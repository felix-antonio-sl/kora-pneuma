"""Synthetic PPTX package bytes through domain, HTTP, MCP, CLI and restore.

Fixture identity/CRC is tested; no desktop editor opening is claimed.
"""
import asyncio
import base64
import copy
import hashlib
import io
import json
import os
import re
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import zipfile

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from gtd_felix.service import GTDService
from gtd_felix.material_files import PPTX_MIME, MAX_FILE, decode_pptx
from gtd_felix.mcp import FIELD_SCHEMAS
import test_mcp as mcp_fixture
import aiohttp
from aiohttp import web
from gtd_felix.application import create_app


def pptx(text='Editable synthetic title'):
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, 'w', zipfile.ZIP_DEFLATED) as archive:
        def write(name, content):
            info = zipfile.ZipInfo(name, date_time=(2026, 9, 11, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, content)
        write('[Content_Types].xml', '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Override PartName="/ppt/presentation.xml" ContentType="'+PPTX_MIME+'.main+xml"/></Types>')
        write('_rels/.rels', '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/></Relationships>')
        write('ppt/presentation.xml', '<p:presentation xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"><p:sldIdLst/></p:presentation>')
        write('ppt/slides/slide1.xml', '<p:sld xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><p:cSld><p:spTree><p:sp><p:txBody><a:p><a:r><a:t>'+text+'</a:t></a:r></a:p></p:txBody></p:sp></p:spTree></p:cSld></p:sld>')
    return stream.getvalue()


def fields(data=None):
    return {'content_base64': base64.b64encode(pptx() if data is None else data).decode(),
        'filename': 'reunión.pptx', 'mime_type': PPTX_MIME}


class MaterialFileTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.service = GTDService(self.root / 'data')
        self.item = self.service.capture('felix', 'capture', 'Prepare a private presentation')['item']

    def tearDown(self):
        self.service.close(); self.temp.cleanup()

    def command(self, values, operation='material', item=None, actor='gtd-felix'):
        target = item or self.service.get_item(self.item['id'])
        return self.service.execute(actor, {'operation_id': operation, 'action': 'put_material',
            'item_id': target['id'], 'expected_version': target['version'], 'fields': values})

    def test_identical_bytes_restart_export_restore_and_text_boundary(self):
        data = pptx()
        receipt = self.command(fields(data))
        self.assertEqual(receipt['status'], 'applied', receipt)
        material = self.service.materials(self.item['id'])[0]
        self.assertEqual(material['original']['filename'], 'reunión.pptx')
        identity, version = material['id'], material['version']
        self.service.close(); self.service = GTDService(self.root / 'data')
        read = self.service.read_material_file(self.item['id'], identity, version)
        self.assertEqual(read['data'], data)
        self.assertEqual(read['sha256'], hashlib.sha256(data).hexdigest())
        with self.assertRaisesRegex(ValueError, 'material_not_textual'):
            self.service.read_material(self.item['id'], identity, version)
        archive = self.root / 'backup.zip'; self.service.export(archive)
        restored = GTDService.restore(archive, self.root / 'restored')
        try:
            self.assertTrue(restored.recovery_required)
            self.assertEqual(restored.read_material_file(self.item['id'], identity, version)['data'], data)
            self.assertEqual(restored.materials(self.item['id']), self.service.materials(self.item['id']))
        finally: restored.close()
        legacy = self.command({'content': 'Legacy UTF-8 ñ'}, 'text')
        self.assertEqual(legacy['status'], 'applied')
        latest = self.service.materials(self.item['id'])[-1]
        self.assertEqual(self.service.read_material(self.item['id'], latest['id'], 1)['content'], 'Legacy UTF-8 ñ')

    @unittest.skipUnless(os.environ.get('GTD_PPTX_PYTHON'), 'separate prepared python-pptx environment not selected')
    def test_real_python_pptx_generated_file_remains_editable_after_restore(self):
        python = os.environ['GTD_PPTX_PYTHON']
        source = self.root / 'real.pptx'
        subprocess.run([python, '-E', '-s', '-B', '-c',
            "from pptx import Presentation; import sys; p=Presentation(); s=p.slides.add_slide(p.slide_layouts[1]); "
            "s.shapes.title.text='Synthetic editable title'; p.save(sys.argv[1])", str(source)], check=True, capture_output=True)
        data = source.read_bytes()
        result = self.command(fields(data))
        self.assertEqual(result['status'], 'applied', result)
        material = self.service.materials(self.item['id'])[0]
        self.service.export(self.root/'real.zip')
        restored = GTDService.restore(self.root/'real.zip', self.root/'real-restored')
        try:
            fetched = restored.read_material_file(self.item['id'], material['id'], 1)['data']
            self.assertEqual(fetched, data)
            download = self.root/'restored.pptx'; download.write_bytes(fetched)
            edited = self.root/'edited.pptx'
            subprocess.run([python, '-E', '-s', '-B', '-c',
                "from pptx import Presentation; import sys; p=Presentation(sys.argv[1]); "
                "assert p.slides[0].shapes.title.text=='Synthetic editable title'; "
                "p.slides[0].shapes.title.text='Edited after restore'; p.save(sys.argv[2]); "
                "assert Presentation(sys.argv[2]).slides[0].shapes.title.text=='Edited after restore'",
                str(download), str(edited)], check=True, capture_output=True)
            self.assertNotEqual(edited.read_bytes(), data)
            self.assertEqual(restored.read_material_file(self.item['id'], material['id'], 1)['data'], data)
        finally: restored.close()

    def test_replay_human_correction_and_human_material_version_protected(self):
        original = copy.deepcopy(self.item)
        first = self.command(fields(), item=original)
        replay = self.command(fields(), item=original)
        self.assertEqual(replay['status'], 'already_applied'); self.assertEqual(first['item'], replay['item'])
        material = self.service.materials(self.item['id'])[0]
        changed = self.service.execute('felix', {'operation_id': 'human-correction', 'action': 'edit',
            'item_id': self.item['id'], 'expected_version': first['item']['version'], 'fields': {'title': 'Human corrected topic'}})
        self.assertEqual(changed['status'], 'applied')
        read = self.service.read_material_file(self.item['id'], material['id'], 1)
        self.assertFalse(read['valid']); self.assertEqual(read['data'], pptx())
        human = self.command({**fields(pptx('Human content')), 'material_id': material['id']}, 'human-material', actor='felix')
        self.assertEqual(human['status'], 'applied')
        attempted = self.command({**fields(), 'material_id': material['id']}, 'overwrite-human')
        self.assertEqual(attempted['status'], 'rejected')
        self.assertEqual(self.service.get_item(self.item['id']), human['item'])
        self.assertEqual([m['version'] for m in self.service.materials(self.item['id'])], [1, 2])

    def test_reject_mixed_fields_base64_format_size_and_paths_without_materials(self):
        for i, bad in enumerate([
            {'content': 'fake PPTX', 'mime_type': PPTX_MIME}, {**fields(), 'content': 'ambiguous'}, {**fields(), 'content_base64': 'not base64'},
            {**fields(), 'content_base64': fields()['content_base64']+'='},
            {**fields(), 'filename': '../escape.pptx'}, {**fields(), 'filename': 'bad\\file.pptx'},
            {**fields(), 'filename': 'bad\nname.pptx'}, {**fields(), 'filename': 'file.zip'},
            {**fields(), 'mime_type': 'application/zip'}, fields(b'not a zip'),
            fields(b'x' * (MAX_FILE + 1)), {**fields(), 'content_base64': 1},
        ]):
            result = self.command(bad, 'bad-'+str(i))
            self.assertEqual(result['status'], 'rejected', (i, result))
            self.assertEqual(self.service.materials(self.item['id']), [])
        archive = io.BytesIO()
        with zipfile.ZipFile(archive, 'w') as stream: stream.writestr('ordinary.txt', 'not PPTX')
        self.assertEqual(self.command(fields(archive.getvalue()), 'zip')['status'], 'rejected')

    def test_original_corruption_hardlink_symlink_and_size_fail_closed(self):
        result = self.command(fields())
        material = self.service.materials(self.item['id'])[0]
        path = self.service.data_dir / material['original']['path']
        original = path.read_bytes()
        path.write_bytes(original[:-1]+b'!')
        with self.assertRaises(ValueError): self.service.read_material_file(self.item['id'], material['id'], 1)
        path.write_bytes(original)
        link = self.root/'hard'; os.link(path, link)
        with self.assertRaises(ValueError): self.service.read_material_file(self.item['id'], material['id'], 1)
        link.unlink(); path.unlink(); path.symlink_to(self.root/'missing')
        with self.assertRaises(ValueError): self.service.read_material_file(self.item['id'], material['id'], 1)


class MaterialFileHTTPTests(unittest.IsolatedAsyncioTestCase):
    asyncSetUp = mcp_fixture.MCPTests.asyncSetUp
    asyncTearDown = mcp_fixture.MCPTests.asyncTearDown

    async def upload(self, value=None):
        return await self.client.call('gtd_command', {'job_id': self.job, 'command': {'operation_id': 'upload',
            'action': 'put_material', 'item_id': self.item['id'], 'expected_version': self.item['version'],
            'fields': fields() if value is None else value}})

    async def test_mcp_binary_and_http_identified_bytes_authorization_before_read(self):
        result = await self.upload()
        self.assertEqual(result['status'], 'applied', result)
        material = self.service.materials(self.item['id'])[0]
        path = '/v1/material-files/'+self.item['id']+'/'+material['id']+'/1'
        async with aiohttp.ClientSession() as session:
            with patch.object(self.service, 'read_material_file', side_effect=AssertionError('read before auth')):
                async with session.get(self.url+path) as response: self.assertEqual(response.status, 401)
            async with session.get(self.url+path, headers={'Authorization':'Bearer '+mcp_fixture.PRINCIPAL}) as response:
                self.assertEqual(response.status, 200)
                self.assertEqual(await response.read(), pptx())
                self.assertEqual(response.headers['X-Content-SHA256'], material['original']['sha256'])
                self.assertEqual(response.headers['Content-Type'], PPTX_MIME)
                self.assertTrue(response.headers['Content-Disposition'].startswith('attachment;'))
            async with session.get(self.url+path+'?path=/etc/passwd', headers={'Authorization':'Bearer '+mcp_fixture.OWNER}) as response:
                self.assertEqual(response.status, 400)
        self.assertTrue(self.control.validate(self.job, 'prepare_private')['allowed'])
        schema = FIELD_SCHEMAS['put_material']
        self.assertEqual(len(schema['oneOf']), 3)
        self.assertEqual(set(schema['properties']['source_material']['required']), {'item_id', 'material_id', 'version', 'sha256'})
        self.assertIn('content_base64', schema['properties'])
        pattern = schema['oneOf'][1]['properties']['filename']['pattern']
        self.assertIsNotNone(re.fullmatch(pattern, 'reunión.pptx'))
        for bad in ('../a.pptx', 'a\\b.pptx', 'a.txt'):
            self.assertIsNone(re.fullmatch(pattern, bad))

    async def test_file_larger_than_old_http_limit_roundtrips_without_text_conversion(self):
        stream = io.BytesIO(pptx())
        with zipfile.ZipFile(stream, 'a', zipfile.ZIP_STORED) as package:
            package.writestr('ppt/media/synthetic.bin', b'\x00' * (2 * 1024 * 1024))
        data = stream.getvalue()
        result = await self.upload(fields(data))
        self.assertEqual(result['status'], 'applied', result)
        material = self.service.materials(self.item['id'])[0]
        self.assertEqual(self.service.read_material_file(self.item['id'], material['id'], 1)['data'], data)

    async def test_cli_upload_download_restart_identity_and_no_overwrite(self):
        source = self.root / 'deck.pptx'; source.write_bytes(pptx()); source.chmod(0o600)
        async def cli(*args):
            env = {**os.environ, 'PYTHONPATH': str(RUNTIME), 'GTD_API_TOKEN': mcp_fixture.PRINCIPAL, 'GTD_JOB_ID': self.job}
            process = await asyncio.create_subprocess_exec(sys.executable, '-B', '-m', 'gtd_felix', '--url', self.url,
                *args, env=env, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
            out, err = await process.communicate()
            return process.returncode, json.loads(out or err)
        code, receipt = await cli('upload', self.item['id'], '--file', str(source), '--operation-id', 'cli-upload',
            '--expected-version', str(self.item['version']))
        self.assertEqual(code, 0); self.assertEqual(receipt['status'], 'applied', receipt)
        material = self.service.materials(self.item['id'])[0]; destination = self.root/'download.pptx'
        args = ('download', self.item['id'], material['id'], '1', '--output', str(destination))
        code, receipt = await cli(*args)
        self.assertEqual(code, 0, receipt); self.assertEqual(destination.read_bytes(), source.read_bytes())
        self.assertEqual(destination.stat().st_mode & 0o777, 0o600)
        self.assertEqual((await cli(*args))[0], 1)
        self.assertEqual(destination.read_bytes(), source.read_bytes())
        original_read = self.service.read_material_file
        def bad_sha(*values):
            return {**original_read(*values), 'sha256': '0'*64}
        bad_destination = self.root/'bad-sha.pptx'
        with patch.object(self.service, 'read_material_file', side_effect=bad_sha):
            code, receipt = await cli('download', self.item['id'], material['id'], '1', '--output', str(bad_destination))
            self.assertEqual(code, 1)
        self.assertFalse(bad_destination.exists())

    async def test_executor_file_scope_and_stop_checked_before_original(self):
        mcp_fixture.MCPTests.finish_native(self, self.job, 'cancelled')
        target = self.service.capture('felix', 'worker-source', 'Worker private deck')['item']
        target = self.service.execute('felix', {'operation_id': 'worker-classify', 'action': 'clarify',
            'item_id': target['id'], 'expected_version': target['version'],
            'fields': {'kind': 'project', 'commitment': 'committed'}})['item']
        grant = self.service.execute('felix', {'operation_id': 'worker-grant', 'action': 'grant_mandate',
            'item_id': target['id'], 'expected_version': target['version'], 'fields': {'scope_item_id': target['id'],
                'capabilities': ['prepare_private'], 'actors': ['history-worker'], 'completion_criteria': 'Prepare a deck'}})
        self.assertEqual(grant['status'], 'applied', grant)
        target = grant['item']
        self.control.register_bot('felix', 'worker-bot', {**self.bot, 'id': 'worker', 'actor': 'history-worker',
            'item_id': target['id'], 'mandate_id': grant['mandate']['id']})
        reservation = self.control.reserve('felix', 'worker-reserve', {**self.request, 'item_id': target['id'],
            'expected_version': target['version'], 'bot_id': 'worker', 'mandate_id': grant['mandate']['id']})
        self.assertEqual(reservation['status'], 'reserved', reservation)
        job = reservation['job_id']
        await self.runner.cleanup()
        config = {'data_dir': str(self.root/'data'), 'actors': {'owner':'felix', 'principal':'gtd-felix', 'executors':['history-worker']},
            'api_tokens': {'synthetic-worker-token':'history-worker', mcp_fixture.OWNER:'felix'}}
        self.runner = web.AppRunner(create_app(self.service, self.control, config), access_log=None)
        await self.runner.setup(); site = web.TCPSite(self.runner, '127.0.0.1', 0); await site.start()
        self.url = 'http://127.0.0.1:'+str(site._server.sockets[0].getsockname()[1])
        headers = {'Authorization':'Bearer synthetic-worker-token', 'X-GTD-Job-ID':job}
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url+'/v1/commands', headers=headers, json={'operation_id':'worker-upload',
                'action':'put_material','item_id':target['id'],'expected_version':target['version'],
                'fields': {**fields(), 'mandate_id':grant['mandate']['id']}}) as response:
                result = await response.json()
            self.assertEqual(result['status'], 'applied', result)
            material = self.service.materials(target['id'])[0]
            path = '/v1/material-files/'+target['id']+'/'+material['id']+'/1'
            async with session.get(self.url+path, headers=headers) as response:
                self.assertEqual(response.status, 200); self.assertEqual(await response.read(), pptx())
            # Token of the executor plus a different principal job is insufficient.
            with patch.object(self.service, 'read_material_file', side_effect=AssertionError('outside scope read')):
                async with session.get(self.url+path, headers={**headers,'X-GTD-Job-ID':self.job}) as response:
                    self.assertEqual(response.status, 404)
            self.control.request_stop('felix', 'worker-stop', job)
            with patch.object(self.service, 'read_material_file', side_effect=AssertionError('stopped job read')):
                async with session.get(self.url+path, headers=headers) as response: self.assertEqual(response.status, 404)
