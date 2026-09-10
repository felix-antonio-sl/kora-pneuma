import json
from pathlib import Path
import tempfile
import unittest

import yaml

from kora.catalog import KoraError
from kora.cli import execute, parser


class PlanBoundaryTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.root = self.base / "source"
        self.home = self.base / "home"
        self.product = self.root / "products/test/method"
        self.product.mkdir(parents=True)
        (self.product / "object.yaml").write_text(yaml.safe_dump({
            "id": "urn:test:skill:method", "name": "method", "kind": "skill",
            "description": "A synthetic method", "content": "content.md", "targets": ["codex"],
        }))
        (self.product / "content.md").write_text("Version one.\n")

    def run_install(self, *options):
        return execute(parser().parse_args([
            "--root", str(self.root), "install", "codex", "urn:test:skill:method",
            "--home", str(self.home), *options,
        ]))

    def preview_file(self):
        plan = self.run_install("--dry-run")
        saved = self.base / "plan.json"
        saved.write_text(json.dumps(plan))
        return saved

    def test_saved_preview_applies_without_source_drift(self):
        saved = self.preview_file()
        result = self.run_install("--plan", str(saved))
        self.assertEqual(result["changed"], [".agents/skills/method/SKILL.md"])

    def test_saved_preview_rejects_changed_source_before_native_writes(self):
        saved = self.preview_file()
        (self.product / "content.md").write_text("Version two.\n")
        with self.assertRaisesRegex(KoraError, "obsoleto"):
            self.run_install("--plan", str(saved))
        self.assertFalse((self.home / ".agents").exists())

    def test_saved_preview_rejects_new_foreign_destination(self):
        saved = self.preview_file()
        native = self.home / ".agents/skills/method/SKILL.md"
        native.parent.mkdir(parents=True)
        native.write_text("Foreign local work.\n")
        with self.assertRaisesRegex(KoraError, "obsoleto"):
            self.run_install("--plan", str(saved))
        self.assertEqual(native.read_text(), "Foreign local work.\n")


if __name__ == "__main__":
    unittest.main()
