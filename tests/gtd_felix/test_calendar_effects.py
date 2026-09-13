"""Calendar semantics over local aiohttp, real GoogleTransport and durable Effects."""
import copy
import asyncio
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sys
import tempfile
import unittest
from urllib.parse import urlsplit

import aiohttp
from aiohttp import web
from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from gtd_felix.calendar_effects import CalendarAgenda, CalendarEffects, CalendarError
from gtd_felix.effects import ExternalEffects
from gtd_felix.google_transport import GoogleTransport
from gtd_felix.service import GTDService

ACCOUNT = 'calendar-user@example.invalid'
CALENDAR = 'calendar-id@example.invalid'


class LocalSession:
    def __init__(self, base, **options):
        self.inner = aiohttp.ClientSession(**options)
        self.base = base
    def request(self, method, url, **kwargs):
        return self.inner.request(method, self.base + urlsplit(url).path, **kwargs)
    async def close(self):
        await self.inner.close()


class CalendarTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.service = GTDService(self.root / 'data')
        self.effects = ExternalEffects(self.service)
        self.item = self.service.capture('felix', 'capture', 'Prepare calendar action')['item']
        self.events, self.pages, self.writes = {}, [], []
        self.role = 'owner'
        self.conflict = self.drop_ack = False
        self.normalize = None
        self.before_write = None
        async def handler(request):
            if request.path == '/v1/userinfo':
                return web.json_response({'email': ACCOUNT, 'email_verified': True})
            if '/calendarList/' in request.path:
                return web.json_response({'id': CALENDAR, 'accessRole': self.role, 'timeZone': 'Europe/Berlin'})
            event_id = request.path.rsplit('/', 1)[-1]
            if request.method == 'GET':
                if event_id == 'events':
                    page = int(request.query.get('pageToken', '0'))
                    document = self.pages[page]
                    return web.json_response(document)
                return web.json_response(self.events.get(event_id, {}), status=200 if event_id in self.events else 404)
            payload = await request.json() if request.can_read_body else None
            self.writes.append({'method': request.method, 'event_id': event_id, 'body': payload,
                                'etag': request.headers.get('If-Match'), 'sendUpdates': request.query.get('sendUpdates')})
            if self.conflict:
                self.events[event_id]['summary'] = 'Human concurrent correction'
                self.events[event_id]['etag'] = '"human"'
                return web.json_response({'error': 'private provider detail'}, status=412)
            if request.method == 'POST':
                event_id = payload['id']
                self.events[event_id] = {**copy.deepcopy(payload), 'etag': '"created"', 'organizer': {'self': True}, 'status': 'confirmed'}
            elif request.method == 'PATCH':
                if payload.get('attendeesOmitted'):
                    for attendee in self.events[event_id]['attendees']:
                        if attendee.get('email') == payload['attendees'][0]['email']:
                            attendee['responseStatus'] = 'declined'
                    payload = {k: v for k, v in payload.items() if k not in {'attendees', 'attendeesOmitted'}}
                self.events[event_id].update(copy.deepcopy(payload))
                self.events[event_id]['etag'] = '"updated"'
            else:
                self.events.pop(event_id, None)
            if self.normalize and event_id in self.events:
                self.normalize(self.events[event_id])
            if self.drop_ack:
                request.transport.close()
                return web.Response(status=204)
            if request.method == 'DELETE':
                return web.Response(status=204)
            return web.json_response(self.events[event_id], status=201 if request.method == 'POST' else 200)
        app = web.Application()
        app.router.add_route('*', '/{tail:.*}', handler)
        self.runner = web.AppRunner(app, access_log=None)
        await self.runner.setup()
        site = web.TCPSite(self.runner, '127.0.0.1', 0)
        await site.start()
        base = 'http://127.0.0.1:' + str(site._server.sockets[0].getsockname()[1])
        credentials = self.root / 'token.json'
        credentials.write_text(json.dumps({'token': 'synthetic', 'expiry': '2099-01-01T00:00:00Z',
            'scopes': ['openid', 'email', 'https://www.googleapis.com/auth/calendar.events']}))
        credentials.chmod(0o600)
        self.transport = GoogleTransport({'account': ACCOUNT, 'token_file': str(credentials), 'gmail': False,
            'calendar_ids': [CALENDAR], 'identity_method': 'oidc'}, session_factory=lambda **kw: LocalSession(base, **kw))
        await self.transport.connect()
        self.driver = CalendarEffects(self.effects, self.transport)

    async def asyncTearDown(self):
        await self.transport.close()
        await self.runner.cleanup()
        self.service.close()
        self.temp.cleanup()

    def event(self, event_id='event1', **changes):
        return {**{'id': event_id, 'etag': '"before"', 'summary': 'Original', 'status': 'confirmed',
            'organizer': {'self': True}, 'start': {'dateTime': '2026-03-29T01:30:00+01:00'},
            'end': {'dateTime': '2026-03-29T03:30:00+02:00'}}, **changes}

    def propose(self, action='update', body=None, identity='event1', calendar=CALENDAR, account=ACCOUNT):
        p = {'provider': 'calendar', 'account': account, 'action': action, 'item_id': self.item['id'],
             'target': {'id': identity}, 'payload': {'calendar_id': calendar, 'event': body if body is not None else {'summary': 'Approved'},
             'send_updates': 'none'}, 'expires_at': (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat()}
        if action != 'insert':
            p['expected_remote_version'] = '"before"'
        number = str(len(self.effects.list('felix')))
        result = self.effects.propose('gtd-felix', 'proposal-' + number, p)
        self.assertEqual(result['status'], 'proposed', result)
        effect = result['effect']
        self.assertEqual(self.effects.authorize('felix', 'authorize-' + number, effect['id'], effect['proposal_hash'])['status'], 'authorized')
        return effect

    async def test_window_occurrences_dst_all_day_exceptions_and_only_busy_overlap(self):
        busy = self.event()
        moved = self.event('moved', recurringEventId='master', originalStartTime={'dateTime': '2026-03-29T01:00:00+01:00'},
            start={'dateTime': '2026-03-29T03:00:00+02:00'}, end={'dateTime': '2026-03-29T04:00:00+02:00'})
        all_day = self.event('all-day', start={'date': '2026-03-29'}, end={'date': '2026-03-30'})
        cancelled = {'id': 'cancelled', 'status': 'cancelled', 'recurringEventId': 'master', 'originalStartTime': {'date': '2026-03-28'}}
        transparent = self.event('transparent', transparency='transparent')
        declined = self.event('declined', attendees=[{'email': ACCOUNT, 'self': True, 'responseStatus': 'declined'}])
        self.pages = [{'items': [busy, moved, cancelled], 'timeZone': 'Europe/Berlin', 'nextPageToken': '1'},
                      {'items': [all_day, transparent, declined], 'timeZone': 'Europe/Berlin'}]
        before = self.service.query()
        result = await CalendarAgenda(self.transport, ACCOUNT, [CALENDAR]).read('2026-03-28T00:00:00+01:00', '2026-03-31T00:00:00+02:00', 'Europe/Berlin')
        self.assertEqual(result['status'], 'complete')
        self.assertEqual(result['calendars'][0]['pages'], 2)
        occurrences = {o['id']: o for o in result['calendars'][0]['occurrences']}
        self.assertEqual(occurrences['moved']['original'], moved)
        self.assertEqual(occurrences['all-day']['interval'], {'start': '2026-03-28T23:00:00+00:00', 'end': '2026-03-29T22:00:00+00:00'})
        self.assertTrue(occurrences['all-day']['end_exclusive'])
        self.assertEqual(len(result['overlaps']), 3)
        self.assertFalse(occurrences['cancelled']['busy'])
        self.assertEqual(self.service.query(), before)
        self.assertEqual(self.writes, [])

    async def test_pagination_limits_and_bad_windows_do_not_claim_coverage(self):
        self.pages = [{'items': [self.event()], 'nextPageToken': '1'}, {'items': [], 'nextPageToken': '1'}]
        agenda = CalendarAgenda(self.transport, ACCOUNT, [CALENDAR])
        result = await agenda.read('2026-03-28T00:00:00Z', '2026-03-31T00:00:00Z', 'Europe/Berlin', max_pages=1)
        self.assertEqual(result['status'], 'incomplete')
        self.assertEqual(result['calendars'][0]['next_page_token'], '1')
        result = await agenda.read('2026-03-28T00:00:00Z', '2026-03-31T00:00:00Z', 'Europe/Berlin')
        self.assertEqual(result['calendars'][0]['error'], 'pagination_not_progressing')
        for start, end, zone in [('2026-01-01', '2026-01-02T00:00:00Z', 'UTC'),
                ('2026-01-01T00:00:00Z', '2028-01-01T00:00:00Z', 'UTC'),
                ('2026-01-01T00:00:00Z', '2026-01-02T00:00:00Z', 'not-a-zone')]:
            with self.assertRaises(CalendarError):
                await agenda.read(start, end, zone)

    async def test_patch_if_match_412_preserves_human_change_without_retry(self):
        self.events['event1'] = self.event()
        effect = self.propose()
        self.conflict = True
        result = await self.driver.dispatch(effect['id'])
        self.assertEqual(result['status'], 'conflict', result)
        self.assertEqual(self.events['event1']['summary'], 'Human concurrent correction')
        self.assertEqual(self.writes[0]['etag'], '"before"')
        self.assertEqual(self.writes[0]['method'], 'PATCH')
        self.assertNotIn('private provider detail', json.dumps(result))
        self.assertEqual((await self.driver.dispatch(effect['id']))['status'], 'conflict')
        self.assertEqual(len(self.writes), 1)
        self.assertEqual(self.effects.pending(), [])

    async def test_successful_patch_keeps_unspecified_fields_and_confirms_readback(self):
        self.events['event1'] = self.event(location='Unchanged room')
        effect = self.propose()
        result = await self.driver.dispatch(effect['id'])
        self.assertEqual(result['status'], 'confirmed', result)
        self.assertFalse(result['notifications_verified'])
        self.assertEqual(self.events['event1']['location'], 'Unchanged room')
        self.assertEqual(self.writes[0]['body'], {'summary': 'Approved'})

    async def test_decline_only_self_cancel_and_delete_copy_have_distinct_preconditions(self):
        self.events['event1'] = self.event(organizer={'self': False}, attendees=[
            {'email': ACCOUNT, 'self': True, 'responseStatus': 'accepted'},
            {'email': 'other@example.invalid', 'responseStatus': 'accepted'}])
        body = {'attendeesOmitted': True, 'attendees': [{'email': ACCOUNT, 'responseStatus': 'declined'}]}
        effect = self.propose('decline', body)
        self.assertEqual((await self.driver.dispatch(effect['id']))['status'], 'confirmed')
        self.assertEqual(self.events['event1']['attendees'][1]['responseStatus'], 'accepted')
        self.assertEqual(self.writes[0]['method'], 'PATCH')
        self.events['event1']['etag'] = '"before"'
        forbidden = self.propose('cancel_event', {})
        self.assertEqual((await self.driver.dispatch(forbidden['id']))['reason'], 'organizer_required')
        copied = self.propose('delete_copy', {})
        self.assertEqual((await self.driver.dispatch(copied['id']))['status'], 'confirmed')
        self.assertEqual(self.writes[-1]['method'], 'DELETE')
        self.events['event1'] = self.event()
        forbidden = self.propose('delete_copy', {})
        self.assertEqual((await self.driver.dispatch(forbidden['id']))['reason'], 'nonorganizer_copy_required')
        cancelled = self.propose('cancel_event', {})
        self.assertEqual((await self.driver.dispatch(cancelled['id']))['status'], 'confirmed')

    async def test_wrong_role_calendar_account_and_attendee_are_rejected_before_write(self):
        self.events['event1'] = self.event()
        self.role = 'reader'
        self.assertEqual((await self.driver.dispatch(self.propose()['id']))['reason'], 'calendar_write_role_required')
        self.role = 'owner'
        self.assertEqual((await self.driver.dispatch(self.propose(calendar='foreign@example.invalid')['id']))['status'], 'rejected')
        self.assertEqual((await self.driver.dispatch(self.propose(account='foreign@example.invalid')['id']))['status'], 'rejected')
        self.events['event1'] = self.event(organizer={'self': False}, attendees=[{'email': ACCOUNT, 'self': True}])
        bad = self.propose('decline', {'attendeesOmitted': True, 'attendees': [{'email': 'other@example.invalid', 'responseStatus': 'declined'}]})
        self.assertEqual((await self.driver.dispatch(bad['id']))['reason'], 'self_attendee_required')
        self.assertEqual(self.writes, [])

    async def test_insert_lost_ack_exact_client_id_reconciles_without_post_retry(self):
        body = {'id': 'client012345', 'summary': 'Approved', 'start': {'dateTime': '2026-04-01T10:00:00+02:00'},
                'end': {'dateTime': '2026-04-01T11:00:00+02:00'}}
        effect = self.propose('insert', body, identity='client012345')
        self.drop_ack = True
        self.assertEqual((await self.driver.dispatch(effect['id']))['status'], 'uncertain')
        self.driver = CalendarEffects(ExternalEffects(self.service), self.transport)
        self.assertEqual((await self.driver.reconcile(effect['id']))['status'], 'confirmed')
        self.assertEqual(len(self.writes), 1)

    async def test_update_lost_ack_requires_approved_new_marker_and_matching_content(self):
        self.events['event1'] = self.event(extendedProperties={'private': {'keep': 'untouched'}})
        effect = self.propose(body={'summary': 'Approved', 'extendedProperties': {'private': {'keep': 'untouched', 'gtd_effect_operation': 'operation-1'}}})
        self.drop_ack = True
        self.assertEqual((await self.driver.dispatch(effect['id']))['status'], 'uncertain')
        self.events['event1']['summary'] = 'Changed later'
        self.assertEqual((await self.driver.reconcile(effect['id']))['status'], 'uncertain')
        self.events['event1']['summary'] = 'Approved'
        self.assertEqual((await self.driver.reconcile(effect['id']))['status'], 'confirmed')
        self.assertEqual(len(self.writes), 1)

    async def test_delete_lost_ack_absence_remains_uncertain(self):
        self.events['event1'] = self.event()
        effect = self.propose('cancel_event', {})
        self.drop_ack = True
        self.assertEqual((await self.driver.dispatch(effect['id']))['status'], 'uncertain')
        self.assertEqual((await self.driver.reconcile(effect['id']))['status'], 'uncertain')
        self.assertEqual(len(self.writes), 1)
        self.assertEqual(len(self.effects.pending()), 1)

    async def test_update_without_marker_and_property_loss_do_not_claim_success(self):
        self.events['event1'] = self.event(extendedProperties={'private': {'keep': 'original'}})
        unsafe = self.propose(body={'extendedProperties': {'private': {'gtd_effect_operation': 'op'}}})
        self.assertEqual((await self.driver.dispatch(unsafe['id']))['reason'], 'existing_properties_must_be_preserved')
        self.assertEqual(self.writes, [])
        effect = self.propose()
        self.drop_ack = True
        self.assertEqual((await self.driver.dispatch(effect['id']))['status'], 'uncertain')
        self.assertEqual((await self.driver.reconcile(effect['id']))['status'], 'uncertain')
        self.assertEqual(len(self.writes), 1)

    async def test_persisted_412_recovers_after_ledger_response_boundary_crash(self):
        self.events['event1'] = self.event()
        effect = self.propose()
        self.conflict = True
        observe = self.effects.observe
        def interrupted(identity, observation):
            if observation['status'] == 'conflict':
                raise RuntimeError('synthetic crash before ledger observation')
            return observe(identity, observation)
        self.effects.observe = interrupted
        with self.assertRaises(RuntimeError):
            await self.driver.dispatch(effect['id'])
        self.service.close()
        self.service = GTDService(self.root / 'data')
        self.effects = ExternalEffects(self.service)
        self.driver = CalendarEffects(self.effects, self.transport)
        self.assertEqual((await self.driver.reconcile(effect['id']))['status'], 'conflict')
        self.assertEqual(self.effects.pending(), [])
        self.assertEqual(len(self.writes), 1)

    async def test_malformed_event_is_preserved_with_incomplete_coverage(self):
        original = {'id': 'unknown-time', 'summary': 'No invented interval'}
        self.pages = [{'items': [original]}]
        result = await CalendarAgenda(self.transport, ACCOUNT, [CALENDAR]).read(
            '2026-03-28T00:00:00Z', '2026-03-31T00:00:00Z', 'Europe/Berlin')
        self.assertEqual(result['status'], 'incomplete')
        self.assertEqual(result['calendars'][0]['events'], [original])
        self.assertEqual(result['overlaps'], [])

    async def test_revocation_or_source_date_change_during_preflight_prevents_write(self):
        self.events['event1'] = self.event()
        for reason in ('revoke', 'source-date'):
            effect = self.propose()
            original = self.transport._calendar_effect_write
            async def intercepted(*args, **kwargs):
                if reason == 'revoke':
                    self.effects.revoke('felix', 'revoke-before-write', effect_id=effect['id'])
                else:
                    item = self.service.get_item(self.item['id'])
                    self.service.execute('felix', {'operation_id': 'source-date', 'action': 'edit', 'item_id': item['id'],
                        'expected_version': item['version'], 'fields': {'due_at': '2027-01-01T10:00:00Z'}})
                return await original(*args, **kwargs)
            self.transport._calendar_effect_write = intercepted
            try:
                self.assertEqual((await self.driver.dispatch(effect['id']))['status'], 'rejected')
            finally:
                self.transport._calendar_effect_write = original
        self.assertEqual(self.writes, [])



    async def test_insert_readback_normalized_boundary_instants(self):
        body={'id':'client012345','summary':'Approved',
            'start':{'dateTime':'2026-04-01T10:00:00Z','timeZone':'UTC'},
            'end':{'dateTime':'2026-04-01T11:00:00+00:00','timeZone':'UTC'}}
        def normalize(event):
            event['start']['dateTime']='2026-04-01T10:00+00:00'
            event['end']['dateTime']='2026-04-01T11:00:00Z'
        self.normalize=normalize
        effect=self.propose('insert',body,identity=body['id'])
        self.assertEqual((await self.driver.dispatch(effect['id']))['status'],'confirmed')

    async def test_insert_identity_gate_concurrent_lost_ack_and_restart_history(self):
        body={'id':'client012345','summary':'Approved',
            'start':{'dateTime':'2026-04-01T10:00:00Z'},'end':{'dateTime':'2026-04-01T11:00:00Z'}}
        first=self.propose('insert',body,identity=body['id']);second=self.propose('insert',body,identity=body['id'])
        original=self.transport._calendar_effect_write
        barrier=asyncio.Event();arrived=0
        async def synchronized(*args,**kwargs):
            nonlocal arrived
            arrived+=1
            if arrived==2:barrier.set()
            await barrier.wait()
            return await original(*args,**kwargs)
        self.transport._calendar_effect_write=synchronized;self.drop_ack=True
        results=await asyncio.gather(self.driver.dispatch(first['id']),CalendarEffects(self.effects,self.transport).dispatch(second['id']))
        self.assertEqual(len(self.writes),1,results)
        rejected=next(r for r in results if r['status']=='rejected')
        self.assertEqual(rejected['reason'],'insert_identity_already_dispatched')
        self.transport._calendar_effect_write=original
        sent=next(e for e in self.effects.list('felix') if 'dispatch' in e)
        self.assertEqual((await self.driver.reconcile(sent['id']))['status'],'confirmed')
        self.events.clear() # Even remote removal cannot renew this local identity.
        self.service.close();self.service=GTDService(self.root/'data');self.effects=ExternalEffects(self.service)
        self.driver=CalendarEffects(self.effects,self.transport)
        third=self.propose('insert',body,identity=body['id'])
        self.assertEqual((await self.driver.dispatch(third['id']))['reason'],'insert_identity_already_dispatched')
        self.assertEqual(len(self.writes),1)

    async def test_readback_distinct_invalid_or_zone_changed_boundary_stays_uncertain(self):
        for changed in ({'dateTime':'2026-04-01T10:01:00Z','timeZone':'UTC'},
                        {'dateTime':'2026-04-01 10:00:00Z','timeZone':'UTC'},
                        {'dateTime':'2026-04-01T10:00:00','timeZone':'UTC'},
                        {'dateTime':'2026-04-01T11:00:00+00:60','timeZone':'UTC'},
                        {'dateTime':'2026-04-01T10:00:00Z','timeZone':'Europe/London'},
                        {'date':'2026-04-01'}):
            with self.subTest(changed=changed):
                identity='client'+str(len(self.writes))
                body={'id':identity,'summary':'Approved','start':{'dateTime':'2026-04-01T10:00:00Z','timeZone':'UTC'},
                      'end':{'dateTime':'2026-04-01T11:00:00Z','timeZone':'UTC'}}
                self.normalize=lambda event: event.update(start=copy.deepcopy(changed))
                effect=self.propose('insert',body,identity=identity)
                self.assertEqual((await self.driver.dispatch(effect['id']))['status'],'uncertain')
        self.assertFalse(CalendarEffects._matches({'start':{'date':'2026-04-02'}},{'start':{'date':'2026-04-01'}}))
        self.assertFalse(CalendarEffects._matches({'custom':{'dateTime':'2026-04-01T10:00:00Z'}},
            {'custom':{'dateTime':'2026-04-01T10:00:00+00:00'}}))


if __name__ == '__main__':
    unittest.main()
