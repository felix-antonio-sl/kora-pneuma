"""Work runner with a real fake-RPC process and isolated real GTD runtime copy."""
from datetime import datetime,timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from runtime_location import RUNTIME
from test_codex import FAKE

SCRIPT=Path(__file__).resolve().parents[2]/'scripts'/'gtd_codex_work_probe.py'
spec=importlib.util.spec_from_file_location('work_probe_contract',SCRIPT)
contract=importlib.util.module_from_spec(spec);spec.loader.exec_module(contract)
FIX='def clamp(value, lower, upper):\n    if lower > upper:\n        raise ValueError("reversed bounds")\n    return min(upper, max(lower, value))\n'


class WorkProbeTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        self.runtime=self.root/'runtime';shutil.copytree(RUNTIME,self.runtime)
        self.home=self.root/'native';self.home.mkdir(mode=0o700)
        (self.home/'config.toml').write_text('model="synthetic-inherited"\n');(self.home/'config.toml').chmod(0o600)
        self.binary=self.root/'fake-codex'
        program=FAKE.replace(" elif method=='turn/start':", " elif method=='turn/start':\n  if settings.get('replacement'): (Path.cwd()/'clamp.py').write_text(settings['replacement'])\n  if settings.get('break_sentinel'): (Path.cwd()/'concurrent_sentinel.txt').write_text('changed')")
        program=program.replace("'ambient_secret':", "'runner_bus_visible':any(k in os.environ for k in ('XDG_RUNTIME_DIR','DBUS_SESSION_BUS_ADDRESS')), 'ambient_secret':")
        self.binary.write_text('#!'+sys.executable+'\n'+program);self.binary.chmod(0o700)
        self.case=self.root/'case';workspace=self.case/'workspace'
        self.config={'case_dir':str(self.case),'runtime_root':str(self.runtime),
            'actors':{'owner':'probe-owner','principal':'probe-principal','executor':'probe-executor'},
            'campaign':{'id':'synthetic-campaign','period_start':datetime.now(timezone.utc).isoformat(),'period_seconds':3600,
                'max_cost_usd':1,'max_runtime_seconds':10},'reservation':{'max_cost_usd':1,'max_runtime_seconds':2},
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
            'complete':True,'replacement':FIX}
        self.save()
    def save(self): (self.home/'fixture.json').write_text(json.dumps(self.settings))
    def tearDown(self): self.temp.cleanup()
    def invoke(self,*flags):
        # The bus belongs to the supervisor, not the native workspace payload.
        bus={k:os.environ[k] for k in ('XDG_RUNTIME_DIR','DBUS_SESSION_BUS_ADDRESS') if k in os.environ}
        process=subprocess.run([sys.executable,'-B',str(SCRIPT),'--config',str(self.configfile),*flags],
            env={'HOME':str(self.root),'PATH':'/usr/bin:/bin','LANG':'C.UTF-8',**bus},capture_output=True,text=True,timeout=30)
        summary=json.loads(process.stdout.splitlines()[-1])
        self.assertIn('receipt',summary,(summary,process.stderr))
        receipt=json.loads((self.case/summary['receipt']).read_text())
        return process.returncode,receipt
    def audit(self):
        path=self.home/'audit.jsonl'
        return [json.loads(x) for x in path.read_text().splitlines()] if path.exists() else []

    def test_discovery_then_one_work_and_replay_verify_actual_workspace(self):
        code,discovery=self.invoke();self.assertEqual(code,0,discovery)
        self.assertEqual(discovery['status'],'DISCOVERY_READY')
        self.assertNotIn('turn/start',[x['method'] for x in self.audit()])
        code,result=self.invoke('--work');self.assertEqual(code,0,result)
        self.assertEqual(result['status'],'TECHNICAL_CRITERIA_PASS')
        self.assertEqual(result['technical_checks']['exit_code'],0)
        self.assertEqual(result['final_job']['integration'],'integrated')
        self.assertEqual(result['principal_assessment'],'NOT_RUN')
        self.assertTrue(result['native_config_unchanged'])
        self.assertTrue(all(x['pid_absent'] for x in result['native_processes']))
        self.assertEqual(result['final_job']['charged_cost_usd'],1)
        self.assertEqual((self.case/'workspace/clamp.py').read_text(),FIX)
        code,repeated=self.invoke('--work');self.assertEqual(code,0,repeated)
        self.assertEqual(repeated['job_id'],result['job_id'])
        self.assertEqual(sum(x['method']=='turn/start' for x in self.audit()),1)
        self.assertEqual(len(repeated['materials']),1)
        self.assertFalse(any(x['runner_bus_visible'] for x in self.audit()))

    def test_broken_protected_file_prevents_material_integration(self):
        self.settings['break_sentinel']=True;self.save()
        code,result=self.invoke('--work');self.assertEqual(code,2)
        self.assertEqual(result['reason'],'protected_workspace_file_changed')
        self.assertNotEqual(result['final_job']['integration'],'integrated')
        self.assertNotIn('materials',result)
        self.assertEqual(result['principal_assessment'],'NOT_RUN')
        prior=sum(x['method']=='turn/start' for x in self.audit())
        _,recovered=self.invoke('--recover')
        self.assertTrue(recovered['terminal'])
        self.assertNotIn('technical_checks',recovered)
        self.assertEqual(sum(x['method']=='turn/start' for x in self.audit()),prior)

    def test_lost_ack_recovers_exact_turn_and_ast_blocks_untrusted_code(self):
        self.settings['lose_turn']=True;self.save()
        code,result=self.invoke('--work');self.assertEqual(code,0,result)
        self.assertEqual(result['status'],'TECHNICAL_CRITERIA_PASS')
        self.assertEqual(sum(x['method']=='turn/start' for x in self.audit()),1)
        target=self.case/'workspace/clamp.py';target.write_text('import os\n')
        with self.assertRaisesRegex(ValueError,'target_function_only'):contract.safe_function(target)

    def test_expiry_and_closed_transport_leave_job_unresolved(self):
        self.settings.update(complete=False,ack_only=True);self.save()
        # Reservation includes supervised startup; .3s can expire before the
        # fixture reaches turn/start, testing admission rather than closure.
        self.config['reservation']['max_runtime_seconds']=3
        self.configfile.write_text(json.dumps(self.config))
        code,result=self.invoke('--work');self.assertEqual(code,2)
        self.assertEqual(sum(x['method']=='turn/start' for x in self.audit()),1,
            {'reason':result.get('reason'),'delivery':result['final_job']['delivery'],
             'methods':[x['method'] for x in self.audit()]})
        self.assertIsNotNone(result['final_job']['native'])
        self.assertFalse(result['terminal'])
        self.assertTrue(result['final_job']['stop_requested'])
        self.assertNotEqual(result['final_job']['integration'],'integrated')
        self.assertTrue(all(x['pid_absent'] for x in result['native_processes']))
        self.assertEqual(sum(x['method']=='turn/start' for x in self.audit()),1)
        code,recovered=self.invoke('--recover');self.assertEqual(code,2)
        self.assertFalse(recovered['terminal'])
        self.assertNotIn('technical_checks',recovered)
        self.assertEqual(sum(x['method']=='turn/start' for x in self.audit()),1)

    def test_native_config_drift_blocks_work_before_dispatch(self):
        code,_=self.invoke();self.assertEqual(code,0)
        (self.home/'config.toml').write_text('model="changed-synthetic"\n')
        code,result=self.invoke('--work');self.assertEqual(code,2)
        self.assertEqual(result['reason'],'native_config_drift')
        self.assertFalse(result['native_config_matches_initial'])
        self.assertNotIn('turn/start',[x['method'] for x in self.audit()])

    def test_native_success_without_correct_workspace_does_not_integrate(self):
        self.settings['replacement']='def clamp(value, lower, upper):\n    return upper\n';self.save()
        code,result=self.invoke('--work');self.assertEqual(code,2)
        self.assertTrue(result['terminal'])
        self.assertEqual(result['reason'],'workspace_criteria_failed')
        self.assertNotEqual(result['technical_checks']['exit_code'],0)
        self.assertNotEqual(result['final_job']['integration'],'integrated')
        self.assertEqual(result['principal_assessment'],'NOT_RUN')

    def test_reviewed_global_source_exact_manifest_and_work(self):
        source=self.home/'AGENTS.md';source.write_text('Reviewed synthetic general guidance.\n')
        approved={str(source):contract.file_hash(source)}
        self.config['reviewed_global_instructions']=approved
        self.config['codex']['routes']['worker']['instruction_sources']=contract.instruction_manifest(self.case/'workspace',approved)
        self.configfile.write_text(json.dumps(self.config))
        self.settings['thread_config']['instructionSources'].append(str(source));self.save()
        code,result=self.invoke('--work');self.assertEqual(code,0,result)
        self.assertEqual(result['principal_assessment'],'NOT_RUN')
        source.write_text('Changed guidance.\n')
        with self.assertRaisesRegex(ValueError,'global_instruction_hash_mismatch'):contract.validate_config(self.config)

    def test_global_source_extra_path_swap_and_override_rejected(self):
        source=self.home/'AGENTS.md';source.write_text('Reviewed.\n')
        self.config['reviewed_global_instructions']={str(source):contract.file_hash(source)}
        route=self.config['codex']['routes']['worker']
        route['instruction_sources']=contract.instruction_manifest(self.case/'workspace',self.config['reviewed_global_instructions'])
        contract.validate_config(self.config)
        extra=self.root/'AGENTS.md';extra.write_text('Unreviewed.\n')
        self.config['reviewed_global_instructions'][str(extra)]=contract.file_hash(extra)
        with self.assertRaisesRegex(ValueError,'global_instruction_path_not_authorized'):contract.validate_config(self.config)
        del self.config['reviewed_global_instructions'][str(extra)]
        source.unlink();source.symlink_to(extra)
        with self.assertRaisesRegex(ValueError,'unsafe_hash_target'):contract.validate_config(self.config)
        source.unlink();source.write_text('Reviewed.\n')
        (self.home/'AGENTS.override.md').write_text('Override.\n')
        with self.assertRaisesRegex(ValueError,'unapproved_instruction_override'):contract.validate_config(self.config)
