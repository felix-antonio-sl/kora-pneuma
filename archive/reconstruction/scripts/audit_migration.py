#!/usr/bin/env python3
"""Independently compare preserved originals, live inputs, and current references.

This audit deliberately does not import the migration implementation. It never
writes its inputs. Optional detailed locators belong only in a private report.
"""

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys

import yaml


HISTORICAL_REFERENCES = {
    "urn:kora:kb:spec:1.0.0": "Referencia histórica al formato KODA; sin objeto actual.",
    "urn:kora:kb:transform:1.0.0": "Referencia histórica al método de transformación; sin objeto actual.",
    "urn:gorenuble:gn:bpmn-c4:1.0.0": "Marco BPMN/C4 citado sin objeto recuperado que declare esa identidad.",
}
BODY_ALIASES = {
    "urn:salud:kb:hsc-gcl-1-2-vias-venosas-centrales": "urn:salud:kb:hsc-gcl-1-2-vias-venosas-centrales-2025",
    "urn:salud:kb:hsc-mo-2q-tele-organizacion-unidad-telemedicina": "urn:salud:kb:hsc-mo-2q-tele-organizacion-unidad-telemedicina-2023",
}
EXTERNAL_SOURCE = re.compile(
    r"/home/felix/kora-external-sources/[^;\n()]+?"
    r"\.(?:pdf|md|txt|yml|yaml|json|ttl|xml|docx|csv|tsv|opl)(?=\s|;|\)|$)"
)
PRIVATE_NAMES = {
    ".remember", ".git", ".env", ".sessions", "sessions", "memories",
    "credentials", "credentials.json", "auth.json", "secrets", "secrets.json",
}
RELATION_FIELDS = ("cita", "depende", "refina", "reemplaza", "conocimiento", "componible")


class AuditError(Exception):
    """Invalid audit input; do not include source payloads in the error."""


class MappingLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str) or key in result:
            raise AuditError("YAML contains duplicate or non-text keys")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


MappingLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def mapping(data):
    try:
        result = yaml.load(data, Loader=MappingLoader)
    except (yaml.YAMLError, UnicodeError) as error:
        raise AuditError("Invalid YAML") from error
    if not isinstance(result, dict):
        raise AuditError("Expected YAML mapping")
    return result


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def relative_path(value):
    if not isinstance(value, str) or not value or "\\" in value:
        raise AuditError("Invalid relative path")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in ("", ".", "..") for part in value.split("/")):
        raise AuditError("Path escapes audit input")
    return Path(*path.parts)


@dataclass(frozen=True)
class Snapshot:
    data: bytes
    mode: int
    stamp: tuple

    @property
    def digest(self):
        return sha256(self.data)


class Reader:
    def __init__(self):
        self.files = {}

    def read(self, path):
        path = Path(path)
        if path in self.files:
            return self.files[path]
        before = path.lstat()
        if not stat.S_ISREG(before.st_mode):
            raise AuditError("Audit input must be a regular file")
        with path.open("rb") as stream:
            data = stream.read()
            after = os.fstat(stream.fileno())
        first = (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns, before.st_ctime_ns)
        last = (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns, after.st_ctime_ns)
        if first != last:
            raise AuditError("Input changed during read")
        value = Snapshot(data, stat.S_IMODE(after.st_mode), last)
        self.files[path] = value
        return value

    def changes(self):
        changed = []
        fresh = Reader()
        for path, original in self.files.items():
            try:
                current = fresh.read(path)
                if current != original:
                    changed.append(path)
            except (OSError, AuditError):
                changed.append(path)
        return changed


def files_under(root):
    files, omitted = [], []
    if not root.is_dir() or root.is_symlink():
        raise AuditError("Missing or linked source directory")
    for directory, folders, names in os.walk(root, followlinks=False):
        directory = Path(directory)
        for name in list(folders):
            path = directory / name
            if name in PRIVATE_NAMES or path.is_symlink():
                omitted.append(path)
                folders.remove(name)
        for name in names:
            path = directory / name
            if name in PRIVATE_NAMES or path.is_symlink():
                omitted.append(path)
            else:
                files.append(path)
    return sorted(files), sorted(omitted)


def frontmatter(data):
    lines = data.splitlines(keepends=True)
    if not lines or lines[0].strip() != b"---":
        raise AuditError("Original has no frontmatter")
    for index in range(1, len(lines)):
        if lines[index].strip() == b"---":
            return mapping(b"".join(lines[1:index])), b"".join(lines[index + 1:])
    raise AuditError("Unclosed original frontmatter")


def entry_kind(path):
    parts = path.parts
    if len(parts) == 4 and parts[0] == "artefactos" and path.suffix == ".md":
        return {"conocimiento": "knowledge", "agentes": "agent"}.get(parts[1])
    if len(parts) == 5 and parts[:2] == ("artefactos", "skills") and path.name == "SKILL.md":
        return "skill"
    return None


def audit(source, root):
    """Return (shareable summary, private details); source and root are read-only."""
    source, root = Path(source).resolve(), Path(root).resolve()
    if source == root:
        raise AuditError("Use the preserved legacy tree, not the successor itself")
    reader = Reader()
    issues, deltas = [], []
    original_files, omitted = files_under(source / "artefactos")
    live = {path.relative_to(source).as_posix(): reader.read(path) for path in original_files}
    entries = {path: entry_kind(Path(path)) for path in live if entry_kind(Path(path))}
    resources = set(live) - set(entries)
    wrappers, wrapper_paths = defaultdict(list), []
    other_provenances = 0
    current_counts = {}
    for section in ("products", "archive/products", "archive/previous"):
        paths = sorted((root / section).rglob("object.yaml"))
        current_counts[section] = len(paths)
        wrapper_paths.extend(paths)
        for path in paths:
            metadata = mapping(reader.read(path).data)
            provenance = metadata.get("provenance", {})
            source_path = provenance.get("source_path")
            if source_path:
                relative_path(source_path)
                if entry_kind(Path(source_path)):
                    wrappers[source_path].append((path, metadata))
                else:
                    other_provenances += 1
    selected, from_previous = {}, 0
    for source_path, candidates in wrappers.items():
        previous = [x for x in candidates if x[0].is_relative_to(root / "archive/previous")]
        choices = previous or candidates
        if len(choices) != 1:
            issues.append({"check": "ambiguous_original", "source": source_path})
            continue
        selected[source_path] = choices[0]
        from_previous += bool(previous)
    for path in sorted(set(selected) ^ set(entries)):
        issues.append({"check": "original_coverage", "source": path,
                       "in_source": path in entries, "in_preserved": path in selected})

    def compare(path, preserved, item):
        current = live[path]
        if preserved.data != current.data or preserved.mode != current.mode:
            deltas.append({"source": path, "item": item,
                           "preserved_sha256": preserved.digest, "live_sha256": current.digest,
                           "preserved_bytes": len(preserved.data), "live_bytes": len(current.data),
                           "preserved_mode": oct(preserved.mode), "live_mode": oct(current.mode)})

    originals, preserved_count, resource_count = {}, 0, 0
    expected_aliases = {}
    historical = defaultdict(set)
    external = defaultdict(list)
    relation_count = 0
    for source_path in sorted(set(selected) & set(entries)):
        wrapper, metadata = selected[source_path]
        content = wrapper.parent / relative_path(metadata["content"])
        body = reader.read(content)
        provenance = metadata["provenance"]
        if metadata["kind"] != entries[source_path]:
            issues.append({"check": "kind", "source": source_path})
        raw = body.data
        if metadata["kind"] != "knowledge":
            header = provenance.get("legacy_header")
            if not isinstance(header, str):
                raise AuditError("Consumable original lacks its literal header")
            raw = header.encode("utf-8") + raw
        if sha256(raw) != provenance.get("source_sha256"):
            issues.append({"check": "preserved_original_digest", "source": source_path})
        else:
            preserved_count += 1
        compare(source_path, Snapshot(raw, body.mode, ()), "original")
        original, original_body = frontmatter(raw)
        identifier = original["urn"]
        originals[source_path] = {"id": identifier, "wrapper": wrapper, "metadata": original,
                                  "body": original_body}
        if identifier != metadata["id"]:
            issues.append({"check": "identity", "source": source_path})
        original_relations = {key: original[key] for key in RELATION_FIELDS if original.get(key)}
        if original_relations != {k: v for k, v in metadata.get("relations", {}).items() if v}:
            issues.append({"check": "preserved_relations", "source": source_path})
        relation_count += sum(len(value) for value in original_relations.values())
        provenance_text = str(original.get("fuente", ""))
        for old_id in re.findall(r"URN KODA legado (urn:[a-zA-Z0-9:._/-]+)", provenance_text):
            if old_id in expected_aliases and expected_aliases[old_id] != identifier:
                issues.append({"check": "ambiguous_legacy_alias", "id": old_id})
            expected_aliases[old_id] = identifier
        text = original_body.decode("utf-8")
        for old_id in HISTORICAL_REFERENCES:
            if re.search(re.escape(old_id) + r"(?![a-zA-Z0-9:._/-])", text):
                historical[old_id].add(identifier)
        for match in EXTERNAL_SOURCE.finditer(provenance_text):
            tail = provenance_text[match.end():match.end() + 160]
            declared = re.search(r"sha256\s*:\s*([0-9a-f]{64})", tail)
            external[match.group()].append({"used_by": identifier,
                                            "declared_sha256": declared.group(1) if declared else None})

    skill_folders = {str(Path(path).parent): wrapper.parent
                     for path, (wrapper, metadata) in selected.items() if metadata["kind"] == "skill"}
    for path in sorted(resources):
        owners = [folder for folder in skill_folders if Path(path).is_relative_to(folder)]
        if len(owners) != 1:
            issues.append({"check": "resource_owner", "source": path})
            continue
        folder = owners[0]
        destination = skill_folders[folder] / Path(path).relative_to(folder)
        try:
            resource = reader.read(destination)
        except (OSError, AuditError):
            issues.append({"check": "resource_missing", "source": path})
            continue
        compare(path, resource, "resource")
        resource_count += 1

    sys.path.insert(0, str(root))
    from kora.catalog import Catalog, KoraError

    if (root / "aliases.yaml").exists():
        reader.read(root / "aliases.yaml")
    try:
        catalog = Catalog(root)
    except KoraError as error:
        raise AuditError("Current catalog cannot be checked") from error
    current_issues = catalog.reference_issues()
    issues.extend({"check": "current_metadata_reference", **item} for item in current_issues)
    dependency_checks = 0
    for product in catalog.products.values():
        reader.read(product.content_path)
        for target in product.targets or ("codex", "hermes"):
            try:
                catalog.dependencies(product, target)
            except KoraError:
                issues.append({"check": "current_dependency", "id": product.id, "target": target})
            dependency_checks += 1
    expected_aliases.update(BODY_ALIASES)
    for alias, identifier in expected_aliases.items():
        try:
            correct = catalog.get(alias).id == identifier
        except KoraError:
            correct = False
        if not correct:
            issues.append({"check": "preserved_alias", "id": alias})
    link_targets = {}
    for path, item in originals.items():
        if entries[path] != "knowledge":
            continue
        link = root / path
        try:
            target = os.readlink(link)
            link_targets[path] = target
            if link.resolve(strict=True) != catalog.get(item["id"]).content_path.resolve(strict=True):
                raise AuditError("Wrong reading target")
        except (OSError, KoraError, AuditError):
            issues.append({"check": "reading_link", "source": path})

    external_details = []
    for location, uses in sorted(external.items()):
        record = {"location": location, "role": "Fuente declarada por productos conservados", "uses": uses}
        try:
            item = reader.read(Path(location))
            record.update({"exists": True, "sha256": item.digest, "bytes": len(item.data),
                           "declared_hashes_match": all(use["declared_sha256"] == item.digest for use in uses)})
        except (OSError, AuditError):
            record.update({"exists": False, "declared_hashes_match": False})
        if not record["declared_hashes_match"]:
            issues.append({"check": "external_source", "used_by": sorted({use["used_by"] for use in uses}),
                           "exists": record["exists"]})
        external_details.append(record)
    for identifier in HISTORICAL_REFERENCES:
        try:
            catalog.get(identifier)
        except KoraError:
            continue
        issues.append({"check": "historical_exception_now_resolvable", "id": identifier})

    recovered = []
    for product in (*catalog.products.values(), *catalog.archived.values()):
        for record in product.metadata.get("provenance", {}).get("sources", []):
            path = product.directory / relative_path(record["path"])
            try:
                intact = reader.read(path).digest == record.get("sha256")
            except (OSError, AuditError):
                intact = False
            recovered.append({"id": product.id, "path": record["path"], "sha256_matches": intact})
            if not intact:
                issues.append({"check": "recovered_source", "id": product.id})

    changed = reader.changes()
    final_source_paths, final_omitted = files_under(source / "artefactos")
    if original_files != final_source_paths or omitted != final_omitted:
        issues.append({"check": "source_file_set_changed_during_audit"})
    final_wrappers = sorted(path for section in ("products", "archive/products", "archive/previous")
                            for path in (root / section).rglob("object.yaml"))
    if sorted(wrapper_paths) != final_wrappers:
        issues.append({"check": "wrapper_set_changed_during_audit"})
    for path, target in link_targets.items():
        try:
            unchanged = os.readlink(root / path) == target
        except OSError:
            unchanged = False
        if not unchanged:
            issues.append({"check": "reading_link_changed_during_audit", "source": path})
    if changed:
        issues.append({"check": "files_changed_during_audit", "count": len(changed)})
    if omitted:
        issues.append({"check": "unread_private_or_linked_inputs", "count": len(omitted)})
    summary = {
        "status": "differences" if issues or deltas else "ok",
        "source_files": len(live), "source_bytes": sum(len(item.data) for item in live.values()),
        "originals": len(entries), "originals_digest_verified": preserved_count,
        "originals_selected_from_previous": from_previous,
        "resources": len(resources), "resources_compared": resource_count,
        "original_relations_preserved": relation_count,
        "reading_links": len(link_targets), "expected_aliases": len(expected_aliases),
        "current_aliases": len(catalog.aliases), "current_objects": current_counts,
        "wrappers_from_other_provenances": other_provenances,
        "current_metadata_reference_issues": len(current_issues), "current_dependency_checks": dependency_checks,
        "external_sources": len(external), "external_source_uses": sum(map(len, external.values())),
        "external_sources_existing": sum(item["exists"] for item in external_details),
        "external_sources_hash_verified": sum(item["declared_hashes_match"] for item in external_details),
        "external_source_formats": dict(sorted(Counter(Path(path).suffix for path in external).items())),
        "historical_references": [{
            "id": identifier, "original_documents": len(historical[identifier]),
            "documents_with_verified_external_source": len({
                use["used_by"] for item in external_details if item["declared_hashes_match"]
                for use in item["uses"] if use["used_by"] in historical[identifier]
            }), "exception": reason} for identifier, reason in HISTORICAL_REFERENCES.items()],
        "recovered_sources": recovered,
        "live_source_deltas": deltas, "issues": issues,
        "limits": "Compara preservación material y referencias declaradas; no acredita fidelidad semántica, instalación ni conducta.",
    }
    details = {"summary": summary, "external_sources": external_details,
               "historical_reference_documents": {key: sorted(value) for key, value in historical.items()},
               "changed_during_audit": [str(path) for path in changed]}
    return summary, details


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Árbol legado preservado, con artefactos originales")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--details", type=Path, help="Informe privado nuevo dentro de ROOT/._local")
    args = parser.parse_args()
    try:
        summary, details = audit(args.source, args.root)
        if args.details:
            destination = args.details.resolve()
            if not destination.is_relative_to(args.root.resolve() / "._local"):
                raise AuditError("Detailed report must be inside ROOT/._local")
            destination.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
            descriptor = os.open(destination, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
            with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                json.dump(details, stream, ensure_ascii=False, indent=2)
                stream.write("\n")
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0 if summary["status"] == "ok" else 1
    except (AuditError, OSError, KeyError, TypeError, ValueError) as error:
        print(json.dumps({"status": "error", "error_type": type(error).__name__,
                          "message": "No se pudo completar la auditoría; los insumos no se modificaron."}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
