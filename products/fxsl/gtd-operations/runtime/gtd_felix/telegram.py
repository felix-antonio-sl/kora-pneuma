"""Durable Telegram transport. No model calls and no authority from message text.

Bot API contract: https://core.telegram.org/bots/api (checked 2026-09-11).
Run one polling receiver per bot/account. The injected service owns persistence.
"""
from __future__ import annotations

import asyncio
from contextvars import ContextVar
from weakref import WeakValueDictionary
import uuid
import hashlib
import json
import re
import math
from datetime import datetime
from zoneinfo import ZoneInfo
from dataclasses import dataclass
from typing import Any, Protocol


class TelegramError(Exception):
    """Public error codes never contain request URLs, tokens or remote bodies."""


class TelegramClient(Protocol):
    async def call(self, method: str, payload: dict) -> Any: ...
    async def download(self, file_id: str) -> bytes: ...


@dataclass(frozen=True)
class TelegramConfig:
    account: str
    owner_user_id: int
    chat_id: int
    actor: str
    poll_timeout: int = 25
    page_size: int = 5
    auto_return: bool = False

    def __post_init__(self):
        if type(self.auto_return) is not bool:
            raise ValueError('invalid_telegram_auto_return')
        if not self.account or not self.actor or self.owner_user_id <= 0 or not self.chat_id:
            raise ValueError('explicit_telegram_identity_required')
        if not 1 <= self.page_size <= 15 or not 1 <= self.poll_timeout <= 50:
            raise ValueError('invalid_telegram_limits')


class AiohttpTelegramClient:
    """Injected aiohttp-compatible session; bounded safe reads, no POST replay.

    sendMessage has no idempotency key. Its uncertain result must not trigger
    automatic HTTP retries; the adapter persists each outbound intent before dispatch.
    """
    def __init__(self, token: str, session, *, attempts: int = 3,
                 timeout: float = 60, max_file_bytes: int = 20 * 1024 * 1024):
        if not token or not 1 <= attempts <= 5 or timeout <= 0 or max_file_bytes <= 0:
            raise ValueError('invalid_telegram_client_configuration')
        self._token = token
        self.session = session
        self.attempts = attempts
        self.timeout = timeout
        self.max_file_bytes = max_file_bytes

    async def _request(self, method, url, *, payload=None, binary=False, retry=False):
        for attempt in range(self.attempts if retry else 1):
            try:
                async with self.session.request(method, url, json=payload,
                                                timeout=self.timeout) as response:
                    if response.status == 429 or response.status >= 500:
                        raise TelegramError('telegram_temporarily_unavailable')
                    if response.status != 200:
                        raise TelegramError('telegram_request_rejected')
                    if binary:
                        data = bytearray()
                        async for chunk in response.content.iter_chunked(65536):
                            data.extend(chunk)
                            if len(data) > self.max_file_bytes:
                                raise TelegramError('telegram_file_too_large')
                        return bytes(data)
                    result = await response.json()
                    if not result.get('ok'):
                        raise TelegramError('telegram_api_rejected')
                    return result['result']
            except asyncio.CancelledError:
                raise
            except Exception:
                if attempt + 1 >= (self.attempts if retry else 1):
                    raise TelegramError('telegram_request_failed') from None
                await asyncio.sleep(min(0.25 * 2 ** attempt, 2))

    async def call(self, method, payload):
        if method not in {'getUpdates', 'getFile', 'sendMessage', 'answerCallbackQuery'}:
            raise TelegramError('telegram_method_not_allowed')
        return await self._request('POST', f'https://api.telegram.org/bot{self._token}/{method}',
                                   payload=payload, retry=method in {'getUpdates', 'getFile'})

    async def download(self, file_id):
        info = await self.call('getFile', {'file_id': file_id})
        path = info.get('file_path', '')
        if (not re.fullmatch(r'[A-Za-z0-9_./-]+', path) or '..' in path.split('/')
                or path.startswith('/') or info.get('file_size', 0) > self.max_file_bytes):
            raise TelegramError('telegram_file_unavailable')
        return await self._request('GET', f'https://api.telegram.org/file/bot{self._token}/{path}',
                                   binary=True, retry=True)


ACTIONS = {'hecho': 'done', 'editar': 'edit', 'posponer': 'postpone',
           'retirar': 'withdraw', 'reabrir': 'reopen', 'deshacer': 'undo'}
LABELS = {'done': 'Hecho', 'edit': 'Editar', 'postpone': 'Posponer', 'pause': 'Pausar asunto',
          'withdraw': 'Retirar', 'reopen': 'Reabrir', 'undo': 'Deshacer'}


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                     separators=(',', ':')).encode()).hexdigest()


class TelegramAdapter:
    def __init__(self, service, client: TelegramClient, config: TelegramConfig, *, control=None, reservation_runtime_seconds=None):
        self.service, self.client, self.config = service, client, config
        self.control = control
        self.reservation_runtime_seconds = reservation_runtime_seconds
        self._tasks = {}
        self._locks = {}
        # Holders and waiters keep locks alive; completed event keys can expire.
        self._notification_locks = WeakValueDictionary()
        self._media_slots = asyncio.Semaphore(3)
        self._outbound_context = ContextVar("telegram_outbound", default=None)
        self._notification_request = ContextVar("telegram_notification_request", default=None)

    def _pending(self, provider='telegram'):
        return self.service.pending_events(provider, self.config.account)

    def _event(self, provider, external_id, payload, revision='1'):
        receipt = self.service.ingest_event({'provider': provider, 'account': self.config.account,
            'external_id': str(external_id), 'revision': str(revision), 'payload': payload})
        if receipt.get('status') == 'rejected' or not receipt.get('event_key'):
            raise TelegramError('telegram_event_not_persisted')
        return receipt

    async def poll_once(self):
        cursor = self.service.get_cursor('telegram', self.config.account)
        args = {'timeout': self.config.poll_timeout,
                'allowed_updates': ['message', 'edited_message', 'callback_query']}
        if cursor is not None:
            args['offset'] = int(cursor)
        updates = await self.client.call('getUpdates', args)
        # A failed durable write stops the batch before acknowledging that update.
        for update in sorted(updates, key=lambda value: value['update_id']):
            self._event('telegram', update['update_id'], update)
            offset = max(int(cursor or 0), update['update_id'] + 1)
            self.service.set_cursor('telegram', self.config.account, str(offset))
            cursor = str(offset)
        return len(updates)

    def schedule_pending(self):
        for event in self._pending():
            key = event['event_key']
            if key not in self._tasks or self._tasks[key].done():
                self._tasks[key] = asyncio.create_task(self._process_safe(event))
        if self.config.auto_return:
            key = 'telegram-auto-return'
            if key not in self._tasks or self._tasks[key].done():
                self._tasks[key] = asyncio.create_task(self._return_pending())
        self._tasks = {key: task for key, task in self._tasks.items() if not task.done()}

    def _question_return_basis(self, event):
        """Durable question/context, never inferred from native_reply wording."""
        with self.service.store.lock:
            item = self.service.get_item(event['payload'].get('item_id'))
            if (not item or not item.get('decision_needed')
                    or not isinstance(item.get('decision_question'), str)
                    or not item['decision_question'].strip()):
                return None
            routes = self.service.routed_human_sources(item)
            sources = [route['source_item_id'] for route in routes]
            latest = {material['id']: material for material in self.service.materials(item['id'])}
            materials = sorted({digest({key: value for key, value in material.items()
                if key not in {'id', 'version', 'created_at'}}) for material in latest.values()})
            # Status/meaning changes are useful even when produced by the principal.
            values = {key: item.get(key) for key in self.service.MEANING | {
                'status', 'due_at', 'review_at', 'decision_at', 'decision_needed', 'decision_question'}}
            assessment = (item.get('assessments') or [{}])[-1]
            assessment = {key: assessment[key] for key in {
                'actor', 'satisfied', 'evidence', 'gap', 'material_id', 'material_version',
                'source_versions', 'mandate_id'} if key in assessment}
            return digest({'item_id': item['id'], 'values': values, 'materials': materials,
                'assessment': assessment, 'result_gap': item.get('result_gap'),
                'inputs': self.service.work_input_basis(item['id'], sources),
                'routed_sources': [(r['source_item_id'], r['source_version'], r['source_revision']) for r in routes]})

    def _question_return_key(self, event):
        return 'telegram-question-return:' + digest([self.config.account, self.config.chat_id,
            self.config.owner_user_id, event['payload'].get('item_id')])

    def _material_return_key(self, event):
        return 'telegram-material-return:' + digest([self.config.account, self.config.chat_id,
            self.config.owner_user_id, self.config.actor, event['payload'].get('item_id')])

    @staticmethod
    def _material_return_identity(material):
        return digest([material['id'], material['version'], material['original']['sha256']])

    def _notification_receipt(self, event, status, reason=None, *, question_basis=None, material_keys=()):
        # This receipt is transport state; it never changes the notification's
        # original payload or asserts that the underlying GTD result is done.
        key = 'telegram-delivery:' + digest([self.config.account, event['event_key']])
        with self.service.store.transaction() as db:
            if status == 'confirmed' and material_keys:
                prior = self.service._meta(self._material_return_key(event), {})
                self.service._set_meta(self._material_return_key(event), {
                    'materials': sorted(set(prior.get('materials', [])) | set(material_keys))})
            if status == 'confirmed' and question_basis is not None:
                self.service._set_meta(self._question_return_key(event), {
                    'basis': question_basis, 'event_key': event['event_key']})
            db.execute('INSERT OR REPLACE INTO metadata VALUES(?,?)', (key, json.dumps({
                'event_key': event['event_key'], 'account': self.config.account,
                'chat_id': self.config.chat_id, 'request_event_key': self._notification_request.get(),
                'delivery_mode': 'requested' if self._notification_request.get() else 'automatic',
                'status': status, 'reason': reason})))
            db.execute("UPDATE events SET status=?,error=? WHERE event_key=? AND status NOT IN ('done','ignored','applied','rejected')",
                ('done' if status == 'confirmed' else 'ignored' if status == 'suppressed' else 'pending',
                 reason, event['event_key']))

    def _notification_sections(self, event, *, omit_materials=frozenset()):
        # Validated lead + material sections; the single source for both the
        # full chunked content and the brief summary of GUIA section 8.
        payload = event['payload']
        item = self.service.get_item(payload.get('item_id'))
        if not item or item['version'] != payload.get('version'):
            raise TelegramError('notification_obsolete')
        if payload.get('kind') == 'completed' and item.get('status') != 'done':
            raise TelegramError('notification_obsolete')
        latest = {}
        for material in self.service.materials(item['id']):
            latest[material['id']] = material
        if payload.get('kind') != 'interrupted' and any(not m.get('valid') for m in latest.values()):
            # 'interrupted' never attaches bodies (all omitted at delivery),
            # so an invalidated prior must not silence the notice itself.
            raise TelegramError('notification_material_invalid')
        return item, latest, self._notification_body(event, item, latest,
            omit_materials=omit_materials)

    # Automatic heads stay short no matter how long the principal reply is;
    # the complete return lives one tap away on Ver resultado.
    HEAD_LIMIT = 1200

    def _notification_lead(self, event, *, omit_materials=frozenset()):
        # Brief head without material bodies: what is ready/decided plus where
        # the full content lives. Capped with an explicit continuation mark so
        # a long reply is never silently cut by the transport.
        item, latest, sections = self._notification_sections(event, omit_materials=omit_materials)
        material_count = sum(1 for m in latest.values()
            if self._material_return_identity(m) not in omit_materials)
        lead = sections[0]
        if material_count:
            lead += ('\n\nHay material preparado para revisar'
                     + ('.' if material_count == 1 else f' ({material_count} piezas).')
                     + ' Usa Ver resultado para leerlo completo.')
        if len(lead) > self.HEAD_LIMIT:
            lead = lead[:self.HEAD_LIMIT].rstrip() + '\n… (continúa en Ver resultado).'
        return lead

    def _long_return_key(self, item_id):
        return 'telegram-long-return:' + digest([self.config.account, item_id])

    def _long_return(self, item):
        # Complete return stored at summary time: principal text plus version.
        # Only the current version reads; anything else falls back to the
        # materials-only content or the not-available notice.
        stored = self.service._meta(self._long_return_key(item["id"]), None)
        if not isinstance(stored, dict) or stored.get("item_version") != item["version"]:
            return None
        return stored

    def _notification_body(self, event, item, latest, *, omit_materials=frozenset()):
        payload = event['payload']
        native_reply = payload.get('native_reply')
        has_reply = isinstance(native_reply, str) and bool(native_reply.strip())
        summary = native_reply.strip() if has_reply else str(payload.get('text') or item['title'])
        sections = [summary]
        if not has_reply and item['title'] not in summary:
            sections[0] += '\n' + item['title']
        if not has_reply and item.get('decision_needed') and item.get('decision_question'):
            sections[0] += '\nDecisión pendiente: ' + item['decision_question']
        used = len(sections[0].encode())
        for material in latest.values():
            if self._material_return_identity(material) in omit_materials:
                continue
            original = material['original']
            mime = original.get('mime_type', 'text/plain').split(';', 1)[0].lower()
            if not (mime.startswith('text/') or mime in {'application/json', 'application/xml'}):
                raise TelegramError('notification_text_transport_required')
            relative = 'originals/' + original['sha256']
            if original.get('path') != relative or not re.fullmatch(r'[0-9a-f]{64}', original['sha256']):
                raise TelegramError('notification_original_unavailable')
            path = self.service.store.root / relative
            if path.is_symlink() or path.parent.is_symlink():
                raise TelegramError('notification_original_unavailable')
            with self.service.store.lock:
                registered = self.service.store.db.execute('SELECT size,relative_path FROM originals WHERE digest=?',
                    (original['sha256'],)).fetchone()
            if not registered or registered['relative_path'] != relative or registered['size'] != original['size']:
                raise TelegramError('notification_original_unavailable')
            used += original['size']
            if used > 65536 or path.stat().st_size != original['size']:
                raise TelegramError('notification_transport_limit')
            with path.open('rb') as stream:
                content = stream.read(65537)
            if len(content) != original['size']:
                raise TelegramError('notification_original_unavailable')
            if hashlib.sha256(content).hexdigest() != original['sha256']:
                raise TelegramError('notification_original_unavailable')
            try:
                text = content.decode('utf-8')
            except UnicodeDecodeError:
                raise TelegramError('notification_text_transport_required') from None
            sections.append(material['title'] + '\n' + text)
        return sections

    def _notification_content(self, event, *, omit_materials=frozenset()):
        item, latest, sections = self._notification_sections(event, omit_materials=omit_materials)
        text = '\n\n'.join(sections)
        if len(text.encode()) > 65536:
            raise TelegramError('notification_transport_limit')
        # 2000 Unicode codepoints fit within Telegram's UTF-16 message limit,
        # including supplementary characters. No material bytes are truncated.
        chunks = [text[index:index + 2000] for index in range(0, len(text), 2000)]
        return ([f'[{index + 1}/{len(chunks)}] ' + chunk for index, chunk in enumerate(chunks)]
                if len(chunks) > 1 else chunks)

    def _auto_return_allowed(self, event):
        if not self.config.auto_return or self.config.actor != self.service.owner_actor:
            return False
        if self.service.recovery_required:
            return False
        # Pin the explicitly configured owner destination. A changed config must
        # never move pending private results to another user/chat after restart.
        identity = [self.config.owner_user_id, self.config.chat_id, self.config.actor]
        with self.service.store.transaction() as db:
            key = 'telegram-return-destination:' + digest(self.config.account)
            row = db.execute('SELECT value FROM metadata WHERE key=?', (key,)).fetchone()
            if row and json.loads(row[0]) != identity:
                return False
            if not row:
                db.execute('INSERT INTO metadata VALUES(?,?)', (key, json.dumps(identity)))
            attention = self.service._meta('attention', {'paused': False, 'notify': True})
        if attention.get('paused') or not attention.get('notify', True):
            return False
        item = self.service.get_item(event['payload'].get('item_id'))
        if not item or self.service.work_paused(item['id']):
            return False
        payload = event['payload']
        if payload.get('kind') in {'no_domain_progress', 'routed'}:
            return False
        if payload.get('kind') == 'interrupted':
            # A guard-stopped attempt with no domain progress is worth one
            # honest return; paused/attention/item guards above still apply.
            return True
        reply = payload.get('native_reply')
        return bool((isinstance(reply, str) and reply.strip()) or self.service.materials(item['id'])
                    or (item.get('decision_needed') and item.get('decision_question')))

    async def _return_pending(self):
        # One pass, at most ten deliverable results. Blocked or uncertain events
        # do not hide later useful returns; their durable state remains available.
        attempted = 0
        for event in self.service.pending_events('gtd-notification', 'local'):
            if await self._deliver_notification(event, automatic=True):
                attempted += 1
                if attempted == 10:
                    break

    async def _deliver_notification(self, event, *, automatic=False):
        key = event['event_key']
        async with self._notification_locks.setdefault(
                'item:' + str(event['payload'].get('item_id', key)), asyncio.Lock()):
            # Both the command and the automatic worker can hold old snapshots.
            with self.service.store.lock:
                row = self.service.store.db.execute('SELECT status FROM events WHERE event_key=?', (key,)).fetchone()
            if not row or row[0] in {'done', 'ignored', 'applied', 'rejected'}:
                return False
            if automatic:
                if not self._auto_return_allowed(event):
                    return False
            elif not self._notification_request.get():
                return False
            return await self._deliver_notification_locked(event, automatic=automatic)

    async def _deliver_notification_locked(self, event, *, automatic):
        key = event['event_key']
        token = self._outbound_context.set([key, 0])
        try:
            if self.config.actor != self.service.owner_actor:
                self._notification_receipt(event, 'pending', 'notification_owner_transport_required')
                return
            if self.service.recovery_required:
                self._notification_receipt(event, 'pending', 'telegram_reconciliation_required')
                return
            intents = self._outbox_intents()
            if event.get('error') == 'notification_delivery_uncertain' or any(
                    intent.get('event') == key
                    and intent.get('status') != 'confirmed' for intent in intents):
                return False
            with self.service.store.lock:
                latest = {m['id']: m for m in self.service.materials(event['payload'].get('item_id'))}
                material_keys = {self._material_return_identity(m) for m in latest.values()}
                confirmed_materials = self.service._meta(self._material_return_key(event), {}).get('materials', [])
            if event['payload'].get('kind') == 'interrupted':
                # Prior materials stay referenced by the item, never attached
                # as if this attempt had produced them; the text names the count.
                omitted = frozenset(self._material_return_identity(m) for m in latest.values())
            else:
                omitted = frozenset(confirmed_materials) if automatic else frozenset()
            chunks = self._notification_content(event, omit_materials=omitted)
            question_basis = self._question_return_basis(event)
            with self.service.store.lock:
                delivered = self.service._meta(self._question_return_key(event), {})
            if automatic and question_basis is not None and delivered.get('basis') == question_basis:
                self._notification_receipt(event, 'suppressed', 'question_already_delivered')
                return False
            # Long returns (5+ chunks) arrive as a brief head with the full
            # content one tap away; shorter multipart keeps inline per-segment
            # delivery with pause/resume without repeats (pinned regressions).
            if automatic and len(chunks) > 4:
                return await self._deliver_long_summary(event, question_basis, omitted)
            for index, chunk in enumerate(chunks):
                # Earlier sends yield to other work. Revalidate before each new
                # effect; a correction during a multipart delivery stops the rest.
                self._notification_content(event, omit_materials=omitted)
                if automatic and not self._auto_return_allowed(event):
                    return False
                options = {}
                if automatic and index == len(chunks) - 1:
                    options['reply_markup'] = {'inline_keyboard': [[
                        self._button('Ver asunto', {'action': 'show', 'item_id': event['payload']['item_id']}),
                        *([self._button('Pausar este asunto', {'action': 'pause',
                            'item_id': event['payload']['item_id'], 'expected_version': event['payload']['version']})]
                          if self.service.get_item(event['payload']['item_id'])['status'] not in {'done', 'withdrawn', 'paused'} else [])]]}
                response = await self._send(chunk, **options)
                if not isinstance(response, dict) or not response.get('message_id'):
                    self._notification_receipt(event, 'uncertain', 'notification_delivery_uncertain')
                    return True
            self._notification_receipt(event, 'confirmed', question_basis=question_basis,
                                       material_keys=material_keys - omitted)
            return True
        except asyncio.CancelledError:
            raise
        except TelegramError as error:
            reason = str(error)
            self._notification_receipt(event, 'suppressed' if reason in {
                'notification_obsolete', 'notification_material_invalid'} else 'pending', reason)
        except Exception:
            # The outbox still owns any dispatch uncertainty if this receipt
            # failed. Reprocessing consults that outbox before any network call.
            try:
                self._notification_receipt(event, 'pending', 'notification_delivery_unavailable')
            except Exception:
                pass
        finally:
            self._outbound_context.reset(token)

    async def _deliver_long_summary(self, event, question_basis, omit_materials):
        # GUIA section 8: a long automatic return arrives as a brief head; the
        # full content stays one tap away on Ver resultado (show_result sends
        # the complete chunks on request). Single send with the same
        # revalidation and uncertainty rules as full chunks; materials are NOT
        # marked delivered so the full text keeps its meaning.
        self._notification_content(event, omit_materials=omit_materials)
        if not self._auto_return_allowed(event):
            return False
        item_id = event['payload']['item_id']
        payload = event['payload']
        self.service._set_meta(self._long_return_key(item_id), {
            'item_id': item_id, 'item_version': payload.get('version'),
            'event_key': event['event_key'],
            'native_reply': payload.get('native_reply') if isinstance(
                payload.get('native_reply'), str) else None,
            'text': payload.get('text')})
        buttons = [[self._button('Ver resultado', {'action': 'result', 'item_id': item_id}),
                    self._button('Ver asunto', {'action': 'show', 'item_id': item_id})]]
        current = self.service.get_item(item_id)
        if current and current['status'] not in {'done', 'withdrawn', 'paused'}:
            buttons[0].append(self._button('Pausar este asunto', {'action': 'pause',
                'item_id': item_id, 'expected_version': event['payload']['version']}))
        response = await self._send(self._notification_lead(event, omit_materials=omit_materials),
                                    reply_markup={'inline_keyboard': buttons})
        if not isinstance(response, dict) or not response.get('message_id'):
            self._notification_receipt(event, 'uncertain', 'notification_delivery_uncertain')
            return True
        self._notification_receipt(event, 'confirmed', question_basis=question_basis,
                                   material_keys=())
        return True

    async def process_pending(self):
        """One bounded retry pass; useful for recovery and deterministic tests."""
        self.schedule_pending()
        if self._tasks:
            await asyncio.gather(*list(self._tasks.values()))

    async def run(self, stop: asyncio.Event):
        async def worker():
            while not stop.is_set():
                self.schedule_pending()
                try:
                    await asyncio.wait_for(stop.wait(), 1)
                except TimeoutError:
                    pass
        worker_task = asyncio.create_task(worker())
        try:
            while not stop.is_set():
                try:
                    await self.poll_once()
                except TelegramError:
                    try:
                        await asyncio.wait_for(stop.wait(), 2)
                    except TimeoutError:
                        pass
        finally:
            worker_task.cancel()
            for task in self._tasks.values():
                task.cancel()
            await asyncio.gather(worker_task, *self._tasks.values(), return_exceptions=True)

    def _authorized(self, update):
        callback = update.get('callback_query')
        message = (callback or {}).get('message') or update.get('message') or update.get('edited_message') or {}
        sender = (callback or message).get('from', {})
        return (sender.get('id') == self.config.owner_user_id and not sender.get('is_bot', False)
                and message.get('chat', {}).get('id') == self.config.chat_id
                and not message.get('sender_chat'))

    async def _process_safe(self, event):
        key, update = event['event_key'], event['payload']
        context_token = self._outbound_context.set([key, 0])
        try:
            if not self._authorized(update):
                self.service.mark_event(key, 'ignored')
                return
            message = update.get('message') or update.get('edited_message') or {}
            identity = str(message.get('message_id', key))
            async with self._locks.setdefault(identity, asyncio.Lock()):
                if 'callback_query' in update:
                    if getattr(self.service, 'recovery_required', False):
                        raise TelegramError('telegram_reconciliation_required')
                    await self._callback(update['callback_query'])
                else:
                    await self._message(message, key, edited='edited_message' in update)
                self.service.mark_event(key, 'applied')
        except asyncio.CancelledError:
            raise
        except Exception:
            self.service.mark_event(key, 'failed', 'telegram_processing_failed')
        finally:
            self._outbound_context.reset(context_token)

    def _delivery_id(self, identity):
        return 'tg:' + digest([self.config.account, identity])

    def _delivery_event_item(self, event_key):
        row = self.service.store.db.execute(
            'SELECT payload FROM events WHERE event_key=?', (event_key,)).fetchone()
        if not row:
            return None, None
        try:
            payload = json.loads(row[0])
        except ValueError:
            return None, None
        item_id = payload.get('item_id')
        version = payload.get('version')
        if not isinstance(item_id, str) or not self.service.get_item(item_id):
            return None, None
        return item_id, version if type(version) is int and version > 0 else None

    def _outbox_intents(self):
        # Single authoritative read of live send intents; scoped per account
        # and unfinished state, with only the columns each caller needs
        # (confirmed history is never decoded here).
        with self.service.store.lock:
            rows = self.service.store.db.execute(
                "SELECT state, payload_json FROM deliveries WHERE channel='telegram'"
                " AND target_key=? AND state != 'confirmed'", (self.config.account,)).fetchall()
        intents = []
        for row in rows:
            try:
                payload = json.loads(row["payload_json"])
            except ValueError:
                continue
            intents.append({'event': payload.get('event'), 'account': self.config.account,
                            'status': row["state"]})
        return intents

    async def _call(self, method, payload):
        if method in {'sendMessage', 'answerCallbackQuery'} and getattr(self.service, 'recovery_required', False):
            raise TelegramError('telegram_reconciliation_required')
        if method not in {'sendMessage', 'answerCallbackQuery'}:
            return await self.client.call(method, payload)
        context = self._outbound_context.get()
        if context is None:
            # Calls outside event processing represent a new explicit UI request.
            identity = [str(uuid.uuid4()), 0]
        else:
            identity = [context[0], context[1]]
            context[1] += 1
        key = self._delivery_id(identity)
        store = self.service.store
        with store.transaction():
            row = store.db.execute(
                'SELECT state, segments_json FROM deliveries WHERE id=?', (key,)).fetchone()
            if row:
                if row["state"] == 'confirmed':
                    try:
                        segments = json.loads(row["segments_json"])
                    except ValueError:
                        segments = []
                    # Preserve the original output even if replay sees newer domain state.
                    for segment in segments:
                        if "response" in segment:
                            return segment['response']
                return {}
            item_id, item_version = self._delivery_event_item(identity[0])
            store.db.execute(
                'INSERT INTO deliveries(id, item_id, item_version, channel, target_key, semantic_key,'
                ' state, payload_json, segments_json, created_at, retry_at, confirmed_at)'
                ' VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',
                (key, item_id, item_version, 'telegram', self.config.account,
                 str(identity[0]) + ':' + str(identity[1]), 'pending',
                 json.dumps({'method': method, 'payload': payload, 'event': identity[0],
                             'ordinal': identity[1], 'account': self.config.account}),
                 '[]', datetime.now().isoformat(), None, None))
        # A durable dispatch marker precedes the network call. A crash here is
        # conservatively uncertain: Telegram supplies no sendMessage idempotency.
        with store.transaction():
            store.db.execute("UPDATE deliveries SET state='uncertain' WHERE id=?", (key,))
        try:
            response = await self.client.call(method, payload)
        except asyncio.CancelledError:
            raise
        except Exception:
            return {}
        with store.transaction():
            store.db.execute("UPDATE deliveries SET state='confirmed', segments_json=?, confirmed_at=?"
                             " WHERE id=?",
                             (json.dumps([{'status': 'confirmed', 'response': response}]),
                              datetime.now().isoformat(), key))
        return response

    async def _send(self, text, **kwargs):
        return await self._call('sendMessage', {'chat_id': self.config.chat_id,
                                                      'text': text[:4096], **kwargs})

    def _token(self, payload):
        token = 'g1:' + digest(payload)[:32]
        self._event('telegram-ui', token, payload)
        return token

    def _lookup(self, token):
        if not isinstance(token, str) or not re.fullmatch(r'g1:[0-9a-f]{32}', token):
            return None
        return next((e['payload'] for e in self._pending('telegram-ui')
                     if e['external_id'] == token), None)

    def _button(self, text, payload):
        return {'text': text, 'callback_data': self._token(payload)}

    async def show_item(self, item, operation_id=None, more=False):
        item = self.service.get_item(item['id'])
        if not item:
            await self._send('El asunto ya no está disponible.')
            return
        base = {'item_id': item['id'], 'expected_version': item['version']}
        terminal = item['status'] in {'done', 'withdrawn'}
        paused = item['status'] == 'paused'
        actions = ['edit', 'postpone', 'withdraw'] if more else ['reopen'] if terminal or paused else ['done']
        buttons = [self._button('Retomar' if paused and action == 'reopen' else LABELS[action],
                               {**base, 'action': action}) for action in actions]
        if operation_id and (more or terminal):
            buttons.append(self._button('Deshacer', {**base, 'action': 'undo',
                                                    'fields': {'operation_id': operation_id}}))
        if not more:
            buttons.append(self._button('Más', {**base, 'action': 'more', 'operation_id': operation_id}))
        if not terminal and not paused:
            if not more:
                buttons.append(self._button(LABELS['pause'], {**base, 'action': 'pause'}))
            if more:
                buttons.append(self._button('Revisar ahora', {**base, 'action': 'request_review'}))
        rows = [buttons[index:index + 3] for index in range(0, len(buttons), 3)]
        if self.service.materials(item['id']):
            rows.append([self._button('Ver resultado', {'action': 'result', 'item_id': item['id']})])
        def excerpt(value):
            if sum(2 if ord(char) > 0xffff else 1 for char in value) <= 700:
                return value
            marker = '… [texto recortado]'
            remaining = 700 - len(marker)
            prefix = []
            for char in value:
                remaining -= 2 if ord(char) > 0xffff else 1
                if remaining < 0:
                    break
                prefix.append(char)
            return ''.join(prefix) + marker

        states = {'active': 'En curso', 'done': 'Terminado', 'withdrawn': 'Retirado',
                  'postponed': 'Para después', 'waiting': 'En espera', 'paused': 'En pausa'}
        lines = [excerpt(item['title']), states.get(item['status'], item['status'])]
        if not terminal:
            if item.get('decision_needed') and item.get('decision_question'):
                lines.append('Pregunta pendiente: ' + excerpt(item['decision_question']))
            if (item['status'] in {'active', 'waiting'} and
                    (item['kind'] == 'waiting' or item['status'] == 'waiting') and item.get('waiting_for')):
                lines.append('En espera de: ' + excerpt(item['waiting_for']))
            for field, label in (('review_at', 'Revisar'), ('decision_at', 'Decidir'), ('due_at', 'Límite')):
                if item.get(field):
                    lines.append(label + ': ' + excerpt(item[field]))
        if more:
            lines.append(f"Comandos: {item['id']}@{item['version']}")
        await self._send('\n'.join(lines),
                         reply_markup={'inline_keyboard': rows})

    async def show_result(self, item_id):
        # An explicit read is independent of notification acknowledgement. Reuse
        # the verified content reader, never revive or consume an outbox event.
        if self.config.actor != self.service.owner_actor:
            await self._send('Esta consulta requiere el acceso del propietario.')
            return
        item = self.service.get_item(item_id)
        stored = self._long_return(item) if item else None
        if not item or (not self.service.materials(item_id) and not stored):
            await self._send('Este asunto todavía no tiene un resultado preparado.')
            return
        payload = {'item_id': item_id, 'version': item['version'],
                   'text': stored.get('text') or 'Resultado disponible' if stored else 'Resultado disponible'}
        if stored and stored.get('native_reply'):
            payload['native_reply'] = stored['native_reply']
        event = {'payload': payload}
        try:
            chunks = self._notification_content(event)
            for chunk in chunks:
                self._notification_content(event)
                await self._send(chunk)
        except TelegramError as error:
            if str(error) not in {'notification_obsolete', 'notification_material_invalid',
                    'notification_text_transport_required', 'notification_original_unavailable',
                    'notification_transport_limit'}:
                raise
            await self._send('El resultado necesita revisión o no puede mostrarse en este formato. '
                             'No lo presento como vigente; el asunto se conserva.')

    async def _attention(self, paused, operation_id):
        receipt = self.service.execute(self.config.actor, {'operation_id': operation_id,
            'action': 'set_attention', 'fields': {'paused': paused}})
        if receipt['status'] not in {'applied', 'already_applied'}:
            await self._report(receipt)
            return
        text = ('Avisos en pausa. Puedes seguir dejando asuntos y consultar lo preparado.'
                if paused else 'Pausa de avisos levantada. Conservo tus preferencias de notificación.')
        buttons = [[self._button('Reanudar avisos', {'action': 'attention', 'paused': False})]] if paused else []
        await self._send(text, reply_markup={'inline_keyboard': buttons})

    async def show_list(self, page=0, filters=None, *, selecting=False, selected=None, view="affairs"):
        filters = {'open': True} if filters is None else filters
        selected = selected or []
        if view not in {'affairs', 'sources', 'all'}:
            raise TelegramError('telegram_invalid_list_view')
        # Linked source affairs come from the queryable authority, even after
        # a source revision or human edit changes the item's current metadata.
        with self.service.store.lock:
            rows = self.service.store.db.execute(
                'SELECT DISTINCT item_id FROM source_entries WHERE item_id IS NOT NULL').fetchall()
        source_ids = {row[0] for row in rows}
        all_items = self.service.query()
        selected_sources = {source_id for item in all_items if item['kind'] != 'capture'
                            for source_id in item.get('source_versions', {})}
        def unselected_source(item):
            return (item['id'] in source_ids and item['kind'] == 'capture'
                    and item['id'] not in selected_sources and not item.get('clarification'))
        items = sorted((item for item in self.service.query(filters)
                        if view == 'all' or (view == 'sources' and item['id'] in source_ids)
                        or (view == 'affairs' and item['kind'] != 'reference' and not unselected_source(item))),
                       key=lambda item: (item['kind'], item['status'], item['id']))
        size = self.config.page_size
        pages = max(1, (len(items) + size - 1) // size)
        page = min(max(0, page), pages - 1)
        visible = items[page * size:(page + 1) * size]
        state = {'page': page, 'filters': filters, 'selecting': selecting, 'selected': selected, 'view': view}
        label = {'affairs': 'Asuntos', 'sources': 'Fuentes sincronizadas', 'all': 'Inventario completo'}[view]
        scope = 'abiertos' if filters.get('open') else 'consulta'
        heading = f"{label} · {len(items)}" + (' registros' if view != 'affairs' else '')
        lines = [heading + (f" · página {page + 1}/{pages}" if pages > 1 else '')]
        if selecting:
            lines.append(f"{len(selected)}/15 seleccionados")
        buttons, group = [], None
        for item in visible:
            current_group = (item['kind'], item['status'])
            if current_group != group:
                kinds = {'capture': 'Por aclarar', 'proposed_entry': 'Por revisar', 'project': 'Proyectos',
                         'action': 'Acciones', 'possibility': 'Posibilidades', 'reference': 'Referencias',
                         'waiting': 'Esperas', 'responsibility': 'Responsabilidades', 'calendar': 'Agenda', 'material': 'Materiales'}
                lines.append(kinds.get(item['kind'], 'Asuntos'))
                group = current_group
            lines.append(item['title'][:180])
            if selecting:
                marked = any(target['item_id'] == item['id'] for target in selected)
                buttons.append([self._button(('☑ ' if marked else '☐ ') + item['title'][:45],
                    {**state, 'action': 'select', 'item_id': item['id'], 'expected_version': item['version']})])
            else:
                buttons.append([self._button(item['title'][:50] or 'Abrir', {'action': 'show', 'item_id': item['id']})])
        nav = [self._button(label, {**state, 'action': 'list', 'page': target})
               for label, target in [('Anterior', page - 1), ('Siguiente', page + 1)] if 0 <= target < pages]
        if nav:
            buttons.append(nav)
        if selecting:
            if selected:
                buttons.append([self._button('Hecho', {'action': 'batch_done', 'targets': selected}),
                                self._button('Posponer', {'action': 'batch_postpone', 'targets': selected})])
            buttons.append([self._button('Salir de selección', {**state, 'action': 'list', 'selecting': False, 'selected': []})])
        else:
            buttons.append([self._button('Seleccionar varios', {**state, 'action': 'list', 'selecting': True})])
        buttons.append([self._button(label, {'action': 'list', 'page': 0,
            'filters': {'open': True} if target == 'affairs' else {}, 'view': target})
            for target, label in [('affairs', 'Asuntos'), ('sources', 'Fuentes'), ('all', 'Inventario')]
            if target != view])
        await self._send('\n'.join(lines), reply_markup={'inline_keyboard': buttons})
        return visible

    async def _batch(self, targets, action, operation_id, fields=None):
        if not 1 <= len(targets) <= 15:
            raise TelegramError('telegram_invalid_selection')
        receipts = [self.service.execute(self.config.actor, {**target, 'action': action,
            'operation_id': operation_id + ':' + str(index), 'fields': fields or {}})
            for index, target in enumerate(targets)]
        for receipt in receipts:
            await self._report(receipt)
        applied = sum(receipt['status'] in {'applied', 'already_applied'} for receipt in receipts)
        await self._send(f"Lote: {applied}/{len(receipts)} aplicados; {len(receipts) - applied} sin aplicar.")

    async def _report(self, receipt):
        status = receipt['status']
        if status in {'applied', 'already_applied'} and receipt.get('item'):
            await self.show_item(receipt['item'], receipt['operation_id'])
        elif status == 'conflict':
            names = {'title': 'Asunto', 'status': 'Estado', 'kind': 'Tipo', 'review_at': 'Retorno',
                     'outcome': 'Resultado', 'executor': 'Responsable', 'project_id': 'Proyecto',
                     'completion_criteria': 'Criterio de cierre', 'depends_on': 'Dependencias'}
            lines = ['Cambió desde esta ficha. Se conserva el estado actual:']
            for key, change in receipt.get('difference', {}).items():
                value = change.get('current')
                rendered = str(value)[:300] if isinstance(value, (str, int, float)) else 'actualizado'
                lines.append(f"{names.get(key, 'Campo modificado')}: {rendered}")
            await self._send('\n'.join(lines))
            if receipt.get('item'):
                await self.show_item(receipt['item'])
        else:
            reasons = {'item_not_found': 'El asunto ya no está disponible. Abre /lista.',
                'kind_not_completable': 'Esta entrada aún no es una acción o resultado comprometido. Puedes aclararla o retirarla.',
                'invalid_date_or_timezone': 'Usa una fecha AAAA-MM-DD o fecha y hora con zona.',
                'review_at_required': 'Indica una fecha de retorno AAAA-MM-DD.',
                'operation_not_undoable': 'Esa operación no se puede deshacer. Revisa la ficha vigente.',
                'already_open': 'El asunto ya está abierto.',
                'terminal_item': 'Reabre el asunto antes de posponerlo.',
                'storage_unavailable': 'El registro no está disponible. La entrada queda pendiente para reintento.'}
            prefix = 'No pude confirmar el cambio. ' if status == 'uncertain' else 'No se aplicó el cambio. '
            await self._send(prefix + reasons.get(receipt.get('error'), 'Abre /lista y revisa la ficha antes de reintentar.'))
        if status == 'uncertain':
            raise TelegramError('telegram_service_write_uncertain')

    async def _callback(self, callback):
        payload = self._lookup(callback.get('data'))
        if payload is None:
            await self._call('answerCallbackQuery', {'callback_query_id': callback['id'],
                                                           'text': 'Control no vigente. Abre /lista.'})
            return
        await self._call('answerCallbackQuery', {'callback_query_id': callback['id']})
        action = payload['action']
        if action == 'list':
            await self.show_list(payload['page'], payload['filters'], selecting=payload.get('selecting', False), selected=payload.get('selected'), view=payload.get('view', 'affairs'))
        elif action == 'select':
            selected = list(payload['selected'])
            if any(target['item_id'] == payload['item_id'] for target in selected):
                selected = [target for target in selected if target['item_id'] != payload['item_id']]
            elif len(selected) < 15:
                selected.append({'item_id': payload['item_id'], 'expected_version': payload['expected_version']})
            await self.show_list(payload['page'], payload['filters'], selecting=True, selected=selected, view=payload.get('view', 'affairs'))
        elif action == 'batch_done':
            await self._batch(payload['targets'], 'done', 'tg-batch:' + callback['id'])
        elif action == 'batch_postpone':
            sent = await self._send('Escribe la fecha de retorno para los seleccionados (AAAA-MM-DD).', reply_markup={'force_reply': True, 'selective': True})
            if sent and sent.get('message_id'):
                self._event('telegram-prompt', sent['message_id'], payload)
        elif action == 'more':
            item = self.service.get_item(payload['item_id'])
            if item:
                await self.show_item(item, payload.get('operation_id'), more=True)
        elif action == 'show':
            item = self.service.get_item(payload['item_id'])
            if item:
                await self.show_item(item)
        elif action == 'result':
            await self.show_result(payload['item_id'])
        elif action == 'pause':
            current = self.service.get_item(payload['item_id'])
            if current and current['status'] == 'paused':
                await self.show_item(current)
            elif current:
                await self._report(self.service.execute(self.config.actor, {**payload,
                    'expected_version': current['version'], 'operation_id': 'tg-callback:' + callback['id']}))
            else:
                await self._send('El asunto ya no está disponible.')
        elif action == 'attention':
            await self._attention(payload['paused'], 'tg-attention-callback:' + callback['id'])
        elif action in {'edit', 'postpone'}:
            prompt = 'Escribe el nuevo texto.' if action == 'edit' else 'Escribe la fecha de retorno (AAAA-MM-DD).'
            sent = await self._send(prompt, reply_markup={'force_reply': True, 'selective': True})
            if sent and sent.get('message_id'):
                self._event('telegram-prompt', sent['message_id'], payload)
        else:
            await self._report(self.service.execute(self.config.actor,
                {**payload, 'operation_id': 'tg-callback:' + callback['id']}))

    def _budget_view(self):
        if self.control is None:
            raise ValueError('budget_unavailable')
        budget = self.control.budget()
        for field in ('remaining_runtime_seconds', 'active'):
            value = budget.get(field)
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
                raise ValueError('invalid_budget_read')
        renewal = 'No hay renovación automática informada.'
        if budget.get('returns_at'):
            instant = datetime.fromisoformat(budget['returns_at'])
            if instant.utcoffset() is None:
                raise ValueError('invalid_budget_renewal')
            zone = self.control.config.get('timezone')
            if zone:
                instant = instant.astimezone(ZoneInfo(zone))
            renewal = 'El tiempo diario se renueva el ' + instant.strftime('%d/%m a las %H:%M')
            label = 'hora de Santiago' if zone == 'America/Santiago' else zone
            renewal += (' (' + label + ').') if label else instant.strftime(' (UTC%z).')
        return budget, renewal

    async def _show_budget(self):
        try:
            budget, renewal = self._budget_view()
            minutes = budget['remaining_runtime_seconds'] / 60
            available = 'menos de 1' if 0 < minutes < 1 else str(math.floor(minutes))
            text = 'Tiempo disponible para preparar: ' + available + ' min. ' + renewal
            if budget['active'] > 0:
                text += ' El turno está ocupado o pendiente de confirmar; no puedo iniciar otra preparación todavía.'
            elif (self.reservation_runtime_seconds is not None
                    and budget['remaining_runtime_seconds'] < self.reservation_runtime_seconds):
                text += ' El saldo no alcanza para iniciar otra preparación.'
            text += ' La renovación no garantiza una hora de inicio.'
        except Exception:
            text = 'No pude consultar el saldo de ejecución. Tus capturas se conservan; no puedo confirmar cuándo habrá capacidad.'
        await self._send(text)

    def _capture_ack(self, text):
        if self.control is None:
            return text
        try:
            budget, renewal = self._budget_view()
            if budget['active'] > 0:
                return text + ' Hay una preparación en curso o por confirmar; esta entrada queda pendiente.'
            if (self.reservation_runtime_seconds is not None
                    and budget['remaining_runtime_seconds'] < self.reservation_runtime_seconds):
                return text + ' Queda pendiente: el saldo no alcanza para otra preparación. ' + renewal + ' No implica inicio automático.'
        except Exception:
            return text + ' No pude consultar el saldo; la preparación queda pendiente de comprobar capacidad.'
        return text

    async def _message(self, message, key, edited=False):
        text = message.get('text', message.get('caption', ''))
        forwarded = any(name in message for name in ('forward_origin', 'forward_from', 'forward_sender_name'))
        # Forwarded commands are source material, never executable instructions.
        if not edited and not forwarded:
            if text.split(maxsplit=1) and text.split(maxsplit=1)[0].lower() == '/saldo':
                await self._command(text, key)
                return
            if getattr(self.service, 'recovery_required', False) and (text.startswith('/') or message.get('reply_to_message')):
                raise TelegramError('telegram_reconciliation_required')
            reply = message.get('reply_to_message', {}).get('message_id')
            prompt = next((event['payload'] for event in self._pending('telegram-prompt')
                           if str(event['external_id']) == str(reply)), None) if reply else None
            if prompt:
                if prompt['action'] == 'batch_postpone':
                    await self._batch(prompt['targets'], 'postpone', 'tg-batch-reply:' + key, {'review_at': text.strip()})
                    return
                fields = {'title': text} if prompt['action'] == 'edit' else {'review_at': text.strip()}
                await self._report(self.service.execute(self.config.actor,
                    {**prompt, 'fields': fields, 'operation_id': 'tg-reply:' + key}))
                return
            if text.startswith('/'):
                if await self._command(text, key):
                    return
        source = {'provider': 'telegram', 'account': self.config.account,
                  'chat_id': message['chat']['id'], 'message_id': message['message_id'],
                  'date': message.get('date'), 'edit_date': message.get('edit_date'),
                  'revision': str(message.get('edit_date', message.get('date', 0))),
                  'forward_origin': message.get('forward_origin'),
                  'original_message': message}
        existing = next((item for item in self.service.query() if all(
            item.get('source', {}).get(name) == source[name]
            for name in ('provider', 'account', 'chat_id', 'message_id'))), None)
        media = message.get('voice') or message.get('document')
        original = None
        if media and (edited or not existing):
            async with self._media_slots:
                original = await self.client.download(media['file_id'])
        filename = (media or {}).get('file_name', 'voice.ogg' if message.get('voice') else None)
        if filename is not None:
            filename = filename.replace('\\', '/').rsplit('/', 1)[-1].replace('\x00', '')
            if filename in {'', '.', '..'}:
                filename = 'original.bin'
        mime_type = (media or {}).get('mime_type')
        if existing:
            if edited:
                receipt = self.service.revise_source(self.config.actor, 'tg-edit:' + key,
                    existing['id'], source, text=text, original=original,
                    filename=filename, mime_type=mime_type)
                if receipt['status'] not in {'applied', 'already_applied'}:
                    await self._report(receipt)
                    return
                self._event('gtd-clarification', key, {'item_id': existing['id'],
                    'event_key': key, 'reason': 'source_revision'})
                await self._send(self._capture_ack('Guardado: edición de la fuente. Tus decisiones se conservan.'))
            else:
                self._event('gtd-clarification', key, {'item_id': existing['id'],
                    'event_key': key, 'reason': 'voice_transcription_pending' if message.get('voice') else 'clarification_pending'})
                await self._send(self._capture_ack('Guardado.'))
            return
        receipt = self.service.capture(self.config.actor,
            'tg-message:' + digest([self.config.account, source['chat_id'], source['message_id']]),
            text or ('Audio' if message.get('voice') else 'Documento'), source=source,
            original=original, filename=filename, mime_type=mime_type)
        if receipt['status'] not in {'applied', 'already_applied'}:
            await self._report(receipt)
            return
        self._event('gtd-clarification', key, {'item_id': receipt['item']['id'],
                    'event_key': key, 'reason': 'voice_transcription_pending' if message.get('voice') else 'clarification_pending'})
        await self._send(self._capture_ack('Guardé el audio; transcripción pendiente.' if message.get('voice') else
                         'Guardado.'))

    async def _command(self, text, key):
        parts = text.split(maxsplit=2)
        name = parts[0][1:].lower()
        if name == 'saldo':
            await self._show_budget()
            return True
        if name in {'pausa', 'reanudar'}:
            if len(parts) != 1:
                await self._send('Usa /pausa para pausar avisos o /reanudar para levantar la pausa.')
            else:
                await self._attention(name == 'pausa', 'tg-attention:' + key)
            return True
        if name == 'preparado':
            events = self.service.pending_events('gtd-notification', 'local')
            if not events:
                await self._send('No hay devoluciones pendientes de entrega.')
                return True
            # Select by durable event identity, not a mutable page offset.
            # Blocked returns remain pending but do not consume delivery slots.
            uncertain = {intent['event'] for intent in self._outbox_intents()
                if intent.get('status') != 'confirmed'}
            request_token = self._notification_request.set(key)
            attempted, suppressed = 0, 0
            try:
                for event in events:
                    if event['event_key'] in uncertain or event.get('error') == 'notification_delivery_uncertain':
                        continue
                    try:
                        self._notification_content(event)
                    except TelegramError as error:
                        reason = str(error)
                        stale = reason in {'notification_obsolete', 'notification_material_invalid'}
                        self._notification_receipt(event, 'suppressed' if stale else 'pending', reason)
                        suppressed += int(stale)
                        continue
                    except Exception:
                        self._notification_receipt(event, 'pending', 'notification_delivery_unavailable')
                        continue
                    await self._deliver_notification(event)
                    attempted += 1
                    if attempted == 10:
                        break
            finally:
                self._notification_request.reset(request_token)
            if suppressed:
                await self._send(f'Omití {suppressed} devoluciones antiguas o con material inválido. El registro conserva el estado vigente.')
            remaining = self.service.pending_events('gtd-notification', 'local')
            if remaining:
                uncertain_count = sum(e['event_key'] in uncertain or e.get('error') ==
                    'notification_delivery_uncertain' for e in remaining)
                blocked_count = sum(bool(e.get('error')) and e['event_key'] not in uncertain and
                    e.get('error') != 'notification_delivery_uncertain' for e in remaining)
                awaiting = len(remaining) - uncertain_count - blocked_count
                detail = (f' {uncertain_count} con envío incierto, sin reintento automático;' if uncertain_count else '')
                detail += (f' {blocked_count} requieren otro transporte o comprobación;' if blocked_count else '')
                detail += (f' {awaiting} por consultar: usa /preparado para continuar.' if awaiting else '')
                await self._send(f'Quedan {len(remaining)} devoluciones pendientes.' + detail)
            return True
        if name in {'lista', 'abiertos', 'fuentes', 'inventario'}:
            await self.show_list(int(parts[1]) - 1 if len(parts) > 1 and parts[1].isdigit() else 0,
                filters=None if name in {'lista', 'abiertos'} else {},
                view={'fuentes': 'sources', 'inventario': 'all'}.get(name, 'affairs'))
            return True
        if name not in ACTIONS:
            return False
        action = ACTIONS[name]
        try:
            targets = parts[1].split(',')
            if not 1 <= len(targets) <= 15:
                raise ValueError()
            commands = []
            for target in targets:
                item_id, version = target.rsplit('@', 1)
                fields = {}
                if action == 'edit':
                    fields = {'title': parts[2]}
                elif action == 'postpone':
                    fields = {'review_at': parts[2]}
                elif action == 'undo':
                    fields = {'operation_id': parts[2]}
                commands.append({'operation_id': 'tg-command:' + key + ':' + str(len(commands)),
                    'action': action, 'item_id': item_id, 'expected_version': int(version), 'fields': fields})
        except (ValueError, IndexError):
            await self._send('Usa /' + name + ' id@versión[,id@versión]'
                             + (' texto' if action == 'edit' else ' AAAA-MM-DD' if action == 'postpone' else
                                ' operación' if action == 'undo' else '') + ' (máximo 15).')
            return True
        receipts = [self.service.execute(self.config.actor, command) for command in commands]
        for receipt in receipts:
            await self._report(receipt)
        return True
