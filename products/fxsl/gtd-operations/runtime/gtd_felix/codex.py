"""Local Codex app-server adapter. Native completion is not domain integration.

Only exact owned thread IDs are read. JSON-RPC IDs are correlation IDs, never
idempotency keys. Lost creation acknowledgements are retained as uncertainty.
"""
import asyncio
import copy
import hashlib
import json
import math
import os
from pathlib import Path
import signal
import time
import uuid


def encoded(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False)


def digest(value):
    return hashlib.sha256(encoded(value).encode()).hexdigest()


def require(value, code):
    if not value:
        raise ValueError(code)


def birth(pid):
    path = Path('/proc') / str(pid)
    require(path.stat().st_uid == os.getuid(), 'process_uid_mismatch')
    return (path / 'stat').read_text().rsplit(')', 1)[1].split()[19]


# Fixed public 0.154.0 switches; callers cannot inject arbitrary CLI config.
OVERLAY_DISABLED_FEATURES = ('hooks', 'plugins', 'remote_plugin', 'apps', 'enable_mcp_apps',
    'multi_agent', 'multi_agent_v2', 'memories', 'external_agent_memory_import', 'tool_suggest',
    'recommended_plugins', 'browser_use', 'browser_use_external', 'browser_use_full_cdp_access',
    'computer_use', 'in_app_browser', 'in_app_local_automation', 'skill_search', 'skill_mcp_dependency_install')


def process_overlay(route):
    overlay = route.get('process_overlay')
    if overlay is None: return {}
    require(isinstance(overlay, dict) and set(overlay) == {'version', 'disabled_mcp_servers'}
            and type(overlay['version']) is int and overlay['version'] == 1, 'invalid_process_overlay')
    names = overlay['disabled_mcp_servers']
    require(isinstance(names, list) and len(names) <= 100
            and all(isinstance(name, str) and name and len(name) <= 128
                    and all(c.isascii() and (c.isalnum() or c in '-_.@') for c in name) for name in names) and len(set(names)) == len(names),
            'invalid_disabled_mcp_servers')
    for key in ('model', 'provider', 'effort'):
        value = route[key]
        require(isinstance(value, str) and value and len(value) <= 128
                and all(c.isascii() and (c.isalnum() or c in '-_./') for c in value), 'overlay_public_identifier_required')
    return {'model': route['model'], 'model_provider': route['provider'], 'model_reasoning_effort': route['effort'],
        'instructions': '', 'developer_instructions': '', 'approval_policy': 'never', 'sandbox_mode': 'workspace-write',
        'web_search': 'disabled', 'sandbox_workspace_write': {'writable_roots': [route['workspace']],
            'network_access': False, 'exclude_tmpdir_env_var': True, 'exclude_slash_tmp': True},
        'features': {**{key: False for key in OVERLAY_DISABLED_FEATURES}, 'skip_host_skill_discovery': True},
        'skills': {'include_instructions': False}, 'agents': {'enabled': False},
        'projects': {route['workspace']: {'trust_level': 'trusted'}},
        'mcp_servers': {name: {'enabled': False} for name in names}}


def overlay_arguments(values):
    def toml(value):
        if isinstance(value, dict): return '{' + ','.join(json.dumps(k) + '=' + toml(v) for k, v in sorted(value.items())) + '}'
        if isinstance(value, list): return '[' + ','.join(toml(v) for v in value) + ']'
        return json.dumps(value)
    return [argument for key, value in sorted(values.items()) for argument in ('-c', key + '=' + toml(value))]


def verify_mcp_inventory(response, route=None):
    overlay = process_overlay(route) if route else {}
    require(isinstance(response, dict) and isinstance(response.get('data'), list)
            and not response.get('nextCursor'), 'native_mcp_inventory_not_empty')
    allowed = set(overlay.get('mcp_servers', {}))
    seen = set()
    for server in response['data']:
        require(isinstance(server, dict) and server.get('name') in allowed and server['name'] not in seen,
                'native_mcp_inventory_not_empty')
        seen.add(server['name'])
        require(server.get('runtimeStatus') in (None, 'disabled') and server.get('tools') == {}
                and server.get('resources') == [] and server.get('resourceTemplates') == []
                and server.get('pluginId') is None and server.get('serverInfo') is None,
                'native_mcp_not_disabled')


class _RPC:
    def __init__(self, adapter, key, process=None, channel=None):
        self.adapter, self.key, self.process, self.channel = adapter, key, process, channel
        self.waiters = {}
        self.reader = asyncio.create_task(self.read())

    async def send(self, message):
        if self.channel is not None: return await self.channel.send(message)
        self.process.stdin.write((encoded(message) + '\n').encode())
        await self.process.stdin.drain()

    async def request(self, method, params):
        identity = uuid.uuid4().hex
        future = asyncio.get_running_loop().create_future()
        self.waiters[identity] = future
        self.adapter._event(self.key, {'direction': 'request', 'method': method, 'id': identity})
        try:
            await self.send({'id': identity, 'method': method, 'params': params})
            timeout = self.adapter.timeout
            state = self.adapter._get('job:' + self.key)
            if state and state.get('turn_requested_at'):
                timeout = min(timeout, max(.1, state['limits']['max_runtime_seconds'] - (time.time() - state['turn_requested_at'])))
            return await asyncio.wait_for(future, timeout)
        finally:
            self.waiters.pop(identity, None)

    async def read(self):
        try:
            while True:
                if self.channel is not None:
                    message = await self.channel.receive()
                    if message is None: break
                else:
                    line = await self.process.stdout.readline()
                    if not line: break
                    message = json.loads(line)
                require(isinstance(message, dict), 'invalid_rpc_message')
                if 'id' in message and 'method' not in message:
                    future = self.waiters.get(message['id'])
                    if future and not future.done():
                        self.adapter._event(self.key, {'direction': 'response', 'id': message['id'], 'accepted': 'error' not in message})
                        if 'error' in message:
                            future.set_exception(ValueError('native_rpc_rejected'))
                        else:
                            future.set_result(message.get('result'))
                    else:
                        self.adapter._event(self.key, {'direction': 'orphan_response'})
                elif 'id' in message:
                    # No approvals, dynamic tools, token refresh or user consent are delegated.
                    await self.send({'id': message['id'], 'error': {'code': -32601, 'message': 'Not authorized by GTD adapter'}})
                    self.adapter._event(self.key, {'direction': 'denied_server_request', 'method': message.get('method')})
                else:
                    params = message.get('params', {})
                    if message.get('method') == 'turn/completed' and isinstance(params, dict):
                        self.adapter._notification(self.key, params)
                    # Reasoning, credentials and arbitrary tool output are never persisted here.
        except (OSError, ValueError, TypeError, KeyError):
            self.adapter._event(self.key, {'direction': 'transport_invalid'})
        finally:
            for future in self.waiters.values():
                if not future.done(): future.set_exception(ValueError('transport_lost'))


class CodexAdapter:
    def __init__(self, control, config):
        self.control, self.store = control, control.store
        self.config = copy.deepcopy(config)
        self.timeout = config.get('request_timeout_seconds', 10)
        self.grace = config.get('shutdown_grace_seconds', 2)
        require(type(self.timeout) in (int, float) and 0 < self.timeout <= 60, 'invalid_timeout')
        require(type(self.grace) in (int, float) and 0 < self.grace <= 10, 'invalid_shutdown_grace')
        self.connections, self.locks, self.monitors = {}, {}, {}
        self.terminal_tasks = {}

    def _get(self, key):
        with self.store.lock:
            row = self.store.db.execute('SELECT value FROM metadata WHERE key=?', ('codex:' + key,)).fetchone()
            return json.loads(row[0]) if row else None

    def _put(self, key, value):
        self.store.db.execute('INSERT INTO metadata VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value',
                              ('codex:' + key, encoded(value)))

    def _update(self, key, **fields):
        with self.store.transaction():
            value = self._get(key) or {}
            value.update(fields)
            self._put(key, value)
        return value

    def _event(self, key, event):
        with self.store.transaction():
            self._put('event:' + key + ':' + uuid.uuid4().hex, {'at': time.time(), **event})

    def _lock(self, key):
        return self.locks.setdefault(key, asyncio.Lock())

    def _route(self, bot_id, *, for_model=True):
        route = self.config.get('routes', {}).get(bot_id)
        require(isinstance(route, dict), 'route_not_configured')
        for key in ('host', 'profile', 'workspace', 'model', 'provider', 'effort', 'base_instructions', 'developer_instructions'):
            require(isinstance(route.get(key), str) and route[key], 'route_field_required')
        if route['host'] == 'ssh':
            from .codex_remote import validate_remote_route
            validate_remote_route(route)
            process_overlay(route)
            return route
        require(route['host'] == 'local', 'local_transport_required')
        for filename in (route['workspace'], self.config.get('codex_home')):
            path = Path(filename or '')
            require(path.is_absolute() and path.is_dir() and path.resolve() == path, 'canonical_directory_required')
        binary = Path(self.config.get('binary', ''))
        require(binary.is_absolute() and binary.is_file() and os.access(binary, os.X_OK), 'binary_required')
        require(hashlib.sha256(binary.resolve(strict=True).read_bytes()).hexdigest() == self.config.get('binary_sha256'), 'binary_hash_mismatch')
        require(isinstance(route.get('instruction_sources'), dict), 'instruction_manifest_required')
        for filename, checksum in (route['instruction_sources'].items() if for_model else ()):
            path = Path(filename)
            require(path.is_absolute() and path.resolve() == path and path.is_file()
                    and hashlib.sha256(path.read_bytes()).hexdigest() == checksum, 'instruction_source_changed')
        process_overlay(route)
        return route

    def _binary_hash(self, route):
        return route['remote']['binary_sha256'] if route['host'] == 'ssh' else self.config['binary_sha256']

    def _remote(self, key, route):
        from .codex_remote import RemoteTransport
        return RemoteTransport(self, key, route)

    def _supervisor(self, key, route):
        if route['host'] == 'ssh': return self._remote(key, route)
        from .codex_local import LocalSupervisor
        return LocalSupervisor(self, key, route)

    async def _verify_route(self, key, route, *, for_model):
        if route['host'] == 'ssh': await self._remote(key, route).validate(for_model=for_model)

    def _job(self, job_id, *, for_model=False):
        job = self.control.get_job(job_id)
        require(job, 'job_not_found')
        route = self.config.get('routes', {}).get(job['bot_id'])
        require(isinstance(route, dict), 'route_not_configured')
        require(all(job['route'].get(k) == route[k] for k in ('host', 'profile')), 'route_identity_mismatch')
        state = self._get('job:' + job_id)
        if state:
            same_route = state['route_hash'] == digest(route)
            # A newly added disabling overlay may recover a legacy reservation, but may not feed it new input.
            legacy_read = (not for_model and not state.get('overlay') and state.get('overlay_hash') in (None, digest({})) and 'process_overlay' in route
                           and state['route_hash'] == digest({k: v for k, v in route.items() if k != 'process_overlay'}))
            require((same_route or legacy_read) and state['binary_sha256'] == self._binary_hash(route), 'route_changed')
        return job, route

    def _valid(self, job):
        result = self.control.validate(job['id'], job['capability'])
        require(result.get('allowed'), 'execution_not_authorized')
        require(result['limits']['max_descendants'] == 0 and result['limits']['max_retries'] == 0,
                'single_turn_reservation_required')
        state = self._get('job:' + job['id']) or {}
        remote = self._get('remote:' + job['id']) or self._get('local:' + job['id'])
        if remote: require(time.time() < remote['deadline'] - self.grace, 'remote_budget_expired')
        if 'turn_requested_at' in state:
            require(time.time() < state['turn_requested_at'] + state['limits']['max_runtime_seconds'],
                    'runtime_budget_expired')
        return result['limits']

    def _sandbox(self, route):
        return {'type': 'workspaceWrite', 'writableRoots': [route['workspace']], 'networkAccess': False,
                'excludeTmpdirEnvVar': True, 'excludeSlashTmp': True}

    def _thread_params(self, route):
        return {'cwd': route['workspace'], 'model': route['model'], 'modelProvider': route['provider'],
                'baseInstructions': route['base_instructions'], 'developerInstructions': route['developer_instructions'],
                'approvalPolicy': 'never', 'sandbox': 'workspace-write',
                'config': {'model_reasoning_effort': route['effort'], 'sandbox_workspace_write': {
                    'writable_roots': [route['workspace']], 'network_access': False,
                    'exclude_tmpdir_env_var': True, 'exclude_slash_tmp': True}}}

    def _effective_config(self, route, response):
        config = response.get('config', {}) if isinstance(response, dict) else {}
        expected = {'model': route['model'], 'model_provider': route['provider'], 'model_reasoning_effort': route['effort'],
            'instructions': route['base_instructions'], 'developer_instructions': route['developer_instructions'],
            'approval_policy': 'never', 'sandbox_mode': 'workspace-write', 'web_search': 'disabled',
            'sandbox_workspace_write': {'writable_roots': [route['workspace']], 'network_access': False,
                'exclude_tmpdir_env_var': True, 'exclude_slash_tmp': True}}
        overlay = process_overlay(route)
        if overlay:
            expected.update(instructions='', developer_instructions='')
            require(all(config.get('features', {}).get(key) is value for key, value in overlay['features'].items()), 'overlay_features_mismatch')
            servers = config.get('mcp_servers', {})
            require(isinstance(servers, dict) and set(servers) == set(overlay['mcp_servers'])
                    and all(isinstance(server, dict) and server.get('enabled') is False for server in servers.values()),
                    'overlay_mcp_not_disabled')
            require(config.get('skills', {}).get('include_instructions') is False
                    and config.get('agents', {}).get('enabled') is False, 'overlay_context_mismatch')
            require(config.get('projects', {}).get(route['workspace'], {}).get('trust_level') == 'trusted',
                    'overlay_project_trust_missing')
            require(not config.get('model_instructions_file') and not config.get('experimental_compact_prompt_file'),
                    'inherited_instruction_file_not_allowed')
        require(all(config.get(k) == v for k, v in expected.items()), 'effective_config_mismatch')
        require(bool(overlay) or (not config.get('mcp_servers') and not config.get('hooks') and not config.get('plugins')
                and not config.get('apps') and not config.get('browser_use') and not config.get('computer_use')),
                'external_capabilities_not_allowed')
        require(config.get('features', {}).get('multi_agent') is False, 'native_delegation_not_disabled')
        return digest({'expected': expected, 'overlay': overlay})

    def _thread_verified(self, route, response, expected_id=None):
        require(isinstance(response, dict) and isinstance(response.get('thread'), dict), 'invalid_thread_response')
        thread = response['thread']
        require(isinstance(thread.get('id'), str) and thread['id'], 'thread_identity_missing')
        require(expected_id is None or thread['id'] == expected_id, 'thread_identity_mismatch')
        sandbox = response.get('sandbox')
        # rust-v0.154.0 protocol.rs: WorkspaceWrite roots are additional to cwd.
        if isinstance(sandbox, dict) and sandbox.get('writableRoots') == []:
            sandbox = {**sandbox, 'writableRoots': [route['workspace']]}
        require(response.get('model') == route['model'] and response.get('modelProvider') == route['provider']
                and response.get('cwd') == route['workspace'] and response.get('approvalPolicy') == 'never'
                and sandbox == self._sandbox(route)
                and response.get('reasoningEffort') == route['effort'], 'effective_thread_mismatch')
        require(set(response.get('instructionSources', [])) == set(route['instruction_sources']), 'instruction_inventory_mismatch')
        return thread

    async def _tools_verified(self, rpc, thread_id=None, route=None):
        params = {'limit': 100}
        if thread_id: params['threadId'] = thread_id
        response = await rpc.request('mcpServerStatus/list', params)
        verify_mcp_inventory(response, route)

    async def _spawn(self, key, route):
        state = self._get('job:' + key)
        if route['host'] == 'local' and (state is None or state.get('local_supervised')):
            from .codex_local import LocalSupervisor
            existing = self._get('local:' + key)
            if existing:
                await LocalSupervisor(self,key,route).stop()
                # A fresh bounded transport may only read the known thread.
                require(state and state.get('thread_id'), 'local_readback_thread_unknown')
                supervisor=LocalSupervisor(self,key+':read:'+uuid.uuid4().hex,route,read_only=True)
            else:
                supervisor=LocalSupervisor(self,key,route)
            channel=await supervisor.start()
            rpc=self.connections[key]=_RPC(self,key,channel=channel)
            await rpc.request('initialize', {'clientInfo':{'name':'gtd-private-adapter','version':'1'}})
            await rpc.send({'method':'initialized','params':{}})
            return rpc
        if route['host'] == 'ssh':
            channel = await self._remote(key, route).connect()
            rpc = self.connections[key] = _RPC(self, key, channel=channel)
            await rpc.request('initialize', {'clientInfo': {'name':'gtd-private-adapter','version':'1'}})
            await rpc.send({'method':'initialized','params':{}})
            return rpc
        with self.store.transaction():
            old = self._get('process:' + key)
            if old and old.get('status') == 'spawning':
                raise ValueError('transport_creation_unresolved')
            if old and old.get('pid'):
                try:
                    require(birth(old['pid']) != old.get('birth'), 'owned_process_still_alive')
                except OSError: pass
            self._put('process:' + key, {'status': 'spawning', 'requested_at': time.time()})
        env = {k: os.environ[k] for k in ('HOME', 'PATH', 'LANG', 'LC_ALL', 'TZ') if k in os.environ}
        env['CODEX_HOME'] = self.config['codex_home']
        process = await asyncio.create_subprocess_exec(str(Path(self.config['binary']).resolve(strict=True)), 'app-server', '--strict-config', '--stdio', *overlay_arguments(process_overlay(route)),
            cwd=route['workspace'], env=env, stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.DEVNULL, start_new_session=True, limit=8*1024*1024)
        self._update('process:' + key, status='running', pid=process.pid, birth=birth(process.pid), pgid=os.getpgid(process.pid))
        self._event(key, {'direction': 'process_started', 'pid': process.pid, 'birth': birth(process.pid), 'pgid': os.getpgid(process.pid)})
        rpc = self.connections[key] = _RPC(self, key, process)
        await rpc.request('initialize', {'clientInfo': {'name': 'gtd-private-adapter', 'version': '1'}})
        await rpc.send({'method': 'initialized', 'params': {}})
        return rpc

    async def _close_process(self, key):
        rpc = self.connections.get(key)
        if not rpc: return
        if rpc.channel is not None:
            await rpc.channel.close()
            self.connections.pop(key, None)
            rpc.reader.cancel()
            await asyncio.gather(rpc.reader, return_exceptions=True)
            if hasattr(rpc.channel, 'websocket'): self._update('ssh:' + key, status='channel_closed')
            return
        self.connections.pop(key, None)
        process = rpc.process
        record = self._get('process:' + key)
        if process.returncode is None:
            try:
                require(record['pid'] == process.pid and birth(process.pid) == record['birth']
                        and os.getpgid(process.pid) == record['pgid'] == process.pid, 'process_identity_changed')
                os.killpg(process.pid, signal.SIGTERM)
                try: await asyncio.wait_for(process.wait(), self.grace)
                except asyncio.TimeoutError:
                    require(birth(process.pid) == record['birth'] and os.getpgid(process.pid) == record['pgid'],
                            'process_identity_changed')
                    os.killpg(process.pid, signal.SIGKILL)
                    await process.wait()
            except ProcessLookupError:
                await process.wait()
        try:
            await asyncio.wait_for(rpc.reader, self.grace)
        except asyncio.TimeoutError:
            self._event(key, {'direction': 'transport_reader_cancelled'})
        self._update('process:' + key, status='exited', returncode=process.returncode)

    async def discover(self, bot_id):
        key = 'discovery:' + uuid.uuid4().hex
        try:
            route = self._route(bot_id)
            await self._verify_route(key, route, for_model=True)
            rpc = await self._spawn(key, route)
            config_hash = self._effective_config(route, await rpc.request('config/read', {'cwd': route['workspace'], 'includeLayers': False}))
            await self._tools_verified(rpc, route=route)
            return {'status': 'ready', 'transport': 'codex-app-server', 'effective_config_hash': config_hash,
                    'binary_sha256': self._binary_hash(route), 'inference': False,
                    'capabilities': {'host_read_isolated': False, 'write_scope': route['workspace'],
                                     'network_access': False, 'native_mcp_servers': [],
                                     'disabled_mcp_servers': sorted(process_overlay(route).get('mcp_servers', {}))}}
        except (OSError, ValueError, asyncio.TimeoutError) as error:
            return {'status': 'unavailable', 'reason': str(error) if isinstance(error, ValueError) else 'codex_discovery_failed'}
        finally:
            await self._close_process(key)
            if self._get('remote:' + key) or self._get('local:' + key):
                try: await self._supervisor(key, route).stop()
                except (OSError, ValueError, asyncio.TimeoutError): pass

    def _uncertain(self, job_id, reason):
        if self._get('job:' + job_id):
            self._update('job:' + job_id, delivery='uncertain', error=reason)
        return {'status': 'uncertain', 'job_id': job_id, 'error': reason, 'terminal': False}

    def _native(self, job, state):
        return {'provider': 'codex-app-server', 'host': job['route']['host'], 'profile': job['route']['profile'],
                'id': state['thread_id'], 'thread_id': state['thread_id']}

    async def submit(self, job_id, prompt, durable=False):
        async with self._lock(job_id):
            try:
                job, route = self._job(job_id, for_model=True)
                require(isinstance(prompt, str) and 0 < len(prompt.encode()) <= 1024*1024, 'prompt_required')
                existing = self._get('job:' + job_id)
                if existing:
                    require(existing['prompt_hash'] == digest(prompt), 'submission_changed')
                    return self._result(job_id)
                self._route(job['bot_id'])
                limits = self._valid(job)
                with self.store.transaction():
                    require(self._get('job:' + job_id) is None, 'submission_already_owned')
                    self._put('job:' + job_id, {'route_hash': digest(route), 'binary_sha256': self._binary_hash(route),
                        'overlay': process_overlay(route), 'overlay_hash': digest(process_overlay(route)), 'prompt_hash': digest(prompt), 'delivery': 'intent', 'created_at': time.time(), 'limits': limits,
                        'client_message_id': uuid.uuid4().hex, 'local_supervised':route['host']=='local'})
                await self._verify_route(job_id, route, for_model=True)
                rpc = await self._spawn(job_id, route)
                config_hash = self._effective_config(route, await rpc.request('config/read', {'cwd': route['workspace'], 'includeLayers': False}))
                self._update('job:' + job_id, effective_config_hash=config_hash)
                self._valid(self.control.get_job(job_id))
                self._update('job:' + job_id, delivery='thread_requested')
                response = await rpc.request('thread/start', self._thread_params(route))
                # Capture exact native ID before any subsequent validation can fail.
                if isinstance(response, dict) and isinstance(response.get('thread', {}).get('id'), str):
                    self._update('job:' + job_id, thread_id=response['thread']['id'])
                thread = self._thread_verified(route, response)
                require(not thread.get('turns'), 'new_thread_has_history')
                state = self._get('job:' + job_id)
                require(self.control.record_dispatch(job_id, self._native(job, state))['status'] == 'recorded', 'dispatch_record_rejected')
                await self._tools_verified(rpc, thread['id'], route=route)
                self._valid(self.control.get_job(job_id))
                self._route(job['bot_id'])  # Recheck instruction hashes immediately before model work.
                await self._verify_route(job_id, route, for_model=True)
                self._valid(self.control.get_job(job_id))
                self._update('job:' + job_id, delivery='turn_requested', turn_requested_at=time.time())
                self.monitors[job_id] = asyncio.create_task(self._monitor(job_id))
                response = await rpc.request('turn/start', {'threadId': thread['id'], 'input': [{'type': 'text', 'text': prompt}],
                    'clientUserMessageId': state['client_message_id'], 'model': route['model'], 'effort': route['effort'],
                    'cwd': route['workspace'], 'approvalPolicy': 'never', 'sandboxPolicy': self._sandbox(route)})
                require(isinstance(response, dict), 'invalid_turn_response')
                turn = response.get('turn', {})
                require(isinstance(turn, dict), 'invalid_turn_response')
                require(isinstance(turn.get('id'), str) and turn['id'], 'turn_identity_missing')
                self._update('job:' + job_id, turn_id=turn['id'], delivery='submitted')
                self._apply_turn(job_id, turn)
                await self._await_remote_terminal(job_id)
                return self._result(job_id)
            except (OSError, ValueError, asyncio.TimeoutError):
                if self._get('job:' + job_id):
                    state = self._get('job:' + job_id)
                    if not state.get('turn_requested_at'): await self._close_process(job_id)
                    return self._uncertain(job_id, 'submission_unconfirmed')
                return {'status': 'rejected', 'job_id': job_id, 'error': 'admission_rejected', 'no_effect': True}

    def _notification(self, key, params):
        state = self._get('job:' + key)
        if not state: return
        if params.get('threadId') != state.get('thread_id'):
            self._event(key, {'direction': 'foreign_notification_rejected'})
            return
        turn = params.get('turn', {})
        if not isinstance(turn, dict):
            self._event(key, {'direction': 'invalid_turn_notification'})
            return
        if state.get('turn_id') != turn.get('id'):
            # It may precede turn/start acknowledgement. Only read-back can recover it.
            self._event(key, {'direction': 'unbound_turn_notification'})
            return
        if turn.get('itemsView', 'full') != 'full':
            self._event(key, {'direction': 'terminal_items_readback_required', 'turn_id': turn.get('id')})
            return
        self._apply_turn(key, turn)

    def _execution_projection(self, route, items):
        require(isinstance(items, list) and len(items) <= 1000, 'turn_items_limit')
        root = Path(route['workspace'])
        def scoped_path(value):
            require(isinstance(value, str) and value and len(value) <= 4096, 'invalid_execution_path')
            path = Path(value)
            require('..' not in path.parts, 'execution_path_outside_workspace')
            path = path if path.is_absolute() else root / path
            require((path.is_relative_to(root) if route['host'] == 'ssh' else path.resolve().is_relative_to(root)), 'execution_path_outside_workspace')
            return str(path)
        def content_hash(value):
            if value is None: return None
            require(isinstance(value, str), 'invalid_execution_content')
            raw = value.encode()
            require(len(raw) <= 1024 * 1024, 'execution_content_limit')
            return {'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}
        result, seen = [], set()
        for item in items:
            require(isinstance(item, dict), 'invalid_turn_item')
            if item.get('type') not in {'commandExecution', 'fileChange'}: continue
            identity = item.get('id')
            require(isinstance(identity, str) and identity and len(identity) <= 256 and identity not in seen,
                    'execution_item_identity_invalid')
            seen.add(identity)
            require(item.get('status') in {'inProgress', 'completed', 'failed', 'declined'}, 'execution_status_invalid')
            entry = {k: item[k] for k in ('id', 'type', 'status')}
            if item['type'] == 'commandExecution':
                command = item.get('command')
                require(isinstance(command, str) and len(command.encode()) <= 4096, 'execution_command_limit')
                code = item.get('exitCode')
                require(code is None or type(code) is int, 'execution_exit_code_invalid')
                entry.update(command=command, cwd=scoped_path(item.get('cwd')), exitCode=code,
                             output=content_hash(item.get('aggregatedOutput')))
            else:
                changes = item.get('changes')
                require(isinstance(changes, list) and len(changes) <= 100, 'execution_changes_limit')
                entry['changes'] = []
                for change in changes:
                    require(isinstance(change, dict) and isinstance(change.get('kind'), dict), 'invalid_file_change')
                    kind = change['kind']
                    require(kind.get('type') in {'add', 'delete', 'update'}, 'invalid_file_change_kind')
                    projected = {'path': scoped_path(change.get('path')), 'kind': kind['type'],
                                 'diff': content_hash(change.get('diff'))}
                    require(projected['diff'] is not None, 'file_change_diff_missing')
                    if kind.get('move_path') is not None: projected['move_path'] = scoped_path(kind['move_path'])
                    entry['changes'].append(projected)
            result.append(entry)
        return result

    def _apply_turn(self, job_id, turn):
        state = self._get('job:' + job_id)
        if state.get('pending_observation'):
            self._start_remote_finalization(job_id)
            return
        require(isinstance(turn, dict), 'invalid_turn')
        require(turn.get('id') == state.get('turn_id'), 'turn_identity_mismatch')
        status = {'completed': 'completed', 'failed': 'failed', 'interrupted': 'cancelled', 'inProgress': 'running'}.get(turn.get('status'))
        require(status, 'unknown_turn_status')
        job = self.control.get_job(job_id)
        if job['terminal']: return
        terminal = status != 'running'
        require(not terminal or turn.get('itemsView', 'full') == 'full', 'full_turn_readback_required')
        output = [{'id': item['id'], 'text': item['text']} for item in turn.get('items', [])
                  if item.get('type') == 'agentMessage' and item.get('phase') in (None, 'final_answer')
                  and isinstance(item.get('id'), str) and isinstance(item.get('text'), str)]
        evidence = {'thread_id': state['thread_id'], 'turn_id': turn['id'], 'status': status,
                    'started_at': turn.get('startedAt'), 'completed_at': turn.get('completedAt'), 'duration_ms': turn.get('durationMs')}
        reference = 'turn:' + job_id + ':' + digest(evidence)
        duration = turn.get('durationMs')
        runtime = duration / 1000 if type(duration) in (int, float) and math.isfinite(duration) and duration >= 0 else (
            state['limits']['max_runtime_seconds'] if terminal else max(0, time.time() - state['turn_requested_at']))
        with self.store.transaction(): self._put(reference, evidence)
        observation = {'native_identity': self._native(job, state), 'native_status': status, 'terminal': terminal,
            'runtime_seconds': max(runtime, job['observed_runtime_seconds']), 'cost_usd': None,
            'evidence_reference': 'codex:' + reference}
        artifact = None
        if terminal:
            _, route = self._job(job_id)
            execution = self._execution_projection(route, turn.get('items', []))
        if terminal and (output or execution):
            raw = encoded({'thread_id': state['thread_id'], 'turn_id': turn['id'], 'messages': output,
                'execution': execution, 'assessment': 'pending_principal', 'workspace_integration': 'not_verified',
                'capabilities': {'host_read_isolated': False, 'write_scope': route['workspace']}}).encode()
            require(len(raw) <= 1024*1024, 'result_too_large')
            with self.store.transaction():
                blob = self.store.save_original(raw)
                self.store.db.execute('INSERT OR IGNORE INTO originals VALUES(?,?,?)', (blob['sha256'], blob['size'], blob['path']))
                artifact = {**blob, 'mime_type': 'application/json', 'thread_id': state['thread_id'], 'turn_id': turn['id']}
        result = {'status': 'observed', 'job_id': job_id, 'terminal': terminal,
            'native_status': status, 'thread_id': state['thread_id'], 'turn_id': turn['id'], 'artifact': artifact,
            'integration': 'not_performed', 'cost_telemetry': 'unknown'}
        self._update('job:' + job_id, prepared_result=result)
        if terminal and (self._get('remote:' + job_id) or self._get('local:' + job_id)):
            self._update('job:' + job_id, pending_observation=observation)
            self._start_remote_finalization(job_id)
            return
        require(self.control.observe(job_id, observation)['status'] == 'recorded', 'observation_rejected')
        self._update('job:' + job_id, result=result, delivery='observed')

    def _start_remote_finalization(self, job_id):
        task = self.terminal_tasks.get(job_id)
        if task is None or task.done():
            self.terminal_tasks[job_id] = asyncio.create_task(self._finish_remote_terminal(job_id))

    async def _finish_remote_terminal(self, job_id):
        try:
            _, route = self._job(job_id)
            await self._supervisor(job_id, route).stop()
            state = self._get('job:' + job_id)
            require(state.get('pending_observation'), 'native_terminal_observation_missing')
            require(self.control.observe(job_id, state['pending_observation'])['status'] == 'recorded', 'observation_rejected')
            self._update('job:' + job_id, result=state['prepared_result'], delivery='observed', pending_observation=None)
            await self._close_process(job_id)
        except (OSError, ValueError, asyncio.TimeoutError):
            self._uncertain(job_id, 'remote_terminal_closure_unconfirmed')

    async def _await_remote_terminal(self, job_id):
        if (self._get('job:' + job_id) or {}).get('pending_observation'):
            self._start_remote_finalization(job_id)
            await self.terminal_tasks[job_id]

    def _result(self, job_id):
        state = self._get('job:' + job_id) or {}
        if state.get('pending_observation') and not self.control.get_job(job_id)['terminal']:
            return {'status':'uncertain','job_id':job_id,'terminal':False,'error':'remote_terminal_closure_pending'}
        if self.control.get_job(job_id)['terminal'] and state.get('prepared_result'):
            return state['prepared_result']
        return state.get('result') or {'status': state.get('delivery', 'uncertain'), 'job_id': job_id,
            'thread_id': state.get('thread_id'), 'turn_id': state.get('turn_id'), 'terminal': False}

    async def _monitor(self, job_id):
        try:
            while not self.control.get_job(job_id)['terminal']:
                await asyncio.sleep(.1)
                state = self._get('job:' + job_id)
                job = self.control.get_job(job_id)
                invalid = not self.control.validate(job_id, job['capability']).get('allowed')
                remote = self._get('remote:' + job_id) or self._get('local:' + job_id)
                expired = (time.time() - state['turn_requested_at'] >= state['limits']['max_runtime_seconds']
                    or bool(remote and time.time() >= remote['deadline'] - self.grace))
                if invalid or expired:
                    await self.stop(job_id)
                    if remote and job_id in self.connections:
                        # Preserve exact native terminal evidence before containment closes stdio.
                        await self.poll(job_id)
                    await asyncio.sleep(self.grace)
                    if remote:
                        try: await self._supervisor(job_id, self._job(job_id)[1]).stop()
                        except (OSError, ValueError, asyncio.TimeoutError): pass
                    await self._close_process(job_id)
                    break
            if self.control.get_job(job_id)['terminal']:
                if self._get('remote:' + job_id) or self._get('local:' + job_id):
                    try: await self._supervisor(job_id, self._job(job_id)[1]).stop()
                    except (OSError, ValueError, asyncio.TimeoutError): pass
                await self._close_process(job_id)
        except (OSError, ValueError, asyncio.CancelledError):
            pass

    async def poll(self, job_id):
        async with self._lock(job_id):
            try:
                job, route = self._job(job_id)
                if job['terminal']: return self._result(job_id)
                state = self._get('job:' + job_id)
                require(state and state.get('thread_id'), 'native_thread_unknown')
                rpc = self.connections.get(job_id)
                if not rpc: return self._uncertain(job_id, 'transport_detached')
                response = await rpc.request('thread/read', {'threadId': state['thread_id'], 'includeTurns': False})
                thread = response.get('thread', {})
                require(thread.get('id') == state['thread_id'], 'thread_identity_mismatch')
                page = await rpc.request('thread/turns/list', {'threadId': state['thread_id'], 'itemsView': 'full', 'limit': 2})
                require(isinstance(page, dict) and not page.get('nextCursor'), 'thread_turns_incomplete')
                turns = page.get('data')
                require(isinstance(turns, list) and len(turns) <= 1, 'unexpected_thread_turns')
                if not state.get('turn_id'):
                    require(len(turns) == 1, 'turn_identity_unresolved')
                    user = [i for i in turns[0].get('items', []) if i.get('type') == 'userMessage']
                    require(len(user) == 1 and user[0].get('clientId') == state['client_message_id'], 'turn_identity_unresolved')
                    content = user[0].get('content', [])
                    require(len(content) == 1 and content[0].get('type') == 'text'
                            and digest(content[0].get('text')) == state['prompt_hash'], 'turn_input_mismatch')
                    self._update('job:' + job_id, turn_id=turns[0]['id'])
                expected = self._get('job:' + job_id)['turn_id']
                require(len(turns) == 1 and turns[0].get('id') == expected, 'turn_identity_mismatch')
                self._apply_turn(job_id, turns[0])
                await self._await_remote_terminal(job_id)
                return self._result(job_id)
            except (OSError, ValueError, asyncio.TimeoutError):
                return self._uncertain(job_id, 'readback_unconfirmed')

    async def reconcile(self, job_id):
        job, route = self._job(job_id)
        state = self._get('job:' + job_id)
        if job['terminal']: return self._result(job_id)
        if state and state.get('pending_observation'):
            await self._await_remote_terminal(job_id)
            return self._result(job_id)
        if not state or not state.get('thread_id'): return self._uncertain(job_id, 'native_thread_unknown')
        rpc = self.connections.get(job_id)
        if rpc and ((rpc.process is not None and rpc.process.returncode is not None) or rpc.reader.done()):
            await self._close_process(job_id)
        if job_id not in self.connections:
            process = self._get('process:' + job_id) or {}
            try:
                if birth(process['pid']) == process['birth']: return self._uncertain(job_id, 'owned_process_still_alive')
            except (OSError, KeyError): pass
            try:
                # Readback neither resumes model input nor re-applies stale instructions.
                # Transport identity remains exact; submit/steer retain admission checks.
                self._route(job['bot_id'], for_model=False)
                await self._spawn(job_id, route)
            except (OSError, ValueError, asyncio.TimeoutError):
                await self._close_process(job_id)
                return self._uncertain(job_id, 'read_transport_unconfirmed')
        result = await self.poll(job_id)
        monitor = self.monitors.get(job_id)
        if not self.control.get_job(job_id)['terminal'] and 'turn_requested_at' in state and (monitor is None or monitor.done()):
            self.monitors[job_id] = asyncio.create_task(self._monitor(job_id))
        return result

    async def steer(self, job_id, text, operation_id):
        async with self._lock(job_id):
            try:
                job, route = self._job(job_id, for_model=True)
                self._route(job['bot_id'])
                self._valid(job)
                await self._verify_route(job_id, route, for_model=True)
                self._valid(self.control.get_job(job_id))
                state = self._get('job:' + job_id)
                require(state and state.get('turn_id') and job_id in self.connections, 'native_turn_unknown')
                require(isinstance(text, str) and text and isinstance(operation_id, str) and operation_id, 'steer_input_required')
                key = 'steer:' + job_id + ':' + digest(operation_id)
                with self.store.transaction():
                    if self._get(key): return {'status': 'uncertain', 'error': 'steer_already_requested', 'terminal': False}
                    self._put(key, {'state': 'requested', 'text_hash': digest(text)})
                result = await self.connections[job_id].request('turn/steer', {'threadId': state['thread_id'],
                    'expectedTurnId': state['turn_id'], 'input': [{'type': 'text', 'text': text}]})
                require(isinstance(result, dict) and result.get('turnId') == state['turn_id'], 'steer_turn_mismatch')
                self._update(key, state='acknowledged')
                return {'status': 'steer_acknowledged', 'terminal': False}
            except (OSError, ValueError, asyncio.TimeoutError):
                return self._uncertain(job_id, 'steer_unconfirmed')

    async def _stop_detached_transport(self, job_id):
        _, route = self._job(job_id)
        if route['host'] == 'ssh' or self._get('local:' + job_id):
            await self._supervisor(job_id, route).stop()
            return self._uncertain(job_id, 'remote_containment_native_unreconciled')
        record = self._get('process:' + job_id) or {}
        require(record.get('pid') and record.get('birth'), 'owned_process_identity_missing')
        pid = record['pid']
        try:
            require(birth(pid) == record['birth'] and os.getpgid(pid) == record.get('pgid') == pid,
                    'process_identity_changed')
            self._event(job_id, {'direction': 'detached_transport_stop_requested', 'pid': pid, 'birth': record['birth']})
            os.killpg(pid, signal.SIGTERM)
            deadline = time.monotonic() + self.grace
            while time.monotonic() < deadline:
                try:
                    if birth(pid) != record['birth']: break
                except OSError: break
                await asyncio.sleep(.01)
            else:
                require(birth(pid) == record['birth'] and os.getpgid(pid) == pid, 'process_identity_changed')
                os.killpg(pid, signal.SIGKILL)
            self._update('process:' + job_id, status='transport_stop_requested')
        except ProcessLookupError:
            pass
        return self._uncertain(job_id, 'transport_stop_requested_native_unreconciled')

    async def stop(self, job_id):
        async with self._lock(job_id):
            try:
                job, _ = self._job(job_id)
                if job['terminal']: return self._result(job_id)
                stop_receipt = self.control.request_stop(job.get('requested_by') or self.control.service.principal_actor,
                                          'codex-stop:' + job_id, job_id)
                require(stop_receipt.get('status') != 'rejected', 'stop_not_authorized')
                state = self._get('job:' + job_id)
                if job_id not in self.connections:
                    return await self._stop_detached_transport(job_id)
                require(state and state.get('turn_id'), 'native_turn_unknown')
                key = 'stop:' + job_id
                with self.store.transaction():
                    if self._get(key): return {'status': 'stop_requested', 'terminal': False}
                    self._put(key, {'state': 'requested', 'thread_id': state['thread_id'], 'turn_id': state['turn_id']})
                await self.connections[job_id].request('turn/interrupt', {'threadId': state['thread_id'], 'turnId': state['turn_id']})
                self._update(key, state='acknowledged')
                return {'status': 'stop_requested', 'terminal': False}
            except (OSError, ValueError, asyncio.TimeoutError):
                return self._uncertain(job_id, 'stop_unconfirmed')

    async def close(self):
        for task in self.terminal_tasks.values(): task.cancel()
        await asyncio.gather(*self.terminal_tasks.values(), return_exceptions=True)
        for task in self.monitors.values(): task.cancel()
        await asyncio.gather(*self.monitors.values(), return_exceptions=True)
        for key in list(self.connections): await self._close_process(key)
