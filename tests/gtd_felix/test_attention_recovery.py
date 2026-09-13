"""Adversarial P5 recovery over real control/orchestration and synthetic IO."""
from datetime import datetime, timedelta, timezone
import unittest
from unittest.mock import patch

import test_attention_capacity as capacity
from gtd_felix.orchestration import OrchestrationWorker


class AttentionRecoveryTests(unittest.IsolatedAsyncioTestCase):
    asyncSetUp = capacity.AttentionCapacityTests.asyncSetUp
    asyncTearDown = capacity.AttentionCapacityTests.asyncTearDown
    clarify = capacity.AttentionCapacityTests.clarify
    deliver = capacity.AttentionCapacityTests.deliver

    async def start_long(self, count=2, **fields):
        for index in range(count):
            item = self.service.capture('felix', 'long-' + str(index), 'Preparación privada ' + str(index))['item']
            self.long_items.add(item['id'])
            self.clarify(item, 'long-meaning-' + str(index), priority=0, **fields)
        await self.worker.tick()
        self.assertEqual(self.control.budget()['active'], count)

    async def short(self, *, window=30):
        await self.deliver(capacity.message(600, 'Compara 42 y 57 y entrega recomendación.'))
        item = next(i for i in self.service.query() if i.get('source', {}).get('message_id') == 600)
        return self.clarify(item, 'short-meaning', priority=100,
            decision_at=(datetime.now(timezone.utc) + timedelta(seconds=window)).isoformat())

    def restart(self):
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)

    async def ticks(self, count=5):
        for _ in range(count):
            await self.worker.tick()
            self.native.sample()

    def record(self):
        records = self.control._load().get('attention_displacements', {})
        self.assertEqual(len(records), 1, records)
        return next(iter(records.values()))

    def assert_resumed_once(self):
        record = self.record()
        self.assertEqual(record['status'], 'resumed', record)
        old, new = (self.control.get_job(record[k]) for k in ('old_job_id', 'new_job_id'))
        self.assertTrue(old['terminal'])
        self.assertEqual(old['observations'][-1]['native_status'], 'cancelled')
        self.assertEqual(new['integration'], 'integrated')
        self.assertEqual(self.service.get_item(old['item_id'])['status'], 'done')
        self.assertEqual(self.native.submissions.count(new['id']), 1)
        self.assertEqual(self.native.stops.count(old['id']), 1)
        self.assertEqual(record['period'], self.control.config)
        self.assertGreaterEqual(self.control.budget()['committed_cost_usd'],
            sum(j['charged_cost_usd'] for j in self.control._load()['jobs'].values()))
        return old, new

    async def test_material_and_authenticated_progress_survive_displacement_and_return(self):
        await self.start_long()
        originals = {}
        # Either equal-priority preparation is a valid victim. Give both real
        # progress so this assertion does not depend on random job-id ordering.
        for old_id in self.native.submissions:
            job = self.control.get_job(old_id)
            item = self.service.get_item(job['item_id'])
            receipt = await self.native.client.call('gtd_command', dict(job_id=old_id, command=dict(
                operation_id='partial-long-material:' + old_id, action='put_material', item_id=item['id'],
                expected_version=item['version'], fields=dict(content='Primer cálculo comprobado: 57 - 42 = 15.'))))
            self.assertEqual(receipt['status'], 'applied', receipt)
            originals[old_id] = self.service.materials(item['id'])[0]
        await self.short()
        await self.ticks()
        old, new = self.assert_resumed_once()
        original = originals[old['id']]
        item = self.service.get_item(old['item_id'])
        self.assertEqual(len(self.service.materials(item['id'])), 2)
        self.assertEqual(self.service.materials(item['id'])[0], original)
        self.assertTrue(any(p['operation_id'] == 'partial-long-material:' + old['id'] for p in old['progress']))
        self.assertIn(original['original']['sha256'], self.worker._state()['runs'][new['id']]['prompt'])
        self.assertEqual(self.service.read_material_file(item['id'], original['id'], original['version'])['data'],
                         'Primer cálculo comprobado: 57 - 42 = 15.'.encode())
        self.restart()
        await self.ticks(2)
        self.assert_resumed_once()

    async def test_restart_after_intention_before_stop_recovers_once(self):
        await self.start_long()
        await self.short()
        begin = self.control._begin_attention_displacement
        def interrupted(*args):
            receipt = begin(*args)
            self.assertEqual(receipt['status'], 'recorded')
            raise RuntimeError('crash after intention')
        with patch.object(self.control, '_begin_attention_displacement', interrupted):
            with self.assertRaisesRegex(RuntimeError, 'crash after intention'):
                await self.worker.tick()
        self.assertEqual(self.native.stops, [])
        self.assertEqual(self.record()['stop_delivery'], 'intent')
        self.restart()
        await self.ticks()
        self.assert_resumed_once()

    async def test_lost_stop_response_reconciles_without_duplicate_stop(self):
        await self.start_long()
        await self.short()
        stop = self.native.stop
        async def lost(job_id):
            await stop(job_id)
            raise TimeoutError('lost native stop response')
        with patch.object(self.native, 'stop', lost):
            await self.worker.tick()
        self.assertEqual(self.record()['stop_delivery'], 'uncertain')
        self.restart()
        await self.ticks()
        self.assert_resumed_once()

    async def test_crash_before_stop_effect_does_not_guess_replay_or_release_capacity(self):
        await self.start_long()
        short = await self.short()
        save = self.control._attention_stop_delivery
        def interrupted(job_id, phase):
            save(job_id, phase)
            if phase == 'sending':
                raise RuntimeError('crash before stop effect')
        with patch.object(self.control, '_attention_stop_delivery', interrupted):
            with self.assertRaisesRegex(RuntimeError, 'crash before stop effect'):
                await self.worker.tick()
        self.restart()
        await self.ticks(3)
        self.assertEqual(self.native.stops, [])
        self.assertEqual(self.control.budget()['active'], 2)
        self.assertFalse(self.service.materials(short['id']))
        self.assertNotIn('new_job_id', self.record())

    async def test_unconfirmed_stop_keeps_slots_and_returns_one_concrete_limit(self):
        await self.start_long()
        short = await self.short()
        self.native.blocked_stops.update(self.native.submissions)
        await self.worker.tick()
        future = datetime.now(timezone.utc) + timedelta(seconds=60)
        class Later(datetime):
            @classmethod
            def now(cls, tz=None):
                return future
        with patch('gtd_felix.orchestration.datetime', Later):
            for _ in range(3):
                self.restart()
                await self.worker.tick()
        self.assertEqual(self.control.budget()['active'], 2)
        self.assertEqual(len(self.native.stops), 1)
        self.assertFalse(self.service.materials(short['id']))
        self.assertNotIn('new_job_id', self.record())
        notices = [e for e in self.service.pending_events('gtd-notification', 'local')
                   if e['payload']['item_id'] == short['id']]
        self.assertEqual(len(notices), 1)
        self.assertIn('no puedo acreditar la detención', notices[0]['payload']['text'])

    async def continuation_crash(self, after_commit):
        await self.start_long()
        await self.short()
        reserve = self.control._reserve_attention_continuation
        def interrupted(*args):
            if after_commit:
                receipt = reserve(*args)
                self.assertEqual(receipt['status'], 'reserved', receipt)
            raise RuntimeError('crash at continuation admission')
        with patch.object(self.control, '_reserve_attention_continuation', interrupted):
            with self.assertRaisesRegex(RuntimeError, 'crash at continuation admission'):
                await self.ticks()
        before = self.record().get('new_job_id')
        self.restart()
        await self.ticks()
        _, new = self.assert_resumed_once()
        if after_commit:
            self.assertEqual(new['id'], before)

    async def test_restart_before_continuation_reservation(self):
        await self.continuation_crash(False)

    async def test_restart_after_atomic_continuation_reservation_before_dispatch(self):
        await self.continuation_crash(True)

    async def test_human_correction_after_stop_prevents_old_work_continuation(self):
        await self.start_long()
        await self.short()
        await self.worker.tick()
        record = self.record()
        item = self.service.get_item(record['item_id'])
        changed = self.service.execute('felix', dict(operation_id='human-new-direction', action='edit',
            item_id=item['id'], expected_version=item['version'], fields=dict(title='Cambió el encargo humano')))
        self.assertEqual(changed['status'], 'applied')
        self.restart()
        await self.ticks()
        self.assertEqual(self.record()['blocker'], 'attention_input_changed')
        self.assertNotIn('new_job_id', self.record())
        self.assertFalse(self.service.materials(item['id']))

    async def test_stop_human_after_new_reservation_cancels_undispatched_new_job(self):
        await self.start_long()
        await self.short()
        reserve = self.control._reserve_attention_continuation
        def stopped(actor, old_id):
            receipt = reserve(actor, old_id)
            self.assertEqual(receipt['status'], 'reserved', receipt)
            result = self.control.request_stop('felix', 'human-stop-old-family', old_id)
            self.assertEqual(result['status'], 'stop_requested')
            return receipt
        with patch.object(self.control, '_reserve_attention_continuation', stopped):
            await self.ticks()
        self.restart()
        await self.ticks(2)
        record = self.record()
        self.assertEqual(record['status'], 'cancelled')
        new = self.control.get_job(record['new_job_id'])
        self.assertTrue(new['terminal'])
        self.assertEqual(new['terminal_resolution']['kind'], 'cancelled_before_dispatch')
        self.assertNotIn(new['id'], self.native.submissions)
        self.assertFalse(self.service.materials(record['item_id']))

    async def test_stop_by_principal_outside_internal_context_is_not_technical(self):
        await self.start_long()
        await self.short()
        await self.worker.tick()
        record = self.record()
        result = self.control.request_stop('gtd-felix', 'gtd-attention-stop:forged-label', record['old_job_id'])
        self.assertEqual(result['status'], 'stop_requested')
        self.restart()
        await self.ticks()
        self.assertEqual(self.record()['status'], 'cancelled')
        self.assertNotIn('new_job_id', self.record())

    async def test_human_stop_old_family_after_new_dispatch_blocks_new_effects(self):
        self.native.finish_resumed = False
        await self.start_long()
        await self.short()
        await self.ticks(4)
        record = self.record()
        new_id = record['new_job_id']
        self.assertIn(new_id, self.native.submissions)
        self.control.request_stop('felix', 'late-human-stop', record['old_job_id'])
        item = self.service.get_item(record['item_id'])
        result = await self.native.client.call('gtd_command', dict(job_id=new_id, command=dict(
            operation_id='forbidden-late-output', action='put_material', item_id=item['id'],
            expected_version=item['version'], fields=dict(content='Must not be accepted'))))
        self.assertEqual(result['status'], 'rejected', result)
        self.restart()
        await self.ticks(3)
        self.assertTrue(self.control.get_job(new_id)['terminal'])
        self.assertFalse(self.service.materials(item['id']))
        self.assertEqual(self.native.submissions.count(new_id), 1)

    async def test_insufficient_period_budget_never_stops_or_renews_to_admit(self):
        self.control.config['max_cost_usd'] = 10  # two reservations plus recovery, no extra cost
        await self.start_long()
        short = await self.short()
        before = self.control._load()['config']
        await self.ticks(3)
        self.assertEqual(self.native.stops, [])
        self.assertEqual(self.control.budget()['active'], 2)
        self.assertEqual(self.control._load()['config'], before)
        self.assertFalse(self.service.materials(short['id']))
        self.assertTrue(any(g['blocker'] == 'budget_unavailable' for g in self.service.review_state()['operational_gaps']))

    async def test_source_priority_cannot_displace_owner_work(self):
        await self.start_long()
        item = self.service.capture('felix', 'external-urgency', 'Urgencia recibida de tercero',
            source=dict(provider='gmail', account='synthetic', revision='1'))['item']
        result = self.service.execute('gtd-felix', dict(operation_id='external-interpretation', action='clarify',
            item_id=item['id'], expected_version=item['version'], fields=dict(kind='reference', commitment='proposed',
                priority=100, decision_at=(datetime.now(timezone.utc) + timedelta(seconds=30)).isoformat())))
        self.assertEqual(result['status'], 'applied', result)
        await self.ticks(3)
        self.assertEqual(self.native.stops, [])
        self.assertFalse(self.service.materials(item['id']))
        self.assertEqual(self.control.budget()['active'], 2)

    async def test_equal_or_earlier_window_is_not_postponable(self):
        earlier = (datetime.now(timezone.utc) + timedelta(seconds=10)).isoformat()
        await self.start_long(decision_at=earlier)
        short = await self.short()
        await self.ticks(3)
        self.assertEqual(self.native.stops, [])
        self.assertFalse(self.service.materials(short['id']))

    async def test_entire_family_must_stop_before_brief_work_is_admitted(self):
        self.control.config['max_descendants'] = 1
        self.config['reservation']['max_descendants'] = 1
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        await self.start_long(count=1)
        root_id = self.native.submissions[0]
        root = self.control.get_job(root_id)
        child = self.control.reserve('gtd-felix', 'synthetic-child', dict(
            item_id=root['item_id'], expected_version=root['expected_version'], mandate_id=None,
            capability='prepare_private', bot_id='principal', purpose='Private child calculation', scope=root['scope'],
            max_cost_usd=1, max_runtime_seconds=50, max_retries=0, max_descendants=0,
            parent_job_id=root_id, orchestrated=True))
        self.assertEqual(child['status'], 'reserved', child)
        await self.worker.tick()
        child_id = child['job_id']
        self.assertIn(child_id, self.native.submissions)
        self.assertEqual(self.control.budget()['active'], 2)
        self.native.blocked_stops.add(child_id)
        short = await self.short()
        await self.ticks(3)
        self.assertTrue(self.control.get_job(root_id)['terminal'])
        self.assertFalse(self.control.get_job(child_id)['terminal'])
        self.assertEqual(self.control.budget()['active'], 1)
        self.assertFalse(any(j['item_id'] == short['id'] for j in self.control._load()['jobs'].values()))
        self.assertEqual(self.native.stops, [root_id])
        # Only a real terminal observation of the remaining synthetic child releases the barrier.
        self.native.runs[child_id] = 'cancelled'
        self.restart()
        await self.ticks()
        self.assertEqual(self.service.get_item(short['id'])['status'], 'done')
        self.assert_resumed_once()

    async def test_forwarded_urgency_does_not_gain_owner_priority(self):
        await self.start_long()
        await self.deliver(capacity.message(601, 'Decisión urgente de un tercero',
            forward_origin=dict(type='hidden_user', sender_user_name='Synthetic sender')))
        item = next(i for i in self.service.query() if i.get('source', {}).get('message_id') == 601)
        result = self.service.execute('gtd-felix', dict(operation_id='forwarded-priority', action='clarify',
            item_id=item['id'], expected_version=item['version'], fields=dict(kind='reference', commitment='proposed',
                priority=100, decision_at=(datetime.now(timezone.utc) + timedelta(seconds=30)).isoformat())))
        self.assertEqual(result['status'], 'applied', result)
        await self.ticks(3)
        self.assertFalse(self.control._load().get('attention_displacements'))
        self.assertEqual(self.native.stops, [])

    async def test_changed_source_invalidates_principal_window_provenance(self):
        await self.start_long()
        short = await self.short()
        changed = self.service.revise_source('felix', 'corrected-short-source', short['id'],
            dict(provider='telegram', revision='2'), text='La ventana anterior ya no corresponde.')
        self.assertEqual(changed['status'], 'applied')
        await self.ticks(3)
        self.assertIsNone(self.control._attention_window(self.service.get_item(short['id'])))
        self.assertEqual(self.native.stops, [])

    async def test_owner_can_correct_priority_without_losing_direct_intent_window(self):
        await self.start_long()
        short = await self.short()
        edited = self.service.execute('felix', dict(operation_id='owner-priority-correction', action='edit',
            item_id=short['id'], expected_version=short['version'], fields=dict(priority=50)))
        self.assertEqual(edited['status'], 'applied')
        await self.ticks()
        self.assertEqual(self.service.get_item(short['id'])['priority'], 50)
        self.assertEqual(self.service.get_item(short['id'])['status'], 'done')
        self.assert_resumed_once()

    async def test_changed_dependency_prevents_resuming_old_preparation(self):
        source = self.service.capture('felix', 'reference-data', 'Dato inicial')['item']
        for event in self.worker._events():
            self.service.mark_event(event['event_key'], 'done')
        await self.start_long(source_versions={source['id']: len(source['source_revisions'])})
        await self.short()
        await self.worker.tick()
        changed = self.service.revise_source('felix', 'correct-reference', source['id'],
            dict(provider='synthetic', revision='2'), text='Dato corregido')
        self.assertEqual(changed['status'], 'applied')
        self.restart()
        await self.ticks()
        self.assertNotIn('new_job_id', self.record())
        self.assertEqual(self.record()['status'], 'cancelled')

    async def test_consumed_cost_is_not_refunded_to_force_continuation(self):
        self.control.config['max_cost_usd'] = 14
        self.native.terminal_cost_usd = 4
        await self.start_long()
        short = await self.short()
        await self.ticks()
        self.assertEqual(self.service.get_item(short['id'])['status'], 'done')
        record = self.record()
        self.assertNotIn('new_job_id', record)
        self.assertEqual(record['blocker'], 'budget_exhausted')
        self.assertEqual(self.control.budget()['remaining_cost_usd'], 0)
        self.assertEqual(self.control.get_job(record['old_job_id'])['charged_cost_usd'], 4)
        self.restart()
        await self.ticks(2)
        self.assertNotIn('new_job_id', self.record())

    async def test_period_expiry_does_not_renew_displaced_work_budget(self):
        await self.start_long()
        await self.short()
        with patch.object(self.control, '_reserve_attention_continuation', side_effect=RuntimeError('hold continuation')):
            with self.assertRaisesRegex(RuntimeError, 'hold continuation'):
                await self.ticks()
        record = self.record()
        future = datetime.now(timezone.utc) + timedelta(hours=2)
        class Later(datetime):
            @classmethod
            def now(cls, tz=None):
                return future
        with patch('gtd_felix.control.datetime', Later):
            result = self.control._reserve_attention_continuation('gtd-felix', record['old_job_id'])
        self.assertEqual(result['error'], 'budget_period_inactive')
        self.assertEqual(self.control._load()['config'], record['period'])
        self.assertNotIn('new_job_id', self.record())

    async def test_reservation_transaction_rollback_leaves_no_orphan_new_job(self):
        await self.start_long()
        await self.short()
        save = self.control._save
        def fail_atomic_commit(state):
            if any(r.get('new_job_id') for r in state.get('attention_displacements', {}).values()):
                raise RuntimeError('continuation commit interrupted')
            return save(state)
        with patch.object(self.control, '_save', fail_atomic_commit):
            with self.assertRaisesRegex(RuntimeError, 'continuation commit interrupted'):
                await self.ticks()
        self.assertNotIn('new_job_id', self.record())
        self.assertEqual(len(self.control._load()['jobs']), 3)
        self.restart()
        await self.ticks()
        self.assert_resumed_once()
        self.assertEqual(len(self.control._load()['jobs']), 4)

    async def test_revoked_explicit_mandate_is_not_replaced_by_standing_preparation(self):
        mandates = {}
        for index in range(2):
            item = self.service.capture('felix', 'mandated-' + str(index), 'Preparación explícita ' + str(index))['item']
            self.long_items.add(item['id'])
            item = self.clarify(item, 'mandated-meaning-' + str(index), priority=0)
            grant = self.service.execute('felix', dict(operation_id='grant-' + str(index), action='grant_mandate',
                item_id=item['id'], expected_version=item['version'], fields=dict(scope_item_id=item['id'],
                    capabilities=['prepare_private'], actors=['gtd-felix'], completion_criteria='Material comprobado')))
            self.assertEqual(grant['status'], 'applied')
            mandates[item['id']] = grant['mandate']['id']
            receipt = self.control.reserve('gtd-felix', 'mandated-run-' + str(index), dict(
                **self.config['reservation'], item_id=item['id'], expected_version=grant['item']['version'],
                mandate_id=grant['mandate']['id'], capability='prepare_private', bot_id='principal',
                purpose='Preparación privada bajo mandato explícito', scope='Solo preparar comparación'))
            self.assertEqual(receipt['status'], 'reserved', receipt)
            self.service.ingest_event(dict(provider='gtd-dispatch', account='local', external_id=receipt['job_id'],
                revision='1', payload=dict(job_id=receipt['job_id'])))
        await self.worker.tick()
        self.assertEqual(self.control.budget()['active'], 2)
        await self.short()
        await self.worker.tick()
        record = self.record()
        item = self.service.get_item(record['item_id'])
        revoked = self.service.execute('felix', dict(operation_id='revoke-displaced', action='revoke_mandate',
            item_id=item['id'], expected_version=item['version'], fields=dict(mandate_id=mandates[item['id']])))
        self.assertEqual(revoked['status'], 'applied')
        self.restart()
        await self.ticks()
        self.assertNotIn('new_job_id', self.record())
        self.assertEqual(self.record()['status'], 'cancelled')
        self.assertFalse(self.service.materials(item['id']))

    async def test_new_owner_direction_after_cancelled_stop_gets_fresh_admission(self):
        await self.start_long()
        await self.short()
        await self.worker.tick()
        record = self.record()
        self.control.request_stop('felix', 'cancel-old-purpose', record['old_job_id'])
        await self.ticks(3)
        self.assertNotIn('new_job_id', self.record())
        item = self.service.get_item(record['item_id'])
        self.native.finish_items.add(item['id'])
        # A corrected human meaning permits fresh private preparation. The
        # existing domain correctly requires a new mandate to assess it done.
        self.native.material_only_items.add(item['id'])
        receipt = self.service.execute('felix', dict(operation_id='new-owner-direction', action='edit',
            item_id=item['id'], expected_version=item['version'],
            fields=dict(title='Nueva preparación: completa la comparación corregida', completion_criteria='Comparación corregida comprobada')))
        self.assertEqual(receipt['status'], 'applied')
        self.restart()
        await self.ticks()
        fresh = [j for j in self.control._load()['jobs'].values()
                 if j['item_id'] == item['id'] and j['id'] != record['old_job_id']
                 and j['purpose'] == 'GTD revisión y preparación']
        self.assertEqual(len(fresh), 1)
        self.assertNotIn('attention_origin', fresh[0])
        self.assertEqual(fresh[0]['integration'], 'integrated')
        self.assertEqual(self.service.get_item(item['id'])['status'], 'active')
        self.assertEqual(len(self.service.materials(item['id'])), 1)
        self.assertEqual(self.record()['status'], 'cancelled')
        self.assertNotIn('new_job_id', self.record())
        self.restart()
        await self.ticks(2)
        self.assertEqual(self.native.submissions.count(fresh[0]['id']), 1)

    async def held_before_stop(self):
        await self.start_long()
        await self.short()
        begin = self.control._begin_attention_displacement
        def held(*args):
            receipt = begin(*args)
            self.assertEqual(receipt['status'], 'recorded')
            raise RuntimeError('hold before stop')
        with patch.object(self.control, '_begin_attention_displacement', held):
            with self.assertRaisesRegex(RuntimeError, 'hold before stop'):
                await self.worker.tick()

    async def test_restore_gate_does_not_send_pending_attention_stop(self):
        await self.held_before_stop()
        with self.service.store.transaction():
            self.service._set_meta('recovery_required', True)
        self.restart()
        await self.ticks(2)
        # Existing recovery safety may stop another active job. It must not
        # send this pending priority displacement or admit/dispatch new work.
        self.assertNotIn(self.record()['old_job_id'], self.native.stops)
        self.assertEqual(self.record()['stop_delivery'], 'intent')
        self.assertEqual(len(self.native.submissions), 2)
        self.assertEqual(len(self.control._load()['jobs']), 2)

    async def test_disabled_worker_does_not_send_pending_attention_stop(self):
        await self.held_before_stop()
        self.config.pop('reservation')
        self.restart()
        await self.ticks(2)
        self.assertEqual(self.native.stops, [])
        self.assertEqual(self.record()['stop_delivery'], 'intent')

    async def test_other_actor_does_not_change_displacement_or_attempt_continuation(self):
        await self.held_before_stop()
        before = self.record()
        self.config['actor'] = 'felix'
        self.restart()
        await self.ticks(2)
        self.assertEqual(self.record(), before)
        self.assertEqual(self.native.stops, [])

    async def reserved_continuation_gate(self, gate):
        await self.start_long()
        await self.short()
        reserve = self.control._reserve_attention_continuation
        def held(*args):
            receipt = reserve(*args)
            self.assertEqual(receipt['status'], 'reserved')
            raise RuntimeError('hold after continuation reservation')
        with patch.object(self.control, '_reserve_attention_continuation', held):
            with self.assertRaisesRegex(RuntimeError, 'hold after continuation reservation'):
                await self.ticks()
        new_id = self.record()['new_job_id']
        self.worker._recover_attention_runs(self.worker._state())
        if gate == 'disabled':
            self.config.pop('reservation')
        elif gate == 'restore':
            with self.service.store.transaction():
                self.service._set_meta('recovery_required', True)
        else:
            self.config['actor'] = 'felix'
        self.restart()
        await self.ticks(2)
        self.assertNotIn(new_id, self.native.submissions)
        self.assertEqual(self.control.get_job(new_id)['delivery'], 'deferred')

    async def test_reserved_continuation_is_not_dispatched_by_disabled_worker(self):
        await self.reserved_continuation_gate('disabled')

    async def test_reserved_continuation_is_not_dispatched_during_restore(self):
        await self.reserved_continuation_gate('restore')

    async def test_reserved_continuation_is_not_dispatched_by_another_actor(self):
        await self.reserved_continuation_gate('other_actor')
