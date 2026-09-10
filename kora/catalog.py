"""Read authored products and resolve the dependencies their consumers need."""

from contextlib import contextmanager
from dataclasses import dataclass, field, replace
import hashlib
import os
from pathlib import Path, PurePosixPath
import re
import stat
import time

import yaml

from .needs import normalize


class KoraError(Exception):
    """An actionable source or installation conflict."""


class UniqueLoader(yaml.SafeLoader):
    """YAML mappings must not silently replace an earlier value."""


def _mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str):
            raise KoraError("Las claves YAML deben ser texto")
        if key in result:
            raise KoraError(f"Clave YAML duplicada: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


# These directories are the compatibility view for existing machine products
# that predate an explicit ``resources`` declaration.  The list is deliberately
# short: a product-owned auxiliary file outside it must be declared explicitly
# rather than being copied by an accidental recursive walk.
_FALLBACK_RESOURCE_DIRECTORIES = ("referencias", "references", "scripts", "agents", "sources")
_GLOB_MARKERS = ("*", "?", "[")
_CACHE_DIRECTORIES = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
_PRIVATE_DIRECTORIES = {".git", ".hg", ".svn", ".bzr", ".agents", ".codex", ".hermes"}
_TEMPORARY_DIRECTORIES = {"tmp", "temp", ".tmp", ".temp"}
_BYTECODE_SUFFIXES = {".pyc", ".pyo"}
_TEMPORARY_SUFFIXES = {".bak", ".new", ".orig", ".part", ".swp", ".swo", ".temp", ".tmp"}


def read_yaml(path: Path):
    try:
        return yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueLoader)
    except (OSError, UnicodeError, yaml.YAMLError) as error:
        raise KoraError(f"No se pudo leer YAML: {path}: {error}") from error


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _digest_mode(relative, mode, *, portable, legacy_modes):
    """Git preserves the owner's executable bit, not local access permissions."""
    executable = bool(mode & stat.S_IXUSR)
    if legacy_modes is not None:
        previous = legacy_modes.get(relative)
        if (type(previous) is not int or not 0 <= previous <= 0o7777
                or bool(previous & stat.S_IXUSR) != executable):
            raise KoraError(f"Modo histórico ausente o ejecutabilidad modificada: {relative}")
        return previous
    return (0o755 if executable else 0o644) if portable else mode


def safe_relative(value: str) -> Path:
    if not isinstance(value, str) or not value or "\\" in value:
        raise KoraError(f"Ruta relativa inválida: {value!r}")
    path = PurePosixPath(value)
    if path.is_absolute() or any(p in ("..", ".", "") for p in value.split("/")):
        raise KoraError(f"Ruta fuera del producto o instalación: {value}")
    return Path(*path.parts)


def _resource_exclusion(relative: str, *, declared=False) -> str | None:
    """Return the reason a filesystem entry is operational residue."""
    parts = PurePosixPath(relative).parts
    if any(part in _CACHE_DIRECTORIES for part in parts):
        return "caché"
    if any(part in _PRIVATE_DIRECTORIES for part in parts):
        return "estado privado"
    if any(part in _TEMPORARY_DIRECTORIES for part in parts):
        return "directorio temporal"
    name = parts[-1]
    name_lower = name.lower()
    if name_lower == ".env":
        return "estado privado (.env)"
    if name_lower.startswith(".env."):
        template = any(name_lower.endswith(suffix) for suffix in (".example", ".sample", ".template"))
        if not (declared and template):
            return "estado privado (.env)"
    if name.endswith("~") or name.startswith(".#") or name.startswith(".~"):
        return "archivo temporal"
    if any(name_lower.endswith(suffix) for suffix in _BYTECODE_SUFFIXES):
        return "bytecode"
    if any(name_lower.endswith(suffix) for suffix in _TEMPORARY_SUFFIXES):
        return "archivo temporal"
    if name in {".kora-lock", ".object.yaml.new"}:
        return "estado temporal de KORA"
    return None


def _provenance_paths(directory: Path, metadata: dict) -> set[str]:
    """Get product-relative originals that compatibility fallback must omit."""
    provenance = metadata.get("provenance", {})
    if not isinstance(provenance, dict):
        return set()
    values = []
    for key in ("original_path", "original"):
        value = provenance.get(key)
        if isinstance(value, str):
            values.append(value)
    sources = provenance.get("sources", [])
    if isinstance(sources, list):
        for source in sources:
            if not isinstance(source, dict):
                continue
            for key in ("path", "original_path"):
                value = source.get(key)
                if isinstance(value, str):
                    values.append(value)
    paths = set()
    directory = Path(directory).resolve()
    parts = directory.parts
    if len(parts) >= 5 and parts[-5:-3] == ("versions", "products"):
        namespace, name = parts[-3:-1]
    elif len(parts) >= 5 and parts[-5] == "candidates" and parts[-1] == "product":
        namespace, name = parts[-4:-2]
    else:
        namespace, name = directory.parent.name, directory.name
    prefixes = (
        ("products", namespace, name),
        ("archive", "products", namespace, name),
    )
    for value in values:
        try:
            candidate = safe_relative(value)
        except KoraError:
            # Provenance may point to an external absolute source.  It is not a
            # product-relative file and therefore cannot affect this selector.
            continue
        parts = candidate.parts
        for prefix in prefixes:
            if parts[:len(prefix)] == prefix:
                candidate = Path(*parts[len(prefix):])
                break
        paths.add(candidate.as_posix())
    return paths


def _resource_path(directory: Path, relative: str, *, declaration=True) -> Path:
    """Resolve one declared resource without following a symlink boundary."""
    path = directory / safe_relative(relative)
    for node in (path, *path.parents):
        if node == directory:
            break
        if node.is_symlink():
            kind = "declarado" if declaration else "seleccionado"
            raise KoraError(f"Recurso {kind} enlazado; requiere un archivo propio: {path}")
    if not path.exists():
        qualifier = "declarado" if declaration else "seleccionado"
        raise KoraError(f"Recurso {qualifier} ausente: {path}")
    if not (path.is_file() or path.is_dir()):
        raise KoraError(f"Recurso declarado no es archivo ni directorio: {path}")
    return path


def _validate_resource_declaration(directory: Path, metadata: dict) -> None:
    """Validate the optional resources field while reading a product manifest."""
    if "resources" not in metadata:
        return
    declared = metadata["resources"]
    path = directory / "object.yaml"
    if not isinstance(declared, list) or any(not isinstance(value, str) or not value for value in declared):
        raise KoraError(f"{path}: resources debe ser una lista de rutas relativas")
    seen = set()
    for value in declared:
        if any(marker in value for marker in _GLOB_MARKERS):
            raise KoraError(f"{path}: resources no admite patrones glob: {value}")
        relative = safe_relative(value).as_posix()
        if relative in seen:
            raise KoraError(f"{path}: recurso declarado duplicado: {value}")
        seen.add(relative)
        if relative in {"object.yaml", metadata["content"]}:
            raise KoraError(f"{path}: resources no puede incluir metadatos ni cuerpo: {value}")
        reason = _resource_exclusion(relative, declared=True)
        if reason is not None:
            raise KoraError(f"{path}: recurso no distribuible ({reason}): {value}")
        _resource_path(directory, relative)


def _walk_product(directory: Path):
    """Yield non-pruned product entries without traversing private state."""
    for current, directories, files in os.walk(directory, topdown=True, followlinks=False):
        current_path = Path(current)
        directories.sort()
        files.sort()
        kept = []
        for name in directories:
            path = current_path / name
            relative = path.relative_to(directory).as_posix()
            if path.is_symlink():
                yield path, relative
            elif _resource_exclusion(relative) is None:
                kept.append(name)
        directories[:] = kept
        for name in files:
            path = current_path / name
            yield path, path.relative_to(directory).as_posix()


def contained_file(directory: Path, relative: str) -> Path:
    path = directory / safe_relative(relative)
    for node in (path, *path.parents):
        if node == directory:
            break
        if node.is_symlink():
            raise KoraError(f"El recurso debe ser un archivo propio, no enlace: {path}")
    if not path.is_file():
        raise KoraError(f"Recurso ausente: {path}")
    return path


@dataclass(frozen=True)
class File:
    data: bytes
    mode: int = 0o644
    source: dict | None = field(default=None, compare=False)


@dataclass(frozen=True)
class Product:
    directory: Path
    metadata: dict
    revision: str | None = None
    reference_root: Path | None = None
    legacy_modes: dict | None = None
    _files: dict[str, File] | None = field(default=None, repr=False, compare=False)

    @property
    def id(self):
        return self.metadata["id"]

    @property
    def kind(self):
        return self.metadata["kind"]

    @property
    def name(self):
        return self.metadata["name"]

    @property
    def description(self):
        return self.metadata["description"]

    @property
    def targets(self):
        return tuple(self.metadata.get("targets", []))

    @property
    def requires(self):
        return tuple(self.metadata.get("requires", []))

    @property
    def needs(self):
        return normalize(self.requires)

    @property
    def content_path(self):
        if self._files is not None:
            return self.directory / safe_relative(self.metadata["content"])
        return contained_file(self.directory, self.metadata["content"])

    @property
    def body(self):
        try:
            return self.file(self.metadata["content"]).data.decode("utf-8")
        except UnicodeError as error:
            raise KoraError(f"Contenido binario; usar el recurso original: {self.id}") from error

    def _legacy_resources(self) -> dict[str, File]:
        resources = {}
        for path in sorted(self.directory.rglob("*")):
            if path.is_symlink():
                raise KoraError(f"Recurso enlazado requiere importación explícita: {path}")
            if not path.is_file() or path in (self.directory / "object.yaml", self.content_path):
                continue
            resources[path.relative_to(self.directory).as_posix()] = File(
                path.read_bytes(), stat.S_IMODE(path.stat().st_mode))
        return resources

    def _selected_resources(self) -> dict[str, File]:
        """Select machine resources once for both bundles and their fingerprint."""
        explicit = "resources" in self.metadata
        declared = self.metadata.get("resources", [])
        roots = []
        if explicit:
            for relative in declared:
                path = _resource_path(self.directory, relative, declaration=False)
                roots.append((safe_relative(relative).as_posix(), path))
        else:
            for name in _FALLBACK_RESOURCE_DIRECTORIES:
                path = self.directory / name
                if path.is_symlink():
                    raise KoraError(f"Recurso de compatibilidad enlazado: {path}")
                if path.is_dir():
                    roots.append((name, path))

        def selected(relative):
            return any(relative == root or relative.startswith(root + "/") for root, _ in roots)

        resources = {}
        provenance = _provenance_paths(self.directory, self.metadata)
        unknown = []
        for path, relative in _walk_product(self.directory):
            if path.is_symlink():
                raise KoraError(f"Recurso enlazado requiere importación explícita: {path}")
            if not path.is_file():
                raise KoraError(f"Recurso no regular; no se puede distribuir: {path}")
            if relative in ("object.yaml", self.metadata["content"]):
                continue
            is_selected = selected(relative)
            if _resource_exclusion(relative, declared=explicit and is_selected) is not None:
                continue
            if relative in provenance and (not explicit or not is_selected):
                continue
            if not is_selected:
                unknown.append(relative)
                continue
            resources[relative] = File(path.read_bytes(), stat.S_IMODE(path.stat().st_mode))
        if unknown:
            raise KoraError(
                f"Auxiliar fuera de la política de recursos de {self.id}: {unknown[0]}; "
                "decláralo en resources"
            )
        return resources

    def resources(self) -> dict[str, File]:
        if self._files is not None:
            return {path: file for path, file in self._files.items()
                    if path not in ("object.yaml", self.metadata["content"])}
        # Published knowledge predates the machine bundle boundary.  Keep its
        # exhaustive byte set so existing reference revisions remain verifiable.
        if self.kind == "knowledge":
            return self._legacy_resources()
        return self._selected_resources()

    def file(self, relative):
        if self._files is not None:
            return self._files[relative]
        path = contained_file(self.directory, relative)
        return File(path.read_bytes(), stat.S_IMODE(path.stat().st_mode))

    def files(self):
        if self._files is not None:
            return dict(self._files)
        return {"object.yaml": self.file("object.yaml"),
                self.metadata["content"]: self.file(self.metadata["content"]), **self.resources()}

    def _check_metadata(self):
        if self._files is None and read_yaml(self.directory / "object.yaml") != self.metadata:
            raise KoraError(f"La ficha cambió durante la operación: {self.id}")

    def capture(self):
        if self._files is not None:
            return self
        files = self.files()
        metadata = yaml.load(files["object.yaml"].data, Loader=UniqueLoader)
        if metadata != self.metadata:
            raise KoraError(f"La ficha cambió durante la operación: {self.id}")
        return replace(self, metadata=metadata, _files=files)

    def fingerprint(self, *, portable=True, legacy_modes=None) -> str:
        self._check_metadata()
        files = self.files()
        h = hashlib.sha256()
        if self.kind != "knowledge":
            h.update(b"kora-distribution-v2\0")
        for relative, file in sorted(files.items()):
            mode = _digest_mode(relative, file.mode, portable=portable, legacy_modes=legacy_modes)
            h.update(relative.encode() + b"\0")
            h.update(str(mode).encode() + b"\0")
            if self.kind != "knowledge":
                h.update(len(file.data).to_bytes(8, "big"))
            h.update(file.data)
        if legacy_modes is not None and files.keys() != legacy_modes.keys():
            raise KoraError(f"Los modos históricos no corresponden a los archivos: {self.id}")
        return h.hexdigest()


def reference_digest(product: Product, *, portable=True, legacy_modes=None) -> str:
    """Identify exactly the reviewed metadata, content and resources, before approval."""
    product._check_metadata()
    metadata = {k: v for k, v in product.metadata.items() if k != "publication"}
    h = hashlib.sha256(yaml.safe_dump(metadata, allow_unicode=True, sort_keys=True).encode())
    files = {product.metadata["content"]: product.file(product.metadata["content"]), **product.resources()}
    for relative, file in sorted(files.items()):
        mode = _digest_mode(relative, file.mode, portable=portable, legacy_modes=legacy_modes)
        h.update(relative.encode() + b"\0" + str(mode).encode() + b"\0")
        h.update(digest(file.data).encode() + b"\0")
    return h.hexdigest()


def knowledge_root(root: Path, explicit: Path | None = None) -> Path:
    """One optional library, selected explicitly or by the local knowledge link."""
    root = Path(root).resolve()
    if explicit is not None:
        return Path(explicit).resolve()
    link = root / "knowledge"
    if link.exists() or link.is_symlink():
        if not link.is_dir():
            raise KoraError(f"Biblioteca de conocimiento ausente: {link}")
        return link.resolve()
    return root


def read_product(directory: Path, revision=None, reference_root=None, legacy_modes=None) -> Product:
    path = directory / "object.yaml"
    metadata = read_yaml(path)
    if not isinstance(metadata, dict):
        raise KoraError(f"La ficha debe ser un mapa: {path}")
    for field in ("id", "kind", "name", "description", "content"):
        if not isinstance(metadata.get(field), str) or not metadata[field].strip():
            raise KoraError(f"{path}: falta texto en {field}")
    if metadata["kind"] not in ("knowledge", "skill", "agent"):
        raise KoraError(f"Tipo desconocido: {metadata['kind']}")
    if metadata["kind"] != "knowledge" and (
        not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", metadata["name"]) or len(metadata["name"]) > 64
    ):
        raise KoraError(f"Nombre nativo inválido: {metadata['name']}")
    for key in ("targets",):
        value = metadata.get(key, [])
        if not isinstance(value, list) or any(not isinstance(x, str) or not x for x in value):
            raise KoraError(f"{path}: {key} debe ser una lista de textos")
    try:
        normalize(metadata.get("requires", []))
    except ValueError as error:
        raise KoraError(f"{path}: {error}") from error
    if set(metadata.get("targets", [])) - {"codex", "hermes"}:
        raise KoraError(f"{path}: destinos admitidos: codex, hermes")
    relations = metadata.get("relations", {})
    if not isinstance(relations, dict) or any(
        not isinstance(v, list) or any(not isinstance(x, str) for x in v) for v in relations.values()
    ):
        raise KoraError(f"{path}: relaciones debe mapear tipo a lista de identidades")
    product = Product(directory, metadata, revision, reference_root, legacy_modes)
    product.content_path
    _validate_resource_declaration(directory, metadata)
    return product


def _reserved_identity(path):
    """Reserve only an unambiguous top-level identity; never guess from a filename."""
    try:
        metadata = read_yaml(path)
        if isinstance(metadata, dict) and isinstance(metadata.get('id'), str):
            return metadata['id']
    except KoraError:
        pass
    try:
        tokens = []
        try:
            for token in yaml.scan(path.read_text(encoding='utf-8')):
                tokens.append(token)
        except yaml.scanner.ScannerError as error:
            if (error.context != 'while scanning a quoted scalar'
                    or error.problem != 'found unexpected end of stream'):
                return None
    except (OSError, UnicodeError, yaml.YAMLError):
        return None
    # A malformed block value can leave the root's scalar identity provable.
    # Flow roots, merges, aliases, tags and multiple documents defeat that proof.
    if (len(tokens) < 3 or not isinstance(tokens[1], yaml.tokens.BlockMappingStartToken)
            or any(isinstance(t, (yaml.tokens.AliasToken, yaml.tokens.AnchorToken,
                                 yaml.tokens.TagToken, yaml.tokens.DocumentStartToken,
                                 yaml.tokens.DocumentEndToken)) for t in tokens)):
        return None
    identities = []
    for index, token in enumerate(tokens):
        if not isinstance(token, yaml.tokens.KeyToken) or token.start_mark.column != 0:
            continue
        following = tokens[index + 1:index + 4]
        if not following or not isinstance(following[0], yaml.tokens.ScalarToken):
            return None
        key = following[0].value
        if key == '<<':
            return None
        if key == 'id':
            if (len(following) != 3 or not isinstance(following[1], yaml.tokens.ValueToken)
                    or not isinstance(following[2], yaml.tokens.ScalarToken)):
                return None
            identities.append(following[2].value)
    return identities[0] if len(identities) == 1 and identities[0].strip() else None


class Catalog:
    def __init__(self, root: Path, *, knowledge: Path | None = None, strict=True, capabilities=()):
        self.root = Path(root).resolve()
        self.knowledge_root = knowledge_root(self.root, knowledge)
        self.products: dict[str, Product] = {}
        self.archived: dict[str, Product] = {}
        self.aliases = {}
        self.legacy_modes = {}
        self.diagnostics = []
        self._blocked = {}
        self._unknown = []
        self._strict = strict
        self.capabilities = frozenset(capabilities)
        self._snapshots = None
        self._consumers = {}
        self.phase_metrics = {}
        roots = [self.root] if self.knowledge_root == self.root else [self.root, self.knowledge_root]
        for source in roots:
            modes_path = source / 'legacy-modes.yaml'
            try:
                modes = read_yaml(modes_path) if modes_path.exists() else {}
                if not isinstance(modes, dict) or any(not isinstance(v, dict) for v in modes.values()):
                    raise KoraError(f'Modos históricos inválidos: {modes_path}')
                for revision, files in modes.items():
                    if not re.fullmatch(r'[0-9a-f]{64}', revision):
                        raise KoraError(f'Revisión histórica inválida: {modes_path}')
                    for relative, mode in files.items():
                        safe_relative(relative)
                        if type(mode) is not int or not 0 <= mode <= 0o7777:
                            raise KoraError(f'Modo histórico inválido: {modes_path}: {relative}')
                self.legacy_modes[source] = modes
            except KoraError as error:
                self._diagnose(modes_path, error)
            aliases_path = source / 'aliases.yaml'
            try:
                aliases = read_yaml(aliases_path) if aliases_path.exists() else {}
                if not isinstance(aliases, dict):
                    raise KoraError('aliases.yaml debe mapear identidad anterior a identidad conservada')
                for alias, identifier in aliases.items():
                    if alias in self.aliases:
                        self._diagnose(aliases_path, KoraError(f'Alias duplicado: {alias}'), alias)
                    elif not isinstance(identifier, str) or not identifier.strip():
                        self._diagnose(aliases_path, KoraError(f'Destino de alias inválido: {alias}'), alias)
                    else:
                        self.aliases[alias] = identifier
            except KoraError as error:
                self._diagnose(aliases_path, error)
        paths = []
        for active, relative in ((True, 'products'), (False, 'archive/products')):
            container = self.root / relative
            paths.extend((p, active, container, None, None) for p in sorted(container.rglob('object.yaml')))
        for source in roots:
            for active, relative in ((True, 'references'), (False, 'archive/references')):
                container = source / relative
                for reference in sorted(container.glob('*/*')):
                    try:
                        if not reference.is_symlink():
                            raise KoraError(f'Una referencia debe enlazar una versión publicada: {reference}')
                        resolved = reference.resolve()
                        expected = source / 'versions' / reference.parent.name / reference.name / resolved.name
                        if resolved != expected or not re.fullmatch(r'[0-9a-f]{64}', resolved.name):
                            raise KoraError(f'Referencia fuera de sus versiones: {reference}')
                        paths.append((reference / 'object.yaml', active, container, resolved.name, source))
                    except (KoraError, OSError, RuntimeError) as error:
                        self._diagnose(reference, KoraError(str(error)))
        for path, active, container, revision, reference_root in paths:
            try:
                if path.is_symlink() or (revision is None and not path.resolve().is_relative_to(container)):
                    raise KoraError(f'Ficha fuera de products: {path}')
                modes = self.legacy_modes.get(reference_root, {}).get(revision)
                product = read_product(path.parent, revision, reference_root, modes)
                if self.knowledge_root != self.root and revision is None and product.kind == 'knowledge':
                    raise KoraError(f'Conocimiento fuera de la biblioteca central: {product.id}')
                if revision is not None:
                    self._check_publication(product)
                if product.id in self.products or product.id in self.archived or product.id in self.aliases:
                    raise KoraError(f'Identidad duplicada: {product.id}')
                (self.products if active else self.archived)[product.id] = product
            except (KoraError, OSError, RuntimeError) as error:
                self._diagnose(path, KoraError(str(error)), _reserved_identity(path))
        for alias in self.aliases:
            try:
                self._lookup(alias)
            except KoraError as error:
                self._diagnose(self.root / 'aliases.yaml', error, alias)

    def _diagnose(self, path, error, identifier=None):
        if self._strict:
            raise error
        issue = {'source': identifier or str(path), 'path': str(path), 'relation': 'discovery',
                 'error': str(error), 'identity': identifier,
                 'uncertainty': None if identifier else 'incertidumbre sobre identidad y colisiones'}
        self.diagnostics.append(issue)
        if identifier is None:
            self._unknown.append(issue)
        else:
            self._blocked.setdefault(identifier, []).append(issue)

    @property
    def in_phase(self):
        return self._snapshots is not None

    @contextmanager
    def phase(self):
        """Nested preparations share captured bytes; a later phase starts fresh."""
        if self.in_phase:
            yield self
            return
        self._snapshots = {}
        self._consumers = {}
        started = time.perf_counter()
        self.phase_metrics = {'objects': 0, 'reference_verifications': 0, 'bytes': 0}
        try:
            yield self
        finally:
            self.phase_metrics['seconds'] = time.perf_counter() - started
            self._snapshots = None

    def capture(self, product):
        if self._unknown or product.id in self._blocked:
            self._lookup(product.id)
        if not self.in_phase:
            if product.revision is not None:
                self._verify_reference(product)
            return product
        key = (str(product.directory), product.revision)
        if key not in self._snapshots:
            captured = product.capture()
            if captured.revision is not None:
                self._verify_reference(captured)
                self.phase_metrics['reference_verifications'] += 1
            self._snapshots[key] = (captured, product.directory.resolve())
            self.phase_metrics['objects'] += 1
            self.phase_metrics['bytes'] += sum(len(file.data) for file in captured._files.values())
        return self._snapshots[key][0]

    def revalidate(self, *, candidate=None):
        """Recheck relevant source bytes and reference targets before effects."""
        if not self.in_phase:
            raise KoraError('La revalidación requiere una fase de preparación activa')
        discovered = Catalog(self.root, knowledge=self.knowledge_root, strict=False,
                             capabilities=self.capabilities)
        if candidate is not None:
            # Authoring validates a source which is deliberately outside the
            # active catalog; reopen that one overlay while checking every
            # provider against its actual discovered identity and bytes.
            discovered.products[candidate.id] = read_product(candidate.directory)
            discovered.archived.pop(candidate.id, None)
        if self.aliases != discovered.aliases or self.legacy_modes != discovered.legacy_modes:
            raise KoraError('La resolución de identidades o modos históricos cambió durante la operación')
        for identifier, targets in self._consumers.items():
            for target in targets:
                discovered.require_available(identifier, target)
        for captured, resolved in self._snapshots.values():
            try:
                active = captured.id in self.products
                current_identity = discovered._lookup(captured.id)
                previous_identity = self._lookup(captured.id)
                if (active != (captured.id in discovered.products)
                        or current_identity.directory != previous_identity.directory):
                    raise KoraError(f'La identidad cambió de ubicación o disponibilidad: {captured.id}')
                if captured.directory.resolve() != resolved:
                    raise KoraError(f'La referencia cambió de versión: {captured.id}')
                current = read_product(captured.directory, captured.revision,
                                       captured.reference_root, captured.legacy_modes)
                if current.fingerprint(portable=False) != captured.fingerprint(portable=False):
                    raise KoraError(f'La fuente cambió durante la operación: {captured.id}')
                if current.kind != 'knowledge' and current.revision is not None:
                    self._verify_reference(current)
            except (OSError, KoraError) as error:
                raise KoraError(f'La fuente cambió durante la operación: {captured.id}: {error}') from error

    def preconditions(self):
        if not self.in_phase:
            raise KoraError('Las precondiciones requieren una fase de preparación activa')
        return [{'id': product.id, 'kind': product.kind, 'revision': product.revision,
                 'path': str(product.directory), 'resolved': str(resolved),
                 'fingerprint': product.fingerprint(portable=False)}
                for product, resolved in self._snapshots.values()] + [
                    {'id': identifier, 'target': target, 'check': 'consumer_availability'}
                    for identifier, targets in self._consumers.items() for target in sorted(targets)]

    def require_available(self, identifier, target):
        product = self._lookup(identifier)
        if product.id not in self.products:
            raise KoraError(f'Consumidor archivado: {identifier}')
        if target not in product.targets:
            raise KoraError(f'Consumidor incompatible con {target}: {identifier}')
        if self.in_phase:
            self._consumers.setdefault(product.id, set()).add(target)
        return product

    @staticmethod
    def _check_publication(product):
        publication = product.metadata.get('publication', {})
        if product.kind != 'knowledge' or not isinstance(publication, dict) or publication.get('status') not in {'approved', 'legacy'}:
            raise KoraError(f'Referencia sin publicación: {product.id}')
        if publication.get('hash_mode') not in (None, 'git-v1'):
            raise KoraError(f'Formato de hash desconocido: {product.id}')
        return publication

    @staticmethod
    def _verify_reference(product):
        if product.kind != 'knowledge':
            from .product_versions import verify
            verify(product)
            return
        publication = Catalog._check_publication(product)
        portable = publication.get('hash_mode') == 'git-v1'
        modes = None if portable else product.legacy_modes
        if (product.fingerprint(portable=portable, legacy_modes=modes) != product.revision
                or reference_digest(product, portable=portable, legacy_modes=modes) != publication.get('sha256')):
            migration_hint = ('; si es una clonación antigua, conserva legacy-modes.yaml desde la biblioteca original'
                              if not portable and modes is None else '')
            raise KoraError(f'Versión publicada modificada: {product.id}; recupera sus bytes desde Git '
                            f'o una copia intacta antes de preparar un borrador con revise{migration_hint}')

    def at_revision(self, identifier: str, revision: str) -> Product:
        current = self._lookup(identifier)
        if current.kind != 'knowledge':
            from .product_versions import at_revision
            return self.capture(at_revision(self.root, current, revision))
        if current.reference_root is None or not re.fullmatch(r'[0-9a-f]{64}', revision):
            raise KoraError(f'Revisión de conocimiento inválida: {revision}')
        directory = current.reference_root / 'versions' / current.directory.parent.name / current.directory.name / revision
        modes = self.legacy_modes[current.reference_root].get(revision)
        item = read_product(directory, revision, current.reference_root, modes)
        if item.id != current.id:
            raise KoraError(f'La revisión no pertenece a {current.id}')
        return self.capture(item)

    def _lookup(self, identifier: str) -> Product:
        """Contain a foreign defect only when its identity is provably disjoint."""
        if self._unknown:
            paths = ', '.join(issue['path'] for issue in self._unknown)
            raise KoraError(f'Identidad indeterminada: no se puede descartar una colisión con {identifier}: {paths}')
        seen = set()
        while True:
            if identifier in self._blocked:
                reasons = '; '.join(issue['error'] for issue in self._blocked[identifier])
                raise KoraError(f'Identidad defectuosa o ambigua {identifier}: {reasons}')
            if identifier not in self.aliases:
                break
            if identifier in seen:
                raise KoraError(f'Ciclo de alias: {identifier}')
            seen.add(identifier)
            identifier = self.aliases[identifier]
        try:
            return self.products[identifier] if identifier in self.products else self.archived[identifier]
        except KeyError as error:
            raise KoraError(f'Referencia ausente: {identifier}') from error

    def get(self, identifier: str) -> Product:
        return self.capture(self._lookup(identifier))

    def availability(self, identifier):
        if self._unknown:
            return 'indeterminate'
        if identifier in self._blocked:
            return 'ambiguous_or_malformed'
        try:
            product = self._lookup(identifier)
        except KoraError:
            return 'absent'
        return 'available' if product.id in self.products else 'retired'

    def explain(self, product: Product, target: str, capabilities=None) -> dict:
        if target not in ('codex', 'hermes'):
            raise KoraError(f'Destino desconocido: {target}')
        capabilities = self.capabilities if capabilities is None else frozenset(capabilities)
        result, edges = [], []
        seen = {product.id: product.revision}

        def visit(item):
            if item.id not in self.products:
                raise KoraError(f'Dependencia archivada sin realización activa: {item.id}')
            if item.kind != 'knowledge' and target not in item.targets:
                raise KoraError(f'{item.id} no tiene realización para {target}')
            for need in item.needs:
                edge = {'source': item.id, 'target': need.id, 'kind': need.kind,
                        'condition': need.condition, 'purpose': need.purpose, 'runtime': target,
                        'revision': need.revision, 'requested_revision': need.revision,
                        'status': 'not_applicable'}
                edges.append(edge)
                if need.target is not None and need.target != target:
                    continue
                old_seen, old_length, edge_start = dict(seen), len(result), len(edges)
                try:
                    if need.kind == 'capability':
                        if need.id not in capabilities:
                            raise KoraError(f'Capacidad no contrastada para {target}: {need.id}')
                        edge.update(status='available', evidence='declared_by_caller')
                        continue
                    dependency = self.at_revision(need.id, need.revision) if need.revision else self.get(need.id)
                    kind = 'knowledge' if dependency.kind == 'knowledge' else 'product'
                    if need.kind is not None and need.kind != kind:
                        raise KoraError(f'Tipo de necesidad incompatible: {need.id}; requiere {need.kind}, resuelve {kind}')
                    edge.update(kind=kind, revision=dependency.revision)
                    if dependency.id in seen:
                        if seen[dependency.id] != dependency.revision:
                            raise KoraError(f'Revisiones incompatibles de {dependency.id}')
                    else:
                        seen[dependency.id] = dependency.revision
                        visit(dependency)
                        result.append(dependency)
                    edge['status'] = 'available'
                except KoraError as error:
                    edge.update(status='unavailable', error=str(error))
                    if need.condition is None:
                        raise KoraError(f'{item.id} necesita {need.id}: {error}') from error
                    seen.clear()
                    seen.update(old_seen)
                    del result[old_length:]
                    for nested in edges[edge_start:]:
                        nested.update(status='unavailable', blocked_by=need.id)
        errors = []
        with self.phase():
            captured = self.capture(product)
            try:
                visit(captured)
            except KoraError as error:
                errors.append(str(error))
        return {'products': [*result, captured], 'edges': edges, 'available': not errors, 'errors': errors}

    def dependencies(self, product: Product, target: str) -> list[Product]:
        explanation = self.explain(product, target)
        if not explanation['available']:
            raise KoraError('; '.join(explanation['errors']))
        return [item for item in explanation['products'] if item.id != product.id]

    def reference_issues(self) -> list[dict]:
        issues = list(self.diagnostics)
        with self.phase():
            for product in [*self.products.values(), *self.archived.values()]:
                if product.revision is not None:
                    try:
                        self.capture(product)
                    except KoraError as error:
                        issues.append({'source': product.id, 'relation': 'integrity',
                                       'target': product.id, 'error': str(error)})
            for product in self.products.values():
                relations = [(relation, identifier) for relation, ids in product.metadata.get('relations', {}).items()
                             for identifier in ids if product.reference_root is None]
                for relation, identifier in relations:
                    try:
                        self._lookup(identifier)
                    except KoraError as error:
                        issues.append({'source': product.id, 'relation': relation,
                                       'target': identifier, 'error': str(error)})
                for need in product.needs:
                    if need.kind == 'capability':
                        continue
                    try:
                        dependency = self.at_revision(need.id, need.revision) if need.revision else self._lookup(need.id)
                        if product.reference_root is not None and dependency.kind != 'knowledge':
                            raise KoraError('El conocimiento de referencia no depende de agentes ni skills')
                    except KoraError as error:
                        if need.condition is None:
                            issues.append({'source': product.id, 'relation': 'requires',
                                           'target': need.id, 'error': str(error)})
        return issues
