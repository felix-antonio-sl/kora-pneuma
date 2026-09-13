"""Real loopback HTTP and subprocess restart tests, exclusively synthetic state."""
import asyncio
from datetime import datetime, timezone
import io
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import unittest
import zipfile

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
import aiohttp
from aiohttp import web
from gtd_felix.application import create_app, load_config, writer_lock
from gtd_felix.service import GTDService
from gtd_felix.control import ExecutionControl

OWNER = 'synthetic-owner-token'
PRINCIPAL = 'synthetic-agent-token'
EXECUTOR = 'synthetic-worker-token'


def config(root, port=0):
    return {'data_dir': str(Path(root) / 'state'), 'listen_host': '127.0.0.1', 'port': port,
        'actors': {'owner': 'felix', 'principal': 'gtd-felix', 'executors': ['worker']},
        'api_tokens': {OWNER: 'felix', PRINCIPAL: 'gtd-felix', EXECUTOR: 'worker'}, 'body_limit': 2048}


class HTTPTests(unittest.IsolatedAsyncioTestCase):
    async def test_source_provider_shorthand_and_invalid_shape(self):
        mail = self.service.capture('felix', 'mail-source', 'Synthetic mail', source={'provider': 'gmail'})['item']
        self.service.capture('felix', 'calendar-source', 'Synthetic appointment', source={'provider': 'calendar'})
        for source in ('gmail', {'provider': 'gmail'}):
            async with self.session.get(self.url + '/v1/items', params={'filters': json.dumps({'source': source})},
                    headers={'Authorization': 'Bearer ' + PRINCIPAL}) as response:
                self.assertEqual(response.status, 200)
                self.assertEqual([item['id'] for item in await response.json()], [mail['id']])
        for source in (None, [], 7, ''):
            async with self.session.get(self.url + '/v1/items', params={'filters': json.dumps({'source': source})},
                    headers={'Authorization': 'Bearer ' + PRINCIPAL}) as response:
                self.assertEqual(response.status, 400)
                self.assertEqual((await response.json())['status'], 'rejected')

    async def asyncSetUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.config = config(self.temp.name)
        self.lock = writer_lock(self.config['data_dir'])
        self.lock.__enter__()
        self.service = GTDService(Path(self.config['data_dir']), executor_actors=['worker'])
        self.control = ExecutionControl(self.service, {})
        self.runner = web.AppRunner(create_app(self.service, self.control, self.config), access_log=None)
        await self.runner.setup()
        site = web.TCPSite(self.runner, '127.0.0.1', 0)
        await site.start()
        self.url = 'http://127.0.0.1:' + str(site._server.sockets[0].getsockname()[1])
        self.session = aiohttp.ClientSession()

    async def test_source_coverage_owner_principal_only_and_legacy_unknown(self):
        for token in (OWNER, PRINCIPAL):
            async with self.session.get(self.url+'/v1/sources',headers={'Authorization':'Bearer '+token}) as response:
                self.assertEqual(response.status,200)
                result=await response.json()
                self.assertIsNone(result['external_sources_current'])
                self.assertFalse(result['external_sources_applicable'])
        async with self.session.get(self.url+'/v1/sources',headers={'Authorization':'Bearer '+EXECUTOR}) as response:
            self.assertEqual(response.status,403)

    async def test_configured_unread_source_visible_without_any_item(self):
        from gtd_felix.source_monitor import SourceMonitor
        monitor=SourceMonitor(self.service,{'poll_interval_seconds':60,'stale_after_seconds':120,
            'accounts':{'selected':{'transport':{'account':'synthetic@example.invalid','token_file':str(Path(self.temp.name)/'absent'),'gmail':True},
            'sources':{'mail':{'provider':'gmail','account':'synthetic@example.invalid','scope':'whole_mailbox'}}}}})
        try:
            async with self.session.get(self.url+'/v1/sources',headers={'Authorization':'Bearer '+PRINCIPAL}) as response:
                result=await response.json()
                self.assertFalse(result['external_sources_current'])
                self.assertEqual(result['sources'][0]['health'],'not_read')
            async with self.session.get(self.url+'/v1/review',headers={'Authorization':'Bearer '+PRINCIPAL}) as response:
                result=await response.json()
                self.assertFalse(result['external_sources_current'])
                self.assertTrue(result['notification_allowed'])
        finally:
            await monitor.close()

    async def asyncTearDown(self):
        await self.session.close()
        await self.runner.cleanup()
        self.service.close()
        self.lock.__exit__(None, None, None)
        self.temp.cleanup()

    async def request(self, method, path, token=OWNER, **kwargs):
        async with self.session.request(method, self.url + path, headers={'Authorization': 'Bearer ' + token}, **kwargs) as response:
            return response.status, await response.json()

    async def test_job_history_requires_bounded_principal_and_preserves_owner_view(self):
        for token in (PRINCIPAL, EXECUTOR):
            status, receipt = await self.request('GET', '/v1/jobs', token=token)
            self.assertEqual(status, 403)
            self.assertEqual(receipt['status'], 'rejected')
        status, jobs = await self.request('GET', '/v1/jobs')
        self.assertEqual(status, 200)
        self.assertEqual(jobs, self.control.pending())
        status, receipt = await self.request('GET', '/v1/jobs?target_job_id=unrelated', token=PRINCIPAL)
        self.assertEqual(status, 400)

    async def test_material_content_scope_and_individual_provenance(self):
        item = self.service.capture('felix', 'read-source', 'Source')['item']
        result = self.service.execute('felix', {'operation_id': 'read-material', 'action': 'put_material',
            'item_id': item['id'], 'expected_version': item['version'], 'fields': {'content': 'Exact content'}})
        material = result['item']['materials'][0]
        path = '/v1/materials/' + item['id'] + '/' + material['id'] + '/1'
        status, value = await self.request('GET', path)
        self.assertEqual(status, 200); self.assertEqual(value['content'], 'Exact content')
        status, value = await self.request('GET', path, token=EXECUTOR)
        self.assertEqual(status, 404); self.assertNotIn('content', value)
        status, value = await self.request('GET', path + '?path=anything')
        self.assertEqual(status, 400); self.assertNotIn('content', value)
        status, value = await self.request('GET', '/v1/items/' + item['id'])
        self.assertIn('field_provenance', value)

    def private_job(self, text='Human source remains unadopted', source=None):
        self.control.config = dict(period_start=datetime.now(timezone.utc).isoformat(), period_seconds=3600,
            max_cost_usd=10, max_runtime_seconds=1000, recovery_cost_usd=1, recovery_runtime_seconds=50,
            max_active=2, max_job_runtime_seconds=300, max_retries=0, max_descendants=1)
        source = self.service.capture('felix', 'private-source', text, source=source)['item']
        self.control.register_bot('felix', 'private-bot', {'id': 'principal', 'state': 'available',
            'source_urn': 'urn:test:principal', 'host': 'synthetic', 'profile': 'fixture',
            'capabilities': ['prepare_private'], 'probe_evidence': 'fixture://probe'})
        receipt = self.control.reserve('gtd-felix', 'private-reserve', {'item_id': source['id'], 'expected_version': source['version'],
            'capability': 'prepare_private', 'bot_id': 'principal', 'mandate_id': None, 'purpose': 'Private preparation',
            'scope': 'Prepare without adopting source', 'max_cost_usd': 2, 'max_runtime_seconds': 60, 'max_retries': 0, 'max_descendants': 0})
        self.assertEqual(receipt['status'], 'reserved', receipt)
        return source, receipt['job_id']

    async def agent_command(self, job_id, item, operation, action, fields):
        async with self.session.post(self.url + '/v1/agent/command',
            headers={'Authorization': 'Bearer ' + PRINCIPAL, 'X-GTD-Job-ID': job_id},
            json={'operation_id': operation, 'action': action, 'item_id': item['id'], 'expected_version': item['version'], 'fields': fields}) as response:
            return await response.json()

    async def test_explicit_private_root_review_material_and_completion_preserve_other_commitments(self):
        source, job = self.private_job('Revisa privadamente mis asuntos y prepara un resumen; no decidas por mí.')
        other = self.service.capture('felix', 'other-human-commitment', 'Human decision remains pending')['item']
        other = self.service.execute('felix', {'operation_id': 'other-human-clarify', 'action': 'clarify', 'item_id': other['id'],
            'expected_version': other['version'], 'fields': {'kind': 'action', 'commitment': 'committed',
                'decision_needed': True, 'decision_question': 'Which human option should I choose?'}})['item']
        clarified = await self.agent_command(job, source, 'explicit-private-clarify', 'clarify',
            {'kind': 'action', 'commitment': 'committed', 'capability': 'prepare_private',
                'completion_criteria': 'Review recorded subjects and prepare a private summary preserving human questions',
                'intent_basis': {'source_item_id': source['id'], 'quote': source['text']}})
        self.assertEqual(clarified['status'], 'applied', clarified)
        item = clarified['item']
        self.assertEqual(item['work_capability'], 'prepare_private')
        self.assertEqual(item['executor'], 'gtd-felix')
        self.assertFalse(item.get('mandate_id'))
        review = await self.agent_command(job, item, 'explicit-private-review', 'review', {})
        self.assertEqual(review['status'], 'applied', review)
        self.assertTrue(review['review']['human_decision_pending'])
        material = await self.agent_command(job, item, 'explicit-private-material', 'put_material',
            {'content': 'Private review: the recorded human choice remains pending; no commitment was changed.'})
        self.assertEqual(material['status'], 'applied', material)
        complete = await self.agent_command(job, material['item'], 'explicit-private-assess', 'assess_result',
            {'satisfied': True, 'evidence': 'Actual review receipt and private summary exist; human choice remains pending'})
        self.assertEqual(complete['status'], 'applied', complete)
        self.assertEqual(complete['item']['status'], 'done')
        self.assertEqual(complete['item']['original'], source['original'])
        self.assertEqual(complete['item']['source_revisions'], source['source_revisions'])
        self.assertEqual(self.service.get_item(other['id']), other)
        self.assertEqual(self.service.mandates(), [])
        self.assertIsNotNone(self.control.own_terminal_progress(job))

    async def explicit_private_root(self):
        source, job = self.private_job('Revisa privadamente mis asuntos y prepara un resumen.')
        clarified = await self.agent_command(job, source, 'scope-private-root', 'clarify',
            {'kind': 'action', 'commitment': 'committed', 'capability': 'prepare_private',
             'completion_criteria': 'A private review and summary',
             'intent_basis': {'source_item_id': source['id'], 'quote': source['text']}})
        self.assertEqual(clarified['status'], 'applied', clarified)
        return clarified['item'], job

    def finish_scope_job(self, job):
        result = self.control.observe(job, {'native_identity': {'provider': 'fixture', 'host': 'synthetic', 'profile': 'fixture', 'id': job},
            'native_status': 'completed', 'terminal': True, 'cost_usd': .1, 'runtime_seconds': 1, 'evidence_reference': 'fixture://scope-terminal'})
        self.assertEqual(result['status'], 'recorded', result)

    def reserve_private_scope(self, root, previous_job, operation, mandate_id=None):
        previous = self.control.get_job(previous_job)
        request = {key: previous[key] for key in ('capability', 'bot_id', 'purpose', 'scope', 'max_cost_usd', 'max_runtime_seconds', 'max_retries', 'max_descendants')}
        reserved = self.control.reserve('gtd-felix', operation, {**request, 'item_id': root['id'], 'expected_version': root['version'], 'mandate_id': mandate_id})
        self.assertEqual(reserved['status'], 'reserved', reserved)
        return reserved['job_id']

    async def assert_fresh_private_scope_rejects_changed_meaning(self, fields):
        root, old = await self.explicit_private_root()
        self.finish_scope_job(old)
        changed = self.service.execute('felix', {'operation_id': 'private-scope-edit', 'action': 'edit',
            'item_id': root['id'], 'expected_version': root['version'], 'fields': fields})
        self.assertEqual(changed['status'], 'applied', changed)
        root = changed['item']
        fresh = self.reserve_private_scope(root, old, 'fresh-after-meaning')
        material = await self.agent_command(fresh, root, 'private-continued-preparation', 'put_material', {'content': 'Private preparation may continue despite unresolved closure authority'})
        self.assertEqual(material['status'], 'applied', material)
        root = material['item']
        denied = await self.agent_command(fresh, root, 'private-obsolete-closure', 'assess_result',
            {'satisfied': True, 'evidence': 'Old interpretation cannot authorize the changed human scope'})
        self.assertEqual(denied['status'], 'rejected', denied)
        self.assertEqual(denied['error'], 'human_position_protected')
        self.assertEqual(self.service.get_item(root['id']), root)
        self.assertEqual(root['status'], 'active')

    async def test_new_reservation_cannot_reuse_private_scope_after_executor_change(self):
        await self.assert_fresh_private_scope_rejects_changed_meaning({'executor': 'felix'})

    async def test_new_reservation_cannot_reuse_private_scope_after_outcome_change(self):
        await self.assert_fresh_private_scope_rejects_changed_meaning({'outcome': 'Different human outcome'})

    async def test_new_reservation_cannot_reuse_private_scope_after_criterion_change(self):
        await self.assert_fresh_private_scope_rejects_changed_meaning({'completion_criteria': 'New human acceptance criterion'})

    async def test_compatible_note_and_fresh_reservation_allow_private_closure(self):
        root, old = await self.explicit_private_root()
        self.finish_scope_job(old)
        noted = self.service.execute('felix', {'operation_id': 'private-scope-note', 'action': 'edit',
            'item_id': root['id'], 'expected_version': root['version'], 'fields': {'notes': 'Compatible human annotation'}})
        self.assertEqual(noted['status'], 'applied', noted)
        root = noted['item']
        fresh = self.reserve_private_scope(root, old, 'fresh-after-note')
        closed = await self.agent_command(fresh, root, 'note-compatible-close', 'assess_result',
            {'satisfied': True, 'evidence': 'Fixture verified the original unchanged private criterion'})
        self.assertEqual(closed['status'], 'applied', closed)
        self.assertEqual(closed['item']['status'], 'done')

    async def test_new_reservation_cannot_close_private_root_while_paused_postponed_or_waiting(self):
        root, old = await self.explicit_private_root()
        for index, status in enumerate(('postponed', 'paused', 'waiting')):
            self.finish_scope_job(old)
            if status == 'postponed':
                updated = self.service.execute('felix', {'operation_id': 'private-postpone', 'action': 'postpone',
                    'item_id': root['id'], 'expected_version': root['version'], 'fields': {'review_at': '2999-01-01T00:00:00+00:00'}})
            elif status == 'paused':
                updated = self.service.execute('felix', {'operation_id': 'private-pause', 'action': 'pause',
                    'item_id': root['id'], 'expected_version': root['version'], 'fields': {}})
            else:
                # Seed waiting through the trusted Store fixture.
                with self.service.store.transaction():
                    item, versions = self.service._item(root['id'])
                    updated = self.service._apply_updates('felix', f'fixture-private-{status}', 'fixture-digest', item, versions, {'status': status})
            self.assertEqual(updated['status'], 'applied', updated)
            root = updated['item']
            if status == 'paused':
                previous = self.control.get_job(old)
                request = {key: previous[key] for key in ('capability', 'bot_id', 'purpose', 'scope',
                    'max_cost_usd', 'max_runtime_seconds', 'max_retries', 'max_descendants')}
                denied = self.control.reserve('gtd-felix', f'fresh-paused-scope-{index}',
                    {**request, 'item_id': root['id'], 'expected_version': root['version'], 'mandate_id': None})
                self.assertEqual(denied['status'], 'rejected', denied)
                self.assertEqual(denied['error'], 'work_paused')
                self.assertEqual(self.service.get_item(root['id']), root)
                read_status, readable = await self.request('GET', '/v1/items/' + root['id'], token=PRINCIPAL)
                self.assertEqual(read_status, 200)
                self.assertEqual(readable['status'], 'paused')
                continue
            fresh = self.reserve_private_scope(root, old, f'fresh-paused-scope-{index}')
            denied = await self.agent_command(fresh, root, f'paused-private-close-{index}', 'assess_result',
                {'satisfied': True, 'evidence': 'No closure while this work is paused'})
            self.assertEqual(denied['status'], 'rejected', denied)
            self.assertEqual(denied['error'], 'work_paused')
            self.assertEqual(self.service.get_item(root['id']), root)
            old = fresh

    async def test_new_explicit_mandate_can_authorize_changed_private_scope(self):
        root, old = await self.explicit_private_root()
        self.finish_scope_job(old)
        changed = self.service.execute('felix', {'operation_id': 'private-new-criterion', 'action': 'edit', 'item_id': root['id'],
            'expected_version': root['version'], 'fields': {'completion_criteria': 'New explicit private criterion'}})
        self.assertEqual(changed['status'], 'applied', changed)
        root = changed['item']
        granted = self.service.execute('felix', {'operation_id': 'private-renewed-mandate', 'action': 'grant_mandate',
            'item_id': root['id'], 'expected_version': root['version'], 'fields': {'scope_item_id': root['id'],
                'capabilities': ['prepare_private'], 'actors': ['gtd-felix'], 'completion_criteria': 'New explicit private criterion'}})
        self.assertEqual(granted['status'], 'applied', granted)
        root = granted['item']
        fresh = self.reserve_private_scope(root, old, 'fresh-explicit-scope', granted['mandate']['id'])
        closed = await self.agent_command(fresh, root, 'renewed-scope-close', 'assess_result',
            {'satisfied': True, 'evidence': 'Fixture verified the explicitly renewed private criterion', 'mandate_id': granted['mandate']['id']})
        self.assertEqual(closed['status'], 'applied', closed)
        self.assertEqual(closed['item']['status'], 'done')

    async def test_owner_retains_authority_after_changing_private_criterion(self):
        root, _ = await self.explicit_private_root()
        changed = self.service.execute('felix', {'operation_id': 'owner-private-criterion', 'action': 'edit', 'item_id': root['id'],
            'expected_version': root['version'], 'fields': {'completion_criteria': 'Criterion now decided by owner'}})
        self.assertEqual(changed['status'], 'applied', changed)
        _, closed = await self.request('POST', '/v1/commands', json={'operation_id': 'owner-private-assess', 'action': 'assess_result',
            'item_id': root['id'], 'expected_version': changed['item']['version'], 'fields': {'satisfied': True, 'evidence': 'Owner explicitly verified their new criterion'}})
        self.assertEqual(closed['status'], 'applied', closed)
        self.assertEqual(closed['item']['status'], 'done')

    async def test_fresh_job_cannot_clear_or_rewrite_owner_decision_even_after_identical_echo(self):
        source, old = self.private_job()
        corrected = self.service.execute('felix', {'operation_id': 'owner-decision', 'action': 'edit',
            'item_id': source['id'], 'expected_version': source['version'],
            'fields': {'decision_needed': True, 'decision_question': 'Which human option should I choose?'}})
        self.assertEqual(corrected['status'], 'applied', corrected)
        root = corrected['item']
        self.finish_scope_job(old)
        job = self.reserve_private_scope(root, old, 'fresh-owner-decision')
        for operation, fields in [('erase-owner-decision', {'decision_needed': False}),
            ('rewrite-owner-question', {'decision_question': 'An agent replacement question'}),
            ('mixed-plan-and-erasure', {'plan_steps': ['A step that must not leak through'], 'decision_needed': False})]:
            rejected = await self.agent_command(job, root, operation, 'plan', fields)
            self.assertEqual(rejected['status'], 'rejected', rejected)
            self.assertEqual(self.service.get_item(root['id']), root)
            self.assertIn(root['id'], [item['id'] for item in self.service.review_state()['human_decisions']])
        planned = await self.agent_command(job, root, 'plan-preserving-question', 'plan', {'plan_steps': ['Prepare information for the human choice']})
        self.assertEqual(planned['status'], 'applied', planned)
        root = planned['item']
        echoed = await self.agent_command(job, root, 'echo-owner-decision', 'plan',
            {'decision_needed': True, 'decision_question': root['decision_question']})
        self.assertEqual(echoed['status'], 'applied', echoed)
        root = echoed['item']
        _, versions = self.service._item(root['id'])
        self.assertEqual(versions['decision_needed']['actor'], 'felix')
        self.assertEqual(versions['decision_question']['actor'], 'felix')
        second = await self.agent_command(job, root, 'erase-after-echo', 'plan', {'decision_needed': False})
        self.assertEqual(second['status'], 'rejected', second)
        self.assertEqual(self.service.get_item(root['id']), root)
        resolved = self.service.execute('felix', {'operation_id': 'owner-resolves-decision', 'action': 'edit',
            'item_id': root['id'], 'expected_version': root['version'], 'fields': {'decision_needed': False}})
        self.assertEqual(resolved['status'], 'applied', resolved)
        self.assertNotIn(root['id'], [item['id'] for item in self.service.review_state()['human_decisions']])

    async def test_principal_can_manage_its_own_new_decision_question(self):
        root, job = self.private_job()
        raised = await self.agent_command(job, root, 'principal-new-question', 'plan',
            {'decision_needed': True, 'decision_question': 'Which missing input is needed for this private draft?'})
        self.assertEqual(raised['status'], 'applied', raised)
        changed = await self.agent_command(job, raised['item'], 'principal-own-question-update', 'plan',
            {'decision_question': 'Which source should this draft cite?'})
        self.assertEqual(changed['status'], 'applied', changed)
        resolved = await self.agent_command(job, changed['item'], 'principal-own-question-resolved', 'plan', {'decision_needed': False})
        self.assertEqual(resolved['status'], 'applied', resolved)
        self.assertFalse(resolved['item']['decision_needed'])
        self.assertEqual(resolved['item']['decision_question'], 'Which source should this draft cite?')

    async def test_general_action_without_explicit_private_capability_still_requires_mandate(self):
        source, job = self.private_job('Llama al proveedor mañana.')
        clarified = await self.agent_command(job, source, 'general-action', 'clarify', {'kind': 'action', 'commitment': 'committed',
            'completion_criteria': 'Supplier contacted', 'intent_basis': {'source_item_id': source['id'], 'quote': source['text']}})
        self.assertEqual(clarified['status'], 'applied', clarified)
        denied = await self.agent_command(job, clarified['item'], 'general-close', 'assess_result', {'satisfied': True, 'evidence': 'Text is not authority'})
        self.assertEqual(denied['status'], 'rejected', denied)
        self.assertEqual(denied['error'], 'mandate_required')
        self.assertEqual(self.service.get_item(source['id'])['status'], 'active')

    async def test_private_intent_rejects_forged_capability_human_executor_and_reconfiguration(self):
        source, job = self.private_job('Prepare a private summary.')
        fields = {'kind': 'action', 'commitment': 'committed', 'capability': 'prepare_private', 'completion_criteria': 'A private summary',
            'intent_basis': {'source_item_id': source['id'], 'quote': source['text']}}
        for operation, invalid in [('human-executor', {**fields, 'executor': 'felix'}),
                                   ('forged-internal-capability', {**fields, 'work_capability': 'prepare_private'})]:
            denied = await self.agent_command(job, source, operation, 'clarify', invalid)
            self.assertEqual(denied['status'], 'rejected', denied)
        accepted = await self.agent_command(job, source, 'proper-private', 'clarify', fields)
        self.assertEqual(accepted['status'], 'applied', accepted)
        changed = await self.agent_command(job, accepted['item'], 'reconfigure-private', 'clarify', fields)
        self.assertEqual(changed['status'], 'rejected', changed)
        self.assertEqual(self.service.get_item(source['id']), accepted['item'])

    async def test_forwarded_third_party_cannot_declare_private_root_intent(self):
        source, job = self.private_job('Prepare this review.', source={'provider': 'telegram', 'third_party': True})
        denied = await self.agent_command(job, source, 'third-party-private', 'clarify', {'kind': 'action', 'commitment': 'committed',
            'capability': 'prepare_private', 'completion_criteria': 'A private review',
            'intent_basis': {'source_item_id': source['id'], 'quote': source['text']}})
        self.assertEqual(denied['status'], 'rejected', denied)
        self.assertEqual(self.service.get_item(source['id']), source)

    async def test_private_child_can_be_prepared_and_completed_without_adopting_source(self):
        source, job = self.private_job()
        derived = await self.agent_command(job, source, 'private-derive', 'derive', {'kind': 'action',
            'title': 'Prepare private draft', 'capability': 'prepare_private', 'completion_criteria': 'Draft includes the stated synthetic facts'})
        self.assertEqual(derived['status'], 'applied', derived)
        child = derived['item']
        self.assertEqual(child['work_capability'], 'prepare_private')
        self.assertIsNone(child['mandate_id'])
        material = await self.agent_command(job, child, 'private-material', 'put_material', {'content': 'Private draft with verified synthetic facts'})
        self.assertEqual(material['status'], 'applied', material)
        completed = await self.agent_command(job, material['item'], 'private-assessment', 'assess_result',
            {'satisfied': True, 'evidence': 'Fixture verified that the private draft includes the declared facts'})
        self.assertEqual(completed['status'], 'applied', completed)
        self.assertEqual(completed['item']['status'], 'done')
        self.assertEqual(self.service.get_item(source['id']), source)
        self.assertEqual(self.control.get_job(job)['progress'][-1]['operation_id'], 'private-assessment')
        replay = await self.agent_command(job, material['item'], 'private-assessment', 'assess_result',
            {'satisfied': True, 'evidence': 'Fixture verified that the private draft includes the declared facts'})
        self.assertEqual(replay['status'], 'already_applied', replay)

    async def test_private_root_assessment_rechecks_descendants_before_closing(self):
        source, original_job = self.private_job()
        derived = await self.agent_command(original_job, source, 'private-root-work', 'derive', {'kind': 'action',
            'title': 'Private preparation root', 'capability': 'prepare_private', 'completion_criteria': 'Verified private contribution'})
        self.assertEqual(derived['status'], 'applied', derived)
        root = derived['item']
        nested = await self.agent_command(original_job, root, 'private-nested-work', 'derive', {'kind': 'action',
            'title': 'Private child contribution', 'capability': 'prepare_private', 'completion_criteria': 'Verified child'})
        self.assertEqual(nested['status'], 'applied', nested)
        child = nested['item']
        previous = self.control.get_job(original_job)
        request = {key: previous[key] for key in ('mandate_id', 'capability', 'bot_id', 'purpose', 'scope', 'max_cost_usd', 'max_runtime_seconds', 'max_retries', 'max_descendants')}
        reserved = self.control.reserve('gtd-felix', 'private-root-reserve', {**request, 'item_id': root['id'], 'expected_version': root['version']})
        self.assertEqual(reserved['status'], 'reserved', reserved)
        job = reserved['job_id']
        note = self.service.execute('felix', {'operation_id': 'private-child-note', 'action': 'edit', 'item_id': child['id'],
            'expected_version': child['version'], 'fields': {'notes': 'Compatible annotation'}})
        self.assertEqual(note['status'], 'applied', note)
        checked = await self.agent_command(job, root, 'private-root-check', 'assess_result',
            {'satisfied': False, 'evidence': 'Assessment allowed with compatible annotation', 'gap': 'Contribution still being checked'})
        self.assertEqual(checked['status'], 'applied', checked)
        root = checked['item']
        corrected = self.service.execute('felix', {'operation_id': 'private-child-correction', 'action': 'edit', 'item_id': child['id'],
            'expected_version': note['item']['version'], 'fields': {'text': 'Material human correction'}})
        self.assertEqual(corrected['status'], 'applied', corrected)
        denied = await self.agent_command(job, root, 'private-root-must-not-close', 'assess_result',
            {'satisfied': True, 'evidence': 'Old child evidence cannot close this root'})
        self.assertEqual(denied['status'], 'rejected', denied)
        self.assertEqual(denied['error'], 'stale_descendant_version')
        self.assertEqual(self.service.get_item(root['id']), root)
        self.assertEqual(root['status'], 'active')
        self.assertEqual(self.service.get_item(source['id']), source)

    async def test_private_assessment_cannot_reduce_root_authority_or_escape_scope(self):
        source, job = self.private_job()
        for operation, fields in [('root-close', {'satisfied': True, 'evidence': 'Not authority'}),
            ('spoof-capability', {'satisfied': True, 'evidence': 'Not authority', 'work_capability': 'prepare_private', 'capability': 'prepare_private'})]:
            result = await self.agent_command(job, source, operation, 'assess_result', fields)
            self.assertEqual(result['status'], 'rejected', result)
        outside = self.service.capture('felix', 'private-outsider', 'Unrelated source')['item']
        denied = await self.agent_command(job, outside, 'outside-assessment', 'assess_result', {'satisfied': True, 'evidence': 'No scope'})
        self.assertEqual(denied['status'], 'rejected', denied)
        self.assertEqual(self.service.get_item(source['id']), source)
        self.assertEqual(self.service.get_item(outside['id']), outside)

    async def test_auth_actor_injection_query_command_and_export(self):
        self.assertEqual((200, {'status': 'ok'}), await self.request('GET', '/health', token=''))
        self.assertEqual(401, (await self.request('GET', '/v1/items', token='unknown'))[0])
        status, cap = await self.request('GET', '/v1/capabilities', token=PRINCIPAL)
        self.assertEqual('principal', cap['role'])
        _, denied = await self.request('POST', '/v1/commands', token=PRINCIPAL,
            json={'actor': 'felix', 'operation_id': 'spoof-owner', 'action': 'set_attention', 'fields': {'paused': True}})
        self.assertEqual('rejected', denied['status'])
        self.assertEqual('agent_action_not_enabled', denied['error'])
        status, capture = await self.request('POST', '/v1/captures', json={'actor': 'intruder', 'operation_id': 'capture-http', 'text': 'Synthetic'})
        self.assertEqual('applied', capture['status'])
        item = capture['item']
        actor = self.service.store.db.execute('SELECT actor FROM operations WHERE operation_id=?', ('capture-http',)).fetchone()[0]
        self.assertEqual('felix', actor)
        self.assertEqual(item['id'], (await self.request('GET', '/v1/items'))[1][0]['id'])
        self.assertEqual(item['id'], (await self.request('GET', '/v1/items/' + item['id']))[1]['id'])
        status, receipt = await self.request('POST', '/v1/commands', json={'operation_id': 'edit-http', 'action': 'edit', 'item_id': item['id'], 'expected_version': item['version'], 'fields': {'title': 'Edited'}})
        self.assertEqual('applied', receipt['status'])
        self.assertEqual(200, (await self.request('GET', '/v1/review'))[0])
        self.assertEqual([], (await self.request('GET', '/v1/materials/' + item['id']))[1])
        self.assertEqual(403, (await self.request('GET', '/v1/export', token=PRINCIPAL))[0])
        async with self.session.get(self.url + '/v1/export', headers={'Authorization': 'Bearer ' + OWNER}) as response:
            self.assertEqual(200, response.status)
            with zipfile.ZipFile(io.BytesIO(await response.read())) as archive:
                self.assertIsNone(archive.testzip())

    async def test_control_boundary_budget_and_sanitized_errors(self):
        self.assertEqual(200, (await self.request('POST', '/v1/control/budget', json={}))[0])
        _, registered = await self.request('POST', '/v1/control/register_bot', token=OWNER,
            json={'operation_id': 'planned-bot', 'bot': {'id': 'synthetic-bot', 'state': 'planned'}})
        self.assertEqual('applied', registered['status'])
        self.assertEqual(1, len((await self.request('POST', '/v1/control/bots', json={}))[1]))
        _, reserved = await self.request('POST', '/v1/control/reserve', token=PRINCIPAL,
            json={'operation_id': 'no-budget', 'request': {}})
        self.assertEqual('rejected', reserved['status'])
        self.assertEqual(403, (await self.request('POST', '/v1/control/budget', token=EXECUTOR, json={}))[0])
        for operation in ('record_dispatch', 'observe', 'record_integration', 'unknown'):
            self.assertEqual(404, (await self.request('POST', '/v1/control/' + operation, json={}))[0])
        self.assertEqual(413, (await self.request('POST', '/v1/captures', json={'text': 'x' * 3000}))[0])
        self.assertEqual(400, (await self.request('POST', '/v1/captures', data='{bad'))[0])
        self.service.query = lambda *a: (_ for _ in ()).throw(RuntimeError('secret personal detail'))
        status, error = await self.request('GET', '/v1/items')
        self.assertEqual(503, status)
        self.assertNotIn('secret', json.dumps(error))
        self.assertEqual(200, (await self.request('GET', '/health'))[0])

    async def test_executor_reads_only_live_mandate_scope(self):
        visible = self.service.capture('felix', 'scope-visible', 'Visible synthetic')['item']
        hidden = self.service.capture('felix', 'scope-hidden', 'Hidden synthetic')['item']
        self.assertEqual([], (await self.request('GET', '/v1/items', token=EXECUTOR))[1])
        visible = self.service.execute('felix', {'operation_id': 'clarify-scope', 'action': 'clarify',
            'item_id': visible['id'], 'expected_version': visible['version'], 'fields': {'kind': 'action'}})['item']
        mandate = self.service.execute('felix', {'operation_id': 'grant-scope', 'action': 'grant_mandate',
            'item_id': visible['id'], 'expected_version': visible['version'], 'fields': {
                'scope_item_id': visible['id'], 'capabilities': ['prepare_private'],
                'actors': ['worker'], 'completion_criteria': 'Synthetic acceptance'}})
        self.assertEqual('applied', mandate['status'])
        self.assertEqual([], (await self.request('GET', '/v1/items', token=EXECUTOR))[1])
        self.assertEqual(404, (await self.request('GET', '/v1/items/' + visible['id'], token=EXECUTOR))[0])
        for prefix in ('/v1/items/', '/v1/materials/'):
            self.assertEqual(404, (await self.request('GET', prefix + hidden['id'], token=EXECUTOR))[0])
        self.assertEqual(403, (await self.request('GET', '/v1/review', token=EXECUTOR))[0])
        cap = (await self.request('GET', '/v1/capabilities', token=EXECUTOR))[1]
        self.assertEqual([], cap['control'])
        self.assertNotIn('review', cap['operations'])
        self.assertNotIn('export', cap['operations'])

    async def test_writer_lock_and_private_configuration(self):
        with self.assertRaisesRegex(ValueError, 'writer_already_running'):
            with writer_lock(self.config['data_dir']):
                self.fail('second writer acquired lock')
        path = Path(self.temp.name) / 'config.json'
        path.write_text(json.dumps(self.config))
        path.chmod(0o600)
        self.assertEqual(self.config, load_config(path))
        path.chmod(0o644)
        with self.assertRaises(ValueError):
            load_config(path)
        path.chmod(0o600)
        link = path.with_name('symlink.json')
        link.symlink_to(path)
        with self.assertRaises(ValueError):
            load_config(link)

    async def test_cli_against_live_http(self):
        env = {**os.environ, 'PYTHONPATH': str(RUNTIME), 'GTD_API_URL': self.url, 'GTD_API_TOKEN': OWNER}
        proc = await asyncio.create_subprocess_exec(sys.executable, '-B', '-m', 'gtd_felix', 'capture',
            env=env, stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await proc.communicate(json.dumps({'operation_id': 'cli', 'text': 'CLI synthetic'}).encode())
        self.assertEqual(0, proc.returncode, stderr)
        self.assertEqual('applied', json.loads(stdout)['status'])


class ProcessTests(unittest.IsolatedAsyncioTestCase):
    async def test_process_restart_retains_capture_and_rejects_second_writer(self):
        with tempfile.TemporaryDirectory() as temp:
            with socket.socket() as sock:
                sock.bind(('127.0.0.1', 0))
                port = sock.getsockname()[1]
            settings = config(temp, port)
            path = Path(temp) / 'config.json'
            path.write_text(json.dumps(settings)); path.chmod(0o600)
            env = {**os.environ, 'PYTHONPATH': str(RUNTIME)}
            args = (sys.executable, '-B', '-m', 'gtd_felix', 'serve', '--config', str(path))
            async with aiohttp.ClientSession() as session:
                for iteration in range(2):
                    process = await asyncio.create_subprocess_exec(*args, env=env, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
                    try:
                        url = f'http://127.0.0.1:{port}'
                        for attempt in range(100):
                            if process.returncode is not None:
                                self.fail((await process.communicate())[1].decode())
                            try:
                                async with session.get(url + '/health') as response:
                                    if response.status == 200:
                                        break
                            except aiohttp.ClientError:
                                pass
                            await asyncio.sleep(.05)
                        else:
                            self.fail('service_start_timeout')
                        headers = {'Authorization': 'Bearer ' + OWNER}
                        if iteration == 0:
                            second = await asyncio.create_subprocess_exec(*args, env=env, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
                            _, error = await asyncio.wait_for(second.communicate(), 5)
                            self.assertEqual(1, second.returncode)
                            self.assertNotIn(OWNER, error.decode())
                            async with session.post(url + '/v1/captures', headers=headers, json={'operation_id': 'restart', 'text': 'Survives process'}) as response:
                                self.assertEqual('applied', (await response.json())['status'])
                        else:
                            async with session.get(url + '/v1/items', headers=headers) as response:
                                self.assertEqual('Survives process', (await response.json())[0]['title'])
                    finally:
                        if process.returncode is None:
                            process.terminate()
                        await asyncio.wait_for(process.communicate(), 10)


class BotBootstrapTests(unittest.IsolatedAsyncioTestCase):
    async def test_restart_does_not_revive_suspended_bot_or_probe_its_route(self):
        from datetime import datetime, timezone
        from gtd_felix.cli import bootstrap_bots
        with tempfile.TemporaryDirectory() as temp:
            configured = dict(id='principal', actor='gtd-felix', state='available', source_urn='urn:test:principal',
                profile='fixture', host='synthetic', capabilities=['prepare_private'], probe_evidence='fixture://initial')
            service = GTDService(Path(temp) / 'state')
            limits = dict(period_start=datetime.now(timezone.utc).isoformat(), period_seconds=3600,
                max_cost_usd=2, max_runtime_seconds=100, recovery_cost_usd=.1, recovery_runtime_seconds=10,
                max_job_runtime_seconds=50, max_retries=0, max_descendants=0, max_active=1)
            control = ExecutionControl(service, limits)
            self.assertEqual(control.register_bot('felix', 'initial', configured)['status'], 'applied')
            self.assertEqual(control.register_bot('felix', 'human-suspend', dict(configured, state='suspended'))['status'], 'applied')
            item = service.capture('felix', 'capture', 'Capture while execution is suspended')['item']
            service.close()
            service = GTDService(Path(temp) / 'state')
            try:
                control = ExecutionControl(service, limits)
                class Native:
                    calls = 0
                    async def discover(self, bot_id):
                        self.calls += 1
                        return {'status': 'ready', 'evidence_reference': 'fixture://new-probe'}
                native = Native()
                await bootstrap_bots(service, control, native, [configured])
                self.assertEqual(control.bots()[0]['state'], 'suspended')
                self.assertEqual(native.calls, 0)
                receipt = control.reserve('gtd-felix', 'after-restart', dict(item_id=item['id'], expected_version=item['version'],
                    bot_id='principal', mandate_id=None, capability='prepare_private', purpose='Prepare', scope='Synthetic',
                    max_cost_usd=.5, max_runtime_seconds=20, max_retries=0, max_descendants=0))
                self.assertEqual(receipt['error'], 'bot_unavailable')
            finally:
                service.close()


    async def test_new_and_available_bots_are_probed_at_each_bootstrap(self):
        from gtd_felix.cli import bootstrap_bots
        with tempfile.TemporaryDirectory() as temp:
            service = GTDService(Path(temp) / 'state')
            try:
                control = ExecutionControl(service, {})
                configured = dict(id='principal', actor='gtd-felix', state='available', source_urn='urn:test:principal',
                    profile='fixture', host='synthetic', capabilities=['prepare_private'])
                class Native:
                    calls = 0
                    ready = True
                    async def discover(self, bot_id):
                        self.calls += 1
                        return {'status': 'ready' if self.ready else 'blocked', 'probe_number': self.calls}
                native = Native()
                await bootstrap_bots(service, control, native, [configured])
                self.assertEqual(control.bots()[0]['state'], 'available')
                self.assertEqual(native.calls, 1)
                native.ready = False
                await bootstrap_bots(service, control, native, [configured])
                self.assertEqual(native.calls, 2)
                self.assertEqual(control.bots()[0]['state'], 'unavailable')
                self.assertEqual(service.query(), [])
            finally:
                service.close()
