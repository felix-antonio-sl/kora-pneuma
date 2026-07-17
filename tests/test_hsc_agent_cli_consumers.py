# -*- coding: utf-8 -*-
"""Evals estructurales del contrato CLI en consumidores KORA (sin PHI)."""
import unittest
from pathlib import Path

import kora


RAIZ = Path(__file__).resolve().parent.parent
CONSUMIDORES_DIRECTOS = {
    "medico-hospitalista": RAIZ / "artefactos/agentes/salud/medico-hospitalista.md",
    "urgenciologo": RAIZ / "artefactos/agentes/salud/urgenciologo.md",
}
MANUAL_PATH = RAIZ / "artefactos/conocimiento/salud/manual-agente-hsc-agent-cli.md"
MANUAL_URN = "urn:salud:kb:manual-agente-hsc-agent-cli"


class TestContratoHscAgentCli(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.consumidores = {}
        for nombre, path in CONSUMIDORES_DIRECTOS.items():
            campos, cuerpo = kora.parsear_archivo(path.read_text(encoding="utf-8"))
            cls.consumidores[nombre] = (campos, cuerpo)
        cls.manual = kora.parsear_archivo(MANUAL_PATH.read_text(encoding="utf-8"))

    def assert_cuerpo_contiene(self, *fragmentos):
        for nombre, (_, cuerpo) in self.consumidores.items():
            with self.subTest(consumidor=nombre):
                cuerpo_normalizado = " ".join(cuerpo.split())
                for fragmento in fragmentos:
                    self.assertIn(" ".join(fragmento.split()), cuerpo_normalizado)

    def test_capacidad_y_manual_excepcional(self):
        for nombre, (campos, _) in self.consumidores.items():
            with self.subTest(consumidor=nombre):
                self.assertIn("Bash", campos["herramientas"])
                self.assertIn(MANUAL_URN, campos["conocimiento"])
                self.assertIn(
                    "data.agent_guide` versión `agent-autonomy-3",
                    " ".join(self.consumidores[nombre][1].split()),
                )
        self.assert_cuerpo_contiene(
            "command_playbook",
            "no es requisito del flujo estándar",
        )

    def test_eval_1_entrada_solo_con_nombre(self):
        self.assert_cuerpo_contiene(
            "hsc-agent-cli health",
            "best_current_context",
            "homónimo",
        )

    def test_eval_2_censo_hodom_sin_alias_singular(self):
        self.assert_cuerpo_contiene(
            "batch_plan.requests[].command_args",
            "no existen aliases `recommended_*`",
            "orden secuencial declarado",
        )

    def test_eval_3_upstream_unavailable_sin_fan_out(self):
        self.assert_cuerpo_contiene(
            "affected_systems",
            "outage_kind",
            "un solo `health`",
            "fan-out",
        )

    def test_eval_4_identity_mismatch_detiene_item(self):
        self.assert_cuerpo_contiene(
            "identity_mismatch",
            "descarta",
        )

    def test_eval_5_bundle_no_decide_clinica(self):
        self.assert_cuerpo_contiene(
            "summary.source_issues",
            "summary.bundle_integrity",
            "compaction",
            "does_not_assess_clinical_safety=true",
        )

    def test_eval_6_autonomia_desde_ayuda_inline(self):
        self.assert_cuerpo_contiene(
            "hsc-agent-cli <comando> --help",
            "batch_plan.requests[].command_args",
            "command_playbook.next",
            "error_detail.alternative_handles",
            "state` y `error_code",
        )

    def test_beta3_no_reintroduce_campos_retirados(self):
        for nombre, (_, cuerpo) in self.consumidores.items():
            cuerpo_normalizado = " ".join(cuerpo.split())
            for campo in (
                "decision_safety",
                "clinical_gaps",
                "usable_clinically",
                "recommended_batch_handle",
            ):
                with self.subTest(consumidor=nombre, campo=campo):
                    self.assertNotIn(campo, cuerpo_normalizado)

    def test_hospitalista_no_promete_no_persistencia(self):
        _, cuerpo = self.consumidores["medico-hospitalista"]
        cuerpo_normalizado = " ".join(cuerpo.split())
        self.assertNotIn(
            "No se almacenan datos de pacientes entre casos",
            cuerpo_normalizado,
        )
        self.assertIn(
            "no reutiliza evidencia clínica entre pacientes",
            cuerpo_normalizado,
        )
        self.assertIn(
            "persistencia automática del runtime",
            cuerpo_normalizado,
        )

    def test_urgenciologo_hace_ejecutable_procedencia_y_autoridad(self):
        campos, cuerpo = self.consumidores["urgenciologo"]
        cuerpo_normalizado = " ".join(cuerpo.split())
        self.assertEqual("3.10.0", campos["version"])
        for fragmento in (
            "`corpus-ref <URN#sección>`",
            "`fuera-de-corpus`",
            "Opción para validación humana",
            "Monitorización / criterio de fracaso",
            "Disposición / responsable",
            "nunca como instrucción imperativa",
        ):
            with self.subTest(fragmento=fragmento):
                self.assertIn(fragmento, cuerpo_normalizado)

    def test_urgenciologo_prioriza_fuentes_hsc_y_salida_pegable(self):
        _, cuerpo = self.consumidores["urgenciologo"]
        cuerpo_normalizado = " ".join(cuerpo.split())
        for fragmento in (
            "médico M1",
            "`hsc-agent-cli` es la fuente primaria de hechos del paciente",
            "DAU, LAB y SGH",
            "HCC",
            "La memoria no es fuente factual del paciente",
            "texto pegable",
            "No explica el razonamiento salvo solicitud explícita",
            "`ALERTA:",
            "`BRECHA:`",
            "dato ausente = `pendiente`",
        ):
            with self.subTest(fragmento=fragmento):
                self.assertIn(fragmento, cuerpo_normalizado)

    def test_urgenciologo_define_rutas_dau_ic_hospitalizacion_y_alta(self):
        _, cuerpo = self.consumidores["urgenciologo"]
        cuerpo_normalizado = " ".join(cuerpo.split())
        for fragmento in (
            "`DAU alta + RUT/DAU`",
            "`IC medicina + RUT/DAU`",
            "`DAU hosp + RUT/DAU`",
            "Se solicita IC [especialidad] por [problema concreto]",
            "Se hospitaliza en [servicio] por [problema activo/riesgo]",
            "Se deja pcte [estable/inestable]",
            "INDICACIONES:",
            "Alta domicilio.",
            "Reconsultar SU ante",
        ):
            with self.subTest(fragmento=fragmento):
                self.assertIn(fragmento, cuerpo_normalizado)
        for rotulo in (
            "ANAMNESIS:",
            "EXAMEN FÍSICO:",
            "HIPÓTESIS:",
            "OBSERVACIONES:",
            "DIAGNÓSTICOS:",
            "INDICACIONES DE ALTA:",
        ):
            with self.subTest(rotulo=rotulo):
                self.assertIn(rotulo, cuerpo)

    def test_consumidores_adoptan_guardas_agent_autonomy_3(self):
        self.assert_cuerpo_contiene(
            "ayuda global raíz",
            "`fields_coverage[].empty_count`",
            "`service_id`, `service_name`, `room_id` y `room_name`",
            "`hospitalization_observed=true`",
            "`hospitalization_handle_ready=false`",
            "el RUT no resuelve ese episodio sin `ingreso_id`",
            "`count>=2`",
            "salida `multi_bundle`",
            "sin cola singleton",
            "cada bundle desde `envelope` por orden de completitud",
            "summary terminal `kind:multi_bundle`",
            "fixtures/evals sintéticos",
        )

    def test_manual_v310_preserva_contrato_completo(self):
        campos, cuerpo = self.manual
        cuerpo_normalizado = " ".join(cuerpo.split())
        self.assertEqual("1.0.16", campos["version"])
        for fragmento in (
            "base publicada `v3.1.0`",
            "`agent-autonomy-3`",
            "ayuda global raíz en texto",
            "`present_count` (la clave existe, incluso si su string está vacío)",
            "`missing_count` (la clave no existe)",
            "`empty_count` (la clave existe y su valor string queda vacío",
            "`service_id`, `service_name`, `room_id` y `room_name`",
            "`hospitalization_observed` y `hospitalization_handle_ready`",
            "esa ruta **no resuelve el episodio SGH**",
            "`batch_plan.requests[].count >= 2`",
            "`[3,3,1] → [3,2,2]`",
            '"kind":"multi_bundle"',
            "fixtures/evals sintéticos",
        ):
            with self.subTest(fragmento=fragmento):
                self.assertIn(" ".join(fragmento.split()), cuerpo_normalizado)

    def test_hospitalista_hace_ejecutable_el_plan_soap(self):
        campos, cuerpo = self.consumidores["medico-hospitalista"]
        cuerpo_normalizado = " ".join(cuerpo.split())
        self.assertEqual("1.7.0", campos["version"])
        for fragmento in (
            "Intervención — indicación — contraindicación relevante — monitor — duración/stop",
            "Disposición — criterios cumplidos — criterios pendientes — responsable — plazo",
            "`corpus-ref <URN#sección>`",
            "`evidencia externa <fuente; nivel/calidad; fecha>`",
            "`inferencia`",
            "`no verificado`",
        ):
            with self.subTest(fragmento=fragmento):
                self.assertIn(fragmento, cuerpo_normalizado)


if __name__ == "__main__":
    unittest.main()
