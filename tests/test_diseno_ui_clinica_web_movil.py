# -*- coding: utf-8 -*-
"""Contrato de la skill KORA para UI clínica web y smartphone."""
import subprocess
import sys
import unittest
from pathlib import Path

import kora


RAIZ = Path(__file__).resolve().parent.parent
SKILL = (
    RAIZ
    / "artefactos/skills/salud/diseno-ui-clinica-web-movil/SKILL.md"
)
MARCO = (
    SKILL.parent
    / "referencias/marco-ui-clinica-web-movil.md"
)
FRAME_GUIA = (
    SKILL.parent
    / "referencias/frame-guia-especificacion-grafica.md"
)


class TestDisenoUiClinicaWebMovil(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.campos, cls.cuerpo = kora.parsear_archivo(
            SKILL.read_text("utf-8"))
        cls.marco = MARCO.read_text("utf-8")
        cls.frame_guia = FRAME_GUIA.read_text("utf-8")

    def test_identidad_y_forma(self):
        self.assertEqual(
            self.campos["urn"],
            "urn:salud:artefacto:diseno-ui-clinica-web-movil")
        self.assertEqual(self.campos["nombre"], "diseno-ui-clinica-web-movil")
        self.assertEqual(self.campos["version"], "1.0.0")
        self.assertEqual(self.campos["estado"], "activo")
        self.assertEqual(self.campos["forma"], "habilidad")
        self.assertEqual(self.campos["arnes"], "disciplina")
        self.assertEqual(self.campos["targets"], ["codex"])
        self.assertEqual(self.campos["alcance"], "usuario")
        self.assertEqual(self.campos["sigma"], [3, 2, 3, 3, 2])

    def test_es_puerta_unica_con_seis_modos(self):
        cuerpo = " ".join(self.cuerpo.split())
        for modo in (
                "`FRAME`", "`MODEL`", "`DESIGN`",
                "`BUILD`", "`EVALUATE`", "`FULL`"):
            self.assertIn(modo, cuerpo)
        for salida in (
                "`UI_FRAME_PACKET`", "`UI_MODEL_PACKET`",
                "`UI_DESIGN_PACKET`",
                "`UI_IMPLEMENTATION_PACKET`", "`UI_EVALUATION_PACKET`",
                "`UI_FULL_PACKET`", "`UI_DESIGN_ERROR`"):
            self.assertIn(salida, cuerpo)
        self.assertIn("Ejecutar exactamente uno", cuerpo)
        self.assertIn("el operador invoca sólo esta skill", cuerpo)

    def test_reutiliza_capacidades_sin_fingir_wiring(self):
        self.assertEqual(
            self.campos["conocimiento"],
            ["urn:dev:kb:canon-diseno-producto-integrado"])
        self.assertEqual(
            self.campos["componible"],
            [
                "urn:dev:artefacto:diseno-producto-integrado",
                "urn:dev:artefacto:design",
                "urn:kora:artefacto:ux-design",
                "urn:fxsl:artefacto:ifml",
                "urn:dev:artefacto:ship-discipline",
            ])
        normalizado = " ".join(self.cuerpo.split())
        for testigo in (
                "I_product", "O_product",
                "I_design", "O_design",
                "I_ifml", "O_ifml",
                "I_ship", "O_ship",
                "I_ux", "O_ux",
                "no prueba invocación"):
            self.assertIn(testigo, normalizado)

    def test_marco_porta_lentes_y_frontera_de_autoridad(self):
        for testigo in (
                "Karri Saarinen / Linear", "Vercel Design Team",
                "Continuidad clínica visible", "Ledger clínico",
                "Hilo de evidencia", "Escena de decisión",
                "Smartphone: superficie de foco",
                "Este marco no fue escrito ni aprobado"):
            self.assertIn(testigo, self.marco)
        for url in (
                "https://linear.app/now/output-isn-t-design",
                "https://linear.app/now/invisible-details",
                "https://vercel.com/design/engineer",
                "https://vercel.com/design/guidelines"):
            self.assertIn(url, self.marco)

    def test_frame_guia_especifica_la_salida_grafica(self):
        for testigo in (
                "GRAPHIC_SPEC_FRAME", "## 01. Frame", "## 02. Tesis gráfica",
                "## 04. Composición web", "## 05. Composición smartphone",
                "## 06. Sistema visual", "## 07. Componentes",
                "## 08. Estados y microinteracción",
                "## 11. Evaluación", "## 12. Decisión y continuidad"):
            self.assertIn(testigo, self.frame_guia)
        self.assertIn(
            "frame-guia-especificacion-grafica.md",
            self.cuerpo)

    def test_conserva_fronteras_spec_model_runtime(self):
        cuerpo = " ".join(self.cuerpo.split()).lower()
        for testigo in (
                "`evidence_ledger`", "`verificado`", "`propuesto`",
                "`inferido`", "`pendiente`", "`spec_only`",
                "no se verifica a sí misma",
                "build verde prueba build; no prueba experiencia",
                "validación clínica sólo proviene de autoridad competente"):
            self.assertIn(testigo, cuerpo)
        self.assertIn("domain_authority_packet", cuerpo)

    def test_exige_web_smartphone_y_estados_reales(self):
        combinado = " ".join((self.cuerpo + self.marco).split()).lower()
        for testigo in (
                "el smartphone recibe una escena propia",
                "recepción incierta", "conflicto", "obsoleto", "offline",
                "teclado", "foco", "tacto", "zoom", "reflow",
                "rendimiento", "responsive"):
            self.assertIn(testigo, combinado)

    def test_emision_codex_es_materializable(self):
        resultado = subprocess.run(
            [
                sys.executable,
                str(RAIZ / "kora.py"),
                "transmutar",
                "--urn", self.campos["urn"],
                "--target", "codex",
                "--stdout",
            ],
            cwd=RAIZ,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertIn("target: codex", resultado.stdout)
        self.assertIn(
            "referencias/marco-ui-clinica-web-movil.md",
            resultado.stdout)
        self.assertIn(
            "referencias/frame-guia-especificacion-grafica.md",
            resultado.stdout)


if __name__ == "__main__":
    unittest.main()
