"""Trusted Gmail effects driver. MIME is immutable; ambiguity never permits resend."""
import asyncio
import base64
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
import hashlib
import json
import re

from .domain import now


class GmailEffectError(ValueError):
    pass


def _require(condition, code):
    if not condition:
        raise GmailEffectError(code)


def _hash(value):
    return hashlib.sha256(value).hexdigest()


def _identity(value):
    return isinstance(value, str) and bool(re.fullmatch(r'[A-Za-z0-9_-]+', value))


def inspect_mime(mime, message_id):
    """Inspect approved bytes, never serialize/recompose them after authorization."""
    _require(isinstance(mime, str), 'immutable_mime_required')
    raw = mime.encode('utf-8')
    message = BytesParser(policy=policy.default).parsebytes(raw)
    _require(not any(part.defects for part in message.walk()), 'mime_malformed')
    _require(isinstance(message_id, str) and re.fullmatch(r'<[^<>\s@]+@[^<>\s@]+>', message_id), 'message_id_invalid')
    _require(message.get_all('Message-ID') == [message_id], 'message_id_mismatch')
    addresses = {}
    for field in ('From', 'To', 'Cc', 'Bcc'):
        values = message.get_all(field, [])
        _require(len(values) <= 1, 'duplicate_address_header')
        addresses[field] = []
        for value in values:
            _require(not value.defects, 'address_invalid')
            for address in value.addresses:
                _require(bool(address.username and address.domain), 'address_invalid')
                addresses[field].append(address.addr_spec)
    _require(len(addresses['From']) == 1 and any(addresses[x] for x in ('To','Cc','Bcc')), 'sender_or_recipients_required')
    _require(not any(key.lower().startswith('resent-') for key in message.keys()), 'resent_headers_unsupported')
    _require(not message.get_all('Sender') or message.get_all('Sender') == message.get_all('From'), 'sender_mismatch')
    _require(len(message.get_all('Subject', [])) == 1, 'subject_required')
    _require(len(message.get_all('Date', [])) == 1 and parsedate_to_datetime(str(message['Date'])).tzinfo is not None, 'date_required')
    _require(message.get('Content-Type') is not None and message.get('MIME-Version') == '1.0', 'content_headers_required')
    for name in ('References', 'In-Reply-To'):
        _require(len(message.get_all(name, [])) <= 1, 'duplicate_thread_header')
    return {'raw': raw, 'sha256': _hash(raw), 'addresses': addresses,
            'subject': str(message['Subject']), 'in_reply_to': str(message.get('In-Reply-To', '')),
            'references': str(message.get('References', '')).split()}


def compare_mime(approved, observed):
    """v1: preserve approved headers/parts, tolerate transfer encoding and CRLF only.

    Added transport tracing headers are ignored, never From/recipient/reply/content
    fields. Missing Bcc or an attachment is unverified, including Gmail omission.
    """
    expected = BytesParser(policy=policy.default).parsebytes(approved)
    actual = BytesParser(policy=policy.default).parsebytes(observed)
    server = {'received','return-path','delivered-to','authentication-results','dkim-signature','x-received'}
    def signature(message, approved_names, *, observed_side=False):
        _require(not message.defects, 'readback_mime_malformed')
        headers = {}
        for key, value in message.items():
            key = key.lower()
            if key in {'content-transfer-encoding','content-type'}:
                continue
            if observed_side and key not in approved_names and (key in server or key.startswith(('arc-', 'x-google-', 'x-gm-'))):
                continue
            headers.setdefault(key, []).append(re.sub(r'\r?\n[ \t]+', ' ', str(value)))
        content_type = message.get_content_type()
        params = [(k.lower(),v) for k,v in message.get_params()[1:]] if message.get_params() else []
        params = sorted((k,v) for k,v in params if k != 'boundary')
        if message.is_multipart():
            parts = list(message.iter_parts())
            payload = parts
        else:
            payload = message.get_payload(decode=True)
            _require(not message.defects, 'readback_mime_malformed')
            _require(isinstance(payload,bytes), 'readback_part_invalid')
            if message.get_content_maintype() == 'text':
                payload = payload.replace(b'\r\n', b'\n')
        return headers, content_type, params, payload
    def compare(left,right):
        names = {x.lower() for x in left.keys()}
        a,b = signature(left,names),signature(right,names,observed_side=True)
        _require(a[:3] == b[:3], 'readback_headers_mismatch')
        if isinstance(a[3],list):
            _require(isinstance(b[3],list) and len(a[3]) == len(b[3]), 'readback_parts_mismatch')
            for x,y in zip(a[3],b[3]): compare(x,y)
            _require(left.preamble == right.preamble and left.epilogue == right.epilogue, 'readback_multipart_text_mismatch')
        else:
            _require(a[3] == b[3], 'readback_body_mismatch')
    compare(expected,actual)
    return {'comparison_profile':'gmail-approved-mime-v1', 'sent_raw_sha256':_hash(approved),
            'observed_raw_sha256':_hash(observed), 'approved_headers_parts_verified':True,
            'tolerances':['server_trace_headers','transfer_encoding','text_crlf']}


class GmailEffects:
    def __init__(self, effects, transport):
        self.effects, self.service, self.transport = effects, effects.service, transport

    def _effect(self, effect_id):
        effect = self.effects.get(self.service.owner_actor, effect_id)
        _require(effect is not None and effect['proposal']['provider'] == 'gmail', 'gmail_effect_required')
        return effect

    def _envelope(self, effect):
        proposal = effect['proposal']
        return {**{k: proposal[k] for k in ('provider','account','action','target')}, 'request_hash': effect['proposal_hash']}

    def _evidence(self, effect, kind, response, **facts):
        digest = _hash(response['body'])
        reference = 'gmail-effect:evidence:' + effect['id'] + ':' + kind + ':' + digest
        record = {'kind': kind, 'observed_at': now(), 'response_sha256': digest,
                  'request_hash': effect['proposal_hash'], 'material_sha256': effect['proposal']['material']['sha256'], **facts}
        with self.service.store.transaction():
            blob = self.service.store.save_original(response['body'])
            self.service.store.db.execute('INSERT OR IGNORE INTO originals VALUES(?,?,?)', (blob['sha256'],blob['size'],blob['path']))
            record['original'] = {**blob, 'mime_type':'application/json'}
            self.service._set_meta(reference, record)
        return reference

    async def _read(self, kind, **kwargs):
        response = await self.transport._effect_get(kind, **kwargs)
        _require(response['status'] == 200, 'gmail_read_http_' + str(response['status']))
        try:
            value = json.loads(response['body'])
        except (ValueError, UnicodeError):
            raise GmailEffectError('gmail_read_invalid_json') from None
        _require(isinstance(value, dict), 'gmail_read_invalid_shape')
        return value, response

    async def _preflight(self, effect):
        proposal = effect['proposal']; payload = proposal['payload']
        await self.transport._effect_prepare(proposal['account'])
        mime = inspect_mime(payload['mime'], payload['message_id'])
        _require(mime['sha256'] == proposal['material']['sha256'], 'material_mime_mismatch')
        aliases, _ = await self._read('send_as')
        valid = [entry for entry in aliases.get('sendAs', []) if isinstance(entry, dict) and entry.get('sendAsEmail') == mime['addresses']['From'][0]
                 and (entry.get('verificationStatus') == 'accepted' or entry.get('isPrimary') is True and entry.get('sendAsEmail') == proposal['account'])]
        _require(len(valid) == 1, 'sender_alias_not_verified')
        thread = payload.get('thread_id')
        if thread:
            _require(_identity(thread), 'thread_id_invalid')
            value, _ = await self._read('thread', identity=thread)
            _require(value.get('id') == thread and isinstance(value.get('messages'), list), 'thread_identity_mismatch')
            parents = []
            for message in value['messages']:
                _require(message.get('threadId') == thread, 'thread_message_mismatch')
                headers = message.get('payload', {}).get('headers', [])
                mapping = {}
                for header in headers:
                    mapping.setdefault(header.get('name', '').lower(), []).append(header.get('value'))
                if mapping.get('message-id') == [mime['in_reply_to']]:
                    parents.append(mapping)
            _require(len(parents) == 1, 'thread_parent_not_verified')
            parent = parents[0]
            _require(parent.get('subject') == [mime['subject']], 'thread_subject_mismatch')
            refs = parent.get('references', [''])
            _require(len(refs) == 1 and mime['references'] == refs[0].split() + [mime['in_reply_to']], 'thread_references_mismatch')
        else:
            _require(not mime['in_reply_to'] and not mime['references'], 'thread_id_required_for_reply')
        return mime

    def _uncertain(self, effect, reason):
        result = self.effects.observe(effect['id'], {**self._envelope(effect), 'status':'uncertain', 'reason':reason})
        if result['status'] == 'rejected':
            return result
        return {'status':'uncertain', 'effect_id':effect['id'], 'reason':reason}

    def _begin(self, effect):
        # RLock covers both the global identity check and the ledger transaction.
        # No nested BEGIN and no await between the check and dispatch admission.
        proposal = effect['proposal']
        with self.service.store.lock:
            for existing in self.effects.list(self.service.owner_actor):
                other = existing['proposal']
                if (existing['id'] != effect['id'] and 'dispatch' in existing
                        and other['provider'] == 'gmail' and other['account'] == proposal['account']
                        and other['action'] == proposal['action']
                        and other['payload']['message_id'] == proposal['payload']['message_id']):
                    return {'status':'rejected', 'error':'message_id_already_dispatched', 'effect_id':effect['id']}
            return self.effects.begin_dispatch(effect['id'])

    async def dispatch(self, effect_id):
        effect = self._effect(effect_id)
        if effect['status'] in {'confirmed','no_dispatch','conflict'}:
            return {'status':effect['status'], 'effect_id':effect_id, 'remote_id':effect.get('remote_id'), 'duplicate':True}
        if 'dispatch' in effect:
            return await self.reconcile(effect_id)
        proposal = effect['proposal']
        try:
            await self._preflight(effect)
            if proposal['action'] == 'draft_update':
                value, response = await self._read('draft', identity=proposal['target']['id'])
                _require(value.get('id') == proposal['target']['id'], 'draft_identity_mismatch')
                reference = self._evidence(effect, 'draft_preserved', response, remote_id=value['id'])
                return {'status':'conflict', 'effect_id':effect_id, 'reason':'draft_update_has_no_native_cas',
                        'evidence_reference':reference, 'remote_preserved':True, 'requires':'new_explicit_draft_create_proposal'}
            raw = base64.urlsafe_b64encode(proposal['payload']['mime'].encode('utf-8')).decode().rstrip('=')
            payload = {'raw':raw}
            if proposal['payload'].get('thread_id'):
                payload['threadId'] = proposal['payload']['thread_id']
            if proposal['action'] == 'draft_create':
                payload = {'message':payload}
            # Refresh/identity preparation is complete before the durable one-shot gate.
            result = await self.transport._effect_post(proposal['action'], payload, proposal['account'],
                lambda: self._begin(effect))
            admission = result['admission']
            if admission['status'] != 'dispatch':
                return admission
            effect = admission['effect']; response = result['response']
            if response is None or response['status'] not in {200,201}:
                return self._uncertain(effect, 'write_response_unconfirmed')
            try:
                ack = json.loads(response['body'])
                remote = ack.get('id')
                _require(_identity(remote), 'ack_identity_invalid')
            except (ValueError, AttributeError):
                return self._uncertain(effect, 'ack_identity_invalid')
            reference = self._evidence(effect, 'ack', response, remote_id=remote)
            observed = self.effects.observe(effect_id, {**self._envelope(effect), 'status':'ack', 'remote_id':remote, 'evidence_reference':reference})
            if observed['status'] != 'acknowledged':
                return observed
            return await self.reconcile(effect_id)
        except asyncio.CancelledError:
            current = self._effect(effect_id)
            if 'dispatch' in current:
                self._uncertain(current, 'dispatch_interrupted')
            raise
        except Exception as error:
            current = self._effect(effect_id)
            if 'dispatch' in current:
                return self._uncertain(current, 'dispatch_or_readback_failed')
            return {'status':'conflict', 'effect_id':effect_id, 'reason':str(error) if isinstance(error,GmailEffectError) else 'preflight_not_verified'}

    async def reconcile(self, effect_id):
        effect = self._effect(effect_id)
        if effect['status'] in {'confirmed','no_dispatch','conflict'}:
            return {'status':effect['status'], 'effect_id':effect_id, 'remote_id':effect.get('remote_id'), 'duplicate':True}
        _require('dispatch' in effect, 'dispatch_intent_required')
        proposal = effect['proposal']
        try:
            await self.transport._effect_prepare(proposal['account'])
            remote = effect.get('remote_id')
            draft = proposal['action'] == 'draft_create'
            if not remote:
                value, _ = await self._read('draft_search' if draft else 'message_search', message_id=proposal['payload']['message_id'])
                matches = value.get('drafts' if draft else 'messages', [])
                _require(not value.get('nextPageToken') and isinstance(matches,list) and len(matches) == 1, 'search_not_unique')
                remote = matches[0].get('id')
            _require(_identity(remote), 'remote_identity_invalid')
            value, response = await self._read('draft' if draft else 'message', identity=remote)
            _require(value.get('id') == remote, 'readback_identity_mismatch')
            message = value.get('message') if draft else value
            _require(isinstance(message,dict) and _identity(message.get('id')) and _identity(message.get('threadId')), 'readback_message_identity_missing')
            _require(('DRAFT' if draft else 'SENT') in message.get('labelIds', []), 'readback_action_not_verified')
            if proposal['payload'].get('thread_id'):
                _require(message['threadId'] == proposal['payload']['thread_id'], 'readback_thread_mismatch')
            encoded = message.get('raw')
            _require(isinstance(encoded,str), 'readback_raw_missing')
            raw = base64.b64decode(encoded + '=' * (-len(encoded)%4), altchars=b'-_', validate=True)
            comparison = compare_mime(proposal['payload']['mime'].encode('utf-8'), raw)
            mime = inspect_mime(proposal['payload']['mime'], proposal['payload']['message_id'])
            reference = self._evidence(effect, 'readback', response, remote_id=remote, thread_id=message['threadId'],
                comparison=comparison, mime_sha256=mime['sha256'], recipients_sha256=_hash(json.dumps(mime['addresses'],sort_keys=True).encode()))
            envelope = self._envelope(effect)
            result = self.effects.observe(effect_id, {**envelope, 'status':'confirmed', 'remote_id':remote,
                'evidence_reference':reference, 'readback':{**envelope,'remote_id':remote,'content_verified':True,
                    'fixed_identity':proposal['payload']['message_id'], 'thread_id':message['threadId'], 'mime_sha256':mime['sha256'], 'comparison':comparison}})
            return {**result, 'remote_id':remote, 'thread_id':message['threadId'], 'evidence_reference':reference}
        except Exception:
            return self._uncertain(effect, 'reconciliation_not_verified')
