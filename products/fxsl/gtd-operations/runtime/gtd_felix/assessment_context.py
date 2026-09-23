"""Bounded, read-only evidence preparation for structured GTD assessments.

Candidate passages are deterministic lexical suggestions only. They do not
establish relevance, entailment, sufficiency, privacy or permission.
"""
import json
import re


PACKAGE_LIMIT = 24_000
PER_SOURCE_SCAN_LIMIT = 250_000
GLOBAL_SCAN_LIMIT = 2_000_000
PASSAGE_LIMIT = 2_000
WINDOW_SIZE = 1_800
MAX_CANDIDATES_PER_SOURCE = 2

_WORD = re.compile(r"[^\W_]{3,}", re.UNICODE)
_PARAGRAPH_BREAK = re.compile(r"(?:\r?\n[ \t]*){2,}")
_STOPWORDS = frozenset({
    "a", "al", "algo", "algunas", "algunos", "ante", "como", "con", "contra", "cual", "cuando",
    "de", "del", "desde", "donde", "durante", "e", "el", "ella", "ellas", "ello", "ellos", "en",
    "entre", "era", "eran", "es", "esa", "esas", "ese", "eso", "esos", "esta", "estaba", "estaban",
    "estado", "estados", "estamos", "estan", "estar", "estas", "este", "esto", "estos", "fue", "fueron",
    "ha", "habia", "hace", "hacia", "han", "hasta", "hay", "he", "la", "las", "le", "les", "lo", "los",
    "mas", "me", "mi", "mis", "mucho", "muy", "no", "nos", "nuestra", "nuestras", "nuestro", "nuestros",
    "o", "para", "pero", "poco", "por", "porque", "que", "quien", "quienes", "se", "sea", "ser", "si",
    "sin", "sobre", "son", "su", "sus", "tambien", "te", "tiene", "tienen", "todo", "todos", "tras", "tu",
    "tus", "un", "una", "unas", "uno", "unos", "usted", "ustedes", "y", "the", "and", "for", "from",
    "with", "that", "this", "are", "was", "were", "will", "have", "has", "had", "not", "but", "you", "your",
})


def _byte_size(value):
    # Match aiohttp.web.json_response's default json.dumps serialization.
    return len(json.dumps(value, allow_nan=False).encode("utf-8"))


def _terms(text):
    return [match.group(0).casefold() for match in _WORD.finditer(text)
            if match.group(0).casefold() not in _STOPWORDS]


def _query_weights(criterion, material_text):
    weights = {}
    for word in _terms(material_text):
        weights[word] = min(8, weights.get(word, 0) + 1)
    for word in _terms(criterion):
        weights[word] = min(12, weights.get(word, 0) + 3)
    ordered = sorted(weights, key=lambda word: (-weights[word], word))
    limited = len(ordered) > 4096
    if limited:
        ordered = ordered[:4096]
    return {word: weights[word] for word in ordered}, limited


def _paragraph_spans(text):
    """Yield nonblank paragraph spans as exact codepoint offsets."""
    start = 0
    for match in _PARAGRAPH_BREAK.finditer(text):
        left, right = start, match.start()
        while left < right and text[left].isspace():
            left += 1
        while right > left and text[right - 1].isspace():
            right -= 1
        if left < right:
            yield left, right
        start = match.end()
    left, right = start, len(text)
    while left < right and text[left].isspace():
        left += 1
    while right > left and text[right - 1].isspace():
        right -= 1
    if left < right:
        yield left, right


def _candidate_windows(text, scanned_length, weights):
    spans = []
    for start, end in _paragraph_spans(text[:scanned_length]):
        length = end - start
        if length <= PASSAGE_LIMIT:
            spans.append((start, end))
            continue
        window_start = start
        while window_start < end:
            window_end = min(window_start + WINDOW_SIZE, end)
            spans.append((window_start, window_end))
            window_start = window_end

    ranked = []
    for start, end in spans:
        quote = text[start:end]
        if not quote or len(quote) > PASSAGE_LIMIT:
            continue
        found = _terms(quote)
        if not found:
            continue
        counts = {}
        for word in found:
            counts[word] = counts.get(word, 0) + 1
        matched = set(counts) & set(weights)
        if not matched:
            continue
        weighted_hits = sum(min(counts[word], 4) * weights[word] for word in matched)
        ranked.append((-weighted_hits, -len(matched), -sum(counts[word] for word in matched), start, end, quote))
    ranked.sort()
    selected = []
    for candidate in ranked:
        _, _, _, start, end, quote = candidate
        if any(start < chosen_end and end > chosen_start for chosen_start, chosen_end, _ in selected):
            continue
        selected.append((start, end, quote))
        if len(selected) == MAX_CANDIDATES_PER_SOURCE:
            break
    return selected, len(ranked)


def build_assessment_context(service, item, material_id, version, *, can_read_source):
    """Build a complete bounded package from current store state; never writes."""
    if (not isinstance(item, dict) or not isinstance(item.get("id"), str)
            or not isinstance(material_id, str) or not material_id or type(version) is not int or version < 1):
        raise ValueError("invalid_assessment_context_request")
    criterion = item.get("completion_criteria")
    if not isinstance(criterion, str) or not criterion.strip():
        raise ValueError("assessment_context_criterion_required")
    materials = service.materials(item["id"])
    material = next((entry for entry in materials
                     if entry.get("id") == material_id and entry.get("version") == version), None)
    if material is None:
        raise ValueError("assessment_context_material_not_found")
    if not material.get("valid"):
        raise ValueError("assessment_context_material_stale")
    read = service.read_material(item["id"], material_id, version)
    if not read.get("valid"):
        raise ValueError("assessment_context_material_stale")

    required = item.get("source_versions", {})
    if not isinstance(required, dict):
        raise ValueError("assessment_context_requirements_invalid")
    required = dict(required)
    material_sources = material.get("source_versions", {})
    if not isinstance(material_sources, dict):
        raise ValueError("assessment_context_requirements_invalid")
    required.update(material_sources)
    routed = service._routed_material_requirements(item)
    required.update(routed)
    if (any(not isinstance(sid, str) or not sid or type(revision) is not int or revision < 1
            for sid, revision in required.items())):
        raise ValueError("assessment_context_requirements_invalid")

    from .decisions import ASSESSMENT_MAX_PASSAGES
    if len(required) > ASSESSMENT_MAX_PASSAGES:
        raise ValueError("assessment_context_source_count_exceeds_passage_limit")

    sources = []
    for source_id in sorted(required):
        source = service.get_item(source_id)
        if source is None or not can_read_source(source_id, source):
            raise ValueError("assessment_context_source_unavailable")
        revisions = source.get("source_revisions", [])
        if not isinstance(revisions, list) or len(revisions) != required[source_id]:
            raise ValueError("assessment_context_source_revision_stale")
        revision_text = revisions[-1].get("text") if revisions and isinstance(revisions[-1], dict) else None
        if not isinstance(revision_text, str):
            revision_text = None
        entry = {"source_id": source_id, "source_revision": required[source_id], "status": "current",
                 "candidates": [], "candidate_omissions": []}
        if source_id in routed:
            if revision_text is None:
                raise ValueError("assessment_context_human_source_unavailable")
            entry["human_text"] = revision_text
        entry["_text"] = revision_text
        sources.append(entry)

    package = {
        "schema": 1,
        "item": {"id": item["id"], "version": item["version"]},
        "criterion": criterion,
        "material": {"id": material_id, "version": version, "sha256": read["sha256"],
                     "text": read["content"]},
        "required_sources": [{k: v for k, v in entry.items() if k != "_text"} for entry in sources],
        "candidate_order": "Lexical overlap only: criterion terms count x3, material terms x1; then matched distinct terms and source offset.",
        "notice": ("Candidate excerpts are suggestions, not proof of relevance or sufficiency. Inspect each source and quote before gtd_decide. "
                   "Pass only the nested candidate.passage object; remove offsets and ranking metadata. Review for clinical identifiers and exclude any unnecessary sensitive text. "
                   "The full source remains available with gtd_read view=item. This package never calls Jev or changes the item."),
    }
    if _byte_size(package) > PACKAGE_LIMIT:
        raise ValueError("assessment_context_package_too_large")

    weights, query_limited = _query_weights(criterion, read["content"])
    package["query_terms_limited"] = query_limited
    total_scanned = 0
    for index, entry in enumerate(sources):
        text = entry.pop("_text")
        output_entry = package["required_sources"][index]
        if text is None:
            output_entry["candidate_omissions"].append({"reason": "current_revision_has_no_text"})
            continue
        remaining = GLOBAL_SCAN_LIMIT - total_scanned
        scanned = min(len(text), PER_SOURCE_SCAN_LIMIT, max(0, remaining))
        total_scanned += scanned
        if scanned == 0:
            output_entry["candidate_omissions"].append({"reason": "global_source_scan_limit"})
            continue
        candidates, matched_windows = _candidate_windows(text, scanned, weights)
        truncated = scanned < len(text)
        if not candidates:
            reason = "no_query_terms" if not weights else "no_lexical_match"
            output_entry["candidate_omissions"].append({"reason": reason})
        if truncated:
            output_entry["candidate_omissions"].append({"reason": "source_scan_limit",
                                                        "scanned_characters": scanned,
                                                        "total_characters": len(text)})
        if matched_windows > len(candidates):
            output_entry["candidate_omissions"].append({"reason": "per_source_selection_limit",
                                                        "count": matched_windows - len(candidates)})
        for start, end, quote in candidates:
            output_entry["candidates"].append({
                "passage": {"source_id": entry["source_id"],
                            "source_revision": entry["source_revision"], "quote": quote},
                "offsets": {"start": start, "end": end, "unit": "unicode_codepoint"},
            })
            if _byte_size(package) > PACKAGE_LIMIT:
                output_entry["candidates"].pop()
                output_entry["candidate_omissions"].append({"reason": "package_byte_limit", "count": 1})
    if _byte_size(package) > PACKAGE_LIMIT:
        raise ValueError("assessment_context_package_too_large")
    return package
