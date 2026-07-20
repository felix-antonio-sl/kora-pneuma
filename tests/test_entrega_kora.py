# -*- coding: utf-8 -*-
"""Contrato del primer corte vertical de UX agéntica entrega-kora."""
import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

import kora

RAIZ = Path(__file__).resolve().parent.parent
SKILL = RAIZ / "artefactos/skills/kora/entrega-kora/SKILL.md"
HELPER = (
    RAIZ
    / "artefactos/skills/kora/entrega-kora/referencias/entrega.py"
)
SPEC = importlib.util.spec_from_file_location("entrega_kora_helper", HELPER)
assert SPEC is not None and SPEC.loader is not None
entrega = importlib.util.module_from_spec(SPEC)
_dont_write_bytecode = sys.dont_write_bytecode
sys.dont_write_bytecode = True
try:
    SPEC.loader.exec_module(entrega)
finally:
    sys.dont_write_bytecode = _dont_write_bytecode


def result(code=0, stdout="", stderr=""):
    return subprocess.CompletedProcess([], code, stdout, stderr)


class TestEntregaKoraContrato(unittest.TestCase):

    def test_skill_es_codex_only_y_no_instaladora(self):
        campos, cuerpo = kora.parsear_archivo(SKILL.read_text("utf-8"))
        self.assertEqual(campos["urn"], "urn:kora:artefacto:entrega-kora")
        self.assertEqual(campos["estado"], "activo")
        self.assertEqual(campos["targets"], ["codex"])
        self.assertEqual(campos["alcance"], "usuario")
        self.assertEqual(campos["herramientas"], ["Bash"])
        self.assertIn("Nunca ejecutar `--aplicar`", cuerpo)
        self.assertNotIn("transmutar --urn U --target T --aplicar", cuerpo)
        self.assertFalse((HELPER.parent / "__pycache__").exists())

    def test_descubrimiento_exacto_no_promueve_sugerencia(self):
        entries = [
            {"urn": "urn:kora:artefacto:cat-thinking",
             "nombre": "cat-thinking", "tipo": "skill", "version": "2.1.1",
             "estado": "activo",
             "path": "artefactos/skills/kora/cat-thinking/SKILL.md"},
        ]
        exact = entrega.discover(entries, "cat-thinking")
        normalized = entrega.discover(entries, "Cat-Thinking")
        partial = entrega.discover(entries, "cat")
        self.assertEqual(exact["status"], "resolved")
        self.assertEqual(normalized["status"], "resolved")
        self.assertEqual(partial["status"], "not-found")
        self.assertEqual(partial["suggestion_count"], 1)

    def test_nombre_duplicado_es_ambiguo(self):
        entries = [
            {"urn": "urn:a:artefacto:util", "nombre": "util", "tipo": "skill",
             "version": "1.0.0", "estado": "activo", "path": "a"},
            {"urn": "urn:b:artefacto:util", "nombre": "util", "tipo": "skill",
             "version": "1.0.0", "estado": "activo", "path": "b"},
        ]
        found = entrega.discover(entries, "util")
        self.assertEqual(found["status"], "ambiguous")
        self.assertEqual(len(found["candidates"]), 2)

    def test_caso_skill_cierra_paridad_sin_aplicar(self):
        entries = [{
            "urn": "urn:kora:artefacto:cat-thinking",
            "nombre": "cat-thinking",
            "tipo": "skill",
            "version": "2.1.1",
            "estado": "activo",
            "path": "artefactos/skills/kora/cat-thinking/SKILL.md",
        }]
        commands = []
        emitted = False

        def fake(argv):
            nonlocal emitted
            commands.append(argv)
            joined = " ".join(argv)
            if joined.endswith("censo --json"):
                return result(stdout=json.dumps(entries))
            if "transmutar --urn" in joined:
                emitted = True
            if joined.endswith("velar --estricto") and not emitted:
                return result(code=1, stderr="sello rancio")
            if "transmutar --paridad" in joined:
                return result(stdout=(
                    "paridad: fiel          codex  cat-thinking\n"
                    "paridad: 1 fiel · 0 desviadas · "
                    "0 no-instaladas · 0 sin-emision.\n"))
            return result(stdout="ok\n")

        receipt, code = entrega.execute(
            RAIZ, "cat-thinking", "codex", fake)
        self.assertEqual(code, 0)
        self.assertEqual(receipt["status"], "parity-faithful")
        self.assertTrue(receipt["mutation"]["derived_emission"])
        self.assertFalse(receipt["mutation"]["runtime_apply"])
        flattened = [part for command in commands for part in command]
        self.assertNotIn("--aplicar", flattened)
        self.assertNotIn("ciclo", flattened)
        self.assertEqual(
            sum("transmutar --paridad" in " ".join(c) for c in commands), 1)
        joined_commands = [" ".join(command) for command in commands]
        emission_i = next(
            i for i, command in enumerate(joined_commands)
            if "transmutar --urn" in command)
        validation_i = next(
            i for i, command in enumerate(joined_commands)
            if command.endswith("velar --estricto"))
        self.assertLess(emission_i, validation_i)

    def test_conocimiento_no_intenta_transmutar(self):
        entries = [{
            "urn": "urn:kora:kb:cat-kora-semantica-operacional",
            "nombre": "cat-kora-semantica-operacional",
            "tipo": "conocimiento",
            "version": "1.0.0",
            "estado": "publicado",
            "path": (
                "artefactos/conocimiento/kora/"
                "cat-kora-semantica-operacional.md"),
        }]
        commands = []

        def fake(argv):
            commands.append(argv)
            if " ".join(argv).endswith("censo --json"):
                return result(stdout=json.dumps(entries))
            return result(stdout="ok\n")

        receipt, code = entrega.execute(
            RAIZ, "cat-kora-semantica-operacional", "codex", fake)
        self.assertEqual(code, 0)
        self.assertEqual(receipt["status"], "knowledge-validated")
        self.assertEqual(receipt["checks"]["parity"], "not-applicable")
        self.assertFalse(any("transmutar" in command for command in commands))

    def test_conocimiento_no_publicado_bloquea_lifecycle(self):
        entries = [{
            "urn": "urn:kora:kb:nota-x",
            "nombre": "nota-x",
            "tipo": "conocimiento",
            "version": "1.0.0",
            "estado": "borrador",
            "path": "artefactos/conocimiento/kora/nota-x.md",
        }]
        commands = []

        def fake(argv):
            commands.append(argv)
            if " ".join(argv).endswith("censo --json"):
                return result(stdout=json.dumps(entries))
            return result(stdout="ok\n")

        receipt, code = entrega.execute(RAIZ, "nota-x", "codex", fake)
        self.assertEqual(code, 1)
        self.assertEqual(receipt["status"], "blocked")
        self.assertEqual(receipt["stage"], "lifecycle")
        self.assertFalse(any("-m" in command for command in commands))

    def test_paridad_sin_unidades_no_es_falso_fiel(self):
        entries = [{
            "urn": "urn:kora:artefacto:cat-thinking",
            "nombre": "cat-thinking",
            "tipo": "skill",
            "version": "2.1.1",
            "estado": "activo",
            "path": "artefactos/skills/kora/cat-thinking/SKILL.md",
        }]

        def fake(argv):
            joined = " ".join(argv)
            if joined.endswith("censo --json"):
                return result(stdout=json.dumps(entries))
            if "transmutar --paridad" in joined:
                return result(stdout=(
                    "paridad: 0 fiel · 0 desviadas · "
                    "0 no-instaladas · 0 sin-emision.\n"))
            return result(stdout="ok\n")

        receipt, code = entrega.execute(
            RAIZ, "cat-thinking", "codex", fake)
        self.assertEqual(code, 2)
        self.assertEqual(receipt["status"], "observation-error")
        self.assertEqual(receipt["stage"], "parity")

    def test_fallo_paridad_sin_resumen_es_bloqueo(self):
        entries = [{
            "urn": "urn:kora:artefacto:cat-thinking",
            "nombre": "cat-thinking",
            "tipo": "skill",
            "version": "2.1.1",
            "estado": "activo",
            "path": "artefactos/skills/kora/cat-thinking/SKILL.md",
        }]

        def fake(argv):
            joined = " ".join(argv)
            if joined.endswith("censo --json"):
                return result(stdout=json.dumps(entries))
            if "transmutar --paridad" in joined:
                return result(code=1, stderr="drift no resumido")
            return result(stdout="ok\n")

        receipt, code = entrega.execute(
            RAIZ, "cat-thinking", "codex", fake)
        self.assertEqual(code, 1)
        self.assertEqual(receipt["status"], "blocked")
        self.assertEqual(receipt["stage"], "parity")

    def test_target_fuera_del_corte_falla_sin_comandos(self):
        commands = []
        receipt, code = entrega.execute(
            RAIZ, "cat-thinking", "openclaw",
            lambda argv: commands.append(argv))
        self.assertEqual(code, 1)
        self.assertEqual(receipt["status"], "unsupported-target")
        self.assertEqual(commands, [])


if __name__ == "__main__":
    unittest.main()
