"""Linux user-unit containment for local stdio, including children with setsid.

The systemd-run pipe driver is not the native process. Unit creation is durable
and exclusive; recovery creates only a separately bounded read-only transport.
"""
import asyncio
import json
import os
from pathlib import Path
import signal
import sys
import time
import uuid


def require(value, reason):
    if not value: raise ValueError(reason)


async def command(*args):
    p = await asyncio.create_subprocess_exec(*args, stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.DEVNULL, start_new_session=True)
    try:
        out, _ = await asyncio.wait_for(p.communicate(), 5)
        require(p.returncode == 0 and len(out) <= 65536, 'local_supervisor_unconfirmed')
        return out.decode()
    finally:
        if p.returncode is None:
            p.kill(); await p.wait()


def identity(pid):
    from .codex import birth
    p = Path('/proc', str(pid))
    return {'pid':pid,'birth':birth(pid),'pgid':os.getpgid(pid),'uid':p.stat().st_uid,
            'exe':str((p/'exe').resolve()),'cwd':str((p/'cwd').resolve())}


def properties(record):
    # An absolute admission guard rejects an activation delayed past the launch
    # allowance, even when the driver has already lost its acknowledgement.
    cutoff = record['deadline'] - record['runtime_seconds'] - record['start_seconds'] - record['grace']
    condition = '/usr/bin/python3 -c "import time,sys;sys.exit(0 if time.time()<=' + repr(cutoff) + ' else 1)"'
    return ['--property=Type=exec','--property=Restart=no','--property=KillMode=control-group',
        '--property=UMask=0077','--property=Description='+record['name'],
        '--property=RuntimeMaxSec='+str(record['runtime_seconds'])+'s',
        '--property=TimeoutStartSec='+str(record['start_seconds'])+'s',
        '--property=TimeoutStopSec='+str(record['grace'])+'s','--property=ExecCondition='+condition]


class LocalChannel:
    def __init__(self, supervisor, driver, read_only):
        self.supervisor, self.driver, self.read_only = supervisor, driver, read_only

    async def send(self, message):
        if self.read_only and message.get('method'):
            require(message['method'] in {'initialize','initialized','config/read','mcpServerStatus/list',
                'thread/read','thread/turns/list','thread/items/list'}, 'read_only_transport_input_rejected')
        from .codex import encoded
        try:
            self.driver.stdin.write((encoded(message)+'\n').encode()); await self.driver.stdin.drain()
        except (ConnectionError, OSError) as e: raise ValueError('local_channel_lost') from e

    async def receive(self):
        line = await self.driver.stdout.readline()
        return json.loads(line) if line else None

    async def close(self):
        await self.supervisor.stop()
        if self.driver.returncode is None:
            try: await asyncio.wait_for(self.driver.wait(), 2)
            except asyncio.TimeoutError:
                record = self.supervisor.adapter._get('driver:'+self.supervisor.key)
                require(identity(self.driver.pid)['birth']==record['birth'], 'local_driver_identity_changed')
                self.driver.terminate(); await asyncio.wait_for(self.driver.wait(), 2)


class LocalSupervisor:
    def __init__(self, adapter, key, route, *, read_only=False):
        self.adapter, self.key, self.route, self.read_only = adapter, key, route, read_only

    async def observe(self):
        record = self.adapter._get('local:'+self.key)
        require(record, 'local_unit_identity_missing')
        raw = await command('systemctl','--user','show',record['unit'],
            '--property=MainPID,ActiveState,SubState,InvocationID,ControlGroup,Description,Result,KillMode,ExecMainStatus')
        value = dict(line.split('=',1) for line in raw.splitlines() if '=' in line)
        pid = int(value.get('MainPID','0'))
        value['pid']=pid; value['process']=identity(pid) if pid else None; value['pids']=[]
        if value.get('ControlGroup'):
            group=Path('/sys/fs/cgroup'+value['ControlGroup'])
            require(record['unit'] in group.parts,'local_cgroup_changed')
            procs=group/'cgroup.procs'
            value['pids']=[int(p) for p in procs.read_text().split()] if procs.exists() else []
        original=record.get('native')
        value['original_pid_absent']=bool(original) and not Path('/proc',str(original['pid'])).exists()
        if pid:
            require(value.get('Description')==record['name'] and value.get('InvocationID')
                    and value.get('KillMode')=='control-group','local_unit_identity_changed')
            if record.get('invocation_id'): require(value['InvocationID']==record['invocation_id'],'local_unit_identity_changed')
            if original: require(value['process']==original,'local_native_identity_changed')
            else:
                require(value['process']['cwd']==self.route['workspace'] and value['process']['uid']==os.getuid(), 'local_native_identity_changed')
            # Public native record is independent from the pipe driver.
            public=self.adapter._get('process:'+self.key)
            if original and public:
                require(public.get('pid')==original['pid'] and public.get('birth')==original['birth'],'process_identity_changed')
        else:
            if value.get('InvocationID') and record.get('invocation_id'):
                require(value['InvocationID']==record['invocation_id'],'local_unit_identity_changed')
        if value.get('InvocationID') and not record.get('invocation_id'):
            require(value.get('Description')==record['name'], 'local_unit_identity_changed')
            self.adapter._update('local:'+self.key,invocation_id=value['InvocationID'],control_group=value.get('ControlGroup'))
        self.adapter._update('local:'+self.key,observation=value)
        return value

    async def start(self):
        from .codex import overlay_arguments, process_overlay
        require(self.adapter._get('local:'+self.key) is None,'local_unit_creation_already_requested')
        state=self.adapter._get('job:'+self.key)
        now=time.time()
        deadline=(now+min(10,self.adapter.timeout+2) if self.read_only else
            (state['created_at']+state['limits']['max_runtime_seconds'] if state else now+30))
        remaining=deadline-now; launch=min(2,remaining/4); grace=self.adapter.grace
        runtime=remaining-2*launch-grace
        require(runtime>0,'local_budget_too_small')
        name='gtd-codex-local-'+uuid.uuid4().hex
        record={'name':name,'unit':name+'.service','deadline':deadline,'start_seconds':launch,
            'runtime_seconds':runtime,'grace':grace,'read_only':self.read_only,'status':'creation_requested'}
        with self.adapter.store.transaction():
            require(self.adapter._get('local:'+self.key) is None,'local_unit_creation_already_requested')
            self.adapter._put('local:'+self.key,record)
        env={k:os.environ[k] for k in ('HOME','PATH','LANG','LC_ALL','TZ') if k in os.environ}
        env['CODEX_HOME']=self.adapter.config['codex_home']
        # env -i passes only the existing local adapter allowlist to the unit.
        args=['systemd-run','--user','--quiet','--pipe','--wait','--unit='+record['unit'],*properties(record),
            '--property=WorkingDirectory='+self.route['workspace'],'/usr/bin/env','-i',
            *[k+'='+v for k,v in sorted(env.items())],str(Path(self.adapter.config['binary']).resolve(strict=True)),
            'app-server','--strict-config','--stdio',*overlay_arguments(process_overlay(self.route))]
        binary=Path(self.adapter.config['binary']).resolve(strict=True)
        with binary.open('rb') as stream: prefix=stream.readline(512)
        executable=str(Path(prefix[2:].decode().strip().split()[0]).resolve()) if prefix.startswith(b'#!') else str(binary)
        driver=await asyncio.create_subprocess_exec(*args,cwd=self.route['workspace'],stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.DEVNULL,start_new_session=True,limit=8*1024*1024)
        self.adapter._update('driver:'+self.key,**identity(driver.pid))
        try:
            until=min(deadline,time.time()+launch)
            while time.time()<until:
                observed=await self.observe()
                ready=observed['pid'] and observed['process']['exe']==executable
                if ready:
                    cmdline=(Path('/proc',str(observed['pid']))/'cmdline').read_bytes().split(b'\0')
                    ready=str(binary).encode() in cmdline
                if ready:
                    self.adapter._update('local:'+self.key,native=observed['process'],invocation_id=observed['InvocationID'],
                        control_group=observed['ControlGroup'],status='running')
                    self.adapter._update('process:'+self.key,**observed['process'],status='running',unit=record['unit'],
                        requested_at=now)
                    return LocalChannel(self,driver,self.read_only)
                if driver.returncode is not None: break
                await asyncio.sleep(.01)
            raise ValueError('local_unit_start_unconfirmed')
        except (OSError,ValueError,asyncio.TimeoutError):
            try: await self.stop()
            finally:
                if driver.returncode is None:
                    driver.terminate()
                    try: await asyncio.wait_for(driver.wait(),1)
                    except asyncio.TimeoutError: driver.kill();await driver.wait()
            raise

    async def stop(self):
        record=self.adapter._get('local:'+self.key)
        require(record,'local_unit_identity_missing')
        if record.get('contained'): return record['observation']
        observed=await self.observe()
        if observed['pid'] or observed['pids']:
            # Creation ACK recovery may bind the authentic unit once, never start it again.
            if observed['pid'] and not record.get('native'):
                self.adapter._update('local:'+self.key,native=observed['process'],invocation_id=observed['InvocationID'],control_group=observed['ControlGroup'])
            await command('systemctl','--user','stop',record['unit'])
            observed=await self.observe()
        record=self.adapter._get('local:'+self.key)
        never_dispatched=not record.get('native') and record['status']=='creation_requested'
        require(not observed['pid'] and not observed['pids'] and (observed['original_pid_absent'] or never_dispatched), 'local_closure_unconfirmed')
        self.adapter._update('local:'+self.key,contained=True,status='contained',observation=observed)
        if record.get('native'):
            self.adapter._update('process:'+self.key,status='exited',returncode=int(observed.get('ExecMainStatus','0')))
        return observed
