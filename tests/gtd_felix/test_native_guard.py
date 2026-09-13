"""Real subprocess identity and public Hermes shell-hook transport, no model."""
import importlib.util
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from runtime_location import RUNTIME

GUARD = RUNTIME / 'gtd_felix/native_guard.py'
spec = importlib.util.spec_from_file_location('native_guard_boundary', GUARD)
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


class NativeGuardTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.profile, self.board = self.root / 'profile', self.root / 'board'
        self.profile.mkdir()
        self.board.mkdir()
        self.db = self.board / 'kanban.db'
        self.db.touch()
        self.argv = [sys.executable, '-B', str(GUARD), '--parent-python', sys.executable,
                     '--profile', str(self.profile), '--kanban-home', str(self.board),
                     '--board', 'work', '--kanban-db', str(self.db)]
        self.env = {key: os.environ[key] for key in ('HOME', 'PATH', 'LANG') if key in os.environ}
        self.env.update(HERMES_HOME=str(self.profile), HERMES_KANBAN_HOME=str(self.board),
                        HERMES_KANBAN_BOARD='work', HERMES_KANBAN_DB=str(self.db))

    def tearDown(self):
        self.temp.cleanup()

    def run_guard(self, tool, task=None, *, parent_task=None, extra_env=None, raw=None):
        env = dict(self.env)
        if parent_task is not None:
            env['HERMES_KANBAN_TASK'] = parent_task
        env.update(extra_env or {})
        payload = raw if raw is not None else json.dumps({'hook_event_name': 'pre_tool_call',
            'tool_name': tool, 'tool_input': {} if task is None else {'task_id': task}})
        # Parent starts with identity; child receives forged identity to prove it is ignored.
        code = "import subprocess,sys,json,os; a=json.loads(sys.argv[1]); e=dict(os.environ,HERMES_KANBAN_TASK='forged'); p=subprocess.run(a,input=sys.argv[2],text=True,capture_output=True,env=e); print(p.stdout,end=''); sys.exit(p.returncode)"
        result = subprocess.run([sys.executable, '-B', '-c', code, json.dumps(self.argv), payload],
            env=env, capture_output=True, text=True, timeout=10)
        return result.returncode, json.loads(result.stdout)['decision']

    def test_own_kanban_show_stays_blocked_even_with_native_default(self):
        schema_path = Path('/home/felix/.hermes/hermes-agent/tools/kanban_tools_schemas.py')
        if not schema_path.exists():
            self.skipTest('native Kanban schema unavailable')
        spec = importlib.util.spec_from_file_location('native_kanban_schema', schema_path)
        schemas = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(schemas)
        schema = schemas.KANBAN_SHOW_SCHEMA['parameters']
        self.assertEqual(schema['required'], [])
        self.assertEqual(set(schema['properties']), {'task_id', 'board'})
        self.assertEqual(schema['properties']['task_id']['type'], 'string')
        for args in ({'task_id': 'own'}, {}, {'task_id': ''}):
            payload = json.dumps({'hook_event_name': 'pre_tool_call', 'tool_name': 'kanban_show', 'tool_input': args})
            with self.subTest(args=args):
                self.assertEqual(self.run_guard('kanban_show', parent_task='own', raw=payload), (2, 'block'))

    def test_worker_uses_parent_identity_and_denies_other_tools_and_tasks(self):
        for tool in guard.ALLOWED:
            self.assertEqual(self.run_guard(tool, 'own', parent_task='own'),
                (2, 'block') if tool == 'kanban_complete' else (0, 'allow'))
            self.assertEqual(self.run_guard(tool, 'foreign', parent_task='own'), (2, 'block'))
        for tool in ('kanban_create', 'delegate_task', 'terminal', *guard.MCP_ALLOWED):
            self.assertEqual(self.run_guard(tool, parent_task='own'), (2, 'block'))

    def test_principal_allows_only_exact_mcp(self):
        for tool in guard.MCP_ALLOWED:
            self.assertEqual(self.run_guard(tool), (0, 'allow'))
        for tool in ('mcp__foreign__gtd_read', 'gtd_read', 'kanban_complete', 'terminal'):
            self.assertEqual(self.run_guard(tool), (2, 'block'))

    def test_delegated_wrong_profile_and_malformed_fail_closed(self):
        self.assertEqual(self.run_guard('kanban_complete', parent_task='own',
            extra_env={'HERMES_DELEGATED_CHILD_CONTEXT': '1'}), (2, 'block'))
        self.assertEqual(self.run_guard('mcp__gtd__gtd_read', extra_env={'HERMES_HOME': '/wrong'}), (2, 'block'))
        self.assertEqual(self.run_guard('mcp__gtd__gtd_read', raw='{'), (2, 'block'))
        self.assertEqual(self.run_guard('mcp__gtd__gtd_read', raw='x' * 65537), (2, 'block'))
        self.argv[self.argv.index('--parent-python') + 1] = '/bin/sh'
        self.assertEqual(self.run_guard('mcp__gtd__gtd_read'), (2, 'block'))

    def test_missing_proc_uid_and_race_fail_closed(self):
        with patch.object(guard, '_snapshot', side_effect=OSError('missing')):
            with self.assertRaises(OSError):
                guard.parent_identity(sys.executable, str(self.profile), str(self.board))
        status = 'Uid:\t999999\t999999\t999999\t999999\n'
        with patch.object(Path, 'read_text', return_value=status):
            with self.assertRaisesRegex(ValueError, 'parent_uid'):
                guard._snapshot(os.getppid(), Path(sys.executable).resolve())
        initial = ('HERMES_HOME=' + str(self.profile) + '\0HERMES_KANBAN_HOME=' + str(self.board)).encode()
        import io
        with patch.object(guard, '_snapshot', side_effect=['before', 'after']), \
             patch.object(Path, 'open', return_value=io.BytesIO(initial)):
            with self.assertRaisesRegex(ValueError, 'parent_identity_changed'):
                guard.parent_identity(sys.executable, str(self.profile), str(self.board))

    @unittest.skipUnless(Path('/home/felix/.local/bin/hermes').exists(), 'native Hermes CLI unavailable')
    def test_public_hooks_transport_in_isolated_profile(self):
        self.argv[self.argv.index('--parent-python') + 1] = '/home/felix/.hermes/hermes-agent/venv/bin/python'
        config = {'hooks_auto_accept': True, 'hooks': {'pre_tool_call': [
            {'matcher': '.*', 'command': shlex.join(self.argv), 'timeout': 5, 'fail_closed': True}]}}
        (self.profile / 'config.yaml').write_text(json.dumps(config))
        for tool, identity, task, expected in (
            ('kanban_complete', 'own', 'own', 'block'),
            ('kanban_block', 'own', 'own', 'allow'),
            ('kanban_heartbeat', 'own', 'own', 'allow'),
            ('kanban_comment', 'own', 'own', 'allow'),
            ('kanban_complete', 'own', 'other', 'block'),
            ('kanban_create', 'own', 'own', 'block'),
            ('mcp__gtd__gtd_read', None, None, 'allow'),
            ('mcp__gtd__gtd_command', None, None, 'allow'),
            ('mcp__gtd__gtd_dispatch', None, None, 'allow'),
            ('terminal', None, None, 'block')):
            env = dict(self.env)
            if identity:
                env['HERMES_KANBAN_TASK'] = identity
            payload = self.root / 'payload.json'
            payload.write_text(json.dumps({'args': {} if task is None else {'task_id': task}}))
            result = subprocess.run(['/home/felix/.local/bin/hermes', 'hooks', 'test', 'pre_tool_call',
                '--for-tool', tool, '--payload-file', str(payload)], env=env, capture_output=True,
                text=True, timeout=20)
            self.assertEqual(result.returncode, 0)
            self.assertIn('"decision":"' + expected + '"', result.stdout, result.stdout)


if __name__ == '__main__':
    unittest.main()
