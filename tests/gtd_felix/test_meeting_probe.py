"""Meeting harness tests never start a gateway or call a model."""
import asyncio
import copy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch, AsyncMock
from runtime_location import RUNTIME
SCRIPTS=Path(__file__).resolve().parents[2]/'scripts'
sys.path.insert(0,str(SCRIPTS))
import gtd_meeting_probe as probe
sys.path.insert(0,str(RUNTIME))
from gtd_felix.service import GTDService
from gtd_felix.application import writer_lock

class MeetingProbeTests(unittest.TestCase):
    def test_default_is_description_without_process_or_model(self):
        with patch.object(probe.trial,'load_config',side_effect=AssertionError('must not load secrets')),patch.object(probe.trial.Supervisor,'run',side_effect=AssertionError('must not run')):
            self.assertEqual(probe.main([]),0)

    def test_actual_fixture_two_revisions_same_identity_only_owner_materials(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);config={'runtime_root':str(RUNTIME)}
            service={'data_dir':str(root/'state'),'actors':{'owner':'felix','principal':'gtd-felix','executors':['meeting-worker']},'budget':{}}
            # The real service initializes actor identity before the fixture
            # reopens its stopped state. Keep the complete configured identity.
            GTDService(root/'state', executor_actors=['meeting-worker']).close()
            first=probe.apply_fixture(config,service,root,1)
            db=GTDService(root/'state', executor_actors=['meeting-worker'])
            before=db.get_item(first['ids']['source']);position=db.get_item(first['ids']['position']);db.close()
            second=probe.apply_fixture(config,service,root,2)
            self.assertEqual(first['ids'],second['ids'])
            db=GTDService(root/'state', executor_actors=['meeting-worker'])
            try:
                after=db.get_item(second['ids']['source'])
                self.assertEqual(len(after['source_revisions']),2)
                self.assertEqual(db.get_item(first['ids']['position']),position)
                self.assertFalse(db.materials(after['id'])[0]['valid'])
                self.assertTrue(db.materials(after['id'])[1]['valid'])
                self.assertEqual(after['materials'][0]['id'],after['materials'][1]['id'])
                self.assertTrue(all(m['author']=='felix' for m in after['materials']))
                self.assertFalse(db._meta('last_review'))
                self.assertEqual(len(db.query()),2)
                snapshot=probe.A.load_snapshot(root/'fixture-r2.zip',probe.A.sha((root/'fixture-r2.zip').read_bytes()))
                result=probe.evaluate(snapshot,second,2)
                self.assertEqual(result['status'],'FAIL')
                self.assertFalse(result['mechanical_checks']['principal_native_terminal'])
            finally:db.close()

    def test_fixture_refuses_concurrent_writer(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);service={'data_dir':str(root/'state'),'actors':{'owner':'felix','principal':'gtd-felix'},'budget':{}}
            with writer_lock(service['data_dir']):
                with self.assertRaises(Exception):probe.apply_fixture({'runtime_root':str(RUNTIME)},service,root,1)
            self.assertFalse((root/'fixture-identities.json').exists())

    def test_terminal_claim_without_native_payload_and_materials_cannot_pass(self):
        job={'id':'j','actor':'gtd-felix','native':{'provider':'hermes','id':'pretend'},'terminal':True,'integration':'integrated',
             'observations':[{'native_identity':{'provider':'hermes','id':'pretend'},'native_status':'completed'}],'progress':[]}
        snapshot={'items':{},'operations':[],'files':{},'metadata':{'execution:state':{'jobs':{'j':job}}}}
        result=probe.evaluate(snapshot,{'ids':{'source':'s','position':'p','collateral':'c'}},1)
        self.assertEqual(result['status'],'FAIL')
        self.assertFalse(result['mechanical_checks']['principal_native_terminal'])
        self.assertFalse(result['mechanical_checks']['principal_pptx_copy'])

    def test_cli_does_not_report_success_when_cleanup_failed_after_review_required(self):
        receipt={'status':'PARTIAL','case':{'status':'REVIEW_REQUIRED'},'unresolved_jobs':[],
                 'admission_close_error':'configured_bot_suspension_unconfirmed',
                 'processes':[{'status':'STOPPED','pid_absent':True,'returncode':0}]}
        with tempfile.TemporaryDirectory() as temporary:
            supervisor=type('Supervisor',(),{'run':AsyncMock(return_value=receipt)})()
            with patch.object(probe.trial,'load_config',return_value=({}, {}, {})), \
                 patch.object(probe,'preflight'),patch.object(probe.trial,'Supervisor',return_value=supervisor):
                self.assertEqual(probe.main(['--execute','--config','/synthetic/config',
                    '--evidence-dir',str(Path(temporary)/'evidence')]),1)

class MeetingProcessTests(unittest.IsolatedAsyncioTestCase):
    async def test_failed_fixture_process_never_restarts_or_enables_service(self):
        with tempfile.TemporaryDirectory() as temporary:
            driver=object.__new__(probe.MeetingDriver);driver.destination=Path(temporary)
            driver.request=AsyncMock(return_value=[])
            class Process:
                returncode=1
                async def wait(self):return 1
            class Owned:
                def __init__(self,*a,**k):self.process=Process()
                async def start(self):return 55
                async def stop(self,*a):return {'pid_absent':True,'returncode':1}
            class Supervisor:
                service=type('Service',(),{'stop':AsyncMock(return_value={'pid_absent':True,'returncode':0})})()
                config={'python':sys.executable,'_meeting_config_path':'/synthetic/config'}
                processes=[]
                start_service=AsyncMock()
            driver.supervisor=Supervisor()
            with patch.object(probe.trial,'OwnedProcess',Owned),self.assertRaisesRegex(probe.trial.TrialError,'fixture_process_failed'):
                await driver.fixture(2)
            driver.supervisor.start_service.assert_not_called()

    async def test_rejected_suspension_never_introduces_fixture(self):
        driver=object.__new__(probe.MeetingDriver)
        driver.request=AsyncMock(side_effect=[[{'id':'principal','state':'available','probe_evidence':{'synthetic':True}}], {'status':'rejected'}])
        driver.fixture=AsyncMock(side_effect=AssertionError('fixture must not run'))
        with self.assertRaisesRegex(probe.trial.TrialError,'meeting_suspension_rejected'):
            await driver.run_case('MEETING')
        driver.fixture.assert_not_called()

    async def test_two_phase_driver_stops_real_writer_before_fixture_and_resumes_after(self):
        """Synthetic control transport; real product fixtures, exports and writer lock.

        The evaluator is replaced deliberately: this tests lifecycle orchestration,
        not native authorship, HTTP transport, material quality or P3 acceptance.
        """
        import time
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary)
            service_config={'data_dir':str(root/'state'),'actors':{'owner':'felix','principal':'gtd-felix'},'budget':{}}
            service_file=root/'service.json';service_file.write_text(json.dumps(service_config));service_file.chmod(0o600)
            config={'runtime_root':str(RUNTIME),'service_config':str(service_file),'python':sys.executable,
                    '_meeting_config_path':str(root/'meeting.json')}
            (root/'meeting.json').write_text(json.dumps(config));(root/'meeting.json').chmod(0o600)
            bot={'id':'principal','state':'available','probe_evidence':{'synthetic':True}}
            events=[]
            class Supervisor:
                def __init__(self):
                    self.config=config;self.processes=[];self.service=None
                async def start_service(self):
                    # A synthetic owned writer stands in for the HTTP service.
                    # Its lock must disappear before the real fixture can acquire it.
                    marker=root/('ready-'+str(len(self.processes)))
                    code=('import sys,time\nfrom pathlib import Path\nsys.path.insert(0,sys.argv[1])\n'
                          'from gtd_felix.application import writer_lock\n'
                          'with writer_lock(sys.argv[2]):\n Path(sys.argv[3]).touch()\n time.sleep(30)\n')
                    owned=probe.trial.OwnedProcess('synthetic-writer',[sys.executable,'-E','-s','-B','-c',code,
                        str(RUNTIME),service_config['data_dir'],str(marker)],
                        probe.trial.clean_environment(root),root,log_dir=root)
                    self.processes.append(owned);self.service=owned
                    await owned.start()
                    deadline=time.monotonic()+5
                    while not marker.exists():
                        if owned.process.returncode is not None or time.monotonic()>deadline:
                            raise AssertionError('synthetic writer did not become ready')
                        await asyncio.sleep(.01)
                    events.append('start')
                    return owned
            supervisor=Supervisor()
            driver=object.__new__(probe.MeetingDriver)
            driver.supervisor=supervisor;driver.destination=root;driver.started=time.monotonic()
            driver.config={'timeout_seconds':30,'poll_interval_seconds':.01}
            async def request(method,path,payload=None,binary=False):
                if path=='/v1/control/bots':return [copy.deepcopy(bot)]
                if path=='/v1/control/pending':return []
                if path=='/v1/control/register_bot':
                    bot.update(payload['bot']);events.append(bot['state'])
                    if bot['state']=='available':
                        self.assertIsNone(supervisor.service.process.returncode)
                        self.assertEqual(len(list(root.glob('owner-fixture-r*.json'))),events.count('available'))
                    return {'status':'applied'}
                raise AssertionError(path)
            async def snapshot(filename):
                db=GTDService(root/'state')
                try:db.export(root/filename)
                finally:db.close()
                return {'file':filename,'sha256':probe.A.sha((root/filename).read_bytes())}
            def lifecycle_evaluation(snapshot,fixture,phase,first,observations):
                source=snapshot['items'][fixture['ids']['source']]
                self.assertEqual(len(source['source_revisions']),phase)
                self.assertEqual(len(source['materials']),phase)
                # Owner fixture alone cannot pass the actual native evaluator.
                self.assertEqual(probe.evaluate(snapshot,fixture,phase)['status'],'FAIL')
                return {'status':'REVIEW_REQUIRED','mechanical_checks':{},'identities':fixture['ids'],'native_jobs':[]}
            real_evaluate=probe.evaluate
            def evaluate_without_native(*args):
                # Avoid recursive lookup while asserting against the real oracle.
                with patch.object(probe,'evaluate',real_evaluate):return lifecycle_evaluation(*args)
            driver.request=request;driver.snapshot=snapshot
            try:
                await supervisor.start_service()
                with patch.object(probe,'evaluate',evaluate_without_native):
                    result=await driver.run_case('MEETING')
                self.assertEqual(len(result['phases']),2)
                self.assertEqual(result['phases'][0]['fixture']['ids'],result['phases'][1]['fixture']['ids'])
                self.assertEqual(events,['start','suspended','start','available','suspended','start','available'])
                self.assertEqual(len(supervisor.processes),5)
                for owned in supervisor.processes[:-1]:
                    self.assertIsNotNone(owned.process.returncode)
                    self.assertTrue(owned.receipt['pid_absent'])
            finally:
                for owned in reversed(supervisor.processes):await owned.stop(2)
            self.assertTrue(all(p.receipt['pid_absent'] for p in supervisor.processes))
