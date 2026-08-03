# -*- coding: utf-8 -*-
"""Contrato canónico del ejecutor delegado Fugaz y su enlace con Steipete."""
import unittest
from pathlib import Path

import kora


RAIZ = Path(__file__).resolve().parent.parent
FUGAZ = RAIZ / "artefactos/agentes/dev/fugaz.md"
STEIPETE = RAIZ / "artefactos/agentes/dev/steipete.md"
SHIP_DISCIPLINE = "urn:dev:artefacto:ship-discipline"
DIAGNOSING_BUGS = "urn:dev:artefacto:diagnosing-bugs"
CODE_REVIEW = "urn:dev:artefacto:code-review"
FUGAZ_URN = "urn:dev:artefacto:fugaz"


class TestFugazContrato(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fugaz_campos, cls.fugaz_cuerpo = kora.parsear_archivo(
            FUGAZ.read_text("utf-8"))
        cls.steipete_campos, cls.steipete_cuerpo = kora.parsear_archivo(
            STEIPETE.read_text("utf-8"))
        cls.fugaz_normalizado = " ".join(cls.fugaz_cuerpo.split())
        cls.steipete_normalizado = " ".join(cls.steipete_cuerpo.split())

    def test_es_subagente_delegado_efimero_codex_only(self):
        self.assertEqual(self.fugaz_campos["urn"], FUGAZ_URN)
        self.assertEqual(self.fugaz_campos["version"], "2.1.0")
        self.assertEqual(self.fugaz_campos["estado"], "activo")
        self.assertEqual(self.fugaz_campos["forma"], "subagente")
        self.assertEqual(self.fugaz_campos["arnes"], "delegado")
        self.assertEqual(self.fugaz_campos["vector"], [3, 1, 2, 0, 1])
        self.assertEqual(self.fugaz_campos["sigma"], [2, 1, 3, 2, 1])
        self.assertEqual(self.fugaz_campos["targets"], ["codex"])
        self.assertEqual(self.fugaz_campos["alcance"], "usuario")
        self.assertNotIn("kora:soul", self.fugaz_cuerpo)

    def test_migracion_bestia_es_reescritura_trazable(self):
        procedencia = self.fugaz_campos["fuente"]
        self.assertIn("Migracion migrar-o-omitir", procedencia)
        self.assertIn("~/kora/artifacts/agents/dev/fugaz/AGENT.md", procedencia)
        self.assertIn(
            "sha256:1cf7424d1310d6ed189e6fe81f583aecf818dd4318aaea98a"
            "e5b3c93e94b560b",
            procedencia,
        )
        self.assertIn("forma=subagente", procedencia)
        self.assertIn("arnes=delegado", procedencia)

    def test_declara_paquete_de_tarea_tipado(self):
        self.assertIn("`I_task`", self.fugaz_cuerpo)
        for campo in (
                "`objective`", "`workspace`", "`candidate`", "`owned_scope`",
                "`acceptance`", "`authority`", "`forbidden_scope`",
                "`constraints`", "`context`"):
            self.assertIn(campo, self.fugaz_cuerpo)
        self.assertIn("`malformed-packet`", self.fugaz_cuerpo)
        self.assertIn("`candidate-mismatch`", self.fugaz_cuerpo)
        self.assertIn(
            "si no coincide, devuelvo `candidate-mismatch` sin editar",
            self.fugaz_normalizado,
        )
        self.assertIn(
            "intersección entre el paquete, la autorización del principal "
            "y la autoridad efectiva del runtime",
            self.fugaz_normalizado,
        )

    def test_devuelve_recibo_tipado_y_epistemicamente_honesto(self):
        self.assertIn("`O_task`", self.fugaz_cuerpo)
        for campo in (
                "`status`", "`candidate`", "`changes`", "`evidence`", "`limits`",
                "`blocker`", "`assumptions`"):
            self.assertIn(campo, self.fugaz_cuerpo)
        for estado in ("`COMPLETE`", "`PARTIAL`", "`BLOCKED`"):
            self.assertIn(estado, self.fugaz_cuerpo)
        for evidencia in ("`PASS`", "`FAIL`", "`ABSENT`", "`NOT_RUN`"):
            self.assertIn(evidencia, self.fugaz_cuerpo)
        self.assertIn(
            "`environment-blocked` cierran `BLOCKED`",
            self.fugaz_normalizado,
        )

    def test_compone_disciplina_sin_fingir_wiring_formal(self):
        self.assertEqual(
            self.fugaz_campos["componible"],
            [SHIP_DISCIPLINE, DIAGNOSING_BUGS],
        )
        for testigo in (
                "uso procedural", "candidato declarado por `componible`",
                "no prueba composición semántica"):
            self.assertIn(testigo, self.fugaz_normalizado)

    def test_fugaz_diagnostica_bugs_en_la_misma_sesion(self):
        for testigo in (
                DIAGNOSING_BUGS, "bucle red-capaz", "hipótesis falsables",
                "una variable por vez", "regresión en el seam correcto",
                "misma sesión Fugaz", "no crea otro agente",
                "no habilita delegación descendiente",
                "`BLOCKED/environment-blocked`", "`NOT_RUN`",
                "instrumentación temporal retirada"):
            self.assertIn(testigo, self.fugaz_normalizado)

    def test_envelope_impide_scope_creep_y_delegacion_recursiva(self):
        for testigo in (
                "`scope-expansion`", "`architecture-decision-required`",
                "`authority-required`", "`concurrent-conflict`",
                "No delega en otros agentes", "preservo cambios ajenos",
                "No devuelve `COMPLETE` sin evidencia"):
            self.assertIn(testigo, self.fugaz_cuerpo)

    def test_modelo_y_autoridad_pertenecen_al_runtime(self):
        self.assertIn(
            "La selección de modelo y esfuerzo pertenece al runtime",
            self.fugaz_normalizado,
        )
        self.assertIn(
            "no prueba la autoridad efectiva",
            self.fugaz_normalizado,
        )
        self.assertNotIn("gpt-", self.fugaz_cuerpo.lower())
        self.assertIn(
            "El contrato no fija, recomienda ni exige modelos",
            self.steipete_normalizado,
        )
        self.assertNotIn("gpt-", self.steipete_cuerpo.lower())

    def test_steipete_es_integrador_y_delega_por_adaptador(self):
        self.assertEqual(self.steipete_campos["version"], "1.3.0")
        self.assertIn(FUGAZ_URN, self.steipete_campos["componible"])
        for testigo in (
                "I_fugaz", "O_fugaz", "integrador responsable",
                "No delego una intención borrosa", "alcances de escritura",
                "no sustituye mi verificación de integración",
                "no amplía autoridad", "Sólo en Codex",
                "En los demás targets", "`agent_type=fugaz`",
                '`fork_turns="none"`', "rechaza la invocación",
                "`agent thread` nuevo",
                "central única de dirección e integración",
                "no se coordinan lateralmente",
                "topología central de un nivel",
                "no me reclasifica como arnés orquestador"):
            self.assertIn(testigo, self.steipete_normalizado)

    def test_steipete_orquesta_revision_bifocal_sin_mezclar_ejes(self):
        self.assertIn(CODE_REVIEW, self.steipete_campos["componible"])
        for testigo in (
                CODE_REVIEW, "Sólo en Codex, para revisar un cambio",
                "fuente única del protocolo bifocal", "no los duplico aquí",
                "dos sesiones Fugaz", "dos `O_task` separados", "read-only",
                "filesystem vivo", "En los demás targets no prometo este adaptador",
                "no amplío autoridad", "no prueba ejecución"):
            self.assertIn(testigo, self.steipete_normalizado)
        for duplicado in (
                "git diff <fixed-point>...HEAD", "paquete `Standards`",
                "paquete `Spec`", "sin ganador global"):
            self.assertNotIn(duplicado, self.steipete_cuerpo)


if __name__ == "__main__":
    unittest.main()
