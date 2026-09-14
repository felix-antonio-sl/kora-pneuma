#!/usr/bin/env python3
"""Synthetic product acceptance. Preparing/evaluating never calls a model.

Live run talks only to the explicitly configured GTD HTTP service. Its existing
orchestrator owns inference, admission and native processes; this probe owns none.
Evaluation reads verified exported copies, never the live SQLite database.
"""
import argparse
import asyncio
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import sqlite3
import stat
import tempfile
import time
from urllib.parse import urlsplit
import uuid
import zipfile


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, allow_nan=False).encode()


def sha(data):
    return hashlib.sha256(data).hexdigest()


# User-facing situations only. No tool recipes, expected answers or evaluator
# predicates are included in these inputs. Preconditions represent owner state.
SCENARIOS = {
 'G1': {'inputs': [
    {'key': 'a', 'text': 'Llamar a la biblioteca para consultar su horario.'},
    {'key': 'b', 'text': 'Organizar el taller sintético: reservar sala y preparar la guía.'},
    {'key': 'c', 'text': 'Referencia: el código de prueba del catálogo es MAREA-27; conservarlo para consultar.'},
    {'key': 'd', 'text': 'Tal vez aprender encuadernación; volver a considerarlo el 2030-02-10, todavía no me comprometo.'},
    {'key': 'e', 'text': 'Descarto la idea de comprar el atril del ensayo; retírala de lo activo.'},
    {'key': 'f', 'text': 'Ana, filtro.'}], 'request': 'Aclara estas notas sintéticas y deja el registro útil para retomarlas.'},
 'G2': {'inputs': [{'key': 'project', 'text': 'Preparar taller sintético. Yo confirmaré la sala por teléfono; tú puedes preparar la guía. La impresión depende de la confirmación de sala.',
    'fields': {'kind': 'project', 'outcome': 'Taller preparado', 'completion_criteria': 'Sala confirmada y guía utilizable'}}],
    'mandate': 'project', 'request': 'Organiza y avanza el taller con los medios habilitados. La sala aún no está confirmada.',
    'intervention': {'trigger': 'human_action_available', 'key': 'project', 'action': 'done', 'fields': {}}},
 'G3': {'inputs': [
    {'key': 'phone', 'text': 'Consultar horario biblioteca', 'fields': {'kind': 'action', 'context': 'phone', 'duration_minutes': 10, 'capacity': 'low', 'executor': 'felix'}},
    {'key': 'desk', 'text': 'Ordenar archivo local en escritorio', 'fields': {'kind': 'action', 'context': 'desk', 'duration_minutes': 45, 'executor': 'felix'}},
    {'key': 'prep', 'text': 'Preparar una nota breve con preguntas para la biblioteca.'}],
    'request': 'Tengo quince minutos, teléfono y capacidad baja. Indica un solo siguiente movimiento con su título; puedes avanzar por separado la preparación privada pertinente.'},
 'G4': {'inputs': [
    {'key': 'silent', 'text': 'Proyecto silencioso del ensayo', 'fields': {'kind': 'project', 'outcome': 'Preparar encuentro', 'completion_criteria': 'Encuentro preparado'}},
    {'key': 'maybe', 'text': 'Quizá aprender encuadernación', 'fields': {'kind': 'possibility', 'review_at': '2030-02-10'}},
    {'key': 'area', 'text': 'Cuidar biblioteca de ensayo', 'fields': {'kind': 'responsibility', 'completion_criteria': 'Material localizable'}},
    {'key': 'decision', 'text': 'No he elegido entre horario diurno y nocturno.', 'fields': {'kind': 'capture', 'decision_needed': True, 'decision_question': '¿Diurno o nocturno?'}}],
    'request': 'Estoy retomando después de una pausa. Revisa el conjunto sintético, lo que quedó sin movimiento y los asuntos que necesitan mi criterio. No tengo cuentas externas conectadas a este ensayo.'},
 'G5': {'inputs': [{'key': 'project', 'text': 'Quiero preparar una lectura pública pequeña, sin comprar equipos. Prioridad: accesibilidad para personas con movilidad reducida.',
    'fields': {'kind': 'project', 'purpose': 'Compartir lectura accesible', 'outcome': 'Lectura preparada', 'completion_criteria': 'Lugar accesible y lectura preparada'}}],
    'mandate': 'project', 'request': 'Conduce este proyecto hasta un avance suficiente con lo conocido; si falta una decisión que cambie el resultado, hazla concreta.'},
 'G6': {'inputs': [
    {'key': 'appointment', 'text': 'Cita sintética confirmada el 2030-03-04 de 10:00 a 11:00 en Europe/Berlin.'},
    {'key': 'deadline', 'text': 'Entregar propuesta sintética a más tardar el 2030-03-06.'},
    {'key': 'reminder', 'text': 'Recuérdame volver a mirar la posibilidad el 2030-03-07; no es una fecha límite.'}],
    'request': 'Ordena lo nuevo y déjalo recuperable. Hoy puedo dedicarme a aclarar estas entradas.'},
 'G7': {'inputs': [{'key': 'project', 'text': 'Preparar guía de uso de una biblioteca ficticia. El horario de la fuente de trabajo es 09:00 a 12:00, pendiente de confirmación de Lara. Usa el único ejecutor de ensayo incorporado para el material; Lara aún no ha respondido.',
    'fields': {'kind': 'project', 'outcome': 'Guía preparada', 'completion_criteria': 'Guía comprobada y horario confirmado'}}],
    'mandate': 'project', 'request': 'Avanza la preparación y conserva lo pendiente de Lara.',
    'intervention': {'trigger': 'native_running', 'key': 'project', 'fields': {'text': 'Preparar guía de uso de una biblioteca ficticia. La fuente de trabajo corregida indica 10:00 a 13:00; Lara aún no confirma. Usa el único ejecutor de ensayo incorporado para preparar el material, sin afirmar confirmación humana.'}}},
 'G8': {'inputs': [{'key': 'capture', 'text': 'Entrada sintética que debo recuperar tras reinicio.'},
    {'key': 'suggestion', 'text': 'Sugerencia de un tercero: quizá comprar otro atril.', 'source': {'third_party': True}}],
    'request': 'Organiza las entradas del ensayo, prepara una nota privada útil para retomarlas y revisa lo que permanece pendiente. Un borrador o una sugerencia no adopta compromisos por sí solo.',
    'return_request': 'Estoy de vuelta. Recupera lo que quedó preparado y revisado, e indica qué permanece pendiente sin adoptar la sugerencia.',
    'requires': ['owned_service_restart']},
 'G9': {'inputs': [{'key': 'project', 'text': 'Deja listo el cierre privado del préstamo de libros del ensayo. Necesito una nota JSON editable con dias (lunes y martes), total comprobado y explicacion breve, y una lista JSON separada de devoluciones pendientes, cada una con persona y libro. El registro de préstamos dice lunes 7 y martes 11; el registro de devoluciones señala que Ana debe devolver Atlas y Luis debe devolver Jardín. Conserva cualquier dato dudoso como pendiente de comprobar. No contactes a nadie ni adoptes la sugerencia de comprar un sistema nuevo.', 'fields': {'kind': 'project', 'outcome': 'Cierre privado de préstamos listo', 'completion_criteria': 'Nota editable de los días de la fuente vigente y total comprobado, más lista separada y comprobada de devoluciones pendientes con persona y libro; ambos entregables listos sin contactar ni comprar.'}}], 'mandate': 'project', 'request': 'Resuelve el cierre privado y comprueba el conjunto; continúa sin pedirme instrucciones por paso.', 'intervention': {'trigger': 'material_created', 'key': 'project', 'fields': {'text': 'Deja listo el cierre privado del préstamo de libros del ensayo. Necesito una nota JSON editable con dias (lunes y martes), total comprobado y explicacion breve, y una lista JSON separada de devoluciones pendientes, cada una con persona y libro. El registro de préstamos corregido dice lunes 7 y martes 13; el registro de devoluciones señala que Ana debe devolver Atlas y Luis debe devolver Jardín. Conserva cualquier dato dudoso como pendiente de comprobar. No contactes a nadie ni adoptes la sugerencia de comprar un sistema nuevo.'}}},
 'G10': {'inputs': [{'key': 'source', 'text': 'Fuente sintética: la biblioteca atiende de 09:00 a 12:00.'},
    {'key': 'independent', 'text': 'Preparar una lista de materiales para el taller, independiente del horario.'},
    {'key': 'decision', 'text': 'Todavía no decido si asistiré al taller.', 'fields': {'kind': 'capture', 'decision_needed': True, 'decision_question': '¿Asistiré al taller?'}}],
    'request': 'Prepara una nota del horario y avanza lo independiente. Mi asistencia sigue sin decidir.',
    'intervention': {'trigger': 'material_created', 'key': 'source', 'fields': {'text': 'Fuente corregida por el dueño: atención 10:00 a 13:00.', 'source': {'acceptance_revision': 2}}}},
}


def private_json(path):
    path = Path(path).absolute()
    if any(p.is_symlink() for p in (path, *path.parents)):
        raise ValueError('unsafe_config')
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
    with os.fdopen(fd) as stream:
        info = os.fstat(stream.fileno())
        if info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) != 0o600 or not stat.S_ISREG(info.st_mode):
            raise ValueError('unsafe_config')
        return json.load(stream)


def write_new(path, data):
    fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, 'wb') as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())


def load_snapshot(path, expected_sha):
    """Verify manifest and parse exported DB only; never opens the live store."""
    data = Path(path).read_bytes()
    if sha(data) != expected_sha:
        raise ValueError('snapshot_digest_mismatch')
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        if len(archive.namelist()) != len(set(archive.namelist())) or sum(i.file_size for i in archive.infolist()) > 64 * 1024 * 1024:
            raise ValueError('invalid_snapshot_archive')
        manifest = json.loads(archive.read('manifest.json'))
        if manifest.get('format') != 'gtd-felix-snapshot' or manifest.get('format_version') != 1:
            raise ValueError('unsupported_snapshot')
        files = {}
        for name, expected in manifest['files'].items():
            content = archive.read(name)
            if len(content) != expected['size'] or sha(content) != expected['sha256']:
                raise ValueError('snapshot_member_corrupt')
            files[name] = content
    with tempfile.TemporaryDirectory(prefix='gtd-evaluator-') as temp:
        database = Path(temp) / 'snapshot.sqlite3'
        write_new(database, files['gtd.sqlite3'])
        db = sqlite3.connect(database.as_uri() + '?mode=ro&immutable=1', uri=True)
        try:
            items = {row[0]: json.loads(row[1]) for row in db.execute('SELECT id,document FROM items')}
            operations = [dict(zip(('operation_id', 'actor', 'receipt'), (r[0], r[1], json.loads(r[2]))))
                for r in db.execute('SELECT operation_id,actor,receipt FROM operations')]
            metadata = {r[0]: json.loads(r[1]) for r in db.execute('SELECT key,value FROM metadata')}
            events = [dict(zip(('event_key', 'provider', 'status', 'payload'), (r[0], r[1], r[2], json.loads(r[3]))))
                for r in db.execute('SELECT event_key,provider,status,payload FROM events')]
        finally:
            db.close()
    return {'items': items, 'operations': operations, 'metadata': metadata, 'events': events,
            'files': files, 'exported_at': manifest['exported_at']}


def _digest_of(material):
    """Content identity across representations: full originals pre-cut,
    reference stubs post-cut. Never invents bytes, only resolves them."""
    original = material.get('original') or {}
    sha256 = original.get('sha256') or material.get('digest')
    path = original.get('path') or ('originals/' + sha256 if sha256 else None)
    return sha256, path


def material_content(snapshot, item):
    """Only verified original bytes of the latest version, never model claims."""
    latest = {m['id']: m for m in item.get('materials', [])}
    result = []
    for material in latest.values():
        sha256, path = _digest_of(material)
        content = snapshot['files'].get(path) if path else None
        if content is None or sha(content) != sha256:
            continue
        result.append((material, content.decode('utf-8', errors='replace')))
    return result


def dependent_materials(current, source_id):
    """Evidence of actual material dependencies; unrelated artifacts never trigger correction."""
    return [{'item_id': obj['id'], 'material_id': material['id'], 'version': material['version'],
             'sha256': material.get('original', {}).get('sha256')}
            for obj in current for material in obj.get('materials', [])
            if source_id in material.get('basis', {}) or source_id in material.get('source_versions', {})]


def human_front_action(current, project_id, owner):
    candidates = [obj for obj in current if obj.get('parent_id') == project_id
        and obj.get('kind') == 'action' and obj.get('executor') == owner
        and obj.get('commitment') == 'committed' and obj.get('status') == 'active'
        and not obj.get('depends_on')]
    return candidates[0] if len(candidates) == 1 else None


def restart_state_proof(old, current, principal):
    """Verify quiescent elaborated state and unchanged records, including accumulated budget."""
    jobs = old['metadata'].get('execution:state', {}).get('jobs', {})
    quiescent = all(job.get('terminal') for job in jobs.values())
    principal_ops = [o for o in old['operations'] if o.get('actor') == principal
        and o.get('receipt', {}).get('status') in {'applied', 'already_applied'}]
    elaborated = bool(principal_ops and (old['metadata'].get('last_review')
        or any(material.get('author') == principal for obj in old['items'].values() for material in obj.get('materials', []))))
    old_ops = {o['operation_id']: o for o in old['operations']}
    new_ops = {o['operation_id']: o for o in current['operations']}
    preserved = (old['items'] == current['items'] and all(new_ops.get(k) == v for k, v in old_ops.items())
        and all(current['files'].get(k) == v for k, v in old['files'].items() if k.startswith('originals/'))
        and all(current['metadata'].get(k) == v for k, v in old['metadata'].items()
            if k == 'execution:state' or k == 'last_review' or k.startswith(('mandate:', 'attention'))))
    return {'elaborated': elaborated, 'quiescent': quiescent, 'state_preserved': preserved,
            'principal_operation_ids': [o['operation_id'] for o in principal_ops],
            'item_ids': sorted(old['items']), 'review_present': bool(old['metadata'].get('last_review')),
            'budget_preserved': old['metadata'].get('execution:state') == current['metadata'].get('execution:state')}


def evaluate_snapshots(case_id, before, after, evidence):
    """Evaluator seam; production CLI calls it only with verified service exports."""
    checks = []
    def check(name, condition, missing=False):
        checks.append({'check': name, 'status': 'PASS' if condition else 'ABSENT' if missing else 'FAIL'})
    aliases = evidence.get('aliases', {})
    items = after['items']
    scope_ids = set(aliases.values())
    while True:
        expanded = scope_ids | {i['id'] for i in items.values() if i.get('parent_id') in scope_ids or i.get('project_id') in scope_ids}
        if expanded == scope_ids:
            break
        scope_ids = expanded
    scoped = [i for i in items.values() if i['id'] in scope_ids]
    def item(key):
        return items.get(aliases.get(key), {})
    old_ops = {o['operation_id'] for o in before['operations']}
    principal = evidence.get('principal_actor', 'gtd-felix')
    operations = [o for o in after['operations'] if o['operation_id'] not in old_ops and o['actor'] == principal
                  and o['receipt'].get('status') in {'applied', 'already_applied'}
                  and (o['receipt'].get('item', {}).get('id') in scope_ids or 'review' in o['receipt'])]
    execution = after['metadata'].get('execution:state', {})
    jobs = [j for j in execution.get('jobs', {}).values() if j.get('item_id') in {i['id'] for i in scoped}]
    native = [j for j in jobs if (j.get('native') or {}).get('provider') in {'hermes', 'hermes-kanban'} and (j.get('native') or {}).get('id')
              and j.get('observations')]
    # No native witness means the principal journey did not run; do not turn
    # deterministic fixtures or an operator-populated final state into model PASS.
    if not native:
        return {'case': case_id, 'status': 'NOT_RUN', 'checks': [{'check': 'principal_native_execution', 'status': 'ABSENT'}],
                'limits': ['No observed Hermes execution in exported control state.']}
    check('principal_authenticated_mutation', bool(operations))
    def witnessed(job, observation):
        reference = observation.get('evidence_reference', '')
        stored = after['metadata'].get(reference, {})
        payload = stored.get('payload')
        payload_hash = sha(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode())
        return (reference == 'hermes:observation:' + job['id'] + ':' + payload_hash
            and stored.get('observation', {}).get('native_identity') == job['native']
            and stored.get('observation', {}).get('native_status') == observation.get('native_status'))
    check('native_observation_payload_persisted', any(witnessed(j, o) for j in native for o in j['observations']))
    check('native_model_and_effort', all(after['metadata'].get('hermes:intent:' + j['id'], {}).get('route', {}).get('model') == 'gpt-6-astra'
        and after['metadata'].get('hermes:intent:' + j['id'], {}).get('route', {}).get('reasoning_effort') == 'low' for j in native))
    progress_ids = {p['operation_id'] for j in native for p in j.get('progress', [])}
    check('native_job_bound_tool_progress', any(o['operation_id'] in progress_ids for o in operations))
    check('native_terminal_observed', any(j.get('terminal') and j['observations'][-1].get('native_status') == 'completed' for j in native))
    check('no_completed_human_decision', all(i.get('status') != 'done' for i in scoped if i.get('decision_needed')))
    check('no_completed_uncommitted_item', all(i.get('commitment') == 'committed' for i in scoped if i.get('status') == 'done'))
    check('budget_not_exceeded', all(j.get('charged_cost_usd', 0) <= j.get('max_cost_usd', 0)
        and j.get('observed_runtime_seconds', 0) <= j.get('max_runtime_seconds', 0) for j in jobs))
    # Material validity supplied by GET /materials is checked against the same
    # exported material identities; missing transport observation is not green.
    material_observations = evidence.get('materials', {})
    for obj in scoped:
        for assessment in obj.get('assessments', []):
            if assessment.get('satisfied') and assessment.get('material_id'):
                observed = next((m for m in material_observations.get(obj['id'], [])
                    if m['id'] == assessment['material_id'] and m['version'] == assessment.get('material_version')), None)
                check('assessed_material_current:' + obj['id'], bool(observed and observed.get('valid')), missing=observed is None)
    intervention = evidence.get('intervention', {})
    correction = next((o for o in after['operations'] if o['operation_id'] == intervention.get('operation_id')
        and o['actor'] != principal and o['receipt'].get('status') == 'applied'
        and o['receipt'].get('item', {}).get('id') == intervention.get('item_id')
        and o['receipt']['item'].get('version') == intervention.get('after_version')
        and o['receipt']['item'].get('text') == intervention.get('fields', {}).get('text')), None)
    def exact_material(material, observed):
        return (material.get('id') == observed.get('id') and material.get('version') == observed.get('version')
            and _digest_of(material)[0] == observed.get('original', {}).get('sha256')
            and bool(_digest_of(material)[0]))
    def post_correction_operation(operation, target_id):
        result = operation['receipt'].get('item', {})
        return bool(correction and operation['operation_id'] in progress_ids and result.get('id') == target_id
            and result.get('version', 0) > intervention.get('after_version', 0))
    review = after['metadata'].get('last_review', {})
    if case_id == 'G1':
        destinations = {'a': {'kind': 'action', 'commitment': 'committed'},
            'b': {'kind': 'project', 'commitment': 'committed'}, 'c': {'kind': 'reference'},
            'd': {'kind': 'possibility', 'commitment': 'proposed', 'review_at': '2030-02-10'},
            'e': {'status': 'withdrawn'}, 'f': {'decision_needed': True}}
        for key, kind in [('a', 'action'), ('b', 'project'), ('c', 'reference'), ('d', 'possibility')]:
            check('destination_' + key, item(key).get('kind') == kind)
        check('direct_intentions_committed', all(item(key).get('commitment') == 'committed' for key in ('a', 'b')))
        check('possibility_not_committed', item('d').get('commitment') == 'proposed')
        check('possibility_return', item('d').get('review_at') == '2030-02-10')
        check('withdrawn_not_done', item('e').get('status') == 'withdrawn')
        question = item('f').get('decision_question')
        check('ambiguity_visible', item('f').get('decision_needed') is True and isinstance(question, str) and bool(question.strip()))
        def original_preserved(key):
            initial, current = before['items'].get(aliases.get(key), {}), item(key)
            revisions = initial.get('source_revisions', [])
            original = initial.get('original', {})
            if (not revisions or not original or current.get('id') != initial.get('id')
                    or current.get('original') != original
                    or current.get('source_revisions', [])[:len(revisions)] != revisions):
                return False
            for blob in [original, *[revision.get('original', {}) for revision in revisions]]:
                path, expected = blob.get('path'), blob.get('sha256')
                old_bytes, new_bytes = before['files'].get(path), after['files'].get(path)
                if old_bytes is None or new_bytes is None or not expected or sha(old_bytes) != expected or sha(new_bytes) != expected:
                    return False
            return True
        check('originals_retained', all(original_preserved(key) for key in destinations))
        for key, fields in destinations.items():
            current = item(key)
            pertinent = {**fields, **({'decision_question': question} if key == 'f' else {})}
            check('principal_destination_receipt_' + key, any(o['operation_id'] in progress_ids
                and o['receipt'].get('item', {}).get('id') == current.get('id')
                and o['receipt']['item'].get('version', 0) > before['items'].get(current.get('id'), {}).get('version', 0)
                and o['receipt']['item'].get('version', 0) <= current.get('version', 0)
                and all(o['receipt']['item'].get(field) == value and current.get(field) == value
                        for field, value in pertinent.items()) for o in operations))
        check('processing_not_completion', all(item(k).get('status') != 'done' for k in ('a','b','d')))
        request_item = item('request')
        request_receipts = [o for o in operations if o['operation_id'] in progress_ids
            and o['receipt'].get('item', {}).get('id') == request_item.get('id')
            and o['receipt']['item'].get('version') == request_item.get('version')]
        request_closed = request_item.get('status') == 'done' and any(
            a.get('actor') == principal and a.get('satisfied') is True and a.get('evidence')
            and any(a in o['receipt']['item'].get('assessments', [])
                and o['receipt']['item'].get('status') == 'done' for o in request_receipts)
            for a in request_item.get('assessments', []))
        if request_closed:
            check('operative_request_resolved', True)
        elif request_item.get('status') == 'withdrawn' and any(
                o['receipt']['item'].get('clarification', {}).get('actor') == principal
                and o['receipt']['item']['clarification'].get('reason') for o in request_receipts):
            checks.append({'check': 'operative_request_resolved', 'status': 'REVIEW_REQUIRED',
                'item_id': request_item['id'], 'reason': 'Direction must verify the authenticated intake resolution actually fulfilled the operative request; withdrawal prose alone is not completion.'})
        else:
            check('operative_request_resolved', False)
        if all(c['status'] == 'PASS' for c in checks):
            checks.append({'check': 'ambiguity_question_useful', 'status': 'REVIEW_REQUIRED',
                'item_id': aliases.get('f'), 'question': question,
                'reason': 'Direction must compare the recorded question with the preserved original ambiguity; presence alone does not prove relevance.'})
    elif case_id == 'G2':
        children = [i for i in scoped if i.get('project_id') == aliases.get('project') or i.get('parent_id') == aliases.get('project')]
        check('two_independent_fronts', len({i.get('front') for i in children if i.get('front')}) >= 2)
        check('distinct_executors', len({i.get('executor') for i in children if i.get('executor')}) >= 2)
        structural_future = any(i.get('depends_on') and all(
            dependency in items and dependency != i['id'] for dependency in i['depends_on']) for i in children)
        project = item('project')
        plan = project.get('plan_steps')
        authenticated_plan = bool(plan and plan != before['items'].get(aliases.get('project'), {}).get('plan_steps')
            and any(o['operation_id'] in progress_ids
                and o['receipt'].get('item', {}).get('id') == project.get('id')
                and o['receipt']['item'].get('plan_steps') == plan for o in operations))
        project_receipts = [o['receipt']['item'] for o in operations if o['operation_id'] in progress_ids
            and o['receipt'].get('item', {}).get('id') == project.get('id')]
        assessment = (project.get('assessments') or [{}])[-1]
        authenticated_assessment = bool(assessment.get('actor') == principal and assessment.get('evidence')
            and assessment.get('gap') and project.get('result_gap') == assessment.get('gap')
            and assessment.get('item_version', -2) + 1 == project.get('version')
            and (not assessment.get('material_id') or any(observed.get('valid')
                and observed.get('id') == assessment['material_id']
                and observed.get('version') == assessment.get('material_version')
                for observed in material_observations.get(project.get('id'), [])))
            and any(r.get('version') == project.get('version') and assessment in r.get('assessments', [])
                and r.get('result_gap') == project.get('result_gap') for r in project_receipts)
            and all(sid in items and type(revision) is int
                and isinstance(items[sid].get('source_revisions'), list)
                and len(items[sid]['source_revisions']) == revision
                for sid, revision in assessment.get('source_versions', {}).items()))
        authenticated_material = any(text.strip()
            and any(observed.get('valid') and exact_material(material, observed)
                for observed in material_observations.get(project.get('id'), []))
            and any(any(exact_material(material, recorded) for recorded in r.get('materials', []))
                for r in project_receipts)
            for material, text in material_content(after, project))
        if structural_future:
            check('future_step_explicit', True)
        elif authenticated_plan or authenticated_assessment or authenticated_material:
            checks.append({'check': 'future_step_explicit', 'status': 'REVIEW_REQUIRED',
                'reason': 'Direction must verify the authenticated current project representation distinguishes a conditional future support step and does not offer it as executable before its condition.'})
        else:
            check('future_step_explicit', False)
        check('blocked_not_completed', all(i['status'] != 'done' for i in children if any(items.get(d, {}).get('status') != 'done' for d in i.get('depends_on', []))))
        if not evidence.get('intervention'):
            check('parent_not_prematurely_done', item('project').get('status') != 'done')
        completion = next((o for o in after['operations'] if o['operation_id'] == intervention.get('operation_id')
            and o['actor'] != principal and o['receipt'].get('status') == 'applied'
            and o['receipt'].get('item', {}).get('id') == intervention.get('item_id')
            and o['receipt']['item'].get('version') == intervention.get('after_version')
            and o['receipt']['item'].get('status') == 'done'), None)
        check('human_front_completed_observed', bool(completion and intervention.get('action') == 'done'
            and intervention.get('target_before', {}).get('executor') == evidence.get('owner_actor', 'felix')))
        consequence = bool(completion and any(o['operation_id'] in progress_ids
            and o['receipt'].get('item', {}).get('id') in scope_ids
            and o['receipt']['item'].get('updated_at', '') > completion['receipt']['item'].get('updated_at', '~')
            and o['receipt']['item'].get('version', 0) > intervention.get('before_versions', {}).get(o['receipt']['item']['id'], 0)
            for o in operations))
        consequence = consequence or bool(completion and any(o['operation_id'] in progress_ids
            and o['receipt'].get('review', {}).get('reviewed_at', '') > completion['receipt']['item'].get('updated_at', '~')
            and any(gap.get('item_id') in scope_ids for gap in o['receipt']['review'].get('gaps', []))
            for o in operations))
        check('post_completion_progress_recorded', consequence)
        if consequence:
            checks.append({'check': 'post_completion_consequence_useful', 'status': 'REVIEW_REQUIRED',
                'reason': 'Direction must verify the selected human action confirms the room and subsequent recorded progress is authorized advancement, a concrete gap or verified result.'})
    elif case_id == 'G3':
        # Recommendation must be an observed native reply, not an expected answer
        # passed to inference. Driver may attach a separately hashed native trace.
        reply_parts = []
        for job in native:
            blob = after['metadata'].get('hermes:artifact:' + job['id'], {})
            content = after['files'].get(blob.get('path'))
            if content is not None and sha(content) == blob.get('sha256'):
                reply_parts.append(content.decode('utf-8', errors='replace'))
        reply = '\n'.join(reply_parts)
        check('compatible_human_choice', bool(item('phone').get('title') and item('phone')['title'] in reply), missing=not reply)
        check('other_action_preserved', item('desk').get('status') == before['items'].get(aliases.get('desk'), {}).get('status'))
        check('independent_preparation', any(material_content(after, i) for i in scoped if i.get('created_by') == principal or i['id'] == aliases.get('prep')))
        query = item('request')
        captured = next((o['receipt']['item'] for o in after['operations']
            if o.get('actor') == evidence.get('owner_actor', 'felix')
            and o.get('receipt', {}).get('status') == 'applied'
            and o['receipt'].get('item', {}).get('id') == query.get('id')
            and o['receipt']['item'].get('version') == 1), {})
        original = captured.get('original', {})
        original_bytes = after['files'].get(original.get('path'))
        retained = bool(captured and original and original_bytes is not None
            and sha(original_bytes) == original.get('sha256') and query.get('original') == original
            and captured.get('source_revisions') and query.get('source_revisions', [])[:len(captured['source_revisions'])] == captured['source_revisions'])
        query_ops = [o['receipt']['item'] for o in operations if o['operation_id'] in progress_ids
            and o['receipt'].get('item', {}).get('id') == query.get('id')]
        classifications = [r for r in query_ops if r.get('kind') == 'reference'
            and r.get('commitment') == 'proposed' and r.get('version', 0) > 1
            and r.get('original') == original]
        answered = any(any(exact_material(material, observed) and observed.get('valid')
                for observed in material_observations.get(query.get('id'), []))
            and any(r.get('version', 0) > classified.get('version', 0)
                and any(exact_material(material, recorded) for recorded in r.get('materials', []))
                and not any(exact_material(material, recorded) for recorded in classified.get('materials', []))
                for r in query_ops for classified in classifications)
            for material, content in material_content(after, query) if content)
        organized = retained and query.get('kind') == 'reference' and query.get('commitment') == 'proposed' and query.get('status') == 'active'
        notes = query.get('notes')
        recorded_notes = isinstance(notes, str) and bool(notes.strip()) and any(
            r.get('kind') == 'reference' and r.get('commitment') == 'proposed'
            and r.get('notes') == notes and r.get('original') == original
            and r.get('version', 0) <= query.get('version', 0)
            and r.get('version', 0) >= classified.get('version', 0)
            for r in query_ops for classified in classifications)
        if organized and answered:
            check('answered_query_organized', True)
        elif organized and recorded_notes:
            checks.append({'check': 'answered_query_organized', 'status': 'REVIEW_REQUIRED',
                'item_id': query['id'], 'reason': 'Authenticated reference notes preserve the recorded answer; direction must verify they answer the query and remain pertinent to current context. Text presence alone does not establish semantic success.'})
        else:
            check('answered_query_organized', False)
    elif case_id == 'G4':
        check('review_recorded', bool(review))
        check('operational_and_human_distinct', review.get('operational_complete') is True and review.get('human_decision_pending') is True)
        check('silent_project_visible', any(g.get('item_id') == aliases.get('silent') for g in review.get('gaps', []))
              or any(i.get('parent_id') == aliases.get('silent') for i in scoped))
        check('possibility_and_responsibility_reviewed', {'possibility','responsibility'} <= set(review.get('views', [])))
        known_sources = set(items)
        check('unknown_accounts_not_claimed', set(review.get('source_coverage', {})) <= known_sources)
    elif case_id == 'G5':
        project = item('project')
        initial = before['items'].get(project.get('id'), {})
        preserved = all(project.get(k) == initial.get(k) for k in ('purpose', 'outcome', 'completion_criteria'))
        check('owner_purpose_preserved', preserved)
        project_ops = [o['receipt']['item'] for o in operations if o['operation_id'] in progress_ids
            and o['receipt'].get('item', {}).get('id') == project.get('id')
            and o['receipt']['item'].get('version', 0) > initial.get('version', 0)]
        planned = bool(project.get('plan_steps') and project.get('plan_steps') != initial.get('plan_steps')
            and any(r.get('plan_steps') == project['plan_steps'] for r in project_ops))
        next_action = any(i.get('parent_id') == project.get('id') and i.get('kind') == 'action'
            and i.get('commitment') == 'committed' and i.get('status') == 'active'
            and not i.get('decision_needed') and not i.get('depends_on')
            and any(o['operation_id'] in progress_ids and o['receipt'].get('item', {}) == i for o in operations)
            for i in scoped)
        decision = (project.get('decision_needed') is True and isinstance(project.get('decision_question'), str)
            and bool(project['decision_question'].strip()) and any(r.get('decision_needed') is True
                and r.get('decision_question') == project['decision_question'] for r in project_ops))
        material_ready = any(any(exact_material(m, observed) and observed.get('valid')
                for observed in material_observations.get(obj['id'], []))
            and any(o['operation_id'] in progress_ids and o['receipt'].get('item', {}).get('id') == obj['id']
                and any(exact_material(m, recorded) for recorded in o['receipt']['item'].get('materials', [])) for o in operations)
            for obj in scoped for m, content in material_content(after, obj) if content)
        if planned and next_action:
            check('plan_and_next_step', True)
        elif planned and decision and material_ready and preserved:
            checks.append({'check': 'plan_and_next_step', 'status': 'REVIEW_REQUIRED',
                'item_id': project['id'], 'reason': 'New authenticated plan, current decision and witnessed private material support an integrated next step; direction must assess sufficiency without requiring a child entity.'})
        else:
            check('plan_and_next_step', False)
        if preserved and planned:
            checks.append({'check': 'human_criterion_influences_plan', 'status': 'REVIEW_REQUIRED',
                'item_id': project['id'], 'reason': 'Direction must verify accessibility and the no-equipment constraint actually guide the plan and next movement; preserved text or keywords alone do not prove influence.'})
        else:
            check('human_criterion_influences_plan', False)
    elif case_id == 'G6':
        check('appointment_is_calendar', item('appointment').get('kind') == 'calendar' and bool(item('appointment').get('starts_at')))
        check('deadline_is_due_date', item('deadline').get('due_at', '').startswith('2030-03-06'))
        check('reminder_is_return_not_deadline', item('reminder').get('review_at') == '2030-03-07' and not item('reminder').get('due_at'))
    elif case_id == 'G7':
        check('single_executor_native', len({j['native']['profile'] for j in native if j['native']['provider'] == 'hermes-kanban' and j.get('parent_job_id')}) == 1)
        check('human_waiting_not_acceptance', any(i.get('kind') == 'waiting' and i.get('waiting_for') and i.get('status') != 'done' for i in scoped))
        old_ids = {j['id'] for j in intervention.get('native_jobs_before', [])
            if (j.get('native') or {}).get('provider') == 'hermes-kanban' and j.get('parent_job_id')
            and j.get('native_status') == 'running' and not j.get('terminal')}
        check('correction_during_execution', bool(correction and old_ids and intervention.get('trigger_observed') == 'native_running'))
        check('old_execution_not_promoted', bool(old_ids) and all(any(j['id'] == old_id
            and (j.get('stop_requested') or j.get('integration') in {'discarded', 'rejected'})
            and j.get('integration') != 'integrated' for j in jobs) for old_id in old_ids))
        project_id = aliases.get('project')
        def belongs(target_id):
            seen = set()
            while target_id and target_id not in seen:
                if target_id == project_id:
                    return True
                seen.add(target_id)
                obj = items.get(target_id, {})
                target_id = obj.get('project_id') or obj.get('parent_id')
            return False
        def delivered(job):
            if not (correction and job['id'] not in old_ids and job.get('parent_job_id')
                and job['native']['provider'] == 'hermes-kanban' and job.get('terminal')
                and job['observations'][-1].get('native_status') == 'completed'
                and witnessed(job, job['observations'][-1]) and job.get('integration') == 'integrated'
                and belongs(job.get('item_id'))):
                return False
            # Durable integration is an authenticated executor put_material,
            # not a principal operation or an unrelated assessment receipt.
            operation_id = 'gtd-output:' + job['id']
            if (job.get('domain_operation_id') != operation_id or operation_id in old_ops
                or job.get('actor') not in after['metadata'].get('actor_config', {}).get('executor_actors', [])):
                return False
            op = next((o for o in after['operations'] if o['operation_id'] == operation_id
                and o['actor'] == job['actor']), None)
            receipt = (op or {}).get('receipt', {})
            result = receipt.get('item', {})
            artifact = after['metadata'].get('hermes:artifact:' + job['id'], {})
            return bool(receipt.get('operation_id') == operation_id
                and receipt.get('status') == 'applied' and result.get('id') == job['item_id']
                and isinstance(job.get('validated_version'), int)
                and result.get('version') == job['validated_version'] + 1
                and artifact.get('job_id') == job['id']
                and any(m.get('author') == job['actor'] and m.get('mandate_id') == job.get('mandate_id')
                and _digest_of(m)[0] == artifact.get('sha256')
                and any(exact_material(m, observed) and observed.get('valid')
                    for observed in material_observations.get(job['item_id'], []))
                for m, content in material_content(after, op['receipt'].get('item', {}))))
        check('return_to_correct_project', any(delivered(j) for j in native))
    elif case_id == 'G8':
        restart = evidence.get('restart', {})
        check('owned_restart_observed', bool(restart.get('validated_exports') and restart.get('after_ready')
            and restart.get('before_stopped', {}).get('pid_absent')
            and restart.get('before_stopped', {}).get('status') == 'STOPPED'
            and restart.get('before_process_id') != restart.get('after_process_id')), missing=not restart)
        check('inventory_retained', set(before['items']) <= set(items))
        check('suggestion_not_committed', item('suggestion').get('commitment') != 'committed')
        proof = restart.get('state_proof', {})
        check('elaborated_state_preserved', bool(proof.get('elaborated') and proof.get('quiescent')
            and proof.get('state_preserved') and proof.get('budget_preserved')))
        check('return_processed_after_restart', any(o['receipt'].get('item', {}).get('id') == aliases.get('return')
            and o['operation_id'] in progress_ids for o in operations))
        check('review_retained', not proof.get('review_present') or bool(review))
        checks.append({'check': 'without_thematic_specialists', 'status': 'REVIEW_REQUIRED',
            'bot_ids': sorted(execution.get('bots', {})),
            'used_bot_ids': sorted({j.get('bot_id') for j in jobs if j.get('bot_id')}),
            'reason': 'Direction must verify registered and used identities are the principal and at most its generic executor, not thematic specialists.'})
    elif case_id == 'G9':
        project = item('project')
        children = [i for i in scoped if i.get('parent_id') == project.get('id') and i.get('created_by') == principal]
        def corrected_json(content):
            try:
                value = json.loads(content)
                return value.get('dias') == {'lunes': 7, 'martes': 13} and value.get('total') == 20 and bool(value.get('explicacion'))
            except (ValueError, TypeError, AttributeError):
                return False
        check('actual_corrected_artifact', any(corrected_json(content)
            and any(m.get('id') == material['id'] and m.get('version') == material['version'] and m.get('valid')
                for m in material_observations.get(i['id'], []))
            for i in scoped for material, content in material_content(after, i)))
        def returns_json(content):
            try:
                rows = json.loads(content)
                if isinstance(rows, dict):
                    rows = rows.get('devoluciones')
                return (isinstance(rows, list) and len(rows) == 2
                    and all(isinstance(row, dict) and set(row) == {'persona', 'libro'}
                        and isinstance(row['persona'], str) and isinstance(row['libro'], str) for row in rows)
                    and {(row['persona'], row['libro']) for row in rows} == {('Ana', 'Atlas'), ('Luis', 'Jardín')})
            except (ValueError, TypeError):
                return False
        def current_material(obj, material):
            return any(exact_material(material, observed) and observed.get('valid')
                for observed in material_observations.get(obj['id'], []))
        totals = [(obj, material) for obj in scoped for material, content in material_content(after, obj)
            if corrected_json(content) and current_material(obj, material)]
        returns = [(obj, material) for obj in scoped for material, content in material_content(after, obj)
            if returns_json(content) and current_material(obj, material)]
        pairs = [(total, pending) for _, total in totals for _, pending in returns
            if total['id'] != pending['id'] and _digest_of(total)[0] != _digest_of(pending)[0]]
        check('separate_current_returns_artifact', bool(pairs))
        deliverable_hashes = {_digest_of(m)[0] for pair in pairs for m in pair}
        def contributed(child):
            if not child.get('mandate_id') or child.get('commitment') != 'committed':
                return False
            created = any(o['operation_id'] in progress_ids
                and o['receipt'].get('item', {}).get('id') == child['id']
                and o['receipt']['item'].get('version') == 1
                and o['receipt']['item'].get('mandate_id') == child['mandate_id'] for o in operations)
            return created and any(current_material(child, material)
                and _digest_of(material)[0] in deliverable_hashes
                and any(o['operation_id'] in progress_ids and o['receipt'].get('item', {}).get('id') == child['id']
                    and any(exact_material(material, recorded) for recorded in o['receipt']['item'].get('materials', []))
                    for o in operations) for material, _ in material_content(after, child))
        check('derived_under_mandate', any(contributed(child) for child in children))
        check('correction_observed', evidence.get('intervention', {}).get('trigger_observed') == 'material_created')
        def assessed_corrected(material, content):
            if not corrected_json(content) or not correction:
                return False
            observed = any(exact_material(material, m) and m.get('valid')
                for m in material_observations.get(project.get('id'), []))
            assessments = [a for a in project.get('assessments', []) if a.get('satisfied') and a.get('evidence')
                and a.get('material_id') == material['id'] and a.get('material_version') == material['version']
                and a.get('item_version', 0) >= intervention.get('after_version', 0)]
            creation = any(post_correction_operation(o, project['id'])
                and any(exact_material(material, m) for m in o['receipt']['item'].get('materials', [])) for o in operations)
            assessment_receipt = any(post_correction_operation(o, project['id'])
                and o['receipt']['item'].get('status') == 'done'
                and any(a in o['receipt']['item'].get('assessments', []) for a in assessments) for o in operations)
            return observed and creation and assessment_receipt and bool(assessments)
        exact_closure = project.get('status') == 'done' and any(
            assessed_corrected(m, content) for m, content in material_content(after, project))
        joint_assessments = [a for a in project.get('assessments', [])
            if a.get('actor') == principal and a.get('satisfied') is True and a.get('evidence')
            and a.get('item_version', 0) >= intervention.get('after_version', 0)
            and any(post_correction_operation(o, project['id'])
                and o['receipt']['item'].get('status') == 'done'
                and a in o['receipt']['item'].get('assessments', []) for o in operations)]
        if exact_closure:
            check('criterion_assessed_and_closed', True)
        elif project.get('status') == 'done' and joint_assessments and pairs and any(contributed(c) for c in children):
            checks.append({'check': 'criterion_assessed_and_closed', 'status': 'REVIEW_REQUIRED',
                'item_id': project['id'],
                'reason': 'Authenticated post-correction root assessment closes the project with current deliverables and witnessed derived work; direction must verify textual joint coverage against child artifacts and receipts. Material copies on the root are not required.'})
        else:
            check('criterion_assessed_and_closed', False)
        def assessed_in_closure(material):
            return any(a.get('satisfied') and a.get('evidence')
                and a.get('material_id') == material['id'] and a.get('material_version') == material['version']
                and any(post_correction_operation(o, project['id'])
                    and o['receipt']['item'].get('status') == 'done'
                    and a in o['receipt']['item'].get('assessments', []) for o in operations)
                for a in project.get('assessments', []))
        both_assessed = any(assessed_in_closure(total) and assessed_in_closure(pending) for total, pending in pairs)
        if both_assessed:
            check('both_deliverables_in_closure', True)
        elif pairs:
            checks.append({'check': 'both_deliverables_in_closure', 'status': 'REVIEW_REQUIRED',
                'reason': 'Current deliverables exist, but exact assessments do not link both to project closure; direction must review artifacts, receipts and transcript, retaining an external technical verdict with hashes.'})
        else:
            check('both_deliverables_in_closure', False)
        check('work_ceased', all(j.get('terminal') for j in jobs))
    elif case_id == 'G10':
        witnesses = intervention.get('dependent_materials_before', [])
        check('source_change_during_work', bool(correction and intervention.get('trigger_observed') == 'material_created' and witnesses))
        check('dependent_material_invalidated', any(not observed.get('valid')
            and any(observed.get('id') == witness.get('material_id') and observed.get('version') == witness.get('version')
                and observed.get('original', {}).get('sha256') == witness.get('sha256') for witness in witnesses)
            for entries in material_observations.values() for observed in entries))
        check('human_correction_retained', '10:00' in item('source').get('text', '') and '13:00' in item('source').get('text', ''))
        def after_change(value):
            try:
                observed = datetime.fromisoformat(value)
                changed = datetime.fromisoformat((correction or {}).get('receipt', {}).get('item', {}).get('updated_at'))
                return bool(correction and observed.utcoffset() is not None and changed.utcoffset() is not None
                    and observed > changed)
            except (TypeError, ValueError, KeyError):
                return False
        covered_ids = {aliases.get(key) for key in ('source', 'independent', 'decision', 'request')}
        covered_kinds = {items[sid].get('kind') for sid in covered_ids if sid in items}
        recorded_reviews = [o['receipt']['review'] for o in operations
            if o['operation_id'] in progress_ids and 'review' in o['receipt']]
        check('review_after_change', bool(None not in covered_ids and any(
            r.get('actor') == principal and after_change(r.get('reviewed_at'))
            and r.get('human_decision_pending') is True and covered_kinds <= set(r.get('views', []))
            and all(sid in items and isinstance(items[sid].get('source_revisions'), list)
                and type(r.get('source_coverage', {}).get(sid)) is int
                and r['source_coverage'][sid] == len(items[sid]['source_revisions']) for sid in covered_ids)
            for r in recorded_reviews)))
        def authenticated_current_material(obj, material):
            return any(observed.get('valid') and exact_material(material, observed)
                for observed in material_observations.get(obj.get('id'), [])) and any(
                o['operation_id'] in progress_ids and o['receipt'].get('item', {}).get('id') == obj.get('id')
                and any(exact_material(material, recorded) for recorded in o['receipt']['item'].get('materials', []))
                for o in operations)
        revised = [(obj, material) for obj in scoped for material, content in material_content(after, obj)
            if content.strip() and after_change(material.get('created_at'))
            and aliases.get('source') in material.get('basis', {})
            and authenticated_current_material(obj, material)]
        check('dependent_result_revised', bool(revised))
        request = item('request')
        def assessment_basis_preserved(assessment, recorded):
            if (recorded.get('version') != assessment.get('item_version', -2) + 1
                    or assessment not in recorded.get('assessments', [])
                    or recorded.get('version', 0) > request.get('version', 0)):
                return False
            pertinent = ('title', 'kind', 'purpose', 'outcome', 'completion_criteria',
                'commitment', 'executor', 'project_id', 'responsibility_id', 'depends_on',
                'text', 'source', 'source_revisions', 'source_versions', 'intent_basis',
                'work_capability', 'mandate_id', 'decision_needed', 'decision_question', 'status', 'result_gap')
            if any(recorded.get(key) != request.get(key) for key in pertinent):
                return False
            if assessment.get('material_id'):
                return any(m.get('id') == assessment['material_id']
                    and m.get('version') == assessment.get('material_version')
                    and any(exact_material(m, current) for obj, current in revised if obj.get('id') == request.get('id'))
                    for m in recorded.get('materials', []))
            # Without a named supporting material, retain the entire current
            # material set present at assessment, rather than guessing its basis.
            old_materials = {m['id']: m for m in recorded.get('materials', [])}
            current_materials = {m['id']: m for m in request.get('materials', [])}
            return (old_materials.keys() == current_materials.keys()
                and all(exact_material(m, current_materials[mid])
                    and authenticated_current_material(request, current_materials[mid])
                    for mid, m in old_materials.items()))
        resolved = [a for a in request.get('assessments', [])
            if a.get('actor') == principal and a.get('evidence') and after_change(a.get('assessed_at'))
            and ((a.get('satisfied') is True and request.get('status') == 'done')
                or (a.get('satisfied') is False and a.get('gap') and request.get('result_gap') == a['gap']))
            and (not a.get('material_id') or any(obj.get('id') == request.get('id')
                and material.get('id') == a['material_id'] and material.get('version') == a.get('material_version')
                for obj, material in revised))
            and all(sid in items and isinstance(items[sid].get('source_revisions'), list)
                and type(revision) is int and len(items[sid]['source_revisions']) == revision
                for sid, revision in a.get('source_versions', {}).items())
            and any(o['operation_id'] in progress_ids and o['receipt'].get('item', {}).get('id') == request.get('id')
                and assessment_basis_preserved(a, o['receipt']['item']) for o in operations)]
        def assessed_coverage(assessment):
            sources = assessment.get('source_versions', {})
            bases = assessment.get('resolution_basis', {})
            if None in covered_ids or not covered_ids <= sources.keys() or not covered_ids <= bases.keys():
                return False
            if any(not isinstance(bases[sid], dict)
                    or bases[sid].get('source') != items[sid].get('source', {})
                    or bases[sid].get('revisions') != items[sid].get('source_revisions')
                    for sid in covered_ids):
                return False
            for obj, material in revised:
                if (obj.get('id') != request.get('id') or material.get('id') != assessment.get('material_id')
                        or material.get('version') != assessment.get('material_version')
                        or not covered_ids <= material.get('basis', {}).keys()
                        or any(material.get('source_versions', {}).get(sid) != sources[sid] for sid in covered_ids)
                        or not any(exact_material(material, m) for m in assessment.get('material_basis', []))):
                    continue
                # Optional normalized native read receipts are supplementary
                # evidence supplied by an offline collector, never model prose.
                reads = evidence.get('native_material_reads')
                if reads is not None and not any(
                        r.get('job_id') in {j['id'] for j in native}
                        and r.get('item_id') == obj['id'] and r.get('material_id') == material['id']
                        and r.get('version') == material['version'] and r.get('valid') is True
                        and r.get('sha256') == _digest_of(material)[0] for r in reads):
                    continue
                return True
            return False
        coverage_check = next(c for c in checks if c['check'] == 'review_after_change')
        if (coverage_check['status'] != 'PASS' and request.get('commitment') == 'committed'
                and request.get('completion_criteria') and any(assessed_coverage(a) for a in resolved)):
            coverage_check.update(status='REVIEW_REQUIRED', reason=(
                'Authenticated post-change assessment and exact current material retain the four source bases. '
                'Direction must verify actual causal examination, native read evidence when available, '
                'independent work and pending human judgment. Source IDs or prose alone do not establish review.'))
        if request.get('commitment') == 'committed' and request.get('completion_criteria') and resolved:
            checks.append({'check': 'private_request_resolved', 'status': 'REVIEW_REQUIRED',
                'reason': 'Direction must verify the authenticated post-change assessment against the corrected material and actual criterion, including whether any remaining gap is necessary. A native final reply or material alone is insufficient.'})
        else:
            check('private_request_resolved', False)
        check('independent_work_advanced', bool(material_content(after, item('independent'))) or any(i.get('parent_id') == aliases.get('independent') for i in scoped))
        check('old_material_invalidated', any(not m.get('valid') for entries in material_observations.values() for m in entries))
        check('silence_not_consent', item('decision').get('decision_needed') is True and item('decision').get('status') != 'done')
    failures = [c for c in checks if c['status'] != 'PASS']
    return {'case': case_id, 'status': ('FAIL' if any(c['status'] != 'REVIEW_REQUIRED' for c in failures)
                                     else 'REVIEW_REQUIRED') if failures else 'PASS', 'checks': checks,
            'limits': ['Exported service receipts prove recorded mutations, not independent provider authenticity or human acceptance.']}


class ProductDriver:
    def __init__(self, config, session, destination):
        self.config, self.session, self.destination = config, session, Path(destination)
        self.calls, self.trace = 0, []
        self.started = time.monotonic()
        self.closing = False
        self.closure_seconds = config.get('closure_seconds', min(30, config['timeout_seconds'] / 4))
        self.closure_calls = config.get('closure_max_http_calls', min(20, max(4, config['max_http_calls'] // 4)))
        parsed = urlsplit(config['product_api_url'])
        if parsed.scheme != 'http' or parsed.hostname not in {'127.0.0.1','::1','localhost'} or parsed.username or parsed.password or parsed.path not in {'','/'} or parsed.query or parsed.fragment:
            raise ValueError('local_product_api_required')
        self.url = config['product_api_url'].rstrip('/')
        self.token = os.environ.get(config['owner_token_env'], '')
        if not self.token or config.get('synthetic') is not True:
            raise ValueError('explicit_synthetic_configuration_required')
        for field in ('timeout_seconds','max_http_calls','max_cases','poll_interval_seconds'):
            if not isinstance(config.get(field), (int,float)) or config[field] <= 0:
                raise ValueError('explicit_limits_required')
        if (not isinstance(self.closure_seconds, (int, float)) or not 0 < self.closure_seconds <= 30
                or not isinstance(self.closure_calls, int) or isinstance(self.closure_calls, bool)
                or not 1 <= self.closure_calls < config['max_http_calls']):
            raise ValueError('invalid_closure_limits')

    async def request(self, method, path, payload=None, binary=False):
        limit = self.config['max_http_calls'] if self.closing else self.config['max_http_calls'] - self.closure_calls
        deadline = self.closure_deadline if self.closing else self.started + self.config['timeout_seconds']
        if self.calls >= limit:
            raise ValueError('probe_http_budget_exhausted')
        if time.monotonic() >= deadline:
            raise ValueError('probe_time_budget_exhausted')
        self.calls += 1
        async with asyncio.timeout(max(.001, deadline - time.monotonic())):
            async with self.session.request(method, self.url + path, json=payload,
                headers={'Authorization': 'Bearer ' + self.token}, allow_redirects=False) as response:
                data = await response.read()
                self.trace.append({'sequence': self.calls, 'method': method, 'path': path,
                    'status': response.status, 'response_sha256': sha(data), 'observed_at': datetime.now(timezone.utc).isoformat()})
                if response.status >= 400:
                    raise ValueError('product_request_rejected')
                return data if binary else json.loads(data)

    async def snapshot(self, filename):
        data = await self.request('GET', '/v1/export', binary=True)
        write_new(self.destination / filename, data)
        return {'file': filename, 'sha256': sha(data)}

    async def command(self, operation_id, item, action, fields):
        result = await self.request('POST', '/v1/commands', {'operation_id': operation_id,
            'item_id': item['id'], 'expected_version': item['version'], 'action': action, 'fields': fields})
        if result.get('status') not in {'applied', 'already_applied'}:
            raise ValueError('precondition_rejected')
        return result.get('item', item)

    async def prepare_case(self, record):
        configured = set(self.config.get('bot_ids', []))
        if not configured:
            raise ValueError('explicit_trial_bot_ids_required')
        bots = await self.request('POST', '/v1/control/bots', {})
        own = [bot for bot in bots if bot.get('id') in configured]
        if {bot['id'] for bot in own} != configured or any(bot.get('state') != 'available' or not bot.get('probe_evidence') for bot in own):
            raise ValueError('verified_trial_bots_required')
        self.prepared_bots = own
        for bot in own:
            receipt = await self.request('POST', '/v1/control/register_bot', {
                'operation_id': record['run_id'] + ':prepare:' + bot['id'], 'bot': {**bot, 'state': 'suspended'}})
            if receipt.get('status') != 'applied':
                raise ValueError('trial_suspension_failed')
        if any(not job.get('terminal') for job in await self.request('POST', '/v1/control/pending', {})):
            raise ValueError('preparation_started_with_active_jobs')
        return {'suspended_bots': sorted(configured), 'observed_at': datetime.now(timezone.utc).isoformat()}

    async def enable_case(self, record):
        current = {bot['id']: bot for bot in await self.request('POST', '/v1/control/bots', {})}
        own = getattr(self, 'prepared_bots', [])
        if not own or any(current.get(bot['id']) != {**bot, 'state': 'suspended'} for bot in own):
            raise ValueError('prepared_bot_identity_or_suspension_changed')
        if any(not job.get('terminal') for job in await self.request('POST', '/v1/control/pending', {})):
            raise ValueError('inference_started_before_case_ready')
        for bot in own:
            receipt = await self.request('POST', '/v1/control/register_bot', {
                'operation_id': record['run_id'] + (':return-ready:' if record.get('restart') else ':ready:') + bot['id'], 'bot': bot})
            if receipt.get('status') != 'applied':
                raise ValueError('trial_promotion_failed')
        return {'enabled_bots': [bot['id'] for bot in own], 'observed_at': datetime.now(timezone.utc).isoformat()}

    async def run_case(self, case_id, *, restart=None, case_prepare=None, case_ready=None):
        scenario, identity = SCENARIOS[case_id], uuid.uuid4().hex
        record = {'case': case_id, 'run_id': identity, 'aliases': {}, 'materials': {},
            'owner_actor': self.config.get('owner_actor', 'felix'),
            'principal_actor': self.config.get('principal_actor','gtd-felix'), 'transport': 'product_http',
            'model_constraint': 'gpt-6-astra', 'reasoning_constraint': 'low'}
        try:
            if case_prepare is not None:
                record['preparation'] = await case_prepare(self, record)
            for seed in scenario['inputs']:
                result = await self.request('POST', '/v1/captures', {'operation_id': identity + ':' + seed['key'],
                    'text': seed['text'], 'source': {'acceptance_case': case_id, 'acceptance_run': identity, **seed.get('source', {})}})
                if result.get('status') not in {'applied','already_applied'}:
                    raise ValueError('capture_precondition_rejected')
                obj = result['item']
                record['aliases'][seed['key']] = obj['id']
                if seed.get('fields'):
                    obj = await self.command(identity + ':seed:' + seed['key'], obj, 'clarify', seed['fields'])
                if scenario.get('mandate') == seed['key']:
                    obj = await self.command(identity + ':mandate', obj, 'grant_mandate', {
                        'scope_item_id': obj['id'], 'capabilities': ['prepare_private','local_work'],
                        'actors': [record['principal_actor'], *self.config.get('executor_actors', [])],
                        'completion_criteria': obj['completion_criteria']})
            record['before'] = await self.snapshot(identity + '-before.zip')
            request = await self.request('POST', '/v1/captures', {'operation_id': identity + ':request',
                'text': scenario['request'], 'source': {'acceptance_case': case_id, 'acceptance_run': identity}})
            record['aliases']['request'] = request['item']['id']
            if case_ready is not None:
                record['admission'] = await case_ready(self, record)
            deadline = min(self.started + self.config['timeout_seconds'],
                time.monotonic() + self.config.get('case_timeout_seconds', self.config['timeout_seconds']))
            terminal_pending_since = None
            previous_pending = None
            settled = 0
            last = None
            while time.monotonic() < deadline:
                current = await self.request('GET', '/v1/items')
                jobs = await self.request('POST', '/v1/control/pending', {})
                state_hash = sha(canonical(current))
                pending_hash = sha(canonical([state_hash, jobs]))
                if jobs and all(j.get('terminal') for j in jobs):
                    terminal_pending_since = terminal_pending_since if pending_hash == previous_pending else time.monotonic()
                    if time.monotonic() - terminal_pending_since >= 15:
                        raise ValueError('terminal_integration_stalled')
                else:
                    terminal_pending_since = None
                previous_pending = pending_hash
                settled = settled + 1 if state_hash == last and not jobs else 0
                last = state_hash
                intervention = scenario.get('intervention')
                if intervention and 'intervention' not in record:
                    native_running = any(j.get('parent_job_id') and (j.get('native') or {}).get('provider') == 'hermes-kanban'
                        and not j.get('terminal') and j.get('observations')
                        and j['observations'][-1].get('native_status') == 'running' for j in jobs)
                    target = next((i for i in current if i['id'] == record['aliases'][intervention['key']]), None)
                    dependencies = dependent_materials(current, target['id']) if case_id == 'G10' and target else []
                    if case_id == 'G2':
                        target = human_front_action(current, record['aliases']['project'], self.config.get('owner_actor', 'felix'))
                    material_created = any(i.get('materials') for i in current if i['id'] in record['aliases'].values()
                        or i.get('parent_id') in record['aliases'].values())
                    if case_id == 'G10':
                        material_created = bool(dependencies)
                    if (intervention['trigger'] == 'human_action_available' and target) or (intervention['trigger'] == 'native_running' and native_running) or (intervention['trigger'] == 'material_created' and material_created):
                        pre_versions = {obj['id']: obj.get('version', 0) for obj in current}
                        changed = await self.command(identity + ':intervention', target, intervention.get('action', 'edit'), intervention['fields'])
                        record['intervention'] = {'trigger_observed': intervention['trigger'],
                            'at': datetime.now(timezone.utc).isoformat(), 'operation_id': identity + ':intervention',
                            'item_id': target['id'], 'before_version': target['version'], 'after_version': changed['version'],
                            'fields': intervention['fields'], 'action': intervention.get('action', 'edit'),
                            'before_versions': pre_versions, 'target_before': target, 'dependent_materials_before': dependencies,
                            'native_jobs_before': [
                                {'id': j['id'], 'item_id': j['item_id'], 'expected_version': j.get('expected_version'),
                                 'native': j.get('native'), 'terminal': j.get('terminal'), 'parent_job_id': j.get('parent_job_id'),
                                 'native_status': (j.get('observations') or [{}])[-1].get('native_status')}
                                for j in jobs if j.get('native') and not j.get('terminal')]}

                        settled = 0
                if settled >= 3:
                    if case_id == 'G8' and 'restart' not in record:
                        if restart is None:
                            raise ValueError('owned_restart_callback_required')
                        record['restart'] = await restart(self, record)
                        if case_ready is not None:
                            record['readmission'] = await case_ready(self, record)
                        returned = await self.request('POST', '/v1/captures', {'operation_id': identity + ':return',
                            'text': scenario['return_request'], 'source': {'acceptance_case': case_id, 'acceptance_run': identity}})
                        record['aliases']['return'] = returned['item']['id']
                        settled, last = 0, None
                        continue
                    break
                await asyncio.sleep(self.config['poll_interval_seconds'])
            else:
                raise ValueError('probe_time_budget_exhausted')
            record['status'] = 'COLLECTED'
        except Exception as error:
            record['status'] = 'PARTIAL' if 'request' in record['aliases'] else 'NOT_RUN'
            safe = {'probe_http_budget_exhausted', 'probe_time_budget_exhausted', 'terminal_integration_stalled',
                    'product_request_rejected', 'capture_precondition_rejected', 'precondition_rejected'}
            record['error'] = str(error) if isinstance(error, ValueError) and str(error) in safe else (
                'probe_transport_timeout' if isinstance(error, TimeoutError) else 'probe_dependency_or_transport_failed')
        finally:
            self.closing = True
            self.closure_deadline = time.monotonic() + self.closure_seconds
            if 'before' in record:
                async def collect_after():
                    # Export first: material observation exhaustion must not lose the ledger.
                    record['after'] = await self.snapshot(identity + '-after.zip')
                    current = await self.request('GET', '/v1/items')
                    for obj in current:
                        if obj['id'] in record['aliases'].values() or obj.get('parent_id') in record['aliases'].values():
                            record['materials'][obj['id']] = await self.request('GET', '/v1/materials/' + obj['id'])
                try:
                    await asyncio.wait_for(collect_after(), self.closure_seconds)
                    record['closure_status'] = 'COLLECTED'
                except Exception:
                    record['closure_status'] = 'INCOMPLETE'
                    record['closure_error'] = 'final_observation_unavailable'
                    record['status'] = 'PARTIAL'
            self.closing = False
        record['http_trace'] = self.trace[:]
        write_new(self.destination / (identity + '-evidence.json'), canonical(record))
        return record


def evaluate_record(record, directory):
    if record.get('status') == 'PARTIAL' or record.get('closure_status') == 'INCOMPLETE':
        return {'case': record['case'], 'status': 'FAIL', 'checks': [{'check': 'complete_observation', 'status': 'ABSENT'}],
                'limits': ['Partial collection preserves evidence but cannot accredit the case.']}
    if record.get('status') != 'COLLECTED' or not all(k in record for k in ('before','after')):
        return {'case': record['case'], 'status': 'NOT_RUN', 'checks': [], 'limits': ['Incomplete product observation.']}
    snapshots = []
    root = Path(directory).resolve()
    export_hashes = {entry.get('response_sha256') for entry in record.get('http_trace', [])
        if entry.get('method') == 'GET' and entry.get('path') == '/v1/export' and entry.get('status') == 200 and entry.get('observed_at')}
    if record.get('transport') != 'product_http' or any(record[key]['sha256'] not in export_hashes for key in ('before','after')):
        raise ValueError('product_export_observation_required')
    for key in ('before','after'):
        path = root / record[key]['file']
        if path.is_symlink() or path.resolve().parent != root:
            raise ValueError('evidence_path_outside_directory')
        snapshots.append(load_snapshot(path, record[key]['sha256']))
    if record['case'] == 'G8' and record.get('restart'):
        restart = record['restart']
        receipt_path = root / restart['file']
        if receipt_path.is_symlink() or receipt_path.resolve().parent != root:
            raise ValueError('restart_receipt_path_invalid')
        data = receipt_path.read_bytes()
        if sha(data) != restart['sha256'] or json.loads(data) != {k:v for k,v in restart.items() if k not in {'file','sha256','validated_exports'}}:
            raise ValueError('restart_receipt_mismatch')
        restart_states = []
        for phase in ('before','after'):
            descriptor = restart[phase]
            path = root / descriptor['file']
            if path.is_symlink() or path.resolve().parent != root or descriptor['sha256'] not in export_hashes:
                raise ValueError('restart_export_not_observed')
            restart_states.append(load_snapshot(path, descriptor['sha256']))
        old, current = restart_states
        proof = restart_state_proof(old, current, record.get('principal_actor', 'gtd-felix'))
        preserved = proof['state_preserved'] and proof['budget_preserved'] and proof['elaborated'] and proof['quiescent']
        preserved = preserved and {o['operation_id'] for o in old['operations']} <= {o['operation_id'] for o in current['operations']}
        preserved = preserved and all(current['files'].get(k) == v for k,v in old['files'].items() if k.startswith('originals/'))
        ids = (restart.get('before_process_id'), restart.get('after_process_id'))
        if not preserved or any(type(pid) is not int or pid <= 0 for pid in ids) or ids[0] == ids[1] or restart.get('before_stopped', {}).get('pid') != ids[0]:
            raise ValueError('restart_identity_or_state_invalid')
        record = {**record, 'restart': {**restart, 'validated_exports': True, 'state_proof': proof}}
    return evaluate_snapshots(record['case'], *snapshots, record)


async def run(config, destination, cases):
    import aiohttp
    if len(cases) > config.get('max_cases', 0):
        raise ValueError('case_budget_exceeded')
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=config['timeout_seconds']), trust_env=False) as session:
        driver = ProductDriver(config, session, destination)
        capabilities = await driver.request('GET','/v1/capabilities')
        if capabilities.get('role') != 'owner':
            raise ValueError('owner_token_required')
        # Deliberately excludes personal or previously populated instances.
        if await driver.request('GET', '/v1/items'):
            raise ValueError('empty_synthetic_service_required')
        return [await driver.run_case(case, case_prepare=lambda d,r: d.prepare_case(r),
            case_ready=lambda d,r: d.enable_case(r)) for case in cases]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    prepare = sub.add_parser('prepare'); prepare.add_argument('--output', required=True)
    evaluate = sub.add_parser('evaluate'); evaluate.add_argument('--evidence', required=True)
    live = sub.add_parser('run'); live.add_argument('--execute', action='store_true')
    live.add_argument('--config', required=True); live.add_argument('--evidence-dir', required=True)
    live.add_argument('--case', action='append', choices=SCENARIOS, required=True)
    args = parser.parse_args(argv)
    try:
        if args.action == 'prepare':
            write_new(Path(args.output), canonical({'version': 1, 'scenarios': SCENARIOS}))
            result = {'status': 'PREPARED', 'live': 'NOT_RUN'}
        elif args.action == 'evaluate':
            path = Path(args.evidence)
            result = evaluate_record(json.loads(path.read_text()), path.parent)
        else:
            if not args.execute:
                raise ValueError('execute_flag_required')
            config = private_json(args.config)
            destination = Path(args.evidence_dir).absolute()
            if any(p.is_symlink() for p in (destination, *destination.parents)):
                raise ValueError('unsafe_evidence_directory')
            destination.mkdir(mode=0o700, parents=False, exist_ok=False)
            records = asyncio.run(run(config, destination, args.case))
            result = {'status': 'COLLECTED', 'cases': [evaluate_record(r, destination) for r in records]}
        print(json.dumps(result, ensure_ascii=False))
        return 0 if result['status'] in {'PASS','PREPARED','COLLECTED'} else 1
    except Exception:
        print(json.dumps({'status': 'NOT_RUN', 'error': 'probe_configuration_or_evidence_invalid'}))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
