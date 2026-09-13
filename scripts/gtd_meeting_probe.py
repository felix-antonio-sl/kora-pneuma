#!/usr/bin/env python3
"""Opt-in native meeting trial. Default describes preparation and runs nothing.

Owner fixture inputs are distinct from principal operations. Source revisions
are ingested only while the owned service is stopped and its writer lock held.
Mechanical success remains REVIEW_REQUIRED for human assessment of the writing.
"""
import argparse
import asyncio
import base64
from email import policy
from email.parser import BytesParser
from email.utils import getaddresses
import hashlib
import json
import os
from pathlib import Path
import sys
import time
import uuid
import gtd_product_trial as trial

A = trial.acceptance
PACKAGE = '/home/felix/.local/state/gtd-felix/p3-product/meeting-materials-okz2gf7p'
EXPECTED = {1: '3ee7bf9216445a7d3077021de5c91078ee1e7ded09aced6f82a636d2593a1c40',
            2: '05ca475773664d507bb459226e0f6902f193cf4601917fd0b90d731ca24478f2'}
MIME = 'application/vnd.openxmlformats-officedocument.presentationml.presentation'


def preflight(config, service):
    trial.require(config.get('meeting', {}).get('package') == PACKAGE, 'explicit_accepted_package_required')
    root = Path(config['runtime_root'])
    manifest = json.loads(trial.private_bytes(config['meeting']['runtime_manifest']))
    files = manifest.get('files', {})
    trial.require(files and all((root / name).is_relative_to(root) and '..' not in Path(name).parts
        and not (root / name).is_symlink() and A.sha((root / name).read_bytes()) == digest for name, digest in files.items()), 'reviewed_runtime_hash_mismatch')
    for name in ('gtd_felix/gtd.py', 'gtd_felix/application.py', 'gtd_felix/mcp.py', 'gtd_felix/hermes.py'):
        trial.require(name in files, 'runtime_manifest_incomplete')
    skill_root = root.parent
    for relative in ('SKILL.md', 'references/operations.md'):
        path = skill_root / relative
        trial.require(path.is_file() and not path.is_symlink(), 'native_realization_required')
        content = path.read_text()
        trial.require(not any(word in content for word in ('references/acceptance.md', 'gtd_meeting_probe', 'test_meeting_probe')), 'oracle_exposed_to_native_instructions')
    for gateway in config['gateways']:
        workspace = Path(gateway['workspace'])
        trial.require(not Path(__file__).resolve().is_relative_to(workspace), 'oracle_in_native_workspace')
    for phase in (1, 2):
        trial.require(A.sha((Path(PACKAGE) / f'v{phase}/taller.pptx').read_bytes()) == EXPECTED[phase], 'accepted_collateral_changed')
    budget, reservation = service['budget'], service['orchestration']['reservation']
    trial.require(budget['max_cost_usd'] == 8 and budget['recovery_cost_usd'] == 2
        and budget.get('max_active') == 1 and reservation['max_cost_usd'] == 3
        and reservation['max_runtime_seconds'] == 240 and budget['max_job_runtime_seconds'] == 240
        and budget['max_runtime_seconds'] - budget['recovery_runtime_seconds'] == 480
        and budget['max_retries'] == reservation['max_retries'] == 0
        and budget['max_descendants'] == reservation['max_descendants'] == 0, 'meeting_budget_mismatch')
    trial.require(service['orchestration'].get('timezone') == 'America/Santiago', 'daily_timezone_mismatch')
    trial.require(not any(service.get(k) for k in ('source_monitor', 'external_effects', 'google_sources', 'telegram')), 'external_connections_forbidden')
    trial.require(len(service.get('bots', [])) == 1 and service['bots'][0].get('state') == 'available', 'single_verified_bootstrap_bot_required')
    return {'status': 'PREPARED', 'native_execution': 'NOT_RUN', 'phases': 2, 'reservation_usd': 6, 'recovery_usd': 2}


def apply_fixture(config, service_config, destination, phase):
    """Subprocess only, with stopped service and exclusive product writer lock."""
    sys.path.insert(0, config['runtime_root'])
    from gtd_felix.application import writer_lock
    from gtd_felix.service import GTDService
    from gtd_felix.source_sync import SourceSync
    from gtd_felix.control import ExecutionControl
    destination = Path(destination)
    owner = service_config['actors']['owner']
    with writer_lock(service_config['data_dir']):
        service = GTDService(Path(service_config['data_dir']), owner_actor=owner,
            principal_actor=service_config['actors']['principal'],
            executor_actors=service_config['actors'].get('executors', []))
        try:
            trial.require(not ExecutionControl(service, service_config['budget']).pending(), 'fixture_requires_quiescence')
            record_path = destination / 'fixture-identities.json'
            ids = json.loads(record_path.read_text()) if phase == 2 else {}
            if phase == 1:
                trial.require(not service.query(), 'fixture_requires_empty_items')
                raw = (Path(PACKAGE) / 'sources/owner-position-r1.json').read_bytes()
                position = service.capture(owner, 'meeting-fixture:position', json.loads(raw)['text'],
                    source={'kind': 'explicit_owner_fixture'}, original=raw, filename='owner-position.json', mime_type='application/json')['item']
                ids['position'] = position['id']
            partition = {'provider': 'authenticated-fixture', 'account': 'meeting@example.invalid', 'collection': 'invitations', 'scope_digest': 'a' * 64}
            sync = SourceSync(service)
            raw = (Path(PACKAGE) / f'sources/invitation-r{phase}.json').read_bytes()
            cycle = 'meeting-fixture:r' + str(phase)
            sync.begin(partition, cycle, 'full' if phase == 1 else 'incremental')
            result = sync.apply_page(partition, cycle, {'page_id': cycle, 'request_token': None, 'next_page_token': None,
                'cursor': str(phase), 'objects': [{'external_id': 'meeting', 'revision': str(phase), 'status': 'present',
                'text': raw.decode(), 'original': raw, 'sha256': A.sha(raw), 'url': 'https://fixture.invalid/meeting', 'mime_type': 'application/json'}]})
            source = service.get_item(result['objects']['meeting']['item_id'])
            if phase == 1:
                ids['source'] = source['id']
                fields = {'kind': 'project', 'commitment': 'committed', 'title': 'Preparación privada del taller comunitario',
                    'outcome': 'Paquete preparatorio privado recuperable',
                    'completion_criteria': 'Preparación comprobada sin dar por confirmada la sala ni adoptar acuerdos o asistencia',
                    'source_versions': {ids['position']: 1}, 'decision_needed': True, 'decision_question': 'Sala pendiente; decisión humana aún no tomada.',
                    'notes': 'Prepara una única preparación privada derivada: selecciona y asocia el PPTX aportado como colateral, escribe una minuta lean y un borrador RFC822 nuevo desde lo conocido (cuentas y Message-ID example.invalid; no enviar). Preserva las fuentes y mi posición. Necesito 20 minutos de lectura y decisión antes del comienzo: registra cuándo volver a ello. Si cambia la invitación, actualiza la misma preparación y sus materiales, manteniendo la historia. No generes otra presentación ni cierres mi decisión de sala.'}
                response = service.execute(owner, {'operation_id': 'meeting-fixture:owner-scope', 'action': 'clarify', 'item_id': source['id'], 'expected_version': source['version'], 'fields': fields})
                trial.require(response['status'] == 'applied', 'owner_fixture_failed')
                source = response['item']
            trial.require(source['id'] == ids['source'], 'source_identity_changed')
            payload = (Path(PACKAGE) / f'v{phase}/taller.pptx').read_bytes()
            fields = {'content_base64': base64.b64encode(payload).decode(), 'filename': 'taller.pptx', 'mime_type': MIME,
                'title': 'Colateral aportado por dueño · invitación r' + str(phase), 'source_versions': {source['id']: phase, ids['position']: 1}}
            if phase == 2:
                fields['material_id'] = ids['collateral']
            result = service.execute(owner, {'operation_id': cycle + ':owner-collateral', 'action': 'put_material',
                'item_id': source['id'], 'expected_version': source['version'], 'fields': fields})
            trial.require(result['status'] == 'applied', 'owner_collateral_failed')
            ids['collateral'] = result['item']['materials'][-1]['id']
            # These are fully specified fixture references, not a principal act.
            for event in service.pending_events('gtd-review', 'local'):
                if event['payload'].get('item_id') == ids['position']:
                    service.mark_event(event['event_key'], 'ignored', 'owner_fixture_reference_only')
            if phase == 1:
                A.write_new(record_path, A.canonical(ids))
            service.export(destination / f'fixture-r{phase}.zip')
            return {'phase': phase, 'actor': owner, 'kind': 'owner_fixture_not_principal', 'ids': ids,
                    'invitation_sha256': A.sha(raw), 'collateral_sha256': A.sha(payload), 'revision': phase}
        finally:
            service.close()


def evaluate(snapshot, fixture, phase, first=None, observations=None):
    """Mechanical gate only; writing quality always requires independent review."""
    items = snapshot['items']; ids = fixture['ids']; source = items.get(ids['source'], {})
    principal = snapshot['metadata'].get('actor_config', {}).get('principal_actor', 'gtd-felix')
    jobs = list(snapshot['metadata'].get('execution:state', {}).get('jobs', {}).values())
    native = [j for j in jobs if j.get('actor') == principal and (j.get('native') or {}).get('provider') == 'hermes'
        and j.get('terminal') and j.get('integration') == 'integrated'
        and j.get('observations') and j['observations'][-1].get('native_identity') == j['native']
        and j['observations'][-1].get('native_status') == 'completed']
    def witnessed(job):
        observation = job['observations'][-1]
        stored = snapshot['metadata'].get(observation.get('evidence_reference'), {})
        digest = A.sha(json.dumps(stored.get('payload'), ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode())
        route = snapshot['metadata'].get('hermes:intent:' + job['id'], {}).get('route', {})
        return (observation.get('evidence_reference') == 'hermes:observation:' + job['id'] + ':' + digest
            and stored.get('observation', {}).get('native_identity') == job['native']
            and stored.get('observation', {}).get('native_status') == 'completed'
            and route.get('model') == 'gpt-6-astra' and route.get('reasoning_effort') == 'low')
    native = [j for j in native if witnessed(j)]
    verified = {p['operation_id'] for j in native for p in j.get('progress', [])}
    authenticated = [o for o in snapshot['operations'] if o['actor'] == principal and o['operation_id'] in verified and o['receipt'].get('status') == 'applied']
    children = [i for i in items.values() if i.get('parent_id') == ids['source'] and i.get('created_by') == principal]
    check = {'principal_native_terminal': len(native) == phase, 'native_authenticated_progress': bool(authenticated),
             'one_preparation': len(children) == 1, 'source_revision': len(source.get('source_revisions', [])) == phase,
             'human_room_decision_preserved': source.get('decision_needed') is True and source.get('decision_question') == 'Sala pendiente; decisión humana aún no tomada.'}
    child = children[0] if len(children) == 1 else {}
    latest = {m['id']: m for m in child.get('materials', [])}
    pp = [m for m in latest.values() if m.get('source_material', {}).get('material_id') == ids['collateral']
          and m['source_material'].get('version') == phase and m['source_material'].get('sha256') == EXPECTED[phase]
          and m['original']['sha256'] == EXPECTED[phase] and m.get('author') == principal]
    check['principal_pptx_copy'] = len(pp) == 1 and snapshot['files'].get(pp[0]['original']['path']) is not None and A.sha(snapshot['files'][pp[0]['original']['path']]) == EXPECTED[phase]
    check['current_dependencies'] = child.get('source_versions') == {ids['source']: phase, ids['position']: 1}
    text_materials = [(m, text) for m, text in A.material_content(snapshot, child) if m.get('author') == principal and not m.get('source_material')]
    minutes = [(m, t) for m, t in text_materials if m['original'].get('mime_type', '').startswith(('text/plain','text/markdown')) and len(t.strip()) >= 120]
    drafts = [(m, t) for m, t in text_materials if m['original'].get('mime_type') == 'message/rfc822']
    check['material_operations_authenticated'] = all(any(m in o['receipt'].get('item', {}).get('materials', []) for o in authenticated) for m in latest.values())
    observed = {m['id']: m for m in (observations or []) if m.get('version') == latest.get(m['id'], {}).get('version')}
    check['latest_materials_observed_valid'] = bool(latest) and all(observed.get(m['id'], {}).get('valid') is True and observed[m['id']].get('original') == m['original'] for m in latest.values())
    check['principal_minutes'] = len(minutes) == 1
    check['principal_draft'] = len(drafts) == 1
    if drafts:
        message = BytesParser(policy=policy.default).parsebytes(drafts[0][1].encode())
        addresses = getaddresses(message.get_all('From', []) + message.get_all('To', []))
        check['draft_private_addresses'] = len(addresses) >= 2 and all(a.endswith('@example.invalid') for _, a in addresses) and str(message.get('Message-ID','')).endswith('@example.invalid>')
    review = snapshot['metadata'].get('last_review', {})
    check['return_recorded'] = review.get('actor') == principal and review.get('return_at') == f"2026-09-12T09:{'40' if phase == 1 else '10'}:00+02:00"
    check['review_authenticated'] = any(o['receipt'].get('review') == review for o in authenticated)
    check['human_position_preserved'] = items.get(ids['position'], {}).get('text') == 'Máximo 12 personas, 2 facilitadores, no ampliar sin decisión, nada de ventas, sala pendiente.'
    mapping = {'preparation': child.get('id'), 'pptx': pp[0]['id'] if pp else None,
               'minutes': minutes[0][0]['id'] if minutes else None, 'draft': drafts[0][0]['id'] if drafts else None}
    if first:
        check['same_identities'] = mapping == first['identities']
        check['new_native_job'] = set(j['id'] for j in native) > set(first['native_jobs'])
        check['r1_materials_observed_invalid'] = all(any(m['id'] == identity and m['version'] == 1 and m.get('valid') is False for m in (observations or [])) for key, identity in mapping.items() if key != 'preparation')
        check['r1_materials_preserved'] = all(any(m['id'] == identity and m['version'] == 1 for m in child.get('materials', [])) for key, identity in mapping.items() if key != 'preparation')
    return {'status': 'REVIEW_REQUIRED' if all(check.values()) else 'FAIL', 'mechanical_checks': check,
            'identities': mapping, 'native_jobs': [j['id'] for j in native],
            'manual_review': ['Minuta and RFC822 body reflect the current invitation and restrictions without fabricated confirmation.',
                              'PPTX selection is reuse of owner collateral, not native generation.']}


class MeetingDriver(A.ProductDriver):
    supervisor = None
    async def fixture(self, phase):
        trial.require(not await self.request('POST', '/v1/control/pending', {}), 'fixture_requires_quiescence')
        stopped = await self.supervisor.service.stop(10)
        trial.require(stopped.get('pid_absent') and stopped.get('returncode') is not None, 'fixture_service_stop_unconfirmed')
        cfg = self.supervisor.config
        owned = trial.OwnedProcess('owner-fixture-r' + str(phase), [cfg['python'], '-E', '-s', '-B', str(Path(__file__).resolve()),
            '--execute', '--fixture-phase', str(phase), '--config', cfg['_meeting_config_path'], '--evidence-dir', str(self.destination)],
            trial.clean_environment(self.destination), str(Path(__file__).parent), log_dir=self.destination)
        self.supervisor.processes.append(owned)
        await owned.start()
        try:
            await asyncio.wait_for(owned.process.wait(), 20)
        finally:
            await owned.stop(5)
        trial.require(owned.process.returncode == 0, 'fixture_process_failed')
        await self.supervisor.start_service()
        return json.loads((self.destination / f'owner-fixture-r{phase}.json').read_text())

    async def run_case(self, case_id, **unused):
        record = {'run_id': uuid.uuid4().hex, 'case': 'MEETING', 'phases': [], 'status': 'PARTIAL'}
        first = None
        for phase in (1, 2):
            phase_record = {'run_id': record['run_id'] + ':' + str(phase)}
            # Empty initial inventory permits verified bootstrap; suspend before
            # introducing any fixture events, and again before revision two.
            bots = await self.request('POST', '/v1/control/bots', {})
            trial.require(len(bots) == 1 and bots[0].get('state') == 'available' and bots[0].get('probe_evidence'), 'verified_single_bot_required')
            self.prepared_bots = [{**bots[0], 'state': 'available'}]
            suspended = await self.request('POST', '/v1/control/register_bot', {'operation_id': phase_record['run_id'] + ':suspend', 'bot': {**bots[0], 'state': 'suspended'}})
            trial.require(suspended.get('status') == 'applied', 'meeting_suspension_rejected')
            fixture = await self.fixture(phase)
            # Fixture subprocess completes both inputs before any resume.
            await self.enable_case(phase_record)
            phase_deadline = min(self.started + self.config['timeout_seconds'], time.monotonic() + 270)
            evaluation = None
            while time.monotonic() < phase_deadline:
                pending = await self.request('POST', '/v1/control/pending', {})
                if not pending:
                    name = f"phase-{phase}-{uuid.uuid4().hex}.zip"
                    exported = await self.snapshot(name)
                    snapshot = A.load_snapshot(self.destination / name, exported['sha256'])
                    descendants = [i for i in snapshot['items'].values() if i.get('parent_id') == fixture['ids']['source']]
                    observations = await self.request('GET', '/v1/materials/' + descendants[0]['id']) if len(descendants) == 1 else []
                    evaluation = evaluate(snapshot, fixture, phase, first, observations)
                    if evaluation['mechanical_checks'].get('principal_pptx_copy'):
                        mid = evaluation['identities']['pptx']
                        original = await self.request('GET', f"/v1/material-files/{descendants[0]['id']}/{mid}/{phase}", binary=True)
                        if A.sha(original) != EXPECTED[phase]:
                            evaluation['status'] = 'FAIL'; evaluation['mechanical_checks']['pptx_http_hash'] = False
                        else:
                            evaluation['mechanical_checks']['pptx_http_hash'] = True
                    if evaluation['status'] == 'REVIEW_REQUIRED':
                        break
                    jobs = snapshot['metadata'].get('execution:state', {}).get('jobs', {})
                    if len(jobs) >= phase:
                        break  # Terminal text/insufficient material is not success.
                await asyncio.sleep(self.config['poll_interval_seconds'])
            trial.require(evaluation is not None, 'phase_timeout')
            record['phases'].append({'fixture': fixture, 'evaluation': evaluation, 'export': exported})
            A.write_new(self.destination / f'phase-{phase}-evaluation.json', A.canonical(record['phases'][-1]))
            if evaluation['status'] != 'REVIEW_REQUIRED':
                break
            first = first or evaluation
        record['status'] = 'REVIEW_REQUIRED' if len(record['phases']) == 2 and all(p['evaluation']['status'] == 'REVIEW_REQUIRED' for p in record['phases']) else 'FAIL'
        A.write_new(self.destination / (record['run_id'] + '-evidence.json'), A.canonical(record))
        return record


def description():
    return {'status': 'NOT_RUN', 'execute_required': True, 'package': PACKAGE,
        'config_contract': 'Existing gtd_product_trial config plus meeting {package, runtime_manifest}; exact reviewed realized runtime, one verified principal bot (suspended before fixture), America/Santiago daily timezone.',
        'budget': {'max_cost_usd': 8, 'recovery_cost_usd': 2, 'max_active': 1, 'phase_cost_usd': 3,
                   'phase_runtime_seconds': 240, 'principal_runtime_seconds': 480, 'max_retries': 0, 'max_descendants': 0},
        'limits': ['No native calls during description.', 'R2 is introduced while owned service is stopped, not live Google detection.', 'Mechanical acceptance requires independent writing review.']}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--execute', action='store_true'); parser.add_argument('--config'); parser.add_argument('--evidence-dir')
    parser.add_argument('--fixture-phase', type=int, choices=(1,2), help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    if not args.execute:
        print(json.dumps(description(), ensure_ascii=False)); return 0
    try:
        if args.fixture_phase:
            config = json.loads(trial.private_bytes(args.config))
            service = json.loads(trial.private_bytes(config['service_config']))
            result = apply_fixture(config, service, args.evidence_dir, args.fixture_phase)
            A.write_new(Path(args.evidence_dir) / f'owner-fixture-r{args.fixture_phase}.json', A.canonical(result))
            return 0
        config, service, env = trial.load_config(args.config)
        config['_meeting_config_path'] = str(Path(args.config).absolute())
        preflight(config, service)
        destination = trial.absolute_path(args.evidence_dir); destination.mkdir(mode=0o700, exist_ok=False)
        supervisor = trial.Supervisor(config, service, env, destination)
        MeetingDriver.supervisor = supervisor
        original_driver, original_evaluate = A.ProductDriver, A.evaluate_record
        A.ProductDriver = MeetingDriver; A.SCENARIOS['MEETING'] = {}
        A.evaluate_record = lambda record, _: {'status': record['status'], 'phases': record['phases']}
        try:
            receipt = asyncio.run(supervisor.run('MEETING'))
        finally:
            A.ProductDriver = original_driver; A.evaluate_record = original_evaluate; A.SCENARIOS.pop('MEETING', None)
        print(json.dumps({'status': receipt['status'], 'receipt': str(destination / 'trial-receipt.json')}))
        closed = bool(receipt.get('processes')) and all(p.get('status') == 'STOPPED'
            and p.get('pid_absent') is True and p.get('returncode') is not None for p in receipt['processes'])
        clean = not any(receipt.get(key) for key in ('error', 'admission_close_error', 'job_stop_error', 'unresolved_jobs'))
        return 0 if receipt.get('case', {}).get('status') == 'REVIEW_REQUIRED' and closed and clean else 1
    except Exception as error:
        print(json.dumps({'status': 'BLOCKED', 'error': str(error) if isinstance(error, trial.TrialError) else type(error).__name__}))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
