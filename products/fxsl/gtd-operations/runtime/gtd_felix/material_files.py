"""Bounded PPTX intake and verified originals; never extracts or opens slides.

Package identity/CRC checks are not a PowerPoint rendering or editing test.
"""
import base64
import binascii
import hashlib
import io
import os
from pathlib import PurePosixPath
import stat
import xml.etree.ElementTree as ET
import zipfile
import zlib

PPTX_MIME = 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
MAX_FILE = 4 * 1024 * 1024
MAX_BASE64 = 4 * ((MAX_FILE + 2) // 3)


def decode_pptx(fields):
    filename, encoded = fields.get('filename'), fields.get('content_base64')
    if (not isinstance(filename, str) or not filename or len(filename.encode('utf-8')) > 255
            or '/' in filename or '\\' in filename or any(ord(c) < 32 or ord(c) == 127 for c in filename)
            or not filename.lower().endswith('.pptx') or filename in {'.pptx', '..pptx'}):
        raise ValueError('invalid_material_filename')
    if fields.get('mime_type') != PPTX_MIME:
        raise ValueError('invalid_material_mime')
    if not isinstance(encoded, str) or not encoded or len(encoded) > MAX_BASE64:
        raise ValueError('material_file_size_invalid')
    try:
        data = base64.b64decode(encoded, validate=True)
    except (ValueError, binascii.Error) as exc:
        raise ValueError('invalid_material_base64') from exc
    if not data or len(data) > MAX_FILE:
        raise ValueError('material_file_size_invalid')
    if base64.b64encode(data).decode('ascii') != encoded:
        raise ValueError('invalid_material_base64')
    validate_pptx(data)
    return data, filename, PPTX_MIME


def validate_pptx(data):
    try:
        if not data.startswith(b'PK\x03\x04'):
            raise ValueError('invalid_pptx')
        with zipfile.ZipFile(io.BytesIO(data)) as package:
            entries = package.infolist()
            names = [entry.filename for entry in entries]
            if (len(entries) > 2048 or len(names) != len(set(names))
                    or sum(entry.file_size for entry in entries) > 32 * 1024 * 1024):
                raise ValueError('pptx_package_limit')
            for entry in entries:
                path = PurePosixPath(entry.filename)
                if (path.is_absolute() or '..' in path.parts or '\\' in entry.filename or '\x00' in entry.filename
                        or entry.flag_bits & 1 or stat.S_ISLNK(entry.external_attr >> 16)
                        or entry.compress_type not in {zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED}):
                    raise ValueError('invalid_pptx_entry')
            required = {'[Content_Types].xml', '_rels/.rels', 'ppt/presentation.xml'}
            if not required.issubset(names):
                raise ValueError('invalid_pptx')
            for name in required:
                if package.getinfo(name).file_size > 1024 * 1024:
                    raise ValueError('pptx_package_limit')
            # Check actual uncompressed bytes/CRC without extracting any paths.
            for entry in entries:
                with package.open(entry) as stream:
                    consumed = 0
                    while block := stream.read(65536):
                        consumed += len(block)
                        if consumed > entry.file_size:
                            raise ValueError('pptx_package_limit')
            content = package.read('[Content_Types].xml')
            presentation = package.read('ppt/presentation.xml')
            relationships = package.read('_rels/.rels')
            if any(b'<!DOCTYPE' in xml.replace(b'\x00', b'').upper() or b'<!ENTITY' in xml.replace(b'\x00', b'').upper() for xml in (content, presentation, relationships)):
                raise ValueError('invalid_pptx_xml')
            types = ET.fromstring(content)
            if not any(e.get('PartName') == '/ppt/presentation.xml' and
                    e.get('ContentType') == PPTX_MIME + '.main+xml' for e in types):
                raise ValueError('invalid_pptx_content_type')
            p = ET.fromstring(presentation)
            if p.tag not in {'{http://schemas.openxmlformats.org/presentationml/2006/main}presentation',
                             '{http://purl.oclc.org/ooxml/presentationml/main}presentation'}:
                raise ValueError('invalid_pptx_presentation')
            rels = ET.fromstring(relationships)
            if not any(e.get('Target', '').lstrip('/') == 'ppt/presentation.xml'
                    and e.get('Type', '').endswith('/officeDocument') and e.get('TargetMode', 'Internal') == 'Internal' for e in rels):
                raise ValueError('invalid_pptx_relationship')
    except (zipfile.BadZipFile, RuntimeError, NotImplementedError, ET.ParseError, EOFError, OSError, zlib.error) as exc:
        raise ValueError('invalid_pptx') from exc


def read_original(store, original, limit):
    digest = original.get('sha256', '')
    if (not isinstance(digest, str) or len(digest) != 64 or any(c not in '0123456789abcdef' for c in digest)
            or original.get('path') != 'originals/' + digest or type(original.get('size')) is not int
            or not 0 <= original['size'] <= limit
            or any(path.is_symlink() for path in (store.originals, *store.originals.parents))):
        raise ValueError('material_integrity_invalid')
    try:
        fd = os.open(store.originals / digest, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
        with os.fdopen(fd, 'rb') as stream:
            info = os.fstat(stream.fileno())
            if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1 or info.st_size != original['size']:
                raise ValueError('material_integrity_invalid')
            data = stream.read(limit + 1)
        if len(data) != original['size'] or hashlib.sha256(data).hexdigest() != digest:
            raise ValueError('material_integrity_invalid')
        return data
    except OSError as exc:
        raise ValueError('material_unreadable') from exc
