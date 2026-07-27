# -*- coding: utf-8 -*-
"""Contrato de propagación del ciclo reversible opforja hacia KORA."""
import unittest
from pathlib import Path

import kora


RAIZ = Path(__file__).resolve().parent.parent
REGLAS = RAIZ / "artefactos/conocimiento/fxsl/reglas-opm-estrictas-es.md"
METODO = RAIZ / "artefactos/conocimiento/fxsl/metodologia-forja-opm-es.md"
SPEC_OPD = RAIZ / "artefactos/conocimiento/fxsl/spec-forja-opd-es.md"
SPEC_OPL = RAIZ / "artefactos/conocimiento/fxsl/spec-forja-opl-es.md"
SKILL = RAIZ / "artefactos/skills/kora/modelamiento-opm/SKILL.md"
BUNDLE = (
    RAIZ
    / "artefactos/skills/kora/modelamiento-opm/referencias/"
    / "bundle-deep-opm-pro.md"
)


def parsear(path: Path):
    return kora.parsear_archivo(path.read_text("utf-8"))


def seccion(cuerpo: str, inicio: str, fin: str) -> str:
    return cuerpo.split(inicio, 1)[1].split(fin, 1)[0]


def normalizar(cuerpo: str) -> str:
    return " ".join(cuerpo.split())


class TestCicloReversibleOpforja(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.reglas_campos, cls.reglas = parsear(REGLAS)
        cls.metodo_campos, cls.metodo = parsear(METODO)
        cls.spec_campos, cls.spec = parsear(SPEC_OPD)
        cls.opl_campos, _ = parsear(SPEC_OPL)
        cls.skill_campos, cls.skill = parsear(SKILL)
        cls.bundle = BUNDLE.read_text("utf-8")

    def test_versiones_vivas_del_corte(self):
        self.assertEqual(self.reglas_campos["version"], "1.5.0")
        self.assertEqual(self.metodo_campos["version"], "1.7.0")
        self.assertEqual(self.spec_campos["version"], "1.4.0")
        self.assertEqual(self.opl_campos["version"], "1.4.1")
        self.assertEqual(self.skill_campos["version"], "2.1.0")

    def test_metodo_separa_los_dos_ciclos_reversibles(self):
        a15 = normalizar(seccion(self.metodo, "**A1.5", "## A2."))
        for testigo in (
                "Apunte ⇄ Modelo",
                "Boceto ⇄ OPD integrado",
                "Graduar a Modelo",
                "Reabrir en Taller",
                "Integrar como",
                "Devolver a Bocetos",
                "independientes",
                "Graduar no integra"):
            self.assertIn(testigo, a15)

    def test_gate_de_bocetos_tiene_propietario_prescriptivo(self):
        reglas = normalizar(self.reglas)
        for regla in (
                "R-CAN-BOCETO-1",
                "R-CAN-BOCETO-2",
                "R-CAN-BOCETO-3",
                "R-CAN-BOCETO-4"):
            self.assertIn(regla, reglas)
        for testigo in (
                "régimen Modelo",
                "bloquear el export canónico",
                "régimen Apunte",
                "marca explícita",
                "NO DEBE bloquear la edición"):
            self.assertIn(testigo, reglas)

    def test_spec_visual_realiza_sin_relegislar_el_gate(self):
        ref20 = normalizar(
            seccion(self.spec, "**R-OPD-REF-20**", "Realización opforja:"))
        for testigo in (
                "Boceto",
                "Integrar como",
                "Devolver a Bocetos",
                "Eliminar refinamiento",
                "R-CAN-BOCETO",
                "banda «Bocetos»"):
            self.assertIn(testigo, ref20)
        self.assertNotIn("banda «Taller»", ref20)
        self.assertNotIn("raíz «Hoja»", ref20)

        self.assertIn("`adoptarOpd`", self.spec)
        self.assertIn('origen:"adopcion"', self.spec)

    def test_skill_habla_con_la_voz_actual_del_producto(self):
        skill = normalizar(self.skill)
        for espacio in ("Taller", "Modelos", "Bibliotecas", "Archivo"):
            self.assertIn(espacio, skill)
        for gesto in (
                "Graduar a Modelo",
                "Graduar con pendientes",
                "Reabrir en Taller",
                "Integrar como",
                "Devolver a Bocetos",
                "Eliminar refinamiento"):
            self.assertIn(gesto, skill)
        for obsoleto in (
                "banda **«Taller»**",
                "gesto **«+ OPD suelto»**",
                "gestor **«Modelos»** de dos zonas",
                "`CintaApunte → DialogoGraduar`"):
            self.assertNotIn(obsoleto, skill)

    def test_bundle_distingue_voz_visible_y_compatibilidad_interna(self):
        bundle = normalizar(self.bundle)
        for testigo in (
                "**Boceto**",
                "`padreId: null`",
                "Integrar",
                "`adoptarOpd`"):
            self.assertIn(testigo, bundle)


if __name__ == "__main__":
    unittest.main()
