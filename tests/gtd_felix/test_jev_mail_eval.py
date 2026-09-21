"""Checks for the offline experiment's evidence, not model-quality assertions."""
import importlib.util
import json
from pathlib import Path
import unittest

path = Path(__file__).resolve().parents[2] / 'scripts/gtd_jev_mail_eval.py'
spec = importlib.util.spec_from_file_location('jev_eval', path)
evaluation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(evaluation)


class JevMailEvaluationTests(unittest.TestCase):
    def setUp(self):
        self.data, self.cases = evaluation.load_cases(evaluation.DEFAULT_CASES, 'dev')

    def result(self, index=0, prediction='selected'):
        request = list(evaluation.prepare(self.cases))[index]
        return {'id': request['id'], 'request_sha256': request['request_sha256'], 'elapsed_ms': 120,
                'response': {'model': evaluation.MODEL, 'answers': {'mail_relevance': {
                    'type': 'choice', 'choice': prediction, 'confidence': 0.9,
                    'probabilities': {label: float(label == prediction) for label in evaluation.LABELS}}},
                    'usage': {'input_tokens': 200, 'output_tokens': 0}}}

    def test_labels_and_other_cases_do_not_enter_requests(self):
        for case, prepared in zip(self.cases, evaluation.prepare(self.cases)):
            self.assertEqual({'text': case['text']}, prepared['request']['state'])
            self.assertNotIn(case['rationale'], json.dumps(prepared, ensure_ascii=False))
        _, holdout = evaluation.load_cases(evaluation.DEFAULT_CASES, 'check')
        self.assertFalse({c['id'] for c in holdout} & {c['id'] for c in self.cases})

    def test_false_negative_distinct_from_missing_or_failed_response(self):
        record = self.result(prediction='noise')
        failure = self.result(1)
        failure.pop('response')
        failure['error'] = 'timeout'
        result = evaluation.score(self.cases, [record, failure])
        self.assertEqual(1, result['relevant_lost_as_noise'])
        self.assertEqual(1, result['technical_failures'])
        self.assertEqual(10, result['missing'])
        self.assertEqual(0, result['uncertain_outputs'])
        self.assertFalse(result['production_accepted'])

    def test_duplicate_or_unknown_result_is_rejected(self):
        with self.assertRaises(ValueError):
            evaluation.score(self.cases, [self.result(), self.result()])
        row = self.result(); row['id'] = 'unknown'
        with self.assertRaises(ValueError):
            evaluation.score(self.cases, [row])

    def test_invalid_probabilities_or_model_are_not_decisions(self):
        for change in ('nan', 'incomplete_mass', 'wrong_model', 'wrong_request'):
            row = self.result()
            if change == 'nan':
                row['response']['answers']['mail_relevance']['probabilities']['selected'] = float('nan')
            elif change == 'incomplete_mass':
                # Observed provider response: preserve it as a contract anomaly,
                # never silently normalize probabilities or pretend a valid decision.
                row['response']['answers']['mail_relevance'].update(
                    choice='noise', confidence=0.33,
                    probabilities={'noise': 0.55, 'selected': 0.4, 'uncertain': 0.04})
            elif change == 'wrong_model':
                row['response']['model'] = 'other-model'
            else:
                row['request_sha256'] = 'changed'
            with self.subTest(change=change):
                self.assertEqual(1, evaluation.score(self.cases, [row])['technical_failures'])

    def test_uncertain_and_usage_are_reported_without_fake_cost(self):
        result = evaluation.score(self.cases, [self.result(prediction='uncertain')])
        self.assertEqual(1, result['uncertain_outputs'])
        self.assertEqual(200, result['observed_usage_valid_responses']['input_tokens'])
        self.assertIsNone(result['cost_usd'])

    def test_context_is_explicit_changes_identity_and_leaves_synthetic_requests_unchanged(self):
        original = self.cases[0]
        before = next(evaluation.prepare([original]))
        contextual = {**original, 'context': 'El usuario coordina telemedicina.'}
        after = next(evaluation.prepare([contextual]))
        self.assertNotEqual(before['request_sha256'], after['request_sha256'])
        self.assertEqual(contextual['context'], after['request']['state']['context'])
        self.assertEqual(before, next(evaluation.prepare([original])))
        score = evaluation.score([contextual], [])
        self.assertEqual(evaluation.fingerprint(after['request']['questions']['mail_relevance']), score['question_sha256'])
        # An old response cannot be reused for the newly contextualized question.
        self.assertEqual(1, evaluation.score([contextual], [self.result()])['technical_failures'])
