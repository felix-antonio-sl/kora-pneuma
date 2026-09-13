"""Authenticated local transport; only the serving process opens the store."""
import asyncio
from contextlib import contextmanager
import fcntl
import hmac
import ipaddress
import json
import os
from pathlib import Path
import stat
import tempfile

from aiohttp import web

from .store import private_dir

ACTOR = web.RequestKey('actor', str)

CONTROL = {
    'transition_budget_policy': ('actor', 'operation_id', 'expected_hash'),
    'register_bot': ('actor', 'operation_id', 'bot'), 'bots': (),
    'reserve': ('actor', 'operation_id', 'request'), 'pending': (),
    'get_job': ('job_id',), 'request_stop': ('actor', 'operation_id', 'job_id'),
    'accept_result': ('actor', 'operation_id', 'job_id', 'result'), 'budget': (),
    'reconcile': ('actor', 'operation_id', 'observations'),
    'validate': ('job_id', 'capability'),
}


SOURCE_MONITOR = web.AppKey('source_monitor', object)
EFFECT_MONITOR = web.AppKey('effect_monitor', object)
EFFECT_CONTROL = {
    'propose_effect': {'operation_id', 'proposal'},
    'authorize_effect': {'operation_id', 'effect_id', 'expected_proposal_hash'},
    'grant_draft_preparation': {'operation_id', 'account', 'grantee', 'expires_at'},
    'revoke_effect': {'operation_id'},
}


def read_private(path):
    path = Path(path).absolute()
    if any(p.is_symlink() for p in (path, *path.parents)):
        raise ValueError('unsafe_private_file')
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(fd, 'rb') as stream:
        info = os.fstat(stream.fileno())
        if (not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid()
                or stat.S_IMODE(info.st_mode) != 0o600 or info.st_nlink != 1):
            raise ValueError('unsafe_private_file')
        data = stream.read(1024 * 1024 + 1)
        if len(data) > 1024 * 1024:
            raise ValueError('private_file_too_large')
        return data


def validate_config(config):
    if not isinstance(config, dict):
        raise ValueError('invalid_configuration')
    host = config.get('listen_host', '127.0.0.1')
    if not ipaddress.ip_address(host).is_loopback:
        raise ValueError('local_bind_required')
    port = config.get('port', 8765)
    if type(port) is not int or not 0 <= port <= 65535:
        raise ValueError('invalid_port')
    actors = config.get('actors', {})
    owner, principal = actors.get('owner'), actors.get('principal')
    executors = actors.get('executors', [])
    if not isinstance(executors, list):
        raise ValueError('invalid_actors')
    identities = [owner, principal, *executors]
    if any(not isinstance(a, str) or not a for a in identities) or len(set(identities)) != len(identities):
        raise ValueError('invalid_actors')
    tokens = config.get('api_tokens')
    if not isinstance(tokens, dict) or not tokens or any(
            not isinstance(t, str) or len(t) < 16 or a not in identities for t, a in tokens.items()):
        raise ValueError('invalid_api_tokens')
    if not isinstance(config.get('data_dir'), str) or not Path(config['data_dir']).is_absolute():
        raise ValueError('absolute_data_dir_required')
    limit = config.get('body_limit', 6 * 1024 * 1024)
    if type(limit) is not int or not 1024 <= limit <= 20 * 1024 * 1024:
        raise ValueError('invalid_body_limit')
    if 'google' in config:
        from .source_monitor import validate_google
        validate_google(config['google'])
    if 'external_effects' in config:
        from .effect_monitor import validate_effects
        accounts = {entry['transport']['account'] for entry in config.get('google', {}).get('accounts', {}).values()}
        validate_effects(config['external_effects'], accounts)
    return config


def load_config(path):
    return validate_config(json.loads(read_private(path)))


@contextmanager
def writer_lock(data_dir):
    root = private_dir(data_dir)
    fd = os.open(root / 'writer.lock', os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or info.st_nlink != 1:
            raise ValueError('unsafe_writer_lock')
        os.fchmod(fd, 0o600)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise ValueError('writer_already_running') from None
        yield
    finally:
        os.close(fd)


def create_app(service, control, config):
    """Caller holds writer_lock for the entire service lifetime, before opening DB."""
    validate_config(config)
    from .source_monitor import SourceMonitor, retire_sources
    monitor = SourceMonitor(service, config['google']) if 'google' in config else None
    if monitor is None:
        retire_sources(service)
    from .effects import ExternalEffects
    from .effect_monitor import EffectMonitor
    effects = ExternalEffects(service)
    effect_worker = EffectMonitor(service, effects, monitor, config.get('external_effects'))
    from .source_evaluation import SourceEvaluation
    selection = SourceEvaluation(service, control, monitor, config)
    tokens = dict(config['api_tokens'])

    @web.middleware
    async def boundary(request, handler):
        try:
            if request.path != '/health':
                authorization = request.headers.get('Authorization', '')
                token = authorization[7:] if authorization.startswith('Bearer ') else ''
                actor = next((a for t, a in tokens.items() if hmac.compare_digest(t.encode(), token.encode())), None)
                if actor is None or service.actor_role(actor) not in {'owner', 'principal', 'executor'}:
                    return web.json_response({'status': 'rejected', 'error': 'unauthorized'}, status=401)
                request[ACTOR] = actor
            return await handler(request)
        except web.HTTPException as exc:
            return web.json_response({'status': 'rejected', 'error': 'body_too_large' if exc.status == 413 else 'request_rejected'}, status=exc.status)
        except (ValueError, TypeError, KeyError):
            return web.json_response({'status': 'rejected', 'error': 'invalid_request'}, status=400)
        except Exception:
            return web.json_response({'status': 'uncertain', 'error': 'service_unavailable'}, status=503)

    app = web.Application(middlewares=[boundary], client_max_size=config.get('body_limit', 6 * 1024 * 1024))

    async def body(request):
        value = await request.json()
        if not isinstance(value, dict):
            raise ValueError('object_required')
        return {k: v for k, v in value.items() if k != 'actor'}

    async def health(request):
        return web.json_response({'status': 'ok'})

    def readable(request, item):
        actor = request[ACTOR]
        if item is None:
            return False
        if service.actor_role(actor) != 'executor':
            return True
        job_id = request.headers.get('X-GTD-Job-ID')
        job = control.get_job(job_id)
        if not job:
            return False
        return control.validate_target(job_id, actor, item['id'], job['capability'])['allowed']

    async def source_evaluation(request):
        value = await body(request)
        if request.match_info['operation'] == 'validate':
            return web.json_response(selection.validate(request[ACTOR], value))
        if request.match_info['operation'] != 'run' or set(value) != {'source_id'}:
            raise ValueError('invalid_source_evaluation_request')
        alive = lambda: request.transport is not None and not request.transport.is_closing()
        result = await selection.run(request[ACTOR], request.headers.get('X-GTD-Job-ID'),
            value['source_id'], alive=alive)
        return web.json_response(result)

    async def capabilities(request):
        role = service.actor_role(request[ACTOR])
        operations = ['query', 'command', 'get', 'materials']
        if role != 'executor':
            operations.extend(['review', 'choose', 'source_coverage', 'effects'])
        if role == 'owner':
            operations.extend(['capture', 'export'])
        controls = ([] if role == 'executor' else list(CONTROL) if role == 'owner' else ['bots', 'pending', 'get_job', 'budget', 'validate'])
        if role != 'executor':
            controls.extend(list(EFFECT_CONTROL) if role == 'owner' else ['propose_effect'])
        return web.json_response({'version': 1, 'actor': request[ACTOR],
            'role': role, 'control': controls, 'operations': operations})

    async def items(request):
        filters = json.loads(request.query.get('filters', '{}'))
        if not isinstance(filters, dict):
            raise ValueError('object_required')
        return web.json_response([item for item in service.query(filters) if readable(request, item)])

    async def item(request):
        result = service.describe_item(request.match_info['item_id'])
        if not readable(request, result):
            result = None
        return web.json_response(result if result else {'status': 'rejected', 'error': 'item_not_found'}, status=200 if result else 404)

    async def source_attachment(request):
        from .source_attachments import read_attachment
        actor = request[ACTOR]
        role = service.actor_role(actor)
        job_id = request.headers.get('X-GTD-Job-ID', '')
        def active():
            if role == 'owner':
                return True
            job = control.get_job(job_id) if role == 'principal' else None
            return bool(job and job['actor'] == actor and job['capability'] == 'prepare_private'
                        and control.validate(job_id, 'prepare_private')['allowed'])
        if not active():
            return web.json_response({'status':'rejected','error':'active_principal_job_required'}, status=403)
        allowed = {'attachment_index', 'sheet_index', 'row_offset', 'row_limit'}
        if set(request.query) - allowed or any(len(request.query.getall(k)) != 1 for k in request.query):
            raise ValueError('invalid_attachment_arguments')
        values = {k:int(v) for k,v in request.query.items()}
        version = int(request.match_info['version'])
        item = service.get_item(request.match_info['item_id'])
        if not item or not readable(request, item):
            return web.json_response({'status':'rejected','error':'item_not_found'}, status=404)
        try:
            result = await asyncio.to_thread(read_attachment, service.store, item, version, **values)
        except Exception as exc:
            codes = {'source_version_changed','selected_gmail_source_required','invalid_attachment_arguments',
                'source_original_mismatch','attachment_not_found','attachment_format_unsupported',
                'attachment_size_limit','attachment_archive_limit','attachment_xml_unsupported',
                'attachment_sheet_not_found','attachment_sheet_unsupported','attachment_row_not_found',
                'attachment_cell_invalid','attachment_string_invalid','attachment_mime_invalid',
                'attachment_sheet_invalid','attachment_row_invalid'}
            code = exc.args[0] if type(exc) is ValueError and len(exc.args) == 1 and type(exc.args[0]) is str else None
            return web.json_response({'status':'rejected','error':code if code in codes else 'attachment_parse_failed'}, status=409)
        current = service.get_item(item['id'])
        if not active() or request.transport is None or request.transport.is_closing():
            return web.json_response({'status':'rejected','error':'attachment_read_cancelled'}, status=409)
        if not current or current['version'] != version:
            return web.json_response({'status':'rejected','error':'source_version_changed'}, status=409)
        return web.json_response(result)

    async def capture(request):
        values = await body(request)
        if service.actor_role(request[ACTOR]) != 'owner':
            return web.json_response({'status': 'rejected', 'error': 'owner_capture_required'}, status=403)
        if set(values) - {'operation_id', 'text', 'source'}:
            raise ValueError('unsupported_capture_fields')
        return web.json_response(service.capture(request[ACTOR], **values))

    async def command(request):
        values = await body(request)
        actor = request[ACTOR]
        if values.get('action') == 'apply_human_instruction' and service.actor_role(actor) != 'principal':
            return web.json_response({'status': 'rejected', 'error': 'principal_required'}, status=403)
        if service.actor_role(actor) == 'owner':
            return web.json_response(service.execute(actor, values))
        job_id = request.headers.get('X-GTD-Job-ID', '')
        action = values.get('action')
        instruction_source = None
        if action == 'apply_human_instruction':
            fields = values.get('fields')
            basis = fields.get('intent_basis') if isinstance(fields, dict) else None
            if not isinstance(basis, dict) or not isinstance(basis.get('source_item_id'), str):
                return web.json_response({'status': 'rejected', 'error': 'invalid_human_instruction'}, status=400)
            instruction_source = basis['source_item_id']
        if action == 'clarify' and values.get('fields', {}).get('capability') == 'prepare_private':
            basis = values['fields'].get('intent_basis')
            if isinstance(basis, dict) and basis.get('source_item_id') != values.get('item_id'):
                instruction_source = basis.get('source_item_id')
        if action not in {'clarify', 'derive', 'plan', 'put_material', 'assess_result', 'review', 'edit', 'apply_human_instruction'}:
            return web.json_response({'status': 'rejected', 'error': 'agent_action_not_enabled'}, status=403)
        job = control.get_job(job_id)
        if not job or job['actor'] != actor:
            return web.json_response({'status': 'rejected', 'error': 'job_required'}, status=403)
        target = values.get('item_id', job['item_id'])
        if instruction_source is not None and target != job['item_id']:
            return web.json_response({'status': 'rejected', 'error': 'outside_job_scope'}, status=409)
        capability = 'local_work' if action == 'edit' else 'prepare_private'
        if action == 'derive':
            capability = values.get('fields', {}).get('capability', 'local_work')
        # No await between guard, mutation and progress acknowledgement: Store's
        # reentrant lock also excludes human changes from another local thread.
        with service.store.lock:
            if action == 'assess_result':
                target_item = service.get_item(target)
                capability = target_item.get('work_capability', 'local_work') if target_item else 'local_work'
            existing = service.store.db.execute('SELECT actor,receipt FROM operations WHERE operation_id=?', (values.get('operation_id'),)).fetchone()
            if existing and existing['actor'] == actor:
                saved = json.loads(existing['receipt'])
                saved_item = saved.get('item', {})
                scope = job.get('item_bases', {})
                if (saved_item.get('id') in scope or saved_item.get('parent_id') in scope
                        or saved.get('review') and action == 'review'):
                    replay = service.execute(actor, values)
                    if replay.get('status') == 'already_applied':
                        progress = control.record_progress(job_id, saved, values.get('expected_version', job['expected_version']))
                        if progress['status'] != 'recorded':
                            return web.json_response({'status': 'uncertain', 'error': 'progress_not_recorded'}, status=409)
                    return web.json_response(replay)
            valid = control.validate_target(job_id, actor, target, capability, require_descendants=action == 'assess_result',
                require_source_snapshot=action == 'plan' and 'source_versions' in values.get('fields', {}),
                human_instruction_source=instruction_source)
            if not valid['allowed']:
                return web.json_response({'status': 'rejected', 'error': valid['reason']}, status=409)
            if action == 'put_material' and 'source_material' in values.get('fields', {}):
                reference = values['fields']['source_material']
                source_id = reference.get('item_id') if isinstance(reference, dict) else None
                source_guard = control.validate_target(job_id, actor, source_id, 'prepare_private')
                if not source_guard['allowed']:
                    return web.json_response({'status': 'rejected', 'error': source_guard['reason']}, status=409)
            previous = valid['current_version']
            if action != 'review' and values.get('expected_version') != previous:
                return web.json_response({'status': 'conflict', 'error': 'expected_version_mismatch', 'current_version': previous}, status=409)
            receipt = service.execute(actor, values)
            if receipt.get('status') == 'applied':
                progress = control.record_progress(job_id, receipt, previous)
                if progress['status'] != 'recorded':
                    return web.json_response({'status': 'uncertain', 'error': 'progress_not_recorded', 'operation_id': values.get('operation_id')}, status=409)
            return web.json_response(receipt)

    async def dispatch(request):
        values = await body(request)
        actor = request[ACTOR]
        job_id = request.headers.get('X-GTD-Job-ID', '')
        if service.actor_role(actor) != 'principal':
            return web.json_response({'status': 'rejected', 'error': 'principal_required'}, status=403)
        parent = control.get_job(job_id)
        if not parent or set(values) != {'operation_id', 'request'}:
            return web.json_response({'status': 'rejected', 'error': 'job_required'}, status=403)
        native_request = values['request']
        with service.store.lock:
            valid = control.validate_target(job_id, actor, native_request.get('item_id'), native_request.get('capability'))
            if not valid['allowed']:
                return web.json_response({'status': 'rejected', 'error': valid['reason']}, status=409)
            native_request = {**native_request, 'parent_job_id': job_id, 'defer_when_busy': True, 'orchestrated': True}
            receipt = control.reserve(actor, values['operation_id'], native_request)
            if receipt.get('status') == 'reserved':
                service.ingest_event({'provider': 'gtd-dispatch', 'account': 'local',
                    'external_id': receipt['job_id'], 'revision': '1',
                    'payload': {'job_id': receipt['job_id'], 'parent_job_id': job_id}})
            return web.json_response(receipt)

    async def choose(request):
        if service.actor_role(request[ACTOR]) == 'executor':
            return web.json_response({'status': 'rejected', 'error': 'forbidden'}, status=403)
        return web.json_response(service.choose(json.loads(request.query.get('context', '{}'))))

    async def job_history(request):
        if set(request.query) - {'item_id'}:
            raise ValueError('invalid_history_fields')
        actor = request[ACTOR]
        caller = request.headers.get('X-GTD-Job-ID')
        if service.actor_role(actor) == 'owner' and not caller and not request.query:
            return web.json_response(control.pending())  # Existing owner view.
        result = control.job_history(actor, caller, request.query.get('item_id'))
        return web.json_response(result, status=403 if isinstance(result, dict) else 200)

    async def control_call(request):
        operation = request.match_info['operation']
        if operation not in CONTROL:
            raise web.HTTPNotFound()
        role = service.actor_role(request[ACTOR])
        if role == 'executor' or (operation not in {'bots', 'pending', 'get_job', 'budget', 'validate'} and role != 'owner'):
            return web.json_response({'status': 'rejected', 'error': 'forbidden'}, status=403)
        values = await body(request)
        names = CONTROL[operation]
        if set(values) != set(names) - {'actor'}:
            raise ValueError('invalid_control_fields')
        args = [request[ACTOR] if name == 'actor' else values[name] for name in names]
        return web.json_response(getattr(control, operation)(*args))

    def effect_view(actor, effect):
        if effect is None:
            return None
        from email import policy
        from email.parser import Parser
        proposal = effect['proposal']
        preview = {'provider': proposal['provider'], 'account': proposal['account'],
            'action': proposal['action'], 'target': proposal['target'], 'material': proposal.get('material')}
        if proposal['provider'] == 'gmail':
            message = Parser(policy=policy.default).parsestr(proposal['payload']['mime'])
            preview.update({key: message.get_all(key, []) for key in ('To', 'Cc', 'Bcc', 'Subject', 'From')})
        else:
            preview['event'] = proposal['payload'].get('event')
            preview['send_updates'] = proposal['payload'].get('send_updates')
        # This diagnostic never authorizes an effect and remains useful with no loop.
        scheduled = effect_worker.config is not None and proposal['account'] in effect_worker.config['accounts']
        return {**effect, 'preview': preview, 'delivery_configured': scheduled,
            'readiness': effects.readiness(effect['id'])}

    async def effect_read(request):
        actor = request[ACTOR]
        if service.actor_role(actor) == 'executor':
            return web.json_response({'status': 'rejected', 'error': 'forbidden'}, status=403)
        if request.query:
            raise ValueError('invalid_effect_query')
        identity = request.match_info.get('effect_id')
        result = effects.get(actor, identity) if identity else effects.list(actor)
        if identity and result is None:
            raise web.HTTPNotFound()
        return web.json_response(effect_view(actor, result) if identity else [effect_view(actor, e) for e in result])

    async def effect_call(request):
        operation, actor = request.match_info['operation'], request[ACTOR]
        role = service.actor_role(actor)
        if role == 'executor' or (operation != 'propose_effect' and role != 'owner'):
            return web.json_response({'status': 'rejected', 'error': 'forbidden'}, status=403)
        values = await request.json()
        if operation not in EFFECT_CONTROL or not isinstance(values, dict):
            raise ValueError('invalid_effect_operation')
        required = EFFECT_CONTROL[operation]
        keys = set(values)
        if operation == 'revoke_effect':
            valid = keys in (required | {'effect_id'}, required | {'grant_id'})
        else:
            valid = keys == required
        if not valid:
            raise ValueError('invalid_effect_fields')
        with service.store.lock:
            if operation == 'propose_effect':
                proposal = values['proposal']
                if not isinstance(proposal, dict):
                    raise ValueError('invalid_proposal')
                if role == 'principal':
                    job_id = request.headers.get('X-GTD-Job-ID', '')
                    guard = control.validate_target(job_id, actor, proposal.get('item_id'), 'prepare_private')
                    if not guard['allowed']:
                        return web.json_response({'status': 'rejected', 'error': guard['reason']}, status=403)
                result = effects.propose(actor, values['operation_id'], proposal)
            elif operation == 'authorize_effect':
                result = effects.authorize(actor, values['operation_id'], values['effect_id'], values['expected_proposal_hash'])
            elif operation == 'grant_draft_preparation':
                result = effects.grant_draft_preparation(actor, values['operation_id'], values['account'], values['grantee'], values['expires_at'])
            else:
                result = effects.revoke(actor, **values)
        return web.json_response(result)

    async def review(request):
        if service.actor_role(request[ACTOR]) == 'executor':
            return web.json_response({'status': 'rejected', 'error': 'forbidden'}, status=403)
        return web.json_response(service.review_state())

    async def agenda(request):
        if service.actor_role(request[ACTOR]) not in {'owner','principal'}:
            return web.json_response({'status':'rejected','error':'forbidden'},status=403)
        required={'account_alias','start','end','timezone'}
        if (set(request.query)-required-{'calendar_id'} or not required<=set(request.query)
                or any(len(request.query.getall(k))!=1 or not request.query[k] for k in required)):
            raise ValueError('invalid_agenda_fields')
        if monitor is None: raise ValueError('agenda_sources_not_configured')
        return web.json_response(await monitor.read_agenda(request.query['account_alias'],
            start=request.query['start'],end=request.query['end'],timezone=request.query['timezone'],
            calendar_ids=request.query.getall('calendar_id') if 'calendar_id' in request.query else None))

    async def sources(request):
        if request.query:
            raise ValueError('invalid_source_coverage_fields')
        if service.actor_role(request[ACTOR]) not in {'owner', 'principal'}:
            return web.json_response({'status': 'rejected', 'error': 'forbidden'}, status=403)
        return web.json_response(service.external_source_coverage())

    async def materials(request):
        if not readable(request, service.get_item(request.match_info['item_id'])):
            return web.json_response({'status': 'rejected', 'error': 'item_not_found'}, status=404)
        return web.json_response(service.materials(request.match_info['item_id']))

    async def material(request):
        if request.query:
            raise ValueError('invalid_material_fields')
        item_id = request.match_info['item_id']
        if not readable(request, service.get_item(item_id)):
            return web.json_response({'status': 'rejected', 'error': 'item_not_found'}, status=404)
        return web.json_response(service.read_material(item_id, request.match_info['material_id'],
            int(request.match_info['version'])))

    async def material_file(request):
        from urllib.parse import quote
        if request.query:
            raise ValueError('invalid_material_fields')
        item_id = request.match_info['item_id']
        with service.store.lock:
            if not readable(request, service.get_item(item_id)):
                return web.json_response({'status': 'rejected', 'error': 'item_not_found'}, status=404)
            result = service.read_material_file(item_id, request.match_info['material_id'], int(request.match_info['version']))
        return web.Response(body=result['data'], headers={
            'Content-Type': result['mime_type'],
            'Content-Disposition': "attachment; filename*=UTF-8''" + quote(result['filename'], safe=''),
            'X-Content-SHA256': result['sha256'], 'ETag': '"' + result['sha256'] + '"',
            'X-GTD-Material-ID': result['material_id'], 'X-GTD-Material-Version': str(result['version']),
            'X-GTD-Material-Valid': str(result['valid']).lower(), 'Cache-Control': 'no-store',
            'X-Content-Type-Options': 'nosniff'})

    async def export(request):
        if service.actor_role(request[ACTOR]) != 'owner':
            return web.json_response({'status': 'rejected', 'error': 'forbidden'}, status=403)
        with tempfile.TemporaryDirectory(dir=service.data_dir, prefix='api-export-') as temp:
            destination = Path(temp) / 'snapshot.zip'
            service.export(destination)
            data = destination.read_bytes()
        return web.Response(body=data, content_type='application/zip', headers={'Content-Disposition': 'attachment; filename="gtd-snapshot.zip"'})

    app.add_routes([web.get('/health', health), web.get('/v1/capabilities', capabilities),
        web.post('/v1/source-evaluation/{operation}', source_evaluation),
        web.get('/v1/items', items), web.get('/v1/items/{item_id}', item),
        web.get('/v1/source-attachments/{item_id}/{version}', source_attachment),
        web.post('/v1/captures', capture), web.post('/v1/commands', command),
        web.post('/v1/agent/command', command), web.post('/v1/agent/dispatch', dispatch), web.get('/v1/choose', choose),
        web.get('/v1/effects', effect_read), web.get('/v1/effects/{effect_id}', effect_read),
        web.post('/v1/effects/{operation}', effect_call), web.get('/v1/agenda', agenda), web.get('/v1/sources', sources), web.get('/v1/jobs', job_history), web.post('/v1/control/{operation}', control_call), web.get('/v1/review', review),
        web.get('/v1/material-files/{item_id}/{material_id}/{version}', material_file),
        web.get('/v1/materials/{item_id}/{material_id}/{version}', material), web.get('/v1/materials/{item_id}', materials), web.get('/v1/export', export)])
    app[SOURCE_MONITOR] = monitor
    app[EFFECT_MONITOR] = effect_worker
    return app
