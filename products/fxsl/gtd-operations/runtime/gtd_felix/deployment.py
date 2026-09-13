"""Offline release preparation. No service activation or independent live DB writer.

prepare_environment installs verified local wheels into a NEW private venv only.

A release is a content-addressed private source bundle, not a frozen interpreter.
Selection affects only future launches. Configuration and state remain external.
"""
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import stat
import subprocess
import tempfile
import zipfile


def _json(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()


def _sha(data):
    return hashlib.sha256(data).hexdigest()


def _path(value):
    path = Path(value)
    if not path.is_absolute() or '..' in path.parts:
        raise ValueError('absolute_path_required')
    if any(p.is_symlink() for p in (path, *path.parents)):
        raise ValueError('symlink_path')
    return path


def _private(path, create=False):
    path = _path(path)
    if not path.exists():
        if not create:
            raise ValueError('directory_missing')
        path.mkdir(mode=0o700)
    info = path.stat()
    if not stat.S_ISDIR(info.st_mode) or info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) != 0o700:
        raise ValueError('private_directory_required')
    return path


def _read(path, limit=8 * 1024 * 1024):
    path = _path(path)
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(fd, 'rb') as stream:
        info = os.fstat(stream.fileno())
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1 or info.st_size > limit:
            raise ValueError('unsafe_file')
        data = stream.read(limit + 1)
        after = os.fstat(stream.fileno())
    if len(data) > limit or (info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns, info.st_ctime_ns) != (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns, after.st_ctime_ns):
        raise ValueError('file_changed')
    return data


def _write(path, data):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, 'wb') as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())


def _sync(path):
    fd = os.open(path, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def _allowed(name):
    p = PurePosixPath(name)
    return (str(p) == name and not p.is_absolute() and '..' not in p.parts and
        (name in {'SKILL.md', 'references/operations.md', 'runtime/pyproject.toml'} or
         len(p.parts) == 3 and p.parts[:2] == ('runtime', 'gtd_felix') and p.suffix == '.py'))


def inspect_environment(python):
    """Observe a trusted local interpreter; never load credentials or install packages.

    Later deployment must create a dedicated venv from a reviewed offline wheelhouse
    with pinned transitive versions and wheel hashes (--no-index --require-hashes).
    This receipt detects ordinary drift, but does not freeze mutable site-packages.
    """
    executable = Path(python)
    _path(executable.parent)
    if not executable.is_absolute():
        raise ValueError('absolute_path_required')
    if not os.access(executable, os.X_OK):
        raise ValueError('python_not_executable')
    code = ('import sys,json,importlib.metadata as m;'
            'print(json.dumps({"version":list(sys.version_info[:3]),'
            '"dependencies":sorted((d.metadata["Name"],d.version) for d in m.distributions())}))')
    result = subprocess.run([str(executable), '-I', '-B', '-c', code], capture_output=True, timeout=20)
    if result.returncode or len(result.stdout) > 1024 * 1024:
        raise ValueError('environment_probe_failed')
    value = json.loads(result.stdout)
    if value['version'] < [3, 12, 0] or ['aiohttp', '3.14.3'] not in value['dependencies']:
        raise ValueError('runtime_dependencies_unmet')
    return {**value, 'python': str(executable), 'python_sha256': _sha(_read(executable.resolve(), 64 * 1024 * 1024)),
            'isolation': 'mutable_external', 'limits': 'Versions and executable hash do not freeze dependency bytes.'}


def _environment_files(root):
    files = {}
    for directory, dirs, names in os.walk(root, followlinks=False):
        for name in dirs + names:
            path = Path(directory) / name
            relative = path.relative_to(root).as_posix()
            if path.is_symlink():
                if not path.resolve().is_relative_to(root):
                    raise ValueError('environment_symlink_escape')
                files[relative] = {'symlink': os.readlink(path)}
            elif path.is_file():
                files[relative] = {'sha256': _sha(_read(path, 64 * 1024 * 1024))}
    return files


def _stdlib_identity(directory):
    root = _path(directory)
    files = {}
    for folder, dirs, names in os.walk(root, followlinks=False):
        dirs[:] = [n for n in dirs if n not in {'site-packages', 'dist-packages', '__pycache__'}]
        for name in names:
            if name.endswith(('.py', '.so')):
                path = Path(folder) / name
                files[path.relative_to(root).as_posix()] = {'resolved': str(path.resolve()),
                    'sha256': _sha(_read(path.resolve(), 64 * 1024 * 1024))}
    return {'root': str(root), 'sha256': _sha(_json(files)), 'files': len(files)}


def prepare_environment(python, destination, wheelhouse, lock_manifest):
    """Install exact reviewed wheels offline into a NEW private venv, never in place.

    lock_manifest = {wheel_filename: {name, version, sha256}} includes every
    transitive runtime dependency. Host Python/stdlib are referenced, not frozen.
    Failure leaves the new directory unselectable for inspection; never upgrades it.
    """
    import re
    dest, wheels = _path(destination), _path(wheelhouse)
    _private(dest.parent)
    if dest.exists() or not lock_manifest:
        raise ValueError('new_environment_required')
    host = Path(python)
    _path(host.parent)
    host_binary = host.resolve(strict=True)
    version = subprocess.run([str(host), '-I', '-B', '-c',
        'import sys,json,sysconfig; print(json.dumps({"version":list(sys.version_info[:3]),"stdlib":sysconfig.get_path("stdlib")}))'], capture_output=True, timeout=20)
    if version.returncode or json.loads(version.stdout)['version'] < [3, 12, 0]:
        raise ValueError('python_version_unsupported')
    host_stdlib = _stdlib_identity(json.loads(version.stdout)['stdlib'])
    verified = {}
    names = set()
    for filename, entry in lock_manifest.items():
        if (set(entry) != {'name', 'version', 'sha256'} or Path(filename).name != filename or not filename.endswith('.whl')
                or not re.fullmatch(r'[A-Za-z0-9_.+-]+', filename)
                or not re.fullmatch(r'[A-Za-z0-9_.-]+', entry['name'])
                or not re.fullmatch(r'[A-Za-z0-9_.+!-]+', entry['version'])):
            raise ValueError('invalid_wheel_lock')
        normalized = re.sub(r'[-_.]+', '-', entry['name']).lower()
        if normalized in names:
            raise ValueError('duplicate_distribution')
        names.add(normalized)
        data = _read(wheels / filename, 64 * 1024 * 1024)
        if _sha(data) != entry['sha256']:
            raise ValueError('wheel_hash_mismatch')
        verified[filename] = data
    if not any(v['name'].lower() == 'aiohttp' and v['version'] == '3.14.3' for v in lock_manifest.values()):
        raise ValueError('runtime_dependencies_unmet')
    dest.mkdir(mode=0o700)
    # Child inherits a restrictive umask without changing the caller process.
    clean_env = {k: v for k, v in os.environ.items() if k in {'PATH', 'LANG', 'LC_ALL', 'SYSTEMROOT'}}
    clean_env.update(PYTHONDONTWRITEBYTECODE='1', PIP_CONFIG_FILE=os.devnull,
                     PIP_NO_INDEX='1', PIP_DISABLE_PIP_VERSION_CHECK='1')
    def run(args):
        result = subprocess.run(args, env=clean_env, capture_output=True, timeout=120, umask=0o077)
        if result.returncode:
            raise ValueError('offline_environment_preparation_failed')
    run([str(host), '-I', '-B', '-m', 'venv', '--copies', str(dest)])
    locked_wheels = _private(dest / 'wheelhouse', create=True)
    for filename, data in verified.items():
        _write(locked_wheels / filename, data)
    requirements = '\n'.join(v['name'] + '==' + v['version'] + ' --hash=sha256:' + v['sha256']
                             for v in lock_manifest.values()) + '\n'
    _write(dest / 'requirements.lock', requirements.encode())
    run([str(dest / 'bin/python'), '-I', '-B', '-m', 'pip', 'install', '--no-index',
         '--require-hashes', '--only-binary=:all:', '--no-compile', '--find-links', str(locked_wheels),
         '-r', str(dest / 'requirements.lock')])
    run([str(dest / 'bin/python'), '-I', '-B', '-m', 'pip', 'check'])
    observed = inspect_environment(dest / 'bin/python')
    actual = {re.sub(r'[-_.]+', '-', n).lower(): v for n, v in observed['dependencies']}
    expected = {re.sub(r'[-_.]+', '-', v['name']).lower(): v['version'] for v in lock_manifest.values()}
    if any(actual.get(n) != v for n, v in expected.items()) or set(actual) - set(expected) - {'pip', 'setuptools'}:
        raise ValueError('installed_distribution_mismatch')
    return {'isolation': 'private_offline', 'python': str(dest / 'bin/python'), 'root': str(dest),
            'observed': observed, 'files': _environment_files(dest), 'lock': lock_manifest,
            'host_stdlib': host_stdlib, 'host_python': str(host_binary), 'host_python_sha256': _sha(_read(host_binary, 64 * 1024 * 1024)),
            'limits': 'Host Python standard library, OS and shared libraries remain external.'}


def verify_environment(environment):
    if environment.get('isolation') == 'private_offline':
        root = _private(environment['root'])
        if environment['python'] != str(root / 'bin/python'):
            raise ValueError('environment_path_mismatch')
        if (_stdlib_identity(environment['host_stdlib']['root']) != environment['host_stdlib']
                or _environment_files(root) != environment['files']
                or _sha(_read(_path(environment['host_python']), 64 * 1024 * 1024)) != environment['host_python_sha256']
                or inspect_environment(environment['python']) != environment['observed']):
            raise ValueError('environment_changed')
    elif inspect_environment(environment['python']) != environment:
        raise ValueError('environment_changed')
    return environment


def prepare_release(source_root, releases_dir, reviewed_files, environment):
    """Copy only explicitly reviewed source hashes. No configs, sessions or state.

    source_root is a complete realized skill with SKILL.md (not a KORA candidate
    containing content.md); runtime/ and instruction paths retain their installed
    relationship. Realization remains the responsibility of KORA. Caller supplies the independently reviewed map.
    """
    source, releases = _path(source_root), _private(releases_dir, create=True)
    if not reviewed_files or not all(_allowed(n) for n in reviewed_files):
        raise ValueError('unapproved_source_path')
    required = {'SKILL.md', 'references/operations.md', 'runtime/pyproject.toml',
                'runtime/gtd_felix/__init__.py', 'runtime/gtd_felix/__main__.py', 'runtime/gtd_felix/deployment.py'}
    if not required.issubset(reviewed_files):
        raise ValueError('incomplete_release')
    modules = {p.relative_to(source).as_posix() for p in (source / 'runtime/gtd_felix').glob('*.py')}
    if modules != {n for n in reviewed_files if n.startswith('runtime/gtd_felix/')} :
        raise ValueError('unreviewed_runtime_module')
    verify_environment(environment)
    manifest = {'format': 'gtd-release-v1', 'files': dict(sorted(reviewed_files.items())), 'environment': environment}
    identity = _sha(_json(manifest))
    stage = Path(tempfile.mkdtemp(prefix='.stage-', dir=releases))
    try:
        signatures = {}
        for name, expected in manifest['files'].items():
            path = _path(source / name)
            signatures[name] = path.stat()
            data = _read(path)
            if _sha(data) != expected:
                raise ValueError('source_hash_mismatch')
            target = stage / name
            for parent in reversed(target.parent.parents):
                if parent.is_relative_to(stage):
                    _private(parent, create=True)
            _private(target.parent, create=True)
            _write(target, data)
        for name, info in signatures.items():
            current = _path(source / name).stat()
            if (info.st_ino, info.st_dev, info.st_mtime_ns, info.st_ctime_ns, info.st_size) != (current.st_ino, current.st_dev, current.st_mtime_ns, current.st_ctime_ns, current.st_size) or _sha(_read(source / name)) != reviewed_files[name]:
                raise ValueError('source_changed_during_copy')
        if modules != {p.relative_to(source).as_posix() for p in (source / 'runtime/gtd_felix').glob('*.py')}:
            raise ValueError('source_changed_during_copy')
        _write(stage / 'manifest.json', _json(manifest))
        verify_release(stage, identity, check_environment=True)
        for directory, _, _ in os.walk(stage, topdown=False):
            _sync(directory)
        destination = releases / identity
        if destination.exists():
            verify_release(destination, identity, check_environment=True)
        else:
            os.rename(stage, destination)
            _sync(releases)
        return {'release_id': identity, 'path': str(destination), 'environment': environment,
                'status': 'prepared' if environment.get('isolation') == 'private_offline' else 'prepared_source_only'}
    finally:
        if stage.exists():
            shutil.rmtree(stage)


def verify_release(release_dir, expected_id, check_environment=True):
    root = _private(release_dir)
    manifest = json.loads(_read(root / 'manifest.json'))
    if manifest.get('format') != 'gtd-release-v1' or _sha(_json(manifest)) != expected_id:
        raise ValueError('release_manifest_mismatch')
    expected = set(manifest['files']) | {'manifest.json'}
    observed = set()
    for directory, dirs, files in os.walk(root, followlinks=False):
        _private(Path(directory))
        for name in dirs:
            _private(Path(directory) / name)
        for name in files:
            path = Path(directory) / name
            relative = path.relative_to(root).as_posix()
            if relative not in expected or (relative != 'manifest.json' and not _allowed(relative)):
                raise ValueError('unexpected_release_file')
            if stat.S_IMODE(path.lstat().st_mode) != 0o600:
                raise ValueError('private_file_required')
            data = _read(path)
            if relative != 'manifest.json' and _sha(data) != manifest['files'][relative]:
                raise ValueError('release_file_mismatch')
            observed.add(relative)
    if observed != expected:
        raise ValueError('release_files_missing')
    if check_environment:
        verify_environment(manifest['environment'])
    return manifest


def select_release(releases_dir, release_id, selection_file):
    """Atomic reference for subsequent launches; no process is signalled/restarted."""
    if len(release_id) != 64 or any(c not in '0123456789abcdef' for c in release_id):
        raise ValueError('invalid_release_id')
    releases = _private(releases_dir)
    manifest = verify_release(releases / release_id, release_id)
    if manifest['environment'].get('isolation') != 'private_offline':
        raise ValueError('environment_not_operational')
    selected = _path(selection_file)
    _private(selected.parent)
    if selected.exists():
        _read(selected)
    fd, temporary = tempfile.mkstemp(prefix='.selection-', dir=selected.parent)
    os.close(fd)
    try:
        with open(temporary, 'wb') as stream:
            stream.write(_json({'release_id': release_id}))
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, selected)
        _sync(selected.parent)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    return resolve_selection(releases, selected)


def resolve_selection(releases_dir, selection_file):
    value = json.loads(_read(selection_file))
    identity = value['release_id']
    if len(identity) != 64 or any(c not in '0123456789abcdef' for c in identity):
        raise ValueError('invalid_release_id')
    path = _private(releases_dir) / identity
    manifest = verify_release(path, identity)
    if manifest['environment'].get('isolation') != 'private_offline':
        raise ValueError('environment_not_operational')
    return path


def render_user_unit(release_dir, python, config):
    """Return text only. Concrete version stays pinned until explicit unit replacement/restart."""
    root, executable, configuration = map(_path, (release_dir, python, config))
    manifest = verify_release(root, root.name)
    if manifest['environment'].get('isolation') != 'private_offline':
        raise ValueError('environment_not_operational')
    if str(executable) != manifest['environment']['python'] or not os.access(executable, os.X_OK):
        raise ValueError('python_mismatch')
    if configuration.is_relative_to(root):
        raise ValueError('configuration_inside_release')
    def quote(path):
        value = str(path)
        if any(c in value for c in '\n\r\x00'):
            raise ValueError('invalid_unit_path')
        return '"' + value.replace('\\', '\\\\').replace('"', '\\"').replace('%', '%%').replace('$', '$$') + '"'
    working_directory = str(root / 'runtime').replace('\\', '\\x5c').replace(' ', '\\x20').replace('%', '%%')
    quote(root)  # Reject control characters for both directives.
    return ('[Unit]\nDescription=GTD Felix pinned release\n[Service]\nType=simple\nUMask=0077\n'
            'WorkingDirectory=' + working_directory + '\nExecStart=' + quote(executable) +
            ' -E -s -B -m gtd_felix.deployment --release ' + quote(root) + ' --config ' + quote(configuration) +
            '\nEnvironment=PYTHONDONTWRITEBYTECODE=1\nStandardOutput=null\nStandardError=null\n'
            'Restart=on-failure\n[Install]\nWantedBy=default.target\n')


def rehearsal_restore(service, export_path, isolated_dir):
    """Use the existing export and restore; no second writer opens the live DB.

    Export contains private state and belongs outside release bundles. Restored
    service remains in recovery and is closed without enabling any adapters.
    """
    archive, target = _path(export_path), _path(isolated_dir)
    if target.exists():
        raise ValueError('restore_destination_exists')
    receipt = service.export(archive)
    with zipfile.ZipFile(archive) as zipped:
        state = json.loads(zipped.read('state.json'))
    restored = type(service).restore(archive, target)
    try:
        if sorted(restored.query(), key=lambda i: i['id']) != sorted(state['items'], key=lambda i: i['id']):
            raise ValueError('restored_items_mismatch')
        for key, value in state['metadata'].items():
            if key != 'recovery_required' and restored._meta(key) != value:
                raise ValueError('restored_metadata_mismatch')
        if not restored.recovery_required:
            raise ValueError('recovery_guard_missing')
        # Re-export verifies all referenced original bytes through the service.
        roundtrip = target / 'rehearsal-roundtrip.zip'
        restored.export(roundtrip)
        with zipfile.ZipFile(archive) as before, zipfile.ZipFile(roundtrip) as after:
            names = [n for n in before.namelist() if n.startswith('originals/')]
            if set(names) != {n for n in after.namelist() if n.startswith('originals/')} or any(before.read(n) != after.read(n) for n in names):
                raise ValueError('restored_originals_mismatch')
        return {'status': 'verified', 'export': receipt, 'items': len(state['items']),
                'originals': len(names), 'recovery_required': True, 'effects_enabled': False}
    finally:
        restored.close()


def launch_release(release_dir, config):
    """Verify immediately before replacing this process; callers explicitly opt in."""
    root, configuration = _path(release_dir), _path(config)
    manifest = verify_release(root, root.name)
    if manifest['environment'].get('isolation') != 'private_offline':
        raise ValueError('environment_not_operational')
    if configuration.is_relative_to(root):
        raise ValueError('configuration_inside_release')
    python = manifest['environment']['python']
    os.chdir(root / 'runtime')
    os.execv(python, [python, '-E', '-s', '-B', '-m', 'gtd_felix', 'serve', '--config', str(configuration)])


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Verify a pinned release before explicit launch')
    parser.add_argument('--release', required=True)
    parser.add_argument('--config', required=True)
    args = parser.parse_args()
    launch_release(args.release, args.config)
