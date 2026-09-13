"""Synthetic in-process Telegram HTTP and real durable GTD service tests."""
import asyncio
import copy
import sys
import tempfile
import unittest
from pathlib import Path

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from gtd_felix.telegram import AiohttpTelegramClient, TelegramAdapter, TelegramConfig, TelegramError
from gtd_felix.service import GTDService


class FakeContent:
    def __init__(self, data):
        self.data = data

    async def iter_chunked(self, size):
        for index in range(0, len(self.data), size):
            yield self.data[index:index + size]


class Response:
    def __init__(self, value=None, status=200, data=b'original audio'):
        self.value, self.status, self.content = value, status, FakeContent(data)

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass

    async def json(self):
        return {'ok': True, 'result': self.value}


class FakeHTTP:
    def __init__(self):
        self.updates, self.calls, self.sent = [], [], []
        self.file_failure = False
        self.file_data = b'original audio'
        self.download_gate = None
        self.on_send = None
        self.next_message = 1000

    def request(self, method, url, *, json=None, timeout=None):
        name = url.rsplit('/', 1)[-1]
        self.calls.append((name, copy.deepcopy(json)))
        if name == 'getUpdates':
            offset = json.get('offset', 0)
            return Response([u for u in self.updates if u['update_id'] >= offset])
        if name == 'getFile':
            return Response({'file_path': 'voice/test.ogg', 'file_size': 14})
        if name == 'test.ogg':
            if self.file_failure:
                return Response(status=503)
            if self.download_gate:
                gate = self.download_gate
                class WaitingResponse(Response):
                    async def __aenter__(self):
                        await gate.wait()
                        return self
                return WaitingResponse()
            return Response(data=self.file_data)
        if name == 'sendMessage':
            if self.on_send:
                self.on_send(json)
            self.sent.append(copy.deepcopy(json))
            self.next_message += 1
            return Response({'message_id': self.next_message})
        if name == 'answerCallbackQuery':
            return Response(True)
        raise AssertionError('unexpected HTTP method')


def message(update_id, text='Ana, filtro', *, message_id=None, user=7, chat=9, **extra):
    return {'update_id': update_id, 'message': {'message_id': message_id or update_id,
        'date': 100, 'chat': {'id': chat}, 'from': {'id': user}, 'text': text, **extra}}


class TelegramTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.service = GTDService(Path(self.temp.name))
        self.http = FakeHTTP()
        self.client = AiohttpTelegramClient('synthetic-secret', self.http, attempts=1)
        self.config = TelegramConfig('synthetic-bot', 7, 9, 'felix')
        self.adapter = TelegramAdapter(self.service, self.client, self.config)

    def tearDown(self):
        self.service.close()
        self.temp.cleanup()

    def notification(self, item, identity='job-return'):
        return self.service.ingest_event({'provider': 'gtd-notification', 'account': 'local',
            'external_id': identity, 'revision': '1', 'payload': {'item_id': item['id'],
            'version': item['version'], 'kind': 'updated', 'text': 'Registro actualizado', 'delivery': 'pending'}})['event_key']

    async def click_named(self, label, update_id):
        button = next(b for row in self.http.sent[-1]['reply_markup']['inline_keyboard']
                      for b in row if b['text'] == label)
        await self.deliver({'update_id': update_id, 'callback_query': {
            'id': 'click-' + str(update_id), 'from': {'id': 7},
            'message': {'chat': {'id': 9}}, 'data': button['callback_data']}})

    def synced_sources(self, count=1):
        import hashlib
        from gtd_felix.source_sync import SourceSync
        sync = SourceSync(self.service)
        partition = dict(provider='calendar-fixture', account='a', collection='cal', scope_digest='a' * 64)
        sync.begin(partition, 'list-fixture')
        objects = []
        for index in range(count):
            data = f'calendar {index}'.encode()
            objects.append(dict(external_id=str(index), revision='1', text=data.decode(),
                original=data, sha256=hashlib.sha256(data).hexdigest(),
                url='https://example.invalid/event', status='present'))
        state = sync.apply_page(partition, 'list-fixture', dict(page_id='p1', request_token=None,
            next_page_token=None, cursor='c1', objects=objects))
        return [record['item_id'] for record in state['objects'].values()]

    async def test_default_list_distinguishes_durable_sources_and_converted_affairs(self):
        source_ids = self.synced_sources(3)
        human = self.service.capture('felix', 'human-calendar', 'calendar human',
            source={'provider': 'calendar-fixture'})['item']
        converted = self.service.execute('felix', {'operation_id': 'convert-source', 'action': 'edit',
            'item_id': source_ids[0], 'expected_version': 1, 'fields': {'kind': 'action'}})
        self.assertEqual('applied', converted['status'])
        changed = self.service.execute('felix', {'operation_id': 'edit-source-metadata', 'action': 'edit',
            'item_id': source_ids[1], 'expected_version': 1, 'fields': {'source': {'provider': 'human'}}})
        self.assertEqual('applied', changed['status'])
        self.restart()
        visible = await self.adapter.show_list()
        self.assertEqual({human['id'], source_ids[0]}, {item['id'] for item in visible})
        selected = self.service.execute('felix', {'operation_id': 'use-source', 'action': 'edit',
            'item_id': source_ids[0], 'expected_version': 2,
            'fields': {'source_versions': {source_ids[2]: 1}}})
        self.assertEqual('applied', selected['status'])
        self.restart()
        visible = await self.adapter.show_list()
        self.assertEqual({human['id'], source_ids[0], source_ids[2]}, {item['id'] for item in visible})
        self.assertEqual(4, len(self.service.query()))
        await self.click_named('Inventario', 981)
        self.assertIn('4 registros', self.http.sent[-1]['text'])
        await self.click_named('Fuentes', 982)
        self.assertIn('3 registros', self.http.sent[-1]['text'])

    async def test_source_list_page_and_batch_selection_survive_restart(self):
        source_ids = self.synced_sources(13)
        await self.deliver(message(983, '/fuentes'))
        self.assertIn('13 registros', self.http.sent[-1]['text'])
        self.restart()
        await self.click_named('Seleccionar varios', 984)
        button = next(b for row in self.http.sent[-1]['reply_markup']['inline_keyboard']
                      for b in row if b['text'].startswith('☐ '))
        await self.click_named(button['text'], 985)
        self.restart()
        await self.click_named('Siguiente', 986)
        self.assertIn('Fuentes sincronizadas', self.http.sent[-1]['text'])
        self.assertIn('1/15 seleccionados', self.http.sent[-1]['text'])
        self.assertIn('13 registros', self.http.sent[-1]['text'])
        await self.click_named('Salir de selección', 987)
        self.assertIn('Fuentes sincronizadas', self.http.sent[-1]['text'])
        await self.click_named('Asuntos', 988)
        self.assertIn('Asuntos · 0', self.http.sent[-1]['text'])
        self.assertEqual(13, len(self.service.query()))

    async def test_return_to_delivered_result_after_restart_without_reopening_notification(self):
        item = self.prepared_item('RESULTADO-RECUPERABLE')
        self.notification(item)
        await self.deliver(message(930, '/preparado'))
        self.restart()
        await self.adapter.show_item(self.service.get_item(item['id']))
        await self.click_named('Ver resultado', 931)
        self.assertEqual(2, sum('RESULTADO-RECUPERABLE' in m['text'] for m in self.http.sent))
        self.assertFalse(self.service.pending_events('gtd-notification', 'local'))
        self.assertEqual(item['version'], self.service.get_item(item['id'])['version'])
        self.restart()
        await self.adapter.process_pending()
        self.assertEqual(2, sum('RESULTADO-RECUPERABLE' in m['text'] for m in self.http.sent))

    async def test_return_card_refreshes_question_wait_and_dates_after_restart(self):
        self.service.capture('felix', 'unrelated-return-card', 'OTRO-ASUNTO-PRIVADO')
        old = self.service.capture('felix', 'return-card', 'Asunto sintético')['item']
        current = self.service.execute('felix', {'operation_id': 'return-card-context',
            'action': 'edit', 'item_id': old['id'], 'expected_version': old['version'],
            'fields': {'kind': 'waiting', 'decision_needed': True,
                'decision_question': '¿Qué opción prefieres?', 'waiting_for': 'Confirmación de fecha',
                'review_at': '2026-12-01', 'decision_at': '2026-12-02'}})['item']
        self.restart()
        await self.adapter.show_item(old)
        text = self.http.sent[-1]['text']
        for value in ('¿Qué opción prefieres?', 'Confirmación de fecha', '2026-12-01', '2026-12-02'):
            self.assertIn(value, text)
        self.assertNotIn('OTRO-ASUNTO-PRIVADO', text)
        for row in self.http.sent[-1]['reply_markup']['inline_keyboard']:
            for button in row:
                payload = self.adapter._lookup(button['callback_data'])
                if 'expected_version' in payload:
                    self.assertEqual(current['version'], payload['expected_version'])
        self.assertEqual(current, self.service.get_item(old['id']))

    async def test_return_card_does_not_revive_corrected_or_resolved_question(self):
        old = self.service.capture('felix', 'return-question', 'Asunto')['item']
        old = self.service.execute('felix', {'operation_id': 'return-old-question', 'action': 'edit',
            'item_id': old['id'], 'expected_version': old['version'],
            'fields': {'decision_needed': True, 'decision_question': 'PREGUNTA-SUPERADA'}})['item']
        current = self.service.execute('felix', {'operation_id': 'return-new-question', 'action': 'edit',
            'item_id': old['id'], 'expected_version': old['version'],
            'fields': {'decision_question': 'PREGUNTA-CORREGIDA'}})['item']
        self.restart()
        await self.adapter.show_item(old)
        self.assertIn('PREGUNTA-CORREGIDA', self.http.sent[-1]['text'])
        self.assertNotIn('PREGUNTA-SUPERADA', self.http.sent[-1]['text'])
        self.service.execute('felix', {'operation_id': 'return-resolved-question', 'action': 'edit',
            'item_id': old['id'], 'expected_version': current['version'],
            'fields': {'decision_needed': False}})
        self.restart()
        await self.adapter.show_item(old)
        self.assertNotIn('PREGUNTA-', self.http.sent[-1]['text'])

    async def test_return_card_terminal_item_does_not_request_old_decision_or_wait(self):
        old = self.service.capture('felix', 'return-terminal', 'Asunto')['item']
        old = self.service.execute('felix', {'operation_id': 'return-terminal-context', 'action': 'edit',
            'item_id': old['id'], 'expected_version': old['version'],
            'fields': {'kind': 'waiting', 'decision_needed': True, 'decision_question': 'PREGUNTA-VIEJA',
                'waiting_for': 'ESPERA-VIEJA', 'review_at': '2026-12-01'}})['item']
        self.service.execute('felix', {'operation_id': 'return-withdraw', 'action': 'withdraw',
            'item_id': old['id'], 'expected_version': old['version']})
        self.restart()
        await self.adapter.show_item(old)
        self.assertIn('Retirado', self.http.sent[-1]['text'])
        for value in ('PREGUNTA-VIEJA', 'ESPERA-VIEJA', '2026-12-01'):
            self.assertNotIn(value, self.http.sent[-1]['text'])

    async def test_return_card_rejects_other_sender_and_chat(self):
        item = self.service.capture('felix', 'return-private', 'ASUNTO-PRIVADO')['item']
        token = self.adapter._token({'action': 'show', 'item_id': item['id']})
        self.restart()
        for update_id, user, chat in ((950, 66, 9), (951, 7, 10)):
            await self.deliver({'update_id': update_id, 'callback_query': {
                'id': 'private-' + str(update_id), 'from': {'id': user},
                'message': {'chat': {'id': chat}}, 'data': token}})
        self.assertFalse(self.http.sent)

    async def test_return_card_marks_long_question_as_truncated(self):
        item = self.service.capture('felix', 'return-long', 'Asunto')['item']
        item = self.service.execute('felix', {'operation_id': 'return-long-question', 'action': 'edit',
            'item_id': item['id'], 'expected_version': item['version'],
            'fields': {'decision_needed': True, 'decision_question': 'x' * 5000}})['item']
        await self.adapter.show_item(item)
        self.assertLessEqual(len(self.http.sent[-1]['text']), 4096)
        self.assertIn('[texto recortado]', self.http.sent[-1]['text'])

    async def test_return_card_emoji_fields_fit_telegram_utf16_limit(self):
        item = self.service.capture('felix', 'return-emoji', 'Asunto')['item']
        item = self.service.execute('felix', {'operation_id': 'return-emoji-fields', 'action': 'edit',
            'item_id': item['id'], 'expected_version': item['version'],
            'fields': {'title': '😀' * 1000, 'kind': 'waiting', 'decision_needed': True,
                'decision_question': '🤔' * 1000, 'waiting_for': '🚀' * 1000,
                'review_at': '2026-12-01', 'decision_at': '2026-12-02'}})['item']
        await self.adapter.show_item(item, more=True)
        text = self.http.sent[-1]['text']
        self.assertLessEqual(len(text.encode('utf-16-le')) // 2, 4096)
        self.assertEqual(3, text.count('[texto recortado]'))
        for value in ('😀', 'Pregunta pendiente: 🤔', 'En espera de: 🚀',
                      'Revisar: 2026-12-01', 'Decidir: 2026-12-02',
                      f"Comandos: {item['id']}@{item['version']}"):
            self.assertIn(value, text)

    async def test_return_card_paused_wait_keeps_explicit_return_without_active_wait(self):
        item = self.service.capture('felix', 'return-paused', 'Asunto')['item']
        item = self.service.execute('felix', {'operation_id': 'return-paused-wait', 'action': 'edit',
            'item_id': item['id'], 'expected_version': item['version'],
            'fields': {'kind': 'waiting', 'waiting_for': 'ESPERA-PAUSADA'}})['item']
        self.service.execute('felix', {'operation_id': 'return-postpone', 'action': 'postpone',
            'item_id': item['id'], 'expected_version': item['version'],
            'fields': {'review_at': '2026-12-01'}})
        self.restart()
        await self.adapter.show_item(item)
        self.assertIn('2026-12-01', self.http.sent[-1]['text'])
        self.assertNotIn('ESPERA-PAUSADA', self.http.sent[-1]['text'])

    async def test_result_button_never_shows_material_invalidated_by_correction(self):
        source = self.service.capture('felix', 'return-source', 'dato original')['item']
        item = self.prepared_item('RESULTADO-SUPERADO', source)
        await self.adapter.show_item(item)
        self.service.execute('felix', {'operation_id': 'return-correction', 'action': 'edit',
            'item_id': source['id'], 'expected_version': source['version'],
            'fields': {'text': 'dato corregido'}})
        await self.click_named('Ver resultado', 932)
        self.assertFalse(any('RESULTADO-SUPERADO' in m['text'] for m in self.http.sent))
        self.assertTrue(any('revisión' in m['text'] for m in self.http.sent))

    async def test_pause_and_resume_keep_captures_and_notification_preference_after_restart(self):
        self.service.execute('felix', {'operation_id': 'quiet-preference', 'action': 'set_attention',
            'fields': {'notify': False}})
        await self.deliver(message(933, '/pausa'))
        self.assertEqual([], self.service.query())
        self.assertTrue(self.service.review_state()['attention']['paused'])
        await self.deliver(message(934, 'guardar durante pausa'))
        self.restart()
        self.assertTrue(self.service.review_state()['attention']['paused'])
        await self.deliver(message(935, '/reanudar'))
        attention = self.service.review_state()['attention']
        self.assertFalse(attention['paused'])
        self.assertFalse(attention['notify'])
        self.assertEqual(['guardar durante pausa'], [i['text'] for i in self.service.query()])

    async def test_forwarded_pause_is_source_material_and_not_attention_authority(self):
        await self.deliver(message(936, '/pausa', forward_origin={'type': 'hidden_user'}))
        self.assertFalse(self.service.review_state()['attention']['paused'])
        self.assertEqual('/pausa', self.service.query()[0]['text'])

    async def test_resume_button_survives_restart_without_creating_an_item(self):
        await self.deliver(message(937, '/pausa'))
        self.restart()
        await self.click_named('Reanudar avisos', 938)
        self.assertFalse(self.service.review_state()['attention']['paused'])
        self.assertFalse(self.service.query())

    async def test_result_read_stops_when_source_changes_during_multipart_return(self):
        source = self.service.capture('felix', 'multipart-return-source', 'dato original')['item']
        item = self.prepared_item('a' * 3000 + 'FIN-SUPERADO', source)
        await self.adapter.show_item(item)
        def correct(payload):
            if '[1/' in payload['text']:
                self.service.execute('felix', {'operation_id': 'mid-return-correction', 'action': 'edit',
                    'item_id': source['id'], 'expected_version': source['version'],
                    'fields': {'text': 'dato corregido'}})
        self.http.on_send = correct
        await self.click_named('Ver resultado', 939)
        self.assertFalse(any('FIN-SUPERADO' in m['text'] for m in self.http.sent))
        self.assertTrue(any('revisión' in m['text'] for m in self.http.sent))

    async def test_result_read_preserves_owner_transport_boundary(self):
        item = self.prepared_item('SOLO-PROPIETARIO')
        self.adapter = TelegramAdapter(self.service, self.client,
            TelegramConfig('synthetic-bot', 7, 9, 'gtd-felix'))
        await self.adapter.show_item(item)
        await self.click_named('Ver resultado', 940)
        self.assertFalse(any('SOLO-PROPIETARIO' in m['text'] for m in self.http.sent))

    async def test_notification_delivers_material_and_survives_restart_without_duplicate(self):
        item = self.service.capture('felix', 'capture-return', 'Preparar nota')['item']
        result = self.service.execute('gtd-felix', {'operation_id': 'material-return', 'action': 'put_material',
            'item_id': item['id'], 'expected_version': item['version'], 'fields': {'content': 'Contenido utilizable íntegro'}})
        self.assertEqual('applied', result['status'])
        item = result['item']
        self.notification(item)
        await self.adapter.process_pending()
        self.assertFalse(self.http.sent)
        await self.deliver(message(900, '/preparado'))
        self.assertTrue(any('Contenido utilizable íntegro' in m['text'] for m in self.http.sent))
        count = len(self.http.sent)
        self.restart()
        await self.adapter.process_pending()
        self.assertEqual(count, len(self.http.sent))
        self.assertFalse(self.service.pending_events('gtd-notification', 'local'))

    def prepared_item(self, content='material legible', source=None):
        item = self.service.capture('felix', 'prepared-' + str(len(self.service.query())), 'Nota')['item']
        fields = {'content': content}
        if source:
            fields['source_versions'] = {source['id']: len(source['source_revisions'])}
        return self.service.execute('gtd-felix', {'operation_id': 'put-' + item['id'], 'action': 'put_material',
            'item_id': item['id'], 'expected_version': item['version'], 'fields': fields})['item']

    async def test_notification_paused_attention_allows_requested_delivery_and_capture(self):
        item = self.prepared_item()
        self.notification(item)
        self.service.execute('felix', {'operation_id': 'pause-notices', 'action': 'set_attention',
            'fields': {'paused': True, 'notify': False}})
        await self.adapter.process_pending()
        self.assertFalse(self.http.sent)
        await self.deliver(message(901, '/preparado'), message(902, 'captura durante pausa'))
        self.assertTrue(any('material legible' in m['text'] for m in self.http.sent))
        self.assertTrue(any(i['text'] == 'captura durante pausa' for i in self.service.query()))
        self.assertTrue(self.service.review_state()['attention']['paused'])

    async def test_notification_uncertain_response_restart_never_repeats_material(self):
        self.notification(self.prepared_item('ENVIO-UNICO'))
        original = self.client.call
        async def lost(method, payload):
            result = await original(method, payload)
            if method == 'sendMessage' and 'ENVIO-UNICO' in payload['text']:
                raise TimeoutError('synthetic response lost')
            return result
        self.client.call = lost
        await self.deliver(message(903, '/preparado'))
        self.restart()
        self.client.call = original
        await self.deliver(message(904, '/preparado'))
        self.assertEqual(1, sum('ENVIO-UNICO' in m['text'] for m in self.http.sent))
        event = self.service.pending_events('gtd-notification', 'local')[0]
        self.assertEqual('notification_delivery_uncertain', event['error'])

    async def test_notification_receipt_failure_after_send_recovers_without_duplicate(self):
        self.notification(self.prepared_item('RECIBO-RECUPERABLE'))
        receipt = self.adapter._notification_receipt
        self.adapter._notification_receipt = lambda *a, **k: (_ for _ in ()).throw(RuntimeError('synthetic rollback'))
        await self.deliver(message(905, '/preparado'))
        self.assertTrue(self.service.pending_events('gtd-notification', 'local'))
        self.restart()
        await self.deliver(message(906, '/preparado'))
        self.assertEqual(1, sum('RECIBO-RECUPERABLE' in m['text'] for m in self.http.sent))
        self.assertFalse(self.service.pending_events('gtd-notification', 'local'))

    async def test_notification_old_version_and_invalid_dependency_are_suppressed(self):
        source = self.service.capture('felix', 'source-for-material', 'dato original')['item']
        item = self.prepared_item('MATERIAL-OBSOLETO', source)
        self.notification(item)
        self.service.execute('felix', {'operation_id': 'correct-source', 'action': 'edit',
            'item_id': source['id'], 'expected_version': source['version'], 'fields': {'text': 'dato corregido'}})
        await self.deliver(message(907, '/preparado'))
        self.assertFalse(any('MATERIAL-OBSOLETO' in m['text'] for m in self.http.sent))
        self.assertFalse(self.service.pending_events('gtd-notification', 'local'))
        other = self.prepared_item('VERSION-ANTIGUA')
        self.notification(other, 'old-version')
        self.service.execute('felix', {'operation_id': 'edit-after-notification', 'action': 'edit',
            'item_id': other['id'], 'expected_version': other['version'], 'fields': {'title': 'Otra versión'}})
        await self.deliver(message(908, '/preparado'))
        self.assertFalse(any('VERSION-ANTIGUA' in m['text'] for m in self.http.sent))

    async def test_notification_chunks_are_complete_and_oversized_stays_pending(self):
        content = '😀texto' * 1000
        self.notification(self.prepared_item(content))
        await self.deliver(message(909, '/preparado'))
        combined = ''.join(m['text'].split('] ', 1)[1] for m in self.http.sent)
        self.assertIn(content, combined)
        self.assertTrue(all(len(m['text'].encode('utf-16-le')) // 2 <= 4096 for m in self.http.sent))
        self.notification(self.prepared_item('x' * 65537), 'too-large')
        await self.deliver(message(910, '/preparado'))
        event = self.service.pending_events('gtd-notification', 'local')[0]
        self.assertEqual('notification_transport_limit', event['error'])

    async def test_notification_correction_between_chunks_stops_remaining_delivery(self):
        item = self.prepared_item('a' * 5000 + 'NO-ENVIAR-FINAL')
        self.notification(item)
        def correct(payload):
            self.http.on_send = None
            self.service.execute('felix', {'operation_id': 'mid-delivery-edit', 'action': 'edit',
                'item_id': item['id'], 'expected_version': item['version'], 'fields': {'text': 'corrección nueva'}})
        self.http.on_send = correct
        await self.deliver(message(911, '/preparado'))
        self.assertFalse(any('NO-ENVIAR-FINAL' in m['text'] for m in self.http.sent))
        self.assertFalse(self.service.pending_events('gtd-notification', 'local'))

    async def test_notification_binary_and_corrupt_original_remain_pending(self):
        item = self.prepared_item('texto con tipo binario')
        # Create the binary-labelled material through the public domain command.
        item = self.service.execute('gtd-felix', {'operation_id': 'binary-material', 'action': 'put_material',
            'item_id': item['id'], 'expected_version': item['version'],
            'fields': {'content': 'binary-placeholder', 'mime_type': 'application/octet-stream'}})['item']
        self.notification(item)
        await self.deliver(message(912, '/preparado'))
        self.assertEqual('notification_text_transport_required', self.service.pending_events('gtd-notification', 'local')[0]['error'])
        other = self.prepared_item('CONTENIDO-NO-CORRUPTO')
        self.notification(other, 'corrupt-original')
        path = self.service.store.root / other['materials'][0]['original']['path']
        path.write_bytes(b'X' * path.stat().st_size)
        await self.deliver(message(913, '/preparado'))
        self.assertFalse(any('CONTENIDO-NO-CORRUPTO' in m['text'] for m in self.http.sent))
        self.assertIn('notification_original_unavailable', {e['error'] for e in self.service.pending_events('gtd-notification', 'local')})

    async def test_ten_uncertain_returns_do_not_hide_new_material_after_restart(self):
        for i in range(10):
            self.notification(self.prepared_item('INCIERTO-' + str(i)), 'uncertain-' + str(i))
        original = self.client.call
        async def lost(method, payload):
            result = await original(method, payload)
            if method == 'sendMessage' and 'INCIERTO-' in payload['text']:
                raise TimeoutError('synthetic response lost')
            return result
        self.client.call = lost
        await self.deliver(message(920, '/preparado'))
        self.assertEqual(10, sum('INCIERTO-' in m['text'] for m in self.http.sent))
        self.restart()
        self.client.call = original
        self.notification(self.prepared_item('NUEVO-ACCESIBLE'), 'new-after-uncertain')
        await self.deliver(message(921, '/preparado'))
        self.assertTrue(any('NUEVO-ACCESIBLE' in m['text'] for m in self.http.sent))
        self.assertEqual(10, sum('INCIERTO-' in m['text'] for m in self.http.sent))
        pending = self.service.pending_events('gtd-notification', 'local')
        self.assertEqual(10, len(pending))
        self.assertTrue(all(e['error'] == 'notification_delivery_uncertain' for e in pending))

    async def test_ten_oversized_returns_do_not_hide_new_material(self):
        for i in range(10):
            self.notification(self.prepared_item('x' * 65537), 'oversized-' + str(i))
        await self.deliver(message(922, '/preparado'))
        self.restart()
        self.notification(self.prepared_item('NUEVO-TRAS-LIMITE'), 'new-after-limit')
        await self.deliver(message(923, '/preparado'))
        self.assertTrue(any('NUEVO-TRAS-LIMITE' in m['text'] for m in self.http.sent))
        self.assertEqual(10, len(self.service.pending_events('gtd-notification', 'local')))
        self.assertTrue(any('10' in m['text'] and 'transporte' in m['text'] for m in self.http.sent))

    async def deliver(self, *updates):
        self.http.updates.extend(updates)
        await self.adapter.poll_once()
        await self.adapter.process_pending()

    def restart(self):
        self.service.close()
        self.service = GTDService(Path(self.temp.name))
        self.adapter = TelegramAdapter(self.service, self.client, self.config)

    async def test_lost_send_response_restart_does_not_repeat_and_controls_continue(self):
        original = self.http.request
        def lost(method, url, **kwargs):
            response = original(method, url, **kwargs)
            if url.endswith('/sendMessage'):
                class Lost(Response):
                    async def __aenter__(self):
                        raise TimeoutError('synthetic_response_lost')
                return Lost()
            return response
        self.http.request = lost
        await self.deliver(message(900, 'Saved before lost acknowledgement'))
        self.assertEqual(1, len(self.http.sent))
        self.http.request = original
        self.restart()
        await self.adapter.process_pending()
        self.assertEqual(1, len(self.http.sent))
        item = self.service.query()[0]
        await self.deliver(message(901, f"/editar {item['id']}@{item['version']} Corrected"))
        self.assertEqual('Corrected', self.service.get_item(item['id'])['title'])
        self.assertEqual(2, len(self.http.sent))

    async def test_crash_after_dispatch_marker_replays_without_second_send(self):
        original = self.client.call
        async def crash(method, payload):
            result = await original(method, payload)
            if method == 'sendMessage':
                raise asyncio.CancelledError()
            return result
        self.client.call = crash
        self.http.updates = [message(902, 'Crash window')]
        await self.adapter.poll_once()
        with self.assertRaises(asyncio.CancelledError):
            await self.adapter.process_pending()
        self.assertEqual(1, len(self.http.sent))
        self.assertEqual(1, len(self.service.pending_events('telegram', self.config.account)))
        self.client.call = original
        self.restart()
        await self.adapter.process_pending()
        self.assertEqual(1, len(self.http.sent))
        self.assertEqual([], self.service.pending_events('telegram', self.config.account))

    async def test_confirmed_force_reply_response_survives_event_replay(self):
        await self.deliver(message(903, 'Prompt target'))
        item = self.service.query()[0]
        await self.adapter.show_item(item, more=True)
        button = self.http.sent[-1]['reply_markup']['inline_keyboard'][0][0]
        update = {'update_id': 904, 'callback_query': {'id': 'prompt-replay',
            'from': {'id': 7}, 'message': {'message_id': 12, 'chat': {'id': 9}}, 'data': button['callback_data']}}
        self.http.updates.append(update)
        await self.adapter.poll_once()
        original = self.service.mark_event
        failed = False
        def fail_final(key, status, error=None):
            nonlocal failed
            if status == 'applied' and not failed:
                failed = True
                raise RuntimeError('crash_after_prompt')
            return original(key, status, error)
        self.service.mark_event = fail_final
        await self.adapter.process_pending()
        sent_count = len(self.http.sent)
        self.restart()
        await self.adapter.process_pending()
        self.assertEqual(sent_count, len(self.http.sent))
        self.assertEqual(1, len(self.service.pending_events('telegram-prompt', self.config.account)))

    async def test_persist_before_offset_and_restart_before_processing(self):
        self.http.updates = [message(1), message(2)]
        original = self.service.set_cursor
        observed = []
        def set_cursor(provider, account, cursor):
            pending = self.service.pending_events(provider, account)
            self.assertTrue(any(e['payload']['update_id'] == int(cursor) - 1 for e in pending))
            observed.append(cursor)
            return original(provider, account, cursor)
        self.service.set_cursor = set_cursor
        await self.adapter.poll_once()
        self.assertEqual(['2', '3'], observed)
        self.assertEqual([], self.service.query())
        self.restart()
        await self.adapter.process_pending()
        self.assertEqual(2, len(self.service.query()))
        await self.adapter.poll_once()
        self.assertEqual(3, self.http.calls[-1][1]['offset'])

    async def test_failed_ingest_never_advances_past_unsaved_update(self):
        self.http.updates = [message(1), message(2)]
        original = self.service.ingest_event
        def fail_second(event):
            if event['external_id'] == '2':
                raise OSError('disk full')
            return original(event)
        self.service.ingest_event = fail_second
        with self.assertRaises(OSError):
            await self.adapter.poll_once()
        self.assertEqual('2', self.service.get_cursor('telegram', self.config.account))
        self.restart()
        await self.deliver()
        self.assertEqual(2, len(self.service.query()))

    async def test_voice_original_before_saved_and_pending_clarification(self):
        def assert_saved(payload):
            if 'Guardé' in payload['text']:
                item = self.service.query()[0]
                self.assertEqual(b'original audio', (Path(self.temp.name) / item['original']['path']).read_bytes())
        self.http.on_send = assert_saved
        await self.deliver(message(1, '', voice={'file_id': 'voice-1', 'mime_type': 'audio/ogg'}))
        self.assertIn('transcripción pendiente', self.http.sent[-1]['text'])
        pending = self.service.pending_events('gtd-clarification', self.config.account)
        self.assertEqual(1, len(pending))
        self.assertEqual('capture', self.service.query()[0]['kind'])

    async def test_media_failure_does_not_block_captures_and_retries_same_identity(self):
        self.http.file_failure = True
        await self.deliver(message(1, '', document={'file_id': 'doc', 'file_name': 'note.txt'}), message(2, 'idea'))
        self.assertEqual(['idea'], [item['title'] for item in self.service.query()])
        self.assertEqual(1, len(self.service.pending_events('telegram', self.config.account)))
        self.restart()
        self.http.file_failure = False
        await self.adapter.process_pending()
        self.assertEqual(2, len(self.service.query()))
        await self.adapter.process_pending()
        self.assertEqual(2, len(self.service.query()))

    async def test_slow_media_does_not_block_new_poll_or_text_worker(self):
        self.http.download_gate = asyncio.Event()
        await self.deliver(message(1, 'first'))
        self.http.updates.append(message(2, '', voice={'file_id': 'voice'}))
        await self.adapter.poll_once()
        self.adapter.schedule_pending()
        await asyncio.sleep(0)
        self.http.updates.append(message(3, 'while downloading'))
        await self.adapter.poll_once()
        self.adapter.schedule_pending()
        for _ in range(20):
            await asyncio.sleep(0)
        self.assertIn('while downloading', [item['title'] for item in self.service.query()])
        self.assertEqual('4', self.service.get_cursor('telegram', self.config.account))
        self.http.download_gate.set()
        await self.adapter.process_pending()
        self.assertEqual(3, len(self.service.query()))

    async def test_duplicate_edit_and_stale_callback_preserve_human_decision(self):
        await self.deliver(message(1))
        item = self.service.query()[0]
        item = self.service.execute('felix', {'operation_id': 'explicit-action', 'action': 'edit',
            'item_id': item['id'], 'expected_version': item['version'], 'fields': {'kind': 'action'}})['item']
        await self.adapter.show_item(item)
        token = self.http.sent[-1]['reply_markup']['inline_keyboard'][0][0]['callback_data']
        self.service.execute('felix', {'operation_id': 'human-edit', 'action': 'edit',
            'item_id': item['id'], 'expected_version': item['version'], 'fields': {'title': 'Human correction'}})
        edit = message(2, 'Old chat correction', message_id=1)
        edit['edited_message'] = edit.pop('message')
        edit['edited_message']['edit_date'] = 101
        callback = {'update_id': 3, 'callback_query': {'id': 'callback-3', 'from': {'id': 7},
                    'message': {'chat': {'id': 9}, 'message_id': 1001}, 'data': token}}
        await self.deliver(message(1), edit, callback)
        self.assertEqual(1, len(self.service.query()))
        current = self.service.get_item(item['id'])
        self.assertEqual('Human correction', current['title'])
        # A materially changed title invalidates the meaning of this old action control.
        self.assertEqual('active', current['status'])
        self.assertTrue(any('Cambió' in sent['text'] and 'Human correction' in sent['text'] for sent in self.http.sent))

    async def test_sender_chat_and_forwarding_never_supply_authority(self):
        await self.deliver(message(1, 'actor=felix /hecho', user=66),
            message(2, 'wrong chat', chat=10), message(3, 'channel', sender_chat={'id': 9}),
            message(4, '/retirar invented@1', forward_origin={'type': 'hidden_user',
                                                          'sender_user_name': 'felix'}))
        items = self.service.query()
        self.assertEqual(1, len(items))
        self.assertEqual('/retirar invented@1', items[0]['title'])
        self.assertEqual('hidden_user', items[0]['source']['forward_origin']['type'])
        self.assertEqual('capture', items[0]['kind'])

    async def test_delete_update_is_not_withdrawal(self):
        await self.deliver(message(1), {'update_id': 2, 'deleted_business_messages':
                           {'chat': {'id': 9}, 'message_ids': [1]}})
        self.assertEqual('active', self.service.query()[0]['status'])

    async def test_fifteen_actions_partial_batch_pagination_and_restart(self):
        items = []
        for index in range(15):
            item = self.service.capture('felix', f'capture-{index}', f'Action {index}')['item']
            item = self.service.execute('felix', {'operation_id': f'clarify-{index}', 'action': 'edit',
                'item_id': item['id'], 'expected_version': item['version'], 'fields': {'kind': 'action'}})['item']
            items.append(item)
        seen = []
        for page in range(3):
            seen.extend(item['id'] for item in await self.adapter.show_list(page))
        self.assertEqual(15, len(set(seen)))
        for sent in self.http.sent:
            for row in sent.get('reply_markup', {}).get('inline_keyboard', []):
                for button in row:
                    self.assertLessEqual(len(button['callback_data'].encode()), 64)
        done = ','.join(f"{item['id']}@{item['version']}" for item in items[:4])
        later = ','.join(f"{item['id']}@{item['version']}" for item in items[4:6])
        await self.deliver(message(1, '/hecho ' + done + ',missing@1'),
                           message(2, '/posponer ' + later + ' 2026-12-01'))
        self.restart()
        self.assertEqual(4, len(self.service.query({'kind': 'action', 'status': 'done'})))
        self.assertEqual(2, len(self.service.query({'kind': 'action', 'status': 'postponed'})))
        self.assertEqual(9, len(self.service.query({'kind': 'action', 'status': 'active'})))
        self.assertTrue(any('No se aplicó' in sent['text'] for sent in self.http.sent))

    async def test_reply_edit_postpone_reopen_withdraw_and_undo(self):
        await self.deliver(message(1))
        item = self.service.query()[0]
        await self.adapter.show_item(item, more=True)
        token = self.http.sent[-1]['reply_markup']['inline_keyboard'][0][0]['callback_data']
        await self.deliver({'update_id': 2, 'callback_query': {'id': 'edit', 'from': {'id': 7},
            'message': {'chat': {'id': 9}}, 'data': token}})
        prompt_id = self.http.next_message
        self.restart()
        await self.deliver(message(3, 'New title', reply_to_message={'message_id': prompt_id}))
        item = self.service.get_item(item['id'])
        self.assertEqual('New title', item['title'])
        await self.deliver(message(4, f"/retirar {item['id']}@{item['version']}"))
        item = self.service.get_item(item['id'])
        self.assertEqual('withdrawn', item['status'])
        undo = next(button['callback_data'] for row in self.http.sent[-1]['reply_markup']['inline_keyboard'] for button in row if button['text'] == 'Deshacer')
        await self.deliver({'update_id': 5, 'callback_query': {'id': 'undo', 'from': {'id': 7},
            'message': {'chat': {'id': 9}}, 'data': undo}})
        self.assertEqual('active', self.service.get_item(item['id'])['status'])
        current = self.service.get_item(item['id'])
        await self.deliver(message(6, f"/hecho {item['id']}@{current['version']}"))
        current = self.service.get_item(item['id'])
        await self.deliver(message(7, f"/reabrir {item['id']}@{current['version']}"))
        self.assertEqual('active', self.service.get_item(item['id'])['status'])

    async def test_http_errors_never_expose_token_and_post_is_not_retried(self):
        class BrokenHTTP:
            calls = 0
            def request(self, *args, **kwargs):
                self.calls += 1
                raise RuntimeError('https://api.telegram.org/botTOP-SECRET/sendMessage')
        http = BrokenHTTP()
        client = AiohttpTelegramClient('TOP-SECRET', http)
        with self.assertRaises(TelegramError) as raised:
            await client.call('sendMessage', {'text': 'private'})
        self.assertNotIn('TOP-SECRET', str(raised.exception))
        self.assertIsNone(raised.exception.__cause__)
        self.assertTrue(raised.exception.__suppress_context__)
        self.assertEqual(1, http.calls)

    async def test_document_replacement_preserves_identity_and_originals(self):
        await self.deliver(message(1, 'Original caption', document={'file_id': 'doc1', 'file_name': 'note.txt'}))
        item = self.service.query()[0]
        original_path = Path(self.temp.name) / item['original']['path']
        self.http.file_data = b'replacement document'
        edit = message(2, 'Edited caption', message_id=1,
                       document={'file_id': 'doc2', 'file_name': 'replacement.txt'}, edit_date=101)
        edit['edited_message'] = edit.pop('message')
        await self.deliver(edit)
        self.assertEqual(1, len(self.service.query()))
        current = self.service.get_item(item['id'])
        self.assertEqual('Original caption', current['title'])
        self.assertEqual(b'original audio', original_path.read_bytes())
        self.assertEqual(2, len(current['source_revisions']))
        self.assertEqual('101', current['source']['revision'])
        self.assertEqual(b'replacement document', (Path(self.temp.name) / current['source_revisions'][-1]['original']['path']).read_bytes())
        originals = [p.read_bytes() for p in (Path(self.temp.name) / 'originals').rglob('*') if p.is_file()]
        self.assertIn(b'replacement document', originals)
        self.restart()
        self.assertEqual(item['id'], self.service.query()[0]['id'])
        self.assertTrue(any('edición de la fuente' in sent['text'] for sent in self.http.sent))

    async def test_callback_allows_compatible_notes_change_with_original_version(self):
        await self.deliver(message(1))
        item = self.service.query()[0]
        item = self.service.execute('felix', {'operation_id': 'explicit-action', 'action': 'edit',
            'item_id': item['id'], 'expected_version': item['version'], 'fields': {'kind': 'action'}})['item']
        await self.adapter.show_item(item)
        token = self.http.sent[-1]['reply_markup']['inline_keyboard'][0][0]['callback_data']
        self.service.execute('felix', {'operation_id': 'notes-edit', 'action': 'edit',
            'item_id': item['id'], 'expected_version': item['version'], 'fields': {'notes': 'More context'}})
        await self.deliver({'update_id': 2, 'callback_query': {'id': 'done-compatible', 'from': {'id': 7},
            'message': {'chat': {'id': 9}}, 'data': token}})
        current = self.service.get_item(item['id'])
        self.assertEqual('done', current['status'])
        self.assertEqual('More context', current['notes'])

    async def test_uncertain_capture_remains_pending_until_storage_recovers(self):
        self.service.capture = lambda *args, **kwargs: {'status': 'uncertain', 'operation_id': args[1]}
        await self.deliver(message(1))
        self.assertEqual(1, len(self.service.pending_events('telegram', self.config.account)))
        self.assertFalse(any('Guardado' in sent['text'] for sent in self.http.sent))
        self.restart()
        await self.adapter.process_pending()
        self.assertEqual(1, len(self.service.query()))

    async def test_rejected_ingest_does_not_advance_offset(self):
        self.http.updates = [message(1)]
        self.service.ingest_event = lambda event: {'status': 'rejected', 'event_key': None}
        with self.assertRaises(TelegramError):
            await self.adapter.poll_once()
        self.assertIsNone(self.service.get_cursor('telegram', self.config.account))

    async def test_crash_after_capture_recovers_clarification_without_duplicate(self):
        original = self.adapter._event
        def crash(provider, external_id, payload, revision='1'):
            if provider == 'gtd-clarification':
                raise OSError('simulated persistence failure')
            return original(provider, external_id, payload, revision)
        self.adapter._event = crash
        await self.deliver(message(1, 'Could this be an idea?'))
        self.assertEqual(1, len(self.service.query()))
        self.assertFalse(any('Guardado' in sent['text'] for sent in self.http.sent))
        self.restart()
        await self.adapter.process_pending()
        self.assertEqual(1, len(self.service.query()))
        self.assertEqual(1, len(self.service.pending_events('gtd-clarification', self.config.account)))
        self.assertEqual('capture', self.service.query()[0]['kind'])

    async def test_replayed_callback_and_bounded_invalid_callback(self):
        await self.deliver(message(1))
        item = self.service.query()[0]
        item = self.service.execute('felix', {'operation_id': 'explicit-action', 'action': 'edit',
            'item_id': item['id'], 'expected_version': item['version'], 'fields': {'kind': 'action'}})['item']
        await self.adapter.show_item(item)
        token = self.http.sent[-1]['reply_markup']['inline_keyboard'][0][0]['callback_data']
        callback = {'update_id': 2, 'callback_query': {'id': 'same-click', 'from': {'id': 7},
                    'message': {'chat': {'id': 9}}, 'data': token}}
        await self.deliver(callback)
        version = self.service.get_item(item['id'])['version']
        # Telegram can redeliver callback identity inside a fresh delivery envelope.
        callback['update_id'] = 3
        await self.deliver(callback)
        self.assertEqual(version, self.service.get_item(item['id'])['version'])
        callback['update_id'] = 4
        callback['callback_query']['data'] = 'g1:' + 'x' * 1000
        await self.deliver(callback)
        self.assertEqual(version, self.service.get_item(item['id'])['version'])

    async def test_ui_selection_across_pages_survives_restart_four_done_two_postponed(self):
        for index in range(15):
            item = self.service.capture('felix', f'ui-capture-{index}', f'Action {index}')['item']
            self.service.execute('felix', {'operation_id': f'ui-action-{index}', 'action': 'edit',
                'item_id': item['id'], 'expected_version': item['version'], 'fields': {'kind': 'action'}})
        counter = 100
        async def click(label=None, checkbox=False):
            nonlocal counter
            buttons = [button for row in self.http.sent[-1]['reply_markup']['inline_keyboard'] for button in row]
            button = next(button for button in buttons if button['text'].startswith('☐ ') if checkbox) if checkbox else next(button for button in buttons if button['text'] == label)
            counter += 1
            update = {'update_id': counter, 'callback_query': {'id': f'click-{counter}', 'from': {'id': 7},
                'message': {'chat': {'id': 9}}, 'data': button['callback_data']}}
            await self.deliver(update)
        await self.adapter.show_list()
        await click('Seleccionar varios')
        await click(checkbox=True)
        await click(checkbox=True)
        await click('Siguiente')
        await click(checkbox=True)
        await click(checkbox=True)
        self.assertIn('4/15 seleccionados', self.http.sent[-1]['text'])
        self.restart()
        await click('Hecho')
        self.assertIn('4/4 aplicados', self.http.sent[-1]['text'])
        await self.adapter.show_list(filters={'kind': 'action', 'status': 'active'})
        await click('Seleccionar varios')
        await click(checkbox=True)
        await click(checkbox=True)
        await click('Posponer')
        prompt_id = self.http.next_message
        self.restart()
        counter += 1
        await self.deliver(message(counter, '2026-12-01', reply_to_message={'message_id': prompt_id}))
        self.restart()
        self.assertEqual(4, len(self.service.query({'status': 'done'})))
        self.assertEqual(2, len(self.service.query({'status': 'postponed'})))
        self.assertEqual(9, len(self.service.query({'status': 'active'})))
        active = self.service.query({'status': 'active'})[0]
        await self.adapter.show_item(active)
        buttons = [button for row in self.http.sent[-1]['reply_markup']['inline_keyboard'] for button in row]
        self.assertLessEqual(len(buttons), 3)
        self.assertNotIn(active['id'], self.http.sent[-1]['text'])

    async def test_restored_store_receives_and_captures_without_dispatch_or_sends(self):
        await self.deliver(message(1))
        item = self.service.query()[0]
        item = self.service.execute('felix', {'operation_id': 'explicit-action', 'action': 'edit',
            'item_id': item['id'], 'expected_version': item['version'], 'fields': {'kind': 'action'}})['item']
        await self.adapter.show_item(item)
        token = self.http.sent[-1]['reply_markup']['inline_keyboard'][0][0]['callback_data']
        self.http.updates.extend([message(2, 'pending capture'), message(3, f"/hecho {item['id']}@{item['version']}"),
            {'update_id': 4, 'callback_query': {'id': 'restored-click', 'from': {'id': 7},
             'message': {'chat': {'id': 9}}, 'data': token}}])
        await self.adapter.poll_once()
        archive = Path(self.temp.name) / 'backup.zip'
        self.service.export(archive)
        self.service.close()
        self.service = GTDService.restore(archive, Path(self.temp.name) / 'restored')
        self.adapter = TelegramAdapter(self.service, self.client, self.config)
        self.http.calls.clear()
        self.http.sent.clear()
        self.assertTrue(self.service.recovery_required)
        await self.adapter.process_pending()
        self.http.updates.append(message(5, 'capture after restore'))
        await self.adapter.poll_once()
        await self.adapter.process_pending()
        self.assertEqual(3, len(self.service.query()))
        self.assertEqual('active', self.service.get_item(item['id'])['status'])
        self.assertEqual([], self.http.sent)
        self.assertFalse(any(name in {'sendMessage', 'answerCallbackQuery'} for name, _ in self.http.calls))
        self.assertEqual('6', self.service.get_cursor('telegram', self.config.account))
        with self.assertRaises(TelegramError):
            await self.adapter.show_list()

    async def test_safe_http_read_retries_are_bounded(self):
        class UnavailableHTTP:
            calls = 0
            def request(self, *args, **kwargs):
                self.calls += 1
                return Response(status=503)
        http = UnavailableHTTP()
        client = AiohttpTelegramClient('synthetic', http, attempts=2)
        with self.assertRaises(TelegramError):
            await client.call('getUpdates', {'timeout': 1})
        self.assertEqual(2, http.calls)

    async def test_file_limit_and_config_validation(self):
        client = AiohttpTelegramClient('synthetic', self.http, attempts=1, max_file_bytes=2)
        with self.assertRaises(TelegramError):
            await client.download('file')
        with self.assertRaises(ValueError):
            TelegramConfig('', 7, 9, 'felix')
