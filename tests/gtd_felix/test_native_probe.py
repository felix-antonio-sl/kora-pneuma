import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('gtd_native_probe', Path(__file__).resolve().parents[2] / 'scripts/gtd_native_probe.py')
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)


class NativeProbeTests(unittest.TestCase):
    def test_environment_drops_all_ambient_credentials_and_platform_settings(self):
        env = probe.clean_environment({'HOME': '/h', 'PATH': '/bin', 'TELEGRAM_BOT_TOKEN': 'secret', 'OPENAI_API_KEY': 'secret', 'HERMES_HOME': '/other', 'API_SERVER_ENABLED': 'false', 'PYTHONPATH': '/bad'}, Path('/canary'), 1234, 'ephemeral')
        self.assertEqual(set(env), {'HOME', 'PATH', 'HERMES_HOME', 'HERMES_KANBAN_HOME', 'API_SERVER_ENABLED', 'API_SERVER_HOST', 'API_SERVER_PORT', 'API_SERVER_KEY', 'HERMES_KANBAN_DISPATCH_IN_GATEWAY', 'PYTHONUNBUFFERED'})
        self.assertEqual(env['HERMES_KANBAN_HOME'], '/canary')

    def test_existing_home_is_never_modified(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp) / 'canary'
            home.mkdir()
            marker = home / 'config.yaml'
            marker.write_text('preserve')
            with self.assertRaises(FileExistsError):
                probe.create_home(home)
            self.assertEqual(marker.read_text(), 'preserve')

    def test_symlink_home_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp) / 'canary'
            home.symlink_to(Path(tmp), target_is_directory=True)
            with self.assertRaises(FileExistsError):
                probe.create_home(home)

    def test_failed_acceptance_stops(self):
        with self.assertRaisesRegex(RuntimeError, 'red'):
            probe.require(False, 'red')

    def test_config_has_native_bounds_and_no_secrets(self):
        import json
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp) / 'canary'
            probe.create_home(home)
            config = json.loads((home / 'config.yaml').read_text())
            self.assertEqual(config['agent']['max_turns'], 1)
            self.assertEqual(config['agent']['api_max_retries'], 1)
            self.assertEqual(config['agent']['run_budget_seconds'], 45)
            self.assertEqual((home / '.env').read_text(), '')
            self.assertEqual(set(config['platforms']), {'api_server'})

    def test_terminal_does_not_treat_stop_acceptance_as_cancelled(self):
        from unittest.mock import Mock, patch
        instance = object.__new__(probe.Probe)
        instance.receipt = {'runs': []}
        instance.request = Mock(side_effect=[(200, {'status': 'running'}), (200, {'status': 'cancelled'})])
        with patch.object(probe.time, 'sleep'):
            self.assertEqual(instance.terminal('synthetic')['status'], 'cancelled')
        self.assertEqual(instance.request.call_count, 2)

    def test_terminal_status_http_error_is_failure(self):
        from unittest.mock import Mock
        instance = object.__new__(probe.Probe)
        instance.receipt = {'runs': []}
        instance.request = Mock(return_value=(404, {}))
        with self.assertRaisesRegex(RuntimeError, 'unavailable'):
            instance.terminal('missing')

    def test_exact_process_stopped_with_kill_fallback(self):
        from unittest.mock import Mock
        import subprocess
        instance = object.__new__(probe.Probe)
        child = Mock(pid=123, returncode=-9)
        child.poll.return_value = None
        child.wait.side_effect = [subprocess.TimeoutExpired('gateway', 20), -9]
        instance.process = child
        instance.receipt = {'checks': {}}
        instance.log = None
        instance.stop()
        child.terminate.assert_called_once()
        child.kill.assert_called_once()
        self.assertIsNone(instance.process)
        self.assertEqual(instance.receipt['checks']['gateway_stopped_123']['status'], 'PASS')
