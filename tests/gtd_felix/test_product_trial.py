"""Owned child HTTP processes only. No Hermes invocation or model call."""
import asyncio
import importlib.util
import json
import os
from pathlib import Path
import socket
import sys
import tempfile
import unittest
from unittest.mock import patch, AsyncMock

from runtime_location import RUNTIME

SPEC = importlib.util.spec_from_file_location('gtd_product_trial', Path(__file__).resolve().parents[2] / 'scripts/gtd_product_trial.py')
trial = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(trial)

DUMMY = '''
from http.server import BaseHTTPRequestHandler, HTTPServer
import json, os, sys, tempfile
from pathlib import Path
from gtd_felix import GTDService
service = GTDService(Path(sys.argv[2]))
if not service.query():
    item = service.capture('felix', 'synthetic-capture', 'Survives owned restart')['item']
    service.execute('gtd-felix', {'operation_id': 'prepared', 'action': 'put_material', 'item_id': item['id'], 'expected_version': item['version'], 'fields': {'content': 'Synthetic prepared state'}})
class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args): pass
    def do_POST(self):
        self.rfile.read(int(self.headers.get('Content-Length', '0')))
        self.send_response(200); self.end_headers(); self.wfile.write(b'[]')
    def do_GET(self):
        if self.path == '/v1/export':
            with tempfile.TemporaryDirectory() as t:
                path = Path(t) / 'snapshot.zip'
                service.export(path)
                body = path.read_bytes()
        elif self.path == '/health/detailed':
            body = json.dumps({'pid': os.getpid(), 'platforms': {'api_server': {}}}).encode()
        elif self.path == '/v1/items':
            body = json.dumps(service.query()).encode()
        else:
            body = b'{"status":"ok"}'
        self.send_response(200); self.send_header('Content-Type', 'application/zip' if self.path == '/v1/export' else 'application/json'); self.end_headers(); self.wfile.write(body)
HTTPServer(('127.0.0.1', int(sys.argv[1])), Handler).serve_forever()
'''


def free_port():
    with socket.socket() as sock:
        sock.bind(('127.0.0.1', 0))
        return sock.getsockname()[1]


class SafetyTests(unittest.TestCase):
    def test_default_does_not_execute(self):
        with patch.object(trial, 'load_config', side_effect=AssertionError('must not read or execute')):
            self.assertEqual(1, trial.main(['--config','/missing','--evidence-dir','/missing','--case','G9']))

    def test_environment_drops_ambient_credentials_and_secrets_never_argv(self):
        with patch.dict(os.environ, {'OPENAI_API_KEY':'ambient', 'GTD_API_TOKEN':'ambient',
                                    'TELEGRAM_BOT_TOKEN':'ambient', 'PYTHONPATH':'/ambient'}):
            env = trial.clean_environment('/synthetic-home', {'API_SERVER_KEY':'explicit'})
        self.assertNotIn('OPENAI_API_KEY', env)
        self.assertNotIn('GTD_API_TOKEN', env)
        self.assertNotIn('TELEGRAM_BOT_TOKEN', env)
        self.assertNotIn('PYTHONPATH', env)
        self.assertEqual(os.environ.get('HOME'), env.get('HOME'))
        self.assertEqual('explicit', env['API_SERVER_KEY'])

    def test_private_file_permissions_symlink_and_forbidden_environment(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'key'
            path.write_text('synthetic-secret'); path.chmod(0o600)
            self.assertEqual({'API_SERVER_KEY':'synthetic-secret'}, trial.file_environment({'API_SERVER_KEY':str(path)}))
            for name in ('HOME','LD_PRELOAD','TELEGRAM_BOT_TOKEN'):
                with self.assertRaises(trial.TrialError): trial.file_environment({name:str(path)})
            path.chmod(0o644)
            with self.assertRaises(trial.TrialError): trial.private_bytes(str(path))
            path.chmod(0o600)
            link = path.with_name('linked'); link.symlink_to(path)
            with self.assertRaises(trial.TrialError): trial.private_bytes(str(link))

    def test_existing_listener_is_not_reused(self):
        with socket.socket() as sock:
            sock.bind(('127.0.0.1', 0)); sock.listen()
            with self.assertRaisesRegex(trial.TrialError, 'port_already_occupied'):
                trial.check_free_port('http://127.0.0.1:' + str(sock.getsockname()[1]))

    def test_closed_http_connection_does_not_block_owned_restart(self):
        with socket.socket() as listener:
            listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            listener.bind(('127.0.0.1', 0)); listener.listen()
            address = listener.getsockname()
            with socket.create_connection(address, timeout=2) as client:
                connection, _ = listener.accept()
                with connection:
                    client.sendall(b'GET / HTTP/1.0\r\n\r\n')
                    connection.recv(1024)
                    connection.sendall(b'HTTP/1.0 200 OK\r\nContent-Length: 0\r\n\r\n')
                    connection.shutdown(socket.SHUT_WR)
                    while client.recv(1024):
                        pass
        trial.check_free_port('http://127.0.0.1:' + str(address[1]))


class ProcessTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        import aiohttp
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.dummy = self.root / 'dummy.py'; self.dummy.write_text(DUMMY)
        self.port = free_port()
        self.url = f'http://127.0.0.1:{self.port}'
        self.config = {'python':sys.executable, 'runtime_root':str(RUNTIME), 'product_api_url':self.url,
            'service_config':str(self.root/'service.json'), 'gateways':[],
            'limits':{'startup_seconds':5,'case_seconds':5,'total_seconds':20,'cleanup_seconds':3,'request_seconds':2},
            'probe':{'owner_token_env':'SYNTHETIC_OWNER_TOKEN'}}
        self.supervisor = trial.Supervisor(self.config, {'data_dir':str(self.root/'data')},
            {'SYNTHETIC_OWNER_TOKEN':'synthetic-token'}, self.root)
        self.session = aiohttp.ClientSession()
        self.supervisor.session = self.session

    async def asyncTearDown(self):
        for process in self.supervisor.processes:
            await process.stop(2)
        await self.session.close()
        self.temp.cleanup()

    async def start_dummy(self):
        trial.check_free_port(self.url)
        env = trial.clean_environment(self.root, {'PYTHONPATH':str(RUNTIME)})
        process = trial.OwnedProcess('service', [sys.executable, '-B', str(self.dummy), str(self.port), str(self.root/'data')], env, self.root)
        self.supervisor.processes.append(process)
        await process.start()
        self.supervisor.service = process
        await self.supervisor.ready(process, self.url)
        return process

    def configure_gateway(self, output='[]', exit_code=0):
        home, board, workspace = [self.root / name for name in ('native', 'kanban', 'workspace')]
        for directory in (home, board, workspace): directory.mkdir()
        key = self.root / 'gateway-key'; key.write_text('synthetic-key'); key.chmod(0o600)
        cli = self.root / 'native-cli'
        cli.write_text('#!' + sys.executable + '\nimport os,sys\nfrom pathlib import Path\n'
            'assert sys.argv[1:]==["kanban","--board","default","list","--json"]\n'
            'assert os.environ["HERMES_KANBAN_BOARD"]=="default"\n'
            'Path(os.environ["HERMES_KANBAN_DB"]).touch()\n'
            + 'print(' + repr(output) + ')\nsys.exit(' + str(exit_code) + ')\n')
        cli.chmod(0o700)
        gateway = {'home': str(home), 'kanban_home': str(board), 'workspace': str(workspace),
            'base_url': 'http://127.0.0.1:' + str(free_port()), 'cli': str(cli),
            'env_files': {'API_SERVER_KEY': str(key)}}
        guard = {'profile': str(home), 'kanban_home': str(board), 'board': 'default',
            'kanban_db': str(board / 'kanban.db'), 'hermes': str(cli)}
        route = {'base_url': gateway['base_url'], 'hermes_home': str(home), 'kanban_home': str(board),
            'workspace': str(workspace), 'native_guard': guard, 'model': 'gpt-6-astra',
            'reasoning_effort': 'low', 'api_key_env': 'SYNTHETIC_GATEWAY_KEY'}
        self.config['gateways'] = [gateway]
        self.supervisor.service_config['hermes'] = {'routes': {'fixture': route}}
        return gateway, guard

    async def test_board_initialized_by_owned_cli_before_gateway_with_exact_environment(self):
        gateway, guard = self.configure_gateway()
        env = self.supervisor.gateway_environment(gateway)
        self.assertEqual(env['HERMES_KANBAN_BOARD'], 'default')
        self.assertEqual(env['HERMES_KANBAN_DB'], guard['kanban_db'])
        events = []
        original = self.supervisor.initialize_board
        async def initialize(gateway, env):
            events.append('initialize')
            await original(gateway, env)
            self.assertTrue(Path(guard['kanban_db']).is_file())
        async def gateway_start(process):
            events.append('gateway')
            self.assertTrue(Path(guard['kanban_db']).is_file())
            raise trial.TrialError('synthetic_stop_before_gateway')
        with patch.object(self.supervisor, 'verify_python', AsyncMock()), \
             patch.object(self.supervisor, 'native_configuration', AsyncMock(return_value={})), \
             patch.object(self.supervisor, 'initialize_board', initialize), \
             patch.object(trial.OwnedProcess, 'start', gateway_start), \
             patch.object(trial.OwnedProcess, 'stop', AsyncMock()), \
             patch.object(trial, 'previous_processes', return_value=[]):
            result = await self.supervisor.run('G7')
        self.assertEqual(events, ['initialize', 'gateway'])
        recorded = result['configuration_processes'][0]
        self.assertIsInstance(recorded['pid'], int)
        self.assertEqual(recorded['returncode'], 0)

    async def test_failed_board_initialization_never_starts_gateway_or_service(self):
        gateway, guard = self.configure_gateway(exit_code=1)
        with patch.object(self.supervisor, 'verify_python', AsyncMock()), \
             patch.object(self.supervisor, 'native_configuration', AsyncMock(return_value={})), \
             patch.object(trial.OwnedProcess, 'start', AsyncMock()) as gateway_start, \
             patch.object(self.supervisor, 'start_service', AsyncMock()) as service_start:
            result = await self.supervisor.run('G7')
        gateway_start.assert_not_awaited()
        service_start.assert_not_awaited()
        self.assertEqual(result['status'], 'BLOCKED')
        self.assertEqual(result['configuration_processes'][0]['returncode'], 1)

    async def test_board_rejects_preexisting_database_and_nonempty_inventory(self):
        gateway, guard = self.configure_gateway(output='[{"id":"previous"}]')
        env = self.supervisor.gateway_environment(gateway)
        with self.assertRaisesRegex(trial.TrialError, 'initial_kanban_inventory_not_empty'):
            await self.supervisor.initialize_board(gateway, env)
        with self.assertRaisesRegex(trial.TrialError, 'previous_kanban_state_refused'):
            await self.supervisor.initialize_board(gateway, env)
        for field, value in (('kanban_db', str(self.root / 'foreign.db')), ('board', 'other')):
            original = guard[field]; guard[field] = value
            with self.assertRaises(trial.TrialError): self.supervisor.gateway_environment(gateway)
            guard[field] = original

    async def test_named_board_matches_native_path_resolver(self):
        native_python = Path('/home/felix/.hermes/hermes-agent/venv/bin/python')
        if not native_python.exists(): self.skipTest('native Hermes unavailable')
        gateway, guard = self.configure_gateway()
        import subprocess
        env = trial.clean_environment(gateway['home'], {'HERMES_HOME': gateway['home'],
            'HERMES_KANBAN_HOME': gateway['kanban_home']})
        code = "import sys; sys.path.insert(0, '/home/felix/.hermes/hermes-agent'); from hermes_cli.kanban_db import kanban_db_path; print(kanban_db_path('synthetic'))"
        result = subprocess.run([str(native_python), '-B', '-c', code], env=env,
            capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        native_path = result.stdout.strip()
        self.assertEqual(native_path, str(Path(gateway['kanban_home']) / 'kanban/boards/synthetic/kanban.db'))
        guard.update(board='synthetic', kanban_db=native_path)
        self.assertEqual(trial.gateway_board(self.supervisor.service_config, gateway), ('synthetic', native_path))
        guard['kanban_db'] = str(Path(gateway['kanban_home']) / 'boards/synthetic/kanban.db')
        with self.assertRaisesRegex(trial.TrialError, 'gateway_board_database_mismatch'):
            trial.gateway_board(self.supervisor.service_config, gateway)

    async def test_load_config_accepts_only_empty_trial_and_exact_board_contract(self):
        from datetime import datetime, timezone
        gateway, guard = self.configure_gateway()
        owner_key = self.root / 'owner-key'; owner_key.write_text('synthetic-token'); owner_key.chmod(0o600)
        self.config.update(synthetic=True, model='gpt-6-astra', reasoning_effort='low',
            environment_files={'SYNTHETIC_OWNER_TOKEN': str(owner_key),
                               'SYNTHETIC_GATEWAY_KEY': gateway['env_files']['API_SERVER_KEY']})
        self.config['probe'].update(max_http_calls=20, poll_interval_seconds=.1)
        self.supervisor.service_config.update(listen_host='127.0.0.1', port=self.port,
            actors={'owner': 'felix'}, api_tokens={'synthetic-token': 'felix'}, orchestration={'enabled': True},
            budget={'period_start': datetime.now(timezone.utc).isoformat(), 'period_seconds': 3600,
                'max_cost_usd': 1, 'max_runtime_seconds': 100, 'max_job_runtime_seconds': 30,
                'recovery_cost_usd': 0, 'recovery_runtime_seconds': 0, 'max_retries': 0, 'max_descendants': 0})
        filename = self.root / 'trial.json'
        filename.write_text(json.dumps(self.config)); filename.chmod(0o600)
        service_path = Path(self.config['service_config'])
        service_path.write_text(json.dumps(self.supervisor.service_config)); service_path.chmod(0o600)
        trial.load_config(str(filename))
        Path(guard['kanban_db']).touch()
        with self.assertRaisesRegex(trial.TrialError, 'previous_kanban_state_refused'):
            trial.load_config(str(filename))
        Path(guard['kanban_db']).unlink()
        guard['kanban_db'] = str(self.root / 'foreign.db')
        service_path.write_text(json.dumps(self.supervisor.service_config))
        with self.assertRaisesRegex(trial.TrialError, 'gateway_board_database_mismatch'):
            trial.load_config(str(filename))

    async def test_board_initialization_timeout_reaps_owned_process_without_gateway(self):
        gateway, _ = self.configure_gateway()
        Path(gateway['cli']).write_text('#!' + sys.executable + '\nimport time\ntime.sleep(10)\n')
        with patch.object(self.supervisor, 'verify_python', AsyncMock()), \
             patch.object(self.supervisor, 'native_configuration', AsyncMock(return_value={})), \
             patch.object(self.supervisor, 'remaining', return_value=.1), \
             patch.object(trial.OwnedProcess, 'start', AsyncMock()) as gateway_start:
            result = await self.supervisor.run('G7')
        gateway_start.assert_not_awaited()
        self.assertEqual(result['status'], 'BLOCKED')
        process = result['configuration_processes'][0]
        self.assertIsNotNone(process['returncode'])
        self.assertFalse(Path('/proc', str(process['pid'])).exists())

    async def test_owned_http_pid_check_restart_preserves_real_exported_state(self):
        process = await self.start_dummy()
        health = await self.supervisor.ready(process, self.url, 'synthetic-token', gateway=True)
        self.assertEqual(process.process.pid, health['pid'])
        driver_config = {'synthetic':True, 'product_api_url':self.url, 'owner_token_env':'SYNTHETIC_OWNER_TOKEN',
            'timeout_seconds':10,'max_http_calls':20,'max_cases':1,'poll_interval_seconds':.01}
        with patch.dict(os.environ, {'SYNTHETIC_OWNER_TOKEN':'synthetic-token'}):
            driver = trial.acceptance.ProductDriver(driver_config, self.session, self.root)
        with patch.object(self.supervisor, 'start_service', self.start_dummy), patch.object(self.supervisor, 'suspend_owned_bots', AsyncMock(return_value=True)):
            result = await self.supervisor.restart_service(driver, {'run_id':'restart-test'})
        self.assertNotEqual(result['before_process_id'], result['after_process_id'])
        self.assertTrue(result['before_stopped']['pid_absent'])
        self.assertTrue(result['after_ready'])
        self.assertTrue(result['state_ids_preserved'])
        for name in ('before','after'):
            snapshot = trial.acceptance.load_snapshot(self.root/result[name]['file'], result[name]['sha256'])
            self.assertEqual('Survives owned restart', next(iter(snapshot['items'].values()))['title'])
        record = {'case':'G8', 'status':'COLLECTED', 'transport':'product_http',
            'before':result['before'], 'after':result['after'], 'restart':result,
            'http_trace':driver.trace, 'aliases':{}}
        self.assertEqual('NOT_RUN', trial.acceptance.evaluate_record(record, self.root)['status'])
        result['before_process_id'] = 1
        with self.assertRaisesRegex(ValueError, 'restart_receipt_mismatch'):
            trial.acceptance.evaluate_record(record, self.root)

    async def test_previous_gateway_process_is_detected_by_exact_home(self):
        env = trial.clean_environment(self.root, {'HERMES_HOME':str(self.root/'gateway')})
        owned = trial.OwnedProcess('previous', [sys.executable, '-B', '-c', 'import time; time.sleep(10)'], env, self.root)
        self.supervisor.processes.append(owned)
        pid = await owned.start()
        self.assertIn(pid, trial.previous_processes([self.root/'gateway']))
        await owned.stop(2)
        self.assertNotIn(pid, trial.previous_processes([self.root/'gateway']))

    async def test_restart_failure_records_safe_phase_without_exception_content(self):
        await self.start_dummy()
        config = {'synthetic':True, 'product_api_url':self.url, 'owner_token_env':'SYNTHETIC_OWNER_TOKEN',
            'timeout_seconds':10,'max_http_calls':20,'max_cases':1,'poll_interval_seconds':.01}
        with patch.dict(os.environ, {'SYNTHETIC_OWNER_TOKEN':'synthetic-token'}):
            driver = trial.acceptance.ProductDriver(config, self.session, self.root)
        with patch.object(self.supervisor, 'start_service', AsyncMock(side_effect=RuntimeError('synthetic-secret'))), patch.object(self.supervisor, 'suspend_owned_bots', AsyncMock(return_value=True)):
            with self.assertRaises(RuntimeError):
                await self.supervisor.restart_service(driver, {'run_id':'failed-restart'})
        self.assertEqual({'phase':'start_after_stop','code':'service_start_failed'}, self.supervisor.receipt['restart_failure'])
        self.assertNotIn('synthetic-secret', json.dumps(self.supervisor.receipt))

    async def test_health_with_wrong_pid_is_rejected_without_killing_other_pid(self):
        owned = await self.start_dummy()
        with patch.object(self.supervisor, 'http', AsyncMock(return_value={'pid':1,'platforms':{}})):
            with self.assertRaisesRegex(trial.TrialError, 'gateway_pid_mismatch'):
                await self.supervisor.ready(owned, self.url, gateway=True)
        self.assertIsNone(owned.process.returncode)

    async def test_private_process_log_is_hashed_without_disclosing_content(self):
        owned = trial.OwnedProcess('logger', [sys.executable, '-B', '-c', 'print("synthetic-secret-log")'],
            trial.clean_environment(self.root), self.root, log_dir=self.root)
        self.supervisor.processes.append(owned)
        await owned.start()
        await owned.process.wait()
        receipt = await owned.stop(1)
        path = Path(receipt['log_path'])
        self.assertEqual(0o600, path.stat().st_mode & 0o777)
        self.assertEqual(trial.acceptance.sha(path.read_bytes()), receipt['log_sha256'])
        self.assertNotIn('synthetic-secret-log', json.dumps(receipt))

    async def test_cleanup_suspends_only_configured_bots_preserving_identity(self):
        self.supervisor.service_config['bots'] = [{'id':'own-bot'}]
        own = {'id':'own-bot','state':'available','profile':'synthetic','source_urn':'urn:test','capabilities':['prepare_private']}
        other = {'id':'unrelated-bot','state':'available'}
        responses = [[own, other], {'status':'applied'}]
        with patch.object(self.supervisor, 'http', AsyncMock(side_effect=responses)) as request:
            self.assertTrue(await self.supervisor.suspend_owned_bots())
        body = request.await_args_list[1].args[3]
        self.assertEqual({**own,'state':'suspended'}, body['bot'])
        self.assertEqual(['own-bot'], self.supervisor.receipt['suspended_bots'])

    async def test_native_job_stop_waits_for_observed_terminal(self):
        responses = [
            [{'id':'own-job','terminal':False,'native':{'id':'native-7'}}],
            {'status':'stop_requested'},
            {'id':'own-job','terminal':False},
            [], {'id':'own-job','terminal':True,'observations':[{'native_status':'cancelled'}]}]
        with patch.object(self.supervisor, 'http', AsyncMock(side_effect=responses)):
            self.assertTrue(await self.supervisor.stop_jobs())
        observed = self.supervisor.receipt['job_stop_observations'][0]
        self.assertTrue(observed['terminal'])
        self.assertEqual('cancelled', observed['observation'][0]['native_status'])

    async def test_lost_job_observation_keeps_native_identity_uncertain(self):
        responses = [[{'id':'own-job','terminal':False,'native':{'id':'native-7'}}],
                     {'status':'stop_requested'}, RuntimeError('synthetic response lost')]
        with patch.object(self.supervisor, 'http', AsyncMock(side_effect=responses)):
            self.assertFalse(await self.supervisor.stop_jobs())
        self.assertEqual('native-7', self.supervisor.receipt['unresolved_jobs'][0]['native']['id'])
        self.assertFalse(self.supervisor.receipt['unresolved_jobs'][0]['terminal'])
