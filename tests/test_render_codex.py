import tempfile
import tomllib
import unittest
from pathlib import Path

import yaml

from kora.catalog import Catalog, KoraError
from kora.render_codex import render


class CodexRenderTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="kora-codex-render-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def product(self, folder="witness", kind="skill", body="# Instrucciones\n", **updates):
        directory = self.root / "products" / "test" / folder
        directory.mkdir(parents=True)
        metadata = {
            "id": f"urn:test:{kind}:{folder}",
            "kind": kind,
            "name": folder,
            "description": "Comprueba la condición y conserva la excepción.",
            "content": "body.md",
            "targets": ["codex"],
        }
        metadata.update(updates)
        (directory / "object.yaml").write_text(yaml.safe_dump(metadata))
        (directory / "body.md").write_text(body)
        return directory

    def rendered(self, identifier="urn:test:skill:witness"):
        catalog = Catalog(self.root)
        return render(catalog, catalog.get(identifier))

    def test_skill_yaml_round_trip_preserves_special_text_and_exact_body(self):
        description = 'Reconoce \\d+; "sí": # excepción\nOtra línea: [unknown].'
        body = '# Fuente\n\nUsa `\\d+`; conserva "sí" y UNKNOWN.  \n\n'
        self.product(description=description, body=body)
        result = self.rendered()
        text = result[".agents/skills/witness/SKILL.md"].data.decode()
        header, emitted_body = text[4:].split("---\n\n", 1)
        self.assertEqual(yaml.safe_load(header), {"name": "witness", "description": description})
        self.assertTrue(emitted_body.startswith(body))
        self.assertIn(str(self.root), emitted_body)
        self.assertNotIn("kora-pneuma", emitted_body)
        self.assertEqual(set(result), {".agents/skills/witness/SKILL.md"})

    def test_skill_preserves_auxiliary_bytes_modes_and_excludes_source_metadata(self):
        directory = self.product()
        script = directory / "scripts" / "read.py"
        script.parent.mkdir()
        script.write_bytes(b"#!/usr/bin/env python3\nprint('source')\n")
        script.chmod(0o755)
        (directory / "sample.bin").write_bytes(bytes(range(256)))
        result = self.rendered()
        self.assertEqual(result[".agents/skills/witness/scripts/read.py"].data, script.read_bytes())
        self.assertEqual(result[".agents/skills/witness/scripts/read.py"].mode, 0o755)
        self.assertEqual(result[".agents/skills/witness/sample.bin"].data, bytes(range(256)))
        self.assertNotIn(".agents/skills/witness/object.yaml", result)
        self.assertNotIn(".agents/skills/witness/body.md", result)

    def test_agent_toml_contains_native_instructions_without_global_configuration(self):
        body = '# Agente\n"Comillas", \\rutas, ñ y control \x7f.\n'
        self.product(kind="agent", body=body)
        result = self.rendered("urn:test:agent:witness")
        self.assertEqual(set(result), {".codex/agents/witness.toml", ".agents/skills/witness/SKILL.md"})
        fields = tomllib.loads(result[".codex/agents/witness.toml"].data.decode())
        self.assertEqual(set(fields), {"name", "description", "developer_instructions"})
        self.assertEqual(fields["name"], "witness")
        self.assertTrue(fields["developer_instructions"].startswith(body))
        wrapper = result[".agents/skills/witness/SKILL.md"].data.decode()
        header, wrapper_body = wrapper[4:].split("---\n\n", 1)
        self.assertEqual(yaml.safe_load(header)["name"], "witness")
        self.assertIn("cuando el usuario pide", yaml.safe_load(header)["description"])
        self.assertTrue(wrapper_body.startswith(body))
        self.assertIn("No crea un proceso ni un agente separado", wrapper_body)
        self.assertIn("sesión conserva sus instrucciones", wrapper_body)

    def test_complete_dependency_closure_keeps_knowledge_readable_in_new_source(self):
        knowledge = self.product("conditions", "knowledge", body="Excepción: lluvia. Dato: UNKNOWN.\n", targets=[])
        self.product("lookup", requires=["urn:test:knowledge:conditions"])
        self.product(kind="agent", requires=["urn:test:skill:lookup"])
        result = self.rendered("urn:test:agent:witness")
        self.assertEqual(set(result), {".agents/skills/lookup/SKILL.md", ".codex/agents/witness.toml",
                                       ".agents/skills/witness/SKILL.md"})
        instructions = tomllib.loads(result[".codex/agents/witness.toml"].data.decode())["developer_instructions"]
        self.assertIn(str(knowledge / "body.md"), instructions)
        self.assertIn("`urn:test:knowledge:conditions`", instructions)
        self.assertIn("`$lookup`", instructions)
        self.assertEqual((knowledge / "body.md").read_text(), "Excepción: lluvia. Dato: UNKNOWN.\n")

    def test_direct_agent_activation_keeps_auxiliary_resources(self):
        directory = self.product(kind="agent")
        reference = directory / "references" / "context.md"
        reference.parent.mkdir()
        reference.write_text("Contexto que debe seguir accesible.\n")
        result = self.rendered("urn:test:agent:witness")
        self.assertEqual(result[".agents/skills/witness/references/context.md"].data,
                         reference.read_bytes())

    def test_missing_transitive_requirement_fails_before_rendering(self):
        self.product(requires=["urn:test:skill:lookup"])
        self.product("lookup", requires=["urn:test:knowledge:absent"])
        with self.assertRaisesRegex(KoraError, "urn:test:knowledge:absent"):
            self.rendered()

    def test_resource_collision_cannot_replace_the_native_skill(self):
        directory = self.product()
        (directory / "SKILL.md").write_text("Archivo auxiliar que no debe sobrescribir instrucciones.")
        with self.assertRaisesRegex(ValueError, "colisiona"):
            self.rendered()

    def test_two_dependencies_with_same_native_name_cannot_silently_overwrite(self):
        self.product(requires=["urn:test:skill:first", "urn:test:skill:second"])
        self.product("first", name="same")
        self.product("second", name="same")
        with self.assertRaisesRegex(ValueError, "colisionan"):
            self.rendered()

    def test_skill_description_limit_is_checked_at_native_boundary(self):
        self.product(description="x" * 1025)
        with self.assertRaisesRegex(ValueError, "1024"):
            self.rendered()


if __name__ == "__main__":
    unittest.main()
