"""Licencias materiales de skills reescritas desde un upstream externo."""
import hashlib
import unittest
from pathlib import Path

import kora


RAIZ = Path(__file__).resolve().parent.parent
SKILLS = (
    RAIZ / "artefactos/skills/dev/code-review",
    RAIZ / "artefactos/skills/dev/diagnosing-bugs",
)
LICENCIA = "referencias/mattpocock-skills-MIT.txt"
SHA256_LICENCIA = (
    "a903dba3f386b6da71e42007dde288c022aec253058288a40814888cf6da9cd3"
)


class TestLicenciasSkillsVendorizadas(unittest.TestCase):

    def test_fuente_atribuye_licencia_y_bytes_estan_presentes(self):
        for skill in SKILLS:
            campos, _ = kora.parsear_archivo(
                (skill / "SKILL.md").read_text(encoding="utf-8"))
            self.assertIn(f"licencia MIT: {LICENCIA}", campos["fuente"])
            licencia = skill / LICENCIA
            self.assertTrue(licencia.is_file(), licencia)
            self.assertEqual(
                SHA256_LICENCIA,
                hashlib.sha256(licencia.read_bytes()).hexdigest(),
            )


if __name__ == "__main__":
    unittest.main()
