"""Explicit owner pause and return through opaque Telegram callbacks."""
import unittest
from test_telegram import TelegramTests as _Fixture


class PauseUITests(unittest.IsolatedAsyncioTestCase):
    setUp = _Fixture.setUp
    tearDown = _Fixture.tearDown
    deliver = _Fixture.deliver
    restart = _Fixture.restart
    prepared_item = _Fixture.prepared_item
    click_named = _Fixture.click_named

    def button(self, label):
        return next(b for row in self.http.sent[-1]['reply_markup']['inline_keyboard']
                    for b in row if b['text'] == label)['callback_data']

    async def callback(self, token, update_id, user=7, chat=9, identity=None):
        await self.deliver({'update_id': update_id, 'callback_query': {
            'id': identity or f'pause-ui-{update_id}', 'from': {'id': user},
            'message': {'chat': {'id': chat}}, 'data': token}})

    async def test_pause_read_restart_and_explicit_resume(self):
        item = self.prepared_item('BORRADOR-CONSERVADO')
        await self.adapter.show_item(item)
        pause = self.button('Pausar asunto')
        self.assertRegex(pause, r'^g1:[0-9a-f]{32}$')
        for update_id, user, chat in ((2, 66, 9), (3, 7, 10)):
            await self.callback(pause, update_id, user, chat)
            self.assertEqual(item, self.service.get_item(item['id']))
        await self.callback(pause, 4, identity='pause-once')
        paused = self.service.get_item(item['id'])
        self.assertEqual(paused['status'], 'paused')
        self.assertIn('En pausa', self.http.sent[-1]['text'])
        labels = [b['text'] for row in self.http.sent[-1]['reply_markup']['inline_keyboard'] for b in row]
        self.assertIn('Retomar', labels)
        self.assertFalse({'Hecho', 'Posponer', 'Pausar asunto'} & set(labels))
        await self.callback(pause, 5, identity='pause-once')
        self.assertEqual(paused, self.service.get_item(item['id']))
        self.restart()
        await self.adapter.show_item(item)
        resume = self.button('Retomar')
        await self.click_named('Ver resultado', 6)
        self.assertIn('BORRADOR-CONSERVADO', self.http.sent[-1]['text'])
        material = self.service.materials(item['id'])[-1]
        self.assertEqual('Resultado disponible\n' + item['title'] + '\n\n' +
                         material['title'] + '\nBORRADOR-CONSERVADO', self.http.sent[-1]['text'])
        for internal in (item['id'], material['id'], ' · versión ',
                         ' v' + str(material['version']), '[1/1]'):
            self.assertNotIn(internal, self.http.sent[-1]['text'])
        self.assertEqual(paused, self.service.get_item(item['id']))
        await self.callback(resume, 7, user=66)
        self.assertEqual(paused, self.service.get_item(item['id']))
        await self.callback(resume, 8, identity='resume-once')
        reopened = self.service.get_item(item['id'])
        self.assertEqual(reopened['status'], 'active')
        await self.callback(resume, 9, identity='resume-once')
        self.assertEqual(reopened, self.service.get_item(item['id']))


del _Fixture
