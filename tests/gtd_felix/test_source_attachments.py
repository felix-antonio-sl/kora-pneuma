"""Selected-original attachment reading: no provider, model, network or extraction files."""
import base64
from email.message import EmailMessage
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile

from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
sys.path.insert(0, str(Path(__file__).parent))
from gtd_felix.source_attachments import spreadsheet, read_attachment
from gtd_felix.service import GTDService


def workbook(rows=None, target='worksheets/sheet1.xml', extra=None):
    rows = rows or '<row r="1"><c r="A1" t="s"><v>0</v></c><c r="B1" t="inlineStr"><is><t>Estado</t></is></c></row><row r="2"><c r="A2" t="inlineStr"><is><t>SYNTHETIC_ONLY</t></is></c><c r="B2"><f>1+1</f><v>2</v></c></row>'
    parts = {
        'xl/workbook.xml':'<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet name="Synthetic" sheetId="1" r:id="rId1"/></sheets></workbook>',
        'xl/_rels/workbook.xml.rels':'<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="'+target+'"/></Relationships>',
        'xl/sharedStrings.xml':'<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><si><r><t>Respons</t></r><r><t>able</t></r></si></sst>',
        'xl/worksheets/sheet1.xml':'<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData>'+rows+'</sheetData></worksheet>'}
    parts.update(extra or {})
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer,'w',zipfile.ZIP_DEFLATED) as z:
        for name,content in parts.items():
            info=zipfile.ZipInfo(name); info.compress_type=zipfile.ZIP_DEFLATED; z.writestr(info,content)
    return buffer.getvalue()


def selected_source(service):
    message = EmailMessage(); message.set_content('Synthetic selected source')
    message.add_attachment(workbook(),maintype='application',subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet',filename='Synthetic.xlsx')
    message.add_attachment(b'SYNTHETIC_PDF',maintype='application',subtype='pdf',filename='Synthetic.pdf')
    raw = json.dumps({'id':'synthetic-mail','raw':base64.urlsafe_b64encode(message.as_bytes()).decode()}).encode()
    digest = hashlib.sha256(raw).hexdigest()
    result = service.capture('felix','selected-attachment','Synthetic selected source',
        source={'provider':'gmail','availability':'present','external_id':'synthetic-mail','sha256':digest},
        original=raw,filename='source.bin',mime_type='application/json')
    return result['item']


class SpreadsheetTests(unittest.TestCase):
    def test_shared_inline_cached_formula_and_pagination(self):
        data = workbook(); first = spreadsheet(data,row_limit=1)
        self.assertEqual(['Responsable','Estado'],[c['value'] for c in first['rows'][0]['cells']])
        self.assertEqual(1,first['next_row_offset']); self.assertFalse(first['complete'])
        last = spreadsheet(data,row_offset=1,row_limit=1)
        self.assertEqual('2',last['rows'][0]['cells'][1]['value'])
        self.assertTrue(last['rows'][0]['cells'][1]['formula_not_evaluated'])
        self.assertIsNone(last['next_row_offset'])
        self.assertTrue(spreadsheet(data)['complete'])

    def test_external_or_traversing_relationship_never_followed(self):
        for target in ('../escape.xml','../../etc/passwd','https://example.invalid/data'):
            with self.assertRaises(ValueError): spreadsheet(workbook(target=target))

    def test_entity_declarations_rejected(self):
        for xml in ('<!DOCTYPE x [<!ENTITY secret "SYNTHETIC_SECRET">]><x>&secret;</x>',
                    '<?xml version="1.0" encoding="utf-16"?><x/>'.encode('utf-16')):
            with self.assertRaisesRegex(ValueError,'attachment_xml_unsupported'):
                spreadsheet(workbook(extra={'xl/workbook.xml':xml}))

    def test_archive_expansion_bound(self):
        with self.assertRaisesRegex(ValueError,'attachment_archive_limit'):
            spreadsheet(workbook(extra={'padding':b'x'*(4*1024*1024+1)}))

    def test_partial_cells_do_not_claim_complete(self):
        value = spreadsheet(workbook(rows='<row r="1"><c r="A1" t="inlineStr"><is><t>'+('x'*2100)+'</t></is></c></row>'))
        self.assertTrue(value['truncated']); self.assertFalse(value['complete'])
        self.assertEqual(2000,len(value['rows'][0]['cells'][0]['value']))

    def test_wide_page_preserves_continuation_under_cell_budget(self):
        rows=''.join('<row r="'+str(r)+'">'+''.join('<c r="'+chr(65+c)+str(r)+'"><v>1</v></c>' for c in range(25))+'</row>' for r in range(1,21))
        page=spreadsheet(workbook(rows=rows),row_limit=20)
        self.assertEqual(8,len(page['rows']))
        self.assertEqual(8,page['next_row_offset'])
        self.assertFalse(page['truncated'])
        self.assertEqual(9,spreadsheet(workbook(rows=rows),row_offset=8,row_limit=1)['rows'][0]['row'])

    def test_unbounded_cell_metadata_rejected(self):
        with self.assertRaisesRegex(ValueError,'attachment_cell_invalid'):
            spreadsheet(workbook(rows='<row r="1"><c r="A1" t="'+('x'*10000)+'"><v>1</v></c></row>'))
        with self.assertRaisesRegex(ValueError,'attachment_row_invalid'):
            spreadsheet(workbook(rows='<row r="'+('1'*10000)+'"><c r="A1"><v>1</v></c></row>'))

    def test_invalid_string_index_and_sheet(self):
        with self.assertRaisesRegex(ValueError,'attachment_string_invalid'):
            spreadsheet(workbook(rows='<row r="1"><c r="A1" t="s"><v>999</v></c></row>'))
        with self.assertRaisesRegex(ValueError,'attachment_sheet_not_found'): spreadsheet(workbook(),sheet_index=1)


class SourceAttachmentTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(); self.service=GTDService(Path(self.temp.name)/'data')
        self.item=selected_source(self.service)
    def tearDown(self):
        self.service.close(); self.temp.cleanup()
    def test_manifest_exact_hash_and_no_new_files(self):
        before=set(Path(self.temp.name).rglob('*'))
        result=read_attachment(self.service.store,self.item,self.item['version'])
        self.assertEqual([True,False],[a['supported'] for a in result['attachments']])
        self.assertNotIn('SYNTHETIC_ONLY',json.dumps(result))
        result=read_attachment(self.service.store,self.item,self.item['version'],attachment_index=0)
        self.assertEqual(self.item['original']['sha256'],result['original_sha256'])
        self.assertEqual(hashlib.sha256(workbook()).hexdigest(),result['attachment_sha256'])
        self.assertEqual(before,set(Path(self.temp.name).rglob('*')))
    def test_version_selection_hash_and_unsupported_guards(self):
        for changed,version,kwargs,code in [
            (self.item,999,{},'source_version_changed'),
            ({**self.item,'source':{**self.item['source'],'availability':'uncertain'}},1,{},'selected_gmail_source_required'),
            ({**self.item,'source':{**self.item['source'],'sha256':'0'*64}},1,{},'source_original_mismatch'),
            (self.item,1,{'attachment_index':1},'attachment_format_unsupported'),
            (self.item,1,{'attachment_index':4},'attachment_not_found'),
            (self.item,1,{'row_limit':21},'invalid_attachment_arguments')]:
            with self.assertRaisesRegex(ValueError,code): read_attachment(self.service.store,changed,version,**kwargs)
    def test_tampered_original_rejected(self):
        path=self.service.store.root/self.item['original']['path']; path.write_bytes(b'x'*self.item['original']['size'])
        with self.assertRaisesRegex(ValueError,'material_integrity_invalid'):
            read_attachment(self.service.store,self.item,self.item['version'])


    def test_full_manifest_honest_without_bytes(self):
        import test_google_sources as fixtures
        full = fixtures.full_message('full-mail')
        raw = json.dumps(full).encode()
        digest = hashlib.sha256(raw).hexdigest()
        item = self.service.capture('felix', 'full-attachment', 'Synthetic full source',
            source={'provider': 'gmail', 'availability': 'present', 'external_id': 'full-mail',
                    'sha256': digest},
            original=raw, filename='source.bin', mime_type='application/json')['item']
        result = read_attachment(self.service.store, item, item['version'])
        self.assertEqual('full', result['representation'])
        self.assertEqual('not_retained', result['content'])
        self.assertEqual(1, len(result['attachments']))
        self.assertEqual('big.bin', result['attachments'][0]['filename'])
        self.assertFalse(result['attachments'][0]['body_present'])
        self.assertEqual(digest, result['original_sha256'])
        with self.assertRaisesRegex(ValueError, 'attachment_content_not_retained'):
            read_attachment(self.service.store, item, item['version'], attachment_index=0)

    def test_full_id_mismatch_rejected_before_manifest(self):
        import test_google_sources as fixtures
        full = fixtures.full_message('actual-id')
        raw = json.dumps(full).encode()
        digest = hashlib.sha256(raw).hexdigest()
        item = self.service.capture('felix', 'full-mismatch', 'Synthetic',
            source={'provider': 'gmail', 'availability': 'present', 'external_id': 'different-id',
                    'sha256': digest},
            original=raw, filename='source.bin', mime_type='application/json')['item']
        with self.assertRaisesRegex(ValueError, 'source_original_mismatch'):
            read_attachment(self.service.store, item, item['version'])

    def test_full_index_existence_before_content_refusal(self):
        import test_google_sources as fixtures
        full = fixtures.full_message('full-mail')
        raw = json.dumps(full).encode()
        digest = hashlib.sha256(raw).hexdigest()
        item = self.service.capture('felix', 'full-index', 'Synthetic',
            source={'provider': 'gmail', 'availability': 'present', 'external_id': 'full-mail',
                    'sha256': digest},
            original=raw, filename='source.bin', mime_type='application/json')['item']
        result = read_attachment(self.service.store, item, item['version'])
        self.assertIn('attachment_id', result['attachments'][0])
        self.assertIn('part_id', result['attachments'][0])
        with self.assertRaisesRegex(ValueError, 'attachment_not_found'):
            read_attachment(self.service.store, item, item['version'], attachment_index=5)
        with self.assertRaisesRegex(ValueError, 'attachment_content_not_retained'):
            read_attachment(self.service.store, item, item['version'], attachment_index=0)

    def test_full_aggregate_content_matches_row_bytes(self):
        # E25.2: the aggregate `content` claim must not contradict its rows.
        # Referenced-only -> not_retained; single inline 'YWJj' -> inline
        # present (never not_retained); mixed referenced+inline -> mixed.
        # Indices and raw compatibility are preserved.
        import base64
        import test_google_sources as fixtures
        # Referenced-only (existing shape): aggregate not_retained.
        full_ref = fixtures.full_message('agg-ref')
        raw_ref = json.dumps(full_ref).encode()
        digest_ref = hashlib.sha256(raw_ref).hexdigest()
        item_ref = self.service.capture('felix', 'agg-ref', 'Synthetic',
            source={'provider': 'gmail', 'availability': 'present', 'external_id': 'agg-ref',
                    'sha256': digest_ref},
            original=raw_ref, filename='source.bin', mime_type='application/json')['item']
        manifest_ref = read_attachment(self.service.store, item_ref, item_ref['version'])
        self.assertEqual('not_retained', manifest_ref['content'])
        self.assertFalse(manifest_ref['attachments'][0]['body_present'])
        # Single inline 'YWJj' (sonda 25): row present, aggregate consistent.
        full_inline = fixtures.full_message('agg-inline', attachments=())
        full_inline['payload']['parts'] = [
            {'mimeType': 'text/plain', 'filename': '', 'headers': [],
             'body': {'size': 2, 'data': base64.urlsafe_b64encode(b'hi').decode().rstrip('=')}},
            {'mimeType': 'application/octet-stream', 'filename': 'tiny.bin', 'headers': [],
             'partId': '3', 'body': {'size': 3, 'data': 'YWJj'}}]
        raw_inline = json.dumps(full_inline).encode()
        digest_inline = hashlib.sha256(raw_inline).hexdigest()
        item_inline = self.service.capture('felix', 'agg-inline', 'Synthetic',
            source={'provider': 'gmail', 'availability': 'present', 'external_id': 'agg-inline',
                    'sha256': digest_inline},
            original=raw_inline, filename='source.bin', mime_type='application/json')['item']
        manifest_inline = read_attachment(self.service.store, item_inline, item_inline['version'])
        self.assertTrue(manifest_inline['attachments'][0]['body_present'])
        self.assertNotEqual('not_retained', manifest_inline['content'])
        self.assertEqual('inline_present', manifest_inline['content'])
        self.assertIsNone(manifest_inline['attachments'][0]['attachment_id'])
        self.assertEqual('3', manifest_inline['attachments'][0]['part_id'])
        # Mixed referenced + inline: aggregate mixed, per-index behaviour keeps.
        wb = workbook()
        b64 = base64.urlsafe_b64encode(wb).decode().rstrip('=')
        full_mixed = fixtures.full_message('agg-mixed', attachments=())
        full_mixed['payload']['parts'] = [
            {'mimeType': 'text/plain', 'filename': '', 'headers': [],
             'body': {'size': 2, 'data': base64.urlsafe_b64encode(b'hi').decode().rstrip('=')}},
            {'mimeType': 'application/octet-stream', 'filename': 'ref.bin', 'headers': [],
             'body': {'size': 999, 'attachmentId': 'ATT_ref'}},
            {'mimeType': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
             'filename': 'inline.xlsx', 'headers': [], 'partId': '5',
             'body': {'size': len(wb), 'data': b64}}]
        raw_mixed = json.dumps(full_mixed).encode()
        digest_mixed = hashlib.sha256(raw_mixed).hexdigest()
        item_mixed = self.service.capture('felix', 'agg-mixed', 'Synthetic',
            source={'provider': 'gmail', 'availability': 'present', 'external_id': 'agg-mixed',
                    'sha256': digest_mixed},
            original=raw_mixed, filename='source.bin', mime_type='application/json')['item']
        manifest_mixed = read_attachment(self.service.store, item_mixed, item_mixed['version'])
        self.assertEqual('mixed', manifest_mixed['content'])
        by_name = {a['filename']: a for a in manifest_mixed['attachments']}
        self.assertFalse(by_name['ref.bin']['body_present'])
        self.assertTrue(by_name['inline.xlsx']['body_present'])
        with self.assertRaisesRegex(ValueError, 'attachment_content_not_retained'):
            read_attachment(self.service.store, item_mixed, item_mixed['version'], attachment_index=0)
        served = read_attachment(self.service.store, item_mixed, item_mixed['version'], attachment_index=1)
        self.assertIn('table', served)
        with self.assertRaisesRegex(ValueError, 'attachment_not_found'):
            read_attachment(self.service.store, item_mixed, item_mixed['version'], attachment_index=7)

    def test_full_inline_bytes_distinguished_from_referenced(self):
        import base64
        import test_google_sources as fixtures
        # Supported inline XLSX with bytes present is served, not refused.
        wb = workbook()
        b64 = base64.urlsafe_b64encode(wb).decode().rstrip('=')
        full = fixtures.full_message('inline-mail', attachments=())
        full['payload']['parts'] = [
            {'mimeType': 'text/plain', 'filename': '', 'headers': [],
             'body': {'size': 2, 'data': base64.urlsafe_b64encode(b'hi').decode().rstrip('=')}},
            {'mimeType': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
             'filename': 'inline.xlsx', 'headers': [], 'partId': '1',
             'body': {'size': len(wb), 'data': b64}}]
        raw = json.dumps(full).encode()
        digest = hashlib.sha256(raw).hexdigest()
        item = self.service.capture('felix', 'full-inline', 'Synthetic',
            source={'provider': 'gmail', 'availability': 'present', 'external_id': 'inline-mail',
                    'sha256': digest},
            original=raw, filename='source.bin', mime_type='application/json')['item']
        manifest = read_attachment(self.service.store, item, item['version'])
        self.assertTrue(manifest['attachments'][0]['body_present'])
        content = read_attachment(self.service.store, item, item['version'], attachment_index=0)
        self.assertIn('table', content)
        self.assertEqual('full', content.get('representation'))
        # Inline bytes present but unsupported format report format_unsupported.
        full2 = fixtures.full_message('inline2', attachments=())
        full2['payload']['parts'] = [
            {'mimeType': 'text/plain', 'filename': '', 'headers': [],
             'body': {'size': 2, 'data': base64.urlsafe_b64encode(b'hi').decode().rstrip('=')}},
            {'mimeType': 'application/pdf', 'filename': 'doc.pdf', 'headers': [], 'partId': '2',
             'body': {'size': 3, 'data': base64.urlsafe_b64encode(b'abc').decode().rstrip('=')}}]
        raw2 = json.dumps(full2).encode()
        digest2 = hashlib.sha256(raw2).hexdigest()
        item2 = self.service.capture('felix', 'full-inline2', 'Synthetic',
            source={'provider': 'gmail', 'availability': 'present', 'external_id': 'inline2',
                    'sha256': digest2},
            original=raw2, filename='source.bin', mime_type='application/json')['item']
        with self.assertRaisesRegex(ValueError, 'attachment_format_unsupported'):
            read_attachment(self.service.store, item2, item2['version'], attachment_index=0)


if __name__=='__main__': unittest.main()
