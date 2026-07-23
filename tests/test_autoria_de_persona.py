# -*- coding: utf-8 -*-
"""Regresiones doctrinales de la skill autoria-de-persona."""
import unittest
from pathlib import Path

import kora


RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "artefactos/skills/kora/autoria-de-persona/SKILL.md"


class TestAutoriaDePersona(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.campos, cls.cuerpo = kora.parsear_archivo(
            FUENTE.read_text("utf-8"))

    def test_vector_es_firma_clasificatoria_no_tipo(self):
        cuerpo_normalizado = " ".join(self.cuerpo.split())
        self.assertEqual(self.campos["version"], "1.2.1")
        self.assertNotIn("vector = tipo", cuerpo_normalizado)
        self.assertIn(
            "vector = firma clasificatoria", cuerpo_normalizado)
        self.assertIn(
            "URN = identidad nominal", cuerpo_normalizado)


if __name__ == "__main__":
    unittest.main()
