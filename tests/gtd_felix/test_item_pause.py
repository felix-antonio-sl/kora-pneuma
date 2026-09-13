"""Owner pauses an affair without losing its private preparation or context."""
import unittest
from test_gtd import GTDTest as _DomainFixture
from test_orchestration import OrchestrationTests as _WorkerFixture
from gtd_felix.orchestration import OrchestrationWorker


class ItemPauseTests(unittest.TestCase):
    setUp = _DomainFixture.setUp
    tearDown = _DomainFixture.tearDown
    restart = _DomainFixture.restart
    cmd = _DomainFixture.cmd
    ok = _DomainFixture.ok
    capture = _DomainFixture.capture
    private_action = _DomainFixture.private_action

    def test_pause_owner_version_replay_and_explicit_reopen(self):
        item = self.private_action()
        self.assertEqual(self.cmd(item, 'edit', {'status': 'paused'})['error'], 'invalid_fields')
        self.assertEqual(self.cmd(item, 'postpone')['error'], 'review_at_required')
        denied = self.cmd(item, 'pause', actor='gtd-felix')
        self.assertEqual(denied['error'], 'owner_or_assessment_required')
        self.assertEqual(self.cmd(item, 'pause', {'review_at': '2030-01-01'})['error'], 'invalid_fields')
        command = dict(operation_id='pause-once', action='pause', item_id=item['id'], expected_version=item['version'], fields={})
        receipt = self.service.execute('felix', command)
        paused = self.ok(receipt)
        self.assertEqual(paused['status'], 'paused')
        self.assertEqual(paused['commitment'], item['commitment'])
        self.assertEqual(paused.get('review_at'), item.get('review_at'))
        self.assertEqual(self.service.execute('felix', command), {**receipt, 'status': 'already_applied'})
        self.assertEqual(self.cmd(item, 'reopen')['status'], 'conflict')
        self.restart()
        self.assertEqual(self.service.get_item(item['id']), paused)
        reopened = self.ok(self.cmd(paused, 'reopen'))
        self.assertEqual(reopened['status'], 'active')
        terminal = self.ok(self.cmd(reopened, 'withdraw'))
        self.assertEqual(self.cmd(terminal, 'pause')['error'], 'terminal_item')

    def test_pause_preserves_v2_and_blocks_private_writes_but_not_reads_or_routing(self):
        item = self.private_action()
        item = self.ok(self.cmd(item, 'put_material', {'content': 'Draft v1'}, actor='gtd-felix'))
        material = self.service.materials(item['id'])[0]
        item = self.ok(self.cmd(item, 'put_material', {'content': 'Corrected draft v2', 'material_id': material['id']}, actor='gtd-felix'))
        before = self.service.materials(item['id'])
        item = self.ok(self.cmd(item, 'pause'))
        for action, fields in [('put_material', {'content': 'Unwanted v3'}), ('plan', {'plan_steps': ['Unwanted preparation']})]:
            self.assertEqual(self.cmd(item, action, fields, actor='gtd-felix')['error'], 'work_paused')
        self.assertTrue(self.service.authorize('gtd-felix', 'prepare_private', item['id'])['allowed'])
        note = self.capture('Retomar este asunto más adelante')
        self.ok(self.cmd(note, 'clarify', {'destination': 'existing', 'target_item_id': item['id'], 'reason': 'Same affair', 'intent_basis': {'quote': note['text'], 'source_item_id': note['id']}}, actor='gtd-felix'))
        self.restart()
        self.assertEqual(self.service.materials(item['id']), before)
        self.assertTrue(before[-1]['valid'])
        self.assertEqual(before[-1]['version'], 2)
        self.assertEqual(self.service.get_item(item['id'])['status'], 'paused')


class ItemPauseWorkerTests(unittest.IsolatedAsyncioTestCase):
    asyncSetUp = _WorkerFixture.asyncSetUp
    asyncTearDown = _WorkerFixture.asyncTearDown
    integrated_executor_delivery = _WorkerFixture.integrated_executor_delivery

    def pause(self, item_id):
        item = self.service.get_item(item_id)
        result = self.service.execute('felix', dict(operation_id='pause-'+item_id, action='pause', item_id=item_id, expected_version=item['version'], fields={}))
        self.assertEqual(result['status'], 'applied', result)
        return result['item']

    async def test_pause_blocks_fresh_reservation_and_dispatch_preserves_explicit_read(self):
        request = {**self.config['reservation'], 'item_id': self.item['id'], 'expected_version': self.item['version'], 'mandate_id': None, 'capability': 'prepare_private', 'bot_id': 'principal', 'purpose': 'Private preparation', 'scope': 'This affair'}
        job = self.control.reserve('gtd-felix', 'before-pause', request)
        self.assertEqual(job['status'], 'reserved', job)
        paused = self.pause(self.item['id'])
        self.assertEqual(self.control.validate(job['job_id'], 'prepare_private')['reason'], 'work_paused')
        request['expected_version'] = paused['version']
        self.assertEqual(self.control.reserve('gtd-felix', 'after-pause', request)['error'], 'work_paused')
        read = await self.client.call('gtd_read', {'view': 'item', 'item_id': paused['id']})
        self.assertEqual(read['status'], 'paused')
        await self.worker.tick()
        self.assertEqual(self.native.submissions, [])
        reopened = self.service.execute('felix', dict(operation_id='resume', action='reopen', item_id=paused['id'], expected_version=paused['version'], fields={}))['item']
        self.assertEqual(self.control.validate(job['job_id'], 'prepare_private')['reason'], 'stale_item_version')
        request['expected_version'] = reopened['version']
        # Old reservations retain their budget until resolved; use the direct
        # domain path to prove explicit resumption permits fresh preparation.
        prepared = self.service.execute('gtd-felix', dict(operation_id='resumed-preparation', action='put_material', item_id=reopened['id'], expected_version=reopened['version'], fields={'content': 'Resumed preparation'}))
        self.assertEqual(prepared['status'], 'applied', prepared)

    async def test_parent_pause_holds_child_return_without_affecting_unrelated_item(self):
        job, child_id, _ = await self.integrated_executor_delivery(child=True)
        before = self.service.materials(child_id)
        self.pause(self.item['id'])
        child = self.service.get_item(child_id)
        blocked = self.service.execute('gtd-felix', dict(operation_id='paused-child-write', action='put_material', item_id=child_id, expected_version=child['version'], fields={'content': 'Unwanted'}))
        self.assertEqual(blocked['error'], 'work_paused')
        unrelated = self.service.capture('felix', 'unrelated', 'Another affair')['item']
        updated = self.service.execute('gtd-felix', dict(operation_id='unrelated-write', action='put_material', item_id=unrelated['id'], expected_version=unrelated['version'], fields={'content': 'Independent draft'}))
        self.assertEqual(updated['status'], 'applied', updated)
        count = len(self.native.submissions)
        for _ in range(2):
            self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
            await self.worker.tick()
        self.assertEqual(self.worker._state()['executor_returns'][job]['blocker'], 'work_paused')
        self.assertFalse(any(self.control.get_job(s['job_id'])['item_id'] in {self.item['id'], child_id} for s in self.native.submissions[count:]))
        self.assertEqual(self.service.materials(child_id), before)

# Imported fixture classes are helpers, not additional suites in this module.
del _DomainFixture, _WorkerFixture
