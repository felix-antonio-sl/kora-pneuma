"""A local reference library: originals, editable drafts and approved snapshots.

Knowledge has two identities while it is being prepared: the canonical
``namespace/name`` location that will be published and, optionally, a named
candidate used to keep more than one piece of work for that identity.  The
candidate is deliberately kept in draft metadata and never participates in
the published location.
"""

from datetime import datetime, timezone
import copy
import os
from pathlib import Path
import re
import shutil
import tempfile

import yaml

from .atomic import exchange, rename_new
from .authoring import _author_lock, _check_publication_path, create
from .catalog import (Catalog, KoraError, Product, contained_file, digest,
                      read_product, reference_digest, safe_relative, _reserved_identity)
from .needs import Need


def _component(value):
    if not isinstance(value, str):
        raise KoraError(f"Nombre de directorio inválido: {value}")
    path = safe_relative(value)
    if len(path.parts) != 1 or value.startswith("."):
        raise KoraError(f"Nombre de directorio inválido: {value}")
    return value


def _candidate_name(value):
    """Validate the optional draft candidate without accepting a path."""
    if value is None:
        return None
    return _component(value)


def _metadata_list(value, count, *, label="provenance"):
    """Validate one caller-supplied metadata entry per source.

    The library only records what the caller supplied.  In particular it does
    not manufacture ``read`` or ``review`` facts from receiving bytes.
    """
    if value is None:
        return [None] * count
    if isinstance(value, dict) and isinstance(value.get("sources"), list):
        value = value["sources"]
    if not isinstance(value, (list, tuple)) or len(value) != count:
        raise KoraError(f"{label} debe tener una entrada por cada fuente")
    entries = []
    for index, entry in enumerate(value, 1):
        if entry is None:
            entries.append(None)
            continue
        if not isinstance(entry, dict):
            raise KoraError(f"{label}[{index}] debe ser un mapa")
        # Copy recursively so a caller cannot mutate the metadata while a
        # publication is being prepared.
        entries.append(copy.deepcopy(entry))
    return entries


def _merge_source_metadata(entry, supplied):
    """Merge optional provenance while retaining computed path/hash fields."""
    if not supplied:
        return entry
    # ``path``, ``origin`` and ``sha256`` identify the bytes actually copied;
    # callers can annotate them but cannot make the integrity check trust a
    # value that was not computed by intake/authoring.
    merged = dict(entry)
    merged.update({key: value for key, value in supplied.items()
                   if key not in {"path", "origin", "sha256"}})
    return merged


def _intake_sidecar(source: Path):
    """Read provenance preserved by an ``intake`` directory, if any."""
    source = Path(source).resolve()
    for parent in (source.parent, *source.parents):
        sidecar = parent / "sources.yaml"
        if not sidecar.is_file():
            continue
        try:
            values = yaml.safe_load(sidecar.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, yaml.YAMLError):
            return None
        if not isinstance(values, list):
            return None
        for value in values:
            if not isinstance(value, dict) or not isinstance(value.get("path"), str):
                continue
            try:
                path = (parent / safe_relative(value["path"])).resolve()
            except KoraError:
                continue
            if path == source:
                return value
        # The nearest sidecar belongs to this intake directory.  Do not walk
        # into an unrelated parent intake if it did not mention the file.
        return None
    return None


def _draft_candidate(item):
    value = item.metadata.get("candidate")
    if value is None:
        return None
    return _candidate_name(value)


def _canonical_coordinates(item):
    """Resolve publication coordinates from metadata, never a candidate path."""
    metadata = item.metadata
    canonical_name = metadata.get("canonical_name")
    if canonical_name is None:
        # Legacy knowledge used ``name`` as display metadata.  Its stable
        # coordinates are the directory leaf, so a human title cannot move a
        # reference accidentally.  Cover the three library layouts and keep
        # a conservative parent/leaf fallback for synthetic drafts.
        parts = Path(item.directory).parts
        for index in range(len(parts) - 3, -1, -1):
            if parts[index] in {"references", "drafts", "versions"}:
                namespace, name = parts[index + 1:index + 3]
                return _component(namespace), _component(name)
        return _component(item.directory.parent.name), _component(item.directory.name)
    namespace = metadata.get("namespace")
    if namespace is None:
        namespace = item.directory.parent.name
    return _component(namespace), _component(canonical_name)


def _draft_paths(root):
    drafts = root / "drafts"
    if drafts.is_symlink():
        raise KoraError(f"La raíz de borradores no es un directorio propio: {drafts}")
    if not drafts.exists():
        return []
    if not drafts.is_dir():
        raise KoraError(f"La raíz de borradores no es un directorio propio: {drafts}")
    paths = []
    for path in sorted(drafts.rglob("object.yaml")):
        if path.is_symlink() or not path.resolve().is_relative_to(drafts):
            raise KoraError(f"Borrador fuera de la biblioteca: {path}")
        paths.append(path)
    return paths


def _read_draft(path, focal_identifier=None):
    """Read one draft while containing a diagnosed, disjoint malformed one."""
    try:
        return read_product(path.parent)
    except KoraError:
        reserved = _reserved_identity(path)
        if reserved is None or focal_identifier is None or reserved == focal_identifier:
            raise
        return None


def _require_catalog_state(catalog, identifier, allowed):
    """Continue past disjoint diagnosed products, but stop uncertainty."""
    state = catalog.availability(identifier)
    if state in allowed:
        return state
    # ``_lookup`` carries the useful indeterminate/ambiguous diagnostic and is
    # deliberately called before any publication-side write.
    try:
        catalog._lookup(identifier)
    except KoraError:
        raise
    raise KoraError(f"Estado inesperado para {identifier}: {state}")


def _check_draft_coordinates(item, namespace, name, candidate):
    """Keep editable metadata from redirecting a draft publication path."""
    draft_root = item.directory.parent.parent
    expected_leaf = name if candidate is None else f"{name}--{candidate}"
    if (draft_root.name != "drafts" or item.directory.parent.name != namespace
            or item.directory.name != expected_leaf):
        raise KoraError(f"Las coordenadas canónicas no corresponden al borrador: {item.id}")


def _write_metadata(directory, metadata):
    temporary = directory / ".object.yaml.new"
    with temporary.open("x", encoding="utf-8") as stream:
        stream.write(yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False))
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, directory / "object.yaml")


def _sync(directory):
    for path in [p for p in directory.rglob("*") if p.is_file() and not p.is_symlink()]:
        with path.open("rb") as stream:
            os.fsync(stream.fileno())
    for path in [p for p in directory.rglob("*") if p.is_dir() and not p.is_symlink()] + [directory]:
        _sync_directory(path)


def _sync_directory(path):
    fd = os.open(path, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def _draft_destination(root, namespace, name, candidate=None):
    """Return a private draft location for a canonical identity."""
    namespace, name = _component(namespace), _component(name)
    candidate = _candidate_name(candidate)
    if candidate is None:
        return root / "drafts" / namespace / name
    # Keep the old default layout intact while giving named candidates their
    # own leaf.  The metadata remains authoritative for publication, so this
    # spelling cannot accidentally become references/<candidate>.
    return root / "drafts" / namespace / f"{name}--{candidate}"


def _draft(root, identifier, candidate=None):
    candidate = _candidate_name(candidate)
    aliases = Catalog(root, strict=False).aliases
    seen = set()
    while identifier in aliases and identifier not in seen:
        seen.add(identifier)
        identifier = aliases[identifier]
    matches = []
    for path in _draft_paths(root):
        item = _read_draft(path, identifier)
        if item is None:
            continue
        if item.id == identifier and (candidate is None or _draft_candidate(item) == candidate):
            matches.append(item)
    if candidate is not None:
        if len(matches) != 1:
            raise KoraError(
                f"Se esperaba el borrador {candidate} de {identifier}; encontrados: {len(matches)}"
            )
        return matches[0]

    # A no-candidate call keeps the backwards-compatible default draft.  If a
    # caller created exactly one named candidate, accepting it is useful for
    # old API clients; two named candidates make omission ambiguous.
    defaults = [item for item in matches if _draft_candidate(item) is None]
    if len(defaults) == 1:
        return defaults[0]
    if len(matches) == 1:
        return matches[0]
    raise KoraError(f"Se esperaba un borrador de {identifier}; encontrados: {len(matches)}")


def intake(root: Path, name: str, sources, *, provenance=None, metadata=None,
           source_metadata=None) -> dict:
    """Preserve supplied originals; receiving a resource does not publish knowledge."""
    root = Path(root).resolve()
    name = _component(name)
    sources = list(sources)
    if not sources:
        raise KoraError("Indica al menos un recurso con --source")
    supplied = [value for value in (provenance, metadata, source_metadata) if value is not None]
    if len(supplied) > 1:
        raise KoraError("Usa una sola lista de metadatos de procedencia")
    source_metadata = _metadata_list(supplied[0] if supplied else None, len(sources))
    with _author_lock(root):
        destination = root / "inbox" / name
        _check_publication_path(root, destination)
        temporary = Path(tempfile.mkdtemp(prefix=".kora-intake-", dir=root))
        try:
            entries = []
            for index, source in enumerate(sources, 1):
                source = Path(source).resolve()
                data = source.read_bytes()
                relative = f"{index}-{source.name}"
                (temporary / safe_relative(relative)).write_bytes(data)
                entry = {"path": relative, "origin": str(source), "sha256": digest(data)}
                entries.append(_merge_source_metadata(entry, source_metadata[index - 1]))
            (temporary / "sources.yaml").write_text(
                yaml.safe_dump(entries, allow_unicode=True, sort_keys=False), encoding="utf-8"
            )
            _sync(temporary)
            destination.parent.mkdir(parents=True, exist_ok=True)
            rename_new(temporary, destination)
            return {"path": str(destination), "sources": entries, "publication": "pending"}
        finally:
            if temporary.exists():
                shutil.rmtree(temporary)


def create_draft(root: Path, namespace: str, name: str, identifier: str,
                 description: str, body: Path, *, sources=(), requires=(),
                 candidate=None, provenance=None, metadata=None,
                 source_metadata=None) -> Product:
    root = Path(root).resolve()
    namespace, name = _component(namespace), _component(name)
    candidate = _candidate_name(candidate)
    supplied = [value for value in (provenance, metadata, source_metadata) if value is not None]
    if len(supplied) > 1:
        raise KoraError("Usa una sola lista de metadatos de procedencia")
    sources = list(sources)
    source_metadata = _metadata_list(supplied[0] if supplied else None, len(sources))
    with _author_lock(root):
        catalog = Catalog(root, strict=False)
        state = catalog.availability(identifier)
        if state != "absent":
            try:
                catalog._lookup(identifier)
            except KoraError:
                raise
            raise KoraError(f"La referencia ya existe: {identifier}; usa revise para preparar una edición")
        for path in _draft_paths(root):
            item = _read_draft(path, identifier)
            if item is None:
                continue
            if item.id == identifier and _draft_candidate(item) == candidate:
                raise KoraError(f"Ya existe un borrador de {identifier}")
        for container in ("references", "archive/references"):
            reference = root / container / namespace / name
            if reference.exists() or reference.is_symlink():
                raise KoraError(f"La ubicación pertenece a una referencia existente: {reference}")
        destination = _draft_destination(root, namespace, name, candidate)
        _check_publication_path(root, destination)
        temporary = Path(tempfile.mkdtemp(prefix=".kora-draft-", dir=root))
        try:
            item = create(temporary, "knowledge", namespace, name, identifier, description, body, sources=sources)
            metadata = dict(item.metadata)
            if requires:
                metadata["requires"] = list(requires)
            if candidate is not None:
                # Canonical coordinates are explicit because the draft leaf is
                # intentionally no longer namespace/name.
                metadata["namespace"] = namespace
                metadata["canonical_name"] = name
                metadata["candidate"] = candidate
            entries = metadata.get("provenance", {}).get("sources", [])
            if not isinstance(entries, list) or len(entries) != len(sources):
                if sources:
                    raise KoraError("La procedencia generada no coincide con las fuentes")
            else:
                enriched = []
                for index, entry in enumerate(entries):
                    sidecar = _intake_sidecar(Path(sources[index]))
                    merged = _merge_source_metadata(entry, sidecar)
                    merged = _merge_source_metadata(merged, source_metadata[index])
                    enriched.append(merged)
                if enriched:
                    metadata["provenance"] = {"sources": enriched}
            _write_metadata(item.directory, metadata)
            item = read_product(item.directory)
            _sync(item.directory)
            destination.parent.mkdir(parents=True, exist_ok=True)
            rename_new(item.directory, destination)
            return read_product(destination)
        finally:
            shutil.rmtree(temporary)


def revise(root: Path, identifier: str, candidate=None) -> Product:
    root = Path(root).resolve()
    candidate = _candidate_name(candidate)
    with _author_lock(root):
        catalog = Catalog(root, strict=False)
        _require_catalog_state(catalog, identifier, {"available"})
        published = catalog.get(identifier)
        if published.reference_root != root:
            raise KoraError(f"No es una referencia de esta biblioteca: {identifier}")
        if not published.directory.is_relative_to(root / "references"):
            raise KoraError(f"La referencia está archivada: {identifier}")
        namespace, name = _canonical_coordinates(published)
        destination = _draft_destination(root, namespace, name, candidate)
        if destination.exists():
            item = _draft(root, identifier, candidate)
            # A pending edit is work to preserve, including repeated revise calls.
            # A seed draft created before the first publication has no base;
            # after another named candidate becomes active it must be rebased
            # onto that published snapshot when the caller explicitly asks
            # for the default path.  Once a base exists, a changed digest is
            # real pending work and remains protected from a stale approval.
            if (reference_digest(item) != reference_digest(published)
                    and item.metadata.get("revision_base") is not None):
                return item
            metadata = {k: v for k, v in item.metadata.items() if k != "publication"}
            metadata["revision_base"] = published.revision
            if candidate is not None:
                metadata["namespace"] = namespace
                metadata["canonical_name"] = name
                metadata["candidate"] = candidate
            else:
                # A published named candidate is allowed to seed the simple
                # default path, but its private candidate identity must not
                # leak into the new default draft.
                metadata.pop("candidate", None)
            _write_metadata(item.directory, metadata)
            return read_product(destination)
        _check_publication_path(root, destination)
        temporary = Path(tempfile.mkdtemp(prefix=".kora-draft-", dir=root))
        try:
            staged = temporary / "product"
            shutil.copytree(published.directory, staged, symlinks=True)
            metadata = {k: v for k, v in published.metadata.items() if k != "publication"}
            metadata["revision_base"] = published.revision
            if candidate is not None:
                metadata["namespace"] = namespace
                metadata["canonical_name"] = name
                metadata["candidate"] = candidate
            else:
                metadata.pop("candidate", None)
            _write_metadata(staged, metadata)
            _sync(staged)
            destination.parent.mkdir(parents=True, exist_ok=True)
            rename_new(staged, destination)
            return read_product(destination)
        finally:
            shutil.rmtree(temporary)


def review(root: Path, identifier: str, candidate=None) -> dict:
    root = Path(root).resolve()
    item = _draft(root, identifier, candidate)
    catalog = Catalog(root, strict=False)
    _require_catalog_state(catalog, item.id, {"absent", "available"})
    namespace, name = _canonical_coordinates(item)
    _check_draft_coordinates(item, namespace, name, _draft_candidate(item))
    return {"id": item.id, "path": str(item.content_path),
            "metadata": str(item.directory / "object.yaml"),
            "reviewed_sha256": reference_digest(item),
            "base_revision": item.metadata.get("revision_base"),
            "requires": list(item.requires),
            "sources": item.metadata.get("provenance", {}).get("sources", []),
            "namespace": namespace, "name": name,
            "candidate": _draft_candidate(item),
            "publication": "draft"}


def _check_sources(item):
    provenance = item.metadata.get("provenance", {})
    if provenance is None:
        return
    if not isinstance(provenance, dict):
        raise KoraError(f"Procedencia inválida: {item.id}")
    sources = provenance.get("sources", [])
    if not isinstance(sources, list):
        raise KoraError(f"Procedencia de fuentes inválida: {item.id}")
    for source in sources:
        if not isinstance(source, dict) or not isinstance(source.get("path"), str):
            raise KoraError(f"Procedencia de fuente inválida: {item.id}")
        path = contained_file(item.directory, source["path"])
        if digest(path.read_bytes()) != source.get("sha256"):
            raise KoraError(f"Original modificado: {source['path']}")


def _publish(root, item, namespace, name, publication, *, archived=False,
             validate=None):
    """Finish a snapshot first, then change exactly one reader-visible name."""
    temporary = Path(tempfile.mkdtemp(prefix=".kora-publish-", dir=root))
    link = None
    try:
        staged = temporary / "product"
        shutil.copytree(item.directory, staged, symlinks=True)
        candidate = read_product(staged)
        if reference_digest(candidate) != publication["sha256"]:
            raise KoraError(f"El borrador cambió durante la publicación: {item.id}")
        _write_metadata(staged, {**candidate.metadata, "publication": publication})
        candidate = read_product(staged)
        revision = candidate.fingerprint()
        version = root / "versions" / namespace / name / revision
        for parent in (version.parent, *version.parent.parents):
            if parent == root:
                break
            if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
                raise KoraError(f"La conservación atraviesa un enlace o archivo: {parent}")
        version.parent.mkdir(parents=True, exist_ok=True)
        if version.exists() or version.is_symlink():
            # A failed pointer change can leave a complete, unreferenced version.
            # Reusing the same bytes makes retry safe without a second journal.
            if version.is_symlink() or not version.is_dir():
                raise KoraError(f"La versión conservada no es un directorio propio: {version}")
            if read_product(version).fingerprint() != revision:
                raise KoraError(f"La versión conservada fue modificada: {version}")
        else:
            _check_publication_path(root, version)
            _sync(staged)
            rename_new(staged, version)
        _sync_directory(version.parent)
        reference = root / ("archive/references" if archived else "references") / namespace / name
        for parent in (reference.parent, *reference.parent.parents):
            if parent == root:
                break
            if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
                raise KoraError(f"La publicación atraviesa un enlace o archivo: {parent}")
        reference.parent.mkdir(parents=True, exist_ok=True)
        # Keep preparation outside the reader-visible reference namespace.
        link = temporary / "reference"
        link.symlink_to(os.path.relpath(version, reference.parent), target_is_directory=True)
        if reference.exists() or reference.is_symlink():
            if not reference.is_symlink():
                raise KoraError(f"La referencia publicada no es un enlace: {reference}")
        # The version is durable before this point.  Revalidate immediately
        # before changing the stable reader-visible pointer so a dependency
        # or base source changed during copying cannot be published.  A
        # failure leaves the conserved version unreferenced for safe retry.
        if reference_digest(item) != publication["sha256"]:
            raise KoraError(f"El borrador cambió durante la publicación: {item.id}")
        _check_sources(item)
        if validate is not None:
            validate()
        if reference.is_symlink():
            exchange(link, reference)
        else:
            rename_new(link, reference)
        _sync_directory(reference.parent)
        return read_product(reference, revision, root)
    finally:
        if link is not None and link.is_symlink():
            link.unlink()
        shutil.rmtree(temporary)


def _check_knowledge_dependencies(catalog, item):
    """Validate typed needs and capture their bytes in one catalog phase.

    A conditional need is retained in the source metadata even when its target
    is absent.  An unconditional need must resolve to an active knowledge
    reference, including a fixed historical revision when one was requested.
    """
    try:
        pending = list(item.needs)
    except ValueError as error:
        raise KoraError(f"Necesidades inválidas en {item.id}: {error}") from error
    seen = {item.id: item.revision}
    failures = []

    def visit(need, optional_origin=None):
        """Return ``(available, conditional_failures)`` for one edge.

        A child without its own condition inherits its parent's optional
        branch.  A child with a condition starts a new branch: its absence is
        recorded but does not poison the containing branch.  Every failed
        branch restores the ``seen`` map, matching Catalog.explain's rollback
        semantics and preventing a failed optional path from satisfying a
        later mandatory edge accidentally.
        """
        if not isinstance(need, Need):
            raise KoraError(f"Necesidad inválida en {item.id}")
        origin = need if need.condition is not None else optional_origin
        before = dict(seen)
        try:
            if need.kind == "capability":
                raise KoraError(
                    f"Una referencia de conocimiento no puede depender de una capacidad: {need.id}"
                )
            dependency = (catalog.at_revision(need.id, need.revision)
                          if need.revision else catalog.get(need.id))
            if dependency.kind != "knowledge":
                raise KoraError(
                    f"El conocimiento requiere otra referencia publicada, no agentes ni skills: {need.id}"
                )
            publication = dependency.metadata.get("publication")
            if (dependency.revision is None or dependency.reference_root is None
                    or not isinstance(publication, dict)
                    or publication.get("status") not in {"approved", "legacy"}):
                raise KoraError(f"La dependencia no es una referencia publicada verificable: {need.id}")
            resolved_kind = "knowledge"
            if need.kind is not None and need.kind != resolved_kind:
                raise KoraError(
                    f"Tipo de necesidad incompatible: {need.id}; requiere {need.kind}, resuelve {resolved_kind}"
                )
            if dependency.id not in catalog.products:
                raise KoraError(f"La dependencia no está activa: {need.id}")
            previous = seen.get(dependency.id)
            if previous is not None and previous != dependency.revision:
                raise KoraError(f"Revisiones incompatibles de {dependency.id}")
            if dependency.id in seen:
                return True, []
            seen[dependency.id] = dependency.revision
            branch_failures = []
            for nested in dependency.needs:
                available, nested_failures = visit(nested, origin)
                branch_failures.extend(nested_failures)
                if not available:
                    # ``available=False`` is fatal to this branch only when
                    # the failure belongs to this branch's inherited origin.
                    # An independently conditional child remains recorded and
                    # does not make its parent unavailable.
                    if any(failed_origin is origin
                           for failed_origin, _ in nested_failures):
                        seen.clear()
                        seen.update(before)
                        return False, branch_failures
            return True, branch_failures
        except (KoraError, ValueError) as error:
            seen.clear()
            seen.update(before)
            if origin is None:
                raise KoraError(f"{item.id} necesita {need.id}: {error}") from error
            return False, [(origin, error)]

    while pending:
        available, branch_failures = visit(pending.pop())
        if not available:
            failures.extend(branch_failures)
        else:
            # A nested conditional child may be unavailable while its parent
            # remains usable.
            failures.extend(branch_failures)

    # Convert the internal tuples while preserving encounter order and avoid
    # duplicate propagation of one failed conditional branch.
    unavailable = []
    seen_failures = set()
    for need, error in failures:
        key = (need.id, need.condition, str(error))
        if key in seen_failures:
            continue
        seen_failures.add(key)
        unavailable.append({"id": need.id, "condition": need.condition,
                            "status": "unavailable", "error": str(error)})
    return unavailable


def approve(root: Path, identifier: str, reviewed: str, candidate=None) -> Product:
    """Execute a content approval already given by Félix or his explicit delegate."""
    root = Path(root).resolve()
    candidate = _candidate_name(candidate)
    with _author_lock(root):
        item = _draft(root, identifier, candidate)
        if item.kind != "knowledge" or reference_digest(item) != reviewed:
            raise KoraError("El borrador no coincide con la revisión aprobada; vuelve a revisar el contenido")
        _check_sources(item)
        catalog = Catalog(root, strict=False)
        namespace, name = _canonical_coordinates(item)
        _check_draft_coordinates(item, namespace, name, _draft_candidate(item))
        _require_catalog_state(catalog, item.id, {"absent", "available", "retired"})
        current = catalog.get(item.id) if item.id in catalog.products else None
        if current is not None:
            current_namespace, current_name = _canonical_coordinates(current)
            if (namespace, name) != (current_namespace, current_name):
                raise KoraError(f"La candidata cambió la ubicación canónica de {item.id}")
        reference = root / "references" / namespace / name
        if reference.exists() or reference.is_symlink():
            if not reference.is_symlink():
                raise KoraError(f"La ubicación pertenece a un archivo o directorio: {reference}")
            if read_product(reference).id != item.id:
                raise KoraError(f"La ubicación pertenece a otra identidad: {reference}")
            try:
                same_reference = current is not None and reference.resolve() == current.directory.resolve()
            except (OSError, RuntimeError) as error:
                raise KoraError(f"La referencia publicada tiene un enlace inválido: {reference}") from error
            if not same_reference:
                raise KoraError(f"La referencia está fuera de su versión publicada: {reference}")
        if item.id in catalog.archived:
            raise KoraError(f"Referencia archivada: {item.id}")
        if current and current.metadata.get("publication", {}).get("status") == "approved" and current.metadata["publication"]["sha256"] == reviewed:
            return current
        if (current.revision if current else None) != item.metadata.get("revision_base"):
            raise KoraError("La referencia cambió desde la preparación del borrador; reconcilia la nueva versión")
        # Capture and revalidate dependency sources at the publication
        # boundary.  The draft itself is checked by the reviewed hash and by
        # _publish immediately before its version is conserved.
        with catalog.phase():
            # ``get`` ran before the phase to establish idempotency/base
            # checks; capture that exact current snapshot in this phase so
            # the final callback also protects the base publication source.
            if current is not None:
                catalog.capture(current)
            unavailable = _check_knowledge_dependencies(catalog, item)
            catalog.revalidate()
            publication = {"status": "approved", "sha256": reviewed, "hash_mode": "git-v1",
                           "approved_at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
            if unavailable:
                publication["conditional_dependencies"] = unavailable
            return _publish(root, item, namespace, name, publication,
                            validate=catalog.revalidate)


def _resolve_alias(catalog, identifier):
    """Resolve an alias without changing the alias file."""
    seen = set()
    while identifier in catalog.aliases:
        if identifier in seen:
            raise KoraError(f"Ciclo de alias: {identifier}")
        seen.add(identifier)
        identifier = catalog.aliases[identifier]
    return identifier


def _consumer_impact(catalog, identifier):
    """Find active products whose typed dependency closure reaches identifier."""
    consumers = []
    details = []

    def reaches(product, target, seen):
        if product.id in seen:
            return False
        seen = {*seen, product.id}
        try:
            needs = product.needs
        except ValueError:
            return False
        for need in needs:
            try:
                dependency = (catalog.at_revision(need.id, need.revision)
                              if need.revision else catalog.get(need.id))
            except KoraError:
                # A missing conditional need is still documented in the
                # source but cannot identify a currently affected consumer.
                continue
            if dependency.id == target or reaches(dependency, target, seen):
                return True
        return False

    for product in sorted(catalog.products.values(), key=lambda item: item.id):
        if product.id == identifier:
            continue
        if reaches(product, identifier, set()):
            consumers.append(product.id)
            details.append({"id": product.id, "kind": product.kind,
                            "revision": product.revision})

    aliases = []
    for alias, target in sorted(catalog.aliases.items()):
        if _resolve_alias(catalog, target) == identifier or _resolve_alias(catalog, alias) == identifier:
            aliases.append(alias)
    return consumers, details, aliases


def _read_lifecycle(root):
    path = root / "lifecycle.yaml"
    if not path.exists():
        return {}
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as error:
        raise KoraError(f"No se pudo leer el ciclo de vida: {path}: {error}") from error
    if value is None:
        return {}
    if not isinstance(value, dict):
        raise KoraError(f"El ciclo de vida debe ser un mapa: {path}")
    return value


def _write_lifecycle(root, records):
    path = root / "lifecycle.yaml"
    if path.is_symlink() or (path.exists() and not path.is_file()):
        raise KoraError(f"El ciclo de vida no es un archivo propio: {path}")
    temporary = root / ".lifecycle.yaml.new"
    if temporary.exists() or temporary.is_symlink():
        raise KoraError(f"El destino contiene trabajo existente: {temporary}")
    try:
        with temporary.open("x", encoding="utf-8") as stream:
            stream.write(yaml.safe_dump(records, allow_unicode=True, sort_keys=True))
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        _sync_directory(root)
    finally:
        if temporary.exists():
            temporary.unlink()


def _retirement_record(existing, identifier, product, reason, replacement,
                       namespace, name):
    """Return a validated lifecycle intent, preserving the first reason."""
    if identifier in existing:
        record = existing[identifier]
        if not isinstance(record, dict):
            raise KoraError(f"Registro de retiro inválido: {identifier}")
        expected = {"id": identifier, "revision": product.revision,
                    "namespace": namespace, "name": name}
        for key, value in expected.items():
            if record.get(key) != value:
                raise KoraError(f"El retiro pendiente no coincide con la referencia: {identifier}")
        if record.get("status") not in {"retiring", "retired"}:
            raise KoraError(f"Estado de retiro desconocido: {identifier}")
        return copy.deepcopy(record)
    return {
        "id": identifier,
        "status": "retiring",
        "namespace": namespace,
        "name": name,
        "revision": product.revision,
        "reason": reason,
        "replacement": replacement,
        "started_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }


def _retirement_alias(root, identifier):
    """Resolve enough of aliases.yaml to find a pending lifecycle intent."""
    path = root / "aliases.yaml"
    if not path.exists():
        return identifier
    try:
        aliases = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except (OSError, UnicodeError, yaml.YAMLError):
        return identifier
    if not isinstance(aliases, dict):
        return identifier
    seen = set()
    while identifier in aliases:
        if identifier in seen:
            raise KoraError(f"Ciclo de alias: {identifier}")
        seen.add(identifier)
        target = aliases[identifier]
        if not isinstance(target, str):
            return identifier
        identifier = target
    return identifier


def _verify_retirement_version(root, expected, revision):
    """Verify the immutable target before removing either stable pointer."""
    try:
        # A pending transition can intentionally expose the same identity at
        # both reference locations, so use a diagnostic catalog only to load
        # legacy mode metadata and verify the version directly.
        probe = Catalog(root, strict=False)
        modes = probe.legacy_modes.get(root, {}).get(revision)
        snapshot = read_product(expected, revision, root, modes)
        Catalog._verify_reference(snapshot)
    except (KoraError, OSError, RuntimeError) as error:
        raise KoraError(f"La versión conservada del retiro cambió: {expected}") from error


def _pending_retirement(root, identifier, lifecycle, *, reconcile=True):
    canonical = _retirement_alias(root, identifier)
    record = lifecycle.get(canonical)
    if not isinstance(record, dict) or record.get("status") != "retiring":
        return None
    if record.get("id") != canonical:
        raise KoraError(f"Registro de retiro inconsistente: {canonical}")
    namespace = _component(record.get("namespace"))
    name = _component(record.get("name"))
    revision = record.get("revision")
    if not isinstance(revision, str) or not re.fullmatch(r"[0-9a-f]{64}", revision):
        raise KoraError(f"Revisión de retiro inválida: {canonical}")
    reference = root / "references" / namespace / name
    archived = root / "archive" / "references" / namespace / name
    expected = root / "versions" / namespace / name / revision
    if not expected.is_dir():
        raise KoraError(f"La versión conservada del retiro está ausente: {canonical}")
    _verify_retirement_version(root, expected, revision)
    active = reference.is_symlink()
    old = archived.is_symlink()
    try:
        active_target = reference.resolve() if active else None
        archived_target = archived.resolve() if old else None
    except (OSError, RuntimeError) as error:
        raise KoraError(f"El retiro pendiente tiene un enlace inválido: {canonical}") from error
    if active and old:
        # A process may have stopped after creating the archive pointer and
        # before removing the active one.  Reconcile only an exact pair.
        if active_target != expected or archived_target != expected:
            raise KoraError(f"El retiro pendiente apunta a versiones distintas: {canonical}")
        if reconcile:
            reference.unlink()
            _sync_directory(reference.parent)
    elif active:
        if active_target != expected:
            raise KoraError(f"El retiro pendiente cambió de versión: {canonical}")
    elif old:
        if archived_target != expected:
            raise KoraError(f"La referencia archivada cambió de versión: {canonical}")
    else:
        raise KoraError(f"El retiro pendiente perdió ambas referencias: {canonical}")
    return canonical


def _finish_retirement(record):
    result = copy.deepcopy(record)
    result["status"] = "retired"
    result.setdefault("retired_at", datetime.now(timezone.utc).isoformat(timespec="seconds"))
    return result


def retire(root: Path, identifier: str, reason: str, replacement=None,
           dry_run=False, *, consumer_root=None) -> dict:
    """Retire one published reference while preserving versions and aliases.

    Only the stable reference name moves.  The immutable version remains at
    ``versions/<namespace>/<name>/<revision>`` and the lifecycle explanation is
    recorded in ``lifecycle.yaml`` outside that snapshot.
    """
    root = Path(root).resolve()
    if not isinstance(reason, str) or not reason.strip():
        raise KoraError("El retiro requiere un motivo no vacío")
    if replacement is not None and (not isinstance(replacement, str) or not replacement.strip()):
        raise KoraError("La sustitución debe ser una identidad no vacía")
    if not isinstance(dry_run, bool):
        raise KoraError("dry_run debe ser booleano")

    with _author_lock(root):
        lifecycle = _read_lifecycle(root)
        # Repair a stopped pointer transition before constructing a strict
        # catalog; both names otherwise represent one identity and discovery
        # would correctly reject the transient duplicate.
        pending = _pending_retirement(root, identifier, lifecycle,
                                      reconcile=not dry_run)
        if pending is not None and dry_run:
            record = lifecycle[pending]
            reference = root / "references" / record["namespace"] / record["name"]
            archived = root / "archive" / "references" / record["namespace"] / record["name"]
            if reference.is_symlink() and archived.is_symlink():
                actions = ["unlink_active_reference_after_exact_pair_check"]
            elif reference.is_symlink():
                actions = ["create_archive_reference", "unlink_active_reference",
                           "complete_lifecycle"]
            elif archived.is_symlink():
                actions = ["complete_lifecycle"]
            else:
                actions = ["repair_missing_reference_pair"]
            return {
                "id": pending,
                "status": "planned",
                "reason": record.get("reason"),
                "replacement": record.get("replacement"),
                "revision": record.get("revision"),
                "reference": str(reference),
                "archive_reference": str(archived),
                "consumers": [],
                "consumer_details": [],
                "aliases": [],
                "impact": {"consumers": [], "consumer_details": [], "aliases": []},
                "dry_run": True,
                "lifecycle": copy.deepcopy(record),
                "recovery_pending": True,
                "actions": actions,
                "would_move": not archived.is_symlink(),
            }
        catalog = Catalog(root)
        product = catalog.get(identifier)
        canonical = product.id
        namespace, name = _canonical_coordinates(product)
        reference = root / "references" / namespace / name
        archived = root / "archive" / "references" / namespace / name
        impact_root = root if consumer_root is None else Path(consumer_root).resolve()
        impact_catalog = (catalog if impact_root == root else
                          Catalog(impact_root, knowledge=root))
        with impact_catalog.phase():
            consumers, consumer_details, aliases = _consumer_impact(impact_catalog, canonical)
            impact_catalog.revalidate()
        existing_record = lifecycle.get(canonical)
        record = _retirement_record(lifecycle, canonical, product, reason, replacement,
                                     namespace, name)
        result = {
            "id": canonical,
            "status": "retired" if product.id in catalog.archived else "planned",
            "reason": record.get("reason", reason),
            "replacement": record.get("replacement", replacement),
            "revision": product.revision,
            "reference": str(reference),
            "archive_reference": str(archived),
            "consumer_root": str(impact_root),
            "consumers": consumers,
            "consumer_details": consumer_details,
            "aliases": aliases,
            "impact": {"consumers": consumers, "consumer_details": consumer_details,
                        "aliases": aliases},
            "dry_run": dry_run,
            "lifecycle": record,
        }
        if dry_run:
            result["status"] = "planned"
            result["would_move"] = not archived.exists()
            return result

        if product.id in catalog.archived:
            if reference.exists() or reference.is_symlink():
                raise KoraError(f"Referencia activa y archivada simultáneamente: {canonical}")
            if not archived.is_symlink():
                raise KoraError(f"Referencia retirada ausente: {archived}")
            # An already retired identity remains immutable and idempotent.
            final = _finish_retirement(record)
            if existing_record != final:
                lifecycle[canonical] = final
                _write_lifecycle(root, lifecycle)
            result["lifecycle"] = final
            result["status"] = "retired"
            return result

        if not reference.is_symlink():
            raise KoraError(f"Referencia activa ausente o inválida: {reference}")
        resolved = reference.resolve()
        expected = root / "versions" / namespace / name / (product.revision or "")
        if not product.revision or resolved != expected or not resolved.is_dir():
            raise KoraError(f"Referencia activa fuera de su versión conservada: {reference}")
        if archived.exists() or archived.is_symlink():
            raise KoraError(f"La referencia retirada ya existe: {archived}")
        _check_publication_path(root, archived)
        archived.parent.mkdir(parents=True, exist_ok=True)
        # Persist the reason and exact transition intent before the first
        # pointer mutation.  A later invocation can reconcile either half.
        lifecycle[canonical] = record
        _write_lifecycle(root, lifecycle)
        temporary = Path(tempfile.mkdtemp(prefix=".kora-retire-", dir=root))
        link = temporary / "reference"
        try:
            link.symlink_to(os.path.relpath(resolved, archived.parent), target_is_directory=True)
            rename_new(link, archived)
            _sync_directory(archived.parent)
            try:
                reference.unlink()
            except Exception:
                # Leave the exact pair and the retiring intent for the next
                # invocation to reconcile.  Removing one side here would make
                # a crash indistinguishable from an intentional partial state.
                raise
            _sync_directory(reference.parent)
        finally:
            if link.is_symlink():
                link.unlink()
            shutil.rmtree(temporary)
        final = _finish_retirement(record)
        lifecycle[canonical] = final
        _write_lifecycle(root, lifecycle)
        result["lifecycle"] = final
        result["status"] = "retired"
        result["would_move"] = True
        return result
