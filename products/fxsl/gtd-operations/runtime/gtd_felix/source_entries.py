"""Single reader/writer for the source_entries authority (I3).

One row per (provider, account, external_id, revision): intake state plus
selection decision, queryable without decoding metadata blobs. The engine
(SourceSync) reports intake/projection; selection paths report decisions.
"""
import hashlib
import json
from datetime import datetime, timezone

STATUSES = frozenset({'pending', 'selected', 'noise', 'uncertain', 'unavailable', 'deleted'})
INTAKE_STATUS = {'present': 'pending', 'deleted': 'deleted', 'degraded': 'unavailable'}


def entry_id(provider, account, external_id, revision):
    return hashlib.sha256('|'.join(
        [provider, account, external_id, revision]).encode()).hexdigest()


def _now():
    return datetime.now(timezone.utc).isoformat()


def _meta(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))


def report_intake(store, *, provider, account, external_id, revision, availability,
                  original_digest, index_key, sequence, observed_at=None):
    """Upsert on first sight of a revision; never downgrades a decided status."""
    if availability not in INTAKE_STATUS:
        raise ValueError('invalid_availability')
    with store.lock:
        row = store.db.execute(
            'SELECT status FROM source_entries WHERE id=?',
            (entry_id(provider, account, external_id, revision),)).fetchone()
        if row is not None:
            return row['status']
        store.db.execute(
            'INSERT INTO source_entries(id, provider, account, external_id, revision,'
            ' status, original_digest, item_id, metadata_json, observed_at)'
            ' VALUES(?,?,?,?,?,?,?,?,?,?)',
            (entry_id(provider, account, external_id, revision), provider, account,
             external_id, revision, INTAKE_STATUS[availability], original_digest, None,
             _meta({'index_key': index_key, 'sequence': sequence,
                    'availability': availability, 'projection': 'pending'}),
             observed_at or _now()))
        return INTAKE_STATUS[availability]


def report_projection(store, *, provider, account, external_id, revision,
                      item_id=None, projected=True):
    """Link the projected affair (or its deliberate absence) to the revision."""
    with store.lock:
        row = store.db.execute(
            'SELECT metadata_json FROM source_entries WHERE id=?',
            (entry_id(provider, account, external_id, revision),)).fetchone()
        if row is None:
            raise ValueError('unknown_source_revision')
        metadata = json.loads(row['metadata_json'])
        metadata['projection'] = 'applied' if projected else 'not_needed'
        store.db.execute(
            'UPDATE source_entries SET item_id=?, metadata_json=? WHERE id=?',
            (item_id, _meta(metadata),
             entry_id(provider, account, external_id, revision)))


def record_decision(store, *, provider, account, external_id, revision, decision,
                    reason_code=None, job_id=None, observed_at=None):
    """Persist a selection decision; creates the row when intake has not seen it."""
    if decision not in {'selected', 'noise', 'uncertain'}:
        raise ValueError('invalid_selection_decision')
    with store.lock:
        row = store.db.execute(
            'SELECT metadata_json FROM source_entries WHERE id=?',
            (entry_id(provider, account, external_id, revision),)).fetchone()
        metadata = json.loads(row['metadata_json']) if row else {}
        metadata.update({k: v for k, v in (
            ('reason_code', reason_code), ('decision_job_id', job_id)) if v is not None})
        if row is None:
            store.db.execute(
                'INSERT INTO source_entries(id, provider, account, external_id, revision,'
                ' status, original_digest, item_id, metadata_json, observed_at)'
                ' VALUES(?,?,?,?,?,?,?,?,?,?)',
                (entry_id(provider, account, external_id, revision), provider, account,
                 external_id, revision, decision, None, None,
                 _meta(metadata), observed_at or _now()))
        else:
            store.db.execute(
                'UPDATE source_entries SET status=?, metadata_json=? WHERE id=?',
                (decision, _meta(metadata),
                 entry_id(provider, account, external_id, revision)))
        return decision


def get(store, provider, account, external_id, revision):
    with store.lock:
        row = store.db.execute(
            'SELECT * FROM source_entries WHERE id=?',
            (entry_id(provider, account, external_id, revision),)).fetchone()
        return dict(row) if row else None


def pending_by_account(store, provider, account, limit=100):
    """Bounded live reads; never decodes history or metadata blobs at large."""
    with store.lock:
        return [dict(row) for row in store.db.execute(
            "SELECT id, external_id, revision, status, item_id, observed_at FROM source_entries"
            " WHERE provider=? AND account=? AND status='pending' ORDER BY observed_at, id LIMIT ?",
            (provider, account, limit)).fetchall()]


def coverage(store, provider, account):
    """Counts by status for one account: capture vs evaluation coverage."""
    with store.lock:
        rows = store.db.execute(
            'SELECT status, COUNT(*) FROM source_entries WHERE provider=? AND account=?'
            ' GROUP BY status', (provider, account)).fetchall()
        return {row[0]: row[1] for row in rows}


def prune_superseded(store, *, provider, account, external_id, keep_revisions):
    """Delete superseded revision rows no reader references anymore.

    Keeps exactly keep_revisions (normally the latest projected revision plus
    any revision a material/assessment basis still cites). Returns the pruned
    row count for the migration/retention receipt. Original blobs are never
    touched here: shared originals GC belongs to a wider, separately
    evidenced pass.
    """
    if not keep_revisions:
        raise ValueError('retention_requires_kept_revision')
    with store.lock:
        rows = store.db.execute(
            'SELECT id, revision FROM source_entries WHERE provider=? AND account=? AND external_id=?',
            (provider, account, external_id)).fetchall()
        pruned = 0
        for row in rows:
            if row['revision'] not in keep_revisions:
                store.db.execute('DELETE FROM source_entries WHERE id=?', (row['id'],))
                pruned += 1
        return pruned
