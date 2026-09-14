"""Transactional application boundary shared by human and agent transports.

Actors are identities supplied by an authenticated caller, never inferred from
source text. This library performs local effects only; no actor string grants
external authority. Field versions guard stale commands and operation-specific
undo, including intervening changes that happen to restore the same value.
"""
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
import sqlite3
import stat
import tempfile
import uuid
import zipfile

from .domain import (EDITABLE, encode, fingerprint, now, safe_member, valid_name,
                     validate_date, validate_fields)
from .gtd import GTDDomain
from .store import SCHEMA_VERSION, Store, fsync_dir, private_dir, write_private


class GTDService(GTDDomain):
    def __init__(self, data_dir: Path, *, owner_actor="felix", principal_actor="gtd-felix", executor_actors=()):
        self.store = Store(data_dir)
        self.data_dir = self.store.root
        self._configure_actors(owner_actor, principal_actor, executor_actors)

    @property
    def recovery_required(self):
        with self.store.lock:
            row = self.store.db.execute("SELECT value FROM metadata WHERE key='recovery_required'").fetchone()
            return bool(row and json.loads(row[0]))

    def _item(self, item_id):
        row = self.store.db.execute("SELECT document,field_versions FROM items WHERE id=?", (item_id,)).fetchone()
        return (json.loads(row[0]), json.loads(row[1])) if row else (None, None)

    def get_item(self, item_id: str) -> dict | None:
        with self.store.lock:
            return self._item(item_id)[0]

    def describe_item(self, item_id):
        """Read projection; never add provenance to stored documents or receipts."""
        with self.store.lock:
            item, versions = self._item(item_id)
            if item is None:
                return None
            provenance = {}
            for key in self.MEANING | {"text", "source", "status", "decision_needed", "decision_question"}:
                field = versions.get(key)
                if not field:
                    continue
                row = self.store.db.execute(
                    "SELECT created_at,actor,item_id,applied_version,receipt FROM operations WHERE operation_id=?",
                    (field.get("operation_id"),)).fetchone()
                verified = row and row[1] == field["actor"] and row[2] == item_id and row[3] == field["version"]
                provenance[key] = {"actor": field["actor"], "version": field["version"],
                    "operation_at": row[0] if verified else None}
                if verified:
                    authority = json.loads(row[4]).get("item", {}).get("human_instruction")
                    if authority and authority.get("operation_id") == field.get("operation_id"):
                        provenance[key]["human_authority"] = authority
            return {**item, "field_provenance": provenance}

    def _replay(self, operation_id, digest):
        row = self.store.db.execute("SELECT fingerprint,receipt FROM operations WHERE operation_id=?", (operation_id,)).fetchone()
        if row is None:
            return None
        if row[0] != digest:
            return {"operation_id": operation_id, "status": "rejected", "error": "operation_id_reused"}
        receipt = json.loads(row[1])
        if receipt["status"] == "applied":
            receipt["status"] = "already_applied"
        return receipt

    def _record(self, actor, operation_id, digest, receipt, before=None, after=None, version=None):
        self.store.db.execute(
            "INSERT INTO operations VALUES(?,?,?,?,?,?,?,?,?)",
            (operation_id, digest, actor, encode(receipt), receipt.get("item", {}).get("id"),
             encode(before) if before is not None else None,
             encode(after) if after is not None else None, version, now()))
        return receipt

    @staticmethod
    def _identity(actor, operation_id):
        return (isinstance(actor, str) and bool(actor.strip()) and isinstance(operation_id, str)
                and bool(operation_id.strip()) and len(operation_id) <= 512)

    def ingest_event(self, event: dict) -> dict:
        try:
            provider, account = event["provider"], event["account"]
            if not all(isinstance(v, str) and v for v in (provider, account)):
                raise ValueError()
            external_id, revision = str(event["external_id"]), str(event["revision"])
            payload = event["payload"]
            if not isinstance(payload, dict):
                raise ValueError()
            key = fingerprint([provider, account, external_id, revision])
            digest = fingerprint(payload)
        except (KeyError, TypeError, ValueError):
            return {"event_key": None, "status": "rejected", "duplicate": False, "error": "invalid_event"}
        with self.store.transaction():
            row = self.store.db.execute("SELECT fingerprint,status FROM events WHERE event_key=?", (key,)).fetchone()
            if row:
                if row[0] != digest:
                    return {"event_key": key, "status": "rejected", "duplicate": False, "error": "event_identity_reused"}
                return {"event_key": key, "status": row[1], "duplicate": True}
            self.store.db.execute("INSERT INTO events VALUES(?,?,?,?,?,?,?,?,NULL,?)",
                                  (key, provider, account, external_id, revision, digest, encode(payload), "received", now()))
            return {"event_key": key, "status": "received", "duplicate": False}

    def pending_events(self, provider: str, account: str) -> list[dict]:
        with self.store.lock:
            rows = self.store.db.execute(
                "SELECT * FROM events WHERE provider=? AND account=? AND status NOT IN ('applied','done','rejected','ignored') ORDER BY received_at,event_key",
                (provider, account)).fetchall()
            return [{**dict(row), "payload": json.loads(row["payload"])} for row in rows]

    def mark_event(self, event_key: str, status: str, error: str | None = None) -> None:
        if status not in {"received", "pending", "processing", "failed", "applied", "done", "rejected", "ignored"}:
            raise ValueError("invalid_event_status")
        with self.store.transaction():
            row = self.store.db.execute("SELECT status FROM events WHERE event_key=?", (event_key,)).fetchone()
            if not row:
                raise ValueError("event_not_found")
            if row[0] in {"applied", "done", "rejected", "ignored"} and row[0] != status:
                raise ValueError("terminal_event")
            self.store.db.execute("UPDATE events SET status=?,error=? WHERE event_key=?", (status, error, event_key))

    def get_cursor(self, provider: str, account: str) -> str | None:
        with self.store.lock:
            row = self.store.db.execute("SELECT cursor FROM cursors WHERE provider=? AND account=?", (provider, account)).fetchone()
            return row[0] if row else None

    def set_cursor(self, provider: str, account: str, cursor: str) -> None:
        if not all(isinstance(v, str) and v for v in (provider, account, cursor)):
            raise ValueError("invalid_cursor")
        with self.store.transaction():
            self.store.db.execute("INSERT INTO cursors VALUES(?,?,?) ON CONFLICT(provider,account) DO UPDATE SET cursor=excluded.cursor", (provider, account, cursor))

    def capture(self, actor: str, operation_id: str, text: str, source: dict | None = None,
                original: bytes | None = None, filename: str | None = None,
                mime_type: str | None = None) -> dict:
        if not self._identity(actor, operation_id):
            return {"operation_id": operation_id, "status": "rejected", "error": "invalid_identity"}
        try:
            if not isinstance(text, str) or (source is not None and not isinstance(source, dict)):
                raise ValueError("invalid_capture")
            if original is not None and not isinstance(original, bytes):
                raise ValueError("invalid_original")
            if filename is not None and not valid_name(filename):
                raise ValueError("unsafe_filename")
            if mime_type is not None and not isinstance(mime_type, str):
                raise ValueError("invalid_mime_type")
            if not text.strip() and original is None:
                raise ValueError("empty_capture")
            content = text.encode() if original is None else original
            digest = fingerprint({"actor": actor, "action": "capture", "text": text, "source": source,
                                  "original": hashlib.sha256(content).hexdigest(), "filename": filename, "mime_type": mime_type})
        except (ValueError, TypeError) as exc:
            return {"operation_id": operation_id, "status": "rejected", "error": str(exc) if isinstance(exc, ValueError) else "invalid_capture"}
        try:
            with self.store.transaction():
                replay = self._replay(operation_id, digest)
                if replay:
                    return replay
                if self.actor_role(actor) is None:
                    return self._record(actor, operation_id, digest, {"operation_id": operation_id, "status": "rejected", "error": "unauthorized_actor"})
                blob = self.store.save_original(content)
                blob.update(filename=filename or ("capture.txt" if original is None else "original.bin"),
                            mime_type=mime_type or ("text/plain; charset=utf-8" if original is None else "application/octet-stream"))
                self.store.db.execute("INSERT OR IGNORE INTO originals VALUES(?,?,?)", (blob["sha256"], blob["size"], blob["path"]))
                stamp = now()
                item = {"id": uuid.uuid4().hex, "kind": "capture", "status": "active", "version": 1,
                        "title": text.strip() or "Audio / original pendiente de aclaración", "text": text,
                        "created_at": stamp, "updated_at": stamp, "created_by": actor,
                        "source": source or {}, "original": blob, "depends_on": [], "relations": [],
                        "commitment": "proposed",
                        "source_revisions": [{"source": source or {}, "text": text, "original": blob, "received_at": stamp}]}
                versions = {key: {"version": 1, "actor": actor, "operation_id": operation_id} for key in item}
                self.store.db.execute("INSERT INTO items VALUES(?,?,?)", (item["id"], encode(item), encode(versions)))
                self._review_event(item, "capture")
                return self._record(actor, operation_id, digest,
                                    {"operation_id": operation_id, "status": "applied", "item": item},
                                    {}, {"_created": True}, 1)
        except (OSError, sqlite3.Error):
            return {"operation_id": operation_id, "status": "uncertain", "error": "storage_unavailable"}

    def revise_source(self, actor: str, operation_id: str, item_id: str, source: dict,
                      text: str | None = None, original: bytes | None = None,
                      filename: str | None = None, mime_type: str | None = None) -> dict:
        """Append source evidence without rewriting human meaning or decisions."""
        if not self._identity(actor, operation_id):
            return {"operation_id": operation_id, "status": "rejected", "error": "invalid_identity"}
        try:
            if not isinstance(item_id, str) or not isinstance(source, dict):
                raise ValueError("invalid_source")
            if text is not None and not isinstance(text, str):
                raise ValueError("invalid_text")
            if original is not None and not isinstance(original, bytes):
                raise ValueError("invalid_original")
            if filename is not None and not valid_name(filename):
                raise ValueError("unsafe_filename")
            if mime_type is not None and not isinstance(mime_type, str):
                raise ValueError("invalid_mime_type")
            content = original if original is not None else (text.encode() if text is not None else None)
            digest = fingerprint({"actor": actor, "action": "revise_source", "item_id": item_id,
                                  "source": source, "text": text, "filename": filename, "mime_type": mime_type,
                                  "original": hashlib.sha256(content).hexdigest() if content is not None else None})
        except (TypeError, ValueError):
            return {"operation_id": operation_id, "status": "rejected", "error": "invalid_source_revision"}
        try:
            with self.store.transaction():
                replay = self._replay(operation_id, digest)
                if replay:
                    return replay
                if self.actor_role(actor) not in {"owner", "principal"}:
                    return self._record(actor, operation_id, digest, {"operation_id": operation_id, "status": "rejected", "error": "unauthorized_actor"})
                item, versions = self._item(item_id)
                if item is None:
                    return self._record(actor, operation_id, digest, {"operation_id": operation_id, "status": "rejected", "error": "item_not_found"})
                blob = item.get("original")
                if content is not None:
                    blob = self.store.save_original(content)
                    blob.update(filename=filename or ("revision.txt" if original is None else "original.bin"),
                                mime_type=mime_type or ("text/plain; charset=utf-8" if original is None else "application/octet-stream"))
                    self.store.db.execute("INSERT OR IGNORE INTO originals VALUES(?,?,?)", (blob["sha256"], blob["size"], blob["path"]))
                revisions = list(item.get("source_revisions", []))
                revisions.append({"source": source, "text": text, "original": blob, "received_at": now()})
                updates = {"source": source, "original": blob, "source_revisions": revisions}
                return self._apply(actor, operation_id, digest, item, versions,
                                   {key: {"present": True, "value": value} for key, value in updates.items()})
        except (OSError, sqlite3.Error):
            return {"operation_id": operation_id, "status": "uncertain", "error": "storage_unavailable"}

    def _validate_relations(self, item, fields):
        for source_id, revision in fields.get("source_versions", {}).items():
            source, _ = self._item(source_id)
            if not source or revision > len(source.get("source_revisions", [])):
                raise ValueError("invalid_source_version")
        for key, kind in (("project_id", "project"), ("responsibility_id", "responsibility")):
            value = fields.get(key)
            if value:
                target, _ = self._item(value)
                if not target or target["kind"] != kind or value == item["id"]:
                    raise ValueError("invalid_relation")
        if "depends_on" in fields:
            pending = list(fields["depends_on"])
            seen = set()
            while pending:
                target_id = pending.pop()
                if target_id == item["id"]:
                    raise ValueError("dependency_cycle")
                if target_id in seen:
                    continue
                seen.add(target_id)
                target, _ = self._item(target_id)
                if target is None:
                    raise ValueError("dependency_not_found")
                pending.extend(target.get("depends_on", []))
        if "relations" in fields:
            for relation in fields["relations"]:
                if (not isinstance(relation, dict) or not isinstance(relation.get("type"), str)
                        or not relation["type"] or not isinstance(relation.get("target_id"), str)
                        or self._item(relation["target_id"])[0] is None):
                    raise ValueError("invalid_relation")

    def _apply(self, actor, operation_id, digest, item, versions, changes):
        before = {key: {"present": key in item, "value": item.get(key)} for key in changes}
        after = {}
        item = dict(item)
        item["version"] += 1
        item["updated_at"] = now()
        for key, change in changes.items():
            if change["present"]:
                item[key] = change["value"]
            else:
                item.pop(key, None)
            after[key] = change
            versions[key] = {"version": item["version"], "actor": actor, "operation_id": operation_id}
        self.store.db.execute("UPDATE items SET document=?,field_versions=? WHERE id=?", (encode(item), encode(versions), item["id"]))
        self._review_event(item, "change")
        if item["status"] in {"done", "withdrawn"}:
            self._exhaust_mandates(item)
        return self._record(actor, operation_id, digest, {"operation_id": operation_id, "status": "applied", "item": item}, before, after, item["version"])

    def execute(self, actor: str, command: dict) -> dict:
        operation_id = command.get("operation_id") if isinstance(command, dict) else None
        if not self._identity(actor, operation_id):
            return {"operation_id": operation_id, "status": "rejected", "error": "invalid_identity"}
        try:
            digest = fingerprint({"actor": actor, "command": command})
        except (ValueError, TypeError):
            return {"operation_id": operation_id, "status": "rejected", "error": "invalid_command"}
        try:
            with self.store.transaction():
                replay = self._replay(operation_id, digest)
                if replay:
                    return replay
                self.store.db.execute("SAVEPOINT command_change")
                try:
                    if self.actor_role(actor) is None:
                        raise ValueError("unauthorized_actor")
                    if self.recovery_required and self.actor_role(actor) != "owner":
                        raise ValueError("recovery_required")
                    if command.get("action") in self.SEMANTIC_ACTIONS:
                        return self._semantic(actor, command, digest)
                    receipt = self._execute(actor, command, digest)
                    if (actor == self.owner_actor and command.get('action') in {'pause', 'reopen'}
                            and receipt.get('status') == 'applied'):
                        self._set_meta('owner_state_action:' + operation_id, {
                            'action': command['action'], 'item_id': receipt['item']['id'],
                            'applied_version': receipt['item']['version']})
                    return receipt
                except (ValueError, TypeError, KeyError) as exc:
                    self.store.db.execute("ROLLBACK TO command_change")
                    self.store.db.execute("RELEASE command_change")
                    code = str(exc) if isinstance(exc, ValueError) else "invalid_command"
                    return self._record(actor, operation_id, digest, {"operation_id": operation_id, "status": "rejected", "error": code})
        except (OSError, sqlite3.Error):
            return {"operation_id": operation_id, "status": "uncertain", "error": "storage_unavailable"}

    def _conflict(self, actor, operation_id, digest, item, fields, versions, reason="stale_fields"):
        return self._record(actor, operation_id, digest,
                            {"operation_id": operation_id, "status": "conflict", "error": reason,
                             "item": item, "difference": {key: {"current": item.get(key), "last_change": versions.get(key)} for key in sorted(fields)}})

    def _execute(self, actor, command, digest):
        operation_id, action = command["operation_id"], command.get("action")
        fields = command.get("fields", {})
        if not isinstance(fields, dict):
            raise ValueError("invalid_fields")
        if action == "undo":
            if self.actor_role(actor) != "owner":
                raise ValueError("owner_required")
            return self._undo(actor, command, digest)
        if action not in {"edit", "done", "postpone", "pause", "withdraw", "reopen"}:
            raise ValueError("unknown_action")
        item_id = command.get("item_id")
        if not isinstance(item_id, str):
            raise ValueError("invalid_item_id")
        item, versions = self._item(item_id)
        if item is None:
            raise ValueError("item_not_found")
        expected = command.get("expected_version")
        if type(expected) is not int or not 1 <= expected <= item["version"]:
            raise ValueError("invalid_expected_version")
        self._authorize_change(actor, action, item, fields)
        if action == "edit":
            validate_fields(fields)
            self._validate_relations(item, fields)
            updates = dict(fields)
            if actor == self.owner_actor and fields.get("kind") in {"action", "project", "waiting", "responsibility", "calendar"}:
                updates.setdefault("commitment", "committed")
            relevant = set(fields)
            # A kind change changes what all domain fields mean. Conversely edits
            # based on a prior kind must not silently target a reclassified item.
            relevant.add("kind")
            if "kind" in fields:
                relevant |= set(EDITABLE) | {"status"}
        else:
            relevant = {"status", "kind", "title", "outcome", "completion_criteria", "executor", "project_id", "depends_on"}
            if action == "postpone":
                if set(fields) - {"review_at", "defer_until"}:
                    raise ValueError("invalid_fields")
                review = fields.get("review_at", fields.get("defer_until"))
                if review is None:
                    raise ValueError("review_at_required")
                validate_date(review)
                if item["status"] in {"done", "withdrawn"}:
                    raise ValueError("terminal_item")
                updates = {"status": "postponed", "review_at": review}
                relevant.add("review_at")
            else:
                if fields:
                    raise ValueError("invalid_fields")
                if action == "done":
                    if item["kind"] not in {"action", "project", "waiting"}:
                        raise ValueError("kind_not_completable")
                    if item["status"] == "withdrawn":
                        raise ValueError("withdrawn_item")
                    updates = {"status": "done", "completed_at": now()}
                elif action == "pause":
                    if item["status"] in {"done", "withdrawn"}:
                        raise ValueError("terminal_item")
                    updates = {"status": "paused"}
                elif action == "withdraw":
                    updates = {"status": "withdrawn", "withdrawn_at": now()}
                else:
                    if item["status"] == "active":
                        raise ValueError("already_open")
                    updates = {"status": "active", "completed_at": None, "withdrawn_at": None, "review_at": None}
                relevant |= set(updates)
        conflicts = {key for key in relevant if versions.get(key, {}).get("version", 0) > expected}
        if conflicts:
            return self._conflict(actor, operation_id, digest, item, conflicts, versions)
        # An explicit owner adoption of a principal's derived operational field
        # transfers authorship even when the wording stays unchanged.
        adopted = {key for key in updates if action == "edit" and actor == self.owner_actor
            and item.get("created_by") == self.principal_actor and item.get("parent_id")
            and item.get("kind") in {"action", "waiting"}
            and (key == "completion_criteria" or key == "waiting_for" and item["kind"] == "waiting")
            and versions.get(key, {}).get("actor") == self.principal_actor}
        changes = {key: {"present": True, "value": value} for key, value in updates.items()
                   if key not in item or item[key] != value or key in adopted}
        return self._apply(actor, operation_id, digest, item, versions, changes)

    def _undo(self, actor, command, digest):
        operation_id = command["operation_id"]
        target_id = command["fields"].get("operation_id")
        if not isinstance(target_id, str) or set(command["fields"]) != {"operation_id"}:
            raise ValueError("invalid_undo")
        target = self.store.db.execute("SELECT * FROM operations WHERE operation_id=?", (target_id,)).fetchone()
        if not target or json.loads(target["receipt"])["status"] != "applied":
            raise ValueError("operation_not_undoable")
        if "mandate" in json.loads(target["receipt"]):
            raise ValueError("mandate_requires_explicit_revoke")
        item, versions = self._item(target["item_id"])
        if item is None:
            raise ValueError("item_not_found")
        if command.get("item_id", item["id"]) != item["id"]:
            raise ValueError("undo_item_mismatch")
        expected = command.get("expected_version", item["version"])
        if type(expected) is not int or not 1 <= expected <= item["version"]:
            raise ValueError("invalid_expected_version")
        before, after = json.loads(target["before_patch"]), json.loads(target["after_patch"])
        if after.get("_created") is True:
            affected = {key for key in versions if key not in {"version", "updated_at"}}
            conflicts = {key for key in affected if versions[key]["version"] != 1}
            if conflicts:
                return self._conflict(actor, operation_id, digest, item, conflicts, versions, "undo_later_changes")
            changes = {"status": {"present": True, "value": "withdrawn"}, "withdrawn_at": {"present": True, "value": now()}}
        else:
            if not after:
                raise ValueError("operation_has_no_change")
            conflicts = {key for key in after if key != "source_revisions" and versions.get(key, {}).get("operation_id") != target_id}
            if conflicts:
                return self._conflict(actor, operation_id, digest, item, conflicts, versions, "undo_later_changes")
            changes = {key: value for key, value in before.items() if key != "source_revisions"}
        # Reverting a kind or relation must remain structurally valid now.
        restored = {key: change["value"] for key, change in changes.items() if change["present"] and key in EDITABLE}
        if restored:
            validate_fields(restored)
            self._validate_relations(item, restored)
        # Results live in tables now: undoing a material/assessment write
        # restores reference stubs in the document and prunes rows the undone
        # versions introduced, so the table stays the single authority.
        # Pruned rows are archived under this undo so inverting the inversion
        # (undo of an undo) restores exact rows instead of dangling stubs.
        # Absent before the undone write stays absent (empty reads alike).
        archive = {"materials": [], "assessments": []}
        for key, identity in (("materials", lambda stub: (stub.get("id"), stub.get("version"))),
                                ("assessments", lambda stub: stub.get("id"))):
            if key not in changes:
                continue
            if changes[key]["present"]:
                before_values = changes[key]["value"] or []
                changes[key] = {"present": True, "value": [
                    GTDDomain._material_stub(v) if key == "materials" else GTDDomain._assessment_stub(v)
                    for v in before_values]}
            else:
                changes[key] = {"present": False}
            keep = {identity(v) for v in changes[key]["value"]} if changes[key]["present"] else set()
            if key == "materials":
                rows = self.store.db.execute(
                    "SELECT * FROM materials WHERE item_id=?", (item["id"],)).fetchall()
                for row in rows:
                    if (row["id"], row["version"]) not in keep:
                        archive["materials"].append(dict(row))
                        self.store.db.execute(
                            "DELETE FROM materials WHERE item_id=? AND id=? AND version=?",
                            (item["id"], row["id"], row["version"]))
                have = {(row["id"], row["version"]) for row in self.store.db.execute(
                    "SELECT id, version FROM materials WHERE item_id=?", (item["id"],)).fetchall()}
                for ident in sorted(keep - have):
                    archived = {(r["id"], r["version"]): r for r in
                        self._meta("undo-archive:" + target_id, {}).get("materials", [])}
                    if ident not in archived:
                        raise ValueError("undone_result_unrecoverable")
                    row = archived[ident]
                    self.store.db.execute(
                        "INSERT INTO materials(id, version, item_id, author, title, mime_type, filename,"
                        " digest, size, basis_json, source_versions_json, mandate_id,"
                        " source_material_json, created_at)"
                        " VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (row["id"], row["version"], item["id"], row["author"], row["title"],
                         row["mime_type"], row["filename"], row["digest"], row["size"],
                         row["basis_json"], row["source_versions_json"], row["mandate_id"],
                         row["source_material_json"], row["created_at"]))
            else:
                rows = self.store.db.execute(
                    "SELECT * FROM assessments WHERE item_id=?", (item["id"],)).fetchall()
                for row in rows:
                    if row["id"] not in keep:
                        archive["assessments"].append(dict(row))
                        self.store.db.execute("DELETE FROM assessments WHERE id=?", (row["id"],))
                have = {row["id"] for row in self.store.db.execute(
                    "SELECT id FROM assessments WHERE item_id=?", (item["id"],)).fetchall()}
                for ident in sorted(keep - have):
                    archived = {r["id"]: r for r in
                        self._meta("undo-archive:" + target_id, {}).get("assessments", [])}
                    if ident not in archived:
                        raise ValueError("undone_result_unrecoverable")
                    row = archived[ident]
                    self.store.db.execute(
                        "INSERT INTO assessments(id, item_id, item_version, material_id, material_version,"
                        " actor, satisfied, criterion_hash, evidence, gap, resolution_basis_json,"
                        " material_basis_json, source_versions_json, mandate_id, created_at)"
                        " VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (row["id"], item["id"], row["item_version"], row["material_id"],
                         row["material_version"], row["actor"], row["satisfied"], row["criterion_hash"],
                         row["evidence"], row["gap"], row["resolution_basis_json"],
                         row["material_basis_json"], row["source_versions_json"], row["mandate_id"],
                         row["created_at"]))
        if archive["materials"] or archive["assessments"]:
            self._set_meta("undo-archive:" + operation_id, archive)
        return self._apply(actor, operation_id, digest, item, versions, changes)

    def query(self, filters: dict | None = None) -> list[dict]:
        filters = filters or {}
        allowed = {"kind", "status", "open", "available", "text", "project_id", "responsibility_id", "ids", "context", "executor", "source"}
        if not isinstance(filters, dict) or set(filters) - allowed:
            raise ValueError("invalid_filters")
        if "source" in filters:
            source = filters["source"]
            if isinstance(source, str) and source.strip():
                filters = {**filters, "source": {"provider": source}}
            elif not isinstance(source, dict):
                raise ValueError("invalid_source_filter")
        with self.store.lock:
            items = [json.loads(row[0]) for row in self.store.db.execute("SELECT document FROM items ORDER BY rowid")]
        by_id = {item["id"]: item for item in items}
        result = []
        for item in items:
            if any(item.get(key) != filters[key] for key in ("kind", "status", "project_id", "responsibility_id", "context", "executor") if key in filters):
                continue
            if "ids" in filters and item["id"] not in filters["ids"]:
                continue
            if filters.get("open") and item["status"] in {"done", "withdrawn"}:
                continue
            if filters.get("available") and (item["kind"] != "action" or item.get("commitment", "committed") != "committed" or item["status"] != "active" or any(by_id.get(dep, {}).get("status") != "done" for dep in item.get("depends_on", []))):
                continue
            if filters.get("text") and str(filters["text"]).casefold() not in (item["title"] + " " + item.get("text", "")).casefold():
                continue
            if "source" in filters and any(item.get("source", {}).get(key) != value for key, value in filters["source"].items()):
                continue
            result.append(item)
        return result

    def export(self, destination: Path) -> dict:
        """Create a dated readable snapshot and a restorable DB/original archive.

        Existing destinations are never overwritten. SQLite backup supplies a
        consistent snapshot even with another coordinator connection writing;
        originals are immutable and selected from that snapshot, not live state.
        """
        destination = Path(destination).absolute()
        if not valid_name(destination.name) or any(p.is_symlink() for p in (destination, *destination.parents)):
            raise ValueError("unsafe_export_path")
        if destination.exists() or not destination.parent.is_dir():
            raise ValueError("export_destination_unavailable")
        with tempfile.TemporaryDirectory(dir=self.data_dir, prefix="export-") as temp_name:
            temp = Path(temp_name)
            db_path = temp / "gtd.sqlite3"
            write_private(db_path, b"")
            snapshot = sqlite3.connect(db_path)
            try:
                with self.store.lock:
                    self.store.db.backup(snapshot)
                records = snapshot.execute("SELECT digest,size,relative_path FROM originals").fetchall()
                items = [json.loads(row[0]) for row in snapshot.execute("SELECT document FROM items ORDER BY rowid")]
                metadata = {row[0]: json.loads(row[1]) for row in snapshot.execute("SELECT key,value FROM metadata")}
                coverage = {"events": snapshot.execute("SELECT COUNT(*) FROM events").fetchone()[0], "items": len(items)}
            finally:
                snapshot.close()
            stamp = now()
            files = {"gtd.sqlite3": db_path.read_bytes()}
            for digest, size, relative in records:
                if relative != f"originals/{digest}" or len(digest) != 64:
                    raise ValueError("unsafe_original_path")
                path = self.data_dir / relative
                if path.is_symlink():
                    raise ValueError("unsafe_original_path")
                data = path.read_bytes()
                if len(data) != size or hashlib.sha256(data).hexdigest() != digest:
                    raise ValueError("original_corrupt")
                files[relative] = data
            files["state.json"] = (encode({"exported_at": stamp, "coverage": coverage, "items": items, "metadata": metadata, "actor_config": metadata.get("actor_config", {}),
                                          "limits": ["Snapshot local; no acredita vigencia de fuentes ni efectos externos."]}) + "\n").encode()
            lines = ["# GTD · copia consultable", "", f"Exportado: {stamp}", "", "Estado local en este instante; fuentes y efectos externos requieren reconciliación.", ""]
            for item in items:
                lines.extend([f"- {item['title']} [{item['kind']} / {item['status']}]", f"  ID: {item['id']} · versión {item['version']}", f"  Datos: {encode(item)}"])
            files["README.md"] = ("\n".join(lines) + "\n").encode()
            manifest = {"format": "gtd-felix-snapshot", "format_version": 1, "schema_version": SCHEMA_VERSION,
                        "exported_at": stamp, "coverage": coverage, "recovery_required": True,
                        "files": {name: {"sha256": hashlib.sha256(data).hexdigest(), "size": len(data)} for name, data in files.items()}}
            archive = temp / "snapshot.zip"
            with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as output:
                for name, data in files.items():
                    output.writestr(name, data)
                output.writestr("manifest.json", encode(manifest))
            write_private(destination, archive.read_bytes())
            return {"status": "applied", "path": str(destination), "sha256": hashlib.sha256(destination.read_bytes()).hexdigest(), **manifest}

    @classmethod
    def restore(cls, archive: Path, data_dir: Path):
        """Validate before touching target; restore only into a new/empty root.

        Pending events and receipts survive, but no jobs or sends are created.
        recovery_required marks that outside effects must first be reconciled.
        """
        data_dir = Path(data_dir).absolute()
        if any(p.is_symlink() for p in (data_dir, *data_dir.parents)):
            raise ValueError("symlink_path")
        if data_dir.exists() and (not data_dir.is_dir() or any(data_dir.iterdir())):
            raise ValueError("restore_requires_empty_directory")
        # Bound untrusted expansion before allocating. Large legitimate backups
        # can be restored only after an explicit product limit revision.
        with zipfile.ZipFile(archive) as incoming:
            entries = incoming.infolist()
            names = [entry.filename for entry in entries]
            if len(names) != len(set(names)) or len(names) > 100000:
                raise ValueError("invalid_archive_entries")
            if any(not safe_member(name) for name in names):
                raise ValueError("unsafe_archive_path")
            if any(stat.S_ISLNK(entry.external_attr >> 16) or entry.is_dir() for entry in entries):
                raise ValueError("unsafe_archive_entry")
            if sum(entry.file_size for entry in entries) > 1024 * 1024 * 1024:
                raise ValueError("archive_too_large")
            try:
                manifest = json.loads(incoming.read("manifest.json"))
                if manifest["format"] != "gtd-felix-snapshot" or manifest["format_version"] != 1 or manifest["schema_version"] != SCHEMA_VERSION:
                    raise ValueError("incompatible_snapshot")
                if set(names) != set(manifest["files"]) | {"manifest.json"}:
                    raise ValueError("archive_manifest_mismatch")
                files = {}
                for name, expected in manifest["files"].items():
                    data = incoming.read(name)
                    if len(data) != expected["size"] or hashlib.sha256(data).hexdigest() != expected["sha256"]:
                        raise ValueError("archive_checksum_mismatch")
                    files[name] = data
                if not {"gtd.sqlite3", "state.json", "README.md"} <= set(files):
                    raise ValueError("incomplete_snapshot")
                if any(name not in {"gtd.sqlite3", "state.json", "README.md"} and not (name.startswith("originals/") and len(name) == 74 and all(c in "0123456789abcdef" for c in name[10:])) for name in files):
                    raise ValueError("unexpected_archive_file")
            except (KeyError, TypeError, json.JSONDecodeError) as exc:
                raise ValueError("invalid_manifest") from exc
        # Validate the DB and its full original inventory in an isolated stage.
        parent = data_dir.parent
        if not parent.is_dir():
            raise ValueError("restore_parent_missing")
        with tempfile.TemporaryDirectory(dir=parent, prefix="gtd-restore-") as stage_name:
            stage = Path(stage_name)
            private_dir(stage / "originals")
            for name, data in files.items():
                write_private(stage / name, data)
            db = sqlite3.connect(stage / "gtd.sqlite3")
            try:
                if db.execute("PRAGMA integrity_check").fetchone()[0] != "ok" or db.execute("PRAGMA user_version").fetchone()[0] != SCHEMA_VERSION:
                    raise ValueError("invalid_snapshot_database")
                if db.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='trigger'").fetchone()[0]:
                    raise ValueError("unexpected_snapshot_trigger")
                originals = db.execute("SELECT digest,size,relative_path FROM originals").fetchall()
                expected_paths = set()
                for digest, size, relative in originals:
                    if relative != f"originals/{digest}" or relative not in files or len(files[relative]) != size or hashlib.sha256(files[relative]).hexdigest() != digest:
                        raise ValueError("snapshot_original_mismatch")
                    expected_paths.add(relative)
                if expected_paths != {name for name in files if name.startswith("originals/")}:
                    raise ValueError("snapshot_original_mismatch")
                state = json.loads(files["state.json"])
                documents = [json.loads(row[0]) for row in db.execute("SELECT document FROM items ORDER BY rowid")]
                db_metadata = {row[0]: json.loads(row[1]) for row in db.execute("SELECT key,value FROM metadata")}
                if "metadata" in state and db_metadata != state["metadata"]:
                    raise ValueError("snapshot_metadata_mismatch")
                if state.get("actor_config", {}) != db_metadata.get("actor_config", {}):
                    raise ValueError("snapshot_actor_config_mismatch")
                if documents != state["items"]:
                    raise ValueError("snapshot_state_mismatch")
                for item in documents:
                    blob = item.get("original")
                    if blob and (blob["path"] not in expected_paths or hashlib.sha256(files[blob["path"]]).hexdigest() != blob["sha256"]):
                        raise ValueError("snapshot_item_original_mismatch")
                db.execute("INSERT OR REPLACE INTO metadata VALUES('recovery_required','true')")
                db.execute("INSERT OR REPLACE INTO metadata VALUES('restored_at',?)", (encode(now()),))
                db.commit()
                db.execute("PRAGMA wal_checkpoint(TRUNCATE)")
            finally:
                db.close()
            # Reserve destination only after complete validation. No overwrite of
            # an existing file or nonempty directory, including concurrent writes.
            root = private_dir(data_dir)
            if any(root.iterdir()):
                raise ValueError("restore_requires_empty_directory")
            private_dir(root / "originals")
            for relative in expected_paths:
                write_private(root / relative, files[relative])
            write_private(root / "gtd.sqlite3", (stage / "gtd.sqlite3").read_bytes())
            fsync_dir(root)
        config = state.get("actor_config") or {}
        return cls(data_dir, **config)

    def close(self) -> None:
        self.store.close()


def migrate_i2_results(store):
    """I2 cut: materials/assessments/outbox-intents move to tables, once.

    Items keep reference stubs (identity, authorship, judgment); base snapshots
    live in rows. Outbox send-intents become deliveries rows; transient UI sends
    without an events row are counted as skipped (they carry no delivery
    obligation: a retry regenerates them). Legacy outbox keys are removed; the
    small per-event/per-key markers (delivery/material/question receipts) stay
    as deduplication state. Processes must be stopped with zero live runs;
    otherwise ValueError('active_work_present'). Unrepresentable rows abort the
    cut instead of dropping data. Returns a receipt dict (also stored).
    """
    with store.transaction():
        live = store.db.execute(
            "SELECT 1 FROM runs WHERE state NOT IN ('completed','failed','cancelled','expired')"
            " LIMIT 1").fetchone()
        if live:
            raise ValueError("active_work_present")
        full_arrays = 0
        for (document,) in store.db.execute("SELECT document FROM items"):
            item = json.loads(document)
            if any(isinstance(m, dict) and "basis" in m for m in item.get("materials", [])):
                full_arrays += 1
            if any(isinstance(a, dict) and "material_basis" in a for a in item.get("assessments", [])):
                full_arrays += 1
        outbox_keys = [row[0] for row in store.db.execute(
            "SELECT key FROM metadata WHERE key LIKE 'telegram-outbox:%'")]
        if not full_arrays and not outbox_keys:
            # Steady state (or fresh database): references everywhere, table
            # rows written by the service itself. Re-running is a no-op.
            return {"note": "already_migrated"}
        migrated_materials = migrated_assessments = migrated_deliveries = 0
        skipped_transient = 0
        for item_id, document in [(row[0], json.loads(row[1]))
                                 for row in store.db.execute("SELECT id, document FROM items")]:
            changed = False
            history = document.get("materials", [])
            if any(isinstance(m, dict) and "basis" in m for m in history):
                stubs = []
                for material in history:
                    for key in ("id", "author", "title", "created_at"):
                        if not isinstance(material.get(key), str) or not material[key]:
                            raise ValueError(f"unrepresentable_material:{item_id}")
                    if type(material.get("version")) is not int or material["version"] < 1:
                        raise ValueError(f"unrepresentable_material:{item_id}")
                    original = material.get("original") or {}
                    digest = original.get("sha256", "")
                    if len(digest) != 64 or not isinstance(original.get("size"), int):
                        raise ValueError(f"unrepresentable_material:{item_id}")
                    if not store.db.execute(
                            "SELECT 1 FROM originals WHERE digest=?", (digest,)).fetchone():
                        raise ValueError(f"material_original_missing:{item_id}")
                    if not isinstance(material.get("basis"), dict) or not isinstance(
                            material.get("source_versions"), dict):
                        raise ValueError(f"unrepresentable_material:{item_id}")
                    store.db.execute(
                        "INSERT INTO materials(id, version, item_id, author, title, mime_type, filename,"
                        " digest, size, basis_json, source_versions_json, mandate_id,"
                        " source_material_json, created_at)"
                        " VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (material["id"], material["version"], item_id, material["author"],
                         material.get("title", "Material preparado"),
                         original.get("mime_type", "text/plain; charset=utf-8"),
                         original.get("filename", "material.txt"), digest, original["size"],
                         encode(material["basis"]), encode(material["source_versions"]),
                         material.get("mandate_id"),
                         encode(material["source_material"]) if material.get("source_material") else None,
                         material["created_at"]))
                    migrated_materials += 1
                    stubs.append(GTDDomain._material_stub(material))
                document["materials"] = stubs
                changed = True
            recorded = document.get("assessments", [])
            if any(isinstance(a, dict) and "material_basis" in a for a in recorded):
                stubs = []
                for assessment in recorded:
                    if not isinstance(assessment.get("evidence"), str) or not assessment["evidence"].strip():
                        raise ValueError(f"unrepresentable_assessment:{item_id}")
                    if type(assessment.get("satisfied")) is not bool:
                        raise ValueError(f"unrepresentable_assessment:{item_id}")
                    if type(assessment.get("item_version")) is not int or assessment["item_version"] < 1:
                        raise ValueError(f"unrepresentable_assessment:{item_id}")
                    if not isinstance(assessment.get("assessed_at"), str):
                        raise ValueError(f"unrepresentable_assessment:{item_id}")
                    if not isinstance(assessment.get("resolution_basis"), dict) or not isinstance(
                            assessment.get("material_basis"), list):
                        raise ValueError(f"unrepresentable_assessment:{item_id}")
                    material_id = assessment.get("material_id")
                    material_version = assessment.get("material_version")
                    if (material_id is None) != (material_version is None):
                        raise ValueError(f"unrepresentable_assessment:{item_id}")
                    derived_id = hashlib.sha256("|".join(
                        [item_id, assessment["assessed_at"], assessment["evidence"]]).encode()).hexdigest()
                    try:
                        store.db.execute(
                            "INSERT INTO assessments(id, item_id, item_version, material_id, material_version,"
                            " actor, satisfied, criterion_hash, evidence, gap, resolution_basis_json,"
                            " material_basis_json, source_versions_json, mandate_id, created_at)"
                            " VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                            (derived_id, item_id, assessment["item_version"], material_id,
                             material_version, assessment.get("actor", ""),
                             1 if assessment["satisfied"] else 0,
                             hashlib.sha256(assessment["evidence"].encode()).hexdigest(),
                             assessment["evidence"], assessment.get("gap"),
                             encode(assessment["resolution_basis"]),
                             encode(assessment["material_basis"]),
                             encode(assessment.get("source_versions", {})),
                             assessment.get("mandate_id"), assessment["assessed_at"]))
                    except sqlite3.IntegrityError as exc:
                        raise ValueError(f"unrepresentable_assessment:{item_id}:{exc}") from exc
                    migrated_assessments += 1
                    stubs.append(GTDDomain._assessment_stub(
                        {"id": derived_id, **assessment,
                         "criterion_hash": hashlib.sha256(assessment["evidence"].encode()).hexdigest(),
                         "assessed_at": assessment["assessed_at"]}))
                document["assessments"] = stubs
                changed = True
            if changed:
                store.db.execute("UPDATE items SET document=? WHERE id=?", (encode(document), item_id))
        for key in outbox_keys:
            intent = json.loads(store.db.execute(
                "SELECT value FROM metadata WHERE key=?", (key,)).fetchone()[0])
            if intent.get("status") not in {"pending", "uncertain", "confirmed"}:
                raise ValueError(f"unrepresentable_delivery:{key}")
            event = store.db.execute(
                "SELECT payload FROM events WHERE event_key=?", (intent.get("event"),)).fetchone()
            event_payload = json.loads(event[0]) if event else None
            item_id = (event_payload or {}).get("item_id")
            if item_id is not None and not store.db.execute(
                    "SELECT 1 FROM items WHERE id=?", (item_id,)).fetchone():
                item_id = None
            if event is None:
                skipped_transient += 1
                store.db.execute("DELETE FROM metadata WHERE key=?", (key,))
                continue
            item_version = (event_payload or {}).get("version")
            if type(item_version) is not int or item_version < 1:
                item_version = None
            if item_id is None:
                item_version = None
            state = {"pending": "pending", "uncertain": "uncertain", "confirmed": "confirmed"}[intent["status"]]
            # The stored response keeps its JSON shape (dict for sends,
            # boolean for callback answers); rollback replays it verbatim.
            segments = [] if "response" not in intent else [{"status": intent["status"], "response": intent["response"]}]
            store.db.execute(
                "INSERT INTO deliveries(id, item_id, item_version, channel, target_key, semantic_key,"
                " state, payload_json, segments_json, created_at, retry_at, confirmed_at)"
                " VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                ("tg:" + key.split(":", 1)[1], item_id, item_version, "telegram",
                 intent.get("account", ""),
                 str(intent.get("event")) + ":" + str(intent.get("ordinal")),
                 state, encode({"method": intent.get("method"), "payload": intent.get("payload"),
                                "event": intent.get("event"), "ordinal": intent.get("ordinal"),
                                "account": intent.get("account")}),
                 encode(segments), None, None, None))
            migrated_deliveries += 1
            store.db.execute("DELETE FROM metadata WHERE key=?", (key,))
        receipt = {"schema": 3, "migrated_materials": migrated_materials,
                   "migrated_assessments": migrated_assessments,
                   "migrated_deliveries": migrated_deliveries,
                   "skipped_transient_sends": skipped_transient,
                   "at": datetime.now(timezone.utc).isoformat()}
        store.db.execute("INSERT OR REPLACE INTO metadata VALUES('migration:i2',?)", (encode(receipt),))
        return receipt


def migrate_i3_sources(store):
    """I3 cut: per-revision intake/selection rows move to source_entries, once.

    Inventories every index-record version event AND every standalone durable
    decision (noise/uncertain without projected object), each with its full
    provider/account/collection scope. Refuses with active sync cycles
    (ValueError('active_sync_present')) so no intake races the cut;
    unrepresentable rows abort instead of dropping data. Pruned row ids stay
    archived: reruns migrate only genuinely new facts and never resurrect.
    A rerun with nothing new reports already_migrated. Returns a receipt.
    """
    from .source_entries import entry_id, _pruned_archive
    with store.transaction():
        for (key,) in store.db.execute(
                "SELECT key FROM metadata WHERE key LIKE 'source-sync:%'"
                " AND key NOT LIKE 'source-sync:object:%' AND key NOT LIKE 'source-sync:google:%'"):
            state = json.loads(store.db.execute(
                "SELECT value FROM metadata WHERE key=?", (key,)).fetchone()[0])
            if isinstance(state, dict) and state.get("active_cycle") is not None:
                raise ValueError("active_sync_present")
        archived = _pruned_archive(store)
        # Standalone decisions keep the scope of the adapter that stored them.
        # One revision seen under several scopes shares one entry: strongest
        # decision wins the inventory (selected > uncertain > noise), so the
        # cut never depends on metadata scan order.
        rank = {"selected": 3, "uncertain": 2, "noise": 1}
        decisions = {}
        adapter_keys = sorted(row[0] for row in store.db.execute(
            "SELECT key FROM metadata WHERE key LIKE 'source-sync:google:%'"))
        for key in adapter_keys:
            adapter = json.loads(store.db.execute(
                "SELECT value FROM metadata WHERE key=?", (key,)).fetchone()[0])
            if not isinstance(adapter, dict):
                continue
            scope = (adapter.get("partition") or {})
            for choice in (adapter.get("decisions") or {}).values():
                if (isinstance(choice, dict) and choice.get("external_id")
                        and choice.get("revision")
                        and choice.get("classification") in rank):
                    full = (scope.get("provider"), scope.get("account"),
                            scope.get("collection"), choice["external_id"],
                            choice["revision"])
                    if rank[choice["classification"]] >= rank.get(
                            decisions.get(full, {}).get("classification"), 0):
                        decisions[full] = choice
        index_keys = [row[0] for row in store.db.execute(
            "SELECT key FROM metadata WHERE key LIKE 'source-sync:object:%'")]
        migrated = skipped_existing = skipped_pruned = standalone = merged_scope = 0
        # One revision observed under several scopes shares one entry (scope
        # is not identity): a selection in any scope wins, with precedence
        # selected > uncertain > noise > pending, and the first affair link
        # fills a missing one. Availability follows the same precedence.
        precedence = {"selected": 4, "uncertain": 3, "noise": 2, "pending": 1,
                      "unavailable": 1, "deleted": 1}

        def insert(provider, account, collection, external_id, revision, status,
                   digest, item_id, metadata, observed):
            nonlocal migrated, skipped_existing, skipped_pruned, merged_scope
            row_id = entry_id(provider, account, collection, external_id, revision)
            if row_id in archived:
                skipped_pruned += 1
                return
            current = store.db.execute(
                "SELECT status, original_digest, item_id, metadata_json FROM source_entries"
                " WHERE id=?", (row_id,)).fetchone()
            if current is not None:
                skipped_existing += 1
                updates, params = [], []
                if precedence.get(status, 0) > precedence.get(current["status"], 0):
                    updates.append("status=?")
                    params.append(status)
                    merged_scope += 1
                if current["original_digest"] is None and digest is not None:
                    updates.append("original_digest=?")
                    params.append(digest)
                if current["item_id"] is None and item_id is not None:
                    updates.append("item_id=?")
                    params.append(item_id)
                stored_meta = json.loads(current["metadata_json"])
                if metadata.get("reason_code") and not stored_meta.get("reason_code"):
                    stored_meta["reason_code"] = metadata["reason_code"]
                    updates.append("metadata_json=?")
                    params.append(encode(stored_meta))
                if updates:
                    params.append(row_id)
                    store.db.execute(
                        "UPDATE source_entries SET " + ", ".join(updates) + " WHERE id=?",
                        params)
                return
            if not isinstance(observed, str) or not observed:
                raise ValueError(f"unrepresentable_source:{external_id}")
            store.db.execute(
                "INSERT INTO source_entries(id, provider, account, collection, external_id,"
                " revision, status, original_digest, item_id, metadata_json, observed_at)"
                " VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                (row_id, provider, account, collection, external_id, revision, status,
                 digest, item_id, encode(metadata), observed))
            migrated += 1

        for index_key in index_keys:
            record = json.loads(store.db.execute(
                "SELECT value FROM metadata WHERE key=?", (index_key,)).fetchone()[0])
            for event in record.get("versions", []):
                partition = event.get("partition") or {}
                provider = partition.get("provider")
                account = partition.get("account")
                collection = partition.get("collection")
                external_id = record.get("external_id")
                document = event.get("document") or {}
                revision = document.get("revision")
                if (not isinstance(provider, str) or not provider
                        or not isinstance(account, str) or not account
                        or not isinstance(collection, str) or not collection
                        or not isinstance(external_id, str) or not external_id
                        or not isinstance(revision, str) or not revision):
                    raise ValueError(f"unrepresentable_source:{external_id}")
                if document.get("status") not in {"present", "deleted", "degraded"}:
                    raise ValueError(f"unrepresentable_source:{external_id}")
                original = event.get("original") or {}
                digest = original.get("sha256")
                if digest is not None and not store.db.execute(
                        "SELECT 1 FROM originals WHERE digest=?", (digest,)).fetchone():
                    raise ValueError(f"source_original_missing:{external_id}")
                choice = decisions.get((provider, account, collection, external_id, revision))
                if choice is not None:
                    status, reason = choice["classification"], choice.get("reason_code")
                else:
                    status = {"present": "pending", "deleted": "deleted",
                              "degraded": "unavailable"}[document["status"]]
                    reason = None
                is_latest = (event == record["versions"][-1])
                metadata = {"index_key": index_key, "sequence": event.get("sequence"),
                            "availability": document["status"],
                            "projection": event.get("projection", "pending"),
                            "scope": "migrated"}
                if reason is not None:
                    metadata["reason_code"] = reason
                insert(provider, account, collection, external_id, revision, status,
                       digest, record.get("item_id") if is_latest else None, metadata,
                       event.get("observed_at"))
        # Standalone decisions: durable selections without any projected object.
        for (provider, account, collection, external_id, revision), choice in sorted(decisions.items()):
            if (not isinstance(provider, str) or not provider
                    or not isinstance(account, str) or not account
                    or not isinstance(collection, str) or not collection):
                raise ValueError(f"unrepresentable_decision_scope:{external_id}")
            row_id = entry_id(provider, account, collection, external_id, revision)
            if row_id in archived:
                skipped_pruned += 1
                continue
            current = store.db.execute(
                "SELECT status, metadata_json FROM source_entries WHERE id=?",
                (row_id,)).fetchone()
            if current is not None:
                skipped_existing += 1
                if precedence.get(choice["classification"], 0) > precedence.get(current["status"], 0):
                    metadata = json.loads(current["metadata_json"])
                    if choice.get("reason_code"):
                        metadata["reason_code"] = choice["reason_code"]
                    store.db.execute(
                        "UPDATE source_entries SET status=?, metadata_json=? WHERE id=?",
                        (choice["classification"], encode(metadata), row_id))
                    merged_scope += 1
                continue
            # Standalone decisions never recorded their decision time;
            # NULL marks unknown (new rows always carry time instead).
            observed = choice.get("decided_at") or choice.get("observed_at")
            store.db.execute(
                "INSERT INTO source_entries(id, provider, account, collection, external_id,"
                " revision, status, original_digest, item_id, metadata_json, observed_at)"
                " VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                (row_id, provider, account, collection, external_id, revision,
                 choice["classification"], None, None,
                 encode({"reason_code": choice.get("reason_code"),
                         "scope": "migrated-standalone-decision"}), observed))
            migrated += 1
            standalone += 1
        if migrated == 0:
            return {"note": "already_migrated", "skipped_existing": skipped_existing,
                    "skipped_pruned": skipped_pruned}
        receipt = {"schema": 4, "migrated_source_entries": migrated,
                   "skipped_existing": skipped_existing, "skipped_pruned": skipped_pruned,
                   "merged_scope": merged_scope,
                   "standalone_decisions": standalone,
                   "at": datetime.now(timezone.utc).isoformat()}
        store.db.execute("INSERT OR REPLACE INTO metadata VALUES('migration:i3',?)", (encode(receipt),))
        return receipt
