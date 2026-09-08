#!/usr/bin/env python3
"""Run KORA from any working directory without an editable package install."""

from kora.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
