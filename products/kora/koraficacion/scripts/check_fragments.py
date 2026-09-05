#!/usr/bin/env python3
"""Check selected literal fragments in source and output; never certify semantics."""
import argparse
import json
from pathlib import Path
import re


def normalize(text):
    return re.sub(r"\s+", " ", text).strip()


def inspect(source, output, units):
    source, output = normalize(source), normalize(output)
    return {"selected_fragments": len(units),
            "absent_from_source": [index for index, unit in enumerate(units, 1)
                                   if normalize(unit) not in source],
            "absent_from_output": [index for index, unit in enumerate(units, 1)
                                   if normalize(unit) not in output],
            "scope": "Literal containment after whitespace normalization; no semantic verdict."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("fragments", type=Path)
    args = parser.parse_args()
    try:
        units = [line.strip() for line in args.fragments.read_text(encoding="utf-8").splitlines()
                 if line.strip()]
        if not units:
            parser.error("The selected fragment list is empty")
        result = inspect(args.source.read_text(encoding="utf-8"),
                         args.output.read_text(encoding="utf-8"), units)
    except (OSError, UnicodeError):
        parser.error("Cannot read one of the supplied text files")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["absent_from_source"] or result["absent_from_output"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
