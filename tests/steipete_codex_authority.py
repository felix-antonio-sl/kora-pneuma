"""Finite authority witness for steipete in ``codex exec --json``."""

import argparse
from collections import Counter
from dataclasses import dataclass
from enum import Enum
import json
from pathlib import Path
import sys
from typing import Iterable


class Capability(Enum):
    COMMAND_EXECUTION = "command_execution"
    FILE_CHANGE = "file_change"
    WEB_SEARCH = "web_search"
    MCP_TOOL_CALL = "mcp_tool_call"
    COLLAB_TOOL_CALL = "collab_tool_call"


class Outcome(Enum):
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    DECLINED = "declined"
    INCOMPLETE = "incomplete"


SOURCE_TO_CODEX = {
    "Read": frozenset({Capability.COMMAND_EXECUTION}),
    "Write": frozenset({
        Capability.COMMAND_EXECUTION,
        Capability.FILE_CHANGE,
    }),
    "Edit": frozenset({
        Capability.COMMAND_EXECUTION,
        Capability.FILE_CHANGE,
    }),
    "Glob": frozenset({Capability.COMMAND_EXECUTION}),
    "Grep": frozenset({Capability.COMMAND_EXECUTION}),
    "Bash": frozenset({Capability.COMMAND_EXECUTION}),
}
DECLARED_IMAGE = frozenset().union(*SOURCE_TO_CODEX.values())

_CAPABILITY_BY_ITEM_TYPE = {
    capability.value: capability for capability in Capability
}
_NON_CAPABILITY_ITEM_TYPES = frozenset({
    "agent_message",
    "reasoning",
    "todo_list",
})


class AuthorityObservationError(ValueError):
    pass


@dataclass(frozen=True)
class CapabilityCall:
    item_id: str
    capability: Capability
    outcome: Outcome


@dataclass(frozen=True)
class AuthorityObservation:
    calls: tuple[CapabilityCall, ...]

    def capabilities(self, outcome: Outcome | None = None):
        return frozenset(
            call.capability
            for call in self.calls
            if outcome is None or call.outcome is outcome
        )

    def counts(self, outcome: Outcome):
        return Counter(
            call.capability
            for call in self.calls
            if call.outcome is outcome
        )

    @property
    def unmapped_successes(self):
        return self.capabilities(Outcome.SUCCEEDED) - DECLARED_IMAGE


def _terminal_outcome(capability: Capability, item: dict) -> Outcome:
    if capability is Capability.WEB_SEARCH:
        if (
            not isinstance(item.get("query"), str)
            or not isinstance(item.get("action"), dict)
        ):
            raise AuthorityObservationError(
                "web-search-without-payload"
            )
        return Outcome.SUCCEEDED

    status = item.get("status")
    if not isinstance(status, str):
        raise AuthorityObservationError("capability-without-status")
    if status == "declined":
        return Outcome.DECLINED
    if status == "failed":
        return Outcome.FAILED
    if status != "completed":
        raise AuthorityObservationError(
            f"non-terminal-completed-item:{status}"
        )

    if capability is Capability.COMMAND_EXECUTION:
        if not isinstance(item.get("command"), str):
            raise AuthorityObservationError("command-without-text")
        exit_code = item.get("exit_code")
        if not isinstance(exit_code, int):
            raise AuthorityObservationError(
                "command-without-exit-code"
            )
        return (
            Outcome.SUCCEEDED if exit_code == 0 else Outcome.FAILED
        )
    if (
        capability is Capability.FILE_CHANGE
        and not isinstance(item.get("changes"), list)
    ):
        raise AuthorityObservationError("file-change-without-changes")
    if capability is Capability.MCP_TOOL_CALL and (
        not isinstance(item.get("server"), str)
        or not isinstance(item.get("tool"), str)
    ):
        raise AuthorityObservationError("mcp-without-identity")
    if (
        capability is Capability.COLLAB_TOOL_CALL
        and not isinstance(item.get("tool"), str)
    ):
        raise AuthorityObservationError("collab-without-tool")
    return Outcome.SUCCEEDED


def observe_authority_jsonl(
        lines: Iterable[str]) -> AuthorityObservation:
    seen = {}
    turn_started = False
    turn_completed = False

    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise AuthorityObservationError(
                f"invalid-json-line:{line_number}"
            ) from exc
        if not isinstance(record, dict):
            raise AuthorityObservationError(
                f"non-object-line:{line_number}"
            )

        record_type = record.get("type")
        if not isinstance(record_type, str):
            raise AuthorityObservationError(
                f"record-without-type:{line_number}"
            )
        if record_type in {"turn.failed", "error"}:
            raise AuthorityObservationError(record_type)
        if record_type == "turn.started":
            if turn_started or turn_completed:
                raise AuthorityObservationError(
                    f"unexpected-turn-start:{line_number}"
                )
            turn_started = True
            continue
        if record_type == "turn.completed":
            if not turn_started or turn_completed:
                raise AuthorityObservationError(
                    f"unexpected-turn-completion:{line_number}"
                )
            turn_completed = True
            continue
        if record_type not in {
                "item.started", "item.updated", "item.completed"}:
            continue
        if not turn_started or turn_completed:
            raise AuthorityObservationError(
                f"item-outside-turn:{line_number}"
            )

        item = record.get("item")
        if not isinstance(item, dict):
            raise AuthorityObservationError(
                f"item-without-payload:{line_number}"
            )
        item_id = item.get("id")
        item_type = item.get("type")
        if not isinstance(item_id, str) or not isinstance(item_type, str):
            raise AuthorityObservationError(
                f"item-without-identity:{line_number}"
            )
        if item_type == "error":
            raise AuthorityObservationError(
                f"item-error:{line_number}"
            )
        if item_type in _NON_CAPABILITY_ITEM_TYPES:
            continue

        capability = _CAPABILITY_BY_ITEM_TYPE.get(item_type)
        if capability is None:
            raise AuthorityObservationError(
                f"unsupported-item-type:{item_type}:line:{line_number}"
            )

        previous = seen.get(item_id)
        if previous is not None and previous[0] is not capability:
            raise AuthorityObservationError(
                f"item-type-changed:{item_id}:line:{line_number}"
            )
        if record_type == "item.completed":
            outcome = _terminal_outcome(capability, item)
            seen[item_id] = (capability, outcome)
        elif previous is None:
            seen[item_id] = (capability, Outcome.INCOMPLETE)

    if not turn_started or not turn_completed:
        raise AuthorityObservationError("trace-not-completed")

    calls = tuple(
        CapabilityCall(item_id, capability, outcome)
        for item_id, (capability, outcome) in sorted(seen.items())
    )
    return AuthorityObservation(calls)


def _names(values):
    return sorted(value.value for value in values)


def _count_payload(observation, outcome):
    counts = observation.counts(outcome)
    return {
        capability.value: counts[capability]
        for capability in sorted(counts, key=lambda item: item.value)
    }


def result_payload(observation: AuthorityObservation) -> dict:
    amplified = observation.unmapped_successes
    return {
        "attempted": _names(observation.capabilities()),
        "succeeded": _count_payload(
            observation, Outcome.SUCCEEDED
        ),
        "failed": _count_payload(observation, Outcome.FAILED),
        "declined": _count_payload(observation, Outcome.DECLINED),
        "incomplete": _count_payload(
            observation, Outcome.INCOMPLETE
        ),
        "declared_image": _names(DECLARED_IMAGE),
        "unmapped_successes": _names(amplified),
        "verdict": (
            "counterexample"
            if amplified else "no-observed-amplification"
        ),
    }


def _observe_path(path: str) -> AuthorityObservation:
    if path == "-":
        return observe_authority_jsonl(sys.stdin)
    with Path(path).open(encoding="utf-8") as trace:
        return observe_authority_jsonl(trace)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Clasifica familias de capacidad observadas en "
            "codex exec --json."
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
        observation = _observe_path(args.trace)
    except (AuthorityObservationError, OSError) as exc:
        print(json.dumps(
            {"observation_error": str(exc)},
            ensure_ascii=False,
            sort_keys=True,
        ))
        return 2

    payload = result_payload(observation)
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    return 1 if observation.unmapped_successes else 0


if __name__ == "__main__":
    raise SystemExit(main())
