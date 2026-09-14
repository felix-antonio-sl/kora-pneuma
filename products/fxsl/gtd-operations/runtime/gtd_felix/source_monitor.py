"""Non-agentic source polling and durable, content-free coverage summaries."""
import asyncio
import copy
from datetime import datetime, timezone
from types import SimpleNamespace

from .domain import fingerprint, now
from .google_sources import GoogleSources
from .google_transport import GoogleTransport
from .source_error_codes import (
    BRIDGE_ERRORS,
    SUMMARY_ERRORS,
    SYNC_ERRORS,
    summary_error as _summary_error,
)
from .source_sync import SourceSync

PREFIX = 'source-monitor:'


def validate_google(config):
    if not isinstance(config, dict) or set(config) != {'accounts', 'poll_interval_seconds', 'stale_after_seconds'}:
        raise ValueError('invalid_google_config')
    interval, stale = config['poll_interval_seconds'], config['stale_after_seconds']
    if type(interval) is not int or not 1 <= interval <= 86400 or type(stale) is not int or not interval <= stale <= 604800:
        raise ValueError('invalid_google_intervals')
    accounts = config['accounts']
    if not isinstance(accounts, dict) or not accounts:
        raise ValueError('explicit_google_accounts_required')
    seen, identities, account_names = set(), set(), set()
    for alias, entry in accounts.items():
        if not isinstance(alias, str) or not alias or not isinstance(entry, dict) or set(entry) != {'transport', 'sources'}:
            raise ValueError('invalid_google_account')
        transport = GoogleTransport(entry['transport']) # constructor is intentionally inert
        if transport.account in account_names:
            raise ValueError('duplicate_google_account')
        account_names.add(transport.account)
        sources = GoogleSources(SimpleNamespace(store=None), transport, entry['sources'])
        for source_id in entry['sources']:
            cfg, _, partition = sources._source(source_id)
            identity = (partition['provider'], partition['account'], partition['collection'])
            if source_id in seen or identity in identities:
                raise ValueError('duplicate_google_source')
            if cfg['account'] != transport.account or (cfg['provider'] == 'gmail' and not transport.gmail) or (cfg['provider'] == 'calendar' and cfg['calendar_id'] not in transport.calendars):
                raise ValueError('google_account_or_collection_mismatch')
            seen.add(source_id); identities.add(identity)
    return config


def coverage(service):
    """A pure read: freshness is recomputed, including after a process restart."""
    with service.store.lock:
        rows = service.store.db.execute('SELECT key,value FROM metadata WHERE key LIKE ?', (PREFIX + '%',)).fetchall()
        import json
        summaries = [json.loads(row['value']) for row in rows]
    stamp = datetime.now(timezone.utc).timestamp()
    for summary in summaries:
        read_at = summary.get('coverage_at')
        stale = not read_at or stamp - datetime.fromisoformat(read_at).timestamp() > summary['stale_after_seconds']
        summary['stale'] = bool(stale)
        summary['current'] = bool(summary.get('configured') and not stale and summary['health'] == 'complete' and summary['originals_complete'] and summary['projection'] == 'current')
    configured = [x for x in summaries if x.get('configured')]
    return {'sources': sorted(summaries, key=lambda x: x['source_id']),
            'configured_count': len(configured), 'external_sources_applicable': bool(configured),
            'external_sources_current': all(x['current'] for x in configured) if configured else None}


def retire_sources(service):
    with service.store.transaction():
        for summary in coverage(service)['sources']:
            summary.pop('stale', None); summary.pop('current', None)
            summary['configured'] = False
            service._set_meta(PREFIX + summary['source_id'], summary)


class SourceMonitor:
    def __init__(self, service, config, *, transport_factory=GoogleTransport):
        validate_google(config)
        self.service, self.config = service, copy.deepcopy(config)
        self.transports, self.sources, self._locks, self._tasks = {}, {}, {}, []
        self._closed = False
        for alias, entry in self.config['accounts'].items():
            transport = transport_factory(entry['transport'])
            self.transports[alias] = transport
            adapter = GoogleSources(SourceSync(service), transport, entry['sources'])
            for source_id in entry['sources']:
                self.sources[source_id] = (alias, adapter)
                self._locks[source_id] = asyncio.Lock()
        # No network/credential read. Configuration itself establishes unread inventory.
        with service.store.transaction():
            for summary in coverage(service)['sources']:
                summary.pop('stale', None); summary.pop('current', None)
                summary['configured'] = summary['source_id'] in self.sources
                service._set_meta(PREFIX + summary['source_id'], summary)
            for source_id, (alias, adapter) in self.sources.items():
                info = adapter.inspect(source_id)
                scope = {'partition': info['partition'], 'effective_parameters': info['effective_parameters'], 'coverage_contract': info['coverage_contract']}
                binding = fingerprint(scope)
                old = service._meta(PREFIX + source_id)
                if old and old['scope_fingerprint'] == binding:
                    old.update(configured=True, account_alias=alias, stale_after_seconds=config['stale_after_seconds'])
                    service._set_meta(PREFIX + source_id, old)
                else:
                    service._set_meta(PREFIX + source_id, {'source_id': source_id, 'account_alias': alias, 'scope': scope,
                        'scope_fingerprint': binding, 'configured': True, 'configured_at': now(),
                        'stale_after_seconds': config['stale_after_seconds'], 'health': 'not_read',
                        'enumeration': 'not_read', 'originals_complete': False, 'projection': 'not_read',
                        'pending_reads': 0, 'semantic_review': info.get('coverage_contract', {}).get('semantic_review'), 'coverage_at': None, 'last_pass_at': None, 'last_success_at': None,
                        'last_error': None, 'retry_after_seconds': None, 'consecutive_failures': 0})

    async def read_agenda(self, account_alias, *, start, end, timezone, calendar_ids=None):
        from .calendar_effects import CalendarAgenda, _instant, _zone
        if self._closed or not isinstance(account_alias,str) or account_alias not in self.transports:
            raise ValueError('agenda_account_unavailable')
        transport=self.transports[account_alias]
        allowed=self.config['accounts'][account_alias]['transport'].get('calendar_ids',[])
        selected=list(allowed) if calendar_ids is None else calendar_ids
        if (not isinstance(selected,list) or not selected or not all(isinstance(c,str) and c in allowed for c in selected)
                or len(set(selected))!=len(selected)):
            raise ValueError('agenda_calendars_not_authorized')
        if not all(isinstance(v,str) and v for v in (start,end,timezone)):
            raise ValueError('agenda_window_required')
        lower,upper=_instant(start),_instant(end);_zone(timezone)
        if not 0<(upper-lower).total_seconds()<=366*86400: raise ValueError('finite_window_required')
        account=self.config['accounts'][account_alias]['transport']['account']
        observation={'account_alias':account_alias,'account':account,'verified_account':None,
            'window':{'start':start,'end':end,'timezone':timezone},'calendar_ids':list(selected),
            'observed_at':now(),'synchronization_coverage_updated':False}
        try:
            result=await CalendarAgenda(transport,account,selected).read(start,end,timezone)
            observation['verified_account']=account if transport.authenticated_account==account else None
            safe_errors={'pagination_not_progressing','page_limit_reached','calendar_read_failed',
                'window_event_limit','event_changed_during_pagination','calendar_transport_or_shape_error'}
            for calendar in result['calendars']:
                if 'error' in calendar and calendar['error'] not in safe_errors: calendar['error']='calendar_read_incomplete'
            return {**result,**observation,'status':'complete' if result['status']=='complete' else 'degraded'}
        except asyncio.CancelledError: raise
        except Exception:
            return {**observation,'status':'degraded','coverage_kind':'expanded_window',
                'error':'agenda_read_failed','calendars':[],'overlaps':[]}

    def inspect(self):
        return coverage(self.service)

    def _save(self, source_id, info, *, error=None):
        state = info.get('sync') or {}
        transport = self.transports[self.sources[source_id][0]].inspect()
        with self.service.store.transaction():
            summary = self.service._meta(PREFIX + source_id)
            summary.update(last_pass_at=now(), health='degraded' if error else info['health'],
                enumeration=state.get('coverage', 'not_read'), projection=state.get('projection', 'not_read'),
                originals_complete=bool(info['originals_complete']), pending_reads=len(info['pending_reads']),
                semantic_review=info.get('coverage_contract', {}).get('semantic_review'),
                priority=copy.deepcopy(info.get('priority')),
                coverage_at=state.get('coverage_completed_at'), projection_at=state.get('projection_completed_at'),
                coverage_started_at=state.get('coverage_started_at'), last_error=error,
                retry_after_seconds=transport.get('retry_after_seconds'))
            if summary['health'] == 'complete' and summary['originals_complete'] and summary['projection'] == 'current':
                summary['last_success_at'] = summary['last_pass_at']
                summary['consecutive_failures'] = 0
            elif summary['health'] == 'degraded':
                summary['consecutive_failures'] += 1
            self.service._set_meta(PREFIX + source_id, summary)

    async def run_once(self, source_id):
        if self._closed or source_id not in self.sources:
            raise ValueError('source_monitor_closed_or_unknown')
        async with self._locks[source_id]:
            alias, adapter = self.sources[source_id]
            transport = self.transports[alias]
            error = None
            try:
                if adapter.config[source_id].get('scope') == 'selective_since':
                    # No refresh is claimed without an actual job-bound pass.
                    return next(x for x in self.inspect()['sources'] if x['source_id'] == source_id)
                if transport.authenticated_account is None:
                    await transport.connect()
                info = await adapter.synchronize(source_id)
                if info['health'] == 'degraded':
                    status = transport.inspect().get('last_http_status')
                    error = 'http_' + str(status) if status in {401,403,429} else 'source_read_degraded'
            except asyncio.CancelledError:
                self._save(source_id, adapter.inspect(source_id), error='pass_cancelled')
                raise
            except Exception:
                # Neither transport exceptions nor provider content enter durable summaries.
                status = transport.inspect().get('last_http_status')
                error = 'http_' + str(status) if status in {401,403,429} else 'source_read_failed'
                info = adapter.inspect(source_id)
            self._save(source_id, info, error=error)
            return next(x for x in self.inspect()['sources'] if x['source_id'] == source_id)

    async def evaluate_once(self, source_id, evaluator, projection_guard=None):
        """Only a job-bound caller supplies this evaluator; shared adapters stay inert."""
        if self._closed or source_id not in self.sources:
            raise ValueError('source_monitor_closed_or_unknown')
        async with self._locks[source_id]:
            alias, shared = self.sources[source_id]
            transport = self.transports[alias]
            adapter = GoogleSources(SourceSync(self.service), transport, shared.config, evaluator=evaluator, projection_guard=projection_guard)
            error = None
            try:
                if transport.authenticated_account is None:
                    await transport.connect()
                info = await adapter.synchronize(source_id)
                if info['health'] == 'degraded':
                    error = _summary_error(info)
            except asyncio.CancelledError:
                self._save(source_id, adapter.inspect(source_id), error='selection_interrupted')
                raise
            except Exception:
                info = adapter.inspect(source_id)
                error = 'selection_unavailable'
            self._save(source_id, info, error=error)
            return next(x for x in self.inspect()['sources'] if x['source_id'] == source_id)

    async def _run(self, source_id):
        while True:
            result = await self.run_once(source_id)
            base = self.config['poll_interval_seconds']
            delay = min(86400, base * 2 ** min(result['consecutive_failures'], 10))
            delay = max(delay, min(604800, result.get('retry_after_seconds') or 0))
            await asyncio.sleep(delay)

    async def start(self):
        if self._closed:
            raise ValueError('source_monitor_closed')
        if not self._tasks:
            self._tasks = [asyncio.create_task(self._run(source_id)) for source_id in self.sources]

    async def close(self):
        self._closed = True
        for task in self._tasks:
            task.cancel()
        await asyncio.gather(*self._tasks, return_exceptions=True)
        self._tasks.clear()
        await asyncio.gather(*(transport.close() for transport in self.transports.values()))
