"""No network or model calls: job binding, lifecycle and private child boundaries."""
import asyncio
import json
import multiprocessing
import os
import signal
import time
import tempfile
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch, AsyncMock

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from gtd_felix import gmail_bridge as bridge

MARKER = 'PRIVATE_MAIL_BODY_MUST_NOT_ESCAPE_91ad'


def private_child(pipe, directory, sqlite=False):
    def fake_infer(credentials, text):
        sys.addaudithook(bridge._deny_writes)
        print(text)
        if sqlite:
            import sqlite3
            connection = sqlite3.connect(str(Path(directory, 'leak.sqlite')))
            connection.execute('CREATE TABLE leaks (body TEXT)')
            connection.execute('INSERT INTO leaks VALUES (?)', (text,))
            connection.commit()
        else:
            Path(directory, 'leak.txt').write_text(text)
        raise RuntimeError(text)
    bridge._infer = fake_infer
    bridge._child(pipe)


class Pipe:
    def __init__(self, context):
        self.context = context
        self.closed = False
    def send(self, value):
        self.context.envelope = value
    def poll(self):
        return self.context.ready and hasattr(self.context, 'envelope')
    def recv(self):
        return self.context.result
    def close(self):
        self.closed = True


class Process:
    def __init__(self, context, **kwargs):
        self.context = context
        self.kwargs = kwargs
        self.alive = False
        self.joined = False
        self.closed = False
    def start(self):
        self.alive = True
    def is_alive(self):
        return self.alive
    def terminate(self):
        self.alive = False
    def kill(self):
        self.alive = False
    def join(self, timeout):
        self.joined = True
    def close(self):
        self.closed = True


class FakeLifetime:
    def __init__(self, process):
        self.process = process
    def attach(self):
        pass
    def dead(self):
        return not self.process.alive
    def send_signal(self, sig):
        self.process.alive = False
    def close(self):
        self.process.join(0)
        self.process.close()


def reaped_result_child(pipe):
    pipe.recv()
    pipe.send(bridge.closed_result({'classification': 'selected', 'reason_code': 'gtd_relevant'}))
    pipe.close()


def waiting_child(pipe):
    pipe.recv()
    time.sleep(30)


class RealContext:
    def __init__(self, target):
        self.context = multiprocessing.get_context('spawn')
        self.target = target
    def Pipe(self, duplex):
        return self.context.Pipe(duplex)
    def Process(self, **kwargs):
        kwargs['target'] = self.target
        self.process = self.context.Process(**kwargs)
        return self.process


class Context:
    def __init__(self, ready=True):
        self.ready = ready
        self.result = bridge.closed_result({'classification': 'selected', 'reason_code': 'gtd_relevant'},
                                          {'input_tokens': 100, 'output_tokens': 5})
    def Pipe(self, duplex):
        self.pipes = Pipe(self), Pipe(self)
        return self.pipes
    def Process(self, **kwargs):
        self.process = Process(self, **kwargs)
        return self.process


class BridgeTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.parent = SimpleNamespace(provider='openai-codex', model='gpt-6-astra',
            api_mode='codex_responses', api_key='PRIVATE_CREDENTIAL', base_url='https://example.invalid',
            is_interrupted=False)
        self.adapter = SimpleNamespace(_active_run_agents={'run': self.parent})
        self.transport = SimpleNamespace(is_closing=lambda: False)
        self.request = SimpleNamespace(transport=self.transport)
        self.payload = dict(job_id='job', run_id='run', evaluation_id='random-private-nonce',
                            external_id='m1', revision='message:10', text=MARKER)
        self.bindings = []
        self.context = Context()
    async def valid(self, binding):
        self.bindings.append(binding)
        return 10.0
    async def call(self, validator=None):
        return await bridge.evaluate(self.adapter, self.request, self.payload,
                                     validator=validator or self.valid, context=self.context, lifetime_factory=FakeLifetime)
    def assert_closed(self):
        self.assertFalse(bridge._BUSY)
        self.assertTrue(self.context.process.joined)
        self.assertTrue(self.context.process.closed)
        self.assertTrue(all(pipe.closed for pipe in self.context.pipes))
    async def test_binding_exact_and_credentials_only_pipe(self):
        result = await self.call()
        self.assertEqual('selected', result['classification'])
        self.assertEqual({'job_id','run_id','evaluation_id','digest'}, set(self.bindings[0]))
        self.assertEqual(bridge.evidence_digest(self.payload), self.bindings[0]['digest'])
        self.assertNotIn(MARKER, json.dumps(result))
        self.assertNotIn('PRIVATE_CREDENTIAL', repr(self.context.process.kwargs))
        self.assertEqual('PRIVATE_CREDENTIAL', self.context.envelope['credentials']['api_key'])
        self.assert_closed()
    async def test_provider_mismatch_before_child_or_validation(self):
        self.parent.model = 'other'
        with self.assertRaisesRegex(ValueError, '^provider_mismatch$'):
            await self.call()
        self.assertEqual([], self.bindings)
        self.assertFalse(hasattr(self.context, 'process'))
    async def test_binding_revoked_after_result(self):
        async def valid(binding):
            self.bindings.append(binding)
            return 0 if len(self.bindings) >= 3 else 10
        with self.assertRaisesRegex(ValueError, 'evaluation_not_active'):
            await self.call(valid)
        self.assert_closed()
    async def test_interrupt_identity_and_disconnect_close_child(self):
        for mode in ('interrupt', 'identity', 'disconnect'):
            self.setUp()
            self.context.ready = False
            async def stop():
                await asyncio.sleep(.01)
                if mode == 'interrupt':
                    self.parent.is_interrupted = True
                elif mode == 'identity':
                    self.adapter._active_run_agents['run'] = object()
                else:
                    self.request.transport = None
            task = asyncio.create_task(stop())
            with self.assertRaisesRegex(ValueError, 'evaluation_cancelled'):
                await self.call()
            await task
            self.assert_closed()
    async def test_cancel_task_joins_and_global_singleton(self):
        self.context.ready = False
        task = asyncio.create_task(self.call())
        await asyncio.sleep(.01)
        with self.assertRaisesRegex(ValueError, 'helper_busy'):
            await self.call()
        task.cancel()
        with self.assertRaises(asyncio.CancelledError):
            await task
        self.assert_closed()
    async def test_timeout_is_bounded(self):
        self.context.ready = False
        async def short(binding):
            return .001
        with self.assertRaisesRegex(ValueError, 'evaluation_cancelled'):
            await self.call(short)
        self.assert_closed()
    async def test_validation_wait_keeps_stop_and_disconnect_responsive(self):
        for mode in ('stop', 'disconnect'):
            self.setUp()
            waiting = asyncio.Event()
            joined = asyncio.Event()
            async def slow(binding):
                waiting.set()
                try:
                    await asyncio.sleep(10)
                    return 10
                finally:
                    joined.set()
            task = asyncio.create_task(self.call(slow))
            await waiting.wait()
            if mode == 'stop':
                self.parent.is_interrupted = True
            else:
                self.request.transport = None
            with self.assertRaisesRegex(ValueError, 'evaluation_cancelled'):
                await asyncio.wait_for(task, .5)
            self.assertTrue(joined.is_set())
            self.assertFalse(hasattr(self.context, 'process'))
            self.assertFalse(bridge._BUSY)

    async def test_stop_during_child_revalidation_joins_both_tasks(self):
        waiting = asyncio.Event()
        joined = asyncio.Event()
        calls = 0
        async def slow_second(binding):
            nonlocal calls
            calls += 1
            if calls == 1:
                return 10
            waiting.set()
            try:
                await asyncio.sleep(10)
                return 10
            finally:
                joined.set()
        task = asyncio.create_task(self.call(slow_second))
        await waiting.wait()
        self.parent.is_interrupted = True
        with self.assertRaisesRegex(ValueError, 'evaluation_cancelled'):
            await asyncio.wait_for(task, .5)
        self.assertTrue(joined.is_set())
        self.assert_closed()

    async def test_initial_validation_is_inside_absolute_deadline(self):
        joined = asyncio.Event()
        async def slow(binding):
            try:
                await asyncio.sleep(10)
                return 20
            finally:
                joined.set()
        with patch.object(bridge, 'MAX_SECONDS', .08):
            with self.assertRaisesRegex(ValueError, 'evaluation_cancelled'):
                await asyncio.wait_for(self.call(slow), .5)
        self.assertTrue(joined.is_set())
        self.assertFalse(hasattr(self.context, 'process'))
        self.assertFalse(bridge._BUSY)

    async def test_http_validation_delay_and_timeout_have_distinct_results(self):
        from aiohttp import web
        from aiohttp.test_utils import TestServer
        async def handler(request):
            self.assertEqual('Bearer stub-token', request.headers['Authorization'])
            await asyncio.sleep(1.2)
            return web.json_response({'allowed': True, 'remaining_seconds': 17})
        app = web.Application()
        app.router.add_post('/v1/source-evaluation/validate', handler)
        async with TestServer(app) as server:
            with patch.dict('os.environ', {'GTD_API_URL': str(server.make_url('/')).rstrip('/'),
                                          'GTD_API_TOKEN': 'stub-token'}):
                self.assertEqual(17, await bridge.service_validate({'job_id': 'stub'}))
                with patch.object(bridge, 'VALIDATION_TIMEOUT_SECONDS', .02):
                    with self.assertRaisesRegex(ValueError, '^validation_timeout$'):
                        await bridge.service_validate({'job_id': 'stub'})
        self.assertEqual('validation_timeout', bridge.error_code(ValueError('validation_timeout')))

    async def test_real_spawn_externally_reaped_then_second_evaluation(self):
        context = RealContext(reaped_result_child)
        calls = 0
        async def validator(binding):
            nonlocal calls
            calls += 1
            if calls == 3:  # Final validation: pipe result arrived, let competing reaper win.
                pid = context.process.pid
                for _ in range(100):
                    if os.waitpid(pid, os.WNOHANG)[0] == pid:
                        break
                    await asyncio.sleep(.01)
                else:
                    self.fail('synthetic child did not exit')
                self.assertTrue(context.process.is_alive())  # Reproduces CPython's stale state.
            return 10
        result = await bridge.evaluate(self.adapter, self.request, self.payload,
                                       validator=validator, context=context)
        self.assertEqual('selected', result['classification'])
        self.assertTrue(context.process._closed)
        self.assertFalse(bridge._BUSY)
        self.assertEqual('selected', (await self.call())['classification'])

    async def test_real_spawn_cancellation_is_shielded_until_death(self):
        context = RealContext(waiting_child)
        attached = asyncio.Event()
        lifetimes = []
        class Guard(bridge._ChildLifetime):
            def attach(self):
                super().attach()
                lifetimes.append(self)
                attached.set()
        task = asyncio.create_task(bridge.evaluate(self.adapter, self.request, self.payload,
            validator=self.valid, context=context, lifetime_factory=Guard))
        await attached.wait()
        task.cancel()
        await asyncio.sleep(.001)
        task.cancel()
        with self.assertRaises(asyncio.CancelledError):
            await task
        self.assertTrue(lifetimes[0].death_proven)
        self.assertTrue(context.process._closed)
        self.assertFalse(bridge._BUSY)

    async def test_start_failure_does_not_leak_busy(self):
        with patch.object(Process, 'start', side_effect=RuntimeError('synthetic_start_failure')):
            with self.assertRaises(RuntimeError):
                await self.call()
        self.assert_closed()

    async def test_cleanup_failure_while_alive_rejects_result_and_next_helper(self):
        class Stuck(FakeLifetime):
            def send_signal(self, sig):
                pass
        async def failed_cleanup(lifetime, pipe, peer):
            raise ValueError('helper_cleanup_pending')
        with patch.object(bridge, '_cleanup_child', new=failed_cleanup):
            with self.assertRaisesRegex(ValueError, '^helper_cleanup_pending$'):
                await bridge.evaluate(self.adapter, self.request, self.payload,
                    validator=self.valid, context=self.context, lifetime_factory=Stuck)
        self.assertTrue(bridge._BUSY)
        with self.assertRaisesRegex(ValueError, '^helper_busy$'):
            await self.call()
        # Synthetic fixture has no OS process; release only for subsequent tests.
        self.context.process.alive = False
        bridge._BUSY = False

    def test_closed_output_never_quotes_model_error(self):
        for raw in (MARKER, {'classification': 'noise', 'reason_code': MARKER},
                    {'classification':'noise','reason_code':'non_actionable','text':MARKER}):
            output = bridge.closed_result(raw, {'input_tokens': MARKER, 'output_tokens': -1})
            self.assertEqual('uncertain', output['classification'])
            self.assertNotIn(MARKER, json.dumps(output))
    def test_closed_diagnostic_codes_do_not_stringify_exceptions(self):
        class HostileError(Exception):
            def __str__(self):
                raise AssertionError('must not stringify')
        for error, expected in [(ValueError('provider_mismatch'), 'provider_mismatch'),
                (ValueError(MARKER), 'bridge_value_error'),
                (AttributeError(MARKER), 'bridge_attribute_error'),
                (TypeError(MARKER), 'bridge_type_error'),
                (TimeoutError(MARKER), 'bridge_timeout_error'),
                (OSError(MARKER), 'bridge_os_error'),
                (HostileError(MARKER), 'bridge_internal_error')]:
            self.assertEqual(expected, bridge.error_code(error))

    def test_payload_bound_digest_and_no_extra_authority(self):
        old = bridge.evidence_digest(self.payload)
        self.payload['revision'] = 'message:20'
        self.assertNotEqual(old, bridge.evidence_digest(self.payload))
        self.payload['text'] = 'é' * 100001
        with self.assertRaisesRegex(ValueError, '^invalid_request$'):
            bridge.validate_payload(self.payload)
        self.payload['text'] = MARKER
        self.payload['api_key'] = 'no'
        with self.assertRaises(ValueError):
            bridge.validate_payload(self.payload)
    def test_write_audit_rejects_body_files_and_processes(self):
        for event, args in [('open', ('/tmp/' + MARKER, 'w', 1)),
                            ('subprocess.Popen', (MARKER,)), ('os.mkdir', (MARKER,)),
                            ('sqlite3.connect', (MARKER,))]:
            with self.assertRaisesRegex(PermissionError, '^ephemeral_write_denied$'):
                bridge._deny_writes(event, args)
        bridge._deny_writes('open', ('some-import.py', 'r', 0))
    async def test_http_auth_closed_errors_and_single_route(self):
        from aiohttp import web
        from aiohttp.test_utils import TestClient, TestServer
        class Adapter:
            def _http_route_table(self):
                return []
            def _room_grant_token(self, request):
                return request.headers.get('X-Room-Grant')
            def _check_run_auth(self, request, permission):
                self.permission = permission
                if request.headers.get('Authorization') != 'Bearer test':
                    return web.json_response({'error': 'unauthorized'}, status=401)
                return None
        bridge.install_route(Adapter)
        adapter = Adapter()
        app = web.Application(client_max_size=2_000_000)
        routes = adapter._http_route_table()
        self.assertEqual(1, len(routes))
        for method, path, handler in routes:
            app.router.add_route(method, path, handler)
        async with TestClient(TestServer(app)) as client:
            response = await client.post('/v1/gtd/evaluate-mail', json=self.payload)
            self.assertEqual(401, response.status)
            response = await client.post('/v1/gtd/evaluate-mail', json=self.payload,
                headers={'Authorization': 'Bearer test', 'X-Room-Grant': 'grant'})
            self.assertEqual(403, response.status)
            with patch.object(bridge, 'evaluate', new=AsyncMock(side_effect=RuntimeError(MARKER))):
                response = await client.post('/v1/gtd/evaluate-mail', json=self.payload,
                    headers={'Authorization': 'Bearer test'})
                self.assertEqual(409, response.status)
                self.assertEqual({'error': 'bridge_internal_error'}, await response.json())
            with patch.object(bridge, 'evaluate', new=AsyncMock(side_effect=ValueError('inactive_parent'))):
                response = await client.post('/v1/gtd/evaluate-mail', json=self.payload,
                    headers={'Authorization': 'Bearer test'})
                self.assertEqual({'error': 'inactive_parent'}, await response.json())
            self.assertEqual('dispatch', adapter.permission)

    def test_real_spawn_error_body_stays_private_and_no_file(self):
        self._spawn_private_check(False)

    def test_real_spawn_sqlite_body_stays_private_and_no_database(self):
        self._spawn_private_check(True)

    def _spawn_private_check(self, sqlite):
        with tempfile.TemporaryDirectory() as directory:
            context = multiprocessing.get_context('spawn')
            pipe, peer = context.Pipe()
            process = context.Process(target=private_child, args=(peer, directory, sqlite))
            process.start()
            peer.close()
            try:
                pipe.send({'credentials': {'api_key': 'SECRET'}, 'text': MARKER})
                self.assertTrue(pipe.poll(5))
                result = pipe.recv()
                self.assertEqual('evaluation_unavailable', result['reason_code'])
                self.assertNotIn(MARKER, json.dumps(result))
                self.assertEqual([], list(Path(directory).iterdir()))
                process.join(5)
                self.assertFalse(process.is_alive())
            finally:
                if process.is_alive():
                    process.terminate()
                    process.join()
                process.close()
                pipe.close()

    def test_absolute_launcher_does_not_shadow_mcp_sdk(self):
        import subprocess
        hermes_python = bridge.HERMES_ROOT / 'venv/bin/python'
        if not hermes_python.is_file():
            self.skipTest('Pinned Hermes environment unavailable')
        script = """
import importlib.util, pathlib, runpy, sys
path = pathlib.Path(sys.argv[1])
sys.path.insert(0, str(path.parent))
namespace = runpy.run_path(str(path), run_name='bridge_test')
assert importlib.util.find_spec('mcp').origin == str(path.parent / 'mcp.py')
namespace['_prepare_import_path']()
import mcp
assert pathlib.Path(mcp.__file__).name == '__init__.py'
assert hasattr(mcp, 'StdioServerParameters')
from tools import mcp_tool
assert hasattr(mcp_tool, 'StdioServerParameters')
print('installed_mcp_sdk_resolved')
"""
        result = subprocess.run([str(hermes_python), '-B', '-c', script, bridge.__file__],
                                capture_output=True, text=True, timeout=20)
        self.assertEqual(0, result.returncode, 'MCP SDK import regression')
        self.assertIn('installed_mcp_sdk_resolved', result.stdout)

    def test_launcher_rejects_profile_and_unverified_runtime(self):
        with patch.dict('os.environ', {'HERMES_HOME': '/other'}):
            with self.assertRaisesRegex(SystemExit, 'profile_mismatch'):
                bridge.main()
        with patch.dict('os.environ', {'HERMES_HOME': str(bridge.PROFILE_HOME)}), \
             patch.object(bridge.subprocess, 'run', return_value=SimpleNamespace(returncode=0, stdout='wrong')):
            with self.assertRaisesRegex(SystemExit, 'runtime_mismatch'):
                bridge.main()


if __name__ == '__main__':
    unittest.main()
