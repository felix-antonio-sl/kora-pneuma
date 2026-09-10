"""Prepare native realizations and their material effects, without applying them."""

from dataclasses import replace
import re

from .catalog import Catalog, File, KoraError, safe_relative


def _profile_name(target: str, profile: str | None) -> str | None:
    if profile is None:
        return None
    if target != "hermes":
        raise KoraError("--profile solo está disponible para skills de Hermes")
    profile = profile.strip().lower()
    if profile == "default":
        raise KoraError("El perfil default es la raíz de Hermes; omitir --profile")
    # Matches named profile IDs in the installed Hermes, without importing it.
    if not re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,63}", profile) or profile in {
        "hermes", "test", "tmp", "root", "sudo"
    }:
        raise KoraError(f"Nombre de perfil Hermes inválido: {profile!r}")
    return profile


def _bundle_key(target: str, identifier: str, profile: str | None = None) -> str:
    return f"hermes@profile:{profile}:{identifier}" if profile is not None else f"{target}:{identifier}"


def _selection(catalog: Catalog, target: str, identifiers, profile):
    selected = ([catalog.get(identifier) for identifier in identifiers] if identifiers else
                [catalog.get(p.id) for p in catalog.products.values() if p.kind != "knowledge" and target in p.targets
                 and (profile is None or p.kind == "skill")])
    if profile is not None and any(product.kind != "skill" for product in selected):
        raise KoraError("--profile solo admite productos skill; no cambia el perfil de un agente")
    return [(product, profile) for product in selected]


def _build_instances_in_phase(catalog: Catalog, target: str, instances) -> dict[str, dict[str, File]]:
    if target == "codex":
        from .render_codex import render
    elif target == "hermes":
        from .render_hermes import render
    else:
        raise KoraError(f"Destino desconocido: {target}")
    instances = [(catalog.capture(product), profile) for product, profile in instances]
    for product, profile in instances:
        if profile is not None and product.kind != "skill":
            raise KoraError(f"La instancia del perfil {profile} requiere una skill activa: {product.id}")
    bundles = {}
    for product, profile in instances:
        files = render(catalog, product)
        pins = {edge["target"]: edge["requested_revision"]
                for edge in catalog.explain(product, target)["edges"]
                if edge["status"] == "available" and edge["requested_revision"]}
        files = {path: replace(file, source={**file.source,
                                             "pinned_revision": pins.get(file.source["id"])})
                 if file.source else file for path, file in files.items()}
        if profile is not None:
            prefix = ".hermes/skills/"
            if any(not path.startswith(prefix) for path in files):
                raise KoraError(f"La realización de skill invade otro ámbito: {product.id}")
            files = {f".hermes/profiles/{profile}/skills/{path[len(prefix):]}": file
                     for path, file in files.items()}
        bundles[_bundle_key(target, product.id, profile)] = files
    # Check physical collisions before any output directory or runtime is touched.
    flat = {}
    for files in bundles.values():
        for relative, file in files.items():
            safe_relative(relative)
            if relative in flat and flat[relative] != file:
                raise KoraError(f"Colisión de realización en {target}: {relative}")
            flat[relative] = file
    return bundles


def _build_instances(catalog: Catalog, target: str, instances):
    owns_phase = not catalog.in_phase
    with catalog.phase():
        bundles = _build_instances_in_phase(catalog, target, instances)
        if owns_phase:
            catalog.revalidate()
        return bundles


def build(catalog: Catalog, target: str, identifiers=(), *, profile=None) -> dict[str, dict[str, File]]:
    profile = _profile_name(target, profile)
    return _build_instances(catalog, target, _selection(catalog, target, identifiers, profile))
