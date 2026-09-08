"""The small operational interface for source, realization and recovery."""

import argparse
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile

from .atomic import rename_new
from .authoring import create
from .catalog import Catalog, File, KoraError, digest, safe_relative, knowledge_root
from .install import Installer


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
                [p for p in catalog.products.values() if p.kind != "knowledge" and target in p.targets
                 and (profile is None or p.kind == "skill")])
    if profile is not None and any(product.kind != "skill" for product in selected):
        raise KoraError("--profile solo admite productos skill; no cambia el perfil de un agente")
    return [(product, profile) for product in selected]


def _build_instances(catalog: Catalog, target: str, instances) -> dict[str, dict[str, File]]:
    if target == "codex":
        from .render_codex import render
    elif target == "hermes":
        from .render_hermes import render
    else:
        raise KoraError(f"Destino desconocido: {target}")
    snapshots = {}
    for product, profile in instances:
        if profile is not None and product.kind != "skill":
            raise KoraError(f"La instancia del perfil {profile} requiere una skill activa: {product.id}")
        for member in [product, *catalog.dependencies(product, target)]:
            snapshots[member.id] = member.fingerprint(portable=False)
    bundles = {}
    for product, profile in instances:
        files = render(catalog, product)
        if profile is not None:
            prefix = ".hermes/skills/"
            if any(not path.startswith(prefix) for path in files):
                raise KoraError(f"La realización de skill invade otro ámbito: {product.id}")
            files = {f".hermes/profiles/{profile}/skills/{path[len(prefix):]}": file
                     for path, file in files.items()}
        bundles[_bundle_key(target, product.id, profile)] = files
    for identifier, fingerprint in snapshots.items():
        if catalog.get(identifier).fingerprint(portable=False) != fingerprint:
            raise KoraError(f"La fuente cambió durante realización: {identifier}")
    # Check physical collisions before any output directory or runtime is touched.
    flat = {}
    for files in bundles.values():
        for relative, file in files.items():
            safe_relative(relative)
            if relative in flat and flat[relative] != file:
                raise KoraError(f"Colisión de realización en {target}: {relative}")
            flat[relative] = file
    return bundles


def build(catalog: Catalog, target: str, identifiers=(), *, profile=None) -> dict[str, dict[str, File]]:
    profile = _profile_name(target, profile)
    return _build_instances(catalog, target, _selection(catalog, target, identifiers, profile))


def _installation_bundles(catalog: Catalog, target: str, identifiers, installed, profile=None):
    instances = _selection(catalog, target, identifiers, profile)

    def references(identifier):
        # Establish relevance first. Only selected sources must be realizable;
        # an archived or absent unrelated source does not block a focal update.
        found, pending = set(), [identifier]
        while pending:
            identifier = pending.pop()
            if identifier in found:
                continue
            found.add(identifier)
            try:
                product = catalog.get(identifier)
            except KoraError:
                continue
            found.add(product.id)
            pending.extend(product.requires)
        return found

    selected = {_bundle_key(target, product.id, place) for product, place in instances}
    candidates = []
    for bundle in installed:
        place = None
        if bundle.startswith(f"{target}:"):
            identifier = bundle[len(target) + 1:]
        elif target == "hermes" and bundle.startswith("hermes@profile:"):
            place, separator, identifier = bundle[len("hermes@profile:"):].partition(":")
            if not separator or not identifier:
                raise KoraError(f"Recibo de instancia Hermes inválido: {bundle}")
            place = _profile_name(target, place)
        else:
            continue
        if profile is not None and place != profile:
            continue
        if bundle not in selected:
            candidates.append((identifier, place, references(identifier), set(installed[bundle])))

    while True:
        bundles = _build_instances(catalog, target, instances)
        affected = set().union(*(references(product.id) for product, _ in instances))
        affected_paths = set().union(*(set(files) | set(installed.get(key, {}))
                                      for key, files in bundles.items()))
        # Previous ownership is physical. Equal skill names in different Hermes
        # profiles do not establish identity; current references connect copies.
        remaining = []
        for identifier, place, required, previous_paths in candidates:
            if not identifiers or affected & required or affected_paths & previous_paths:
                instances.append((catalog.get(identifier), place))
            else:
                remaining.append((identifier, place, required, previous_paths))
        if len(remaining) == len(candidates):
            return bundles
        candidates = remaining


def emit(bundles, output: Path):
    output = Path(output).absolute()
    if output.exists() or output.is_symlink():
        raise KoraError(f"La salida ya existe; usar un directorio nuevo: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=".kora-render-", dir=output.parent))
    files = {}
    try:
        for members in bundles.values():
            for relative, file in members.items():
                if relative in files and files[relative] != file:
                    raise KoraError(f"Colisión de salida: {relative}")
                files[relative] = file
        for relative, file in files.items():
            path = temporary / safe_relative(relative)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(file.data)
            path.chmod(file.mode)
        if output.exists() or output.is_symlink():
            raise KoraError(f"La salida apareció durante realización: {output}")
        try:
            rename_new(temporary, output)
        except FileExistsError as error:
            raise KoraError(f"La salida apareció durante realización: {output}") from error
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)
    return {"output": str(output), "files": len(files), "bundles": sorted(bundles)}


def parser():
    result = argparse.ArgumentParser(description="KORA: fuentes, productos nativos y recuperación")
    result.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="Raíz de la maquinaria o de un corpus independiente")
    result.add_argument("--knowledge-root", type=Path, help="Biblioteca de referencia; por defecto el enlace knowledge de la raíz")
    commands = result.add_subparsers(dest="command", required=True)
    listing = commands.add_parser("list", help="Derivar catálogo desde los archivos")
    listing.add_argument("--kind", choices=["knowledge", "skill", "agent"])
    listing.add_argument("--target", choices=["codex", "hermes"])
    listing.add_argument("--archived", action="store_true")
    resolve = commands.add_parser("resolve", help="Resolver identidad a archivo de contenido")
    resolve.add_argument("id")
    resolve.add_argument("--revision", help="Consultar una versión exacta de conocimiento")
    intake = commands.add_parser("intake", help="Conservar recursos de entrada sin publicarlos")
    intake.add_argument("name")
    intake.add_argument("--source", type=Path, required=True, action="append")
    for name, help_text in (("revise", "Preparar un borrador conservando la referencia vigente"),
                            ("review", "Mostrar el borrador y el hash de los archivos a revisar"),
                            ("approve", "Publicar el contenido cuya aprobación fue autorizada")):
        command = commands.add_parser(name, help=help_text)
        command.add_argument("id")
        if name == "approve":
            command.add_argument("--reviewed", required=True, help="SHA-256 de la revisión concreta aprobada")
    author = commands.add_parser("create", help="Crear una fuente con cuerpo autorado y originales recuperables")
    author.add_argument("kind", choices=["knowledge", "skill", "agent"])
    author.add_argument("namespace")
    author.add_argument("name")
    author.add_argument("--id", required=True)
    author.add_argument("--description", required=True)
    author.add_argument("--body", type=Path, required=True)
    author.add_argument("--source", type=Path, action="append", default=[])
    author.add_argument("--target", choices=["codex", "hermes"], action="append", default=[])
    author.add_argument("--requires", action="append", default=[])
    check = commands.add_parser("check", help="Comprobar referencias y realizaciones; no acredita semántica ni conducta")
    check.add_argument("--target", choices=["codex", "hermes"], action="append")
    render = commands.add_parser("render", help="Producir archivos nativos en una salida nueva")
    render.add_argument("target", choices=["codex", "hermes"])
    render.add_argument("ids", nargs="*")
    render.add_argument("--output", type=Path, required=True)
    render.add_argument("--profile", help="Realizar skills dentro de un perfil nombrado de Hermes")
    install = commands.add_parser("install", help="Instalar o actualizar conservando cambios locales")
    install.add_argument("target", choices=["codex", "hermes"])
    install.add_argument("ids", nargs="*")
    install.add_argument("--home", type=Path, default=Path.home())
    install.add_argument("--adopt", type=Path, help="Mapa revisado de paths existentes y sus SHA-256")
    install.add_argument("--profile", help="Instalar una instancia de skills en un perfil de Hermes")
    remove = commands.add_parser("remove", help="Retirar solo archivos propios intactos")
    remove.add_argument("target", choices=["codex", "hermes"])
    remove.add_argument("ids", nargs="+")
    remove.add_argument("--home", type=Path, default=Path.home())
    remove.add_argument("--profile", help="Retirar solo la instancia de skills de este perfil Hermes")
    for name, help_text in (("status", "Detectar cambios en archivos instalados"),
                            ("recover", "Recuperar una instalación interrumpida"),
                            ("rollback", "Deshacer la última instalación sin perder cambios posteriores")):
        command = commands.add_parser(name, help=help_text)
        command.add_argument("--home", type=Path, default=Path.home())
    return result


def execute(args):
    if args.command in ("status", "recover", "rollback"):
        return getattr(Installer(args.home), args.command)()
    profile = (_profile_name(args.target, getattr(args, "profile", None))
               if args.command in ("render", "install", "remove") else None)
    if args.command == "remove":
        installer = Installer(args.home)
        installed = set(installer.status()["bundles"])
        catalog = None
        bundles = []
        for identifier in args.ids:
            bundle = _bundle_key(args.target, identifier, profile)
            if bundle not in installed:
                # A recorded canonical ID remains removable even without its
                # source. Historical aliases resolve just as they do on install.
                catalog = catalog or Catalog(args.root, knowledge=args.knowledge_root)
                product = catalog.get(identifier)
                if profile is not None and product.kind != "skill":
                    raise KoraError("--profile solo admite productos skill")
                bundle = _bundle_key(args.target, product.id, profile)
            bundles.append(bundle)
        return installer.apply({}, remove=bundles)
    if args.command == "create":
        if args.kind == "knowledge":
            from .knowledge import create_draft
            if args.target:
                raise KoraError("El conocimiento de referencia no tiene runtime de destino")
            item = create_draft(knowledge_root(args.root, args.knowledge_root), args.namespace, args.name,
                                args.id, args.description, args.body, sources=args.source, requires=args.requires)
            return {"id": item.id, "path": str(item.content_path), "publication": "draft"}
        item = create(args.root, args.kind, args.namespace, args.name, args.id, args.description, args.body,
                      sources=args.source, targets=args.target, requires=args.requires, knowledge=args.knowledge_root)
        return {"id": item.id, "path": str(item.content_path)}
    if args.command in ("intake", "revise", "review", "approve"):
        from . import knowledge
        root = knowledge_root(args.root, args.knowledge_root)
        if args.command == "intake":
            return knowledge.intake(root, args.name, args.source)
        if args.command == "review":
            return knowledge.review(root, args.id)
        item = (knowledge.revise(root, args.id) if args.command == "revise" else
                knowledge.approve(root, args.id, args.reviewed))
        return {"id": item.id, "path": str(item.content_path), "revision": item.revision,
                "publication": item.metadata.get("publication", {}).get("status", "draft")}
    catalog = Catalog(args.root, knowledge=args.knowledge_root)
    if args.command == "resolve":
        product = catalog.at_revision(args.id, args.revision) if args.revision else catalog.get(args.id)
        return {"id": product.id, "path": str(product.content_path), "active": product.id in catalog.products,
                "revision": product.revision,
                "publication": product.metadata.get("publication", {}).get("status")}
    if args.command == "list":
        products = catalog.archived if args.archived else catalog.products
        return [{"id": p.id, "kind": p.kind, "name": p.name, "targets": p.targets, "path": str(p.content_path),
                 "publication": p.metadata.get("publication", {}).get("status")}
                for p in products.values() if (not args.kind or p.kind == args.kind) and
                (not args.target or args.target in p.targets)]
    if args.command == "check":
        issues = catalog.reference_issues()
        for target in args.target or ("codex", "hermes"):
            target_failed = False
            for product in catalog.products.values():
                if product.kind != "knowledge" and target in product.targets:
                    try:
                        build(catalog, target, [product.id])
                    except (KoraError, ValueError) as error:
                        issues.append({"source": product.id, "target": target, "error": str(error)})
                        target_failed = True
            if not target_failed:
                try:
                    build(catalog, target)
                except (KoraError, ValueError) as error:
                    issues.append({"target": target, "error": str(error)})
        return {"ok": not issues, "active": len(catalog.products), "archived": len(catalog.archived), "issues": issues}
    if args.command == "render":
        bundles = build(catalog, args.target, args.ids, profile=profile)
        return emit(bundles, args.output)
    if args.command == "install":
        installer = Installer(args.home)
        bundles = _installation_bundles(catalog, args.target, args.ids,
                                        installer.receipts(), profile)
        adoption = json.loads(args.adopt.read_text()) if args.adopt else None
        return installer.apply(bundles, adopt=adoption)
    raise KoraError(f"Comando desconocido: {args.command}")


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        result = execute(args)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1 if isinstance(result, dict) and result.get("ok") is False else 0
    except (KoraError, OSError, ValueError) as error:
        print(f"KORA: {error}", file=sys.stderr)
        return 1
