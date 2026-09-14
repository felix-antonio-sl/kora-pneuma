"""Provider-neutral durable source intake; no transport or external authority.

Callers authenticate provider/account/scope and supply opaque ordered revisions.
Collection is a stable namespace (messages/calendar ID), never a filter.
Object identity excludes scope_digest; coverage and cursors include it.
One active pagination chain per exact partition. The Store's writer ownership
contract still applies; no network call belongs inside this engine.
"""
import copy
from datetime import datetime, timezone
import hashlib
import json
import re
from urllib.parse import urlsplit

from .source_entries import report_intake, report_projection


def _now():
    return datetime.now(timezone.utc).isoformat()


def _json(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False)


def _hash(value):
    return hashlib.sha256(_json(value).encode()).hexdigest()


def _require(value, error):
    if not value:
        raise ValueError(error)


def _token(value):
    return isinstance(value, str) and bool(value) and len(value) <= 8192


class SourceSync:
    """begin/apply_page/recover never interpret source content as a mandate."""
    PREFIX = 'source-sync:'
    PARTITION_FIELDS = {'provider', 'account', 'collection', 'scope_digest'}

    def __init__(self, service):
        self.service, self.store = service, service.store

    def _key(self, partition):
        _require(isinstance(partition, dict) and set(partition) == self.PARTITION_FIELDS,
                 'invalid_partition')
        _require(all(_token(v) for v in partition.values()), 'invalid_partition')
        _require(re.fullmatch(r'[a-f0-9]{64}', partition['scope_digest']), 'invalid_scope_digest')
        _require(partition['provider'] not in {'local', 'human', 'owner'}, 'external_provider_required')
        return self.PREFIX + _hash(partition)

    def _object_key(self, partition, external_id):
        return self.PREFIX + 'object:' + _hash([partition[k] for k in ('provider', 'account', 'collection')] + [external_id])

    def _load(self, key):
        row = self.store.db.execute('SELECT value FROM metadata WHERE key=?', (key,)).fetchone()
        return json.loads(row[0]) if row else None

    def _save(self, key, state):
        self.store.db.execute('INSERT INTO metadata VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value',
                              (key, _json(state)))

    def inspect(self, partition):
        with self.store.lock:
            state = self._load(self._key(partition))
            if state:
                for record in state['objects'].values():
                    record['item_id'] = self._load(record['index_key'])['item_id']
            return copy.deepcopy(state)

    def begin(self, partition, cycle_id, mode='full'):
        key = self._key(partition)
        _require(_token(cycle_id) and mode in {'full', 'incremental', 'rebuild'}, 'invalid_cycle')
        with self.store.transaction():
            state = self._load(key) or {'partition': copy.deepcopy(partition), 'cursor': None,
                'cursor_valid': False, 'coverage': 'not_started', 'projection': 'current', 'semantic_review': 'not_evaluated',
                'objects': {}, 'pending': [], 'cycles': {}, 'active_cycle': None}
            if cycle_id in state['cycles']:
                cycle = state['cycles'][cycle_id]
                _require(cycle['mode'] == mode, 'cycle_id_reused')
                return copy.deepcopy(cycle)
            _require(state['active_cycle'] is None, 'cycle_in_progress')
            _require(not state['pending'], 'projection_recovery_required')
            _require(mode != 'incremental' or state['cursor'] is not None
                     and state['cursor_valid'], 'full_or_rebuild_required')
            cycle = {'id': cycle_id, 'mode': mode, 'status': 'active',
                'base_cursor': state['cursor'] if mode == 'incremental' else None,
                'next_page_token': None, 'candidate_cursor': None, 'pages': {}, 'seen': [],
                'final_page': False, 'started_at': _now(), 'coverage_completed_at': None,
                'projection_completed_at': None}
            state['cycles'][cycle_id] = cycle
            state.update(active_cycle=cycle_id, coverage='in_progress', coverage_started_at=cycle['started_at'])
            self._save(key, state)
            return copy.deepcopy(cycle)

    def _object(self, value):
        required = {'external_id', 'revision', 'status', 'text', 'original', 'sha256', 'url'}
        _require(isinstance(value, dict) and required <= set(value)
                 and not set(value) - required - {'mime_type'}, 'invalid_external_object')
        _require(_token(value['external_id']) and _token(value['revision']), 'stable_identity_required')
        _require(value['status'] in {'present', 'deleted', 'degraded'}, 'invalid_external_status')
        missing_content = value['status'] in {'deleted', 'degraded'} and value['original'] is None
        _require(isinstance(value['text'], str) or missing_content and value['text'] is None, 'invalid_source_content')
        if missing_content:
            _require(value['sha256'] is None and value['text'] is None, 'tombstone_content_mismatch')
        else:
            _require(isinstance(value['original'], bytes), 'invalid_source_content')
            _require(len(value['original']) <= 4 * 1024 * 1024 and len(value['text']) <= 1024 * 1024,
                     'source_too_large')
            _require(hashlib.sha256(value['original']).hexdigest() == value['sha256'], 'source_hash_mismatch')
        url = value['url']
        _require(isinstance(url, str), 'invalid_source_url')
        parsed = urlsplit(url)
        _require(parsed.scheme in {'http', 'https'} and parsed.netloc and not parsed.username
                 and not parsed.password, 'invalid_source_url')
        mime = value.get('mime_type', 'application/octet-stream')
        _require(isinstance(mime, str) and bool(mime), 'invalid_mime_type')
        return {k: copy.deepcopy(v) for k, v in value.items() if k != 'original'} | {'mime_type': mime}

    def _queue(self, state, partition, external, document, signature, original, observed_at):
        index_key = self._object_key(partition, external)
        record = self._load(index_key) or {'external_id': external, 'item_id': None,
            'versions': [], 'revision_hashes': {}, 'availability': 'unknown'}
        event = next((v for v in record['versions'] if v['signature'] == signature), None)
        if event is None:
            event = {'sequence': len(record['versions']) + 1, 'signature': signature,
                'document': copy.deepcopy(document), 'original': original, 'projection': 'pending',
                'observed_at': observed_at, 'partition': copy.deepcopy(partition)}
            event['operation_id'] = self.PREFIX + _hash([index_key, event['sequence']])
            record['versions'].append(event)
            # Queryable intake authority mirrors every new revision; a prior
            # selection decision for the same revision is never downgraded.
            report_intake(self.store, provider=partition['provider'], account=partition['account'],
                collection=partition['collection'],
                external_id=external, revision=document['revision'],
                availability=document['status'],
                original_digest=original['sha256'] if original else None,
                index_key=index_key, sequence=event['sequence'], observed_at=observed_at)
            record['revision_hashes'][document['revision']] = signature
            record['availability'] = document['status']
            self._save(index_key, record)
        state['objects'][external] = {'external_id': external, 'item_id': record['item_id'],
            'index_key': index_key, 'availability': document['status'], 'revision': document['revision'],
            'observed_at': observed_at}
        pending = {'external_id': external, 'sequence': event['sequence']}
        if pending not in state['pending']:
            state['pending'].append(pending)
        state.update(projection='pending', projection_pending_at=observed_at)

    def apply_page(self, partition, cycle_id, page):
        key = self._key(partition)
        _require(isinstance(page, dict) and set(page) == {'page_id', 'request_token', 'next_page_token', 'cursor', 'objects'},
                 'invalid_page')
        _require(_token(page['page_id']) and isinstance(page['objects'], list) and len(page['objects']) <= 1000,
                 'invalid_page')
        for field in ('request_token', 'next_page_token', 'cursor'):
            _require(page[field] is None or _token(page[field]), 'invalid_page_token')
        final = page['next_page_token'] is None
        _require((final and page['cursor'] is not None) or (not final and page['cursor'] is None),
                 'final_cursor_required')
        documents = [self._object(value) for value in page['objects']]
        page_hash = _hash({**page, 'objects': documents})
        with self.store.lock:
            with self.store.transaction():
                state = self._load(key)
                _require(state is not None and cycle_id in state['cycles'], 'unknown_cycle')
                cycle = state['cycles'][cycle_id]
                _require(cycle['status'] in {'active', 'complete'} and state['active_cycle'] in {None, cycle_id}, 'cycle_not_active')
                if page['page_id'] in cycle['pages']:
                    _require(cycle['pages'][page['page_id']]['sha256'] == page_hash, 'page_id_reused')
                else:
                    _require(state['active_cycle'] == cycle_id and cycle['status'] == 'active'
                             and not cycle['final_page'], 'cycle_not_active')
                    _require(page['request_token'] == cycle['next_page_token'], 'unexpected_page_token')
                    used = [p['request_token'] for p in cycle['pages'].values()]
                    _require(not page['next_page_token'] or page['next_page_token'] not in used + [page['request_token']],
                             'page_token_cycle')
                    observed_at = _now()
                    for value, document in zip(page['objects'], documents):
                        external = document['external_id']
                        record = self._load(self._object_key(partition, external))
                        signature = _hash(document)
                        known = record['revision_hashes'].get(document['revision']) if record else None
                        _require(known is None or known == signature, 'revision_content_conflict')
                        blob = None
                        if value['original'] is not None:
                            blob = self.store.save_original(value['original'])
                            self.store.db.execute('INSERT OR IGNORE INTO originals VALUES(?,?,?)',
                                                  (blob['sha256'], blob['size'], blob['path']))
                        self._queue(state, partition, external, document, signature, blob, observed_at)
                        if external not in cycle['seen']:
                            cycle['seen'].append(external)
                    cycle['pages'][page['page_id']] = {'sha256': page_hash, 'received_at': observed_at,
                        'request_token': page['request_token'], 'next_page_token': page['next_page_token']}
                    cycle.update(next_page_token=page['next_page_token'], candidate_cursor=page['cursor'], final_page=final)
                    if final:
                        cycle['coverage_completed_at'] = observed_at
                        state.update(coverage='complete', coverage_completed_at=observed_at)
                    if final and cycle['mode'] in {'full', 'rebuild'}:
                        for external, record in list(state['objects'].items()):
                            if external not in cycle['seen'] and record['availability'] not in {'absent', 'deleted'}:
                                # Absence is scoped coverage evidence, not global deletion.
                                record.update(availability='absent', absence_cycle=cycle_id, absent_at=observed_at)
                    self._save(key, state)
            return self.recover(partition)

    def _project(self, record, event):
        document, partition = event['document'], event['partition']
        source = {**partition, **{k: document[k] for k in ('external_id', 'revision', 'url', 'sha256')},
                  'availability': document['status'], 'partition_key': self._key(partition),
                  'observed_at': event['observed_at']}
        blob = event['original']
        content = (self.store.root / blob['path']).read_bytes() if blob else None
        if content is not None:
            _require(hashlib.sha256(content).hexdigest() == blob['sha256'], 'stored_original_corrupt')
        if record['item_id'] is None and document['status'] != 'present':
            return {'status': 'not_needed'}
        if record['item_id'] is None:
            return self.service.capture(self.service.principal_actor, event['operation_id'],
                document['text'], source=source, original=content, filename='source.bin',
                mime_type=document['mime_type'])
        return self.service.revise_source(self.service.principal_actor, event['operation_id'],
            record['item_id'], source, text=document['text'] if blob else None,
            original=content, filename='source.bin' if blob else None,
            mime_type=document['mime_type'] if blob else None)

    def recover(self, partition):
        key = self._key(partition)
        with self.store.lock:
            state = self._load(key)
            _require(state is not None, 'unknown_partition')
            had_pending = bool(state['pending'])
            while state['pending']:
                pending = state['pending'][0]
                local = state['objects'][pending['external_id']]
                record = self._load(local['index_key'])
                # Another scope may recover this same durable first capture. Always
                # resolve earlier object revisions before this partition's revision.
                for event in record['versions'][:pending['sequence']]:
                    if event['projection'] != 'pending':
                        continue
                    result = self._project(record, event)
                    if result.get('status') not in {'applied', 'already_applied', 'not_needed'}:
                        state.update(projection='blocked', projection_failed_at=_now(),
                                     projection_error=result.get('error', 'projection_uncertain'))
                        with self.store.transaction():
                            self._save(key, state)
                        return copy.deepcopy(state)
                    if result['status'] != 'not_needed':
                        record['item_id'] = result['item']['id']
                    event.update(projection='not_needed' if result['status'] == 'not_needed' else 'applied',
                                 item_id=record['item_id'], projected_at=_now())
                    # Upsert first: rows for events written before the I3
                    # cut (or its migration) must not break projection.
                    report_intake(self.store, provider=event['partition']['provider'],
                        account=event['partition']['account'],
                        collection=event['partition']['collection'],
                        external_id=pending['external_id'],
                        revision=event['document']['revision'],
                        availability='present' if event['document']['status'] == 'present'
                        else event['document']['status'],
                        original_digest=(event['original'] or {}).get('sha256'),
                        index_key=local['index_key'], sequence=event['sequence'],
                        observed_at=event['observed_at'])
                    report_projection(self.store, provider=event['partition']['provider'],
                        account=event['partition']['account'],
                        collection=event['partition']['collection'],
                        external_id=pending['external_id'],
                        revision=event['document']['revision'],
                        item_id=record['item_id'] if result['status'] != 'not_needed' else None,
                        projected=result['status'] != 'not_needed')
                    with self.store.transaction():
                        self._save(local['index_key'], record)
                local['item_id'] = record['item_id']
                state['pending'].pop(0)
                with self.store.transaction():
                    self._save(key, state)
            state['projection'] = 'current'
            state.pop('projection_error', None)
            cycle_id = state['active_cycle']
            if had_pending:
                state['projection_completed_at'] = _now()
            if cycle_id is not None:
                cycle = state['cycles'][cycle_id]
                if cycle['final_page']:
                    stamp = _now()
                    cycle.update(status='complete', projection_completed_at=stamp)
                    state.update(cursor=cycle['candidate_cursor'], cursor_valid=True, active_cycle=None,
                                 coverage='complete', projection_completed_at=stamp)
            with self.store.transaction():
                self._save(key, state)
            return copy.deepcopy(state)

    def invalidate_cursor(self, partition, cycle_id):
        return self.degrade(partition, cycle_id, 'cursor_expired', rebuild=True)

    def degrade(self, partition, cycle_id, reason, *, rebuild=False):
        key = self._key(partition)
        _require(_token(reason), 'degradation_reason_required')
        with self.store.transaction():
            state = self._load(key)
            _require(state is not None and state['active_cycle'] == cycle_id, 'cycle_not_active')
            stamp = _now()
            state['cycles'][cycle_id].update(status='invalidated' if rebuild else 'degraded', reason=reason, degraded_at=stamp)
            state.update(active_cycle=None, coverage='rebuild_required' if rebuild else 'degraded', degraded_at=stamp)
            if rebuild:
                state['cursor_valid'] = False
            self._save(key, state)
            return copy.deepcopy(state)
