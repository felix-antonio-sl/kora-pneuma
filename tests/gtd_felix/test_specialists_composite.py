"""P4 composed service evidence; Hermes transport and contributions are synthetic.

HTTP/MCP, domain, reservations, material bytes and orchestration are real local
seams. This does not exercise models, a human bot conversation or remote nodes.
"""
from datetime import datetime, timezone
from pathlib import Path
import tempfile
import unittest
import aiohttp

from test_orchestration import (
    ExecutionControl, GTDService, MCPClient, NativeFixture,
    OrchestrationWorker, create_app, web,
)


class SpecialistsCompositeTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.actors = ['specialist-a', 'specialist-a-replacement', 'specialist-b']
        self.service = GTDService(self.root / 'data', executor_actors=self.actors)
        self.budget = dict(period_start=datetime.now(timezone.utc).isoformat(), period_seconds=3600,
            max_cost_usd=20, max_runtime_seconds=2000, recovery_cost_usd=2,
            recovery_runtime_seconds=100, max_job_runtime_seconds=500,
            max_retries=0, max_descendants=3, max_active=2)
        self.control = ExecutionControl(self.service, self.budget)
        self.config = dict(actor='gtd-felix', principal_bot_id='principal',
            clarification_accounts=[], reservation=dict(max_cost_usd=6,
                max_runtime_seconds=400, max_retries=0, max_descendants=3),
            poll_seconds=.01, review_interval_seconds=300)
        await self.open_http()
        self.native = NativeFixture(self.control, self.client)
        self.native.no_progress = True
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        self.counter = 0
        self.project = self.service.capture('felix', 'project', 'Synthetic workshop')['item']['id']
        self.command(self.project, 'clarify', kind='project', commitment='committed',
            completion_criteria='A and B integrated; Felix confirms the booking')
        self.a = self.command(self.project, 'derive', kind='action', title='Determine capacity',
            text='Capacity is 8 people', executor=self.actors[0], capability='prepare_private')['item']['id']
        self.b = self.command(self.project, 'derive', kind='action', title='Compute catering',
            executor=self.actors[2], capability='prepare_private', depends_on=[self.a],
            source_versions={self.project: 1})['item']['id']
        self.waiting = self.command(self.project, 'derive', kind='waiting', title='Felix confirms booking',
            waiting_for='Felix confirms booking', executor='felix', capability='prepare_private')['item']['id']
        self.mandate = self.command(self.project, 'grant_mandate', scope_item_id=self.project,
            actors=['gtd-felix', *self.actors], capabilities=['prepare_private'],
            completion_criteria='Private workshop calculations only')['mandate']['id']
        self.bot('principal', 'gtd-felix', 'available')

    async def open_http(self):
        tokens = {'synthetic-owner-token': 'felix', 'synthetic-principal': 'gtd-felix',
            **{'synthetic-' + actor: actor for actor in self.actors}}
        appconfig = dict(data_dir=str(self.root / 'data'),
            actors={'owner': 'felix', 'principal': 'gtd-felix', 'executors': self.actors},
            api_tokens=tokens)
        self.runner = web.AppRunner(create_app(self.service, self.control, appconfig), access_log=None)
        await self.runner.setup()
        site = web.TCPSite(self.runner, '127.0.0.1', 0)
        await site.start()
        self.url = 'http://127.0.0.1:' + str(site._server.sockets[0].getsockname()[1])
        self.client = MCPClient(self.url, 'synthetic-principal')

    async def reopen(self):
        await self.runner.cleanup()
        self.service.close()
        self.service = GTDService(self.root / 'data', executor_actors=self.actors)
        self.control = ExecutionControl(self.service, self.budget)
        await self.open_http()
        # The fake remote retains its native runs; all service objects are fresh.
        self.native.control, self.native.client = self.control, self.client
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)

    async def asyncTearDown(self):
        await self.runner.cleanup()
        self.service.close()
        self.temp.cleanup()

    def command(self, item_id, action, **fields):
        self.counter += 1
        item = self.service.get_item(item_id)
        receipt = self.service.execute('felix', dict(operation_id=f'{action}-{self.counter}',
            action=action, item_id=item_id, expected_version=item['version'], fields=fields))
        self.assertEqual(receipt['status'], 'applied', receipt)
        return receipt

    def bot(self, bot_id, actor, state):
        receipt = self.control.register_bot('felix', bot_id + '-' + state,
            dict(id=bot_id, actor=actor, state=state, source_urn='urn:test:shared-specialist',
                host='synthetic', profile='fixture', capabilities=['prepare_private'],
                probe_evidence='fixture://route/' + bot_id))
        self.assertEqual(receipt['status'], 'applied', receipt)

    def reserve(self, item_id, bot_id, purpose, **overrides):
        self.counter += 1
        request = dict(item_id=item_id, expected_version=self.service.get_item(item_id)['version'],
            mandate_id=self.mandate, capability='prepare_private', bot_id=bot_id,
            purpose=purpose, scope='Only this synthetic workshop matter',
            max_cost_usd=1, max_runtime_seconds=50, max_retries=0, max_descendants=0)
        request.update(overrides)
        return self.control.reserve('gtd-felix', 'reserve-' + str(self.counter), request)

    async def start(self, receipt):
        self.assertEqual(receipt['status'], 'reserved', receipt)
        job_id = receipt['job_id']
        state = self.worker._state()
        state['runs'][job_id] = dict(phase='intent', durable=True, event_keys=[],
            prompt=self.worker._prompt(receipt['job'], []))
        await self.worker._advance(state, job_id)
        self.assertIn(job_id, self.native.runs)
        return job_id

    async def finish(self, job_id, content):
        self.native.runs[job_id]['output'] = content
        await self.worker._advance(self.worker._state(), job_id)
        return self.control.get_job(job_id)

    async def read_material(self, item_id):
        materials = await self.client.call('gtd_read', dict(view='materials', item_id=item_id))
        self.assertEqual(len(materials), 1)
        material = materials[0]
        read = await self.client.call('gtd_read', dict(view='material', item_id=item_id,
            material_id=material['id'], version=material['version']))
        self.assertTrue(read['valid'], read)
        return read

    async def test_two_specialists_corrected_replaced_and_integrated_once(self):
        await self.run_composite()

    async def test_correction_of_a_after_b_reservation_rejects_b_old_return(self):
        await self.run_composite(correct_after_b=True)

    async def run_composite(self, correct_after_b=False):
        # Planned and incorporated inventory never grants a usable execution route.
        for state in ('planned', 'incorporated'):
            self.bot('a', self.actors[0], state)
            denied = self.reserve(self.a, 'a', 'capacity')
            self.assertEqual(denied['error'], 'bot_unavailable', denied)
        self.bot('a', self.actors[0], 'available')
        old = await self.start(self.reserve(self.a, 'a', 'capacity'))
        old_identity = self.control.get_job(old)['native']
        current = self.service.get_item(self.a)
        # Owner addresses A's actual matter while A is running, without principal interpretation.
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url + '/v1/commands',
                    headers={'Authorization': 'Bearer synthetic-owner-token'},
                    json=dict(operation_id='human-corrects-a', action='edit', item_id=self.a,
                        expected_version=current['version'], fields={'text': 'Capacity is 12 people'})) as response:
                corrected = await response.json()
        self.assertEqual(corrected['status'], 'applied', corrected)
        stale = await self.finish(old, 'Capacity is 8 people; buy 16 portions')
        self.assertEqual(stale['integration'], 'discarded', stale)
        self.assertEqual(self.service.materials(self.a), [])
        self.bot('a', self.actors[0], 'suspended')
        self.assertEqual(self.reserve(self.a, 'a', 'capacity-again')['status'], 'rejected')
        self.bot('a2', self.actors[1], 'available')
        self.bot('b', self.actors[2], 'available')
        root = self.reserve(self.project, 'principal', 'Coordinate corrected workshop',
            max_cost_usd=6, max_runtime_seconds=400, max_descendants=3)
        self.assertEqual(root['status'], 'reserved', root)
        parent = await self.start(root)
        a_job = await self.start(self.reserve(self.a, 'a2', 'Corrected capacity', parent_job_id=parent))
        self.assertNotEqual(a_job, old)
        self.assertEqual(self.control.get_job(a_job)['actor'], self.actors[1])
        self.assertEqual(self.control.get_job(old)['native'], old_identity)
        a_client = MCPClient(self.url, 'synthetic-' + self.actors[1])
        basis = await a_client.call('gtd_read', dict(view='item', item_id=self.a, job_id=a_job))
        self.assertEqual(basis['text'], 'Capacity is 12 people')
        denied = await a_client.call('gtd_read', dict(view='item', item_id=self.b, job_id=a_job))
        self.assertEqual(denied['error'], 'item_not_found', denied)
        self.assertEqual((await self.finish(a_job, basis['text']))['integration'], 'integrated')
        a_material = await self.read_material(self.a)
        self.assertEqual(a_material['content'], 'Capacity is 12 people')
        sources = {self.project: len(self.service.get_item(self.project)['source_revisions'])}
        # Principal conveys the material bytes and provenance, rather than a bare dependency ID.
        b_scope = ('Use two portions per person. A material ' + a_material['material_id']
            + ' item=' + self.a + ' version=' + str(a_material['version'])
            + ' sha256=' + a_material['sha256'] + ': ' + a_material['content'])
        oversized = self.reserve(self.b, 'b', 'Overallocated catering', parent_job_id=parent,
            max_cost_usd=6, scope=b_scope)
        self.assertEqual(oversized['error'], 'parent_allocation_exhausted', oversized)
        b_job = await self.start(self.reserve(self.b, 'b', 'Catering based on corrected A',
            parent_job_id=parent, scope=b_scope))
        b_record = self.control.get_job(b_job)
        b_client = MCPClient(self.url, 'synthetic-' + self.actors[2])
        b_context = await b_client.call('gtd_read', dict(view='item', item_id=self.b, job_id=b_job))
        self.assertEqual(b_context['source_versions'], sources)
        denied = await b_client.call('gtd_read', dict(view='material', item_id=self.a,
            material_id=a_material['material_id'], version=a_material['version'], job_id=b_job))
        self.assertEqual(denied['error'], 'item_not_found', denied)
        self.assertEqual(b_record['source_versions'], sources)
        self.assertEqual(b_record['root_job_id'], parent)
        self.assertEqual(self.control.get_job(a_job)['root_job_id'], parent)
        self.assertEqual(self.control.validate(parent, 'prepare_private')['limits']['max_cost_usd'], 4)
        prompt = next(s['prompt'] for s in self.native.submissions if s['job_id'] == b_job)
        self.assertIn(a_material['content'], prompt)
        self.assertIn(a_material['material_id'], prompt)
        # Deterministic synthetic B function is explicitly conditioned on supplied A bytes.
        people = int(b_record['scope'].split('Capacity is ')[1].split()[0])
        b_output = f'Prepare {people * 2} portions for {people} people; await Felix booking confirmation'
        if correct_after_b:
            current = self.service.get_item(self.a)
            async with aiohttp.ClientSession() as session:
                async with session.post(self.url + '/v1/commands',
                        headers={'Authorization': 'Bearer synthetic-owner-token'},
                        json=dict(operation_id='human-corrects-a-again', action='edit', item_id=self.a,
                            expected_version=current['version'], fields={'text': 'Capacity is 20 people'})) as response:
                    corrected = await response.json()
            self.assertEqual(corrected['status'], 'applied', corrected)
            self.assertFalse(self.service.materials(self.a)[0]['valid'])
            result = await self.finish(b_job, b_output)
            self.assertEqual(result['integration'], 'discarded',
                'B must reject its 12-person return after owner corrects A to 20; '
                'the explicit B depends_on A relationship must retain its reserved basis')
            self.assertEqual(self.service.materials(self.b), [])
            return
        self.assertEqual((await self.finish(b_job, b_output))['integration'], 'integrated')
        b_material = await self.read_material(self.b)
        self.assertIn('24 portions for 12 people', b_material['content'])
        combined = '\n'.join(
            f'{label}: {material["content"]} '
            f'[item={material["item_id"]}, material={material["material_id"]}, '
            f'version={material["version"]}, sha256={material["sha256"]}]'
            for label, material in [('A', a_material), ('B', b_material)])
        integrated = await self.client.call('gtd_command', {'job_id': parent, 'command': dict(
            operation_id='principal-integrates-a-b', action='put_material', item_id=self.project,
            expected_version=self.service.get_item(self.project)['version'], fields={
                'content': combined, 'source_versions': sources, 'mandate_id': self.mandate})})
        self.assertEqual(integrated['status'], 'applied', integrated)
        project_material = await self.read_material(self.project)
        self.assertEqual(project_material['content'], combined)
        waiting = self.service.get_item(self.waiting)
        self.assertEqual(waiting['parent_id'], self.project)
        self.assertEqual(waiting['waiting_for'], 'Felix confirms booking')
        self.assertNotEqual(waiting['status'], 'done')
        self.assertNotEqual(self.service.get_item(self.project)['status'], 'done')
        submissions = len(self.native.submissions)
        await self.reopen()
        for _ in range(2):
            for job in (old, a_job, b_job):
                await self.worker._advance(self.worker._state(), job)
        replay = await self.client.call('gtd_command', {'job_id': parent, 'command': dict(
            operation_id='principal-integrates-a-b', action='put_material', item_id=self.project,
            expected_version=integrated['item']['version'] - 1, fields={
                'content': combined, 'source_versions': sources, 'mandate_id': self.mandate})})
        self.assertEqual(replay['status'], 'already_applied', replay)
        self.assertEqual((await self.finish(parent, combined))['integration'], 'integrated')
        await self.reopen()
        await self.worker._advance(self.worker._state(), parent)
        self.assertEqual(len(self.native.submissions), submissions)
        self.assertEqual(len(self.service.materials(self.project)), 1)
        self.assertEqual(len(self.service.materials(self.a)), 1)
        self.assertEqual(len(self.service.materials(self.b)), 1)

    async def test_suspension_blocks_reserved_delivery_and_new_reservations(self):
        self.bot('a', self.actors[0], 'available')
        receipt = self.reserve(self.a, 'a', 'Reserved but not delivered')
        self.assertEqual(receipt['status'], 'reserved', receipt)
        job_id = receipt['job_id']
        self.bot('a', self.actors[0], 'suspended')
        rejected = self.reserve(self.a, 'a', 'New delivery while suspended')
        self.assertEqual(rejected['error'], 'bot_unavailable', rejected)
        state = self.worker._state()
        state['runs'][job_id] = dict(phase='intent', durable=True, event_keys=[],
            prompt=self.worker._prompt(receipt['job'], []))
        await self.worker._advance(state, job_id)
        self.assertEqual(self.native.submissions, [])
        self.assertIsNone(self.control.get_job(job_id)['native'])
        self.assertEqual(self.control.get_job(job_id)['observations'], [])
        self.assertEqual(self.service.materials(self.a), [])
