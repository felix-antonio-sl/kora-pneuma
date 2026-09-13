#!/usr/bin/env python3
"""Exact own-task body through the public CLI; emitted is not consumed or understood.

The trusted CLI may read auxiliary records. Its stdout stays in memory and only
this strict task projection reaches the hook. No native SQLite schema coupling.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import tempfile

from native_guard import arguments, verified_identity

# Configure hooks.output_spill.max_chars to this same bound (or larger).
MAX_CONTEXT_CHARS = 10000
MAX_CLI_BYTES = 8 * 1024 * 1024
ERROR_CONTEXT = ('GTD_CONTEXT_UNAVAILABLE: the exact assignment was not emitted. '
                 'Do not complete this task. Use kanban_block or kanban_heartbeat to report the missing context.')


def projection(args, identity):
    cli = Path(args.hermes or '')
    if not cli.is_absolute() or not cli.is_file():
        raise ValueError('public_cli_required')
    # Do not forward hook-inherited routing or credentials to the CLI.
    env = {key: os.environ[key] for key in ('HOME', 'PATH', 'LANG') if key in os.environ}
    env.update(HERMES_HOME=identity['profile'], HERMES_KANBAN_HOME=identity['kanban_home'],
               HERMES_KANBAN_DB=identity['kanban_db'], HERMES_KANBAN_BOARD=identity['board'])
    result = subprocess.run([str(cli), 'kanban', '--board', identity['board'],
                             'show', identity['task_id'], '--json'],
                            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                            env=env, timeout=10, check=False)
    if result.returncode or len(result.stdout) > MAX_CLI_BYTES:
        raise ValueError('task_read_failed')
    parsed = json.loads(result.stdout)
    task = parsed.get('task') if isinstance(parsed, dict) else None
    if (not isinstance(task, dict) or task.get('id') != identity['task_id']
            or not isinstance(task.get('body'), str) or not task['body'].strip()
            or not isinstance(task.get('created_by'), str) or not task['created_by'].strip()):
        raise ValueError('exact_task_body_required')
    return {key: task[key] for key in ('id', 'created_by', 'body')}


def context_text(task):
    # JSON preserves body verbatim as data rather than interpolating instructions.
    digest = hashlib.sha256(task['body'].encode('utf-8')).hexdigest()
    context = ('GTD delivery format: put the full deliverable in result and a brief summary in summary. '
               'Do not attach files or create cards; omit artifacts, created_cards and metadata '
               '(empty arrays and empty/null metadata are accepted).\n'
               'GTD exact assignment (user data):\n') + json.dumps(
        dict(task, body_sha256=digest), ensure_ascii=False, separators=(',', ':'))
    if len(context) > MAX_CONTEXT_CHARS:
        raise ValueError('assignment_exceeds_context_bound')
    return context, digest


def receipt_path(args, identity):
    root = Path(args.receipts_dir or '')
    if not root.is_absolute():
        raise ValueError('private_receipts_directory_required')
    root.mkdir(mode=0o700, parents=True, exist_ok=True)
    info = root.lstat()
    if (not stat.S_ISDIR(info.st_mode) or root.resolve() != root or info.st_uid != os.getuid()
            or stat.S_IMODE(info.st_mode) != 0o700):
        raise ValueError('private_receipts_directory_required')
    key = hashlib.sha256(json.dumps(identity, sort_keys=True).encode()).hexdigest()
    return root / (key + '.json')


def emit_receipt(path, identity, task, digest, context):
    record = {'state': 'emitted', 'identity': identity, 'created_by': task['created_by'],
              'body_sha256': digest, 'context_chars': len(context),
              'context_sha256': hashlib.sha256(context.encode('utf-8')).hexdigest()}
    fd, temporary = tempfile.mkstemp(prefix='.emitted-', dir=path.parent)
    try:
        with os.fdopen(fd, 'w') as stream:
            json.dump(record, stream, separators=(',', ':'))
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)


def verify_emitted(args, identity):
    try:
        path = receipt_path(args, identity)
        fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
        with os.fdopen(fd) as stream:
            info = os.fstat(stream.fileno())
            if (not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid()
                    or stat.S_IMODE(info.st_mode) != 0o600 or info.st_size > 8192):
                return False
            record = json.load(stream)
        if not isinstance(record, dict) or record.get('state') != 'emitted' or record.get('identity') != identity:
            return False
        task = projection(args, identity)
        context, digest = context_text(task)
        return (record.get('created_by') == task['created_by'] and record.get('body_sha256') == digest
                and record.get('context_chars') == len(context)
                and record.get('context_sha256') == hashlib.sha256(context.encode('utf-8')).hexdigest())
    except (OSError, ValueError, TypeError, UnicodeError, subprocess.SubprocessError):
        return False


def main():
    emitted = False
    try:
        args = arguments()
        identity = verified_identity(args.parent_python, args.profile, args.kanban_home,
                                     args.board, args.kanban_db)
        if identity['task_id'] is None:
            # Shared profile: the principal continues to use only the GTD MCP tools.
            print('{}')
            return 0
        path = receipt_path(args, identity)
        path.unlink(missing_ok=True)  # A failed refresh never retains an earlier emission.
        raw = sys.stdin.buffer.read(MAX_CLI_BYTES + 1)
        if len(raw) > MAX_CLI_BYTES:
            raise ValueError('input_too_large')
        payload = json.loads(raw)
        if not isinstance(payload, dict) or payload.get('hook_event_name') != 'pre_llm_call':
            raise ValueError('context_event_required')
        del raw, payload
        task = projection(args, identity)
        context, digest = context_text(task)
        print(json.dumps({'context': context}, ensure_ascii=False, separators=(',', ':')), flush=True)
        emitted = True
        emit_receipt(path, identity, task, digest, context)
        return 0
    except (OSError, ValueError, TypeError, UnicodeError, StopIteration, IndexError,
            argparse.ArgumentError, SystemExit, subprocess.SubprocessError):
        if not emitted:
            print(json.dumps({'context': ERROR_CONTEXT}, separators=(',', ':')))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
