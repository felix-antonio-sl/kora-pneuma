"""Useful Telegram replies and direct controls; synthetic transport, real store."""
import dataclasses
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
