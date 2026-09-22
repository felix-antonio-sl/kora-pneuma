"""Recovery and library seam; reviewer statements here are synthetic fixtures."""

import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from kora.catalog import KoraError
from kora.knowledge import approve, create_draft, review as library_review


SCRIPT = Path(os.environ.get('KORA_WORKFLOW_SCRIPT',
    Path(__file__).resolve().parents[1] / 'products/kora/koraficacion-integral/scripts/workflow.py'))
spec = importlib.util.spec_from_file_location('workflow_recovery_test', SCRIPT)
workflow = importlib.util.module_from_spec(spec)
previous = sys.dont_write_bytecode
try:
    sys.dont_write_bytecode = True
    spec.loader.exec_module(workflow)
finally:
    sys.dont_write_bytecode = previous


class RecoveryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.work = self.root / 'work'
        self.body = self.root / 'content.md'
        self.body.write_text('Borrador anterior sin revisión.\n')
        self.source = self.root / 'source.txt'
        self.source.write_text('Si existe reserva o invitación, puede entrar.\n')
        self.proposal = self.root / 'proposal.md'
        self.proposal.write_text('Puede entrar con reserva o invitación.\n')

    def call(self, command, **kwargs):
        from argparse import Namespace
        args = Namespace(command=command, work=str(self.work), source=None, body=None,
                         scope=None, resource=None, require_independent=False,
                         independent_repairs=False, file=None, review=None, base_revision=None)
        for key, value in kwargs.items():
            setattr(args, key, value)
        with workflow.locked(self.work, command == 'init'):
            return workflow.execute(args, self.work)

    def initialize(self):
        return self.call('init', source=[str(self.source)], body=str(self.body), scope='Fuente completa')

    def statement(self, revision):
        value = {'revision': revision, 'reviewer': 'synthetic-fixture',
                 'isolation': 'author_context', 'authored_target': True,
                 'scope': 'full', 'coverage': 'complete', 'result': 'accepted',
                 'evidence': 'Fixture mecánico, no cotejo observado de un modelo.',
                 'issues': [], 'limits': []}
        path = self.root / 'judgment.json'
        path.write_text(json.dumps(value))
        return str(path)

    def test_body_write_interruption_recovers_same_reviewed_target_and_initial_body(self):
        self.initialize()
        target = self.call('preview', file=str(self.proposal))
        judgment = self.statement(target['revision'])
        real = workflow.atomic_write

        def fail_body(path, raw, **kwargs):
            if path == self.body:
                raise OSError('simulated body interruption')
            real(path, raw, **kwargs)

        with patch.object(workflow, 'atomic_write', fail_body):
            with self.assertRaises(OSError):
                self.call('repair', file=str(self.proposal), review=judgment)
        self.assertEqual(self.body.read_text(), 'Borrador anterior sin revisión.\n')
        with self.assertRaisesRegex(workflow.Conflict, 'RECOVERY_REQUIRED'):
            self.call('export')
        self.assertEqual(self.call('recover')['state'], 'reviewed')
        self.assertEqual(self.body.read_bytes(), self.proposal.read_bytes())
        receipt = self.call('export')
        self.assertEqual(Path(receipt['initial_snapshot']).read_text(), 'Borrador anterior sin revisión.\n')
        state = (self.work / 'state.json').read_bytes()
        self.call('recover')
        self.assertEqual((self.work / 'state.json').read_bytes(), state)

    def test_interruption_after_body_before_record_completion_recovers_without_second_edit(self):
        self.initialize()
        real = workflow.save

        def fail_completion(work, state):
            if state['versions'] and state['pending'] is None:
                raise OSError('simulated final state interruption')
            real(work, state)

        with patch.object(workflow, 'save', fail_completion):
            with self.assertRaises(OSError):
                self.call('candidate', file=str(self.proposal))
        body_before = self.body.stat().st_mtime_ns
        self.call('recover')
        self.assertEqual(self.body.stat().st_mtime_ns, body_before)
        self.assertEqual(self.call('status')['state'], 'unreviewed')

    def test_recovery_preserves_foreign_edit(self):
        self.initialize()
        real = workflow.atomic_write
        with patch.object(workflow, 'atomic_write', side_effect=lambda p, r, **kw:
                          (_ for _ in ()).throw(OSError('interrupt')) if p == self.body else real(p, r, **kw)):
            with self.assertRaises(OSError):
                self.call('candidate', file=str(self.proposal))
        self.body.write_text('Edición ajena posterior.\n')
        state = (self.work / 'state.json').read_bytes()
        with self.assertRaisesRegex(workflow.Conflict, 'BODY_CHANGED'):
            self.call('recover')
        self.assertEqual(self.body.read_text(), 'Edición ajena posterior.\n')
        self.assertEqual((self.work / 'state.json').read_bytes(), state)

    def test_edit_after_materialization_precheck_is_preserved(self):
        self.initialize()
        real = workflow.atomic_write

        def edit_then_write(path, raw, **kwargs):
            if path == self.body:
                path.write_text('Edición externa antes del reemplazo.\n')
            real(path, raw, **kwargs)

        with patch.object(workflow, 'atomic_write', edit_then_write):
            with self.assertRaisesRegex(workflow.Conflict, 'BODY_CHANGED'):
                self.call('candidate', file=str(self.proposal))
        self.assertEqual(self.body.read_text(), 'Edición externa antes del reemplazo.\n')
        self.assertTrue(workflow.load(self.work)['pending'])

    def test_symlink_destination_and_source_overwrite_rejected(self):
        linked = self.root / 'linked.md'
        linked.symlink_to(self.body)
        with self.assertRaisesRegex(workflow.Conflict, 'SYMLINK'):
            self.call('init', source=[str(self.source)], body=str(linked), scope='Completa')
        with self.assertRaisesRegex(workflow.Conflict, 'fuente original'):
            self.call('init', source=[str(self.source)], body=str(self.source), scope='Completa')
        (self.root / 'nested').mkdir()
        with self.assertRaisesRegex(workflow.Conflict, 'fuente original'):
            self.call('init', source=[str(self.source)],
                      body=str(self.root / 'nested' / '..' / 'source.txt'), scope='Completa')
        self.assertEqual(self.source.read_text(), 'Si existe reserva o invitación, puede entrar.\n')

    def test_rejected_same_bytes_need_explicit_resolution_before_acceptance(self):
        self.initialize()
        version = self.call('candidate', file=str(self.proposal))
        path = Path(self.statement(version['current_revision']))
        accepted = json.loads(path.read_text())
        path.write_text(json.dumps({**accepted, 'result': 'repair', 'issues': ['Supuesto cambio de modalidad.']}))
        negative = self.call('review', file=str(path))
        path.write_text(json.dumps(accepted))
        before = (self.work / 'state.json').read_bytes()
        with self.assertRaisesRegex(workflow.Conflict, 'OPEN_REVIEW'):
            self.call('review', file=str(path))
        self.assertEqual((self.work / 'state.json').read_bytes(), before)
        path.write_text(json.dumps({**accepted, 'supersedes': negative['review_id'],
                                   'resolution': 'Ambas versiones dicen puede; el hallazgo se retira con cotejo.'}))
        self.assertEqual(self.call('review', file=str(path))['state'], 'reviewed')
        self.assertEqual(len(self.call('export')['history'][0]['reviews']), 2)

    def test_workflow_to_library_publication_and_stale_draft_rejected(self):
        library = self.root / 'library'
        library.mkdir()
        draft = create_draft(library, 'test', 'permission', 'urn:test:kb:permission',
                             'Regla de acceso', self.body, sources=[self.source])
        self.body = draft.content_path
        self.source = draft.directory / draft.metadata['provenance']['sources'][0]['path']
        self.initialize()
        version = self.call('candidate', file=str(self.proposal))
        self.call('review', file=self.statement(version['current_revision']))
        evidence = self.call('export')
        self.assertEqual(evidence['body_sha256'], workflow.digest(draft.content_path.read_bytes()))
        assessed = library_review(library, draft.id)
        published = approve(library, draft.id, assessed['reviewed_sha256'])
        self.assertEqual(published.content_path.read_bytes(), self.proposal.read_bytes())
        self.assertEqual(approve(library, draft.id, assessed['reviewed_sha256']).revision, published.revision)
        self.body.write_text('Alteración posterior a la revisión.\n')
        with self.assertRaises(KoraError):
            approve(library, draft.id, assessed['reviewed_sha256'])
        self.assertEqual(published.content_path.read_bytes(), self.proposal.read_bytes())
        with self.assertRaisesRegex(workflow.Conflict, 'BODY_CHANGED'):
            self.call('export')


if __name__ == '__main__':
    unittest.main()
