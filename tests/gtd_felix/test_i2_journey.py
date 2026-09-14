"""I2 journey: conversation identity, correction, pause/return, devolution.

Synthetic transports only: no paid model calls, no real Telegram sends. The
principal's wording choices (relative dates, thread linking) belong to the
prepared human run (NOT_RUN here); these tests pin the service plumbing that
must conserve identity, scope, deadlines and precisions either way.
"""
import asyncio
import unittest
import test_telegram as fixtures
from gtd_felix.orchestration import OrchestrationWorker


LOOK_AFTER_MONDAY = "2026-09-21"


def run(coro):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


class ConversationIdentityTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.TelegramTests()
        self.fixture.setUp()
        self.service = self.fixture.service
        self.adapter = self.fixture.adapter

    def tearDown(self):
        self.fixture.tearDown()

    def clarify_action(self, item, operation, outcome="Resultado útil", criteria="Criterio comprobable"):
        receipt = self.service.execute("felix", {"operation_id": operation, "action": "clarify",
            "item_id": item["id"], "expected_version": item["version"],
            "fields": {"kind": "action", "commitment": "committed", "outcome": outcome,
                       "completion_criteria": criteria}})
        self.assertEqual(receipt["status"], "applied", receipt)
        return receipt["item"]

    def test_fronts_deadline_and_precisions_conserve_identity(self):
        tele = self.clarify_action(
            self.service.capture("felix", "i2-tele", "Poner al día Telemedicina: responsabilidades")["item"],
            "i2-clarify-tele")
        hodom = self.clarify_action(
            self.service.capture("felix", "i2-hodom", "Poner al día HODOM: pendientes")["item"],
            "i2-clarify-hodom")
        saneo = self.clarify_action(
            self.service.capture("felix", "i2-saneo", "Saneo de asistencia personal")["item"],
            "i2-clarify-saneo")
        before = {item["id"]: (item["version"], item["text"], item["title"]) for item in (tele, hodom, saneo)}
        # "Antes del próximo lunes": one explicit deadline per known affair.
        for item in (tele, hodom, saneo):
            current = self.service.get_item(item["id"])
            receipt = self.service.execute("felix", {"operation_id": "i2-due-" + item["id"][:8],
                "action": "edit", "item_id": item["id"], "expected_version": current["version"],
                "fields": {"due_at": LOOK_AFTER_MONDAY}})
            self.assertEqual(receipt["status"], "applied", receipt)
        for item_id, (version, text, title) in before.items():
            current = self.service.get_item(item_id)
            self.assertEqual(current["due_at"], LOOK_AFTER_MONDAY)
            self.assertEqual(current["version"], version + 1)
            self.assertEqual((current["text"], current["title"]), (text, title))
        # Precision: the saneo belongs to Félix's own assistance.
        saneo_now = self.service.get_item(saneo["id"])
        receipt = self.service.execute("felix", {"operation_id": "i2-saneo-scope", "action": "edit",
            "item_id": saneo["id"], "expected_version": saneo_now["version"],
            "fields": {"title": "Saneo de la asistencia de Félix", "text": "Saneo de la asistencia de Félix"}})
        self.assertEqual(receipt["status"], "applied", receipt)
        for other in (tele["id"], hodom["id"]):
            untouched = self.service.get_item(other)
            self.assertEqual(untouched["due_at"], LOOK_AFTER_MONDAY)
            self.assertNotIn("Félix", untouched["title"] + untouched["text"])
        # Per-front background periods, one front at a time.
        notes = {tele["id"]: "Telemedicina: turnos enero-marzo",
                 hodom["id"]: "HODOM: episodio febrero",
                 saneo["id"]: "Asistencia: marzo en curso"}
        for item_id, note in notes.items():
            current = self.service.get_item(item_id)
            receipt = self.service.execute("felix", {"operation_id": "i2-note-" + item_id[:8],
                "action": "edit", "item_id": item_id, "expected_version": current["version"],
                "fields": {"notes": note}})
            self.assertEqual(receipt["status"], "applied", receipt)
        for item_id, note in notes.items():
            self.assertEqual(self.service.get_item(item_id)["notes"], note)
        self.assertEqual(self.service.get_item(saneo["id"])["title"], "Saneo de la asistencia de Félix")

    def test_unrelated_message_stays_a_separate_affair(self):
        first = self.clarify_action(
            self.service.capture("felix", "i2-first", "Poner al día Telemedicina")["item"], "i2-first-clarify")
        count = len(self.service.query())
        other = self.service.capture("felix", "i2-other", "Comprar café")["item"]
        self.assertEqual(len(self.service.query()), count + 1)
        self.assertEqual(other["kind"], "capture")
        self.assertNotEqual(other["id"], first["id"])
        self.assertEqual(other.get("relations", []), [])

    def test_correction_invalidates_old_material_and_devolution_references_current(self):
        item = self.clarify_action(
            self.service.capture("felix", "i2-mat", "Mapa de responsabilidades")["item"], "i2-mat-clarify")
        item = self.service.execute("felix", {"operation_id": "i2-mat-v1", "action": "put_material",
            "item_id": item["id"], "expected_version": item["version"],
            "fields": {"content": "Borrador con dato viejo", "title": "Mapa"}})["item"]
        v1 = self.service.materials(item["id"])[-1]
        self.assertTrue(v1["valid"])
        current = self.service.get_item(item["id"])
        item = self.service.execute("felix", {"operation_id": "i2-mat-fix", "action": "edit",
            "item_id": item["id"], "expected_version": current["version"],
            "fields": {"text": "Mapa de responsabilidades corregido"}})["item"]
        self.assertFalse([m for m in self.service.materials(item["id"]) if m["id"] == v1["id"]][0]["valid"])
        item = self.service.execute("felix", {"operation_id": "i2-mat-v2", "action": "put_material",
            "item_id": item["id"], "expected_version": item["version"],
            "fields": {"content": "Mapa corregido y vigente", "title": "Mapa",
                       "material_id": v1["id"]}})["item"]
        live = [m for m in self.service.materials(item["id"]) if m["valid"]]
        self.assertEqual([(m["id"], m["version"]) for m in live], [(v1["id"], 2)])
        event = {"payload": {"item_id": item["id"], "version": item["version"], "text": item["title"]}}
        text = "\n".join(self.adapter._notification_content(event))
        self.assertIn("Mapa corregido y vigente", text)
        self.assertNotIn("dato viejo", text)

    def test_pause_blocks_agent_work_and_return_shows_current_material(self):
        item = self.clarify_action(
            self.service.capture("felix", "i2-pause", "Encargo en curso")["item"], "i2-pause-clarify")
        item = self.service.execute("felix", {"operation_id": "i2-pause-mat", "action": "put_material",
            "item_id": item["id"], "expected_version": item["version"],
            "fields": {"content": "Avance parcial útil", "title": "Avance"}})["item"]
        current = self.service.get_item(item["id"])
        paused = self.service.execute("felix", {"operation_id": "i2-pause-now", "action": "pause",
            "item_id": item["id"], "expected_version": current["version"], "fields": {}})["item"]
        self.assertEqual(paused["status"], "paused")
        blocked = self.service.execute("gtd-felix", {"operation_id": "i2-paused-plan", "action": "plan",
            "item_id": item["id"], "expected_version": paused["version"],
            "fields": {"plan_steps": ["Seguir igual"]}})
        self.assertEqual(blocked["error"], "work_paused", blocked)
        resumed = self.service.execute("felix", {"operation_id": "i2-resume", "action": "reopen",
            "item_id": item["id"], "expected_version": paused["version"], "fields": {}})["item"]
        self.assertEqual(resumed["status"], "active")
        live = [m for m in self.service.materials(item["id"]) if m["valid"]]
        self.assertEqual(len(live), 1)
        self.assertEqual(
            self.service.read_material(item["id"], live[0]["id"], live[0]["version"])["content"],
            "Avance parcial útil")

    def test_due_date_surfaces_as_authorized_return(self):
        item = self.clarify_action(
            self.service.capture("felix", "i2-due", "Asunto con plazo")["item"], "i2-due-clarify")
        current = self.service.get_item(item["id"])
        item = self.service.execute("felix", {"operation_id": "i2-due-set", "action": "edit",
            "item_id": item["id"], "expected_version": current["version"],
            "fields": {"due_at": "2026-01-05"}})["item"]
        returns = {entry["item_id"]: entry for entry in self.service.review_state()["returns"]}
        self.assertEqual(returns[item["id"]]["due_at"], "2026-01-05")
        from gtd_felix.control import ExecutionControl
        from datetime import datetime, timezone
        control = ExecutionControl(self.service, dict(
            period_start=datetime.now(timezone.utc).isoformat(), period_seconds=3600,
            max_cost_usd=10, max_runtime_seconds=1000, recovery_cost_usd=0,
            recovery_runtime_seconds=0, max_job_runtime_seconds=500, max_retries=0,
            max_descendants=0, max_active=1))
        worker = OrchestrationWorker(self.service, control, None, {"timezone": "America/Santiago"})
        before = len(self.service.pending_events("gtd-review", "local"))
        worker._temporal_return(self.service.get_item(item["id"]), "due_at", "2026-01-05",
                                1780000000.0 + 10 * 86400)
        after = self.service.pending_events("gtd-review", "local")
        self.assertEqual(len(after), before + 1)
        self.assertEqual(after[-1]["payload"]["field"], "due_at")
        future = len(self.service.pending_events("gtd-review", "local"))
        worker._temporal_return(self.service.get_item(item["id"]), "due_at", "2036-05-05", 1780000000.0)
        self.assertEqual(len(self.service.pending_events("gtd-review", "local")), future)

    def test_long_material_is_fully_reachable_in_chunks(self):
        item = self.clarify_action(
            self.service.capture("felix", "i2-long", "Informe extenso")["item"], "i2-long-clarify")
        body = "".join(f"Hecho verificado {index:04d}. " for index in range(400))
        item = self.service.execute("felix", {"operation_id": "i2-long-mat", "action": "put_material",
            "item_id": item["id"], "expected_version": item["version"],
            "fields": {"content": body, "title": "Informe"}})["item"]
        event = {"payload": {"item_id": item["id"], "version": item["version"], "text": item["title"]}}
        chunks = self.adapter._notification_content(event)
        self.assertGreater(len(chunks), 1)
        joined = "".join(chunk.split("] ", 1)[1] for chunk in chunks)
        self.assertIn(body[:200], joined)
        self.assertIn(body[-200:], joined)


class BatchFifteenTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.TelegramTests()
        self.fixture.setUp()
        self.service = self.fixture.service
        self.adapter = self.fixture.adapter

    def tearDown(self):
        self.fixture.tearDown()

    def clarify_many(self, count):
        ids = []
        for index in range(count):
            capture = self.service.capture("felix", f"i2-batch-{index}", f"Asunto {index:02d}")["item"]
            receipt = self.service.execute("felix", {"operation_id": f"i2-batch-clarify-{index}",
                "action": "clarify", "item_id": capture["id"], "expected_version": capture["version"],
                "fields": {"kind": "action", "commitment": "committed", "outcome": f"Resultado {index:02d}",
                           "completion_criteria": f"Criterio {index:02d}"}})
            self.assertEqual(receipt["status"], "applied", receipt)
            ids.append((receipt["item"]["id"], receipt["item"]["version"]))
        return ids

    def test_fifteen_affairs_batch_with_individual_results(self):
        ids = self.clarify_many(15)
        done = run(self.adapter._batch(
            [{"item_id": item_id, "expected_version": version} for item_id, version in ids[:4]],
            "done", "i2-batch-done"))
        self.assertIn("Lote: 4/4 aplicados", self.fixture.http.sent[-1]["text"])
        postponed = run(self.adapter._batch(
            [{"item_id": item_id, "expected_version": version} for item_id, version in ids[4:6]],
            "postpone", "i2-batch-post", {"review_at": "2026-10-01"}))
        self.assertIsNone(postponed)
        for item_id, _ in ids[:4]:
            self.assertEqual(self.service.get_item(item_id)["status"], "done")
        for item_id, _ in ids[4:6]:
            current = self.service.get_item(item_id)
            self.assertEqual(current["status"], "postponed")
            self.assertEqual(current["review_at"], "2026-10-01")
        rest = [self.service.get_item(item_id) for item_id, _ in ids[6:]]
        self.assertEqual(len(rest), 9)
        for item in rest:
            self.assertEqual(item["status"], "active")
            self.assertIsNone(item.get("review_at"))

    def test_list_pagination_and_navigation_create_nothing(self):
        self.clarify_many(7)
        count = len(self.service.query())
        page0 = run(self.adapter.show_list(0))
        page1 = run(self.adapter.show_list(1))
        self.assertTrue(page0 and page1)
        self.assertEqual({item["id"] for item in page0} & {item["id"] for item in page1}, set())
        self.assertEqual(len(self.service.query()), count)
        first = page0[0]
        run(self.adapter.show_item(first))
        run(self.adapter.show_item(first, more=True))
        self.assertEqual(len(self.service.query()), count)


class DeliveriesTableTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.TelegramTests()
        self.fixture.setUp()
        self.service = self.fixture.service
        self.adapter = self.fixture.adapter
        self.http = self.fixture.http

    def tearDown(self):
        self.fixture.tearDown()

    def _send_under_event(self, event_key, text):
        token = self.adapter._outbound_context.set([event_key, 0])
        try:
            return run(self.adapter._call("sendMessage", {"chat_id": 9, "text": text}))
        finally:
            self.adapter._outbound_context.reset(token)

    def test_send_intent_is_idempotent_without_second_post(self):
        first = self._send_under_event("evt-replay", "Hola")
        replayed = self._send_under_event("evt-replay", "Hola")
        posts = [c for c in self.http.calls if c[0] == "sendMessage"]
        self.assertEqual(len(posts), 1)
        self.assertEqual(replayed, first)
        self.assertIn("message_id", first)
        rows = self.service.store.db.execute(
            "SELECT state FROM deliveries WHERE channel='telegram'").fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["state"], "confirmed")

    def test_uncertain_send_never_reposts_on_reprocessing(self):
        calls = {"sendMessage": 0}
        real_call = self.http.request

        def flaky(method, url, *, json=None, timeout=None):
            if method == "POST" and url.rsplit("/", 1)[-1] == "sendMessage":
                calls["sendMessage"] += 1
                if calls["sendMessage"] == 1:
                    raise Exception("transport down")
            return real_call(method, url, json=json, timeout=timeout)

        self.http.request = flaky
        try:
            first = self._send_under_event("evt-flaky", "Uno")
            second = self._send_under_event("evt-flaky", "Uno")
        finally:
            self.http.request = real_call
        self.assertEqual(first, {})
        self.assertEqual(second, {})
        self.assertEqual(calls["sendMessage"], 1)
        rows = self.service.store.db.execute(
            "SELECT state FROM deliveries WHERE channel='telegram'").fetchall()
        self.assertTrue(rows and all(row["state"] == "uncertain" for row in rows))


class MigrationI2Tests(unittest.TestCase):
    def setUp(self):
        import tempfile
        from pathlib import Path
        from gtd_felix.service import GTDService, migrate_i2_results
        self.temp = tempfile.TemporaryDirectory()
        self.service = GTDService(Path(self.temp.name) / "data")
        self.migrate_i2_results = migrate_i2_results

    def tearDown(self):
        self.service.close()
        self.temp.cleanup()

    def test_migrates_arrays_and_outbox_once_with_stubs(self):
        import json as _json
        from gtd_felix.service import migrate_i2_results
        item = self.service.capture("felix", "i2-mig", "Asunto migrable")["item"]
        item = self.service.execute("felix", {"operation_id": "i2-mig-clarify", "action": "clarify",
            "item_id": item["id"], "expected_version": item["version"],
            "fields": {"kind": "action", "commitment": "committed", "completion_criteria": "Criterio"}})["item"]
        # Forge pre-cut document shapes directly: full arrays as the old writer
        # persisted them. New code paths already write stubs (covered above).
        blob = self.service.store.save_original(b"Contenido migrable")
        blob.update(filename="material.txt", mime_type="text/plain; charset=utf-8")
        self.service.store.db.execute("INSERT OR IGNORE INTO originals VALUES(?,?,?)",
            (blob["sha256"], blob["size"], blob["path"]))
        full_material = {"id": "m" * 32, "version": 1, "author": "felix", "title": "Migrable",
            "original": dict(blob), "created_at": "2026-09-14T00:00:00+00:00",
            "basis": {}, "source_versions": {}, "mandate_id": None}
        full_assessment = {"actor": "felix", "satisfied": False, "evidence": "Evidencia migrable",
            "gap": "Brecha", "item_version": item["version"], "source_versions": {},
            "mandate_id": None, "assessed_at": "2026-09-14T00:00:01+00:00",
            "resolution_basis": {}, "material_basis": []}
        with self.service.store.transaction() as db:
            document, _ = self.service._item(item["id"])
            document = dict(document)
            document["materials"] = [full_material]
            document["assessments"] = [full_assessment]
            db.execute("UPDATE items SET document=? WHERE id=?",
                       (_json.dumps(document, sort_keys=True), item["id"]))
        notice = self.service.ingest_event({"provider": "gtd-notification", "account": "local",
            "external_id": "i2-mig-notice", "revision": "1",
            "payload": {"item_id": item["id"], "version": item["version"], "kind": "updated",
                        "text": "Devolución", "delivery": "pending"}})
        with self.service.store.transaction() as db:
            db.execute("INSERT INTO metadata VALUES(?,?)", ("telegram-outbox:fixture",
                __import__("json").dumps({"status": "uncertain", "account": "synthetic-bot",
                    "event": notice["event_key"], "ordinal": 0, "method": "sendMessage",
                    "payload": {"chat_id": 9, "text": "x"}})))
        receipt = migrate_i2_results(self.service.store)
        self.assertEqual(
            (receipt["migrated_materials"], receipt["migrated_assessments"], receipt["migrated_deliveries"]),
            (1, 1, 1))
        stored = self.service.get_item(item["id"])
        self.assertNotIn("basis", stored["materials"][0])
        self.assertNotIn("original", stored["materials"][0])
        self.assertEqual(stored["materials"][0]["digest"], full_material["original"]["sha256"])
        self.assertNotIn("material_basis", stored["assessments"][0])
        self.assertIn("resolution_basis", stored["assessments"][0])
        reread = self.service.materials(item["id"])[0]
        self.assertEqual(reread["original"]["sha256"], full_material["original"]["sha256"])
        # Idempotent re-run and active-work refusal keep the cut safe.
        self.assertEqual(migrate_i2_results(self.service.store)["note"], "already_migrated")

    def test_migration_refuses_with_live_runs(self):
        from gtd_felix.service import migrate_i2_results
        from gtd_felix.control import ExecutionControl
        from datetime import datetime, timezone
        item = self.service.capture("felix", "i2-live", "Asunto vivo")["item"]
        control = ExecutionControl(self.service, dict(
            period_start=datetime.now(timezone.utc).isoformat(), period_seconds=3600,
            max_cost_usd=10, max_runtime_seconds=1000, recovery_cost_usd=0,
            recovery_runtime_seconds=0, max_job_runtime_seconds=500, max_retries=0,
            max_descendants=0, max_active=1))
        control.register_bot("felix", "bot-live", {"id": "b", "state": "available",
            "source_urn": "urn:t", "host": "h", "profile": "p", "capabilities": ["prepare_private"],
            "probe_evidence": "x"})
        receipt = control.reserve("gtd-felix", "live-op", {"item_id": item["id"], "expected_version": 1,
            "capability": "prepare_private", "bot_id": "b", "purpose": "P", "scope": "S",
            "max_cost_usd": 1, "max_runtime_seconds": 60, "max_retries": 0, "max_descendants": 0})
        self.assertEqual(receipt["status"], "reserved", receipt)
        with self.assertRaises(ValueError):
            migrate_i2_results(self.service.store)


if __name__ == "__main__":
    unittest.main()
