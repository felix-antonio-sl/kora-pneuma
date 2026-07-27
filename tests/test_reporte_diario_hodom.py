# -*- coding: utf-8 -*-
"""Contrato de la skill KORA para el reporte diario HODOM."""
import subprocess
import sys
import unittest
from pathlib import Path

import kora


RAIZ = Path(__file__).resolve().parent.parent
SKILL = (
    RAIZ
    / "artefactos/skills/salud/reporte-diario-hodom/SKILL.md"
)
CONTRATO = SKILL.parent / "referencias/contrato-reporte-diario.md"


class TestReporteDiarioHodom(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.campos, cls.cuerpo = kora.parsear_archivo(
            SKILL.read_text("utf-8"))
        cls.contrato = CONTRATO.read_text("utf-8")

    def test_identidad_forma_y_target(self):
        self.assertEqual(
            self.campos["urn"],
            "urn:salud:artefacto:reporte-diario-hodom")
        self.assertEqual(self.campos["nombre"], "reporte-diario-hodom")
        self.assertEqual(self.campos["version"], "1.0.0")
        self.assertEqual(self.campos["estado"], "activo")
        self.assertEqual(self.campos["forma"], "habilidad")
        self.assertEqual(self.campos["arnes"], "disciplina")
        self.assertEqual(self.campos["targets"], ["codex"])
        self.assertEqual(self.campos["alcance"], "usuario")

    def test_define_dos_cortes_y_delta_honesto(self):
        combinado = self.cuerpo + self.contrato
        for testigo in (
                "CORTE-0800",
                "ACTUALIZACION-1100",
                "America/Santiago",
                "baseline-unavailable",
                "reporte completo"):
            self.assertIn(testigo, combinado)
        self.assertIn(
            "corte base 08:00 no disponible",
            " ".join(combinado.split()))

    def test_brief_cubre_estado_pendientes_y_alta(self):
        for testigo in (
                "En qué estamos",
                "Pendientes",
                "Qué falta para alta HODOM",
                "Acción inmediata",
                "Responsable humano"):
            self.assertIn(testigo, self.contrato)

    def test_conflictos_son_observaciones(self):
        combinado = self.cuerpo + self.contrato
        self.assertIn(
            "Toda discrepancia material se rotula `Observación`",
            self.cuerpo)
        self.assertIn("Observación:", combinado)
        self.assertIn("Impacto:", combinado)
        self.assertIn("Pendiente para resolver:", combinado)

    def test_busqueda_cubre_servicios_y_no_autoriza_ingreso(self):
        combinado = self.cuerpo + self.contrato
        for servicio in (
                "Unidad de Emergencia",
                "Medicina",
                "Traumatología",
                "Cirugía"):
            self.assertIn(servicio, combinado)
        self.assertIn(
            "preselección censal; no constituye aceptación HODOM",
            self.contrato)
        for gate in (
                "estabilidad clínica",
                "domicilio apto",
                "cuidador o red de apoyo",
                "consentimiento",
                "ruta de reingreso"):
            self.assertIn(gate, self.cuerpo)

    def test_privacidad_y_anti_tormenta(self):
        cuerpo = " ".join(self.cuerpo.split())
        for testigo in (
                "directorio de salida es externo a todo repositorio",
                "modo `0700`",
                "modo `0600`",
                "no persiste una sesión con PHI",
                "un probe adicional",
                "jamás fan-out",
                "no aumentar concurrencia"):
            self.assertIn(testigo, cuerpo)

    def test_reutiliza_metodos_existentes(self):
        self.assertEqual(
            self.campos["conocimiento"],
            ["urn:salud:kb:manual-agente-hsc-agent-cli"])
        self.assertEqual(
            self.campos["componible"],
            [
                "urn:salud:artefacto:hospitalizacion-domiciliaria",
                "urn:salud:artefacto:hospitalista",
                "urn:salud:artefacto:asistencial-hospital",
                "urn:salud:artefacto:asistencial-hodom",
                "urn:salud:artefacto:auditor-calidad-hospitalizacion",
            ])

    def test_contrato_declara_gates_de_cierre(self):
        for gate in (
                "G1-privacy",
                "G2-census",
                "G3-brief",
                "G4-conflict",
                "G5-services",
                "G6-candidates",
                "G7-delta",
                "G8-docx"):
            self.assertIn(gate, self.contrato)

    def test_fuente_y_pruebas_no_contienen_identificadores_clinicos(self):
        combinado = SKILL.read_text("utf-8") + self.contrato
        self.assertNotRegex(combinado, r"\b\d{7,8}-[\dkK]\b")
        self.assertNotRegex(
            combinado,
            r"reporte-diario-hodom-\d{4}-\d{2}-\d{2}\.docx")

    def test_transmutacion_codex_compila(self):
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


if __name__ == "__main__":
    unittest.main()
