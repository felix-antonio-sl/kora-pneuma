"""Realización pura de productos KORA en archivos nativos de Hermes."""

from __future__ import annotations

from pathlib import Path, PurePosixPath
import re
import shlex

import yaml

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
    if dependencies:
        lines.extend(["", "Dependencias disponibles:", ""])
    for dependency in dependencies:
        if dependency.kind == "skill":
            lines.append(
                f"- `{dependency.id}`: carga la skill nativa `{dependency.name}` "
                "con `skill_view` cuando corresponda a la tarea."
            )
        elif dependency.kind == "knowledge":
            lines.append(
                f"- `{dependency.id}`: lee `{dependency.content_path.absolute()}` "
                "cuando necesites ese conocimiento; sus recursos relativos se resuelven "
                "desde el directorio del archivo."
            )
        else:
            raise KoraError(f"Tipo de dependencia no realizable en Hermes: {dependency.kind}")
    if any(p.reference_root is not None for p in dependencies):
        library = next(p.reference_root for p in dependencies if p.reference_root is not None)
        entrypoint = catalog.root / "kora_cli.py"
        if not entrypoint.is_file():
            entrypoint = Path(__file__).resolve().parents[1] / "kora_cli.py"
        resolver = shlex.join(["python3", str(entrypoint),
                               "--root", str(library), "resolve", "URN"])
        lines += ["", "El conocimiento publicado es de consulta. Su `object.yaml` indica "
                  "el estado de publicación; `legacy` conserva disponibilidad sin una nueva aprobación. "
                  "Para editarlo prepara un borrador con KORA; conserva la referencia vigente hasta aprobar la revisión.",
                  f"Resuelve otras identidades y las referencias que añada el conocimiento con `{resolver}`."]
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
    return files


def render(catalog: Catalog, product: Product) -> dict[str, File]:
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
        files[manifest_name] = File(
            yaml.safe_dump(manifest, allow_unicode=True, sort_keys=False).encode("utf-8")
        )
    return files
