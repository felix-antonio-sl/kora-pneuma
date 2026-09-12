import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml

from kora.authoring import create, retire as retire_product
from kora.catalog import Catalog
from kora.cli import execute, parser
from kora.knowledge import approve, create_draft, retire as retire_knowledge, review, revise
from kora.product_versions import preserve


class HistoricalIntegrityTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.root = self.base / 'machinery'
        self.library = self.base / 'library'
        self.root.mkdir()
        self.library.mkdir()
        self.body = self.base / 'body.md'
        self.body.write_text('Apply the rule unless revoked.\n')

    def catalog(self):
        return Catalog(self.root, knowledge=self.library)

    def check(self, history=False):
        args = ['--root', str(self.root), '--knowledge-root', str(self.library), 'check']
        return execute(parser().parse_args(args + (['--history'] if history else [])))

    def versions(self):
        product = create(self.root, 'skill', 'test', 'reader', 'urn:test:skill:reader',
                         'Read the rule', self.body)
        first = preserve(self.root, product)
        product.content_path.write_text('Apply the revised rule unless revoked.\n')
        second = preserve(self.root, product)
        product_paths = [self.root / 'versions/products/test/reader' / rev for rev in (first, second)]
        draft = create_draft(self.library, 'test', 'rule', 'urn:test:kb:rule',
                             'Rule and exception', self.body)
        first = approve(self.library, draft.id, review(self.library, draft.id)['reviewed_sha256'])
        draft = revise(self.library, draft.id)
        draft.content_path.write_text('Revised rule; revocation still prevails.\n')
        second = approve(self.library, draft.id, review(self.library, draft.id)['reviewed_sha256'])
        knowledge_paths = [self.library / 'versions/test/rule' / item.revision for item in (first, second)]
        return product, second, product_paths, knowledge_paths

    def test_checks_previous_versions_and_retired_identities_without_changing_bytes(self):
        product, knowledge, products, references = self.versions()
        retire_product(self.root, product.id, 'Synthetic retirement', knowledge=self.library)
        retire_knowledge(self.library, knowledge.id, 'Synthetic retirement')
        before = {p: p.read_bytes() for directory in products + references
                  for p in directory.rglob('*') if p.is_file()}
        report = self.check(history=True)
        self.assertTrue(report['ok'], report)
        self.assertEqual(report['archived'], 2)
        self.assertEqual(report['history']['verified'], {'products': 2, 'knowledge': 2})
        self.assertNotIn('todas las revisiones históricas', report['not_checked'])
        self.assertEqual(before, {p: p.read_bytes() for p in before})

    def test_previous_corruption_is_explicit_and_restoring_bytes_recovers_check(self):
        _, _, products, references = self.versions()
        originals = {}
        for directory in (products[0], references[0]):
            path = directory / 'content.md'
            originals[path] = path.read_bytes()
            path.write_text('Corrupted old revision.\n')
        self.assertTrue(self.check()['ok'])
        report = self.check(history=True)
        self.assertFalse(report['ok'])
        self.assertEqual(report['history']['verified'], {'products': 1, 'knowledge': 1})
        self.assertEqual({issue['path'] for issue in report['history']['issues']},
                         {str(products[0]), str(references[0])})
        for path, data in originals.items():
            path.write_bytes(data)
        self.assertTrue(self.check(history=True)['ok'])

    def test_orphan_revisions_are_checked_without_catalog_identity(self):
        _, _, products, references = self.versions()
        shutil.rmtree(self.root / 'products')
        shutil.rmtree(self.library / 'references')
        self.assertEqual(self.catalog().products, {})
        report = self.catalog().historical_integrity()
        self.assertEqual(report['verified'], {'products': 2, 'knowledge': 2})
        (products[0] / 'content.md').write_text('Changed orphan.\n')
        (references[0] / 'content.md').write_text('Changed orphan.\n')
        self.assertEqual(len(self.catalog().historical_integrity()['issues']), 2)

    def test_ordinary_queries_and_check_do_not_scan_history(self):
        self.versions()
        with patch.object(Catalog, 'historical_integrity', side_effect=AssertionError('History scanned')):
            catalog = self.catalog()
            self.assertEqual(catalog.get('urn:test:skill:reader').name, 'reader')
            self.assertEqual(len(catalog.products), 2)
            report = self.check()
            self.assertTrue(report['ok'])
            self.assertNotIn('history', report)
            self.assertIn('todas las revisiones históricas', report['not_checked'])

    def test_malformed_and_linked_entries_are_diagnosed_without_following_them(self):
        bad_hash = self.root / 'versions/products/test/reader/not-a-hash'
        bad_hash.mkdir(parents=True)
        absent_manifest = self.library / 'versions/test/rule' / ('a' * 64)
        absent_manifest.mkdir(parents=True)
        bad_manifest = self.library / 'versions/test/rule' / ('b' * 64)
        bad_manifest.mkdir()
        (bad_manifest / 'object.yaml').write_text('id: first\nid: duplicate\n')
        outside = self.base / 'outside'
        outside.mkdir()
        sentinel = outside / 'object.yaml'
        sentinel.write_text('Must not be read as a version.\n')
        linked = self.library / 'versions/linked'
        linked.symlink_to(outside, target_is_directory=True)
        unexpected_file = self.root / 'versions/products/stray'
        unexpected_file.write_text('Malformed container.\n')
        dangling = self.root / 'versions/dangling'
        dangling.symlink_to(self.base / 'missing')
        report = self.catalog().historical_integrity()
        self.assertEqual(report['verified'], {'products': 0, 'knowledge': 0})
        self.assertEqual({issue['path'] for issue in report['issues']},
                         {str(path) for path in (bad_hash, absent_manifest, bad_manifest,
                                               linked, unexpected_file, dangling)})
        self.assertEqual(sentinel.read_text(), 'Must not be read as a version.\n')

    def test_unknown_publication_hash_format_is_not_accepted_as_historical(self):
        _, _, _, references = self.versions()
        manifest = references[0] / 'object.yaml'
        metadata = yaml.safe_load(manifest.read_text())
        metadata['publication']['hash_mode'] = 'future-format'
        manifest.write_text(yaml.safe_dump(metadata))
        report = self.catalog().historical_integrity()
        self.assertEqual(len(report['issues']), 1)
        self.assertIn('Formato de hash desconocido', report['issues'][0]['error'])

    def test_intact_revision_under_another_identity_is_rejected(self):
        _, _, products, references = self.versions()
        other = create(self.root, 'skill', 'test', 'other', 'urn:test:skill:other',
                       'Another reader', self.body)
        other_revision = preserve(self.root, other)
        alien_product = self.root / 'versions/products/test/other' / other_revision
        misplaced_product = products[0].parent / other_revision
        shutil.copytree(alien_product, misplaced_product)
        draft = create_draft(self.library, 'test', 'other', 'urn:test:kb:other',
                             'Another rule', self.body)
        other_knowledge = approve(self.library, draft.id,
                                  review(self.library, draft.id)['reviewed_sha256'])
        alien_knowledge = self.library / 'versions/test/other' / other_knowledge.revision
        misplaced_knowledge = references[0].parent / other_knowledge.revision
        shutil.copytree(alien_knowledge, misplaced_knowledge)
        report = self.catalog().historical_integrity()
        self.assertEqual({issue['path'] for issue in report['issues']},
                         {str(misplaced_product), str(misplaced_knowledge)})
        self.assertTrue(all('no pertenece' in issue['error'] for issue in report['issues']))

    def test_legacy_modes_are_used_for_an_unreferenced_revision(self):
        revision = 'fd141f821443705800e62b3b2ef26a02e4806cbb74a3482c706c4edcce500630'
        version = self.library / 'versions/test/permission' / revision
        version.mkdir(parents=True)
        (version / 'content.md').write_bytes(b'Valid permission; revocation takes precedence.\n')
        (version / 'object.yaml').write_text(
            'id: urn:test:kb:permission\nkind: knowledge\nname: permission\n'
            'description: Permission and exception\ncontent: content.md\n'
            'publication:\n  status: legacy\n'
            '  sha256: 5f164dd03e0d2f4d0a91cb179e0785682bac2985a20e20f05638a3118cb609ee\n'
        )
        for path in version.iterdir():
            path.chmod(0o644)
        (self.library / 'legacy-modes.yaml').write_text(yaml.safe_dump({
            revision: {'content.md': 0o600, 'object.yaml': 0o664},
        }))
        self.assertEqual(self.catalog().historical_integrity(),
                         {'verified': {'products': 0, 'knowledge': 1}, 'issues': []})
        (version / 'content.md').chmod(0o755)
        self.assertEqual(len(self.catalog().historical_integrity()['issues']), 1)

    def test_cli_returns_failure_for_historical_corruption_and_reports_empty_history(self):
        report = self.check(history=True)
        self.assertTrue(report['ok'])
        self.assertEqual(report['history']['verified'], {'products': 0, 'knowledge': 0})
        _, _, products, _ = self.versions()
        (products[0] / 'content.md').write_text('Corrupted previous version.\n')
        command = [sys.executable, str(Path(__file__).resolve().parents[1] / 'kora_cli.py'),
                   '--root', str(self.root), '--knowledge-root', str(self.library),
                   'check', '--history']
        result = subprocess.run(command, capture_output=True, text=True, timeout=15)
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertFalse(json.loads(result.stdout)['ok'])


if __name__ == '__main__':
    unittest.main()
