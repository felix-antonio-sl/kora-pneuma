"""Real runtime + synthetic local SSH/websocket peers. No remote or model calls."""
import asyncio
import copy
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from aiohttp import web

_spec=importlib.util.spec_from_file_location('readiness',Path(__file__).resolve().parents[2]/'scripts/gtd_codex_remote_readiness.py')
readiness=importlib.util.module_from_spec(_spec);_spec.loader.exec_module(readiness)
import test_codex_remote as remote_tests
from gtd_felix.codex import process_overlay


class CompanionHelperTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name);self.bin=self.root/'bin';self.bin.mkdir()
        self.binary=self.bin/'codex';self.binary.write_text('synthetic binary')
        self.binary.chmod(0o700)
        self.host=self.bin/'codex-code-mode-host'
        self.host.write_text('#!'+sys.executable+'''\nimport json,struct,sys,os
assert set(os.environ)<= {'PATH','LC_CTYPE'}
assert os.environ['PATH']=='/usr/bin:/bin'
assert sys.argv[1:]==['--listen','stdio']
raw=sys.stdin.buffer.read();assert struct.unpack('<I',raw[:4])[0]==len(raw)-4
assert json.loads(raw[4:])=={'type':'connection/hello','supportedVersions':[1],'requiredCapabilities':[],'optionalCapabilities':[]}
out=json.dumps({'type':'connection/ready','selectedVersion':1,'capabilities':[]}).encode()
sys.stdout.buffer.write(struct.pack('<I',len(out))+out)
''');self.host.chmod(0o700)
        (self.root/'config.toml').write_text('synthetic=true\n')
        self.request={'route':{'remote':{'hostname':os.uname().nodename,'uid':os.getuid(),
            'binary':str(self.binary),'binary_sha256':readiness.sha(self.binary.read_bytes()),'codex_home':str(self.root)}},
            'companion_sha256':readiness.sha(self.host.read_bytes()),
            'native_config_sha256':readiness.sha((self.root/'config.toml').read_bytes())}

    def helper(self):
        process=subprocess.run([sys.executable,'-I','-B','-c',readiness.HELPER],
            input=json.dumps(self.request),text=True,capture_output=True,timeout=10)
        self.assertEqual(process.returncode,0,process.stderr)
        return json.loads(process.stdout)

    def test_fixed_framed_protocol_success(self):self.assertEqual(self.helper()['status'],'PASS')
    def test_missing_companion(self):
        self.host.unlink();self.assertEqual(self.helper()['reason'],'companion_missing')
    def test_wrong_hash_prevents_companion_execution(self):
        self.request['companion_sha256']='0'*64
        self.assertEqual(self.helper()['reason'],'companion_hash_changed')
    def test_hostname_rejected(self):
        self.request['route']['remote']['hostname']='wrong'
        self.assertEqual(self.helper()['reason'],'remote_host_changed')
    def test_bad_handshake(self):
        self.host.write_text('#!'+sys.executable+'\nprint("bad")\n')
        self.request['companion_sha256']=readiness.sha(self.host.read_bytes())
        self.assertEqual(self.helper()['status'],'FAIL')


class ReadinessIntegrationTests(unittest.IsolatedAsyncioTestCase):
    save=remote_tests.RemoteIntegrationTests.save
    reserve=remote_tests.RemoteIntegrationTests.reserve
    modify=remote_tests.RemoteIntegrationTests.modify
    remote_calls=remote_tests.RemoteIntegrationTests.remote_calls
    asyncTearDown=remote_tests.RemoteIntegrationTests.asyncTearDown

    async def asyncSetUp(self):
        await remote_tests.RemoteIntegrationTests.asyncSetUp(self)
        await self.server.cleanup()
        # Existing fixture bootstraps an unrelated captured item, but zero jobs.
        self.command_result={'exitCode':0,'stdout':'','stderr':''}
        self.native_error=False;self.command_params=[]
        async def handler(request):
            ws=web.WebSocketResponse();await ws.prepare(request);self.sockets.append(ws)
            async for message in ws:
                q=json.loads(message.data);method=q.get('method');self.methods.append(method)
                if 'id' not in q:continue
                result={}
                if method=='config/read':
                    effective=copy.deepcopy(self.settings['effective']);effective.update(process_overlay(self.route))
                    result={'config':effective}
                elif method=='mcpServerStatus/list':result={'data':[],'nextCursor':None}
                elif method=='command/exec':
                    self.command_params.append(q['params'])
                    if self.native_error:
                        await ws.send_json({'id':q['id'],'error':{'code':-32000,'message':'synthetic sandbox denial'}});continue
                    result=self.command_result
                await ws.send_json({'id':q['id'],'result':result})
            return ws
        app=web.Application();app.router.add_get('/',handler);self.server=web.AppRunner(app);await self.server.setup()
        self.site=web.UnixSite(self.server,str(self.root/'native.sock'));await self.site.start()
        # Real helper reports boot_id on closure; fixture previously omitted it.
        self.modify(override={'boot_id':'00000000-0000-0000-0000-000000000000'})

    async def evaluate(self,gate_result=None):
        async def gate(identities):return gate_result or {'status':'PASS'}
        return await readiness.evaluate(self.adapter,self.route,gate)

    async def test_success_real_adapter_zero_jobs_threads_turns_and_fresh_close(self):
        result=await self.evaluate()
        self.assertEqual(result['status'],'READY',result)
        self.assertEqual(result['jobs_observed'],0)
        self.assertEqual(result['dispatch_counts'],{'thread/start':0,'thread/resume':0,'turn/start':0})
        self.assertEqual(self.command_params,[readiness.native_params(str(self.workspace))])
        self.assertEqual(self.methods,['initialize','initialized','config/read','mcpServerStatus/list','command/exec'])
        self.assertEqual(result['closure'],'PASS')
        self.assertTrue(all(readiness.pid_absent(i) for i in result['ssh_identities']))
        self.assertEqual(json.loads(self.fixture.read_text())['calls'][-1]['op'],'observe')
        self.assertEqual(len(self.remote_calls('start')),1)

    async def test_gate_failures_never_dispatch_native_or_start_unit(self):
        for reason in ('remote_host_changed','companion_hash_changed','companion_missing','companion_handshake_failed'):
            result=await self.evaluate({'status':'FAIL','reason':reason})
            self.assertEqual(result['status'],'FAIL');self.assertEqual(result['native_command'],'NOT_RUN')
            self.assertEqual(self.methods,[]);self.assertEqual(self.remote_calls('start'),[])

    async def test_sandbox_exit_error_blocks_and_bounds_stderr(self):
        self.command_result={'exitCode':1,'stderr':'synthetic sandbox error '*200}
        result=await self.evaluate()
        self.assertEqual(result['status'],'FAIL',result)
        self.assertEqual(result['reason'],'native_sandbox_command_failed')
        self.assertEqual(len(result['native_command']['stderr']),2048)
        self.assertEqual(result['closure'],'PASS')

    async def test_native_rpc_error_blocks(self):
        self.native_error=True;result=await self.evaluate()
        self.assertEqual(result['status'],'FAIL');self.assertEqual(result['reason'],'native_rpc_rejected')
        self.assertEqual(result['closure'],'PASS')

    async def test_unconfirmed_fresh_closure_blocks_ready(self):
        from gtd_felix.codex_remote import RemoteTransport
        original=RemoteTransport._call
        async def altered(transport,op,*args,**kwargs):
            value=await original(transport,op,*args,**kwargs)
            if op=='observe' and transport.adapter._get('remote:'+transport.key).get('contained'):
                value['owned_pid_absent']=False
            return value
        with patch.object(RemoteTransport,'_call',altered):result=await self.evaluate()
        self.assertEqual(result['status'],'FAIL');self.assertEqual(result['closure'],'FAIL')
        self.assertEqual(result['closure_reason'],'fresh_remote_closure_unconfirmed')

    async def test_own_ssh_pid_present_blocks_ready(self):
        with patch.object(readiness,'pid_absent',return_value=False):result=await self.evaluate()
        self.assertEqual(result['status'],'FAIL');self.assertEqual(result['closure_reason'],'owned_ssh_closure_unconfirmed')


class DescriptionTests(unittest.IsolatedAsyncioTestCase):
    async def test_describe_valid_config_no_ssh_no_output_no_case_change(self):
        from datetime import datetime,timezone
        from runtime_location import RUNTIME
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);path=root/'config.json';output=root/'new-output';case=root/'old-case'
            case.mkdir();(case/'lease').write_text('untouched')
            route={'host':'ssh','profile':'synthetic','workspace':'/synthetic/work','model':'gpt-6-astra',
                'provider':'openai','effort':'low','base_instructions':'Synthetic.','developer_instructions':'Synthetic.',
                'instruction_sources':{'/synthetic/work/AGENTS.md':readiness.sha(readiness.probe.SEED['AGENTS.md'].encode())},
                'process_overlay':{'version':1,'disabled_mcp_servers':[]},'remote':{'ssh_alias':'synthetic',
                'hostname':'synthetic','uid':os.getuid(),'binary':'/synthetic/bin/codex','binary_sha256':'a'*64,
                'codex_home':'/synthetic/home','private_root':'/synthetic/private','max_runtime_seconds':30}}
            config={'case_dir':str(case),'runtime_root':str(RUNTIME),
                'runtime_manifest':readiness.probe.contract.source_manifest(RUNTIME),
                'core_hostname':os.uname().nodename,'core_uid':os.getuid(),'native_config_sha256':'b'*64,
                'actors':{'owner':'owner','principal':'principal','executor':'executor'},
                'campaign':{'id':'synthetic','period_start':datetime.now(timezone.utc).isoformat(),
                    'period_seconds':3600,'max_cost_usd':1,'max_runtime_seconds':30},
                'reservation':{'max_cost_usd':1,'max_runtime_seconds':30},
                'codex':{'routes':{'worker':route},'request_timeout_seconds':5,'shutdown_grace_seconds':1}}
            path.write_text(json.dumps(config));path.chmod(0o600);original=path.read_bytes()
            with patch.object(asyncio,'create_subprocess_exec',side_effect=AssertionError('zero SSH required')):
                result=await readiness.run(str(path),'c'*64,str(output))
            self.assertEqual(result['status'],'DESCRIBE');self.assertFalse(output.exists())
            self.assertEqual(path.read_bytes(),original);self.assertEqual((case/'lease').read_text(),'untouched')

    async def test_altered_dependency_rejected_before_import(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);marker=root/'executed'
            script=root/'gtd_codex_remote_readiness.py';script.write_bytes(Path(readiness.__file__).read_bytes())
            (root/'gtd_codex_remote_work_probe.py').write_text('from pathlib import Path\nPath('+repr(str(marker))+').touch()\n')
            process=subprocess.run([sys.executable,'-B',str(script),'--help'],capture_output=True,text=True)
            self.assertNotEqual(process.returncode,0);self.assertFalse(marker.exists())
            self.assertIn('frozen_contract_changed',process.stderr)
