import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml

from kora.catalog import Catalog, KoraError, read_yaml
from kora.knowledge import approve, create_draft, intake, review, revise
from kora.render_codex import render as render_codex
from kora.render_hermes import render as render_hermes


class KnowledgePublicationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="kora-knowledge-")
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.store = self.base / "knowledge"
        self.store.mkdir()
        self.machinery = self.base / "machinery"
        self.machinery.mkdir()
        self.body = self.base / "authored.md"
        self.body.write_bytes(b"# Permission\r\n\r\nContinue with permission, unless revoked.\r\n")
        self.source = self.base / "source.csv"
        self.source.write_bytes(b"permission,exception\r\nvalid,unless revoked\r\n")
        self.identifier = "urn:test:kb:permission"

    def draft(self, name="permission", **kwargs):
        return create_draft(
            self.store, "test", name, f"urn:test:kb:{name}",
            "Permiso vigente y excepción", self.body, **kwargs,
        )

    def publish(self, identifier=None):
        identifier = identifier or self.identifier
        reviewed = review(self.store, identifier)
        return approve(self.store, identifier, reviewed["reviewed_sha256"])

    def consumer(self, kind="skill", name="reader", requires=None):
        directory = self.machinery / "products/test" / name
        directory.mkdir(parents=True)
        metadata = {
            "id": f"urn:test:{kind}:{name}", "kind": kind, "name": name,
            "description": "Consultar el permiso conservando su excepción",
            "content": "content.md", "targets": ["codex", "hermes"],
            "requires": list(requires if requires is not None else [self.identifier]),
        }
        (directory / "object.yaml").write_text(yaml.safe_dump(metadata))
        (directory / "content.md").write_text("Consulta el conocimiento antes de resolver.\n")
        return metadata["id"]

    def update_metadata(self, draft, **changes):
        metadata = read_yaml(draft.directory / "object.yaml")
        metadata.update(changes)
        (draft.directory / "object.yaml").write_text(yaml.safe_dump(metadata))

    def test_draft_is_not_consultable_or_a_realizable_dependency_before_approval(self):
        draft = self.draft()
        consumer = self.consumer()
        catalog = Catalog(self.machinery, knowledge=self.store)
        self.assertNotIn(draft.id, catalog.products)
        with self.assertRaises(KoraError):
            catalog.get(draft.id)
        for renderer in (render_codex, render_hermes):
            with self.subTest(runtime=renderer.__module__):
                with self.assertRaises(KoraError):
                    renderer(catalog, catalog.get(consumer))

        published = self.publish()
        self.assertEqual(published.metadata["publication"]["status"], "approved")
        catalog = Catalog(self.machinery, knowledge=self.store)
        self.assertEqual(catalog.get(draft.id).body, draft.body)
        for renderer in (render_codex, render_hermes):
            with self.subTest(runtime=renderer.__module__):
                self.assertTrue(renderer(catalog, catalog.get(consumer)))

    def test_intake_to_publication_keeps_original_bytes_and_provenance_after_input_disappears(self):
        source_bytes = self.source.read_bytes()
        body_bytes = self.body.read_bytes()
        intake(self.store, "permission-input", [self.source])
        stored_sources = [
            path for path in (self.store / "inbox/permission-input").rglob("*")
            if path.is_file() and path.read_bytes() == source_bytes
        ]
        self.assertEqual(len(stored_sources), 1)
        self.source.unlink()
        draft = self.draft(sources=stored_sources)
        shutil.rmtree(self.store / "inbox/permission-input")
        self.body.unlink()
        published = self.publish()
        self.assertEqual(published.content_path.read_bytes(), body_bytes)
        originals = published.metadata["provenance"]["sources"]
        self.assertEqual(len(originals), 1)
        self.assertEqual((published.directory / originals[0]["path"]).read_bytes(), source_bytes)
        self.assertEqual(originals[0]["sha256"], hashlib.sha256(source_bytes).hexdigest())
        self.assertEqual(draft.content_path.read_bytes(), body_bytes)

    def test_native_resolver_uses_the_destination_machinery_when_it_has_its_own_cli(self):
        self.draft()
        self.publish()
        identifier = self.consumer()
        entrypoint = self.machinery / "kora_cli.py"
        entrypoint.write_text("# CLI disponible en la copia de destino\n")
        catalog = Catalog(self.machinery, knowledge=self.store)
        for renderer in (render_codex, render_hermes):
            with self.subTest(runtime=renderer.__module__):
                files = renderer(catalog, catalog.get(identifier))
                instructions = "\n".join(file.data.decode() for file in files.values())
                self.assertIn(f"python3 {entrypoint} --root {self.store} resolve URN", instructions)
                generator = Path(__file__).resolve().parents[1] / "kora_cli.py"
                self.assertNotIn(f"python3 {generator}", instructions)

    def test_approval_rejects_reviewed_hash_after_body_or_original_changes(self):
        for change in ("content", "original"):
            with self.subTest(change=change):
                draft = self.draft(name=change, sources=[self.source])
                reviewed = review(self.store, draft.id)["reviewed_sha256"]
                changed = draft.content_path if change == "content" else (
                    draft.directory / draft.metadata["provenance"]["sources"][0]["path"]
                )
                changed.write_bytes(changed.read_bytes() + b"Changed after review.\n")
                with self.assertRaises(KoraError):
                    approve(self.store, draft.id, reviewed)
                self.assertNotIn(draft.id, Catalog(self.store).products)
                self.assertTrue(draft.directory.exists())

    def test_new_approved_version_reaches_both_native_consumers_without_reinstallation(self):
        self.draft()
        first = self.publish()
        reader = self.consumer()
        catalog = Catalog(self.machinery, knowledge=self.store)
        old_content = first.content_path.read_bytes()
        installed = {}
        for renderer in (render_codex, render_hermes):
            files = renderer(catalog, catalog.get(reader))
            native = self.base / "home"
            for relative, file in files.items():
                path = native / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(file.data)
                installed[path] = file.data

        referenced_paths = []
        for data in installed.values():
            paths = [Path(value) for value in re.findall(r"`([^`]+)`", data.decode())
                     if value.startswith(str(self.store) + "/")]
            self.assertTrue(paths, data.decode())
            for path in paths:
                self.assertTrue(path.is_relative_to(self.store / "references"))
                self.assertEqual(path.read_bytes(), old_content)
            referenced_paths.extend(paths)

        draft = revise(self.store, self.identifier)
        draft.content_path.write_text("New permission rule; revocation still takes precedence.\n")
        for path in referenced_paths:
            self.assertEqual(path.read_bytes(), old_content)
        self.assertEqual(Catalog(self.store).get(self.identifier).revision, first.revision)
        second = self.publish()
        self.assertNotEqual(second.revision, first.revision)
        for path, original in installed.items():
            self.assertEqual(path.read_bytes(), original)
        for path in referenced_paths:
            self.assertEqual(path.read_text(), draft.body)
        catalog = Catalog(self.machinery, knowledge=self.store)
        for renderer in (render_codex, render_hermes):
            for relative, file in renderer(catalog, catalog.get(reader)).items():
                self.assertEqual(file.data, installed[self.base / "home" / relative])
        self.assertEqual(catalog.at_revision(self.identifier, first.revision).content_path.read_bytes(),
                         old_content)

    def test_reference_and_its_alias_remain_consultable_without_agents_or_machinery(self):
        draft = self.draft()
        self.update_metadata(draft, relations={"cita": ["urn:test:agent:advisor"]})
        first = self.publish()
        original = first.body
        alias = "urn:previous:kb:permission"
        (self.store / "aliases.yaml").write_text(yaml.safe_dump({alias: self.identifier}))
        self.consumer(kind="agent", name="advisor")
        (self.machinery / "knowledge").symlink_to(self.store, target_is_directory=True)
        self.assertEqual(Catalog(self.machinery).get(alias).revision, first.revision)
        revised = revise(self.store, alias)
        revised.content_path.write_text("A new rule preserves the former exception.\n")
        second = self.publish(alias)

        shutil.rmtree(self.machinery)
        catalog = Catalog(self.store)
        self.assertEqual(catalog.get(alias).id, self.identifier)
        self.assertEqual(catalog.get(alias).revision, second.revision)
        self.assertEqual(catalog.at_revision(alias, first.revision).body, original)
        self.assertEqual(catalog.reference_issues(), [])
        self.assertTrue(all(p.kind == "knowledge" for p in catalog.products.values()))

    def test_failure_before_switching_reference_preserves_previous_version_and_draft(self):
        self.draft()
        first = self.publish()
        original = first.content_path.read_bytes()
        draft = revise(self.store, self.identifier)
        draft.content_path.write_text("Proposed replacement, not yet available.\n")
        reviewed = review(self.store, self.identifier)["reviewed_sha256"]
        observed = []

        def unavailable_exchange(*_args, **_kwargs):
            visible = Catalog(self.store).get(self.identifier)
            self.assertEqual(visible.revision, first.revision)
            self.assertEqual(visible.content_path.read_bytes(), original)
            observed.append(visible.revision)
            raise OSError("Injected failure before publishing the reference")

        with patch("kora.knowledge.exchange", side_effect=unavailable_exchange) as switch:
            with self.assertRaises((KoraError, OSError)):
                approve(self.store, self.identifier, reviewed)
            switch.assert_called_once()
        self.assertEqual(observed, [first.revision])
        catalog = Catalog(self.store)
        self.assertEqual(catalog.get(self.identifier).revision, first.revision)
        self.assertEqual(catalog.at_revision(self.identifier, first.revision).content_path.read_bytes(),
                         original)
        self.assertIn("Proposed replacement", draft.body)
        published = approve(self.store, self.identifier, reviewed)
        self.assertEqual(published.body, draft.body)

    def test_reference_cannot_require_an_agent_or_an_unpublished_knowledge(self):
        agent_id = self.consumer(kind="agent", name="advisor", requires=[])
        shutil.copytree(self.machinery / "products", self.store / "products")
        self.assertEqual(Catalog(self.store).get(agent_id).kind, "agent")
        unpublished = self.draft(name="unpublished")
        for name, requirement in (("agent-dependent", agent_id), ("draft-dependent", unpublished.id)):
            with self.subTest(requirement=requirement):
                candidate = self.draft(name=name)
                self.update_metadata(candidate, requires=[requirement])
                reviewed = review(self.store, candidate.id)["reviewed_sha256"]
                with self.assertRaises(KoraError):
                    approve(self.store, candidate.id, reviewed)
                self.assertNotIn(candidate.id, Catalog(self.store).products)

        self.publish(unpublished.id)
        dependent = self.publish("urn:test:kb:draft-dependent")
        catalog = Catalog(self.store)
        self.assertEqual([p.id for p in catalog.dependencies(dependent, "codex")], [unpublished.id])

    def test_revise_preserves_work_and_advances_base_only_for_an_unchanged_draft(self):
        self.draft(sources=[self.source])
        first = self.publish()
        draft = revise(self.store, self.identifier)
        self.assertEqual(review(self.store, self.identifier)["base_revision"], first.revision)
        draft.content_path.write_text("Work in progress, with an unresolved exception.\n")
        note = draft.directory / "notes.md"
        note.write_text("A detail that must survive repeated preparation.\n")
        before = {p.relative_to(draft.directory): p.read_bytes()
                  for p in draft.directory.rglob("*") if p.is_file()}
        revised_again = revise(self.store, self.identifier)
        self.assertEqual({p.relative_to(revised_again.directory): p.read_bytes()
                          for p in revised_again.directory.rglob("*") if p.is_file()}, before)
        second = self.publish()
        draft = revise(self.store, self.identifier)
        self.assertEqual(review(self.store, self.identifier)["base_revision"], second.revision)
        self.assertEqual(draft.body, second.body)
        self.assertEqual((draft.directory / "notes.md").read_bytes(), note.read_bytes())

    def test_modifying_a_published_snapshot_is_detected_instead_of_silently_served(self):
        self.draft()
        published = self.publish()
        published.content_path.write_text("An unreviewed edit to a published snapshot.\n")
        with self.assertRaises(KoraError):
            Catalog(self.store).get(published.id)
        with self.assertRaises(KoraError):
            Catalog(self.store).at_revision(published.id, published.revision)
        with self.assertRaises(KoraError):
            self.publish(published.id)

    def test_damaged_reference_does_not_block_a_healthy_one_but_full_check_reports_it(self):
        self.draft()
        damaged = self.publish()
        self.draft(name="healthy")
        healthy = self.publish("urn:test:kb:healthy")
        (self.store / "aliases.yaml").write_text(yaml.safe_dump({
            "urn:old:kb:damaged": damaged.id, "urn:old:kb:healthy": healthy.id,
        }))
        damaged.content_path.write_text("An edit that was never approved.\n")

        catalog = Catalog(self.store)
        self.assertEqual(catalog.get("urn:old:kb:healthy").body, healthy.body)
        with self.assertRaises(KoraError):
            catalog.get(damaged.id)
        with self.assertRaises(KoraError):
            catalog.get("urn:old:kb:damaged")
        issues = catalog.reference_issues()
        self.assertEqual([(i["source"], i["relation"]) for i in issues],
                         [(damaged.id, "integrity")])

        executable = Path(__file__).resolve().parents[1] / "kora_cli.py"
        command = [sys.executable, str(executable), "--root", str(self.store)]
        resolved = subprocess.run(command + ["resolve", "urn:old:kb:healthy"],
                                  capture_output=True, text=True, timeout=15)
        self.assertEqual(resolved.returncode, 0, resolved.stderr)
        self.assertEqual(json.loads(resolved.stdout)["id"], healthy.id)
        checked = subprocess.run(command + ["check"], capture_output=True, text=True, timeout=15)
        self.assertEqual(checked.returncode, 1, checked.stderr)
        report = json.loads(checked.stdout)
        self.assertFalse(report["ok"])
        self.assertEqual(report["issues"], issues)

    def test_a_different_identity_cannot_replace_an_existing_reference_at_the_same_path(self):
        draft = self.draft()
        first = self.publish()
        original = first.body
        shutil.rmtree(draft.directory)
        with self.assertRaises(KoraError):
            other = create_draft(
                self.store, "test", "permission", "urn:test:kb:another-identity",
                "Otra referencia independiente", self.body,
            )
            self.publish(other.id)
        revised = revise(self.store, self.identifier)
        self.update_metadata(revised, id="urn:test:kb:another-identity", revision_base=None)
        with self.assertRaises(KoraError):
            self.publish("urn:test:kb:another-identity")
        catalog = Catalog(self.store)
        self.assertEqual(catalog.get(self.identifier).revision, first.revision)
        self.assertEqual(catalog.get(self.identifier).body, original)
        self.assertNotIn("urn:test:kb:another-identity", catalog.products)

    def test_cli_pipeline_exposes_only_approved_references_and_exact_revisions(self):
        executable = Path(__file__).resolve().parents[1] / "kora_cli.py"

        def cli(*args, ok=True):
            result = subprocess.run(
                [sys.executable, str(executable), "--root", str(self.machinery),
                 "--knowledge-root", str(self.store), *args],
                cwd=self.base, capture_output=True, text=True, timeout=15,
            )
            if not ok:
                self.assertNotEqual(result.returncode, 0, result.stdout)
                return result
            self.assertEqual(result.returncode, 0, result.stderr)
            return json.loads(result.stdout)

        cli("intake", "cli-input", "--source", str(self.source))
        cli("create", "knowledge", "test", "permission", "--id", self.identifier,
            "--description", "Permiso y excepción", "--body", str(self.body),
            "--source", str(self.source))
        listed = cli("list", "--kind", "knowledge")
        self.assertNotIn(self.identifier, json.dumps(listed))
        cli("resolve", self.identifier, ok=False)
        reviewed = cli("review", self.identifier)
        cli("approve", self.identifier, "--reviewed", reviewed["reviewed_sha256"])
        first = cli("resolve", self.identifier)
        self.assertEqual(first["publication"], "approved")
        self.assertEqual(len(first["revision"]), 64)
        self.assertEqual(Path(first["path"]).read_bytes(), self.body.read_bytes())
        self.assertIn(self.identifier, json.dumps(cli("list", "--kind", "knowledge")))

        cli("revise", self.identifier)
        draft = self.store / "drafts/test/permission/content.md"
        draft.write_text("Reviewed revision two, with the original exception.\n")
        reviewed = cli("review", self.identifier)
        cli("approve", self.identifier, "--reviewed", reviewed["reviewed_sha256"])
        second = cli("resolve", self.identifier)
        self.assertNotEqual(second["revision"], first["revision"])
        self.assertEqual(second["path"], first["path"])
        historic = cli("resolve", self.identifier, "--revision", first["revision"])
        self.assertEqual(historic["revision"], first["revision"])
        self.assertEqual(Path(historic["path"]).read_bytes(), self.body.read_bytes())


if __name__ == "__main__":
    unittest.main()
