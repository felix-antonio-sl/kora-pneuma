"""Reconcile native names while retaining displaced objects and local state."""

from contextlib import contextmanager
import fcntl
import json
import os
from pathlib import Path
import shutil
import stat
import tempfile
import uuid

from .catalog import File, KoraError, digest, safe_relative
from .atomic import exchange, rename_new


def _sync_directory(path):
    fd = os.open(path, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def _atomic_bytes(path, data, mode=0o600):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".kora-", dir=path.parent)
    temporary = Path(temporary)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fchmod(stream.fileno(), mode)
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        _sync_directory(path.parent)
    finally:
        temporary.unlink(missing_ok=True)


def _json_write(path, value):
    _atomic_bytes(path, (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode())


def _read_json(path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError) as error:
        raise KoraError(f"Estado ilegible; conservar para recuperar: {path}") from error


def _description(file):
    return {"sha256": digest(file.data), "mode": file.mode}


def _identity(path):
    try:
        info = path.lstat()
    except FileNotFoundError:
        return None
    return [info.st_dev, info.st_ino]


def _file_info(path):
    """Read one opened inode, without following a late symlink substitution."""
    try:
        fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    except FileNotFoundError:
        return None
    except OSError as error:
        raise KoraError(f"Archivo no legible sin seguir enlaces: {path}") from error
    with os.fdopen(fd, "rb") as stream:
        info = os.fstat(stream.fileno())
        if not stat.S_ISREG(info.st_mode):
            raise KoraError(f"Objeto no regular; se conserva: {path}")
        return {"sha256": digest(stream.read()), "mode": stat.S_IMODE(info.st_mode)}


class Installer:
    def __init__(self, home: Path):
        self.home = Path(home).resolve()
        self.state = self.home / ".local/state/kora"
        self.state_file = self.state / "installed.json"
        self.journal_file = self.state / "journal.json"

    def _path(self, relative, *, captured=False):
        path = self.home / safe_relative(relative)
        for component in (path, *path.parents):
            if component == self.home:
                break
            if component.is_symlink() and not (captured and component == path):
                raise KoraError(f"Destino enlazado; requiere reconciliación explícita: {relative}")
            if component.exists() and component != path and not component.is_dir():
                raise KoraError(f"Un archivo ocupa el directorio requerido: {relative}")
        return path

    @contextmanager
    def _lock(self):
        self._path(".local/state/kora/lock")
        self.state.mkdir(parents=True, exist_ok=True, mode=0o700)
        self.state.chmod(0o700)
        with (self.state / "lock").open("a") as stream:
            try:
                fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError as error:
                raise KoraError("Hay otra operación KORA de instalación en curso") from error
            yield

    def _current(self, relative):
        return _file_info(self._path(relative))

    @staticmethod
    def _union(bundles):
        files = {}
        for bundle, members in bundles.items():
            for path, info in members.items():
                safe_relative(path)
                if path in files and files[path] != info:
                    raise KoraError(f"Archivo compartido con versiones distintas: {path}; actualizar sus consumidores juntos")
                files[path] = info
        return files

    def _replace(self, source, destination):
        # source becomes the actual displaced inode, including open writers.
        exchange(source, destination)
        _sync_directory(destination.parent)
        _sync_directory(source.parent)

    def _save(self, journal):
        # journal.json is authoritative; the per-transaction copy makes retained
        # objects discoverable after subsequent operations. Both precede rename.
        _json_write(self.journal_file, journal)
        _json_write(self.state / "transactions" / journal["transaction"] / "transaction.json", journal)

    def _slot(self, journal, step):
        # A late leaf symlink may itself have been captured. Inspect that name
        # with lstat/O_NOFOLLOW; never follow its target or accept linked parents.
        return self._path(f".local/state/kora/transactions/{journal['transaction']}/{step['slot']}", captured=True)

    def _done(self, journal, step):
        identity = _identity(self._slot(journal, step))
        if step["kind"] == "exchange":
            if identity is None:
                raise KoraError("Falta un objeto del intercambio; conservar la transacción para recuperar")
            return identity != step["incoming"]
        if step["kind"] == "publish":
            return identity is None
        return identity is not None

    def _run(self, journal, entry, step):
        path = self._path(entry["path"])
        slot = self._slot(journal, step)
        if step["kind"] == "exchange":
            self._replace(slot, path)
        else:
            source, destination = (slot, path) if step["kind"] == "publish" else (path, slot)
            rename_new(source, destination)
            _sync_directory(destination.parent)
            _sync_directory(source.parent)

    def _captured(self, journal, step):
        return step["kind"] != "publish" and self._done(journal, step)

    def apply(self, bundles: dict[str, dict[str, File]], remove=(), adopt=None):
        """Adoption requires the exact reviewed current digest, never a force flag."""
        with self._lock():
            self._recover_locked()
            before_state = _read_json(self.state_file, {})
            remove = set(remove)
            after_state = {key: value for key, value in before_state.items() if key not in remove}
            payloads = {}
            for bundle, files in bundles.items():
                after_state[bundle] = {}
                for relative, file in files.items():
                    path = self._path(relative)
                    if path == self.state or self.state in path.parents:
                        raise KoraError(f"El destino invade el estado del instalador: {relative}")
                    if not isinstance(file, File) or file.mode not in (0o600, 0o644, 0o700, 0o755, 0o664, 0o775):
                        raise KoraError(f"Archivo o modo no admitido: {relative}")
                    after_state[bundle][relative] = _description(file)
                    payloads[relative] = file
            before = self._union(before_state)
            after = self._union(after_state)
            reviewed = adopt or {}
            entries = []
            affected = {path for bundle in set(bundles) | remove
                        for state in (before_state, after_state)
                        for path in state.get(bundle, {})}
            for relative in sorted(affected):
                # Removing a consumer need not touch a still-shared file.
                if before.get(relative) == after.get(relative) and relative not in payloads:
                    continue
                current = self._current(relative)
                if relative in before and current != before[relative]:
                    raise KoraError(f"Se detectó cambio local; conservar y reconciliar: {relative}")
                if relative not in before and current is not None and reviewed.get(relative) != current["sha256"]:
                    raise KoraError(f"Archivo ajeno sin adopción comprobada: {relative}")
                wanted = after.get(relative)
                if current != wanted:
                    entries.append({"path": relative, "before": current, "after": wanted})
            if not entries and before_state == after_state:
                return {"changed": [], "transaction": None}

            transaction = uuid.uuid4().hex
            work = self.state / "transactions" / transaction
            work.mkdir(parents=True, mode=0o700)
            # Immutable snapshots document the reviewed bytes. The rename slots
            # separately retain the actual displaced objects, never just copies.
            try:
                for index, entry in enumerate(entries):
                    entry["index"] = index
                    path = self._path(entry["path"])
                    path.parent.mkdir(parents=True, exist_ok=True)
                    if path.parent.stat().st_dev != work.stat().st_dev:
                        raise KoraError(f"Destino y recuperación requieren el mismo filesystem: {entry['path']}")
                    if entry["before"] is not None:
                        saved = path.read_bytes()
                        if digest(saved) != entry["before"]["sha256"]:
                            raise KoraError(f"Se detectó cambio local durante preparación: {entry['path']}")
                        _atomic_bytes(work / f"{index}.before", saved)
                    if entry["after"] is not None:
                        _atomic_bytes(work / f"{index}.after", payloads[entry["path"]].data,
                                      entry["after"]["mode"])
                        entry["forward"] = {"kind": "publish" if entry["before"] is None else "exchange",
                                            "slot": f"{index}.after",
                                            "incoming": _identity(work / f"{index}.after")}
                    else:
                        entry["forward"] = {"kind": "capture", "slot": f"{index}.removed"}
            except BaseException:
                shutil.rmtree(work)
                raise
            journal = {"version": 2, "transaction": transaction, "status": "prepared", "entries": entries,
                       "before_state": before_state, "after_state": after_state}
            self._save(journal)
            try:
                for entry in entries:
                    if self._current(entry["path"]) != entry["before"]:
                        raise KoraError(f"Se detectó cambio local durante preparación: {entry['path']}")
                for entry in entries:
                    if self._current(entry["path"]) != entry["before"]:
                        raise KoraError(f"Se detectó cambio local durante instalación: {entry['path']}")
                    self._run(journal, entry, entry["forward"])
                    if self._captured(journal, entry["forward"]):
                        slot = self._slot(journal, entry["forward"])
                        if _file_info(slot) != entry["before"]:
                            raise KoraError(f"Se conservó cambio local concurrente: {entry['path']}; objeto: {slot}")
                _json_write(self.state_file, after_state)
                journal["status"] = "committed"
                self._save(journal)
            except Exception:
                self._restore(journal)
                raise
            return {"changed": [e["path"] for e in entries], "transaction": transaction}

    def _restore(self, journal):
        # Refuse known live edits before beginning. Atomic capture, not this
        # preflight, protects edits that race the actual undo operation.
        for entry in journal["entries"]:
            if not self._done(journal, entry["forward"]):
                continue
            if "undo" in entry and self._done(journal, entry["undo"]):
                continue
            if self._current(entry["path"]) != entry["after"]:
                raise KoraError(f"Recuperación conserva cambio local posterior: {entry['path']}")
        journal["status"] = "restoring"
        self._save(journal)
        concurrent = []
        for entry in reversed(journal["entries"]):
            if not self._done(journal, entry["forward"]):
                continue
            if "undo" in entry and self._done(journal, entry["undo"]):
                continue
            if self._current(entry["path"]) != entry["after"]:
                raise KoraError(f"Recuperación conserva cambio local posterior: {entry['path']}")
            if "undo" not in entry:
                step = {"kind": "capture", "slot": f"{entry['index']}.undo"}
                if entry["before"] is not None:
                    preserved = self._slot(journal, entry["forward"])
                    info = preserved.lstat()
                    if not stat.S_ISREG(info.st_mode):
                        raise KoraError(f"Objeto desplazado no regular conservado para recuperación manual: {preserved}")
                    slot = self._slot(journal, step)
                    # A hard link keeps the original capture in place, even
                    # after restoring its inode to the live name.
                    if not slot.exists():
                        os.link(preserved, slot, follow_symlinks=False)
                        _sync_directory(slot.parent)
                    if _identity(slot) != _identity(preserved):
                        raise KoraError(f"Objeto de recuperación ajeno; se conserva: {slot}")
                    step.update(kind="publish" if entry["after"] is None else "exchange",
                                incoming=_identity(slot))
                else:
                    if _identity(self._slot(journal, step)) is not None:
                        raise KoraError("Slot de recuperación ocupado; se conserva")
                entry["undo"] = step
                self._save(journal)
            self._run(journal, entry, entry["undo"])
            if self._captured(journal, entry["undo"]):
                slot = self._slot(journal, entry["undo"])
                if _file_info(slot) != entry["after"]:
                    concurrent.append(str(slot))
        _json_write(self.state_file, journal["before_state"])
        journal["status"] = "rolled_back"
        self._save(journal)
        if concurrent:
            raise KoraError("Recuperación conservó cambio local concurrente en: " + ", ".join(concurrent))

    def _recover_locked(self):
        journal = _read_json(self.journal_file, {})
        if journal.get("status") not in ("prepared", "restoring"):
            return {"recovered": False}
        if journal.get("version") != 2:
            raise KoraError("Journal anterior sin captura de inodes; conservar para reconciliación explícita")
        if journal["status"] == "prepared" and _read_json(self.state_file, {}) == journal["after_state"]:
            journal["status"] = "committed"
            self._save(journal)
            return {"recovered": True, "result": "committed"}
        self._restore(journal)
        return {"recovered": True, "result": "rolled_back"}

    def recover(self):
        with self._lock():
            return self._recover_locked()

    def rollback(self):
        with self._lock():
            self._recover_locked()
            journal = _read_json(self.journal_file, {})
            if journal.get("status") != "committed":
                raise KoraError("No hay una última instalación confirmada para deshacer")
            if _read_json(self.state_file, {}) != journal["after_state"]:
                raise KoraError("El estado avanzó; no se puede deshacer esta transacción")
            self._restore(journal)
            return {"rolled_back": journal["transaction"]}

    def status(self):
        state = _read_json(self.state_file, {})
        changes = []
        for relative, expected in self._union(state).items():
            try:
                current = self._current(relative)
                if current != expected:
                    changes.append({"path": relative, "state": "missing" if current is None else "modified"})
            except KoraError as error:
                changes.append({"path": relative, "state": "conflict", "error": str(error)})
        journal = _read_json(self.journal_file, {})
        preserved_changes = []
        for manifest in sorted((self.state / "transactions").glob("*/transaction.json")):
            transaction = _read_json(manifest, {})
            if transaction.get("version") != 2:
                continue
            for entry in transaction["entries"]:
                for direction, expected in (("forward", entry["before"]), ("undo", entry["after"])):
                    step = entry.get(direction)
                    if step is None or not self._captured(transaction, step):
                        continue
                    slot = self._slot(transaction, step)
                    try:
                        changed = _file_info(slot) != expected
                    except KoraError:
                        changed = True
                    if changed:
                        preserved_changes.append({"path": entry["path"], "backup": str(slot.relative_to(self.home)),
                                                  "transaction": transaction["transaction"]})
        return {"bundles": sorted(state), "changes": changes,
                "recovery_pending": journal.get("status") in ("prepared", "restoring"),
                "preserved_changes": preserved_changes}
