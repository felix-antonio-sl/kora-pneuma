# -*- coding: utf-8 -*-
"""Retiro de la skill genérica que perdió el dominio HODOM de su fuente."""
import unittest
from pathlib import Path

import kora


REPO = Path(__file__).resolve().parent.parent
SKILL = REPO / "artefactos/skills/kora/decision-operable/SKILL.md"
URN = "urn:kora:artefacto:decision-operable"


class TestDecisionOperable(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.campos, _ = kora.parsear_archivo(
            SKILL.read_text("utf-8"))

    def test_conserva_identidad_pero_queda_deprecada(self):
        self.assertEqual(self.campos["urn"], URN)
        self.assertEqual(self.campos["nombre"], "decision-operable")
        self.assertEqual(self.campos["version"], "1.0.0")
        self.assertEqual(self.campos["estado"], "deprecado")
        self.assertEqual(self.campos["forma"], "habilidad")


if __name__ == "__main__":
    unittest.main()
