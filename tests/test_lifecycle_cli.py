import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from kora.catalog import KoraError
from kora.cli import execute, parser


class LifecycleCliTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.root = self.base / "machinery"
        self.library = self.base / "library"
        self.home = self.base / "native"
        self.body = self.base / "body.md"
        self.body.write_text("Condición A; excepción B; dato ausente UNKNOWN.\n")

    def cli(self, *args):
        return execute(parser().parse_args([
            "--root", str(self.root), "--knowledge-root", str(self.library),
            *[str(value) for value in args],
        ]))

    def create(self, kind, name, *args):
        return self.cli("create", kind, "test", name, "--id", f"urn:test:{kind}:{name}",
                        "--description", f"Usar {name}", "--body", self.body, *args)

    def test_prepare_admit_update_exact_revision_install_and_recover(self):
        item = self.create("skill", "method", "--prepare-only", "--candidate", "first")
        self.assertEqual(item["state"], "candidate")
        self.assertFalse((self.root / "products/test/method").exists())
        review = self.cli("review", item["id"], "--candidate", "first")
        self.assertTrue(review["realizable"])
        first = self.cli("admit", item["id"], "--candidate", "first",
                         "--reviewed", review["reviewed_sha256"])
        original = Path(first["path"]).read_bytes()
        alias = "urn:test:skill:former-method"
        self.cli("alias", alias, item["id"])
        self.assertEqual(self.cli("resolve", alias)["id"], item["id"])

        for target in ("codex", "hermes"):
            self.cli("install", target, alias, "--home", self.home)
        revised = self.cli("revise", alias, "--candidate", "second")
        Path(revised["path"]).write_text("Condición C; excepción B; dato ausente UNKNOWN.\n")
        reviewed = self.cli("review", alias, "--candidate", "second")
        second = self.cli("admit", alias, "--candidate", "second",
                          "--reviewed", reviewed["reviewed_sha256"])
        self.assertNotEqual(second["revision"], first["revision"])
        exact = self.cli("resolve", alias, "--revision", first["revision"])
        self.assertEqual(Path(exact["path"]).read_bytes(), original)

        for target in ("codex", "hermes"):
            plan = self.cli("install", target, alias, "--home", self.home, "--dry-run")
            saved = self.base / f"{target}-plan.json"
            saved.write_text(json.dumps(plan))
            self.cli("install", target, alias, "--home", self.home, "--plan", saved)
        status = self.cli("status", "--home", self.home, "--compare-source", "--id", item["id"])
        self.assertEqual(status["changes"], [])
        self.assertTrue(all(row["source_state"] == "current" for row in status["source_comparison"]))
        self.cli("remove", "codex", alias, "--home", self.home)
        self.cli("rollback", "--home", self.home)
        self.assertEqual(self.cli("status", "--home", self.home)["changes"], [])

    def test_two_knowledge_candidates_and_retirement_include_machine_consumers(self):
        draft = self.create("knowledge", "rule")
        reviewed = self.cli("review", draft["id"])
        first = self.cli("approve", draft["id"], "--reviewed", reviewed["reviewed_sha256"])
        original = Path(first["path"]).read_bytes()
        left = self.cli("revise", draft["id"], "--candidate", "left")
        right = self.cli("revise", draft["id"], "--candidate", "right")
        Path(left["path"]).write_text("Nueva condición conservando la excepción.\n")
        left_review = self.cli("review", draft["id"], "--candidate", "left")
        right_review = self.cli("review", draft["id"], "--candidate", "right")
        self.cli("approve", draft["id"], "--candidate", "left", "--reviewed", left_review["reviewed_sha256"])
        with self.assertRaisesRegex(KoraError, "cambió"):
            self.cli("approve", draft["id"], "--candidate", "right", "--reviewed", right_review["reviewed_sha256"])
        self.assertTrue(Path(right["path"]).exists())
        exact = self.cli("resolve", draft["id"], "--revision", first["revision"])
        self.assertEqual(Path(exact["path"]).read_bytes(), original)
        consumer = self.create("skill", "reader", "--requires", draft["id"])
        alias = "urn:test:knowledge:former-rule"
        self.cli("alias", alias, draft["id"])
        planned = self.cli("retire", alias, "--reason", "Ensayo sintético", "--dry-run")
        self.assertIn(consumer["id"], json.dumps(planned["impact"]))
        self.assertTrue(self.cli("resolve", alias)["active"])
        self.cli("retire", alias, "--reason", "Ensayo sintético")
        self.assertFalse(self.cli("resolve", alias)["active"])
        self.assertTrue(Path(self.cli("resolve", alias, "--revision", first["revision"])["path"]).is_file())

    def test_retirement_retry_routes_before_duplicate_identity_discovery(self):
        draft = self.create("knowledge", "rule")
        reviewed = self.cli("review", draft["id"])
        self.cli("approve", draft["id"], "--reviewed", reviewed["reviewed_sha256"])
        reference = self.library / "references/test/rule"
        archived = self.library / "archive/references/test/rule"
        original_unlink = Path.unlink

        def stop_before_active_unlink(path, *args, **kwargs):
            if path == reference:
                raise OSError("synthetic interruption")
            return original_unlink(path, *args, **kwargs)

        with patch.object(Path, "unlink", stop_before_active_unlink):
            with self.assertRaisesRegex(OSError, "synthetic interruption"):
                self.cli("retire", draft["id"], "--reason", "Motivo conservado")
        self.assertTrue(reference.is_symlink() and archived.is_symlink())

        def snapshot():
            return {str(path.relative_to(self.library)):
                    (path.lstat().st_mode, path.lstat().st_mtime_ns,
                     str(path.readlink()) if path.is_symlink() else path.read_bytes())
                    for path in self.library.rglob("*") if path.is_symlink() or path.is_file()}

        before = snapshot()
        preview = self.cli("retire", draft["id"], "--reason", "Motivo conservado", "--dry-run")
        self.assertTrue(preview["dry_run"])
        self.assertEqual(snapshot(), before)
        result = self.cli("retire", draft["id"], "--reason", "Motivo conservado")
        self.assertEqual(result["status"], "retired")
        self.assertEqual(result["reason"], "Motivo conservado")
        self.assertFalse(reference.is_symlink())
        self.assertTrue(archived.is_symlink())


if __name__ == "__main__":
    unittest.main()
