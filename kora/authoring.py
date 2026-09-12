"""Create authored knowledge, skills and agents with recoverable original sources."""

from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import os
from pathlib import Path
import re
import shutil
import stat
import tempfile
import uuid

import yaml

from .catalog import Catalog, KoraError, Product, digest, read_product, read_yaml, safe_relative
from .atomic import exchange, rename_new


@contextmanager
def _author_lock(root):
    root.mkdir(parents=True, exist_ok=True)
    fd = os.open(root, os.O_RDONLY | os.O_DIRECTORY)
    try:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise KoraError("Hay otra autoría en curso para esta raíz; vuelve a intentar al terminar") from error
        yield
    finally:
        os.close(fd)


def _check_publication_path(root, destination):
    for path in (destination, *destination.parents):
        if path == root:
            break
        if path.is_symlink():
            raise KoraError(f"La publicación atraviesa un enlace: {path}")
        if path.exists() and (path == destination or not path.is_dir()):
            raise KoraError(f"El destino contiene trabajo existente: {path}")


def create(root: Path, kind: str, namespace: str, name: str, identifier: str,
           description: str, body: Path, *, sources=(), targets=(), requires=(), knowledge=None,
           candidate=None) -> Product:
    root = Path(root).resolve()
    # Knowledge has a separate publication lifecycle owned by knowledge.py.
    # Keep this branch byte-compatible because create_draft() uses it to stage
    # a knowledge source before adding its own metadata.
    if kind == "knowledge":
        with _author_lock(root):
            return _create(root, kind, namespace, name, identifier, description, body,
                           sources=sources, targets=targets, requires=requires, knowledge=knowledge)

    prepared = prepare(root, kind, namespace, name, identifier, description, body,
                       sources=sources, targets=targets, requires=requires,
                       knowledge=knowledge, candidate=candidate)
    token = prepared.directory.parent.name
    report = review(root, prepared.id, candidate=token, knowledge=knowledge)
    if not report["realizable"]:
        message = "; ".join(report["errors"]) or "la candidata no es realizable"
        raise KoraError(f"No se puede admitir {prepared.id}; candidata conservada: {message}")
    return admit(root, prepared.id, report["reviewed_sha256"], candidate=token, knowledge=knowledge)


def _create(root, kind, namespace, name, identifier, description, body, *, sources, targets, requires, knowledge=None):
    if kind not in ("knowledge", "skill", "agent"):
        raise KoraError(f"Tipo desconocido: {kind}")
    if len(safe_relative(namespace).parts) != 1 or len(safe_relative(name).parts) != 1:
        raise KoraError("Namespace y nombre deben ser componentes únicos")
    destination = root / "products" / namespace / name
    _check_publication_path(root, destination)
    catalog = Catalog(root, knowledge=knowledge)
    if identifier in catalog.products or identifier in catalog.archived or identifier in catalog.aliases:
        raise KoraError(f"La identidad ya existe: {identifier}")
    for identifier_needed in requires:
        catalog.get(identifier_needed)
    metadata = {"id": identifier, "kind": kind, "name": name,
                "description": description, "content": "content.md"}
    if kind != "knowledge":
        metadata["targets"] = list(targets) if targets else ["codex", "hermes"]
    if requires:
        metadata["requires"] = list(requires)
    root.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=".kora-author-", dir=root))
    staged = temporary / "products" / namespace / name
    staged.mkdir(parents=True)
    try:
        (staged / "content.md").write_bytes(Path(body).read_bytes())
        source_entries = []
        for index, source in enumerate(sources):
            source = Path(source).resolve()
            data = source.read_bytes()
            relative = f"sources/{index + 1}-{source.name}"
            target = staged / safe_relative(relative)
            target.parent.mkdir(exist_ok=True)
            target.write_bytes(data)
            source_entries.append({"path": relative, "sha256": digest(data), "origin": str(source)})
        if source_entries:
            metadata["provenance"] = {"sources": source_entries}
        (staged / "object.yaml").write_text(yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False), encoding="utf-8")
        # Exercise the same source reader used by realization before publishing the directory.
        candidate = Catalog(temporary).get(identifier)
        catalog.products[identifier] = candidate
        for target in candidate.targets:
            catalog.dependencies(candidate, target)
        destination.parent.mkdir(parents=True, exist_ok=True)
        _check_publication_path(root, destination)
        try:
            rename_new(staged, destination)
        except FileExistsError as error:
            raise KoraError(f"El producto apareció durante la autoría: {destination}") from error
        return Product(destination, metadata)
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)


# Product candidates deliberately have their own namespace.  Catalog only
# discovers products and archived products, so a prepared candidate cannot be
# mistaken for an active source by ordinary resolution.
_CANDIDATE_ROOT = "candidates"
_STATE_NAME = "state.yaml"
_REVISION = re.compile(r"[0-9a-f]{64}\Z")


def _one_component(value, label):
    if not isinstance(value, str):
        raise KoraError(f"{label} debe ser texto")
    try:
        path = safe_relative(value)
    except KoraError as error:
        raise KoraError(f"{label} inválido: {value!r}") from error
    if len(path.parts) != 1 or value.startswith("."):
        raise KoraError(f"{label} debe ser un componente único")
    return path.name


def _candidate_component(value):
    if isinstance(value, Product):
        value = value.directory.parent.name
    elif isinstance(value, Path):
        value = value.parent.name if value.name == "product" else value.name
    elif isinstance(value, str) and ("/" in value or "\\" in value):
        path = Path(value)
        value = path.parent.name if path.name == "product" else path.name
    return _one_component(value, "candidate")


def _candidate_scope(root, namespace, name, candidate):
    return (Path(root).resolve() / _CANDIDATE_ROOT / namespace / name / candidate)


def _assert_private_path(root, path):
    """Check sidecar/temporary parents without requiring the final path to exist."""
    root = Path(root).resolve()
    path = Path(path)
    try:
        path.absolute().relative_to(root)
    except ValueError as error:
        raise KoraError(f"La ruta queda fuera de la raíz: {path}") from error
    for node in (path.parent, *path.parent.parents):
        if node == root:
            break
        if node.is_symlink():
            raise KoraError(f"La operación atraviesa un enlace: {node}")
        if node.exists() and not node.is_dir():
            raise KoraError(f"La operación atraviesa un archivo: {node}")


def _write_yaml(path, value, *, root=None):
    path = Path(path)
    if root is not None:
        _assert_private_path(root, path)
    path.parent.mkdir(parents=True, exist_ok=True)
    old_mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o644
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(temporary)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            stream.write(yaml.safe_dump(value, allow_unicode=True, sort_keys=False))
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(temporary, old_mode)
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def _new_candidate_name():
    return "candidate-" + uuid.uuid4().hex


def _candidate_state(candidate_directory):
    path = Path(candidate_directory) / _STATE_NAME
    if path.is_symlink():
        raise KoraError(f"El estado de candidata es un enlace: {path}")
    if not path.exists():
        return {}
    state = read_yaml(path)
    if not isinstance(state, dict):
        raise KoraError(f"El estado de candidata debe ser un mapa: {path}")
    return state


def _save_candidate_state(root, record, changes):
    state = dict(record.get("state", {}))
    state.update(changes)
    state.setdefault("id", record["product"].id)
    state.setdefault("candidate", record["candidate"])
    state.setdefault("namespace", record["namespace"])
    state.setdefault("name", record["name"])
    path = record["directory"] / _STATE_NAME
    _write_yaml(path, state, root=root)
    record["state"] = state
    return state


def _candidate_records(root, identifier=None):
    root = Path(root).resolve()
    container = root / _CANDIDATE_ROOT
    if not container.exists():
        return []
    if container.is_symlink() or not container.is_dir():
        raise KoraError(f"La raíz de candidatas no es un directorio propio: {container}")
    records = []
    for namespace_path in sorted(container.iterdir()):
        if namespace_path.is_symlink() or not namespace_path.is_dir():
            raise KoraError(f"Namespace de candidata inválido: {namespace_path}")
        for name_path in sorted(namespace_path.iterdir()):
            if name_path.is_symlink() or not name_path.is_dir():
                raise KoraError(f"Nombre de candidata inválido: {name_path}")
            for candidate_path in sorted(name_path.iterdir()):
                if candidate_path.is_symlink() or not candidate_path.is_dir():
                    raise KoraError(f"Candidata inválida: {candidate_path}")
                product_path = candidate_path / "product"
                if product_path.is_symlink() or not product_path.is_dir():
                    raise KoraError(f"Producto de candidata ausente o enlazado: {product_path}")
                try:
                    item = read_product(product_path)
                except KoraError:
                    # A malformed candidate is still addressable by its
                    # explicit path; for identity lookup it cannot be safely
                    # attributed and therefore is not silently guessed.
                    if identifier is not None:
                        continue
                    raise
                if identifier is not None and item.id != identifier:
                    continue
                try:
                    candidate = _one_component(candidate_path.name, "candidate")
                    namespace = _one_component(namespace_path.name, "namespace")
                    name = _one_component(name_path.name, "name")
                except KoraError:
                    raise
                records.append({"product": item, "directory": candidate_path,
                                "candidate": candidate, "namespace": namespace,
                                "name": name, "state": _candidate_state(candidate_path)})
    return records


def _canonical_id(root, identifier, knowledge=None):
    try:
        catalog = Catalog(root, knowledge=knowledge, strict=False)
        return catalog.get(identifier).id
    except KoraError:
        return identifier


def _find_candidate(root, identifier, candidate=None, knowledge=None):
    canonical = _canonical_id(root, identifier, knowledge)
    records = _candidate_records(root, canonical)
    if candidate is not None:
        requested_path = None
        if isinstance(candidate, Product):
            requested_path = Path(candidate.directory).absolute()
        elif isinstance(candidate, Path):
            requested_path = (candidate / "product" if candidate.name != "product" else candidate).absolute()
        elif isinstance(candidate, str) and ("/" in candidate or "\\" in candidate):
            path = Path(candidate)
            requested_path = (path / "product" if path.name != "product" else path).absolute()
        if requested_path is not None:
            records = [record for record in records
                       if Path(record["product"].directory).absolute() == requested_path]
        else:
            token = _candidate_component(candidate)
            records = [record for record in records if record["candidate"] == token]
    if not records:
        qualifier = f" candidata {candidate!r}" if candidate is not None else ""
        raise KoraError(f"No se encontró{qualifier} para {identifier}")
    if len(records) > 1:
        choices = ", ".join(record["candidate"] for record in records)
        raise KoraError(f"Hay varias candidatas para {identifier}; indica --candidate: {choices}")
    record = records[0]
    if record["product"].id != canonical:
        raise KoraError(f"La candidata no conserva la identidad solicitada: {identifier}")
    return record


def _candidate_metadata(kind, namespace, name, identifier, description, targets, requires, sources):
    metadata = {"id": identifier, "kind": kind, "name": name,
                "description": description, "content": "content.md",
                "targets": list(targets) if targets else ["codex", "hermes"]}
    if requires:
        metadata["requires"] = list(requires)
    if sources:
        metadata["provenance"] = {"sources": sources}
    return metadata


def _read_source_file(source):
    """Read one input source once so its metadata and copied bytes agree."""
    source = Path(source)
    try:
        data = source.read_bytes()
        mode = stat.S_IMODE(source.stat().st_mode)
    except (OSError, ValueError) as error:
        raise KoraError(f"No se pudo leer la fuente: {source}") from error
    return source, data, mode


def _copy_source_file(source, destination, *, data=None, mode=None):
    """Copy a source snapshot, retaining the captured bytes and mode."""
    if data is None or mode is None:
        source, data, mode = _read_source_file(source)
    source = Path(source)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(data)
    os.chmod(destination, mode)


def _publish_candidate(root, staged, destination):
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    _check_publication_path(root, destination)
    try:
        rename_new(staged, destination)
    except FileExistsError as error:
        raise KoraError(f"La candidata apareció durante la preparación: {destination}") from error


def prepare(root: Path, kind: str, namespace: str, name: str, identifier: str,
            description: str, body: Path, sources=(), targets=(), requires=(),
            knowledge=None, candidate=None) -> Product:
    """Materialize a machine-product candidate without changing active products."""
    root = Path(root).resolve()
    if kind not in ("skill", "agent"):
        raise KoraError("prepare solo admite agentes y skills; conocimiento usa knowledge.create_draft")
    namespace = _one_component(namespace, "namespace")
    name = _one_component(name, "name")
    if not isinstance(identifier, str) or not identifier.strip():
        raise KoraError("La identidad debe ser texto no vacío")
    if not isinstance(description, str):
        raise KoraError("La descripción debe ser texto")
    try:
        body = Path(body)
        body_data = body.read_bytes()
        body_mode = stat.S_IMODE(body.stat().st_mode)
    except (OSError, TypeError) as error:
        raise KoraError(f"No se pudo leer el cuerpo: {body}") from error
    sources = list(sources or ())
    source_entries = []
    source_snapshots = []
    for index, source in enumerate(sources, 1):
        source_path, source_data, source_mode = _read_source_file(source)
        relative = f"sources/{index}-{source_path.name}"
        source_entries.append({"path": relative, "sha256": digest(source_data),
                               "origin": str(source_path.resolve())})
        source_snapshots.append((source_path, source_data, source_mode))

    with _author_lock(root):
        catalog = Catalog(root, knowledge=knowledge, strict=False)
        if identifier in catalog.products or identifier in catalog.archived or identifier in catalog.aliases:
            raise KoraError(f"La identidad ya existe: {identifier}; usa revise para preparar una edición")
        if identifier in catalog._blocked:
            raise KoraError(f"La identidad está defectuosa o es ambigua: {identifier}")
        token = _candidate_component(candidate) if candidate is not None else _new_candidate_name()
        destination = _candidate_scope(root, namespace, name, token)
        temporary = Path(tempfile.mkdtemp(prefix=".kora-candidate-", dir=root))
        staged = temporary / "candidate"
        product_path = staged / "product"
        try:
            product_path.mkdir(parents=True)
            metadata = _candidate_metadata(kind, namespace, name, identifier, description,
                                           targets, requires, source_entries)
            (product_path / "content.md").write_bytes(body_data)
            os.chmod(product_path / "content.md", body_mode)
            for index, (source, source_data, source_mode) in enumerate(source_snapshots, 1):
                _copy_source_file(
                    source, product_path / f"sources/{index}-{source.name}",
                    data=source_data, mode=source_mode
                )
            (product_path / "object.yaml").write_text(
                yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False), encoding="utf-8"
            )
            formal_error = None
            try:
                item = read_product(product_path)
            except KoraError as error:
                # A malformed candidate is still useful authored work.  Keep
                # its body, manifest and exact diagnostic in the candidate
                # area so the caller can repair it without losing the input.
                formal_error = error
                item = None
            base_residue = None
            if formal_error is None:
                try:
                    from .product_versions import residue_digest
                    base_residue = residue_digest(item)
                except KoraError as error:
                    # Links and special files are rejected even when they sit
                    # under a path that would otherwise be operational
                    # residue.  Preserve that diagnostic with the candidate.
                    formal_error = error
            formal_message = None
            if formal_error is not None:
                # The parser saw the private staging path.  Persist the
                # candidate location in the diagnostic instead of leaving a
                # pointer to a directory that the cleanup below will remove.
                formal_message = str(formal_error).replace(
                    str(product_path), str(destination / "product")
                )
            state = {"id": identifier, "kind": kind, "namespace": namespace, "name": name,
                     "candidate": token, "base": None, "base_revision": None,
                     "base_residue": base_residue,
                     "status": "failed" if formal_error else "prepared",
                     "reviewed_sha256": None,
                     "realizable": False if formal_error else None,
                     "errors": [formal_message] if formal_error else [],
                     "diagnostics": ([{"target": None, "error": formal_message}]
                                     if formal_error else [])}
            _write_yaml(staged / _STATE_NAME, state)
            _publish_candidate(root, staged, destination)
            if formal_error is not None:
                raise KoraError(
                    f"Candidata conservada en {destination}: {formal_message}"
                ) from formal_error
            return read_product(destination / "product")
        finally:
            if temporary.exists():
                shutil.rmtree(temporary)


def _validate_candidate(root, item, knowledge=None):
    """Validate native contracts against a temporary overlay catalog.

    Calling renderer internals inside one catalog phase is intentional.  The
    public renderers revalidate their catalog against the on-disk active tree;
    doing that for a candidate would reject the very overlay being examined.
    Dependencies are then checked explicitly on the same captured objects.
    """
    errors = []
    diagnostics = []
    realizable = {}
    provenance_errors, provenance_diagnostics = _provenance_issues(item)
    errors.extend(provenance_errors)
    diagnostics.extend(provenance_diagnostics)
    if not item.targets:
        errors.append(f"{item.id}: no declara destinos de realización")
        return False, realizable, errors, diagnostics
    try:
        overlay = Catalog(root, knowledge=knowledge, strict=False)
        overlay.products[item.id] = item
        overlay.archived.pop(item.id, None)
    except (KoraError, OSError) as error:
        message = str(error)
        errors.append(message)
        return False, realizable, errors, diagnostics

    try:
        with overlay.phase():
            captured = overlay.capture(item)
            for target in item.targets:
                target_errors = []
                try:
                    if target == "codex":
                        from .render_codex import _render as native_render
                    elif target == "hermes":
                        from .render_hermes import _render as native_render
                    else:
                        raise KoraError(f"Destino desconocido: {target}")
                    native_render(overlay, captured)
                    # Keep this explicit even though renderers also traverse
                    # dependencies; it makes the acceptance boundary clear.
                    overlay.dependencies(captured, target)
                except (KoraError, ValueError, TypeError, OSError) as error:
                    target_errors.append(str(error))
                realizable[target] = not target_errors
                for message in target_errors:
                    diagnostics.append({"target": target, "error": message})
                    errors.append(f"{target}: {message}")
            overlay.revalidate(candidate=item)
    except (KoraError, ValueError, TypeError, OSError) as error:
        message = str(error)
        errors.append(message)
        diagnostics.append({"target": None, "error": message})
    return not errors, realizable, errors, diagnostics


def _dependency_context(root, item, knowledge=None):
    """Capture the dependency resolution that admission must keep stable.

    ``Catalog.revalidate`` quite correctly expects every captured product to
    already be active.  A candidate is deliberately absent from the active
    catalog, so admission uses this smaller equivalent context: the candidate
    is overlaid only while traversing its native dependency closure, while
    every actual provider is recorded from the discovered catalog.  A second
    call just before the exchange catches changes to providers, aliases or
    resolution diagnostics without pretending the candidate was published.
    """
    from .product_versions import source_digest

    overlay = Catalog(root, knowledge=knowledge, strict=False)
    overlay.products[item.id] = item
    overlay.archived.pop(item.id, None)

    def product_context(product):
        context = {
            "id": product.id,
            "kind": product.kind,
            "name": product.name,
            "directory": str(Path(product.directory).absolute()),
            "revision": product.revision,
            "fingerprint": product.fingerprint(
                portable=False, legacy_modes=product.legacy_modes
            ),
        }
        if product.kind != "knowledge":
            context["source_digest"] = source_digest(product)
        return context

    dependencies = {}
    with overlay.phase():
        captured = overlay.capture(item)
        for target in item.targets:
            dependencies[target] = sorted(
                (product_context(product)
                 for product in overlay.dependencies(captured, target)),
                key=lambda product: (product["id"], product["directory"],
                                     product["revision"] or ""),
            )

    aliases = tuple(sorted(
        ((repr(alias), repr(target)) for alias, target in overlay.aliases.items()),
        key=lambda pair: pair[0],
    ))
    blocked = tuple(sorted(
        ((repr(identifier), tuple(issue.get("error", "") for issue in issues))
         for identifier, issues in overlay._blocked.items()),
        key=lambda pair: pair[0],
    ))
    return {"aliases": aliases, "blocked": blocked, "dependencies": dependencies}


def _provenance_issues(item):
    errors = []
    diagnostics = []
    provenance = item.metadata.get("provenance", {})
    if provenance is None:
        return errors, diagnostics
    if not isinstance(provenance, dict):
        message = "La procedencia debe ser un mapa"
        return [message], [{"target": None, "error": message}]
    sources = provenance.get("sources", [])
    if sources is None:
        return errors, diagnostics
    if not isinstance(sources, list):
        message = "La procedencia.sources debe ser una lista"
        return [message], [{"target": None, "error": message}]
    seen = set()
    for index, source in enumerate(sources, 1):
        try:
            if not isinstance(source, dict):
                raise KoraError(f"Procedencia inválida en la fuente {index}")
            relative = source["path"]
            expected = source["sha256"]
            if not isinstance(relative, str) or not isinstance(expected, str):
                raise KoraError(f"Procedencia inválida en la fuente {index}")
            if not _REVISION.fullmatch(expected):
                raise KoraError(f"Hash de procedencia inválido: {relative}")
            relative_path = safe_relative(relative)
            normalized = relative_path.as_posix()
            if normalized in seen:
                raise KoraError(f"Ruta de procedencia duplicada: {relative}")
            seen.add(normalized)
            source_path = item.directory / relative_path
            if (source_path.is_symlink() or not source_path.is_file()
                    or digest(source_path.read_bytes()) != expected):
                raise KoraError(f"Original modificado: {relative}")
        except (KeyError, TypeError, OSError, KoraError) as error:
            message = str(error)
            errors.append(message)
            diagnostics.append({"target": None, "error": message})
    return errors, diagnostics


def _report_for_candidate(root, record, knowledge=None):
    item = record["product"]
    previous_status = record["state"].get("status", "prepared")
    errors = []
    diagnostics = []
    try:
        from .product_versions import source_digest
        reviewed = source_digest(item)
    except KoraError as error:
        reviewed = None
        errors.append(str(error))
        diagnostics.append({"target": None, "error": str(error)})
    if reviewed is not None:
        valid, realizable_targets, validation_errors, validation_diagnostics = _validate_candidate(
            root, item, knowledge=knowledge
        )
        errors.extend(validation_errors)
        diagnostics.extend(validation_diagnostics)
        valid = valid and not errors
    else:
        valid, realizable_targets = False, {}
    persisted_status = (previous_status if previous_status in {"admitting", "admitted"}
                        else ("reviewed" if valid else "failed"))
    report = {
        "id": item.id,
        "kind": item.kind,
        "candidate": record["candidate"],
        "path": str(item.content_path),
        "metadata": str(item.directory / "object.yaml"),
        "reviewed_sha256": reviewed,
        "base": record["state"].get("base_revision", record["state"].get("base")),
        "base_revision": record["state"].get("base_revision", record["state"].get("base")),
        "base_residue": record["state"].get("base_residue"),
        "realizable": valid,
        "realizable_targets": realizable_targets,
        "errors": errors,
        "diagnostics": diagnostics,
        "targets": list(item.targets),
        "requires": list(item.requires),
        "state": persisted_status,
        "candidate_path": str(record["directory"]),
        "staged_path": record["state"].get("staged_path"),
        "displaced_path": record["state"].get("displaced_path"),
        "publication": "candidate",
    }
    _save_candidate_state(root, record, {
        "status": persisted_status,
        "reviewed_sha256": reviewed,
        "realizable": valid,
        "realizable_targets": realizable_targets,
        "errors": errors,
        "diagnostics": diagnostics,
    })
    return report


def review(root: Path, identifier: str, candidate=None, knowledge=None) -> dict:
    """Review a candidate and persist its exact diagnostic outside the product."""
    root = Path(root).resolve()
    with _author_lock(root):
        record = _find_candidate(root, identifier, candidate=candidate, knowledge=knowledge)
        return _report_for_candidate(root, record, knowledge=knowledge)


def _failure(root, record, message, *, reviewed=None, diagnostics=None):
    errors = [message]
    _save_candidate_state(root, record, {
        "status": "failed", "reviewed_sha256": reviewed,
        "realizable": False, "errors": errors,
        "diagnostics": diagnostics or [{"target": None, "error": message}],
        "staged_path": None,
    })


def _active_revision(product):
    from .product_versions import source_digest, verify
    if product.revision is not None:
        verify(product)
        return product.revision
    return source_digest(product)


def _destination_for_record(root, record):
    return Path(root).resolve() / "products" / record["namespace"] / record["name"]


def _displace_old_source(record, staged, displaced=None):
    """Keep the directory displaced by an exchange for late writers/recovery."""
    if displaced is None:
        displaced = record["directory"] / ("displaced-" + uuid.uuid4().hex)
    displaced = Path(displaced)
    _assert_private_path(record["directory"].parents[3], displaced)
    try:
        rename_new(staged, displaced)
    except FileExistsError:
        # UUID collisions are not expected, but retrying keeps this path
        # recoverable without replacing another preserved directory.
        if displaced.name.startswith("displaced-recovery-"):
            raise
        displaced = record["directory"] / ("displaced-" + uuid.uuid4().hex)
        rename_new(staged, displaced)
    return displaced


def _recover_admission(root, record, active, reviewed, expected_base, expected_residue=None):
    """Complete an exchange whose final state write was interrupted.

    The candidate state records both the temporary staged directory and the
    permanent displaced location before exchanging the active name.  A retry
    can therefore finish moving the old source without treating the already
    visible reviewed revision as a stale candidate.
    """
    from .product_versions import at_revision, residue_matches, source_digest, verify

    destination = _destination_for_record(root, record)
    if Path(active.directory).absolute() != destination.absolute():
        raise KoraError(f"La admisión recuperada está en una ubicación inesperada: {destination}")
    if source_digest(active) != reviewed:
        raise KoraError(f"La fuente activa no corresponde a la admisión revisada: {active.id}")
    # Confirm the immutable snapshot before changing any recovery locator.
    at_revision(root, active, reviewed)
    if expected_residue is not None:
        candidate_residue_matches = residue_matches(record["product"], expected_residue)
        if not candidate_residue_matches:
            raise KoraError(
                "La candidata cambió en archivos operacionales desde la revisión; "
                "conserva los cambios y prepara otra candidata desde la fuente vigente"
            )
    state = record.get("state", {})
    staged_value = state.get("staged_path")
    displaced_value = state.get("displaced_path")
    staged = Path(staged_value) if isinstance(staged_value, str) and staged_value else None
    displaced = Path(displaced_value) if isinstance(displaced_value, str) and displaced_value else None
    if staged is not None:
        _assert_private_path(root, staged)
        if staged.absolute() == destination.absolute():
            raise KoraError("El staging de admisión coincide con la fuente activa")
        if staged.exists() and (staged.is_symlink() or not staged.is_dir()):
            raise KoraError(f"El staging de admisión no es un directorio propio: {staged}")
    if displaced is not None:
        _assert_private_path(root, displaced)
        if displaced.absolute() == destination.absolute():
            raise KoraError("El desplazamiento de admisión coincide con la fuente activa")
        if displaced.exists() and (displaced.is_symlink() or not displaced.is_dir()):
            raise KoraError(f"El desplazamiento de admisión no es un directorio propio: {displaced}")

    if staged is not None and staged.exists():
        if displaced is None:
            displaced = record["directory"] / ("displaced-recovered-" + uuid.uuid4().hex)
            _assert_private_path(root, displaced)
        if displaced.exists():
            raise KoraError(f"Staging y desplazamiento de admisión existen a la vez: {staged}")
        rename_new(staged, displaced)
    elif expected_base is not None and (displaced is None or not displaced.exists()):
        # An update must retain the old source directory.  Its immutable
        # snapshot is still available, but a missing live locator means the
        # interrupted exchange cannot be completed safely.
        raise KoraError("La admisión recuperada perdió el directorio activo desplazado")

    changes = {
        "status": "admitted", "reviewed_sha256": reviewed,
        "realizable": True, "revision": reviewed,
        "previous_revision": expected_base, "staged_path": None,
        "recovered": True,
    }
    if displaced is not None:
        changes["displaced_path"] = str(displaced)
    _save_candidate_state(root, record, changes)
    admitted = read_product(destination, revision=reviewed)
    verify(admitted)
    return admitted


def admit(root: Path, identifier: str, reviewed: str, candidate=None, knowledge=None) -> Product:
    """Admit a reviewed candidate after base and native validations still match."""
    root = Path(root).resolve()
    with _author_lock(root):
        record = _find_candidate(root, identifier, candidate=candidate, knowledge=knowledge)
        item = record["product"]
        from .product_versions import (preserve, residue_matches, source_digest,
                                       verify, _copy_source_tree)
        if not isinstance(reviewed, str) or not _REVISION.fullmatch(reviewed):
            message = "La revisión aprobada debe ser un SHA-256 completo"
            _failure(root, record, message)
            raise KoraError(message)
        try:
            actual = source_digest(item)
        except KoraError as error:
            _failure(root, record, str(error), reviewed=reviewed)
            raise
        if actual != reviewed:
            message = "La candidata cambió desde la revisión; vuelve a revisar el contenido"
            _failure(root, record, message, reviewed=actual)
            raise KoraError(message)

        expected_base = record["state"].get("base_revision", record["state"].get("base"))
        expected_residue = record["state"].get("base_residue")
        lifecycle_status = record["state"].get("status")
        catalog = Catalog(root, knowledge=knowledge, strict=False)
        active = catalog.products.get(item.id)
        if active is None and item.id in catalog.archived:
            message = f"La identidad está retirada: {item.id}"
            _failure(root, record, message, reviewed=actual)
            raise KoraError(message)
        # A previous process may have exchanged the active name and then
        # stopped before its final state write.  An exact active hash plus a
        # valid immutable snapshot is an effective admission, not a stale
        # candidate; recovery can finish the displaced-directory locator.
        if active is not None and lifecycle_status in {"admitting", "admitted"}:
            current_base = _active_revision(active)
            if current_base == actual and current_base != expected_base:
                return _recover_admission(
                    root, record, active, actual, expected_base, expected_residue
                )

        # ``source_digest`` intentionally ignores operational residue.  Keep
        # a separate state stamp so a late edit to a private/temporary file cannot
        # be overwritten by an admission prepared from an older active tree.
        # During recovery the active tree is already the new selected source;
        # _recover_admission validates the candidate and its snapshot instead.
        if expected_residue is not None:
            try:
                candidate_residue_matches = residue_matches(item, expected_residue)
                active_residue_matches = residue_matches(active, expected_residue) if active is not None else True
            except KoraError as error:
                _failure(root, record, str(error), reviewed=actual)
                raise
            if not candidate_residue_matches:
                message = (
                    "La candidata cambió en archivos operacionales desde la preparación; "
                    "conserva los cambios y prepara otra candidata desde la fuente vigente"
                )
                _failure(root, record, message, reviewed=actual)
                raise KoraError(message)
            if not active_residue_matches:
                message = (
                    "La fuente activa cambió en archivos operacionales desde la preparación; "
                    "se conserva la candidata y el trabajo local"
                )
                _failure(root, record, message, reviewed=actual)
                raise KoraError(message)

        valid, _, errors, diagnostics = _validate_candidate(root, item, knowledge=knowledge)
        if not valid:
            message = "; ".join(errors) or "La candidata no es realizable en sus destinos"
            _failure(root, record, message, reviewed=actual, diagnostics=diagnostics)
            raise KoraError(message)

        current_base = _active_revision(active) if active is not None else None
        if current_base != expected_base:
            message = (f"La fuente activa cambió desde la preparación de {item.id}; "
                       f"base esperada {expected_base}, actual {current_base}")
            _failure(root, record, message, reviewed=actual)
            raise KoraError(message)

        destination = _destination_for_record(root, record)
        if active is not None and Path(active.directory).absolute() != destination.absolute():
            message = f"La fuente activa no coincide con la ubicación esperada: {destination}"
            _failure(root, record, message, reviewed=actual)
            raise KoraError(message)
        if destination.exists() and active is None:
            message = f"El destino contiene una identidad activa: {destination}"
            _failure(root, record, message, reviewed=actual)
            raise KoraError(message)

        # Both source snapshots are complete before the reader-visible exchange.
        old_revision = preserve(root, active) if active is not None else None
        new_revision = preserve(root, item)
        if new_revision != actual:
            message = "La candidata cambió mientras se conservaba la revisión; vuelve a revisar el contenido"
            _failure(root, record, message, reviewed=new_revision)
            raise KoraError(message)
        temporary = Path(tempfile.mkdtemp(prefix=".kora-admit-", dir=root))
        staged = temporary / "product"
        displaced = None
        if active is not None:
            displaced = record["directory"] / ("displaced-" + uuid.uuid4().hex)
            _assert_private_path(root, displaced)
        published = False
        keep_temporary = False
        try:
            _copy_source_tree(item, staged)
            staged_item = read_product(staged, revision=new_revision)
            if source_digest(staged_item) != new_revision:
                raise KoraError(f"La fuente cambió al preparar la admisión de {item.id}")
            # Re-open both sides immediately before exchanging names.  The
            # initial review/base check is intentionally insufficient: a
            # dependency, alias, candidate, or active source may have changed
            # while snapshots and the staged copy were being prepared.
            fresh_dependency_context = _dependency_context(
                root, item, knowledge=knowledge
            )
            fresh_valid, _, fresh_errors, fresh_diagnostics = _validate_candidate(
                root, item, knowledge=knowledge
            )
            if source_digest(item) != actual:
                raise KoraError("La candidata cambió antes de la admisión; vuelve a revisar el contenido")
            if expected_residue is not None and not residue_matches(item, expected_residue):
                raise KoraError(
                    "La candidata cambió en archivos operacionales antes de la admisión; "
                    "conserva los cambios y prepara otra candidata desde la fuente vigente"
                )
            if not fresh_valid:
                raise KoraError("; ".join(fresh_errors) or "La candidata dejó de ser realizable")
            if destination.exists():
                if destination.is_symlink() or not destination.is_dir():
                    raise KoraError(f"El destino de admisión no es un directorio propio: {destination}")
                fresh_active = read_product(destination)
                if fresh_active.id != item.id:
                    raise KoraError(f"El destino pertenece a otra identidad: {destination}")
                fresh_base = _active_revision(fresh_active)
                if fresh_base != expected_base:
                    raise KoraError(
                        f"La fuente activa cambió antes de la admisión; base esperada {expected_base}, actual {fresh_base}"
                    )
                if expected_residue is not None and not residue_matches(fresh_active, expected_residue):
                    raise KoraError(
                        "La fuente activa cambió en archivos operacionales antes de la admisión; "
                        "se conserva la candidata y el trabajo local"
                    )
            _save_candidate_state(root, record, {
                "status": "admitting", "reviewed_sha256": actual,
                "realizable": True, "revision": new_revision,
                "previous_revision": old_revision, "errors": [], "diagnostics": [],
                "staged_path": str(staged),
                "destination_path": str(destination),
                "displaced_path": str(displaced) if displaced is not None else None,
            })
            destination.parent.mkdir(parents=True, exist_ok=True)
            if active is not None:
                if not destination.exists():
                    raise KoraError(f"La fuente activa desapareció antes de la admisión: {destination}")
                if destination.is_symlink() or not destination.is_dir():
                    raise KoraError(f"El destino de admisión no es un directorio propio: {destination}")
                current = read_product(destination)
                if current.id != item.id:
                    raise KoraError(f"El destino pertenece a otra identidad: {destination}")
                current_base = _active_revision(current)
                if current_base != expected_base:
                    raise KoraError(
                        f"La fuente activa cambió antes del intercambio; base esperada {expected_base}, actual {current_base}"
                    )
                if expected_residue is not None and not residue_matches(current, expected_residue):
                    raise KoraError(
                        "La fuente activa cambió en archivos operacionales justo antes del intercambio; "
                        "se conserva la candidata y el trabajo local"
                    )
                # Recheck the candidate immediately before the effect.  The
                # staging tree was captured earlier, so a selected or
                # operational file edited during the last preflight must not
                # be admitted under the previous approval.
                if source_digest(item) != actual:
                    raise KoraError(
                        "La candidata cambió justo antes del intercambio; "
                        "vuelve a revisar el contenido"
                    )
                if expected_residue is not None and not residue_matches(item, expected_residue):
                    raise KoraError(
                        "La candidata cambió en archivos operacionales justo antes del intercambio; "
                        "conserva los cambios y prepara otra candidata desde la fuente vigente"
                    )
                if _dependency_context(root, item, knowledge=knowledge) != fresh_dependency_context:
                    raise KoraError(
                        "Las dependencias o alias cambiaron justo antes del intercambio; "
                        "vuelve a revisar la candidata"
                    )
                exchange(staged, destination)
                published = True
                # The active directory may have been edited between the
                # preflight and the exchange.  The exchanged name now points
                # at the candidate while ``staged`` holds precisely the
                # directory that would otherwise be discarded.  Check that
                # displaced directory before moving it; if it is late work,
                # swap the names back and leave the active edit in place.
                try:
                    displaced_active = read_product(staged)
                    displaced_revision = _active_revision(displaced_active)
                    if displaced_revision != expected_base:
                        raise KoraError(
                            f"La fuente activa cambió durante el intercambio; base esperada {expected_base}, actual {displaced_revision}"
                        )
                    if expected_residue is not None and not residue_matches(displaced_active, expected_residue):
                        raise KoraError(
                            "La fuente activa cambió en archivos operacionales durante el intercambio; "
                            "se conserva la candidata y el trabajo local"
                        )
                except (KoraError, OSError, shutil.Error):
                    try:
                        exchange(staged, destination)
                        published = False
                    except (KoraError, OSError, shutil.Error):
                        keep_temporary = True
                    raise
                displaced = _displace_old_source(record, staged, displaced)
                _save_candidate_state(root, record, {
                    "displaced_path": str(displaced),
                })
            else:
                _check_publication_path(root, destination)
                if source_digest(item) != actual:
                    raise KoraError(
                        "La candidata cambió justo antes de la admisión; "
                        "vuelve a revisar el contenido"
                    )
                if expected_residue is not None and not residue_matches(item, expected_residue):
                    raise KoraError(
                        "La candidata cambió en archivos operacionales justo antes de la admisión; "
                        "conserva los cambios y prepara otra candidata desde la fuente vigente"
                    )
                if _dependency_context(root, item, knowledge=knowledge) != fresh_dependency_context:
                    raise KoraError(
                        "Las dependencias o alias cambiaron justo antes de la admisión; "
                        "vuelve a revisar la candidata"
                    )
                rename_new(staged, destination)
                published = True
            _save_candidate_state(root, record, {
                "status": "admitted", "revision": new_revision,
                "previous_revision": old_revision,
                "staged_path": None,
                "displaced_path": str(displaced) if displaced is not None else None,
                "admitted_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            })
            admitted = read_product(destination, revision=new_revision)
            verify(admitted)
            return admitted
        except (KoraError, OSError, shutil.Error) as error:
            if not isinstance(error, KoraError):
                error = KoraError(str(error))
            if published:
                # The new source is already reader-visible. A state write or
                # displaced-directory move after that point must remain
                # recoverable as ``admitting`` rather than becoming a failed
                # candidate. Keep old staging if it was not moved yet.
                if staged.exists():
                    keep_temporary = True
            else:
                # If the exchange itself failed, the active destination
                # remains in place. Keep the candidate and its diagnostic for
                # a retry.
                _failure(root, record, str(error), reviewed=actual)
            raise error
        finally:
            if temporary.exists() and not keep_temporary:
                shutil.rmtree(temporary)


def revise(root: Path, identifier: str, candidate=None, knowledge=None) -> Product:
    """Copy the active agent or skill into a candidate based on its full revision."""
    root = Path(root).resolve()
    with _author_lock(root):
        catalog = Catalog(root, knowledge=knowledge, strict=False)
        try:
            active = catalog.get(identifier)
        except KoraError:
            raise
        if active.id not in catalog.products:
            raise KoraError(f"La identidad no está activa: {identifier}")
        if active.kind not in ("skill", "agent"):
            raise KoraError("revise de authoring solo admite agentes y skills")
        if Path(active.directory).absolute() != (root / "products" / active.directory.parent.name / active.directory.name).absolute():
            raise KoraError(f"La fuente activa tiene una ubicación no admitida: {active.directory}")
        from .product_versions import preserve, residue_digest
        base = preserve(root, active)
        base_residue = residue_digest(active)
        if candidate is not None:
            try:
                return _find_candidate(root, active.id, candidate=candidate, knowledge=knowledge)["product"]
            except KoraError as error:
                if "No se encontró" not in str(error):
                    raise
        token = _candidate_component(candidate) if candidate is not None else _new_candidate_name()
        destination = _candidate_scope(root, active.directory.parent.name, active.directory.name, token)
        temporary = Path(tempfile.mkdtemp(prefix=".kora-candidate-", dir=root))
        staged = temporary / "candidate"
        try:
            shutil.copytree(active.directory, staged / "product", symlinks=False, copy_function=shutil.copy2)
            state = {"id": active.id, "kind": active.kind,
                     "namespace": active.directory.parent.name, "name": active.directory.name,
                     "candidate": token, "base": base, "base_revision": base,
                     "base_residue": base_residue,
                     "status": "prepared", "reviewed_sha256": None,
                     "realizable": None, "errors": [], "diagnostics": []}
            _write_yaml(staged / _STATE_NAME, state)
            _publish_candidate(root, staged, destination)
            return read_product(destination / "product")
        finally:
            if temporary.exists():
                shutil.rmtree(temporary)


def _read_aliases(root):
    path = Path(root).resolve() / "aliases.yaml"
    if not path.exists():
        return {}
    if path.is_symlink():
        raise KoraError(f"aliases.yaml no puede ser un enlace: {path}")
    aliases = read_yaml(path)
    if not isinstance(aliases, dict):
        raise KoraError("aliases.yaml debe mapear identidad anterior a identidad conservada")
    return dict(aliases)


def alias(root: Path, aliasid: str, target: str, knowledge=None):
    """Record a stable identity alias using the repository's aliases.yaml format."""
    root = Path(root).resolve()
    if not isinstance(aliasid, str) or not aliasid.strip() or not isinstance(target, str) or not target.strip():
        raise KoraError("Alias y destino deben ser textos no vacíos")
    if aliasid == target:
        raise KoraError("Un alias no puede dirigirse a sí mismo")
    with _author_lock(root):
        catalog = Catalog(root, knowledge=knowledge, strict=False)
        if aliasid in catalog.products or aliasid in catalog.archived:
            raise KoraError(f"La identidad ya existe y no puede ser alias: {aliasid}")
        aliases = _read_aliases(root)
        # A machine root and its knowledge library share resolution, but each
        # root owns its own aliases.yaml.  Do not reserve an identity already
        # claimed by the other root; Catalog's merged map alone cannot tell
        # which file supplied it after discovery.
        foreign_aliases = {}
        if catalog.knowledge_root != root:
            foreign_aliases = _read_aliases(catalog.knowledge_root)
        if aliasid in foreign_aliases:
            raise KoraError(f"El alias ya está reservado en la otra raíz: {aliasid}")
        if aliasid in catalog._blocked:
            raise KoraError(f"El alias está defectuoso o duplicado: {aliasid}")
        if aliasid in aliases and aliases[aliasid] != target:
            raise KoraError(f"El alias ya apunta a otra identidad: {aliasid}")
        probe = dict(aliases)
        probe[aliasid] = target
        current = target
        seen = set()
        while current in probe:
            if current in seen:
                raise KoraError(f"Ciclo de alias: {aliasid}")
            seen.add(current)
            current = probe[current]
            if not isinstance(current, str) or not current.strip():
                raise KoraError(f"Destino de alias inválido: {aliasid}")
        try:
            catalog.get(current)
        except KoraError as error:
            raise KoraError(f"Destino de alias ausente: {target}") from error
        aliases[aliasid] = target
        _write_yaml(root / "aliases.yaml", aliases, root=root)
        return {"alias": aliasid, "target": target, "path": str(root / "aliases.yaml")}


def _consumer_impact(catalog, retired):
    impact = []
    for product in catalog.products.values():
        if product.id == retired.id:
            continue
        for need in product.needs:
            try:
                resolved = catalog._lookup(need.id).id
            except KoraError:
                resolved = need.id
            if resolved == retired.id:
                impact.append({"consumer": product.id, "id": product.id, "relation": "requires",
                               "target": need.id, "target_id": retired.id,
                               "target_runtime": need.target})
        relations = product.metadata.get("relations", {})
        for relation, identifiers in relations.items():
            for requested in identifiers:
                try:
                    resolved = catalog._lookup(requested).id
                except KoraError:
                    resolved = requested
                if resolved == retired.id:
                    impact.append({"consumer": product.id, "id": product.id, "relation": relation,
                                   "target": requested, "target_id": retired.id})
    return impact


def retire(root: Path, identifier: str, reason: str, replacement=None, dry_run=False, knowledge=None):
    """Archive an active agent or skill, preserving a snapshot and impact record."""
    root = Path(root).resolve()
    if not isinstance(reason, str) or not reason.strip():
        raise KoraError("El retiro requiere un motivo no vacío")
    with _author_lock(root) if not dry_run else _null_context():
        catalog = Catalog(root, knowledge=knowledge, strict=False)
        retired = catalog.get(identifier)
        if retired.id not in catalog.products:
            # A process can be interrupted after moving the source and before
            # its lifecycle sidecar is made visible.  Complete that sidecar on
            # retry instead of leaving an archived identity permanently
            # unreportable.
            if retired.id in catalog.archived and retired.kind in ("skill", "agent"):
                destination = Path(retired.directory)
                sidecar = destination.parent / f"{destination.name}.retirement.yaml"
                if sidecar.exists():
                    if sidecar.is_symlink():
                        raise KoraError(f"El registro de retiro es un enlace: {sidecar}")
                    data = read_yaml(sidecar)
                    if not isinstance(data, dict):
                        raise KoraError(f"El registro de retiro debe ser un mapa: {sidecar}")
                    return {"id": retired.id, "kind": retired.kind, "name": retired.name,
                            "revision": data.get("revision"), "source": str(root / "products"),
                            "archive": str(destination), "sidecar": str(sidecar),
                            "reason": data.get("reason"), "replacement": data.get("replacement"),
                            "impact": data.get("impact", []), "dry_run": bool(dry_run),
                            "recovered": False}
                from .product_versions import source_digest
                revision = source_digest(retired)
                impact = _consumer_impact(catalog, retired)
                report = {"id": retired.id, "kind": retired.kind, "name": retired.name,
                          "revision": revision, "source": str(root / "products"),
                          "archive": str(destination), "sidecar": str(sidecar),
                          "reason": reason, "replacement": replacement, "impact": impact,
                          "dry_run": bool(dry_run), "recovered": True}
                if dry_run:
                    return report
                sidecar_data = {"id": retired.id, "kind": retired.kind, "name": retired.name,
                                "revision": revision, "reason": reason, "replacement": replacement,
                                "impact": impact,
                                "retired_at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
                _write_yaml(sidecar, sidecar_data, root=root)
                return report
            raise KoraError(f"La identidad no está activa: {identifier}")
        if retired.kind not in ("skill", "agent"):
            raise KoraError("retire solo admite agentes y skills")
        if replacement is not None:
            if not isinstance(replacement, str) or not replacement.strip() or replacement == retired.id:
                raise KoraError("La sustitución debe ser otra identidad no vacía")
            try:
                replacement_product = catalog.get(replacement)
            except KoraError as error:
                raise KoraError(f"Sustitución ausente: {replacement}") from error
            if replacement_product.id == retired.id:
                raise KoraError("La sustitución no puede ser la identidad retirada")
        impact = _consumer_impact(catalog, retired)
        from .product_versions import preserve, source_digest
        revision = source_digest(retired) if dry_run else preserve(root, retired)
        source = Path(retired.directory)
        destination = root / "archive" / "products" / source.parent.name / source.name
        sidecar = destination.parent / f"{destination.name}.retirement.yaml"
        report = {"id": retired.id, "kind": retired.kind, "name": retired.name,
                  "revision": revision, "source": str(source), "archive": str(destination),
                  "sidecar": str(sidecar), "reason": reason,
                  "replacement": replacement, "impact": impact, "dry_run": bool(dry_run)}
        if dry_run:
            return report
        _check_publication_path(root, destination)
        _check_publication_path(root, sidecar)
        sidecar_data = {"id": retired.id, "kind": retired.kind, "name": retired.name,
                        "revision": revision, "reason": reason, "replacement": replacement,
                        "impact": impact,
                        "retired_at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
        _write_yaml(sidecar, sidecar_data, root=root)
        try:
            rename_new(source, destination)
        except OSError as error:
            # The sidecar belongs to this operation and is safe to remove if
            # the archive destination was occupied before the move.
            if sidecar.exists():
                sidecar.unlink()
            raise KoraError(f"El archivo histórico ya existe: {destination}") from error
        return report


@contextmanager
def _null_context():
    yield
