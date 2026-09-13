"""Real ledger, authenticated HTTP/MCP and loopback Google; no live accounts."""
import asyncio
from datetime import datetime, timedelta, timezone
import os
import json
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import aiohttp
import test_gmail_effects as gmail_fixture
from test_google_transport import ACCOUNT
import test_mcp as mcp_fixture
from test_mcp import OWNER, PRINCIPAL
from gtd_felix.effect_monitor import EffectMonitor, KEY, validate_effects
from gtd_felix.effects import ExternalEffects
from gtd_felix.service import GTDService
from gtd_felix.application import create_app, EFFECT_MONITOR, SOURCE_MONITOR
from gtd_felix.control import ExecutionControl
from runtime_location import RUNTIME
from aiohttp import web
from gtd_felix.mcp import MCPClient, TOOLS


class MonitorTests(unittest.IsolatedAsyncioTestCase):
    asyncSetUp = gmail_fixture.GmailEffectsTests.asyncSetUp
    asyncTearDown = gmail_fixture.GmailEffectsTests.asyncTearDown
    step = gmail_fixture.GmailEffectsTests.step
    preflight = gmail_fixture.GmailEffectsTests.preflight
    propose = gmail_fixture.GmailEffectsTests.propose
    readback = gmail_fixture.GmailEffectsTests.readback

    def monitor(self, enabled=True):
        return EffectMonitor(self.service, self.effects, SimpleNamespace(transports={'alias': self.transport}),
            {'accounts': [ACCOUNT], 'poll_interval_seconds': 1, 'retry_interval_seconds': 10} if enabled else None)

    def due(self, identity):
        with self.service.store.transaction():
            state = self.service._meta(KEY, {})
            state[identity]['next_attempt_at'] = 0
            self.service._set_meta(KEY, state)

    def draft_steps(self):
        self.preflight(); self.step({'id': 'draft1'})
        self.step({'emailAddress': ACCOUNT}); self.step(self.readback(True))

    async def test_proposed_no_network_then_standing_draft_once_and_review(self):
        effect = self.propose('draft_create', authorized=False)
        monitor = self.monitor()
        await monitor.tick(); await monitor.tick()
        self.assertEqual(self.calls, []); self.assertEqual(self.writes, [])
        self.assertEqual(self.effects.get('felix', effect['id'])['status'], 'proposed')
        self.effects.grant_draft_preparation('felix', 'grant', ACCOUNT, 'gtd-felix',
            (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat())
        self.due(effect['id']); self.draft_steps()
        await monitor.tick(); await self.monitor().tick()
        self.assertEqual(len(self.writes), 1)
        self.assertEqual(self.effects.get('felix', effect['id'])['status'], 'confirmed')
        events = self.service.pending_events('gtd-review', 'local')
        confirmed = [e for e in events if e['payload'].get('status') == 'confirmed']
        self.assertEqual(len(confirmed), 1)
        self.assertEqual(confirmed[0]['payload']['item_id'], self.item['id'])
        self.assertNotEqual(self.service.get_item(self.item['id'])['status'], 'done')

    async def test_standing_draft_never_send_and_disabled_no_loop(self):
        effect = self.propose(authorized=False)
        self.effects.grant_draft_preparation('felix', 'grant', ACCOUNT, 'gtd-felix', '2099-01-01T00:00:00Z')
        await self.monitor().tick()
        self.assertEqual(self.calls, [])
        self.effects.authorize('felix', 'owner', effect['id'], effect['proposal_hash'])
        await self.monitor(False).tick()
        self.assertEqual(self.calls, [])
        self.assertEqual(self.effects.get('felix', effect['id'])['status'], 'authorized')

    async def test_lost_ack_restart_readback_only_even_recovery(self):
        effect = self.propose()
        self.preflight(); self.step('disconnect')
        await self.monitor().tick()
        self.assertEqual(len(self.writes), 1)
        self.assertIn(self.effects.get('felix', effect['id'])['status'], {'uncertain', 'dispatching'})
        # Recreate both ledger and monitor over the same durable Store.
        self.service.close()
        self.service = GTDService(self.root / 'store')
        self.effects = ExternalEffects(self.service)
        with self.service.store.transaction(): self.service._set_meta('recovery_required', True)
        self.due(effect['id'])
        self.step({'emailAddress': ACCOUNT}); self.step({'messages': [{'id': 'message1'}]}); self.step(self.readback())
        await self.monitor().tick()
        self.assertEqual(len(self.writes), 1)
        self.assertEqual(self.effects.get('felix', effect['id'])['status'], 'confirmed')
        self.assertTrue(self.service.recovery_required)

    async def test_readiness_correction_recovery_and_revocation_prevent_preflight(self):
        effect = self.propose()
        with self.service.store.transaction(): self.service._set_meta('recovery_required', True)
        before = self.effects.get('felix', effect['id'])
        self.assertEqual(self.effects.readiness(effect['id'])['reason'], 'recovery_required')
        self.assertEqual(self.effects.get('felix', effect['id']), before)
        await self.monitor().tick(); self.assertEqual(self.calls, [])
        with self.service.store.transaction(): self.service._set_meta('recovery_required', False)
        result = self.service.execute('felix', {'operation_id': 'human', 'action': 'edit', 'item_id': self.item['id'],
            'expected_version': self.item['version'], 'fields': {'text': 'Corrected human source'}})
        self.assertEqual(result['status'], 'applied')
        self.due(effect['id']); await self.monitor().tick()
        self.assertEqual(self.calls, [])
        self.assertFalse(self.effects.readiness(effect['id'])['ready'])
        self.effects.revoke('felix', 'revoke', effect_id=effect['id'])
        self.due(effect['id']); await self.monitor().tick()
        self.assertEqual(self.calls, [])

    async def test_durable_backoff_retry_after_and_cancellation(self):
        effect = self.propose()
        async def fail(identity):
            self.transport._retry_after = 120
            raise RuntimeError('secret provider body must not persist')
        with patch('gtd_felix.effect_monitor.GmailEffects.dispatch', side_effect=fail) as call:
            await self.monitor().tick(); await self.monitor().tick()
            self.assertEqual(call.call_count, 1)
        record = self.service._meta(KEY)[effect['id']]
        self.assertGreater(record['next_attempt_at'], datetime.now(timezone.utc).timestamp() + 100)
        self.assertNotIn('secret', str(record))
        self.due(effect['id'])
        async def cancel(identity):
            self.effects.begin_dispatch(identity)
            raise asyncio.CancelledError()
        with patch('gtd_felix.effect_monitor.GmailEffects.dispatch', side_effect=cancel):
            with self.assertRaises(asyncio.CancelledError): await self.monitor().tick()
        self.assertEqual(self.effects.get('felix', effect['id'])['status'], 'dispatching')
        self.assertGreater(self.service._meta(KEY)[effect['id']]['next_attempt_at'], datetime.now(timezone.utc).timestamp())

    async def test_app_reuses_source_transport_and_configuration_stays_optional(self):
        config = {'data_dir': str(self.root / 'store'),
            'actors': {'owner': 'felix', 'principal': 'gtd-felix'},
            'api_tokens': {OWNER: 'felix'},
            'google': {'poll_interval_seconds': 10, 'stale_after_seconds': 60, 'accounts': {'source-alias': {
                'transport': {'account': ACCOUNT, 'token_file': str(self.root / 'token.json'), 'gmail': True},
                'sources': {'mail': {'provider': 'gmail', 'account': ACCOUNT, 'scope': 'whole_mailbox', 'page_size': 2}}}}},
            'external_effects': {'accounts': [ACCOUNT], 'poll_interval_seconds': 2, 'retry_interval_seconds': 30}}
        app = create_app(self.service, ExecutionControl(self.service, {}), config)
        self.assertIs(app[EFFECT_MONITOR].transports[ACCOUNT], app[SOURCE_MONITOR].transports['source-alias'])
        await app[SOURCE_MONITOR].close()
        del config['external_effects']
        app = create_app(self.service, ExecutionControl(self.service, {}), config)
        self.assertIsNone(app[EFFECT_MONITOR].config)
        await app[SOURCE_MONITOR].close()

    def test_account_config_exact_and_no_alias_or_unknown_keys(self):
        for account in ('alias', 'foreign@example.invalid'):
            with self.assertRaises(ValueError): validate_effects({'accounts': [account], 'poll_interval_seconds': 1, 'retry_interval_seconds': 2}, {ACCOUNT})


class EffectsHTTPTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        await mcp_fixture.MCPTests.asyncSetUp(self)
        await self.runner.cleanup()
        config = {'data_dir': str(self.root / 'data'),
            'actors': {'owner': 'felix', 'principal': 'gtd-felix', 'executors': ['history-worker']},
            'api_tokens': {OWNER: 'felix', PRINCIPAL: 'gtd-felix', 'synthetic-worker-token': 'history-worker'}}
        self.runner = web.AppRunner(create_app(self.service, self.control, config), access_log=None)
        await self.runner.setup()
        site = web.TCPSite(self.runner, '127.0.0.1', 0)
        await site.start()
        self.url = 'http://127.0.0.1:' + str(site._server.sockets[0].getsockname()[1])
        self.client = MCPClient(self.url, PRINCIPAL)
    asyncTearDown = mcp_fixture.MCPTests.asyncTearDown

    def proposal(self):
        return {'provider': 'calendar', 'account': 'calendar@example.invalid', 'action': 'insert',
            'item_id': self.item['id'], 'target': {'id': 'fixed123'},
            'payload': {'calendar_id': 'calendar@example.invalid', 'event': {'id': 'fixed123', 'summary': 'Private block'}, 'send_updates': 'none'},
            'expires_at': '2099-01-01T00:00:00Z'}

    async def post(self, operation, values, token=PRINCIPAL, job=None):
        headers = {'Authorization': 'Bearer ' + token}
        if job: headers['X-GTD-Job-ID'] = job
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url + '/v1/effects/' + operation, json=values, headers=headers) as response:
                return response.status, await response.json()

    async def test_principal_job_scope_owner_exact_hash_and_no_read_authorization(self):
        values = {'operation_id': 'proposal', 'proposal': self.proposal()}
        self.assertEqual((await self.post('propose_effect', values))[0], 403)
        code, receipt = await self.post('propose_effect', values, job=self.job)
        self.assertEqual(receipt['status'], 'proposed', receipt)
        identity = receipt['effect']['id']
        view = await self.client.call('gtd_read', {'view': 'effect', 'effect_id': identity})
        self.assertEqual(view['status'], 'proposed'); self.assertFalse(view['delivery_configured'])
        self.assertEqual(view['readiness']['reason'], 'external_authorization_required')
        auth = {'operation_id': 'auth', 'effect_id': identity, 'expected_proposal_hash': receipt['effect']['proposal_hash']}
        self.assertEqual((await self.post('authorize_effect', auth, job=self.job))[0], 403)
        wrong = await self.post('authorize_effect', {**auth, 'expected_proposal_hash': 'wrong'}, OWNER)
        self.assertEqual(wrong[1]['status'], 'rejected')
        auth['operation_id'] = 'auth-good'
        self.assertEqual((await self.post('authorize_effect', auth, OWNER))[1]['status'], 'authorized')
        self.assertEqual((await self.post('propose_effect', {**values, 'actor': 'felix'}, job=self.job))[0], 400)
        other = self.service.capture('felix', 'other', 'Different matter')['item']
        bad = {'operation_id': 'outside', 'proposal': {**self.proposal(), 'item_id': other['id']}}
        self.assertEqual((await self.post('propose_effect', bad, job=self.job))[0], 403)
        self.control.request_stop('felix', 'stop', self.job)
        self.assertEqual((await self.post('propose_effect', values, job=self.job))[0], 403)

    async def test_mcp_alternative_exact_actor_grantee_and_legacy_shape(self):
        self.assertEqual([t['name'] for t in TOOLS], ['gtd_read', 'gtd_command', 'gtd_dispatch'])
        with patch.dict(os.environ, {'GTD_JOB_ID': self.job}):
            result = await self.client.call('gtd_command', {'effect_control': 'propose_effect',
                'request': {'operation_id': 'mcp-propose', 'proposal': self.proposal()}})
        self.assertEqual(result['status'], 'proposed', result)
        with self.assertRaises(ValueError):
            await self.client.call('gtd_command', {'effect_control': 'propose_effect', 'request': {}, 'job_id': self.job})
        owner = MCPClient(self.url, OWNER)
        grant = await owner.call('gtd_command', {'effect_control': 'grant_draft_preparation', 'request': {
            'operation_id': 'grant', 'account': 'calendar@example.invalid', 'grantee': 'gtd-felix', 'expires_at': '2099-01-01T00:00:00Z'}})
        self.assertEqual(grant['status'], 'granted', grant)
        revoked = await owner.call('gtd_command', {'effect_control': 'revoke_effect', 'request': {
            'operation_id': 'revoke', 'grant_id': grant['grant']['id']}})
        self.assertEqual(revoked['status'], 'revoked')
        for op in ('begin_dispatch', 'observe', 'configure'):
            with self.assertRaises(ValueError): await owner.call('gtd_command', {'effect_control': op, 'request': {}})

    async def test_executor_has_no_effect_inventory_or_controls(self):
        worker = MCPClient(self.url, 'synthetic-worker-token')
        self.assertEqual((await worker.call('gtd_read', {'view': 'effects'}))['error'], 'forbidden')
        for op, values in [('propose_effect', {'operation_id': 'worker', 'proposal': self.proposal()}),
            ('authorize_effect', {'operation_id': 'auth', 'effect_id': 'none', 'expected_proposal_hash': 'none'}),
            ('grant_draft_preparation', {'operation_id': 'grant', 'account': 'a', 'grantee': 'history-worker', 'expires_at': '2099-01-01T00:00:00Z'})]:
            self.assertEqual((await self.post(op, values, 'synthetic-worker-token', self.job))[0], 403)

    async def test_owner_can_prepare_without_job_but_cannot_forge_identity_or_observe(self):
        result = await self.post('propose_effect', {'operation_id': 'owner-proposal', 'proposal': self.proposal()}, OWNER)
        self.assertEqual(result[1]['status'], 'proposed')
        owner = MCPClient(self.url, OWNER)
        own = await owner.call('gtd_read', {'view': 'effects'})
        principal = await self.client.call('gtd_read', {'view': 'effects'})
        self.assertEqual(len(own), 1); self.assertEqual(principal, [])
        self.assertEqual((await self.post('observe', {'status': 'confirmed'}, OWNER))[0], 400)
        self.assertEqual((await self.post('grant_draft_preparation', {'operation_id': 'grant', 'account': 'a',
            'grantee': 'gtd-felix', 'actor': 'felix', 'expires_at': '2099-01-01T00:00:00Z'}, OWNER))[0], 400)

    async def test_cli_effect_control_and_inspection_use_only_http(self):
        async def cli(*arguments, payload=None):
            env = {**os.environ, 'PYTHONPATH': str(RUNTIME), 'GTD_API_TOKEN': OWNER}
            process = await asyncio.create_subprocess_exec(sys.executable, '-B', '-m', 'gtd_felix',
                '--url', self.url, *arguments, env=env, stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
            out, err = await process.communicate(json.dumps(payload).encode() if payload else b'')
            self.assertEqual(process.returncode, 0, err.decode())
            return json.loads(out)
        proposed = await cli('control', 'propose_effect', payload={'operation_id': 'cli', 'proposal': self.proposal()})
        self.assertEqual(proposed['status'], 'proposed')
        result = await cli('effect', proposed['effect']['id'])
        self.assertFalse(result['delivery_configured'])
        self.assertEqual(len(await cli('effects')), 1)
