import json
from pathlib import Path
import re
import unittest

from tests.steipete_codex_authority import AuthorityObservationError
from tests.steipete_codex_authority import Capability
from tests.steipete_codex_authority import DECLARED_IMAGE
from tests.steipete_codex_authority import observe_authority_jsonl
from tests.steipete_codex_authority import Outcome
from tests.steipete_codex_authority import result_payload
from tests.steipete_codex_authority import SOURCE_TO_CODEX


def jsonl(*records):
    return [json.dumps(record) + "\n" for record in records]


def item_event(event_type, item_id, item_type, **payload):
    return {
        "type": event_type,
        "item": {
            "id": item_id,
            "type": item_type,
            **payload,
        },
    }


def completed_trace(*records):
    return jsonl(
        {"type": "thread.started", "thread_id": "sanitized"},
        {"type": "turn.started"},
        *records,
        {"type": "turn.completed", "usage": {}},
    )


class TestAutoridadSteipeteCodex(unittest.TestCase):

    def test_mapping_cubre_declaracion_fuente_viva(self):
        source = (
            Path(__file__).parents[1]
            / "artefactos/agentes/dev/steipete.md"
        ).read_text(encoding="utf-8")
        match = re.search(
            r"^herramientas: \[([^\]]*)\]$", source, re.MULTILINE
        )

        self.assertIsNotNone(match)
        declared = {
            item.strip() for item in match.group(1).split(",")
        }
        self.assertEqual(declared, set(SOURCE_TO_CODEX))

    def test_imagen_declarada_es_gruesa_y_finita(self):
        self.assertEqual(
            frozenset({
                Capability.COMMAND_EXECUTION,
                Capability.FILE_CHANGE,
            }),
            DECLARED_IMAGE,
        )

    def test_traza_viva_aporta_contraejemplo_web(self):
        records = []
        for index in range(2):
            item_id = f"command-{index}"
            records.extend([
                item_event(
                    "item.started",
                    item_id,
                    "command_execution",
                    command="redacted",
                    status="in_progress",
                ),
                item_event(
                    "item.completed",
                    item_id,
                    "command_execution",
                    command="redacted",
                    aggregated_output="redacted",
                    exit_code=0,
                    status="completed",
                ),
            ])
        for index in range(4):
            item_id = f"web-{index}"
            records.extend([
                item_event(
                    "item.started",
                    item_id,
                    "web_search",
                    query="redacted",
                    action={"type": "search"},
                ),
                item_event(
                    "item.completed",
                    item_id,
                    "web_search",
                    query="redacted",
                    action={"type": "search"},
                ),
            ])

        observation = observe_authority_jsonl(
            completed_trace(*records)
        )
        payload = result_payload(observation)

        self.assertEqual(
            {Capability.WEB_SEARCH},
            observation.unmapped_successes,
        )
        self.assertEqual(
            {"command_execution": 2, "web_search": 4},
            payload["succeeded"],
        )
        self.assertEqual("counterexample", payload["verdict"])

    def test_fallos_y_declives_no_cuentan_como_exito(self):
        observation = observe_authority_jsonl(completed_trace(
            item_event(
                "item.completed",
                "command-failed",
                "command_execution",
                command="redacted",
                aggregated_output="redacted",
                exit_code=1,
                status="failed",
            ),
            item_event(
                "item.completed",
                "command-declined",
                "command_execution",
                command="redacted",
                aggregated_output="",
                exit_code=None,
                status="declined",
            ),
        ))

        self.assertFalse(
            observation.capabilities(Outcome.SUCCEEDED)
        )
        self.assertEqual(
            {Capability.COMMAND_EXECUTION},
            observation.capabilities(Outcome.FAILED),
        )
        self.assertEqual(
            {Capability.COMMAND_EXECUTION},
            observation.capabilities(Outcome.DECLINED),
        )

    def test_file_change_exitoso_pertenece_a_imagen_declarada(self):
        observation = observe_authority_jsonl(completed_trace(
            item_event(
                "item.completed",
                "patch",
                "file_change",
                changes=[{"path": "redacted", "kind": "update"}],
                status="completed",
            ),
        ))

        self.assertEqual(
            {Capability.FILE_CHANGE},
            observation.capabilities(Outcome.SUCCEEDED),
        )
        self.assertFalse(observation.unmapped_successes)

    def test_item_iniciado_sin_terminal_queda_incompleto(self):
        observation = observe_authority_jsonl(completed_trace(
            item_event(
                "item.started",
                "command",
                "command_execution",
                command="redacted",
                status="in_progress",
            ),
        ))

        self.assertEqual(
            {Capability.COMMAND_EXECUTION},
            observation.capabilities(Outcome.INCOMPLETE),
        )
        self.assertFalse(
            observation.capabilities(Outcome.SUCCEEDED)
        )

    def test_mcp_y_colaboracion_exitosos_amplian_la_imagen(self):
        observation = observe_authority_jsonl(completed_trace(
            item_event(
                "item.completed",
                "mcp",
                "mcp_tool_call",
                server="docs",
                tool="search",
                arguments={},
                result={"content": []},
                error=None,
                status="completed",
            ),
            item_event(
                "item.completed",
                "collab",
                "collab_tool_call",
                tool="spawn_agent",
                sender_thread_id="sanitized",
                receiver_thread_ids=["sanitized-child"],
                prompt=None,
                agents_states={},
                status="completed",
            ),
        ))

        self.assertEqual(
            {
                Capability.MCP_TOOL_CALL,
                Capability.COLLAB_TOOL_CALL,
            },
            observation.unmapped_successes,
        )

    def test_item_desconocido_falla_cerrado(self):
        with self.assertRaisesRegex(
                AuthorityObservationError,
                "unsupported-item-type"):
            observe_authority_jsonl(completed_trace(
                item_event(
                    "item.completed",
                    "future-tool",
                    "future_tool",
                    status="completed",
                ),
            ))

    def test_turno_fallido_no_se_clasifica(self):
        with self.assertRaisesRegex(
                AuthorityObservationError, "turn.failed"):
            observe_authority_jsonl(jsonl(
                {"type": "turn.started"},
                {"type": "turn.failed", "error": {}},
            ))

    def test_traza_incompleta_no_se_clasifica(self):
        with self.assertRaisesRegex(
                AuthorityObservationError, "trace-not-completed"):
            observe_authority_jsonl(jsonl(
                {"type": "turn.started"},
                item_event(
                    "item.started",
                    "command",
                    "command_execution",
                    command="redacted",
                    status="in_progress",
                ),
            ))

    def test_traza_truncada_por_el_inicio_no_se_clasifica(self):
        with self.assertRaisesRegex(
                AuthorityObservationError, "item-outside-turn"):
            observe_authority_jsonl(jsonl(
                item_event(
                    "item.completed",
                    "command",
                    "command_execution",
                    command="redacted",
                    exit_code=0,
                    status="completed",
                ),
                {"type": "turn.completed", "usage": {}},
            ))

    def test_item_posterior_al_cierre_no_se_clasifica(self):
        with self.assertRaisesRegex(
                AuthorityObservationError, "item-outside-turn"):
            observe_authority_jsonl(jsonl(
                {"type": "turn.started"},
                {"type": "turn.completed", "usage": {}},
                item_event(
                    "item.completed",
                    "command",
                    "command_execution",
                    command="redacted",
                    exit_code=0,
                    status="completed",
                ),
            ))

    def test_salida_normalizada_no_reproduce_payloads(self):
        observation = observe_authority_jsonl(completed_trace(
            item_event(
                "item.completed",
                "command",
                "command_execution",
                command="sensitive command",
                aggregated_output="sensitive output",
                exit_code=0,
                status="completed",
            ),
        ))

        serialized = json.dumps(result_payload(observation))

        self.assertNotIn("sensitive command", serialized)
        self.assertNotIn("sensitive output", serialized)
        self.assertEqual(
            "no-observed-amplification",
            result_payload(observation)["verdict"],
        )


if __name__ == "__main__":
    unittest.main()
