"""Reconcile native names while retaining displaced objects and local state."""

from contextlib import contextmanager
import copy
import fcntl
import inspect
import json
import os
from pathlib import Path
import shutil
import stat
import tempfile
import uuid

from .catalog import File, KoraError, _resource_exclusion, digest, safe_relative
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


_ALLOWED_MODES = (0o600, 0o644, 0o700, 0o755, 0o664, 0o775)
_PRESERVABLE_RESIDUE_REASONS = {
    "caché", "bytecode", "archivo temporal", "directorio temporal",
    "estado temporal de KORA",
}


def _json_copy(value, label):
    """Return JSON-compatible data without retaining a caller-owned object."""
    try:
        encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, allow_nan=False)
        return copy.deepcopy(json.loads(encoded))
    except (TypeError, ValueError, json.JSONDecodeError) as error:
        raise KoraError(f"{label} debe ser JSON serializable") from error


def _canonical(value):
    try:
        return json.dumps(value, ensure_ascii=False, sort_keys=True,
                          separators=(",", ":"), allow_nan=False).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise KoraError("El plan no puede representarse como JSON determinista") from error


def _physical(info):
    """Project a receipt member to the fields that describe the live inode."""
    if info is None:
        return None
    if not isinstance(info, dict) or "sha256" not in info or "mode" not in info:
        raise KoraError("Recibo de instalación inválido; faltan sha256 o mode")
    return {"sha256": info["sha256"], "mode": info["mode"]}


def _description(file):
    if not isinstance(file, File) or not isinstance(file.data, bytes):
        raise KoraError("Archivo no admitido; se requiere File con bytes")
    if file.mode not in _ALLOWED_MODES:
        raise KoraError("Archivo o modo no admitido")
    result = {"sha256": digest(file.data), "mode": file.mode}
    if file.source is not None:
        if not isinstance(file.source, dict):
            raise KoraError("La procedencia del archivo debe ser un objeto")
        result["source"] = _json_copy(file.source, "La procedencia del archivo")
    return result


def _project_union(bundles):
    """Project ownership to physical descriptors while retaining all members."""
    files = {}
    conflicts = []
    for bundle in sorted(bundles):
        members = bundles[bundle]
        if not isinstance(members, dict):
            raise KoraError(f"Recibo de instalación inválido para {bundle}")
        for path in sorted(members):
            safe_relative(path)
            info = _physical(members[path])
            previous = files.get(path)
            if previous is not None and previous != info:
                conflicts.append({
                    "path": path,
                    "kind": "shared_version",
                    "error": (f"Archivo compartido con versiones distintas: {path}; "
                              "actualizar sus consumidores juntos"),
                    "before": previous,
                    "after": info,
                })
                continue
            files[path] = info
    return files, conflicts


def _plan_digest(plan):
    return digest(_canonical({key: value for key, value in plan.items()
                              if key != "plan_sha256"}))


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


def _file_bytes(path):
    """Read a regular destination through an opened, non-following descriptor."""
    try:
        fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    except FileNotFoundError:
        raise KoraError(f"Falta el destino durante la preparación: {path}")
    except OSError as error:
        raise KoraError(f"Archivo no legible sin seguir enlaces: {path}") from error
    with os.fdopen(fd, "rb") as stream:
        info = os.fstat(stream.fileno())
        if not stat.S_ISREG(info.st_mode):
            raise KoraError(f"Objeto no regular; se conserva: {path}")
        return stream.read()


class Installer:
    def __init__(self, home: Path):
        self.home = Path(home).resolve()
        self.state = self.home / ".local/state/kora"
        self.state_file = self.state / "installed.json"
        self.journal_file = self.state / "journal.json"

    def receipts(self):
        """Read existing ownership for selection; apply still checks the live files."""
        return _read_json(self.state_file, {})

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
        files, conflicts = _project_union(bundles)
        if conflicts:
            raise KoraError(conflicts[0]["error"])
        return files

    @staticmethod
    def _copy_state(state):
        if not isinstance(state, dict):
            raise KoraError("Recibo de instalación inválido; se esperaba un objeto")
        copied = _json_copy(state, "El recibo de instalación")
        result = {}
        for bundle in sorted(copied):
            if not isinstance(bundle, str) or not bundle:
                raise KoraError(f"Nombre de bundle inválido en el recibo: {bundle!r}")
            members = copied[bundle]
            if not isinstance(members, dict):
                raise KoraError(f"Recibo de instalación inválido para {bundle}")
            result[bundle] = {path: members[path] for path in sorted(members)}
        return result

    def _destination(self, relative):
        path = self._path(relative)
        if path == self.state or self.state in path.parents:
            raise KoraError(f"El destino invade el estado del instalador: {relative}")
        return path

    @staticmethod
    def _remove_names(remove):
        if remove is None:
            return []
        if isinstance(remove, (str, bytes)):
            raise KoraError("remove debe ser una colección de bundles")
        try:
            names = list(remove)
        except TypeError as error:
            raise KoraError("remove debe ser una colección de bundles") from error
        for name in names:
            if not isinstance(name, str) or not name:
                raise KoraError(f"Nombre de bundle inválido: {name!r}")
        return sorted(set(names))

    @staticmethod
    def _bundle_inputs(value, label):
        if value is None:
            return {}
        if not isinstance(value, dict):
            raise KoraError(f"{label} debe ser un objeto de bundles")
        result = {}
        for bundle in sorted(value):
            if not isinstance(bundle, str) or not bundle:
                raise KoraError(f"Nombre de bundle inválido: {bundle!r}")
            members = value[bundle]
            if not isinstance(members, dict):
                raise KoraError(f"{label} inválido para {bundle}")
            result[bundle] = {path: members[path] for path in sorted(members)}
        return result

    @staticmethod
    def _residue_reason(relative):
        # Native destinations such as .agents are private containers, while a
        # managed .pyc below them is still bytecode residue. Ask the catalog
        # policy about each suffix and retain only an explicitly temporary
        # classification; .env and other private leaves never qualify.
        parts = relative.split("/")
        for index in range(len(parts)):
            reason = _resource_exclusion("/".join(parts[index:]))
            if reason in _PRESERVABLE_RESIDUE_REASONS:
                return reason
        return None

    @staticmethod
    def _invoke_validate(validate, plan):
        if validate is None:
            return
        if not callable(validate):
            raise KoraError("validate debe ser una función de revalidación")
        try:
            signature = inspect.signature(validate)
            required = [parameter for parameter in signature.parameters.values()
                        if parameter.kind in (parameter.POSITIONAL_ONLY,
                                              parameter.POSITIONAL_OR_KEYWORD)
                        and parameter.default is parameter.empty]
        except (TypeError, ValueError):
            required = []
        result = validate(plan) if required else validate()
        if result is False:
            raise KoraError("La revalidación de fuentes rechazó la instalación")

    def _calculate(self, bundles, remove=(), adopt=None, patches=None, context=None):
        """Build a read-only, deterministic calculation for one operation."""
        full = self._bundle_inputs(bundles, "bundles")
        sparse = self._bundle_inputs(patches, "patches")
        removed = self._remove_names(remove)
        overlap = (set(full) & set(sparse)) | (set(full) & set(removed)) | (set(sparse) & set(removed))
        if overlap:
            names = ", ".join(sorted(overlap))
            raise KoraError(f"Bundle seleccionado con operaciones ambiguas: {names}")
        if adopt is None:
            reviewed = {}
        elif isinstance(adopt, dict):
            reviewed = dict(adopt)
        else:
            raise KoraError("adopt debe ser un objeto de hashes revisados")
        context_value = None if context is None else _json_copy(context, "context")

        before_state = self._copy_state(self.receipts())
        after_state = self._copy_state(before_state)
        payloads = {}
        for bundle in full:
            members = {}
            for relative, file in full[bundle].items():
                safe_relative(relative)
                description = _description(file)
                members[relative] = description
                payloads[relative] = file
            after_state[bundle] = members
        for bundle in sparse:
            members = self._copy_state({bundle: before_state.get(bundle, {})}).get(bundle, {})
            for relative, file in sparse[bundle].items():
                safe_relative(relative)
                if file is None:
                    members.pop(relative, None)
                    continue
                description = _description(file)
                members[relative] = description
                payloads[relative] = file
            if members or bundle in before_state:
                after_state[bundle] = {path: members[path] for path in sorted(members)}
            else:
                after_state.pop(bundle, None)
        for bundle in removed:
            after_state.pop(bundle, None)
        before_state = {bundle: {path: before_state[bundle][path] for path in sorted(before_state[bundle])}
                        for bundle in sorted(before_state)}
        after_state = {bundle: {path: after_state[bundle][path] for path in sorted(after_state[bundle])}
                       for bundle in sorted(after_state)}

        before, conflicts = _project_union(before_state)
        after, after_conflicts = _project_union(after_state)
        conflicts.extend(after_conflicts)
        touched_bundles = set(full) | set(sparse) | set(removed)
        affected = {relative for bundle in touched_bundles
                    for state in (before_state, after_state)
                    for relative in state.get(bundle, {})}
        current = {}
        destination_errors = {}
        for relative in sorted(affected):
            try:
                self._destination(relative)
                current[relative] = self._current(relative)
            except KoraError as error:
                current[relative] = None
                destination_errors[relative] = str(error)

        def add_conflict(kind, relative, error, expected=None, actual=None, desired=None):
            item = {"path": relative, "kind": kind, "error": error}
            if expected is not None:
                item["expected"] = expected
            if actual is not None:
                item["actual"] = actual
            if desired is not None:
                item["desired"] = desired
            conflicts.append(item)

        entries = []
        for relative in sorted(affected):
            expected = before.get(relative)
            desired = after.get(relative)
            live = current[relative]
            live_error = destination_errors.get(relative)

            # Ownership/source metadata can change without changing the live
            # bytes or mode. Preserve a regular local edit in that case: there
            # is no physical effect to protect or execute.
            if expected == desired:
                if live_error:
                    add_conflict("destination", relative, live_error,
                                 expected=expected, desired=desired)
                elif expected is not None and live is None:
                    add_conflict("missing", relative,
                                 f"Falta el archivo administrado: {relative}",
                                 expected=expected, desired=desired)
                continue

            if live_error:
                add_conflict("destination", relative, live_error,
                             expected=expected, actual=live, desired=desired)
                continue
            if expected is not None and live != expected:
                if desired is None and live is not None:
                    reason = self._residue_reason(relative)
                    if reason is not None:
                        entries.append({
                            "path": relative,
                            "before": expected,
                            "after": desired,
                            "preserved": live,
                            "preservation": {
                                "reason": reason,
                                "expected": expected,
                                "actual": live,
                            },
                        })
                        continue
                add_conflict("local_edit", relative,
                             f"Se detectó cambio local; conservar y reconciliar: {relative}",
                             expected=expected, actual=live, desired=desired)
                continue
            adopted = False
            if expected is None and live is not None:
                if reviewed.get(relative) != live["sha256"]:
                    add_conflict("foreign", relative,
                                 f"Archivo ajeno sin adopción comprobada: {relative}",
                                 actual=live, desired=desired)
                    continue
                adopted = True
            if desired is not None and desired != live and relative not in payloads:
                add_conflict("payload", relative,
                             f"No hay payload para actualizar: {relative}",
                             expected=expected, actual=live, desired=desired)
                continue
            entry = {"path": relative, "before": expected, "after": desired}
            if adopted:
                entry["adopted"] = True
            entries.append(entry)

        ownership = []
        for bundle in sorted(set(before_state) | set(after_state)):
            old_members = before_state.get(bundle, {})
            new_members = after_state.get(bundle, {})
            for relative in sorted(set(old_members) | set(new_members)):
                old = old_members.get(relative)
                new = new_members.get(relative)
                if old == new:
                    continue
                action = "add" if old is None else "remove" if new is None else "update"
                ownership.append({"bundle": bundle, "path": relative,
                                  "before": old, "after": new, "action": action})

        effects = []
        for entry in entries:
            if entry.get("preservation") is not None:
                action = "preserve"
            elif entry["before"] is None:
                action = "create"
            elif entry["after"] is None:
                action = "remove"
            else:
                action = "update"
            effect = {"path": entry["path"], "before": entry["before"],
                      "after": entry["after"], "action": action}
            effects.append(effect)

        preconditions = {
            "receipt_sha256": digest(_canonical(before_state)),
            "destinations": {relative: current[relative] for relative in sorted(current)},
        }
        if destination_errors:
            preconditions["destination_errors"] = {
                relative: destination_errors[relative] for relative in sorted(destination_errors)
            }
        plan = {
            "ok": not conflicts,
            "home": str(self.home),
            "bundles": sorted(full),
            "patches": {bundle: sorted(sparse[bundle]) for bundle in sorted(sparse)},
            "remove": removed,
            "effects": effects,
            "ownership": ownership,
            "conflicts": conflicts,
            "preconditions": preconditions,
            "context": context_value,
        }
        plan["plan_sha256"] = _plan_digest(plan)
        return {
            "plan": plan,
            "before_state": before_state,
            "after_state": after_state,
            "entries": entries,
            "payloads": payloads,
        }

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

    @staticmethod
    def _plan_body(plan):
        if not isinstance(plan, dict) or not isinstance(plan.get("plan_sha256"), str):
            raise KoraError("Plan de instalación inválido o sin digest")
        if _plan_digest(plan) != plan["plan_sha256"]:
            raise KoraError("Plan de instalación alterado; requiere una nueva preparación")
        return {key: value for key, value in plan.items() if key != "plan_sha256"}

    @staticmethod
    def _assert_same_plan(expected, actual):
        expected_body = Installer._plan_body(expected)
        actual_body = Installer._plan_body(actual)
        if expected_body != actual_body:
            raise KoraError("El plan de instalación quedó obsoleto; preparar nuevamente")

    def _check_runtime_preconditions(self, calculation):
        plan = calculation["plan"]
        expected_receipt = plan["preconditions"]["receipt_sha256"]
        actual_receipt = digest(_canonical(self._copy_state(self.receipts())))
        if actual_receipt != expected_receipt:
            raise KoraError("El recibo de instalación quedó obsoleto; preparar nuevamente")
        expected_destinations = plan["preconditions"].get("destinations", {})
        for relative in sorted(expected_destinations):
            try:
                actual = self._current(relative)
            except KoraError as error:
                actual = None
                expected_error = plan["preconditions"].get("destination_errors", {}).get(relative)
                if expected_error != str(error):
                    raise KoraError(f"El plan de instalación quedó obsoleto; destino: {relative}") from error
            if actual != expected_destinations[relative]:
                raise KoraError(f"El plan de instalación quedó obsoleto; destino: {relative}")

    def _execute(self, calculation):
        plan = calculation["plan"]
        if not plan["ok"]:
            details = "; ".join(item.get("error", "conflicto de instalación")
                                 for item in plan["conflicts"])
            raise KoraError(details or "Conflicto de instalación")
        entries = []
        for raw in calculation["entries"]:
            entry = {key: copy.deepcopy(value) for key, value in raw.items()
                     if key not in ("adopted",)}
            entries.append(entry)
        before_state = calculation["before_state"]
        after_state = calculation["after_state"]
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
                    saved = _file_bytes(path)
                    expected = entry.get("preserved", entry["before"])
                    if _file_info(path) != expected:
                        raise KoraError(f"Se detectó cambio local durante preparación: {entry['path']}")
                    _atomic_bytes(work / f"{index}.before", saved)
                if entry["after"] is not None:
                    file = calculation["payloads"].get(entry["path"])
                    if file is None:
                        raise KoraError(f"No hay payload para actualizar: {entry['path']}")
                    _atomic_bytes(work / f"{index}.after", file.data,
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
            # The first pass catches edits between the read-only calculation
            # and staging. A preserved residue deliberately uses its captured
            # descriptor as the live expectation.
            for entry in entries:
                expected = entry.get("preserved", entry["before"])
                if self._current(entry["path"]) != expected:
                    raise KoraError(f"Se detectó cambio local durante preparación: {entry['path']}")
            for entry in entries:
                expected = entry.get("preserved", entry["before"])
                if self._current(entry["path"]) != expected:
                    raise KoraError(f"Se detectó cambio local durante instalación: {entry['path']}")
                self._run(journal, entry, entry["forward"])
                if self._captured(journal, entry["forward"]):
                    slot = self._slot(journal, entry["forward"])
                    captured_expected = entry.get("preserved", entry["before"])
                    if _file_info(slot) != captured_expected:
                        raise KoraError(f"Se conservó cambio local concurrente: {entry['path']}; objeto: {slot}")
            _json_write(self.state_file, after_state)
            journal["status"] = "committed"
            self._save(journal)
        except Exception:
            self._restore(journal)
            raise
        return {"changed": [e["path"] for e in entries], "transaction": transaction}

    def prepare(self, bundles: dict[str, dict[str, File]], remove=(), adopt=None,
                patches=None, context=None):
        """Return a deterministic plan without creating or writing installer state."""
        return self._calculate(bundles, remove=remove, adopt=adopt,
                               patches=patches, context=context)["plan"]

    def apply(self, bundles: dict[str, dict[str, File]], remove=(), adopt=None,
              patches=None, context=None, plan=None, validate=None):
        """Apply one prepared calculation while preserving journal v2 recovery."""
        with self._lock():
            self._recover_locked()
            calculation = self._calculate(bundles, remove=remove, adopt=adopt,
                                           patches=patches, context=context)
            if plan is not None:
                self._assert_same_plan(plan, calculation["plan"])
            if not calculation["plan"]["ok"]:
                self._execute(calculation)
            if validate is not None:
                self._invoke_validate(validate, calculation["plan"])

            # Re-read receipt and relevant destinations after source
            # revalidation. This is the stale-plan gate immediately before any
            # staging or live rename.
            refreshed = self._calculate(bundles, remove=remove, adopt=adopt,
                                         patches=patches, context=context)
            self._assert_same_plan(calculation["plan"], refreshed["plan"])
            if not refreshed["plan"]["ok"]:
                self._execute(refreshed)
            significant = bool(refreshed["entries"] or refreshed["plan"]["ownership"])
            if significant and validate is not None:
                self._invoke_validate(validate, refreshed["plan"])
                final = self._calculate(bundles, remove=remove, adopt=adopt,
                                        patches=patches, context=context)
                self._assert_same_plan(refreshed["plan"], final["plan"])
                calculation = final
            else:
                calculation = refreshed
            if not calculation["plan"]["ok"]:
                self._execute(calculation)
            self._check_runtime_preconditions(calculation)
            return self._execute(calculation)

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
        state = self.receipts()
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
                preservation = entry.get("preservation")
                if preservation is not None:
                    step = entry.get("forward")
                    if step is not None and self._captured(transaction, step):
                        slot = self._slot(transaction, step)
                        try:
                            actual = _file_info(slot)
                        except KoraError:
                            actual = None
                        # A residue is an intentional preservation event. It
                        # remains visible even when the captured slot still
                        # matches the actual descriptor recorded at capture.
                        preserved_changes.append({
                            "path": entry["path"],
                            "backup": str(slot.relative_to(self.home)),
                            "transaction": transaction["transaction"],
                            "reason": preservation["reason"],
                            "expected": preservation["expected"],
                            "actual": actual,
                            "preserved": True,
                        })
                    continue
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
