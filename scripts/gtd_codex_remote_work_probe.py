#!/usr/bin/env python3
"""Synthetic remote workspace probe; default description performs zero SSH/inference.

--preflight validates the prepared workspace and discovers the real adapter (zero
turns). --work reserves once and deliberately reconnects the SSH channel.
--recover reads/stops only that durable job, never submits or renews its deadline.
Root prepares the four SEED files remotely. No auth files are read or copied.
Remote file, local evidence copy, native GTD report and principal assessment are
four distinct planes. Remote SSH trust uses the operator's explicit SSH alias.
"""
import argparse
import asyncio
import base64
from datetime import datetime
import fcntl
import importlib.util
import inspect
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import shlex
import stat
import sys
import time
import uuid

_LOCAL = Path(__file__).with_name('gtd_codex_work_probe.py')
_spec = importlib.util.spec_from_file_location('remote_probe_local_contract', _LOCAL)
contract = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(contract)
SEED, PROTECTED = contract.SEED, contract.PROTECTED
sha, encode, require = contract.sha, contract.encode, contract.require
private_file, file_hash = contract.private_file, contract.file_hash
SSH = '/usr/bin/ssh'

# Fixed program: no caller-selected command/path list, no arbitrary remote writes.
# The AST gate is exactly the local probe's existing gate, not a weaker copy.
HELPER = '''import ast,base64,hashlib,json,os,stat,sys,subprocess,signal,time,types
from pathlib import Path
def require(v,e):
 if not v: raise ValueError(e)
''' + inspect.getsource(contract.safe_function) + '\nSEED = ' + repr(SEED) + r'''
q=json.load(sys.stdin);route=q['route'];r=route['remote']
require(q['op'] in ('snapshot','test'),'operation_invalid')
require(os.getuid()==r['uid'] and os.uname().nodename==r['hostname'],'remote_host_changed')
def directory(value):
 p=Path(value);s=p.lstat()
 require(p.is_absolute() and str(p.resolve(strict=True))==value and stat.S_ISDIR(s.st_mode) and s.st_uid==r['uid'],'remote_directory_changed')
 return p
def read(p,maximum):
 require(str(p.resolve(strict=True))==str(p),'remote_file_path_changed')
 fd=os.open(p,os.O_RDONLY|os.O_NOFOLLOW)
 try:
  s=os.fstat(fd);require(stat.S_ISREG(s.st_mode) and s.st_uid==r['uid'] and s.st_nlink==1 and s.st_size<=maximum,'remote_file_unsafe')
  with os.fdopen(fd,'rb',closefd=False) as f:raw=f.read(maximum+1)
  after=os.fstat(fd)
  require(len(raw)<=maximum and (after.st_size,after.st_mtime_ns,after.st_ctime_ns)==(s.st_size,s.st_mtime_ns,s.st_ctime_ns),'remote_file_changed_during_read')
  require(p.lstat().st_ino==s.st_ino,'remote_file_replaced_during_read')
  return raw
 finally:os.close(fd)
root=directory(route['workspace']);home=directory(r['codex_home']);private=directory(r['private_root'])
require(stat.S_IMODE(private.stat().st_mode)==0o700,'remote_private_root_changed')
binary=read(Path(r['binary']),256*1024*1024)
require(hashlib.sha256(binary).hexdigest()==r['binary_sha256'],'remote_binary_changed')
config=read(home/'config.toml',65536)
require(hashlib.sha256(config).hexdigest()==q['native_config_sha256'],'native_config_changed')
require(not (home/'AGENTS.override.md').exists() and not (home/'AGENTS.override.md').is_symlink(),'remote_instruction_override')
global_path=home/'AGENTS.md'
if global_path.exists() or global_path.is_symlink():
 require(str(global_path) in route['instruction_sources'],'unapproved_global_instructions')
 require(hashlib.sha256(read(global_path,65536)).hexdigest()==route['instruction_sources'][str(global_path)],'global_instruction_changed')
else:require(str(global_path) not in route['instruction_sources'],'global_instruction_missing')
def snapshot():
 require(set(p.name for p in root.iterdir())==set(SEED),'unexpected_workspace_files')
 return {name:read(root/name,65536) for name in SEED}
files=snapshot()
require(all(files[n]==SEED[n].encode() for n in SEED if n!='clamp.py'),'protected_workspace_file_changed')
result={'hostname':r['hostname'],'uid':r['uid'],'workspace':str(root),
 'native_config_sha256':hashlib.sha256(config).hexdigest(),
 'files':{n:{'sha256':hashlib.sha256(raw).hexdigest(),'base64':base64.b64encode(raw).decode(),'size':len(raw)} for n,raw in files.items()}}
if q['op']=='test':
 require(q['expected_hashes']=={n:hashlib.sha256(raw).hexdigest() for n,raw in files.items()},'snapshot_changed_before_test')
 class Captured:
  def stat(self):return types.SimpleNamespace(st_size=len(files['clamp.py']))
  def is_symlink(self):return False
  def read_text(self):return files['clamp.py'].decode()
 safe_function(Captured())
 # Run the captured, hash-verified immutable bytes, not mutable imports from disk.
 code="import sys,json,types,unittest;v=json.load(sys.stdin);m=types.ModuleType('clamp');exec(compile(v['clamp.py'],'clamp.py','exec'),m.__dict__);sys.modules['clamp']=m;t=types.ModuleType('test_clamp');exec(compile(v['test_clamp.py'],'test_clamp.py','exec'),t.__dict__);r=unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromModule(t));sys.exit(not r.wasSuccessful())"
 p=subprocess.Popen(['/usr/bin/python3','-I','-B','-c',code],cwd=root,env={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8'},stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,start_new_session=True)
 birth=Path('/proc',str(p.pid),'stat').read_text().rsplit(')',1)[1].split()[19]
 try:out,err=p.communicate(json.dumps({n:files[n].decode() for n in ('clamp.py','test_clamp.py')}).encode(),timeout=10)
 except subprocess.TimeoutExpired:
  require(Path('/proc',str(p.pid),'stat').read_text().rsplit(')',1)[1].split()[19]==birth,'test_process_identity_changed')
  os.killpg(p.pid,signal.SIGKILL);out,err=p.communicate()
 require(snapshot()==files,'workspace_changed_during_test')
 result['test']={'exit_code':p.returncode,'pid':p.pid,'birth':birth,'pid_absent':not Path('/proc',str(p.pid)).exists(),
  'stdout_sha256':hashlib.sha256(out).hexdigest(),'stderr_sha256':hashlib.sha256(err).hexdigest(),
  'stdout_bytes':len(out),'stderr_bytes':len(err),'location':'remote_captured_immutable_bytes'}
print(json.dumps(result))
'''


def canonical_remote(value):
    return isinstance(value, str) and value.startswith('/') and str(PurePosixPath(value)) == value and '..' not in PurePosixPath(value).parts


def validate_config(config):
    require(set(config) == {'case_dir','runtime_root','runtime_manifest','core_hostname','core_uid','actors','codex',
                            'campaign','reservation','native_config_sha256'}, 'config_fields_invalid')
    case, runtime = Path(config['case_dir']), Path(config['runtime_root'])
    require(all(p.is_absolute() and p.resolve()==p for p in (case,runtime)) and case.parent.is_dir() and runtime.is_dir(), 'local_paths_invalid')
    require(config['core_hostname']==os.uname().nodename and config['core_uid']==os.getuid(), 'core_identity_changed')
    require(config['runtime_manifest']==contract.source_manifest(runtime), 'runtime_manifest_changed')
    require(re.fullmatch('[0-9a-f]{64}',config['native_config_sha256']) is not None,'native_config_pin_required')
    require(set(config['actors'])=={'owner','principal','executor'} and len(set(config['actors'].values()))==3
            and all(isinstance(v,str) and v for v in config['actors'].values()), 'actors_invalid')
    native=config['codex']
    require(set(native)=={'routes','request_timeout_seconds','shutdown_grace_seconds'}, 'native_fields_invalid')
    require(set(native['routes'])=={'worker'}, 'one_worker_route_required')
    route=native['routes']['worker']
    require(set(route)=={'host','profile','workspace','model','provider','effort','base_instructions','developer_instructions',
                        'instruction_sources','process_overlay','remote'}, 'route_fields_invalid')
    require(route['host']=='ssh' and route['model']=='gpt-6-astra' and route['provider']=='openai' and route['effort']=='low', 'explicit_remote_astra_low_required')
    for key in ('profile','base_instructions','developer_instructions'):
        require(isinstance(route[key],str) and route[key], 'route_field_required')
    remote=route['remote']
    require(set(remote)=={'ssh_alias','hostname','uid','binary','binary_sha256','codex_home','private_root','max_runtime_seconds'}, 'remote_fields_invalid')
    require(all(isinstance(remote[k],str) and re.fullmatch('[A-Za-z0-9][A-Za-z0-9_.-]{0,127}',remote[k]) for k in ('ssh_alias','hostname')), 'remote_host_invalid')
    require(type(remote['uid']) is int and remote['uid']>=0, 'remote_uid_invalid')
    require(all(canonical_remote(p) for p in (route['workspace'],remote['binary'],remote['codex_home'],remote['private_root'])), 'remote_path_invalid')
    require(re.fullmatch('[0-9a-f]{64}',remote['binary_sha256']) is not None, 'remote_hash_invalid')
    workspace, home=PurePosixPath(route['workspace']),PurePosixPath(remote['codex_home'])
    require(not workspace.is_relative_to(home) and not home.is_relative_to(workspace), 'remote_home_separate_required')
    sources=route['instruction_sources'];required={str(workspace/'AGENTS.md'):sha(SEED['AGENTS.md'].encode())}
    require(isinstance(sources,dict) and sources.get(str(workspace/'AGENTS.md'))==required[str(workspace/'AGENTS.md')]
            and set(sources)<=set(required)|{str(home/'AGENTS.md')}
            and all(isinstance(v,str) and re.fullmatch('[0-9a-f]{64}',v) for v in sources.values()), 'instruction_manifest_invalid')
    campaign,reservation=config['campaign'],config['reservation']
    require(set(campaign)=={'id','period_start','period_seconds','max_cost_usd','max_runtime_seconds'}, 'campaign_fields_invalid')
    require(isinstance(campaign['id'],str) and campaign['id'] and datetime.fromisoformat(campaign['period_start']).tzinfo is not None, 'campaign_identity_invalid')
    require(set(reservation)=={'max_cost_usd','max_runtime_seconds'}, 'reservation_fields_invalid')
    for values,keys in ((campaign,('period_seconds','max_cost_usd','max_runtime_seconds')),(reservation,tuple(reservation)),
                        (native,('request_timeout_seconds','shutdown_grace_seconds')),(remote,('max_runtime_seconds',))):
        require(all(type(values[k]) in (int,float) and math.isfinite(values[k]) and values[k]>0 for k in keys), 'budget_invalid')
    require(campaign['period_seconds']<=86400 and reservation['max_cost_usd']<=campaign['max_cost_usd']
            and reservation['max_runtime_seconds']<=campaign['max_runtime_seconds']
            and reservation['max_runtime_seconds']==remote['max_runtime_seconds']<=120
            and native['shutdown_grace_seconds']<reservation['max_runtime_seconds']
            and native['request_timeout_seconds']<=30, 'reservation_exceeds_campaign')
    return case,runtime


async def remote_call(config, op, expected_hashes=None):
    from gtd_felix.codex import birth
    from gtd_felix.codex_remote import _close_owned
    route=config['codex']['routes']['worker']
    request={'op':op,'route':route,'native_config_sha256':config['native_config_sha256'],'expected_hashes':expected_hashes}
    process=await asyncio.create_subprocess_exec(SSH,'-oBatchMode=yes','-oConnectTimeout=8',route['remote']['ssh_alias'],
        'python3 -c '+shlex.quote(HELPER),stdin=asyncio.subprocess.PIPE,stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.DEVNULL,start_new_session=True,limit=1024*1024)
    identity={'pid':process.pid,'birth':birth(process.pid),'pgid':os.getpgid(process.pid)}
    try:
        raw,_=await asyncio.wait_for(process.communicate(encode(request)),25)
        require(process.returncode==0 and len(raw)<=400000,'remote_evidence_unconfirmed')
        value=json.loads(raw)
        require(value['hostname']==route['remote']['hostname'] and value['uid']==route['remote']['uid']
                and value['workspace']==route['workspace'] and value['native_config_sha256']==config['native_config_sha256'], 'remote_evidence_identity_changed')
        return value
    finally:
        await _close_owned(process,identity)


def verify_snapshot(snapshot):
    require(set(snapshot['files'])==set(SEED),'remote_allowlist_changed')
    contents={}
    for name,value in snapshot['files'].items():
        raw=base64.b64decode(value['base64'],validate=True)
        require(len(raw)<=65536 and len(raw)==value['size'] and sha(raw)==value['sha256'],'remote_evidence_hash_mismatch')
        contents[name]=raw
    require(all(contents[n]==SEED[n].encode() for n in PROTECTED),'protected_workspace_file_changed')
    return contents


async def check_workspace(config, case, label, job_id=None):
    snapshot=await remote_call(config,'snapshot');contents=verify_snapshot(snapshot)
    copy=case/('evidence-'+label+'-'+uuid.uuid4().hex);copy.mkdir(mode=0o700)
    for name,raw in contents.items():private_file(copy/name,raw)
    contract.safe_function(copy/'clamp.py')
    hashes={n:sha(raw) for n,raw in contents.items()}
    tested=await remote_call(config,'test',hashes)
    require(verify_snapshot(tested)==contents,'snapshot_changed_before_test')
    require(tested['test']['pid_absent'] is True,'remote_test_process_unresolved')
    report={'label':label,'job_id':job_id,'files':hashes,'exit_code':tested['test']['exit_code'],
            'remote_test':tested['test'],'remote_workspace':config['codex']['routes']['worker']['workspace'],
            'evidence_copy':str(copy),'copy_role':'probatory_not_delivery_or_gtd_material'}
    private_file(copy/'receipt.json',encode(report))
    return report


def identity_projection(adapter, job_id):
    remote=adapter._get('remote:'+job_id) or {};native=adapter._get('job:'+job_id) or {}
    return {**{k:remote.get(k) for k in ('name','unit','deadline','remote_deadline','boot_id','invocation_id','pid','birth','socket','route_hash')},
            **{k:native.get(k) for k in ('thread_id','turn_id')}}


def events(adapter):
    return [{'key':r[0],'event':json.loads(r[1])} for r in adapter.store.db.execute("SELECT key,value FROM metadata WHERE key LIKE 'codex:event:%'")]


def dispatch_counts(adapter):
    values=events(adapter)
    return {method:sum(e['event'].get('direction')=='request' and e['event'].get('method')==method for e in values)
            for method in ('thread/start','thread/resume','turn/start')}


async def reconnect(router, adapter, job_id):
    current=await router.reconcile(job_id)
    if current.get('terminal'):
        return current,{'verified':False,'status':'NOT_RUN','reason':'native_already_terminal_before_disconnect'}
    require(current.get('native_status')=='running','running_turn_unconfirmed')
    route=adapter._job(job_id)[1]
    transport=adapter._remote(job_id,route)
    identity=adapter._get('remote:'+job_id)
    alive=await transport._call('observe',identity)
    transport._bind(identity,alive)
    require(alive.get('pid') and alive.get('cgroup_pids'),'live_remote_unit_unconfirmed')
    before=identity_projection(adapter,job_id);counts=dispatch_counts(adapter)
    require(before['name'] and before['thread_id'],'exact_remote_session_missing')
    await adapter._close_process(job_id)
    response=await router.reconcile(job_id)
    after=identity_projection(adapter,job_id)
    # Lost turn ACK may acquire its first turn ID; it may never replace a known ID.
    require(all(after[k]==v for k,v in before.items() if v is not None),'reconnect_identity_changed')
    require(dispatch_counts(adapter)==counts,'reconnect_dispatched_new_work')
    require(after['turn_id'] and response.get('status')=='observed','reconnect_readback_unconfirmed')
    return response,{'before':before,'after':after,'dispatch_counts':counts,'verified':True,'before_native':current,'before_unit':alive}


async def run(config_path, *, work=False, recover=False, preflight=False):
    require(sum((work,recover,preflight))<=1,'exclusive_modes_required')
    config_path=Path(config_path)
    require(config_path.is_absolute() and config_path.resolve()==config_path and config_path.name!='auth.json','canonical_config_required')
    info=config_path.lstat()
    require(stat.S_ISREG(info.st_mode) and info.st_uid==os.getuid() and info.st_nlink==1
            and info.st_mode&0o077==0 and info.st_size<=65536,'private_config_required')
    raw=config_path.read_bytes();config=json.loads(raw);case,runtime=validate_config(config)
    if not (work or recover or preflight):
        return {'status':'DESCRIPTION_READY','ssh_calls':0,'work_submissions_requested':0,
                'remote_workspace':config['codex']['routes']['worker']['workspace'],
                'seed_sha256':{n:sha(v.encode()) for n,v in SEED.items()},
                'reservation':config['reservation'],'principal_assessment':'NOT_RUN'}
    sys.path.insert(0,str(runtime))
    from gtd_felix.service import GTDService
    from gtd_felix.control import ExecutionControl
    from gtd_felix.codex import CodexAdapter, process_overlay
    from gtd_felix.codex_remote import validate_remote_route
    from gtd_felix.adapters import AdapterRouter
    from gtd_felix.orchestration import OrchestrationWorker
    require(Path(sys.modules['gtd_felix.codex'].__file__).resolve().is_relative_to(runtime),'runtime_import_mismatch')
    route=config['codex']['routes']['worker'];validate_remote_route(route);process_overlay(route)
    if not case.exists():
        require(not recover,'recover_case_missing');case.mkdir(mode=0o700)
        private_file(case/'state.json',encode({'config_sha256':sha(raw),'runtime':config['runtime_manifest'],
            'script_sha256':file_hash(Path(__file__)),'contract_sha256':file_hash(_LOCAL),'phase':'prepared','job_id':None}))
    require(case.is_dir() and case.stat().st_uid==os.getuid() and case.stat().st_mode&0o077==0,'private_case_required')
    lock=os.open(case/'runner.lock',os.O_WRONLY|os.O_CREAT|os.O_NOFOLLOW,0o600)
    try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except OSError:os.close(lock);raise ValueError('case_already_running')
    service=router=adapter=None;state={};control=None
    result={'status':'BLOCKED','mode':'recover' if recover else 'work' if work else 'preflight',
            'work_submissions_requested':0,'principal_assessment':'NOT_RUN','remote_delivery':'NOT_VERIFIED',
            'gtd_native_report_integration':'NOT_RUN','local_copy_role':'probatory_only',
            'campaign_id':config['campaign']['id'],'config_sha256':sha(raw),'case_dir':str(case)}
    try:
        state=json.loads((case/'state.json').read_text())
        require(state['config_sha256']==sha(raw) and state['runtime']==config['runtime_manifest']
                and state['script_sha256']==file_hash(Path(__file__)) and state['contract_sha256']==file_hash(_LOCAL),'case_binding_changed')
        campaign=config['campaign'];reservation=config['reservation'];actors=config['actors']
        budget={k:campaign[k] for k in ('period_start','period_seconds','max_cost_usd','max_runtime_seconds')}
        budget.update(recovery_cost_usd=0,recovery_runtime_seconds=0,max_active=1,
                      max_job_runtime_seconds=reservation['max_runtime_seconds'],max_retries=0,max_descendants=0)
        service=GTDService(case/'data',owner_actor=actors['owner'],principal_actor=actors['principal'],executor_actors=[actors['executor']])
        control=ExecutionControl(service,budget);adapter=CodexAdapter(control,config['codex'])
        router=AdapterRouter(control,None,adapter,{'providers':{'worker':'codex'}})
        prior=control._load()['operations'].get('codex-remote-work:reserve',{}).get('receipt',{})
        job_id=state.get('job_id') or prior.get('job_id')
        if job_id:
            state['job_id']=job_id;require(recover,'existing_job_requires_recover')
        elif recover:
            result.update(status='NOT_RUN',reason='no_existing_reservation');return result
        else:
            baseline=await check_workspace(config,case,'before')
            require(baseline['files']=={n:sha(v.encode()) for n,v in SEED.items()} and baseline['exit_code']!=0,'synthetic_baseline_not_red')
            state['before']=baseline
            discovery=await router.discover('worker');result['discovery']=discovery
            require(discovery.get('status')=='ready','discovery_unavailable')
            if preflight:result['status']='PREFLIGHT_READY';return result
            item=service.capture(actors['owner'],'codex-remote-work:capture','Correct the remote synthetic clamp in its authorized workspace')['item']
            clarified=service.execute(actors['owner'],{'operation_id':'codex-remote-work:clarify','action':'clarify',
                'item_id':item['id'],'expected_version':item['version'],'fields':{'kind':'action','commitment':'committed',
                'completion_criteria':'Inclusive clamp, reversed bounds ValueError, six immutable tests pass; preserve other three files.'}})
            require(clarified['status']=='applied','owner_contract_rejected');item=clarified['item']
            grant=service.execute(actors['owner'],{'operation_id':'codex-remote-work:mandate','action':'grant_mandate',
                'item_id':item['id'],'expected_version':item['version'],'fields':{'scope_item_id':item['id'],
                'capabilities':['prepare_private'],'actors':[actors['executor']],'completion_criteria':item['completion_criteria']}})
            require(grant['status']=='applied','owner_mandate_rejected')
            registered=control.register_bot(actors['owner'],'codex-remote-work:bot',{'id':'worker','actor':actors['executor'],
                'state':'available','source_urn':'urn:synthetic:codex-remote-clamp-probe','host':'ssh','profile':route['profile'],
                'capabilities':['prepare_private'],'probe_evidence':discovery})
            require(registered['status']=='applied','worker_registration_rejected')
            reserved=control.reserve(actors['principal'],'codex-remote-work:reserve',{'item_id':item['id'],
                'expected_version':service.get_item(item['id'])['version'],'mandate_id':grant['mandate']['id'],
                'capability':'prepare_private','bot_id':'worker','purpose':'Correct clamp in remote workspace',
                'scope':route['workspace'],**reservation,'max_retries':0,'max_descendants':0})
            require(reserved['status']=='reserved','reservation_rejected')
            job_id=reserved['job_id'];state.update(job_id=job_id,phase='reserved')
            private_file(case/'state.json',encode(state),replace=True)
            prompt=('Implement clamp(value, lower, upper): inclusive bounds; raise ValueError when lower > upper. '
                'Only edit clamp.py. Use one undecorated function, min/max or comparisons/return/raise ValueError; '
                'no imports, attributes, loops, recursion, annotations, new files or external effects. '
                'Preserve AGENTS.md, test_clamp.py and concurrent_sentinel.txt byte for byte. '
                'Run python3 -B -m unittest test_clamp.py in the authorized workspace. '
                'Report actual changes and tests in your native final response; do not claim principal assessment. '
                'Workspace: '+route['workspace']+'. Job: '+job_id)
            result['work_submissions_requested']=1
            await router.submit(job_id,prompt,durable=True)
        result['job_id']=job_id
        original=identity_projection(adapter,job_id)
        require(original['name'],'remote_job_identity_missing')
        if state.get('remote_identity'):
            require(all(original[k]==v for k,v in state['remote_identity'].items() if v is not None),'durable_remote_identity_changed')
        else:state['remote_identity']=original
        private_file(case/'state.json',encode(state),replace=True)
        response=await router.reconcile(job_id) if control.get_job(job_id)['terminal'] else None
        if not control.get_job(job_id)['terminal'] and original['thread_id']:
            response,witness=await reconnect(router,adapter,job_id)
            state['reconnect']=witness
            private_file(case/'state.json',encode(state),replace=True)
        # Deadline originates in the real adapter's durable record; never a new
        # reservation or relative runtime granted by this invocation.
        while not control.get_job(job_id)['terminal'] and time.time()<original['deadline']-config['codex']['shutdown_grace_seconds']:
            if not original['thread_id']:break
            await asyncio.sleep(.2);response=await router.reconcile(job_id)
        if not control.get_job(job_id)['terminal']:
            await router.stop(job_id)
            response=await router.reconcile(job_id)
            # Lost unit ACK before thread creation has no native session to read.
            # Bind/stop only the existing identity, never ensure/create a new unit.
            await adapter._remote(job_id,route).stop()
        job=control.get_job(job_id)
        result.update(terminal=job['terminal'],native=job.get('native'),reconnect=state.get('reconnect'),
                      budget=control.budget(),cost_semantics='technical_reservation_not_measured_billing')
        require(job['terminal'] and job['observations'][-1]['native_status']=='completed','native_success_unconfirmed')
        after=await check_workspace(config,case,'after',job_id);result['technical_checks']=after
        require(after['exit_code']==0 and after['files']['clamp.py']!=sha(contract.INITIAL.encode()),'workspace_criteria_failed')
        result['remote_delivery']='VERIFIED'
        worker=OrchestrationWorker(service,control,router,{})
        output=worker._output(response)
        require(output and json.loads(output).get('messages'),'native_final_missing')
        integrated=worker._integrate(job_id,response,durable=True)
        require(integrated.get('status')=='integrated','native_report_not_integrated')
        result.update(gtd_native_report_integration='integrated',
            material_kind='native_execution_report_not_remote_file',
            materials=[{'id':m['id'],'version':m['version']} for m in service.materials(job['item_id'])],
            item_status=service.get_item(job['item_id'])['status'],
            status='TECHNICAL_CRITERIA_PASS' if state.get('reconnect',{}).get('verified') else 'PARTIAL_RECONNECT_NOT_OBSERVED')
        state['phase']='technical_verified';return result
    except (ValueError,OSError,KeyError,TypeError,SyntaxError,asyncio.TimeoutError) as error:
        result.update(status='BLOCKED',reason=str(error) if isinstance(error,ValueError) else type(error).__name__)
        return result
    finally:
        if adapter:
            pending=state.get('job_id')
            if pending and not control.get_job(pending)['terminal']:
                try:
                    await asyncio.wait_for(router.stop(pending),10)
                    await asyncio.wait_for(router.reconcile(pending),10)
                    if adapter._get('remote:'+pending):await asyncio.wait_for(adapter._remote(pending,route).stop(),10)
                except (ValueError,OSError,asyncio.TimeoutError):pass
            try:await router.close()
            except (ValueError,OSError,asyncio.TimeoutError):result.update(status='BLOCKED',reason='ssh_close_unconfirmed')
            units=[{'key':r[0],'identity':json.loads(r[1])} for r in service.store.db.execute("SELECT key,value FROM metadata WHERE key LIKE 'codex:remote:%'")]
            for unit in units:
                identity=unit['identity']
                try:
                    observed=await adapter._remote(unit['key'].removeprefix('codex:remote:'),route)._call('observe',identity)
                    require(observed.get('uid')==route['remote']['uid'] and observed.get('hostname')==route['remote']['hostname']
                            and observed.get('boot_id')==identity.get('boot_id')
                            and observed.get('InvocationID') in ('',identity.get('invocation_id')), 'remote_closure_identity_changed')
                    unit['fresh_observation']=observed
                except (ValueError,OSError,asyncio.TimeoutError):unit['fresh_observation']={}
            result['remote_units']=units
            result['remote_closure_verified']=bool(units) and all(
                v['identity'].get('contained') is True and v['fresh_observation'].get('owned_pid_absent') is True
                and not v['fresh_observation'].get('pid') and not v['fresh_observation'].get('cgroup_pids') for v in units)
            result['native_events']=events(adapter);result['dispatch_counts']=dispatch_counts(adapter)
            ssh=[json.loads(r[0]) for r in service.store.db.execute("SELECT value FROM metadata WHERE key LIKE 'codex:ssh:%'")]
            ssh.extend(e['event']['ssh'] for e in result['native_events'] if e['event'].get('direction')=='remote_control_channel')
            for record in ssh:record['pid_absent']=not Path('/proc',str(record.get('pid'))).exists()
            result['ssh_channels']=ssh
            if (units and not result['remote_closure_verified']) or not all(v['pid_absent'] for v in ssh):
                result.update(status='BLOCKED',reason='owned_process_closure_unconfirmed')
            if result['dispatch_counts']['turn/start']>1 or result['dispatch_counts']['thread/start']>1 or result['dispatch_counts']['thread/resume']:
                result.update(status='BLOCKED',reason='duplicate_native_dispatch')
            if pending:result['final_job']=control.get_job(pending)
            result['control']=control._load();service.close()
        private_file(case/'state.json',encode(state),replace=True)
        name='receipt-'+uuid.uuid4().hex+'.json';data=encode(result);private_file(case/name,data)
        result['receipt']=str(case/name);result['receipt_sha256']=sha(data)
        fcntl.flock(lock,fcntl.LOCK_UN);os.close(lock)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--config',required=True)
    modes=parser.add_mutually_exclusive_group()
    for name in ('work','recover','preflight'):modes.add_argument('--'+name,action='store_true')
    args=parser.parse_args()
    try:result=asyncio.run(run(args.config,work=args.work,recover=args.recover,preflight=args.preflight))
    except Exception as error:result={'status':'BLOCKED','reason':str(error) if isinstance(error,ValueError) else type(error).__name__}
    print(json.dumps(result if result['status']=='DESCRIPTION_READY' else {k:result[k] for k in ('status','reason','job_id','receipt','receipt_sha256','work_submissions_requested') if k in result}))
    return 0 if result['status'] in ('DESCRIPTION_READY','PREFLIGHT_READY','TECHNICAL_CRITERIA_PASS') else 2


if __name__=='__main__':raise SystemExit(main())
