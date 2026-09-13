"""Non-agentic external effects: one admission, then read-only reconciliation.

Uses SourceMonitor's account transports and the same Store. Durable retry times
are scheduling hints, never permission to repeat a dispatched provider request.
"""
import asyncio
from datetime import datetime, timezone
import hashlib
import json

from .calendar_effects import CalendarEffects
from .gmail_effects import GmailEffects

KEY = 'effect-monitor:state'
TERMINAL = {'confirmed', 'no_dispatch', 'conflict', 'revoked'}


def validate_effects(config, accounts):
    if not isinstance(config, dict) or set(config) != {'accounts', 'poll_interval_seconds', 'retry_interval_seconds'}:
        raise ValueError('invalid_external_effects_config')
    selected = config['accounts']
    if (not isinstance(selected, list) or not selected or any(not isinstance(a, str) or a not in accounts for a in selected)
            or len(set(selected)) != len(selected)):
        raise ValueError('invalid_external_effect_accounts')
    for field in ('poll_interval_seconds', 'retry_interval_seconds'):
        if type(config[field]) is not int or not 1 <= config[field] <= 86400:
            raise ValueError('invalid_external_effect_intervals')
    return config


class EffectMonitor:
    def __init__(self, service, effects, source_monitor, config=None):
        self.service, self.effects = service, effects
        self.transports = {t.account: t for t in getattr(source_monitor, 'transports', {}).values()}
        self.config = validate_effects(config, self.transports) if config is not None else None
        self._lock = asyncio.Lock()

    def _load(self):
        return self.service._meta(KEY, {})

    def _record(self, effect, reason, delay):
        identity = effect['id']
        signature = hashlib.sha256(json.dumps([effect['status'], reason], separators=(',', ':')).encode()).hexdigest()
        # Persist the exact event before ingestion. A crash replays the same event
        # identity and payload; no transaction nests inside ingest_event.
        with self.service.store.transaction():
            state = self._load()
            previous = state.get(identity, {})
            changed = previous.get('signature') != signature
            event = previous.get('event') if not changed else {
                'provider': 'gtd-review', 'account': 'local', 'external_id': 'external-effect:' + identity,
                'revision': signature, 'payload': {'item_id': effect['proposal']['item_id'],
                    'effect_id': identity, 'status': effect['status'], 'reason': 'external_effect_status',
                    'detail': reason, 'proposal_hash': effect['proposal_hash']}}
            state[identity] = {'signature': signature, 'status': effect['status'], 'reason': reason,
                'next_attempt_at': datetime.now(timezone.utc).timestamp() + delay,
                'event': event, 'event_pending': changed or previous.get('event_pending', False)}
            self.service._set_meta(KEY, state)
        self._publish(identity)

    def _publish(self, identity):
        with self.service.store.lock:
            record = self._load().get(identity, {})
        if not record.get('event_pending'):
            return
        receipt = self.service.ingest_event(record['event'])
        if receipt['status'] == 'rejected':
            return
        with self.service.store.transaction():
            state = self._load()
            if state.get(identity, {}).get('signature') == record['signature']:
                state[identity]['event_pending'] = False
                self.service._set_meta(KEY, state)

    async def tick(self):
        if self.config is None:
            return
        async with self._lock:
            # Internal inventory; no public/global permission is inferred here.
            with self.service.store.lock:
                identities = list(self.effects._load()['effects'])
            for identity in identities:
                self._publish(identity)
                with self.service.store.lock:
                    effect = self.effects._load()['effects'][identity]
                    record = self._load().get(identity, {})
                if effect['proposal']['account'] not in self.config['accounts']:
                    continue
                if effect['status'] in TERMINAL:
                    if record.get('status') != effect['status']:
                        self._record(effect, effect.get('error'), 0)
                    continue
                if record.get('next_attempt_at', 0) > datetime.now(timezone.utc).timestamp():
                    continue
                transport = self.transports[effect['proposal']['account']]
                driver = (GmailEffects if effect['proposal']['provider'] == 'gmail' else CalendarEffects)(self.effects, transport)
                delay = self.config['retry_interval_seconds']
                if 'dispatch' not in effect:
                    ready = self.effects.readiness(identity)
                    if not ready['ready']:
                        self._record(effect, ready['reason'], delay)
                        continue
                # Backoff is committed before awaiting; cancellation cannot create
                # an immediate hot loop after restart. Ledger intent gates writes.
                with self.service.store.transaction():
                    state = self._load()
                    state.setdefault(identity, {})['next_attempt_at'] = datetime.now(timezone.utc).timestamp() + delay
                    self.service._set_meta(KEY, state)
                try:
                    result = await (driver.reconcile(identity) if 'dispatch' in effect else driver.dispatch(identity))
                    reason = result.get('error') or result.get('reason')
                except asyncio.CancelledError:
                    raise
                except Exception:
                    reason = 'provider_unavailable'  # Never persist provider body/credentials.
                retry_after = transport.inspect().get('retry_after_seconds')
                if type(retry_after) is int and retry_after > 0:
                    delay = max(delay, min(retry_after, 604800))
                with self.service.store.lock:
                    current = self.effects._load()['effects'][identity]
                self._record(current, reason, delay)

    async def run(self, stop):
        if self.config is None:
            return
        while not stop.is_set():
            await self.tick()
            try:
                await asyncio.wait_for(stop.wait(), self.config['poll_interval_seconds'])
            except asyncio.TimeoutError:
                pass
