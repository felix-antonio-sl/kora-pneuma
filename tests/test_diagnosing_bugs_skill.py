# -*- coding: utf-8 -*-
"""Contrato focal de la skill KORA diagnosing-bugs."""
import re
import unittest
from pathlib import Path

import kora


RAIZ = Path(__file__).resolve().parent.parent
SKILL = RAIZ / "artefactos/skills/dev/diagnosing-bugs/SKILL.md"
LICENSE = SKILL.parent / "referencias/mattpocock-skills-MIT.txt"
URN = "urn:dev:artefacto:diagnosing-bugs"
UPSTREAM_COMMIT = "2ab958093e83e0ec752e6c1c5932da465bf23e0c"
UPSTREAM_SHA = (
    "7a0779480f323a66d109404646bcc1a14bf0232b45b3e3ea93b652a035718acb"
)


class TestDiagnosingBugsSkill(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.campos, cls.cuerpo = kora.parsear_archivo(
            SKILL.read_text(encoding="utf-8"))
        cls.normalizado = " ".join(cls.cuerpo.split())
        cls.license = LICENSE.read_text(encoding="utf-8")

    def test_identidad_y_forma_kora(self):
        self.assertEqual(self.campos["urn"], URN)
        self.assertEqual(self.campos["nombre"], "diagnosing-bugs")
        self.assertEqual(self.campos["version"], "1.0.0")
        self.assertEqual(self.campos["estado"], "activo")
        self.assertEqual(self.campos["arnes"], "disciplina")
        self.assertEqual(self.campos["forma"], "habilidad")
        self.assertEqual(self.campos["vector"], [2, 0, 2, 0, 1])
        self.assertEqual(self.campos["sigma"], [2, 1, 3, 2, 1])
        self.assertEqual(self.campos["targets"], ["codex"])
        self.assertEqual(
            self.campos["herramientas"],
            ["Read", "Grep", "Glob", "Write", "Edit", "Bash"],
        )

    def test_procedencia_upstream_y_reescritura(self):
        fuente = self.campos["fuente"]
        self.assertIn(UPSTREAM_COMMIT, fuente)
        self.assertIn(f"sha256:{UPSTREAM_SHA}", fuente)
        self.assertIn(
            "mattpocock/skills/skills/engineering/diagnosing-bugs/SKILL.md",
            fuente,
        )
        self.assertIn("referencias/mattpocock-skills-MIT.txt", fuente)
        self.assertNotIn("mattpocock-skills-study", fuente)
        self.assertNotIn("/tmp/", fuente)
        self.assertNotIn("/home/", fuente)
        self.assertTrue(LICENSE.is_file())
        self.assertIn("Copyright (c) 2026 Matt Pocock", self.license)
        self.assertIn("Permission is hereby granted", self.license)
        self.assertNotIn("Everything else is mechanical", self.cuerpo)
        self.assertNotIn("Be aggressive. Be creative.", self.cuerpo)

    def test_loop_es_gate_y_conserva_alternativas(self):
        for testigo in (
                "gate previo a toda hipótesis",
                "red-capaz",
                "test fallido",
                "curl",
                "CLI",
                "navegador headless",
                "replay",
                "harness descartable",
                "fuzz",
                "bisección",
                "loop diferencial",
                "script HITL",
                "caso no determinista",
                "bloqueo honesto",
                "Sin bucle no formular hipótesis"):
            self.assertIn(testigo, self.normalizado)

    def test_fases_de_razonamiento_observable_y_seams(self):
        for fase in range(1, 7):
            self.assertIn(f"## Fase {fase}", self.cuerpo)
        self.assertEqual(
            self.cuerpo.count("Criterio de completitud comprobable"), 6)
        for testigo in (
                "3–5 hipótesis rankeadas",
                "predicción observable",
                "checkpoint humano no bloqueante",
                "una sola variable",
                "Rama de rendimiento",
                "baseline",
                "test de regresión antes del fix",
                "seam correcto",
                "rojo antes del fix",
                "verde después",
                "post-mortem"):
            self.assertIn(testigo, self.normalizado)

    def test_honestidad_epistemica_y_evidencia_ligada(self):
        for estado in ("PASS", "FAIL", "ABSENT", "NOT_RUN"):
            self.assertIn(estado, self.cuerpo)
        for testigo in (
                "candidato evaluado",
                "commit o árbol",
                "observación",
                "límite de inferencia",
                "suite",
                "aceptación humana",
                "causalidad universal",
                "runtime"):
            self.assertIn(testigo, self.normalizado)
        self.assertIn("No fijar nombres de modelo", self.normalizado)
        self.assertIn("niveles de razonamiento", self.cuerpo)
        self.assertIn("suite amplia que no pueda ponerse roja", self.cuerpo)

    def test_no_fija_nombres_de_modelo(self):
        nombres_de_modelo = re.compile(
            r"\b(?:gpt|claude|gemini|llama|deepseek|sonnet|opus)"
            r"(?:[- ][a-z0-9.]+)?\b",
            re.IGNORECASE,
        )
        self.assertIsNone(nombres_de_modelo.search(self.cuerpo))


if __name__ == "__main__":
    unittest.main()
