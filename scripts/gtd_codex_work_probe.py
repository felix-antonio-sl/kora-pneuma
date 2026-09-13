#!/usr/bin/env python3
"""Explicit synthetic Codex campaign. Default discovery; --work permits one reservation.

--recover only stops/reads the existing job. Never reads auth.json or copies auth.
The campaign config and runtime are pinned. Native terminality, technical checks,
material integration and principal assessment remain distinct.
"""
import argparse
import ast
import asyncio
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import signal
import stat
import sys
import time
import uuid

INSTRUCTIONS = ('Synthetic bounded Python task. Only edit clamp.py in this workspace.\n'
    'Preserve test_clamp.py, AGENTS.md and concurrent_sentinel.txt byte for byte.\n'
    'No imports in clamp.py, external effects, new files or delegation. Running the existing Python unittest command and its test imports is authorized. Return a native final report.\n')
INITIAL = 'def clamp(value, lower, upper):\n    return min(lower, max(upper, value))\n'
TESTS = '''import unittest
from clamp import clamp
class ClampTests(unittest.TestCase):
    def test_inside(self): self.assertEqual(clamp(5, 0, 10), 5)
    def test_low(self): self.assertEqual(clamp(-3, 0, 10), 0)
    def test_high(self): self.assertEqual(clamp(13, 0, 10), 10)
    def test_equal(self): self.assertEqual(clamp(4, 4, 4), 4)
    def test_negative(self): self.assertEqual(clamp(-3, -5, -1), -3)
    def test_reversed(self):
        with self.assertRaises(ValueError): clamp(0, 10, 1)
'''
SENTINEL = 'Concurrent contribution owned by another author: preserve exactly.\n'
SEED = {'clamp.py': INITIAL, 'test_clamp.py': TESTS, 'AGENTS.md': INSTRUCTIONS,
        'concurrent_sentinel.txt': SENTINEL}
PROTECTED = tuple(name for name in SEED if name != 'clamp.py')


def sha(raw): return hashlib.sha256(raw).hexdigest()
def encode(value): return json.dumps(value, sort_keys=True, ensure_ascii=False, indent=2).encode()
def require(condition, reason):
    if not condition: raise ValueError(reason)


def private_file(path, raw, *, replace=False):
    temporary = path.with_name(path.name + '.' + uuid.uuid4().hex) if replace else path
    fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, 'wb') as stream:
        stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    if replace: os.replace(temporary, path)
    directory = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
    try: os.fsync(directory)
    finally: os.close(directory)


def file_hash(path):
    info = path.lstat()
    require(stat.S_ISREG(info.st_mode) and info.st_uid == os.getuid() and info.st_nlink == 1
            and info.st_size <= 4 * 1024 * 1024, 'unsafe_hash_target')
    return sha(path.read_bytes())


def instruction_manifest(workspace, global_source=None):
    manifest = {str(Path(workspace) / 'AGENTS.md'): sha(INSTRUCTIONS.encode())}
    if global_source is not None: manifest.update(global_source)
    return manifest


def validate_config(config):
    require(set(config) - {'reviewed_global_instructions'} == {'case_dir', 'runtime_root', 'actors', 'codex', 'campaign', 'reservation'}, 'config_fields_invalid')
    case, runtime = Path(config['case_dir']), Path(config['runtime_root'])
    for path in (case, runtime):
        require(path.is_absolute() and path.resolve() == path and '..' not in path.parts, 'canonical_path_required')
    require(runtime.is_dir() and case.parent.is_dir(), 'parent_or_runtime_missing')
    require(set(config['actors']) == {'owner', 'principal', 'executor'}
            and all(isinstance(a, str) and a for a in config['actors'].values())
            and len(set(config['actors'].values())) == 3, 'actors_invalid')
    native = config['codex']
    require(set(native) <= {'binary', 'binary_sha256', 'codex_home', 'routes', 'request_timeout_seconds', 'shutdown_grace_seconds'},
            'native_config_fields_invalid')
    require(set(native['routes']) == {'worker'}, 'one_worker_route_required')
    route = native['routes']['worker']
    require(set(route) == {'host', 'profile', 'workspace', 'model', 'provider', 'effort', 'base_instructions',
                           'developer_instructions', 'instruction_sources', 'process_overlay'}, 'route_fields_invalid')
    require(route['host'] == 'local' and route['model'] == 'gpt-6-astra' and route['provider'] == 'openai'
            and route['effort'] == 'low', 'explicit_local_astra_low_required')
    global_source = config.get('reviewed_global_instructions', {})
    require(isinstance(global_source, dict) and (not global_source or set(global_source) == {str(Path(native['codex_home'])/'AGENTS.md')}),
            'global_instruction_path_not_authorized')
    for path, digest in global_source.items():
        require(isinstance(digest, str) and len(digest) == 64 and file_hash(Path(path)) == digest, 'global_instruction_hash_mismatch')
    require(not (Path(native['codex_home'])/'AGENTS.override.md').exists(), 'unapproved_instruction_override')
    require(route['workspace'] == str(case/'workspace') and route['instruction_sources'] == instruction_manifest(case/'workspace', global_source),
            'synthetic_workspace_manifest_required')
    require(Path(native['codex_home']).is_absolute() and Path(native['codex_home']).resolve() == Path(native['codex_home']),
            'canonical_native_home_required')
    require(not Path(native['codex_home']).is_relative_to(case), 'native_home_separate_required')
    campaign, reservation = config['campaign'], config['reservation']
    require(set(campaign) == {'id', 'period_start', 'period_seconds', 'max_cost_usd', 'max_runtime_seconds'}, 'campaign_fields_invalid')
    require(isinstance(campaign['id'], str) and campaign['id'], 'campaign_id_required')
    start = datetime.fromisoformat(campaign['period_start'])
    require(start.tzinfo is not None, 'campaign_timezone_required')
    require(set(reservation) == {'max_cost_usd', 'max_runtime_seconds'}, 'reservation_fields_invalid')
    for values in (campaign, reservation):
        for key in ('max_cost_usd', 'max_runtime_seconds'):
            require(type(values[key]) in (int, float) and math.isfinite(values[key]) and values[key] > 0, 'budget_invalid')
    require(type(campaign['period_seconds']) in (int, float) and 0 < campaign['period_seconds'] <= 86400,
            'campaign_window_invalid')
    require(0 < reservation['max_runtime_seconds'] <= 600 and reservation['max_runtime_seconds'] <= campaign['max_runtime_seconds']
            and reservation['max_cost_usd'] <= campaign['max_cost_usd'], 'reservation_exceeds_campaign')
    return case, runtime


def source_manifest(runtime):
    return {str(path.relative_to(runtime)): file_hash(path) for path in sorted((runtime/'gtd_felix').glob('*.py'))}


def safe_function(path):
    require(path.stat().st_size <= 65536 and not path.is_symlink(), 'target_size_or_link_invalid')
    tree = ast.parse(path.read_text())
    require(len(tree.body) == 1 and isinstance(tree.body[0], ast.FunctionDef), 'target_function_only')
    function = tree.body[0]
    require(function.name == 'clamp' and not function.decorator_list and function.returns is None
            and [a.arg for a in function.args.args] == ['value', 'lower', 'upper']
            and all(arg.annotation is None for arg in function.args.args)
            and not function.args.posonlyargs and not function.args.kwonlyargs and not function.args.defaults
            and function.args.vararg is None and function.args.kwarg is None, 'target_signature_invalid')
    allowed = (ast.Module, ast.FunctionDef, ast.arguments, ast.arg, ast.Return, ast.If, ast.IfExp,
               ast.Compare, ast.Lt, ast.LtE, ast.Gt, ast.GtE, ast.Eq, ast.NotEq, ast.Name, ast.Load,
               ast.Call, ast.Raise, ast.Constant, ast.Expr, ast.UnaryOp, ast.USub, ast.UAdd,
               ast.BoolOp, ast.And, ast.Or)
    for node in ast.walk(tree):
        require(isinstance(node, allowed), 'target_ast_outside_contract')
        if isinstance(node, ast.Name): require(node.id in {'value', 'lower', 'upper', 'min', 'max', 'ValueError'}, 'target_name_invalid')
        if isinstance(node, ast.Call): require(isinstance(node.func, ast.Name) and node.func.id in {'min', 'max', 'ValueError'}
                                              and not node.keywords, 'target_call_invalid')
        if isinstance(node, ast.Constant): require(type(node.value) in (int, float, str, type(None))
                                                  and len(str(node.value)) <= 4096, 'target_constant_invalid')


def workspace_hashes(workspace):
    require(set(path.name for path in workspace.iterdir()) == set(SEED), 'unexpected_workspace_files')
    return {name: file_hash(workspace/name) for name in SEED}


def process_birth(pid): return Path('/proc', str(pid), 'stat').read_text().rsplit(')', 1)[1].split()[19]


async def check_workspace(case, label, job_id=None):
    workspace = case/'workspace'
    hashes = workspace_hashes(workspace)
    require(all(hashes[name] == sha(SEED[name].encode()) for name in PROTECTED), 'protected_workspace_file_changed')
    safe_function(workspace/'clamp.py')
    # Trusted harness imports only the AST-checked target and immutable test module.
    code = 'import sys,unittest;sys.path.insert(0,sys.argv[1]);s=unittest.defaultTestLoader.discover(sys.argv[1],pattern="test_clamp.py");r=unittest.TextTestRunner().run(s);sys.exit(not r.wasSuccessful())'
    process = await asyncio.create_subprocess_exec(sys.executable, '-I', '-B', '-c', code, str(workspace),
        cwd=workspace, env={'HOME':str(case), 'PATH':'/usr/bin:/bin', 'LANG':'C.UTF-8'},
        stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE, start_new_session=True)
    identity = {'pid':process.pid,'birth':process_birth(process.pid),'pgid':os.getpgid(process.pid)}
    try:
        stdout, stderr = await asyncio.wait_for(process.communicate(), 10)
    except asyncio.TimeoutError:
        require(process_birth(process.pid) == identity['birth'] and os.getpgid(process.pid) == process.pid, 'test_process_identity_changed')
        os.killpg(process.pid, signal.SIGKILL)
        stdout, stderr = await process.communicate()
    require(workspace_hashes(workspace) == hashes, 'tests_changed_workspace')
    report = {'label':label,'job_id':job_id,'exit_code':process.returncode,'files':hashes,'stdout_sha256':sha(stdout),'stderr_sha256':sha(stderr),
              'stdout_bytes':len(stdout),'stderr_bytes':len(stderr),'process':{**identity,'pid_absent':not Path('/proc',str(process.pid)).exists()}}
    private_file(case/(label+'-tests-'+uuid.uuid4().hex+'.json'),encode(report))
    return report


async def run(config_path, *, work=False, recover=False):
    require(not(work and recover), 'work_and_recover_exclusive')
    config_path = Path(config_path)
    require(config_path.is_absolute() and config_path.resolve() == config_path and config_path.name != 'auth.json',
            'canonical_probe_config_required')
    info = config_path.lstat()
    require(stat.S_ISREG(info.st_mode) and info.st_uid == os.getuid() and info.st_mode & 0o077 == 0
            and info.st_nlink == 1 and info.st_size <= 65536, 'private_config_required')
    raw = config_path.read_bytes(); config = json.loads(raw)
    case, runtime = validate_config(config)
    sys.path.insert(0, str(runtime))
    from gtd_felix.service import GTDService
    from gtd_felix.control import ExecutionControl
    from gtd_felix.codex import CodexAdapter, process_overlay
    from gtd_felix.adapters import AdapterRouter
    from gtd_felix.orchestration import OrchestrationWorker
    require(Path(sys.modules['gtd_felix.codex'].__file__).resolve().is_relative_to(runtime), 'runtime_import_mismatch')
    require(process_overlay(config['codex']['routes']['worker']), 'process_overlay_required')
    native_config = Path(config['codex']['codex_home'])/'config.toml'
    native_before = file_hash(native_config)
    if not case.exists():
        require(not recover, 'recover_case_missing')
        case.mkdir(mode=0o700)
        state = {'config_sha256':sha(raw),'runtime':source_manifest(runtime),'script_sha256':file_hash(Path(__file__)),
                 'native_config_sha256':native_before,'phase':'prepared','job_id':None}
        private_file(case/'state.json',encode(state))
        (case/'workspace').mkdir(mode=0o700)
        for name, content in SEED.items(): private_file(case/'workspace'/name, content.encode())
    require(case.is_dir() and case.stat().st_uid == os.getuid() and case.stat().st_mode & 0o077 == 0, 'private_case_required')
    lock = os.open(case/'runner.lock',os.O_WRONLY|os.O_CREAT|os.O_NOFOLLOW,0o600)
    try: fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except OSError:
        os.close(lock);raise ValueError('case_already_running')
    service = router = adapter = None
    result = {'status':'PARTIAL','mode':'recover' if recover else ('work' if work else 'discovery'),
              'campaign_id':config['campaign']['id'],'config_sha256':sha(raw),'case_dir':str(case),
              'work_submissions_requested':0,'principal_assessment':'NOT_RUN','workspace_integration':'not_performed'}
    try:
        state=json.loads((case/'state.json').read_text())
        require(state['config_sha256']==sha(raw) and state['runtime']==source_manifest(runtime)
                and state['script_sha256']==file_hash(Path(__file__)), 'case_binding_changed')
        result['native_config_matches_initial']=state['native_config_sha256']==native_before
        if not recover: require(result['native_config_matches_initial'], 'native_config_drift')
        campaign=config['campaign'];reservation=config['reservation'];actors=config['actors']
        budget={key:campaign[key] for key in ('period_start','period_seconds','max_cost_usd','max_runtime_seconds')}
        budget.update(recovery_cost_usd=0,recovery_runtime_seconds=0,max_active=1,
                      max_job_runtime_seconds=reservation['max_runtime_seconds'],max_retries=0,max_descendants=0)
        service=GTDService(case/'data',owner_actor=actors['owner'],principal_actor=actors['principal'],executor_actors=[actors['executor']])
        control=ExecutionControl(service,budget);adapter=CodexAdapter(control,config['codex'])
        router=AdapterRouter(control,None,adapter,{'providers':{'worker':'codex'}})
        prior=control._load()['operations'].get('codex-work-probe:reserve',{}).get('receipt',{})
        job_id=state.get('job_id') or prior.get('job_id')
        if job_id:
            state['job_id']=job_id
            require(work or recover, 'existing_job_requires_recover_or_work')
        elif recover:
            result.update(status='NOT_RUN',reason='no_existing_reservation');return result
        else:
            discovery=await router.discover('worker');result['discovery']=discovery
            require(discovery.get('status')=='ready','discovery_unavailable')
            require(file_hash(native_config)==native_before,'native_config_changed_during_discovery')
            if not work:
                result['status']='DISCOVERY_READY';return result
            before=await check_workspace(case,'before')
            require(before['exit_code']!=0,'synthetic_baseline_not_red')
            state['before']=before
            capture=service.capture(actors['owner'],'codex-work-probe:capture','Correct synthetic clamp within its workspace')['item']
            clarified=service.execute(actors['owner'],{'operation_id':'codex-work-probe:clarify','action':'clarify',
                'item_id':capture['id'],'expected_version':capture['version'],'fields':{'kind':'action','commitment':'committed',
                    'completion_criteria':'Inclusive clamp, ValueError on reversed bounds, six immutable tests pass; preserve all other files.'}})
            require(clarified['status']=='applied','owner_contract_rejected');item=clarified['item']
            grant=service.execute(actors['owner'],{'operation_id':'codex-work-probe:mandate','action':'grant_mandate',
                'item_id':item['id'],'expected_version':item['version'],'fields':{'scope_item_id':item['id'],
                    'capabilities':['prepare_private'],'actors':[actors['executor']],
                    'completion_criteria':item['completion_criteria']}})
            require(grant['status']=='applied','owner_mandate_rejected')
            route=config['codex']['routes']['worker']
            registered=control.register_bot(actors['owner'],'codex-work-probe:bot',{'id':'worker','actor':actors['executor'],
                'state':'available','source_urn':'urn:synthetic:codex-clamp-probe','host':route['host'],'profile':route['profile'],
                'capabilities':['prepare_private'],'probe_evidence':discovery})
            require(registered['status']=='applied','worker_registration_rejected')
            reserved=control.reserve(actors['principal'],'codex-work-probe:reserve',{'item_id':item['id'],
                'expected_version':service.get_item(item['id'])['version'],'mandate_id':grant['mandate']['id'],
                'capability':'prepare_private','bot_id':'worker','purpose':'Correct clamp and verify synthetic cases',
                'scope':str(case/'workspace'),**reservation,'max_retries':0,'max_descendants':0})
            require(reserved['status']=='reserved','reservation_rejected')
            job_id=reserved['job_id'];state.update(job_id=job_id,phase='reserved')
            private_file(case/'state.json',encode(state),replace=True)
            prompt=('Implement clamp(value, lower, upper): inclusive bounds; raise ValueError when lower > upper. '
                'Only edit clamp.py. Use one undecorated function, min/max or comparisons/return/raise ValueError; '
                'no imports, attributes, loops, recursion, annotations, new files or external effects. '
                'Preserve AGENTS.md, test_clamp.py and concurrent_sentinel.txt byte for byte. '
                'Run python3 -B -m unittest test_clamp.py in the authorized workspace. '
                'Report actual changes and tests in your native final response; do not claim principal assessment. '
                'Workspace: '+str(case/'workspace')+'. Job: '+job_id)
            result['work_submissions_requested']=1
            await router.submit(job_id,prompt,durable=True)
        result['job_id']=job_id
        if recover: await router.stop(job_id)
        deadline=time.monotonic()+(min(15,reservation['max_runtime_seconds']) if recover else reservation['max_runtime_seconds']+10)
        response=await router.reconcile(job_id)
        while not control.get_job(job_id)['terminal'] and not control.get_job(job_id)['stop_requested'] and time.monotonic()<deadline:
            await asyncio.sleep(.2)
            response=await router.reconcile(job_id)
        if not control.get_job(job_id)['terminal']:
            await router.stop(job_id)
            for _ in range(10):
                response=await router.reconcile(job_id)
                if control.get_job(job_id)['terminal']: break
                await asyncio.sleep(.2)
        job=control.get_job(job_id);result.update(terminal=job['terminal'],native=job.get('native'),
            status='NATIVE_TERMINAL' if job['terminal'] else 'UNRESOLVED_NATIVE_JOB',budget=control.budget(),
            cost_semantics='technical_reservation_not_measured_billing')
        if recover: return result
        require(job['terminal'] and job['observations'][-1]['native_status']=='completed','native_success_unconfirmed')
        after=await check_workspace(case,'after',job_id);result['technical_checks']=after
        require(after['exit_code']==0 and after['files']['clamp.py']!=sha(INITIAL.encode()),'workspace_criteria_failed')
        require(file_hash(native_config)==native_before,'native_config_changed_during_work')
        worker=OrchestrationWorker(service,control,router,{})
        output=worker._output(response)
        require(output and json.loads(output).get('messages'),'native_final_missing')
        integrated=worker._integrate(job_id,response,durable=True)
        require(integrated.get('status')=='integrated','material_not_integrated')
        result.update(status='TECHNICAL_CRITERIA_PASS',material_integration=integrated['status'],
                      item_status=service.get_item(job['item_id'])['status'],
                      materials=[{'id':m['id'],'version':m['version']} for m in service.materials(job['item_id'])])
        state['phase']='technical_verified'
        return result
    except (ValueError,OSError,KeyError,SyntaxError,asyncio.TimeoutError) as error:
        result.update(status='BLOCKED',reason=str(error) if isinstance(error,ValueError) else type(error).__name__)
        return result
    finally:
        if router:
            pending_id=state.get('job_id')
            if pending_id and not control.get_job(pending_id)['terminal']:
                try:
                    await asyncio.wait_for(router.stop(pending_id),5)
                    await asyncio.wait_for(router.reconcile(pending_id),5)
                except (ValueError,OSError,asyncio.TimeoutError): pass
            try: await router.close()
            except (ValueError,OSError,asyncio.TimeoutError):
                result.update(status='BLOCKED',reason='transport_close_unconfirmed')
        result['native_config_before_sha256']=native_before
        try: result['native_config_after_sha256']=file_hash(native_config)
        except (ValueError,OSError): result['native_config_after_sha256']=None
        result['native_config_unchanged']=result['native_config_after_sha256']==native_before
        if not result['native_config_unchanged']: result.update(status='BLOCKED',reason='native_config_changed')
        if service:
            result['control']=control._load()
            result['native_processes']=[json.loads(row[0]) for row in service.store.db.execute(
                "SELECT value FROM metadata WHERE key LIKE 'codex:process:%'")]
            for process in result['native_processes']:
                process['pid_absent']=not Path('/proc',str(process.get('pid'))).exists()
            result['native_events']=[{'key':row[0],'event':json.loads(row[1])} for row in service.store.db.execute(
                "SELECT key,value FROM metadata WHERE key LIKE 'codex:event:%'")]
            result['native_turn_start_requests']=sum(e['event'].get('direction')=='request' and e['event'].get('method')=='turn/start' for e in result['native_events'])
            if state.get('job_id'):
                result['final_job']=control.get_job(state['job_id'])
                result['terminal']=result['final_job']['terminal']
                native_state=adapter._get('job:'+state['job_id']) or {}
                result['reservation_limits']=config['reservation']
                result['runtime_limit_reached']=bool('turn_requested_at' in native_state and time.time() >=
                    native_state['turn_requested_at']+config['reservation']['max_runtime_seconds'])
            service.close()
        private_file(case/'state.json',encode(state),replace=True)
        name='receipt-'+uuid.uuid4().hex+'.json';data=encode(result);private_file(case/name,data)
        fcntl.flock(lock,fcntl.LOCK_UN);os.close(lock)
        print(json.dumps({'status':result['status'],'job_id':result.get('job_id'),'case_dir':str(case),
            'receipt':name,'receipt_sha256':sha(data),'terminal':result.get('terminal'),
            'native_config_unchanged':result['native_config_unchanged']}))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config',required=True)
    modes=parser.add_mutually_exclusive_group();modes.add_argument('--work',action='store_true');modes.add_argument('--recover',action='store_true')
    args=parser.parse_args()
    try: result=asyncio.run(run(args.config,work=args.work,recover=args.recover))
    except Exception as error:
        print(json.dumps({'status':'BLOCKED','reason':type(error).__name__}));return 2
    return 0 if result['status'] in {'DISCOVERY_READY','TECHNICAL_CRITERIA_PASS','NATIVE_TERMINAL'} else 2


if __name__=='__main__': raise SystemExit(main())
