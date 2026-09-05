#!/usr/bin/env python3
"""Prueba material aislada de la maquinaria nueva; usa inferencia real autorizada.

El montaje oculta /home y /tmp, salvo el binario Codex, su autenticación de solo
lectura y el directorio sintético. No modifica el namespace del host.
https://github.com/containers/bubblewrap#usage
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from kora.catalog import Catalog
from kora.cli import build
from kora.install import Installer


KNOWLEDGE = "urn:probe:kb:envios"
SKILL = "urn:probe:artefacto:evaluar-envios"
AGENT = "urn:probe:artefacto:inspector-envios"
SOURCE = """Fuente ficticia de prueba. Manual de envío de piezas, versión 1, 2026-09-05.
Clave de versión que debe conservarse: PZ_6139_V1.
Estos criterios se aplican solo a este ejercicio; no describen una operación real.
Primero: un permiso REVOCADO produce DENEGADA, aunque las demás condiciones sean favorables.
Con permiso VIGENTE, si llueve el envío queda DIFERIDA, independientemente de la masa.
Con permiso VIGENTE y sin lluvia, masa conocida de hasta 12 kg inclusive produce AUTORIZADA.
Con permiso VIGENTE y sin lluvia, una masa mayor que 12 kg produce DENEGADA.
Si falta un dato que impide aplicar la regla correspondiente, el resultado es UNKNOWN.
La distancia al destino no fue medida y debe conservarse como UNKNOWN.
No interpretar un dato ausente como cero, falso ni una negativa.
"""


def emit(value):
    print(json.dumps(value, ensure_ascii=False), flush=True)


def prepare(output):
    temporary = Path(tempfile.mkdtemp(prefix="kora-independence-"))
    temporary.chmod(0o700)
    work = temporary / "work"
    work.mkdir()
    shutil.copytree(ROOT / "kora", work / "kora", ignore=shutil.ignore_patterns("__pycache__", "migrate.py"))
    shutil.copy2(ROOT / "kora_cli.py", work / "kora_cli.py")
    shutil.copy2(ROOT / "README.md", work / "README.md")
    shutil.copytree(ROOT / "docs", work / "docs")
    catalog = Catalog(ROOT)
    agent = catalog.get("urn:kora:artefacto:kora")
    for item in [agent, *catalog.dependencies(agent, "codex")]:
        relative = item.directory.relative_to(ROOT)
        shutil.copytree(item.directory, work / relative)
    (work / "inputs").mkdir()
    (work / "inputs/manual-envios-v1.txt").write_text(SOURCE, encoding="utf-8")
    (work / "reports").mkdir()
    (work / "tests").mkdir()
    shutil.copy2(ROOT / "tests/test_install.py", work / "tests/test_install.py")
    Installer(work).apply(build(Catalog(work), "codex", [agent.id]))
    subprocess.run(["git", "init", "-q", str(work)], check=True)
    config = temporary / "codex"
    config.mkdir()
    (config / "auth.json").touch(mode=0o600)
    (config / "config.toml").write_text('[analytics]\nenabled = false\n', encoding="utf-8")
    output.mkdir(parents=True, exist_ok=False)
    output.chmod(0o700)
    (output / "location.json").write_text(json.dumps({"temporary": str(temporary), "work": str(work)}))
    immutable = {path.relative_to(work): hashlib.sha256(path.read_bytes()).hexdigest()
                 for directory in (work / "kora", work / "products")
                 for path in directory.rglob("*") if path.is_file() and "__pycache__" not in path.parts}
    immutable[Path("kora_cli.py")] = hashlib.sha256((work / "kora_cli.py").read_bytes()).hexdigest()
    return temporary, work, config, immutable


def namespace(temporary, config):
    executable = Path(shutil.which("codex")).resolve()
    release = executable.parent.parent
    authentication = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")) / "auth.json"
    if not authentication.is_file():
        raise RuntimeError("No está disponible la autenticación local de Codex")
    return ["bwrap", "--ro-bind", "/", "/", "--tmpfs", "/home", "--tmpfs", "/tmp",
            "--bind", str(temporary), str(temporary),
            "--ro-bind", str(release), str(release),
            "--ro-bind", str(authentication), str(config / "auth.json"),
            "--unshare-pid", "--new-session", "--proc", "/proc", "--dev", "/dev", "--"], executable


def run_codex(prefix, executable, work, config, name, prompt):
    output = work / "reports" / f"{name}-final.txt"
    command = [*prefix, str(executable), "-a", "never", "-s", "danger-full-access",
               "-m", "gpt-6-astra", "-c", 'model_reasoning_effort="max"',
               "-c", "features.apps=false", "-c", "features.remote_plugin=false",
               "-c", "features.memories=false", "-c", "check_for_update_on_startup=false",
               "-c", f"projects.{json.dumps(str(work))}.trust_level=\"trusted\"",
               "exec", "--ephemeral", "--ignore-user-config", "--ignore-rules", "--json",
               "-C", str(work), "--output-last-message", str(output), prompt]
    environment = dict(os.environ)
    environment["CODEX_HOME"] = str(config)
    environment["PYTHONPATH"] = str(work)
    emit({"phase": name, "started": True, "model": "gpt-6-astra", "effort": "max"})
    with (work / "reports" / f"{name}-events.jsonl").open("wb") as events, \
         (work / "reports" / f"{name}-errors.log").open("wb") as errors:
        result = subprocess.run(command, cwd=work, env=environment, stdout=events, stderr=errors)
    if result.returncode:
        raise RuntimeError(f"La fase {name} terminó con código {result.returncode}; evidencia privada conservada")
    return output.read_text(encoding="utf-8")


def evaluate(prefix, executable, work, config, name):
    prompt = (
        "Usa $inspector-envios directamente en esta sesión, lee su skill y conocimiento. "
        "Evalúa A: permiso VIGENTE, sin lluvia, masa 10 kg; "
        "B: permiso VIGENTE, lluvia, masa 10 kg; "
        "C: permiso VIGENTE, sin lluvia, masa ausente; "
        "D: permiso VIGENTE, sin lluvia, masa 13 kg; "
        "E: permiso REVOCADO, lluvia, masa 10 kg. "
        "Devuelve solo JSON con cases (objeto A..E con valor de estado), distance y source_version. "
        "No edites archivos, no delegues y no crees Goals."
    )
    text = run_codex(prefix, executable, work, config, name, prompt)
    return json.loads(text.strip().removeprefix("```json").removesuffix("```").strip())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Directorio privado nuevo para recibo y localizador")
    args = parser.parse_args()
    temporary, work, config, immutable = prepare(args.output.resolve())
    prefix, executable = namespace(temporary, config)
    proof = subprocess.run([*prefix, "python3", "-c",
        "from pathlib import Path; "
        "assert not Path('/home/felix/kora-pneuma/kora.py').exists(); "
        "assert not Path('/home/felix/kora-pneuma/ley').exists(); "
        "assert not Path('/home/felix/kora-rebuild/kora').exists(); "
        "print('source_and_previous_kernel_unavailable')"], capture_output=True, text=True, check=True)
    emit({"phase": "isolation", "ok": "unavailable" in proof.stdout, "previous_core_access": False})
    prompt = (
        "Usa $kora para completar este encargo sintético dentro de este directorio. "
        "La maquinaria y sus fuentes nuevas están aquí; el host de construcción y sus repositorios anteriores son inaccesibles. "
        "Lee inputs/manual-envios-v1.txt. Korafica esa fuente como conocimiento con identidad " + KNOWLEDGE + ". "
        "Conserva original, alcance, prioridades, condiciones, excepción, incertidumbre y clave de versión. "
        "Crea después una skill llamada evaluar-envios con identidad " + SKILL + " que requiera ese conocimiento, "
        "y un agente llamado inspector-envios con identidad " + AGENT + " que requiera esa skill. "
        "La función de ambos es evaluar casos del manual; el agente devuelve JSON con cases (objeto id→estado), "
        "distance y source_version (la clave de versión de la fuente), leyendo el conocimiento vigente. "
        "Autoriza ambos destinos Codex y Hermes. Usa kora_cli.py para crear, comprobar e instalar los tres "
        "productos en este directorio como --home, conservando los archivos que ya existen. "
        "Elige namespace probe. No construyas otro núcleo ni cambies kora/, kora_cli.py, los productos de "
        "maquinaria ni el original. Puedes preparar cuerpos en inputs/. No lances otros modelos, no delegues, "
        "no publiques Git y no crees Goals. Completa la realización efectiva y devuelve qué comprobaste."
    )
    run_codex(prefix, executable, work, config, "author", prompt)
    catalog = Catalog(work)
    knowledge, skill, agent = [catalog.get(identifier) for identifier in (KNOWLEDGE, SKILL, AGENT)]
    assert knowledge.kind == "knowledge" and skill.kind == "skill" and agent.kind == "agent"
    assert KNOWLEDGE in skill.requires and SKILL in agent.requires
    originals = knowledge.metadata.get("provenance", {}).get("sources", [])
    assert any((knowledge.directory / item["path"]).read_bytes() == SOURCE.encode()
               and item["sha256"] == hashlib.sha256(SOURCE.encode()).hexdigest() for item in originals)
    state = Installer(work).status()
    assert not state["changes"]
    assert (work / ".codex/agents/inspector-envios.toml").is_file()
    assert (work / ".hermes/profiles/inspector-envios/SOUL.md").is_file()
    before = evaluate(prefix, executable, work, config, "read_v1")
    expected = {"A": "AUTORIZADA", "B": "DIFERIDA", "C": "UNKNOWN", "D": "DENEGADA", "E": "DENEGADA"}
    assert before["cases"] == expected and before["distance"] == "UNKNOWN" and before["source_version"] == "PZ_6139_V1", before
    update = SOURCE.replace("versión 1", "versión 2").replace("PZ_6139_V1", "PZ_6139_V2").replace("12 kg", "15 kg")
    (work / "inputs/manual-envios-v2.txt").write_text(update, encoding="utf-8")
    run_codex(prefix, executable, work, config, "update", (
        "Usa $kora. Actualiza únicamente los tres productos probe existentes desde inputs/manual-envios-v2.txt. "
        "Preserva el original v1 y añade la nueva procedencia recuperable. Mantén las identidades y dependencias. "
        "Añade a la skill la nota de cambio de umbral con la clave vigente, para que su instalación cambie también. "
        "Comprueba e instala skill y agente en Codex y Hermes usando este directorio como --home. "
        "Conserva el estado ajeno. No modifiques maquinaria, no delegues, no lances inferencia adicional ni crees Goals."
    ))
    after = evaluate(prefix, executable, work, config, "read_v2")
    expected["D"] = "AUTORIZADA"
    assert after["cases"] == expected and after["distance"] == "UNKNOWN" and after["source_version"] == "PZ_6139_V2", after
    for relative, expected_hash in immutable.items():
        assert hashlib.sha256((work / relative).read_bytes()).hexdigest() == expected_hash, relative
    catalog = Catalog(work)
    knowledge = catalog.get(KNOWLEDGE)
    sources = knowledge.metadata["provenance"]["sources"]
    for original in (SOURCE, update):
        assert any((knowledge.directory / item["path"]).read_bytes() == original.encode()
                   and item["sha256"] == hashlib.sha256(original.encode()).hexdigest() for item in sources)
    for target in ("codex", "hermes"):
        for files in build(catalog, target, [SKILL, AGENT]).values():
            for relative, expected_file in files.items():
                installed = work / relative
                assert installed.read_bytes() == expected_file.data, relative
                assert installed.stat().st_mode & 0o777 == expected_file.mode, relative
    state = Installer(work).status()
    assert not state["changes"] and not state["recovery_pending"] and not state["preserved_changes"], state
    test_result = subprocess.run([*prefix, "python3", "-m", "unittest", "discover", "-s", "tests", "-p", "test_install.py", "-v"],
        cwd=work, capture_output=True, text=True)
    (work / "reports/recovery-tests.log").write_text(test_result.stdout + test_result.stderr)
    assert test_result.returncode == 0, "Pruebas de recuperación independientes fallaron"
    report = {"ok": True, "old_core_access": False, "authoring": "actual KORA native direct activation",
              "targets_installed": ["codex", "hermes"], "native_behavior_observed": ["codex"],
              "before": before, "after": after, "recovery_process_tests": "PASS",
              "hermes_behavior": "pending on this authored corpus", "temporary_preserved": True}
    (args.output / "result.json").write_text(json.dumps(report, ensure_ascii=False, indent=2))
    emit(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
