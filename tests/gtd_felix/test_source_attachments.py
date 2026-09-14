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


if __name__=='__main__': unittest.main()
