from dataclasses import dataclass
from enum import Enum
from itertools import combinations
import unittest


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


if __name__ == "__main__":
    unittest.main()
