"""Deterministic authoring-resource tests; not a claim of model behavior."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from runtime_location import RUNTIME

HELPER = RUNTIME / 'gtd_felix/canary.py'
spec = importlib.util.spec_from_file_location("gtd_canary_under_test", HELPER)
canary = importlib.util.module_from_spec(spec)
spec.loader.exec_module(canary)


class CanaryTests(unittest.TestCase):
    def test_marker_and_native_hash_match_exact_bytes(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            native = root / "SKILL.md"
            native.write_bytes(b"synthetic native instructions\n")
            destination = root / "markers"
            destination.mkdir()
            receipt = canary.run_canary("synthetic-01", destination, native)
            marker = destination / "gtd-canary-synthetic-01.json"
            self.assertEqual(json.loads(marker.read_text()), receipt)
            self.assertEqual(receipt["native_path"], str(native.resolve()))
            self.assertEqual(receipt["native_sha256"], hashlib.sha256(native.read_bytes()).hexdigest())
            self.assertEqual(receipt["helper_sha256"], hashlib.sha256(HELPER.read_bytes()).hexdigest())
            self.assertEqual(list(destination.iterdir()), [marker])

    def test_refuses_path_traversal_and_overwrite(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            native = root / "SKILL.md"
            native.write_text("synthetic")
            for invalid in ("../escape", "/absolute", "a/b", "", "x" * 65):
                with self.assertRaises(ValueError):
                    canary.run_canary(invalid, root, native)
            receipt = canary.run_canary("once", root, native)
            before = Path(receipt["marker_path"]).read_bytes()
            with self.assertRaises(FileExistsError):
                canary.run_canary("once", root, native)
            self.assertEqual(Path(receipt["marker_path"]).read_bytes(), before)

    def test_missing_resource_and_destination_do_not_write(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            with self.assertRaises(FileNotFoundError):
                canary.run_canary("missing", root, root / "missing.md")
            self.assertEqual(list(root.iterdir()), [])
            with self.assertRaises(FileNotFoundError):
                canary.run_canary("missing", root / "absent", HELPER)
            self.assertFalse((root / "absent").exists())

    def test_cli_requires_explicit_paths_and_reports_missing_resource(self):
        for arguments in ([], ["--identifier", "test"]):
            result = subprocess.run([sys.executable, str(HELPER), *arguments], capture_output=True)
            self.assertEqual(result.returncode, 2)
        with tempfile.TemporaryDirectory() as temporary:
            result = subprocess.run([sys.executable, str(HELPER), "--identifier", "test",
                                     "--destination", temporary, "--native-instructions",
                                     str(Path(temporary) / "missing")], capture_output=True)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(result.stdout, b"")
            self.assertEqual(list(Path(temporary).iterdir()), [])

    def test_changed_native_resource_changes_observed_hash(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            native = root / "SKILL.md"
            native.write_text("synthetic v1")
            first = canary.run_canary("v1", root, native)
            native.write_text("synthetic v2")
            second = canary.run_canary("v2", root, native)
            self.assertNotEqual(first["native_sha256"], second["native_sha256"])


if __name__ == "__main__":
    unittest.main()
