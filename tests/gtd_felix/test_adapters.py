"""Explicit provider routing over real durable control, without native models."""
import unittest
import test_codex
from gtd_felix.adapters import AdapterRouter


class HermesStub:
    def __init__(self): self.calls=[]
    async def discover(self, bot): self.calls.append(('discover',bot));return {'status':'ready'}
    async def submit(self, job, prompt, durable=False): self.calls.append(('submit',job,durable));return {'status':'submitted'}
    async def poll(self, job): self.calls.append(('poll',job));return {'status':'uncertain'}
    async def reconcile(self, job): return await self.poll(job)
    async def stop(self, job): self.calls.append(('stop',job));return {'status':'stop_requested'}
    async def steer(self, job, text): self.calls.append(('steer',job));return {'status':'steer_requested'}


class AdapterTests(unittest.IsolatedAsyncioTestCase):
    asyncSetUp=test_codex.CodexTests.asyncSetUp
    asyncTearDown=test_codex.CodexTests.asyncTearDown
    reserve=test_codex.CodexTests.reserve
    save=test_codex.CodexTests.save
    audit=test_codex.CodexTests.audit

    async def test_explicit_provider_persists_before_submit_and_rejects_change(self):
        hermes=HermesStub(); router=AdapterRouter(self.control,hermes,self.adapter,{'providers':{'codex':'codex'}})
        job=self.reserve()
        # This private action is principal-owned; Codex cannot replace the principal.
        result=await router.submit(job,'task',durable=True)
        self.assertEqual(result['error'],'codex_executor_required')
        self.assertEqual(self.audit(),[])
        self.assertEqual(hermes.calls,[])

    async def test_legacy_hermes_and_explicit_missing_provider_no_fallback(self):
        hermes=HermesStub();legacy=AdapterRouter(self.control,hermes,None,{})
        self.assertEqual((await legacy.discover('old'))['status'],'ready')
        explicit=AdapterRouter(self.control,hermes,self.adapter,{'providers':{'codex':'codex'}})
        self.assertEqual((await explicit.discover('old'))['status'],'unavailable')
        self.assertEqual(hermes.calls,[('discover','old')])

    async def prepare_executor(self):
        from gtd_felix.service import GTDService
        from gtd_felix.control import ExecutionControl
        from gtd_felix.codex import CodexAdapter
        budget={**self.control.config, "max_descendants":1}
        self.service.close()
        self.service=GTDService(self.root/'code-data',executor_actors=['code-worker'])
        self.control=ExecutionControl(self.service,budget)
        self.adapter=CodexAdapter(self.control,self.config)
        self.item=self.service.capture('felix','code-source','Synthetic project')['item']
        item=self.service.execute('felix',{'operation_id':'project','action':'clarify','item_id':self.item['id'],
            'expected_version':self.item['version'],'fields':{'kind':'project','commitment':'committed'}})['item']
        grant=self.service.execute('felix',{'operation_id':'grant','action':'grant_mandate','item_id':item['id'],
            'expected_version':item['version'],'fields':{'scope_item_id':item['id'],'capabilities':['prepare_private'],
                'actors':['code-worker','gtd-felix'],'completion_criteria':'Private synthetic work'}})
        self.assertEqual(grant['status'],'applied',grant)
        self.control.register_bot('felix','worker-bot',{'id':'codex','actor':'code-worker','state':'available',
            'source_urn':'urn:test:codex','host':'local','profile':'synthetic','capabilities':['prepare_private'],'probe_evidence':'fixture'})
        self.control.register_bot('felix','principal-bot',{'id':'principal','state':'available','source_urn':'urn:test:principal',
            'host':'local','profile':'principal','capabilities':['prepare_private'],'probe_evidence':'fixture'})
        child=self.service.execute('felix',{'operation_id':'child','action':'derive','item_id':item['id'],
            'expected_version':self.service.get_item(item['id'])['version'],'fields':{'kind':'action','title':'Synthetic code change',
                'executor':'code-worker','capability':'prepare_private'}})['item']
        parent=self.control.reserve('gtd-felix','parent-reserve',{'item_id':item['id'],
            'expected_version':self.service.get_item(item['id'])['version'],'mandate_id':grant['mandate']['id'],
            'capability':'prepare_private','bot_id':'principal','purpose':'Coordinate code','scope':'Synthetic project',
            'max_cost_usd':3,'max_runtime_seconds':50,'max_retries':0,'max_descendants':1})
        self.assertEqual(parent['status'],'reserved',parent)
        receipt=self.control.reserve('gtd-felix','code-reserve',{'item_id':child['id'],'expected_version':child['version'],
            'mandate_id':grant['mandate']['id'],'capability':'prepare_private','bot_id':'codex','purpose':'Private code',
            'scope':'Synthetic workspace','parent_job_id':parent['job_id'],'max_cost_usd':2,'max_runtime_seconds':20,'max_retries':0,'max_descendants':0})
        self.assertEqual(receipt['status'],'reserved',receipt)
        native={'provider':'hermes','host':'local','profile':'principal','id':'synthetic-parent'}
        self.control.record_dispatch(parent['job_id'],native)
        observed=self.control.observe(parent['job_id'],{'native_identity':native,'native_status':'completed','terminal':True,
            'runtime_seconds':1,'cost_usd':.1,'evidence_reference':'fixture://parent'})
        self.assertEqual(observed['status'],'recorded',observed)
        self.control.acknowledge_progress(parent['job_id'])
        return receipt['job_id'],child

    async def test_codex_material_returns_to_principal_once_without_kanban(self):
        import json
        from gtd_felix.orchestration import OrchestrationWorker
        job,child=await self.prepare_executor()
        self.settings.update(complete=True,lose_turn=True);self.save()
        hermes=HermesStub()
        router=AdapterRouter(self.control,hermes,self.adapter,{'providers':{'codex':'codex','principal':'hermes'}})
        config={'actor':'gtd-felix','principal_bot_id':'principal','reservation':{'max_cost_usd':1,'max_runtime_seconds':20,
            'max_retries':0,'max_descendants':0},'review_interval_seconds':99999}
        worker=OrchestrationWorker(self.service,self.control,router,config)
        state=worker._state();prompt=worker._prompt(self.control.get_job(job),[])
        self.assertNotIn('kanban',prompt.lower());self.assertIn(str(self.workspace),prompt)
        state['runs'][job]={'phase':'intent','prompt':prompt,'durable':True,'event_keys':[]};worker._save(state)
        await worker._advance(state,job)
        self.assertFalse(self.control.get_job(job)['terminal'])
        await router.close()
        from gtd_felix.codex import CodexAdapter
        self.adapter=CodexAdapter(self.control,self.config)
        router=AdapterRouter(self.control,hermes,self.adapter,{'providers':{'codex':'codex','principal':'hermes'}})
        worker=OrchestrationWorker(self.service,self.control,router,config)
        state=worker._state()
        await worker._advance(state,job)
        self.assertEqual(self.control.get_job(job)['integration'],'integrated')
        materials=self.service.materials(child['id']);self.assertEqual(len(materials),1)
        self.assertEqual(self.service.get_item(child['id'])['status'],'active')
        self.assertEqual(self.control.get_job(job)['charged_cost_usd'],2)
        worker._executor_returns(state)
        await worker.tick()
        principal_calls=[c for c in hermes.calls if c[0]=='submit']
        self.assertEqual(len(principal_calls),1,worker._state())
        for _ in range(3):
            worker=OrchestrationWorker(self.service,self.control,router,config);await worker.tick()
        self.assertEqual(len([c for c in hermes.calls if c[0]=='submit']),1)
        self.assertEqual(len([r for r in self.audit() if r['method']=='turn/start']),1)
        self.assertFalse(any(c[1]==job for c in hermes.calls))
        changed=AdapterRouter(self.control,hermes,self.adapter,{'providers':{'codex':'hermes','principal':'hermes'}})
        self.assertEqual((await changed.poll(job))['error'],'native_provider_mismatch')
        blob=json.loads(worker._output(await router.poll(job)))
        self.assertEqual(blob['assessment'],'pending_principal')
        self.assertFalse(blob['capabilities']['host_read_isolated'])

    async def test_human_change_discards_codex_delivery(self):
        from gtd_felix.orchestration import OrchestrationWorker
        job,child=await self.prepare_executor();self.settings['complete']=True;self.save()
        router=AdapterRouter(self.control,HermesStub(),self.adapter,{'providers':{'codex':'codex'}})
        worker=OrchestrationWorker(self.service,self.control,router,{})
        state=worker._state();state['runs'][job]={'phase':'intent','prompt':worker._prompt(self.control.get_job(job),[]),'durable':True,'event_keys':[]}
        worker._save(state);await worker._advance(state,job)
        edit=self.service.execute('felix',{'operation_id':'changed','action':'edit','item_id':child['id'],
            'expected_version':child['version'],'fields':{'completion_criteria':'New human condition'}})
        self.assertEqual(edit['status'],'applied',edit)
        await worker._advance(state,job)
        self.assertEqual(self.control.get_job(job)['integration'],'discarded')
        self.assertEqual(self.service.materials(child['id']),[])

    async def test_selection_is_durable_before_transport_and_cannot_be_replaced(self):
        from unittest.mock import AsyncMock
        import json
        job,_=await self.prepare_executor()
        hermes=HermesStub()
        router=AdapterRouter(self.control,hermes,self.adapter,{'providers':{'codex':'hermes'}})
        original_submit=hermes.submit
        async def checked_submit(*args,**kwargs):
            row=self.service.store.db.execute('SELECT value FROM metadata WHERE key=?',('adapter:job:'+job,)).fetchone()
            self.assertEqual(json.loads(row[0])['provider'],'hermes')
            return await original_submit(*args,**kwargs)
        hermes.submit=checked_submit
        await router.submit(job,'bounded',durable=True)
        row=self.service.store.db.execute('SELECT value FROM metadata WHERE key=?',('adapter:job:'+job,)).fetchone()
        self.assertEqual(json.loads(row[0])['provider'],'hermes')
        changed=AdapterRouter(self.control,hermes,self.adapter,{'providers':{'codex':'codex'}})
        self.assertEqual((await changed.submit(job,'bounded',durable=True))['error'],'adapter_selection_changed')
        self.assertEqual(self.audit(),[])
        self.assertEqual(len(hermes.calls),1)

    async def test_bootstrap_routes_discovery_and_preserves_suspension(self):
        from gtd_felix.cli import bootstrap_bots
        await self.prepare_executor()
        hermes=HermesStub();router=AdapterRouter(self.control,hermes,self.adapter,{'providers':{'codex':'codex','principal':'hermes'}})
        bots=self.control.bots()
        receipts=await bootstrap_bots(self.service,self.control,router,bots)
        self.assertTrue(all(r['status']=='applied' for r in receipts),receipts)
        self.assertIn(('discover','principal'),hermes.calls)
        self.assertNotIn('turn/start',[x['method'] for x in self.audit()])
        self.assertEqual([x for x in self.control.bots() if x['id']=='codex'][0]['probe_evidence']['adapter_provider'],'codex')
        bot=next(b for b in self.control.bots() if b['id']=='codex')
        self.control.register_bot('felix','suspend-code',{**bot,'state':'suspended'})
        before=len(self.audit())
        receipt=await bootstrap_bots(self.service,self.control,router,[bot])
        self.assertEqual(receipt[0]['status'],'preserved')
        self.assertEqual(len(self.audit()),before)

    async def test_cli_constructs_router_and_closes_transports(self):
        import asyncio
        from unittest.mock import patch
        from gtd_felix.cli import serve
        seen={}
        class Native(HermesStub):
            def __init__(self,*args): super().__init__();seen.setdefault('natives',[]).append(self)
            async def close(self): self.calls.append(('close',))
        class Worker:
            def __init__(self,service,control,adapter,config): seen['router']=adapter
            async def run(self,stop): await stop.wait()
        def run_app(app,**kwargs):
            async def lifecycle():
                generator=app.cleanup_ctx[0](app)
                await generator.__anext__()
                await generator.aclose()
            asyncio.run(lifecycle())
        config={'data_dir':str(self.root/'cli-data'),'actors':{'owner':'felix','principal':'gtd-felix','executors':['code-worker']},
            'api_tokens':{'synthetic-owner-token-for-cli':'felix'},'budget':self.control.config,'bots':[],
            'codex':self.config,'adapters':{'providers':{'principal':'hermes','codex':'codex'}},
            'orchestration':{'principal_bot_id':'principal'}}
        with patch('gtd_felix.hermes.HermesAdapter',Native),patch('gtd_felix.codex.CodexAdapter',Native), \
             patch('gtd_felix.orchestration.OrchestrationWorker',Worker),patch('gtd_felix.cli.web.run_app',run_app):
            await asyncio.to_thread(serve,config)
            self.assertIsInstance(seen['router'],AdapterRouter)
            self.assertEqual(seen['router'].provider('codex'),'codex')
            self.assertTrue(all(('close',) in n.calls for n in seen['natives']))
            config['data_dir']=str(self.root/'cli-bad')
            config['adapters']['providers']['principal']='codex'
            with self.assertRaisesRegex(ValueError,'principal_hermes_required'):
                await asyncio.to_thread(serve,config)
