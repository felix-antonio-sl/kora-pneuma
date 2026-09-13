"""Synthetic principal -> MCP -> real HTTP -> control/domain instruction loop."""
from copy import deepcopy
from pathlib import Path
import sys
import tempfile
import unittest

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from aiohttp.test_utils import TestClient, TestServer
from gtd_felix.application import create_app, writer_lock
from gtd_felix.control import ExecutionControl
from gtd_felix.mcp import MCPClient, COMMAND
from gtd_felix.service import GTDService
from gtd_felix.orchestration import OrchestrationWorker
from test_orchestration import NativeFixture
from test_mcp import budget
from test_application import config, OWNER, PRINCIPAL, EXECUTOR


class HumanInstructionAPITests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.config = config(self.temp.name)
        self.lock = writer_lock(self.config['data_dir'])
        self.lock.__enter__()
        self.service = GTDService(Path(self.config['data_dir']), executor_actors=['worker'])
        self.control = ExecutionControl(self.service, {**budget(), 'max_active': 2,
            'max_cost_usd': 100, 'max_runtime_seconds': 10000})
        self.control.register_bot('felix', 'bot', dict(id='principal', state='available',
            source_urn='urn:test:principal', host='synthetic', profile='fixture',
            capabilities=['prepare_private'], probe_evidence='fixture://route'))
        self.http = TestClient(TestServer(create_app(self.service, self.control, self.config)))
        await self.http.start_server()
        self.mcp = MCPClient(str(self.http.make_url('/')).rstrip('/'), PRINCIPAL)
        self.n = 0
        self.target = await self.capture('Una posibilidad de ver amigos')
        job = self.reserve(self.target)
        receipt = await self.send(job, self.command(self.target, 'clarify',
            {'kind': 'possibility', 'commitment': 'proposed'}))
        self.assertEqual(receipt['status'], 'applied', receipt)
        self.target = receipt['item']
        self.finish(job)

    async def asyncTearDown(self):
        await self.http.close()
        self.service.close()
        self.lock.__exit__(None, None, None)
        self.temp.cleanup()

    def identity(self):
        self.n += 1
        return 'instruction-api-' + str(self.n)

    async def capture(self, text):
        response = await self.http.post('/v1/captures', headers={'Authorization': 'Bearer ' + OWNER},
            json={'operation_id': self.identity(), 'text': text})
        result = await response.json()
        self.assertEqual(result['status'], 'applied', result)
        return result['item']

    def finish(self, job):
        result = self.control.observe(job, {'native_identity': {'provider': 'fixture', 'host': 'synthetic',
            'profile': 'fixture', 'id': job}, 'native_status': 'completed', 'terminal': True,
            'cost_usd': .01, 'runtime_seconds': 1, 'evidence_reference': 'fixture://completed'})
        self.assertEqual(result['status'], 'recorded', result)

    def reserve(self, item, sources=()):
        active = [j for j in self.control._load()['jobs'].values() if not j['terminal']]
        if len(active) >= 2:
            self.finish(active[0]['id'])
        receipt = self.control.reserve('gtd-felix', self.identity(), dict(item_id=item['id'],
            expected_version=item['version'], capability='prepare_private', bot_id='principal',
            purpose='Synthetic instruction ' + self.identity(), scope='This subject', mandate_id=None,
            human_instruction_source_ids=list(sources), max_cost_usd=1, max_runtime_seconds=60,
            max_retries=0, max_descendants=0))
        self.assertEqual(receipt['status'], 'reserved', receipt)
        return receipt['job_id']

    def command(self, item, action, fields):
        return dict(operation_id=self.identity(), item_id=item['id'], expected_version=item['version'],
            action=action, fields=fields)

    async def send(self, job, command):
        return await self.mcp.call('gtd_command', {'job_id': job, 'command': command})

    async def routed(self, text='Corrige: quiero volver a conversar con amigos', target=None, reserve_destination=True):
        target = target or self.target
        source = await self.capture(text)
        source_job = self.reserve(source)
        result = await self.send(source_job, self.command(source, 'clarify', dict(destination='existing',
            target_item_id=target['id'], reason='Instrucción directa sobre el asunto',
            intent_basis={'source_item_id': source['id'], 'quote': text})))
        self.assertEqual(result['status'], 'applied', result)
        source = result['item']
        self.finish(source_job)
        events = [e for e in self.service.pending_events('gtd-review', 'local')
            if e['payload'].get('source_capture_id') == source['id']]
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]['payload']['item_id'], target['id'])
        self.assertEqual(events[0]['payload']['intent_basis']['quote'], text)
        destination_job = self.reserve(target, [events[0]['payload']['source_capture_id']]) if reserve_destination else None
        return source, source_job, destination_job

    def instruction(self, source, instruction='correct', changes=None, target=None):
        return self.command(target or self.target, 'apply_human_instruction', dict(instruction=instruction,
            intent_basis=dict(source_item_id=source['id'], source_revision=len(source['source_revisions']),
                quote=source['source_revisions'][-1]['text']),
            changes=({'title': 'Conversar con amigos', 'text': 'Volver a conversar, sin organizar evento'}
                if changes is None else changes)))

    async def test_principal_correction_then_pause_receipt_and_replay_preserve_admission(self):
        source, _, job = await self.routed()
        command = self.instruction(source)
        result = await self.send(job, command)
        self.assertEqual(result['status'], 'applied', result)
        self.target = result['item']
        self.assertEqual(self.target['commitment'], 'proposed')
        self.assertEqual(self.target['source_versions'][source['id']], 1)
        self.assertTrue(self.control.validate(job, 'prepare_private')['allowed'])
        self.assertEqual(self.control.get_job(job)['progress'][-1]['operation_id'], command['operation_id'])
        provenance = self.service.describe_item(self.target['id'])['field_provenance']['title']
        self.assertEqual(provenance['actor'], 'gtd-felix')
        self.assertEqual(provenance['human_authority']['intent_basis'], command['fields']['intent_basis'])
        source, _, pause_job = await self.routed('Pausa este asunto')
        before = self.control.get_job(pause_job)
        command = self.instruction(source, 'pause', {})
        result = await self.send(pause_job, command)
        self.assertEqual(result['status'], 'applied', result)
        self.assertEqual(result['item']['status'], 'paused')
        self.assertEqual(result['item'].get('source_versions'), self.target.get('source_versions'))
        after = self.control.get_job(pause_job)
        self.assertEqual(after['item_bases'], before['item_bases'])
        self.assertEqual(after['source_bases'], before['source_bases'])
        self.assertEqual(after['expected_version'], before['expected_version'])
        self.assertEqual(after['progress'][-1]['operation_id'], command['operation_id'])
        self.assertEqual(self.control.validate(pause_job, 'prepare_private')['reason'], 'work_paused')
        replay = await self.send(pause_job, command)
        self.assertEqual(replay['status'], 'already_applied', replay)
        self.assertEqual(self.control.get_job(pause_job), after)
        newer = self.command(result['item'], 'put_material', {'content': 'Must not run'})
        self.assertEqual((await self.send(pause_job, newer))['error'], 'work_paused')
        reopened = self.service.execute('felix', self.command(result['item'], 'reopen', {}))
        self.assertEqual(reopened['status'], 'applied', reopened)
        self.assertEqual(self.control.validate(pause_job, 'prepare_private')['reason'], 'stale_item_version')

    async def test_owner_executor_and_impersonation_cannot_use_principal_action(self):
        source, _, job = await self.routed()
        command = self.instruction(source)
        for token in (OWNER, EXECUTOR):
            response = await self.http.post('/v1/agent/command',
                headers={'Authorization': 'Bearer ' + token, 'X-GTD-Job-ID': job},
                json={**command, 'actor': 'gtd-felix'})
            self.assertEqual(response.status, 403)
            self.assertEqual((await response.json())['error'], 'principal_required')
        self.assertEqual(self.service.get_item(self.target['id']), self.target)
        result = await self.send(job, {**command, 'actor': 'felix'})
        self.assertEqual(result['status'], 'applied', result)
        self.assertEqual(result['item']['human_instruction']['interpreted_by'], 'gtd-felix')

    async def test_capture_job_cross_scope_missing_and_expired_job_rejected(self):
        source, source_job, job = await self.routed()
        command = self.instruction(source)
        self.assertEqual((await self.send(source_job, command))['error'], 'outside_job_scope')
        other = await self.capture('Otro asunto')
        other_job = self.reserve(other)
        self.assertEqual((await self.send(other_job, command))['error'], 'outside_job_scope')
        self.assertEqual((await self.send('absent', command))['error'], 'job_required')
        state = self.control._load()
        state['jobs'][job]['observed_runtime_seconds'] = state['jobs'][job]['max_runtime_seconds']
        self.control._save(state)
        self.assertEqual((await self.send(job, command))['error'], 'job_runtime_exhausted')
        self.assertEqual(self.service.get_item(self.target['id']), self.target)

    async def test_snapshot_missing_stale_source_and_stale_target_rejected(self):
        source, _, job = await self.routed()
        command = self.instruction(source)
        bare_job = self.reserve(self.target)
        self.assertEqual((await self.send(bare_job, command))['error'], 'routed_intent_set_stale')
        result = self.service.execute('felix', self.command(source, 'edit', {'text': 'Instrucción cambiada'}))
        self.assertEqual(result['status'], 'applied', result)
        self.assertEqual((await self.send(job, command))['error'], 'source_version_stale')
        source, _, job = await self.routed('Otra corrección directa')
        result = self.service.execute('felix', self.command(self.target, 'edit', {'title': 'Corrección humana posterior'}))
        self.assertEqual(result['status'], 'applied', result)
        self.assertEqual((await self.send(job, self.instruction(source)))['error'], 'stale_item_version')

    async def test_real_routed_event_admits_destination_source_snapshot(self):
        source, source_job, _ = await self.routed(reserve_destination=False)
        native = NativeFixture(self.control, self.mcp)
        native.no_progress = True
        native.keep_running = True
        worker = OrchestrationWorker(self.service, self.control, native, dict(actor='gtd-felix',
            principal_bot_id='principal', clarification_accounts=['fixture'],
            reservation=dict(max_cost_usd=1, max_runtime_seconds=60, max_retries=0, max_descendants=0),
            poll_seconds=.01, review_interval_seconds=300))
        await worker.tick()
        admissions = [submission for submission in native.submissions
            if self.control.get_job(submission['job_id'])['item_id'] == self.target['id']]
        self.assertEqual(len(admissions), 1, native.submissions)
        job = self.control.get_job(admissions[0]['job_id'])
        self.assertEqual(job['human_instruction_source_ids'], [source['id']])
        self.assertEqual(job['source_bases'][source['id']], self.control._basis(source['id']))
        self.assertNotIn(source['id'], job['item_bases'])
        self.assertNotEqual(job['id'], source_job)
        self.assertIn(source['id'], admissions[0]['prompt'])
        result = await self.send(job['id'], self.instruction(source))
        self.assertEqual(result['status'], 'applied', result)
        self.assertEqual(self.control.get_job(job['id'])['progress'][-1]['operation_id'], result['operation_id'])

    async def test_malformed_instruction_objects_reject_without_server_error(self):
        source, _, job = await self.routed()
        base = self.instruction(source)
        for fields in (None, [], 'wrong', {'intent_basis': None}, {'intent_basis': []},
                       {'intent_basis': {'source_item_id': 3}}):
            command = {**base, 'operation_id': self.identity(), 'fields': fields}
            response = await self.http.post('/v1/agent/command',
                headers={'Authorization': 'Bearer ' + PRINCIPAL, 'X-GTD-Job-ID': job}, json=command)
            self.assertEqual(response.status, 400)
            self.assertEqual((await response.json())['error'], 'invalid_human_instruction')
        self.assertEqual(self.service.get_item(self.target['id']), self.target)

    async def test_schema_and_domain_reject_extra_fields_done_reopen_and_invalid_revision(self):
        schema = next(branch for branch in COMMAND['oneOf']
            if branch['properties']['action']['const'] == 'apply_human_instruction')
        self.assertFalse(schema['additionalProperties'])
        branches = schema['properties']['fields']['oneOf']
        self.assertEqual({b['properties']['instruction']['const'] for b in branches}, {'correct', 'pause'})
        for branch in branches:
            self.assertFalse(branch['additionalProperties'])
            basis = branch['properties']['intent_basis']
            self.assertFalse(basis['additionalProperties'])
            self.assertEqual(basis['properties']['source_revision'], {'type': 'integer', 'minimum': 1})
            changes = branch['properties']['changes']
            self.assertFalse(changes['additionalProperties'])
            if branch['properties']['instruction']['const'] == 'correct':
                self.assertEqual(set(changes['properties']), {'title', 'text'})
                self.assertEqual(changes['minProperties'], 1)
            else:
                self.assertEqual(changes['properties'], {})
        source, _, job = await self.routed()
        base = self.instruction(source)
        invalid = [dict(instruction='done'), dict(instruction='reopen'), dict(changes={}),
            dict(changes={'due_at': '2026-10-01'}), dict(changes={'title': 3}), dict(extra='no'),
            dict(instruction='pause', changes={'title': 'No'})]
        for change in invalid:
            command = deepcopy(base)
            command['operation_id'] = self.identity()
            command['fields'].update(change)
            result = await self.send(job, command)
            self.assertEqual(result['status'], 'rejected', result)
        for revision in (True, 0, 2):
            command = deepcopy(base)
            command['operation_id'] = self.identity()
            command['fields']['intent_basis']['source_revision'] = revision
            self.assertEqual((await self.send(job, command))['status'], 'rejected')
        self.assertEqual(self.service.get_item(self.target['id']), self.target)
