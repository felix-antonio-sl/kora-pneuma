"""P5 capacity outcome against real product; only native/Telegram IO is synthetic.

Run with GTD_RUNTIME_ROOT set to the candidate runtime. The two-second window
is a synthetic acceptance deadline, not a production latency claim. Long work
does not finish during that window unless the product safely stops it. The
fixture has no scheduling, priority, reservation or preemption implementation.
"""
import asyncio
from datetime import datetime, timedelta, timezone
from pathlib import Path
import sys
import tempfile
import time
import unittest

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from aiohttp import web
from gtd_felix.application import create_app
from gtd_felix.control import ExecutionControl
from gtd_felix.mcp import MCPClient
from gtd_felix.orchestration import OrchestrationWorker
from gtd_felix.service import GTDService
from gtd_felix.telegram import AiohttpTelegramClient, TelegramAdapter, TelegramConfig
from test_telegram import FakeHTTP, message


MATERIAL = 'Opción A: 42 unidades. Opción B: 57 unidades. A ahorra 15 unidades; recomiendo A.'
LONG_MATERIAL = 'Preparación larga terminada: comparación comprobada y material anterior conservado.'


class AttentionNative:
    """Synthetic interruptible private work; real MCP writes and control receipts."""
    def __init__(self, control, client, long_items):
        self.control, self.client, self.long_items = control, client, long_items
        self.runs, self.submissions, self.stops, self.active_samples = {}, [], [], []
        self.blocked_stops = set()
        self.finish_resumed = True
        self.finish_items = set()
        self.material_only_items = set()
        self.terminal_cost_usd = .25

    def native(self, job_id):
        return dict(provider='fixture', host='synthetic', profile='fixture', id=job_id)

    def sample(self):
        self.active_samples.append(self.control.budget()['active'])
        if self.active_samples[-1] > 2:
            raise AssertionError('Global admission exceeded two even transiently')

    async def discover(self, bot_id):
        return dict(status='ready', capabilities=['submit', 'poll', 'stop'])

    async def submit(self, job_id, prompt, durable=False):
        self.sample()
        if job_id in self.runs:
            raise AssertionError('Duplicate native dispatch')
        self.submissions.append(job_id)
        self.control.record_dispatch(job_id, self.native(job_id))
        self.runs[job_id] = 'running'
        job = self.control.get_job(job_id)
        if job['item_id'] in self.material_only_items and self.control.service.materials(job['item_id']):
            # A later evaluation sees the existing private material; it must
            # not manufacture another copy or claim a protected human result.
            self.runs[job_id] = 'completed'
            return dict(status='submitted', job_id=job_id, native_id=job_id)
        if (job['item_id'] not in self.long_items or job['item_id'] in self.finish_items
                or (job.get('attention_origin') and self.finish_resumed)):
            content = LONG_MATERIAL if job['item_id'] in self.long_items else MATERIAL
            item = await self.client.call('gtd_read', dict(view='item', item_id=job['item_id']))
            for action, fields in (
                ('put_material', dict(content=content, source_versions={}, mandate_id=job['mandate_id'])),
                ('assess_result', dict(satisfied=True, evidence='Synthetic comparison checked: 57 - 42 = 15.',
                                       mandate_id=job['mandate_id'])),
            ):
                if action == 'assess_result' and job['item_id'] in self.material_only_items:
                    continue
                receipt = await self.client.call('gtd_command', dict(job_id=job_id, command=dict(
                    operation_id=job_id + ':' + action, action=action, item_id=item['id'],
                    expected_version=item['version'], fields=fields)))
                if receipt.get('status') != 'applied':
                    raise AssertionError(receipt)
                item = receipt['item']
            self.runs[job_id] = 'completed'
        return dict(status='submitted', job_id=job_id, native_id=job_id)

    async def poll(self, job_id):
        self.sample()
        status = self.runs[job_id]
        observation = dict(native_identity=self.native(job_id), native_status=status,
            terminal=status != 'running', cost_usd=self.terminal_cost_usd if status != 'running' else .25, runtime_seconds=5,
            evidence_reference='fixture://attention/' + job_id)
        if not self.control.get_job(job_id)['terminal']:
            receipt = self.control.observe(job_id, observation)
            if receipt['status'] != 'recorded':
                raise AssertionError(receipt)
        return dict(status='observed', job_id=job_id, terminal=observation['terminal'],
                    native_status=status, observation=observation,
                    output=(LONG_MATERIAL if self.control.get_job(job_id)['item_id'] in self.long_items else MATERIAL)
                        if status == 'completed' else None)

    async def reconcile(self, job_id):
        return await self.poll(job_id)

    async def stop(self, job_id):
        self.sample()  # A request alone must not release global capacity.
        self.stops.append(job_id)
        # Hermes/Codex also register their own control stop before provider IO.
        receipt = self.control.request_stop('gtd-felix', 'synthetic-native-stop:' + job_id, job_id)
        if receipt['status'] != 'stop_requested':
            raise AssertionError(receipt)
        for member in self.control._load()['jobs'].values():
            if (member['root_job_id'] == job_id or member['id'] == job_id) and member['id'] not in self.blocked_stops:
                self.runs[member['id']] = 'cancelled'
        return dict(status='stop_requested', job_id=job_id)


class AttentionCapacityTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.service = GTDService(Path(self.temp.name) / 'data')
        self.budget = dict(period_start=datetime.now(timezone.utc).isoformat(), period_seconds=3600,
            max_cost_usd=20, max_runtime_seconds=2000, recovery_cost_usd=2,
            recovery_runtime_seconds=100, max_job_runtime_seconds=300,
            max_retries=0, max_descendants=0, max_active=2)
        self.control = ExecutionControl(self.service, self.budget)
        self.long_items = set()
        self.control.register_bot('felix', 'attention-bot', dict(id='principal', state='available',
            source_urn='urn:test:principal', host='synthetic', profile='fixture',
            capabilities=['prepare_private'], item_id=None, mandate_id=None,
            probe_evidence='fixture://attention'))
        config = dict(data_dir=str(Path(self.temp.name) / 'data'),
            actors=dict(owner='felix', principal='gtd-felix', executors=[]),
            api_tokens={'synthetic-agent-token': 'gtd-felix'})
        self.runner = web.AppRunner(create_app(self.service, self.control, config), access_log=None)
        await self.runner.setup()
        site = web.TCPSite(self.runner, '127.0.0.1', 0)
        await site.start()
        url = 'http://127.0.0.1:' + str(site._server.sockets[0].getsockname()[1])
        self.native = AttentionNative(self.control, MCPClient(url, 'synthetic-agent-token'), self.long_items)
        self.config = dict(actor='gtd-felix', principal_bot_id='principal', clarification_accounts=['synthetic-bot'],
            reservation=dict(max_cost_usd=4, max_runtime_seconds=200, max_retries=0, max_descendants=0),
            poll_seconds=.01, review_interval_seconds=300, timezone='UTC')
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        self.http = FakeHTTP()
        self.telegram_config = TelegramConfig('synthetic-bot', 7, 9, 'felix')
        self.telegram_client = AiohttpTelegramClient('synthetic-secret', self.http, attempts=1)
        self.telegram = TelegramAdapter(self.service, self.telegram_client, self.telegram_config)

    async def asyncTearDown(self):
        # There are no native subprocesses; close the owned HTTP listener and DB.
        await self.runner.cleanup()
        self.service.close()
        self.temp.cleanup()

    async def deliver(self, update):
        self.http.updates = [update]
        await self.telegram.poll_once()
        await self.telegram.process_pending()

    def clarify(self, item, operation, **extra):
        receipt = self.service.execute('gtd-felix', dict(operation_id=operation, action='clarify',
            item_id=item['id'], expected_version=item['version'], fields=dict(
                kind='action', commitment='committed', capability='prepare_private',
                completion_criteria='Compare 42 and 57 and provide the difference and recommendation.',
                intent_basis=dict(source_item_id=item['id'], quote=item['text']), **extra)))
        self.assertEqual(receipt['status'], 'applied', receipt)
        return receipt['item']

    async def scenario(self, long_count):
        for index in range(long_count):
            item = self.service.capture('felix', 'long-' + str(index),
                                        'Preparación privada larga posponible ' + str(index))['item']
            self.long_items.add(item['id'])
            self.clarify(item, 'clarify-long-' + str(index), priority=0)
        await self.worker.tick()
        self.assertEqual(self.control.budget()['active'], long_count)
        self.assertEqual(len(self.native.submissions), long_count)
        started = time.monotonic()
        update = message(500, 'Compara 42 y 57: necesito decidir dentro de dos segundos; entrega diferencia y recomendación.')
        await self.deliver(update)
        captured = [i for i in self.service.query() if i.get('source', {}).get('message_id') == 500]
        self.assertEqual(len(captured), 1, 'Reception must persist under full preparation capacity')
        short = self.clarify(captured[0], 'clarify-short', priority=100,
            decision_at=(datetime.now(timezone.utc) + timedelta(seconds=2)).isoformat())
        self.assertLess(time.monotonic() - started, 2, 'Reception missed the synthetic window')
        for _ in range(2):
            await self.deliver(update)
        self.assertEqual(sum(i.get('source', {}).get('message_id') == 500 for i in self.service.query()), 1)
        self.assertEqual(sum(m['text'].startswith('Guardado.') for m in self.http.sent), 1)
        # Isolate concurrency from exhausted period budget: another reservation
        # fits monetarily and temporally, but may not exceed the two global slots.
        available = self.control.budget()
        self.assertGreaterEqual(available['remaining_cost_usd'], self.config['reservation']['max_cost_usd'])
        self.assertGreaterEqual(available['remaining_runtime_seconds'], self.config['reservation']['max_runtime_seconds'])
        deadline = started + 2
        while time.monotonic() < deadline:
            await self.worker.tick()
            self.native.sample()
            budget = self.control.budget()
            self.assertLessEqual(budget['committed_cost_usd'] + budget['recovery_cost_usd'], 20)
            self.assertLessEqual(budget['committed_runtime_seconds'] + budget['recovery_runtime_seconds'], 2000)
            if self.service.get_item(short['id'])['status'] == 'done':
                # Result integration and notification use another real worker tick.
                await self.worker.tick()
                break
            await asyncio.sleep(.02)
        materials = self.service.materials(short['id'])
        short_jobs = [j for j in self.control._load()['jobs'].values() if j['item_id'] == short['id']]
        self.assertTrue(materials, 'P5: brief request persisted but received no useful material before its window; '
            f'long_count={long_count}, active={self.control.budget()["active"]}, '
            f'short_jobs={len(short_jobs)}, safe_stop_requests={len(self.native.stops)}')
        self.assertEqual(len(materials), 1)
        self.assertEqual(self.service.get_item(short['id'])['status'], 'done')
        self.assertEqual(len(short_jobs), 1)
        self.assertEqual(short_jobs[0]['integration'], 'integrated')
        await self.deliver(message(501, '/preparado'))
        self.assertEqual(sum(MATERIAL in m['text'] for m in self.http.sent), 1)
        self.assertLess(time.monotonic() - started, 2, 'Useful delivery missed the synthetic window')
        # Replayed input and fresh workers must not dispatch or notify twice.
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        self.telegram = TelegramAdapter(self.service, self.telegram_client, self.telegram_config)
        await self.deliver(update)
        for _ in range(3):
            await self.worker.tick()
        await self.deliver(message(502, '/preparado'))
        self.assertEqual(sum(MATERIAL in m['text'] for m in self.http.sent), 1)
        self.assertEqual(len(self.service.materials(short['id'])), 1)
        self.assertEqual(len([j for j in self.control._load()['jobs'].values() if j['item_id'] == short['id']]), 1)
        self.assertLessEqual(max(self.native.active_samples), 2)
        if long_count == 2:
            records = self.control._load()['attention_displacements']
            self.assertEqual(len(records), 1)
            record = next(iter(records.values()))
            old = self.control.get_job(record['old_job_id'])
            new = self.control.get_job(record['new_job_id'])
            self.assertNotEqual(old['id'], new['id'])
            self.assertTrue(old['terminal'])
            self.assertTrue(new['terminal'])
            self.assertEqual(new['integration'], 'integrated')
            self.assertEqual(self.service.get_item(old['item_id'])['status'], 'done')
            self.assertEqual(len(self.native.stops), 1)
            self.assertEqual(record['period'], self.control.config)

    async def test_brief_work_material_and_delivery_with_one_free_slot(self):
        await self.scenario(1)

    async def test_brief_work_gets_capacity_while_two_long_preparations_run(self):
        await self.scenario(2)
