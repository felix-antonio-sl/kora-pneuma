"""E66: assess_result without explicit mandate_id records progress (M65 shape).

The agent's assess fields carry no mandate_id; the assessment row inherits the
item's mandate. The receipt stub must match the stored row shape or the
worker's own progress is rejected and the job is guard-stopped. Real HTTP
application path underneath; existing NativeFixture as the fake provider."""
import asyncio
import json
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path
import tempfile

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from aiohttp import web
from gtd_felix.application import create_app
from gtd_felix.control import ExecutionControl
from gtd_felix.mcp import MCPClient
from gtd_felix.orchestration import OrchestrationWorker
from gtd_felix.service import GTDService
from test_orchestration import NativeFixture


class AssessShapeFixture(NativeFixture):
    """M65 shape: put/assess fields carry no mandate_id; the item has one."""

    async def submit(self, job_id, prompt, durable=False):
        self.submissions.append({'job_id': job_id, 'prompt': prompt, 'durable': durable})
        if job_id in self.runs:
            raise AssertionError('blind native resend')
        self.control.record_dispatch(job_id, self.native(job_id))
        self.runs[job_id] = {'status': 'running'}
        job = self.control.get_job(job_id)
        item = await self.client.call('gtd_read', {'view': 'item', 'item_id': job['item_id']})
        put = await self.client.call('gtd_command', {'job_id': job_id, 'command': {
            'operation_id': job_id + ':material', 'action': 'put_material', 'item_id': item['id'],
            'expected_version': item['version'], 'fields': {'content': 'Synthetic result text'}}})
        if put.get('status') != 'applied':
            raise AssertionError(put)
        current = put['item']
        assessed = await self.client.call('gtd_command', {'job_id': job_id, 'command': {
            'operation_id': job_id + ':assess', 'action': 'assess_result', 'item_id': current['id'],
            'expected_version': current['version'], 'fields': {'satisfied': True,
                'evidence': 'Fixture read the saved synthetic material and it meets the criterion.',
                'material_id': current['materials'][0]['id'], 'material_version': 1}}})
        if assessed.get('status') != 'applied':
            raise AssertionError(assessed)
        self.runs[job_id]['output'] = 'Prepared synthetic result.'
        return {'status': 'submitted', 'job_id': job_id, 'native_id': job_id}


class AssessProgressTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.service = GTDService(self.root / 'data', executor_actors=['bounded-executor'])
        self.control = ExecutionControl(self.service, dict(
            period_start=datetime.now(timezone.utc).isoformat(), period_seconds=3600,
            max_cost_usd=20, max_runtime_seconds=2000, recovery_cost_usd=2, recovery_runtime_seconds=100,
            max_job_runtime_seconds=300, max_retries=0, max_descendants=1, max_active=1))
        self.item = self.service.capture('felix', 'capture', 'Synthetic E66 matter')['item']
        clarified = self.service.execute('felix', dict(operation_id='owner-action', action='clarify',
            item_id=self.item['id'], expected_version=self.item['version'], fields={
                'kind': 'action', 'commitment': 'committed', 'capability': 'prepare_private',
                'completion_criteria': 'Fixture verifies a synthetic result.',
                'intent_basis': {'source_item_id': self.item['id'], 'quote': self.item['text']}}))
        granted = self.service.execute('felix', dict(operation_id='owner-grant', action='grant_mandate',
            item_id=self.item['id'], expected_version=clarified['item']['version'], fields={
                'scope_item_id': self.item['id'], 'actors': ['gtd-felix'],
                'capabilities': ['prepare_private', 'local_work'],
                'completion_criteria': 'Fixture verifies a synthetic result.'}))
        self.mandate_id = granted['mandate']['id']
        self.control.register_bot('felix', 'bot', dict(id='principal', state='available',
            source_urn='urn:test:principal', host='synthetic', profile='fixture',
            capabilities=['prepare_private', 'local_work'], item_id=self.item['id'],
            mandate_id=None, probe_evidence='fixture://route'))
        self.config = dict(actor='gtd-felix', principal_bot_id='principal', clarification_accounts=['fixture'],
            reservation=dict(max_cost_usd=4, max_runtime_seconds=200, max_retries=0, max_descendants=1),
            poll_seconds=.01, review_interval_seconds=300)
        appconfig = dict(data_dir=str(self.root / 'data'),
            actors={'owner': 'felix', 'principal': 'gtd-felix', 'executors': []},
            api_tokens={'synthetic-owner-token': 'felix', 'synthetic-agent-token': 'gtd-felix'})
        self.runner = web.AppRunner(create_app(self.service, self.control, appconfig), access_log=None)
        await self.runner.setup()
        site = web.TCPSite(self.runner, '127.0.0.1', 0)
        await site.start()
        self.url = 'http://127.0.0.1:' + str(site._server.sockets[0].getsockname()[1])
        self.client = MCPClient(self.url, 'synthetic-agent-token')
        self.native = AssessShapeFixture(self.control, self.client)
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        self.service.ingest_event({'provider': 'gtd-clarification', 'account': 'fixture',
            'external_id': self.item['id'], 'revision': '1',
            'payload': {'item_id': self.item['id'], 'reason': 'clarification_pending'}})

    async def asyncTearDown(self):
        await self.runner.cleanup()
        self.service.close()
        self.temp.cleanup()

    async def test_assess_without_mandate_records_completes_and_returns_once(self):
        await self.worker.tick()
        self.assertEqual(1, len(self.native.submissions))
        job_id = self.native.submissions[0]['job_id']
        job = self.control.get_job(job_id)
        self.assertFalse(job['stop_requested'])
        self.assertEqual([p['operation_id'] for p in job.get('progress', [])],
            [job_id + ':material', job_id + ':assess'])
        self.assertTrue(self.control.own_terminal_progress(job_id))
        self.assertEqual(self.service.get_item(self.item['id'])['status'], 'done')
        await self.worker.tick()
        job = self.control.get_job(job_id)
        self.assertTrue(job['terminal'])
        self.assertEqual(job['integration'], 'integrated')
        self.assertEqual(len(self.service.materials(self.item['id'])), 1)
        notices = self.service.pending_events('gtd-notification', 'local')
        self.assertEqual(1, len(notices))
        self.assertEqual(notices[0]['payload']['kind'], 'completed')
        # Restart: no resubmission, no duplicate return.
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        await self.worker.tick()
        await self.worker.tick()
        self.assertEqual(1, len(self.native.submissions))
        self.assertEqual(1, len(self.service.pending_events('gtd-notification', 'local')))
        self.assertEqual(1, len(self.service.materials(self.item['id'])))

    async def test_wrong_version_conflicts_without_progress(self):
        # Direct reservation (no worker tick): put, then a stale assess.
        version = self.service.get_item(self.item['id'])['version']
        reserved = self.control.reserve('gtd-felix', 'neg-reserve', dict(
            item_id=self.item['id'], expected_version=version, capability='prepare_private',
            bot_id='principal', purpose='Negatives', scope='Synthetic', mandate_id=self.mandate_id,
            max_cost_usd=4, max_runtime_seconds=200, max_retries=0, max_descendants=0))
        job_id = reserved['job_id']
        put = await self.client.call('gtd_command', {'job_id': job_id, 'command': {
            'operation_id': job_id + ':put', 'action': 'put_material', 'item_id': self.item['id'],
            'expected_version': version, 'fields': {'content': 'Synthetic negative text'}}})
        self.assertEqual('applied', put['status'])
        stale = await self.client.call('gtd_command', {'job_id': job_id, 'command': {
            'operation_id': job_id + ':stale', 'action': 'assess_result', 'item_id': self.item['id'],
            'expected_version': version, 'fields': {'satisfied': True, 'evidence': 'Stale synthetic claim.'}}})
        self.assertEqual('conflict', stale['status'])
        self.assertEqual('expected_version_mismatch', stale['error'])
        self.assertEqual([job_id + ':put'],
            [p['operation_id'] for p in self.control.get_job(job_id).get('progress', [])])
        fixed = await self.client.call('gtd_command', {'job_id': job_id, 'command': {
            'operation_id': job_id + ':assess', 'action': 'assess_result', 'item_id': self.item['id'],
            'expected_version': version + 1, 'fields': {'satisfied': True,
                'evidence': 'Fresh synthetic verification.'}}})
        self.assertEqual('applied', fixed['status'])
        # Foreign adoption and unknown jobs stay rejected.
        row = self.service.store.db.execute(
            'SELECT receipt FROM operations WHERE operation_id=?', (job_id + ':assess',)).fetchone()
        import json as _json
        self.assertEqual('rejected',
            self.control.record_progress('no-such-job', _json.loads(row[0]), version + 1)['status'])
        self.assertEqual('rejected',
            self.control.record_progress(job_id, {'status': 'applied'}, version + 1)['status'])

    async def test_pause_prevails_over_own_close(self):
        version = self.service.get_item(self.item['id'])['version']
        reserved = self.control.reserve('gtd-felix', 'neg-pause', dict(
            item_id=self.item['id'], expected_version=version, capability='prepare_private',
            bot_id='principal', purpose='Negatives', scope='Synthetic', mandate_id=self.mandate_id,
            max_cost_usd=4, max_runtime_seconds=200, max_retries=0, max_descendants=0))
        job_id = reserved['job_id']
        put = await self.client.call('gtd_command', {'job_id': job_id, 'command': {
            'operation_id': job_id + ':put', 'action': 'put_material', 'item_id': self.item['id'],
            'expected_version': version, 'fields': {'content': 'Synthetic pausable text'}}})
        self.assertEqual('applied', put['status'])
        paused = self.service.execute('felix', dict(operation_id='owner-pause', action='pause',
            item_id=self.item['id'], expected_version=self.service.get_item(self.item['id'])['version'],
            fields={}))
        self.assertEqual('applied', paused['status'])
        self.assertFalse(self.control.validate(job_id, 'prepare_private')['allowed'])
        self.assertIsNone(self.control.own_terminal_progress(job_id))
