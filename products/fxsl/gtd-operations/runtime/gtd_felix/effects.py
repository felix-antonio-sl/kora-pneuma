"""Durable external-effect authorization. No provider I/O or public dispatcher.

Only trusted adapters call begin_dispatch/observe. They must never infer permission
from a source body, retry an existing intent, or claim CAS for Gmail draft updates.
"""
import copy
from datetime import datetime, timezone
from email import policy
from email.parser import Parser
import hashlib
import json
import math
import uuid


ACTIONS = {'gmail': {'draft_create', 'draft_update', 'send'},
           'calendar': {'insert', 'update', 'decline', 'delete_copy', 'cancel_event'}}
UNRESOLVED = {'dispatching', 'uncertain', 'acknowledged'}
MAX_BYTES = 65536


def _now():
    return datetime.now(timezone.utc)


def _text(value):
    return isinstance(value, str) and bool(value.strip()) and len(value) <= 1024


def _instant(value):
    if not isinstance(value, str):
        raise ValueError('expiry_with_timezone_required')
    try:
        result = datetime.fromisoformat(value)
    except ValueError as exc:
        raise ValueError('expiry_with_timezone_required') from exc
    if result.tzinfo is None:
        raise ValueError('expiry_with_timezone_required')
    return result


def _json(value):
    # Validate depth/size before serialization; no arbitrary Python objects.
    count = 0
    def walk(node, depth=0):
        nonlocal count
        count += 1
        if depth > 12 or count > 4096:
            raise ValueError('payload_too_complex')
        if isinstance(node, dict):
            if not all(isinstance(k, str) for k in node):
                raise ValueError('invalid_json')
            for k, v in node.items():
                if len(k) > MAX_BYTES:
                    raise ValueError('payload_too_large')
                walk(v, depth + 1)
        elif isinstance(node, list):
            for child in node:
                walk(child, depth + 1)
        elif isinstance(node, str):
            if len(node) > MAX_BYTES:
                raise ValueError('payload_too_large')
        elif node is not None and type(node) not in {bool, int, float}:
            raise ValueError('invalid_json')
        elif type(node) is float and not math.isfinite(node):
            raise ValueError('invalid_json')
        elif type(node) is int and node.bit_length() > 128:
            raise ValueError('invalid_json')
    walk(value)
    result = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()
    if len(result) > MAX_BYTES:
        raise ValueError('payload_too_large')
    return result


def _hash(value):
    return hashlib.sha256(_json(value)).hexdigest()


class ExternalEffects:
    KEY = 'effects:state'
    # Source meaning is augmented with scheduling/position fields relevant to effects.
    POSITION = {'parent_id', 'status', 'due_at', 'review_at', 'decision_at', 'starts_at',
                'ends_at', 'timezone', 'decision_needed', 'decision_question', 'waiting_for', 'context'}

    def __init__(self, service):
        self.service, self.store = service, service.store

    def _load(self):
        return self.service._meta(self.KEY, {'effects': {}, 'grants': {}, 'operations': {}})

    def _save(self, state):
        self.service._set_meta(self.KEY, state)

    def _role(self, actor, owner=False):
        role = self.service.actor_role(actor)
        if role not in ({'owner'} if owner else {'owner', 'principal'}):
            raise ValueError('owner_required' if owner else 'actor_forbidden')
        return role

    def _operation(self, actor, operation_id, kind, arguments, apply, owner=False):
        try:
            self._role(actor, owner)
            if not _text(operation_id):
                raise ValueError('operation_id_required')
            fingerprint = _hash([actor, kind, arguments])
        except (ValueError, TypeError) as error:
            return {'status': 'rejected', 'error': str(error)}
        with self.store.transaction():
            state = self._load()
            previous = state['operations'].get(operation_id)
            if previous:
                if previous['fingerprint'] != fingerprint:
                    return {'status': 'rejected', 'error': 'operation_id_conflict'}
                return {**copy.deepcopy(previous['receipt']), 'duplicate': True}
            try:
                receipt = apply(state)
            except (ValueError, KeyError, TypeError) as error:
                receipt = {'status': 'rejected', 'error': str(error)}
            state['operations'][operation_id] = {'fingerprint': fingerprint, 'actor': actor,
                                                'kind': kind, 'receipt': receipt}
            self._save(state)
            return copy.deepcopy(receipt)

    def _basis(self, item_id):
        item, versions = self.service._item(item_id)
        if not item:
            raise ValueError('item_not_found')
        return {'meaning': self.service._basis(item_id),
                'position': {k: item.get(k) for k in self.POSITION},
                'generations': {k: v['version'] for k, v in versions.items() if k in self.POSITION}}

    def _dependencies(self, proposal):
        dependencies = set(proposal.get('source_versions', {})) | {proposal['item_id']}
        item = self.service.get_item(proposal['item_id'])
        if not item:
            raise ValueError('item_not_found')
        visited = set()
        while item:
            if item['id'] in visited:
                raise ValueError('invalid_ancestry')
            visited.add(item['id'])
            dependencies.add(item['id'])
            dependencies.update(item.get('source_versions', {}))
            parent = item.get('parent_id')
            item = self.service.get_item(parent) if parent else None
            if parent and not item:
                raise ValueError('item_not_found')
        if proposal.get('material'):
            material = self._material(proposal)
            dependencies.update(material.get('basis', {}))
            dependencies.update(material.get('source_versions', {}))
        return dependencies

    def _material(self, proposal):
        expected = proposal['material']
        if (not isinstance(expected, dict) or set(expected) != {'id', 'version', 'sha256'}
                or not _text(expected.get('id')) or type(expected.get('version')) is not int):
            raise ValueError('invalid_material_reference')
        material = next((m for m in self.service.materials(proposal['item_id'])
            if m['id'] == expected['id'] and m['version'] == expected['version']), None)
        if not material or not material['valid'] or material['original']['sha256'] != expected['sha256']:
            raise ValueError('material_not_current')
        content = self.service.read_material(proposal['item_id'], expected['id'], expected['version'])
        if content['sha256'] != expected['sha256']:
            raise ValueError('material_hash_mismatch')
        if proposal['provider'] == 'gmail' and proposal['payload'].get('mime') != content['content']:
            raise ValueError('mime_material_mismatch')
        return material

    def _validate_proposal(self, proposal):
        required = {'provider', 'account', 'action', 'item_id', 'target', 'payload', 'expires_at'}
        if not isinstance(proposal, dict) or not required.issubset(proposal) or set(proposal) - required - {'material', 'expected_remote_version', 'source_versions'}:
            raise ValueError('invalid_proposal')
        _json(proposal)
        provider, action = proposal['provider'], proposal['action']
        if provider not in ACTIONS or action not in ACTIONS[provider]:
            raise ValueError('unsupported_effect')
        if not _text(proposal['account']) or not _text(proposal['item_id']):
            raise ValueError('invalid_destination')
        if not isinstance(proposal['target'], dict) or set(proposal['target']) != {'id'}:
            raise ValueError('invalid_target')
        target = proposal['target']['id']
        if target is not None and not _text(target):
            raise ValueError('invalid_target')
        modifying = action in {'draft_update', 'update', 'decline', 'delete_copy', 'cancel_event'}
        if modifying and (target is None or not _text(proposal.get('expected_remote_version'))):
            raise ValueError('remote_version_required')
        if action in {'draft_create', 'send'} and target is not None:
            raise ValueError('new_message_required')
        if not isinstance(proposal['payload'], dict):
            raise ValueError('invalid_payload')
        if _instant(proposal['expires_at']) <= _now():
            raise ValueError('proposal_expired')
        sources = proposal.get('source_versions', {})
        if not isinstance(sources, dict) or any(not _text(k) or type(v) is not int or v < 1 for k, v in sources.items()):
            raise ValueError('invalid_source_versions')
        for item_id, version in sources.items():
            if self.service._basis(item_id)['source_revision'] != version:
                raise ValueError('source_version_stale')
        if provider == 'gmail':
            payload = proposal['payload']
            if set(payload) - {'mime', 'message_id', 'thread_id'} or not _text(payload.get('message_id')) or not isinstance(payload.get('mime'), str):
                raise ValueError('immutable_mime_required')
            if 'thread_id' in payload and not _text(payload['thread_id']):
                raise ValueError('invalid_thread_id')
            headers = Parser(policy=policy.default).parsestr(payload['mime'], headersonly=True)
            if headers.get_all('Message-ID') != [payload['message_id']]:
                raise ValueError('message_identity_mismatch')
            if not proposal.get('material'):
                raise ValueError('material_required')
        if proposal.get('material'):
            self._material(proposal)

    def propose(self, actor, operation_id, proposal):
        """Persist an immutable exact proposal; never grant permission or dispatch.

        Gmail payload = {mime, message_id, thread_id?}, MIME equals current material
        bytes. send means messages.send of that MIME, never draft.send. Modifications
        require expected_remote_version. The adapter must read and compare that version
        before the write; Gmail draft updates have no native CAS, so comparison is
        not an atomic concurrency guarantee. No version is inferred here.
        """
        def apply(state):
            self._validate_proposal(proposal)
            bases = {identity: self._basis(identity) for identity in sorted(self._dependencies(proposal))}
            identity = uuid.uuid4().hex
            frozen = {'proposal': copy.deepcopy(proposal), 'bases': bases, 'proposed_by': actor}
            effect = {**frozen, 'id': identity, 'proposal_hash': _hash(frozen), 'status': 'proposed',
                      'created_at': _now().isoformat(), 'observations': [], 'revoked': False}
            state['effects'][identity] = effect
            return {'status': 'proposed', 'effect': effect}
        return self._operation(actor, operation_id, 'propose', proposal, apply)

    def _fresh(self, effect):
        if self.service.recovery_required:
            raise ValueError('recovery_required')
        self._role(effect['proposed_by'])
        frozen = {k: effect[k] for k in ('proposal', 'bases', 'proposed_by')}
        if _hash(frozen) != effect['proposal_hash']:
            raise ValueError('proposal_hash_mismatch')
        self._validate_proposal(effect['proposal'])
        if set(effect['bases']) != self._dependencies(effect['proposal']):
            raise ValueError('source_basis_changed')
        if any(self._basis(identity) != basis for identity, basis in effect['bases'].items()):
            raise ValueError('source_basis_changed')

    def authorize(self, owner, operation_id, effect_id, expected_proposal_hash):
        def apply(state):
            effect = state['effects'][effect_id]
            if effect['proposal_hash'] != expected_proposal_hash:
                raise ValueError('proposal_hash_mismatch')
            if effect['status'] != 'proposed' or effect['revoked']:
                raise ValueError('effect_not_authorizable')
            self._fresh(effect)
            effect['authorization'] = {'owner': owner, 'proposal_hash': expected_proposal_hash,
                                       'operation_id': operation_id, 'authorized_at': _now().isoformat()}
            effect['status'] = 'authorized'
            return {'status': 'authorized', 'effect_id': effect_id, 'proposal_hash': expected_proposal_hash}
        return self._operation(owner, operation_id, 'authorize', [effect_id, expected_proposal_hash], apply, owner=True)

    def grant_draft_preparation(self, owner, operation_id, account, actor, expires_at):
        def apply(state):
            if not _text(account) or self.service.actor_role(actor) != 'principal' or _instant(expires_at) <= _now():
                raise ValueError('invalid_draft_grant')
            grant = {'id': uuid.uuid4().hex, 'account': account, 'actor': actor, 'expires_at': expires_at,
                     'owner': owner, 'status': 'active', 'created_at': _now().isoformat()}
            state['grants'][grant['id']] = grant
            return {'status': 'granted', 'grant': grant}
        return self._operation(owner, operation_id, 'grant_draft_preparation', [account, actor, expires_at], apply, owner=True)

    def revoke(self, owner, operation_id, *, effect_id=None, grant_id=None):
        def apply(state):
            if bool(effect_id) == bool(grant_id):
                raise ValueError('one_revocation_target_required')
            if grant_id:
                state['grants'][grant_id]['status'] = 'revoked'
                affected = [e for e in state['effects'].values() if e.get('dispatch', {}).get('grant_id') == grant_id]
            else:
                affected = [state['effects'][effect_id]]
            for effect in affected:
                effect['revoked'] = True
                effect['revoked_at'] = _now().isoformat()
                if 'dispatch' not in effect:
                    effect['status'] = 'revoked'
            return {'status': 'revoked', 'effect_id': effect_id, 'grant_id': grant_id}
        return self._operation(owner, operation_id, 'revoke', [effect_id, grant_id], apply, owner=True)

    def _authority(self, state, effect):
        if effect['revoked']:
            raise ValueError('effect_revoked')
        auth = effect.get('authorization')
        if auth and auth['proposal_hash'] == effect['proposal_hash'] and self.service.actor_role(auth['owner']) == 'owner':
            return {'owner': auth['owner'], 'authorization_operation': auth['operation_id']}
        p = effect['proposal']
        if p['provider'] == 'gmail' and p['action'] in {'draft_create', 'draft_update'}:
            for grant in state['grants'].values():
                if (grant['status'] == 'active' and grant['account'] == p['account'] and grant['actor'] == effect['proposed_by']
                        and self.service.actor_role(grant['owner']) == 'owner' and self.service.actor_role(grant['actor']) == 'principal'
                        and _instant(grant['expires_at']) > _now()):
                    return {'owner': grant['owner'], 'grant_id': grant['id']}
        raise ValueError('external_authorization_required')

    def readiness(self, effect_id):
        """Trusted, read-only preflight gate. It never grants provider I/O.

        An existing dispatch must only be reconciled, including during recovery;
        begin_dispatch remains the final transactional gate for a first write.
        """
        with self.store.lock:
            state = self._load()
            effect = state['effects'].get(effect_id)
            if not effect:
                return {'ready': False, 'reason': 'effect_not_found', 'state': None}
            if 'dispatch' in effect:
                return {'ready': False, 'reason': 'already_dispatched', 'state': effect['status']}
            if effect['status'] not in {'proposed', 'authorized'}:
                return {'ready': False, 'reason': 'effect_resolved', 'state': effect['status']}
            try:
                self._fresh(effect)
                self._authority(state, effect)
            except (ValueError, KeyError, TypeError) as error:
                return {'ready': False, 'reason': str(error), 'state': effect['status']}
            return {'ready': True, 'reason': None, 'state': effect['status']}

    def begin_dispatch(self, effect_id):
        """Trusted adapter only: status=dispatch is the ONE permission for provider I/O.

        Every subsequent invocation returns already_dispatched/resolved, never a
        second permission. Crash after this commit must reconcile, not resend.
        """
        with self.store.transaction():
            state = self._load()
            effect = state['effects'].get(effect_id)
            if not effect:
                return {'status': 'rejected', 'error': 'effect_not_found'}
            if 'dispatch' in effect:
                return {'status': 'already_dispatched', 'effect_id': effect_id, 'state': effect['status']}
            if effect['status'] not in {'proposed', 'authorized'}:
                return {'status': 'rejected', 'error': 'effect_resolved'}
            try:
                self._fresh(effect)
                authority = self._authority(state, effect)
            except (ValueError, KeyError, TypeError) as error:
                reason = str(error)
                if reason not in {'recovery_required', 'external_authorization_required'}:
                    effect['status'], effect['error'] = 'conflict', reason
                    self._save(state)
                return {'status': 'rejected', 'error': reason}
            effect['dispatch'] = {**authority, 'id': uuid.uuid4().hex, 'started_at': _now().isoformat(),
                                  'request_hash': effect['proposal_hash']}
            effect['status'] = 'dispatching'
            self._save(state)
            return {'status': 'dispatch', 'effect': copy.deepcopy(effect)}

    def observe(self, effect_id, observation):
        """Trusted provider adapter evidence; no public HTTP/MCP binding.

        Exact envelope: provider/account/action/target/request_hash/status. ACK is
        insufficient. confirmed also requires evidence_reference and readback with
        the same envelope plus remote_id and content_verified=True. Lost ACK can be
        reconciled by fixed_identity: Gmail Message-ID or Calendar client event ID;
        the driver must verify exact MIME/recipients or event payload, not just a hit.
        conflict accepts only Calendar conditional rejection 412 proof tied to
        dispatch_id and approved expected_remote_version, without prior ACK.
        no_dispatch requires proof={kind:request_not_sent, dispatch_id:...}; a local
        adapter must KNOW no write request left, never infer this from a 404/search.
        """
        with self.store.transaction():
            state = self._load()
            effect = state['effects'].get(effect_id)
            try:
                if not effect or 'dispatch' not in effect:
                    raise ValueError('dispatch_intent_required')
                if not isinstance(observation, dict):
                    raise ValueError('invalid_observation')
                _json(observation)
                if observation in effect['observations']:
                    return {'status': effect['status'], 'duplicate': True}
                if effect['status'] not in UNRESOLVED:
                    raise ValueError('effect_already_resolved')
                p = effect['proposal']
                envelope = {k: p[k] for k in ('provider', 'account', 'action', 'target')}
                envelope['request_hash'] = effect['proposal_hash']
                if any(observation.get(k) != v for k, v in envelope.items()):
                    raise ValueError('observation_destination_mismatch')
                status = observation.get('status')
                if status not in {'ack', 'uncertain', 'confirmed', 'no_dispatch', 'conflict'}:
                    raise ValueError('invalid_observation_status')
                if status != 'uncertain' and not _text(observation.get('evidence_reference')):
                    raise ValueError('evidence_required')
                if status in {'ack', 'confirmed'}:
                    remote_id = observation.get('remote_id')
                    if not _text(remote_id) or (effect.get('remote_id') and remote_id != effect['remote_id']):
                        raise ValueError('remote_identity_mismatch')
                    if p['target']['id'] is not None and remote_id != p['target']['id']:
                        raise ValueError('remote_identity_mismatch')
                if status == 'confirmed':
                    readback = observation.get('readback', {})
                    if (not isinstance(readback, dict) or any(readback.get(k) != v for k, v in envelope.items())
                            or readback.get('remote_id') != remote_id or readback.get('content_verified') is not True):
                        raise ValueError('exact_readback_required')
                    if not effect.get('remote_id'):
                        fixed = p['payload'].get('message_id') if p['provider'] == 'gmail' else p['target']['id']
                        if not fixed or readback.get('fixed_identity') != fixed:
                            raise ValueError('fixed_identity_required_without_ack')
                if status == 'conflict':
                    proof = observation.get('proof')
                    expected = {'kind': 'conditional_write_rejected', 'http_status': 412,
                                'dispatch_id': effect['dispatch']['id'],
                                'expected_remote_version': p.get('expected_remote_version')}
                    if (p['provider'] != 'calendar' or p['action'] not in {'update', 'decline', 'delete_copy', 'cancel_event'}
                            or not p.get('expected_remote_version') or effect.get('remote_id') or proof != expected):
                        raise ValueError('conditional_rejection_not_proven')
                if status == 'no_dispatch':
                    if effect.get('remote_id') or observation.get('proof') != {'kind': 'request_not_sent', 'dispatch_id': effect['dispatch']['id']}:
                        raise ValueError('no_dispatch_not_proven')
                effect['observations'].append(copy.deepcopy(observation))
                effect['status'] = {'ack': 'acknowledged'}.get(status, status)
                if status in {'ack', 'confirmed'}:
                    effect['remote_id'] = remote_id
                self._save(state)
                return {'status': effect['status'], 'effect_id': effect_id}
            except (ValueError, KeyError, TypeError) as error:
                return {'status': 'rejected', 'error': str(error)}

    def get(self, actor, effect_id):
        with self.store.lock:
            self._role(actor)
            effect = self._load()['effects'].get(effect_id)
            if not effect or self.service.actor_role(actor) != 'owner' and effect['proposed_by'] != actor:
                return None
            return copy.deepcopy(effect)

    def list(self, actor):
        with self.store.lock:
            role = self._role(actor)
            return [copy.deepcopy(e) for e in self._load()['effects'].values() if role == 'owner' or e['proposed_by'] == actor]

    def pending(self):
        """Internal recovery seam: unresolved I/O only, not unapproved proposals."""
        with self.store.lock:
            return [copy.deepcopy(e) for e in self._load()['effects'].values() if e['status'] in UNRESOLVED]
