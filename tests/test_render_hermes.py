from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

import yaml

from kora.catalog import Catalog, KoraError
from kora.render_hermes import render


class HermesRenderTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def product(self, namespace, name, kind, body, requires=(), resources=None):
        directory = self.root / "products" / namespace / name
        directory.mkdir(parents=True)
        identity = f"urn:{namespace}:artefacto:{name}"
        metadata = {
            "id": identity,
            "kind": kind,
            "name": name,
            "description": f"Prueba de {name}: condiciones, límites y recuperación.",
            "content": "content.md",
            "targets": ["codex", "hermes"],
            "requires": list(requires),
        }
        (directory / "object.yaml").write_text(yaml.safe_dump(metadata), encoding="utf-8")
        (directory / "content.md").write_text(body, encoding="utf-8")
        for relative, (data, mode) in (resources or {}).items():
            path = directory / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            path.chmod(mode)
        return identity

    def test_skill_keeps_body_resources_and_resolvable_knowledge(self):
        knowledge = self.product("test", "reference", "knowledge", "Dato con excepción: desconocido.\n")
        body = "# Método\n\nConserva esta condición y la excepción.\n"
        skill = self.product(
            "test", "method", "skill", body, [knowledge],
            {"scripts/run.sh": (b"#!/bin/sh\nexit 0\n", 0o755), "assets/data.bin": (b"\x00\xff", 0o644)},
        )
        catalog = Catalog(self.root)
        files = render(catalog, catalog.get(skill))
        content = files[".hermes/skills/method/SKILL.md"].data.decode("utf-8")
        self.assertIn(body, content)
        metadata = yaml.safe_load(content.split("---", 2)[1])
        self.assertEqual(metadata["name"], "method")
        self.assertEqual(metadata["metadata"]["kora_id"], skill)
        self.assertIn(str(catalog.get(knowledge).content_path.resolve()), content)
        self.assertEqual(files[".hermes/skills/method/assets/data.bin"].data, b"\x00\xff")
        self.assertEqual(files[".hermes/skills/method/scripts/run.sh"].mode & 0o777, 0o755)

    def test_source_relative_guide_is_recoverable_outside_installed_bundle(self):
        guide = self.root / "docs/operacion.md"
        guide.parent.mkdir()
        guide.write_text("Guía del ensayo.\n", encoding="utf-8")
        body = "Lee la [guía](../../../docs/operacion.md).\n"
        skill = self.product("test", "method", "skill", body)
        catalog = Catalog(self.root)
        product = catalog.get(skill)
        files = render(catalog, product)
        installed = self.root / "home/.hermes/skills/method/SKILL.md"
        installed.parent.mkdir(parents=True)
        content = files[".hermes/skills/method/SKILL.md"].data.decode("utf-8")
        installed.write_text(content, encoding="utf-8")
        relative = "../../../docs/operacion.md"
        self.assertFalse((installed.parent / relative).exists())
        self.assertEqual((product.content_path.parent / relative).read_text(), "Guía del ensayo.\n")
        self.assertIn(body, content)
        self.assertIn(f"Referencias relativas del cuerpo: base `{product.content_path.parent.resolve()}`", content)
        self.assertIn("`read_file`", content)
        self.assertIn("`skill_view` solo abre recursos internos del bundle", content)

    def test_agent_packages_transitive_skills_with_explicit_file_ownership(self):
        secondary = self.product("test", "secondary", "skill", "Procedimiento auxiliar.\n")
        primary = self.product("test", "primary", "skill", "Procedimiento principal.\n", [secondary])
        agent = self.product(
            "test", "advisor", "agent", "# Asesor\n\nConduce el método.\n", [primary],
            {"config.yaml": (b"example: true\n", 0o644), "scripts/check.sh": (b"#!/bin/sh\nexit 0\n", 0o755)},
        )
        catalog = Catalog(self.root)
        files = render(catalog, catalog.get(agent))
        prefix = ".hermes/profiles/advisor/"
        self.assertIn(prefix + "skills/primary/SKILL.md", files)
        self.assertIn(prefix + "skills/secondary/SKILL.md", files)
        self.assertNotIn(prefix + "config.yaml", files)
        self.assertEqual(files[prefix + "resources/config.yaml"].data, b"example: true\n")
        self.assertEqual(files[prefix + "resources/scripts/check.sh"].mode, 0o755)
        self.assertFalse(any("memories/" in path or path.endswith("auth.json") for path in files))
        manifest = yaml.safe_load(files[prefix + "distribution.yaml"].data)
        self.assertEqual(set(manifest["distribution_owned"]), {path[len(prefix):] for path in files})
        self.assertNotIn("source", manifest)
        self.assertNotIn("skills", manifest["distribution_owned"])

    def test_agent_requirement_fails_instead_of_pretending_invocation(self):
        other = self.product("test", "other", "agent", "Otra identidad.\n")
        agent = self.product("test", "advisor", "agent", "Asesor.\n", [other])
        catalog = Catalog(self.root)
        with self.assertRaisesRegex(KoraError, "perfil Hermes"):
            render(catalog, catalog.get(agent))

    def test_native_skill_resource_collision_is_rejected(self):
        skill = self.product("test", "method", "skill", "Método.\n", resources={"SKILL.md": (b"local", 0o644)})
        catalog = Catalog(self.root)
        with self.assertRaisesRegex(KoraError, "colisiona"):
            render(catalog, catalog.get(skill))

    def test_missing_dependency_cannot_emit_a_partial_profile(self):
        agent = self.product("test", "advisor", "agent", "Asesor.\n", ["urn:test:artefacto:missing"])
        with self.assertRaises(KoraError):
            catalog = Catalog(self.root)
            render(catalog, catalog.get(agent))

    def test_files_parse_with_installed_hermes(self):
        hermes = Path(os.environ.get("HERMES_SOURCE", Path.home() / ".hermes/hermes-agent"))
        interpreter = hermes / "venv/bin/python"
        if not interpreter.is_file():
            self.skipTest("No está disponible el Python del Hermes instalado")
        skill = self.product("test", "method", "skill", "Conserva incertidumbre.\n")
        agent = self.product("test", "advisor", "agent", "Asesor.\n", [skill])
        catalog = Catalog(self.root)
        files = render(catalog, catalog.get(agent))
        target = self.root / "native"
        for relative, file in files.items():
            path = target / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(file.data)
        native_code = """
import json, sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
from hermes_cli.profile_distribution import read_manifest
from agent.skill_utils import parse_frontmatter
profile = Path(sys.argv[2])
manifest = read_manifest(profile)
metadata, body = parse_frontmatter((profile / 'skills/method/SKILL.md').read_text())
print(json.dumps({'name': manifest.name, 'owned': manifest.distribution_owned,
                  'skill': metadata['name'], 'body_present': 'Conserva incertidumbre.' in body}))
"""
        environment = {"PATH": os.defpath, "HERMES_HOME": str(target / "isolated-home"), "PYTHONDONTWRITEBYTECODE": "1"}
        result = subprocess.run(
            [str(interpreter), "-c", native_code, str(hermes), str(target / ".hermes/profiles/advisor")],
            cwd=target, env=environment, text=True, capture_output=True, check=True, timeout=30,
        )
        parsed = json.loads(result.stdout)
        self.assertEqual(parsed["name"], "advisor")
        self.assertEqual(parsed["skill"], "method")
        self.assertTrue(parsed["body_present"])
        self.assertIn("skills/method/SKILL.md", parsed["owned"])


if __name__ == "__main__":
    unittest.main()
