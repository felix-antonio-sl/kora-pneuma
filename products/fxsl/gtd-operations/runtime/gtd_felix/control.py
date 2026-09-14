"""Durable admission and native receipts, on the application's existing Store.

Trusted adapters must persist a reservation before sending its job_id as the
provider's idempotency key. This module never schedules or retries native work.
"""
import copy
from contextlib import contextmanager
from contextvars import ContextVar
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
import hashlib
import json
import math
import sqlite3
import uuid

from .gtd import GTDDomain


def _json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def _number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value) and value >= 0


class ExecutionControl:
    KEY = "execution:state"
    TERMINAL = {"completed", "failed", "cancelled"}
    LIVE = {"queued", "running", "waiting", "uncertain", "not_found"}

    def __init__(self, service, config, clock=None):
        self._clock = clock or (lambda: datetime.now(timezone.utc))
        self.service = service
        self.store = service.store
        self.config = copy.deepcopy(config)
        self.config.setdefault("max_active", 1)
        self._technical_stops = ContextVar('gtd_attention_stop', default=frozenset())

    LEGACY_OP_PREFIX = "control:op:"
    LEGACY_STATE_BACKUP = "execution:state:legacy:v1"

    def _load(self):
        # Active path after I1 cut: small JSON (bots/config/periods, no jobs,
        # no control operations map). Legacy full blob is preserved frozen as
        # LEGACY_STATE_BACKUP for history/rollback and never written here.
        row = self.store.db.execute("SELECT value FROM metadata WHERE key=?", (self.KEY,)).fetchone()
        if row:
            state = json.loads(row[0])
            state.setdefault("bots", {})
            state.setdefault("operations", {})
            state.setdefault("config", None)
            state.setdefault("jobs", {})
            return state
        return {"jobs": {}, "bots": {}, "operations": {}, "config": None}

    def _save(self, state):
        # Never persist jobs or the legacy operations map in the active blob
        # once tables are authoritative. Jobs live in
        # work_cycles/runs/run_observations; control idempotency lives in
        # per-operation keys (see _control_op_get/_control_op_put). This keeps
        # active reads bounded (KB, not MB).
        # Defense in depth: while the database is still pre-migration (legacy
        # jobs present, tables empty), write the state unchanged so a stray
        # save can never strip the legacy collections. Mutating entry points
        # additionally refuse pre-migration work without any writes.
        if self._legacy_has_jobs() and not self._tables_have_runs():
            self.store.db.execute("INSERT OR REPLACE INTO metadata VALUES(?,?)", (self.KEY, _json(state)))
            return
        slim = {k: v for k, v in state.items() if k not in ("jobs", "operations")}
        # Keep an empty operations map for backward-compatible readers that
        # expect the key; authoritative idempotency is per-key.
        slim.setdefault("operations", {})
        self.store.db.execute("INSERT OR REPLACE INTO metadata VALUES(?,?)", (self.KEY, _json(slim)))

    def _legacy_has_jobs(self):
        row = self.store.db.execute("SELECT value FROM metadata WHERE key=?", (self.KEY,)).fetchone()
        if not row:
            return False
        try:
            state = json.loads(row[0])
        except ValueError:
            return False
        return bool(state.get("jobs"))
    def _tables_have_runs(self):
        row = self.store.db.execute("SELECT COUNT(*) FROM runs").fetchone()
        return bool(row and row[0])

    def _require_migrated(self):
        # After the I1 cut the tables are authoritative. A legacy blob with
        # jobs plus empty tables means migration has not run: refuse to
        # silently lose work instead of guessing.
        if self._legacy_has_jobs() and not self._tables_have_runs():
            raise ValueError("migration_required")

    def _control_op_key(self, operation_id):
        return self.LEGACY_OP_PREFIX + operation_id

    def _control_op_get(self, operation_id):
        row = self.store.db.execute("SELECT value FROM metadata WHERE key=?", (self._control_op_key(operation_id),)).fetchone()
        if row:
            return json.loads(row[0])
        # Backward compat: legacy map inside the active blob (pre-migration).
        # After migration this map is empty; per-key rows are authoritative.
        try:
            state = self._load()
            return state.get("operations", {}).get(operation_id)
        except ValueError:
            return None

    def _control_op_put(self, operation_id, fingerprint, receipt):
        self.store.db.execute("INSERT OR REPLACE INTO metadata VALUES(?,?)",
            (self._control_op_key(operation_id), _json({"fingerprint": fingerprint, "receipt": receipt})))

    # ---- I1 table layer: cycles/runs/observations are authoritative ----
    RUN_TERMINAL = {"completed", "failed", "cancelled", "expired"}
    RUN_ACTIVE_NATIVE = {"dispatching", "running", "stop_requested", "uncertain"}

    def _cycle_row(self, cycle_id):
        return self.store.db.execute("SELECT * FROM work_cycles WHERE id=?", (cycle_id,)).fetchone()

    def _run_row(self, run_id):
        return self.store.db.execute("SELECT * FROM runs WHERE id=?", (run_id,)).fetchone()

    def _run_observations(self, run_id):
        rows = self.store.db.execute(
            "SELECT seq, observed_at, native_state, runtime_seconds, cost_usd, receipt_json "
            "FROM run_observations WHERE run_id=? ORDER BY seq", (run_id,)).fetchall()
        out = []
        for r in rows:
            receipt = json.loads(r["receipt_json"])
            # receipt_json already holds the full observation dict; expose it
            # directly for semantic parity with legacy job['observations'].
            out.append(receipt)
        return out

    def _job_from_rows(self, cycle, run):
        # Reconstruct the legacy job dict for API compatibility from the
        # authoritative rows. detail_json carries the mutable legacy projection
        # (bases, progress, route, delivery); columns carry constraints.
        # This keeps commands/versions/receipts compatible while reads stay
        # bounded to the requested rows (no global history decode).
        detail = json.loads(run["detail_json"]) if run["detail_json"] else {}
        admission = json.loads(run["admission_json"]) if run["admission_json"] else {}
        cycle_detail = {}
        try:
            cycle_detail = json.loads(cycle["detail_json"]) if cycle and cycle["detail_json"] else {}
        except (KeyError, TypeError, ValueError):
            cycle_detail = {}
        obs = self._run_observations(run["id"])
        native = None
        if run["native_provider"] and run["native_profile"] and run["native_id"]:
            native = {"provider": run["native_provider"], "host": run["native_host"] or "localhost",
                      "profile": run["native_profile"], "id": run["native_id"]}
            # Preserve provider-specific identity facets (e.g. Codex
            # thread_id) kept in the mutable detail projection. Columns stay
            # authoritative for the indexed quadruple; extras round-trip so a
            # later observation with the identical full identity is not
            # misread as native_identity_changed.
            stored = detail.get("native")
            if isinstance(stored, dict):
                for key, value in stored.items():
                    if key not in native:
                        native[key] = copy.deepcopy(value)
        # Legacy terminal/delivery derived for compat; authoritative state is
        # runs.state / runs.integration.
        terminal = run["state"] in self.RUN_TERMINAL
        # Map new run states back to legacy delivery for readers that still
        # branch on it (orchestration, hermes, application).
        if run["state"] == "reserved":
            delivery = detail.get("delivery", "intent")
        elif run["state"] in ("dispatching", "running", "waiting_child", "stop_requested"):
            delivery = "acknowledged" if detail.get("delivery", "acknowledged") != "uncertain" else "uncertain"
        elif run["state"] == "uncertain":
            delivery = "uncertain"
        else:
            delivery = detail.get("delivery", "acknowledged")
        job = {
            "id": run["id"],
            "item_id": run["item_id"],
            "actor": run["actor"],
            "requested_by": detail.get("requested_by", admission.get("requested_by", run["actor"])),
            "parent_job_id": run["parent_run_id"],
            "root_job_id": detail.get("root_job_id", run["id"]),
            "capability": detail.get("capability", admission.get("capability")),
            "mandate_id": detail.get("mandate_id", admission.get("mandate_id")),
            "bot_id": detail.get("bot_id", admission.get("bot_id")),
            "purpose": cycle["purpose"] if cycle is not None else detail.get("purpose"),
            "scope": detail.get("scope", admission.get("scope")),
            "max_cost_usd": detail.get("max_cost_usd", admission.get("max_cost_usd", 0)),
            "max_runtime_seconds": detail.get("max_runtime_seconds", admission.get("max_runtime_seconds", run["reserved_seconds"])),
            "max_retries": detail.get("max_retries", admission.get("max_retries", 0)),
            "max_descendants": detail.get("max_descendants", admission.get("max_descendants", 0)),
            "expected_version": detail.get("expected_version", admission.get("expected_version")),
            "item_bases": detail.get("item_bases", admission.get("item_bases", {})),
            "source_bases": detail.get("source_bases", admission.get("source_bases", {})),
            "source_versions": detail.get("source_versions", admission.get("source_versions", {})),
            "scope_ancestry": detail.get("scope_ancestry", {}),
            "route": detail.get("route", admission.get("route")),
            "progress": detail.get("progress", []),
            "delivery": delivery,
            "stop_requested": detail.get("stop_requested", run["state"] == "stop_requested"),
            "terminal": terminal,
            "native": native,
            # Compat: legacy intermediates (accepted_pending_integration,
            # no_domain_progress) live in detail; authoritative new enum lives
            # in the column (pending/integrated/discarded).
            "integration": detail.get("integration", run["integration"])
            if detail.get("integration") in ("accepted_pending_integration", "no_domain_progress")
            else (run["integration"] if run["integration"] != "pending" else detail.get("integration", "pending")),
            "observations": obs,
            "charged_cost_usd": detail.get("charged_cost_usd", run["cost_usd"] if run["cost_usd"] is not None else 0),
            "observed_runtime_seconds": run["observed_seconds"],
            "budget_period_id": run["budget_period_id"],
            "orchestrated": detail.get("orchestrated", False),
        }
        # Preserve optional legacy keys when present in detail.
        for key in ("terminal_resolution", "integration_error", "result", "validated_version",
                    "domain_operation_id", "domain_operation_ids", "attention_origin",
                    "human_instruction_source_ids"):
            if key in detail:
                job[key] = copy.deepcopy(detail[key])
        # Human-instruction sources live in admission for new rows.
        if "human_instruction_source_ids" not in job and admission.get("human_instruction_source_ids") is not None:
            job["human_instruction_source_ids"] = copy.deepcopy(admission["human_instruction_source_ids"])
        return job

    def _iter_run_ids(self, where, params=(), chunk=200):
        # Complete paginated walk with bounded per-round memory (keyset on
        # rowid). Arbitrary LIMIT cutoffs silently drop candidates (e.g. an
        # exhausted review past 64 historical rows); pagination preserves them
        # all. Callers add selective WHERE filters (item, actor, integration)
        # so each round stays small and the walk stays complete.
        last = 0
        while True:
            rows = self.store.db.execute(
                f"SELECT rowid, id FROM runs WHERE ({where}) AND rowid>? "
                f"ORDER BY rowid LIMIT ?", (*params, last, chunk)).fetchall()
            if not rows:
                return
            for r in rows:
                last = r["rowid"]
                yield r["id"]

    def _iter_run_ids_by_item(self, item_id, chunk=200):
        return self._iter_run_ids("item_id=?", (item_id,), chunk)

    def _active_run_rows(self):
        # Complete active-work projection: non-terminal or pending-integration
        # rows. The set stays small by protocol (single global native slot,
        # max_active admissions, deferred bounded per family), so no LIMIT
        # truncation is applied; every active run must be visible.
        return self.store.db.execute(
            "SELECT id, cycle_id, item_id, actor, parent_run_id, state, integration, "
            "native_provider, native_host, native_profile, native_id, budget_period_id, "
            "reserved_seconds, observed_seconds, cost_usd FROM runs "
            "WHERE state NOT IN ('completed','failed','cancelled','expired') OR integration='pending' "
            "ORDER BY rowid").fetchall()

    def _operation(self, actor, operation_id, action, payload, fn):
        if not isinstance(operation_id, str) or not operation_id:
            return {"status": "rejected", "error": "operation_id_required"}
        try:
            digest = hashlib.sha256(_json([actor, action, payload]).encode()).hexdigest()
        except (ValueError, TypeError):
            return {"status": "rejected", "error": "invalid_json_payload"}
        with self.store.transaction():
            # Preserve the legacy state intact until a successful migration
            # cut. Pre-migration mutating operations are rejected without any
            # writes: no state cleanup, no per-key receipts (so the same
            # operation_id stays retryable after migration).
            if self._legacy_has_jobs() and not self._tables_have_runs():
                return {"status": "rejected", "error": "migration_required",
                        "operation_id": operation_id}
            # Bounded idempotency: single-key lookup, never the global map.
            old = self._control_op_get(operation_id)
            if old:
                if old["fingerprint"] != digest:
                    return {"status": "rejected", "error": "idempotency_conflict", "operation_id": operation_id}
                return dict(old["receipt"], duplicate=True)
            # Small state only (bots/config/periods). Jobs live in tables and
            # are touched by fn via bounded SQL inside the same transaction.
            # SQLite BEGIN IMMEDIATE gives us atomicity across metadata+tables;
            # service-level invariants (admission immutability, monotonic
            # consumption, family budget, single native) are enforced by fn.
            state = self._load()
            # Drop legacy large collections if a pre-migration blob is still
            # present: fn must use tables, never state["jobs"].
            state.pop("jobs", None)
            state.pop("operations", None)
            try:
                receipt = fn(state)
            except (ValueError, KeyError, TypeError) as error:
                receipt = {"status": "rejected", "error": str(error)}
            receipt["operation_id"] = operation_id
            # Persist small state + per-key receipt atomically. Rejected
            # receipts are also idempotent (same operation_id returns same
            # rejection) without ever writing jobs.
            self._save(state)
            self._control_op_put(operation_id, digest, receipt)
            return copy.deepcopy(receipt)

    def _manager(self, actor):
        if self.service.actor_role(actor) not in {"owner", "principal"}:
            raise ValueError("actor_not_manager")

    @staticmethod
    def policy_hash(config):
        return hashlib.sha256(_json(config).encode()).hexdigest()

    def _daily(self, config=None):
        return (self.config if config is None else config).get('budget_mode', 'fixed') == 'daily_subscription'

    def _period(self, config):
        digest = self.policy_hash(config)
        if not self._daily(config):
            return dict(id='fixed:' + digest, policy_hash=digest, config=copy.deepcopy(config),
                        start=config['period_start'], end=(datetime.fromisoformat(config['period_start'])
                        + timedelta(seconds=config['period_seconds'])).isoformat())
        zone = ZoneInfo(config['timezone'])
        day = self._clock().astimezone(zone).date()
        start = datetime.combine(day, datetime.min.time(), zone)
        end = datetime.combine(day + timedelta(days=1), datetime.min.time(), zone)
        # Some civil days begin at 01:00; serialize the real local instant.
        start = start.astimezone(timezone.utc).astimezone(zone)
        end = end.astimezone(timezone.utc).astimezone(zone)
        return dict(id='daily:' + digest + ':' + day.isoformat(), policy_hash=digest,
                    config=copy.deepcopy(config), start=start.isoformat(), end=end.isoformat())

    def _validate_policy(self):
        config = self.config
        if config.get('budget_mode', 'fixed') not in {'fixed', 'daily_subscription'}:
            raise ValueError('invalid_budget_mode')
        keys = ('max_cost_usd', 'max_runtime_seconds', 'recovery_cost_usd',
                'recovery_runtime_seconds', 'max_job_runtime_seconds', 'max_retries', 'max_descendants', 'max_active')
        if any(key not in config or not _number(config[key]) for key in keys):
            raise ValueError('execution_disabled')
        # max_active bounds admitted reservations (budget/active intents,
        # including deferred children), NOT native executions: the native slot
        # stays single-global (one_native_active) even with max_active=2. A
        # second reservation waits (deferred/uncertain + reconcile) instead of
        # a second simultaneous inference. Both values remain admissible.
        if config['max_active'] not in (1, 2) or any(int(config[k]) != config[k] for k in ('max_retries', 'max_descendants', 'max_active')):
            raise ValueError('invalid_limits')
        if self._daily():
            try:
                ZoneInfo(config['timezone'])
            except (KeyError, TypeError, ValueError, ZoneInfoNotFoundError):
                raise ValueError('invalid_daily_timezone') from None
            if ('period_start' in config or 'period_seconds' in config
                    or config['max_runtime_seconds'] <= 0
                    or config['max_job_runtime_seconds'] > config['max_runtime_seconds']):
                raise ValueError('invalid_daily_policy')
        else:
            try:
                start = datetime.fromisoformat(config['period_start'])
                if start.utcoffset() is None or not _number(config['period_seconds']):
                    raise ValueError()
            except (ValueError, KeyError, TypeError):
                raise ValueError('period_timezone_required') from None
        if ((not self._daily() and config['recovery_cost_usd'] > config['max_cost_usd'])
                or config['recovery_runtime_seconds'] > config['max_runtime_seconds']):
            raise ValueError('invalid_recovery_reserve')
        return config

    def _configuration(self, state):
        config = self._validate_policy()
        if state['config'] is not None and state['config'] != config:
            raise ValueError('budget_configuration_changed')
        if not self._daily():
            age = (self._clock() - datetime.fromisoformat(config['period_start'])).total_seconds()
            if not 0 <= age < config['period_seconds']:
                raise ValueError('budget_period_inactive')
        return config

    def transition_budget_policy(self, actor, operation_id, expected_hash):
        """Owner compare-and-set; configuration alone cannot replace pinned policy."""
        def apply(state):
            if self.service.actor_role(actor) != 'owner':
                raise ValueError('actor_not_owner')
            config = self._validate_policy()
            old = state.get('config')
            if not old or self.policy_hash(old) != expected_hash:
                raise ValueError('budget_policy_hash_mismatch')
            if not self._daily() or config == old:
                raise ValueError('unsupported_budget_transition')
            # Bounded: active runs only (at most max_active+uncertain few).
            active = self.store.db.execute(
                "SELECT 1 FROM runs WHERE state NOT IN ('completed','failed','cancelled','expired') LIMIT 1").fetchone()
            if active:
                raise ValueError('budget_transition_requires_terminal_jobs')
            historical = self._period(old)
            if self._daily(old):
                used = self.store.db.execute(
                    "SELECT 1 FROM runs WHERE budget_period_id=? LIMIT 1", (historical['id'],)).fetchone()
                if used:
                    raise ValueError('budget_transition_requires_unused_day')
            else:
                # Fixed predecessors carry placeholder periods; pin them to the
                # historical fixed id so the cut preserves budget lineage.
                self.store.db.execute(
                    "UPDATE runs SET budget_period_id=? WHERE budget_period_id='fixed:unscoped'",
                    (historical['id'],))
                self.store.db.execute(
                    "UPDATE work_cycles SET budget_period_id=? WHERE budget_period_id='fixed:unscoped'",
                    (historical['id'],))
            state.setdefault('periods', {})[historical['id']] = historical
            state.setdefault('policy_transitions', []).append(dict(actor=actor, operation_id=operation_id,
                previous_hash=expected_hash, policy_hash=self.policy_hash(config), at=self._clock().isoformat()))
            state['config'] = copy.deepcopy(config)
            return dict(status='applied', policy_hash=self.policy_hash(config), historical_period_id=historical['id'])
        return self._operation(actor, operation_id, 'transition_budget_policy',
                               dict(expected_hash=expected_hash, policy=self.config), apply)

    def register_bot(self, actor, operation_id, bot):
        def apply(state):
            self._manager(actor)
            if bot.get("state") not in {"planned", "incorporated", "available", "suspended", "unavailable"} or not bot.get("id"):
                raise ValueError("invalid_bot")
            if bot.get("actor") is not None and self.service.actor_role(bot["actor"]) not in {"principal", "executor"}:
                raise ValueError("invalid_bot_actor")
            if bot["state"] != "planned":
                if not all(bot.get(k) for k in ("source_urn", "profile", "host", "capabilities")):
                    raise ValueError("bot_identity_required")
                if not isinstance(bot["capabilities"], list) or any(c not in {"prepare_private", "local_work"} for c in bot["capabilities"]):
                    raise ValueError("invalid_bot_capabilities")
                if self.service.actor_role(actor) != "owner":
                    for capability in bot["capabilities"]:
                        auth = self.service.authorize(actor, capability, bot.get("item_id"), bot.get("mandate_id"))
                        if not auth["allowed"]:
                            raise ValueError(auth["reason"])
            if bot["state"] == "available" and not bot.get("probe_evidence"):
                raise ValueError("route_probe_required")
            state["bots"][bot["id"]] = copy.deepcopy(bot)
            return {"status": "applied", "bot": bot}
        return self._operation(actor, operation_id, "register_bot", bot, apply)

    def bots(self):
        with self.store.lock:
            return list(self._load()["bots"].values())

    def _budget(self, state):
        # Bounded family budget without decoding global history or detail_json.
        # Only numeric columns for the current period (or all roots for fixed).
        # Unknown cost stays NULL in tables; here it is treated conservatively
        # via max(assignment, observed) for open families and via observed sum
        # for closed ones, never as zero. See GUIA section 7.
        config = state.get('config') or self.config
        daily = self._daily(config)
        period = self._period(config) if daily else None
        period_id = period["id"] if daily else None
        # Fetch only roots in scope (parent_run_id IS NULL) with small columns.
        if daily:
            roots = self.store.db.execute(
                "SELECT id, state, integration, reserved_seconds, observed_seconds, cost_usd, "
                "detail_json FROM runs WHERE parent_run_id IS NULL AND budget_period_id=?",
                (period_id,)).fetchall()
        else:
            roots = self.store.db.execute(
                "SELECT id, state, integration, reserved_seconds, observed_seconds, cost_usd, "
                "detail_json FROM runs WHERE parent_run_id IS NULL").fetchall()
        cost = runtime = 0.0
        active = 0
        for root in roots:
            # Family numeric aggregation without detail decode, except for
            # max assignment which lives in detail/admission for fixed periods.
            fam = self.store.db.execute(
                "SELECT state, integration, observed_seconds, cost_usd, reserved_seconds, detail_json "
                "FROM runs WHERE id=? OR parent_run_id=? OR id IN "
                "(SELECT id FROM runs WHERE cycle_id IN (SELECT id FROM work_cycles WHERE parent_cycle_id IN "
                "(SELECT cycle_id FROM runs WHERE id=?)))",
                (root["id"], root["id"], root["id"])).fetchall()
            # Simpler and still bounded: family = runs sharing the root cycle
            # lineage. For I1 singletons family is one row; for delegated
            # same-item children family is same cycle; for cross-item children
            # family spans child cycles via parent_cycle_id. Fetch via cycle.
            root_run = self._run_row(root["id"])
            if root_run is None:
                continue
            cycle_id = root_run["cycle_id"]
            # Collect all cycles in this family (root + descendants) bounded to
            # a few rows: families are tiny (max_descendants<=config).
            family_cycle_ids = [cycle_id]
            frontier = [cycle_id]
            while frontier:
                nxt = []
                for cid in frontier:
                    rows = self.store.db.execute(
                        "SELECT id FROM work_cycles WHERE parent_cycle_id=?", (cid,)).fetchall()
                    for r in rows:
                        if r["id"] not in family_cycle_ids:
                            family_cycle_ids.append(r["id"])
                            nxt.append(r["id"])
                frontier = nxt
                if len(family_cycle_ids) > 32:
                    break
            placeholders = ",".join("?" for _ in family_cycle_ids)
            fam2 = self.store.db.execute(
                f"SELECT state, integration, observed_seconds, cost_usd, reserved_seconds, detail_json "
                f"FROM runs WHERE cycle_id IN ({placeholders})", tuple(family_cycle_ids)).fetchall()
            # Assignment from root detail (bounded single small JSON, not history).
            try:
                root_detail = json.loads(root["detail_json"]) if root["detail_json"] else {}
            except ValueError:
                root_detail = {}
            max_cost = root_detail.get("max_cost_usd", 0)
            max_runtime = root_detail.get("max_runtime_seconds", root["reserved_seconds"])
            # Closed family (all terminal) commits only real consumption.
            states = [r["state"] for r in fam2]
            terminal_all = states and all(s in self.RUN_TERMINAL for s in states)
            if terminal_all:
                for r in fam2:
                    try:
                        d = json.loads(r["detail_json"]) if r["detail_json"] else {}
                    except ValueError:
                        d = {}
                    # charged_cost in detail preserves legacy conservative
                    # accounting for unknown cost (reservation) at terminal.
                    cost += d.get("charged_cost_usd", r["cost_usd"] if r["cost_usd"] is not None else 0)
                    runtime += r["observed_seconds"] or 0
            else:
                # Open/uncertain: max(assignment, observed sum). Unknown cost
                # never becomes zero: if observed NULL, use assignment.
                obs_cost_sum = 0.0
                obs_runtime_sum = 0.0
                for r in fam2:
                    try:
                        d = json.loads(r["detail_json"]) if r["detail_json"] else {}
                    except ValueError:
                        d = {}
                    c = d.get("charged_cost_usd", r["cost_usd"])
                    obs_cost_sum += c if isinstance(c, (int, float)) else 0
                    obs_runtime_sum += r["observed_seconds"] or 0
                cost += max(float(max_cost or 0), obs_cost_sum)
                runtime += max(float(max_runtime or 0), obs_runtime_sum)
        # Active count: non-terminal, non-deferred (deferred lives in detail).
        # Terminal pending-integration is NOT active (matches legacy
        # not-terminal check); pending() separately includes it for integration.
        # No LIMIT: the live set stays small by protocol (single native slot,
        # max_active admissions), and truncating it would undercount budget.
        active_rows = self.store.db.execute(
            "SELECT id FROM runs WHERE state NOT IN ('completed','failed','cancelled','expired')").fetchall()
        for r in active_rows:
            full = self._run_row(r["id"])
            if full is None:
                continue
            try:
                d = json.loads(full["detail_json"]) if full["detail_json"] else {}
            except ValueError:
                d = {}
            if d.get("delivery") != "deferred":
                active += 1
        config = state.get('config') or self.config
        return {"committed_cost_usd": cost, "committed_runtime_seconds": runtime,
                "remaining_cost_usd": None if daily else max(0, config.get("max_cost_usd", 0) - config.get("recovery_cost_usd", 0) - cost),
                "cost_control": not daily, "budget_mode": config.get("budget_mode", "fixed"),
                "policy_hash": self.policy_hash(config),
                "period_id": period["id"] if daily else None,
                "returns_at": period["end"] if daily else None,
                "runtime_enforcement": "cooperative",
                "remaining_runtime_seconds": max(0, config.get("max_runtime_seconds", 0) - config.get("recovery_runtime_seconds", 0) - runtime),
                "active": active,
                "recovery_cost_usd": config.get("recovery_cost_usd", 0),
                "recovery_runtime_seconds": config.get("recovery_runtime_seconds", 0)}

    def budget(self):
        with self.store.lock:
            # Small state only; family aggregation is bounded to the period.
            return self._budget(self._load())

    def _dependencies(self, state, job):
        """Declared dependency closure is a validity basis, never execution scope."""
        pending = [job["item_id"], *job.get("source_versions", {}), *job.get("human_instruction_source_ids", [])]
        parent_id = job.get("parent_job_id")
        if parent_id:
            # Bounded single-row lookup, never the global history.
            prow = self._run_row(parent_id)
            if prow is not None:
                # item_id is a small column; no detail decode needed.
                pending.append(prow["item_id"])
        visited = set()
        while pending:
            item_id = pending.pop()
            if item_id in visited:
                continue
            visited.add(item_id)
            item = self.service.get_item(item_id) or {}
            pending.extend(item.get("source_versions", {}))
            pending.extend(item.get("depends_on", []))
            if item.get("parent_id"):
                pending.append(item["parent_id"])
        return visited - {job["item_id"]}

    def _vigent(self, state, job, capability, integration=False):
        if not integration:
            self._configuration(state)
            if self._daily() and job.get("budget_period_id") != self._period(self.config)["id"]:
                raise ValueError("job_budget_period_expired")
        if self.service.recovery_required:
            raise ValueError("recovery_required")
        if capability != job["capability"]:
            raise ValueError("capability_mismatch")
        if not integration and job["observed_runtime_seconds"] >= job["max_runtime_seconds"]:
            raise ValueError("job_runtime_exhausted")
        if not integration and not self._daily() and job["charged_cost_usd"] >= job["max_cost_usd"]:
            raise ValueError("job_cost_exhausted")
        if job["stop_requested"]:
            raise ValueError("stop_requested")
        if job["terminal"] and not integration:
            raise ValueError("terminal_job")
        item = self.service.get_item(job["item_id"])
        if not item:
            raise ValueError("stale_item_version")
        if self.service.work_paused(item["id"]):
            raise ValueError("work_paused")
        basis = job.get("item_bases", {}).get(job["item_id"])
        if basis is not None:
            if (self._basis(item["id"]) != basis
                    and not self._compatible_parent_coordination(state, job, item["id"], basis)):
                raise ValueError("stale_item_version")
        elif item["version"] != job["expected_version"]:
            raise ValueError("stale_item_version")
        for source_id, revision in job.get("source_versions", {}).items():
            source = self.service.get_item(source_id)
            if not source or len(source.get("source_revisions", [])) != revision:
                raise ValueError("source_version_stale")
        # Bounded existence check: single-row lookup, never global history.
        _exists = self._run_row(job["id"]) is not None
        if ("source_versions" in job or _exists) and not self._dependencies(state, job).issubset(job.get("source_bases", {})):
            raise ValueError("source_basis_required")
        for source_id, basis in job.get("source_bases", {}).items():
            if basis is None or (self._basis(source_id) != basis
                    and not self._compatible_parent_coordination(state, job, source_id, basis)):
                raise ValueError("source_version_stale")
        bot = state["bots"].get(job["bot_id"], {})
        if job.get("route") and any(bot.get(k) != v for k, v in job["route"].items()):
            raise ValueError("bot_route_changed")
        if bot.get("state") != "available" or capability not in bot.get("capabilities", []):
            raise ValueError("bot_unavailable")
        if job["mandate_id"]:
            mandate = next((m for m in self.service.mandates() if m["id"] == job["mandate_id"]), None)
            if not mandate or mandate.get("status") != "active":
                raise ValueError("mandate_not_active")
        elif capability != "prepare_private":
            raise ValueError("mandate_required")
        auth = self.service.authorize(job["actor"], capability, job["item_id"], job["mandate_id"])
        if not auth["allowed"]:
            raise ValueError(auth["reason"])

    def reserve(self, actor, operation_id, request):
        """Reserve request's item_id, expected_version, mandate_id, capability,
        bot_id, purpose, scope, max_cost_usd, max_runtime_seconds, max_retries,
        max_descendants; optional parent_job_id allocates from its root budget.
        Returned job_id MUST be the native idempotency key. No automatic retry.
        """
        return self._operation(actor, operation_id, "reserve", request,
                               lambda state: self._reserve(state, actor, operation_id, request))

    def _trigger_key_for(self, operation_id):
        # Cause deduplication: repeating the same cause must not re-admit.
        # Orchestration event admissions carry attempt suffixes; strip to cause.
        if operation_id.startswith("gtd-event:"):
            # gtd-event:<identity>:<attempt> -> gtd-event:<identity>
            base = operation_id.rsplit(":", 1)[0]
            return base
        return "op:" + operation_id

    def _reserve(self, state, actor, operation_id, request):
        self._manager(actor)
        self._require_migrated()
        config = self._configuration(state)
        for key in ("item_id", "expected_version", "capability", "bot_id", "purpose", "scope"):
            if not request.get(key):
                raise ValueError("request_identity_required")
        for key in ("max_cost_usd", "max_runtime_seconds", "max_retries", "max_descendants"):
            if not _number(request.get(key)):
                raise ValueError("request_limits_required")
        if request["max_runtime_seconds"] > config["max_job_runtime_seconds"] or any(request[k] > config[k] or int(request[k]) != request[k] for k in ("max_retries", "max_descendants")):
            raise ValueError("request_limit_exceeded")
        if request["max_cost_usd"] <= 0 or request["max_runtime_seconds"] <= 0:
            raise ValueError("positive_reservation_required")
        job = {key: copy.deepcopy(request.get(key)) for key in ("item_id", "expected_version", "mandate_id", "capability", "bot_id", "purpose", "scope", "max_cost_usd", "max_runtime_seconds", "max_retries", "max_descendants")}
        run_id = uuid.uuid4().hex
        job.update(id=run_id, actor=actor, delivery="intent", stop_requested=False,
                   terminal=False, integration="pending", native=None, observations=[],
                   charged_cost_usd=0, observed_runtime_seconds=0,
                   parent_job_id=request.get("parent_job_id"), orchestrated=request.get("orchestrated") is True)
        instruction_sources = request.get("human_instruction_source_ids", [])
        if (not isinstance(instruction_sources, list) or any(not isinstance(sid, str) for sid in instruction_sources)):
            raise ValueError("invalid_human_instruction_sources")
        if instruction_sources:
            job["human_instruction_source_ids"] = list(dict.fromkeys(instruction_sources))
        job["root_job_id"] = job["id"]
        if self._daily():
            period = self._period(config)
            state.setdefault("periods", {})[period["id"]] = period
            job["budget_period_id"] = period["id"]
        else:
            # Fixed periods carry no per-day id; keep the configured period for
            # family accounting. Bounded: no table scan, config only.
            job["budget_period_id"] = self._period(config)["id"] if False else job.get("budget_period_id", "fixed:unscoped")
            if "budget_period_id" not in job or not job["budget_period_id"]:
                job["budget_period_id"] = "fixed:unscoped"
        execution_bot = state.get("bots", {}).get(job["bot_id"], {})
        job["requested_by"] = actor
        job["actor"] = execution_bot.get("actor", actor)
        self._vigent(state, job, job["capability"])
        bot = state["bots"][job["bot_id"]]
        job["route"] = {k: bot[k] for k in ("host", "profile")}
        job["source_versions"] = copy.deepcopy(self.service.get_item(job["item_id"]).get("source_versions", {}))
        job["item_bases"] = {job["item_id"]: self._basis(job["item_id"])}
        job["scope_ancestry"] = {}
        if (self.service.actor_role(job["actor"]) == "principal"
                and (job["mandate_id"] or job["capability"] == "prepare_private")):
            for candidate in self.service.query():
                path = self._descendant_path(candidate["id"], job["item_id"])
                if path and self.service.authorize(job["actor"], job["capability"], candidate["id"], job["mandate_id"])["allowed"]:
                    job["item_bases"][candidate["id"]] = self._basis(candidate["id"])
                    job["scope_ancestry"][candidate["id"]] = path
        job["source_bases"] = {sid: self._basis(sid) for sid in self._dependencies(state, job)}
        job["progress"] = []
        self._vigent(state, job, job["capability"])
        budget = self._budget(state)
        # Bounded overrun check: only live/uncertain rows in this period (few),
        # never the full history. Unknown cost never becomes zero: only
        # numeric overruns block; NULL stays conservative via charged detail.
        # No LIMIT: every live run in scope must be checked; the live set
        # stays small by protocol (single native slot, max_active admissions).
        if self._daily():
            over_rows = self.store.db.execute(
                "SELECT observed_seconds, reserved_seconds, detail_json, budget_period_id FROM runs "
                "WHERE state NOT IN ('completed','failed','cancelled','expired') AND budget_period_id=?",
                (job["budget_period_id"],)).fetchall()
            for r in over_rows:
                try:
                    d = json.loads(r["detail_json"]) if r["detail_json"] else {}
                except ValueError:
                    d = {}
                max_rt = d.get("max_runtime_seconds", r["reserved_seconds"])
                if (r["observed_seconds"] or 0) > (max_rt or 0):
                    raise ValueError("observed_budget_overrun")
        else:
            over_rows = self.store.db.execute(
                "SELECT observed_seconds, reserved_seconds, cost_usd, detail_json FROM runs "
                "WHERE state NOT IN ('completed','failed','cancelled','expired')").fetchall()
            for r in over_rows:
                try:
                    d = json.loads(r["detail_json"]) if r["detail_json"] else {}
                except ValueError:
                    d = {}
                max_rt = d.get("max_runtime_seconds", r["reserved_seconds"])
                max_cost = d.get("max_cost_usd", 0)
                charged = d.get("charged_cost_usd", r["cost_usd"] if r["cost_usd"] is not None else 0)
                if (charged > max_cost) or ((r["observed_seconds"] or 0) > (max_rt or 0)):
                    raise ValueError("observed_budget_overrun")
        if budget["active"] >= config["max_active"]:
            if request.get("defer_when_busy") is True and job["parent_job_id"]:
                job["delivery"] = "deferred"
            else:
                raise ValueError("concurrency_exhausted")
        parent = root = None
        children = []
        if job["parent_job_id"]:
            prow = self._run_row(job["parent_job_id"])
            if prow is None:
                raise ValueError("parent_not_found")
            # Reconstruct parent compat dict bounded to one row + observations.
            pcycle = self._cycle_row(prow["cycle_id"])
            parent = self._job_from_rows(pcycle, prow)
            self._vigent(state, parent, parent["capability"])
            rrow = self._run_row(parent["root_job_id"])
            if rrow is None:
                raise ValueError("root_not_found")
            rcycle = self._cycle_row(rrow["cycle_id"])
            root = self._job_from_rows(rcycle, rrow)
            if root["terminal"]:
                raise ValueError("terminal_root")
            # Bounded family fetch: runs in root lineage (few rows).
            root_cycle_id = rrow["cycle_id"]
            fam_cycle_ids = [root_cycle_id]
            frontier = [root_cycle_id]
            while frontier:
                nxt = []
                for cid in frontier:
                    for rr in self.store.db.execute(
                            "SELECT id FROM work_cycles WHERE parent_cycle_id=?", (cid,)).fetchall():
                        if rr["id"] not in fam_cycle_ids:
                            fam_cycle_ids.append(rr["id"])
                            nxt.append(rr["id"])
                frontier = nxt
            placeholders = ",".join("?" for _ in fam_cycle_ids)
            fam_rows = self.store.db.execute(
                f"SELECT id, parent_run_id, detail_json FROM runs WHERE cycle_id IN ({placeholders})",
                tuple(fam_cycle_ids)).fetchall()
            # Children = family minus root, with legacy max fields from detail.
            children = []
            for fr in fam_rows:
                if fr["id"] == root["id"]:
                    continue
                try:
                    dd = json.loads(fr["detail_json"]) if fr["detail_json"] else {}
                except ValueError:
                    dd = {}
                children.append({"id": fr["id"], "parent_job_id": fr["parent_run_id"],
                                 "max_cost_usd": dd.get("max_cost_usd", 0),
                                 "max_runtime_seconds": dd.get("max_runtime_seconds", 0),
                                 "max_descendants": dd.get("max_descendants", 0)})
            descendants = {parent["id"]}
            child_ids = {c["id"]: c for c in children}
            while True:
                expanded = descendants | {cid for cid, c in child_ids.items() if c.get("parent_job_id") in descendants}
                if expanded == descendants:
                    break
                descendants = expanded
            if len(children) >= root["max_descendants"] or len(descendants) - 1 >= parent["max_descendants"]:
                raise ValueError("descendants_exhausted")
            if (any(job[k] != parent[k] for k in ("mandate_id", "capability"))
                    or job["item_id"] not in parent.get("item_bases", {parent["item_id"]: None})
                    or self.service.get_item(job["item_id"])["version"] != job["expected_version"]):
                raise ValueError("descendant_authority_mismatch")
            if ((not self._daily() and sum(j["max_cost_usd"] for j in children) + job["max_cost_usd"] + root["charged_cost_usd"] > root["max_cost_usd"])
                    or sum(j["max_runtime_seconds"] for j in children) + job["max_runtime_seconds"] + root["observed_runtime_seconds"] > root["max_runtime_seconds"]):
                raise ValueError("parent_allocation_exhausted")
            job["root_job_id"] = root["id"]
        elif (budget["cost_control"] and job["max_cost_usd"] > budget["remaining_cost_usd"]) or job["max_runtime_seconds"] > budget["remaining_runtime_seconds"]:
            raise ValueError("budget_exhausted")
        if not job["parent_job_id"]:
            # Bounded duplicate-cause check: one open run per item+purpose.
            dup = self.store.db.execute(
                "SELECT runs.id FROM runs JOIN work_cycles ON runs.cycle_id=work_cycles.id "
                "WHERE runs.item_id=? AND work_cycles.purpose=? AND runs.state NOT IN "
                "('completed','failed','cancelled','expired') LIMIT 1",
                (job["item_id"], job["purpose"])).fetchone()
            if dup:
                raise ValueError("purpose_already_active")
        # ---- Persist cycle + run atomically (same SQLite transaction) ----
        # SQLite guards uniqueness/partial indexes; service guards admission
        # immutability, monotonic consumption and family budget above.
        state["config"] = config
        trigger_key = self._trigger_key_for(operation_id)
        input_fp = hashlib.sha256(_json([job["item_id"], job.get("item_bases", {}),
                                         job.get("source_bases", {}), job["purpose"]]).encode()).hexdigest()
        authority = {"actor": job["actor"], "requested_by": job.get("requested_by", actor),
                     "capability": job["capability"], "mandate_id": job.get("mandate_id"),
                     "bot_id": job["bot_id"], "operation_id": operation_id}
        now_iso = self._clock().isoformat()
        # Cycle + run persist as one atomic unit: a savepoint rolls back a
        # half-written admission (e.g. cycle without run) when a uniqueness
        # contract rejects it, so the outer transaction never commits partial
        # control state.
        self.store.db.execute("SAVEPOINT reserve_unit")
        try:
            if job["parent_job_id"]:
                # Same-item child: new attempt in the same authorized cycle, no new
                # quota. Cross-item child: new child cycle with assignment from the
                # parent family (parent_cycle_id), same budget period as root.
                if job["item_id"] == parent["item_id"]:
                    cycle_id = parent_cycle_id = prow["cycle_id"]
                    # Enforce attempts limit on the shared cycle (bounded count).
                    crow = self._cycle_row(cycle_id)
                    runs_in_cycle = self.store.db.execute(
                        "SELECT COUNT(*) FROM runs WHERE cycle_id=?", (cycle_id,)).fetchone()[0]
                    if runs_in_cycle >= (crow["attempts_limit"] if crow else 1):
                        # Fall through to descendants check already done; attempts
                        # exhaustion surfaces as descendants_exhausted for compat.
                        pass
                    cycle_state = crow["state"] if crow else "running"
                    # Keep the cycle running while the new attempt is reserved.
                    if cycle_state in ("ready", "waiting", "paused"):
                        self.store.db.execute(
                            "UPDATE work_cycles SET state='running' WHERE id=?", (cycle_id,))
                else:
                    cycle_id = uuid.uuid4().hex
                    parent_cycle_id = prow["cycle_id"]
                    # Prevent kinship cycles (bounded walk, families are tiny).
                    seen = {cycle_id}
                    cur = parent_cycle_id
                    while cur:
                        if cur in seen:
                            raise ValueError("cycle_kinship_violation")
                        seen.add(cur)
                        prow2 = self._cycle_row(cur)
                        cur = prow2["parent_cycle_id"] if prow2 and prow2["parent_cycle_id"] else None
                    self.store.db.execute(
                        "INSERT INTO work_cycles(id,item_id,trigger_key,input_fingerprint,purpose,"
                        "authority_json,state,allowance_seconds,attempts_limit,wake_json,"
                        "predecessor_id,parent_cycle_id,budget_period_id,created_at,closed_at,detail_json) "
                        "VALUES(?,?,?,?,?,?,?, ?,?,?, ?,?,?,?,?,?)",
                        (cycle_id, job["item_id"], "op:"+operation_id+":child:"+run_id, input_fp, job["purpose"],
                         _json(authority), "running", float(job["max_runtime_seconds"]),
                         int(job["max_retries"])+1 if isinstance(job.get("max_retries"), int) else 1, None,
                         None, parent_cycle_id, job["budget_period_id"], now_iso, None,
                         _json({"origin": "child", "parent_run_id": job["parent_job_id"],
                                "root_run_id": job["root_job_id"], "operation_id": operation_id})))
            else:
                cycle_id = uuid.uuid4().hex
                self.store.db.execute(
                    "INSERT INTO work_cycles(id,item_id,trigger_key,input_fingerprint,purpose,"
                    "authority_json,state,allowance_seconds,attempts_limit,wake_json,"
                    "predecessor_id,parent_cycle_id,budget_period_id,created_at,closed_at,detail_json) "
                    "VALUES(?,?,?,?,?,?,?, ?,?,?, ?,?,?,?,?,?)",
                    (cycle_id, job["item_id"], trigger_key, input_fp, job["purpose"],
                     _json(authority), "running", float(job["max_runtime_seconds"]),
                     int(job["max_retries"])+1 if isinstance(job.get("max_retries"), int) else 1, None,
                     None, None, job["budget_period_id"], now_iso, None,
                     _json({"origin": "root", "operation_id": operation_id})))
        except sqlite3.IntegrityError as exc:
            self.store.db.execute("ROLLBACK TO reserve_unit")
            self.store.db.execute("RELEASE reserve_unit")
            msg = str(exc).lower()
            if "one_open_cycle_per_item" in msg:
                raise ValueError("purpose_already_active")
            if "trigger_key" in msg:
                # Repeating a cause never re-admits the same work. If an open
                # cycle for the subject still exists, report it as active
                # work; otherwise report the duplicate cause itself.
                open_same = self.store.db.execute(
                    "SELECT 1 FROM work_cycles WHERE item_id=? AND state IN "
                    "('ready','running','paused','recovery_required') LIMIT 1",
                    (job["item_id"],)).fetchone()
                if open_same:
                    raise ValueError("purpose_already_active")
                raise ValueError("duplicate_cause")
            raise
        admission = {"requested_by": job["requested_by"], "capability": job["capability"],
                     "mandate_id": job.get("mandate_id"), "bot_id": job["bot_id"],
                     "expected_version": job["expected_version"],
                     "max_cost_usd": job["max_cost_usd"], "max_runtime_seconds": job["max_runtime_seconds"],
                     "max_retries": job["max_retries"], "max_descendants": job["max_descendants"],
                     "item_bases": job["item_bases"], "source_bases": job["source_bases"],
                     "source_versions": job["source_versions"], "route": job["route"],
                     "scope": job["scope"], "purpose": job["purpose"]}
        if job.get("human_instruction_source_ids") is not None:
            admission["human_instruction_source_ids"] = copy.deepcopy(job["human_instruction_source_ids"])
        detail = {"requested_by": job["requested_by"], "capability": job["capability"],
                  "mandate_id": job.get("mandate_id"), "bot_id": job["bot_id"],
                  "expected_version": job["expected_version"],
                  "max_cost_usd": job["max_cost_usd"], "max_runtime_seconds": job["max_runtime_seconds"],
                  "max_retries": job["max_retries"], "max_descendants": job["max_descendants"],
                  "item_bases": job["item_bases"], "source_bases": job["source_bases"],
                  "source_versions": job["source_versions"], "scope_ancestry": job["scope_ancestry"],
                  "route": job["route"], "scope": job["scope"], "purpose": job["purpose"],
                  "progress": [], "delivery": job["delivery"], "stop_requested": False,
                  "charged_cost_usd": 0, "root_job_id": job["root_job_id"],
                  "orchestrated": job["orchestrated"]}
        if job.get("human_instruction_source_ids") is not None:
            detail["human_instruction_source_ids"] = copy.deepcopy(job["human_instruction_source_ids"])
        try:
            self.store.db.execute(
                "INSERT INTO runs(id,cycle_id,item_id,actor,parent_run_id,state,integration,"
                "admission_json,detail_json,native_provider,native_host,native_profile,native_id,"
                "budget_period_id,reserved_seconds,observed_seconds,cost_usd,"
                "admitted_at,started_at,ended_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (run_id, cycle_id, job["item_id"], job["actor"], job["parent_job_id"],
                 "reserved", "pending", _json(admission), _json(detail),
                 None, None, None, None,
                 job["budget_period_id"], float(job["max_runtime_seconds"]), 0, None,
                 now_iso, None, None))
        except sqlite3.IntegrityError as exc:
            # Revert the cycle row above with the run: half-written admissions
            # never persist. SQLite guards stay the backstop; service maps them
            # to domain rejections.
            self.store.db.execute("ROLLBACK TO reserve_unit")
            self.store.db.execute("RELEASE reserve_unit")
            msg = str(exc).lower()
            if "one_open_cycle_per_item" in msg:
                raise ValueError("purpose_already_active")
            if "trigger_key" in msg:
                open_same = self.store.db.execute(
                    "SELECT 1 FROM work_cycles WHERE item_id=? AND state IN "
                    "('ready','running','paused','recovery_required') LIMIT 1",
                    (job["item_id"],)).fetchone()
                if open_same:
                    raise ValueError("purpose_already_active")
                raise ValueError("duplicate_cause")
            raise
        self.store.db.execute("RELEASE reserve_unit")
        # Persist small-state config change atomically with the rows above.
        self._save(state)
        # Return the legacy-shaped receipt for command/version compatibility.
        job["budget_period_id"] = job["budget_period_id"]
        return {"status": "reserved", "job_id": run_id, "job": job}

    def get_job(self, job_id):
        # Bounded single-row projection; never decodes global history.
        with self.store.lock:
            try:
                self._require_migrated()
            except ValueError:
                # Pre-migration fresh tests have no legacy jobs; legacy base
                # without migration must not silently return None for real work.
                # Fall back to legacy map only when tables are still empty and
                # no legacy jobs exist (empty fresh DB).
                if self._legacy_has_jobs():
                    raise
                return None
            run = self._run_row(job_id)
            if run is None:
                return None
            cycle = self._cycle_row(run["cycle_id"])
            return self._job_from_rows(cycle, run)

    def job_history(self, actor, caller_job_id, item_id=None):
        """Read bounded execution evidence; historical jobs grant no authority."""
        with self.store.lock:
            try:
                caller = self.get_job(caller_job_id)
            except ValueError as exc:
                return {'status': 'rejected', 'error': str(exc)}
            if (self.service.actor_role(actor) != 'principal' or not caller
                    or caller['actor'] != actor):
                return {'status': 'rejected', 'error': 'job_actor_mismatch'}
            valid = self.validate(caller_job_id, caller['capability'])
            if not valid['allowed']:
                return {'status': 'rejected', 'error': valid['reason']}
            anchor = item_id or caller['item_id']
            allowed = self.validate_target(caller_job_id, actor, anchor, 'prepare_private')
            if not allowed['allowed']:
                return {'status': 'rejected', 'error': allowed['reason']}
            visible = {target for target in caller.get('item_bases', {})
                if (target == anchor or self._descendant_path(target, anchor))
                and self.validate_target(caller_job_id, actor, target, 'prepare_private')['allowed']}
            if not visible:
                return []
            fields = ('id', 'item_id', 'actor', 'requested_by', 'parent_job_id', 'root_job_id',
                'capability', 'mandate_id', 'bot_id', 'purpose', 'expected_version',
                'max_cost_usd', 'max_runtime_seconds', 'max_retries', 'max_descendants',
                'delivery', 'stop_requested', 'terminal', 'native', 'integration', 'integration_error',
                'terminal_resolution', 'domain_operation_id', 'charged_cost_usd', 'observed_runtime_seconds')
            # Complete per-item walks (paginated): only runs whose item is in
            # the visible scope (typically 1-3 items), never the global
            # history, and never truncated by an arbitrary LIMIT.
            result = []
            for target in sorted(visible):
                for rid in self._iter_run_ids_by_item(target):
                    run = self._run_row(rid)
                    if run is None:
                        continue
                    cycle = self._cycle_row(run["cycle_id"])
                    job = self._job_from_rows(cycle, run)
                    if job['item_id'] not in visible:
                        continue
                    record = {key: copy.deepcopy(job[key]) for key in fields if key in job}
                    record['last_observation'] = copy.deepcopy(job['observations'][-1]) if job.get('observations') else None
                    result.append(record)
            return result

    def pending(self):
        # Active projection without LIMIT truncation: the live set stays small
        # by protocol (single global native slot, max_active admissions,
        # deferred bounded per family), and every live run must be visible.
        with self.store.lock:
            try:
                self._require_migrated()
            except ValueError:
                if self._legacy_has_jobs():
                    raise
                return []
            rows = self._active_run_rows()
            out = []
            for r in rows:
                run = self._run_row(r["id"])
                if run is None:
                    continue
                cycle = self._cycle_row(run["cycle_id"])
                out.append(self._job_from_rows(cycle, run))
            return out

    def validate(self, job_id, capability):
        with self.store.lock:
            try:
                state = self._load()
                run = self._run_row(job_id)
                if run is None:
                    return {"allowed": False, "reason": "job_not_found"}
                cycle = self._cycle_row(run["cycle_id"])
                job = self._job_from_rows(cycle, run)
                self._vigent(state, job, capability)
                if job["delivery"] == "deferred":
                    raise ValueError("dispatch_deferred")
                # Bounded subtree fetch: only assignments below this attempt
                # count against its limits. The root family's total stays in
                # _budget/parent-allocation checks, never subtracted twice here.
                subtree = self._subtree_run_details(job_id)
                descendants = [c for c in subtree if c["id"] != job_id]
                limits = {}
                for key in ("max_cost_usd", "max_runtime_seconds"):
                    limits[key] = job[key] - sum(c.get(key, 0) for c in descendants)
                limits.update(cost_control=not self._daily(), max_retries=job["max_retries"], max_descendants=job["max_descendants"] - len(descendants))
                return {"allowed": True, "reason": None, "limits": limits,
                        "current_version": self.service.get_item(job["item_id"])["version"]}
            except (ValueError, KeyError) as error:
                return {"allowed": False, "reason": str(error)}

    def _family_run_details(self, job):
        # Bounded family fetch for budget/descendant checks (few rows).
        run = self._run_row(job["id"])
        if run is None:
            return []
        cycle_id = run["cycle_id"]
        # Find root cycle via parent_cycle chain (bounded walk).
        cur = cycle_id
        root_cycle = cur
        for _ in range(16):
            crow = self._cycle_row(cur)
            if crow is None or not crow["parent_cycle_id"]:
                root_cycle = cur
                break
            root_cycle = crow["parent_cycle_id"]
            cur = root_cycle
        # Collect descendant cycles (bounded, families tiny).
        family_cycles = [root_cycle]
        frontier = [root_cycle]
        while frontier:
            nxt = []
            for cid in frontier:
                for rr in self.store.db.execute(
                        "SELECT id FROM work_cycles WHERE parent_cycle_id=?", (cid,)).fetchall():
                    if rr["id"] not in family_cycles:
                        family_cycles.append(rr["id"])
                        nxt.append(rr["id"])
            frontier = nxt
            if len(family_cycles) > 32:
                break
        placeholders = ",".join("?" for _ in family_cycles)
        rows = self.store.db.execute(
            f"SELECT id, detail_json FROM runs WHERE cycle_id IN ({placeholders})", tuple(family_cycles)).fetchall()
        out = []
        for rr in rows:
            try:
                d = json.loads(rr["detail_json"]) if rr["detail_json"] else {}
            except ValueError:
                d = {}
            out.append({"id": rr["id"], "max_cost_usd": d.get("max_cost_usd", 0),
                        "max_runtime_seconds": d.get("max_runtime_seconds", 0),
                        "max_descendants": d.get("max_descendants", 0),
                        "parent_job_id": self._run_row(rr["id"])["parent_run_id"] if self._run_row(rr["id"]) else None})
        # Enrich parent ids without extra large decodes (single-row lookups above
        # already bounded; families are tiny so this stays bounded).
        return out

    def _subtree_run_details(self, job_id):
        # Bounded descendant walk from one run via parent_run_id (families are
        # tiny: max_descendants per config). Returns the run itself plus its
        # subtree with assignment fields, for per-attempt limit accounting.
        # Root-level accounting stays separate (see validate/_budget).
        seen = {job_id}
        queue = [job_id]
        ids = []
        while queue:
            current = queue.pop(0)
            ids.append(current)
            for r in self.store.db.execute(
                    "SELECT id FROM runs WHERE parent_run_id=?", (current,)).fetchall():
                if r["id"] not in seen:
                    seen.add(r["id"])
                    queue.append(r["id"])
                if len(seen) > 64:
                    break
            if len(seen) > 64:
                break
        out = []
        for rid in ids:
            row = self._run_row(rid)
            if row is None:
                continue
            try:
                d = json.loads(row["detail_json"]) if row["detail_json"] else {}
            except ValueError:
                d = {}
            out.append({"id": rid, "max_cost_usd": d.get("max_cost_usd", 0),
                        "max_runtime_seconds": d.get("max_runtime_seconds", 0),
                        "max_descendants": d.get("max_descendants", 0),
                        "parent_job_id": row["parent_run_id"]})
        return out

    def _native(self, state, job, native):
        if not isinstance(native, dict) or not all(isinstance(native.get(k), str) and native[k] for k in ("provider", "host", "profile", "id")):
            raise ValueError("native_identity_required")
        route = job.get("route") or {}
        if native["host"] != route.get("host") or native["profile"] != route.get("profile"):
            raise ValueError("native_route_mismatch")
        if job.get("native") and job["native"] != native:
            raise ValueError("native_identity_changed")
        # Bounded uniqueness check: single indexed lookup, never global decode.
        # SQLite UNIQUE also guards; this gives the legacy contract error.
        row = self.store.db.execute(
            "SELECT id FROM runs WHERE native_provider=? AND native_host=? AND native_profile=? AND native_id=? LIMIT 1",
            (native["provider"], native["host"], native["profile"], native["id"])).fetchone()
        if row and row["id"] != job["id"]:
            raise ValueError("native_identity_already_accounted")

    def claim_dispatch(self, job_id):
        """Durably claim the single global native slot before any remote effect.

        Pure storage transaction: no network inside. On success the run is
        `dispatching` (or already was, with no native identity yet: duplicate),
        so a later remote creation cannot collide with another execution.
        Uncertainty keeps the claim: only terminality, STOP handling or an
        explicit reconciled failure releases it. Returns a structured receipt,
        never a raw SQL error.
        """
        with self.store.transaction():
            try:
                self._require_migrated()
                run = self._run_row(job_id)
                if run is None:
                    raise ValueError("job_not_found")
                try:
                    detail = json.loads(run["detail_json"]) if run["detail_json"] else {}
                except ValueError:
                    detail = {}
                if detail.get("delivery") == "deferred":
                    raise ValueError("dispatch_deferred")
                if run["state"] in self.RUN_TERMINAL:
                    raise ValueError("terminal_job")
                if detail.get("stop_requested") or run["state"] == "stop_requested":
                    raise ValueError("stop_requested")
                if run["native_provider"] is not None or run["native_id"] is not None:
                    cycle = self._cycle_row(run["cycle_id"])
                    return {"status": "claimed", "job": self._job_from_rows(cycle, run), "duplicate": True}
                if run["state"] in ("dispatching", "uncertain"):
                    cycle = self._cycle_row(run["cycle_id"])
                    return {"status": "claimed", "job": self._job_from_rows(cycle, run), "duplicate": True}
                if run["state"] != "reserved":
                    raise ValueError("slot_not_claimable")
                now_iso = self._clock().isoformat()
                try:
                    self.store.db.execute(
                        "UPDATE runs SET state='dispatching', started_at=COALESCE(started_at,?) WHERE id=?",
                        (now_iso, job_id))
                except sqlite3.IntegrityError as exc:
                    if "one_native_active" in str(exc).lower():
                        raise ValueError("native_slot_busy")
                    raise
                if run["state"] == "reserved":
                    cycle = self._cycle_row(run["cycle_id"])
                    if cycle and cycle["state"] in ("ready", "waiting", "paused"):
                        self.store.db.execute("UPDATE work_cycles SET state='running' WHERE id=?", (cycle["id"],))
                run2 = self._run_row(job_id)
                cycle2 = self._cycle_row(run2["cycle_id"])
                return {"status": "claimed", "job": self._job_from_rows(cycle2, run2)}
            except (ValueError, KeyError) as error:
                return {"status": "rejected", "error": str(error)}

    def record_dispatch(self, job_id, native):
        with self.store.transaction():
            try:
                self._require_migrated()
                run = self._run_row(job_id)
                if run is None:
                    raise ValueError("job_not_found")
                cycle = self._cycle_row(run["cycle_id"])
                job = self._job_from_rows(cycle, run)
                self._native(self._load(), job, native)
                # Recording an already dispatched effect remains possible after revocation.
                detail = json.loads(run["detail_json"]) if run["detail_json"] else {}
                detail["delivery"] = "acknowledged"
                # Keep the full provider identity (facets beyond the indexed
                # quadruple) so later observations compare equal.
                detail["native"] = copy.deepcopy(native)
                # State: reserved -> dispatching (takes the global slot;
                # one_native_active partial index guards single execution).
                new_state = "dispatching" if run["state"] == "reserved" else run["state"]
                now_iso = self._clock().isoformat()
                try:
                    self.store.db.execute(
                        "UPDATE runs SET native_provider=?, native_host=?, native_profile=?, native_id=?, "
                        "state=?, detail_json=?, started_at=COALESCE(started_at,?) WHERE id=?",
                        (native["provider"], native["host"], native["profile"], native["id"],
                         new_state, _json(detail), now_iso, job_id))
                except sqlite3.IntegrityError as exc:
                    msg = str(exc).lower()
                    if "one_native_active" in msg:
                        raise ValueError("concurrency_exhausted")
                    if "unique" in msg:
                        raise ValueError("native_identity_already_accounted")
                    raise
                # Cycle follows the attempt into running (bounded single-row).
                if cycle and cycle["state"] in ("ready", "waiting"):
                    self.store.db.execute("UPDATE work_cycles SET state='running' WHERE id=?", (cycle["id"],))
                run2 = self._run_row(job_id)
                cycle2 = self._cycle_row(run2["cycle_id"])
                return {"status": "recorded", "job": self._job_from_rows(cycle2, run2)}
            except (ValueError, KeyError) as error:
                return {"status": "rejected", "error": str(error)}

    def _observe(self, state, job_id, observation):
        # Table-backed observation with monotonic consumption and correlated
        # run_observations. SQLite guards FK/CHECK/UNIQUE; service guards
        # admission immutability, monotonicity and terminal/integration split
        # inside this same transaction.
        run = self._run_row(job_id)
        if run is None:
            raise ValueError("job_not_found")
        cycle = self._cycle_row(run["cycle_id"])
        job = self._job_from_rows(cycle, run)
        native = observation.get("native_identity")
        self._native(state, job, native)
        status = observation.get("native_status")
        terminal = observation.get("terminal")
        if type(terminal) is not bool or status not in self.TERMINAL | self.LIVE or terminal != (status in self.TERMINAL):
            raise ValueError("invalid_native_status")
        if not observation.get("evidence_reference") or not _number(observation.get("runtime_seconds")):
            raise ValueError("observation_evidence_required")
        cost = observation.get("cost_usd")
        if cost is not None and not _number(cost):
            raise ValueError("invalid_observed_cost")
        # Last observation for duplicate/conflict (bounded single-row).
        last_row = self.store.db.execute(
            "SELECT receipt_json FROM run_observations WHERE run_id=? ORDER BY seq DESC LIMIT 1",
            (job_id,)).fetchone()
        last_obs = json.loads(last_row["receipt_json"]) if last_row else None
        terminal_now = run["state"] in self.RUN_TERMINAL
        if terminal_now:
            if last_obs is not None and observation == last_obs:
                return {"status": "recorded", "duplicate": True, "job": job}
            raise ValueError("terminal_observation_conflict")
        detail = json.loads(run["detail_json"]) if run["detail_json"] else {}
        charged = detail.get("charged_cost_usd", 0)
        observed_prev = run["observed_seconds"] or 0
        if cost is not None and cost < charged:
            raise ValueError("cost_regressed")
        if observation["runtime_seconds"] < observed_prev:
            raise ValueError("runtime_regressed")
        # Correlated observation row: seq monotonic per run, receipt immutable.
        # The insert and the run/cycle updates below form one atomic unit: a
        # savepoint rolls everything back if a later constraint (global native
        # exclusion, native uniqueness) rejects the observation, so a rejected
        # receipt never leaves a partial observation row behind.
        seq_row = self.store.db.execute(
            "SELECT COALESCE(MAX(seq),0) FROM run_observations WHERE run_id=?", (job_id,)).fetchone()
        seq = (seq_row[0] or 0) + 1
        now_iso = self._clock().isoformat()
        self.store.db.execute("SAVEPOINT observe_unit")
        # observed_at is required for new rows (migrated rows may carry NULL
        # with provenance); service enforces, SQLite allows NULL for history.
        self.store.db.execute(
            "INSERT INTO run_observations(run_id,seq,observed_at,native_state,"
            "runtime_seconds,cost_usd,receipt_json) VALUES(?,?,?,?,?,?,?)",
            (job_id, seq, now_iso, status,
             float(observation["runtime_seconds"]), cost, _json(observation)))
        # Map native terminality to run state; integration stays separate.
        if status == "completed":
            new_state = "completed" if terminal else "running"
        elif status == "failed":
            new_state = "failed" if terminal else "running"
        elif status == "cancelled":
            new_state = "cancelled" if terminal else "stop_requested"
        elif status in ("uncertain", "not_found"):
            # Uncertain keeps the global slot until reconciled; timeout never
            # proves detention.
            new_state = "uncertain"
        elif status in ("queued", "waiting"):
            new_state = "running" if run["state"] in ("dispatching", "reserved") else run["state"]
        else:  # running
            new_state = "running" if not terminal else "completed"
        if terminal and status in ("queued", "running", "waiting"):
            # Defensive: terminal must agree with native terminal set above;
            # already validated, keep running->completed mapping.
            new_state = "completed"
        delivery = "uncertain" if status in {"uncertain", "not_found"} else "acknowledged"
        detail["delivery"] = delivery
        detail["native"] = copy.deepcopy(native)
        # Monotonic cumulative consumption: never sum accumulated polls twice.
        # Unknown cost stays NULL in the column; charged detail stays
        # conservative for budget without inventing zero.
        new_observed = float(observation["runtime_seconds"])
        if terminal:
            # Children draw allocations from the root, not extra reservations.
            # Legacy rule: only the root subtracts its descendants; non-roots
            # charge their own max (their allocation already came from root).
            is_root = (detail.get("root_job_id", job_id) == job_id)
            if is_root:
                fam = self._family_run_details(job)
                children = [c for c in fam if c["id"] != job_id]
            else:
                children = []
            own_max = max(0, detail.get("max_cost_usd", 0) - sum(c.get("max_cost_usd", 0) for c in children))
            if cost is None:
                detail["charged_cost_usd"] = max(own_max, charged)
            else:
                detail["charged_cost_usd"] = cost
            new_cost_col = cost  # NULL when unknown, never zero-invented.
            new_integration = "discarded" if status != "completed" else run["integration"]
        else:
            if cost is not None:
                detail["charged_cost_usd"] = max(charged, cost)
            new_cost_col = cost if cost is not None else run["cost_usd"]
            new_integration = run["integration"]
        try:
            self.store.db.execute(
                "UPDATE runs SET native_provider=?, native_host=?, native_profile=?, native_id=?, "
                "state=?, integration=?, detail_json=?, observed_seconds=?, cost_usd=?, "
                "ended_at=CASE WHEN ? IN ('completed','failed','cancelled','expired') THEN ? ELSE ended_at END "
                "WHERE id=?",
                (native["provider"], native["host"], native["profile"], native["id"],
                 new_state, new_integration, _json(detail), new_observed, new_cost_col,
                 new_state, now_iso if terminal else None, job_id))
            # Cycle follows terminality (bounded single-row); integration stays
            # pending for completed until accept/integrate proves it. Completed
            # moves to waiting (frees the one-open slot for a successor with new
            # cause, but does not autorenew budget); failed/cancelled abandons.
            if cycle:
                if new_state in ("failed", "cancelled", "expired"):
                    self.store.db.execute("UPDATE work_cycles SET state='abandoned', closed_at=? WHERE id=?",
                        (now_iso, cycle["id"]))
                elif new_state == "completed":
                    self.store.db.execute("UPDATE work_cycles SET state='waiting' WHERE id=?", (cycle["id"],))
                elif new_state == "uncertain":
                    # Keep running; uncertain keeps the slot, never frees it.
                    pass
        except sqlite3.IntegrityError as exc:
            # Revert the whole observation unit: a rejected receipt must never
            # leave a partial observation row behind. External-effect evidence,
            # if any, is not silently kept; the caller must reconcile identity,
            # consumption and uncertain state explicitly before retrying.
            self.store.db.execute("ROLLBACK TO observe_unit")
            self.store.db.execute("RELEASE observe_unit")
            msg = str(exc).lower()
            if "one_native_active" in msg:
                raise ValueError("concurrency_exhausted")
            if "unique" in msg:
                raise ValueError("native_identity_already_accounted")
            raise
        self.store.db.execute("RELEASE observe_unit")
        run2 = self._run_row(job_id)
        cycle2 = self._cycle_row(run2["cycle_id"])
        job2 = self._job_from_rows(cycle2, run2)
        if terminal_now:
            return {"status": "recorded", "duplicate": True, "job": job2}
        return {"status": "recorded", "job": job2}

    def observe(self, job_id, observation):
        """Record trusted native identity/status/evidence and cumulative consumption.

        Consumption is exclusive of separately registered descendants; unknown
        cost is None. Network errors/not_found are nonterminal. Provider limits
        must be enforced by the adapter using validate's shared allocation.
        """
        with self.store.transaction():
            try:
                result = self._observe(self._load(), job_id, observation)
                return copy.deepcopy(result)
            except (ValueError, KeyError, TypeError) as error:
                return {"status": "rejected", "error": str(error)}

    def request_stop(self, actor, operation_id, job_id):
        def apply(state):
            self._manager(actor)
            self._require_migrated()
            run = self._run_row(job_id)
            if run is None:
                raise ValueError("job_not_found")
            # Bounded descendant walk (families tiny, at most a few rows).
            affected = {job_id}
            while True:
                placeholders = ",".join("?" for _ in affected)
                rows = self.store.db.execute(
                    f"SELECT id FROM runs WHERE parent_run_id IN ({placeholders})", tuple(affected)).fetchall()
                expanded = affected | {r["id"] for r in rows}
                if expanded == affected:
                    break
                affected = expanded
                if len(affected) > 32:
                    break
            # A trusted scheduler context, never a caller-supplied reason or
            # operation-id prefix, distinguishes yielding from a manager stop.
            technical = actor != self.service.owner_actor and job_id in self._technical_stops.get()
            if not technical:
                for record in state.get('attention_displacements', {}).values():
                    if affected.intersection(set(record.get('family', []))) or record.get('new_job_id') in affected:
                        record.update(status='cancelled', blocker='stop_requested',
                            cancel_version=self.service.get_item(record['item_id'])['version'])
                        resumed = record.get('new_job_id')
                        if resumed:
                            # Bounded: runs sharing the resumed root (few).
                            rrow = self._run_row(resumed)
                            if rrow is not None:
                                rcycle = rrow["cycle_id"]
                                for rr in self.store.db.execute(
                                        "SELECT id FROM runs WHERE cycle_id=?", (rcycle,)).fetchall():
                                    affected.add(rr["id"])
            for identity in sorted(affected):
                r = self._run_row(identity)
                if r is None:
                    continue
                try:
                    d = json.loads(r["detail_json"]) if r["detail_json"] else {}
                except ValueError:
                    d = {}
                d["stop_requested"] = True
                # STOP keeps the native slot until terminality is observed.
                # Undispatched reservations (reserved, no native) stay reserved
                # with the stop flag; only dispatched runs take stop_requested,
                # preserving the single global native slot (one_native_active).
                # Deferred resolves administratively via _resolve_undispatched.
                new_state = r["state"]
                if r["state"] in ("dispatching", "running", "waiting_child", "uncertain"):
                    new_state = "stop_requested"
                self.store.db.execute(
                    "UPDATE runs SET detail_json=?, state=? WHERE id=?", (_json(d), new_state, identity))
                # Re-read for _resolve_undispatched compat (bounded single-row).
                r2 = self._run_row(identity)
                c2 = self._cycle_row(r2["cycle_id"]) if r2 else None
                if r2 is not None and c2 is not None:
                    j2 = self._job_from_rows(c2, r2)
                    self._resolve_undispatched(state, j2, 'stop_requested')
                    # _resolve_undispatched may have marked terminal discarded;
                    # persist its decision back to tables (bounded).
                    # It mutates the passed dict; reflect stop + terminal.
                    r3 = self._run_row(identity)
                    if r3 is not None:
                        try:
                            d3 = json.loads(r3["detail_json"]) if r3["detail_json"] else {}
                        except ValueError:
                            d3 = {}
                        d3["stop_requested"] = True
                        if j2.get("terminal") and j2.get("integration") == "discarded":
                            d3.update({k: j2[k] for k in ("terminal_resolution", "integration_error") if k in j2})
                            self.store.db.execute(
                                "UPDATE runs SET detail_json=?, state='cancelled', integration='discarded' WHERE id=?",
                                (_json(d3), identity))
                        else:
                            self.store.db.execute(
                                "UPDATE runs SET detail_json=?, state=? WHERE id=?", (_json(d3), new_state, identity))
            cycle = self._cycle_row(run["cycle_id"])
            job = self._job_from_rows(cycle, self._run_row(job_id))
            return {"status": "stop_requested", "job": job, "affected_job_ids": sorted(affected)}
        return self._operation(actor, operation_id, "request_stop", job_id, apply)

    def _attention_window(self, item):
        """Owner fields or the principal's recorded direct-owner interpretation.

        This validates provenance, not linguistic entailment. Source content
        alone and arbitrary principal edits never establish scheduling authority.
        """
        if not item or item.get('status') != 'active' or not _number(item.get('priority')):
            return None
        row = self.store.db.execute('SELECT field_versions FROM items WHERE id=?', (item['id'],)).fetchone()
        fields = json.loads(row[0])
        for key in ('priority', 'decision_at'):
            provenance = fields.get(key, {})
            if provenance.get('actor') == self.service.owner_actor:
                continue
            if provenance.get('actor') != self.service.principal_actor:
                return None
            row = self.store.db.execute('SELECT * FROM operations WHERE item_id=? AND applied_version=? AND actor=?',
                (item['id'], provenance.get('version'), self.service.principal_actor)).fetchone()
            if not row:
                return None
            receipt = json.loads(row['receipt'])
            snapshot = receipt.get('item', {})
            intent = snapshot.get('intent_basis', {})
            after = json.loads(row['after_patch'] or '{}')
            if (receipt.get('status') != 'applied' or key not in after or 'intent_basis' not in after
                    or intent.get('interpreted_by') != self.service.principal_actor
                    or snapshot.get(key) != item.get(key)
                    or snapshot.get('source_revisions') != item.get('source_revisions')
                    or snapshot.get('source') != item.get('source')):
                return None
            previous = copy.deepcopy(snapshot)
            for field, entry in json.loads(row['before_patch'] or '{}').items():
                if entry['present']:
                    previous[field] = entry['value']
                else:
                    previous.pop(field, None)
            try:
                self.service._validate_intent_basis(previous,
                    {field: intent.get(field) for field in ('quote', 'source_item_id')}, proposed_entry=True)
            except ValueError:
                return None
        try:
            instant = datetime.fromisoformat(item['decision_at'])
            return instant.timestamp() if instant.utcoffset() is not None else None
        except (TypeError, ValueError, KeyError):
            return None

    @contextmanager
    def _attention_stop_context(self, old_job_id):
        with self.store.lock:
            record = self._load().get('attention_displacements', {}).get(old_job_id)
            family = frozenset(record['family']) if record else frozenset()
        token = self._technical_stops.set(family)
        try:
            yield
        finally:
            self._technical_stops.reset(token)

    def _begin_attention_displacement(self, actor, job_id, beneficiary_id):
        """Persist a bounded continuation intention before any native stop."""
        with self.store.transaction():
            state = self._load()
            try:
                self._manager(actor)
                self._require_migrated()
                config = self._configuration(state)
                records = state.setdefault('attention_displacements', {})
                if job_id in records:
                    return dict(status='recorded', displacement=copy.deepcopy(records[job_id]))
                beneficiary = self.service.get_item(beneficiary_id)
                deadline = self._attention_window(beneficiary)
                if deadline is None or deadline <= datetime.now(timezone.utc).timestamp():
                    raise ValueError('attention_window_unavailable')
                run = self._run_row(job_id)
                if run is None:
                    raise ValueError('job_not_found')
                cycle = self._cycle_row(run["cycle_id"])
                job = self._job_from_rows(cycle, run)
                if job['parent_job_id'] or job.get('attention_origin') or job['actor'] != actor:
                    raise ValueError('attention_root_required')
                # Bounded family: runs sharing the root lineage (few).
                try:
                    fam_details = self._family_run_details(job)
                except ValueError:
                    fam_details = []
                family = []
                for c in fam_details:
                    cr = self._run_row(c["id"])
                    if cr is None:
                        continue
                    cc = self._cycle_row(cr["cycle_id"])
                    try:
                        family.append(self._job_from_rows(cc, cr))
                    except Exception:
                        continue
                # Ensure the root itself is included (family details may miss
                # singletons if lineage walk is empty).
                if not any(f["id"] == job_id for f in family):
                    family = [job] + family
                if job['terminal'] or any(j['stop_requested'] or j['capability'] != 'prepare_private' for j in family):
                    raise ValueError('attention_work_not_interruptible')
                for member in family:
                    if not member['terminal']:
                        self._vigent(state, member, member['capability'])
                    item = self.service.get_item(member['item_id'])
                    window = item.get('decision_at')
                    if window:
                        try:
                            instant = datetime.fromisoformat(window)
                            if instant.utcoffset() is None or instant.timestamp() <= deadline:
                                raise ValueError('attention_work_not_postponable')
                        except (ValueError, TypeError):
                            raise ValueError('attention_work_not_postponable') from None
                    priority = item.get('priority', 0)
                    if not _number(priority) or priority >= beneficiary['priority']:
                        raise ValueError('attention_priority_not_lower')
                sources = sorted({sid for j in family for sid in [j['item_id'], *j.get('source_bases', {})]})
                record = dict(old_job_id=job_id, item_id=job['item_id'], item_version=self.service.get_item(job['item_id'])['version'],
                    family=[j['id'] for j in family], beneficiary_id=beneficiary_id, deadline=deadline,
                    period=copy.deepcopy(config), budget_period_id=job.get("budget_period_id"), sources=sources,
                    input_basis=self.service.work_input_basis(job['item_id'], sources, include_evidence=False),
                    status='stopping', stop_delivery='intent', blocker='attention_stop_pending')
                records[job_id] = record
                self._save(state)
                return dict(status='recorded', displacement=copy.deepcopy(record))
            except (ValueError, KeyError, TypeError) as error:
                return dict(status='rejected', error=str(error))

    def _attention_stop_delivery(self, job_id, phase):
        with self.store.transaction():
            state = self._load()
            state['attention_displacements'][job_id]['stop_delivery'] = phase
            self._save(state)

    def _reserve_attention_continuation(self, actor, old_job_id):
        """One atomic NEW admission per displacement, never a reset of old work."""
        with self.store.transaction():
            state = self._load()
            try:
                record = state['attention_displacements'][old_job_id]
            except KeyError:
                return dict(status='rejected', error='attention_record_not_found')
            if record.get('new_job_id'):
                try:
                    dup_run = self._run_row(record['new_job_id'])
                    dup_cycle = self._cycle_row(dup_run["cycle_id"]) if dup_run else None
                    dup_job = self._job_from_rows(dup_cycle, dup_run) if dup_run else None
                except (ValueError, KeyError, TypeError):
                    dup_job = None
                return dict(status='reserved', job_id=record['new_job_id'],
                            job=copy.deepcopy(dup_job), duplicate=True)
            if record['status'] == 'cancelled':
                return dict(status='rejected', error=record['blocker'])
            try:
                self._manager(actor)
                self._require_migrated()
                self._configuration(state)
                if (record['period'] != self.config or record['period'] != state.get('config')
                        or (self._daily() and record.get('budget_period_id') != self._period(self.config)['id'])):
                    raise ValueError('attention_budget_period_changed')
                for jid in record.get('family', []):
                    jj = self._run_row(jid)
                    if jj is None:
                        raise ValueError('attention_family_not_stopped')
                    cc = self._cycle_row(jj["cycle_id"])
                    jjd = self._job_from_rows(cc, jj)
                    if not jjd.get('terminal'):
                        raise ValueError('attention_family_not_stopped')
                if self.service.work_input_basis(record['item_id'], record['sources'], include_evidence=False) != record['input_basis']:
                    raise ValueError('attention_input_changed')
                old_run = self._run_row(old_job_id)
                if old_run is None:
                    raise ValueError('job_not_found')
                old_cycle = self._cycle_row(old_run["cycle_id"])
                old = self._job_from_rows(old_cycle, old_run)
                if actor != old['actor'] or state.get('bots', {}).get(old['bot_id'], {}).get('actor', actor) != old['actor']:
                    raise ValueError('attention_actor_changed')
                # Verified progress can advance the old job's bases; arbitrary
                # changes cannot. Keep both its live bases and external anchor.
                for jid in record.get('family', []):
                    fr = self._run_row(jid)
                    if fr is None:
                        raise ValueError('attention_family_not_stopped')
                    fc = self._cycle_row(fr["cycle_id"])
                    fj = self._job_from_rows(fc, fr)
                    shadow = copy.deepcopy(fj)
                    shadow.update(stop_requested=False, terminal=False)
                    self._vigent(state, shadow, shadow['capability'], integration=True)
                item = self.service.get_item(old['item_id'])
                if item['status'] != 'active' or self.service.work_resolution_current(item['id']):
                    raise ValueError('attention_work_resolved_or_inactive')
                request = {k: old[k] for k in ('item_id', 'mandate_id', 'capability', 'bot_id', 'purpose', 'scope',
                    'max_cost_usd', 'max_runtime_seconds', 'max_retries', 'max_descendants')}
                request['expected_version'] = item['version']
                op_id = 'gtd-attention-continuation:' + old_job_id
                receipt = self._reserve(state, actor, op_id, request)
                if receipt.get('status') != 'reserved':
                    raise ValueError(receipt.get('error', 'attention_continuation_unavailable'))
                # Mark deferred + attention origin in the new run's detail
                # (admission stays immutable).
                new_run = self._run_row(receipt['job_id'])
                try:
                    nd = json.loads(new_run["detail_json"]) if new_run and new_run["detail_json"] else {}
                except ValueError:
                    nd = {}
                nd['attention_origin'] = old_job_id
                nd['delivery'] = 'deferred'
                self.store.db.execute("UPDATE runs SET detail_json=? WHERE id=?", (_json(nd), receipt['job_id']))
                record.update(status='resumed', blocker=None, new_job_id=receipt['job_id'])
                self._save(state)
                run2 = self._run_row(receipt['job_id'])
                cycle2 = self._cycle_row(run2["cycle_id"]) if run2 else None
                job2 = self._job_from_rows(cycle2, run2) if run2 else receipt.get('job')
                return dict(status='reserved', job_id=receipt['job_id'], job=copy.deepcopy(job2))
            except (ValueError, KeyError, TypeError) as error:
                reason = str(error)
                record.update(status='waiting', blocker=reason)
                if reason in {'attention_input_changed', 'stale_item_version', 'source_version_stale',
                              'mandate_not_active', 'attention_work_resolved_or_inactive'}:
                    record['status'] = 'cancelled'
                self._save(state)
                return dict(status='rejected', error=reason)

    def accept_result(self, actor, operation_id, job_id, result):
        def apply(state):
            self._manager(actor)
            self._require_migrated()
            run = self._run_row(job_id)
            if run is None:
                raise ValueError("job_not_found")
            cycle = self._cycle_row(run["cycle_id"])
            job = self._job_from_rows(cycle, run)
            self._vigent(state, job, job["capability"], integration=True)
            # Terminal success: run completed (native completed) and terminal.
            if run["state"] != "completed":
                # Fall back to legacy job view for compat (terminal bool + last obs).
                if not job.get("terminal"):
                    raise ValueError("terminal_success_required")
                last = job.get("observations", [{}])[-1] if job.get("observations") else {}
                if last.get("native_status") != "completed":
                    raise ValueError("terminal_success_required")
            else:
                # Verify last observation is completed (bounded single-row).
                last_row = self.store.db.execute(
                    "SELECT receipt_json FROM run_observations WHERE run_id=? ORDER BY seq DESC LIMIT 1",
                    (job_id,)).fetchone()
                last = json.loads(last_row["receipt_json"]) if last_row else {}
                if last.get("native_status") != "completed":
                    raise ValueError("terminal_success_required")
            if run["integration"] != "pending":
                # Legacy accepted_pending_integration maps to pending in the
                # new enum; detail preserves the intermediate for compat.
                try:
                    d0 = json.loads(run["detail_json"]) if run["detail_json"] else {}
                except ValueError:
                    d0 = {}
                if d0.get("integration") not in (None, "pending") and run["integration"] != "pending":
                    raise ValueError("result_already_integrated")
                if run["integration"] != "pending":
                    raise ValueError("result_already_integrated")
            if result.get("criteria_met") is not True or not all(isinstance(result.get(k), str) and result[k].strip() for k in ("evidence_reference", "artifact_reference")):
                raise ValueError("result_evidence_required")
            try:
                detail = json.loads(run["detail_json"]) if run["detail_json"] else {}
            except ValueError:
                detail = {}
            detail["result"] = copy.deepcopy(result)
            detail["integration"] = "accepted_pending_integration"
            detail["validated_version"] = self.service.get_item(job["item_id"])["version"]
            # New enum stays pending until record_integration proves the domain
            # receipt; detail carries the accepted intermediate for compat.
            self.store.db.execute(
                "UPDATE runs SET detail_json=? WHERE id=?", (_json(detail), job_id))
            run2 = self._run_row(job_id)
            cycle2 = self._cycle_row(run2["cycle_id"])
            job2 = self._job_from_rows(cycle2, run2)
            # Expose accepted intermediate in the compat view.
            job2["integration"] = "accepted_pending_integration"
            job2["result"] = copy.deepcopy(result)
            job2["validated_version"] = detail["validated_version"]
            return {"status": "accepted", "job": job2}
        return self._operation(actor, operation_id, "accept_result", [job_id, result], apply)

    def reconcile(self, actor, operation_id, observations):
        def apply(state):
            if self.service.actor_role(actor) != "owner":
                raise ValueError("owner_required")
            self._require_migrated()
            # Apply observations atomically in this transaction; invalid batches
            # roll back via the surrounding Store.transaction (no partial).
            for observation in observations:
                res = self._observe(state, observation["job_id"], {k: v for k, v in observation.items() if k != "job_id"})
                if res.get("status") != "recorded":
                    raise ValueError(res.get("error", "reconcile_observation_rejected"))
            # Bounded unresolved check: active rows only (few), never history.
            remaining = self.store.db.execute(
                "SELECT runs.id, runs.detail_json FROM runs WHERE state NOT IN "
                "('completed','failed','cancelled','expired') LIMIT 1").fetchone()
            if remaining:
                raise ValueError("unresolved_execution")
            uncertain = self.store.db.execute(
                "SELECT 1 FROM runs WHERE state='uncertain' LIMIT 1").fetchone()
            if uncertain:
                raise ValueError("unresolved_execution")
            # Uncertain delivery lives in detail for completed-uncertain edge?
            # New uncertain runs are already caught above via state.
            if self.store.db.execute(
                    "SELECT 1 FROM deliveries WHERE state != 'confirmed' LIMIT 1").fetchone():
                raise ValueError("unresolved_output")
            from .effects import ExternalEffects
            if ExternalEffects(self.service).pending():
                raise ValueError('unresolved_external_effects')
            self.store.db.execute("INSERT OR REPLACE INTO metadata VALUES('recovery_required','false')")
            return {"status": "reconciled"}
        return self._operation(actor, operation_id, "reconcile", observations, apply)

    def record_integration(self, job_id, domain_receipt):
        """Trusted integration acknowledgement; verify the actual stored receipt.

        Domain execution happens separately with expected_version from acceptance.
        This method never calls execute and cannot make a stale result current.
        """
        with self.store.transaction():
            try:
                self._require_migrated()
                run = self._run_row(job_id)
                if run is None:
                    raise ValueError("job_not_found")
                cycle = self._cycle_row(run["cycle_id"])
                job = self._job_from_rows(cycle, run)
                try:
                    detail0 = json.loads(run["detail_json"]) if run["detail_json"] else {}
                except ValueError:
                    detail0 = {}
                if detail0.get("integration") != "accepted_pending_integration" and run["integration"] != "pending":
                    # New enum stays pending until here; legacy intermediate lives
                    # in detail. Both must show accepted before integration.
                    if not (run["integration"] == "pending" and detail0.get("integration") == "accepted_pending_integration"):
                        raise ValueError("accepted_result_required")
                if run["integration"] == "integrated" or detail0.get("integration") == "integrated":
                    raise ValueError("accepted_result_required")
                operation_id = domain_receipt.get("operation_id")
                row = self.store.db.execute("SELECT receipt,after_patch,applied_version,item_id FROM operations WHERE operation_id=?", (operation_id,)).fetchone()
                if not row or json.loads(row["receipt"]) != domain_receipt:
                    raise ValueError("domain_receipt_not_verified")
                after = json.loads(row["after_patch"] or "{}")
                if not {"materials", "assessments"}.intersection(after):
                    raise ValueError("domain_result_change_required")
                item = domain_receipt.get("item", {})
                current = self.service.get_item(job["item_id"])
                if domain_receipt.get("status") != "applied" or item.get("id") != job["item_id"] or row["item_id"] != job["item_id"]:
                    raise ValueError("domain_receipt_mismatch")
                # validated_version lives in detail for new rows.
                try:
                    _d = json.loads(run["detail_json"]) if run["detail_json"] else {}
                except ValueError:
                    _d = {}
                _validated = _d.get("validated_version", job.get("validated_version"))
                if item.get("version") != _validated + 1 or not current or current["version"] != item["version"]:
                    raise ValueError("integration_version_mismatch")
                _d["integration"] = "integrated"
                _d["domain_operation_id"] = operation_id
                # Keep domain_operation_ids list for compat readers.
                _ids = list(_d.get("domain_operation_ids", []) or [])
                if operation_id not in _ids:
                    _ids.append(operation_id)
                _d["domain_operation_ids"] = _ids
                now_iso = self._clock().isoformat()
                self.store.db.execute(
                    "UPDATE runs SET integration='integrated', detail_json=? WHERE id=?",
                    (_json({**json.loads(run["detail_json"] or '{}'), **_d}), job_id))
                # Resolved cycle on successful integration (bounded single-row).
                if cycle:
                    self.store.db.execute(
                        "UPDATE work_cycles SET state='resolved', closed_at=? WHERE id=?", (now_iso, cycle["id"]))
                run2 = self._run_row(job_id)
                cycle2 = self._cycle_row(run2["cycle_id"])
                job2 = self._job_from_rows(cycle2, run2)
                return {"status": "integrated", "job": copy.deepcopy(job2)}
            except (ValueError, KeyError, TypeError) as error:
                return {"status": "rejected", "error": str(error)}

    _COMPATIBLE = frozenset({"notes", "coverage", "updated_at", "version"})

    def _basis_values(self, item):
        values = {k: v for k, v in item.items() if k not in self._COMPATIBLE and k != "materials"}
        # Normalize to reference stubs: receipts keep full result arrays while
        # stored documents and admission snapshots keep stubs; both shapes must
        # compare on identity and authorship, never on raw representation.
        human_materials = [GTDDomain._material_stub(m) for m in item.get("materials", [])
                           if m.get("author") == self.service.owner_actor]
        if human_materials:
            values["materials"] = human_materials
        # Absent and empty read the same: items created before result tables
        # carry no arrays while normalized documents carry empty ones.
        if values.get("assessments"):
            values["assessments"] = [GTDDomain._assessment_stub(a) for a in values["assessments"]]
        else:
            values.pop("assessments", None)
        return values

    def _basis(self, item_id):
        """Meaning/source plus field generations detect even human change-and-undo."""
        item = self.service.get_item(item_id)
        if item is None:
            return None
        row = self.store.db.execute("SELECT field_versions FROM items WHERE id=?", (item_id,)).fetchone()
        versions = json.loads(row[0])
        return {"values": self._basis_values(item),
                "generations": {k: v["version"] for k, v in versions.items() if k not in self._COMPATIBLE and k != "materials"}}

    def _compatible_parent_coordination(self, state, job, source_id, basis):
        """Only authenticated principal coordination of a child's ancestor.

        Keep reserved bases intact. On the entrusted object only its actual
        parent job may coordinate; human meaning, sources and authority stay strict.
        """
        parent = None
        if job.get('parent_job_id'):
            # Bounded single-row parent fetch, never global history.
            prow = self._run_row(job['parent_job_id'])
            if prow is not None:
                pcycle = self._cycle_row(prow["cycle_id"])
                parent = self._job_from_rows(pcycle, prow)
        own_item = source_id == job['item_id']
        if (not parent or self.service.actor_role(parent['actor']) != 'principal'
                or (own_item and (source_id not in parent.get('item_bases', {})
                    or not self._scope_path_valid(parent, source_id)))
                or (not own_item and not self._descendant_path(job['item_id'], source_id))):
            return False
        current = self._basis(source_id)
        if not current or not basis:
            return False
        coordination = {'assessments', 'result_gap', 'plan_steps', 'uncertainties'}
        for section in ('values', 'generations'):
            if {k:v for k,v in current[section].items() if k not in coordination} != {
                    k:v for k,v in basis[section].items() if k not in coordination}:
                return False
        floor = job['expected_version'] if own_item else max(basis['generations'].values(), default=0)
        rows = self.store.db.execute('SELECT * FROM operations WHERE item_id=? AND applied_version>? ORDER BY applied_version',
                                    (source_id, floor)).fetchall()
        for row in rows:
            after = json.loads(row['after_patch'] or '{}')
            if own_item and 'materials' in after:
                # Recover only this accepted delivery's exact domain operation;
                # another material write cannot become compatible coordination.
                receipt = json.loads(row['receipt'])
                if not (job.get('integration') == 'accepted_pending_integration'
                        and row['operation_id'] == 'gtd-output:' + job['id']
                        and row['actor'] == job['actor'] and set(after) == {'materials'}
                        and receipt.get('status') == 'applied'
                        and row['applied_version'] == job.get('validated_version', -1) + 1):
                    return False
            changed = set(after) - self._COMPATIBLE - {'materials'}
            if own_item and any(not after[key].get('present') for key in changed):
                return False
            if not changed:
                continue
            if (not changed <= coordination or row['actor'] != parent['actor']):
                return False
            # Bounded coordination proof: parent alone for own-item, else the
            # small family of the job (few rows), never global history.
            if own_item:
                candidates = [parent]
            else:
                candidates = []
                try:
                    fam = self._family_run_details(job)
                    for c in fam:
                        cr = self._run_row(c["id"])
                        if cr is None:
                            continue
                        cc = self._cycle_row(cr["cycle_id"])
                        candidates.append(self._job_from_rows(cc, cr))
                except ValueError:
                    candidates = [parent]
            if not any(j['actor'] == row['actor'] and self._scope_path_valid(j, source_id)
                        and any(p['operation_id'] == row['operation_id'] for p in j.get('progress', []))
                        for j in candidates):
                return False
            if 'assessments' in changed:
                assessments = json.loads(row['receipt']).get('item', {}).get('assessments', [])
                if not assessments or assessments[-1].get('satisfied') is not False:
                    return False
        return bool(rows)

    def _resolve_undispatched(self, state, job, reason):
        """Administrative terminality, never a fabricated native observation."""
        if job.get('terminal_resolution', {}).get('kind') == 'cancelled_before_dispatch':
            return True
        # A manager stop also closes a pristine STANDALONE intent reservation:
        # no native run, observations, spend, progress or integration exists to
        # preserve, so keeping it reserved would wedge the single global slot
        # until the period ends with no worker able to advance it. Family
        # members (parent_job_id set) keep the shutdown protocol and its
        # accounting; deferred keeps its existing rule; expiry keeps intent
        # only for its own past-period case.
        if reason == 'job_budget_period_expired':
            closable = {'deferred', 'intent'}
        elif reason == 'stop_requested' and job.get('parent_job_id') is None:
            # Standalone pristine intent only; family shutdown keeps its
            # protocol (a root with descendants still records the native
            # outcome, members keep family accounting) and deferred keeps
            # its rule.
            children = self.store.db.execute(
                'SELECT 1 FROM runs WHERE parent_run_id=? LIMIT 1', (job['id'],)).fetchone()
            closable = {'deferred'} if children else {'deferred', 'intent'}
        else:
            closable = {'deferred'}
        if (self.service.recovery_required or job.get('delivery') not in closable
                or job.get('terminal') or job.get('native') is not None or job.get('observations')
                or job.get('charged_cost_usd') != 0 or job.get('observed_runtime_seconds') != 0
                or job.get('progress') or job.get('integration') != 'pending'):
            return False
        if reason == 'source_version_stale' and any(basis is None or self._basis(sid) is None
                for sid, basis in job.get('source_bases', {}).items()):
            return False
        if reason == 'stale_item_version' and (not job.get('item_bases', {}).get(job['item_id'])
                or self._basis(job['item_id']) is None):
            return False
        if self.store.db.execute('SELECT 1 FROM metadata WHERE key=? OR key=? OR key LIKE ? LIMIT 1',
                ('hermes:intent:'+job['id'], 'hermes:artifact:'+job['id'], 'hermes:observation:'+job['id']+':%')).fetchone():
            return False
        if self.store.db.execute('SELECT 1 FROM metadata WHERE key=? OR key=? OR key LIKE ? LIMIT 1',
                ('codex:job:'+job['id'], 'codex:process:'+job['id'], 'codex:event:'+job['id']+':%')).fetchone():
            return False
        orchestration = self.service._meta('execution:orchestration', {})
        run = orchestration.get('runs', {}).get(job['id'])
        if run is not None and (run.get('phase') != 'intent' or run.get('response') or run.get('last_status')):
            return False
        job.update(terminal=True, integration='discarded', integration_error=reason,
            terminal_resolution={'kind':'cancelled_before_dispatch', 'reason':reason,
                'at':datetime.now(timezone.utc).isoformat(), 'parent_job_id':job.get('parent_job_id'),
                'item_id':job['item_id'], 'return_status':'needs_replanning', 'native_effect':'not_dispatched'})
        return True

    def _descendant_path(self, item_id, root_id):
        """Actual parent_id ancestry only; project_id and other links confer none."""
        path, seen = [], {item_id}
        item = self.service.get_item(item_id)
        while item and item.get('parent_id'):
            parent_id = item['parent_id']
            if parent_id in seen:
                return None
            path.append(parent_id)
            if parent_id == root_id:
                return path
            seen.add(parent_id)
            item = self.service.get_item(parent_id)
        return None

    def _scope_path_valid(self, job, item_id):
        if item_id == job['item_id']:
            return True
        path = self._descendant_path(item_id, job['item_id'])
        return bool(path) and path == job.get('scope_ancestry', {}).get(item_id, path)

    def validate_target(self, job_id, actor, item_id, capability, *, require_descendants=False, require_source_snapshot=False, human_instruction_source=None):
        """Internal guard; require_descendants is a trusted root-assessment flag.

        The model never supplies these options. require_source_snapshot gates
        maintenance of existing dependencies against this admission. Default root local_work checks and
        closed admitted scope remain unchanged for other commands.
        """
        with self.store.lock:
            try:
                job = self.get_job(job_id)
            except ValueError as exc:
                return {"allowed": False, "reason": str(exc)}
            if not job or job["actor"] != actor:
                return {"allowed": False, "reason": "job_actor_mismatch"}
            valid = self.validate(job_id, job["capability"])
            if not valid["allowed"]:
                return valid
            if item_id not in job.get("item_bases", {job["item_id"]: None}):
                return {"allowed": False, "reason": "outside_job_scope"}
            if not self._scope_path_valid(job, item_id):
                return {"allowed": False, "reason": "outside_job_scope"}
            if (job.get("item_bases", {}).get(item_id) != self._basis(item_id)
                    and not self._compatible_parent_coordination(self._load(), job, item_id, job.get("item_bases", {}).get(item_id))):
                return {"allowed": False, "reason": "stale_item_version"}
            # A newly routed human reply does not increment target.version.
            # Require the complete current evidence set, without deciding
            # whether replies supersede or complement one another.
            targets = {job['item_id'], item_id}
            if require_descendants:
                targets.update(job.get('item_bases', {}))
            for target_id in targets:
                target = self.service.get_item(target_id)
                for evidence in self.service.routed_human_sources(target):
                    source_id = evidence['source_item_id']
                    if (source_id not in job.get('human_instruction_source_ids', [])
                            or job.get('source_bases', {}).get(source_id) != self._basis(source_id)):
                        return {'allowed': False, 'reason': 'routed_intent_set_stale'}
            if human_instruction_source is not None:
                if human_instruction_source not in job.get("human_instruction_source_ids", []):
                    return {"allowed": False, "reason": "source_basis_required"}
                if job.get("source_bases", {}).get(human_instruction_source) != self._basis(human_instruction_source):
                    return {"allowed": False, "reason": "source_version_stale"}
            if require_source_snapshot:
                # Trusted HTTP plan flag. Dependencies must already have been
                # observed by this admission; never extend or refresh its bases.
                sources = (self.service.get_item(item_id) or {}).get("source_versions", {})
                snapshots = {**job.get("source_bases", {}), **job.get("item_bases", {})}
                if not sources or any(sid not in snapshots for sid in sources):
                    return {"allowed": False, "reason": "source_basis_required"}
                if any(snapshots[sid] != self._basis(sid) for sid in sources):
                    return {"allowed": False, "reason": "source_version_stale"}
            if item_id == job["item_id"] and (capability == "local_work" or require_descendants):
                # Root work can close a whole commitment. Reject stale admitted
                # descendants before the domain mutation, not merely at final ack.
                if any((basis != self._basis(descendant_id)
                        and not self._compatible_parent_coordination(self._load(), job, descendant_id, basis))
                        or not self._scope_path_valid(job, descendant_id)
                       for descendant_id, basis in job.get("item_bases", {}).items()):
                    return {"allowed": False, "reason": "stale_descendant_version"}
            mandate_id = None if capability == "prepare_private" and self.service.actor_role(actor) == "principal" else job["mandate_id"]
            auth = self.service.authorize(actor, capability, item_id, mandate_id)
            if not auth["allowed"]:
                return auth
            if capability != job["capability"] and capability != "prepare_private":
                return {"allowed": False, "reason": "capability_mismatch"}
            return {**valid, "current_version": self.service.get_item(item_id)["version"]}

    def record_progress(self, job_id, domain_receipt, previous_version):
        """Trusted acknowledgement after guarded execute under the same Store lock.

        An actual actor-matching receipt advances only its own changed item; new
        derived items enter scope only through a verified creation receipt.
        No endpoint accepts this acknowledgement from the model.
        """
        with self.store.transaction():
            try:
                self._require_migrated()
                run = self._run_row(job_id)
                if run is None:
                    raise ValueError("job_not_found")
                cycle = self._cycle_row(run["cycle_id"])
                job = self._job_from_rows(cycle, run)
                try:
                    detail = json.loads(run["detail_json"]) if run["detail_json"] else {}
                except ValueError:
                    detail = {}
                row = self.store.db.execute("SELECT * FROM operations WHERE operation_id=?", (domain_receipt.get("operation_id"),)).fetchone()
                if not row or json.loads(row["receipt"]) != domain_receipt or row["actor"] != job["actor"] or domain_receipt.get("status") != "applied":
                    raise ValueError("progress_receipt_not_verified")
                operation_id = domain_receipt["operation_id"]
                if any(p["operation_id"] == operation_id for p in detail.get("progress", [])):
                    return {"status": "recorded", "duplicate": True, "job": copy.deepcopy(job)}
                item = domain_receipt.get("item")
                if item is None and domain_receipt.get("review"):
                    detail.setdefault("progress", []).append({"operation_id": operation_id, "review": True})
                else:
                    current = self.service.get_item(item["id"])
                    # Receipts keep full result arrays while stored documents
                    # keep stubs; compare the reference views, not raw shapes.
                    if GTDDomain._stub_view(current or {}) != GTDDomain._stub_view(item) or row["item_id"] != item["id"] or type(previous_version) is not int:
                        raise ValueError("progress_version_mismatch")
                    bases = detail.setdefault("item_bases", copy.deepcopy(job.get("item_bases", {})))
                    after = json.loads(row["after_patch"] or "{}")
                    if after.get("_created"):
                        parent = self.service.get_item(item.get("parent_id"))
                        if not parent or parent["id"] not in bases or self._basis(parent["id"]) != bases[parent["id"]] or parent["version"] != previous_version or item["version"] != 1:
                            raise ValueError("progress_scope_mismatch")
                    else:
                        if item["id"] not in bases or row["applied_version"] != previous_version + 1 or item["version"] != previous_version + 1:
                            raise ValueError("progress_version_mismatch")
                        # Reconstruct meaning before this operation; never adopt an
                        # unrelated human correction as if it were our progress.
                        before = json.loads(row["before_patch"] or "{}")
                        prior = copy.deepcopy(item)
                        for key, entry in before.items():
                            if entry["present"]:
                                prior[key] = entry["value"]
                            else:
                                prior.pop(key, None)
                        values = self._basis_values(prior)
                        if values != bases[item["id"]]["values"]:
                            raise ValueError("progress_meaning_mismatch")
                    # A verified human pause invalidates this reservation. Keep
                    # its admission bases intact while acknowledging the receipt.
                    if (after.get("human_instruction", {}).get("value", {}).get("instruction") == "pause"
                            and after.get("status", {}).get("value") == "paused"):
                        detail.setdefault("progress", []).append({"operation_id": operation_id, "item_id": item["id"],
                            "previous_version": previous_version, "version": item["version"]})
                        self.store.db.execute("UPDATE runs SET detail_json=? WHERE id=?", (_json(detail), job_id))
                        run2 = self._run_row(job_id)
                        cycle2 = self._cycle_row(run2["cycle_id"])
                        return {"status": "recorded", "job": self._job_from_rows(cycle2, run2)}
                    bases[item["id"]] = self._basis(item["id"])
                    if after.get("_created"):
                        detail.setdefault("scope_ancestry", {})[item["id"]] = self._descendant_path(item["id"], job["item_id"])
                    if item["id"] == job["item_id"]:
                        detail["expected_version"] = item["version"]
                        detail["source_versions"] = copy.deepcopy(item.get("source_versions", {}))
                    detail.setdefault("progress", []).append({"operation_id": operation_id, "item_id": item["id"], "previous_version": previous_version, "version": item["version"]})
                self.store.db.execute("UPDATE runs SET detail_json=? WHERE id=?", (_json(detail), job_id))
                run2 = self._run_row(job_id)
                cycle2 = self._cycle_row(run2["cycle_id"])
                return {"status": "recorded", "job": self._job_from_rows(cycle2, run2)}
            except (ValueError, KeyError, TypeError) as error:
                return {"status": "rejected", "error": str(error)}

    def expire_undispatched(self, job_id):
        """Expire a never-dispatched reservation only with durable negative evidence."""
        with self.store.transaction():
            try:
                self._require_migrated()
            except ValueError as exc:
                return {'status': 'rejected', 'error': str(exc)}
            run = self._run_row(job_id)
            if run is None:
                return {'status': 'rejected', 'error': 'job_not_found'}
            cycle = self._cycle_row(run["cycle_id"])
            job = self._job_from_rows(cycle, run)
            if not self._daily() or job.get('budget_period_id') == self._period(self.config)['id']:
                return {'status': 'unchanged'}
            if not self._resolve_undispatched(self._load(), job, 'job_budget_period_expired'):
                return {'status': 'rejected', 'error': 'dispatch_absence_not_proven'}
            # Persist administrative terminality (bounded single-row).
            try:
                detail = json.loads(run["detail_json"]) if run["detail_json"] else {}
            except ValueError:
                detail = {}
            detail.update({k: job[k] for k in ("terminal_resolution", "integration_error") if k in job})
            self.store.db.execute(
                "UPDATE runs SET detail_json=?, state='expired', integration='discarded' WHERE id=?",
                (_json(detail), job_id))
            if cycle:
                self.store.db.execute("UPDATE work_cycles SET state='abandoned', closed_at=? WHERE id=?",
                    (self._clock().isoformat(), cycle["id"]))
            run2 = self._run_row(job_id)
            cycle2 = self._cycle_row(run2["cycle_id"])
            return {'status': 'discarded', 'job': self._job_from_rows(cycle2, run2)}

    def activate_deferred(self, job_id):
        """Trusted worker admits an already reserved intention to the global slot."""
        with self.store.transaction():
            try:
                self._require_migrated()
                run = self._run_row(job_id)
                if run is None:
                    return {'status': 'rejected', 'error': 'job_not_found'}
                cycle = self._cycle_row(run["cycle_id"])
                job = self._job_from_rows(cycle, run)
                if job.get('terminal_resolution', {}).get('kind') == 'cancelled_before_dispatch':
                    return {'status':'discarded', 'job': copy.deepcopy(job)}
                if job["delivery"] != "deferred":
                    return {"status": "unchanged"}
                state = self._load()
                self._vigent(state, job, job["capability"])
                if self._budget(state)["active"] >= self.config.get("max_active", 1):
                    raise ValueError("concurrency_exhausted")
                try:
                    detail = json.loads(run["detail_json"]) if run["detail_json"] else {}
                except ValueError:
                    detail = {}
                detail["delivery"] = "intent"
                self.store.db.execute("UPDATE runs SET detail_json=? WHERE id=?", (_json(detail), job_id))
                run2 = self._run_row(job_id)
                cycle2 = self._cycle_row(run2["cycle_id"])
                return {"status": "activated", "job": self._job_from_rows(cycle2, run2)}
            except (ValueError, KeyError) as error:
                reason = str(error)
                if reason in {'job_budget_period_expired', 'stop_requested', 'stale_item_version', 'source_version_stale',
                        'mandate_not_active', 'mandate_revoked', 'terminal_item', 'outside_mandate'}:
                    try:
                        run0 = self._run_row(job_id)
                        cycle0 = self._cycle_row(run0["cycle_id"]) if run0 else None
                        job0 = self._job_from_rows(cycle0, run0) if run0 else {"id": job_id}
                        if self._resolve_undispatched(self._load(), job0, reason):
                            try:
                                d0 = json.loads(run0["detail_json"]) if run0 and run0["detail_json"] else {}
                            except ValueError:
                                d0 = {}
                            d0.update({k: job0[k] for k in ("terminal_resolution", "integration_error") if k in job0})
                            self.store.db.execute(
                                "UPDATE runs SET detail_json=?, state='cancelled', integration='discarded' WHERE id=?",
                                (_json(d0), job_id))
                            run2 = self._run_row(job_id)
                            cycle2 = self._cycle_row(run2["cycle_id"]) if run2 else None
                            job2 = self._job_from_rows(cycle2, run2) if run2 else job0
                            return {'status':'discarded', 'job': copy.deepcopy(job2)}
                    except (ValueError, KeyError):
                        pass
                return {"status": "rejected", "error": str(error)}

    def own_terminal_progress(self, job_id):
        """Only a verified own terminal domain result permits polling without stop."""
        with self.store.lock:
            try:
                job = self.get_job(job_id)
            except ValueError:
                return None
            if not job or job['stop_requested'] or self._basis(job['item_id']) != job.get('item_bases', {}).get(job['item_id']):
                return None
            if any(self._basis(item_id) != basis or not self._scope_path_valid(job, item_id)
                   for item_id, basis in job.get('item_bases', {}).items()):
                return None
            state = self._load()
            if (not self._dependencies(state, job).issubset(job.get('source_bases', {}))
                    or any(basis is None or (self._basis(source_id) != basis
                        and not self._compatible_parent_coordination(state, job, source_id, basis))
                        for source_id, basis in job.get('source_bases', {}).items())):
                return None
            item = self.service.get_item(job['item_id'])
            if item.get('status') not in {'done', 'withdrawn'}:
                return None
            for progress in reversed(job.get('progress', [])):
                if progress.get('item_id') != item['id'] or progress.get('version') != item['version']:
                    continue
                row = self.store.db.execute('SELECT actor,receipt,after_patch FROM operations WHERE operation_id=?', (progress['operation_id'],)).fetchone()
                if not row or row['actor'] != job['actor']:
                    return None
                receipt, after = json.loads(row['receipt']), json.loads(row['after_patch'] or '{}')
                if receipt.get('status') == 'applied' and GTDDomain._stub_view(receipt.get('item') or {}) == GTDDomain._stub_view(item) and (
                        'assessments' in after or ('clarification' in after and (item.get('clarification', {}).get('destination') == 'discard'
                        or (item.get('clarification', {}).get('destination') == 'existing'
                            and item.get('clarification', {}).get('resolution') == 'routed')))):
                    return receipt
            return None

    def discard_obsolete_terminal(self, job_id):
        """Trusted, idempotent resolution; prove obsolete bases, never accept a caller reason.

        Preserve authenticated progress and native/accounting evidence. Recovery and
        missing evidence are not proof of obsolescence and remain retryable.
        """
        with self.store.transaction():
            try:
                self._require_migrated()
            except ValueError as exc:
                return {'status': 'rejected', 'error': str(exc)}
            run = self._run_row(job_id)
            if run is None:
                return {'status': 'rejected', 'error': 'job_not_found'}
            cycle = self._cycle_row(run["cycle_id"])
            job = self._job_from_rows(cycle, run)
            try:
                detail = json.loads(run["detail_json"]) if run["detail_json"] else {}
            except ValueError:
                detail = {}
            if run["integration"] == "discarded" or detail.get("integration") == "discarded":
                return {'status': 'discarded', 'job': copy.deepcopy(job)}
            if self.service.recovery_required:
                return {'status': 'rejected', 'error': 'recovery_required'}
            if run["state"] != "completed":
                # Compat: legacy terminal bool + last native completed.
                if not job.get('terminal') or not job.get('observations') \
                        or job['observations'][-1]['native_status'] != 'completed':
                    return {'status': 'rejected', 'error': 'terminal_success_required'}
            else:
                last_row = self.store.db.execute(
                    "SELECT receipt_json FROM run_observations WHERE run_id=? ORDER BY seq DESC LIMIT 1",
                    (job_id,)).fetchone()
                last = json.loads(last_row["receipt_json"]) if last_row else {}
                if last.get("native_status") != "completed":
                    return {'status': 'rejected', 'error': 'terminal_success_required'}
            state = self._load()
            if run["integration"] not in {'pending'} and detail.get("integration") not in {'pending', 'accepted_pending_integration', None}:
                # Already resolved (integrated/discarded) beyond pending.
                if run["integration"] != "pending":
                    return {'status': 'rejected', 'error': 'integration_already_resolved'}
            reason = None
            for item_id, basis in job.get('item_bases', {}).items():
                if basis is not None and ((self._basis(item_id) != basis
                        and not self._compatible_parent_coordination(state, job, item_id, basis))
                        or not self._scope_path_valid(job, item_id)):
                    reason = 'stale_item_version' if item_id == job['item_id'] else 'stale_descendant_version'
                    break
            if reason is None and any(basis is not None and self._basis(source_id) != basis
                    and not self._compatible_parent_coordination(state, job, source_id, basis)
                    for source_id, basis in job.get('source_bases', {}).items()):
                reason = 'source_version_stale'
            if reason is None:
                return {'status': 'rejected', 'error': 'obsolescence_not_verified'}
            detail["integration"] = "discarded"
            detail["integration_error"] = reason
            self.store.db.execute(
                "UPDATE runs SET integration='discarded', detail_json=? WHERE id=?", (_json(detail), job_id))
            if cycle:
                self.store.db.execute("UPDATE work_cycles SET state='abandoned', closed_at=? WHERE id=?",
                    (self._clock().isoformat(), cycle["id"]))
            run2 = self._run_row(job_id)
            cycle2 = self._cycle_row(run2["cycle_id"])
            return {'status': 'discarded', 'job': self._job_from_rows(cycle2, run2)}

    def acknowledge_progress(self, job_id):
        """Trusted terminal acknowledgement of authenticated domain operations.

        Final model text is not domain evidence. This method never writes an item,
        material or assessment, and never refreshes a basis from unrelated edits.
        """
        with self.store.transaction():
            try:
                self._require_migrated()
                run = self._run_row(job_id)
                if run is None:
                    raise ValueError('job_not_found')
                cycle = self._cycle_row(run["cycle_id"])
                job = self._job_from_rows(cycle, run)
                state = self._load()
                self._vigent(state, job, job['capability'], integration=True)
                if run["state"] != "completed":
                    if not job.get('terminal'):
                        raise ValueError('terminal_success_required')
                    last = job.get('observations', [{}])[-1] if job.get('observations') else {}
                    if last.get('native_status') != 'completed':
                        raise ValueError('terminal_success_required')
                else:
                    last_row = self.store.db.execute(
                        "SELECT receipt_json FROM run_observations WHERE run_id=? ORDER BY seq DESC LIMIT 1",
                        (job_id,)).fetchone()
                    last = json.loads(last_row["receipt_json"]) if last_row else {}
                    if last.get("native_status") != "completed":
                        raise ValueError('terminal_success_required')
                if self.service.actor_role(job['actor']) != 'principal':
                    raise ValueError('principal_required')
                for item_id, basis in job.get('item_bases', {}).items():
                    if basis != self._basis(item_id) or not self._scope_path_valid(job, item_id):
                        raise ValueError('stale_item_version')
                try:
                    detail = json.loads(run["detail_json"]) if run["detail_json"] else {}
                except ValueError:
                    detail = {}
                operations = []
                for progress in detail.get('progress', []):
                    row = self.store.db.execute('SELECT * FROM operations WHERE operation_id=?', (progress['operation_id'],)).fetchone()
                    receipt = json.loads(row['receipt']) if row else {}
                    if not row or row['actor'] != job['actor'] or receipt.get('status') != 'applied':
                        raise ValueError('progress_receipt_not_verified')
                    if progress.get('review'):
                        if not receipt.get('review'):
                            raise ValueError('progress_receipt_not_verified')
                    elif (row['item_id'] != progress.get('item_id')
                            or receipt.get('item', {}).get('version') != progress.get('version')
                            or row['applied_version'] != progress.get('version')
                            or progress.get('item_id') not in job.get('item_bases', {})):
                        raise ValueError('progress_receipt_not_verified')
                    operations.append(progress['operation_id'])
                # Legacy compat status (integrated / no_domain_progress);
                # authoritative column becomes integrated in both cases.
                compat = 'integrated' if operations else 'no_domain_progress'
                detail['domain_operation_ids'] = operations
                if operations:
                    detail['domain_operation_id'] = operations[-1]
                detail['validated_version'] = self.service.get_item(job['item_id'])['version']
                detail['integration'] = compat
                self.store.db.execute(
                    "UPDATE runs SET integration='integrated', detail_json=? WHERE id=?",
                    (_json(detail), job_id))
                if cycle and compat == 'integrated':
                    self.store.db.execute("UPDATE work_cycles SET state='resolved', closed_at=? WHERE id=?",
                        (self._clock().isoformat(), cycle["id"]))
                run2 = self._run_row(job_id)
                cycle2 = self._cycle_row(run2["cycle_id"])
                job2 = self._job_from_rows(cycle2, run2)
                return {'status': compat, 'job': copy.deepcopy(job2)}
            except (ValueError, KeyError, TypeError) as error:
                return {'status': 'rejected', 'error': str(error)}

    def integrate_terminal_progress(self, job_id):
        """Acknowledge an already applied terminal result; no further domain effect."""
        with self.store.transaction():
            try:
                self._require_migrated()
            except ValueError as exc:
                return {'status': 'rejected', 'error': str(exc)}
            run = self._run_row(job_id)
            if run is None:
                return {'status': 'rejected', 'error': 'own_terminal_result_required'}
            cycle = self._cycle_row(run["cycle_id"])
            job = self._job_from_rows(cycle, run)
            receipt = self.own_terminal_progress(job_id)
            if not job.get('terminal') or not receipt:
                return {'status': 'rejected', 'error': 'own_terminal_result_required'}
            try:
                detail = json.loads(run["detail_json"]) if run["detail_json"] else {}
            except ValueError:
                detail = {}
            detail['integration'] = 'integrated'
            detail['domain_operation_id'] = receipt['operation_id']
            detail['validated_version'] = receipt['item']['version']
            self.store.db.execute(
                "UPDATE runs SET integration='integrated', detail_json=? WHERE id=?", (_json(detail), job_id))
            if cycle:
                self.store.db.execute("UPDATE work_cycles SET state='resolved', closed_at=? WHERE id=?",
                    (self._clock().isoformat(), cycle["id"]))
            run2 = self._run_row(job_id)
            cycle2 = self._cycle_row(run2["cycle_id"])
            return {'status': 'integrated', 'job': self._job_from_rows(cycle2, run2)}

    def migrate_legacy_i1(self):
        """I1 cut: move legacy execution:state jobs/operations to tables/keys.

        Preserves IDs, native identities, versions, authorship, idempotent
        receipts, corrections, permissions, pauses, budget and pending effects.
        Historic times unknown stay NULL with explicit provenance; migrated
        cycles are closed (resolved/abandoned, never executable) so missing
        admission originals cannot authorize new work. Legacy full blobs are
        frozen as execution:state:legacy:v1 / execution:orchestration:legacy:v1
        for history/rollback; active blobs become small. Single authority after
        the cut: tables + active small blobs, no dual write.
        Must run with processes stopped, in one transaction. Returns counts.
        """
        with self.store.transaction():
            legacy_row = self.store.db.execute(
                "SELECT value FROM metadata WHERE key='execution:state'").fetchone()
            if not legacy_row:
                return {"migrated_cycles": 0, "migrated_runs": 0, "migrated_observations": 0,
                        "migrated_control_ops": 0, "note": "no_legacy_state"}
            legacy = json.loads(legacy_row[0])
            legacy_jobs = legacy.get("jobs", {}) or {}
            if not legacy_jobs and self._tables_have_runs():
                return {"migrated_cycles": 0, "migrated_runs": 0, "migrated_observations": 0,
                        "migrated_control_ops": 0, "note": "already_migrated"}
            if not legacy_jobs:
                return {"migrated_cycles": 0, "migrated_runs": 0, "migrated_observations": 0,
                        "migrated_control_ops": 0, "note": "nothing_to_migrate"}
            # Freeze full legacy blobs before mutating (history/rollback).
            self.store.db.execute("INSERT OR REPLACE INTO metadata VALUES(?,?)",
                (self.LEGACY_STATE_BACKUP, legacy_row[0]))
            orch_row = self.store.db.execute(
                "SELECT value FROM metadata WHERE key='execution:orchestration'").fetchone()
            if orch_row:
                self.store.db.execute("INSERT OR REPLACE INTO metadata VALUES(?,?)",
                    ("execution:orchestration:legacy:v1", orch_row[0]))
            # Control idempotency map -> per-key rows (bounded future reads).
            legacy_ops = legacy.get("operations", {}) or {}
            for op_id, entry in legacy_ops.items():
                self.store.db.execute("INSERT OR REPLACE INTO metadata VALUES(?,?)",
                    (self._control_op_key(op_id), _json(entry)))
            # Jobs -> cycles/runs/observations. Deterministic cycle ids preserve
            # provenance without inventing chronology (UUID order is not time).
            migrated_cycles = migrated_runs = migrated_obs = 0
            for job_id in sorted(legacy_jobs):
                job = legacy_jobs[job_id]
                cycle_id = "cycle:" + job_id
                # Skip if already migrated (idempotent re-run).
                if self.store.db.execute("SELECT 1 FROM runs WHERE id=?", (job_id,)).fetchone():
                    continue
                # Cycle state: closed history only (never executable).
                integration = job.get("integration", "pending")
                if integration in ("integrated", "no_domain_progress"):
                    cycle_state = "resolved"
                elif integration == "discarded":
                    cycle_state = "abandoned"
                else:
                    # Active legacy jobs should not exist in the base (all 32
                    # terminal). Preserve safely as recovery_required, never
                    # executable by default, for explicit reconciliation.
                    cycle_state = "recovery_required"
                trigger_key = "migrated:" + job_id
                try:
                    input_fp = hashlib.sha256(_json([
                        job.get("item_id"), job.get("item_bases", {}),
                        job.get("source_bases", {}), job.get("purpose")]).encode()).hexdigest()
                except (ValueError, TypeError):
                    input_fp = hashlib.sha256(job_id.encode()).hexdigest()
                authority = {"actor": job.get("actor"), "requested_by": job.get("requested_by", job.get("actor")),
                             "capability": job.get("capability"), "mandate_id": job.get("mandate_id"),
                             "bot_id": job.get("bot_id"), "migrated_from": "execution:state:v1",
                             "trigger_key": trigger_key}
                allowance = float(job.get("max_runtime_seconds") or 240)
                if not (allowance > 0):
                    allowance = 240.0
                attempts = job.get("max_retries", 0)
                attempts = int(attempts) + 1 if isinstance(attempts, int) and attempts >= 0 else 1
                budget_period = job.get("budget_period_id") or "fixed:unscoped"
                detail_cycle = {"legacy_job_id": job_id, "origin": "migrated",
                                "scope": job.get("scope"), "orchestrated": bool(job.get("orchestrated")),
                                "root_job_id": job.get("root_job_id", job_id),
                                "parent_job_id": job.get("parent_job_id"),
                                "provenance": "migrated from execution:state v1; times unknown (NULL), "
                                "original admission bases unknown (current bases preserved), not executable"}
                self.store.db.execute(
                    "INSERT INTO work_cycles(id,item_id,trigger_key,input_fingerprint,purpose,"
                    "authority_json,state,allowance_seconds,attempts_limit,wake_json,"
                    "predecessor_id,parent_cycle_id,budget_period_id,created_at,closed_at,detail_json) "
                    "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (cycle_id, job.get("item_id"), trigger_key, input_fp, job.get("purpose", "migrated"),
                     _json(authority), cycle_state, allowance, attempts, None,
                     None, None, budget_period, None, None, _json(detail_cycle)))
                migrated_cycles += 1
                # Run state mapping (terminal history).
                last_native = (job.get("observations") or [{}])[-1].get("native_status") if job.get("observations") else None
                if job.get("terminal"):
                    if last_native == "completed":
                        run_state = "completed"
                    elif last_native == "failed":
                        run_state = "failed"
                    elif last_native == "cancelled":
                        run_state = "cancelled"
                    else:
                        run_state = "completed" if integration in ("integrated", "no_domain_progress") else "cancelled"
                else:
                    run_state = "recovery_required" if False else "uncertain"
                    # Active legacy: conserve slot until reconciled.
                    run_state = "uncertain"
                if integration == "no_domain_progress":
                    run_integration = "integrated"
                elif integration == "accepted_pending_integration":
                    run_integration = "pending"
                elif integration in ("pending", "integrated", "discarded"):
                    run_integration = integration
                else:
                    run_integration = "pending"
                native = job.get("native") or {}
                admission = {"requested_by": job.get("requested_by", job.get("actor")),
                             "capability": job.get("capability"), "mandate_id": job.get("mandate_id"),
                             "bot_id": job.get("bot_id"), "expected_version": job.get("expected_version"),
                             "max_cost_usd": job.get("max_cost_usd", 0),
                             "max_runtime_seconds": job.get("max_runtime_seconds", allowance),
                             "max_retries": job.get("max_retries", 0),
                             "max_descendants": job.get("max_descendants", 0),
                             "item_bases": job.get("item_bases", {}), "source_bases": job.get("source_bases", {}),
                             "source_versions": job.get("source_versions", {}), "route": job.get("route"),
                             "scope": job.get("scope"), "purpose": job.get("purpose"),
                             "migrated": True,
                             "provenance": "admission originals unknown; current bases preserved; not executable"}
                if job.get("human_instruction_source_ids") is not None:
                    admission["human_instruction_source_ids"] = copy.deepcopy(job["human_instruction_source_ids"])
                # Detail preserves the full legacy job minus observations (which
                # live in run_observations) for exact compat reconstruction.
                detail = {k: copy.deepcopy(v) for k, v in job.items() if k != "observations"}
                # Ensure required detail keys for _job_from_rows.
                detail.setdefault("root_job_id", job.get("root_job_id", job_id))
                detail.setdefault("delivery", job.get("delivery", "acknowledged"))
                detail.setdefault("charged_cost_usd", job.get("charged_cost_usd", 0))
                self.store.db.execute(
                    "INSERT INTO runs(id,cycle_id,item_id,actor,parent_run_id,state,integration,"
                    "admission_json,detail_json,native_provider,native_host,native_profile,native_id,"
                    "budget_period_id,reserved_seconds,observed_seconds,cost_usd,"
                    "admitted_at,started_at,ended_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (job_id, cycle_id, job.get("item_id"), job.get("actor"), job.get("parent_job_id"),
                     run_state, run_integration, _json(admission), _json(detail),
                     native.get("provider"), native.get("host"), native.get("profile"), native.get("id"),
                     budget_period, float(job.get("max_runtime_seconds") or allowance),
                     float(job.get("observed_runtime_seconds") or 0), None,
                     None, None, None))
                migrated_runs += 1
                for seq, obs in enumerate(job.get("observations") or [], start=1):
                    self.store.db.execute(
                        "INSERT INTO run_observations(run_id,seq,observed_at,native_state,"
                        "runtime_seconds,cost_usd,receipt_json) VALUES(?,?,?,?,?,?,?)",
                        (job_id, seq, None, obs.get("native_status", "completed"),
                         float(obs.get("runtime_seconds") or 0), obs.get("cost_usd"), _json(obs)))
                    migrated_obs += 1
            # Shrink active blobs to small (no jobs, no ops map). Bots/config/
            # periods/transitions/displacements stay (KB, not MB).
            slim = {k: v for k, v in legacy.items() if k not in ("jobs", "operations")}
            slim.setdefault("operations", {})
            slim.setdefault("bots", {})
            self.store.db.execute("INSERT OR REPLACE INTO metadata VALUES(?,?)",
                (self.KEY, _json(slim)))
            # Orchestration active -> small (historic runs/admissions archived in
            # legacy key above). Preserve review_at for periodic scheduling.
            if orch_row:
                try:
                    orch = json.loads(orch_row[0])
                except ValueError:
                    orch = {}
                active_orch = {"runs": {}, "attempts": {}, "admissions": {}, "continuations": {},
                               "continuation_sources": {}, "executor_returns": {},
                               "review_at": orch.get("review_at", 0)}
                self.store.db.execute("INSERT OR REPLACE INTO metadata VALUES(?,?)",
                    ("execution:orchestration", _json(active_orch)))
            return {"migrated_cycles": migrated_cycles, "migrated_runs": migrated_runs,
                    "migrated_observations": migrated_obs, "migrated_control_ops": len(legacy_ops)}
