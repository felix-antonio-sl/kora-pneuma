#!/usr/bin/env python3
"""Prueba KORA sin sus antepasados ni el estado privado del host.

--offline prueba maquinaria y biblioteca sin red, modelo ni autenticación.
--output prueba autoría y mantenimiento con inferencia real autorizada de Codex.
Los montajes ocultan /home y /tmp. No modifican el namespace del host.
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
from kora.catalog import Catalog, knowledge_root
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


def copy_operating_tree(work):
    library = knowledge_root(ROOT)
    if library == ROOT:
        raise RuntimeError("El ensayo requiere una biblioteca separada mediante el enlace knowledge")
    work.mkdir()
    for name in ("kora", "products", "archive/products", "docs", "tests", "scripts"):
        shutil.copytree(ROOT / name, work / name, symlinks=True,
                        ignore=shutil.ignore_patterns("__pycache__"))
    for name in ("kora_cli.py", "README.md", "AGENTS.md", ".gitignore", "requirements.txt"):
        shutil.copy2(ROOT / name, work / name)
    copied_library = work / "knowledge"
    copied_library.mkdir()
    # Only published reference data enters the isolated fixture. In particular,
    # Git, incoming resources, drafts and publication temporaries remain outside.
    for name in ("references", "versions", "archive/references"):
        if (library / name).exists():
            shutil.copytree(library / name, copied_library / name, symlinks=True)
    for name in ("aliases.yaml", "legacy-modes.yaml"):
        if (library / name).exists():
            shutil.copy2(library / name, copied_library / name)
    links = [path for path in work.rglob("*") if path.is_symlink()]
    for path in links:
        if path.exists() and path.resolve().is_relative_to(work):
            continue
        original = (library / path.relative_to(copied_library) if path.is_relative_to(copied_library)
                    else ROOT / path.relative_to(work))
        # Map the link's lexical target, retaining a stable reference instead of
        # resolving it prematurely to the currently published version.
        target = Path(os.path.abspath(original.parent / os.readlink(original)))
        if target.is_relative_to(library):
            destination = copied_library / target.relative_to(library)
        elif target.is_relative_to(ROOT):
            destination = work / target.relative_to(ROOT)
        else:
            raise RuntimeError(f"Enlace operativo fuera de maquinaria y biblioteca: {original}")
        path.unlink()
        path.symlink_to(os.path.relpath(destination, path.parent))
    assert all(path.exists() and path.resolve().is_relative_to(work) for path in links)
    return len(links)


def fingerprint(path):
    return ("link:" + os.readlink(path) if path.is_symlink()
            else "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest())


def prepare(output):
    temporary = Path(tempfile.mkdtemp(prefix="kora-independence-"))
    temporary.chmod(0o700)
    work = temporary / "work"
    copy_operating_tree(work)
    catalog = Catalog(work)
    agent = catalog.get("urn:kora:artefacto:kora")
    (work / "inputs").mkdir()
    (work / "inputs/manual-envios-v1.txt").write_text(SOURCE, encoding="utf-8")
    (work / "reports").mkdir()
    Installer(work).apply(build(Catalog(work), "codex", [agent.id]))
    subprocess.run(["git", "init", "-q", str(work)], check=True)
    config = temporary / "codex"
    config.mkdir()
    (config / "auth.json").touch(mode=0o600)
    (config / "config.toml").write_text('[analytics]\nenabled = false\n', encoding="utf-8")
    output.mkdir(parents=True, exist_ok=False)
    output.chmod(0o700)
    (output / "location.json").write_text(json.dumps({"temporary": str(temporary), "work": str(work)}))
    immutable = {path.relative_to(work): fingerprint(path)
                 for directory in (work / "kora", work / "products", work / "archive/products",
                                   work / "docs", work / "scripts", work / "tests", work / "knowledge")
                 for path in directory.rglob("*")
                 if (path.is_file() or path.is_symlink()) and "__pycache__" not in path.parts}
    for name in ("kora_cli.py", "README.md", "AGENTS.md", ".gitignore", "requirements.txt"):
        immutable[Path(name)] = fingerprint(work / name)
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


def offline():
    # Copy current sources, not a Git revision, a private backup or an installed
    # realization. Machinery and library are copied explicitly, without private
    # work in progress or construction tools.
    with tempfile.TemporaryDirectory(prefix="kora-offline-") as folder:
        temporary = Path(folder)
        work, home = temporary / "repo", temporary / "operator"
        internal_links = copy_operating_tree(work)
        home.mkdir()
        prefix = ["bwrap", "--ro-bind", "/", "/", "--tmpfs", "/home", "--tmpfs", "/tmp",
                  "--bind", str(temporary), str(temporary), "--unshare-net", "--unshare-pid",
                  "--new-session", "--proc", "/proc", "--dev", "/dev"]
        interpreter = sys.executable
        if sys.prefix != sys.base_prefix:
            # Keep the explicitly installed Python dependencies available even
            # when the invoking venv is inside the hidden original checkout.
            python_environment = temporary / "python"
            python_environment.mkdir()
            prefix += ["--ro-bind", sys.prefix, str(python_environment)]
            interpreter = str(python_environment / "bin" / Path(sys.executable).name)
        prefix.append("--")
        environment = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "PYTHONNOUSERSITE": "1"}

        def run(arguments):
            result = subprocess.run([*prefix, interpreter, *arguments], cwd=work,
                                    env=environment, capture_output=True, text=True, timeout=180)
            if result.returncode:
                raise RuntimeError(f"Falló la comprobación {arguments[0]}:\n{result.stdout}{result.stderr}")
            return result

        run(["-c", "from pathlib import Path; "
             f"assert not Path({str(ROOT)!r}).exists(); "
             f"assert not Path({str(knowledge_root(ROOT))!r}).exists(); "
             "assert not list(Path('/home').iterdir()); "
             "assert not Path('.git').exists(); "
             "assert not Path('archive/reconstruction').exists(); "
             "assert not Path('archive/previous').exists(); "
             "assert not Path('._local').exists(); "
             "assert Path('knowledge').is_dir() and not Path('knowledge').is_symlink(); "
             "assert not Path('knowledge/.git').exists(); "
             "assert not Path('knowledge/inbox').exists(); "
             "assert not Path('knowledge/drafts').exists()"])
        report = json.loads(run(["kora_cli.py", "check"]).stdout)
        assert report["ok"], report
        emit({"phase": "isolated_catalog", "active": report["active"], "archived": report["archived"],
              "internal_links": internal_links, "separate_library": True, "ok": True})
        installations = {}
        for target in ("codex", "hermes"):
            receipt = json.loads(run(["kora_cli.py", "install", target, "--home", str(home)]).stdout)
            installations[target] = {"changed_files": len(receipt["changed"])}
        state = json.loads(run(["kora_cli.py", "status", "--home", str(home)]).stdout)
        assert not state["changes"] and not state["recovery_pending"] and not state["preserved_changes"]
        result = run(["-m", "unittest", "discover", "-s", "tests", "-v"])
        emit({"phase": "offline", "ok": True, "network": False, "personal_home": False,
              "construction_archive": False, "git_required": False, "model_called": False,
              "installations": installations, "tests": result.stderr.strip().splitlines()[-3:],
              "skipped": [line for line in result.stderr.splitlines() if "... skipped " in line]})
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--offline", action="store_true", help="Probar el árbol operativo sin red ni modelo")
    mode.add_argument("--output", type=Path, help="Usar inferencia real; directorio privado nuevo para recibo y localizador")
    args = parser.parse_args()
    if args.offline:
        return offline()
    temporary, work, config, immutable = prepare(args.output.resolve())
    prefix, executable = namespace(temporary, config)
    proof = subprocess.run([*prefix, "python3", "-c",
        "from pathlib import Path; "
        f"assert not Path({str(ROOT)!r}).exists(); "
        f"assert not Path({str(knowledge_root(ROOT))!r}).exists(); "
        "assert not Path('archive/reconstruction').exists(); "
        "assert not Path('archive/previous').exists(); "
        "print('source_and_previous_kernel_unavailable')"], capture_output=True, text=True, check=True)
    emit({"phase": "isolation", "ok": "unavailable" in proof.stdout, "previous_core_access": False})
    prompt = (
        "Usa $kora para completar este encargo sintético dentro de este directorio. "
        "La maquinaria y una copia separada de su biblioteca están aquí; el host de construcción y sus repositorios anteriores son inaccesibles. "
        "Lee inputs/manual-envios-v1.txt. Korafica esa fuente como conocimiento con identidad " + KNOWLEDGE + ". "
        "Conserva original, alcance, prioridades, condiciones, excepción, incertidumbre y clave de versión. "
        "Está delegada explícitamente la aprobación SOLO de este conocimiento sintético de prueba, " + KNOWLEDGE + ", "
        "y únicamente desde la fuente ficticia indicada. Usa intake, create knowledge, review y approve --reviewed "
        "para conservar el recurso, preparar el borrador y publicar la revisión que hayas comparado con la fuente. "
        "Esto no autoriza aprobar, revisar ni editar conocimiento real o heredado de la biblioteca. "
        "Crea después una skill llamada evaluar-envios con identidad " + SKILL + " que requiera ese conocimiento, "
        "y un agente llamado inspector-envios con identidad " + AGENT + " que requiera esa skill. "
        "La función de ambos es evaluar casos del manual; el agente devuelve JSON con cases (objeto id→estado), "
        "distance y source_version (la clave de versión de la fuente), leyendo el conocimiento vigente. "
        "Autoriza ambos destinos Codex y Hermes. Usa kora_cli.py para comprobar e instalar la skill y el agente "
        "en este directorio como --home, conservando los archivos que ya existen. El conocimiento se consulta por referencia. "
        "Elige namespace probe. No construyas otro núcleo ni cambies kora/, kora_cli.py, los productos de "
        "maquinaria ni el original. Puedes preparar cuerpos en inputs/. No lances otros modelos, no delegues, "
        "no publiques Git y no crees Goals. Completa la realización efectiva y devuelve qué comprobaste."
    )
    run_codex(prefix, executable, work, config, "author", prompt)
    catalog = Catalog(work)
    knowledge, skill, agent = [catalog.get(identifier) for identifier in (KNOWLEDGE, SKILL, AGENT)]
    assert knowledge.kind == "knowledge" and skill.kind == "skill" and agent.kind == "agent"
    assert knowledge.reference_root == work / "knowledge"
    assert knowledge.metadata["publication"]["status"] == "approved"
    assert KNOWLEDGE in skill.requires and SKILL in agent.requires
    first_revision = knowledge.revision
    first_content = knowledge.content_path.read_bytes()
    reference_path = knowledge.content_path
    originals = knowledge.metadata.get("provenance", {}).get("sources", [])
    assert any((knowledge.directory / item["path"]).read_bytes() == SOURCE.encode()
               and item["sha256"] == hashlib.sha256(SOURCE.encode()).hexdigest() for item in originals)
    state = Installer(work).status()
    assert not state["changes"]
    assert (work / ".codex/agents/inspector-envios.toml").is_file()
    assert (work / ".hermes/profiles/inspector-envios/SOUL.md").is_file()
    native_before = {relative: fingerprint(work / relative)
                     for target in ("codex", "hermes")
                     for files in build(catalog, target, [SKILL, AGENT]).values()
                     for relative in files}
    before = evaluate(prefix, executable, work, config, "read_v1")
    expected = {"A": "AUTORIZADA", "B": "DIFERIDA", "C": "UNKNOWN", "D": "DENEGADA", "E": "DENEGADA"}
    assert before["cases"] == expected and before["distance"] == "UNKNOWN" and before["source_version"] == "PZ_6139_V1", before
    update = SOURCE.replace("versión 1", "versión 2").replace("PZ_6139_V1", "PZ_6139_V2").replace("12 kg", "15 kg")
    (work / "inputs/manual-envios-v2.txt").write_text(update, encoding="utf-8")
    run_codex(prefix, executable, work, config, "update", (
        "Usa $kora. Actualiza únicamente el conocimiento sintético " + KNOWLEDGE + " desde inputs/manual-envios-v2.txt. "
        "Preserva el original v1 y añade la nueva procedencia recuperable. Mantén las identidades y dependencias. "
        "Está delegada explícitamente la aprobación SOLO de la revisión de ese conocimiento sintético desde la fuente v2 indicada. "
        "Usa revise para preparar el borrador; compara su contenido, ejecuta review y publica mediante approve --reviewed. "
        "No edites directamente references ni versions. La referencia v1 debe permanecer consultable hasta publicar v2. "
        "No cambies ni reinstales skill o agente: deben leer la nueva versión por la misma referencia estable. "
        "No apruebes ni edites otros conocimientos. Conserva el estado ajeno; no modifiques maquinaria, "
        "no delegues, no lances inferencia adicional ni crees Goals."
    ))
    after = evaluate(prefix, executable, work, config, "read_v2")
    expected["D"] = "AUTORIZADA"
    assert after["cases"] == expected and after["distance"] == "UNKNOWN" and after["source_version"] == "PZ_6139_V2", after
    for relative, expected_hash in immutable.items():
        assert fingerprint(work / relative) == expected_hash, relative
    for relative, expected_hash in native_before.items():
        assert fingerprint(work / relative) == expected_hash, relative
    catalog = Catalog(work)
    knowledge = catalog.get(KNOWLEDGE)
    assert knowledge.reference_root == work / "knowledge"
    assert knowledge.metadata["publication"]["status"] == "approved"
    assert knowledge.content_path == reference_path and knowledge.revision != first_revision
    assert catalog.at_revision(KNOWLEDGE, first_revision).content_path.read_bytes() == first_content
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
              "separate_library": True, "knowledge_approval": "delegated only for synthetic probe knowledge",
              "updated_without_reinstall": True, "exact_prior_revision_readable": True,
              "before": before, "after": after, "recovery_process_tests": "PASS",
              "hermes_behavior": "pending on this authored corpus", "temporary_preserved": True}
    (args.output / "result.json").write_text(json.dumps(report, ensure_ascii=False, indent=2))
    emit(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
