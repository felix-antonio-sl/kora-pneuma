#!/usr/bin/env python3
"""Zero-model remote readiness. Default DESCRIBE performs zero SSH.

Explicit --preflight uses a NEW private evidence directory and one owned bounded
transport, never a campaign reservation. Existing case/config/lease remain intact.
"""
import argparse
import asyncio
import importlib.util
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import stat
import sys
import uuid

FROZEN = Path(__file__).with_name('gtd_codex_remote_work_probe.py')
FROZEN_SHA256 = 'cae63da7deb91566c7694f5b3cee4334429a69238594e2568a61e616a1c1c281'
# Check both executable dependencies before importing either one.
for dependency, expected in ((FROZEN,FROZEN_SHA256),
        (FROZEN.with_name('gtd_codex_work_probe.py'),'58fff6ccd572a1cb0c479d73441fe632f49f1f248fee00fa4c85836fe7635ae6')):
    if hashlib.sha256(dependency.read_bytes()).hexdigest()!=expected:
        raise ValueError('frozen_contract_changed')
_spec = importlib.util.spec_from_file_location('readiness_remote_contract', FROZEN)
probe = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(probe)
require, sha, encode = probe.require, probe.sha, probe.encode

# Fixed program, fixed companion sibling, PATH-only framed protocol probe.
# Only code binaries and config.toml are read; no account/session/auth files.
HELPER = r'''
import hashlib,json,os,stat,struct,subprocess,sys
from pathlib import Path
def need(value,reason):
 if not value: raise ValueError(reason)
def read(path,limit):
 need(str(path.resolve(strict=True))==str(path),'file_path_changed')
 fd=os.open(path,os.O_RDONLY|os.O_NOFOLLOW)
 try:
  before=os.fstat(fd)
  need(stat.S_ISREG(before.st_mode) and before.st_uid==q['route']['remote']['uid'] and before.st_nlink==1 and before.st_size<=limit,'file_identity_changed')
  with os.fdopen(fd,'rb',closefd=False) as stream: data=stream.read(limit+1)
  after=os.fstat(fd)
  need(len(data)<=limit and (before.st_size,before.st_mtime_ns,before.st_ctime_ns)==(after.st_size,after.st_mtime_ns,after.st_ctime_ns) and path.lstat().st_ino==before.st_ino,'file_changed_during_read')
  return data
 finally:os.close(fd)
q=json.load(sys.stdin);r=q['route']['remote'];result={'status':'FAIL'}
try:
 need(os.uname().nodename==r['hostname'] and os.getuid()==r['uid'],'remote_host_changed')
 binary=Path(r['binary']);host=binary.with_name('codex-code-mode-host')
 need(binary.name=='codex' and binary.parent.name=='bin','binary_layout_invalid')
 need(hashlib.sha256(read(binary,256*1024*1024)).hexdigest()==r['binary_sha256'],'codex_hash_changed')
 need(host.exists(),'companion_missing')
 need(hashlib.sha256(read(host,256*1024*1024)).hexdigest()==q['companion_sha256'],'companion_hash_changed')
 need(os.access(binary,os.X_OK) and os.access(host,os.X_OK),'binary_not_executable')
 need(hashlib.sha256(read(Path(r['codex_home'])/'config.toml',65536)).hexdigest()==q['native_config_sha256'],'native_config_changed')
 payload=json.dumps({'type':'connection/hello','supportedVersions':[1],'requiredCapabilities':[],'optionalCapabilities':[]}).encode()
 p=subprocess.run([str(host),'--listen','stdio'],input=struct.pack('<I',len(payload))+payload,env={'PATH':'/usr/bin:/bin'},cwd='/',timeout=5,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 need(p.returncode==0 and not p.stderr and 4<=len(p.stdout)<=4096,'companion_handshake_failed')
 length=struct.unpack('<I',p.stdout[:4])[0]
 need(length==len(p.stdout)-4 and json.loads(p.stdout[4:])=={'type':'connection/ready','selectedVersion':1,'capabilities':[]},'companion_protocol_invalid')
 result.update(status='PASS',hostname=r['hostname'],uid=r['uid'],binary_sha256=r['binary_sha256'],companion_sha256=q['companion_sha256'],native_config_sha256=q['native_config_sha256'],protocol=1)
except (OSError,ValueError,subprocess.TimeoutExpired) as error:
 result['reason']=str(error) if isinstance(error,ValueError) else type(error).__name__
print(json.dumps(result))
'''


def native_params(workspace):
    return {'command':['/usr/bin/true'],'cwd':workspace,
            'sandboxPolicy':{'type':'workspaceWrite','writableRoots':[workspace],
                'networkAccess':False,'excludeSlashTmp':True,'excludeTmpdirEnvVar':True},
            'timeoutMs':5000,'outputBytesCap':2048}


def pid_absent(identity):
    # Deliberately stricter than merely detecting PID reuse.
    return not Path('/proc',str(identity['pid'])).exists()


async def check_companion(config, companion_sha256, ssh_identities):
    from gtd_felix.codex import birth
    from gtd_felix.codex_remote import _close_owned
    route=config['codex']['routes']['worker']
    request={'route':route,'companion_sha256':companion_sha256,
             'native_config_sha256':config['native_config_sha256']}
    process=await asyncio.create_subprocess_exec(probe.SSH,'-oBatchMode=yes','-oConnectTimeout=8',
        route['remote']['ssh_alias'],'python3 -I -B -c '+shlex.quote(HELPER),
        stdin=asyncio.subprocess.PIPE,stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.DEVNULL,start_new_session=True,limit=65536)
    identity={'pid':process.pid,'birth':birth(process.pid),'pgid':os.getpgid(process.pid)}
    ssh_identities.append(identity)
    try:
        raw,_=await asyncio.wait_for(process.communicate(encode(request)),15)
        require(process.returncode==0 and len(raw)<=8192,'companion_evidence_unconfirmed')
        result=json.loads(raw)
        require(isinstance(result,dict),'companion_evidence_invalid')
        if result.get('status')=='PASS':
            require(all(result.get(k)==v for k,v in {'hostname':route['remote']['hostname'],
                'uid':route['remote']['uid'],'binary_sha256':route['remote']['binary_sha256'],
                'companion_sha256':companion_sha256,'native_config_sha256':config['native_config_sha256'],
                'protocol':1}.items()),'companion_evidence_identity_changed')
        return result
    finally:
        await _close_owned(process,identity)
        require(pid_absent(identity),'companion_ssh_closure_unconfirmed')


def bounded_error(error):
    # RPC intentionally discards native error bodies. Do not invent diagnostics.
    return str(error)[:2048] if isinstance(error,ValueError) else type(error).__name__


async def evaluate(adapter, route, gate):
    """Real adapter seam, also exercised with local simulated SSH/native peers."""
    key='readiness:'+uuid.uuid4().hex
    result={'status':'FAIL','key':key,'jobs_reserved':0,'model_calls':0,
            'companion':'NOT_RUN','native_command':'NOT_RUN','closure':'NOT_RUN'}
    transport=adapter._remote(key,route)
    own_ssh=[]
    try:
        result['companion']=await gate(own_ssh)
        require(result['companion'].get('status')=='PASS','companion_not_ready')
        rpc=await adapter._spawn(key,route)
        result['effective_config_sha256']=adapter._effective_config(route,
            await rpc.request('config/read',{'cwd':route['workspace'],'includeLayers':False}))
        await adapter._tools_verified(rpc,route=route)
        result['native_command']='DISPATCHED'
        native=await rpc.request('command/exec',native_params(route['workspace']))
        require(isinstance(native,dict),'native_command_response_invalid')
        stderr=native.get('stderr','')
        require(isinstance(stderr,str),'native_stderr_invalid')
        result['native_command']={'exit_code':native.get('exitCode'),'stderr':stderr[:2048]}
        require(type(native.get('exitCode')) is int and native['exitCode']==0,'native_sandbox_command_failed')
        result['status']='READY'
    except Exception as error:
        result['reason']=bounded_error(error)
    finally:
        try:
            await adapter._close_process(key)
            identity=adapter._get('remote:'+key)
            if identity:
                await transport.stop()
                identity=adapter._get('remote:'+key)
                fresh=await transport._call('observe',identity)
                require(fresh.get('uid')==route['remote']['uid'] and fresh.get('hostname')==route['remote']['hostname']
                    and fresh.get('boot_id')==identity['boot_id']
                    and fresh.get('InvocationID') in ('',identity.get('invocation_id'))
                    and not fresh.get('pid') and fresh.get('owned_pid_absent') is True
                    and fresh.get('cgroup_pids')==[],'fresh_remote_closure_unconfirmed')
                result['remote_identity']={k:identity.get(k) for k in ('name','unit','pid','birth','boot_id','invocation_id','deadline','remote_deadline','runtime_ceiling','route_hash')}
                result['remote_closed']={k:fresh.get(k) for k in ('pid','owned_pid_absent','cgroup_pids','boot_id','InvocationID')}
            ssh=adapter._get('ssh:'+key)
            if ssh:own_ssh.append({k:ssh[k] for k in ('pid','birth','pgid')})
            rows=probe.events(adapter)
            for entry in rows:
                event=entry['event']
                if event.get('direction')=='remote_control_channel':own_ssh.append(event['ssh'])
            require(all(pid_absent(i) for i in own_ssh),'owned_ssh_closure_unconfirmed')
            result['ssh_identities']=own_ssh
            result['closure']='PASS'
        except Exception as error:
            result.update(status='FAIL',closure='FAIL',closure_reason=bounded_error(error))
        counts=probe.dispatch_counts(adapter)
        command_count=sum(e['event'].get('direction')=='request' and e['event'].get('method')=='command/exec'
            for e in probe.events(adapter))
        result['command_exec_count']=command_count
        result['dispatch_counts']=counts
        jobs=adapter.control._load().get('jobs',{})
        result['jobs_observed']=len(jobs)
        if any(counts.values()) or jobs or command_count>1:result.update(status='FAIL',reason='zero_model_invariant_failed')
    return result


async def run(config_path, companion_sha256, output_dir, *, preflight=False):
    require(probe.file_hash(FROZEN)==FROZEN_SHA256,'frozen_contract_changed')
    path=Path(config_path)
    require(path.is_absolute() and path.resolve()==path and path.name!='auth.json','canonical_config_required')
    info=path.lstat()
    require(stat.S_ISREG(info.st_mode) and info.st_uid==os.getuid() and info.st_nlink==1
        and info.st_mode&0o077==0 and info.st_size<=65536,'private_config_required')
    raw=path.read_bytes();config=json.loads(raw)
    _,runtime=probe.validate_config(config)
    require(re.fullmatch('[0-9a-f]{64}',companion_sha256) is not None,'companion_pin_required')
    output=Path(output_dir)
    require(output.is_absolute() and output.resolve()==output and output.parent.is_dir()
        and not output.exists() and not output.is_symlink(),'new_canonical_output_required')
    result={'status':'DESCRIBE','ssh_calls':0,'model_calls':0,'jobs_reserved':0,
        'config_sha256':sha(raw),'runtime_manifest':config['runtime_manifest'],
        'script_sha256':probe.file_hash(Path(__file__)),'frozen_contract_sha256':FROZEN_SHA256,
        'companion_sha256':companion_sha256,'output_dir':str(output),
        'verification_scope':'companion protocol and one native sandbox command; no model/tool-turn proof',
        'native_command_params':native_params(config['codex']['routes']['worker']['workspace'])}
    if not preflight:return result
    output.mkdir(mode=0o700)
    sys.path.insert(0,str(runtime))
    from gtd_felix.service import GTDService
    from gtd_felix.control import ExecutionControl
    from gtd_felix.codex import CodexAdapter
    require(Path(sys.modules['gtd_felix.codex'].__file__).resolve().is_relative_to(runtime),'runtime_import_mismatch')
    actors=config['actors'];campaign=config['campaign']
    service=GTDService(output/'data',owner_actor=actors['owner'],principal_actor=actors['principal'],executor_actors=[actors['executor']])
    try:
        budget={k:campaign[k] for k in ('period_start','period_seconds','max_cost_usd','max_runtime_seconds')}
        budget.update(recovery_cost_usd=0,recovery_runtime_seconds=0,max_active=1,
            max_job_runtime_seconds=config['reservation']['max_runtime_seconds'],max_retries=0,max_descendants=0)
        adapter=CodexAdapter(ExecutionControl(service,budget),config['codex'])
        route=adapter._route('worker')
        async def gate(identities):return await check_companion(config,companion_sha256,identities)
        result.pop('ssh_calls')
        result.update(await evaluate(adapter,route,gate))
    finally:
        service.close()
    probe.private_file(output/'receipt.json',encode(result))
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config',required=True)
    parser.add_argument('--companion-sha256',required=True)
    parser.add_argument('--output-dir',required=True)
    parser.add_argument('--preflight',action='store_true')
    args=parser.parse_args()
    try:result=asyncio.run(run(args.config,args.companion_sha256,args.output_dir,preflight=args.preflight))
    except Exception as error:result={'status':'FAIL','reason':bounded_error(error)}
    summary={k:v for k,v in result.items() if k not in ('runtime_manifest','ssh_identities','native_command_params')}
    if args.preflight and Path(args.output_dir,'receipt.json').is_file():
        summary['receipt_path']=str(Path(args.output_dir,'receipt.json'))
    print(json.dumps(summary,sort_keys=True,indent=2))
    return 0 if result['status'] in ('DESCRIBE','READY') else 1


if __name__=='__main__':raise SystemExit(main())
