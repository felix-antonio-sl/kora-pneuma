"""E47: honest return for a guard-stopped attempt without domain progress.

Real history (520f13f2/ca99acbc/b025d38f) shows terminal-discarded runs with
zero gtd-notification events: the user got silence. The worker now emits one
'interrupted' notice for guard-initiated stops on active items; user-requested
stops and paused items stay silent. Fake clock/native/Telegram transport, real
worker/state/outbox/renderer. No inference, no network.
"""
import asyncio
import dataclasses
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from aiohttp import web
from gtd_felix.application import create_app
from gtd_felix.control import ExecutionControl
from gtd_felix.mcp import MCPClient
from gtd_felix.orchestration import OrchestrationWorker
from gtd_felix.service import GTDService
import test_orchestration as orch_fx
import test_telegram as tg_fx

BUDGET = dict(period_start=datetime.now(timezone.utc).isoformat(), period_seconds=3600,
              max_cost_usd=20, max_runtime_seconds=2000, recovery_cost_usd=2,
              recovery_runtime_seconds=100, max_job_runtime_seconds=500,
              max_retries=0, max_descendants=2)


def prepare_item(service):
    item = service.capture('felix', 'cap-int', 'Mapa de responsabilidades TM')['item']
    receipt = service.execute('gtd-felix', {'operation_id': 'int-clarify', 'action': 'clarify',
        'item_id': item['id'], 'expected_version': item['version'],
        'fields': {'kind': 'action', 'commitment': 'committed', 'capability': 'prepare_private',
                   'completion_criteria': 'Minuta parcial verificable',
                   'intent_basis': {'source_item_id': item['id'], 'quote': item['text']}}})
    assert receipt['status'] == 'applied', receipt
    item = receipt['item']
    mandate = service.execute('felix', {'operation_id': 'int-mandate', 'action': 'grant_mandate',
        'item_id': item['id'], 'expected_version': item['version'],
        'fields': {'scope_item_id': item['id'], 'capabilities': ['prepare_private'],
                   'actors': ['gtd-felix'], 'completion_criteria': 'Minuta parcial'}})
    assert mandate['status'] == 'applied', mandate
    return mandate['item'], mandate['mandate']['id']


def open_job(service, control, item, mandate_id, bot_id='int-bot', operation='int-reserve'):
    control.register_bot('felix', 'int-botreg', dict(id=bot_id, state='available',
        source_urn='urn:test:int', host='synthetic', profile='fixture',
        capabilities=['prepare_private'], mandate_id=mandate_id,
        item_id=item['id'], probe_evidence='fixture://int'))
    job = control.reserve('gtd-felix', operation, dict(
        item_id=item['id'], expected_version=service.get_item(item['id'])['version'],
        mandate_id=mandate_id, capability='prepare_private', bot_id=bot_id,
        purpose='Preparacion acotada', scope='s', max_cost_usd=4, max_runtime_seconds=200,
        max_retries=0, max_descendants=0))
    assert job['status'] == 'reserved', job
    control.record_dispatch(job['job_id'], {'provider': 'fixture', 'host': 'synthetic',
                                            'profile': 'fixture', 'id': job['job_id']})
    return job['job_id']


def observe_terminal_cancelled(control, job_id):
    receipt = control.observe(job_id, {
        'native_identity': {'provider': 'fixture', 'host': 'synthetic', 'profile': 'fixture', 'id': job_id},
        'native_status': 'cancelled', 'terminal': True,
        'cost_usd': None, 'runtime_seconds': 252,
        'evidence_reference': 'fixture://int/' + job_id})
    assert receipt['status'] == 'recorded', receipt
    job = control.get_job(job_id)
    assert job['terminal'] and job['integration'] == 'discarded', job
    return job


class SilentFixture(orch_fx.NativeFixture):
    """Provider silence: submits and polls, never tools, never output."""
    observed_runtime = 9999

    async def submit(self, job_id, prompt, durable=False):
        self.submissions.append({'job_id': job_id, 'prompt': prompt, 'durable': durable})
        self.control.record_dispatch(job_id, self.native(job_id))
        self.runs[job_id] = {'status': 'running'}
        return {'status': 'submitted', 'job_id': job_id, 'native_id': job_id}

    async def poll(self, job_id):
        # Local clock keeps growing while the provider stays silent; the
        # terminal observation preserves the over-limit runtime (E32: 252/240).
        self.polls += 1
        if job_id not in self.runs:
            return {'status': 'uncertain', 'job_id': job_id}
        cancelled = self.runs[job_id]['status'] == 'cancelled'
        observation = {'native_identity': self.native(job_id),
            'native_status': 'cancelled' if cancelled else 'running',
            'terminal': cancelled, 'cost_usd': None, 'runtime_seconds': self.observed_runtime,
            'evidence_reference': 'fixture://int/' + job_id}
        if not self.control.get_job(job_id)['terminal']:
            recorded = self.control.observe(job_id, observation)
            if recorded['status'] != 'recorded':
                raise AssertionError(recorded)
        return {'status': 'observed', 'job_id': job_id, 'terminal': cancelled,
                'native_status': observation['native_status'], 'observation': observation}


class WorkerEmissionTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.service = GTDService(self.root / 'data')
        self.control = ExecutionControl(self.service, dict(BUDGET))
        self.item, self.mandate_id = prepare_item(self.service)
        self.control.register_bot('felix', 'bot', dict(id='principal', state='available',
            source_urn='urn:test:principal', host='synthetic', profile='fixture',
            capabilities=['prepare_private'], item_id=self.item['id'],
            mandate_id=None, probe_evidence='fixture://route'))
        self.config = dict(actor='gtd-felix', principal_bot_id='principal',
            clarification_accounts=['fixture'],
            reservation=dict(max_cost_usd=4, max_runtime_seconds=200, max_retries=0, max_descendants=0),
            poll_seconds=.01, review_interval_seconds=300)
        appconfig = dict(data_dir=str(self.root / 'data'),
            actors={'owner': 'felix', 'principal': 'gtd-felix', 'executors': []},
            api_tokens={'synthetic-owner-token': 'felix', 'synthetic-agent-token': 'gtd-felix'})
        self.runner = web.AppRunner(create_app(self.service, self.control, appconfig), access_log=None)
        await self.runner.setup()
        site = web.TCPSite(self.runner, '127.0.0.1', 0)
        await site.start()
        self.url = 'http://127.0.0.1:' + str(site._server.sockets[0].getsockname()[1])
        self.client = MCPClient(self.url, 'synthetic-agent-token')
        self.native = SilentFixture(self.control, self.client)
        self.native.keep_running = True
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        self.service.ingest_event({'provider': 'gtd-clarification', 'account': 'fixture',
            'external_id': self.item['id'], 'revision': '1',
            'payload': {'item_id': self.item['id'], 'reason': 'clarification_pending'}})

    async def asyncTearDown(self):
        await self.runner.cleanup()
        self.service.close()
        self.temp.cleanup()

    def interrupted(self):
        return [e for e in self.service.pending_events('gtd-notification', 'local')
                if e['payload'].get('kind') == 'interrupted']

    async def test_guard_stop_emits_one_honest_notice(self):
        for _ in range(6):
            await self.worker.tick()
            if self.native.submissions:
                break
        self.assertEqual(1, len(self.native.submissions))
        job_id = self.native.submissions[0]['job_id']
        event = None
        for _ in range(15):
            await self.worker.tick()
            found = self.interrupted()
            if found:
                event = found[0]
                break
        self.assertIsNotNone(event, 'guard-stopped silence produced no notice')
        payload = event['payload']
        self.assertEqual(payload['item_id'], self.item['id'])
        self.assertEqual(payload['version'], self.service.get_item(self.item['id'])['version'])
        self.assertEqual(payload['text'],
                         'No pude completar esta preparación: ' + self.item['title'] + '. '
                         'El asunto conserva su historial; no hay material guardado. '
                         'Puedes ver el asunto, revisarlo cuando quieras o pausarlo.')
        self.assertNotIn(job_id, payload['text'])
        for banned in ('USD', 'segundos', 'Traceback', 'stack'):
            self.assertNotIn(banned, payload['text'])
        job = self.control.get_job(job_id)
        self.assertTrue(job['terminal'])
        self.assertEqual(job['integration'], 'discarded')
        self.assertEqual(self.control.budget()['active'], 0)
        for _ in range(5):
            self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
            await self.worker.tick()
        self.assertEqual(1, len(self.interrupted()))

    async def test_director_probe_p1_human_stop_at_limit_stays_silent(self):
        # Sonda P1 de direccion: STOP humano con tiempo sobre el cupo no avisa.
        for _ in range(6):
            await self.worker.tick()
            if self.native.submissions:
                break
        self.assertEqual(1, len(self.native.submissions))
        self.native.observed_runtime = 252
        job_id = self.native.submissions[0]['job_id']
        stop = self.control.request_stop('felix', 'director-human-stop', job_id)
        self.assertTrue(self.control.get_job(job_id)['stop_requested'], stop)
        self.native.runs[job_id]['status'] = 'cancelled'
        for _ in range(12):
            await self.worker.tick()
        job = self.control.get_job(job_id)
        self.assertTrue(job['terminal'])
        self.assertEqual(self.interrupted(), [])

    async def test_director_probe_p2_partial_draft_is_named(self):
        # Sonda P2 de direccion: material del intento no es "nada" ni "anterior".
        for _ in range(6):
            await self.worker.tick()
            if self.native.submissions:
                break
        self.assertEqual(1, len(self.native.submissions))
        job_id = self.native.submissions[0]['job_id']
        job = self.control.get_job(job_id)
        put = await self.client.call('gtd_command', {'job_id': job_id, 'command': {
            'operation_id': job_id + ':partial', 'action': 'put_material',
            'item_id': job['item_id'],
            'expected_version': self.service.get_item(job['item_id'])['version'],
            'fields': {'content': 'Borrador parcial guardado por este intento',
                       'mandate_id': job['mandate_id']}}})
        self.assertEqual(put['status'], 'applied', put)
        event = None
        for _ in range(15):
            await self.worker.tick()
            found = self.interrupted()
            if found:
                event = found[0]
                break
        self.assertIsNotNone(event, 'partial draft produced no notice')
        text = event['payload']['text']
        self.assertIn('Hay material guardado en el asunto; revisa allí su estado antes de usarlo.', text)
        self.assertNotIn('Borrador parcial guardado por este intento', text)
        self.assertNotIn('anterior', text)
        self.assertNotIn('nuevo', text)
        self.assertNotIn(job_id, text)

    async def test_user_stop_stays_silent(self):
        for _ in range(6):
            await self.worker.tick()
            if self.native.submissions:
                break
        self.assertEqual(1, len(self.native.submissions))
        self.native.observed_runtime = 5
        job_id = self.native.submissions[0]['job_id']
        stop = self.control.request_stop('felix', 'user-stop:1', job_id)
        self.assertTrue(self.control.get_job(job_id)['stop_requested'], stop)
        self.native.runs[job_id]['status'] = 'cancelled'
        for _ in range(10):
            await self.worker.tick()
        job = self.control.get_job(job_id)
        self.assertTrue(job['terminal'])
        self.assertEqual(self.interrupted(), [])


class EmissionScopeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.service = GTDService(Path(self.temp.name) / 'data')
        self.control = ExecutionControl(self.service, dict(BUDGET))
        self.item, self.mandate_id = prepare_item(self.service)
        self.worker = OrchestrationWorker(self.service, self.control, None, {})

    def tearDown(self):
        self.service.close()
        self.temp.cleanup()

    def interrupted(self):
        return [e for e in self.service.pending_events('gtd-notification', 'local')
                if e['payload'].get('kind') == 'interrupted']

    def test_paused_item_stays_silent(self):
        job_id = open_job(self.service, self.control, self.item, self.mandate_id)
        self.control.request_stop('gtd-felix', 'gtd-invalid-stop:' + job_id, job_id)
        observe_terminal_cancelled(self.control, job_id)
        paused = self.service.execute('felix', {'operation_id': 'int-pause', 'action': 'pause',
            'item_id': self.item['id'],
            'expected_version': self.service.get_item(self.item['id'])['version'], 'fields': {}})
        self.assertEqual(paused['status'], 'applied', paused)
        self.worker._notify_interrupted(job_id)
        self.assertEqual(self.interrupted(), [])

    def test_repeat_emission_is_single(self):
        job_id = open_job(self.service, self.control, self.item, self.mandate_id)
        self.control.request_stop('gtd-felix', 'gtd-invalid-stop:' + job_id, job_id)
        observe_terminal_cancelled(self.control, job_id)
        self.worker._notify_interrupted(job_id)
        self.worker._notify_interrupted(job_id)
        self.assertEqual(1, len(self.interrupted()))


class DeliveryTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.fixture = tg_fx.TelegramTests()
        self.fixture.setUp()
        self.service = self.fixture.service
        self.adapter = self.fixture.adapter
        self.http = self.fixture.http
        self.adapter.config = dataclasses.replace(self.adapter.config, auto_return=True)
        self.control = ExecutionControl(self.service, dict(BUDGET))
        self.item, self.mandate_id = prepare_item(self.service)
        self.mini = OrchestrationWorker(self.service, self.control, None, {})

    def tearDown(self):
        self.fixture.tearDown()

    def interrupted_event(self, operation='int-job'):
        job_id = open_job(self.service, self.control, self.item, self.mandate_id, operation=operation)
        self.control.request_stop('gtd-felix', 'gtd-invalid-stop:' + job_id, job_id)
        observe_terminal_cancelled(self.control, job_id)
        self.mini._notify_interrupted(job_id)
        events = [e for e in self.service.pending_events('gtd-notification', 'local')
                  if e['payload'].get('kind') == 'interrupted']
        self.assertEqual(1, len(events))
        return events[0], job_id

    async def test_notice_delivers_once_with_working_pause_and_show(self):
        event, job_id = self.interrupted_event()
        await self.adapter._deliver_notification(event, automatic=True)
        self.assertEqual(1, len(self.http.sent))
        sent = self.http.sent[-1]
        self.assertIn('No pude completar esta preparación', sent['text'])
        self.assertNotIn(job_id, sent['text'])
        buttons = [b for row in sent['reply_markup']['inline_keyboard'] for b in row]
        self.assertTrue(any(b['text'] == 'Ver asunto' for b in buttons))
        self.assertTrue(any(b['text'] == 'Pausar este asunto' for b in buttons))
        self.assertFalse(any(b['text'] == 'Pausar avisos' for b in buttons))
        config = self.adapter.config
        self.service.close()
        self.service = tg_fx.GTDService(tg_fx.Path(self.fixture.temp.name))
        self.fixture.service = self.service
        self.adapter = tg_fx.TelegramAdapter(self.service, self.fixture.client, config)
        self.fixture.service = self.service
        self.fixture.adapter = self.adapter
        await self.adapter._deliver_notification(event, automatic=True)
        self.assertEqual(1, len(self.http.sent))
        controls = {b['text']: b['callback_data']
                    for row in sent['reply_markup']['inline_keyboard'] for b in row}
        await self.adapter._callback({'id': 'ux-show', 'data': controls['Ver asunto']})
        self.assertIn(self.item['title'], self.http.sent[-1]['text'])
        await self.adapter._callback({'id': 'ux-pause', 'data': controls['Pausar este asunto']})
        self.assertEqual(self.service.get_item(self.item['id'])['status'], 'paused')

    async def test_pause_between_decision_and_delivery_suppresses(self):
        event, _ = self.interrupted_event(operation='int-job-pause')
        paused = self.service.execute('felix', {'operation_id': 'int-pause-late', 'action': 'pause',
            'item_id': self.item['id'],
            'expected_version': self.service.get_item(self.item['id'])['version'], 'fields': {}})
        self.assertEqual(paused['status'], 'applied', paused)
        await self.adapter._deliver_notification(event, automatic=True)
        self.assertEqual(0, len(self.http.sent))

    async def test_partial_and_prior_materials_are_distinguished(self):
        other = self.service.execute('felix', {'operation_id': 'int-mand2', 'action': 'grant_mandate',
            'item_id': self.item['id'],
            'expected_version': self.service.get_item(self.item['id'])['version'],
            'fields': {'scope_item_id': self.item['id'], 'capabilities': ['prepare_private'],
                       'actors': ['gtd-felix'], 'completion_criteria': 'x'}})
        self.assertEqual(other['status'], 'applied', other)
        old = self.service.execute('gtd-felix', {'operation_id': 'int-old-mat', 'action': 'put_material',
            'item_id': self.item['id'],
            'expected_version': self.service.get_item(self.item['id'])['version'],
            'fields': {'content': 'Minuta anterior ya conservada',
                       'mandate_id': self.mandate_id}})
        self.assertEqual(old['status'], 'applied', old)
        job_id = open_job(self.service, self.control, self.item, other['mandate']['id'],
                          bot_id='int-bot-2', operation='int-reserve-2')
        job = self.control.get_job(job_id)
        put = self.service.execute('gtd-felix', {'operation_id': job_id + ':partial2', 'action': 'put_material',
            'item_id': job['item_id'],
            'expected_version': self.service.get_item(job['item_id'])['version'],
            'fields': {'content': 'Borrador parcial de este segundo intento',
                       'mandate_id': other['mandate']['id']}})
        self.assertEqual(put['status'], 'applied', put)
        self.control.request_stop('gtd-felix', 'gtd-invalid-stop:' + job_id, job_id)
        observe_terminal_cancelled(self.control, job_id)
        self.mini._notify_interrupted(job_id)
        events = [e for e in self.service.pending_events('gtd-notification', 'local')
                  if e['payload'].get('kind') == 'interrupted']
        self.assertEqual(1, len(events))
        await self.adapter._deliver_notification(events[0], automatic=True)
        self.assertEqual(1, len(self.http.sent))
        text = self.http.sent[-1]['text']
        self.assertIn('Hay material guardado en el asunto; revisa allí su estado antes de usarlo.', text)
        self.assertNotIn('Borrador parcial de este segundo intento', text)
        self.assertNotIn('Minuta anterior ya conservada', text)
        self.assertEqual(2, len(self.service.materials(self.item['id'])))

    async def test_invalidated_material_is_pointed_at_not_attached(self):
        put = self.service.execute('gtd-felix', {'operation_id': 'int-mat-inv', 'action': 'put_material',
            'item_id': self.item['id'],
            'expected_version': self.service.get_item(self.item['id'])['version'],
            'fields': {'content': 'Borrador que quedara invalidado', 'mandate_id': self.mandate_id}})
        self.assertEqual(put['status'], 'applied', put)
        edit = self.service.execute('felix', {'operation_id': 'int-edit-inv', 'action': 'edit',
            'item_id': self.item['id'],
            'expected_version': self.service.get_item(self.item['id'])['version'],
            'fields': {'title': 'Mapa de responsabilidades TM corregido'}})
        self.assertEqual(edit['status'], 'applied', edit)
        mats = self.service.materials(self.item['id'])
        self.assertEqual(1, len(mats))
        self.assertFalse(mats[0]['valid'])
        fresh = self.service.execute('felix', {'operation_id': 'int-mand-inv', 'action': 'grant_mandate',
            'item_id': self.item['id'],
            'expected_version': self.service.get_item(self.item['id'])['version'],
            'fields': {'scope_item_id': self.item['id'], 'capabilities': ['prepare_private'],
                       'actors': ['gtd-felix'], 'completion_criteria': 'x'}})
        self.assertEqual(fresh['status'], 'applied', fresh)
        self.mandate_id = fresh['mandate']['id']
        event, _ = self.interrupted_event(operation='int-job-inv')
        self.assertIn('Hay material guardado en el asunto', event['payload']['text'])
        await self.adapter._deliver_notification(event, automatic=True)
        self.assertEqual(1, len(self.http.sent))
        self.assertNotIn('Borrador que quedara invalidado', self.http.sent[-1]['text'])
        self.assertEqual(1, len(self.service.materials(self.item['id'])))

    async def test_domain_change_without_material_keeps_history_truth(self):
        edit = self.service.execute('felix', {'operation_id': 'int-edit-nomat', 'action': 'edit',
            'item_id': self.item['id'],
            'expected_version': self.service.get_item(self.item['id'])['version'],
            'fields': {'title': 'Mapa de responsabilidades TM aclarado'}})
        self.assertEqual(edit['status'], 'applied', edit)
        fresh = self.service.execute('felix', {'operation_id': 'int-mand-nomat', 'action': 'grant_mandate',
            'item_id': self.item['id'],
            'expected_version': self.service.get_item(self.item['id'])['version'],
            'fields': {'scope_item_id': self.item['id'], 'capabilities': ['prepare_private'],
                       'actors': ['gtd-felix'], 'completion_criteria': 'x'}})
        self.assertEqual(fresh['status'], 'applied', fresh)
        self.mandate_id = fresh['mandate']['id']
        event, _ = self.interrupted_event(operation='int-job-nomat')
        self.assertIn('no hay material guardado', event['payload']['text'])
        self.assertNotIn('intacto', event['payload']['text'])

    async def test_prior_material_is_named_not_attached(self):
        put = self.service.execute('gtd-felix', {'operation_id': 'int-mat', 'action': 'put_material',
            'item_id': self.item['id'],
            'expected_version': self.service.get_item(self.item['id'])['version'],
            'fields': {'content': 'Antecedente previo verificable', 'mandate_id': self.mandate_id}})
        self.assertEqual(put['status'], 'applied', put)
        event, _ = self.interrupted_event(operation='int-job-mat')
        await self.adapter._deliver_notification(event, automatic=True)
        self.assertEqual(1, len(self.http.sent))
        sent = self.http.sent[-1]
        self.assertIn('Hay material guardado en el asunto; revisa allí su estado antes de usarlo.', sent['text'])
        self.assertNotIn('Antecedente previo verificable', sent['text'])


if __name__ == '__main__':
    unittest.main()
