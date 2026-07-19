import json
import unittest

from tests.steipete_codex_observer import Accepted
from tests.steipete_codex_observer import all_events
from tests.steipete_codex_observer import CANONICAL_GATE_COMMANDS
from tests.steipete_codex_observer import evaluate_codex_jsonl
from tests.steipete_codex_observer import Event
from tests.steipete_codex_observer import EventKind
from tests.steipete_codex_observer import Gate
from tests.steipete_codex_observer import is_safe
from tests.steipete_codex_observer import ObservationError
from tests.steipete_codex_observer import Phase
from tests.steipete_codex_observer import powerset
from tests.steipete_codex_observer import Rejected
from tests.steipete_codex_observer import REQUIRED_GATES
from tests.steipete_codex_observer import run_trace
from tests.steipete_codex_observer import State
from tests.steipete_codex_observer import step


def jsonl(*records):
    return [json.dumps(record) + "\n" for record in records]


def agent_marker(marker, item_id):
    return {
        "type": "item.completed",
        "item": {
            "id": item_id,
            "type": "agent_message",
            "text": "KORA_OBS " + json.dumps(marker),
        },
    }


def completed_command(gate, item_id, exit_code=0):
    return {
        "type": "item.completed",
        "item": {
            "id": item_id,
            "type": "command_execution",
            "command": (
                "/usr/bin/zsh -lc "
                + repr(CANONICAL_GATE_COMMANDS[gate])
            ),
            "aggregated_output": "salida no proyectada",
            "exit_code": exit_code,
            "status": "completed" if exit_code == 0 else "failed",
        },
    }


def complete_codex_trace():
    records = [
        {"type": "thread.started", "thread_id": "sanitized"},
        {"type": "turn.started"},
        agent_marker({"kind": "estimate"}, "estimate"),
        {
            "type": "item.completed",
            "item": {
                "id": "change",
                "type": "file_change",
                "changes": [{"path": "x", "kind": "update"}],
                "status": "completed",
            },
        },
    ]
    for gate in sorted(
        REQUIRED_GATES - {Gate.FEEL_REVIEW},
        key=lambda item: item.value,
    ):
        records.append(completed_command(gate, gate.value))
    records.extend([
        agent_marker(
            {"kind": "feel-review", "passed": True},
            "feel-review",
        ),
        {"type": "turn.completed", "usage": {}},
    ])
    return records


class TestCasoVerticalSteipeteCodex(unittest.TestCase):

    def test_traza_vertical_de_referencia_cierra(self):
        trace = [
            Event(EventKind.CAPTURE),
            Event(EventKind.ESTIMATE),
            Event(EventKind.CHANGE),
            *[
                Event(EventKind.GATE, gate, True)
                for gate in sorted(
                    REQUIRED_GATES, key=lambda item: item.value)
            ],
            Event(EventKind.CLOSE),
        ]

        result = run_trace(trace)

        self.assertIsInstance(result, Accepted)
        self.assertEqual(Phase.CLOSED, result.state.phase)
        self.assertEqual(REQUIRED_GATES, result.state.passed)

    def test_cierre_sin_evidencia_completa_es_rechazado(self):
        state = State(Phase.VALIDATING, REQUIRED_GATES - {Gate.TESTS})

        result = step(state, Event(EventKind.CLOSE))

        self.assertEqual(Rejected("close-without:tests"), result)

    def test_cambio_invalida_toda_evidencia_previa(self):
        state = State(Phase.VALIDATING, REQUIRED_GATES)

        result = step(state, Event(EventKind.CHANGE))

        self.assertEqual(
            Accepted("evidence-invalidated", State(Phase.DIRTY)),
            result,
        )
        self.assertIsInstance(
            step(result.state, Event(EventKind.CLOSE)),
            Rejected,
        )

    def test_gate_rojo_invalida_toda_evidencia_previa(self):
        state = State(Phase.VALIDATING, REQUIRED_GATES)

        result = step(
            state,
            Event(EventKind.GATE, Gate.TESTS, False),
        )

        self.assertEqual(Accepted("gate-failed", State(Phase.DIRTY)), result)

    def test_step_es_total_y_preserva_el_invariante(self):
        events = all_events()
        total = 0
        safe_pairs = 0
        for phase in Phase:
            for passed in powerset(REQUIRED_GATES):
                state = State(phase, passed)
                for event in events:
                    total += 1
                    result = step(state, event)
                    self.assertIsInstance(result, (Accepted, Rejected))
                    if is_safe(state):
                        safe_pairs += 1
                        if isinstance(result, Accepted):
                            self.assertTrue(is_safe(result.state))

        self.assertEqual(6144, total)
        self.assertEqual(5136, safe_pairs)

    def test_obs_r_cierra_traza_codex_instrumentada(self):
        events, result = evaluate_codex_jsonl(
            jsonl(*complete_codex_trace())
        )

        self.assertEqual(10, len(events))
        self.assertIsInstance(result, Accepted)
        self.assertEqual(Phase.CLOSED, result.state.phase)

    def test_obs_r_rechaza_traza_codex_sin_protocolo(self):
        records = [
            {"type": "thread.started", "thread_id": "sanitized"},
            {"type": "turn.started"},
            {
                "type": "item.completed",
                "item": {
                    "id": "command",
                    "type": "command_execution",
                    "command": (
                        "/usr/bin/zsh -lc "
                        "'python3 -m unittest -v "
                        "tests.test_steipete_vertical'"
                    ),
                    "aggregated_output": "OK",
                    "exit_code": 0,
                    "status": "completed",
                },
            },
            {"type": "turn.completed", "usage": {}},
        ]

        _, result = evaluate_codex_jsonl(jsonl(*records))

        self.assertEqual(Rejected("close-out-of-order"), result)

    def test_obs_r_cambio_tardio_invalida_gates(self):
        records = complete_codex_trace()
        records.insert(-1, {
            "type": "item.completed",
            "item": {
                "id": "late-change",
                "type": "file_change",
                "changes": [{"path": "x", "kind": "update"}],
                "status": "completed",
            },
        })

        _, result = evaluate_codex_jsonl(jsonl(*records))

        self.assertEqual(Rejected("close-out-of-order"), result)

    def test_obs_r_gate_rojo_impide_cierre(self):
        records = complete_codex_trace()
        failed = completed_command(Gate.TESTS, "tests-red", exit_code=1)
        for index, record in enumerate(records):
            item = record.get("item", {})
            if item.get("id") == Gate.TESTS.value:
                records[index] = failed
                break

        _, result = evaluate_codex_jsonl(jsonl(*records))

        self.assertIsInstance(result, Rejected)
        self.assertIn("close-without:", result.violation)

    def test_obs_r_rechaza_gate_no_canonico(self):
        commands = [
            (
                completed_command(Gate.TESTS, "combined")["item"]["command"]
                + " && git diff --check"
            ),
            (
                "/usr/bin/zsh -lc 'PYTHONPATH=/tmp/falso "
                + CANONICAL_GATE_COMMANDS[Gate.TESTS]
                + "'"
            ),
        ]

        for command in commands:
            with self.subTest(command=command):
                record = completed_command(Gate.TESTS, "non-canonical")
                record["item"]["command"] = command
                with self.assertRaisesRegex(
                        ObservationError, "non-canonical-gate-command"):
                    evaluate_codex_jsonl(jsonl(record))

    def test_obs_r_rechaza_marker_malformado(self):
        record = agent_marker({"kind": "estimate"}, "estimate")
        record["item"]["text"] = "KORA_OBS no-json"

        with self.assertRaisesRegex(
                ObservationError, "invalid-marker-json"):
            evaluate_codex_jsonl(jsonl(record))


if __name__ == "__main__":
    unittest.main()
