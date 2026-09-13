#!/usr/bin/env python3
"""Explicit zero-turn native Codex protocol probe in new unauthenticated state.

Never invokes turn/start, login, global history, model work or operator config.
"""
import argparse
import asyncio
import hashlib
import json
import os
from pathlib import Path
import signal
import tempfile
import time
import sys

BINARY_SHA256 = '3188814c35471432d4123203e0eb38e5bddc60226e3d7ddf0e59e649ea140022'
METHODS = {'initialize', 'config/read', 'mcpServerStatus/list', 'thread/start', 'thread/read', 'thread/resume', 'thread/turns/list'}


def save(path, value):
    raw = json.dumps(value, ensure_ascii=False, indent=2).encode()
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, 'wb') as stream: stream.write(raw)
    return hashlib.sha256(raw).hexdigest()


def birth(pid):
    return (Path('/proc') / str(pid) / 'stat').read_text().rsplit(')', 1)[1].split()[19]


async def probe(args):
    binary = Path(args.binary).resolve(strict=True)
    if hashlib.sha256(binary.read_bytes()).hexdigest() != BINARY_SHA256:
        raise ValueError('binary_hash_mismatch')
    root = Path(tempfile.mkdtemp(prefix='native-zero-turn-', dir=args.evidence_root))
    root.chmod(0o700)
    home = root / 'home'; home.mkdir(mode=0o700)
    workspace = Path(tempfile.mkdtemp(prefix='gtd-codex-zero-turn-')); workspace.chmod(0o700)
    # Avoid loading ancestor AGENTS files belonging to the operator.
    if any((parent / 'AGENTS.md').exists() for parent in workspace.parents):
        raise ValueError('workspace_ancestor_instructions_present')
    base = 'Synthetic protocol probe. No user work and no model turn is authorized.'
    developer = 'Do not contact services, read outside this synthetic workspace, or publish anything.'
    instructions = workspace / 'AGENTS.md'
    instructions.write_text(base + '\n' + developer + '\n'); instructions.chmod(0o600)
    config = '\n'.join([
        'model = "gpt-6-astra"', 'model_provider = "openai"', 'model_reasoning_effort = "low"',
        'approval_policy = "never"', 'sandbox_mode = "workspace-write"', 'web_search = "disabled"',
        'instructions = ' + json.dumps(base), 'developer_instructions = ' + json.dumps(developer),
        '[features]', 'multi_agent = false', '[analytics]', 'enabled = false',
        '[sandbox_workspace_write]', 'writable_roots = [' + json.dumps(str(workspace)) + ']',
        'network_access = false', 'exclude_tmpdir_env_var = true', 'exclude_slash_tmp = true', ''])
    overlay = {}
    marker = root / 'forbidden-capability-started'
    if args.overlay:
        runtime = Path(os.environ['GTD_RUNTIME_ROOT']).resolve(strict=True)
        sys.path.insert(0, str(runtime))
        from gtd_felix.codex import process_overlay, overlay_arguments
        overlay = process_overlay({'model':'gpt-6-astra','provider':'openai','effort':'low','workspace':str(workspace),
            'process_overlay':{'version':1,'disabled_mcp_servers':['synthetic']}})
        config = '\n'.join(['model="synthetic-inherited"','model_reasoning_effort="high"',
            'instructions="PRIVATE_SYNTHETIC_INHERITED"','developer_instructions="PRIVATE_SYNTHETIC_DEVELOPER"',
            '[features]','hooks=true','plugins=true','multi_agent=true',
            '[mcp_servers.synthetic]','command="/usr/bin/touch"','args=['+json.dumps(str(marker))+']',
            '[plugins."synthetic@example"]','enabled=true',
            '[[hooks.SessionStart]]','[[hooks.SessionStart.hooks]]','type="command"',
            'command='+json.dumps('/usr/bin/touch '+str(marker)),''])
    path = home / 'config.toml'; path.write_text(config); path.chmod(0o600)
    env = {'HOME': str(home), 'CODEX_HOME': str(home), 'PATH': '/usr/local/bin:/usr/bin:/bin', 'LANG': 'C.UTF-8'}
    receipt = {'status': 'PARTIAL', 'binary': str(binary), 'binary_sha256': BINARY_SHA256,
        'evidence_dir': str(root), 'workspace': str(workspace), 'codex_home': str(home),
        'config_sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'auth_copied': False,
        'model_turns_requested': 0, 'overlay_enabled': args.overlay, 'overlay_sha256': hashlib.sha256(json.dumps(overlay,sort_keys=True).encode()).hexdigest(), 'methods': [], 'artifacts': {}, 'started_at': time.time()}
    process = None; stderr_task = None; events = []; pending = {}; counter = 0
    async def stderr_read():
        data = await process.stderr.read(1024*1024)
        return data.decode(errors='replace')
    async def request(method, params):
        nonlocal counter
        if method not in METHODS: raise ValueError('method_not_allowed')
        counter += 1
        process.stdin.write((json.dumps({'id': counter, 'method': method, 'params': params}) + '\n').encode())
        await process.stdin.drain()
        receipt['methods'].append(method)
        deadline = time.monotonic() + args.timeout
        while True:
            line = await asyncio.wait_for(process.stdout.readline(), max(.01, deadline-time.monotonic()))
            if not line: raise ValueError('native_transport_closed')
            response = json.loads(line)
            if response.get('id') == counter and 'method' not in response:
                name = str(counter).zfill(2) + '-' + method.replace('/', '-') + '.json'
                receipt['artifacts'][name] = save(root / name, response)
                if 'error' in response: raise ValueError('native_rpc_rejected:' + method)
                return response['result']
            if 'id' in response and 'method' in response:
                process.stdin.write((json.dumps({'id':response['id'],'error':{'code':-32601,'message':'No authorization or credentials in zero-turn probe'}})+'\n').encode())
                await process.stdin.drain()
                raise ValueError('native_server_request_not_authorized')
            events.append({'method': response.get('method')})
    try:
        process = await asyncio.create_subprocess_exec(str(binary), 'app-server', '--strict-config', '--stdio', *(overlay_arguments(overlay) if args.overlay else []),
            cwd=workspace, env=env, stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE, start_new_session=True, limit=8*1024*1024)
        receipt['process'] = {'pid':process.pid, 'birth':birth(process.pid), 'pgid':os.getpgid(process.pid)}
        stderr_task = asyncio.create_task(stderr_read())
        await request('initialize', {'clientInfo':{'name':'gtd-zero-turn-probe','version':'1'}})
        process.stdin.write(b'{"method":"initialized","params":{}}\n'); await process.stdin.drain()
        effective = await request('config/read', {'cwd':str(workspace),'includeLayers':False})
        if args.overlay:
            from gtd_felix.codex import CodexAdapter
            route={'model':'gpt-6-astra','provider':'openai','effort':'low','workspace':str(workspace),
                'base_instructions':base,'developer_instructions':developer,
                'instruction_sources':{str(instructions):hashlib.sha256(instructions.read_bytes()).hexdigest()},
                'process_overlay':{'version':1,'disabled_mcp_servers':['synthetic']}}
            CodexAdapter._effective_config(object.__new__(CodexAdapter),route,effective)
            receipt['overlay_config'] = 'VERIFIED'
        mcp = await request('mcpServerStatus/list', {'limit':100})
        if args.overlay:
            from gtd_felix.codex import verify_mcp_inventory
            verify_mcp_inventory(mcp,route)
        elif mcp.get('data') != [] or mcp.get('nextCursor'): raise ValueError('unexpected_mcp_inventory')
        receipt['discovery'] = 'OBSERVED'
        if args.thread:
            params = {'model':'gpt-6-astra','modelProvider':'openai','cwd':str(workspace),
                'approvalPolicy':'never','sandbox':'workspace-write','baseInstructions':base,'developerInstructions':developer,
                'config':{'model_reasoning_effort':'low','sandbox_workspace_write':{'writable_roots':[str(workspace)],
                    'network_access':False,'exclude_tmpdir_env_var':True,'exclude_slash_tmp':True}}}
            started = await request('thread/start', params)
            thread = started.get('thread', {})
            if not thread.get('id') or thread.get('turns'): raise ValueError('new_thread_not_empty')
            receipt['thread_id'] = thread['id']
            if args.overlay:
                CodexAdapter._thread_verified(object.__new__(CodexAdapter),route,started)
                scoped = await request('mcpServerStatus/list', {'threadId':thread['id'],'limit':100})
                verify_mcp_inventory(scoped,route)
                receipt['thread_overlay'] = 'OBSERVED_ZERO_TURNS'
                receipt['status'] = 'COLLECTED'
                return receipt
            read = await request('thread/read', {'threadId':thread['id'],'includeTurns':False})
            if read['thread']['id'] != thread['id'] or read['thread'].get('turns'): raise ValueError('read_thread_not_empty')
            resumed = await request('thread/resume', {**params,'threadId':thread['id']})
            if resumed['thread']['id'] != thread['id'] or resumed['thread'].get('turns'): raise ValueError('resume_thread_not_empty')
            turns = await request('thread/turns/list', {'threadId':thread['id'],'itemsView':'full','limit':2})
            if turns.get('data') != [] or turns.get('nextCursor'): raise ValueError('thread_turns_not_empty')
            receipt['thread_probe'] = 'OBSERVED_ZERO_TURNS'
        else: receipt['thread_probe'] = 'NOT_RUN'
        receipt['status'] = 'COLLECTED'
    except (ValueError, OSError, asyncio.TimeoutError, KeyError) as error:
        receipt['error'] = str(error) if isinstance(error, ValueError) else type(error).__name__
    finally:
        if process:
            if process.returncode is None:
                identity = receipt['process']
                if birth(process.pid) != identity['birth'] or os.getpgid(process.pid) != identity['pgid']:
                    raise ValueError('owned_process_identity_changed')
                os.killpg(process.pid, signal.SIGTERM)
                try: await asyncio.wait_for(process.wait(), 3)
                except asyncio.TimeoutError:
                    if birth(process.pid) != identity['birth']: raise ValueError('owned_process_identity_changed')
                    os.killpg(process.pid, signal.SIGKILL); await process.wait()
            receipt['process'].update(returncode=process.returncode, pid_absent=not Path('/proc',str(process.pid)).exists())
        if stderr_task:
            try: stderr = await asyncio.wait_for(stderr_task, 3)
            except asyncio.TimeoutError: stderr = 'stderr capture timeout'
            receipt['artifacts']['native-stderr.json'] = save(root/'native-stderr.json', {'stderr':stderr})
        receipt['artifacts']['events.json'] = save(root/'events.json', events)
        receipt['forbidden_capability_marker_absent'] = not marker.exists()
        receipt['config_unchanged'] = hashlib.sha256(path.read_bytes()).hexdigest() == receipt['config_sha256']
        receipt['auth_absent'] = not (home/'auth.json').exists()
        if marker.exists(): receipt.update(status='FAILED',error='inherited_capability_executed')
        if args.overlay and not receipt['config_unchanged']:
            receipt.update(status='FAILED',error='native_config_changed')
        receipt['finished_at'] = time.time()
        checksum = save(root/'receipt.json', receipt)
        print(json.dumps({'evidence_dir':str(root),'receipt_sha256':checksum,'status':receipt['status'],
            'error':receipt.get('error'),'process':receipt.get('process'),'methods':receipt['methods'],
            'model_turns_requested':0}, ensure_ascii=False))
    return receipt


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--execute',action='store_true')
    parser.add_argument('--overlay',action='store_true',help='Verify fixed process overlay against synthetic inherited capabilities.')
    parser.add_argument('--thread',action='store_true',help='Attempt one empty thread; never create a turn.')
    parser.add_argument('--binary',default='/home/felix/.local/bin/codex')
    parser.add_argument('--evidence-root',default='/home/felix/.local/state/gtd-felix/p4-probe')
    parser.add_argument('--timeout',type=float,default=15)
    args=parser.parse_args()
    if not args.execute: raise SystemExit('NOT_RUN: --execute required')
    if not 0 < args.timeout <= 30: raise SystemExit('invalid timeout')
    asyncio.run(probe(args))


if __name__=='__main__': main()
