import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def load_probe(runtime):
    path = SCRIPTS / f"probe_{runtime}.py"
    spec = importlib.util.spec_from_file_location(f"native_probe_{runtime}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class NativeCanaryFixtureTests(unittest.TestCase):
    def test_effect_snapshot_detects_links_and_empty_directories(self):
        for runtime in ("codex", "hermes"):
            module = load_probe(runtime)
            with self.subTest(runtime=runtime), tempfile.TemporaryDirectory() as folder:
                root = Path(folder)
                before = module._snapshot_files(root)
                (root / "extra").mkdir()
                (root / "link").symlink_to("absent-target")
                after = module._snapshot_files(root)
                self.assertEqual(module._changed_files(before, after), ["extra", "link"])

    def test_flags_keep_basic_and_expose_extended_scenarios(self):
        for runtime, mode in (("codex", "--canary"), ("hermes", "--live")):
            result = subprocess.run([sys.executable, str(SCRIPTS / f"probe_{runtime}.py"), "--help"],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("--scenario", result.stdout)
            for scenario in ("basic", "resources", "update", "incomplete"):
                self.assertIn(scenario, result.stdout)
            self.assertIn(mode, result.stdout)

    def test_prepare_and_render_never_execute_the_helper(self):
        for runtime in ("codex", "hermes"):
            module = load_probe(runtime)
            with self.subTest(runtime=runtime), tempfile.TemporaryDirectory() as folder:
                fixture = module.build_synthetic_fixture(Path(folder), "resources")
                evidence = module.evaluate_synthetic_fixture(fixture, advance=False)
                self.assertTrue(evidence["ok"], evidence)
                self.assertTrue(evidence["checks"]["helper_not_autoexecuted"])
                self.assertFalse(fixture["effect"].exists())
                self.assertTrue(fixture["template"].is_file())
                self.assertTrue(fixture["helper"].stat().st_mode & 0o111)
                self.assertTrue(fixture["sentinel"].is_file())
                edge = evidence["conditional_edge"]
                self.assertEqual(edge["target"], module.OPTIONAL_NEED)
                self.assertEqual(edge["status"], "unavailable")
                self.assertIn("Recorrido no disponible", (
                    fixture["workspace"] / (".agents/skills/kora-canary-lookup/SKILL.md"
                                             if runtime == "codex" else
                                             "../runtime/skills/kora-canary-lookup/SKILL.md")
                ).read_text())

    def test_authorized_helper_has_only_temporary_bounded_effect(self):
        for runtime in ("codex", "hermes"):
            module = load_probe(runtime)
            with self.subTest(runtime=runtime), tempfile.TemporaryDirectory() as folder:
                fixture = module.build_synthetic_fixture(Path(folder), "resources")
                before = module.evaluate_synthetic_fixture(fixture, advance=False)
                helper = module.run_authorized_helper(fixture)
                after = module.evaluate_synthetic_fixture(fixture, helper_result=helper, advance=False)
                self.assertTrue(before["ok"], before)
                self.assertTrue(after["ok"], after)
                self.assertTrue(helper["effect_absent_before"])
                self.assertTrue(helper["effect_created"])
                self.assertTrue(helper["effect_marker"])
                self.assertTrue(helper["effect_temporary"])
                self.assertTrue(helper["sentinel_preserved"])
                self.assertEqual(helper["changed_files"], ["canary-authorized-effect.json"])
                self.assertEqual(helper["unexpected_changes"], [])
                self.assertEqual(json.loads(fixture["effect"].read_text()),
                                 {"marker": module.HELPER_EFFECT_MARKER, "temporary": True})

    def test_update_reads_new_source_between_uses(self):
        for runtime in ("codex", "hermes"):
            module = load_probe(runtime)
            with self.subTest(runtime=runtime), tempfile.TemporaryDirectory() as folder:
                fixture = module.build_synthetic_fixture(Path(folder), "update")
                evidence = module.evaluate_synthetic_fixture(fixture)
                self.assertTrue(evidence["ok"], evidence)
                self.assertEqual(evidence["loaded_versions"], ["V1", "V2"])
                self.assertTrue(evidence["checks"]["source_v1_read"])
                self.assertTrue(evidence["checks"]["source_v2_read"])
                self.assertTrue(evidence["checks"]["same_source_path"])
                self.assertTrue(evidence["checks"]["native_role_v1_materialized"])
                self.assertTrue(evidence["checks"]["native_role_v2_materialized"])
                self.assertTrue(fixture["sentinel"].is_file())

    def test_incomplete_contract_is_declared_without_faking_runtime_evidence(self):
        for runtime in ("codex", "hermes"):
            module = load_probe(runtime)
            with self.subTest(runtime=runtime), tempfile.TemporaryDirectory() as folder:
                fixture = module.build_synthetic_fixture(Path(folder), "incomplete")
                evidence = module.evaluate_synthetic_fixture(fixture)
                self.assertTrue(evidence["ok"], evidence)
                self.assertEqual(evidence["expected_contract"]["child"]["status"], "INCOMPLETE")
                self.assertEqual(evidence["expected_contract"]["child"]["limitation"], "MISSING_INPUT")
                self.assertEqual(evidence["expected_contract"]["parent"]["status"], "CLOSED_WITH_LIMITATION")
                self.assertEqual(evidence["expected_contract"]["parent"]["limitation"], "MISSING_INPUT")
                self.assertTrue(evidence["checks"]["incomplete_contract_declared"])
                self.assertNotIn("child_result", evidence)
                self.assertNotIn("parent_closure", evidence)
                self.assertFalse(fixture["effect"].exists())
                self.assertTrue(fixture["sentinel"].is_file())

    def test_independence_offline_fixture_matrix_is_model_free(self):
        module = load_probe("independence")
        report = module.synthetic_fixture_checks()
        self.assertTrue(report["ok"], report)
        self.assertTrue(report["helper_autoexecution_absent"])
        self.assertIsNone(report["model"])
        self.assertIsNone(report["effort"])
        self.assertEqual(set(report["scenarios"]), {"codex", "hermes"})
        for runtime_report in report["scenarios"].values():
            self.assertEqual(set(runtime_report), {"basic", "resources", "update", "incomplete"})
            self.assertTrue(all(item["ok"] for item in runtime_report.values()))

    def test_extended_prompts_do_not_supply_resource_or_update_answers(self):
        forbidden = {
            "KORA_SYNTHETIC_RESOURCE_KNOWLEDGE_V1", "KORA_SYNTHETIC_RESOURCE_KNOWLEDGE_V2",
            "CONDITIONAL_UNAVAILABLE", "KORA_CANARY_HELPER_EFFECT",
        }
        for runtime in ("codex", "hermes"):
            module = load_probe(runtime)
            with self.subTest(runtime=runtime), tempfile.TemporaryDirectory() as folder:
                fixture = module.build_synthetic_fixture(Path(folder), "resources")
                resource_prompt = (module._extended_prompt(fixture, "resources", False, phase="first")
                                   if runtime == "codex" else
                                   module._extended_prompt(fixture, "resources", "first"))
                update_prompt = (module._extended_prompt(fixture, "update", False, phase="v1")
                                 if runtime == "codex" else
                                 module._extended_prompt(fixture, "update", "first"))
                self.assertFalse(any(value in resource_prompt for value in forbidden), resource_prompt)
                self.assertFalse(any(value in update_prompt for value in forbidden), update_prompt)

    def test_hermes_does_not_claim_child_evidence_without_delegation(self):
        module = load_probe("hermes")
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            with patch.object(module, "read_live_access_token") as auth:
                report = module.live_probe(root, root, root / "auth.json", scenario="incomplete")
            auth.assert_not_called()
            self.assertFalse(report["passed"])
            self.assertFalse(report["inference_started"])
            self.assertFalse(report["child_result_observed"])
            self.assertEqual(report["preflight"], "DELEGATION_NOT_EXPOSED_BY_CANARY")

    def test_codex_child_evidence_requires_completed_collaboration_result(self):
        module = load_probe("codex")
        prompt_echo = [{"item": {"type": "collab_tool_call", "tool": "spawn_agent",
                                  "arguments": {"marker": "KORA_CHILD_INCOMPLETE"}}}]
        completed = [{"item": {"type": "collab_wait.completed", "tool": "wait",
                                "agents_states": {"child": {"result": json.dumps({
                                    "status": "INCOMPLETE", "limitation": "MISSING_INPUT",
                                    "marker": "KORA_CHILD_INCOMPLETE"})}}}}]
        self.assertFalse(module._incomplete_child_result(prompt_echo)["observed"])
        result = module._incomplete_child_result(completed)
        self.assertTrue(result["observed"])
        self.assertEqual(result["status"], "INCOMPLETE")
        self.assertEqual(result["limitation"], "MISSING_INPUT")

        # The native stream historically exposed the completed wait item but
        # no separate spawn_agent event.  The child result plus that wait is
        # sufficient evidence; a prompt/tool-call echo remains insufficient.
        self.assertTrue(module._delegation_tools_observed({"wait"}))
        outer_completed = [{"type": "item.completed", "item": {
            "type": "collab_tool_call", "status": "completed", "tool": "wait",
            "result": {"status": "INCOMPLETE", "limitation": "MISSING_INPUT",
                       "marker": "KORA_CHILD_INCOMPLETE"},
        }}]
        self.assertTrue(module._incomplete_child_result(outer_completed)["observed"])


if __name__ == "__main__":
    unittest.main()
