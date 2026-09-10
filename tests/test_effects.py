import hashlib
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from kora.authoring import create


class EffectsCliTests(unittest.TestCase):
    """M3 synthetic checks for focal effects, source state, and ownership."""

    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="kora-effects-")
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.root = self.base / "corpus"
        self.home = self.base / "home"
        self.executable = Path(__file__).resolve().parents[1] / "kora_cli.py"

    def product(self, kind, name, *, namespace="example", identifier=None,
                requires=(), targets=None, body=None):
        if targets is None:
            targets = () if kind == "knowledge" else ("codex", "hermes")
        identifier = identifier or f"urn:{namespace}:{kind}:{name}"
        body_path = self.base / f"{namespace}-{kind}-{name}-body.md"
        body_path.write_text(body or f"{name} source version one.\n", encoding="utf-8")
        return create(self.root, kind, namespace, name, identifier,
                      f"Use {name}", body_path, targets=targets, requires=requires)

    def cli(self, *args, ok=True):
        command = [sys.executable, str(self.executable), "--root", str(self.root), *args]
        if args and args[0] in ("install", "remove", "status", "rollback", "recover"):
            command += ["--home", str(self.home)]
        result = subprocess.run(command, cwd=self.base, capture_output=True, text=True)
        if ok:
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout)
        if result.stdout.strip():
            return json.loads(result.stdout)
        self.fail(f"La CLI no entregó JSON; stderr: {result.stderr.strip()}")

    def state(self):
        return json.loads((self.home / ".local/state/kora/installed.json").read_text())

    def snapshot_home(self):
        if not self.home.exists():
            return None
        result = []
        for path in sorted(self.home.rglob("*")):
            relative = path.relative_to(self.home).as_posix()
            mode = path.lstat().st_mode
            if stat.S_ISLNK(mode):
                result.append(("link", relative, os.readlink(path)))
            elif stat.S_ISREG(mode):
                result.append(("file", relative, stat.S_IMODE(mode), path.read_bytes()))
            elif stat.S_ISDIR(mode):
                result.append(("dir", relative, stat.S_IMODE(mode)))
        return result

    def assert_plan_shape(self, plan):
        self.assertTrue({
            "ok", "effects", "ownership", "conflicts", "preconditions",
            "context", "plan_sha256",
        }.issubset(plan))
        self.assertRegex(plan["plan_sha256"], r"^[0-9a-f]{64}$")
        body = {key: value for key, value in plan.items() if key != "plan_sha256"}
        canonical = json.dumps(body, ensure_ascii=False, sort_keys=True,
                               separators=(",", ":")).encode("utf-8")
        self.assertEqual(plan["plan_sha256"], hashlib.sha256(canonical).hexdigest())
        self.assertIsInstance(plan["effects"], list)
        for effect in plan["effects"]:
            self.assertEqual({"path", "action", "before", "after"}, set(effect))
            self.assertIsInstance(effect["path"], str)

    def test_install_and_remove_dry_run_are_side_effect_free_and_share_effect_shape(self):
        skill = self.product("skill", "preview")

        install_plan = self.cli("install", "codex", skill.id, "--dry-run")
        self.assertTrue(install_plan["ok"])
        self.assert_plan_shape(install_plan)
        self.assertIsNone(self.snapshot_home())
        self.assertFalse((self.home / ".local/state/kora/lock").exists())

        applied = self.cli("install", "codex", skill.id)
        planned_paths = {effect["path"] for effect in install_plan["effects"]}
        if "changed" in applied:
            self.assertEqual(set(applied["changed"]), planned_paths)

        before_remove = self.snapshot_home()
        remove_plan = self.cli("remove", "codex", skill.id, "--dry-run")
        self.assertTrue(remove_plan["ok"])
        self.assert_plan_shape(remove_plan)
        self.assertTrue(any(effect["path"] == ".agents/skills/preview/SKILL.md"
                            for effect in remove_plan["effects"]))
        self.assertEqual(self.snapshot_home(), before_remove)

        self.cli("remove", "codex", skill.id)
        self.assertFalse((self.home / ".agents/skills/preview/SKILL.md").exists())

    def test_focal_preview_and_apply_do_not_expand_through_shared_knowledge(self):
        knowledge = self.product("knowledge", "shared-knowledge")
        alpha = self.product("skill", "alpha", requires=(knowledge.id,), targets=("codex",))
        beta = self.product("skill", "beta", requires=(knowledge.id,), targets=("codex",))
        self.cli("install", "codex", alpha.id, beta.id)

        beta_path = self.home / ".agents/skills/beta/SKILL.md"
        beta_path.write_bytes(b"beta local work\n")
        beta_path.chmod(0o600)
        beta_bytes = beta_path.read_bytes()
        beta_mode = stat.S_IMODE(beta_path.stat().st_mode)
        state_before = self.state()
        alpha.content_path.write_text("alpha source version two.\n", encoding="utf-8")
        home_before = self.snapshot_home()

        plan = self.cli("install", "codex", alpha.id, "--dry-run")
        self.assertTrue(plan["ok"])
        self.assert_plan_shape(plan)
        self.assertNotIn(beta.id, json.dumps(plan["ownership"], ensure_ascii=False))
        if "bundles" in plan:
            self.assertNotIn(beta.id, json.dumps(plan["bundles"], ensure_ascii=False))
        self.assertFalse(any("/beta/" in effect["path"] or effect["path"].endswith("/beta/SKILL.md")
                             for effect in plan["effects"]))
        self.assertEqual(self.snapshot_home(), home_before)

        self.cli("install", "codex", alpha.id)
        self.assertIn("alpha source version two",
                      (self.home / ".agents/skills/alpha/SKILL.md").read_text())
        self.assertEqual(beta_path.read_bytes(), beta_bytes)
        self.assertEqual(stat.S_IMODE(beta_path.stat().st_mode), beta_mode)
        self.assertEqual(self.state()[f"codex:{beta.id}"], state_before[f"codex:{beta.id}"])

    def run_shared_update(self, focal):
        gamma = self.product("skill", "gamma", targets=("codex",))
        secondary = self.product("skill", "secondary", targets=("codex",))
        alpha = self.product("skill", "alpha", requires=(gamma.id,), targets=("codex",))
        beta = self.product("skill", "beta", requires=(gamma.id, secondary.id), targets=("codex",))
        self.cli("install", "codex", alpha.id, beta.id)

        alpha_path = self.home / ".agents/skills/alpha/SKILL.md"
        beta_path = self.home / ".agents/skills/beta/SKILL.md"
        gamma_path = self.home / ".agents/skills/gamma/SKILL.md"
        secondary_path = self.home / ".agents/skills/secondary/SKILL.md"
        beta_path.write_bytes(b"beta own local body\n")
        beta_path.chmod(0o600)
        beta_bytes = beta_path.read_bytes()
        beta_mode = stat.S_IMODE(beta_path.stat().st_mode)
        secondary_bytes = secondary_path.read_bytes()
        secondary_mode = stat.S_IMODE(secondary_path.stat().st_mode)
        state_before = self.state()

        gamma.content_path.write_text("gamma source version two.\n", encoding="utf-8")
        alpha.content_path.write_text("alpha source version two.\n", encoding="utf-8")
        beta.content_path.write_text("beta source version two.\n", encoding="utf-8")
        secondary.content_path.write_text("secondary source version two.\n", encoding="utf-8")
        focal_product = alpha if focal == "alpha" else gamma
        self.cli("install", "codex", focal_product.id)

        self.assertIn("gamma source version two", gamma_path.read_text())
        self.assertEqual(beta_path.read_bytes(), beta_bytes)
        self.assertEqual(stat.S_IMODE(beta_path.stat().st_mode), beta_mode)
        self.assertEqual(secondary_path.read_bytes(), secondary_bytes)
        self.assertEqual(stat.S_IMODE(secondary_path.stat().st_mode), secondary_mode)

        state_after = self.state()
        alpha_key = f"codex:{alpha.id}"
        beta_key = f"codex:{beta.id}"
        gamma_relative = ".agents/skills/gamma/SKILL.md"
        secondary_relative = ".agents/skills/secondary/SKILL.md"
        beta_relative = ".agents/skills/beta/SKILL.md"
        self.assertNotEqual(state_after[alpha_key][gamma_relative], state_before[alpha_key][gamma_relative])
        self.assertNotEqual(state_after[beta_key][gamma_relative], state_before[beta_key][gamma_relative])
        self.assertEqual(state_after[beta_key][beta_relative], state_before[beta_key][beta_relative])
        self.assertEqual(state_after[beta_key][secondary_relative], state_before[beta_key][secondary_relative])
        if focal == "alpha":
            self.assertIn("alpha source version two", alpha_path.read_text())
            self.assertNotEqual(state_after[alpha_key][str(alpha_path.relative_to(self.home))],
                                state_before[alpha_key][str(alpha_path.relative_to(self.home))])
        else:
            self.assertNotIn("alpha source version two", alpha_path.read_text())
            self.assertEqual(state_after[alpha_key][str(alpha_path.relative_to(self.home))],
                             state_before[alpha_key][str(alpha_path.relative_to(self.home))])

    def test_shared_skill_update_from_alpha_patches_only_shared_receipts(self):
        gamma = self.product("skill", "gamma", targets=("codex",))
        secondary = self.product("skill", "secondary", targets=("codex",))
        alpha = self.product("skill", "alpha", requires=(gamma.id,), targets=("codex",))
        beta = self.product("skill", "beta", requires=(gamma.id, secondary.id), targets=("codex",))
        self.cli("install", "codex", alpha.id, beta.id)
        beta_path = self.home / ".agents/skills/beta/SKILL.md"
        gamma_path = self.home / ".agents/skills/gamma/SKILL.md"
        secondary_path = self.home / ".agents/skills/secondary/SKILL.md"
        alpha_path = self.home / ".agents/skills/alpha/SKILL.md"
        beta_path.write_bytes(b"beta own local body\n")
        beta_path.chmod(0o600)
        beta_bytes = beta_path.read_bytes()
        beta_mode = stat.S_IMODE(beta_path.stat().st_mode)
        secondary_bytes = secondary_path.read_bytes()
        state_before = self.state()
        gamma.content_path.write_text("gamma source version two.\n", encoding="utf-8")
        alpha.content_path.write_text("alpha source version two.\n", encoding="utf-8")
        beta.content_path.write_text("beta source version two.\n", encoding="utf-8")
        secondary.content_path.write_text("secondary source version two.\n", encoding="utf-8")

        self.cli("install", "codex", alpha.id)
        self.assertIn("alpha source version two", alpha_path.read_text())
        self.assertIn("gamma source version two", gamma_path.read_text())
        self.assertEqual(beta_path.read_bytes(), beta_bytes)
        self.assertEqual(stat.S_IMODE(beta_path.stat().st_mode), beta_mode)
        self.assertEqual(secondary_path.read_bytes(), secondary_bytes)
        state_after = self.state()
        beta_key = f"codex:{beta.id}"
        self.assertEqual(state_after[beta_key][".agents/skills/beta/SKILL.md"],
                         state_before[beta_key][".agents/skills/beta/SKILL.md"])
        self.assertEqual(state_after[beta_key][".agents/skills/secondary/SKILL.md"],
                         state_before[beta_key][".agents/skills/secondary/SKILL.md"])
        self.assertNotEqual(state_after[beta_key][".agents/skills/gamma/SKILL.md"],
                            state_before[beta_key][".agents/skills/gamma/SKILL.md"])

    def test_shared_skill_update_from_gamma_leaves_consumer_sources_pending(self):
        self.run_shared_update("gamma")

    def test_profile_selection_updates_only_attributable_instances(self):
        skill = self.product("skill", "same-name", targets=("hermes",))
        foreign = self.product("skill", "same-name", namespace="foreign",
                               identifier="urn:foreign:skill:same-name", targets=("hermes",))
        self.cli("install", "hermes", skill.id, "--profile", "dev")
        self.cli("install", "hermes", skill.id, "--profile", "urgencia")
        self.cli("install", "hermes", skill.id)
        self.cli("install", "hermes", foreign.id, "--profile", "foreign")

        unmanaged = self.home / ".hermes/profiles/unmanaged/skills/same-name/SKILL.md"
        unmanaged.parent.mkdir(parents=True)
        unmanaged.write_bytes(b"unmanaged same-name copy\n")
        managed_paths = {
            "dev": self.home / ".hermes/profiles/dev/skills/same-name/SKILL.md",
            "urgencia": self.home / ".hermes/profiles/urgencia/skills/same-name/SKILL.md",
            "root": self.home / ".hermes/skills/same-name/SKILL.md",
            "foreign": self.home / ".hermes/profiles/foreign/skills/same-name/SKILL.md",
        }
        before = {name: path.read_bytes() for name, path in managed_paths.items()}
        unmanaged_before = unmanaged.read_bytes()
        skill.content_path.write_text("same-name source version two.\n", encoding="utf-8")

        self.cli("install", "hermes", skill.id, "--profile", "dev")
        self.assertIn("version two", managed_paths["dev"].read_text())
        for name in ("urgencia", "root", "foreign"):
            self.assertEqual(managed_paths[name].read_bytes(), before[name])
        self.assertEqual(unmanaged.read_bytes(), unmanaged_before)

        self.cli("install", "hermes", skill.id)
        for name in ("dev", "urgencia", "root"):
            self.assertIn("version two", managed_paths[name].read_text())
        self.assertEqual(managed_paths["foreign"].read_bytes(), before["foreign"])
        self.assertEqual(unmanaged.read_bytes(), unmanaged_before)
        comparison = self.cli("status", "--compare-source", "--target", "hermes",
                              "--id", skill.id, "--profile", "dev")
        self.assertTrue(comparison["source_comparison"])
        self.assertTrue(all(item["profile"] == "dev" for item in comparison["source_comparison"]))

    def test_status_profile_includes_its_agent_even_if_source_disappeared(self):
        agent = self.product("agent", "profile-agent", targets=("hermes",))
        self.cli("install", "hermes", agent.id)
        for expected in ("current", "absent"):
            if expected == "absent":
                shutil.rmtree(agent.directory)
            status = self.cli("status", "--compare-source", "--target", "hermes",
                              "--profile", "profile-agent")
            rows = status["source_comparison"]
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["id"], agent.id)
            self.assertEqual(rows[0]["profile"], "profile-agent")
            self.assertEqual(rows[0]["source_state"], expected)

    def test_status_compare_keeps_source_and_native_planes_and_respects_focal_ids(self):
        alpha = self.product("skill", "alpha", targets=("codex",))
        beta = self.product("skill", "beta", targets=("codex",))
        self.cli("install", "codex", alpha.id, beta.id)
        beta.content_path.write_text("beta source version two.\n", encoding="utf-8")

        focal = self.cli("status", "--compare-source", "--target", "codex", "--id", alpha.id)
        self.assertEqual({item["id"] for item in focal["source_comparison"]}, {alpha.id})
        self.assertEqual(focal["source_comparison"][0]["source_state"], "current")
        self.assertEqual(focal["source_comparison"][0]["load_evidence"], "not_observed")

        alpha.content_path.write_text("alpha source version two.\n", encoding="utf-8")
        alpha_native = self.home / ".agents/skills/alpha/SKILL.md"
        alpha_native.write_bytes(b"alpha local native edit\n")
        status = self.cli("status", "--compare-source", "--target", "codex", "--id", alpha.id)
        entry = status["source_comparison"][0]
        self.assertEqual(entry["source_state"], "changed")
        self.assertIn("dependency_state", entry)
        self.assertTrue(any(change.get("path") == ".agents/skills/alpha/SKILL.md"
                            for change in entry["native_changes"]))
        self.assertEqual(entry["load_evidence"], "not_observed")

    def test_status_compare_distinguishes_retired_and_absent_sources(self):
        retired = self.product("skill", "retired", targets=("codex",))
        absent = self.product("skill", "absent", targets=("codex",))
        self.cli("install", "codex", retired.id, absent.id)
        destination = self.root / "archive/products/example/retired"
        destination.parent.mkdir(parents=True)
        shutil.move(retired.directory, destination)
        shutil.rmtree(absent.directory)

        status = self.cli("status", "--compare-source", "--target", "codex",
                          "--id", retired.id, "--id", absent.id)
        states = {item["id"]: item["source_state"] for item in status["source_comparison"]}
        self.assertEqual(states[retired.id], "retired")
        self.assertEqual(states[absent.id], "absent")

    def test_dry_run_conflict_reports_no_effects_and_preserves_local_work(self):
        skill = self.product("skill", "conflicted", targets=("codex",))
        self.cli("install", "codex", skill.id)
        native = self.home / ".agents/skills/conflicted/SKILL.md"
        native.write_bytes(b"local work\n")
        native.chmod(0o600)
        skill.content_path.write_text("conflicted source version two.\n", encoding="utf-8")
        before = self.snapshot_home()

        plan = self.cli("install", "codex", skill.id, "--dry-run", ok=False)
        self.assert_plan_shape(plan)
        self.assertFalse(plan["ok"])
        self.assertTrue(plan["conflicts"])
        self.assertEqual(plan["effects"], [])
        self.assertEqual(self.snapshot_home(), before)


if __name__ == "__main__":
    unittest.main()
