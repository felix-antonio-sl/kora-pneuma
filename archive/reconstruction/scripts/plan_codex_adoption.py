#!/usr/bin/env python3
"""Prepare private evidence for Codex adoption; never modify an installation."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import time
import tomllib

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from kora.catalog import Catalog, KoraError
from kora.render_codex import render


SCOPES = (".agents/skills", ".codex/skills", ".codex/agents")
PRIVATE_DIRS = {".git", ".remember", "memoria", "memories", "sessions", "logs", "__pycache__"}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def regular(path: Path) -> bytes:
    before = path.lstat()
    if not stat.S_ISREG(before.st_mode):
        raise ValueError(f"Archivo no regular: {path}")
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(fd, "rb") as stream:
        data = stream.read()
        after = os.fstat(stream.fileno())
    signature = lambda s: (s.st_dev, s.st_ino, s.st_mode, s.st_size, s.st_mtime_ns, s.st_ctime_ns)
    if signature(before) != signature(after) or signature(after) != signature(path.lstat()):
        raise ValueError(f"Archivo cambió durante la lectura: {path}")
    return data


def split_markdown(data: bytes) -> tuple[dict, str]:
    text = data.decode("utf-8")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", text, re.S)
    if not match:
        return {}, text
    header = yaml.safe_load(match.group(1))
    return header if isinstance(header, dict) else {}, text[match.end():]


def main_info(path: str, data: bytes) -> dict:
    try:
        if path.endswith(".toml"):
            header = tomllib.loads(data.decode())
            text = header.get("developer_instructions", "")
        else:
            header, text = split_markdown(data)
        seal = re.search(r"<!-- kora:sello\s*\n(.*?)-->", text, re.S)
        block = seal.group(1) if seal else ""
        def value(pattern, source):
            match = re.search(pattern, source, re.M)
            return match.group(1).strip() if match else None
        identity = (value(r"^fuente:\s*(urn:\S+)", block)
                    or header.get("source_urn")
                    or value(r"^- Source URN:\s*`([^`]+)`", text)
                    or value(r"^Identidad:\s*`(urn:[^`]+)`", text))
        source_hash = (value(r"^hash-fuente:\s*sha256:([0-9a-f]{64})", block)
                       or value(r"^- Source Hash:\s*`sha256:([0-9a-f]{64})`", text))
        return {"id": identity, "name": header.get("name"),
                "function": header.get("description"), "source_sha256": source_hash,
                "version": value(r"^version:\s*(.+)$", block),
                "declaration": "kora_seal" if seal else "source_urn" if identity else None}
    except (UnicodeError, ValueError, yaml.YAMLError):
        return {"id": None, "declaration": None, "parse_error": True}


class Capture:
    def __init__(self, directory: Path):
        directory.mkdir(mode=0o700)
        self.directory = directory
        (directory / "blobs").mkdir(mode=0o700)
        self.sources = {}

    def blob(self, data: bytes) -> str:
        relative = f"blobs/{sha(data)}"
        path = self.directory / relative
        if not path.exists():
            fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            with os.fdopen(fd, "wb") as stream:
                stream.write(data)
        return relative

    def source(self, label: str, relative: str, path: Path | None = None,
               data: bytes | None = None, commit: str | None = None) -> dict:
        if data is None:
            data = regular(path)
        key = f"{label}:{commit or 'worktree'}:{relative}"
        record = {"repository": label, "path": relative, "sha256": sha(data),
                  "snapshot": self.blob(data)}
        if path is not None:
            record["mode"] = stat.S_IMODE(path.lstat().st_mode)
        if commit:
            record["commit"] = commit
        self.sources[key] = record
        return record

    def write_json(self, relative: str, value):
        path = self.directory / relative
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.write("\n")


def scan(home: Path, capture: Capture) -> tuple[dict, dict]:
    entries, payloads = {}, {}
    def visit(path: Path):
        relative = path.relative_to(home).as_posix()
        info = path.lstat()
        record = {"path": relative, "mode": stat.S_IMODE(info.st_mode)}
        if stat.S_ISLNK(info.st_mode):
            record.update(type="symlink", target=os.readlink(path))
        elif stat.S_ISDIR(info.st_mode):
            record["type"] = "directory"
            for child in sorted(path.iterdir()):
                if relative == ".codex/skills" and child.name == ".system":
                    continue
                visit(child)
        elif stat.S_ISREG(info.st_mode):
            data = regular(path)
            payloads[relative] = data
            record.update(type="file", sha256=sha(data), bytes=len(data), snapshot=capture.blob(data))
        else:
            record["type"] = "unsupported"
        entries[relative] = record
    for relative in SCOPES:
        path = home / relative
        if any(p.is_symlink() for p in path.parents if p != home and p.is_relative_to(home)):
            entries[relative] = {"path": relative, "type": "linked_parent", "mode": None}
            continue
        if path.exists() or path.is_symlink():
            visit(path)
    return dict(sorted(entries.items())), payloads


def source_snapshot(root: Path) -> str:
    h = hashlib.sha256()
    paths = [root / "aliases.yaml", root / "kora/catalog.py", root / "kora/render_codex.py"]
    for directory in (root / "products", root / "archive/products"):
        paths += sorted(p for p in directory.rglob("*") if p.is_file() or p.is_symlink())
    for path in paths:
        if not path.exists():
            continue
        h.update(path.relative_to(root).as_posix().encode() + b"\0")
        h.update(str(stat.S_IMODE(path.lstat().st_mode)).encode() + b"\0")
        h.update(regular(path))
    return h.hexdigest()


def desired_files(root: Path):
    problems = []
    for attempt in range(3):
        try:
            before = source_snapshot(root)
            catalog = Catalog(root)
            desired = {}
            for product in catalog.products.values():
                if product.kind == "knowledge" or "codex" not in product.targets:
                    continue
                for path, file in render(catalog, product).items():
                    item = {"sha256": sha(file.data), "mode": file.mode, "owners": []}
                    if path in desired and any(desired[path][k] != item[k] for k in ("sha256", "mode")):
                        raise ValueError(f"Realizaciones contradictorias: {path}")
                    desired.setdefault(path, item)["owners"].append(f"codex:{product.id}")
            if before != source_snapshot(root):
                raise ValueError("Las fuentes cambiaron durante el render")
            return catalog, dict(sorted(desired.items())), {"complete": True, "sha256": before}
        except (OSError, ValueError, KoraError) as error:
            problems.append(str(error))
            if attempt < 2:
                time.sleep(0.2)
    return None, {}, {"complete": False, "errors": problems}


def source_index(repositories: list[Path], names: set[str], capture: Capture):
    result = defaultdict(list)
    for repository in repositories:
        candidates = []
        if (repository / "artefactos").is_dir():
            candidates += list((repository / "artefactos/skills").glob("*/*/SKILL.md"))
            candidates += list((repository / "artefactos/agentes").glob("*/*.md"))
        if (repository / "artifacts").is_dir():
            for kind, filename in (("skills", "SKILL.md"), ("agents", "AGENT.md")):
                for base, directories, files in os.walk(repository / "artifacts" / kind):
                    directories[:] = [d for d in directories if d not in PRIVATE_DIRS | {"_BUILD"}
                                      and not (Path(base) / d).is_symlink()]
                    if filename in files:
                        candidates.append(Path(base) / filename)
        for path in candidates:
            name = path.stem if path.parent.parent.name == "agentes" else path.parent.name
            if name not in names:
                continue
            raw = regular(path)
            metadata, _ = split_markdown(raw)
            identity = metadata.get("urn") or metadata.get("_manifest", {}).get("urn")
            ref = capture.source(repository.name, path.relative_to(repository).as_posix(), path, raw)
            result[name].append({"repository": repository, "path": path, "raw": raw,
                                 "id": identity, "metadata": metadata, "evidence": ref})
    return result


def historical_source(source: dict, wanted: str, capture: Capture):
    if sha(source["raw"]) == wanted:
        return source["raw"], source["evidence"]
    repository = source["repository"]
    relative = source["path"].relative_to(repository).as_posix()
    log = subprocess.run(["git", "-C", str(repository), "log", "--all", "--format=%H", "--", relative],
                         capture_output=True)
    if log.returncode:
        return None
    for commit in dict.fromkeys(log.stdout.decode().splitlines()):
        result = subprocess.run(["git", "-C", str(repository), "show", f"{commit}:{relative}"],
                                capture_output=True)
        if result.returncode == 0 and sha(result.stdout) == wanted:
            return result.stdout, capture.source(repository.name, relative, data=result.stdout, commit=commit)
    return None


def historic_projection(path: str, installed: bytes, emitted: bytes, source: dict, capture: Capture):
    old_info, new_info = main_info(path, installed), main_info(path, emitted)
    if not old_info.get("source_sha256") or old_info.get("id") != new_info.get("id"):
        return None
    old = historical_source(source, old_info["source_sha256"], capture)
    new = historical_source(source, new_info.get("source_sha256", ""), capture)
    if old is None or new is None:
        return None
    old_header, old_body = split_markdown(old[0])
    new_header, new_body = split_markdown(new[0])
    old_body, new_body = old_body.strip("\n"), new_body.strip("\n")
    if not old_body:
        return None
    encode = (lambda s: json.dumps(s, ensure_ascii=False)[1:-1]) if path.endswith(".toml") else (lambda s: s)
    old_text = encode(old_body)
    text = installed.decode()
    if text.count(old_text) != 1:
        return None
    advanced = text.replace(old_text, encode(new_body), 1)
    advanced = advanced.replace(old_info["source_sha256"], new_info["source_sha256"])
    advanced = advanced.replace(f"version: {old_info.get('version')}", f"version: {new_info.get('version')}")
    old_description, new_description = old_header.get("descripcion"), new_header.get("descripcion")
    if isinstance(old_description, str) and isinstance(new_description, str) and old_description != new_description:
        advanced = advanced.replace(encode(old_description), encode(new_description), 1)
    if advanced.encode() != emitted:
        return None
    return {"kind": "historical_projection_exact_after_source_substitution",
            "historical_source": old[1], "comparison_source": new[1],
            "substitutions": ["source_body", "source_sha256", "source_version", "source_description"],
            "whole_file_bytes_verified": True}


def inspect_preferences(home: Path, entries: dict, names: set[str]):
    path = home / ".codex/config.toml"
    if not path.is_file() or path.is_symlink():
        return {"skills": [], "agents": [], "config_type": "absent_or_symlink"}
    raw = regular(path)
    config = tomllib.loads(raw.decode())
    skills, agents = [], []
    for item in config.get("skills", {}).get("config", []):
        if not isinstance(item, dict) or not isinstance(item.get("path"), str):
            continue
        absolute = Path(item["path"]).expanduser()
        if not absolute.is_absolute():
            absolute = path.parent / absolute
        try:
            relative = absolute.relative_to(home).as_posix()
        except ValueError:
            continue
        if any(relative.startswith(scope + "/") for scope in SCOPES[:2]):
            skills.append({"path": relative, "enabled": item.get("enabled", True),
                           "exists": relative in entries})
    for name, item in config.get("agents", {}).items():
        if isinstance(item, dict) and name in names:
            record = {"name": name}
            if isinstance(item.get("config_file"), str):
                referenced = Path(item["config_file"]).expanduser()
                if not referenced.is_absolute():
                    referenced = path.parent / referenced
                record["config_file"] = str(referenced)
            agents.append(record)
    return {"config_sha256": sha(raw), "skills": skills, "agents": agents,
            "handling": "Preservar overrides existentes, incluso rutas ausentes; no inferir habilitación de sucesores"}


def installer_manifest(home: Path):
    path = home / ".local/state/kora/installed.json"
    if not path.is_file() or path.is_symlink():
        return {"present": False, "files": {}}
    raw = regular(path)
    state = json.loads(raw)
    files = {}
    for bundle, members in state.items():
        if not bundle.startswith("codex:") or not isinstance(members, dict):
            continue
        for relative, info in members.items():
            if any(relative.startswith(scope + "/") for scope in SCOPES) and isinstance(info, dict):
                item = files.setdefault(relative, {"sha256": info.get("sha256"),
                                                   "mode": info.get("mode"), "owners": []})
                item["owners"].append(bundle)
    return {"present": True, "sha256": sha(raw), "files": files}


def prepare(root: Path, home: Path, repositories: list[Path], directory: Path) -> dict:
    capture = Capture(directory)
    entries, payloads = scan(home, capture)
    catalog, desired, source_state = desired_files(root)
    mains = {path: main_info(path, data) for path, data in payloads.items()
             if path.endswith("/SKILL.md") or path.startswith(".codex/agents/") and path.endswith(".toml")}
    names = {Path(path).stem if path.endswith(".toml") else Path(path).parent.name for path in mains}
    sources = source_index(repositories, names, capture)
    preferences = inspect_preferences(home, entries, names)
    manifest = installer_manifest(home)
    disabled = {item["path"] for item in preferences["skills"] if item["enabled"] is False}
    tree_mains = {str(Path(p).parent): p for p in mains if p.endswith("/SKILL.md")}
    records, adopt, retire, ambiguous, preserved = {}, {}, [], [], []
    timestamp = re.compile(rb"(?m)^- Transmuted At: `[0-9T:.+\-Z]+`\r?$")

    for path, entry in entries.items():
        if entry["type"] == "directory":
            continue
        parts = Path(path).parts
        name = Path(path).stem if path.startswith(".codex/agents/") else parts[2] if len(parts) > 2 else ""
        main = path if path in mains else tree_mains.get("/".join(parts[:3]))
        info = mains.get(main, {})
        record = {**entry, "main": main, "id": info.get("id"), "evidence": []}
        evidence = record["evidence"]
        if entry["type"] != "file":
            record.update(ownership="unproven", action="preserve", reason="Enlace o tipo no regular exige revisión individual")
            ambiguous.append({"path": path, "reason": record["reason"]})
            records[path] = record
            continue
        data = payloads[path]
        tracked = manifest["files"].get(path)
        if tracked and tracked["sha256"] == entry["sha256"] and tracked["mode"] == entry["mode"]:
            evidence.append({"kind": "installer_manifest_exact", "manifest_sha256": manifest["sha256"],
                             "owners": tracked["owners"]})
        if path in desired and entry["sha256"] == desired[path]["sha256"]:
            evidence.append({"kind": "current_render_exact", "source_snapshot": source_state.get("sha256")})
        counterpart = "agents/" + Path(path).name if path.startswith(".codex/agents/") else "skills/" + "/".join(parts[2:])
        for repository in repositories:
            emitted = repository / "_emision/codex" / counterpart
            if emitted.is_file() and not emitted.is_symlink():
                raw = regular(emitted)
                ref = capture.source(repository.name, emitted.relative_to(repository).as_posix(), emitted, raw)
                if raw == data:
                    evidence.append({"kind": "legacy_emission_exact", "source": ref})
                elif path in mains:
                    for source in sources.get(name, []):
                        if source["repository"] == repository and source["id"] == info.get("id"):
                            proof = historic_projection(path, data, raw, source, capture)
                            if proof:
                                evidence.append({**proof, "emission": ref})
        for source in sources.get(name, []):
            tail = Path(*parts[3:]) if not path.startswith(".codex/agents/") else Path("SKILL.md")
            built = source["path"].parent / "_BUILD/codex" / name / tail
            if built.is_file() and not built.is_symlink():
                raw = regular(built)
                ref = capture.source(source["repository"].name, built.relative_to(source["repository"]).as_posix(), built, raw)
                if data == raw:
                    evidence.append({"kind": "legacy_build_exact", "source": ref})
                    record["id"] = record["id"] or source["id"]
                elif timestamp.search(data) and timestamp.sub(b"<generation-time>", data) == timestamp.sub(b"<generation-time>", raw):
                    evidence.append({"kind": "legacy_build_exact_except_generation_timestamp", "source": ref})
                    record["id"] = record["id"] or source["id"]
        record["ownership"] = "proven" if evidence else "declared" if info.get("id") else "unproven"
        if record["ownership"] == "proven" and path in desired:
            adopt[path] = entry["sha256"]
            record["action"] = "adopt"
        elif record["ownership"] == "proven" and source_state["complete"]:
            record["action"] = "retire_candidate"
            retire.append({"path": path, "sha256": entry["sha256"], "mode": entry["mode"],
                           "id": record["id"], "evidence": evidence,
                           "condition": "Preservación y sustitución funcional o archivo inactivo revisados por integración"})
        else:
            record["action"] = "preserve"
            reason = "Sin origen byte verificable" if info.get("id") else "Sin atribución KORA comprobada"
            if main and any(sources.get(name, [])):
                reason = "Recurso en árbol KORA sin coincidencia byte verificable"
            ambiguous.append({"path": path, "reason": reason})
            preserved.append(path)
        records[path] = record

    identities = defaultdict(list)
    skill_names = defaultdict(list)
    legacy = []
    for path, info in mains.items():
        record = records[path]
        identity = record["id"]
        if identity:
            identities[identity].append(path)
        if path.endswith("/SKILL.md"):
            skill_names[Path(path).parent.name].append(path)
        if path.startswith(".codex/skills/"):
            name = Path(path).parent.name
            resolution = None
            if catalog and identity:
                try:
                    product = catalog.get(identity)
                    resolution = {"id": product.id, "kind": product.kind, "name": product.name,
                                  "active": product.id in catalog.products,
                                  "path": product.directory.relative_to(root).as_posix()}
                except KoraError:
                    pass
            legacy.append({"name": name, "id": identity, "function": info.get("function"),
                           "path": path, "enabled": path not in disabled, "resolution": resolution,
                           "ownership": record["ownership"], "sources": [s["evidence"] for s in sources.get(name, [])]})
    # A second snapshot detects additions, removals, chmod and symlink changes too.
    after_entries, _ = scan(home, capture)
    stable = entries == after_entries
    if preferences.get("config_sha256"):
        stable &= sha(regular(home / ".codex/config.toml")) == preferences["config_sha256"]
    stable &= installer_manifest(home) == manifest
    if source_state["complete"] and source_snapshot(root) != source_state["sha256"]:
        source_state = {"complete": False, "errors": ["El catálogo cambió durante la atribución de instalaciones"]}
    if not stable or not source_state["complete"]:
        adopt, retire = {}, []
        for record in records.values():
            if record["action"] in ("adopt", "retire_candidate"):
                record["action"] = "defer_unstable_snapshot"
    plan = {"format": 1, "created_at": datetime.now(timezone.utc).isoformat(),
            "planner_sha256": sha(regular(Path(__file__))),
            "read_only": True, "installation_stable": stable, "source": source_state,
            "roots": {"catalog": str(root), "home": str(home), "legacy_repositories": [str(p) for p in repositories]},
            "snapshot": {"entries": entries, "evidence_sources": list(capture.sources.values()),
                         "encoding": "Blobs SHA256 exactos; modos y enlaces en metadata. No se siguen enlaces.",
                         "excluded": [".codex/skills/.system", "configuración no pertinente", "historiales y credenciales"]},
            "desired": desired, "files": records, "adopt": adopt, "retire_candidates": retire,
            "installer_manifest": manifest,
            "ambiguous": ambiguous, "preserve": preserved, "preserve_preferences": preferences,
            "legacy_skills": legacy,
            "duplicate_skill_names": [{"name": key, "paths": value} for key, value in skill_names.items()
                                      if len(value) > 1],
            "same_identity_surfaces": [{"id": key, "paths": value,
                                        "note": "Un rol TOML y su skill directa son superficies complementarias"}
                                       for key, value in identities.items() if len(value) > 1],
            "application": "Revisar; pasar adopt a Installer.apply(..., adopt=digests). Este script no aplica ni retira archivos.",
            "counts": {"files": len(records), "adopt": len(adopt), "retire_candidates": len(retire),
                       "ambiguous": len(ambiguous), "desired": len(desired),
                       "ownership": dict(Counter(r["ownership"] for r in records.values()))}}
    capture.write_json("plan.json", plan)
    return plan


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--home", type=Path, default=Path.home())
    parser.add_argument("--legacy-root", type=Path, action="append", required=True,
                        help="Repositorio de productos anteriores; repetir para cada origen")
    args = parser.parse_args()
    root, home = args.root.resolve(), args.home.resolve()
    repositories = [p.resolve() for p in args.legacy_root]
    if any(not p.is_dir() or p == root for p in repositories):
        parser.error("Cada origen legado debe existir y ser distinto del catálogo activo")
    private = root / "._local"
    if private.is_symlink():
        parser.error("._local no puede ser un enlace")
    private.mkdir(mode=0o700, exist_ok=True)
    output = private / ("codex-adoption-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ"))
    plan = prepare(root, home, repositories, output)
    print(json.dumps({"plan": str((output / "plan.json").relative_to(root)),
                      "source_complete": plan["source"]["complete"],
                      "installation_stable": plan["installation_stable"], **plan["counts"]}, ensure_ascii=False))
    return 0 if plan["source"]["complete"] and plan["installation_stable"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
