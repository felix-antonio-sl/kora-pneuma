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
import uuid


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

    def _load(self):
        row = self.store.db.execute("SELECT value FROM metadata WHERE key=?", (self.KEY,)).fetchone()
        return json.loads(row[0]) if row else {"jobs": {}, "bots": {}, "operations": {}, "config": None}

    def _save(self, state):
        self.store.db.execute("INSERT OR REPLACE INTO metadata VALUES(?,?)", (self.KEY, _json(state)))

    def _operation(self, actor, operation_id, action, payload, fn):
        if not isinstance(operation_id, str) or not operation_id:
            return {"status": "rejected", "error": "operation_id_required"}
        try:
            digest = hashlib.sha256(_json([actor, action, payload]).encode()).hexdigest()
        except (ValueError, TypeError):
            return {"status": "rejected", "error": "invalid_json_payload"}
        with self.store.transaction():
            state = self._load()
            old = state["operations"].get(operation_id)
            if old:
                if old["fingerprint"] != digest:
                    return {"status": "rejected", "error": "idempotency_conflict", "operation_id": operation_id}
                return dict(old["receipt"], duplicate=True)
            try:
                revised = copy.deepcopy(state)
                receipt = fn(revised)
                state = revised
            except (ValueError, KeyError, TypeError) as error:
                receipt = {"status": "rejected", "error": str(error)}
            receipt["operation_id"] = operation_id
            state["operations"][operation_id] = {"fingerprint": digest, "receipt": receipt}
            self._save(state)
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
            old = state['config']
            if not old or self.policy_hash(old) != expected_hash:
                raise ValueError('budget_policy_hash_mismatch')
            if not self._daily() or config == old:
                raise ValueError('unsupported_budget_transition')
            if any(not job['terminal'] for job in state['jobs'].values()):
                raise ValueError('budget_transition_requires_terminal_jobs')
            historical = self._period(old)
            if self._daily(old) and any(job.get('budget_period_id') == historical['id'] for job in state['jobs'].values()):
                raise ValueError('budget_transition_requires_unused_day')
            state.setdefault('periods', {})[historical['id']] = historical
            for job in state['jobs'].values():
                job.setdefault('budget_period_id', historical['id'])
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
        config = state['config'] or self.config
        daily = self._daily(config)
        period = self._period(config) if daily else None
        cost = runtime = 0
        for job in state["jobs"].values():
            if job.get("parent_job_id") or (daily and job.get("budget_period_id") != period["id"]):
                continue
            family = [j for j in state["jobs"].values() if j["root_job_id"] == job["id"]]
            if all(j["terminal"] for j in family):
                cost += sum(j["charged_cost_usd"] for j in family)
                runtime += sum(j["observed_runtime_seconds"] for j in family)
            else:
                cost += max(job["max_cost_usd"], sum(j["charged_cost_usd"] for j in family))
                runtime += max(job["max_runtime_seconds"], sum(j["observed_runtime_seconds"] for j in family))
        config = state["config"] or self.config
        return {"committed_cost_usd": cost, "committed_runtime_seconds": runtime,
                "remaining_cost_usd": None if daily else max(0, config.get("max_cost_usd", 0) - config.get("recovery_cost_usd", 0) - cost),
                "cost_control": not daily, "budget_mode": config.get("budget_mode", "fixed"),
                "policy_hash": self.policy_hash(config),
                "period_id": period["id"] if daily else None,
                "returns_at": period["end"] if daily else None,
                "runtime_enforcement": "cooperative",
                "remaining_runtime_seconds": max(0, config.get("max_runtime_seconds", 0) - config.get("recovery_runtime_seconds", 0) - runtime),
                "active": sum(not j["terminal"] and j["delivery"] != "deferred" for j in state["jobs"].values()),
                "recovery_cost_usd": config.get("recovery_cost_usd", 0),
                "recovery_runtime_seconds": config.get("recovery_runtime_seconds", 0)}

    def budget(self):
        with self.store.lock:
            return self._budget(self._load())

    def _dependencies(self, state, job):
        """Declared dependency closure is a validity basis, never execution scope."""
        pending = [job["item_id"], *job.get("source_versions", {}), *job.get("human_instruction_source_ids", [])]
        parent_job = state["jobs"].get(job.get("parent_job_id"), {})
        if parent_job.get("item_id"):
            pending.append(parent_job["item_id"])
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
        if ("source_versions" in job or job["id"] in state["jobs"]) and not self._dependencies(state, job).issubset(job.get("source_bases", {})):
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
                               lambda state: self._reserve(state, actor, request))

    def _reserve(self, state, actor, request):
        self._manager(actor)
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
        job.update(id=uuid.uuid4().hex, actor=actor, delivery="intent", stop_requested=False,
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
        execution_bot = state["bots"].get(job["bot_id"], {})
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
        if any(((not self._daily() and j["charged_cost_usd"] > j["max_cost_usd"]) or j["observed_runtime_seconds"] > j["max_runtime_seconds"])
               and (not self._daily() or j.get("budget_period_id") == job["budget_period_id"]) for j in state["jobs"].values()):
            raise ValueError("observed_budget_overrun")
        if budget["active"] >= config["max_active"]:
            if request.get("defer_when_busy") is True and job["parent_job_id"]:
                job["delivery"] = "deferred"
            else:
                raise ValueError("concurrency_exhausted")
        if job["parent_job_id"]:
            parent = state["jobs"][job["parent_job_id"]]
            self._vigent(state, parent, parent["capability"])
            root = state["jobs"][parent["root_job_id"]]
            if root["terminal"]:
                raise ValueError("terminal_root")
            children = [j for j in state["jobs"].values() if j["root_job_id"] == root["id"] and j["id"] != root["id"]]
            descendants = {parent["id"]}
            while True:
                expanded = descendants | {j["id"] for j in children if j.get("parent_job_id") in descendants}
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
        if any(not j["terminal"] and j["item_id"] == job["item_id"] and j["purpose"] == job["purpose"] and not job["parent_job_id"] for j in state["jobs"].values()):
            raise ValueError("purpose_already_active")
        state["config"] = config
        state["jobs"][job["id"]] = job
        return {"status": "reserved", "job_id": job["id"], "job": job}

    def get_job(self, job_id):
        with self.store.lock:
            return self._load()["jobs"].get(job_id)

    def job_history(self, actor, caller_job_id, item_id=None):
        """Read bounded execution evidence; historical jobs grant no authority."""
        with self.store.lock:
            caller = self.get_job(caller_job_id)
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
            fields = ('id', 'item_id', 'actor', 'requested_by', 'parent_job_id', 'root_job_id',
                'capability', 'mandate_id', 'bot_id', 'purpose', 'expected_version',
                'max_cost_usd', 'max_runtime_seconds', 'max_retries', 'max_descendants',
                'delivery', 'stop_requested', 'terminal', 'native', 'integration', 'integration_error',
                'terminal_resolution', 'domain_operation_id', 'charged_cost_usd', 'observed_runtime_seconds')
            result = []
            for job in self._load()['jobs'].values():
                if job['item_id'] not in visible:
                    continue
                record = {key: copy.deepcopy(job[key]) for key in fields if key in job}
                record['last_observation'] = copy.deepcopy(job['observations'][-1]) if job.get('observations') else None
                result.append(record)
            return result

    def pending(self):
        with self.store.lock:
            return [j for j in self._load()["jobs"].values() if not j["terminal"] or j["integration"] == "pending"]

    def validate(self, job_id, capability):
        with self.store.lock:
            state = self._load()
            try:
                self._vigent(state, state["jobs"][job_id], capability)
                job = state["jobs"][job_id]
                if job["delivery"] == "deferred":
                    raise ValueError("dispatch_deferred")
                children = [j for j in state["jobs"].values() if j["root_job_id"] == job_id and j["id"] != job_id]
                limits = {key: job[key] - sum(j[key] for j in children) for key in ("max_cost_usd", "max_runtime_seconds")}
                limits.update(cost_control=not self._daily(), max_retries=job["max_retries"], max_descendants=job["max_descendants"] - len(children))
                return {"allowed": True, "reason": None, "limits": limits,
                        "current_version": self.service.get_item(job["item_id"])["version"]}
            except (ValueError, KeyError) as error:
                return {"allowed": False, "reason": str(error)}

    def _native(self, state, job, native):
        if not isinstance(native, dict) or not all(isinstance(native.get(k), str) and native[k] for k in ("provider", "host", "profile", "id")):
            raise ValueError("native_identity_required")
        route = job["route"]
        if native["host"] != route["host"] or native["profile"] != route["profile"]:
            raise ValueError("native_route_mismatch")
        if job["native"] and job["native"] != native:
            raise ValueError("native_identity_changed")
        if any(j["id"] != job["id"] and j["native"] == native for j in state["jobs"].values()):
            raise ValueError("native_identity_already_accounted")

    def record_dispatch(self, job_id, native):
        with self.store.transaction():
            state = self._load()
            try:
                job = state["jobs"][job_id]
                self._native(state, job, native)
                # Recording an already dispatched effect remains possible after revocation.
                job["native"] = copy.deepcopy(native)
                job["delivery"] = "acknowledged"
                self._save(state)
                return {"status": "recorded", "job": copy.deepcopy(job)}
            except (ValueError, KeyError) as error:
                return {"status": "rejected", "error": str(error)}

    def _observe(self, state, job_id, observation):
        job = state["jobs"][job_id]
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
        if job["terminal"]:
            if observation == job["observations"][-1]:
                return {"status": "recorded", "duplicate": True, "job": job}
            raise ValueError("terminal_observation_conflict")
        if cost is not None and cost < job["charged_cost_usd"]:
            raise ValueError("cost_regressed")
        if observation["runtime_seconds"] < job["observed_runtime_seconds"]:
            raise ValueError("runtime_regressed")
        job["native"] = copy.deepcopy(native)
        job["delivery"] = "uncertain" if status in {"uncertain", "not_found"} else "acknowledged"
        job["terminal"] = terminal
        job["observed_runtime_seconds"] = observation["runtime_seconds"]
        job["observations"].append(copy.deepcopy(observation))
        if terminal:
            children = [j for j in state["jobs"].values() if j["root_job_id"] == job["id"] and j["id"] != job["id"]]
            # Children draw allocations from the root, not extra reservations.
            own_max = max(0, job["max_cost_usd"] - sum(j["max_cost_usd"] for j in children))
            job["charged_cost_usd"] = max(own_max, job["charged_cost_usd"]) if cost is None else cost
            if status != "completed":
                job["integration"] = "discarded"
        elif cost is not None:
            job["charged_cost_usd"] = max(job["charged_cost_usd"], cost)
        return {"status": "recorded", "job": job}

    def observe(self, job_id, observation):
        """Record trusted native identity/status/evidence and cumulative consumption.

        Consumption is exclusive of separately registered descendants; unknown
        cost is None. Network errors/not_found are nonterminal. Provider limits
        must be enforced by the adapter using validate's shared allocation.
        """
        with self.store.transaction():
            state = self._load()
            try:
                result = self._observe(state, job_id, observation)
                self._save(state)
                return copy.deepcopy(result)
            except (ValueError, KeyError, TypeError) as error:
                return {"status": "rejected", "error": str(error)}

    def request_stop(self, actor, operation_id, job_id):
        def apply(state):
            self._manager(actor)
            job = state["jobs"][job_id]
            affected = {job_id}
            while True:
                expanded = affected | {j["id"] for j in state["jobs"].values() if j.get("parent_job_id") in affected}
                if expanded == affected:
                    break
                affected = expanded
            # A trusted scheduler context, never a caller-supplied reason or
            # operation-id prefix, distinguishes yielding from a manager stop.
            technical = actor != self.service.owner_actor and job_id in self._technical_stops.get()
            if not technical:
                for record in state.get('attention_displacements', {}).values():
                    if affected.intersection(record['family']) or record.get('new_job_id') in affected:
                        record.update(status='cancelled', blocker='stop_requested',
                            cancel_version=self.service.get_item(record['item_id'])['version'])
                        resumed = record.get('new_job_id')
                        if resumed:
                            affected.update(j['id'] for j in state['jobs'].values() if j['root_job_id'] == resumed)
            for identity in affected:
                state["jobs"][identity]["stop_requested"] = True
                self._resolve_undispatched(state, state['jobs'][identity], 'stop_requested')
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
                config = self._configuration(state)
                records = state.setdefault('attention_displacements', {})
                if job_id in records:
                    return dict(status='recorded', displacement=copy.deepcopy(records[job_id]))
                beneficiary = self.service.get_item(beneficiary_id)
                deadline = self._attention_window(beneficiary)
                if deadline is None or deadline <= datetime.now(timezone.utc).timestamp():
                    raise ValueError('attention_window_unavailable')
                job = state['jobs'][job_id]
                if job['parent_job_id'] or job.get('attention_origin') or job['actor'] != actor:
                    raise ValueError('attention_root_required')
                family = [j for j in state['jobs'].values() if j['root_job_id'] == job_id]
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
            record = state['attention_displacements'][old_job_id]
            if record.get('new_job_id'):
                return dict(status='reserved', job_id=record['new_job_id'],
                            job=copy.deepcopy(state['jobs'][record['new_job_id']]), duplicate=True)
            if record['status'] == 'cancelled':
                return dict(status='rejected', error=record['blocker'])
            try:
                self._manager(actor)
                self._configuration(state)
                if (record['period'] != self.config or record['period'] != state['config']
                        or (self._daily() and record.get('budget_period_id') != self._period(self.config)['id'])):
                    raise ValueError('attention_budget_period_changed')
                if any(not state['jobs'][jid]['terminal'] for jid in record['family']):
                    raise ValueError('attention_family_not_stopped')
                if self.service.work_input_basis(record['item_id'], record['sources'], include_evidence=False) != record['input_basis']:
                    raise ValueError('attention_input_changed')
                old = state['jobs'][old_job_id]
                if actor != old['actor'] or state['bots'].get(old['bot_id'], {}).get('actor', actor) != old['actor']:
                    raise ValueError('attention_actor_changed')
                # Verified progress can advance the old job's bases; arbitrary
                # changes cannot. Keep both its live bases and external anchor.
                for jid in record['family']:
                    shadow = copy.deepcopy(state['jobs'][jid])
                    shadow.update(stop_requested=False, terminal=False)
                    self._vigent(state, shadow, shadow['capability'], integration=True)
                item = self.service.get_item(old['item_id'])
                if item['status'] != 'active' or self.service.work_resolution_current(item['id']):
                    raise ValueError('attention_work_resolved_or_inactive')
                request = {k: old[k] for k in ('item_id', 'mandate_id', 'capability', 'bot_id', 'purpose', 'scope',
                    'max_cost_usd', 'max_runtime_seconds', 'max_retries', 'max_descendants')}
                request['expected_version'] = item['version']
                receipt = self._reserve(state, actor, request)
                job = state['jobs'][receipt['job_id']]
                job['attention_origin'] = old_job_id
                # Existing deferred activation revalidates before dispatch and
                # can prove cancellation if a human stop arrives in this gap.
                job['delivery'] = 'deferred'
                record.update(status='resumed', blocker=None, new_job_id=job['id'])
                self._save(state)
                return dict(status='reserved', job_id=job['id'], job=copy.deepcopy(job))
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
            job = state["jobs"][job_id]
            self._vigent(state, job, job["capability"], integration=True)
            if not job["terminal"] or job["observations"][-1]["native_status"] != "completed":
                raise ValueError("terminal_success_required")
            if job["integration"] != "pending":
                raise ValueError("result_already_integrated")
            if result.get("criteria_met") is not True or not all(isinstance(result.get(k), str) and result[k].strip() for k in ("evidence_reference", "artifact_reference")):
                raise ValueError("result_evidence_required")
            job["result"] = copy.deepcopy(result)
            job["integration"] = "accepted_pending_integration"
            job["validated_version"] = self.service.get_item(job["item_id"])["version"]
            return {"status": "accepted", "job": job}
        return self._operation(actor, operation_id, "accept_result", [job_id, result], apply)

    def reconcile(self, actor, operation_id, observations):
        def apply(state):
            if self.service.actor_role(actor) != "owner":
                raise ValueError("owner_required")
            # Work on a copy: invalid batches never partly reconcile.
            revised = copy.deepcopy(state)
            for observation in observations:
                self._observe(revised, observation["job_id"], {k: v for k, v in observation.items() if k != "job_id"})
            if any(not j["terminal"] or j["delivery"] == "uncertain" for j in revised["jobs"].values()):
                raise ValueError("unresolved_execution")
            outbox = self.store.db.execute("SELECT value FROM metadata WHERE key LIKE 'telegram-outbox:%'").fetchall()
            if any(json.loads(row[0]).get("status") != "confirmed" for row in outbox):
                raise ValueError("unresolved_output")
            from .effects import ExternalEffects
            if ExternalEffects(self.service).pending():
                raise ValueError('unresolved_external_effects')
            state.update(revised)
            self.store.db.execute("INSERT OR REPLACE INTO metadata VALUES('recovery_required','false')")
            return {"status": "reconciled"}
        return self._operation(actor, operation_id, "reconcile", observations, apply)

    def record_integration(self, job_id, domain_receipt):
        """Trusted integration acknowledgement; verify the actual stored receipt.

        Domain execution happens separately with expected_version from acceptance.
        This method never calls execute and cannot make a stale result current.
        """
        with self.store.transaction():
            state = self._load()
            try:
                job = state["jobs"][job_id]
                if job["integration"] != "accepted_pending_integration":
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
                if item.get("version") != job["validated_version"] + 1 or not current or current["version"] != item["version"]:
                    raise ValueError("integration_version_mismatch")
                job["integration"] = "integrated"
                job["domain_operation_id"] = operation_id
                self._save(state)
                return {"status": "integrated", "job": copy.deepcopy(job)}
            except (ValueError, KeyError, TypeError) as error:
                return {"status": "rejected", "error": str(error)}

    _COMPATIBLE = frozenset({"notes", "coverage", "updated_at", "version"})

    def _basis_values(self, item):
        values = {k: v for k, v in item.items() if k not in self._COMPATIBLE and k != "materials"}
        human_materials = [m for m in item.get("materials", []) if m.get("author") == self.service.owner_actor]
        if human_materials:
            values["materials"] = human_materials
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
        parent = state['jobs'].get(job.get('parent_job_id'))
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
            if (not changed <= coordination or row['actor'] != parent['actor']
                    or not any(j['actor'] == row['actor'] and self._scope_path_valid(j, source_id)
                        and any(p['operation_id'] == row['operation_id'] for p in j.get('progress', []))
                        for j in ([parent] if own_item else state['jobs'].values()))):
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
        if (self.service.recovery_required or job.get('delivery') not in ({'deferred', 'intent'} if reason == 'job_budget_period_expired' else {'deferred'})
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
            job = self.get_job(job_id)
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
            state = self._load()
            try:
                job = state["jobs"][job_id]
                row = self.store.db.execute("SELECT * FROM operations WHERE operation_id=?", (domain_receipt.get("operation_id"),)).fetchone()
                if not row or json.loads(row["receipt"]) != domain_receipt or row["actor"] != job["actor"] or domain_receipt.get("status") != "applied":
                    raise ValueError("progress_receipt_not_verified")
                operation_id = domain_receipt["operation_id"]
                if any(p["operation_id"] == operation_id for p in job.get("progress", [])):
                    return {"status": "recorded", "duplicate": True, "job": copy.deepcopy(job)}
                item = domain_receipt.get("item")
                if item is None and domain_receipt.get("review"):
                    job.setdefault("progress", []).append({"operation_id": operation_id, "review": True})
                else:
                    current = self.service.get_item(item["id"])
                    if current != item or row["item_id"] != item["id"] or type(previous_version) is not int:
                        raise ValueError("progress_version_mismatch")
                    bases = job.setdefault("item_bases", {})
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
                        job.setdefault("progress", []).append({"operation_id": operation_id, "item_id": item["id"],
                            "previous_version": previous_version, "version": item["version"]})
                        self._save(state)
                        return {"status": "recorded", "job": copy.deepcopy(job)}
                    bases[item["id"]] = self._basis(item["id"])
                    if after.get("_created"):
                        job.setdefault("scope_ancestry", {})[item["id"]] = self._descendant_path(item["id"], job["item_id"])
                    if item["id"] == job["item_id"]:
                        job["expected_version"] = item["version"]
                        job["source_versions"] = copy.deepcopy(item.get("source_versions", {}))
                    job.setdefault("progress", []).append({"operation_id": operation_id, "item_id": item["id"], "previous_version": previous_version, "version": item["version"]})
                self._save(state)
                return {"status": "recorded", "job": copy.deepcopy(job)}
            except (ValueError, KeyError, TypeError) as error:
                return {"status": "rejected", "error": str(error)}

    def expire_undispatched(self, job_id):
        """Expire a never-dispatched reservation only with durable negative evidence."""
        with self.store.transaction():
            state = self._load()
            job = state['jobs'][job_id]
            if not self._daily() or job.get('budget_period_id') == self._period(self.config)['id']:
                return {'status': 'unchanged'}
            if not self._resolve_undispatched(state, job, 'job_budget_period_expired'):
                return {'status': 'rejected', 'error': 'dispatch_absence_not_proven'}
            self._save(state)
            return {'status': 'discarded', 'job': copy.deepcopy(job)}

    def activate_deferred(self, job_id):
        """Trusted worker admits an already reserved intention to the global slot."""
        with self.store.transaction():
            state = self._load()
            try:
                job = state["jobs"][job_id]
                if job.get('terminal_resolution', {}).get('kind') == 'cancelled_before_dispatch':
                    return {'status':'discarded', 'job':copy.deepcopy(job)}
                if job["delivery"] != "deferred":
                    return {"status": "unchanged"}
                self._vigent(state, job, job["capability"])
                if self._budget(state)["active"] >= self.config.get("max_active", 1):
                    raise ValueError("concurrency_exhausted")
                job["delivery"] = "intent"
                self._save(state)
                return {"status": "activated", "job": copy.deepcopy(job)}
            except (ValueError, KeyError) as error:
                reason = str(error)
                if reason in {'job_budget_period_expired', 'stop_requested', 'stale_item_version', 'source_version_stale',
                        'mandate_not_active', 'mandate_revoked', 'terminal_item', 'outside_mandate'}:
                    if self._resolve_undispatched(state, state['jobs'][job_id], reason):
                        self._save(state)
                        return {'status':'discarded', 'job':copy.deepcopy(state['jobs'][job_id])}
                return {"status": "rejected", "error": str(error)}

    def own_terminal_progress(self, job_id):
        """Only a verified own terminal domain result permits polling without stop."""
        with self.store.lock:
            job = self.get_job(job_id)
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
                if receipt.get('status') == 'applied' and receipt.get('item') == item and (
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
            state = self._load()
            job = state['jobs'].get(job_id)
            if not job:
                return {'status': 'rejected', 'error': 'job_not_found'}
            if job['integration'] == 'discarded':
                return {'status': 'discarded', 'job': copy.deepcopy(job)}
            if self.service.recovery_required:
                return {'status': 'rejected', 'error': 'recovery_required'}
            if (not job['terminal'] or not job.get('observations')
                    or job['observations'][-1]['native_status'] != 'completed'):
                return {'status': 'rejected', 'error': 'terminal_success_required'}
            if job['integration'] not in {'pending', 'accepted_pending_integration'}:
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
            job['integration'] = 'discarded'
            job['integration_error'] = reason
            self._save(state)
            return {'status': 'discarded', 'job': copy.deepcopy(job)}

    def acknowledge_progress(self, job_id):
        """Trusted terminal acknowledgement of authenticated domain operations.

        Final model text is not domain evidence. This method never writes an item,
        material or assessment, and never refreshes a basis from unrelated edits.
        """
        with self.store.transaction():
            state = self._load()
            try:
                job = state['jobs'][job_id]
                self._vigent(state, job, job['capability'], integration=True)
                if (not job['terminal'] or not job['observations']
                        or job['observations'][-1]['native_status'] != 'completed'):
                    raise ValueError('terminal_success_required')
                if self.service.actor_role(job['actor']) != 'principal':
                    raise ValueError('principal_required')
                for item_id, basis in job.get('item_bases', {}).items():
                    if basis != self._basis(item_id) or not self._scope_path_valid(job, item_id):
                        raise ValueError('stale_item_version')
                operations = []
                for progress in job.get('progress', []):
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
                job['integration'] = 'integrated' if operations else 'no_domain_progress'
                job['domain_operation_ids'] = operations
                if operations:
                    job['domain_operation_id'] = operations[-1]
                job['validated_version'] = self.service.get_item(job['item_id'])['version']
                self._save(state)
                return {'status': job['integration'], 'job': copy.deepcopy(job)}
            except (ValueError, KeyError, TypeError) as error:
                return {'status': 'rejected', 'error': str(error)}

    def integrate_terminal_progress(self, job_id):
        """Acknowledge an already applied terminal result; no further domain effect."""
        with self.store.transaction():
            state = self._load()
            job = state['jobs'].get(job_id)
            receipt = self.own_terminal_progress(job_id)
            if not job or not job['terminal'] or not receipt:
                return {'status': 'rejected', 'error': 'own_terminal_result_required'}
            job['integration'] = 'integrated'
            job['domain_operation_id'] = receipt['operation_id']
            job['validated_version'] = receipt['item']['version']
            self._save(state)
            return {'status': 'integrated', 'job': copy.deepcopy(job)}
