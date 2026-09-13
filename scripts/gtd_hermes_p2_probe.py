#!/usr/bin/env python3
"""Opt-in synthetic P2 Hermes probe; uses an existing privately configured route.

Never starts/installs Hermes, reads credentials from files, or touches native DBs.
Without --execute only CLI help is shown. Runs are reserved in an isolated local
application Store before the adapter can submit them. Existing runs resume via
--job-id; an uncertain operation is never replaced by a fresh job automatically.
"""
import argparse
import asyncio
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
_runtime_override = os.environ.get('GTD_RUNTIME_ROOT')
if _runtime_override is not None:
    if not _runtime_override.strip():
        raise RuntimeError('gtd_runtime_unavailable')
    RUNTIME = Path(_runtime_override).expanduser().resolve()
else:
    RUNTIME = ROOT / 'products/fxsl/gtd-operations/runtime'
if not (RUNTIME / 'gtd_felix/__init__.py').is_file():
    raise RuntimeError('gtd_runtime_unavailable')
sys.path.insert(0, str(RUNTIME))

import aiohttp
from gtd_felix import GTDService
from gtd_felix.control import ExecutionControl
from gtd_felix.hermes import HermesAdapter


async def run(args):
    config = json.loads(args.config.read_text())
    if config.get('synthetic_canary') is not True:
        raise ValueError('synthetic_canary_config_required')
    data_dir = Path(config['data_dir']).absolute()
    if not args.job_id and data_dir.exists() and any(data_dir.iterdir()):
        raise ValueError('new_canary_requires_empty_data_dir')
    service = GTDService(data_dir, **config.get('actors', {}))
    control = ExecutionControl(service, config['execution'])
    receipt = {'status': 'PARTIAL', 'checks': {}, 'job_id': args.job_id,
               'limits': ['Synthetic existing-route probe only; does not install or restart Hermes.',
                          'Unknown USD telemetry debits the reserved amount; this is not a native billing cutoff.']}
    try:
        async with aiohttp.ClientSession() as session:
            adapter = HermesAdapter(control, config['hermes'], session)
            discovery = await adapter.discover(args.bot)
            receipt['checks']['discovery'] = discovery
            if discovery['status'] != 'ready':
                receipt['status'] = 'BLOCKED'
                return receipt
            if args.mode == 'discover':
                receipt['status'] = 'COMPLETE'
                return receipt
            if args.job_id:
                job_id = args.job_id
            else:
                prompt = args.prompt_file.read_text() if args.prompt_file else 'Return exactly SYNTHETIC_GTD_P2_OK.'
                item = service.capture(service.owner_actor, 'canary-capture', 'Synthetic bounded private preparation')['item']
                route = config['hermes']['routes'][args.bot]
                bot = {'id': args.bot, 'state': 'available', 'source_urn': 'urn:fxsl:agent:gtd-felix',
                    'profile': route['profile'], 'host': route['host'], 'capabilities': ['prepare_private'],
                    'item_id': item['id'], 'probe_evidence': 'hermes:discovery:' + args.bot}
                registered = control.register_bot(service.owner_actor, 'canary-bot', bot)
                if registered['status'] != 'applied':
                    raise ValueError('canary_bot_not_registered')
                reservation = config['reservation']
                reserved = control.reserve(service.principal_actor, 'canary-reserve', {
                    'item_id': item['id'], 'expected_version': item['version'], 'mandate_id': None,
                    'capability': 'prepare_private', 'bot_id': args.bot, 'purpose': 'Synthetic P2 adapter proof',
                    'scope': 'Synthetic private output only', **reservation})
                if reserved['status'] != 'reserved':
                    receipt['checks']['admission'] = reserved
                    receipt['status'] = 'BLOCKED'
                    return receipt
                job_id = reserved['job_id']
                receipt['job_id'] = job_id
                receipt['checks']['submit'] = await adapter.submit(job_id, prompt, durable=args.mode == 'durable')
            if args.mode == 'stop':
                receipt['checks']['stop'] = await adapter.stop(job_id)
            elif args.mode == 'steer':
                if not args.prompt_file:
                    raise ValueError('steer_prompt_file_required')
                receipt['checks']['steer'] = await adapter.steer(job_id, args.prompt_file.read_text())
            else:
                receipt['checks']['reconcile'] = await adapter.reconcile(job_id)
            # A finite observer loop only; native execution belongs to Hermes.
            deadline = time.monotonic() + min(args.wait_seconds, 120)
            result = {}
            while time.monotonic() < deadline:
                result = await adapter.poll(job_id)
                if result.get('terminal') or result['status'] in {'uncertain', 'rejected'}:
                    break
                await asyncio.sleep(.5)
            receipt['checks']['terminal'] = result
            receipt['budget'] = control.budget()
            receipt['status'] = 'COMPLETE' if result.get('terminal') else 'PARTIAL'
            return receipt
    finally:
        service.close()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--execute', action='store_true')
    parser.add_argument('--config', type=Path, help='Private JSON config; only environment variable names for API keys.')
    parser.add_argument('--bot', default='gtd-felix-p2-canary')
    parser.add_argument('--mode', choices=('discover', 'api', 'durable', 'poll', 'stop', 'steer'), default='discover')
    parser.add_argument('--job-id', help='Exact existing control job for observation/control; never a replacement.')
    parser.add_argument('--prompt-file', type=Path, help='Synthetic prompt/guidance; never credentials.')
    parser.add_argument('--receipt', type=Path, help='New private output file; never overwrite prior evidence.')
    parser.add_argument('--wait-seconds', type=float, default=30)
    args = parser.parse_args(argv)
    if not args.execute:
        parser.print_help()
        return 0
    if not args.config or not args.receipt or not 0 <= args.wait_seconds <= 120:
        parser.error('--config, --receipt and bounded --wait-seconds are required')
    if args.mode in {'poll', 'stop', 'steer'} and not args.job_id:
        parser.error('control/observation requires --job-id')
    os.umask(0o077)
    fd = os.open(args.receipt, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    try:
        receipt = asyncio.run(run(args))
    except Exception as exc:
        # Native messages can contain personal data or credentials; emit type only.
        receipt = {'status': 'BLOCKED', 'error': type(exc).__name__, 'limits': ['Inspect private configuration; no provider error text emitted.']}
    receipt['recorded_at'] = datetime.now(timezone.utc).isoformat()
    content = (json.dumps(receipt, indent=2, ensure_ascii=False) + '\n').encode()
    with os.fdopen(fd, 'wb') as stream:
        stream.write(content)
        stream.flush()
        os.fsync(stream.fileno())
    print(json.dumps({'status': receipt['status'], 'job_id': receipt.get('job_id'),
                      'receipt': str(args.receipt), 'sha256': hashlib.sha256(content).hexdigest()}))
    return 0 if receipt['status'] == 'COMPLETE' else 1


if __name__ == '__main__':
    raise SystemExit(main())
