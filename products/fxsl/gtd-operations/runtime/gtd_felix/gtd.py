"""Local GTD semantics. All mutations run in the service command transaction."""
from datetime import datetime, timezone
import json
import hashlib
import os
import stat
import uuid

from .domain import encode, fingerprint, now, validate_date, validate_fields, KINDS


class GTDDomain:
    SEMANTIC_ACTIONS = frozenset({"clarify", "derive", "grant_mandate", "revoke_mandate",
        "plan", "put_material", "assess_result", "review", "request_review", "set_attention", "apply_human_instruction"})
    MEANING = frozenset({"title", "kind", "purpose", "outcome", "completion_criteria",
        "commitment", "executor", "project_id", "responsibility_id", "depends_on"})

    def _meta(self, key, default=None):
        row = self.store.db.execute("SELECT value FROM metadata WHERE key=?", (key,)).fetchone()
        return json.loads(row[0]) if row else default

    def _set_meta(self, key, value):
        self.store.db.execute("INSERT INTO metadata VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value", (key, encode(value)))

    def _configure_actors(self, owner, principal, executors):
        actors = [owner, principal, *executors]
        if any(not isinstance(a, str) or not a.strip() for a in actors) or len(set(actors)) != len(actors):
            self.store.close()
            raise ValueError("invalid_actor_config")
        config = {"owner_actor": owner, "principal_actor": principal, "executor_actors": list(executors)}
        with self.store.transaction():
            existing = self._meta("actor_config")
            if existing is not None and existing != config:
                raise ValueError("actor_config_mismatch")
            self._set_meta("actor_config", config)
        self.owner_actor, self.principal_actor, self.executor_actors = owner, principal, tuple(executors)

    def actor_role(self, actor):
        if actor == self.owner_actor:
            return "owner"
        if actor == self.principal_actor:
            return "principal"
        if actor in self.executor_actors:
            return "executor"
        return None

    def _meaning(self, item):
        return fingerprint({k: item.get(k) for k in self.MEANING})

    def _scope_versions(self, item_id):
        _, versions = self._item(item_id)
        return {k: v["version"] for k, v in versions.items() if k in self.MEANING}

    def _within(self, item, scope_id):
        seen = set()
        while item and item["id"] not in seen:
            if item["id"] == scope_id:
                return True
            seen.add(item["id"])
            item = self._item(item.get("parent_id"))[0]
        return False

    def authorize(self, actor, capability, item_id, mandate_id=None):
        with self.store.lock:
            role = self.actor_role(actor)
            item = self._item(item_id)[0] if isinstance(item_id, str) else None
            reason = None
            if role is None:
                reason = "unauthorized_actor"
            elif capability not in {"prepare_private", "local_work"}:
                reason = "capability_not_enabled"
            elif not item:
                reason = "item_not_found"
            elif self.recovery_required and role != "owner":
                reason = "recovery_required"
            elif item["status"] in {"done", "withdrawn"}:
                reason = "terminal_item"
            elif item["status"] in {"paused", "postponed", "waiting"} and capability == "local_work":
                reason = "work_paused"
            elif capability == "local_work" and (item["kind"] not in {"action", "project", "waiting", "responsibility"} or item.get("commitment") != "committed"):
                reason = "item_not_committed_work"
            elif role == "owner":
                return {"allowed": True, "reason": "owner_local_authority"}
            elif not mandate_id and capability == "prepare_private" and role == "principal":
                return {"allowed": True, "reason": "standing_private_preparation"}
            else:
                mandate = self._meta("mandate:" + str(mandate_id))
                scope = self._item(mandate["scope_item_id"])[0] if mandate else None
                if not mandate:
                    reason = "mandate_required"
                elif mandate["status"] != "active":
                    reason = "mandate_" + mandate["status"]
                elif not scope or scope["status"] in {"done", "withdrawn"}:
                    reason = "mandate_exhausted"
                elif scope["status"] in {"paused", "postponed", "waiting"} and capability == "local_work":
                    reason = "work_paused"
                elif (self._meaning(scope) != mandate["scope_meaning"]
                      or self._scope_versions(scope["id"]) != mandate["scope_versions"]):
                    reason = "mandate_stale"
                elif capability not in mandate["capabilities"] or actor not in mandate["actors"]:
                    reason = "outside_mandate"
                elif not self._within(item, scope["id"]):
                    reason = "outside_mandate_scope"
                elif item.get("decision_needed") and capability == "local_work":
                    reason = "human_decision_pending"
                else:
                    return {"allowed": True, "reason": "active_mandate", "mandate_id": mandate_id}
            return {"allowed": False, "reason": reason}

    def work_paused(self, item_id):
        """Pause is an admission/write boundary; explicit reads remain available."""
        with self.store.lock:
            item = self._item(item_id)[0]
            seen = set()
            while item and item["id"] not in seen:
                if item["status"] == "paused":
                    return True
                seen.add(item["id"])
                item = self._item(item.get("parent_id"))[0]
            return False

    def _require(self, actor, capability, item, mandate_id=None):
        result = self.authorize(actor, capability, item["id"], mandate_id)
        if not result["allowed"]:
            raise ValueError(result["reason"])

    def mandates(self):
        with self.store.lock:
            return [json.loads(row[0]) for row in self.store.db.execute("SELECT value FROM metadata WHERE key LIKE 'mandate:%' ORDER BY key")]

    def _exhaust_mandates(self, item):
        for mandate in self.mandates():
            if mandate["scope_item_id"] == item["id"] and mandate["status"] == "active" and not mandate["recurring"]:
                mandate.update(status="exhausted", ended_at=now())
                self._set_meta("mandate:" + mandate["id"], mandate)

    def _review_event(self, item, reason):
        payload = {"item_id": item["id"], "version": item["version"], "reason": reason}
        key = fingerprint(["gtd-review", "local", item["id"], item["version"], reason])
        self.store.db.execute("INSERT OR IGNORE INTO events VALUES(?,?,?,?,?,?,?,?,NULL,?)",
            (key, "gtd-review", "local", item["id"], str(item["version"]) + ":" + reason,
             fingerprint(payload), encode(payload), "received", now()))

    def _authorize_change(self, actor, action, item, fields):
        if actor == self.owner_actor:
            return
        if action != "edit":
            raise ValueError("owner_or_assessment_required")
        if self.work_paused(item["id"]):
            raise ValueError("work_paused")
        operational = set(fields) - {"notes", "plan_steps", "uncertainties"}
        if operational:
            # The principal may maintain its own derived operational criteria;
            # this does not authorize replacing the owner's meaning or scope.
            _, versions = self._item(item["id"])
            mandate = self._meta("mandate:" + str(item.get("mandate_id")))
            if (actor != self.principal_actor or item.get("created_by") != actor
                    or item.get("kind") not in {"action", "waiting"}
                    or item.get("commitment") != "committed"
                    or not operational <= {"completion_criteria", "waiting_for"}
                    or ("waiting_for" in operational and item["kind"] != "waiting")
                    or not mandate or item["id"] == mandate["scope_item_id"]
                    or not item.get("parent_id") or not self._within(item, mandate["scope_item_id"])
                    or any(versions.get(key, {}).get("actor") != actor for key in operational)
                    or any(not isinstance(fields[key], str) or not fields[key].strip() for key in operational)):
                raise ValueError("human_position_protected")
        self._require(actor, "local_work", item, item.get("mandate_id"))

    def _semantic(self, actor, command, digest):
        action, operation_id = command["action"], command["operation_id"]
        fields = command.get("fields", {})
        if not isinstance(fields, dict):
            raise ValueError("invalid_fields")
        if action == "review":
            return self._review(actor, command, digest)
        if action == "set_attention":
            if actor != self.owner_actor:
                raise ValueError("owner_required")
            if set(fields) - {"paused", "notify", "return_at", "reason"} or not fields:
                raise ValueError("invalid_attention")
            for key in ("paused", "notify"):
                if key in fields and type(fields[key]) is not bool:
                    raise ValueError("invalid_attention")
            validate_date(fields.get("return_at"))
            attention = {**self._meta("attention", {"paused": False, "notify": True}), **fields}
            self._set_meta("attention", attention)
            return self._record(actor, operation_id, digest, {"operation_id": operation_id, "status": "applied", "attention": attention})
        item, versions = self._item(command.get("item_id"))
        if item is None:
            raise ValueError("item_not_found")
        expected = command.get("expected_version")
        if type(expected) is not int or not 1 <= expected <= item["version"]:
            raise ValueError("invalid_expected_version")
        # Semantic operations consume the meaning as a whole, unlike independent P1 notes.
        if expected != item["version"]:
            return self._conflict(actor, operation_id, digest, item, set(versions), versions)
        if action == 'request_review':
            if actor != self.owner_actor:
                raise ValueError('owner_required')
            if fields:
                raise ValueError('invalid_review_request')
            if self.work_paused(item['id']):
                raise ValueError('work_paused')
            if item['status'] in {'done', 'withdrawn'}:
                raise ValueError('review_target_terminal')
            payload = {'item_id': item['id'], 'version': item['version'],
                'reason': 'requested_review', 'operation_id': operation_id}
            key = fingerprint(['gtd-review', 'local', 'request:' + operation_id, '1'])
            self.store.db.execute('INSERT INTO events VALUES(?,?,?,?,?,?,?,?,NULL,?)',
                (key, 'gtd-review', 'local', 'request:' + operation_id, '1',
                 fingerprint(payload), encode(payload), 'received', now()))
            return self._record(actor, operation_id, digest, {'operation_id': operation_id,
                'status': 'applied', 'event_key': key, 'review_requested': True,
                'item_id': item['id'], 'expected_version': item['version']})
        if action == "apply_human_instruction":
            return self._apply_human_instruction(actor, operation_id, digest, item, versions, fields)
        if actor != self.owner_actor and self.work_paused(item["id"]):
            raise ValueError("work_paused")
        if action in {"grant_mandate", "revoke_mandate"}:
            return self._mandate_command(actor, command, digest, item, versions)
        if action == "derive":
            return self._derive(actor, command, digest, item)
        if action == "put_material":
            return self._put_material(actor, command, digest, item, versions)
        if action == "assess_result":
            return self._assess(actor, command, digest, item, versions)
        if action == "clarify" and fields.get("destination") == "existing":
            return self._route_existing(actor, operation_id, digest, item, versions, fields)
        if action == "clarify" and "destination" in fields:
            if (set(fields) != {"destination", "reason"} or fields["destination"] != "discard"
                    or not isinstance(fields["reason"], str) or not fields["reason"].strip()):
                raise ValueError("invalid_discard")
            if self.actor_role(actor) not in {"owner", "principal"}:
                raise ValueError("principal_required")
            if (item["kind"] not in {"capture", "proposed_entry"}
                    or item.get("commitment") == "committed" or item["status"] != "active"):
                raise ValueError("discard_only_unclarified_entry")
            # Intake disposal cannot undo a later human interpretation, source
            # correction, date/decision or explicit reopening of the entry.
            protected = self.MEANING | {"text", "source", "status", "decision_needed",
                "decision_question", "due_at", "review_at", "starts_at", "ends_at", "decision_at"}
            if any(v.get("actor") == self.owner_actor and v.get("version", 1) > 1
                   for key, v in versions.items() if key in protected):
                raise ValueError("human_position_protected")
            stamp = now()
            return self._apply_updates(actor, operation_id, digest, item, versions, {
                "status": "withdrawn", "withdrawn_at": stamp,
                "clarification": {"destination": "discard", "reason": fields["reason"].strip(),
                                  "actor": actor, "at": stamp}})
        if action in {"clarify", "plan"}:
            fields = dict(fields)
            intent_basis = fields.pop("intent_basis", None)
            private_intent = "capability" in fields
            if private_intent:
                capability = fields.pop("capability")
                if (action != "clarify" or capability != "prepare_private"
                        or self.actor_role(actor) not in {"owner", "principal"}
                        or item["kind"] not in {"capture", "proposed_entry"} or item.get("commitment") == "committed"
                        or item.get("status") != "active"
                        or fields.get("kind") not in {"action", "project"}
                        or fields.get("commitment") != "committed"
                        or not isinstance(fields.get("completion_criteria"), str)
                        or not fields["completion_criteria"].strip()
                        or fields.get("executor", self.principal_actor) != self.principal_actor):
                    raise ValueError("invalid_private_intent")
                self._validate_intent_basis(item, intent_basis, proposed_entry=True)
                if (intent_basis['source_item_id'] != item['id'] and set(fields) -
                        {'kind', 'commitment', 'completion_criteria', 'executor', 'title'}):
                    raise ValueError('routed_private_intent_fields_restricted')
                protected = self.MEANING | {"text", "source", "status", "decision_needed", "decision_question"}
                routed_resume = (intent_basis['source_item_id'] != item['id']
                    and self._attested_resumed_status(item))
                if any(v.get("actor") == self.owner_actor and v.get("version", 1) > 1
                       for key, v in versions.items() if key in protected and not (key == 'status' and routed_resume)):
                    raise ValueError("human_position_protected")
                fields["executor"] = self.principal_actor
            validate_fields(fields)
            self._validate_relations(item, fields)
            updates = dict(fields)
            if private_intent:
                updates["work_capability"] = "prepare_private"
                updates["intent_basis"] = {**intent_basis, "interpreted_by": actor, "recorded_at": now()}
            if actor != self.owner_actor:
                if actor != self.principal_actor:
                    raise ValueError("principal_required")
                if action == "plan":
                    self._require(actor, "prepare_private", item, item.get("mandate_id"))
                    if set(fields) - {"plan_steps", "uncertainties", "decision_needed", "decision_question", "source_versions"}:
                        raise ValueError("human_position_protected")
                    if "source_versions" in fields:
                        previous_sources = item.get("source_versions")
                        sources = fields["source_versions"]
                        # This is maintenance of the principal's dependency, not
                        # permission to select sources or adopt a human choice.
                        if (not previous_sources or set(sources) != set(previous_sources)
                                or versions.get("source_versions", {}).get("actor") != actor):
                            raise ValueError("human_position_protected")
                        if any(revision < previous_sources[sid]
                               or self._basis(sid)["source_revision"] != revision
                               for sid, revision in sources.items()):
                            raise ValueError("source_version_stale")
                    if any(key in fields and fields[key] != item.get(key)
                           and versions.get(key, {}).get("actor") == self.owner_actor
                           for key in ("decision_needed", "decision_question")):
                        raise ValueError("human_position_protected")
                else:
                    if item["kind"] not in {"capture", "proposed_entry"}:
                        raise ValueError("human_position_protected")
                    if fields.get("commitment") == "committed":
                        self._validate_intent_basis(item, intent_basis, proposed_entry=private_intent)
                        if fields.get("kind") not in {"action", "project", "calendar", "waiting", "responsibility"}:
                            raise ValueError("intent_not_actionable")
                        updates["intent_basis"] = {**intent_basis, "interpreted_by": actor, "recorded_at": now()}
                    else:
                        updates["commitment"] = "proposed"
                    # Do not replace meaning the human has explicitly corrected.
                    if any(versions.get(k, {}).get("actor") == self.owner_actor and versions.get(k, {}).get("version", 1) > 1 for k in fields):
                        raise ValueError("human_position_protected")
            elif fields.get("kind") in {"action", "project", "calendar", "waiting", "responsibility"}:
                updates.setdefault("commitment", "committed")
            if updates.get("decision_needed") and not updates.get("decision_question", item.get("decision_question")):
                raise ValueError("decision_question_required")
            return self._apply_updates(actor, operation_id, digest, item, versions, updates)
        raise ValueError("unknown_action")

    def _route_existing(self, actor, operation_id, digest, item, versions, fields):
        """Resolve intake to an existing subject, without authority over its state."""
        if (set(fields) != {'destination', 'target_item_id', 'reason', 'intent_basis'}
                or not isinstance(fields.get('target_item_id'), str)
                or not isinstance(fields.get('reason'), str) or not fields['reason'].strip()):
            raise ValueError('invalid_existing_destination')
        if self.actor_role(actor) not in {'owner', 'principal'}:
            raise ValueError('principal_required')
        if (item['kind'] not in {'capture', 'proposed_entry'} or item.get('commitment') == 'committed'
                or item['status'] != 'active'):
            raise ValueError('route_only_unclarified_entry')
        if item.get('decision_needed') or any(v.get('actor') == self.owner_actor and v.get('version', 1) > 1
                for key, v in versions.items() if key not in {'source', 'source_revisions', 'original'}):
            raise ValueError('human_position_protected')
        self._validate_human_source(item, {**fields['intent_basis'],
            'source_revision': len(item.get('source_revisions', []))}, require_full_quote=False)
        target, _ = self._item(fields['target_item_id'])
        if not target:
            raise ValueError('route_target_not_found')
        if target['id'] == item['id']:
            raise ValueError('route_target_is_source')
        if target['status'] in {'done', 'withdrawn'}:
            raise ValueError('route_target_terminal')
        if not self.authorize(self.principal_actor, 'prepare_private', target['id'], None)['allowed']:
            raise ValueError('route_target_not_readable')
        stamp = now()
        resolution = {'destination': 'existing', 'resolution': 'routed', 'target_item_id': target['id'],
            'target_version': target['version'], 'source_revision': len(item['source_revisions']),
            'source_version': item['version'] + 1,
            'reason': fields['reason'].strip(),
            'intent_basis': dict(fields['intent_basis']), 'actor': actor, 'at': stamp}
        receipt = self._apply_updates(actor, operation_id, digest, item, versions, {
            'status': 'withdrawn', 'withdrawn_at': stamp, 'clarification': resolution,
            'relations': [*item.get('relations', []), {'type': 'routed_to', 'target_id': target['id']}]})
        payload = {'item_id': target['id'], 'target_version': target['version'],
            'reason': 'routed_human_instruction', 'source_capture_id': item['id'],
            'source_original': item.get('original'), 'original_text': item['source_revisions'][-1]['text'],
            'intent_basis': dict(fields['intent_basis']), 'reason_detail': fields['reason'].strip()}
        external_id, revision = 'routed:' + item['id'], str(receipt['item']['version'])
        key = fingerprint(['gtd-review', 'local', external_id, revision])
        self.store.db.execute('INSERT INTO events VALUES(?,?,?,?,?,?,?,?,NULL,?)',
            (key, 'gtd-review', 'local', external_id, revision, fingerprint(payload), encode(payload), 'received', stamp))
        return receipt

    def _validate_human_source(self, source, basis, *, require_full_quote=True):
        """Verify current direct provenance; linguistic entailment belongs to the principal."""
        if (not isinstance(basis, dict) or set(basis) != {"source_item_id", "source_revision", "quote"}
                or not source or basis.get("source_item_id") != source["id"]
                or source.get("created_by") != self.owner_actor):
            raise ValueError("intent_basis_not_owner_direct")
        _, source_fields = self._item(source["id"])
        if source_fields.get("source_revisions", {}).get("actor") != self.owner_actor:
            raise ValueError("intent_basis_not_owner_direct")
        revisions = source.get("source_revisions", [])
        revision = basis.get("source_revision")
        if type(revision) is not int or revision < 1 or revision != len(revisions):
            raise ValueError("source_version_stale")
        def indirect(value):
            if isinstance(value, dict):
                return any((key in {"forward_origin", "forward_from", "forward_sender_name",
                    "forwarded", "third_party", "forward_from_chat", "forward_date"} and bool(child))
                    or indirect(child) for key, child in value.items())
            return isinstance(value, list) and any(indirect(child) for child in value)
        metadata = revisions[-1].get("source", {})
        if (not isinstance(metadata, dict) or metadata.get("provider") not in {None, "local", "telegram"}
                or indirect(metadata) or indirect(source.get("source", {}))
                or not isinstance(basis.get("quote"), str) or not basis["quote"].strip()
                or not isinstance(revisions[-1].get("text"), str)
                or (basis["quote"] != revisions[-1]["text"] if require_full_quote
                    else basis["quote"] not in revisions[-1]["text"])):
            raise ValueError("intent_basis_not_owner_direct")

    def _apply_human_instruction(self, actor, operation_id, digest, item, versions, fields):
        if actor != self.principal_actor:
            raise ValueError("principal_required")
        if (set(fields) != {"instruction", "intent_basis", "changes"}
                or fields.get("instruction") not in {"correct", "pause"}
                or not isinstance(fields.get("changes"), dict)):
            raise ValueError("invalid_human_instruction")
        instruction, changes = fields["instruction"], fields["changes"]
        if (instruction == "correct" and (not changes or set(changes) - {"title", "text"})
                or instruction == "pause" and changes):
            raise ValueError("invalid_human_instruction")
        if (item["status"] in {"done", "withdrawn"}
                or instruction == "correct" and (item["kind"] != "possibility" or item.get("commitment") != "proposed")):
            raise ValueError("human_instruction_target_invalid")
        if changes:
            validate_fields(changes)
        basis = fields["intent_basis"]
        source = self._item(basis.get("source_item_id"))[0] if isinstance(basis, dict) and isinstance(basis.get("source_item_id"), str) else None
        self._validate_human_source(source, basis)
        consumed_key = "human_instruction:" + fingerprint([source["id"], basis["source_revision"]])
        if self._meta(consumed_key) is not None:
            raise ValueError("human_instruction_source_consumed")
        route = source.get("clarification", {})
        if (route.get("destination") != "existing" or route.get("resolution") != "routed"
                or route.get("target_item_id") != item["id"]):
            raise ValueError("human_instruction_source_not_routed")
        if (route.get("source_revision") != basis["source_revision"]
                or route.get("source_version") != source["version"]
                or route.get("target_version") != item["version"]):
            raise ValueError("human_instruction_route_stale")
        evidence = {"instruction": instruction, "intent_basis": dict(basis), "changes": dict(changes),
            "interpreted_by": actor, "owner_actor": self.owner_actor, "operation_id": operation_id,
            "target_version": item["version"], "recorded_at": now()}
        updates = {**changes, "human_instruction": evidence}
        if instruction == "pause":
            updates["status"] = "paused"
        else:
            updates["source_versions"] = {**item.get("source_versions", {}), source["id"]: basis["source_revision"]}
        receipt = self._apply_updates(actor, operation_id, digest, item, versions, updates)
        self._set_meta(consumed_key, evidence)
        return receipt

    def _attested_owner_state_transition(self, item, row):
        before = json.loads(row['before_patch'] or '{}')
        after = json.loads(row['after_patch'] or '{}')
        evidence = self._meta('owner_state_action:' + row['operation_id'], {})
        action = evidence.get('action')
        return (row['actor'] == self.owner_actor and action in {'pause', 'reopen'}
            and evidence == {'action': action, 'item_id': item['id'], 'applied_version': row['applied_version']}
            and not set(after) - {'status', 'completed_at', 'withdrawn_at', 'review_at'}
            and after.get('status') == {'present': True, 'value': 'paused' if action == 'pause' else 'active'}
            and before.get('status', {}).get('value') in ({'active', 'paused'} if action == 'pause' else {'paused'})
            and not any(entry.get('present') and entry.get('value') is not None
                        for field, entry in before.items() if field != 'status'))

    def _attested_resumed_status(self, item):
        if item['status'] != 'active':
            return False
        rows = self.store.db.execute(
            'SELECT actor,operation_id,applied_version,before_patch,after_patch FROM operations '
            'WHERE item_id=? AND applied_version>1 ORDER BY applied_version', (item['id'],)).fetchall()
        status_changes = [row for row in rows if 'status' in json.loads(row['after_patch'] or '{}')]
        return bool(status_changes) and all(self._attested_owner_state_transition(item, row) for row in status_changes)

    def routed_human_sources(self, item):
        """Current direct routed evidence for context, independently of target kind."""
        if not item or item['status'] in {'done', 'withdrawn'}:
            return []
        sources = []
        for source in self.query():
            route = source.get('clarification', {})
            if (route.get('target_item_id') != item['id'] or route.get('destination') != 'existing'
                    or route.get('resolution') != 'routed' or route.get('source_version') != source['version']):
                continue
            revision = route.get('source_revision')
            if self._meta('human_instruction:' + fingerprint([source['id'], revision])) is not None:
                continue
            revisions = source.get('source_revisions', [])
            basis = {'source_item_id': source['id'], 'quote': revisions[-1].get('text') if revisions else None}
            try:
                self._validate_human_source(source, {**basis, 'source_revision': revision})
            except ValueError:
                continue
            sources.append({'source_item_id': source['id'], 'source_version': source['version'],
                'source_revision': revision, 'intent_basis': basis, 'clarification': route})
        return sources

    def pending_routed_intents(self, item):
        """Recover compatible capture intent, never replay terminal events."""
        if item['kind'] not in {'capture', 'proposed_entry'} or item['status'] != 'active':
            return []
        pending = []
        for evidence in self.routed_human_sources(item):
            try:
                self._validate_intent_basis(item, evidence['intent_basis'], proposed_entry=True)
            except ValueError:
                continue
            pending.append(evidence)
        return pending

    def _validate_intent_basis(self, item, basis, *, proposed_entry=False):
        # This validates provenance, not linguistic entailment. The configured
        # principal owns interpretation and records its exact evidence for review.
        if not isinstance(basis, dict) or set(basis) != {"quote", "source_item_id"}:
            raise ValueError("mandate_required")
        if proposed_entry and basis.get("source_item_id") != item["id"]:
            source, _ = self._item(basis.get("source_item_id"))
            route = source.get("clarification", {}) if source else {}
            if (item["kind"] not in {"capture", "proposed_entry"}
                    or item.get("commitment") == "committed" or item["status"] != "active"
                    or route.get("destination") != "existing" or route.get("resolution") != "routed"
                    or route.get("target_item_id") != item["id"]):
                raise ValueError("human_instruction_source_not_routed")
            self._validate_human_source(source, {**basis,
                "source_revision": route.get("source_revision")})
            if route.get("source_version") != source["version"]:
                raise ValueError("human_instruction_route_stale")
            base = route.get("target_version")
            if type(base) is not int or not 1 <= base <= item["version"]:
                raise ValueError("human_instruction_route_stale")
            if base != item["version"]:
                allowed = {'plan_steps', 'uncertainties', 'decision_needed', 'decision_question'}
                _, field_versions = self._item(item['id'])
                state_fields = {'status', 'completed_at', 'withdrawn_at', 'review_at'}
                if any(not (version.get('actor') == self.principal_actor and field in allowed
                            or version.get('actor') == self.owner_actor and field in state_fields)
                       for field, version in field_versions.items() if version.get('version', 1) > base):
                    raise ValueError('human_instruction_route_stale')
                # Also reject intervening human/material changes later overwritten
                # by a principal: latest field versions alone cannot prove absence.
                rows = self.store.db.execute(
                    'SELECT actor,operation_id,applied_version,before_patch,after_patch FROM operations WHERE item_id=? '
                    'AND applied_version>? ORDER BY applied_version', (item['id'], base)).fetchall()
                if [row['applied_version'] for row in rows] != list(range(base + 1, item['version'] + 1)):
                    raise ValueError('human_instruction_route_stale')
                for row in rows:
                    after = json.loads(row['after_patch'] or '{}')
                    if row['actor'] == self.principal_actor and not set(after) - allowed:
                        continue
                    if not self._attested_owner_state_transition(item, row):
                        raise ValueError('human_instruction_route_stale')
            return
        source = item.get("source", {})
        if (item["kind"] not in ({"capture", "proposed_entry"} if proposed_entry else {"capture"}) or item.get("created_by") != self.owner_actor
                or source.get("provider") not in {None, "telegram"}
                or any(source.get(k) for k in ("forward_origin", "forward_from", "forward_sender_name", "forwarded", "third_party"))
                or basis.get("source_item_id") != item["id"]
                or not isinstance(basis.get("quote"), str) or not basis["quote"].strip()
                or not item.get("source_revisions")
                or basis["quote"] not in (item["source_revisions"][0].get("text") or "")):
            raise ValueError("intent_basis_not_owner_direct")

    def _apply_updates(self, actor, operation_id, digest, item, versions, updates):
        return self._apply(actor, operation_id, digest, item, versions,
            {k: {"present": True, "value": v} for k, v in updates.items() if k not in item or item[k] != v})

    def _mandate_command(self, actor, command, digest, item, versions):
        if actor != self.owner_actor:
            raise ValueError("owner_required")
        fields, operation_id = command.get("fields", {}), command["operation_id"]
        if command["action"] == "grant_mandate":
            if set(fields) - {"scope_item_id", "capabilities", "completion_criteria", "actors", "recurring"}:
                raise ValueError("invalid_mandate")
            capabilities = fields.get("capabilities")
            actors = fields.get("actors", [self.principal_actor])
            criteria = fields.get("completion_criteria")
            if (fields.get("scope_item_id") != item["id"] or item["status"] in {"done", "withdrawn"}
                    or item.get("commitment") != "committed"
                    or item["kind"] not in {"action", "project", "waiting", "responsibility"}
                    or not isinstance(capabilities, list) or not capabilities
                    or any(c not in {"prepare_private", "local_work"} for c in capabilities)
                    or not isinstance(actors, list) or not actors
                    or any(self.actor_role(a) not in {"principal", "executor"} for a in actors)
                    or not isinstance(criteria, str) or not criteria.strip()
                    or type(fields.get("recurring", False)) is not bool):
                raise ValueError("invalid_mandate")
            mandate = {"id": uuid.uuid4().hex, "scope_item_id": item["id"], "scope_meaning": self._meaning(item), "scope_versions": self._scope_versions(item["id"]),
                "capabilities": capabilities, "actors": actors, "completion_criteria": criteria,
                "recurring": fields.get("recurring", False), "status": "active", "granted_by": actor, "created_at": now()}
        else:
            if set(fields) != {"mandate_id"}:
                raise ValueError("invalid_mandate")
            mandate = self._meta("mandate:" + str(fields["mandate_id"]))
            if not mandate or mandate["scope_item_id"] != item["id"]:
                raise ValueError("mandate_not_found")
            mandate.update(status="revoked", ended_at=now())
        self._set_meta("mandate:" + mandate["id"], mandate)
        receipt = self._apply_updates(actor, operation_id, digest, item, versions, {"mandate_id": mandate["id"]})
        receipt["mandate"] = mandate
        self.store.db.execute("UPDATE operations SET receipt=? WHERE operation_id=?", (encode(receipt), operation_id))
        return receipt

    def _derive(self, actor, command, digest, parent):
        if self.actor_role(actor) not in {"owner", "principal"}:
            raise ValueError("principal_required")
        fields = dict(command["fields"])
        mandate_id = fields.pop("mandate_id", None)
        capability = fields.pop("capability", "local_work")
        validate_fields(fields)
        if fields.get("kind") not in {"action", "project", "waiting", "possibility", "reference"} or not fields.get("title"):
            raise ValueError("invalid_derived_item")
        proposed = fields.get("commitment") == "proposed" or fields["kind"] in {"possibility", "reference"}
        if not mandate_id and actor != self.owner_actor and capability == "local_work":
            proposed = True
        if not proposed:
            self._require(actor, capability, parent, mandate_id)
        elif self.actor_role(actor) not in {"owner", "principal"}:
            raise ValueError("principal_required")
        # Standing preparation can create preparation work, never adopt its source.
        if not mandate_id and actor != self.owner_actor:
            if capability != "prepare_private":
                proposed = True
            else:
                fields["executor"] = self.principal_actor
        stamp = now()
        child = {"id": uuid.uuid4().hex, "kind": fields["kind"], "status": "active", "version": 1,
            "created_at": stamp, "updated_at": stamp, "created_by": actor, "depends_on": [], "relations": [],
            "source": parent.get("source", {}), "source_revisions": [], **fields,
            "parent_id": parent["id"], "mandate_id": mandate_id,
            "commitment": "proposed" if proposed else "committed", "work_capability": capability}
        if parent["kind"] == "project":
            child.setdefault("project_id", parent["id"])
        self._validate_relations(child, fields)
        versions = {k: {"version": 1, "actor": actor, "operation_id": command["operation_id"]} for k in child}
        self.store.db.execute("INSERT INTO items VALUES(?,?,?)", (child["id"], encode(child), encode(versions)))
        self._review_event(child, "derive")
        return self._record(actor, command["operation_id"], digest,
            {"operation_id": command["operation_id"], "status": "applied", "item": child}, {}, {"_created": True}, 1)

    def _basis(self, item_id):
        item, versions = self._item(item_id)
        if not item:
            raise ValueError("source_not_found")
        return {"text": fingerprint(item.get("text")), "source_revision": len(item.get("source_revisions", [])), "source": fingerprint(item.get("source", {})), "meaning": self._meaning(item),
            "human_versions": {k: v["version"] for k, v in versions.items()
                if v.get("actor") == self.owner_actor and k in self.MEANING | {"text", "source"}}}

    def _put_material(self, actor, command, digest, item, versions):
        fields = command["fields"]
        if set(fields) - {"content", "title", "material_id", "source_versions", "mandate_id", "mime_type", "content_base64", "filename", "source_material"}:
            raise ValueError("invalid_material")
        self._require(actor, "prepare_private", item, fields.get("mandate_id", item.get("mandate_id")))
        material_id = fields.get("material_id") or uuid.uuid4().hex
        previous = self._raw_materials(item["id"], material_id)
        if previous and previous[-1]["author"] == self.owner_actor and actor != self.owner_actor:
            raise ValueError("human_material_protected")
        if fields.get("material_id") and not previous:
            raise ValueError("material_not_found")
        from .material_files import decode_pptx, PPTX_MIME
        binary = 'content_base64' in fields or 'filename' in fields
        copied = None
        if 'source_material' in fields:
            if set(fields) & {'content', 'content_base64', 'filename', 'mime_type'}:
                raise ValueError('invalid_material_content_choice')
            ref = fields['source_material']
            if (not isinstance(ref, dict) or set(ref) != {'item_id', 'material_id', 'version', 'sha256'}
                    or not isinstance(ref['item_id'], str) or not isinstance(ref['material_id'], str)
                    or type(ref['version']) is not int or ref['version'] < 1
                    or not isinstance(ref['sha256'], str) or len(ref['sha256']) != 64):
                raise ValueError('invalid_source_material')
            source_item = self._item(ref['item_id'])[0]
            if source_item is None:
                raise ValueError('material_not_found')
            self._require(actor, 'prepare_private', source_item, fields.get('mandate_id'))
            copied = next((m for m in self.materials(ref['item_id'])
                if m['id'] == ref['material_id'] and m['version'] == ref['version']), None)
            if not copied or not copied['valid']:
                raise ValueError('source_material_not_current')
            if copied['original']['sha256'] != ref['sha256']:
                raise ValueError('source_material_hash_mismatch')
            if ref['item_id'] == item['id'] and ref['material_id'] == material_id:
                raise ValueError('material_copy_self_version')
            original = self.read_material_file(ref['item_id'], ref['material_id'], ref['version'])
            data, filename, mime_type = original['data'], original['filename'], original['mime_type']
        elif binary:
            if 'content' in fields or not {'content_base64', 'filename', 'mime_type'} <= set(fields):
                raise ValueError('invalid_material_content_choice')
            data, filename, mime_type = decode_pptx(fields)
        else:
            content = fields.get('content')
            if not isinstance(content, str) or not content.strip():
                raise ValueError('material_content_required')
            if fields.get('mime_type') == PPTX_MIME:
                raise ValueError('pptx_binary_content_required')
            data, filename, mime_type = content.encode(), 'material.txt', fields.get('mime_type', 'text/plain; charset=utf-8')
        sources = fields.get("source_versions", {})
        if not isinstance(sources, dict):
            raise ValueError("invalid_source_versions")
        for source_id, revision in sources.items():
            if type(revision) is not int or self._basis(source_id)["source_revision"] != revision:
                raise ValueError("source_version_stale")
        blob = self.store.save_original(data)
        blob.update(filename=filename, mime_type=mime_type)
        self.store.db.execute("INSERT OR IGNORE INTO originals VALUES(?,?,?)", (blob["sha256"], blob["size"], blob["path"]))
        material = {"id": material_id, "version": len(previous) + 1, "author": actor,
            "title": fields.get("title", "Material preparado"), "original": blob, "created_at": now(),
            "basis": {source_id: self._basis(source_id) for source_id in {item["id"], *sources}},
            "source_versions": sources, "mandate_id": fields.get("mandate_id", item.get("mandate_id"))}
        if copied:
            # Preserve dependency snapshots and actual source authorship. New
            # destination fields cannot wash away stale source evidence.
            material['basis'].update(copied['basis'])
            material['basis'][ref['item_id']] = self._basis(ref['item_id'])
            material['basis'][item['id']] = self._basis(item['id'])
            material['source_versions'] = {**copied.get('source_versions', {}), **sources}
            material['source_material'] = {**ref, 'author': copied['author'], 'created_at': copied['created_at']}
        self._insert_material_row(item["id"], material)
        # Receipts, patches and the stored document all carry reference stubs;
        # full rows live only in materials. Readers resolve content by digest.
        history = [self._material_stub(entry) for entry in self._raw_materials(item["id"])]
        receipt = self._apply_updates(actor, command["operation_id"], digest, item, versions, {"materials": history})
        self._store_result_stubs(item["id"])
        return receipt

    def _store_result_stubs(self, item_id):
        # Derive the document projection from the authoritative rows, in the
        # same transaction as the write that triggered it. Never invents rows.
        # Absent stays absent: like before the cut, arrays appear only once
        # they hold references, so receipts and stored documents keep the
        # same shape.
        document, _ = self._item(item_id)
        if document is None:
            return
        document = dict(document)
        stubs = [self._material_stub(material) for material in self._raw_materials(item_id)]
        if stubs:
            document["materials"] = stubs
        else:
            document.pop("materials", None)
        assess = [self._assessment_stub(assessment) for assessment in self._assessment_rows(item_id)]
        if assess:
            document["assessments"] = assess
        else:
            document.pop("assessments", None)
        self.store.db.execute("UPDATE items SET document=? WHERE id=?", (encode(document), item_id))

    @staticmethod
    def _material_stub(material):
        # Reference projection kept in the item document. Identity, authorship
        # and judgment stay readable; base snapshots live in materials rows.
        # Idempotent: an existing stub (no base snapshots) passes through.
        if "basis" not in material and "original" not in material:
            return dict(material)
        stub = {"id": material["id"], "version": material["version"],
                "author": material["author"], "title": material.get("title"),
                "digest": material["original"]["sha256"], "size": material["original"]["size"],
                "mime_type": material["original"].get("mime_type"), "created_at": material.get("created_at")}
        # Mandate scope and copy provenance are identity (who/what/when),
        # not base snapshots.
        if material.get("mandate_id") is not None:
            stub["mandate_id"] = material["mandate_id"]
        if isinstance(material.get("source_material"), dict):
            stub["source_material"] = dict(material["source_material"])
        return stub

    def _material_stubs(self, item_id):
        return [self._material_stub(material) for material in self._raw_materials(item_id)]

    def _insert_material_row(self, item_id, material):
        original = material["original"]
        self.store.db.execute(
            "INSERT INTO materials(id, version, item_id, author, title, mime_type, filename,"
            " digest, size, basis_json, source_versions_json, mandate_id, source_material_json, created_at)"
            " VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (material["id"], material["version"], item_id, material["author"],
             material.get("title", "Material preparado"),
             original.get("mime_type", "text/plain; charset=utf-8"),
             original.get("filename", "material.txt"),
             original["sha256"], original["size"],
             encode(material.get("basis", {})), encode(material.get("source_versions", {})),
             material.get("mandate_id"),
             encode(material["source_material"]) if material.get("source_material") else None,
             material.get("created_at")))

    def _material_row(self, item_id, material_id, version):
        row = self.store.db.execute(
            "SELECT * FROM materials WHERE item_id=? AND id=? AND version=?",
            (item_id, material_id, version)).fetchone()
        return self._material_dict(row) if row else None

    @staticmethod
    def _material_dict(row):
        material = {"id": row["id"], "version": row["version"], "author": row["author"],
            "title": row["title"], "created_at": row["created_at"],
            "basis": json.loads(row["basis_json"]),
            "source_versions": json.loads(row["source_versions_json"]),
            "mandate_id": row["mandate_id"],
            "original": {"path": f"originals/{row['digest']}", "sha256": row["digest"],
                         "size": row["size"], "filename": row["filename"], "mime_type": row["mime_type"]}}
        if row["source_material_json"]:
            material["source_material"] = json.loads(row["source_material_json"])
        return material

    def _raw_materials(self, item_id, material_id=None):
        # Full table rows without validity flags: the shape historical
        # material_basis snapshots and admission bases already carry. Ordered
        # by insertion (rowid): document arrays were append-ordered and UUID
        # order must never stand in for chronology.
        if material_id is not None:
            rows = self.store.db.execute(
                "SELECT * FROM materials WHERE item_id=? AND id=? ORDER BY version",
                (item_id, material_id)).fetchall()
        else:
            rows = self.store.db.execute(
                "SELECT * FROM materials WHERE item_id=? ORDER BY rowid",
                (item_id,)).fetchall()
        return [self._material_dict(row) for row in rows]

    def _material_invalid_reasons(self, item_id, material, visited=frozenset()):
        identity = (item_id, material['id'], material['version'])
        if identity in visited or len(visited) >= 64:
            return ['source_material_chain_invalid']
        row = self.store.db.execute(
            "SELECT MAX(version) FROM materials WHERE item_id=? AND id=?",
            (item_id, material['id'])).fetchone()
        latest = row[0] or 0
        reasons = ['basis_changed:' + sid for sid, basis in material['basis'].items() if self._basis(sid) != basis]
        if material['version'] != latest:
            reasons.append('material_superseded')
        mandate = self._meta('mandate:' + str(material.get('mandate_id')))
        if mandate and mandate['status'] == 'revoked':
            reasons.append('mandate_revoked')
        reference = material.get('source_material')
        if reference:
            source = self._material_row(reference['item_id'], reference['material_id'], reference['version'])
            if (source is None or source['original']['sha256'] != reference['sha256']
                    or self._material_invalid_reasons(reference['item_id'], source, visited | {identity})):
                reasons.append('source_material_not_current')
        return reasons

    def materials(self, item_id):
        with self.store.lock:
            if self._item(item_id)[0] is None:
                return []
            return [{**material, "valid": not (reasons := self._material_invalid_reasons(item_id, material)),
                     "invalid_reasons": reasons}
                    for material in self._raw_materials(item_id)]

    def _assessment_rows(self, item_id):
        rows = self.store.db.execute(
            "SELECT * FROM assessments WHERE item_id=? ORDER BY created_at, rowid",
            (item_id,)).fetchall()
        return [self._assessment_dict(row) for row in rows]

    def assessments(self, item_id):
        """Full assessment rows by identity; the item document keeps stubs."""
        with self.store.lock:
            return self._assessment_rows(item_id)

    @staticmethod
    def _assessment_dict(row):
        # Keys absent at write time stay absent (NULL columns are omitted), so
        # table reads reproduce the stored receipt shape exactly.
        assessment = {"id": row["id"], "item_version": row["item_version"],
            "actor": row["actor"], "satisfied": bool(row["satisfied"]),
            "criterion_hash": row["criterion_hash"], "evidence": row["evidence"],
            "source_versions": json.loads(row["source_versions_json"]),
            "assessed_at": row["created_at"],
            "resolution_basis": json.loads(row["resolution_basis_json"]),
            "material_basis": json.loads(row["material_basis_json"])}
        if row["mandate_id"] is not None:
            assessment["mandate_id"] = row["mandate_id"]
        if row["material_id"] is not None:
            assessment["material_id"] = row["material_id"]
            assessment["material_version"] = row["material_version"]
        if row["gap"] is not None:
            assessment["gap"] = row["gap"]
        return assessment

    @staticmethod
    def _assessment_stub(assessment):
        # Reference projection kept in the item document: everything but the
        # material_basis snapshot, which duplicates the materials collection
        # per assessment and lives in assessment rows. The verdict context
        # (resolution_basis) stays readable so composed views keep evidence.
        # Idempotent: an existing stub passes through unchanged. Explicit None
        # optionals read the same as absent keys (NULL columns are omitted).
        return {key: value for key, value in assessment.items()
                if key != "material_basis" and value is not None}

    @staticmethod
    def _stub_view(item):
        # Normalize either representation era to reference stubs so a stored
        # receipt and the current document compare on identity and judgment.
        view = dict(item)
        view["materials"] = [GTDDomain._material_stub(m) for m in item.get("materials", [])]
        view["assessments"] = [GTDDomain._assessment_stub(a) for a in item.get("assessments", [])]
        return view

    def read_material(self, item_id, material_id, version):
        """Read one UTF-8 original (maximum 256 KiB), without changing validity."""
        if type(version) is not int or version < 1:
            raise ValueError("invalid_material_version")
        with self.store.lock:
            material = next((m for m in self.materials(item_id)
                if m["id"] == material_id and m["version"] == version), None)
            if not material:
                raise ValueError("material_not_found")
            original = material["original"]
            mime = original.get("mime_type", "").split(";", 1)[0].strip().lower()
            if not (mime.startswith("text/") or mime in {"application/json", "application/xml"}):
                raise ValueError("material_not_textual")
            from .material_files import read_original
            data = read_original(self.store, original, 262144)
            digest = original['sha256']
            try:
                content = data.decode('utf-8')
            except UnicodeError as exc:
                raise ValueError('material_unreadable') from exc
            return {"item_id": item_id, "material_id": material_id, "version": version,
                "content": content, "sha256": digest, "size": len(data),
                "valid": material["valid"], "invalid_reasons": material["invalid_reasons"]}

    def read_material_file(self, item_id, material_id, version):
        """Internal identified-file read. Transport must authorize scope first."""
        from .material_files import MAX_FILE, read_original
        if type(version) is not int or version < 1:
            raise ValueError('invalid_material_version')
        with self.store.lock:
            material = next((m for m in self.materials(item_id)
                if m['id'] == material_id and m['version'] == version), None)
            if material is None:
                raise ValueError('material_not_found')
            data = read_original(self.store, material['original'], MAX_FILE)
            return {'item_id': item_id, 'material_id': material_id, 'version': version,
                'data': data, 'sha256': material['original']['sha256'], 'size': len(data),
                'filename': material['original'].get('filename', 'material.bin'),
                'mime_type': material['original'].get('mime_type', 'application/octet-stream'),
                'valid': material['valid'], 'invalid_reasons': material['invalid_reasons']}

    def _assess(self, actor, command, digest, item, versions):
        fields = command["fields"]
        if set(fields) - {"evidence", "satisfied", "material_id", "material_version", "source_versions", "gap", "mandate_id"}:
            raise ValueError("invalid_assessment")
        capability = item.get("work_capability", "local_work")
        mandate_id = fields.get("mandate_id", item.get("mandate_id"))
        if actor != self.owner_actor and capability == "prepare_private" and item.get("intent_basis"):
            if item.get("status") in {"paused", "postponed", "waiting"}:
                raise ValueError("work_paused")
            classified_at = versions.get("work_capability", {}).get("version", 0)
            changed = not classified_at or any(v.get("actor") == self.owner_actor
                and v.get("version", 0) > classified_at for key, v in versions.items() if key in self.MEANING)
            if changed:
                if not mandate_id:
                    raise ValueError("human_position_protected")
                # Only a newly applicable explicit mandate can replace the old
                # private interpretation; authorize validates its current scope.
        self._require(actor, capability, item, mandate_id)
        if not isinstance(fields.get("evidence"), str) or not fields["evidence"].strip() or type(fields.get("satisfied")) is not bool:
            raise ValueError("assessment_evidence_required")
        if item.get("commitment") != "committed" or item["kind"] not in {"action", "project", "waiting"}:
            raise ValueError("kind_not_completable")
        if not item.get("completion_criteria"):
            raise ValueError("completion_criteria_required")
        if item.get("decision_needed"):
            raise ValueError("human_decision_pending")
        required = item.get("source_versions", {})
        supplied = fields.get("source_versions", {})
        if not isinstance(supplied, dict) or set(required) - set(supplied):
            raise ValueError("source_coverage_incomplete")
        for sid, revision in supplied.items():
            if type(revision) is not int or self._basis(sid)["source_revision"] != revision:
                raise ValueError("source_version_stale")
        if fields.get("material_id"):
            material = next((m for m in self.materials(item["id"]) if m["id"] == fields["material_id"] and m["version"] == fields.get("material_version")), None)
            if not material or not material["valid"]:
                raise ValueError("material_stale_or_missing")
        if fields["satisfied"] and any(self._item(dep)[0].get("status") != "done" for dep in item.get("depends_on", [])):
            raise ValueError("dependencies_incomplete")
        assessment = {**fields, "id": fingerprint([item["id"], now(), fields.get("evidence", "")]),
            "actor": actor, "assessed_at": now(), "item_version": item["version"],
            "criterion_hash": fingerprint(fields.get("evidence", "")),
            "source_versions": fields.get("source_versions", {}),
            "resolution_basis": self.work_input_basis(item["id"], fields.get("source_versions", {})),
            "material_basis": self._raw_materials(item["id"])}
        self.store.db.execute(
            "INSERT INTO assessments(id, item_id, item_version, material_id, material_version,"
            " actor, satisfied, criterion_hash, evidence, gap, resolution_basis_json,"
            " material_basis_json, source_versions_json, mandate_id, created_at)"
            " VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (assessment["id"], item["id"], item["version"], fields.get("material_id"),
             fields.get("material_version"), actor, 1 if fields["satisfied"] else 0,
             assessment["criterion_hash"], fields["evidence"], fields.get("gap"),
             encode(assessment["resolution_basis"]), encode(assessment["material_basis"]),
             encode(fields.get("source_versions", {})), fields.get("mandate_id", item.get("mandate_id")),
             assessment["assessed_at"]))
        full = [self._assessment_stub(entry) for entry in self._assessment_rows(item["id"])]
        updates = {"assessments": full, "result_gap": None if fields["satisfied"] else fields.get("gap", "criterion_not_met")}
        if fields["satisfied"]:
            updates.update(status="done", completed_at=now())
        receipt = self._apply_updates(actor, command["operation_id"], digest, item, versions, updates)
        self._store_result_stubs(item["id"])
        return receipt

    @staticmethod
    def _instant(value):
        validate_date(value)
        parsed = datetime.fromisoformat(value)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)

    def choose(self, context):
        if not isinstance(context, dict):
            raise ValueError("invalid_context")
        with self.store.lock:
            available = self.query({"available": True})
            human, agent = [], []
            for item in available:
                if item.get("starts_at") and self._instant(item["starts_at"]) > self._instant(context.get("now", now())):
                    continue
                if item.get("decision_needed"):
                    continue
                executor = item.get("executor", self.owner_actor)
                if executor != self.owner_actor:
                    capability = item.get("work_capability", "local_work")
                    if self.authorize(executor, capability, item["id"], item.get("mandate_id"))["allowed"]:
                        agent.append(item)
                    continue
                if item.get("context") and item["context"] not in context.get("contexts", [context.get("context")]):
                    continue
                if context.get("minutes") is not None and (item.get("duration_minutes") is None or item["duration_minutes"] > context["minutes"]):
                    continue
                if item.get("capacity") and item["capacity"] != context.get("capacity"):
                    continue
                if item.get("energy") and item["energy"] != context.get("energy"):
                    continue
                human.append(item)
            human.sort(key=lambda x: (-float(x.get("priority", 0)), x["created_at"], x["id"]))
            return {"selected": human[0] if human else None, "human_actions": human, "agent_actions": agent,
                "context": context, "limits": ["Selection uses declared context; it does not complete an action."]}

    def work_input_basis(self, item_id, extra_sources=(), *, include_evidence=True):
        """External generations only: our outputs cannot renew execution authority."""
        with self.store.lock:
            pending, seen, basis = [item_id, *extra_sources], set(), {}
            while pending:
                sid = pending.pop()
                if sid in seen:
                    continue
                seen.add(sid)
                item = self.get_item(sid)
                if not item:
                    basis[sid] = None
                    continue
                row = self.store.db.execute('SELECT field_versions FROM items WHERE id=?', (sid,)).fetchone()
                fields = json.loads(row[0])
                basis[sid] = {'source': item.get('source', {}), 'revisions': item.get('source_revisions', []),
                    'human': {k: v for k, v in fields.items() if v.get('actor') == self.owner_actor
                        and k not in {'notes', 'coverage', 'version', 'updated_at', 'assessments', 'result_gap'}},
                    'human_materials': [m for m in self._raw_materials(sid) if m.get('author') == self.owner_actor]}
                if include_evidence or sid != item_id or fields.get('source_versions', {}).get('actor') == self.owner_actor:
                    pending.extend(item.get('source_versions', {}))
                if include_evidence:
                    for evidence in [*self._raw_materials(sid),
                                     *(a for a in self.assessments(sid))]:
                        pending.extend(evidence.get('source_versions', {}))
                        pending.extend(evidence.get('basis', {}))
                if include_evidence or sid != item_id or fields.get('depends_on', {}).get('actor') == self.owner_actor:
                    pending.extend(item.get('depends_on', []))
                if item.get('parent_id') and (include_evidence or sid != item_id or fields.get('parent_id', {}).get('actor') == self.owner_actor):
                    pending.append(item['parent_id'])
            return basis

    def work_resolution_current(self, item_id):
        item = self.get_item(item_id)
        if not item or item['status'] in {'done', 'withdrawn'}:
            return True
        assessments = self.assessments(item_id)
        if not assessments:
            return False
        assessment = assessments[-1]
        if assessment.get('material_id'):
            material = next((m for m in self.materials(item_id) if m['id'] == assessment['material_id']
                and m['version'] == assessment.get('material_version')), None)
            if not material or not material['valid']:
                return False
        if 'resolution_basis' in assessment:
            return (assessment['resolution_basis'] == self.work_input_basis(item_id)
                    and assessment.get('material_basis', []) == self._raw_materials(item_id))
        # Historical receipts retain their explicit evidence, not inferred freshness.
        sources = self.work_input_basis(item_id)
        for sid, basis in sources.items():
            if basis is None:
                return False
            if sid == item_id and any(v.get('version', 0) > assessment.get('item_version', 0)
                                     for v in basis['human'].values()):
                return False
            if self._basis(sid)['source_revision'] and assessment.get('source_versions', {}).get(sid) != self._basis(sid)['source_revision']:
                return False
            if sid != item_id:
                changes = self.store.db.execute('SELECT after_patch FROM operations WHERE item_id=? AND actor=? AND created_at>?',
                    (sid, self.owner_actor, assessment.get('assessed_at', ''))).fetchall()
                if any((self.MEANING | {'text', 'source'}).intersection(json.loads(row[0] or '{}')) for row in changes):
                    return False
        return not any(m.get('created_at', '') > assessment.get('assessed_at', '') for m in self._raw_materials(item_id))

    def external_source_coverage(self):
        from .source_monitor import coverage
        return coverage(self)

    def review_state(self):
        with self.store.lock:
            items = self.query()
            open_items = [i for i in items if i["status"] not in {"done", "withdrawn"}]
            stamp = self._instant(now())
            available = {i["id"] for i in self.query({"available": True})
                if not i.get("decision_needed") and (not i.get("starts_at") or self._instant(i["starts_at"]) <= stamp)}
            gaps, invalid = [], []
            for item in open_items:
                if item["kind"] == "project" and item.get("commitment") == "committed":
                    children = [c for c in open_items if c.get("project_id") == item["id"] or c.get("parent_id") == item["id"]]
                    committed = [c for c in children if c.get("commitment") == "committed"]
                    future = lambda child: any(child.get(k) and self._instant(child[k]) > stamp for k in ("starts_at", "review_at"))
                    waiting = lambda child: child["kind"] == "waiting" and bool(child.get("waiting_for")) and child["status"] in {"active", "waiting"}
                    if not any(c["id"] in available or waiting(c) or future(c) for c in committed):
                        due = any(any(c.get(k) and self._instant(c[k]) <= stamp for k in ("starts_at", "review_at")) for c in committed)
                        gaps.append({"item_id": item["id"], "reason": "due_return" if due else "project_without_advance"})
                if item["kind"] == "responsibility":
                    if not item.get("completion_criteria"):
                        gaps.append({"item_id": item["id"], "reason": "responsibility_standard_missing"})
                    if not any(c.get("responsibility_id") == item["id"] or c.get("parent_id") == item["id"] for c in open_items):
                        gaps.append({"item_id": item["id"], "reason": "responsibility_without_followup"})
                latest = {}
                for material in self.materials(item["id"]):
                    latest[material["id"]] = material
                invalid.extend({"item_id": item["id"], "material_id": m["id"], "reasons": m["invalid_reasons"]} for m in latest.values() if not m["valid"])
            continuations = self._meta("execution:orchestration", {}).get("continuations", {})
            operational = [{"item_id": c["item_id"], "continuation_id": key,
                "reason": "continuation_without_resolution" if c.get("exhausted") else "authorized_work_without_resolution",
                "status": c["status"], "blocker": c.get("blocker")}
                for key, c in continuations.items() if c["status"] in {"pending", "blocked"}
                and c.get('blocker') != 'explicit_return'
                and not self.work_resolution_current(c["item_id"])]
            decisions = [i for i in open_items if i.get("decision_needed")]
            external = self.external_source_coverage()
            attention = self._meta("attention", {"paused": False, "notify": True})
            return {"views": {kind: [i["id"] for i in open_items if i["kind"] == kind] for kind in sorted(KINDS)},
                "gaps": gaps, "invalid_materials": invalid, "operational_gaps": operational, "human_decisions": decisions,
                "paused_items": [i["id"] for i in open_items if i["status"] in {"paused", "postponed"}],
                "returns": [{"item_id": i["id"], "review_at": i.get("review_at"), "decision_at": i.get("decision_at"), "due_at": i.get("due_at")} for i in open_items if i.get("review_at") or i.get("decision_at") or i.get("due_at")],
                "attention": attention, "last_review": self._meta("last_review"),
                "external_sources": external["sources"], "external_sources_current": external["external_sources_current"],
                "external_sources_applicable": external["external_sources_applicable"], "configured_source_count": external["configured_count"],
                "source_coverage": [{"item_id": i["id"], "coverage": i.get("coverage")} for i in items if i.get("source")],
                "notification_allowed": bool(attention.get("notify", True) and not attention.get("paused", False) and (decisions or gaps or invalid or operational or external["external_sources_current"] is False))}

    def _review(self, actor, command, digest):
        if self.actor_role(actor) not in {"owner", "principal"}:
            raise ValueError("principal_required")
        fields = command.get("fields", {})
        if set(fields) - {"views", "source_coverage", "return_at"}:
            raise ValueError("invalid_review")
        state = self.review_state()
        views = fields.get("views", list(state["views"]))
        if not isinstance(views, list) or set(views) - set(KINDS):
            raise ValueError("invalid_review_views")
        coverage = fields.get("source_coverage", {})
        if not isinstance(coverage, dict):
            raise ValueError("invalid_source_coverage")
        required_sources = {entry["item_id"] for entry in state["source_coverage"]}
        missing = sorted(sid for sid in required_sources if coverage.get(sid) != self._basis(sid)["source_revision"])
        validate_date(fields.get("return_at"))
        review = {"reviewed_at": now(), "actor": actor, "views": views, "source_coverage": coverage,
            "missing_sources": missing, "missing_views": sorted(set(KINDS) - set(views)),
            "operational_complete": not missing and set(views) == set(KINDS),
            "external_sources_current": state["external_sources_current"], "external_sources": state["external_sources"],
            "external_sources_applicable": state["external_sources_applicable"],
            "human_decision_pending": bool(state["human_decisions"]), "gaps": state["gaps"],
            "invalid_materials": state["invalid_materials"], "operational_gaps": state["operational_gaps"], "return_at": fields.get("return_at"),
            "limits": ["Only recorded sources and declared coverage were checked; human perspective is not inferred."]}
        self._set_meta("last_review", review)
        if review["operational_complete"]:
            # Global coverage does not discharge an executor delivery. Its own
            # admission/run owns that event, including pending or failed review.
            events = self.store.db.execute("SELECT event_key,payload FROM events WHERE provider='gtd-review' AND account='local'").fetchall()
            self.store.db.executemany("UPDATE events SET status='done' WHERE event_key=?",
                [(event['event_key'],) for event in events
                 if json.loads(event['payload']).get('reason') != 'executor_return'])
        return self._record(actor, command["operation_id"], digest,
            {"operation_id": command["operation_id"], "status": "applied", "review": review})
