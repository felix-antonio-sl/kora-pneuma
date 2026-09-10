"""Deterministic, optional token measurements for source and candidate inputs.

This module deliberately measures byte-backed text files only.  It does not
parse, transform, or judge their meaning.  ``tiktoken`` remains an optional
operator dependency so the rest of KORA can run when no counter is installed.
"""

from pathlib import Path


def _paths(value, *, required=False):
    if value is None:
        values = []
    elif isinstance(value, (str, Path)):
        values = [value]
    else:
        try:
            values = list(value)
        except TypeError as error:
            raise TypeError("Las rutas deben ser Path o una secuencia de Path") from error
    if required and not values:
        raise ValueError("Se requiere al menos una fuente")
    paths = []
    for value in values:
        if not isinstance(value, (str, Path)):
            raise TypeError("Cada entrada debe ser una ruta")
        paths.append(Path(value))
    return paths


def _read(paths):
    """Read all paths without decoding lossy binary data."""
    values = []
    first_error = None
    for path in paths:
        try:
            data = path.read_bytes()
        except OSError as error:
            entry = {
                "path": str(path),
                "bytes": None,
                "characters": None,
                "reason": "input_unavailable",
                "detail": str(error),
            }
            values.append(entry)
            first_error = first_error or entry
            continue
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError as error:
            entry = {
                "path": str(path),
                "bytes": len(data),
                "characters": None,
                "reason": "input_not_utf8",
                "detail": str(error),
            }
            values.append(entry)
            first_error = first_error or entry
            continue
        values.append({"path": str(path), "bytes": len(data), "characters": len(text), "text": text})
    return values, first_error


def _group(values, tokens=None):
    byte_values = [value.get("bytes") for value in values]
    character_values = [value.get("characters") for value in values]
    result = {
        "paths": [value["path"] for value in values],
        "bytes": (sum(byte_values) if all(isinstance(value, int) for value in byte_values)
                  else None),
        "characters": (sum(character_values)
                        if all(isinstance(value, int) for value in character_values)
                        else None),
    }
    if tokens is not None:
        result["tokens"] = tokens
    return result


def _encode(encoder, text):
    try:
        return len(encoder.encode(text, disallowed_special=()))
    except TypeError:
        # Small test doubles and older compatible encoders may only accept the
        # text argument.  The measured encoder is still identified in output.
        return len(encoder.encode(text))


def _not_measured(encoding, source_values, candidate_values, auxiliary_values,
                  wrapper_values, reason, *, detail=None):
    groups = {
        "source": _group(source_values),
        "candidate": _group(candidate_values),
        "auxiliaries": _group(auxiliary_values),
        "wrapper": _group(wrapper_values),
    }
    for group in groups.values():
        group["tokens"] = None
    result = {
        "status": "NOT_MEASURED",
        "reason": reason,
        "encoding": encoding,
        "tokenizer": None,
        "tokenizer_version": None,
        "source": groups["source"],
        "candidate": groups["candidate"],
        "auxiliaries": groups["auxiliaries"],
        "wrapper": groups["wrapper"],
        "total": {"source": None, "candidate": None},
        "limits": ["No se acreditan fidelidad, cobertura ni equivalencia semántica."],
    }
    if detail is not None:
        result["detail"] = detail
    return result


def measure(source, candidate, auxiliaries=(), wrapper=None,
            encoding="cl100k_base") -> dict:
    """Measure complete source and candidate context costs.

    ``source`` and ``candidate`` are paths (or path sequences).  Auxiliary
    paths and the optional wrapper are counted as part of the complete
    candidate cost, while each component remains visible in the result.  A
    missing counter or a non-UTF-8 input yields ``NOT_MEASURED`` rather than a
    fabricated token count.
    """
    if not isinstance(encoding, str) or not encoding.strip():
        raise ValueError("encoding debe identificar una codificación")
    source_paths = _paths(source, required=True)
    candidate_paths = _paths(candidate, required=True)
    auxiliary_paths = _paths(auxiliaries)
    wrapper_paths = _paths(wrapper)

    source_values, source_error = _read(source_paths)
    candidate_values, candidate_error = _read(candidate_paths)
    auxiliary_values, auxiliary_error = _read(auxiliary_paths)
    wrapper_values, wrapper_error = _read(wrapper_paths)
    invalid = next((error for error in (source_error, candidate_error,
                                        auxiliary_error, wrapper_error) if error), None)
    if invalid is not None:
        return _not_measured(encoding, source_values, candidate_values,
                             auxiliary_values, wrapper_values,
                             invalid["reason"], detail=invalid.get("detail"))

    try:
        import tiktoken
    except (ImportError, ModuleNotFoundError) as error:
        return _not_measured(encoding, source_values, candidate_values,
                             auxiliary_values, wrapper_values,
                             "counter_unavailable", detail=str(error))
    try:
        encoder = tiktoken.get_encoding(encoding)
    except Exception as error:
        return _not_measured(encoding, source_values, candidate_values,
                             auxiliary_values, wrapper_values,
                             "encoding_unavailable", detail=str(error))

    source_tokens = sum(_encode(encoder, value["text"]) for value in source_values)
    candidate_tokens = sum(_encode(encoder, value["text"]) for value in candidate_values)
    auxiliary_tokens = sum(_encode(encoder, value["text"]) for value in auxiliary_values)
    wrapper_tokens = sum(_encode(encoder, value["text"]) for value in wrapper_values)
    candidate_total = candidate_tokens + auxiliary_tokens + wrapper_tokens
    result = {
        "status": "MEASURED",
        "encoding": encoding,
        "tokenizer": "tiktoken",
        "tokenizer_version": getattr(tiktoken, "__version__", "unknown"),
        "source": _group(source_values, source_tokens),
        "candidate": _group(candidate_values, candidate_tokens),
        "auxiliaries": _group(auxiliary_values, auxiliary_tokens),
        "wrapper": _group(wrapper_values, wrapper_tokens),
        "total": {"source": source_tokens, "candidate": candidate_total},
        "limits": ["El conteo no acredita fidelidad, cobertura ni equivalencia semántica."],
    }
    return result
