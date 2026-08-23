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
OPENAI_YAML = SKILL_DIR / "agents/openai.yaml"


class TestCodexRoute(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.campos, cls.cuerpo = kora.parsear_archivo(
            SKILL.read_text("utf-8"))

    def test_identidad_forma_version_y_target_codex_only(self):
        self.assertEqual(
            self.campos["urn"], "urn:dev:artefacto:codex-route")
        self.assertEqual(self.campos["nombre"], "codex-route")
        self.assertEqual(self.campos["version"], "3.0.0")
        self.assertEqual(self.campos["forma"], "habilidad")
        self.assertEqual(self.campos["arnes"], "disciplina")
        self.assertEqual(self.campos["targets"], ["codex"])
        self.assertEqual(self.campos["alcance"], "usuario")

    def test_invocacion_es_explicita_en_metadata_runtime(self):
        metadata = OPENAI_YAML.read_text("utf-8")
        self.assertIn('display_name: "Codex Route"', metadata)
        self.assertIn("short_description:", metadata)
        self.assertIn("default_prompt:", metadata)
        self.assertIn("allow_implicit_invocation: false", metadata)
        self.assertIn("invocar explícitamente", self.cuerpo.lower())

    def test_route_only_es_default_y_run_requiere_autoridad_explicita(self):
        cuerpo = " ".join(self.cuerpo.split()).lower()
        self.assertIn("`route-only` — predeterminado", cuerpo)
        self.assertIn("no crear sesiones", cuerpo)
        self.assertIn("`route-and-run` — explícito", cuerpo)
        self.assertIn("no amplía permisos", cuerpo)

    def test_politica_cerrada_admite_solo_tres_pares(self):
        routing = (REFERENCIAS / "model-effort-routing.md").read_text(
            "utf-8")
        routing_normalizado = " ".join(routing.lower().split())
        for par in (
                "{model: gpt-5.6-sol, effort: high}",
                "{model: gpt-5.6-sol, effort: max}",
                "{model: gpt-5.6-luna, effort: max}"):
            self.assertIn(par, routing)
        self.assertIn("terra: forbidden", routing)
        self.assertIn("sol en `low|medium|xhigh|ultra`", routing_normalizado)
        self.assertIn("luna por debajo de `max`", routing_normalizado)
        self.assertIn("silent_fallback: forbidden", routing)
        self.assertIn("unpinned_descendants: forbidden", routing)

    def test_fallbacks_fallan_cerrado_y_preflight_observa_runtime(self):
        routing = (REFERENCIAS / "model-effort-routing.md").read_text(
            "utf-8")
        protocolo = (REFERENCIAS / "communication-protocol.md").read_text(
            "utf-8")
        for testigo in (
                "colapsar", "blocked", "director_pair_not_allowed",
                "director_pair_unobserved", "requested_pair_not_allowed",
                "sol_required_unavailable"):
            self.assertIn(testigo, routing)
        for campo in (
                "root_model_observed", "root_model_allowed",
                "spawn_available", "model_override_available",
                "luna_max_available", "sol_high_available",
                "sol_max_available", "exact_pair_override_available",
                "fork_control_available",
                "lifecycle_controls"):
            self.assertIn(campo, protocolo)

    def test_routing_es_dos_pasadas_y_perfila_cada_sesion(self):
        cuerpo = " ".join(self.cuerpo.lower().split())
        self.assertIn("cem global residual", cuerpo)
        self.assertIn("selección provisional", cuerpo)
        self.assertIn("calcular `j`", cuerpo)
        self.assertIn("ajustar el par de la directora", cuerpo)
        self.assertIn("cem local residual", cuerpo)
        self.assertLess(cuerpo.index("calcular `j`"),
                        cuerpo.index("ajustar el par de la directora"))
        routing = (REFERENCIAS / "model-effort-routing.md").read_text(
            "utf-8")
        self.assertNotIn("max(A,N,E,O,C,J)", routing.replace(" ", ""))
        self.assertIn("integration_load", routing)

    def test_schema_separa_recomendado_disponible_efectivo_y_cumplimiento(self):
        schema = (REFERENCIAS / "communication-protocol.md").read_text(
            "utf-8")
        for campo in (
                "recommended_model", "available_models", "effective_model",
                "model_compliance", "recommended_effort",
                "available_efforts", "effective_effort",
                "effort_compliance"):
            self.assertIn(campo, schema)
        self.assertIn("cognitive_class", schema)
        self.assertIn("routing_basis", schema)

    def test_ruta_decide_superficie_modelo_y_esfuerzo(self):
        superficies_path = REFERENCIAS / "execution-surfaces.md"
        self.assertTrue(superficies_path.is_file())
        superficies = superficies_path.read_text("utf-8")
        superficies_normalizadas = " ".join(superficies.lower().split())
        for testigo in (
                "route_candidate = (execution_surface, model, effort)",
                "current_session", "subagent", "independent_thread",
                "codex_app__create_thread", "codex_app__list_projects",
                "codex_app__read_thread",
                "codex_app__send_message_to_thread",
                "codex_app__wait_threads", "codex_app__handoff_thread",
                "codex_app__share_thread",
                "codex_app__list_archived_threads",
                "codex_app__read_thread_terminal",
                "codex_app__open_in_codex"):
            self.assertIn(testigo, superficies)
        self.assertIn("solicitud explícita", superficies_normalizadas)
        self.assertIn("propiedad del usuario", superficies_normalizadas)
        self.assertIn("worktree por defecto", superficies_normalizadas)
        self.assertIn("isgitrepository=false", superficies_normalizadas)
        self.assertIn("environment.type=local", superficies_normalizadas)
        self.assertIn("clientthreadid", superficies_normalizadas)
        self.assertIn("fork_thread` a worktree", superficies_normalizadas)
        self.assertIn("no archivarlo", superficies_normalizadas)

    def test_thread_separa_creacion_de_override_de_modelo(self):
        superficies = (
            REFERENCIAS / "execution-surfaces.md").read_text("utf-8")
        protocolo = (
            REFERENCIAS / "communication-protocol.md").read_text("utf-8")
        contrato = " ".join(
            f"{self.cuerpo}\n{superficies}\n{protocolo}".lower().split())

        self.assertIn("creation_authorized", protocolo)
        self.assertIn("pair_override_authorized", protocolo)
        self.assertIn("par concreto", contrato)
        self.assertIn("model_override_not_authorized", contrato)
        self.assertIn("no crear el thread", contrato)

    def test_goal_nativo_se_evalua_sin_activacion_implicita(self):
        protocolo = (REFERENCIAS / "communication-protocol.md").read_text(
            "utf-8")
        protocolo_normalizado = " ".join(protocolo.lower().split())
        for campo in (
                "native_goal", "fit:", "scope:", "activation:",
                "stopping_condition:"):
            self.assertIn(campo, protocolo)
        self.assertIn("s0 + goal", protocolo_normalizado)
        self.assertIn("`create_goal`", protocolo)
        self.assertIn("`get_goal`", protocolo)
        self.assertIn("goal no reemplaza", protocolo_normalizado)
        self.assertIn("autorización explícita", protocolo_normalizado)

    def test_comparacion_privilegiada_luna_max_con_sol_high(self):
        routing = (REFERENCIAS / "model-effort-routing.md").read_text(
            "utf-8")
        routing_normalizado = " ".join(routing.lower().split())
        self.assertIn("gpt-5.6-luna:max, gpt-5.6-sol:high", routing_normalizado)
        self.assertIn("ambos triples sean ejecutables", routing_normalizado)
        self.assertIn("comparación privilegiada", routing_normalizado)
        self.assertIn("discarded_candidate_reason", routing)
        self.assertIn("eval representativa", routing_normalizado)
        self.assertIn("sol max", routing_normalizado)

    def test_fast_path_y_salida_por_defecto_son_compactos(self):
        cuerpo = " ".join(self.cuerpo.split()).lower()
        self.assertIn("luna max", cuerpo)
        self.assertIn("sol high", cuerpo)
        self.assertIn("sol max", cuerpo)
        self.assertIn("`compact_graph_route` — predeterminado", cuerpo)
        self.assertIn("`full_graph_route`", cuerpo)
        self.assertLessEqual(len(self.cuerpo.splitlines()), 180)

    def test_grafos_separan_control_datos_y_decision_local_global(self):
        protocolo = (REFERENCIAS / "communication-protocol.md").read_text(
            "utf-8")
        for testigo in (
                "M_c = M_parent ∪ M_peer",
                "M_peer ⊆ E_dependency ∪ E_review",
                "TASK", "INTERRUPT", "CLOSE", "CONTRACT", "EVIDENCE",
                "LOCAL_DECISION", "GLOBAL_DECISION"):
            self.assertIn(testigo, protocolo)

    def test_s8_es_iteracion_acotada_y_cada_iteracion_es_dag(self):
        catalogo = " ".join((
            REFERENCIAS / "topology-catalog.md").read_text("utf-8").split())
        for testigo in (
                "iteration_control", "max_iterations",
                "max_consecutive_failures", "minimum_improvement",
                "evaluator_mutable: false", "rollback: required",
                "cada iteración finita es un DAG"):
            self.assertIn(testigo, catalogo)

    def test_lifecycle_usa_operaciones_segun_contrato_vivo(self):
        protocolo = (REFERENCIAS / "communication-protocol.md").read_text(
            "utf-8")
        protocolo_normalizado = " ".join(protocolo.lower().split())
        self.assertIn(
            "planned → spawned → acknowledged → running → completed → "
            "integrated → closed", " ".join(protocolo.split()))
        self.assertIn("`send_message` no inicia", protocolo)
        self.assertIn("`followup_task`", protocolo)
        self.assertIn("si `close_agent` está expuesto", protocolo_normalizado)
        self.assertIn("limitación de lifecycle", protocolo_normalizado)

    def test_persistencia_no_colisiona_y_worktree_exige_interferencia_real(self):
        sgm = (REFERENCIAS / "session-graph-matrix.md").read_text("utf-8")
        for nivel in range(5):
            self.assertIn(f"L{nivel}", sgm)
        self.assertNotRegex(sgm, r"\bP[0-4]\b")
        protocolo = (REFERENCIAS / "communication-protocol.md").read_text(
            "utf-8")
        self.assertIn("workspace compartido + un escritor", protocolo)
        self.assertIn("interfaces inestables", protocolo)

    def test_topologia_base_fases_y_modificadores_no_son_suma_de_codigos(self):
        dominios = (REFERENCIAS / "domain-overrides.md").read_text("utf-8")
        self.assertIn("base_topology", dominios)
        self.assertIn("phases", dominios)
        self.assertIn("modifiers", dominios)
        self.assertNotRegex(dominios, r"S\d\s*\+\s*S\d")
        self.assertIn("manejo clínico", dominios.lower())
        self.assertIn("Sol monosession", dominios)

    def test_referencias_progresivas_existen_y_estan_enlazadas(self):
        nombres = (
            "cognitive-epistemic-matrix.md",
            "session-graph-matrix.md",
            "topology-catalog.md",
            "communication-protocol.md",
            "execution-surfaces.md",
            "model-effort-routing.md",
            "domain-overrides.md",
            "calibration.md",
        )
        for nombre in nombres:
            with self.subTest(nombre=nombre):
                self.assertTrue((REFERENCIAS / nombre).is_file())
                self.assertIn(f"referencias/{nombre}", self.cuerpo)

    def test_matrices_miden_complejidad_residual_y_gates_locales(self):
        cem = (REFERENCIAS / "cognitive-epistemic-matrix.md").read_text(
            "utf-8")
        sgm = (REFERENCIAS / "session-graph-matrix.md").read_text("utf-8")
        self.assertIn("complejidad residual", cem)
        self.assertIn("Gate de Luna Max", cem)
        self.assertIn("Gate de Sol High", cem)
        self.assertIn("Elevación a Sol Max", cem)
        self.assertNotIn("Gate de Terra", cem)
        self.assertIn("R gobierna autonomía y verificación", cem)
        self.assertIn("D ≥ 2", sgm)
        self.assertIn("K ≥ 2", sgm)

    def test_calibracion_mide_cumplimiento_y_arrepentimiento(self):
        calibracion = (REFERENCIAS / "calibration.md").read_text("utf-8")
        for metrica in (
                "pair_policy_compliance", "unobserved_pair_rate",
                "execution_surface_compliance",
                "routing_regret", "graph_regret",
                "goal_regret", "independent_thread_regret",
                "pareto_dominated_route_rate",
                "late_escalation_rate",
                "human_major_correction_rate"):
            self.assertIn(metrica, calibracion)
        self.assertIn("tres pares permitidos", calibracion)

    def test_emision_codex_incluye_politica_de_invocacion(self):
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
        self.assertIn("=== codex/skills/codex-route/SKILL.md ===",
                      resultado.stdout)
        self.assertIn(
            "=== codex/skills/codex-route/agents/openai.yaml ===",
            resultado.stdout)
        self.assertIn("allow_implicit_invocation: false", resultado.stdout)


if __name__ == "__main__":
    unittest.main()
