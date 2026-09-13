"""Civil-day subscription budget: real Store, injected UTC clock, no provider calls."""
import copy
from datetime import datetime, timezone, timedelta
import json
from pathlib import Path
import sys
import unittest
from zoneinfo import ZoneInfo

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from gtd_felix.control import ExecutionControl
import test_control as fixed


class DailyBudgetTest(unittest.TestCase):
    # Reuse synthetic domain fixture without inheriting its fixed-period test suite.
    setUp = fixed.ControlTest.setUp
    tearDown = fixed.ControlTest.tearDown
    request = fixed.ControlTest.request
    reserve = fixed.ControlTest.reserve
    native = fixed.ControlTest.native
    observation = fixed.ControlTest.observation
    finish = fixed.ControlTest.finish

    def daily(self):
        self.now = datetime(2026, 9, 12, 15, tzinfo=timezone.utc)
        self.config = {k: v for k, v in self.config.items() if k not in {'period_start', 'period_seconds'}}
        self.config.update(budget_mode='daily_subscription', timezone='America/Santiago',
            max_active=1, max_cost_usd=2, recovery_cost_usd=0,
            max_runtime_seconds=7200, recovery_runtime_seconds=0)
        self.control = ExecutionControl(self.service, self.config, clock=lambda: self.now)

    def test_unknown_cost_does_not_stop_third_job_and_budget_is_json(self):
        self.daily()
        for i in range(4):
            job = self.reserve(str(i), max_cost_usd=1)
            self.finish(job, cost_usd=None, runtime_seconds=100)
        budget = self.control.budget()
        self.assertEqual(budget['remaining_runtime_seconds'], 6800)
        self.assertEqual(budget['committed_cost_usd'], 4)
        self.assertIsNone(budget['remaining_cost_usd'])
        self.assertFalse(budget['cost_control'])
        json.dumps(budget, allow_nan=False)

    def test_migration_requires_owner_hash_terminal_and_is_idempotent(self):
        job = self.reserve()
        old_config = copy.deepcopy(self.control.config)
        digest = self.control.policy_hash(old_config)
        self.daily()
        self.assertEqual(self.control.reserve('gtd-felix', 'wrong-config', self.request())['error'], 'budget_configuration_changed')
        self.assertEqual(self.control.transition_budget_policy('gtd-felix', 'not-owner', digest)['error'], 'actor_not_owner')
        self.assertEqual(self.control.transition_budget_policy('felix', 'bad-hash', 'x')['error'], 'budget_policy_hash_mismatch')
        self.assertEqual(self.control.transition_budget_policy('felix', 'busy', digest)['error'], 'budget_transition_requires_terminal_jobs')
        self.finish(job, runtime_seconds=250)  # Historical overrun must not poison a new day.
        before = copy.deepcopy(self.control._load())
        receipt = self.control.transition_budget_policy('felix', 'transition', digest)
        self.assertEqual(receipt['status'], 'applied', receipt)
        self.assertTrue(self.control.transition_budget_policy('felix', 'transition', digest)['duplicate'])
        after = self.control._load()
        expected = dict(before['jobs'][job], budget_period_id=receipt['historical_period_id'])
        self.assertEqual(after['jobs'][job], expected)
        for key, operation in before['operations'].items():
            self.assertEqual(after['operations'][key], operation)
        self.assertEqual(len(after['policy_transitions']), 1)
        self.reserve('daily-first')
        self.assertEqual(self.control.budget()['committed_runtime_seconds'], 200)

    def test_midnight_restart_and_uncertain_global_slot(self):
        self.daily()
        self.now = datetime(2026, 9, 13, 2, 59, tzinfo=timezone.utc)
        job = self.reserve('old')
        period_id = self.control.get_job(job)['budget_period_id']
        self.control.observe(job, self.observation(job, native_status='uncertain', terminal=False, runtime_seconds=10))
        self.now += timedelta(minutes=2)
        self.control = ExecutionControl(self.service, self.config, clock=lambda: self.now)
        self.assertEqual(self.control.budget()['remaining_runtime_seconds'], 7200)
        self.assertEqual(self.control.budget()['active'], 1)
        self.assertEqual(self.control.validate(job, 'local_work')['reason'], 'job_budget_period_expired')
        self.assertEqual(self.control.reserve('gtd-felix', 'new-busy', self.request(purpose='new'))['error'], 'concurrency_exhausted')
        self.finish(job, runtime_seconds=250)
        self.assertEqual(self.control.get_job(job)['budget_period_id'], period_id)
        new = self.reserve('new', purpose='new')
        self.assertNotEqual(self.control.get_job(new)['budget_period_id'], period_id)
        self.assertEqual(len(self.control._load()['periods']), 2)
        self.assertEqual(len(self.control.get_job(job)['observations']), 2)

    def test_live_overrun_blocks_until_confirmed_terminal_then_charges_actual(self):
        self.daily()
        job = self.reserve()
        for status in ('running', 'uncertain', 'not_found'):
            self.finish(job, native_status=status, terminal=False, runtime_seconds=201)
            self.assertEqual(self.control.reserve('gtd-felix', 'blocked-' + status,
                self.request())['error'], 'observed_budget_overrun')
        self.finish(job, native_status='cancelled', runtime_seconds=217)
        restarted = ExecutionControl(self.service, self.config, clock=lambda: self.now)
        self.assertEqual(restarted.budget()['committed_runtime_seconds'], 217)
        self.assertEqual(restarted.budget()['remaining_runtime_seconds'], 6983)
        receipt = restarted.reserve('gtd-felix', 'after-terminal', self.request())
        self.assertEqual(receipt['status'], 'reserved', receipt)
        self.assertEqual(len(restarted.get_job(job)['observations']), 4)
        self.assertFalse(restarted.validate(job, 'local_work')['allowed'])

    def test_terminal_overrun_never_restores_consumed_daily_allowance(self):
        self.daily()
        job = self.reserve()
        self.finish(job, runtime_seconds=7201)
        self.assertEqual(self.control.budget()['committed_runtime_seconds'], 7201)
        self.assertEqual(self.control.budget()['remaining_runtime_seconds'], 0)
        self.assertEqual(self.control.reserve('gtd-felix', 'exhausted-overrun',
            self.request())['error'], 'budget_exhausted')
        self.now += timedelta(days=1)
        self.reserve('tomorrow')

    def test_exhaustion_preserves_capture_and_new_day_balance(self):
        self.daily()
        for i in range(18):
            job = self.reserve(str(i), max_runtime_seconds=400)
            self.finish(job, cost_usd=None, runtime_seconds=400)
        self.assertEqual(self.control.budget()['remaining_runtime_seconds'], 0)
        self.assertEqual(self.control.reserve('gtd-felix', 'exhausted', self.request())['error'], 'budget_exhausted')
        item = self.service.capture('felix', 'still-capture', 'preserved while exhausted')['item']
        self.assertEqual(self.service.get_item(item['id'])['text'], 'preserved while exhausted')
        self.now += timedelta(days=1)
        self.assertEqual(self.control.budget()['remaining_runtime_seconds'], 7200)
        self.reserve('return')

    def test_santiago_calendar_days_include_23_and_25_hour_days(self):
        self.daily()
        for local_date, expected_hours in [('2026-09-06', 23), ('2026-04-04', 25), ('2026-09-12', 24)]:
            self.now = datetime.fromisoformat(local_date + 'T12:00:00').replace(tzinfo=ZoneInfo('America/Santiago'))
            period = self.control._period(self.config)
            duration = (datetime.fromisoformat(period['end']).astimezone(timezone.utc)
                        - datetime.fromisoformat(period['start']).astimezone(timezone.utc)).total_seconds()
            self.assertEqual(duration, expected_hours * 3600, period)
            self.assertEqual(self.control.budget()['remaining_runtime_seconds'], 7200)

    def test_dst_rollover_happens_at_real_civil_boundary(self):
        self.daily()
        for boundary in ('2026-09-06T04:00:00+00:00', '2026-04-05T04:00:00+00:00'):
            self.now = datetime.fromisoformat(boundary) - timedelta(seconds=1)
            previous = self.control._period(self.config)
            self.now += timedelta(seconds=1)
            current = self.control._period(self.config)
            self.assertNotEqual(previous['id'], current['id'])
            self.assertEqual(datetime.fromisoformat(previous['end']), self.now)
            self.assertEqual(datetime.fromisoformat(current['start']), self.now)
            self.assertEqual(datetime.fromisoformat(current['start']).astimezone(ZoneInfo('America/Santiago')).isoformat(),
                             current['start'])

    def test_descendants_keep_root_period_and_time_allocation(self):
        self.daily()
        root = self.reserve(max_cost_usd=1, max_runtime_seconds=200)
        child = self.reserve('child', parent_job_id=root, defer_when_busy=True,
            max_cost_usd=3, max_runtime_seconds=50, max_descendants=0)
        self.assertEqual(self.control.get_job(root)['budget_period_id'], self.control.get_job(child)['budget_period_id'])
        self.assertEqual(self.control.budget()['committed_runtime_seconds'], 200)
        self.now += timedelta(days=1)
        discarded = self.control.activate_deferred(child)
        self.assertEqual(discarded['status'], 'discarded', discarded)
        self.assertEqual(self.control.budget()['active'], 1)

    def test_policy_changes_and_malformed_modes_do_not_expand_authority(self):
        self.daily()
        job = self.reserve()
        self.finish(job)
        for change in [dict(max_runtime_seconds=14400), dict(timezone='Europe/Berlin'), dict(max_active=2),
                       dict(period_start='2099-01-01T00:00:00+00:00'), dict(budget_mode='future'),
                       dict(max_retries=0)]:
            control = ExecutionControl(self.service, dict(self.config, **change), clock=lambda: self.now)
            result = control.reserve('gtd-felix', 'change-' + str(change), self.request())
            self.assertEqual(result['status'], 'rejected', result)
        self.assertEqual(self.control._load()['config'], self.config)

    def test_descendant_cannot_reuse_expired_root(self):
        self.daily()
        root = self.reserve()
        self.now += timedelta(days=1)
        result = self.control.reserve('gtd-felix', 'descendant', self.request(parent_job_id=root, defer_when_busy=True))
        self.assertEqual(result['error'], 'job_budget_period_expired')
        self.assertEqual(len(self.control._load()['jobs']), 1)


class DailyHTTPTest(unittest.IsolatedAsyncioTestCase):
    async def test_transition_owner_only_and_replay(self):
        from aiohttp import web, ClientSession
        from test_application import config, OWNER, PRINCIPAL
        from gtd_felix.application import create_app
        fixture = DailyBudgetTest()
        fixture.setUp()
        runner = None
        try:
            job = fixture.reserve()
            fixture.finish(job)
            digest = fixture.control.policy_hash(fixture.control.config)
            fixture.daily()
            runner = web.AppRunner(create_app(fixture.service, fixture.control, config(fixture.root)))
            await runner.setup()
            site = web.TCPSite(runner, '127.0.0.1', 0)
            await site.start()
            url = 'http://127.0.0.1:' + str(site._server.sockets[0].getsockname()[1]) + '/v1/control/transition_budget_policy'
            payload = dict(operation_id='http-transition', expected_hash=digest)
            async with ClientSession() as session:
                async with session.post(url, json=payload, headers={'Authorization': 'Bearer ' + PRINCIPAL}) as response:
                    self.assertEqual(response.status, 403)
                for duplicate in (False, True):
                    async with session.post(url, json=payload, headers={'Authorization': 'Bearer ' + OWNER}) as response:
                        self.assertEqual(response.status, 200)
                        result = await response.json()
                        self.assertEqual(result['status'], 'applied', result)
                        self.assertEqual(result.get('duplicate', False), duplicate)
        finally:
            if runner:
                await runner.cleanup()
            fixture.tearDown()

class DailyRecoveryTest(unittest.TestCase):
    setUp = DailyBudgetTest.setUp
    tearDown = DailyBudgetTest.tearDown
    request = DailyBudgetTest.request
    reserve = DailyBudgetTest.reserve
    native = DailyBudgetTest.native
    observation = DailyBudgetTest.observation
    finish = DailyBudgetTest.finish
    daily = DailyBudgetTest.daily
    def test_expire_never_dispatched_requires_durable_negative_evidence(self):
        self.daily()
        job = self.reserve()
        self.now += timedelta(days=1)
        with self.service.store.transaction():
            self.service._set_meta('hermes:intent:' + job, {'delivery': 'intent'})
        self.assertEqual(self.control.expire_undispatched(job)['error'], 'dispatch_absence_not_proven')
        self.assertEqual(self.control.budget()['active'], 1)
        with self.service.store.transaction():
            self.service.store.db.execute('DELETE FROM metadata WHERE key=?', ('hermes:intent:' + job,))
            self.service._set_meta('codex:job:' + job, {'delivery': 'intent'})
        self.assertEqual(self.control.expire_undispatched(job)['error'], 'dispatch_absence_not_proven')
        with self.service.store.transaction():
            self.service.store.db.execute('DELETE FROM metadata WHERE key=?', ('codex:job:' + job,))
        receipt = self.control.expire_undispatched(job)
        self.assertEqual(receipt['status'], 'discarded', receipt)
        self.assertEqual(receipt['job']['observations'], [])
        self.assertEqual(receipt['job']['terminal_resolution']['native_effect'], 'not_dispatched')
        self.assertEqual(self.control.budget()['active'], 0)
        self.reserve('replanned')

    def test_owner_daily_policy_transition_preserves_periods(self):
        self.daily()
        job = self.reserve()
        self.finish(job)
        old_period = self.control.get_job(job)['budget_period_id']
        digest = self.control.policy_hash(self.config)
        self.config = dict(self.config, max_runtime_seconds=600, max_job_runtime_seconds=300)
        self.control = ExecutionControl(self.service, self.config, clock=lambda: self.now)
        blocked = self.control.transition_budget_policy('felix', 'owner-used-day', digest)
        self.assertEqual(blocked['error'], 'budget_transition_requires_unused_day')
        self.now += timedelta(days=1)
        receipt = self.control.transition_budget_policy('felix', 'owner-new-policy', digest)
        self.assertEqual(receipt['status'], 'applied', receipt)
        self.assertEqual(self.control.get_job(job)['budget_period_id'], old_period)
        self.assertIn(old_period, self.control._load()['periods'])
        self.assertEqual(self.control.budget()['remaining_runtime_seconds'], 600)

    def test_displaced_continuation_remains_waiting_without_reusing_expired_authority(self):
        self.daily()
        job = self.reserve()
        self.finish(job, native_status='cancelled')
        with self.service.store.transaction():
            state = self.control._load()
            state['attention_displacements'] = {job: dict(status='waiting', period=copy.deepcopy(self.config),
                budget_period_id=state['jobs'][job]['budget_period_id'], family=[job])}
            self.control._save(state)
        self.now += timedelta(days=1)
        receipt = self.control._reserve_attention_continuation('gtd-felix', job)
        self.assertEqual(receipt['error'], 'attention_budget_period_changed')
        self.assertEqual(self.control._load()['attention_displacements'][job]['status'], 'waiting')
        self.assertEqual(len(self.control._load()['jobs']), 1)


class DailyOrchestrationTest(unittest.IsolatedAsyncioTestCase):
    async def test_expired_intent_is_retained_and_releases_only_never_sent_slot(self):
        from gtd_felix.orchestration import OrchestrationWorker
        fixture = DailyBudgetTest()
        fixture.setUp()
        try:
            fixture.daily()
            job = fixture.reserve()
            worker = OrchestrationWorker(fixture.service, fixture.control, object(),
                {'actor': 'gtd-felix', 'principal_bot_id': 'test-bot', 'reservation': fixture.request()})
            state = worker._state()
            state['runs'][job] = dict(phase='intent', event_keys=[], prompt='synthetic', durable=False)
            worker._save(state)
            fixture.now += timedelta(days=1)
            # Reconstructed controller/worker use the persisted intention after restart.
            fixture.control = ExecutionControl(fixture.service, fixture.config, clock=lambda: fixture.now)
            worker.control = fixture.control
            await worker._advance(worker._state(), job)
            self.assertEqual(worker._state()['runs'][job]['phase'], 'done')
            self.assertEqual(fixture.control.budget()['active'], 0)
            self.assertTrue(fixture.control.get_job(job)['terminal'])
            self.assertEqual(fixture.control.get_job(job)['observations'], [])
            fixture.reserve('replanned')
        finally:
            fixture.tearDown()

    async def test_worker_admits_four_completed_jobs_despite_old_usd_cap(self):
        import test_orchestration as orchestration
        fixture = orchestration.OrchestrationTests()
        await fixture.asyncSetUp()
        try:
            daily = {k: v for k, v in fixture.budget.items() if k not in {'period_start', 'period_seconds'}}
            daily.update(budget_mode='daily_subscription', timezone='America/Santiago',
                max_runtime_seconds=7200, recovery_runtime_seconds=0, max_cost_usd=2, recovery_cost_usd=0)
            fixture.control.config = daily
            original_poll = fixture.native.poll
            async def unknown_cost(job_id):
                # Fixture polls emit a trusted cost observation; replace with unknown
                # before control consumption so runtime follows actual no-cost telemetry.
                original_observe = fixture.control.observe
                def observe(identity, observation):
                    return original_observe(identity, dict(observation, cost_usd=None))
                fixture.control.observe = observe
                try:
                    return await original_poll(job_id)
                finally:
                    fixture.control.observe = original_observe
            fixture.native.poll = unknown_cost
            for i in range(4):
                if i:
                    item = fixture.service.capture('felix', 'extra-' + str(i), 'Synthetic note ' + str(i))['item']
                    fixture.service.ingest_event({'provider': 'gtd-clarification', 'account': 'fixture',
                        'external_id': item['id'], 'revision': '1', 'payload': {'item_id': item['id'], 'reason': 'clarification_pending'}})
                for _ in range(5):
                    await fixture.worker.tick()
            self.assertEqual(len(fixture.native.submissions), 4)
            self.assertGreater(fixture.control.budget()['committed_cost_usd'], 2)
            self.assertEqual(fixture.control.budget()['active'], 0)
        finally:
            await fixture.asyncTearDown()
