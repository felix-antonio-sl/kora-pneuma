"""Actual remote adapter/router/worker; SSH fixture and bounded local WS backend.

The fixed evidence helper runs as a real local subprocess against synthetic
remote files. No real SSH or LLM, no global config/auth access.
"""
import asyncio
import copy
from datetime import datetime, timezone
import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from aiohttp import web
from runtime_location import RUNTIME
import test_codex_remote as remote_tests

SCRIPT=Path(__file__).resolve().parents[2]/'scripts/gtd_codex_remote_work_probe.py'
spec=importlib.util.spec_from_file_location('remote_work_probe',SCRIPT)
probe=importlib.util.module_from_spec(spec);spec.loader.exec_module(probe)
FIX='def clamp(value, lower, upper):\n    if lower > upper:\n        raise ValueError("reversed bounds")\n    return min(upper, max(lower, value))\n'


class RemoteWorkProbeTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        self.home=self.root/'home';self.home.mkdir(mode=0o700)
        (self.home/'config.toml').write_text('model="synthetic"\n')
        self.workspace=self.root/'workspace';self.workspace.mkdir(mode=0o700)
        for name,value in probe.SEED.items():(self.workspace/name).write_text(value)
        self.private=self.root/'r';self.private.mkdir(mode=0o700)
        self.binary=self.root/'native';self.binary.write_text('synthetic binary pin');self.binary.chmod(0o700)
        self.case=self.root/'case';self.configfile=self.root/'probe.json'
        self.fixture=self.root/'ssh-state.json';self.fixture.write_text(json.dumps({'units':{},'calls':[]}))
        self.fake_ssh=self.root/'ssh'
        # Execute the literal fixed helper supplied by the harness, not a fake
        # success. Adapter control operations still use the existing SSH fixture.
        program=remote_tests.FAKE_SSH.replace("q=json.load(sys.stdin);state=json.loads(fixture.read_text());", "q=json.load(sys.stdin)\n if q['op'] in ('snapshot','test'):\n  import subprocess,shlex\n  p=subprocess.run([sys.executable,'-c',shlex.split(sys.argv[-1])[2]],input=json.dumps(q).encode(),stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)\n  sys.stdout.buffer.write(p.stdout);sys.exit(p.returncode)\n state=json.loads(fixture.read_text());")
        program=program.replace("if state.get('lost_ack'):","if state.get('lost_ack') or (state.get('lost_work_ack') and len(state['units'])>1):")
        self.fake_ssh.write_text('#!'+sys.executable+'\n'+program);self.fake_ssh.chmod(0o700)
        self.route={'host':'ssh','profile':'synthetic','workspace':str(self.workspace),'model':'gpt-6-astra',
            'provider':'openai','effort':'low','base_instructions':'Synthetic only.','developer_instructions':'No external effects.',
            'instruction_sources':probe.contract.instruction_manifest(self.workspace),
            'process_overlay':{'version':1,'disabled_mcp_servers':[]},'remote':{'ssh_alias':'fixture',
            'hostname':os.uname().nodename,'uid':os.getuid(),'binary':str(self.binary),'binary_sha256':probe.file_hash(self.binary),
            'codex_home':str(self.home),'private_root':str(self.private),'max_runtime_seconds':12}}
        self.config={'case_dir':str(self.case),'runtime_root':str(RUNTIME),'runtime_manifest':probe.contract.source_manifest(RUNTIME),
            'core_hostname':os.uname().nodename,'core_uid':os.getuid(),'native_config_sha256':probe.file_hash(self.home/'config.toml'),
            'actors':{'owner':'probe-owner','principal':'probe-principal','executor':'probe-executor'},
            'campaign':{'id':'fixed-synthetic','period_start':datetime.now(timezone.utc).isoformat(),'period_seconds':3600,
                'max_cost_usd':1,'max_runtime_seconds':12},'reservation':{'max_cost_usd':1,'max_runtime_seconds':12},
            'codex':{'routes':{'worker':self.route},'request_timeout_seconds':1,'shutdown_grace_seconds':.1}}
        self.save()
        self.methods=[];self.turn=None;self.connections=0;self.turn_connection=None
        self.replacement=FIX;self.break_sentinel=False;self.lost_turn=False;self.immediate=False;self.sockets=[]
        async def handler(request):
            from gtd_felix.codex import process_overlay
            ws=web.WebSocketResponse();await ws.prepare(request);self.sockets.append(ws)
            self.connections+=1;connection=self.connections
            async for message in ws:
                q=json.loads(message.data);method=q.get('method');p=q.get('params',{});self.methods.append(method)
                if 'id' not in q:continue
                result={}
                if method=='config/read':result={'config':process_overlay(self.route)}
                elif method=='mcpServerStatus/list':result={'data':[],'nextCursor':None}
                elif method=='thread/start':result={'thread':{'id':'exact-thread','turns':[]},'model':'gpt-6-astra',
                    'modelProvider':'openai','reasoningEffort':'low','cwd':str(self.workspace),'approvalPolicy':'never',
                    'approvalsReviewer':'user','sandbox':{'type':'workspaceWrite','writableRoots':[str(self.workspace)],
                    'networkAccess':False,'excludeTmpdirEnvVar':True,'excludeSlashTmp':True},
                    'instructionSources':list(self.route['instruction_sources'])}
                elif method=='turn/start':
                    self.turn_connection=connection
                    (self.workspace/'clamp.py').write_text(self.replacement)
                    if self.break_sentinel:(self.workspace/'concurrent_sentinel.txt').write_text('other author damaged')
                    self.turn={'id':'exact-turn','status':'completed' if self.immediate else 'inProgress','durationMs':1,
                        'items':[{'type':'userMessage','id':'u','clientId':p['clientUserMessageId'],'content':p['input']},
                                 {'type':'agentMessage','id':'answer','phase':'final_answer','text':'Synthetic native report.'}]}
                    if self.lost_turn:continue
                    result={'turn':self.turn}
                elif method=='thread/read':
                    self.assertEqual(p['threadId'],'exact-thread');result={'thread':{'id':'exact-thread'}}
                elif method=='thread/turns/list':
                    if connection!=self.turn_connection:self.turn['status']='completed'
                    result={'data':[self.turn],'nextCursor':None}
                elif method=='turn/interrupt':self.turn['status']='interrupted'
                await ws.send_json({'id':q['id'],'result':result})
            return ws
        app=web.Application();app.router.add_get('/',handler);self.server=web.AppRunner(app);await self.server.setup()
        self.site=web.UnixSite(self.server,str(self.root/'native.sock'));await self.site.start()
        self.patches=[patch.object(probe,'SSH',str(self.fake_ssh)),patch('gtd_felix.codex_remote.SSH',str(self.fake_ssh))]
        for p in self.patches:p.start()

    def save(self):self.configfile.write_text(json.dumps(self.config));self.configfile.chmod(0o600)

    async def asyncTearDown(self):
        for ws in self.sockets:await ws.close()
        await self.server.cleanup()
        for p in self.patches:p.stop()
        self.temp.cleanup()

    def calls(self,operation):return [c for c in json.loads(self.fixture.read_text())['calls'] if c['op']==operation]

    async def test_default_description_has_no_ssh_no_case_no_inference(self):
        result=await probe.run(self.configfile)
        self.assertEqual(result['status'],'DESCRIPTION_READY',result)
        self.assertFalse(self.case.exists());self.assertEqual(self.calls('validate'),[]);self.assertEqual(self.methods,[])

    async def test_preflight_red_baseline_discovery_zero_turns(self):
        result=await probe.run(self.configfile,preflight=True)
        self.assertEqual(result['status'],'PREFLIGHT_READY',result)
        self.assertEqual(result['dispatch_counts']['turn/start'],0)
        self.assertTrue(result['remote_closure_verified'])
        self.assertIsNone(json.loads((self.case/'state.json').read_text())['job_id'])
        config_before=self.configfile.read_bytes()
        worked=await probe.run(self.configfile,work=True)
        self.assertEqual(worked['status'],'TECHNICAL_CRITERIA_PASS',worked)
        self.assertEqual(self.configfile.read_bytes(),config_before)
        self.assertEqual(worked['dispatch_counts']['turn/start'],1)
        self.assertTrue(worked['remote_closure_verified'])

    async def test_remote_delivery_reconnect_report_and_recovery_are_distinct(self):
        result=await probe.run(self.configfile,work=True)
        self.assertEqual(result['status'],'TECHNICAL_CRITERIA_PASS',result)
        self.assertEqual(result['remote_delivery'],'VERIFIED')
        self.assertEqual((self.workspace/'clamp.py').read_text(),FIX)
        self.assertEqual(result['technical_checks']['exit_code'],0)
        self.assertEqual(result['gtd_native_report_integration'],'integrated')
        self.assertEqual(result['principal_assessment'],'NOT_RUN')
        self.assertEqual(result['material_kind'],'native_execution_report_not_remote_file')
        self.assertTrue(result['reconnect']['verified']);self.assertTrue(result['remote_closure_verified'])
        self.assertEqual(result['reconnect']['before_native']['native_status'],'running')
        self.assertTrue(result['reconnect']['before_unit']['pid'])
        self.assertEqual(result['reconnect']['before'],result['reconnect']['after'])
        starts=len(self.calls('start'));self.assertEqual(starts,2) # discovery + one work unit
        self.assertEqual(result['dispatch_counts'],{'thread/start':1,'thread/resume':0,'turn/start':1})
        self.assertTrue(all(v['pid_absent'] for v in result['ssh_channels']))
        again=await probe.run(self.configfile,recover=True)
        self.assertEqual(again['status'],'TECHNICAL_CRITERIA_PASS',again)
        self.assertEqual(again['job_id'],result['job_id']);self.assertEqual(len(again['materials']),1)
        self.assertEqual(again['work_submissions_requested'],0);self.assertEqual(len(self.calls('start')),starts)
        self.assertEqual(self.methods.count('turn/start'),1)

    async def test_finished_before_disconnect_is_not_reconnect_evidence(self):
        self.immediate=True
        result=await probe.run(self.configfile,work=True)
        self.assertEqual(result['status'],'PARTIAL_RECONNECT_NOT_OBSERVED',result)
        self.assertFalse(result.get('reconnect'))
        self.assertEqual(result['remote_delivery'],'VERIFIED')

    async def test_lost_turn_ack_never_repeats_submission(self):
        self.lost_turn=True
        result=await probe.run(self.configfile,work=True)
        self.assertEqual(result['status'],'TECHNICAL_CRITERIA_PASS',result)
        self.assertEqual(self.methods.count('turn/start'),1)
        self.assertTrue(result['reconnect']['verified'])

    async def test_corrupt_sentinel_blocks_integration(self):
        self.break_sentinel=True
        result=await probe.run(self.configfile,work=True)
        self.assertEqual(result['status'],'BLOCKED',result)
        self.assertEqual(result['gtd_native_report_integration'],'NOT_RUN')
        self.assertTrue(result['remote_closure_verified'])

    async def test_native_completion_with_wrong_code_does_not_integrate(self):
        self.replacement='def clamp(value, lower, upper):\n    return upper\n'
        result=await probe.run(self.configfile,work=True)
        self.assertEqual(result['reason'],'workspace_criteria_failed',result)
        self.assertNotEqual(result['technical_checks']['exit_code'],0)
        self.assertEqual(result['gtd_native_report_integration'],'NOT_RUN')

    async def test_existing_reservation_requires_recover_without_new_start(self):
        await probe.run(self.configfile,work=True)
        starts=len(self.calls('start'))
        result=await probe.run(self.configfile,work=True)
        self.assertEqual(result['reason'],'existing_job_requires_recover',result)
        self.assertEqual(len(self.calls('start')),starts);self.assertEqual(self.methods.count('turn/start'),1)

    async def test_fixed_helper_rejects_links_extra_files_ast_and_changed_snapshot(self):
        snapshot=await probe.remote_call(self.config,'snapshot')
        contents=probe.verify_snapshot(snapshot);hashes={n:probe.sha(raw) for n,raw in contents.items()}
        (self.workspace/'clamp.py').write_text(FIX)
        with self.assertRaisesRegex(ValueError,'remote_evidence_unconfirmed'):
            await probe.remote_call(self.config,'test',hashes)
        (self.workspace/'clamp.py').write_text('import os\n')
        with self.assertRaisesRegex(ValueError,'target_function_only'):
            self.case.mkdir(mode=0o700);await probe.check_workspace(self.config,self.case,'unsafe')
        (self.workspace/'clamp.py').unlink();(self.workspace/'clamp.py').symlink_to(self.home/'config.toml')
        with self.assertRaisesRegex(ValueError,'remote_evidence_unconfirmed'):await probe.remote_call(self.config,'snapshot')
        (self.workspace/'clamp.py').unlink();(self.workspace/'clamp.py').write_text(probe.SEED['clamp.py'])
        (self.workspace/'unexpected').write_text('extra')
        with self.assertRaisesRegex(ValueError,'remote_evidence_unconfirmed'):await probe.remote_call(self.config,'snapshot')

    async def test_pins_and_budget_are_enforced_before_ssh(self):
        for change in ('core','runtime','budget'):
            config=copy.deepcopy(self.config)
            if change=='core':config['core_hostname']='different-core'
            if change=='runtime':config['runtime_manifest']={}
            if change=='budget':config['reservation']['max_runtime_seconds']=121
            with self.subTest(change=change),self.assertRaises(ValueError):probe.validate_config(config)
        self.assertEqual(self.methods,[])

    async def test_remote_config_drift_and_unapproved_global_fail_before_dispatch(self):
        (self.home/'config.toml').write_text('changed')
        result=await probe.run(self.configfile,work=True)
        self.assertEqual(result['status'],'BLOCKED');self.assertNotIn('turn/start',self.methods)

    def test_snapshot_digest_mismatch_cannot_become_evidence(self):
        value={'files':{n:{'base64':'eA==','size':1,'sha256':'0'*64} for n in probe.SEED}}
        with self.assertRaisesRegex(ValueError,'remote_evidence_hash_mismatch'):probe.verify_snapshot(value)

    async def test_lost_unit_ack_recover_never_creates_alternative_or_submits(self):
        value=json.loads(self.fixture.read_text());value['lost_work_ack']=True;self.fixture.write_text(json.dumps(value))
        result=await probe.run(self.configfile,work=True)
        self.assertEqual(result['status'],'BLOCKED',result)
        self.assertEqual(result['reason'],'native_success_unconfirmed',result)
        self.assertFalse(result['final_job']['terminal'])
        self.assertEqual(len(self.calls('start')),2)
        self.assertNotIn('turn/start',self.methods)
        recovered=await probe.run(self.configfile,recover=True)
        self.assertEqual(recovered['job_id'],result['job_id'])
        self.assertEqual(recovered['status'],'BLOCKED')
        self.assertEqual(recovered['work_submissions_requested'],0)
        self.assertEqual(len(self.calls('start')),2)
        self.assertNotIn('turn/start',self.methods)
        self.assertTrue(recovered['remote_closure_verified'])

    async def test_remote_hardlink_global_override_and_global_source_rejected(self):
        (self.root/'hardlink').hardlink_to(self.workspace/'clamp.py')
        with self.assertRaisesRegex(ValueError,'remote_evidence_unconfirmed'):await probe.remote_call(self.config,'snapshot')
        (self.root/'hardlink').unlink()
        for name in ('AGENTS.md','AGENTS.override.md'):
            with self.subTest(name=name):
                (self.home/name).write_text('unapproved')
                with self.assertRaisesRegex(ValueError,'remote_evidence_unconfirmed'):await probe.remote_call(self.config,'snapshot')
                (self.home/name).unlink()
