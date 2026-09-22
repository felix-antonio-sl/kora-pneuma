#!/usr/bin/env python3
"""Koraficación: versiones exactas, cotejo declarado y reparación recuperable.

No extrae PDF, llama modelos, juzga significado ni publica conocimiento.
Los originales y revisiones se conservan fuera del cuerpo de conocimiento.
integral.py mantiene exclusivamente la compatibilidad con trabajos integral-3.
"""

import argparse
from contextlib import contextmanager
import copy
import difflib
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile


PROTOCOL = 'integral-4'
UNCHECKED = object()


class Conflict(Exception):
    pass


def require(condition, message):
    if not condition:
        raise Conflict(message)


def digest(raw):
    return hashlib.sha256(raw if isinstance(raw, bytes) else raw.encode('utf-8')).hexdigest()


def encoded(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')


def read_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, 'Clave JSON duplicada: ' + key)
            result[key] = value
        return result
    return json.loads(Path(path).read_text(encoding='utf-8'), object_pairs_hook=unique)


def plain_path(path):
    path = Path(path).expanduser().absolute()
    require(not any(p.is_symlink() for p in (path, *path.parents)),
            'SYMLINK: destino o antecesor enlazado: ' + str(path))
    # Check links before collapsing '..', then compare/write a canonical path.
    return Path(os.path.abspath(path))


def file_hash(path):
    path = plain_path(path)
    return digest(path.read_bytes()) if path.exists() else None


def atomic_write(path, raw, expected_sha=UNCHECKED):
    path = plain_path(path)
    require(path.parent.is_dir(), 'Falta directorio de destino: ' + str(path.parent))
    fd, tmp = tempfile.mkstemp(prefix='.workflow-', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        if expected_sha is not UNCHECKED:
            require(file_hash(path) == expected_sha,
                    'BODY_CHANGED: edición detectada antes del reemplazo; recuperación pendiente.')
        os.replace(tmp, path)
        parent = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(parent)
        finally:
            os.close(parent)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


@contextmanager
def locked(work, create=False):
    plain_path(work)
    if create:
        work.mkdir(mode=0o700, parents=True, exist_ok=True)
    require(work.is_dir(), 'Trabajo inexistente; usa init.')
    require(work.stat().st_mode & 0o077 == 0, 'WORK_PERMISSIONS: el trabajo debe ser privado (0700).')
    fd = os.open(work / '.lock', os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
    try:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise Conflict('WORK_LOCKED: otra operación usa el trabajo.') from exc
        yield
    finally:
        os.close(fd)


def object_path(work, sha):
    require(isinstance(sha, str) and re.fullmatch('[0-9a-f]{64}', sha), 'Hash de objeto inválido.')
    return plain_path(work / 'objects' / sha)


def put_object(work, raw):
    sha = digest(raw)
    path = object_path(work, sha)
    if path.exists():
        require(path.read_bytes() == raw, 'SNAPSHOT_CHANGED: ' + sha)
    else:
        atomic_write(path, raw)
    return sha


def object_bytes(work, sha):
    raw = object_path(work, sha).read_bytes()
    require(digest(raw) == sha, 'SNAPSHOT_CHANGED: ' + sha)
    return raw


def save(work, state):
    envelope = {'data': state, 'sha256': digest(encoded(state))}
    atomic_write(work / 'state.json', encoded(envelope) + b'\n')


def load(work):
    envelope = read_json(plain_path(work / 'state.json'))
    state = envelope['data']
    require(digest(encoded(state)) == envelope['sha256'], 'STATE_CHANGED: registro alterado.')
    require(state['protocol'] == PROTOCOL, 'PROTOCOL_CHANGED: no se migra evidencia automáticamente.')
    hashes = {source['sha256'] for source in state['sources']}
    if state.get('initial_sha256'):
        hashes.add(state['initial_sha256'])
    for version in state['versions']:
        hashes.add(version['body_sha256'])
        hashes.update(item['sha256'] for item in version['resources'])
    for sha in hashes:
        object_bytes(work, sha)
    return state


def current(state):
    return state['versions'][-1] if state['versions'] else None


def verify_body(state):
    require(not state.get('pending'), 'RECOVERY_REQUIRED: usa recover antes de continuar.')
    require(file_hash(state['body']) == state['installed_sha256'],
            'BODY_CHANGED: edición ajena; conserva y reconcilia antes de continuar.')


def verify_resources(version):
    if version:
        for item in version['resources']:
            require(file_hash(item['origin']) == item['sha256'],
                    'RESOURCE_CHANGED: registra una candidata con los recursos vigentes.')


def initialize(args, work):
    require(args.source and args.body and args.scope and args.scope.strip(),
            'init requiere --source, --body y --scope.')
    body = plain_path(args.body)
    require(body.parent.is_dir(), 'El directorio del borrador debe existir.')
    require(not body.is_relative_to(work), 'El borrador debe quedar fuera del estado de trabajo.')
    sources = []
    raws = []
    for origin in args.source:
        origin = Path(origin).expanduser().resolve(strict=True)
        raw = origin.read_bytes()
        raws.append(raw)
        sources.append({'origin': str(origin), 'sha256': digest(raw)})
    require(str(body) not in {source['origin'] for source in sources},
            'El borrador no puede sobrescribir una fuente original.')
    resources = [str(plain_path(p)) for p in (args.resource or [])]
    require(len(set(resources)) == len(resources), 'Recurso duplicado.')
    require(str(body) not in resources, 'El cuerpo no puede ser su propio recurso.')
    config = {'body': str(body), 'scope': args.scope.strip(), 'sources': sources,
              'resource_paths': resources, 'require_independent': args.require_independent,
              'independent_repairs': args.independent_repairs}
    if (work / 'state.json').exists():
        state = load(work)
        require(all(state[key] == value for key, value in config.items()),
                'CONFIG_CHANGED: usa otro trabajo; conserva la evidencia anterior.')
        verify_body(state)
        return {**status(state, work), 'reused': True}
    objects = plain_path(work / 'objects')
    objects.mkdir(mode=0o700, exist_ok=True)
    require(objects.stat().st_mode & 0o077 == 0, 'OBJECT_PERMISSIONS: se requiere carpeta privada.')
    for raw in raws:
        put_object(work, raw)
    initial = put_object(work, body.read_bytes()) if body.exists() else None
    state = {**config, 'protocol': PROTOCOL, 'engine_sha256': digest(Path(__file__).read_bytes()),
             'installed_sha256': initial, 'initial_sha256': initial, 'versions': [], 'pending': None}
    save(work, state)
    return status(state, work)


def target(state, path):
    raw = Path(path).read_bytes()
    raw.decode('utf-8')
    resources, payloads = [], [raw]
    for origin in state['resource_paths']:
        data = plain_path(origin).read_bytes()
        resources.append({'origin': origin, 'sha256': digest(data)})
        payloads.append(data)
    previous = current(state)
    if previous and previous['body_sha256'] == digest(raw) and previous['resources'] == resources:
        return copy.deepcopy(previous), payloads
    version = {'body_sha256': digest(raw), 'resources': resources,
               'parent': previous['revision'] if previous else None, 'reviews': []}
    version['revision'] = digest(encoded({
        'sources': state['sources'], 'scope': state['scope'],
        'body_sha256': version['body_sha256'], 'resources': resources, 'parent': version['parent']}))
    return version, payloads


def find_review(state, identifier):
    for version in state['versions']:
        for review in version['reviews']:
            if review['review_id'] == identifier:
                return version, review
    raise Conflict('REVIEW_MISSING: evidencia base no encontrada.')


def validate_review(state, version, data):
    require(isinstance(data, dict), 'La revisión debe ser un objeto JSON.')
    require(data.get('revision') == version['revision'], 'REVISION_CHANGED: coteja el objetivo exacto.')
    for field in ('reviewer', 'evidence'):
        require(isinstance(data.get(field), str) and data[field].strip(), 'Falta ' + field)
    require(data.get('isolation') in ('author_context', 'separate_context', 'unknown'),
            'Declara aislamiento real: author_context, separate_context o unknown.')
    require(type(data.get('authored_target')) is bool, 'Declara authored_target booleano.')
    require(data.get('scope') in ('full', 'changes'), 'scope debe ser full o changes.')
    require(data.get('coverage') in ('complete', 'incomplete'), 'Declara cobertura de fuente.')
    require(data.get('result') in ('accepted', 'repair', 'limited'), 'Resultado inválido.')
    for field in ('issues', 'limits'):
        require(isinstance(data.get(field), list)
                and all(isinstance(v, str) and v.strip() for v in data[field]),
                field + ' debe ser una lista de textos.')
    if data['result'] == 'accepted':
        require(not data['issues'] and data['coverage'] == 'complete',
                'OPEN_ISSUES: no se acepta pérdida conocida o cobertura incompleta.')
        prior = version['reviews'][-1] if version['reviews'] else None
        if prior and prior['result'] != 'accepted':
            require(data.get('supersedes') == prior['review_id']
                    and isinstance(data.get('resolution'), str) and data['resolution'].strip(),
                    'OPEN_REVIEW: resuelve explícitamente el último dictamen con supersedes y resolution.')
    if data['result'] == 'repair':
        require(data['issues'], 'repair requiere hallazgos concretos.')
    if data['result'] == 'limited':
        require(data['limits'] or data['issues'] or data['coverage'] == 'incomplete',
                'limited requiere límite concreto.')
    if data['scope'] == 'changes':
        base_version, base_review = find_review(state, data.get('basis'))
        require(base_version['revision'] == version['parent']
                and base_review == base_version['reviews'][-1]
                and base_review['coverage'] == 'complete',
                'BASIS_CHANGED: changes requiere el último cotejo completo de la versión padre.')
        require(isinstance(data.get('impact'), str) and data['impact'].strip(),
                'changes requiere impact: relaciones afectadas, cierre de hallazgos y alcance cotejado.')
    else:
        require(not data.get('basis'), 'Una revisión full no hereda un cotejo parcial.')
    review = copy.deepcopy(data)
    # These fields describe evidence, never a signature or proof of comprehension.
    review['engine_sha256'] = digest(Path(__file__).read_bytes())
    review.pop('review_id', None)
    review['review_id'] = digest(encoded(review))
    return review


def independent(state, review):
    if review['isolation'] != 'separate_context':
        return False
    if not review['authored_target']:
        return True
    if state['independent_repairs'] or review['scope'] != 'changes':
        return False
    _, prior = find_review(state, review['basis'])
    return independent(state, prior)


def status(state, work):
    version = current(state)
    review = version['reviews'][-1] if version and version['reviews'] else None
    result = 'empty' if not version else 'unreviewed'
    separate = independent(state, review) if review else False
    if review:
        result = {'accepted': 'reviewed', 'repair': 'repair', 'limited': 'limited'}[review['result']]
        if result == 'reviewed' and (state['require_independent'] or state['independent_repairs']) and not separate:
            result = 'limited'
    return {'protocol': PROTOCOL, 'state': result, 'scope': state['scope'],
            'current_revision': version['revision'] if version else None,
            'body': state['body'], 'body_sha256': state['installed_sha256'],
            'sources': [{**source, 'path': str(object_path(work, source['sha256']))}
                        for source in state['sources']],
            'review_id': review['review_id'] if review else None,
            'independent_review_declared': bool(review and review['isolation'] == 'separate_context'
                                                and not review['authored_target']),
            'review_chain_satisfies_policy': separate,
            'reviewer_authored_target': review['authored_target'] if review else None,
            'recovery_required': bool(state.get('pending'))}


def materialize(work, state):
    pending = state.get('pending')
    if not pending:
        verify_body(state)
        return
    require(file_hash(state['body']) in (pending['before'], pending['after']),
            'BODY_CHANGED: recuperación detenida por edición ajena; evidencia preservada.')
    if file_hash(state['body']) != pending['after']:
        atomic_write(Path(state['body']), object_bytes(work, pending['after']),
                     expected_sha=pending['before'])
    state['installed_sha256'] = pending['after']
    state['pending'] = None
    save(work, state)


def commit(work, state, version, payloads):
    verify_body(state)
    # Verify resource inputs again immediately before committing a decision.
    verify_resources(version)
    for source in state['sources']:
        object_bytes(work, source['sha256'])
    for raw in payloads:
        put_object(work, raw)
    state['versions'].append(version)
    state['pending'] = {'before': state['installed_sha256'], 'after': version['body_sha256']}
    save(work, state)
    materialize(work, state)


def check_base(state, expected):
    version = current(state)
    require(expected == (version['revision'] if version else None),
            'BASE_CHANGED: usa --base-revision con la versión vigente.')


def preview(state, work, path):
    verify_body(state)
    version, payloads = target(state, path)
    old = object_bytes(work, current(state)['body_sha256']).decode('utf-8') if current(state) else ''
    return {'revision': version['revision'], 'body_sha256': version['body_sha256'],
            'base_revision': current(state)['revision'] if current(state) else None,
            'resources': version['resources'],
            'diff': ''.join(difflib.unified_diff(old.splitlines(True), payloads[0].decode('utf-8').splitlines(True),
                                               fromfile='base', tofile='target')),
            'note': 'Propuesta sin aceptación. El revisor debe leer objetivo completo, fuentes y relaciones.'}


def execute(args, work):
    if args.command == 'init':
        return initialize(args, work)
    state = load(work)
    if args.command == 'recover':
        materialize(work, state)
        return status(state, work)
    verify_body(state)
    if args.command not in ('candidate', 'preview', 'repair'):
        verify_resources(current(state))
    if args.command == 'status':
        return status(state, work)
    if args.command == 'preview':
        require(args.file, 'preview requiere --file con el objetivo completo.')
        return preview(state, work, args.file)
    if args.command in ('candidate', 'repair'):
        require(args.file, 'Se requiere --file con la candidata completa UTF-8.')
        version, payloads = target(state, args.file)
        previous = current(state)
        if args.command == 'repair':
            require(args.review, 'repair requiere --review del objetivo exacto.')
            review = validate_review(state, version, read_json(args.review))
            require(review['result'] == 'accepted', 'repair atómica requiere objetivo ya aceptado.')
            if previous and previous['revision'] == version['revision']:
                require(previous['reviews'] and previous['reviews'][-1] == review
                        and args.base_revision in (version['parent'], version['revision']),
                        'REPLAY_CHANGED: no corresponde a la reparación vigente.')
                verify_resources(version)
                return {**status(state, work), 'reused': True}
            check_base(state, args.base_revision)
            version['reviews'].append(review)
        else:
            if previous and previous['revision'] == version['revision']:
                require(args.base_revision in (version['parent'], version['revision']), 'BASE_CHANGED')
                verify_resources(version)
                return {**status(state, work), 'reused': True}
            check_base(state, args.base_revision)
        commit(work, state, version, payloads)
        return status(state, work)
    version = current(state)
    if args.command == 'review':
        require(version and args.file, 'review requiere candidata y --file.')
        review = validate_review(state, version, read_json(args.file))
        if version['reviews'] and version['reviews'][-1] == review:
            return {**status(state, work), 'reused': True}
        require(not any(row['review_id'] == review['review_id'] for row in version['reviews']),
                'REVIEW_SUPERSEDED: no se reactiva una revisión antigua sobre un fallo posterior.')
        version['reviews'].append(review)
        verify_resources(version)
        verify_body(state)
        save(work, state)
        return status(state, work)
    if args.command == 'next':
        return {**status(state, work),
                'candidate_snapshot': str(object_path(work, version['body_sha256'])) if version else None,
                'resources': version['resources'] if version else [],
                'reviews': version['reviews'] if version else [],
                'next_action': 'candidate' if not version else ('export' if status(state, work)['state'] == 'reviewed' else 'review_or_repair')}
    require(args.command == 'export', 'Comando desconocido.')
    require(status(state, work)['state'] == 'reviewed',
            'REVIEW_REQUIRED: falta aceptación, cobertura o aislamiento requerido.')
    return {**status(state, work), 'candidate_snapshot': str(object_path(work, version['body_sha256'])),
            'initial_snapshot': str(object_path(work, state['initial_sha256'])) if state.get('initial_sha256') else None,
            'resources': version['resources'], 'review': version['reviews'][-1],
            'history': [{'revision': v['revision'], 'body_sha256': v['body_sha256'],
                         'snapshot': str(object_path(work, v['body_sha256'])),
                         'reviews': v['reviews']} for v in state['versions']],
            'publication': 'not_performed',
            'claim': 'Juicios declarados vinculados a bytes exactos; no prueba automática de fidelidad ni independencia.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['init', 'candidate', 'preview', 'review', 'repair',
                                            'status', 'next', 'recover', 'export'])
    parser.add_argument('--work', required=True)
    parser.add_argument('--source', action='append')
    parser.add_argument('--body')
    parser.add_argument('--scope')
    parser.add_argument('--resource', action='append')
    parser.add_argument('--require-independent', action='store_true')
    parser.add_argument('--independent-repairs', action='store_true')
    parser.add_argument('--file')
    parser.add_argument('--review')
    parser.add_argument('--base-revision')
    args = parser.parse_args()
    try:
        work = plain_path(args.work)
        with locked(work, args.command == 'init'):
            result = execute(args, work)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (Conflict, OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({'error': str(exc), 'publication': 'not_performed'}, ensure_ascii=False))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
