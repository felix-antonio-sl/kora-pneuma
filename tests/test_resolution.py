import json
import shlex
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import yaml

from kora.catalog import Catalog, KoraError
from kora.cli import build
from kora.knowledge import approve, create_draft, review, revise
from kora.needs import Need
from kora.render_codex import render as render_codex
from kora.render_hermes import render as render_hermes


class ResolutionTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="kora-resolution-")
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.root = self.base / "machinery"
        self.root.mkdir()
        self.library = self.base / "knowledge"
        self.library.mkdir()

    def product(self, folder, *, root=None, kind="skill", identifier=None,
                targets=("codex", "hermes"), requires=(), body="Fuente\n",
                description=None):
        root = self.root if root is None else Path(root)
        directory = root / "products" / "test" / folder
        directory.mkdir(parents=True, exist_ok=True)
        identifier = identifier or f"urn:test:{kind}:{folder}"
        metadata = {
            "id": identifier,
            "kind": kind,
            "name": folder,
            "description": description or f"Producto de prueba {folder}.",
            "content": "body.md",
            "targets": list(targets),
            "requires": list(requires),
        }
        (directory / "object.yaml").write_text(
            yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )
        (directory / "body.md").write_text(body, encoding="utf-8")
        return identifier, directory

    def publish_knowledge(self, name="rules", body="Regla publicada.\n"):
        source = self.base / f"{name}-source.md"
        source.write_text(body, encoding="utf-8")
        identifier = f"urn:test:knowledge:{name}"
        create_draft(
            self.library,
            "test",
            name,
            identifier,
            f"Referencia {name}",
            source,
        )
        reviewed = review(self.library, identifier)["reviewed_sha256"]
        return approve(self.library, identifier, reviewed)

    def test_needs_normalize_mappings_while_requires_keeps_source_data(self):
        fixed_revision = "a" * 64
        raw_requires = [
            "urn:test:knowledge:plain",
            {
                "id": "urn:test:skill:advanced",
                "kind": "product",
                "revision": fixed_revision,
                "target": "codex",
                "condition": "cuando se solicite el análisis",
                "purpose": "aportar el método avanzado",
            },
        ]
        identifier, directory = self.product("consumer", requires=raw_requires)

        catalog = Catalog(self.root)
        product = catalog.get(identifier)

        self.assertEqual(list(product.requires), raw_requires)
        self.assertEqual(yaml.safe_load((directory / "object.yaml").read_text())["requires"],
                         raw_requires)
        self.assertIsInstance(product.needs, tuple)
        self.assertEqual(
            product.needs,
            (
                Need("urn:test:knowledge:plain"),
                Need(
                    "urn:test:skill:advanced",
                    kind="product",
                    revision=fixed_revision,
                    target="codex",
                    condition="cuando se solicite el análisis",
                    purpose="aportar el método avanzado",
                ),
            ),
        )

    def test_explain_uses_directed_edges_and_omits_unavailable_conditional_branch(self):
        always, _ = self.product("always", body="Siempre disponible.\n")
        cross_target, _ = self.product("hermes-only", targets=("hermes",))
        missing_conditional = "urn:test:skill:optional"
        capability = "urn:test:capability:search"
        main, _ = self.product(
            "main",
            kind="agent",
            requires=[
                {"id": always, "kind": "product", "target": "codex",
                 "purpose": "método principal"},
                {"id": missing_conditional, "kind": "product", "target": "codex",
                 "condition": "si el caso contiene una excepción"},
                {"id": cross_target, "kind": "product", "target": "hermes"},
                {"id": capability, "kind": "capability", "target": "codex",
                 "condition": "si requiere buscar fuentes externas"},
            ],
        )
        catalog = Catalog(self.root, capabilities=())

        explanation = catalog.explain(catalog.get(main), "codex", capabilities=())
        edges = {edge["target"]: edge for edge in explanation["edges"]}

        self.assertEqual({product.id for product in explanation["products"]},
                         {always, main})
        self.assertEqual(edges[always]["source"], main)
        self.assertEqual(edges[always]["kind"], "product")
        self.assertEqual(edges[always]["status"], "available")
        self.assertEqual(edges[always].get("purpose"), "método principal")
        self.assertEqual(edges[missing_conditional]["status"], "unavailable")
        self.assertEqual(edges[missing_conditional].get("condition"),
                         "si el caso contiene una excepción")
        self.assertEqual(edges[cross_target]["status"], "not_applicable")
        self.assertEqual(edges[capability]["status"], "unavailable")
        self.assertEqual([product.id for product in catalog.dependencies(
            catalog.get(main), "codex")], [always])

        rendered = render_codex(catalog, catalog.get(main))
        rendered_text = "\n".join(file.data.decode("utf-8") for file in rendered.values())
        self.assertIn(always, rendered_text)
        self.assertIn(missing_conditional, rendered_text)
        self.assertIn("no disponible", rendered_text.lower())
        self.assertNotIn(cross_target, rendered_text)
        self.assertIn(capability, rendered_text)

    def test_target_mismatch_is_not_applicable_and_does_not_block_other_target(self):
        hermes_only, _ = self.product("hermes-only", targets=("hermes",))
        codex_only, _ = self.product("codex-only", targets=("codex",))
        main, _ = self.product(
            "targeted",
            requires=[
                {"id": hermes_only, "kind": "product", "target": "hermes"},
                {"id": codex_only, "kind": "product", "target": "codex"},
            ],
        )
        catalog = Catalog(self.root)

        codex = catalog.explain(catalog.get(main), "codex")
        codex_edges = {edge["target"]: edge for edge in codex["edges"]}
        self.assertEqual(codex_edges[hermes_only]["status"], "not_applicable")
        self.assertEqual([product.id for product in catalog.dependencies(
            catalog.get(main), "codex")], [codex_only])

        hermes = catalog.explain(catalog.get(main), "hermes")
        hermes_edges = {edge["target"]: edge for edge in hermes["edges"]}
        self.assertEqual(hermes_edges[codex_only]["status"], "not_applicable")
        self.assertEqual([product.id for product in catalog.dependencies(
            catalog.get(main), "hermes")], [hermes_only])

    def test_unconditional_missing_need_fails_resolution_and_rendering(self):
        missing = "urn:test:skill:required"
        identifier, _ = self.product(
            "consumer",
            requires=[{"id": missing, "kind": "product", "target": "codex"}],
        )
        catalog = Catalog(self.root)
        edge = catalog.explain(catalog.get(identifier), "codex")["edges"][0]
        self.assertEqual(edge["status"], "unavailable")
        with self.assertRaisesRegex(KoraError, missing):
            catalog.dependencies(catalog.get(identifier), "codex")
        with self.assertRaisesRegex(KoraError, missing):
            render_codex(catalog, catalog.get(identifier))

    def test_capability_requires_evidence_and_can_be_satisfied_explicitly(self):
        capability = "urn:test:capability:ocr"
        identifier, _ = self.product(
            "consumer",
            requires=[{"id": capability, "kind": "capability", "target": "codex"}],
        )
        catalog = Catalog(self.root, capabilities=())
        unavailable = catalog.explain(catalog.get(identifier), "codex", capabilities=())["edges"][0]
        self.assertEqual(unavailable["status"], "unavailable")
        with self.assertRaisesRegex(KoraError, capability):
            catalog.dependencies(catalog.get(identifier), "codex")

        available = catalog.explain(catalog.get(identifier), "codex", capabilities=(capability,))["edges"][0]
        self.assertEqual(available["status"], "available")
        capable_catalog = Catalog(self.root, capabilities=(capability,))
        self.assertEqual(capable_catalog.dependencies(capable_catalog.get(identifier), "codex"), [])

    def test_strict_false_contains_unrelated_invalid_target_but_strict_default_rejects_it(self):
        healthy, _ = self.product("healthy")
        broken, _ = self.product("broken", targets=("codex", "unknown"))

        with self.assertRaises(KoraError):
            Catalog(self.root)

        catalog = Catalog(self.root, strict=False)
        self.assertEqual(catalog.get(healthy).id, healthy)
        with self.assertRaisesRegex(KoraError, broken):
            catalog.get(broken)
        diagnostics = json.dumps(catalog.diagnostics, ensure_ascii=False)
        self.assertIn(broken, diagnostics)
        self.assertIn("destinos", diagnostics.lower())

    def test_strict_false_reserves_unique_identity_from_broken_yaml(self):
        healthy, _ = self.product("healthy")
        broken = "urn:test:skill:broken-yaml"
        directory = self.root / "products" / "test" / "broken-yaml"
        directory.mkdir(parents=True)
        (directory / "object.yaml").write_text(
            f"id: {broken}\nkind: skill\ndescription: \"unterminated\n",
            encoding="utf-8",
        )

        catalog = Catalog(self.root, strict=False)
        self.assertEqual(catalog.get(healthy).id, healthy)
        with self.assertRaisesRegex(KoraError, broken):
            catalog.get(broken)
        self.assertIn(broken, json.dumps(catalog.diagnostics, ensure_ascii=False))

    def test_indeterminable_identity_blocks_even_healthy_get_with_uncertainty_diagnostic(self):
        healthy, _ = self.product("healthy")
        directory = self.root / "products" / "test" / "unknown-yaml"
        directory.mkdir(parents=True)
        (directory / "object.yaml").write_text(
            "kind: skill\n[broken\n",
            encoding="utf-8",
        )

        catalog = Catalog(self.root, strict=False)
        with self.assertRaisesRegex(KoraError, "[Ii]dentidad|incertidumbre"):
            catalog.get(healthy)
        diagnostics = json.dumps(catalog.diagnostics, ensure_ascii=False).lower()
        self.assertIn("incertid", diagnostics)

    def test_collision_blocks_only_implicated_identity_and_check_reports_all_errors(self):
        healthy, _ = self.product("healthy")
        duplicate = "urn:test:skill:collision"
        self.product("collision-one", identifier=duplicate)
        self.product("collision-two", identifier=duplicate)
        invalid, _ = self.product("invalid", targets=("wat",))

        catalog = Catalog(self.root, strict=False)
        self.assertEqual(catalog.get(healthy).id, healthy)
        with self.assertRaisesRegex(KoraError, duplicate):
            catalog.get(duplicate)
        diagnostics = json.dumps(catalog.diagnostics, ensure_ascii=False)
        self.assertIn(duplicate, diagnostics)
        self.assertIn(invalid, diagnostics)

        executable = Path(__file__).resolve().parents[1] / "kora_cli.py"
        checked = subprocess.run(
            [sys.executable, str(executable), "--root", str(self.root), "check"],
            cwd=self.base,
            capture_output=True,
            text=True,
            timeout=15,
        )
        self.assertNotEqual(checked.returncode, 0, checked.stderr)
        report = json.loads(checked.stdout)
        self.assertFalse(report["ok"])
        issue_text = json.dumps(report["issues"], ensure_ascii=False)
        self.assertIn(duplicate, issue_text)
        self.assertIn(invalid, issue_text)

    def test_fixed_revision_resolves_exact_old_snapshot_after_new_publication(self):
        first = self.publish_knowledge(body="Primera revisión; conserva excepción.\n")
        revised = revise(self.library, first.id)
        revised.content_path.write_text("Segunda revisión; otra regla.\n", encoding="utf-8")
        second = approve(self.library, first.id,
                         review(self.library, first.id)["reviewed_sha256"])
        self.assertNotEqual(first.revision, second.revision)

        consumer, _ = self.product(
            "consumer",
            requires=[{"id": first.id, "kind": "knowledge", "revision": first.revision}],
        )
        catalog = Catalog(self.root, knowledge=self.library)
        dependencies = catalog.dependencies(catalog.get(consumer), "codex")
        self.assertEqual([(item.id, item.revision, item.body) for item in dependencies],
                         [(first.id, first.revision, "Primera revisión; conserva excepción.\n")])

    def test_two_fixed_revisions_for_one_identity_are_a_conflict(self):
        first = self.publish_knowledge(body="Primera revisión.\n")
        revised = revise(self.library, first.id)
        revised.content_path.write_text("Segunda revisión.\n", encoding="utf-8")
        second = approve(self.library, first.id,
                         review(self.library, first.id)["reviewed_sha256"])
        consumer, _ = self.product(
            "consumer",
            requires=[
                {"id": first.id, "kind": "knowledge", "revision": first.revision},
                {"id": first.id, "kind": "knowledge", "revision": second.revision},
            ],
        )
        catalog = Catalog(self.root, knowledge=self.library)
        with self.assertRaisesRegex(KoraError, "revisi|conflict|incompat"):
            catalog.dependencies(catalog.get(consumer), "codex")

    def test_phase_reuses_verified_snapshot_and_revalidate_detects_tampering(self):
        published = self.publish_knowledge(body="Contenido estable.\n")
        catalog = Catalog(self.library)
        path = published.content_path

        with catalog.phase():
            first = catalog.get(published.id)
            second = catalog.get(published.id)
            self.assertEqual(first.body, second.body)

        original = path.read_bytes()
        with catalog.phase():
            before = catalog.get(published.id).body
            with catalog.phase():
                self.assertEqual(catalog.get(published.id).body, before)
            path.write_bytes(b"Contenido alterado durante la fase.\n")
            self.assertEqual(catalog.get(published.id).body, before)
            with self.assertRaises(KoraError):
                catalog.revalidate()
            path.write_bytes(original)

        path.write_text("Alteración antes de una fase nueva.\n", encoding="utf-8")
        with self.assertRaises(KoraError):
            with catalog.phase():
                catalog.get(published.id)

    def test_get_outside_phase_verifies_each_reference_access(self):
        published = self.publish_knowledge(body="Consulta repetible.\n")
        catalog = Catalog(self.library)
        path = published.content_path
        catalog.get(published.id)
        path.write_text("Cambio fuera de una fase.\n", encoding="utf-8")
        with self.assertRaises(KoraError):
            catalog.get(published.id)

    def test_shared_graph_verifies_each_reference_once_per_phase_and_reports_work(self):
        published = self.publish_knowledge(body="Excepción compartida.\n" * 80)
        readers = [self.product(f"reader-{index}", requires=[published.id])[0]
                   for index in range(6)]
        catalog = Catalog(self.root, knowledge=self.library)
        verify = Catalog._verify_reference
        with patch.object(Catalog, "_verify_reference", wraps=verify) as checked:
            with catalog.phase():
                for identifier in readers:
                    build(catalog, "codex", [identifier])
            self.assertEqual(checked.call_count, 1)
            self.assertEqual(catalog.phase_metrics["reference_verifications"], 1)
            self.assertEqual(catalog.phase_metrics["objects"], 7)
            self.assertGreater(catalog.phase_metrics["bytes"], len(published.body.encode()))
            self.assertGreaterEqual(catalog.phase_metrics["seconds"], 0)
            with catalog.phase():
                catalog.get(published.id)
            self.assertEqual(checked.call_count, 2)

    def test_new_identity_collision_invalidates_prepared_view(self):
        identifier, _ = self.product("healthy")
        catalog = Catalog(self.root)
        with catalog.phase():
            catalog.get(identifier)
            self.product("collision", identifier=identifier)
            with self.assertRaisesRegex(KoraError, "[Cc]olisi|ambigua|duplicada"):
                catalog.revalidate()

    def resolver_command(self, files, identifier):
        for file in files.values():
            text = file.data.decode("utf-8")
            if "resolve URN" not in text:
                continue
            line = next(line for line in text.splitlines() if "resolve URN" in line)
            start = line.index("python3 ")
            end = line.index("`", start)
            command = line[start:end].replace("resolve URN", f"resolve {identifier}")
            return shlex.split(command)
        self.fail("La realización no emitió un comando resolver sustituible")

    def test_rendered_codex_and_hermes_resolver_use_independent_machinery_and_library_roots(self):
        published = self.publish_knowledge(body="Referencia accesible desde dos raíces.\n")
        skill, _ = self.product("reader", requires=[published.id], targets=("codex", "hermes"))
        catalog = Catalog(self.root, knowledge=self.library)
        outside = self.base / "unrelated-cwd"
        outside.mkdir()

        for target, renderer in (("codex", render_codex), ("hermes", render_hermes)):
            with self.subTest(target=target):
                files = renderer(catalog, catalog.get(skill))
                for identifier in (skill, published.id):
                    command = self.resolver_command(files, identifier)
                    self.assertEqual(command[command.index("--root") + 1], str(self.root.resolve()))
                    self.assertEqual(command[command.index("--knowledge-root") + 1],
                                     str(self.library.resolve()))
                    result = subprocess.run(
                        command,
                        cwd=outside,
                        capture_output=True,
                        text=True,
                        timeout=15,
                    )
                    self.assertEqual(result.returncode, 0, result.stderr)
                    resolved = json.loads(result.stdout)
                    self.assertEqual(resolved["id"], identifier)
                    expected = (catalog.get(identifier).content_path.resolve()
                                if identifier == published.id
                                else catalog.get(identifier).content_path.resolve())
                    self.assertEqual(Path(resolved["path"]).resolve(), expected)
                    self.assertEqual(resolved["kind"], "knowledge" if identifier == published.id else "skill")


if __name__ == "__main__":
    unittest.main()
