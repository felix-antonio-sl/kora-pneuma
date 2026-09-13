"""Job-bound Gmail selection; bodies only cross the private ephemeral bridge."""
import asyncio
import hashlib
import ipaddress
import json
import math
import os
import time
from urllib.parse import urlsplit
from uuid import uuid4

import aiohttp


def digest_message(message):
    return hashlib.sha256(json.dumps({k: message[k] for k in ('text', 'external_id', 'revision')},
        sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()


BRIDGE_ERRORS = frozenset({'invalid_request', 'helper_busy', 'inactive_parent', 'provider_mismatch',
    'helper_monitor_unavailable', 'helper_cleanup_pending', 'validation_timeout', 'evaluation_not_active', 'evaluation_cancelled', 'helper_failed', 'evaluation_unavailable', 'unauthorized',
    'bridge_timeout_error', 'bridge_attribute_error', 'bridge_type_error', 'bridge_os_error',
    'bridge_value_error', 'bridge_internal_error'})


class SourceEvaluation:
    def __init__(self, service, control, monitor, config, *, bridge=None, clock=time.monotonic):
        self.service, self.control, self.monitor, self.config = service, control, monitor, config
        self.bridge, self.clock = bridge or self._bridge, clock
        self.active = {}
        self.busy = False

    def _job(self, actor, job_id):
        if actor != self.service.principal_actor or not isinstance(job_id, str):
            raise ValueError('principal_job_required')
        job = self.control.get_job(job_id)
        if not job or job['actor'] != actor:
            raise ValueError('principal_job_required')
        target = self.control.validate_target(job_id, actor, job['item_id'], 'prepare_private')
        if not target.get('allowed'):
            raise ValueError('current_parent_required')
        valid = self.control.validate(job_id, 'prepare_private')
        if not valid.get('allowed') or valid['limits'].get('cost_control', True):
            raise ValueError('daily_private_job_required')
        native = job.get('native') or {}
        if native.get('provider') != 'hermes' or not native.get('id'):
            raise ValueError('native_parent_required')
        return job, valid['limits']

    def validate(self, actor, payload):
        try:
            if not isinstance(payload, dict) or set(payload) != {'job_id', 'run_id', 'evaluation_id', 'digest'}:
                raise ValueError()
            if any(not isinstance(v, str) for v in payload.values()):
                raise ValueError()
            entry = self.active.get(payload['evaluation_id'])
            if not entry or any(entry[k] != payload[k] for k in ('job_id', 'run_id', 'digest')) or not entry['alive']():
                raise ValueError()
            job, limits = self._job(actor, payload['job_id'])
            if job['native']['id'] != payload['run_id']:
                raise ValueError()
            remaining = min(entry['deadline'] - self.clock(),
                limits['max_runtime_seconds'] - job['observed_runtime_seconds'])
            if remaining <= 0:
                raise ValueError()
            return {'allowed': True, 'remaining_seconds': remaining}
        except (ValueError, TypeError, KeyError):
            return {'allowed': False, 'remaining_seconds': 0}

    async def _bridge(self, route, payload, timeout):
        parsed = urlsplit(route.get('base_url', ''))
        if (parsed.scheme != 'http' or not ipaddress.ip_address(parsed.hostname).is_loopback
                or parsed.username or parsed.password or parsed.query or parsed.fragment):
            raise ValueError('local_bridge_required')
        if route.get('provider') != 'openai-codex' or route.get('model') not in {'gpt-6-astra', 'gpt-5.6-luna'}:
            raise ValueError('configured_subscription_required')
        token = os.environ.get(route.get('api_key_env', ''))
        if not token:
            raise ValueError('bridge_auth_unavailable')
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=timeout), trust_env=False) as session:
            async with session.post(route['base_url'].rstrip('/') + '/v1/gtd/evaluate-mail',
                    headers={'Authorization': 'Bearer ' + token}, json=payload, allow_redirects=False) as response:
                raw = await response.content.read(8193)
                if len(raw) > 8192:
                    raise ValueError('bridge_response_too_large')
                value = json.loads(raw)
                if response.status != 200:
                    code = value.get('error') if isinstance(value, dict) else None
                    raise ValueError('bridge_' + (code if code in BRIDGE_ERRORS else 'evaluation_unavailable'))
                return value

    @staticmethod
    def _result(result):
        allowed = {'selected': {'gtd_relevant'}, 'noise': {'non_actionable'},
                   'uncertain': {'needs_review', 'evaluation_unavailable'}}
        if (not isinstance(result, dict) or set(result) != {'classification', 'reason_code', 'usage', 'duration_seconds'}
                or result.get('classification') not in allowed
                or result.get('reason_code') not in allowed[result['classification']]):
            raise ValueError('invalid_evaluation_result')
        usage = result['usage']
        if not isinstance(usage, dict) or set(usage) != {'input_tokens', 'output_tokens'}:
            raise ValueError('invalid_evaluation_usage')
        if any(v is not None and (type(v) is not int or not 0 <= v <= 10**9) for v in usage.values()):
            raise ValueError('invalid_evaluation_usage')
        duration = result['duration_seconds']
        if type(duration) not in {int, float} or not math.isfinite(duration) or not 0 <= duration <= 60:
            raise ValueError('invalid_evaluation_duration')
        return {k: result[k] for k in ('classification', 'reason_code')}

    async def run(self, actor, job_id, source_id, *, alive=lambda: True):
        if (not self.config.get('source_evaluation_enabled', False) or self.monitor is None
                or not isinstance(source_id, str) or source_id not in self.monitor.sources):
            raise ValueError('source_evaluation_unavailable')
        job, limits = self._job(actor, job_id)
        alias, adapter = self.monitor.sources[source_id]
        cfg = adapter.config[source_id]
        if cfg.get('provider') != 'gmail' or cfg.get('scope') != 'selective_since':
            raise ValueError('selective_source_required')
        if cfg.get('page_size', 100) > 5 or cfg.get('max_pages', 100) != 1 or cfg.get('pending_retry_limit', 10) > 5:
            raise ValueError('bounded_selection_configuration_required')
        route = self.config.get('hermes', {}).get('routes', {}).get(job['bot_id'])
        if not route:
            raise ValueError('bridge_route_required')
        if self.busy:
            return {'status': 'rejected', 'error': 'source_evaluation_busy'}
        self.busy = True
        deadline = self.clock() + min(20, max(0, limits['max_runtime_seconds'] - job['observed_runtime_seconds'] - 2))
        counts = dict(selected=0, noise=0, uncertain=0)
        total_usage = dict(input_tokens=0, output_tokens=0)
        calls = 0
        call_id = uuid4().hex

        def projection_guard():
            if self.clock() >= deadline or not alive():
                raise asyncio.CancelledError()
            try:
                current, _ = self._job(actor, job_id)
                if current['native']['id'] != job['native']['id']:
                    raise ValueError('native_parent_changed')
            except (ValueError, KeyError, TypeError):
                raise asyncio.CancelledError() from None

        async def evaluate(message):
            nonlocal calls
            if calls >= 10 or self.clock() >= deadline or not alive():
                raise asyncio.CancelledError()
            calls += 1
            identity = uuid4().hex
            payload = {k: message[k] for k in ('text', 'external_id', 'revision')}
            if any(not isinstance(v, str) for v in payload.values()) or len(payload['text'].encode()) > 200000:
                counts['uncertain'] += 1
                return {'classification': 'uncertain', 'reason_code': 'needs_review'}
            payload.update(job_id=job_id, run_id=job['native']['id'], evaluation_id=identity)
            check = {k: payload[k] for k in ('job_id', 'run_id', 'evaluation_id')}
            check['digest'] = digest_message(payload)
            self.active[identity] = {**check, 'deadline': deadline, 'alive': alive}
            try:
                guard = self.validate(actor, check)
                if not guard['allowed']:
                    raise asyncio.CancelledError()
                result = await self.bridge(route, payload, guard['remaining_seconds'])
                if not self.validate(actor, check)['allowed']:
                    raise asyncio.CancelledError()
                decision = self._result(result)
                counts[decision['classification']] += 1
                for key, value in result['usage'].items():
                    total_usage[key] = None if value is None or total_usage[key] is None else total_usage[key] + value
                with self.service.store.transaction():
                    self.service._set_meta('source-evaluation:receipt:' + identity,
                        {'job_id': job_id, 'run_id': job['native']['id'], 'source_id': source_id,
                         'classification': decision['classification'], 'reason_code': decision['reason_code'],
                         'usage': result['usage'], 'duration_seconds': result['duration_seconds'],
                         'time_accounting': 'included_in_parent_wall_time', 'cost_usd': None})
                return decision
            except (Exception, asyncio.CancelledError) as exc:
                code = str(exc) if isinstance(exc, ValueError) else ''
                code = code if code in {'bridge_' + error for error in BRIDGE_ERRORS} else (
                    'evaluation_interrupted' if isinstance(exc, asyncio.CancelledError) else 'evaluation_unavailable')
                counts['uncertain'] += 1
                for key in total_usage:
                    total_usage[key] = None
                with self.service.store.transaction():
                    self.service._set_meta('source-evaluation:receipt:' + identity,
                        {'job_id': job_id, 'run_id': job['native']['id'], 'source_id': source_id,
                         'classification': 'uncertain', 'reason_code': 'evaluation_unavailable', 'error': code,
                         'usage': {'input_tokens': None, 'output_tokens': None},
                         'time_accounting': 'included_in_parent_wall_time', 'cost_usd': None})
                raise
            finally:
                self.active.pop(identity, None)

        try:
            seconds = deadline - self.clock()
            if seconds <= 0:
                raise ValueError('selection_time_unavailable')
            info = await asyncio.wait_for(self.monitor.evaluate_once(source_id, evaluate, projection_guard), timeout=seconds)
            projection_guard()
            return {'status': 'evaluated' if info.get('health') == 'complete' else 'partial',
                    'source_id': source_id, 'counts': counts, 'usage': total_usage,
                    'coverage': {k: info.get(k) for k in ('health', 'enumeration', 'projection', 'pending_reads', 'priority')},
                    'time_accounting': 'included_in_parent_wall_time'}
        except (asyncio.TimeoutError, asyncio.CancelledError):
            return {'status': 'partial', 'source_id': source_id, 'counts': counts,
                    'usage': total_usage, 'reason': 'evaluation_interrupted',
                    'time_accounting': 'included_in_parent_wall_time'}
        finally:
            self.busy = False
            with self.service.store.transaction():
                self.service._set_meta('source-evaluation:call:' + call_id,
                    {'job_id': job_id, 'source_id': source_id, 'counts': counts, 'usage': total_usage,
                     'time_accounting': 'included_in_parent_wall_time'})
