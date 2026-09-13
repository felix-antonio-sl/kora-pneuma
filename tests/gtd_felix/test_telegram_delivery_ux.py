"""Useful Telegram replies and direct controls; synthetic transport, real store."""
import dataclasses
import asyncio
from unittest.mock import patch, AsyncMock
import unittest
import test_telegram as fixtures


class DeliveryUXTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.fixture = fixtures.TelegramTests()
        self.fixture.setUp()
        self.service = self.fixture.service
        self.adapter = self.fixture.adapter
        self.http = self.fixture.http

    def tearDown(self):
        self.fixture.tearDown()

    def capture(self):
        return self.service.capture('felix', 'ux-capture', 'Actualizar mapa de responsabilidades')['item']

    async def test_native_reply_is_delivered_once_without_repeated_record_or_question(self):
        item = self.capture()
        item = self.service.execute('felix', {'operation_id': 'ux-question', 'action': 'edit',
            'item_id': item['id'], 'expected_version': item['version'],
            'fields': {'decision_needed': True, 'decision_question': '¿Qué período revisamos?'}})['item']
        event = {'payload': {'item_id': item['id'], 'version': item['version'],
            'kind': 'updated', 'native_reply': '¿Qué período revisamos?',
            'text': 'Registro actualizado: ' + item['title'] + '\n¿Qué período revisamos?'}}
        self.assertEqual(self.adapter._notification_content(event), ['¿Qué período revisamos?'])

    async def test_automatic_reply_has_direct_item_pause_and_preserves_newer_content(self):
        item = self.capture()
        self.adapter.config = dataclasses.replace(self.adapter.config, auto_return=True)
        self.service.ingest_event({'provider': 'gtd-notification', 'account': 'local',
            'external_id': 'ux-reply', 'revision': '1', 'payload': {'item_id': item['id'],
                'version': item['version'], 'kind': 'updated', 'native_reply': 'Prepararé el mapa con los antecedentes disponibles.'}})
        event = self.service.pending_events('gtd-notification', 'local')[0]
        await self.adapter._deliver_notification(event, automatic=True)
        buttons = [b for row in self.http.sent[-1]['reply_markup']['inline_keyboard'] for b in row]
        button = next(b for b in buttons if b['text'] == 'Pausar este asunto')
        self.assertFalse(any(b['text'] == 'Pausar avisos' for b in buttons))
        current = self.service.execute('felix', {'operation_id': 'ux-newer-title', 'action': 'edit',
            'item_id': item['id'], 'expected_version': item['version'], 'fields': {'title': 'Título corregido por Félix'}})['item']
        await self.adapter._callback({'id': 'ux-pause', 'data': button['callback_data']})
        paused = self.service.get_item(item['id'])
        self.assertEqual(paused['status'], 'paused')
        self.assertEqual(paused['title'], current['title'])
        self.assertFalse(self.service._meta('attention', {}).get('paused', False))

    def question_item(self, question='¿Qué período revisamos?'):
        item = self.capture()
        receipt = self.service.execute('felix', {'operation_id': 'durable-question', 'action': 'edit',
            'item_id': item['id'], 'expected_version': item['version'],
            'fields': {'decision_needed': True, 'decision_question': question}})
        self.assertEqual('applied', receipt['status'], receipt)
        self.adapter.config = dataclasses.replace(self.adapter.config, auto_return=True)
        return receipt['item']

    def return_event(self, item, operation):
        receipt = self.service.ingest_event({'provider': 'gtd-notification', 'account': 'local',
            'external_id': operation, 'revision': '1', 'payload': {'item_id': item['id'],
                'version': item['version'], 'job_id': operation, 'kind': 'updated',
                'native_reply': '¿Qué período revisamos?'}})
        return next(e for e in self.service.pending_events('gtd-notification', 'local')
                    if e['event_key'] == receipt['event_key'])

    async def test_same_question_across_jobs_and_restart_is_not_sent_again(self):
        item = self.question_item()
        await self.adapter._deliver_notification(self.return_event(item, 'job-one'), automatic=True)
        self.assertEqual(1, len(self.http.sent))
        config = self.adapter.config
        self.service.close()
        self.service = fixtures.GTDService(fixtures.Path(self.fixture.temp.name))
        self.fixture.service = self.service
        self.adapter = fixtures.TelegramAdapter(self.service, self.fixture.client, config)
        events = [self.return_event(item, 'job-two'), self.return_event(item, 'job-three')]
        await asyncio.gather(*(self.adapter._deliver_notification(event, automatic=True) for event in events))
        self.assertEqual(1, len(self.http.sent))
        await self.adapter.show_item(item)
        self.assertIn(item['decision_question'], self.http.sent[-1]['text'])

    async def test_technical_plan_version_is_not_a_new_question_basis(self):
        item = self.question_item()
        await self.adapter._deliver_notification(self.return_event(item, 'before-plan'), automatic=True)
        receipt = self.service.execute('gtd-felix', {'operation_id': 'technical-plan', 'action': 'plan',
            'item_id': item['id'], 'expected_version': item['version'],
            'fields': {'plan_steps': ['Reintentar comprobación técnica']}})
        self.assertEqual('applied', receipt['status'], receipt)
        item = self.service.get_item(item['id'])
        await self.adapter._deliver_notification(self.return_event(item, 'after-plan'), automatic=True)
        self.assertEqual(1, len(self.http.sent))

    async def test_source_correction_reopens_delivery_of_same_question(self):
        item = self.question_item()
        await self.adapter._deliver_notification(self.return_event(item, 'before-source'), automatic=True)
        item = self.service.execute('felix', {'operation_id': 'source-correction', 'action': 'edit',
            'item_id': item['id'], 'expected_version': item['version'],
            'fields': {'text': 'Antecedentes corregidos del informe'}})['item']
        await self.adapter._deliver_notification(self.return_event(item, 'after-source'), automatic=True)
        self.assertEqual(2, len(self.http.sent))

    async def test_new_material_and_human_change_are_delivered(self):
        item = self.question_item()
        await self.adapter._deliver_notification(self.return_event(item, 'first'), automatic=True)
        receipt = self.service.execute('felix', {'operation_id': 'new-material', 'action': 'put_material',
            'item_id': item['id'], 'expected_version': item['version'],
            'fields': {'title': 'Aporte nuevo', 'content': 'Evidencia útil nueva', 'source_versions': {}}})
        self.assertEqual('applied', receipt['status'], receipt)
        item = self.service.get_item(item['id'])
        await self.adapter._deliver_notification(self.return_event(item, 'material-return'), automatic=True)
        self.assertTrue(any('Evidencia útil nueva' in message['text'] for message in self.http.sent))
        count = len(self.http.sent)
        item = self.service.execute('felix', {'operation_id': 'owner-correction', 'action': 'edit',
            'item_id': item['id'], 'expected_version': item['version'],
            'fields': {'decision_question': '¿Qué período y unidad revisamos?'}})['item']
        # Change a decision field: no material basis meaning change is needed to reopen delivery.
        await self.adapter._deliver_notification(self.return_event(item, 'new-position'), automatic=True)
        self.assertGreater(len(self.http.sent), count)

    async def test_new_assessment_gap_delivered_despite_same_pending_question(self):
        item = self.capture()
        receipt = self.service.execute('gtd-felix', {'operation_id': 'assessment-action', 'action': 'clarify',
            'item_id': item['id'], 'expected_version': item['version'], 'fields': {
                'kind': 'action', 'commitment': 'committed', 'capability': 'prepare_private',
                'outcome': 'Preparar informe', 'completion_criteria': 'Informe comprobado',
                'intent_basis': {'source_item_id': item['id'], 'quote': item['text']}}})
        self.assertEqual('applied', receipt['status'], receipt)
        self.adapter.config = dataclasses.replace(self.adapter.config, auto_return=True)
        def command(operation, action, fields):
            current = self.service.get_item(item['id'])
            result = self.service.execute('gtd-felix', {'operation_id': operation, 'action': action,
                'item_id': item['id'], 'expected_version': current['version'], 'fields': fields})
            self.assertEqual('applied', result['status'], result)
            return self.service.get_item(item['id'])
        question = {'decision_needed': True, 'decision_question': '¿Qué período revisamos?'}
        current = command('ask-first', 'plan', question)
        await self.adapter._deliver_notification(self.return_event(current, 'before-assessment'), automatic=True)
        for suffix, evidence, gap in [('new', 'Falta el período en la fuente comprobada', 'Completar período'),
                                      ('repeat', 'Falta el período en la fuente comprobada', 'Completar período')]:
            command('clear-' + suffix, 'plan', {'decision_needed': False, 'decision_question': ''})
            command('assess-' + suffix, 'assess_result', {'satisfied': False, 'evidence': evidence, 'gap': gap})
            current = command('ask-' + suffix, 'plan', question)
            await self.adapter._deliver_notification(self.return_event(current, 'after-' + suffix), automatic=True)
            self.assertEqual(2, len(self.http.sent))  # New evidence delivered; timestamp/version-only repeat suppressed.

    async def test_empty_durable_question_never_inferred_from_native_reply(self):
        item = self.question_item('')
        for job in ('empty-first', 'empty-second'):
            await self.adapter._deliver_notification(self.return_event(item, job), automatic=True)
        self.assertEqual(2, len(self.http.sent))

    async def test_unconfirmed_delivery_does_not_establish_question_memory(self):
        item = self.question_item()
        event = self.return_event(item, 'uncertain-first')
        with patch.object(self.adapter, '_send', new=AsyncMock(return_value=None)):
            await self.adapter._deliver_notification(event, automatic=True)
        with self.service.store.lock:
            self.assertIsNone(self.service._meta(self.adapter._question_return_key(event)))
        await self.adapter._deliver_notification(self.return_event(item, 'after-uncertain'), automatic=True)
        self.assertEqual(1, len(self.http.sent))

    async def test_parallel_first_returns_only_one_confirmed_question(self):
        item = self.question_item()
        events = [self.return_event(item, name) for name in ('parallel-one', 'parallel-two')]
        await asyncio.gather(*(self.adapter._deliver_notification(event, automatic=True) for event in events))
        self.assertEqual(1, len(self.http.sent))

    def material_item(self):
        item = self.capture()
        result = self.service.execute('felix', {'operation_id': 'material-first', 'action': 'put_material',
            'item_id': item['id'], 'expected_version': item['version'],
            'fields': {'title': 'Informe', 'content': 'OLD_MATERIAL_BODY', 'source_versions': {}}})
        self.assertEqual('applied', result['status'], result)
        self.adapter.config = dataclasses.replace(self.adapter.config, auto_return=True)
        return result['item']

    async def test_confirmed_material_not_reattached_after_restart_but_explicit_read_full(self):
        item = self.material_item()
        await self.adapter._deliver_notification(self.return_event(item, 'material-first-return'), automatic=True)
        self.assertIn('OLD_MATERIAL_BODY', self.http.sent[-1]['text'])
        config = self.adapter.config
        self.service.close()
        self.service = fixtures.GTDService(fixtures.Path(self.fixture.temp.name))
        self.fixture.service = self.service
        self.adapter = fixtures.TelegramAdapter(self.service, self.fixture.client, config)
        await self.adapter._deliver_notification(self.return_event(item, 'material-second-return'), automatic=True)
        self.assertEqual('¿Qué período revisamos?', self.http.sent[-1]['text'])
        await self.adapter.show_result(item['id'])
        self.assertIn('OLD_MATERIAL_BODY', self.http.sent[-1]['text'])

    async def test_changed_material_version_delivered_and_other_account_not_deduplicated(self):
        item = self.material_item()
        await self.adapter._deliver_notification(self.return_event(item, 'initial-material'), automatic=True)
        material = self.service.materials(item['id'])[-1]
        result = self.service.execute('felix', {'operation_id': 'material-updated', 'action': 'put_material',
            'item_id': item['id'], 'expected_version': item['version'], 'fields': {
                'material_id': material['id'], 'title': 'Informe', 'content': 'NEW_MATERIAL_BODY', 'source_versions': {}}})
        self.assertEqual('applied', result['status'], result)
        item = result['item']
        await self.adapter._deliver_notification(self.return_event(item, 'updated-material'), automatic=True)
        self.assertIn('NEW_MATERIAL_BODY', self.http.sent[-1]['text'])
        self.assertNotIn('OLD_MATERIAL_BODY', self.http.sent[-1]['text'])
        self.adapter.config = dataclasses.replace(self.adapter.config, account='other-owner-account')
        await self.adapter._deliver_notification(self.return_event(item, 'other-account-material'), automatic=True)
        self.assertIn('NEW_MATERIAL_BODY', self.http.sent[-1]['text'])

    async def test_uncertain_material_delivery_keeps_material_for_next_return(self):
        item = self.material_item()
        event = self.return_event(item, 'uncertain-material')
        with patch.object(self.adapter, '_send', new=AsyncMock(return_value=None)):
            await self.adapter._deliver_notification(event, automatic=True)
        with self.service.store.lock:
            self.assertIsNone(self.service._meta(self.adapter._material_return_key(event)))
        await self.adapter._deliver_notification(self.return_event(item, 'after-uncertain-material'), automatic=True)
        self.assertIn('OLD_MATERIAL_BODY', self.http.sent[-1]['text'])

    async def test_capture_ack_and_list_use_human_language(self):
        await self.fixture.deliver(fixtures.message(980, 'Mensaje con un título largo que no hace falta repetir'))
        self.assertEqual(self.http.sent[-1]['text'], 'Guardado.')
        await self.adapter.show_list()
        text = self.http.sent[-1]['text']
        self.assertNotIn('capture', text)
        self.assertNotIn('active', text)
        self.assertIn('Por aclarar', text)
        item = self.service.query()[0]
        await self.adapter.show_item(item)
        labels = [b['text'] for row in self.http.sent[-1]['reply_markup']['inline_keyboard'] for b in row]
        self.assertIn('Pausar asunto', labels)
