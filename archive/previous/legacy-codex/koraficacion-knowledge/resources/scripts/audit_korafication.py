#!/usr/bin/env python3
"""Mechanical audit for DocHumano -> KORA/MD transformations.

This script is a conservative guardrail. It cannot prove semantic FS=100%, but
it catches cheap losses: numbers, dates, URLs, missing frontmatter, bad headings
and obvious labelese. It reports raw CR plus IDC, a contextual dehydration index
calibrated by source profile.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


NUMBER_RE = re.compile(r"(?<![\w])\d+(?:[.,:/-]\d+)*(?![\w])")
DATE_RE = re.compile(
    r"\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}-\d{2}-\d{2}|\d{1,2}\s+de\s+[A-Za-z]+(?:\s+de)?\s+\d{4})\b",
    re.IGNORECASE,
)
URL_RE = re.compile(r"https?://[^\s)>\]]+")
LABEL_HEADING_RE = re.compile(r"^#{1,6}\s+(?:Titulo|Title|Path|Ruta|Tipo|Contenido|Content|Asunto)\s*$", re.IGNORECASE)

PROFILE_EXPECTATIONS = {
    "prosa-redundante": {
        "expected_cr": 1.70,
        "description": "Narrative prose with transitions, rhetoric or repetition.",
    },
    "mixto": {
        "expected_cr": 1.40,
        "description": "Guides, policies or technical notes with prose plus lists/sections.",
    },
    "denso-estructurado": {
        "expected_cr": 1.15,
        "description": "Procedures, norms, tables or documents rich in numbers/dates.",
    },
    "fuente-ya-densa": {
        "expected_cr": 1.00,
        "description": "Already compressed markdown, outlines, glossaries or curated corpus.",
    },
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalize_token(token: str) -> str:
    return token.strip().rstrip(".,;:)").lstrip("(")


def unique_matches(pattern: re.Pattern[str], text: str) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for match in pattern.findall(text):
        token = normalize_token(match)
        if token and token not in seen:
            seen.add(token)
            out.append(token)
    return out


def missing_tokens(source_tokens: list[str], artifact_text: str) -> list[str]:
    normalized_artifact = artifact_text.replace("\u00a0", " ")
    missing: list[str] = []
    for token in source_tokens:
        if token not in normalized_artifact:
            missing.append(token)
    return missing


def markdown_body(text: str) -> str:
    if not text.startswith("---"):
        return text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return text
    return parts[2].lstrip()


def heading_findings(body: str) -> dict:
    truncated: list[str] = []
    labelese: list[str] = []
    primary_headings = 0
    thematic_headings = 0
    for line in body.splitlines():
        if not line.startswith("#"):
            continue
        if re.match(r"^#\s+", line):
            primary_headings += 1
        if re.match(r"^##\s+", line):
            thematic_headings += 1
        if line.rstrip().endswith("..."):
            truncated.append(line.strip())
        if LABEL_HEADING_RE.match(line.strip()):
            labelese.append(line.strip())
    return {
        "primary_headings": primary_headings,
        "thematic_headings": thematic_headings,
        "truncated_headings": truncated,
        "labelese_headings": labelese,
    }


def line_structure_ratio(text: str) -> float:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return 0.0
    structured = 0
    for line in lines:
        if (
            line.startswith(("#", "-", "*", "|"))
            or re.match(r"^\d+[.)]\s+", line)
            or "\t" in line
        ):
            structured += 1
    return structured / len(lines)


def average_line_length(text: str) -> float:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return 0.0
    return sum(len(line) for line in lines) / len(lines)


def infer_source_profile(source: str, numbers: list[str], dates: list[str], urls: list[str]) -> dict:
    chars = max(len(source), 1)
    numeric_density = round((len(numbers) + len(dates) + len(urls)) / chars * 1000, 3)
    structure_ratio = round(line_structure_ratio(source), 3)
    avg_line = round(average_line_length(source), 1)

    if structure_ratio >= 0.45 or numeric_density >= 18:
        profile = "fuente-ya-densa"
    elif structure_ratio >= 0.25 or numeric_density >= 9:
        profile = "denso-estructurado"
    elif structure_ratio >= 0.10 or numeric_density >= 3 or avg_line < 90:
        profile = "mixto"
    else:
        profile = "prosa-redundante"

    return {
        "profile": profile,
        "method": "auto",
        "numeric_density_per_1k": numeric_density,
        "structured_line_ratio": structure_ratio,
        "average_line_length": avg_line,
        **PROFILE_EXPECTATIONS[profile],
    }


def contextual_status(idc: float) -> str:
    if idc >= 1.0:
        return "adequate"
    if idc >= 0.85:
        return "review"
    return "weak"


def audit(source_path: Path, artifact_path: Path, profile_override: str = "auto") -> dict:
    source = read_text(source_path)
    artifact = read_text(artifact_path)
    body = markdown_body(artifact)

    source_chars = len(source)
    artifact_chars = len(artifact)
    cr = round(source_chars / artifact_chars, 3) if artifact_chars else 0

    numbers = unique_matches(NUMBER_RE, source)
    dates = unique_matches(DATE_RE, source)
    urls = unique_matches(URL_RE, source)

    if profile_override == "auto":
        profile = infer_source_profile(source, numbers, dates, urls)
    else:
        profile = {
            "profile": profile_override,
            "method": "manual",
            "numeric_density_per_1k": round((len(numbers) + len(dates) + len(urls)) / max(source_chars, 1) * 1000, 3),
            "structured_line_ratio": round(line_structure_ratio(source), 3),
            "average_line_length": round(average_line_length(source), 1),
            **PROFILE_EXPECTATIONS[profile_override],
        }
    idc = round(cr / profile["expected_cr"], 3) if profile["expected_cr"] else 0
    idc_status = contextual_status(idc)

    missing_numbers = missing_tokens(numbers, artifact)
    missing_dates = missing_tokens(dates, artifact)
    missing_urls = missing_tokens(urls, artifact)
    headings = heading_findings(body)

    failures: list[str] = []
    warnings: list[str] = []
    if not artifact.startswith("---"):
        failures.append("frontmatter ausente")
    if missing_numbers:
        failures.append("cifras/tokens numericos ausentes")
    if missing_dates:
        failures.append("fechas ausentes")
    if missing_urls:
        failures.append("URLs ausentes")
    if headings["truncated_headings"]:
        failures.append("headings truncados")
    if headings["labelese_headings"]:
        failures.append("labelese en headings")
    if idc_status == "review":
        warnings.append("IDC bajo 1.0; revisar perfil, fat residual o redundancia")
    if idc_status == "weak":
        warnings.append("IDC bajo 0.85; revisar deshidratacion antes de aceptar")
    if headings["primary_headings"] != 1:
        warnings.append("se esperaba exactamente un heading # primario")
    if headings["thematic_headings"] < 1:
        warnings.append("se esperaba al menos un heading ## tematico")

    status = "fail" if failures else "warn" if warnings else "pass"
    return {
        "status": status,
        "source": str(source_path),
        "artifact": str(artifact_path),
        "source_chars": source_chars,
        "artifact_chars": artifact_chars,
        "compression_ratio": cr,
        "contextual_dehydration": {
            "index": idc,
            "status": idc_status,
            **profile,
        },
        "mechanical_checks": {
            "source_numeric_tokens": len(numbers),
            "missing_numeric_tokens": missing_numbers,
            "source_dates": len(dates),
            "missing_dates": missing_dates,
            "source_urls": len(urls),
            "missing_urls": missing_urls,
            **headings,
        },
        "failures": failures,
        "warnings": warnings,
        "note": "Mechanical audit only; semantic FS still requires source-vs-artifact fact ledger.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit KORA/MD korafication against source.")
    parser.add_argument("source", type=Path)
    parser.add_argument("artifact", type=Path)
    parser.add_argument(
        "--profile",
        choices=("auto", *PROFILE_EXPECTATIONS.keys()),
        default="auto",
        help="Source profile for contextual dehydration index (IDC).",
    )
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    report = audit(args.source, args.artifact, profile_override=args.profile)
    if args.as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"status: {report['status']}")
        print(f"CR: {report['compression_ratio']}")
        cdi = report["contextual_dehydration"]
        print(f"IDC: {cdi['index']} ({cdi['status']}; profile={cdi['profile']}, expected_cr={cdi['expected_cr']})")
        for failure in report["failures"]:
            print(f"FAIL: {failure}")
        for warning in report["warnings"]:
            print(f"WARN: {warning}")
    return 1 if report["status"] == "fail" else 0


if __name__ == "__main__":
    raise SystemExit(main())
