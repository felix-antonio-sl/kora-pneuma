"""E63: entrada proporcional con referencias registradas y alcanzables (MCP real)."""
import json
import re
import shutil
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
from gtd_felix.mcp import ALLOWED_REFERENCES, MCPClient, TOOLS, handle, instructions
from gtd_felix.service import GTDService

OWNER, PRINCIPAL = 'synthetic-owner-token', 'synthetic-principal-token'
PRODUCT = Path(__file__).resolve().parents[2] / 'products' / 'fxsl' / 'gtd-operations'


def budget():
    return dict(period_start=datetime.now(timezone.utc).isoformat(), period_seconds=3600,
        max_cost_usd=20, max_runtime_seconds=2000, recovery_cost_usd=2, recovery_runtime_seconds=100,
        max_job_runtime_seconds=300, max_retries=0, max_descendants=2, max_active=1)


class SkillProportionTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.service = GTDService(self.root / 'data', executor_actors=['history-worker'])
        self.control = ExecutionControl(self.service, budget())
        self.item = self.service.capture('felix', 'capture', 'Synthetic E63 matter')['item']
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

    def test_entry_references_are_all_registered_and_reachable(self):
        entry = (PRODUCT / 'content.md').read_text()
        mentioned = set(re.findall(r'references/[A-Za-z0-9_.]+\.md', entry))
        self.assertEqual({'references/operations.md', 'references/flujos.md'}, mentioned)
        self.assertTrue(set(mentioned) <= set(ALLOWED_REFERENCES))
        self.assertEqual(sorted(ALLOWED_REFERENCES - {'SKILL.md'}),
            sorted(TOOLS[0]['inputSchema']['properties']['reference']['enum'][1:]))

    def test_flujos_loads_bounded_with_section_index(self):
        first = instructions('references/flujos.md')
        self.assertEqual('references/flujos.md', first['reference'])
        self.assertIsNotNone(first['next_offset'])
        self.assertLessEqual(len(first['content']), 8000)
        titles = [s['title'] for s in first['sections']]
        for expected in ('A · Capturar', 'B · Derivar', 'C · Comprobar', 'D · Revisar'):
            self.assertTrue(any(t.startswith(expected) for t in titles), titles)
        rest = instructions('references/flujos.md', offset=first['next_offset'])
        self.assertEqual(first['next_offset'], rest['offset'])
        self.assertNotEqual(first['content'], rest['content'])

    def test_unregistered_reference_still_rejected(self):
        with self.assertRaises(ValueError):
            instructions('references/other.md')

    def test_moved_conditions_stay_reachable(self):
        text = (PRODUCT / 'references' / 'flujos.md').read_text()
        for anchor in ('put_material', 'source_material', 'source_coverage', 'intent_basis',
                'destination="existing"', 'apply_human_instruction', 'next_offset'):
            self.assertIn(anchor, text)

    def test_conserved_entry_block_is_identical_and_indexed(self):
        import subprocess
        src71 = subprocess.run(['git', 'show',
            '71a319d:products/fxsl/gtd-operations/content.md'],
            capture_output=True, text=True, cwd=Path(__file__).resolve().parents[2]).stdout
        block = src71[src71.find('La conversación es continua:'):src71.find('## A ·')].rstrip('\n')
        self.assertEqual(3678, len(src71[src71.find('La conversación es continua:'):src71.find('## A ·')]))
        flujos = (PRODUCT / 'references' / 'flujos.md').read_text()
        head, sep, tail = flujos.partition('## Conversación, fuentes y saldo\n\n')
        self.assertTrue(sep)
        self.assertEqual(block, tail.rstrip('\n'))
        entry = (PRODUCT / 'content.md').read_text()
        self.assertIn('Conversación, fuentes y saldo', entry)
        self.assertIn('una sola respuesta natural sin repetir acuse', entry)
        self.assertIn('Guardar material no cumple por sí solo', entry)
        self.assertIn('no prueban por sí solos que la\n   interpretación', entry)
        ops = (PRODUCT / 'references' / 'operations.md').read_text()
        self.assertIn('`references/operations.md` y `references/flujos.md`', ops)

    async def test_rendered_bundle_reads_prepare_and_persists(self):
        # Rendered bundle copy: frontmatter + entry, references alongside.
        bundle = self.root / 'skill'
        (bundle / 'references').mkdir(parents=True)
        (bundle / 'SKILL.md').write_text('---\nname: gtd-operations\n---\n\n'
            + (PRODUCT / 'content.md').read_text())
        for ref in ('references/operations.md', 'references/flujos.md'):
            shutil.copy(PRODUCT / ref, bundle / ref)
        rooted = MCPClient(self.url, PRINCIPAL, instruction_root=bundle)
        entry = await rooted.call('gtd_read', {'view': 'instructions'})
        self.assertIn('Obligaciones nucleares', entry['content'])
        flows = await rooted.call('gtd_read', {'view': 'instructions', 'reference': 'references/flujos.md'})
        self.assertIn('A · Capturar', json.dumps([s['title'] for s in flows['sections']], ensure_ascii=False))
        item = await rooted.call('gtd_read', {'view': 'item', 'item_id': self.item['id'], 'detail': 'full'})
        command = {'operation_id': 'e63-bundle-put', 'action': 'put_material', 'item_id': self.item['id'],
            'expected_version': item['version'], 'fields': {'title': 'Synthetic', 'content': 'Synthetic useful text'}}
        applied = await rooted.call('gtd_command', {'job_id': self.job, 'command': command})
        self.assertEqual('applied', applied['status'])
        mats = await rooted.call('gtd_read', {'view': 'materials', 'item_id': self.item['id']})
        self.assertEqual(1, len(mats if isinstance(mats, list) else mats['materials']))
        again = await rooted.call('gtd_command', {'job_id': self.job, 'command': command})
        self.assertIn(again['status'], {'applied', 'already_applied'})


if __name__ == '__main__':
    unittest.main()
