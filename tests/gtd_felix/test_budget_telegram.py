"""Deterministic budget reading and capture acknowledgement, no provider work."""
from datetime import datetime, timedelta, timezone
import unittest
from unittest.mock import Mock
import test_telegram as telegram
from gtd_felix.telegram import TelegramAdapter
from gtd_felix.control import ExecutionControl

class BudgetTelegramTest(unittest.IsolatedAsyncioTestCase):
    setUp = telegram.TelegramTests.setUp
    tearDown = telegram.TelegramTests.tearDown
    deliver = telegram.TelegramTests.deliver

    def budget(self, remaining=7200, active=0):
        control = Mock()
        control.config = {'timezone': 'America/Santiago'}
        control.budget.return_value = {'remaining_runtime_seconds': remaining, 'active': active,
            'remaining_cost_usd': None, 'returns_at': '2026-09-14T00:00:00-03:00'}
        self.adapter = TelegramAdapter(self.service, self.client, self.config,
            control=control, reservation_runtime_seconds=600)
        return control

    def work_events(self):
        return self.service.store.db.execute("SELECT COUNT(*) FROM events WHERE provider IN ('gtd-review','gtd-clarification','gtd-dispatch')").fetchone()[0]

    async def test_saldo_is_read_only_and_replay_does_not_create_work(self):
        self.budget()
        await self.deliver(telegram.message(1, '/saldo'))
        self.assertEqual(self.service.query(), [])
        self.assertEqual(self.work_events(), 0)
        self.assertIn('120 min', self.http.sent[-1]['text'])
        self.assertIn('14/09 a las 00:00 (hora de Santiago)', self.http.sent[-1]['text'])
        self.assertNotIn('USD', self.http.sent[-1]['text'])
        sent = len(self.http.sent)
        await self.deliver(telegram.message(1, '/saldo'))
        self.assertEqual(len(self.http.sent), sent)
        self.assertEqual(self.work_events(), 0)

    async def test_insufficient_budget_preserves_capture_with_honest_return(self):
        self.budget(remaining=300)
        await self.deliver(telegram.message(1, 'Preparar una nota'))
        self.assertEqual(len(self.service.query()), 1)
        text = self.http.sent[-1]['text']
        self.assertIn('Guardado.', text)
        self.assertIn('saldo no alcanza', text)
        self.assertIn('14/09 a las 00:00', text)
        self.assertIn('No implica inicio automático', text)

    async def test_busy_is_not_called_exhaustion(self):
        self.budget(remaining=0, active=1)
        await self.deliver(telegram.message(1, 'Conservar esta idea'))
        text = self.http.sent[-1]['text']
        self.assertIn('preparación en curso o por confirmar', text)
        self.assertNotIn('saldo no alcanza', text)
        await self.deliver(telegram.message(2, '/saldo'))
        self.assertIn('turno está ocupado', self.http.sent[-1]['text'])
        self.assertNotIn('saldo no alcanza', self.http.sent[-1]['text'])

    async def test_failure_and_missing_control_never_turn_saldo_into_capture(self):
        control = self.budget()
        control.budget.side_effect = RuntimeError('private detail must not leak')
        await self.deliver(telegram.message(1, '/saldo'))
        self.assertIn('No pude consultar', self.http.sent[-1]['text'])
        self.assertNotIn('private detail', self.http.sent[-1]['text'])
        self.assertEqual(self.service.query(), [])
        await self.deliver(telegram.message(2, 'Guardar pese al fallo'))
        self.assertEqual(len(self.service.query()), 1)
        self.assertIn('Guardado.', self.http.sent[-1]['text'])
        self.adapter = TelegramAdapter(self.service, self.client, self.config)
        await self.deliver(telegram.message(3, '/saldo'))
        self.assertIn('No pude consultar', self.http.sent[-1]['text'])
        self.assertEqual(len(self.service.query()), 1)

    async def test_only_paired_owner_can_read(self):
        control = self.budget()
        await self.deliver(telegram.message(1, '/saldo', user=8), telegram.message(2, '/saldo', chat=10))
        control.budget.assert_not_called()
        self.assertEqual(self.http.sent, [])
        self.assertEqual(self.service.query(), [])

    async def test_day_change_reads_current_civil_renewal_from_control(self):
        now = [datetime(2026, 9, 13, 2, 59, tzinfo=timezone.utc)]
        control = ExecutionControl(self.service, dict(budget_mode='daily_subscription', timezone='America/Santiago',
            max_runtime_seconds=7200, recovery_runtime_seconds=0, max_active=1,
            max_job_runtime_seconds=600, max_retries=0, max_descendants=0,
            max_cost_usd=2, recovery_cost_usd=0), clock=lambda: now[0])
        self.adapter = TelegramAdapter(self.service, self.client, self.config,
            control=control, reservation_runtime_seconds=600)
        await self.deliver(telegram.message(1, '/saldo'))
        self.assertIn('13/09 a las 00:00', self.http.sent[-1]['text'])
        now[0] += timedelta(minutes=2)
        await self.deliver(telegram.message(2, '/saldo'))
        self.assertIn('14/09 a las 00:00', self.http.sent[-1]['text'])
        self.assertEqual(self.work_events(), 0)
        self.assertEqual(control._load()['jobs'], {})

    async def test_legacy_capture_ack_unchanged_without_control(self):
        await self.deliver(telegram.message(1, 'Nota local'))
        self.assertEqual(self.http.sent[-1]['text'], 'Guardado.')

    async def test_uppercase_saldo_remains_read_only_during_recovery(self):
        control = self.budget()
        with self.service.store.transaction():
            self.service._set_meta('recovery_required', True)
        await self.deliver(telegram.message(1, '/SALDO'))
        control.budget.assert_called_once()
        # Existing recovery protection still withholds external sends; the
        # normalized command reaches read-only handling, never capture.
        self.assertEqual(self.http.sent, [])
        self.assertEqual(self.service.query(), [])
        self.assertEqual(self.work_events(), 0)
