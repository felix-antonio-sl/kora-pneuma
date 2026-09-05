"""Create authored knowledge, skills and agents with recoverable original sources."""

from contextlib import contextmanager
import fcntl
import os
from pathlib import Path
import shutil
import tempfile

import yaml

from .catalog import Catalog, KoraError, Product, digest, safe_relative
from .atomic import rename_new


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
           description: str, body: Path, *, sources=(), targets=(), requires=(), knowledge=None) -> Product:
    root = Path(root).resolve()
    with _author_lock(root):
        return _create(root, kind, namespace, name, identifier, description, body,
                       sources=sources, targets=targets, requires=requires, knowledge=knowledge)


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
