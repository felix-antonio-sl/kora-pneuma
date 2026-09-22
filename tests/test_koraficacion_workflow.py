"""Pruebas de contrato del workflow integral por su CLI.

Estas pruebas ejercitan la frontera observable del candidato.  No importan
su implementación ni intentan inferir si una revisión es semánticamente
correcta: los juicios se entregan como declaraciones explícitas y la suite
comprueba que la maquinaria conserve bytes, versiones, dependencias y
conflictos.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


REPOSITORY = Path(__file__).resolve().parents[1]
ADMITTED_SCRIPT = (
    REPOSITORY
    / "products/kora/koraficacion-integral/scripts/workflow.py"
)
if "KORA_WORKFLOW_SCRIPT" in os.environ:
    SCRIPT = Path(os.environ["KORA_WORKFLOW_SCRIPT"]).expanduser().resolve()
else:
    SCRIPT = ADMITTED_SCRIPT


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


class WorkflowCliTests(unittest.TestCase):
    """Contrato CLI mínimo del recorrido fuente → candidata → revisión."""

    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.work = self.base / "work"
        self.source = self.base / "source.txt"
        self.body = self.base / "body.md"
        self.source.write_text(
            "El registro debe conservarse durante 30 días. "
            "No puede eliminarse antes de ese plazo.\n",
            encoding="utf-8",
        )

    def run_cli(self, command: str, *args: object, work: Path | None = None,
                ok: bool = True) -> dict | subprocess.CompletedProcess:
        """Ejecuta una operación y decodifica el JSON que imprime la CLI."""

        selected_work = work or self.work
        command_line = [
            sys.executable,
            str(SCRIPT),
            command,
            "--work",
            str(selected_work),
            *(str(value) for value in args),
        ]
        result = subprocess.run(
            command_line,
            cwd=REPOSITORY,
            capture_output=True,
        )
        output = result.stdout.decode("utf-8", errors="replace")
        error = result.stderr.decode("utf-8", errors="replace")
        if ok:
            self.assertEqual(
                result.returncode,
                0,
                f"{command_line!r}\nstdout={output}\nstderr={error}",
            )
        else:
            self.assertNotEqual(
                result.returncode,
                0,
                f"{command_line!r}\nstdout={output}\nstderr={error}",
            )
        if not output.strip():
            return result
        try:
            payload = json.loads(output)
        except json.JSONDecodeError as exc:
            self.fail(f"La CLI no imprimió JSON válido: {output!r}; {exc}")
        self.assertIsInstance(payload, dict, output)
        return payload

    def init_work(self, *, source: Path | None = None, body: Path | None = None,
                  scope: str = "retención y eliminación del registro",
                  resources: list[Path] | None = None,
                  require_independent: bool = False,
                  independent_repairs: bool = False,
                  work: Path | None = None) -> dict:
        source = source or self.source
        body = body or self.body
        args: list[object] = [
            "--source",
            source,
            "--body",
            body,
            "--scope",
            scope,
        ]
        for resource in resources or []:
            args.extend(("--resource", resource))
        if require_independent:
            args.append("--require-independent")
        if independent_repairs:
            args.append("--independent-repairs")
        return self.run_cli("init", *args, work=work)

    def write_candidate(self, text: str, *, name: str = "candidate.txt") -> Path:
        path = self.base / name
        path.write_text(text, encoding="utf-8")
        return path

    def write_review(self, value: dict, *, name: str = "review.json") -> Path:
        path = self.base / name
        path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")
        return path

    def review_payload(self, revision: str, *, result: str = "accepted",
                       isolation: str = "separate_context",
                       authored_target: bool = False,
                       scope: str = "full", coverage: str = "complete",
                       issues: list[str] | None = None,
                       limits: list[str] | None = None,
                       reviewer: str = "reviewer-a", basis: str | None = None,
                       impact: str | None = None) -> dict:
        payload = {
            "revision": revision,
            "reviewer": reviewer,
            "isolation": isolation,
            "authored_target": authored_target,
            "scope": scope,
            "coverage": coverage,
            "result": result,
            "evidence": "Cotejé objeto, plazo, negación y la condición completa.",
            "issues": list(issues or []),
            "limits": list(limits or []),
        }
        if basis is not None:
            payload["basis"] = basis
        if impact is not None:
            payload["impact"] = impact
        return payload

    def submit_review(self, payload: dict, *, name: str = "review.json",
                      work: Path | None = None, ok: bool = True):
        path = self.write_review(payload, name=name)
        return self.run_cli("review", "--file", path, work=work, ok=ok)

    def candidate(self, path: Path, *, base: str | None = None,
                  work: Path | None = None, ok: bool = True):
        args: list[object] = ["--file", path]
        if base is not None:
            args.extend(("--base-revision", base))
        return self.run_cli("candidate", *args, work=work, ok=ok)

    def preview(self, path: Path, *, work: Path | None = None,
                ok: bool = True):
        return self.run_cli("preview", "--file", path, work=work, ok=ok)

    def repair(self, path: Path, base: str, review: dict, *, name: str = "repair-review.json",
               work: Path | None = None, ok: bool = True):
        review_path = self.write_review(review, name=name)
        return self.run_cli(
            "repair",
            "--file",
            path,
            "--base-revision",
            base,
            "--review",
            review_path,
            work=work,
            ok=ok,
        )

    def status(self, *, work: Path | None = None, ok: bool = True):
        return self.run_cli("status", work=work, ok=ok)

    def export(self, *, work: Path | None = None, ok: bool = True):
        return self.run_cli("export", work=work, ok=ok)

    @staticmethod
    def work_snapshot(work: Path) -> dict[str, bytes]:
        """Captura archivos y envelopes sin depender de timestamps."""

        if not work.exists():
            return {}
        return {
            str(path.relative_to(work)): path.read_bytes()
            for path in work.rglob("*")
            if path.is_file()
        }

    def test_simple_document_without_inventory_round_trips_to_export(self):
        """Una fuente breve no exige formularios de inventario intermedios."""

        self.source.write_text(
            "Página 3 de 4.\n"
            "El registro debe conservarse durante 30 días. "
            "No puede eliminarse antes de ese plazo.\n",
            encoding="utf-8",
        )
        initial = self.init_work()
        self.assertEqual(initial["state"], "empty")
        self.assertIsNone(initial["current_revision"])
        self.assertEqual(len(initial["sources"]), 1)

        target = self.write_candidate(
            "El registro debe conservarse durante 30 días; "
            "no puede eliminarse antes de ese plazo.\n"
        )
        before_preview = self.work_snapshot(self.work)
        preview = self.preview(target)
        self.assertTrue({"revision", "body_sha256", "base_revision"}.issubset(preview))
        self.assertEqual(preview["base_revision"], None)
        self.assertEqual(self.work_snapshot(self.work), before_preview)

        candidate_result = self.candidate(target)
        revision = candidate_result["current_revision"]
        self.assertRegex(revision, r"^[0-9a-f]{64}$")
        review = self.review_payload(revision)
        reviewed = self.submit_review(review)
        self.assertEqual(reviewed["state"], "reviewed")
        self.assertTrue(reviewed["independent_review_declared"])
        self.assertEqual(reviewed["review_id"],
                         self.status()["review_id"])

        receipt = self.export()
        self.assertEqual(receipt["publication"], "not_performed")
        self.assertEqual(receipt["current_revision"], revision)
        self.assertEqual(self.body.read_text(encoding="utf-8"), target.read_text(encoding="utf-8"))
        self.assertEqual(receipt["body_sha256"], sha256(target.read_bytes()))

    def test_negative_review_is_preserved_and_exact_repair_installs_target(self):
        self.init_work()
        bad = self.write_candidate("El registro debe conservarse durante 30 días.\n", name="bad.txt")
        bad_result = self.candidate(bad)
        bad_revision = bad_result["current_revision"]
        bad_review = self.review_payload(
            bad_revision,
            result="repair",
            issues=["Falta la prohibición de eliminar antes del plazo."],
        )
        bad_review_result = self.submit_review(bad_review, name="bad-review.json")
        self.assertEqual(bad_review_result["state"], "repair")
        self.assertEqual(bad_review_result["review_id"], self.status()["review_id"])

        good = self.write_candidate(
            "El registro debe conservarse durante 30 días; "
            "no puede eliminarse antes de ese plazo.\n",
            name="good.txt",
        )
        good_preview = self.preview(good)
        self.assertEqual(good_preview["base_revision"], bad_revision)
        good_revision = good_preview["revision"]
        repair_review = self.review_payload(good_revision)
        repaired = self.repair(good, bad_revision, repair_review)
        self.assertEqual(repaired["state"], "reviewed")
        self.assertEqual(repaired["current_revision"], good_revision)
        self.assertEqual(self.body.read_bytes(), good.read_bytes())

        receipt = self.export()
        self.assertEqual([row["revision"] for row in receipt["history"]],
                         [bad_revision, good_revision])
        self.assertEqual(receipt["history"][0]["reviews"][0]["result"], "repair")
        self.assertEqual(receipt["history"][1]["reviews"][0]["result"], "accepted")
        rejected_snapshot = Path(receipt["history"][0]["snapshot"])
        self.assertTrue(rejected_snapshot.is_file())
        self.assertEqual(rejected_snapshot.read_bytes(), bad.read_bytes())

    def test_candidate_requires_current_base_revision(self):
        self.init_work()
        first = self.write_candidate("Versión uno del registro.\n", name="first.txt")
        first_result = self.candidate(first)
        first_revision = first_result["current_revision"]
        self.submit_review(self.review_payload(first_revision), name="first-review.json")
        self.export()

        second = self.write_candidate("Versión dos del registro.\n", name="second.txt")
        before = self.work_snapshot(self.work)
        self.candidate(second, ok=False)
        self.candidate(second, base="0" * 64, ok=False)
        self.assertEqual(self.work_snapshot(self.work), before)
        second_result = self.candidate(second, base=first_revision)
        self.assertNotEqual(second_result["current_revision"], first_revision)

    def test_obsolete_review_and_repair_base_are_rejected_without_mutation(self):
        self.init_work()
        first = self.write_candidate("Versión uno.\n", name="v1.txt")
        first_result = self.candidate(first)
        first_revision = first_result["current_revision"]
        first_review = self.review_payload(first_revision)
        first_review_result = self.submit_review(first_review, name="v1-review.json")
        first_review_id = first_review_result["review_id"]
        self.export()

        second = self.write_candidate("Versión dos.\n", name="v2.txt")
        second_result = self.candidate(second, base=first_revision)
        second_revision = second_result["current_revision"]
        before_stale_review = self.work_snapshot(self.work)
        self.submit_review(first_review, name="stale-review.json", ok=False)
        self.assertEqual(self.work_snapshot(self.work), before_stale_review)

        repair_target = self.write_candidate("Versión dos corregida.\n", name="v2-repair.txt")
        repair_preview = self.preview(repair_target)
        repair_review = self.review_payload(repair_preview["revision"])
        before_wrong_base = self.work_snapshot(self.work)
        self.repair(repair_target, first_revision, repair_review, name="wrong-base.json", ok=False)
        self.assertEqual(self.work_snapshot(self.work), before_wrong_base)

        # También debe quedar obsoleta la revisión si el objetivo que se
        # presentó al revisor ya no coincide con los bytes que se repararán.
        repair_target.write_text("Versión dos con otro cambio.\n", encoding="utf-8")
        before_changed_target = self.work_snapshot(self.work)
        self.repair(repair_target, second_revision, repair_review,
                    name="changed-target.json", ok=False)
        self.assertEqual(self.work_snapshot(self.work), before_changed_target)
        self.assertEqual(self.status()["current_revision"], second_revision)
        self.assertEqual(first_review_id, first_review_result["review_id"])

    def test_resource_change_invalidates_export_and_preserves_body(self):
        resource = self.base / "resource.bin"
        resource.write_bytes(b"resource-v1\x00\xff")
        self.init_work(resources=[resource])
        target = self.write_candidate("Candidata con recurso.\n")
        candidate_result = self.candidate(target)
        revision = candidate_result["current_revision"]
        self.submit_review(self.review_payload(revision))
        body_before = self.body.read_bytes()
        state_before = self.work_snapshot(self.work)

        resource.write_bytes(b"resource-v2\x00\xff")
        self.export(ok=False)
        self.assertEqual(self.body.read_bytes(), body_before)
        self.assertEqual(self.work_snapshot(self.work), state_before)

        resource.write_bytes(b"resource-v1\x00\xff")
        receipt = self.export()
        self.assertEqual(receipt["current_revision"], revision)

    def test_body_external_edit_is_never_overwritten(self):
        self.body.write_text("Base administrada antes de la candidata.\n", encoding="utf-8")
        self.init_work()
        target = self.write_candidate("Candidata revisada.\n")
        revision = self.candidate(target)["current_revision"]
        self.submit_review(self.review_payload(revision))
        self.export()

        external = "Edición ajena conservada.\n".encode("utf-8")
        self.body.write_bytes(external)
        before = self.work_snapshot(self.work)
        self.export(ok=False)
        self.assertEqual(self.body.read_bytes(), external)
        self.assertEqual(self.work_snapshot(self.work), before)

    def test_author_context_does_not_satisfy_required_independence(self):
        self.init_work(require_independent=True)
        target = self.write_candidate("Candidata que requiere lectura separada.\n")
        revision = self.candidate(target)["current_revision"]
        same_context = self.review_payload(revision, isolation="author_context")
        limited = self.submit_review(same_context)
        self.assertEqual(limited["state"], "limited")
        self.assertFalse(limited["independent_review_declared"])
        self.export(ok=False)

        separate = self.submit_review(
            self.review_payload(revision, isolation="separate_context"),
            name="separate-review.json",
        )
        self.assertEqual(separate["state"], "reviewed")
        self.assertTrue(separate["independent_review_declared"])
        self.export()

    def test_authored_target_basis_is_allowed_but_independent_repairs_forbid_it(self):
        def run_case(work: Path, *, strict: bool) -> tuple[dict, dict, str]:
            self.init_work(work=work, require_independent=True,
                           independent_repairs=strict)
            first = self.write_candidate("Primera versión autónoma.\n", name=f"{work.name}-first.txt")
            first_revision = self.candidate(first, work=work)["current_revision"]
            first_review_result = self.submit_review(
                self.review_payload(first_revision, reviewer=f"{work.name}-reviewer"),
                name=f"{work.name}-first-review.json",
                work=work,
            )
            self.export(work=work)
            second = self.write_candidate("Segunda versión propuesta por el autor.\n",
                                          name=f"{work.name}-second.txt")
            second_revision = self.candidate(second, base=first_revision, work=work)["current_revision"]
            authored = self.review_payload(
                second_revision,
                isolation="separate_context",
                authored_target=True,
                scope="changes",
                basis=first_review_result["review_id"],
                impact="Se cotejó sólo el cambio y sus dependencias con la versión padre.",
                reviewer=f"{work.name}-reviewer",
            )
            result = self.submit_review(authored, name=f"{work.name}-authored.json", work=work)
            return result, authored, second_revision

        permitted, _, permitted_revision = run_case(self.base / "permitted", strict=False)
        self.assertEqual(permitted["state"], "reviewed")
        self.assertFalse(permitted["independent_review_declared"])
        self.assertTrue(permitted["review_chain_satisfies_policy"])
        self.assertEqual(permitted["current_revision"], permitted_revision)
        self.export(work=self.base / "permitted")

        strict, _, strict_revision = run_case(self.base / "strict", strict=True)
        self.assertEqual(strict["state"], "limited")
        self.assertFalse(strict["independent_review_declared"])
        self.assertEqual(strict["current_revision"], strict_revision)
        self.export(work=self.base / "strict", ok=False)

    def test_binary_source_snapshot_survives_external_change_and_detects_tampering(self):
        binary = self.base / "source.bin"
        original = b"cabecera\x00\xff\x10contenido\n"
        binary.write_bytes(original)
        initialized = self.init_work(source=binary)
        source_entry = initialized["sources"][0]
        snapshot = Path(source_entry["path"])
        self.assertEqual(source_entry["sha256"], sha256(original))
        self.assertEqual(snapshot.read_bytes(), original)

        binary.write_bytes(b"fuente externa reemplazada\n")
        after_external_change = self.status()
        self.assertEqual(after_external_change["sources"][0]["sha256"], sha256(original))
        self.assertEqual(snapshot.read_bytes(), original)

        snapshot.write_bytes(b"snapshot alterado\x00")
        self.status(ok=False)

    def test_replaying_init_candidate_review_and_export_is_idempotent(self):
        first_init = self.init_work()
        first_state = self.work_snapshot(self.work)
        replay_init = self.init_work()
        self.assertTrue(replay_init.get("reused"))
        self.assertEqual(self.work_snapshot(self.work), first_state)

        target = self.write_candidate("Candidata repetible.\n")
        first_candidate = self.candidate(target)
        revision = first_candidate["current_revision"]
        candidate_state = self.work_snapshot(self.work)
        replay_candidate = self.candidate(target)
        self.assertTrue(replay_candidate.get("reused"))
        self.assertEqual(self.work_snapshot(self.work), candidate_state)

        review_path = self.write_review(self.review_payload(revision), name="replay-review.json")
        first_review = self.run_cli("review", "--file", review_path)
        review_state = self.work_snapshot(self.work)
        replay_review = self.run_cli("review", "--file", review_path)
        self.assertTrue(replay_review.get("reused"))
        self.assertEqual(self.work_snapshot(self.work), review_state)

        first_export = self.export()
        second_export = self.export()
        self.assertEqual(first_export, second_export)
        self.assertEqual(self.work_snapshot(self.work), review_state)
        self.assertEqual(first_init["state"], "empty")
        self.assertEqual(first_review["state"], "reviewed")

    def test_next_exposes_snapshot_paths_and_the_required_next_action(self):
        self.init_work()
        initial_next = self.run_cli("next")
        self.assertEqual(initial_next["next_action"], "candidate")
        self.assertIsNone(initial_next["candidate_snapshot"])
        self.assertTrue(Path(initial_next["sources"][0]["path"]).is_file())

        target = self.write_candidate("Candidata para next.\n")
        revision = self.candidate(target)["current_revision"]
        pending_next = self.run_cli("next")
        self.assertEqual(pending_next["next_action"], "review_or_repair")
        self.assertTrue(Path(pending_next["candidate_snapshot"]).is_file())
        self.assertEqual(pending_next["reviews"], [])

        self.submit_review(self.review_payload(revision))
        ready_next = self.run_cli("next")
        self.assertEqual(ready_next["next_action"], "export")
        self.assertEqual(ready_next["reviews"][-1]["revision"], revision)

    def test_export_requires_review_and_rejects_open_or_incomplete_judgment(self):
        self.init_work()
        target = self.write_candidate("Candidata con revisión pendiente.\n")
        revision = self.candidate(target)["current_revision"]
        self.export(ok=False)
        before = self.work_snapshot(self.work)

        self.submit_review(
            self.review_payload(revision, issues=["Se detectó una diferencia."]),
            name="accepted-with-issues.json",
            ok=False,
        )
        self.assertEqual(self.work_snapshot(self.work), before)
        self.submit_review(
            self.review_payload(revision, coverage="incomplete"),
            name="accepted-incomplete.json",
            ok=False,
        )
        self.assertEqual(self.work_snapshot(self.work), before)

        repair = self.submit_review(
            self.review_payload(
                revision,
                result="repair",
                issues=["Falta cotejar la relación entre condición y consecuencia."],
            ),
            name="repair.json",
        )
        self.assertEqual(repair["state"], "repair")
        after_repair = self.work_snapshot(self.work)
        self.export(ok=False)
        self.assertEqual(self.work_snapshot(self.work), after_repair)

    def test_changes_review_requires_parent_basis_and_material_impact(self):
        self.init_work()
        first = self.write_candidate("Versión padre.\n", name="basis-parent.txt")
        first_revision = self.candidate(first)["current_revision"]
        first_review_result = self.submit_review(self.review_payload(first_revision), name="basis-review.json")
        self.export()

        second = self.write_candidate("Versión hija.\n", name="basis-child.txt")
        second_revision = self.candidate(second, base=first_revision)["current_revision"]
        before = self.work_snapshot(self.work)
        self.submit_review(
            self.review_payload(second_revision, scope="changes"),
            name="missing-basis.json",
            ok=False,
        )
        self.assertEqual(self.work_snapshot(self.work), before)
        valid = self.review_payload(
            second_revision,
            scope="changes",
            basis=first_review_result["review_id"],
            impact="Cotejé la relación modificada y sus efectos sobre el alcance.",
        )
        accepted = self.submit_review(valid, name="valid-changes.json")
        self.assertEqual(accepted["state"], "reviewed")
        self.export()

    def test_metadata_numbers_are_excluded_without_forcing_literal_support(self):
        self.source.write_text(
            "Página 12 de 40; OCR ejecutado.\n"
            "El lote contiene 3 unidades y se conserva por 30 días.\n",
            encoding="utf-8",
        )
        self.init_work(scope="contenido sustantivo del lote")
        target = self.write_candidate(
            "El lote contiene 3 unidades y se conserva por 30 días.\n",
            name="metadata-free.txt",
        )
        revision = self.candidate(target)["current_revision"]
        self.submit_review(self.review_payload(revision), name="metadata-review.json")
        receipt = self.export()
        artifact = self.body.read_text(encoding="utf-8")
        self.assertIn("3 unidades", artifact)
        self.assertIn("30 días", artifact)
        self.assertNotIn("Página 12", artifact)
        self.assertNotIn("OCR", artifact)
        self.assertEqual(receipt["body_sha256"], sha256(target.read_bytes()))

    def test_recover_after_a_completed_transition_is_safe_and_replayable(self):
        self.init_work()
        target = self.write_candidate("Candidata recuperable.\n")
        revision = self.candidate(target)["current_revision"]
        self.submit_review(self.review_payload(revision))
        self.export()
        body_before = self.body.read_bytes()
        files_before = self.work_snapshot(self.work)

        recovered = self.run_cli("recover")
        self.assertEqual(recovered["state"], "reviewed")
        self.assertEqual(recovered["current_revision"], revision)
        self.assertEqual(self.body.read_bytes(), body_before)
        self.assertEqual(self.work_snapshot(self.work), files_before)


if __name__ == "__main__":
    unittest.main()
