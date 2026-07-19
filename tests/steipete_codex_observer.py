"""Executable witness for the steipete -> Codex trace monitor."""

import argparse
from dataclasses import dataclass
from enum import Enum
from itertools import combinations
import json
from pathlib import Path
import re
import shlex
import sys
from typing import Iterable


class Phase(Enum):
    START = "start"
    INTENT = "intent"
    ESTIMATED = "estimated"
    DIRTY = "dirty"
    VALIDATING = "validating"
    CLOSED = "closed"


class EventKind(Enum):
    CAPTURE = "capture"
    ESTIMATE = "estimate"
    CHANGE = "change"
    GATE = "gate"
    CLOSE = "close"


class Gate(Enum):
    DIFF_CHECK = "diff-check"
    FEEL_REVIEW = "feel-review"
    PARITY_STEIPETE = "paridad-steipete"
    PY_COMPILE = "py-compile"
    TESTS = "tests"
    VELAR = "velar"


REQUIRED_GATES = frozenset(Gate)
STEIPETE_URN = "urn:dev:artefacto:steipete"
MARKER_PREFIX = "KORA_OBS "

CANONICAL_GATE_COMMANDS = {
    Gate.PY_COMPILE: (
        "PYTHONPYCACHEPREFIX=/tmp/kora-observer-pyc "
        "python3 -m py_compile kora.py "
        "tests/steipete_codex_observer.py "
        "tests/test_steipete_vertical.py"
    ),
    Gate.TESTS: (
        "PYTHONDONTWRITEBYTECODE=1 "
        "python3 -m unittest discover -s tests"
    ),
    Gate.VELAR: "python3 kora.py velar --estricto",
    Gate.DIFF_CHECK: "git diff --check",
    Gate.PARITY_STEIPETE: (
        "python3 kora.py transmutar --paridad "
        f"--urn {STEIPETE_URN}"
    ),
}

_GATE_HINTS = (
    "python3 -m py_compile",
    "python3 -m unittest discover -s tests",
    "python3 kora.py velar --estricto",
    "git diff --check",
    "python3 kora.py transmutar --paridad",
)
_ENV_ASSIGNMENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=.*$")


@dataclass(frozen=True)
class State:
    phase: Phase
    passed: frozenset[Gate] = frozenset()


@dataclass(frozen=True)
class Event:
    kind: EventKind
    gate: Gate | None = None
    passed: bool | None = None


@dataclass(frozen=True)
class Accepted:
    output: str
    state: State


@dataclass(frozen=True)
class Rejected:
    violation: str


Result = Accepted | Rejected


class ObservationError(ValueError):
    pass


def step(state: State, event: Event) -> Result:
    """Coalgebraic monitor step U x I -> (O x U) + V."""
    if not state.passed <= REQUIRED_GATES:
        return Rejected("unknown-evidence")
    if state.phase is Phase.CLOSED:
        return Rejected("already-closed")
    if event.kind is not EventKind.GATE and (
            event.gate is not None or event.passed is not None):
        return Rejected("malformed-event")

    if event.kind is EventKind.CAPTURE:
        if state.phase is not Phase.START:
            return Rejected("intent-out-of-order")
        return Accepted("intent-captured", State(Phase.INTENT))

    if event.kind is EventKind.ESTIMATE:
        if state.phase is not Phase.INTENT:
            return Rejected("estimate-out-of-order")
        return Accepted("blast-radius-estimated", State(Phase.ESTIMATED))

    if event.kind is EventKind.CHANGE:
        if state.phase not in {
                Phase.ESTIMATED, Phase.DIRTY, Phase.VALIDATING}:
            return Rejected("change-out-of-order")
        return Accepted("evidence-invalidated", State(Phase.DIRTY))

    if event.kind is EventKind.GATE:
        if event.gate not in REQUIRED_GATES or event.passed is None:
            return Rejected("malformed-gate")
        if state.phase not in {Phase.DIRTY, Phase.VALIDATING}:
            return Rejected("gate-out-of-order")
        if not event.passed:
            return Accepted("gate-failed", State(Phase.DIRTY))
        return Accepted(
            "gate-passed",
            State(Phase.VALIDATING, state.passed | {event.gate}),
        )

    if event.kind is EventKind.CLOSE:
        if state.phase is not Phase.VALIDATING:
            return Rejected("close-out-of-order")
        missing = REQUIRED_GATES - state.passed
        if missing:
            names = sorted(gate.value for gate in missing)
            return Rejected("close-without:" + ",".join(names))
        return Accepted("closed", State(Phase.CLOSED, REQUIRED_GATES))

    return Rejected("unknown-event")


def run_trace(events: list[Event]) -> Result:
    state = State(Phase.START)
    for event in events:
        result = step(state, event)
        if isinstance(result, Rejected):
            return result
        state = result.state
    return Accepted("trace-accepted", state)


def is_safe(state: State) -> bool:
    return (
        state.passed <= REQUIRED_GATES
        and (state.phase is not Phase.CLOSED
             or state.passed == REQUIRED_GATES)
    )


def powerset(values: frozenset[Gate]):
    ordered = sorted(values, key=lambda gate: gate.value)
    for size in range(len(ordered) + 1):
        for subset in combinations(ordered, size):
            yield frozenset(subset)


def all_events() -> list[Event]:
    events = [
        Event(EventKind.CAPTURE),
        Event(EventKind.ESTIMATE),
        Event(EventKind.CHANGE),
        Event(EventKind.CLOSE),
    ]
    for gate in sorted(REQUIRED_GATES, key=lambda item: item.value):
        events.append(Event(EventKind.GATE, gate, True))
        events.append(Event(EventKind.GATE, gate, False))
    return events


def _shell_payload(command: str) -> str:
    try:
        outer = shlex.split(command)
    except ValueError as exc:
        raise ObservationError("invalid-command-quoting") from exc
    if len(outer) == 3 and outer[1] == "-lc":
        return outer[2]
    return command


def _command_tokens(command: str) -> tuple[str, dict[str, str], list[str]]:
    payload = _shell_payload(command)
    try:
        tokens = shlex.split(payload)
    except ValueError as exc:
        raise ObservationError("invalid-command-quoting") from exc
    environment = {}
    while tokens and _ENV_ASSIGNMENT.fullmatch(tokens[0]):
        name, value = tokens.pop(0).split("=", 1)
        if name in environment:
            raise ObservationError("duplicate-command-environment")
        environment[name] = value
    return payload, environment, tokens


def gate_for_command(command: str) -> Gate | None:
    payload, environment, tokens = _command_tokens(command)
    gate = None

    if (
        environment == {
            "PYTHONPYCACHEPREFIX": "/tmp/kora-observer-pyc"
        }
        and tokens == [
            "python3",
            "-m",
            "py_compile",
            "kora.py",
            "tests/steipete_codex_observer.py",
            "tests/test_steipete_vertical.py",
        ]
    ):
        gate = Gate.PY_COMPILE
    elif (
        environment == {"PYTHONDONTWRITEBYTECODE": "1"}
        and tokens == [
            "python3", "-m", "unittest", "discover", "-s", "tests"
        ]
    ):
        gate = Gate.TESTS
    elif (
        not environment
        and tokens == ["python3", "kora.py", "velar", "--estricto"]
    ):
        gate = Gate.VELAR
    elif not environment and tokens == ["git", "diff", "--check"]:
        gate = Gate.DIFF_CHECK
    elif (
        not environment
        and tokens == [
            "python3", "kora.py", "transmutar", "--paridad",
            "--urn", STEIPETE_URN,
        ]
    ):
        gate = Gate.PARITY_STEIPETE

    if gate is None and any(hint in payload for hint in _GATE_HINTS):
        raise ObservationError("non-canonical-gate-command")
    return gate


def _marker_events(text: str) -> list[Event]:
    events = []
    for line in text.splitlines():
        if not line.startswith(MARKER_PREFIX):
            continue
        try:
            marker = json.loads(line[len(MARKER_PREFIX):])
        except json.JSONDecodeError as exc:
            raise ObservationError("invalid-marker-json") from exc
        if not isinstance(marker, dict):
            raise ObservationError("invalid-marker")

        if marker == {"kind": "estimate"}:
            events.append(Event(EventKind.ESTIMATE))
        elif marker == {"kind": "change"}:
            events.append(Event(EventKind.CHANGE))
        elif (
            set(marker) == {"kind", "passed"}
            and marker["kind"] == "feel-review"
            and isinstance(marker["passed"], bool)
        ):
            events.append(
                Event(
                    EventKind.GATE,
                    Gate.FEEL_REVIEW,
                    marker["passed"],
                )
            )
        else:
            raise ObservationError("unsupported-marker")
    return events


def observe_record(record: dict) -> list[Event]:
    record_type = record.get("type")
    if not isinstance(record_type, str):
        raise ObservationError("record-without-type")

    if record_type == "turn.started":
        return [Event(EventKind.CAPTURE)]
    if record_type == "turn.completed":
        return [Event(EventKind.CLOSE)]
    if record_type in {"turn.failed", "error"}:
        raise ObservationError(record_type)
    if record_type != "item.completed":
        return []

    item = record.get("item")
    if not isinstance(item, dict):
        raise ObservationError("completed-item-without-payload")
    item_type = item.get("type")
    if not isinstance(item_type, str):
        raise ObservationError("completed-item-without-type")

    if item_type == "agent_message":
        text = item.get("text")
        if not isinstance(text, str):
            raise ObservationError("agent-message-without-text")
        return _marker_events(text)

    if item_type == "file_change":
        changes = item.get("changes")
        if not isinstance(changes, list):
            raise ObservationError("file-change-without-changes")
        return [Event(EventKind.CHANGE)] if changes else []

    if item_type == "command_execution":
        command = item.get("command")
        if not isinstance(command, str):
            raise ObservationError("command-without-text")
        gate = gate_for_command(command)
        if gate is None:
            return []
        exit_code = item.get("exit_code")
        status = item.get("status")
        if not isinstance(exit_code, int):
            raise ObservationError("gate-without-exit-code")
        if not isinstance(status, str):
            raise ObservationError("gate-without-status")
        passed = status == "completed" and exit_code == 0
        return [Event(EventKind.GATE, gate, passed)]

    return []


def observe_codex_jsonl(lines: Iterable[str]) -> list[Event]:
    events = []
    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ObservationError(
                f"invalid-json-line:{line_number}"
            ) from exc
        if not isinstance(record, dict):
            raise ObservationError(f"non-object-line:{line_number}")
        try:
            events.extend(observe_record(record))
        except ObservationError as exc:
            raise ObservationError(
                f"{exc}:line:{line_number}"
            ) from exc
    return events


def evaluate_codex_jsonl(lines: Iterable[str]) -> tuple[list[Event], Result]:
    events = observe_codex_jsonl(lines)
    result = run_trace(events)
    if (
        isinstance(result, Accepted)
        and result.state.phase is not Phase.CLOSED
    ):
        result = Rejected(f"trace-not-closed:{result.state.phase.value}")
    return events, result


def _event_payload(event: Event) -> dict:
    payload = {"kind": event.kind.value}
    if event.kind is EventKind.GATE:
        payload["gate"] = event.gate.value
        payload["passed"] = event.passed
    return payload


def _result_payload(events: list[Event], result: Result) -> dict:
    payload = {
        "events": [_event_payload(event) for event in events],
        "accepted": isinstance(result, Accepted),
    }
    if isinstance(result, Accepted):
        payload["phase"] = result.state.phase.value
        payload["passed"] = sorted(
            gate.value for gate in result.state.passed
        )
    else:
        payload["violation"] = result.violation
    return payload


def _evaluate_path(path: str) -> tuple[list[Event], Result]:
    if path == "-":
        return evaluate_codex_jsonl(sys.stdin)
    with Path(path).open(encoding="utf-8") as trace:
        return evaluate_codex_jsonl(trace)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Proyecta codex exec --json al monitor vertical "
            "steipete -> Codex."
        )
    )
    parser.add_argument(
        "trace",
        nargs="?",
        default="-",
        help="JSONL de codex exec --json; '-' lee stdin.",
    )
    args = parser.parse_args(argv)

    try:
        events, result = _evaluate_path(args.trace)
    except (ObservationError, OSError) as exc:
        print(json.dumps(
            {"accepted": False, "observation_error": str(exc)},
            ensure_ascii=False,
            sort_keys=True,
        ))
        return 2

    print(json.dumps(
        _result_payload(events, result),
        ensure_ascii=False,
        sort_keys=True,
    ))
    return 0 if isinstance(result, Accepted) else 1


if __name__ == "__main__":
    raise SystemExit(main())
