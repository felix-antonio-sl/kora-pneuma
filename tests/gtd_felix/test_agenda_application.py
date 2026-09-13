"""Window reads through real aiohttp/MCP/CLI; inert configured provider transport."""
import asyncio
import copy
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from runtime_location import RUNTIME
sys.path.insert(0,str(RUNTIME))
import aiohttp
from aiohttp import web
from gtd_felix.application import create_app
from gtd_felix.control import ExecutionControl
from gtd_felix.service import GTDService
from gtd_felix.source_monitor import SourceMonitor
from gtd_felix.mcp import MCPClient,TOOLS
from test_mcp import budget

ACCOUNT='agenda@example.invalid'
CAL1='calendar+one@example.invalid'
CAL2='calendar/two@example.invalid'
START='2026-03-28T00:00:00+01:00'
END='2026-03-31T00:00:00+02:00'

class Transport:
    def __init__(self,config):
        self.account=config['account'];self.authenticated_account=None;self.calls=[];self.pages={};self.failure=None
    async def _effect_prepare(self,account):
        self.calls.append(('prepare',account))
        if self.failure:raise RuntimeError(self.failure)
        assert account==self.account;self.authenticated_account=account
    async def _calendar_effect_get(self,calendar,params=None):
        self.calls.append((calendar,copy.deepcopy(params)))
        value=self.pages.get((calendar,(params or {}).get('pageToken')),{'items':[]})
        if isinstance(value,int):return {'status':value,'body':b'{"secret":"provider-private"}'}
        return {'status':200,'body':json.dumps(value).encode()}
    def inspect(self):return {'state':'synthetic'}
    async def close(self):pass

class AgendaApplicationTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        self.service=GTDService(self.root/'data',executor_actors=['worker'])
        self.control=ExecutionControl(self.service,budget());self.transports={}
        def factory(config):
            t=Transport(config);self.transports[config['account']]=t;return t
        google={'poll_interval_seconds':10,'stale_after_seconds':60,'accounts':{
            'selected + alias':{'transport':{'account':ACCOUNT,'token_file':str(self.root/'never-read-token'),'gmail':False,'calendar_ids':[CAL1,CAL2],'identity_method':'oidc'},
             'sources':{'calendar':{'provider':'calendar','account':ACCOUNT,'calendar_id':CAL1,'scope':'calendar_masters_and_exceptions'}}},
            'mail-only':{'transport':{'account':'mail@example.invalid','token_file':str(self.root/'never-read-mail-token'),'gmail':True,'calendar_ids':[]},
             'sources':{'mail':{'provider':'gmail','account':'mail@example.invalid','scope':'whole_mailbox'}}}}}
        config={'data_dir':str(self.root/'data'),'actors':{'owner':'felix','principal':'gtd-felix','executors':['worker']},
                'api_tokens':{'synthetic-owner-token':'felix','synthetic-principal-token':'gtd-felix','synthetic-executor-token':'worker'},'google':google}
        with patch('gtd_felix.source_monitor.SourceMonitor',side_effect=lambda service,cfg:SourceMonitor(service,cfg,transport_factory=factory)):
            self.app=create_app(self.service,self.control,config)
        self.runner=web.AppRunner(self.app,access_log=None);await self.runner.setup()
        site=web.TCPSite(self.runner,'127.0.0.1',0);await site.start()
        self.url='http://127.0.0.1:'+str(site._server.sockets[0].getsockname()[1]);self.transport=self.transports[ACCOUNT]
        self.params={'account_alias':'selected + alias','start':START,'end':END,'timezone':'Europe/Berlin'}
    async def asyncTearDown(self):
        await self.runner.cleanup();self.service.close();self.temp.cleanup()
    async def get(self,params=None,token='principal'):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url+'/v1/agenda',params=self.params if params is None else params,headers={'Authorization':'Bearer synthetic-'+token+'-token'}) as response:
                return response.status,await response.json()
    def metadata(self):return self.service.store.db.execute('SELECT key,value FROM metadata ORDER BY key').fetchall()
    async def test_default_multicalendar_pagination_and_coverage_unchanged(self):
        self.transport.pages[(CAL1,None)]={'items':[],'nextPageToken':'second'}
        self.transport.pages[(CAL1,'second')]={'items':[{'id':'day','start':{'date':'2026-03-29'},'end':{'date':'2026-03-30'}}],'timeZone':'Europe/Berlin'}
        before=self.metadata();status,result=await self.get(token='owner')
        self.assertEqual(status,200,result);self.assertEqual(result['status'],'complete')
        self.assertEqual(result['verified_account'],ACCOUNT);self.assertEqual(result['calendar_ids'],[CAL1,CAL2])
        self.assertEqual(result['calendars'][0]['pages'],2)
        self.assertEqual(result['calendars'][0]['occurrences'][0]['interval']['start'],'2026-03-28T23:00:00+00:00')
        self.assertFalse(result['synchronization_coverage_updated']);self.assertEqual(self.metadata(),before)
    async def test_subset_degraded_and_sanitized_failure(self):
        before=self.metadata();self.transport.pages[(CAL2,None)]=403
        status,result=await self.get({**self.params,'calendar_id':CAL2})
        self.assertEqual(result['status'],'degraded');self.assertEqual(result['calendar_ids'],[CAL2])
        self.assertNotIn('provider-private',json.dumps(result));self.assertNotIn(CAL1,[c[0] for c in self.transport.calls])
        self.transport.failure='token=secret-provider-body'
        _,result=await self.get();self.assertEqual(result['error'],'agenda_read_failed')
        self.assertNotIn('secret',json.dumps(result));self.assertEqual(self.metadata(),before)
    async def test_role_and_invalid_inputs_do_no_io(self):
        cases=[({**self.params,'unknown':'x'},'owner'),({**self.params,'account_alias':'other'},'owner'),
            ({**self.params,'account_alias':'mail-only'},'owner'),({**self.params,'calendar_id':'foreign'},'owner'),
            ({**self.params,'start':'invalid'},'owner'),({**self.params,'timezone':'bad-zone'},'owner'),
            (list(self.params.items())+[('calendar_id',CAL1),('calendar_id',CAL1)],'owner'),
            (list(self.params.items())+[('start',START)],'owner'),(self.params,'executor')]
        for params,token in cases:
            with self.subTest(params=params,token=token):
                status,_=await self.get(params,token);self.assertIn(status,(400,403))
        self.assertTrue(all(not t.calls for t in self.transports.values()))
    async def test_mcp_three_tools_and_cli_escaping_repeated_calendar(self):
        self.assertEqual(len(TOOLS),3)
        client=MCPClient(self.url,'synthetic-principal-token')
        result=await client.call('gtd_read',{'view':'agenda',**self.params,'calendar_ids':[CAL2],'job_id':'current-read-context'})
        self.assertEqual(result['calendar_ids'],[CAL2])
        before=len(self.transport.calls)
        for change in ({'unknown':'extra'},{'calendar_ids':[]},{'calendar_ids':[CAL1,CAL1]}):
            with self.assertRaises(ValueError):await client.call('gtd_read',{'view':'agenda',**self.params,**change})
        self.assertEqual(len(self.transport.calls),before)
        process=await asyncio.create_subprocess_exec(sys.executable,'-B','-m','gtd_felix','--url',self.url,'agenda',
            '--account-alias',self.params['account_alias'],'--start',START,'--end',END,'--timezone','Europe/Berlin',
            '--calendar-id',CAL2,'--calendar-id',CAL1,env={**os.environ,'GTD_API_TOKEN':'synthetic-principal-token','PYTHONPATH':str(RUNTIME)},
            stdout=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.PIPE)
        out,err=await asyncio.wait_for(process.communicate(),10)
        self.assertEqual(process.returncode,0,err.decode());result=json.loads(out)
        self.assertEqual(result['calendar_ids'],[CAL2,CAL1]);self.assertEqual(result['window']['start'],START)

    async def test_pagination_failure_does_not_upgrade_window_or_sync(self):
        self.transport.pages[(CAL1,None)]={'items':[],'nextPageToken':'same'}
        self.transport.pages[(CAL1,'same')]={'items':[],'nextPageToken':'same'}
        before=self.metadata();_,result=await self.get({**self.params,'calendar_id':CAL1})
        self.assertEqual(result['status'],'degraded')
        self.assertEqual(result['calendars'][0]['error'],'pagination_not_progressing')
        self.assertEqual(self.metadata(),before)
