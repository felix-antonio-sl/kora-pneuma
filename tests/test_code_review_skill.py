"""Prueba focal de identidad y contrato operativo de la skill code-review."""
import re
import unittest
from pathlib import Path

import kora


RAIZ = Path(__file__).resolve().parent.parent
SKILL = RAIZ / "artefactos/skills/dev/code-review/SKILL.md"
BASELINE = SKILL.parent / "referencias/smell-baseline.md"
LICENSE = SKILL.parent / "referencias/mattpocock-skills-MIT.txt"
URN = "urn:dev:artefacto:code-review"
UPSTREAM_COMMIT = "2ab958093e83e0ec752e6c1c5932da465bf23e0c"
UPSTREAM_SHA256 = "6a65cc61114f96db07ec41e3920e67c9c5bf70dd6e0901eb9460ebcb2bdc209f"


class TestCodeReviewSkill(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.campos, cls.cuerpo = kora.parsear_archivo(
            SKILL.read_text(encoding="utf-8"))
        cls.normalizado = " ".join(cls.cuerpo.split())
        cls.baseline = BASELINE.read_text(encoding="utf-8")
        cls.license = LICENSE.read_text(encoding="utf-8")

    def test_identidad_y_firma_kora(self):
        self.assertEqual(SKILL, RAIZ / "artefactos/skills/dev/code-review/SKILL.md")
        self.assertEqual(self.campos["urn"], URN)
        self.assertEqual(self.campos["nombre"], "code-review")
        self.assertEqual(self.campos["version"], "1.0.0")
        self.assertEqual(self.campos["estado"], "activo")
        self.assertEqual(self.campos["arnes"], "disciplina")
        self.assertEqual(self.campos["forma"], "habilidad")
        self.assertEqual(self.campos["vector"], [2, 0, 2, 0, 1])
        self.assertEqual(self.campos["sigma"], [2, 1, 3, 2, 1])
        self.assertEqual(self.campos["targets"], ["codex"])

    def test_procedencia_y_herramientas_read_only_minimas(self):
        self.assertIn(
            "mattpocock/skills/skills/engineering/code-review/SKILL.md",
            self.campos["fuente"],
        )
        self.assertIn(UPSTREAM_COMMIT, self.campos["fuente"])
        self.assertIn(f"sha256:{UPSTREAM_SHA256}", self.campos["fuente"])
        self.assertIn("referencias/mattpocock-skills-MIT.txt", self.campos["fuente"])
        self.assertNotIn("/tmp/", self.campos["fuente"])
        self.assertNotIn("/home/", self.campos["fuente"])
        self.assertTrue(LICENSE.is_file())
        self.assertIn("Copyright (c) 2026 Matt Pocock", self.license)
        self.assertIn("Permission is hereby granted", self.license)
        self.assertEqual(self.campos["herramientas"], ["Read", "Glob", "Grep", "Bash"])
        self.assertNotIn("Write", self.campos["herramientas"])
        self.assertNotIn("Edit", self.campos["herramientas"])
        self.assertIn("read-only", self.cuerpo)

    def test_fixed_point_y_fallo_temprano(self):
        for testigo in (
                "punto fijo", "git rev-parse --verify <fixed-point>^{commit}",
                "git rev-parse --verify HEAD^{commit}",
                "git diff <fixed-commit>...<head-commit>",
                "git log <fixed-commit>..<head-commit> --oneline",
                "ref no resuelve", "diff es vacío", "FAIL", "BLOCKED",
                "resolver `HEAD` otra vez", "candidate-mismatch",
                "árbol Git del commit resuelto"):
            self.assertIn(testigo, self.normalizado)

    def test_dos_ejes_aislados_y_spec_absent(self):
        for testigo in (
                "**Standards**", "**Spec**", "eje Standards", "eje Spec",
                "**Spec** como `ABSENT`", "Standards y Spec", "sin fusionar",
                "sin rerankear", "sin ganador global", "context.spec_source",
                "no sustituir silenciosamente", "`FAIL` y `BLOCKED`"):
            self.assertIn(testigo, self.normalizado)

    def test_topologia_central_un_nivel_y_contrato_fugaz(self):
        for testigo in (
                "Steipete es la central", "dos sesiones o `agent threads` Fugaz",
                "nuevos y aislados", "hace el `join`", "un solo nivel",
                "no se coordinan lateralmente", "no crean descendencia",
                "no es un agente ni un suborquestador", "`I_task`", "`O_task`",
                "nombres de modelo", "runtime"):
            self.assertIn(testigo, self.normalizado)

    def test_citas_y_recibo_epistemicamente_honesto(self):
        for testigo in (
                "árbol Git del commit resuelto", "path, línea o hunk",
                "citas de cada hallazgo",
                "evidence", "limits", "`PASS`", "`FAIL`", "`ABSENT`", "`NOT_RUN`",
                "smell siempre es un juicio", "estándar local documentado prevalece"):
            self.assertIn(testigo.lower(), self.normalizado.lower())

    def test_baseline_completo_y_referenciado(self):
        self.assertTrue(BASELINE.is_file())
        self.assertIn("`referencias/smell-baseline.md`", self.cuerpo)
        self.assertIn("no es una reproducción literal", self.baseline)
        self.assertIn(UPSTREAM_COMMIT, self.baseline)
        for smell in (
                "Mysterious Name", "Duplicated Code", "Feature Envy",
                "Data Clumps", "Primitive Obsession", "Repeated Switches",
                "Shotgun Surgery", "Divergent Change", "Speculative Generality",
                "Message Chains", "Middle Man", "Refused Bequest"):
            self.assertIn(smell, self.baseline)

    def test_no_fusion_ni_nombres_de_modelo(self):
        self.assertIn("ganador global", self.normalizado.lower())
        self.assertNotRegex(
            self.normalizado.lower(),
            re.compile(r"\b(?:gpt|claude|sonnet|opus|gemini|llama)\b|\bgpt-[\w.-]+\b"),
        )


if __name__ == "__main__":
    unittest.main()
