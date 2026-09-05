#!/usr/bin/env python3
"""Audita URNs de un índice KORA contra el censo JSON vivo."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path


URN_PATTERN = (
    r"urn:[a-z0-9]+(?:-[a-z0-9]+)*:kb:"
    r"[a-z0-9]+(?:-[a-z0-9]+)*")
URN_RE = re.compile(URN_PATTERN)
URN_TOKEN_RE = re.compile(
    r"urn:[^:\s`\"'<>\[\](){}|,;*]+:kb:"
    r"[^\s`\"'<>\[\](){}|,;*]+")
PREFIX_RE = re.compile(
    r"urn:[a-z0-9]+(?:-[a-z0-9]+)*:kb:[a-z0-9-]*")


def extraer_urns(texto: str) -> tuple[list[str], list[str]]:
    validas = []
    invalidas = []
    for coincidencia in URN_TOKEN_RE.finditer(texto):
        token = coincidencia.group(0).rstrip(".:!?")
        if URN_RE.fullmatch(token):
            validas.append(token)
        else:
            invalidas.append(token)
    return validas, invalidas


def separar_frontmatter(texto: str) -> tuple[str, str]:
    lineas = texto.splitlines()
    if not lineas or lineas[0].strip() != "---":
        raise ValueError("frontmatter incompleto: falta el delimitador inicial")
    for indice, linea in enumerate(lineas[1:], start=1):
        if linea.strip() == "---":
            return "\n".join(lineas[1:indice]), "\n".join(lineas[indice + 1:])
    raise ValueError("frontmatter incompleto: falta el delimitador final")


def encontrar_raiz(artefacto: Path) -> Path:
    for candidato in (artefacto.parent, *artefacto.parents):
        if (candidato / "kora.py").is_file():
            return candidato
    raise ValueError(f"no se encontró kora.py desde '{artefacto}'")


def cargar_censo(raiz: Path) -> list[dict]:
    nucleo = raiz / "kora.py"
    if not nucleo.is_file():
        raise ValueError(f"la raíz '{raiz}' no contiene kora.py")
    proceso = subprocess.run(
        [sys.executable, str(nucleo), "censo", "--json"],
        cwd=raiz, capture_output=True, text=True, check=False,
    )
    if proceso.returncode != 0:
        detalle = proceso.stderr.strip() or proceso.stdout.strip()
        raise ValueError(f"censo --json falló: {detalle[:500]}")
    try:
        datos = json.loads(proceso.stdout)
    except json.JSONDecodeError as exc:
        raise ValueError(f"censo --json devolvió JSON inválido: {exc}") from exc
    if not isinstance(datos, list) or not all(isinstance(e, dict) for e in datos):
        raise ValueError("censo --json no devolvió una lista de entradas")
    return datos


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Verifica resolución, duplicados y cobertura explícita "
                    "de URNs en un índice KORA.")
    parser.add_argument("artefacto", type=Path)
    parser.add_argument(
        "--root", type=Path,
        help="raíz KORA; por defecto se descubre desde el artefacto")
    parser.add_argument(
        "--prefix", action="append", default=[],
        help="prefijo KB publicado cuya exposición corporal se audita; repetible")
    parser.add_argument(
        "--require-complete", action="store_true",
        help="convierte toda omisión bajo --prefix en fallo")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = construir_parser()
    args = parser.parse_args(argv)
    if args.require_complete and not args.prefix:
        parser.error("--require-complete exige al menos un --prefix")
    for prefijo in args.prefix:
        if PREFIX_RE.fullmatch(prefijo) is None:
            parser.error(f"prefijo KB inválido: '{prefijo}'")

    artefacto = args.artefacto.resolve()
    if not artefacto.is_file():
        parser.error(f"el artefacto no es un archivo: '{artefacto}'")
    raiz = args.root.resolve() if args.root else encontrar_raiz(artefacto)

    try:
        frontmatter, cuerpo = separar_frontmatter(
            artefacto.read_text(encoding="utf-8-sig"))
        censo = cargar_censo(raiz)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 2

    referencias_frontmatter, invalidas_frontmatter = extraer_urns(frontmatter)
    referencias_cuerpo, invalidas_cuerpo = extraer_urns(cuerpo)
    urns_frontmatter = set(referencias_frontmatter)
    identidad = re.search(rf"(?m)^urn:\s*({URN_PATTERN})\s*$", frontmatter)
    if identidad is not None:
        urns_frontmatter.discard(identidad.group(1))
    conteo_cuerpo = Counter(referencias_cuerpo)
    urns_cuerpo = set(conteo_cuerpo)
    urns_citadas = urns_frontmatter | urns_cuerpo
    conteo_censo = Counter(
        str(entrada.get("urn"))
        for entrada in censo
        if entrada.get("tipo") == "conocimiento")
    no_resuelven = sorted(
        urn for urn in urns_citadas if conteo_censo[urn] == 0)
    ambiguas = sorted(
        urn for urn in urns_citadas if conteo_censo[urn] > 1)
    invalidas = sorted(set(invalidas_frontmatter + invalidas_cuerpo))
    fallo_resolucion = bool(no_resuelven or ambiguas or invalidas)
    estado_resolucion = "FAIL" if fallo_resolucion else "PASS"
    print(f"RESOLUCION {estado_resolucion} citadas={len(urns_citadas)} "
          f"no_resuelven={len(no_resuelven)} "
          f"ambiguas={len(ambiguas)} invalidas={len(invalidas)}")
    for urn in no_resuelven:
        print(f"NO_RESUELVE {urn}")
    for urn in ambiguas:
        print(f"AMBIGUA {urn} x{conteo_censo[urn]}")
    for urn in invalidas:
        print(f"URN_INVALIDA {urn}")

    duplicadas = sorted(
        (urn, cantidad) for urn, cantidad in conteo_cuerpo.items()
        if cantidad > 1)
    print(f"DUPLICADOS INFO cuerpo={len(duplicadas)}")
    for urn, cantidad in duplicadas:
        print(f"DUPLICADA {urn} x{cantidad}")

    fallo_cobertura = False
    publicadas = {
        str(entrada.get("urn"))
        for entrada in censo
        if entrada.get("tipo") == "conocimiento"
        and entrada.get("estado") == "publicado"
    }
    for prefijo in args.prefix:
        corpus_prefijo = {urn for urn in publicadas if urn.startswith(prefijo)}
        if not corpus_prefijo:
            fallo_cobertura = True
            print(f"COBERTURA_TEXTUAL ABSENT prefijo={prefijo} "
                  "publicadas=0 expuestas=0 omitidas=0")
            continue
        expuestas = corpus_prefijo & urns_cuerpo
        omitidas = sorted(corpus_prefijo - urns_cuerpo)
        if omitidas and args.require_complete:
            estado = "FAIL"
            fallo_cobertura = True
        elif omitidas:
            estado = "GAP"
        else:
            estado = "PASS"
        print(f"COBERTURA_TEXTUAL {estado} prefijo={prefijo} "
              f"publicadas={len(corpus_prefijo)} expuestas={len(expuestas)} "
              f"omitidas={len(omitidas)}")
        for urn in omitidas:
            print(f"OMISION {urn}")
        solo_frontmatter = sorted(
            (corpus_prefijo & urns_frontmatter) - urns_cuerpo)
        for urn in solo_frontmatter:
            print(f"SOLO_FRONTMATTER {urn}")

    return 1 if fallo_resolucion or fallo_cobertura else 0


if __name__ == "__main__":
    sys.exit(main())
