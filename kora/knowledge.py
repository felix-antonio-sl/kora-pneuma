"""A local reference library: originals, editable drafts and approved snapshots."""

from datetime import datetime, timezone
import os
from pathlib import Path
import shutil
import tempfile

import yaml

from .atomic import exchange, rename_new
from .authoring import _author_lock, _check_publication_path, create
from .catalog import (Catalog, KoraError, Product, contained_file, digest,
                      read_product, reference_digest, safe_relative)


def _component(value):
    path = safe_relative(value)
    if len(path.parts) != 1 or value.startswith("."):
        raise KoraError(f"Nombre de directorio inválido: {value}")
    return value


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


def _draft(root, identifier):
    aliases = Catalog(root).aliases
    seen = set()
    while identifier in aliases and identifier not in seen:
        seen.add(identifier)
        identifier = aliases[identifier]
    matches = []
    for path in sorted((root / "drafts").glob("*/*/object.yaml")):
        if path.is_symlink() or not path.resolve().is_relative_to(root / "drafts"):
            raise KoraError(f"Borrador fuera de la biblioteca: {path}")
        item = read_product(path.parent)
        if item.id == identifier:
            matches.append(item)
    if len(matches) != 1:
        raise KoraError(f"Se esperaba un borrador de {identifier}; encontrados: {len(matches)}")
    return matches[0]


def intake(root: Path, name: str, sources) -> dict:
    """Preserve supplied originals; receiving a resource does not publish knowledge."""
    root = Path(root).resolve()
    name = _component(name)
    sources = list(sources)
    if not sources:
        raise KoraError("Indica al menos un recurso con --source")
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
                entries.append({"path": relative, "origin": str(source), "sha256": digest(data)})
            (temporary / "sources.yaml").write_text(yaml.safe_dump(entries, allow_unicode=True, sort_keys=False))
            _sync(temporary)
            destination.parent.mkdir(parents=True, exist_ok=True)
            rename_new(temporary, destination)
            return {"path": str(destination), "sources": entries, "publication": "pending"}
        finally:
            if temporary.exists():
                shutil.rmtree(temporary)


def create_draft(root: Path, namespace: str, name: str, identifier: str,
                 description: str, body: Path, *, sources=(), requires=()) -> Product:
    root = Path(root).resolve()
    namespace, name = _component(namespace), _component(name)
    with _author_lock(root):
        catalog = Catalog(root)
        if identifier in catalog.products or identifier in catalog.archived or identifier in catalog.aliases:
            raise KoraError(f"La referencia ya existe: {identifier}; usa revise para preparar una edición")
        for path in (root / "drafts").glob("*/*/object.yaml"):
            if read_product(path.parent).id == identifier:
                raise KoraError(f"Ya existe un borrador de {identifier}")
        for container in ("references", "archive/references"):
            reference = root / container / namespace / name
            if reference.exists() or reference.is_symlink():
                raise KoraError(f"La ubicación pertenece a una referencia existente: {reference}")
        destination = root / "drafts" / namespace / name
        _check_publication_path(root, destination)
        temporary = Path(tempfile.mkdtemp(prefix=".kora-draft-", dir=root))
        try:
            item = create(temporary, "knowledge", namespace, name, identifier, description, body, sources=sources)
            metadata = dict(item.metadata)
            if requires:
                metadata["requires"] = list(requires)
            _write_metadata(item.directory, metadata)
            item = read_product(item.directory)
            _sync(item.directory)
            destination.parent.mkdir(parents=True, exist_ok=True)
            rename_new(item.directory, destination)
            return read_product(destination)
        finally:
            shutil.rmtree(temporary)


def revise(root: Path, identifier: str) -> Product:
    root = Path(root).resolve()
    with _author_lock(root):
        published = Catalog(root).get(identifier)
        if published.reference_root != root:
            raise KoraError(f"No es una referencia de esta biblioteca: {identifier}")
        if not published.directory.is_relative_to(root / "references"):
            raise KoraError(f"La referencia está archivada: {identifier}")
        destination = root / "drafts" / published.directory.parent.name / published.directory.name
        if destination.exists():
            item = _draft(root, identifier)
            # A pending edit is work to preserve, including repeated revise calls.
            if reference_digest(item) != reference_digest(published):
                return item
            metadata = {k: v for k, v in item.metadata.items() if k != "publication"}
            metadata["revision_base"] = published.revision
            _write_metadata(item.directory, metadata)
            return read_product(destination)
        _check_publication_path(root, destination)
        temporary = Path(tempfile.mkdtemp(prefix=".kora-draft-", dir=root))
        try:
            staged = temporary / "product"
            shutil.copytree(published.directory, staged, symlinks=True)
            metadata = {k: v for k, v in published.metadata.items() if k != "publication"}
            metadata["revision_base"] = published.revision
            _write_metadata(staged, metadata)
            _sync(staged)
            destination.parent.mkdir(parents=True, exist_ok=True)
            rename_new(staged, destination)
            return read_product(destination)
        finally:
            shutil.rmtree(temporary)


def review(root: Path, identifier: str) -> dict:
    root = Path(root).resolve()
    item = _draft(root, identifier)
    return {"id": item.id, "path": str(item.content_path),
            "metadata": str(item.directory / "object.yaml"),
            "reviewed_sha256": reference_digest(item),
            "base_revision": item.metadata.get("revision_base"),
            "requires": list(item.requires),
            "sources": item.metadata.get("provenance", {}).get("sources", []),
            "publication": "draft"}


def _check_sources(item):
    for source in item.metadata.get("provenance", {}).get("sources", []):
        if not isinstance(source, dict) or not isinstance(source.get("path"), str):
            raise KoraError(f"Procedencia de fuente inválida: {item.id}")
        path = contained_file(item.directory, source["path"])
        if digest(path.read_bytes()) != source.get("sha256"):
            raise KoraError(f"Original modificado: {source['path']}")


def _publish(root, item, namespace, name, publication, *, archived=False):
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
        version.parent.mkdir(parents=True, exist_ok=True)
        if version.exists():
            # A failed pointer change can leave a complete, unreferenced version.
            # Reusing the same bytes makes retry safe without a second journal.
            if version.is_symlink() or read_product(version).fingerprint() != revision:
                raise KoraError(f"La versión conservada fue modificada: {version}")
        else:
            _check_publication_path(root, version)
            _sync(staged)
            rename_new(staged, version)
        _sync_directory(version.parent)
        reference = root / ("archive/references" if archived else "references") / namespace / name
        reference.parent.mkdir(parents=True, exist_ok=True)
        for parent in (reference.parent, *reference.parent.parents):
            if parent == root:
                break
            if parent.is_symlink():
                raise KoraError(f"La publicación atraviesa un enlace: {parent}")
        # Keep preparation outside the reader-visible reference namespace.
        link = temporary / "reference"
        link.symlink_to(os.path.relpath(version, reference.parent), target_is_directory=True)
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


def approve(root: Path, identifier: str, reviewed: str) -> Product:
    """Execute a content approval already given by Félix or his explicit delegate."""
    root = Path(root).resolve()
    with _author_lock(root):
        item = _draft(root, identifier)
        if item.kind != "knowledge" or reference_digest(item) != reviewed:
            raise KoraError("El borrador no coincide con la revisión aprobada; vuelve a revisar el contenido")
        _check_sources(item)
        catalog = Catalog(root)
        current = catalog.get(item.id) if item.id in catalog.products else None
        reference = root / "references" / item.directory.parent.name / item.directory.name
        if reference.exists() or reference.is_symlink():
            if read_product(reference).id != item.id:
                raise KoraError(f"La ubicación pertenece a otra identidad: {reference}")
        if item.id in catalog.archived:
            raise KoraError(f"Referencia archivada: {item.id}")
        if current and current.metadata.get("publication", {}).get("status") == "approved" and current.metadata["publication"]["sha256"] == reviewed:
            return current
        if (current.revision if current else None) != item.metadata.get("revision_base"):
            raise KoraError("La referencia cambió desde la preparación del borrador; reconcilia la nueva versión")
        pending, seen = list(item.requires), {item.id}
        while pending:
            identifier_needed = pending.pop()
            dependency = catalog.get(identifier_needed)
            if dependency.id in seen:
                continue
            if dependency.kind != "knowledge" or dependency.revision is None or dependency.id not in catalog.products:
                raise KoraError(f"El conocimiento requiere otra referencia publicada, no agentes ni skills: {identifier_needed}")
            seen.add(dependency.id)
            pending.extend(dependency.requires)
        publication = {"status": "approved", "sha256": reviewed, "hash_mode": "git-v1",
                       "approved_at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
        return _publish(root, item, item.directory.parent.name, item.directory.name, publication)
