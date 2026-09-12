import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
PROBE = ROOT / "scripts/probe_codex.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("probe_codex_child", PROBE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CodexChildEvidenceTests(unittest.TestCase):
    def test_native_child_turn_requires_matching_lifecycle_and_final_answer(self):
        module = load_probe()
        answer = {"status": "INCOMPLETE", "limitation": "MISSING_INPUT",
                  "marker": "KORA_CHILD_INCOMPLETE"}
        start = {"method": "item/completed", "params": {"threadId": "parent", "item": {
            "type": "subAgentActivity", "kind": "started", "agentThreadId": "child",
            "agentPath": "/parent/child"}}}
        end = {"method": "item/completed", "params": {"threadId": "parent", "item": {
            "type": "subAgentActivity", "kind": "completed", "agentThreadId": "child",
            "agentPath": "/parent/child"}}}
        turn = {"method": "turn/completed", "params": {"threadId": "child", "turn": {
            "status": "completed", "items": [{"type": "agentMessage", "phase": "final_answer",
                                                "text": json.dumps(answer)}]}}}
        observed = module._incomplete_child_result([start, turn, end])
        self.assertTrue(observed["observed"])
        extended = json.loads(json.dumps(turn))
        extended["params"]["turn"]["items"][0]["text"] = json.dumps({**answer, "detail": "input absent"})
        self.assertTrue(module._incomplete_child_result([start, extended, end])["observed"])
        self.assertEqual(observed["child_thread_id"], "child")
        self.assertEqual(observed["parent_thread_id"], "parent")
        for missing in ([turn], [start, turn], [turn, end]):
            self.assertFalse(module._incomplete_child_result(missing)["observed"])
        for field, value in (("threadId", "parent"), ("threadId", "unrelated")):
            altered = json.loads(json.dumps(turn))
            altered["params"][field] = value
            self.assertFalse(module._incomplete_child_result([start, altered, end])["observed"])
        for status in ("failed", "interrupted"):
            altered = json.loads(json.dumps(turn))
            altered["params"]["turn"]["status"] = status
            self.assertFalse(module._incomplete_child_result([start, altered, end])["observed"])
        echoed = json.loads(json.dumps(turn))
        echoed["params"]["turn"]["items"][0]["type"] = "userMessage"
        self.assertFalse(module._incomplete_child_result([start, echoed, end])["observed"])

    @classmethod
    def setUpClass(cls):
        cls.module = load_probe()

    def test_prompt_echo_empty_state_and_unrelated_raw_output_are_rejected(self):
        contract = json.dumps({
            "status": "INCOMPLETE",
            "limitation": "MISSING_INPUT",
            "marker": "KORA_CHILD_INCOMPLETE",
        })
        events = [
            {"item": {"type": "collab_tool_call", "tool": "spawn_agent",
                      "arguments": {"marker": "KORA_CHILD_INCOMPLETE"}}},
            {"method": "item/completed", "params": {"item": {
                "type": "collabAgentToolCall", "id": "real-call", "tool": "wait",
                "status": "completed", "receiverThreadIds": [], "agentsStates": {},
            }}},
            {"method": "rawResponseItem/completed", "params": {"item": {
                "type": "function_call_output", "call_id": "unrelated-call", "name": "wait",
                "output": contract,
            }}},
        ]

        result = self.module._incomplete_child_result(events)

        self.assertFalse(result["observed"])

    def test_event_objects_accepts_native_json_array_receipt(self):
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8") as stream:
            json.dump([{"method": "item/completed"}, {"method": "turn/completed"}], stream)
            stream.flush()

            events = self.module._event_objects(Path(stream.name))

        self.assertEqual([event["method"] for event in events],
                         ["item/completed", "turn/completed"])

    def test_completed_native_collab_agents_states_exposes_child_contract(self):
        events = [{"method": "item/completed", "params": {"item": {
            "type": "collabAgentToolCall", "id": "wait-call", "tool": "wait",
            "status": "completed", "receiverThreadIds": ["child-thread"],
            "agentsStates": {"child-thread": {
                "status": "completed",
                "message": json.dumps({
                    "status": "INCOMPLETE",
                    "limitation": "MISSING_INPUT",
                    "marker": "KORA_CHILD_INCOMPLETE",
                }),
            }},
        }}}]

        result = self.module._incomplete_child_result(events)

        self.assertTrue(result["observed"])
        self.assertEqual(result["status"], "INCOMPLETE")
        self.assertEqual(result["limitation"], "MISSING_INPUT")
        self.assertEqual(result["marker"], "KORA_CHILD_INCOMPLETE")
        self.assertIn("collabAgentToolCall", result["event_types"])

    def test_correlated_raw_function_call_output_is_accepted(self):
        events = [
            {"method": "rawResponseItem/completed", "params": {"item": {
                "type": "function_call", "id": "responses-call", "call_id": "responses-call",
                "name": "wait", "arguments": "{}",
            }}},
            {"method": "item/completed", "params": {"item": {
                "type": "collabAgentToolCall", "id": "collab-call", "tool": "wait",
                "status": "completed", "receiverThreadIds": ["child-thread"],
                "agentsStates": {},
            }}},
            {"method": "rawResponseItem/completed", "params": {"item": {
                "type": "function_call_output", "call_id": "responses-call", "name": "wait",
                "output": json.dumps({
                    "status": "INCOMPLETE",
                    "limitation": "MISSING_INPUT",
                    "marker": "KORA_CHILD_INCOMPLETE",
                }),
            }}},
        ]

        result = self.module._incomplete_child_result(events)

        self.assertTrue(result["observed"])
        self.assertIn("function_call_output", result["event_types"])

    def test_raw_function_call_output_without_collab_item_is_rejected(self):
        contract = json.dumps({
            "status": "INCOMPLETE",
            "limitation": "MISSING_INPUT",
            "marker": "KORA_CHILD_INCOMPLETE",
        })
        events = [{
            "method": "rawResponseItem/completed",
            "params": {"item": {
                "type": "function_call", "id": "free-call", "call_id": "free-call",
                "name": "wait", "arguments": "{}",
            }},
        }, {
            "method": "rawResponseItem/completed",
            "params": {"item": {
                "type": "function_call_output", "call_id": "free-call", "name": "wait",
                "output": contract,
            }},
        }]

        result = self.module._incomplete_child_result(events)

        self.assertFalse(result["observed"])

    def test_app_server_request_retains_notifications_for_receive(self):
        module = self.module
        server = object.__new__(module.AppServer)
        server.buffer = (
            json.dumps({"method": "item/completed", "params": {"item": {"type": "marker"}}})
            + "\n"
            + json.dumps({"id": 1, "result": {"ok": True}})
            + "\n"
            + json.dumps({"method": "turn/completed", "params": {"threadId": "thread"}})
            + "\n"
        ).encode()
        server.notifications = []
        server.next_id = 0
        server.send = lambda message: None

        self.assertEqual(server.request("probe", {}), {"ok": True})
        completed = server.receive(lambda message: message.get("method") == "turn/completed")

        self.assertEqual(completed["method"], "turn/completed")
        self.assertEqual([item["method"] for item in server.notifications],
                         ["item/completed", "turn/completed"])

    def test_run_once_uses_native_app_server_turn(self):
        module = self.module
        calls = []

        class FakeServer:
            def __init__(self, workspace, config_home, log, prefix=None):
                self.notifications = []
                self.requests = []

            def request(self, method, params):
                self.requests.append((method, params))
                if method == "thread/start":
                    return {"thread": {"id": "thread-1"}, "model": "effective-model",
                            "reasoningEffort": "medium"}
                if method == "turn/start":
                    return {"turn": {"id": "turn-1"}}
                raise AssertionError(method)

            def receive(self, predicate):
                completed = {"method": "turn/completed", "params": {
                    "threadId": "thread-1",
                    "turn": {"id": "turn-1", "status": "completed", "items": [{
                        "type": "agentMessage",
                        "text": json.dumps({
                            "status": "CLOSED_WITH_LIMITATION",
                            "limitation": "MISSING_INPUT",
                            "marker": "KORA_PARENT_CLOSED",
                        }),
                    }]},
                }}
                self.notifications.append(completed)
                self.assert_predicate = predicate
                return completed

            def close(self):
                calls.append(self)

        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            workspace = root / "workspace"
            workspace.mkdir()
            with patch.object(module, "AppServer", FakeServer), \
                 patch.object(module.subprocess, "run", side_effect=AssertionError("legacy CLI")):
                result = module._run_codex_once(
                    ["codex", "-a", "never"], workspace, root, "synthetic prompt",
                    name="incomplete", model="synthetic-model", effort="high",
                )

        self.assertEqual(len(calls), 1)
        server = calls[0]
        self.assertEqual(result["returncode"], 0)
        self.assertEqual(result["answer"]["marker"], "KORA_PARENT_CLOSED")
        self.assertEqual(result["effective_model"], "effective-model")
        self.assertEqual(result["effective_effort"], "medium")
        thread_method, thread_params = server.requests[0]
        turn_method, turn_params = server.requests[1]
        self.assertEqual(thread_method, "thread/start")
        self.assertTrue(thread_params["ephemeral"])
        self.assertTrue(thread_params["experimentalRawEvents"])
        self.assertEqual(thread_params["model"], "synthetic-model")
        self.assertEqual(thread_params["config"]["model_reasoning_effort"], "high")
        self.assertEqual(turn_method, "turn/start")
        self.assertEqual(turn_params["threadId"], "thread-1")
        self.assertEqual(turn_params["input"], [{"type": "text", "text": "synthetic prompt"}])


if __name__ == "__main__":
    unittest.main()
