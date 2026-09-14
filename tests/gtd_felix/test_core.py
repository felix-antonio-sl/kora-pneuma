"""Synthetic acceptance at the real SQLite/filesystem boundary."""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import sqlite3
import stat
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from gtd_felix import GTDService


class CoreTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.service = GTDService(self.root / "data", owner_actor="human:test")
        self.sequence = 0

    def tearDown(self):
        self.service.close()
        self.temp.cleanup()

    def capture(self, title="Synthetic note", **kwargs):
        self.sequence += 1
        result = self.service.capture("human:test", f"capture-{self.sequence}", title, **kwargs)
        self.assertEqual(result["status"], "applied", result)
        return result["item"]

    def command(self, item, action, fields=None, **kwargs):
        self.sequence += 1
        return self.service.execute("human:test", {"operation_id": f"command-{self.sequence}", "item_id": item["id"],
                                    "action": action, "expected_version": item["version"], "fields": fields or {}, **kwargs})

    def action(self, title="Synthetic action"):
        return self.command(self.capture(title), "edit", {"kind": "action"})["item"]

    def restart(self):
        self.service.close()
        self.service = GTDService(self.root / "data", owner_actor="human:test")

    def test_audio_original_durable_before_ack_and_restart(self):
        raw = b"synthetic-audio\x00\xff"
        source = {"provider": "telegram", "chat_id": "synthetic", "message_id": 12}
        item = self.capture("", source=source, original=raw, filename="voice.ogg", mime_type="audio/ogg")
        self.assertEqual((self.service.data_dir / item["original"]["path"]).read_bytes(), raw)
        self.restart()
        recovered = self.service.get_item(item["id"])
        self.assertEqual(recovered["source"], source)
        self.assertEqual((self.service.data_dir / recovered["original"]["path"]).read_bytes(), raw)
        self.assertEqual(recovered["kind"], "capture")

    def test_source_revision_preserves_decisions_and_all_originals(self):
        first_source = {"provider": "test", "message_id": "1", "revision": "1"}
        item = self.capture("Source title", source=first_source, original=b"first-binary", filename="first.bin")
        corrected = self.command(item, "edit", {"title": "Human position", "kind": "action"})["item"]
        updated_source = {**first_source, "revision": "2"}
        receipt = self.service.revise_source("human:test", "source-edit", item["id"], updated_source,
                                             text="New source caption", original=b"second-binary", filename="second.bin")
        self.assertEqual(receipt["status"], "applied")
        self.restart()
        current = self.service.get_item(item["id"])
        self.assertEqual((current["title"], current["kind"], current["status"]), ("Human position", "action", "active"))
        self.assertEqual(current["text"], corrected["text"])
        self.assertEqual(current["source"], updated_source)
        self.assertEqual([revision["text"] for revision in current["source_revisions"]], ["Source title", "New source caption"])
        self.assertEqual([(self.service.data_dir / revision["original"]["path"]).read_bytes()
                          for revision in current["source_revisions"]], [b"first-binary", b"second-binary"])
        replay = self.service.revise_source("human:test", "source-edit", item["id"], updated_source,
                                            text="New source caption", original=b"second-binary", filename="second.bin")
        self.assertEqual(replay["status"], "already_applied")
        self.assertEqual(self.service.revise_source("human:test", "source-edit", item["id"], updated_source,
                                                    original=b"different")["error"], "operation_id_reused")
        archive = self.root / "revisions.zip"
        self.service.export(archive)
        restored = GTDService.restore(archive, self.root / "revisions-restored")
        try:
            self.assertEqual(restored.get_item(item["id"])["source_revisions"], current["source_revisions"])
            for revision in current["source_revisions"]:
                self.assertTrue((restored.data_dir / revision["original"]["path"]).is_file())
        finally:
            restored.close()

    def test_storage_failure_never_confirms_and_transaction_receipt_rolls_back(self):
        with patch.object(self.service.store, "save_original", side_effect=OSError("synthetic disk failure")):
            receipt = self.service.capture("human:test", "disk-fail", "Durable note")
        self.assertEqual(receipt["status"], "uncertain")
        self.assertEqual(self.service.query(), [])
        self.assertEqual(self.service.capture("human:test", "disk-fail", "Durable note")["status"], "applied")
        with patch.object(self.service, "_record", side_effect=sqlite3.OperationalError("synthetic transaction failure")):
            failed = self.service.capture("human:test", "transaction-fail", "Another note")
        self.assertEqual(failed["status"], "uncertain")
        self.restart()
        self.assertEqual(len(self.service.query()), 1)
        recovered = self.service.capture("human:test", "transaction-fail", "Another note")
        self.assertEqual(recovered["status"], "applied")
        self.assertEqual(len(self.service.query()), 2)

    def test_fifteen_four_done_two_postponed_nine_available_after_restart(self):
        items = [self.action(f"Action {n}") for n in range(15)]
        for item in items[:4]:
            self.assertEqual(self.command(item, "done")["status"], "applied")
        for item in items[4:6]:
            receipt = self.command(item, "postpone", {"review_at": "2030-01-01"})
            self.assertEqual(receipt["status"], "applied")
            self.assertNotIn("due_at", receipt["item"])
        self.restart()
        self.assertEqual(len(self.service.query({"kind": "action", "status": "done"})), 4)
        self.assertEqual(len(self.service.query({"kind": "action", "status": "postponed"})), 2)
        self.assertEqual(len(self.service.query({"available": True})), 9)
        self.assertEqual(len(self.service.query({"open": True})), 11)

    def test_capture_and_command_idempotency_and_identity_reuse(self):
        first = self.service.capture("human:test", "stable", "same")
        self.restart()
        self.assertEqual(self.service.capture("human:test", "stable", "same")["status"], "already_applied")
        self.assertEqual(self.service.capture("human:test", "stable", "different")["error"], "operation_id_reused")
        self.assertEqual(self.service.capture("agent:test", "stable", "same")["error"], "operation_id_reused")
        cmd = {"operation_id": "cmd", "action": "edit", "item_id": first["item"]["id"], "expected_version": 1, "fields": {"title": "changed"}}
        self.assertEqual(self.service.execute("human:test", cmd)["status"], "applied")
        self.assertEqual(self.service.execute("human:test", cmd)["status"], "already_applied")
        cmd["fields"] = {"title": "new attempt"}
        self.assertEqual(self.service.execute("human:test", cmd)["error"], "operation_id_reused")
        self.assertEqual(len(self.service.query()), 1)

    def test_stale_compatible_and_incompatible_changes(self):
        item = self.action()
        corrected = self.command(item, "edit", {"title": "Human corrected meaning"})["item"]
        compatible = self.command(item, "edit", {"notes": "Independent agent note"})
        self.assertEqual(compatible["status"], "applied")
        self.assertEqual(compatible["item"]["title"], corrected["title"])
        conflict = self.command(item, "edit", {"title": "Old inferred meaning"})
        self.assertEqual(conflict["status"], "conflict")
        self.assertIn("title", conflict["difference"])
        self.assertEqual(self.command(item, "done")["status"], "conflict")
        self.assertEqual(self.service.get_item(item["id"])["status"], "active")

    def test_stale_done_allows_independent_notes(self):
        item = self.action()
        self.command(item, "edit", {"notes": "Independent context"})
        done = self.command(item, "done")
        self.assertEqual(done["status"], "applied")
        self.assertEqual(done["item"]["status"], "done")
        self.assertEqual(done["item"]["notes"], "Independent context")

    def test_undo_preserves_later_independent_human_change(self):
        item = self.action()
        edited = self.command(item, "edit", {"notes": "Temporary enrichment"})
        later = self.command(edited["item"], "edit", {"title": "Human correction"})
        undone = self.command(later["item"], "undo", {"operation_id": edited["operation_id"]})
        self.assertEqual(undone["status"], "applied")
        self.assertEqual(undone["item"]["title"], "Human correction")
        self.assertNotIn("notes", undone["item"])

    def test_undo_rejects_same_field_change_even_if_value_returns(self):
        item = self.action()
        edited = self.command(item, "edit", {"notes": "Agent text"})
        human = self.command(edited["item"], "edit", {"notes": "Human text"})
        restored = self.command(human["item"], "edit", {"notes": "Agent text"})
        undone = self.command(restored["item"], "undo", {"operation_id": edited["operation_id"]})
        self.assertEqual(undone["status"], "conflict")
        self.assertEqual(self.service.get_item(item["id"])["notes"], "Agent text")

    def test_events_cursor_edits_and_recovery(self):
        event = {"provider": "synthetic", "account": "test", "external_id": "1", "revision": 0, "payload": {"text": "note"}}
        receipt = self.service.ingest_event(event)
        self.assertEqual(receipt["status"], "received")
        self.service.set_cursor("synthetic", "test", "2")
        self.service.mark_event(receipt["event_key"], "processing")
        self.restart()
        self.assertEqual(self.service.get_cursor("synthetic", "test"), "2")
        pending = self.service.pending_events("synthetic", "test")
        self.assertEqual(pending[0]["payload"], event["payload"])
        self.assertTrue(self.service.ingest_event(event)["duplicate"])
        changed = {**event, "payload": {"text": "edit"}}
        self.assertEqual(self.service.ingest_event(changed)["error"], "event_identity_reused")
        changed["revision"] = 1
        self.assertEqual(self.service.ingest_event(changed)["status"], "received")
        self.service.mark_event(receipt["event_key"], "applied")
        self.assertEqual(len(self.service.pending_events("synthetic", "test")), 1)
        with self.assertRaises(ValueError):
            self.service.mark_event(receipt["event_key"], "received")

    def test_export_restore_originals_receipts_events_and_private_mode(self):
        item = self.capture("", original=b"synthetic-voice", filename="voice.ogg")
        action = self.action()
        receipt = self.command(action, "done")
        self.service.ingest_event({"provider": "test", "account": "test", "external_id": 1, "revision": 0, "payload": {"a": 1}})
        self.service.set_cursor("test", "test", "2")
        archive = self.root / "backup.zip"
        exported = self.service.export(archive)
        self.assertEqual(exported["coverage"]["items"], 2)
        self.assertEqual(stat.S_IMODE(archive.stat().st_mode), 0o600)
        restored = GTDService.restore(archive, self.root / "restored")
        try:
            self.assertEqual(restored.query(), self.service.query())
            self.assertEqual((restored.data_dir / item["original"]["path"]).read_bytes(), b"synthetic-voice")
            self.assertEqual(restored.get_cursor("test", "test"), "2")
            self.assertEqual(len(restored.pending_events("test", "test")), 1)
            self.assertTrue(restored.recovery_required)
            undone = restored.execute("human:test", {"operation_id": "after-restore", "action": "undo", "fields": {"operation_id": receipt["operation_id"]}})
            self.assertEqual(undone["status"], "applied")
            self.assertEqual(undone["item"]["status"], "active")
            for path in restored.data_dir.rglob("*"):
                self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o700 if path.is_dir() else 0o600)
        finally:
            restored.close()
        with self.assertRaises(ValueError):
            GTDService.restore(archive, self.root / "restored")

    def test_path_traversal_symlinks_and_tampered_backup_rejected(self):
        for filename in ("../outside", "/absolute", "a/b", "a\\b", ".", ".."):
            self.assertEqual(self.service.capture("human:test", f"bad-{filename}", "note", original=b"x", filename=filename)["status"], "rejected")
        outside = self.root / "outside"
        outside.mkdir()
        link = self.root / "link"
        link.symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ValueError):
            GTDService(link)
        evil = self.root / "evil.zip"
        with zipfile.ZipFile(evil, "w") as archive:
            archive.writestr("../outside.txt", "bad")
        with self.assertRaises(ValueError):
            GTDService.restore(evil, self.root / "bad")
        self.assertFalse((self.root / "outside.txt").exists())
        self.capture()
        archive = self.root / "backup.zip"
        self.service.export(archive)
        tampered = self.root / "tampered.zip"
        with zipfile.ZipFile(archive) as source, zipfile.ZipFile(tampered, "w") as target:
            for name in source.namelist():
                target.writestr(name, b"damaged" if name == "gtd.sqlite3" else source.read(name))
        with self.assertRaises(ValueError):
            GTDService.restore(tampered, self.root / "bad")
        self.assertFalse((self.root / "bad").exists())

    def test_migration_reopen_and_reject_future_schema(self):
        # I3: schema is now v4 (source_entries); old code rejects
        # newer_schema, new code rejects future versions.
        self.assertEqual(self.service.store.db.execute("PRAGMA user_version").fetchone()[0], 4)
        self.capture()
        self.restart()
        self.assertEqual(len(self.service.query()), 1)
        future = self.root / "future"
        future.mkdir()
        db = sqlite3.connect(future / "gtd.sqlite3")
        db.execute("PRAGMA user_version=999")
        db.close()
        with self.assertRaisesRegex(ValueError, "newer_schema"):
            GTDService(future)

    def test_project_is_not_completed_by_its_last_action_and_dependencies(self):
        project = self.command(self.capture("Synthetic outcome"), "edit", {"kind": "project", "outcome": "Verified outcome"})["item"]
        first = self.action("First")
        second = self.command(self.action("Second"), "edit", {"project_id": project["id"], "depends_on": [first["id"]]})["item"]
        self.assertNotIn(second["id"], {item["id"] for item in self.service.query({"available": True})})
        self.command(first, "done")
        self.assertIn(second["id"], {item["id"] for item in self.service.query({"available": True})})
        self.command(second, "done")
        self.assertEqual(self.service.get_item(project["id"])["status"], "active")
        self.assertEqual(self.command(first, "edit", {"depends_on": [second["id"]]})["error"], "dependency_cycle")

    def test_withdraw_reopen_and_original_kept(self):
        item = self.action()
        withdrawn = self.command(item, "withdraw")["item"]
        self.assertEqual(withdrawn["status"], "withdrawn")
        self.assertTrue((self.service.data_dir / item["original"]["path"]).exists())
        reopened = self.command(withdrawn, "reopen")["item"]
        self.assertEqual(reopened["status"], "active")
        self.assertNotIn("completed_at", withdrawn)

    def test_independent_connections_same_operation_one_commit(self):
        def run(_):
            service = GTDService(self.root / "data", owner_actor="human:test")
            try:
                return service.capture("human:test", "race", "One note")
            finally:
                service.close()
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            receipts = list(pool.map(run, range(4)))
        self.assertEqual(sorted(receipt["status"] for receipt in receipts), ["already_applied"] * 3 + ["applied"])
        self.assertEqual(len(self.service.query()), 1)

    def test_invalid_date_and_fields_are_durable_rejections(self):
        item = self.action()
        invalid = self.command(item, "postpone", {"review_at": "2030-01-01T10:00:00"})
        self.assertEqual(invalid["status"], "rejected")
        self.assertEqual(self.command(item, "edit", {"version": 9000})["status"], "rejected")
        self.assertEqual(self.service.get_item(item["id"])["version"], item["version"])


if __name__ == "__main__":
    unittest.main()
