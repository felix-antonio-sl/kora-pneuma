"""Explicitly connected, identity-bound Google read transport; no credential writes."""
import asyncio
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import stat
from urllib.parse import quote

import aiohttp

from .google_sources import canonical_gmail_query
from .source_error_codes import TransportError

GMAIL = 'https://gmail.googleapis.com/gmail/v1/users/me'
OIDC = 'https://openidconnect.googleapis.com/v1/userinfo'
TOKEN = 'https://oauth2.googleapis.com/token'
# Only a stable, secret-free error code crosses the transport boundary
# (TransportError itself lives in source_error_codes; re-exported here).


class GoogleTransport:
    def __init__(self, config, *, session_factory=None):
        allowed = {'account', 'token_file', 'gmail', 'calendar_ids', 'identity_method',
                   'timeout_seconds', 'max_response_bytes'}
        if not isinstance(config, dict) or set(config) - allowed:
            raise TransportError('invalid_config')
        self.account = config.get('account')
        self.path = Path(config.get('token_file', ''))
        self.gmail = config.get('gmail', False)
        self.calendars = config.get('calendar_ids', [])
        self.identity = config.get('identity_method', 'gmail_profile')
        self.timeout = config.get('timeout_seconds', 20)
        self.limit = config.get('max_response_bytes', 8 * 1024 * 1024)
        if (not isinstance(self.account, str) or '@' not in self.account or
                not self.path.is_absolute() or not isinstance(self.gmail, bool) or
                not isinstance(self.calendars, list) or any(not isinstance(x, str) or not x or x == 'primary' for x in self.calendars) or
                not (self.gmail or self.calendars) or self.identity not in {'gmail_profile', 'oidc'} or
                (self.gmail and self.identity != 'gmail_profile') or
                not isinstance(self.timeout, (int, float)) or not 0 < self.timeout <= 120 or
                not isinstance(self.limit, int) or not 1024 <= self.limit <= 32 * 1024 * 1024):
            raise TransportError('invalid_config')
        self._factory = session_factory or aiohttp.ClientSession
        self._session = None
        self._lock = asyncio.Lock()
        self._credentials = {}
        self._fingerprint = None
        self._expiry = None
        self.authenticated_account = None
        self._state = 'disconnected'
        self._declared = []
        self._observed = []
        self._verified = set()
        self._http_status = None
        self._retry_after = None

    def inspect(self):
        return {'state': self._state, 'authenticated_account': self.authenticated_account,
                'declared_scopes': list(self._declared), 'observed_scopes': list(self._observed),
                'verified_capabilities': sorted(self._verified), 'transport_policy': 'GET_only_public_request',
                'public_request_policy': 'GET_only', 'trusted_effects_policy': 'fixed_routes_ledger_gate_single_handler',
                'oauth_scope_restricted_by_transport': False,
                'last_http_status': self._http_status, 'retry_after_seconds': self._retry_after}

    def _fail(self, code):
        self.authenticated_account = None
        self._verified.clear()
        self._state = code
        raise TransportError(code) from None

    def _read_file(self):
        try:
            directory = os.open('/', os.O_RDONLY | os.O_DIRECTORY)
            try:
                for part in self.path.parts[1:-1]:
                    child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=directory)
                    os.close(directory)
                    directory = child
                fd = os.open(self.path.name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=directory)
            finally:
                os.close(directory)
            with os.fdopen(fd, 'rb') as stream:
                info = os.fstat(stream.fileno())
                if not stat.S_ISREG(info.st_mode) or stat.S_IMODE(info.st_mode) != 0o600 or info.st_uid != os.getuid() or info.st_nlink != 1:
                    raise ValueError()
                body = stream.read(1024 * 1024 + 1)
                after = os.fstat(stream.fileno())
                if len(body) > 1024 * 1024 or (after.st_size, after.st_mtime_ns, after.st_ctime_ns) != (info.st_size, info.st_mtime_ns, info.st_ctime_ns):
                    raise ValueError()
            value = json.loads(body)
            if not isinstance(value, dict):
                raise ValueError()
            fingerprint = (info.st_dev, info.st_ino, info.st_mtime_ns, info.st_ctime_ns, hashlib.sha256(body).hexdigest())
            return value, fingerprint
        except (OSError, ValueError):
            self._fail('credential_file_invalid')

    @staticmethod
    def _scopes(value):
        if isinstance(value, str):
            value = value.split()
        if value is None:
            return []
        if not isinstance(value, list) or any(not isinstance(x, str) or not (x.startswith('https://www.googleapis.com/auth/') or x in {'openid', 'email', 'profile'}) or len(x) > 200 for x in value):
            raise TransportError('invalid_scopes')
        return sorted(set(value))

    def _check_file(self):
        _, fingerprint = self._read_file()
        if fingerprint != self._fingerprint:
            self._fail('credential_file_changed_reconnect_required')

    async def connect(self):
        async with self._lock:
            self.authenticated_account = None
            self._verified.clear()
            self._observed = []
            value, self._fingerprint = self._read_file()
            if value.get('token_uri', TOKEN) != TOKEN:
                self._fail('token_endpoint_forbidden')
            for field in ('token', 'refresh_token', 'client_id', 'client_secret'):
                if value.get(field) is not None and (not isinstance(value[field], str) or not value[field] or '\r' in value[field] or '\n' in value[field]):
                    self._fail('credential_invalid')
            self._credentials = {k: value.get(k) for k in ('token', 'refresh_token', 'client_id', 'client_secret')}
            self._declared = self._scopes(value.get('scopes', value.get('scope')))
            self._state = 'verifying'
            self._expiry = None
            if value.get('expiry'):
                try:
                    parsed = datetime.fromisoformat(value['expiry'].replace('Z', '+00:00'))
                    self._expiry = parsed.replace(tzinfo=timezone.utc).timestamp() if parsed.tzinfo is None else parsed.timestamp()
                except (TypeError, ValueError):
                    self._fail('credential_expiry_invalid')
            if self.identity == 'oidc' and not ({'openid', 'email'} <= set(self._declared) or {'openid', 'https://www.googleapis.com/auth/userinfo.email'} <= set(self._declared)):
                self._fail('identity_scope_required')
            if self._session is None:
                self._session = self._factory(trust_env=False, timeout=aiohttp.ClientTimeout(total=self.timeout))
            refreshed = False
            if not self._credentials.get('token') or self._expired():
                await self._refresh()
                refreshed = True
            await self._verify(allow_refresh=not refreshed)
            return self.inspect()

    def _expired(self):
        return self._expiry is not None and self._expiry <= datetime.now(timezone.utc).timestamp() + 30

    async def _http(self, method, url, *, params=None, data=None, json_body=None, extra_headers=None, one_shot=False):
        headers = {'Authorization': 'Bearer ' + self._credentials['token']} if url != TOKEN else {}
        headers.update(extra_headers or {})
        entered = False
        async def single_handler(request, handler):
            nonlocal entered
            if entered:
                raise TransportError('write_retry_blocked')
            entered = True
            return await handler(request)
        request_options = {'middlewares': (single_handler,)} if one_shot else {}
        try:
            async with self._session.request(method, url, params=params, data=data, headers=headers, **request_options, **({"json": json_body} if json_body is not None else {}), allow_redirects=False) as response:
                self._http_status = response.status
                retry = response.headers.get('Retry-After', '')
                self._retry_after = int(retry) if retry.isdigit() and len(retry) < 10 else None
                if response.content_length is not None and response.content_length > self.limit:
                    raise TransportError('response_too_large')
                parts = bytearray()
                async for chunk in response.content.iter_chunked(65536):
                    if len(parts) + len(chunk) > self.limit:
                        raise TransportError('response_too_large')
                    parts.extend(chunk)
                # Error bodies may echo credentials. Never expose them to consumers/loggers.
                return {'status': response.status, 'body': bytes(parts) if 200 <= response.status < 300 else b'{}'}
        except TransportError:
            raise
        except (aiohttp.ClientError, asyncio.TimeoutError, OSError, ValueError):
            raise TransportError('http_transport_failure') from None

    async def _refresh(self):
        self.authenticated_account = None
        self._verified.clear()
        self._state = 'refreshing'
        self._check_file()
        if not all(self._credentials.get(k) for k in ('refresh_token', 'client_id', 'client_secret')):
            self._fail('refresh_credential_missing')
        response = await self._http('POST', TOKEN, data={'grant_type': 'refresh_token', **{k: self._credentials[k] for k in ('refresh_token', 'client_id', 'client_secret')}})
        if response['status'] != 200:
            self._fail('refresh_http_' + str(response['status']))
        try:
            value = json.loads(response['body'])
            access = value['access_token']
            lifetime = value['expires_in']
            if not isinstance(access, str) or not access or '\r' in access or '\n' in access or not isinstance(lifetime, (int, float)) or not 0 < lifetime <= 86400 or value.get('token_type', 'Bearer').lower() != 'bearer':
                raise ValueError()
        except (ValueError, KeyError, TypeError, AttributeError):
            self._fail('refresh_response_invalid')
        if value.get('refresh_token', self._credentials['refresh_token']) != self._credentials['refresh_token']:
            self._fail('refresh_rotation_requires_explicit_persistence')
        self._observed = self._scopes(value.get('scope'))
        self._credentials['token'] = access
        self._expiry = datetime.now(timezone.utc).timestamp() + lifetime
        self._check_file()

    async def _verify(self, *, allow_refresh=False):
        url = GMAIL + '/profile' if self.identity == 'gmail_profile' else OIDC
        response = await self._http('GET', url)
        if response['status'] == 401 and allow_refresh:
            await self._refresh()
            response = await self._http('GET', url)
        if response['status'] != 200:
            self._fail('identity_http_' + str(response['status']))
        try:
            body = json.loads(response['body'])
            account = body.get('emailAddress') if self.identity == 'gmail_profile' else body.get('email')
            if account != self.account or (self.identity == 'oidc' and body.get('email_verified') is not True):
                self._fail('identity_mismatch')
        except (ValueError, AttributeError):
            self._fail('identity_response_invalid')
        self._check_file()
        self.authenticated_account = self.account
        self._state = 'connected'

    def _route(self, method, url, params):
        if method != 'GET' or not isinstance(url, str) or not isinstance(params, dict):
            raise TransportError('request_forbidden')
        allowed = None
        if self.gmail:
            if url == GMAIL + '/profile':
                allowed = set()
            elif url == GMAIL + '/messages':
                allowed = {'maxResults', 'includeSpamTrash', 'pageToken', 'q'}
                if 'q' in params and not canonical_gmail_query(params['q']):
                    raise TransportError('request_forbidden')
            elif url == GMAIL + '/history':
                allowed = {'maxResults', 'startHistoryId', 'pageToken'}
            elif url.startswith(GMAIL + '/messages/'):
                identity = url[len(GMAIL + '/messages/'):]
                if identity and all(x.isascii() and (x.isalnum() or x in '_-') for x in identity):
                    allowed = {'format'}
                    if params.get('format') != 'raw':
                        raise TransportError('request_forbidden')
        if url in {'https://www.googleapis.com/calendar/v3/calendars/' + quote(x, safe='') + '/events' for x in self.calendars}:
            allowed = {'maxResults', 'singleEvents', 'showDeleted', 'syncToken', 'pageToken'}
        if allowed is None or set(params) - allowed or any(not isinstance(v, (str, int, bool)) for v in params.values()):
            raise TransportError('request_forbidden')
        return 'gmail_read' if url.startswith(GMAIL) else 'calendar_read'

    async def request(self, method, url, *, params=None):
        params = {} if params is None else dict(params)
        capability = self._route(method, url, params)
        async with self._lock:
            if self.authenticated_account is None:
                raise TransportError('connect_required')
            self._check_file()
            refreshed = False
            if self._expired():
                await self._refresh()
                await self._verify()
                refreshed = True
            response = await self._http('GET', url, params=params)
            if response['status'] == 401 and not refreshed:
                await self._refresh()
                await self._verify()
                response = await self._http('GET', url, params=params)
            self._check_file()
            if response['status'] == 401:
                self.authenticated_account = None
                self._state = 'authentication_rejected'
            elif 200 <= response['status'] < 300:
                self._verified.add(capability)
            return response

    async def _effect_prepare(self, account):
        """Trusted effects only. Revalidate identity before opening a dispatch gate."""
        if account != self.account:
            raise TransportError('effect_account_mismatch')
        if self.authenticated_account is None:
            await self.connect()
            return
        async with self._lock:
            self._check_file()
            if self._expired():
                await self._refresh()
            await self._verify()

    async def _effect_get(self, kind, *, identity=None, message_id=None):
        if not self.gmail:
            raise TransportError('gmail_not_configured')
        params = {}
        if kind == 'send_as':
            url = GMAIL + '/settings/sendAs'
        elif kind in {'draft', 'message', 'thread'}:
            if not isinstance(identity, str) or not identity or not all(x.isascii() and (x.isalnum() or x in '_-') for x in identity):
                raise TransportError('effect_identity_invalid')
            url = GMAIL + '/' + {'draft':'drafts','message':'messages','thread':'threads'}[kind] + '/' + identity
            params = {'format':'metadata' if kind == 'thread' else 'raw'}
        elif kind in {'draft_search', 'message_search'}:
            import re
            if not isinstance(message_id, str) or not re.fullmatch(r'<[^<>\s@]+@[^<>\s@]+>', message_id):
                raise TransportError('effect_message_id_invalid')
            url = GMAIL + ('/drafts' if kind == 'draft_search' else '/messages')
            params = {'q':'rfc822msgid:' + message_id, 'maxResults':2, 'includeSpamTrash':'true'}
        else:
            raise TransportError('effect_read_forbidden')
        async with self._lock:
            if self.authenticated_account != self.account:
                raise TransportError('connect_required')
            self._check_file()
            return await self._http('GET', url, params=params)

    async def _effect_post(self, action, payload, account, begin_dispatch):
        if not self.gmail or action not in {'draft_create','send'}:
            raise TransportError('effect_write_forbidden')
        url = GMAIL + ('/drafts' if action == 'draft_create' else '/messages/send')
        async with self._lock:
            self._check_file()
            if self.authenticated_account != account or account != self.account or self._expired():
                raise TransportError('effect_identity_preparation_required')
            admission = begin_dispatch()
            if admission.get('status') != 'dispatch':
                return {'admission':admission, 'response':None}
            response = await self._http('POST', url, json_body=payload, one_shot=True)
            return {'admission':admission, 'response':response}

    def _calendar_url(self, calendar_id):
        if calendar_id not in self.calendars:
            raise TransportError('calendar_not_configured')
        return 'https://www.googleapis.com/calendar/v3/calendars/' + quote(calendar_id, safe='') + '/events'

    async def _calendar_effect_get(self, calendar_id, event_id=None, params=None, calendar_list=False):
        url = self._calendar_url(calendar_id)
        params = {} if params is None else dict(params)
        if calendar_list:
            if event_id is not None or params:
                raise TransportError('calendar_read_forbidden')
            url = 'https://www.googleapis.com/calendar/v3/users/me/calendarList/' + quote(calendar_id, safe='')
        elif event_id is not None:
            if not isinstance(event_id,str) or not event_id or not all(x.isascii() and (x.isalnum() or x in '_-') for x in event_id) or params:
                raise TransportError('calendar_read_forbidden')
            url += '/' + event_id
        else:
            if (set(params) - {'singleEvents','showDeleted','timeMin','timeMax','timeZone','maxResults','pageToken'}
                    or params.get('singleEvents') != 'true' or params.get('showDeleted') != 'true'
                    or not all(isinstance(params.get(k),str) and params[k] for k in ('timeMin','timeMax','timeZone'))
                    or type(params.get('maxResults')) is not int or not 1 <= params['maxResults'] <= 2500):
                raise TransportError('calendar_read_forbidden')
        async with self._lock:
            if self.authenticated_account != self.account:
                raise TransportError('connect_required')
            self._check_file()
            return await self._http('GET',url,params=params)

    async def _calendar_effect_write(self, action, calendar_id, event_id, payload, account, begin_dispatch, *, etag=None, send_updates):
        url = self._calendar_url(calendar_id)
        if action not in {'insert','update','decline','delete_copy','cancel_event'} or send_updates not in {'none','all','externalOnly'}:
            raise TransportError('calendar_write_forbidden')
        if action == 'insert':
            if event_id is not None or etag is not None:
                raise TransportError('calendar_write_forbidden')
            method = 'POST'
        else:
            if (not isinstance(event_id,str) or not event_id or not all(x.isascii() and (x.isalnum() or x in '_-') for x in event_id)
                    or not isinstance(etag,str) or not etag or any(x in etag for x in '\r\n')):
                raise TransportError('calendar_precondition_required')
            url += '/' + event_id
            method = 'PATCH' if action in {'update','decline'} else 'DELETE'
        async with self._lock:
            self._check_file()
            if self.authenticated_account != account or account != self.account or self._expired():
                raise TransportError('effect_identity_preparation_required')
            admission = begin_dispatch()
            if admission.get('status') != 'dispatch':
                return {'admission':admission,'response':None}
            response = await self._http(method,url,params={'sendUpdates':send_updates},json_body=payload,
                extra_headers={'If-Match':etag} if etag else None, one_shot=True)
            return {'admission':admission,'response':response}

    async def close(self):
        async with self._lock:
            if self._session is not None:
                await self._session.close()
            self._session = None
            self._credentials = {}
            self._fingerprint = None
            self.authenticated_account = None
            self._verified.clear()
            self._state = 'closed'
