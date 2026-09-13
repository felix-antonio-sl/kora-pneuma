"""Bounded SSH transport. Unit identity is never a local tunnel PID.

One nonrenewable transient unit per reservation. No remote GTD writer, auth
transfer, shell config edits or implicit restart. Unit death is containment
 evidence, not a fabricated native terminal observation.
"""
import asyncio
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import shlex
import signal
import stat
import tempfile
import time
import uuid

import aiohttp

SSH = '/usr/bin/ssh'


def require(value, reason):
    if not value: raise ValueError(reason)


def canonical(value):
    return (isinstance(value, str) and value.startswith('/') and len(value) <= 4096
            and str(PurePosixPath(value)) == value and '..' not in PurePosixPath(value).parts)


def validate_remote_route(route):
    remote = route.get('remote')
    require(route.get('host') == 'ssh' and isinstance(remote, dict) and set(remote) == {
        'ssh_alias', 'hostname', 'uid', 'binary', 'binary_sha256', 'codex_home', 'private_root',
        'max_runtime_seconds'}, 'remote_route_fields_invalid')
    for key in ('ssh_alias', 'hostname'):
        require(isinstance(remote[key], str) and re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]{0,127}', remote[key]), 'remote_host_invalid')
    require(type(remote['uid']) is int and remote['uid'] >= 0, 'remote_uid_invalid')
    require(all(canonical(p) for p in (remote['binary'], remote['codex_home'], remote['private_root'], route.get('workspace'))), 'remote_path_invalid')
    require(isinstance(remote['binary_sha256'], str) and re.fullmatch('[0-9a-f]{64}', remote['binary_sha256']), 'remote_hash_invalid')
    require(type(remote['max_runtime_seconds']) in (int, float) and math.isfinite(remote['max_runtime_seconds'])
            and 0 < remote['max_runtime_seconds'] <= 120, 'remote_runtime_invalid')
    sources = route.get('instruction_sources')
    require(isinstance(sources, dict) and len(sources) <= 100 and all(canonical(p) and isinstance(h, str)
        and re.fullmatch('[0-9a-f]{64}', h) for p, h in sources.items()), 'remote_instruction_manifest_invalid')
    require(route.get('process_overlay') is not None, 'remote_overlay_required')
    return remote


# Fixed helper, input via stdin; no config/instructions/credentials in SSH argv.
# stdout is a bounded projection. Never read auth or native session contents.
HELPER = r'''
import sys,json,os,stat,hashlib,subprocess,time,re
from pathlib import Path
q=json.load(sys.stdin); r=q['remote']; route=q['route']; op=q['op']
def need(v,e):
 if not v: raise ValueError(e)
def path(value,kind):
 p=Path(value); need(p.is_absolute() and str(p.resolve(strict=True))==value,'remote_path_changed')
 s=p.lstat();need(s.st_uid==r['uid'],'remote_path_uid_changed')
 need(stat.S_ISDIR(s.st_mode) if kind=='dir' else stat.S_ISREG(s.st_mode),'remote_path_type_changed')
 return p
def digest(p):
 need(p.stat().st_size<=16*1024*1024,'remote_file_too_large');return hashlib.sha256(p.read_bytes()).hexdigest()
need(os.getuid()==r['uid'] and subprocess.check_output(['hostname'],text=True).strip()==r['hostname'],'remote_host_identity_changed')
binary=path(r['binary'],'file');need(os.access(binary,os.X_OK),'remote_binary_not_executable')
# Native executable can be larger than instruction files.
need(binary.stat().st_size<=256*1024*1024 and hashlib.sha256(binary.read_bytes()).hexdigest()==r['binary_sha256'],'remote_binary_hash_changed')
for value in (r['codex_home'],route['workspace'],r['private_root']):path(value,'dir')
need(stat.S_IMODE(Path(r['private_root']).stat().st_mode)==0o700,'remote_root_not_private')
if q.get('for_model'):
 for filename,checksum in route['instruction_sources'].items():need(digest(path(filename,'file'))==checksum,'remote_instruction_source_changed')
boot_id=Path('/proc/sys/kernel/random/boot_id').read_text().strip()
if op=='validate':
 print(json.dumps({'uid':os.getuid(),'hostname':r['hostname'],'binary_sha256':r['binary_sha256'],
 'boot_id':boot_id,'monotonic':time.monotonic()}));sys.exit(0)
i=q['identity']
need(i.get('boot_id') in (None,boot_id),'remote_boot_changed')
need(i['directory']==str(Path(r['private_root'])/i['name']),'remote_directory_mismatch')
need(i['unit']==i['name']+'.service' and i['name'].startswith('gtd-codex-') and len(i['name'])==42,'remote_unit_invalid')
need(i['socket']==i['directory']+'/s' and len(i['socket'].encode())<104,'remote_socket_invalid')
def run(args):
 p=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,text=True,timeout=10)
 need(len(p.stdout)<=65536,'remote_response_too_large');return p
if op=='start':
 need(i.get('boot_id')==boot_id and isinstance(i.get('remote_deadline'),(int,float)),'remote_clock_binding_missing')
 remaining=i['remote_deadline']-time.monotonic();launch=min(2,remaining/4)
 runtime=remaining-2*launch-q['grace'];need(0<runtime<=120,'remote_deadline_expired')
 cutoff=i['remote_deadline']-runtime-launch-q['grace']
 condition='/usr/bin/python3 -c '+json.dumps('import time,sys;from pathlib import Path;sys.exit(0 if Path("/proc/sys/kernel/random/boot_id").read_text().strip()=='+repr(boot_id)+' and time.monotonic()<='+repr(cutoff)+' else 1)')
 d=Path(i['directory']);d.mkdir(mode=0o700) # Exclusive claim; never repeat a start.
 args=['systemd-run','--user','--unit='+i['unit'],'--property=Type=exec','--property=Restart=no',
 '--property=Description='+i['name'],'--property=RuntimeMaxSec='+str(runtime)+'s',
 '--property=TimeoutStartSec='+str(launch)+'s','--property=ExecCondition='+condition,
 '--property=TimeoutStopSec='+str(q['grace'])+'s','--property=KillMode=control-group','--property=UMask=0077',
 '--property=WorkingDirectory='+route['workspace'],'--property=StandardOutput=null','--property=StandardError=null',
 '/usr/bin/env','-i','HOME='+r['codex_home'],'CODEX_HOME='+r['codex_home'],'PATH=/usr/bin:/bin','LANG=C.UTF-8',
 str(binary),'app-server','--strict-config','--listen','unix://'+i['socket'],*q['overlay_args']]
 need(run(args).returncode==0,'remote_unit_start_unconfirmed')
def observation():
 p=run(['systemctl','--user','show',i['unit'],'--property=MainPID,ActiveState,SubState,Result,InvocationID,ControlGroup,Description,KillMode,RuntimeMaxUSec'])
 d=dict(line.split('=',1) for line in p.stdout.splitlines() if '=' in line)
 pid=int(d.get('MainPID','0')); d['pid']=pid; d['birth']=None;d['uid']=os.getuid();d['hostname']=r['hostname'];d['boot_id']=boot_id
 d['socket']=None;d['cgroup_pids']=[];d['runtime_seconds']=None
 d['owned_pid_absent']=bool(i.get('pid')) and not Path('/proc',str(i['pid'])).exists()
 if pid:
  raw=d.get('RuntimeMaxUSec','');parts=re.findall(r'([0-9.]+)(h|min|ms|us|s)',raw)
  need(parts and ''.join(a+b for a,b in parts)==raw.replace(' ',''),'remote_runtime_unbounded')
  d['runtime_seconds']=sum(float(a)*{'h':3600,'min':60,'s':1,'ms':.001,'us':.000001}[b] for a,b in parts)
 if pid:
  proc=Path('/proc',str(pid));need(proc.stat().st_uid==r['uid'],'remote_process_uid_changed')
  need(str((proc/'exe').resolve())==str(binary),'remote_process_executable_changed')
  need(str((proc/'cwd').resolve())==route['workspace'],'remote_process_cwd_changed')
  cmd=(proc/'cmdline').read_bytes().split(b'\0');need(b'app-server' in cmd and ('unix://'+i['socket']).encode() in cmd,'remote_process_argv_changed')
  d['birth']=(proc/'stat').read_text().rsplit(')',1)[1].split()[19]
 if d.get('ControlGroup'):
  group=Path('/sys/fs/cgroup'+d['ControlGroup']);need(i['unit'] in group.parts,'remote_cgroup_changed')
  f=group/'cgroup.procs';d['cgroup_pids']=[int(x) for x in f.read_text().split()] if f.exists() else []
 socket=Path(i['socket'])
 if socket.exists():
  s=socket.lstat();parent=path(i['directory'],'dir');need(stat.S_ISSOCK(s.st_mode) and s.st_uid==r['uid'] and stat.S_IMODE(s.st_mode)==0o600 and stat.S_IMODE(parent.stat().st_mode)==0o700,'remote_socket_identity_changed')
  d['socket']={'uid':s.st_uid,'mode':stat.S_IMODE(s.st_mode),'inode':s.st_ino}
 return d
value=observation()
if op=='stop':
 need(value.get('InvocationID')==i.get('invocation_id') and value.get('Description')==i['name'],'remote_unit_identity_changed')
 if value['pid']:need(value['pid']==i.get('pid') and value['birth']==i.get('birth'),'remote_process_identity_changed')
 need(value.get('ControlGroup') in ('',i.get('control_group')),'remote_cgroup_changed')
 need(run(['systemctl','--user','stop',i['unit']]).returncode==0,'remote_unit_stop_unconfirmed')
 value=observation()
print(json.dumps(value))
'''


async def _close_owned(process, identity):
    if process.returncode is None:
        from .codex import birth
        require(birth(process.pid) == identity['birth'] and os.getpgid(process.pid) == identity['pgid'] == process.pid,
                'ssh_process_identity_changed')
        os.killpg(process.pid, signal.SIGTERM)
        try: await asyncio.wait_for(process.wait(), 1)
        except asyncio.TimeoutError:
            require(birth(process.pid) == identity['birth'], 'ssh_process_identity_changed')
            os.killpg(process.pid, signal.SIGKILL); await process.wait()


class RemoteChannel:
    def __init__(self, process, identity, session, websocket, directory):
        self.process, self.identity = process, identity  # Explicit SSH identity only.
        self.session, self.websocket, self.directory = session, websocket, directory

    async def send(self, message):
        try: await self.websocket.send_json(message)
        except (aiohttp.ClientError, ConnectionError) as e: raise ValueError('remote_channel_lost') from e

    async def receive(self):
        try:
            message = await self.websocket.receive()
            if message.type == aiohttp.WSMsgType.TEXT: return json.loads(message.data)
            if message.type in (aiohttp.WSMsgType.CLOSED, aiohttp.WSMsgType.CLOSE, aiohttp.WSMsgType.ERROR): return None
            raise ValueError('remote_rpc_message_invalid')
        except (aiohttp.ClientError, ConnectionError) as e: raise ValueError('remote_channel_lost') from e

    async def close(self):
        try: await self.session.close()
        finally: await _close_owned(self.process, self.identity)
        socket = self.directory / 's'
        if socket.exists(): socket.unlink()
        self.directory.rmdir()


class RemoteTransport:
    def __init__(self, adapter, key, route):
        self.adapter, self.key, self.route = adapter, key, route
        self.remote = validate_remote_route(route)

    async def _call(self, op, identity=None, *, for_model=False):
        from .codex import birth, overlay_arguments, process_overlay
        request = {'op':op,'remote':self.remote,'route':self.route,'identity':identity,
            'for_model':for_model,'grace':self.adapter.grace,'overlay_args':overlay_arguments(process_overlay(self.route))}
        process = await asyncio.create_subprocess_exec(SSH, '-oBatchMode=yes', '-oConnectTimeout=8',
            self.remote['ssh_alias'], 'python3 -c ' + shlex.quote(HELPER),
            stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.DEVNULL,
            start_new_session=True, limit=1024*1024)
        local = {'pid':process.pid,'birth':birth(process.pid),'pgid':os.getpgid(process.pid)}
        self.adapter._event(self.key, {'direction':'remote_control_channel','operation':op,'ssh':local})
        try:
            raw, _ = await asyncio.wait_for(process.communicate(json.dumps(request).encode()), self.adapter.timeout)
            require(process.returncode == 0 and len(raw) <= 65536, 'remote_control_unconfirmed')
            result = json.loads(raw)
            require(isinstance(result, dict), 'remote_response_invalid')
            return result
        finally:
            await _close_owned(process, local)

    async def validate(self, *, for_model):
        return await self._call('validate', for_model=for_model)

    def _bind(self, identity, observed):
        if identity.get('boot_id'): require(observed.get('boot_id')==identity['boot_id'],'remote_boot_changed')
        require(observed.get('uid') == self.remote['uid'] and observed.get('hostname') == self.remote['hostname'], 'remote_host_identity_changed')
        if not observed.get('pid') and observed.get('ActiveState')=='activating':
            require(observed.get('Description')==identity['name'] and observed.get('InvocationID'),'remote_unit_identity_changed')
            if identity.get('invocation_id'): require(identity['invocation_id']==observed['InvocationID'],'remote_unit_identity_changed')
            identity.update(invocation_id=observed['InvocationID'],control_group=observed.get('ControlGroup'))
            self.adapter._update('remote:' + self.key, **{**identity, 'observation':observed})
            return identity
        if not observed.get('pid'):
            require(not observed.get('cgroup_pids'), 'remote_children_unresolved')
            self.adapter._update('remote:' + self.key, observation=observed)
            raise ValueError('remote_unit_dead_readback_not_supported')
        runtime = observed.get('runtime_seconds')
        require(type(runtime) in (int,float) and math.isfinite(runtime) and 0 < runtime <= identity['runtime_ceiling'], 'remote_runtime_unbounded')
        require(observed.get('Description') == identity['name'] and observed.get('InvocationID')
            and observed.get('KillMode') == 'control-group', 'remote_unit_identity_changed')
        for field, native in (('invocation_id','InvocationID'),('pid','pid'),('birth','birth'),('control_group','ControlGroup')):
            if identity.get(field) is not None: require(identity[field] == observed.get(native), 'remote_unit_identity_changed')
            else: identity[field] = observed.get(native)
        require(identity['birth'] and identity['control_group'], 'remote_identity_incomplete')
        if observed.get('socket'):
            require(observed['socket']['uid'] == self.remote['uid'] and observed['socket']['mode'] == 0o600, 'remote_socket_identity_changed')
            if identity.get('socket_identity'): require(identity['socket_identity'] == observed['socket'], 'remote_socket_identity_changed')
            identity['socket_identity'] = observed['socket']
        self.adapter._update('remote:' + self.key, **{**identity, 'observation': observed})
        return identity

    async def ensure(self):
        from .codex import digest
        identity = self.adapter._get('remote:' + self.key)
        if identity is None:
            job = self.adapter._get('job:' + self.key)
            origin = job['created_at'] if job else time.time()
            duration = min(self.remote['max_runtime_seconds'], job['limits']['max_runtime_seconds'] if job else 30)
            require(duration > self.adapter.grace, 'remote_budget_too_small')
            clock=await self._call('validate',for_model=True)
            received=time.time()
            require(type(clock.get('monotonic')) in (int,float) and math.isfinite(clock['monotonic'])
                    and clock['monotonic']>=0 and isinstance(clock.get('boot_id'),str)
                    and re.fullmatch('[0-9a-f-]{36}',clock['boot_id']), 'remote_clock_binding_missing')
            # The remote sample precedes this receipt: anchoring at receipt is conservative.
            remaining=origin+duration-received
            require(remaining>self.adapter.grace,'remote_deadline_expired')
            name = 'gtd-codex-' + uuid.uuid4().hex
            identity = {'name':name,'unit':name+'.service','directory':self.remote['private_root']+'/'+name,
                'deadline':origin+duration,'remote_deadline':clock['monotonic']+remaining,'boot_id':clock['boot_id'],'runtime_ceiling':duration-self.adapter.grace,'route_hash':digest(self.route),'status':'creation_requested'}
            identity['socket'] = identity['directory'] + '/s'
            require(len(identity['socket'].encode()) < 104, 'remote_socket_path_too_long')
            with self.adapter.store.transaction():
                require(self.adapter._get('remote:' + self.key) is None, 'remote_creation_already_owned')
                self.adapter._put('remote:' + self.key, identity)
            # A lost ACK must never reissue this effect, even when no PID was received.
            observed = await self._call('start', identity, for_model=True)
        else:
            require(identity['route_hash'] == digest(self.route), 'remote_route_changed')
            observed = await self._call('observe', identity)
        identity = self._bind(identity, observed)
        deadline = min(time.time()+self.adapter.timeout, identity['deadline'])
        while not identity.get('socket_identity') and time.time() < deadline:
            await asyncio.sleep(.05)
            identity = self._bind(identity, await self._call('observe', identity))
        require(identity.get('socket_identity'), 'remote_socket_unconfirmed')
        return identity

    async def connect(self):
        from .codex import birth
        old = self.adapter._get('ssh:' + self.key)
        if old and old.get('pid') and old.get('status') != 'channel_closed':
            try: require(birth(old['pid']) != old.get('birth'), 'owned_ssh_channel_still_alive')
            except OSError: pass
        identity = await self.ensure()
        require(time.time() < identity['deadline'], 'remote_deadline_expired')
        directory = Path(tempfile.mkdtemp(prefix='gtd-ssh-')); directory.chmod(0o700)
        path = directory/'s'
        process = await asyncio.create_subprocess_exec(SSH, '-oBatchMode=yes', '-oConnectTimeout=8',
            '-oExitOnForwardFailure=yes', '-oClearAllForwardings=no', '-oStreamLocalBindMask=0177',
            '-N', '-L', str(path)+':'+identity['socket'], self.remote['ssh_alias'],
            stdin=asyncio.subprocess.DEVNULL, stdout=asyncio.subprocess.DEVNULL, stderr=asyncio.subprocess.DEVNULL,
            start_new_session=True)
        local = {'pid':process.pid,'birth':birth(process.pid),'pgid':os.getpgid(process.pid)}
        self.adapter._update('ssh:' + self.key, **local)
        session = None
        try:
            deadline = min(time.time()+self.adapter.timeout, identity['deadline'])
            while not path.exists() and process.returncode is None and time.time()<deadline: await asyncio.sleep(.02)
            info = path.lstat()
            require(stat.S_ISSOCK(info.st_mode) and info.st_uid == os.getuid() and stat.S_IMODE(info.st_mode)==0o600, 'local_forward_socket_invalid')
            session = aiohttp.ClientSession(connector=aiohttp.UnixConnector(path=str(path)), timeout=aiohttp.ClientTimeout(total=self.adapter.timeout))
            websocket = await session.ws_connect('http://localhost/', max_msg_size=8*1024*1024)
            return RemoteChannel(process, local, session, websocket, directory)
        except (OSError, ValueError, aiohttp.ClientError, asyncio.TimeoutError) as e:
            if session: await session.close()
            await _close_owned(process, local)
            if path.exists(): path.unlink()
            directory.rmdir()
            raise ValueError('remote_channel_unconfirmed') from e

    async def stop(self):
        identity = self.adapter._get('remote:' + self.key)
        require(identity is not None, 'remote_identity_missing')
        if identity.get('contained'): return identity['observation']
        observed = await self._call('observe', identity)
        if not observed.get('pid') and observed.get('ActiveState')=='activating':
            require(observed.get('Description')==identity['name'] and observed.get('InvocationID'),'remote_unit_identity_changed')
            if identity.get('invocation_id'): require(identity['invocation_id']==observed['InvocationID'],'remote_unit_identity_changed')
            identity.update(invocation_id=observed['InvocationID'],control_group=observed.get('ControlGroup'))
            self.adapter._update('remote:' + self.key, **{**identity, 'observation':observed})
            return identity
        if not observed.get('pid'):
            require(identity.get('invocation_id') and observed.get('InvocationID') in ('',identity['invocation_id'])
                    and observed.get('owned_pid_absent') is True and not observed.get('cgroup_pids'),
                    'remote_closure_unconfirmed')
            result = observed
        else:
            identity = self._bind(identity, observed)
            result = await self._call('stop', identity)
        require(not result.get('pid') and not result.get('cgroup_pids') and result.get('owned_pid_absent') is True,
                'remote_closure_unconfirmed')
        self.adapter._update('remote:' + self.key, observation=result, stop_requested=True, contained=True)
        return result
