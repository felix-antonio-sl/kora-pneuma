#!/usr/bin/env python3
"""Plan privado y read-only de adopción de las superficies KORA de Hermes.

Compara bytes y modos con emisiones conocidas; no importa ni ejecuta el núcleo
anterior, no lee credenciales/conversaciones y nunca escribe en el runtime.
El JSON contiene hashes y rutas, nunca cuerpos de archivos.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tempfile

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from kora.catalog import Catalog, KoraError
from kora.render_hermes import render


AGENTS = {
    "director-tecnico-hodom": "urn:salud:artefacto:director-tecnico-hodom",
    "dov-dori": "urn:fxsl:artefacto:dov-dori",
    "kora": "urn:kora:artefacto:kora",
    "steipete": "urn:dev:artefacto:steipete",
    "fugaz": "urn:dev:artefacto:fugaz",
    "agent-architect": "urn:dev:artefacto:agent-architect",
}
SEAL = "<!-- kora:sello"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def file_info(path):
    try:
        info = path.lstat()
    except FileNotFoundError:
        return None
    mode = stat.S_IMODE(info.st_mode)
    if not stat.S_ISREG(info.st_mode):
        return {"kind": "symlink" if stat.S_ISLNK(info.st_mode) else "other", "mode": mode}
    return {"kind": "file", "sha256": sha(path.read_bytes()), "mode": mode, "bytes": info.st_size}


def same(first, second):
    return first is not None and first == second


def frontmatter(text):
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not match:
        return {}, text
    metadata = yaml.safe_load(match.group(1)) or {}
    return metadata, text[match.end():]


def identity(path):
    if not path.is_file() or path.is_symlink():
        return None
    text = path.read_text(encoding="utf-8")
    match = re.search(r"<!-- kora:sello\s+fuente:\s*(urn:[^\s]+)", text)
    if match:
        return match.group(1)
    metadata, _ = frontmatter(text)
    return (metadata.get("metadata") or {}).get("kora_id")


def regular_files(root):
    if root.is_symlink() or not root.is_dir():
        return []
    return [path for path in sorted(root.rglob("*")) if path.is_file() or path.is_symlink()]


class Evidence:
    def __init__(self, legacy):
        self.legacy = legacy
        self.history = {}

    def historical_form(self, live, emitted, product_id):
        """Identify an older source and prove the complete installed wrapper.

        This is evidence for adoption only. It substitutes reviewed literal
        source/version/hash into an existing emission; it is not a renderer.
        Any additional change leaves the file ambiguous.
        """
        if not emitted.is_file() or emitted.is_symlink() or live.is_symlink():
            return None
        old = live.read_text(encoding="utf-8")
        current = emitted.read_text(encoding="utf-8")
        old_hash = re.search(r"^hash-fuente: sha256:([a-f0-9]{64})$", old, re.M)
        if not old_hash or SEAL not in current or SEAL not in old:
            return None
        namespace, name = product_id.split(":")[1], product_id.rsplit(":", 1)[1]
        relative = (f"artefactos/agentes/{namespace}/{name}.md" if live.name == "SOUL.md"
                    else f"artefactos/skills/{namespace}/{name}/SKILL.md")
        source = self.legacy / relative
        if not source.is_file():
            return None
        key = relative, old_hash.group(1)
        if key not in self.history:
            self.history[key] = None
            commits = subprocess.check_output(
                ["git", "-C", str(self.legacy), "log", "--format=%H", "--", relative], text=True
            ).splitlines()
            for commit in commits:
                historical = subprocess.check_output(
                    ["git", "-C", str(self.legacy), "show", f"{commit}:{relative}"], stderr=subprocess.DEVNULL
                )
                if sha(historical) == key[1]:
                    self.history[key] = historical.decode("utf-8"), commit
                    break
        found = self.history[key]
        if found is None:
            return None
        historical, commit = found
        historical_meta, historical_body = frontmatter(historical)
        current_meta, current_body = frontmatter(source.read_text(encoding="utf-8"))
        if historical_meta.get("urn") != product_id or current_meta.get("urn") != product_id:
            return None
        prefix, seal = current.split(SEAL, 1)
        if prefix.count(current_body.strip()) != 1:
            return None
        prefix = prefix.replace(current_body.strip(), historical_body.strip(), 1)
        if prefix.startswith("---\n"):
            header, body = prefix.split("\n---\n", 1)
            header = re.sub(r"^version: .*$", "version: " + str(historical_meta["version"]), header, flags=re.M)
            prefix = header + "\n---\n" + body
        seal = re.sub(r"^version: .*$", "version: " + str(historical_meta["version"]), seal, flags=re.M)
        seal = re.sub(r"^hash-fuente: sha256:[a-f0-9]{64}$", "hash-fuente: sha256:" + key[1], seal, flags=re.M)
        if (prefix + SEAL + seal).encode("utf-8") != live.read_bytes():
            return None
        if stat.S_IMODE(live.stat().st_mode) != stat.S_IMODE(emitted.stat().st_mode):
            return None
        return {"kind": "exact_historical_form", "source": relative, "commit": commit,
                "source_sha256": key[1], "version": str(historical_meta["version"])}


def preserved_counts(root, managed, default=False):
    counts = {"regular_files": 0, "symlinks": 0, "other_nodes": 0}
    for directory, names, files in os.walk(root, followlinks=False):
        base = Path(directory)
        if default and base == root:
            names[:] = [name for name in names if name not in {"profiles", "hermes-agent"}]
        for name in list(names):
            path = base / name
            if path.is_symlink():
                if path not in managed:
                    counts["symlinks"] += 1
                names.remove(name)
        for name in files:
            path = base / name
            if path in managed:
                continue
            info = path.lstat()
            key = "regular_files" if stat.S_ISREG(info.st_mode) else "symlinks" if stat.S_ISLNK(info.st_mode) else "other_nodes"
            counts[key] += 1
    return counts


def build_plan(home, catalog_root, legacy):
    runtime = home / ".hermes"
    emission = legacy / "_emision/hermes"
    catalog = Catalog(catalog_root)
    evidence = Evidence(legacy)
    plan = {"version": 1, "created_at": datetime.now(timezone.utc).isoformat(),
            "home": str(home), "catalog": str(catalog_root), "legacy_emission": str(emission),
            "adopt": {}, "retire_candidates": [], "ambiguous": [], "bundles": [],
            "files": {}, "preserved_extra_state_counts": {}, "archived_skills_preserved": 0}
    managed = {}

    def relative(path):
        return str(path.relative_to(home))

    def assess(path, old_path, desired, product_id, historical_agent=None):
        key = relative(path)
        current = file_info(path)
        if any(parent.is_symlink() for parent in path.parents if parent != home and home in parent.parents):
            current = {"kind": "linked_parent"}
        old_info = file_info(old_path)
        wanted = None if desired is None else {
            "kind": "file", "sha256": sha(desired.data), "mode": desired.mode, "bytes": len(desired.data)}
        proof = None
        if same(current, old_info):
            proof = {"kind": "exact_legacy_emission", "path": str(old_path.relative_to(legacy))}
        elif same(current, wanted):
            proof = {"kind": "exact_current_renderer"}
        elif current and current["kind"] == "file" and old_info and old_info["kind"] == "file":
            if path.name in {"SOUL.md", "SKILL.md"}:
                proof = evidence.historical_form(path, old_path, product_id)
            elif path.name == "distribution.yaml" and historical_agent:
                text = old_path.read_text(encoding="utf-8")
                expected = re.sub(r"^version: .*$", "version: " + historical_agent["version"], text, flags=re.M)
                if expected.encode() == path.read_bytes() and current["mode"] == old_info["mode"]:
                    proof = {**historical_agent, "kind": "exact_historical_manifest"}
        row = {"product": product_id, "current": current, "desired": wanted, "evidence": proof}
        plan["files"][key] = row
        if current is None:
            return proof
        if proof and desired is not None:
            plan["adopt"][key] = current["sha256"]
        elif proof:
            plan["retire_candidates"].append({"path": key, **current, "evidence": proof,
                                               "reason": "known_old_output_absent_from_new_bundle"})
        else:
            plan["ambiguous"].append({"path": key, "product": product_id,
                                       "current": current, "reason": "no_exact_emission_or_source_match"})
        return proof

    def scope(root, product_id, agent=False, installed_skill=None):
        product = catalog.get(product_id)
        rendered = render(catalog, product)
        emitted_prefix = f".hermes/profiles/{product.name}/" if agent else ".hermes/"
        desired = {root / name.removeprefix(emitted_prefix): file for name, file in rendered.items()}
        if any(not name.startswith(emitted_prefix) for name in rendered):
            raise KoraError("El renderer emitió fuera del prefijo esperado")
        profile = "default" if root == runtime else root.name
        plan["bundles"].append({"profile": profile, "product": product.id, "kind": product.kind,
                                "source": str(product.content_path.relative_to(catalog_root)),
                                "destination_prefix": relative(root),
                                "paths": sorted(relative(path) for path in desired)})
        if agent:
            old_root = emission / "profiles" / root.name
            manifest_path = old_root / "distribution.yaml"
            manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {} if manifest_path.is_file() else {}
            owned = []
            for item in manifest.get("distribution_owned", []):
                item_path = Path(item)
                if item_path.is_absolute() or ".." in item_path.parts:
                    raise KoraError("Manifiesto anterior fuera del perfil")
                candidate = old_root / item_path
                owned.extend(regular_files(candidate) if candidate.is_dir() else [candidate])
            old = {root / path.relative_to(old_root): path for path in owned}
            soul = root / "SOUL.md"
            soul_proof = assess(soul, old.get(soul, emission / "__not_emitted__"), desired.get(soul), product_id)
        else:
            old_root = emission / "skills" / installed_skill
            old = {root / "skills" / installed_skill / path.relative_to(old_root): path
                   for path in regular_files(old_root)}
            soul, soul_proof = None, None
        all_paths = set(old) | set(desired)
        managed.setdefault(root, set()).update(all_paths)
        for path in sorted(all_paths):
            if path == soul:
                continue
            assess(path, old.get(path, emission / "__not_emitted__"), desired.get(path), product_id, soul_proof)

    known_skills = {path.name for path in (emission / "skills").iterdir() if path.is_dir()}
    roots = [runtime] + sorted(path for path in (runtime / "profiles").iterdir() if path.is_dir() and not path.name.startswith("."))
    for root in roots:
        if root.is_symlink():
            plan["ambiguous"].append({"path": relative(root), "reason": "linked_runtime_root"})
            continue
        if root.name in AGENTS and root != runtime:
            if identity(root / "SOUL.md") != AGENTS[root.name]:
                plan["ambiguous"].append({"path": relative(root / "SOUL.md"), "reason": "agent_identity_differs"})
                continue
            scope(root, AGENTS[root.name], agent=True)
        else:
            for name in sorted(known_skills):
                path = root / "skills" / name / "SKILL.md"
                installed_id = identity(path)
                if installed_id:
                    try:
                        scope(root, installed_id, installed_skill=name)
                    except KoraError as error:
                        plan["ambiguous"].append({"path": relative(path), "reason": str(error)})
        # util-x is positively identified as the legacy test fixture, not by
        # its absence alone. Retire remains a candidate, never an action here.
        util = root / "skills/util-x/SKILL.md"
        if identity(util) == "urn:kora:artefacto:util-x":
            metadata, body = frontmatter(util.read_text(encoding="utf-8"))
            before_seal = body.split(SEAL, 1)[0].strip()
            fixture = (legacy / "tests/test_kora.py").read_text(encoding="utf-8")
            if (metadata == {"name": "util-x", "description": "Skill sintética de prueba.", "version": "1.0.0"}
                    and before_seal == "# Cuerpo\n\nTexto sintético."
                    and 'urn="urn:kora:artefacto:util-x"' in fixture):
                plan["retire_candidates"].append({"path": relative(util), **file_info(util),
                    "reason": "legacy_synthetic_test_fixture_without_active_product",
                    "evidence": {"source": "tests/test_kora.py:29-44", "installation_cause": "not_accredited"}})
                managed.setdefault(root, set()).add(util)
            else:
                plan["ambiguous"].append({"path": relative(util), "reason": "util_x_differs_from_known_fixture"})
        archive = root / "skills/.archive"
        if archive.is_dir():
            plan["archived_skills_preserved"] += sum(1 for p in archive.glob("*/SKILL.md") if identity(p))
        plan["preserved_extra_state_counts"]["default" if root == runtime else root.name] = preserved_counts(
            root, managed.get(root, set()), default=root == runtime)
    for name, product_id in AGENTS.items():
        root = runtime / "profiles" / name
        if not root.exists():
            product = catalog.get(product_id)
            if "hermes" in product.targets:
                scope(root, product_id, agent=True)
    plan["native_profile_entrypoints"] = {
        "verification_command": "python3 scripts/probe_hermes.py --profile-entrypoints",
        "new_profile_launch": "hermes --profile NAME chat --provider openai-codex --model gpt-6-astra",
        "config_inheritance": False, "credential_fallback": "native_global_root_per_provider",
        "config_bootstrap_required_for_explicit_launch": False,
    }
    plan["summary"] = {"adopt_files": len(plan["adopt"]), "retire_candidates": len(plan["retire_candidates"]),
                       "ambiguous": len(plan["ambiguous"]), "bundles": len(plan["bundles"]),
                       "new_files": sum(row["current"] is None and row["desired"] is not None for row in plan["files"].values())}
    return plan


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--home", type=Path, default=Path.home())
    parser.add_argument("--catalog-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--legacy-root", type=Path, required=True,
                        help="Repositorio anterior preservado, distinto del catálogo activo")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    catalog = args.catalog_root.resolve()
    if not args.legacy_root.is_dir() or args.legacy_root.resolve() == catalog:
        parser.error("El origen legado debe existir y ser distinto del catálogo activo")
    output = (args.output or catalog / "._local/hermes-adoption-plan.json").absolute()
    if not output.resolve().is_relative_to(catalog / "._local"):
        parser.error("El plan debe permanecer bajo ._local del catálogo")
    plan = build_plan(args.home.resolve(), catalog, args.legacy_root.resolve())
    output.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    fd, temporary = tempfile.mkstemp(prefix=".hermes-plan-", dir=output.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(plan, stream, ensure_ascii=False, indent=2, sort_keys=True)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, output)
    finally:
        Path(temporary).unlink(missing_ok=True)
    print(json.dumps({"private_plan": str(output), **plan["summary"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
