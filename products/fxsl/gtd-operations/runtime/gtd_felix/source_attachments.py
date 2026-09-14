"""Bounded, read-only XLSX views of already retained selected Gmail originals."""
import base64
import binascii
from email import policy
from email.parser import BytesParser
import hashlib
import io
import json
import posixpath
import re
from xml.etree import ElementTree as ET
import zipfile

from .material_files import read_original

MAX_BYTES = 4 * 1024 * 1024
NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
RID = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'


def _require(condition, code):
    if not condition:
        raise ValueError(code)


def _xml(data):
    _require(b'\x00' not in data and b'<!DOCTYPE' not in data.upper()
             and b'<!ENTITY' not in data.upper(), 'attachment_xml_unsupported')
    return ET.fromstring(data)


def spreadsheet(data, sheet_index=0, row_offset=0, row_limit=2):
    """Return raw cell values; never evaluate formulas, dates, macros or links."""
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        entries = archive.infolist()
        names = [entry.filename for entry in entries]
        _require(len(entries) <= 256 and len(set(names)) == len(names)
            and sum(e.file_size for e in entries) <= 16 * 1024 * 1024
            and all(e.file_size <= MAX_BYTES and not e.flag_bits & 1
                    and e.compress_type in {zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED}
                    and not e.filename.startswith('/') and '\\' not in e.filename
                    and '..' not in e.filename.split('/') for e in entries), 'attachment_archive_limit')
        workbook = _xml(archive.read('xl/workbook.xml'))
        rels = _xml(archive.read('xl/_rels/workbook.xml.rels'))
        relations = {node.get('Id'): node for node in rels}
        sheets = workbook.findall('s:sheets/s:sheet', NS)
        _require(len(sheets) <= 64 and all(0 < len(s.get('name', '')) <= 128 for s in sheets), 'attachment_sheet_invalid')
        _require(0 <= sheet_index < len(sheets), 'attachment_sheet_not_found')
        relation = relations.get(sheets[sheet_index].get(RID))
        _require(relation is not None and relation.get('TargetMode', 'Internal') == 'Internal'
                 and relation.get('Type', '').endswith('/worksheet'), 'attachment_sheet_unsupported')
        target = relation.get('Target', '')
        path = posixpath.normpath(target.lstrip('/') if target.startswith('/') else 'xl/' + target)
        _require(path.startswith('xl/worksheets/') and '..' not in target.split('/'), 'attachment_sheet_unsupported')
        strings = []
        if 'xl/sharedStrings.xml' in names:
            shared = _xml(archive.read('xl/sharedStrings.xml'))
            strings = [''.join(t.text or '' for t in node.iter('{' + NS['s'] + '}t'))
                       for node in shared.findall('s:si', NS)]
        root = _xml(archive.read(path))
        rows = root.findall('s:sheetData/s:row', NS)
        _require(row_offset <= len(rows), 'attachment_row_not_found')
        rendered, truncated, remaining, cell_budget = [], False, 40000, 200
        for row in rows[row_offset:row_offset + row_limit]:
            cells = []
            row_number = row.get('r', '')
            _require(row_number.isdecimal() and len(row_number) <= 7 and 1 <= int(row_number) <= 1048576, 'attachment_row_invalid')
            raw_cells = row.findall('s:c', NS)
            if rendered and min(len(raw_cells), 100) > cell_budget:
                break
            row_truncated = len(raw_cells) > 100
            for cell in raw_cells[:100]:
                coordinate = cell.get('r', '')
                _require(re.fullmatch(r'[A-Z]{1,3}[1-9][0-9]{0,6}', coordinate), 'attachment_cell_invalid')
                kind = cell.get('t', 'n')
                _require(kind in {'s','n','inlineStr','str','b','e','d'}, 'attachment_cell_invalid')
                node = cell.find('s:v', NS)
                value = node.text or '' if node is not None else ''
                if kind == 's':
                    _require(value.isdecimal() and int(value) < len(strings), 'attachment_string_invalid')
                    value = strings[int(value)]
                elif kind == 'inlineStr':
                    value = ''.join(t.text or '' for t in cell.findall('s:is//s:t', NS))
                limit = min(2000, remaining)
                clipped = len(value) > limit
                cells.append({'cell': coordinate, 'type': kind, 'value': value[:limit],
                    'formula_not_evaluated': cell.find('s:f', NS) is not None, 'truncated': clipped})
                remaining -= len(value[:limit])
                cell_budget -= 1
                row_truncated |= clipped
            rendered.append({'row': int(row_number), 'cells': cells, 'truncated': row_truncated})
            truncated |= row_truncated
        end = row_offset + len(rendered)
        return {'format': 'xlsx', 'sheets': [{'index': i, 'name': s.get('name')} for i,s in enumerate(sheets)],
            'sheet_index': sheet_index, 'row_offset': row_offset, 'total_rows': len(rows),
            'rows': rendered, 'next_row_offset': end if end < len(rows) else None,
            'truncated': truncated, 'complete': end == len(rows) and not truncated,
            'interpretation': 'raw_cached_values_no_formula_execution_or_date_conversion'}


def _full_manifest(item, version, original, value, attachment_index=None, sheet_index=0, row_offset=0, row_limit=2):
    """Honest manifest for a structured (format=full) retained original.

    Attachment bytes behind attachmentId are referenced, not retained, so
    content requests for referenced-only entries get a concrete refusal.
    Entries with inline bytes present are distinguished: supported XLSX
    reuses the bounded reader, unsupported formats report format_unsupported.
    Index existence is checked before any content refusal.
    """
    walked = []

    def walk(part, depth):
        _require(isinstance(part, dict) and depth <= 8 and len(walked) <= 64, 'attachment_mime_invalid')
        subs = part.get('parts')
        _require(subs is None or isinstance(subs, list), 'attachment_mime_invalid')
        if subs:
            for sub in subs:
                walk(sub, depth + 1)
            return
        filename = part.get('filename') or ''
        if not filename:
            return
        body = part.get('body') or {}
        _require(isinstance(body, dict), 'attachment_mime_invalid')
        att_id = body.get('attachmentId')
        part_id = part.get('partId')
        walked.append({'filename': filename, 'content_type': part.get('mimeType', ''),
            'size': body.get('size') if isinstance(body.get('size'), int) else None,
            'body_present': bool(body.get('data')),
            'attachment_id': att_id if isinstance(att_id, str) else None,
            'part_id': part_id if isinstance(part_id, str) else None,
            'data': body.get('data') if isinstance(body.get('data'), str) else None})

    payload = value.get('payload')
    _require(isinstance(payload, dict), 'attachment_mime_invalid')
    walk(payload, 0)
    manifest = [{'index': i, 'filename': (w['filename'] or '')[:200],
        'filename_truncated': len(w['filename'] or '') > 200,
        'mime_type': (w['content_type'] or '')[:200],
        'supported': (w['filename'] or '').lower().endswith('.xlsx'),
        'body_present': w['body_present'], 'size': w['size'],
        'attachment_id': w['attachment_id'], 'part_id': w['part_id']} for i, w in enumerate(walked)]
    if attachment_index is None:
        return {'item_id': item['id'], 'source_version': version, 'original_sha256': original['sha256'],
            'attachments': manifest, 'content_is_untrusted': True,
            'representation': 'full', 'content': 'not_retained'}
    _require(type(attachment_index) is int and attachment_index >= 0, 'invalid_attachment_arguments')
    _require(attachment_index < len(walked), 'attachment_not_found')
    entry = walked[attachment_index]
    if not entry['body_present']:
        raise ValueError('attachment_content_not_retained')
    _require(entry['filename'].lower().endswith('.xlsx'), 'attachment_format_unsupported')
    payload_bytes = base64.b64decode(entry['data'] + '=' * (-len(entry['data']) % 4), altchars=b'-_', validate=True)
    _require(isinstance(payload_bytes, bytes) and len(payload_bytes) <= MAX_BYTES, 'attachment_size_limit')
    result = {'item_id': item['id'], 'source_version': version, 'original_sha256': original['sha256'],
        'attachments': manifest, 'content_is_untrusted': True, 'representation': 'full',
        'attachment_index': attachment_index, 'attachment_sha256': hashlib.sha256(payload_bytes).hexdigest(),
        'table': spreadsheet(payload_bytes, sheet_index, row_offset, row_limit)}
    # sheet/window args are validated by the caller frame; reuse them here
    return result


def read_attachment(store, item, version, attachment_index=None, sheet_index=0, row_offset=0, row_limit=2):
    _require(type(version) is int and version >= 1 and item.get('version') == version, 'source_version_changed')
    source = item.get('source', {})
    _require(source.get('provider') == 'gmail' and source.get('availability') == 'present' and item.get('status') != 'withdrawn', 'selected_gmail_source_required')
    _require(all(type(v) is int and v >= 0 for v in (sheet_index, row_offset))
             and type(row_limit) is int and 1 <= row_limit <= 20
             and (attachment_index is None or type(attachment_index) is int and attachment_index >= 0), 'invalid_attachment_arguments')
    original = item.get('original', {})
    data = read_original(store, original, MAX_BYTES)
    _require(source.get('sha256') == original.get('sha256'), 'source_original_mismatch')
    try:
        value = json.loads(data)
        _require(value.get('id') == source.get('external_id'), 'source_original_mismatch')
        if 'raw' not in value and isinstance(value.get('payload'), dict):
            return _full_manifest(item, version, original, value, attachment_index, sheet_index, row_offset, row_limit)
        raw = value['raw']
        message = BytesParser(policy=policy.default).parsebytes(base64.b64decode(raw + '=' * (-len(raw) % 4), altchars=b'-_', validate=True))
        parts = [part for part in message.walk() if not part.is_multipart()
                 and (part.get_filename() or part.get_content_disposition() == 'attachment')]
        _require(not message.defects and len(parts) <= 64 and all(not p.defects for p in parts), 'attachment_mime_invalid')
        manifest = [{'index': i, 'filename': (p.get_filename() or '')[:200], 'filename_truncated': len(p.get_filename() or '') > 200, 'mime_type': p.get_content_type()[:200],
            'supported': (p.get_filename() or '').lower().endswith('.xlsx')} for i,p in enumerate(parts)]
        result = {'item_id': item['id'], 'source_version': version, 'original_sha256': original['sha256'],
                  'attachments': manifest, 'content_is_untrusted': True}
        if attachment_index is None:
            return result
        _require(attachment_index < len(parts), 'attachment_not_found')
        _require(manifest[attachment_index]['supported'], 'attachment_format_unsupported')
        part = parts[attachment_index]
        payload = part.get_payload(decode=True)
        _require(not part.defects, 'attachment_mime_invalid')
        _require(isinstance(payload, bytes) and len(payload) <= MAX_BYTES, 'attachment_size_limit')
        result.update(attachment_index=attachment_index, attachment_sha256=hashlib.sha256(payload).hexdigest(),
                      table=spreadsheet(payload, sheet_index, row_offset, row_limit))
        return result
    except (KeyError, TypeError, binascii.Error, zipfile.BadZipFile, ET.ParseError, RuntimeError, NotImplementedError, OSError):
        raise ValueError('attachment_parse_failed') from None
