"""Offline public-transport probes against actual Store and ExecutionControl."""
import asyncio
from datetime import datetime, timezone
import hashlib
import json
import os
import shlex
import subprocess
from pathlib import Path
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

import aiohttp
from aiohttp import web

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from gtd_felix import GTDService
from gtd_felix.control import ExecutionControl
from gtd_felix.hermes import HermesAdapter


class HermesTest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for name in ('native', 'board', 'workspace'):
            (self.root / name).mkdir()
        self.service = GTDService(self.root / 'data', executor_actors=['gtd-worker'])
        self.budget_config = dict(period_start=datetime.now(timezone.utc).isoformat(), period_seconds=3600,
            max_cost_usd=10, max_runtime_seconds=1000, recovery_cost_usd=1, recovery_runtime_seconds=50,
            max_active=2, max_job_runtime_seconds=300, max_retries=1, max_descendants=1)
        self.control = ExecutionControl(self.service, self.budget_config)
        self.sequence = 0
        self.item = self.service.capture('felix', 'capture', 'Synthetic preparation')['item']
        bot = dict(id='fixture', state='available', source_urn='urn:test:fixture', host='synthetic',
            profile='fixture', capabilities=['prepare_private'], item_id=self.item['id'], probe_evidence='synthetic://probe')
        self.assertEqual(self.control.register_bot('felix', 'bot', bot)['status'], 'applied')
        self.env = patch.dict(os.environ, {'SYNTHETIC_HERMES_KEY': 'fake-private-test-key'})
        self.env.start()
        self.native_config = {'agent.execution_guidance': False, 'tools.tool_search.enabled': 'off', 'agent.max_turns': 1, 'agent.run_budget_seconds': 20,
            'agent.api_max_retries': 1, 'agent.reasoning_effort': 'low', 'agent.disabled_toolsets': [], 'platform_toolsets.api_server': [],
            'platform_toolsets.cli': [], 'kanban.auto_decompose': False, 'kanban.max_spawn': 1,
            'kanban.max_in_progress': 1, 'kanban.dispatch_in_gateway': True,
            'model.default': 'synthetic-model', 'model.provider': 'synthetic-provider'}
        self.requests, self.cli_calls, self.runs, self.cards = [], [], {}, {}
        self.post_delay, self.post_http, self.status_http = 0, 202, 200
        self.cli_timeout = False
        self.run_status = 'completed'
        self.tool_inventory = None
        self.app = web.Application()
        self.app.router.add_route('*', '/{path:.*}', self.http)
        self.server = web.AppRunner(self.app)
        await self.server.setup()
        site = web.TCPSite(self.server, '127.0.0.1', 0)
        await site.start()
        port = site._server.sockets[0].getsockname()[1]
        self.route = dict(base_url=f'http://127.0.0.1:{port}', api_key_env='SYNTHETIC_HERMES_KEY',
            profile='fixture', host='synthetic', hermes_home=str(self.root / 'native'),
            kanban_home=str(self.root / 'board'), workspace=str(self.root / 'workspace'),
            model='synthetic-model', provider='synthetic-provider', reasoning_effort='low',
            reservation_cost_usd=1, max_turns=1)
        guard = RUNTIME / 'gtd_felix/native_guard.py'
        context = guard.with_name('native_context.py')
        db = self.root / 'board' / 'kanban.db'
        db.touch()
        receipts = self.root / 'receipts'
        receipts.mkdir(mode=0o700)
        self.route['native_guard'] = {'python': sys.executable, 'path': str(guard),
            'sha256': hashlib.sha256(guard.read_bytes()).hexdigest(), 'parent_python': sys.executable,
            'profile': self.route['hermes_home'], 'kanban_home': self.route['kanban_home'],
            'context_path': str(context), 'context_sha256': hashlib.sha256(context.read_bytes()).hexdigest(),
            'board': 'default', 'kanban_db': str(db), 'hermes': sys.executable, 'receipts_dir': str(receipts)}
        flags = ['--parent-python', sys.executable, '--profile', self.route['hermes_home'],
            '--kanban-home', self.route['kanban_home'], '--board', 'default', '--kanban-db', str(db),
            '--hermes', sys.executable, '--receipts-dir', str(receipts)]
        self.native_config.update(hooks={
            'output_spill': {'enabled': True, 'max_chars': 10000},
            'pre_tool_call': [{'matcher': '.*', 'command': shlex.join([sys.executable, '-B', str(guard), *flags]),
                               'timeout': 20, 'fail_closed': True}],
            'pre_llm_call': [{'command': shlex.join([sys.executable, '-B', str(context), *flags]), 'timeout': 20}]},
            hooks_auto_accept=True)
        self.config = {'routes': {'fixture': self.route}, 'request_timeout_seconds': .15, 'cli_path': sys.executable}
        self.session = aiohttp.ClientSession()
        self.adapter = HermesAdapter(self.control, self.config, self.session, self.runner)

    async def asyncTearDown(self):
        await self.session.close()
        await self.server.cleanup()
        self.service.close()
        self.env.stop()
        self.temp.cleanup()

    def reserve(self, **updates):
        self.sequence += 1
        receipt = self.control.reserve('gtd-felix', 'reserve-' + str(self.sequence),
            dict(item_id=self.item['id'], expected_version=self.item['version'], capability='prepare_private',
                mandate_id=None, bot_id='fixture', purpose='Synthetic material', scope='Private test',
                max_cost_usd=2, max_runtime_seconds=60, max_retries=0, max_descendants=0, **updates))
        self.assertEqual(receipt['status'], 'reserved', receipt)
        return receipt['job_id']

    async def http(self, request):
        body = await request.json() if request.can_read_body else None
        self.requests.append((request.method, request.path, body, request.headers.get('Idempotency-Key')))
        self.assertEqual(request.headers.get('Authorization'), 'Bearer ' + os.environ['SYNTHETIC_HERMES_KEY'])
        if request.path == '/v1/capabilities':
            return web.json_response({'features': {k: True for k in ('run_submission', 'run_status', 'run_stop', 'run_steer')} | {
                'runs_idempotency': {'supported': True, 'durable': True, 'retention_seconds': 86400}}})
        if request.path == '/v1/toolsets':
            return web.json_response({'data': self.tool_inventory if self.tool_inventory is not None else [{'name': 'terminal', 'enabled': bool(self.native_config['platform_toolsets.api_server'])}]})
        if request.path == '/v1/runs' and request.method == 'POST':
            job_id = request.headers['Idempotency-Key']
            intent = self.adapter._get('hermes:intent:' + job_id)
            self.assertEqual(intent['body'], body, 'intention must precede effect')
            if self.post_http != 202:
                return web.json_response({}, status=self.post_http)
            if job_id in self.runs:
                self.assertEqual(self.runs[job_id]['body'], body)
            else:
                self.runs[job_id] = {'id': 'run_' + str(len(self.runs)), 'body': body}
            if self.post_delay:
                await asyncio.sleep(self.post_delay)
            return web.json_response({'run_id': self.runs[job_id]['id'], 'status': 'started'}, status=202)
        if request.path.endswith('/stop'):
            job = next(job for job in self.control.pending() if job.get('native', {}).get('id') == request.path.split('/')[-2])
            self.assertTrue(self.adapter._get('hermes:stop:' + job['id']))
            return web.json_response({'status': 'stopping'})
        if request.path.endswith('/steer'):
            return web.json_response({'accepted': True})
        if request.path.startswith('/v1/runs/'):
            return web.json_response({'run_id': request.path.split('/')[-1], 'status': self.run_status,
                'created_at': 100, 'updated_at': 102, 'output': 'Synthetic prepared output',
                'usage': {'input_tokens': 10, 'output_tokens': 5}}, status=self.status_http)
        return web.json_response({}, status=404)

    async def runner(self, argv, *, env, cwd, timeout):
        self.cli_calls.append(argv)
        self.assertEqual(env['HERMES_HOME'], self.route['hermes_home'])
        self.assertEqual(env['HERMES_KANBAN_HOME'], self.route['kanban_home'])
        self.assertNotEqual(env['HERMES_HOME'], env['HERMES_KANBAN_HOME'])
        self.assertNotIn('SYNTHETIC_HERMES_KEY', env)
        self.assertNotIn('fake-private-test-key', json.dumps(argv))
        if argv[1:4] == ['config', 'get', 'mcp_servers']:
            servers = self.native_config.get('mcp_servers', {name: {} for name in self.adapter.routes['fixture'].get('allowed_mcp_toolsets', {})})
            return {'returncode': 0, 'stdout': json.dumps(servers)}
        if argv[1:3] == ['config', 'get']:
            return {'returncode': 0, 'stdout': json.dumps(self.native_config.get(argv[3],
                {'include': ['gtd_read', 'gtd_command', 'gtd_dispatch'], 'prompts': False, 'resources': False}
                if argv[3] == 'mcp_servers.gtd.tools' else None))}
        if argv[1] == 'prompt-size':
            return {'returncode': 0, 'stdout': json.dumps({'tools': {'count': 3},
                'toolsets_breakdown': [{'toolset': 'mcp-gtd', 'tool_count': 3}]})}
        if argv[1:3] == ['mcp', 'test']:
            return {'returncode': 0, 'stdout': 'Tools discovered: 3\n\n    gtd_read      Read\n    gtd_command   Command\n    gtd_dispatch  Dispatch\n'}
        action = argv[2]
        if action == 'create':
            job_id = argv[argv.index('--idempotency-key') + 1]
            self.assertTrue(self.adapter._get('hermes:intent:' + job_id))
            self.assertNotIn('--initial-status', argv)
            self.assertEqual(argv[argv.index('--max-retries') + 1], '1')
            self.assertTrue(argv[argv.index('--workspace') + 1].startswith('dir:'))
            task = self.cards.setdefault(job_id, {'id': 't_' + str(len(self.cards)), 'title': argv[3],
                'body': argv[argv.index('--body') + 1], 'created_by': 'gtd:' + job_id,
                'assignee': 'fixture', 'status': 'done', 'workspace_kind': 'dir', 'workspace_path': cwd,
                'model_override': 'synthetic-model', 'provider_override': 'synthetic-provider',
                'result': 'Durable output', 'completed_at': 102})
            if self.cli_timeout:
                raise asyncio.TimeoutError()
            return {'returncode': 0, 'stdout': json.dumps(task)}
        if action == 'list':
            return {'returncode': 0, 'stdout': json.dumps(list(self.cards.values()))}
        if action == 'show':
            task = next((t for t in self.cards.values() if t['id'] == argv[3]), None)
            if not task:
                return {'returncode': 1, 'stdout': ''}
            run = task.get('_run', {'id': 1, 'profile': 'fixture', 'status': 'completed', 'outcome': 'completed',
                'worker_pid': None, 'started_at': 100, 'ended_at': 102})
            return {'returncode': 0, 'stdout': json.dumps({'task': task, 'runs': [run], 'children': []})}
        if action == 'reassign':
            task = next(t for t in self.cards.values() if t['id'] == argv[3])
            task['assignee'] = None
            task['status'] = 'ready'
            task['_run'] = {'id': 1, 'outcome': 'reclaimed', 'metadata': {'terminated': True},
                'worker_pid': None, 'started_at': 100, 'ended_at': 102}
            return {'returncode': 0, 'stdout': 'Reassigned'}
        return {'returncode': 1, 'stdout': ''}

    def restart(self):
        self.service.close()
        self.service = GTDService(self.root / 'data', executor_actors=['gtd-worker'])
        self.control = ExecutionControl(self.service, self.budget_config)
        self.adapter = HermesAdapter(self.control, self.config, self.session, self.runner)

    async def test_discover_and_submit_intent_first_stable_payload_idempotency(self):
        self.assertEqual((await self.adapter.discover('fixture'))['status'], 'ready')
        job_id = self.reserve()
        result = await self.adapter.submit(job_id, 'Prepare synthetic output')
        self.assertEqual(result['status'], 'submitted', result)
        intent = self.adapter._get('hermes:intent:' + job_id)
        self.assertNotIn('fake-private-test-key', json.dumps(intent))
        self.assertEqual(intent['body']['model'], 'synthetic-model')
        self.restart()
        self.assertEqual((await self.adapter.submit(job_id, 'Prepare synthetic output'))['status'], 'already_submitted')
        self.assertEqual((await self.adapter.submit(job_id, 'Different'))['error'], 'intent_conflict')
        self.assertEqual(len(self.runs), 1)
        self.assertEqual(len([r for r in self.requests if r[0] == 'POST']), 1)

    async def test_timeout_uncertain_reconcile_same_key_and_body_no_new_run(self):
        job_id = self.reserve()
        self.post_delay = .3
        result = await self.adapter.submit(job_id, 'Synthetic timeout')
        self.assertEqual(result['status'], 'uncertain')
        self.assertEqual(self.control.budget()['active'], 1)
        self.restart()
        self.post_delay = 0
        recovered = await self.adapter.reconcile(job_id)
        self.assertEqual(recovered['status'], 'observed', recovered)
        self.assertTrue(recovered['terminal'])
        self.assertEqual(len(self.runs), 1)
        bodies = [r[2] for r in self.requests if r[0] == 'POST']
        self.assertEqual(bodies[0], bodies[1])

    async def test_expired_or_rotated_uncertain_intent_never_replays(self):
        job_id = self.reserve()
        self.post_delay = .3
        self.assertEqual((await self.adapter.submit(job_id, 'Uncertain'))['status'], 'uncertain')
        posts = len([r for r in self.requests if r[0] == 'POST'])
        with patch('gtd_felix.hermes.time.time', return_value=time.time() + 86401):
            self.assertEqual((await self.adapter.reconcile(job_id))['error'], 'idempotency_retention_expired')
        with patch.dict(os.environ, {'SYNTHETIC_HERMES_KEY': 'new-key'}):
            self.assertEqual((await self.adapter.reconcile(job_id))['error'], 'api_key_rotated')
        self.assertEqual(posts, len([r for r in self.requests if r[0] == 'POST']))
        self.assertFalse(self.control.get_job(job_id)['terminal'])

    async def test_known_native_404_never_resubmits_or_frees_reservation(self):
        job_id = self.reserve()
        await self.adapter.submit(job_id, 'Known identity')
        self.status_http = 404
        self.assertEqual((await self.adapter.reconcile(job_id))['error'], 'native_status_http_404')
        self.assertEqual(len(self.runs), 1)
        self.assertFalse(self.control.get_job(job_id)['terminal'])
        self.assertEqual(self.control.budget()['active'], 1)

    async def test_observe_usage_unknown_usd_and_durable_original_before_terminal(self):
        job_id = self.reserve()
        await self.adapter.submit(job_id, 'Prepare')
        result = await self.adapter.poll(job_id)
        self.assertEqual(result['native_status'], 'completed')
        self.assertIsNone(result['observation']['cost_usd'])
        self.assertEqual(result['observation']['usage']['input_tokens'], 10)
        self.assertEqual(result['observation']['cost_telemetry'], 'unknown')
        self.assertEqual(self.control.get_job(job_id)['charged_cost_usd'], 2)
        blob = result['artifact']
        raw = (self.service.data_dir / blob['path']).read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(), blob['sha256'])
        self.restart()
        self.assertEqual(await self.adapter.poll(job_id), result)
        archive = self.root / 'snapshot.zip'
        self.service.export(archive)
        restored = GTDService.restore(archive, self.root / 'restored')
        try:
            self.assertEqual((restored.data_dir / blob['path']).read_bytes(), raw)
        finally:
            restored.close()

    async def test_stop_request_is_not_terminal_and_steer_is_not_replayed(self):
        job_id = self.reserve()
        self.run_status = 'running'
        await self.adapter.submit(job_id, 'Long synthetic work')
        self.assertEqual((await self.adapter.steer(job_id, 'Narrow scope'))['status'], 'accepted')
        self.assertEqual((await self.adapter.steer(job_id, 'Narrow scope'))['status'], 'accepted')
        self.assertEqual(len([r for r in self.requests if r[1].endswith('/steer')]), 1)
        self.assertEqual((await self.adapter.stop(job_id))['status'], 'stop_requested')
        self.assertFalse(self.control.get_job(job_id)['terminal'])
        self.assertEqual((await self.adapter.poll(job_id))['native_status'], 'running')
        self.run_status = 'cancelled'
        self.assertEqual((await self.adapter.poll(job_id))['native_status'], 'cancelled')
        self.assertTrue(self.control.get_job(job_id)['terminal'])

    async def test_native_limits_children_tools_and_reservation_fail_closed(self):
        for key, value in [('agent.max_turns', 20), ('agent.run_budget_seconds', 120),
                           ('agent.api_max_retries', 3), ('platform_toolsets.api_server', ['terminal'])]:
            job_id = self.reserve()
            original = self.native_config[key]
            self.native_config[key] = value
            self.assertEqual((await self.adapter.submit(job_id, 'Must not run'))['status'], 'rejected')
            self.native_config[key] = original
        job_id = self.reserve()
        self.adapter.routes['fixture']['reservation_cost_usd'] = 3
        self.assertEqual((await self.adapter.submit(job_id, 'Must not run'))['error'], 'route_reservation_insufficient')
        self.assertEqual(self.runs, {})
        self.assertIsNone(self.adapter._get('hermes:intent:' + job_id))

    async def test_revocation_or_human_change_before_network_prevents_dispatch(self):
        job_id = self.reserve()
        self.service.execute('felix', {'operation_id': 'correct', 'action': 'edit', 'item_id': self.item['id'],
            'expected_version': self.item['version'], 'fields': {'title': 'Corrected'}})
        self.assertEqual((await self.adapter.submit(job_id, 'Old work'))['error'], 'stale_item_version')
        self.assertEqual(self.requests, [])

    async def test_kanban_durable_idempotency_and_artifact_survive_restart(self):
        job_id = self.reserve()
        submitted = await self.adapter.submit(job_id, 'Durable synthetic output', durable=True)
        self.assertEqual(submitted['status'], 'submitted', submitted)
        self.restart()
        self.assertEqual((await self.adapter.submit(job_id, 'Durable synthetic output', durable=True))['status'], 'already_submitted')
        result = await self.adapter.poll(job_id)
        self.assertTrue(result['terminal'])
        self.assertEqual((self.service.data_dir / result['artifact']['path']).read_text(), 'Durable output')
        self.assertTrue((self.root / 'workspace').is_dir())
        self.assertEqual(len([a for a in self.cli_calls if a[1:3] == ['kanban', 'create']]), 1)

    async def test_kanban_timeout_recovered_from_inventory_never_create_again(self):
        job_id = self.reserve()
        self.cli_timeout = True
        self.assertEqual((await self.adapter.submit(job_id, 'Durable', durable=True))['status'], 'uncertain')
        self.restart()
        self.cli_timeout = False
        result = await self.adapter.reconcile(job_id)
        self.assertEqual(result['status'], 'observed', result)
        self.assertEqual(len(self.cards), 1)
        self.assertEqual(len([a for a in self.cli_calls if a[1:3] == ['kanban', 'create']]), 1)

    async def test_kanban_missing_inventory_does_not_recreate(self):
        job_id = self.reserve()
        self.cli_timeout = True
        await self.adapter.submit(job_id, 'Durable', durable=True)
        self.cards.clear()
        self.cli_timeout = False
        self.assertEqual((await self.adapter.reconcile(job_id))['status'], 'uncertain')
        self.assertEqual(len([a for a in self.cli_calls if a[1:3] == ['kanban', 'create']]), 1)

    async def test_kanban_blocked_is_not_terminal_stop_checks_termination(self):
        job_id = self.reserve()
        await self.adapter.submit(job_id, 'Durable running', durable=True)
        card = self.cards[job_id]
        card['status'] = 'blocked'
        card['_run'] = {'id': 1, 'worker_pid': 123, 'started_at': 100, 'ended_at': None}
        result = await self.adapter.poll(job_id)
        self.assertEqual(result['native_status'], 'running')
        self.assertFalse(result['terminal'])
        self.assertEqual((await self.adapter.steer(job_id, 'Change guidance'))['status'], 'unsupported')
        self.assertEqual((await self.adapter.stop(job_id))['status'], 'stop_requested')
        result = await self.adapter.poll(job_id)
        self.assertEqual(result['native_status'], 'cancelled')
        self.assertFalse(any('pkill' in a for a in self.cli_calls))

    async def stopped_blocked_task(self, change=None):
        job_id = self.reserve()
        await self.adapter.submit(job_id, 'Durable blocked', durable=True)
        # Exact public show keys from the closed diagnostic, anonymized values.
        created = self.cards[job_id]
        task = {key: None for key in ('id','title','body','assignee','status','priority','tenant',
            'workspace_kind','workspace_path','branch_name','project_id','created_by','created_at',
            'started_at','completed_at','result','skills','max_retries','model_override','provider_override',
            'session_id','workflow_template_id','current_step_key','completion_contract','last_failure_error')}
        task.update(id=created['id'],title='Synthetic task',body='Synthetic context',assignee='fixture',
            status='blocked',priority=0,workspace_kind='dir',workspace_path=str(self.root/'workspace'),
            created_by='gtd:'+job_id,created_at=99,started_at=100,skills=[],max_retries=1,
            model_override='synthetic-model',provider_override='synthetic-provider',completion_contract='local-only')
        runs = [{'id':2,'profile':'fixture','step_key':None,'status':'blocked','outcome':'blocked',
                 'summary':'Synthetic capability block','error':None,'metadata':None,
                 'worker_pid':None,'started_at':100,'ended_at':113}]
        events = [{'kind':'blocked','payload':{'kind':'capability','reason':'Synthetic block',
            'recurrences':1,'source_status':'ready'},'created_at':113,'run_id':2}]
        original_runner = self.runner
        async def runner(argv, **kwargs):
            if len(argv)>2 and argv[1:3]==['kanban','reassign']:
                self.cli_calls.append(argv)
                if change == 'stop_uncertain': raise asyncio.TimeoutError()
                self.assertEqual(argv[3],task['id'])
                self.assertIn('--reclaim',argv)
                task['assignee']=None  # Native reclaim=False; closed blocked run unchanged.
                events.append({'kind':'assigned','payload':{'assignee':None},'created_at':int(time.time()),'run_id':None})
                return {'returncode':0,'stdout':'Reassigned'}
            if len(argv)>2 and argv[1:3]==['kanban','show']:
                self.cli_calls.append(argv)
                return {'returncode':0,'stdout':json.dumps({'task':task,'latest_summary':'Synthetic capability block','parents':[],
                    'children':[],'comments':[],'events':events,'runs':runs})}
            return await original_runner(argv,**kwargs)
        self.adapter.runner=runner
        waiting=await self.adapter.poll(job_id)
        self.assertEqual(waiting['native_status'],'waiting')
        if change != 'foreign_stop': await self.adapter.stop(job_id)
        else: task['assignee']=None
        if change=='missing_run': runs.clear()
        elif change=='active_pid': runs[0]['worker_pid']=123
        elif change=='open_run': runs[0]['ended_at']=None
        elif change=='extra_open_run': runs.append({**runs[0],'id':1,'ended_at':None})
        elif change=='claim': events.insert(-1,{'kind':'claimed','payload':{'lock':'new'},'created_at':114,'run_id':3})
        elif change=='missing_claim_proof': events.pop(0)
        elif change=='missing_assignment': events.pop()
        elif change=='old_assignment': events[-1]['created_at']=1
        elif change=='new_assignment': task['assignee']='another-worker'
        elif change=='wrong_task': task['id']='other-task'
        elif change=='wrong_run': events[0]['run_id']=99
        elif change=='foreign_receipt':
            record=self.adapter._get('hermes:stop:'+job_id)
            record['receipt']['job_id']='other-job'
            with self.service.store.transaction(): self.adapter._set('hermes:stop:'+job_id,record)
        self.restart()
        self.adapter.runner=runner
        return job_id, await self.adapter.poll(job_id)

    async def test_stop_closed_blocked_readback_is_cancelled_without_reclaimed_run(self):
        job_id,result=await self.stopped_blocked_task()
        self.assertEqual(result['native_status'],'cancelled',result)
        self.assertTrue(result['terminal'])
        self.assertEqual(result['observation']['runtime_seconds'],13)
        stored=self.adapter._get(result['observation']['evidence_reference'])
        self.assertEqual(stored['payload']['runs'][0]['outcome'],'blocked')
        self.assertEqual(stored['payload']['task']['status'],'blocked')
        self.assertEqual(self.control.get_job(job_id)['observed_runtime_seconds'],13)
        observed_count=len(self.control.get_job(job_id)['observations'])
        self.assertEqual(await self.adapter.poll(job_id),result)
        self.assertEqual(len(self.control.get_job(job_id)['observations']),observed_count)

    async def test_stop_closed_blocked_rejects_incomplete_or_foreign_evidence(self):
        for change in ('missing_run','active_pid','open_run','extra_open_run','claim','missing_claim_proof','missing_assignment','old_assignment','new_assignment',
                       'stop_uncertain','foreign_stop','foreign_receipt','wrong_task','wrong_run'):
            with self.subTest(change=change):
                # Each transport scenario owns an independent service/budget.
                case=HermesTest();await case.asyncSetUp()
                try:
                    _,result=await case.stopped_blocked_task(change)
                    self.assertFalse(result.get('terminal',False),result)
                finally: await case.asyncTearDown()

    async def test_kanban_requires_separate_home_and_native_dispatch_limits(self):
        for key, value in [('kanban.auto_decompose', True), ('platform_toolsets.cli', ['delegate_task']), ('kanban.max_spawn', 2)]:
            job_id = self.reserve()
            old = self.native_config[key]
            self.native_config[key] = value
            self.assertEqual((await self.adapter.submit(job_id, 'No uncontrolled work', durable=True))['status'], 'rejected')
            self.native_config[key] = old
        self.assertEqual(self.cards, {})

    async def test_native_kanban_implicit_creation_tools_must_be_disabled(self):
        job_id = self.reserve()
        self.native_config['hooks'] = {}
        result = await self.adapter.submit(job_id, 'Native worker could create children', durable=True)
        self.assertEqual(result['error'], 'native_route_not_ready')
        self.assertEqual(self.cards, {})

    async def test_change_during_discovery_is_revalidated_before_effect(self):
        job_id = self.reserve()
        discover = self.adapter.discover
        async def corrected(bot_id):
            result = await discover(bot_id)
            self.service.execute('felix', {'operation_id': 'during-discovery', 'action': 'edit',
                'item_id': self.item['id'], 'expected_version': self.item['version'], 'fields': {'title': 'New human meaning'}})
            return result
        self.adapter.discover = corrected
        result = await self.adapter.submit(job_id, 'Old basis')
        self.assertEqual(result['error'], 'stale_item_version')
        self.assertFalse(any(r[0] == 'POST' for r in self.requests))
        self.assertIsNone(self.adapter._get('hermes:intent:' + job_id))

    def _family_request(self, purpose, **changes):
        request = dict(item_id=self.item['id'], expected_version=self.item['version'], capability='prepare_private',
            mandate_id=None, bot_id='fixture', purpose=purpose, scope='Synthetic family', max_cost_usd=4,
            max_runtime_seconds=120, max_retries=0, max_descendants=1)
        return dict(request, **changes)

    def _local_native_active(self):
        return self.service.store.db.execute(
            "SELECT COUNT(*) FROM runs WHERE state IN ('dispatching','running','stop_requested','uncertain')").fetchone()[0]

    def _provider_creates(self):
        return [r for r in self.requests if r[0] == 'POST' and r[1] == '/v1/runs']

    async def test_stop_registered_family_exact_ids(self):
        # Single global native slot: parent and child execute sequentially, and
        # STOP addresses each admitted identity exactly once.
        root = self.control.reserve('gtd-felix', 'parent', self._family_request('Parent'))['job_id']
        child = self.control.reserve('gtd-felix', 'child', self._family_request(
            'Child', parent_job_id=root, max_cost_usd=2, max_runtime_seconds=60, max_descendants=0))['job_id']
        self.run_status = 'running'
        self.assertEqual((await self.adapter.submit(root, 'Parent'))['status'], 'submitted')
        blocked = await self.adapter.submit(child, 'Child')
        self.assertEqual(blocked['status'], 'uncertain', blocked)
        self.assertEqual(blocked['error'], 'native_slot_busy')
        self.assertEqual(len(self._provider_creates()), 1)
        # STOP reaches exactly the admitted identities: the running parent
        # gets a remote stop; the reserved child only records the local stop
        # flag without any remote call. Neither becomes terminal, and a
        # stopped slot stays occupied until terminality is observed.
        stopped = await self.adapter.stop(root)
        self.assertEqual(len(stopped['children']), 1)
        parent_native = self.control.get_job(root)['native']['id']
        self.assertEqual(
            {r[1].split('/')[-2] for r in self.requests if r[1].endswith('/stop')}, {parent_native})
        self.assertTrue(all(self.control.get_job(identity)['stop_requested'] for identity in (root, child)))
        self.assertFalse(any(self.control.get_job(identity)['terminal'] for identity in (root, child)))
        self.assertEqual(self._local_native_active(), 1)
        again = await self.adapter.submit(child, 'Child')
        self.assertEqual(again['status'], 'uncertain', again)
        self.assertEqual(len(self._provider_creates()), 1)

    async def test_child_executes_after_parent_terminal_with_own_assignment(self):
        # Sequential family execution under one slot: while the parent runs,
        # the child creates nothing remotely; once the parent is terminal, a
        # reconcile dispatches the child with its own assignment (60 s / cost
        # 2) without ever exceeding one local execution.
        root = self.control.reserve('gtd-felix', 'parent', self._family_request('Parent'))['job_id']
        child = self.control.reserve('gtd-felix', 'child', self._family_request(
            'Child', parent_job_id=root, max_cost_usd=2, max_runtime_seconds=60, max_descendants=0))['job_id']
        self.run_status = 'running'
        self.assertEqual((await self.adapter.submit(root, 'Parent'))['status'], 'submitted')
        waiting = await self.adapter.submit(child, 'Child')
        self.assertEqual(waiting['status'], 'uncertain', waiting)
        self.assertEqual(waiting['error'], 'native_slot_busy')
        self.assertEqual(len(self._provider_creates()), 1)
        terminal = {'native_identity': self.control.get_job(root)['native'], 'native_status': 'completed',
            'terminal': True, 'runtime_seconds': 5, 'cost_usd': None, 'evidence_reference': 'fixture://done'}
        self.assertEqual(self.control.observe(root, terminal)['status'], 'recorded')
        self.assertEqual(self._local_native_active(), 0)
        retried = await self.adapter.reconcile(child)
        self.assertEqual(retried['native_status'], 'running', retried)
        self.assertEqual(len(self._provider_creates()), 2)
        self.assertEqual(len(self.runs), 2)
        self.assertEqual(self._local_native_active(), 1)
        child_limits = self.control.validate(child, 'prepare_private')
        self.assertTrue(child_limits['allowed'], child_limits)
        self.assertEqual(child_limits['limits']['max_runtime_seconds'], 60)
        self.assertEqual(child_limits['limits']['max_cost_usd'], 2)

    async def test_second_dispatch_holds_slot_without_remote_create(self):
        root = self.control.reserve('gtd-felix', 'parent', self._family_request('Parent'))['job_id']
        child = self.control.reserve('gtd-felix', 'child', self._family_request(
            'Child', parent_job_id=root, max_cost_usd=2, max_runtime_seconds=60, max_descendants=0))['job_id']
        self.run_status = 'running'
        self.assertEqual((await self.adapter.submit(root, 'Parent'))['status'], 'submitted')
        second = await self.adapter.submit(child, 'Child')
        self.assertEqual(second['status'], 'uncertain', second)
        self.assertEqual(second['error'], 'native_slot_busy')
        # No second remote creation and no leaked adapter-side identity.
        self.assertEqual(len(self._provider_creates()), 1)
        self.assertEqual(len(self.runs), 1)
        self.assertEqual(self._local_native_active(), 1)
        self.assertEqual(self.control._run_row(child)['state'], 'reserved')
        self.assertIsNone(self.control.get_job(child)['native'])
        self.assertIsNone((self.adapter._get('hermes:state:' + child) or {}).get('native_id'))

    async def test_concurrent_dispatch_creates_single_remote_run(self):
        root = self.control.reserve('gtd-felix', 'parent', self._family_request('Parent'))['job_id']
        derived = self.service.execute('felix', dict(operation_id='derive-second', action='derive',
            item_id=self.item['id'], expected_version=self.item['version'], fields={'kind': 'action',
            'title': 'Second', 'capability': 'prepare_private'}))['item']
        second = self.control.reserve('gtd-felix', 'second', self._family_request(
            'Second', item_id=derived['id'], expected_version=derived['version']))['job_id']
        self.run_status = 'running'
        first, other = await asyncio.gather(
            self.adapter.submit(root, 'Parent'), self.adapter.submit(second, 'Second'))
        self.assertEqual({first['status'], other['status']}, {'submitted', 'uncertain'})
        self.assertEqual(len(self._provider_creates()), 1)
        self.assertEqual(len(self.runs), 1)
        self.assertEqual(self._local_native_active(), 1)

    async def test_claim_survives_restart_between_claim_and_post(self):
        root = self.control.reserve('gtd-felix', 'parent', self._family_request('Parent'))['job_id']
        self.run_status = 'running'
        real_http = self.adapter._http
        async def failing_post(route, method, path, body=None, idempotency_key=None):
            if method == 'POST' and path == '/v1/runs':
                raise asyncio.TimeoutError()
            return await real_http(route, method, path, body, idempotency_key)
        self.adapter._http = failing_post
        try:
            lost = await self.adapter.submit(root, 'Parent')
        finally:
            self.adapter._http = real_http
        self.assertEqual(lost['status'], 'uncertain', lost)
        # The claim is held durably despite the lost receipt: no remote run,
        # slot still taken, intent persisted for reconciliation.
        self.assertEqual(len(self._provider_creates()), 0)
        self.assertEqual(self.control._run_row(root)['state'], 'dispatching')
        self.assertEqual(self._local_native_active(), 1)
        self.restart()
        reconciled = await self.adapter.reconcile(root)
        self.assertEqual(reconciled['status'], 'observed', reconciled)
        self.assertEqual(len(self._provider_creates()), 1)
        self.assertEqual(len(self.runs), 1)
        self.assertIsNotNone(self.control.get_job(root)['native'])

    async def test_restart_between_post_and_receipt_reuses_idempotency_key(self):
        root = self.control.reserve('gtd-felix', 'parent', self._family_request('Parent'))['job_id']
        self.run_status = 'running'
        self.assertEqual((await self.adapter.submit(root, 'Parent'))['status'], 'submitted')
        self.assertEqual(len(self.runs), 1)
        # Lose only the adapter-side receipt; the intent and the provider run
        # (keyed by job_id) survive. Reconciling must not create a second run.
        with self.service.store.transaction() as db:
            db.execute("DELETE FROM metadata WHERE key=?", ('hermes:state:' + root,))
        recovered = await self.adapter.reconcile(root)
        self.assertEqual(recovered['status'], 'observed', recovered)
        # The retry re-POSTs under the same Idempotency-Key; the provider
        # answers with the single existing run instead of creating another.
        self.assertEqual(len(self.runs), 1)
        self.assertEqual(len(self._provider_creates()), 2)
        self.assertIsNotNone(self.control.get_job(root)['native'])

    async def _durable_pair(self):
        # Two durable-capable reservations on distinct items (one open cycle
        # per item): the first dispatches, the second waits without sending.
        root = self.reserve()
        derived = self.service.execute('felix', dict(operation_id='derive-durable-second', action='derive',
            item_id=self.item['id'], expected_version=self.item['version'], fields={'kind': 'action',
            'title': 'Durable second', 'capability': 'prepare_private'}))['item']
        req = dict(item_id=derived['id'], expected_version=derived['version'], capability='prepare_private',
            mandate_id=None, bot_id='fixture', purpose='Second', scope='Test',
            max_cost_usd=2, max_runtime_seconds=60, max_retries=0, max_descendants=0)
        child = self.control.reserve('gtd-felix', 'second', req)['job_id']
        return root, child

    async def test_durable_never_sent_recovers_after_slot_frees(self):
        root, child = await self._durable_pair()
        self.assertEqual((await self.adapter.submit(root, 'First', durable=True))['status'], 'submitted')
        second = await self.adapter.submit(child, 'Second', durable=True)
        self.assertEqual(second['status'], 'uncertain', second)
        self.assertEqual(second['error'], 'native_slot_busy')
        self.assertEqual(len(self.cards), 1)
        done = self.control.observe(root, dict(
            native_identity=self.control.get_job(root)['native'], native_status='completed',
            terminal=True, runtime_seconds=5, cost_usd=None, evidence_reference='fixture://done'))
        self.assertEqual(done['status'], 'recorded', done)
        # The adapter durably knew nothing was ever sent, so reconciliation
        # performs the first send now instead of searching for a receipt.
        retried = await self.adapter.reconcile(child)
        self.assertEqual(retried['native_status'], 'completed', retried)
        self.assertTrue(retried['terminal'], retried)
        self.assertEqual(len(self.cards), 2)
        self.assertEqual(self._local_native_active(), 0)
        self.assertEqual(self.control.get_job(child)['native']['id'], 't_1')

    async def test_durable_never_sent_survives_restart_before_first_send(self):
        root, child = await self._durable_pair()
        self.assertEqual((await self.adapter.submit(root, 'First', durable=True))['status'], 'submitted')
        waiting = await self.adapter.submit(child, 'Second', durable=True)
        self.assertEqual(waiting['status'], 'uncertain', waiting)
        done = self.control.observe(root, dict(
            native_identity=self.control.get_job(root)['native'], native_status='completed',
            terminal=True, runtime_seconds=5, cost_usd=None, evidence_reference='fixture://done'))
        self.assertEqual(done['status'], 'recorded', done)
        self.restart()
        retried = await self.adapter.reconcile(child)
        self.assertEqual(retried['native_status'], 'completed', retried)
        self.assertEqual(len(self.cards), 2)

    async def test_durable_never_sent_stop_blocks_first_send(self):
        root, child = await self._durable_pair()
        self.assertEqual((await self.adapter.submit(root, 'First', durable=True))['status'], 'submitted')
        waiting = await self.adapter.submit(child, 'Second', durable=True)
        self.assertEqual(waiting['status'], 'uncertain', waiting)
        stopped = self.control.request_stop('felix', 'stop-never-sent', child)
        self.assertEqual(stopped['status'], 'stop_requested', stopped)
        done = self.control.observe(root, dict(
            native_identity=self.control.get_job(root)['native'], native_status='completed',
            terminal=True, runtime_seconds=5, cost_usd=None, evidence_reference='fixture://done'))
        self.assertEqual(done['status'], 'recorded', done)
        # STOP wins over the pending first send: no remote creation.
        held = await self.adapter.reconcile(child)
        self.assertEqual(held['status'], 'uncertain', held)
        self.assertEqual(len(self.cards), 1)
        self.assertTrue(self.control.get_job(child)['stop_requested'])
        self.assertFalse(self.control.get_job(child)['terminal'])

    async def test_durable_uncertain_send_never_recreates_blindly(self):
        # The claim succeeded and the CLI failed: the provider may or may not
        # hold the card, so reconciliation searches the inventory instead of
        # creating again. With nothing there it stays uncertain, no new call.
        root = self.reserve()
        real_cli = self.adapter._cli
        async def failing_create(route, args, json_output=True, text_output=False):
            if list(args[:2]) == ['kanban', 'create']:
                raise asyncio.TimeoutError()
            return await real_cli(route, args, json_output=json_output, text_output=text_output)
        self.adapter._cli = failing_create
        try:
            lost = await self.adapter.submit(root, 'First', durable=True)
        finally:
            self.adapter._cli = real_cli
        self.assertEqual(lost['status'], 'uncertain', lost)
        self.assertEqual(self.cards, {})
        creates = len([c for c in self.cli_calls if len(c) > 2 and c[2] == 'create'])
        held = await self.adapter.reconcile(root)
        self.assertEqual(held['status'], 'uncertain', held)
        self.assertEqual(held['error'], 'kanban_receipt_not_uniquely_recovered')
        self.assertEqual(len([c for c in self.cli_calls if len(c) > 2 and c[2] == 'create']), creates)
        self.assertEqual(self.cards, {})

    async def test_uncertain_execution_keeps_slot_until_reconciled(self):
        root = self.control.reserve('gtd-felix', 'parent', self._family_request('Parent'))['job_id']
        child = self.control.reserve('gtd-felix', 'child', self._family_request(
            'Child', parent_job_id=root, max_cost_usd=2, max_runtime_seconds=60, max_descendants=0))['job_id']
        self.run_status = 'running'
        self.assertEqual((await self.adapter.submit(root, 'Parent'))['status'], 'submitted')
        self.status_http = 500
        try:
            self.assertEqual((await self.adapter.poll(root))['status'], 'uncertain')
        finally:
            self.status_http = 200
        # Uncertainty is not detention proof: the slot stays occupied and the
        # second dispatch still creates nothing remotely.
        self.assertEqual(self._local_native_active(), 1)
        waiting = await self.adapter.submit(child, 'Child')
        self.assertEqual(waiting['status'], 'uncertain', waiting)
        self.assertEqual(len(self._provider_creates()), 1)

    async def test_same_kanban_home_is_rejected_without_effect(self):
        job_id = self.reserve()
        self.adapter.routes['fixture']['kanban_home'] = self.route['hermes_home']
        self.assertEqual((await self.adapter.submit(job_id, 'Not isolated', durable=True))['error'], 'separate_kanban_home_required')
        self.assertEqual(self.cli_calls, [])
        self.assertEqual(self.requests, [])

    async def test_mcp_requires_direct_schemas_without_tool_search_bridge(self):
        self.adapter.routes['fixture']['allowed_mcp_toolsets'] = {'gtd': ['gtd_read', 'gtd_command', 'gtd_dispatch']}
        self.native_config['platform_toolsets.api_server'] = ['gtd']
        self.tool_inventory = [{'name': 'terminal', 'enabled': False, 'configured': True, 'tools': []}]
        for value in ('auto', 'on', None):
            self.native_config['tools.tool_search.enabled'] = value
            result = await self.adapter.discover('fixture')
            self.assertEqual(result['status'], 'blocked', result)
            self.assertIn('mcp_direct_schemas_required', result['errors'])
        self.native_config['tools.tool_search.enabled'] = 'off'
        self.assertEqual((await self.adapter.discover('fixture'))['status'], 'ready')

    async def test_exact_gtd_mcp_tool_inventory_allowed_but_escapes_rejected(self):
        self.adapter.routes['fixture']['allowed_mcp_toolsets'] = {'gtd': ['gtd_read', 'gtd_command', 'gtd_dispatch']}
        self.native_config['platform_toolsets.api_server'] = ['gtd']
        self.tool_inventory = [{'name': 'gtd', 'enabled': True, 'configured': True, 'tools': ['mcp__gtd__gtd_read', 'mcp__gtd__gtd_command', 'mcp__gtd__gtd_dispatch']}]
        self.assertEqual((await self.adapter.discover('fixture'))['status'], 'ready')
        original = list(self.tool_inventory[0]['tools'])
        for invalid in (original[:-1], original + ['mcp__gtd__extra'],
                        ['mcp__other__gtd_read', *original[1:]],
                        ['gtd_read', 'gtd_command', 'gtd_dispatch']):
            self.tool_inventory[0]['tools'] = invalid
            self.assertIn('mcp_tool_inventory_mismatch', (await self.adapter.discover('fixture'))['errors'])
        self.tool_inventory[0]['tools'] = original
        self.tool_inventory[0]['tools'].append('execute_shell')
        blocked = await self.adapter.discover('fixture')
        self.assertIn('mcp_tool_inventory_mismatch', blocked['errors'])
        self.tool_inventory[0]['tools'].pop()
        self.tool_inventory.append({'name': 'delegation', 'enabled': True, 'configured': True, 'tools': ['delegate_task']})
        self.assertIn('uncontrolled_native_tools', (await self.adapter.discover('fixture'))['errors'])
        self.tool_inventory[-1] = {'name': 'mcp-ambient', 'enabled': False, 'configured': True, 'tools': ['arbitrary_effect']}
        self.assertIn('uncontrolled_native_tools', (await self.adapter.discover('fixture'))['errors'])

    async def test_public_cli_complements_absent_http_mcp_and_rejects_inexact_evidence(self):
        route = self.adapter.routes['fixture']
        route['allowed_mcp_toolsets'] = {'gtd': ['gtd_read', 'gtd_command', 'gtd_dispatch']}
        self.native_config['platform_toolsets.api_server'] = ['gtd']
        self.tool_inventory = [{'name': 'terminal', 'enabled': False, 'configured': True, 'tools': []}]
        self.assertEqual((await self.adapter.discover('fixture'))['status'], 'ready')
        original_runner = self.adapter.runner
        for bad in ('Tools discovered: 3\n    gtd_read Read\n',
                    'Tools discovered: 3\n    gtd_read Read\n    gtd_command Command\n    foreign_dispatch Dispatch\n',
                    'Tools discovered: 4\n    gtd_read Read\n    gtd_command Command\n    gtd_dispatch Dispatch\n    shell Shell\n',
                    'Connection failed'):
            async def changed(argv, **kwargs):
                if argv[1:3] == ['mcp', 'test']:
                    return {'returncode': 0, 'stdout': bad}
                return await original_runner(argv, **kwargs)
            self.adapter.runner = changed
            self.assertEqual((await self.adapter.discover('fixture'))['status'], 'blocked')
        async def wrong_effective(argv, **kwargs):
            if argv[1] == 'prompt-size':
                return {'returncode': 0, 'stdout': json.dumps({'tools': {'count': 0}, 'toolsets_breakdown': []})}
            return await original_runner(argv, **kwargs)
        self.adapter.runner = wrong_effective
        self.assertEqual((await self.adapter.discover('fixture'))['status'], 'ready')
        self.assertFalse(any(argv[1] == 'prompt-size' for argv in self.cli_calls))
        self.adapter.runner = original_runner
        self.native_config['mcp_servers.gtd.tools'] = {'include': ['gtd_read'], 'prompts': False, 'resources': False}
        self.assertEqual((await self.adapter.discover('fixture'))['status'], 'blocked')

    async def test_mcp_requires_execution_guidance_explicitly_disabled(self):
        self.adapter.routes['fixture']['allowed_mcp_toolsets'] = {'gtd': ['gtd_read', 'gtd_command', 'gtd_dispatch']}
        self.native_config['platform_toolsets.api_server'] = ['gtd']
        self.tool_inventory = []
        for value in (None, 'auto', True):
            if value is None:
                self.native_config.pop('agent.execution_guidance', None)
            else:
                self.native_config['agent.execution_guidance'] = value
            result = await self.adapter.discover('fixture')
            self.assertEqual(result['status'], 'blocked', result)
            self.assertIn('mcp_execution_guidance_must_be_disabled', result['errors'])
        self.native_config['agent.execution_guidance'] = False
        self.assertEqual((await self.adapter.discover('fixture'))['status'], 'ready')
        self.assertFalse(any(method == 'POST' for method, *_ in self.requests))

    async def test_total_enabled_mcp_servers_rejected_without_exposing_credentials(self):
        self.tool_inventory = []
        self.adapter.routes['fixture']['allowed_mcp_toolsets'] = {'gtd': ['gtd_read', 'gtd_command', 'gtd_dispatch']}
        self.native_config['platform_toolsets.api_server'] = ['gtd']
        self.native_config['mcp_servers'] = {'gtd': {}, 'foreign': {'env': {'SECRET': 'synthetic-secret-canary'}}}
        result = await self.adapter.discover('fixture')
        self.assertEqual(result['status'], 'blocked')
        self.assertIn('mcp_enabled_servers_mismatch', result['errors'])
        self.assertNotIn('synthetic-secret-canary', json.dumps(result))
        self.assertNotIn('synthetic-secret-canary', json.dumps(self.adapter._get('hermes:discovery:fixture')))
        self.native_config['mcp_servers']['foreign']['enabled'] = False
        self.assertEqual((await self.adapter.discover('fixture'))['status'], 'ready')
        original = self.adapter.runner
        async def broken(argv, **kwargs):
            if argv[1:4] == ['config', 'get', 'mcp_servers']:
                return {'returncode': 1, 'stdout': 'synthetic-secret-canary'}
            return await original(argv, **kwargs)
        self.adapter.runner = broken
        result = await self.adapter.discover('fixture')
        self.assertEqual(result['errors'], ['native_cli_failed'])
        self.assertNotIn('synthetic-secret-canary', json.dumps(result))

    async def test_discovery_without_guard_is_blocked_and_cannot_dispatch(self):
        self.native_config['hooks'] = {}
        discovery = await self.adapter.discover('fixture')
        self.assertFalse(discovery['native_limits']['guard_verified'])
        self.assertEqual(discovery['status'], 'blocked')
        self.assertIn('native_guard_unverified', discovery['errors'])
        result = await self.adapter.submit(self.reserve(), 'No verified guard')
        self.assertEqual(result['status'], 'rejected')
        self.assertTrue(result['no_effect'])
        self.assertFalse(any(method == 'POST' for method, *_ in self.requests))

    async def test_api_requires_exact_global_guard_before_any_native_effect(self):
        self.native_config['hooks']['pre_tool_call'][0]['matcher'] = 'kanban_.*'
        result = await self.adapter.submit(self.reserve(), 'API must be guarded')
        self.assertEqual(result['status'], 'rejected')
        self.assertTrue(result['no_effect'])
        self.assertFalse(any(method == 'POST' for method, *_ in self.requests))

    async def test_mcp_environment_passes_only_explicit_variable_bindings(self):
        route = self.adapter.routes['fixture']
        route['mcp_environment'] = {'GTD_API_TOKEN': 'TEST_GTD_PRIVATE_TOKEN'}
        with patch.dict(os.environ, {'TEST_GTD_PRIVATE_TOKEN': 'synthetic-secret', 'UNRELATED_SECRET': 'not-passed'}):
            env = self.adapter._environment(route)
            self.assertEqual(env['GTD_API_TOKEN'], 'synthetic-secret')
            self.assertNotIn('TEST_GTD_PRIVATE_TOKEN', env)
            self.assertNotIn('UNRELATED_SECRET', env)
            route['mcp_environment'] = {'PYTHONPATH': 'TEST_GTD_PRIVATE_TOKEN'}
            with self.assertRaisesRegex(ValueError, 'invalid_mcp_environment'):
                self.adapter._environment(route)

    async def test_executor_stop_remains_available_after_mandate_revocation(self):
        self.item = self.service.execute('felix', dict(operation_id='clarify-worker', action='clarify',
            item_id=self.item['id'], expected_version=self.item['version'],
            fields={'kind': 'action', 'commitment': 'committed'}))['item']
        grant = self.service.execute('felix', dict(operation_id='grant-worker', action='grant_mandate',
            item_id=self.item['id'], expected_version=self.item['version'], fields={
                'scope_item_id': self.item['id'], 'actors': ['gtd-worker'],
                'capabilities': ['prepare_private'], 'completion_criteria': 'Synthetic output'}))
        self.assertEqual(grant['status'], 'applied', grant)
        self.item = grant['item']
        bot = dict(id='fixture', actor='gtd-worker', state='available', source_urn='urn:test:fixture',
            host='synthetic', profile='fixture', capabilities=['prepare_private'],
            item_id=self.item['id'], mandate_id=grant['mandate']['id'], probe_evidence='synthetic://probe')
        self.assertEqual(self.control.register_bot('felix', 'worker-bot', bot)['status'], 'applied')
        receipt = self.control.reserve('gtd-felix', 'worker-reserve', dict(item_id=self.item['id'],
            expected_version=self.item['version'], capability='prepare_private', mandate_id=grant['mandate']['id'],
            bot_id='fixture', purpose='Synthetic material', scope='Private test', max_cost_usd=2,
            max_runtime_seconds=60, max_retries=0, max_descendants=0))
        self.assertEqual(receipt['status'], 'reserved', receipt)
        job_id = receipt['job_id']
        self.assertEqual((await self.adapter.submit(job_id, 'Worker preparation'))['status'], 'submitted')
        revoked = self.service.execute('felix', dict(operation_id='revoke-worker', action='revoke_mandate',
            item_id=self.item['id'], expected_version=self.item['version'],
            fields={'mandate_id': grant['mandate']['id']}))
        self.assertEqual(revoked['status'], 'applied', revoked)
        self.assertFalse(self.control.validate(job_id, 'prepare_private')['allowed'])
        stopped = await self.adapter.stop(job_id)
        self.assertNotEqual(stopped.get('error'), 'stop_not_authorized', stopped)
        self.assertTrue(self.control.get_job(job_id)['stop_requested'])
        self.assertTrue(any(method == 'POST' and path.endswith('/stop') for method, path, *_ in self.requests))

    async def test_exact_fail_closed_hook_and_hash_required(self):
        job_id = self.reserve()
        entry = self.native_config['hooks']['pre_tool_call'][0]
        entry['fail_closed'] = False
        self.assertEqual((await self.adapter.submit(job_id, 'Unsafe hook', durable=True))['error'], 'native_route_not_ready')
        entry['fail_closed'] = True
        entry['command'] += ' --extra'
        discovery = await self.adapter.discover('fixture')
        self.assertFalse(discovery['native_limits']['guard_verified'])
        self.assertNotIn('--extra', json.dumps(discovery))
        entry['command'] = entry['command'].removesuffix(' --extra')
        self.adapter.routes['fixture']['native_guard']['sha256'] = '0' * 64
        self.assertFalse((await self.adapter.discover('fixture'))['native_limits']['guard_verified'])

    async def test_context_guard_discovery_and_admission_exact_contract(self):
        discovery = await self.adapter.discover('fixture')
        self.assertTrue(discovery['native_limits']['guard_verified'])
        job_id = self.reserve()
        submitted = await self.adapter.submit(job_id, 'Exact hooks', durable=True)
        self.assertEqual(submitted['status'], 'submitted', submitted)

    async def test_exact_board_query_and_historical_route_poll(self):
        original_runner = self.adapter.runner
        observed = []
        async def capture(argv, **kwargs):
            if argv[1:3] == ['kanban', 'show']:
                observed.append(kwargs['env'])
            return await original_runner(argv, **kwargs)
        self.adapter.runner = capture
        job_id = self.reserve()
        await self.adapter.submit(job_id, 'Board pinned', durable=True)
        await self.adapter.poll(job_id)
        self.assertEqual(observed[-1]['HERMES_KANBAN_BOARD'], 'default')
        self.assertEqual(observed[-1]['HERMES_KANBAN_DB'], self.route['native_guard']['kanban_db'])
        # A route admitted by the previous runtime retains its exact old shape.
        guard = self.adapter.routes['fixture']['native_guard']
        for key in ('context_path', 'context_sha256', 'board', 'kanban_db', 'hermes', 'receipts_dir'):
            guard.pop(key)
        historical = self.reserve()
        with patch.object(self.adapter, '_guard_verified', return_value=True):
            await self.adapter.submit(historical, 'Previously admitted', durable=True)
        result = await self.adapter.poll(historical)
        self.assertEqual(result['status'], 'observed', result)
        self.assertNotIn('HERMES_KANBAN_BOARD', observed[-1])
        self.assertNotIn('HERMES_KANBAN_DB', observed[-1])
        guard['board'] = 'default'
        with self.assertRaisesRegex(ValueError, 'invalid_native_board_identity'):
            self.adapter._environment(self.adapter.routes['fixture'])

    async def test_context_guard_rejects_hash_hook_board_and_spill_changes(self):
        import copy
        original_route = copy.deepcopy(self.adapter.routes['fixture'])
        original_native = copy.deepcopy(self.native_config)
        changes = [('context_hash', lambda r,n: r['native_guard'].update(context_sha256='0'*64)),
            ('board', lambda r,n: r['native_guard'].update(board='foreign')),
            ('db', lambda r,n: r['native_guard'].update(kanban_db='/foreign')),
            ('spill', lambda r,n: n['hooks']['output_spill'].update(max_chars=9999)),
            ('disabled_spill', lambda r,n: n['hooks']['output_spill'].update(enabled=False)),
            ('missing_context', lambda r,n: n['hooks'].pop('pre_llm_call')),
            ('context_command', lambda r,n: n['hooks']['pre_llm_call'][0].update(command='other')),
            ('extra_hook', lambda r,n: n['hooks'].update(post_tool_call=[]))]
        for label, mutate in changes:
            with self.subTest(label=label):
                self.adapter.routes['fixture'] = copy.deepcopy(original_route)
                self.native_config = copy.deepcopy(original_native)
                mutate(self.adapter.routes['fixture'], self.native_config)
                discovery = await self.adapter.discover('fixture')
                self.assertFalse(discovery['native_limits']['guard_verified'])

    async def test_guard_route_arguments_and_parent_executable_are_exact(self):
        route = self.adapter.routes['fixture']
        self.assertTrue(self.adapter._guard_verified(route, self.native_config))
        for key, wrong in [('profile', self.route['workspace']), ('kanban_home', self.route['workspace']),
                           ('parent_python', 'relative-python')]:
            original = route['native_guard'][key]
            route['native_guard'][key] = wrong
            self.assertFalse(self.adapter._guard_verified(route, self.native_config))
            route['native_guard'][key] = original
        self.native_config['hooks']['pre_tool_call'][0]['command'] += ' --profile /different'
        self.assertFalse(self.adapter._guard_verified(route, self.native_config))

    async def test_guard_subprocess_blocks_malformed_other_task_and_creation(self):
        guard = RUNTIME / 'gtd_felix/native_guard.py'
        def call(raw, own='t_owned'):
            env = {'PATH': os.environ.get('PATH', ''), 'HERMES_KANBAN_TASK': own}
            completed = subprocess.run([sys.executable, '-B', str(guard), '--parent-python', sys.executable, '--profile', self.route['hermes_home'], '--kanban-home', self.route['kanban_home']], input=raw, text=True,
                capture_output=True, timeout=5, env=env)
            self.assertEqual(completed.stderr, '')
            return completed.returncode, json.loads(completed.stdout)
        for raw in ('bad json', '[]', 'null', 'x' * 65537):
            code, result = call(raw)
            self.assertEqual((code, result['decision']), (2, 'block'))
        for tool in ('kanban_create', 'kanban_list', 'kanban_reassign', 'kanban_edit', 'terminal'):
            code, result = call(json.dumps({'hook_event_name': 'pre_tool_call', 'tool_name': tool, 'tool_input': {}}))
            self.assertEqual((code, result['decision']), (2, 'block'))
        for tool in ('kanban_complete', 'kanban_block', 'kanban_comment', 'kanban_heartbeat'):
            payload = {'hook_event_name': 'pre_tool_call', 'tool_name': tool, 'tool_input': {'task_id': 't_owned'}}
            self.assertEqual(call(json.dumps(payload))[0], 2)
            payload['tool_input']['task_id'] = 't_other'
            self.assertEqual(call(json.dumps(payload))[0], 2)

    async def test_preflight_rejection_proves_no_effect_and_releases_reservation(self):
        job_id = self.reserve()
        self.native_config['agent.max_turns'] = 99
        rejected = await self.adapter.submit(job_id, 'Never dispatched')
        self.assertTrue(rejected['no_effect'])
        self.assertTrue(rejected['terminal'])
        self.assertEqual(self.control.budget()['active'], 0)
        self.assertEqual(self.control.budget()['committed_cost_usd'], 0)
        self.assertEqual(self.control.get_job(job_id)['native']['provider'], 'gtd-hermes-admission')
        self.assertFalse(any(r[0] == 'POST' for r in self.requests))
        self.assertIsNone(self.adapter._get('hermes:intent:' + job_id))
        self.native_config['agent.max_turns'] = 1
        self.restart()
        self.assertEqual((await self.adapter.submit(job_id, 'Do not revive old admission'))['status'], 'rejected')
        self.assertFalse(any(r[0] == 'POST' for r in self.requests))

    async def test_durable_worker_excludes_implicit_global_mcp(self):
        self.adapter.routes['fixture']['allowed_mcp_toolsets'] = {'gtd': ['gtd_read', 'gtd_command', 'gtd_dispatch']}
        self.native_config['platform_toolsets.api_server'] = ['gtd']
        self.tool_inventory = [{'name': 'gtd', 'enabled': True, 'configured': True,
                                'tools': ['mcp__gtd__gtd_read', 'mcp__gtd__gtd_command', 'mcp__gtd__gtd_dispatch']}]
        denied = await self.adapter.submit(self.reserve(), 'No implicit MCP', durable=True)
        self.assertEqual(denied['error'], 'durable_implicit_mcp_not_allowed')
        self.assertTrue(denied['no_effect'])
        self.native_config['platform_toolsets.cli'] = ['no_mcp']
        admitted = await self.adapter.submit(self.reserve(), 'Native lifecycle only', durable=True)
        self.assertEqual(admitted['status'], 'submitted', admitted)

    async def test_stalled_running_enforces_limit_and_stop_is_durable(self):
        # E28 repro: frozen provider timestamps (created 100, updated 102)
        # must not freeze enforcement. Fails on base (observed stays 2,
        # validate never fires); passes with the local admission floor.
        job_id = self.reserve()  # max_runtime_seconds=60
        self.run_status = "running"
        t0 = time.time()
        self.assertEqual((await self.adapter.submit(job_id, "Stalled work"))["status"], "submitted")
        first = await self.adapter.poll(job_id)
        self.assertEqual(first["native_status"], "running")
        self.assertLess(first["observation"]["runtime_seconds"], 60)
        self.assertEqual(first["observation"]["native_runtime_seconds"], 2)
        self.assertIsNotNone((self.adapter._get("hermes:state:" + job_id) or {}).get("native_admitted_at"))
        # Silence without chunks past the limit: controlled clock, no sleep.
        with patch("gtd_felix.hermes.time.time", return_value=t0 + 125):
            stalled = await self.adapter.poll(job_id)
        obs = stalled["observation"]
        self.assertGreaterEqual(obs["runtime_seconds"], 124)
        self.assertLessEqual(obs["runtime_seconds"], 125)
        self.assertEqual(obs["native_runtime_seconds"], 2)
        self.assertEqual(obs["cost_telemetry"], "unknown")
        self.assertEqual(self.control.validate(job_id, "prepare_private")["reason"], "job_runtime_exhausted")
        with self.assertRaisesRegex(ValueError, "job_runtime_exhausted"):
            self.adapter._validation(self.control.get_job(job_id))
        # Durable idempotent STOP by exact admitted identity, single remote call.
        stop1 = await self.adapter.stop(job_id)
        self.assertEqual(stop1["status"], "stop_requested")
        stops = [r for r in self.requests if r[0] == "POST" and r[1].endswith("/stop")]
        self.assertEqual(1, len(stops))
        self.assertEqual(await self.adapter.stop(job_id), stop1)
        self.assertEqual(1, len([r for r in self.requests if r[0] == "POST" and r[1].endswith("/stop")]))
        # No fabricated terminality: still running remotely keeps the slot.
        still = await self.adapter.poll(job_id)
        self.assertEqual(still["native_status"], "running")
        self.assertFalse(self.control.get_job(job_id)["terminal"])
        self.assertEqual(self.control.budget()["active"], 1)
        # Terminal failure integrates as discarded without double charge.
        self.run_status = "failed"
        final = await self.adapter.poll(job_id)
        self.assertTrue(final["terminal"])
        job = self.control.get_job(job_id)
        self.assertTrue(job["terminal"])
        self.assertEqual(job["integration"], "discarded")
        budget = self.control.budget()
        self.assertEqual(budget["active"], 0)
        self.assertLessEqual(budget["committed_runtime_seconds"], obs["runtime_seconds"] + 60)
        self.assertEqual(len(self.runs), 1)

    async def test_running_floor_survives_restart_without_resetting_deadline(self):
        # The durable anchor (not the poll clock) owns the deadline across
        # restarts and reconciles; no resubmission, no double run.
        job_id = self.reserve()
        self.run_status = "running"
        t0 = time.time()
        await self.adapter.submit(job_id, "Stall across restart")
        await self.adapter.poll(job_id)
        self.restart()
        with patch("gtd_felix.hermes.time.time", return_value=t0 + 130):
            stalled = await self.adapter.poll(job_id)
        self.assertGreaterEqual(stalled["observation"]["runtime_seconds"], 129)
        self.assertEqual(self.control.validate(job_id, "prepare_private")["reason"], "job_runtime_exhausted")
        self.assertEqual(len(self.runs), 1)
        self.assertEqual(1, len([r for r in self.requests if r[0] == "POST" and r[1] == "/v1/runs"]))

    async def test_healthy_running_keeps_telemetry_and_never_sent_uncharged(self):
        # Guard against false positives: under-limit running validates, and a
        # never-sent identity carries no anchor, no charge, no remote effect.
        job_id = self.reserve()
        self.run_status = "running"
        t0 = time.time()
        await self.adapter.submit(job_id, "Healthy work")
        with patch("gtd_felix.hermes.time.time", return_value=t0 + 10):
            early = await self.adapter.poll(job_id)
        self.assertEqual(early["observation"]["native_runtime_seconds"], 2)
        self.assertGreaterEqual(early["observation"]["runtime_seconds"], 9)
        self.assertLessEqual(early["observation"]["runtime_seconds"], 10)
        self.assertTrue(self.control.validate(job_id, "prepare_private")["allowed"])
        self.run_status = "completed"
        done = await self.adapter.poll(job_id)
        self.assertTrue(done["terminal"])
        self.assertTrue(self.control.get_job(job_id)["terminal"])
        other = self.service.capture("felix", "capture-never", "Other synthetic preparation")["item"]
        def never_request(purpose, **changes):
            req = dict(item_id=other["id"], expected_version=other["version"], capability="prepare_private",
                mandate_id=None, bot_id="fixture", purpose=purpose, scope="Synthetic family",
                max_cost_usd=4, max_runtime_seconds=120, max_retries=0, max_descendants=1)
            return dict(req, **changes)
        root = self.control.reserve("gtd-felix", "parent-never", never_request("Parent"))["job_id"]
        child = self.control.reserve("gtd-felix", "child-never", never_request(
            "Child", parent_job_id=root, max_cost_usd=2, max_runtime_seconds=60,
            max_descendants=0))["job_id"]
        await self.adapter.submit(root, "Parent")
        second = await self.adapter.submit(child, "Child")
        self.assertEqual(second["error"], "native_slot_busy")
        self.assertIsNone((self.adapter._get("hermes:state:" + child) or {}).get("native_admitted_at"))
        self.assertEqual((await self.adapter.poll(child))["error"], "native_identity_missing")
        self.assertEqual(self.control.get_job(child)["observed_runtime_seconds"], 0)


if __name__ == '__main__':
    unittest.main()
