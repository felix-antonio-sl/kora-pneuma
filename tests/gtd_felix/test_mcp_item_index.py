"""Compact MCP index over real filtered, authenticated HTTP item reads."""
import json
import unittest
from aiohttp import web
import test_application as fixtures
import test_mcp as mcp_fixtures
from gtd_felix.mcp import MCPClient, item_index, handle


class ItemIndexTests(unittest.IsolatedAsyncioTestCase):
    asyncSetUp = fixtures.HTTPTests.asyncSetUp
    asyncTearDown = fixtures.HTTPTests.asyncTearDown

    async def test_hundred_large_records_page_completely_without_body_leakage(self):
        marker = 'PRIVATE_LONG_BODY_283819'
        ids = set()
        for index in range(100):
            item = self.service.capture('felix', f'index-{index}', 'Long title ' + 'x' * 200 + marker * 1000,
                source={'provider': 'telegram', 'original_message': {'text': marker * 100}})['item']
            ids.add(item['id'])
        client = MCPClient(self.url, fixtures.OWNER)
        collected, cursor = [], None
        for page in range(5):
            result = await client.call('gtd_read', {'view': 'items', 'cursor': cursor})
            self.assertEqual(100, result['total'])
            self.assertEqual(20, result['returned'])
            self.assertEqual(page * 20, result['offset'])
            self.assertLess(len(json.dumps(result)), 18000)
            self.assertNotIn(marker, json.dumps(result))
            for entry in result['items']:
                self.assertLessEqual(len(entry['title']), 160)
                self.assertTrue(entry['title_truncated'])
                self.assertFalse({'text', 'source', 'original', 'source_revisions', 'materials', 'bases'} & set(entry))
            collected.extend(entry['id'] for entry in result['items'])
            cursor = result['next_cursor']
            if page < 4:
                self.assertIsNotNone(cursor)
                client = MCPClient(self.url, fixtures.OWNER)  # cursor independent of client process
        self.assertIsNone(cursor)
        self.assertEqual(ids, set(collected))
        self.assertEqual(100, len(collected))
        detail = await client.call('gtd_read', {'view': 'item', 'item_id': collected[0]})
        self.assertIn(marker, detail['text'])

    async def test_filters_apply_before_index_and_changed_snapshot_rejects_cursor(self):
        for index in range(4):
            self.service.capture('felix', f'filtered-{index}', ('wanted ' if index < 3 else 'other ') + str(index))
        client = MCPClient(self.url, fixtures.OWNER)
        arguments = {'view': 'items', 'filters': {'text': 'wanted'}, 'page_size': 2}
        first = await client.call('gtd_read', arguments)
        self.assertEqual(3, first['total'])
        with self.assertRaises(ValueError):
            await client.call('gtd_read', {**arguments, 'filters': {}, 'cursor': first['next_cursor']})
        item = self.service.get_item(first['items'][0]['id'])
        self.service.execute('felix', {'operation_id': 'change-index', 'action': 'edit',
            'item_id': item['id'], 'expected_version': item['version'], 'fields': {'notes': 'changed'}})
        with self.assertRaisesRegex(ValueError, 'item_index_snapshot_changed'):
            await client.call('gtd_read', {**arguments, 'cursor': first['next_cursor']})
        response = await handle({'jsonrpc': '2.0', 'id': 1, 'method': 'tools/call',
            'params': {'name': 'gtd_read', 'arguments': {**arguments, 'cursor': first['next_cursor']}}}, client)
        self.assertTrue(response['result']['isError'])
        self.assertEqual('item_index_snapshot_changed', json.loads(response['result']['content'][0]['text'])['error'])

    async def test_invalid_cursor_page_size_and_http_errors_are_not_success_indices(self):
        client = MCPClient(self.url, fixtures.OWNER)
        for size in (0, 51, True, '20'):
            with self.assertRaises(ValueError):
                await client.call('gtd_read', {'view': 'items', 'page_size': size})
        for cursor in ('garbage!', '', 'e30', 1):
            with self.assertRaises(ValueError):
                await client.call('gtd_read', {'view': 'items', 'cursor': cursor})
        denied = await MCPClient(self.url, 'wrong-token').call('gtd_read', {'view': 'items'})
        self.assertEqual('rejected', denied['status'])
        self.assertNotIn('items', denied)
        app = web.Application()
        async def unavailable(request):
            return web.json_response([], status=503)
        app.router.add_get('/v1/items', unavailable)
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, '127.0.0.1', 0)
        await site.start()
        try:
            url = 'http://127.0.0.1:' + str(site._server.sockets[0].getsockname()[1])
            failed = await MCPClient(url, 'fixture').call('gtd_read', {'view': 'items'})
            self.assertEqual('rejected', failed['status'])
            self.assertEqual(503, failed['http_status'])
            self.assertNotIn('items', failed)
        finally:
            await runner.cleanup()

    async def test_executor_index_is_limited_to_live_job_scope(self):
        visible = self.service.capture('felix', 'visible', 'Visible')['item']
        self.service.capture('felix', 'hidden', 'Hidden')
        visible = self.service.execute('felix', {'operation_id': 'clarify', 'action': 'clarify',
            'item_id': visible['id'], 'expected_version': visible['version'], 'fields': {'kind': 'action'}})['item']
        grant = self.service.execute('felix', {'operation_id': 'grant', 'action': 'grant_mandate',
            'item_id': visible['id'], 'expected_version': visible['version'], 'fields': {
                'scope_item_id': visible['id'], 'capabilities': ['prepare_private'], 'actors': ['worker'],
                'completion_criteria': 'Bounded private work'}})
        self.control.config = mcp_fixtures.budget()
        self.control.register_bot('felix', 'bot', {'id': 'worker', 'actor': 'worker', 'state': 'available',
            'source_urn': 'urn:test:worker', 'host': 'synthetic', 'profile': 'fixture',
            'capabilities': ['prepare_private'], 'item_id': visible['id'], 'mandate_id': grant['mandate']['id'],
            'probe_evidence': 'fixture://worker'})
        reserved = self.control.reserve('felix', 'reserve', {'item_id': visible['id'],
            'expected_version': grant['item']['version'], 'capability': 'prepare_private', 'bot_id': 'worker',
            'mandate_id': grant['mandate']['id'], 'purpose': 'Bounded work', 'scope': 'Visible only',
            'max_cost_usd': 1, 'max_runtime_seconds': 50, 'max_retries': 0, 'max_descendants': 0})
        self.assertEqual('reserved', reserved['status'], reserved)
        client = MCPClient(self.url, fixtures.EXECUTOR)
        self.assertEqual(0, (await client.call('gtd_read', {'view': 'items'}))['total'])
        result = await client.call('gtd_read', {'view': 'items', 'job_id': reserved['job_id']})
        self.assertEqual([visible['id']], [item['id'] for item in result['items']])
        self.assertEqual(1, result['total'])

    async def test_summary_bounds_provider_and_dates_and_accepts_max_page(self):
        records = [{'id': str(index), 'version': 1, 'title': 'Title', 'kind': 'capture', 'status': 'active',
            'source': {'provider': 'p' * 1000}, 'due_at': 'd' * 1000, 'review_at': 'r' * 1000} for index in range(51)]
        result = item_index(records, {'page_size': 50})
        self.assertEqual(50, result['returned'])
        self.assertEqual(64, len(result['items'][0]['provider']))
        self.assertEqual(64, len(result['items'][0]['due_at']))
        self.assertEqual({'provider', 'due_at', 'review_at'}, set(result['items'][0]['truncated_fields']))
        self.assertIsNotNone(result['next_cursor'])
