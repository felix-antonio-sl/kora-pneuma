"""Private SQLite store and immutable originals. No provider effects live here."""
from contextlib import contextmanager
import hashlib
import os
from pathlib import Path
import sqlite3
import threading

SCHEMA_VERSION = 1
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
                    self.db.execute("PRAGMA user_version=1")
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
