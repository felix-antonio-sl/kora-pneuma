"""Read-only Google source adapters, without OAuth or a network implementation.

Transport contract: authenticated_account identifies the credential's verified
account, and async request('GET', absolute_url, params=dict) returns
{'status': int, 'body': bytes}. It must enforce its own connection timeout and
must not redirect requests to another authority. Bodies are bounded here before
parsing; transports should bound their receive buffers too.

Gmail supports legacy whole-mailbox scope and explicit selective_since scope
from epoch 1785556800. Selection requires an injected ephemeral evaluator;
only selected revisions retain originals. No arbitrary search or label selectors. Original JSON response bytes retain RAW MIME/attachments; text projection does not interpret
attachments, HTML, or remote content. Calendar sync preserves raw masters and
exceptions (singleEvents=false), without expanding recurrence or bounding time.
"""
import asyncio
import base64
import binascii
import copy
from email import policy
from email.parser import BytesParser
import hashlib
from html.parser import HTMLParser
import json
import inspect
import re
from urllib.parse import quote
import uuid

from .source_entries import get as get_entry, record_decision
from .source_error_codes import sanitize_adapter_error, TransportError
from .source_sync import _hash, _json, _now
DECIDED = frozenset({'selected', 'noise', 'uncertain'})


class VisibleHTML(HTMLParser):
    """Text-only projection: no browser, fetching, CSS execution or DOM effects."""
    VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
    HIDDEN = {'script','style','head','template','noscript'}
    BLOCK = {'p','div','section','article','header','footer','li','tr','h1','h2','h3','h4','h5','h6','blockquote'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.parts = [], []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        style = ''.join((values.get('style') or '').lower().split())
        hidden = (any(v for _,v in self.stack) or tag in self.HIDDEN or 'hidden' in values
                  or (values.get('aria-hidden') or '').lower() == 'true'
                  or 'display:none' in style or 'visibility:hidden' in style)
        if not hidden and (tag in self.BLOCK or tag in {'br','hr'}):
            self.parts.append('\n')
        if tag not in self.VOID:
            self.stack.append((tag, hidden))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for index in range(len(self.stack)-1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                break
        if tag in self.BLOCK and not any(v for _,v in self.stack):
            self.parts.append('\n')

    def handle_data(self, data):
        if not any(v for _,v in self.stack):
            self.parts.append(data)

    def text(self):
        return '\n'.join(line for line in (' '.join(v.split()) for v in ''.join(self.parts).splitlines()) if line)


class ResponseDocument(dict):
    def __init__(self, value, original):
        super().__init__(value)
        self.original = original


class SourceError(ValueError):
    pass


def _require(value, code):
    if not value:
        raise SourceError(code)


def _string(value):
    return isinstance(value, str) and bool(value)


_GMAIL_SCOPE_QUERY = 'after:1785556800'
_PRIORITY_TOKEN_PREFIX = 'gtd-priority-v1:'


def priority_query(terms):
    """Only bounded literal phrases; no caller-controlled Gmail operators/escapes."""
    _require(isinstance(terms, list) and len(terms) <= 12, 'invalid_priority_terms')
    for term in terms:
        _require(isinstance(term, str) and 0 < len(term) <= 80
            and term == ' '.join(term.split())
            and all(char.isalnum() or char == ' ' for char in term), 'invalid_priority_terms')
    _require(len({term.casefold() for term in terms}) == len(terms), 'invalid_priority_terms')
    return _GMAIL_SCOPE_QUERY + (' {' + ' '.join('"' + term + '"' for term in terms) + '}' if terms else '')


def canonical_gmail_query(query):
    if query == _GMAIL_SCOPE_QUERY:
        return True
    prefix = _GMAIL_SCOPE_QUERY + ' {'
    if not isinstance(query, str) or not query.startswith(prefix) or not query.endswith('}'):
        return False
    terms = re.findall(r'"([^"\n]+)"', query[len(prefix):-1])
    try:
        return bool(terms) and priority_query(terms) == query
    except SourceError:
        return False


def _priority_token(priority, phase, token):
    data = {'generation': priority['generation'], 'phase': phase, 'google_token': token}
    return _PRIORITY_TOKEN_PREFIX + base64.urlsafe_b64encode(_json(data).encode()).decode()


def _priority_position(priority, token):
    if 'topics_entry_token' in priority and token == priority['topics_entry_token']:
        return 'topics', {'index': 0, 'cursors': [None] * len(priority['terms'])}
    if token == priority['entry_token']:
        return 'priority', None
    _require(isinstance(token, str) and token.startswith(_PRIORITY_TOKEN_PREFIX), 'invalid_priority_page_state')
    try:
        data = json.loads(base64.urlsafe_b64decode(token[len(_PRIORITY_TOKEN_PREFIX):]))
    except (ValueError, binascii.Error, UnicodeError):
        raise SourceError('invalid_priority_page_state') from None
    _require(isinstance(data, dict) and set(data) == {'generation', 'phase', 'google_token'}
        and data['generation'] == priority['generation'] and data['phase'] in {'priority', 'global', 'topics'},
        'invalid_priority_page_state')
    position = data['google_token']
    if data['phase'] == 'topics':
        _require('topics_entry_token' in priority and isinstance(position, dict)
            and set(position) == {'index', 'cursors'} and type(position['index']) is int
            and isinstance(position['cursors'], list) and len(position['cursors']) == len(priority['terms'])
            and 0 <= position['index'] < len(position['cursors'])
            and all(value is None or value is False or _string(value) for value in position['cursors'])
            and position['cursors'][position['index']] is not False, 'invalid_priority_page_state')
    else:
        _require(position is None or _string(position), 'invalid_priority_page_state')
    _require(_priority_token(priority, data['phase'], data['google_token']) == token, 'invalid_priority_page_state')
    return data['phase'], data['google_token']


def _next_topic(priority, position, next_token):
    """Page advancement is encoded in the committed page, never mutable side state."""
    position = copy.deepcopy(position)
    current = position['index']
    position['cursors'][current] = False if next_token is None else next_token
    for distance in range(1, len(position['cursors']) + 1):
        index = (current + distance) % len(position['cursors'])
        if position['cursors'][index] is not False:
            position['index'] = index
            return _priority_token(priority, 'topics', position)
    return _priority_token(priority, 'global', priority['entry_token'])


class GoogleSources:
    def __init__(self, sync, transport, config, *, evaluator=None, projection_guard=None):
        self.sync, self.store, self.transport = sync, sync.store, transport
        self.evaluator = evaluator
        self.projection_guard = projection_guard
        self.config = copy.deepcopy(config)
        self._locks = {}
        _require(isinstance(config, dict) and config, 'source_config_required')
        for source_id in config:
            self._source(source_id)

    def _source(self, source_id):
        _require(source_id in self.config and _string(source_id), 'unknown_source')
        cfg = self.config[source_id]
        allowed = {'provider', 'account', 'calendar_id', 'scope', 'page_size', 'max_pages', 'max_response_bytes', 'request_timeout_seconds', 'pending_retry_limit', 'since_epoch', 'priority_terms', 'priority_strategy'}
        _require(isinstance(cfg, dict) and not set(cfg) - allowed, 'unsupported_source_filter')
        _require(cfg.get('provider') in {'gmail', 'calendar'} and _string(cfg.get('account')), 'explicit_account_required')
        selective = cfg['provider'] == 'gmail' and cfg.get('scope') == 'selective_since'
        _require(selective or cfg.get('scope') == ('whole_mailbox' if cfg['provider'] == 'gmail' else 'calendar_masters_and_exceptions'), 'explicit_coverage_scope_required')
        _require(cfg.get('since_epoch') == 1785556800 if selective else 'since_epoch' not in cfg, 'explicit_since_scope_required')
        if 'priority_terms' in cfg:
            _require(selective, 'priority_requires_selective_scope')
            priority_query(cfg['priority_terms'])
        if 'priority_strategy' in cfg:
            _require(selective and bool(cfg.get('priority_terms'))
                and cfg['priority_strategy'] in ('combined', 'round_robin'), 'invalid_priority_strategy')
        calendar = cfg.get('calendar_id')
        _require(cfg['provider'] != 'calendar' or _string(calendar) and calendar != 'primary', 'concrete_calendar_required')
        _require(cfg['provider'] != 'gmail' or calendar is None, 'gmail_calendar_mismatch')
        for key, default, maximum in [('page_size', 100, 500), ('max_pages', 100, 1000),
                                      ('max_response_bytes', 6 * 1024 * 1024, 8 * 1024 * 1024),
                                      ('request_timeout_seconds', 20, 60), ('pending_retry_limit', 10, 100)]:
            value = cfg.get(key, default)
            _require(type(value) is int and 0 < value <= maximum, 'invalid_source_limit')
        params = {'maxResults': cfg.get('page_size', 100)}
        if cfg['provider'] == 'gmail':
            params['includeSpamTrash'] = 'true'
            if selective:
                params['q'] = 'after:' + str(cfg['since_epoch'])
        else:
            params.update(singleEvents='false', showDeleted='true')
        partition = {'provider': cfg['provider'], 'account': cfg['account'],
            'collection': 'messages' if cfg['provider'] == 'gmail' else calendar,
            'scope_digest': _hash({'params': params, 'representation': 'raw-mime-v1' if cfg['provider'] == 'gmail' else 'raw-event-v1'})}
        return cfg, params, partition

    def _key(self, partition):
        return 'source-sync:google:' + _hash(partition)

    def _load(self, partition):
        with self.store.lock:
            row = self.store.db.execute('SELECT value FROM metadata WHERE key=?', (self._key(partition),)).fetchone()
            return json.loads(row[0]) if row else None

    def _save(self, partition, state):
        with self.store.transaction():
            self.store.db.execute('INSERT INTO metadata VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value',
                                  (self._key(partition), _json(state)))

    def inspect(self, source_id):
        cfg, params, partition = self._source(source_id)
        adapter = self._load(partition)
        state = self.sync.inspect(partition)
        pending = (adapter or {}).get('pending_reads', {})
        priority = (adapter or {}).get('priority')
        phase = None
        position = None
        if priority and state and adapter.get('cycle_id') in state['cycles']:
            cycle = state['cycles'][adapter['cycle_id']]
            if cycle['status'] == 'complete':
                phase = 'complete'
            else:
                phase, position = _priority_position(priority, cycle['next_page_token'])
        health = 'degraded' if pending or (adapter or {}).get('error') or state and state['coverage'] in {'degraded','rebuild_required'} else 'complete' if state and state['coverage'] == 'complete' and state['projection'] == 'current' else 'in_progress'
        return {'partition': partition, 'effective_parameters': params, 'health': health,
            'originals_complete': not pending and bool(state) and state['coverage'] == 'complete',
            'pending_reads': copy.deepcopy(pending),
            'priority': {'phase': phase, 'terms': copy.deepcopy(priority['terms']) if priority else [],
                'next_term': priority['terms'][position['index']] if phase == 'topics' else None,
                'global_backfill_pending': bool(priority and phase != 'complete')},
            'coverage_contract': {'scope': 'selective_since_including_spam_trash' if cfg.get('scope') == 'selective_since' else 'whole_mailbox_including_spam_trash' if cfg['provider'] == 'gmail' else 'calendar_masters_and_exceptions',
                'interval': {'since_epoch': cfg['since_epoch'], 'timezone': 'America/Santiago'} if cfg.get('scope') == 'selective_since' else None, 'recurrence_expanded': False, 'attachments_interpreted': False,
                'semantic_review': ('evaluated' if health == 'complete' else 'pending' if pending or state else 'not_evaluated') if cfg.get('scope') == 'selective_since' else 'not_evaluated',
                'retention': 'selected_originals_only' if cfg.get('scope') == 'selective_since' else 'all_originals',
                'history_continuity': 'lost_rebuilt_scope' if (adapter or {}).get('continuity_lost_at') else 'not_lost_observed'},
            'adapter': adapter, 'sync': state}

    async def _get(self, cfg, url, params):
        _require(getattr(self.transport, 'authenticated_account', None) == cfg['account'], 'credential_account_mismatch')
        response = await asyncio.wait_for(self.transport.request('GET', url, params=copy.deepcopy(params)),
                                         cfg.get('request_timeout_seconds', 20))
        _require(isinstance(response, dict) and type(response.get('status')) is int
                 and isinstance(response.get('body'), bytes), 'invalid_http_response')
        _require(len(response['body']) <= cfg.get('max_response_bytes', 6 * 1024 * 1024), 'response_too_large')
        status = response['status']
        if status != 200:
            return status, {}
        try:
            body = json.loads(response['body'])
        except (ValueError, UnicodeError):
            raise SourceError('invalid_json') from None
        _require(isinstance(body, dict), 'invalid_response_shape')
        return status, ResponseDocument(body, response['body'])

    async def _ok(self, cfg, url, params):
        status, body = await self._get(cfg, url, params)
        _require(status == 200, 'http_' + str(status))
        return body

    def _gmail_object(self, message, identity):
        _require(message.get('id') == identity and _string(message.get('threadId'))
                 and _string(message.get('historyId')) and _string(message.get('raw')),
                 'message_identity_or_raw_missing')
        _require(_string(message.get('internalDate')) and message['internalDate'].isdigit()
                 and ('labelIds' not in message or isinstance(message['labelIds'], list) and all(_string(v) for v in message['labelIds'])),
                 'message_metadata_missing')
        raw = message['raw']
        try:
            rfc = base64.b64decode(raw + '=' * (-len(raw) % 4), altchars=b'-_', validate=True)
            parsed = BytesParser(policy=policy.default).parsebytes(rfc)
        except (ValueError, binascii.Error):
            raise SourceError('invalid_raw_message') from None
        original = message.original
        _require(len(original) <= 4 * 1024 * 1024, 'message_too_large')
        _require(not parsed.defects, 'mime_parse_degraded')
        parts, html_parts, attachments = [], [], []
        for part in parsed.walk():
            _require(not part.defects, 'mime_parse_degraded')
            if part.is_multipart():
                continue
            if part.get_content_disposition() == 'attachment' or part.get_filename():
                attachments.append({'filename': part.get_filename(), 'content_type': part.get_content_type()})
            elif part.get_content_type() in {'text/plain','text/html'}:
                try:
                    content = part.get_content()
                    if part.get_content_type() == 'text/plain':
                        parts.append(content)
                    else:
                        parser = VisibleHTML(); parser.feed(content); parser.close()
                        html_parts.append(parser.text())
                except (LookupError, UnicodeError, ValueError):
                    raise SourceError('mime_text_decode_degraded') from None
        metadata = {k: message.get(k) for k in ('id', 'threadId', 'historyId', 'internalDate', 'labelIds')}
        metadata['headers'] = {k: str(parsed[k]) for k in ('Subject', 'From', 'To', 'Date', 'Message-ID') if parsed[k] is not None}
        metadata['attachments_not_interpreted'] = attachments
        metadata['html_not_executed_or_rendered'] = True
        metadata['body_projection'] = 'plain' if parts else 'visible_html' if html_parts else 'unavailable'
        text = _json(metadata) + '\n\n' + ('\n'.join(parts or html_parts) if parts or html_parts else '[No text body; original MIME retained, attachments not interpreted.]')
        _require(len(text) <= 1024 * 1024, 'message_text_too_large')
        return dict(external_id=identity, revision='message:' + message['historyId'] + ':' + hashlib.sha256(original).hexdigest(), status='present',
            text=text, original=original, sha256=hashlib.sha256(original).hexdigest(),
            url='https://mail.google.com/mail/u/' + quote(self.transport.authenticated_account, safe='') + '/#all/' + quote(identity, safe=''),
            mime_type='application/json')

    def _mail_url(self, cfg, identity):
        return 'https://mail.google.com/mail/u/' + quote(cfg['account'], safe='') + '/#all/' + quote(identity, safe='')

    async def _read_message(self, cfg, identity, adapter):
        if cfg.get('scope') == 'selective_since':
            return await self._read_selective_message(cfg, identity, adapter)
        try:
            message = await self._ok(cfg, 'https://gmail.googleapis.com/gmail/v1/users/me/messages/' + quote(identity, safe=''), {'format':'raw'})
            obj = self._gmail_object(message, identity)
            if identity in adapter.get('pending_reads', {}):
                adapter['pending_reads'][identity]['resolving_revision'] = obj['revision']
            return obj
        except (SourceError, TransportError) as exc:
            if isinstance(exc, TransportError):
                code = 'evaluation_unavailable'
            elif str(exc) not in {'response_too_large','message_too_large','mime_parse_degraded',
                'mime_text_decode_degraded','invalid_raw_message','message_text_too_large','http_404',
                'message_metadata_missing','message_identity_or_raw_missing'}:
                raise
            else:
                code = str(exc)
            stamp = _now()
            pending = adapter.setdefault('pending_reads', {}).setdefault(identity,
                {'external_id':identity, 'observed_at':stamp, 'attempts':0})
            pending.update(reason=code, last_attempt_at=stamp, attempts=pending['attempts']+1)
            pending.pop('resolving_revision', None)
            return dict(external_id=identity, revision='unread-observation:' + _hash([identity, pending['observed_at'], pending['reason']]), status='degraded',
                        text=None, original=None, sha256=None, url=self._mail_url(cfg, identity))

    def _unretained_message(self, cfg, identity, revision, adapter):
        record = self.sync._load(self.sync._object_key(adapter['partition'], identity))
        if record and record.get('item_id'):
            return dict(external_id=identity, revision=revision, status='degraded',
                text=None, original=None, sha256=None, url=self._mail_url(cfg, identity))
        return None

    def _stored_decision(self, cfg, partition, adapter, identity, revision):
        # The table is the selection authority. A decision persisted by
        # older code in the adapter dict is adopted once and only before the
        # migration cut; after the cut the archive is never reread, so pruned
        # rows and post-cut verdicts stay exactly as left.
        row = get_entry(self.store, 'gmail', cfg['account'], partition['collection'],
                        identity, revision)
        if row is not None and row['status'] in DECIDED:
            return {'classification': row['status'],
                    'reason_code': json.loads(row['metadata_json']).get('reason_code')}
        with self.store.lock:
            cut = self.store.db.execute(
                "SELECT 1 FROM metadata WHERE key='migration:i3'").fetchone()
        if cut is not None:
            return None
        legacy = (adapter.get('decisions') or {}).get(_hash([identity, revision]))
        if (isinstance(legacy, dict) and legacy.get('classification') in DECIDED
                and legacy.get('external_id') == identity and legacy.get('revision') == revision):
            record_decision(self.store, provider='gmail', account=cfg['account'],
                collection=partition['collection'], external_id=identity, revision=revision,
                decision=legacy['classification'], reason_code=legacy.get('reason_code'))
            return {'classification': legacy['classification'],
                    'reason_code': legacy.get('reason_code')}
        return None

    async def _read_selective_message(self, cfg, identity, adapter):
        partition = adapter['partition']
        pending = adapter.setdefault('pending_reads', {}).setdefault(identity,
            {'external_id': identity, 'revision': None, 'observed_at': _now(), 'attempts': 0})
        pending.update(attempts=pending['attempts'] + 1, last_attempt_at=_now(), reason='evaluation_pending')
        pending.pop('resolving_revision', None)
        pending['revision'] = None
        self._save(partition, adapter)  # obligation precedes network/evaluator and cursor
        try:
            message = await self._ok(cfg, 'https://gmail.googleapis.com/gmail/v1/users/me/messages/' + quote(identity, safe=''), {'format': 'raw'})
            _require(message.get('id') == identity and _string(message.get('historyId'))
                and _string(message.get('internalDate')) and message['internalDate'].isdigit(), 'message_metadata_missing')
            revision = 'message:' + message['historyId'] + ':' + hashlib.sha256(message.original).hexdigest()
            pending['revision'] = revision
            self._save(partition, adapter)
            stored = self._stored_decision(cfg, partition, adapter, identity, revision)
            decision = stored
            if int(message['internalDate']) < cfg['since_epoch'] * 1000:
                decision = {'classification': 'noise', 'reason_code': 'outside_scope'}
            elif decision is None or decision['classification'] == 'uncertain':
                _require(callable(self.evaluator), 'evaluator_unavailable')
                obj = self._gmail_object(message, identity)
                # Caller owns model budget and no-retention transport. This adapter
                # never persists evaluator input, free-form rationale or transcript.
                try:
                    result = self.evaluator({'external_id': identity, 'revision': revision,
                        'text': obj['text'], 'original': obj['original'], 'mime_type': obj['mime_type']})
                    if inspect.isawaitable(result):
                        result = await result
                except Exception:
                    raise SourceError('evaluation_unavailable') from None
                _require(isinstance(result, dict) and set(result) == {'classification', 'reason_code'}
                    and result['classification'] in {'selected', 'noise', 'uncertain'}
                    and result['reason_code'] in {'gtd_relevant', 'non_actionable', 'needs_review', 'evaluation_unavailable'},
                    'invalid_evaluation')
                _require(result['reason_code'] in ({'gtd_relevant'} if result['classification'] == 'selected'
                    else {'non_actionable'} if result['classification'] == 'noise'
                    else {'needs_review', 'evaluation_unavailable'}), 'invalid_evaluation')
                decision = dict(result)
            # The table owns the decision (bodies never cross here); the
            # per-identity pointer stays as transport-scoped pending state.
            record_decision(self.store, provider='gmail', account=cfg['account'],
                collection=partition['collection'],
                external_id=identity, revision=revision,
                decision=decision['classification'],
                reason_code=decision.get('reason_code'))
            adapter.setdefault('current_decisions', {})[identity] = _hash([identity, revision])
            if decision['classification'] == 'uncertain':
                pending['reason'] = decision['reason_code']
                self._save(partition, adapter)
                return self._unretained_message(cfg, identity, 'unassessed:' + revision, adapter)
            if decision['classification'] == 'noise':
                del adapter['pending_reads'][identity]
                self._save(partition, adapter)
                return self._unretained_message(cfg, identity, 'not-selected:' + revision, adapter)
            obj = self._gmail_object(message, identity)
            pending['resolving_revision'] = obj['revision']
            self._save(partition, adapter)
            return obj
        except (SourceError, OSError, asyncio.TimeoutError, TransportError):
            pending['reason'] = 'evaluation_unavailable'
            pending.pop('resolving_revision', None)
            self._save(partition, adapter)
            revision = ('unassessed:' + pending['revision'] if pending.get('revision') else
                        'unread:' + _hash([identity, pending['observed_at']]))
            return self._unretained_message(cfg, identity, revision, adapter)

    def _clear_projected_reads(self, partition, adapter, state):
        if state and state['projection'] == 'current' and not state['pending']:
            for identity, pending in list(adapter.get('pending_reads', {}).items()):
                obj = state['objects'].get(identity, {})
                if pending.get('resolving_revision') == obj.get('revision') and obj.get('availability') in {'present','deleted'}:
                    del adapter['pending_reads'][identity]
            self._save(partition, adapter)

    async def _gmail_page(self, cfg, params, cycle, adapter):
        base = 'https://gmail.googleapis.com/gmail/v1/users/me'
        token = cycle['next_page_token']
        priority = adapter.get('priority') if cycle['mode'] != 'incremental' else None
        phase = None
        if priority:
            phase, token = _priority_position(priority, token)
        topic_position = token if phase == 'topics' else None
        if topic_position is not None:
            token = topic_position['cursors'][topic_position['index']]
        query = {'maxResults': params['maxResults']}
        if token is not None:
            query['pageToken'] = token
        incremental = cycle['mode'] == 'incremental'
        if incremental:
            query['startHistoryId'] = cycle['base_cursor']
            status, body = await self._get(cfg, base + '/history', query)
            if status == 404:
                raise SourceError('cursor_expired')
        else:
            query['includeSpamTrash'] = 'true'
            if 'q' in params:
                query['q'] = (priority_query([priority['terms'][topic_position['index']]]) if phase == 'topics'
                    else priority_query(priority['terms']) if phase == 'priority' else params['q'])
            status, body = await self._get(cfg, base + '/messages', query)
        _require(status == 200, 'http_' + str(status))
        changed, deleted = {}, {}
        if incremental:
            history = body.get('history', [])
            _require(isinstance(history, list), 'invalid_history')
            for entry in history:
                _require(isinstance(entry, dict) and _string(entry.get('id')), 'invalid_history')
                for kind in ('messagesAdded', 'labelsAdded', 'labelsRemoved', 'messagesDeleted'):
                    entries = entry.get(kind, [])
                    _require(isinstance(entries, list), 'invalid_history')
                    for value in entries:
                        message = value.get('message', {}) if isinstance(value, dict) else {}
                        identity = message.get('id')
                        _require(_string(identity), 'history_message_id_missing')
                        if kind == 'messagesDeleted':
                            deleted[identity] = entry['id']
                            changed.pop(identity, None)
                        else:
                            changed[identity] = True
                            deleted.pop(identity, None)
                # Generic messages can repeat typed entries; do not infer deletion.
                for message in entry.get('messages', []):
                    _require(isinstance(message, dict) and _string(message.get('id')), 'invalid_history')
                    if message['id'] not in deleted:
                        changed[message['id']] = True
        else:
            messages = body.get('messages', [])
            _require(isinstance(messages, list), 'invalid_message_list')
            for message in messages:
                _require(isinstance(message, dict) and _string(message.get('id')), 'invalid_message_list')
                changed[message['id']] = True
        objects = []
        for identity in changed:
            obj = await self._read_message(cfg, identity, adapter)
            if obj is not None:
                objects.append(obj)
        for identity, revision in deleted.items():
            if cfg.get('scope') == 'selective_since':
                if identity not in adapter.get('current_decisions', {}) and identity not in adapter.get('pending_reads', {}):
                    continue  # history deletion alone cannot establish the date scope
                # Deletion tombstones flow through intake (status deleted);
                # only the per-identity pointer is transport state.
                adapter.setdefault('current_decisions', {})[identity] = _hash([identity, 'deleted:' + revision])
            if identity in adapter.get('pending_reads', {}):
                adapter['pending_reads'][identity]['resolving_revision'] = 'deleted:' + revision
            objects.append(dict(external_id=identity, revision='deleted:' + revision, status='deleted',
                text=None, original=None, sha256=None,
                url='https://mail.google.com/mail/u/' + quote(cfg['account'], safe='') + '/#all/' + quote(identity, safe='')))
        next_token = body.get('nextPageToken')
        _require(next_token is None or _string(next_token), 'invalid_next_page_token')
        if priority:
            if phase == 'topics':
                next_token = _next_topic(priority, topic_position, next_token)
            elif phase == 'priority':
                next_token = (_priority_token(priority, 'priority', next_token) if next_token is not None
                    else _priority_token(priority, 'global', priority['entry_token']))
            elif next_token is not None:
                next_token = _priority_token(priority, 'global', next_token)
        cursor = body.get('historyId') if incremental else adapter['baseline_history_id']
        _require(next_token is not None or _string(cursor), 'final_cursor_missing')
        return objects, next_token, None if next_token is not None else cursor, set(changed) | set(deleted)

    async def _calendar_page(self, cfg, params, cycle, adapter):
        query = dict(params)
        if cycle['next_page_token'] is not None:
            query['pageToken'] = cycle['next_page_token']
        if cycle['mode'] == 'incremental':
            query['syncToken'] = cycle['base_cursor']
        url = 'https://www.googleapis.com/calendar/v3/calendars/' + quote(cfg['calendar_id'], safe='') + '/events'
        status, body = await self._get(cfg, url, query)
        if status == 410 and cycle['mode'] == 'incremental':
            raise SourceError('cursor_expired')
        _require(status == 200, 'http_' + str(status))
        events = body.get('items', [])
        _require(isinstance(events, list), 'invalid_event_list')
        objects = []
        for event in events:
            _require(isinstance(event, dict) and _string(event.get('id')) and event.get('status') in {'confirmed','tentative','cancelled'}, 'invalid_event')
            original = _json(event).encode()
            _require(len(original) <= 4 * 1024 * 1024, 'event_too_large')
            revision = event.get('etag')
            # Cancelled exceptions may expose only ID; hash their exact tombstone,
            # never fabricate title/dates or withdraw the adopted GTD item.
            _require(_string(revision) or event['status'] == 'cancelled', 'event_revision_missing')
            revision = 'etag:' + revision if revision else 'tombstone:' + hashlib.sha256(original).hexdigest()
            link = event.get('htmlLink') or url + '/' + quote(event['id'], safe='')
            objects.append(dict(external_id=event['id'], revision=revision,
                status='deleted' if event['status'] == 'cancelled' else 'present',
                text=_json(event), original=original, sha256=hashlib.sha256(original).hexdigest(),
                url=link, mime_type='application/json'))
        next_token = body.get('nextPageToken')
        _require(next_token is None or _string(next_token), 'invalid_next_page_token')
        cursor = body.get('nextSyncToken')
        _require(next_token is None and _string(cursor) or next_token is not None and cursor is None, 'final_cursor_missing')
        return objects, next_token, cursor, {obj['external_id'] for obj in objects}

    async def synchronize(self, source_id):
        cfg, params, partition = self._source(source_id)
        async with self._locks.setdefault(self._key(partition), asyncio.Lock()):
            return await self._synchronize(source_id, cfg, params, partition)

    async def _synchronize(self, source_id, cfg, params, partition):
        adapter = self._load(partition)
        cycle_id = adapter.get('cycle_id') if adapter and adapter.get('active') else None
        if cycle_id and adapter.get('priority'):
            _require(cfg.get('priority_terms', []) == adapter['priority']['terms'], 'priority_terms_changed_active_cycle')
            _require('topics_entry_token' not in adapter['priority']
                or cfg.get('priority_strategy', 'combined') == 'round_robin', 'priority_strategy_changed_active_cycle')
        try:
            _require(cfg.get('scope') != 'selective_since' or callable(self.evaluator), 'evaluator_unavailable')
            _require(getattr(self.transport, 'authenticated_account', None) == cfg['account'], 'credential_account_mismatch')
            state = self.sync.inspect(partition)
            if state and state['pending']:
                if self.projection_guard is not None:
                    self.projection_guard()
                state = self.sync.recover(partition)
                if state['projection'] == 'blocked':
                    return self.inspect(source_id)
            if adapter:
                self._clear_projected_reads(partition, adapter, state)
            if cycle_id:
                # Recovery first: a completed durable page is never fetched again.
                if state is None or cycle_id not in state['cycles']:
                    self.sync.begin(partition, cycle_id, adapter['mode'])
                if self.projection_guard is not None:
                    self.projection_guard()
                state = self.sync.recover(partition)
                if state['cycles'][cycle_id]['status'] == 'complete':
                    adapter.update(active=False, status='complete', completed_at=_now())
                    self._save(partition, adapter)
                    return self.inspect(source_id)
            else:
                mode = 'incremental' if state and state['cursor_valid'] else ('rebuild' if state else 'full')
                baseline = None
                if cfg['provider'] == 'gmail':
                    profile = await self._ok(cfg, 'https://gmail.googleapis.com/gmail/v1/users/me/profile', {})
                    _require(profile.get('emailAddress') == cfg['account'] and _string(profile.get('historyId')), 'gmail_profile_mismatch')
                    baseline = profile['historyId']
                cycle_id = uuid.uuid4().hex
                pending_reads = (adapter or {}).get('pending_reads', {})
                previous = adapter or {}
                adapter = {'pending_reads':pending_reads, 'cycle_id': cycle_id, 'mode': mode, 'active': True,
                    'verified_account': cfg['account'], 'started_at': _now(), 'baseline_history_id': baseline,
                    **{key: previous[key] for key in ('decisions', 'current_decisions', 'continuity_lost_at') if key in previous}}
                if cfg.get('scope') == 'selective_since':
                    adapter['partition'] = partition
                self._save(partition, adapter)
                self.sync.begin(partition, cycle_id, mode)
            state = self.sync.inspect(partition)
            cycle = state['cycles'][cycle_id]
            if (cfg.get('priority_terms') and cycle['mode'] in {'full', 'rebuild'}
                    and not adapter.get('priority')):
                adapter['priority'] = {'terms': copy.deepcopy(cfg['priority_terms']),
                    'entry_token': cycle['next_page_token'],
                    'generation': _hash([cycle_id, cycle['next_page_token'], cfg['priority_terms']])}
                self._save(partition, adapter)  # freeze terms/resume point BEFORE the first priority read
            priority = adapter.get('priority')
            if (priority and cfg.get('priority_strategy') == 'round_robin'
                    and 'topics_entry_token' not in priority
                    and _priority_position(priority, cycle['next_page_token'])[0] == 'priority'):
                # Migrate an unfinished combined search without changing partition,
                # cycle, global resume point, or previously evaluated revisions.
                priority['topics_entry_token'] = cycle['next_page_token']
                self._save(partition, adapter)
            priority_active = bool(adapter.get('priority') and
                _priority_position(adapter['priority'], cycle['next_page_token'])[0] in {'priority', 'topics'})
            retried = []
            if cfg['provider'] == 'gmail' and not priority_active:
                pending = adapter.get('pending_reads', {})
                oldest = sorted(pending, key=lambda identity: (pending[identity].get('last_attempt_at', pending[identity]['observed_at']), identity))
                for identity in oldest[:cfg.get('pending_retry_limit', 10)]:
                    obj = await self._read_message(cfg, identity, adapter)
                    if obj is not None:
                        retried.append(obj)
                self._save(partition, adapter)
            for _ in range(cfg.get('max_pages', 100)):
                state = self.sync.inspect(partition)
                cycle = state['cycles'][cycle_id]
                if state['projection'] == 'blocked':
                    return self.inspect(source_id)
                loader = self._gmail_page if cfg['provider'] == 'gmail' else self._calendar_page
                objects, next_token, cursor, current_ids = await loader(cfg, params, cycle, adapter)
                # Every later observation supersedes an earlier retry, including
                # noise/uncertain observations that intentionally retain no body.
                objects = [obj for obj in retried if obj['external_id'] not in current_ids] + objects
                retried = []
                # Read failures/resolution intent precede page commit, so a cut
                # cannot lose the independent retry obligation when cursor advances.
                self._save(partition, adapter)
                request_token = cycle['next_page_token']
                page = {'page_id': _hash([cycle_id, request_token]), 'request_token': request_token,
                    'next_page_token': next_token, 'cursor': cursor, 'objects': objects}
                if self.projection_guard is not None:
                    self.projection_guard()
                state = self.sync.apply_page(partition, cycle_id, page)
                self._clear_projected_reads(partition, adapter, state)
                if state['projection'] == 'blocked':
                    return self.inspect(source_id)
                if state['cycles'][cycle_id]['status'] == 'complete':
                    adapter.update(active=False, status='complete', completed_at=_now())
                    self._save(partition, adapter)
                    return self.inspect(source_id)
            adapter.update(active=True, status='in_progress', yielded_at=_now())
            self._save(partition, adapter)
            return self.inspect(source_id)
        except (SourceError, OSError, asyncio.TimeoutError, ValueError, TransportError) as exc:
            raw = str(exc) if isinstance(exc, (ValueError, SourceError)) else 'transport_unavailable'
            # Closed frontier: only domain literals (incl. bounded http_<status>)
            # propagate to sync.degrade and durable adapter state; anything else
            # (transport/model text, tokens, tracebacks) becomes fixed generic.
            code = sanitize_adapter_error(raw)
            state = self.sync.inspect(partition)
            if cycle_id and state and state['active_cycle'] == cycle_id:
                if code == 'cursor_expired':
                    self.sync.invalidate_cursor(partition, cycle_id)
                else:
                    self.sync.degrade(partition, cycle_id, code)
            adapter = adapter or {'active': False}
            adapter.update(active=False, error=code, degraded_at=_now())
            if code == 'cursor_expired':
                adapter['continuity_lost_at'] = _now()
            self._save(partition, adapter)
            return self.inspect(source_id)
