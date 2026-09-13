"""Deterministic values and validation, independent of inference and transport."""
from datetime import date, datetime, timezone
import hashlib
import json
from pathlib import PurePosixPath

KINDS = frozenset({"capture", "proposed_entry", "possibility", "reference", "action",
                   "project", "calendar", "waiting", "responsibility", "material"})
STATUSES = frozenset({"active", "waiting", "paused", "postponed", "done", "withdrawn"})
DATE_FIELDS = frozenset({"due_at", "review_at", "starts_at", "ends_at", "decision_at"})
EDITABLE = frozenset({"kind", "title", "text", "source", "context", "executor", "project_id",
                      "responsibility_id", "depends_on", "outcome", "completion_criteria",
                      "notes", "waiting_for", "waiting_kind", "relations", "uncertainties",
                      "duration_minutes", "energy", "priority", "timezone", "coverage",
                      "commitment", "purpose", "front", "plan_steps", "decision_needed",
                      "decision_question", "capacity", "source_versions"}) | DATE_FIELDS


def now():
    return datetime.now(timezone.utc).isoformat()


def encode(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def fingerprint(value):
    return hashlib.sha256(encode(value).encode()).hexdigest()


def valid_name(value):
    return (isinstance(value, str) and bool(value) and value not in {".", ".."}
            and "/" not in value and "\\" not in value and "\x00" not in value)


def safe_member(value):
    path = PurePosixPath(value)
    return (isinstance(value, str) and value and not path.is_absolute()
            and all(part not in {".", "..", ""} for part in value.split("/"))
            and "\\" not in value and "\x00" not in value)


def validate_date(value):
    if value is None:
        return
    if not isinstance(value, str):
        raise ValueError("invalid_date")
    try:
        if len(value) == 10:
            date.fromisoformat(value)
        elif datetime.fromisoformat(value).utcoffset() is None:
            raise ValueError("ambiguous_timezone")
    except ValueError as exc:
        raise ValueError("invalid_date_or_timezone") from exc


def validate_fields(fields):
    if not isinstance(fields, dict) or not fields or set(fields) - EDITABLE:
        raise ValueError("invalid_fields")
    encode(fields)
    if "commitment" in fields and fields["commitment"] not in {"proposed", "committed"}:
        raise ValueError("invalid_commitment")
    if "decision_needed" in fields and type(fields["decision_needed"]) is not bool:
        raise ValueError("invalid_decision_needed")
    for key in ("purpose", "front", "decision_question", "capacity"):
        if key in fields and fields[key] is not None and not isinstance(fields[key], str):
            raise ValueError("invalid_field_type")
    if "source_versions" in fields and (not isinstance(fields["source_versions"], dict) or
            any(not isinstance(k, str) or type(v) is not int or v < 1 for k, v in fields["source_versions"].items())):
        raise ValueError("invalid_source_versions")
    if "plan_steps" in fields and (not isinstance(fields["plan_steps"], list) or
            any(not isinstance(v, str) or not v.strip() for v in fields["plan_steps"])):
        raise ValueError("invalid_plan_steps")
    for key, value in fields.items():
        if key == "kind" and value not in KINDS:
            raise ValueError("invalid_kind")
        if key in {"title", "text", "notes", "outcome", "completion_criteria", "context",
                   "executor", "timezone", "waiting_for", "energy"} and value is not None and not isinstance(value, str):
            raise ValueError("invalid_field_type")
        if key == "text" and not isinstance(value, str):
            raise ValueError("invalid_text")
        if key == "title" and (not isinstance(value, str) or not value.strip()):
            raise ValueError("empty_title")
        if key == "source" and not isinstance(value, dict):
            raise ValueError("invalid_source")
        if key in {"depends_on", "relations", "uncertainties"} and not isinstance(value, list):
            raise ValueError("invalid_field_type")
        if key == "depends_on" and any(not isinstance(v, str) for v in value):
            raise ValueError("invalid_dependency")
        if key in {"project_id", "responsibility_id"} and value is not None and not isinstance(value, str):
            raise ValueError("invalid_relation")
        if key == "waiting_kind" and value not in {None, "person", "agent"}:
            raise ValueError("invalid_waiting_kind")
        if key == "duration_minutes" and (isinstance(value, bool) or not isinstance(value, (int, float)) or value < 0):
            raise ValueError("invalid_duration")
        if key in DATE_FIELDS:
            validate_date(value)
