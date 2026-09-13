"""Private offline recovery: real exported snapshot, synthetic secrets only."""
import io
import json
import os
from pathlib import Path
import stat
import sys
import tempfile
import unittest
import zipfile

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from gtd_felix.service import GTDService
from gtd_felix.recovery_bundle import create, restore


class RecoveryBundleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        service = GTDService(self.root / 'data')
        service.capture('felix', 'fixture', 'Synthetic recovery case')
        self.export = self.root / 'service.zip'
        service.export(self.export)
        service.close()
        self.config = self.root / 'config'
        self.config.mkdir()
        (self.config / '.env').write_bytes(b'SECRET=synthetic-no-disclosure\x00\xff')
        (self.config / 'empty').mkdir()
        self.bundle = self.root / 'bundle.zip'
        self.receipt = {'verified': True, 'evidence_id': 'synthetic-stopped-writers'}

    def tearDown(self):
        self.temp.cleanup()

    def pack(self, **kwargs):
        return create(self.export, {'config': self.config}, self.bundle,
                      quiescence_receipt=kwargs.get('receipt', self.receipt))

    def tamper(self, transform):
        with zipfile.ZipFile(self.bundle) as incoming:
            files = {name: incoming.read(name) for name in incoming.namelist()}
        transform(files)
        with zipfile.ZipFile(self.bundle, 'w') as output:
            for name, data in files.items():
                output.writestr(name, data)

    def test_binary_hidden_files_permissions_and_reconciliation(self):
        self.pack()
        destination = self.root / 'isolated'
        receipt = restore(self.bundle, destination)
        self.assertTrue(receipt['reconciliation_required'])
        self.assertFalse(receipt['services_started'])
        self.assertFalse(receipt['effects_replayed'])
        self.assertEqual((self.config / '.env').read_bytes(), (destination / 'inputs/config/.env').read_bytes())
        self.assertTrue((destination / 'inputs/config/empty').is_dir())
        for path in [destination, *destination.rglob('*')]:
            self.assertEqual(0o700 if path.is_dir() else 0o600, stat.S_IMODE(path.stat().st_mode))
        self.assertEqual(0o600, stat.S_IMODE(self.bundle.stat().st_mode))
        recovered = GTDService.restore(destination / 'service-export.zip', self.root / 'restored-service')
        try:
            self.assertEqual(1, len(recovered.query()))
            self.assertEqual('true', recovered.store.db.execute("SELECT value FROM metadata WHERE key='recovery_required'").fetchone()[0])
        finally:
            recovered.close()

    def test_explicit_quiescence_and_real_export_required(self):
        for receipt in ({}, {'verified': False, 'evidence_id': 'x'}):
            with self.assertRaisesRegex(ValueError, '^recovery_bundle_rejected$'):
                self.pack(receipt=receipt)
        self.export.write_bytes(b'SQLite live or arbitrary file is not export')
        with self.assertRaises(ValueError):
            self.pack()
        self.assertFalse(self.bundle.exists())

    def test_symlinks_hardlinks_and_unsafe_labels_rejected_without_secret_errors(self):
        link = self.config / 'link'
        link.symlink_to(self.config / '.env')
        with self.assertRaisesRegex(ValueError, '^recovery_bundle_rejected$'):
            self.pack()
        link.unlink()
        os.link(self.config / '.env', link)
        with self.assertRaisesRegex(ValueError, '^recovery_bundle_rejected$'):
            self.pack()
        link.unlink()
        with self.assertRaisesRegex(ValueError, '^recovery_bundle_rejected$'):
            create(self.export, {'../synthetic-no-disclosure': self.config}, self.bundle,
                   quiescence_receipt=self.receipt)
        self.assertFalse(self.bundle.exists())

    def test_corruption_rejected_before_destination_created(self):
        self.pack()
        self.tamper(lambda files: files.__setitem__('inputs/config/.env', b'corrupt'))
        destination = self.root / 'isolated'
        with self.assertRaisesRegex(ValueError, '^recovery_bundle_rejected$'):
            restore(self.bundle, destination)
        self.assertFalse(destination.exists())

    def test_path_traversal_and_existing_empty_destination_rejected(self):
        self.pack()
        destination = self.root / 'isolated'
        destination.mkdir(mode=0o700)
        with self.assertRaises(ValueError):
            restore(self.bundle, destination)
        self.assertFalse(list(destination.iterdir()))
        destination.rmdir()
        self.tamper(lambda files: files.__setitem__('../escaped', b'invalid'))
        with self.assertRaises(ValueError):
            restore(self.bundle, destination)
        self.assertFalse(destination.exists())
        self.assertFalse((self.root.parent / 'escaped').exists())

    def test_manifest_directory_traversal_and_file_collision_rejected(self):
        self.pack()
        original = self.bundle.read_bytes()
        for directory in ('../escaped', 'inputs/config/.env/child'):
            self.bundle.write_bytes(original)
            def change(files):
                manifest = json.loads(files['manifest.json'])
                manifest['directories'].append(directory)
                files['manifest.json'] = json.dumps(manifest).encode()
            self.tamper(change)
            with self.assertRaises(ValueError):
                restore(self.bundle, self.root / 'isolated')
            self.assertFalse((self.root / 'isolated').exists())

    def test_snapshot_integrity_checked_even_with_updated_outer_hash(self):
        import hashlib
        self.pack()
        def change(files):
            files['service-export.zip'] = b'not a valid export'
            manifest = json.loads(files['manifest.json'])
            manifest['files']['service-export.zip'] = {'size': len(files['service-export.zip']),
                'sha256': hashlib.sha256(files['service-export.zip']).hexdigest()}
            files['manifest.json'] = json.dumps(manifest).encode()
        self.tamper(change)
        with self.assertRaises(ValueError):
            restore(self.bundle, self.root / 'isolated')
        self.assertFalse((self.root / 'isolated').exists())
