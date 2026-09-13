"""Durable explicit native provider selection; never falls back between providers."""
import asyncio
import json


class AdapterRouter:
    NATIVE = {'hermes': {'hermes', 'hermes-kanban', 'gtd-hermes-admission'},
              'codex': {'codex-app-server'}}

    def __init__(self, control, hermes, codex, config):
        self.control, self.store = control, control.service.store
        self.adapters = {'hermes': hermes, 'codex': codex}
        if not isinstance(config, dict) or not isinstance(config.get("providers", {}), dict):
            raise ValueError("invalid_adapter_config")
        if any(not isinstance(bot, str) or not bot or provider not in self.NATIVE
               for bot, provider in config.get("providers", {}).items()):
            raise ValueError("invalid_adapter_config")
        self.config = dict(config)
        self.legacy = codex is None and not self.config

    def provider(self, bot_id):
        provider = 'hermes' if self.legacy else self.config.get('providers', {}).get(bot_id)
        if provider not in self.NATIVE or self.adapters[provider] is None:
            raise ValueError('explicit_adapter_required')
        return provider

    def workspace(self, bot_id):
        provider = self.provider(bot_id)
        if provider != 'codex': return None
        return self.adapters[provider]._route(bot_id)['workspace']

    def _select(self, job_id):
        job = self.control.get_job(job_id)
        if not job: raise ValueError('job_not_found')
        provider = self.provider(job['bot_id'])
        if provider == 'codex' and self.control.service.actor_role(job['actor']) != 'executor':
            raise ValueError('codex_executor_required')
        native = job.get('native')
        if native and native.get('provider') not in self.NATIVE[provider]:
            raise ValueError('native_provider_mismatch')
        value = {'provider': provider, 'bot_id': job['bot_id'], 'route': job['route']}
        key = 'adapter:job:' + job_id
        with self.store.transaction() as db:
            row = db.execute('SELECT value FROM metadata WHERE key=?', (key,)).fetchone()
            if row and json.loads(row[0]) != value: raise ValueError('adapter_selection_changed')
            if not row: db.execute('INSERT INTO metadata VALUES(?,?)', (key, json.dumps(value, sort_keys=True)))
        return provider, self.adapters[provider]

    async def discover(self, bot_id):
        try:
            provider = self.provider(bot_id)
            response = await self.adapters[provider].discover(bot_id)
            return {**response, 'adapter_provider': provider}
        except ValueError as error:
            return {'status': 'unavailable', 'reason': str(error)}

    async def _call(self, method, job_id, *args, **kwargs):
        try:
            provider, adapter = self._select(job_id)
            if method == 'steer' and provider == 'hermes': kwargs.pop('operation_id', None)
            response = await getattr(adapter, method)(job_id, *args, **kwargs)
            # A provider must not bind a job to another native after selection.
            self._select(job_id)
            return response
        except ValueError as error:
            return {'status': 'uncertain', 'job_id': job_id, 'terminal': False, 'error': str(error)}

    async def submit(self, job_id, prompt, durable=False):
        return await self._call('submit', job_id, prompt, durable=durable)

    async def poll(self, job_id): return await self._call('poll', job_id)
    async def reconcile(self, job_id): return await self._call('reconcile', job_id)
    async def stop(self, job_id): return await self._call('stop', job_id)
    async def steer(self, job_id, text, operation_id=None):
        return await self._call('steer', job_id, text, operation_id=operation_id)

    async def close(self):
        closers = [getattr(adapter, 'close', None) for adapter in self.adapters.values()]
        results = await asyncio.gather(*(close() for close in closers if close), return_exceptions=True)
        for result in results:
            if isinstance(result, BaseException): raise result
