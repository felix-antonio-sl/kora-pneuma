"""Realización pura de productos KORA en archivos nativos de Hermes."""

from __future__ import annotations

from pathlib import Path, PurePosixPath
import re

import yaml

from .render_common import availability_note, resolver_note, sourced_files

from .catalog import Catalog, File, KoraError, Product


def _skill_name(product: Product) -> str:
    name = product.name
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        raise KoraError(f"Nombre de skill incompatible con Hermes: {name!r}")
    return name


def _dependencies(catalog: Catalog, product: Product) -> list[Product]:
    dependencies = catalog.dependencies(product, "hermes")
    for dependency in dependencies:
        if dependency.kind == "agent":
            raise KoraError(
                f"{product.id} requiere el agente {dependency.id}; "
                "un perfil Hermes no realiza esa invocación por declarar una dependencia"
            )
    return dependencies


def _source_note(catalog: Catalog, product: Product, dependencies: list[Product]) -> str:
    lines = [
        "", "", "## Fuente KORA", "",
        f"Identidad: `{product.id}`.",
        f"Fuente editable: `{product.content_path.resolve()}`.",
        "Este archivo es una realización; las actualizaciones se hacen desde su fuente.",
        f"Referencias relativas del cuerpo: base `{product.content_path.parent.resolve()}`; "
        "léelas con `read_file`. `skill_view` solo abre recursos internos del bundle instalado.",
    ]
    if product.kind == "agent" and product.resources():
        lines.extend([
            "", "Los recursos propios del agente se conservan bajo "
            "`$HERMES_HOME/resources/`, con la estructura relativa de la fuente.",
        ])
    by_identity: dict[str, list[dict]] = {}
    for edge in catalog.explain(product, "hermes")["edges"]:
        if edge["status"] == "not_applicable":
            continue
        key = edge.get("resolved_id") or edge["target"]
        by_identity.setdefault(key, []).append(edge)
    emitted: set[str] = set()
    known = {dependency.id for dependency in dependencies}
    if dependencies:
        lines.extend([
            "", "Dependencias disponibles:", "",
            "Cada conocimiento se lee por su path exacto cuando el encargo lo requiere; "
            "sus recursos relativos se resuelven desde el directorio del archivo. "
            "Cada skill nativa se carga con `skill_view` cuando corresponda a la tarea.", "",
        ])
    grouped: dict[tuple[bool, str], list[str]] = {}
    order: list[tuple[bool, str]] = []
    extras: list[str] = []

    def note_routing(edge: dict) -> str:
        resolved = edge.get("resolved_id") or edge["target"]
        if resolved != edge["target"]:
            return f" Resuelve a `{resolved}`."
        return ""

    def register(edge: dict, identity: str) -> None:
        if edge["status"] == "unavailable":
            scope = f"cuando {edge['condition']}" if edge.get("condition") else "necesidad obligatoria"
            text = (f"- Recorrido no disponible ({scope}): `{edge['target']}`. "
                    f"{edge.get('error', 'Depende de otro recorrido no disponible')}. "
                    f"Detén ese recorrido hasta satisfacer su necesidad.{note_routing(edge)}")
            if text not in emitted:
                emitted.add(text)
                extras.append(text)
            return
        is_capability = edge.get("kind") == "capability"
        condition = edge.get("condition")
        # Las capacidades disponibles sólo llegan si el llamador las declara en
        # explain(); render() no lo hace, pero se conservan igual que el baseline.
        if condition:
            resolved = edge.get("resolved_id") or edge["target"]
            display = f"`{identity}`" if identity == resolved else f"`{identity}` → `{resolved}`"
            key = (is_capability, condition)
            if key not in grouped:
                grouped[key] = []
                order.append(key)
            if display not in grouped[key]:
                grouped[key].append(display)
        elif is_capability:
            text = (f"- Capacidad `{edge['target']}` declarada por el llamador para esta preparación. "
                    "Su uso conserva los permisos efectivos del runtime y del encargo."
                    f"{note_routing(edge)}")
            if text not in emitted:
                emitted.add(text)
                extras.append(text)

    for dependency in dependencies:
        if dependency.kind == "skill":
            head = (f"- `{dependency.id}`: skill nativa `{dependency.name}` "
                    "(`skill_view`)")
        elif dependency.kind == "knowledge":
            head = f"- `{dependency.id}` → `{dependency.content_path.absolute()}`"
        else:
            raise KoraError(f"Tipo de dependencia no realizable en Hermes: {dependency.kind}")
        if head not in emitted:
            emitted.add(head)
            lines.append(head)
        for edge in by_identity.get(dependency.id, []):
            register(edge, edge["target"])
    for identity, group in by_identity.items():
        if identity in known:
            continue
        for edge in group:
            register(edge, edge["target"])
    lines.extend(extras)
    if order:
        lines.extend(["", "Condiciones: úsalo únicamente cuando ese caso corresponda al encargo.", ""])
        for is_capability, condition in order:
            urns = ", ".join(grouped[(is_capability, condition)])
            text = f"- Para {condition}: {urns}."
            if is_capability:
                text += (" Capacidad declarada por el llamador; su uso conserva los permisos "
                         "efectivos del runtime y del encargo.")
            if text not in emitted:
                emitted.add(text)
                lines.append(text)
    lines += resolver_note(catalog, dependencies)
    return "\n".join(lines) + "\n"


def _skill_files(catalog: Catalog, product: Product) -> dict[str, File]:
    _skill_name(product)
    description = product.description
    if not description.strip() or len(description) > 1024:
        raise KoraError(f"Descripción de skill incompatible con Hermes: {product.id}")
    metadata = {
        "name": product.name,
        "description": description,
        "metadata": {
            "kora_id": product.id,
            "kora_source": str(product.content_path.resolve()),
        },
    }
    header = yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False)
    body = product.body + _source_note(catalog, product, _dependencies(catalog, product))
    files = {"SKILL.md": File(("---\n" + header + "---\n\n" + body).encode("utf-8"))}
    for relative, resource in product.resources().items():
        path = PurePosixPath(relative)
        if path.is_absolute() or ".." in path.parts or not path.parts:
            raise KoraError(f"Recurso fuera del bundle: {relative}")
        if str(path) in files:
            raise KoraError(f"Recurso colisiona con un archivo nativo: {relative}")
        files[str(path)] = resource
    return sourced_files(product, files)


def _render(catalog: Catalog, product: Product) -> dict[str, File]:
    """Devuelve paths relativos al home del operador; nunca escribe ni configura Hermes.

    Los agentes realizan perfiles; sus skills requeridas quedan dentro del perfil.
    Las skills independientes y sus dependencias skill se realizan en la raíz de skills.
    El conocimiento permanece en la fuente accesible desde este mismo host.
    """
    if "hermes" not in product.targets:
        raise KoraError(f"{product.id} no declara el destino hermes")
    if product.kind not in {"agent", "skill"}:
        raise KoraError(f"Hermes realiza agentes y skills; recibió {product.kind}")
    dependencies = _dependencies(catalog, product)
    skills = [dependency for dependency in dependencies if dependency.kind == "skill"]
    if product.kind == "skill":
        skills.insert(0, product)
        base = PurePosixPath(".hermes")
        files: dict[str, File] = {}
    else:
        _skill_name(product)
        base = PurePosixPath(".hermes/profiles") / product.name
        soul = product.body + _source_note(catalog, product, dependencies)
        files = {str(base / "SOUL.md"): File(soul.encode("utf-8"))}
        for relative, resource in product.resources().items():
            files[str(base / "resources" / relative)] = resource
        files = sourced_files(product, files)
    names: dict[str, str] = {}
    for skill in skills:
        name = _skill_name(skill)
        if name in names and names[name] != skill.id:
            raise KoraError(f"Dos skills requeridas comparten el nombre Hermes {name!r}")
        names[name] = skill.id
        for relative, file in _skill_files(catalog, skill).items():
            path = str(base / "skills" / name / relative)
            if path in files and files[path] != file:
                raise KoraError(f"Dos realizaciones distintas colisionan en {path}")
            files[path] = file
    if product.kind == "agent":
        manifest_name = str(base / "distribution.yaml")
        manifest = {
            "name": product.name,
            "description": product.description,
            "distribution_owned": sorted(
                [str(PurePosixPath(path).relative_to(base)) for path in files]
                + ["distribution.yaml"]
            ),
        }
        if "version" in product.metadata:
            manifest["version"] = str(product.metadata["version"])
        files.update(sourced_files(product, {manifest_name: File(
            yaml.safe_dump(manifest, allow_unicode=True, sort_keys=False).encode("utf-8"))}))
    return files


def render(catalog: Catalog, product: Product) -> dict[str, File]:
    owns_phase = not catalog.in_phase
    with catalog.phase():
        files = _render(catalog, catalog.capture(product))
        if owns_phase:
            catalog.revalidate()
        return files
