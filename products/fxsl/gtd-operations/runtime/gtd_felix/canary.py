"""Synthetic native-resource witness; never reads configuration or personal state."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


def run_canary(identifier: str, destination: Path, native_instructions: Path) -> dict:
    """Create one exclusive marker in an existing, explicitly selected directory."""
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", identifier):
        raise ValueError("identifier must be 1-64 ASCII letters, digits, '_' or '-'")
    destination = destination.resolve(strict=True)
    if not destination.is_dir():
        raise ValueError("destination must be an existing directory")
    native_instructions = native_instructions.resolve(strict=True)
    native_digest = hashlib.sha256(native_instructions.read_bytes()).hexdigest()
    helper = Path(__file__).resolve(strict=True)
    receipt = {
        "synthetic": True,
        "identifier": identifier,
        "native_path": str(native_instructions),
        "native_sha256": native_digest,
        "helper_path": str(helper),
        "helper_sha256": hashlib.sha256(helper.read_bytes()).hexdigest(),
        "marker_path": str(destination / f"gtd-canary-{identifier}.json"),
    }
    encoded = json.dumps(receipt, ensure_ascii=False, sort_keys=True) + "\n"
    # Exclusive creation also refuses an existing symlink; never replaces a marker.
    with Path(receipt["marker_path"]).open("x", encoding="utf-8") as marker:
        marker.write(encoded)
    return receipt


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--identifier", required=True)
    parser.add_argument("--destination", required=True, type=Path)
    parser.add_argument("--native-instructions", required=True, type=Path)
    args = parser.parse_args()
    try:
        receipt = run_canary(args.identifier, args.destination, args.native_instructions)
    except (OSError, ValueError):
        parser.exit(2, "Canario no aplicado: revise identificador, recursos y destino explícito.\n")
    print(json.dumps(receipt, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
