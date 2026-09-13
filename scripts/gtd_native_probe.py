#!/usr/bin/env python3
"""P0 real, opt-in. Public Hermes CLI/API only; never loads/copies credentials."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import secrets
import shutil
import socket
import subprocess
import tempfile
import time
import urllib.error
import urllib.request

HOME = Path('/home/felix/.hermes/profiles/gtd-felix-p0-canary')
EVIDENCE = Path('/home/felix/.local/state/gtd-felix/p0-native-probe')
TERMINAL = {'completed', 'failed', 'cancelled', 'interrupted'}


def clean_environment(source, home, port, key):
    env = {k: source[k] for k in ('PATH', 'HOME', 'LANG', 'LC_ALL', 'TZ') if k in source}
    env.update(HERMES_HOME=str(home), HERMES_KANBAN_HOME=str(home),
               API_SERVER_ENABLED='true', API_SERVER_HOST='127.0.0.1',
               API_SERVER_PORT=str(port), API_SERVER_KEY=key,
               HERMES_KANBAN_DISPATCH_IN_GATEWAY='true', PYTHONUNBUFFERED='1')
    return env


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def create_home(home):
    # Refuse all preexisting state, including a symlink. No silent resume.
    home.mkdir(mode=0o700, parents=False, exist_ok=False)
    config = {
        'model': {'provider': 'openai-codex', 'default': 'gpt-6-astra'},
        'agent': {'max_turns': 1, 'reasoning_effort': 'low',
                  'api_max_retries': 1, 'run_budget_seconds': 45},
        'platform_toolsets': {'api_server': [], 'cli': []},
        'platforms': {'api_server': {'enabled': True}},
        'kanban': {'dispatch_in_gateway': True, 'dispatch_interval_seconds': 1,
                   'max_spawn': 1, 'max_in_progress': 1, 'failure_limit': 1,
                   'auto_decompose': False},
        'memory': {'memory_enabled': False, 'user_profile_enabled': False},
    }
    (home / 'config.yaml').write_text(json.dumps(config, indent=2))
    (home / '.env').touch(mode=0o600)
    (home / 'SOUL.md').write_text('Synthetic API test. Answer briefly. Do not access files, tools, or external systems.\n')


class Probe:
    def __init__(self, cli, home, evidence):
        self.cli, self.home, self.evidence = cli, home, evidence
        self.process = None
        self.log = None
        self.started = time.monotonic()
        self.receipt = {'checks': {}, 'runs': [], 'gateway_pids': [], 'limits':
                        'Synthetic P0 only. No product loading or external transports.'}
        with socket.socket() as sock:
            sock.bind(('127.0.0.1', 0))
            self.port = sock.getsockname()[1]
        self.key = secrets.token_urlsafe(48)
        self.env = clean_environment(os.environ, home, self.port, self.key)
        self.base = f'http://127.0.0.1:{self.port}'
        self.work = evidence / 'workspace'
        self.work.mkdir(mode=0o700)

    def check(self, name, condition, detail=None):
        self.receipt['checks'][name] = {'status': 'PASS' if condition else 'FAIL', 'detail': detail}
        require(condition, name)

    def request(self, method, path, body=None, key=None, authenticated=True):
        require(time.monotonic() - self.started < 570, 'gateway budget exhausted')
        headers = {'Content-Type': 'application/json'}
        if authenticated:
            headers['Authorization'] = 'Bearer ' + self.key
        if key:
            headers['Idempotency-Key'] = key
        req = urllib.request.Request(self.base + path, data=None if body is None else json.dumps(body).encode(), headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                return response.status, json.load(response)
        except urllib.error.HTTPError as exc:
            return exc.code, json.load(exc)

    def start(self):
        self.log = (self.evidence / ('gateway-%d.log' % len(self.receipt['gateway_pids']))).open('w')
        self.process = subprocess.Popen([self.cli, 'gateway', 'run', '--external-supervisor', '--quiet'], env=self.env, cwd=self.work, stdout=self.log, stderr=subprocess.STDOUT, start_new_session=True)
        self.receipt['gateway_pids'].append(self.process.pid)
        for _ in range(60):
            require(self.process.poll() is None, 'gateway exited; inspect private log')
            try:
                code, health = self.request('GET', '/health/detailed')
                if code == 200:
                    self.check('exclusive_api_receiver', health.get('pid') == self.process.pid, health)
                    platforms = health.get('platforms', {})
                    self.check('only_api_platform', set(platforms) <= {'api_server'}, platforms)
                    return
            except (OSError, ValueError):
                pass
            time.sleep(1)
        raise RuntimeError('gateway readiness timeout')

    def stop(self):
        if self.process is not None:
            pid = self.process.pid
            if self.process.poll() is None:
                self.process.terminate()
                try:
                    self.process.wait(timeout=20)
                except subprocess.TimeoutExpired:
                    self.process.kill()
                    self.process.wait(timeout=5)
            self.receipt['checks'][f'gateway_stopped_{pid}'] = {'status': 'PASS', 'exit_code': self.process.returncode}
            self.process = None
        if self.log:
            self.log.close()
            self.log = None

    def terminal(self, run_id, timeout=65):
        end = time.monotonic() + timeout
        while time.monotonic() < end:
            code, run = self.request('GET', '/v1/runs/' + run_id)
            require(code == 200, 'run status unavailable')
            if run.get('status') in TERMINAL:
                self.receipt['runs'].append(run)
                return run
            time.sleep(.2)
        raise RuntimeError('terminal observation timeout')

    def kanban_create(self):
        args = [self.cli, 'kanban', 'create', 'Synthetic P0 idempotency', '--body', 'Reply P0_OK only.', '--idempotency-key', 'gtd-p0-card', '--initial-status', 'blocked', '--max-runtime', '45s', '--max-retries', '1', '--json']
        result = subprocess.run(args, env=self.env, cwd=self.work, capture_output=True, text=True, timeout=20)
        require(result.returncode == 0, 'kanban CLI failed')
        # CLI may emit an update warning before JSON. Never publish arbitrary logs.
        offset = result.stdout.find('{')
        require(offset >= 0, 'kanban CLI returned no JSON')
        return json.loads(result.stdout[offset:])

    def kanban_cli(self, *args, json_output=False):
        result = subprocess.run([self.cli, 'kanban', *args], env=self.env, cwd=self.work,
                                capture_output=True, text=True, timeout=20)
        require(result.returncode == 0, 'kanban CLI failed: ' + args[0])
        if json_output:
            offset = result.stdout.find('{')
            require(offset >= 0, 'kanban CLI returned no JSON')
            return json.loads(result.stdout[offset:])

    def consume(self, card_id):
        self.kanban_cli('assign', card_id, HOME.name)
        before = self.kanban_cli('show', card_id, '--json', json_output=True)
        if before.get('task', before)['status'] != 'ready':
            self.kanban_cli('promote', card_id)
        self.start()
        deadline = time.monotonic() + 75
        observed = []
        while time.monotonic() < deadline:
            card = self.kanban_cli('show', card_id, '--json', json_output=True)
            task = card.get('task', card)
            observed.append(card)
            if task.get('status') in {'done', 'blocked', 'review'}:
                break
            time.sleep(1)
        self.receipt['kanban_observations'] = observed
        consumed = any(t.get('runs') or any(e.get('kind') in {'claimed', 'worker_spawned'} for e in t.get('events', [])) for t in observed)
        self.check('kanban_consumption', consumed, card)
        task = card.get('task', card)
        if task.get('status') not in {'done', 'blocked', 'review'}:
            self.kanban_cli('block', card_id)
            raise RuntimeError('kanban worker did not reach terminal within native cap')
        self.receipt['checks']['kanban_terminal'] = {'status': 'PASS', 'detail': task}

    def run(self):
        self.start()
        code, caps = self.request('GET', '/v1/capabilities')
        self.check('capabilities', code == 200, caps)
        code, _ = self.request('GET', '/v1/capabilities', authenticated=False)
        self.check('unauthenticated_rejected', code in {401, 403}, code)
        card = self.kanban_create()
        again = self.kanban_create()
        self.check('kanban_idempotency', card['id'] == again['id'], card)
        payload = {'input': 'Remember synthetic code P0_71. Reply P0_OK only.', 'model_options': {'reasoning_effort': 'low'}}
        code, admission = self.request('POST', '/v1/runs', payload, 'gtd-p0-run')
        self.check('run_admitted', code == 202, admission)
        run_id = admission['run_id']
        code, replay = self.request('POST', '/v1/runs', payload, 'gtd-p0-run')
        self.check('run_idempotency', code == 202 and replay['run_id'] == run_id, replay)
        code, _ = self.request('POST', '/v1/runs', {**payload, 'input': 'Different payload'}, 'gtd-p0-run')
        self.check('idempotency_conflict', code == 409, code)
        first = self.terminal(run_id)
        self.check('model_completed', first['status'] == 'completed', first)
        session_id = first['session_id']
        code, continuation = self.request('POST', '/v1/runs', {'input': 'What synthetic code did I ask you to remember? Reply code only.', 'session_id': session_id}, 'gtd-p0-continuation')
        self.check('continuation_admitted', code == 202, continuation)
        second = self.terminal(continuation['run_id'])
        self.check('session_continuity', second['status'] == 'completed' and second['session_id'] == session_id and 'P0_71' in json.dumps(second.get('output')), second)
        code, cancel = self.request('POST', '/v1/runs', {'input': 'Count from one to ten thousand in words.'}, 'gtd-p0-cancel')
        self.check('cancel_admitted', code == 202, cancel)
        code, stopped = self.request('POST', '/v1/runs/' + cancel['run_id'] + '/stop', {})
        self.check('stop_accepted', code in {200, 202}, stopped)
        cancelled = self.terminal(cancel['run_id'])
        self.check('cancelled_terminal', cancelled['status'] == 'cancelled', cancelled)
        self.stop()
        self.start()
        code, recovered = self.request('GET', '/v1/runs/' + run_id)
        self.check('run_recovered_after_restart', code == 200 and recovered['run_id'] == run_id, recovered)
        code, replay = self.request('POST', '/v1/runs', payload, 'gtd-p0-run')
        self.check('run_replay_after_restart', code == 202 and replay['run_id'] == run_id, replay)
        card_after = self.kanban_create()
        self.check('kanban_replay_after_restart', card['id'] == card_after['id'], card_after)
        self.stop()
        self.consume(card['id'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--execute', action='store_true', help='Create the exact new canary home and run the bounded real probe.')
    parser.add_argument('--continue-kanban', type=Path, help='Continue only the blocked card from a prior private receipt; does not rerun API inference.')
    args = parser.parse_args()
    if not args.execute and not args.continue_kanban:
        parser.print_help()
        return 0
    os.umask(0o077)
    EVIDENCE.mkdir(parents=True, exist_ok=True, mode=0o700)
    evidence = Path(tempfile.mkdtemp(prefix='attempt-', dir=EVIDENCE))
    probe = None
    receipt = {'status': 'BLOCKED', 'checks': {}}
    try:
        if not args.continue_kanban:
            create_home(HOME)
        cli = shutil.which('hermes')
        require(cli is not None, 'hermes CLI absent')
        probe = Probe(cli, HOME, evidence)
        if args.continue_kanban:
            require(args.continue_kanban.resolve().is_relative_to(EVIDENCE.resolve()), 'receipt outside private evidence root')
            prior = json.loads(args.continue_kanban.read_text())
            require(prior['checks']['kanban_consumption']['status'] == 'NOT_RUN', 'consumption already attempted')
            card_id = prior['checks']['kanban_idempotency']['detail']['id']
            card = probe.kanban_cli('show', card_id, '--json', json_output=True)
            require(card.get('task', card)['status'] in {'blocked', 'ready'} and card.get('task', card).get('assignee') in {None, HOME.name} and not card.get('runs'), 'prior card already assigned or consumed')
            probe.receipt['prior_receipt'] = str(args.continue_kanban.resolve())
            probe.consume(card_id)
        else:
            probe.run()
        receipt = probe.receipt
        receipt['status'] = 'COMPLETE'
    except Exception as exc:
        receipt = probe.receipt if probe else receipt
        receipt.update(status='BLOCKED', blocker=str(exc))
    finally:
        if probe:
            probe.stop()
        receipt['harness_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        (evidence / 'receipt.json').write_text(json.dumps(receipt, indent=2))
    print(json.dumps({'status': receipt['status'], 'receipt': str(evidence / 'receipt.json')}))
    return 0 if receipt['status'] == 'COMPLETE' else 2


if __name__ == '__main__':
    raise SystemExit(main())
