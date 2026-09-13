"""Trusted effects ledger + real aiohttp, synthetic credentials and local Gmail server."""
import asyncio
import base64
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from aiohttp import web
from test_google_transport import LocalSession, ACCOUNT
from gtd_felix import GTDService
from gtd_felix.effects import ExternalEffects
from gtd_felix.gmail_effects import GmailEffects, compare_mime, GmailEffectError
from gtd_felix.google_transport import GoogleTransport


class GmailEffectsTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        self.service=GTDService(self.root/'store');self.effects=ExternalEffects(self.service)
        self.mime='Message-ID: <fixed@example.invalid>\r\nDate: Fri, 11 Sep 2026 10:00:00 +0000\r\nFrom: '+ACCOUNT+'\r\nTo: recipient@example.invalid\r\nBcc: private@example.invalid\r\nSubject: Prepared\r\nMIME-Version: 1.0\r\nContent-Type: text/plain; charset=utf-8\r\nContent-Transfer-Encoding: 7bit\r\n\r\nApproved body\r\n'
        item=self.service.capture('felix','capture','Source is not permission')['item']
        result=self.service.execute('gtd-felix',{'operation_id':'material','action':'put_material','item_id':item['id'],'expected_version':item['version'],'fields':{'content':self.mime}})
        self.item=result['item'];material=self.service.materials(item['id'])[0]
        self.material={'id':material['id'],'version':material['version'],'sha256':material['original']['sha256']}
        token=self.root/'token.json';token.write_text(json.dumps({'token':'fake','expiry':'2099-01-01T00:00:00Z'}));token.chmod(0o600)
        self.steps=[];self.calls=[];self.writes=[]
        async def handle(request):
            self.assertFalse(self.service.store.db.in_transaction)
            if request.method=='POST':self.writes.append(await request.json())
            status,body=self.steps.pop(0)
            if body=='disconnect':request.transport.close();return web.Response()
            return web.json_response(body,status=status)
        app=web.Application();app.router.add_route('*','/',handle)
        self.runner=web.AppRunner(app);await self.runner.setup()
        site=web.TCPSite(self.runner,'127.0.0.1',0);await site.start()
        self.base='http://127.0.0.1:'+str(site._server.sockets[0].getsockname()[1])+'/'
        self.transport=GoogleTransport({'account':ACCOUNT,'token_file':str(token),'gmail':True},session_factory=lambda **kw:LocalSession(self.base,self.calls,**kw))
        self.driver=GmailEffects(self.effects,self.transport)
    async def asyncTearDown(self):await self.transport.close();await self.runner.cleanup();self.service.close();self.temp.cleanup()
    def step(self,body,status=200):self.steps.append((status,body))
    def preflight(self,alias=ACCOUNT):
        self.step({'emailAddress':ACCOUNT});self.step({'sendAs':[{'sendAsEmail':alias,'verificationStatus':'accepted'}]})
    def propose(self,action='send',authorized=True,**extra):
        proposal={'provider':'gmail','account':ACCOUNT,'action':action,'item_id':self.item['id'],'target':{'id':None},
            'payload':{'mime':self.mime,'message_id':'<fixed@example.invalid>'},'material':self.material,
            'expires_at':(datetime.now(timezone.utc)+timedelta(hours=1)).isoformat(),**extra}
        effect=self.effects.propose('gtd-felix','proposal',proposal)['effect']
        if authorized:self.effects.authorize('felix','authorize',effect['id'],effect['proposal_hash'])
        return effect
    def readback(self,draft=False,raw=None):
        message={'id':'message1','threadId':'thread1','labelIds':['DRAFT' if draft else 'SENT'],
            'raw':base64.urlsafe_b64encode(raw if raw is not None else self.mime.encode()).decode()}
        return {'id':'draft1','message':message} if draft else message
    async def test_send_readback_exact_and_echo_never_resends(self):
        effect=self.propose();self.preflight();self.step({'id':'message1','threadId':'thread1'})
        self.step({'emailAddress':ACCOUNT});self.step(self.readback())
        result=await self.driver.dispatch(effect['id']);self.assertEqual(result['status'],'confirmed',result)
        self.assertEqual(len(self.writes),1);self.assertEqual(base64.urlsafe_b64decode(self.writes[0]['raw']+'=='),self.mime.encode())
        again=await self.driver.dispatch(effect['id']);self.assertTrue(again['duplicate']);self.assertEqual(len(self.writes),1)
        current=self.effects.get('felix',effect['id']);comparison=current['observations'][-1]['readback']['comparison']
        self.assertEqual(comparison['comparison_profile'],'gmail-approved-mime-v1')
        evidence=self.service._meta(result['evidence_reference'])
        self.assertEqual((self.service.data_dir/evidence['original']['path']).stat().st_mode & 0o777,0o600)
        self.assertEqual(json.loads((self.service.data_dir/evidence['original']['path']).read_bytes())['id'],'message1')
    async def test_draft_readback_normalized_mime_and_human_update_preserved(self):
        effect=self.propose('draft_create');self.preflight();self.step({'id':'draft1'})
        normalized=b'Received: by synthetic\r\n'+self.mime.encode().replace(b'Content-Transfer-Encoding: 7bit',b'Content-Transfer-Encoding: base64').replace(b'Approved body\r\n',base64.b64encode(b'Approved body\n'))
        self.step({'emailAddress':ACCOUNT});self.step(self.readback(True,normalized))
        self.assertEqual((await self.driver.dispatch(effect['id']))['status'],'confirmed')
    async def test_draft_update_has_no_write_even_when_human_changed(self):
        effect=self.propose('draft_update',target={'id':'draft1'},expected_remote_version='old')
        self.preflight();self.step({'id':'draft1','message':{'id':'human','raw':'human-changed'}})
        result=await self.driver.dispatch(effect['id']);self.assertEqual(result['reason'],'draft_update_has_no_native_cas')
        self.assertTrue(result['remote_preserved']);self.assertEqual(self.writes,[])
        self.assertNotIn('dispatch',self.effects.get('felix',effect['id']))
    async def test_wrong_alias_and_technical_receipt_do_not_authorize(self):
        effect=self.propose(authorized=False);self.preflight('other@example.invalid')
        self.assertEqual((await self.driver.dispatch(effect['id']))['status'],'conflict');self.assertEqual(self.writes,[])
        self.preflight();result=await self.driver.dispatch(effect['id'])
        self.assertEqual(result['error'],'external_authorization_required');self.assertEqual(self.writes,[])
    async def test_revocation_immediately_before_post_rejects(self):
        effect=self.propose();self.preflight();original=self.effects.begin_dispatch
        def gate(identity):
            self.effects.revoke('felix','revoke',effect_id=identity)
            return original(identity)
        with patch.object(self.effects,'begin_dispatch',side_effect=gate):result=await self.driver.dispatch(effect['id'])
        self.assertEqual(result['status'],'rejected');self.assertEqual(self.writes,[])
    async def test_two_proposals_same_message_id_concurrent_and_new_driver_one_post(self):
        first=self.propose()
        second=self.effects.propose('gtd-felix','proposal2',first['proposal'])['effect']
        self.effects.authorize('felix','authorize2',second['id'],second['proposal_hash'])
        self.step({'emailAddress':ACCOUNT});await self.transport.connect()
        self.step({'id':'message1'});self.step({'emailAddress':ACCOUNT});self.step(self.readback())
        async def prepared(effect):return None
        with patch.object(self.driver,'_preflight',side_effect=prepared):
            results=await asyncio.gather(self.driver.dispatch(first['id']),self.driver.dispatch(second['id']))
        self.assertEqual(sorted(x['status'] for x in results),['confirmed','rejected']);self.assertEqual(len(self.writes),1)
        self.service.close();self.service=GTDService(self.root/'store');self.effects=ExternalEffects(self.service)
        restarted=GmailEffects(self.effects,self.transport)
        loser=next(x['effect_id'] for x in results if x['status']=='rejected')
        with patch.object(restarted,'_preflight',side_effect=prepared):result=await restarted.dispatch(loser)
        self.assertEqual(result['error'],'message_id_already_dispatched');self.assertEqual(len(self.writes),1)
        sent=base64.urlsafe_b64decode(self.writes[0]['raw']+'==')
        self.assertIn(b'Message-ID: <fixed@example.invalid>',sent)

    async def test_basis_changed_immediately_before_gate_no_post(self):
        effect=self.propose();self.preflight();original=self.effects.begin_dispatch
        def changed(identity):
            item=self.service.get_item(self.item['id'])
            self.service.execute('felix',{'operation_id':'human-change','action':'edit','item_id':item['id'],'expected_version':item['version'],'fields':{'text':'Changed human source'}})
            return original(identity)
        with patch.object(self.effects,'begin_dispatch',side_effect=changed):result=await self.driver.dispatch(effect['id'])
        self.assertEqual(result['status'],'rejected');self.assertEqual(self.writes,[])

    async def test_false_thread_blocks_before_dispatch(self):
        effect=self.propose(payload={'mime':self.mime,'message_id':'<fixed@example.invalid>','thread_id':'thread1'})
        self.preflight();self.step({'id':'other-thread','messages':[]})
        result=await self.driver.dispatch(effect['id'])
        self.assertEqual(result['status'],'conflict');self.assertEqual(self.writes,[])

    async def test_reply_requires_exact_real_parent_references_and_subject(self):
        self.mime=self.mime.replace('Subject: Prepared', 'In-Reply-To: <parent@example.invalid>\r\nReferences: <parent@example.invalid>\r\nSubject: Prepared')
        item=self.service.get_item(self.item['id'])
        self.service.execute('gtd-felix',{'operation_id':'reply-material','action':'put_material','item_id':item['id'],'expected_version':item['version'],'fields':{'content':self.mime}})
        material=self.service.materials(item['id'])[-1]
        self.material={'id':material['id'],'version':material['version'],'sha256':material['original']['sha256']}
        effect=self.propose(payload={'mime':self.mime,'message_id':'<fixed@example.invalid>','thread_id':'thread1'})
        self.preflight();self.step({'id':'thread1','messages':[{'id':'parent1','threadId':'thread1','payload':{'headers':[
            {'name':'Message-ID','value':'<parent@example.invalid>'},{'name':'Subject','value':'Prepared'}]}}]})
        self.step({'id':'message1'});self.step({'emailAddress':ACCOUNT});self.step(self.readback())
        result=await self.driver.dispatch(effect['id']);self.assertEqual(result['status'],'confirmed',result)
        self.assertEqual(self.writes[0]['threadId'],'thread1')

    async def test_ambiguous_search_is_not_a_confirmation(self):
        effect=self.propose();self.effects.begin_dispatch(effect['id'])
        self.step({'emailAddress':ACCOUNT});self.step({'messages':[{'id':'a'},{'id':'b'}]})
        self.assertEqual((await self.driver.reconcile(effect['id']))['status'],'uncertain')
        self.assertEqual(self.writes,[])

    async def test_write_429_is_uncertain_without_retry(self):
        effect=self.propose();self.preflight();self.step({'sensitive':'provider body'},429)
        result=await self.driver.dispatch(effect['id']);self.assertEqual(result['status'],'uncertain')
        self.assertEqual(len(self.writes),1)

    def test_decoded_attachment_hash_must_match(self):
        raw=b'MIME-Version: 1.0\r\nContent-Type: multipart/mixed; boundary=x\r\n\r\n--x\r\nContent-Type: application/octet-stream\r\nContent-Disposition: attachment; filename=a.bin\r\nContent-Transfer-Encoding: base64\r\n\r\nQUJD\r\n--x--\r\n'
        compare_mime(raw,raw)
        with self.assertRaises(GmailEffectError):compare_mime(raw,raw.replace(b'QUJD',b'WFla'))

    async def test_lost_ack_reconciles_one_hit_and_never_reposts(self):
        effect=self.propose();self.preflight();self.step('disconnect')
        self.assertEqual((await self.driver.dispatch(effect['id']))['status'],'uncertain')
        self.step({'emailAddress':ACCOUNT});self.step({'messages':[{'id':'message1'}]});self.step(self.readback())
        result=await self.driver.reconcile(effect['id']);self.assertEqual(result['status'],'confirmed',result)
        self.assertEqual(len(self.writes),1)
        self.assertEqual(self.calls[-2][2]['params']['q'],'rfc822msgid:<fixed@example.invalid>')
    async def test_empty_search_or_unverifiable_bcc_remain_uncertain(self):
        effect=self.propose();self.effects.begin_dispatch(effect['id'])
        self.step({'emailAddress':ACCOUNT});self.step({'messages':[]})
        self.assertEqual((await self.driver.reconcile(effect['id']))['status'],'uncertain')
        self.step({'emailAddress':ACCOUNT});self.step({'messages':[{'id':'message1'}]})
        self.step(self.readback(raw=self.mime.replace('Bcc: private@example.invalid\r\n','').encode()))
        self.assertEqual((await self.driver.reconcile(effect['id']))['status'],'uncertain');self.assertEqual(self.writes,[])
    async def test_write_401_no_refresh_no_retry_no_error_body(self):
        effect=self.propose();self.preflight();self.step({'secret':'do not persist'},401)
        result=await self.driver.dispatch(effect['id']);self.assertEqual(result['status'],'uncertain');self.assertEqual(len(self.writes),1)
        self.assertNotIn('secret',json.dumps(self.effects.get('felix',effect['id'])))
        self.assertEqual(sum(call[0]=='POST' for call in self.calls),1)
    def test_semantic_profile_rejects_recipient_body_attachment_changes(self):
        for altered in [self.mime.replace('recipient@example.invalid','other@example.invalid'),self.mime.replace('Approved body','Different body'),self.mime.replace('text/plain','application/octet-stream')]:
            with self.assertRaises(GmailEffectError):compare_mime(self.mime.encode(),altered.encode())
