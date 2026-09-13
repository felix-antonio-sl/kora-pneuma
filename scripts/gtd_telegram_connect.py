#!/usr/bin/env python3
"""Prepare an explicitly selected existing Telegram bot; never receive updates.

Inspection uses getMe/getWebhookInfo; pairing adds one non-acknowledging
getUpdates read. Ongoing ingestion remains the product adapter.
Capture requires a real terminal and creates a new private file without overwrite.
"""
import argparse
import asyncio
from datetime import datetime, timezone
import getpass
import secrets
import time
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
import warnings


class Blocked(Exception):
    pass


def directory(path):
    fd = os.open('/', os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in Path(os.path.abspath(path)).parts[1:]:
            child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = child
        info = os.fstat(fd)
        if info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) != 0o700:
            raise Blocked('private_directory_required')
        return fd
    except BaseException:
        os.close(fd)
        raise


def valid_token(value):
    if not isinstance(value, str) or not re.fullmatch(r'[0-9]{1,20}:[A-Za-z0-9_-]{30,200}', value):
        raise Blocked('invalid_token_format')
    return value


def read_token(path):
    path = Path(os.path.abspath(path))
    parent = directory(path.parent)
    try:
        fd = os.open(path.name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=parent)
        try:
            before = os.fstat(fd)
            if not stat.S_ISREG(before.st_mode) or before.st_uid != os.getuid() or stat.S_IMODE(before.st_mode) != 0o600 or before.st_nlink != 1 or before.st_size > 1024:
                raise Blocked('private_token_file_required')
            data = os.read(fd, 1025)
            after = os.fstat(fd)
            if (before.st_size, before.st_mtime_ns, before.st_ctime_ns) != (after.st_size, after.st_mtime_ns, after.st_ctime_ns):
                raise Blocked('token_file_changed')
            return valid_token(data.decode('ascii').rstrip('\n'))
        finally:
            os.close(fd)
    finally:
        os.close(parent)


def capture(path):
    """Local-only capture; no API call and no echo fallback when TTY is absent."""
    path = Path(os.path.abspath(path))
    parent = directory(path.parent)
    try:
        try:
            os.stat(path.name, dir_fd=parent, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise Blocked('output_exists')
        if not sys.stdin.isatty():
            raise Blocked('private_terminal_required')
        with warnings.catch_warnings():
            warnings.simplefilter('error', getpass.GetPassWarning)
            value = valid_token(getpass.getpass('Token del bot existente (oculto; no lo pegues en el chat): '))
        fd = os.open(path.name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=parent)
        with os.fdopen(fd, 'w') as output:
            os.fchmod(output.fileno(), 0o600)
            output.write(value + '\n')
            output.flush()
            os.fsync(output.fileno())
        os.fsync(parent)
        return {'status': 'captured_not_verified', 'token_file': str(path), 'network_calls': 0}
    finally:
        os.close(parent)


async def inspect(path, expected_username='korax_kv_bot', *, attempts=2, timeout=10, session_factory=None):
    if not re.fullmatch(r'[A-Za-z0-9_]{5,32}', expected_username) or type(attempts) is not int or not 1 <= attempts <= 3 or type(timeout) not in (int, float) or not 0 < timeout <= 30:
        raise Blocked('invalid_inspection_parameters')
    token = read_token(path)
    import aiohttp
    async with (session_factory or aiohttp.ClientSession)(trust_env=False) as session:
        async def read(method):
            for attempt in range(attempts):
                retry = False
                try:
                    async with session.get('https://api.telegram.org/bot' + token + '/' + method,
                                           timeout=aiohttp.ClientTimeout(total=timeout), allow_redirects=False) as response:
                        if response.status in (401, 403):
                            raise Blocked('telegram_authentication_failed')
                        if response.status == 429 or 500 <= response.status <= 599:
                            retry = True
                        elif response.status != 200:
                            raise Blocked('telegram_request_rejected')
                        else:
                            data = bytearray()
                            async for chunk in response.content.iter_chunked(4096):
                                data.extend(chunk)
                                if len(data) > 65536:
                                    raise Blocked('telegram_response_too_large')
                            value = json.loads(data)
                            if not isinstance(value, dict) or value.get('ok') is not True or not isinstance(value.get('result'), dict):
                                raise Blocked('telegram_response_invalid')
                            return value['result']
                except Blocked:
                    raise
                except (aiohttp.ClientError, asyncio.TimeoutError):
                    retry = True
                except Exception:
                    raise Blocked('telegram_response_invalid') from None
                if retry and attempt + 1 < attempts:
                    await asyncio.sleep(.25 * (attempt + 1))
            raise Blocked('telegram_temporarily_unavailable')
        bot = await read('getMe')
        if bot.get('is_bot') is not True or type(bot.get('id')) is not int or bot['id'] <= 0 or bot.get('username') != expected_username:
            raise Blocked('bot_identity_mismatch')
        webhook = await read('getWebhookInfo')
        if not isinstance(webhook.get('url'), str) or type(webhook.get('pending_update_count')) is not int or webhook['pending_update_count'] < 0:
            raise Blocked('webhook_response_invalid')
        result = {'bot_id': bot['id'], 'username': bot['username'], 'username_matches': True,
                  'webhook_present': bool(webhook['url']), 'pending_update_count': webhook['pending_update_count']}
        return {**result, 'status': 'blocked_webhook_present' if result['webhook_present'] else 'verified_identity_owner_selection_pending',
                'metadata_sha256': hashlib.sha256(json.dumps(result, sort_keys=True).encode()).hexdigest(),
                'observed_at': datetime.now(timezone.utc).isoformat(), 'polling_started': False,
                'owner_user_id': None, 'chat_id': None,
                'next_step': 'User starts a private conversation, then owner user/chat must be explicitly selected and verified before the product poller starts.',
                'limits': ['No webhook modification, messages or updates requested.', 'No assertion that another polling client is absent.']}


def prepare(path, expected_username='korax_kv_bot', seconds=300):
    """Create a NEW secret challenge, displayed only for the owner's manual use."""
    if not re.fullmatch(r'[A-Za-z0-9_]{5,32}', expected_username) or type(seconds) is not int or not 30 <= seconds <= 600:
        raise Blocked('invalid_challenge_parameters')
    path = Path(os.path.abspath(path))
    parent = directory(path.parent)
    try:
        challenge = {'version': 1, 'username': expected_username, 'phrase': 'GTD ' + secrets.token_urlsafe(24),
                     'created_at': int(time.time()), 'expires_at': int(time.time()) + seconds, 'used': False}
        fd = os.open(path.name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=parent)
        with os.fdopen(fd, 'w') as output:
            os.fchmod(output.fileno(), 0o600)
            json.dump(challenge, output)
            output.flush()
            os.fsync(output.fileno())
        os.fsync(parent)
        return {'status': 'challenge_prepared', 'challenge_file': str(path), 'phrase': challenge['phrase'],
                'expected_username': expected_username, 'expires_at': challenge['expires_at'],
                'instruction': 'Send this exact phrase manually to the selected bot in a private chat. Do not paste it into another chat.'}
    finally:
        os.close(parent)


async def pair(token_file, challenge_file, *, session_factory=None):
    """One bounded non-acknowledging read. Local nonce consumption is exclusive.

    No offset is sent; no update content, names or challenge phrase are returned.
    A successful match consumes the local challenge before returning its receipt.
    """
    import aiohttp
    path = Path(os.path.abspath(challenge_file))
    parent = directory(path.parent)
    fd = None
    try:
        fd = os.open(path.name, os.O_RDWR | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=parent)
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) != 0o600 or info.st_nlink != 1 or info.st_size > 4096:
            raise Blocked('private_challenge_required')
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise Blocked('challenge_in_use') from None
        challenge = json.loads(os.read(fd, 4097))
        if (not isinstance(challenge, dict) or challenge.get('version') != 1
                or type(challenge.get('used')) is not bool
                or not isinstance(challenge.get('phrase'), str)
                or not re.fullmatch(r'GTD [A-Za-z0-9_-]{32}', challenge['phrase'])
                or type(challenge.get('created_at')) is not int or type(challenge.get('expires_at')) is not int
                or not 30 <= challenge['expires_at'] - challenge['created_at'] <= 600):
            raise Blocked('invalid_challenge')
        if challenge['used']:
            raise Blocked('challenge_already_used')
        if not challenge['created_at'] <= time.time() < challenge['expires_at']:
            raise Blocked('challenge_expired')
        token = read_token(token_file)
        identity = await inspect(token_file, challenge['username'], attempts=1, timeout=5, session_factory=session_factory)
        if identity['webhook_present']:
            raise Blocked('webhook_present')
        if read_token(token_file) != token:
            raise Blocked('token_file_changed')
        requests_sent = 0
        async def one_read(request, handler):
            nonlocal requests_sent
            requests_sent += 1
            if requests_sent != 1:
                raise Blocked('pairing_read_retry_blocked')
            return await handler(request)
        try:
            async with (session_factory or aiohttp.ClientSession)(trust_env=False) as session:
                async with session.get('https://api.telegram.org/bot' + token + '/getUpdates',
                    params={'limit': 100, 'timeout': 0}, timeout=aiohttp.ClientTimeout(total=5), allow_redirects=False, middlewares=(one_read,)) as response:
                    if response.status == 409:
                        raise Blocked('another_receiver_conflict')
                    if response.status != 200:
                        raise Blocked('pairing_read_rejected')
                    data = bytearray()
                    async for chunk in response.content.iter_chunked(4096):
                        data.extend(chunk)
                        if len(data) > 2 * 1024 * 1024:
                            raise Blocked('pairing_response_too_large')
                    value = json.loads(data)
        except Blocked:
            raise
        except Exception:
            raise Blocked('pairing_read_failed') from None
        if not isinstance(value, dict) or value.get('ok') is not True or not isinstance(value.get('result'), list) or len(value['result']) > 100:
            raise Blocked('pairing_response_invalid')
        matches = []
        for update in value['result']:
            if not isinstance(update, dict):
                raise Blocked('pairing_response_invalid')
            message = update.get('message') or {}
            if not isinstance(message, dict) or message.get('text') != challenge['phrase']:
                continue
            author, chat = message.get('from') or {}, message.get('chat') or {}
            if (not isinstance(author, dict) or not isinstance(chat, dict)
                    or author.get('is_bot') is not False or chat.get('type') != 'private'
                    or type(author.get('id')) is not int or author['id'] <= 0
                    or type(chat.get('id')) is not int or chat['id'] != author['id']
                    or type(update.get('update_id')) is not int or update['update_id'] < 0
                    or type(message.get('date')) is not int
                    or not challenge['created_at'] <= message['date'] <= min(time.time(), challenge['expires_at'])
                    or any(k in message for k in ('forward_origin', 'forward_from', 'sender_chat', 'via_bot'))):
                raise Blocked('challenge_match_invalid')
            matches.append((author['id'], chat['id'], update['update_id'], message['date']))
        if time.time() >= challenge['expires_at']:
            raise Blocked('challenge_expired')
        if not matches:
            raise Blocked('challenge_not_observed_in_window')
        if len(matches) != 1:
            raise Blocked('ambiguous_challenge_matches')
        owner, chat, update, sent = matches[0]
        receipt = {'status': 'paired_selection_not_poller_started', 'bot_id': identity['bot_id'],
            'username': identity['username'], 'owner_user_id': owner, 'chat_id': chat, 'update_id': update,
            'challenge_sha256': hashlib.sha256(challenge['phrase'].encode()).hexdigest(),
            'message_at': sent, 'verified_at': datetime.now(timezone.utc).isoformat(), 'polling_started': False}
        challenge.update(used=True, receipt=receipt)
        os.lseek(fd, 0, os.SEEK_SET)
        os.ftruncate(fd, 0)
        payload = json.dumps(challenge).encode()
        with os.fdopen(os.dup(fd), 'wb') as output:
            output.write(payload)
            output.flush()
            os.fsync(output.fileno())
        return receipt
    finally:
        if fd is not None:
            os.close(fd)
        os.close(parent)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    sub.add_parser('capture').add_argument('--token-file', required=True)
    prep = sub.add_parser('prepare')
    prep.add_argument('--challenge-file', required=True)
    prep.add_argument('--expected-username', default='korax_kv_bot')
    prep.add_argument('--seconds', type=int, default=300)
    pairing = sub.add_parser('pair')
    pairing.add_argument('--token-file', required=True)
    pairing.add_argument('--challenge-file', required=True)
    command = sub.add_parser('inspect')
    command.add_argument('--token-file', required=True)
    command.add_argument('--expected-username', default='korax_kv_bot')
    command.add_argument('--attempts', type=int, default=2)
    command.add_argument('--timeout', type=float, default=10)
    args = parser.parse_args(argv)
    try:
        if args.action == 'prepare':
            result = prepare(args.challenge_file, args.expected_username, args.seconds)
        elif args.action == 'pair':
            result = asyncio.run(pair(args.token_file, args.challenge_file))
        elif args.action == 'capture':
            result = capture(args.token_file)
        else:
            result = asyncio.run(inspect(args.token_file, args.expected_username, attempts=args.attempts, timeout=args.timeout))
        print(json.dumps(result, ensure_ascii=False))
        return 2 if result['status'].startswith('blocked') else 0
    except (Exception, KeyboardInterrupt) as error:
        print(json.dumps({'status': 'blocked', 'reason': str(error) if isinstance(error, Blocked) else 'private_capture_or_inspection_failed'}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
