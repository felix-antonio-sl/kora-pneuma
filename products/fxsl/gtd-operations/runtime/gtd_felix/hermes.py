"""Trusted public Hermes API/CLI adapter; no native DB or inference scheduler.

Routes and model settings are private operator configuration. USD reservations
are accounting ceilings, not claims of native billing cutoffs. Native turn/time
limits are checked through public config reads before dispatch. The API budget
is cooperative; Kanban runtime termination additionally has dispatcher latency.
"""
import asyncio
import copy
import hashlib
import json
import math
import os
import re
from pathlib import Path
import socket
import shlex
import sys
import time
from urllib.parse import quote, urlsplit

import aiohttp


def _json(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False)


def _hash(value):
    return hashlib.sha256(_json(value).encode()).hexdigest()


def _number(value):
    return isinstance(value, (float, int)) and not isinstance(value, bool) and math.isfinite(value) and value >= 0


class HermesAdapter:
    """runner(argv, *, env, cwd, timeout) is an async trusted CLI transport.

    It returns {returncode:int, stdout:str}. The default uses subprocess exec,
    never a shell. A custom runner is needed for configured remote hosts.
    session is caller-owned; this adapter neither starts gateways nor closes it.
    """
    CONFIG_KEYS = ('agent.max_turns', 'agent.run_budget_seconds', 'agent.api_max_retries',
                   'tools.tool_search.enabled', 'agent.execution_guidance', 'agent.reasoning_effort', 'agent.disabled_toolsets', 'platform_toolsets.api_server', 'platform_toolsets.cli',
                   'kanban.auto_decompose', 'kanban.max_spawn', 'kanban.max_in_progress',
                   'kanban.dispatch_in_gateway', 'model.default', 'model.provider', 'hooks', 'hooks_auto_accept')
    TERMINAL = {'completed', 'failed', 'cancelled'}

    def __init__(self, control, config, session, runner=None):
        self.control, self.store, self.session = control, control.store, session
        self.config = copy.deepcopy(config)
        self.routes = self.config.get('routes', {})
        self.runner = runner or self._run_cli
        self._custom_runner = runner is not None
        self._locks = {}
        self.timeout = float(self.config.get('request_timeout_seconds', 10))
        if not 0 < self.timeout <= 60:
            raise ValueError('invalid_request_timeout')

    def _lock(self, job_id):
        return self._locks.setdefault(job_id, asyncio.Lock())

    def _get(self, key):
        with self.store.lock:
            row = self.store.db.execute('SELECT value FROM metadata WHERE key=?', (key,)).fetchone()
            return json.loads(row[0]) if row else None

    def _set(self, key, value):
        self.store.db.execute('INSERT INTO metadata VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value', (key, _json(value)))

    def _state(self, job_id, **updates):
        with self.store.transaction():
            value = self._get('hermes:state:' + job_id) or {}
            value.update(updates)
            self._set('hermes:state:' + job_id, value)
        return value

    def _route(self, bot_id):
        route = self.routes.get(bot_id)
        required = ('base_url', 'api_key_env', 'profile', 'host', 'hermes_home', 'kanban_home',
                    'workspace', 'model', 'provider', 'reasoning_effort')
        if not isinstance(route, dict) or any(not isinstance(route.get(k), str) or not route[k] for k in required):
            raise ValueError('route_not_configured')
        parsed = urlsplit(route['base_url'])
        if (parsed.scheme not in {'http', 'https'} or not parsed.hostname or parsed.username or parsed.password
                or parsed.query or parsed.fragment):
            raise ValueError('invalid_base_url')
        for key in ('hermes_home', 'kanban_home', 'workspace'):
            path = Path(route[key])
            if not path.is_absolute() or '..' in path.parts:
                raise ValueError('absolute_route_paths_required')
        if Path(route['kanban_home']) == Path(route['hermes_home']):
            raise ValueError('separate_kanban_home_required')
        return route

    def _key(self, route):
        key = os.environ.get(route['api_key_env'])
        if not key:
            raise ValueError('api_key_unavailable')
        return key

    def _route_fingerprint(self, route):
        return _hash(route)

    def _job_route(self, job_id):
        job = self.control.get_job(job_id)
        if not job:
            raise ValueError('job_not_found')
        route = self._route(job['bot_id'])
        if any(job.get('route', {}).get(k) != route[k] for k in ('host', 'profile')):
            raise ValueError('configured_route_mismatch')
        return job, route

    def _validation(self, job):
        result = self.control.validate(job['id'], job['capability'])
        if not result.get('allowed'):
            raise ValueError(result.get('reason') or 'execution_not_allowed')
        return result['limits']

    def _environment(self, route):
        env = {k: os.environ[k] for k in ('PATH', 'HOME', 'LANG', 'LC_ALL', 'TZ') if k in os.environ}
        env.update(HERMES_HOME=route['hermes_home'], HERMES_KANBAN_HOME=route['kanban_home'],
                   HERMES_PROFILE=route['profile'], PYTHONUNBUFFERED='1')
        guard = route.get('native_guard', {})
        if isinstance(guard, dict) and ('board' in guard or 'kanban_db' in guard):
            if not all(isinstance(guard.get(key), str) and guard[key] for key in ('board', 'kanban_db')):
                raise ValueError('invalid_native_board_identity')
            env.update(HERMES_KANBAN_BOARD=guard['board'], HERMES_KANBAN_DB=guard['kanban_db'])
        bindings = route.get('mcp_environment', {})
        if not isinstance(bindings, dict):
            raise ValueError('invalid_mcp_environment')
        for target, source in bindings.items():
            if (not isinstance(target, str) or not re.fullmatch(r'[A-Z][A-Z0-9_]*', target)
                    or not isinstance(source, str) or not re.fullmatch(r'[A-Z][A-Z0-9_]*', source)
                    or target in env or target.startswith(('HERMES_', 'PYTHON', 'LD_'))):
                raise ValueError('invalid_mcp_environment')
            if not os.environ.get(source):
                raise ValueError('mcp_environment_missing')
            env[target] = os.environ[source]
        return env

    async def _run_cli(self, argv, *, env, cwd, timeout):
        process = await asyncio.create_subprocess_exec(*argv, env=env, cwd=cwd,
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.DEVNULL)
        try:
            stdout, _ = await asyncio.wait_for(process.communicate(), timeout)
        except (asyncio.TimeoutError, asyncio.CancelledError):
            # This only ends the CLI transport; it never means a native job stopped.
            if process.returncode is None:
                process.kill()
            await process.wait()
            raise
        return {'returncode': process.returncode, 'stdout': stdout.decode('utf-8', errors='replace')}

    async def _cli(self, route, args, json_output=True, text_output=False):
        local = set(self.config.get('local_hosts', ('localhost', '127.0.0.1', socket.gethostname())))
        if route['host'] not in local and not self._custom_runner:
            raise ValueError('remote_cli_transport_unavailable')
        argv = [self.config.get('cli_path', 'hermes'), *args]
        result = await self.runner(argv, env=self._environment(route), cwd=route['workspace'], timeout=self.timeout)
        if result.get('returncode') != 0:
            raise ValueError('native_cli_failed')
        if not json_output and not text_output:
            return {'accepted': True}
        raw = result.get('stdout', '')
        if not isinstance(raw, str) or len(raw) > 4 * 1024 * 1024:
            raise ValueError('invalid_native_json')
        if text_output:
            return raw
        try:
            return json.loads(raw)
        except (ValueError, TypeError):
            # Some public CLI versions emit an update notice before a JSON object.
            for position, char in enumerate(raw):
                if char in '{[':
                    try:
                        return json.loads(raw[position:])
                    except ValueError:
                        continue
            raise ValueError('invalid_native_json') from None

    async def _http(self, route, method, path, body=None, idempotency_key=None):
        headers = {'Authorization': 'Bearer ' + self._key(route), 'Content-Type': 'application/json'}
        if idempotency_key:
            headers['Idempotency-Key'] = idempotency_key
        async with self.session.request(method, route['base_url'].rstrip('/') + path,
                headers=headers, data=None if body is None else _json(body).encode(),
                timeout=aiohttp.ClientTimeout(total=self.timeout), allow_redirects=False) as response:
            raw = await response.content.read(4 * 1024 * 1024 + 1)
            if len(raw) > 4 * 1024 * 1024:
                raise ValueError('native_response_too_large')
            try:
                payload = json.loads(raw)
            except ValueError:
                payload = {}
            return response.status, payload

    async def discover(self, bot_id):
        """Read capabilities and non-secret native config; never starts work."""
        try:
            route = self._route(bot_id)
            status, caps = await self._http(route, 'GET', '/v1/capabilities')
            if status != 200 or not isinstance(caps, dict):
                raise ValueError('capabilities_unavailable')
            status, tools = await self._http(route, 'GET', '/v1/toolsets')
            if status != 200 or not isinstance(tools, dict) or not isinstance(tools.get('data'), list):
                raise ValueError('toolsets_unavailable')
            native = {}
            errors = []
            for name in self.CONFIG_KEYS:
                try:
                    native[name] = await self._cli(route, ['config', 'get', name, '--json'])
                except ValueError as exc:
                    native[name] = None
                    errors.append(self._discovery_error(exc))
            features = caps.get('features', {})
            retention = features.get('runs_idempotency', {})
            if not all(features.get(k) for k in ('run_submission', 'run_status', 'run_stop', 'run_steer')):
                errors.append('run_control_unavailable')
            if not (retention.get('supported') and retention.get('durable') and _number(retention.get('retention_seconds')) and retention['retention_seconds'] > 0):
                errors.append('durable_idempotency_unavailable')
            if not all(_number(native.get(k)) and native[k] > 0 for k in ('agent.max_turns', 'agent.run_budget_seconds', 'agent.api_max_retries')):
                errors.append('native_limits_unconfigured')
            if native.get('model.default') != route['model'] or native.get('model.provider') != route['provider']:
                errors.append('native_model_route_mismatch')
            if native.get('agent.reasoning_effort') != route['reasoning_effort']:
                errors.append('native_reasoning_mismatch')
            if route.get('allowed_mcp_toolsets') and native.get('agent.execution_guidance') is not False:
                errors.append('mcp_execution_guidance_must_be_disabled')
            inventory = tools['data']
            inventory = await self._mcp_inventory(route, native, inventory)
            errors.extend(self._tool_boundary(route, native, inventory))
            native['guard_verified'] = self._guard_verified(route, native)
            if not native['guard_verified']:
                errors.append('native_guard_unverified')
            # Arbitrary hook commands can contain sensitive arguments. Keep only
            # verification, never copy unapproved command strings to evidence.
            native['hooks'] = {'exact_native_guard': native['guard_verified']}
            result = {'status': 'ready' if not errors else 'blocked', 'bot_id': bot_id,
                'capabilities': caps, 'native_limits': native, 'errors': errors,
                'retention_seconds': min(float(retention.get('retention_seconds') or 0), 86400),
                'route_fingerprint': self._route_fingerprint(route), 'observed_at': time.time(),
                'limits': ['Public configuration is checked at admission; no hard native USD billing cutoff.',
                           'API run_budget_seconds is cooperative; in-flight calls and dispatcher shutdown can overrun wall time.',
                           'Only explicitly configured GTD MCP toolsets and exact tool names are admitted; shell, native delegation and other MCP routes are excluded.',
                           'All work requires the exact fail-closed native guard; effective hook loading and lifecycle completion need a live canary.']}
            with self.store.transaction():
                self._set('hermes:discovery:' + bot_id, result)
            return result
        except (ValueError, OSError, asyncio.TimeoutError, aiohttp.ClientError) as exc:
            result = {'status': 'blocked', 'bot_id': bot_id, 'errors': [self._discovery_error(exc)]}
            with self.store.transaction():
                self._set('hermes:discovery:' + bot_id, result)
            return result

    @staticmethod
    def _discovery_error(exc):
        safe = {'mcp_execution_guidance_must_be_disabled', 'native_guard_unverified', 'capabilities_unavailable', 'toolsets_unavailable', 'invalid_mcp_allowlist', 'mcp_direct_schemas_required',
                'mcp_enabled_servers_mismatch', 'invalid_mcp_server_config', 'mcp_filters_not_exact',
                'mcp_inventory_missing', 'mcp_inventory_mismatch', 'remote_cli_transport_unavailable',
                'native_cli_failed', 'invalid_native_json', 'native_response_too_large',
                'route_not_configured', 'invalid_base_url', 'absolute_route_paths_required',
                'separate_kanban_home_required', 'api_key_unavailable'}
        return str(exc) if isinstance(exc, ValueError) and str(exc) in safe else 'native_discovery_unavailable'

    async def _mcp_inventory(self, route, native, advertised):
        allowed = route.get('allowed_mcp_toolsets', {})
        if (not isinstance(allowed, dict) or any(not isinstance(server, str)
                or not re.fullmatch(r'[A-Za-z0-9_]+', server)
                or not isinstance(names, list) or not names
                or any(not isinstance(name, str) or not re.fullmatch(r'[A-Za-z0-9_]+', name) for name in names)
                or len(set(names)) != len(names) for server, names in allowed.items())):
            raise ValueError('invalid_mcp_allowlist')
        # The global guard admits direct MCP names, never the native search/call bridge.
        if allowed and native.get('tools.tool_search.enabled') != 'off':
            raise ValueError('mcp_direct_schemas_required')
        # Full config is transient: project only names and enabled state. Never
        # persist or report commands, URLs, environment bindings or credentials.
        servers = await self._cli(route, ['config', 'get', 'mcp_servers', '--json'])
        if servers is None and not allowed:
            servers = {}
        if not isinstance(servers, dict) or any(not isinstance(name, str) or not isinstance(value, dict)
                or ('enabled' in value and not isinstance(value['enabled'], bool)) for name, value in servers.items()):
            raise ValueError('invalid_mcp_server_config')
        enabled = {name for name, value in servers.items() if value.get('enabled', True)}
        if enabled != set(allowed):
            raise ValueError('mcp_enabled_servers_mismatch')
        native['mcp_servers_verified'] = {name: value.get('enabled', True) for name, value in servers.items()}
        del servers
        result = list(advertised)
        for server, names in allowed.items():
            filters = await self._cli(route, ['config', 'get', 'mcp_servers.' + server + '.tools', '--json'])
            if (not isinstance(filters, dict) or set(filters.get('include', [])) != set(names)
                    or filters.get('exclude') or filters.get('prompts') is not False
                    or filters.get('resources') is not False):
                raise ValueError('mcp_filters_not_exact')
            raw = await self._cli(route, ['mcp', 'test', server], text_output=True)
            raw = re.sub(r'\x1b\[[0-9;]*m', '', raw)
            match = re.search(r'Tools discovered: ([0-9]+)\s*\n', raw)
            if not match:
                raise ValueError('mcp_inventory_missing')
            lines = [line for line in raw[match.end():].splitlines() if line.strip()]
            parsed = [re.fullmatch(r'    ([A-Za-z0-9_]+)\s+.*', line) for line in lines]
            found = [entry.group(1) for entry in parsed if entry]
            if (len(found) != len(lines) or len(found) != int(match.group(1))
                    or len(set(found)) != len(found) or set(found) != set(names)):
                raise ValueError('mcp_inventory_mismatch')
            # Public CLI lists original names; schema registration applies this
            # exact prefix. Config and HTTP inventory constrain platform membership;
            # CLI discovery is not proof that the running gateway loaded hooks.
            result.append({'name': server, 'enabled': True, 'configured': True,
                           'tools': ['mcp__' + server + '__' + tool for tool in found]})
        return result

    @staticmethod
    def _tool_boundary(route, native, advertised):
        allowed = route.get('allowed_mcp_toolsets', {})
        if (not isinstance(allowed, dict) or any(not isinstance(name, str) or not re.fullmatch(r'[A-Za-z0-9_]+', name)
                or not isinstance(names, list) or not names or any(not isinstance(n, str) or not n for n in names)
                for name, names in allowed.items())):
            return ['invalid_mcp_allowlist']
        # Configuration uses server names; Hermes registers mcp-<server>
        # and wire names mcp__<server>__<tool>.
        # Require unambiguous components; never strip a foreign server prefix.
        components = [part for name, names in allowed.items() for part in [name, *names]]
        if any(any(c not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_' for c in part)
               for part in components):
            return ['invalid_mcp_allowlist']
        expected = {name: {'mcp__' + name + '__' + tool for tool in names}
                    for name, names in allowed.items()}
        configured = native.get('platform_toolsets.api_server')
        if not isinstance(configured, list) or set(configured) != set(allowed):
            return ['uncontrolled_native_tools']
        observed = {}
        for row in advertised:
            if not isinstance(row, dict) or not isinstance(row.get('name'), str):
                return ['invalid_native_tool_inventory']
            name = row['name']
            # Hermes automatically includes default MCP servers when constructing
            # an agent. A configured unknown MCP is unsafe even when this endpoint
            # reports enabled=False (its enumeration omits default MCP additions).
            active = row.get('enabled') or (name.startswith(('mcp-', 'mcp_')) and row.get('configured'))
            if active and name not in allowed:
                return ['uncontrolled_native_tools']
            if name in allowed:
                tools = row.get('tools')
                if (not isinstance(tools, list) or any(not isinstance(t, str) for t in tools)
                        or not row.get('enabled') or not row.get('configured')
                        or set(tools) != expected[name]):
                    return ['mcp_tool_inventory_mismatch']
                observed[name] = tools
        if set(observed) != set(allowed):
            return ['mcp_tool_inventory_incomplete']
        return []

    def _guard_verified(self, route, native):
        guard = route.get('native_guard')
        fields = {'python', 'path', 'sha256', 'parent_python', 'profile', 'kanban_home',
                  'context_path', 'context_sha256', 'board', 'kanban_db', 'hermes', 'receipts_dir'}
        if not isinstance(guard, dict) or set(guard) != fields:
            return False
        try:
            interpreter, script, context = [Path(guard[key]) for key in ('python', 'path', 'context_path')]
            if (not interpreter.is_absolute() or interpreter.resolve() != Path(sys.executable).resolve()
                    or not os.access(interpreter, os.X_OK) or script.parent != context.parent):
                return False
            for path, filename, digest_key in ((script, 'native_guard.py', 'sha256'),
                                               (context, 'native_context.py', 'context_sha256')):
                if (not path.is_absolute() or not path.is_file() or path.resolve() != path
                        or path.name != filename):
                    return False
                digest = hashlib.sha256(Path(__file__).with_name(filename).read_bytes()).hexdigest()
                if guard[digest_key] != digest or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                    return False
            for key in ('parent_python', 'hermes'):
                executable = Path(guard[key])
                if not executable.is_absolute() or not executable.is_file() or not os.access(executable, os.X_OK):
                    return False
            if guard['hermes'] != self.config.get('cli_path'):
                return False
            for key in ('profile', 'kanban_home', 'receipts_dir'):
                directory = Path(guard[key])
                if not directory.is_absolute() or not directory.is_dir() or directory.resolve() != directory:
                    return False
            if (guard['profile'] != route['hermes_home'] or guard['kanban_home'] != route['kanban_home']
                    or guard['profile'] == guard['kanban_home']
                    or not isinstance(guard['board'], str) or not re.fullmatch(r'[a-z0-9][a-z0-9_-]*', guard['board'])):
                return False
            receipt_stat = Path(guard['receipts_dir']).stat()
            db = Path(guard['kanban_db'])
            if (receipt_stat.st_uid != os.getuid() or receipt_stat.st_mode & 0o777 != 0o700
                    or not db.is_absolute() or not db.is_file() or db.resolve() != db):
                return False
            flags = ['--parent-python', guard['parent_python'], '--profile', guard['profile'],
                '--kanban-home', guard['kanban_home'], '--board', guard['board'], '--kanban-db', guard['kanban_db'],
                '--hermes', guard['hermes'], '--receipts-dir', guard['receipts_dir']]
            expected = {
                'output_spill': {'enabled': True, 'max_chars': 10000},
                'pre_tool_call': [{'matcher': '.*', 'command': shlex.join([str(interpreter), '-B', str(script), *flags]),
                                   'timeout': 20, 'fail_closed': True}],
                'pre_llm_call': [{'command': shlex.join([str(interpreter), '-B', str(context), *flags]), 'timeout': 20}]}
            return native.get('hooks') == expected and native.get('hooks_auto_accept') is True
        except (OSError, ValueError, TypeError, KeyError):
            return False

    def _check_limits(self, route, discovery, limits, durable):
        if discovery.get('status') != 'ready':
            raise ValueError('native_route_not_ready')
        native = discovery['native_limits']
        maximum_turns = route.get('max_turns', 1)
        if (not _number(maximum_turns) or maximum_turns < 1
                or native['agent.max_turns'] > maximum_turns
                or native['agent.run_budget_seconds'] > limits['max_runtime_seconds']
                or native['agent.api_max_retries'] > limits['max_retries'] + 1):
            raise ValueError('native_limits_exceed_reservation')
        reservation = route.get('reservation_cost_usd')
        if not _number(reservation) or reservation <= 0 or (limits.get('cost_control', True) and reservation > limits['max_cost_usd']):
            raise ValueError('route_reservation_insufficient')
        if native.get('guard_verified') is not True:
            raise ValueError('native_descendant_limit_unverified')
        if durable:
            if limits['max_descendants'] != 0:
                raise ValueError('durable_native_descendants_disabled')
            if 'kanban' in (native.get('agent.disabled_toolsets') or []):
                raise ValueError('native_lifecycle_disabled')
            cli_tools = native.get('platform_toolsets.cli')
            if route.get('allowed_mcp_toolsets') and cli_tools != ['no_mcp']:
                raise ValueError('durable_implicit_mcp_not_allowed')
            if (cli_tools not in ([], ['no_mcp']) or native.get('kanban.auto_decompose') is not False
                    or native.get('kanban.max_spawn') != 1 or native.get('kanban.max_in_progress') != 1
                    or native.get('kanban.dispatch_in_gateway') is not True):
                raise ValueError('durable_native_limits_unverified')

    def _body(self, job, route, prompt, durable, limits):
        if not isinstance(prompt, str) or not prompt.strip():
            raise ValueError('prompt_required')
        if durable:
            return {'title': 'GTD ' + job['id'], 'body': prompt, 'created_by': 'gtd:' + job['id'],
                'assignee': route['profile'], 'workspace': 'dir:' + route['workspace'],
                'model': route['model'], 'provider': route['provider'],
                'max_runtime_seconds': limits['max_runtime_seconds'], 'max_retries': 1,
                'completion_contract': 'local-only'}
        return {'input': prompt, 'model': route['model'], 'provider': route['provider'],
            'model_options': {'reasoning_effort': route['reasoning_effort']}, 'require_model_lock': True}

    def _intent(self, job, route, body, durable, discovery, limits):
        key = 'hermes:intent:' + job['id']
        candidate = {'job_id': job['id'], 'bot_id': job['bot_id'], 'durable': durable, 'body': body,
            'body_hash': _hash(body), 'route': {k: route[k] for k in ('base_url', 'host', 'profile', 'hermes_home', 'kanban_home', 'workspace', 'model', 'provider', 'reasoning_effort')},
            'route_fingerprint': self._route_fingerprint(route),
            'key_fingerprint': hashlib.sha256(self._key(route).encode()).hexdigest(),
            'limits': limits, 'retention_seconds': discovery['retention_seconds']}
        with self.store.transaction():
            if self._get('hermes:no-dispatch:' + job['id']):
                raise ValueError('admission_already_closed')
            previous = self._get(key)
            if previous:
                if any(previous[k] != candidate[k] for k in ('body_hash', 'route_fingerprint', 'key_fingerprint', 'durable')):
                    raise ValueError('intent_conflict')
                return previous, False
            candidate['created_at'] = time.time()
            self._set(key, candidate)
            self._set('hermes:state:' + job['id'], {'delivery': 'intent', 'native_id': None})
        return candidate, True

    def _same_route(self, route, intent):
        if self._route_fingerprint(route) != intent['route_fingerprint']:
            raise ValueError('route_changed')
        if hashlib.sha256(self._key(route).encode()).hexdigest() != intent['key_fingerprint']:
            raise ValueError('api_key_rotated')

    def _native(self, route, native_id, durable):
        return {'provider': 'hermes-kanban' if durable else 'hermes', 'host': route['host'], 'profile': route['profile'], 'id': native_id}

    def _uncertain(self, job_id, reason):
        state = self._state(job_id, delivery='uncertain', error=reason)
        job = self.control.get_job(job_id)
        if job and job.get('native') and not job.get('terminal'):
            self.control.observe(job_id, {'native_identity': job['native'], 'native_status': 'uncertain',
                'terminal': False, 'evidence_reference': 'hermes:state:' + job_id,
                'runtime_seconds': job.get('observed_runtime_seconds', 0), 'cost_usd': None})
        return {'status': 'uncertain', 'job_id': job_id, 'native_id': state.get('native_id'), 'error': reason}

    def _reject_no_effect(self, job_id, reason):
        job = self.control.get_job(job_id)
        if not job:
            return {'status': 'rejected', 'job_id': job_id, 'error': reason}
        evidence_key = 'hermes:no-dispatch:' + job_id
        with self.store.transaction():
            job = self.control.get_job(job_id)
            proof = self._get(evidence_key)
            if proof and (job.get('native') or {}).get('provider') == 'gtd-hermes-admission' and job.get('terminal'):
                return {'status': 'rejected', 'job_id': job_id, 'error': proof['reason'], 'no_effect': True,
                        'terminal': True, 'evidence_reference': evidence_key}
            if self._get('hermes:intent:' + job_id) or job.get('native'):
                return {'status': 'uncertain', 'job_id': job_id, 'error': reason, 'no_effect': False}
            if proof is None:
                proof = {'job_id': job_id, 'reason': reason, 'dispatch_attempted': False,
                         'observed_at': time.time(), 'scope': 'local_adapter_admission'}
                self._set(evidence_key, proof)
        # The marker prevents any adapter from installing an intent between this
        # check and observation. This identity explicitly names a LOCAL admission,
        # not a fabricated remote run. No native reference was ever acknowledged.
        native = {'provider': 'gtd-hermes-admission', 'host': job['route']['host'],
                  'profile': job['route']['profile'], 'id': 'undispatched:' + job_id}
        observation = {'native_identity': native, 'native_status': 'failed', 'terminal': True,
            'runtime_seconds': 0, 'cost_usd': 0, 'evidence_reference': evidence_key,
            'no_effect': True, 'scope': 'local_adapter_admission'}
        recorded = self.control.observe(job_id, observation)
        return {'status': 'rejected', 'job_id': job_id, 'error': proof['reason'], 'no_effect': True,
                'terminal': recorded.get('status') == 'recorded', 'evidence_reference': evidence_key}

    async def submit(self, job_id, prompt, durable=False):
        async with self._lock(job_id):
            try:
                job, route = self._job_route(job_id)
                old = self._get('hermes:intent:' + job_id)
                if old:
                    self._same_route(route, old)
                    body = self._body(job, route, prompt, durable, old['limits'])
                    if old['body_hash'] != _hash(body) or old['durable'] != durable:
                        raise ValueError('intent_conflict')
                    state = self._get('hermes:state:' + job_id) or {}
                    if state.get('native_id'):
                        return {'status': 'already_submitted', 'job_id': job_id, 'native_id': state['native_id']}
                    if state.get('never_sent'):
                        # A previous attempt never reached the provider (no
                        # slot): reconcile-style first send, not a blind retry.
                        return await self._first_send(job, route, old, durable)
                    return self._uncertain(job_id, 'dispatch_receipt_missing_reconcile')
                limits = self._validation(job)
                discovery = await self.discover(job['bot_id'])
                self._check_limits(route, discovery, limits, durable)
                # Revalidate after discovery, before persisting and again before effect.
                limits = self._validation(job)
                self._check_limits(route, discovery, limits, durable)
                body = self._body(job, route, prompt, durable, limits)
                intent, created = self._intent(job, route, body, durable, discovery, limits)
                if not created:
                    return self._uncertain(job_id, 'concurrent_intent_reconcile')
                return await self._dispatch(job, route, intent)
            except ValueError as exc:
                if str(exc) in {'api_key_rotated', 'route_changed'} and self._get('hermes:intent:' + job_id):
                    return self._uncertain(job_id, str(exc))
                if (self._get('hermes:state:' + job_id) or {}).get('delivery') == 'sending':
                    return self._uncertain(job_id, 'native_submission_unconfirmed')
                return self._reject_no_effect(job_id, str(exc))
            except (OSError, asyncio.TimeoutError, aiohttp.ClientError):
                if not self._get('hermes:intent:' + job_id):
                    return self._reject_no_effect(job_id, 'preflight_transport_failed')
                return self._uncertain(job_id, 'native_transport_uncertain')

    async def _first_send(self, job, route, intent, durable_check):
        # Shared first-send tail: revalidate, reclaim the slot and perform the
        # initial remote creation. Used when the adapter durably knows nothing
        # was ever sent (never_sent), from submit retries and reconciliations.
        # durable_check mirrors each caller's strictness (submit uses its
        # durable flag; reconcile keeps its historical relaxed check).
        self._validation(job)
        discovery = await self.discover(job['bot_id'])
        self._check_limits(route, discovery, self._validation(job), durable_check)
        return await self._dispatch(job, route, intent)

    async def _dispatch(self, job, route, intent):
        self._validation(job)
        self._same_route(route, intent)
        # Claim the single global native slot durably BEFORE any remote
        # effect. The network stays outside the storage transaction; if the
        # slot is taken, persist never_sent (nothing reached the provider) and
        # return without creating a second remote run. The claim and the flag
        # survive uncertainty and restarts via the persisted intent/state.
        claimed = self.control.claim_dispatch(job['id'])
        if claimed.get('status') != 'claimed':
            out = self._uncertain(job['id'], claimed.get('error', 'native_slot_busy'))
            self._state(job['id'], never_sent=True)
            return out
        self._state(job['id'], delivery='sending', never_sent=False)
        if intent['durable']:
            body = intent['body']
            args = ['kanban', 'create', body['title'], '--body', body['body'], '--created-by', body['created_by'],
                '--assignee', body['assignee'], '--workspace', body['workspace'], '--model', body['model'],
                '--provider', body['provider'], '--max-runtime', str(body['max_runtime_seconds']) + 's',
                '--max-retries', '1', '--completion-contract', 'local-only', '--idempotency-key', job['id'], '--json']
            payload = await self._cli(route, args)
            native_id = payload.get('id') if isinstance(payload, dict) else None
        else:
            status, payload = await self._http(route, 'POST', '/v1/runs', intent['body'], job['id'])
            if status != 202:
                return self._uncertain(job['id'], 'native_submission_http_' + str(status))
            native_id = payload.get('run_id') if isinstance(payload, dict) else None
        if not isinstance(native_id, str) or not native_id or len(native_id) > 200:
            return self._uncertain(job['id'], 'native_identity_missing')
        self._state(job['id'], delivery='acknowledged', native_id=native_id)
        recorded = self.control.record_dispatch(job['id'], self._native(route, native_id, intent['durable']))
        if recorded.get('status') != 'recorded':
            return self._uncertain(job['id'], 'dispatch_record_rejected')
        # Durable admission anchor: a native run was proven to exist remotely
        # (validated native_id). Local wall time from here bounds enforcement
        # even if the provider later stops updating its own timestamps. Never
        # set on never_sent/uncertain paths, so nonexistent execution is never
        # charged. Same local clock for both ends: no cross-clock skew.
        self._state(job['id'], native_admitted_at=time.time())
        return {'status': 'submitted', 'job_id': job['id'], 'native_id': native_id}

    async def poll(self, job_id):
        async with self._lock(job_id):
            return await self._poll(job_id)

    async def _poll(self, job_id):
        try:
            job, route = self._job_route(job_id)
            intent, state = self._get('hermes:intent:' + job_id), self._get('hermes:state:' + job_id) or {}
            if not intent or not state.get('native_id'):
                return self._uncertain(job_id, 'native_identity_missing')
            self._same_route(route, intent)
            if job.get('terminal') and state.get('last_result'):
                return state['last_result']
            native_id = state['native_id']
            if intent['durable']:
                payload = await self._cli(route, ['kanban', 'show', native_id, '--json'])
                return self._observe_kanban(job, route, intent, payload)
            status, payload = await self._http(route, 'GET', '/v1/runs/' + quote(native_id, safe=''))
            if status != 200:
                return self._uncertain(job_id, 'native_status_http_' + str(status))
            if payload.get('run_id') != native_id:
                return self._uncertain(job_id, 'native_identity_mismatch')
            return self._observe_api(job, route, intent, payload)
        except ValueError as exc:
            return self._uncertain(job_id, str(exc))
        except (OSError, asyncio.TimeoutError, aiohttp.ClientError):
            return self._uncertain(job_id, 'native_poll_uncertain')

    def _artifact(self, job_id, output, payload):
        if not isinstance(output, str):
            output = _json(output)
        content = output.encode()
        if len(content) > 4 * 1024 * 1024:
            raise ValueError('native_artifact_too_large')
        with self.store.transaction():
            blob = self.store.save_original(content)
            self.store.db.execute('INSERT OR IGNORE INTO originals VALUES(?,?,?)', (blob['sha256'], blob['size'], blob['path']))
            artifact = {**blob, 'mime_type': 'text/plain; charset=utf-8', 'job_id': job_id, 'native_evidence_hash': _hash(payload)}
            self._set('hermes:artifact:' + job_id, artifact)
        return artifact

    def _record_observation(self, job, route, intent, payload, status, runtime, output=None, native_runtime=None):
        terminal = status in self.TERMINAL
        native_id = (self._get('hermes:state:' + job['id']) or {})['native_id']
        native = self._native(route, native_id, intent['durable'])
        usage = payload.get('usage') if isinstance(payload.get('usage'), dict) else {}
        cost = payload.get('cost_usd', usage.get('cost_usd'))
        if not _number(cost):
            cost = None
        runtime = max(job.get('observed_runtime_seconds', 0), runtime)
        artifact = self._artifact(job['id'], output, payload) if terminal and output is not None else None
        evidence_key = 'hermes:observation:' + job['id'] + ':' + _hash(payload)
        observation = {'native_identity': native, 'native_status': status, 'terminal': terminal,
            'runtime_seconds': runtime, 'native_runtime_seconds': native_runtime, 'cost_usd': cost, 'usage': usage,
            'cost_telemetry': 'unknown' if cost is None else 'provider_reported', 'evidence_reference': evidence_key}
        with self.store.transaction():
            self._set(evidence_key, {'observed_at': time.time(), 'payload': payload, 'observation': observation, 'artifact': artifact})
        receipt = self.control.observe(job['id'], observation)
        if receipt.get('status') != 'recorded':
            return self._uncertain(job['id'], 'native_observation_rejected')
        result = {'status': 'observed', 'job_id': job['id'], 'native_id': native_id,
            'native_status': status, 'terminal': terminal, 'observation': observation}
        if output is not None:
            result['output'] = output
        if artifact:
            result['artifact'] = artifact
        self._state(job['id'], last_result=result, delivery='observed')
        return result

    def _admitted_elapsed(self, job):
        # Local wall time since the durably proven remote admission. One-time
        # backfill for runs admitted before this guard existed (conservative
        # under-count, documented); afterwards the anchor never moves, so
        # restarts/reconciles cannot reset the deadline. max(0,...) bounds a
        # backward local clock jump; a forward jump fails safe (earlier STOP).
        state = self._get('hermes:state:' + job['id']) or {}
        admitted = state.get('native_admitted_at')
        if not _number(admitted):
            admitted = time.time()
            self._state(job['id'], native_admitted_at=admitted)
        return max(0.0, time.time() - admitted)

    def _observe_api(self, job, route, intent, payload):
        raw = payload.get('status')
        status = {'started': 'running', 'stopping': 'running', 'interrupted': 'failed'}.get(raw, raw)
        if status not in self.TERMINAL | {'queued', 'running', 'waiting'}:
            return self._uncertain(job['id'], 'unknown_native_status')
        start, finish = payload.get('created_at'), payload.get('updated_at')
        native_runtime = max(0, finish - start) if _number(start) and _number(finish) else None
        if status == 'running':
            # Provider silence (frozen updated_at) must not freeze enforcement:
            # floor by local elapsed since proven admission. queued/waiting keep
            # remote-derived values so unstarted execution is never charged.
            floor = self._admitted_elapsed(job)
            base = native_runtime if native_runtime is not None else job.get('observed_runtime_seconds', 0)
            runtime = max(base, floor)
        else:
            runtime = (max(0, finish - start) if _number(start) and _number(finish)
                       else (job['max_runtime_seconds'] if status in self.TERMINAL else job.get('observed_runtime_seconds', 0)))
        return self._record_observation(job, route, intent, payload, status, runtime, payload.get('output'), native_runtime=native_runtime)

    def _observe_kanban(self, job, route, intent, payload):
        if not isinstance(payload, dict):
            return self._uncertain(job['id'], 'invalid_kanban_status')
        task, runs = payload.get('task', payload), payload.get('runs', [])
        native_id = (self._get('hermes:state:' + job['id']) or {}).get('native_id')
        if task.get('id') != native_id or payload.get('children'):
            return self._uncertain(job['id'], 'kanban_identity_or_descendants_unverified')
        if not isinstance(runs, list) or any(not isinstance(run, dict) for run in runs):
            return self._uncertain(job['id'], 'invalid_kanban_runs')
        live = any(run.get('worker_pid') or (run.get('started_at') and not run.get('ended_at')) for run in runs)
        latest = max(runs, key=lambda r: r.get('id', 0)) if runs else {}
        raw, status = task.get('status'), 'waiting'
        if raw == 'done' and not live:
            status = 'completed'
        elif raw == 'running' or live:
            status = 'running'
        elif raw in {'ready', 'todo'}:
            status = 'queued'
        if not live and latest.get('outcome') == 'gave_up':
            status = 'failed'
        if (not live and task.get('assignee') is None and latest.get('outcome') == 'reclaimed'
                and latest.get('metadata', {}).get('terminated') is True):
            status = 'cancelled'
        # Public show omits task claim fields and run.task_id. Its runs/events
        # are scoped by the exact show task ID. Native block_task atomically
        # clears claim/PID, ends the run, and records blocked(run_id); assign_task
        # then records assigned. Require that causal public tail, not absent keys.
        stop = self._get('hermes:stop:' + job['id']) or {}
        stop_receipt = stop.get('receipt') or {}
        closed_runs = bool(runs) and all(
            'worker_pid' in run and run['worker_pid'] is None
            and _number(run.get('started_at')) and _number(run.get('ended_at'))
            and run['ended_at'] >= run['started_at']
            and run.get('status') and run['status'] not in {'running', 'queued', 'pending'}
            and run.get('outcome') for run in runs)
        events = payload.get('events', [])
        public_release = False
        if isinstance(events, list) and all(isinstance(event, dict) for event in events):
            blocked = [index for index, event in enumerate(events)
                if event.get('kind') == 'blocked' and event.get('run_id') == latest.get('id')
                and _number(event.get('created_at')) and _number(latest.get('ended_at'))
                and event['created_at'] >= latest['ended_at']]
            tail = events[blocked[-1]+1:] if blocked else []
            public_release = (bool(tail) and all(event.get('kind') == 'assigned' for event in tail)
                and tail[-1].get('payload') == {'assignee': None}
                and _number(tail[-1].get('created_at')) and _number(stop.get('requested_at'))
                and tail[-1]['created_at'] >= int(stop['requested_at'])
                and latest.get('status') == 'blocked' and latest.get('outcome') == 'blocked')
        if (raw == 'blocked' and intent.get('durable') is True and job.get('stop_requested')
                and stop.get('native_id') == native_id
                and stop_receipt == {'status':'stop_requested', 'job_id':job['id'],
                    'native_id':native_id, 'terminal':False}
                and 'assignee' in task and task['assignee'] is None
                and closed_runs and public_release):
            status = 'cancelled'
        # 'blocked' without a closed run is a wait, never proof of termination.
        runtime = sum(max(0, run['ended_at'] - run['started_at']) for run in runs
            if _number(run.get('started_at')) and _number(run.get('ended_at')))
        output = task.get('result') or payload.get('latest_summary')
        return self._record_observation(job, route, intent, payload, status, runtime, output)

    async def reconcile(self, job_id):
        async with self._lock(job_id):
            try:
                job, route = self._job_route(job_id)
                intent, state = self._get('hermes:intent:' + job_id), self._get('hermes:state:' + job_id) or {}
                if not intent:
                    return {'status': 'rejected', 'job_id': job_id, 'error': 'intent_missing'}
                self._same_route(route, intent)
                if state.get('native_id'):
                    return await self._poll(job_id)
                if intent['durable']:
                    if (state.get('never_sent') and not state.get('native_id')
                            and not self._get('hermes:no-dispatch:' + job_id)):
                        # Durably never sent (slot was busy): this is a first
                        # send, not a recovery. Revalidate, reclaim and create
                        # once the slot is free; an uncertain send without
                        # receipt keeps the inventory path below, never a blind
                        # recreation.
                        result = await self._first_send(job, route, intent, False)
                        if result.get('status') == 'submitted':
                            return await self._poll(job_id)
                        return result
                    matches = []
                    for extra in ([], ['--archived']):
                        tasks = await self._cli(route, ['kanban', 'list', '--json', *extra])
                        if not isinstance(tasks, list):
                            raise ValueError('invalid_kanban_inventory')
                        matches.extend(t for t in tasks if t.get('created_by') == 'gtd:' + job_id
                            and t.get('title') == intent['body']['title'] and t.get('body') == intent['body']['body'])
                    identities = {t['id'] for t in matches}
                    if len(identities) != 1:
                        return self._uncertain(job_id, 'kanban_receipt_not_uniquely_recovered')
                    native_id = identities.pop()
                    self._state(job_id, native_id=native_id)
                    self.control.record_dispatch(job_id, self._native(route, native_id, True))
                    return await self._poll(job_id)
                age = time.time() - intent['created_at']
                if not 0 <= age < intent['retention_seconds']:
                    return self._uncertain(job_id, 'idempotency_retention_expired')
                # Same job id, exact body, route and key only; an expired or known
                # missing identity is never submitted as replacement work.
                self._validation(job)
                discovery = await self.discover(job['bot_id'])
                self._check_limits(route, discovery, self._validation(job), False)
                result = await self._dispatch(job, route, intent)
                if result.get('status') == 'submitted':
                    return await self._poll(job_id)
                return result
            except ValueError as exc:
                return self._uncertain(job_id, str(exc))
            except (OSError, asyncio.TimeoutError, aiohttp.ClientError):
                return self._uncertain(job_id, 'native_reconciliation_uncertain')

    async def stop(self, job_id):
        # Descendants registered by ExecutionControl have independent exact
        # identities. Stop each one; never guess PIDs or traverse native tasks
        # that were not admitted through control. Bounded descendant walk via
        # parent_run_id (families are tiny), never a full pending scan.
        affected = {job_id}
        store = self.control.store
        while True:
            placeholders = ",".join("?" for _ in affected)
            rows = store.db.execute(
                f"SELECT id FROM runs WHERE parent_run_id IN ({placeholders})",
                tuple(affected)).fetchall()
            expanded = affected | {r["id"] for r in rows}
            if expanded == affected:
                break
            affected = expanded
            if len(affected) > 64:
                break
        result = await self._stop_one(job_id)
        children = [await self._stop_one(identity) for identity in sorted(affected - {job_id})]
        if children:
            result = {**result, 'children': children, 'terminal': False}
        return result

    async def _stop_one(self, job_id):
        async with self._lock(job_id):
            try:
                job, route = self._job_route(job_id)
                intent, state = self._get('hermes:intent:' + job_id), self._get('hermes:state:' + job_id) or {}
                if not intent or not state.get('native_id'):
                    return self._uncertain(job_id, 'native_identity_missing')
                self._same_route(route, intent)
                if job.get('terminal'):
                    return await self._poll(job_id)
                key = 'hermes:stop:' + job_id
                old = self._get(key)
                if old and old.get('receipt'):
                    # Durable idempotent STOP: an already requested stop is
                    # returned verbatim, even after the limit (when validate
                    # would refuse). One remote stop per admitted identity.
                    return old['receipt']
                # Stop is permitted after revocation/version changes. validate's
                # refusal is recorded, not misread as permission to continue work.
                validation = self.control.validate(job_id, job['capability'])
                requested = self.control.request_stop(job.get('requested_by') or self.control.service.principal_actor, 'hermes-stop:' + job_id, job_id)
                if requested.get('status') == 'rejected':
                    raise ValueError('stop_not_authorized')
                with self.store.transaction():
                    old = self._get(key)
                    if old:
                        return old.get('receipt') or {'status': 'uncertain', 'job_id': job_id, 'error': 'stop_receipt_missing'}
                    self._set(key, {'requested_at': time.time(), 'native_id': state['native_id'], 'validation': validation})
                native_id = state['native_id']
                if intent['durable']:
                    await self._cli(route, ['kanban', 'reassign', native_id, 'none', '--reclaim', '--reason', 'GTD stop requested'], json_output=False)
                else:
                    status, payload = await self._http(route, 'POST', '/v1/runs/' + quote(native_id, safe='') + '/stop', {})
                    if status not in {200, 202}:
                        return self._uncertain(job_id, 'native_stop_http_' + str(status))
                receipt = {'status': 'stop_requested', 'job_id': job_id, 'native_id': native_id, 'terminal': False}
                with self.store.transaction():
                    record = self._get('hermes:stop:' + job_id)
                    record['receipt'] = receipt
                    self._set('hermes:stop:' + job_id, record)
                return receipt
            except ValueError as exc:
                return self._uncertain(job_id, str(exc))
            except (OSError, asyncio.TimeoutError, aiohttp.ClientError):
                return self._uncertain(job_id, 'native_stop_uncertain')

    async def steer(self, job_id, text):
        async with self._lock(job_id):
            try:
                job, route = self._job_route(job_id)
                self._validation(job)
                if not isinstance(text, str) or not text.strip():
                    raise ValueError('steer_text_required')
                intent, state = self._get('hermes:intent:' + job_id), self._get('hermes:state:' + job_id) or {}
                if not intent or not state.get('native_id'):
                    raise ValueError('native_identity_missing')
                self._same_route(route, intent)
                identity = _hash([job_id, text])
                key = 'hermes:steer:' + identity
                with self.store.transaction():
                    previous = self._get(key)
                    if previous:
                        return previous['receipt']
                    receipt = {'status': 'uncertain', 'job_id': job_id, 'error': 'steer_receipt_missing'}
                    self._set(key, {'text': text, 'native_id': state['native_id'], 'created_at': time.time(), 'receipt': receipt})
                if intent['durable']:
                    receipt = {'status': 'unsupported', 'job_id': job_id, 'error': 'kanban_live_steer_unavailable', 'guidance_reference': key}
                else:
                    self._validation(job)
                    status, payload = await self._http(route, 'POST', '/v1/runs/' + quote(state['native_id'], safe='') + '/steer', {'input': text})
                    if status == 200 and payload.get('accepted') is True:
                        receipt = {'status': 'accepted', 'job_id': job_id, 'native_id': state['native_id']}
                    else:
                        receipt = {'status': 'uncertain', 'job_id': job_id, 'error': 'steer_not_confirmed'}
                with self.store.transaction():
                    record = self._get(key)
                    record['receipt'] = receipt
                    self._set(key, record)
                return receipt
            except ValueError as exc:
                return {'status': 'rejected', 'job_id': job_id, 'error': str(exc)}
            except (OSError, asyncio.TimeoutError, aiohttp.ClientError):
                return self._uncertain(job_id, 'native_steer_uncertain')
