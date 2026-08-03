"""Contrato documental de la skill scaffold-repo."""
import unittest
from pathlib import Path

import kora


RAIZ = Path(__file__).resolve().parent.parent
SKILL_DIR = RAIZ / "artefactos/skills/dev/scaffold-repo"
SKILL = SKILL_DIR / "SKILL.md"
REFS = SKILL_DIR / "referencias"


class TestScaffoldRepo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.campos, cls.cuerpo = kora.parsear_archivo(
            SKILL.read_text(encoding="utf-8"))

    def test_identidad_y_version_mayor(self):
        self.assertEqual(self.campos["urn"], "urn:dev:artefacto:scaffold-repo")
        self.assertEqual(self.campos["version"], "2.0.0")
        self.assertEqual(self.campos["estado"], "activo")
        self.assertEqual(self.campos["targets"], ["claude-code", "codex"])

    def test_claude_importa_exactamente_agents(self):
        self.assertEqual(
            (REFS / "claude-import.md").read_bytes(),
            b"@AGENTS.md\n",
        )
        self.assertIn("byte-equivalente a `@AGENTS.md\\n`", self.cuerpo)

    def test_referencias_son_minimas_y_sin_politica_anterior(self):
        self.assertEqual(
            {path.name for path in REFS.iterdir() if path.is_file()},
            {
                "README.md",
                "agents-conocimiento.md",
                "agents-cuaderno-rol.md",
                "agents-desarrollo.md",
                "agents-modelamiento.md",
                "claude-import.md",
                "gitignore-base",
            },
        )
        corpus = "\n".join(
            path.read_text(encoding="utf-8")
            for path in REFS.iterdir()
            if path.is_file()
        )
        self.assertNotIn("_archivo/", corpus)
        self.assertNotIn("handoff-AAAA-MM-DD", corpus)
        self.assertNotIn("BITACORA.md", corpus)

    def test_cada_arquetipo_custodia_continuidad_simple(self):
        for nombre in (
            "agents-desarrollo.md",
            "agents-conocimiento.md",
            "agents-cuaderno-rol.md",
            "agents-modelamiento.md",
        ):
            cuerpo = (REFS / nombre).read_text(encoding="utf-8")
            self.assertIn("`HANDOFF.md` es único, estable", cuerpo)
            self.assertIn("No crees `MEMORY.md`", cuerpo)
            self.assertIn("Git conserva la narrativa cerrada", cuerpo)
            self.assertTrue(cuerpo.startswith("# AGENTS.md\n"))


if __name__ == "__main__":
    unittest.main()
