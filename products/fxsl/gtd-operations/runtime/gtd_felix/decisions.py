"""Default typed judgment provider. No tools, domain writes or retry cascade."""
import asyncio
import hashlib
import json
import math
import os
import shlex
import time

import aiohttp

MODEL = 'jev-1.13.0'
POLICY = 'jev-default-2026-09-22'
ENDPOINT = 'https://api.typesafe.ai/v1/systemone'
DEFAULTS = {'provider': 'typesafe', 'model': MODEL, 'api_key_env': 'TYPESAFE_API_KEY',
            'env_file': '/home/felix/.config/secrets/typesafe.env'}
QUESTION_SCHEMA = {'oneOf': [
    {'type': 'object', 'additionalProperties': False,
     'properties': {'type': {'const': kind}, 'instructions': {'type': 'string', 'minLength': 1},
                    'criteria': criteria},
     'required': ['type', 'instructions'] + ([] if kind == 'noul' else ['criteria'])}
    for kind, criteria in [
        ('noul', {'type': 'object', 'additionalProperties': False,
                  'properties': {'true': {'type': 'string'}, 'false': {'type': 'string'}},
                  'required': ['true', 'false']}),
        ('choice', {'type': 'object', 'minProperties': 2, 'maxProperties': 255,
                    'additionalProperties': {'type': 'string', 'minLength': 1}}),
        ('score', {'type': 'array', 'minItems': 2, 'maxItems': 10,
                   'items': {'type': 'string', 'minLength': 1}})]]}
QUESTIONS_SCHEMA = {'type': 'object', 'minProperties': 1, 'maxProperties': 8,
                    'additionalProperties': QUESTION_SCHEMA}


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                    allow_nan=False).encode()).hexdigest()


def probability(value):
    return type(value) in (int, float) and math.isfinite(value) and 0 <= value <= 1


def validate_questions(questions):
    if not isinstance(questions, dict) or not 1 <= len(questions) <= 8:
        raise ValueError('invalid_judgment_questions')
    for identity, question in questions.items():
        if (not isinstance(identity, str) or not identity.strip() or len(identity) > 128
                or not isinstance(question, dict) or set(question) - {'type', 'instructions', 'criteria'}
                or not isinstance(question.get('instructions'), str) or not question['instructions'].strip()):
            raise ValueError('invalid_judgment_question')
        kind, criteria = question.get('type'), question.get('criteria')
        if kind == 'noul':
            if criteria is None and 'criteria' not in question:
                continue
            valid = isinstance(criteria, dict) and set(criteria) == {'true', 'false'}
        elif kind == 'choice':
            valid = (isinstance(criteria, dict) and 2 <= len(criteria) <= 255
                     and all(isinstance(k, str) and k.strip() for k in criteria))
        elif kind == 'score':
            valid = isinstance(criteria, list) and 2 <= len(criteria) <= 10
        else:
            valid = False
        if not valid or not all(isinstance(v, str) and v.strip() for v in
                                (criteria.values() if isinstance(criteria, dict) else criteria)):
            raise ValueError('invalid_judgment_criteria')


class JevClient:
    def __init__(self, config=None):
        if config is not None and not isinstance(config, dict):
            raise ValueError('invalid_decision_configuration')
        self.config = {**DEFAULTS, **(config or {})}
        if (self.config['provider'] != 'typesafe' or self.config['model'] != MODEL
                or set(self.config) != set(DEFAULTS)
                or not isinstance(self.config['api_key_env'], str) or not self.config['api_key_env']
                or (self.config['env_file'] is not None and not isinstance(self.config['env_file'], str))):
            raise ValueError('invalid_decision_configuration')

    def token(self):
        name = self.config['api_key_env']
        value = os.environ.get(name)
        if not value and self.config.get('env_file'):
            from .application import read_private
            # systemd LoadCredential supplies an owner-only, read-only 0400
            # file. Keep 0600 support for the original private env file.
            for line in read_private(self.config['env_file'], allowed_modes=(0o400, 0o600)).decode().splitlines():
                line = line.strip().removeprefix('export ')
                key, sep, raw = line.partition('=')
                if sep and key.strip() == name:
                    parts = shlex.split(raw, comments=True)
                    if len(parts) == 1:
                        value = parts[0]
        if not isinstance(value, str) or not value.strip() or any(c.isspace() for c in value):
            raise ValueError('decision_credentials_unavailable')
        return value

    def request(self, state, questions):
        validate_questions(questions)
        if not isinstance(state, (str, dict, list)):
            raise ValueError('invalid_judgment_state')
        request = {'model': MODEL, 'state': state, 'questions': questions}
        # Local conservative byte bound; not a claim about token equivalence.
        if len(json.dumps(request, ensure_ascii=False, allow_nan=False).encode()) > 24000:
            raise ValueError('judgment_context_too_large')
        return request

    @staticmethod
    def response(value, questions):
        if (not isinstance(value, dict) or value.get('model') != MODEL
                or not isinstance(value.get('answers'), dict) or set(value['answers']) != set(questions)):
            raise ValueError('invalid_judgment_response')
        answers = {}
        for identity, q in questions.items():
            a = value['answers'][identity]
            if not isinstance(a, dict) or a.get('type') != q['type']:
                raise ValueError('invalid_judgment_response')
            if q['type'] == 'noul':
                if not probability(a.get('noul')):
                    raise ValueError('invalid_judgment_response')
                p = a['noul']
                answers[identity] = {'type': 'noul', 'noul': p,
                    'decision': 'yes' if p >= .8 else 'no' if p <= .2 else 'uncertain'}
                continue
            keys = set(q['criteria']) if q['type'] == 'choice' else {str(i) for i in range(len(q['criteria']))}
            probs = a.get('probabilities')
            if (not isinstance(probs, dict) or set(probs) != keys
                    or not all(probability(p) for p in probs.values())
                    or not math.isclose(sum(probs.values()), 1, abs_tol=1e-5)
                    or not probability(a.get('confidence'))):
                raise ValueError('invalid_judgment_response')
            answer = {'type': q['type'], 'probabilities': probs, 'confidence': a['confidence']}
            if q['type'] == 'choice':
                choice = a.get('choice')
                if not isinstance(choice, str) or choice not in keys or probs[choice] < max(probs.values()):
                    raise ValueError('invalid_judgment_response')
                answer['choice'] = choice
            else:
                score = a.get('score')
                if (type(score) not in (int, float) or not math.isfinite(score)
                        or not 0 <= score <= len(keys) - 1
                        or not math.isclose(score, sum(int(k) * p for k, p in probs.items()), abs_tol=1e-5)
                        or a.get('legend') != {str(i): c for i, c in enumerate(q['criteria'])}):
                    raise ValueError('invalid_judgment_response')
                answer.update(score=score, legend=a['legend'])
            answers[identity] = answer
        usage = value.get('usage')
        if not isinstance(usage, dict) or any(type(usage.get(k)) is not int or usage[k] < 0
                                             for k in ('input_tokens', 'output_tokens')):
            raise ValueError('invalid_judgment_response')
        return answers, {k: usage[k] for k in ('input_tokens', 'output_tokens')}

    async def judge(self, state, questions, *, timeout=20):
        request = self.request(state, questions)
        token = self.token()
        started = time.monotonic()
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=min(20, timeout)),
                                         trust_env=False) as session:
            async with session.post(ENDPOINT, json=request, headers={'Authorization': 'Bearer ' + token},
                                    allow_redirects=False) as response:
                if response.status != 200:
                    raise ValueError('judgment_provider_unavailable')
                try:
                    raw = await response.content.readexactly(65537)
                except asyncio.IncompleteReadError as error:
                    raw = error.partial
                if len(raw) > 65536:
                    raise ValueError('invalid_judgment_response')
                answers, usage = self.response(json.loads(raw), questions)
        return {'provider': 'typesafe', 'model': MODEL, 'policy': POLICY,
                'request_sha256': fingerprint(request), 'questions_sha256': fingerprint(questions),
                'answers': answers, 'usage': usage, 'cost_usd': None,
                'duration_seconds': time.monotonic() - started}


class DecisionService:
    """Job-scoped inference with existing control and metadata, never a second job."""
    def __init__(self, service, control, config):
        self.service, self.control = service, control
        self.client = JevClient(config.get('decisions'))

    def guard(self, actor, job_id, payload):
        job = self.control.get_job(job_id)
        if (not job or job['actor'] != actor or not (job.get('native') or {}).get('id')
                or job['capability'] not in {'prepare_private', 'local_work'}):
            raise ValueError('judgment_job_required')
        check = self.control.validate_target(job_id, actor, payload['item_id'], job['capability'])
        valid = self.control.validate(job_id, job['capability'])
        if not check.get('allowed') or not valid.get('allowed') or valid['limits'].get('cost_control', True):
            raise ValueError('judgment_job_unavailable')
        item = self.service.get_item(payload['item_id'])
        if not item or item['version'] != payload['expected_version']:
            raise ValueError('judgment_state_changed')
        remaining = valid['limits']['max_runtime_seconds'] - job['observed_runtime_seconds']
        if remaining <= 0:
            raise ValueError('judgment_time_exhausted')
        return item, min(20, remaining)

    async def run(self, actor, job_id, payload, *, alive):
        required = {'operation_id', 'item_id', 'expected_version', 'state', 'questions'}
        if (not isinstance(payload, dict) or set(payload) != required
                or any(not isinstance(payload[k], str) or not 1 <= len(payload[k]) <= 200
                       for k in ('operation_id', 'item_id'))
                or not isinstance(payload['state'], (str, dict, list))
                or type(payload['expected_version']) is not int or payload['expected_version'] < 1):
            raise ValueError('invalid_judgment_request')
        item, timeout = self.guard(actor, job_id, payload)
        if not alive():
            raise ValueError('judgment_interrupted')
        # The service contributes canonical owner context; supplied evidence stays explicit.
        state = {'item': {k: item[k] for k in ('id', 'version', 'title', 'text', 'outcome',
                 'completion_criteria', 'status', 'mandate_id') if k in item}, 'evidence': payload['state']}
        request = self.client.request(state, payload['questions'])
        digest = fingerprint(request)
        key = 'judgment:receipt:' + fingerprint([actor, job_id, payload['operation_id']])
        counter = 'judgment:count:' + job_id
        with self.service.store.transaction():
            old = self.service._meta(key)
            if old:
                if old['request_sha256'] != digest:
                    raise ValueError('judgment_operation_conflict')
                return old
            if self.service._meta(counter, 0) >= 16:
                raise ValueError('judgment_job_limit')
            receipt = {'status': 'uncertain', 'error': 'judgment_incomplete',
                       'operation_id': payload['operation_id'], 'job_id': job_id,
                       'item_id': item['id'], 'item_version': item['version'],
                       'request_sha256': digest, 'provider': 'typesafe', 'model': MODEL, 'policy': POLICY,
                       'usage': {'input_tokens': None, 'output_tokens': None}, 'cost_usd': None,
                       'time_accounting': 'included_in_parent_wall_time'}
            self.service._set_meta(key, receipt)
            self.service._set_meta(counter, self.service._meta(counter, 0) + 1)
        try:
            result = await self.client.judge(state, payload['questions'], timeout=timeout)
            receipt.update(result)
            self.guard(actor, job_id, payload)
            if not alive():
                raise ValueError('judgment_interrupted')
            receipt.update(status='evaluated')
            receipt.pop('error', None)
        except (Exception, asyncio.CancelledError):
            # Do not return stale answers or provider text. Preserve any known usage.
            receipt.pop('answers', None)
            receipt.update(status='uncertain', error='judgment_unavailable')
        with self.service.store.transaction():
            self.service._set_meta(key, receipt)
        return receipt
