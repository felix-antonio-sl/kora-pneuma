"""Single queryable authority for per-revision intake/selection state (I3).

One row per (provider, account, collection, external_id, revision); the id is
a JSON-array digest so no separator can collide with opaque fields. The sync
engine reports intake/projection; selection paths report decisions; retention
prunes superseded rows and archives their ids so migration never resurrects.
Ownership: this table answers per-revision status; partition/cursor/cycle
state stays with the sync engine; coverage summaries stay with the monitor.
"""
import hashlib
import json
from datetime import datetime, timezone

STATUSES = frozenset({'pending', 'selected', 'noise', 'uncertain', 'unavailable', 'deleted'})
INTAKE_STATUS = {'present': 'pending', 'deleted': 'deleted', 'degraded': 'unavailable'}
PRUNED_ARCHIVE_KEY = 'source-entries:pruned'
RETENTION_RECEIPT_KEY = 'source-entries:retention'


def entry_id(provider, account, collection, external_id, revision):
    return hashlib.sha256(json.dumps(
        [provider, account, collection, external_id, revision],
        ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()


def _now():
    return datetime.now(timezone.utc).isoformat()


def _meta(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))


def report_intake(store, *, provider, account, collection, external_id, revision,
                  availability, original_digest, index_key, sequence, observed_at=None):
    """Upsert on sight of a revision; merges intake facts, keeps decisions."""
    if availability not in INTAKE_STATUS:
        raise ValueError('invalid_availability')
    row_id = entry_id(provider, account, collection, external_id, revision)
    with store.lock:
        row = store.db.execute(
            'SELECT status, original_digest, metadata_json FROM source_entries WHERE id=?',
            (row_id,)).fetchone()
        if row is None:
            store.db.execute(
                'INSERT INTO source_entries(id, provider, account, collection, external_id,'
                ' revision, status, original_digest, item_id, metadata_json, observed_at)'
                ' VALUES(?,?,?,?,?,?,?,?,?,?,?)',
                (row_id, provider, account, collection, external_id, revision,
                 INTAKE_STATUS[availability], original_digest, None,
                 _meta({'index_key': index_key, 'sequence': sequence,
                        'availability': availability, 'projection': 'pending'}),
                 observed_at or _now()))
            return INTAKE_STATUS[availability]
        # A decision-first row (selective path) gains its intake facts here;
        # a decided status is never downgraded, availability stays current.
        metadata = json.loads(row['metadata_json'])
        metadata['availability'] = availability
        metadata.setdefault('index_key', index_key)
        metadata.setdefault('sequence', sequence)
        store.db.execute(
            'UPDATE source_entries SET original_digest=COALESCE(original_digest,?),'
            ' metadata_json=? WHERE id=?',
            (original_digest, _meta(metadata), row_id))
        return row['status']


def report_projection(store, *, provider, account, collection, external_id, revision,
                      item_id=None, projected=True):
    """Link the projected affair (or its deliberate absence) to the revision."""
    row_id = entry_id(provider, account, collection, external_id, revision)
    with store.lock:
        row = store.db.execute(
            'SELECT metadata_json FROM source_entries WHERE id=?', (row_id,)).fetchone()
        if row is None:
            raise ValueError('unknown_source_revision')
        metadata = json.loads(row['metadata_json'])
        metadata['projection'] = 'applied' if projected else 'not_needed'
        store.db.execute(
            'UPDATE source_entries SET item_id=?, metadata_json=? WHERE id=?',
            (item_id, _meta(metadata), row_id))


def record_decision(store, *, provider, account, collection, external_id, revision,
                    decision, reason_code=None, job_id=None, observed_at=None):
    """Persist a selection decision; creates the row when intake has not seen it."""
    if decision not in {'selected', 'noise', 'uncertain'}:
        raise ValueError('invalid_selection_decision')
    row_id = entry_id(provider, account, collection, external_id, revision)
    with store.lock:
        row = store.db.execute(
            'SELECT metadata_json FROM source_entries WHERE id=?', (row_id,)).fetchone()
        metadata = json.loads(row['metadata_json']) if row else {}
        metadata.update({k: v for k, v in (
            ('reason_code', reason_code), ('decision_job_id', job_id)) if v is not None})
        if row is None:
            store.db.execute(
                'INSERT INTO source_entries(id, provider, account, collection, external_id,'
                ' revision, status, original_digest, item_id, metadata_json, observed_at)'
                ' VALUES(?,?,?,?,?,?,?,?,?,?,?)',
                (row_id, provider, account, collection, external_id, revision,
                 decision, None, None, _meta(metadata), observed_at or _now()))
        else:
            store.db.execute(
                'UPDATE source_entries SET status=?, metadata_json=? WHERE id=?',
                (decision, _meta(metadata), row_id))
        return decision


def get(store, provider, account, collection, external_id, revision):
    with store.lock:
        row = store.db.execute(
            'SELECT * FROM source_entries WHERE id=?',
            (entry_id(provider, account, collection, external_id, revision),)).fetchone()
        return dict(row) if row else None


def pending_by_account(store, provider, account, collection=None, limit=100):
    """Bounded live reads; never decodes history or metadata blobs at large."""
    with store.lock:
        if collection is None:
            rows = store.db.execute(
                "SELECT id, collection, external_id, revision, status, item_id, observed_at"
                " FROM source_entries WHERE provider=? AND account=? AND status='pending'"
                " ORDER BY observed_at, id LIMIT ?",
                (provider, account, limit)).fetchall()
        else:
            rows = store.db.execute(
                "SELECT id, collection, external_id, revision, status, item_id, observed_at"
                " FROM source_entries WHERE provider=? AND account=? AND collection=?"
                " AND status='pending' ORDER BY observed_at, id LIMIT ?",
                (provider, account, collection, limit)).fetchall()
        return [dict(row) for row in rows]


def coverage(store, provider, account, collection=None):
    """Counts by status for one account (optionally one collection)."""
    with store.lock:
        if collection is None:
            rows = store.db.execute(
                'SELECT status, COUNT(*) FROM source_entries WHERE provider=? AND account=?'
                ' GROUP BY status', (provider, account)).fetchall()
        else:
            rows = store.db.execute(
                'SELECT status, COUNT(*) FROM source_entries WHERE provider=? AND account=?'
                ' AND collection=? GROUP BY status', (provider, account, collection)).fetchall()
        return {row[0]: row[1] for row in rows}


def _pruned_archive(store):
    with store.lock:
        row = store.db.execute(
            'SELECT value FROM metadata WHERE key=?', (PRUNED_ARCHIVE_KEY,)).fetchone()
        return set(json.loads(row[0])) if row else set()


def _archive_pruned(store, row_ids):
    with store.lock:
        known = _pruned_archive(store)
        known |= set(row_ids)
        store.db.execute('INSERT OR REPLACE INTO metadata VALUES(?,?)',
                         (PRUNED_ARCHIVE_KEY, _meta(sorted(known))))


def prune_superseded(store, *, provider, account, external_id, keep_revisions, collection=None):
    """Delete superseded revision rows no reader references anymore.

    Keeps exactly keep_revisions. Pruned ids join the durable archive so a
    later migration never resurrects them. Original blobs are never touched
    here. collection=None keeps the single-collection behavior for callers
    that already scoped the external id; pass it when ids repeat per
    collection.
    """
    if not keep_revisions:
        raise ValueError('retention_requires_kept_revision')
    with store.transaction(), store.lock:
        if collection is None:
            rows = store.db.execute(
                'SELECT id, revision FROM source_entries WHERE provider=? AND account=?'
                ' AND external_id=?', (provider, account, external_id)).fetchall()
        else:
            rows = store.db.execute(
                'SELECT id, revision FROM source_entries WHERE provider=? AND account=?'
                ' AND collection=? AND external_id=?',
                (provider, account, collection, external_id)).fetchall()
        pruned = []
        for row in rows:
            if row['revision'] not in keep_revisions:
                store.db.execute('DELETE FROM source_entries WHERE id=?', (row['id'],))
                pruned.append(row['id'])
        if pruned:
            _archive_pruned(store, pruned)
        return len(pruned)


DECIDED_KEEP = frozenset({'selected', 'noise', 'uncertain'})

# Synthetic per-revision traces: their meaning is covered exactly when the
# underlying revision's own row stays retained. Anything else without bytes
# (deleted:, genuine unavailable, unread:) is provider evidence, not a trace.
SYNTHETIC_TRACE_PREFIXES = ("not-selected:", "unassessed:")


def _trace_underlying(revision):
    for prefix in SYNTHETIC_TRACE_PREFIXES:
        if revision.startswith(prefix):
            return revision[len(prefix):]
    return None


def run_retention(store):
    """Effective retention pass with an honest keep policy.

    Keeps, per object: every pending row (live obligations are never pruned),
    every row whose bytes are still cited, the latest projected row with bytes
    (intake sequence order), and the latest decided row (decision time order)
    so the current verdict is never re-inferred. Sequence and decision time
    are never compared across families; rows with unknown order stay.
    Transport traces without bytes (unavailable/deleted, no digest) are never
    projections. A selection verdict never substitutes posterior provider
    evidence, so only a synthetic trace (not-selected:/unassessed:) whose
    underlying revision stays retained is covered and goes; real availability
    evidence (deleted:, genuine unavailable) is always kept. Pruned ids join
    the durable archive so migration never resurrects them. One transaction;
    the receipt persists (reruns converge to zero).
    """
    with store.transaction():
        cited = set()
        for (document,) in store.db.execute("SELECT document FROM items"):
            item = json.loads(document)
            for rev in item.get("source_revisions", []) or []:
                digest = ((rev or {}).get("original") or {}).get("sha256")
                if digest:
                    cited.add(digest)
            for stub in item.get("materials", []) or []:
                if stub.get("digest"):
                    cited.add(stub["digest"])

        def sequence(row):
            try:
                value = json.loads(row["metadata_json"]).get("sequence")
            except (ValueError, TypeError):
                value = None
            return value if isinstance(value, int) else None

        def decided_time(row):
            if row["status"] not in DECIDED_KEEP:
                return None
            observed = row["observed_at"]
            return observed if isinstance(observed, str) and observed else None

        groups = store.db.execute(
            "SELECT provider, account, collection, external_id FROM source_entries"
            " GROUP BY provider, account, collection, external_id").fetchall()
        pruned_total, objects = 0, 0
        for group in groups:
            rows = [dict(r) for r in store.db.execute(
                "SELECT * FROM source_entries"
                " WHERE provider=? AND account=? AND collection=? AND external_id=?",
                (group["provider"], group["account"], group["collection"],
                 group["external_id"])).fetchall()]
            if len(rows) < 2:
                continue
            objects += 1
            keep = set()
            for row in rows:
                if row["status"] == "pending" or row["original_digest"] in cited:
                    keep.add(row["id"])
            projected = [r for r in rows
                         if r["original_digest"] is not None
                         and json.loads(r["metadata_json"]).get("projection") == "applied"
                         and sequence(r) is not None]
            if projected:
                keep.add(max(projected, key=sequence)["id"])
            timed = [(r, decided_time(r)) for r in rows]
            timed = [(r, moment) for r, moment in timed if moment is not None]
            if timed:
                keep.add(max(timed, key=lambda pair: pair[1])[0]["id"])
            # Vigente vs historial is decided here per object, by observed
            # order only (never by id/hash): kept rows are the live state,
            # the rest is history eligible for pruning when covered.
            kept_revisions = {r["revision"] for r in rows if r["id"] in keep}
            for row in rows:
                if row["id"] in keep:
                    continue
                if row["original_digest"] is None and row["status"] in {
                        "unavailable", "deleted"}:
                    # Only a synthetic trace whose underlying revision stays
                    # retained is covered; anything else (real deletion or
                    # genuine unavailability) is current availability evidence.
                    underlying = _trace_underlying(row["revision"])
                    if underlying is None or underlying not in kept_revisions:
                        continue
                elif sequence(row) is None and decided_time(row) is None:
                    continue
                store.db.execute("DELETE FROM source_entries WHERE id=?", (row["id"],))
                pruned_total += 1
                _archive_pruned(store, [row["id"]])
        receipt = {"pruned_rows": pruned_total, "multi_revision_objects": objects,
                   "cited_digests": len(cited)}
        store.db.execute("INSERT OR REPLACE INTO metadata VALUES(?,?)",
                         (RETENTION_RECEIPT_KEY, _meta(receipt)))
        return receipt
