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
MANUAL_URN = "urn:salud:kb:manual-agente-hsc-agent-cli"


class TestContratoHscAgentCli(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.consumidores = {}
        for nombre, path in CONSUMIDORES_DIRECTOS.items():
            campos, cuerpo = kora.parsear_archivo(path.read_text(encoding="utf-8"))
            cls.consumidores[nombre] = (campos, cuerpo)

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
        self.assert_cuerpo_contiene(
            "data.agent_guide.command_playbook",
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
            "recommended_batch_handles[].command_args",
            "recommended_batch_handle` singular",
            "en serie",
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
            "clinical_gaps",
            "compaction",
            "decision_safety",
            "seguridad clínica",
        )

    def test_eval_6_autonomia_desde_ayuda_inline(self):
        self.assert_cuerpo_contiene(
            "hsc-agent-cli <comando> --help",
            "handles, `command_args` y `next_steps`",
            "state` y `error_code",
        )


if __name__ == "__main__":
    unittest.main()
