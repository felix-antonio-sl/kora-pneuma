"""Invariantes de contenido, exclusiones, reanudación y referencias.

Los booleanos que entrega el revisor son declaraciones de juicio; estas
pruebas comprueban que el helper no las convierte en una prueba semántica.
"""

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import types
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / 'products/kora/koraficacion-integral/scripts/integral.py'
spec = importlib.util.spec_from_file_location('integral_helper', SCRIPT)
helper = importlib.util.module_from_spec(spec)
previous_bytecode = sys.dont_write_bytecode
try:
    sys.dont_write_bytecode = True
    spec.loader.exec_module(helper)
finally:
    sys.dont_write_bytecode = previous_bytecode


class IntegralTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.source = self.root / 'source.md'
        self.source.write_text('El archivo debe retenerse durante 30 días. '
                               'Está prohibido borrarlo antes de que termine ese plazo.\n')
        self.work = self.root / 'work'
        self.call('init', '--source', str(self.source))

    def call(self, command, *args, expected=0, work=None):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), command, '--work', str(work or self.work), *args],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return json.loads(result.stdout)

    def submit(self, data, block='b0001', expected=0, work=None):
        path = self.root / ('step-' + block + '.json')
        path.write_text(json.dumps(data, ensure_ascii=False))
        return self.call('submit', '--block', block, '--file', str(path), expected=expected, work=work)

    def snapshot(self, work=None):
        path = (work or self.work) / 'state.json'
        return path.read_bytes(), path.stat().st_mtime_ns

    def inventory(self, packet=None, question_ids=('q01', 'q02')):
        packet = packet or self.call('next')
        first, last = packet['lines']
        units = [
            {'id': 'u01', 'lines': [first, last],
             'statement': 'El archivo debe retenerse durante 30 días.'},
            {'id': 'u02', 'lines': [first, last],
             'statement': 'No se permite borrar antes del plazo.'},
        ]
        questions = [
            {'id': question_ids[0], 'question': '¿Cuál es el plazo?', 'expected': '30 días.'},
            {'id': question_ids[1], 'question': '¿Se puede borrar antes?', 'expected': 'No.'},
        ]
        return {
            'stage': 'inventory', 'units': units, 'questions': questions,
            'dependencies': [], 'source_rechecked': True,
            'source_review': 'Volví al original y cotejé objeto, plazo, unidad y prohibición.',
        }

    def candidate(self, text='Archivo: retener 30 días; no borrar antes.\n',
                  mappings=None, references=None, literal_changes=None,
                  transformations=None):
        return {
            'stage': 'candidate', 'text': text,
            'mapping': mappings or [
                {'unit': 'u01', 'quote': '30 días'},
                {'unit': 'u02', 'quote': 'no borrar antes'},
            ],
            'references': references or [],
            'transformations': transformations or ['Fusiona la puntuación sin cambiar el plazo.'],
            'literal_changes': literal_changes or [],
            'issues': [],
        }

    def review(self, packet=None, literal_changes=None, **overrides):
        packet = packet or self.call('next')
        unit_ids = [unit['id'] for unit in packet['inventory']['units']]
        question_ids = [question['id'] for question in packet['inventory']['questions']]
        value = {
            'stage': 'review',
            'candidate_sha256': packet['schema']['candidate_sha256'],
            'unit_checks': [
                {'id': unit_id, 'preserved': True, 'reason': 'Afirmación, condición y referente cotejados.'}
                for unit_id in unit_ids
            ],
            'source_rechecked': True,
            'backward_complete': True,
            'relations_preserved': True,
            'relations_review': 'La prohibición sigue referida al mismo plazo del archivo.',
            'questions': [
                {'id': question_id, 'answer': 'Respuesta observada en candidata.', 'satisfied': True}
                for question_id in question_ids
            ],
            'literal_changes': literal_changes if literal_changes is not None else [],
            'isolation': 'same_context',
            'issues': [],
        }
        value.update(overrides)
        return value

    def global_review(self, work=None):
        packet = self.call('next', work=work)
        return {
            'stage': 'global',
            'assembly_sha256': packet['assembly_sha256'],
            'block_checks': [
                {'id': row['id'], 'preserved': True,
                 'reason': 'Bloque y relaciones cotejados con su fuente.'}
                for row in packet['index']
            ],
            'source_rechecked': True,
            'relations_review': 'Se conserva el orden y el alcance entre los bloques.',
            'issues': [],
            'limits': 'Cotejo del fixture; no prueba equivalencia semántica universal.',
            'negative_control': {'status': 'NOT_RUN', 'reason': 'No se realizó llamada separada.'},
        }

    def complete(self):
        self.submit(self.inventory())
        candidate = self.candidate()
        self.submit(candidate)
        self.submit(self.review())
        self.submit(self.global_review(), 'global')

    def _multi_block_work(self, text='Mismo encabezado.\n\nMismo encabezado.\n\nMismo encabezado.\n'):
        source = self.root / 'multi.md'
        source.write_text(text)
        work = self.root / 'multi-work'
        self.call('init', '--source', str(source), '--max-chars', '15', work=work)
        return source, work

    def _multi_inventory(self, work, block_id):
        packet = self.call('show', '--block', block_id, work=work)
        first, last = packet['lines']
        return {
            'stage': 'inventory',
            'units': [{'id': 'u01', 'lines': [first, last], 'statement': 'Se conserva el encabezado.'}],
            'questions': [{'id': 'q01', 'question': '¿Qué encabezado se conserva?',
                          'expected': 'Mismo encabezado.'}],
            'dependencies': [], 'source_rechecked': True,
            'source_review': 'Revisé todas las líneas no vacías del rango y su encabezado.',
        }

    def _multi_candidate(self, work, block_id, text, references=None, ref_id=None,
                         quote='Mismo encabezado.'):
        mappings = [{'unit': 'u01', 'quote': quote}]
        if ref_id:
            mappings[0]['block'] = ref_id
        return {
            'stage': 'candidate', 'text': text, 'mapping': mappings,
            'references': references or [],
            'transformations': ['Deduplica el encabezado repetido y conserva su alcance.'],
            'literal_changes': [], 'issues': [],
        }

    def _accept_multi(self, work, block_id, candidate):
        state = json.loads((work / 'state.json').read_text())
        block = next(item for item in state['blocks'] if item['id'] == block_id)
        if 'inventory' not in block:
            self.submit(self._multi_inventory(work, block_id), block_id, work=work)
        self.submit(candidate, block_id, work=work)
        packet = self.call('next', work=work)
        self.submit(self.review(packet), block_id, work=work)

    def test_protocol_v3_and_inventory_questions_are_separate(self):
        self.assertEqual(self.call('status')['protocol'], 'integral-3')
        packet = self.call('next')
        self.assertEqual(packet['stage'], 'inventory')
        self.assertIn('questions', packet['schema'])
        self.assertNotIn('question', packet['schema']['units'][0])
        self.assertNotIn('expected', packet['schema']['units'][0])
        self.submit(self.inventory())
        state = json.loads((self.work / 'state.json').read_text())
        self.assertNotIn('evidence', state['blocks'][0]['inventory']['units'][0])
        self.assertNotIn('question', state['blocks'][0]['inventory']['units'][0])

    def test_exclusion_is_scoped_and_does_not_exempt_same_number_in_content(self):
        self.source.write_text('PDF página 30. ' + self.source.read_text())
        self.work = self.root / 'content'
        self.call('init', '--source', str(self.source))
        inventory = self.inventory()
        inventory['exclusions'] = [{
            'id': 'x01', 'lines': [1, 1], 'quote': 'PDF página 30. ',
            'reason': 'Paginación física, sin modificar el plazo de retención.',
        }]
        self.submit(inventory)
        packet = self.call('next')
        self.assertNotIn('PDF página', packet['content_source'])
        self.assertIn('30 días', packet['content_source'])
        bad = self.candidate('Archivo: retener; no borrar antes.\n', mappings=[
            {'unit': 'u01', 'quote': 'retener'}, {'unit': 'u02', 'quote': 'no borrar antes'},
        ])
        before = self.snapshot()
        self.submit(bad, expected=2)
        self.call('retain', '--block', 'b0001', '--reason', 'No reintroducir soporte.', expected=2)
        self.assertEqual(before, self.snapshot())
        self.submit(self.candidate())
        review = self.review()
        self.submit(review, expected=2)
        review['exclusion_checks'] = [{
            'id': 'x01', 'justified': True,
            'reason': 'Sólo se retira la paginación; el plazo de 30 días queda completo.',
        }]
        self.submit(review)
        self.submit(self.global_review(), 'global')
        self.call('build')
        artifact = (self.work / 'artifact.md').read_text()
        self.assertIn('30 días', artifact)
        self.assertNotIn('PDF página', artifact)
        receipt = json.loads((self.work / 'receipt.json').read_text())
        self.assertEqual(receipt['blocks'][0]['exclusions'], inventory['exclusions'])
        before = self.snapshot()
        self.assertTrue(self.call('build')['reused'])
        self.assertEqual(before, self.snapshot())

    def test_exclusion_quotes_require_exact_unambiguous_nonoverlapping_spans(self):
        self.source.write_text('Página 1.\nPágina 1.\nRetener 30 días; no borrar antes.\n')
        self.work = self.root / 'exclusion-spans'
        self.call('init', '--source', str(self.source))
        inventory = self.inventory()
        cases = [
            [{'id': 'x01', 'lines': [1, 2], 'quote': 'Página 1.', 'reason': 'Paginación.'}],
            [{'id': 'x01', 'lines': [1, 1], 'quote': 'Página 2.', 'reason': 'Paginación.'}],
            [{'id': 'x01', 'lines': [1, 1], 'quote': 'Página 1.', 'reason': ''}],
            [{'id': 'x01', 'lines': [1, 1], 'quote': 'Página 1.', 'reason': 'Paginación.'},
             {'id': 'x02', 'lines': [1, 1], 'quote': '1.', 'reason': 'Solapamiento.'}],
        ]
        before = self.snapshot()
        for exclusions in cases:
            inventory['exclusions'] = exclusions
            self.submit(inventory, expected=2)
            self.assertEqual(before, self.snapshot())

    def test_excluding_part_of_a_line_does_not_count_unreviewed_content_as_covered(self):
        self.source.write_text('PDF página 7. Debe retenerse durante 30 días.\nProhibido borrarlo antes.\n')
        self.work = self.root / 'mixed-line'
        self.call('init', '--source', str(self.source))
        inventory = self.inventory()
        for unit in inventory['units']:
            unit['lines'] = [2, 2]
        inventory['exclusions'] = [{
            'id': 'x01', 'lines': [1, 1], 'quote': 'PDF página 7. ', 'reason': 'Paginación.',
        }]
        before = self.snapshot()
        self.submit(inventory, expected=2)
        self.assertEqual(before, self.snapshot())

    def test_support_only_block_has_no_artifact_knowledge_or_invented_question(self):
        self.source.write_text('PDF página 7 de 12. Archivo: `copia.pdf`.\n')
        self.work = self.root / 'support-only'
        self.call('init', '--source', str(self.source))
        inventory = {
            'stage': 'inventory', 'units': [], 'questions': [], 'dependencies': [],
            'exclusions': [{'id': 'x01', 'lines': [1, 1], 'quote': self.source.read_text().strip(),
                            'reason': 'Sólo describe página y nombre de archivo, sin contenido.'}],
            'source_rechecked': True, 'source_review': 'El bloque completo es soporte documental.',
        }
        self.submit(inventory)
        self.submit({'stage': 'candidate', 'text': '', 'mapping': [], 'references': [],
                     'transformations': ['Retira soporte del artefacto.'], 'issues': []})
        review = self.review(exclusion_checks=[{
            'id': 'x01', 'justified': True, 'reason': 'No hay una afirmación sustantiva en el bloque.',
        }])
        self.submit(review)
        self.submit(self.global_review(), 'global')
        self.call('build')
        self.assertEqual((self.work / 'artifact.md').read_text().strip(), '')
        state = helper.load(self.work)
        self.assertIn('copia.pdf', state['sources'][0]['text'])
        self.assertEqual(state['blocks'][0]['inventory']['exclusions'], inventory['exclusions'])

    def test_negative_exclusion_review_cannot_accept_candidate(self):
        self.source.write_text('Página 7.\n' + self.source.read_text())
        self.work = self.root / 'negative-exclusion'
        self.call('init', '--source', str(self.source))
        inventory = self.inventory()
        inventory['exclusions'] = [{
            'id': 'x01', 'lines': [1, 1], 'quote': 'Página 7.', 'reason': 'Paginación.',
        }]
        self.submit(inventory)
        self.submit(self.candidate())
        result = self.submit(self.review(exclusion_checks=[{
            'id': 'x01', 'justified': False, 'reason': 'No se pudo justificar el alcance de la exclusión.',
        }]))
        self.assertFalse(result['accepted'])
        self.assertEqual(self.call('next')['stage'], 'candidate')
        self.call('build', expected=2)

    def test_exclusions_do_not_bypass_fenced_code_protection(self):
        self.source.write_text('```sh\nrun --limit 30\n```\n')
        self.work = self.root / 'code-exclusion'
        self.call('init', '--source', str(self.source))
        inventory = {
            'stage': 'inventory', 'units': [], 'questions': [], 'dependencies': [],
            'exclusions': [{'id': 'x01', 'lines': [1, 3], 'quote': self.source.read_text(),
                            'reason': 'Declaración deliberadamente incorrecta para probar el límite.'}],
            'source_rechecked': True, 'source_review': 'Se prueba que no se puede eliminar código.',
        }
        self.submit(inventory)
        before = self.snapshot()
        self.submit({'stage': 'candidate', 'text': '', 'mapping': [], 'references': [],
                     'transformations': ['Retiro de código declarado como soporte.'], 'issues': []}, expected=2)
        self.assertEqual(before, self.snapshot())

    def test_support_removal_and_content_compression_are_measured_separately(self):
        original_content = self.source.read_text()
        self.source.write_text('PDF página 7 de 12.\n' + original_content)
        self.work = self.root / 'separate-measurement'
        self.call('init', '--source', str(self.source))
        inventory = self.inventory()
        inventory['exclusions'] = [{
            'id': 'x01', 'lines': [1, 1], 'quote': 'PDF página 7 de 12.', 'reason': 'Paginación.',
        }]
        self.submit(inventory)
        candidate = self.candidate(original_content, mappings=[
            {'unit': 'u01', 'quote': '30 días'}, {'unit': 'u02', 'quote': 'Está prohibido borrarlo'},
        ])
        self.submit(candidate)
        self.submit(self.review(exclusion_checks=[{
            'id': 'x01', 'justified': True, 'reason': 'Sólo página y total de páginas.',
        }]))
        state = helper.load(self.work)

        class FakeEncoding:
            def encode(self, value, disallowed_special=()):
                return value.split()

        fake = types.SimpleNamespace(__version__='test', get_encoding=lambda _: FakeEncoding())
        with patch.dict(sys.modules, {'tiktoken': fake}):
            measurement = helper.measure(state, helper.assembly(state))
        self.assertGreater(measurement['excluded_source_tokens'], 0)
        self.assertEqual(measurement['saving_vs_content_tokens'], 0)
        self.assertEqual(measurement['compression_status'], 'NO_GAIN')
        self.assertEqual(measurement['source_tokens'] - measurement['candidate_tokens'],
                         measurement['excluded_source_tokens'] + measurement['saving_vs_content_tokens'])

    def test_inventory_requires_mechanical_nonempty_line_range_coverage(self):
        self.source.write_text('Primera cláusula.\n\nSegunda cláusula.\n')
        self.work = self.root / 'gaps'
        self.call('init', '--source', str(self.source), work=self.work)
        packet = self.call('next', work=self.work)
        inventory = {
            'stage': 'inventory',
            'units': [{'id': 'u01', 'lines': [packet['lines'][0], packet['lines'][0]],
                       'statement': 'Solo se registró la primera cláusula.'}],
            'questions': [{'id': 'q01', 'question': '¿Cuál es la primera?', 'expected': 'Primera.'}],
            'dependencies': [], 'source_rechecked': True, 'source_review': 'Revisé el rango inicial.',
        }
        before = self.snapshot(self.work)
        self.submit(inventory, expected=2, work=self.work)
        self.assertEqual(before, self.snapshot(self.work))

    def test_evidence_is_optional_but_when_present_must_match_range(self):
        self.submit(self.inventory())
        candidate = self.candidate()
        self.submit(candidate)
        self.assertEqual(self.call('next')['stage'], 'review')
        bad_inventory = self.inventory()
        bad_inventory['units'][0]['evidence'] = 'No existe en este rango.'
        other_work = self.root / 'bad-evidence'
        self.call('init', '--source', str(self.source), work=other_work)
        self.submit(bad_inventory, expected=2, work=other_work)

    def test_candidate_digest_binds_references_and_no_backward_inventory_is_required(self):
        self.submit(self.inventory())
        candidate = self.candidate()
        self.submit(candidate)
        packet = self.call('next')
        self.assertEqual(packet['schema']['candidate_sha256'], helper.candidate_digest(candidate))
        self.assertEqual(helper.candidate_digest(candidate['text'], candidate['references']),
                         packet['schema']['candidate_sha256'])
        self.assertNotIn('backward', candidate)
        review = self.review(packet)
        review.pop('literal_changes')
        before = self.snapshot()
        self.assertEqual(self.submit(review)['stage'], 'accepted')
        self.assertNotEqual(before, self.snapshot())

    def test_protected_code_inline_link_and_number_or_literal_change(self):
        self.source.write_text('Ejecuta `cmd --limit 30` y consulta [guía](docs/guide.md).\n')
        self.work = self.root / 'protected'
        self.call('init', '--source', str(self.source), work=self.work)
        packet = self.call('next', work=self.work)
        inventory = {
            'stage': 'inventory',
            'units': [{'id': 'u01', 'lines': packet['lines'], 'statement': 'Ejecuta el comando y consulta la guía.'}],
            'questions': [{'id': 'q01', 'question': '¿Qué comando?', 'expected': '`cmd --limit 30`'}],
            'dependencies': [], 'source_rechecked': True, 'source_review': 'Cotejé comando, número y destino.',
        }
        self.submit(inventory, work=self.work)
        candidate = {
            'stage': 'candidate', 'text': 'Ejecuta `cmd --limit 30` y consulta [guía](docs/guide.md).\n',
            'mapping': [{'unit': 'u01', 'quote': '`cmd --limit 30`'}], 'references': [],
            'transformations': ['Compacta el conector preservando elementos técnicos.'],
            'literal_changes': [], 'issues': [],
        }
        self.submit(candidate, work=self.work)
        bad = dict(candidate)
        bad['text'] = 'Ejecuta `cmd --limit 20` y consulta [guía](docs/guide.md).\n'
        bad['mapping'] = [{'unit': 'u01', 'quote': '`cmd --limit 20`'}]
        before = self.snapshot(self.work)
        self.submit(bad, expected=2, work=self.work)
        self.assertEqual(before, self.snapshot(self.work))

    def test_literal_change_must_match_missing_source_number_and_review_must_cotejar_it(self):
        self.source.write_text('Página 2: encabezado común.\n')
        self.work = self.root / 'literal-change'
        self.call('init', '--source', str(self.source), work=self.work)
        packet = self.call('next', work=self.work)
        inventory = {
            'stage': 'inventory',
            'units': [{'id': 'u01', 'lines': packet['lines'], 'statement': 'El encabezado está en una página.'}],
            'questions': [{'id': 'q01', 'question': '¿Qué página?', 'expected': 'Página 2.'}],
            'dependencies': [], 'source_rechecked': True, 'source_review': 'Cotejé el número de página.',
        }
        self.submit(inventory, work=self.work)
        candidate = {
            'stage': 'candidate', 'text': 'Páginas 1–19: encabezado común.\n',
            'mapping': [{'unit': 'u01', 'quote': 'Páginas 1–19: encabezado común.'}],
            'references': [], 'transformations': ['Agrupa la paginación en el rango continuo.'],
            'literal_changes': [{
                'literal': '2', 'quote': 'Páginas 1–19',
                'reason': 'El 2 es número de página comprendido en el rango, no dato de dominio.',
            }],
            'issues': [],
        }
        self.submit(candidate, work=self.work)
        packet = self.call('next', work=self.work)
        missing_review = self.review(packet)
        missing_review.pop('literal_changes')
        self.submit(missing_review, expected=2, work=self.work)
        review = self.review(packet, literal_changes=[{
            'literal': '2', 'preserved': True,
            'reason': 'Se cotejó que el 2 es página incluida en el rango y no plazo.',
        }])
        self.assertEqual(self.submit(review, work=self.work)['stage'], 'accepted')

    def test_factor_previous_accepted_block_and_expose_referenced_context(self):
        _, work = self._multi_block_work()
        self._accept_multi(work, 'b0001', self._multi_candidate(work, 'b0001', 'Mismo encabezado.\n'))
        first = json.loads((work / 'state.json').read_text())['blocks'][0]['accepted']
        candidate = self._multi_candidate(
            work, 'b0002', 'Mismo encabezado.\n',
            references=[{'block': 'b0001', 'sha256': first['sha256']}], ref_id='b0001')
        self._accept_multi(work, 'b0002', candidate)
        packet = self.call('next', work=work)
        self.assertEqual(packet['stage'], 'inventory')
        self.submit(self._multi_inventory(work, 'b0003'), 'b0003', work=work)
        packet = self.call('next', work=work)
        self.assertEqual(packet['stage'], 'candidate')
        second = json.loads((work / 'state.json').read_text())['blocks'][1]['accepted']
        empty = self._multi_candidate(
            work, 'b0003', '',
            references=[{'block': 'b0002', 'sha256': second['sha256']}], ref_id='b0002')
        self.submit(empty, 'b0003', work=work)
        b3_packet = self.call('next', work=work)
        self.assertEqual(b3_packet['stage'], 'review')
        self.assertEqual(b3_packet['referenced_context'][0]['block'], 'b0001')
        self.assertEqual(b3_packet['referenced_context'][1]['block'], 'b0002')
        self.assertEqual(b3_packet['referenced_context'][0]['sha256'], first['sha256'])
        self.submit(self.review(b3_packet), 'b0003', work=work)
        global_packet = self.call('show', '--block', 'global', work=work)
        self.assertEqual(global_packet['text'], 'Mismo encabezado.\n\nMismo encabezado.\n')
        self.assertEqual(global_packet['assembly_sha256'], helper.digest(global_packet['text']))

    def test_empty_candidate_is_allowed_only_when_all_units_map_to_reference(self):
        _, work = self._multi_block_work('Encabezado.\n\nDetalle.\n')
        self._accept_multi(work, 'b0001', self._multi_candidate(
            work, 'b0001', 'Encabezado.\n', quote='Encabezado.'))
        state = json.loads((work / 'state.json').read_text())
        accepted = state['blocks'][0]['accepted']
        self.submit(self._multi_inventory(work, 'b0002'), 'b0002', work=work)
        bad = self._multi_candidate(work, 'b0002', '', references=[
            {'block': 'b0001', 'sha256': accepted['sha256']}
        ])
        bad['mapping'] = [{'unit': 'u01', 'quote': 'Encabezado.'}]
        self.submit(bad, 'b0002', expected=2, work=work)
        good = dict(bad)
        good['mapping'] = [{'unit': 'u01', 'quote': 'Encabezado.', 'block': 'b0001'}]
        self.submit(good, 'b0002', work=work)

    def test_references_reject_unknown_future_cross_source_and_stale_hash(self):
        source2 = self.root / 'second.md'
        source2.write_text('Otra fuente.\n')
        work = self.root / 'refs'
        self.call('init', '--source', str(self.source), '--source', str(source2), work=work)
        packet1 = self.call('show', '--block', 'b0001', work=work)
        inventory1 = {
            'stage': 'inventory',
            'units': [{'id': 'u01', 'lines': packet1['lines'],
                       'statement': 'Se conserva el archivo y su plazo.'}],
            'questions': [{'id': 'q01', 'question': '¿Cuál es el plazo?', 'expected': '30 días.'}],
            'dependencies': [], 'source_rechecked': True,
            'source_review': 'Cotejé la primera fuente completa.',
        }
        self.submit(inventory1, 'b0001', work=work)
        future = self._multi_candidate(work, 'b0001', '',
                                        references=[{'block': 'b0001', 'sha256': '0' * 64}], ref_id='b0001')
        before = self.snapshot(work)
        self.submit(future, 'b0001', expected=2, work=work)
        self.assertEqual(before, self.snapshot(work))
        # Complete the first block and prepare the second block inventory.
        candidate1 = {
            'stage': 'candidate', 'text': 'Archivo: retener 30 días. No borrar antes.\n',
            'mapping': [{'unit': 'u01', 'quote': 'Archivo: retener 30 días.'}],
            'references': [], 'transformations': ['Compacta la forma manteniendo el texto.'],
            'literal_changes': [], 'issues': [],
        }
        self.submit(candidate1, 'b0001', work=work)
        packet = self.call('next', work=work)
        self.submit(self.review(packet), 'b0001', work=work)
        packet = self.call('next', work=work)
        self.assertEqual(packet['block'], 'b0002')
        self.submit(self._multi_inventory(work, 'b0002'), 'b0002', work=work)
        for ref_id, ref_hash in (('b9999', '0' * 64), ('b0001', '0' * 64)):
            bad = self._multi_candidate(work, 'b0002', '',
                                        references=[{'block': ref_id, 'sha256': ref_hash}], ref_id=ref_id)
            before = self.snapshot(work)
            self.submit(bad, 'b0002', expected=2, work=work)
            self.assertEqual(before, self.snapshot(work))

    def test_reopen_archives_evidence_invalidates_recursive_consumers_and_is_idempotent(self):
        _, work = self._multi_block_work()
        self._accept_multi(work, 'b0001', self._multi_candidate(work, 'b0001', 'Mismo encabezado.\n'))
        state = json.loads((work / 'state.json').read_text())
        b1hash = state['blocks'][0]['accepted']['sha256']
        self._accept_multi(work, 'b0002', self._multi_candidate(
            work, 'b0002', 'Mismo encabezado.\n',
            references=[{'block': 'b0001', 'sha256': b1hash}], ref_id='b0001'))
        state = json.loads((work / 'state.json').read_text())
        b2hash = state['blocks'][1]['accepted']['sha256']
        self._accept_multi(work, 'b0003', self._multi_candidate(
            work, 'b0003', '', references=[{'block': 'b0002', 'sha256': b2hash}], ref_id='b0002'))
        self.submit(self.global_review(work), 'global', work=work)
        self.call('build', work=work)
        old_artifact = (work / 'artifact.md').read_bytes()
        old_receipt = (work / 'receipt.json').read_bytes()
        result = self.call('reopen', '--block', 'b0001', '--reason', 'Revisar la deduplicación.',
                           '--candidate-sha256', b1hash, work=work)
        self.assertEqual(result['invalidated'], ['b0002', 'b0003'])
        state = json.loads((work / 'state.json').read_text())
        self.assertNotIn('accepted', state['blocks'][0])
        self.assertNotIn('candidate', state['blocks'][0])
        self.assertNotIn('review', state['blocks'][0])
        self.assertEqual(state['blocks'][0]['seen'], [])
        self.assertIn('accepted', state['blocks'][0]['history'][-1]['archived'])
        self.assertEqual(state['blocks'][1]['stage'] if 'stage' in state['blocks'][1] else helper.stage(state['blocks'][1]),
                         'candidate')
        self.assertEqual(old_artifact, (work / 'artifact.md').read_bytes())
        self.assertEqual(old_receipt, (work / 'receipt.json').read_bytes())
        before = self.snapshot(work)
        repeated = self.call('reopen', '--block', 'b0001', '--reason', 'Revisar la deduplicación.',
                             '--candidate-sha256', b1hash, work=work)
        self.assertTrue(repeated['reused'])
        self.assertEqual(before, self.snapshot(work))
        self.call('reopen', '--block', 'b0001', '--reason', 'Otro motivo.',
                  '--candidate-sha256', '0' * 64, expected=2, work=work)
        self.assertEqual(before, self.snapshot(work))
        # A repaired accepted candidate gets a new hash. The first hash is stale,
        # while a second reopen using the new hash is a new, valid request.
        self._accept_multi(work, 'b0001', self._multi_candidate(
            work, 'b0001', 'Mismo encabezado corregido.\n', quote='Mismo encabezado corregido.'))
        repaired = json.loads((work / 'state.json').read_text())['blocks'][0]['accepted']['sha256']
        self.assertNotEqual(repaired, b1hash)
        before = self.snapshot(work)
        self.call('reopen', '--block', 'b0001', '--reason', 'Usar el hash antiguo.',
                  '--candidate-sha256', b1hash, expected=2, work=work)
        self.assertEqual(before, self.snapshot(work))
        second = self.call('reopen', '--block', 'b0001', '--reason', 'Revisar la reparación.',
                           '--candidate-sha256', repaired, work=work)
        self.assertFalse(second['reused'])
        self.assertEqual(second['invalidated'], [])

    def test_retain_changed_provider_invalidates_consumer(self):
        _, work = self._multi_block_work('Original.\n\nOriginal.\n')
        self._accept_multi(work, 'b0001', self._multi_candidate(
            work, 'b0001', 'Versión.\n', quote='Versión.'))
        state = json.loads((work / 'state.json').read_text())
        provider_hash = state['blocks'][0]['accepted']['sha256']
        self._accept_multi(work, 'b0002', self._multi_candidate(
            work, 'b0002', '', references=[{'block': 'b0001', 'sha256': provider_hash}],
            ref_id='b0001', quote='Versión.'))
        result = self.call('retain', '--block', 'b0001', '--reason', 'La forma compacta deja duda.', work=work)
        self.assertEqual(result['invalidated'], ['b0002'])
        state = json.loads((work / 'state.json').read_text())
        self.assertEqual(state['blocks'][0]['accepted']['kind'], 'retained')
        self.assertEqual(helper.stage(state['blocks'][1]), 'candidate')
        self.assertTrue(state['blocks'][1]['history'][-1]['archived']['candidate'])

    def test_reviewer_can_accept_a_negation_mutation_but_receipt_does_not_claim_detection(self):
        # Leave enough source wording for the deliberate negation mutation to
        # remain buildable when a real tokenizer is installed; this test checks
        # the declared reviewer judgment, not a forced token regression.
        self.source.write_text('Debe hacerlo de forma inmediata.\n')
        self.work = self.root / 'negation'
        self.call('init', '--source', str(self.source), work=self.work)
        packet = self.call('next', work=self.work)
        inventory = {
            'stage': 'inventory',
            'units': [{'id': 'u01', 'lines': packet['lines'], 'statement': 'Debe hacerlo.'}],
            'questions': [{'id': 'q01', 'question': '¿Debe hacerlo?', 'expected': 'Sí.'}],
            'dependencies': [], 'source_rechecked': True, 'source_review': 'Cotejé la modalidad verbal.',
        }
        self.submit(inventory, work=self.work)
        candidate = self.candidate('No debe hacerlo.\n',
                                   mappings=[{'unit': 'u01', 'quote': 'No debe hacerlo.'}])
        self.submit(candidate, work=self.work)
        self.submit(self.review(), work=self.work)
        self.submit(self.global_review(self.work), 'global', work=self.work)
        self.call('build', work=self.work)
        receipt = json.loads((self.work / 'receipt.json').read_text())
        self.assertIn('no prueba equivalencia universal', receipt['claim'])

    def test_measurement_distinguishes_not_measured_no_gain_and_observed_gain(self):
        class FakeEncoding:
            def encode(self, value, disallowed_special=()):
                return value.split()

        fake_tiktoken = types.SimpleNamespace(__version__='test', get_encoding=lambda _: FakeEncoding())
        self.complete()
        state = helper.load(self.work)
        with patch.dict(sys.modules, {'tiktoken': fake_tiktoken}):
            measurement = helper.measure(state, helper.assembly(state))
        self.assertEqual(measurement['tokens_status'], 'MEASURED')
        self.assertEqual(measurement['compression_status'], 'GAIN_OBSERVED')
        self.assertTrue(measurement['transformation_observed'])
        self.call('retain', '--block', 'b0001', '--reason', 'Se conserva literalmente.')
        state = helper.load(self.work)
        with patch.dict(sys.modules, {'tiktoken': fake_tiktoken}):
            measurement = helper.measure(state, helper.assembly(state))
        self.assertEqual(measurement['compression_status'], 'NO_GAIN')
        with patch.dict(sys.modules, {'tiktoken': None}):
            not_measured = helper.measure(state, helper.assembly(state))
        self.assertEqual(not_measured['compression_status'], 'NOT_MEASURED')

    def test_token_regression_advises_repair_without_dropping_blocks(self):
        self.complete()
        before = self.snapshot()
        with patch.object(helper, 'measure', return_value={
            'tokens_status': 'MEASURED', 'saving_tokens': -1, 'compression_status': 'NO_GAIN'
        }):
            with self.assertRaisesRegex(helper.Conflict, 'TOKEN_REGRESSION'):
                helper.build(helper.load(self.work), self.work)
        self.assertEqual(before, self.snapshot())
        state = helper.load(self.work)
        self.assertEqual(helper.stage(state['blocks'][0]), 'accepted')

    def test_build_and_outputs_remain_idempotent_and_manual_edits_are_guarded(self):
        self.complete()
        result = self.call('build')
        self.assertEqual(set(result['changed_files']), {'artifact.md', 'receipt.json'})
        snapshot = {path.name: (path.read_bytes(), path.stat().st_mtime_ns)
                    for path in self.work.iterdir() if path.is_file()}
        self.assertTrue(self.call('build')['reused'])
        self.assertEqual(snapshot, {path.name: (path.read_bytes(), path.stat().st_mtime_ns)
                                    for path in self.work.iterdir() if path.is_file()})
        artifact = self.work / 'artifact.md'
        artifact.write_text('Edición manual ajena.\n')
        before = self.snapshot()
        self.call('build', expected=2)
        self.assertEqual(artifact.read_text(), 'Edición manual ajena.\n')
        self.assertEqual(before, self.snapshot())

    def test_init_and_accepted_steps_remain_noops(self):
        before = self.snapshot()
        self.assertTrue(self.call('init', '--source', str(self.source))['reused'])
        self.assertEqual(before, self.snapshot())
        inventory = self.inventory()
        self.submit(inventory)
        self.submit(self.candidate())
        review = self.review()
        self.submit(review)
        before = self.snapshot()
        self.assertTrue(self.submit(review)['reused'])
        self.assertTrue(self.submit(inventory)['reused'])
        self.assertEqual(before, self.snapshot())

    def test_changed_source_and_parameters_preserve_state(self):
        before = self.snapshot()
        self.call('init', '--source', str(self.source), '--max-chars', '1000', expected=2)
        self.assertEqual(before, self.snapshot())
        self.source.write_text('Otra fuente.\n')
        self.call('next', expected=2)
        self.call('init', '--source', str(self.source), expected=2)
        self.assertEqual(before, self.snapshot())

    def test_partition_covers_exact_source_and_never_splits_fenced_code(self):
        text = '# Título\n\nPárrafo.\n\n```python\n' + ('x = 3\n\n' * 30) + '```\n\nFinal.\n'
        lines = text.splitlines(keepends=True)
        parts = [''.join(lines[first - 1:last]) for first, last in helper.split_source(text, 70)]
        self.assertEqual(''.join(parts), text)
        self.assertEqual(sum(part.count('```') == 2 for part in parts), 1)
        self.assertTrue(any(len(part) > 70 and '```python' in part for part in parts))

    def test_stale_and_negative_reviews_cannot_accept_or_replay_a_rejected_candidate(self):
        self.submit(self.inventory())
        candidate = self.candidate()
        self.submit(candidate)
        review = self.review()
        current_hash = review['candidate_sha256']
        self.assertEqual(current_hash, helper.candidate_digest(candidate))
        review['candidate_sha256'] = 'stale'
        before = self.snapshot()
        self.submit(review, expected=2)
        self.assertEqual(before, self.snapshot())
        review['candidate_sha256'] = current_hash
        review['unit_checks'][1]['preserved'] = False
        self.assertFalse(self.submit(review)['accepted'])
        self.assertEqual(self.call('next')['stage'], 'candidate')
        before = self.snapshot()
        self.assertTrue(self.submit(candidate)['reused'])
        self.assertEqual(self.call('next')['stage'], 'candidate')
        self.assertEqual(before, self.snapshot())

    def test_lock_and_source_snapshot_tampering_fail_without_mutation(self):
        before = self.snapshot()
        with helper.locked(self.work):
            self.call('next', expected=2)
        self.assertEqual(before, self.snapshot())
        state = json.loads((self.work / 'state.json').read_text())
        state['sources'][0]['text'] = 'Alteración accidental.\n'
        (self.work / 'state.json').write_text(json.dumps(state))
        before = self.snapshot()
        self.call('next', expected=2)
        self.assertEqual(before, self.snapshot())

    def test_build_requires_global_and_recovers_missing_derived_file(self):
        self.call('build', expected=2)
        self.complete()
        self.call('build')
        receipt = self.work / 'receipt.json'
        expected = receipt.read_bytes()
        receipt.unlink()
        self.assertEqual(self.call('build')['changed_files'], ['receipt.json'])
        self.assertEqual(receipt.read_bytes(), expected)

    def test_interruption_between_outputs_can_resume(self):
        self.complete()
        state = helper.load(self.work)
        real = helper.write_if_changed

        def interrupted(path, data):
            if path.name == 'receipt.json':
                raise OSError('synthetic interrupted write')
            return real(path, data)

        with patch.object(helper, 'write_if_changed', side_effect=interrupted):
            with self.assertRaises(OSError):
                helper.build(state, self.work)
        self.assertTrue((self.work / 'artifact.md').exists())
        self.assertEqual(self.call('build')['changed_files'], ['receipt.json'])

    def test_retain_invalidates_global_and_preserves_source_spacing(self):
        self.complete()
        self.call('build')
        self.call('retain', '--block', 'b0001', '--reason', 'Conservación literal.')
        before = self.snapshot()
        self.assertTrue(self.call('retain', '--block', 'b0001', '--reason', 'Conservación literal.')['reused'])
        self.assertEqual(before, self.snapshot())
        self.call('build', expected=2)
        self.submit(self.global_review(), 'global')
        self.call('build')
        self.assertEqual((self.work / 'artifact.md').read_text(), self.source.read_text())
        receipt = json.loads((self.work / 'receipt.json').read_text())['blocks'][0]
        self.assertEqual(receipt['kind'], 'retained')
        self.assertIsNone(receipt['review_hash'])
        self.assertIsNone(receipt['reader_isolation_declared'])
        self.source.write_text('Primer párrafo.\n\n\n\nSegundo párrafo.\n\n\nFinal.\n')
        self.work = self.root / 'spacing'
        self.call('init', '--source', str(self.source), '--max-chars', '20')
        for row in self.call('next')['index']:
            self.call('retain', '--block', row['id'], '--reason', 'Conservación literal completa.')
        self.submit(self.global_review(), 'global')
        self.call('build')
        self.assertEqual((self.work / 'artifact.md').read_text(), self.source.read_text())

    def test_oversize_and_multiple_source_boundaries_remain_explicit(self):
        other = self.root / 'second.txt'
        other.write_text('Fuente independiente.\n')
        self.work = self.root / 'many'
        self.call('init', '--source', str(self.source), '--source', str(other), '--max-chars', '10')
        packet = self.call('next')
        self.assertTrue(packet['oversize'])
        self.assertEqual(len(packet['index']), 2)
        for block in ('b0001', 'b0002'):
            self.call('retain', '--block', block, '--reason', 'Literal de prueba.')
        self.submit(self.global_review(), 'global')
        self.call('build')
        expected = self.source.read_text().rstrip() + '\n\n---\n\n' + other.read_text()
        self.assertEqual((self.work / 'artifact.md').read_text(), expected)
        receipt = json.loads((self.work / 'receipt.json').read_text())
        self.assertEqual([row['origin'] for row in receipt['sources']],
                         [str(self.source), str(other)])
        measurements = receipt['measurements']
        self.assertEqual(measurements['source_characters'], measurements['candidate_characters'])


if __name__ == '__main__':
    unittest.main()
