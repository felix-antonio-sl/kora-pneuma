"""Read authored products and resolve the dependencies their consumers need."""

from dataclasses import dataclass
import hashlib
from pathlib import Path, PurePosixPath
import re
import stat

import yaml


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


def read_yaml(path: Path):
    try:
        return yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueLoader)
    except (OSError, UnicodeError, yaml.YAMLError) as error:
        raise KoraError(f"No se pudo leer YAML: {path}: {error}") from error


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_relative(value: str) -> Path:
    if not isinstance(value, str) or not value or "\\" in value:
        raise KoraError(f"Ruta relativa inválida: {value!r}")
    path = PurePosixPath(value)
    if path.is_absolute() or any(p in ("..", ".", "") for p in value.split("/")):
        raise KoraError(f"Ruta fuera del producto o instalación: {value}")
    return Path(*path.parts)


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


@dataclass(frozen=True)
class Product:
    directory: Path
    metadata: dict
    revision: str | None = None
    reference_root: Path | None = None

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
    def content_path(self):
        return contained_file(self.directory, self.metadata["content"])

    @property
    def body(self):
        try:
            return self.content_path.read_bytes().decode("utf-8")
        except UnicodeError as error:
            raise KoraError(f"Contenido binario; usar el recurso original: {self.id}") from error

    def resources(self) -> dict[str, File]:
        resources = {}
        for path in sorted(self.directory.rglob("*")):
            if path.is_symlink():
                raise KoraError(f"Recurso enlazado requiere importación explícita: {path}")
            if not path.is_file() or path in (self.directory / "object.yaml", self.content_path):
                continue
            resources[path.relative_to(self.directory).as_posix()] = File(
                path.read_bytes(), stat.S_IMODE(path.stat().st_mode))
        return resources

    def fingerprint(self) -> str:
        if read_yaml(self.directory / "object.yaml") != self.metadata:
            raise KoraError(f"La ficha cambió durante la operación: {self.id}")
        h = hashlib.sha256()
        for path in sorted(self.directory.rglob("*")):
            if path.is_symlink():
                raise KoraError(f"Recurso enlazado: {path}")
            if path.is_file():
                h.update(path.relative_to(self.directory).as_posix().encode() + b"\0")
                h.update(str(stat.S_IMODE(path.stat().st_mode)).encode() + b"\0")
                h.update(path.read_bytes())
        return h.hexdigest()


def reference_digest(product: Product) -> str:
    """Identify exactly the reviewed metadata, content and resources, before approval."""
    if read_yaml(product.directory / "object.yaml") != product.metadata:
        raise KoraError(f"La ficha cambió durante la operación: {product.id}")
    metadata = {k: v for k, v in product.metadata.items() if k != "publication"}
    h = hashlib.sha256(yaml.safe_dump(metadata, allow_unicode=True, sort_keys=True).encode())
    files = {product.metadata["content"]: File(product.content_path.read_bytes(),
              stat.S_IMODE(product.content_path.stat().st_mode)), **product.resources()}
    for relative, file in sorted(files.items()):
        h.update(relative.encode() + b"\0" + str(file.mode).encode() + b"\0")
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


def read_product(directory: Path, revision=None, reference_root=None) -> Product:
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
    for key in ("targets", "requires"):
        value = metadata.get(key, [])
        if not isinstance(value, list) or any(not isinstance(x, str) or not x for x in value):
            raise KoraError(f"{path}: {key} debe ser una lista de textos")
    if set(metadata.get("targets", [])) - {"codex", "hermes"}:
        raise KoraError(f"{path}: destinos admitidos: codex, hermes")
    relations = metadata.get("relations", {})
    if not isinstance(relations, dict) or any(
        not isinstance(v, list) or any(not isinstance(x, str) for x in v) for v in relations.values()
    ):
        raise KoraError(f"{path}: relaciones debe mapear tipo a lista de identidades")
    product = Product(directory, metadata, revision, reference_root)
    product.content_path
    return product


class Catalog:
    def __init__(self, root: Path, *, knowledge: Path | None = None):
        self.root = Path(root).resolve()
        self.knowledge_root = knowledge_root(self.root, knowledge)
        self.products: dict[str, Product] = {}
        self.archived: dict[str, Product] = {}
        self.aliases = {}
        roots = [self.root] if self.knowledge_root == self.root else [self.root, self.knowledge_root]
        for source in roots:
            aliases = read_yaml(source / "aliases.yaml") if (source / "aliases.yaml").exists() else {}
            if not isinstance(aliases, dict):
                raise KoraError("aliases.yaml debe mapear identidad anterior a identidad conservada")
            if self.aliases.keys() & aliases.keys():
                raise KoraError("Alias duplicado entre maquinaria y conocimiento")
            self.aliases.update(aliases)
        paths = []
        for active, relative in ((True, "products"), (False, "archive/products")):
            container = self.root / relative
            paths.extend((p, active, container, None, None) for p in sorted(container.rglob("object.yaml")))
        for source in roots:
            for active, relative in ((True, "references"), (False, "archive/references")):
                container = source / relative
                for reference in sorted(container.glob("*/*")):
                    if not reference.is_symlink():
                        raise KoraError(f"Una referencia debe enlazar una versión publicada: {reference}")
                    resolved = reference.resolve()
                    expected = source / "versions" / reference.parent.name / reference.name / resolved.name
                    if resolved != expected or not re.fullmatch(r"[0-9a-f]{64}", resolved.name):
                        raise KoraError(f"Referencia fuera de sus versiones: {reference}")
                    paths.append((reference / "object.yaml", active, container, resolved.name, source))
        for path, active, container, revision, reference_root in paths:
            if path.is_symlink() or (revision is None and not path.resolve().is_relative_to(container)):
                raise KoraError(f"Ficha fuera de products: {path}")
            product = read_product(path.parent, revision, reference_root)
            if self.knowledge_root != self.root and revision is None and product.kind == "knowledge":
                raise KoraError(f"Conocimiento fuera de la biblioteca central: {product.id}")
            if revision is not None:
                self._check_publication(product)
            if product.id in self.products or product.id in self.archived or product.id in self.aliases:
                raise KoraError(f"Identidad duplicada: {product.id}")
            (self.products if active else self.archived)[product.id] = product
        for alias in self.aliases:
            self._lookup(alias)

    @staticmethod
    def _check_publication(product):
        publication = product.metadata.get("publication", {})
        if product.kind != "knowledge" or not isinstance(publication, dict) or publication.get("status") not in {"approved", "legacy"}:
            raise KoraError(f"Referencia sin publicación: {product.id}")
        return publication

    @staticmethod
    def _verify_reference(product):
        publication = Catalog._check_publication(product)
        if product.fingerprint() != product.revision or reference_digest(product) != publication.get("sha256"):
            raise KoraError(f"Versión publicada modificada: {product.id}; recupera sus bytes desde Git "
                            "o una copia intacta antes de preparar un borrador con revise")

    def at_revision(self, identifier: str, revision: str) -> Product:
        current = self._lookup(identifier)
        if current.reference_root is None or not re.fullmatch(r"[0-9a-f]{64}", revision):
            raise KoraError(f"Revisión de conocimiento inválida: {revision}")
        directory = current.reference_root / "versions" / current.directory.parent.name / current.directory.name / revision
        item = read_product(directory, revision, current.reference_root)
        if item.id != current.id:
            raise KoraError(f"La revisión no pertenece a {current.id}")
        self._verify_reference(item)
        return item

    def _lookup(self, identifier: str) -> Product:
        """Resolve identity and aliases without reading unrelated reference bodies."""
        seen = set()
        while identifier in self.aliases:
            if identifier in seen:
                raise KoraError(f"Ciclo de alias: {identifier}")
            seen.add(identifier)
            identifier = self.aliases[identifier]
            if not isinstance(identifier, str):
                raise KoraError("El destino de un alias debe ser una identidad")
        try:
            return self.products[identifier] if identifier in self.products else self.archived[identifier]
        except KeyError as error:
            raise KoraError(f"Referencia ausente: {identifier}") from error

    def get(self, identifier: str) -> Product:
        product = self._lookup(identifier)
        if product.revision is not None:
            self._verify_reference(product)
        return product

    def dependencies(self, product: Product, target: str) -> list[Product]:
        if target not in ("codex", "hermes"):
            raise KoraError(f"Destino desconocido: {target}")
        if product.revision is not None:
            self._verify_reference(product)
        result = []
        seen = {product.id}

        def visit(item):
            if item.id not in self.products:
                raise KoraError(f"Dependencia archivada sin realización activa: {item.id}")
            if item.kind != "knowledge" and target not in item.targets:
                raise KoraError(f"{item.id} no tiene realización para {target}")
            for identifier in item.requires:
                dependency = self.get(identifier)
                if dependency.id not in seen:
                    seen.add(dependency.id)
                    visit(dependency)
                    result.append(dependency)

        visit(product)
        return result

    def reference_issues(self) -> list[dict]:
        issues = []
        # A full check is explicit; consulting one reference need not hash the library.
        for product in [*self.products.values(), *self.archived.values()]:
            if product.revision is not None:
                try:
                    self._verify_reference(product)
                except KoraError as error:
                    issues.append({"source": product.id, "relation": "integrity",
                                   "target": product.id, "error": str(error)})
        for product in self.products.values():
            relations = {**product.metadata.get("relations", {}), "requires": list(product.requires)}
            for relation, identifiers in relations.items():
                for identifier in identifiers:
                    # A documentary citation can name something outside the library.
                    # Only requires makes its availability an operational obligation.
                    if product.reference_root is not None and relation != "requires":
                        continue
                    try:
                        dependency = self._lookup(identifier)
                        if product.reference_root is not None and relation == "requires" and dependency.kind != "knowledge":
                            raise KoraError("El conocimiento de referencia no depende de agentes ni skills")
                    except KoraError as error:
                        issues.append({"source": product.id, "relation": relation,
                                       "target": identifier, "error": str(error)})
        return issues
