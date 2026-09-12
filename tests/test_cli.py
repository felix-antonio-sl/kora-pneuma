import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml

from kora.authoring import create
from kora.catalog import Catalog, KoraError
from kora.cli import build, execute, parser


class CliJourneyTests(unittest.TestCase):
    def test_check_rejects_missing_or_file_root_without_creating_it(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            absent, occupied = base / "absent", base / "file"
            occupied.write_text("user data")
            library = base / "library"
            library.mkdir()
            executable = Path(__file__).resolve().parents[1] / "kora_cli.py"
            for root in (absent, occupied):
                with self.subTest(root=root):
                    result = subprocess.run([
                        sys.executable, str(executable), "--root", str(root),
                        "--knowledge-root", str(library), "check",
                    ], capture_output=True, text=True)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn("raíz", result.stdout + result.stderr)
            self.assertFalse(absent.exists())
            self.assertEqual(occupied.read_text(), "user data")
            result = subprocess.run([
                sys.executable, str(executable), "--root", str(library), "check",
            ], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(json.loads(result.stdout)["ok"])

    def test_realization_still_detects_concurrent_local_permission_changes(self):
        from kora.render_codex import render

        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            body = root / "body.md"
            body.write_text("Read the supplied source.\n")
            item = create(root, "skill", "test", "reader", "urn:test:skill:reader",
                          "Read a source", body, targets=["codex"])
            resource = item.directory / "reference.txt"
            resource.write_text("Local resource.\n")
            resource.chmod(0o644)
            metadata = {**item.metadata, "resources": ["reference.txt"]}
            (item.directory / "object.yaml").write_text(yaml.safe_dump(metadata))

            def change_permission(catalog, product):
                files = render(catalog, product)
                resource.chmod(0o600)
                return files

            with patch("kora.render_codex.render", side_effect=change_permission):
                with self.assertRaisesRegex(KoraError, "fuente cambió"):
                    build(Catalog(root), "codex", [item.id])

    def test_an_alias_used_for_installation_also_retires_the_same_product(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            root, home = base / "corpus", base / "home"
            body = base / "body.md"
            body.write_text("Procedimiento de prueba.\n")
            create(root, "skill", "one", "alias-reader", "urn:one:skill:reader", "Leer", body,
                   targets=["codex"])
            (root / "aliases.yaml").write_text("urn:old:reader: urn:one:skill:reader\n")
            executable = Path(__file__).resolve().parents[1] / "kora_cli.py"
            for action in ("install", "remove"):
                result = subprocess.run([sys.executable, str(executable), "--root", str(root),
                    action, "codex", "urn:old:reader", "--home", str(home)], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                if action == "install":
                    self.assertTrue((home / ".agents/skills/alias-reader/SKILL.md").is_file())
            self.assertFalse((home / ".agents/skills/alias-reader/SKILL.md").exists())

    def test_check_reports_physical_collision_between_individually_valid_products(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            body = root / "body.md"
            body.write_text("Procedimiento utilizable.\n")
            create(root, "skill", "one", "same-name", "urn:one:skill:same", "Una función", body,
                   targets=["codex"])
            create(root, "skill", "two", "same-name", "urn:two:skill:same", "Otra función", body,
                   targets=["codex"])
            executable = Path(__file__).resolve().parents[1] / "kora_cli.py"
            result = subprocess.run([sys.executable, str(executable), "--root", str(root),
                                     "check", "--target", "codex"], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1, result.stderr)
            report = json.loads(result.stdout)
            self.assertFalse(report["ok"])
            self.assertIn("same-name/SKILL.md", report["issues"][0]["error"])

    def test_check_reports_independent_failures_after_combined_realization_fails(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            body = root / "body.md"
            body.write_text("Consultar la fuente.\n")
            first = create(root, "skill", "test", "first", "urn:test:skill:first",
                           "Primera función", body, targets=["codex"])
            second = create(root, "skill", "test", "second", "urn:test:skill:second",
                            "Segunda función", body, targets=["codex"])
            for product, updates in (
                (first, {"description": "x" * 1025}),
                (second, {"requires": ["urn:test:skill:missing"]}),
            ):
                (product.directory / "object.yaml").write_text(
                    yaml.safe_dump({**product.metadata, **updates}))
            report = execute(parser().parse_args(["--root", str(root), "check", "--target", "codex"]))
            self.assertFalse(report["ok"])
            failures = {issue.get("source") for issue in report["issues"] if issue.get("target") == "codex"}
            self.assertEqual(failures, {first.id, second.id})

    def test_relocated_source_to_two_native_targets_update_and_rollback(self):
        import hashlib

        # Approval is explicitly delegated for this synthetic fixture only.
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            source = base / "source.txt"
            original = "La actividad puede continuar con permiso vigente, salvo revocación.\n"
            source.write_text(original)
            body = base / "body.md"
            first_content = "Conservar permiso, condición y excepción; consultar fuente antes de afirmar.\n"
            body.write_text(first_content)
            root = base / "initial/machinery"
            library = base / "initial/library"
            home = base / "home"
            root.mkdir(parents=True)
            library.mkdir()
            (root / "knowledge").symlink_to("../library", target_is_directory=True)
            home.mkdir()
            implementation = Path(__file__).resolve().parents[1]
            shutil.copytree(implementation / "kora", root / "kora",
                            ignore=shutil.ignore_patterns("__pycache__"))
            shutil.copy2(implementation / "kora_cli.py", root / "kora_cli.py")

            def run(*args):
                result = subprocess.run([sys.executable, str(root / "kora_cli.py"), *args],
                                        cwd=base, capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                return json.loads(result.stdout)

            intake = run("intake", "permission", "--source", str(source))
            received = Path(intake["path"]) / intake["sources"][0]["path"]
            self.assertEqual(received.read_bytes(), source.read_bytes())
            draft = run("create", "knowledge", "example", "permission", "--id", "urn:example:kb:permission",
                        "--description", "Permiso y excepción", "--body", str(body), "--source", str(received))
            self.assertEqual(draft["publication"], "draft")
            self.assertEqual(run("list", "--kind", "knowledge"), [])
            review = run("review", "urn:example:kb:permission")
            first = run("approve", "urn:example:kb:permission", "--reviewed", review["reviewed_sha256"])
            self.assertEqual(first["publication"], "approved")
            run("create", "skill", "example", "read-permission", "--id", "urn:example:skill:read",
                "--description", r"Interpretar permiso y patrón \d+", "--body", str(body),
                "--requires", "urn:example:kb:permission")
            run("create", "agent", "example", "permission-reader", "--id", "urn:example:agent:reader",
                "--description", "Usa la habilidad y declara límites", "--body", str(body),
                "--requires", "urn:example:skill:read")
            for runtime in ("codex", "hermes"):
                run("install", runtime, "--home", str(home))
            previous, previous_library = root, library
            root, library = base / "relocated/machinery", base / "relocated/library"
            root.parent.mkdir()
            shutil.move(previous, root)
            shutil.move(previous_library, library)
            source.unlink()
            body.unlink()
            shutil.rmtree(library / "inbox")
            self.assertFalse(previous.exists())
            self.assertFalse(previous_library.exists())
            resolved = run("resolve", "urn:example:kb:permission")
            self.assertTrue(Path(resolved["path"]).is_relative_to(library / "references"))
            self.assertFalse((root / "products/example/permission").exists())
            originals = list((Path(resolved["path"]).parent / "sources").iterdir())
            self.assertEqual(len(originals), 1)
            self.assertEqual(originals[0].read_text(), original)
            for runtime in ("codex", "hermes"):
                run("install", runtime, "--home", str(home))
            native_paths = (".codex/agents/permission-reader.toml",
                            ".agents/skills/read-permission/SKILL.md",
                            ".hermes/profiles/permission-reader/SOUL.md",
                            ".hermes/profiles/permission-reader/skills/read-permission/SKILL.md")
            for relative in native_paths:
                native_text = (home / relative).read_text()
                self.assertIn(str(root / "products"), native_text)
                self.assertIn(str(library / "references"), native_text)
                self.assertNotIn(str(previous), native_text)
                self.assertNotIn(str(previous_library), native_text)
            self.assertTrue((home / ".codex/agents/permission-reader.toml").is_file())
            self.assertTrue((home / ".hermes/profiles/permission-reader/SOUL.md").is_file())

            native_before = {relative: (home / relative).read_bytes() for relative in native_paths}
            pending = run("revise", "urn:example:kb:permission")
            pending_path = Path(pending["path"])
            second_content = first_content + "Registrar la revocación antes de continuar.\n"
            pending_path.write_text(second_content)
            next_source = base / "source-v2.txt"
            next_original = original + "La revocación debe registrarse antes de continuar.\n"
            next_source.write_text(next_original)
            copied_source = pending_path.parent / "sources/2-source-v2.txt"
            shutil.copy2(next_source, copied_source)
            metadata_path = pending_path.parent / "object.yaml"
            metadata = yaml.safe_load(metadata_path.read_text())
            metadata["provenance"]["sources"].append({
                "path": "sources/2-source-v2.txt", "origin": str(next_source),
                "sha256": hashlib.sha256(next_source.read_bytes()).hexdigest()})
            metadata_path.write_text(yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False))
            self.assertEqual(Path(resolved["path"]).read_text(), first_content)
            self.assertEqual(run("resolve", "urn:example:kb:permission")["revision"], first["revision"])
            review = run("review", "urn:example:kb:permission")
            self.assertEqual(review["base_revision"], first["revision"])
            second = run("approve", "urn:example:kb:permission", "--reviewed", review["reviewed_sha256"])
            next_source.unlink()
            self.assertNotEqual(second["revision"], first["revision"])
            self.assertEqual(second["path"], resolved["path"])
            self.assertEqual(Path(second["path"]).read_text(), second_content)
            old = run("resolve", "urn:example:kb:permission", "--revision", first["revision"])
            self.assertEqual(Path(old["path"]).read_text(), first_content)
            self.assertEqual((Path(second["path"]).parent / "sources/2-source-v2.txt").read_text(), next_original)
            for relative, before in native_before.items():
                self.assertEqual((home / relative).read_bytes(), before)

            personal = home / ".hermes/profiles/permission-reader/MEMORY.md"
            personal.write_bytes(b"personal memory")
            (root / "products/example/read-permission/content.md").write_text("Updated, with permission and revocation preserved.\n")
            for runtime, relative in (("codex", ".agents/skills/read-permission/SKILL.md"),
                                      ("hermes", ".hermes/profiles/permission-reader/skills/read-permission/SKILL.md")):
                run("install", runtime, "--home", str(home))
                native = home / relative
                self.assertIn("Updated", native.read_text())
                run("rollback", "--home", str(home))
                self.assertNotIn("Updated", native.read_text())
                self.assertEqual(run("resolve", "urn:example:kb:permission")["revision"], second["revision"])
            self.assertEqual(personal.read_bytes(), b"personal memory")
            run("recover", "--home", str(home))
            state = run("status", "--home", str(home))
            self.assertEqual(state["changes"], [])
            self.assertFalse(state["recovery_pending"])


class CliProfileMaintenanceTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.root = self.base / "corpus"
        self.home = self.base / "home"
        self.executable = Path(__file__).resolve().parents[1] / "kora_cli.py"

    def product(self, kind, name, requires=(), targets=("codex", "hermes")):
        body = self.base / f"{name}-body.md"
        body.write_text(f"{name} version one, with exception preserved.\n")
        return create(self.root, kind, "example", name, f"urn:example:{kind}:{name}",
                      f"Use {name}", body, targets=targets, requires=requires)

    def cli(self, *args, ok=True):
        command = [sys.executable, str(self.executable), "--root", str(self.root), *args]
        if args[0] in ("install", "remove", "status", "rollback", "recover"):
            command += ["--home", str(self.home)]
        result = subprocess.run(command, cwd=self.base, capture_output=True, text=True)
        if ok:
            self.assertEqual(result.returncode, 0, result.stderr)
            return json.loads(result.stdout)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        return result

    def test_profile_dependency_update_and_alias_removal_preserve_shared_and_personal_files(self):
        knowledge = self.product("knowledge", "rules")
        leaf = self.product("skill", "read-rules", [knowledge.id])
        middle = self.product("skill", "interpret-rules", [leaf.id])
        top = self.product("skill", "review-delivery", [middle.id])
        peer = self.product("skill", "review-another", [middle.id])
        tool = leaf.directory / "scripts/check.sh"
        tool.parent.mkdir()
        tool.write_bytes(b"#!/bin/sh\nexit 0\n")
        tool.chmod(0o755)
        (self.root / "aliases.yaml").write_text(f"urn:old:review: {top.id}\n")
        profile = self.home / ".hermes/profiles/dev"
        personal = {"SOUL.md": b"Personal identity", "config.yaml": b"provider: personal\n",
                    "memories/MEMORY.md": b"Personal memory", "skills/review-delivery/note.txt": b"Local note"}
        for relative, data in personal.items():
            path = profile / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)

        self.cli("install", "hermes", "urn:old:review", "--profile", "Dev")
        self.assertIn(f"hermes@profile:dev:{top.id}", self.cli("status")["bundles"])
        self.assertFalse((self.home / ".hermes/skills/read-rules/SKILL.md").exists())
        self.assertEqual((profile / "skills/read-rules/scripts/check.sh").stat().st_mode & 0o777, 0o755)
        self.cli("install", "hermes", top.id)
        leaf.content_path.write_text("Version two; the exception remains.\n")
        self.cli("install", "hermes", leaf.id)
        global_leaf = self.home / ".hermes/skills/read-rules/SKILL.md"
        self.assertIn("Version two", global_leaf.read_text())
        self.assertEqual(global_leaf.read_bytes(), (profile / "skills/read-rules/SKILL.md").read_bytes())

        self.cli("install", "hermes", peer.id, "--profile", "dev")
        self.cli("remove", "hermes", "urn:old:review", "--profile", "dev")
        self.assertFalse((profile / "skills/review-delivery/SKILL.md").exists())
        self.assertTrue((profile / "skills/read-rules/SKILL.md").is_file())
        self.assertTrue((profile / "skills/review-another/SKILL.md").is_file())
        self.assertTrue((self.home / ".hermes/skills/review-delivery/SKILL.md").is_file())
        self.assertIn(f"hermes:{top.id}", self.cli("status")["bundles"])
        self.assertNotIn(f"hermes@profile:dev:{top.id}", self.cli("status")["bundles"])
        for relative, data in personal.items():
            self.assertEqual((profile / relative).read_bytes(), data)

    def test_install_all_refreshes_registered_profile_without_discovering_unmanaged_copies(self):
        skill = self.product("skill", "maintain")
        self.cli("install", "hermes", skill.id, "--profile", "dev")
        unmanaged = self.home / ".hermes/profiles/urgencia/skills/maintain/SKILL.md"
        unmanaged.parent.mkdir(parents=True)
        unmanaged.write_bytes(b"Unmanaged copy")
        skill.content_path.write_text("Updated source.\n")
        self.cli("install", "hermes")
        for relative in (".hermes/skills/maintain/SKILL.md",
                         ".hermes/profiles/dev/skills/maintain/SKILL.md"):
            self.assertIn("Updated source", (self.home / relative).read_text())
        self.assertEqual(unmanaged.read_bytes(), b"Unmanaged copy")
        self.assertNotIn(f"hermes@profile:urgencia:{skill.id}", self.cli("status")["bundles"])

    def test_profile_update_refreshes_shared_consumers_only_in_that_profile(self):
        shared = self.product("skill", "shared")
        first = self.product("skill", "first", [shared.id])
        second = self.product("skill", "second", [shared.id])
        self.cli("install", "hermes", first.id, second.id, "--profile", "dev")
        self.cli("install", "hermes", first.id)
        self.cli("install", "hermes", second.id, "--profile", "urgencia")
        state_path = self.home / ".local/state/kora/installed.json"
        previous_state = json.loads(state_path.read_text())
        preserved = {
            relative: (self.home / relative).read_bytes()
            for bundle, members in previous_state.items()
            if not bundle.startswith("hermes@profile:dev:")
            for relative in members
        }

        shared.content_path.write_text("Shared dependency version two.\n")
        self.cli("install", "hermes", shared.id, "--profile", "dev")
        self.assertIn("Shared dependency version two",
                      (self.home / ".hermes/profiles/dev/skills/shared/SKILL.md").read_text())
        current_state = json.loads(state_path.read_text())
        for product in (first, second):
            key = f"hermes@profile:dev:{product.id}"
            self.assertNotEqual(current_state[key], previous_state[key])
        for bundle, members in previous_state.items():
            if not bundle.startswith("hermes@profile:dev:"):
                self.assertEqual(current_state[bundle], members)
        for relative, data in preserved.items():
            self.assertEqual((self.home / relative).read_bytes(), data)
        self.assertEqual(self.cli("status")["changes"], [])

    def test_dependency_update_refreshes_managed_agents_only_in_requested_target(self):
        skill = self.product("skill", "shared")
        agent = self.product("agent", "managed", [skill.id])
        self.product("agent", "not-installed", [skill.id])
        for target in ("codex", "hermes"):
            self.cli("install", target, agent.id)
        codex = self.home / ".agents/skills/shared/SKILL.md"
        hermes = self.home / ".hermes/profiles/managed/skills/shared/SKILL.md"
        skill.content_path.write_text("Version two.\n")
        self.cli("install", "codex", skill.id)
        self.assertIn("Version two", codex.read_text())
        self.assertIn("version one", hermes.read_text())
        self.assertFalse((self.home / ".codex/agents/not-installed.toml").exists())
        skill.content_path.write_text("Version three.\n")
        self.cli("install", "hermes", skill.id)
        self.assertIn("Version three", hermes.read_text())
        self.assertIn("Version three", (self.home / ".hermes/skills/shared/SKILL.md").read_text())
        self.assertIn("Version two", codex.read_text())
        self.assertFalse((self.home / ".hermes/profiles/not-installed").exists())
        self.assertEqual(self.cli("status")["changes"], [])

    def test_other_dependencies_of_refreshed_consumers_keep_shared_receipts_consistent(self):
        selected = self.product("skill", "selected", targets=["codex"])
        secondary = self.product("skill", "secondary", targets=["codex"])
        first = self.product("agent", "a-secondary", [secondary.id], targets=["codex"])
        last = self.product("agent", "z-both", [selected.id, secondary.id], targets=["codex"])
        self.cli("install", "codex", first.id, last.id)
        state_path = self.home / ".local/state/kora/installed.json"
        previous_state = json.loads(state_path.read_text())
        secondary_path = ".agents/skills/secondary/SKILL.md"
        secondary_before = (self.home / secondary_path).read_bytes()
        secondary_mode = (self.home / secondary_path).stat().st_mode & 0o777
        selected.content_path.write_text("Selected updated.\n")
        secondary.content_path.write_text("Secondary updated.\n")
        self.cli("install", "codex", selected.id)
        self.assertIn("Selected updated", (self.home / ".agents/skills/selected/SKILL.md").read_text())
        self.assertEqual((self.home / secondary_path).read_bytes(), secondary_before)
        self.assertEqual((self.home / secondary_path).stat().st_mode & 0o777, secondary_mode)
        current_state = json.loads(state_path.read_text())
        for bundle in (f"codex:{first.id}", f"codex:{last.id}"):
            self.assertEqual(current_state[bundle].get(secondary_path), previous_state[bundle].get(secondary_path))
        comparison = self.cli("status", "--compare-source", "--target", "codex",
                              "--id", last.id)
        entry = next(item for item in comparison["source_comparison"]
                     if item["id"] == last.id)
        self.assertEqual(entry["source_state"], "current")
        self.assertEqual(entry["dependency_state"], "changed")
        self.assertEqual(self.cli("status")["changes"], [])

    def test_removed_dependency_reconciles_previous_owners_in_each_requested_location(self):
        shared = self.product("skill", "shared")
        consumer = self.product("skill", "consumer", [shared.id])
        other = self.product("skill", "other-consumer", [shared.id])
        for target in ("codex", "hermes"):
            self.cli("install", target, consumer.id, other.id)
        self.cli("install", "hermes", consumer.id, "--profile", "dev")
        self.cli("install", "hermes", other.id, "--profile", "dev")
        body_before = {}
        for prefix in (".agents", ".hermes"):
            body_before[(prefix, "consumer")] = (
                self.home / prefix / "skills/consumer/SKILL.md").read_bytes()
            body_before[(prefix, "other-consumer")] = (
                self.home / prefix / "skills/other-consumer/SKILL.md").read_bytes()
        body_before[(".hermes/profiles/dev", "consumer")] = (
            self.home / ".hermes/profiles/dev/skills/consumer/SKILL.md").read_bytes()
        body_before[(".hermes/profiles/dev", "other-consumer")] = (
            self.home / ".hermes/profiles/dev/skills/other-consumer/SKILL.md").read_bytes()
        metadata_path = consumer.directory / "object.yaml"
        metadata = yaml.safe_load(metadata_path.read_text())
        metadata["requires"] = []
        metadata_path.write_text(yaml.safe_dump(metadata))
        shared.content_path.write_text("Shared version two.\n")
        state_path = self.home / ".local/state/kora/installed.json"
        previous_state = json.loads(state_path.read_text())

        for target, prefix in (("codex", ".agents"), ("hermes", ".hermes")):
            with self.subTest(target=target):
                self.cli("install", target, shared.id)
                self.assertIn("Shared version two", (self.home / prefix / "skills/shared/SKILL.md").read_text())
                state = json.loads(state_path.read_text())
                shared_path = f"{prefix}/skills/shared/SKILL.md"
                self.assertIn(shared_path, state[f"{target}:{consumer.id}"])
                self.assertIn(shared.id, (self.home / prefix / "skills/consumer/SKILL.md").read_text())
                self.assertEqual(state[f"{target}:{consumer.id}"][f"{prefix}/skills/consumer/SKILL.md"],
                                 previous_state[f"{target}:{consumer.id}"][f"{prefix}/skills/consumer/SKILL.md"])
                self.assertEqual((self.home / prefix / "skills/consumer/SKILL.md").read_bytes(),
                                 body_before[(prefix, "consumer")])
                self.assertEqual((self.home / prefix / "skills/other-consumer/SKILL.md").read_bytes(),
                                 body_before[(prefix, "other-consumer")])

                if target == "codex":
                    self.cli("install", target, consumer.id)
                    state = json.loads(state_path.read_text())
                    self.assertNotIn(shared_path, state[f"{target}:{consumer.id}"])
                    self.assertNotIn(shared.id, (self.home / prefix / "skills/consumer/SKILL.md").read_text())
                    self.assertEqual((self.home / prefix / "skills/other-consumer/SKILL.md").read_bytes(),
                                     body_before[(prefix, "other-consumer")])
                self.assertIn(shared_path, state[f"{target}:{other.id}"])
                self.assertIn("Shared version two", (self.home / prefix / "skills/shared/SKILL.md").read_text())

        profile = self.home / ".hermes/profiles/dev/skills"
        profile_shared = ".hermes/profiles/dev/skills/shared/SKILL.md"
        profile_consumer = ".hermes/profiles/dev/skills/consumer/SKILL.md"
        profile_other = ".hermes/profiles/dev/skills/other-consumer/SKILL.md"
        state = json.loads(state_path.read_text())
        self.assertIn(profile_shared, state[f"hermes@profile:dev:{consumer.id}"])
        self.assertIn(shared.id, (self.home / profile_consumer).read_text())
        self.assertEqual((self.home / profile_consumer).read_bytes(),
                         body_before[(".hermes/profiles/dev", "consumer")])
        self.assertEqual((self.home / profile_other).read_bytes(),
                         body_before[(".hermes/profiles/dev", "other-consumer")])
        self.assertIn("Shared version two", (self.home / profile_shared).read_text())
        self.cli("install", "hermes", consumer.id, "--profile", "dev")
        state = json.loads(state_path.read_text())
        self.assertNotIn(profile_shared, state[f"hermes@profile:dev:{consumer.id}"])
        self.assertNotIn(shared.id, (self.home / profile_consumer).read_text())
        self.assertIn(profile_shared, state[f"hermes@profile:dev:{other.id}"])
        self.assertTrue((self.home / profile_other).is_file())
        self.assertIn("Shared version two", (self.home / profile_shared).read_text())
        self.assertEqual(self.cli("status")["changes"], [])
        self.cli("rollback")
        self.assertIn("Shared version two", (profile / "shared/SKILL.md").read_text())
        self.assertIn(shared.id, (profile / "consumer/SKILL.md").read_text())

    def test_unrelated_archived_or_missing_source_does_not_block_focal_update(self):
        selected = self.product("skill", "selected")
        archived = self.product("skill", "archived")
        missing = self.product("skill", "missing")
        for target in ("codex", "hermes"):
            self.cli("install", target, selected.id, archived.id, missing.id)
        destination = self.root / "archive/products/example/archived"
        destination.parent.mkdir(parents=True)
        shutil.move(archived.directory, destination)
        shutil.rmtree(missing.directory)
        state_path = self.home / ".local/state/kora/installed.json"
        previous = json.loads(state_path.read_text())
        preserved = {relative: (self.home / relative).read_bytes()
                     for key, files in previous.items() if not key.endswith(selected.id)
                     for relative in files}
        selected.content_path.write_text("Selected version two.\n")

        for target in ("codex", "hermes"):
            with self.subTest(target=target):
                self.cli("install", target, selected.id)
        current = json.loads(state_path.read_text())
        for key, files in previous.items():
            if not key.endswith(selected.id):
                self.assertEqual(current[key], files)
        for relative, data in preserved.items():
            self.assertEqual((self.home / relative).read_bytes(), data)
        self.assertEqual(self.cli("status")["changes"], [])

    def test_removed_dependency_still_protects_a_local_edit_before_reconciliation(self):
        shared = self.product("skill", "shared")
        consumer = self.product("skill", "consumer", [shared.id])
        self.cli("install", "hermes", consumer.id, "--profile", "dev")
        native = self.home / ".hermes/profiles/dev/skills/shared/SKILL.md"
        native.write_text("Local work that must survive.\n")
        metadata_path = consumer.directory / "object.yaml"
        metadata = yaml.safe_load(metadata_path.read_text())
        metadata["requires"] = []
        metadata_path.write_text(yaml.safe_dump(metadata))
        shared.content_path.write_text("Shared version two.\n")
        state_path = self.home / ".local/state/kora/installed.json"
        previous = state_path.read_bytes()

        result = self.cli("install", "hermes", shared.id, "--profile", "dev", ok=False)
        self.assertIn("cambio local", result.stderr)
        self.assertEqual(native.read_text(), "Local work that must survive.\n")
        self.assertEqual(state_path.read_bytes(), previous)
        self.assertFalse((self.home / ".hermes/skills/shared/SKILL.md").exists())

    def test_reused_skill_name_does_not_reconcile_an_unrelated_profile(self):
        previous = self.product("skill", "same-name")
        self.cli("install", "hermes", previous.id, "--profile", "urgencia")
        metadata_path = previous.directory / "object.yaml"
        metadata = yaml.safe_load(metadata_path.read_text())
        metadata["name"] = "renamed-other"
        metadata_path.write_text(yaml.safe_dump(metadata))
        body = self.base / "independent.md"
        body.write_text("An independent procedure.\n")
        independent = create(self.root, "skill", "another", "same-name", "urn:another:skill:new",
                             "Independent", body, targets=["hermes"])
        state_path = self.home / ".local/state/kora/installed.json"
        state = json.loads(state_path.read_text())
        profile_file = self.home / ".hermes/profiles/urgencia/skills/same-name/SKILL.md"
        original = profile_file.read_bytes()

        self.cli("install", "hermes", independent.id)
        self.assertEqual(profile_file.read_bytes(), original)
        self.assertFalse((profile_file.parent.parent / "renamed-other").exists())
        current = json.loads(state_path.read_text())
        for key, files in state.items():
            self.assertEqual(current[key], files)
        self.assertIn("An independent procedure", (self.home / ".hermes/skills/same-name/SKILL.md").read_text())

    def test_profile_render_filters_skills_and_rejects_other_targets_types_and_unsafe_names(self):
        knowledge = self.product("knowledge", "reference")
        skill = self.product("skill", "procedure", [knowledge.id])
        agent = self.product("agent", "person", [skill.id])
        output = self.base / "rendered"
        report = self.cli("render", "hermes", "--profile", "review_team", "--output", str(output))
        self.assertEqual(report["bundles"], [f"hermes@profile:review_team:{skill.id}"])
        self.assertTrue((output / ".hermes/profiles/review_team/skills/procedure/SKILL.md").is_file())
        self.assertFalse(any(output.rglob("SOUL.md")))
        for action in ("render", "install", "remove"):
            extra = ["--output", str(self.base / "invalid-render")] if action == "render" else []
            with self.subTest(action=action, target="codex"):
                result = self.cli(action, "codex", skill.id, "--profile", "dev", *extra, ok=False)
                self.assertIn("solo", result.stderr)
            for product in (knowledge, agent):
                with self.subTest(action=action, kind=product.kind):
                    result = self.cli(action, "hermes", product.id, "--profile", "dev", *extra, ok=False)
                    self.assertIn("skill", result.stderr)
        for name in ("../dev", "dev/child", "dev:other", "dev\\child", "default", "x" * 65):
            with self.subTest(profile=name):
                result = self.cli("install", "hermes", skill.id, "--profile", name, ok=False)
                self.assertIn("perfil", result.stderr)
        self.assertFalse((self.base / "invalid-render").exists())

    def test_explicit_profile_assignment_does_not_adopt_existing_unmanaged_content(self):
        skill = self.product("skill", "existing")
        native = self.home / ".hermes/profiles/dev/skills/existing/SKILL.md"
        native.parent.mkdir(parents=True)
        native.write_bytes(b"Existing unowned instructions")
        result = self.cli("install", "hermes", skill.id, "--profile", "dev", ok=False)
        self.assertIn("adopción", result.stderr)
        self.assertEqual(native.read_bytes(), b"Existing unowned instructions")
        self.assertEqual(self.cli("status")["bundles"], [])

    def assert_invalid_managed_consumer_is_preserved(self, archive):
        skill = self.product("skill", "needed", targets=["codex"])
        agent = self.product("agent", "consumer", [skill.id], targets=["codex"])
        self.cli("install", "codex", agent.id)
        native = self.home / ".agents/skills/needed/SKILL.md"
        previous = native.read_bytes()
        if archive:
            destination = self.root / "archive/products/example/consumer"
            destination.parent.mkdir(parents=True)
            shutil.move(agent.directory, destination)
        else:
            path = agent.directory / "object.yaml"
            metadata = yaml.safe_load(path.read_text())
            metadata["targets"] = ["hermes"]
            path.write_text(yaml.safe_dump(metadata))
        skill.content_path.write_text("Changed source.\n")
        self.cli("install", "codex", skill.id, ok=False)
        self.assertEqual(native.read_bytes(), previous)
        self.assertIn(f"codex:{agent.id}", self.cli("status")["bundles"])

    def test_archived_managed_consumer_stops_update_without_deleting_it(self):
        self.assert_invalid_managed_consumer_is_preserved(archive=True)

    def test_incompatible_managed_consumer_stops_update_without_deleting_it(self):
        self.assert_invalid_managed_consumer_is_preserved(archive=False)


if __name__ == "__main__":
    unittest.main()
