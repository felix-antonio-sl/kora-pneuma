"""Synthetic durable execution acceptance against real SQLite and domain."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import tempfile
import unittest

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from gtd_felix import GTDService
from gtd_felix.control import ExecutionControl


class ControlTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.service = GTDService(self.root / "data")
        self.config = dict(period_start=datetime.now(timezone.utc).isoformat(), period_seconds=3600,
                           max_cost_usd=10, max_runtime_seconds=1000, recovery_cost_usd=2,
                           recovery_runtime_seconds=100, max_active=2, max_job_runtime_seconds=500,
                           max_retries=1, max_descendants=2)
        self.control = ExecutionControl(self.service, self.config)
        self.item = self.service.capture("felix", "capture", "Synthetic project")["item"]
        receipt = self.service.execute("felix", dict(operation_id="clarify", action="clarify", item_id=self.item["id"], expected_version=self.item["version"], fields={"kind": "project", "commitment": "committed", "outcome": "Synthetic output", "completion_criteria": "Verified output"}))
        self.assertEqual(receipt["status"], "applied", receipt)
        self.item = receipt["item"]
        receipt = self.service.execute("felix", dict(operation_id="mandate", action="grant_mandate", item_id=self.item["id"], expected_version=self.item["version"], fields={"scope_item_id": self.item["id"], "capabilities": ["local_work"], "actors": ["gtd-felix"], "completion_criteria": "Verified output"}))
        self.assertEqual(receipt["status"], "applied", receipt)
        self.item = receipt["item"]
        self.mandate = receipt["mandate"]["id"]
        self.bot = dict(id="test-bot", state="available", source_urn="urn:test:bot", host="synthetic", profile="fixture", capabilities=["local_work"], mandate_id=self.mandate, item_id=self.item["id"], probe_evidence="fixture://probe")
        self.assertEqual(self.control.register_bot("felix", "bot", self.bot)["status"], "applied")

    def tearDown(self):
        self.service.close()
        self.temp.cleanup()

    def request(self, **changes):
        request = dict(item_id=self.item["id"], expected_version=self.item["version"], mandate_id=self.mandate,
                       capability="local_work", bot_id="test-bot", purpose="Prepare", scope="Synthetic private work",
                       max_cost_usd=4, max_runtime_seconds=200, max_retries=0, max_descendants=2)
        return dict(request, **changes)

    def reserve(self, operation="reserve", **changes):
        receipt = self.control.reserve("gtd-felix", operation, self.request(**changes))
        self.assertEqual(receipt["status"], "reserved", receipt)
        return receipt["job_id"]

    def native(self, job):
        return dict(provider="fixture", host="synthetic", profile="fixture", id=job)

    def observation(self, job, **changes):
        return dict(dict(native_identity=self.native(job), native_status="completed", terminal=True,
                         cost_usd=1, runtime_seconds=30, evidence_reference="fixture://terminal"), **changes)

    def finish(self, job, **changes):
        result = self.control.observe(job, self.observation(job, **changes))
        self.assertEqual(result["status"], "recorded", result)
        return result

    def test_job_history_excludes_siblings_source_parent_and_lateral_project(self):
        def derive(parent, operation):
            return self.service.execute('felix', dict(operation_id=operation, action='derive',
                item_id=parent['id'], expected_version=parent['version'], fields={'kind': 'action',
                'title': operation, 'capability': 'local_work', 'mandate_id': self.mandate}))['item']
        child, sibling = derive(self.item, 'history-child'), derive(self.item, 'history-sibling')
        root_job = self.reserve('history-root')
        self.finish(root_job, native_status='cancelled')
        sibling_job = self.reserve('history-sibling-job', item_id=sibling['id'], expected_version=sibling['version'])
        self.finish(sibling_job, native_status='cancelled')
        caller = self.reserve('history-caller', item_id=child['id'], expected_version=child['version'])
        lateral = self.service.capture('felix', 'history-lateral', 'Not in child scope')['item']
        linked = self.service.execute('felix', dict(operation_id='history-lateral-link', action='edit',
            item_id=lateral['id'], expected_version=lateral['version'], fields={'project_id': self.item['id']}))
        self.assertEqual(linked['status'], 'applied')
        before = self.control._load()
        self.assertEqual([job['id'] for job in self.control.job_history('gtd-felix', caller)], [caller])
        for item_id in (self.item['id'], sibling['id'], lateral['id']):
            self.assertEqual(self.control.job_history('gtd-felix', caller, item_id)['error'], 'outside_job_scope')
        for actor, job_id in (('worker', caller), ('gtd-felix', None), ('gtd-felix', 'missing')):
            self.assertEqual(self.control.job_history(actor, job_id)['status'], 'rejected')
        self.assertEqual(self.control._load(), before)
        self.control.request_stop('felix', 'history-caller-stop', caller)
        self.assertEqual(self.control.job_history('gtd-felix', caller)['error'], 'stop_requested')

    def test_job_history_distinguishes_administrative_terminal_without_native_observation(self):
        root, child = self.deferred_contribution()
        self.control.request_stop('felix', 'history-cancel-deferred', child)
        history = self.control.job_history('gtd-felix', root)
        summary = next(job for job in history if job['id'] == child)
        self.assertTrue(summary['terminal'])
        self.assertEqual(summary['terminal_resolution']['kind'], 'cancelled_before_dispatch')
        self.assertIsNone(summary['native'])
        self.assertIsNone(summary['last_observation'])
        self.assertEqual(summary['charged_cost_usd'], 0)

    def test_terminal_discard_requires_obsolete_evidence_and_preserves_job(self):
        job = self.reserve()
        self.assertEqual(self.control.discard_obsolete_terminal(job)['error'], 'terminal_success_required')
        self.finish(job)
        self.assertEqual(self.control.discard_obsolete_terminal(job)['error'], 'obsolescence_not_verified')
        before = self.control.get_job(job)
        changed = self.service.execute('felix', dict(operation_id='obsolete-root', action='edit',
            item_id=self.item['id'], expected_version=self.item['version'], fields={'text': 'Corrected human source'}))
        self.assertEqual(changed['status'], 'applied')
        with self.service.store.transaction():
            self.service.store.db.execute("INSERT OR REPLACE INTO metadata VALUES('recovery_required', 'true')")
        self.assertEqual(self.control.discard_obsolete_terminal(job)['error'], 'recovery_required')
        self.assertEqual(self.control.get_job(job), before)
        with self.service.store.transaction():
            self.service.store.db.execute("DELETE FROM metadata WHERE key='recovery_required'")
        result = self.control.discard_obsolete_terminal(job)
        self.assertEqual(result['status'], 'discarded')
        self.assertEqual(result['job']['integration_error'], 'stale_item_version')
        self.assertEqual({k: v for k, v in result['job'].items() if k not in {'integration', 'integration_error'}},
                         {k: v for k, v in before.items() if k != 'integration'})
        self.assertEqual(self.control.discard_obsolete_terminal(job), result)
        self.assertNotIn(job, [j['id'] for j in self.control.pending()])

    def test_restore_reconcile_requires_external_effect_resolution(self):
        from datetime import timedelta
        from gtd_felix.effects import ExternalEffects
        for outcome in ('confirmed', 'conflict'):
            with self.subTest(outcome=outcome):
                job = self.reserve('external-job-' + outcome)
                self.finish(job)
                effects = ExternalEffects(self.service)
                proposal = {'provider': 'calendar', 'account': 'synthetic', 'action': 'update',
                    'item_id': self.item['id'], 'target': {'id': 'event'}, 'payload': {'summary': 'approved'},
                    'expected_remote_version': '"before"',
                    'expires_at': (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat()}
                effect = effects.propose('gtd-felix', 'external-' + outcome, proposal)['effect']
                effects.authorize('felix', 'authorize-external-' + outcome, effect['id'], effect['proposal_hash'])
                dispatch = effects.begin_dispatch(effect['id'])['effect']['dispatch']
                archive = self.root / (outcome + '.zip')
                self.service.export(archive)
                restored = GTDService.restore(archive, self.root / ('restore-' + outcome))
                try:
                    control = ExecutionControl(restored, self.config)
                    self.assertEqual(control.reconcile('felix', 'blocked', [])['error'], 'unresolved_external_effects')
                    self.assertTrue(restored.recovery_required)
                    self.assertEqual(control.reconcile('gtd-felix', 'cannot-clear', [])['error'], 'owner_required')
                    adapter = ExternalEffects(restored)
                    envelope = {k: proposal[k] for k in ('provider', 'account', 'action', 'target')}
                    envelope.update(request_hash=effect['proposal_hash'])
                    if outcome == 'confirmed':
                        adapter.observe(effect['id'], {**envelope, 'status': 'ack', 'remote_id': 'event', 'evidence_reference': 'fixture://ack'})
                        result = adapter.observe(effect['id'], {**envelope, 'status': 'confirmed', 'remote_id': 'event',
                            'evidence_reference': 'fixture://readback', 'readback': {**envelope, 'remote_id': 'event', 'content_verified': True}})
                    else:
                        result = adapter.observe(effect['id'], {**envelope, 'status': 'conflict', 'evidence_reference': 'fixture://412',
                            'proof': {'kind': 'conditional_write_rejected', 'http_status': 412,
                                      'dispatch_id': dispatch['id'], 'expected_remote_version': '"before"'}})
                    self.assertEqual(result['status'], outcome, result)
                    self.assertEqual(control.reconcile('felix', 'resolved', [])['status'], 'reconciled')
                    self.assertFalse(restored.recovery_required)
                finally:
                    restored.close()
                # Resolve original synthetic pending state for the next independent case.
                effects.observe(effect['id'], {**envelope, 'status': 'no_dispatch', 'evidence_reference': 'fixture://not-sent',
                    'proof': {'kind': 'request_not_sent', 'dispatch_id': dispatch['id']}})

    def test_restart_between_intent_and_native_response_never_recreates_job(self):
        job = self.reserve()
        self.service.close()
        self.service = GTDService(self.root / "data")
        self.control = ExecutionControl(self.service, self.config)
        repeat = self.control.reserve("gtd-felix", "reserve", self.request())
        self.assertEqual(repeat["job_id"], job)
        self.assertTrue(repeat["duplicate"])
        self.assertEqual(self.control.pending()[0]["delivery"], "intent")
        self.assertEqual(self.control.budget()["committed_cost_usd"], 4)
        self.assertEqual(self.control.record_dispatch(job, self.native(job))["status"], "recorded")
        self.assertEqual(self.control.budget()["active"], 1)

    def deferred_contribution(self, prior_material=False):
        grant = self.service.execute('felix', dict(operation_id='coordination-mandate', action='grant_mandate',
            item_id=self.item['id'], expected_version=self.item['version'], fields={
                'scope_item_id':self.item['id'], 'capabilities':['local_work','prepare_private'],
                'actors':['gtd-felix'], 'completion_criteria':'Verified output'}))
        self.item, self.mandate = grant['item'], grant['mandate']['id']
        self.config['max_active'] = 1
        self.control = ExecutionControl(self.service, self.config)
        root = self.reserve()
        result = self.service.execute('gtd-felix', dict(operation_id='derive-contribution', action='derive',
            item_id=self.item['id'], expected_version=self.item['version'], fields={'kind':'action',
            'title':'Prepare guide', 'capability':'local_work', 'mandate_id':self.mandate,
            'executor':'gtd-felix', 'completion_criteria':'Guide checked'}))
        self.assertEqual(result['status'], 'applied', result)
        self.assertEqual(self.control.record_progress(root, result, self.item['version'])['status'], 'recorded')
        if prior_material:
            material = self.service.execute('gtd-felix', dict(operation_id='pre-reservation-material', action='put_material',
                item_id=result['item']['id'], expected_version=result['item']['version'],
                fields={'content': 'Already known preparation', 'mandate_id': self.mandate}))
            self.assertEqual(material['status'], 'applied', material)
            self.assertEqual(self.control.record_progress(root, material, result['item']['version'])['status'], 'recorded')
            result = material
        child = self.reserve('child-contribution', item_id=result['item']['id'], expected_version=result['item']['version'],
            parent_job_id=root, defer_when_busy=True, max_cost_usd=1, max_runtime_seconds=50, max_descendants=0)
        return root, child

    def test_deferred_child_survives_authenticated_parent_assessment_and_plan(self):
        root, child = self.deferred_contribution()
        for operation, action, fields in [('parent-draft','put_material',{'content':'Parent working note'}),
                ('parent-gap','assess_result',{'satisfied':False,
                'evidence':'Child guide pending', 'gap':'Await reserved contribution', 'mandate_id':self.mandate}),
                ('parent-plan','plan',{'plan_steps':['Integrate child guide'], 'uncertainties':['Pending contribution']})]:
            item = self.service.get_item(self.item['id'])
            receipt = self.service.execute('gtd-felix', dict(operation_id=operation, action=action,
                item_id=item['id'], expected_version=item['version'], fields=fields))
            self.assertEqual(receipt['status'], 'applied', receipt)
            self.assertEqual(self.control.record_progress(root, receipt, item['version'])['status'], 'recorded')
        self.finish(root)
        self.assertEqual(self.control.activate_deferred(child)['status'], 'activated')
        self.assertTrue(self.control.validate(child, 'local_work')['allowed'])
        self.finish(child)
        self.assertEqual(self.control.discard_obsolete_terminal(child)['error'], 'obsolescence_not_verified')
        self.assertEqual(self.control.accept_result('gtd-felix','accept-compatible-child',child,
            {'criteria_met':True,'evidence_reference':'fixture://checked','artifact_reference':'fixture://guide'})['status'], 'accepted')

    def assess_reserved_child(self, root, child, *, actor='gtd-felix', satisfied=False, authenticate=True):
        item = self.service.get_item(self.control.get_job(child)['item_id'])
        receipt = self.service.execute(actor, dict(operation_id='child-gap-' + str(item['version']), action='assess_result',
            item_id=item['id'], expected_version=item['version'], fields={'satisfied': satisfied,
                'evidence': 'Reserved contribution has not returned', 'gap': 'Await same reserved child',
                'mandate_id': self.mandate}))
        self.assertEqual(receipt['status'], 'applied', receipt)
        if authenticate:
            self.assertEqual(self.control.record_progress(root, receipt, item['version'])['status'], 'recorded')
        return receipt

    def test_same_child_parent_assessment_preserves_reservation_through_integration(self):
        root, child = self.deferred_contribution()
        original = self.control.get_job(child)['item_bases']
        self.assess_reserved_child(root, child)
        self.finish(root)
        self.assertEqual(self.control.activate_deferred(child)['status'], 'activated')
        self.finish(child)
        self.assertEqual(self.control.discard_obsolete_terminal(child)['error'], 'obsolescence_not_verified')
        accepted = self.control.accept_result('gtd-felix', 'same-child-accept', child,
            {'criteria_met': True, 'evidence_reference': 'fixture://checked', 'artifact_reference': 'fixture://guide'})
        self.assertEqual(accepted['status'], 'accepted', accepted)
        item = self.service.get_item(self.control.get_job(child)['item_id'])
        material = self.service.execute('gtd-felix', dict(operation_id='same-child-material', action='put_material',
            item_id=item['id'], expected_version=item['version'], fields={'content': 'Verified contribution', 'mandate_id': self.mandate}))
        self.assertEqual(material['status'], 'applied', material)
        self.assertEqual(self.control.record_integration(child, material)['status'], 'integrated')
        self.assertEqual(self.control.get_job(child)['item_bases'], original)
        self.assertEqual(self.service.store.db.execute('SELECT COUNT(*) FROM runs').fetchone()[0], 2)

    def test_same_child_coordination_preserves_material_present_at_reservation(self):
        root, child = self.deferred_contribution(prior_material=True)
        job = self.control.get_job(child)
        self.assertGreater(job['expected_version'], max(job['item_bases'][job['item_id']]['generations'].values()))
        self.assess_reserved_child(root, child)
        self.finish(root)
        self.assertEqual(self.control.activate_deferred(child)['status'], 'activated')
        self.assertEqual(self.control.get_job(child)['item_bases'], job['item_bases'])

    def reject_same_child_change(self, change):
        root, child = self.deferred_contribution()
        original = self.control.get_job(child)['item_bases']
        if change == 'unauthenticated':
            self.assess_reserved_child(root, child, authenticate=False)
        elif change == 'other_parent':
            self.finish(root)
            other = self.reserve('other-coordinator', max_cost_usd=2)
            self.assess_reserved_child(other, child)
            self.finish(other)
        elif change == 'true':
            self.assess_reserved_child(root, child, satisfied=True)
        else:
            if change == 'human_then_parent':
                self.assess_reserved_child(root, child, actor='felix', authenticate=False)
            assessment = self.assess_reserved_child(root, child, authenticate=change != 'human_then_parent')
            item = self.service.get_item(self.control.get_job(child)['item_id'])
            if change in {'criterion', 'source', 'status', 'material', 'undo'}:
                action, fields = {
                    'criterion': ('edit', {'completion_criteria': 'Different operational criterion'}),
                    'source': ('edit', {'text': 'Human corrected source'}),
                    'status': ('withdraw', {}),
                    'undo': ('undo', {'operation_id': assessment['operation_id']}),
                    'material': ('put_material', {'content': 'Other material', 'mandate_id': self.mandate})}[change]
                actor = 'felix' if change in {'source', 'status', 'undo'} else 'gtd-felix'
                receipt = self.service.execute(actor, dict(operation_id='material-change', action=action,
                    item_id=item['id'], expected_version=item['version'], fields=fields))
                self.assertEqual(receipt['status'], 'applied', receipt)
                if actor == 'gtd-felix':
                    self.assertEqual(self.control.record_progress(root, receipt, item['version'])['status'], 'recorded')
        if not self.control.get_job(root)['terminal']:
            self.finish(root)
        result = self.control.activate_deferred(child)
        self.assertEqual(result['status'], 'discarded', result)
        self.assertEqual(result['job']['integration_error'], 'stale_item_version')
        self.assertEqual(result['job']['item_bases'], original)
        self.assertIsNone(result['job']['native'])

    def test_same_child_coordination_rejects_changed_criterion(self):
        self.reject_same_child_change('criterion')

    def test_same_child_coordination_rejects_human_source(self):
        self.reject_same_child_change('source')

    def test_same_child_coordination_rejects_status(self):
        self.reject_same_child_change('status')

    def test_same_child_coordination_rejects_true_assessment(self):
        self.reject_same_child_change('true')

    def test_same_child_coordination_rejects_missing_progress(self):
        self.reject_same_child_change('unauthenticated')

    def test_same_child_coordination_rejects_other_principal_job(self):
        self.reject_same_child_change('other_parent')

    def test_same_child_coordination_rejects_intermediate_human(self):
        self.reject_same_child_change('human_then_parent')

    def test_same_child_coordination_rejects_removed_assessment(self):
        self.reject_same_child_change('undo')

    def test_same_child_coordination_rejects_other_material(self):
        self.reject_same_child_change('material')

    def test_parent_coordination_without_authentic_progress_is_not_compatible(self):
        root, child = self.deferred_contribution()
        item = self.service.get_item(self.item['id'])
        receipt = self.service.execute('gtd-felix', dict(operation_id='unacknowledged-plan', action='plan',
            item_id=item['id'], expected_version=item['version'], fields={'plan_steps':['Changed coordination']}))
        self.assertEqual(receipt['status'],'applied')
        self.assertEqual(self.control.validate(child,'local_work')['reason'],'source_version_stale')

    def test_human_coordination_never_becomes_compatible_agent_progress(self):
        root, child = self.deferred_contribution()
        item = self.service.get_item(self.item['id'])
        receipt = self.service.execute('felix', dict(operation_id='human-plan', action='edit',
            item_id=item['id'], expected_version=item['version'], fields={'plan_steps':['Human requirement']}))
        self.assertEqual(receipt['status'],'applied')
        self.assertEqual(self.control.validate(child,'local_work')['reason'],'source_version_stale')

    def test_parent_plan_on_child_is_compatible_without_replacing_reserved_basis(self):
        root, child = self.deferred_contribution()
        original = self.control.get_job(child)['item_bases']
        item = self.service.get_item(self.control.get_job(child)['item_id'])
        receipt = self.service.execute('gtd-felix', dict(operation_id='child-plan', action='plan',
            item_id=item['id'], expected_version=item['version'], fields={'plan_steps':['Changed child task']}))
        self.assertEqual(receipt['status'],'applied')
        self.assertEqual(self.control.record_progress(root,receipt,item['version'])['status'],'recorded')
        self.finish(root)
        self.assertEqual(self.control.activate_deferred(child)['status'], 'activated')
        self.assertEqual(self.control.get_job(child)['item_bases'], original)
        self.assertEqual(self.service.get_item(item['id'])['completion_criteria'], item['completion_criteria'])

    def test_intermediate_human_coordination_is_not_erased_by_later_principal(self):
        root, child = self.deferred_contribution()
        self.finish(root)
        item = self.service.get_item(self.item['id'])
        human = self.service.execute('felix', dict(operation_id='human-intermediate-plan', action='edit',
            item_id=item['id'], expected_version=item['version'], fields={'plan_steps':['Human constraint']}))
        self.item = human['item']
        other = self.reserve('another-principal', max_cost_usd=2)
        own = self.service.execute('gtd-felix', dict(operation_id='later-own-plan', action='plan',
            item_id=self.item['id'], expected_version=self.item['version'], fields={'plan_steps':['Integrate guide']}))
        self.assertEqual(own['status'],'applied')
        self.assertEqual(self.control.record_progress(other,own,self.item['version'])['status'],'recorded')
        self.assertEqual(self.control.validate(child,'local_work')['reason'],'source_version_stale')

    def test_deferred_invalid_never_dispatched_closes_once_without_native_evidence(self):
        root, child = self.deferred_contribution()
        item = self.service.get_item(self.item['id'])
        self.service.execute('felix', dict(operation_id='correct-parent', action='edit', item_id=item['id'],
            expected_version=item['version'], fields={'text':'Changed source'}))
        result = self.control.activate_deferred(child)
        self.assertEqual(result['status'], 'discarded')
        job = self.control.get_job(child)
        self.assertTrue(job['terminal']); self.assertIsNone(job['native'])
        self.assertEqual(job['observations'], [])
        self.assertEqual(job['charged_cost_usd'], 0)
        self.assertEqual(job['integration_error'], 'source_version_stale')
        self.assertEqual(job['terminal_resolution']['parent_job_id'], root)
        self.assertEqual(self.control.activate_deferred(child), result)
        self.assertNotIn(child, [j['id'] for j in self.control.pending()])

    def test_deferred_stop_and_uncertain_dispatch_are_distinct(self):
        root, child = self.deferred_contribution()
        with self.service.store.transaction():
            self.service.store.db.execute('INSERT INTO metadata VALUES(?,?)', ('hermes:intent:'+child,'{}'))
        self.control.request_stop('felix','stop-child',child)
        self.assertEqual(self.control.activate_deferred(child)['status'], 'rejected')
        self.assertFalse(self.control.get_job(child)['terminal'])
        with self.service.store.transaction():
            self.service.store.db.execute('DELETE FROM metadata WHERE key=?', ('hermes:intent:'+child,))
        self.assertEqual(self.control.activate_deferred(child)['status'], 'discarded')
        self.assertEqual(self.control.get_job(child)['integration_error'], 'stop_requested')

    def test_open_cycle_collision_returns_rejection_not_raw_error(self):
        # A second admission for a matter with an open cycle must be a
        # contained purpose_already_active rejection: the raw sqlite error
        # used to escape reserve and silently stall every orchestration tick.
        first = self.reserve('first-open')
        receipt = self.control.reserve('gtd-felix', 'second-open', self.request())
        self.assertEqual(receipt['status'], 'rejected', receipt)
        self.assertEqual(receipt['error'], 'purpose_already_active')

    def test_direct_stop_closes_pristine_intent_without_worker_or_native(self):
        # A manager-stopped intent reservation with no native run, spend,
        # observations or progress must reach terminality within the period;
        # otherwise the single global slot wedges with no worker able to
        # advance it (bare admission has no orchestration run).
        job_id = self.reserve('stop-intent')
        result = self.control.request_stop('felix', 'direct-stop-intent', job_id)
        self.assertTrue(result['job']['terminal'])
        self.assertEqual(result['job']['terminal_resolution']['kind'], 'cancelled_before_dispatch')
        self.assertIsNone(result['job']['native'])
        self.assertEqual(result['job']['observations'], [])
        self.assertEqual(result['job']['charged_cost_usd'], 0)
        self.assertEqual(result['job']['integration'], 'discarded')
        self.assertEqual(self.control.request_stop('felix', 'direct-stop-intent', job_id)['job'], result['job'])
        self.assertNotIn(job_id, [j['id'] for j in self.control.pending()])
        cycle = self.service.store.db.execute(
            'SELECT state FROM work_cycles WHERE id=(SELECT cycle_id FROM runs WHERE id=?)',
            (job_id,)).fetchone()
        self.assertEqual(cycle['state'], 'abandoned')

    def test_restop_heals_cycle_orphaned_by_older_code(self):
        job_id = self.reserve('stop-intent-orphan')
        self.control.request_stop('felix', 'direct-stop-orphan', job_id)
        with self.service.store.transaction():
            self.service.store.db.execute(
                "UPDATE work_cycles SET state='running', closed_at=NULL WHERE id="
                "(SELECT cycle_id FROM runs WHERE id=?)", (job_id,))
        result = self.control.request_stop('felix', 'direct-stop-orphan-again', job_id)
        self.assertTrue(result['job']['terminal'])
        cycle = self.service.store.db.execute(
            'SELECT state FROM work_cycles WHERE id=(SELECT cycle_id FROM runs WHERE id=?)',
            (job_id,)).fetchone()
        self.assertEqual(cycle['state'], 'abandoned')

    def test_direct_stop_closes_deferred_without_worker_or_native(self):
        root, child = self.deferred_contribution()
        result = self.control.request_stop('felix','direct-stop',child)
        self.assertTrue(result['job']['terminal'])
        self.assertEqual(result['job']['terminal_resolution']['kind'], 'cancelled_before_dispatch')
        self.assertEqual(self.control.request_stop('felix','direct-stop',child)['job'], result['job'])
        self.assertEqual(self.control.get_job(child)['observations'], [])
        self.assertEqual(self.control.get_job(child)['charged_cost_usd'], 0)
        self.assertEqual(self.service.store.db.execute('SELECT COUNT(*) FROM runs').fetchone()[0], 2)

    def test_deferred_transient_and_uncertain_run_do_not_release_reservation(self):
        root, child = self.deferred_contribution()
        budget = self.control.budget()
        self.assertEqual(self.control.activate_deferred(child)['error'], 'concurrency_exhausted')
        with self.service.store.transaction():
            self.service.store.db.execute("INSERT INTO metadata VALUES('recovery_required','true')")
        self.control.request_stop('felix','stop-during-recovery',child)
        self.assertEqual(self.control.activate_deferred(child)['error'], 'recovery_required')
        self.assertFalse(self.control.get_job(child)['terminal'])
        with self.service.store.transaction():
            self.service.store.db.execute("DELETE FROM metadata WHERE key='recovery_required'")
            self.service.store.db.execute('INSERT INTO metadata VALUES(?,?)', ('execution:orchestration',
                json.dumps({'runs':{child:{'phase':'submitting'}}})))
        self.assertEqual(self.control.activate_deferred(child)['status'], 'rejected')
        self.assertFalse(self.control.get_job(child)['terminal'])
        self.assertEqual(self.control.budget(), budget)

    def test_idempotency_conflict_and_atomic_concurrent_admission(self):
        self.reserve()
        conflict = self.control.reserve("gtd-felix", "reserve", self.request(scope="Other"))
        self.assertEqual(conflict["error"], "idempotency_conflict")
        # I1: one open cycle per item, so concurrent admissions race on distinct
        # derived items for the last global slot (max_active=2).
        derived = []
        for n in range(2):
            derived.append(self.service.execute('felix', dict(operation_id=f'concurrent-derive-{n}', action='derive',
                item_id=self.item['id'], expected_version=self.service.get_item(self.item['id'])['version'],
                fields={'kind': 'action', 'title': f'concurrent-{n}', 'capability': 'local_work',
                        'mandate_id': self.mandate}))['item'])
        with ThreadPoolExecutor(2) as pool:
            results = list(pool.map(lambda n: self.control.reserve("gtd-felix", f"concurrent{n}",
                self.request(item_id=derived[n]['id'], expected_version=derived[n]['version'], purpose=f"purpose{n}")), range(2)))
        self.assertEqual(sum(r["status"] == "reserved" for r in results), 1)
        self.assertEqual(self.control.budget()["active"], 2)
        self.assertEqual(self.control.budget()["remaining_cost_usd"], 0)

    def test_recovery_reserve_is_not_ordinary_budget(self):
        receipt = self.control.reserve("gtd-felix", "expensive", self.request(max_cost_usd=9))
        self.assertEqual(receipt["error"], "budget_exhausted")
        self.assertEqual(self.control.budget()["recovery_cost_usd"], 2)
        disabled = ExecutionControl(self.service, {})
        self.assertEqual(disabled.reserve("gtd-felix", "disabled", self.request())["error"], "execution_disabled")

    def test_no_budget_renewal_by_reconstructing_control(self):
        self.reserve()
        changed = ExecutionControl(self.service, dict(self.config, max_cost_usd=100))
        self.assertEqual(changed.reserve("gtd-felix", "renew", self.request(purpose="other"))["error"], "budget_configuration_changed")

    def test_unknown_cost_charges_max_and_duplicate_observation_does_not_add(self):
        job = self.reserve()
        observation = self.observation(job, cost_usd=None)
        self.control.observe(job, observation)
        self.assertTrue(self.control.observe(job, observation)["duplicate"])
        self.assertEqual(self.control.budget()["committed_cost_usd"], 4)
        self.assertIsNone(self.control.get_job(job)["observations"][-1]["cost_usd"])

    def test_timeout_and_stop_are_not_terminal(self):
        job = self.reserve()
        self.finish(job, native_status="uncertain", terminal=False, cost_usd=None)
        self.assertEqual(self.control.request_stop("felix", "stop", job)["status"], "stop_requested")
        self.assertFalse(self.control.get_job(job)["terminal"])
        self.assertEqual(self.control.budget()["active"], 1)
        self.assertEqual(self.control.budget()["committed_cost_usd"], 4)
        self.assertFalse(self.control.validate(job, "local_work")["allowed"])
        self.finish(job, native_status="cancelled")
        self.assertEqual(self.control.budget()["active"], 0)

    def test_material_correction_prevents_old_output_acceptance(self):
        job = self.reserve()
        result = self.service.execute("felix", dict(operation_id="human-edit", action="edit", item_id=self.item["id"], expected_version=self.item["version"], fields={"title": "Corrected purpose"}))
        self.assertEqual(result["status"], "applied", result)
        self.assertEqual(self.control.validate(job, "local_work")["reason"], "stale_item_version")
        self.finish(job)
        result = self.control.accept_result("gtd-felix", "accept-old", job, dict(evidence_reference="fixture://e", artifact_reference="fixture://a", criteria_met=True))
        self.assertEqual(result["error"], "stale_item_version")
        self.assertEqual(self.service.get_item(self.item["id"])["title"], "Corrected purpose")
        self.assertNotEqual(self.control.get_job(job)["integration"], "integrated")

    def test_revoked_mandate_blocks_even_without_version_drift(self):
        job = self.reserve()
        with self.service.store.transaction() as db:
            key = "mandate:" + self.mandate
            mandate = json.loads(db.execute("SELECT value FROM metadata WHERE key=?", (key,)).fetchone()[0])
            mandate["status"] = "revoked"
            db.execute("UPDATE metadata SET value=? WHERE key=?", (json.dumps(mandate), key))
        self.assertEqual(self.control.validate(job, "local_work")["reason"], "mandate_not_active")
        self.finish(job)
        self.assertEqual(self.control.budget()["active"], 0)

    def test_unavailable_bots_and_wrong_actors_cannot_dispatch(self):
        for state in ("planned", "incorporated", "suspended", "unavailable"):
            bot = dict(self.bot, state=state)
            self.control.register_bot("felix", "bot-" + state, bot)
            self.assertEqual(self.control.reserve("gtd-felix", "request-" + state, self.request())["error"], "bot_unavailable")
        self.assertEqual(self.control.reserve("untrusted", "untrusted", self.request())["error"], "actor_not_manager")
        bot = dict(self.bot, probe_evidence="")
        self.assertEqual(self.control.register_bot("felix", "unprobed", bot)["error"], "route_probe_required")

    def test_descendants_share_parent_reserve_and_global_slots(self):
        root = self.reserve(max_cost_usd=6)
        child = self.reserve("child", parent_job_id=root, purpose="child", max_cost_usd=2, max_runtime_seconds=50)
        self.assertEqual(self.control.budget()["committed_cost_usd"], 6)
        self.assertEqual(self.control.budget()["active"], 2)
        self.assertEqual(self.control.reserve("gtd-felix", "third", self.request(parent_job_id=root, purpose="third", max_cost_usd=1))["error"], "concurrency_exhausted")
        self.finish(child, cost_usd=None)
        self.assertEqual(self.control.budget()["committed_cost_usd"], 6)
        self.finish(root, cost_usd=None)
        self.assertEqual(self.control.budget()["committed_cost_usd"], 6)
        self.assertEqual(self.control.budget()["active"], 0)

    def test_native_identity_cannot_double_count_across_jobs(self):
        first = self.reserve()
        # I1: one open cycle per item, so the second run uses a derived item
        # in the same mandate scope to test cross-run native uniqueness.
        derived = self.service.execute('felix', dict(operation_id='native-second-derive', action='derive',
            item_id=self.item['id'], expected_version=self.item['version'], fields={'kind': 'action',
            'title': 'native-second', 'capability': 'local_work', 'mandate_id': self.mandate}))['item']
        second = self.reserve("second", item_id=derived['id'], expected_version=derived['version'], purpose="second")
        self.control.record_dispatch(first, self.native(first))
        receipt = self.control.record_dispatch(second, self.native(first))
        self.assertEqual(receipt["error"], "native_identity_already_accounted")
        self.assertEqual(self.control.budget()["active"], 2)

    def test_invalid_terminal_claim_cannot_release_reservation(self):
        job = self.reserve()
        for changes in ({"native_status": "uncertain"}, {"evidence_reference": ""}, {"runtime_seconds": -1}, {"cost_usd": float("nan")}, {"native_identity": {"id": job}}):
            self.assertEqual(self.control.observe(job, self.observation(job, **changes))["status"], "rejected")
        self.assertEqual(self.control.budget()["active"], 1)
        self.assertEqual(self.control.budget()["committed_cost_usd"], 4)

    def test_restore_uncertainty_blocks_reconciliation_and_does_not_free_budget(self):
        job = self.reserve()
        archive = self.root / "backup.zip"
        self.service.export(archive)
        restored = GTDService.restore(archive, self.root / "restored")
        try:
            control = ExecutionControl(restored, self.config)
            self.assertTrue(restored.recovery_required)
            self.assertEqual(control.reconcile("gtd-felix", "wrong-owner", [])["error"], "owner_required")
            self.assertEqual(control.reconcile("felix", "no-evidence", [])["error"], "unresolved_execution")
            uncertain = dict(self.observation(job, native_status="uncertain", terminal=False), job_id=job)
            self.assertEqual(control.reconcile("felix", "uncertain", [uncertain])["error"], "unresolved_execution")
            self.assertTrue(restored.recovery_required)
            self.assertEqual(control.budget()["committed_cost_usd"], 4)
            terminal = dict(self.observation(job, native_status="cancelled"), job_id=job)
            self.assertEqual(control.reconcile("felix", "resolved", [terminal])["status"], "reconciled")
            self.assertFalse(restored.recovery_required)
            self.assertEqual(control.budget()["active"], 0)
        finally:
            restored.close()

    def test_acceptance_is_not_domain_integration_and_forgery_is_rejected(self):
        job = self.reserve()
        self.finish(job)
        result = self.control.accept_result("gtd-felix", "accept", job, dict(evidence_reference="fixture://e", artifact_reference="fixture://a", criteria_met=True))
        self.assertEqual(result["status"], "accepted", result)
        self.assertEqual(result["job"]["integration"], "accepted_pending_integration")
        self.assertEqual(self.control.record_integration(job, {"status": "applied", "operation_id": "fake"})["error"], "domain_receipt_not_verified")
        self.assertNotEqual(self.service.get_item(self.item["id"])["status"], "done")

    def test_not_found_is_uncertain_and_retains_budget(self):
        job = self.reserve()
        invalid = self.control.observe(job, self.observation(job, native_status="not_found"))
        self.assertEqual(invalid["error"], "invalid_native_status")
        self.finish(job, native_status="not_found", terminal=False)
        self.assertEqual(self.control.get_job(job)["delivery"], "uncertain")
        self.assertEqual(self.control.budget()["active"], 1)
        self.assertEqual(self.control.reconcile("felix", "missing", [])["error"], "unresolved_execution")

    def test_stop_root_also_stops_child_and_retains_family_budget(self):
        root = self.reserve(max_cost_usd=6)
        child = self.reserve("child", parent_job_id=root, purpose="child", max_cost_usd=2, max_runtime_seconds=50)
        receipt = self.control.request_stop("felix", "stop-family", root)
        self.assertEqual(set(receipt["affected_job_ids"]), {root, child})
        self.finish(root, native_status="cancelled", cost_usd=None)
        self.assertTrue(self.control.get_job(child)["stop_requested"])
        self.assertFalse(self.control.validate(child, "local_work")["allowed"])
        self.assertEqual(self.control.budget()["committed_cost_usd"], 6)
        self.assertEqual(self.control.budget()["active"], 1)

    def test_pending_telegram_output_blocks_restore_reconciliation(self):
        # I2: send intents live in deliveries; a non-confirmed row blocks
        # reconcile exactly like the legacy outbox key did.
        with self.service.store.transaction() as db:
            db.execute("INSERT INTO metadata VALUES('recovery_required', 'true')")
            db.execute("INSERT INTO deliveries(id, channel, target_key, semantic_key, state,"
                       " payload_json, segments_json) VALUES(?,?,?,?,?,?,?)",
                       ("tg:fixture", "telegram", "synthetic", "evt:fixture", "uncertain",
                        json.dumps({"payload": {"text": "synthetic"}}), "[]"))
        self.assertEqual(self.control.reconcile("felix", "output-uncertain", [])["error"], "unresolved_output")
        self.assertTrue(self.service.recovery_required)
        with self.service.store.transaction() as db:
            db.execute("UPDATE deliveries SET state='confirmed', segments_json=? WHERE id='tg:fixture'",
                       (json.dumps([{"status": "confirmed", "response": {"message_id": 42}}]),))
        self.assertEqual(self.control.reconcile("felix", "output-confirmed", [])["status"], "reconciled")
        self.assertFalse(self.service.recovery_required)

    def test_bot_route_change_does_not_erase_inflight_native_identity(self):
        job = self.reserve()
        self.control.register_bot("felix", "move-bot", dict(self.bot, host="new-host", state="suspended"))
        self.assertFalse(self.control.validate(job, "local_work")["allowed"])
        self.finish(job, native_status="cancelled")
        self.assertEqual(self.control.budget()["active"], 0)

    def test_limits_are_enforced_and_overrun_is_charged(self):
        self.assertEqual(self.control.reserve("gtd-felix", "too-long", self.request(max_runtime_seconds=501))["error"], "request_limit_exceeded")
        self.assertEqual(self.control.reserve("gtd-felix", "too-many-retries", self.request(max_retries=2))["error"], "request_limit_exceeded")
        job = self.reserve()
        self.finish(job, native_status="running", terminal=False, runtime_seconds=201, cost_usd=5)
        self.assertFalse(self.control.validate(job, "local_work")["allowed"])
        self.assertEqual(self.control.budget()["committed_cost_usd"], 5)
        self.assertEqual(self.control.budget()["committed_runtime_seconds"], 201)
        self.finish(job, runtime_seconds=202, cost_usd=5)
        self.assertEqual(self.control.budget()["committed_cost_usd"], 5)

    def test_actual_domain_result_receipt_closes_integration(self):
        job = self.reserve()
        self.finish(job)
        self.control.accept_result("gtd-felix", "accept", job, dict(evidence_reference="fixture://e", artifact_reference="fixture://a", criteria_met=True))
        receipt = self.service.execute("felix", dict(operation_id="material", action="put_material", item_id=self.item["id"], expected_version=self.item["version"], fields={"content": "Synthetic accepted output"}))
        self.assertEqual(receipt["status"], "applied", receipt)
        integrated = self.control.record_integration(job, receipt)
        self.assertEqual(integrated["status"], "integrated", integrated)
        self.assertNotEqual(self.service.get_item(self.item["id"])["status"], "done")

    def test_correction_between_acceptance_and_material_prevents_integration(self):
        job = self.reserve()
        self.finish(job)
        self.control.accept_result("gtd-felix", "accept", job, dict(evidence_reference="fixture://e", artifact_reference="fixture://a", criteria_met=True))
        edit = self.service.execute("felix", dict(operation_id="correction", action="edit", item_id=self.item["id"], expected_version=self.item["version"], fields={"title": "New human meaning"}))
        self.assertEqual(edit["status"], "applied", edit)
        rejected = self.control.record_integration(job, edit)
        self.assertEqual(rejected["error"], "domain_result_change_required")
        self.assertEqual(self.control.get_job(job)["integration"], "accepted_pending_integration")

    def test_standing_private_preparation_of_capture_needs_no_new_mandate(self):
        capture = self.service.capture("felix", "new-capture", "Synthetic incoming note")["item"]
        bot = dict(self.bot, id="principal", capabilities=["prepare_private"], mandate_id=None, item_id=capture["id"])
        registered = self.control.register_bot("gtd-felix", "principal-bot", bot)
        self.assertEqual(registered["status"], "applied", registered)
        request = self.request(item_id=capture["id"], expected_version=capture["version"], capability="prepare_private", bot_id="principal", mandate_id=None)
        receipt = self.control.reserve("gtd-felix", "prepare-capture", request)
        self.assertEqual(receipt["status"], "reserved", receipt)
        self.assertTrue(self.control.validate(receipt["job_id"], "prepare_private")["allowed"])
        self.assertIsNone(receipt["job"]["mandate_id"])

    def test_zero_reservations_cannot_create_unbudgeted_dispatch(self):
        for field in ("max_cost_usd", "max_runtime_seconds"):
            receipt = self.control.reserve("gtd-felix", "zero-" + field, self.request(**{field: 0}))
            self.assertEqual(receipt["error"], "positive_reservation_required")
        self.assertEqual(self.control.budget()["active"], 0)

    def test_shared_allocations_and_descendant_cap_cannot_be_multiplied(self):
        root = self.reserve(max_cost_usd=6, max_descendants=1)
        child = self.reserve("child", parent_job_id=root, purpose="child", max_cost_usd=2, max_runtime_seconds=50, max_descendants=0)
        limits = self.control.validate(root, "local_work")["limits"]
        self.assertEqual(limits["max_cost_usd"], 4)
        self.assertEqual(limits["max_runtime_seconds"], 150)
        self.finish(child)
        rejected = self.control.reserve("gtd-felix", "another-child", self.request(parent_job_id=root, purpose="other", max_cost_usd=1, max_runtime_seconds=10))
        self.assertEqual(rejected["error"], "descendants_exhausted")
        self.assertEqual(self.control.budget()["committed_cost_usd"], 6)

    def private_job(self):
        capture = self.service.capture("felix", "progress-capture", "Prepare synthetic response")["item"]
        bot = dict(self.bot, id="principal", capabilities=["prepare_private"], mandate_id=None, item_id=capture["id"])
        self.control.register_bot("gtd-felix", "progress-bot", bot)
        receipt = self.control.reserve("gtd-felix", "progress-reserve", self.request(item_id=capture["id"], expected_version=capture["version"], capability="prepare_private", bot_id="principal", mandate_id=None))
        self.assertEqual(receipt["status"], "reserved", receipt)
        return receipt["job_id"], capture

    def test_verified_own_progress_advances_and_human_meaning_still_invalidates(self):
        job, item = self.private_job()
        receipt = self.service.execute("gtd-felix", dict(operation_id="own-clarify", action="clarify", item_id=item["id"], expected_version=item["version"], fields={"kind": "reference", "commitment": "proposed"}))
        self.assertEqual(receipt["status"], "applied", receipt)
        self.assertFalse(self.control.validate(job, "prepare_private")["allowed"])
        progress = self.control.record_progress(job, receipt, item["version"])
        self.assertEqual(progress["status"], "recorded", progress)
        self.assertTrue(self.control.validate(job, "prepare_private")["allowed"])
        current = receipt["item"]
        note = self.service.execute("felix", dict(operation_id="human-note", action="edit", item_id=item["id"], expected_version=current["version"], fields={"notes": "Compatible annotation"}))
        self.assertEqual(note["status"], "applied", note)
        valid = self.control.validate(job, "prepare_private")
        self.assertTrue(valid["allowed"], valid)
        self.assertEqual(valid["current_version"], note["item"]["version"])
        changed = self.service.execute("felix", dict(operation_id="human-title", action="edit", item_id=item["id"], expected_version=note["item"]["version"], fields={"title": "Human correction"}))
        self.assertEqual(changed["status"], "applied", changed)
        self.assertFalse(self.control.validate(job, "prepare_private")["allowed"])
        self.assertEqual(self.control.record_progress(job, changed, note["item"]["version"])["error"], "progress_receipt_not_verified")

    def test_derived_item_enters_scope_only_through_actual_own_receipt(self):
        job, item = self.private_job()
        receipt = self.service.execute("gtd-felix", dict(operation_id="own-derived", action="derive", item_id=item["id"], expected_version=item["version"], fields={"kind": "reference", "title": "Derived synthetic", "capability": "prepare_private"}))
        self.assertEqual(receipt["status"], "applied", receipt)
        self.assertEqual(self.control.record_progress(job, receipt, item["version"])["status"], "recorded")
        self.assertTrue(self.control.validate_target(job, "gtd-felix", receipt["item"]["id"], "prepare_private")["allowed"])
        self.assertFalse(self.control.validate_target(job, "gtd-felix", self.item["id"], "prepare_private")["allowed"])

    def test_deferred_child_retains_root_budget_until_global_slot_available(self):
        self.config["max_active"] = 1
        self.control = ExecutionControl(self.service, self.config)
        root = self.reserve(max_cost_usd=6)
        receipt = self.control.reserve("gtd-felix", "deferred", self.request(parent_job_id=root, purpose="child", max_cost_usd=2, max_runtime_seconds=50, defer_when_busy=True))
        self.assertEqual(receipt["status"], "reserved", receipt)
        child = receipt["job_id"]
        self.assertEqual(receipt["job"]["delivery"], "deferred")
        self.assertEqual(self.control.budget()["active"], 1)
        self.finish(root, cost_usd=None)
        self.assertEqual(self.control.budget()["committed_cost_usd"], 6)
        self.assertEqual(self.control.activate_deferred(child)["status"], "activated")
        self.assertEqual(self.control.budget()["active"], 1)

    def test_owner_bootstraps_capability_inventory_without_creating_a_task(self):
        service = GTDService(self.root / "empty")
        try:
            control = ExecutionControl(service, self.config)
            bot = {k: v for k, v in self.bot.items() if k not in {"item_id", "mandate_id"}}
            self.assertEqual(control.register_bot("felix", "bootstrap", bot)["status"], "applied")
            self.assertEqual(service.query(), [])
            self.assertEqual(control.reserve("gtd-felix", "no-item", self.request())["status"], "rejected")
        finally:
            service.close()

    def test_executor_actor_receives_only_its_own_granted_scope(self):
        service = GTDService(self.root / "executor", executor_actors=["worker"])
        try:
            control = ExecutionControl(service, self.config)
            item = service.capture("felix", "input", "Synthetic executor task")["item"]
            item = service.execute("felix", dict(operation_id="action", action="clarify", item_id=item["id"], expected_version=item["version"], fields={"kind": "action", "commitment": "committed"}))["item"]
            grant = service.execute("felix", dict(operation_id="grant", action="grant_mandate", item_id=item["id"], expected_version=item["version"], fields={"scope_item_id": item["id"], "actors": ["worker"], "capabilities": ["prepare_private"], "completion_criteria": "Synthetic evidence"}))
            self.assertEqual(grant["status"], "applied", grant)
            item = grant["item"]
            nested = service.execute("felix", dict(operation_id="worker-existing-child", action="derive", item_id=item["id"], expected_version=item["version"],
                fields={"kind": "reference", "title": "Existing nested content", "capability": "prepare_private", "mandate_id": grant["mandate"]["id"]}))["item"]
            bot = dict(self.bot, actor="worker", item_id=item["id"], capabilities=["prepare_private"], mandate_id=grant["mandate"]["id"])
            self.assertEqual(control.register_bot("felix", "worker", bot)["status"], "applied")
            request = self.request(item_id=item["id"], expected_version=item["version"], capability="prepare_private", mandate_id=grant["mandate"]["id"])
            receipt = control.reserve("gtd-felix", "delegate", request)
            self.assertEqual(receipt["status"], "reserved", receipt)
            job = receipt["job"]
            self.assertEqual(job["actor"], "worker")
            self.assertNotIn(nested["id"], job["item_bases"])
            self.assertEqual(control.validate_target(job["id"], "worker", nested["id"], "prepare_private")["reason"], "outside_job_scope")
            self.assertEqual(job["requested_by"], "gtd-felix")
            self.assertTrue(control.validate_target(job["id"], "worker", item["id"], "prepare_private")["allowed"])
            self.assertFalse(control.validate_target(job["id"], "gtd-felix", item["id"], "prepare_private")["allowed"])
        finally:
            service.close()

    def test_own_intake_discard_is_terminal_progress_without_new_authority(self):
        job, item = self.private_job()
        receipt = self.service.execute("gtd-felix", dict(operation_id="discard", action="clarify", item_id=item["id"], expected_version=item["version"], fields={"destination": "discard", "reason": "Synthetic nonactionable intake"}))
        self.assertEqual(receipt["status"], "applied", receipt)
        self.assertEqual(self.control.record_progress(job, receipt, item["version"])["status"], "recorded")
        self.assertEqual(self.control.own_terminal_progress(job)["operation_id"], "discard")
        self.finish(job)
        self.assertEqual(self.control.integrate_terminal_progress(job)["status"], "integrated")
        self.assertFalse(self.control.get_job(job)["stop_requested"])

    def test_agent_material_does_not_invalidate_deferred_child_but_human_material_does(self):
        root, item = self.private_job()
        child_request = self.request(item_id=item["id"], expected_version=item["version"], capability="prepare_private", bot_id="principal", mandate_id=None,
            parent_job_id=root, purpose="child", max_cost_usd=1, max_runtime_seconds=20, defer_when_busy=True)
        child = self.control.reserve("gtd-felix", "child-material", child_request)
        self.assertEqual(child["status"], "reserved", child)
        child_id = child["job_id"]
        own = self.service.execute("gtd-felix", dict(operation_id="parent-material", action="put_material", item_id=item["id"], expected_version=item["version"], fields={"content": "Parent's private preparation"}))
        self.assertEqual(self.control.record_progress(root, own, item["version"])["status"], "recorded")
        self.assertTrue(self.control.validate(child_id, "prepare_private")["allowed"])
        human = self.service.execute("felix", dict(operation_id="human-material", action="put_material", item_id=item["id"], expected_version=own["item"]["version"], fields={"content": "Human-authored position"}))
        self.assertEqual(human["status"], "applied", human)
        self.assertEqual(self.control.validate(child_id, "prepare_private")["reason"], "stale_item_version")

    def test_legacy_dependency_without_basis_is_blocked_without_migration(self):
        derived = self.service.execute("felix", dict(operation_id="legacy-dependent", action="derive", item_id=self.item["id"], expected_version=self.item["version"], fields={"kind": "action", "title": "Legacy child", "capability": "local_work"}))
        child = derived["item"]
        job = self.reserve(item_id=child["id"], expected_version=child["version"])
        # I1: corrupt the bounded per-row admission+detail (not global history)
        # to prove the service still requires the dependency basis.
        with self.service.store.transaction():
            import json as _json
            row = self.service.store.db.execute("SELECT admission_json, detail_json FROM runs WHERE id=?", (job,)).fetchone()
            admission = _json.loads(row["admission_json"])
            detail = _json.loads(row["detail_json"])
            admission.pop("source_bases", None)
            detail.pop("source_bases", None)
            self.service.store.db.execute("UPDATE runs SET admission_json=?, detail_json=? WHERE id=?",
                (_json.dumps(admission, sort_keys=True), _json.dumps(detail, sort_keys=True), job))
        self.assertEqual(self.control.validate(job, "local_work")["reason"], "source_basis_required")

    def test_child_parent_text_correction_rejects_old_output_without_revoking_mandate(self):
        derived = self.service.execute("felix", dict(operation_id="dependent", action="derive", item_id=self.item["id"], expected_version=self.item["version"], fields={"kind": "action", "title": "Prepare contribution", "capability": "local_work"}))
        self.assertEqual(derived["status"], "applied", derived)
        child = derived["item"]
        job = self.reserve(item_id=child["id"], expected_version=child["version"])
        self.control.record_dispatch(job, self.native(job))
        parent = self.service.get_item(self.item["id"])
        note = self.service.execute("felix", dict(operation_id="parent-note", action="edit", item_id=parent["id"], expected_version=parent["version"], fields={"notes": "Independent note"}))
        self.assertEqual(note["status"], "applied", note)
        self.assertTrue(self.control.validate(job, "local_work")["allowed"])
        material = self.service.execute("gtd-felix", dict(operation_id="parent-generated", action="put_material", item_id=parent["id"], expected_version=note["item"]["version"], fields={"content": "Private generated material", "mandate_id": None}))
        self.assertEqual(material["status"], "applied", material)
        self.assertTrue(self.control.validate(job, "local_work")["allowed"])
        changed = self.service.execute("felix", dict(operation_id="parent-facts", action="edit", item_id=parent["id"], expected_version=material["item"]["version"], fields={"text": "Corrected synthetic facts, same purpose"}))
        self.assertEqual(changed["status"], "applied", changed)
        self.assertEqual(self.control.validate(job, "local_work").get("reason"), "source_version_stale")
        self.finish(job)
        self.assertEqual(self.control.accept_result("gtd-felix", "old-result", job, {"criteria_met": True, "evidence_reference": "fixture://evidence", "artifact_reference": "fixture://old"})["error"], "source_version_stale")
        self.assertEqual(next(m for m in self.service.mandates() if m["id"] == self.mandate)["status"], "active")
        fresh = self.reserve("fresh-child", item_id=child["id"], expected_version=child["version"])
        self.assertTrue(self.control.validate(fresh, "local_work")["allowed"])

    def test_progress_ack_rechecks_receipts_and_human_correction_after_restart(self):
        job, item = self.private_job()
        receipt = self.service.execute('gtd-felix', dict(operation_id='ack-clarify', action='clarify', item_id=item['id'], expected_version=item['version'], fields={'kind': 'reference', 'commitment': 'proposed'}))
        self.assertEqual(receipt['status'], 'applied', receipt)
        self.assertEqual(self.control.record_progress(job, receipt, item['version'])['status'], 'recorded')
        self.finish(job)
        operations_before = self.service.store.db.execute('SELECT count(*) FROM operations').fetchone()[0]
        self.assertEqual(self.control.acknowledge_progress(job)['status'], 'integrated')
        self.service.close()
        self.service = GTDService(self.root / 'data')
        self.control = ExecutionControl(self.service, self.config)
        self.assertEqual(self.control.acknowledge_progress(job)['status'], 'integrated')
        self.assertEqual(self.service.store.db.execute('SELECT count(*) FROM operations').fetchone()[0], operations_before)
        current = self.service.get_item(item['id'])
        correction = self.service.execute('felix', dict(operation_id='ack-human-correction', action='edit', item_id=item['id'], expected_version=current['version'], fields={'text': 'Human corrected facts'}))
        self.assertEqual(correction['status'], 'applied', correction)
        self.assertEqual(self.control.acknowledge_progress(job)['error'], 'stale_item_version')

    def test_progress_ack_rejects_unverified_operation_even_after_terminal(self):
        job, item = self.private_job()
        self.finish(job)
        with self.service.store.transaction():
            import json as _json
            row = self.service.store.db.execute("SELECT detail_json FROM runs WHERE id=?", (job,)).fetchone()
            detail = _json.loads(row["detail_json"])
            detail['progress'] = [{'operation_id': 'nonexistent', 'review': True}]
            self.service.store.db.execute("UPDATE runs SET detail_json=? WHERE id=?", (_json.dumps(detail, sort_keys=True), job))
        self.assertEqual(self.control.acknowledge_progress(job)['error'], 'progress_receipt_not_verified')
        self.assertNotEqual(self.control.get_job(job)['integration'], 'integrated')

    def test_routed_terminal_progress_requires_authentic_resolution_and_preserves_target(self):
        job, source = self.private_job()
        target = self.service.capture('felix', 'routing-target', 'Existing target')['item']
        receipt = self.service.execute('gtd-felix', {'operation_id': 'control-route', 'action': 'clarify',
            'item_id': source['id'], 'expected_version': source['version'], 'fields': {'destination': 'existing',
                'target_item_id': target['id'], 'reason': 'Continue existing subject',
                'intent_basis': {'source_item_id': source['id'], 'quote': source['text']}}})
        self.assertEqual(receipt['status'], 'applied', receipt)
        self.assertIsNone(self.control.own_terminal_progress(job))
        self.assertEqual(self.control.record_progress(job, receipt, source['version'])['status'], 'recorded')
        self.assertEqual(self.control.own_terminal_progress(job)['operation_id'], 'control-route')
        self.finish(job)
        self.assertEqual(self.control.integrate_terminal_progress(job)['status'], 'integrated')
        self.assertEqual(self.service.get_item(target['id']), target)

    def test_new_principal_admission_snapshots_existing_authorized_descendants_only(self):
        child = self.service.execute('gtd-felix', dict(operation_id='previous-child', action='derive', item_id=self.item['id'], expected_version=self.item['version'],
            fields={'kind': 'action', 'title': 'Existing child', 'capability': 'local_work', 'mandate_id': self.mandate, 'completion_criteria': 'Checked child'}))['item']
        old = self.reserve('old-run')
        corrected = self.service.execute('felix', dict(operation_id='root-new-facts', action='edit', item_id=self.item['id'], expected_version=self.item['version'], fields={'text': 'New facts, same mandate'}))
        self.assertEqual(corrected['status'], 'applied', corrected)
        self.assertFalse(self.control.validate(old, 'local_work')['allowed'])
        self.finish(old, native_status='cancelled')
        self.item = corrected['item']
        job = self.reserve('continued')
        self.assertTrue(self.control.validate_target(job, 'gtd-felix', child['id'], 'local_work')['allowed'])
        outsider = self.service.capture('felix', 'outside-continuation', 'Other matter')['item']
        self.assertEqual(self.control.validate_target(job, 'gtd-felix', outsider['id'], 'prepare_private')['reason'], 'outside_job_scope')
        late = self.service.execute('felix', dict(operation_id='late-human-child', action='derive', item_id=self.item['id'], expected_version=self.item['version'], fields={'kind': 'action', 'title': 'Late child', 'capability': 'local_work', 'mandate_id': self.mandate}))['item']
        self.assertEqual(self.control.validate_target(job, 'gtd-felix', late['id'], 'local_work')['reason'], 'outside_job_scope')
        edit = self.service.execute('felix', dict(operation_id='child-correction', action='edit', item_id=child['id'], expected_version=child['version'], fields={'text': 'Corrected child facts'}))
        self.assertEqual(edit['status'], 'applied', edit)
        self.assertFalse(self.control.validate_target(job, 'gtd-felix', child['id'], 'local_work')['allowed'])

    def test_ancestry_movement_and_lateral_project_link_do_not_expand_scope(self):
        def derive(parent, operation):
            return self.service.execute('felix', dict(operation_id=operation, action='derive', item_id=parent['id'], expected_version=parent['version'],
                fields={'kind': 'action', 'title': operation, 'capability': 'local_work', 'mandate_id': self.mandate}))['item']
        child = derive(self.item, 'scope-child')
        grandchild = derive(child, 'scope-grandchild')
        lateral = self.service.capture('felix', 'scope-lateral', 'Lateral item')['item']
        linked = self.service.execute('felix', dict(operation_id='project-link', action='clarify', item_id=lateral['id'], expected_version=lateral['version'],
            fields={'kind': 'action', 'commitment': 'committed', 'project_id': self.item['id']}))['item']
        job = self.reserve('scope-principal')
        self.assertTrue(self.control.validate_target(job, 'gtd-felix', grandchild['id'], 'local_work')['allowed'])
        self.assertEqual(self.control.validate_target(job, 'gtd-felix', linked['id'], 'local_work')['reason'], 'outside_job_scope')
        # Public domain currently has no reparent command; simulate persisted
        # topology replacement to verify the guard independently of that API.
        with self.service.store.transaction():
            item, versions = self.service._item(child['id'])
            self.service._apply_updates('felix', 'synthetic-reparent', 'synthetic-digest', item, versions, {'parent_id': linked['id']})
        self.assertEqual(self.control.validate_target(job, 'gtd-felix', grandchild['id'], 'local_work')['reason'], 'outside_job_scope')
        self.assertFalse(self.control.validate_target(job, 'gtd-felix', self.item['id'], 'local_work')['allowed'])

    def test_standing_private_preparation_resumes_proposed_children_without_commitment_authority(self):
        old, root = self.private_job()
        derived = self.service.execute('gtd-felix', dict(operation_id='private-proposal', action='derive', item_id=root['id'], expected_version=root['version'],
            fields={'kind': 'action', 'title': 'Proposed preparation', 'commitment': 'proposed', 'capability': 'prepare_private', 'completion_criteria': 'Private draft'}))
        self.assertEqual(derived['status'], 'applied', derived)
        child = derived['item']
        self.finish(old)
        prior = self.control.get_job(old)
        request = {key: prior[key] for key in ('item_id', 'expected_version', 'mandate_id', 'capability', 'bot_id', 'purpose', 'scope', 'max_cost_usd', 'max_runtime_seconds', 'max_retries', 'max_descendants')}
        reserved = self.control.reserve('gtd-felix', 'resume-private', request)
        self.assertEqual(reserved['status'], 'reserved', reserved)
        job = reserved['job_id']
        self.assertIsNone(reserved['job']['mandate_id'])
        self.assertTrue(self.control.validate_target(job, 'gtd-felix', child['id'], 'prepare_private')['allowed'])
        self.assertFalse(self.control.validate_target(job, 'gtd-felix', child['id'], 'local_work')['allowed'])
        prepared = self.service.execute('gtd-felix', dict(operation_id='resumed-draft', action='put_material', item_id=child['id'], expected_version=child['version'], fields={'content': 'Resumed private draft'}))
        self.assertEqual(prepared['status'], 'applied', prepared)
        self.assertEqual(self.control.record_progress(job, prepared, child['version'])['status'], 'recorded')
        closed = self.service.execute('gtd-felix', dict(operation_id='cannot-close-proposal', action='assess_result', item_id=child['id'], expected_version=prepared['item']['version'], fields={'satisfied': True, 'evidence': 'Draft existence is not commitment'}))
        self.assertEqual(closed['status'], 'rejected')
        self.assertEqual(self.service.get_item(child['id'])['commitment'], 'proposed')
        self.assertEqual(self.service.get_item(child['id'])['status'], 'active')

    def test_pre_migration_rejection_preserves_legacy_state(self):
        # I1: a mutating operation refused before the migration cut must leave
        # legacy jobs, idempotency map and backups untouched, and must not
        # store its rejection (the same operation stays retryable post-cut).
        with self.service.store.transaction():
            state = self.control._load()
            state["jobs"] = {"legacy-job": {"id": "legacy-job"}}
            self.service.store.db.execute("INSERT OR REPLACE INTO metadata VALUES(?,?)",
                (self.control.KEY, json.dumps(state)))
        receipt = self.control.reserve("gtd-felix", "pre-migration", self.request())
        self.assertEqual(receipt["status"], "rejected", receipt)
        self.assertEqual(receipt["error"], "migration_required")
        after = self.control._load()
        self.assertEqual(len(after.get("jobs", {})), 1)
        self.assertIsNone(self.service.store.db.execute(
            "SELECT 1 FROM metadata WHERE key=?", (self.control.LEGACY_STATE_BACKUP,)).fetchone())
        self.assertIsNone(self.service.store.db.execute(
            "SELECT 1 FROM metadata WHERE key=?",
            (self.control._control_op_key("pre-migration"),)).fetchone())

    def test_deferred_child_validate_reports_own_subtree_limits(self):
        # I1: a child's effective limits come from its own subtree only; the
        # root family's accounting stays separate (adapters enforce these).
        root, child = self.deferred_contribution()
        self.finish(root)
        self.assertEqual(self.control.activate_deferred(child)["status"], "activated")
        valid = self.control.validate(child, "local_work")
        self.assertTrue(valid["allowed"], valid)
        self.assertEqual(valid["limits"]["max_runtime_seconds"], 50)
        self.assertEqual(valid["limits"]["max_cost_usd"], 1)
        self.assertEqual(valid["limits"]["max_descendants"], 0)

    def test_repeated_event_cause_returns_duplicate_cause_without_partial_cycle(self):
        # I1: repeating a cause (same gtd-event identity, new attempt suffix)
        # after its work finished is a structured domain rejection, never raw
        # SQL, and never a half-written cycle without its run.
        cycles_before = self.service.store.db.execute("SELECT COUNT(*) FROM work_cycles").fetchone()[0]
        root = self.reserve("gtd-event:cause:1")
        self.finish(root)
        receipt = self.control.reserve("gtd-felix", "gtd-event:cause:2", self.request())
        self.assertEqual(receipt["status"], "rejected", receipt)
        self.assertEqual(receipt["error"], "duplicate_cause")
        self.assertEqual(receipt["operation_id"], "gtd-event:cause:2")
        cycles_after = self.service.store.db.execute("SELECT COUNT(*) FROM work_cycles").fetchone()[0]
        self.assertEqual(cycles_after, cycles_before + 1)
        self.assertEqual(
            self.service.store.db.execute("SELECT COUNT(*) FROM runs").fetchone()[0], 1)

    def test_spent_review_found_beyond_sixty_four_row_history(self):
        # I1: spent-review consultation is complete past any row cap: with 64
        # non-exhausted runs plus one exhausted review, the guard still finds it.
        from gtd_felix.orchestration import OrchestrationWorker
        for n in range(65):
            jid = self.reserve(f"history-{n}")
            self.finish(jid, runtime_seconds=200 if n == 64 else 1, cost_usd=0)
        worker = OrchestrationWorker(self.service, self.control, None, {})
        spent, _ = worker._tied_spent_reviews(self.control._load(), self.item["id"])
        self.assertEqual(len(spent), 1)

    def test_rejected_observation_commits_no_rows_and_keeps_reserved_slot(self):
        # I1: an observation rejected by the global native exclusion leaves no
        # partial observation row and keeps the run reserved (still retryable).
        first = self.reserve("first")
        self.control.record_dispatch(first, self.native(first))
        derived = self.service.execute("felix", dict(operation_id="derive-second", action="derive",
            item_id=self.item["id"], expected_version=self.item["version"], fields={"kind": "action",
            "title": "Second", "capability": "local_work", "mandate_id": self.mandate}))["item"]
        second = self.reserve("second", item_id=derived["id"], expected_version=derived["version"])
        receipt = self.control.observe(second, self.observation(
            second, native_status="running", terminal=False, runtime_seconds=1, cost_usd=0))
        self.assertEqual(receipt["status"], "rejected", receipt)
        self.assertEqual(receipt["error"], "concurrency_exhausted")
        self.assertEqual(self.service.store.db.execute(
            "SELECT COUNT(*) FROM run_observations WHERE run_id=?", (second,)).fetchone()[0], 0)
        self.assertEqual(self.control._run_row(second)["state"], "reserved")

    def test_dispatch_claim_is_atomic_idempotent_and_exclusive(self):
        # I1: the native slot is claimed durably before any remote effect.
        first = self.reserve()
        claimed = self.control.claim_dispatch(first)
        self.assertEqual(claimed["status"], "claimed", claimed)
        self.assertNotIn("duplicate", claimed)
        again = self.control.claim_dispatch(first)
        self.assertEqual(again["status"], "claimed", again)
        self.assertTrue(again.get("duplicate"))
        derived = self.service.execute("felix", dict(operation_id="claim-second-derive", action="derive",
            item_id=self.item["id"], expected_version=self.item["version"], fields={"kind": "action",
            "title": "Claim second", "capability": "local_work", "mandate_id": self.mandate}))["item"]
        second = self.reserve("second", item_id=derived["id"], expected_version=derived["version"])
        busy = self.control.claim_dispatch(second)
        self.assertEqual(busy["status"], "rejected", busy)
        self.assertEqual(busy["error"], "native_slot_busy")
        self.finish(first)
        self.assertEqual(self.control.claim_dispatch(second)["status"], "claimed")
        self.assertEqual(
            self.control.claim_dispatch("missing")["error"], "job_not_found")

    def test_native_identity_preserves_provider_facets(self):
        # I1: provider-specific identity facets (e.g. Codex thread_id) round-trip
        # through the table projection; repeating the identical full identity
        # in a later observation is not a native_identity_changed.
        job = self.reserve()
        full = dict(self.native(job), thread_id=job)
        self.assertEqual(self.control.record_dispatch(job, full)["status"], "recorded")
        self.assertEqual(self.control.get_job(job)["native"], full)
        receipt = self.control.observe(job, self.observation(job, native_identity=full))
        self.assertEqual(receipt["status"], "recorded", receipt)
        self.assertEqual(self.control.get_job(job)["native"], full)

    def test_private_root_descendant_guard_is_an_explicit_trusted_option(self):
        job, source = self.private_job()
        derived = self.service.execute('gtd-felix', dict(operation_id='flag-child', action='derive', item_id=source['id'], expected_version=source['version'],
            fields={'kind': 'reference', 'title': 'Tracked private content', 'capability': 'prepare_private'}))
        self.assertEqual(derived['status'], 'applied', derived)
        self.assertEqual(self.control.record_progress(job, derived, source['version'])['status'], 'recorded')
        child = derived['item']
        corrected = self.service.execute('felix', dict(operation_id='flag-child-correction', action='edit', item_id=child['id'], expected_version=child['version'], fields={'text': 'Human correction'}))
        self.assertEqual(corrected['status'], 'applied', corrected)
        self.assertTrue(self.control.validate_target(job, 'gtd-felix', source['id'], 'prepare_private')['allowed'])
        guarded = self.control.validate_target(job, 'gtd-felix', source['id'], 'prepare_private', require_descendants=True)
        self.assertEqual(guarded['reason'], 'stale_descendant_version')


if __name__ == "__main__":
    unittest.main()
