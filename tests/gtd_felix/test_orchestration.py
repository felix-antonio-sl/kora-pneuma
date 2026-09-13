"""Synthetic native adapter; actual MCP HTTP/domain/events/materials underneath."""
import asyncio
from datetime import datetime, timezone
import json
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
from gtd_felix.mcp import MCPClient
from gtd_felix.orchestration import OrchestrationWorker
from gtd_felix.service import GTDService


class NativeFixture:
    """Models transport windows; tool effects really cross authenticated HTTP."""
    def __init__(self, control, client):
        self.control, self.client = control, client
        self.submissions, self.runs = [], {}
        self.down = self.lost_response = self.keep_running = False
        self.polls = self.reconciliations = 0
        self.complete_criterion = False
        self.material_sources = {}
        self.delegate = False
        self.no_progress = self.clarify_only = False

    async def discover(self, bot_id):
        return {'status': 'ready', 'capabilities': ['submit', 'poll', 'stop']}

    def native(self, job_id):
        return {'provider': 'fixture', 'host': 'synthetic', 'profile': 'fixture', 'id': job_id}

    async def submit(self, job_id, prompt, durable=False):
        self.submissions.append({'job_id': job_id, 'prompt': prompt, 'durable': durable})
        if self.down:
            raise asyncio.TimeoutError()
        if job_id in self.runs:
            raise AssertionError('blind native resend')
        self.control.record_dispatch(job_id, self.native(job_id))
        self.runs[job_id] = {'status': 'running'}
        job = self.control.get_job(job_id)
        if self.no_progress:
            self.runs[job_id]['output'] = 'No pude acceder a las herramientas.'
            return {'status': 'submitted', 'job_id': job_id, 'native_id': job_id}
        item = await self.client.call('gtd_read', {'view': 'item', 'item_id': job['item_id']})
        if item['kind'] == 'capture':
            receipt = await self.client.call('gtd_command', {'job_id': job_id, 'command': {
                'operation_id': job_id + ':clarify', 'action': 'clarify', 'item_id': item['id'],
                'expected_version': item['version'], 'fields': {'kind': 'reference', 'commitment': 'proposed'}}})
            if receipt.get('status') != 'applied':
                raise AssertionError(receipt)
            item = receipt['item']
        if self.clarify_only:
            self.runs[job_id]['output'] = 'Clasificación actualizada.'
            return {'status': 'submitted', 'job_id': job_id, 'native_id': job_id}
        receipt = await self.client.call('gtd_command', {'job_id': job_id, 'command': {
            'operation_id': job_id + ':material', 'action': 'put_material', 'item_id': item['id'],
            'expected_version': item['version'], 'fields': {'content': 'Synthetic preparation for: ' + item['title'],
                'source_versions': self.material_sources, 'mandate_id': job['mandate_id']}}})
        if receipt.get('status') != 'applied':
            raise AssertionError(receipt)
        if self.delegate:
            self.delegate = False
            current = receipt['item']
            delegated = await self.client.call('gtd_dispatch', {'job_id': job_id, 'operation_id': job_id + ':delegate',
                'request': {'item_id': current['id'], 'expected_version': current['version'], 'mandate_id': job['mandate_id'],
                    'capability': job['capability'], 'bot_id': job['bot_id'], 'purpose': 'Durable synthetic contribution',
                    'scope': 'Bounded contribution', 'max_cost_usd': 1, 'max_runtime_seconds': 50, 'max_retries': 0, 'max_descendants': 0}})
            if delegated.get('status') != 'reserved':
                raise AssertionError(delegated)
            self.child_id = delegated['job_id']
        if self.complete_criterion:
            current = receipt['item']
            completed = await self.client.call('gtd_command', {'job_id': job_id, 'command': {
                'operation_id': job_id + ':assess', 'action': 'assess_result', 'item_id': current['id'],
                'expected_version': current['version'], 'fields': {'satisfied': True,
                    'evidence': 'Fixture explicitly verified the declared synthetic acceptance criterion.',
                    'mandate_id': job['mandate_id']}}})
            if completed.get('status') != 'applied':
                raise AssertionError(completed)
        self.runs[job_id]['output'] = 'Prepared result for: ' + item['title']
        if self.lost_response:
            self.lost_response = False
            raise asyncio.TimeoutError()
        return {'status': 'submitted', 'job_id': job_id, 'native_id': job_id}

    async def poll(self, job_id):
        self.polls += 1
        if self.down or job_id not in self.runs:
            return {'status': 'uncertain', 'job_id': job_id}
        status = 'cancelled' if self.runs[job_id]['status'] == 'cancelled' else ('running' if self.keep_running else 'completed')
        observation = {'native_identity': self.native(job_id), 'native_status': status, 'terminal': status != 'running',
            'cost_usd': .25, 'runtime_seconds': 5, 'evidence_reference': 'fixture://native/' + job_id}
        if not self.control.get_job(job_id)['terminal']:
            recorded = self.control.observe(job_id, observation)
            if recorded['status'] != 'recorded':
                raise AssertionError(recorded)
        return {'status': 'observed', 'job_id': job_id, 'terminal': observation['terminal'],
            'native_status': status, 'output': self.runs[job_id].get('output'), 'observation': observation}

    async def reconcile(self, job_id):
        self.reconciliations += 1
        return await self.poll(job_id)

    async def stop(self, job_id):
        if job_id in self.runs:
            self.runs[job_id]['status'] = 'cancelled'
        return {'status': 'stop_requested', 'job_id': job_id}


class OrchestrationTests(unittest.IsolatedAsyncioTestCase):
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
        self.event = self.service.ingest_event({'provider': 'gtd-clarification', 'account': 'fixture',
            'external_id': self.item['id'], 'revision': '1', 'payload': {'item_id': self.item['id'], 'reason': 'clarification_pending'}})

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

    async def test_principal_prompt_omits_only_nested_assessment_snapshots(self):
        self.native.keep_running = True
        await self.worker.tick()
        job = self.control.get_job(self.native.submissions[0]['job_id'])
        item = {**self.service.get_item(self.item['id']), 'assessments': [{
            'actor':'felix', 'evidence':'RETAIN_OBSERVATION', 'gap':'RETAIN_GAP',
            'material_id':'EXACT_MATERIAL', 'material_version':2,
            'resolution_basis':{'snapshot':'DUPLICATED_SNAPSHOT_'*1000},
            'material_basis':[{'snapshot':'DUPLICATED_MATERIAL_'*1000}]}]}
        before = json.dumps(item, sort_keys=True)
        prompt = self.worker._prompt(job, [], item)
        self.assertNotIn('DUPLICATED_', prompt)
        for marker in ('RETAIN_OBSERVATION','RETAIN_GAP','EXACT_MATERIAL',job['id'],item['text']):
            self.assertIn(marker,prompt)
        self.assertIn('full_record',prompt)
        self.assertEqual(before,json.dumps(item,sort_keys=True))

    async def test_parent_source_change_refreshes_existing_child_once_across_restart(self):
        self.native.clarify_only = True
        await self.worker.tick()
        await self.worker.tick()
        parent = self.service.get_item(self.item['id'])
        child = self.service.execute('gtd-felix', {'operation_id': 'dependent-preparation', 'action': 'derive',
            'item_id': parent['id'], 'expected_version': parent['version'], 'fields': {
                'kind': 'action', 'title': 'Private proposed package', 'capability': 'prepare_private',
                'commitment': 'proposed', 'source_versions': {parent['id']: 1}}})['item']
        for event in self.service.pending_events('gtd-review', 'local'):
            if event['payload'].get('item_id') == child['id']:
                self.service.mark_event(event['event_key'], 'done')
        original_submit = self.native.submit
        async def refresh(job_id, prompt, durable=False):
            receipt = await original_submit(job_id, prompt, durable)
            job = self.control.get_job(job_id)
            self.assertEqual(job['item_id'], parent['id'])
            current = self.service.get_item(child['id'])
            updated = await self.client.call('gtd_command', {'job_id': job_id, 'command': {
                'operation_id': 'refresh-event-r2', 'action': 'plan', 'item_id': current['id'],
                'expected_version': current['version'], 'fields': {'source_versions': {parent['id']: 2}}}})
            self.assertEqual(updated['status'], 'applied', updated)
            return receipt
        self.native.submit = refresh
        self.service.revise_source('felix', 'new-source-event', parent['id'], source={'revision': '2'}, text='Earlier meeting time')
        await self.worker.tick()
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)
        self.assertEqual(self.service.get_item(child['id'])['source_versions'], {parent['id']: 2})
        for _ in range(3):
            self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)
        self.assertEqual(len(self.service.query()), 2)

    async def test_private_continuation_g10_has_one_durable_followup(self):
        self.make_private_action()
        await self.worker.tick()
        await self.worker.tick()
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)
        for _ in range(4):
            self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)
        item = self.service.get_item(self.item['id'])
        self.assertEqual(item['status'], 'active')
        self.assertEqual(len(self.service.materials(item['id'])), 2)
        self.assertFalse(item.get('result_gap'))
        gaps = self.service.review_state()['operational_gaps']
        self.assertEqual(gaps[0]['reason'], 'continuation_without_resolution')
        self.assertTrue(self.service.review_state()['notification_allowed'])

    async def prepare_pending_continuation(self):
        self.make_private_action()
        await self.worker.tick()
        self.worker.config['reservation'] = {**self.config['reservation'], 'max_cost_usd': 100}
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 1)
        self.assertEqual(self.control.get_job(self.native.submissions[0]['job_id'])['integration'], 'integrated')
        self.assertEqual(len(self.service.review_state()['operational_gaps']), 1)

    async def test_private_continuation_assessment_closes_authentically(self):
        await self.prepare_pending_continuation()
        self.native.complete_criterion = True
        self.worker.config['reservation'] = self.config['reservation']
        await self.worker.tick()
        await self.worker.tick()
        item = self.service.get_item(self.item['id'])
        self.assertEqual(item['status'], 'done')
        self.assertEqual(item['assessments'][-1]['actor'], 'gtd-felix')
        self.assertEqual(len(self.native.submissions), 2)
        self.assertEqual(self.service.review_state()['operational_gaps'], [])
        self.assertEqual(self.control.budget()['active'], 0)

    async def test_private_continuation_survives_global_review_and_budget_wait(self):
        await self.prepare_pending_continuation()
        budget = self.control.budget()
        reviewed = self.service.execute('gtd-felix', {'operation_id': 'global-review', 'action': 'review',
            'fields': {'source_coverage': {i['item_id']: len(self.service.get_item(i['item_id'])['source_revisions'])
                for i in self.service.review_state()['source_coverage']}}})
        self.assertEqual(reviewed['status'], 'applied', reviewed)
        self.assertEqual(len(reviewed['review']['operational_gaps']), 1)
        for _ in range(3):
            await self.worker.tick()
        self.assertEqual(self.control.budget(), budget)
        self.assertEqual(len(self.native.submissions), 1)
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        await self.worker.tick()
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)
        self.assertEqual(len(self.service.review_state()['operational_gaps']), 1)

    async def test_private_continuation_external_source_and_human_change_renew_once(self):
        self.make_private_action()
        for _ in range(4):
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)
        result = self.service.revise_source('felix', 'new-source', self.item['id'],
            {'provider': 'synthetic', 'revision': '2'}, text='Updated synthetic source')
        self.assertEqual(result['status'], 'applied', result)
        for _ in range(4):
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 3)
        item = self.service.get_item(self.item['id'])
        edited = self.service.execute('felix', {'operation_id': 'human-priority', 'action': 'edit',
            'item_id': item['id'], 'expected_version': item['version'], 'fields': {'priority': 2}})
        self.assertEqual(edited['status'], 'applied', edited)
        for _ in range(4):
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 4)

    async def continuation_reserve_crash(self, after):
        await self.prepare_pending_continuation()
        self.worker.config['reservation'] = self.config['reservation']
        reserve = self.control.reserve
        def crashed(actor, operation_id, request):
            if after:
                reserve(actor, operation_id, request)
            raise RuntimeError('synthetic process interruption')
        with patch.object(self.control, 'reserve', side_effect=crashed):
            with self.assertRaisesRegex(RuntimeError, 'synthetic process interruption'):
                await self.worker.tick()
        jobs_before = set(self.control._load()['jobs'])
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        for _ in range(4):
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)
        jobs_after = set(self.control._load()['jobs'])
        self.assertEqual(len(jobs_after), 2)
        self.assertEqual(len(jobs_after - jobs_before), 0 if after else 1)
        self.assertEqual(self.control.budget()['active'], 0)
        self.assertEqual(sum(j['charged_cost_usd'] for j in self.control._load()['jobs'].values()), .5)

    async def test_private_continuation_recovers_before_reserve(self):
        await self.continuation_reserve_crash(False)

    async def test_private_continuation_recovers_after_reserve(self):
        await self.continuation_reserve_crash(True)

    async def test_private_continuation_pause_decision_return_and_dependencies_block(self):
        await self.prepare_pending_continuation()
        self.worker.config['reservation'] = self.config['reservation']
        dependency = self.service.capture('felix', 'dependency', 'Human work')['item']
        for event in self.service.pending_events('gtd-review', 'local'):
            if event['payload'].get('item_id') == dependency['id']:
                self.service.mark_event(event['event_key'], 'done')
        for index, fields in enumerate(({'status': 'paused'}, {'status': 'postponed'},
                {'status': 'waiting'}, {'status': 'active', 'decision_needed': True, 'decision_question': 'Which result?'},
                {'decision_needed': False, 'review_at': '2099-01-01'}, {'review_at': None, 'depends_on': [dependency['id']]})):
            item = self.service.get_item(self.item['id'])
            if 'status' in fields:
                # The domain has no public pause/wait command; persist the same
                # authenticated transition used by existing boundary regressions.
                with self.service.store.transaction():
                    current, versions = self.service._item(item['id'])
                    receipt = self.service._apply_updates('felix', 'block-' + str(index),
                        'synthetic-state', current, versions, fields)
            else:
                receipt = self.service.execute('felix', {'operation_id': 'block-' + str(index), 'action': 'edit',
                    'item_id': item['id'], 'expected_version': item['version'], 'fields': fields})
            self.assertEqual(receipt['status'], 'applied', receipt)
            await self.worker.tick()
            self.assertEqual(len(self.native.submissions), 1)
        self.assertEqual(self.service.review_state()['operational_gaps'][-1]['blocker'], 'dependencies_incomplete')

    async def test_private_continuation_never_upgrades_to_new_mandate(self):
        await self.prepare_pending_continuation()
        item = self.service.get_item(self.item['id'])
        grant = self.service.execute('felix', {'operation_id': 'later-grant', 'action': 'grant_mandate',
            'item_id': item['id'], 'expected_version': item['version'], 'fields': {'scope_item_id': item['id'],
                'actors': ['gtd-felix'], 'capabilities': ['prepare_private', 'local_work'],
                'completion_criteria': item['completion_criteria']}})
        self.assertEqual(grant['status'], 'applied', grant)
        self.worker.config['reservation'] = self.config['reservation']
        await self.worker.tick()
        job = self.control.get_job(self.native.submissions[-1]['job_id'])
        self.assertEqual(job['capability'], 'prepare_private')
        self.assertIsNone(job['mandate_id'])
        self.assertEqual(job['actor'], 'gtd-felix')

    async def test_private_continuation_g10_independent_material_source_changes(self):
        source = self.service.capture('felix', 'independent-source', 'Numerical source v1')['item']
        self.native.material_sources = {source['id']: 1}
        for event in self.service.pending_events('gtd-review', 'local'):
            if event['payload'].get('item_id') == source['id']:
                self.service.mark_event(event['event_key'], 'done')
        self.make_private_action()
        for _ in range(4):
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)
        self.assertNotIn(source['id'], self.service.get_item(self.item['id']).get('source_versions', {}))
        revised = self.service.execute('felix', {'operation_id': 'correct-source-text', 'action': 'edit',
            'item_id': source['id'], 'expected_version': source['version'], 'fields': {'text': 'Numerical source corrected'}})
        self.assertEqual(revised['status'], 'applied', revised)
        self.assertEqual(len(revised['item']['source_revisions']), 1)
        # Isolate target admissions: the source is human-owned unrelated intake.
        for event in self.service.pending_events('gtd-review', 'local'):
            if event['payload'].get('item_id') == source['id']:
                self.service.mark_event(event['event_key'], 'done')
        for _ in range(4):
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 3)
        self.assertEqual(self.control.get_job(self.native.submissions[-1]['job_id'])['item_id'], self.item['id'])

    async def test_private_continuation_new_own_material_source_does_not_renew_quota(self):
        await self.prepare_pending_continuation()
        source = self.service.capture('felix', 'additional-source', 'An additional reference')['item']
        self.native.material_sources = {source['id']: 1}
        for event in self.service.pending_events('gtd-review', 'local'):
            if event['payload'].get('item_id') == source['id']:
                self.service.mark_event(event['event_key'], 'done')
        self.worker.config['reservation'] = self.config['reservation']
        for _ in range(5):
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)
        changed = self.service.execute('felix', {'operation_id': 'new-cited-source-change', 'action': 'edit',
            'item_id': source['id'], 'expected_version': source['version'], 'fields': {'text': 'Later external correction'}})
        self.assertEqual(changed['status'], 'applied', changed)
        for event in self.service.pending_events('gtd-review', 'local'):
            if event['payload'].get('item_id') == source['id']:
                self.service.mark_event(event['event_key'], 'done')
        for _ in range(4):
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 3)

    async def test_private_continuation_past_starts_at_and_due_return_do_not_stall(self):
        await self.prepare_pending_continuation()
        item = self.service.get_item(self.item['id'])
        edited = self.service.execute('felix', {'operation_id': 'past-dates', 'action': 'edit',
            'item_id': item['id'], 'expected_version': item['version'],
            'fields': {'starts_at': '2000-01-01T09:00:00+00:00', 'review_at': '2000-01-02T09:00:00+00:00'}})
        self.assertEqual(edited['status'], 'applied', edited)
        self.worker.config.update(reservation=self.config['reservation'], review_interval_seconds=0)
        for _ in range(4):
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)

    async def test_private_continuation_revoked_origin_mandate_blocks(self):
        item = self.make_private_action()
        grant = self.service.execute('felix', {'operation_id': 'origin-grant', 'action': 'grant_mandate',
            'item_id': item['id'], 'expected_version': item['version'], 'fields': {'scope_item_id': item['id'],
                'actors': ['gtd-felix'], 'capabilities': ['prepare_private', 'local_work'],
                'completion_criteria': item['completion_criteria']}})
        self.assertEqual(grant['status'], 'applied', grant)
        self.control.register_bot('felix', 'local-bot', dict(self.control.bots()[0], capabilities=['prepare_private', 'local_work']))
        await self.worker.tick()
        self.worker.config['reservation'] = {**self.config['reservation'], 'max_cost_usd': 100}
        await self.worker.tick()
        origin = self.control.get_job(self.native.submissions[0]['job_id'])
        self.assertEqual(origin['capability'], 'local_work')
        item = self.service.get_item(item['id'])
        revoked = self.service.execute('felix', {'operation_id': 'origin-revoke', 'action': 'revoke_mandate',
            'item_id': item['id'], 'expected_version': item['version'], 'fields': {'mandate_id': grant['mandate']['id']}})
        self.assertEqual(revoked['status'], 'applied', revoked)
        self.worker.config['reservation'] = self.config['reservation']
        for _ in range(3):
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 1)
        self.assertEqual(self.service.review_state()['operational_gaps'][-1]['blocker'], 'mandate_revoked')

    async def test_private_continuation_recovery_required_never_admits(self):
        await self.prepare_pending_continuation()
        with self.service.store.transaction():
            self.service._set_meta('recovery_required', True)
        self.worker.config['reservation'] = self.config['reservation']
        before = self.control.budget()
        for _ in range(3):
            self.assertEqual((await self.worker.tick())['reason'], 'recovery_required')
        self.assertEqual(len(self.native.submissions), 1)
        self.assertEqual(self.control.budget(), before)

    async def test_private_continuation_covers_only_authentic_touched_child(self):
        original_submit = self.native.submit
        children = []
        async def with_child(job_id, prompt, durable=False):
            response = await original_submit(job_id, prompt, durable)
            if children:
                return response
            item = self.service.get_item(self.item['id'])
            child = await self.client.call('gtd_command', {'job_id': job_id, 'command': {
                'operation_id': 'authentic-child', 'action': 'derive', 'item_id': item['id'],
                'expected_version': item['version'], 'fields': {'kind': 'action',
                    'title': 'Prepare the authorized child', 'capability': 'prepare_private',
                    'completion_criteria': 'Child material checked'}}})
            self.assertEqual(child['status'], 'applied', child)
            children.append(child['item']['id'])
            return response
        self.native.submit = with_child
        for _ in range(4):
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)
        origin = self.control.get_job(self.native.submissions[0]['job_id'])
        continuation = self.control.get_job(self.native.submissions[1]['job_id'])
        self.assertEqual(continuation['item_id'], children[0])
        self.assertEqual(continuation['capability'], origin['capability'])
        self.assertEqual(continuation['mandate_id'], origin['mandate_id'])
        self.assertEqual(self.service.review_state()['operational_gaps'][0]['item_id'], children[0])

    async def test_private_continuation_owner_future_return_resolves_operational_gap(self):
        await self.prepare_pending_continuation()
        submit = self.native.submit
        async def with_return(job_id, prompt, durable=False):
            result = await submit(job_id, prompt, durable)
            item = self.service.get_item(self.item['id'])
            receipt = self.service.execute('felix', {
                'operation_id': 'persist-return', 'action': 'edit', 'item_id': item['id'],
                'expected_version': item['version'], 'fields': {'review_at': '2099-01-01T09:00:00+00:00'}})
            self.assertEqual(receipt['status'], 'applied', receipt)
            return result
        self.native.submit = with_return
        self.worker.config['reservation'] = self.config['reservation']
        for _ in range(4):
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)
        self.assertEqual(self.service.get_item(self.item['id'])['status'], 'active')
        self.assertEqual(self.service.review_state()['operational_gaps'], [])
        self.assertEqual(self.service.review_state()['returns'][0]['review_at'], '2099-01-01T09:00:00+00:00')

    async def test_terminal_child_correction_resolves_pending_and_historical_run(self):
        await self.worker.tick()
        job_id = self.native.submissions[0]['job_id']
        root = self.service.get_item(self.item['id'])
        child = await self.client.call('gtd_command', {'job_id': job_id, 'command': {
            'operation_id': 'terminal-child', 'action': 'derive', 'item_id': root['id'],
            'expected_version': root['version'], 'fields': {'kind': 'action',
                'title': 'Human-owned room confirmation', 'capability': 'prepare_private'}}})
        self.assertEqual(child['status'], 'applied', child)
        child = child['item']
        changed = self.service.execute('felix', dict(operation_id='human-room-done', action='done',
            item_id=child['id'], expected_version=child['version'], fields={}))
        self.assertEqual(changed['status'], 'applied', changed)
        await self.worker.tick()
        job = self.control.get_job(job_id)
        self.assertEqual(job['integration'], 'discarded')
        self.assertEqual(job['integration_error'], 'stale_descendant_version')
        self.assertNotIn(job_id, [j['id'] for j in self.control.pending()])
        self.assertEqual(self.service.get_item(child['id'])['status'], 'done')
        self.assertEqual(len(self.service.materials(root['id'])), 1)
        # Reconstruct the old persisted orphan, then recover without native resend.
        with self.service.store.transaction():
            state = self.control._load()
            state['jobs'][job_id]['integration'] = 'pending'
            state['jobs'][job_id].pop('integration_error')
            self.control._save(state)
        state = self.worker._state()
        state['runs'][job_id]['phase'] = 'done'
        state['runs'][job_id]['result_status'] = 'rejected'
        self.worker._save(state)
        submissions = len(self.native.submissions)
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        await self.worker.tick()
        await self.worker.tick()
        self.assertEqual(self.control.get_job(job_id)['integration'], 'discarded')
        self.assertEqual(len(self.native.submissions), submissions)
        self.assertEqual(self.worker._state()['runs'][job_id]['error'], 'stale_descendant_version')
        # New input is admitted separately, retaining the human completion and old material.
        self.service.ingest_event({'provider': 'gtd-review', 'account': 'local',
            'external_id': 'continuation-after-discard', 'revision': '1',
            'payload': {'item_id': root['id'], 'reason': 'routed_human_instruction'}})
        await self.worker.tick()
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), submissions + 1)
        new_job = self.native.submissions[-1]['job_id']
        self.assertEqual(self.control.get_job(new_job)['integration'], 'integrated')
        self.assertEqual(self.service.get_item(child['id'])['status'], 'done')
        self.assertEqual(len(self.service.materials(root['id'])), 2)

    async def test_terminal_transient_rejection_remains_retryable(self):
        await self.worker.tick()
        job_id = self.native.submissions[0]['job_id']
        # Terminal observation is already trustworthy; domain is temporarily in recovery.
        await self.native.poll(job_id)
        with self.service.store.transaction():
            self.service.store.db.execute("INSERT OR REPLACE INTO metadata VALUES('recovery_required', 'true')")
        await self.worker.tick()
        self.assertEqual(self.control.get_job(job_id)['integration'], 'pending')
        run = self.worker._state()['runs'][job_id]
        self.assertEqual(run['phase'], 'integration_pending')
        self.assertEqual(run['error'], 'recovery_required')
        self.assertTrue(self.service.pending_events('gtd-clarification', 'fixture'))
        with self.service.store.transaction():
            self.service.store.db.execute("DELETE FROM metadata WHERE key='recovery_required'")
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        await self.worker.tick()
        self.assertEqual(self.control.get_job(job_id)['integration'], 'integrated')
        self.assertEqual(len(self.native.submissions), 1)
        self.assertEqual(len(self.service.materials(self.item['id'])), 1)

    async def test_suspended_ticks_preserve_pending_capture_without_admission_churn(self):
        bot = self.control.bots()[0]
        self.control.register_bot('felix', 'pause-bot', dict(bot, state='suspended'))
        before = len(self.control._load()['operations'])
        await self.worker.tick()
        await self.worker.tick()
        self.assertEqual(len(self.control._load()['operations']), before)
        self.assertEqual(self.worker._state().get('admissions', {}), {})
        self.assertEqual(self.worker._state()['attempts'], {})
        self.assertEqual(self.service.get_item(self.item['id'])['kind'], 'capture')
        self.assertEqual(len(self.service.pending_events('gtd-clarification', 'fixture')), 1)
        self.assertEqual(self.native.submissions, [])
        self.control.register_bot('felix', 'resume-bot', dict(bot, state='available'))
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 1)

    async def test_event_to_mcp_to_persisted_material_and_return_without_self_loop(self):
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 1)
        self.assertIn(self.item['title'], self.native.submissions[0]['prompt'])
        self.assertEqual(self.service.get_item(self.item['id'])['kind'], 'reference')
        self.assertEqual(len(self.service.materials(self.item['id'])), 1)
        await self.worker.tick()
        job_id = self.native.submissions[0]['job_id']
        self.assertEqual(self.control.get_job(job_id)['integration'], 'integrated')
        self.assertEqual(len(self.service.materials(self.item['id'])), 1)
        self.assertEqual(len(self.service.pending_events('gtd-notification', 'local')), 1)
        self.assertEqual(self.service.pending_events('gtd-clarification', 'fixture'), [])
        await self.worker.tick()
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 1)
        self.assertNotEqual(self.service.get_item(self.item['id'])['status'], 'done')
        self.assertEqual(self.service.get_item(self.item['id'])['commitment'], 'proposed')

    async def test_principal_error_output_is_no_domain_progress_not_material(self):
        self.native.no_progress = True
        await self.worker.tick()
        job = self.native.submissions[0]['job_id']
        await self.worker.tick()
        self.assertEqual(self.service.materials(self.item['id']), [])
        self.assertEqual(self.service.get_item(self.item['id'])['kind'], 'capture')
        self.assertEqual(self.control.get_job(job)['integration'], 'no_domain_progress')
        notices = self.service.pending_events('gtd-notification', 'local')
        self.assertEqual(len(notices), 1)
        self.assertEqual(notices[0]['payload']['kind'], 'no_domain_progress')
        self.assertNotIn('Material preparado', notices[0]['payload']['text'])
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 1)
        self.assertEqual(len(self.service.pending_events('gtd-notification', 'local')), 1)

    async def test_principal_clarification_is_real_progress_without_material(self):
        self.native.clarify_only = True
        await self.worker.tick()
        job = self.native.submissions[0]['job_id']
        await self.worker.tick()
        self.assertEqual(self.service.materials(self.item['id']), [])
        self.assertEqual(self.service.get_item(self.item['id'])['kind'], 'reference')
        self.assertEqual(self.control.get_job(job)['integration'], 'integrated')
        self.assertEqual(self.control.get_job(job)['domain_operation_id'], job + ':clarify')
        self.assertNotEqual(self.service.get_item(self.item['id'])['status'], 'done')

    async def test_principal_malformed_output_does_not_fabricate_progress(self):
        self.native.no_progress = True
        await self.worker.tick()
        job = self.native.submissions[0]['job_id']
        self.native.runs[job]['output'] = {'unexpected': 'not a native textual result'}
        await self.worker.tick()
        self.assertEqual(self.service.materials(self.item['id']), [])
        self.assertEqual(self.control.get_job(job)['integration'], 'no_domain_progress')

    async def test_restart_after_dispatch_before_response_recovers_exact_native_run(self):
        self.native.lost_response = True
        await self.worker.tick()
        job = self.native.submissions[0]['job_id']
        self.assertEqual(self.worker._state()['runs'][job]['phase'], 'uncertain')
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        await self.worker.tick()
        self.assertEqual(self.native.reconciliations, 1)
        self.assertEqual(len(self.native.submissions), 1)
        self.assertEqual(self.control.get_job(job)['integration'], 'integrated')

    async def test_llm_down_keeps_capture_and_controls_independent(self):
        self.native.down = True
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 1)
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url + '/v1/captures', headers={'Authorization': 'Bearer synthetic-owner-token'},
                    json={'operation_id': 'during-outage', 'text': 'Captured while inference is down'}) as response:
                self.assertEqual(response.status, 200)
                self.assertEqual((await response.json())['status'], 'applied')
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 1)
        self.assertEqual(self.control.budget()['active'], 1)
        self.assertEqual(self.control.budget()['committed_cost_usd'], 4)
        self.assertNotEqual(self.service.pending_events('gtd-clarification', 'fixture'), [])

    def temporal_events(self):
        rows = self.service.store.db.execute("SELECT payload FROM events WHERE provider='gtd-review'").fetchall()
        return [json.loads(row[0]) for row in rows if json.loads(row[0]).get('reason') == 'periodic_return']

    async def test_due_and_future_returns_are_idempotent_across_restart_and_own_progress(self):
        receipt = self.service.execute('felix', {'operation_id': 'scheduled-reference', 'action': 'clarify',
            'item_id': self.item['id'], 'expected_version': self.item['version'],
            'fields': {'kind': 'reference', 'commitment': 'proposed', 'review_at': '2000-01-01T09:00:00-03:00',
                'decision_at': '2999-01-01T00:00:00+00:00'}})
        self.assertEqual(receipt['status'], 'applied', receipt)
        self.worker.config['review_interval_seconds'] = 0
        self.worker._periodic_review(self.worker._state())
        events = self.temporal_events()
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]['field'], 'review_at')
        self.assertEqual(events[0]['due_at'], '2000-01-01T12:00:00+00:00')
        await self.worker.tick()
        await self.worker.tick()
        self.worker = OrchestrationWorker(self.service, self.control, self.native, dict(self.config, review_interval_seconds=0))
        await self.worker.tick()
        self.assertEqual(len(self.temporal_events()), 1)
        self.assertEqual(len(self.native.submissions), 1)
        current = self.service.get_item(self.item['id'])
        changed = self.service.execute('felix', {'operation_id': 'rescheduled', 'action': 'edit',
            'item_id': current['id'], 'expected_version': current['version'], 'fields': {'review_at': '2001-01-01T00:00:00+00:00'}})
        self.assertEqual(changed['status'], 'applied', changed)
        self.worker._periodic_review(self.worker._state())
        self.assertEqual(len(self.temporal_events()), 2)

    async def test_due_return_stays_pending_during_bot_suspension_without_admission_churn(self):
        changed = self.service.execute('felix', {'operation_id': 'paused-due', 'action': 'clarify',
            'item_id': self.item['id'], 'expected_version': self.item['version'],
            'fields': {'kind': 'reference', 'commitment': 'proposed', 'review_at': '2000-01-01T00:00:00+00:00'}})
        self.assertEqual(changed['status'], 'applied', changed)
        bot = self.control.bots()[0]
        self.control.register_bot('felix', 'temporal-suspend', dict(bot, state='suspended'))
        before = len(self.control._load()['operations'])
        self.worker.config['review_interval_seconds'] = 0
        await self.worker.tick()
        await self.worker.tick()
        self.assertEqual(len(self.temporal_events()), 1)
        self.assertEqual(len(self.control._load()['operations']), before)
        self.assertEqual(self.native.submissions, [])
        self.control.register_bot('felix', 'temporal-resume', dict(bot, state='available'))
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 1)

    async def test_global_review_return_same_date_is_not_reemitted_by_new_review(self):
        self.worker.config['review_interval_seconds'] = 0
        for operation, date in [('review-one', '2000-01-01T00:00:00+00:00'),
                                ('review-same', '2000-01-01T00:00:00+00:00'),
                                ('review-new', '2001-01-01T00:00:00+00:00')]:
            receipt = self.service.execute('felix', {'operation_id': operation, 'action': 'review', 'fields': {'return_at': date}})
            self.assertEqual(receipt['status'], 'applied', receipt)
            self.worker = OrchestrationWorker(self.service, self.control, self.native, dict(self.config, review_interval_seconds=0))
            self.worker._periodic_review(self.worker._state())
            self.assertEqual(len(self.temporal_events()), 2 if operation == 'review-new' else 1)
        self.assertTrue(all(event['scope'] == 'global_review' for event in self.temporal_events()))
        self.assertEqual(len(self.service.query()), 1)

    async def test_global_return_does_not_reemit_when_anchor_closes(self):
        self.service.capture('felix', 'another-anchor', 'Another existing subject')
        review = self.service.execute('felix', {'operation_id': 'global-return-anchor', 'action': 'review',
            'fields': {'return_at': '2000-01-01T00:00:00+00:00'}})
        self.assertEqual(review['status'], 'applied', review)
        self.worker.config['review_interval_seconds'] = 0
        self.worker._periodic_review(self.worker._state())
        anchor = self.service.get_item(self.temporal_events()[0]['item_id'])
        closed = self.service.execute('felix', {'operation_id': 'close-anchor', 'action': 'clarify',
            'item_id': anchor['id'], 'expected_version': anchor['version'], 'fields': {'destination': 'discard', 'reason': 'Anchor no longer relevant'}})
        self.assertEqual(closed['status'], 'applied', closed)
        self.worker = OrchestrationWorker(self.service, self.control, self.native, dict(self.config, review_interval_seconds=0))
        self.worker._periodic_review(self.worker._state())
        self.assertEqual(len(self.temporal_events()), 1)

    async def test_date_only_requires_explicit_timezone_and_notification_pause_does_not_pause_work(self):
        receipt = self.service.execute('felix', {'operation_id': 'date-only', 'action': 'clarify',
            'item_id': self.item['id'], 'expected_version': self.item['version'],
            'fields': {'kind': 'reference', 'commitment': 'proposed', 'decision_at': '2000-01-01'}})
        self.assertEqual(receipt['status'], 'applied', receipt)
        for event in self.worker._events():
            self.service.mark_event(event['event_key'], 'done')
        self.worker.config['review_interval_seconds'] = 0
        self.worker._periodic_review(self.worker._state())
        self.assertEqual(self.temporal_events(), [])
        self.worker.config['timezone'] = 'America/Santiago'
        attention = self.service.execute('felix', {'operation_id': 'quiet-attention', 'action': 'set_attention', 'fields': {'paused': True, 'notify': False}})
        self.assertEqual(attention['status'], 'applied', attention)
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 1)
        self.assertEqual(self.temporal_events()[0]['due_at'], '2000-01-01T03:00:00+00:00')
        self.assertEqual(self.temporal_events()[0]['time_basis'], 'America/Santiago')
        self.assertTrue(self.service.review_state()['attention']['paused'])

    async def test_no_budget_and_periodic_silence_do_not_call_inference(self):
        self.worker.control = ExecutionControl(self.service, {})
        await self.worker.tick()
        self.assertEqual(self.native.submissions, [])
        self.assertEqual(len(self.service.pending_events('gtd-clarification', 'fixture')), 1)
        self.service.mark_event(self.event['event_key'], 'done')
        for event in self.service.pending_events('gtd-review', 'local'):
            self.service.mark_event(event['event_key'], 'done')
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        await self.worker.tick()
        self.assertEqual(self.native.submissions, [])

    async def test_human_correction_during_run_preserves_new_events_and_blocks_old_output(self):
        await self.worker.tick()
        job = self.native.submissions[0]['job_id']
        current = self.service.get_item(self.item['id'])
        changed = self.service.execute('felix', dict(operation_id='correct', action='edit', item_id=current['id'], expected_version=current['version'], fields={'title': 'New human meaning'}))
        self.assertEqual(changed['status'], 'applied')
        await self.worker.tick()
        self.assertTrue(self.control.get_job(job)['stop_requested'])
        self.assertNotEqual(self.control.get_job(job)['integration'], 'integrated')
        self.assertEqual(self.service.get_item(self.item['id'])['title'], 'New human meaning')
        # It may admit fresh work only after native cancellation is observed.
        self.assertEqual(self.control.get_job(job)['observations'][-1]['native_status'], 'cancelled')
        self.assertEqual(self.service.pending_events('gtd-notification', 'local'), [])

    async def test_stop_signal_does_not_claim_terminal_before_native_observation(self):
        self.native.keep_running = True
        await self.worker.tick()
        job = self.native.submissions[0]['job_id']
        self.control.request_stop('felix', 'human-stop', job)
        self.assertFalse(self.control.get_job(job)['terminal'])
        self.assertEqual(self.control.budget()['active'], 1)
        await self.worker.tick()
        self.assertTrue(self.control.get_job(job)['terminal'])
        self.assertNotEqual(self.control.get_job(job)['integration'], 'integrated')

    async def test_terminal_observed_before_worker_receipt_is_recovered_not_lost(self):
        await self.worker.tick()
        job = self.native.submissions[0]['job_id']
        await self.native.poll(job)  # crash window: native observation persisted first
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        await self.worker.tick()
        self.assertEqual(self.control.get_job(job)['integration'], 'integrated')
        self.assertEqual(len(self.native.submissions), 1)

    async def test_late_duplicate_source_event_does_not_restart_preparation(self):
        await self.worker.tick()
        await self.worker.tick()
        self.service.ingest_event({'provider': 'gtd-clarification', 'account': 'fixture',
            'external_id': 'late-copy', 'revision': '1', 'payload': {'item_id': self.item['id'], 'reason': 'clarification_pending'}})
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 1)
        self.assertEqual(self.service.pending_events('gtd-clarification', 'fixture'), [])

    async def test_existing_local_work_mandate_allows_actual_mcp_assessment_without_self_stop(self):
        clarified = self.service.execute('felix', dict(operation_id='owner-action', action='clarify', item_id=self.item['id'], expected_version=self.item['version'], fields={
            'kind': 'action', 'commitment': 'committed', 'completion_criteria': 'Fixture explicitly verifies a synthetic result.'}))
        item = clarified['item']
        granted = self.service.execute('felix', dict(operation_id='owner-grant', action='grant_mandate', item_id=item['id'], expected_version=item['version'], fields={
            'scope_item_id': item['id'], 'actors': ['gtd-felix'], 'capabilities': ['prepare_private', 'local_work'], 'completion_criteria': item['completion_criteria']}))
        self.assertEqual(granted['status'], 'applied', granted)
        bot = dict(self.control.bots()[0], capabilities=['prepare_private', 'local_work'])
        self.assertEqual(self.control.register_bot('felix', 'local-bot', bot)['status'], 'applied')
        self.native.complete_criterion = True
        await self.worker.tick()
        job_id = self.native.submissions[0]['job_id']
        job = self.control.get_job(job_id)
        self.assertEqual(job['capability'], 'local_work')
        self.assertEqual(job['mandate_id'], granted['mandate']['id'])
        self.assertEqual(self.service.get_item(item['id'])['status'], 'done')
        self.assertFalse(job['terminal'])
        await self.worker.tick()
        job = self.control.get_job(job_id)
        self.assertFalse(job['stop_requested'])
        self.assertTrue(job['terminal'])
        self.assertEqual(job['integration'], 'integrated')
        self.assertEqual(job['observations'][-1]['native_status'], 'completed')
        self.assertEqual(len(self.service.materials(item['id'])), 1)
        self.assertEqual(self.service.pending_events('gtd-notification', 'local')[0]['payload']['kind'], 'completed')

    async def test_verified_native_admission_rejection_releases_capacity_without_success(self):
        async def rejected(job_id, prompt, durable=False):
            self.native.submissions.append({'job_id': job_id, 'prompt': prompt, 'durable': durable})
            observation = {'native_identity': self.native.native(job_id), 'native_status': 'failed', 'terminal': True,
                'cost_usd': 0, 'runtime_seconds': 0, 'evidence_reference': 'fixture://admission/undispatched/' + job_id}
            self.control.observe(job_id, observation)
            return {'status': 'rejected', 'job_id': job_id, 'terminal': True, 'no_effect': True, 'error': 'native_limits_unconfigured'}
        self.native.submit = rejected
        await self.worker.tick()
        job_id = self.native.submissions[0]['job_id']
        self.assertTrue(self.control.get_job(job_id)['terminal'])
        self.assertEqual(self.control.budget()['active'], 0)
        self.assertEqual(self.control.budget()['committed_cost_usd'], 0)
        await self.worker.tick()
        self.assertNotEqual(self.control.get_job(job_id)['integration'], 'integrated')
        self.assertEqual(self.service.pending_events('gtd-notification', 'local'), [])
        self.assertEqual(self.service.pending_events('gtd-clarification', 'fixture')[0]['status'], 'failed')
        self.assertEqual(len(self.native.submissions), 1)

    async def test_durable_delegation_waits_for_parent_then_returns_without_duplicate_intention(self):
        self.native.delegate = True
        await self.worker.tick()
        parent = self.native.submissions[0]['job_id']
        child = self.native.child_id
        self.assertEqual(self.control.get_job(child)['delivery'], 'deferred')
        self.assertEqual(self.control.budget()['active'], 1)
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)
        self.assertEqual(self.native.submissions[1]['job_id'], child)
        self.assertTrue(self.native.submissions[1]['durable'])
        self.assertTrue(self.control.get_job(parent)['terminal'])
        self.assertFalse(self.control.get_job(child)['terminal'])
        await self.worker.tick()
        self.assertEqual(self.control.get_job(child)['integration'], 'integrated')
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)
        self.assertEqual(self.control.budget()['active'], 0)

    async def test_deferred_stop_returns_once_without_submit_poll_or_retry(self):
        self.native.delegate = True
        await self.worker.tick()
        child = self.native.child_id
        state = self.worker._state()
        state['runs'][child] = {'phase':'intent', 'event_keys':[], 'prompt':'Synthetic deferred task', 'durable':True}
        self.worker._save(state)
        stopped = self.control.request_stop('felix','cancel-deferred',child)
        self.assertTrue(stopped['job']['terminal'])
        submissions, polls = len(self.native.submissions), self.native.polls
        await self.worker._advance(state,child)
        run = self.worker._state()['runs'][child]
        self.assertEqual(run['result_status'],'discarded')
        self.assertEqual(run['operational_return']['kind'],'cancelled_before_dispatch')
        self.worker = OrchestrationWorker(self.service,self.control,self.native,self.config)
        for _ in range(3):
            await self.worker._advance(self.worker._state(),child)
        self.assertEqual(len(self.native.submissions),submissions)
        self.assertEqual(self.native.polls,polls)
        self.assertEqual(self.control.get_job(child)['observations'],[])

    async def test_deferred_capacity_failure_is_visible_and_retryable(self):
        self.native.delegate = True
        await self.worker.tick()
        child = self.native.child_id
        state = self.worker._state()
        state['runs'][child] = {'phase':'intent', 'event_keys':[], 'prompt':'Synthetic deferred task', 'durable':True}
        self.worker._save(state)
        await self.worker._advance(state,child)
        self.assertEqual(self.worker._state()['runs'][child]['error'],'concurrency_exhausted')
        self.assertFalse(self.control.get_job(child)['terminal'])

    async def integrated_executor_delivery(self, child=False, crash=False, kind="project", coordinate=False):
        clarified = self.service.execute('felix', {'operation_id': 'worker-action', 'action': 'clarify',
            'item_id': self.item['id'], 'expected_version': self.item['version'],
            'fields': {'kind': kind, 'commitment': 'committed', **({'completion_criteria': 'Verified guide'} if coordinate else {})}})
        self.assertEqual(clarified['status'], 'applied', clarified)
        waiting = self.service.execute('felix', {'operation_id':'human-wait','action':'derive',
            'item_id':self.item['id'],'expected_version':clarified['item']['version'],
            'fields':{'kind':'waiting','title':'Lara confirmation','waiting_for':'Lara confirms schedule',
                      'executor':'felix','capability':'prepare_private'}})
        self.assertEqual(waiting['status'],'applied',waiting)
        target = self.service.get_item(self.item['id'])
        if child:
            derived = self.service.execute('felix', {'operation_id': 'executor-child', 'action': 'derive',
                'item_id': target['id'], 'expected_version': target['version'],
                'fields': {'kind': 'action', 'title': 'Private child contribution',
                    'executor': 'bounded-executor', 'capability': 'prepare_private',
                    **({'completion_criteria': 'Verified bounded guide'} if coordinate else {})}})
            self.assertEqual(derived['status'], 'applied', derived)
            target = derived['item']
            self.assertNotEqual(target['id'], self.item['id'])
            self.assertEqual(target['parent_id'], self.item['id'])
            unrelated = self.service.capture('felix', 'unrelated-project', 'Unrelated project')['item']
            unrelated = self.service.execute('felix', {'operation_id': 'unrelated-project-kind',
                'action': 'clarify', 'item_id': unrelated['id'], 'expected_version': unrelated['version'],
                'fields': {'kind': 'project', 'commitment': 'proposed'}})['item']
            linked = self.service.execute('felix', {'operation_id': 'unrelated-project-link',
                'action': 'edit', 'item_id': target['id'], 'expected_version': target['version'],
                'fields': {'project_id': unrelated['id']}})
            self.assertEqual(linked['status'], 'applied', linked)
            target = linked['item']
        grant = self.service.execute('felix', {'operation_id': 'worker-mandate', 'action': 'grant_mandate',
            'item_id': self.item['id'], 'expected_version': self.service.get_item(self.item['id'])['version'],
            'fields': {'scope_item_id': self.item['id'], 'capabilities': ['prepare_private', 'local_work'] if coordinate else ['prepare_private'],
                'actors': ['gtd-felix', 'bounded-executor'] if coordinate else ['bounded-executor'], 'completion_criteria': 'A bounded private contribution'}})
        self.assertEqual(grant['status'], 'applied', grant)
        registered = self.control.register_bot('felix', 'worker-bot', {'id': 'worker', 'actor': 'bounded-executor',
            'state': 'available', 'source_urn': 'urn:test:worker', 'host': 'synthetic', 'profile': 'fixture',
            'capabilities': ['prepare_private'], 'probe_evidence': 'fixture://worker'})
        self.assertEqual(registered['status'], 'applied', registered)
        parent = None
        if coordinate:
            parent_receipt = self.control.reserve('gtd-felix', 'coordinating-parent', {**self.config['reservation'],
                'item_id': self.item['id'], 'expected_version': self.service.get_item(self.item['id'])['version'],
                'mandate_id': grant['mandate']['id'], 'capability': 'prepare_private', 'bot_id': 'principal',
                'purpose': 'Coordinate guide', 'scope': 'Guide and its actual children'})
            self.assertEqual(parent_receipt['status'], 'reserved', parent_receipt)
            parent = parent_receipt['job_id']
        receipt = self.control.reserve('gtd-felix', 'worker-reserve', {**self.config['reservation'],
            'item_id': target['id'], 'expected_version': self.service.get_item(target['id'])['version'], 'mandate_id': grant['mandate']['id'],
            'capability': 'prepare_private', 'bot_id': 'worker', 'purpose': 'Private contribution', 'scope': 'This item only',
            **({'parent_job_id': parent, 'defer_when_busy': True, 'max_cost_usd': 1, 'max_runtime_seconds': 50} if coordinate else {})})
        self.assertEqual(receipt['status'], 'reserved', receipt)
        job = receipt['job_id']
        if coordinate:
            reserved_basis = self.control.get_job(job)['item_bases']
            for target_id in (target['id'], self.item['id']):
                current = self.service.get_item(target_id)
                assessment = self.service.execute('gtd-felix', {'operation_id': 'coordinate-' + target_id,
                    'action': 'assess_result', 'item_id': target_id, 'expected_version': current['version'],
                    'fields': {'satisfied': False, 'evidence': 'Reserved child has no delivery yet',
                        'gap': 'Await same contribution', 'mandate_id': grant['mandate']['id']}})
                self.assertEqual(assessment['status'], 'applied', assessment)
                self.assertEqual(self.control.record_progress(parent, assessment, current['version'])['status'], 'recorded')
            observed = self.control.observe(parent, {'native_identity': self.native.native(parent),
                'native_status': 'completed', 'terminal': True, 'cost_usd': .1, 'runtime_seconds': 1,
                'evidence_reference': 'fixture://coordinating-parent'})
            self.assertEqual(observed['status'], 'recorded', observed)
            self.assertEqual(self.control.acknowledge_progress(parent)['status'], 'integrated')
            prompt = self.worker._prompt(self.control.get_job(job), [])
            self.assertNotIn('source_version_stale', prompt)
            self.assertIn('Source-specific synthetic note', prompt)

        self.service.mark_event(self.event['event_key'], 'done')
        for event in self.service.pending_events('gtd-review','local'):
            self.service.mark_event(event['event_key'],'done')
        self.native.no_progress = True
        state = self.worker._state()
        state['runs'][job] = {'phase': 'intent', 'durable': True, 'event_keys': [], 'prompt': self.worker._prompt(receipt['job'], [])}
        await self.worker._advance(state, job)
        self.native.runs[job]['output'] = 'Bounded executor contribution, with explicit evidence and limits.'
        if crash == 'domain':
            with patch.object(self.control, 'record_integration', side_effect=OSError('crash after domain')):
                await self.worker._advance(state, job)
            self.assertEqual(self.control.get_job(job)['integration'], 'accepted_pending_integration')
            self.assertEqual(len(self.service.materials(target['id'])), 1)
            return job, target['id'], waiting
        if crash:
            with patch.object(self.worker, '_notify', side_effect=RuntimeError('crash before notification')):
                with self.assertRaises(RuntimeError):
                    await self.worker._advance(state, job)
        else:
            await self.worker._advance(state, job)
        self.assertEqual(self.control.get_job(job)['integration'], 'integrated')
        self.assertEqual(len(self.service.materials(target['id'])), 1)
        self.assertEqual(self.service.materials(target['id'])[0]['author'], 'bounded-executor')
        if not crash:
            await self.worker._advance(state, job)
        self.assertEqual(len(self.service.materials(target['id'])), 1)
        self.assertNotEqual(self.service.get_item(self.item['id'])['status'], 'done')

        if coordinate:
            self.assertEqual(self.control.get_job(job)['item_bases'], reserved_basis)
        return job, target['id'], waiting

    async def test_executor_same_child_assessment_and_reconstructed_source_prompt_integrate(self):
        job, target, _ = await self.integrated_executor_delivery(child=True, coordinate=True)
        self.assertEqual(self.control.get_job(job)['integration'], 'integrated')
        self.assertEqual(len(self.service.materials(target)), 1)

    async def test_executor_same_child_coordination_recovers_exact_material_after_crash(self):
        job, target, _ = await self.integrated_executor_delivery(child=True, coordinate=True, crash='domain')
        original = self.control.get_job(job)['item_bases']
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        await self.worker.tick()
        self.assertEqual(self.control.get_job(job)['integration'], 'integrated')
        self.assertEqual(self.control.get_job(job)['item_bases'], original)
        self.assertEqual(len(self.service.materials(target)), 1)
        self.assertEqual(sum(s['job_id'] == job for s in self.native.submissions), 1)

    async def test_executor_return_reviews_project_once_across_restart(self):
        await self._assert_executor_return(False)

    async def test_executor_return_reviews_real_parent_after_integration_crash(self):
        await self._assert_executor_return(True, crash=True)

    async def test_executor_return_recovers_domain_before_integration(self):
        await self._assert_executor_return(True, crash='domain')

    async def _assert_executor_return(self, child, crash=False):
        job, target, waiting = await self.integrated_executor_delivery(child, crash)
        self.assertEqual(self.service.review_state()['gaps'], [])
        self.native.no_progress = False
        for _ in range(5):
            self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)
        reviewed = self.control.get_job(self.native.submissions[-1]['job_id'])
        self.assertEqual(reviewed['item_id'], self.item['id'])
        record = self.worker._state()['executor_returns'][job]
        self.assertEqual(record['payload']['material_item_id'], target)
        self.assertIn(record['payload']['material_id'], self.native.submissions[-1]['prompt'])
        self.assertNotEqual(self.service.get_item(self.item['id'])['status'], 'done')
        self.assertTrue(any(i.get('waiting_for') == 'Lara confirms schedule'
                            for i in self.service.query({'kind': 'waiting'})))

    async def test_executor_return_review_writes_do_not_grant_action_continuation(self):
        job, _, _ = await self.integrated_executor_delivery(kind='action')
        self.native.no_progress = False
        for _ in range(5):
            self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)
        self.assertEqual(self.worker._state().get('continuations', {}), {})

    async def test_executor_return_global_review_preserves_pending_delivery(self):
        job, _, _ = await self.integrated_executor_delivery()
        budget = self.control.budget()
        with patch.object(self.control, 'budget', return_value={**budget, 'remaining_cost_usd': 0}):
            await self.worker.tick()
        record = self.worker._state()['executor_returns'][job]
        def global_review(operation):
            receipt = self.service.execute('felix', {'operation_id': operation, 'action': 'review',
                'fields': {'source_coverage': {entry['item_id']: len(self.service.get_item(entry['item_id'])['source_revisions'])
                    for entry in self.service.review_state()['source_coverage']}}})
            self.assertEqual(receipt['status'], 'applied', receipt)
            self.assertTrue(receipt['review']['operational_complete'])
        global_review('review-before-delivery-admission')
        events = self.service.pending_events('gtd-review', 'local')
        self.assertTrue(any(event['event_key'] == record['event_key'] and event['status'] == 'pending'
                            for event in events))
        self.native.no_progress = False
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)
        global_review('review-during-delivery-review')
        await self.worker.tick()
        self.assertEqual(self.control.get_job(self.native.submissions[-1]['job_id'])['integration'], 'integrated')
        global_review('review-after-delivery-review')
        for _ in range(2):
            self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)

    async def test_executor_return_waits_for_available_principal_and_budget(self):
        job, target, _ = await self.integrated_executor_delivery()
        budget = self.control.budget()
        with patch.object(self.control, 'budget', return_value={**budget, 'remaining_cost_usd': 0}):
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 1)
        self.assertEqual(self.worker._state()['executor_returns'][job]['blocker'], 'budget_unavailable')
        with patch.object(self.control, 'bots', return_value=[]):
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 1)
        self.assertEqual(self.worker._state()['executor_returns'][job]['blocker'], 'principal_unavailable')
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)

    async def test_executor_return_recovery_and_suspension_preserve_pending(self):
        job, _, _ = await self.integrated_executor_delivery()
        self.service._set_meta('recovery_required', True)
        self.assertEqual((await self.worker.tick())['reason'], 'recovery_required')
        self.assertEqual(self.worker._state()['executor_returns'][job]['blocker'], 'recovery_required')
        self.assertEqual(len(self.native.submissions), 1)
        self.service._set_meta('recovery_required', False)
        bot = next(b for b in self.control.bots() if b['id'] == 'principal')
        self.control.register_bot('felix', 'pause-delivery-review', dict(bot, state='suspended'))
        for _ in range(2):
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 1)
        self.assertEqual(self.worker._state()['executor_returns'][job]['blocker'], 'principal_unavailable')
        self.control.register_bot('felix', 'resume-delivery-review', dict(bot, state='available'))
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)

    async def test_executor_return_revoked_material_never_admits(self):
        job, _, _ = await self.integrated_executor_delivery()
        mandate = self.control.get_job(job)['mandate_id']
        current = self.service.get_item(self.item['id'])
        receipt = self.service.execute('felix', {'operation_id': 'revoke-delivery', 'action': 'revoke_mandate',
            'item_id': current['id'], 'expected_version': current['version'], 'fields': {'mandate_id': mandate}})
        self.assertEqual(receipt['status'], 'applied', receipt)
        for event in self.service.pending_events('gtd-review', 'local'):
            self.service.mark_event(event['event_key'], 'done')
        with patch.object(self.worker, '_periodic_review'):
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 1)
        self.assertEqual(self.worker._state()['executor_returns'][job]['blocker'], 'material_invalid')

    async def test_executor_return_reclassified_parent_preserves_original_destination(self):
        job, target, _ = await self.integrated_executor_delivery(child=True)
        current = self.service.get_item(self.item['id'])
        changed = self.service.execute('felix', {'operation_id': 'reclassify-after-delivery', 'action': 'edit',
            'item_id': current['id'], 'expected_version': current['version'], 'fields': {'kind': 'reference'}})
        self.assertEqual(changed['status'], 'applied', changed)
        for event in self.service.pending_events('gtd-review', 'local'):
            self.service.mark_event(event['event_key'], 'done')
        with patch.object(self.worker, '_periodic_review'):
            await self.worker.tick()
        record = self.worker._state()['executor_returns'][job]
        self.assertEqual(record['payload']['item_id'], self.item['id'])
        self.assertEqual(record['blocker'], 'parent_changed')
        self.assertEqual(len(self.native.submissions), 1)

    async def test_executor_return_invalid_material_stays_pending(self):
        job, target, _ = await self.integrated_executor_delivery()
        item = self.service.get_item(target)
        changed = self.service.execute('felix', {'operation_id': 'changed-criterion', 'action': 'edit',
            'item_id': target, 'expected_version': item['version'],
            'fields': {'completion_criteria': 'Different criterion'}})
        self.assertEqual(changed['status'], 'applied', changed)
        for event in self.service.pending_events('gtd-review', 'local'):
            self.service.mark_event(event['event_key'], 'done')
        # Isolate the delivery return from the independent human correction event.
        with patch.object(self.worker, '_periodic_review'):
            await self.worker.tick()
        record = self.worker._state()['executor_returns'][job]
        self.assertEqual(record['blocker'], 'material_invalid')
        self.assertEqual(len(self.native.submissions), 1)
        events = self.service.pending_events('gtd-review', 'local')
        self.assertTrue(any(e['event_key'] == record['event_key'] and e['status'] == 'pending' for e in events))

    async def test_durable_executor_return_still_creates_exactly_one_material(self):
        clarified = self.service.execute('felix', {'operation_id': 'worker-action', 'action': 'clarify',
            'item_id': self.item['id'], 'expected_version': self.item['version'],
            'fields': {'kind': 'action', 'commitment': 'committed'}})
        self.assertEqual(clarified['status'], 'applied', clarified)
        grant = self.service.execute('felix', {'operation_id': 'worker-mandate', 'action': 'grant_mandate',
            'item_id': self.item['id'], 'expected_version': self.service.get_item(self.item['id'])['version'],
            'fields': {'scope_item_id': self.item['id'], 'capabilities': ['prepare_private'],
                'actors': ['bounded-executor'], 'completion_criteria': 'A bounded private contribution'}})
        self.assertEqual(grant['status'], 'applied', grant)
        registered = self.control.register_bot('felix', 'worker-bot', {'id': 'worker', 'actor': 'bounded-executor',
            'state': 'available', 'source_urn': 'urn:test:worker', 'host': 'synthetic', 'profile': 'fixture',
            'capabilities': ['prepare_private'], 'probe_evidence': 'fixture://worker'})
        self.assertEqual(registered['status'], 'applied', registered)
        receipt = self.control.reserve('gtd-felix', 'worker-reserve', {**self.config['reservation'],
            'item_id': self.item['id'], 'expected_version': grant['item']['version'], 'mandate_id': grant['mandate']['id'],
            'capability': 'prepare_private', 'bot_id': 'worker', 'purpose': 'Private contribution', 'scope': 'This item only'})
        self.assertEqual(receipt['status'], 'reserved', receipt)
        job = receipt['job_id']
        self.native.no_progress = True
        state = self.worker._state()
        state['runs'][job] = {'phase': 'intent', 'durable': True, 'event_keys': [], 'prompt': self.worker._prompt(receipt['job'], [])}
        await self.worker._advance(state, job)
        self.native.runs[job]['output'] = 'Bounded executor contribution, with explicit evidence and limits.'
        await self.worker._advance(state, job)
        self.assertEqual(self.control.get_job(job)['integration'], 'integrated')
        self.assertEqual(len(self.service.materials(self.item['id'])), 1)
        self.assertEqual(self.service.materials(self.item['id'])[0]['author'], 'bounded-executor')
        await self.worker._advance(state, job)
        self.assertEqual(len(self.service.materials(self.item['id'])), 1)
        self.assertNotEqual(self.service.get_item(self.item['id'])['status'], 'done')

    async def confirmed_external_effect(self):
        from types import SimpleNamespace
        from gtd_felix.effects import ExternalEffects
        from gtd_felix.effect_monitor import EffectMonitor
        effects = ExternalEffects(self.service)
        proposal = {'provider': 'calendar', 'account': 'fixture@example.invalid', 'action': 'insert',
            'item_id': self.item['id'], 'target': {'id': 'fixed123'}, 'expires_at': '2099-01-01T00:00:00Z',
            'payload': {'calendar_id': 'fixture@example.invalid', 'event': {'id': 'fixed123'}, 'send_updates': 'none'}}
        effect = effects.propose('felix', 'external-proposal', proposal)['effect']
        effects.authorize('felix', 'external-authorize', effect['id'], effect['proposal_hash'])
        self.assertEqual(effects.begin_dispatch(effect['id'])['status'], 'dispatch')
        envelope = {k: proposal[k] for k in ('provider', 'account', 'action', 'target')}
        envelope.update(request_hash=effect['proposal_hash'], remote_id='fixed123')
        observed = effects.observe(effect['id'], {**envelope, 'status': 'confirmed',
            'evidence_reference': 'fixture://exact-calendar-readback',
            'readback': {**envelope, 'content_verified': True, 'fixed_identity': 'fixed123'}})
        self.assertEqual(observed['status'], 'confirmed')
        monitor = EffectMonitor(self.service, effects,
            SimpleNamespace(transports={'alias': SimpleNamespace(account=proposal['account'])}),
            {'accounts': [proposal['account']], 'poll_interval_seconds': 1, 'retry_interval_seconds': 10})
        await monitor.tick()
        return effect, monitor

    async def test_confirmed_effect_same_item_version_reviews_once_across_restart(self):
        await self.worker.tick()
        await self.worker.tick()
        before = self.service.get_item(self.item['id'])
        self.assertEqual(len(self.native.submissions), 1)
        effect, monitor = await self.confirmed_external_effect()
        self.assertEqual(self.service.get_item(self.item['id']), before)
        self.native.no_progress = True
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)
        self.assertIn(effect['id'], self.native.submissions[-1]['prompt'])
        self.assertIn('external_effect_status', self.native.submissions[-1]['prompt'])
        for _ in range(3):
            await monitor.tick()
            self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
            await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)
        self.assertEqual(self.service.get_item(self.item['id']), before)

    async def test_confirmed_effect_stays_pending_with_blocked_continuation(self):
        await self.prepare_pending_continuation()
        effect, monitor = await self.confirmed_external_effect()
        await self.worker.tick()
        events = [e for e in self.service.pending_events('gtd-review', 'local')
            if e['payload'].get('effect_id') == effect['id']]
        self.assertEqual(len(events), 1)
        self.assertNotEqual(events[0]['status'], 'ignored')
        self.assertEqual(len(self.native.submissions), 1)

    async def test_routed_instruction_waits_for_running_target_and_survives_same_basis_completion(self):
        self.budget['max_active'] = 2
        self.native.keep_running = True
        await self.worker.tick()
        first = self.native.submissions[0]['job_id']
        target = self.service.get_item(self.item['id'])
        source = self.service.capture('felix', 'route-new-intake', 'Continue the existing subject using these new human instructions')['item']
        command = {'operation_id': 'route-to-running', 'action': 'clarify', 'item_id': source['id'], 'expected_version': source['version'],
            'fields': {'destination': 'existing', 'target_item_id': target['id'], 'reason': 'Continue existing work',
                'intent_basis': {'source_item_id': source['id'], 'quote': source['text']}}}
        receipt = self.service.execute('gtd-felix', command)
        self.assertEqual(receipt['status'], 'applied', receipt)
        self.assertEqual(self.service.get_item(target['id']), target)
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 1)
        routed = [event for event in self.service.pending_events('gtd-review', 'local') if event['payload'].get('reason') == 'routed_human_instruction']
        self.assertEqual(len(routed), 1)
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        self.native.keep_running = False
        await self.worker.tick()
        self.assertTrue(self.control.get_job(first)['terminal'])
        self.assertEqual(len(self.native.submissions), 2)
        second = self.native.submissions[1]
        self.assertIn('routed_human_instruction', second['prompt'])
        self.assertIn(source['text'], second['prompt'])
        self.assertEqual(self.control.get_job(second['job_id'])['item_id'], target['id'])
        self.assertNotIn(source['id'], self.control.get_job(second['job_id'])['item_bases'])
        await self.worker.tick()
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 2)

    async def test_corrected_root_new_job_continues_existing_children_through_http_and_closes(self):
        root = self.service.execute('felix', {'operation_id': 'continuity-project', 'action': 'clarify',
            'item_id': self.item['id'], 'expected_version': self.item['version'],
            'fields': {'kind': 'project', 'commitment': 'committed', 'outcome': 'Two verified contributions', 'completion_criteria': 'Both child criteria verified'}})['item']
        granted = self.service.execute('felix', {'operation_id': 'continuity-grant', 'action': 'grant_mandate',
            'item_id': root['id'], 'expected_version': root['version'], 'fields': {'scope_item_id': root['id'],
                'capabilities': ['local_work', 'prepare_private'], 'actors': ['gtd-felix'], 'completion_criteria': 'Both child criteria verified'}})
        self.assertEqual(granted['status'], 'applied', granted)
        root, mandate = granted['item'], granted['mandate']['id']
        bot = self.control.bots()[0]
        self.control.register_bot('felix', 'continuity-bot', dict(bot, capabilities=['local_work', 'prepare_private']))
        request = {**self.config['reservation'], 'item_id': root['id'], 'expected_version': root['version'],
            'capability': 'local_work', 'bot_id': bot['id'], 'mandate_id': mandate, 'purpose': 'Continue hierarchy', 'scope': 'Root and authorized descendants'}
        old = self.control.reserve('gtd-felix', 'continuity-old', request)['job_id']
        children = []
        for index in range(2):
            receipt = await self.client.call('gtd_command', {'job_id': old, 'command': {'operation_id': f'old-child-{index}',
                'action': 'derive', 'item_id': root['id'], 'expected_version': root['version'],
                'fields': {'kind': 'action', 'title': f'Contribution {index}', 'capability': 'local_work',
                    'mandate_id': mandate, 'completion_criteria': f'Explicit fixture check {index}'}}})
            self.assertEqual(receipt['status'], 'applied', receipt)
            children.append(receipt['item'])
        corrected = self.service.execute('felix', {'operation_id': 'continuity-correction', 'action': 'edit',
            'item_id': root['id'], 'expected_version': root['version'], 'fields': {'text': 'Corrected facts, original commitment retained'}})
        self.assertEqual(corrected['status'], 'applied', corrected)
        self.assertFalse(self.control.validate(old, 'local_work')['allowed'])
        observation = {'native_identity': self.native.native(old), 'native_status': 'cancelled', 'terminal': True,
            'cost_usd': .25, 'runtime_seconds': 5, 'evidence_reference': 'fixture://old-cancelled'}
        self.assertEqual(self.control.observe(old, observation)['status'], 'recorded')
        admitted = self.control.reserve('gtd-felix', 'continuity-new', {**request, 'expected_version': corrected['item']['version']})
        self.assertEqual(admitted['status'], 'reserved', admitted)
        job = admitted['job_id']
        for index, child in enumerate(children):
            material = await self.client.call('gtd_command', {'job_id': job, 'command': {'operation_id': f'continued-material-{index}',
                'action': 'put_material', 'item_id': child['id'], 'expected_version': child['version'],
                'fields': {'content': 'Updated contribution based on corrected root facts', 'mandate_id': mandate}}})
            self.assertEqual(material['status'], 'applied', material)
            assessed = await self.client.call('gtd_command', {'job_id': job, 'command': {'operation_id': f'continued-assess-{index}',
                'action': 'assess_result', 'item_id': child['id'], 'expected_version': material['item']['version'],
                'fields': {'satisfied': True, 'evidence': f'Fixture explicitly verified child criterion {index}', 'mandate_id': mandate}}})
            self.assertEqual(assessed['status'], 'applied', assessed)
        closed = await self.client.call('gtd_command', {'job_id': job, 'command': {'operation_id': 'continued-root-assess',
            'action': 'assess_result', 'item_id': root['id'], 'expected_version': corrected['item']['version'],
            'fields': {'satisfied': True, 'evidence': 'Both fixture child criteria were separately verified', 'mandate_id': mandate}}})
        self.assertEqual(closed['status'], 'applied', closed)
        self.assertIsNotNone(self.control.own_terminal_progress(job))
        self.assertEqual(self.control.observe(job, {**observation, 'native_identity': self.native.native(job), 'native_status': 'completed'})['status'], 'recorded')
        self.assertEqual(self.control.integrate_terminal_progress(job)['status'], 'integrated')
        self.assertTrue(all(self.service.get_item(child['id'])['status'] == 'done' for child in children))
        self.assertEqual(len(self.service.query()), 3)
        self.assertEqual(self.service.get_item(root['id'])['status'], 'done')

    async def test_human_child_correction_blocks_root_assessment_before_domain_write(self):
        root = self.service.execute('felix', {'operation_id': 'stale-project', 'action': 'clarify',
            'item_id': self.item['id'], 'expected_version': self.item['version'],
            'fields': {'kind': 'project', 'commitment': 'committed', 'outcome': 'Verified contribution', 'completion_criteria': 'Child criterion'}})['item']
        grant = self.service.execute('felix', {'operation_id': 'stale-grant', 'action': 'grant_mandate',
            'item_id': root['id'], 'expected_version': root['version'], 'fields': {'scope_item_id': root['id'],
                'capabilities': ['local_work'], 'actors': ['gtd-felix'], 'completion_criteria': 'Child criterion'}})
        root, mandate = grant['item'], grant['mandate']['id']
        child = self.service.execute('felix', {'operation_id': 'stale-child', 'action': 'derive', 'item_id': root['id'],
            'expected_version': root['version'], 'fields': {'kind': 'action', 'title': 'Contribution', 'mandate_id': mandate,
                'capability': 'local_work', 'completion_criteria': 'Verified output'}})['item']
        bot = self.control.bots()[0]
        self.control.register_bot('felix', 'stale-bot', dict(bot, capabilities=['local_work', 'prepare_private']))
        admitted = self.control.reserve('gtd-felix', 'stale-new-reserve', {**self.config['reservation'], 'item_id': root['id'],
            'expected_version': root['version'], 'mandate_id': mandate, 'capability': 'local_work', 'bot_id': bot['id'],
            'purpose': 'Complete hierarchy', 'scope': 'Admitted descendants'})
        self.assertEqual(admitted['status'], 'reserved', admitted)
        job = admitted['job_id']
        note = self.service.execute('felix', {'operation_id': 'independent-child-note', 'action': 'edit', 'item_id': child['id'],
            'expected_version': child['version'], 'fields': {'notes': 'Compatible human note'}})
        self.assertEqual(note['status'], 'applied', note)
        self.assertTrue(self.control.validate_target(job, 'gtd-felix', root['id'], 'local_work')['allowed'])
        corrected = self.service.execute('felix', {'operation_id': 'late-child-facts', 'action': 'edit', 'item_id': child['id'],
            'expected_version': note['item']['version'], 'fields': {'text': 'New material human correction'}})
        self.assertEqual(corrected['status'], 'applied', corrected)
        rejected = await self.client.call('gtd_command', {'job_id': job, 'command': {'operation_id': 'must-not-close-stale-root',
            'action': 'assess_result', 'item_id': root['id'], 'expected_version': root['version'],
            'fields': {'satisfied': True, 'evidence': 'Earlier evidence is no longer current', 'mandate_id': mandate}}})
        self.assertEqual(rejected['status'], 'rejected', rejected)
        self.assertEqual(rejected['error'], 'stale_descendant_version')
        current = self.service.get_item(root['id'])
        self.assertEqual(current['status'], 'active')
        self.assertEqual(current['version'], root['version'])
        self.assertFalse(current.get('assessments'))

    async def test_restart_after_reserve_before_run_link_recovers_orphaned_intention(self):
        original = self.control.reserve
        def crash_after_reserve(*args, **kwargs):
            receipt = original(*args, **kwargs)
            self.assertEqual(receipt['status'], 'reserved')
            raise RuntimeError('synthetic crash window')
        self.control.reserve = crash_after_reserve
        with self.assertRaisesRegex(RuntimeError, 'synthetic crash window'):
            await self.worker.tick()
        self.control.reserve = original
        self.assertEqual(self.control.budget()['active'], 1)
        self.assertEqual(self.native.submissions, [])
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 1)
        self.assertEqual(self.control.budget()['active'], 1)
        await self.worker.tick()
        self.assertEqual(self.control.budget()['active'], 0)
        self.assertEqual(len(self.native.submissions), 1)

    async def test_executor_prompt_uses_native_return_and_captured_authoritative_context(self):
        item = self.service.get_item(self.item['id'])
        captured = {**item, 'notes': 'Correction: use the updated synthetic source, not the earlier draft.'}
        source = self.service.capture('felix', 'linked-source', 'Authoritative linked synthetic facts')['item']
        job = {'id': 'native-child', 'actor': 'bounded-executor', 'requested_by': 'gtd-felix',
            'item_id': item['id'], 'mandate_id': 'scope-mandate', 'capability': 'prepare_private',
            'purpose': 'Prepare a bounded contribution', 'scope': 'Only the supplied synthetic material',
            'max_cost_usd': 1, 'max_runtime_seconds': 50, 'max_retries': 0, 'max_descendants': 0,
            'source_versions': {source['id']: 1}, 'source_bases': {source['id']: self.control._basis(source['id'])}}
        event = {'payload': {'reason': 'source_revision', 'item_id': item['id']}}
        original_mandates = self.service.mandates
        self.service.mandates = lambda: [{'id': 'scope-mandate', 'scope_item_id': item['id'],
            'status': 'active', 'capabilities': ['prepare_private'], 'completion_criteria': 'A sourced synthetic contribution'}]
        try:
            prompt = self.worker._prompt(job, [event], captured)
        finally:
            self.service.mandates = original_mandates
        self.assertIn('kanban_complete', prompt)
        for missing_tool in ('gtd_read', 'gtd_command', 'gtd_dispatch', 'SKILL.md'):
            self.assertNotIn(missing_tool, prompt)
        context = json.loads(prompt.split('\n', 1)[1])
        self.assertEqual(context['item']['notes'], captured['notes'])
        self.assertEqual(context['item']['source_revisions'], item['source_revisions'])
        self.assertEqual(context['mandate']['completion_criteria'], 'A sourced synthetic contribution')
        self.assertEqual(context['job']['purpose'], job['purpose'])
        self.assertEqual(context['job']['max_descendants'], 0)
        self.assertEqual(context['events'][0]['reason'], 'source_revision')
        self.assertEqual(context['sources'][0]['id'], source['id'])
        self.assertEqual(context['sources'][0]['text'], source['text'])

    async def test_principal_prompt_keeps_its_mcp_tools(self):
        job = {'id': 'principal-fixture', 'actor': 'gtd-felix', 'item_id': self.item['id']}
        prompt = self.worker._prompt(job, [])
        for tool in ('gtd_read', 'gtd_command', 'gtd_dispatch'):
            self.assertIn(tool, prompt)
        self.assertNotIn('kanban_complete', prompt)
