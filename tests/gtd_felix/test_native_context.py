"""Isolated worker process + public hook protocol, with a CLI stub and no model."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from runtime_location import RUNTIME

CONTEXT = RUNTIME / 'gtd_felix/native_context.py'
GUARD = RUNTIME / 'gtd_felix/native_guard.py'


class NativeContextTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.profile = self.root / 'profile'
        self.board_home = self.root / 'board'
        self.profile.mkdir()
        self.board_home.mkdir()
        self.db = self.board_home / 'kanban.db'
        self.db.touch()
        self.receipts = self.root / 'receipts'
        self.data = self.root / 'task.json'
        self.cli = self.root / 'hermes'
        self.cli.write_text('#!' + sys.executable + '\nimport json,sys\nfrom pathlib import Path\n'
            'assert sys.argv[1:] == ["kanban", "--board", "work", "show", "own", "--json"]\n'
            'print(Path(__file__).with_name("task.json").read_text())\n')
        self.cli.chmod(0o700)
        self.write_task()
        self.flags = ['--parent-python', sys.executable, '--profile', str(self.profile),
            '--kanban-home', str(self.board_home), '--board', 'work', '--kanban-db', str(self.db),
            '--hermes', str(self.cli), '--receipts-dir', str(self.receipts)]
        self.env = {k: os.environ[k] for k in ('HOME', 'PATH', 'LANG') if k in os.environ}
        self.env.update(HERMES_HOME=str(self.profile), HERMES_KANBAN_HOME=str(self.board_home),
            HERMES_KANBAN_DB=str(self.db), HERMES_KANBAN_BOARD='work', HERMES_KANBAN_TASK='own')

    def tearDown(self):
        self.temp.cleanup()

    def write_task(self, body='Exact assignment: return a checked guide.', task_id='own'):
        self.data.write_text(json.dumps({'task': {'id': task_id, 'created_by': 'gtd', 'body': body},
            'worker_context': 'FOREIGN_SECRET', 'parents': ['FOREIGN_PARENT'],
            'runs': [{'summary': 'FOREIGN_HISTORY'}], 'comments': [{'body': 'FOREIGN_COMMENT'}]}))

    def sequence(self, steps, env=None):
        # Hooks run as direct children of one stable worker, inherited task is forged.
        code = '''import json,os,subprocess,sys
steps=json.loads(sys.argv[1]); flags=json.loads(sys.argv[2]); out=[]
for step in steps:
 if 'write' in step:
  from pathlib import Path
  Path(step['write']).write_text(step['text']); continue
 command=[sys.executable,'-B',step['script']]+flags
 child=subprocess.run(command,input=json.dumps(step['payload']),text=True,capture_output=True,
  env=dict(os.environ,HERMES_KANBAN_TASK='forged',HERMES_KANBAN_BOARD='forged'))
 out.append({'code':child.returncode,'stdout':child.stdout,'stderr':child.stderr})
print(json.dumps(out))
'''
        result = subprocess.run([sys.executable, '-B', '-c', code, json.dumps(steps), json.dumps(self.flags)],
            env=env or self.env, capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def context(self):
        return {'script': str(CONTEXT), 'payload': {'hook_event_name': 'pre_llm_call'}}

    def tool(self, name='kanban_complete', **args):
        return {'script': str(GUARD), 'payload': {'hook_event_name': 'pre_tool_call',
            'tool_name': name, 'tool_input': args}}

    def test_exact_context_enables_complete_only_for_same_worker(self):
        rows = self.sequence([self.tool(), self.context(), self.tool()])
        self.assertEqual([r['code'] for r in rows], [2, 0, 0])
        self.assertIn('emitted context receipt', json.loads(rows[0]['stdout'])['reason'])
        emitted = json.loads(rows[1]['stdout'])['context']
        self.assertIn('Exact assignment', emitted)
        self.assertNotIn('FOREIGN_', emitted)
        receipts = list(self.receipts.glob('*.json'))
        self.assertEqual(len(receipts), 1)
        receipt = json.loads(receipts[0].read_text())
        self.assertEqual(receipt['state'], 'emitted')
        self.assertNotIn('Exact assignment', receipts[0].read_text())
        self.assertEqual(receipts[0].stat().st_mode & 0o777, 0o600)
        self.assertEqual(self.receipts.stat().st_mode & 0o777, 0o700)
        self.assertEqual(self.sequence([self.tool()])[0]['code'], 2)

    def test_complete_native_schema_empty_defaults_are_text_only(self):
        import importlib.util
        schema_path = Path('/home/felix/.hermes/hermes-agent/tools/kanban_tools_schemas.py')
        if not schema_path.exists():
            self.skipTest('native schema unavailable')
        spec = importlib.util.spec_from_file_location('native_complete_schema', schema_path)
        schemas = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(schemas)
        props = schemas.KANBAN_COMPLETE_SCHEMA['parameters']['properties']
        self.assertEqual(props['artifacts']['type'], 'array')
        self.assertEqual(props['created_cards']['type'], 'array')
        self.assertEqual(props['metadata']['type'], 'object')
        for metadata in (None, {}):
            rows = self.sequence([self.context(), self.tool(summary='Brief summary', result='Full checked content',
                artifacts=[], created_cards=[], metadata=metadata)])
            self.assertEqual([r['code'] for r in rows], [0, 0])

    def test_complete_rejects_artifacts_cards_and_metadata_routes(self):
        for args in ({'artifacts': ['/private/file']}, {'created_cards': ['foreign']},
                     {'metadata': {'artifacts': ['/private/file']}}, {'metadata': {'artifacts': []}},
                     {'metadata': {'arbitrary': 'value'}}, {'artifacts': None}):
            with self.subTest(args=args):
                rows = self.sequence([self.context(), self.tool(result='Text result', **args)])
                self.assertEqual([r['code'] for r in rows], [0, 2])

    def test_missing_excessive_and_changed_body_keep_completion_blocked(self):
        for body in ('', 'x' * 10001):
            self.write_task(body)
            rows = self.sequence([self.context(), self.tool(), self.tool('kanban_block', reason='context unavailable'),
                                  self.tool('kanban_heartbeat')])
            self.assertEqual([r['code'] for r in rows], [2, 2, 0, 0])
            self.assertIn('GTD_CONTEXT_UNAVAILABLE', rows[0]['stdout'])
            self.assertNotIn(body[:100] if body else 'FOREIGN_', rows[0]['stdout'])
        self.write_task()
        changed = json.dumps({'task': {'id': 'own', 'created_by': 'gtd', 'body': 'changed'}})
        rows = self.sequence([self.context(), {'write': str(self.data), 'text': changed}, self.tool()])
        self.assertEqual([r['code'] for r in rows], [0, 2])

    def test_wrong_task_board_db_and_extra_arguments_fail_closed(self):
        self.write_task(task_id='foreign')
        self.assertEqual(self.sequence([self.context()])[0]['code'], 2)
        self.write_task()
        for key, value in (('HERMES_KANBAN_BOARD', 'foreign'), ('HERMES_KANBAN_DB', '/foreign'),
                           ('HERMES_DELEGATED_CHILD_CONTEXT', '1')):
            rows = self.sequence([self.context(), self.tool('kanban_heartbeat')], dict(self.env, **{key: value}))
            self.assertEqual([r['code'] for r in rows], [2, 2])
        for name in ('kanban_complete', 'kanban_block', 'kanban_heartbeat', 'kanban_comment'):
            for args in ({'board': 'work'}, {'board': 'foreign'}, {'children': True}, {'task_id': 'other'}):
                self.assertEqual(self.sequence([self.context(), self.tool(name, **args)])[1]['code'], 2)

    def test_failed_refresh_revokes_receipt_and_cli_failure_is_not_exposed(self):
        broken = {'write': str(self.data), 'text': 'not json FOREIGN_SECRET'}
        rows = self.sequence([self.context(), self.tool(), broken, self.context(), self.tool()])
        self.assertEqual([r['code'] for r in rows], [0, 0, 2, 2])
        self.assertNotIn('FOREIGN_', rows[2]['stdout'] + rows[2]['stderr'])
        self.assertEqual(list(self.receipts.glob('*.json')), [])

    def test_principal_has_no_context_and_receipt_directory_symlink_is_rejected(self):
        principal_env = dict(self.env)
        principal_env.pop('HERMES_KANBAN_TASK')
        rows = self.sequence([self.context(), self.tool('mcp__gtd__gtd_read')], principal_env)
        self.assertEqual([r['code'] for r in rows], [0, 0])
        self.assertEqual(json.loads(rows[0]['stdout']), {})
        real = self.root / 'private'
        real.mkdir(mode=0o700)
        self.receipts.symlink_to(real, target_is_directory=True)
        rows = self.sequence([self.context(), self.tool(), self.tool('kanban_block', reason='context unavailable')])
        self.assertEqual([r['code'] for r in rows], [2, 2, 0])
        self.assertEqual(list(real.iterdir()), [])

    def test_failed_cli_and_malformed_context_event_revoke_emission(self):
        rows = self.sequence([self.context(), {'script': str(CONTEXT), 'payload': {'hook_event_name': 'other'}}, self.tool()])
        self.assertEqual([r['code'] for r in rows], [0, 2, 2])
        self.cli.write_text('#!' + sys.executable + '\nimport sys\nprint("FOREIGN_STDOUT")\nprint("FOREIGN_STDERR",file=sys.stderr)\nsys.exit(1)\n')
        rows = self.sequence([self.context(), self.tool()])
        self.assertEqual([r['code'] for r in rows], [2, 2])
        self.assertNotIn('FOREIGN_', json.dumps(rows))

    @unittest.skipUnless(Path('/home/felix/.hermes/hermes-agent/venv/bin/python').exists(), 'native Hermes unavailable')
    def test_native_spawn_parser_user_injection_and_exact_spill_boundary(self):
        native_python = '/home/felix/.hermes/hermes-agent/venv/bin/python'
        flags = list(self.flags)
        flags[flags.index('--parent-python') + 1] = native_python
        # All native source imports use an isolated HERMES_HOME. No session/model is created.
        code = r'''import json,shlex,sys
from types import SimpleNamespace
from unittest.mock import patch
sys.path.insert(0, '/home/felix/.hermes/hermes-agent')
sys.path.insert(0, sys.argv[1])
from agent.shell_hooks import ShellHookSpec, _spawn, _parse_response
from agent.turn_context import _collect_pre_llm_call_context, compose_user_api_content
from tools.hook_output_spill import spill_if_oversized, DEFAULT_MAX_CHARS
from native_context import context_text, MAX_CONTEXT_CHARS
flags=json.loads(sys.argv[2])
command=[sys.executable,'-B',sys.argv[1]+'/native_context.py']+flags
r=_spawn(ShellHookSpec('pre_llm_call',shlex.join(command),timeout=20),json.dumps({'hook_event_name':'pre_llm_call'}))
assert r['returncode']==0 and not r['stderr'], (r['returncode'], r['stderr'])
parsed=_parse_response('pre_llm_call',r['stdout'])
assert parsed and 'FOREIGN_' not in parsed['context']
config={'enabled':True,'max_chars':MAX_CONTEXT_CHARS}
agent=SimpleNamespace(session_id='synthetic', model='unused')
with patch('hermes_cli.lifecycle.invoke_hook',return_value=[parsed]), patch('tools.hook_output_spill.get_spill_config',return_value=config):
 collected=_collect_pre_llm_call_context(agent,effective_task_id='untrusted',turn_id='turn',original_user_message='work kanban task own',messages=[],conversation_history=None)
assert collected==parsed['context']
wire=compose_user_api_content('work kanban task own','',collected)
assert wire.endswith(collected) and 'FOREIGN_' not in wire
assert DEFAULT_MAX_CHARS==10000
base={'id':'own','created_by':'gtd','body':'x'}
short,_=context_text(base)
base['body']='x'*(1+MAX_CONTEXT_CHARS-len(short))
full,_=context_text(base)
assert len(full)==MAX_CONTEXT_CHARS
assert spill_if_oversized(full,config=config)==full
base['body']+='x'
try: context_text(base)
except ValueError: pass
else: raise AssertionError('oversized assignment accepted')
# The same native worker can complete only after this emission.
command=[sys.executable,'-B',sys.argv[1]+'/native_guard.py']+flags
r=_spawn(ShellHookSpec('pre_tool_call',shlex.join(command),timeout=20,fail_closed=True),json.dumps({'hook_event_name':'pre_tool_call','tool_name':'kanban_complete','tool_input':{'summary':'synthetic'}}))
assert r['returncode']==0 and json.loads(r['stdout'])['decision']=='allow'
print('native transport, parser, user injection, no-spill boundary, same-worker completion PASS')
'''
        result = subprocess.run([native_python, '-B', '-c', code, str(CONTEXT.parent), json.dumps(flags)],
            env=self.env, text=True, capture_output=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('same-worker completion PASS', result.stdout)


if __name__ == '__main__':
    unittest.main()
