# -*- coding: utf-8 -*-
"""Contrato focal de la skill KORA codex-route."""
import subprocess
import sys
import unittest
from pathlib import Path

import kora


RAIZ = Path(__file__).resolve().parent.parent
SKILL_DIR = RAIZ / "artefactos/skills/dev/codex-route"
SKILL = SKILL_DIR / "SKILL.md"
REFERENCIAS = SKILL_DIR / "referencias"


class TestCodexRoute(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.campos, cls.cuerpo = kora.parsear_archivo(
            SKILL.read_text("utf-8"))

    def test_identidad_forma_y_target_codex_only(self):
        self.assertEqual(
            self.campos["urn"], "urn:dev:artefacto:codex-route")
        self.assertEqual(self.campos["nombre"], "codex-route")
        self.assertEqual(self.campos["version"], "1.0.0")
        self.assertEqual(self.campos["forma"], "habilidad")
        self.assertEqual(self.campos["arnes"], "disciplina")
        self.assertEqual(self.campos["targets"], ["codex"])
        self.assertEqual(self.campos["alcance"], "usuario")

    def test_route_only_es_default_y_run_requiere_instruccion_explicita(self):
        cuerpo = " ".join(self.cuerpo.split()).lower()
        self.assertIn("`route-only` — predeterminado", cuerpo)
        self.assertIn("no crear sesiones", cuerpo)
        self.assertIn("`route-and-run` — explícito", cuerpo)
        self.assertIn("no amplía permisos", cuerpo)

    def test_modela_cinco_grafos_y_autoridad_central(self):
        cuerpo = self.cuerpo.lower()
        for testigo in (
                "γ = (v, t_g, d_t, m_c, w_f, θ)",
                "árbol de gobierno explícito",
                "`m_c ⊆ d_t ∪ e_review`",
                "la directora conserva objetivo",
                "la mensajería coordina información; no sincroniza escrituras",
        ):
            self.assertIn(testigo, cuerpo)

    def test_fast_path_no_fabrica_ceremonia(self):
        cuerpo = " ".join(self.cuerpo.split()).lower()
        self.assertIn("usar s0 sin desplegar matrices", cuerpo)
        self.assertIn("no usar dos matrices", cuerpo)
        self.assertIn("no maximizar sesiones", cuerpo)

    def test_referencias_progresivas_existen_y_estan_enlazadas(self):
        nombres = (
            "cognitive-epistemic-matrix.md",
            "session-graph-matrix.md",
            "topology-catalog.md",
            "communication-protocol.md",
            "model-effort-routing.md",
            "domain-overrides.md",
            "calibration.md",
        )
        for nombre in nombres:
            with self.subTest(nombre=nombre):
                self.assertTrue((REFERENCIAS / nombre).is_file())
                self.assertIn(f"referencias/{nombre}", self.cuerpo)

    def test_matrices_tienen_dimensiones_y_gates_completos(self):
        cem = (REFERENCIAS / "cognitive-epistemic-matrix.md").read_text(
            "utf-8")
        sgm = (REFERENCIAS / "session-graph-matrix.md").read_text("utf-8")
        for dimension in (
                "A — Ambigüedad", "N — Novedad", "E — Especialización",
                "O — Debilidad", "B — Amplitud", "C — Acoplamiento",
                "H — Horizonte", "R — Riesgo"):
            self.assertIn(dimension, cem)
        for dimension in (
                "D — Descomponibilidad", "K — Separabilidad",
                "P — Holgura", "M — Comunicación", "W — Contención",
                "J — Integración", "L — Valor", "I — Independencia"):
            self.assertIn(dimension, sgm)
        self.assertIn("No promediar", cem)
        self.assertIn("D ≥ 2", sgm)
        self.assertIn("K ≥ 2", sgm)

    def test_catalogo_contiene_s0_a_s9(self):
        catalogo = (REFERENCIAS / "topology-catalog.md").read_text("utf-8")
        for codigo in range(10):
            self.assertIn(f"## S{codigo} —", catalogo)

    def test_routing_de_modelo_falla_cerrado_a_capacidad_viva(self):
        routing = (REFERENCIAS / "model-effort-routing.md").read_text(
            "utf-8")
        for testigo in (
                "modelo recomendado, disponible y efectivamente usado",
                "superficie actual",
                "gpt-5.6-sol",
                "gpt-5.6-terra",
                "gpt-5.6-luna",
                "no un override ejecutable garantizado",
                "Ultra es una política de ejecución, no una topología",
        ):
            self.assertIn(testigo, routing)

    def test_protocolo_usa_solo_operaciones_vivas(self):
        protocolo = (REFERENCIAS / "communication-protocol.md").read_text(
            "utf-8")
        for operacion in (
                "`spawn_agent`", "`send_message`", "`followup_task`",
                "`wait_agent`", "`list_agents`", "`interrupt_agent`"):
            self.assertIn(operacion, protocolo)
        self.assertIn("No inventar `close_agent`", protocolo)

    def test_calibracion_no_finge_validacion_predictiva(self):
        calibracion = (REFERENCIAS / "calibration.md").read_text("utf-8")
        self.assertIn("predictor validado", calibracion.lower())
        self.assertIn("no prueba generalización", calibracion.lower())

    def test_emision_codex_es_materializable(self):
        resultado = subprocess.run(
            [
                sys.executable,
                str(RAIZ / "kora.py"),
                "transmutar",
                "--urn", "urn:dev:artefacto:codex-route",
                "--target", "codex",
                "--stdout",
            ],
            cwd=RAIZ,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertIn("name: codex-route", resultado.stdout)
        self.assertIn("target: codex", resultado.stdout)


if __name__ == "__main__":
    unittest.main()
