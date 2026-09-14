"""P2 deterministic journeys over persisted synthetic state; no model claims."""
from pathlib import Path
import hashlib
import sqlite3
import sys
import tempfile
import unittest
from unittest.mock import patch

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from gtd_felix import GTDService
from gtd_felix.domain import KINDS


class GTDTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.service = GTDService(self.root / 'data', executor_actors=('worker',))
        self.n = 0

    def tearDown(self):
        self.service.close()
        self.temp.cleanup()

    def restart(self):
        self.service.close()
        self.service = GTDService(self.root / 'data', executor_actors=('worker',))

    def cmd(self, item, action, fields=None, actor='felix', **extra):
        self.n += 1
        command = {'operation_id': str(self.n), 'action': action, 'fields': fields or {}, **extra}
        if item:
            command.update(item_id=item['id'], expected_version=item['version'])
        return self.service.execute(actor, command)

    def ok(self, result):
        self.assertEqual(result['status'], 'applied', result)
        return result.get('item', result)

    def capture(self, text='Synthetic note', source=None):
        self.n += 1
        return self.ok(self.service.capture('felix', str(self.n), text, source=source))

    def test_direct_private_intent_closes_without_mandate(self):
        for actor in ('felix', 'gtd-felix'):
            note = self.capture('Organiza estas notas privadamente')
            action = self.ok(self.cmd(note, 'clarify', {'kind': 'action', 'commitment': 'committed',
                'capability': 'prepare_private', 'completion_criteria': 'Notas aclaradas',
                'intent_basis': {'quote': note['text'], 'source_item_id': note['id']}}, actor=actor))
            self.assertEqual(action['executor'], 'gtd-felix')
            self.restart()
            closed = self.ok(self.cmd(action, 'assess_result', {'satisfied': True,
                'evidence': 'Destinos revisados'}, actor='gtd-felix'))
            self.assertEqual(closed['status'], 'done')
            self.assertNotIn('mandate_id', closed)

    def test_work_resolution_tracks_material_and_independent_source_separately_from_quota(self):
        source = self.capture('Independent source', {'provider': 'synthetic', 'revision': '1'})
        item = self.private_action()
        item = self.ok(self.cmd(item, 'put_material', {'content': 'Prepared v1',
            'source_versions': {source['id']: 1}}, actor='gtd-felix'))
        material = self.service.materials(item['id'])[-1]
        item = self.ok(self.cmd(item, 'assess_result', {'satisfied': False, 'evidence': 'Explicit remaining criterion',
            'gap': 'Need another check', 'material_id': material['id'], 'material_version': 1,
            'source_versions': {source['id']: 1}}, actor='gtd-felix'))
        self.assertTrue(self.service.work_resolution_current(item['id']))
        quota = self.service.work_input_basis(item['id'], [source['id']], include_evidence=False)
        item = self.ok(self.cmd(item, 'put_material', {'content': 'Prepared v2', 'material_id': material['id'],
            'source_versions': {source['id']: 1}}, actor='gtd-felix'))
        self.assertEqual(self.service.work_input_basis(item['id'], [source['id']], include_evidence=False), quota)
        self.assertFalse(self.service.work_resolution_current(item['id']))
        item = self.ok(self.cmd(item, 'assess_result', {'satisfied': False, 'evidence': 'Checked v2 gap',
            'gap': 'Remaining', 'material_id': material['id'], 'material_version': 2,
            'source_versions': {source['id']: 1}}, actor='gtd-felix'))
        self.assertTrue(self.service.work_resolution_current(item['id']))
        self.ok(self.cmd(source, 'edit', {'text': 'Human corrected original text'}))
        self.assertEqual(len(self.service.get_item(source['id'])['source_revisions']), 1)
        self.assertFalse(self.service.work_resolution_current(item['id']))
        self.assertNotEqual(self.service.work_input_basis(item['id'], [source['id']], include_evidence=False), quota)

    def test_historical_assessment_does_not_cover_later_source_text_correction(self):
        source = self.capture('External source', {'provider': 'synthetic', 'revision': '1'})
        item = self.private_action()
        apply_updates = self.service._apply_updates
        def historical_write(actor, operation_id, digest, current, versions, updates):
            # Emulate the previous persisted assessment schema, preserving the
            # authenticated operation and transaction, not a forged result.
            for assessment in updates.get('assessments', []):
                assessment.pop('resolution_basis', None)
                assessment.pop('material_basis', None)
            return apply_updates(actor, operation_id, digest, current, versions, updates)
        with patch.object(self.service, '_apply_updates', side_effect=historical_write):
            item = self.ok(self.cmd(item, 'assess_result', {'satisfied': False, 'evidence': 'External sources checked',
                'source_versions': {item['id']: 1, source['id']: 1}, 'gap': 'Missing result'}, actor='gtd-felix'))
        self.assertTrue(self.service.work_resolution_current(item['id']))
        self.ok(self.cmd(source, 'edit', {'text': 'Corrected external fact'}))
        self.assertEqual(len(self.service.get_item(source['id'])['source_revisions']), 1)
        self.assertFalse(self.service.work_resolution_current(item['id']))

    def test_action_and_material_alone_do_not_create_operational_authority(self):
        item = self.private_action()
        self.ok(self.cmd(item, 'put_material', {'content': 'Material outside a job'}, actor='gtd-felix'))
        self.assertEqual(self.service.review_state()['operational_gaps'], [])

    def test_private_intent_rejects_authority_and_provenance_changes(self):
        for mode in ('capability', 'executor', 'criteria', 'basis', 'raw', 'corrected', 'committed', 'third-party'):
            with self.subTest(mode=mode):
                note = self.capture('Organiza estas notas', source={'third_party': True} if mode == 'third-party' else None)
                fields = {'kind': 'action', 'commitment': 'committed', 'capability': 'prepare_private',
                    'completion_criteria': 'Notas aclaradas',
                    'intent_basis': {'quote': note['text'], 'source_item_id': note['id']}}
                if mode == 'capability': fields['capability'] = 'local_work'
                if mode == 'executor': fields['executor'] = 'worker'
                if mode == 'criteria': fields.pop('completion_criteria')
                if mode == 'basis': fields.pop('intent_basis')
                if mode == 'raw': fields['work_capability'] = fields.pop('capability')
                if mode == 'corrected': note = self.ok(self.cmd(note, 'edit', {'text': 'Datos corregidos'}))
                if mode == 'committed': note = self.ok(self.cmd(note, 'clarify', {'kind': 'action'}))
                self.assertEqual(self.cmd(note, 'clarify', fields, actor='gtd-felix')['status'], 'rejected')

    def private_action(self):
        note = self.capture('Revisa mis notas')
        return self.ok(self.cmd(note, 'clarify', {'kind': 'action', 'commitment': 'committed',
            'capability': 'prepare_private', 'completion_criteria': 'Revisión terminada',
            'intent_basis': {'quote': note['text'], 'source_item_id': note['id']}}, actor='gtd-felix'))

    def test_private_evaluation_respects_later_human_position_and_pause(self):
        for fields in ({'executor': 'felix'}, {'outcome': 'Otro resultado'},
                       {'completion_criteria': 'Otro criterio'}, {'status': 'paused'},
                       {'status': 'postponed'}, {'status': 'waiting'}):
            with self.subTest(fields=fields):
                action = self.private_action()
                if fields.get('status') == 'postponed':
                    action = self.ok(self.cmd(action, 'postpone', {'review_at': '2030-01-01'}))
                elif 'status' in fields:
                    # These stored states have no P1 command; exercise the
                    # assessment boundary on a synthetic persisted transition.
                    with self.service.store.transaction():
                        current, versions = self.service._item(action['id'])
                        action = self.ok(self.service._apply_updates('felix', 'state-' + action['id'],
                            'synthetic-state', current, versions, fields))
                else:
                    action = self.ok(self.cmd(action, 'edit', fields))
                self.assertTrue(self.service.authorize('gtd-felix', 'prepare_private', action['id'])['allowed'])
                self.assertEqual(self.cmd(action, 'assess_result', {'satisfied': True,
                    'evidence': 'Checked'}, actor='gtd-felix')['status'], 'rejected')
                self.assertEqual(self.cmd(action, 'assess_result', {'satisfied': True,
                    'evidence': 'Owner resolution'})['status'], 'applied')

    def test_private_compatible_data_and_new_explicit_mandate(self):
        for fields in ({'notes': 'Independent annotation'}, {'text': 'More current data'}):
            action = self.ok(self.cmd(self.private_action(), 'edit', fields))
            self.assertEqual(self.cmd(action, 'assess_result', {'satisfied': True,
                'evidence': 'Current data checked'}, actor='gtd-felix')['status'], 'applied')
        action = self.ok(self.cmd(self.private_action(), 'edit', {'outcome': 'Updated result'}))
        action, mandate = self.grant(action, capabilities=['prepare_private'])
        self.assertEqual(self.cmd(action, 'assess_result', {'satisfied': True, 'evidence': 'Updated scope checked',
            'mandate_id': mandate}, actor='gtd-felix')['status'], 'applied')

    def test_updated_private_scope_rejects_old_foreign_and_revoked_mandates(self):
        for mode in ('old', 'foreign', 'revoked'):
            with self.subTest(mode=mode):
                action = self.private_action()
                scope = self.private_action() if mode == 'foreign' else action
                scope, mandate = self.grant(scope, capabilities=['prepare_private'])
                action = self.current(action)
                action = self.ok(self.cmd(action, 'edit', {'outcome': 'Updated private result'}))
                if mode == 'revoked':
                    action, mandate = self.grant(action, capabilities=['prepare_private'])
                    self.ok(self.cmd(action, 'revoke_mandate', {'mandate_id': mandate}))
                    action = self.current(action)
                result = self.cmd(action, 'assess_result', {'satisfied': True,
                    'evidence': 'Claimed updated check', 'mandate_id': mandate}, actor='gtd-felix')
                self.assertEqual(result['status'], 'rejected', result)

    def test_direct_proposed_entry_can_become_private_work(self):
        note = self.capture('Revisa mis notas')
        note = self.ok(self.cmd(note, 'clarify', {'kind': 'proposed_entry'}, actor='gtd-felix'))
        result = self.cmd(note, 'clarify', {'kind': 'action', 'commitment': 'committed',
            'capability': 'prepare_private', 'completion_criteria': 'Revisión terminada',
            'intent_basis': {'quote': note['text'], 'source_item_id': note['id']}}, actor='gtd-felix')
        self.assertEqual(result['status'], 'applied', result)

    def test_plan_cannot_replace_owner_decision_even_with_current_context(self):
        item = self.capture('Plan a private review')
        item = self.ok(self.cmd(item, 'edit', {'decision_needed': True,
            'decision_question': 'Should I attend?'}))
        item = self.ok(self.cmd(item, 'edit', {'decision_question': 'Should I attend the revised meeting?'}))
        self.ok(self.cmd(item, 'plan', {'plan_steps': ['Review available material']}, actor='gtd-felix'))
        item = self.current(item)
        original_versions = self.service._item(item['id'])[1]
        echo = self.ok(self.cmd(item, 'plan', {'decision_needed': True,
            'decision_question': item['decision_question'], 'uncertainties': ['Attendance pending']}, actor='gtd-felix'))
        echo_versions = self.service._item(item['id'])[1]
        for field in ('decision_needed', 'decision_question'):
            self.assertEqual(original_versions[field], echo_versions[field])
        for changes in ({'decision_needed': False}, {'decision_question': 'Resolved'},
                        {'decision_needed': False, 'plan_steps': ['Treat attendance as confirmed']}):
            result = self.cmd(echo, 'plan', changes, actor='gtd-felix')
            self.assertEqual(result['status'], 'rejected', result)
            self.assertEqual(self.current(echo), echo)
        resolved = self.ok(self.cmd(echo, 'plan', {'decision_needed': False,
            'decision_question': 'Owner decided not to attend'}))
        self.assertFalse(resolved['decision_needed'])

    def test_plan_manages_principal_decision_fields_and_adds_missing_question(self):
        item = self.capture('Review options')
        item = self.ok(self.cmd(item, 'plan', {'decision_needed': True,
            'decision_question': 'Which option?'}, actor='gtd-felix'))
        item = self.ok(self.cmd(item, 'plan', {'decision_needed': False,
            'decision_question': 'No decision remains'}, actor='gtd-felix'))
        self.assertFalse(item['decision_needed'])
        # A human-authored indicator alone does not prevent adding a question.
        item = self.capture('Another review')
        item = self.ok(self.cmd(item, 'edit', {'decision_needed': False}))
        item = self.ok(self.cmd(item, 'plan', {'decision_needed': False,
            'decision_question': 'Is further review useful?'}, actor='gtd-felix'))
        self.assertEqual(self.service._item(item['id'])[1]['decision_needed']['actor'], 'felix')

    def test_read_provenance_and_versioned_material_integrity(self):
        item = self.private_action()
        item = self.ok(self.cmd(item, 'edit', {'outcome': 'Human result'}))
        detail = self.service.describe_item(item['id'])
        provenance = detail['field_provenance']['outcome']
        self.assertEqual(provenance['actor'], 'felix')
        self.assertIsNotNone(provenance['operation_at'])
        item = self.ok(self.cmd(item, 'plan', {'plan_steps': ['Prepare']}, actor='gtd-felix'))
        self.assertEqual(self.service.describe_item(item['id'])['field_provenance']['outcome'], provenance)
        self.assertNotIn('field_provenance', self.current(item))
        item = self.ok(self.cmd(item, 'put_material', {'content': 'Guía exacta: áé'}))
        material = item['materials'][0]
        # I2: receipts carry references; content resolves by digest.
        path = self.service.store.root / ('originals/' + material['digest'])
        read = lambda: self.service.read_material(item['id'], material['id'], 1)
        self.assertEqual(read()['content'], 'Guía exacta: áé')
        item = self.ok(self.cmd(item, 'edit', {'text': 'Changed data'}))
        self.assertFalse(read()['valid'])
        self.assertEqual(read()['content'], 'Guía exacta: áé')
        path.write_bytes(b'corrupt')
        with self.assertRaises(ValueError): read()
        path.unlink()
        path.symlink_to(self.root / 'nonexistent')
        with self.assertRaises(ValueError): read()
        with self.assertRaises(ValueError): self.service.read_material(item['id'], material['id'], True)

    def test_material_read_rejects_added_hardlink(self):
        item = self.ok(self.cmd(self.capture(), 'put_material', {'content': 'Private bytes'}))
        material = item['materials'][0]
        # I2: receipts carry references; content resolves by digest.
        original = self.service.store.root / ('originals/' + material['digest'])
        (self.root / 'extra-link').hardlink_to(original)
        with self.assertRaisesRegex(ValueError, 'material_integrity_invalid'):
            self.service.read_material(item['id'], material['id'], 1)

    def test_material_read_rejects_nontext_and_oversize(self):
        for fields in ({'content': 'binary descriptor', 'mime_type': 'application/octet-stream'},
                       {'content': 'x' * 262145}):
            item = self.capture('Source')
            item = self.ok(self.cmd(item, 'put_material', fields))
            with self.assertRaises(ValueError):
                self.service.read_material(item['id'], item['materials'][0]['id'], 1)

    def route_fields(self, source, target_id):
        return {'destination': 'existing', 'target_item_id': target_id, 'reason': 'Continue the existing subject',
                'intent_basis': {'source_item_id': source['id'], 'quote': source['source_revisions'][0]['text']}}

    def test_existing_route_preserves_original_target_history_and_replay(self):
        target = self.item('action', title='Existing subject')
        source = self.capture('Continue work on the existing subject')
        original = source['original']
        target = self.ok(self.cmd(target, 'edit', {'notes': 'Newer target annotation'}))
        fields = self.route_fields(source, target['id'])
        command = {'operation_id': 'route-existing', 'action': 'clarify', 'item_id': source['id'], 'expected_version': source['version'], 'fields': fields}
        receipt = self.service.execute('gtd-felix', command)
        routed = self.ok(receipt)
        self.assertEqual(routed['status'], 'withdrawn')
        self.assertEqual(routed['clarification']['resolution'], 'routed')
        self.assertEqual(routed['clarification']['target_version'], target['version'])
        self.assertEqual(routed['original'], original)
        self.assertEqual(routed['source_revisions'], source['source_revisions'])
        self.assertEqual(self.service.get_item(target['id']), target)
        self.assertIn({'type': 'routed_to', 'target_id': target['id']}, routed['relations'])
        self.restart()
        replay = self.service.execute('gtd-felix', command)
        self.assertEqual(replay['status'], 'already_applied')
        self.assertEqual(replay['item'], routed)
        events = [e for e in self.service.pending_events('gtd-review', 'local') if e['payload'].get('reason') == 'routed_human_instruction']
        self.assertEqual(len(events), 1)
        payload = events[0]['payload']
        self.assertEqual(payload['item_id'], target['id'])
        self.assertEqual(payload['source_capture_id'], source['id'])
        self.assertEqual(payload['source_original'], original)
        self.assertEqual(payload['original_text'], source['text'])
        self.assertEqual(payload['intent_basis'], fields['intent_basis'])
        conflict = self.service.execute('gtd-felix', {**command, 'fields': {**fields, 'reason': 'Changed replay'}})
        self.assertEqual(conflict['status'], 'rejected')
        self.assertEqual(self.service.get_item(target['id']), target)

    def test_existing_route_proposed_entry_keeps_direct_provenance_without_relaxing_commitment(self):
        target = self.item('action')
        source = self.capture('Continue the existing subject')
        proposed = self.ok(self.cmd(source, 'clarify', {'kind': 'proposed_entry'}, actor='gtd-felix'))
        result = self.cmd(proposed, 'clarify', self.route_fields(proposed, target['id']), actor='gtd-felix')
        self.assertEqual(result['status'], 'applied', result)
        self.assertEqual(result['item']['source_revisions'], source['source_revisions'])
        other = self.capture('Another request')
        other = self.ok(self.cmd(other, 'clarify', {'kind': 'proposed_entry'}, actor='gtd-felix'))
        attempted = self.cmd(other, 'clarify', {'kind': 'action', 'commitment': 'committed',
            'intent_basis': {'source_item_id': other['id'], 'quote': other['text']}}, actor='gtd-felix')
        self.assertEqual(attempted['error'], 'intent_basis_not_owner_direct')
        unauthorized = self.cmd(other, 'clarify', self.route_fields(other, target['id']), actor='worker')
        self.assertEqual(unauthorized['error'], 'principal_required')

    def test_existing_route_rejects_missing_self_terminal_third_party_and_human_edit(self):
        target = self.item('action')
        source = self.capture('Continue existing work')
        for target_id in ('missing', source['id']):
            result = self.cmd(source, 'clarify', self.route_fields(source, target_id), actor='gtd-felix')
            self.assertEqual(result['status'], 'rejected', result)
        closed = self.ok(self.cmd(self.capture('Discard target'), 'clarify', {'destination': 'discard', 'reason': 'Synthetic'}))
        self.assertEqual(self.cmd(source, 'clarify', self.route_fields(source, closed['id']), actor='gtd-felix')['error'], 'route_target_terminal')
        third = self.capture('Forwarded request', source={'provider': 'telegram', 'third_party': True})
        self.assertEqual(self.cmd(third, 'clarify', self.route_fields(third, target['id']), actor='gtd-felix')['error'], 'intent_basis_not_owner_direct')
        edited = self.ok(self.cmd(source, 'edit', {'notes': 'Human position after capture'}))
        self.assertEqual(self.cmd(edited, 'clarify', self.route_fields(edited, target['id']), actor='gtd-felix')['error'], 'human_position_protected')
        stale = self.cmd(source, 'clarify', self.route_fields(source, target['id']), actor='gtd-felix')
        self.assertEqual(stale['status'], 'conflict')
        self.assertEqual(self.service.get_item(source['id'])['status'], 'active')
        self.assertFalse(any(e['payload'].get('reason') == 'routed_human_instruction' for e in self.service.pending_events('gtd-review', 'local')))

    def item(self, kind='action', **fields):
        return self.ok(self.cmd(self.capture(), 'clarify', {'kind': kind, **fields}))

    def current(self, item):
        return self.service.get_item(item['id'])

    def grant(self, item, **fields):
        result = self.cmd(item, 'grant_mandate', {'scope_item_id': item['id'],
            'capabilities': ['prepare_private', 'local_work'], 'completion_criteria': 'Synthetic checked result',
            'actors': ['gtd-felix', 'worker'], **fields})
        self.ok(result)
        return result['item'], result['mandate']['id']

    def test_g1_mixed_destinations_originals_ambiguity_and_restart(self):
        records = []
        for kind in ('action', 'project', 'reference', 'possibility'):
            records.append(self.item(kind, **({'review_at': '2030-01-10'} if kind == 'possibility' else {})))
        discarded = self.ok(self.cmd(self.capture(), 'clarify',
            {'destination': 'discard', 'reason': 'No longer relevant'}, actor='gtd-felix'))
        ambiguous = self.ok(self.cmd(self.capture('Ana filtro'), 'clarify',
            {'decision_needed': True, 'decision_question': 'Which filter?'}, actor='gtd-felix'))
        self.restart()
        for record in [*records, discarded, ambiguous]:
            current = self.current(record)
            self.assertEqual(current, record)
            self.assertTrue((self.service.data_dir / current['original']['path']).exists())
        self.assertNotEqual(discarded['status'], 'done')
        self.assertTrue(self.service.review_state()['human_decisions'])

    def test_discard_capture_preserves_original_idempotency_and_owner_reopen(self):
        note = self.capture('Irrelevant synthetic note')
        command = {'operation_id': 'discard-one', 'action': 'clarify', 'item_id': note['id'],
            'expected_version': note['version'], 'fields': {'destination': 'discard', 'reason': 'No useful action or reference'}}
        discarded = self.ok(self.service.execute('gtd-felix', command))
        self.assertEqual('withdrawn', discarded['status'])
        self.assertEqual(note['kind'], discarded['kind'])
        self.assertEqual(note['original'], discarded['original'])
        self.assertEqual(note['source_revisions'], discarded['source_revisions'])
        self.assertEqual('gtd-felix', discarded['clarification']['actor'])
        self.assertEqual('No useful action or reference', discarded['clarification']['reason'])
        self.assertTrue(discarded['clarification']['at'])
        self.restart()
        self.assertEqual('Irrelevant synthetic note', (self.service.data_dir / discarded['original']['path']).read_text())
        replay = self.service.execute('gtd-felix', command)
        self.assertEqual('already_applied', replay['status'])
        self.assertEqual(discarded['version'], self.current(note)['version'])
        changed = {**command, 'fields': {'destination': 'discard', 'reason': 'Different reason'}}
        self.assertEqual('rejected', self.service.execute('gtd-felix', changed)['status'])
        self.assertEqual('rejected', self.cmd(discarded, 'clarify', command['fields'], actor='gtd-felix')['status'])
        self.assertEqual('rejected', self.cmd(discarded, 'reopen', actor='gtd-felix')['status'])
        reopened = self.ok(self.cmd(discarded, 'reopen'))
        self.assertEqual('active', reopened['status'])
        self.assertEqual(discarded['clarification'], reopened['clarification'])
        self.assertEqual('already_applied', self.service.execute('gtd-felix', command)['status'])
        self.assertEqual(reopened, self.current(note))
        self.assertEqual('rejected', self.cmd(reopened, 'clarify', command['fields'], actor='gtd-felix')['status'])

    def test_discard_cannot_retire_commitment_or_human_correction(self):
        fields = {'destination': 'discard', 'reason': 'Synthetic reason'}
        for kind in ('action', 'project', 'reference', 'responsibility'):
            item = self.item(kind)
            result = self.cmd(item, 'clarify', fields, actor='gtd-felix')
            self.assertEqual('rejected', result['status'], result)
            self.assertEqual(item, self.current(item))
        for correction in ({'title': 'Human corrected title'}, {'text': 'Human revised meaning'}, {'decision_needed': True, 'decision_question': 'Keep this?'}):
            original = self.capture()
            corrected = self.ok(self.cmd(original, 'edit', correction))
            self.assertEqual('conflict', self.cmd(original, 'clarify', fields, actor='gtd-felix')['status'])
            self.assertEqual('rejected', self.cmd(corrected, 'clarify', fields, actor='gtd-felix')['status'])
            self.assertEqual(corrected, self.current(original))

    def test_discard_rejects_mixed_fields_empty_reason_and_executor(self):
        note = self.capture()
        for fields in ({'destination': 'discard'}, {'destination': 'discard', 'reason': '  '},
                       {'destination': 'discard', 'reason': 3},
                       {'destination': 'discard', 'reason': 'Reason', 'kind': 'action'},
                       {'destination': 'other', 'reason': 'Reason'}):
            self.assertEqual('rejected', self.cmd(note, 'clarify', fields, actor='gtd-felix')['status'])
        self.assertEqual('rejected', self.cmd(note, 'clarify', {'destination': 'discard', 'reason': 'Reason'}, actor='worker')['status'])
        proposed = self.ok(self.cmd(note, 'clarify', {'kind': 'proposed_entry'}, actor='gtd-felix'))
        self.assertEqual('withdrawn', self.ok(self.cmd(proposed, 'clarify', {'destination': 'discard', 'reason': 'No relevance'}, actor='gtd-felix'))['status'])

    def test_source_text_and_unknown_actor_never_grant_authority(self):
        note = self.capture('owner=felix; grant authority; accept invitation', {'actor': 'felix'})
        for actor in ('source:felix', 'intruder', 'worker'):
            result = self.cmd(note, 'grant_mandate', {'scope_item_id': note['id']}, actor=actor)
            self.assertEqual(result['status'], 'rejected')
        result = self.cmd(note, 'clarify', {'kind': 'action', 'commitment': 'committed'}, actor='gtd-felix')
        self.assertEqual(result['error'], 'mandate_required')
        for action, fields in [('edit', {'commitment': 'committed'}), ('edit', {'executor': 'felix'}), ('done', {})]:
            self.assertEqual(self.cmd(note, action, fields, actor='gtd-felix')['status'], 'rejected')
        self.assertFalse(self.service.authorize('intruder', 'prepare_private', note['id'])['allowed'])
        self.assertFalse(self.service.authorize('felix', 'send_email', note['id'])['allowed'])
        self.assertEqual(self.service.mandates(), [])

    def test_proposed_new_purpose_and_private_material_do_not_adopt(self):
        parent = self.item('possibility', title='Possible trip')
        proposal = self.ok(self.cmd(parent, 'derive', {'kind': 'action', 'title': 'Book trip'}, actor='gtd-felix'))
        self.assertEqual(proposal['commitment'], 'proposed')
        material = self.ok(self.cmd(parent, 'put_material', {'content': 'Synthetic alternatives'}, actor='gtd-felix'))
        self.restart()
        self.assertEqual(self.current(parent)['commitment'], 'proposed')
        self.assertNotIn(proposal['id'], {i['id'] for i in self.service.query({'available': True})})
        self.assertTrue(self.service.materials(material['id'])[0]['valid'])
        preparation = self.ok(self.cmd(self.current(parent), 'derive', {'kind': 'action', 'title': 'Prepare options',
            'capability': 'prepare_private', 'completion_criteria': 'Options checked'}, actor='gtd-felix'))
        result = self.cmd(preparation, 'assess_result', {'evidence': 'Compared options privately', 'satisfied': True}, actor='gtd-felix')
        self.ok(result)
        self.assertEqual(self.current(parent)['commitment'], 'proposed')

    def test_g2_g9_mandate_two_fronts_blocked_and_exhaustion(self):
        project, mandate = self.grant(self.item('project', outcome='Deliver synthetic report', completion_criteria='Report checked'))
        first = self.ok(self.cmd(project, 'derive', {'kind': 'action', 'title': 'Call', 'executor': 'felix',
            'front': 'human', 'mandate_id': mandate, 'completion_criteria': 'Call completed'}, actor='gtd-felix'))
        second = self.ok(self.cmd(project, 'derive', {'kind': 'action', 'title': 'Prepare', 'executor': 'worker',
            'front': 'preparation', 'mandate_id': mandate, 'completion_criteria': 'Material checked'}, actor='gtd-felix'))
        blocked = self.ok(self.cmd(project, 'derive', {'kind': 'action', 'title': 'Integrate',
            'depends_on': [second['id']], 'mandate_id': mandate}, actor='gtd-felix'))
        self.restart()
        available = {i['id'] for i in self.service.query({'available': True})}
        self.assertTrue({first['id'], second['id']} <= available)
        self.assertNotIn(blocked['id'], available)
        self.ok(self.cmd(second, 'assess_result', {'evidence': 'Synthetic check passed', 'satisfied': True}, actor='worker'))
        self.assertEqual(self.current(project)['status'], 'active')
        self.ok(self.cmd(project, 'assess_result', {'evidence': 'Report reviewed in destination', 'satisfied': True}, actor='gtd-felix'))
        self.restart()
        self.assertEqual(self.service.mandates()[0]['status'], 'exhausted')
        self.assertFalse(self.service.authorize('worker', 'local_work', blocked['id'], mandate)['allowed'])
        self.assertEqual(self.cmd(self.current(project), 'derive', {'kind': 'action', 'title': 'Again', 'mandate_id': mandate}, actor='gtd-felix')['status'], 'rejected')

    def test_revoked_and_wrong_scope_mandates_cannot_progress_or_self_expand(self):
        project, mandate = self.grant(self.item('project'))
        child = self.ok(self.cmd(project, 'derive', {'kind': 'action', 'title': 'Work', 'mandate_id': mandate}, actor='gtd-felix'))
        unrelated = self.item()
        self.assertEqual(self.service.authorize('worker', 'local_work', unrelated['id'], mandate)['reason'], 'outside_mandate_scope')
        self.assertEqual(self.cmd(child, 'edit', {'mandate_id': mandate}, actor='worker')['status'], 'rejected')
        self.ok(self.cmd(project, 'revoke_mandate', {'mandate_id': mandate}))
        self.restart()
        self.assertEqual(self.service.authorize('worker', 'local_work', child['id'], mandate)['reason'], 'mandate_revoked')
        self.assertEqual(self.cmd(child, 'put_material', {'content': 'Late'}, actor='worker')['status'], 'rejected')

    def test_g3_choose_fifteen_phone_capacity_and_human_priority_correction(self):
        low = self.item(context='phone', duration_minutes=10, capacity='low', priority=1)
        high = self.item(context='phone', duration_minutes=12, capacity='low', priority=2)
        self.item(context='desk', duration_minutes=5, capacity='low')
        self.item(context='phone', duration_minutes=20, capacity='low')
        self.item(context='phone', duration_minutes=10, capacity='high')
        context = {'minutes': 15, 'contexts': ['phone'], 'capacity': 'low'}
        self.assertEqual(self.service.choose(context)['selected']['id'], high['id'])
        self.ok(self.cmd(low, 'edit', {'priority': 3}))
        self.restart()
        self.assertEqual(self.service.choose(context)['selected']['id'], low['id'])
        self.assertEqual(len(self.service.query({'available': True})), 5)

    def test_g5_plan_does_not_invent_missing_human_purpose(self):
        project = self.item('project', decision_needed=True, decision_question='What outcome matters?')
        project = self.ok(self.cmd(project, 'plan', {'plan_steps': ['Explore options', 'Choose approach']}))
        self.assertNotIn('purpose', project)
        project = self.ok(self.cmd(project, 'plan', {'purpose': 'Reduce recurring effort', 'outcome': 'Verified reduction',
            'completion_criteria': 'Measure improvement', 'decision_needed': False}))
        self.restart()
        self.assertEqual(self.current(project)['purpose'], 'Reduce recurring effort')
        self.assertTrue(self.service.review_state()['gaps'])

    def test_g6_dates_keep_distinct_meanings(self):
        appointment = self.item('calendar', starts_at='2030-01-01T10:00:00+00:00', ends_at='2030-01-01T11:00:00+00:00')
        deadline = self.item(due_at='2030-01-03')
        possibility = self.item('possibility', review_at='2030-01-02', decision_at='2030-01-05')
        self.restart()
        self.assertNotIn('due_at', self.current(appointment))
        self.assertNotIn('review_at', self.current(deadline))
        self.assertNotIn('due_at', self.current(possibility))
        self.assertEqual(self.current(possibility)['commitment'], 'proposed')

    def test_g10_source_revision_and_human_correction_invalidate_only_dependent_material(self):
        source = self.capture('Source v1', {'provider': 'synthetic', 'revision': '1'})
        dependent = self.item(completion_criteria='Verified material', source_versions={source['id']: 1})
        independent = self.item()
        dependent = self.ok(self.cmd(dependent, 'put_material', {'content': 'Dependent', 'source_versions': {source['id']: 1}}))
        independent = self.ok(self.cmd(independent, 'put_material', {'content': 'Independent'}))
        self.n += 1
        self.ok(self.service.revise_source('felix', str(self.n), source['id'], {'provider': 'synthetic', 'revision': '2'}, text='Source v2'))
        self.restart()
        self.assertFalse(self.service.materials(dependent['id'])[0]['valid'])
        self.assertTrue(self.service.materials(independent['id'])[0]['valid'])
        self.assertEqual(self.cmd(dependent, 'assess_result', {'satisfied': True, 'evidence': 'Old check', 'source_versions': {source['id']: 1}})['error'], 'source_version_stale')
        self.assertEqual(self.cmd(dependent, 'assess_result', {'satisfied': True, 'evidence': 'Missing source'})['error'], 'source_coverage_incomplete')
        self.assertTrue(self.service.pending_events('gtd-review', 'local'))
        corrected = self.ok(self.cmd(independent, 'edit', {'title': 'Human position'}))
        self.assertFalse(self.service.materials(corrected['id'])[0]['valid'])
        self.assertEqual(self.cmd(corrected, 'edit', {'title': 'Agent replaces position'}, actor='gtd-felix')['error'], 'human_position_protected')

    def test_material_data_correction_preserves_mandate_but_invalidates_old_result(self):
        item, mandate = self.grant(self.item(completion_criteria='Checked data'))
        item = self.ok(self.cmd(item, 'put_material', {'content': 'Old calculation', 'mandate_id': mandate}, actor='gtd-felix'))
        old = self.service.materials(item['id'])[0]
        item = self.ok(self.cmd(item, 'edit', {'notes': 'Independent annotation'}))
        self.assertTrue(self.service.materials(item['id'])[0]['valid'])
        independent = self.item('reference')
        self.ok(self.cmd(independent, 'edit', {'text': 'Independent note'}))
        self.assertTrue(self.service.materials(item['id'])[0]['valid'])
        item = self.ok(self.cmd(item, 'edit', {'text': 'Corrected numerical input'}))
        self.restart()
        self.assertFalse(self.service.materials(item['id'])[0]['valid'])
        self.assertEqual(self.cmd(item, 'assess_result', {'satisfied': True, 'evidence': 'Old calculation',
            'material_id': old['id'], 'material_version': old['version']})['error'], 'material_stale_or_missing')
        self.assertTrue(self.service.authorize('gtd-felix', 'local_work', item['id'], mandate)['allowed'])
        item = self.ok(self.cmd(item, 'put_material', {'content': 'Corrected calculation', 'mandate_id': mandate}, actor='gtd-felix'))
        self.assertTrue(self.service.materials(item['id'])[-1]['valid'])
        # Restoring the old text cannot resurrect the previous human generation.
        item = self.ok(self.cmd(item, 'edit', {'text': 'Synthetic note'}))
        self.assertFalse(self.service.materials(item['id'])[0]['valid'])
        self.assertTrue(self.service.authorize('gtd-felix', 'local_work', item['id'], mandate)['allowed'])

    def test_material_legacy_basis_without_working_text_is_stale(self):
        item = self.item(completion_criteria='Checked data')
        legacy_basis = self.service._basis(item['id'])
        legacy_basis.pop('text')
        with patch.object(self.service, '_basis', return_value=legacy_basis):
            item = self.ok(self.cmd(item, 'put_material', {'content': 'Legacy draft'}))
        self.restart()
        self.assertFalse(self.service.materials(item['id'])[0]['valid'])
        item = self.ok(self.cmd(item, 'put_material', {'content': 'Current draft'}))
        self.assertTrue(self.service.materials(item['id'])[-1]['valid'])

    def test_material_versions_human_authorship_and_assessment_not_file_presence(self):
        item = self.item(completion_criteria='Checked output')
        item = self.ok(self.cmd(item, 'put_material', {'content': 'Human draft'}))
        material = self.service.materials(item['id'])[0]
        self.assertEqual(self.cmd(item, 'put_material', {'content': 'Agent overwrite', 'material_id': material['id']}, actor='gtd-felix')['error'], 'human_material_protected')
        item = self.ok(self.cmd(item, 'put_material', {'content': 'Human corrected', 'material_id': material['id']}))
        self.assertEqual([m['version'] for m in self.service.materials(item['id'])], [1, 2])
        self.assertEqual(item['status'], 'active')
        self.assertEqual(self.cmd(item, 'assess_result', {'satisfied': True})['error'], 'assessment_evidence_required')
        checked = self.ok(self.cmd(item, 'assess_result', {'satisfied': True, 'evidence': 'Compared against criteria',
            'material_id': material['id'], 'material_version': 2}))
        self.assertEqual(checked['status'], 'done')

    def test_g4_review_coverage_silent_projects_responsibilities_pause_and_return(self):
        source = self.capture('Source', {'provider': 'synthetic'})
        project = self.item('project')
        responsibility = self.item('responsibility')
        decision = self.item('possibility', decision_needed=True, decision_question='Adopt?', review_at='2030-01-02')
        self.ok(self.cmd(None, 'set_attention', {'paused': True, 'notify': False, 'return_at': '2030-01-02'}))
        partial = self.ok(self.cmd(None, 'review', {'views': ['project'], 'return_at': '2030-01-02'}, actor='gtd-felix'))['review']
        self.assertFalse(partial['operational_complete'])
        self.assertIn(source['id'], partial['missing_sources'])
        self.restart()
        state = self.service.review_state()
        self.assertFalse(state['notification_allowed'])
        self.assertTrue(state['human_decisions'])
        self.assertTrue({project['id'], responsibility['id']} <= {gap['item_id'] for gap in state['gaps']})
        self.assertEqual(state['last_review']['return_at'], '2030-01-02')
        full = self.ok(self.cmd(None, 'review', {'source_coverage': {source['id']: 1}}, actor='gtd-felix'))['review']
        self.assertTrue(full['operational_complete'])
        self.assertTrue(full['human_decision_pending'])
        self.assertEqual(self.current(decision)['commitment'], 'proposed')
        self.assertEqual(self.service.pending_events('gtd-review', 'local'), [])

    def test_g8_export_restore_all_semantics_and_recovery_blocks_agents(self):
        project, mandate = self.grant(self.item('project', completion_criteria='Checked'))
        project = self.ok(self.cmd(project, 'put_material', {'content': 'Synthetic preparation'}, actor='gtd-felix'))
        self.ok(self.cmd(None, 'set_attention', {'paused': True, 'return_at': '2030-01-02'}))
        self.ok(self.cmd(None, 'review', {}, actor='gtd-felix'))
        archive = self.root / 'export.zip'
        self.service.export(archive)
        restored = GTDService.restore(archive, self.root / 'restored')
        try:
            self.assertEqual(restored.mandates(), self.service.mandates())
            self.assertEqual(restored.materials(project['id']), self.service.materials(project['id']))
            self.assertEqual(restored.review_state(), self.service.review_state())
            self.assertTrue(restored.recovery_required)
            self.assertEqual(restored.authorize('gtd-felix', 'local_work', project['id'], mandate)['reason'], 'recovery_required')
            self.assertEqual(restored.actor_role('worker'), 'executor')
            for material in restored.materials(project['id']):
                raw = (restored.data_dir / material['original']['path']).read_bytes()
                self.assertEqual(hashlib.sha256(raw).hexdigest(), material['original']['sha256'])
        finally:
            restored.close()

    def test_semantic_idempotency_and_atomic_material_receipt_failure(self):
        item = self.item()
        command = {'operation_id': 'stable-material', 'action': 'put_material', 'item_id': item['id'],
            'expected_version': item['version'], 'fields': {'content': 'Only once'}}
        with patch.object(self.service, '_record', side_effect=sqlite3.OperationalError('synthetic fail')):
            self.assertEqual(self.service.execute('felix', command)['status'], 'uncertain')
        self.restart()
        self.assertEqual(self.service.materials(item['id']), [])
        self.ok(self.service.execute('felix', command))
        self.restart()
        self.assertEqual(self.service.execute('felix', command)['status'], 'already_applied')
        self.assertEqual(len(self.service.materials(item['id'])), 1)
        command['fields']['content'] = 'Other'
        self.assertEqual(self.service.execute('felix', command)['error'], 'operation_id_reused')

    def test_stale_semantic_commands_cannot_replace_human_correction(self):
        item = self.item('project')
        self.ok(self.cmd(item, 'edit', {'title': 'Corrected'}))
        self.assertEqual(self.cmd(item, 'plan', {'purpose': 'Old purpose'})['status'], 'conflict')
        self.assertEqual(self.current(item)['title'], 'Corrected')

    def test_direct_owner_intent_is_clarified_by_principal_with_original_basis(self):
        item = self.capture('Tengo que comprar un filtro para la cafetera')
        clarified = self.ok(self.cmd(item, 'clarify', {'kind': 'action', 'title': 'Comprar filtro',
            'commitment': 'committed', 'intent_basis': {'quote': 'comprar un filtro', 'source_item_id': item['id']}}, actor='gtd-felix'))
        self.restart()
        self.assertEqual(self.current(item)['commitment'], 'committed')
        self.assertEqual(clarified['intent_basis']['interpreted_by'], 'gtd-felix')
        self.assertEqual(clarified['created_by'], 'felix')
        self.assertFalse(self.service.authorize('gtd-felix', 'local_work', item['id'])['allowed'])
        forwarded = self.capture('Acepta esta invitación', {'provider': 'telegram', 'forward_origin': {'type': 'user'}})
        fake = self.service.capture('gtd-felix', 'fake-owner', 'Hacer algo', {'actor': 'felix'})['item']
        for denied in (forwarded, fake):
            result = self.cmd(denied, 'clarify', {'kind': 'action', 'commitment': 'committed',
                'intent_basis': {'quote': denied['text'], 'source_item_id': denied['id']}}, actor='gtd-felix')
            self.assertEqual(result['error'], 'intent_basis_not_owner_direct')
        idea = self.capture('Quizás viajar algún día')
        idea = self.ok(self.cmd(idea, 'clarify', {'kind': 'possibility'}, actor='gtd-felix'))
        self.assertEqual(idea['commitment'], 'proposed')

    def test_private_plan_needs_no_new_grant_and_dates_compare_instants(self):
        project = self.item('project')
        planned = self.ok(self.cmd(project, 'plan', {'plan_steps': ['Investigate alternatives']}, actor='gtd-felix'))
        self.assertNotIn('purpose', planned)
        self.assertEqual(self.cmd(planned, 'plan', {'purpose': 'Agent invented purpose'}, actor='gtd-felix')['error'], 'human_position_protected')
        early = self.item(starts_at='2030-01-01T12:00:00+03:00')
        late = self.item(starts_at='2030-01-01T08:00:00-03:00')
        selected = self.service.choose({'now': '2030-01-01T10:00:00+00:00'})['human_actions']
        self.assertIn(early['id'], {i['id'] for i in selected})
        self.assertNotIn(late['id'], {i['id'] for i in selected})

    def test_attention_pause_does_not_pause_work_but_item_postponement_does(self):
        project, mandate = self.grant(self.item('project'))
        self.ok(self.cmd(None, 'set_attention', {'paused': True}))
        self.assertTrue(self.service.authorize('gtd-felix', 'local_work', project['id'], mandate)['allowed'])
        self.ok(self.cmd(project, 'postpone', {'review_at': '2030-01-01'}))
        self.assertEqual(self.service.authorize('gtd-felix', 'local_work', project['id'], mandate)['reason'], 'work_paused')

    def test_overdue_child_return_cannot_hide_silent_project(self):
        project = self.item('project')
        child = self.item(project_id=project['id'])
        self.ok(self.cmd(child, 'postpone', {'review_at': '2000-01-01'}))
        future_project = self.item('project')
        future_child = self.item(project_id=future_project['id'])
        self.ok(self.cmd(future_child, 'postpone', {'review_at': '2999-01-01'}))
        self.restart()
        gaps = {gap['item_id']: gap['reason'] for gap in self.service.review_state()['gaps']}
        self.assertEqual(gaps[project['id']], 'due_return')
        self.assertNotIn(future_project['id'], gaps)

    def test_mandate_does_not_revive_when_human_meaning_changes_back(self):
        project, mandate = self.grant(self.item('project', title='Original'))
        changed = self.ok(self.cmd(project, 'edit', {'title': 'Corrected'}))
        restored = self.ok(self.cmd(changed, 'edit', {'title': 'Original'}))
        self.restart()
        self.assertEqual(self.service.authorize('gtd-felix', 'local_work', restored['id'], mandate)['reason'], 'mandate_stale')


    def own_operational_children(self):
        parent = self.item('project', completion_criteria='Guide checked and Lara confirms', text='09:00 to 12:00 provisional')
        parent, mandate = self.grant(parent)
        children = []
        for kind in ('action', 'waiting'):
            fields = {'kind':kind, 'title':'Own '+kind, 'mandate_id':mandate,
                'capability':'local_work', 'completion_criteria':'Check provisional 09:00 to 12:00'}
            if kind == 'waiting': fields['waiting_for']='Lara confirms provisional 09:00 to 12:00'
            children.append(self.ok(self.cmd(self.current(parent),'derive',fields,actor='gtd-felix')))
        parent = self.ok(self.cmd(self.current(parent),'edit',{'text':'10:00 to 13:00 provisional; Lara still pending'}))
        return parent, mandate, children

    def test_own_operational_fields_follow_corrected_source_preserving_history(self):
        parent, mandate, children = self.own_operational_children()
        for child in children:
            fields={'completion_criteria':'Check provisional 10:00 to 13:00'}
            if child['kind']=='waiting': fields['waiting_for']='Lara confirms provisional 10:00 to 13:00'
            changed=self.ok(self.cmd(child,'edit',fields,actor='gtd-felix'))
            self.assertEqual(changed['version'],2)
            self.assertEqual(changed['parent_id'],parent['id'])
            self.assertEqual(changed['commitment'],'committed')
            self.assertEqual(changed['status'],'active')
            row=self.service.store.db.execute('SELECT before_patch FROM operations WHERE operation_id=?',(str(self.n),)).fetchone()
            self.assertIn('09:00 to 12:00',row[0])
            _,versions=self.service._item(child['id'])
            self.assertEqual(versions['completion_criteria']['actor'],'gtd-felix')
        self.restart()
        self.assertEqual(self.current(parent)['completion_criteria'],'Guide checked and Lara confirms')
        self.assertTrue(self.service.authorize('gtd-felix','local_work',children[0]['id'],mandate)['allowed'])

    def test_own_operational_edit_protects_owner_fields_and_root(self):
        parent, _, children=self.own_operational_children()
        for child in children:
            field='waiting_for' if child['kind']=='waiting' else 'completion_criteria'
            adopted=self.ok(self.cmd(child,'edit',{field:'Human criterion'}))
            result=self.cmd(adopted,'edit',{field:'Principal replacement'},actor='gtd-felix')
            self.assertEqual(result['error'],'human_position_protected')
        self.assertEqual(self.cmd(parent,'edit',{'completion_criteria':'Replacement'},actor='gtd-felix')['error'],'human_position_protected')

    def test_own_operational_edit_rejects_other_actor_and_scope_changes(self):
        parent, _, children=self.own_operational_children();child=children[0]
        for value in ('', '   ', None):
            self.assertEqual(self.cmd(child,'edit',{'completion_criteria':value},actor='gtd-felix')['status'],'rejected')
        for actor in ('worker','other-principal'):
            self.assertEqual(self.cmd(child,'edit',{'completion_criteria':'New'},actor=actor)['status'],'rejected')
        for field,value in [('kind','reference'),('commitment','proposed'),('project_id','fake'),('parent_id','fake'),('executor','worker')]:
            result=self.cmd(child,'edit',{'completion_criteria':'New',field:value},actor='gtd-felix')
            self.assertEqual(result['status'],'rejected',result)
        self.assertEqual(self.cmd(child,'edit',{'waiting_for':'New'},actor='gtd-felix')['status'],'rejected')

    def test_own_operational_edit_requires_real_descendant_and_active_mandate(self):
        parent, mandate, children=self.own_operational_children()
        unrelated=self.item('project')
        fake=self.ok(self.cmd(unrelated,'derive',{'kind':'action','title':'Outside',
            'commitment':'proposed','project_id':parent['id'],'completion_criteria':'Old'},actor='gtd-felix'))
        self.assertEqual(self.cmd(fake,'edit',{'completion_criteria':'New'},actor='gtd-felix')['status'],'rejected')
        self.ok(self.cmd(self.current(parent),'revoke_mandate',{'mandate_id':mandate}))
        self.assertEqual(self.cmd(children[0],'edit',{'completion_criteria':'New'},actor='gtd-felix')['error'],'mandate_revoked')

    def test_owner_created_child_never_becomes_principal_owned(self):
        parent, mandate, _=self.own_operational_children()
        child=self.ok(self.cmd(self.current(parent),'derive',{'kind':'waiting','title':'Human wait',
            'mandate_id':mandate,'waiting_for':'Human condition','completion_criteria':'Human criterion'}))
        self.assertEqual(self.cmd(child,'edit',{'waiting_for':'Replacement'},actor='gtd-felix')['error'],'human_position_protected')



    def test_owner_same_value_adoption_and_undo_preserve_protection_atomically(self):
        _, _, children = self.own_operational_children()
        for child in children:
            field = 'waiting_for' if child['kind'] == 'waiting' else 'completion_criteria'
            original = child[field]
            adopted = self.ok(self.cmd(child, 'edit', {field: original}))
            operation = str(self.n)
            self.assertEqual(adopted[field], original)
            self.assertEqual(self.service._item(child['id'])[1][field]['actor'], 'felix')
            result = self.cmd(adopted, 'edit', {field: 'Changed by principal', 'notes': 'No partial write'}, actor='gtd-felix')
            self.assertEqual(result['error'], 'human_position_protected')
            self.assertEqual(self.current(child), adopted)
            restored = self.ok(self.cmd(adopted, 'undo', {'operation_id': operation}))
            self.assertEqual(restored[field], original)
            self.assertEqual(self.service._item(child['id'])[1][field]['actor'], 'felix')
            result = self.cmd(restored, 'edit', {field: 'Changed after undo', 'notes': 'No partial write'}, actor='gtd-felix')
            self.assertEqual(result['error'], 'human_position_protected')
            self.assertEqual(self.current(child), restored)
            owner_version = self.service._item(child['id'])[1][field]['version']
            self.ok(self.cmd(restored, 'edit', {field: original}))
            self.assertEqual(self.service._item(child['id'])[1][field]['version'], owner_version)
        self.restart()
        for child in children:
            field = 'waiting_for' if child['kind'] == 'waiting' else 'completion_criteria'
            self.assertEqual(self.service._item(child['id'])[1][field]['actor'], 'felix')


if __name__ == '__main__':
    unittest.main()
