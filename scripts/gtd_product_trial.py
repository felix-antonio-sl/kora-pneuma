#!/usr/bin/env python3
"""Opt-in supervisor for one synthetic GTD/Hermes product trial.

No installation, direct model endpoint or live database access.
Only new child process identities are controlled; stopping a gateway is never
recorded as proof that its durable jobs stopped.
"""
import argparse
import asyncio
from datetime import datetime, timezone
import importlib.util
import json
import os
from pathlib import Path
import re
import socket
import stat
import sys
import time
from urllib.parse import urlsplit
import uuid

_SPEC = importlib.util.spec_from_file_location('gtd_acceptance_trial_dependency', Path(__file__).with_name('gtd_acceptance_probe.py'))
acceptance = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(acceptance)


class TrialError(Exception):
    """Only fixed public codes, never subprocess output or remote responses."""


def require(condition, code):
    if not condition:
        raise TrialError(code)


def stamp():
    return datetime.now(timezone.utc).isoformat()


def private_bytes(filename):
    path = Path(filename)
    require(path.is_absolute() and not any(p.is_symlink() for p in (path, *path.parents)), 'unsafe_private_path')
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(fd, 'rb') as stream:
        info = os.fstat(stream.fileno())
        require(stat.S_ISREG(info.st_mode) and info.st_uid == os.getuid()
                and stat.S_IMODE(info.st_mode) == 0o600 and info.st_nlink == 1, 'unsafe_private_file')
        data = stream.read(1024 * 1024 + 1)
        require(len(data) <= 1024 * 1024, 'private_file_too_large')
        return data


def absolute_path(value, directory=False):
    require(isinstance(value, str) and Path(value).is_absolute(), 'absolute_path_required')
    path = Path(value)
    require(not any(p.is_symlink() for p in (path, *path.parents)), 'symlink_path_refused')
    if directory:
        require(path.is_dir() and path.stat().st_uid == os.getuid(), 'owned_directory_required')
    return path


def local_address(url):
    value = urlsplit(url)
    require(value.scheme == 'http' and value.hostname in {'127.0.0.1', '::1'} and value.port
            and value.username is None and value.password is None and value.path in {'', '/'}
            and not value.query and not value.fragment, 'explicit_loopback_url_required')
    return value.hostname, value.port


def check_free_port(url):
    host, port = local_address(url)
    with socket.socket(socket.AF_INET6 if ':' in host else socket.AF_INET) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            sock.bind((host, port))
        except OSError:
            raise TrialError('port_already_occupied') from None


def previous_processes(paths):
    """Inspect matching state roots only; never emit environment contents."""
    needles = {str(Path(p)) for p in paths}
    matches = []
    for entry in Path('/proc').iterdir():
        if not entry.name.isdigit() or int(entry.name) == os.getpid():
            continue
        try:
            if entry.stat().st_uid != os.getuid():
                continue
            values = (entry / 'environ').read_bytes().split(b'\0')
            homes = {part.split(b'=', 1)[1].decode(errors='replace') for part in values
                     if part.startswith((b'HERMES_HOME=', b'HERMES_KANBAN_HOME='))}
            if homes & needles:
                matches.append(int(entry.name))
        except (OSError, PermissionError):
            continue
    return matches


RESERVED_ENV = {'HOME', 'PATH', 'PYTHONPATH', 'PYTHONHOME', 'HERMES_HOME', 'HERMES_KANBAN_HOME',
    'HERMES_KANBAN_BOARD', 'HERMES_KANBAN_DB', 'HERMES_KANBAN_TASK',
    'API_SERVER_ENABLED', 'API_SERVER_HOST', 'API_SERVER_PORT', 'HERMES_KANBAN_DISPATCH_IN_GATEWAY'}


def file_environment(mapping):
    require(isinstance(mapping, dict), 'invalid_environment_files')
    result = {}
    for name, filename in mapping.items():
        require(isinstance(name, str) and re.fullmatch(r'[A-Z][A-Z0-9_]*', name)
                and name not in RESERVED_ENV and not name.startswith(('LD_', 'DYLD_'))
                and not any(word in name for word in ('TELEGRAM', 'GOOGLE', 'GMAIL', 'CALENDAR')),
                'environment_name_not_allowed')
        value = private_bytes(filename).decode().strip()
        require(value and '\x00' not in value and '\n' not in value and '\r' not in value, 'invalid_environment_value')
        result[name] = value
    return result


def clean_environment(home, additions=None):
    env = {k: os.environ[k] for k in ('HOME', 'PATH', 'LANG', 'LC_ALL', 'TZ') if k in os.environ}
    # HERMES_HOME selects the profile; HOME retains the operator identity and
    # its explicitly authorized native authentication fallback.
    env.update(PYTHONUNBUFFERED='1', PYTHONDONTWRITEBYTECODE='1')
    env.update(additions or {})
    return env


def require_empty_board(home):
    require(not any(path.name.endswith('.db') or '.db-' in path.name
                    for path in Path(home).rglob('*')), 'previous_kanban_state_refused')


def gateway_board(service, gateway):
    routes = [route for route in service.get('hermes', {}).get('routes', {}).values()
              if route.get('base_url', '').rstrip('/') == gateway['base_url'].rstrip('/')]
    require(routes, 'service_gateway_route_mismatch')
    identities = []
    home = absolute_path(gateway['kanban_home'], directory=True)
    for route in routes:
        guard = route.get('native_guard', {})
        require(isinstance(guard, dict) and guard.get('profile') == gateway['home']
                and guard.get('kanban_home') == str(home) and guard.get('hermes') == gateway['cli'],
                'gateway_guard_identity_mismatch')
        board = guard.get('board')
        require(isinstance(board, str) and re.fullmatch(r'[a-z0-9][a-z0-9_-]*', board),
                'gateway_board_identity_invalid')
        db = absolute_path(guard.get('kanban_db'))
        expected = home / 'kanban.db' if board == 'default' else home / 'kanban' / 'boards' / board / 'kanban.db'
        require(db == expected, 'gateway_board_database_mismatch')
        identities.append((board, str(db)))
    require(len(set(identities)) == 1, 'gateway_board_identity_conflict')
    return identities[0]


def load_config(filename):
    config = json.loads(private_bytes(filename))
    require(config.get('synthetic') is True, 'synthetic_configuration_required')
    require(config.get('model') == 'gpt-6-astra' and config.get('reasoning_effort') == 'low', 'model_constraint_required')
    runtime = absolute_path(config['runtime_root'], directory=True)
    require((runtime / 'gtd_felix/__main__.py').is_file(), 'runtime_unavailable')
    # venv interpreters/console scripts commonly are symlinks. Resolve the exact
    # executable; directory/config paths retain the stricter no-symlink contract.
    for name in ('python',):
        require(Path(config[name]).is_absolute() and os.access(config[name], os.X_OK), 'absolute_executable_required')
    service = json.loads(private_bytes(config['service_config']))
    require(not any(service.get(k) for k in ('telegram','google','gmail','calendar')), 'external_accounts_forbidden')
    data_dir = absolute_path(service['data_dir'])
    require(not data_dir.exists() or (data_dir.is_dir() and not any(data_dir.iterdir())), 'empty_service_state_required')
    host = service.get('listen_host', '127.0.0.1')
    require(host in {'127.0.0.1','::1'} and type(service.get('port')) is int and 0 < service['port'] <= 65535, 'explicit_service_port_required')
    config['product_api_url'] = f"http://{'[' + host + ']' if ':' in host else host}:{service['port']}"
    limits = config.get('limits', {})
    for name in ('startup_seconds','case_seconds','total_seconds','cleanup_seconds','request_seconds'):
        require(type(limits.get(name)) in (int,float) and 0 < limits[name] <= 3600, 'explicit_time_limits_required')
    require(limits['total_seconds'] > limits['startup_seconds'] + limits['cleanup_seconds'], 'insufficient_total_budget')
    probe = config.get('probe', {})
    require(type(probe.get('max_http_calls')) is int and 10 <= probe['max_http_calls'] <= 10000
            and type(probe.get('poll_interval_seconds')) in (int,float) and 0 < probe['poll_interval_seconds'] <= 30,
            'explicit_probe_limits_required')
    env = file_environment(config.get('environment_files', {}))
    require(probe.get('owner_token_env') in env, 'explicit_owner_token_required')
    require(service.get('api_tokens', {}).get(env[probe['owner_token_env']]) == service.get('actors', {}).get('owner'), 'owner_token_mismatch')
    budget = service.get('budget', {})
    for name in ('period_seconds','max_cost_usd','max_runtime_seconds','max_job_runtime_seconds'):
        require(type(budget.get(name)) in (int,float) and budget[name] > 0, 'service_budget_required')
    for name in ('recovery_cost_usd','recovery_runtime_seconds','max_retries','max_descendants'):
        require(type(budget.get(name)) in (int,float) and budget[name] >= 0, 'service_budget_required')
    require(budget.get('max_active', 1) in (1,2), 'invalid_service_concurrency')
    start = datetime.fromisoformat(budget['period_start'])
    require(start.utcoffset() is not None and 0 <= (datetime.now(timezone.utc) - start).total_seconds() < budget['period_seconds'], 'service_budget_inactive')
    gateways = config.get('gateways')
    require(isinstance(gateways, list) and 1 <= len(gateways) <= 2, 'bounded_gateways_required')
    homes, urls = [], [config['product_api_url']]
    for gateway in gateways:
        for name in ('home','kanban_home','workspace'):
            absolute_path(gateway[name], directory=True)
        require(gateway['home'] != gateway['kanban_home'], 'separate_kanban_home_required')
        require(Path(gateway['cli']).is_absolute() and os.access(gateway['cli'], os.X_OK), 'absolute_gateway_cli_required')
        require_empty_board(gateway['kanban_home'])
        homes.extend([gateway['home'], gateway['kanban_home']])
        urls.append(gateway['base_url'])
        require('API_SERVER_KEY' in file_environment(gateway.get('env_files', {})), 'explicit_gateway_key_required')
    require(len(set(homes)) == len(homes) and len(set(urls)) == len(urls), 'duplicate_trial_identity')
    for url in urls:
        check_free_port(url)
    require(not previous_processes(homes), 'previous_gateway_process_refused')
    routes = service.get('hermes', {}).get('routes', {})
    require(routes and service.get('orchestration'), 'configured_orchestrator_required')
    for route in routes.values():
        require(route.get('model') == config['model'] and route.get('reasoning_effort') == config['reasoning_effort'], 'service_route_model_mismatch')
        gateway = next((g for g in gateways if g['base_url'].rstrip('/') == route.get('base_url', '').rstrip('/')), None)
        require(gateway is not None and route.get('hermes_home') == gateway['home'] and route.get('kanban_home') == gateway['kanban_home']
                and route.get('workspace') == gateway['workspace'], 'service_gateway_route_mismatch')
        key_name = route.get('api_key_env')
        require(key_name in env and env[key_name] == file_environment(gateway['env_files'])['API_SERVER_KEY'], 'route_api_key_mismatch')
    for gateway in gateways:
        gateway_board(service, gateway)
    return config, service, env


class OwnedProcess:
    def __init__(self, name, argv, env, cwd, *, log_dir=None):
        self.log_dir = Path(log_dir) if log_dir is not None else Path(cwd)
        self.log = None
        self.name, self.argv, self.env, self.cwd = name, list(argv), env, str(cwd)
        self.process = None
        self.receipt = {'name': name, 'status': 'NOT_RUN'}

    async def start(self):
        require(self.process is None, 'process_already_started')
        log_path = self.log_dir / (self.name + '-' + uuid.uuid4().hex + '.log')
        descriptor = os.open(log_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY | os.O_NOFOLLOW, 0o600)
        self.log = os.fdopen(descriptor, 'wb')
        self.receipt['log_path'] = str(log_path)
        try:
            self.process = await asyncio.create_subprocess_exec(*self.argv, env=self.env, cwd=self.cwd,
                stdin=asyncio.subprocess.DEVNULL, stdout=self.log, stderr=asyncio.subprocess.STDOUT,
                start_new_session=True)
        except BaseException:
            self.log.close()
            raise
        self.receipt.update(pid=self.process.pid, started_at=stamp(), status='RUNNING')
        return self.process.pid

    async def stop(self, timeout):
        if self.process is None:
            return self.receipt
        if self.process.returncode is None:
            self.process.terminate()
            try:
                await asyncio.wait_for(self.process.wait(), max(.1, timeout * .8))
            except TimeoutError:
                self.process.kill()
                await asyncio.wait_for(self.process.wait(), max(.1, timeout * .2))
        if self.log and not self.log.closed:
            self.log.flush()
            os.fsync(self.log.fileno())
            self.log.close()
        self.receipt['log_sha256'] = acceptance.sha(Path(self.receipt['log_path']).read_bytes())
        self.receipt.update(status='STOPPED', returncode=self.process.returncode, stopped_at=stamp(),
            pid_absent=not Path(f'/proc/{self.process.pid}').exists())
        return self.receipt


class Supervisor:
    def __init__(self, config, service, env, evidence_dir):
        self.config, self.service_config, self.env = config, service, env
        self.evidence_dir = Path(evidence_dir)
        self.processes, self.gateways, self.service = [], [], None
        self.session = None
        self.started = time.monotonic()
        self.receipt = {'trial_id': uuid.uuid4().hex, 'status': 'PARTIAL', 'started_at': stamp(), 'checks': {}, 'processes': [], 'unresolved_jobs': [],
            'limits': ['Stopping owned transport processes does not prove durable native jobs stopped.']}

    def remaining(self):
        return max(0, self.config['limits']['total_seconds'] - (time.monotonic() - self.started))

    async def http(self, method, url, token=None, body=None):
        headers = {'Authorization': 'Bearer ' + token} if token else {}
        async with self.session.request(method, url, json=body, headers=headers, allow_redirects=False,
            timeout=min(self.config['limits']['request_seconds'], max(.1, self.remaining()))) as response:
            require(response.status == 200, 'trial_http_failed')
            return await response.json()

    async def configuration_query(self, name, argv, env, cwd):
        path = self.evidence_dir / ('config-' + uuid.uuid4().hex + '.log')
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY | os.O_NOFOLLOW, 0o600)
        process = None
        output = b''
        try:
            with os.fdopen(fd, 'wb') as log:
                process = await asyncio.create_subprocess_exec(*argv, env=env, cwd=cwd,
                    stdin=asyncio.subprocess.DEVNULL, stdout=asyncio.subprocess.PIPE, stderr=log)
                try:
                    output, _ = await asyncio.wait_for(process.communicate(), min(10, max(.1, self.remaining())))
                except BaseException:
                    if process.returncode is None:
                        process.kill()
                        await process.wait()
                    raise
                finally:
                    log.write(output)
                    log.flush()
                    os.fsync(log.fileno())
        finally:
            self.receipt.setdefault('configuration_processes', []).append({
                'name': name, 'pid': process.pid if process else None,
                'returncode': process.returncode if process else None,
                'log_path': str(path), 'log_sha256': acceptance.sha(path.read_bytes())})
        require(process.returncode == 0 and len(output) < 65536, 'native_configuration_unavailable')
        return output

    async def verify_python(self):
        output = await self.configuration_query('python-version', [self.config['python'], '-B', '-c',
            'import sys; print(str(sys.version_info.major) + "." + str(sys.version_info.minor))'],
            clean_environment(Path(self.service_config['data_dir']).parent), self.config['runtime_root'])
        require(output.strip() == b'3.12', 'python312_required')
        self.receipt['checks']['python'] = '3.12'

    async def native_configuration(self, gateway, env):
        observed = {}
        keys = ('model.default','agent.reasoning_effort','agent.max_turns','agent.run_budget_seconds','agent.api_max_retries','platforms')
        for key in keys:
            output = await self.configuration_query(key, [gateway['cli'], 'config', 'get', key, '--json'], env, gateway['workspace'])
            observed[key] = json.loads(output)
        require(observed['model.default'] == 'gpt-6-astra' and observed['agent.reasoning_effort'] == 'low', 'native_model_mismatch')
        require(all(type(observed[k]) in (int,float) and observed[k] > 0 for k in ('agent.max_turns','agent.run_budget_seconds','agent.api_max_retries')), 'native_limits_required')
        require(observed['agent.run_budget_seconds'] <= self.service_config['budget']['max_job_runtime_seconds'], 'native_duration_exceeds_reservation')
        require(observed['agent.api_max_retries'] <= self.service_config['budget']['max_retries'] + 1, 'native_retries_exceed_reservation')
        platforms = observed['platforms']
        require(isinstance(platforms, dict) and all(k == 'api_server' or not v or (isinstance(v,dict) and not v.get('enabled')) for k,v in platforms.items()), 'native_external_platform_forbidden')
        # Keep only nonsecret scalar constraints, not platform configuration.
        return {k:v for k,v in observed.items() if k != 'platforms'}

    def gateway_environment(self, gateway):
        host, port = local_address(gateway['base_url'])
        board, db = gateway_board(self.service_config, gateway)
        additions = file_environment(gateway['env_files'])
        additions.update(HERMES_HOME=gateway['home'], HERMES_KANBAN_HOME=gateway['kanban_home'],
            HERMES_KANBAN_BOARD=board, HERMES_KANBAN_DB=db,
            API_SERVER_ENABLED='true', API_SERVER_HOST=host, API_SERVER_PORT=str(port),
            HERMES_KANBAN_DISPATCH_IN_GATEWAY='true')
        return clean_environment(gateway['home'], additions)

    async def initialize_board(self, gateway, env):
        board, filename = gateway_board(self.service_config, gateway)
        require(env.get('HERMES_KANBAN_BOARD') == board and env.get('HERMES_KANBAN_DB') == filename
                and env.get('HERMES_KANBAN_HOME') == gateway['kanban_home'], 'gateway_board_environment_mismatch')
        require_empty_board(gateway['kanban_home'])
        output = await self.configuration_query('kanban-initialize:' + gateway['base_url'],
            [gateway['cli'], 'kanban', '--board', board, 'list', '--json'], env, gateway['workspace'])
        try:
            inventory = json.loads(output)
        except (ValueError, UnicodeError):
            raise TrialError('initial_kanban_inventory_invalid') from None
        require(inventory == [], 'initial_kanban_inventory_not_empty')
        db = absolute_path(filename)
        require(db.is_file() and db.stat().st_uid == os.getuid(), 'initial_kanban_database_missing')
        self.receipt['checks']['kanban:' + gateway['base_url']] = {
            'status': 'INITIALIZED_EMPTY', 'board': board, 'database': filename, 'task_count': 0}

    async def ready(self, owned, url, token=None, gateway=False):
        deadline = time.monotonic() + min(self.config['limits']['startup_seconds'], max(.1,self.remaining()))
        while time.monotonic() < deadline:
            require(owned.process.returncode is None, 'owned_process_exited_before_ready')
            try:
                response = await self.http('GET', url + ('/health/detailed' if gateway else '/health'), token)
                if gateway:
                    require(response.get('pid') == owned.process.pid, 'gateway_pid_mismatch')
                    require(set(response.get('platforms', {})) <= {'api_server'}, 'gateway_external_platform_active')
                require(owned.process.returncode is None, 'owned_process_exited_after_health')
                return response
            except TrialError as error:
                if str(error) in {'gateway_pid_mismatch','gateway_external_platform_active'}:
                    raise
            except Exception:
                pass
            await asyncio.sleep(.1)
        raise TrialError('owned_process_readiness_timeout')

    async def start_service(self):
        check_free_port(self.config['product_api_url'])
        env = clean_environment(Path(self.service_config['data_dir']).parent, self.env)
        env['PYTHONPATH'] = self.config['runtime_root']
        owned = OwnedProcess('service', [self.config['python'], '-B', '-m', 'gtd_felix', 'serve', '--config', self.config['service_config']], env, self.config['runtime_root'], log_dir=self.evidence_dir)
        self.processes.append(owned)
        await owned.start()
        self.service = owned
        await self.ready(owned, self.config['product_api_url'])
        return owned

    async def restart_service(self, driver, record):
        require(not await driver.request('POST', '/v1/control/pending', {}), 'restart_not_quiescent')
        require(await self.suspend_owned_bots(), 'restart_admission_not_suspended')
        require(not await driver.request('POST', '/v1/control/pending', {}), 'restart_not_quiescent')
        before = await driver.snapshot(record['run_id'] + '-restart-before.zip')
        old_state = acceptance.load_snapshot(self.evidence_dir / before['file'], before['sha256'])
        proof = acceptance.restart_state_proof(old_state, old_state, record.get('principal_actor', 'gtd-felix'))
        require(proof['quiescent'] and proof['elaborated'], 'restart_requires_elaborated_quiescent_state')
        old = self.service
        stopped = await old.stop(min(10, self.config['limits']['cleanup_seconds']))
        require(stopped.get('pid_absent') and stopped['returncode'] is not None, 'service_restart_stop_unconfirmed')
        try:
            await self.start_service()
        except Exception as error:
            code = str(error) if isinstance(error, TrialError) and str(error) in {
                'port_already_occupied', 'owned_process_readiness_timeout',
                'owned_process_exited_after_health'} else 'service_start_failed'
            self.receipt['restart_failure'] = {'phase': 'start_after_stop', 'code': code}
            raise
        after = await driver.snapshot(record['run_id'] + '-restart-after.zip')
        old_state = acceptance.load_snapshot(self.evidence_dir / before['file'], before['sha256'])
        new_state = acceptance.load_snapshot(self.evidence_dir / after['file'], after['sha256'])
        proof = acceptance.restart_state_proof(old_state, new_state, record.get('principal_actor', 'gtd-felix'))
        retained = proof['state_preserved']
        require(retained and proof['budget_preserved'], 'restart_lost_state_or_budget')
        result = {'before_process_id': old.process.pid, 'after_process_id': self.service.process.pid,
            'before_stopped': stopped, 'after_ready': True, 'before': before, 'after': after,
            'state_ids_preserved': retained, 'state_proof': proof, 'service_url': self.config['product_api_url'], 'observed_at': stamp()}
        filename = record['run_id'] + '-restart.json'
        data = acceptance.canonical(result)
        acceptance.write_new(self.evidence_dir / filename, data)
        return {**result, 'file': filename, 'sha256': acceptance.sha(data)}

    async def suspend_owned_bots(self):
        configured = {bot['id'] for bot in self.service_config.get('bots', [])}
        if not configured:
            return True
        token = self.env[self.config['probe']['owner_token_env']]
        base = self.config['product_api_url']
        try:
            bots = await self.http('POST', base + '/v1/control/bots', token, {})
            own = [bot for bot in bots if bot.get('id') in configured]
            require({bot['id'] for bot in own} == configured, 'configured_bot_inventory_incomplete')
            suspended = []
            for bot in own:
                response = await self.http('POST', base + '/v1/control/register_bot', token, {
                    'operation_id': 'trial-suspend:' + self.receipt['trial_id'] + ':' + bot['id'],
                    'bot': {**bot, 'state': 'suspended'}})
                require(response.get('status') == 'applied', 'trial_bot_suspension_rejected')
                suspended.append(bot['id'])
            self.receipt['suspended_bots'] = suspended
            return True
        except Exception:
            self.receipt['admission_close_error'] = 'configured_bot_suspension_unconfirmed'
            return False

    async def stop_jobs(self):
        token = self.env[self.config['probe']['owner_token_env']]
        base = self.config['product_api_url']
        deadline = time.monotonic() + min(self.config['limits']['cleanup_seconds'] * .6, max(.1,self.remaining()))
        requested, known = set(), {}
        while time.monotonic() < deadline:
            try:
                pending = await self.http('POST', base + '/v1/control/pending', token, {})
                live = [j for j in pending if not j.get('terminal')]
                for job in live:
                    known[job['id']] = {'id': job['id'], 'native': job.get('native'), 'terminal': False}
                    if job['id'] not in requested:
                        response = await self.http('POST', base + '/v1/control/request_stop', token,
                            {'operation_id': 'trial-stop:' + job['id'], 'job_id': job['id']})
                        requested.add(job['id'])
                        known[job['id']]['stop_request_status'] = response.get('status')
                for job_id in list(known):
                    job = await self.http('POST', base + '/v1/control/get_job', token, {'job_id': job_id})
                    if job and job.get('terminal'):
                        known[job_id].update(terminal=True, observation=job.get('observations', [])[-1:] )
                if not live:
                    self.receipt['job_stop_observations'] = list(known.values())
                    self.receipt['unresolved_jobs'] = [j for j in known.values() if not j['terminal']]
                    return not self.receipt['unresolved_jobs']
            except Exception:
                self.receipt['job_stop_error'] = 'control_observation_unavailable'
                break
            await asyncio.sleep(.2)
        self.receipt['job_stop_observations'] = list(known.values())
        self.receipt['unresolved_jobs'] = [j for j in known.values() if not j['terminal']]
        if not known:
            self.receipt['unresolved_jobs'].append({'status': 'unknown', 'reason': 'control_inventory_unavailable'})
        return False

    async def run(self, case):
        import aiohttp
        require(case in acceptance.SCENARIOS, 'unknown_case')
        async with aiohttp.ClientSession(trust_env=False, timeout=aiohttp.ClientTimeout(total=self.config['limits']['request_seconds'])) as session:
            self.session = session
            try:
                # All configurations are checked before the first gateway starts.
                await self.verify_python()
                for gateway in self.config['gateways']:
                    env = self.gateway_environment(gateway)
                    constraints = await self.native_configuration(gateway, env)
                    self.receipt['checks']['native:' + gateway['base_url']] = constraints
                for gateway in self.config['gateways']:
                    await self.initialize_board(gateway, self.gateway_environment(gateway))
                for gateway in self.config['gateways']:
                    require(self.remaining() > self.config['limits']['cleanup_seconds'], 'total_work_budget_exhausted')
                    check_free_port(gateway['base_url'])
                    require(not previous_processes([gateway['home'],gateway['kanban_home']]), 'previous_gateway_process_refused')
                    env = self.gateway_environment(gateway)
                    owned = OwnedProcess('gateway', [gateway['cli'],'gateway','run','--external-supervisor','--quiet'], env, gateway['workspace'], log_dir=self.evidence_dir)
                    self.processes.append(owned); self.gateways.append(owned)
                    await owned.start()
                    await self.ready(owned, gateway['base_url'], env['API_SERVER_KEY'], gateway=True)
                require(self.remaining() > self.config['limits']['cleanup_seconds'], 'total_work_budget_exhausted')
                await self.start_service()
                probe = {'synthetic': True, **self.config['probe'], 'product_api_url': self.config['product_api_url'],
                    'timeout_seconds': min(self.config['limits']['case_seconds'], max(.1,self.remaining()-self.config['limits']['cleanup_seconds']-31)),
                    'case_timeout_seconds': self.config['limits']['case_seconds'], 'max_cases': 1,
                    'bot_ids': [bot['id'] for bot in self.service_config.get('bots', [])]}
                # ProductDriver resolves only the explicitly named token. Scope
                # injection is local to this process and reverted after the call.
                token_name = probe['owner_token_env']
                old_token = os.environ.get(token_name)
                os.environ[token_name] = self.env[token_name]
                try:
                    driver = acceptance.ProductDriver(probe, session, self.evidence_dir)
                finally:
                    if old_token is None: os.environ.pop(token_name, None)
                    else: os.environ[token_name] = old_token
                require(not await driver.request('GET','/v1/items'), 'initial_service_inventory_not_empty')
                record = await asyncio.wait_for(driver.run_case(case, restart=self.restart_service if case == 'G8' else None,
                    case_prepare=lambda d,r: d.prepare_case(r), case_ready=lambda d,r: d.enable_case(r)), probe['timeout_seconds'] + driver.closure_seconds + 1)
                self.receipt['case'] = acceptance.evaluate_record(record, self.evidence_dir)
                self.receipt['case_evidence'] = record['run_id'] + '-evidence.json'
                self.receipt['status'] = 'COMPLETE' if self.receipt['case']['status'] == 'PASS' else 'PARTIAL'
            except BaseException as error:
                self.receipt['status'] = 'PARTIAL' if self.processes else 'BLOCKED'
                self.receipt['error'] = str(error) if isinstance(error, TrialError) else type(error).__name__
            finally:
                if self.service and self.service.process.returncode is None:
                    if not await self.suspend_owned_bots():
                        self.receipt['status'] = 'PARTIAL'
                    if not await self.stop_jobs():
                        self.receipt['status'] = 'PARTIAL'
                elif self.service:
                    self.receipt['status'] = 'PARTIAL'
                    self.receipt['unresolved_jobs'] = [{'status': 'unknown', 'reason': 'service_exited_before_job_reconciliation'}]
                for index, owned in enumerate(reversed(self.processes)):
                    try:
                        await owned.stop(max(.2, min(10, self.remaining() / max(1, len(self.processes) - index))))
                    except Exception:
                        self.receipt['status'] = 'PARTIAL'
                        owned.receipt['status'] = 'STOP_UNCONFIRMED'
                self.receipt['processes'] = [p.receipt for p in self.processes]
                self.receipt['finished_at'] = stamp()
                self.receipt['elapsed_seconds'] = time.monotonic() - self.started
                acceptance.write_new(self.evidence_dir / 'trial-receipt.json', acceptance.canonical(self.receipt))
        return self.receipt


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--execute', action='store_true')
    parser.add_argument('--config', required=True)
    parser.add_argument('--evidence-dir', required=True)
    parser.add_argument('--case', choices=acceptance.SCENARIOS, required=True)
    args = parser.parse_args(argv)
    if not args.execute:
        print(json.dumps({'status': 'NOT_RUN', 'error': 'execute_flag_required'}))
        return 1
    try:
        config, service, env = load_config(args.config)
        path = absolute_path(args.evidence_dir)
        path.mkdir(mode=0o700, parents=False, exist_ok=False)
        receipt = asyncio.run(Supervisor(config, service, env, path).run(args.case))
        print(json.dumps({'status': receipt['status'], 'receipt': str(path / 'trial-receipt.json'),
            'unresolved_jobs': receipt.get('unresolved_jobs', [])}))
        return 0 if receipt['status'] == 'COMPLETE' else 1
    except Exception as error:
        print(json.dumps({'status': 'BLOCKED', 'error': str(error) if isinstance(error,TrialError) else type(error).__name__}))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
