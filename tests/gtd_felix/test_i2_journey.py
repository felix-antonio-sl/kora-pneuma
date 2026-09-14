"""I2 journey: conversation identity, correction, pause/return, devolution.

Synthetic transports only: no paid model calls, no real Telegram sends. The
principal's wording choices (relative dates, thread linking) belong to the
prepared human run (NOT_RUN here); these tests pin the service plumbing that
must conserve identity, scope, deadlines and precisions either way.
"""
import asyncio
import json
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


class UndoRedoTests(unittest.TestCase):
    """Inverting an undo restores exact rows, never dangling stubs."""

    def setUp(self):
        self.fixture = fixtures.TelegramTests()
        self.fixture.setUp()
        self.service = self.fixture.service

    def tearDown(self):
        self.fixture.tearDown()

    def _action(self, tag):
        capture = self.service.capture("felix", f"i2-redo-{tag}", "Sonda")["item"]
        return self.service.execute("felix", {"operation_id": f"i2-redo-{tag}-clarify", "action": "clarify",
            "item_id": capture["id"], "expected_version": capture["version"],
            "fields": {"kind": "action", "commitment": "committed", "outcome": "O",
                       "completion_criteria": "C"}})["item"]

    def _do(self, item, operation, action, fields):
        receipt = self.service.execute("felix", {"operation_id": operation, "action": action,
            "item_id": item["id"], "expected_version": item["version"], "fields": fields})
        self.assertEqual(receipt["status"], "applied", receipt)
        return self.service.get_item(item["id"])

    def test_undo_of_undo_restores_readable_material(self):
        item = self._action("rr1")
        item = self._do(item, "i2-rr1-put", "put_material",
                        {"content": "Contenido conservable", "title": "Material"})
        original = self.service.materials(item["id"])[-1]
        item = self._do(item, "i2-rr1-undo", "undo", {"operation_id": "i2-rr1-put"})
        self.assertEqual(self.service.materials(item["id"]), [])
        item = self._do(item, "i2-rr1-redo", "undo", {"operation_id": "i2-rr1-undo"})
        live = self.service.materials(item["id"])
        self.assertEqual([(m["id"], m["version"]) for m in live], [(original["id"], 1)])
        self.assertEqual(live[0]["original"]["sha256"], original["original"]["sha256"])
        read = self.service.read_material(item["id"], original["id"], 1)
        self.assertIn("Contenido conservable", read["content"])

    def test_redo_then_undo_again_prunes_without_resurrecting(self):
        item = self._action("cyc")
        item = self._do(item, "i2-cyc-put", "put_material",
                        {"content": "v1", "title": "T"})
        item = self._do(item, "i2-cyc-undo", "undo", {"operation_id": "i2-cyc-put"})
        item = self._do(item, "i2-cyc-redo", "undo", {"operation_id": "i2-cyc-undo"})
        self.assertEqual(len(self.service.materials(item["id"])), 1)
        item = self._do(item, "i2-cyc-undo2", "undo", {"operation_id": "i2-cyc-redo"})
        self.assertEqual(self.service.materials(item["id"]), [])
        self.assertNotIn("materials", self.service.get_item(item["id"]))

    def test_redo_survives_restart(self):
        item = self._action("rst")
        item = self._do(item, "i2-rst-put", "put_material",
                        {"content": "Durable", "title": "T"})
        item = self._do(item, "i2-rst-undo", "undo", {"operation_id": "i2-rst-put"})
        self.fixture.restart()
        self.service = self.fixture.service
        self.adapter = self.fixture.adapter
        item = self.service.get_item(item["id"])
        item = self._do(item, "i2-rst-redo", "undo", {"operation_id": "i2-rst-undo"})
        live = self.service.materials(item["id"])
        self.assertEqual(len(live), 1)
        self.assertEqual(live[0]["original"]["sha256"],
                         self.service.materials(item["id"])[0]["original"]["sha256"])


class RecentHumanContextTests(unittest.TestCase):
    """Boundary: the evidence handed to the native worker after a reply.

    Same-chat messages, replies and prior affairs are preserved as evidence
    with durable identity; selection uses account/chat/date/message order,
    never wording similarity, and grants no command authority.
    """

    def setUp(self):
        self.fixture = fixtures.TelegramTests()
        self.fixture.setUp()
        self.service = self.fixture.service
        self.adapter = self.fixture.adapter

    def tearDown(self):
        self.fixture.tearDown()

    def _tg(self, message_id, text, date=100, **extra):
        return {"message_id": message_id, "date": date, "chat": {"id": 9},
                "from": {"id": 7}, "text": text, **extra}

    def test_reply_and_continuation_reach_worker_as_bounded_evidence(self):
        run(self.adapter._message(self._tg(7401, "Poner al día Telemedicina"), "ev-7401"))
        # Reply to a devolution: quoted text travels as evidence, not as a merge order.
        run(self.adapter._message(self._tg(7402, "Agrega el turno noche", date=200,
            reply_to_message={"message_id": 7500, "text": "Devolución: mapa listo"}), "ev-7402"))
        # Same wording elsewhere is another entry, never deduped by similarity.
        run(self.adapter._message(self._tg(7403, "Poner al día Telemedicina", date=300), "ev-7403"))
        # Another chat never leaks into this conversation.
        run(self.adapter._message(dict(self._tg(7404, "Poner al día Telemedicina", date=400),
                                       chat={"id": 77}), "ev-7404"))
        worker = OrchestrationWorker(self.service, None, None, {"timezone": "America/Santiago"})
        anchor = next(i for i in self.service.query() if i.get("source", {}).get("message_id") == 7403)
        job = {"human_instruction_source_ids": [i["id"] for i in self.service.query()
               if i.get("source", {}).get("chat_id") == 9]}
        entries = worker._recent_human_context(anchor, job)
        by_message = {e["message_id"]: e for e in entries}
        # The anchor affair itself is the subject (context['item']); strictly
        # prior same-chat messages arrive as evidence, including the reply.
        self.assertEqual(set(by_message), {7401, 7402})
        self.assertEqual(by_message[7402]["reply_to_message_id"], 7500)
        self.assertIn("mapa listo", by_message[7402]["reply_to_text"])
        self.assertLessEqual(len(entries), 12)
        for entry in entries:
            for forbidden in ("command", "authority", "allowed", "action"):
                self.assertNotIn(forbidden, entry)


class OutboxScopeTests(unittest.TestCase):
    """_outbox_intents reads live intents only, never confirmed history."""

    def setUp(self):
        self.fixture = fixtures.TelegramTests()
        self.fixture.setUp()
        self.service = self.fixture.service
        self.adapter = self.fixture.adapter

    def tearDown(self):
        self.fixture.tearDown()

    def _seed_delivery(self, key, state, event):
        with self.service.store.transaction() as db:
            db.execute(
                "INSERT INTO deliveries(id, item_id, item_version, channel, target_key,"
                " semantic_key, state, payload_json, segments_json, created_at, retry_at, confirmed_at)"
                " VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                (key, None, None, "telegram", self.adapter.config.account,
                 key, state,
                 json.dumps({"method": "sendMessage", "payload": {}, "event": event,
                             "ordinal": 0, "account": self.adapter.config.account}),
                 "[]", None, None, None))

    def test_confirmed_history_is_not_decoded_as_live_intent(self):
        for index in range(3):
            self._seed_delivery(f"hist-{index}", "confirmed", f"old-event-{index}")
        self._seed_delivery("live-0", "uncertain", "live-event")
        intents = self.adapter._outbox_intents()
        self.assertEqual([(i["event"], i["status"]) for i in intents],
                         [("live-event", "uncertain")])


class LongSummaryTests(unittest.TestCase):
    """GUIA section 8: automatic long returns arrive brief; full stays on tap."""

    def setUp(self):
        import dataclasses
        self.fixture = fixtures.TelegramTests()
        self.fixture.setUp()
        self.service = self.fixture.service
        self.adapter = self.fixture.adapter
        self.adapter.config = dataclasses.replace(self.adapter.config, auto_return=True)

    def tearDown(self):
        self.fixture.tearDown()

    def _long_item(self):
        capture = self.service.capture("felix", "i2-sum-long", "Informe extenso")["item"]
        item = self.service.execute("felix", {"operation_id": "i2-sum-clarify", "action": "clarify",
            "item_id": capture["id"], "expected_version": capture["version"],
            "fields": {"kind": "action", "commitment": "committed", "outcome": "Resultado útil",
                       "completion_criteria": "Criterio comprobable"}})["item"]
        body = "".join(f"Hecho verificado {index:04d}. " for index in range(400))
        item = self.service.execute("felix", {"operation_id": "i2-sum-mat", "action": "put_material",
            "item_id": item["id"], "expected_version": item["version"],
            "fields": {"content": body, "title": "Informe"}})["item"]
        return item, body

    def test_automatic_long_notification_sends_brief_head_with_full_on_demand(self):
        item, body = self._long_item()
        key = self.fixture.notification(item)
        event = next(e for e in self.service.pending_events("gtd-notification", "local")
                     if e["event_key"] == key)
        self.assertGreater(len(self.adapter._notification_content(event)), 2)
        sent_before = len(self.fixture.http.sent)
        self.assertTrue(run(self.adapter._deliver_notification(event, automatic=True)))
        fresh = self.fixture.http.sent[sent_before:]
        self.assertEqual(len(fresh), 1)
        self.assertIn("Informe extenso", fresh[0]["text"])
        self.assertNotIn(body[-200:], fresh[0]["text"])
        buttons = [b["text"] for row in fresh[0]["reply_markup"]["inline_keyboard"] for b in row]
        self.assertIn("Ver resultado", buttons)
        run(self.adapter.show_result(item["id"]))
        joined = "\n".join(m["text"] for m in self.fixture.http.sent[sent_before + 1:])
        self.assertIn(body[:200], joined)
        self.assertIn(body[-200:], joined)

    def test_long_principal_reply_arrives_bounded_with_full_on_demand(self):
        item, body = self._long_item()
        marker = "DECISION_FINAL_NO_DEBE_PERDERSE"
        key = self.fixture.notification(item)
        event = next(e for e in self.service.pending_events("gtd-notification", "local")
                     if e["event_key"] == key)
        event["payload"]["native_reply"] = ("Explicación relevante del resultado. " * 300) + marker
        sent_before = len(self.fixture.http.sent)
        self.assertTrue(run(self.adapter._deliver_notification(event, automatic=True)))
        fresh = self.fixture.http.sent[sent_before:]
        self.assertEqual(len(fresh), 1)
        self.assertLess(len(fresh[0]["text"]), 4096)
        self.assertNotIn(marker, fresh[0]["text"])
        run(self.adapter.show_result(item["id"]))
        joined = "\n".join(m["text"] for m in self.fixture.http.sent[sent_before + 1:])
        self.assertIn(marker, joined)
        self.assertIn(body[-200:], joined)

    def test_long_reply_without_material_stays_reachable(self):
        capture = self.service.capture("felix", "i2-sum-nomat", "Pregunta larga")["item"]
        item = self.service.execute("felix", {"operation_id": "i2-sum-nomat-clarify", "action": "clarify",
            "item_id": capture["id"], "expected_version": capture["version"],
            "fields": {"kind": "action", "commitment": "committed", "outcome": "Responder",
                       "completion_criteria": "Respuesta dada"}})["item"]
        marker = "RESPUESTA_FINAL_SIN_MATERIAL"
        key = self.fixture.notification(item)
        event = next(e for e in self.service.pending_events("gtd-notification", "local")
                     if e["event_key"] == key)
        event["payload"]["native_reply"] = ("Respuesta extensa del principal. " * 300) + marker
        sent_before = len(self.fixture.http.sent)
        self.assertTrue(run(self.adapter._deliver_notification(event, automatic=True)))
        fresh = self.fixture.http.sent[sent_before:]
        self.assertEqual(len(fresh), 1)
        self.assertLess(len(fresh[0]["text"]), 4096)
        run(self.adapter.show_result(item["id"]))
        joined = "\n".join(m["text"] for m in self.fixture.http.sent[sent_before + 1:])
        self.assertIn(marker, joined)

    def test_short_notification_still_arrives_inline(self):
        capture = self.service.capture("felix", "i2-sum-short", "Nota breve")["item"]
        item = self.service.execute("felix", {"operation_id": "i2-sum-short-clarify", "action": "clarify",
            "item_id": capture["id"], "expected_version": capture["version"],
            "fields": {"kind": "action", "commitment": "committed", "outcome": "Listo",
                       "completion_criteria": "Hecho"}})["item"]
        item = self.service.execute("felix", {"operation_id": "i2-sum-short-mat", "action": "put_material",
            "item_id": item["id"], "expected_version": item["version"],
            "fields": {"content": "Detalle corto.", "title": "Nota"}})["item"]
        key = self.fixture.notification(item)
        event = next(e for e in self.service.pending_events("gtd-notification", "local")
                     if e["event_key"] == key)
        self.assertLessEqual(len(self.adapter._notification_content(event)), 2)
        sent_before = len(self.fixture.http.sent)
        self.assertTrue(run(self.adapter._deliver_notification(event, automatic=True)))
        fresh = self.fixture.http.sent[sent_before:]
        self.assertEqual(len(fresh), 1)
        self.assertIn("Detalle corto.", fresh[0]["text"])


class TransportContinuityTests(unittest.TestCase):
    """Capture, precision and return share one affair through the transport.

    Identity comes from durable Telegram source identity and explicit reply
    prompts, never from wording similarity. Wording choices of the principal
    (relative dates, thread linking) stay in the prepared human run.
    """

    def setUp(self):
        self.fixture = fixtures.TelegramTests()
        self.fixture.setUp()
        self.service = self.fixture.service
        self.adapter = self.fixture.adapter

    def tearDown(self):
        self.fixture.tearDown()

    def _tg_message(self, message_id, text, **extra):
        return {"message_id": message_id, "date": 100, "chat": {"id": 9},
                "from": {"id": 7}, "text": text, **extra}

    def test_capture_precision_and_return_share_one_affair(self):
        before = len(self.service.query())
        run(self.adapter._message(self._tg_message(7201, "Poner al día Telemedicina: responsabilidades"),
                                  "ev-7201"))
        self.assertEqual(len(self.service.query()), before + 1)
        item = next(i for i in self.service.query() if i.get("source", {}).get("message_id") == 7201)
        self.assertEqual(item["source"]["provider"], "telegram")
        # Transport retry of the same Telegram message never forks an affair.
        run(self.adapter._message(self._tg_message(7201, "Poner al día Telemedicina: responsabilidades"),
                                  "ev-7201-retry"))
        self.assertEqual(len(self.service.query()), before + 1)
        # Principal-side clarification and precisions conserve the affair.
        item = self.service.execute("felix", {"operation_id": "i2-tc-clarify", "action": "clarify",
            "item_id": item["id"], "expected_version": item["version"],
            "fields": {"kind": "action", "commitment": "committed", "outcome": "Mapa vigente",
                       "completion_criteria": "Responsables por frente"}})["item"]
        current = self.service.get_item(item["id"])
        item = self.service.execute("felix", {"operation_id": "i2-tc-due", "action": "edit",
            "item_id": item["id"], "expected_version": current["version"],
            "fields": {"due_at": LOOK_AFTER_MONDAY}})["item"]
        self.assertEqual(self.service.get_item(item["id"])["due_at"], LOOK_AFTER_MONDAY)
        item = self.service.execute("felix", {"operation_id": "i2-tc-mat", "action": "put_material",
            "item_id": item["id"], "expected_version": item["version"],
            "fields": {"content": "Mapa vigente por frentes.", "title": "Mapa"}})["item"]
        key = self.fixture.notification(item)
        event = next(e for e in self.service.pending_events("gtd-notification", "local")
                     if e["event_key"] == key)
        self.assertIn("Mapa vigente por frentes.", "\n".join(self.adapter._notification_content(event)))

    def test_reply_precision_applies_to_prompted_affair_only(self):
        run(self.adapter._message(self._tg_message(7211, "Encargo con dato"), "ev-7211"))
        item = next(i for i in self.service.query() if i.get("source", {}).get("message_id") == 7211)
        others_before = len(self.service.query())
        self.adapter._event("telegram-prompt", 7300,
            {"action": "edit", "item_id": item["id"], "expected_version": item["version"]})
        run(self.adapter._message(
            self._tg_message(7212, "Encargo con dato corregido",
                             reply_to_message={"message_id": 7300}), "ev-7212"))
        self.assertEqual(len(self.service.query()), others_before)
        self.assertEqual(self.service.get_item(item["id"])["title"], "Encargo con dato corregido")

    def test_unrelated_transport_message_stays_a_separate_affair(self):
        run(self.adapter._message(self._tg_message(7221, "Poner al día Telemedicina"), "ev-7221"))
        count = len(self.service.query())
        run(self.adapter._message(self._tg_message(7222, "Comprar café"), "ev-7222"))
        self.assertEqual(len(self.service.query()), count + 1)
        other = next(i for i in self.service.query() if i.get("source", {}).get("message_id") == 7222)
        self.assertEqual(other["kind"], "capture")


class UndoPruneTests(unittest.TestCase):
    """Undoing a result write leaves no orphan rows and stable stubs."""

    def setUp(self):
        self.fixture = fixtures.TelegramTests()
        self.fixture.setUp()
        self.service = self.fixture.service

    def tearDown(self):
        self.fixture.tearDown()

    def _action(self, tag):
        capture = self.service.capture("felix", f"i2-undo-{tag}", "Sonda")["item"]
        return self.service.execute("felix", {"operation_id": f"i2-undo-{tag}-clarify", "action": "clarify",
            "item_id": capture["id"], "expected_version": capture["version"],
            "fields": {"kind": "action", "commitment": "committed", "outcome": "O",
                       "completion_criteria": "C"}})["item"]

    def test_undo_of_first_material_prunes_row_and_keeps_empty_stubs(self):
        item = self._action("first")
        item = self.service.execute("felix", {"operation_id": "i2-undo-first-mat", "action": "put_material",
            "item_id": item["id"], "expected_version": item["version"],
            "fields": {"content": "v1", "title": "T"}})["item"]
        self.assertEqual(len(self.service.materials(item["id"])), 1)
        receipt = self.service.execute("felix", {"operation_id": "i2-undo-first-undo", "action": "undo",
            "item_id": item["id"], "expected_version": item["version"],
            "fields": {"operation_id": "i2-undo-first-mat"}})
        self.assertEqual(receipt["status"], "applied", receipt)
        self.assertEqual(self.service.materials(item["id"]), [])
        # Faithful inversion: absent before the undone write stays absent.
        self.assertNotIn("materials", self.service.get_item(item["id"]))

    def test_undo_of_second_version_keeps_first(self):
        item = self._action("second")
        item = self.service.execute("felix", {"operation_id": "i2-undo-second-mat1", "action": "put_material",
            "item_id": item["id"], "expected_version": item["version"],
            "fields": {"content": "v1", "title": "T"}})["item"]
        first = self.service.materials(item["id"])[-1]
        item = self.service.execute("felix", {"operation_id": "i2-undo-second-mat2", "action": "put_material",
            "item_id": item["id"], "expected_version": item["version"],
            "fields": {"content": "v2", "title": "T", "material_id": first["id"]}})["item"]
        receipt = self.service.execute("felix", {"operation_id": "i2-undo-second-undo", "action": "undo",
            "item_id": item["id"], "expected_version": item["version"],
            "fields": {"operation_id": "i2-undo-second-mat2"}})
        self.assertEqual(receipt["status"], "applied", receipt)
        remaining = self.service.materials(item["id"])
        self.assertEqual([(m["id"], m["version"]) for m in remaining], [(first["id"], 1)])


if __name__ == "__main__":
    unittest.main()
