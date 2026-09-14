"""Private SQLite store and immutable originals. No provider effects live here."""
from contextlib import contextmanager
import hashlib
import os
from pathlib import Path
import sqlite3
import threading

SCHEMA_VERSION = 3
MIGRATION_1 = (
    "CREATE TABLE items(id TEXT PRIMARY KEY, document TEXT NOT NULL, field_versions TEXT NOT NULL)",
    "CREATE TABLE operations(operation_id TEXT PRIMARY KEY, fingerprint TEXT NOT NULL, actor TEXT NOT NULL, receipt TEXT NOT NULL, item_id TEXT, before_patch TEXT, after_patch TEXT, applied_version INTEGER, created_at TEXT NOT NULL)",
    "CREATE INDEX operations_item ON operations(item_id)",
    "CREATE TABLE events(event_key TEXT PRIMARY KEY, provider TEXT NOT NULL, account TEXT NOT NULL, external_id TEXT NOT NULL, revision TEXT NOT NULL, fingerprint TEXT NOT NULL, payload TEXT NOT NULL, status TEXT NOT NULL, error TEXT, received_at TEXT NOT NULL, UNIQUE(provider,account,external_id,revision))",
    "CREATE INDEX events_pending ON events(provider,account,status)",
    "CREATE TABLE cursors(provider TEXT NOT NULL, account TEXT NOT NULL, cursor TEXT NOT NULL, PRIMARY KEY(provider,account))",
    "CREATE TABLE originals(digest TEXT PRIMARY KEY, size INTEGER NOT NULL, relative_path TEXT NOT NULL UNIQUE)",
    "CREATE TABLE metadata(key TEXT PRIMARY KEY, value TEXT NOT NULL)",
)
# I1: work_cycles / runs / run_observations as authoritative control.
# Reference DDL is GUIA section 6; adjustments vs that text are documented in
# GUIA itself: runs.native_host preserves the full native identity required by
# hermes/codex adapters (provider+host+profile+id); run_observations.observed_at
# is nullable for migrated rows without durable timestamps (service requires it
# for new rows); runs.detail_json / work_cycles.detail_json carry the mutable
# legacy projection (bases, progress, route, delivery) transitional to bounded
# per-row reads without decoding the global JSON history.
MIGRATION_2 = (
    """CREATE TABLE work_cycles (
  id TEXT NOT NULL PRIMARY KEY, item_id TEXT NOT NULL REFERENCES items(id),
  trigger_key TEXT NOT NULL UNIQUE,
  input_fingerprint TEXT NOT NULL, purpose TEXT NOT NULL,
  authority_json TEXT NOT NULL CHECK(json_valid(authority_json)),
  state TEXT NOT NULL CHECK(state IN
    ('ready','running','waiting','paused','resolved','abandoned','recovery_required')),
  allowance_seconds REAL NOT NULL CHECK(allowance_seconds > 0),
  attempts_limit INTEGER NOT NULL CHECK(attempts_limit > 0),
  wake_json TEXT CHECK(wake_json IS NULL OR json_valid(wake_json)),
  predecessor_id TEXT REFERENCES work_cycles(id),
  parent_cycle_id TEXT REFERENCES work_cycles(id),
  budget_period_id TEXT NOT NULL,
  created_at TEXT, closed_at TEXT,
  detail_json TEXT NOT NULL DEFAULT '{}' CHECK(json_valid(detail_json)),
  UNIQUE(id, item_id)
)""",
    "CREATE INDEX cycles_ready ON work_cycles(state, item_id)",
    """CREATE UNIQUE INDEX one_open_cycle_per_item ON work_cycles(item_id)
  WHERE state IN ('ready','running','paused','recovery_required')""",
    """CREATE TABLE runs (
  id TEXT NOT NULL PRIMARY KEY, cycle_id TEXT NOT NULL,
  item_id TEXT NOT NULL, actor TEXT NOT NULL, parent_run_id TEXT REFERENCES runs(id),
  state TEXT NOT NULL CHECK(state IN
    ('reserved','dispatching','running','waiting_child','stop_requested','uncertain',
     'completed','failed','cancelled','expired')),
  integration TEXT NOT NULL CHECK(integration IN ('pending','integrated','discarded')),
  admission_json TEXT NOT NULL CHECK(json_valid(admission_json)),
  detail_json TEXT NOT NULL CHECK(json_valid(detail_json)),
  native_provider TEXT, native_host TEXT, native_profile TEXT, native_id TEXT,
  budget_period_id TEXT NOT NULL, reserved_seconds REAL NOT NULL CHECK(reserved_seconds > 0),
  observed_seconds REAL NOT NULL DEFAULT 0 CHECK(observed_seconds >= 0),
  cost_usd REAL CHECK(cost_usd IS NULL OR cost_usd >= 0),
  admitted_at TEXT, started_at TEXT, ended_at TEXT,
  FOREIGN KEY(cycle_id, item_id) REFERENCES work_cycles(id, item_id),
  UNIQUE(native_provider, native_host, native_profile, native_id)
)""",
    "CREATE INDEX runs_cycle ON runs(cycle_id, state)",
    "CREATE INDEX runs_period ON runs(budget_period_id, cycle_id)",
    "CREATE INDEX runs_active ON runs(state, integration)",
    "CREATE INDEX runs_item ON runs(item_id, state)",
    """CREATE UNIQUE INDEX one_native_active ON runs((1))
  WHERE state IN ('dispatching','running','stop_requested','uncertain')""",
    """CREATE TABLE run_observations (
  run_id TEXT NOT NULL REFERENCES runs(id), seq INTEGER NOT NULL CHECK(seq > 0),
  observed_at TEXT, native_state TEXT NOT NULL,
  runtime_seconds REAL NOT NULL CHECK(runtime_seconds >= 0),
  cost_usd REAL CHECK(cost_usd IS NULL OR cost_usd >= 0),
  receipt_json TEXT NOT NULL CHECK(json_valid(receipt_json)),
  PRIMARY KEY(run_id, seq)
)""",
    "CREATE INDEX observations_run ON run_observations(run_id, seq)",
)
# I2: materials / assessments / deliveries as the single authoritative
# representation. Reference DDL is GUIA section 6; adjustments are documented
# in GUIA: assessment ids are deterministic digests of durable fields (legacy
# records carried none); criterion_hash derives from the assessment evidence;
# created_at/retry_at/confirmed_at on deliveries are nullable because migrated
# outbox intents carry no durable timestamps (inventing them is forbidden);
# deliveries.item_id/item_version are nullable for transient UI sends without
# an item obligation; deliveries_target index serves the per-account scans.
MIGRATION_3 = (
    """CREATE TABLE materials (
  id TEXT NOT NULL, version INTEGER NOT NULL CHECK(version > 0),
  item_id TEXT NOT NULL REFERENCES items(id),
  author TEXT NOT NULL, title TEXT NOT NULL,
  mime_type TEXT NOT NULL, filename TEXT NOT NULL,
  digest TEXT NOT NULL REFERENCES originals(digest),
  size INTEGER NOT NULL CHECK(size >= 0),
  basis_json TEXT NOT NULL CHECK(json_valid(basis_json)),
  source_versions_json TEXT NOT NULL CHECK(json_valid(source_versions_json)),
  mandate_id TEXT,
  source_material_json TEXT CHECK(source_material_json IS NULL OR json_valid(source_material_json)),
  created_at TEXT NOT NULL,
  PRIMARY KEY(id, version),
  UNIQUE(id, version, item_id)
)""",
    "CREATE INDEX materials_item ON materials(item_id, id, version)",
    """CREATE TABLE assessments (
  id TEXT NOT NULL PRIMARY KEY, item_id TEXT NOT NULL REFERENCES items(id),
  item_version INTEGER NOT NULL CHECK(item_version > 0),
  material_id TEXT, material_version INTEGER,
  actor TEXT NOT NULL, satisfied INTEGER NOT NULL CHECK(satisfied IN (0,1)),
  criterion_hash TEXT NOT NULL, evidence TEXT NOT NULL, gap TEXT,
  resolution_basis_json TEXT NOT NULL CHECK(json_valid(resolution_basis_json)),
  material_basis_json TEXT NOT NULL CHECK(json_valid(material_basis_json)),
  source_versions_json TEXT NOT NULL CHECK(json_valid(source_versions_json)),
  mandate_id TEXT,
  created_at TEXT NOT NULL,
  CHECK((material_id IS NULL) = (material_version IS NULL)),
  FOREIGN KEY(material_id, material_version, item_id)
    REFERENCES materials(id, version, item_id)
)""",
    "CREATE INDEX assessments_item ON assessments(item_id, created_at, id)",
    """CREATE TABLE deliveries (
  id TEXT NOT NULL PRIMARY KEY, item_id TEXT REFERENCES items(id),
  item_version INTEGER CHECK(item_version IS NULL OR item_version > 0),
  channel TEXT NOT NULL, target_key TEXT NOT NULL, semantic_key TEXT NOT NULL,
  state TEXT NOT NULL CHECK(state IN
    ('pending','sending','confirmed','suppressed','uncertain','failed')),
  payload_json TEXT NOT NULL CHECK(json_valid(payload_json)),
  segments_json TEXT NOT NULL CHECK(json_valid(segments_json)),
  created_at TEXT, retry_at TEXT, confirmed_at TEXT,
  UNIQUE(channel, target_key, semantic_key)
)""",
    "CREATE INDEX deliveries_pending ON deliveries(state, retry_at)",
    "CREATE INDEX deliveries_target ON deliveries(channel, target_key, state)",
)


def private_dir(path):
    path = Path(path).absolute()
    for component in (path, *path.parents):
        if component.is_symlink():
            raise ValueError("symlink_path")
    path.mkdir(mode=0o700, parents=True, exist_ok=True)
    if not path.is_dir() or path.stat().st_uid != os.getuid():
        raise ValueError("unsafe_directory")
    path.chmod(0o700)
    return path


def fsync_dir(path):
    fd = os.open(path, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def write_private(path, data):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
    except BaseException:
        Path(path).unlink(missing_ok=True)
        raise
    fsync_dir(Path(path).parent)


class Store:
    def __init__(self, data_dir):
        self.root = private_dir(data_dir)
        self.originals = private_dir(self.root / "originals")
        self.path = self.root / "gtd.sqlite3"
        for path in (self.path, Path(str(self.path) + "-wal"), Path(str(self.path) + "-shm")):
            if path.is_symlink():
                raise ValueError("symlink_path")
            if path.exists():
                if not path.is_file() or path.stat().st_uid != os.getuid() or path.stat().st_nlink != 1:
                    raise ValueError("unsafe_database")
                path.chmod(0o600)
        if not self.path.exists():
            write_private(self.path, b"")
        self.lock = threading.RLock()
        self.db = sqlite3.connect(self.path, isolation_level=None, check_same_thread=False, timeout=10)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA foreign_keys=ON")
        self.db.execute("PRAGMA busy_timeout=10000")
        try:
            with self.transaction():
                version = self.db.execute("PRAGMA user_version").fetchone()[0]
                if version > SCHEMA_VERSION:
                    raise ValueError("newer_schema")
                if version == 0:
                    for statement in MIGRATION_1:
                        self.db.execute(statement)
                    for statement in MIGRATION_2:
                        self.db.execute(statement)
                    for statement in MIGRATION_3:
                        self.db.execute(statement)
                    self.db.execute("PRAGMA user_version=3")
                elif version == 1:
                    for statement in MIGRATION_2:
                        self.db.execute(statement)
                    for statement in MIGRATION_3:
                        self.db.execute(statement)
                    self.db.execute("PRAGMA user_version=3")
                elif version == 2:
                    for statement in MIGRATION_3:
                        self.db.execute(statement)
                    self.db.execute("PRAGMA user_version=3")
            self.db.execute("PRAGMA journal_mode=WAL")
            self.db.execute("PRAGMA synchronous=FULL")
            for suffix in ("", "-wal", "-shm"):
                path = Path(str(self.path) + suffix)
                if path.exists():
                    path.chmod(0o600)
        except BaseException:
            self.db.close()
            raise

    @contextmanager
    def transaction(self):
        with self.lock:
            self.db.execute("BEGIN IMMEDIATE")
            try:
                yield self.db
                self.db.execute("COMMIT")
            except BaseException:
                self.db.execute("ROLLBACK")
                raise

    def save_original(self, content):
        digest = hashlib.sha256(content).hexdigest()
        path = self.originals / digest
        try:
            write_private(path, content)
        except FileExistsError:
            if path.is_symlink() or not path.is_file() or path.stat().st_nlink != 1:
                raise ValueError("unsafe_original")
            if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                raise ValueError("original_corrupt")
            path.chmod(0o600)
        return {"path": f"originals/{digest}", "sha256": digest, "size": len(content)}

    def close(self):
        with self.lock:
            self.db.close()
