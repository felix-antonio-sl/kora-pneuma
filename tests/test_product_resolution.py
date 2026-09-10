from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import yaml

from kora.catalog import Catalog, KoraError, digest
from kora.install import Installer
from kora.product_versions import preserve
from kora.realization import build, installation_effects


class ProductRevisionResolutionTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.root = self.base / "source"
        self.home = self.base / "home"

    def product(self, name, body, requires=()):
        path = self.root / "products/test" / name
        path.mkdir(parents=True)
        (path / "content.md").write_text(body)
        (path / "object.yaml").write_text(yaml.safe_dump({
            "id": f"urn:test:skill:{name}", "kind": "skill", "name": name,
            "description": f"Use {name}", "content": "content.md",
            "targets": ["codex"], "requires": list(requires),
        }))
        return Catalog(self.root).get(f"urn:test:skill:{name}")

    def test_fixed_product_revision_is_realized_after_active_source_changes(self):
        method = self.product("method", "Method A.\n")
        revision = preserve(self.root, method)
        method.content_path.write_text("Method B.\n")
        alpha = self.product("alpha", "Use the fixed method.\n", [
            {"id": method.id, "kind": "product", "revision": revision},
        ])
        files = next(iter(build(Catalog(self.root), "codex", [alpha.id]).values()))
        native = files[".agents/skills/method/SKILL.md"]
        self.assertIn(b"Method A.", native.data)
        self.assertNotIn(b"Method B.", native.data)
        self.assertEqual(native.source["revision"], revision)
        self.assertEqual(native.source["pinned_revision"], revision)

    def test_candidate_review_rejects_a_provider_changed_during_native_validation(self):
        from kora import authoring, render_codex

        method = self.product("method", "Method A.\n")
        alpha = self.product("alpha", "Use the method.\n", [method.id])
        candidate = authoring.revise(self.root, alpha.id, candidate="change")
        original = render_codex._render

        def render_then_change_provider(*args, **kwargs):
            result = original(*args, **kwargs)
            method.content_path.write_text("Method changed during review.\n")
            return result

        with patch.object(render_codex, "_render", side_effect=render_then_change_provider):
            valid, _, errors, _ = authoring._validate_candidate(self.root, candidate)
        self.assertFalse(valid)
        self.assertTrue(any("cambió" in error for error in errors), errors)
        self.assertTrue(candidate.directory.is_dir())

    def test_fixed_consumer_blocks_incompatible_shared_update(self):
        method = self.product("method", "Method A.\n")
        revision = preserve(self.root, method)
        alpha = self.product("alpha", "Use A.\n", [
            {"id": method.id, "kind": "product", "revision": revision},
        ])
        installer = Installer(self.home)
        installer.apply(build(Catalog(self.root), "codex", [alpha.id]))
        method.content_path.write_text("Method B.\n")
        catalog = Catalog(self.root)
        with catalog.phase():
            result = installation_effects(catalog, "codex", [method.id], installer)
        self.assertTrue(any("fijada" in issue["error"] for issue in result["conflicts"]))
        self.assertIn("Method A.", (self.home / ".agents/skills/method/SKILL.md").read_text())

    def test_tampering_with_nondistributed_snapshot_provenance_is_rejected(self):
        method = self.product("method", "Method A.\n")
        original = method.directory / "sources/original.txt"
        original.parent.mkdir()
        original.write_text("Original A.\n")
        metadata = dict(method.metadata)
        metadata["provenance"] = {"sources": [{"path": "sources/original.txt",
                                              "sha256": digest(original.read_bytes())}]}
        (method.directory / "object.yaml").write_text(yaml.safe_dump(metadata))
        method = Catalog(self.root).get(method.id)
        revision = preserve(self.root, method)
        catalog = Catalog(self.root)
        exact = catalog.at_revision(method.id, revision)
        (exact.directory / "sources/original.txt").write_text("Original altered.\n")
        with self.assertRaisesRegex(KoraError, "modificada"):
            catalog.at_revision(method.id, revision)

    def test_prefixed_original_stays_out_of_fixed_revision_distribution(self):
        method = self.product("method", "Method A.\n")
        original = method.directory / "sources/original.txt"
        original.parent.mkdir()
        original.write_text("Original input, preserved for provenance.\n")
        metadata = dict(method.metadata)
        metadata["provenance"] = {"original_path": "products/test/method/sources/original.txt"}
        (method.directory / "object.yaml").write_text(yaml.safe_dump(metadata))
        method = Catalog(self.root).get(method.id)
        revision = preserve(self.root, method)
        exact = Catalog(self.root).at_revision(method.id, revision)
        self.assertTrue((exact.directory / "sources/original.txt").is_file())
        self.assertEqual(method.resources(), exact.resources())
        self.assertNotIn("sources/original.txt", exact.resources())


if __name__ == "__main__":
    unittest.main()
