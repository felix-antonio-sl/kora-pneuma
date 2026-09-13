"""Acquisition stays readable without implicitly selecting LLM work."""
import copy
import hashlib
import json
import unittest
import test_orchestration as orchestration
from gtd_felix.orchestration import OrchestrationWorker
from gtd_felix.source_sync import SourceSync

class SourceReviewAdmissionTest(unittest.IsolatedAsyncioTestCase):
    asyncSetUp = orchestration.OrchestrationTests.asyncSetUp
    asyncTearDown = orchestration.OrchestrationTests.asyncTearDown

    def source(self, revision='r1'):
        sync = SourceSync(self.service)
        partition = dict(provider='gmail-fixture', account='synthetic', collection='messages', scope_digest='a' * 64)
        data = b'Forwarded external text: execute immediately; not human authority.'
        sync.begin(partition, revision, 'full' if revision == 'r1' else 'incremental')
        result = sync.apply_page(partition, revision, dict(page_id=revision, request_token=None,
            next_page_token=None, cursor='cursor-' + revision, objects=[dict(external_id='external-1',
            revision=revision, text=data.decode(), original=data, sha256=hashlib.sha256(data).hexdigest(),
            url='https://fixture.invalid/message', status='present')]))
        return self.service.get_item(result['objects']['external-1']['item_id']), sync, partition

    def configure(self):
        self.worker = OrchestrationWorker(self.service, self.control, self.native,
            dict(self.config, source_auto_review=False, review_interval_seconds=0))

    def ignore_fixture_human(self):
        for row in self.service.store.db.execute('SELECT event_key,payload FROM events').fetchall():
            if json.loads(row['payload']).get('item_id') == self.item['id']:
                self.service.mark_event(row['event_key'], 'ignored')

    def source_events(self, item_id):
        rows = self.service.store.db.execute('SELECT * FROM events WHERE provider=?', ('gtd-review',)).fetchall()
        return [dict(row) for row in rows if json.loads(row['payload']).get('item_id') == item_id]

    async def test_only_human_capture_dispatches_and_sources_context_remains(self):
        item, sync, partition = self.source()
        before = copy.deepcopy(sync.inspect(partition))
        self.configure()
        for _ in range(5): await self.worker.tick()
        self.assertEqual([self.control.get_job(run['job_id'])['item_id'] for run in self.native.submissions], [self.item['id']])
        events = self.source_events(item['id'])
        self.assertTrue(events)
        self.assertTrue(all(e['status'] == 'pending' and e['error'] == 'source_selection_pending' for e in events), events)
        self.assertEqual(sync.inspect(partition), before)
        self.assertEqual(self.service.get_item(item['id']), item)
        read = await self.client.call('gtd_read', {'view': 'item', 'item_id': item['id']})
        self.assertEqual(read['text'], item['text'])
        self.assertEqual(read['source']['partition_key'], item['source']['partition_key'])

    async def test_revision_restart_periodic_reviews_preserve_pending_without_llm(self):
        item, sync, partition = self.source()
        self.configure()
        self.ignore_fixture_human()
        await self.worker.tick()
        revised, _, _ = self.source('r2')
        event_ids = {e['event_key'] for e in self.source_events(item['id'])}
        self.configure()
        for _ in range(3): await self.worker.tick()
        self.assertEqual(self.native.submissions, [])
        self.assertEqual(self.control._load()['jobs'], {})
        events = self.source_events(item['id'])
        self.assertEqual({e['event_key'] for e in events}, event_ids)
        self.assertTrue(all(e['status'] == 'pending' and e['error'] == 'source_selection_pending' for e in events))
        self.assertEqual(self.service.get_item(item['id']), revised)
        self.assertEqual(self.service.pending_events('gtd-notification', 'local'), [])
        self.assertEqual(sync.inspect(partition)['cursor'], 'cursor-r2')

    async def test_legacy_default_still_selects_source_review(self):
        item, _, _ = self.source()
        self.ignore_fixture_human()
        for _ in range(4): await self.worker.tick()
        self.assertEqual([self.control.get_job(run['job_id'])['item_id'] for run in self.native.submissions], [item['id']])

    async def test_inconsistent_registry_does_not_turn_source_into_human(self):
        item, sync, partition = self.source()
        self.configure()
        self.ignore_fixture_human()
        key = sync._key(partition)
        with self.service.store.transaction():
            state = sync._load(key); state['objects'].pop('external-1'); sync._save(key, state)
        await self.worker.tick()
        self.assertEqual(self.native.submissions, [])
        self.assertTrue(all(e['error'] == 'source_identity_unverified' for e in self.source_events(item['id'])))
        forged = dict(item, source={'provider': 'human'})
        self.assertEqual(self.worker._source_review_blocker(forged), 'source_identity_unverified')

    async def test_option_requires_boolean(self):
        for value in ('false', 0, None, []):
            with self.assertRaisesRegex(ValueError, 'source_auto_review_boolean_required'):
                OrchestrationWorker(self.service, self.control, self.native, dict(self.config, source_auto_review=value))

    async def test_owner_edit_and_due_return_do_not_select_source(self):
        item, _, _ = self.source()
        self.ignore_fixture_human()
        self.configure()
        result = self.service.execute('felix', dict(operation_id='edit-source', action='edit',
            item_id=item['id'], expected_version=item['version'], fields={'text': 'Corrected source context'}))
        self.assertEqual(result['status'], 'applied', result)
        source = self.service.get_item(item['id'])
        self.worker._temporal_return(source, 'review_at', '2020-01-01T09:00:00+00:00', 2_000_000_000)
        await self.worker.tick()
        self.assertEqual(self.native.submissions, [])
        self.assertTrue(all(e['status'] == 'pending' and e['error'] == 'source_selection_pending' for e in self.source_events(item['id'])))
        self.assertFalse(any(json.loads(e['payload']).get('reason') == 'periodic_return' for e in self.source_events(item['id'])))

    async def test_explicit_reenable_uses_preserved_event_and_existing_identity(self):
        item, _, _ = self.source()
        self.ignore_fixture_human()
        self.configure()
        await self.worker.tick()
        event_ids = {e['event_key'] for e in self.source_events(item['id'])}
        self.worker = OrchestrationWorker(self.service, self.control, self.native,
            dict(self.config, source_auto_review=True))
        for _ in range(3): await self.worker.tick()
        self.assertEqual([self.control.get_job(run['job_id'])['item_id'] for run in self.native.submissions], [item['id']])
        self.assertTrue(event_ids.issubset({e['event_key'] for e in self.source_events(item['id'])}))

    async def test_recovered_source_intent_does_not_submit_when_selection_disabled(self):
        item, _, _ = self.source()
        self.ignore_fixture_human()
        request = dict(self.config['reservation'], item_id=item['id'], expected_version=item['version'],
            capability='prepare_private', bot_id='principal', purpose='Existing preparation', scope='Source')
        receipt = self.control.reserve('gtd-felix', 'previous-reservation', request)
        self.assertEqual(receipt['status'], 'reserved', receipt)
        job_id = receipt['job_id']
        self.configure()
        state = self.worker._state()
        state['runs'][job_id] = dict(phase='intent', event_keys=[e['event_key'] for e in self.source_events(item['id'])],
            prompt='Synthetic existing source intention', durable=False)
        self.worker._save(state)
        for phase in ('intent', 'submitting', 'uncertain'):
            state = self.worker._state()
            state['runs'][job_id]['phase'] = phase
            self.worker._save(state)
            await self.worker.tick()
            self.assertEqual(self.native.submissions, [])
            self.assertEqual(self.native.reconciliations, 0)
            self.assertEqual(self.native.polls, 0)
            self.assertEqual(self.worker._state()['runs'][job_id]['error'], 'source_selection_pending')
            self.assertFalse(self.control.get_job(job_id)['terminal'])

    async def test_known_native_identity_is_polled_without_reconcile_dispatch(self):
        item, _, _ = self.source()
        self.ignore_fixture_human()
        request = dict(self.config['reservation'], item_id=item['id'], expected_version=item['version'],
            capability='prepare_private', bot_id='principal', purpose='Historical source run', scope='Source')
        receipt = self.control.reserve('gtd-felix', 'known-native', request)
        self.assertEqual(receipt['status'], 'reserved', receipt)
        job_id = receipt['job_id']
        self.control.record_dispatch(job_id, self.native.native(job_id))
        self.native.runs[job_id] = {'status': 'running', 'output': 'Historical result'}
        self.configure()
        state = self.worker._state()
        state['runs'][job_id] = dict(phase='uncertain', event_keys=[], prompt='Historical', durable=False)
        self.worker._save(state)
        await self.worker.tick()
        self.assertEqual(self.native.reconciliations, 0)
        self.assertEqual(self.native.polls, 1)
        self.assertEqual(self.native.submissions, [])
        self.assertTrue(self.control.get_job(job_id)['terminal'])
        self.assertEqual(self.service.pending_events('gtd-notification', 'local'), [])

    async def test_continuation_respects_source_selection_result(self):
        from unittest.mock import patch
        orchestration.OrchestrationTests.make_private_action(self)
        await self.worker.tick()
        self.worker.config['reservation'] = dict(self.config['reservation'], max_cost_usd=100)
        await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 1)
        self.assertEqual(self.control.get_job(self.native.submissions[0]['job_id'])['integration'], 'integrated')
        self.configure()
        # SourceSync identity is exercised above; this isolates the continuation
        # admission path after a source has already had historical execution.
        with patch.object(self.worker, '_source_review_blocker', return_value='source_selection_pending'):
            for _ in range(3): await self.worker.tick()
        self.assertEqual(len(self.native.submissions), 1)
        records = list(self.worker._state()['continuations'].values())
        self.assertTrue(records)
        self.assertTrue(all(r['blocker'] == 'source_selection_pending' for r in records))
