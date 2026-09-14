"""Evaluator regression tests; synthetic fixtures never accredit a model run."""
import copy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch, AsyncMock

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from gtd_felix.service import GTDService

spec = importlib.util.spec_from_file_location('gtd_acceptance_probe', Path(__file__).resolve().parents[2] / 'scripts/gtd_acceptance_probe.py')
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)


def state():
    return {'items': {}, 'operations': [], 'metadata': {}, 'events': [], 'files': {}}


def native_fixture(after, item_id, actor='gtd-felix'):
    after['operations'] = [{'operation_id': 'agent-operation', 'actor': actor,
        'receipt': {'status': 'applied', 'item': after['items'][item_id]}}]
    after['metadata']['execution:state'] = {'jobs': {'job-1': {'id': 'job-1', 'actor': actor,
        'item_id': item_id, 'native': {'provider': 'hermes', 'id': 'synthetic-run', 'profile': 'synthetic-principal'},
        'observations': [{'native_status': 'completed'}], 'terminal': True,
        'progress': [{'operation_id': 'agent-operation'}], 'max_cost_usd': 1, 'charged_cost_usd': .1,
        'max_runtime_seconds': 60, 'observed_runtime_seconds': 1}}}


class AcceptanceProbeTests(unittest.TestCase):
    def test_prepare_has_ten_situations_without_oracle_or_tool_recipe(self):
        self.assertEqual({f'G{i}' for i in range(1,11)}, set(probe.SCENARIOS))
        for scenario in probe.SCENARIOS.values():
            self.assertNotIn('expected', scenario)
            self.assertNotIn('checks', scenario)
            self.assertNotIn('operation_id', scenario['request'])
            self.assertNotIn('gtd_command', scenario['request'])
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'cases.json'
            with patch.object(probe, 'run', side_effect=AssertionError('must not run')):
                self.assertEqual(0, probe.main(['prepare', '--output', str(path)]))
            self.assertEqual(10, len(json.loads(path.read_text())['scenarios']))

    def test_g10_independent_material_never_triggers_source_correction(self):
        objects = [{'id': 'independent', 'materials': [{'id': 'm', 'version': 1,
            'basis': {'independent': {}}, 'original': {'sha256': 'hash'}}]}]
        self.assertEqual(probe.dependent_materials(objects, 'source'), [])
        objects[0]['materials'][0]['basis']['source'] = {'text': 'source-hash'}
        self.assertEqual(probe.dependent_materials(objects, 'source')[0]['material_id'], 'm')

    def g10_resolution_fixture(self):
        before, after = state(), state()
        stamp = '2026-01-01T10:01:00+00:00'
        for key, kind in [('source', 'reference'), ('independent', 'action'), ('decision', 'capture'), ('request', 'action')]:
            after['items'][key] = {'id': key, 'kind': kind, 'status': 'active', 'version': 2,
                'commitment': 'proposed', 'source_revisions': [{}], 'materials': []}
        after['items']['source'].update(text='Corrected 10:00 to 13:00', updated_at='2026-01-01T10:00:00+00:00')
        after['items']['decision'].update(decision_needed=True)
        body = b'Corrected private note'
        material = {'id': 'note', 'version': 2, 'created_at': stamp, 'basis': {'source': {}},
            'original': {'path': 'originals/note', 'sha256': probe.sha(body)}}
        assessment = {'actor': 'gtd-felix', 'satisfied': True, 'evidence': 'Criterion checked',
            'assessed_at': stamp, 'item_version': 2, 'material_id': 'note', 'material_version': 2,
            'source_versions': {'source': 1}}
        request = after['items']['request']
        request.update(version=3, commitment='committed', status='done', completion_criteria='Checked private note',
            materials=[material], assessments=[assessment])
        after['files']['originals/note'] = body
        native_fixture(after, 'request')
        after['operations'][0]['receipt']['item'] = copy.deepcopy(request)
        review = {'actor': 'gtd-felix', 'reviewed_at': stamp, 'human_decision_pending': True,
            'views': ['reference', 'action', 'capture'], 'source_coverage': {key: 1 for key in after['items']}}
        after['metadata']['last_review'] = copy.deepcopy(review)
        after['operations'].extend([
            {'operation_id': 'review', 'actor': 'gtd-felix', 'receipt': {'status': 'applied', 'review': review}},
            {'operation_id': 'correct', 'actor': 'felix', 'receipt': {'status': 'applied', 'item': copy.deepcopy(after['items']['source'])}}])
        after['metadata']['execution:state']['jobs']['job-1']['progress'].append({'operation_id': 'review'})
        evidence = {'aliases': {key: key for key in after['items']},
            'intervention': {'at': '2026-01-01T10:00:00+00:00', 'operation_id': 'correct',
                'item_id': 'source', 'after_version': 2, 'fields': {'text': 'Corrected 10:00 to 13:00'}},
            'materials': {'request': [{**material, 'valid': True}]}}
        return before, after, evidence

    def test_g10_review_requires_authenticated_current_coverage_after_change(self):
        for mode in ('valid-partial', 'old-review', 'no-progress', 'missing-source', 'wrong-source-version', 'missing-view', 'owner-review'):
            with self.subTest(mode=mode):
                before, after, evidence = self.g10_resolution_fixture()
                operation = after['operations'][1]
                review = operation['receipt']['review']
                if mode == 'old-review': review['reviewed_at'] = '2026-01-01T09:59:00+00:00'
                if mode == 'no-progress': after['metadata']['execution:state']['jobs']['job-1']['progress'].pop()
                if mode == 'missing-source': review['source_coverage'].pop('source')
                if mode == 'wrong-source-version': review['source_coverage']['source'] = 2
                if mode == 'missing-view': review['views'].remove('reference')
                if mode == 'owner-review': operation['actor'] = 'felix'
                checks = {c['check']: c['status'] for c in probe.evaluate_snapshots('G10', before, after, evidence)['checks']}
                self.assertEqual(checks['review_after_change'], 'PASS' if mode == 'valid-partial' else 'FAIL')

    def test_g10_private_resolution_requires_current_authentic_assessment_and_semantic_review(self):
        for mode in ('closed', 'gap', 'material-only', 'old-assessment', 'new-item-version', 'stale-material', 'wrong-material-version', 'no-receipt'):
            with self.subTest(mode=mode):
                before, after, evidence = self.g10_resolution_fixture()
                request = after['items']['request']
                assessment = request['assessments'][0]
                if mode == 'gap':
                    assessment.update(satisfied=False, gap='Necessary input missing')
                    request.update(status='active', result_gap=assessment['gap'])
                if mode == 'material-only': request.update(status='active', assessments=[])
                if mode == 'old-assessment': assessment['assessed_at'] = '2026-01-01T09:59:00+00:00'
                if mode == 'new-item-version': request['version'] += 1
                if mode == 'stale-material': evidence['materials']['request'][0]['valid'] = False
                if mode == 'wrong-material-version': assessment['material_version'] = 1
                if mode != 'no-receipt': after['operations'][0]['receipt']['item'] = copy.deepcopy(request)
                else: after['operations'][0]['receipt']['item']['assessments'] = []
                checks = {c['check']: c['status'] for c in probe.evaluate_snapshots('G10', before, after, evidence)['checks']}
                self.assertEqual(checks['private_request_resolved'], 'REVIEW_REQUIRED' if mode in ('closed', 'gap') else 'FAIL')

    def test_g10_revised_material_requires_post_change_causal_basis_and_current_bytes(self):
        for mode in ('valid', 'old-material', 'independent-only', 'invalid', 'unwitnessed'):
            with self.subTest(mode=mode):
                before, after, evidence = self.g10_resolution_fixture()
                material = after['items']['request']['materials'][0]
                if mode == 'old-material': material['created_at'] = '2026-01-01T09:59:00+00:00'
                if mode == 'independent-only': material['basis'] = {'independent': {}}
                if mode == 'invalid': evidence['materials']['request'][0]['valid'] = False
                if mode == 'unwitnessed': after['metadata']['execution:state']['jobs']['job-1']['progress'] = []
                checks = {c['check']: c['status'] for c in probe.evaluate_snapshots('G10', before, after, evidence)['checks']}
                self.assertEqual(checks['dependent_result_revised'], 'PASS' if mode == 'valid' else 'FAIL')

    def test_g10_assessed_coverage_is_review_required_not_automatic_acceptance(self):
        modes = ('valid', 'native-read', 'before-change', 'missing-source', 'stale-source',
            'wrong-basis', 'missing-basis', 'invalid-material', 'wrong-material',
            'prose-only', 'no-authentication', 'native-missing', 'native-wrong-hash')
        for mode in modes:
            with self.subTest(mode=mode):
                before, after, evidence = self.g10_resolution_fixture()
                after['operations'][1]['receipt']['review']['source_coverage'] = {'decision': 1}
                request = after['items']['request']; a = request['assessments'][0]; material = request['materials'][0]
                coverage = {sid: len(item['source_revisions']) for sid, item in after['items'].items()}
                a['source_versions'] = dict(coverage)
                a['resolution_basis'] = {sid: {'source': item.get('source', {}),
                    'revisions': copy.deepcopy(item['source_revisions'])} for sid, item in after['items'].items()}
                material['source_versions'] = dict(coverage)
                material['basis'] = {sid: {} for sid in coverage}
                a['material_basis'] = [copy.deepcopy(material)]
                if mode == 'before-change': a['assessed_at'] = '2026-01-01T09:59:00+00:00'
                if mode == 'missing-source': a['source_versions'].pop('independent')
                if mode == 'stale-source': a['source_versions']['source'] = 0
                if mode == 'wrong-basis': a['resolution_basis']['source']['source'] = {'changed': True}
                if mode == 'missing-basis': a['resolution_basis'].pop('decision')
                if mode == 'invalid-material': evidence['materials']['request'][0]['valid'] = False
                if mode == 'wrong-material': a['material_basis'][0]['original']['sha256'] = 'other'
                if mode == 'prose-only': request['assessments'] = []
                if mode in ('native-read', 'native-missing', 'native-wrong-hash'):
                    evidence['native_material_reads'] = [] if mode == 'native-missing' else [
                        {'job_id': 'job-1', 'item_id': 'request', 'material_id': 'note', 'version': 2,
                         'valid': True, 'sha256': material['original']['sha256'] if mode == 'native-read' else 'other'}]
                after['operations'][0]['receipt']['item'] = copy.deepcopy(request)
                if mode == 'no-authentication': after['metadata']['execution:state']['jobs']['job-1']['progress'] = []
                checks = {c['check']: c['status'] for c in probe.evaluate_snapshots('G10', before, after, evidence)['checks']}
                self.assertEqual(checks['review_after_change'], 'REVIEW_REQUIRED' if mode in ('valid', 'native-read') else 'FAIL')

    def test_g10_persisted_correction_precedes_http_return(self):
        before, after, evidence = self.g10_resolution_fixture()
        evidence['intervention']['at'] = '2026-01-01T10:02:00+00:00'
        checks = {c['check']: c['status'] for c in probe.evaluate_snapshots('G10', before, after, evidence)['checks']}
        self.assertEqual(checks['review_after_change'], 'PASS')
        self.assertEqual(checks['dependent_result_revised'], 'PASS')
        self.assertEqual(checks['private_request_resolved'], 'REVIEW_REQUIRED')

    def test_g10_gap_survives_compatible_plan_but_not_changed_basis(self):
        for linked in (True, False):
            for mode in ('plan', 'criterion', 'source', 'material'):
                with self.subTest(linked=linked, mode=mode):
                    before, after, evidence = self.g10_resolution_fixture()
                    request = after['items']['request']
                    assessment = request['assessments'][0]
                    assessment.update(satisfied=False, gap='Input still missing')
                    if not linked:
                        assessment.pop('material_id'); assessment.pop('material_version')
                    request.update(status='active', result_gap=assessment['gap'])
                    after['operations'][0]['receipt']['item'] = copy.deepcopy(request)
                    request.update(version=4, plan_steps=['Continue independent preparation'])
                    if mode == 'criterion': request['completion_criteria'] = 'Different criterion'
                    if mode == 'source': after['items']['source']['source_revisions'].append({})
                    if mode == 'material':
                        request['materials'][0]['version'] += 1
                        evidence['materials']['request'][0]['valid'] = False
                    checks = {c['check']: c['status'] for c in probe.evaluate_snapshots('G10', before, after, evidence)['checks']}
                    self.assertEqual(checks['private_request_resolved'], 'REVIEW_REQUIRED' if mode == 'plan' else 'FAIL')

    def test_g2_human_action_requires_unique_available_derived_owner_action(self):
        human = {'id': 'human', 'parent_id': 'p', 'kind': 'action', 'executor': 'felix',
            'commitment': 'committed', 'status': 'active', 'depends_on': []}
        self.assertEqual(probe.human_front_action([human], 'p', 'felix'), human)
        self.assertIsNone(probe.human_front_action([human, {**human, 'id': 'other'}], 'p', 'felix'))
        self.assertIsNone(probe.human_front_action([{**human, 'depends_on': ['blocked']}], 'p', 'felix'))
        self.assertIsNone(probe.human_front_action([{**human, 'executor': 'worker'}], 'p', 'felix'))

    def test_g2_future_plan_requires_new_authenticated_progress_and_review(self):
        for mode in ('valid', 'no-progress', 'old-plan', 'different-receipt', 'owner', 'missing-plan'):
            with self.subTest(mode=mode):
                before, after = state(), state()
                before['items']['p'] = {'id': 'p', 'kind': 'project', 'status': 'active', 'version': 1}
                after['items']['p'] = {**before['items']['p'], 'version': 2,
                    'plan_steps': ['Preparar impresión cuando la sala esté confirmada']}
                native_fixture(after, 'p')
                after['operations'][0]['receipt']['item'] = copy.deepcopy(after['items']['p'])
                if mode == 'no-progress': after['metadata']['execution:state']['jobs']['job-1']['progress'] = []
                if mode == 'old-plan': before['items']['p']['plan_steps'] = after['items']['p']['plan_steps'][:]
                if mode == 'different-receipt': after['operations'][0]['receipt']['item']['plan_steps'] = ['Otro plan']
                if mode == 'owner': after['operations'][0]['actor'] = 'felix'
                if mode == 'missing-plan': after['items']['p'].pop('plan_steps')
                checks = {c['check']: c['status'] for c in probe.evaluate_snapshots(
                    'G2', before, after, {'aliases': {'project': 'p'}})['checks']}
                self.assertEqual(checks['future_step_explicit'], 'REVIEW_REQUIRED' if mode == 'valid' else 'FAIL')

    def test_g2_current_assessment_or_material_requires_authenticated_receipt(self):
        for representation in ('assessment', 'material'):
            for mode in ('valid', 'no-progress', 'stale', 'no-receipt'):
                with self.subTest(representation=representation, mode=mode):
                    before, after = state(), state()
                    obj = {'id': 'p', 'kind': 'project', 'status': 'active', 'version': 2}
                    after['items']['p'] = obj
                    evidence = {'aliases': {'project': 'p'}}
                    if representation == 'assessment':
                        obj.update(result_gap='Condition unresolved', assessments=[{'actor': 'gtd-felix',
                            'item_version': 1, 'gap': 'Condition unresolved', 'evidence': 'Current review',
                            'source_versions': {'source': 1}, 'satisfied': False}])
                        after['items']['source'] = {'id': 'source', 'version': 7, 'source_revisions': [{'text': 'Original'}]}
                        if mode == 'stale': after['items']['source']['source_revisions'].append({'text': 'Corrected original'})
                    else:
                        content = b'Conditional future support'; material = {'id': 'm', 'version': 2,
                            'original': {'path': 'originals/m', 'sha256': probe.sha(content)}}
                        obj['materials'] = [material]; after['files']['originals/m'] = content
                        evidence['materials'] = {'p': [{**material, 'valid': mode != 'stale'}]}
                    native_fixture(after, 'p')
                    if mode == 'no-progress': after['metadata']['execution:state']['jobs']['job-1']['progress'] = []
                    if mode == 'no-receipt': after['operations'] = []
                    checks = {c['check']: c['status'] for c in probe.evaluate_snapshots('G2', before, after, evidence)['checks']}
                    self.assertEqual(checks['future_step_explicit'], 'REVIEW_REQUIRED' if mode == 'valid' else 'FAIL')

    def test_g8_seed_only_busy_and_budget_reset_do_not_accredit_restart(self):
        old = state()
        old['items']['p'] = {'id': 'p', 'materials': []}
        self.assertFalse(probe.restart_state_proof(old, copy.deepcopy(old), 'gtd-felix')['elaborated'])
        old['items']['p']['materials'] = [{'id': 'm', 'author': 'gtd-felix'}]
        old['operations'] = [{'operation_id': 'prepare', 'actor': 'gtd-felix', 'receipt': {'status': 'applied'}}]
        old['metadata']['execution:state'] = {'jobs': {'job': {'terminal': False}}, 'spent': 2}
        self.assertFalse(probe.restart_state_proof(old, copy.deepcopy(old), 'gtd-felix')['quiescent'])
        old['metadata']['execution:state']['jobs']['job']['terminal'] = True
        old['metadata']['last_review'] = {'source_coverage': {'p': 1}, 'human_decision_pending': True}
        proof = probe.restart_state_proof(old, copy.deepcopy(old), 'gtd-felix')
        self.assertTrue(all(proof[k] for k in ('elaborated', 'quiescent', 'state_preserved', 'budget_preserved')))
        changed = copy.deepcopy(old)
        changed['metadata']['execution:state']['spent'] = 0
        self.assertFalse(probe.restart_state_proof(old, changed, 'gtd-felix')['budget_preserved'])
        changed = copy.deepcopy(old)
        changed['metadata']['last_review']['source_coverage'] = {}
        self.assertFalse(probe.restart_state_proof(old, changed, 'gtd-felix')['state_preserved'])

    def test_g3_answered_query_requires_organization_and_current_authenticated_material(self):
        for mode in ('valid', 'capture', 'invalid-material', 'no-classification-receipt', 'changed-original', 'notes', 'notes-no-receipt', 'empty-notes'):
            with self.subTest(mode=mode):
                before, after = state(), state()
                content = b'Question'; original = {'path': 'originals/q', 'sha256': probe.sha(content)}
                captured = {'id': 'q', 'kind': 'capture', 'status': 'active', 'commitment': 'proposed',
                    'version': 1, 'original': original, 'source_revisions': [{'text': 'Question', 'original': original}]}
                classified = {**captured, 'kind': 'reference', 'version': 2}
                answer = b'Observed answer'; material = {'id': 'answer', 'version': 1,
                    'original': {'path': 'originals/answer', 'sha256': probe.sha(answer)}}
                query = {**classified, 'version': 3, 'materials': [material]}
                after['items']['q'] = query
                after['files'].update({'originals/q': content, 'originals/answer': answer})
                native_fixture(after, 'q')
                after['operations'] += [
                    {'operation_id': 'capture', 'actor': 'felix', 'receipt': {'status': 'applied', 'item': captured}},
                    {'operation_id': 'classification', 'actor': 'gtd-felix', 'receipt': {'status': 'applied', 'item': classified}}]
                after['metadata']['execution:state']['jobs']['job-1']['progress'].append({'operation_id': 'classification'})
                evidence = {'aliases': {'request': 'q'}, 'materials': {'q': [{**material, 'valid': True}]}}
                if mode in ('notes', 'notes-no-receipt', 'empty-notes'):
                    query['materials'] = []
                    query['notes'] = 'Recorded answer' if mode != 'empty-notes' else ''
                    if mode == 'notes-no-receipt':
                        after['operations'][0]['receipt']['item'] = {**query, 'notes': 'Different prior note'}
                if mode == 'capture': query['kind'] = 'capture'
                if mode == 'invalid-material': evidence['materials']['q'][0]['valid'] = False
                if mode == 'no-classification-receipt': after['operations'].pop()
                if mode == 'changed-original': query['original'] = {'path': 'elsewhere', 'sha256': 'other'}
                checks = {c['check']: c['status'] for c in probe.evaluate_snapshots('G3', before, after, evidence)['checks']}
                self.assertEqual(checks['answered_query_organized'], 'PASS' if mode == 'valid' else 'REVIEW_REQUIRED' if mode == 'notes' else 'FAIL')

    def test_g5_integrated_plan_requires_current_witnesses_and_direction_review(self):
        for mode in ('valid', 'old-plan', 'no-progress', 'stale-material', 'empty-question', 'changed-criterion'):
            with self.subTest(mode=mode):
                before, after = state(), state()
                initial = {'id': 'p', 'version': 1, 'kind': 'project', 'status': 'active',
                    'commitment': 'committed', 'purpose': 'Accessible reading', 'outcome': 'Prepared reading',
                    'completion_criteria': 'Accessible place, no equipment purchases'}
                before['items']['p'] = copy.deepcopy(initial)
                content = b'Private preparation'; material = {'id': 'm', 'version': 1,
                    'original': {'path': 'originals/m', 'sha256': probe.sha(content)}}
                after['files']['originals/m'] = content
                after['items']['p'] = {**initial, 'version': 3, 'plan_steps': ['Check venue access'],
                    'decision_needed': True, 'decision_question': 'Which city?', 'materials': [material]}
                native_fixture(after, 'p')
                evidence = {'aliases': {'project': 'p'}, 'materials': {'p': [{**material, 'valid': True}]}}
                if mode == 'old-plan': before['items']['p']['plan_steps'] = ['Check venue access']
                if mode == 'no-progress': after['metadata']['execution:state']['jobs']['job-1']['progress'] = []
                if mode == 'stale-material': evidence['materials']['p'][0]['valid'] = False
                if mode == 'empty-question': after['items']['p']['decision_question'] = ' '
                if mode == 'changed-criterion': after['items']['p']['completion_criteria'] = 'Buy equipment'
                checks = {c['check']: c['status'] for c in probe.evaluate_snapshots('G5', before, after, evidence)['checks']}
                self.assertEqual(checks['plan_and_next_step'], 'REVIEW_REQUIRED' if mode == 'valid' else 'FAIL')

    def g1_fixture(self):
        before, after = state(), state()
        aliases = {key: key for key in 'abcdef'}
        for seed in probe.SCENARIOS['G1']['inputs']:
            key = seed['key']; content = seed['text'].encode()
            blob = {'path': 'originals/' + key, 'sha256': probe.sha(content), 'size': len(content)}
            obj = {'id': key, 'kind': 'capture', 'status': 'active', 'version': 1, 'commitment': 'proposed',
                   'original': blob, 'source_revisions': [{'text': seed['text'], 'original': blob}]}
            before['items'][key] = copy.deepcopy(obj); after['items'][key] = copy.deepcopy(obj)
            before['files'][blob['path']] = content; after['files'][blob['path']] = content
        for key, fields in {'a': {'kind': 'action', 'commitment': 'committed'},
            'b': {'kind': 'project', 'commitment': 'committed'}, 'c': {'kind': 'reference'},
            'd': {'kind': 'possibility', 'review_at': '2030-02-10'}, 'e': {'status': 'withdrawn'},
            'f': {'decision_needed': True, 'decision_question': 'What did you want to retain about Ana and the filter?'}}.items():
            after['items'][key].update(fields, version=2)
        aliases['request'] = 'request'
        after['items']['request'] = {'id': 'request', 'kind': 'action', 'status': 'done',
            'commitment': 'committed', 'version': 3, 'assessments': [{'actor': 'gtd-felix',
                'satisfied': True, 'evidence': 'The six destinations were reviewed'}]}
        native_fixture(after, 'a')
        after['operations'] = [{'operation_id': 'clarify-' + key, 'actor': 'gtd-felix',
            'receipt': {'status': 'applied', 'item': copy.deepcopy(after['items'][key])}} for key in aliases]
        job = after['metadata']['execution:state']['jobs']['job-1']
        job['progress'] = [{'operation_id': row['operation_id']} for row in after['operations']]
        payload = {'status': 'completed'}
        reference = 'hermes:observation:job-1:' + probe.sha(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode())
        job['observations'][0]['evidence_reference'] = reference
        after['metadata'][reference] = {'payload': payload, 'observation': {'native_identity': job['native'], 'native_status': 'completed'}}
        after['metadata']['hermes:intent:job-1'] = {'route': {'model': 'gpt-6-astra', 'reasoning_effort': 'low'}}
        return before, after, {'aliases': aliases}

    def test_g1_mechanical_success_requires_direction_review_of_question(self):
        before, after, evidence = self.g1_fixture()
        result = probe.evaluate_snapshots('G1', before, after, evidence)
        self.assertEqual(result['status'], 'REVIEW_REQUIRED', result)
        self.assertEqual([c['check'] for c in result['checks'] if c['status'] != 'PASS'], ['ambiguity_question_useful'])

    def test_g1_open_or_unassessed_operative_request_fails(self):
        for mode in ('open', 'no-assessment', 'no-progress'):
            before, after, evidence = self.g1_fixture()
            if mode == 'open': after['items']['request']['status'] = 'active'
            if mode == 'no-assessment': after['items']['request']['assessments'] = []
            if mode == 'no-progress':
                after['metadata']['execution:state']['jobs']['job-1']['progress'] = [
                    p for p in after['metadata']['execution:state']['jobs']['job-1']['progress']
                    if p['operation_id'] != 'clarify-request']
            self.assertIn({'check': 'operative_request_resolved', 'status': 'FAIL'},
                probe.evaluate_snapshots('G1', before, after, evidence)['checks'])

    def test_g1_wrong_commitment_cannot_hide_behind_correct_kind(self):
        for key, commitment, expected in (('a', 'proposed', 'direct_intentions_committed'),
                ('b', 'proposed', 'direct_intentions_committed'), ('d', 'committed', 'possibility_not_committed')):
            before, after, evidence = self.g1_fixture()
            after['items'][key]['commitment'] = commitment
            checks = probe.evaluate_snapshots('G1', before, after, evidence)['checks']
            self.assertIn({'check': expected, 'status': 'FAIL'}, checks)

    def test_g1_original_identity_revision_or_bytes_cannot_be_replaced(self):
        for mode in ('descriptor', 'revision', 'bytes'):
            before, after, evidence = self.g1_fixture()
            if mode == 'descriptor': after['items']['a']['original']['sha256'] = 'other'
            if mode == 'revision': after['items']['a']['source_revisions'][0]['text'] = 'Changed original'
            if mode == 'bytes': after['files']['originals/a'] = b'Changed bytes'
            checks = probe.evaluate_snapshots('G1', before, after, evidence)['checks']
            self.assertIn({'check': 'originals_retained', 'status': 'FAIL'}, checks)

    def test_g1_each_destination_needs_pertinent_principal_progress_receipt(self):
        for mode in ('owner', 'missing-progress', 'unrelated-fields'):
            before, after, evidence = self.g1_fixture()
            operation = next(o for o in after['operations'] if o['operation_id'] == 'clarify-c')
            if mode == 'owner': operation['actor'] = 'felix'
            if mode == 'missing-progress':
                after['metadata']['execution:state']['jobs']['job-1']['progress'] = [p for p in after['metadata']['execution:state']['jobs']['job-1']['progress'] if p['operation_id'] != 'clarify-c']
            if mode == 'unrelated-fields': operation['receipt']['item']['kind'] = 'capture'
            checks = probe.evaluate_snapshots('G1', before, after, evidence)['checks']
            self.assertIn({'check': 'principal_destination_receipt_c', 'status': 'FAIL'}, checks)

    def test_missing_native_execution_never_passes(self):
        before, after = state(), state()
        after['items']['p'] = {'id': 'p', 'kind': 'project', 'status': 'done', 'commitment': 'committed'}
        result = probe.evaluate_snapshots('G9', before, after, {'aliases': {'project': 'p'}})
        self.assertEqual('NOT_RUN', result['status'])

    def test_false_success_without_actual_material_is_red(self):
        before, after = state(), state()
        after['items']['p'] = {'id': 'p', 'kind': 'project', 'status': 'done', 'commitment': 'committed',
            'assessments': [{'satisfied': True, 'evidence': 'Model claims everything is ready'}]}
        native_fixture(after, 'p')
        result = probe.evaluate_snapshots('G9', before, after, {'aliases': {'project': 'p'}})
        self.assertEqual('FAIL', result['status'])
        self.assertIn({'check': 'actual_corrected_artifact', 'status': 'FAIL'}, result['checks'])

    def test_old_material_cannot_accredit_completion(self):
        before, after = state(), state()
        after['items']['p'] = {'id': 'p', 'kind': 'project', 'status': 'done', 'commitment': 'committed',
            'assessments': [{'satisfied': True, 'evidence': 'old source', 'material_id': 'old', 'material_version': 1}]}
        native_fixture(after, 'p')
        result = probe.evaluate_snapshots('G9', before, after, {'aliases': {'project': 'p'},
            'materials': {'p': [{'id': 'old', 'version': 1, 'valid': False}]}})
        self.assertEqual('FAIL', result['status'])
        self.assertIn({'check': 'assessed_material_current:p', 'status': 'FAIL'}, result['checks'])

    def test_old_assessment_and_new_correct_material_do_not_close_g9(self):
        before, after = state(), state()
        content = probe.canonical({'dias': {'lunes': 7, 'martes': 13}, 'total': 20, 'explicacion': 'Suma de la fuente corregida'})
        material = {'id': 'new-material', 'version': 2, 'author': 'gtd-felix',
            'original': {'path': 'originals/new', 'sha256': probe.sha(content)}}
        after['files']['originals/new'] = content
        after['items']['p'] = {'id': 'p', 'kind': 'project', 'status': 'done', 'commitment': 'committed',
            'version': 8, 'materials': [material], 'assessments': [{'actor': 'gtd-felix', 'satisfied': True,
            'evidence': 'Old check', 'material_id': 'old-material', 'material_version': 1, 'item_version': 2}]}
        native_fixture(after, 'p')
        evidence = {'aliases': {'project': 'p'}, 'intervention': {'trigger_observed': 'material_created',
            'operation_id': 'correct', 'item_id': 'p', 'before_version': 3, 'after_version': 4},
            'materials': {'p': [{**material, 'valid': True}]}}
        result = probe.evaluate_snapshots('G9', before, after, evidence)
        self.assertIn({'check': 'criterion_assessed_and_closed', 'status': 'FAIL'}, result['checks'])

    def g9_deliverables(self):
        before, after = state(), state()
        def material(identity, data):
            content = probe.canonical(data)
            path = 'originals/' + identity
            after['files'][path] = content
            return {'id': identity, 'version': 1, 'author': 'gtd-felix',
                    'original': {'path': path, 'sha256': probe.sha(content)}}
        total = material('total', {'dias': {'lunes': 7, 'martes': 13}, 'total': 20, 'explicacion': 'Datos corregidos'})
        pending_data = [{'persona': 'Ana', 'libro': 'Atlas'}, {'persona': 'Luis', 'libro': 'Jardín'}]
        pending = material('pending', pending_data)
        contribution = material('child-pending', pending_data)
        assessments = [{'satisfied': True, 'evidence': 'Verified against current source',
            'material_id': m['id'], 'material_version': 1, 'item_version': 6} for m in (total, pending)]
        project = {'id': 'p', 'kind': 'project', 'status': 'done', 'commitment': 'committed',
            'version': 8, 'text': 'Corrected data', 'materials': [total, pending], 'assessments': assessments}
        child = {'id': 'child', 'parent_id': 'p', 'kind': 'action', 'created_by': 'gtd-felix',
            'commitment': 'committed', 'mandate_id': 'mandate', 'version': 2, 'materials': [contribution]}
        after['items'].update(p=project, child=child)
        native_fixture(after, 'p')
        after['operations'] += [
            {'operation_id': 'correction', 'actor': 'felix', 'receipt': {'status': 'applied',
                'item': {'id': 'p', 'version': 4, 'text': 'Corrected data'}}},
            {'operation_id': 'derive-child', 'actor': 'gtd-felix', 'receipt': {'status': 'applied',
                'item': {**child, 'version': 1, 'materials': []}}},
            {'operation_id': 'prepare-child', 'actor': 'gtd-felix', 'receipt': {'status': 'applied', 'item': child}}]
        after['metadata']['execution:state']['jobs']['job-1']['progress'] += [
            {'operation_id': name} for name in ('derive-child', 'prepare-child')]
        evidence = {'aliases': {'project': 'p'}, 'intervention': {'trigger_observed': 'material_created',
            'operation_id': 'correction', 'item_id': 'p', 'before_version': 3, 'after_version': 4,
            'fields': {'text': 'Corrected data'}}, 'materials': {'p': [{**m, 'valid': True} for m in (total, pending)],
            'child': [{**contribution, 'valid': True}]}}
        return before, after, evidence

    def test_g9_both_deliverables_and_real_derived_contribution(self):
        before, after, evidence = self.g9_deliverables()
        checks = {c['check']: c['status'] for c in probe.evaluate_snapshots('G9', before, after, evidence)['checks']}
        for name in ('derived_under_mandate', 'separate_current_returns_artifact',
                     'both_deliverables_in_closure', 'criterion_assessed_and_closed'):
            self.assertEqual(checks[name], 'PASS', checks)

    def test_g9_joint_root_assessment_with_child_materials_requires_review(self):
        for missing_assessment in (False, True):
            before, after, evidence = self.g9_deliverables()
            root = after['items']['p']
            child = after['items']['child']
            child['materials'] += root['materials']
            evidence['materials']['child'] += evidence['materials'].pop('p')
            root['materials'] = []
            root['assessments'] = [] if missing_assessment else [{'actor': 'gtd-felix',
                'satisfied': True, 'evidence': 'Joint result reviewed', 'item_version': 6}]
            checks = {c['check']: c['status'] for c in
                probe.evaluate_snapshots('G9', before, after, evidence)['checks']}
            self.assertEqual(checks['criterion_assessed_and_closed'],
                'FAIL' if missing_assessment else 'REVIEW_REQUIRED')
            self.assertEqual(checks['derived_under_mandate'], 'PASS')
            self.assertEqual(checks['both_deliverables_in_closure'], 'REVIEW_REQUIRED')

    def test_g9_missing_second_deliverable_cannot_pass(self):
        before, after, evidence = self.g9_deliverables()
        after['items']['p']['materials'] = after['items']['p']['materials'][:1]
        after['items']['child']['materials'] = []
        checks = probe.evaluate_snapshots('G9', before, after, evidence)['checks']
        self.assertIn({'check': 'separate_current_returns_artifact', 'status': 'FAIL'}, checks)
        self.assertIn({'check': 'both_deliverables_in_closure', 'status': 'FAIL'}, checks)

    def test_g9_decorative_child_or_unwitnessed_contribution_cannot_pass(self):
        for mode in ('label-only', 'no-progress'):
            before, after, evidence = self.g9_deliverables()
            if mode == 'label-only':
                after['items']['child'].update(title='Prepare and verify both deliverables', materials=[])
            else:
                after['metadata']['execution:state']['jobs']['job-1']['progress'] = [{'operation_id': 'agent-operation'}]
            checks = probe.evaluate_snapshots('G9', before, after, evidence)['checks']
            self.assertIn({'check': 'derived_under_mandate', 'status': 'FAIL'}, checks)

    def test_g9_free_text_claim_about_both_deliverables_requires_review(self):
        before, after, evidence = self.g9_deliverables()
        after['items']['p']['assessments'] = after['items']['p']['assessments'][:1]
        after['items']['p']['assessments'][0]['evidence'] = 'Both deliverables verified, returns complete'
        result = probe.evaluate_snapshots('G9', before, after, evidence)
        self.assertEqual(result['status'], 'FAIL')
        self.assertTrue(any(c['check'] == 'both_deliverables_in_closure' and c['status'] == 'REVIEW_REQUIRED'
                            for c in result['checks']))

    def test_undelivered_durable_child_does_not_accredit_g7_return(self):
        before, after = state(), state()
        after['items']['p'] = {'id': 'p', 'kind': 'project', 'status': 'active', 'commitment': 'committed'}
        native_fixture(after, 'p')
        parent = after['metadata']['execution:state']['jobs']['job-1']
        child = copy.deepcopy(parent)
        child.update(id='child', parent_job_id='job-1', integration='pending', terminal=False)
        child['native'] = {'provider': 'hermes-kanban', 'id': 'synthetic-card', 'profile': 'synthetic-executor'}
        child['observations'] = [{'native_status': 'running'}]
        after['metadata']['execution:state']['jobs']['child'] = child
        result = probe.evaluate_snapshots('G7', before, after, {'aliases': {'project': 'p'}})
        self.assertIn({'check': 'return_to_correct_project', 'status': 'FAIL'}, result['checks'])

    def test_human_pending_cannot_be_complete(self):
        before, after = state(), state()
        after['items']['p'] = {'id': 'p', 'kind': 'project', 'status': 'done', 'commitment': 'committed', 'decision_needed': True}
        native_fixture(after, 'p')
        result = probe.evaluate_snapshots('G9', before, after, {'aliases': {'project': 'p'}})
        self.assertIn({'check': 'no_completed_human_decision', 'status': 'FAIL'}, result['checks'])

    def test_owner_populated_state_not_model_mutation(self):
        before, after = state(), state()
        after['items']['p'] = {'id': 'p', 'kind': 'project', 'status': 'active', 'commitment': 'committed'}
        native_fixture(after, 'p', actor='felix')
        result = probe.evaluate_snapshots('G9', before, after, {'aliases': {'project': 'p'}})
        self.assertIn({'check': 'principal_authenticated_mutation', 'status': 'FAIL'}, result['checks'])

    def test_real_export_verified_and_material_content_loaded(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            service = GTDService(root / 'state')
            try:
                item = service.capture('felix', 'capture', 'Synthetic')['item']
                receipt = service.execute('felix', {'operation_id': 'material', 'item_id': item['id'],
                    'expected_version': item['version'], 'action': 'put_material', 'fields': {'content': 'Original synthetic bytes'}})
                self.assertEqual('applied', receipt['status'])
                path = root / 'snapshot.zip'
                service.export(path)
            finally:
                service.close()
            snapshot = probe.load_snapshot(path, probe.sha(path.read_bytes()))
            self.assertEqual('Original synthetic bytes', probe.material_content(snapshot, snapshot['items'][item['id']])[0][1])
            with self.assertRaisesRegex(ValueError, 'snapshot_digest_mismatch'):
                probe.load_snapshot(path, '0' * 64)

    def test_run_requires_execute_and_private_config(self):
        with patch.object(probe, 'run', side_effect=AssertionError('must not run')):
            self.assertEqual(1, probe.main(['run', '--config', '/missing', '--evidence-dir', '/missing', '--case', 'G1']))
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'config.json'
            path.write_text('{}'); path.chmod(0o644)
            with self.assertRaises(ValueError):
                probe.private_json(path)

    def test_positive_date_fixture_is_red_if_reminder_becomes_deadline(self):
        before, after = state(), state()
        after['items'] = {
            'a': {'id': 'a', 'kind': 'calendar', 'status': 'active', 'commitment': 'committed', 'starts_at': '2030-03-04T10:00:00+01:00'},
            'd': {'id': 'd', 'kind': 'action', 'status': 'active', 'commitment': 'committed', 'due_at': '2030-03-06'},
            'r': {'id': 'r', 'kind': 'possibility', 'status': 'active', 'commitment': 'proposed', 'review_at': '2030-03-07'}}
        native_fixture(after, 'a')
        job = after['metadata']['execution:state']['jobs']['job-1']
        payload = {'id': 'synthetic-run', 'status': 'completed'}
        digest = probe.sha(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode())
        reference = 'hermes:observation:job-1:' + digest
        job['observations'][0]['evidence_reference'] = reference
        after['metadata'][reference] = {'payload': payload, 'observation': {
            'native_identity': job['native'], 'native_status': 'completed'}}
        after['metadata']['hermes:intent:job-1'] = {'route': {'model': 'gpt-6-astra', 'reasoning_effort': 'low'}}
        evidence = {'aliases': {'appointment': 'a', 'deadline': 'd', 'reminder': 'r'}}
        self.assertEqual('PASS', probe.evaluate_snapshots('G6', before, after, evidence)['status'])
        after['items']['r']['due_at'] = '2030-03-07'
        self.assertEqual('FAIL', probe.evaluate_snapshots('G6', before, after, evidence)['status'])

    def test_explicit_runtime_override_never_falls_back(self):
        from runtime_location import runtime_root
        with patch.dict('os.environ', {'GTD_RUNTIME_ROOT': '/missing-synthetic-runtime'}):
            with self.assertRaisesRegex(RuntimeError, 'gtd_runtime_unavailable'):
                runtime_root()


class DriverTests(unittest.IsolatedAsyncioTestCase):
    async def test_poll_limits_preserve_after_and_closure_failure_cannot_pass(self):
        for mode in ('calls', 'time', 'broken_closure'):
            with self.subTest(mode=mode), tempfile.TemporaryDirectory() as temp:
                objects = []
                class Response:
                    status = 200
                    async def __aenter__(self): return self
                    async def __aexit__(self, *a): pass
                    async def read(self): return self.data
                class Session:
                    def request(self, method, url, json=None, **kw):
                        response = Response();path = url.split(':8765')[-1]
                        if path == '/v1/captures':
                            obj = {'id': str(len(objects)), 'version': 1};objects.append(obj)
                            value = {'status': 'applied', 'item': obj}
                        elif path == '/v1/items': value = objects
                        elif path == '/v1/control/pending': value = [{'id': 'busy', 'terminal': False}]
                        elif path.startswith('/v1/materials/'): value = []
                        elif path == '/v1/export':
                            if mode == 'broken_closure' and driver.closing: raise OSError('synthetic closure transport failure')
                            response.data = b'synthetic-export';return response
                        else: raise AssertionError(path)
                        response.data = probe.canonical(value);return response
                config = {'synthetic': True, 'product_api_url': 'http://127.0.0.1:8765',
                    'owner_token_env': 'SYNTHETIC_TOKEN', 'max_http_calls': 1000 if mode == 'time' else 30, 'max_cases': 1,
                    'timeout_seconds': .03 if mode == 'time' else 2, 'poll_interval_seconds': .001,
                    'closure_seconds': .2, 'closure_max_http_calls': 10}
                with patch.dict('os.environ', {'SYNTHETIC_TOKEN': 'synthetic'}):
                    driver = probe.ProductDriver(config, Session(), temp)
                    record = await driver.run_case('G6')
                self.assertEqual('PARTIAL', record['status'])
                self.assertNotEqual('PASS', probe.evaluate_record(record, temp)['status'])
                if mode == 'broken_closure':
                    self.assertNotIn('after', record)
                    self.assertEqual('INCOMPLETE', record['closure_status'])
                else:
                    self.assertIn('after', record)
                    self.assertEqual('COLLECTED', record['closure_status'])
                    self.assertEqual('probe_time_budget_exhausted' if mode == 'time' else 'probe_http_budget_exhausted', record['error'])

    async def test_g8_restarts_only_after_initial_processing_then_requests_return(self):
        with tempfile.TemporaryDirectory() as temp:
            driver = object.__new__(probe.ProductDriver)
            driver.config = {'timeout_seconds': 2, 'case_timeout_seconds': 1, 'poll_interval_seconds': .001}
            driver.destination = Path(temp)
            driver.started = probe.time.monotonic()
            driver.closure_seconds = .5
            driver.trace = []
            objects, events = [], []
            async def request(method, path, payload=None, **kwargs):
                if path == '/v1/captures':
                    obj = {'id': str(len(objects)), 'version': 1, 'materials': [], 'text': payload['text']}
                    objects.append(obj)
                    events.append('return' if payload['operation_id'].endswith(':return') else 'capture')
                    return {'item': obj, 'status': 'applied'}
                if path == '/v1/items':
                    events.append('poll')
                    return objects
                if path == '/v1/control/pending':
                    return []
                if path.startswith('/v1/materials/'):
                    return []
                raise AssertionError(path)
            driver.request = request
            driver.snapshot = AsyncMock(return_value={'file': 'synthetic.zip', 'sha256': 'synthetic'})
            async def ready(d, record):
                events.append('ready')
                return {'enabled_bots': ['principal']}
            async def restart(d, record):
                self.assertIn('ready', events)
                self.assertGreaterEqual(events.count('poll'), 4)
                self.assertNotIn('return', events)
                events.append('restart')
                return {'synthetic': True}
            record = await driver.run_case('G8', restart=restart, case_ready=ready)
            self.assertEqual(record['status'], 'COLLECTED')
            self.assertLess(events.index('ready'), events.index('restart'))
            self.assertLess(events.index('restart'), events.index('return'))
            self.assertEqual(events.count('ready'), 2)

    async def test_admission_preserves_identity_and_rejects_restart_reactivation(self):
        driver = object.__new__(probe.ProductDriver)
        driver.config = {'bot_ids': ['own']}
        bot = {'id': 'own', 'state': 'available', 'probe_evidence': 'verified', 'profile': 'synthetic'}
        driver.request = AsyncMock(side_effect=[[bot, {'id': 'other'}], {'status': 'applied'}, []])
        await driver.prepare_case({'run_id': 'r'})
        self.assertEqual({**bot, 'state': 'suspended'}, driver.request.call_args_list[1].args[2]['bot'])
        driver.request = AsyncMock(return_value=[bot])
        with self.assertRaisesRegex(ValueError, 'suspension_changed'):
            await driver.enable_case({'run_id': 'r'})
        self.assertEqual(1, driver.request.await_count)
        driver.request = AsyncMock(side_effect=[[{**bot, 'state': 'suspended'}], [], {'status': 'applied'}])
        await driver.enable_case({'run_id': 'r'})
        self.assertEqual(bot, driver.request.call_args_list[-1].args[2]['bot'])

    async def test_real_service_exports_through_fake_http_without_model_remain_not_run(self):
        # No socket or live service is started. Real domain/export is exercised
        # through an in-process HTTP seam, with no fabricated principal changes.
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            evidence_dir = root / 'evidence'; evidence_dir.mkdir()
            service = GTDService(root / 'state')
            counter = 0
            class Response:
                status = 200
                def __init__(self, data): self.data = data
                async def __aenter__(self): return self
                async def __aexit__(self, *args): pass
                async def read(self): return self.data
            class Session:
                def request(self, method, url, json=None, **kwargs):
                    nonlocal counter
                    path = url.split(':8765')[-1]
                    if path == '/v1/captures':
                        value = service.capture('felix', **json)
                    elif path == '/v1/commands':
                        value = service.execute('felix', json)
                    elif path == '/v1/items':
                        value = service.query()
                    elif path == '/v1/control/pending':
                        value = []
                    elif path.startswith('/v1/materials/'):
                        value = service.materials(path.rsplit('/', 1)[-1])
                    elif path == '/v1/export':
                        counter += 1
                        archive = root / f'export-{counter}.zip'
                        service.export(archive)
                        return Response(archive.read_bytes())
                    else:
                        raise AssertionError('unexpected route')
                    return Response(probe.canonical(value))
            config = {'synthetic': True, 'product_api_url': 'http://127.0.0.1:8765',
                'owner_token_env': 'SYNTHETIC_TEST_TOKEN', 'timeout_seconds': 10,
                'max_http_calls': 40, 'max_cases': 1, 'poll_interval_seconds': .001}
            try:
                with patch.dict('os.environ', {'SYNTHETIC_TEST_TOKEN': 'synthetic-no-account'}):
                    driver = probe.ProductDriver(config, Session(), evidence_dir)
                    order = []
                    async def prepare(d, r):
                        self.assertFalse(service.query())
                        order.append('prepare')
                    async def ready(d, r):
                        self.assertIn('before', r)
                        self.assertIn('request', r['aliases'])
                        order.append('ready')
                    record = await driver.run_case('G6', case_prepare=prepare, case_ready=ready)
                    self.assertEqual(['prepare', 'ready'], order)
                self.assertEqual('COLLECTED', record['status'])
                self.assertEqual('NOT_RUN', probe.evaluate_record(record, evidence_dir)['status'])
                self.assertNotIn('synthetic-no-account', probe.canonical(record).decode())
                self.assertEqual(4, len(service.query()))
            finally:
                service.close()


class G7ReturnOracleTests(unittest.TestCase):
    def g7_authenticated_return_fixture(self):
        # A real domain receipt/export; native observations remain synthetic.
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            service = GTDService(root / 'state', executor_actors=('worker',))
            try:
                obj = service.capture('felix', 'capture', 'Guide 09-12; Lara pending')['item']
                def command(actor, operation, action, fields):
                    current = service.get_item(obj['id'])
                    receipt = service.execute(actor, {'operation_id': operation, 'item_id': obj['id'],
                        'expected_version': current['version'], 'action': action, 'fields': fields})
                    self.assertEqual('applied', receipt['status'], receipt)
                    return receipt
                command('felix', 'clarify', 'clarify', {'kind': 'project', 'commitment': 'committed',
                    'outcome': 'Guide prepared', 'completion_criteria': 'Guide checked and Lara confirms'})
                mandate = command('felix', 'grant', 'grant_mandate', {'scope_item_id': obj['id'],
                    'capabilities': ['prepare_private', 'local_work'], 'actors': ['gtd-felix', 'worker'],
                    'completion_criteria': 'Private guide prepared'})['mandate']['id']
                correction = command('felix', 'correct', 'edit', {'text': 'Guide 10-13; Lara pending'})
                validated_version = service.get_item(obj['id'])['version']
                receipt = command('worker', 'gtd-output:child', 'put_material',
                    {'content': 'Guide uses 10-13; Lara confirmation remains pending.', 'mandate_id': mandate})
                observed = service.materials(obj['id'])
                # I2: receipt items carry references; the native artifact
                # resolves the full original (identical bytes to pre-cut).
                ref = receipt['item']['materials'][-1]
                full_material = next(m for m in observed
                                     if m['id'] == ref['id'] and m['version'] == ref['version'])
                path = root / 'snapshot.zip'
                service.export(path)
                after = probe.load_snapshot(path, probe.sha(path.read_bytes()))
            finally:
                service.close()
        native = {'provider': 'hermes-kanban', 'id': 'card', 'profile': 'synthetic-worker'}
        payload = {'id': 'card', 'status': 'completed'}
        reference = 'hermes:observation:child:' + probe.sha(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode())
        job = {'id': 'child', 'actor': 'worker', 'item_id': obj['id'], 'parent_job_id': 'parent',
            'mandate_id': mandate, 'validated_version': validated_version, 'native': native,
            'terminal': True, 'integration': 'integrated', 'domain_operation_id': 'gtd-output:child',
            'observations': [{'native_status': 'completed', 'evidence_reference': reference}]}
        after['metadata']['execution:state'] = {'jobs': {'child': job}}
        after['metadata'][reference] = {'payload': payload,
            'observation': {'native_identity': native, 'native_status': 'completed'}}
        after['metadata']['hermes:artifact:child'] = {**full_material['original'],
                                                       'job_id': 'child'}
        evidence = {'aliases': {'project': obj['id']}, 'materials': {obj['id']: observed},
            'intervention': {'operation_id': 'correct', 'item_id': obj['id'],
                'after_version': correction['item']['version'], 'fields': {'text': correction['item']['text']}}}
        return state(), after, evidence

    def test_g7_executor_authenticated_return_is_accepted(self):
        before, after, evidence = self.g7_authenticated_return_fixture()
        operation = next(o for o in after['operations'] if o['operation_id'] == 'gtd-output:child')
        self.assertEqual('worker', operation['actor'])
        self.assertEqual('worker', operation['receipt']['item']['materials'][-1]['author'])
        result = probe.evaluate_snapshots('G7', before, after, evidence)
        self.assertIn({'check': 'return_to_correct_project', 'status': 'PASS'}, result['checks'])

    def test_g7_return_rejects_wrong_receipt_actor_binding_and_material(self):
        before, base, evidence = self.g7_authenticated_return_fixture()
        for change in ('actor', 'operation', 'receipt_operation', 'item', 'version', 'artifact_job',
                       'artifact_hash', 'assessment_only', 'material_author', 'material_mandate',
                       'stale', 'wrong_project', 'already_present'):
            with self.subTest(change=change):
                after, ev, old = copy.deepcopy(base), copy.deepcopy(evidence), copy.deepcopy(before)
                job = after['metadata']['execution:state']['jobs']['child']
                operation = next(o for o in after['operations'] if o['operation_id'] == 'gtd-output:child')
                receipt = operation['receipt']
                # Alias into this snapshot copy: mutation sub-cases corrupt
                # the evaluated receipt reference itself.
                material = receipt['item']['materials'][-1]
                if change == 'actor': operation['actor'] = 'felix'
                elif change == 'operation': job['domain_operation_id'] = 'correct'
                elif change == 'receipt_operation': receipt['operation_id'] = 'different'
                elif change == 'item': receipt['item']['id'] = 'different'
                elif change == 'version': receipt['item']['version'] += 1
                elif change == 'artifact_job': after['metadata']['hermes:artifact:child']['job_id'] = 'other'
                elif change == 'artifact_hash': after['metadata']['hermes:artifact:child']['sha256'] = 'different'
                elif change == 'assessment_only': receipt['item']['materials'] = []; receipt['item']['assessments'] = [{'satisfied': True}]
                elif change == 'material_author': material['author'] = 'felix'
                elif change == 'material_mandate': material['mandate_id'] = 'other'
                elif change == 'stale': ev['materials'][job['item_id']][0]['valid'] = False
                elif change == 'wrong_project': ev['aliases']['project'] = 'other'
                elif change == 'already_present': old['operations'].append(copy.deepcopy(operation))
                result = probe.evaluate_snapshots('G7', old, after, ev)
                expected = 'NOT_RUN' if change == 'wrong_project' else 'FAIL'
                if expected == 'NOT_RUN': self.assertEqual(expected, result['status'])
                else: self.assertIn({'check': 'return_to_correct_project', 'status': expected}, result['checks'])
