# -*- coding: utf-8 -*-
"""Contrato vigente del subagente KORA agent-architect."""
import unittest
from pathlib import Path

import kora


RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "artefactos/agentes/dev/agent-architect.md"
CONTRATO = "urn:kora:kb:cat-contrato-ingenieria-agentica"


class TestAgentArchitectContrato(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.campos, cls.cuerpo = kora.parsear_archivo(
            FUENTE.read_text("utf-8"))

    def test_es_subagente_persona_codex_only(self):
        self.assertEqual(
            self.campos["urn"], "urn:dev:artefacto:agent-architect")
        self.assertEqual(self.campos["version"], "2.7.0")
        self.assertEqual(self.campos["estado"], "activo")
        self.assertEqual(self.campos["forma"], "subagente")
        self.assertEqual(self.campos["arnes"], "persona")
        self.assertEqual(self.campos["targets"], ["codex"])

    def test_conoce_el_contrato_agentico_vigente(self):
        self.assertIn(CONTRATO, self.campos["conocimiento"])
        for nivel in ("Spec(a)", "Model(a)", "Runtime_T(a,r)"):
            self.assertIn(nivel, self.cuerpo)
        self.assertIn("I`, `O`", self.cuerpo)
        self.assertIn("`U`, `M`, `step`", self.cuerpo)

    def test_clasifica_las_cuatro_formas(self):
        for forma in (
                "`forma=habilidad`", "`forma=subagente`",
                "`forma=agente`", "`forma=plataforma`"):
            self.assertIn(forma, self.cuerpo)

    def test_clasifica_por_invocacion_y_valida_dominio_de_materia(self):
        cuerpo_normalizado = " ".join(self.cuerpo.split())
        self.assertIn("modo de invocacion", cuerpo_normalizado)
        for forma, dominio in (
                ("habilidad", "{0,1}"), ("subagente", "{0,1,2}"),
                ("agente", "{2,3}"), ("plataforma", "{3}")):
            self.assertIn(
                f"`forma={forma}` admite `mu` ∈ {dominio}",
                cuerpo_normalizado)

    def test_codex_only_limita_despliegue_no_dominio_de_autoria(self):
        cuerpo_normalizado = " ".join(self.cuerpo.split())
        self.assertIn("desplegado solo en Codex", self.campos["descripcion"])
        self.assertIn(
            "cada target declarado por el artefacto en autoria",
            cuerpo_normalizado)
        self.assertNotIn("mapa de transmutacion a Codex", self.cuerpo)

    def test_declara_su_propio_contrato_observable(self):
        for testigo in (
                "## Contrato observable propio", "`I_self`", "`O_self`",
                "`ambiguous-intent`", "`unresolved-reference`",
                "`invalid-source`"):
            self.assertIn(testigo, self.cuerpo)

    def test_uso_de_persona_es_procedural_no_composicion_semantica(self):
        cuerpo_normalizado = " ".join(self.cuerpo.split())
        self.assertNotIn("Compongo y ejerzo", self.cuerpo)
        self.assertNotIn("El agente compone cajas", self.cuerpo)
        for testigo in (
                "candidato declarado por `componible`", "`I_persona`",
                "`O_persona`", "si la URN no resuelve"):
            self.assertIn(testigo, cuerpo_normalizado)

    def test_anclas_semanticas_corresponden_al_corpus_vigente(self):
        cuerpo_normalizado = " ".join(self.cuerpo.split())
        for ancla_obsoleta in (
                "`cat-agent-coalgebra` §2.3", "`cat-agent-modulo` §3",
                "cat-agent-modulo`, eje de encapsulacion",
                "`cat-agent-modulo` §5 (eje de encapsulacion"):
            self.assertNotIn(ancla_obsoleta, self.cuerpo)
        self.assertIn(
            "La ausencia de `U_phen` en habilidades se deriva de "
            "`ley/2 §§8 y 10`", cuerpo_normalizado)
        self.assertIn(
            "doctrina procedural propia de `autoria-de-persona`",
            cuerpo_normalizado)

    def test_herramientas_declaran_pero_no_prueban_enforcement(self):
        cuerpo_normalizado = " ".join(self.cuerpo.split())
        self.assertNotIn(
            "Las herramientas son enforcement de scope", self.cuerpo)
        self.assertIn(
            "la autoridad efectiva se verifica por target y runtime",
            cuerpo_normalizado)
        self.assertIn("no prueba least-privilege", self.cuerpo)

    def test_procedencia_no_reintroduce_vector_como_tipo(self):
        self.assertNotIn("vector da tipo", self.campos["fuente"])
        self.assertNotIn("vector = tipo", self.campos["fuente"])


if __name__ == "__main__":
    unittest.main()
