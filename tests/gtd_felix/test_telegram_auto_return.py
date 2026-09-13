"""Automatic owner returns, real durable service and entirely synthetic HTTP."""
import asyncio
import dataclasses
import json
import unittest
import test_telegram as fixture
from test_telegram import TelegramAdapter, Response, message


class AutoReturnTests(unittest.IsolatedAsyncioTestCase):
    setUp = fixture.TelegramTests.setUp
    tearDown = fixture.TelegramTests.tearDown
    prepared_item = fixture.TelegramTests.prepared_item
    notification = fixture.TelegramTests.notification
    restart = fixture.TelegramTests.restart
    deliver = fixture.TelegramTests.deliver
    click_named = fixture.TelegramTests.click_named

    def enable(self, **changes):
        self.config = dataclasses.replace(self.config, auto_return=True, **changes)
        self.adapter = TelegramAdapter(self.service, self.client, self.config)

    def attention(self, **fields):
        result = self.service.execute('felix', {'operation_id': 'attention-' + str(len(self.http.calls)) + str(fields),
            'action': 'set_attention', 'fields': fields})
        self.assertIn(result['status'], {'applied', 'already_applied'})

    async def test_opt_in_and_restart_no_duplicate_with_persistent_controls(self):
        self.notification(self.prepared_item('RESULTADO-AUTO'))
        await self.adapter.process_pending()
        self.assertEqual([], self.http.sent)
        self.enable()
        await self.adapter.process_pending()
        self.assertEqual(1, len(self.http.sent))
        self.assertIn('RESULTADO-AUTO', self.http.sent[0]['text'])
        with self.service.store.lock:
            receipt = json.loads(self.service.store.db.execute(
                "SELECT value FROM metadata WHERE key LIKE 'telegram-delivery:%'").fetchone()[0])
        self.assertEqual('automatic', receipt['delivery_mode'])
        self.assertIsNone(receipt['request_event_key'])
        self.restart()
        await self.adapter.process_pending()
        self.assertEqual(1, len(self.http.sent))
        await self.click_named('Ver asunto', 123)
        self.assertIn('Nota', self.http.sent[-1]['text'])

    async def test_global_pause_notify_and_resume(self):
        self.enable()
        self.notification(self.prepared_item())
        self.attention(paused=True)
        await self.adapter.process_pending()
        self.assertFalse(self.http.sent)
        self.attention(paused=False, notify=False)
        await self.adapter.process_pending()
        self.assertFalse(self.http.sent)
        self.attention(notify=True)
        await self.adapter.process_pending()
        self.assertEqual(1, len(self.http.sent))

    async def test_pause_between_chunks_resumes_without_repeating_first(self):
        self.enable()
        self.notification(self.prepared_item('x' * 5000))
        self.http.on_send = lambda payload: self.attention(paused=True)
        await self.adapter.process_pending()
        self.assertEqual(1, len(self.http.sent))
        self.http.on_send = None
        self.attention(paused=False)
        self.restart()
        await self.adapter.process_pending()
        self.assertEqual(3, len(self.http.sent))
        self.assertFalse(self.service.pending_events('gtd-notification', 'local'))

    async def test_uncertain_does_not_replay_or_hide_new_result(self):
        self.enable()
        self.notification(self.prepared_item('UNCERTAIN'))
        original = self.http.request
        def lost(method, url, **kwargs):
            response = original(method, url, **kwargs)
            if url.endswith('/sendMessage'):
                class Lost(Response):
                    async def __aenter__(self):
                        raise TimeoutError('synthetic lost response')
                return Lost()
            return response
        self.http.request = lost
        await self.adapter.process_pending()
        self.restart()
        self.http.request = original
        self.notification(self.prepared_item('NEW-RESULT'), 'new')
        await self.adapter.process_pending()
        self.assertEqual(2, len(self.http.sent))
        self.assertIn('NEW-RESULT', self.http.sent[-1]['text'])
        self.assertEqual(1, len(self.service.pending_events('gtd-notification', 'local')))

    async def test_changed_destination_and_nonowner_refused(self):
        self.enable()
        self.notification(self.prepared_item('FIRST'))
        await self.adapter.process_pending()
        self.notification(self.prepared_item('PRIVATE'), 'private')
        self.enable(chat_id=99)
        await self.adapter.process_pending()
        self.enable(chat_id=9, owner_user_id=99)
        await self.adapter.process_pending()
        self.enable(owner_user_id=7, actor='gtd-felix')
        await self.adapter.process_pending()
        self.assertEqual(1, len(self.http.sent))

    async def test_noise_and_blocked_material_do_not_hide_native_reply(self):
        self.enable()
        for index in range(11):
            self.notification(self.prepared_item('x' * 65537), str(index))
        item = self.prepared_item('noise')
        for kind in ['no_domain_progress', 'routed']:
            self.service.ingest_event({'provider': 'gtd-notification', 'account': 'local',
                'external_id': kind, 'revision': '1', 'payload': {'item_id': item['id'],
                'version': item['version'], 'kind': kind, 'text': 'NOISE', 'native_reply': 'NOISE'}})
        item = self.service.capture('felix', 'native', 'Question')['item']
        self.service.ingest_event({'provider': 'gtd-notification', 'account': 'local',
            'external_id': 'native', 'revision': '1', 'payload': {'item_id': item['id'],
            'version': item['version'], 'kind': 'updated', 'text': 'ANSWER', 'native_reply': 'ANSWER'}})
        await self.adapter.process_pending()
        self.assertEqual(1, len(self.http.sent))
        self.assertIn('ANSWER', self.http.sent[0]['text'])

    async def test_auto_and_requested_concurrency_share_outbox(self):
        self.enable()
        self.notification(self.prepared_item('SINGLE'))
        await asyncio.gather(self.adapter.process_pending(), self.deliver(message(1, '/preparado')))
        self.assertEqual(1, sum('SINGLE' in sent['text'] for sent in self.http.sent))

    async def test_recovery_blocks_return(self):
        self.enable()
        self.notification(self.prepared_item())
        with self.service.store.transaction() as db:
            db.execute("INSERT OR REPLACE INTO metadata VALUES('recovery_required','true')")
        await self.adapter.process_pending()
        self.assertFalse(self.http.sent)

    def command(self, item, action, fields=None):
        receipt = self.service.execute('felix', {'operation_id': action + '-' + item['id'] + '-' + str(item['version']),
            'action': action, 'item_id': item['id'], 'expected_version': item['version'], 'fields': fields or {}})
        self.assertEqual('applied', receipt['status'], receipt)
        return receipt['item']

    async def test_paused_item_requires_new_current_return_after_reopen(self):
        self.enable()
        item = self.command(self.prepared_item('PAUSED'), 'pause')
        self.notification(item)
        await self.adapter.process_pending()
        self.assertFalse(self.http.sent)
        item = self.command(item, 'reopen')
        self.notification(item, 'resumed-current')
        await self.adapter.process_pending()
        self.assertEqual(1, len(self.http.sent))
        self.assertFalse(self.service.pending_events('gtd-notification', 'local'))

    async def test_ancestor_pause_between_chunks_and_resume(self):
        self.enable()
        parent = self.service.capture('felix', 'parent', 'Parent')['item']
        parent = self.command(parent, 'clarify', {'kind': 'project', 'commitment': 'committed',
            'capability': 'prepare_private', 'completion_criteria': 'Result checked',
            'intent_basis': {'quote': parent['text'], 'source_item_id': parent['id']}})
        child = self.command(parent, 'derive', {'kind': 'action', 'title': 'Child',
            'completion_criteria': 'Result checked'})
        child = self.service.execute('gtd-felix', {'operation_id': 'child-material', 'action': 'put_material',
            'item_id': child['id'], 'expected_version': child['version'], 'fields': {'content': 'x' * 5000}})['item']
        self.notification(child)
        self.http.on_send = lambda payload: self.command(self.service.get_item(parent['id']), 'pause')
        await self.adapter.process_pending()
        self.assertEqual(1, len(self.http.sent))
        self.http.on_send = None
        self.command(self.service.get_item(parent['id']), 'reopen')
        self.restart()
        await self.adapter.process_pending()
        self.assertEqual(3, len(self.http.sent))

    async def test_correction_between_chunks_suppresses_obsolete_rest(self):
        self.enable()
        item = self.prepared_item('x' * 5000)
        self.notification(item)
        self.http.on_send = lambda payload: self.command(item, 'edit', {'title': 'Corrected'})
        await self.adapter.process_pending()
        self.assertEqual(1, len(self.http.sent))
        self.assertFalse(self.service.pending_events('gtd-notification', 'local'))

    async def test_bounded_pass_and_restart_continue_remaining(self):
        self.enable()
        for index in range(11):
            self.notification(self.prepared_item('RESULT-' + str(index)), str(index))
        await self.adapter.process_pending()
        self.assertEqual(10, len(self.http.sent))
        self.assertEqual(0, len(self.adapter._notification_locks))
        self.restart()
        await self.adapter.process_pending()
        self.assertEqual(11, len(self.http.sent))

    async def test_auto_receipt_failure_after_send_restart_keeps_payload_and_controls(self):
        self.enable()
        self.notification(self.prepared_item('RECEIPT-RECOVERY'))
        self.adapter._notification_receipt = lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError('synthetic receipt failure'))
        await self.adapter.process_pending()
        first = self.http.sent[0]
        self.assertEqual(1, len(self.service.pending_events('gtd-notification', 'local')))
        self.restart()
        await self.adapter.process_pending()
        self.assertEqual([first], self.http.sent)
        self.assertFalse(self.service.pending_events('gtd-notification', 'local'))
        await self.click_named('Ver asunto', 4242)
        self.assertIn('Nota', self.http.sent[-1]['text'])

    async def test_nonstring_native_reply_cannot_block_later_useful_result(self):
        self.enable()
        item = self.service.capture('felix', 'malformed-native', 'Malformed')['item']
        self.service.ingest_event({'provider': 'gtd-notification', 'account': 'local',
            'external_id': 'malformed-native', 'revision': '1', 'payload': {'item_id': item['id'],
            'version': item['version'], 'kind': 'updated', 'native_reply': {'unexpected': 'object'}}})
        self.notification(self.prepared_item('GOOD-AFTER-MALFORMED'), 'good')
        await self.adapter.process_pending()
        self.assertEqual(1, len(self.http.sent))
        self.assertIn('GOOD-AFTER-MALFORMED', self.http.sent[0]['text'])
