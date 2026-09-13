"""Local service entrypoint and HTTP-only worker tool. Never accepts argv secrets."""
import argparse
import base64
import hashlib
import stat
import asyncio
import json
import os
from pathlib import Path
import sys
from urllib.parse import quote, urlsplit

import aiohttp
from aiohttp import web

from .application import create_app, load_config, read_private, writer_lock, CONTROL, EFFECT_CONTROL


async def bootstrap_bots(service, control, hermes, bots):
    """Run the serving process's bot bootstrap against the durable registry."""
    from .domain import fingerprint
    receipts = []
    for bot in bots:
        bot = dict(bot)
        existing = next((entry for entry in control.bots() if entry['id'] == bot['id']), None)
        if existing and existing.get('state') == 'suspended':
            receipts.append({'status': 'preserved', 'bot': existing})
            continue
        if bot.get('state') == 'available':
            probe = await hermes.discover(bot['id'])
            if probe.get('status') != 'ready':
                bot['state'] = 'unavailable'
            else:
                bot['probe_evidence'] = probe
        receipts.append(control.register_bot(service.owner_actor, 'bootstrap-bot:' + fingerprint(bot), bot))
    return receipts


def serve(config):
    from .service import GTDService
    from .control import ExecutionControl
    actors = config['actors']
    with writer_lock(config['data_dir']):
        service = GTDService(Path(config['data_dir']), owner_actor=actors['owner'],
            principal_actor=actors['principal'], executor_actors=actors.get('executors', []))
        try:
            control = ExecutionControl(service, config.get('budget', {}))
            app = create_app(service, control, config)
            if 'google' in config:
                from .application import SOURCE_MONITOR
                monitor = app[SOURCE_MONITOR]
                async def source_monitor(app):
                    await monitor.start()
                    try:
                        yield
                    finally:
                        await monitor.close()
                app.cleanup_ctx.append(source_monitor)
            if 'external_effects' in config:
                from .application import EFFECT_MONITOR
                async def external_effect_monitor(app):
                    stop = asyncio.Event()
                    task = asyncio.create_task(app[EFFECT_MONITOR].run(stop))
                    try:
                        yield
                    finally:
                        stop.set()
                        task.cancel()
                        await asyncio.gather(task, return_exceptions=True)
                app.cleanup_ctx.append(external_effect_monitor)
            orchestration = config.get('orchestration')
            if orchestration:
                from .hermes import HermesAdapter
                from .orchestration import OrchestrationWorker
                from .adapters import AdapterRouter
                from .codex import CodexAdapter
                async def native_worker(app):
                    async with aiohttp.ClientSession(trust_env=False) as session:
                        hermes = HermesAdapter(control, config.get('hermes', {}), session)
                        codex = CodexAdapter(control, config['codex']) if 'codex' in config else None
                        router = AdapterRouter(control, hermes, codex, config.get('adapters', {}))
                        if router.provider(orchestration['principal_bot_id']) != 'hermes':
                            raise ValueError('principal_hermes_required')
                        await bootstrap_bots(service, control, router, config.get('bots', []))
                        worker = OrchestrationWorker(service, control, router,
                            {'actor': actors['principal'], **orchestration})
                        stop = asyncio.Event()
                        task = asyncio.create_task(worker.run(stop))
                        try:
                            yield
                        finally:
                            stop.set()
                            task.cancel()
                            await asyncio.gather(task, return_exceptions=True)
                            await router.close()
                app.cleanup_ctx.append(native_worker)
            telegram = config.get('telegram')
            if telegram:
                from .telegram import AiohttpTelegramClient, TelegramAdapter, TelegramConfig
                token = (read_private(telegram['token_file']).decode().strip() if telegram.get('token_file')
                         else os.environ.get(telegram.get('token_env', ''), ''))
                if not token or telegram.get('actor', actors['owner']) != actors['owner']:
                    raise ValueError('explicit_telegram_owner_and_token_required')
                async def transport(app):
                    async with aiohttp.ClientSession() as session:
                        adapter = TelegramAdapter(service, AiohttpTelegramClient(token, session),
                            TelegramConfig(**{'actor': actors['owner'], **{k: v for k, v in telegram.items() if k not in {'token_file', 'token_env'}}}),
                            control=control, reservation_runtime_seconds=((config.get('orchestration') or {})
                                .get('reservation') or {}).get('max_runtime_seconds'))
                        stop = asyncio.Event()
                        task = asyncio.create_task(adapter.run(stop))
                        try:
                            yield
                        finally:
                            stop.set()
                            task.cancel()
                            await asyncio.gather(task, return_exceptions=True)
                app.cleanup_ctx.append(transport)
            web.run_app(app, host=config.get('listen_host', '127.0.0.1'),
                        port=config.get('port', 8765), access_log=None, print=None)
        finally:
            service.close()


async def client(args):
    url = args.url or os.environ.get('GTD_API_URL', 'http://127.0.0.1:8765')
    parsed = urlsplit(url)
    if parsed.scheme != 'http' or parsed.hostname not in {'127.0.0.1', '::1', 'localhost'} or parsed.username or parsed.password or parsed.query or parsed.fragment or parsed.path not in {'', '/'}:
        raise ValueError('local_api_url_required')
    token = read_private(args.token_file).decode().strip() if args.token_file else os.environ.get('GTD_API_TOKEN', '')
    if not token:
        raise ValueError('api_token_required')
    values = {}
    if args.action in {'query', 'capture', 'command', 'control'}:
        raw = Path(args.input).read_text() if args.input else sys.stdin.read()
        values = json.loads(raw or '{}')
        if not isinstance(values, dict):
            raise ValueError('json_object_required')
    method, params, payload = 'GET', None, None
    if args.action == 'upload':
        from .material_files import MAX_FILE, PPTX_MIME
        path = Path(args.file).absolute()
        if any(p.is_symlink() for p in (path, *path.parents)):
            raise ValueError('unsafe_upload_file')
        fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
        with os.fdopen(fd, 'rb') as stream:
            info = os.fstat(stream.fileno())
            if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or info.st_size > MAX_FILE:
                raise ValueError('unsafe_upload_file')
            data = stream.read(MAX_FILE + 1)
        if len(data) > MAX_FILE:
            raise ValueError('material_file_size_invalid')
        fields = {'content_base64': base64.b64encode(data).decode('ascii'), 'filename': path.name, 'mime_type': PPTX_MIME,
            'source_versions': json.loads(args.source_versions)}
        for name in ('material_id', 'title', 'mandate_id'):
            if getattr(args, name): fields[name] = getattr(args, name)
        path, method = '/v1/commands', 'POST'
        payload = {'operation_id': args.operation_id, 'action': 'put_material', 'item_id': args.item_id,
            'expected_version': args.expected_version, 'fields': fields}
    elif args.action == 'download':
        path = '/v1/material-files/' + '/'.join(quote(str(v), safe='') for v in (args.item_id, args.material_id, args.version))
    elif args.action == 'query':
        path, params = '/v1/items', {'filters': json.dumps(values)}
    elif args.action in {'capture', 'command'}:
        path = '/v1/' + {'capture': 'captures', 'command': 'commands'}[args.action]
        method, payload = 'POST', values
    elif args.action == 'control':
        path, method, payload = ('/v1/effects/' if args.operation in EFFECT_CONTROL else '/v1/control/') + args.operation, 'POST', values
    elif args.action == 'agenda':
        path='/v1/agenda';params=[(k,getattr(args,k)) for k in ('account_alias','start','end','timezone')]
        if args.calendar_id: params.extend(('calendar_id',c) for c in args.calendar_id)
    elif args.action == 'effect':
        path = '/v1/effects/' + quote(args.effect_id, safe='')
    elif args.action in {'get', 'materials'}:
        path = '/v1/' + ('items/' if args.action == 'get' else 'materials/') + quote(args.item_id, safe='')
    else:
        path = '/v1/' + args.action
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=60), trust_env=False) as session:
        async with session.request(method, url.rstrip('/') + path, params=params, json=payload,
                headers={'Authorization': 'Bearer ' + token, **({'X-GTD-Job-ID': os.environ['GTD_JOB_ID']} if os.environ.get('GTD_JOB_ID') else {})}, allow_redirects=False) as response:
            if args.action == 'download' and response.status == 200:
                from .material_files import MAX_FILE
                digest = response.headers.get('X-Content-SHA256', '')
                length = response.headers.get('Content-Length', '')
                if (len(digest) != 64 or any(c not in '0123456789abcdef' for c in digest)
                        or not length.isdigit() or not 0 <= int(length) <= MAX_FILE
                        or response.headers.get('X-GTD-Material-ID') != args.material_id
                        or response.headers.get('X-GTD-Material-Version') != str(args.version)):
                    raise ValueError('download_identity_invalid')
                data = bytearray()
                async for chunk in response.content.iter_chunked(65536):
                    data.extend(chunk)
                    if len(data) > MAX_FILE:
                        raise ValueError('download_size_invalid')
                if len(data) != int(length) or hashlib.sha256(data).hexdigest() != digest:
                    raise ValueError('download_hash_invalid')
                destination = Path(args.output).absolute()
                if any(p.is_symlink() for p in destination.parents):
                    raise ValueError('unsafe_download_destination')
                fd = os.open(destination, os.O_CREAT | os.O_EXCL | os.O_WRONLY | os.O_NOFOLLOW, 0o600)
                try:
                    with os.fdopen(fd, 'wb') as stream:
                        stream.write(data)
                        stream.flush()
                        os.fsync(stream.fileno())
                except BaseException:
                    destination.unlink()
                    raise
                print(json.dumps({'status': 'downloaded', 'material_id': args.material_id,
                    'version': args.version, 'sha256': digest, 'size': len(data),
                    'valid': response.headers.get('X-GTD-Material-Valid') == 'true'}))
                return 0
            if args.action == 'export' and response.status == 200:
                fd = os.open(args.output, os.O_CREAT | os.O_EXCL | os.O_WRONLY | os.O_NOFOLLOW, 0o600)
                with os.fdopen(fd, 'wb') as stream:
                    async for chunk in response.content.iter_chunked(65536):
                        stream.write(chunk)
                    stream.flush()
                    os.fsync(stream.fileno())
                print(json.dumps({'status': 'exported'}))
                return 0
            result = await response.json()
            print(json.dumps(result, ensure_ascii=False))
            return 0 if response.status < 400 else 1


def main(argv=None):
    parser = argparse.ArgumentParser(prog='gtd-felix')
    parser.add_argument('--url')
    parser.add_argument('--token-file')
    commands = parser.add_subparsers(dest='action', required=True)
    server = commands.add_parser('serve')
    server.add_argument('--config', required=True)
    for name in ('query', 'capture', 'command', 'control'):
        sub = commands.add_parser(name)
        sub.add_argument('--input', help='JSON file; defaults to stdin')
        if name == 'control':
            sub.add_argument('operation', choices=[*CONTROL, *EFFECT_CONTROL])
    for name in ('get', 'materials'):
        commands.add_parser(name).add_argument('item_id')
    agenda=commands.add_parser('agenda',help='Read a configured Calendar window without changing source coverage')
    for field in ('account-alias','start','end','timezone'): agenda.add_argument('--'+field,required=True)
    agenda.add_argument('--calendar-id',action='append')
    commands.add_parser('effect').add_argument('effect_id')
    for name in ('review', 'capabilities', 'sources', 'effects'):
        commands.add_parser(name)
    upload = commands.add_parser('upload', help='Upload one local PPTX as an identified material; authority remains HTTP/job scoped')
    upload.add_argument('item_id')
    upload.add_argument('--file', required=True)
    upload.add_argument('--operation-id', required=True)
    upload.add_argument('--expected-version', type=int, required=True)
    upload.add_argument('--source-versions', default='{}', help='JSON source revision mapping')
    for name in ('material-id', 'title', 'mandate-id'):
        upload.add_argument('--' + name)
    download = commands.add_parser('download', help='Download verified material bytes to a new private file')
    download.add_argument('item_id')
    download.add_argument('material_id')
    download.add_argument('version', type=int)
    download.add_argument('--output', required=True)
    commands.add_parser('export').add_argument('--output', required=True)
    commands.add_parser('mcp', help='Narrow GTD MCP over stdio; credentials only from environment')
    args = parser.parse_args(argv)
    try:
        if args.action == 'mcp':
            from .mcp import main as mcp_main
            return mcp_main()
        if args.action == 'serve':
            serve(load_config(args.config))
            return 0
        return asyncio.run(client(args))
    except KeyboardInterrupt:
        return 130
    except Exception:
        print(json.dumps({'status': 'rejected', 'error': 'configuration_or_transport_failed'}), file=sys.stderr)
        return 1
