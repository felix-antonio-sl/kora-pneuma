"""Selective Gmail durable obligations with injected ephemeral classification."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from gtd_felix.service import GTDService
from gtd_felix.source_sync import SourceSync
from gtd_felix.google_sources import GoogleSources
import test_google_sources as fixtures


class SelectiveGmailTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.path = Path(self.temp.name) / 'data'
        self.service = GTDService(self.path)
        self.transport = fixtures.Transport(self.service)
        self.config = {'mail': {'provider': 'gmail', 'account': fixtures.ACCOUNT, 'scope': 'selective_since',
            'since_epoch': 1785556800, 'page_size': 2}}
        self.answers = {}
        self.evaluated = []
        self.adapter = GoogleSources(SourceSync(self.service), self.transport, self.config, evaluator=self.evaluate)

    async def asyncTearDown(self):
        self.service.close()
        self.temp.cleanup()

    async def evaluate(self, evidence):
        self.assertFalse(self.service.store.db.in_transaction)
        state = self.adapter.inspect('mail')['adapter']
        self.assertEqual(evidence['revision'], state['pending_reads'][evidence['external_id']]['revision'])
        self.evaluated.append(evidence['external_id'])
        classification = self.answers.get(evidence['external_id'], 'noise')
        return {'classification': classification, 'reason_code': {
            'noise': 'non_actionable', 'selected': 'gtd_relevant', 'uncertain': 'needs_review'}[classification]}

    def profile(self, history='10'):
        self.transport.add(fixtures.GMAIL + '/profile', {}, {'emailAddress': fixtures.ACCOUNT, 'historyId': history})

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
            self.transport.add(fixtures.GMAIL + '/messages/' + identity, {'format': 'raw'}, fixtures.raw_message(identity, history=end))

    def restart(self):
        self.service.close()
        self.service = GTDService(self.path)
        self.transport.service = self.service
        self.adapter = GoogleSources(SourceSync(self.service), self.transport, self.config, evaluator=self.evaluate)

    async def test_noise_never_persists_body_and_newsletter_relevance_is_evaluated(self):
        self.answers['newsletter'] = 'selected'
        self.profile()
        self.page(['noise', 'newsletter'])
        result = await self.adapter.synchronize('mail')
        self.assertEqual('complete', result['health'])
        self.assertEqual({'noise', 'newsletter'}, set(self.evaluated))
        self.assertEqual(1, len(self.service.query()))
        self.assertEqual('newsletter', self.service.query()[0]['source']['external_id'])
        adapter = json.dumps(result['adapter'])
        self.assertNotIn('External assignment', adapter)
        self.assertNotIn('Read this source', adapter)
        self.assertNotIn('raw', adapter)
        self.assertEqual(1, self.service.store.db.execute('SELECT count(*) FROM originals').fetchone()[0])
        self.assertEqual('10', result['sync']['cursor'])

    async def test_uncertain_obligation_survives_advanced_cursor_and_restart(self):
        self.answers['m1'] = 'uncertain'
        self.profile(); self.page(['m1'])
        result = await self.adapter.synchronize('mail')
        self.assertEqual('10', result['sync']['cursor'])
        self.assertEqual('degraded', result['health'])
        self.assertEqual([], self.service.query())
        self.assertEqual(0, self.service.store.db.execute('SELECT count(*) FROM originals').fetchone()[0])
        self.restart()
        self.answers['m1'] = 'selected'
        self.profile('20')
        self.transport.add(fixtures.GMAIL + '/messages/m1', {'format': 'raw'}, fixtures.raw_message())
        self.history('10', end='20')
        result = await self.adapter.synchronize('mail')
        self.assertEqual('complete', result['health'])
        self.assertEqual(1, len(self.service.query()))
        self.assertEqual({}, result['pending_reads'])

    async def test_page_restart_and_noise_revision_idempotence(self):
        self.config['mail']['max_pages'] = 1
        self.adapter = GoogleSources(SourceSync(self.service), self.transport, self.config, evaluator=self.evaluate)
        self.profile(); self.page(['m1'], next_token='p2')
        first = await self.adapter.synchronize('mail')
        self.assertIsNone(first['sync']['cursor'])
        self.restart()
        self.page(['m1', 'm2'], token='p2')
        result = await self.adapter.synchronize('mail')
        self.assertEqual('10', result['sync']['cursor'])
        self.assertEqual(['m1', 'm2'], self.evaluated)
        self.assertEqual([], self.service.query())
        self.assertEqual(0, self.service.store.db.execute('SELECT count(*) FROM originals').fetchone()[0])

    async def test_expired_history_rebuilds_only_scoped_query_with_honest_gap(self):
        self.profile(); self.page(['m1'])
        await self.adapter.synchronize('mail')
        self.profile('20'); self.history('10', status=404)
        failed = await self.adapter.synchronize('mail')
        self.assertEqual('rebuild_required', failed['sync']['coverage'])
        self.restart()
        self.profile('30'); self.page(['m1'])
        rebuilt = await self.adapter.synchronize('mail')
        self.assertEqual('30', rebuilt['sync']['cursor'])
        self.assertEqual('lost_rebuilt_scope', rebuilt['coverage_contract']['history_continuity'])
        self.assertEqual('selective_since_including_spam_trash', rebuilt['coverage_contract']['scope'])

    async def test_selected_to_noise_keeps_only_historical_original_and_marks_new_revision(self):
        self.answers['m1'] = 'selected'
        self.profile(); self.page(['m1'])
        await self.adapter.synchronize('mail')
        old = self.service.query()[0]
        self.answers['m1'] = 'noise'
        self.profile('20'); self.history('10', ['m1'], end='20')
        result = await self.adapter.synchronize('mail')
        current = self.service.query()[0]
        self.assertEqual(old['id'], current['id'])
        self.assertEqual(old['original'], current['original'])
        self.assertIsNone(current['source']['sha256'])
        self.assertEqual('degraded', current['source']['availability'])
        self.assertEqual(old['original'], current['source_revisions'][0]['original'])
        self.assertEqual(1, self.service.store.db.execute('SELECT count(*) FROM originals').fetchone()[0])
        key = result['adapter']['current_decisions']['m1']
        self.assertEqual('noise', result['adapter']['decisions'][key]['classification'])

    async def test_unconfigured_evaluator_fails_closed_before_network(self):
        self.adapter = GoogleSources(SourceSync(self.service), self.transport, self.config)
        result = await self.adapter.synchronize('mail')
        self.assertEqual('degraded', result['health'])
        self.assertEqual('evaluator_unavailable', result['adapter']['error'])
        self.assertEqual('not_evaluated', result['coverage_contract']['semantic_review'])
        self.assertEqual([], self.transport.calls)
        self.assertEqual([], self.service.query())

    async def test_history_before_scope_is_not_evaluated_or_projected(self):
        self.profile(); self.page([])
        await self.adapter.synchronize('mail')
        self.profile('20')
        self.transport.add(fixtures.GMAIL + '/history', {'maxResults': 2, 'startHistoryId': '10'},
            {'historyId': '20', 'history': [{'id': '20', 'messagesAdded': [{'message': {'id': 'old'}}]}]})
        old = fixtures.raw_message('old', history='20')
        old['internalDate'] = str((1785556800 - 1) * 1000)
        self.transport.add(fixtures.GMAIL + '/messages/old', {'format': 'raw'}, old)
        result = await self.adapter.synchronize('mail')
        self.assertEqual([], self.evaluated)
        self.assertEqual([], self.service.query())
        decision = result['adapter']['decisions'][result['adapter']['current_decisions']['old']]
        self.assertEqual('outside_scope', decision['reason_code'])

    async def test_evaluator_failure_retains_obligation_without_message_or_error_text(self):
        marker = 'SYNTHETIC_PRIVATE_NEWSLETTER_BODY_728319'
        async def failing(evidence):
            self.assertIn(marker, evidence['text'])
            raise RuntimeError(marker)
        self.adapter.evaluator = failing
        self.profile()
        self.transport.add(fixtures.GMAIL + '/messages',
            {'maxResults': 2, 'includeSpamTrash': 'true', 'q': 'after:1785556800'}, {'messages': [{'id': 'noise'}]})
        raw = fixtures.raw_message('noise')
        import base64
        rfc = base64.urlsafe_b64decode(raw['raw'] + '=' * (-len(raw['raw']) % 4))
        raw['raw'] = base64.urlsafe_b64encode(rfc + marker.encode()).decode()
        self.transport.add(fixtures.GMAIL + '/messages/noise', {'format': 'raw'}, raw)
        result = await self.adapter.synchronize('mail')
        self.assertEqual('degraded', result['health'])
        self.assertEqual('10', result['sync']['cursor'])
        self.assertIn('noise', result['pending_reads'])
        self.assertNotIn(marker, json.dumps(result))
        self.assertEqual(0, self.service.store.db.execute('SELECT count(*) FROM originals').fetchone()[0])
        self.assertNotIn(marker, '\n'.join(self.service.store.db.iterdump()))

    async def test_noise_exact_body_never_reaches_database(self):
        marker = 'SYNTHETIC_NOISE_728391_NORETENTION'
        self.profile()
        self.transport.add(fixtures.GMAIL + '/messages',
            {'maxResults': 2, 'includeSpamTrash': 'true', 'q': 'after:1785556800'}, {'messages': [{'id': 'noise'}]})
        import base64
        raw = fixtures.raw_message('noise')
        rfc = base64.urlsafe_b64decode(raw['raw'] + '=' * (-len(raw['raw']) % 4)) + marker.encode()
        raw['raw'] = base64.urlsafe_b64encode(rfc).decode()
        self.transport.add(fixtures.GMAIL + '/messages/noise', {'format': 'raw'}, raw)
        await self.adapter.synchronize('mail')
        dump = '\n'.join(self.service.store.db.iterdump())
        self.assertNotIn(marker, dump)
        self.assertNotIn(raw['raw'], dump)
        self.assertEqual(0, self.service.store.db.execute('SELECT count(*) FROM originals').fetchone()[0])
        self.assertEqual([], self.service.query())

    async def test_newsletter_body_is_evaluated_without_label_shortcut(self):
        import base64
        body = 'Within a newsletter: prepare the HODOM staffing summary for Monday.'
        async def evaluate_body(evidence):
            self.assertIn(body, evidence['text'])
            self.assertIn('CATEGORY_PROMOTIONS', evidence['text'])
            return {'classification': 'selected', 'reason_code': 'gtd_relevant'}
        self.adapter.evaluator = evaluate_body
        self.profile(); self.page(['newsletter'])
        raw = self.transport.steps[-1][2]
        rfc = base64.urlsafe_b64decode(raw['raw'] + '=' * (-len(raw['raw']) % 4))
        raw['raw'] = base64.urlsafe_b64encode(rfc + body.encode()).decode()
        await self.adapter.synchronize('mail')
        self.assertIn(body, self.service.query()[0]['text'])

    async def test_transport_allows_only_exact_authorized_epoch_query(self):
        from gtd_felix.google_transport import GoogleTransport, TransportError
        transport = GoogleTransport.__new__(GoogleTransport)
        transport.gmail, transport.calendars = True, []
        self.assertEqual('gmail_read', transport._route('GET', fixtures.GMAIL + '/messages',
            {'q': 'after:1785556800', 'includeSpamTrash': 'true', 'maxResults': 2}))
        for query in ('after:0', 'in:anywhere', 'after:1785556800 label:inbox'):
            with self.assertRaises(TransportError):
                transport._route('GET', fixtures.GMAIL + '/messages', {'q': query})

    async def test_later_noise_observation_suppresses_selected_retry(self):
        self.answers['m1'] = 'uncertain'
        self.profile(); self.page(['m1'])
        await self.adapter.synchronize('mail')
        self.restart()
        async def by_revision(evidence):
            return {'classification': 'selected', 'reason_code': 'gtd_relevant'} if evidence['revision'].startswith('message:10:') else {
                'classification': 'noise', 'reason_code': 'non_actionable'}
        self.adapter.evaluator = by_revision
        self.profile('20')
        self.transport.add(fixtures.GMAIL + '/messages/m1', {'format': 'raw'}, fixtures.raw_message('m1', history='10'))
        self.history('10', ['m1'], end='20')
        result = await self.adapter.synchronize('mail')
        self.assertEqual('complete', result['health'])
        self.assertEqual('noise', result['adapter']['decisions'][result['adapter']['current_decisions']['m1']]['classification'])
        self.assertEqual([], self.service.query())
        self.assertEqual(0, self.service.store.db.execute('SELECT count(*) FROM originals').fetchone()[0])
        self.assertEqual({}, result['pending_reads'])

    async def test_later_uncertain_observation_suppresses_selected_retry_and_stays_pending(self):
        self.answers['m1'] = 'uncertain'
        self.profile(); self.page(['m1'])
        await self.adapter.synchronize('mail')
        self.restart()
        async def by_revision(evidence):
            return {'classification': 'selected', 'reason_code': 'gtd_relevant'} if evidence['revision'].startswith('message:10:') else {
                'classification': 'uncertain', 'reason_code': 'needs_review'}
        self.adapter.evaluator = by_revision
        self.profile('20')
        self.transport.add(fixtures.GMAIL + '/messages/m1', {'format': 'raw'}, fixtures.raw_message('m1', history='10'))
        self.history('10', ['m1'], end='20')
        result = await self.adapter.synchronize('mail')
        self.assertEqual('degraded', result['health'])
        self.assertEqual('pending', result['coverage_contract']['semantic_review'])
        self.assertEqual([], self.service.query())
        self.assertTrue(result['pending_reads']['m1']['revision'].startswith('message:20:'))
        self.assertNotIn('resolving_revision', result['pending_reads']['m1'])
        self.assertEqual(0, self.service.store.db.execute('SELECT count(*) FROM originals').fetchone()[0])

    async def test_selected_source_is_invalidated_when_new_revision_is_uncertain(self):
        self.answers['m1'] = 'selected'
        self.profile(); self.page(['m1'])
        await self.adapter.synchronize('mail')
        old = self.service.query()[0]
        self.answers['m1'] = 'uncertain'
        self.profile('20'); self.history('10', ['m1'], end='20')
        result = await self.adapter.synchronize('mail')
        current = self.service.query()[0]
        self.assertEqual('degraded', result['health'])
        self.assertEqual('degraded', current['source']['availability'])
        self.assertTrue(current['source']['revision'].startswith('unassessed:message:20:'))
        self.assertGreater(current['version'], old['version'])
        self.assertEqual(old['original'], current['original'])
        self.assertIsNone(current['source']['sha256'])
        self.assertIn('m1', result['pending_reads'])
        self.assertEqual(1, self.service.store.db.execute('SELECT count(*) FROM originals').fetchone()[0])

    async def test_selected_source_read_error_invalidates_current_basis_without_retaining_body(self):
        self.answers['m1'] = 'selected'
        self.profile(); self.page(['m1'])
        await self.adapter.synchronize('mail')
        old = self.service.query()[0]
        self.profile('20')
        self.transport.add(fixtures.GMAIL + '/history', {'maxResults': 2, 'startHistoryId': '10'},
            {'historyId': '20', 'history': [{'id': '20', 'messagesAdded': [{'message': {'id': 'm1'}}]}]})
        self.transport.add(fixtures.GMAIL + '/messages/m1', {'format': 'raw'}, {}, status=404)
        result = await self.adapter.synchronize('mail')
        current = self.service.query()[0]
        self.assertEqual('degraded', current['source']['availability'])
        self.assertGreater(current['version'], old['version'])
        self.assertIn('m1', result['pending_reads'])
        self.assertIsNone(result['pending_reads']['m1']['revision'])
        self.assertEqual(1, self.service.store.db.execute('SELECT count(*) FROM originals').fetchone()[0])

    def enable_priority(self, terms=None):
        self.config['mail'].update(priority_terms=terms or ['Asistencia', 'Telemedicina', 'HODOM'], max_pages=1)
        self.adapter = GoogleSources(SourceSync(self.service), self.transport, self.config, evaluator=self.evaluate)

    def priority_page(self, messages, *, token=None, next_token=None):
        from gtd_felix.google_sources import priority_query
        query = {'maxResults': 2, 'includeSpamTrash': 'true', 'q': priority_query(self.config['mail']['priority_terms'])}
        if token:
            query['pageToken'] = token
        body = {'messages': [{'id': identity} for identity in messages]}
        if next_token:
            body['nextPageToken'] = next_token
        self.transport.add(fixtures.GMAIL + '/messages', query, body)
        for identity in messages:
            self.transport.add(fixtures.GMAIL + '/messages/' + identity, {'format': 'raw'},
                fixtures.raw_message(identity, labels=['CATEGORY_PROMOTIONS']))

    async def test_priority_pages_restart_global_scope_and_revision_dedup(self):
        partition = self.adapter.inspect('mail')['partition']
        self.enable_priority()
        self.assertEqual(partition, self.adapter.inspect('mail')['partition'])
        self.answers['relevant'] = 'selected'
        self.profile(); self.priority_page(['relevant'], next_token='priority-two')
        first = await self.adapter.synchronize('mail')
        self.assertEqual('priority', first['priority']['phase'])
        self.assertTrue(first['priority']['global_backfill_pending'])
        self.assertIsNone(first['sync']['cursor'])
        self.assertEqual('present', self.service.query()[0]['source']['availability'])
        self.restart(); self.priority_page(['noise'], token='priority-two')
        second = await self.adapter.synchronize('mail')
        self.assertEqual('global', second['priority']['phase'])
        self.assertNotEqual('complete', second['health'])
        self.assertIsNone(second['sync']['cursor'])
        self.restart(); self.page(['relevant', 'noise'])
        final = await self.adapter.synchronize('mail')
        self.assertEqual('10', final['sync']['cursor'])
        self.assertEqual('complete', final['priority']['phase'])
        self.assertEqual(['relevant', 'noise'], self.evaluated)
        self.assertEqual(1, len(self.service.query()))
        self.profile('20'); self.history('10', end='20')
        incremental = await self.adapter.synchronize('mail')
        self.assertEqual('20', incremental['sync']['cursor'])
        self.assertEqual(['relevant', 'noise'], self.evaluated)

    async def test_priority_can_preempt_started_backfill_without_losing_global_page(self):
        self.config['mail']['max_pages'] = 1
        self.restart(); self.profile(); self.page(['first'], next_token='global-two')
        initial = await self.adapter.synchronize('mail')
        cycle_id = initial['adapter']['cycle_id']
        self.enable_priority(); self.priority_page(['priority'])
        priority = await self.adapter.synchronize('mail')
        self.assertEqual(cycle_id, priority['adapter']['cycle_id'])
        self.assertEqual('global', priority['priority']['phase'])
        self.restart(); self.page(['last'], token='global-two')
        final = await self.adapter.synchronize('mail')
        self.assertEqual('10', final['sync']['cursor'])
        self.assertEqual(['first', 'priority', 'last'], self.evaluated)

    async def test_priority_term_change_rejected_without_cursor_or_cycle_mutation(self):
        from gtd_felix.google_sources import SourceError
        self.enable_priority(); self.profile(); self.priority_page([])
        before = await self.adapter.synchronize('mail')
        for terms in ([], ['Other']):
            self.config['mail']['priority_terms'] = terms
            self.restart()
            with self.assertRaisesRegex(SourceError, '^priority_terms_changed_active_cycle$'):
                await self.adapter.synchronize('mail')
            self.assertEqual(before['sync'], self.adapter.inspect('mail')['sync'])
        self.config['mail']['priority_terms'] = ['Asistencia', 'Telemedicina', 'HODOM']
        self.restart(); self.page([])
        self.assertEqual('complete', (await self.adapter.synchronize('mail'))['health'])

    async def test_priority_page_commit_crash_resumes_global_not_priority(self):
        from unittest.mock import patch
        self.enable_priority(); self.profile(); self.priority_page(['m1'])
        apply_page = self.adapter.sync.apply_page
        def crash(*args):
            apply_page(*args)
            raise SystemExit('synthetic-crash')
        with patch.object(self.adapter.sync, 'apply_page', side_effect=crash):
            with self.assertRaises(SystemExit):
                await self.adapter.synchronize('mail')
        self.restart(); self.page(['m1'])
        result = await self.adapter.synchronize('mail')
        self.assertEqual('10', result['sync']['cursor'])
        self.assertEqual(['m1'], self.evaluated)

    async def test_priority_uncertain_debt_survives_then_global_revision_changes(self):
        self.enable_priority(); self.answers['m1'] = 'uncertain'
        self.profile(); self.priority_page(['m1'])
        first = await self.adapter.synchronize('mail')
        self.assertIn('m1', first['pending_reads'])
        self.assertEqual('degraded', first['health'])
        self.assertEqual(0, self.service.store.db.execute('SELECT count(*) FROM originals').fetchone()[0])
        self.restart(); self.answers['m1'] = 'selected'
        self.transport.add(fixtures.GMAIL + '/messages/m1', {'format': 'raw'},
            fixtures.raw_message('m1', labels=['CATEGORY_PROMOTIONS']))
        self.page(['m1'])
        final = await self.adapter.synchronize('mail')
        self.assertEqual('complete', final['health'])
        self.assertEqual(['m1', 'm1'], self.evaluated)
        self.profile('20'); self.answers['m1'] = 'noise'; self.history('10', ['m1'], end='20')
        changed = await self.adapter.synchronize('mail')
        self.assertEqual('20', changed['sync']['cursor'])
        self.assertEqual('degraded', self.service.query()[0]['source']['availability'])
        self.assertEqual(1, self.service.store.db.execute('SELECT count(*) FROM originals').fetchone()[0])

    async def test_expired_history_rebuild_retains_scope_and_priority_is_not_complete(self):
        self.enable_priority(); self.profile(); self.priority_page([])
        await self.adapter.synchronize('mail'); self.page([])
        await self.adapter.synchronize('mail')
        self.profile('30'); self.history('10', status=404)
        expired = await self.adapter.synchronize('mail')
        self.assertFalse(expired['sync']['cursor_valid'])
        self.profile('40'); self.priority_page([])
        priority = await self.adapter.synchronize('mail')
        self.assertEqual('rebuild', priority['adapter']['mode'])
        self.assertNotEqual('complete', priority['health'])
        self.assertFalse(priority['sync']['cursor_valid'])
        self.page([])
        final = await self.adapter.synchronize('mail')
        self.assertEqual('40', final['sync']['cursor'])
        self.assertEqual('lost_rebuilt_scope', final['coverage_contract']['history_continuity'])
