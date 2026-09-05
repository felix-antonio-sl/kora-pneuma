import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import yaml

from kora.authoring import create


class CliJourneyTests(unittest.TestCase):
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

    def test_independent_source_to_two_native_targets_update_and_rollback(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            source = base / "source.txt"
            source.write_text("La actividad puede continuar con permiso vigente, salvo revocación.\n")
            body = base / "body.md"
            body.write_text("Conservar permiso, condición y excepción; consultar fuente antes de afirmar.\n")
            root = base / "corpus"
            home = base / "home"
            root.mkdir()
            home.mkdir()
            executable = Path(__file__).resolve().parents[1] / "kora_cli.py"

            def run(*args):
                result = subprocess.run([sys.executable, str(executable), "--root", str(root), *args],
                                        cwd=base, capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                return json.loads(result.stdout)

            run("create", "knowledge", "example", "permission", "--id", "urn:example:kb:permission",
                "--description", "Permiso y excepción", "--body", str(body), "--source", str(source))
            run("create", "skill", "example", "read-permission", "--id", "urn:example:skill:read",
                "--description", r"Interpretar permiso y patrón \d+", "--body", str(body),
                "--requires", "urn:example:kb:permission")
            run("create", "agent", "example", "permission-reader", "--id", "urn:example:agent:reader",
                "--description", "Usa la habilidad y declara límites", "--body", str(body),
                "--requires", "urn:example:skill:read")
            for runtime in ("codex", "hermes"):
                run("install", runtime, "--home", str(home))
            self.assertTrue((home / ".codex/agents/permission-reader.toml").is_file())
            self.assertTrue((home / ".hermes/profiles/permission-reader/SOUL.md").is_file())
            personal = home / ".hermes/profiles/permission-reader/MEMORY.md"
            personal.write_bytes(b"personal memory")
            (root / "products/example/read-permission/content.md").write_text("Updated, with permission and revocation preserved.\n")
            run("install", "hermes", "--home", str(home))
            native = home / ".hermes/profiles/permission-reader/skills/read-permission/SKILL.md"
            self.assertIn("Updated", native.read_text())
            run("rollback", "--home", str(home))
            self.assertNotIn("Updated", native.read_text())
            self.assertEqual(personal.read_bytes(), b"personal memory")
            self.assertEqual(run("status", "--home", str(home))["changes"], [])


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
        selected.content_path.write_text("Selected updated.\n")
        secondary.content_path.write_text("Secondary updated.\n")
        self.cli("install", "codex", selected.id)
        self.assertIn("Secondary updated", (self.home / ".agents/skills/secondary/SKILL.md").read_text())
        self.assertEqual(self.cli("status")["changes"], [])

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
