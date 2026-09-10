import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def load_script(name):
    path = SCRIPTS / name
    spec = importlib.util.spec_from_file_location(name.removesuffix(".py"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ProbeParameterTests(unittest.TestCase):
    def test_help_exposes_model_and_effort_for_each_probe(self):
        for name in ("probe_codex.py", "probe_hermes.py", "probe_independence.py"):
            result = subprocess.run([sys.executable, str(SCRIPTS / name), "--help"],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("--model", result.stdout)
            self.assertIn("--effort", result.stdout)

    def test_defaults_remain_the_current_selection(self):
        for name in ("probe_codex.py", "probe_hermes.py", "probe_independence.py"):
            module = load_script(name)
            self.assertEqual(module.DEFAULT_MODEL, "gpt-6-astra")
            self.assertEqual(module.DEFAULT_EFFORT, "max")

    def test_codex_probe_propagates_selection_to_config_and_thread(self):
        module = load_script("probe_codex.py")
        model, effort = "synthetic-codex-model", "high"
        servers = []
        config_contents = []

        class FakeServer:
            def __init__(self, workspace, config_home, log, prefix=None):
                self.config_home = config_home
                self.requests = []
                self.trusted = len(servers) == 1
                config_contents.append((config_home / "config.toml").read_text(encoding="utf-8"))
                log.write_text(
                    "Ignoring malformed agent role definition\n"
                    + ("project-malformed.toml\n" if self.trusted else ""),
                    encoding="utf-8",
                )
                servers.append(self)

            def request(self, method, params):
                self.requests.append((method, params))
                if method == "model/list":
                    return {"data": [{"model": model, "supportedReasoningEfforts": [
                        {"reasoningEffort": effort},
                    ]}]}
                if method == "skills/list":
                    return {"data": [{"skills": [
                        {"name": name, "scope": "repo", "enabled": True, "interface": {}}
                        for name in ("kora-probe-repo", "kora-probe-legacy", "kora-probe-linked")
                    ]}]}
                if method == "thread/start":
                    return {"model": model, "reasoningEffort": effort}
                raise AssertionError(method)

            def close(self):
                return None

        def fake_run(command, *args, **kwargs):
            if "generate-json-schema" in command:
                output = Path(command[command.index("--out") + 1]) / "v2"
                output.mkdir(parents=True)
                (output / "ThreadStartParams.json").write_text(
                    json.dumps({"properties": {"agentType": {}}}), encoding="utf-8"
                )
                (output / "SkillsListParams.json").write_text(
                    json.dumps({"properties": {"perCwdExtraUserRoots": {}}}), encoding="utf-8"
                )
            return subprocess.CompletedProcess(command, 0)

        output = io.StringIO()
        with patch.object(module.subprocess, "check_output", return_value="codex synthetic\n"), \
             patch.object(module.subprocess, "run", side_effect=fake_run), \
             patch.object(module, "AppServer", FakeServer), \
             contextlib.redirect_stdout(output):
            self.assertTrue(module.probe(model=model, effort=effort))

        result = json.loads(output.getvalue().strip())
        self.assertEqual(result["model"], model)
        self.assertEqual(result["thread_model"], model)
        self.assertEqual(result["thread_effort"], effort)
        self.assertEqual(result["requested_model"], model)
        self.assertEqual(result["requested_effort"], effort)
        self.assertEqual(len(servers), 2)
        thread = next(params for method, params in servers[0].requests if method == "thread/start")
        self.assertEqual(thread["model"], model)
        self.assertEqual(thread["config"]["model_reasoning_effort"], effort)
        config = config_contents[0]
        self.assertIn('model = "synthetic-codex-model"', config)
        self.assertIn('model_reasoning_effort = "high"', config)

    def test_hermes_outer_child_receives_selection_without_running_runtime(self):
        module = load_script("probe_hermes.py")
        model, effort = "synthetic-hermes-model", "low"
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "hermes"
            interpreter = source / "venv/bin/python"
            interpreter.parent.mkdir(parents=True)
            interpreter.touch()
            calls = []

            def fake_run(command, *args, **kwargs):
                calls.append(command)
                return subprocess.CompletedProcess(
                    command, 0, stdout=json.dumps({"plane": "native_cli_profiles_synthetic_offline", "passed": True}),
                    stderr="",
                )

            argv = [str(SCRIPTS / "probe_hermes.py"), "--source", str(source),
                    "--profile-entrypoints", "--model", model, "--effort", effort]
            with patch.object(module.subprocess, "run", side_effect=fake_run), \
                 patch.object(sys, "argv", argv), \
                 contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(module.main(), 0)

        self.assertEqual(len(calls), 1)
        command = calls[0]
        self.assertEqual(command[command.index("--model") + 1], model)
        self.assertEqual(command[command.index("--effort") + 1], effort)
        self.assertIn("--profile-entrypoints", command)

    def test_independence_phase_command_propagates_selection(self):
        module = load_script("probe_independence.py")
        model, effort = "synthetic-independent-model", "medium"
        with tempfile.TemporaryDirectory() as folder:
            work = Path(folder) / "work"
            reports = work / "reports"
            config = Path(folder) / "codex"
            reports.mkdir(parents=True)
            config.mkdir()
            calls = []

            def fake_run(command, *args, **kwargs):
                calls.append(command)
                output = Path(command[command.index("--output-last-message") + 1])
                output.write_text("{}", encoding="utf-8")
                return subprocess.CompletedProcess(command, 0)

            stream = io.StringIO()
            with patch.object(module.subprocess, "run", side_effect=fake_run), \
                 patch.object(module, "emit", side_effect=lambda value: stream.write(json.dumps(value) + "\n")):
                self.assertEqual(module.run_codex(["sandbox"], Path("/bin/codex"), work, config,
                                                  "synthetic", "No inferir.", model=model, effort=effort), "{}")

        self.assertEqual(len(calls), 1)
        command = calls[0]
        self.assertEqual(command[command.index("-m") + 1], model)
        self.assertEqual(command[command.index("-c", command.index("-m")) + 1],
                         'model_reasoning_effort="medium"')
        report = json.loads(stream.getvalue())
        self.assertEqual(report["model"], model)
        self.assertEqual(report["effort"], effort)


if __name__ == "__main__":
    unittest.main()
