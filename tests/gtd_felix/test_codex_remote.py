import unittest
from runtime_location import RUNTIME
import sys
sys.path.insert(0,str(RUNTIME))
from gtd_felix.codex_remote import validate_remote_route

class RemoteRouteTests(unittest.TestCase):
    def test_explicit_remote_pins_required(self):
        with self.assertRaises(ValueError):validate_remote_route({'host':'ssh','workspace':'/work','remote':{}})

import asyncio
import copy
import hashlib
import json
import os
from pathlib import Path
import time
from unittest.mock import patch
import aiohttp
from aiohttp import web
from gtd_felix.codex import CodexAdapter, process_overlay
from gtd_felix.codex_remote import RemoteTransport, HELPER
import test_codex as local_tests

FAKE_SSH = r'''
import asyncio,json,os,sys,time
from pathlib import Path
root=Path(__file__).parent; fixture=root/'ssh-state.json'
if '-N' in sys.argv:
 local,remote=sys.argv[sys.argv.index('-L')+1].split(':',1)
 async def main():
  async def forward(reader,writer):
   state=json.loads(fixture.read_text());assert any(i['socket']==remote for i in state['units'].values())
   r,w=await asyncio.open_unix_connection(str(root/'native.sock'))
   async def copy(a,b):
    try:
     while data:=await a.read(65536):b.write(data);await b.drain()
    finally:b.close()
   await asyncio.gather(copy(reader,w),copy(r,writer),return_exceptions=True)
  server=await asyncio.start_unix_server(forward,path=local);os.chmod(local,0o600)
  async with server:await server.serve_forever()
 asyncio.run(main())
else:
 q=json.load(sys.stdin);state=json.loads(fixture.read_text());op=q['op'];state['calls'].append({'op':op,'identity':q.get('identity')})
 def persist():fixture.write_text(json.dumps(state))
 if state.get('deny_validate') and q.get('for_model'):persist();sys.exit(1)
 if op=='validate':persist();print(json.dumps({'uid':q['remote']['uid'],'hostname':q['remote']['hostname'],'boot_id':'00000000-0000-0000-0000-000000000000','monotonic':time.monotonic()}));sys.exit(0)
 identity=q['identity'];name=identity['name']
 if op=='start':
  assert name not in state['units'];state['units'][name]={**identity,'InvocationID':'inv-'+name,'pid':900001,'birth':'synthetic-birth','ControlGroup':'/synthetic/'+identity['unit'],'Description':name,'KillMode':'control-group','uid':q['remote']['uid'],'hostname':q['remote']['hostname'],'socket':identity['socket'],'active':True,'runtime_seconds':identity['runtime_ceiling']}
  if state.get('lost_ack'):persist();sys.exit(1)
 unit=state['units'].get(name)
 if not unit: persist();sys.exit(1)
 if op=='stop':
  assert identity['invocation_id']==unit['InvocationID'] and identity['birth']==unit['birth'];unit['active']=False
 result={**unit,'socket':{'uid':unit['uid'],'mode':384,'inode':5},'cgroup_pids':[900001]}
 if not unit['active']:result.update(pid=0,birth=None,cgroup_pids=[],socket=None,owned_pid_absent=True)
 result.update(state.get('override',{}));persist();print(json.dumps(result))
'''


class RemoteIntegrationTests(unittest.IsolatedAsyncioTestCase):
    save = local_tests.CodexTests.save
    reserve = local_tests.CodexTests.reserve

    async def asyncSetUp(self):
        await local_tests.CodexTests.asyncSetUp(self)
        self.fake_ssh=self.root/'ssh';self.fake_ssh.write_text('#!'+sys.executable+'\n'+FAKE_SSH);self.fake_ssh.chmod(0o700)
        self.fixture=self.root/'ssh-state.json';self.fixture.write_text(json.dumps({'units':{},'calls':[]}))
        self.private=self.root/'r';self.private.mkdir(mode=0o700)
        self.route.update(host='ssh',process_overlay={'version':1,'disabled_mcp_servers':[]},remote={
            'ssh_alias':'synthetic','hostname':'synthetic','uid':os.getuid(),'binary':str(self.binary),
            'binary_sha256':self.config['binary_sha256'],'codex_home':str(self.home),'private_root':str(self.private),'max_runtime_seconds':20})
        self.control.register_bot('felix','remote-registration',dict(id='codex',state='available',source_urn='urn:test:codex',host='ssh',profile='synthetic',capabilities=['prepare_private'],item_id=self.item['id'],probe_evidence='fixture'))
        self.config['routes']['codex']=self.route;self.config['request_timeout_seconds']=2
        self.adapter=CodexAdapter(self.control,self.config)
        self.methods=[];self.turn=None;self.thread='exact-thread';self.sockets=[]
        async def handler(request):
            ws=web.WebSocketResponse();await ws.prepare(request);self.sockets.append(ws)
            async for message in ws:
                q=json.loads(message.data);method=q.get('method');p=q.get('params',{});self.methods.append(method)
                if 'id' not in q:continue
                result={}
                if method=='config/read':
                    effective=copy.deepcopy(self.settings['effective'])
                    effective.update(process_overlay(self.route));result={'config':effective}
                elif method=='mcpServerStatus/list':result={'data':[],'nextCursor':None}
                elif method=='thread/start':result={'thread':{'id':self.thread,'turns':[]},**self.settings['thread_config']}
                elif method=='turn/start':
                    self.turn={'id':'exact-turn','status':'inProgress','durationMs':1,'items':[{'type':'userMessage','id':'u','clientId':p['clientUserMessageId'],'content':p['input']}]};result={'turn':self.turn}
                elif method=='thread/read':self.assertEqual(p['threadId'],self.thread);result={'thread':{'id':self.thread}}
                elif method=='thread/turns/list':result={'data':[self.turn],'nextCursor':None}
                elif method=='turn/steer':result={'turnId':'exact-turn'}
                elif method=='turn/interrupt':self.turn['status']='interrupted'
                await ws.send_json({'id':q['id'],'result':result})
            return ws
        app=web.Application();app.router.add_get('/',handler);self.server=web.AppRunner(app);await self.server.setup()
        self.site=web.UnixSite(self.server,str(self.root/'native.sock'));await self.site.start()
        self.patch=patch('gtd_felix.codex_remote.SSH',str(self.fake_ssh));self.patch.start()

    def modify(self,**fields):
        value=json.loads(self.fixture.read_text());value.update(fields);self.fixture.write_text(json.dumps(value))

    def remote_calls(self,op):return [x for x in json.loads(self.fixture.read_text())['calls'] if x['op']==op]

    async def asyncTearDown(self):
        await self.adapter.close()
        for ws in self.sockets:await ws.close()
        await self.server.cleanup();self.patch.stop();self.service.close();self.temp.cleanup()

    async def test_live_disconnect_reconnect_same_ids_deadline_no_dispatch(self):
        job=self.reserve();result=await self.adapter.submit(job,'synthetic')
        self.assertEqual(result['native_status'],'running',result)
        original=self.adapter._get('remote:'+job)
        self.assertEqual(self.adapter.connections[job].process,None)
        await self.adapter.close() # SSH only; unit remains active.
        self.assertTrue(next(iter(json.loads(self.fixture.read_text())['units'].values()))['active'])
        self.adapter=CodexAdapter(self.control,self.config)
        result=await self.adapter.reconcile(job)
        self.assertFalse(result['terminal']);self.assertEqual(result['turn_id'],'exact-turn')
        self.assertEqual(self.adapter._get('remote:'+job)['deadline'],original['deadline'])
        self.assertEqual(len(self.remote_calls('start')),1)
        self.assertEqual(self.methods.count('turn/start'),1);self.assertEqual(self.methods.count('thread/start'),1)
        self.assertNotIn('thread/resume',self.methods)
        await self.adapter.stop(job);result=await self.adapter.poll(job)
        self.assertTrue(result['terminal']);self.assertEqual(result['native_status'],'cancelled')

    async def test_lost_start_ack_reconciles_unit_without_second_start(self):
        self.modify(lost_ack=True);job=self.reserve()
        result=await self.adapter.submit(job,'synthetic');self.assertFalse(result['terminal'])
        identity=self.adapter._get('remote:'+job);self.assertIsNotNone(identity)
        self.modify(lost_ack=False)
        transport=RemoteTransport(self.adapter,job,self.route)
        recovered=await transport.ensure()
        self.assertEqual(recovered['name'],identity['name']);self.assertEqual(recovered['deadline'],identity['deadline'])
        self.assertEqual(len(self.remote_calls('start')),1);self.assertNotIn('turn/start',self.methods)
        await transport.stop()

    async def test_reused_identity_rejected_and_no_stop_collateral(self):
        job=self.reserve();await self.adapter.submit(job,'synthetic');await self.adapter._close_process(job)
        for overrides in ({'InvocationID':'foreign'},{'uid':9999},{'boot_id':'foreign'},{'birth':'reused'},{'ControlGroup':'/foreign'}, {'runtime_seconds':121}, {'socket':{'uid':os.getuid(),'mode':511,'inode':5}}):
            with self.subTest(overrides=overrides):
                self.modify(override=overrides)
                self.assertEqual((await self.adapter.reconcile(job))['status'],'uncertain')
                self.assertEqual((await self.adapter.stop(job))['status'],'uncertain')
        self.assertEqual(len(self.remote_calls('stop')),0)

    async def test_dead_unit_never_native_terminal_and_no_restart(self):
        job=self.reserve();await self.adapter.submit(job,'synthetic');await self.adapter._close_process(job)
        self.modify(override={'pid':0,'birth':None,'cgroup_pids':[],'socket':None})
        result=await self.adapter.reconcile(job)
        self.assertFalse(result['terminal']);self.assertFalse(self.control.get_job(job)['terminal'])
        self.assertEqual(len(self.remote_calls('start')),1)

    async def test_instruction_change_denies_input_allows_exact_read_stop(self):
        job=self.reserve();await self.adapter.submit(job,'synthetic')
        self.modify(deny_validate=True)
        result=await self.adapter.steer(job,'new input','once');self.assertFalse(result['terminal'])
        self.assertNotIn('turn/steer',self.methods)
        await self.adapter._close_process(job)
        self.assertEqual((await self.adapter.reconcile(job))['native_status'],'running')
        await self.adapter.stop(job);self.assertEqual((await self.adapter.poll(job))['native_status'],'cancelled')

    async def test_deadline_and_revoke_block_new_input_without_renewal(self):
        job=self.reserve();await self.adapter.submit(job,'synthetic')
        self.adapter._update('remote:'+job,deadline=time.time()-1)
        result=await self.adapter.steer(job,'late','late');self.assertFalse(result['terminal']);self.assertNotIn('turn/steer',self.methods)
        await self.adapter._close_process(job)
        result=await self.adapter.reconcile(job);self.assertFalse(result['terminal'])
        self.assertEqual(len(self.remote_calls('start')),1)

    async def test_private_discovery_no_turn_and_stops_own_unit(self):
        # Remote pins replace local binary/home validation, not a fake local Path check.
        for key in ('binary','binary_sha256','codex_home'): self.adapter.config.pop(key)
        result=await self.adapter.discover('codex');self.assertEqual(result['status'],'ready',result)
        self.assertEqual(len(self.remote_calls('stop')),1)
        self.assertNotIn('turn/start',self.methods)

    async def test_actual_helper_validates_remote_files_not_local_path_assumptions(self):
        import subprocess
        route=copy.deepcopy(self.route);route['remote']['hostname']=os.uname().nodename
        source=self.workspace/'AGENTS.md';source.write_text('explicit synthetic instructions')
        route['instruction_sources']={str(source):hashlib.sha256(source.read_bytes()).hexdigest()}
        async def call(value,for_model=True):
            p=await asyncio.create_subprocess_exec(sys.executable,'-c',HELPER,stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.DEVNULL)
            out,_=await p.communicate(json.dumps({'op':'validate','remote':value['remote'],'route':value,'for_model':for_model}).encode())
            return p.returncode,out
        self.assertEqual((await call(route))[0],0)
        source.write_text('owner changed source')
        self.assertNotEqual((await call(route))[0],0)
        self.assertEqual((await call(route,False))[0],0)
        for key,value in [('uid',os.getuid()+1),('hostname','foreign'),('binary_sha256','0'*64),('codex_home',str(self.home/'..'/'native'))]:
            modified=copy.deepcopy(route);modified['remote'][key]=value
            with self.subTest(key=key):self.assertNotEqual((await call(modified,False))[0],0)

    async def test_human_edit_blocks_steer_but_stop_read_preserved(self):
        job=self.reserve();await self.adapter.submit(job,'synthetic')
        current=self.service.get_item(self.item['id'])
        self.service.execute('felix', {'operation_id':'human-change','action':'edit','item_id':self.item['id'],'expected_version':current['version'],'fields':{'text':'Changed human request'}})
        result=await self.adapter.steer(job,'stale input','stale')
        self.assertFalse(result['terminal']);self.assertNotIn('turn/steer',self.methods)
        await self.adapter.stop(job)
        observed=await self.adapter.poll(job)
        self.assertEqual(observed['native_status'],'cancelled')

    async def test_native_terminal_waits_for_remote_closure_and_recovers_without_replay(self):
        job=self.reserve();await self.adapter.submit(job,'synthetic')
        # Native interruption arrives while remote closure cannot yet be proved.
        self.modify(override={'owned_pid_absent':False})
        await self.adapter.stop(job)
        result=await self.adapter.poll(job)
        self.assertFalse(result['terminal']);self.assertFalse(self.control.get_job(job)['terminal'])
        self.assertIsNotNone(self.adapter._get('job:'+job)['pending_observation'])
        await self.adapter.close();self.adapter=CodexAdapter(self.control,self.config)
        self.modify(override={})
        before=list(self.methods)
        result=await self.adapter.reconcile(job)
        self.assertTrue(result['terminal']);self.assertEqual(result['native_status'],'cancelled')
        self.assertEqual(self.methods,before)
        self.assertEqual(len(self.remote_calls('start')),1)
        self.assertEqual(self.control.get_job(job)['charged_cost_usd'],2)

    async def test_remote_result_is_identified_material_not_workspace_integration(self):
        job=self.reserve();await self.adapter.submit(job,'synthetic')
        self.turn.update(status='completed',items=[
            {'type':'agentMessage','id':'answer','phase':'final_answer','text':'Synthetic final result'},
            {'type':'commandExecution','id':'cmd','status':'completed','command':'python -m unittest',
             'cwd':self.route['workspace'],'exitCode':0,'aggregatedOutput':'1 test OK'},
            {'type':'reasoning','id':'private','text':'must not persist'}])
        result=await self.adapter.poll(job)
        self.assertTrue(result['terminal']);self.assertEqual(result['integration'],'not_performed')
        body=json.loads((self.service.data_dir/result['artifact']['path']).read_text())
        self.assertEqual(body['workspace_integration'],'not_verified')
        self.assertEqual(body['assessment'],'pending_principal')
        self.assertEqual(body['execution'][0]['exitCode'],0)
        self.assertNotIn('must not persist',json.dumps(body))
        self.assertTrue(self.adapter._get('remote:'+job)['contained'])

    async def test_real_helper_rejects_delayed_activation_despite_wall_clock_skew(self):
        import shutil
        import uuid
        native=self.root/'native-python';shutil.copyfile(Path(sys.executable).resolve(),native);native.chmod(0o700)
        marker=self.workspace/'executed'
        script=self.workspace/'app-server';script.write_text('from pathlib import Path\nimport time\nPath("executed").write_text("late")\ntime.sleep(20)\n')
        route=copy.deepcopy(self.route)
        route['remote'].update(hostname=os.uname().nodename,binary=str(native),binary_sha256=hashlib.sha256(native.read_bytes()).hexdigest())
        name='gtd-codex-'+uuid.uuid4().hex
        identity={'name':name,'unit':name+'.service','directory':str(self.private/name),'socket':str(self.private/name/'s'),
            'deadline':time.time()+2,'remote_deadline':time.monotonic()+2,
            'boot_id':Path('/proc/sys/kernel/random/boot_id').read_text().strip()}
        request={'op':'start','remote':route['remote'],'route':route,'identity':identity,'for_model':True,
            'grace':.1,'overlay_args':[],'sent_at':time.time(),'transport_timeout':.5}
        # Delay manager submission beyond the absolute cutoff; skew is within
        # the old sent_at tolerance. No model, auth or native Codex execution.
        prefix='''import subprocess,time
original_run=subprocess.run
original_time=time.time
time.time=lambda:original_time()-.25
def delayed(args,*a,**k):
 if args[0]=='systemd-run':time.sleep(.8)
 return original_run(args,*a,**k)
subprocess.run=delayed
'''
        try:
            p=await asyncio.create_subprocess_exec(sys.executable,'-c',prefix+HELPER,stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.PIPE)
            out,err=await asyncio.wait_for(p.communicate(json.dumps(request).encode()),5)
            self.assertEqual(p.returncode,0,err.decode())
            result=json.loads(out);self.assertEqual(result['pid'],0);self.assertEqual(result['cgroup_pids'],[])
            self.assertFalse(marker.exists())
        finally:
            p=await asyncio.create_subprocess_exec('systemctl','--user','stop',identity['unit'],stdout=asyncio.subprocess.DEVNULL,stderr=asyncio.subprocess.DEVNULL)
            await p.wait()

    async def test_real_helper_active_unit_contained_with_separate_child(self):
        import shutil
        import uuid
        native=self.root/'native-python';shutil.copyfile(Path(sys.executable).resolve(),native);native.chmod(0o700)
        script=self.workspace/'app-server';script.write_text('''import os,sys,socket,time,subprocess,json
from pathlib import Path
child=subprocess.Popen([sys.executable,'-c','import threading;threading.Event().wait()'],start_new_session=True)
Path('child.json').write_text(json.dumps({'pid':child.pid,'birth':Path('/proc',str(child.pid),'stat').read_text().rsplit(')',1)[1].split()[19]}))
s=socket.socket(socket.AF_UNIX);target=sys.argv[sys.argv.index('--listen')+1][7:];s.bind(target);os.chmod(target,0o600);time.sleep(20)
''')
        route=copy.deepcopy(self.route);route['remote'].update(hostname=os.uname().nodename,binary=str(native),binary_sha256=hashlib.sha256(native.read_bytes()).hexdigest())
        name='gtd-codex-'+uuid.uuid4().hex
        identity={'name':name,'unit':name+'.service','directory':str(self.private/name),'socket':str(self.private/name/'s'),
            'deadline':time.time()+8,'remote_deadline':time.monotonic()+8,
            'boot_id':Path('/proc/sys/kernel/random/boot_id').read_text().strip()}
        async def helper(op):
            p=await asyncio.create_subprocess_exec(sys.executable,'-c',HELPER,stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.PIPE)
            out,err=await asyncio.wait_for(p.communicate(json.dumps({'op':op,'remote':route['remote'],'route':route,'identity':identity,
                'for_model':False,'grace':.1,'overlay_args':[]}).encode()),5)
            self.assertEqual(p.returncode,0,err.decode());return json.loads(out)
        try:
            observed=await helper('start')
            for _ in range(30):
                if observed.get('pid') and observed.get('socket'):break
                await asyncio.sleep(.03);observed=await helper('observe')
            self.assertTrue(observed['socket'])
            identity.update(pid=observed['pid'],birth=observed['birth'],invocation_id=observed['InvocationID'],control_group=observed['ControlGroup'])
            child=json.loads((self.workspace/'child.json').read_text())
            self.assertIn(child['pid'],observed['cgroup_pids'])
            result=await helper('stop')
            self.assertEqual(result['cgroup_pids'],[]);self.assertTrue(result['owned_pid_absent'])
            self.assertFalse(Path('/proc',str(child['pid'])).exists())
        finally:
            p=await asyncio.create_subprocess_exec('systemctl','--user','stop',identity['unit'],stdout=asyncio.subprocess.DEVNULL,stderr=asyncio.subprocess.DEVNULL)
            await p.wait()
