"""Immutable source snapshots for authored agents and skills.

Product distribution has a deliberately smaller file selection than the source
tree.  This module owns the other integrity boundary: a product revision is a
hash of every policy-selected regular file in its source directory, including
provenance and the Git-significant executable mode (or exact host mode when
requested). Operational residue follows the same exclusion policy as
distribution and never becomes part of a revision or preserved snapshot.
Candidate state and retirement records live outside those directories and
therefore cannot silently change a revision.
"""

from __future__ import annotations

import hashlib
import os
from pathlib import Path
import shutil
import stat
import tempfile
import re

from .atomic import rename_new
from .catalog import (KoraError, Product, _provenance_paths, _resource_exclusion,
                       read_product, safe_relative)


_REVISION = re.compile(r"[0-9a-f]{64}\Z")


def _product_value(product: Product | Path) -> Product:
    if isinstance(product, Product):
        return product
    if isinstance(product, (str, Path)):
        try:
            return read_product(Path(product))
        except (OSError, TypeError) as error:
            raise KoraError(f"No se pudo leer el producto: {product}") from error
    raise KoraError("Se requiere un producto KORA")


def _resource_selection(metadata, directory: Path):
    """Return the declaration and provenance paths used by source selection."""
    explicit_resources = isinstance(metadata, dict) and "resources" in metadata
    declared_roots = []
    if explicit_resources:
        declared = metadata.get("resources", [])
        if isinstance(declared, list):
            for value in declared:
                try:
                    declared_roots.append(safe_relative(value).as_posix())
                except (KoraError, TypeError) as error:
                    raise KoraError(f"Recurso declarado inválido: {value!r}") from error
    provenance = _provenance_paths(directory, metadata) if isinstance(metadata, dict) else set()
    return explicit_resources, declared_roots, provenance


def _is_declared(relative: str, declared_roots) -> bool:
    return any(relative == root or relative.startswith(root + "/")
               for root in declared_roots)


def _regular_files(directory: Path, metadata=None):
    """Return source files after applying KORA's operational residue policy.

    ``os.walk(..., followlinks=False)`` still lists a symlink directory in its
    ``directories`` output.  Inspecting that output explicitly is necessary:
    silently pruning it would make a source digest depend on traversal details
    and could hide bytes outside the product.
    """
    directory = Path(directory)
    explicit_resources, declared_roots, provenance = _resource_selection(metadata, directory)

    entries = []
    for relative, mode, data in _all_regular_files(directory):
        reason = _resource_exclusion(
            relative, declared=explicit_resources and _is_declared(relative, declared_roots)
        )
        if reason is not None:
            # Original provenance is retained when it is a legitimate
            # product file; operational/private names remain excluded by
            # the same policy used by distribution.
            if relative not in provenance:
                continue
            if _resource_exclusion(relative, declared=False) is not None:
                continue
        entries.append((relative, mode, data))
    return entries


def _all_regular_files(directory: Path):
    """Read every regular file, including files excluded from a revision.

    Revision selection deliberately prunes private/cache directories.  The
    lifecycle still needs a physical stamp for those files so an admission
    cannot silently overwrite late local work.  This walk therefore has no
    pruning and applies the same strict link/special-file boundary as the
    selected-source walk.
    """
    directory = Path(directory)
    try:
        root_stat = directory.lstat()
    except OSError as error:
        raise KoraError(f"Fuente de producto ausente: {directory}") from error
    if stat.S_ISLNK(root_stat.st_mode):
        raise KoraError(f"La fuente del producto es un enlace: {directory}")
    if not stat.S_ISDIR(root_stat.st_mode):
        raise KoraError(f"La fuente del producto no es un directorio: {directory}")
    for parent in directory.parents:
        if parent.is_symlink():
            raise KoraError(f"La fuente del producto atraviesa un enlace: {parent}")

    entries = []
    walk_errors = []
    for current, directories, files in os.walk(
            directory, topdown=True, followlinks=False, onerror=walk_errors.append):
        current_path = Path(current)
        directories.sort()
        files.sort()
        for name in directories:
            path = current_path / name
            try:
                mode = path.lstat().st_mode
            except OSError as error:
                raise KoraError(f"No se pudo inspeccionar la fuente: {path}") from error
            if stat.S_ISLNK(mode):
                raise KoraError(f"La fuente del producto contiene un enlace: {path}")
            if not stat.S_ISDIR(mode):
                raise KoraError(f"La fuente del producto contiene un objeto no regular: {path}")
        for name in files:
            path = current_path / name
            try:
                mode = path.lstat().st_mode
            except OSError as error:
                raise KoraError(f"No se pudo inspeccionar la fuente: {path}") from error
            if stat.S_ISLNK(mode):
                raise KoraError(f"La fuente del producto contiene un enlace: {path}")
            if not stat.S_ISREG(mode):
                raise KoraError(f"La fuente del producto contiene un objeto no regular: {path}")
            try:
                data = path.read_bytes()
            except OSError as error:
                raise KoraError(f"No se pudo leer la fuente del producto: {path}") from error
            entries.append((path.relative_to(directory).as_posix(), stat.S_IMODE(mode), data))
    if walk_errors:
        error = walk_errors[0]
        raise KoraError(f"No se pudo inspeccionar la fuente: {directory}: {error}") from error
    return entries


def _digest_records(prefix: bytes, entries, *, portable):
    """Hash sorted length-delimited path/mode/content records."""
    result = hashlib.sha256()
    result.update(prefix)
    entries = sorted(entries)
    result.update(len(entries).to_bytes(8, "big"))
    for relative, mode, data in entries:
        if portable:
            mode = 0o755 if mode & stat.S_IXUSR else 0o644
        relative_data = relative.encode("utf-8")
        result.update(len(relative_data).to_bytes(8, "big"))
        result.update(relative_data)
        result.update(mode.to_bytes(4, "big"))
        result.update(len(data).to_bytes(8, "big"))
        result.update(hashlib.sha256(data).digest())
    return result.hexdigest()


def residue_digest(product: Product | Path, *, portable=False) -> str:
    """Stamp files excluded as operational residue by source selection.

    The stamp is kept in candidate state, outside the product source.  It is
    intentionally separate from ``source_digest``: changing a cache, private
    file, or temporary artifact must not create a published revision, while a
    change made after ``revise`` must still be detected before an admission.
    Exact host modes are used by default because this is a local race guard;
    callers may request Git-portable mode for cross-machine diagnostics.
    """
    product = _product_value(product)
    explicit_resources, declared_roots, _ = _resource_selection(
        product.metadata, Path(product.directory)
    )
    residue = []
    for relative, mode, data in _all_regular_files(product.directory):
        reason = _resource_exclusion(
            relative, declared=explicit_resources and _is_declared(relative, declared_roots)
        )
        if reason is not None:
            residue.append((relative, mode, data))
    return _digest_records(b"kora-product-residue-v1\0", residue, portable=portable)


def _copy_source_tree(product: Product, destination: Path):
    """Copy exactly the digestable source files, omitting operational residue."""
    entries = _regular_files(product.directory, product.metadata)
    destination.mkdir(parents=True, exist_ok=True)
    for relative, mode, data in entries:
        target = destination / safe_relative(relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        os.chmod(target, mode)
    # A declared empty resource directory is still part of a readable source
    # even though directories themselves have no digest record.
    declared = product.metadata.get("resources", [])
    if isinstance(declared, list):
        for relative in declared:
            source = product.directory / safe_relative(relative)
            if source.is_dir():
                (destination / safe_relative(relative)).mkdir(parents=True, exist_ok=True)


def source_digest(product: Product | Path, *, portable=True) -> str:
    """Hash the complete legitimate source tree, including provenance files.

    This revision format uses length-delimited canonical records rather than
    concatenating raw file bytes.  A record commits the relative path, mode,
    byte length and SHA-256 of its bytes, so one file cannot absorb the header
    of the next file and produce the same stream.  In portable mode, file modes
    retain only Git's executable bit (0644/0755), so a clone's local umask or
    write permission changes cannot fabricate a new revision.  ``portable=False``
    lets a caller inspect exact host modes.
    """
    product = _product_value(product)
    directory = Path(product.directory)
    entries = _regular_files(directory, product.metadata)
    return _digest_records(b"kora-product-source-v1\0", entries, portable=portable)


def _coordinates(root: Path, product: Product) -> tuple[str, str]:
    """Resolve namespace/name from an active, archived, candidate, or snapshot path."""
    root = Path(root).resolve()
    directory = Path(product.directory)
    # Do not resolve a source directory before source_digest: a symlink must be
    # rejected as a source, rather than turned into an apparently safe path.
    try:
        relative = directory.absolute().relative_to(root)
    except ValueError as error:
        raise KoraError(f"La fuente del producto está fuera de la raíz: {directory}") from error
    parts = relative.parts
    if len(parts) >= 3 and parts[0] == "products":
        selected = parts[1:3]
    elif len(parts) >= 4 and parts[0:2] == ("archive", "products"):
        selected = parts[2:4]
    elif len(parts) >= 5 and parts[0] == "candidates" and parts[-1] == "product":
        selected = parts[1:3]
    elif len(parts) >= 5 and parts[:2] == ("versions", "products"):
        selected = parts[2:4]
    else:
        raise KoraError(
            "No se pudo derivar namespace y nombre de la fuente; "
            "use products/<namespace>/<name> o su layout de candidatos"
        )
    namespace, name = selected
    for value in (namespace, name):
        try:
            if len(safe_relative(value).parts) != 1:
                raise KoraError(f"Componente de producto inválido: {value}")
        except TypeError as error:
            raise KoraError(f"Componente de producto inválido: {value!r}") from error
    return namespace, name


def _check_path(root: Path, path: Path, *, destination=False):
    """Reject links and non-directories along a source or publication path."""
    root = Path(root).resolve()
    path = Path(path)
    try:
        path.absolute().relative_to(root)
    except ValueError as error:
        raise KoraError(f"La ruta queda fuera de la raíz: {path}") from error
    for node in (path, *path.parents):
        if node == root:
            break
        if node.is_symlink():
            raise KoraError(f"La operación atraviesa un enlace: {node}")
        if node.exists() and node != path and not node.is_dir():
            raise KoraError(f"La operación atraviesa un archivo: {node}")
    if destination and path.exists() and path.is_symlink():
        raise KoraError(f"El destino es un enlace: {path}")


def _same_version(version: Path, revision: str) -> bool:
    if version.is_symlink() or not version.is_dir():
        raise KoraError(f"La versión conservada no es un directorio propio: {version}")
    try:
        item = read_product(version, revision=revision)
        return source_digest(item) == revision
    except (OSError, KoraError) as error:
        raise KoraError(f"La versión conservada fue modificada: {version}: {error}") from error


def preserve(root: Path, product: Product) -> str:
    """Preserve an exact product source tree under its content revision.

    Existing snapshots are accepted only when their complete source digest is
    still the same.  A failed publication may therefore leave an unreferenced
    but valid snapshot without weakening a later retry.
    """
    root = Path(root).resolve()
    product = _product_value(product)
    revision = source_digest(product)
    namespace, name = _coordinates(root, product)
    version = root / "versions" / "products" / namespace / name / revision
    _check_path(root, version, destination=True)
    if version.exists():
        _same_version(version, revision)
        return revision

    root.mkdir(parents=True, exist_ok=True)
    version.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=".kora-product-version-", dir=root))
    staged = temporary / "product"
    try:
        try:
            _copy_source_tree(product, staged)
        except (OSError, shutil.Error, KoraError) as error:
            raise KoraError(f"No se pudo conservar la fuente de {product.id}") from error
        copied = read_product(staged, revision=revision)
        if source_digest(copied) != revision:
            raise KoraError(f"La fuente cambió al conservar la revisión de {product.id}")
        _check_path(root, version, destination=True)
        try:
            rename_new(staged, version)
        except FileExistsError:
            # Another writer may have completed this same immutable snapshot.
            _same_version(version, revision)
        return revision
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)


def verify(product: Product, *, portable=True) -> bool:
    """Verify a product source against its fixed revision.

    The function is intentionally usable for an active product whose revision
    was obtained from a preserved snapshot as well as for the snapshot itself.
    """
    product = _product_value(product)
    revision = product.revision
    if not isinstance(revision, str) or not _REVISION.fullmatch(revision):
        raise KoraError(f"Producto sin revisión SHA-256 fija: {product.id}")
    try:
        actual = source_digest(product, portable=portable)
    except KoraError:
        raise
    if actual != revision:
        raise KoraError(
            f"Fuente de producto modificada: {product.id}; "
            f"se esperaba {revision}, se obtuvo {actual}"
        )
    return True


def at_revision(root: Path, current: Product, revision: str) -> Product:
    """Read and verify an exact preserved product revision."""
    root = Path(root).resolve()
    current = _product_value(current)
    if not isinstance(revision, str) or not _REVISION.fullmatch(revision):
        raise KoraError(f"Revisión de producto inválida: {revision!r}")
    namespace, name = _coordinates(root, current)
    directory = root / "versions" / "products" / namespace / name / revision
    _check_path(root, directory)
    if directory.is_symlink() or not directory.is_dir():
        raise KoraError(f"Revisión de producto ausente: {revision}")
    item = read_product(directory, revision=revision)
    if item.id != current.id:
        raise KoraError(f"La revisión no pertenece a {current.id}")
    verify(item)
    return item
