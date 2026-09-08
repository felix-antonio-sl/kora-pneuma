import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import yaml

from kora.catalog import Catalog, KoraError, digest
from kora.migrate import apply_import, import_legacy, plan_import


class MigrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "legacy"
        self.destination = self.root / "new"
        self.source.mkdir()

    def legacy(self, name, kind="knowledge", namespace="test", body=b"# Fuente\n\nSalvo excepciones.\n", **fields):
        bucket = {"knowledge": "conocimiento", "skill": "skills", "agent": "agentes"}[kind]
        path = self.source / "artefactos" / bucket / namespace / name
        path = path / "SKILL.md" if kind == "skill" else path.with_suffix(".md")
        path.parent.mkdir(parents=True, exist_ok=True)
        identifier = f"urn:{namespace}:{'kb' if kind == 'knowledge' else 'artefacto'}:{name}"
        metadata = dict(urn=identifier, nombre=name, descripcion=f"Usar {name} con sus condiciones",
                        estado="publicado" if kind == "knowledge" else "activo",
                        fuente="Fuente sintética con límites explícitos")
        if kind != "knowledge":
            metadata["targets"] = ["codex", "hermes"]
        metadata.update(fields)
        raw = b"---\n" + yaml.safe_dump(metadata, allow_unicode=True).encode() + b"---\n" + body
        path.write_bytes(raw)
        return identifier, path, raw

    def test_full_journey_preserves_bytes_resources_links_and_legacy_identity(self):
        kid, knowledge, raw = self.legacy(
            "domain", body=b"# Texto\n\n```yaml\noriginal: true\n---\n```\n",
            fuente="Fuente preservada; URN KODA legado urn:historical:domain:1.0.0; sin pérdida")
        sid, skill, skill_raw = self.legacy("operate", "skill", conocimiento=[kid],
                                           body=b"# Operar\r\n\r\n1. Leer.\r\n")
        resource = skill.parent / "scripts" / "run.py"
        resource.parent.mkdir()
        resource.write_bytes(b"#!/usr/bin/python3\nprint('local')\n")
        resource.chmod(0o755)
        before = {p: p.read_bytes() for p in self.source.rglob("*") if p.is_file()}
        report = import_legacy(self.source, self.destination)
        self.assertTrue(report["written"])
        self.assertEqual(report["source_files"], 3)
        catalog = Catalog(self.destination)
        domain, procedure = catalog.get(kid), catalog.get(sid)
        self.assertEqual(domain.content_path.read_bytes(), raw)
        self.assertEqual(catalog.get("urn:historical:domain:1.0.0").id, kid)
        restored = procedure.metadata["provenance"]["legacy_header"].encode() + procedure.content_path.read_bytes()
        self.assertEqual(restored, skill_raw)
        self.assertEqual(digest(restored), procedure.metadata["provenance"]["source_sha256"])
        self.assertEqual(procedure.resources()["scripts/run.py"].data, resource.read_bytes())
        self.assertEqual(procedure.resources()["scripts/run.py"].mode, 0o755)
        compatibility = self.destination / knowledge.relative_to(self.source)
        self.assertTrue(compatibility.is_symlink())
        self.assertEqual(compatibility.resolve(), domain.content_path)
        self.assertEqual(compatibility.read_bytes(), raw)
        self.assertEqual(before, {p: p.read_bytes() for p in self.source.rglob("*") if p.is_file()})
        self.source.rename(self.root / "source-unavailable")
        self.assertEqual(Catalog(self.destination).get(sid).resources()["scripts/run.py"].mode, 0o755)

    def test_machinery_and_retired_objects_resolve_without_becoming_active(self):
        machine, _, raw = self.legacy("kora", "agent", namespace="kora", body=b"# Maquinaria anterior\n")
        product, _, _ = self.legacy("mente-omega", "skill", namespace="kora")
        retired, _, _ = self.legacy("old", "skill", estado="deprecado")
        user, _, _ = self.legacy("consumer", "skill", conocimiento=[machine])
        report = import_legacy(self.source, self.destination)
        catalog = Catalog(self.destination)
        self.assertIn(product, catalog.products)
        self.assertNotIn(machine, catalog.products)
        self.assertNotIn(retired, catalog.products)
        self.assertEqual(catalog.get(machine).metadata["provenance"]["legacy_header"].encode()
                         + catalog.get(machine).content_path.read_bytes(), raw)
        self.assertIn({"id": user, "requires": machine, "issue": "archived"}, report["dependency_issues"])
        with self.assertRaises(KoraError):
            catalog.dependencies(catalog.get(user), "codex")

    def test_relations_retain_meaning_without_implicit_agent_composition(self):
        knowledge, _, _ = self.legacy("knowledge")
        procedure, _, _ = self.legacy("procedure", "skill", targets=["codex"])
        agent, _, _ = self.legacy("delegate", "agent")
        caller, _, _ = self.legacy("caller", "agent", conocimiento=[knowledge],
                                   depende=[procedure], componible=[agent], cita=[agent])
        report = import_legacy(self.source, self.destination)
        product = Catalog(self.destination).get(caller)
        self.assertEqual(list(product.requires), [knowledge, procedure])
        self.assertEqual(product.metadata["relations"]["componible"], [agent])
        self.assertEqual(product.metadata["relations"]["cita"], [agent])
        self.assertIn({"id": caller, "requires": procedure, "target": "hermes", "issue": "target_unavailable"},
                      report["dependency_issues"])

    def test_same_name_is_not_same_identity_and_drafts_are_not_promoted(self):
        knowledge, _, _ = self.legacy("same", estado="borrador")
        agent, _, _ = self.legacy("same", "agent")
        import_legacy(self.source, self.destination)
        catalog = Catalog(self.destination)
        self.assertEqual(catalog.get(knowledge).directory.name, "same-knowledge")
        self.assertEqual(catalog.get(agent).directory.name, "same")
        self.assertEqual(catalog.get(knowledge).metadata["provenance"]["legacy_state"], "borrador")
        self.assertEqual(catalog.get(knowledge).name, catalog.get(agent).name)

    def test_retired_target_is_preserved_without_creating_an_adapter(self):
        identifier, _, raw = self.legacy("fleet", "agent", targets=["openclaw"])
        report = import_legacy(self.source, self.destination)
        catalog = Catalog(self.destination)
        self.assertNotIn(identifier, catalog.products)
        archived = catalog.get(identifier)
        self.assertEqual(archived.targets, ())
        self.assertEqual(archived.metadata["provenance"]["legacy_header"].encode()
                         + archived.content_path.read_bytes(), raw)
        self.assertEqual(report["archived_objects"], 1)

    def test_private_archive_and_state_are_not_ingested_or_disclosed(self):
        self.legacy("domain")
        secret = self.source / "artefactos" / ".remember" / "state.txt"
        secret.parent.mkdir()
        secret.write_text("PRIVATE-CONTENT")
        archived = self.source / "_archivo" / "private.txt"
        archived.parent.mkdir()
        archived.write_text("ARCHIVE-PRIVATE-CONTENT")
        report = import_legacy(self.source, self.destination)
        self.assertEqual(report["source_files"], 1)
        self.assertEqual(report["archive"]["files"], 1)
        self.assertEqual(report["excluded_private_entries"], 1)
        self.assertNotIn("PRIVATE-CONTENT", str(report))
        self.assertFalse(any("PRIVATE-CONTENT" in p.read_text() for p in self.destination.rglob("*") if p.is_file()))

    def test_symbolic_source_cannot_silently_import_external_content(self):
        _, skill, _ = self.legacy("skill", "skill")
        external = self.root / "external.txt"
        external.write_text("private")
        (skill.parent / "reference.txt").symlink_to(external)
        with self.assertRaisesRegex(KoraError, "no regular"):
            import_legacy(self.source, self.destination)
        self.assertFalse(self.destination.exists())

    def test_check_is_read_only_and_existing_destination_stops_all_writes(self):
        self.legacy("domain")
        report = import_legacy(self.source, self.destination, dry_run=True)
        self.assertFalse(report["written"])
        self.assertFalse(self.destination.exists())
        occupied = self.destination / "products" / "test" / "domain" / "content.md"
        occupied.parent.mkdir(parents=True)
        occupied.write_text("edición ajena")
        with self.assertRaisesRegex(KoraError, "no se sobrescribe"):
            import_legacy(self.source, self.destination)
        self.assertEqual(occupied.read_text(), "edición ajena")
        self.assertFalse((self.destination / "aliases.yaml").exists())

    def test_source_change_after_plan_rejects_stale_import(self):
        _, source, _ = self.legacy("domain")
        plan = plan_import(self.source, self.destination)
        source.write_bytes(source.read_bytes() + b"\nCambio concurrente\n")
        with self.assertRaisesRegex(KoraError, "corpus cambió"):
            apply_import(plan)
        self.assertFalse(self.destination.exists())

    def test_source_edit_during_publication_is_preserved_and_import_is_reverted(self):
        _, source, original = self.legacy("domain")
        import kora.migrate as migration
        publish = migration._publish_file
        changed = original + "\nEdición concurrente del origen\n".encode()

        def publish_then_edit(staged, target):
            publish(staged, target)
            source.write_bytes(changed)

        with patch("kora.migrate._publish_file", side_effect=publish_then_edit):
            with self.assertRaisesRegex(KoraError, "revertida.*corpus cambió durante"):
                import_legacy(self.source, self.destination)
        self.assertEqual(source.read_bytes(), changed)
        self.assertEqual(list(self.destination.iterdir()), [])

    def test_publication_failure_removes_only_imported_outputs(self):
        self.legacy("domain")
        self.destination.mkdir()
        unrelated = self.destination / "README.md"
        unrelated.write_text("trabajo ajeno")
        import kora.migrate as migration
        publish = migration._publish_file
        calls = []

        def fail_on_second(staged, target):
            calls.append(target)
            if len(calls) == 2:
                raise OSError("fallo simulado")
            publish(staged, target)

        with patch("kora.migrate._publish_file", side_effect=fail_on_second):
            with self.assertRaisesRegex(KoraError, "revertida"):
                import_legacy(self.source, self.destination)
        self.assertEqual(list(self.destination.iterdir()), [unrelated])
        self.assertEqual(unrelated.read_text(), "trabajo ajeno")

    def test_failure_keeps_a_concurrent_edit_to_a_published_file(self):
        self.legacy("domain")
        import kora.migrate as migration
        publish = migration._publish_file
        first = []

        def edit_then_fail(staged, target):
            if first:
                first[0].write_bytes(b"cambio concurrente")
                raise OSError("fallo posterior")
            publish(staged, target)
            first.append(target)

        with patch("kora.migrate._publish_file", side_effect=edit_then_fail):
            with self.assertRaisesRegex(KoraError, "concurrentes conservados"):
                import_legacy(self.source, self.destination)
        self.assertEqual(first[0].read_bytes(), b"cambio concurrente")
        self.assertFalse((self.destination / "aliases.yaml").exists())

    def test_orphan_resources_and_duplicate_keys_fail_before_writing(self):
        _, source, _ = self.legacy("domain")
        orphan = source.parent / "unowned.bin"
        orphan.write_bytes(b"\x00\xff")
        with self.assertRaisesRegex(KoraError, "sin objeto conservador"):
            import_legacy(self.source, self.destination)
        orphan.unlink()
        source.write_bytes(source.read_bytes().replace(b"---\n", b"---\nurn: urn:test:kb:other\n", 1))
        with self.assertRaisesRegex(KoraError, "duplicada"):
            import_legacy(self.source, self.destination)
        self.assertFalse(self.destination.exists())


if __name__ == "__main__":
    unittest.main()
