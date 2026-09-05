# -*- coding: utf-8 -*-
"""Contrato material y de distribución de director-tecnico-hodom."""
import subprocess
import sys
import unittest
from pathlib import Path

import kora


REPO = Path(__file__).resolve().parent.parent
AGENT = REPO / "artefactos/agentes/salud/director-tecnico-hodom.md"
ROLE = REPO / "artefactos/agentes/salud/hodom-hsc-direccion-tecnica.md"
DOMAIN = (
    REPO
    / "artefactos/skills/salud/hospitalizacion-domiciliaria/SKILL.md"
)
URN = "urn:salud:artefacto:director-tecnico-hodom"


class TestDirectorTecnicoHodom(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if AGENT.is_file():
            cls.fields, cls.body = kora.parsear_archivo(
                AGENT.read_text("utf-8"))
        else:
            cls.fields, cls.body = None, ""
        cls.role_fields, _ = kora.parsear_archivo(ROLE.read_text("utf-8"))
        cls.domain_fields, _ = kora.parsear_archivo(
            DOMAIN.read_text("utf-8"))

    def test_es_una_persona_directamente_invocable_en_ambos_targets(self):
        self.assertIsNotNone(self.fields, "falta la fuente del agente")
        self.assertEqual(self.fields["urn"], URN)
        self.assertEqual(self.fields["nombre"], "director-tecnico-hodom")
        self.assertEqual(self.fields["version"], "1.0.0")
        self.assertEqual(self.fields["estado"], "activo")
        self.assertEqual(self.fields["forma"], "agente")
        self.assertEqual(self.fields["arnes"], "persona")
        self.assertEqual(self.fields["alcance"], "usuario")
        self.assertEqual(self.fields["targets"], ["codex", "hermes"])
        self.assertEqual(self.fields["vector"], [3, 2, 3, 1, 2])
        self.assertEqual(self.fields["sigma"], [3, 3, 3, 3, 3])

    def test_depende_de_las_dos_disciplinas_hodom_distribuibles(self):
        self.assertIsNotNone(self.fields, "falta la fuente del agente")
        self.assertEqual(
            self.fields["depende"],
            [
                "urn:salud:artefacto:conducir-decisiones-hodom",
                "urn:salud:artefacto:hospitalizacion-domiciliaria",
            ],
        )
        self.assertIn("hermes", self.domain_fields["targets"])

    def test_no_reemplaza_al_rol_sintetico_situado(self):
        self.assertIsNotNone(self.fields, "falta la fuente del agente")
        self.assertEqual(
            self.role_fields["urn"],
            "urn:salud:artefacto:hodom-hsc-direccion-tecnica",
        )
        self.assertEqual(self.role_fields["estado"], "activo")
        self.assertEqual(self.role_fields["forma"], "subagente")
        self.assertEqual(self.role_fields["alcance"], "proyecto")
        self.assertNotIn("reemplaza", self.fields)

    def test_porta_contrato_directivo_y_personalidad_del_faro(self):
        self.assertIsNotNone(self.fields, "falta la fuente del agente")
        normalized = " ".join(self.body.split()).lower()
        self.assertIn("<!-- kora:soul -->", self.body)
        self.assertIn("<!-- kora:soul:fin -->", self.body)
        for witness in (
            "fin", "razono desde el fracaso", "organización, no por fuerza",
            "registro", "c sobre b", "`i_self`", "`o_self`",
            "authority_gap", "real_data_not_authorized",
            "no_material_witness", "spec", "model", "runtime",
        ):
            self.assertIn(witness, normalized)

    def test_transmuta_con_dependencias_en_codex_y_hermes(self):
        self.assertIsNotNone(self.fields, "falta la fuente del agente")
        expected = {
            "codex": (
                "codex/skills/conducir-decisiones-hodom/SKILL.md",
                "codex/skills/hospitalizacion-domiciliaria/SKILL.md",
                "codex/agents/director-tecnico-hodom.toml",
                "codex/skills/director-tecnico-hodom/SKILL.md",
            ),
            "hermes": (
                "hermes/skills/conducir-decisiones-hodom/SKILL.md",
                "hermes/skills/hospitalizacion-domiciliaria/SKILL.md",
                "hermes/profiles/director-tecnico-hodom/distribution.yaml",
                "hermes/profiles/director-tecnico-hodom/SOUL.md",
                "skills/conducir-decisiones-hodom/",
                "skills/hospitalizacion-domiciliaria/",
            ),
        }

        for target, paths in expected.items():
            with self.subTest(target=target):
                result = subprocess.run(
                    [
                        sys.executable,
                        str(REPO / "kora.py"),
                        "transmutar",
                        "--urn", URN,
                        "--target", target,
                        "--stdout",
                    ],
                    cwd=REPO,
                    check=False,
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                for path in paths:
                    self.assertIn(path, result.stdout)


if __name__ == "__main__":
    unittest.main()
