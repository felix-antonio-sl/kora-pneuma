"""Real Store/domain, synthetic provider evidence; no network or accounts."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
import copy
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from gtd_felix.effects import ExternalEffects
from gtd_felix.service import GTDService


class EffectsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.service = GTDService(self.root / 'data', executor_actors=['worker'])
        self.effects = ExternalEffects(self.service)
        self.item = self.service.capture('felix', 'capture', 'Synthetic source; body is not authority')['item']
        self.mime = 'Message-ID: <stable-synthetic@example.invalid>\nFrom: sender@example.invalid\nTo: recipient@example.invalid\nSubject: Prepared\n\nSynthetic content\n'
        receipt = self.service.execute('gtd-felix', {'operation_id': 'material', 'action': 'put_material',
            'item_id': self.item['id'], 'expected_version': self.item['version'], 'fields': {'content': self.mime}})
        self.assertEqual(receipt['status'], 'applied', receipt)
        self.item = receipt['item']
        m = self.service.materials(self.item['id'])[0]
        self.material = {'id': m['id'], 'version': m['version'], 'sha256': m['original']['sha256']}
        self.expiry = (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat()

    def tearDown(self):
        self.service.close()
        self.temp.cleanup()

    def proposal(self, **changes):
        return dict({'provider': 'gmail', 'account': 'synthetic-account', 'action': 'draft_create',
            'item_id': self.item['id'], 'target': {'id': None}, 'payload': {'mime': self.mime,
            'message_id': '<stable-synthetic@example.invalid>'}, 'material': self.material, 'expires_at': self.expiry}, **changes)

    def propose(self, operation='proposal', **changes):
        result = self.effects.propose('gtd-felix', operation, self.proposal(**changes))
        self.assertEqual(result['status'], 'proposed', result)
        return result['effect']

    def authorize(self, effect, operation='authorize'):
        result = self.effects.authorize('felix', operation, effect['id'], effect['proposal_hash'])
        self.assertEqual(result['status'], 'authorized', result)

    def observation(self, effect, status='ack', **extra):
        p = effect['proposal']
        return dict({**{k: p[k] for k in ('provider', 'account', 'action', 'target')},
            'request_hash': effect['proposal_hash'], 'status': status, 'remote_id': 'remote-draft',
            'evidence_reference': 'fixture://verified-provider-response'}, **extra)

    def readback(self, effect, remote='remote-draft'):
        p = effect['proposal']
        return {**{k: p[k] for k in ('provider', 'account', 'action', 'target')},
            'request_hash': effect['proposal_hash'], 'remote_id': remote, 'content_verified': True,
            'fixed_identity': p['payload'].get('message_id', p['target']['id'])}

    def test_proposal_is_not_permission_and_source_cannot_supply_actor(self):
        effect = self.propose(action='send')
        self.assertEqual(self.effects.begin_dispatch(effect['id'])['error'], 'external_authorization_required')
        self.assertEqual(self.effects.authorize('gtd-felix', 'self-authorize', effect['id'], effect['proposal_hash'])['error'], 'owner_required')
        self.assertEqual(self.effects.propose('worker', 'worker-proposal', self.proposal())['error'], 'actor_forbidden')
        self.assertEqual(self.effects.propose('gtd-felix', 'forged-owner', self.proposal(actor='felix'))['error'], 'invalid_proposal')
        self.assertEqual(self.effects.grant_draft_preparation('gtd-felix', 'self-grant', 'synthetic-account', 'gtd-felix', self.expiry)['error'], 'owner_required')
        with self.assertRaises(ValueError):
            self.effects.list('worker')
        self.assertEqual(len(self.effects.list('gtd-felix')), 1)
        self.authorize(effect)
        self.assertEqual(self.effects.begin_dispatch(effect['id'])['status'], 'dispatch')

    def test_standing_drafts_do_not_grant_send_calendar_or_other_account(self):
        grant = self.effects.grant_draft_preparation('felix', 'grant', 'synthetic-account', 'gtd-felix', self.expiry)
        self.assertEqual(grant['status'], 'granted')
        for action in ('draft_create', 'draft_update'):
            effect = self.propose(action, action=action, target={'id': 'draft-existing'} if action == 'draft_update' else {'id': None},
                **({'expected_remote_version': 'opaque-before-fingerprint'} if action == 'draft_update' else {}))
            self.assertEqual(self.effects.begin_dispatch(effect['id'])['status'], 'dispatch')
        for name, changes in [('send', {'action': 'send'}), ('other-account', {'account': 'different-account'}),
                ('calendar', {'provider': 'calendar', 'action': 'insert', 'payload': {'summary': 'Meeting'}, 'material': None})]:
            effect = self.propose(name, **changes)
            self.assertEqual(self.effects.begin_dispatch(effect['id'])['error'], 'external_authorization_required')

    def test_replay_hash_conflict_and_concurrent_dispatch_only_one_io_permission(self):
        effect = self.propose()
        repeat = self.effects.propose('gtd-felix', 'proposal', self.proposal())
        self.assertTrue(repeat['duplicate'])
        self.assertEqual(repeat['effect'], effect)
        self.assertEqual(self.effects.propose('gtd-felix', 'proposal', self.proposal(account='changed'))['error'], 'operation_id_conflict')
        self.assertEqual(self.effects.authorize('felix', 'wrong-hash', effect['id'], '0' * 64)['error'], 'proposal_hash_mismatch')
        self.authorize(effect)
        with ThreadPoolExecutor(2) as pool:
            results = list(pool.map(lambda _: self.effects.begin_dispatch(effect['id']), range(2)))
        self.assertEqual(sorted(r['status'] for r in results), ['already_dispatched', 'dispatch'])
        self.service.close()
        self.service = GTDService(self.root / 'data', executor_actors=['worker'])
        self.effects = ExternalEffects(self.service)
        self.assertEqual(self.effects.begin_dispatch(effect['id'])['status'], 'already_dispatched')
        self.assertEqual(len(self.effects.pending()), 1)
        self.assertTrue(self.effects.authorize('felix', 'authorize', effect['id'], effect['proposal_hash'])['duplicate'])

    def test_material_change_and_human_source_correction_invalidate_old_authorization(self):
        for case in ('material', 'source', 'date'):
            with self.subTest(case=case):
                effect = self.propose(case)
                self.authorize(effect, 'authorize-' + case)
                item = self.service.get_item(self.item['id'])
                if case == 'material':
                    fields = {'content': self.mime, 'material_id': self.material['id']}
                    action = 'put_material'
                elif case == 'source':
                    fields, action = {'text': 'Changed human source'}, 'edit'
                else:
                    fields, action = {'due_at': '2027-01-01T10:00:00+00:00'}, 'edit'
                result = self.service.execute('felix', {'operation_id': 'change-' + case, 'action': action,
                    'item_id': item['id'], 'expected_version': item['version'], 'fields': fields})
                self.assertEqual(result['status'], 'applied', result)
                rejected = self.effects.begin_dispatch(effect['id'])
                self.assertEqual(rejected['status'], 'rejected')
                self.assertNotIn('dispatch', self.effects.get('felix', effect['id']))
                # Prepare a fresh independent material and bases for the next case.
                current = self.service.get_item(self.item['id'])
                self.service.execute('felix', {'operation_id': 'fresh-' + case, 'action': 'put_material',
                    'item_id': current['id'], 'expected_version': current['version'], 'fields': {'content': self.mime}})
                m = self.service.materials(current['id'])[-1]
                self.material = {'id': m['id'], 'version': m['version'], 'sha256': m['original']['sha256']}

    def test_declared_material_dependency_date_change_is_relevant_notes_are_not(self):
        source = self.service.capture('felix', 'external-source', 'Meeting source')['item']
        item = self.service.get_item(self.item['id'])
        self.service.execute('gtd-felix', {'operation_id': 'linked-material', 'action': 'put_material',
            'item_id': item['id'], 'expected_version': item['version'],
            'fields': {'content': self.mime, 'source_versions': {source['id']: 1}}})
        m = self.service.materials(item['id'])[-1]
        self.material = {'id': m['id'], 'version': m['version'], 'sha256': m['original']['sha256']}
        effect = self.propose()
        self.authorize(effect)
        self.assertIn(source['id'], effect['bases'])
        self.service.execute('felix', {'operation_id': 'source-date', 'action': 'edit', 'item_id': source['id'],
            'expected_version': source['version'], 'fields': {'due_at': '2027-02-01T10:00:00+00:00'}})
        self.assertEqual(self.effects.begin_dispatch(effect['id'])['error'], 'source_basis_changed')
        newer = self.propose('new-date')
        self.authorize(newer, 'new-date-authorize')
        current = self.service.get_item(source['id'])
        result = self.service.execute('felix', {'operation_id': 'compatible-note', 'action': 'edit', 'item_id': source['id'],
            'expected_version': current['version'], 'fields': {'notes': 'Independent note'}})
        self.assertEqual(result['status'], 'applied', result)
        self.assertEqual(self.effects.begin_dispatch(newer['id'])['status'], 'dispatch')

    def test_ack_is_pending_confirmation_must_match_exact_destination(self):
        effect = self.propose()
        self.authorize(effect)
        self.effects.begin_dispatch(effect['id'])
        ack = self.observation(effect)
        self.assertEqual(self.effects.observe(effect['id'], ack)['status'], 'acknowledged')
        self.assertEqual(len(self.effects.pending()), 1)
        confirmed = self.observation(effect, 'confirmed', readback=self.readback(effect))
        for key, value in [('account', 'foreign-account'), ('request_hash', 'foreign-hash'), ('target', {'id': 'foreign-target'})]:
            bad = copy.deepcopy(confirmed)
            bad['readback'][key] = value
            self.assertEqual(self.effects.observe(effect['id'], bad)['status'], 'rejected')
        self.assertEqual(self.effects.observe(effect['id'], confirmed)['status'], 'confirmed')
        self.assertTrue(self.effects.observe(effect['id'], confirmed)['duplicate'])
        self.assertEqual(self.effects.pending(), [])
        self.assertEqual(self.effects.begin_dispatch(effect['id'])['status'], 'already_dispatched')

    def test_lost_ack_reconciles_fixed_identity_not_empty_search(self):
        effect = self.propose(action='send')
        self.authorize(effect)
        self.effects.begin_dispatch(effect['id'])
        self.effects.observe(effect['id'], self.observation(effect, 'uncertain', remote_id=None))
        empty = self.observation(effect, 'no_dispatch', proof={'kind': 'not_found'})
        self.assertEqual(self.effects.observe(effect['id'], empty)['error'], 'no_dispatch_not_proven')
        confirmed = self.observation(effect, 'confirmed', readback=self.readback(effect))
        bad = copy.deepcopy(confirmed)
        bad['readback']['fixed_identity'] = '<other@example.invalid>'
        self.assertEqual(self.effects.observe(effect['id'], bad)['error'], 'fixed_identity_required_without_ack')
        self.assertEqual(self.effects.observe(effect['id'], confirmed)['status'], 'confirmed')

    def test_revocation_before_and_after_dispatch_preserves_uncertainty(self):
        grant = self.effects.grant_draft_preparation('felix', 'grant', 'synthetic-account', 'gtd-felix', self.expiry)['grant']
        first, second = self.propose('first'), self.propose('second')
        self.effects.begin_dispatch(first['id'])
        self.effects.revoke('felix', 'revoke-grant', grant_id=grant['id'])
        self.assertEqual(self.effects.begin_dispatch(second['id'])['error'], 'external_authorization_required')
        self.assertEqual(self.effects.get('felix', first['id'])['status'], 'dispatching')
        self.assertTrue(self.effects.get('felix', first['id'])['revoked'])
        confirmed = self.observation(first, 'confirmed', readback=self.readback(first))
        self.assertEqual(self.effects.observe(first['id'], confirmed)['status'], 'confirmed')
        self.effects.revoke('felix', 'revoke-effect', effect_id=second['id'])
        self.assertEqual(self.effects.begin_dispatch(second['id'])['error'], 'effect_resolved')

    def test_proven_no_request_does_not_renew_dispatch_permission(self):
        effect = self.propose()
        self.authorize(effect)
        dispatch = self.effects.begin_dispatch(effect['id'])['effect']['dispatch']
        observation = self.observation(effect, 'no_dispatch', proof={'kind': 'request_not_sent', 'dispatch_id': dispatch['id']})
        self.assertEqual(self.effects.observe(effect['id'], observation)['status'], 'no_dispatch')
        self.assertEqual(self.effects.pending(), [])
        self.assertEqual(self.effects.begin_dispatch(effect['id'])['status'], 'already_dispatched')
        self.assertIn('dispatch', self.effects.get('felix', effect['id']))

    def test_restore_blocks_owner_dispatch_but_allows_truthful_reconciliation(self):
        waiting, dispatched = self.propose('waiting'), self.propose('dispatched')
        self.authorize(waiting, 'authorize-waiting')
        self.authorize(dispatched, 'authorize-dispatched')
        self.effects.begin_dispatch(dispatched['id'])
        archive = self.root / 'backup.zip'
        self.service.export(archive)
        restored = GTDService.restore(archive, self.root / 'restored')
        try:
            effects = ExternalEffects(restored)
            self.assertTrue(restored.recovery_required)
            self.assertEqual(effects.begin_dispatch(waiting['id'])['error'], 'recovery_required')
            self.assertEqual(effects.authorize('felix', 'after-restore', waiting['id'], waiting['proposal_hash'])['status'], 'rejected')
            self.assertEqual(effects.begin_dispatch(dispatched['id'])['status'], 'already_dispatched')
            self.assertEqual(effects.observe(dispatched['id'], self.observation(dispatched, 'confirmed', readback=self.readback(dispatched)))['status'], 'confirmed')
            self.assertTrue(restored.recovery_required)
        finally:
            restored.close()

    def test_restart_at_each_durable_boundary_never_repeats_io(self):
        def restart():
            self.service.close()
            self.service = GTDService(self.root / 'data', executor_actors=['worker'])
            self.effects = ExternalEffects(self.service)
        effect = self.propose()
        restart()
        self.assertTrue(self.effects.propose('gtd-felix', 'proposal', self.proposal())['duplicate'])
        self.authorize(effect)
        restart()
        self.assertTrue(self.effects.authorize('felix', 'authorize', effect['id'], effect['proposal_hash'])['duplicate'])
        self.assertEqual(self.effects.begin_dispatch(effect['id'])['status'], 'dispatch')
        restart()  # crash before knowing whether the request left
        self.assertEqual(self.effects.begin_dispatch(effect['id'])['status'], 'already_dispatched')
        self.assertEqual(self.effects.pending()[0]['status'], 'dispatching')
        ack = self.observation(effect)
        self.effects.observe(effect['id'], ack)
        restart()  # ACK persisted, but confirmation has not happened
        self.assertTrue(self.effects.observe(effect['id'], ack)['duplicate'])
        self.assertEqual(self.effects.pending()[0]['status'], 'acknowledged')
        confirmation = self.observation(effect, 'confirmed', readback=self.readback(effect))
        self.effects.observe(effect['id'], confirmation)
        restart()  # confirmation response lost
        self.assertTrue(self.effects.observe(effect['id'], confirmation)['duplicate'])
        self.assertEqual(self.effects.pending(), [])
        self.assertEqual(self.effects.begin_dispatch(effect['id'])['status'], 'already_dispatched')

    def test_invalid_content_expiry_and_malformed_evidence_do_not_dispatch(self):
        forged = dict(self.material, sha256='0' * 64)
        self.assertEqual(self.effects.propose('gtd-felix', 'forged-material', self.proposal(material=forged))['error'], 'material_not_current')
        self.assertEqual(self.effects.propose('gtd-felix', 'missing-material', self.proposal(material=None))['error'], 'material_required')
        deep = {}
        node = deep
        for _ in range(20):
            node['next'] = {}
            node = node['next']
        self.assertEqual(self.effects.propose('gtd-felix', 'deep-payload', self.proposal(payload=deep))['error'], 'payload_too_complex')
        effect = self.propose()
        self.authorize(effect)
        with patch('gtd_felix.effects._now', return_value=datetime.now(timezone.utc) + timedelta(days=1)):
            self.assertEqual(self.effects.begin_dispatch(effect['id'])['error'], 'proposal_expired')
        self.assertNotIn('dispatch', self.effects.get('felix', effect['id']))
        other = self.propose('valid')
        self.authorize(other, 'authorize-valid')
        self.effects.begin_dispatch(other['id'])
        self.assertEqual(self.effects.observe(other['id'], [])['error'], 'invalid_observation')
        self.assertEqual(self.effects.observe(other['id'], self.observation(other, 'confirmed'))['error'], 'exact_readback_required')
        self.assertEqual(self.effects.observe(other['id'], self.observation(other, 'confirmed', readback=[]))['error'], 'exact_readback_required')
        self.assertEqual(len(self.effects.pending()), 1)

    def test_conditional_412_is_terminal_only_for_exact_unacknowledged_write(self):
        effect = self.propose(provider='calendar', action='update', payload={'summary': 'Changed'},
            material=None, target={'id': 'event-1'}, expected_remote_version='"before"')
        self.authorize(effect)
        dispatch = self.effects.begin_dispatch(effect['id'])['effect']['dispatch']
        proof = {'kind': 'conditional_write_rejected', 'http_status': 412,
                 'dispatch_id': dispatch['id'], 'expected_remote_version': '"before"'}
        for key, value in [('http_status', 404), ('dispatch_id', 'foreign'), ('expected_remote_version', 'other')]:
            observation = self.observation(effect, 'conflict', proof={**proof, key: value})
            self.assertEqual(self.effects.observe(effect['id'], observation)['error'], 'conditional_rejection_not_proven')
        observation = self.observation(effect, 'conflict', proof=proof)
        self.assertEqual(self.effects.observe(effect['id'], observation)['status'], 'conflict')
        self.assertEqual(self.effects.pending(), [])
        self.assertEqual(self.effects.begin_dispatch(effect['id'])['status'], 'already_dispatched')
        other = self.propose('acked-update', provider='calendar', action='update', payload={'summary': 'Changed'},
            material=None, target={'id': 'event-1'}, expected_remote_version='"before"')
        self.authorize(other, 'authorize-other')
        dispatch = self.effects.begin_dispatch(other['id'])['effect']['dispatch']
        self.effects.observe(other['id'], self.observation(other, remote_id='event-1'))
        self.assertEqual(self.effects.observe(other['id'], self.observation(other, 'conflict',
            proof={**proof, 'dispatch_id': dispatch['id']}))['error'], 'conditional_rejection_not_proven')

    def test_calendar_exact_action_remote_version_and_client_id(self):
        for action in ('update', 'decline', 'delete_copy', 'cancel_event'):
            proposal = self.proposal(provider='calendar', action=action, payload={}, material=None, target={'id': 'event-1'})
            self.assertEqual(self.effects.propose('gtd-felix', action, proposal)['error'], 'remote_version_required')
        effect = self.propose(provider='calendar', action='insert', payload={'summary': 'Synthetic meeting'}, material=None,
                              target={'id': 'client-event-id'})
        self.authorize(effect)
        self.effects.begin_dispatch(effect['id'])
        self.assertEqual(self.effects.observe(effect['id'], self.observation(effect, 'confirmed', remote_id='client-event-id',
            readback=self.readback(effect, 'client-event-id')))['status'], 'confirmed')
        self.assertEqual(self.effects.propose('gtd-felix', 'arbitrary-http', self.proposal(action='POST'))['error'], 'unsupported_effect')


if __name__ == '__main__':
    unittest.main()
