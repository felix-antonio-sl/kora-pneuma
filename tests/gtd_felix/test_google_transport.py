"""Real aiohttp I/O against a local server through an explicit test session factory."""
import asyncio
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest

import aiohttp
from aiohttp import web
from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from gtd_felix.google_transport import GoogleTransport, TransportError, GMAIL, TOKEN, OIDC
from gtd_felix.google_sources import GoogleSources
from gtd_felix.source_sync import SourceSync
from gtd_felix import GTDService

ACCOUNT = 'reader@example.invalid'


class LocalSession:
    def __init__(self, base, calls, **options):
        assert options['trust_env'] is False
        self.inner = aiohttp.ClientSession(**options)
        self.base, self.calls = base, calls
    def request(self, method, url, **kwargs):
        self.calls.append((method, url, kwargs))
        assert kwargs['allow_redirects'] is False
        return self.inner.request(method, self.base, **kwargs)
    async def close(self):
        await self.inner.close()


class GoogleTransportTest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.path = Path(self.temp.name) / 'token.json'
        self.credentials = {'token':'fake-access', 'refresh_token':'fake-refresh', 'client_id':'fake-client',
                            'client_secret':'fake-secret', 'token_uri':TOKEN, 'expiry':'2099-01-01T00:00:00Z',
                            'scopes':['https://www.googleapis.com/auth/gmail.readonly']}
        self.write()
        self.calls, self.steps, self.received = [], [], []
        async def handle(request):
            self.received.append((request.method, dict(request.query), request.headers.get('Authorization'), await request.post()))
            status, body, headers = self.steps.pop(0)
            if body == 'disconnect':
                request.transport.close()
                return web.Response()
            if headers.pop('test_delay', None):
                await asyncio.sleep(0.1)
            if isinstance(body, bytes):
                response = web.StreamResponse(status=status, headers=headers)
                await response.prepare(request)
                await response.write(body)
                await response.write_eof()
                return response
            return web.json_response(body, status=status, headers=headers)
        app = web.Application(); app.router.add_route('*','/',handle)
        self.runner = web.AppRunner(app); await self.runner.setup()
        site = web.TCPSite(self.runner,'127.0.0.1',0); await site.start()
        self.base = 'http://127.0.0.1:' + str(site._server.sockets[0].getsockname()[1]) + '/'
        self.config = {'account':ACCOUNT,'token_file':str(self.path),'gmail':True,'calendar_ids':['cal@example.invalid']}
        self.transports = []
        self.transport = self.make()
    def write(self):
        self.path.write_text(json.dumps(self.credentials)); self.path.chmod(0o600)
    def make(self, **overrides):
        transport = GoogleTransport({**self.config, **overrides}, session_factory=lambda **kw: LocalSession(self.base,self.calls,**kw))
        self.transports.append(transport); return transport
    def step(self, body, status=200, **headers): self.steps.append((status,body,headers))
    async def connect(self):
        self.step({'emailAddress':ACCOUNT}); await self.transport.connect()
    async def asyncTearDown(self):
        for transport in self.transports: await transport.close()
        await self.runner.cleanup(); self.temp.cleanup()
    async def test_constructor_inert_and_real_sources_read(self):
        self.assertIsNone(self.transport.authenticated_account); self.assertEqual(self.calls,[])
        await self.connect()
        service = GTDService(Path(self.temp.name)/'store')
        try:
            sources = GoogleSources(SourceSync(service),self.transport,{'mail':{'provider':'gmail','account':ACCOUNT,'scope':'whole_mailbox'}})
            self.step({'emailAddress':ACCOUNT,'historyId':'10'}); self.step({'messages':[]})
            result = await sources.synchronize('mail')
            self.assertEqual(result['sync']['cursor'],'10')
            self.assertEqual(self.received[-1][1],{'maxResults':'100','includeSpamTrash':'true'})
            self.assertEqual(self.received[-1][2],'Bearer fake-access')
            self.assertEqual(self.transport.inspect()['verified_capabilities'],['gmail_read'])
            self.assertNotIn('fake-',json.dumps(self.transport.inspect()))
        finally: service.close()
    async def test_forbidden_routes_and_methods_never_send(self):
        await self.connect(); count=len(self.calls)
        for method,url,params in [('POST',GMAIL+'/messages',{}),('GET','http://gmail.googleapis.com/gmail/v1/users/me/messages',{}),
                ('GET',GMAIL+'/messages?access_token=x',{}),('GET',GMAIL+'/messages/../profile',{}),
                ('GET','https://www.googleapis.com/calendar/v3/calendars/other/events',{}),
                ('GET',GMAIL+'/messages',{'access_token':'x'}),('GET',GMAIL+'/messages/send',{})]:
            with self.assertRaises(TransportError): await self.transport.request(method,url,params=params)
        self.assertEqual(len(self.calls),count)
    async def test_refresh_401_once_rebinds_and_file_unchanged(self):
        before=self.path.read_bytes(); await self.connect()
        self.step({'secret':'do not expose'},401)
        self.step({'access_token':'fake-new','expires_in':3600,'scope':'https://www.googleapis.com/auth/gmail.readonly'})
        self.step({'emailAddress':ACCOUNT}); self.step({'messages':[]})
        result=await self.transport.request('GET',GMAIL+'/messages')
        self.assertEqual(result['status'],200); self.assertEqual(self.path.read_bytes(),before)
        self.assertEqual([x[0] for x in self.calls],['GET','GET','POST','GET','GET'])
        self.assertEqual(self.calls[2][1],TOKEN)
        self.assertNotIn('scope',self.received[2][3]); self.assertIsNone(self.received[2][2])
        self.assertEqual(self.received[-1][2],'Bearer fake-new')
    async def test_expiry_refresh_and_persistent_401_no_loop(self):
        self.credentials['expiry']='2000-01-01T00:00:00Z'; self.write()
        self.step({'access_token':'fake-new','expires_in':3600}); self.step({'emailAddress':ACCOUNT})
        await self.transport.connect()
        self.step({},401); self.step({'access_token':'fake-new2','expires_in':3600}); self.step({'emailAddress':ACCOUNT}); self.step({},401)
        result=await self.transport.request('GET',GMAIL+'/messages')
        self.assertEqual(result['status'],401); self.assertIsNone(self.transport.authenticated_account)
        self.assertEqual(sum(x[0]=='POST' for x in self.calls),2)
    async def test_changed_file_invalidates_before_request(self):
        await self.connect(); self.credentials['token']='different'; self.write()
        with self.assertRaisesRegex(TransportError,'credential_file_changed'): await self.transport.request('GET',GMAIL+'/messages')
        self.assertEqual(len(self.calls),1); self.assertIsNone(self.transport.authenticated_account)
        await self.connect(); self.assertEqual(self.received[-1][2],'Bearer different')
    async def test_identity_mismatch_and_rotation_are_closed(self):
        self.step({'emailAddress':'other@example.invalid'})
        with self.assertRaisesRegex(TransportError,'identity_mismatch'): await self.transport.connect()
        self.assertIsNone(self.transport.authenticated_account)
        self.credentials['expiry']='2000-01-01T00:00:00Z'; self.write(); before=self.path.read_bytes()
        self.step({'access_token':'fake-new','expires_in':3600,'refresh_token':'rotated-secret'})
        with self.assertRaisesRegex(TransportError,'refresh_rotation_requires_explicit_persistence'): await self.transport.connect()
        self.assertEqual(self.path.read_bytes(),before); self.assertIsNone(self.transport.authenticated_account)
    async def test_stream_limit_and_redirect_error_sanitization(self):
        self.transport=self.make(max_response_bytes=1024); await self.connect()
        self.step(b'x'*2048)
        with self.assertRaisesRegex(TransportError,'response_too_large'): await self.transport.request('GET',GMAIL+'/messages')
        self.step({'token':'secret'},302,Location='http://127.0.0.1:1/secret')
        result=await self.transport.request('GET',GMAIL+'/messages')
        self.assertEqual(result,{'status':302,'body':b'{}'})
        for status in (403,429):
            self.step({'token':'secret'},status,**{'Retry-After':'45'})
            result=await self.transport.request('GET',GMAIL+'/messages')
            self.assertEqual(result['body'],b'{}'); self.assertEqual(self.transport.inspect()['retry_after_seconds'],45)
        self.assertFalse(any(x[0]=='POST' for x in self.calls))
    async def test_timeout_is_sanitized_and_concurrent_refresh_serialized(self):
        slow=self.make(timeout_seconds=0.02)
        self.step({'emailAddress':ACCOUNT},test_delay=True)
        with self.assertRaisesRegex(TransportError,'http_transport_failure'):
            await slow.connect()
        self.assertIsNone(slow.authenticated_account)
        await self.connect()
        self.transport._expiry=0
        self.step({'access_token':'fake-new','expires_in':3600})
        self.step({'emailAddress':ACCOUNT}); self.step({}); self.step({})
        responses=await asyncio.gather(self.transport.request('GET',GMAIL+'/messages'),self.transport.request('GET',GMAIL+'/messages'))
        self.assertEqual([x['status'] for x in responses],[200,200])
        self.assertEqual(sum(x[0]=='POST' for x in self.calls),1)

    async def test_private_effect_gate_and_json_bearer_do_not_open_public_write(self):
        await self.connect()
        denied=await self.transport._effect_post('send',{'raw':'Zml4ZWQ'},ACCOUNT,lambda:{'status':'rejected'})
        self.assertIsNone(denied['response']);self.assertEqual(len(self.calls),1)
        self.step({'error':'sensitive'},401)
        result=await self.transport._effect_post('send',{'raw':'Zml4ZWQ'},ACCOUNT,lambda:{'status':'dispatch'})
        self.assertEqual(result['response'],{'status':401,'body':b'{}'})
        self.assertEqual(self.calls[-1][1],GMAIL+'/messages/send')
        self.assertEqual(self.calls[-1][2]['json'],{'raw':'Zml4ZWQ'})
        self.assertEqual(self.received[-1][2],'Bearer fake-access')
        self.assertEqual(sum(x[0]=='POST' for x in self.calls),1)
        with self.assertRaises(TransportError):await self.transport.request('POST',GMAIL+'/messages/send')

    async def test_delete_disconnect_public_middleware_blocks_second_io(self):
        await self.connect();self.step('disconnect')
        admission_count=[]
        def gate():admission_count.append(1);return {'status':'dispatch'}
        with self.assertRaisesRegex(TransportError,'write_retry_blocked'):
            await self.transport._calendar_effect_write('delete_copy','cal@example.invalid','event1',None,ACCOUNT,
                gate,etag='"version1"',send_updates='none')
        self.assertEqual(len(admission_count),1)
        self.assertEqual(sum(row[0]=='DELETE' for row in self.received),1)
        self.assertEqual(self.steps,[])

    async def test_calendar_private_allowlist_if_match_single_attempt(self):
        await self.connect();self.step({},412)
        result=await self.transport._calendar_effect_write('update','cal@example.invalid','event1',{'summary':'Approved'},ACCOUNT,
            lambda:{'status':'dispatch'},etag='"version1"',send_updates='none')
        self.assertEqual(result['response']['status'],412)
        self.assertEqual(self.calls[-1][0],'PATCH');self.assertEqual(self.calls[-1][2]['headers']['If-Match'],'"version1"')
        self.assertEqual(self.calls[-1][2]['params'],{'sendUpdates':'none'})
        with self.assertRaises(TransportError):
            await self.transport._calendar_effect_write('delete_copy','other','event1',None,ACCOUNT,lambda:{'status':'dispatch'},etag='"v"',send_updates='none')
        with self.assertRaises(TransportError):
            await self.transport._calendar_effect_write('update','cal@example.invalid','event1',{},ACCOUNT,lambda:{'status':'dispatch'},send_updates='none')
        self.assertEqual(len(self.calls),2)

    async def test_private_file_and_oidc_verified_email(self):
        self.path.chmod(0o644)
        with self.assertRaisesRegex(TransportError,'credential_file_invalid'): await self.transport.connect()
        self.path.chmod(0o600); link=Path(self.temp.name)/'link'; link.symlink_to(self.path)
        linked=self.make(token_file=str(link))
        with self.assertRaisesRegex(TransportError,'credential_file_invalid'): await linked.connect()
        self.credentials['scopes']=['openid','email']; self.write()
        oidc=self.make(gmail=False,identity_method='oidc')
        self.step({'email':ACCOUNT,'email_verified':False})
        with self.assertRaisesRegex(TransportError,'identity_mismatch'): await oidc.connect()
        self.step({'email':ACCOUNT,'email_verified':True}); await oidc.connect()
        self.assertEqual(self.calls[-1][1],OIDC)
        self.step({'items':[]})
        await oidc.request('GET','https://www.googleapis.com/calendar/v3/calendars/cal%40example.invalid/events')
        self.assertEqual(oidc.inspect()['verified_capabilities'],['calendar_read'])

    async def test_priority_query_only_canonical_literals_inside_fixed_date(self):
        from gtd_felix.google_sources import priority_query, SourceError
        await self.connect()
        query = priority_query(['Asistencia', 'Telemedicina HSC', 'HODOM'])
        self.step({'messages': []})
        await self.transport.request('GET', GMAIL + '/messages', params={'q': query})
        count = len(self.calls)
        for text in ['after:0 {"HODOM"}', 'after:1785556800 OR HODOM',
                     'after:1785556800 {"after:0"}', 'after:1785556800 {"HODOM"} OR older:2020',
                     'after:1785556800 {"HODOM" "HODOM"}']:
            with self.assertRaises(TransportError):
                await self.transport.request('GET', GMAIL + '/messages', params={'q': text})
        for terms in [['from:someone'], ['x" OR y'], ['x\\y'], [' x'], ['a'] * 13]:
            with self.assertRaises(SourceError):
                priority_query(terms)
        self.assertEqual(count, len(self.calls))


if __name__=='__main__': unittest.main()
