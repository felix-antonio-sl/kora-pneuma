#!/usr/bin/env python3
"""Trabajo por bloques, cotejo explícito y entrega idempotente de texto UTF-8.

El helper mantiene una instantánea de las fuentes y separa el juicio semántico
del revisor de las comprobaciones mecánicas que puede ejecutar. No llama
modelos, no ejecuta las instrucciones de una fuente ni publica conocimiento.
"""

import argparse
from contextlib import contextmanager
import copy
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile


PROTOCOL = 'integral-3'


class Conflict(Exception):
    """Error de estado, contrato o concurrencia que no muta el trabajo."""


def require(condition, message):
    if not condition:
        raise Conflict(message)


def digest(value):
    """SHA-256 de bytes o de texto UTF-8."""
    if not isinstance(value, bytes):
        value = value.encode('utf-8')
    return hashlib.sha256(value).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))


def norm(value):
    return re.sub(r'\s+', ' ', value).strip()


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def read_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, 'Clave JSON repetida: ' + key)
            result[key] = value
        return result

    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique)


def write_if_changed(path, data):
    require(not path.is_symlink(), 'Destino enlazado; conserva el trabajo: ' + path.name)
    raw = data.encode('utf-8')
    if path.exists() and path.read_bytes() == raw:
        return False
    fd, name = tempfile.mkstemp(prefix='.integral-', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
        parent = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(parent)
        finally:
            os.close(parent)
    finally:
        if os.path.exists(name):
            os.unlink(name)
    return True


@contextmanager
def locked(work, create=False):
    require(not work.is_symlink(), 'La carpeta de trabajo no puede ser un enlace.')
    if create:
        work.mkdir(mode=0o700, parents=True, exist_ok=True)
    require(work.is_dir(), 'Carpeta inexistente; ejecuta init.')
    fd = os.open(work / '.lock', os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW, 0o600)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        yield
    except BlockingIOError:
        raise Conflict('Otra operación usa esta carpeta; vuelve a intentar.')
    finally:
        os.close(fd)


def engine_hash():
    return digest(Path(__file__).read_bytes())


def source_text(state, block):
    source = state['sources'][block['source']]
    return ''.join(source['text'].splitlines(keepends=True)[block['start'] - 1:block['end']])


def split_source(text, limit):
    """Partición contigua por párrafos, sin cortar cercos Markdown."""
    lines = text.splitlines(keepends=True)
    paragraphs, start, fence = [], 0, None
    for index, line in enumerate(lines):
        mark = re.match(r'^\s*(`{3,}|~{3,})', line)
        if mark:
            token = mark[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
        if not line.strip() and fence is None:
            paragraphs.append((start, index + 1))
            start = index + 1
    if start < len(lines):
        paragraphs.append((start, len(lines)))
    chunks, begin, end, size = [], 0, 0, 0
    for first, last in paragraphs:
        length = sum(len(line) for line in lines[first:last])
        if size and size + length > limit:
            chunks.append((begin + 1, end))
            begin, size = first, 0
        end, size = last, size + length
    if end > begin:
        chunks.append((begin + 1, end))
    return chunks


def initialize(args, work):
    require(args.source, 'init requiere al menos un --source.')
    require(args.max_chars > 0, '--max-chars debe ser positivo.')
    sources = []
    for filename in args.source:
        path = Path(filename).expanduser().resolve(strict=True)
        require(path.is_file(), 'La fuente debe ser un archivo.')
        raw = path.read_bytes()
        text = raw.decode('utf-8')
        require(bool(text.strip()), 'Fuente vacía; no se certifica un corpus vacío.')
        sources.append({'origin': str(path), 'sha256': digest(raw), 'text': text})
    origins = [source['origin'] for source in sources]
    require(len(origins) == len(set(origins)), 'Fuente repetida en --source.')
    context = Path(args.context_file).read_bytes().decode('utf-8') if args.context_file else ''
    config = {
        'protocol': PROTOCOL,
        'engine_sha256': engine_hash(),
        'sources': [{key: source[key] for key in ('origin', 'sha256')} for source in sources],
        'context': context,
        'encoding': args.encoding,
        'max_chars': args.max_chars,
    }
    path = work / 'state.json'
    if path.exists():
        state = load(work)
        require(state['config'] == config,
                'SOURCE_OR_CONFIG_CHANGED: usa otra carpeta; se preservó el estado.')
        return {'reused': True, **status(state, work)}
    require(not any(p.name not in ('.lock',) and not p.name.startswith('.integral-')
                    for p in work.iterdir()),
            'Carpeta con trabajo ajeno; elige una vacía.')
    blocks = []
    for index, source in enumerate(sources):
        for first, last in split_source(source['text'], args.max_chars):
            blocks.append({
                'id': f'b{len(blocks) + 1:04d}',
                'source': index,
                'start': first,
                'end': last,
                'seen': [],
                'history': [],
                'reopen_requests': [],
            })
    state = {'config': config, 'sources': sources, 'blocks': blocks,
             'global': None, 'outputs': {}}
    save(work, state)
    return {'reused': False, **status(state, work)}


def _block_ids(state):
    return {block['id'] for block in state['blocks']}


def _block_position(state, block_id):
    for position, block in enumerate(state['blocks']):
        if block['id'] == block_id:
            return position
    return None


def find_block(state, block_id):
    matches = [block for block in state['blocks'] if block['id'] == block_id]
    require(len(matches) == 1, 'Bloque desconocido: ' + str(block_id))
    return matches[0]


def _quote_pattern(quote):
    # split() deliberately allows any whitespace variation while retaining
    # punctuation, accents and the exact order of the words.
    return r'\s+'.join(re.escape(part) for part in quote.split())


def contains_quote(text, quote):
    return nonempty(quote) and re.search(_quote_pattern(quote), text) is not None


def _fenced_spans(text):
    """Return character spans occupied by closed Markdown fenced blocks."""
    spans, fence, start = [], None, None
    position = 0
    for line in text.splitlines(keepends=True):
        mark = re.match(r'^\s*(`{3,}|~{3,})', line)
        if mark and fence is None:
            fence = mark[1]
            start = position
        elif mark and fence is not None and mark[1][0] == fence[0] and len(mark[1]) >= len(fence):
            spans.append((start, position + len(line)))
            fence, start = None, None
        position += len(line)
    return spans


def _without_fenced(text):
    spans = _fenced_spans(text)
    if not spans:
        return text
    result, position = [], 0
    for start, end in spans:
        result.append(text[position:start])
        result.append('\n' * text[start:end].count('\n'))
        position = end
    result.append(text[position:])
    return ''.join(result)


def code_blocks(text):
    result, current, fence = [], [], None
    for line in text.splitlines(keepends=True):
        mark = re.match(r'^\s*(`{3,}|~{3,})', line)
        if fence is None:
            if mark:
                fence = mark[1]
                current = [line]
        else:
            current.append(line)
            if mark and mark[1][0] == fence[0] and len(mark[1]) >= len(fence):
                result.append(''.join(current).rstrip('\r\n'))
                current, fence = [], None
    if current:
        result.append(''.join(current))
    return result


NUMBER_PATTERN = r'(?<!\w)[+-]?\d+(?:[.,:/-]\d+)*'


def _protected_requirements(source):
    plain = _without_fenced(source)
    return {
        'inline': set(re.findall(r'`([^`\n]+)`', plain)),
        'links': set(re.findall(r'\]\(([^)]+)\)', plain)),
        'numbers': set(re.findall(NUMBER_PATTERN, plain)),
    }


def candidate_digest(candidate_or_text, references=None):
    """Digest público de texto local y referencias declaradas.

    Acepta una candidata completa o ``text, references`` para facilitar el uso
    desde pruebas y revisores. Los hashes de las referencias vinculan el texto
    indirecto a la versión aceptada vigente; el orden de la lista forma parte
    del digest porque también forma parte del contexto ensamblado.
    """
    if isinstance(candidate_or_text, dict):
        text = candidate_or_text.get('text')
        references = candidate_or_text.get('references', [])
    else:
        text = candidate_or_text
    require(isinstance(text, str), 'candidate_digest requiere texto de candidata.')
    require(isinstance(references, list), 'candidate_digest requiere lista de referencias.')
    refs = []
    for reference in references:
        require(isinstance(reference, dict) and isinstance(reference.get('block'), str)
                and isinstance(reference.get('sha256'), str),
                'Referencia inválida para candidate_digest.')
        refs.append({'block': reference['block'], 'sha256': reference['sha256']})
    return digest(canonical({'text': text, 'references': refs}))


def _validate_reference_entries(state, block, references):
    require(isinstance(references, list), 'references debe ser una lista.')
    position = _block_position(state, block['id'])
    require(position is not None, 'Bloque no pertenece al estado.')
    found = {}
    for reference in references:
        require(isinstance(reference, dict), 'Cada referencia debe ser un objeto.')
        require(set(reference) <= {'block', 'sha256'},
                'Cada referencia solo admite block y sha256.')
        ref_id, ref_hash = reference.get('block'), reference.get('sha256')
        require(isinstance(ref_id, str) and re.fullmatch(r'b\d{4}', ref_id)
                and isinstance(ref_hash, str) and re.fullmatch(r'[0-9a-f]{64}', ref_hash),
                'Cada referencia requiere block y sha256 vigente.')
        require(ref_id not in found, 'Referencia repetida: ' + ref_id)
        target_position = _block_position(state, ref_id)
        require(target_position is not None, 'Referencia desconocida: ' + ref_id)
        target = state['blocks'][target_position]
        require(target_position < position, 'REFERENCE_FUTURE: ' + ref_id)
        require(target['source'] == block['source'], 'REFERENCE_CROSS_SOURCE: ' + ref_id)
        require('accepted' in target, 'Referencia no aceptada: ' + ref_id)
        expected = target['accepted'].get('sha256')
        require(ref_hash == expected,
                'REFERENCE_STALE: la referencia no coincide con el hash aceptado de ' + ref_id)
        require(digest(target['accepted'].get('text', '')) == expected,
                'REFERENCE_STALE: hash aceptado inválido en ' + ref_id)
        found[ref_id] = target
    return found


def _reference_context(state, block, candidate):
    """Return direct and transitive accepted context in source order."""
    if not candidate:
        return []
    direct = _validate_reference_entries(state, block, candidate.get('references', []))
    targets = dict(direct)
    pending = list(direct.items())
    while pending:
        reference_id, target = pending.pop(0)
        target_candidate = target.get('candidate')
        if not isinstance(target_candidate, dict):
            continue
        nested = _validate_reference_entries(state, target, target_candidate.get('references', []))
        for nested_id, nested_target in nested.items():
            if nested_id not in targets:
                targets[nested_id] = nested_target
                pending.append((nested_id, nested_target))
    ordered = sorted(targets, key=lambda item: _block_position(state, item))
    return [
        {'block': reference_id,
         'text': targets[reference_id]['accepted']['text'],
         'sha256': targets[reference_id]['accepted']['sha256']}
        for reference_id in ordered
    ]


def load(work):
    path = work / 'state.json'
    require(not path.is_symlink(), 'state.json no puede ser un enlace.')
    state = read_json(path)
    require(state['config']['protocol'] == PROTOCOL
            and state['config']['engine_sha256'] == engine_hash(),
            'ENGINE_CHANGED: usa otra carpeta con el procedimiento nuevo.')
    require(isinstance(state.get('sources'), list)
            and len(state['sources']) == len(state['config']['sources']),
            'SOURCE_SNAPSHOT_CHANGED: estructura de fuentes inválida.')
    for source, expected in zip(state['sources'], state['config']['sources'], strict=True):
        require(digest(source['text']) == source['sha256'] == expected['sha256']
                and source['origin'] == expected['origin'],
                'SOURCE_SNAPSHOT_CHANGED: conserva y revisa el estado.')
        origin = Path(source['origin'])
        if origin.exists():
            require(digest(origin.read_bytes()) == source['sha256'],
                    'SOURCE_CHANGED: usa otra carpeta; no se reutiliza evidencia obsoleta.')
    expected_blocks = [
        (index, first, last)
        for index, source in enumerate(state['sources'])
        for first, last in split_source(source['text'], state['config']['max_chars'])
    ]
    require([(block['source'], block['start'], block['end']) for block in state['blocks']]
            == expected_blocks
            and [block['id'] for block in state['blocks']]
            == [f'b{index + 1:04d}' for index in range(len(expected_blocks))],
            'BLOCK_PLAN_CHANGED')
    for block in state['blocks']:
        require(isinstance(block.get('seen'), list) and isinstance(block.get('history'), list),
                'Estado de historial inválido: ' + block['id'])
        for field in ('inventory', 'candidate', 'review'):
            if field in block:
                require(digest(canonical(block[field])) == block[field + '_hash'],
                        'EVIDENCE_CHANGED: ' + block['id'] + '/' + field)
        if 'candidate' in block:
            _validate_reference_entries(state, block, block['candidate'].get('references', []))
        if 'accepted' in block:
            accepted = block['accepted']
            require(accepted.get('kind') in ('reviewed', 'retained'),
                    'Accepted inválido: ' + block['id'])
            require(digest(accepted['text']) == accepted['sha256'],
                    'ACCEPTED_TEXT_CHANGED: ' + block['id'])
            expected_text = (source_text(state, block) if accepted['kind'] == 'retained'
                             else block.get('candidate', {}).get('text'))
            require(accepted['text'] == expected_text,
                    'ACCEPTED_BINDING_CHANGED: ' + block['id'])
            if accepted['kind'] == 'reviewed':
                require('candidate' in block and 'review' in block,
                        'ACCEPTED_REVIEW_MISSING: ' + block['id'])
    if state.get('global'):
        require(digest(canonical(state['global'])) == state['global_hash'],
                'GLOBAL_REVIEW_CHANGED')
        if state['global'].get('accepted') and all('accepted' in block for block in state['blocks']):
            require(state['global'].get('assembly_sha256') == digest(assembly(state)),
                    'GLOBAL_ASSEMBLY_CHANGED: revisa el conjunto exacto.')
    return state


def save(work, state):
    write_if_changed(work / 'state.json', json.dumps(state, ensure_ascii=False, indent=2) + '\n')


def stage(block):
    if 'accepted' in block:
        return 'accepted'
    if 'inventory' not in block:
        return 'inventory'
    if 'candidate' not in block:
        return 'candidate'
    return 'review'


def join_sources(state, texts):
    prefix = state['config']['context']
    # Identity and source locations belong to the receipt. Authors provide any
    # title or attribution that the content actually needs for interpretation.
    texts = [text for text in texts if text.strip()]
    return ((prefix.rstrip('\n') + '\n\n') if prefix else '') + '\n\n---\n\n'.join(texts) + '\n'


def _accepted_texts(state):
    texts = []
    for source_index, source in enumerate(state['sources']):
        blocks = [block for block in state['blocks'] if block['source'] == source_index]
        require(blocks and all('accepted' in block for block in blocks), 'Hay bloques pendientes.')
        if all(block['accepted']['kind'] == 'retained' for block in blocks):
            text = source['text']
        else:
            # An empty candidate is a deliberate reference to an earlier block;
            # its context already occurs before it in the same source.
            pieces = [block['accepted']['text'].rstrip('\r\n')
                      for block in blocks if block['accepted']['text'].strip()]
            text = '\n\n'.join(pieces)
        texts.append(text.rstrip('\r\n'))
    return texts


def assembly(state):
    require(all('accepted' in block for block in state['blocks']), 'Hay bloques pendientes.')
    # Recheck current references at the point of assembly even when load() was
    # not called by a direct Python consumer.
    for block in state['blocks']:
        if 'candidate' in block:
            _validate_reference_entries(state, block, block['candidate'].get('references', []))
    return join_sources(state, _accepted_texts(state))


def status(state, work):
    counts = {key: sum(stage(block) == key for block in state['blocks'])
              for key in ('inventory', 'candidate', 'review', 'accepted')}
    changed = [name for name, expected in state['outputs'].items()
               if (work / name).is_symlink()
               or ((work / name).exists() and digest((work / name).read_bytes()) != expected)]
    global_ok = bool(state.get('global') and state['global'].get('accepted'))
    return {
        'protocol': PROTOCOL,
        'blocks': len(state['blocks']),
        'counts': counts,
        'global_review_accepted': global_ok,
        'edited_outputs': changed,
        'missing_outputs': [name for name in state['outputs'] if not (work / name).exists()],
        'origin_missing': [source['origin'] for source in state['sources']
                           if not Path(source['origin']).exists()],
    }


def index(state):
    result = []
    for block in state['blocks']:
        lines = state['sources'][block['source']]['text'].splitlines()
        heading = next((line for line in reversed(lines[:block['start']])
                        if line.startswith('#')), None)
        result.append({
            'id': block['id'],
            'source': block['source'],
            'lines': [block['start'], block['end']],
            'heading': heading,
            'stage': stage(block),
        })
    return result


def _schema(state, block, step):
    if step == 'inventory':
        return {
            'stage': 'inventory',
            'units': [{'id': 'u01', 'lines': [block['start'], block['end']],
                       'statement': 'Afirmación con condiciones, excepciones y relaciones.'}],
            'exclusions': [],
            'questions': [{'id': 'q01', 'question': 'Pregunta fijada desde la fuente.',
                          'expected': 'Respuesta esperada cotejada con la fuente.'}],
            'dependencies': [],
            'source_rechecked': True,
            'source_review': 'Qué cotejaste al volver del inventario a la fuente.',
        }
    if step == 'candidate':
        return {
            'stage': 'candidate',
            'text': 'Contenido del bloque; vacío si no hay unidades o todas remiten.',
            'mapping': [{'unit': 'u01', 'quote': 'Fragmento local o del bloque referenciado.'}],
            'references': [],
            'transformations': ['Descripción concreta de la transformación.'],
            'literal_changes': [],
            'issues': [],
        }
    return {
        'stage': 'review',
        'candidate_sha256': candidate_digest(block.get('candidate', {'text': '', 'references': []})),
        'unit_checks': [{'id': unit['id'], 'preserved': True,
                         'reason': 'Fundamento del cotejo de la afirmación y sus condiciones.'}
                        for unit in block.get('inventory', {}).get('units', [])],
        'exclusion_checks': [
            {'id': row['id'], 'justified': True,
             'reason': 'Por qué lo excluido sólo describe soporte o procedencia y no altera contenido.'}
            for row in block.get('inventory', {}).get('exclusions', [])],
        'source_rechecked': True,
        'backward_complete': True,
        'relations_preserved': True,
        'relations_review': 'Condiciones, referentes y relaciones comprobadas.',
        'questions': [{'id': question['id'], 'answer': 'Respuesta observada en la candidata.',
                       'satisfied': True}
                      for question in block.get('inventory', {}).get('questions', [])],
        'literal_changes': [],
        'isolation': 'same_context',
        'issues': [],
    }


def packet_global(state):
    require(all('accepted' in block for block in state['blocks']), 'Hay bloques pendientes.')
    text = assembly(state)
    return {
        'stage': 'done' if (state.get('global') or {}).get('accepted') else 'global',
        'text': text,
        'assembly_sha256': digest(text),
        'index': index(state),
        'dependencies': {block['id']: block.get('inventory', {}).get('dependencies', [])
                         for block in state['blocks']},
        'instruction': ('Revisa el conjunto y sus fuentes con show. Envía stage=global, '
                        'assembly_sha256, source_rechecked=true, block_checks (id, preserved, '
                        'reason), relations_review, issues=[], limits y negative_control '
                        '(observado o NOT_RUN).'),
    }


def packet(state, block=None):
    if block == 'global':
        return packet_global(state)
    if isinstance(block, str):
        block = find_block(state, block)
    if block is None:
        block = next((item for item in state['blocks'] if stage(item) != 'accepted'), None)
    if block is None:
        return packet_global(state)
    step = stage(block)
    candidate = block.get('candidate')
    references = _reference_context(state, block, candidate) if candidate else []
    return {
        'block': block['id'],
        'stage': step,
        'lines': [block['start'], block['end']],
        'source': source_text(state, block),
        'content_source': content_source(state, block),
        'oversize': len(source_text(state, block)) > state['config']['max_chars'],
        'interpretation_context': state['config']['context'],
        'headings': [line for line in state['sources'][block['source']]['text'].splitlines()
                     [:block['start']] if line.startswith('#')][-8:],
        'index': index(state),
        'inventory': block.get('inventory'),
        'candidate': candidate,
        'accepted': block.get('accepted'),
        'referenced_context': references,
        'attempts': len(block.get('history', [])),
        'schema': _schema(state, block, step),
    }


def rows_by_id(rows, ids, field='id'):
    require(isinstance(rows, list), 'Se esperaba una lista de cotejos.')
    require(all(isinstance(row, dict) and row.get(field) in ids for row in rows),
            'Identidad ausente o desconocida.')
    require(len(rows) == len(ids) and {row[field] for row in rows} == set(ids),
            'Debe haber exactamente un cotejo por elemento.')


def _validate_span(span, offset, line_count, message='lines debe ser [inicio,fin].'):
    require(isinstance(span, list) and len(span) == 2
            and all(type(number) is int for number in span), message)
    first, last = span
    require(offset <= first <= last < offset + line_count, 'Rango fuera del texto: ' + str(span))
    return first, last


def inventory_coverage(rows, text, offset):
    """Mechanical line-range coverage; it says nothing about semantics."""
    lines = text.splitlines(keepends=True)
    covered = set()
    for row in rows:
        first, last = _validate_span(row.get('lines'), offset, len(lines))
        covered.update(range(first, last + 1))
    absent = [offset + index for index, line in enumerate(lines)
              if line.strip() and offset + index not in covered]
    require(not absent, 'Texto sin cobertura mecánica en líneas: ' + str(absent[:30]))


def content_source(state, block, inventory=None):
    """Remove explicitly located support text, retaining source line numbers.

    The declared reason is a semantic judgment for the reviewer. Exact spans
    stop an exclusion from silently exempting other occurrences of a literal.
    """
    text = source_text(state, block)
    exclusions = (inventory if inventory is not None else block.get('inventory', {})).get(
        'exclusions', [])
    require(isinstance(exclusions, list), 'exclusions debe ser una lista.')
    lines = text.splitlines(keepends=True)
    ids, spans = set(), []
    for row in exclusions:
        require(isinstance(row, dict) and isinstance(row.get('id'), str)
                and re.fullmatch(r'x\d+', row['id']) and row['id'] not in ids,
                'Usa ids únicos x01, x02… para exclusions.')
        ids.add(row['id'])
        require(nonempty(row.get('quote')) and nonempty(row.get('reason')),
                'Cada exclusión requiere quote exacta y reason.')
        first, last = _validate_span(row.get('lines'), block['start'], len(lines))
        selected = ''.join(lines[first - block['start']:last - block['start'] + 1])
        require(selected.count(row['quote']) == 1,
                'La quote de exclusión debe existir exactamente una vez en su rango: ' + row['id'])
        start = len(''.join(lines[:first - block['start']])) + selected.index(row['quote'])
        end = start + len(row['quote'])
        require(all(end <= left or start >= right for left, right in spans),
                'Exclusiones solapadas: ' + row['id'])
        spans.append((start, end))
    for start, end in sorted(spans, reverse=True):
        # Preserve newlines for coverage; no new words enter the source.
        text = text[:start] + ''.join(c for c in text[start:end] if c in '\r\n') + text[end:]
    return text


def validate_inventory(state, block, data):
    substantive = content_source(state, block, data)
    units = data.get('units')
    require(isinstance(units, list) and (bool(units) or not substantive.strip()),
            'units debe inventariar el contenido no excluido del bloque.')
    ids = [unit.get('id') if isinstance(unit, dict) else None for unit in units]
    require(all(isinstance(identifier, str) and re.fullmatch(r'u\d+', identifier)
                for identifier in ids) and len(ids) == len(set(ids)),
            'Usa ids únicos u01, u02…')
    for unit in units:
        require(isinstance(unit, dict) and isinstance(unit.get('lines'), list)
                and nonempty(unit.get('statement')),
                'Cada unidad requiere lines y statement.')
        require(set(unit) <= {'id', 'lines', 'statement', 'evidence'},
                'question/expected pertenecen a inventory.questions, no a units.')
        if 'evidence' in unit:
            first, last = _validate_span(unit['lines'], block['start'],
                                         len(source_text(state, block).splitlines(keepends=True)))
            block_lines = source_text(state, block).splitlines(keepends=True)
            selected = ''.join(block_lines[first - block['start']:last - block['start'] + 1])
            require(nonempty(unit['evidence']) and contains_quote(selected, unit['evidence']),
                    'Evidencia ausente del rango: ' + str(unit['lines']))
    inventory_coverage(units, substantive, block['start'])
    questions = data.get('questions')
    require(isinstance(questions, list) and (bool(questions) if units else not questions),
            'questions requiere preguntas de contenido; [] si el bloque sólo contiene soporte excluido.')
    question_ids = [question.get('id') if isinstance(question, dict) else None
                    for question in questions]
    require(all(isinstance(identifier, str) and re.fullmatch(r'q\d+', identifier)
                for identifier in question_ids)
            and len(question_ids) == len(set(question_ids)),
            'Usa ids únicos q01, q02… para questions.')
    require(all(isinstance(question, dict) and nonempty(question.get('question'))
                and nonempty(question.get('expected')) for question in questions),
            'Cada question requiere question y expected.')
    dependencies = data.get('dependencies')
    require(isinstance(dependencies, list) and len(dependencies) == len(set(dependencies))
            and all(dependency in _block_ids(state) and dependency != block['id']
                    for dependency in dependencies),
            'dependencies requiere ids de otros bloques conocidos.')
    require(data.get('source_rechecked') is True and nonempty(data.get('source_review')),
            'Vuelve a cotejar fuente e inventario y registra source_review.')


def _candidate_visible_text(state, block, data):
    targets = _validate_reference_entries(state, block, data.get('references', []))
    context = _reference_context(state, block, data)
    parts = [data.get('text', '')]
    parts.extend(package['text'] for package in context)
    return '\n\n'.join(parts), targets


def _validate_literal_changes(source, visible, changes):
    require(isinstance(changes, list), 'literal_changes debe ser una lista.')
    requirements = _protected_requirements(source)
    missing_numbers = requirements['numbers'] - set(re.findall(NUMBER_PATTERN, visible))
    declared = set()
    for change in changes:
        require(isinstance(change, dict) and nonempty(change.get('literal'))
                and nonempty(change.get('quote')) and nonempty(change.get('reason')),
                'Cada literal_change requiere literal, quote y reason.')
        literal = change['literal']
        require(literal in requirements['numbers'],
                'literal_change no corresponde a un número requerido por la fuente: ' + literal)
        require(literal not in declared, 'literal_change repetido: ' + literal)
        require(literal in missing_numbers,
                'literal_change sobrante o ya presente en texto+referencias: ' + literal)
        require(contains_quote(visible, change['quote']),
                'Quote de literal_change ausente en texto+referencias: ' + literal)
        declared.add(literal)
    require(declared == missing_numbers,
            'Faltan justificaciones exactas para literales requeridos: '
            + str(sorted(missing_numbers - declared)))
    for label, values in (('literal de código', requirements['inline']),
                          ('destino de enlace', requirements['links'])):
        pattern = r'`([^`\n]+)`' if label == 'literal de código' else r'\]\(([^)]+)\)'
        actual = set(re.findall(pattern, visible))
        require(values <= actual, 'Falta ' + label + ' requerido; coteja el bloque y sus referencias.')
    return requirements, missing_numbers


def validate_candidate(state, block, data):
    require(isinstance(data.get('text'), str), 'text debe ser texto UTF-8.')
    require(isinstance(data.get('mapping'), list), 'mapping debe ser una lista.')
    require(isinstance(data.get('references'), list), 'references debe ser una lista.')
    require(isinstance(data.get('transformations'), list)
            and all(nonempty(transformation) for transformation in data['transformations']),
            'transformations requiere descripciones concretas.')
    require(isinstance(data.get('issues'), list) and data['issues'] == [],
            'Hay pérdidas o incertidumbres abiertas en candidate; corrige o usa retain.')
    inventory = block['inventory']
    ids = [unit['id'] for unit in inventory['units']]
    rows_by_id(data['mapping'], ids, 'unit')
    visible, targets = _candidate_visible_text(state, block, data)
    referenced_ids = set(targets)
    for row in data['mapping']:
        require(nonempty(row.get('quote')), 'Cada mapping requiere quote.')
        if 'block' in row:
            ref_id = row.get('block')
            require(isinstance(ref_id, str) and ref_id in referenced_ids,
                    'mapping.block requiere referencia declarada: ' + str(ref_id))
            require(contains_quote(targets[ref_id]['accepted']['text'], row['quote']),
                    'El fragmento mapeado no está en el texto aceptado de ' + ref_id + '.')
        else:
            require(contains_quote(data['text'], row['quote']),
                    'El fragmento mapeado no está en el texto local de la candidata.')
    if not data['text'].strip():
        require(all('block' in row for row in data['mapping']),
                'text vacío requiere unidades remitidas a referencias o un bloque sólo de soporte excluido.')
    _validate_literal_changes(content_source(state, block), visible,
                              data.get('literal_changes', []))
    source_codes = code_blocks(source_text(state, block))
    available_codes = code_blocks(visible)
    for code in source_codes:
        require(available_codes.count(code) >= source_codes.count(code),
                'Se alteró un bloque de código; conserva literalmente o usa retain.')


def _review_literal_rows(data):
    if 'literal_changes' in data:
        return data['literal_changes']
    return data.get('literal_checks')


def validate_review(block, data):
    candidate = block['candidate']
    require(data.get('candidate_sha256') == candidate_digest(candidate),
            'CANDIDATE_CHANGED: revisa la candidata exacta y sus referencias.')
    inventory = block['inventory']
    unit_ids = [unit['id'] for unit in inventory['units']]
    question_ids = [question['id'] for question in inventory['questions']]
    exclusion_ids = [row['id'] for row in inventory.get('exclusions', [])]
    rows_by_id(data.get('unit_checks'), unit_ids)
    rows_by_id(data.get('questions'), question_ids)
    exclusion_checks = data.get('exclusion_checks', [])
    rows_by_id(exclusion_checks, exclusion_ids)
    require(all(type(row.get('justified')) is bool and nonempty(row.get('reason'))
                for row in exclusion_checks),
            'Cada exclusión necesita justified y reason; coteja que no quite contenido sustantivo.')
    require(all(nonempty(row.get('reason')) and type(row.get('preserved')) is bool
                for row in data['unit_checks']),
            'Cada unidad necesita preserved y reason.')
    require(all(nonempty(row.get('answer')) and type(row.get('satisfied')) is bool
                for row in data['questions']),
            'Cada pregunta necesita respuesta observada y satisfied.')
    literal_changes = candidate.get('literal_changes', [])
    literal_rows = _review_literal_rows(data)
    if literal_rows is None and not literal_changes:
        literal_rows = []
    require(literal_rows is not None and isinstance(literal_rows, list),
            'El revisor debe cotejar literal_changes explícitamente cuando existen.')
    literal_ids = [change.get('literal') if isinstance(change, dict) else None
                   for change in literal_rows]
    require(set(literal_ids) == {change['literal'] for change in literal_changes}
            and len(literal_ids) == len(set(literal_ids)),
            'El cotejo de literal_changes no corresponde a la candidata.')
    require(all(isinstance(row, dict) and type(row.get('preserved')) is bool
                and nonempty(row.get('reason')) for row in literal_rows),
            'Cada literal_change requiere preserved booleano y razón concreta.')
    require(data.get('isolation') in ('same_context', 'independent_context', 'unknown'),
            'Declara el aislamiento real de la lectura.')
    require(isinstance(data.get('issues'), list) and nonempty(data.get('relations_review')),
            'Registra issues y relations_review.')
    for field in ('source_rechecked', 'backward_complete', 'relations_preserved'):
        require(type(data.get(field)) is bool, 'Falta booleano ' + field)
    return (
        not data['issues']
        and all(data[field] for field in ('source_rechecked', 'backward_complete',
                                          'relations_preserved'))
        and all(row['preserved'] for row in data['unit_checks'])
        and all(row['justified'] for row in exclusion_checks)
        and all(row['satisfied'] for row in data['questions'])
        and all(row['preserved'] for row in literal_rows)
    )


def _current_evidence(block):
    return {
        field: copy.deepcopy(block[field])
        for field in ('candidate', 'candidate_hash', 'review', 'review_hash', 'accepted')
        if field in block
    }


def _clear_evidence(block):
    for field in ('candidate', 'candidate_hash', 'review', 'review_hash', 'accepted'):
        block.pop(field, None)


def _reference_graph(state):
    graph = {block['id']: set() for block in state['blocks']}
    for block in state['blocks']:
        candidate = block.get('candidate')
        if isinstance(candidate, dict) and isinstance(candidate.get('references'), list):
            graph[block['id']] = {reference.get('block') for reference in candidate['references']
                                  if isinstance(reference, dict) and isinstance(reference.get('block'), str)}
    return graph


def _consumer_closure(state, provider_id):
    graph = _reference_graph(state)
    closure, frontier = set(), {provider_id}
    while frontier:
        newly = {block_id for block_id, refs in graph.items()
                 if block_id not in closure and block_id != provider_id and refs & frontier}
        if not newly:
            break
        closure.update(newly)
        frontier = newly
    return [block['id'] for block in state['blocks'] if block['id'] in closure]


def _invalidate_consumers(state, provider_id, reason, already=None):
    invalidated = []
    for consumer_id in _consumer_closure(state, provider_id):
        if already and consumer_id in already:
            continue
        consumer = find_block(state, consumer_id)
        archived = _current_evidence(consumer)
        consumer['history'].append({
            'event': 'invalidation',
            'provider': provider_id,
            'reason': reason,
            'archived': archived,
            'seen': copy.deepcopy(consumer.get('seen', [])),
        })
        _clear_evidence(consumer)
        consumer['seen'] = []
        invalidated.append(consumer_id)
    return invalidated


def submit(state, block_id, data):
    require(isinstance(data, dict), 'El paso debe ser un objeto JSON.')
    incoming = digest(canonical(data))
    if block_id == 'global':
        require(data.get('stage') == 'global', 'stage debe ser global.')
        require(data.get('assembly_sha256') == digest(assembly(state)),
                'ASSEMBLY_CHANGED: revisa el conjunto exacto.')
        ids = [block['id'] for block in state['blocks']]
        rows_by_id(data.get('block_checks'), ids)
        require(all(type(row.get('preserved')) is bool and nonempty(row.get('reason'))
                    for row in data['block_checks']),
                'Cada bloque global necesita preserved y reason.')
        require(type(data.get('source_rechecked')) is bool
                and nonempty(data.get('relations_review'))
                and nonempty(data.get('limits'))
                and isinstance(data.get('issues'), list),
                'Revisión global incompleta.')
        accepted = (data['source_rechecked'] and not data['issues']
                    and all(row['preserved'] for row in data['block_checks']))
        value = {**data, 'accepted': accepted}
        if state.get('global') == value:
            return {'reused': True, 'accepted': accepted}
        if state.get('global'):
            state.setdefault('global_history', []).append(copy.deepcopy(state['global']))
        state['global'] = value
        state['global_hash'] = digest(canonical(value))
        return {'reused': False, 'accepted': accepted}

    block = find_block(state, block_id)
    if incoming in block.get('seen', []):
        return {'reused': True, 'stage': stage(block)}
    expected = stage(block)
    require(expected != 'accepted',
            'Bloque aceptado: usa reopen con el hash aceptado para revisar este bloque.')
    require(data.get('stage') == expected, 'Paso esperado: ' + expected)
    if expected == 'inventory':
        validate_inventory(state, block, data)
    elif expected == 'candidate':
        validate_candidate(state, block, data)
    else:
        passed = validate_review(block, data)
        if not passed:
            archived_candidate = copy.deepcopy(block.pop('candidate'))
            archived_hash = block.pop('candidate_hash', None)
            block.pop('review', None)
            block.pop('review_hash', None)
            block['history'].append({
                'event': 'review_rejected',
                'candidate': archived_candidate,
                'candidate_hash': archived_hash,
                'review': copy.deepcopy(data),
            })
            block.setdefault('seen', []).append(incoming)
            state['global'] = None
            state.pop('global_hash', None)
            return {
                'reused': False,
                'accepted': False,
                'next': 'candidate',
                'hint': 'Repara unidad/relación fallida; conserva literalmente solo pasaje difícil dentro de candidata.',
            }
        candidate = block['candidate']
        block['accepted'] = {
            'kind': 'reviewed',
            'text': candidate['text'],
            'sha256': digest(candidate['text']),
        }
    block[expected] = data
    block[expected + '_hash'] = incoming
    block.setdefault('seen', []).append(incoming)
    state['global'] = None
    state.pop('global_hash', None)
    return {'reused': False, 'stage': stage(block)}


def reopen(state, block, reason, expected_hash):
    require(nonempty(reason), 'Explica por qué reabres el bloque.')
    require(isinstance(expected_hash, str) and re.fullmatch(r'[0-9a-f]{64}', expected_hash),
            'reopen requiere el sha256 aceptado vigente.')
    request = {'block': block['id'], 'reason': reason, 'candidate_sha256': expected_hash}
    request_hash = digest(canonical(request))
    requests = block.setdefault('reopen_requests', [])
    for previous in requests:
        if previous.get('request_hash') == request_hash:
            return {'reused': True, 'stage': stage(block), 'request_hash': request_hash,
                    'invalidated': previous.get('invalidated', [])}
    require('accepted' in block, 'Bloque no aceptado; no hay revisión puntual que reabrir.')
    require(block['accepted']['sha256'] == expected_hash,
            'REOPEN_STALE: hash aceptado diferente al vigente.')
    invalidated = _consumer_closure(state, block['id'])
    archived = _current_evidence(block)
    seen = copy.deepcopy(block.get('seen', []))
    block['history'].append({
        'event': 'reopen',
        'request_hash': request_hash,
        'expected_accepted_sha256': expected_hash,
        'reason': reason,
        'archived': archived,
        'seen': seen,
        'invalidated': invalidated,
    })
    _clear_evidence(block)
    block['seen'] = []
    request_record = {
        'request_hash': request_hash,
        'expected_accepted_sha256': expected_hash,
        'reason': reason,
        'invalidated': invalidated,
    }
    requests.append(request_record)
    invalidated_consumers = _invalidate_consumers(
        state, block['id'], 'Proveedor reabierto: ' + reason)
    # _consumer_closure was captured before clearing the provider. The graph is
    # unchanged for consumers, so this is a consistency assertion, not a new
    # traversal that could lose a recursive dependent.
    require(invalidated_consumers == invalidated,
            'INVALIDATION_GRAPH_CHANGED: vuelve a intentar con el mismo estado.')
    state['global'] = None
    state.pop('global_hash', None)
    return {'reused': False, 'stage': stage(block), 'request_hash': request_hash,
            'invalidated': invalidated}


def retain(state, block, reason):
    require(nonempty(reason), 'Explica por qué conservas el original.')
    require(not block.get('inventory', {}).get('exclusions'),
            'RETAIN_WOULD_RESTORE_EXCLUSIONS: presenta content_source como candidata '
            'y coteja las exclusiones; retain restauraría también el soporte omitido.')
    text = source_text(state, block)
    if block.get('accepted', {}).get('kind') == 'retained':
        require(block['accepted']['text'] == text, 'RETAIN_CHANGED: la fuente aceptada no coincide.')
        return {'reused': True, 'stage': 'accepted', 'invalidated': []}
    old_text = block.get('accepted', {}).get('text') if block.get('accepted') else None
    invalidated = _consumer_closure(state, block['id']) if old_text is not None and old_text != text else []
    archived = _current_evidence(block)
    if archived:
        block['history'].append({'event': 'retain', 'reason': reason, 'archived': archived,
                                 'seen': copy.deepcopy(block.get('seen', []))})
    _clear_evidence(block)
    block['accepted'] = {'kind': 'retained', 'text': text, 'sha256': digest(text), 'reason': reason}
    if invalidated:
        invalidated_consumers = _invalidate_consumers(
            state, block['id'], 'Proveedor retenido con texto actualizado: ' + reason)
        require(invalidated_consumers == invalidated,
                'INVALIDATION_GRAPH_CHANGED: vuelve a intentar con el mismo estado.')
    state['global'] = None
    state.pop('global_hash', None)
    return {'reused': False, 'stage': 'accepted', 'invalidated': invalidated}


def _normalize_for_measurement(text):
    parts = re.split(r'(```[^\n]*\n[\s\S]*?```|~~~[^\n]*\n[\s\S]*?~~~)', text)
    return ''.join(part if part.startswith(('```', '~~~'))
                   else re.sub(r'(?<=\S)\n(?=\S)(?![#>*|\-])', ' ', part)
                   for part in parts)


def measure(state, text):
    source = join_sources(state, [source['text'].rstrip('\r\n') for source in state['sources']])
    content = join_sources(state, [
        ''.join(content_source(state, block) for block in state['blocks']
                if block['source'] == index).strip('\r\n')
        for index in range(len(state['sources']))
    ])
    result = {
        'source_characters': len(source),
        'candidate_characters': len(text),
        'encoding': state['config']['encoding'],
        'tokens_status': 'NOT_MEASURED',
        'compression_status': 'NOT_MEASURED',
        'savings_basis': 'normalized_content_source_tokens_minus_candidate_tokens',
        'transformation_observed': False,
    }
    try:
        import tiktoken
    except ImportError:
        return result
    encoder = tiktoken.get_encoding(state['config']['encoding'])
    normalized = _normalize_for_measurement(source)
    normalized_content = _normalize_for_measurement(content)
    count = lambda value: len(encoder.encode(value, disallowed_special=()))
    raw, normal, compact = count(source), count(normalized), count(text)
    content_count, content_normal = count(content), count(normalized_content)
    transformation_observed = any(
        block.get('accepted', {}).get('kind') == 'reviewed'
        and block.get('candidate', {}).get('text').strip() != content_source(state, block).strip()
        and bool(block.get('candidate', {}).get('transformations'))
        for block in state['blocks']
    )
    status_value = ('GAIN_OBSERVED' if compact < content_normal and transformation_observed else 'NO_GAIN')
    result.update({
        'tokens_status': 'MEASURED',
        'tokenizer_version': getattr(tiktoken, '__version__', 'unknown'),
        'source_tokens': raw,
        'normalized_source_tokens': normal,
        'content_source_tokens': content_count,
        'normalized_content_source_tokens': content_normal,
        'excluded_source_tokens': raw - content_count,
        'candidate_tokens': compact,
        'saving_tokens': raw - compact,
        'saving_percent': round(100 * (1 - compact / raw), 2) if raw else 0.0,
        'saving_vs_normalized_tokens': normal - compact,
        'saving_vs_normalized_percent': round(100 * (1 - compact / normal), 2)
        if normal else 0.0,
        'saving_vs_content_tokens': content_count - compact,
        'saving_vs_content_percent': round(100 * (1 - compact / content_count), 2)
        if content_count else 0.0,
        'saving_vs_normalized_content_tokens': content_normal - compact,
        'saving_vs_normalized_content_percent': round(100 * (1 - compact / content_normal), 2)
        if content_normal else 0.0,
        'transformation_observed': transformation_observed,
        'compression_status': status_value,
        'measurement_claim': ('Retiro de soporte y compresión del contenido medidos por separado '
                              'con este encoding y esta candidata; '
                              'no prueba universal de conservación semántica.'),
    })
    return result


def build(state, work):
    text = assembly(state)
    require(state.get('global') and state['global'].get('accepted')
            and state['global'].get('assembly_sha256') == digest(text),
            'Falta revisión global aceptada de este texto.')
    measurements = measure(state, text)
    require(measurements.get('saving_tokens', 0) >= 0
            and measurements.get('saving_vs_content_tokens', 0) >= 0,
            'TOKEN_REGRESSION: la candidata consume más tokens que el contenido fuente '
            'o que las fuentes completas. '
            'Repara los bloques que aumentan el costo y vuelve a revisar el conjunto; '
            'no se descartan bloques automáticamente.')
    compression_status = measurements.get('compression_status', 'NOT_MEASURED')
    reviewed = [block for block in state['blocks']
                if block['accepted']['kind'] == 'reviewed']
    retained = [block for block in state['blocks']
                if block['accepted']['kind'] == 'retained']
    receipt = {
        'protocol': PROTOCOL,
        'sources': state['config']['sources'],
        'artifact_sha256': digest(text),
        'blocks': [
            {
                'id': block['id'],
                'kind': block['accepted']['kind'],
                'sha256': block['accepted']['sha256'],
                'inventory_hash': block.get('inventory_hash'),
                'candidate_digest': candidate_digest(block['candidate'])
                if block['accepted']['kind'] == 'reviewed' else None,
                'review_hash': block.get('review_hash')
                if block['accepted']['kind'] == 'reviewed' else None,
                'reader_isolation_declared': block.get('review', {}).get('isolation')
                if block['accepted']['kind'] == 'reviewed' else None,
                'references': copy.deepcopy(block.get('candidate', {}).get('references', []))
                if block['accepted']['kind'] == 'reviewed' else [],
                'exclusions': copy.deepcopy(block.get('inventory', {}).get('exclusions', [])),
                'retained_reason': block['accepted'].get('reason')
                if block['accepted']['kind'] == 'retained' else None,
            }
            for block in state['blocks']
        ],
        'global_review_hash': state['global_hash'],
        'conservation_reviewed_blocks': [block['id'] for block in reviewed],
        'conservation_retained_blocks': [block['id'] for block in retained],
        'compression_status': compression_status,
        'measurements': measurements,
        'limits': state['global'].get('limits'),
        'claim': ('Conservación del contenido sustantivo y exclusiones de soporte declaradas '
                  'en revisiones explícitas por bloque; '
                  'retenciones literales se distinguen. El ahorro es una medida observada '
                  'frente a la fuente y a su versión normalizada; no prueba equivalencia '
                  'universal, independencia del revisor ni publicación.'),
    }
    files = {
        'artifact.md': text,
        'receipt.json': json.dumps(receipt, ensure_ascii=False, indent=2) + '\n',
    }
    for name, content in files.items():
        path = work / name
        require(not path.is_symlink(), 'Salida enlazada: ' + name)
        if path.exists():
            actual = digest(path.read_bytes())
            require(actual in (state['outputs'].get(name), digest(content)),
                    'OUTPUT_EDITED: se preservó ' + name)
    changed = []
    for name, content in files.items():
        if write_if_changed(work / name, content):
            changed.append(name)
        state['outputs'][name] = digest(content)
    return {'reused': not changed, 'changed_files': changed,
            'artifact': str(work / 'artifact.md'), 'receipt': receipt}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['init', 'next', 'show', 'submit', 'retain', 'reopen',
                                             'build', 'status'])
    parser.add_argument('--work', required=True)
    parser.add_argument('--source', action='append')
    parser.add_argument('--context-file')
    parser.add_argument('--encoding', default='o200k_base')
    parser.add_argument('--max-chars', type=int, default=4000)
    parser.add_argument('--block')
    parser.add_argument('--file')
    parser.add_argument('--reason')
    parser.add_argument('--candidate-sha256')
    args = parser.parse_args()
    work = Path(args.work).expanduser().absolute()
    try:
        with locked(work, args.command == 'init'):
            if args.command == 'init':
                result = initialize(args, work)
            else:
                state = load(work)
                if args.command == 'status':
                    result = status(state, work)
                elif args.command == 'next':
                    result = packet(state)
                elif args.command == 'show':
                    require(args.block, 'show requiere --block.')
                    result = packet(state, args.block if args.block == 'global'
                                    else find_block(state, args.block))
                elif args.command == 'submit':
                    require(args.file and args.block, 'submit requiere --block y --file.')
                    result = submit(state, args.block, read_json(Path(args.file)))
                    save(work, state)
                elif args.command == 'retain':
                    require(args.block, 'retain requiere --block.')
                    result = retain(state, find_block(state, args.block), args.reason)
                    save(work, state)
                elif args.command == 'reopen':
                    require(args.block and args.candidate_sha256,
                            'reopen requiere --block y --candidate-sha256.')
                    result = reopen(state, find_block(state, args.block), args.reason,
                                    args.candidate_sha256)
                    save(work, state)
                else:
                    result = build(state, work)
                    save(work, state)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (Conflict, OSError, ValueError, KeyError, TypeError) as error:
        print(json.dumps({'error': str(error),
                          'state': 'No se aprobó ni publicó contenido por este error.'},
                         ensure_ascii=False))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
