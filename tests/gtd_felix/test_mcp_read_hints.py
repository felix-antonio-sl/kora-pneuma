"""E61: rejected E60 calls get closed codes+hints; corrected calls persist (real MCP->HTTP->SQLite)."""
import json
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path
import tempfile

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from aiohttp import web
from gtd_felix.application import create_app
from gtd_felix.control import ExecutionControl
from gtd_felix.mcp import MCPClient, ReadInputError, handle
from gtd_felix.service import GTDService

OWNER, PRINCIPAL = 'synthetic-owner-token', 'synthetic-principal-token'


def budget():
    return dict(period_start=datetime.now(timezone.utc).isoformat(), period_seconds=3600,
        max_cost_usd=20, max_runtime_seconds=2000, recovery_cost_usd=2, recovery_runtime_seconds=100,
        max_job_runtime_seconds=300, max_retries=0, max_descendants=2, max_active=1)


class ReadHintTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.service = GTDService(self.root / 'data', executor_actors=['history-worker'])
        self.control = ExecutionControl(self.service, budget())
        self.item = self.service.capture('felix', 'capture', 'Synthetic E61 matter')['item']
        self.bot = dict(id='principal', state='available', source_urn='urn:test:principal', host='synthetic', profile='fixture',
            capabilities=['prepare_private'], item_id=self.item['id'], mandate_id=None, probe_evidence='fixture://route')
        self.control.register_bot('felix', 'bot', self.bot)
        self.request = dict(item_id=self.item['id'], expected_version=self.item['version'], capability='prepare_private',
            bot_id='principal', purpose='Prepare', scope='Synthetic', mandate_id=None,
            max_cost_usd=4, max_runtime_seconds=200, max_retries=0, max_descendants=1)
        self.job = self.control.reserve('gtd-felix', 'reserve', self.request)['job_id']
        config = dict(data_dir=str(self.root / 'data'), actors={'owner': 'felix', 'principal': 'gtd-felix', 'executors': ['history-worker']},
            api_tokens={OWNER: 'felix', PRINCIPAL: 'gtd-felix'})
        self.runner = web.AppRunner(create_app(self.service, self.control, config), access_log=None)
        await self.runner.setup()
        site = web.TCPSite(self.runner, '127.0.0.1', 0)
        await site.start()
        self.url = 'http://127.0.0.1:' + str(site._server.sockets[0].getsockname()[1])
        self.client = MCPClient(self.url, PRINCIPAL)

    async def asyncTearDown(self):
        await self.runner.cleanup()
        self.service.close()
        self.temp.cleanup()

    async def rejected(self, name, arguments):
        result = await handle({'jsonrpc': '2.0', 'id': 1, 'method': 'tools/call',
            'params': {'name': name, 'arguments': arguments}}, self.client)
        self.assertTrue(result['result']['isError'])
        return json.loads(result['result']['content'][0]['text'])

    async def test_reference_without_view_gets_closed_code_and_hint(self):
        # Exact E60 shape: {"reference": "references/operations.md"} (no view).
        with self.assertRaises(ReadInputError) as caught:
            await self.client.call('gtd_read', {'reference': 'references/operations.md'})
        self.assertEqual('reference_requires_instructions_view', str(caught.exception))
        receipt = await self.rejected('gtd_read', {'reference': 'references/operations.md'})
        self.assertEqual('reference_requires_instructions_view', receipt['error'])
        self.assertIn('view="instructions"', receipt['hint'])
        # Corrected call reads the reference over HTTP.
        value = await self.client.call('gtd_read', {'view': 'instructions', 'reference': 'references/operations.md'})
        self.assertEqual('references/operations.md', value['reference'])
        self.assertIn('put_material', value['content'])

    async def test_materials_without_top_level_item_id_gets_closed_code(self):
        # Exact E60 shape: context.item_id present, top-level item_id absent.
        arguments = {'view': 'materials', 'context': {'item_id': self.item['id']}}
        with self.assertRaises(ReadInputError) as caught:
            await self.client.call('gtd_read', arguments)
        self.assertEqual('read_item_id_required', str(caught.exception))
        receipt = await self.rejected('gtd_read', arguments)
        self.assertEqual('read_item_id_required', receipt['error'])
        self.assertIn('top level', receipt['hint'])
        # Corrected call reads the (empty) material list.
        value = await self.client.call('gtd_read', {'view': 'materials', 'item_id': self.item['id']})
        self.assertEqual([], value if isinstance(value, list) else value['materials'])
        value = await self.client.call('gtd_read', {'view': 'item', 'item_id': self.item['id'], 'detail': 'full'})
        self.assertEqual(self.item['id'], value['id'])

    async def test_text_plus_filename_still_rejected_but_hinted_then_persists(self):
        fields = {'title': 'Synthetic plan', 'content': 'Synthetic three-step text', 'filename': 'plan.txt',
            'mime_type': 'text/plain; charset=utf-8'}
        command = {'operation_id': 'e61-put-01', 'action': 'put_material', 'item_id': self.item['id'],
            'expected_version': self.item['version'], 'fields': fields}
        before = self.service.get_item(self.item['id'])['version']
        rejected = await self.client.call('gtd_command', {'job_id': self.job, 'command': command})
        self.assertEqual('rejected', rejected['status'])
        self.assertEqual('invalid_material_content_choice', rejected['error'])
        self.assertIn('content only', rejected['hint'])
        self.assertEqual(before, self.service.get_item(self.item['id'])['version'])
        # Corrected: same text, content only, fresh operation_id (idempotency
        # binds the original operation_id to its rejected payload).
        fixed = dict(command, operation_id='e61-put-01b',
            fields={'title': 'Synthetic plan', 'content': 'Synthetic three-step text'})
        applied = await self.client.call('gtd_command', {'job_id': self.job, 'command': fixed})
        self.assertEqual('applied', applied['status'])
        materials = self.service.materials(self.item['id'])
        self.assertEqual(1, len(materials))
        body = self.service.read_material(self.item['id'], materials[0]['id'], materials[0]['version'])
        self.assertIn('Synthetic three-step text', json.dumps(body, ensure_ascii=False))
        # Idempotent replay: same payload + same operation_id, no duplicate.
        again = await self.client.call('gtd_command', {'job_id': self.job, 'command': fixed})
        self.assertIn(again['status'], {'applied', 'already_applied'})
        self.assertIn('new operation_id', rejected['hint'])
        # Corrected payload under the rejected operation_id stays rejected
        # (idempotency binds it); the fix needs its own operation_id.
        clash = await self.client.call('gtd_command', {'job_id': self.job,
            'command': dict(fixed, operation_id='e61-put-01')})
        self.assertIn(clash['status'], {'rejected', 'conflict'})
        self.assertEqual(1, len(self.service.materials(self.item['id'])))
        self.assertEqual(1, len(self.service.materials(self.item['id'])))

    async def test_negative_choices_keep_rejection_without_leak(self):
        base = {'operation_id': 'e61-put-02', 'action': 'put_material', 'item_id': self.item['id'],
            'expected_version': self.service.get_item(self.item['id'])['version']}
        for op, fields in [
                ('e61-put-02', {'content': 'x', 'content_base64': 'eA==', 'filename': 'a.potx',
                    'mime_type': 'application/vnd.openxmlformats-officedocument.presentationml.presentation'}),
                ('e61-put-03', {'content': 'x', 'source_material': {'item_id': self.item['id'], 'material_id': 'm',
                    'version': 1, 'sha256': '0' * 64}})]:
            rejected = await self.client.call('gtd_command', {'job_id': self.job,
                'command': {**base, 'operation_id': op, 'fields': fields}})
            self.assertEqual('invalid_material_content_choice', rejected['error'])
            self.assertIn('hint', rejected)
        # Unknown views still fail closed without internals.
        receipt = await self.rejected('gtd_read', {'view': 'no_such_view'})
        self.assertEqual('tool_or_transport_failed', receipt['error'])
        self.assertNotIn('hint', receipt)


if __name__ == '__main__':
    unittest.main()
