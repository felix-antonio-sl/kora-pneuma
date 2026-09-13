#!/usr/bin/env python3
"""Explicit, read-only Desktop OAuth bootstrap; optional google-auth-oauthlib.

No credential discovery or installation. A caller supplies a private Desktop
client file and a new token pathname in an existing private directory. The
public Flow API owns PKCE and token exchange; this module only gates the local
callback, verifies the granted account/scopes, and publishes a new file.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import http.server
import json
import os
from pathlib import Path
import secrets
import stat
import socket
import threading
import sys
import time
from urllib.parse import parse_qs, urlsplit

SCOPES = ("https://www.googleapis.com/auth/gmail.readonly", "https://www.googleapis.com/auth/calendar.readonly")
TOKEN_URI = "https://oauth2.googleapis.com/token"
PROFILE_URI = "https://gmail.googleapis.com/gmail/v1/users/me/profile"
CALENDAR_LIST_URI = "https://www.googleapis.com/calendar/v3/users/me/calendarList"
AUTH_URIS = {"https://accounts.google.com/o/oauth2/auth", "https://accounts.google.com/o/oauth2/v2/auth"}


class Blocked(Exception):
    """Safe diagnostic code, never an upstream exception or response body."""


def _directory(path):
    path = Path(os.path.abspath(path))
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in path.parts[1:]:
            next_fd = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = next_fd
        info = os.fstat(fd)
        if info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) != 0o700:
            raise Blocked("private_directory_required")
        return fd
    except BaseException:
        os.close(fd)
        raise


def _private_json(path, label):
    path = Path(os.path.abspath(path))
    parent = _directory(path.parent)
    try:
        fd = os.open(path.name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=parent)
        try:
            before = os.fstat(fd)
            if not stat.S_ISREG(before.st_mode) or before.st_uid != os.getuid() or stat.S_IMODE(before.st_mode) != 0o600 or before.st_nlink != 1 or before.st_size > 65536:
                raise Blocked("private_" + label + "_file_required")
            data = os.read(fd, 65537)
            after = os.fstat(fd)
            if (before.st_size, before.st_mtime_ns, before.st_ctime_ns) != (after.st_size, after.st_mtime_ns, after.st_ctime_ns):
                raise Blocked(label + "_changed")
        finally:
            os.close(fd)
    finally:
        os.close(parent)
    try:
        return json.loads(data)
    except (ValueError, UnicodeError):
        raise Blocked("invalid_" + label + "_json") from None


def _client(path):
    try:
        config = _private_json(path, "client")
        client = config["installed"]
        if set(config) != {"installed"} or not isinstance(client, dict):
            raise ValueError()
        if client.get("auth_uri") not in AUTH_URIS or client.get("token_uri") != TOKEN_URI:
            raise ValueError()
        for key in ("client_id", "client_secret"):
            if not isinstance(client.get(key), str) or not client[key] or len(client[key]) > 4096 or any(c.isspace() for c in client[key]):
                raise ValueError()
        if not client["client_id"].endswith(".apps.googleusercontent.com"):
            raise ValueError()
        # Ignore unneeded downloaded metadata; no endpoint can be selected by it.
        return {"installed": {key: client[key] for key in ("client_id", "client_secret", "auth_uri", "token_uri")}}
    except (KeyError, TypeError, ValueError):
        raise Blocked("invalid_desktop_client") from None


def _flow(config):
    try:
        from google_auth_oauthlib.flow import Flow
    except ImportError:
        raise Blocked("optional_dependency_missing_google_auth_oauthlib") from None
    return Flow.from_client_config(config, scopes=list(SCOPES), autogenerate_code_verifier=True)


def _profile(token, timeout):
    import requests
    with requests.Session() as session:
        session.trust_env = False
        with session.get(PROFILE_URI, params={"fields": "emailAddress"}, headers={"Authorization": "Bearer " + token}, timeout=timeout, allow_redirects=False, stream=True) as response:
            if response.status_code != 200:
                raise Blocked("identity_readback_failed")
            data = bytearray()
            for chunk in response.iter_content(4096):
                data.extend(chunk)
                if len(data) > 16384:
                    raise Blocked("identity_response_too_large")
            return json.loads(data).get("emailAddress")


def _publish(parent, name, payload):
    temporary = ".google-token-" + secrets.token_hex(16)
    fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=parent)
    try:
        os.fchmod(fd, 0o600)
        with os.fdopen(fd, "wb") as output:
            output.write(payload)
            output.flush()
            os.fsync(output.fileno())
        os.link(temporary, name, src_dir_fd=parent, dst_dir_fd=parent, follow_symlinks=False)
        os.fsync(parent)
    finally:
        os.unlink(temporary, dir_fd=parent)


def connect(account, client_file, token_file, *, port=0, timeout=180, emit=None, flow_factory=None, profile_reader=None):
    """Block for one exact callback; dependencies are injectable for offline tests.

    Returned receipt contains no token/client/code. ``emit`` receives only the
    authorization URL and listener coordinates, before callback waiting starts.
    A denied/malformed callback consumes this attempt. No exchange is retried.
    """
    if not isinstance(account, str) or len(account) > 254 or account.count("@") != 1 or any(c.isspace() for c in account):
        raise Blocked("invalid_account")
    if isinstance(port, bool) or not isinstance(port, int) or not (port == 0 or 1024 <= port <= 65535):
        raise Blocked("invalid_port")
    if isinstance(timeout, bool) or not isinstance(timeout, (int, float)) or not 1 <= timeout <= 900:
        raise Blocked("invalid_timeout")
    target = Path(os.path.abspath(token_file))
    parent = _directory(target.parent)
    server = None
    try:
        try:
            os.stat(target.name, dir_fd=parent, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise Blocked("output_exists")
        config = _client(client_file)
        flow = (flow_factory or _flow)(config)
        flow.oauth2session.trust_env = False
        granted_evidence = {}
        def capture_granted(response):
            # Public compliance hook sees the actual token response before
            # oauthlib can substitute the requested scopes when scope is absent.
            try:
                granted_evidence["scope"] = response.json().get("scope")
            except (ValueError, AttributeError):
                granted_evidence["scope"] = None
            return response
        flow.oauth2session.register_compliance_hook("access_token_response", capture_granted)
        accepted = {}
        state = secrets.token_urlsafe(32)
        class Callback(http.server.BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def do_GET(self):
                error = None
                try:
                    if len(self.path) > 8192 or self.headers.get_all("Host") != [f"127.0.0.1:{server.server_port}"]:
                        raise ValueError()
                    parsed = urlsplit(self.path)
                    if parsed.scheme or parsed.netloc or parsed.path != "/oauth2/callback" or parsed.fragment:
                        raise ValueError()
                    query = parse_qs(parsed.query, strict_parsing=True, max_num_fields=12)
                    if query.get("state") != [state] or len(query.get("code", [])) != 1 or not query["code"][0] or "error" in query:
                        raise ValueError()
                    if accepted:
                        raise ValueError()
                    accepted["code"] = query["code"][0]
                except (ValueError, TypeError):
                    error = "callback_rejected"
                    accepted["error"] = error
                self.send_response(400 if error else 200)
                self.send_header("Content-Type", "text/plain; charset=utf-8")
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(b"Authorization received. Return to the local terminal." if not error else b"Authorization callback rejected.")

            def do_POST(self):
                accepted["error"] = "callback_rejected"
                self.send_error(405)
        timers = []
        class Receiver(http.server.HTTPServer):
            def handle_error(self, request, address):
                accepted["error"] = "callback_rejected"

            def get_request(self):
                connection, address = super().get_request()
                connection.settimeout(timeout)
                def expire():
                    try:
                        connection.shutdown(socket.SHUT_RDWR)
                    except OSError:
                        pass
                timer = threading.Timer(timeout, expire)
                timer.daemon = True
                timers.append(timer)
                timer.start()
                return connection, address
        server = Receiver(("127.0.0.1", port), Callback)
        server.timeout = timeout
        flow.redirect_uri = f"http://127.0.0.1:{server.server_port}/oauth2/callback"
        url, returned_state = flow.authorization_url(state=state, access_type="offline", prompt="consent", login_hint=account, include_granted_scopes="false")
        parts = urlsplit(url)
        query = parse_qs(parts.query)
        if parts.scheme != "https" or parts.netloc != "accounts.google.com" or returned_state != state or query.get("state") != [state] or query.get("code_challenge_method") != ["S256"] or not query.get("code_challenge"):
            raise Blocked("authorization_url_invalid")
        if emit:
            emit({"status": "awaiting_consent", "authorization_url": url, "host": "127.0.0.1", "port": server.server_port, "timeout_seconds": timeout})
        started = time.monotonic()
        try:
            server.handle_request()
        finally:
            for timer in timers:
                timer.cancel()
        server.server_close()
        server = None
        if accepted.get("error"):
            raise Blocked(accepted["error"])
        if not accepted.get("code") or time.monotonic() - started >= timeout:
            raise Blocked("callback_timeout")
        # State is checked above, so only the code reaches public Flow. It adds
        # the verifier itself; HTTP loopback is not passed as a token endpoint.
        try:
            flow.fetch_token(code=accepted.pop("code"), timeout=min(timeout, 30), allow_redirects=False)
        except Exception:
            if "scope" in granted_evidence:
                raise Blocked("token_exchange_or_scopes_rejected") from None
            raise Blocked("token_exchange_failed") from None
        granted = granted_evidence.get("scope")
        if isinstance(granted, str):
            granted = granted.split()
        if not isinstance(granted, (list, tuple)) or set(granted) != set(SCOPES) or len(granted) != len(SCOPES):
            raise Blocked("granted_scopes_not_exact")
        credentials = flow.credentials
        if not credentials.token or not credentials.refresh_token:
            raise Blocked("offline_credentials_missing")
        expiry = credentials.expiry
        if not isinstance(expiry, dt.datetime):
            raise Blocked("expiry_missing")
        if expiry.tzinfo is None:
            expiry = expiry.replace(tzinfo=dt.timezone.utc)  # google-auth documents naive UTC.
        expiry = expiry.astimezone(dt.timezone.utc)
        if expiry <= dt.datetime.now(dt.timezone.utc):
            raise Blocked("credentials_expired")
        if (profile_reader or _profile)(credentials.token, min(timeout, 30)) != account:
            raise Blocked("account_mismatch")
        payload = json.dumps({"type": "authorized_user", "token": credentials.token, "refresh_token": credentials.refresh_token, "client_id": config["installed"]["client_id"], "client_secret": config["installed"]["client_secret"], "token_uri": TOKEN_URI, "scopes": list(SCOPES), "expiry": expiry.isoformat().replace("+00:00", "Z")}, sort_keys=True).encode()
        # Reopen the destination path to detect replaced/symlinked directories.
        check = _directory(target.parent)
        try:
            if (os.fstat(check).st_dev, os.fstat(check).st_ino) != (os.fstat(parent).st_dev, os.fstat(parent).st_ino):
                raise Blocked("output_directory_changed")
        finally:
            os.close(check)
        _publish(parent, target.name, payload)
        return {"status": "connected_readonly", "account": account, "scopes": list(SCOPES), "expiry": expiry.isoformat(), "token_file": str(target), "sha256": hashlib.sha256(payload).hexdigest()}
    except Blocked:
        raise
    except Exception:
        raise Blocked("connection_failed") from None
    finally:
        if server is not None:
            server.server_close()
        os.close(parent)


def list_calendars(account, token_file, *, max_pages=5, timeout=20, session_factory=None):
    """List only calendarList metadata, never events. Refresh stays in memory.

    Bounded pages are not a snapshot or a census of all accessible calendars.
    Continuation tokens remain private; an incomplete run must restart.
    """
    if not isinstance(account, str) or account.count("@") != 1 or len(account) > 254 or any(c.isspace() for c in account):
        raise Blocked("invalid_account")
    if type(max_pages) is not int or not 1 <= max_pages <= 20 or type(timeout) not in (int, float) or not 1 <= timeout <= 120:
        raise Blocked("invalid_listing_bounds")
    try:
        import requests
        original = _private_json(token_file, "token")
        if not isinstance(original, dict) or original.get("type") != "authorized_user" or original.get("token_uri") != TOKEN_URI:
            raise Blocked("invalid_token_credentials")
        scopes = original.get("scopes")
        if not isinstance(scopes, list) or len(scopes) != len(SCOPES) or set(scopes) != set(SCOPES):
            raise Blocked("granted_scopes_not_exact")
        for key in ("token", "refresh_token", "client_id", "client_secret"):
            value = original.get(key)
            if not isinstance(value, str) or not value or len(value) > 16384 or any(c.isspace() for c in value):
                raise Blocked("invalid_token_credentials")
        expiry = dt.datetime.fromisoformat(original["expiry"].replace("Z", "+00:00"))
        if expiry.tzinfo is None:
            raise Blocked("invalid_token_expiry")
        token = original["token"]
        refreshed = False

        def check_file():
            if _private_json(token_file, "token") != original:
                raise Blocked("token_changed")

        with (session_factory or requests.Session)() as session:
            session.trust_env = False

            def request(url, params=None, data=None):
                # The only POST is OAuth refresh. No caller-selectable endpoint.
                if url not in (PROFILE_URI, CALENDAR_LIST_URI, TOKEN_URI) or (url == TOKEN_URI) != (data is not None):
                    raise Blocked("request_forbidden")
                for attempt in range(2 if data is None else 1):
                    check_file()
                    with session.request("POST" if data is not None else "GET", url, params=params, data=data,
                            headers={} if data is not None else {"Authorization": "Bearer " + token},
                            timeout=timeout, allow_redirects=False, stream=True) as response:
                        status = response.status_code
                        if status in (429, 500, 502, 503, 504) and attempt == 0 and data is None:
                            # Do not ignore a provider-directed backoff or sleep unboundedly.
                            if response.headers.get("Retry-After"):
                                return status, {}
                            continue
                        if status != 200:
                            return status, {}
                        body = bytearray()
                        for chunk in response.iter_content(4096):
                            body.extend(chunk)
                            if len(body) > 1024 * 1024:
                                raise Blocked("response_too_large")
                        value = json.loads(body)
                        if not isinstance(value, dict):
                            raise Blocked("invalid_provider_response")
                        check_file()
                        return status, value

            def refresh():
                nonlocal token, refreshed
                if refreshed:
                    raise Blocked("refresh_limit_reached")
                refreshed = True
                status, value = request(TOKEN_URI, data={"grant_type": "refresh_token", **{key: original[key] for key in ("client_id", "client_secret", "refresh_token")}})
                if status != 200:
                    raise Blocked("refresh_http_" + str(status))
                access = value.get("access_token")
                lifetime = value.get("expires_in")
                if (not isinstance(access, str) or not access or len(access) > 16384 or any(c.isspace() for c in access)
                        or type(lifetime) not in (int, float) or not 0 < lifetime <= 86400
                        or value.get("token_type", "").lower() != "bearer"):
                    raise Blocked("invalid_refresh_response")
                if value.get("refresh_token", original["refresh_token"]) != original["refresh_token"]:
                    raise Blocked("refresh_rotation_requires_explicit_persistence")
                if "scope" in value and (not isinstance(value["scope"], str) or sorted(value["scope"].split()) != sorted(SCOPES)):
                    raise Blocked("granted_scopes_not_exact")
                token = access

            def verify():
                status, value = request(PROFILE_URI, {"fields": "emailAddress"})
                if status == 401 and not refreshed:
                    refresh()
                    status, value = request(PROFILE_URI, {"fields": "emailAddress"})
                if status != 200:
                    raise Blocked("identity_http_" + str(status))
                if value.get("emailAddress") != account:
                    raise Blocked("account_mismatch")

            if expiry <= dt.datetime.now(dt.timezone.utc) + dt.timedelta(seconds=30):
                refresh()
            verify()
            result = {"status": "complete", "coverage": "user_calendar_list_only", "calendars": [],
                      "pages_read": 0, "continuation_required": False}
            page_token = None
            seen = set()
            for _ in range(max_pages):
                params = {"maxResults": 250, "showHidden": "true", "showDeleted": "false",
                          "fields": "nextPageToken,items(id,summary,primary,accessRole,timeZone,selected)"}
                if page_token:
                    params["pageToken"] = page_token
                try:
                    status, value = request(CALENDAR_LIST_URI, params)
                    if status == 401 and not refreshed:
                        refresh()
                        verify()
                        status, value = request(CALENDAR_LIST_URI, params)
                    if status != 200:
                        raise Blocked("calendar_list_http_" + str(status))
                    items = value.get("items", [])
                    if not isinstance(items, list) or len(items) > 250:
                        raise Blocked("invalid_calendar_page")
                    cleaned = []
                    for item in items:
                        if not isinstance(item, dict) or not isinstance(item.get("id"), str) or not item["id"]:
                            raise Blocked("invalid_calendar_metadata")
                        row = {}
                        for key in ("id", "summary", "accessRole", "timeZone", "primary", "selected"):
                            if key not in item:
                                continue
                            field = item[key]
                            if key in ("primary", "selected"):
                                if type(field) is not bool:
                                    raise Blocked("invalid_calendar_metadata")
                            elif not isinstance(field, str) or len(field) > 4096 or any(not c.isprintable() for c in field):
                                raise Blocked("invalid_calendar_metadata")
                            if isinstance(field, str) and any(secret in field for secret in (token, *(original[k] for k in ("token", "refresh_token", "client_secret")))):
                                raise Blocked("invalid_calendar_metadata")
                            row[key] = field
                        cleaned.append(row)
                    next_token = value.get("nextPageToken")
                    if next_token is not None and (not isinstance(next_token, str) or not next_token or len(next_token) > 8192):
                        raise Blocked("invalid_page_token")
                    result["calendars"].extend(cleaned)
                    result["pages_read"] += 1
                    if next_token is None:
                        return result
                    if next_token in seen:
                        raise Blocked("pagination_repeated")
                    seen.add(next_token)
                    page_token = next_token
                except Blocked as error:
                    # Identity/credential failures invalidate the whole result.
                    if str(error) not in {"pagination_repeated", "invalid_page_token", "invalid_calendar_page", "invalid_calendar_metadata", "response_too_large"} and not str(error).startswith("calendar_list_http_"):
                        raise
                    result.update(status="partial", reason=str(error), continuation_required=True, continuation="restart_required")
                    return result
                except (requests.RequestException, ValueError, UnicodeError):
                    result.update(status="partial", reason="calendar_page_unavailable", continuation_required=True, continuation="restart_required")
                    return result
            result.update(status="partial", reason="page_limit_reached", continuation_required=True, continuation="restart_with_larger_bound_or_review_limit")
            return result
    except Blocked:
        raise
    except Exception:
        raise Blocked("calendar_listing_failed") from None


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--account", required=True)
    parser.add_argument("--client-file", help="Explicit Desktop JSON file, owner-only 0600 in a 0700 directory")
    parser.add_argument("--token-file", required=True, help="Private token pathname: NEW for OAuth, existing for --list-calendars; owner-only 0700 directory")
    parser.add_argument("--port", type=int, default=0)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--list-calendars", action="store_true", help="Read calendarList metadata using the existing private token; never events")
    parser.add_argument("--max-pages", type=int, default=5, help="Calendar metadata page bound, 1–20")
    args = parser.parse_args(argv)
    try:
        if args.list_calendars:
            if args.client_file or args.port:
                raise Blocked("listing_arguments_conflict")
            result = list_calendars(args.account, args.token_file, max_pages=args.max_pages, timeout=min(args.timeout, 120))
        else:
            if not args.client_file:
                raise Blocked("client_file_required")
            result = connect(args.account, args.client_file, args.token_file, port=args.port, timeout=args.timeout, emit=lambda value: print(json.dumps(value), flush=True))
        print(json.dumps(result), flush=True)
        return 3 if result.get("status") == "partial" else 0
    except (Blocked, OSError) as error:
        print(json.dumps({"status": "blocked", "reason": str(error) if isinstance(error, Blocked) else "private_file_access_failed"}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
