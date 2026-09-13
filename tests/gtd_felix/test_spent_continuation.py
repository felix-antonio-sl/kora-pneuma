"""Spent review alone never funds another reservation (tick-level behavior).

Exact resolved-assessment case: the event-driven origin assesses (unsatisfied,
item stays active) so the continuation record is resolved with no job; a later
explicit review exhausts its cupo writing material WITHOUT a new assessment,
flipping resolution stale. Base auto-reserves from the historic origin; the
candidate blocks with a visible reason until a fresh owner direction or input.
"""
import asyncio
from datetime import datetime, timezone
from pathlib import Path
import sys
import tempfile
import unittest

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from test_orchestration import NativeFixture
from gtd_felix.application import create_app
from gtd_felix.control import ExecutionControl
from gtd_felix.mcp import MCPClient
from gtd_felix.orchestration import OrchestrationWorker
from gtd_felix.service import GTDService
from aiohttp import web


class SpentContinuationTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.service = GTDService(self.root / 'data', executor_actors=['bounded-executor'])
        self.budget = dict(period_start=datetime.now(timezone.utc).isoformat(), period_seconds=3600,
            max_cost_usd=20, max_runtime_seconds=2000, recovery_cost_usd=2, recovery_runtime_seconds=100,
            max_job_runtime_seconds=300, max_retries=0, max_descendants=1, max_active=1)
        self.control = ExecutionControl(self.service, self.budget)
        self.item = self.service.capture('felix', 'capture', 'Source-specific synthetic note')['item']
        self.control.register_bot('felix', 'bot', dict(id='principal', state='available', source_urn='urn:test:principal',
            host='synthetic', profile='fixture', capabilities=['prepare_private'], item_id=self.item['id'],
            mandate_id=None, probe_evidence='fixture://route'))
        self.config = dict(actor='gtd-felix', principal_bot_id='principal', clarification_accounts=['fixture'],
            reservation=dict(max_cost_usd=4, max_runtime_seconds=200, max_retries=0, max_descendants=1),
            poll_seconds=.01, review_interval_seconds=300)
        appconfig = dict(data_dir=str(self.root / 'data'), actors={'owner': 'felix', 'principal': 'gtd-felix', 'executors': []},
            api_tokens={'synthetic-owner-token': 'felix', 'synthetic-agent-token': 'gtd-felix'})
        self.runner = web.AppRunner(create_app(self.service, self.control, appconfig), access_log=None)
        await self.runner.setup()
        site = web.TCPSite(self.runner, '127.0.0.1', 0)
        await site.start()
        self.url = 'http://127.0.0.1:' + str(site._server.sockets[0].getsockname()[1])
        self.client = MCPClient(self.url, 'synthetic-agent-token')
        self.native = NativeFixture(self.control, self.client)
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        self.cited = {}

    async def asyncTearDown(self):
        await self.runner.cleanup()
        self.service.close()
        self.temp.cleanup()

    def make_private_action(self):
        item = self.service.get_item(self.item['id'])
        result = self.service.execute('gtd-felix', {'operation_id': 'private-intent',
            'action': 'clarify', 'item_id': item['id'], 'expected_version': item['version'],
            'fields': {'kind': 'action', 'commitment': 'committed', 'capability': 'prepare_private',
                'completion_criteria': 'Synthetic preparation verified',
                'intent_basis': {'source_item_id': item['id'], 'quote': item['text']}}})
        self.assertEqual(result['status'], 'applied', result)
        return result['item']

    def silence_source_events(self, source_id):
        for event in self.service.pending_events('gtd-review', 'local'):
            if event['payload'].get('item_id') == source_id:
                self.service.mark_event(event['event_key'], 'done')

    def drive_origin_resolved(self):
        self.make_private_action()
        return len(self.native.submissions)

    async def drive_origin_resolved_async(self):
        self.make_private_action()
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 1)
        origin = self.native.submissions[0]['job_id']
        current = self.service.get_item(self.item['id'])
        assessed = await self.client.call('gtd_command', {'job_id': origin, 'command': {
            'operation_id': 'origin-assess-open', 'action': 'assess_result', 'item_id': current['id'],
            'expected_version': current['version'], 'fields': {'satisfied': False,
                'evidence': 'Fixture assessment keeps the item open but resolved.',
                'mandate_id': self.control.get_job(origin)['mandate_id']}}})
        self.assertEqual(assessed['status'], 'applied', assessed)
        for _ in range(3):
            await self.worker.tick()
        job = self.control.get_job(origin)
        self.assertTrue(job['terminal'], job)
        self.assertEqual(job['integration'], 'integrated', job)
        item = self.service.get_item(self.item['id'])
        self.assertEqual(item['status'], 'active', item)
        self.assertTrue(self.service.work_resolution_current(item['id']))
        self.assertEqual(len(self.native.submissions), 1)
        records = [record for record in self.worker._state().get('continuations', {}).values()
                   if record.get('item_id') == item['id']]
        self.assertTrue(records)
        self.assertTrue(all(record.get('status') == 'resolved' and not record.get('job_id') for record in records))
        return origin

    def reserve_review(self, operation_id):
        version = self.service.get_item(self.item['id'])['version']
        bot = self.control.bots()[0]
        admitted = self.control.reserve('gtd-felix', operation_id, {**self.config['reservation'],
            'item_id': self.item['id'], 'expected_version': version, 'mandate_id': None,
            'capability': 'prepare_private', 'bot_id': bot['id'], 'source_versions': dict(self.cited),
            'human_instruction_source_ids': list(self.cited),
            'purpose': 'Spent fixture review', 'scope': 'Bounded synthetic preparation'})
        self.assertEqual(admitted['status'], 'reserved', admitted)
        return admitted['job_id']

    async def settle(self, job_id, status, runtime):
        await self.native.submit(job_id, 'spent fixture prompt')
        observation = {'native_identity': self.native.native(job_id), 'native_status': status, 'terminal': True,
            'cost_usd': .1, 'runtime_seconds': runtime, 'evidence_reference': 'fixture://spent/' + job_id}
        self.assertEqual(self.control.observe(job_id, observation)['status'], 'recorded')
        for _ in range(4):
            await self.worker.tick()
        settled = self.control.get_job(job_id)
        self.assertTrue(settled['terminal'], settled)
        return settled

    def purposes(self, since=0):
        jobs = {}
        for sub in self.native.submissions[since:]:
            jobs[sub['job_id']] = self.control.get_job(sub['job_id'])['purpose']
        return jobs

    def spent_blocker_present(self):
        records = self.worker._state().get('continuations', {})
        return any(record.get('blocker') == 'spent_review_without_new_direction'
                   and record.get('item_id') == self.item['id']
                   for record in records.values())

    async def test_spent_material_only_review_blocks_first_continuation(self):
        await self.drive_origin_resolved_async()
        spent = self.reserve_review('spent-op')
        before = len(self.native.submissions)
        settled = await self.settle(spent, 'cancelled', self.config['reservation']['max_runtime_seconds'])
        self.assertEqual(settled['integration'], 'discarded', settled)
        self.assertGreaterEqual(settled['observed_runtime_seconds'], settled['max_runtime_seconds'])
        self.assertEqual(len(self.native.submissions), before + 1)
        for _ in range(4):
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), before + 1)
        self.assertTrue(self.spent_blocker_present())

    async def test_fresh_owner_direction_rearms_continuation(self):
        await self.drive_origin_resolved_async()
        spent = self.reserve_review('spent-op')
        before = len(self.native.submissions)
        await self.settle(spent, 'cancelled', self.config['reservation']['max_runtime_seconds'])
        self.assertEqual(len(self.native.submissions), before + 1)
        for _ in range(4):
            await self.worker.tick()
        edited = self.service.execute('felix', {'operation_id': 'owner-new-direction', 'action': 'edit',
            'item_id': self.item['id'], 'expected_version': self.service.get_item(self.item['id'])['version'],
            'fields': {'priority': 2}})
        self.assertEqual(edited['status'], 'applied', edited)
        for _ in range(4):
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), before + 2)

    async def test_fresh_request_review_advances_by_authorized_path(self):
        await self.drive_origin_resolved_async()
        spent = self.reserve_review('spent-op')
        before = len(self.native.submissions)
        await self.settle(spent, 'cancelled', self.config['reservation']['max_runtime_seconds'])
        self.assertEqual(len(self.native.submissions), before + 1)
        for _ in range(4):
            await self.worker.tick()
        item = self.service.get_item(self.item['id'])
        requested = self.service.execute('felix', {'operation_id': 'owner-explicit-review',
            'action': 'request_review', 'item_id': item['id'], 'expected_version': item['version'], 'fields': {}})
        self.assertEqual(requested['status'], 'applied', requested)
        seen = {}
        for _ in range(8):
            await self.worker.tick()
            seen = self.purposes(before + 1)
            if 'GTD revisión y preparación' in seen.values():
                break
        self.assertIn('GTD revisión y preparación', seen.values())
        self.assertGreaterEqual(len(self.native.submissions), before + 2)

    async def test_early_human_stop_never_counts_as_spent(self):
        guard = getattr(self.worker, '_spent_review_blocks', None)
        if guard is None:
            self.skipTest('spent guard absent on this runtime')
        await self.drive_origin_resolved_async()
        stopped = self.reserve_review('stopped-op')
        before = len(self.native.submissions)
        await self.native.submit(stopped, 'stopped fixture prompt')
        self.assertEqual(len(self.native.submissions), before + 1)
        self.assertEqual(self.control.request_stop('felix', 'human-stop', stopped)['status'], 'stop_requested')
        observation = {'native_identity': self.native.native(stopped), 'native_status': 'cancelled', 'terminal': True,
            'cost_usd': .1, 'runtime_seconds': 5, 'evidence_reference': 'fixture://stopped/' + stopped}
        self.assertEqual(self.control.observe(stopped, observation)['status'], 'recorded')
        for _ in range(4):
            await self.worker.tick()
        settled = self.control.get_job(stopped)
        self.assertTrue(settled['terminal'], settled)
        self.assertLess(settled['observed_runtime_seconds'], settled['max_runtime_seconds'])
        item = self.service.get_item(self.item['id'])
        basis = self.service.work_input_basis(item['id'])
        state = self.control._load()
        self.assertFalse(guard(state, item, basis, {}))
        self.assertFalse(self.spent_blocker_present())

    async def test_known_source_revision_rearms_continuation(self):
        source = self.service.capture('felix', 'known-source', 'Numerical source v1')['item']
        self.native.material_sources = {source['id']: 1}
        self.cited = {source['id']: source['version']}
        self.silence_source_events(source['id'])
        await self.drive_origin_resolved_async()
        spent = self.reserve_review('spent-op')
        before = len(self.native.submissions)
        await self.settle(spent, 'cancelled', self.config['reservation']['max_runtime_seconds'])
        self.assertEqual(len(self.native.submissions), before + 1)
        for _ in range(4):
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), before + 1)
        revised = self.service.execute('felix', {'operation_id': 'known-source-revision',
            'action': 'edit', 'item_id': source['id'], 'expected_version': source['version'],
            'fields': {'text': 'Numerical source corrected'}})
        self.assertEqual(revised['status'], 'applied', revised)
        self.silence_source_events(source['id'])
        for _ in range(4):
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), before + 2)
        self.assertEqual(self.control.get_job(self.native.submissions[-1]['job_id'])['item_id'], self.item['id'])

    async def test_first_citation_without_change_does_not_rearm(self):
        extra = self.service.capture('felix', 'cited-only-source', 'A reference cited without changes')['item']
        self.silence_source_events(extra['id'])
        await self.drive_origin_resolved_async()
        spent = self.reserve_review('spent-op')
        before = len(self.native.submissions)
        await self.settle(spent, 'cancelled', self.config['reservation']['max_runtime_seconds'])
        self.assertEqual(len(self.native.submissions), before + 1)
        for _ in range(4):
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), before + 1)
        citing = self.reserve_review('citing-op')
        self.native.material_sources = {extra['id']: 1}
        await self.settle(citing, 'cancelled', self.config['reservation']['max_runtime_seconds'])
        self.assertEqual(len(self.native.submissions), before + 2)
        for _ in range(4):
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), before + 2)
        self.assertTrue(self.spent_blocker_present())

    async def test_tied_exhaustions_need_change_against_each(self):
        guard = getattr(self.worker, '_spent_review_blocks', None)
        if guard is None:
            self.skipTest('spent guard absent on this runtime')
        item = self.make_private_action()
        source = self.service.capture('felix', 'tie-source', 'Tie source v1')['item']
        self.silence_source_events(source['id'])
        version = self.service.get_item(item['id'])['version']

        def spent_job(job_id, bases):
            return {'id': job_id, 'item_id': item['id'], 'terminal': True, 'integration': 'discarded',
                    'max_runtime_seconds': 200, 'observed_runtime_seconds': 200,
                    'expected_version': version, 'progress': [{'item_id': item['id'], 'version': version}],
                    'item_bases': {}, 'source_bases': bases}

        real = self.control._basis(source['id'])
        old = {'revision': 'stale-synthetic-marker'}
        jobs_ab = {'job-a': spent_job('job-a', {source['id']: old}),
                   'job-b': spent_job('job-b', {source['id']: real})}
        jobs_ba = {'job-b': jobs_ab['job-b'], 'job-a': jobs_ab['job-a']}
        inputs = {source['id']: None}
        self.assertTrue(guard({'jobs': jobs_ab}, item, inputs, {}))
        self.assertTrue(guard({'jobs': jobs_ba}, item, inputs, {}))
        requested = self.service.execute('felix', {'operation_id': 'tie-review',
            'action': 'request_review', 'item_id': item['id'], 'expected_version': item['version'], 'fields': {}})
        self.assertEqual(requested['status'], 'applied', requested)
        self.assertTrue(guard({'jobs': jobs_ab}, item, inputs, {}))
        revised = self.service.execute('felix', {'operation_id': 'tie-revision', 'action': 'edit',
            'item_id': source['id'], 'expected_version': source['version'], 'fields': {'text': 'Tie source v2'}})
        self.assertEqual(revised['status'], 'applied', revised)
        self.silence_source_events(source['id'])
        self.assertFalse(guard({'jobs': jobs_ab}, item, inputs, {}))
        self.assertFalse(guard({'jobs': jobs_ba}, item, inputs, {}))
