"""Real MCP stdio -> authenticated loopback HTTP -> SQLite domain commands."""
import asyncio
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
import aiohttp
from aiohttp import web
from gtd_felix.application import create_app
from gtd_felix.control import ExecutionControl
from gtd_felix.mcp import MCPClient, TOOLS, instructions
from gtd_felix.service import GTDService

OWNER, PRINCIPAL = 'synthetic-owner-token', 'synthetic-principal-token'


def budget():
    return dict(period_start=datetime.now(timezone.utc).isoformat(), period_seconds=3600,
        max_cost_usd=20, max_runtime_seconds=2000, recovery_cost_usd=2, recovery_runtime_seconds=100,
        max_job_runtime_seconds=300, max_retries=0, max_descendants=2, max_active=1)


class MCPTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.service = GTDService(self.root / 'data', executor_actors=['history-worker'])
        self.control = ExecutionControl(self.service, budget())
        self.item = self.service.capture('felix', 'capture', 'Prepare a synthetic note')['item']
        self.bot = dict(id='principal', state='available', source_urn='urn:test:principal', host='synthetic', profile='fixture',
            capabilities=['prepare_private'], item_id=self.item['id'], mandate_id=None, probe_evidence='fixture://route')
        self.control.register_bot('felix', 'bot', self.bot)
        self.request = dict(item_id=self.item['id'], expected_version=self.item['version'], capability='prepare_private',
            bot_id='principal', purpose='Prepare', scope='Synthetic', mandate_id=None,
            max_cost_usd=4, max_runtime_seconds=200, max_retries=0, max_descendants=1)
        self.job = self.control.reserve('gtd-felix', 'reserve', self.request)['job_id']
        config = dict(data_dir=str(self.root / 'data'), actors={'owner': 'felix', 'principal': 'gtd-felix', 'executors': ['history-worker']},
            api_tokens={OWNER: 'felix', PRINCIPAL: 'gtd-felix'})
        self.runner = web.AppRunner(create_app(self.service, self.control, config), access_log=None)
        await self.runner.setup()
        site = web.TCPSite(self.runner, '127.0.0.1', 0)
        await site.start()
        self.url = 'http://127.0.0.1:' + str(site._server.sockets[0].getsockname()[1])
        self.client = MCPClient(self.url, PRINCIPAL)

    async def test_source_coverage_keeps_three_tools_and_reads_http(self):
        self.assertEqual(len(TOOLS),3)
        result=await self.client.call('gtd_read',{'view':'source_coverage'})
        self.assertIsNone(result['external_sources_current'])
        self.assertEqual(result['configured_count'],0)
        with self.assertRaises(ValueError):
            await self.client.call('gtd_read',{'view':'source_coverage','account':'arbitrary'})

    async def asyncTearDown(self):
        await self.runner.cleanup()
        self.service.close()
        self.temp.cleanup()

    async def test_material_read_exact_identity_and_argument_boundary(self):
        result = self.service.execute('felix', {'operation_id': 'material-read', 'action': 'put_material',
            'item_id': self.item['id'], 'expected_version': self.item['version'], 'fields': {'content': 'Exact UTF-8 ñ'}})
        material = result['item']['materials'][0]
        args = {'view': 'material', 'item_id': self.item['id'], 'material_id': material['id'], 'version': 1}
        value = await self.client.call('gtd_read', args)
        self.assertEqual(value['content'], 'Exact UTF-8 ñ')
        for changes in ({'version': True}, {'path': '/arbitrary'}, {'material_id': ''}):
            with self.assertRaises(ValueError): await self.client.call('gtd_read', {**args, **changes})

    def command(self, operation='clarify', **changes):
        return dict(dict(operation_id=operation, action='clarify', item_id=self.item['id'], expected_version=self.item['version'],
            fields={'kind': 'reference', 'commitment': 'proposed'}), **changes)

    async def test_stdio_protocol_and_actual_command_persistence(self):
        messages = [dict(jsonrpc='2.0', id=1, method='initialize', params={'protocolVersion': '2024-11-05', 'capabilities': {}, 'clientInfo': {'name': 'fixture', 'version': '1'}}),
            dict(jsonrpc='2.0', method='notifications/initialized'), dict(jsonrpc='2.0', id=2, method='ping'),
            dict(jsonrpc='2.0', id=3, method='tools/list'),
            dict(jsonrpc='2.0', id=4, method='tools/call', params={'name': 'gtd_command', 'arguments': {'job_id': self.job, 'command': self.command()}})]
        messages.extend([dict(jsonrpc='2.0', id=5, method='tools/call', params={'name': 'gtd_read', 'arguments': {'view': 'calculate', 'calculation': {'operation': 'sum', 'operands': ['18.25', '0.75']}}}),
            dict(jsonrpc='2.0', id=6, method='tools/call', params={'name': 'gtd_read', 'arguments': {'view': 'calculate', 'calculation': {'operation': 'divide', 'operands': [1, 0]}}})])
        env = {**os.environ, 'PYTHONPATH': str(RUNTIME), 'GTD_API_URL': self.url, 'GTD_API_TOKEN': PRINCIPAL}
        proc = await asyncio.create_subprocess_exec(sys.executable, '-B', '-m', 'gtd_felix.mcp', env=env,
            stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await asyncio.wait_for(proc.communicate(('\n'.join(json.dumps(m) for m in messages) + '\n').encode()), 20)
        self.assertEqual(proc.returncode, 0, stderr)
        self.assertEqual(stderr, b'')
        responses = [json.loads(line) for line in stdout.splitlines()]
        self.assertEqual([r['id'] for r in responses], [1, 2, 3, 4, 5, 6])
        self.assertEqual({t['name'] for t in responses[2]['result']['tools']}, {'gtd_read', 'gtd_command', 'gtd_dispatch'})
        self.assertFalse(responses[4]['result']['isError'])
        self.assertEqual(json.loads(responses[4]['result']['content'][0]['text'])['result'], '19')
        self.assertTrue(responses[5]['result']['isError'])
        self.assertIn('calculation_division_by_zero', responses[5]['result']['content'][0]['text'])
        self.assertFalse(responses[3]['result']['isError'])
        receipt = json.loads(responses[3]['result']['content'][0]['text'])
        self.assertEqual(receipt['status'], 'applied', receipt)
        self.assertEqual(self.service.get_item(self.item['id'])['kind'], 'reference')
        self.assertTrue(self.control.validate(self.job, 'prepare_private')['allowed'])
        self.assertNotIn(PRINCIPAL, stdout.decode())

    async def test_own_clarification_then_material_and_compatible_human_notes(self):
        clarified = await self.client.call('gtd_command', {'job_id': self.job, 'command': self.command()})
        self.assertEqual(clarified['status'], 'applied', clarified)
        current = clarified['item']
        note = self.service.execute('felix', dict(operation_id='note', action='edit', item_id=current['id'], expected_version=current['version'], fields={'notes': 'Human annotation'}))
        item = await self.client.call('gtd_read', {'view': 'item', 'item_id': current['id']})
        material = await self.client.call('gtd_command', {'job_id': self.job, 'command': self.command('material', action='put_material', expected_version=item['version'], fields={'content': 'Prepared using actual state'})})
        self.assertEqual(material['status'], 'applied', material)
        self.assertEqual(len(self.service.materials(current['id'])), 1)
        self.assertEqual(self.service.get_item(current['id'])['notes'], 'Human annotation')
        self.assertEqual(len(self.control.get_job(self.job)['progress']), 2)

    async def test_private_clarification_capability_is_narrow_and_resolutions_stay_exclusive(self):
        command = TOOLS[1]['inputSchema']['properties']['command']['oneOf']
        clarify = next(c for c in command if c['properties']['action']['const'] == 'clarify')['properties']['fields']
        self.assertEqual(clarify['properties']['capability']['enum'], ['prepare_private'])
        self.assertNotIn('work_capability', clarify['properties'])
        for action in ('plan', 'edit', 'put_material', 'assess_result', 'review'):
            fields = next(c for c in command if c['properties']['action']['const'] == action)['properties']['fields']
            self.assertNotIn('capability', fields['properties'])
        resolutions = {branch['if']['properties']['destination']['const']: branch['then']
            for branch in clarify['allOf'] if 'destination' in branch['if'].get('properties', {})}
        for destination in ('existing', 'discard'):
            self.assertFalse(resolutions[destination]['additionalProperties'])
            self.assertNotIn('capability', resolutions[destination]['properties'])
        receipt = await self.client.call('gtd_command', {'job_id': self.job, 'command': self.command('private-explicit', fields={
            'kind': 'action', 'commitment': 'committed', 'capability': 'prepare_private',
            'completion_criteria': 'Prepare the synthetic note privately',
            'intent_basis': {'source_item_id': self.item['id'], 'quote': self.item['text']}})})
        self.assertEqual(receipt['status'], 'applied', receipt)
        self.assertEqual(receipt['item']['work_capability'], 'prepare_private')

    async def test_existing_route_uses_source_job_without_granting_target_scope(self):
        target = self.service.capture('felix', 'existing-target', 'Existing subject')['item']
        fields = {'destination': 'existing', 'target_item_id': target['id'], 'reason': 'Related human intake',
            'intent_basis': {'source_item_id': self.item['id'], 'quote': self.item['text']}}
        receipt = await self.client.call('gtd_command', {'job_id': self.job, 'command': self.command('route', fields=fields)})
        self.assertEqual(receipt['status'], 'applied', receipt)
        self.assertEqual(receipt['item']['clarification']['target_item_id'], target['id'])
        self.assertEqual(self.service.get_item(target['id']), target)
        self.assertNotIn(target['id'], self.control.get_job(self.job)['item_bases'])
        self.assertIsNotNone(self.control.own_terminal_progress(self.job))
        observed = self.control.observe(self.job, {'native_identity': {'provider': 'fixture', 'host': 'synthetic', 'profile': 'fixture', 'id': self.job},
            'native_status': 'completed', 'terminal': True, 'cost_usd': .1, 'runtime_seconds': 1, 'evidence_reference': 'fixture://routed-terminal'})
        self.assertEqual(observed['status'], 'recorded', observed)
        self.assertEqual(self.control.integrate_terminal_progress(self.job)['status'], 'integrated')
        self.assertTrue(any(e['payload'].get('reason') == 'routed_human_instruction' for e in self.service.pending_events('gtd-review', 'local')))
        mutation = await self.client.call('gtd_command', {'job_id': self.job, 'command': self.command('escape', item_id=target['id'], expected_version=target['version'], fields={'kind': 'reference'})})
        self.assertEqual(mutation['status'], 'rejected', mutation)
        self.assertEqual(self.service.get_item(target['id']), target)
        fields_schema = next(c for c in TOOLS[1]['inputSchema']['properties']['command']['oneOf'] if c['properties']['action']['const'] == 'clarify')['properties']['fields']
        self.assertIn('existing', fields_schema['properties']['destination']['enum'])

    async def test_no_principal_mutation_bypass_or_owner_escalation(self):
        async with aiohttp.ClientSession() as session:
            for path in ('/v1/commands', '/v1/agent/command'):
                async with session.post(self.url + path, headers={'Authorization': 'Bearer ' + PRINCIPAL}, json=self.command()) as response:
                    self.assertEqual(response.status, 403)
                    self.assertEqual((await response.json())['error'], 'job_required')
            async with session.post(self.url + '/v1/control/reserve', headers={'Authorization': 'Bearer ' + PRINCIPAL}, json={'operation_id': 'bypass', 'request': self.request}) as response:
                self.assertEqual(response.status, 403)
        escalation = await self.client.call('gtd_command', {'job_id': self.job, 'command': self.command(action='set_attention', fields={'paused': True}, actor='felix')})
        self.assertEqual(escalation['error'], 'agent_action_not_enabled')
        self.assertEqual(self.service.get_item(self.item['id'])['kind'], 'capture')

    async def test_human_correction_and_stop_block_future_tool_effects(self):
        edited = self.service.execute('felix', dict(operation_id='human-edit', action='edit', item_id=self.item['id'], expected_version=self.item['version'], fields={'title': 'Corrected human meaning'}))
        rejected = await self.client.call('gtd_command', {'job_id': self.job, 'command': self.command(expected_version=edited['item']['version'])})
        self.assertEqual(rejected['error'], 'stale_item_version')
        self.control.request_stop('felix', 'stop', self.job)
        rejected = await self.client.call('gtd_command', {'job_id': self.job, 'command': self.command()})
        self.assertEqual(rejected['error'], 'stop_requested')

    def finish_native(self, job_id, status='completed', runtime=1):
        native = {'provider': 'fixture', 'host': 'synthetic', 'profile': 'fixture', 'id': job_id}
        if not self.control.get_job(job_id)['native']:
            self.control.record_dispatch(job_id, native)
        receipt = self.control.observe(job_id, {'native_identity': native, 'native_status': status,
            'terminal': True, 'cost_usd': .1, 'runtime_seconds': runtime, 'evidence_reference': 'fixture://' + job_id})
        self.assertEqual(receipt['status'], 'recorded', receipt)
        if status == 'completed':
            self.control.integrate_terminal_progress(job_id)

    async def test_jobs_history_after_correction_exposes_cancelled_child_without_new_effect(self):
        self.finish_native(self.job)
        project = self.service.capture('felix', 'history-project', 'Prepare guide 09-12')['item']
        project = self.service.execute('felix', {'operation_id': 'history-kind', 'action': 'clarify',
            'item_id': project['id'], 'expected_version': project['version'],
            'fields': {'kind': 'project', 'commitment': 'committed'}})['item']
        grant = self.service.execute('felix', {'operation_id': 'history-worker-mandate', 'action': 'grant_mandate',
            'item_id': project['id'], 'expected_version': project['version'], 'fields': {
                'scope_item_id': project['id'], 'capabilities': ['prepare_private'],
                'actors': ['gtd-felix', 'history-worker'], 'completion_criteria': 'Guide prepared'}})
        self.assertEqual(grant['status'], 'applied', grant)
        project = grant['item']
        registered = self.control.register_bot('felix', 'history-worker-bot', {**self.bot,
            'id': 'history-worker', 'actor': 'history-worker', 'item_id': project['id'], 'mandate_id': grant['mandate']['id']})
        self.assertEqual(registered['status'], 'applied', registered)
        child = self.service.execute('felix', {'operation_id': 'history-child', 'action': 'derive',
            'item_id': project['id'], 'expected_version': project['version'],
            'fields': {'kind': 'action', 'title': 'Prepare bounded guide', 'capability': 'prepare_private',
                'executor': 'history-worker', 'mandate_id': grant['mandate']['id']}})['item']
        request = {**self.request, 'item_id': project['id'], 'expected_version': project['version'], 'mandate_id': grant['mandate']['id']}
        parent = self.control.reserve('gtd-felix', 'history-parent', request)['job_id']
        dispatch = {'job_id': parent, 'operation_id': 'history-dispatch', 'request': {
            **self.request, 'item_id': child['id'], 'expected_version': child['version'],
            'purpose': 'Bounded guide', 'bot_id': 'history-worker', 'mandate_id': grant['mandate']['id'], 'max_cost_usd': .5, 'max_runtime_seconds': 30, 'max_descendants': 0}}
        receipt = await self.client.call('gtd_dispatch', dispatch)
        self.assertEqual(receipt['status'], 'reserved', receipt)
        previous = receipt['job_id']
        self.finish_native(parent)
        activated = self.control.activate_deferred(previous)
        self.assertEqual(activated['status'], 'activated', activated)
        self.control.record_dispatch(previous, {'provider': 'fixture', 'host': 'synthetic', 'profile': 'fixture', 'id': previous})
        current = self.service.get_item(project['id'])
        corrected = self.service.execute('felix', {'operation_id': 'history-correction', 'action': 'edit',
            'item_id': project['id'], 'expected_version': current['version'], 'fields': {'text': 'Prepare guide 10-13'}})
        self.assertEqual(corrected['status'], 'applied', corrected)
        self.control.request_stop('felix', 'history-stop', previous)
        self.finish_native(previous, 'cancelled', 2)
        new = self.control.reserve('gtd-felix', 'history-new-parent', {
            **request, 'expected_version': corrected['item']['version']})['job_id']
        before = self.control._load()
        history = await self.client.call('gtd_read', {'view': 'jobs', 'job_id': new})
        cancelled = next((j for j in history if j['id'] == previous), None)
        self.assertIsNotNone(cancelled, history)
        self.assertEqual(cancelled['actor'], 'history-worker')
        self.assertTrue(cancelled['terminal'])
        self.assertEqual(cancelled['integration'], 'discarded')
        self.assertEqual(cancelled['last_observation']['runtime_seconds'], 2)
        self.assertEqual(cancelled['last_observation']['native_status'], 'cancelled')
        self.assertNotIn('source_bases', cancelled)
        self.assertEqual(self.control._load(), before)
        replacement = await self.client.call('gtd_dispatch', {**dispatch, 'job_id': new, 'operation_id': 'history-replacement'})
        self.assertEqual(replacement['status'], 'reserved', replacement)
        replay = await self.client.call('gtd_dispatch', {**dispatch, 'job_id': new, 'operation_id': 'history-replacement'})
        self.assertEqual(replay['job_id'], replacement['job_id'])

    async def test_dispatch_reserves_once_without_waiting_for_native_work(self):
        child = {**self.request, 'purpose': 'Private specialist', 'max_cost_usd': 1, 'max_runtime_seconds': 50, 'max_descendants': 0}
        args = {'job_id': self.job, 'operation_id': 'dispatch', 'request': child}
        first = await self.client.call('gtd_dispatch', args)
        second = await self.client.call('gtd_dispatch', args)
        self.assertEqual(first['status'], 'reserved', first)
        self.assertEqual(first['job_id'], second['job_id'])
        self.assertEqual(first['job']['delivery'], 'deferred')
        self.assertEqual(self.control.budget()['active'], 1)
        self.assertEqual(self.control.budget()['committed_cost_usd'], 4)
        self.assertEqual(len(self.service.pending_events('gtd-dispatch', 'local')), 1)

    async def test_calculate_exact_arithmetic_without_http_or_domain_effects(self):
        before = self.service.store.db.execute('SELECT count(*) FROM operations').fetchone()[0]
        cases = [('sum', ['0.1', '0.2', '1.70'], '2'),
                 ('subtract', ['100.00', '19.95'], '80.05'),
                 ('multiply', ['12.5', '4', '-0.2'], '-10'),
                 ('divide', ['7', '8'], '0.875'),
                 ('sum', [2, 0.25, '-0.00'], '2.25')]
        with patch('gtd_felix.mcp.aiohttp.ClientSession', side_effect=AssertionError('Calculation must not use HTTP')):
            for operation, operands, expected in cases:
                result = await self.client.call('gtd_read', {'view': 'calculate', 'calculation': {'operation': operation, 'operands': operands}})
                self.assertEqual(result['result'], expected)
                self.assertTrue(result['exact'])
                self.assertEqual(result['precision'], 128)
                replay = await self.client.call('gtd_read', {'view': 'calculate', 'calculation': {'operation': operation, 'operands': result['operands']}})
                self.assertEqual(replay, result)
        self.assertEqual(self.service.store.db.execute('SELECT count(*) FROM operations').fetchone()[0], before)

    async def test_calculate_rejects_ambiguous_nonfinite_and_unbounded_inputs(self):
        invalid = ['1,000', '1,2', ' 1', '+1', '01', '1e9', 'NaN', 'Infinity', '1+2',
                   True, None, {}, float('nan'), float('inf'), 10 ** 1000, '1' * 129,
                   '0.' + '0' * 64 + '1']
        for operand in invalid:
            with self.subTest(operand_type=type(operand).__name__):
                with self.assertRaises(ValueError):
                    await self.client.call('gtd_read', {'view': 'calculate', 'calculation': {'operation': 'sum', 'operands': [operand]}})
        for request in (None, {}, {'operation': 'eval', 'operands': [1]},
                        {'operation': 'sum', 'operands': []}, {'operation': 'sum', 'operands': [1] * 65},
                        {'operation': 'divide', 'operands': [1]}, {'operation': 'multiply', 'operands': [0, 'bad']}):
            with self.assertRaises(ValueError):
                await self.client.call('gtd_read', {'view': 'calculate', 'calculation': request})

    async def test_calculate_never_rounds_division_or_overflow_into_exact_claim(self):
        cases = [('divide', ['1', '3'], 'calculation_inexact'),
                 ('divide', ['0', '0'], 'calculation_division_by_zero'),
                 ('divide', ['5', '-0.0'], 'calculation_division_by_zero'),
                 ('multiply', ['9' * 64] * 4, None)]
        for operation, operands, error in cases:
            with self.assertRaises(ValueError) as caught:
                await self.client.call('gtd_read', {'view': 'calculate', 'calculation': {'operation': operation, 'operands': operands}})
            if error:
                self.assertEqual(str(caught.exception), error)
        schema = TOOLS[0]['inputSchema']
        self.assertIn('calculate', schema['properties']['view']['enum'])
        self.assertEqual(schema['allOf'][0]['then']['required'], ['calculation'])

    async def test_instruction_whitelist_traversal_and_symlink_rejection(self):
        native = self.root / 'native'
        native.mkdir()
        (native / 'SKILL.md').write_text('Synthetic native instruction')
        self.assertEqual(instructions(root=native)['content'], 'Synthetic native instruction')
        (native / 'references').mkdir()
        (native / 'references/operations.md').write_text('Approved operational instructions')
        self.assertEqual(instructions('references/operations.md', root=native)['content'], 'Approved operational instructions')
        for reference in ('references/acceptance.md', 'references/other.md'):
            (native / reference).write_text('Unapproved synthetic content')
        for reference in ('references/acceptance.md', 'references/other.md', '../secret', '/etc/passwd', 'runtime/gtd_felix/service.py'):
            with self.assertRaises(ValueError):
                instructions(reference, root=native)
        (native / 'SKILL.md').unlink()
        (native / 'SKILL.md').symlink_to(self.root / 'outside')
        with self.assertRaises(ValueError):
            instructions(root=native)
        self.assertEqual(TOOLS[0]['inputSchema']['properties']['reference']['enum'], ['SKILL.md', 'references/operations.md'])
        actions = TOOLS[1]['inputSchema']['properties']['command']['oneOf']
        self.assertIn('intent_basis', next(a for a in actions if a['properties']['action']['const'] == 'clarify')['properties']['fields']['properties'])

    async def test_identical_command_replay_after_progress_is_not_a_second_effect(self):
        args = {'job_id': self.job, 'command': self.command()}
        first = await self.client.call('gtd_command', args)
        second = await self.client.call('gtd_command', args)
        self.assertEqual(first['status'], 'applied')
        self.assertEqual(second['status'], 'already_applied', second)
        self.assertEqual(self.service.get_item(self.item['id'])['version'], first['item']['version'])
        self.assertEqual(len(self.control.get_job(self.job)['progress']), 1)
        changed = await self.client.call('gtd_command', {'job_id': self.job, 'command': self.command(fields={'kind': 'possibility'})})
        self.assertEqual(changed['error'], 'operation_id_reused')
