"""Durable monitoring through real Google adapters and loopback aiohttp transport."""
import asyncio
import copy
from datetime import datetime, timezone, timedelta
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from test_google_transport import LocalSession, ACCOUNT
from test_google_sources import raw_message
from aiohttp import web
from gtd_felix import GTDService
from gtd_felix.google_transport import GoogleTransport, TOKEN
from gtd_felix.source_monitor import SourceMonitor, coverage, validate_google, retire_sources, PREFIX


class SourceMonitorTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp=tempfile.TemporaryDirectory(); self.root=Path(self.temp.name)
        self.service=GTDService(self.root/'store')
        token=self.root/'token.json'; token.write_text(json.dumps({'token':'fake','expiry':'2099-01-01T00:00:00Z'})); token.chmod(0o600)
        self.config={'poll_interval_seconds':10,'stale_after_seconds':60,'accounts':{'selected':{
            'transport':{'account':ACCOUNT,'token_file':str(token),'gmail':True,'calendar_ids':['cal@example.invalid']},
            'sources':{'mail':{'provider':'gmail','account':ACCOUNT,'scope':'whole_mailbox','page_size':2}}}}}
        self.steps=[]; self.calls=[]; self.monitors=[]
        async def handle(request):
            self.assertFalse(self.service.store.db.in_transaction)
            status,body,headers=self.steps.pop(0)
            return web.json_response(body,status=status,headers=headers)
        app=web.Application();app.router.add_route('*','/',handle)
        self.runner=web.AppRunner(app);await self.runner.setup()
        site=web.TCPSite(self.runner,'127.0.0.1',0);await site.start()
        self.base='http://127.0.0.1:'+str(site._server.sockets[0].getsockname()[1])+'/'
        self.monitor=self.make()
    def make(self):
        result=SourceMonitor(self.service,self.config,transport_factory=lambda cfg:GoogleTransport(cfg,session_factory=lambda **kw:LocalSession(self.base,self.calls,**kw)))
        self.monitors.append(result);return result
    def step(self,body,status=200,**headers):self.steps.append((status,body,headers))
    def profile(self,h='10'):self.step({'emailAddress':ACCOUNT,'historyId':h})
    async def seed(self):
        self.profile();self.profile();self.step({'messages':[{'id':'m1'}]});self.step(raw_message())
        return await self.monitor.run_once('mail')
    async def asyncTearDown(self):
        for monitor in self.monitors:await monitor.close()
        await self.runner.cleanup();self.service.close();self.temp.cleanup()
    async def test_not_read_complete_stale_restart_and_semantic_review_separate(self):
        unread=self.monitor.inspect();self.assertFalse(unread['external_sources_current'])
        self.assertEqual(unread['sources'][0]['health'],'not_read')
        result=await self.seed();self.assertTrue(result['current']);self.assertEqual(result['pending_reads'],0)
        first_at=result['coverage_at']; self.assertNotIn('cursor',json.dumps(result)); self.assertNotIn('fake',json.dumps(result))
        await self.monitor.close(); self.service.close();self.service=GTDService(self.root/'store');self.monitor=self.make()
        self.assertEqual(self.monitor.inspect()['sources'][0]['coverage_at'],first_at)
        with self.service.store.transaction():
            old=self.service._meta(PREFIX+'mail');old['coverage_at']=(datetime.now(timezone.utc)-timedelta(seconds=120)).isoformat();self.service._set_meta(PREFIX+'mail',old)
        self.assertFalse(coverage(self.service)['external_sources_current'])
        review=self.service.execute('felix',{'operation_id':'review','action':'review','fields':{}})['review']
        self.assertFalse(review['external_sources_current']);self.assertTrue(review['external_sources_applicable'])
        self.assertTrue(self.service.review_state()['notification_allowed'])
    async def test_cursor_invalidation_degraded_and_pending_not_complete(self):
        await self.seed();self.profile('20');self.step({},404)
        result=await self.monitor.run_once('mail');self.assertFalse(result['current']);self.assertEqual(result['enumeration'],'rebuild_required')
        self.profile('30');self.step({'messages':[{'id':'m1'},{'id':'bad'}]});self.step(raw_message());self.step({'id':'bad'})
        result=await self.monitor.run_once('mail')
        self.assertEqual(result['enumeration'],'complete');self.assertFalse(result['originals_complete']);self.assertEqual(result['pending_reads'],1);self.assertFalse(result['current'])
    async def test_zero_items_failure_wrong_account_and_retirement(self):
        self.step({'emailAddress':'wrong@example.invalid'})
        result=await self.monitor.run_once('mail');self.assertEqual(result['health'],'degraded');self.assertFalse(result['current']);self.assertEqual(self.service.store.db.execute('SELECT COUNT(*) FROM items').fetchone()[0],0)
        self.profile();self.profile();self.step({},429,**{'Retry-After':'120'})
        result=await self.monitor.run_once('mail');self.assertEqual(result['last_error'],'http_429');self.assertEqual(result['retry_after_seconds'],120)
        retire_sources(self.service);state=coverage(self.service)
        self.assertIsNone(state['external_sources_current']);self.assertFalse(state['external_sources_applicable']);self.assertFalse(state['sources'][0]['configured'])
    async def test_cancel_closes_owned_tasks_sessions_and_legacy(self):
        entered=asyncio.Event()
        async def wait(*args):entered.set();await asyncio.Event().wait()
        with patch.object(self.monitor.transports['selected'],'connect',side_effect=wait):
            await self.monitor.start();await entered.wait();await self.monitor.close()
        self.assertEqual(self.monitor._tasks,[]);self.assertEqual(self.monitor.inspect()['sources'][0]['last_error'],'pass_cancelled')
        other=GTDService(self.root/'legacy')
        try:
            self.assertEqual(coverage(other),{'sources':[],'configured_count':0,'external_sources_applicable':False,'external_sources_current':None})
            review=other.execute('felix',{'operation_id':'r','action':'review','fields':{}})['review']
            self.assertTrue(review['operational_complete']);self.assertIsNone(review['external_sources_current'])
        finally:other.close()
    async def test_application_initializes_unread_then_retires_before_http(self):
        from gtd_felix.application import create_app, SOURCE_MONITOR
        from gtd_felix.control import ExecutionControl
        cfg={'data_dir':str(self.root/'store'),'actors':{'owner':'felix','principal':'gtd-felix'},
             'api_tokens':{'synthetic-token-long':'felix'},'google':self.config}
        app=create_app(self.service,ExecutionControl(self.service,{}),cfg)
        self.assertEqual(self.service.external_source_coverage()['sources'][0]['health'],'not_read')
        self.assertEqual(self.calls,[])
        await app[SOURCE_MONITOR].close()
        del cfg['google'];create_app(self.service,ExecutionControl(self.service,{}),cfg)
        self.assertFalse(self.service.external_source_coverage()['sources'][0]['configured'])

    async def test_restart_uses_durable_cursor_and_scope_change_unread(self):
        await self.seed();await self.monitor.close();self.monitor=self.make()
        self.profile();self.profile('20');self.step({'history':[],'historyId':'20'})
        result=await self.monitor.run_once('mail');self.assertTrue(result['current'])
        self.assertEqual(self.calls[-1][2]['params']['startHistoryId'],'10')
        self.config['accounts']['selected']['sources']['mail']['page_size']=3
        changed=self.make();self.assertEqual(changed.inspect()['sources'][0]['health'],'not_read')

    async def test_slow_account_does_not_block_other_source(self):
        cfg=copy.deepcopy(self.config['accounts']['selected'])
        cfg['transport']['account']='second@example.invalid'
        cfg['sources']={'second':{**cfg['sources']['mail'],'account':'second@example.invalid'}}
        self.config['accounts']['second']=cfg
        monitor=self.make();entered=asyncio.Event()
        async def wait():entered.set();await asyncio.Event().wait()
        self.step({'emailAddress':'second@example.invalid'})
        self.step({'emailAddress':'second@example.invalid','historyId':'2'})
        self.step({'messages':[]})
        with patch.object(monitor.transports['selected'],'connect',side_effect=wait):
            await monitor.start();await entered.wait()
            async def completed():
                while not next(x for x in monitor.inspect()['sources'] if x['source_id']=='second')['current']:
                    await asyncio.sleep(0.01)
            await asyncio.wait_for(completed(),2)
            self.assertFalse(next(x for x in monitor.inspect()['sources'] if x['source_id']=='mail')['current'])
            await monitor.close()

    async def test_background_backoff_waits_after_429(self):
        self.profile();self.profile();self.step({},429,**{'Retry-After':'120'})
        await self.monitor.start()
        async def failed():
            while self.monitor.inspect()['sources'][0]['last_error'] != 'http_429':
                await asyncio.sleep(0.01)
        await asyncio.wait_for(failed(),2)
        count=len(self.calls)
        await asyncio.sleep(0.03)
        self.assertEqual(len(self.calls),count)
        self.assertEqual(self.monitor.inspect()['sources'][0]['retry_after_seconds'],120)
        await self.monitor.close()

    async def test_configuration_rejects_cross_account_duplicate_and_unbounded(self):
        for change in ('account','duplicate','interval'):
            cfg=copy.deepcopy(self.config)
            if change=='account':cfg['accounts']['selected']['sources']['mail']['account']='other@example.invalid'
            elif change=='duplicate':cfg['accounts']['selected']['sources']['other']=copy.deepcopy(cfg['accounts']['selected']['sources']['mail'])
            else:cfg['stale_after_seconds']=1
            with self.assertRaises(ValueError):validate_google(cfg)
