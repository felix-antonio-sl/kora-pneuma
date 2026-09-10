import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from kora.catalog import File, KoraError, digest
from kora.install import Installer


class InstallerPlanTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="kora-install-plan-")
        self.addCleanup(temporary.cleanup)
        self.home = Path(temporary.name) / "home"
        self.installer = Installer(self.home)
        self.skill = ".agents/skills/example/SKILL.md"

    def test_prepare_is_deterministic_and_does_not_create_installer_state(self):
        files = {self.skill: File(b"one", source={"id": "urn:test:one", "revision": "r1"})}
        first = self.installer.prepare({"codex:example": files}, context={"purpose": "preview"})
        second = self.installer.prepare({"codex:example": files}, context={"purpose": "preview"})

        self.assertEqual(first, second)
        self.assertTrue(first["ok"])
        self.assertEqual(first["bundles"], ["codex:example"])
        self.assertEqual(first["patches"], {})
        self.assertEqual(first["remove"], [])
        self.assertEqual([effect["path"] for effect in first["effects"]], [self.skill])
        self.assertEqual(first["effects"][0]["before"], None)
        self.assertEqual(first["effects"][0]["after"]["sha256"], digest(b"one"))
        self.assertNotIn("data", json.dumps(first))
        self.assertFalse(self.home.exists())

    def test_apply_plan_has_the_preview_effect_paths_and_keeps_source_metadata(self):
        source = {"id": "urn:test:one", "fingerprint": "f1"}
        files = {self.skill: File(b"one", source=source)}
        plan = self.installer.prepare({"codex:example": files})

        result = self.installer.apply({"codex:example": files}, plan=plan)

        self.assertEqual(result["changed"], [effect["path"] for effect in plan["effects"]])
        self.assertEqual(self.installer.receipts()["codex:example"][self.skill]["source"], source)

    def test_source_only_patch_does_not_touch_or_block_a_local_edit(self):
        first = File(b"one", source={"id": "urn:test:one", "fingerprint": "f1"})
        self.installer.apply({"codex:example": {self.skill: first}})
        (self.home / self.skill).write_bytes(b"local edit")
        second = File(b"one", source={"id": "urn:test:one", "fingerprint": "f2"})

        plan = self.installer.prepare({}, patches={"codex:example": {self.skill: second}})
        result = self.installer.apply({}, patches={"codex:example": {self.skill: second}}, plan=plan)

        self.assertTrue(plan["ok"])
        self.assertEqual(plan["effects"], [])
        self.assertEqual(result["changed"], [])
        self.assertEqual((self.home / self.skill).read_bytes(), b"local edit")
        self.assertEqual(self.installer.receipts()["codex:example"][self.skill]["source"]["fingerprint"], "f2")

    def test_sparse_patch_does_not_pull_an_unselected_bundle_into_the_delta(self):
        alpha_path = ".agents/skills/alpha/SKILL.md"
        beta_path = ".agents/skills/beta/SKILL.md"
        shared = ".agents/skills/shared/SKILL.md"
        self.installer.apply({
            "alpha": {
                alpha_path: File(b"alpha-one", source={"id": "alpha", "fingerprint": "a1"}),
                shared: File(b"shared", source={"id": "shared", "fingerprint": "s-alpha"}),
            },
            "beta": {
                beta_path: File(b"beta-one", source={"id": "beta", "fingerprint": "b1"}),
                shared: File(b"shared", source={"id": "shared", "fingerprint": "s-beta"}),
            },
        })
        (self.home / beta_path).write_bytes(b"beta local edit")
        update = File(b"alpha-two", source={"id": "alpha", "fingerprint": "a2"})

        plan = self.installer.prepare({}, patches={"alpha": {alpha_path: update}})
        result = self.installer.apply({}, patches={"alpha": {alpha_path: update}}, plan=plan)

        self.assertEqual(result["changed"], [alpha_path])
        self.assertEqual((self.home / alpha_path).read_bytes(), b"alpha-two")
        self.assertEqual((self.home / beta_path).read_bytes(), b"beta local edit")
        receipts = self.installer.receipts()
        self.assertEqual(receipts["beta"][beta_path]["source"]["fingerprint"], "b1")
        self.assertEqual(receipts["beta"][shared]["source"]["fingerprint"], "s-beta")

    def test_stale_plan_rejects_destination_without_writing_over_it(self):
        files = {self.skill: File(b"one")}
        plan = self.installer.prepare({"codex:example": files})
        path = self.home / self.skill
        path.parent.mkdir(parents=True)
        path.write_bytes(b"foreign")

        with self.assertRaisesRegex(KoraError, "obsoleto"):
            self.installer.apply({"codex:example": files}, plan=plan)
        self.assertEqual(path.read_bytes(), b"foreign")
        self.assertFalse((self.home / ".local/state/kora/installed.json").exists())

    def test_stale_plan_rejects_receipt_after_another_operation(self):
        first = {self.skill: File(b"one")}
        self.installer.apply({"codex:example": first})
        update = {self.skill: File(b"two")}
        plan = self.installer.prepare({"codex:example": update})
        self.installer.apply({"codex:example": {self.skill: File(b"three")}})

        with self.assertRaisesRegex(KoraError, "obsoleto"):
            self.installer.apply({"codex:example": update}, plan=plan)
        self.assertEqual((self.home / self.skill).read_bytes(), b"three")

    def test_validate_callback_runs_before_writes_and_again_for_significant_apply(self):
        source = self.home.parent / "source.txt"
        source.write_bytes(b"source-v1")
        files = {self.skill: File(b"one", source={"path": str(source), "sha256": hashlib.sha256(b"source-v1").hexdigest()})}
        plan = self.installer.prepare({"codex:example": files})
        source.write_bytes(b"source-v2")
        calls = []

        def validate():
            calls.append(True)
            if source.read_bytes() != b"source-v1":
                raise KoraError("La fuente cambió durante la operación")

        with self.assertRaisesRegex(KoraError, "fuente cambió"):
            self.installer.apply({"codex:example": files}, plan=plan, validate=validate)
        self.assertEqual(calls, [True])
        self.assertFalse((self.home / self.skill).exists())
        self.assertFalse((self.home / ".local/state/kora/installed.json").exists())

    def test_modified_legacy_bytecode_is_preserved_on_retirement_and_rollback(self):
        bytecode = ".agents/skills/example/scripts/__pycache__/module.pyc"
        self.installer.apply({"codex:example": {bytecode: File(b"original")}})
        path = self.home / bytecode
        path.write_bytes(b"operator bytecode")
        plan = self.installer.prepare({}, remove=["codex:example"])

        result = self.installer.apply({}, remove=["codex:example"], plan=plan)
        status = self.installer.status()

        self.assertEqual(result["changed"], [bytecode])
        self.assertFalse(path.exists())
        self.assertEqual(len(status["preserved_changes"]), 1)
        report = status["preserved_changes"][0]
        self.assertTrue(report["preserved"])
        self.assertEqual(report["reason"], "caché")
        self.assertEqual((self.home / report["backup"]).read_bytes(), b"operator bytecode")
        self.installer.rollback()
        self.assertEqual(path.read_bytes(), b"operator bytecode")
        self.assertEqual(self.installer.status()["changes"], [{"path": bytecode, "state": "modified"}])

    def test_private_env_residue_stays_a_conflict(self):
        private = ".agents/skills/example/.env"
        self.installer.apply({"codex:example": {private: File(b"original")}})
        (self.home / private).write_bytes(b"operator secret")

        plan = self.installer.prepare({}, remove=["codex:example"])

        self.assertFalse(plan["ok"])
        self.assertEqual(plan["effects"], [])
        self.assertEqual((self.home / private).read_bytes(), b"operator secret")
        with self.assertRaisesRegex(KoraError, "cambio local"):
            self.installer.apply({}, remove=["codex:example"], plan=plan)

    def test_full_patch_and_remove_overlap_is_rejected(self):
        with self.assertRaisesRegex(KoraError, "ambiguas"):
            self.installer.prepare({"a": {self.skill: File(b"one")}},
                                   patches={"a": {self.skill: File(b"two")}})
        with self.assertRaisesRegex(KoraError, "ambiguas"):
            self.installer.prepare({"a": {self.skill: File(b"one")}}, remove=["a"])


if __name__ == "__main__":
    unittest.main()
