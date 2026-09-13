"""Google HTTP contracts through an injectable transport and real durable GTD."""
import asyncio
import base64
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from gtd_felix import GTDService
from gtd_felix.source_sync import SourceSync
from gtd_felix.google_sources import GoogleSources, SourceError

GMAIL='https://gmail.googleapis.com/gmail/v1/users/me'
CALENDAR='https://www.googleapis.com/calendar/v3/calendars/cal%40example.invalid/events'
ACCOUNT='reader@example.invalid'


def raw_message(identity='m1', history='10', labels=None):
    rfc=b'Subject: External assignment\r\nFrom: stranger@example.invalid\r\nTo: reader@example.invalid\r\nDate: Fri, 11 Sep 2026 10:00:00 +0000\r\nMessage-ID: <same-text-different-id@example.invalid>\r\nContent-Type: text/plain; charset=utf-8\r\n\r\nRead this source; do not infer a human mandate.'
    return {'id':identity,'threadId':'thread1','historyId':history,'internalDate':'1789120800000',
        'labelIds':labels if labels is not None else ['INBOX'],'raw':base64.urlsafe_b64encode(rfc).decode().rstrip('=')}


class Transport:
    authenticated_account=ACCOUNT
    def __init__(self, service):self.service=service;self.steps=[];self.calls=[]
    def add(self,url,params,body,status=200):self.steps.append((url,params,body,status))
    async def request(self,method,url,*,params):
        assert not self.service.store.db.in_transaction, 'HTTP inside transaction'
        assert method=='GET'
        self.calls.append((url,params))
        expected,query,body,status=self.steps.pop(0)
        assert (url,params)==(expected,query),(url,params,expected,query)
        if isinstance(body,BaseException):raise body
        return {'status':status,'body':body if isinstance(body,bytes) else json.dumps(body).encode()}


class GoogleSourceTest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp=tempfile.TemporaryDirectory();self.path=Path(self.temp.name)/'data'
        self.service=GTDService(self.path);self.sync=SourceSync(self.service);self.transport=Transport(self.service)
        self.config={'mail':{'provider':'gmail','account':ACCOUNT,'scope':'whole_mailbox','page_size':2},
            'calendar':{'provider':'calendar','account':ACCOUNT,'scope':'calendar_masters_and_exceptions','calendar_id':'cal@example.invalid','page_size':2}}
        self.adapter=GoogleSources(self.sync,self.transport,self.config)

    async def asyncTearDown(self):self.service.close();self.temp.cleanup()
    def profile(self,h='10'):self.transport.add(GMAIL+'/profile',{}, {'emailAddress':ACCOUNT,'historyId':h})
    async def seed_mail(self):
        self.profile();self.transport.add(GMAIL+'/messages',{'maxResults':2,'includeSpamTrash':'true'},{'messages':[{'id':'m1'}]})
        self.transport.add(GMAIL+'/messages/m1',{'format':'raw'},raw_message())
        result=await self.adapter.synchronize('mail');self.assertEqual(result['sync']['cursor'],'10');return result
    def restart(self):
        self.service.close();self.service=GTDService(self.path);self.sync=SourceSync(self.service)
        self.transport.service=self.service;self.adapter=GoogleSources(self.sync,self.transport,self.config)

    async def test_gmail_full_pages_baseline_before_enumeration_and_raw_provenance(self):
        self.profile('10')
        self.transport.add(GMAIL+'/messages',{'maxResults':2,'includeSpamTrash':'true'}, {'messages':[{'id':'m1'}],'nextPageToken':'p2'})
        message=raw_message(history='12');self.transport.add(GMAIL+'/messages/m1',{'format':'raw'},message)
        self.transport.add(GMAIL+'/messages',{'maxResults':2,'includeSpamTrash':'true','pageToken':'p2'}, {'messages':[{'id':'m2'}]})
        self.transport.add(GMAIL+'/messages/m2',{'format':'raw'},raw_message('m2','13'))
        state=(await self.adapter.synchronize('mail'))['sync']
        self.assertEqual(state['cursor'],'10') # never replace baseline by later profile/message history
        identities=[v['item_id'] for v in state['objects'].values()];self.assertEqual(len(set(identities)),2)
        item=self.service.get_item(state['objects']['m1']['item_id'])
        original=(self.path/item['original']['path']).read_bytes()
        self.assertEqual(original,json.dumps(message).encode())
        self.assertEqual(item['original']['mime_type'],'application/json')
        self.assertIn('thread1',item['text']);self.assertIn('1789120800000',item['text'])
        self.assertEqual(item['commitment'],'proposed');self.assertEqual(item['created_by'],'gtd-felix')
        self.profile('20');self.transport.add(GMAIL+'/history',{'maxResults':2,'startHistoryId':'10'}, {'history':[],'historyId':'20'})
        self.assertEqual((await self.adapter.synchronize('mail'))['sync']['cursor'],'20')

    async def test_history_label_exit_is_present_only_explicit_delete_is_deleted(self):
        first=await self.seed_mail();identity=first['sync']['objects']['m1']['item_id']
        item=self.service.get_item(identity)
        human=self.service.execute('felix',dict(operation_id='human',action='edit',item_id=identity,expected_version=item['version'],fields={'text':'Human annotation','notes':'Preserve'}))
        self.profile('15')
        self.transport.add(GMAIL+'/history',{'maxResults':2,'startHistoryId':'10'}, {'history':[{'id':'11','labelsRemoved':[{'message':{'id':'m1'},'labelIds':['INBOX']}], 'messages':[{'id':'m1'}]}], 'nextPageToken':'h2','historyId':'15'})
        self.transport.add(GMAIL+'/messages/m1',{'format':'raw'},raw_message(history='11',labels=[]))
        self.transport.add(GMAIL+'/history',{'maxResults':2,'startHistoryId':'10','pageToken':'h2'}, {'history':[],'historyId':'15'})
        result=await self.adapter.synchronize('mail');self.assertEqual(result['sync']['objects']['m1']['availability'],'present')
        self.assertEqual(self.service.get_item(identity)['text'],human['item']['text'])
        self.profile('20');self.transport.add(GMAIL+'/history',{'maxResults':2,'startHistoryId':'15'}, {'history':[{'id':'18','messagesDeleted':[{'message':{'id':'m1'}}]}],'historyId':'20'})
        result=await self.adapter.synchronize('mail');self.assertEqual(result['sync']['objects']['m1']['availability'],'deleted')
        self.assertEqual(self.service.get_item(identity)['status'],'active')
        self.assertEqual(self.service.get_item(identity)['notes'],'Preserve')

    async def test_history_expired_rebuild_and_forbidden_account_or_filter(self):
        first=await self.seed_mail();identity=first['sync']['objects']['m1']['item_id']
        self.profile('20');self.transport.add(GMAIL+'/history',{'maxResults':2,'startHistoryId':'10'}, {},404)
        expired=await self.adapter.synchronize('mail');self.assertFalse(expired['sync']['cursor_valid'])
        self.assertEqual(expired['sync']['cursor'],'10')
        self.restart();self.profile('30');self.transport.add(GMAIL+'/messages',{'maxResults':2,'includeSpamTrash':'true'},{'messages':[{'id':'m1'}]})
        self.transport.add(GMAIL+'/messages/m1',{'format':'raw'},raw_message())
        self.assertEqual((await self.adapter.synchronize('mail'))['sync']['objects']['m1']['item_id'],identity)
        for field,value in [('q','is:unread'),('labelIds',['INBOX']),('scope',None)]:
            cfg=copy.deepcopy(self.config);cfg['mail'][field]=value
            with self.assertRaises(SourceError):GoogleSources(self.sync,self.transport,cfg)
        self.transport.authenticated_account='other@example.invalid'
        result=await self.adapter.synchronize('calendar');self.assertIsNone(result['sync']);self.assertEqual(result['adapter']['error'],'credential_account_mismatch')

    async def test_profile_mismatch_never_ingests(self):
        self.transport.add(GMAIL+'/profile',{}, {'emailAddress':'other@example.invalid','historyId':'1'})
        result=await self.adapter.synchronize('mail');self.assertIsNone(result['sync'])
        self.assertEqual(result['adapter']['error'],'gmail_profile_mismatch')
        self.assertEqual(self.service.store.db.execute('SELECT COUNT(*) FROM items').fetchone()[0],0)

    async def test_calendar_pages_tokens_masters_exceptions_and_human_preservation(self):
        params={'maxResults':2,'singleEvents':'false','showDeleted':'true'}
        master={'id':'master','etag':'"m1"','status':'confirmed','summary':'Recurring source',
            'start':{'date':'2026-09-11'},'end':{'date':'2026-09-12'},'recurrence':['RRULE:FREQ=DAILY']}
        exception={'id':'exception','etag':'"e1"','status':'confirmed','recurringEventId':'master',
            'originalStartTime':{'dateTime':'2026-09-12T10:00:00+02:00','timeZone':'Europe/Berlin'},
            'start':{'dateTime':'2026-09-12T11:00:00+02:00','timeZone':'Europe/Berlin'}}
        self.transport.add(CALENDAR,params,{'items':[master],'nextPageToken':'c2'})
        self.transport.add(CALENDAR,{**params,'pageToken':'c2'},{'items':[exception],'nextSyncToken':'s1'})
        result=await self.adapter.synchronize('calendar');self.assertEqual(result['sync']['cursor'],'s1')
        identity=result['sync']['objects']['master']['item_id'];item=self.service.get_item(identity)
        self.assertEqual(json.loads((self.path/item['original']['path']).read_bytes()),master)
        human=self.service.execute('felix',dict(operation_id='adopt-calendar',action='clarify',item_id=identity,expected_version=1,fields={'kind':'project','commitment':'committed','outcome':'Human','completion_criteria':'Human criterion'}))
        self.assertEqual(human['status'],'applied')
        self.transport.add(CALENDAR,{**params,'syncToken':'s1'},{'items':[{'id':'master','status':'cancelled'}],'nextPageToken':'d2'})
        self.transport.add(CALENDAR,{**params,'syncToken':'s1','pageToken':'d2'},{'items':[],'nextSyncToken':'s2'})
        result=await self.adapter.synchronize('calendar');self.assertEqual(result['sync']['cursor'],'s2')
        item=self.service.get_item(identity);self.assertEqual(item['commitment'],'committed');self.assertEqual(item['status'],'active')
        self.assertEqual(item['completion_criteria'],'Human criterion')
        self.assertFalse(result['coverage_contract']['recurrence_expanded'])

    async def test_calendar_410_and_network_failures_never_advance_cursor(self):
        params={'maxResults':2,'singleEvents':'false','showDeleted':'true'}
        self.transport.add(CALENDAR,params,{'items':[],'nextSyncToken':'s1'})
        await self.adapter.synchronize('calendar')
        self.transport.add(CALENDAR,{**params,'syncToken':'s1'},{},410)
        result=await self.adapter.synchronize('calendar');self.assertFalse(result['sync']['cursor_valid'])
        for status in (403,429):
            self.transport.add(CALENDAR,params,{},status)
            result=await self.adapter.synchronize('calendar');self.assertEqual(result['sync']['cursor'],'s1');self.assertEqual(result['sync']['coverage'],'degraded')
        self.transport.add(CALENDAR,params,OSError('private transport details must not persist'))
        result=await self.adapter.synchronize('calendar');self.assertEqual(result['adapter']['error'],'transport_unavailable')

    async def test_restart_after_projection_gap_uses_no_http_and_keeps_read_time(self):
        self.profile();self.transport.add(GMAIL+'/messages',{'maxResults':2,'includeSpamTrash':'true'},{'messages':[{'id':'m1'}]})
        self.transport.add(GMAIL+'/messages/m1',{'format':'raw'},raw_message())
        self.config['mail']['max_pages']=1;self.adapter=GoogleSources(self.sync,self.transport,self.config)
        with patch.object(self.service,'capture',return_value={'status':'uncertain'}):result=await self.adapter.synchronize('mail')
        stamp=result['sync']['coverage_completed_at'];count=len(self.transport.calls)
        self.restart();result=await self.adapter.synchronize('mail')
        self.assertEqual(len(self.transport.calls),count)
        self.assertEqual(result['sync']['coverage_completed_at'],stamp)
        self.assertEqual(result['sync']['projection'],'current')

    async def test_missing_page_cursor_size_and_attachment_content_limits(self):
        params={'maxResults':2,'singleEvents':'false','showDeleted':'true'}
        self.transport.add(CALENDAR,params,{'items':[]})
        result=await self.adapter.synchronize('calendar');self.assertIsNone(result['sync']['cursor'])
        self.assertEqual(result['sync']['coverage'],'degraded')
        cfg=copy.deepcopy(self.config);cfg['mail']['max_response_bytes']=128
        adapter=GoogleSources(self.sync,self.transport,cfg)
        self.profile();self.transport.add(GMAIL+'/messages',{'maxResults':2,'includeSpamTrash':'true'},b' '*129)
        result=await adapter.synchronize('mail');self.assertEqual(result['adapter']['error'],'response_too_large');self.assertIsNone(result['sync']['cursor'])

    async def test_history_second_page_failure_retains_previous_cursor(self):
        await self.seed_mail();self.profile('20')
        self.transport.add(GMAIL+'/history',{'maxResults':2,'startHistoryId':'10'}, {'history':[],'nextPageToken':'h2','historyId':'20'})
        self.transport.add(GMAIL+'/history',{'maxResults':2,'startHistoryId':'10','pageToken':'h2'}, {},429)
        result=await self.adapter.synchronize('mail')
        self.assertEqual(result['sync']['cursor'],'10')
        self.assertEqual(result['sync']['coverage'],'degraded')
        self.assertEqual(result['adapter']['error'],'http_429')

    async def test_message_404_is_not_inferred_as_permanent_deletion(self):
        first=await self.seed_mail();identity=first['sync']['objects']['m1']['item_id'];self.profile('20')
        self.transport.add(GMAIL+'/history',{'maxResults':2,'startHistoryId':'10'}, {'history':[{'id':'11','labelsRemoved':[{'message':{'id':'m1'}}]}],'historyId':'20'})
        self.transport.add(GMAIL+'/messages/m1',{'format':'raw'}, {},404)
        result=await self.adapter.synchronize('mail')
        self.assertEqual(result['sync']['objects']['m1']['availability'],'degraded')
        self.assertEqual(result['sync']['cursor'],'20')
        self.assertEqual(result['pending_reads']['m1']['reason'],'http_404')
        self.assertEqual(self.service.get_item(identity)['status'],'active')

    async def test_mime_attachment_preserved_without_executing_html(self):
        self.profile();self.transport.add(GMAIL+'/messages',{'maxResults':2,'includeSpamTrash':'true'},{'messages':[{'id':'m1'}]})
        message=raw_message();rfc=(b'MIME-Version: 1.0\r\nContent-Type: multipart/mixed; boundary=x\r\n\r\n'
            b'--x\r\nContent-Type: text/html\r\n\r\n<script>do_not_execute()</script>\r\n'
            b'--x\r\nContent-Type: application/octet-stream\r\nContent-Disposition: attachment; filename="example.bin"\r\nContent-Transfer-Encoding: base64\r\n\r\nYWJj\r\n--x--\r\n')
        message['raw']=base64.urlsafe_b64encode(rfc).decode().rstrip('=')
        self.transport.add(GMAIL+'/messages/m1',{'format':'raw'},message)
        result=await self.adapter.synchronize('mail');item=self.service.get_item(result['sync']['objects']['m1']['item_id'])
        self.assertIn('example.bin',item['text']);self.assertNotIn('<script>',item['text'])
        self.assertEqual(json.loads((self.path/item['original']['path']).read_bytes()),message)
        self.assertFalse(result['coverage_contract']['attachments_interpreted'])

    async def test_oversized_raw_attachment_does_not_claim_complete_coverage(self):
        self.profile();self.transport.add(GMAIL+'/messages',{'maxResults':2,'includeSpamTrash':'true'},{'messages':[{'id':'m1'}]})
        message=raw_message();message['raw']=base64.urlsafe_b64encode(b'a'*(4*1024*1024)).decode()
        self.transport.add(GMAIL+'/messages/m1',{'format':'raw'},message)
        result=await self.adapter.synchronize('mail')
        self.assertEqual(result['pending_reads']['m1']['reason'],'message_too_large')
        self.assertEqual(result['sync']['cursor'],'10');self.assertEqual(result['health'],'degraded')
        self.assertFalse(result['originals_complete'])

    async def test_restart_resumes_next_page_without_rereading_first_page(self):
        params={'maxResults':2,'singleEvents':'false','showDeleted':'true'}
        self.transport.add(CALENDAR,params,{'items':[{'id':'e1','etag':'v1','status':'confirmed'}],'nextPageToken':'p2'})
        self.transport.add(CALENDAR,{**params,'pageToken':'p2'},RuntimeError('synthetic process cut'))
        with self.assertRaises(RuntimeError):await self.adapter.synchronize('calendar')
        before=self.adapter.inspect('calendar')['sync'];cycle=before['active_cycle'];first_page=next(iter(before['cycles'][cycle]['pages']));stamp=before['cycles'][cycle]['pages'][first_page]['received_at']
        self.assertIsNone(before['cursor']);self.restart()
        self.transport.add(CALENDAR,{**params,'pageToken':'p2'},{'items':[],'nextSyncToken':'s1'})
        final=(await self.adapter.synchronize('calendar'))['sync']
        self.assertEqual(final['cursor'],'s1');self.assertEqual(final['cycles'][cycle]['pages'][first_page]['received_at'],stamp)
        self.assertEqual(sum(params==q for _,q in self.transport.calls),1)

    async def test_calendar_token_loop_and_scope_filters_are_rejected(self):
        params={'maxResults':2,'singleEvents':'false','showDeleted':'true'}
        self.transport.add(CALENDAR,params,{'items':[],'nextPageToken':'p2'})
        self.transport.add(CALENDAR,{**params,'pageToken':'p2'},{'items':[],'nextPageToken':'p2'})
        result=await self.adapter.synchronize('calendar')
        self.assertEqual(result['adapter']['error'],'page_token_cycle');self.assertIsNone(result['sync']['cursor'])
        for field,value in [('timeMin','2026-09-11T00:00:00Z'),('q','search'),('singleEvents',True),('calendar_id','primary')]:
            cfg=copy.deepcopy(self.config);cfg['calendar'][field]=value
            with self.assertRaises(SourceError):GoogleSources(self.sync,self.transport,cfg)

    async def test_page_budget_yields_and_restart_continues_same_baseline(self):
        self.config['mail']['max_pages']=1;self.adapter=GoogleSources(self.sync,self.transport,self.config)
        self.profile('10')
        self.transport.add(GMAIL+'/messages',{'maxResults':2,'includeSpamTrash':'true'},{'messages':[{'id':'m1'}],'nextPageToken':'p2'})
        self.transport.add(GMAIL+'/messages/m1',{'format':'raw'},raw_message())
        first=await self.adapter.synchronize('mail');cycle=first['sync']['active_cycle']
        self.assertTrue(first['adapter']['active']);self.assertEqual(first['adapter']['status'],'in_progress')
        self.assertIsNone(first['sync']['cursor']);self.restart()
        self.transport.add(GMAIL+'/messages',{'maxResults':2,'includeSpamTrash':'true','pageToken':'p2'},{'messages':[{'id':'m2'}]})
        self.transport.add(GMAIL+'/messages/m2',{'format':'raw'},raw_message('m2','12'))
        final=await self.adapter.synchronize('mail')
        self.assertEqual(final['sync']['cursor'],'10');self.assertEqual(final['adapter']['cycle_id'],cycle)
        self.assertEqual(sum(url==GMAIL+'/profile' for url,_ in self.transport.calls),1)
        self.assertEqual(sum(url==GMAIL+'/messages' and 'pageToken' not in q for url,q in self.transport.calls),1)
        self.assertEqual(len(final['sync']['objects']),2)

    async def test_html_only_visible_question_date_and_hidden_content(self):
        self.profile();self.transport.add(GMAIL+'/messages',{'maxResults':2,'includeSpamTrash':'true'},{'messages':[{'id':'m1'}]})
        message=raw_message();rfc=(b'Subject: Appointment\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
            b'<html><head><title>hidden title</title><style>secret-style</style></head><body>'
            b'<p>Can you confirm the appointment?</p><div>2026-09-14 at 10:00</div>'
            b'<script>secret-script()</script><p hidden>secret-hidden</p><p aria-hidden="true">secret-aria</p>'
            b'<p style="display: none">secret-display</p><p style="visibility:hidden">secret-visibility</p>'
            b'<a href="https://no-fetch.invalid">Visible link label</a><img src="https://no-fetch.invalid/image"></body></html>')
        message['raw']=base64.urlsafe_b64encode(rfc).decode();self.transport.add(GMAIL+'/messages/m1',{'format':'raw'},message)
        result=await self.adapter.synchronize('mail');item=self.service.get_item(result['sync']['objects']['m1']['item_id'])
        self.assertIn('Can you confirm the appointment?',item['text']);self.assertIn('2026-09-14 at 10:00',item['text'])
        self.assertIn('Visible link label',item['text']);self.assertNotIn('secret-',item['text']);self.assertNotIn('hidden title',item['text'])
        self.assertEqual(json.loads((self.path/item['original']['path']).read_bytes()),message)

    async def test_multipart_alternative_prefers_plain_without_duplicate_html(self):
        self.profile();self.transport.add(GMAIL+'/messages',{'maxResults':2,'includeSpamTrash':'true'},{'messages':[{'id':'m1'}]})
        message=raw_message();rfc=(b'MIME-Version: 1.0\r\nContent-Type: multipart/alternative; boundary=x\r\n\r\n'
            b'--x\r\nContent-Type: text/plain\r\n\r\nSingle visible question?\r\n'
            b'--x\r\nContent-Type: text/html\r\n\r\n<p>Single visible question?</p><p>HTML-only alternative</p>\r\n--x--\r\n')
        message['raw']=base64.urlsafe_b64encode(rfc).decode();self.transport.add(GMAIL+'/messages/m1',{'format':'raw'},message)
        result=await self.adapter.synchronize('mail');item=self.service.get_item(result['sync']['objects']['m1']['item_id'])
        self.assertEqual(item['text'].count('Single visible question?'),1);self.assertNotIn('HTML-only alternative',item['text'])

    async def test_unread_pending_does_not_block_new_mail_and_retries_after_restart(self):
        self.config['mail'].update(max_response_bytes=1200,pending_retry_limit=1)
        self.adapter=GoogleSources(self.sync,self.transport,self.config)
        self.profile('10');self.transport.add(GMAIL+'/messages',{'maxResults':2,'includeSpamTrash':'true'}, {'messages':[{'id':'m1'},{'id':'bad'}]})
        self.transport.add(GMAIL+'/messages/m1',{'format':'raw'},raw_message())
        self.transport.add(GMAIL+'/messages/bad',{'format':'raw'},b'x'*1201)
        first=await self.adapter.synchronize('mail');stamp=first['pending_reads']['bad']['observed_at']
        first_read=first['sync']['coverage_completed_at'];good=first['sync']['objects']['m1']['item_id']
        self.assertIsNotNone(good);self.assertIsNone(first['sync']['objects']['bad']['item_id'])
        self.assertEqual(first['sync']['cursor'],'10');self.assertEqual(first['health'],'degraded');self.assertFalse(first['originals_complete'])
        self.restart();self.profile('20')
        self.transport.add(GMAIL+'/messages/bad',{'format':'raw'},b'x'*1201)
        self.transport.add(GMAIL+'/history',{'maxResults':2,'startHistoryId':'10'}, {'history':[{'id':'18','messagesAdded':[{'message':{'id':'m2'}}]}],'historyId':'20'})
        self.transport.add(GMAIL+'/messages/m2',{'format':'raw'},raw_message('m2','18'))
        second=await self.adapter.synchronize('mail');self.assertIsNotNone(second['sync']['objects']['m2']['item_id'])
        self.assertEqual(second['sync']['cursor'],'20');self.assertEqual(second['pending_reads']['bad']['observed_at'],stamp)
        self.profile('30');self.transport.add(GMAIL+'/messages/bad',{'format':'raw'},raw_message('bad','25'))
        self.transport.add(GMAIL+'/history',{'maxResults':2,'startHistoryId':'20'},{'history':[],'historyId':'30'})
        third=await self.adapter.synchronize('mail');self.assertEqual(third['pending_reads'],{});self.assertEqual(third['health'],'complete')
        self.assertTrue(third['originals_complete']);self.assertIsNotNone(third['sync']['objects']['bad']['item_id'])
        self.assertEqual(self.service.store.db.execute('SELECT COUNT(*) FROM items').fetchone()[0],3)
        oldcycle=first['adapter']['cycle_id'];self.assertEqual(third['sync']['cycles'][oldcycle]['coverage_completed_at'],first_read)
        self.assertEqual(third['sync']['objects']['m1']['item_id'],good)

    async def test_explicit_delete_clears_pending_without_fabricating_capture(self):
        self.config['mail']['max_response_bytes']=1200;self.adapter=GoogleSources(self.sync,self.transport,self.config)
        self.profile();self.transport.add(GMAIL+'/messages',{'maxResults':2,'includeSpamTrash':'true'},{'messages':[{'id':'bad'}]})
        self.transport.add(GMAIL+'/messages/bad',{'format':'raw'},b'x'*1201)
        await self.adapter.synchronize('mail')
        self.profile('20');self.transport.add(GMAIL+'/messages/bad',{'format':'raw'},{},404)
        self.transport.add(GMAIL+'/history',{'maxResults':2,'startHistoryId':'10'},{'history':[{'id':'18','messagesDeleted':[{'message':{'id':'bad'}}]}],'historyId':'20'})
        result=await self.adapter.synchronize('mail');self.assertEqual(result['pending_reads'],{})
        self.assertEqual(result['sync']['objects']['bad']['availability'],'deleted')
        self.assertEqual(self.service.store.db.execute('SELECT COUNT(*) FROM items').fetchone()[0],0)

    async def test_pending_resolution_survives_cut_after_page_commit(self):
        self.config['mail']['max_response_bytes']=1200;self.adapter=GoogleSources(self.sync,self.transport,self.config)
        self.profile();self.transport.add(GMAIL+'/messages',{'maxResults':2,'includeSpamTrash':'true'},{'messages':[{'id':'bad'}]})
        self.transport.add(GMAIL+'/messages/bad',{'format':'raw'},b'x'*1201)
        await self.adapter.synchronize('mail')
        self.profile('20');self.transport.add(GMAIL+'/messages/bad',{'format':'raw'},raw_message('bad','18'))
        self.transport.add(GMAIL+'/history',{'maxResults':2,'startHistoryId':'10'},{'history':[],'historyId':'20'})
        apply=self.sync.apply_page
        def cut(*args,**kwargs):
            result=apply(*args,**kwargs)
            self.assertEqual(result['cursor'],'20')
            raise RuntimeError('cut after durable page')
        with patch.object(self.sync,'apply_page',side_effect=cut),self.assertRaises(RuntimeError):await self.adapter.synchronize('mail')
        count=len(self.transport.calls);self.restart()
        final=await self.adapter.synchronize('mail')
        self.assertEqual(final['pending_reads'],{});self.assertEqual(final['sync']['cursor'],'20')
        self.assertEqual(len(self.transport.calls),count)
        self.assertEqual(self.service.store.db.execute('SELECT COUNT(*) FROM items').fetchone()[0],1)

    async def test_message_without_label_ids_is_valid_whole_mailbox_source(self):
        self.profile();self.transport.add(GMAIL+'/messages',{'maxResults':2,'includeSpamTrash':'true'},{'messages':[{'id':'m1'}]})
        message=raw_message();message.pop('labelIds')
        self.transport.add(GMAIL+'/messages/m1',{'format':'raw'},message)
        result=await self.adapter.synchronize('mail')
        self.assertEqual(result['sync']['cursor'],'10');self.assertEqual(result['pending_reads'],{})
        item=self.service.get_item(result['sync']['objects']['m1']['item_id'])
        self.assertNotIn('labelIds',json.loads((self.path/item['original']['path']).read_bytes()))
        self.assertIsNone(json.loads(item['text'].split('\n\n',1)[0])['labelIds'])

    async def test_repeated_same_unread_failure_only_updates_operational_attempts(self):
        first=await self.seed_mail();identity=first['sync']['objects']['m1']['item_id']
        item=self.service.get_item(identity)
        self.service.execute('felix',dict(operation_id='human-note-before-degradation',action='edit',item_id=identity,expected_version=item['version'],fields={'text':'Human choice','notes':'Human note'}))
        self.profile('20');self.transport.add(GMAIL+'/history',{'maxResults':2,'startHistoryId':'10'}, {'history':[{'id':'18','labelsRemoved':[{'message':{'id':'m1'}}]}],'historyId':'20'})
        self.transport.add(GMAIL+'/messages/m1',{'format':'raw'},{},404)
        degraded=await self.adapter.synchronize('mail')
        item_before,versions_before=self.service._item(identity)
        events_before=self.service.store.db.execute('SELECT COUNT(*) FROM events').fetchone()[0]
        self.profile('30');self.transport.add(GMAIL+'/messages/m1',{'format':'raw'},{},404)
        self.transport.add(GMAIL+'/history',{'maxResults':2,'startHistoryId':'20'},{'history':[],'historyId':'30'})
        retry=await self.adapter.synchronize('mail')
        item_after,versions_after=self.service._item(identity)
        self.assertEqual(item_before,item_after);self.assertEqual(versions_before,versions_after)
        self.assertEqual(self.service.store.db.execute('SELECT COUNT(*) FROM events').fetchone()[0],events_before)
        self.assertEqual(retry['pending_reads']['m1']['attempts'],degraded['pending_reads']['m1']['attempts']+1)
        self.assertEqual(retry['pending_reads']['m1']['observed_at'],degraded['pending_reads']['m1']['observed_at'])
        self.assertGreaterEqual(retry['pending_reads']['m1']['last_attempt_at'],degraded['pending_reads']['m1']['last_attempt_at'])
