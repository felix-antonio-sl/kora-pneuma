"""Local HTTP projection only; no existing credential or Telegram account."""
import asyncio
import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import pty
import select
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import aiohttp
from aiohttp import web

SCRIPT=Path(__file__).resolve().parents[2]/'scripts/gtd_telegram_connect.py'
spec=importlib.util.spec_from_file_location('gtd_telegram_connect',SCRIPT)
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
TOKEN='12345:'+'SYNTHETIC_SECRET_'*3

class TelegramConnectTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        self.path=self.root/'token';self.path.write_text(TOKEN+'\n');self.path.chmod(0o600)
        self.calls=[];self.username='korax_kv_bot';self.webhook='';self.status=200
        self.failures=0;self.huge=False
        self.updates=[];self.update_status=200;self.update_queries=[];self.disconnect_updates=False
        async def route(request):
            self.calls.append(request.match_info['method'])
            if self.calls[-1]=='getUpdates':
                self.update_queries.append(dict(request.query))
                if self.disconnect_updates:
                    request.transport.close()
                    return web.Response()
                return web.json_response({'ok':True,'result':self.updates},status=self.update_status)
            if self.failures:
                self.failures-=1;return web.Response(status=503,text=TOKEN)
            if self.status!=200:return web.Response(status=self.status,text=TOKEN)
            if self.huge:return web.Response(text=TOKEN*2000)
            value={'id':12345,'is_bot':True,'username':self.username} if self.calls[-1]=='getMe' else {'url':self.webhook,'pending_update_count':4,'last_error_message':TOKEN}
            return web.json_response({'ok':True,'result':value})
        app=web.Application();app.router.add_get('/{method}',route)
        self.runner=web.AppRunner(app,access_log=None);await self.runner.setup()
        site=web.TCPSite(self.runner,'127.0.0.1',0);await site.start()
        self.url='http://127.0.0.1:'+str(site._server.sockets[0].getsockname()[1])

    async def asyncTearDown(self):
        await self.runner.cleanup();self.temp.cleanup()

    def factory(self,**kwargs):
        owner=self
        class Local:
            async def __aenter__(self):
                self.session=aiohttp.ClientSession(**kwargs);return self
            async def __aexit__(self,*args):await self.session.close()
            def get(self,url,**options):
                assert url.startswith('https://api.telegram.org/bot'+TOKEN+'/')
                method=url.rsplit('/',1)[-1]
                assert method in {'getMe','getWebhookInfo','getUpdates'}
                assert options['allow_redirects'] is False
                return self.session.get(owner.url+'/'+method,**options)
        return Local()

    async def test_exact_identity_only_two_reads_and_safe_receipt(self):
        result=await g.inspect(self.path,session_factory=self.factory)
        self.assertEqual(self.calls,['getMe','getWebhookInfo'])
        self.assertEqual(result['status'],'verified_identity_owner_selection_pending')
        self.assertFalse(result['polling_started']);self.assertIsNone(result['chat_id'])
        self.assertNotIn(TOKEN,json.dumps(result))

    async def test_wrong_bot_stops_before_webhook_or_poll(self):
        self.username='other_bot'
        with self.assertRaisesRegex(g.Blocked,'bot_identity_mismatch'):
            await g.inspect(self.path,session_factory=self.factory)
        self.assertEqual(self.calls,['getMe'])

    async def test_webhook_present_blocks_without_exposing_url(self):
        self.webhook='https://secret.invalid/'+TOKEN
        result=await g.inspect(self.path,session_factory=self.factory)
        self.assertEqual(result['status'],'blocked_webhook_present')
        self.assertNotIn('secret.invalid',json.dumps(result))
        self.assertNotIn(TOKEN,json.dumps(result))
        self.assertEqual(self.calls,['getMe','getWebhookInfo'])

    async def test_safe_read_retry_bounded(self):
        self.failures=1
        await g.inspect(self.path,session_factory=self.factory)
        self.assertEqual(self.calls,['getMe','getMe','getWebhookInfo'])
        self.calls.clear();self.failures=10
        with self.assertRaisesRegex(g.Blocked,'telegram_temporarily_unavailable'):
            await g.inspect(self.path,attempts=3,session_factory=self.factory)
        self.assertEqual(len(self.calls),3)

    async def test_auth_error_does_not_retry_or_expose_provider_body(self):
        self.status=401
        with self.assertRaises(g.Blocked) as caught:
            await g.inspect(self.path,session_factory=self.factory)
        self.assertEqual(str(caught.exception),'telegram_authentication_failed')
        self.assertNotIn(TOKEN,str(caught.exception));self.assertEqual(self.calls,['getMe'])

    async def test_response_size_bound(self):
        self.huge=True
        with self.assertRaisesRegex(g.Blocked,'telegram_response_too_large'):
            await g.inspect(self.path,session_factory=self.factory)

    async def test_unsafe_file_never_requests(self):
        self.path.chmod(0o644)
        with self.assertRaises(g.Blocked):await g.inspect(self.path,session_factory=self.factory)
        self.path.chmod(0o600);link=self.root/'symlink';link.symlink_to(self.path)
        with self.assertRaises(OSError):await g.inspect(link,session_factory=self.factory)
        hard=self.root/'hard';os.link(self.path,hard)
        with self.assertRaises(g.Blocked):await g.inspect(self.path,session_factory=self.factory)
        self.assertEqual(self.calls,[])

    async def test_capture_requires_terminal_and_never_overwrites(self):
        with patch.object(g.sys.stdin,'isatty',return_value=False),self.assertRaisesRegex(g.Blocked,'private_terminal_required'):
            g.capture(self.root/'new')
        with patch.object(g.getpass,'getpass',side_effect=AssertionError('must not prompt')),self.assertRaisesRegex(g.Blocked,'output_exists'):
            g.capture(self.path)
        self.assertEqual(self.path.read_text(),TOKEN+'\n')
        capture=self.root/'race'
        def raced(prompt):capture.write_text('preserve');return TOKEN
        with patch.object(g.sys.stdin,'isatty',return_value=True),patch.object(g.getpass,'getpass',side_effect=raced),self.assertRaises(FileExistsError):
            g.capture(capture)
        self.assertEqual(capture.read_text(),'preserve')

    async def test_real_terminal_capture_no_echo(self):
        master,slave=pty.openpty();target=self.root/'tty-token'
        process=subprocess.Popen([sys.executable,'-E','-s','-B',str(SCRIPT),'capture','--token-file',str(target)],stdin=slave,stderr=slave,stdout=subprocess.PIPE)
        os.close(slave)
        try:
            ready,_,_=select.select([master],[],[],5)
            self.assertTrue(ready)
            prompt=os.read(master,4096)
            os.write(master,(TOKEN+'\n').encode())
            out,_=process.communicate(timeout=5)
            self.assertEqual(process.returncode,0)
            self.assertNotIn(TOKEN.encode(),out+prompt)
            self.assertEqual(target.read_text(),TOKEN+'\n')
            self.assertEqual(target.stat().st_mode&0o777,0o600)
        finally:
            if process.poll() is None:process.kill();process.wait()
            os.close(master)

    async def test_cli_sanitizes_arbitrary_failure(self):
        output=io.StringIO()
        with patch.object(g,'capture',side_effect=OSError('https://api.telegram.org/bot'+TOKEN+'/getMe')),contextlib.redirect_stderr(output):
            result=g.main(['capture','--token-file',str(self.root/'new')])
        self.assertEqual(result,2);self.assertNotIn(TOKEN,output.getvalue())

    def challenge(self):
        path=self.root/'challenge.json'
        prepared=g.prepare(path)
        self.updates=[{'update_id':7,'message':{'text':prepared['phrase'],'date':int(g.time.time()),
            'from':{'id':91,'is_bot':False,'first_name':'PRIVATE_NAME'},'chat':{'id':91,'type':'private'}}}]
        return path,prepared

    async def test_pair_one_read_no_offset_private_receipt_and_single_use(self):
        path,prepared=self.challenge()
        self.updates.insert(0,{'update_id':6,'message':{'text':'UNRELATED_BODY','from':{'id':99}}})
        result=await g.pair(self.path,path,session_factory=self.factory)
        self.assertEqual(result['owner_user_id'],91)
        self.assertEqual(result['chat_id'],91)
        self.assertEqual(self.calls,['getMe','getWebhookInfo','getUpdates'])
        self.assertNotIn('offset',self.update_queries[0])
        for private in (prepared['phrase'],'PRIVATE_NAME','UNRELATED_BODY',TOKEN):
            self.assertNotIn(private,json.dumps(result))
        with self.assertRaisesRegex(g.Blocked,'challenge_already_used'):
            await g.pair(self.path,path,session_factory=self.factory)
        self.assertEqual(self.calls.count('getUpdates'),1)

    async def test_pair_rejects_multiple_matches_wrong_chat_and_stale_message(self):
        path,_=self.challenge()
        original=json.loads(json.dumps(self.updates[0]))
        for mode in ('multiple','group','old','bot','forward'):
            self.updates=[json.loads(json.dumps(original))]
            if mode=='multiple':self.updates.append(json.loads(json.dumps(original)))
            if mode=='group':self.updates[0]['message']['chat']['type']='group'
            if mode=='old':self.updates[0]['message']['date']-=1000
            if mode=='bot':self.updates[0]['message']['from']['is_bot']=True
            if mode=='forward':self.updates[0]['message']['forward_origin']={}
            with self.subTest(mode=mode),self.assertRaises(g.Blocked):
                await g.pair(self.path,path,session_factory=self.factory)
        self.assertFalse(json.loads(path.read_text())['used'])

    async def test_pair_expiry_conflict_webhook_and_absent_challenge(self):
        path,_=self.challenge()
        self.update_status=409
        with self.assertRaisesRegex(g.Blocked,'another_receiver_conflict'):
            await g.pair(self.path,path,session_factory=self.factory)
        self.update_status=200;self.updates=[]
        with self.assertRaisesRegex(g.Blocked,'challenge_not_observed_in_window'):
            await g.pair(self.path,path,session_factory=self.factory)
        count=self.calls.count('getUpdates');self.webhook='https://private.invalid/secret'
        with self.assertRaisesRegex(g.Blocked,'webhook_present'):
            await g.pair(self.path,path,session_factory=self.factory)
        self.assertEqual(self.calls.count('getUpdates'),count)
        self.webhook='';value=json.loads(path.read_text());value['created_at']-=1000;value['expires_at']-=1000;path.write_text(json.dumps(value))
        with self.assertRaisesRegex(g.Blocked,'challenge_expired'):
            await g.pair(self.path,path,session_factory=self.factory)
        self.assertEqual(self.calls.count('getUpdates'),count)

    async def test_challenge_create_exclusive_and_unsafe_file(self):
        path,_=self.challenge()
        with self.assertRaises(FileExistsError):g.prepare(path)
        path.chmod(0o644)
        with self.assertRaisesRegex(g.Blocked,'private_challenge_required'):
            await g.pair(self.path,path,session_factory=self.factory)
        self.assertEqual(self.calls,[])

    async def test_pair_disconnect_is_never_automatically_resent(self):
        path,_=self.challenge();self.disconnect_updates=True
        with self.assertRaises(g.Blocked):
            await g.pair(self.path,path,session_factory=self.factory)
        self.assertEqual(self.calls.count('getUpdates'),1)
        self.assertFalse(json.loads(path.read_text())['used'])
