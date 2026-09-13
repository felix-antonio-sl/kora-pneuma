"""Private offline recovery unit; caller owns quiescence and input authority.

Never pass a live database: service_export must be GTDService.export's archive.
The receipt is an explicit caller attestation, not independent process detection.
Only logical input labels appear in the manifest. No service is started/stopped.
"""
import argparse
import functools
import io
import json
import os
from pathlib import Path, PurePosixPath
import stat
import tempfile
import zipfile

from .deployment import _json, _path, _private, _read, _sha, _sync, _write
from .service import GTDService

LIMIT = 1024 * 1024 * 1024
MAX_FILES = 100000


def _public_errors(function):
    @functools.wraps(function)
    def guarded(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception:
            # Paths, file contents, credentials and parser excerpts are private.
            raise ValueError('recovery_bundle_rejected') from None
    return guarded


def _name(name):
    if not isinstance(name, str) or not name or '\\' in name or '\x00' in name:
        raise ValueError('unsafe_name')
    path = PurePosixPath(name)
    if path.is_absolute() or '..' in path.parts or str(path) != name or name == '.':
        raise ValueError('unsafe_name')
    return name


def _validate_export(data, parent):
    # Reuse complete snapshot/database/original validation in an isolated stage.
    with tempfile.TemporaryDirectory(dir=parent, prefix='validate-export-') as temp:
        root = Path(temp)
        archive = root / 'export.zip'
        _write(archive, data)
        restored = GTDService.restore(archive, root / 'data')
        restored.close()


def _receipt(value):
    if (not isinstance(value, dict) or set(value) != {'verified', 'evidence_id'}
            or value['verified'] is not True or not isinstance(value['evidence_id'], str)
            or not value['evidence_id'].strip() or len(value['evidence_id']) > 200):
        raise ValueError('quiescence_receipt_required')
    return value


@_public_errors
def create(service_export, inputs, destination, *, quiescence_receipt):
    """Copy explicit {logical_label: absolute_path} files/trees after quiescence.

    Caller verifies all writers stopped before snapshotting these inputs and keeps
    them stopped through completion. Hidden files are included. Trees must contain
    only real directories and singly-linked regular files; no implicit HOME scan.
    """
    receipt = _receipt(quiescence_receipt)
    destination = _path(destination)
    _private(destination.parent)
    if destination.exists() or not isinstance(inputs, dict):
        raise ValueError('invalid_destination_or_inputs')
    files = {'service-export.zip': _read(_path(service_export), LIMIT)}
    directories = set()
    total = len(files['service-export.zip'])
    _validate_export(files['service-export.zip'], destination.parent)

    def collect(source, logical):
        nonlocal total
        source = _path(source)
        info = source.lstat()
        if stat.S_ISDIR(info.st_mode):
            directories.add(logical)
            if len(directories) + len(files) > MAX_FILES:
                raise ValueError('bundle_too_large')
            for child in sorted(source.iterdir()):
                collect(child, _name(logical + '/' + child.name))
        elif stat.S_ISREG(info.st_mode) and info.st_nlink == 1:
            data = _read(source, LIMIT - total)
            total += len(data)
            files[logical] = data
        else:
            raise ValueError('unsafe_input')
        if total > LIMIT or len(directories) + len(files) > MAX_FILES:
            raise ValueError('bundle_too_large')

    for label, source in inputs.items():
        if '/' in _name(label):
            raise ValueError('invalid_label')
        collect(_path(source), 'inputs/' + label)
    manifest = {'format': 'gtd-private-recovery', 'version': 1,
        'quiescence': receipt, 'reconciliation_required': True,
        'directories': sorted(directories),
        'files': {name: {'size': len(data), 'sha256': _sha(data)} for name, data in files.items()}}
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in files.items():
            archive.writestr(name, data)
        archive.writestr('manifest.json', _json(manifest))
    _write(destination, output.getvalue())
    _sync(destination.parent)
    return {'status': 'created', 'sha256': _sha(output.getvalue()),
            'files': len(files), 'reconciliation_required': True}


@_public_errors
def restore(bundle, destination):
    """Validate everything before writing an exclusively NEW isolated directory.

    Restores bytes, not a runnable deployment. Leaves the service export archived;
    separately invoking GTDService.restore preserves its recovery_required marker.
    """
    destination = _path(destination)
    _private(destination.parent)
    if destination.exists():
        raise ValueError('new_destination_required')
    data = _read(_path(bundle), LIMIT + 64 * 1024 * 1024)
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        entries = archive.infolist()
        names = [entry.filename for entry in entries]
        if (len(names) != len(set(names)) or len(names) > MAX_FILES + 1
                or sum(entry.file_size for entry in entries) > LIMIT + 16 * 1024 * 1024):
            raise ValueError('invalid_archive')
        for entry in entries:
            _name(entry.filename)
            mode = entry.external_attr >> 16
            if entry.is_dir() or stat.S_IFMT(mode) not in {0, stat.S_IFREG}:
                raise ValueError('unsafe_archive_entry')
        manifest = json.loads(archive.read('manifest.json'))
        if (manifest['format'] != 'gtd-private-recovery' or manifest['version'] != 1
                or manifest['reconciliation_required'] is not True):
            raise ValueError('invalid_manifest')
        _receipt(manifest['quiescence'])
        if set(names) != set(manifest['files']) | {'manifest.json'}:
            raise ValueError('manifest_mismatch')
        directories = manifest['directories']
        if not isinstance(directories, list) or len(set(directories)) != len(directories):
            raise ValueError('invalid_directories')
        if len(directories) + len(names) > MAX_FILES + 1:
            raise ValueError('bundle_too_large')
        for name in [*manifest['files'], *directories]:
            _name(name)
            if name != 'service-export.zip' and not name.startswith('inputs/'):
                raise ValueError('unexpected_member')
        if 'service-export.zip' not in manifest['files'] or set(directories) & set(manifest['files']):
            raise ValueError('invalid_layout')
        files = {}
        for name, expected in manifest['files'].items():
            content = archive.read(name)
            if len(content) != expected['size'] or _sha(content) != expected['sha256']:
                raise ValueError('checksum_mismatch')
            files[name] = content
        for name in [*files, *directories]:
            if any(str(parent) in files for parent in PurePosixPath(name).parents):
                raise ValueError('file_directory_collision')
    _validate_export(files['service-export.zip'], destination.parent)
    destination.mkdir(mode=0o700)  # exclusive: existing empty directories rejected too
    def private_parents(path):
        if path == destination:
            return
        private_parents(path.parent)
        path.mkdir(mode=0o700, exist_ok=True)
    for name in sorted(directories, key=lambda value: (value.count('/'), value)):
        private_parents(destination / name)
    for name, content in files.items():
        target = destination / name
        private_parents(target.parent)
        _write(target, content)
    recovery = {'reconciliation_required': True, 'services_started': False,
                'effects_replayed': False, 'bundle_sha256': _sha(data)}
    _write(destination / 'manifest.json', _json(manifest))
    _write(destination / 'recovery-receipt.json', _json(recovery))
    _sync(destination)
    return recovery


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    packing = commands.add_parser('create')
    packing.add_argument('--spec', required=True, help='Private JSON: service_export, inputs, destination, quiescence_receipt')
    unpacking = commands.add_parser('restore')
    unpacking.add_argument('--bundle', required=True)
    unpacking.add_argument('--destination', required=True)
    args = parser.parse_args()
    try:
        if args.command == 'create':
            result = create(**json.loads(_read(_path(args.spec), 1024 * 1024)))
        else:
            result = restore(args.bundle, args.destination)
        print(json.dumps(result, sort_keys=True))
    except Exception:
        print('{"error":"recovery_bundle_rejected"}')
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
