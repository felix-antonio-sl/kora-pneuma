"""One real durable reservation, Google transport, projection and ephemeral callback."""
import asyncio
import base64
import copy
import json
import unittest
from unittest.mock import patch

import test_source_monitor as fixtures
from test_google_sources import raw_message
from gtd_felix.control import ExecutionControl
from gtd_felix.source_evaluation import SourceEvaluation, digest_message
from gtd_felix.source_sync import SourceSync


class SourceEvaluationTests(unittest.IsolatedAsyncioTestCase):
    asyncSetUpBase = fixtures.SourceMonitorTests.asyncSetUp
    asyncTearDown = fixtures.SourceMonitorTests.asyncTearDown
    make = fixtures.SourceMonitorTests.make
    step = fixtures.SourceMonitorTests.step
    profile = fixtures.SourceMonitorTests.profile

    async def asyncSetUp(self):
        await self.asyncSetUpBase()
        await self.monitor.close()
        self.config['accounts']['selected']['sources']['mail'].update(
            scope='selective_since', since_epoch=1785556800, max_pages=1, pending_retry_limit=2)
        self.monitor = self.make()
        policy = dict(budget_mode='daily_subscription', timezone='America/Santiago',
            max_runtime_seconds=7200, recovery_runtime_seconds=0, max_cost_usd=1,
            recovery_cost_usd=0, max_active=1, max_job_runtime_seconds=240, max_retries=0, max_descendants=0)
        self.control = ExecutionControl(self.service, policy)
        self.item = self.service.capture('felix', 'selection-anchor', 'Revisar correspondencia elegida')['item']
        self.control.register_bot('felix', 'register-selection-parent', dict(id='parent', state='available',
            source_urn='urn:test:principal', host='localhost', profile='gtd-felix',
            capabilities=['prepare_private'], probe_evidence='fixture://native'))
        reserved = self.control.reserve('gtd-felix', 'reserve-selection', dict(
            item_id=self.item['id'], expected_version=1, capability='prepare_private', bot_id='parent',
            purpose='Review configured correspondence', scope='Private source preparation', mandate_id=None,
            max_cost_usd=1, max_runtime_seconds=120, max_retries=0, max_descendants=0))
        self.assertEqual('reserved', reserved['status'], reserved)
        self.job_id = reserved['job_id']
        self.control.record_dispatch(self.job_id, dict(provider='hermes', host='localhost', profile='gtd-felix', id='run-parent'))
        self.bridge_calls = []
        self.evaluation = SourceEvaluation(self.service, self.control, self.monitor,
            {'source_evaluation_enabled': True, 'hermes': {'routes': {'parent': {
                'base_url': 'http://127.0.0.1:51111', 'provider': 'openai-codex', 'model': 'gpt-6-astra'}}}},
            bridge=self.bridge)

    async def bridge(self, route, payload, timeout):
        check = {k: payload[k] for k in ('job_id', 'run_id', 'evaluation_id')}
        check['digest'] = digest_message(payload)
        self.assertTrue(self.evaluation.validate('gtd-felix', check)['allowed'])
        self.assertFalse(self.evaluation.validate('gtd-felix', {**check, 'digest': 'forged'})['allowed'])
        self.assertFalse(self.evaluation.validate('felix', check)['allowed'])
        self.bridge_calls.append(payload['external_id'])
        selected = payload['external_id'] == 'selected'
        return {'classification': 'selected' if selected else 'noise',
            'reason_code': 'gtd_relevant' if selected else 'non_actionable',
            'usage': {'input_tokens': 12, 'output_tokens': 3}, 'duration_seconds': 0.02}

    def messages(self, ids):
        self.profile(); self.profile()
        self.step({'messages': [{'id': identity} for identity in ids]})
        for identity in ids:
            message = raw_message(identity)
            raw = base64.urlsafe_b64decode(message['raw'] + '=' * (-len(message['raw']) % 4))
            raw += ('\r\nPRIVATE_BODY_' + identity).encode()
            message['raw'] = base64.urlsafe_b64encode(raw).decode().rstrip('=')
            self.step(message)

    async def test_selected_and_noise_under_one_job_without_body_receipts(self):
        self.messages(['selected', 'noise'])
        before = self.control.get_job(self.job_id)
        result = await self.evaluation.run('gtd-felix', self.job_id, 'mail')
        self.assertEqual({'selected': 1, 'noise': 1, 'uncertain': 0}, result['counts'], result)
        self.assertEqual(['selected', 'noise'], self.bridge_calls)
        self.assertEqual(before, self.control.get_job(self.job_id))
        self.assertEqual(1, len(self.control.pending()))
        rows = self.service.query({'source': {'provider': 'gmail'}})
        self.assertEqual(1, len(rows))
        self.assertIn('PRIVATE_BODY_selected', rows[0]['text'])
        self.assertEqual([{'item_id': rows[0]['id'], 'version': rows[0]['version'],
                           'subject': 'External assignment'}], result['selected_sources'])
        self.assertNotIn('PRIVATE_BODY', json.dumps(result['selected_sources']))
        metadata = [row[0] for row in self.service.store.db.execute(
            "SELECT value FROM metadata WHERE key LIKE 'source-evaluation:%'")]
        self.assertNotIn('PRIVATE_BODY', json.dumps(metadata))
        self.assertEqual(3, len(metadata))
        self.assertNotIn('PRIVATE_BODY_noise', '\n'.join(self.service.store.db.iterdump()))
        self.assertEqual({}, self.evaluation.active)

    async def test_poller_does_not_evaluate_or_call_google(self):
        before = len(self.calls)
        result = await self.monitor.run_once('mail')
        self.assertEqual(before, len(self.calls))
        self.assertFalse(result['current'])
        self.assertEqual([], self.bridge_calls)

    async def test_pause_while_evaluating_discards_result_and_preserves_pending(self):
        self.messages(['selected'])
        original = self.evaluation.bridge
        async def paused(route, payload, timeout):
            result = await original(route, payload, timeout)
            current = self.service.get_item(self.item['id'])
            self.service.execute('felix', {'operation_id': 'pause-during-helper', 'action': 'pause',
                'item_id': current['id'], 'expected_version': current['version']})
            return result
        self.evaluation.bridge = paused
        result = await self.evaluation.run('gtd-felix', self.job_id, 'mail')
        self.assertEqual('evaluation_interrupted', result['reason'])
        self.assertEqual([], self.service.query({'source': {'provider': 'gmail'}}))
        self.assertIn('selected', self.monitor.sources['mail'][1].inspect('mail')['pending_reads'])
        self.assertEqual({}, self.evaluation.active)

    async def test_pause_during_cached_retry_blocks_projection_after_cut(self):
        self.messages(['selected'])
        original_message = copy.deepcopy(self.steps[-1][1])
        with patch.object(SourceSync, 'apply_page', side_effect=OSError('synthetic-cut')):
            await self.evaluation.run('gtd-felix', self.job_id, 'mail')
        self.assertEqual([], self.service.query({'source': {'provider': 'gmail'}}))
        self.assertEqual(['selected'], self.bridge_calls)

        self.profile('20')
        self.step(original_message)
        self.step({'messages': []})
        transport = self.monitor.transports['selected']
        original_request = transport.request

        async def pause_after_cached_read(method, url, **kwargs):
            response = await original_request(method, url, **kwargs)
            if url.endswith('/messages/selected'):
                item = self.service.get_item(self.item['id'])
                receipt = self.service.execute('felix', {
                    'operation_id': 'pause-on-cached-read', 'action': 'pause',
                    'item_id': item['id'], 'expected_version': item['version']})
                self.assertEqual('applied', receipt['status'])
            return response

        with patch.object(transport, 'request', side_effect=pause_after_cached_read):
            result = await self.evaluation.run('gtd-felix', self.job_id, 'mail')
        self.assertEqual('paused', self.service.get_item(self.item['id'])['status'])
        self.assertEqual('partial', result['status'])
        self.assertEqual('evaluation_interrupted', result['reason'])
        self.assertEqual([], self.service.query({'source': {'provider': 'gmail'}}))
        self.assertEqual(['selected'], self.bridge_calls)
        self.assertIn('selected', self.monitor.sources['mail'][1].inspect('mail')['pending_reads'])
        self.assertEqual({}, self.evaluation.active)

    async def test_owner_and_legacy_budget_cannot_invoke_helper(self):
        with self.assertRaises(ValueError):
            await self.evaluation.run('felix', self.job_id, 'mail')
        self.assertEqual([], self.calls)
        self.evaluation.config['source_evaluation_enabled'] = False
        with self.assertRaises(ValueError):
            await self.evaluation.run('gtd-felix', self.job_id, 'mail')

    async def test_later_routed_owner_reply_blocks_helper_before_network(self):
        source = self.service.capture('felix', 'later-source-review-direction',
            'Stop this review.', source={'provider': 'telegram'})['item']
        routed = self.service.execute('gtd-felix', {
            'operation_id': 'route-later-source-review-direction', 'action': 'clarify',
            'item_id': source['id'], 'expected_version': source['version'],
            'fields': {'destination': 'existing', 'target_item_id': self.item['id'],
                'reason': 'Later owner direction',
                'intent_basis': {'source_item_id': source['id'], 'quote': source['text']}}})
        self.assertEqual('applied', routed['status'])
        self.assertEqual('routed_intent_set_stale', self.control.validate_target(
            self.job_id, 'gtd-felix', self.item['id'], 'prepare_private')['reason'])
        before = len(self.calls)
        with self.assertRaisesRegex(ValueError, '^current_parent_required$'):
            await self.evaluation.run('gtd-felix', self.job_id, 'mail')
        self.assertEqual(before, len(self.calls))
        self.assertEqual([], self.bridge_calls)
        self.assertEqual({}, self.evaluation.active)

    async def test_error_body_not_retained(self):
        self.messages(['noise'])
        async def failed(*args):
            raise ValueError('PRIVATE_BODY_noise_SECRET_ERROR')
        self.evaluation.bridge = failed
        result = await self.evaluation.run('gtd-felix', self.job_id, 'mail')
        self.assertEqual('partial', result['status'])
        self.assertNotIn('PRIVATE_BODY_noise_SECRET_ERROR', '\n'.join(self.service.store.db.iterdump()))
        self.assertEqual([], self.service.query({'source': {'provider': 'gmail'}}))
        self.assertEqual({}, self.evaluation.active)

    async def test_bridge_failure_receipt_has_closed_code_and_unknown_usage(self):
        self.messages(['noise'])
        async def failed(*args):
            raise ValueError('bridge_inactive_parent')
        self.evaluation.bridge = failed
        result = await self.evaluation.run('gtd-felix', self.job_id, 'mail')
        self.assertEqual({'input_tokens': None, 'output_tokens': None}, result['usage'])
        self.assertEqual(1, result['counts']['uncertain'])
        receipts = [json.loads(row[0]) for row in self.service.store.db.execute(
            "SELECT value FROM metadata WHERE key LIKE 'source-evaluation:receipt:%'")]
        self.assertEqual(['bridge_inactive_parent'], [row['error'] for row in receipts])
        self.assertNotIn('PRIVATE_BODY', json.dumps(receipts))

    async def test_helper_failure_preserves_debt_without_claiming_zero_usage(self):
        self.messages(['noise'])
        async def failed(*args):
            raise ValueError('bridge_helper_turn_failed')
        self.evaluation.bridge = failed
        result = await self.evaluation.run('gtd-felix', self.job_id, 'mail')
        self.assertEqual({'input_tokens': None, 'output_tokens': None}, result['usage'])
        receipts = [json.loads(row[0]) for row in self.service.store.db.execute(
            "SELECT value FROM metadata WHERE key LIKE 'source-evaluation:receipt:%'")]
        self.assertEqual(['bridge_helper_turn_failed'], [row['error'] for row in receipts])
        self.assertIn('noise', self.monitor.sources['mail'][1].inspect('mail')['pending_reads'])
        self.assertEqual([], self.service.query({'source': {'provider': 'gmail'}}))
        self.assertNotIn('PRIVATE_BODY_noise', '\n'.join(self.service.store.db.iterdump()))

    async def test_malformed_validation_and_result_fail_closed(self):
        for value in [{}, {'job_id': []}, None]:
            self.assertFalse(self.evaluation.validate('gtd-felix', value)['allowed'])
        with self.assertRaises(ValueError):
            self.evaluation._result({'classification': 'noise', 'reason_code': 'non_actionable',
                'usage': {'input_tokens': 'body', 'output_tokens': 1}, 'duration_seconds': 1})

    def test_route_gate_admits_deepseek_and_rejects_near_miss(self):
        from gtd_felix.source_evaluation import _route_allowed
        self.assertTrue(_route_allowed({'provider': 'opencode-go', 'model': 'deepseek-v4.1-flash'}))
        self.assertTrue(_route_allowed({'provider': 'openai-codex', 'model': 'gpt-5.6-luna'}))
        self.assertTrue(_route_allowed({'provider': 'openai-codex', 'model': 'gpt-6-astra'}))
        self.assertFalse(_route_allowed({'provider': 'opencode-go', 'model': 'deepseek-v4-flash'}))
        self.assertFalse(_route_allowed({'provider': 'openai-codex', 'model': 'deepseek-v4.1-flash'}))
        self.assertFalse(_route_allowed({}))
        self.assertFalse(_route_allowed(None))

    async def test_mcp_to_authenticated_http_uses_same_parent_without_bodies(self):
        from aiohttp import web, ClientSession
        from gtd_felix.application import create_app
        from gtd_felix.mcp import MCPClient
        config = {'data_dir': str(self.root / 'store'), 'actors': {'owner': 'felix',
            'principal': 'gtd-felix', 'executors': []},
            'api_tokens': {'synthetic-principal-token': 'gtd-felix', 'synthetic-owner-token': 'felix'},
            'google': self.config}
        with patch('gtd_felix.source_monitor.SourceMonitor', return_value=self.monitor), \
             patch('gtd_felix.source_evaluation.SourceEvaluation', return_value=self.evaluation):
            app = create_app(self.service, self.control, config)
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, '127.0.0.1', 0)
        await site.start()
        url = 'http://127.0.0.1:' + str(site._server.sockets[0].getsockname()[1])
        try:
            async with ClientSession() as session:
                async with session.post(url + '/v1/source-evaluation/validate', json={}) as response:
                    self.assertEqual(401, response.status)
            self.messages(['selected', 'noise'])
            client = MCPClient(url, 'synthetic-principal-token')
            result = await client.call('gtd_read', {'view': 'source_evaluation',
                'source_id': 'mail', 'job_id': self.job_id})
            self.assertEqual(1, result['counts']['selected'], result)
            self.assertNotIn('PRIVATE_BODY', json.dumps(result))
            owner = MCPClient(url, 'synthetic-owner-token')
            result = await owner.call('gtd_read', {'view': 'source_evaluation',
                'source_id': 'mail', 'job_id': self.job_id})
            self.assertEqual('rejected', result['status'])
        finally:
            await runner.cleanup()
