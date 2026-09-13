"""Local HTTP provider and listener; no real account or Google request."""
import concurrent.futures
import contextlib
import datetime as dt
import http.client
import http.server
import importlib.util
import io
import json
import os
from pathlib import Path
import stat
import sys
import tempfile
import socket
import time
import threading
import unittest
from urllib.parse import parse_qs, urlencode, urlsplit

SCRIPT = Path(__file__).resolve().parents[2] / 'scripts' / 'gtd_google_connect.py'
spec = importlib.util.spec_from_file_location('gtd_google_connect', SCRIPT)
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)


class ConnectTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.client = self.root / 'client.json'
        self.client.write_text(json.dumps({'installed': {'client_id': 'synthetic.apps.googleusercontent.com', 'client_secret': 'CLIENT_SECRET_CANARY', 'auth_uri': next(iter(g.AUTH_URIS)), 'token_uri': g.TOKEN_URI}}))
        self.client.chmod(0o600)
        self.output = self.root / 'new-token.json'
        self.scopes = ' '.join(g.SCOPES)
        self.email = 'owner@example.invalid'
        self.exchanges = 0
        self.profile_reads = 0
        self.received = []
        self.challenge = None
        self.emitted = []
        test = self
        class Provider(http.server.BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass
            def do_POST(self):
                test.exchanges += 1
                body = self.rfile.read(int(self.headers['Content-Length'])).decode()
                fields = parse_qs(body)
                test.received.append(fields)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                value = {'access_token': 'ACCESS_SECRET_CANARY', 'refresh_token': 'REFRESH_SECRET_CANARY', 'token_type': 'Bearer', 'expires_in': 3600}
                if test.scopes is not None:
                    value['scope'] = test.scopes
                self.wfile.write(json.dumps(value).encode())
            def do_GET(self):
                test.profile_reads += 1
                self.send_response(200)
                self.end_headers()
                self.wfile.write(json.dumps({'emailAddress': test.email}).encode())
        self.provider = http.server.ThreadingHTTPServer(('127.0.0.1', 0), Provider)
        self.thread = threading.Thread(target=self.provider.serve_forever, daemon=True)
        self.thread.start()

    def tearDown(self):
        self.provider.shutdown()
        self.provider.server_close()
        self.thread.join()
        self.tmp.cleanup()

    def factory(self, config):
        # Real installed public Flow, public Requests adapter redirects only the
        # token endpoint to the synthetic local HTTP server. No insecure OAuth
        # environment toggle and no Google connection.
        import requests
        flow = g._flow(config)
        provider_port = self.provider.server_port
        class LocalAdapter(requests.adapters.HTTPAdapter):
            def send(self, request, **kwargs):
                if request.url != g.TOKEN_URI:
                    raise AssertionError('unexpected endpoint')
                request.url = f'http://127.0.0.1:{provider_port}/token'
                return super().send(request, **kwargs)
        flow.oauth2session.trust_env = False
        flow.oauth2session.mount(g.TOKEN_URI, LocalAdapter())
        return flow

    def profile(self, token, timeout):
        connection = http.client.HTTPConnection('127.0.0.1', self.provider.server_port, timeout=timeout)
        connection.request('GET', '/profile', headers={'Authorization': 'Bearer ' + token})
        response = connection.getresponse()
        value = json.loads(response.read())
        connection.close()
        return value['emailAddress']

    def run_connect(self, *, state=True, host=True, path=True, timeout=False, duplicate=False):
        callbacks = []
        def callback(info):
            self.emitted.append(info)
            query = parse_qs(urlsplit(info['authorization_url']).query)
            self.challenge = query['code_challenge'][0]
            self.assertEqual(query['code_challenge_method'], ['S256'])
            if timeout:
                return
            def send():
                conn = http.client.HTTPConnection('127.0.0.1', info['port'], timeout=2)
                request = ('/oauth2/callback' if path else '/wrong') + '?' + urlencode({'state': query['state'][0] if state else 'wrong', 'code': 'CODE_SECRET_CANARY'})
                conn.request('GET', request, headers={'Host': f"127.0.0.1:{info['port']}" if host else 'evil.example'})
                try:
                    reply = conn.getresponse()
                    reply.read()
                    if duplicate:
                        try:
                            conn.close()
                            conn = http.client.HTTPConnection('127.0.0.1', info['port'], timeout=1)
                            conn.request('GET', request)
                            conn.getresponse().read()
                        except (OSError, http.client.HTTPException):
                            pass
                finally:
                    conn.close()
            thread = threading.Thread(target=send)
            callbacks.append(thread)
            thread.start()
        try:
            return g.connect('owner@example.invalid', self.client, self.output, timeout=1 if timeout else 4, emit=callback, flow_factory=self.factory, profile_reader=self.profile)
        finally:
            for thread in callbacks:
                thread.join()

    def test_success_real_flow_pkce_private_token_and_no_second_exchange(self):
        capture = io.StringIO()
        with contextlib.redirect_stdout(capture), contextlib.redirect_stderr(capture):
            receipt = self.run_connect(duplicate=True)
        self.assertEqual(self.exchanges, 1)
        self.assertEqual(self.profile_reads, 1)
        token = json.loads(self.output.read_text())
        self.assertEqual(stat.S_IMODE(self.output.stat().st_mode), 0o600)
        self.assertEqual(token['token_uri'], g.TOKEN_URI)
        self.assertEqual(set(token['scopes']), set(g.SCOPES))
        self.assertTrue(token['expiry'].endswith('Z'))
        self.assertEqual(token['refresh_token'], 'REFRESH_SECRET_CANARY')
        from runtime_location import RUNTIME
        sys.path.insert(0, str(RUNTIME))
        from gtd_felix.google_transport import GoogleTransport
        transport = GoogleTransport({'account': 'owner@example.invalid', 'token_file': str(self.output), 'gmail': True})
        stored, fingerprint = transport._read_file()
        self.assertEqual(stored, token)
        self.assertEqual(transport._scopes(stored['scopes']), sorted(g.SCOPES))
        self.assertTrue(fingerprint)
        import base64, hashlib
        verifier = self.received[0]['code_verifier'][0]
        self.assertEqual(base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).decode().rstrip('='), self.challenge)
        exposed = capture.getvalue() + json.dumps(receipt) + json.dumps(self.emitted)
        for secret in ('ACCESS_SECRET_CANARY', 'REFRESH_SECRET_CANARY', 'CLIENT_SECRET_CANARY', 'CODE_SECRET_CANARY'):
            self.assertNotIn(secret, exposed)

    def test_wrong_state_host_and_path_never_exchange(self):
        for field in ('state', 'host', 'path'):
            with self.subTest(field=field), self.assertRaisesRegex(g.Blocked, 'callback_rejected'):
                self.run_connect(**{field: False})
        self.assertEqual(self.exchanges, 0)
        self.assertFalse(self.output.exists())

    def test_timeout_no_exchange(self):
        with self.assertRaisesRegex(g.Blocked, 'callback_timeout'):
            self.run_connect(timeout=True)
        self.assertEqual(self.exchanges, 0)

    def test_account_mismatch_never_publishes(self):
        self.email = 'other@example.invalid'
        with self.assertRaisesRegex(g.Blocked, 'account_mismatch'):
            self.run_connect()
        self.assertFalse(self.output.exists())

    def test_scopes_missing_extra_and_partial_never_publish(self):
        for scopes in (None, ' '.join(g.SCOPES) + ' https://www.googleapis.com/auth/gmail.send', g.SCOPES[0]):
            self.scopes = scopes
            with self.subTest(scopes=scopes), self.assertRaises(g.Blocked):
                self.run_connect()
        self.assertFalse(self.output.exists())
        self.assertEqual(self.profile_reads, 0)

    def test_existing_output_and_symlink_fail_before_oauth(self):
        self.output.write_text('preserve')
        with self.assertRaisesRegex(g.Blocked, 'output_exists'):
            self.run_connect()
        self.assertEqual(self.output.read_text(), 'preserve')
        self.output.unlink()
        self.output.symlink_to(self.root / 'absent')
        with self.assertRaisesRegex(g.Blocked, 'output_exists'):
            self.run_connect()
        self.assertEqual(self.exchanges, 0)

    def test_output_appearing_after_consent_is_not_overwritten(self):
        original_profile = self.profile
        def raced(token, timeout):
            self.output.write_text('concurrent owner output')
            return original_profile(token, timeout)
        self.profile = raced
        with self.assertRaises(g.Blocked):
            self.run_connect()
        self.assertEqual(self.output.read_text(), 'concurrent owner output')
        self.assertEqual(list(self.root.glob('.google-token-*')), [])

    def test_incomplete_http_headers_have_finite_deadline(self):
        sockets = []
        def incomplete(info):
            connection = socket.create_connection(('127.0.0.1', info['port']))
            sockets.append(connection)
            connection.sendall(b'GET /oauth2/callback HTTP/1.1\r\n')
        started = time.monotonic()
        try:
            with self.assertRaises(g.Blocked):
                g.connect('owner@example.invalid', self.client, self.output, timeout=1, emit=incomplete, flow_factory=self.factory, profile_reader=self.profile)
        finally:
            for connection in sockets:
                connection.close()
        self.assertLess(time.monotonic() - started, 3)
        self.assertEqual(self.exchanges, 0)

    def test_client_symlink_and_permissions_and_endpoint_rejected(self):
        real = self.root / 'real.json'
        self.client.rename(real)
        self.client.symlink_to(real)
        with self.assertRaises(g.Blocked):
            self.run_connect()
        self.client.unlink()
        real.rename(self.client)
        self.client.chmod(0o644)
        with self.assertRaisesRegex(g.Blocked, 'private_client_file_required'):
            self.run_connect()
        self.client.chmod(0o600)
        value = json.loads(self.client.read_text())
        value['installed']['token_uri'] = 'https://evil.example/token'
        self.client.write_text(json.dumps(value))
        with self.assertRaisesRegex(g.Blocked, 'invalid_desktop_client'):
            self.run_connect()
        self.assertEqual(self.exchanges, 0)


class CalendarListTests(unittest.TestCase):
    def setUp(self):
        import requests
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.token = self.root / 'token.json'
        self.credentials = {'type': 'authorized_user', 'token': 'ACCESS_CANARY', 'refresh_token': 'REFRESH_CANARY',
            'client_id': 'synthetic.apps.googleusercontent.com', 'client_secret': 'CLIENT_CANARY',
            'token_uri': g.TOKEN_URI, 'scopes': list(g.SCOPES),
            'expiry': (dt.datetime.now(dt.timezone.utc) + dt.timedelta(hours=1)).isoformat()}
        self.write_token()
        self.requests = []
        self.account = 'owner@example.invalid'
        self.pages = [(200, {'items': [{'id': 'cal@example.invalid', 'summary': 'Calendar', 'primary': True,
            'selected': False, 'accessRole': 'owner', 'timeZone': 'UTC', 'description': 'PRIVATE_DESCRIPTION'}]})]
        self.refresh_body = {'access_token': 'NEW_ACCESS_CANARY', 'token_type': 'Bearer', 'expires_in': 3600}
        self.profile_status = 200
        test = self
        class Provider(http.server.BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass
            def reply(self, status, value):
                self.send_response(status)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(value).encode())
            def do_GET(self):
                test.requests.append(('GET', self.path, self.headers.get('Authorization')))
                if self.path.startswith('/profile?'):
                    self.reply(test.profile_status, {'emailAddress': test.account})
                else:
                    status, value = test.pages.pop(0)
                    self.reply(status, value)
            def do_POST(self):
                body = self.rfile.read(int(self.headers['Content-Length'])).decode()
                test.requests.append(('POST', self.path, parse_qs(body)))
                self.reply(200, test.refresh_body)
        self.provider = http.server.ThreadingHTTPServer(('127.0.0.1', 0), Provider)
        self.thread = threading.Thread(target=self.provider.serve_forever, daemon=True)
        self.thread.start()
        class LocalAdapter(requests.adapters.HTTPAdapter):
            def send(self, request, **kwargs):
                parts = urlsplit(request.url)
                base = parts._replace(query='').geturl()
                routes = {g.PROFILE_URI: '/profile', g.CALENDAR_LIST_URI: '/calendarList', g.TOKEN_URI: '/token'}
                if base not in routes:
                    raise AssertionError('unexpected endpoint')
                request.url = f'http://127.0.0.1:{test.provider.server_port}' + routes[base] + ('?' + parts.query if parts.query else '')
                return super().send(request, **kwargs)
        def factory():
            session = requests.Session()
            session.mount('https://', LocalAdapter())
            return session
        self.factory = factory

    def write_token(self):
        self.token.write_text(json.dumps(self.credentials))
        self.token.chmod(0o600)

    def tearDown(self):
        self.provider.shutdown()
        self.provider.server_close()
        self.thread.join()
        self.tmp.cleanup()

    def run_list(self, **kwargs):
        return g.list_calendars('owner@example.invalid', self.token, session_factory=self.factory, **kwargs)

    def test_metadata_only_fixed_routes_identity_first(self):
        result = self.run_list()
        self.assertEqual(result['status'], 'complete')
        self.assertEqual(result['coverage'], 'user_calendar_list_only')
        self.assertEqual(result['calendars'][0]['id'], 'cal@example.invalid')
        self.assertFalse(result['calendars'][0]['selected'])
        self.assertEqual(len(self.requests), 2)
        self.assertTrue(self.requests[0][1].startswith('/profile?'))
        params = parse_qs(urlsplit(self.requests[1][1]).query)
        self.assertEqual(params['showHidden'], ['true'])
        self.assertNotIn('description', params['fields'][0])
        self.assertNotIn('PRIVATE_DESCRIPTION', json.dumps(result))
        for value in ('ACCESS_CANARY', 'CLIENT_CANARY', 'REFRESH_CANARY'):
            self.assertNotIn(value, json.dumps(result))

    def test_identity_mismatch_no_calendar_request(self):
        self.account = 'other@example.invalid'
        with self.assertRaisesRegex(g.Blocked, 'account_mismatch'):
            self.run_list()
        self.assertEqual(len(self.requests), 1)

    def test_pagination_limit_and_repeat_are_partial_without_token_output(self):
        self.pages = [(200, {'items': [], 'nextPageToken': 'PRIVATE_PAGE'}), (200, {'items': [], 'nextPageToken': 'PRIVATE_PAGE'})]
        result = self.run_list(max_pages=1)
        self.assertEqual(result['reason'], 'page_limit_reached')
        self.assertTrue(result['continuation_required'])
        self.assertNotIn('PRIVATE_PAGE', json.dumps(result))
        self.pages.insert(0, (200, {'items': [], 'nextPageToken': 'PRIVATE_PAGE'}))
        result = self.run_list()
        self.assertEqual(result['reason'], 'pagination_repeated')
        self.assertEqual(result['pages_read'], 2)
        self.assertNotIn('PRIVATE_PAGE', json.dumps(result))

    def test_two_pages_complete_and_error_preserves_first_page(self):
        first = self.pages[0][1]
        first['nextPageToken'] = 'PAGE_TWO'
        self.pages.append((200, {'items': []}))
        result = self.run_list()
        self.assertEqual(result['pages_read'], 2)
        self.assertEqual(result['status'], 'complete')
        self.pages = [(200, first), (403, {'error': 'ACCESS_CANARY'})]
        result = self.run_list()
        self.assertEqual(result['status'], 'partial')
        self.assertEqual(len(result['calendars']), 1)
        self.assertEqual(result['reason'], 'calendar_list_http_403')

    def test_bounded_read_retries_no_redirect(self):
        self.pages = [(503, {}), (503, {'error': 'ACCESS_CANARY'})]
        result = self.run_list()
        self.assertEqual(result['reason'], 'calendar_list_http_503')
        self.assertEqual(len(self.requests), 3)
        self.pages = [(302, {'location': 'https://evil.invalid'})]
        self.assertEqual(self.run_list()['reason'], 'calendar_list_http_302')

    def test_refresh_in_memory_identity_rechecked_and_no_secret_output(self):
        self.credentials['expiry'] = '2000-01-01T00:00:00Z'
        self.write_token()
        before = self.token.read_bytes()
        output = io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            result = self.run_list()
        self.assertEqual([r[0] for r in self.requests], ['POST', 'GET', 'GET'])
        self.assertEqual(self.requests[0][1], '/token')
        self.assertEqual(self.requests[1][2], 'Bearer NEW_ACCESS_CANARY')
        self.assertEqual(self.token.read_bytes(), before)
        self.assertNotIn('CANARY', output.getvalue() + json.dumps(result))

    def test_401_refresh_reverifies_before_retry_and_mismatch_aborts(self):
        self.pages.insert(0, (401, {}))
        result = self.run_list()
        self.assertEqual(result['status'], 'complete')
        self.assertEqual([url.split('?')[0] for _, url, _ in self.requests], ['/profile', '/calendarList', '/token', '/profile', '/calendarList'])
        self.requests.clear()
        self.credentials['expiry'] = '2000-01-01T00:00:00Z'
        self.write_token()
        self.account = 'other@example.invalid'
        with self.assertRaisesRegex(g.Blocked, 'account_mismatch'):
            self.run_list()
        self.assertEqual(len(self.requests), 2)

    def test_refresh_scope_rotation_and_endpoint_rejected(self):
        self.credentials['expiry'] = '2000-01-01T00:00:00Z'
        self.write_token()
        for field, value in [('scope', g.SCOPES[0]), ('refresh_token', 'ROTATED_CANARY')]:
            with self.subTest(field=field):
                self.refresh_body[field] = value
                with self.assertRaises(g.Blocked):
                    self.run_list()
                del self.refresh_body[field]
        self.credentials['token_uri'] = 'https://evil.invalid/token'
        self.write_token()
        count = len(self.requests)
        with self.assertRaises(g.Blocked):
            self.run_list()
        self.assertEqual(len(self.requests), count)

    def test_private_permissions_links_parent_and_scope_before_network(self):
        self.token.chmod(0o644)
        with self.assertRaises(g.Blocked):
            self.run_list()
        self.token.chmod(0o600)
        self.root.chmod(0o755)
        with self.assertRaises(g.Blocked):
            self.run_list()
        self.root.chmod(0o700)
        other = self.root / 'other.json'
        os.link(self.token, other)
        with self.assertRaises(g.Blocked):
            self.run_list()
        other.unlink()
        self.token.rename(other)
        self.token.symlink_to(other)
        with self.assertRaises(g.Blocked):
            self.run_list()
        self.token.unlink()
        other.rename(self.token)
        self.credentials['scopes'].append('https://www.googleapis.com/auth/calendar')
        self.write_token()
        with self.assertRaises(g.Blocked):
            self.run_list()
        self.assertEqual(self.requests, [])

    def test_invalid_metadata_and_page_shapes_are_explicit(self):
        for body in ({'items': 'bad'}, {'items': [{'id': 'cal', 'summary': '\x1bsecret'}]}, {'items': [], 'nextPageToken': 3}, {'items': [{'id': 'cal', 'summary': 'Echo ACCESS_CANARY'}]}):
            self.pages = [(200, body)]
            result = self.run_list()
            self.assertEqual(result['status'], 'partial')
            self.assertEqual(result['pages_read'], 0)

    def test_cli_listing_needs_no_client_and_partial_exit_is_distinct(self):
        from unittest.mock import patch
        for status, expected in [('complete', 0), ('partial', 3)]:
            capture = io.StringIO()
            with patch.object(g, 'list_calendars', return_value={'status': status}) as listing, contextlib.redirect_stdout(capture):
                code = g.main(['--list-calendars', '--account', self.account, '--token-file', str(self.token), '--max-pages', '2'])
            self.assertEqual(code, expected)
            self.assertEqual(json.loads(capture.getvalue())['status'], status)
            self.assertEqual(listing.call_args.kwargs['max_pages'], 2)
        capture = io.StringIO()
        with contextlib.redirect_stderr(capture):
            self.assertEqual(g.main(['--account', self.account, '--token-file', str(self.token)]), 2)
        self.assertEqual(json.loads(capture.getvalue())['reason'], 'client_file_required')

    def test_failed_refresh_output_is_sanitized_and_not_retried(self):
        self.credentials['expiry'] = '2000-01-01T00:00:00Z'
        self.write_token()
        self.refresh_body = {'access_token': 'BAD\nACCESS_CANARY', 'expires_in': 3600, 'token_type': 'Bearer'}
        with self.assertRaisesRegex(g.Blocked, '^invalid_refresh_response$'):
            self.run_list()
        self.assertEqual(len(self.requests), 1)


if __name__ == '__main__':
    unittest.main()
