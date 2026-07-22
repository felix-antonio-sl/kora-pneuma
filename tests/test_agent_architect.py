# -*- coding: utf-8 -*-
"""Contrato vigente del subagente KORA agent-architect."""
import unittest
from pathlib import Path

import kora


RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "artefactos/agentes/dev/agent-architect.md"
CONTRATO = "urn:kora:kb:cat-contrato-ingenieria-agentica"


class TestAgentArchitectContrato(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.campos, cls.cuerpo = kora.parsear_archivo(
            FUENTE.read_text("utf-8"))

    def test_es_subagente_persona_codex_only(self):
        self.assertEqual(
            self.campos["urn"], "urn:dev:artefacto:agent-architect")
        self.assertEqual(self.campos["estado"], "activo")
        self.assertEqual(self.campos["forma"], "subagente")
        self.assertEqual(self.campos["arnes"], "persona")
        self.assertEqual(self.campos["targets"], ["codex"])

    def test_conoce_el_contrato_agentico_vigente(self):
        self.assertIn(CONTRATO, self.campos["conocimiento"])
        for nivel in ("Spec(a)", "Model(a)", "Runtime_T(a,r)"):
            self.assertIn(nivel, self.cuerpo)
        self.assertIn("I`, `O`", self.cuerpo)
        self.assertIn("`U`, `M`, `step`", self.cuerpo)

    def test_clasifica_las_cuatro_formas(self):
        for forma in (
                "`forma=habilidad`", "`forma=subagente`",
                "`forma=agente`", "`forma=plataforma`"):
            self.assertIn(forma, self.cuerpo)

    def test_herramientas_declaran_pero_no_prueban_enforcement(self):
        cuerpo_normalizado = " ".join(self.cuerpo.split())
        self.assertNotIn(
            "Las herramientas son enforcement de scope", self.cuerpo)
        self.assertIn(
            "la autoridad efectiva se verifica por target y runtime",
            cuerpo_normalizado)
        self.assertIn("no prueba least-privilege", self.cuerpo)


if __name__ == "__main__":
    unittest.main()
