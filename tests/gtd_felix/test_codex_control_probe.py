"""Work runner with a real fake-RPC process and isolated real GTD runtime copy."""
from datetime import datetime,timezone
import asyncio
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import sysconfig
import subprocess
import sys
import tempfile
import unittest
from types import SimpleNamespace
from runtime_location import RUNTIME
from test_codex import FAKE

SCRIPT=Path(__file__).resolve().parents[2]/'scripts'/'gtd_codex_control_probe.py'
spec=importlib.util.spec_from_file_location('work_probe_contract',SCRIPT)
contract=importlib.util.module_from_spec(spec);spec.loader.exec_module(contract)
FIX='def render_label():\n    return "reviewed"\n'



class TerminalReadOrderingTests(unittest.IsolatedAsyncioTestCase):
    async def check_terminal_ordering(self, connection_present):
        connections={}
        events=[]
        state={'thread_id':'thread-exact','turn_id':'turn-exact','local_supervised':True}
        async def original_monitor():
            await asyncio.sleep(.01)
            connections.pop('job',None)
            events.append('original_closed')
        async def read(method,params):
            self.assertEqual(method,'thread/turns/list')
            self.assertEqual(params,{'threadId':'thread-exact','itemsView':'full','limit':2})
            await asyncio.sleep(.02)
            if 'job' not in connections: raise ValueError('transport_lost')
            return {'data':[{'id':'turn-exact','status':'interrupted','itemsView':'full'}],'nextCursor':None}
        async def spawn(job,route):
            events.append('read_opened')
            rpc=SimpleNamespace(channel=SimpleNamespace(read_only=True),request=read)
            connections[job]=rpc
            return rpc
        async def close(job):
            if connections.pop(job,None) is not None:
                events.append('read_closed')
        if connection_present:
            connections['job']=SimpleNamespace(request=read)
        monitor=asyncio.create_task(original_monitor())
        adapter=SimpleNamespace(connections=connections,monitors={'job':monitor},terminal_tasks={},timeout=.3,grace=.1,
            _get=lambda key: state if key=='job:job' else {'contained':True},
            _job=lambda job: ({'terminal':True,'bot_id':'worker'},{}),
            _route=lambda *args,**kwargs: {},_spawn=spawn,_close_process=close)
        try:
            result=await contract.native_control_evidence(adapter,'job')
        finally:
            await monitor
        self.assertEqual(result['status'],'interrupted')
        self.assertEqual(events,['original_closed','read_opened','read_closed'])

    async def test_original_monitor_finishes_before_new_read_transport(self):
        await self.check_terminal_ordering(False)

    async def test_terminal_with_original_rpc_still_present_waits_for_closure(self):
        await self.check_terminal_ordering(True)


class ControlProbeTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        self.runtime=self.root/'runtime';shutil.copytree(RUNTIME,self.runtime)
        self.home=self.root/'native';self.home.mkdir(mode=0o700)
        (self.home/'config.toml').write_text('model="synthetic-inherited"\n');(self.home/'config.toml').chmod(0o600)
        self.binary=self.root/'fake-codex'
        program=FAKE.replace("import json,os,sys,uuid", "import json,os,sys,uuid,subprocess,time,signal,shlex,re")
        program=program.replace("'ambient_secret':", "'runner_bus_visible':any(k in os.environ for k in ('XDG_RUNTIME_DIR','DBUS_SESSION_BUS_ADDRESS')), 'ambient_secret':")
        program=program.replace("state=json.loads(statefile.read_text()) if statefile.exists() else {}", "state=json.loads(statefile.read_text()) if statefile.exists() else {}\ngate=None\nsteered=False")
        program=program.replace("  if settings.get('complete'):", "  if not settings.get('complete'):\n   text=' '.join(i['text'] for i in p['input'] if i.get('type')=='text')\n   command=shlex.split(re.search(r'First run (.*?) in the workspace',text).group(1))\n   gate=subprocess.Popen(command,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)\n  if settings.get('complete'):",1)
        program=program.replace(" elif method=='thread/read':", " elif method=='thread/read':\n  if gate and gate.poll() is not None and steered:\n   (Path.cwd()/'task.py').write_text(settings['replacement'])\n   state['turns'][0].update(status='completed')\n   state['turns'][0]['items'].append({'type':'agentMessage','id':'a1','text':'Verified synthetic oriented label','phase':'final_answer'})\n   persist()\n   gate=None")
        program=program.replace(" elif method=='turn/steer':", " elif method=='turn/steer':\n  steered=True")
        program=program.replace("  if not settings.get('ack_only'):", "  if gate and not settings.get('ack_only'):\n   gate.terminate();gate.wait(timeout=2)\n  if not settings.get('ack_only'):")
        program=program.replace(" elif method=='turn/start':", " elif method=='turn/start':\n  if settings.get('change_gate'): (Path.cwd()/'gate.py').write_text((Path.cwd()/'gate.py').read_text()+'\\n# changed\\n')")
        program=program.replace("result={'data':state['turns'],'nextCursor':settings.get('next_cursor')}", "result={'data':state['turns'],'nextCursor':settings.get('next_cursor')}\n  if gate is None and settings.get('terminal_read') and state.get('turns',[{}])[0].get('status')=='interrupted':\n   result['data']=[] if settings['terminal_read']=='missing' else [{**state['turns'][0],'id':'foreign-turn'}]")
        self.binary.write_text('#!'+sys.executable+'\n'+program);self.binary.chmod(0o700)
        self.case=self.root/'case';workspace=self.case/'workspace'
        self.config={'case_dir':str(self.case),'runtime_root':str(self.runtime),
            'actors':{'owner':'probe-owner','principal':'probe-principal','executor':'probe-executor'},
            'campaign':{'id':'synthetic-campaign','period_start':datetime.now(timezone.utc).isoformat(),'period_seconds':3600,
                'max_cost_usd':1,'max_runtime_seconds':30},'reservation':{'max_cost_usd':1,'max_runtime_seconds':5},
            'codex':{'binary':str(self.binary),'binary_sha256':hashlib.sha256(self.binary.read_bytes()).hexdigest(),
                'codex_home':str(self.home),'request_timeout_seconds':.3,'shutdown_grace_seconds':.1,
                'routes':{'worker':{'host':'local','profile':'synthetic','workspace':str(workspace),
                    'model':'gpt-6-astra','provider':'openai','effort':'low','base_instructions':'Synthetic only.',
                    'developer_instructions':'No external effects.','instruction_sources':contract.instruction_manifest(workspace),
                    'process_overlay':{'version':1,'disabled_mcp_servers':[]}}}}}
        self.configfile=self.root/'private.json';self.configfile.write_text(json.dumps(self.config));self.configfile.chmod(0o600)
        self.settings={'effective':{},'thread_config':{'model':'gpt-6-astra','modelProvider':'openai','reasoningEffort':'low',
            'cwd':str(workspace),'approvalPolicy':'never','sandbox':{'type':'workspaceWrite','writableRoots':[],
            'networkAccess':False,'excludeTmpdirEnvVar':True,'excludeSlashTmp':True},'instructionSources':[str(workspace/'AGENTS.md')]},
            'complete':False,'replacement':FIX}
        self.save()
    def save(self): (self.home/'fixture.json').write_text(json.dumps(self.settings))
    def tearDown(self): self.temp.cleanup()
    def invoke(self,*flags):
        # Only the supervising runner receives the user-bus capability. Native
        # payloads retain the runtime's separate, minimal environment allowlist.
        bus={k:os.environ[k] for k in ('XDG_RUNTIME_DIR','DBUS_SESSION_BUS_ADDRESS') if k in os.environ}
        process=subprocess.run([getattr(self,'runner_python',sys.executable),'-B',str(SCRIPT),'--config',str(self.configfile),*flags],
            env={'HOME':str(self.root),'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','PYTHONPATH':sysconfig.get_path('purelib'),**bus},capture_output=True,text=True,timeout=30)
        summary=json.loads(process.stdout.splitlines()[-1])
        self.assertIn('receipt',summary,(summary,process.stderr))
        receipt=json.loads((self.case/summary['receipt']).read_text())
        return process.returncode,receipt
    def audit(self):
        path=self.home/'audit.jsonl'
        return [json.loads(x) for x in path.read_text().splitlines()] if path.exists() else []


    def test_steer_live_gate_one_turn_and_protected_result(self):
        code,discovery=self.invoke();self.assertEqual(code,0,discovery)
        code,result=self.invoke('--steer');self.assertEqual(code,0,result)
        self.assertEqual(result['status'],'CONTROL_STEER_PASS')
        self.assertEqual(result['technical_checks']['exit_code'],0)
        self.assertEqual(result['principal_assessment'],'NOT_RUN')
        self.assertEqual(sum(x['method']=='turn/start' for x in self.audit()),1)
        self.assertEqual(sum(x['method']=='turn/steer' for x in self.audit()),1)
        code,replay=self.invoke('--steer');self.assertEqual(code,0,replay)
        self.assertEqual(sum(x['method']=='turn/start' for x in self.audit()),1)
        self.assertEqual(sum(x['method']=='turn/steer' for x in self.audit()),1)

    def test_stop_interrupt_and_gate_disappearance_recovery_no_resend(self):
        code,result=self.invoke('--stop');self.assertEqual(code,0,result)
        self.assertEqual(result['status'],'CONTROL_STOP_PASS')
        self.assertTrue(result['gate_closed'])
        self.assertEqual(result['final_job']['observations'][-1]['native_status'],'cancelled')
        self.assertEqual(result['native_control_terminal']['status'],'interrupted')
        self.assertFalse(any(x['runner_bus_visible'] for x in self.audit()))
        code,result=self.invoke('--recover');self.assertEqual(code,0,result)
        self.assertEqual(sum(x['method']=='turn/start' for x in self.audit()),1)
        self.assertEqual(sum(x['method']=='turn/interrupt' for x in self.audit()),1)

    def test_terminal_before_action_is_not_run(self):
        self.settings['complete']=True;self.save()
        code,result=self.invoke('--steer');self.assertEqual(code,2,result)
        self.assertEqual(result['status'],'NOT_RUN')
        self.assertNotIn('turn/steer',[x['method'] for x in self.audit()])
        self.assertEqual(sum(x['method']=='turn/start' for x in self.audit()),1)

    def assert_terminal_read_rejected(self, mode):
        self.settings['terminal_read']=mode;self.save()
        code,result=self.invoke('--stop')
        self.assertEqual(code,2,result)
        self.assertEqual(result['status'],'BLOCKED')
        self.assertEqual(result['reason'],'native_control_turn_mismatch')
        self.assertTrue(result['terminal'])
        self.assertTrue(all(x['pid_absent'] for x in result['native_processes']))
        self.assertEqual(sum(x['method']=='turn/start' for x in self.audit()),1)
        self.assertEqual(sum(x['method']=='turn/interrupt' for x in self.audit()),1)
        self.assertNotIn('thread/resume',[x['method'] for x in self.audit()])

    def test_terminal_readback_missing_turn_never_passes(self):
        self.assert_terminal_read_rejected('missing')

    def test_terminal_readback_foreign_turn_never_passes(self):
        self.assert_terminal_read_rejected('foreign')

    def test_stop_ack_alone_never_passes(self):
        self.settings['ack_only']=True;self.save()
        self.config['reservation']['max_runtime_seconds']=1
        self.configfile.write_text(json.dumps(self.config))
        code,result=self.invoke('--stop');self.assertEqual(code,2,result)
        self.assertNotEqual(result['status'],'CONTROL_STOP_PASS')
        self.assertFalse(result['terminal'])

    def test_pid_reuse_never_proves_current_identity(self):
        self.assertFalse(contract.identity_alive({'pid':os.getpid(),'birth':'wrong-birth'}))

    def test_protected_gate_change_prevents_control(self):
        self.settings['change_gate']=True;self.save()
        code,result=self.invoke('--steer');self.assertEqual(code,2,result)
        self.assertEqual(result['reason'],'protected_workspace_file_changed')
        self.assertNotIn('turn/steer',[x['method'] for x in self.audit()])

    def test_case_mode_cannot_change_or_redispatch(self):
        code,result=self.invoke('--steer');self.assertEqual(code,0,result)
        code,result=self.invoke('--stop');self.assertEqual(code,2,result)
        self.assertEqual(result['reason'],'case_mode_changed')
        self.assertEqual(sum(x['method']=='turn/start' for x in self.audit()),1)

    def test_copied_runner_interpreter_gate_consumes_prompt_not_path_python(self):
        copied=self.root/'copied python'
        shutil.copyfile(Path(sys.executable).resolve(),copied);copied.chmod(0o700)
        self.runner_python=str(copied)
        self.assertNotEqual(copied.resolve(),Path('/usr/bin/python3').resolve())
        code,result=self.invoke('--steer')
        self.assertEqual(code,0,{'status':result['status'],'reason':result.get('reason')})
        state=json.loads((self.case/'state.json').read_text())
        self.assertEqual(result['runner_interpreter']['path'],str(copied))
        self.assertEqual(result['runner_interpreter']['sha256'],hashlib.sha256(copied.read_bytes()).hexdigest())
        self.assertEqual(state['gate_identity']['executable'],str(copied))
        self.assertEqual(result['status'],'CONTROL_STEER_PASS')

    def test_namespace_gate_resolves_only_owned_host_pid_and_birth(self):
        proc=self.root/'proc';proc.mkdir();workspace=self.case/'workspace';workspace.mkdir(parents=True)
        nonce='a'*32
        def process(pid,parent,birth,nspid,nsgroup,children=''):
            path=proc/str(pid);path.mkdir()
            fields=['S',str(parent),'400']+['0']*16+[birth]
            (path/'stat').write_text(str(pid)+' (python) '+' '.join(fields))
            (path/'status').write_text('NSpid: '+nspid+'\nNSpgid: '+nsgroup+'\n')
            (path/'exe').symlink_to(Path(sys.executable).resolve());(path/'cwd').symlink_to(workspace)
            (path/'cmdline').write_bytes(b'python\0-B\0gate.py\0'+nonce.encode()+b'\0')
            task=path/'task'/str(pid);task.mkdir(parents=True);(task/'children').write_text(children)
        process(400,1,'100','400','400','500 501')
        process(500,400,'200','500 2','400 1')
        process(501,400,'201','501 2','400 1') # reused namespace PID is not this birth
        process(2,1,'200','2','1') # host PID 2 is outside the authorized tree
        record={'pid':2,'pgid':1,'birth':'200','nonce':nonce,'started_at':0}
        found=contract.resolve_gate(record,{'pid':400,'birth':'100'},workspace,nonce,proc)
        self.assertEqual(found['pid'],500);self.assertEqual(found['namespace_pid'],2)
        self.assertEqual(found['pgid'],400);self.assertEqual(found['namespace_pgid'],1)
        self.assertIsNone(contract.resolve_gate({**record,'birth':'missing'},{'pid':400,'birth':'100'},workspace,nonce,proc))
        with self.assertRaisesRegex(ValueError,'native_parent_reused'):
            contract.resolve_gate(record,{'pid':400,'birth':'old'},workspace,nonce,proc)
        (proc/'500/status').write_text('NSpid: 500 2\nNSpgid: 400 9\n')
        self.assertIsNone(contract.resolve_gate(record,{'pid':400,'birth':'100'},workspace,nonce,proc))

    def test_inventory_failure_records_exact_names_without_accepting_transient(self):
        workspace=self.root/'inventory';workspace.mkdir()
        for name,value in contract.SEED.items():(workspace/name).write_text(value)
        for name in contract.PROTECTED_DIRS:(workspace/name).mkdir(mode=0o700)
        extra=workspace/'.synthetic-native-temporary';extra.write_text('synthetic')
        with self.assertRaises(contract.WorkspaceInventoryError) as caught:contract.workspace_hashes(workspace)
        self.assertEqual(caught.exception.snapshot['unexpected'],[extra.name])
        self.assertEqual(caught.exception.snapshot['missing'],[])
        extra.unlink()
        self.assertEqual(set(contract.workspace_hashes(workspace)),set(contract.SEED))

    def test_protected_directories_reject_content_links_files_and_replacement(self):
        workspace=self.root/'directories';workspace.mkdir()
        for name,value in contract.SEED.items():(workspace/name).write_text(value)
        for name in contract.PROTECTED_DIRS:(workspace/name).mkdir(mode=0o700)
        expected=contract.directory_manifest(workspace)
        contract.workspace_hashes(workspace,expected)
        target=workspace/'.codex'
        (target/'config.toml').write_text('unapproved')
        with self.assertRaisesRegex(ValueError,'not_empty'):contract.workspace_hashes(workspace,expected)
        (target/'config.toml').unlink()
        target.chmod(0o755)
        with self.assertRaisesRegex(ValueError,'identity_invalid'):contract.workspace_hashes(workspace,expected)
        target.chmod(0o700)
        target.rename(self.root/'original-directory')
        target.symlink_to(self.root/'original-directory',target_is_directory=True)
        with self.assertRaisesRegex(ValueError,'identity_invalid'):contract.workspace_hashes(workspace,expected)
        target.unlink();target.write_text('')
        with self.assertRaisesRegex(ValueError,'identity_invalid'):contract.workspace_hashes(workspace,expected)
        target.unlink();target.mkdir(mode=0o700)
        with self.assertRaisesRegex(ValueError,'directory_changed'):contract.workspace_hashes(workspace,expected)
