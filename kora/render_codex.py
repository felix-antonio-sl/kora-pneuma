"""Render KORA products to the native files consumed by Codex."""

from __future__ import annotations

import json
from pathlib import Path
import re
import tomllib

import yaml

from .render_common import availability_note, resolver_note, sourced_files

from .catalog import Catalog, File, Product


def _resource_instructions(catalog: Catalog, product: Product, dependencies: list[Product]) -> str:
    lines = [
        "## Recursos locales KORA",
        "",
        f"Identidad: `{product.id}`.",
        f"Fuente de estas instrucciones: `{product.content_path.resolve()}`.",
        "Las referencias relativas del cuerpo se interpretan desde el directorio "
        "de esa fuente. Lee los recursos necesarios para el encargo.",
    ]
    if dependencies:
        lines += ["", "Dependencias disponibles en este host:", ""]
        for dependency in dependencies:
            suffix = (
                f"; skill nativa `${dependency.name}`"
                if dependency.kind == "skill"
                else ""
            )
            lines.append(
                f"- `{dependency.id}` → `{dependency.content_path.absolute()}`{suffix}."
            )
    lines += resolver_note(catalog, dependencies)
    lines += availability_note(catalog, product, "codex")
    return "\n".join(lines) + "\n"


def _instructions(catalog: Catalog, product: Product, dependencies: list[Product]) -> str:
    # The source body remains an exact prefix, including its trailing whitespace.
    return product.body + "\n\n" + _resource_instructions(catalog, product, dependencies)


def _skill_files(product: Product, instructions: str, description: str) -> dict[str, File]:
    if not description.strip() or len(description) > 1024:
        raise ValueError(f"{product.id}: descripción de skill fuera de 1–1024 caracteres")
    root = f".agents/skills/{product.name}"
    header = {"name": product.name, "description": description}
    frontmatter = yaml.safe_dump(
        header, allow_unicode=True, sort_keys=False, width=1000
    )
    if yaml.safe_load(frontmatter) != header:
        raise ValueError(f"{product.id}: frontmatter YAML no reversible")
    files = {f"{root}/{path}": item for path, item in product.resources().items()}
    main = f"{root}/SKILL.md"
    if main in files:
        raise ValueError(f"{product.id}: un recurso colisiona con SKILL.md")
    files[main] = File(f"---\n{frontmatter}---\n\n{instructions}".encode())
    return files


def _render_product(catalog: Catalog, product: Product) -> dict[str, File]:
    dependencies = catalog.dependencies(product, "codex")
    if product.kind == "knowledge":
        return {}
    if "codex" not in product.targets:
        raise ValueError(f"{product.id}: no admite el destino codex")
    if (
        not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", product.name)
        or len(product.name) > 64
    ):
        raise ValueError(f"{product.id}: nombre nativo inseguro: {product.name!r}")

    instructions = _instructions(catalog, product, dependencies)
    if product.kind == "skill":
        return sourced_files(product, _skill_files(product, instructions, product.description))

    if product.kind == "agent":
        fields = {
            "name": product.name,
            "description": product.description,
            "developer_instructions": instructions,
        }
        # JSON basic strings are valid TOML after escaping DEL as well.
        encoded = "".join(
            f"{key} = {json.dumps(value, ensure_ascii=False).replace(chr(127), r'\u007f')}\n"
            for key, value in fields.items()
        )
        if tomllib.loads(encoded) != fields:
            raise ValueError(f"{product.id}: agente TOML no reversible")
        activation = instructions + (
            "\n## Activación en esta sesión\n\n"
            "Esta skill carga la perspectiva y la conducta de la fuente en la sesión actual. "
            "No crea un proceso ni un agente separado, ni aplica las opciones de modelo "
            "o sandbox del rol personalizado. La sesión conserva sus instrucciones "
            "y permisos efectivos.\n"
        )
        description = (
            f"Activa la perspectiva y conducta de {product.name} en la sesión actual "
            "cuando el usuario pide actuar directamente como este agente; "
            "para delegar se usa el tipo nativo."
        )
        files = _skill_files(product, activation, description)
        files[f".codex/agents/{product.name}.toml"] = File(encoded.encode())
        return sourced_files(product, files)

    raise ValueError(f"{product.id}: tipo de producto desconocido: {product.kind}")


def _render(catalog: Catalog, product: Product) -> dict[str, File]:
    """Return this product and its dependency closure as files relative to HOME.

    This function does not write anything. Knowledge stays in the source
    catalog and is exposed through concrete readable paths.
    """
    dependencies = catalog.dependencies(product, "codex")
    files: dict[str, File] = {}
    for item in [*dependencies, product]:
        for path, file in _render_product(catalog, item).items():
            if path in files and files[path] != file:
                raise ValueError(f"Dos productos distintos colisionan en {path}")
            files[path] = file
    return files


def render(catalog: Catalog, product: Product) -> dict[str, File]:
    owns_phase = not catalog.in_phase
    with catalog.phase():
        files = _render(catalog, catalog.capture(product))
        if owns_phase:
            catalog.revalidate()
        return files
