"""One-time, read-only interpretation of legacy products; never imports their core."""

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import tempfile

import yaml

from .catalog import File, KoraError, UniqueLoader, digest, safe_relative


RELATIONS = ("cita", "depende", "refina", "reemplaza", "conocimiento", "componible")
KINDS = {"conocimiento": "knowledge", "agentes": "agent", "skills": "skill"}
PRIVATE_NAMES = {".remember", ".git", "__pycache__", ".env", "auth.json",
                 "memories", "sessions", "logs", "credentials", "secrets"}
URN = re.compile(r"urn:([a-z0-9-]+):(kb|artefacto):([a-z0-9-]+)\Z")
BODY_URN = re.compile(r"urn:[a-zA-Z0-9][a-zA-Z0-9:._/-]*\*?")
KODA_ALIAS = re.compile(r"URN KODA legado (urn:[a-zA-Z0-9:._/-]+)")

# Adjudicated by function against the inspected products, not by namespace.
# Original payloads remain recoverable until an explicit successor is authored.
MACHINERY = {
    "urn:kora:artefacto:kora": "Opera los gestos y el canon anteriores",
    "urn:dev:artefacto:agent-architect": "Autora contra la ley y forma anteriores",
    "urn:kora:artefacto:autoria-de-persona": "Autora personalidad y mapas de transmutación anteriores",
    "urn:kora:artefacto:auditoria-artefactos-kora": "Audita contra forma y ciclo anteriores",
    "urn:kora:artefacto:auditoria-exposicion-kora": "Invoca el núcleo anterior para resolver el corpus",
    "urn:kora:kb:alma-de-kora": "Describe la identidad y operación anteriores",
    "urn:kora:kb:guia-rapida-pneuma": "Enseña los comandos y la forma anteriores",
    "urn:kora:kb:regimen-de-ley": "Declara la ley anterior como autoridad",
    "urn:kora:kb:frontera-fuentes-tecnicas": "Regula la conservación de fuentes de KORA",
    "urn:kora:kb:cat-kora-kernel": "Formaliza el núcleo anterior",
    "urn:kora:kb:cat-kora-semantica-operacional": "Formaliza operaciones y estados anteriores",
    "urn:kora:kb:cat-contrato-ingenieria-agentica": "Fija contrato y forma de ingeniería de KORA",
}
RETIRED_RUNTIME = {
    "urn:ops:artefacto:clawforge": "Opera una flota cuyo único destino es OpenClaw",
    "urn:kora:kb:deploy-flota-openclaw": "Runbook de un destino retirado",
    "urn:openclaw-fleet:kb:fleet-canon-policy": "Política operacional de flota externa",
    "urn:openclaw-fleet:kb:handoff-policy": "Política de continuidad de flota externa",
}
BODY_ALIASES = {
    "urn:salud:kb:hsc-gcl-1-2-vias-venosas-centrales":
        "urn:salud:kb:hsc-gcl-1-2-vias-venosas-centrales-2025",
    "urn:salud:kb:hsc-mo-2q-tele-organizacion-unidad-telemedicina":
        "urn:salud:kb:hsc-mo-2q-tele-organizacion-unidad-telemedicina-2023",
}
HISTORICAL_REFERENCES = {
    "urn:kora:kb:spec:1.0.0": "Referencia de formato KODA dentro de la fuente preservada; no es una dependencia nueva",
    "urn:kora:kb:transform:1.0.0": "Referencia del método KODA dentro de la fuente preservada; no es una dependencia nueva",
    "urn:gorenuble:gn:bpmn-c4:1.0.0": "Marco histórico BPMN/C4 sin identidad canónica equivalente demostrada",
}


@dataclass
class LegacyObject:
    path: Path
    raw: bytes
    mode: int
    header: bytes
    body: bytes
    metadata: dict
    kind: str

    @property
    def id(self):
        return self.metadata["urn"]


@dataclass
class MigrationPlan:
    source: Path
    destination: Path
    files: dict[Path, File]
    links: dict[Path, str]
    source_files: dict[Path, File]
    report: dict


def _paths(source: Path) -> tuple[list[Path], int]:
    """Enumerate without following links or entering personal-state directories."""
    root = source / "artefactos"
    if not root.is_dir() or root.is_symlink():
        raise KoraError(f"No existe un directorio propio de productos: {root}")
    paths, excluded = [], 0
    for base, directories, filenames in os.walk(root, followlinks=False):
        for name in list(directories):
            path = Path(base) / name
            if name in PRIVATE_NAMES:
                directories.remove(name)
                excluded += 1
            elif path.is_symlink():
                raise KoraError(f"Enlace de origen exige conservación explícita: {path.relative_to(source)}")
        for name in filenames:
            if name in PRIVATE_NAMES or name.startswith(".env."):
                excluded += 1
                continue
            path = Path(base) / name
            if not stat.S_ISREG(path.lstat().st_mode):
                raise KoraError(f"Fuente no regular exige conservación explícita: {path.relative_to(source)}")
            paths.append(path.relative_to(source))
    return sorted(paths), excluded


def _read_source(source: Path, relative: Path) -> File:
    path = source / relative
    before = path.lstat()
    if not stat.S_ISREG(before.st_mode):
        raise KoraError(f"La fuente cambió de tipo: {relative}")
    data = path.read_bytes()
    after = path.lstat()
    if (before.st_ino, before.st_size, before.st_mtime_ns, before.st_mode) != (
            after.st_ino, after.st_size, after.st_mtime_ns, after.st_mode):
        raise KoraError(f"La fuente cambió durante la lectura: {relative}")
    return File(data, stat.S_IMODE(after.st_mode))


def _entry(relative: Path, file: File) -> LegacyObject | None:
    parts = relative.parts
    if len(parts) < 3 or parts[1] not in KINDS:
        return None
    kind = KINDS[parts[1]]
    is_entry = (kind == "skill" and len(parts) == 5 and parts[-1] == "SKILL.md") or (
        kind != "skill" and len(parts) == 4 and relative.suffix == ".md")
    if not is_entry:
        return None
    lines = file.data.splitlines(keepends=True)
    if not lines or lines[0] not in (b"---\n", b"---\r\n"):
        raise KoraError(f"Falta encabezado anterior en {relative}")
    end = next((i for i, line in enumerate(lines[1:], 1)
                if line.rstrip(b"\r\n") == b"---"), None)
    if end is None:
        raise KoraError(f"Encabezado anterior sin cierre en {relative}")
    header, body = b"".join(lines[:end + 1]), b"".join(lines[end + 1:])
    try:
        metadata = yaml.load(b"".join(lines[1:end]).decode("utf-8"), Loader=UniqueLoader)
        header.decode("utf-8")
        body.decode("utf-8")
    except (UnicodeError, yaml.YAMLError) as error:
        raise KoraError(f"Formato anterior ilegible: {relative}") from error
    if not isinstance(metadata, dict):
        raise KoraError(f"Encabezado anterior no es un mapa: {relative}")
    for key in ("urn", "nombre", "descripcion", "estado"):
        if not isinstance(metadata.get(key), str) or not metadata[key]:
            raise KoraError(f"{relative}: falta {key}")
    if not URN.fullmatch(metadata["urn"]):
        raise KoraError(f"Identidad anterior no admitida: {relative}")
    safe_relative(metadata["nombre"])
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", metadata["nombre"]):
        raise KoraError(f"Nombre anterior necesita adaptación explícita: {relative}")
    if kind != "knowledge" and len(metadata["nombre"]) > 64:
        raise KoraError(f"Nombre nativo excede 64 caracteres: {relative}")
    if header + body != file.data:
        raise KoraError(f"La separación perdió bytes: {relative}")
    return LegacyObject(relative, file.data, file.mode, header, body, metadata, kind)


def _list(metadata: dict, field: str) -> list[str]:
    values = metadata.get(field, [])
    if isinstance(values, str):
        values = [values]
    if not isinstance(values, list) or any(not isinstance(item, str) for item in values):
        raise KoraError(f"{metadata['urn']}: relación {field} inválida")
    return values


def _disposition(entry: LegacyObject) -> str | None:
    if entry.id in MACHINERY:
        return "Reconstrucción de maquinaria: " + MACHINERY[entry.id]
    if entry.id in RETIRED_RUNTIME:
        return "Destino retirado: " + RETIRED_RUNTIME[entry.id]
    if entry.metadata["estado"] in ("deprecado", "retirado"):
        return "Estado conservado del origen: " + entry.metadata["estado"]
    if entry.kind != "knowledge" and "targets" in entry.metadata and not (
            set(_list(entry.metadata, "targets")) & {"codex", "hermes"}):
        return "No tiene un destino autorizado de realización"
    return None


def _yaml(data: dict) -> bytes:
    return yaml.safe_dump(data, allow_unicode=True, sort_keys=False).encode("utf-8")


def _archive_summary(source: Path) -> dict:
    count, size = 0, 0
    for base, directories, files in os.walk(source / "_archivo", followlinks=False):
        directories[:] = [name for name in directories if name not in PRIVATE_NAMES
                           and not (Path(base) / name).is_symlink()]
        for name in files:
            path = Path(base) / name
            if name not in PRIVATE_NAMES and stat.S_ISREG(path.lstat().st_mode):
                count += 1
                size += path.stat().st_size
    return {"files": count, "bytes": size,
            "handling": "No ingerido ni versionado; permanece en origen, con respaldo a cargo de integración"}


def plan_import(source: Path, destination: Path) -> MigrationPlan:
    source, destination = Path(source).resolve(), Path(destination).resolve()
    if source == destination or destination.is_relative_to(source):
        raise KoraError("El destino independiente debe quedar fuera del origen")
    paths, excluded = _paths(source)
    source_files = {path: _read_source(source, path) for path in paths}
    entries = [entry for path, file in source_files.items() if (entry := _entry(path, file))]
    by_id = {}
    for entry in entries:
        if entry.id in by_id:
            raise KoraError(f"Identidad duplicada en el origen: {entry.id}")
        by_id[entry.id] = entry
    if not entries:
        raise KoraError("El origen no contiene objetos importables")

    aliases, body_refs = {}, defaultdict(set)
    for entry in entries:
        for token in BODY_URN.findall(entry.body.decode("utf-8")):
            if not token.endswith("*"):
                body_refs[token.rstrip(".:")].add(entry.id)
        for alias in KODA_ALIAS.findall(str(entry.metadata.get("fuente", ""))):
            if alias in by_id or (alias in aliases and aliases[alias] != entry.id):
                raise KoraError(f"Alias histórico ambiguo: {alias}")
            aliases[alias] = entry.id
    for alias, target in BODY_ALIASES.items():
        if alias in body_refs and target in by_id and alias not in by_id:
            if alias in aliases and aliases[alias] != target:
                raise KoraError(f"Alias corporal contradice la procedencia: {alias}")
            aliases[alias] = target

    names = Counter((URN.fullmatch(e.id).group(1), e.metadata["nombre"]) for e in entries)
    files, links, locations, metadata_by_id = {}, {}, {}, {}
    reasons = {e.id: reason for e in entries if (reason := _disposition(e))}
    target_changes, relation_counts = [], Counter()
    owned = set()
    for entry in entries:
        namespace = URN.fullmatch(entry.id).group(1)
        name = entry.metadata["nombre"]
        slug = name + "-knowledge" if names[(namespace, name)] > 1 and entry.kind == "knowledge" else name
        bucket = Path("archive/products" if entry.id in reasons else "products")
        directory = bucket / namespace / slug
        if directory in locations.values():
            raise KoraError(f"Colisión de ubicación importada: {directory}")
        locations[entry.id] = directory
        provenance = {"source_path": entry.path.as_posix(), "source_sha256": digest(entry.raw),
                      "legacy_state": entry.metadata["estado"]}
        if entry.kind != "knowledge":
            provenance["legacy_header"] = entry.header.decode("utf-8")
        metadata = {"id": entry.id, "kind": entry.kind, "name": name,
                    "description": entry.metadata["descripcion"], "content": "content.md"}
        if entry.kind != "knowledge":
            old_targets = _list(entry.metadata, "targets") if "targets" in entry.metadata else None
            metadata["targets"] = [target for target in ("codex", "hermes")
                                   if old_targets is None or target in old_targets]
            if old_targets != metadata["targets"]:
                target_changes.append({"id": entry.id, "previous": old_targets,
                                       "current": metadata["targets"],
                                       "reason": "Destinos del mandato; la lista anterior permanece en procedencia"})
        relations = {key: _list(entry.metadata, key) for key in RELATIONS if key in entry.metadata}
        relation_counts.update({key: len(values) for key, values in relations.items()})
        requires = list(relations.get("conocimiento", [])) if entry.kind in ("skill", "agent") else []
        for identifier in relations.get("depende", []):
            if identifier not in by_id or by_id[identifier].kind in ("skill", "knowledge"):
                requires.append(identifier)
        metadata.update(requires=list(dict.fromkeys(requires)), relations=relations, provenance=provenance)
        metadata_by_id[entry.id] = metadata
        files[directory / "object.yaml"] = File(_yaml(metadata))
        files[directory / "content.md"] = File(entry.raw if entry.kind == "knowledge" else entry.body, entry.mode)
        owned.add(entry.path)
        if entry.kind == "skill":
            for path, resource in source_files.items():
                if path != entry.path and path.is_relative_to(entry.path.parent):
                    relative = path.relative_to(entry.path.parent)
                    if relative in (Path("object.yaml"), Path("content.md")):
                        raise KoraError(f"Recurso colisiona con la forma nueva: {path}")
                    files[directory / relative] = resource
                    owned.add(path)
        if entry.kind == "knowledge":
            links[entry.path] = os.path.relpath(directory / "content.md", entry.path.parent)
    if remaining := set(source_files) - owned:
        raise KoraError("Archivos sin objeto conservador: " + ", ".join(str(p) for p in sorted(remaining)))
    files[Path("aliases.yaml")] = File(_yaml(dict(sorted(aliases.items()))))

    dependency_issues = []
    for identifier, metadata in metadata_by_id.items():
        if identifier in reasons:
            continue
        for required in metadata["requires"]:
            if required not in by_id:
                dependency_issues.append({"id": identifier, "requires": required, "issue": "missing"})
            elif required in reasons:
                dependency_issues.append({"id": identifier, "requires": required, "issue": "archived"})
            elif by_id[required].kind != "knowledge":
                for target in metadata.get("targets", []):
                    if target not in metadata_by_id[required].get("targets", []):
                        dependency_issues.append({"id": identifier, "requires": required,
                                                  "target": target, "issue": "target_unavailable"})
    unknown = [{"reference": token, "sources": sorted(body_refs[token]),
                "reason": HISTORICAL_REFERENCES.get(token, "Referencia corporal no resuelta")}
               for token in sorted(set(body_refs) - by_id.keys() - aliases.keys())]
    old_operations = [e.id for e in entries if e.id not in reasons and e.kind != "knowledge"
                      and re.search(rb"kora\.py|ley/[0-4]", e.body)]
    head = subprocess.run(["git", "-C", str(source), "rev-parse", "HEAD"],
                          capture_output=True, text=True, check=False)
    report = {"source_head": head.stdout.strip() if head.returncode == 0 else None,
              "source_files": len(source_files), "source_bytes": sum(len(f.data) for f in source_files.values()),
              "source_manifest_sha256": digest(b"\n".join(
                  path.as_posix().encode() + b"\0" + str(file.mode).encode() + b"\0" + digest(file.data).encode()
                  for path, file in source_files.items())),
              "objects": len(entries), "kinds": dict(Counter(e.kind for e in entries)),
              "active_objects": len(entries) - len(reasons), "archived_objects": len(reasons),
              "auxiliary_files": len(source_files) - len(entries), "excluded_private_entries": excluded,
              "relations": dict(relation_counts), "aliases": len(aliases),
              "archive": _archive_summary(source),
              "dispositions": [{"id": identifier, "reason": reason} for identifier, reason in reasons.items()],
              "target_changes": target_changes, "dependency_issues": dependency_issues,
              "unresolved_body_references": unknown, "legacy_operation_consumers": old_operations,
              "preservation": "Conocimiento íntegro; encabezado+cuerpo reconstruibles; recursos íntegros",
              "written": False}
    return MigrationPlan(source, destination, files, links, source_files, report)


def _preflight(plan: MigrationPlan):
    for relative in (*plan.files, *plan.links):
        path = plan.destination / relative
        if path.exists() or path.is_symlink():
            raise KoraError(f"El destino ya contiene trabajo; no se sobrescribe: {relative}")
        for parent in path.parents:
            if parent.is_symlink():
                raise KoraError(f"El destino atraviesa un enlace: {parent}")
            if parent.exists() and not parent.is_dir():
                raise KoraError(f"El destino atraviesa un archivo: {parent}")
            if parent == plan.destination:
                break


def _publish_file(staged: Path, destination: Path):
    """Exclusive publication; unlike replace(), concurrent files are never overwritten."""
    os.link(staged, destination)


def _source_matches(plan: MigrationPlan) -> bool:
    paths, _ = _paths(plan.source)
    return set(paths) == set(plan.source_files) and all(
        _read_source(plan.source, path) == original for path, original in plan.source_files.items())


def apply_import(plan: MigrationPlan) -> dict:
    _preflight(plan)
    if not _source_matches(plan):
        raise KoraError("El corpus cambió después de preparar la importación")
    plan.destination.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".kora-import-", dir=plan.destination))
    created_files, created_dirs = [], []

    def parents(directory):
        missing = []
        while not directory.exists():
            missing.append(directory)
            directory = directory.parent
        if directory.is_symlink() or not directory.is_dir():
            raise KoraError(f"El destino cambió durante la importación: {directory}")
        for path in reversed(missing):
            try:
                path.mkdir()
                created_dirs.append(path)
            except FileExistsError:
                if path.is_symlink() or not path.is_dir():
                    raise KoraError(f"Destino concurrente incompatible: {path}")

    try:
        for relative, file in plan.files.items():
            path = staging / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(file.data)
            path.chmod(file.mode)
        for relative in plan.files:
            path = plan.destination / relative
            parents(path.parent)
            _publish_file(staging / relative, path)
            created_files.append(relative)
        for relative, target in plan.links.items():
            path = plan.destination / relative
            parents(path.parent)
            path.symlink_to(target)
            created_files.append(relative)
        for relative, file in plan.files.items():
            path = plan.destination / relative
            if path.read_bytes() != file.data or stat.S_IMODE(path.stat().st_mode) != file.mode:
                raise KoraError(f"Verificación de bytes o modo falló: {relative}")
        for relative, target in plan.links.items():
            if os.readlink(plan.destination / relative) != target or not (plan.destination / relative).is_file():
                raise KoraError(f"Ruta de lectura no resuelta: {relative}")
        if not _source_matches(plan):
            raise KoraError("El corpus cambió durante la importación")
    except Exception as error:
        preserved = []
        for relative in reversed(created_files):
            path = plan.destination / relative
            if relative in plan.links:
                unchanged = path.is_symlink() and os.readlink(path) == plan.links[relative]
            else:
                expected = plan.files[relative]
                unchanged = (path.is_file() and not path.is_symlink() and path.read_bytes() == expected.data
                             and stat.S_IMODE(path.stat().st_mode) == expected.mode)
            if unchanged:
                path.unlink()
            elif path.exists() or path.is_symlink():
                preserved.append(relative.as_posix())
        for directory in reversed(created_dirs):
            try:
                directory.rmdir()
            except OSError:
                pass
        suffix = " Cambios concurrentes conservados: " + ", ".join(preserved) if preserved else ""
        raise KoraError(f"Importación revertida tras fallo: {error}.{suffix}") from error
    finally:
        shutil.rmtree(staging)
    return {**plan.report, "written": True}


def import_legacy(source: Path, destination: Path, dry_run: bool = False) -> dict:
    plan = plan_import(source, destination)
    _preflight(plan)
    return plan.report if dry_run else apply_import(plan)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Importar productos anteriores sin ejecutar su maquinaria")
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--check", action="store_true", help="Comprobar y reportar sin escribir")
    args = parser.parse_args(argv)
    try:
        print(json.dumps(import_legacy(args.source, args.destination, args.check),
                         ensure_ascii=False, indent=2))
    except KoraError as error:
        parser.exit(1, f"{error}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
