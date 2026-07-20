#!/usr/bin/env python3
"""Fachada determinista y no instaladora sobre los gestos KORA."""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Callable

CONTRACT = "entrega-kora-v1"
PARITY_RE = re.compile(
    r"paridad: (\d+) fiel · (\d+) desviadas · "
    r"(\d+) no-instaladas · (\d+) sin-emision\."
)


def public_candidate(entry: dict) -> dict:
    return {
        key: entry.get(key, "")
        for key in ("urn", "nombre", "tipo", "version", "estado", "path")
    }


def discover(entries: list[dict], query: str) -> dict:
    query = query.strip()
    exact = [
        public_candidate(entry)
        for entry in entries
        if query in (entry.get("urn"), entry.get("path"))
        or query.casefold() == str(entry.get("nombre", "")).casefold()
    ]
    if len(exact) == 1:
        return {"status": "resolved", "artifact": exact[0]}
    if len(exact) > 1:
        return {"status": "ambiguous", "candidates": exact}

    needle = query.casefold()
    suggestions = [
        public_candidate(entry)
        for entry in entries
        if needle and any(
            needle in str(entry.get(key, "")).casefold()
            for key in ("urn", "nombre", "path")
        )
    ]
    return {
        "status": "not-found",
        "suggestion_count": len(suggestions),
        "suggestions": suggestions[:10],
    }


def detail(result: subprocess.CompletedProcess) -> str:
    message = (result.stderr or result.stdout or "").strip()
    return message[-2000:]


def mutation(derived_emission: bool = False) -> dict:
    return {
        "derived_emission": derived_emission,
        "runtime_apply": False,
        "lifecycle": False,
        "source_edit": False,
        "git": False,
    }


def epistemic() -> dict:
    return {
        "source_validation": "form-coherence-only",
        "parity_scope": "managed-material-only",
        "runtime_behavior": "not-verified",
        "runtime_authority": "not-verified",
    }


def blocked(base: dict, stage: str,
            result: subprocess.CompletedProcess) -> tuple[dict, int]:
    base.update({
        "status": "blocked",
        "stage": stage,
        "detail": detail(result),
        "next_action": "fix-stage-before-retry",
    })
    return base, 1


def execute(raiz: Path, query: str, target: str,
            run: Callable[[list[str]], subprocess.CompletedProcess]
            ) -> tuple[dict, int]:
    base = {
        "contract": CONTRACT,
        "query": query,
        "target": target,
        "epistemic": epistemic(),
        "mutation": mutation(),
    }
    if target != "codex":
        base.update({
            "status": "unsupported-target",
            "next_action": "use-codex-or-stop",
        })
        return base, 1

    censo = run([sys.executable, str(raiz / "kora.py"), "censo", "--json"])
    if censo.returncode:
        base.update({
            "status": "observation-error",
            "stage": "census",
            "detail": detail(censo),
            "next_action": "restore-observability-before-retry",
        })
        return base, 2
    try:
        entries = json.loads(censo.stdout)
        if not isinstance(entries, list) \
                or any(not isinstance(entry, dict) for entry in entries):
            raise TypeError("se esperaba una lista de entradas")
        discovery = discover(entries, query)
    except (json.JSONDecodeError, TypeError, ValueError) as exc:
        base.update({
            "status": "observation-error",
            "stage": "census",
            "detail": f"censo JSON inválido: {exc}",
            "next_action": "restore-observability-before-retry",
        })
        return base, 2
    if discovery["status"] != "resolved":
        base.update(discovery)
        base["next_action"] = (
            "choose-exact-urn" if discovery["status"] == "ambiguous"
            else "provide-exact-identifier"
        )
        return base, 1

    artifact = discovery["artifact"]
    base["artifact"] = artifact
    nombre = run([
        sys.executable, str(raiz / "kora.py"), "nombre", artifact["urn"]
    ])
    if nombre.returncode:
        base.update({
            "status": "observation-error",
            "stage": "resolution",
            "detail": detail(nombre),
            "next_action": "restore-observability-before-retry",
        })
        return base, 2
    expected_state = {
        "conocimiento": "publicado",
        "skill": "activo",
        "agente": "activo",
    }.get(artifact["tipo"])
    if expected_state is None:
        base.update({
            "status": "observation-error",
            "stage": "classification",
            "detail": f"tipo inesperado '{artifact['tipo']}'",
            "next_action": "restore-observability-before-retry",
        })
        return base, 2
    if artifact["estado"] != expected_state:
        base.update({
            "status": "blocked",
            "stage": "lifecycle",
            "detail": (
                f"estado '{artifact['estado']}'; se exige '{expected_state}'"
            ),
            "next_action": "resolve-lifecycle-outside-this-skill",
        })
        return base, 1

    tests = run([
        sys.executable, "-m", "unittest", "discover", "-s", "tests"
    ])
    if tests.returncode:
        return blocked(base, "tests", tests)

    base["checks"] = {"resolution": "passed", "tests": "passed"}
    if artifact["tipo"] == "conocimiento":
        velar = run([
            sys.executable, str(raiz / "kora.py"), "velar", "--estricto"
        ])
        if velar.returncode:
            return blocked(base, "validation", velar)
        base.update({
            "status": "knowledge-validated",
            "checks": {**base["checks"], "validation": "passed",
                       "emission": "not-applicable",
                       "parity": "not-applicable"},
            "next_action": "consume-as-context",
        })
        return base, 0

    emission = run([
        sys.executable, str(raiz / "kora.py"), "transmutar",
        "--urn", artifact["urn"], "--target", target,
    ])
    if emission.returncode:
        return blocked(base, "emission", emission)
    base["mutation"] = mutation(derived_emission=True)

    validation = run([
        sys.executable, str(raiz / "kora.py"), "velar", "--estricto"
    ])
    if validation.returncode:
        return blocked(base, "validation", validation)

    parity = run([
        sys.executable, str(raiz / "kora.py"), "transmutar", "--paridad",
        "--urn", artifact["urn"], "--target", target,
    ])
    match = PARITY_RE.search(parity.stdout or "")
    if match is None:
        if parity.returncode:
            return blocked(base, "parity", parity)
        base.update({
            "status": "observation-error",
            "stage": "parity",
            "detail": detail(parity) or "paridad sin resumen reconocible",
            "next_action": "restore-observability-before-retry",
        })
        return base, 2
    faithful, drifted, missing, unissued = map(int, match.groups())
    counts = {
        "faithful": faithful,
        "drifted": drifted,
        "not_installed": missing,
        "not_emitted": unissued,
    }
    if faithful + missing == 0 and drifted + unissued == 0:
        base.update({
            "status": "observation-error",
            "stage": "parity",
            "detail": "paridad no observó ninguna unidad del artefacto",
            "next_action": "restore-observability-before-retry",
        })
        return base, 2
    base["checks"] = {
        **base["checks"],
        "emission": "derived",
        "validation": "passed",
        "parity": counts,
    }
    if parity.returncode or drifted or unissued:
        return blocked(base, "parity", parity)
    if missing and faithful:
        status = "partially-installed"
    elif missing:
        status = "not-installed"
    else:
        status = "parity-faithful"
    base.update({
        "status": status,
        "next_action": (
            "none" if status == "parity-faithful"
            else "manual-apply-requires-explicit-approval"
        ),
    })
    return base, 0


def runner(raiz: Path) -> Callable[[list[str]], subprocess.CompletedProcess]:
    env = os.environ.copy()
    env["KORA_RAIZ"] = str(raiz)

    def run(argv: list[str]) -> subprocess.CompletedProcess:
        return subprocess.run(
            argv, cwd=raiz, env=env, text=True, capture_output=True,
            check=False,
        )

    return run


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Prepara y verifica una entrega KORA sin instalarla.")
    parser.add_argument("--raiz", required=True)
    parser.add_argument("--query", required=True)
    parser.add_argument("--target", default="codex")
    args = parser.parse_args(argv)
    raiz = Path(args.raiz).expanduser().resolve()
    if not (raiz / "kora.py").is_file() or not (raiz / "tests").is_dir():
        receipt = {
            "contract": CONTRACT,
            "status": "observation-error",
            "query": args.query,
            "target": args.target,
            "stage": "anchor",
            "detail": f"'{raiz}' no es una raíz KORA operable",
            "epistemic": epistemic(),
            "mutation": mutation(),
            "next_action": "provide-valid-kora-root",
        }
        print(json.dumps(receipt, ensure_ascii=False, sort_keys=True))
        return 2
    receipt, code = execute(raiz, args.query, args.target, runner(raiz))
    print(json.dumps(receipt, ensure_ascii=False, sort_keys=True))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
