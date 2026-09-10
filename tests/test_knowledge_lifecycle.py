import json
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

import yaml

from kora.catalog import Catalog, KoraError
from kora.knowledge import approve, create_draft, intake, retire, review, revise
from kora.measurement import measure


class KnowledgeLifecycleTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="kora-m5-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.library = self.root / "library"
        self.library.mkdir()
        self.body = self.root / "body.md"
        self.body.write_text("Regla vigente; conserva la excepción.\n", encoding="utf-8")
        self.identifier = "urn:test:kb:rule"

    def draft(self, identifier=None, name="rule", **kwargs):
        return create_draft(
            self.library, "test", name, identifier or self.identifier,
            "Regla de prueba", self.body, **kwargs,
        )

    def publish(self, identifier=None, candidate=None):
        identifier = identifier or self.identifier
        checked = review(self.library, identifier, candidate=candidate)
        return approve(self.library, identifier, checked["reviewed_sha256"], candidate=candidate)

    def test_two_named_candidates_keep_a_and_reject_stale_right(self):
        self.draft()
        first = self.publish()
        first_body = first.body
        left = revise(self.library, self.identifier, candidate="left")
        right = revise(self.library, self.identifier, candidate="right")
        left.content_path.write_text("Revisión B izquierda; conserva la excepción.\n", encoding="utf-8")
        right.content_path.write_text("Revisión C derecha; conserva la excepción.\n", encoding="utf-8")
        left_hash = review(self.library, self.identifier, candidate="left")["reviewed_sha256"]
        right_hash = review(self.library, self.identifier, candidate="right")["reviewed_sha256"]

        second = approve(self.library, self.identifier, left_hash, candidate="left")
        self.assertEqual(Catalog(self.library).get(self.identifier).body,
                         "Revisión B izquierda; conserva la excepción.\n")
        self.assertEqual(Catalog(self.library).at_revision(self.identifier, first.revision).body,
                         first_body)
        self.assertEqual(right.content_path.read_text(encoding="utf-8"),
                         "Revisión C derecha; conserva la excepción.\n")
        self.assertEqual(review(self.library, self.identifier, candidate="right")["base_revision"],
                         first.revision)
        with self.assertRaises(KoraError):
            approve(self.library, self.identifier, right_hash, candidate="right")
        # Replaying the already-approved hash is a no-op, even when the named
        # draft remains available for later inspection.
        self.assertEqual(approve(self.library, self.identifier, left_hash,
                                 candidate="left").revision, second.revision)

    def test_candidate_name_is_safe_and_publication_uses_canonical_coordinates(self):
        with self.assertRaises(KoraError):
            self.draft(identifier="urn:test:kb:safe", name="safe", candidate="left/right")
        draft = self.draft(identifier="urn:test:kb:safe", name="safe", candidate="left")
        self.assertEqual(draft.metadata["candidate"], "left")
        self.assertEqual(draft.metadata["namespace"], "test")
        checked = review(self.library, draft.id, candidate="left")
        published = approve(self.library, draft.id, checked["reviewed_sha256"], candidate="left")
        self.assertTrue((self.library / "references/test/safe").is_symlink())
        self.assertEqual(published.directory.resolve(),
                         (self.library / "versions/test/safe" / published.revision).resolve())
        self.assertFalse((self.library / "references/test/safe--left").exists())

    def test_default_revise_can_follow_named_publication_without_candidate_leak(self):
        self.draft()
        self.publish()
        named = revise(self.library, self.identifier, candidate="left")
        named.content_path.write_text("Candidato izquierdo publicado.\n", encoding="utf-8")
        named_review = review(self.library, self.identifier, candidate="left")
        self.assertEqual(approve(self.library, self.identifier,
                                 named_review["reviewed_sha256"], candidate="left").body,
                         "Candidato izquierdo publicado.\n")

        default = revise(self.library, self.identifier)
        self.assertIsNone(default.metadata.get("candidate"))
        default_review = review(self.library, self.identifier)
        published = approve(self.library, self.identifier,
                            default_review["reviewed_sha256"])
        self.assertIsNone(published.metadata.get("candidate"))

    def test_focal_operation_continues_past_disjoint_diagnosed_product(self):
        self.draft()
        self.publish()
        malformed = self.library / "products/test/foreign"
        malformed.mkdir(parents=True)
        (malformed / "object.yaml").write_text(
            "id: urn:test:kb:foreign\nkind: knowledge\n", encoding="utf-8"
        )
        draft = revise(self.library, self.identifier)
        draft.content_path.write_text("Actualización focal.\n", encoding="utf-8")
        checked = review(self.library, self.identifier)
        published = approve(self.library, self.identifier,
                             checked["reviewed_sha256"])
        self.assertEqual(published.body, "Actualización focal.\n")
        self.assertEqual(Catalog(self.library, strict=False).get(self.identifier).body,
                         "Actualización focal.\n")

    def test_indeterminate_discovery_blocks_before_pointer_write(self):
        draft = self.draft()
        checked = review(self.library, self.identifier)
        malformed = self.library / "products/test/unknown"
        malformed.mkdir(parents=True)
        (malformed / "object.yaml").write_text("kind: [\n", encoding="utf-8")
        with self.assertRaises(KoraError):
            approve(self.library, self.identifier, checked["reviewed_sha256"])
        self.assertFalse((self.library / "references/test/rule").exists())
        self.assertFalse((self.library / "versions/test/rule").exists())
        self.assertEqual(Catalog(self.library, strict=False).availability(draft.id),
                         "indeterminate")

    def test_intake_metadata_and_bytes_survive_as_provenance(self):
        source = self.root / "form.json"
        source.write_bytes(b'{"zero":0,"false":false,"null":null}')
        received = intake(
            self.library, "forms", [source], provenance=[{
                "obtained_at": "2026-09-10T09:00:00Z",
                "localizer": "drive://fixture/form",
                "version": None,
                "view": "native",
                "extraction_status": "unknown",
                "limits": ["not read", "not reviewed"],
            }]
        )
        entry = received["sources"][0]
        self.assertEqual(entry["version"], None)
        self.assertEqual(entry["limits"], ["not read", "not reviewed"])
        preserved = Path(received["path"]) / entry["path"]
        self.assertEqual(preserved.read_bytes(), source.read_bytes())
        draft = self.draft(identifier="urn:test:kb:form", name="form",
                           sources=[preserved])
        copied = draft.metadata["provenance"]["sources"][0]
        self.assertEqual(copied["localizer"], "drive://fixture/form")
        self.assertIsNone(copied["version"])
        self.assertNotIn("read", copied)
        self.assertNotIn("review", copied)
        source.unlink()
        self.assertEqual((draft.directory / copied["path"]).read_bytes(),
                         b'{"zero":0,"false":false,"null":null}')

    def test_typed_dependencies_allow_documented_optional_branch_and_require_active_exact(self):
        dependency = self.draft(identifier="urn:test:kb:dependency", name="dependency")
        dependency = self.publish(dependency.id)
        first_dependency_body = dependency.body
        changed = revise(self.library, dependency.id)
        changed.content_path.write_text("Segunda dependencia.\n", encoding="utf-8")
        second_dependency = self.publish(dependency.id)
        candidate = self.draft(
            identifier="urn:test:kb:dependent", name="dependent",
            requires=[
                {"id": dependency.id, "kind": "knowledge", "revision": dependency.revision},
                {"id": "urn:test:kb:missing", "kind": "knowledge",
                 "condition": "cuando se necesita la excepción"},
            ]
        )
        checked = review(self.library, candidate.id)
        published = approve(self.library, candidate.id, checked["reviewed_sha256"])
        self.assertEqual(published.metadata["publication"]["conditional_dependencies"][0]["id"],
                         "urn:test:kb:missing")
        self.assertEqual(Catalog(self.library).at_revision(dependency.id, dependency.revision).body,
                         first_dependency_body)
        self.assertNotEqual(second_dependency.revision, dependency.revision)
        inline = self.library / "products/test/inline"
        inline.mkdir(parents=True)
        (inline / "object.yaml").write_text(yaml.safe_dump({
            "id": "urn:test:kb:inline", "kind": "knowledge", "name": "inline",
            "description": "Conocimiento sin referencia publicada", "content": "content.md",
        }), encoding="utf-8")
        (inline / "content.md").write_text("inline\n", encoding="utf-8")
        inline_dependent = self.draft(
            identifier="urn:test:kb:inline-dependent", name="inline-dependent",
            requires=["urn:test:kb:inline"]
        )
        with self.assertRaises(KoraError):
            approve(self.library, inline_dependent.id,
                    review(self.library, inline_dependent.id)["reviewed_sha256"])
        mandatory = self.draft(
            identifier="urn:test:kb:mandatory", name="mandatory",
            requires=[{"id": "urn:test:kb:missing", "kind": "knowledge"}]
        )
        with self.assertRaises(KoraError):
            approve(self.library, mandatory.id, review(self.library, mandatory.id)["reviewed_sha256"])

    def test_late_dependency_change_is_rejected_after_version_conservation(self):
        dependency = self.draft(identifier="urn:test:kb:dependency", name="dependency")
        dependency = self.publish(dependency.id)
        candidate = self.draft(identifier="urn:test:kb:dependent", name="dependent",
                                requires=[dependency.id])
        checked = review(self.library, candidate.id)
        dependency_body = dependency.directory.resolve() / "content.md"
        original_bytes = dependency_body.read_bytes()
        original_revalidate = Catalog.revalidate
        calls = {"count": 0}

        def change_before_final_check(catalog):
            calls["count"] += 1
            if calls["count"] == 2:
                dependency_body.write_bytes(original_bytes + b"late change\n")
            return original_revalidate(catalog)

        with patch.object(Catalog, "revalidate", change_before_final_check):
            with self.assertRaises(KoraError):
                approve(self.library, candidate.id, checked["reviewed_sha256"])
        dependency_body.write_bytes(original_bytes)
        self.assertEqual(calls["count"], 2)
        self.assertFalse((self.library / "references/test/dependent").exists())
        self.assertTrue((self.library / "versions/test/dependent").is_dir())
        self.assertTrue(candidate.directory.exists())

    def test_retire_reports_consumer_impact_moves_only_reference_and_keeps_alias(self):
        self.draft()
        first = self.publish()
        alias = "urn:old:kb:rule"
        (self.library / "aliases.yaml").write_text(f"{alias}: {first.id}\n", encoding="utf-8")
        machinery = self.root / "machinery"
        consumer = machinery / "products/test/reader"
        consumer.mkdir(parents=True)
        (consumer / "object.yaml").write_text(json.dumps({
            "id": "urn:test:skill:reader", "kind": "skill", "name": "reader",
            "description": "reader", "content": "content.md", "targets": ["codex"],
            "requires": [first.id],
        }), encoding="utf-8")
        (consumer / "content.md").write_text("Lee la referencia.\n", encoding="utf-8")
        version = self.library / "versions/test/rule" / first.revision
        before = {path.name: path.read_bytes() for path in version.iterdir()}
        planned = retire(self.library, alias, "Fuente reemplazada", replacement="urn:test:kb:new",
                         dry_run=True, consumer_root=machinery)
        self.assertEqual(planned["status"], "planned")
        self.assertIn("urn:test:skill:reader", planned["consumers"])
        self.assertTrue((self.library / "references/test/rule").is_symlink())
        result = retire(self.library, alias, "Fuente reemplazada", replacement="urn:test:kb:new",
                        consumer_root=machinery)
        self.assertEqual(result["status"], "retired")
        self.assertEqual(result["aliases"], [alias])
        self.assertFalse((self.library / "references/test/rule").exists())
        archived = self.library / "archive/references/test/rule"
        self.assertTrue(archived.is_symlink())
        self.assertEqual(archived.resolve(), version.resolve())
        self.assertEqual({path.name: path.read_bytes() for path in version.iterdir()}, before)
        self.assertEqual(Catalog(machinery, knowledge=self.library).availability(alias), "retired")
        self.assertEqual((self.library / "lifecycle.yaml").read_text(encoding="utf-8").count("Fuente reemplazada"), 1)
        self.assertNotIn("reason", Catalog(self.library).at_revision(alias, first.revision).metadata)

    def test_retirement_retries_after_pointer_transition_failure(self):
        self.draft()
        first = self.publish()
        active = self.library / "references/test/rule"
        version = self.library / "versions/test/rule" / first.revision
        before = {path.relative_to(version): path.read_bytes()
                  for path in version.rglob("*") if path.is_file()}
        original_unlink = Path.unlink
        failed = {"once": True}

        def fail_active(path, *args, **kwargs):
            if path == active and failed["once"]:
                failed["once"] = False
                raise OSError("injected interruption")
            return original_unlink(path, *args, **kwargs)

        with patch.object(Path, "unlink", fail_active):
            with self.assertRaises(OSError):
                retire(self.library, first.id, "interrumpido")
        self.assertTrue(active.is_symlink())
        self.assertTrue((self.library / "archive/references/test/rule").is_symlink())
        self.assertEqual({path.relative_to(version): path.read_bytes()
                          for path in version.rglob("*") if path.is_file()}, before)
        pending_lifecycle = yaml.safe_load(
            (self.library / "lifecycle.yaml").read_text(encoding="utf-8"))
        self.assertEqual(pending_lifecycle[first.id]["status"], "retiring")
        self.assertEqual(pending_lifecycle[first.id]["reason"], "interrumpido")
        planned = retire(self.library, first.id, "otro motivo", dry_run=True)
        self.assertTrue(planned["recovery_pending"])
        self.assertIn("unlink_active_reference_after_exact_pair_check", planned["actions"])
        self.assertTrue(active.is_symlink())
        result = retire(self.library, first.id, "interrumpido")
        self.assertEqual(result["status"], "retired")
        self.assertEqual(Catalog(self.library).availability(first.id), "retired")

    def test_retirement_retries_after_active_unlink_before_final_lifecycle(self):
        self.draft()
        first = self.publish()
        version = self.library / "versions/test/rule" / first.revision
        before = {path.relative_to(version): path.read_bytes()
                  for path in version.rglob("*") if path.is_file()}
        import importlib
        knowledge = importlib.import_module("kora.knowledge")
        original_write = knowledge._write_lifecycle
        calls = {"count": 0}

        def fail_final(root, records):
            calls["count"] += 1
            if calls["count"] == 2:
                raise OSError("injected final lifecycle interruption")
            return original_write(root, records)

        with patch.object(knowledge, "_write_lifecycle", side_effect=fail_final):
            with self.assertRaises(OSError):
                retire(self.library, first.id, "final interrumpido")
        self.assertFalse((self.library / "references/test/rule").exists())
        self.assertTrue((self.library / "archive/references/test/rule").is_symlink())
        self.assertEqual({path.relative_to(version): path.read_bytes()
                          for path in version.rglob("*") if path.is_file()}, before)
        pending = yaml.safe_load((self.library / "lifecycle.yaml").read_text(encoding="utf-8"))
        self.assertEqual(pending[first.id]["status"], "retiring")
        self.assertEqual(pending[first.id]["reason"], "final interrumpido")
        result = retire(self.library, first.id, "otro motivo")
        self.assertEqual(result["status"], "retired")


class MeasurementTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="kora-m5-measure-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.source = self.root / "source.md"
        self.candidate = self.root / "candidate.md"
        self.aux = self.root / "aux.md"
        self.wrapper = self.root / "wrapper.md"
        self.source.write_text("source", encoding="utf-8")
        self.candidate.write_text("candidate", encoding="utf-8")
        self.aux.write_text("aux", encoding="utf-8")
        self.wrapper.write_text("wrapper", encoding="utf-8")

    def test_measurement_stub_identifies_encoding_and_counts_complete_candidate(self):
        class Encoder:
            def encode(self, value, **_kwargs):
                return list(value)

        fake = types.SimpleNamespace(__version__="fixture", get_encoding=lambda name: Encoder())
        with patch.dict(sys.modules, {"tiktoken": fake}):
            result = measure(self.source, self.candidate, [self.aux], self.wrapper)
        self.assertEqual(result["status"], "MEASURED")
        self.assertEqual(result["tokenizer"], "tiktoken")
        self.assertEqual(result["encoding"], "cl100k_base")
        self.assertEqual(result["candidate"]["tokens"], len("candidate"))
        self.assertEqual(result["total"]["candidate"], len("candidateauxwrapper"))

    def test_missing_counter_and_binary_input_are_not_measured(self):
        with patch.dict(sys.modules, {"tiktoken": None}):
            result = measure(self.source, self.candidate)
        self.assertEqual(result["status"], "NOT_MEASURED")
        self.assertEqual(result["reason"], "counter_unavailable")
        binary = self.root / "binary"
        binary.write_bytes(b"\xff")
        with patch.dict(sys.modules, {"tiktoken": None}):
            invalid = measure([self.source, binary], [self.candidate],
                              auxiliaries=[self.aux], wrapper=self.wrapper)
        self.assertEqual(invalid["status"], "NOT_MEASURED")
        self.assertEqual(invalid["reason"], "input_not_utf8")
        self.assertEqual(invalid["source"]["paths"],
                         [str(self.source), str(binary)])
        self.assertEqual(invalid["source"]["bytes"],
                         self.source.stat().st_size + 1)
        self.assertIsNone(invalid["source"]["characters"])
        self.assertIsNone(invalid["total"]["source"])


if __name__ == "__main__":
    unittest.main()
