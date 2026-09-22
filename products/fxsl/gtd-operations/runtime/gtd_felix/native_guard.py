#!/usr/bin/env python3
"""Linux shell-hook boundary using only verified direct-parent initial identity.

No network or environment logging. /proc reads are limited to parent identity;
no ancestor traversal and no trust in the hook's inherited task environment.
"""
import argparse
import json
import os
from pathlib import Path
import sys

ALLOWED = frozenset({'kanban_complete', 'kanban_block', 'kanban_heartbeat', 'kanban_comment'})
MCP_ALLOWED = frozenset({'mcp__gtd__gtd_read', 'mcp__gtd__gtd_command', 'mcp__gtd__gtd_dispatch', 'mcp__gtd__gtd_decide'})
IDENTITY_KEYS = frozenset({'HERMES_HOME', 'HERMES_KANBAN_HOME', 'HERMES_KANBAN_TASK', 'HERMES_DELEGATED_CHILD_CONTEXT', 'HERMES_KANBAN_DB', 'HERMES_KANBAN_BOARD'})


def blocked():
    return {'decision': 'block', 'reason': 'GTD native identity or capability is not allowed.'}


LIFECYCLE_ARGS = {
    'kanban_complete': frozenset({'task_id', 'summary', 'metadata', 'result', 'artifacts', 'created_cards'}),
    'kanban_block': frozenset({'task_id', 'reason', 'kind'}),
    'kanban_heartbeat': frozenset({'task_id', 'note'}),
    'kanban_comment': frozenset({'task_id', 'body'}),
}


def decision(payload, own_task_id, *, context_emitted=False):
    if not isinstance(payload, dict) or payload.get('hook_event_name') != 'pre_tool_call':
        return blocked()
    args = payload.get('tool_input')
    if not isinstance(args, dict):
        return blocked()
    if own_task_id is None:
        return {'decision': 'allow'} if payload.get('tool_name') in MCP_ALLOWED else blocked()
    if payload.get('tool_name') == 'kanban_show':
        return {'decision': 'block', 'reason': 'GTD supplies the exact task body through emitted user context. '
                'Use that context; if unavailable, report the missing context with kanban_block.'}
    if (not isinstance(own_task_id, str) or not own_task_id or payload.get('tool_name') not in ALLOWED
            or args.get('task_id', own_task_id) not in ('', own_task_id)
            or set(args) - LIFECYCLE_ARGS[payload['tool_name']]
            or (payload['tool_name'] == 'kanban_complete' and not context_emitted)):
        return blocked()
    if payload['tool_name'] == 'kanban_complete':
        if (args.get('artifacts', []) != [] or args.get('created_cards', []) != []
                or args.get('metadata') not in (None, {})):
            return blocked()
    return {'decision': 'allow'}


def _snapshot(pid, parent_python):
    parent = Path('/proc') / str(pid)
    status = (parent / 'status').read_text()
    uid_line = next(line for line in status.splitlines() if line.startswith('Uid:'))
    if any(int(uid) != os.getuid() for uid in uid_line.split()[1:]):
        raise ValueError('parent_uid')
    if (parent / 'exe').resolve(strict=True) != parent_python:
        raise ValueError('parent_executable')
    # starttime distinguishes PID reuse; comm can itself contain spaces or ')'.
    stat = (parent / 'stat').read_text().rsplit(')', 1)[1].split()
    return stat[19]


def verified_identity(parent_python, profile, kanban_home, board=None, kanban_db=None):
    paths = [Path(value) for value in (parent_python, profile, kanban_home)]
    if any(not path.is_absolute() for path in paths):
        raise ValueError('absolute_identity_required')
    executable, profile_path, board_path = [path.resolve(strict=True) for path in paths]
    if str(profile_path) != profile or str(board_path) != kanban_home or profile_path == board_path:
        raise ValueError('canonical_identity_required')
    pid = os.getppid()
    if pid <= 1:
        raise ValueError('parent_missing')
    before = _snapshot(pid, executable)
    values = {}
    # Retain only identity fields, never expose or persist the environment.
    with (Path('/proc') / str(pid) / 'environ').open('rb') as stream:
        raw = stream.read(1024 * 1024 + 1)
    if len(raw) > 1024 * 1024:
        raise ValueError('parent_environment_too_large')
    for entry in raw.split(b'\0'):
        key, separator, value = entry.partition(b'=')
        if key in {name.encode() for name in IDENTITY_KEYS}:
            name = key.decode('ascii')
            if not separator or name in values:
                raise ValueError('ambiguous_identity')
            values[name] = value.decode('utf-8')
    del raw
    if (values.get('HERMES_HOME') != profile or values.get('HERMES_KANBAN_HOME') != kanban_home
            or values.get('HERMES_DELEGATED_CHILD_CONTEXT')
            or os.getppid() != pid or _snapshot(pid, executable) != before):
        raise ValueError('parent_identity_changed')
    task = values.get('HERMES_KANBAN_TASK')
    if task is not None and not task.strip():
        raise ValueError('empty_task_identity')
    identity = {'pid': pid, 'birth': before, 'profile': profile, 'kanban_home': kanban_home,
                'task_id': task}
    if task is not None:
        if (not board or not kanban_db or values.get('HERMES_KANBAN_BOARD') != board
                or values.get('HERMES_KANBAN_DB') != kanban_db):
            raise ValueError('worker_board_identity')
        db = Path(kanban_db)
        if not db.is_absolute() or str(db.resolve(strict=True)) != kanban_db or not db.is_file():
            raise ValueError('canonical_board_database_required')
        identity.update(board=board, kanban_db=kanban_db)
    return identity


def parent_identity(parent_python, profile, kanban_home):
    return verified_identity(parent_python, profile, kanban_home)['task_id']


def arguments():
    parser = argparse.ArgumentParser(add_help=False, exit_on_error=False)
    parser.add_argument('--parent-python', required=True)
    parser.add_argument('--profile', required=True)
    parser.add_argument('--kanban-home', required=True)
    parser.add_argument('--board')
    parser.add_argument('--kanban-db')
    parser.add_argument('--hermes')
    parser.add_argument('--receipts-dir')
    return parser.parse_args()


def main():
    try:
        args = arguments()
        identity = verified_identity(args.parent_python, args.profile, args.kanban_home,
                                     args.board, args.kanban_db)
        raw = sys.stdin.buffer.read(65537)
        if len(raw) > 65536:
            raise ValueError('input_too_large')
        payload = json.loads(raw)
        emitted = False
        if (identity['task_id'] is not None and isinstance(payload, dict)
                and payload.get('tool_name') == 'kanban_complete'):
            from native_context import verify_emitted
            emitted = verify_emitted(args, identity)
        result = decision(payload, identity['task_id'], context_emitted=emitted)
        if (identity['task_id'] is not None and isinstance(payload, dict)
                and payload.get('tool_name') == 'kanban_complete' and not emitted
                and decision(payload, identity['task_id'], context_emitted=True)['decision'] == 'allow'):
            result = {'decision': 'block', 'reason': 'GTD exact assignment has no current emitted context receipt. '
                      'Use kanban_block or kanban_heartbeat to report the missing context.'}
    except (ValueError, TypeError, UnicodeError, OSError, StopIteration, IndexError, argparse.ArgumentError, SystemExit):
        result = blocked()
    print(json.dumps(result, separators=(',', ':')))
    return 0 if result['decision'] == 'allow' else 2


if __name__ == '__main__':
    raise SystemExit(main())
