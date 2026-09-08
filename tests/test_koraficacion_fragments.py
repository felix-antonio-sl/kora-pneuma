import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


class FragmentReviewTests(unittest.TestCase):
    def run_review(self, source, output, fragments):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name, body in [('source', source), ('output', output), ('fragments', fragments)]:
                (root / name).write_text(body)
            script = Path(__file__).resolve().parents[1] / 'products/kora/koraficacion/scripts/check_fragments.py'
            return subprocess.run([sys.executable, str(script), str(root / 'source'),
                                   str(root / 'output'), str(root / 'fragments')],
                                  capture_output=True, text=True)

    def test_an_invented_fragment_present_in_output_is_rejected(self):
        result = self.run_review('El límite es 12 kg.', 'El límite es 15 kg.', '15 kg\n')
        self.assertEqual(result.returncode, 1)
        report = json.loads(result.stdout)
        self.assertEqual(report['absent_from_source'], [1])
        self.assertEqual(report['absent_from_output'], [])
        self.assertNotIn('15 kg', result.stdout)

    def test_missing_heading_is_not_treated_as_a_comment(self):
        result = self.run_review('# Excepciones\nNo enviar.', 'No enviar.', '# Excepciones\n')
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout)['absent_from_output'], [1])

    def test_whitespace_normalization_and_empty_selection_have_distinct_outcomes(self):
        result = self.run_review('No\n  enviar.', 'No enviar.', 'No enviar.\n')
        self.assertEqual(result.returncode, 0, result.stderr)
        empty = self.run_review('No enviar.', 'No enviar.', ' \n')
        self.assertNotEqual(empty.returncode, 0)
        self.assertEqual(empty.stdout, '')


if __name__ == '__main__':
    unittest.main()
