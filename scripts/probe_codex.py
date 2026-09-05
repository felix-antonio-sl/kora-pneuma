#!/usr/bin/env python3
"""Probe the installed Codex surface with synthetic data and sanitized output."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import selectors
import shutil
import subprocess
import sys
import tempfile
import time
import tomllib


def emit(value):
    print(json.dumps(value, ensure_ascii=False), flush=True)


def isolated_environment(config_home: Path):
    environment = dict(os.environ)
    environment["CODEX_HOME"] = str(config_home)
    return environment


def disabled_global_skills():
    paths = sorted((Path.home() / ".agents/skills").rglob("SKILL.md"))
    entries = [f"{{ path = {json.dumps(str(path))}, enabled = false }}" for path in paths]
    return "skills.config=[" + ",".join(entries) + "]", paths


class AppServer:
    def __init__(self, workspace: Path, config_home: Path, log: Path, prefix=None):
        self.error_stream = log.open("wb")
        self.process = subprocess.Popen(
            [*(prefix or ["codex"]), "app-server", "--stdio"],
            cwd=workspace,
            env=isolated_environment(config_home),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=self.error_stream,
            bufsize=0,
        )
        self.selector = selectors.DefaultSelector()
        self.selector.register(self.process.stdout, selectors.EVENT_READ)
        self.buffer = b""
        self.next_id = 0
        self.request("initialize", {
            "clientInfo": {"name": "kora_codex_probe", "version": "1"},
            "capabilities": {"experimentalApi": True},
        })
        self.send({"method": "initialized"})

    def send(self, message):
        self.process.stdin.write(json.dumps(message).encode() + b"\n")
        self.process.stdin.flush()

    def request(self, method, params):
        self.next_id += 1
        request_id = self.next_id
        self.send({"id": request_id, "method": method, "params": params})
        deadline = time.monotonic() + 30
        while time.monotonic() < deadline:
            if b"\n" not in self.buffer:
                if not self.selector.select(max(0, deadline - time.monotonic())):
                    break
                chunk = os.read(self.process.stdout.fileno(), 65536)
                if not chunk:
                    raise RuntimeError("App Server terminó antes de responder")
                self.buffer += chunk
                continue
            line, self.buffer = self.buffer.split(b"\n", 1)
            message = json.loads(line)
            if message.get("id") == request_id:
                if "error" in message:
                    raise RuntimeError(f"{method}: {message['error']}")
                return message["result"]
        raise TimeoutError(f"App Server no respondió {method}")

    def close(self):
        self.process.terminate()
        try:
            self.process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            self.process.kill()
            self.process.wait()
        self.selector.close()
        self.error_stream.close()
        self.process.stdin.close()
        self.process.stdout.close()


def write_skill(directory: Path, name: str):
    directory.mkdir(parents=True)
    (directory / "SKILL.md").write_text(
        f"---\nname: {name}\ndescription: Synthetic KORA native discovery probe.\n---\n\n"
        "KORA_SYNTHETIC_SKILL\n",
        encoding="utf-8",
    )


def probe():
    version = subprocess.check_output(["codex", "--version"], text=True).strip()
    with tempfile.TemporaryDirectory(prefix="kora-codex-probe-") as temporary:
        root = Path(temporary)
        workspace = root / "workspace"
        config_home = root / "codex"
        workspace.mkdir()
        (config_home / "agents").mkdir(parents=True)
        subprocess.run(["git", "init", "-q", str(workspace)], check=True)
        (config_home / "config.toml").write_text(
            'model = "gpt-6-astra"\nmodel_reasoning_effort = "max"\n'
            '[analytics]\nenabled = false\n'
        )
        # A malformed file provides an observable native loader witness.
        (config_home / "agents" / "malformed.toml").write_text(
            'name = 42\ndescription = "synthetic"\ndeveloper_instructions = "synthetic"\n'
        )
        (config_home / "agents" / "different-filename.toml").write_text(
            'name = "kora-probe-agent"\ndescription = "synthetic"\n'
            'developer_instructions = "KORA_SYNTHETIC_AGENT"\n'
        )
        project_agents = workspace / ".codex/agents"
        project_agents.mkdir(parents=True)
        (project_agents / "project-malformed.toml").write_text(
            'name = 42\ndescription = "synthetic"\ndeveloper_instructions = "synthetic"\n'
        )
        write_skill(workspace / ".agents/skills/kora-probe-repo", "kora-probe-repo")
        write_skill(config_home / "skills/kora-probe-legacy", "kora-probe-legacy")
        linked = workspace / ".agents/skills/kora-probe-linked"
        write_skill(root / "linked-source", "kora-probe-linked")
        linked.symlink_to(root / "linked-source", target_is_directory=True)
        for metadata_format in ["yaml", "json", "both"]:
            skill = workspace / ".agents/skills" / f"kora-probe-{metadata_format}"
            write_skill(skill, f"kora-probe-{metadata_format}")
            if metadata_format in {"yaml", "both"}:
                (skill / "agents").mkdir()
                (skill / "agents/openai.yaml").write_text(
                    "interface:\n  display_name: YAML native metadata\n"
                    "  short_description: Synthetic YAML\n"
                )
            if metadata_format in {"json", "both"}:
                (skill / "SKILL.json").write_text(json.dumps({
                    "interface": {"display_name": "JSON native metadata",
                                  "short_description": "Synthetic JSON"}
                }))

        schema_root = root / "schemas"
        subprocess.run(
            ["codex", "app-server", "generate-json-schema", "--experimental", "--out", str(schema_root)],
            env=isolated_environment(config_home), check=True, capture_output=True,
        )
        thread_schema = json.loads((schema_root / "v2/ThreadStartParams.json").read_text())
        skill_schema = json.loads((schema_root / "v2/SkillsListParams.json").read_text())
        log = root / "server.log"
        server = AppServer(workspace, config_home, log)
        try:
            models = server.request("model/list", {"limit": 100, "includeHidden": True})
            model = next(item for item in models["data"] if item["model"] == "gpt-6-astra")
            skills = server.request("skills/list", {"cwds": [str(workspace)], "forceReload": True})
            listed = [skill for item in skills["data"] for skill in item["skills"]]
            selected = {skill["name"]: {"scope": skill["scope"], "enabled": skill["enabled"],
                                       "display_name": (skill.get("interface") or {}).get("displayName")}
                        for skill in listed if skill["name"].startswith("kora-probe-")}
            thread = server.request("thread/start", {
                "cwd": str(workspace), "ephemeral": True, "model": "gpt-6-astra",
                "approvalPolicy": "never", "sandbox": "read-only",
                "config": {"model_reasoning_effort": "max"},
            })
        finally:
            server.close()
        project_without_trust = "project-malformed.toml" in log.read_text()
        with (config_home / "config.toml").open("a") as config_stream:
            config_stream.write(f"[projects.{json.dumps(str(workspace))}]\ntrust_level = \"trusted\"\n")
        trusted_log = root / "trusted-server.log"
        server = AppServer(workspace, config_home, trusted_log)
        try:
            server.request("thread/start", {"cwd": str(workspace), "ephemeral": True,
                                           "approvalPolicy": "never", "sandbox": "read-only"})
        finally:
            server.close()
        result = {
            "version": version,
            "proof": "native discovery and thread setup; no model inference",
            "model": model["model"],
            "efforts": [item["reasoningEffort"] for item in model["supportedReasoningEfforts"]],
            "thread_model": thread["model"],
            "thread_effort": thread["reasoningEffort"],
            "skills": selected,
            "skill_scopes": dict(Counter(skill["scope"] for skill in listed)),
            "standalone_agent_loader_observed": "Ignoring malformed agent role definition" in log.read_text(),
            "standalone_agent_requires_config_registration": False,
            "project_agent_loader_without_trust": project_without_trust,
            "project_agent_loader_with_trust": "project-malformed.toml" in trusted_log.read_text(),
            "thread_start_has_agent_type": "agentType" in thread_schema["properties"],
            "skills_list_has_extra_roots_parameter": "perCwdExtraUserRoots" in skill_schema["properties"],
        }
        result["ok"] = (
            "max" in result["efforts"] and result["thread_effort"] == "max"
            and result["standalone_agent_loader_observed"]
            and {"kora-probe-repo", "kora-probe-legacy", "kora-probe-linked"} <= set(selected)
        )
        emit(result)
        return result["ok"]


def inventory():
    home = Path.home()
    config_path = home / ".codex/config.toml"
    config = tomllib.loads(config_path.read_text()) if config_path.exists() else {}
    disabled = {item["path"]: item.get("enabled", True)
                for item in config.get("skills", {}).get("config", []) if "path" in item}
    for relative in [".agents/skills", ".codex/skills", ".codex/agents"]:
        directory = home / relative
        items = []
        if not directory.exists():
            continue
        for entry in sorted(directory.iterdir()):
            if entry.name.startswith("."):
                continue
            path = entry / "SKILL.md" if entry.is_dir() else entry
            if not path.is_file() or path.suffix not in {".md", ".toml"}:
                continue
            content = path.read_bytes()
            markers = [marker for marker in [b"kora-pneuma", b"urn:kora:", b"urn:salud:", b"KORA"]
                       if marker in content]
            if markers:
                items.append({"name": entry.name, "bytes": len(content),
                              "sha256": hashlib.sha256(content).hexdigest(),
                              "symlink": entry.is_symlink(),
                              "enabled_override": disabled.get(str(path)),
                              "relation_markers": [marker.decode() for marker in markers]})
        emit({"directory": relative, "relation_is_not_ownership": True, "items": items})
    emit({"configured_model": config.get("model"),
          "configured_effort": config.get("model_reasoning_effort"),
          "agents_table_present": "agents" in config})
    return True


def canary(direct=False):
    """Run one explicitly requested real inference against a synthetic catalog."""
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    import yaml
    from kora.catalog import Catalog
    from kora.render_codex import render

    source_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    auth_file = source_home / "auth.json"
    if not auth_file.is_file():
        raise RuntimeError("El canario requiere autenticación local disponible en archivo")
    with tempfile.TemporaryDirectory(prefix="kora-codex-canary-") as temporary:
        root = Path(temporary)
        workspace = root / "workspace"
        source = workspace / "source"
        config_home = root / "codex"
        config_home.mkdir()
        (config_home / "auth.json").symlink_to(auth_file)
        objects = [
            ("conditions", "knowledge", [],
             "La entrega procede con color verde. Excepción: si llueve, queda diferida.\n"
             "La distancia no está disponible: UNKNOWN. No inferirla.\n"
             "Marca de lectura del conocimiento: KORA_FACT_LITERAL_37B9.\n"),
            ("kora-canary-lookup", "skill", ["urn:test:knowledge:conditions"],
             "Lee el conocimiento requerido para resolver el caso. Devuelve un objeto JSON "
             "con state (procede o diferida), exception, distance, knowledge_marker, "
             "skill_marker y role_marker. Mantén la incertidumbre tal como aparece. "
             "skill_marker debe ser KORA_SKILL_NATIVE_5B2C. role_marker debe ser la "
             "marca indicada en las instrucciones del agente.\n"),
            ("kora-canary-witness", "agent", ["urn:test:skill:kora-canary-lookup"],
             "Eres el testigo sintético de una realización nativa de Codex. Carga el SKILL.md "
             "nativo de kora-canary-lookup y sigue su procedimiento. Tu role_marker es "
             "KORA_ROLE_NATIVE_8FA1. Lee las fuentes requeridas; no modifiques archivos, "
             "no crees Goals ni delegues de nuevo.\n"),
        ]
        for name, kind, requires, body in objects:
            directory = source / "products/test" / name
            directory.mkdir(parents=True)
            metadata = {"id": f"urn:test:{kind}:{name}", "kind": kind, "name": name,
                        "description": "Evalúa el caso sintético del canario KORA.",
                        "content": "body.md", "requires": requires,
                        "targets": [] if kind == "knowledge" else ["codex"]}
            (directory / "object.yaml").write_text(yaml.safe_dump(metadata))
            (directory / "body.md").write_text(body)
        catalog = Catalog(source)
        for relative, file in render(catalog, catalog.get("urn:test:agent:kora-canary-witness")).items():
            path = workspace / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(file.data)
            path.chmod(file.mode)
        subprocess.run(["git", "init", "-q", str(workspace)], check=True)
        output = root / "result.txt"
        events = root / "events.jsonl"
        stderr = root / "stderr.log"
        prompt = (
            "Usa $kora-canary-witness directamente en esta sesión para evaluar el caso "
            "color verde, con lluvia. Carga su skill requerida y conocimiento. "
            "Devuelve solo el objeto JSON que indique el procedimiento. "
            "No delegues, no crees Goals ni ejecutes otras tareas."
        ) if direct else (
            "Usa un único subagente de tipo kora-canary-witness. No inspecciones tú los "
            "archivos del caso ni actives la skill homónima en la sesión principal. "
            "Envíale: Evalúa el caso color verde, con lluvia, aplicando "
            "tu skill requerida; devuelve el objeto JSON que indique tu procedimiento. "
            "Espera su término y entrega íntegro ese objeto JSON. Puedes gestionar al "
            "subagente y leer su resultado. No crees Goals ni ejecutes otras tareas."
        )
        disabled_skills, global_paths = disabled_global_skills()
        base_command = [
            "codex", "-a", "never", "-s", "read-only", "-m", "gpt-6-astra",
            "-c", 'model_reasoning_effort="max"',
            "-c", "features.apps=false", "-c", "features.remote_plugin=false",
            "-c", "features.memories=false", "-c", "check_for_update_on_startup=false",
            "-c", disabled_skills,
            "-c", f"projects.{json.dumps(str(workspace))}.trust_level=\"trusted\"",
        ]
        server = AppServer(workspace, config_home, root / "discovery.log", prefix=base_command)
        try:
            listed = server.request("skills/list", {"cwds": [str(workspace)], "forceReload": True})
            native_skills = sorted({item["name"] for group in listed["data"] for item in group["skills"]
                                    if item["enabled"] and item["name"].startswith("kora-canary-")})
        finally:
            server.close()
        context_probe = subprocess.run(
            [*base_command, "-C", str(workspace), "debug", "prompt-input", prompt],
            env=isolated_environment(config_home), cwd=workspace, capture_output=True, text=True,
        )
        isolated_context = (context_probe.returncode == 0
                            and native_skills == ["kora-canary-lookup", "kora-canary-witness"]
                            and "kora-canary-lookup" in context_probe.stdout
                            and not any(str(path) in context_probe.stdout for path in global_paths)
                            and "kora-pneuma" not in context_probe.stdout)
        if not isolated_context:
            emit({"phase": "canary_context", "ok": False,
                  "reason": "El contexto sintético no quedó aislado de skills globales"})
            return False
        command = [*base_command,
            "exec", "--ephemeral", "--ignore-user-config", "--ignore-rules", "--json",
            "-C", str(workspace), "--output-last-message", str(output), prompt,
        ]
        emit({"phase": "canary_started", "model": "gpt-6-astra", "effort": "max",
              "activation": "direct_skill" if direct else "native_role",
              "ephemeral": True, "sources": "synthetic temporary catalog",
              "native_skills_discovered": native_skills,
              "synthetic_skill_in_context": True, "global_skills_in_context": False,
              "credential": "existing local authentication; contents not read by probe"})
        with events.open("wb") as event_stream, stderr.open("wb") as error_stream:
            result = subprocess.run(command, env=isolated_environment(config_home),
                                    cwd=workspace, stdout=event_stream, stderr=error_stream)
        raw_events = events.read_text()
        final = output.read_text() if output.exists() else ""
        try:
            answer = json.loads(final.strip().removeprefix("```json").removesuffix("```").strip())
        except (ValueError, TypeError):
            answer = {}
        event_objects = [json.loads(line) for line in raw_events.splitlines() if line.strip()]
        item_types = Counter(item.get("item", {}).get("type") for item in event_objects if "item" in item)
        collab_items = [item.get("item", {}) for item in event_objects
                        if "collab" in item.get("item", {}).get("type", "")]
        collaboration_tools = {str(item.get("tool")) for item in collab_items}
        expected = {"state": "diferida", "distance": "UNKNOWN",
                    "knowledge_marker": "KORA_FACT_LITERAL_37B9",
                    "skill_marker": "KORA_SKILL_NATIVE_5B2C", "role_marker": "KORA_ROLE_NATIVE_8FA1"}
        checks = {key: answer.get(key) == value for key, value in expected.items()}
        exception = str(answer.get("exception", "")).lower()
        checks["exception_preserved"] = "lluvia" in exception or "llueve" in exception
        if direct:
            checks["no_delegation_event"] = not collab_items
        else:
            checks["native_delegation_observed"] = bool(
                collaboration_tools & {"spawn_agent", "spawnAgent", "wait", "wait_agent"}
            )
        checks["process_completed"] = result.returncode == 0
        checks["isolated_skill_context"] = isolated_context
        sanitized = {"phase": "canary_completed", "ok": all(checks.values()),
                     "activation": "direct_skill" if direct else "native_role",
                     "checks": checks, "answer": {key: answer.get(key) for key in [*expected, "exception"]},
                     "event_item_types": dict(item_types),
                     "collaboration_tools": sorted(collaboration_tools)}
        if result.returncode:
            sanitized["failure_event_types"] = sorted({str(item.get("type")) for item in event_objects})
        if not sanitized["ok"]:
            # This conversation contains only synthetic data. Keep a bounded
            # diagnostic and redact the temporary/private path prefix.
            sanitized["diagnostic"] = final.replace(str(root), "<temporary>").replace(
                str(Path.home()), "<home>"
            )[:1600]
        emit(sanitized)
        return sanitized["ok"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--inventory", action="store_true", help="Read KORA-related local entries only")
    mode.add_argument("--canary", action="store_true", help="Run real inference on synthetic temporary sources")
    parser.add_argument("--direct", action="store_true", help="Exercise direct skill activation in the canary")
    args = parser.parse_args()
    if args.direct and not args.canary:
        parser.error("--direct requiere --canary")
    if not shutil.which("codex"):
        parser.error("codex no está disponible en PATH")
    success = inventory() if args.inventory else canary(args.direct) if args.canary else probe()
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
