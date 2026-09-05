# -*- coding: utf-8 -*-
"""Contrato de la skill que conduce decisiones HODOM adoptables."""
import subprocess
import sys
import unittest
from pathlib import Path

import kora


REPO = Path(__file__).resolve().parent.parent
SKILL = (
    REPO / "artefactos/skills/salud/conducir-decisiones-hodom/SKILL.md"
)
ANTERIOR = REPO / "artefactos/skills/kora/decision-operable/SKILL.md"
URN = "urn:salud:artefacto:conducir-decisiones-hodom"
SOURCE_SHA256 = (
    "2b8c69ddbc8ec755c030330e2c7ad302339fe58301af5546b2861d89e4a390d7"
)


class TestConducirDecisionesHodom(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.campos, cls.cuerpo = kora.parsear_archivo(
            SKILL.read_text("utf-8"))
        cls.campos_anteriores, _ = kora.parsear_archivo(
            ANTERIOR.read_text("utf-8"))

    def test_es_la_skill_salud_activa_sustentada_por_el_snapshot(self):
        self.assertEqual(self.campos["urn"], URN)
        self.assertEqual(
            self.campos["nombre"], "conducir-decisiones-hodom")
        self.assertEqual(self.campos["version"], "1.0.0")
        self.assertEqual(self.campos["estado"], "activo")
        self.assertEqual(self.campos["forma"], "habilidad")
        self.assertEqual(self.campos["arnes"], "disciplina")
        self.assertEqual(self.campos["targets"], ["codex", "hermes"])
        self.assertEqual(self.campos["alcance"], "usuario")
        self.assertIn(SOURCE_SHA256, self.campos["fuente"])

    def test_reemplaza_el_artefacto_generico_accidental(self):
        self.assertEqual(
            self.campos["reemplaza"],
            ["urn:kora:artefacto:decision-operable"])
        self.assertEqual(self.campos_anteriores["estado"], "deprecado")

    def test_declara_la_composicion_hodom_sin_fingir_wiring(self):
        self.assertEqual(
            self.campos["componible"],
            [
                "urn:salud:artefacto:salubrista",
                "urn:salud:artefacto:hospitalizacion-domiciliaria",
            ],
        )
        normalizado = " ".join(self.cuerpo.split()).lower()
        self.assertIn("candidatos declarados", normalizado)
        self.assertIn("no prueba wiring", normalizado)

    def test_separa_planos_de_autoridad_hodom(self):
        cuerpo = " ".join(self.cuerpo.split()).lower()
        for plano in (
                "especificación", "desarrollo", "preproducción",
                "práctica clínica", "autorización institucional",
                "operación productiva"):
            self.assertIn(plano, cuerpo)
        for clase in (
                "hecho observado", "declaración del director técnico",
                "propuesta", "decisión ratificada", "implementación",
                "validación"):
            self.assertIn(clase, cuerpo)

    def test_conserva_objeto_cadena_material_tiempo_y_recuperacion(self):
        cuerpo = " ".join(self.cuerpo.split()).lower()
        for testigo in (
                "quién hace qué", "sobre qué", "para quién",
                "en qué momento", "con qué consecuencia", "función",
                "acto", "objeto", "autorización", "resultado",
                "receptor capaz", "acuse", "obligación sucesora",
                "recuperación ante falla", "cuándo comienza",
                "qué la mantiene activa", "qué resultado la transfiere",
                "qué condición permite cerrarla"):
            self.assertIn(testigo, cuerpo)

    def test_preserva_fracturas_ontologicas_hodom(self):
        cuerpo = self.cuerpo.lower()
        for contraste in (
                "caso ≠ episodio hodom",
                "atención domiciliaria ≠ hospitalización domiciliaria",
                "visita ≠ prestación realizada",
                "gps ≠ atención",
                "registro local ≠ ficha clínica institucional",
                "egreso ≠ cierre longitudinal",
                "envío a aps ≠ transferencia de responsabilidad",
                "dato provisional rem ≠ cierre mensual oficial",
                "indicador agregado ≠ juicio clínico individual"):
            self.assertIn(contraste, cuerpo)

    def test_salida_es_predecision_adoptable_no_formulario(self):
        cuerpo = " ".join(self.cuerpo.split()).lower()
        for parte in (
                "pregunta clara", "contexto necesario", "recomendación",
                "pre-respuesta", "estado propuesto", "evidencia decisiva",
                "límite"):
            self.assertIn(parte, cuerpo)
        self.assertIn("predecidir sin usurpar autoridad", cuerpo)
        self.assertIn("respondida", cuerpo)
        self.assertIn("abierta", cuerpo)
        self.assertIn("bloqueada", cuerpo)
        self.assertIn("diferible", cuerpo)
        self.assertIn("necesita evidencia", cuerpo)

    def test_antiburocracia_usa_realidad_y_no_devuelve_trabajo(self):
        cuerpo = " ".join(self.cuerpo.split()).lower()
        for regla in (
                "no pedir nuevamente un hecho ya declarado",
                "no crear un rol nuevo", "no tratar disponibilidad nominal",
                "no construir módulos sobre problemas hipotéticos",
                "no introducir preguntas sobre el cuestionario",
                "no pedirle al operador una decisión de implementación"):
            self.assertIn(regla, cuerpo)
        self.assertIn("falla principal", cuerpo)

    def test_delimita_uso_y_no_hace_clinica_individual(self):
        cuerpo = " ".join(self.cuerpo.split()).lower()
        self.assertIn("cuestionarios", cuerpo)
        self.assertIn("protocolos", cuerpo)
        self.assertIn("preproducción hodom", cuerpo)
        self.assertIn("no usar para diagnóstico", cuerpo)
        self.assertIn("paciente individual", cuerpo)

    def test_transmuta_como_skill_nativa_en_codex_y_hermes(self):
        for target in ("codex", "hermes"):
            with self.subTest(target=target):
                resultado = subprocess.run(
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
                self.assertEqual(
                    resultado.returncode, 0, resultado.stderr)
                self.assertIn(
                    "name: conducir-decisiones-hodom", resultado.stdout)
                self.assertIn(f"target: {target}", resultado.stdout)


if __name__ == "__main__":
    unittest.main()
