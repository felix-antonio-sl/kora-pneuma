"""I3 source authority: per-revision intake/selection rows, coverage, retention."""
import hashlib
import json
import sqlite3
import tempfile
from pathlib import Path
import sys
import unittest

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from gtd_felix.service import GTDService, migrate_i3_sources
from gtd_felix.source_sync import SourceSync
from gtd_felix.google_sources import GoogleSources
from gtd_felix.source_entries import (
    entry_id, get, pending_by_account, coverage, record_decision,
    prune_superseded, run_retention)
import test_google_sources as fixtures


def entry(store, provider, account, collection, external_id, revision):
    return get(store, provider, account, collection, external_id, revision)


class SchemaTests(unittest.TestCase):
    def test_fresh_database_is_v4_with_source_entries(self):
        temp = tempfile.TemporaryDirectory()
        try:
            service = GTDService(Path(temp.name) / 'data')
            try:
                self.assertEqual(
                    service.store.db.execute('PRAGMA user_version').fetchone()[0], 4)
                cols = [r[1] for r in service.store.db.execute(
                    'PRAGMA table_info(source_entries)')]
                self.assertEqual(cols, ['id', 'provider', 'account', 'collection',
                    'external_id', 'revision', 'status', 'original_digest', 'item_id',
                    'metadata_json', 'observed_at'])
            finally:
                service.close()
        finally:
            temp.cleanup()

    def test_newer_schema_is_rejected(self):
        temp = tempfile.TemporaryDirectory()
        try:
            path = Path(temp.name) / 'data'
            service = GTDService(path)
            service.close()
            db = sqlite3.connect(path / 'gtd.sqlite3')
            db.execute('PRAGMA user_version=99')
            db.commit()
            db.close()
            with self.assertRaises(ValueError):
                GTDService(path)
        finally:
            temp.cleanup()

    def test_identity_scopes_collection_unambiguously(self):
        other = entry_id('p', 'a', 'c2', 'e', 'r')
        self.assertNotEqual(entry_id('p', 'a', 'c1', 'e', 'r'), other)
        # No separator-joined ambiguity: fields containing '|' stay distinct.
        self.assertNotEqual(entry_id('p', 'a|b', 'c', 'e', 'r'),
                            entry_id('p', 'a', 'b|c', 'e', 'r'))


class IntakeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.service = GTDService(Path(self.temp.name) / 'data')
        self.sync = SourceSync(self.service)
        self.partition = dict(provider='mail-fixture', account='account-A',
            collection='messages', scope_digest='a' * 64)

    def tearDown(self):
        self.service.close()
        self.temp.cleanup()

    def obj(self, identity='message-1', revision='r1', text='External evidence'):
        data = text.encode()
        return dict(external_id=identity, revision=revision, text=text, original=data,
            sha256=hashlib.sha256(data).hexdigest(),
            url='https://provider.invalid/object/' + identity, status='present')

    def test_entry_exists_before_cursor_advances(self):
        self.sync.begin(self.partition, 'full')
        state = self.sync.apply_page(self.partition, 'full', dict(
            page_id='p1', request_token=None, next_page_token='p2', cursor=None,
            objects=[self.obj()]))
        self.assertIsNone(state['cursor'])
        row = entry(self.service.store, 'mail-fixture', 'account-A', 'messages', 'message-1', 'r1')
        self.assertIsNotNone(row)
        self.assertEqual(row['status'], 'pending')
        self.assertIsNotNone(row['item_id'])
        self.assertEqual(row['original_digest'], hashlib.sha256(b'External evidence').hexdigest())
        final = self.sync.apply_page(self.partition, 'full', dict(
            page_id='p2', request_token='p2', next_page_token=None, cursor='c1', objects=[]))
        self.assertEqual(final['cursor'], 'c1')
        self.assertEqual(
            entry(self.service.store, 'mail-fixture', 'account-A', 'messages', 'message-1', 'r1')['item_id'],
            final['objects']['message-1']['item_id'])

    def test_incremental_second_cycle_accumulates_entries(self):
        self.sync.begin(self.partition, 'full')
        self.sync.apply_page(self.partition, 'full', dict(
            page_id='p1', request_token=None, next_page_token=None, cursor='c1',
            objects=[self.obj('m1')]))
        self.sync.begin(self.partition, 'incremental')
        self.sync.apply_page(self.partition, 'incremental', dict(
            page_id='p2', request_token=None, next_page_token=None, cursor='c2',
            objects=[self.obj('m2')]))
        self.assertEqual(
            coverage(self.service.store, 'mail-fixture', 'account-A'), {'pending': 2})

    def test_pending_and_coverage_reads_are_bounded(self):
        self.sync.begin(self.partition, 'full')
        self.sync.apply_page(self.partition, 'full', dict(
            page_id='p1', request_token=None, next_page_token=None, cursor='c1',
            objects=[self.obj('m1'), self.obj('m2')]))
        pending = pending_by_account(self.service.store, 'mail-fixture', 'account-A')
        self.assertEqual({p['external_id'] for p in pending}, {'m1', 'm2'})
        self.assertEqual(
            pending_by_account(self.service.store, 'mail-fixture', 'account-A',
                               collection='messages'), pending)
        self.assertEqual(pending_by_account(self.service.store, 'mail-fixture', 'other'), [])

    def test_decided_status_is_never_downgraded_by_intake(self):
        record_decision(self.service.store, provider='mail-fixture', account='account-A',
            collection='messages', external_id='message-9', revision='r9',
            decision='noise', reason_code='non_actionable')
        self.sync.begin(self.partition, 'full')
        self.sync.apply_page(self.partition, 'full', dict(
            page_id='p1', request_token=None, next_page_token=None, cursor='c1',
            objects=[self.obj('message-9', 'r9', 'External evidence')]))
        row = entry(self.service.store, 'mail-fixture', 'account-A', 'messages', 'message-9', 'r9')
        self.assertEqual(row['status'], 'noise')

    def test_collections_keep_separate_identities(self):
        for collection in ('calendar-A', 'calendar-B'):
            part = dict(provider='calendar-fixture', account='single-user',
                collection=collection, scope_digest='a' * 64)
            body = collection.encode()
            self.sync.begin(part, collection)
            self.sync.apply_page(part, collection, dict(
                page_id='p1', request_token=None, next_page_token=None, cursor='c1', objects=[
                    dict(external_id='same-event', revision='r1', text=collection,
                         original=body, sha256=hashlib.sha256(body).hexdigest(),
                         url='https://fixture.invalid/event', status='present')]))
        row_a = entry(self.service.store, 'calendar-fixture', 'single-user',
                      'calendar-A', 'same-event', 'r1')
        row_b = entry(self.service.store, 'calendar-fixture', 'single-user',
                      'calendar-B', 'same-event', 'r1')
        self.assertEqual(row_a['original_digest'], hashlib.sha256(b'calendar-A').hexdigest())
        self.assertEqual(row_b['original_digest'], hashlib.sha256(b'calendar-B').hexdigest())
        self.assertNotEqual(row_a['item_id'], row_b['item_id'])
        item_b = self.service.get_item(row_b['item_id'])
        self.assertEqual(item_b['source']['collection'], 'calendar-B')


class MigrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.service = GTDService(Path(self.temp.name) / 'data')
        self.sync = SourceSync(self.service)
        self.partition = dict(provider='mail-fixture', account='account-A',
            collection='messages', scope_digest='a' * 64)

    def tearDown(self):
        self.service.close()
        self.temp.cleanup()

    def _seed_legacy(self):
        self.sync.begin(self.partition, 'full')
        data = b'Legacy body'
        self.sync.apply_page(self.partition, 'full', dict(
            page_id='p1', request_token=None, next_page_token=None, cursor='c1', objects=[
                dict(external_id='legacy-1', revision='r1', text='Legacy one', original=data,
                     sha256=hashlib.sha256(data).hexdigest(),
                     url='https://provider.invalid/object/legacy-1', status='present')]))
        with self.service.store.transaction() as db:
            db.execute("DELETE FROM source_entries")

    def test_migrates_rows_once_with_decisions_and_links(self):
        self._seed_legacy()
        with self.service.store.transaction() as db:
            db.execute("INSERT INTO metadata VALUES(?,?)", (
                'source-sync:google:legacy-adapter', json.dumps({'partition': {
                    'provider': 'mail-fixture', 'account': 'account-A',
                    'collection': 'messages', 'scope_digest': 'a' * 64},
                    'decisions': {'any-key': {
                        'external_id': 'legacy-1', 'revision': 'r1',
                        'classification': 'selected', 'reason_code': 'gtd_relevant'}}})))
        receipt = migrate_i3_sources(self.service.store)
        self.assertEqual(receipt['migrated_source_entries'], 1, receipt)
        row = entry(self.service.store, 'mail-fixture', 'account-A', 'messages', 'legacy-1', 'r1')
        self.assertEqual(row['status'], 'selected')
        self.assertIsNotNone(row['item_id'])
        self.assertEqual(json.loads(row['metadata_json'])['reason_code'], 'gtd_relevant')
        rerun = migrate_i3_sources(self.service.store)
        self.assertEqual(rerun.get('note'), 'already_migrated', rerun)

    def test_migrates_standalone_decisions_without_objects(self):
        with self.service.store.transaction() as db:
            db.execute("INSERT INTO metadata VALUES(?,?)", (
                'source-sync:google:solo-adapter', json.dumps({'partition': {
                    'provider': 'mail-fixture', 'account': 'account-A',
                    'collection': 'messages', 'scope_digest': 'a' * 64},
                    'decisions': {'solo-key': {
                        'external_id': 'solo-1', 'revision': 'r9',
                        'classification': 'noise', 'reason_code': 'non_actionable'}}})))
        receipt = migrate_i3_sources(self.service.store)
        self.assertEqual(receipt['migrated_source_entries'], 1, receipt)
        self.assertEqual(receipt.get('standalone_decisions'), 1, receipt)
        row = entry(self.service.store, 'mail-fixture', 'account-A', 'messages', 'solo-1', 'r9')
        self.assertEqual(row['status'], 'noise')
        self.assertIsNone(row['item_id'])

    def test_migration_never_resurrects_pruned_rows(self):
        self._seed_legacy()
        receipt = migrate_i3_sources(self.service.store)
        self.assertEqual(receipt['migrated_source_entries'], 1, receipt)
        removed = prune_superseded(self.service.store, provider='mail-fixture',
            account='account-A', collection='messages', external_id='legacy-1',
            keep_revisions={'r1-keep'})
        # r1 is the only revision: keeping another name prunes it; rerun must
        # not resurrect from legacy, only report the archive.
        self.assertEqual(removed, 1)
        second = migrate_i3_sources(self.service.store)
        self.assertEqual(second.get('note'), 'already_migrated', second)
        self.assertIsNone(entry(
            self.service.store, 'mail-fixture', 'account-A', 'messages', 'legacy-1', 'r1'))

    def test_cross_scope_merge_prefers_selection(self):
        self._seed_legacy()
        with self.service.store.transaction() as db:
            db.execute("INSERT INTO metadata VALUES(?,?)", (
                'source-sync:google:legacy-adapter', json.dumps({'partition': {
                    'provider': 'mail-fixture', 'account': 'account-A',
                    'collection': 'messages', 'scope_digest': 'a' * 64},
                    'decisions': {'k1': {
                        'external_id': 'legacy-1', 'revision': 'r1',
                        'classification': 'noise', 'reason_code': 'non_actionable'}}})))
            db.execute("INSERT INTO metadata VALUES(?,?)", (
                'source-sync:google:other-scope', json.dumps({'partition': {
                    'provider': 'mail-fixture', 'account': 'account-A',
                    'collection': 'messages', 'scope_digest': 'b' * 64},
                    'decisions': {'k2': {
                        'external_id': 'legacy-1', 'revision': 'r1',
                        'classification': 'selected', 'reason_code': 'gtd_relevant'}}})))
        receipt = migrate_i3_sources(self.service.store)
        self.assertEqual(receipt['migrated_source_entries'], 1, receipt)
        row = entry(self.service.store, 'mail-fixture', 'account-A', 'messages', 'legacy-1', 'r1')
        self.assertEqual(row['status'], 'selected')
        self.assertEqual(json.loads(row['metadata_json'])['reason_code'], 'gtd_relevant')

    def test_post_cut_rerun_changes_nothing_new_decisions_use_live_path(self):
        # After the cut, migration is a pure no-op: a decision landing in
        # legacy adapter state is NOT picked up; the live record_decision
        # path owns new decisions.
        self._seed_legacy()
        first = migrate_i3_sources(self.service.store)
        self.assertNotIn('note', first, first)
        with self.service.store.transaction() as db:
            db.execute("INSERT INTO metadata VALUES(?,?)", (
                'source-sync:google:late-adapter', json.dumps({'partition': {
                    'provider': 'mail-fixture', 'account': 'account-A',
                    'collection': 'messages', 'scope_digest': 'c' * 64},
                    'decisions': {'k3': {
                        'external_id': 'legacy-1', 'revision': 'r1',
                        'classification': 'selected', 'reason_code': 'gtd_relevant'}}})))
        second = migrate_i3_sources(self.service.store)
        self.assertEqual(second.get('note'), 'already_migrated', second)
        row = entry(self.service.store, 'mail-fixture', 'account-A', 'messages', 'legacy-1', 'r1')
        self.assertEqual(row['status'], 'pending')
        record_decision(self.service.store, provider='mail-fixture', account='account-A',
            collection='messages', external_id='legacy-1', revision='r1',
            decision='selected', reason_code='gtd_relevant')
        row = entry(self.service.store, 'mail-fixture', 'account-A', 'messages', 'legacy-1', 'r1')
        self.assertEqual(row['status'], 'selected')

    def test_empty_cut_still_writes_durable_receipt(self):
        receipt = migrate_i3_sources(self.service.store)
        self.assertNotIn('note', receipt, receipt)
        self.assertEqual(receipt['migrated_source_entries'], 0, receipt)
        stored = self.service._meta('migration:i3')
        self.assertEqual(stored['migrated_source_entries'], 0, stored)
        second = migrate_i3_sources(self.service.store)
        self.assertEqual(second.get('note'), 'already_migrated', second)
        self.assertEqual(self.service._meta('migration:i3'), stored)

    def test_preincorporated_rows_still_close_the_cut(self):
        import json as _json
        self._seed_legacy()
        with self.service.store.transaction() as db:
            db.execute("INSERT INTO metadata VALUES(?,?)", (
                'source-sync:google:legacy-adapter', _json.dumps({'partition': {
                    'provider': 'mail-fixture', 'account': 'account-A',
                    'collection': 'messages', 'scope_digest': 'a' * 64},
                    'decisions': {'k1': {
                        'external_id': 'legacy-1', 'revision': 'r1',
                        'classification': 'selected', 'reason_code': 'gtd_relevant'}}})))
        # The identical verdict already lives in the table via the live path.
        record_decision(self.service.store, provider='mail-fixture', account='account-A',
            collection='messages', external_id='legacy-1', revision='r1',
            decision='selected', reason_code='gtd_relevant')
        before = entry(self.service.store, 'mail-fixture', 'account-A',
            'messages', 'legacy-1', 'r1')
        receipt = migrate_i3_sources(self.service.store)
        self.assertNotIn('note', receipt, receipt)
        self.assertEqual(receipt['migrated_source_entries'], 0, receipt)
        self.assertGreaterEqual(receipt['skipped_existing'], 1, receipt)
        stored = self.service._meta('migration:i3')
        self.assertEqual(stored['migrated_source_entries'], 0, stored)
        after = entry(self.service.store, 'mail-fixture', 'account-A',
            'messages', 'legacy-1', 'r1')
        self.assertEqual(after['status'], before['status'])
        self.assertEqual(after['metadata_json'], before['metadata_json'])
        second = migrate_i3_sources(self.service.store)
        self.assertEqual(second.get('note'), 'already_migrated', second)
        self.assertEqual(self.service._meta('migration:i3'), stored)

    def test_refuses_with_active_sync_cycle(self):
        self.sync.begin(self.partition, 'active-cycle')
        with self.assertRaises(ValueError):
            migrate_i3_sources(self.service.store)


class SelectiveJourneyTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.path = Path(self.temp.name) / 'data'
        self.service = GTDService(self.path)
        self.transport = fixtures.Transport(self.service)
        self.config = {'mail': {'provider': 'gmail', 'account': fixtures.ACCOUNT,
            'scope': 'selective_since', 'since_epoch': 1785556800, 'page_size': 2}}
        self.answers = {}
        self.adapter = GoogleSources(SourceSync(self.service), self.transport,
            self.config, evaluator=self.evaluate)

    async def asyncTearDown(self):
        self.service.close()
        self.temp.cleanup()

    async def evaluate(self, evidence):
        classification = self.answers.get(evidence['external_id'], 'noise')
        return {'classification': classification, 'reason_code': {
            'noise': 'non_actionable', 'selected': 'gtd_relevant',
            'uncertain': 'needs_review'}[classification]}

    def profile(self, history='10'):
        self.transport.add(fixtures.GMAIL + '/profile', {},
            {'emailAddress': fixtures.ACCOUNT, 'historyId': history})

    def page(self, messages, *, token=None, next_token=None):
        query = {'maxResults': 2, 'includeSpamTrash': 'true', 'q': 'after:1785556800'}
        if token:
            query['pageToken'] = token
        body = {'messages': [{'id': identity} for identity in messages]}
        if next_token:
            body['nextPageToken'] = next_token
        self.transport.add(fixtures.GMAIL + '/messages', query, body)
        for identity in messages:
            self.transport.add(fixtures.GMAIL + '/messages/' + identity, {'format': 'raw'},
                fixtures.raw_message(identity, labels=['CATEGORY_PROMOTIONS']))

    def history(self, start, identities=(), *, end='20', status=200):
        self.transport.add(fixtures.GMAIL + '/history', {'maxResults': 2, 'startHistoryId': start},
            {'historyId': end, 'history': [{'id': end, 'messagesAdded': [{'message': {'id': i}} for i in identities]}]}, status=status)
        for identity in identities:
            self.transport.add(fixtures.GMAIL + '/messages/' + identity, {'format': 'raw'},
                fixtures.raw_message(identity, history=end))

    def entries(self, external_id):
        return [dict(r) for r in self.service.store.db.execute(
            "SELECT * FROM source_entries WHERE provider='gmail' AND external_id=? ORDER BY observed_at",
            (external_id,)).fetchall()]

    async def test_selected_projects_affair_and_revision_invalidates_only_dependents(self):
        self.answers['m1'] = 'selected'
        self.profile()
        self.page(['m1'])
        result = await self.adapter.synchronize('mail')
        self.assertEqual('complete', result['health'])
        rows = self.entries('m1')
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['status'], 'selected')
        self.assertIsNotNone(rows[0]['original_digest'])
        self.assertIsNotNone(rows[0]['item_id'])
        affair = next(i for i in self.service.query()
                      if i.get('source', {}).get('external_id') == 'm1')
        self.assertEqual(rows[0]['item_id'], affair['id'])
        self.assertIsNone(affair.get('waiting_for'))
        self.assertEqual(len(self.service.query()), 1)
        current = self.service.get_item(affair['id'])
        affair = self.service.execute('felix', {'operation_id': 'i3-clarify', 'action': 'clarify',
            'item_id': affair['id'], 'expected_version': current['version'],
            'fields': {'kind': 'action', 'commitment': 'committed', 'outcome': 'Atender',
                       'completion_criteria': 'Hecho'}})['item']
        other = self.service.capture('felix', 'i3-other', 'Asunto ajeno')['item']
        other = self.service.execute('felix', {'operation_id': 'i3-other-mat', 'action': 'put_material',
            'item_id': other['id'], 'expected_version': other['version'],
            'fields': {'content': 'Material ajeno intacto', 'title': 'Ajeno'}})['item']
        affair = self.service.execute('felix', {'operation_id': 'i3-mat-v1', 'action': 'put_material',
            'item_id': affair['id'], 'expected_version': affair['version'],
            'fields': {'content': 'Preparacion v1', 'title': 'Prep',
                       'source_versions': {affair['id']: len(affair['source_revisions'])}}})['item']
        self.assertTrue(self.service.materials(affair['id'])[0]['valid'])
        self.profile('20')
        self.history('10', ['m1'], end='20')
        result = await self.adapter.synchronize('mail')
        self.assertEqual('complete', result['health'])
        rows = self.entries('m1')
        self.assertEqual(len(rows), 2)
        self.assertEqual({r['status'] for r in rows}, {'selected'})
        self.assertTrue(all(r['original_digest'] is not None for r in rows))
        revised = self.service.get_item(affair['id'])
        self.assertGreater(revised['version'], affair['version'])
        invalid = self.service.materials(affair['id'])[0]
        self.assertFalse(invalid['valid'])
        self.assertTrue(any(r.startswith('basis_changed') for r in invalid['invalid_reasons']))
        intact = self.service.materials(other['id'])[0]
        self.assertTrue(intact['valid'])
        content = self.service.read_material(other['id'], intact['id'], intact['version'])['content']
        self.assertIn('Material ajeno intacto', content)

    async def test_table_rules_over_legacy_dict_without_reevaluation(self):
        from gtd_felix.source_entries import record_decision
        self.answers['m1'] = 'selected'
        self.profile()
        self.page(['m1'])
        await self.adapter.synchronize('mail')
        calls = []
        async def counting(evidence):
            calls.append(evidence['external_id'])
            return {'classification': 'selected', 'reason_code': 'gtd_relevant'}
        # A newer decision lands directly; the selective read must honor the
        # table without spending another inference.
        rows = self.entries('m1')
        record_decision(self.service.store, provider='gmail', account='reader@example.invalid',
            collection=rows[0]['collection'], external_id='m1', revision=rows[0]['revision'],
            decision='noise', reason_code='non_actionable')
        partition = self.adapter.inspect('mail')['partition']
        adapter = self.service._meta('source-sync:google:' + __import__(
            'hashlib').sha256(__import__('json').dumps(
                partition, ensure_ascii=False, sort_keys=True,
                separators=(',', ':')).encode()).hexdigest())
        self.adapter.evaluator = counting
        self.transport.add(fixtures.GMAIL + '/messages/m1', {'format': 'raw'},
            fixtures.raw_message('m1', labels=['CATEGORY_PROMOTIONS']))
        affairs_before = len(self.service.query())
        obj = await self.adapter._read_selective_message(
            self.config['mail'], 'm1', adapter)
        self.assertEqual(calls, [])
        self.assertTrue(obj is None or obj.get('status') == 'degraded', obj)
        self.assertEqual(len(self.service.query()), affairs_before)
        rows = self.entries('m1')
        decided = [r for r in rows if r['revision'].startswith('message:')]
        self.assertTrue(decided)
        self.assertTrue(all(r['status'] == 'noise' for r in decided))

    async def test_migration_rerun_preserves_newer_decisions(self):
        from gtd_felix.source_entries import record_decision
        self.answers['m1'] = 'selected'
        self.profile()
        self.page(['m1'])
        await self.adapter.synchronize('mail')
        rows = self.entries('m1')
        # Simulate the pre-cut legacy shape: index history present, no rows.
        with self.service.store.transaction() as db:
            db.execute("DELETE FROM source_entries")
        first = migrate_i3_sources(self.service.store)
        self.assertNotIn('note', first, first)
        record_decision(self.service.store, provider='gmail', account='reader@example.invalid',
            collection=rows[0]['collection'], external_id='m1', revision=rows[0]['revision'],
            decision='noise', reason_code='non_actionable')
        before = self.service._meta('migration:i3')
        second = migrate_i3_sources(self.service.store)
        self.assertEqual(second.get('note'), 'already_migrated', second)
        self.assertEqual(self.service._meta('migration:i3'), before)
        rows = self.entries('m1')
        decided = [r for r in rows if r['revision'].startswith('message:')]
        self.assertTrue(decided)
        self.assertTrue(all(r['status'] == 'noise' for r in decided))

    async def test_prune_keeps_current_verdict_without_reevaluation(self):
        self.answers['m1'] = 'selected'
        self.profile()
        self.page(['m1'])
        await self.adapter.synchronize('mail')
        self.answers['m1'] = 'noise'
        self.profile('20')
        self.history('10', ['m1'], end='20')
        await self.adapter.synchronize('mail')
        rows = self.entries('m1')
        self.assertEqual(len(rows), 3, [r['status'] for r in rows])
        receipt = self.service.prune_sources('felix')
        self.assertEqual(receipt['pruned_rows'], 1, receipt)
        rows = self.entries('m1')
        self.assertEqual({r['status'] for r in rows}, {'selected', 'noise'})
        # Restart: the verdict must survive prune plus reopen, then rereading
        # the new revision honors the recorded noise verdict without inference.
        self.service.close()
        self.service = GTDService(Path(self.temp.name) / 'data')
        calls = []
        async def counting(evidence):
            calls.append(evidence['external_id'])
            return {'classification': 'selected', 'reason_code': 'gtd_relevant'}
        self.transport.service = self.service
        adapter = GoogleSources(SourceSync(self.service), self.transport,
            self.config, evaluator=counting)
        partition = adapter.inspect('mail')['partition']
        persisted = self.service._meta('source-sync:google:' + __import__(
            'hashlib').sha256(__import__('json').dumps(
                partition, ensure_ascii=False, sort_keys=True,
                separators=(',', ':')).encode()).hexdigest())
        self.transport.add(fixtures.GMAIL + '/messages/m1', {'format': 'raw'},
            fixtures.raw_message('m1', history='20'))
        obj = await adapter._read_selective_message(
            self.config['mail'], 'm1', persisted)
        self.assertEqual(calls, [])
        self.assertTrue(obj is None or obj.get('status') == 'degraded', obj)
        rows = self.entries('m1')
        self.assertEqual({r['status'] for r in rows}, {'selected', 'noise'})

    async def test_uncertain_row_survives_prune_and_reevaluates_by_design(self):
        # Uncertain is deliberately non-terminal: the read path re-evaluates
        # it on contact (see _read_selective_message). Retention's duty is to
        # keep the row so the verdict history is never lost to maintenance.
        self.answers['m1'] = 'selected'
        self.profile()
        self.page(['m1'])
        await self.adapter.synchronize('mail')
        self.answers['m1'] = 'uncertain'
        self.profile('20')
        self.history('10', ['m1'], end='20')
        await self.adapter.synchronize('mail')
        rows = self.entries('m1')
        self.assertEqual(len(rows), 3, [r['status'] for r in rows])
        receipt = self.service.prune_sources('felix')
        self.assertEqual(receipt['pruned_rows'], 1, receipt)
        rows = self.entries('m1')
        self.assertEqual({r['status'] for r in rows}, {'selected', 'uncertain'})
        # Restart, then reread: uncertain re-evaluates by design and the fresh
        # verdict lands without losing the retained history.
        self.service.close()
        self.service = GTDService(Path(self.temp.name) / 'data')
        calls = []
        async def counting(evidence):
            calls.append(evidence['external_id'])
            return {'classification': 'selected', 'reason_code': 'gtd_relevant'}
        self.transport.service = self.service
        adapter = GoogleSources(SourceSync(self.service), self.transport,
            self.config, evaluator=counting)
        partition = adapter.inspect('mail')['partition']
        persisted = self.service._meta('source-sync:google:' + __import__(
            'hashlib').sha256(__import__('json').dumps(
                partition, ensure_ascii=False, sort_keys=True,
                separators=(',', ':')).encode()).hexdigest())
        self.transport.add(fixtures.GMAIL + '/messages/m1', {'format': 'raw'},
            fixtures.raw_message('m1', history='20'))
        await adapter._read_selective_message(
            self.config['mail'], 'm1', persisted)
        self.assertEqual(calls, ['m1'])
        rows = self.entries('m1')
        self.assertTrue(any(r['status'] == 'selected' for r in rows), rows)

    async def test_post_cut_legacy_is_never_adopted(self):
        self.answers['m1'] = 'selected'
        self.profile()
        self.page(['m1'])
        await self.adapter.synchronize('mail')
        rows = self.entries('m1')
        with self.service.store.transaction() as db:
            db.execute("DELETE FROM source_entries")
        migrate_i3_sources(self.service.store)
        # Contradictory legacy for a revision with no row: post-cut reads
        # must not resurrect it; a legitimate reread evaluates anew.
        partition = self.adapter.inspect('mail')['partition']
        adapter = dict(self.service._meta('source-sync:google:' + __import__(
            'hashlib').sha256(__import__('json').dumps(
                partition, ensure_ascii=False, sort_keys=True,
                separators=(',', ':')).encode()).hexdigest()))
        adapter.setdefault('decisions', {})['forged'] = {
            'external_id': 'm1', 'revision': rows[0]['revision'],
            'classification': 'noise', 'reason_code': 'non_actionable'}
        with self.service.store.transaction() as db:
            db.execute("INSERT OR REPLACE INTO metadata VALUES(?,?)", (
                'source-sync:google:' + __import__('hashlib').sha256(__import__('json').dumps(
                    partition, ensure_ascii=False, sort_keys=True,
                    separators=(',', ':')).encode()).hexdigest(),
                json.dumps(adapter)))
        calls = []
        async def counting(evidence):
            calls.append(evidence['external_id'])
            return {'classification': 'selected', 'reason_code': 'gtd_relevant'}
        self.adapter.evaluator = counting
        self.transport.add(fixtures.GMAIL + '/messages/m1', {'format': 'raw'},
            fixtures.raw_message('m1', labels=['CATEGORY_PROMOTIONS']))
        await self.adapter._read_selective_message(self.config['mail'], 'm1', adapter)
        self.assertEqual(calls, ['m1'])
        rows = self.entries('m1')
        decided = [r for r in rows if r['revision'].startswith('message:')]
        self.assertTrue(all(r['status'] == 'selected' for r in decided), rows)

    async def test_noise_keeps_obligation_without_body(self):
        self.answers['m1'] = 'noise'
        self.profile()
        self.page(['m1'])
        await self.adapter.synchronize('mail')
        rows = self.entries('m1')
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['status'], 'noise')
        self.assertIsNone(rows[0]['item_id'])
        self.assertEqual(self.service.query(), [])
        blob = json.dumps([dict(r) for r in self.service.store.db.execute(
            "SELECT key, value FROM metadata")])
        self.assertNotIn('Read this source', blob)

    async def test_failed_evaluation_keeps_retry_obligation_without_body(self):
        async def failing(evidence):
            raise RuntimeError('synthetic bridge down')
        self.adapter = GoogleSources(SourceSync(self.service), self.transport,
            self.config, evaluator=failing)
        self.profile()
        self.page(['m1'])
        result = await self.adapter.synchronize('mail')
        self.assertEqual('degraded', result['health'])
        pending = result['adapter']['pending_reads']
        self.assertIn('m1', pending)
        blob = json.dumps([dict(r) for r in self.service.store.db.execute(
            "SELECT key, value FROM metadata")])
        self.assertNotIn('Read this source', blob)
        self.assertNotIn('synthetic bridge down', blob)


class RetentionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.service = GTDService(Path(self.temp.name) / 'data')

    def tearDown(self):
        self.service.close()
        self.temp.cleanup()

    def test_prune_keeps_only_referenced_revisions(self):
        from gtd_felix.source_entries import run_retention
        record_decision(self.service.store, provider='gmail', account='a',
            collection='inbox', external_id='m1', revision='r1', decision='selected')
        record_decision(self.service.store, provider='gmail', account='a',
            collection='inbox', external_id='m1', revision='r2', decision='selected')
        receipt = run_retention(self.service.store)
        self.assertEqual(receipt['pruned_rows'], 1, receipt)
        self.assertEqual(receipt['multi_revision_objects'], 1, receipt)
        remaining = [r[0] for r in self.service.store.db.execute(
            "SELECT revision FROM source_entries WHERE external_id='m1'")]
        self.assertEqual(remaining, ['r2'])
        again = run_retention(self.service.store)
        self.assertEqual(again['pruned_rows'], 0, again)

    def test_prune_requires_kept_revision(self):
        with self.assertRaises(ValueError):
            prune_superseded(self.service.store, provider='gmail', account='a',
                collection='inbox', external_id='m1', keep_revisions=set())

    def test_prune_sources_owner_only_converges_and_persists(self):
        record_decision(self.service.store, provider='gmail', account='a',
            collection='inbox', external_id='m8', revision='r1', decision='noise')
        record_decision(self.service.store, provider='gmail', account='a',
            collection='inbox', external_id='m8', revision='r2', decision='noise')
        with self.assertRaises(ValueError):
            self.service.prune_sources('gtd-felix')
        receipt = self.service.prune_sources('felix')
        self.assertEqual(receipt['pruned_rows'], 1, receipt)
        again = self.service.prune_sources('felix')
        self.assertEqual(again['pruned_rows'], 0, again)
        stored = json.loads(self.service.store.db.execute(
            "SELECT value FROM metadata WHERE key='source-entries:retention'").fetchone()[0])
        self.assertEqual(stored['pruned_rows'], 0, stored)
        self.service.close()
        self.service = GTDService(Path(self.temp.name) / 'data')
        kept = [r[0] for r in self.service.store.db.execute(
            "SELECT revision FROM source_entries WHERE external_id='m8'")]
        self.assertEqual(kept, ['r2'])

    def test_retention_survives_restart_with_receipt(self):
        from gtd_felix.source_entries import run_retention
        record_decision(self.service.store, provider='gmail', account='a',
            collection='inbox', external_id='m9', revision='r1', decision='noise')
        record_decision(self.service.store, provider='gmail', account='a',
            collection='inbox', external_id='m9', revision='r2', decision='noise')
        self.service.close()
        self.service = GTDService(Path(self.temp.name) / 'data')
        receipt = run_retention(self.service.store)
        self.assertEqual(receipt['pruned_rows'], 1, receipt)
        stored = json.loads(self.service.store.db.execute(
            "SELECT value FROM metadata WHERE key='source-entries:retention'").fetchone()[0])
        self.assertEqual(stored['pruned_rows'], 1, stored)


if __name__ == '__main__':
    unittest.main()
