"""Windowed Calendar reads and exact approved effects; no scheduler or Google accounts.

Provider semantics: https://developers.google.com/workspace/calendar/api/v3/reference/events
https://developers.google.com/workspace/calendar/api/guides/version-resources
Window coverage is not the masters/exceptions synchronization of SourceSync.
"""
import asyncio
import copy
from datetime import date, datetime, time, timezone
import hashlib
import json
import re
from zoneinfo import ZoneInfo

from .google_transport import TransportError


class CalendarError(ValueError):
    pass


def _require(condition, code):
    if not condition:
        raise CalendarError(code)


def _instant(value):
    _require(isinstance(value, str), 'offset_datetime_required')
    try:
        stamp = datetime.fromisoformat(value)
    except ValueError as exc:
        raise CalendarError('offset_datetime_required') from exc
    _require(stamp.tzinfo is not None, 'offset_datetime_required')
    return stamp.astimezone(timezone.utc)


def _zone(value):
    try:
        _require(isinstance(value, str) and bool(value), 'iana_timezone_required')
        return ZoneInfo(value)
    except (KeyError, ValueError) as exc:
        raise CalendarError('iana_timezone_required') from exc


def _hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()).hexdigest()


def _document(response):
    _require(response.get('status') == 200, 'calendar_read_failed')
    body = response.get('body')
    _require(isinstance(body, bytes) and len(body) <= 8 * 1024 * 1024, 'calendar_response_invalid')
    try:
        value = json.loads(body)
    except (ValueError, UnicodeError) as exc:
        raise CalendarError('calendar_response_invalid') from exc
    _require(isinstance(value, dict), 'calendar_response_invalid')
    return value


def _boundary(value, zone):
    _require(isinstance(value, dict), 'event_time_missing')
    if 'date' in value:
        _require('dateTime' not in value, 'event_time_invalid')
        try:
            local = datetime.combine(date.fromisoformat(value['date']), time(), zone)
        except (ValueError, TypeError) as exc:
            raise CalendarError('event_time_invalid') from exc
        _require(local.astimezone(timezone.utc).astimezone(zone).replace(tzinfo=None) == local.replace(tzinfo=None), 'nonexistent_calendar_date')
        return local.astimezone(timezone.utc), True
    text = value.get('dateTime')
    _require(isinstance(text, str), 'event_time_missing')
    try:
        stamp = datetime.fromisoformat(text)
    except ValueError as exc:
        raise CalendarError('event_time_invalid') from exc
    if stamp.tzinfo is None:
        tz = _zone(value.get('timeZone'))
        stamp = stamp.replace(tzinfo=tz)
        _require(stamp.utcoffset() == stamp.replace(fold=1).utcoffset()
                 and stamp.astimezone(timezone.utc).astimezone(tz).replace(tzinfo=None) == datetime.fromisoformat(text),
                 'ambiguous_event_time')
    return stamp.astimezone(timezone.utc), False


def _occurrence(event, calendar_id, zone):
    _require(isinstance(event, dict) and isinstance(event.get('id'), str) and event['id'], 'event_identity_missing')
    _require(isinstance(event.get('attendees', []), list) and all(isinstance(a, dict) for a in event.get('attendees', []))
             and isinstance(event.get('organizer', {}), dict), 'event_participation_invalid')
    own = [a for a in event.get('attendees', []) if a.get('self') is True]
    _require(len(own) <= 1, 'ambiguous_self_participation')
    cancelled = event.get('status') == 'cancelled'
    declined = bool(own and own[0].get('responseStatus') == 'declined')
    result = {'calendar_id': calendar_id, 'id': event['id'], 'etag': event.get('etag'),
              'original': copy.deepcopy(event), 'recurring_event_id': event.get('recurringEventId'),
              'original_start_time': copy.deepcopy(event.get('originalStartTime')),
              'organizer': copy.deepcopy(event.get('organizer')), 'self_participation': copy.deepcopy(own[0]) if own else None,
              'cancelled': cancelled, 'declined': declined, 'transparency': event.get('transparency', 'opaque'),
              'busy': False, 'interval': None}
    if cancelled and ('start' not in event or 'end' not in event):
        return result  # Cancelled exceptions may contain only identity/originalStartTime.
    start, all_day = _boundary(event.get('start'), zone)
    end, end_all_day = _boundary(event.get('end'), zone)
    _require(end > start and all_day == end_all_day, 'event_interval_invalid')
    result.update(all_day=all_day, end_exclusive=True,
                  interval={'start': start.isoformat(), 'end': end.isoformat()},
                  busy=not cancelled and not declined and event.get('transparency', 'opaque') == 'opaque')
    result['kind'] = 'own_block' if event.get('organizer', {}).get('self') is True and not event.get('attendees') else 'event'
    return result


class CalendarAgenda:
    def __init__(self, transport, account, calendar_ids):
        _require(isinstance(account, str) and bool(account), 'account_required')
        _require(isinstance(calendar_ids, list) and calendar_ids and len(calendar_ids) <= 100
                 and len(set(calendar_ids)) == len(calendar_ids)
                 and all(isinstance(c, str) and c and c != 'primary' for c in calendar_ids), 'concrete_calendars_required')
        self.transport, self.account, self.calendars = transport, account, list(calendar_ids)

    async def read(self, start, end, timezone_name, max_pages=100):
        """Expand occurrences via events.list; preserve originals and incomplete coverage."""
        lower, upper, zone = _instant(start), _instant(end), _zone(timezone_name)
        _require(0 < (upper - lower).total_seconds() <= 366 * 86400, 'finite_window_required')
        _require(type(max_pages) is int and 1 <= max_pages <= 1000, 'page_limit_invalid')
        result = {'status': 'complete', 'coverage_kind': 'expanded_window',
                  'window': {'start': start, 'end': end, 'timezone': timezone_name}, 'calendars': [], 'overlaps': []}
        await self.transport._effect_prepare(self.account)
        _require(self.transport.authenticated_account == self.account, 'account_mismatch')
        occupied, total_events = [], 0
        for calendar_id in self.calendars:
            entry = {'calendar_id': calendar_id, 'status': 'incomplete', 'pages': 0, 'events': [], 'occurrences': []}
            result['calendars'].append(entry)
            cursor, seen_tokens, seen_events = None, set(), {}
            try:
                for _ in range(max_pages):
                    params = {'singleEvents': 'true', 'showDeleted': 'true', 'timeMin': start, 'timeMax': end,
                              'timeZone': timezone_name, 'maxResults': 2500}
                    if cursor:
                        params['pageToken'] = cursor
                    response = await self.transport._calendar_effect_get(calendar_id, params=params)
                    document = _document(response)
                    entry['pages'] += 1
                    values = document.get('items', [])
                    _require(isinstance(values, list) and total_events + len(values) <= 10000, 'window_event_limit')
                    for event in values:
                        entry['events'].append(copy.deepcopy(event))
                        total_events += 1
                        occurrence = _occurrence(event, calendar_id, _zone(document.get('timeZone', timezone_name)))
                        old = seen_events.get(occurrence['id'])
                        _require(old is None or old == event, 'event_changed_during_pagination')
                        if old is not None:
                            entry['events'].pop()
                            continue
                        seen_events[occurrence['id']] = event
                        entry['occurrences'].append(occurrence)
                        if occurrence['busy']:
                            occupied.append(occurrence)
                    cursor = document.get('nextPageToken')
                    if not cursor:
                        entry['status'] = 'complete'
                        break
                    _require(isinstance(cursor, str) and cursor not in seen_tokens and len(cursor) <= 4096, 'pagination_not_progressing')
                    seen_tokens.add(cursor)
                    entry['next_page_token'] = cursor
                if entry['status'] == 'complete':
                    entry.pop('next_page_token', None)
                else:
                    entry['error'] = 'page_limit_reached'
            except (CalendarError, TransportError, TypeError, KeyError) as error:
                entry['error'] = str(error) if isinstance(error, CalendarError) else 'calendar_transport_or_shape_error'
            if entry['status'] != 'complete':
                result['status'] = 'incomplete'
        occupied.sort(key=lambda o: o['interval']['start'])
        for index, first in enumerate(occupied):
            a, b = _instant(first['interval']['start']), _instant(first['interval']['end'])
            for second in occupied[index + 1:]:
                c, d = _instant(second['interval']['start']), _instant(second['interval']['end'])
                if c >= b:
                    break
                # Two calendar copies of the same occurrence are not two obligations.
                uid = first['original'].get('iCalUID')
                if uid and uid == second['original'].get('iCalUID') and a == c and b == d:
                    continue
                if max(a, c, lower) < min(b, d, upper):
                    if len(result['overlaps']) >= 10000:
                        result['status'], result['overlap_status'] = 'incomplete', 'overlap_limit_reached'
                        return result
                    result['overlaps'].append({'first': [first['calendar_id'], first['id']],
                        'second': [second['calendar_id'], second['id']],
                        'start': max(a, c, lower).isoformat(), 'end': min(b, d, upper).isoformat()})
        return result


class CalendarEffects:
    PATCH_FIELDS = {'summary', 'description', 'location', 'start', 'end', 'transparency',
                    'visibility', 'recurrence', 'extendedProperties'}
    MARKER = 'gtd_effect_operation'

    def __init__(self, effects, transport):
        self.effects, self.service, self.transport = effects, effects.service, transport
        self._locks = {}

    def _effect(self, identity):
        effect = self.effects.get(self.service.owner_actor, identity)
        _require(effect is not None and effect['proposal']['provider'] == 'calendar', 'calendar_effect_required')
        return effect

    def _payload(self, effect):
        p = effect['proposal']
        payload = p['payload']
        _require(set(payload) == {'calendar_id', 'event', 'send_updates'}, 'invalid_calendar_payload')
        calendar, event, notifications = payload['calendar_id'], payload['event'], payload['send_updates']
        _require(isinstance(calendar, str) and calendar and calendar != 'primary', 'concrete_calendar_required')
        _require(notifications in {'none', 'all', 'externalOnly'}, 'explicit_notification_policy_required')
        _require(isinstance(event, dict), 'event_payload_required')
        action, target = p['action'], p['target']['id']
        for field in {'summary', 'description', 'location', 'visibility', 'transparency'} & set(event):
            _require(isinstance(event[field], str), 'invalid_event_field')
        if 'recurrence' in event:
            _require(isinstance(event['recurrence'], list) and all(isinstance(r, str) for r in event['recurrence']), 'invalid_recurrence')
        if 'extendedProperties' in event:
            ext = event['extendedProperties']
            _require(isinstance(ext, dict) and set(ext) <= {'private', 'shared'}
                     and all(isinstance(v, dict) and all(isinstance(k, str) and isinstance(x, str) for k, x in v.items()) for v in ext.values()),
                     'invalid_extended_properties')
        if action == 'insert':
            _require(isinstance(target, str) and re.fullmatch('[a-v0-9]{5,1024}', target) is not None,
                     'client_event_id_required')
            _require(event.get('id') == target and set(event) <= self.PATCH_FIELDS | {'id', 'attendees'}, 'invalid_insert_fields')
            if 'attendees' in event:
                _require(isinstance(event['attendees'], list) and all(isinstance(a, dict) and set(a) == {'email'}
                    and isinstance(a['email'], str) and '@' in a['email'] for a in event['attendees']), 'insert_invitees_required')
            start, day = _boundary(event.get('start'), _zone(event.get('start', {}).get('timeZone', 'UTC')))
            end, end_day = _boundary(event.get('end'), _zone(event.get('end', {}).get('timeZone', 'UTC')))
            _require(end > start and day == end_day, 'event_interval_invalid')
        elif action == 'update':
            _require(event and set(event) <= self.PATCH_FIELDS, 'invalid_patch_fields')
        elif action == 'decline':
            _require(set(event) <= {'attendees', 'attendeesOmitted', 'extendedProperties'}
                     and event.get('attendeesOmitted') is True and isinstance(event.get('attendees'), list)
                     and len(event['attendees']) == 1 and set(event['attendees'][0]) == {'email', 'responseStatus'}
                     and event['attendees'][0]['responseStatus'] == 'declined', 'self_decline_payload_required')
        else:
            _require(action in {'delete_copy', 'cancel_event'} and not event, 'empty_delete_payload_required')
        return calendar, copy.deepcopy(event), notifications

    def _record(self, identity, **fields):
        with self.service.store.transaction():
            key = 'calendar-effect:' + identity
            state = self.service._meta(key, {})
            state.update(copy.deepcopy(fields))
            self.service._set_meta(key, state)
            return state

    def _stored(self, identity):
        with self.service.store.lock:
            return self.service._meta('calendar-effect:' + identity, {})

    def _observation(self, effect, status, **fields):
        p = effect['proposal']
        return {**{k: p[k] for k in ('provider', 'account', 'action', 'target')},
                'request_hash': effect['proposal_hash'], 'status': status, **fields}

    def _uncertain(self, effect, reason):
        result = self.effects.observe(effect['id'], self._observation(effect, 'uncertain'))
        return {'status': 'uncertain', 'effect_id': effect['id'], 'reason': reason, 'observation': result}

    async def _preflight(self, effect):
        p = effect['proposal']
        calendar, event, notifications = self._payload(effect)
        await self.transport._effect_prepare(p['account'])
        _require(self.transport.authenticated_account == p['account'], 'account_mismatch')
        metadata = _document(await self.transport._calendar_effect_get(calendar, calendar_list=True))
        _require(metadata.get('id') == calendar and metadata.get('accessRole') in {'owner', 'writer'}, 'calendar_write_role_required')
        response = await self.transport._calendar_effect_get(calendar, p['target']['id'])
        if p['action'] == 'insert':
            _require(response['status'] == 404, 'client_event_id_already_exists_or_unverified')
            before = None
        else:
            before = _document(response)
            _require(before.get('id') == p['target']['id'] and before.get('etag') == p['expected_remote_version'], 'remote_version_conflict')
            _require(before.get('status') != 'cancelled', 'event_already_cancelled')
            _require(isinstance(before.get('organizer', {}), dict) and isinstance(before.get('attendees', []), list)
                     and all(isinstance(a, dict) for a in before.get('attendees', [])), 'event_participation_invalid')
            organizer = before.get('organizer', {}).get('self')
            if p['action'] in {'cancel_event', 'update'}:
                _require(organizer is True, 'organizer_required')
            elif p['action'] == 'delete_copy':
                _require(organizer is False, 'nonorganizer_copy_required')
            else:
                own = [a for a in before.get('attendees', []) if a.get('self') is True]
                _require(organizer is False and len(own) == 1 and own[0].get('email') == event['attendees'][0]['email'], 'self_attendee_required')
            if 'start' in event or 'end' in event:
                zone = _zone(metadata.get('timeZone'))
                start, all_day = _boundary(event.get('start', before.get('start')), zone)
                end, end_all_day = _boundary(event.get('end', before.get('end')), zone)
                _require(end > start and all_day == end_all_day, 'event_interval_invalid')
            if 'extendedProperties' in event:
                old = before.get('extendedProperties', {})
                new = event['extendedProperties']
                _require(isinstance(new, dict) and set(new) <= {'private', 'shared'}, 'invalid_extended_properties')
                for visibility, values in old.items():
                    _require(isinstance(new.get(visibility), dict) and all(
                        k == self.MARKER or new[visibility].get(k) == v for k, v in values.items()), 'existing_properties_must_be_preserved')
                marker = new.get('private', {}).get(self.MARKER)
                if marker:
                    _require(isinstance(marker, str) and marker != old.get('private', {}).get(self.MARKER), 'operation_marker_not_new')
        return calendar, event, notifications, before

    def _begin_dispatch(self, effect):
        # Shared durable history, not an adapter-local lock or terminal-state filter.
        with self.service.store.lock:
            p = effect['proposal']
            if p['action'] == 'insert':
                for existing in self.effects._load()['effects'].values():
                    other = existing['proposal']
                    if (existing['id'] != effect['id'] and 'dispatch' in existing
                            and other['provider'] == 'calendar' and other['action'] == 'insert'
                            and other['account'] == p['account']
                            and other['payload']['calendar_id'] == p['payload']['calendar_id']
                            and other['target']['id'] == p['target']['id']):
                        return {'status': 'rejected', 'error': 'insert_identity_already_dispatched'}
            return self.effects.begin_dispatch(effect['id'])

    async def dispatch(self, effect_id):
        async with self._locks.setdefault(effect_id, asyncio.Lock()):
            effect = self._effect(effect_id)
            if 'dispatch' in effect:
                return await self.reconcile(effect_id)
            try:
                calendar, event, notifications, before = await self._preflight(effect)
            except (CalendarError, TransportError, TypeError, KeyError, ValueError) as error:
                return {'status': 'rejected', 'reason': str(error) if isinstance(error, CalendarError) else 'calendar_preflight_failed'}
            self._record(effect_id, proposal_hash=effect['proposal_hash'], before=before)
            p = effect['proposal']
            try:
                sent = await self.transport._calendar_effect_write(p['action'], calendar,
                    None if p['action'] == 'insert' else p['target']['id'],
                    None if p['action'] in {'delete_copy', 'cancel_event'} else event, p['account'],
                    lambda: self._begin_dispatch(effect), etag=p.get('expected_remote_version'), send_updates=notifications)
            except (TransportError, OSError, asyncio.TimeoutError):
                latest = self._effect(effect_id)
                return self._uncertain(latest, 'write_response_unknown') if 'dispatch' in latest else {'status': 'rejected', 'reason': 'transport_prepared_write_failed'}
            if sent['admission'].get('status') != 'dispatch':
                return {'status': 'rejected', 'reason': sent['admission'].get('error', 'already_dispatched')}
            response = sent['response']
            latest = self._effect(effect_id)
            evidence = 'calendar-response:' + _hash([effect_id, effect['proposal_hash'], response['status'], response['body'].hex()])
            self._record(effect_id, response_status=response['status'], response_evidence=evidence)
            if response['status'] == 412 and p['action'] != 'insert':
                proof = {'kind': 'conditional_write_rejected', 'http_status': 412,
                         'dispatch_id': latest['dispatch']['id'], 'expected_remote_version': p['expected_remote_version']}
                return self.effects.observe(effect_id, self._observation(effect, 'conflict', proof=proof, evidence_reference=evidence))
            if response['status'] not in {200, 201, 204}:
                return self._uncertain(latest, 'provider_write_not_confirmed')
            if p['action'] in {'delete_copy', 'cancel_event'}:
                if response['status'] != 204:
                    return self._uncertain(latest, 'delete_ack_invalid')
                self._record(effect_id, acknowledged=True)
            else:
                try:
                    value = _document({**response, 'status': 200})
                    _require(value.get('id') == p['target']['id'] and isinstance(value.get('etag'), str), 'write_ack_identity_invalid')
                except CalendarError:
                    return self._uncertain(latest, 'write_ack_invalid')
                self._record(effect_id, acknowledged=True, ack_etag=value['etag'])
            self.effects.observe(effect_id, self._observation(effect, 'ack', remote_id=p['target']['id'], evidence_reference=evidence))
            return await self.reconcile(effect_id)

    @staticmethod
    def _matches(actual, requested, path=()):
        if path in {('start', 'dateTime'), ('end', 'dateTime')}:
            def instant(value):
                if not isinstance(value, str) or not re.fullmatch(
                        r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2}(?:\.\d{1,6})?)?(?:Z|[+-]\d{2}:\d{2})', value):
                    return None
                if value[-1] != 'Z' and (int(value[-5:-3]) > 23 or int(value[-2:]) > 59):
                    return None
                try:
                    return datetime.fromisoformat(value.replace('Z', '+00:00')).astimezone(timezone.utc)
                except ValueError:
                    return None
            expected, observed = instant(requested), instant(actual)
            return expected is not None and observed is not None and expected == observed
        if isinstance(requested, dict):
            return isinstance(actual, dict) and all(CalendarEffects._matches(actual.get(k), v, path + (k,)) for k, v in requested.items())
        if isinstance(requested, list):
            if requested and all(isinstance(a, dict) and 'email' in a for a in requested):
                return isinstance(actual, list) and len(actual) == len(requested) and all(any(CalendarEffects._matches(a, r) for a in actual) for r in requested)
            return actual == requested
        return actual == requested

    async def reconcile(self, effect_id):
        effect = self._effect(effect_id)
        if effect['status'] in {'confirmed', 'no_dispatch', 'conflict'}:
            return {'status': effect['status'], 'effect_id': effect_id}
        _require('dispatch' in effect, 'dispatch_intent_required')
        calendar, event, _ = self._payload(effect)
        p, state = effect['proposal'], self._stored(effect_id)
        if state.get('proposal_hash') != effect['proposal_hash']:
            return self._uncertain(effect, 'driver_evidence_not_bound')
        if state.get('response_status') == 412 and state.get('response_evidence') and p['action'] != 'insert':
            return self.effects.observe(effect_id, self._observation(effect, 'conflict',
                evidence_reference=state['response_evidence'], proof={'kind': 'conditional_write_rejected',
                    'http_status': 412, 'dispatch_id': effect['dispatch']['id'],
                    'expected_remote_version': p['expected_remote_version']}))
        try:
            await self.transport._effect_prepare(p['account'])
            response = await self.transport._calendar_effect_get(calendar, p['target']['id'])
            deleting = p['action'] in {'delete_copy', 'cancel_event'}
            if deleting:
                absent = response['status'] in {404, 410}
                if response['status'] == 200:
                    current = _document(response)
                    absent = current.get('id') == p['target']['id'] and current.get('status') == 'cancelled'
                _require(state.get('acknowledged') and absent, 'delete_causality_unverified')
                current = {'id': p['target']['id'], 'absent': True}
            else:
                current = _document(response)
                requested = {k: v for k, v in event.items() if k != 'attendeesOmitted'}
                if p['action'] == 'decline':
                    self_reply = requested.pop('attendees')[0]
                    _require(isinstance(current.get('attendees', []), list) and all(isinstance(a, dict) for a in current.get('attendees', [])), 'event_participation_invalid')
                    self_actual = [a for a in current.get('attendees', []) if a.get('self') is True]
                    _require(len(self_actual) == 1 and self._matches(self_actual[0], self_reply), 'self_reply_not_observed')
                    before_others = [a for a in (state.get('before') or {}).get('attendees', []) if a.get('self') is not True]
                    after_others = [a for a in current.get('attendees', []) if a.get('self') is not True]
                    _require(sorted(before_others, key=lambda a: a.get('email', '')) == sorted(after_others, key=lambda a: a.get('email', '')), 'other_participation_changed')
                _require(current.get('id') == p['target']['id'] and isinstance(current.get('etag'), str)
                         and current.get('status') != 'cancelled' and self._matches(current, requested), 'readback_content_mismatch')
                if state.get('acknowledged'):
                    _require(current['etag'] == state.get('ack_etag'), 'readback_version_changed')
                elif p['action'] != 'insert':
                    marker = event.get('extendedProperties', {}).get('private', {}).get(self.MARKER)
                    _require(state.get('before') is not None and marker and
                        state['before'].get('extendedProperties', {}).get('private', {}).get(self.MARKER) != marker
                        and current['etag'] != p['expected_remote_version'], 'update_causality_unverified')
            readback = {**{k: p[k] for k in ('provider', 'account', 'action', 'target')},
                        'request_hash': effect['proposal_hash'], 'remote_id': p['target']['id'],
                        'fixed_identity': p['target']['id'], 'content_verified': True}
            evidence = 'calendar-readback:' + _hash([effect_id, effect['proposal_hash'], current])
            self._record(effect_id, readback=current, readback_evidence=evidence)
            result = self.effects.observe(effect_id, self._observation(effect, 'confirmed', remote_id=p['target']['id'],
                                         evidence_reference=evidence, readback=readback))
            return {**result, 'notifications_verified': False}
        except (CalendarError, TransportError, TypeError, KeyError, ValueError):
            return self._uncertain(effect, 'readback_or_causality_unverified')
