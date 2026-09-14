"""E45: offline incorporation of one executor identity into actor_config.

Regression of the E44 install block: reopening a pre-existing base with a
widened executor set fails actor_config_mismatch; the candidate maintenance
operation is the only supported transition. No live state, no inference.
"""
import json
import tempfile
from datetime import datetime, timezone
from pathlib import Path
import sys
import unittest

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from gtd_felix.control import ExecutionControl
from gtd_felix.service import GTDService, incorporate_executor
from gtd_felix.store import Store


OLD = {"owner_actor": "felix", "principal_actor": "gtd-felix", "executor_actors": []}
NEW = "gtd-private-helper"


def metadata(store):
    return {r[0]: json.loads(r[1]) for r in store.db.execute("SELECT key,value FROM metadata")}


def counts(db):
    return {t: db.execute("SELECT COUNT(*) FROM %s" % t).fetchone()[0]
            for t in ("items", "operations", "runs", "work_cycles", "materials",
                      "assessments", "deliveries", "source_entries", "events")}


class IncorporationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "data"

    def tearDown(self):
        self.temp.cleanup()

    def make_base(self):
        service = GTDService(self.root)
        item = service.capture("felix", "cap:1", "Synthetic project")["item"]
        service.close()
        return item["id"]

    def test_transition_real_base(self):
        item_id = self.make_base()
        with self.assertRaises(ValueError) as ctx:
            GTDService(self.root, executor_actors=(NEW,))
        self.assertEqual(str(ctx.exception), "actor_config_mismatch")
        store = Store(self.root)
        try:
            receipt = incorporate_executor(store, "op:1", OLD, NEW)
        finally:
            store.close()
        self.assertEqual(receipt["status"], "applied")
        self.assertEqual(receipt["after"]["executor_actors"], [NEW])
        service = GTDService(self.root, executor_actors=(NEW,))
        try:
            self.assertEqual(service.get_item(item_id)["text"], "Synthetic project")
        finally:
            service.close()

    def test_old_config_rejected_after_change(self):
        self.make_base()
        store = Store(self.root)
        try:
            incorporate_executor(store, "op:1", OLD, NEW)
        finally:
            store.close()
        with self.assertRaises(ValueError) as ctx:
            GTDService(self.root)
        self.assertEqual(str(ctx.exception), "actor_config_mismatch")

    def test_collision_and_invalid_actor_leave_no_changes(self):
        self.make_base()
        for bad in ("felix", "gtd-felix", "", "   ", None, 42):
            store = Store(self.root)
            try:
                before = metadata(store)
                with self.assertRaises(ValueError):
                    incorporate_executor(store, "op:%r" % (bad,), OLD, bad)
                self.assertEqual(metadata(store), before)
            finally:
                store.close()

    def test_wrong_precondition_leaves_no_changes(self):
        self.make_base()
        store = Store(self.root)
        try:
            before = metadata(store)
            wrong = dict(OLD, executor_actors=["someone-else"])
            with self.assertRaises(ValueError) as ctx:
                incorporate_executor(store, "op:1", wrong, NEW)
            self.assertEqual(str(ctx.exception), "actor_config_mismatch")
            self.assertEqual(metadata(store), before)
        finally:
            store.close()

    def test_absent_config_refused(self):
        store = Store(self.root)
        try:
            with self.assertRaises(ValueError) as ctx:
                incorporate_executor(store, "op:1", OLD, NEW)
            self.assertEqual(str(ctx.exception), "actor_config_absent")
        finally:
            store.close()

    def test_repeat_is_idempotent(self):
        self.make_base()
        store = Store(self.root)
        try:
            first = incorporate_executor(store, "op:1", OLD, NEW)
            second = incorporate_executor(store, "op:1", OLD, NEW)
            self.assertEqual(first, second)
            current = json.loads(store.db.execute(
                "SELECT value FROM metadata WHERE key='actor_config'").fetchone()[0])
            self.assertEqual(current["executor_actors"], [NEW])
        finally:
            store.close()

    def test_same_id_different_request_conflicts(self):
        self.make_base()
        store = Store(self.root)
        try:
            incorporate_executor(store, "op:1", OLD, NEW)
            with self.assertRaises(ValueError) as ctx:
                incorporate_executor(store, "op:1", OLD, "other-helper")
            self.assertEqual(str(ctx.exception), "operation_id_conflict")
        finally:
            store.close()

    def test_only_actor_config_and_receipt_change(self):
        self.make_base()
        store = Store(self.root)
        try:
            meta_before, rows_before = metadata(store), counts(store.db)
            incorporate_executor(store, "op:1", OLD, NEW)
            meta_after, rows_after = metadata(store), counts(store.db)
            self.assertEqual(rows_before, rows_after)
            self.assertEqual(set(meta_after) - set(meta_before),
                             {"maintenance:incorporate-executor:op:1"})
            for key, value in meta_before.items():
                if key != "actor_config":
                    self.assertEqual(meta_after[key], value, key)
            self.assertEqual(meta_after["actor_config"]["executor_actors"], [NEW])
        finally:
            store.close()

    def reserve_active(self):
        service = GTDService(self.root)
        config = dict(period_start=datetime.now(timezone.utc).isoformat(), period_seconds=3600,
                      max_cost_usd=10, max_runtime_seconds=1000, recovery_cost_usd=2,
                      recovery_runtime_seconds=100, max_active=2, max_job_runtime_seconds=500,
                      max_retries=1, max_descendants=2)
        control = ExecutionControl(service, config)
        item = service.capture("felix", "cap:2", "Synthetic active")["item"]
        clar = service.execute("felix", dict(operation_id="clarify", action="clarify",
            item_id=item["id"], expected_version=item["version"],
            fields={"kind": "project", "commitment": "committed", "outcome": "O",
                    "completion_criteria": "C"}))
        mand = service.execute("felix", dict(operation_id="mandate", action="grant_mandate",
            item_id=item["id"], expected_version=clar["item"]["version"],
            fields={"scope_item_id": item["id"], "capabilities": ["local_work"],
                    "actors": ["gtd-felix"], "completion_criteria": "C"}))
        control.register_bot("felix", "bot", dict(id="test-bot", state="available",
            source_urn="urn:test:bot", host="synthetic", profile="fixture",
            capabilities=["local_work"], mandate_id=mand["mandate"]["id"],
            item_id=item["id"], probe_evidence="fixture://probe"))
        job = control.reserve("gtd-felix", "reserve", dict(
            item_id=item["id"], expected_version=service.get_item(item["id"])["version"],
            mandate_id=mand["mandate"]["id"], capability="local_work", bot_id="test-bot",
            purpose="Prepare", scope="s", max_cost_usd=4, max_runtime_seconds=200,
            max_retries=0, max_descendants=2))
        self.assertEqual(job["status"], "reserved", job)
        return service

    def test_active_work_blocks_without_changes(self):
        service = self.reserve_active()
        service.close()
        store = Store(self.root)
        try:
            before = metadata(store)
            with self.assertRaises(ValueError) as ctx:
                incorporate_executor(store, "op:1", OLD, NEW)
            self.assertEqual(str(ctx.exception), "active_work_present")
            self.assertEqual(metadata(store), before)
        finally:
            store.close()

    def test_pending_integration_blocks_despite_terminal_state(self):
        service = self.reserve_active()
        job_id = service.store.db.execute(
            "SELECT id FROM runs WHERE state NOT IN ('completed','failed','cancelled','expired')"
            " LIMIT 1").fetchone()[0]
        service.store.db.execute(
            "UPDATE runs SET state='completed', integration='pending' WHERE id=?", (job_id,))
        service.store.db.commit()
        service.close()
        store = Store(self.root)
        try:
            with self.assertRaises(ValueError) as ctx:
                incorporate_executor(store, "op:1", OLD, NEW)
            self.assertEqual(str(ctx.exception), "active_work_present")
        finally:
            store.close()


if __name__ == "__main__":
    unittest.main()
