#!/usr/bin/env python3
"""Observa KORA y prueba Hermes instalado con un home sintético aislado.

El modo predeterminado no llama proveedores ni lee credenciales o sesiones.
El modo --live usa autenticación existente solo en memoria, sin modificarla.
Las comprobaciones no alteran instalaciones; describen esta versión.
"""

from __future__ import annotations

import argparse
import base64
import contextlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time


def metadata_inventory(runtime: Path) -> dict:
    import yaml

    def identity(path):
        if not path.is_file():
            return None
        text = path.read_text(encoding="utf-8", errors="replace")
        legacy = re.search(r"<!-- kora:sello\s+fuente:\s*(urn:[^\s]+)", text)
        current = re.search(r"Identidad: `(urn:[^`]+)`", text)
        if legacy or current:
            return (legacy or current).group(1)
        if text.startswith("---\n"):
            try:
                frontmatter = yaml.safe_load(text.split("---", 2)[1]) or {}
                return (frontmatter.get("metadata") or {}).get("kora_id")
            except (yaml.YAMLError, IndexError, AttributeError):
                return None
        return None

    rows = []
    profiles = runtime / "profiles"
    roots = [runtime] + sorted(p for p in profiles.iterdir() if p.is_dir() and not p.name.startswith(".")) if profiles.is_dir() else [runtime]
    for root in roots:
        soul_id = identity(root / "SOUL.md")
        skills = []
        for path in sorted((root / "skills").glob("**/SKILL.md")):
            skill_id = identity(path)
            if skill_id:
                relative = path.relative_to(root)
                skills.append({"id": skill_id, "path": str(relative), "archived": ".archive" in relative.parts})
        if not soul_id and not skills:
            continue
        row = {"profile": "default" if root == runtime else root.name, "agent_id": soul_id, "skills": skills}
        manifest_path = root / "distribution.yaml"
        if soul_id and manifest_path.is_file():
            manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
            row["distribution_owned"] = manifest.get("distribution_owned", [])
            row["native_update_source_present"] = bool(manifest.get("source"))
        rows.append(row)
    return {"plane": "filesystem_metadata", "profiles": rows}


def isolated_probe(source: Path, temporary: Path) -> dict:
    # Import only after HERMES_HOME is assigned by the parent subprocess.
    home = checked_isolated_home(temporary)
    sys.path.insert(0, str(source))
    import socket

    def deny_network(*args, **kwargs):
        raise RuntimeError("La prueba offline no permite conexiones de red")

    socket.socket.connect = deny_network
    socket.socket.connect_ex = deny_network
    socket.create_connection = deny_network

    import yaml
    from hermes_cli import __version__, __release_date__
    from hermes_cli import profile_distribution as native
    from agent.prompt_builder import build_context_files_prompt, load_soul_md
    from agent.skill_utils import iter_skill_index_files
    from tools.skills_tool import _locate_skill

    home.mkdir(parents=True, exist_ok=True)
    (home / "SOUL.md").write_text("KORA_PROFILE_IDENTITY\n", encoding="utf-8")
    work = temporary / "work"
    work.mkdir()
    (work / ".git").mkdir()
    (work / "SOUL.md").write_text("WRONG_CWD_IDENTITY\n", encoding="utf-8")
    (work / "AGENTS.md").write_text("ROOT_GUIDANCE\n", encoding="utf-8")
    child = work / "child"
    child.mkdir()
    (child / "AGENTS.md").write_text("CHILD_GUIDANCE\n", encoding="utf-8")
    (child / "AGENTS.override.md").write_text("OVERRIDE_GUIDANCE\n", encoding="utf-8")
    identity = load_soul_md(home_override=home)
    context = build_context_files_prompt(cwd=str(child), skip_soul=True)

    def write_skill(directory, marker):
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "SKILL.md").write_text(
            "---\nname: method\ndescription: Synthetic probe method.\n---\n" + marker + "\n", encoding="utf-8"
        )

    local = home / "skills"
    external = temporary / "external"
    write_skill(local / "method", "LOCAL")
    write_skill(external / "method", "EXTERNAL")
    write_skill(local / ".archive/old", "ARCHIVED")
    scanned = list(iter_skill_index_files(local, "SKILL.md"))
    error, _, _ = _locate_skill("method", None, [], [local, external])

    distribution = temporary / "distribution"
    distribution.mkdir()
    (distribution / "SOUL.md").write_text("DISTRIBUTED_A\n", encoding="utf-8")
    write_skill(distribution / "skills/method", "DISTRIBUTED_A")
    manifest = {"name": "kora-probe", "distribution_owned": ["SOUL.md", "skills/method", "distribution.yaml"]}
    (distribution / "distribution.yaml").write_text(yaml.safe_dump(manifest), encoding="utf-8")
    preview = native.plan_install(str(distribution), temporary / "preview")
    if not preview.target_dir.resolve().is_relative_to(temporary.resolve()):
        raise RuntimeError("Hermes resolvió un destino fuera del directorio temporal")
    installed = native.install_distribution(str(distribution))
    target = installed.target_dir
    if not target.resolve().is_relative_to(temporary.resolve()):
        raise RuntimeError("Hermes resolvió un destino fuera del directorio temporal")
    personal = {"config.yaml": b"model: {default: synthetic-personal}\n", "memories/MEMORY.md": b"SYNTHETIC_MEMORY\n"}
    for name, content in personal.items():
        path = target / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    (target / "skills/method/SKILL.md").write_text("LOCAL_EDIT\n", encoding="utf-8")
    (target / "skills/method/personal.txt").write_text("LOCAL_ADDITION\n", encoding="utf-8")
    write_skill(distribution / "skills/method", "DISTRIBUTED_B")
    native.update_distribution("kora-probe")
    personal_preserved = all((target / name).read_bytes() == data for name, data in personal.items())
    overwritten = "DISTRIBUTED_B" in (target / "skills/method/SKILL.md").read_text()
    addition_removed = not (target / "skills/method/personal.txt").exists()
    manifest["distribution_owned"] = ["SOUL.md", "distribution.yaml"]
    (distribution / "distribution.yaml").write_text(yaml.safe_dump(manifest), encoding="utf-8")
    native.update_distribution("kora-probe")
    stale_retained = (target / "skills/method/SKILL.md").exists()
    (distribution / "extra.txt").write_text("EXTRA\n", encoding="utf-8")
    implicit = native.DistributionManifest(name="implicit")
    extra_owned = any(parts == ("extra.txt",) for _, parts in native._owned_entries(distribution, implicit))
    (distribution / "linked").symlink_to(distribution / "extra.txt")
    try:
        native.plan_install(str(distribution), temporary / "stage")
        symlink_rejected = False
    except native.DistributionError:
        symlink_rejected = True
    observations = {
        "soul_uses_profile_home": identity == "KORA_PROFILE_IDENTITY",
        "agents_chain_and_per_directory_override": "ROOT_GUIDANCE" in context and "OVERRIDE_GUIDANCE" in context and "CHILD_GUIDANCE" not in context,
        "archive_excluded_from_discovery": len(scanned) == 1,
        "local_external_duplicate_refuses_bare_name": bool(error and "Ambiguous" in error),
        "native_update_preserves_config_and_memory": personal_preserved,
        "native_update_overwrites_modified_owned_skill": overwritten,
        "native_update_deletes_local_addition_in_owned_directory": addition_removed,
        "native_update_retains_path_removed_from_manifest": stale_retained,
        "implicit_ownership_includes_arbitrary_extra_file": extra_owned,
        "native_distribution_rejects_symlink": symlink_rejected,
    }
    return {"plane": "installed_code_synthetic_offline", "version": __version__, "release_date": __release_date__, "observations": observations}


def checked_isolated_home(temporary: Path) -> Path:
    configured = os.environ.get("HERMES_HOME")
    expected = temporary.resolve() / "runtime"
    if not configured or Path(configured).resolve() != expected:
        raise RuntimeError("La prueba requiere su HERMES_HOME temporal explícito")
    return expected


def profile_entrypoint_probe(source: Path, temporary: Path) -> dict:
    """CLI y resolución nativas con perfiles y autenticación exclusivamente sintéticos."""
    import yaml
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from kora.catalog import Catalog
    from kora.render_hermes import render

    home = checked_isolated_home(temporary)
    authored = temporary / "authored-entrypoints"
    for name in ("fugaz", "agent-architect"):
        product = authored / "products/probe" / name
        product.mkdir(parents=True)
        (product / "object.yaml").write_text(yaml.safe_dump({
            "id": "urn:probe:artefacto:" + name, "kind": "agent", "name": name,
            "description": "Prueba sintética de entrada por perfil.", "content": "content.md",
            "targets": ["hermes"], "requires": [],
        }), encoding="utf-8")
        (product / "content.md").write_text("# PROFILE_" + name + "\n\nSolo ensayo sintético.\n", encoding="utf-8")
    catalog = Catalog(authored)
    for product in catalog.products.values():
        for relative, file in render(catalog, product).items():
            destination = home / relative.removeprefix(".hermes/")
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(file.data)
            destination.chmod(file.mode)
    root_config = b"model:\n  default: synthetic-root-model\n  provider: synthetic-root-provider\n"
    (home / "config.yaml").write_bytes(root_config)
    claims = base64.urlsafe_b64encode(json.dumps({"exp": int(time.time()) + 7200}).encode()).decode().rstrip("=")
    # Deliberately fake, future-dated JWT: exercises local resolution, never an API.
    fake_token = "synthetic." + claims + ".not-a-signature"
    auth = {"active_provider": "openai-codex", "providers": {"openai-codex": {
        "tokens": {"access_token": fake_token, "refresh_token": "synthetic-not-a-refresh-token"}}}}
    (home / "auth.json").write_text(json.dumps(auth), encoding="utf-8")
    root_auth = (home / "auth.json").read_bytes()
    child = r'''
import contextlib, io, json, socket, sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
name = sys.argv[2]
def deny(*args, **kwargs):
    raise RuntimeError("OFFLINE_NETWORK_DENIED")
socket.create_connection = deny
socket.socket.connect = deny
socket.socket.connect_ex = deny
sys.argv = ["hermes", "--profile", name, "prompt-size", "--json"]
captured = io.StringIO()
with contextlib.redirect_stdout(captured), contextlib.redirect_stderr(captured):
    import hermes_cli.main as entry
    from hermes_cli.config import load_config
    from hermes_constants import get_hermes_home
    from agent.prompt_builder import load_soul_md
    selected = get_hermes_home()
    cfg = load_config()
    entry.main()
try:
    prompt_size = json.loads(captured.getvalue())
except ValueError:
    prompt_size = {}
from hermes_cli._parser import build_top_level_parser
parser, _, _ = build_top_level_parser()
args = parser.parse_args(["chat", "--provider", "openai-codex", "--model", "gpt-6-astra"])
captured = io.StringIO()
with contextlib.redirect_stdout(captured), contextlib.redirect_stderr(captured):
    from cli import HermesCLI
    native = HermesCLI(model=args.model, provider=args.provider, verbose=False)
    guarded = entry._has_any_provider_configured()
    resolved = native._ensure_runtime_credentials()
    global_auth = json.loads((selected.parent.parent / "auth.json").read_text())
    token_matches = native.api_key == global_auth["providers"]["openai-codex"]["tokens"]["access_token"]
    soul = load_soul_md(home_override=selected)
row = {
    "profile": name, "selected_correctly": selected.name == name,
    "soul_loaded": "PROFILE_" + name in soul,
    "prompt_size_json": bool(prompt_size.get("system_prompt")),
    "root_config_inherited": cfg.get("model") == {"default": "synthetic-root-model", "provider": "synthetic-root-provider"},
    "startup_guard_accepts_shared_auth": guarded,
    "cli_route_resolved": resolved and native.provider == "openai-codex" and native.model == "gpt-6-astra",
    "shared_auth_used": token_matches,
    "profile_config_absent": not (selected / "config.yaml").exists(),
    "profile_auth_absent": not (selected / "auth.json").exists(),
}
print(json.dumps(row))
'''
    rows = []
    environment = {"PATH": os.defpath, "HERMES_HOME": str(home), "PYTHONDONTWRITEBYTECODE": "1",
                   "XDG_CACHE_HOME": str(temporary / "cache")}
    for name in ("fugaz", "agent-architect"):
        completed = subprocess.run([str(source / "venv/bin/python"), "-c", child, str(source), name],
                                   cwd=temporary, env=environment, capture_output=True, text=True, timeout=35)
        try:
            row = json.loads(completed.stdout)
        except ValueError:
            row = {"profile": name, "child_failed": True, "exit_code": completed.returncode}
        rows.append(row)
    required = {"selected_correctly", "soul_loaded", "prompt_size_json", "startup_guard_accepts_shared_auth",
                "cli_route_resolved", "shared_auth_used", "profile_config_absent", "profile_auth_absent"}
    unchanged = (home / "config.yaml").read_bytes() == root_config and (home / "auth.json").read_bytes() == root_auth
    return {"plane": "native_cli_profiles_synthetic_offline", "profiles": rows,
            "root_state_unchanged": unchanged,
            "passed": unchanged and all(all(row.get(key) is True for key in required) for row in rows)}


def soul_budget_probe(source: Path, temporary: Path, catalog_root: Path) -> dict:
    """Mide los SOUL actuales en perfiles temporales; no lee configuración personal."""
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from kora.catalog import Catalog
    from kora.render_hermes import render

    home = checked_isolated_home(temporary)
    catalog = Catalog(catalog_root)
    agents = sorted((p for p in catalog.products.values() if p.kind == "agent" and "hermes" in p.targets),
                    key=lambda p: p.name)
    for product in agents:
        for relative, file in render(catalog, product).items():
            destination = home / relative.removeprefix(".hermes/")
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(file.data)
            destination.chmod(file.mode)
    child = r'''
import contextlib, io, json, logging, socket, sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
name = sys.argv[2]
def deny(*args, **kwargs):
    raise RuntimeError("OFFLINE_NETWORK_DENIED")
socket.socket.connect = deny
socket.socket.connect_ex = deny
socket.create_connection = deny
logging.disable(logging.CRITICAL)
sys.argv = ["hermes", "--profile", name, "prompt-size", "--json"]
captured = io.StringIO()
with contextlib.redirect_stdout(captured), contextlib.redirect_stderr(captured):
    import hermes_cli.main as entry
    from hermes_constants import get_hermes_home
    from agent.prompt_builder import load_soul_md, _get_context_file_max_chars
    from hermes_cli.prompt_size import _build_inspection_agent
    from agent.system_prompt import build_system_prompt_parts
    entry.main()
cli_output = captured.getvalue()
# Hermes surfaces a truncation warning before the JSON even in quiet mode.
json_start = cli_output.index("{")
prompt_size = json.loads(cli_output[json_start:])
captured = io.StringIO()
with contextlib.redirect_stdout(captured), contextlib.redirect_stderr(captured):
    home = get_hermes_home()
    raw = (home / "SOUL.md").read_text().strip()
    note = raw[raw.index("## Fuente KORA"):]
    direct = load_soul_md(home_override=home)
    inspection = _build_inspection_agent("cli")
    from run_agent import AIAgent
    from hermes_cli.auth_constants import DEFAULT_CODEX_BASE_URL
    routed = AIAgent(model="gpt-6-astra", provider="openai-codex", api_key="inspect-only",
        base_url=DEFAULT_CODEX_BASE_URL, api_mode="codex_responses", quiet_mode=True,
        skip_memory=True, skip_background_review=True, save_trajectories=False,
        skip_context_files=True, load_soul_identity=True, enabled_toolsets=[])
    row = {"profile": name, "rendered_chars": len(raw), "direct_without_context": {
        "limit": _get_context_file_max_chars(), "loaded_chars": len(direct),
        "complete": direct == raw, "dependency_map_complete": note in direct}}
    for label, native in (("prompt_size_without_model", inspection), ("gpt6_astra", routed)):
        window = native.context_compressor.context_length
        loaded = load_soul_md(window, home_override=home)
        stable = build_system_prompt_parts(native)["stable"]
        row[label] = {"context_length": window, "limit": _get_context_file_max_chars(window),
            "loaded_chars": len(loaded), "complete": loaded == raw,
            "dependency_map_complete": note in loaded, "loaded_in_system_prompt": loaded in stable}
        native.close()
    row["prompt_size_without_model"].update(system_prompt_chars=prompt_size["system_prompt"]["chars"],
                                            warning_before_json=bool(cli_output[:json_start].strip()))
print(json.dumps(row))
'''
    environment = {"PATH": os.defpath, "HERMES_HOME": str(home), "PYTHONDONTWRITEBYTECODE": "1",
                   "XDG_CACHE_HOME": str(temporary / "cache")}
    rows = []
    for product in agents:
        completed = subprocess.run([str(source / "venv/bin/python"), "-c", child, str(source), product.name],
                                   cwd=temporary, env=environment, capture_output=True, text=True, timeout=40)
        try:
            rows.append(json.loads(completed.stdout))
        except ValueError:
            rows.append({"profile": product.name, "child_failed": True, "exit_code": completed.returncode})
    checks = ("complete", "dependency_map_complete", "loaded_in_system_prompt")
    return {"plane": "native_current_catalog_soul_offline", "profiles": rows,
            "routing": "openai-codex/gpt-6-astra", "personal_configuration_read": False,
            "passed": bool(rows) and all(all(row.get("gpt6_astra", {}).get(key) is True for key in checks)
                                         for row in rows)}


def read_live_access_token(auth_store: Path) -> tuple[str | None, str]:
    """Solo devuelve el access token dentro del proceso; nunca importa ni refresca OAuth."""
    try:
        data = json.loads(auth_store.read_text(encoding="utf-8"))
        token = data["providers"]["openai-codex"]["tokens"]["access_token"]
        if not isinstance(token, str) or not token:
            return None, "ACCESS_TOKEN_ABSENT"
        payload = token.split(".")[1]
        claims = json.loads(base64.urlsafe_b64decode(payload + "=" * (-len(payload) % 4)))
        expiry = claims.get("exp")
        if not isinstance(expiry, (int, float)) or expiry <= time.time() + 600:
            return None, "ACCESS_TOKEN_EXPIRED_OR_NEAR_EXPIRY"
        return token, "READY"
    except (OSError, ValueError, KeyError, IndexError, TypeError):
        return None, "ACCESS_TOKEN_UNAVAILABLE"


def _tool_text(value) -> str:
    if isinstance(value, str):
        try:
            decoded = json.loads(value)
        except (ValueError, TypeError):
            return value
        return _tool_text(decoded) if not isinstance(decoded, str) else decoded
    if isinstance(value, dict):
        return "\n".join(_tool_text(item) for item in value.values())
    if isinstance(value, list):
        return "\n".join(_tool_text(item) for item in value)
    return str(value)


def _contains_body(content, body: str) -> bool:
    # Native read_file prefixes line numbers; compare source lines inside the
    # actual tool response rather than relying on an echoed identity marker.
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    text = _tool_text(content)
    return bool(lines) and all(line in text for line in lines)


def live_probe(source: Path, temporary: Path, auth_store: Path, *, catalog_root: Path | None = None,
               agent_id: str | None = None, prompt_file: Path | None = None,
               expected_file: Path | None = None) -> dict:
    """Un caso sintético por el agente nativo; salida limitada a hechos evaluables."""
    home = checked_isolated_home(temporary)
    token, preflight = read_live_access_token(auth_store)
    result = {"plane": "live_synthetic", "provider": "openai-codex", "model": "gpt-6-astra", "reasoning_effort": "max", "preflight": preflight}
    if token is None:
        result["passed"] = False
        return result
    if (source / ".env").exists():
        result.update(preflight="INSTALL_DOTENV_PRESENT_REQUIRES_ISOLATED_IMPORT", passed=False)
        return result

    import logging
    logging.disable(logging.CRITICAL)
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from kora.catalog import Catalog
    from kora.render_hermes import render
    import yaml

    authored = temporary / "authored"
    def product(name, kind, body, requires=()):
        directory = authored / "products/probe" / name
        directory.mkdir(parents=True)
        identity = f"urn:probe:artefacto:{name}"
        (directory / "object.yaml").write_text(yaml.safe_dump({
            "id": identity, "kind": kind, "name": name,
            "description": "Clasifica cajas sintéticas conservando condiciones, excepciones y desconocidos.",
            "content": "content.md", "targets": ["hermes"], "requires": list(requires),
        }), encoding="utf-8")
        (directory / "content.md").write_text(body, encoding="utf-8")
        return identity

    if catalog_root is None:
        return _live_default_fixture(source, temporary, auth_store, result, token, product)
    catalog = Catalog(catalog_root)
    selected = catalog.get(agent_id)
    if selected.kind != "agent":
        raise RuntimeError("El catálogo temporal debe seleccionar un agente")
    prompt = prompt_file.read_text(encoding="utf-8")
    expected = json.loads(expected_file.read_text(encoding="utf-8"))
    return _run_live_catalog(source, temporary, result, token, catalog, selected, prompt, expected)


def _live_default_fixture(source, temporary, auth_store, result, token, product):
    from kora.catalog import Catalog

    knowledge = product("norma-cajas", "knowledge", (
        "# Norma sintética QC-719\n\n"
        "Una caja queda PREPARADA solo si el sello está vigente y tiene al menos tres piezas.\n"
        "Excepción prioritaria: cualquier caja declarada frágil queda RETENIDA, incluso si cumple la regla general.\n"
        "Si no es frágil y se desconoce el número de piezas, queda INDETERMINADA; no conviertas desconocido en cero.\n"
        "Si no es frágil, se conocen las piezas y el sello está vencido o tiene menos de tres piezas, queda NO_PREPARADA.\n"
    ))
    skill = product("kora-cajas", "skill", (
        "# Clasificar cajas sintéticas\n\n"
        "Procedimiento APLICA_CLASIFICACION_CAJAS: lee la norma requerida desde el archivo fuente "
        "indicado en Dependencias disponibles. Aplica la excepción, las condiciones y el estado desconocido. "
        "Devuelve solo un objeto JSON con claves A, B, C y D y valores de clasificación; no agregues texto.\n"
    ), [knowledge])
    agent_id = product("kora-canary", "agent", (
        "# Asesor de cajas sintéticas\n\n"
        "Usa la skill kora-cajas para clasificar las cajas del ensayo. Conserva los desconocidos "
        "y las excepciones de la fuente. Trabaja solo con los archivos sintéticos del ensayo.\n"
    ), [skill])
    catalog = Catalog(temporary / "authored")
    prompt = (
        "Usa la skill kora-cajas y consulta su conocimiento requerido para clasificar estos casos. "
        "A: sello vigente, 4 piezas, no frágil. B: sello vigente, 4 piezas, frágil. "
        "C: sello vigente, cantidad de piezas desconocida, no frágil. "
        "D: sello vencido, 4 piezas, no frágil. Devuelve el JSON que indica la skill.")
    expected = {"A": "PREPARADA", "B": "RETENIDA", "C": "INDETERMINADA", "D": "NO_PREPARADA"}
    return _run_live_catalog(source, temporary, result, token, catalog, catalog.get(agent_id), prompt, expected)


def _run_live_catalog(source, temporary, result, token, catalog, selected, prompt, expected):
    import yaml
    from kora.render_hermes import render

    home = checked_isolated_home(temporary)
    dependencies = catalog.dependencies(selected, "hermes")
    skills = [product for product in dependencies if product.kind == "skill"]
    knowledge = [product for product in dependencies if product.kind == "knowledge"]
    if not skills or not knowledge:
        result.update(preflight="SKILL_AND_KNOWLEDGE_REQUIRED", passed=False)
        return result
    prefix = f".hermes/profiles/{selected.name}/"
    home.mkdir(parents=True, exist_ok=True)
    for relative, file in render(catalog, selected).items():
        if not relative.startswith(prefix):
            raise RuntimeError("El renderer emitió fuera del perfil seleccionado")
        path = home / relative.removeprefix(prefix)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(file.data)
        path.chmod(file.mode)
    (home / "config.yaml").write_text(yaml.safe_dump({
        "model": {"provider": "openai-codex", "default": "gpt-6-astra"},
        "agent": {"reasoning_effort": "max"},
        "terminal": {"backend": "local", "cwd": str(temporary)},
        "memory": {"memory_enabled": False, "user_profile_enabled": False},
    }), encoding="utf-8")
    sys.path.insert(0, str(source))
    from hermes_cli.auth_constants import DEFAULT_CODEX_BASE_URL
    from run_agent import AIAgent

    # La API de toolsets admite conjuntos locales: solo estas tres herramientas
    # entran al esquema del canario. No se modifica el checkout ni la configuración viva.
    from toolsets import TOOLSETS
    TOOLSETS["kora-probe-read"] = {
        "description": "Lectura del ensayo sintético", "includes": [],
        "tools": ["skills_list", "skill_view", "read_file"],
    }
    native = None
    conversation = {}
    try:
        native = AIAgent(
            api_key=token, base_url=DEFAULT_CODEX_BASE_URL, provider="openai-codex",
            api_mode="codex_responses", model="gpt-6-astra",
            reasoning_config={"enabled": True, "effort": "max"},
            enabled_toolsets=["kora-probe-read"], max_iterations=6,
            run_budget_seconds=240, quiet_mode=True, verbose_logging=False,
            skip_context_files=True, load_soul_identity=True, skip_memory=True,
            skip_background_review=True, save_trajectories=False,
            session_id="kora-synthetic-canary", credential_pool=None,
        )
        available = sorted(tool.get("function", {}).get("name", "") for tool in native.tools)
        result["read_tools_only"] = set(available) == {"skills_list", "skill_view", "read_file"}
        if not result["read_tools_only"]:
            result.update(preflight="TOOL_SURFACE_DIFFERS", passed=False)
            return result
        conversation = native.run_conversation(prompt)
        messages = conversation.get("messages", [])
        called = {}
        successful = set()
        for message in messages:
            for call in message.get("tool_calls", []) or []:
                name = call.get("function", {}).get("name")
                if name in {"skills_list", "skill_view", "read_file"}:
                    called[call.get("id")] = name
            if message.get("role") == "tool":
                name = called.get(message.get("tool_call_id"))
                content = message.get("content", "")
                if not isinstance(content, str):
                    content = json.dumps(content)
                if name == "skill_view" and any(_contains_body(content, product.body) for product in skills):
                    successful.add(name)
                if name == "read_file" and any(_contains_body(content, product.body) for product in knowledge):
                    successful.add(name)
        raw_response = conversation.get("final_response", "").strip()
        if raw_response.startswith("```json\n") and raw_response.endswith("```"):
            raw_response = raw_response[8:-3].strip()
        try:
            answer_matches = json.loads(raw_response) == expected
        except (ValueError, TypeError):
            answer_matches = False
        result.update(
            api_calls=conversation.get("api_calls"),
            skill_loaded="skill_view" in successful,
            knowledge_read="read_file" in successful,
            answer_matches=answer_matches,
            conditions_exception_unknown_correct=answer_matches,
            passed=answer_matches and successful == {"skill_view", "read_file"},
        )
        if answer_matches:
            result["classification"] = expected
    except Exception as error:
        # El mensaje crudo de un cliente HTTP puede contener headers o payloads.
        result.update(passed=False, error_type=type(error).__name__)
        status = getattr(error, "status_code", None)
        if isinstance(status, int):
            result["http_status"] = status
    finally:
        if native is not None:
            with contextlib.suppress(Exception):
                native.close()
        token_bytes = token.encode("utf-8")
        result["credential_material_persisted"] = any(
            token_bytes in path.read_bytes() for path in temporary.rglob("*") if path.is_file()
        )
        if result["credential_material_persisted"]:
            result["passed"] = False
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path.home() / ".hermes/hermes-agent")
    parser.add_argument("--runtime", type=Path, default=Path.home() / ".hermes")
    parser.add_argument("--inventory", action="store_true", help="Solo metadata de identidades y skills KORA del filesystem")
    parser.add_argument("--profile-entrypoints", action="store_true", help="CLI nativo y auth compartida sintética; sin red ni credenciales personales")
    parser.add_argument("--soul-budgets", action="store_true", help="SOUL completo y mapa de dependencias en el prompt nativo; sin red ni configuración personal")
    parser.add_argument("--live", action="store_true", help="Ejecuta un canario sintético real con OAuth existente solo en memoria")
    parser.add_argument("--auth-store", type=Path, default=Path.home() / ".hermes/auth.json", help="Auth Hermes autorizado; sus valores nunca se imprimen")
    parser.add_argument("--catalog-root", type=Path, help="Catálogo para --soul-budgets o fuente temporal de --live")
    parser.add_argument("--agent-id", help="Identidad del agente dentro del catálogo temporal")
    parser.add_argument("--prompt-file", type=Path, help="Pregunta sintética; única entrada de tarea al modelo")
    parser.add_argument("--expected-file", type=Path, help="JSON esperado; solo evaluador, nunca se agrega al prompt")
    parser.add_argument("--isolated-child", type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args()
    if sum((args.inventory, args.profile_entrypoints, args.soul_budgets, args.live)) > 1:
        parser.error("--inventory, --profile-entrypoints, --soul-budgets y --live son modos separados")
    custom = (args.catalog_root, args.agent_id, args.prompt_file, args.expected_file)
    if args.soul_budgets and any(custom[1:]):
        parser.error("--soul-budgets solo admite --catalog-root como selección de fuente")
    if any(custom) and not args.soul_budgets and (not all(custom) or not args.live):
        parser.error("--catalog-root, --agent-id, --prompt-file y --expected-file requieren --live y se usan juntos")
    if args.inventory:
        result = metadata_inventory(args.runtime)
    elif args.isolated_child:
        captured = io.StringIO()
        with contextlib.redirect_stdout(captured), contextlib.redirect_stderr(captured):
            try:
                if args.profile_entrypoints:
                    result = profile_entrypoint_probe(args.source, args.isolated_child)
                elif args.soul_budgets:
                    result = soul_budget_probe(args.source, args.isolated_child, args.catalog_root)
                elif args.live:
                    result = live_probe(args.source, args.isolated_child, args.auth_store,
                                        catalog_root=args.catalog_root, agent_id=args.agent_id,
                                        prompt_file=args.prompt_file, expected_file=args.expected_file)
                else:
                    result = isolated_probe(args.source, args.isolated_child)
            except Exception as error:
                if not args.live:
                    raise
                result = {"plane": "live_synthetic", "passed": False, "error_type": type(error).__name__}
    else:
        interpreter = args.source / "venv/bin/python"
        if not interpreter.is_file():
            parser.error("No existe el Python de la instalación Hermes indicada")
        with tempfile.TemporaryDirectory(prefix="kora-hermes-probe-") as temporary:
            environment = {"PATH": os.defpath, "HERMES_HOME": str(Path(temporary) / "runtime"), "PYTHONDONTWRITEBYTECODE": "1"}
            command = [str(interpreter), str(Path(__file__).resolve()), "--source", str(args.source.resolve()), "--isolated-child", temporary]
            if args.profile_entrypoints:
                command.append("--profile-entrypoints")
            if args.soul_budgets:
                catalog = args.catalog_root or Path(__file__).resolve().parents[1]
                command += ["--soul-budgets", "--catalog-root", str(catalog.resolve())]
            if args.live:
                command += ["--live", "--auth-store", str(args.auth_store.resolve())]
                if args.catalog_root:
                    command += ["--catalog-root", str(args.catalog_root.resolve()), "--agent-id", args.agent_id,
                                "--prompt-file", str(args.prompt_file.resolve()),
                                "--expected-file", str(args.expected_file.resolve())]
            try:
                completed = subprocess.run(
                    command, cwd=temporary, env=environment, text=True, capture_output=True,
                    timeout=300 if args.live else 90 if args.soul_budgets else 45,
                )
            except subprocess.TimeoutExpired:
                result = {"plane": "live_synthetic" if args.live else "installed_code_synthetic_offline", "passed": False, "error_type": "TimeoutExpired"}
            else:
                if completed.returncode and not args.live:
                    print(completed.stderr, file=sys.stderr, end="")
                    return completed.returncode
                try:
                    result = json.loads(completed.stdout)
                except ValueError:
                    result = {"plane": "live_synthetic" if args.live else "installed_code_synthetic_offline", "passed": False, "error_type": "UnexpectedChildOutput", "exit_code": completed.returncode}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("passed", True) and all(result.get("observations", {}).values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
