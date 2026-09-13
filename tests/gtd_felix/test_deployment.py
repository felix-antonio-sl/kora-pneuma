"""Offline synthetic releases/environments; never touch installed services."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from gtd_felix import deployment as dep
from gtd_felix.service import GTDService


class DeploymentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.shared = tempfile.TemporaryDirectory()
        root = Path(cls.shared.name)
        wheels = root / 'wheels'
        wheels.mkdir(mode=0o700)
        # Deliberately synthetic, not a claim to exercise aiohttp behavior.
        filename = 'aiohttp-3.14.3-py3-none-any.whl'
        with zipfile.ZipFile(wheels / filename, 'w') as z:
            z.writestr('aiohttp/__init__.py', '__version__="3.14.3"\n')
            z.writestr('aiohttp-3.14.3.dist-info/METADATA', 'Metadata-Version: 2.1\nName: aiohttp\nVersion: 3.14.3\n')
            z.writestr('aiohttp-3.14.3.dist-info/WHEEL', 'Wheel-Version: 1.0\nGenerator: synthetic\nRoot-Is-Purelib: true\nTag: py3-none-any\n')
            z.writestr('aiohttp-3.14.3.dist-info/RECORD', '')
        cls.lock = {filename: {'name': 'aiohttp', 'version': '3.14.3',
            'sha256': hashlib.sha256((wheels / filename).read_bytes()).hexdigest()}}
        cls.wheels = wheels
        cls.environment = dep.prepare_environment(sys.executable, root / 'environment', wheels, cls.lock)

    @classmethod
    def tearDownClass(cls):
        cls.shared.cleanup()

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.source = self.root / 'source'
        (self.source / 'runtime/gtd_felix').mkdir(parents=True)
        (self.source / 'references').mkdir()
        self.files = {'SKILL.md': 'Instructions', 'references/operations.md': 'Operations',
            'runtime/pyproject.toml': '[project]\nname="synthetic"\n',
            'runtime/gtd_felix/__init__.py': 'VERSION="one"\n',
            'runtime/gtd_felix/deployment.py': '# synthetic launch fixture\n',
            'runtime/gtd_felix/__main__.py': 'from . import VERSION\nprint(VERSION)\n'}
        for name, content in self.files.items():
            (self.source / name).write_text(content)
        self.releases = self.root / 'releases'

    def tearDown(self):
        self.temp.cleanup()

    def prepare(self):
        reviewed = {n: hashlib.sha256((self.source / n).read_bytes()).hexdigest() for n in self.files}
        return dep.prepare_release(self.source, self.releases, reviewed, self.environment)

    def test_release_switch_rollback_and_running_process_pin(self):
        first = self.prepare()
        selection = self.root / 'selected.json'
        old = dep.select_release(self.releases, first['release_id'], selection)
        code = 'from gtd_felix import VERSION; print(VERSION,flush=True); input(); print(VERSION,flush=True)'
        process = subprocess.Popen([self.environment['python'], '-B', '-c', code],
            cwd=old / 'runtime', stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        try:
            self.assertEqual(process.stdout.readline().strip(), 'one')
            (self.source / 'runtime/gtd_felix/__init__.py').write_text('VERSION="two"\n')
            second = self.prepare()
            new = dep.select_release(self.releases, second['release_id'], selection)
            self.assertNotEqual(old, new)
            output = subprocess.check_output([self.environment['python'], '-B', '-m', 'gtd_felix'], cwd=new / 'runtime', text=True)
            self.assertEqual(output.strip(), 'two')
            self.assertEqual(process.communicate('\n', timeout=5)[0].strip(), 'one')
            self.assertEqual(dep.select_release(self.releases, first['release_id'], selection), old)
            unit = dep.render_user_unit(old, self.environment['python'], self.root / 'config.json')
            self.assertIn(str(old / 'runtime'), unit)
            self.assertIn('StandardError=null', unit)
            self.assertNotIn(str(selection), unit)
        finally:
            if process.poll() is None:
                process.kill()
                process.wait()

    def test_corruption_extra_secret_symlink_and_review_mismatch_fail(self):
        receipt = self.prepare()
        release = Path(receipt['path'])
        (release / 'secret.json').write_text('{}')
        with self.assertRaises(ValueError):
            dep.select_release(self.releases, receipt['release_id'], self.root / 'selected')
        (release / 'secret.json').unlink()
        (release / 'SKILL.md').write_text('changed')
        with self.assertRaises(ValueError):
            dep.verify_release(release, receipt['release_id'])
        name = 'runtime/gtd_felix/__main__.py'
        (self.source / name).unlink()
        (self.source / name).symlink_to(self.source / 'SKILL.md')
        with self.assertRaises(ValueError):
            self.prepare()
        with self.assertRaises(ValueError):
            dep.prepare_release(self.source, self.releases, {'../secret': '0' * 64}, self.environment)

    def test_source_change_during_copy_is_not_published(self):
        reviewed = {n: hashlib.sha256((self.source / n).read_bytes()).hexdigest() for n in self.files}
        original = dep._write
        def write(path, data):
            original(path, data)
            if path.name == 'SKILL.md':
                (self.source / 'SKILL.md').write_text('concurrent correction')
        with patch.object(dep, '_write', side_effect=write), self.assertRaises(ValueError):
            dep.prepare_release(self.source, self.releases, reviewed, self.environment)
        self.assertEqual(list(self.releases.iterdir()), [])

    def test_environment_drift_and_source_only_cannot_select(self):
        file = Path(self.environment['root']) / 'requirements.lock'
        original = file.read_bytes()
        try:
            file.write_bytes(original + b'\n')
            with self.assertRaises(ValueError):
                dep.verify_environment(self.environment)
        finally:
            file.write_bytes(original)
        mutable = dep.inspect_environment(self.environment['python'])
        reviewed = {n: hashlib.sha256((self.source / n).read_bytes()).hexdigest() for n in self.files}
        receipt = dep.prepare_release(self.source, self.releases, reviewed, mutable)
        self.assertEqual(receipt['status'], 'prepared_source_only')
        with self.assertRaises(ValueError):
            dep.select_release(self.releases, receipt['release_id'], self.root / 'selected')
        with self.assertRaises(ValueError):
            dep.prepare_environment(sys.executable, self.root / 'bad-env', self.wheels,
                {k: dict(v, sha256='0' * 64) for k, v in self.lock.items()})
        self.assertFalse((self.root / 'bad-env').exists())

    def test_hardlink_and_launch_drift_fail_before_exec(self):
        receipt = self.prepare()
        root = Path(receipt['path'])
        os.link(root / 'SKILL.md', self.root / 'alias')
        with self.assertRaises(ValueError):
            dep.verify_release(root, receipt['release_id'])
        (self.root / 'alias').unlink()
        (root / 'SKILL.md').write_text('changed before launch')
        with patch.object(dep.os, 'execv') as execute, self.assertRaises(ValueError):
            dep.launch_release(root, self.root / 'config.json')
        execute.assert_not_called()

    def test_unit_and_final_exec_ignore_python_environment_injection(self):
        import shlex
        attacker = self.root / 'external-python'
        (attacker / 'aiohttp').mkdir(parents=True)
        (attacker / 'aiohttp/__init__.py').write_text('raise RuntimeError("external dependency executed")\n')
        # Run the actual deployment entrypoint, then its real exec into the fixture app.
        (self.source / 'runtime/gtd_felix/deployment.py').write_text(Path(dep.__file__).read_text())
        (self.source / 'runtime/gtd_felix/__main__.py').write_text(
            'import aiohttp,json,os,sys\n'
            'print(json.dumps({"dependency":aiohttp.__version__,"ignore_environment":sys.flags.ignore_environment,'
            '"no_user_site":sys.flags.no_user_site,"app_environment_preserved":os.environ.get("GTD_SYNTHETIC_CONTEXT")=="retained"}))\n')
        receipt = self.prepare()
        release = Path(receipt['path'])
        unit = dep.render_user_unit(release, self.environment['python'], self.root / 'config.json')
        command = next(line.removeprefix('ExecStart=') for line in unit.splitlines() if line.startswith('ExecStart='))
        environment = dict(os.environ, PYTHONPATH=str(attacker), PYTHONHOME=str(attacker),
                           GTD_SYNTHETIC_CONTEXT='retained')
        result = subprocess.run(shlex.split(command), cwd=release / 'runtime', env=environment,
                                capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {'dependency': '3.14.3', 'ignore_environment': 1,
                         'no_user_site': 1, 'app_environment_preserved': True})

    def test_generated_unit_is_accepted_by_systemd_parser(self):
        import shutil
        if not shutil.which('systemd-analyze'):
            self.skipTest('systemd-analyze unavailable')
        receipt = self.prepare()
        unit = self.root / 'gtd-synthetic.service'
        unit.write_text(dep.render_user_unit(Path(receipt['path']), self.environment['python'], self.root / 'config.json'))
        result = subprocess.run(['systemd-analyze', '--user', 'verify', str(unit)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_existing_export_restore_preserves_state_material_and_recovery(self):
        service = GTDService(self.root / 'live')
        try:
            item = service.capture('felix', 'capture', 'Original synthetic source')['item']
            material = service.execute('gtd-felix', {'operation_id': 'material', 'action': 'put_material',
                'item_id': item['id'], 'expected_version': item['version'], 'fields': {'content': 'Synthetic draft'}})
            self.assertEqual(material['status'], 'applied', material)
            result = dep.rehearsal_restore(service, self.root / 'backup.zip', self.root / 'restored')
            self.assertTrue(result['recovery_required'])
            self.assertFalse(result['effects_enabled'])
            self.assertEqual(result['originals'], 2)
            self.assertFalse(service.recovery_required)
        finally:
            service.close()


if __name__ == '__main__':
    unittest.main()
