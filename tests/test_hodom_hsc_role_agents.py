# -*- coding: utf-8 -*-
"""Contrato del panel participativo de roles HODOM-HSC para Codex."""
import re
import unittest
from pathlib import Path

import kora


RAIZ = Path(__file__).resolve().parent.parent
ZONA = RAIZ / "artefactos/agentes/salud"
MAPA_SHA256 = "64fd46129ecb3f5c88bb870b56225e3827861a6ed8e06c1ef9278556d5c3744d"
CATALOGO_SHA256 = "d4af558d2dc5bf57db07d21ea81d3435843132873c59bd830ae16bf2a61296c6"
GUARD_TEMPORAL = (
    "Presencia, ausencia, absorción de funciones, horarios y estado de "
    "V01–V13 pertenecen al corte fuente 2026-07-22. Antes de tratarlos "
    "como actuales, exige evidencia viva en la entrada; sin ella responde "
    "`non-demonstrated-practice`."
)

ROLES = {
    "hodom-hsc-direccion-tecnica": (
        "direccion-tecnica", ("capacidad", "cartera", "interfaces", "decisor universal")),
    "hodom-hsc-enfermera-coordinadora": (
        "enfermera-coordinadora", ("cola única", "compuertas", "acuse", "autoridad clínica")),
    "hodom-hsc-medico-atencion-directa": (
        "medico-atencion-directa", ("elegibilidad clínica", "plan", "rescate", "presión de camas")),
    "hodom-hsc-medico-regulador": (
        "medico-regulador", ("respuesta real", "handoff", "teléfono", "fallback")),
    "hodom-hsc-enfermero-clinico": (
        "enfermero-clinico", ("plan de cuidados", "dispositivos", "educación", "escalamiento")),
    "hodom-hsc-kinesiologo": (
        "kinesiologo", ("función respiratoria", "función motora", "respuesta", "continuidad")),
    "hodom-hsc-tecnico-enfermeria": (
        "tecnico-enfermeria", ("asignación", "supervisión", "competencia", "administrativa")),
    "hodom-hsc-trabajador-social": (
        "trabajador-social", ("domicilio", "cuidador", "redes", "dotación ausente")),
    "hodom-hsc-fonoaudiologo": (
        "fonoaudiologo", ("deglución", "comunicación", "educación", "handoff")),
    "hodom-hsc-otro-profesional": (
        "otro-profesional", ("cartera", "competencia", "mínimo privilegio", "disciplina")),
    "hodom-hsc-seremi": (
        "seremi", ("fiscalización", "diseño", "operación", "cadena clínica")),
    "hodom-hsc-administrador-seguridad": (
        "administrador-seguridad", ("identidad", "mínimo privilegio", "auditoría", "break-glass")),
    "hodom-hsc-conductor": (
        "conductor", ("ruta", "vehículo", "custodia", "decisiones clínicas")),
    "hodom-hsc-administrativo": (
        "administrativo", ("completitud", "agenda", "elegibilidad", "alta clínica")),
}

CONOCIMIENTO_COMUN = {
    "urn:salud:kb:hodom-reglamento-ds1-2022",
    "urn:salud:kb:hodom-norma-tecnica-2024",
    "urn:salud:kb:hsc-pro-002-hospitalizacion-domiciliaria",
    "urn:salud:kb:hodom-invariante-no-equivale-cerrada",
    "urn:salud:kb:hodom-direccion-tecnica",
    "urn:salud:kb:post-agudo-ltss-transiciones",
}


class TestPanelRolesHodomHsc(unittest.TestCase):

    def test_catalogo_cerrado_de_catorce_subagentes(self):
        self.assertEqual(len(ROLES), 14)
        for nombre in ROLES:
            self.assertTrue((ZONA / f"{nombre}.md").is_file(), nombre)
        presentes = {
            path.stem for path in ZONA.glob("hodom-hsc-*.md")
        }
        self.assertEqual(presentes, set(ROLES))
        self.assertNotIn("hodom-hsc-superusuario-dev", ROLES)

    def test_firma_y_despliegue_son_homogeneos(self):
        for nombre in ROLES:
            campos, _ = kora.parsear_archivo(
                (ZONA / f"{nombre}.md").read_text("utf-8"))
            with self.subTest(nombre=nombre):
                self.assertEqual(campos["urn"], f"urn:salud:artefacto:{nombre}")
                self.assertEqual(campos["nombre"], nombre)
                self.assertEqual(campos["version"], "1.0.0")
                self.assertEqual(campos["estado"], "activo")
                self.assertEqual(campos["forma"], "subagente")
                self.assertEqual(campos["arnes"], "persona")
                self.assertEqual(campos["vector"], [2, 1, 2, 1, 2])
                self.assertEqual(campos["sigma"], [3, 3, 3, 3, 2])
                self.assertEqual(campos["herramientas"], ["Read", "Grep", "Glob"])
                self.assertEqual(campos["targets"], ["codex"])
                self.assertEqual(campos["alcance"], "proyecto")
                self.assertTrue(CONOCIMIENTO_COMUN.issubset(campos["conocimiento"]))

    def test_procedencia_amarra_mapa_y_catalogo_ejecutable(self):
        for nombre, (role_type, _) in ROLES.items():
            campos, cuerpo = kora.parsear_archivo(
                (ZONA / f"{nombre}.md").read_text("utf-8"))
            with self.subTest(nombre=nombre):
                self.assertIn(MAPA_SHA256, campos["fuente"])
                self.assertIn(CATALOGO_SHA256, campos["fuente"])
                self.assertIn(f"`{role_type}`", cuerpo)
                self.assertNotIn("/home/felix", campos["fuente"])
                self.assertNotIn("/home/felix", cuerpo)

    def test_contrato_observable_y_limites_comunes(self):
        testigos = (
            "<!-- kora:soul -->",
            "<!-- kora:soul:fin -->",
            "## Contrato observable",
            "`ROLE_REVIEW`",
            "`missing-context`",
            "`outside-role`",
            "`authority-gap`",
            "`non-demonstrated-practice`",
            "`phi-detected`",
            "No eres la persona titular ni una autoridad institucional",
            "N/L/O/D/V",
            "V01–V13",
            "datos desidentificados",
            "no mutas el repositorio",
            "`human_decision_required`",
        )
        for nombre in ROLES:
            _, cuerpo = kora.parsear_archivo(
                (ZONA / f"{nombre}.md").read_text("utf-8"))
            cuerpo = " ".join(cuerpo.split())
            with self.subTest(nombre=nombre):
                for testigo in testigos:
                    self.assertIn(testigo, cuerpo)

    def test_cada_persona_porta_el_conflicto_observable_de_su_oficio(self):
        voces = set()
        for nombre, (_, marcadores) in ROLES.items():
            _, cuerpo = kora.parsear_archivo(
                (ZONA / f"{nombre}.md").read_text("utf-8"))
            voz = cuerpo.split("<!-- kora:soul -->", 1)[1].split(
                "<!-- kora:soul:fin -->", 1)[0]
            voces.add(" ".join(voz.split()))
            cuerpo = cuerpo.lower()
            with self.subTest(nombre=nombre):
                for marcador in marcadores:
                    self.assertIn(marcador.lower(), cuerpo)
        self.assertEqual(len(voces), len(ROLES))

    def test_el_corte_temporal_no_se_presenta_como_estado_vivo(self):
        for nombre in ROLES:
            _, cuerpo = kora.parsear_archivo(
                (ZONA / f"{nombre}.md").read_text("utf-8"))
            cuerpo_normalizado = " ".join(cuerpo.split())
            with self.subTest(nombre=nombre):
                self.assertIn(GUARD_TEMPORAL, cuerpo_normalizado)
                self.assertIsNone(
                    re.search(r"\b(?:hoy|actualmente)\b", cuerpo.lower()))


if __name__ == "__main__":
    unittest.main()
