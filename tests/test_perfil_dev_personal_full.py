# -*- coding: utf-8 -*-
"""Contrato del perfil privado mono-usuario para datos reales."""
import unittest
from pathlib import Path

import kora


RAIZ = Path(__file__).resolve().parent.parent
PROFILE = (
    RAIZ
    / "artefactos/conocimiento/salud/perfil-dev-personal-full.md"
)


class TestPerfilDevPersonalFull(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.campos, cls.cuerpo = kora.parsear_archivo(
            PROFILE.read_text("utf-8"))
        cls.normalizado = " ".join(cls.cuerpo.split())

    def test_identidad_y_estado(self):
        self.assertEqual(
            self.campos["urn"],
            "urn:salud:kb:perfil-dev-personal-full")
        self.assertEqual(self.campos["version"], "1.0.0")
        self.assertEqual(self.campos["estado"], "publicado")

    def test_habilita_datos_reales_en_superficie_privada(self):
        for testigo in (
                "procesar, persistir, recuperar, cruzar y visualizar PII/PHI",
                "Drive",
                "`hsc-agent-cli`",
                "bases persistentes",
                "mismo operador"):
            self.assertIn(testigo, self.normalizado)

    def test_conserva_fronteras_no_relajadas(self):
        for testigo in (
                "**Secretos:** credenciales",
                "repositorios Git, commits, PR",
                "destinatario nuevo",
                "decisión clínica final",
                "`INSTITUTIONAL_CONTROLLED`"):
            self.assertIn(testigo, self.normalizado)


if __name__ == "__main__":
    unittest.main()
