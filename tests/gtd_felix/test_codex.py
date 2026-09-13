"""Real owned fake JSON-RPC subprocesses + real ExecutionControl; no Codex/model."""
import asyncio
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from gtd_felix import GTDService
from gtd_felix.control import ExecutionControl
from gtd_felix.codex import CodexAdapter

FAKE = r'''
import json,os,sys,uuid
from pathlib import Path
home=Path(os.environ['CODEX_HOME'])
settings=json.loads((home/'fixture.json').read_text())
import tomllib
def merge(target, values):
 for key,value in values.items():
  if isinstance(value,dict) and isinstance(target.get(key),dict):merge(target[key],value)
  else:target[key]=value
for index,arg in enumerate(sys.argv):
 if arg=='-c':merge(settings['effective'],tomllib.loads(sys.argv[index+1]))
audit=home/'audit.jsonl'
statefile=home/'native.json'
state=json.loads(statefile.read_text()) if statefile.exists() else {}
def persist(): statefile.write_text(json.dumps(state))
def send(x): print(json.dumps(x),flush=True)
for line in sys.stdin:
 q=json.loads(line); method=q.get('method'); p=q.get('params',{})
 with audit.open('a') as f: f.write(json.dumps({'method':method,'params':p,'argv':sys.argv[1:], 'ambient_secret':bool(os.environ.get('OPENAI_API_KEY'))})+'\n')
 if 'id' not in q: continue
 result={}
 if method=='initialize': result={'userAgent':'codex/0.154.0'}
 elif method=='config/read': result={'config':settings['effective'],'origins':{}}
 elif method=='mcpServerStatus/list': result={'data':settings.get('mcp',[]),'nextCursor':None}
 elif method=='thread/start':
  state={'id':'thread-'+uuid.uuid4().hex,'turns':[]};persist()
  if settings.get('lose_thread'): sys.exit(0)
  result={'thread':state,**settings['thread_config']}
 elif method=='thread/resume':
  state=json.loads(statefile.read_text());result={'thread':state,**settings['thread_config']}
 elif method=='turn/start':
  turn={'id':'turn-'+uuid.uuid4().hex,'status':'inProgress','items':[
    {'type':'userMessage','id':'u1','clientId':p['clientUserMessageId'],'content':p['input']}],
    'startedAt':int(__import__('time').time()),'durationMs':10}
  if settings.get('complete'):
   turn.update(status='completed',completedAt=int(__import__('time').time()))
   turn['items'].append({'type':'agentMessage','id':'a1','text':'Synthetic checked result','phase':'final_answer'})
  turn['items'].extend(settings.get('execution_items',[]))
  state['turns']=[turn];persist()
  if settings.get('lose_turn'): sys.exit(0)
  result={'turn':turn}
 elif method=='thread/read':
  state=json.loads(statefile.read_text())
  result={'thread':{**state,'id':'foreign' if settings.get('wrong_read') else state['id']}}
 elif method=='thread/turns/list':
  state=json.loads(statefile.read_text());result={'data':state['turns'],'nextCursor':settings.get('next_cursor')}
  if settings.get('summary_items'):
   result['data']=[{**t,'itemsView':'summary'} for t in state['turns']]
 elif method=='turn/steer':
  result={'turnId':p['expectedTurnId']}
  if settings.get('notify_on_steer'):
   state['turns'][0].update(status='completed',items=[{'type':'agentMessage','id':'final','text':'Identified final result'}]);persist()
   send({'method':'turn/completed','params':{'threadId':state['id'],'turn':state['turns'][0]}})
 elif method=='turn/interrupt':
  if not settings.get('ack_only'):
   state['turns'][0]['status']='interrupted';persist()
  result={}
 else:
  send({'id':q['id'],'error':{'code':-32601,'message':'unsupported'}});continue
 if settings.get('wrong_rpc') and method=='turn/start':send({'id':'foreign','result':result});continue
 send({'id':q['id'],'result':result})
 if settings.get('wrong_notification') and method=='turn/start':
  send({'method':'turn/completed','params':{'threadId':'foreign','turn':{**state['turns'][0],'status':'completed'}}})
'''


class CodexTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.home = self.root / 'native'; self.home.mkdir()
        self.workspace = self.root / 'workspace'; self.workspace.mkdir()
        self.binary = self.root / 'fake-codex'
        self.binary.write_text('#!' + sys.executable + '\n' + FAKE); self.binary.chmod(0o700)
        self.service = GTDService(self.root / 'data')
        self.control = ExecutionControl(self.service, dict(period_start=datetime.now(timezone.utc).isoformat(), period_seconds=3600,
            max_cost_usd=10, max_runtime_seconds=1000, recovery_cost_usd=1, recovery_runtime_seconds=50,
            max_active=2, max_job_runtime_seconds=300, max_retries=0, max_descendants=0))
        self.item = self.service.capture('felix', 'capture', 'Synthetic code task')['item']
        self.control.register_bot('felix', 'bot', dict(id='codex', state='available', source_urn='urn:test:codex',
            host='local', profile='synthetic', capabilities=['prepare_private'], item_id=self.item['id'], probe_evidence='fixture'))
        self.route = dict(host='local', profile='synthetic', workspace=str(self.workspace), model='synthetic', provider='test', effort='low',
            base_instructions='Only this private work.', developer_instructions='Never publish.', instruction_sources={})
        self.config = dict(binary=str(self.binary), binary_sha256=hashlib.sha256(self.binary.read_bytes()).hexdigest(),
            codex_home=str(self.home), routes={'codex':self.route}, request_timeout_seconds=.3, shutdown_grace_seconds=.1)
        self.adapter = CodexAdapter(self.control, self.config)
        self.settings = {'effective': {'model':'synthetic','model_provider':'test','model_reasoning_effort':'low',
            'instructions':self.route['base_instructions'],'developer_instructions':self.route['developer_instructions'],
            'approval_policy':'never','sandbox_mode':'workspace-write','web_search':'disabled',
            'sandbox_workspace_write':{'writable_roots':[str(self.workspace)],'network_access':False,
                'exclude_tmpdir_env_var':True,'exclude_slash_tmp':True}, 'features':{'multi_agent':False}},
            'thread_config':{'cwd':str(self.workspace),'model':'synthetic','modelProvider':'test','reasoningEffort':'low',
                'approvalPolicy':'never','approvalsReviewer':'user','sandbox':self.adapter._sandbox(self.route),'instructionSources':[]}}
        self.save()
        self.serial = 0

    def save(self): (self.home/'fixture.json').write_text(json.dumps(self.settings))

    def reserve(self):
        self.serial += 1
        result = self.control.reserve('gtd-felix','reserve-'+str(self.serial), dict(item_id=self.item['id'],
            expected_version=self.service.get_item(self.item['id'])['version'], capability='prepare_private',
            mandate_id=None, bot_id='codex', purpose='Private code '+str(self.serial), scope='Synthetic workspace',
            max_cost_usd=2,max_runtime_seconds=20,max_retries=0,max_descendants=0))
        self.assertEqual(result['status'],'reserved',result)
        return result['job_id']

    def audit(self):
        path=self.home/'audit.jsonl'
        return [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []

    async def asyncTearDown(self):
        await self.adapter.close()
        self.service.close()
        self.temp.cleanup()

    async def test_discovery_has_no_thread_or_turn_and_checks_native_mcp(self):
        discovery = await self.adapter.discover('codex')
        self.assertEqual(discovery['status'],'ready')
        self.assertFalse(discovery['capabilities']['host_read_isolated'])
        self.assertNotIn('thread/start',[x['method'] for x in self.audit()])
        self.settings['mcp']=[{'name':'foreign'}];self.save()
        self.assertEqual((await self.adapter.discover('codex'))['reason'],'native_mcp_inventory_not_empty')

    async def test_one_thread_one_turn_exact_result_unknown_cost_no_integration(self):
        self.settings['complete']=True;self.save();job=self.reserve()
        with patch.dict(os.environ,{'OPENAI_API_KEY':'secret-never-forward','CODEX_HOME':'/foreign'}):
            result=await self.adapter.submit(job,'Synthetic prompt')
        self.assertTrue(result['terminal'],result)
        self.assertEqual(result['integration'],'not_performed')
        self.assertEqual(self.control.get_job(job)['charged_cost_usd'],2)
        self.assertNotEqual(self.control.get_job(job)['integration'],'integrated')
        self.assertEqual(await self.adapter.submit(job,'Synthetic prompt'),result)
        rows=self.audit()
        self.assertEqual(sum(x['method']=='thread/start' for x in rows),1)
        self.assertEqual(sum(x['method']=='turn/start' for x in rows),1)
        self.assertTrue(all(not x['ambient_secret'] and x['argv']==['app-server','--strict-config','--stdio'] for x in rows))
        self.assertIsNotNone(result['artifact'])

    async def test_lost_thread_ack_never_creates_replacement_or_global_history(self):
        self.settings['lose_thread']=True;self.save();job=self.reserve()
        self.assertEqual((await self.adapter.submit(job,'prompt'))['status'],'uncertain')
        await self.adapter.close();self.adapter=CodexAdapter(self.control,self.config)
        self.assertEqual((await self.adapter.reconcile(job))['error'],'native_thread_unknown')
        await self.adapter.submit(job,'prompt')
        self.assertEqual(sum(x['method']=='thread/start' for x in self.audit()),1)
        self.assertFalse(self.control.get_job(job)['terminal'])

    async def test_lost_turn_ack_recovers_exact_known_thread_without_resend(self):
        self.settings.update(lose_turn=True,complete=True);self.save();job=self.reserve()
        await self.adapter.submit(job,'prompt')
        await self.adapter.close();self.adapter=CodexAdapter(self.control,self.config)
        self.settings.pop('lose_turn');self.save()
        result=await self.adapter.reconcile(job)
        self.assertTrue(result['terminal'],result)
        self.assertEqual(sum(x['method']=='turn/start' for x in self.audit()),1)
        self.assertTrue(all(x['method'] != 'thread/list' for x in self.audit()))
        self.assertEqual(sum(x['method']=='thread/resume' for x in self.audit()),0)

    async def test_stop_ack_and_transport_close_are_not_terminal(self):
        self.settings['ack_only']=True;self.save();job=self.reserve()
        await self.adapter.submit(job,'prompt')
        self.assertFalse((await self.adapter.stop(job))['terminal'])
        self.assertFalse(self.control.get_job(job)['terminal'])
        await self.adapter.close()
        self.assertFalse(self.control.get_job(job)['terminal'])
        self.assertEqual(self.control.budget()['active'],1)

    async def test_stop_native_readback_and_steer_expected_turn_no_repeat(self):
        job=self.reserve();await self.adapter.submit(job,'prompt')
        self.assertEqual((await self.adapter.steer(job,'Correction','op'))['status'],'steer_acknowledged')
        await self.adapter.steer(job,'Correction','op')
        await self.adapter.stop(job)
        result=await self.adapter.poll(job)
        self.assertEqual(result['native_status'],'cancelled',result)
        calls=[x for x in self.audit() if x['method']=='turn/steer']
        self.assertEqual(len(calls),1)
        self.assertEqual(calls[0]['params']['expectedTurnId'],result['turn_id'])

    async def test_revoked_budget_config_and_foreign_notifications_do_not_dispatch_or_close(self):
        job=self.reserve();self.control.request_stop('gtd-felix','stop-before',job)
        self.assertEqual((await self.adapter.submit(job,'prompt'))['status'],'rejected')
        self.assertEqual(self.audit(),[])
        self.settings['effective']['approval_policy']='on-request';self.save()
        job=self.reserve();await self.adapter.submit(job,'prompt')
        self.assertNotIn('turn/start',[x['method'] for x in self.audit()])

    async def test_foreign_thread_read_and_notification_are_rejected(self):
        self.settings.update(wrong_read=True,wrong_notification=True);self.save()
        job=self.reserve();await self.adapter.submit(job,'prompt');await asyncio.sleep(.03)
        self.assertFalse(self.control.get_job(job)['terminal'])
        self.assertEqual((await self.adapter.poll(job))['status'],'uncertain')
        self.assertFalse(self.control.get_job(job)['terminal'])

    async def test_live_transport_cannot_be_replaced_by_second_adapter(self):
        job=self.reserve();await self.adapter.submit(job,'prompt')
        other=CodexAdapter(self.control,self.config)
        try:
            self.assertEqual((await other.reconcile(job))['error'],'owned_process_still_alive')
            await other.submit(job,'prompt')
            self.assertEqual(sum(x['method']=='thread/start' for x in self.audit()),1)
        finally: await other.close()

    async def test_wrong_rpc_ack_is_uncertain_and_exact_read_recovers_same_turn(self):
        self.settings['wrong_rpc']=True;self.save();job=self.reserve()
        self.assertEqual((await self.adapter.submit(job,'prompt'))['status'],'uncertain')
        result=await self.adapter.poll(job)
        self.assertEqual(result['native_status'],'running',result)
        self.assertEqual(sum(x['method']=='turn/start' for x in self.audit()),1)

    async def test_revocation_during_work_interrupts_without_new_reservation(self):
        job=self.reserve();await self.adapter.submit(job,'prompt')
        self.control.request_stop('gtd-felix','owner-stop',job)
        await asyncio.sleep(.35)
        self.assertTrue(any(x['method']=='turn/interrupt' for x in self.audit()))
        # Monitor reads the exact interrupted turn before containing the unit.
        await asyncio.wait_for(self.adapter.monitors[job], 3)
        self.assertTrue(self.control.get_job(job)['terminal'])
        self.assertTrue(self.adapter._get('local:'+job)['contained'])
        result=await self.adapter.reconcile(job)
        self.assertEqual(result['native_status'],'cancelled',result)

    async def test_binary_hash_and_instruction_sources_are_verified_before_inference(self):
        self.adapter.config['binary_sha256']='0'*64
        self.assertEqual((await self.adapter.discover('codex'))['reason'],'binary_hash_mismatch')
        self.assertEqual(self.audit(),[])
        self.adapter.config['binary_sha256']=self.config['binary_sha256']
        source=self.workspace/'AGENTS.md';source.write_text('Original instructions')
        self.adapter.config['routes']['codex']['instruction_sources']={str(source):hashlib.sha256(source.read_bytes()).hexdigest()}
        source.write_text('Changed instructions')
        self.assertEqual((await self.adapter.discover('codex'))['reason'],'instruction_source_changed')
        self.assertEqual(self.audit(),[])

    async def test_detached_stop_only_signals_exact_owned_process_without_terminal(self):
        job=self.reserve();await self.adapter.submit(job,'prompt')
        driver=self.adapter.connections[job].channel.driver
        other=CodexAdapter(self.control,self.config)
        try:
            result=await other.stop(job)
            self.assertFalse(result['terminal'])
            self.assertTrue(self.control.get_job(job)['stop_requested'])
            self.assertFalse(self.control.get_job(job)['terminal'])
            await asyncio.sleep(.05)
            self.assertIsNotNone(driver.returncode)
            self.assertEqual(sum(x['method']=='turn/start' for x in self.audit()),1)
        finally: await other.close()

    async def test_native_completed_notification_records_exact_turn(self):
        self.settings['notify_on_steer']=True;self.save()
        job=self.reserve();await self.adapter.submit(job,'prompt')
        await self.adapter.steer(job,'finish','finish-op')
        await self.adapter._await_remote_terminal(job)
        self.assertTrue(self.control.get_job(job)['terminal'])
        self.assertEqual((await self.adapter.poll(job))['native_status'],'completed')
        self.assertIsNotNone((await self.adapter.poll(job))['artifact'])

    async def test_artifact_survives_crash_after_terminal_observation(self):
        self.settings['complete']=True;self.save();job=self.reserve()
        original=self.control.observe
        def observe_then_crash(*args):
            result=original(*args)
            if result.get('job',{}).get('terminal'): raise ValueError('synthetic_post_observation_crash')
            return result
        with patch.object(self.control,'observe',side_effect=observe_then_crash):
            await self.adapter.submit(job,'prompt')
        self.assertTrue(self.control.get_job(job)['terminal'])
        result=await self.adapter.reconcile(job)
        self.assertTrue(result['terminal'])
        self.assertIsNotNone(result['artifact'])
        self.assertEqual(sum(x['method']=='turn/start' for x in self.audit()),1)

    async def test_detached_stop_rejects_changed_pid_birth(self):
        job=self.reserve();await self.adapter.submit(job,'prompt')
        original=self.adapter._get('process:'+job)
        other=CodexAdapter(self.control,self.config)
        try:
            other._update('process:'+job,birth='not-the-owned-process')
            self.assertEqual((await other.stop(job))['status'],'uncertain')
            self.assertIsNone(self.adapter.connections[job].channel.driver.returncode)
        finally:
            other._update('process:'+job,**original)
            await other.close()

    async def test_native_cwd_implicit_sandbox_accepts_no_extra_root_only(self):
        self.settings['thread_config']['sandbox']['writableRoots'] = []
        self.save()
        job = self.reserve()
        result = await self.adapter.submit(job, 'Bounded task')
        self.assertEqual(result['native_status'], 'running')
        self.assertFalse(result['terminal'])
        response = {'thread': {'id': 'exact'}, **self.settings['thread_config']}
        response['sandbox'] = {**response['sandbox'], 'writableRoots': ['/tmp']}
        with self.assertRaisesRegex(ValueError, 'effective_thread_mismatch'):
            self.adapter._thread_verified(self.route, response)

    async def test_paginated_read_requires_full_items_and_end_of_exact_thread(self):
        self.settings.update(complete=True, lose_turn=True, next_cursor='more'); self.save()
        job = self.reserve()
        await self.adapter.submit(job, 'Bounded task')
        await self.adapter.close()
        self.adapter = CodexAdapter(self.control, self.config)
        result = await self.adapter.reconcile(job)
        self.assertFalse(result['terminal'])
        self.settings.update(complete=True, summary_items=True, next_cursor=None); self.save()
        await self.adapter.close()
        self.adapter = CodexAdapter(self.control, self.config)
        result = await self.adapter.reconcile(job)
        self.assertFalse(result['terminal'])
        self.assertEqual(sum(x['method']=='turn/start' for x in self.audit()), 1)

    async def test_recovered_live_turn_restores_monitor_for_revocation_and_expiry(self):
        job=self.reserve();await self.adapter.submit(job,'prompt')
        await self.adapter.close();self.adapter=CodexAdapter(self.control,self.config)
        result=await self.adapter.reconcile(job)
        self.assertEqual(result['native_status'],'running')
        self.assertIn(job,self.adapter.monitors)
        self.control.request_stop('gtd-felix','recovered-revoke',job)
        await asyncio.sleep(.35)
        self.assertNotIn(job,self.adapter.connections)
        self.assertFalse(any(x['method']=='turn/interrupt' for x in self.audit()))
        self.assertTrue(self.adapter._get('local:'+job)['contained'])
        self.assertFalse(self.control.get_job(job)['terminal'])
        self.assertEqual(sum(x['method']=='turn/start' for x in self.audit()),1)

    async def test_recovery_of_expired_turn_rejects_entry_then_stops_without_poll(self):
        job=self.reserve();await self.adapter.submit(job,'prompt');await self.adapter.close()
        self.adapter=CodexAdapter(self.control,self.config)
        self.adapter._update('job:'+job,turn_requested_at=0)
        await self.adapter.reconcile(job)
        result=await self.adapter.steer(job,'too late','late-entry')
        self.assertNotEqual(result['status'],'steer_acknowledged')
        await asyncio.sleep(.35)
        self.assertNotIn(job,self.adapter.connections)
        self.assertNotIn('turn/steer',[x['method'] for x in self.audit()])
        self.assertFalse(any(x['method']=='turn/interrupt' for x in self.audit()))
        self.assertTrue(self.adapter._get('local:'+job)['contained'])
        self.assertFalse(self.control.get_job(job)['terminal'])

    async def test_detached_terminal_read_survives_changed_instructions_without_model_entry(self):
        source=self.workspace/'AGENTS.md';source.write_text('Original instructions')
        manifest={str(source):hashlib.sha256(source.read_bytes()).hexdigest()}
        self.config['routes']['codex']['instruction_sources']=manifest
        self.adapter=CodexAdapter(self.control,self.config)
        self.settings['thread_config']['instructionSources']=[str(source)]
        self.settings.update(complete=True,lose_turn=True);self.save()
        job=self.reserve();await self.adapter.submit(job,'prompt');await self.adapter.close()
        source.write_text('Changed instructions')
        self.adapter=CodexAdapter(self.control,self.config)
        self.settings.pop('lose_turn');self.save()
        result=await self.adapter.reconcile(job)
        self.assertTrue(result['terminal'],result)
        self.assertEqual(sum(x['method']=='turn/start' for x in self.audit()),1)
        self.assertNotIn('thread/resume',[x['method'] for x in self.audit()])

    async def test_typed_execution_evidence_has_hashes_not_reasoning_or_raw_diffs(self):
        self.settings.update(complete=True, execution_items=[
            {'type':'reasoning','id':'hidden','text':'PRIVATE REASONING SENTINEL'},
            {'type':'commandExecution','id':'cmd1','command':'python3 -m unittest','commandActions':[],
             'cwd':str(self.workspace),'status':'completed','exitCode':0,'aggregatedOutput':'3 tests OK'},
            {'type':'fileChange','id':'patch1','status':'completed','changes':[{'path':'app.py',
             'kind':{'type':'add'},'diff':'+synthetic contents'}]}]);self.save()
        result=await self.adapter.submit(self.reserve(),'Synthetic work',durable=True)
        raw=(self.service.data_dir/result['artifact']['path']).read_text();artifact=json.loads(raw)
        self.assertNotIn('PRIVATE REASONING',raw);self.assertNotIn('+synthetic contents',raw)
        self.assertEqual(artifact['execution'][0]['output'],{'sha256':hashlib.sha256(b'3 tests OK').hexdigest(),'bytes':10})
        self.assertEqual(artifact['execution'][0]['exitCode'],0)
        self.assertEqual(artifact['execution'][1]['changes'][0]['path'],str(self.workspace/'app.py'))
        self.assertEqual(artifact['workspace_integration'],'not_verified')
        self.assertEqual(artifact['assessment'],'pending_principal')

    async def test_execution_projection_rejects_foreign_paths_duplicate_ids_and_excess(self):
        command={'type':'commandExecution','id':'cmd','command':'test','cwd':str(self.workspace),'status':'completed'}
        for items,reason in [([{**command,'cwd':'/etc'}],'execution_path_outside_workspace'),
            ([command,command],'execution_item_identity_invalid'),
            ([{**command,'aggregatedOutput':'x'*(1024*1024+1)}],'execution_content_limit'),
            ([{'type':'fileChange','id':'f','status':'completed','changes':[{'path':'safe','kind':{'type':'update','move_path':'../foreign'},'diff':'x'}]}],
             'execution_path_outside_workspace')]:
            with self.subTest(reason=reason),self.assertRaisesRegex(ValueError,reason):
                self.adapter._execution_projection(self.route,items)

    def configure_overlay(self):
        self.route['process_overlay']={'version':1,'disabled_mcp_servers':['configured']}
        self.route['base_instructions']='PRIVATE_BASE_SENTINEL'
        self.route['developer_instructions']='PRIVATE_DEVELOPER_SENTINEL'
        self.settings['effective'].update(instructions='PRIVATE_INHERITED_SENTINEL',developer_instructions='PRIVATE_INHERITED_DEVELOPER',
            mcp_servers={'configured':{'enabled':True,'command':'synthetic-command'}},hooks={'SessionStart':[{'synthetic':True}]},
            plugins={'synthetic':{'enabled':True}})
        self.settings['mcp']=[{'name':'configured','runtimeStatus':'disabled','pluginId':None,'serverInfo':None,
            'tools':{},'resources':[],'resourceTemplates':[]}]
        self.save()
        self.adapter=CodexAdapter(self.control,self.config)

    async def test_process_overlay_disables_inherited_capabilities_without_argv_instructions(self):
        self.configure_overlay()
        discovery=await self.adapter.discover('codex')
        self.assertEqual(discovery['status'],'ready')
        self.assertEqual(discovery['capabilities']['disabled_mcp_servers'],['configured'])
        job=self.reserve();result=await self.adapter.submit(job,'Private task')
        self.assertEqual(result['native_status'],'running',result)
        argv=' '.join(self.audit()[0]['argv'])
        self.assertNotIn('PRIVATE_',argv)
        thread=next(row for row in self.audit() if row['method']=='thread/start')
        self.assertEqual(thread['params']['baseInstructions'],'PRIVATE_BASE_SENTINEL')
        self.assertEqual(thread['params']['developerInstructions'],'PRIVATE_DEVELOPER_SENTINEL')
        self.assertTrue(self.adapter._get('job:'+job)['overlay_hash'])
        self.assertTrue(all(not row['ambient_secret'] for row in self.audit()))
        await self.adapter.close()
        self.adapter=CodexAdapter(self.control,self.config)
        self.assertFalse((await self.adapter.reconcile(job))['terminal'])
        self.assertEqual(sum(row['method']=='turn/start' for row in self.audit()),1)

    async def test_overlay_unknown_or_active_mcp_and_wrong_feature_are_rejected(self):
        from gtd_felix.codex import process_overlay,verify_mcp_inventory
        self.configure_overlay()
        for server in [{**self.settings['mcp'][0],'name':'foreign'},
                       {**self.settings['mcp'][0],'runtimeStatus':'connected'},
                       {**self.settings['mcp'][0],'tools':{'effect':{}}}]:
            with self.subTest(server=server),self.assertRaises(ValueError):
                verify_mcp_inventory({'data':[server]},self.route)
        self.settings['effective']['mcp_servers']['unknown']={'enabled':True};self.save()
        self.assertEqual((await self.adapter.discover('codex'))['reason'],'overlay_mcp_not_disabled')
        self.assertNotIn('thread/start',[row['method'] for row in self.audit()])
        overlay=process_overlay(self.route)
        expected={**self.settings['effective'],**overlay}
        expected['features']={**overlay['features'],'hooks':True}
        with self.assertRaisesRegex(ValueError,'overlay_features_mismatch'):
            self.adapter._effective_config(self.route,{'config':expected})
        with self.assertRaisesRegex(ValueError,'native_mcp_inventory_not_empty'):
            verify_mcp_inventory({'data':self.settings['mcp']})

    async def test_added_overlay_can_read_legacy_terminal_but_cannot_steer_old_admission(self):
        self.settings.update(complete=True,lose_turn=True);self.save()
        job=self.reserve();await self.adapter.submit(job,'Legacy input');await self.adapter.close()
        self.route['process_overlay']={'version':1,'disabled_mcp_servers':[]}
        self.adapter=CodexAdapter(self.control,self.config)
        self.assertEqual((await self.adapter.steer(job,'New input','forbidden'))['error'],'steer_unconfirmed')
        result=await self.adapter.reconcile(job)
        self.assertTrue(result['terminal'],result)
        self.assertEqual(sum(row['method']=='turn/start' for row in self.audit()),1)
        self.assertNotIn('turn/steer',[row['method'] for row in self.audit()])
        self.assertNotIn('thread/resume',[row['method'] for row in self.audit()])

    async def test_overlay_rejects_arbitrary_keys_and_secret_identifiers(self):
        from gtd_felix.codex import process_overlay
        for change in [{'version':1,'disabled_mcp_servers':[],'OPENAI_API_KEY':'secret'},
                       {'version':1,'disabled_mcp_servers':['bad\nname']}, {'version':1,'disabled_mcp_servers':[{}]}]:
            with self.assertRaises(ValueError):process_overlay({**self.route,'process_overlay':change})
        with self.assertRaisesRegex(ValueError,'overlay_public_identifier_required'):
            process_overlay({**self.route,'model':'secret value','process_overlay':{'version':1,'disabled_mcp_servers':[]}})

    async def test_protocol_fields_match_pinned_public_schema(self):
        schema=Path('/home/felix/.local/state/gtd-felix/p4-probe/schema-codex-0.154.0-20260911/v2')
        if not schema.exists(): self.skipTest('pinned schema absent')
        job=self.reserve();await self.adapter.submit(job,'prompt');await self.adapter.steer(job,'correction','op');await self.adapter.stop(job);await self.adapter.poll(job)
        names={'thread/read':'ThreadReadParams','thread/turns/list':'ThreadTurnsListParams','config/read':'ConfigReadParams','thread/start':'ThreadStartParams','thread/resume':'ThreadResumeParams','turn/start':'TurnStartParams',
               'turn/steer':'TurnSteerParams','turn/interrupt':'TurnInterruptParams','mcpServerStatus/list':'ListMcpServerStatusParams'}
        for row in self.audit():
            if row['method'] in names:
                definition=json.loads((schema/(names[row['method']]+'.json')).read_text())
                self.assertTrue(set(definition.get('required', [])) <= set(row['params']))
                self.assertTrue(set(row['params']) <= set(definition['properties']))


if __name__=='__main__': unittest.main()
