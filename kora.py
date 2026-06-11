#!/usr/bin/env python3
"""KORA pneuma — núcleo único.

Repositorio, catálogo y guardián de artefactos para sistemas LLM, sublimado a
un solo archivo de stdlib pura. La ley vive en ley/; este núcleo la realiza.

Gestos: censo, nombre, velar, transmutar, ciclo, ley.
La raíz del corpus es KORA_RAIZ si existe; si no, el directorio de este
archivo. El filesystem es la fuente de verdad; el censo siempre se deriva.
"""
from __future__ import annotations

import sys

if sys.version_info < (3, 11):
    sys.stderr.write(
        "kora.py requiere Python >= 3.11 (esta versión es %d.%d).\n"
        % (sys.version_info[0], sys.version_info[1])
    )
    sys.exit(2)

import argparse
import hashlib
import json
import os
import re
import shutil
from pathlib import Path

# ------------------------------------------------------------------ constantes

TARGETS_CONOCIDOS = ("claude-code", "codex", "opencode", "openclaw", "hermes")
TARGETS_REALIZADOS = ("claude-code", "codex", "opencode")

ESTADOS_CONOCIMIENTO = ("borrador", "publicado", "deprecado")
ESTADOS_AGENTICO = ("borrador", "activo", "deprecado", "retirado")

FORMAS = ("habilidad", "subagente", "agente", "plataforma")
ARNESES = ("utilidad", "disciplina", "delegado", "persona",
           "orquestador", "servicio", "arquetipo")
FAMILIAS = ("nota", "fuente", "bok")
LANGS = ("es", "en")

EJES = ("pi", "mu", "xi", "lambda", "phi")
RANGO_EJE = {"pi": 3, "mu": 3, "xi": 4, "lambda": 3, "phi": 4}  # máximo; mínimo 0
SIGMA_NOMBRES = ("safety", "fairness", "transparency",
                 "accountability", "sustainability")

# Dominio de proyección por forma (contrato §3.2; autoria-spec §5).
DOMINIO_FORMA = {
    "habilidad": {"pi": {1, 2}, "mu": {0, 1}, "xi": {1, 2},
                  "lambda": {0}, "phi": {1}},
    "subagente": {"pi": {1, 2, 3}, "mu": {0, 1, 2}, "xi": {1, 2, 3},
                  "lambda": {0, 1}, "phi": {1, 2}},
    "agente": {"pi": {2, 3}, "mu": {2, 3}, "xi": {2, 3, 4},
               "lambda": {0, 1, 2}, "phi": {1, 2, 3}},
    "plataforma": {"pi": {2, 3}, "mu": {3}, "xi": {3, 4},
                   "lambda": {1, 2, 3}, "phi": {1, 2, 3}},
}

# Compatibilidad arnés × forma (contrato §3.3; autoria-spec §6).
ARNES_POR_FORMA = {
    "habilidad": {"utilidad", "disciplina", "delegado"},
    "subagente": {"delegado", "persona"},
    "agente": {"persona", "orquestador"},
    "plataforma": {"orquestador", "servicio"},
}

RE_URN = re.compile(
    r"^urn:[a-z0-9]+(?:-[a-z0-9]+)*:(kb|artefacto):[a-z0-9]+(?:-[a-z0-9]+)*$")
RE_SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
RE_FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}$")
RE_CLAVE = re.compile(r"^([a-z][a-z0-9-]*):(.*)$")
RE_ENTERO = re.compile(r"^-?\d+$")

CAMPOS_COMUNES = {
    "urn", "nombre", "version", "estado", "descripcion", "fuente",
    "autor", "creado", "lang", "tags", "cita", "depende", "reemplaza", "refina",
}
CAMPOS_AGENTICOS = {
    "vector", "sigma", "arnes", "forma", "herramientas", "targets",
    "conocimiento", "componible", "estados",
}
CAMPOS_CONOCIMIENTO = {"familia"}

CAMPOS_OBLIGATORIOS_COMUNES = ("urn", "nombre", "version", "estado",
                               "descripcion", "fuente")
CAMPOS_OBLIGATORIOS_AGENTICOS = ("vector", "sigma", "arnes", "forma",
                                 "herramientas", "targets")
CAMPOS_LISTA = ("tags", "cita", "depende", "reemplaza", "refina",
                "herramientas", "targets", "conocimiento", "componible",
                "estados", "vector", "sigma")
CAMPOS_RELACION = ("cita", "depende", "reemplaza", "refina")

CHECKS = ("forma-valida", "nombre-verdadero", "lugar-coincide",
          "vector-en-reticulo", "leyes-inter-eje", "dominio-forma",
          "arnes-compatible", "estado-valido", "referencias-resuelven",
          "relaciones-legales", "targets-conocidos", "sello-fresco")
CHECK_ESTRICTO = "publicacion-digna"


def raiz_corpus() -> Path:
    """Raíz del corpus: KORA_RAIZ si existe, si no el directorio de kora.py."""
    env = os.environ.get("KORA_RAIZ")
    if env:
        return Path(env).resolve()
    return Path(__file__).resolve().parent


# ------------------------------------------------- parser de frontmatter (§2)

class ErrorDeForma(Exception):
    """Error de parse del frontmatter, con número de línea (1-indexado)."""

    def __init__(self, linea: int, mensaje: str):
        self.linea = linea
        self.mensaje = mensaje
        super().__init__(f"línea {linea}: {mensaje}")


def _quitar_comentario(crudo: str) -> str:
    """Recorta un comentario al final de línea, respetando comillas dobles."""
    dentro = False
    for i, ch in enumerate(crudo):
        if ch == '"':
            dentro = not dentro
        elif ch == "#" and not dentro and (i == 0 or crudo[i - 1] in " \t"):
            return crudo[:i].rstrip()
    return crudo


def _dividir_comas(interior: str, linea: int) -> list[str]:
    """Divide los ítems de una lista inline por comas de primer nivel."""
    items, actual, dentro = [], [], False
    for ch in interior:
        if ch == '"':
            dentro = not dentro
            actual.append(ch)
        elif ch == "[" and not dentro:
            raise ErrorDeForma(linea, "listas anidadas no permitidas")
        elif ch == "]" and not dentro:
            raise ErrorDeForma(
                linea, "lista mal formada: ']' interno (se espera un único "
                       "'[' inicial y un único ']' final, sin texto después)")
        elif ch == "{" and not dentro:
            raise ErrorDeForma(linea, "objetos '{}' no permitidos")
        elif ch == "," and not dentro:
            items.append("".join(actual))
            actual = []
        else:
            actual.append(ch)
    if dentro:
        raise ErrorDeForma(linea, "comillas sin cerrar")
    items.append("".join(actual))
    return items


def _parsear_escalar(s: str, linea: int):
    """Parsea un escalar: string (con o sin comillas), entero o fecha."""
    if s == "":
        raise ErrorDeForma(linea, "valor o elemento de lista vacío")
    if s[0] == '"':
        if len(s) < 2 or not s.endswith('"') or '"' in s[1:-1]:
            raise ErrorDeForma(linea, "string con comillas mal cerradas")
        return s[1:-1]
    if s[0] == "[":
        raise ErrorDeForma(linea, "listas anidadas no permitidas")
    if s[0] == "{":
        raise ErrorDeForma(linea, "objetos '{}' no permitidos")
    if s[0] in "|>":
        raise ErrorDeForma(linea, "bloques multilínea ('|', '>') no permitidos")
    if RE_ENTERO.match(s):
        return int(s)
    return s


def _parsear_valor(crudo: str, linea: int):
    """Parsea el valor de una línea `clave: valor` (escalar o lista inline)."""
    s = _quitar_comentario(crudo).strip()
    if s == "":
        raise ErrorDeForma(
            linea, "valor vacío (los bloques anidados no están permitidos)")
    if s[0] == "[":
        if not s.endswith("]"):
            if "]" in s:
                raise ErrorDeForma(
                    linea, "lista mal formada: hay texto después del "
                           "cierre ']'")
            raise ErrorDeForma(linea, "lista inline sin cierre ']'")
        interior = s[1:-1].strip()
        if interior == "":
            return []
        return [_parsear_escalar(item.strip(), linea)
                for item in _dividir_comas(interior, linea)]
    return _parsear_escalar(s, linea)


def parsear_archivo(texto: str) -> tuple[dict, str]:
    """Parsea un artefacto: devuelve (campos del frontmatter, cuerpo).

    Gramática del contrato §2: subconjunto regular de YAML. Sin anidamiento,
    sin multilínea, sin objetos. Claves duplicadas son error de parse.
    """
    lineas = texto.split("\n")
    if not lineas or lineas[0].strip() != "---":
        raise ErrorDeForma(1, "falta frontmatter: el archivo debe abrir con '---'")
    cierre = None
    for i in range(1, len(lineas)):
        if lineas[i].strip() == "---":
            cierre = i
            break
    if cierre is None:
        raise ErrorDeForma(len(lineas), "frontmatter sin cierre '---'")
    campos: dict = {}
    for i in range(1, cierre):
        cruda = lineas[i]
        num = i + 1  # número de línea 1-indexado en el archivo
        if not cruda.strip():
            continue
        if cruda.lstrip().startswith("#"):
            continue  # comentario en línea propia
        if cruda[0] in " \t":
            raise ErrorDeForma(
                num, "anidamiento no permitido: la línea comienza indentada")
        m = RE_CLAVE.match(cruda)
        if not m:
            raise ErrorDeForma(
                num, "línea no reconocida: se espera 'clave: valor' con "
                     "clave [a-z][a-z0-9-]*")
        clave, resto = m.group(1), m.group(2)
        if clave in campos:
            raise ErrorDeForma(num, f"clave duplicada: '{clave}'")
        if resto == "":
            raise ErrorDeForma(
                num, f"la clave '{clave}' no tiene valor en la misma línea "
                     "(los bloques anidados no están permitidos)")
        if not resto.startswith(" "):
            raise ErrorDeForma(num, "se requiere un espacio después de ':'")
        campos[clave] = _parsear_valor(resto[1:], num)
    cuerpo = "\n".join(lineas[cierre + 1:])
    return campos, cuerpo


# --------------------------------------------------- corpus y derivación (§2.4)

def derivar_tipo(campos: dict) -> tuple[str | None, str | None]:
    """Deriva el tipo del artefacto. El tipo no se declara: se es."""
    if "vector" in campos:
        forma = campos.get("forma")
        if forma == "habilidad":
            return "skill", None
        if forma in ("subagente", "agente", "plataforma"):
            return "agente", None
        if forma is None:
            return None, "el campo 'forma' es obligatorio cuando 'vector' está presente"
        return None, (f"forma desconocida: '{forma}' "
                      f"(esperado: {'|'.join(FORMAS)})")
    return "conocimiento", None


class Artefacto:
    """Un artefacto cargado del filesystem (o su error de parse)."""

    __slots__ = ("path", "rel", "zona", "campos", "cuerpo",
                 "tipo", "error_parse", "error_tipo")

    def __init__(self, path: Path, rel: str, zona: str):
        self.path = path
        self.rel = rel
        self.zona = zona
        self.campos: dict = {}
        self.cuerpo = ""
        self.tipo: str | None = None
        self.error_parse: str | None = None
        self.error_tipo: str | None = None

    @property
    def urn(self) -> str | None:
        u = self.campos.get("urn")
        return u if isinstance(u, str) else None

    @property
    def cadena_estados(self) -> tuple:
        if self.tipo == "conocimiento":
            return ESTADOS_CONOCIMIENTO
        return ESTADOS_AGENTICO

    def vector_valido(self) -> list | None:
        v = self.campos.get("vector")
        if isinstance(v, list) and len(v) == 5 and all(
                isinstance(x, int) for x in v):
            return v
        return None

    def sigma_valido(self) -> list | None:
        s = self.campos.get("sigma")
        if isinstance(s, list) and len(s) == 5 and all(
                isinstance(x, int) for x in s):
            return s
        return None


def cargar_corpus(raiz: Path) -> list[Artefacto]:
    """Recorre artefactos/ y carga cada artefacto. Nunca lanza por contenido."""
    arts: list[Artefacto] = []
    base = raiz / "artefactos"
    if not base.is_dir():
        return arts
    rutas: list[tuple[str, Path]] = []
    for zona in ("conocimiento", "agentes"):
        zdir = base / zona
        if zdir.is_dir():
            rutas.extend((zona, p) for p in sorted(zdir.rglob("*.md")))
    zdir = base / "skills"
    if zdir.is_dir():
        # Solo skills/{ns}/{nombre}/SKILL.md es artefacto (profundidad exacta
        # 3 bajo la zona); un .md dentro de referencias/ jamás se indexa.
        rutas.extend(("skills", p) for p in sorted(zdir.glob("*/*/SKILL.md")))
    for zona, p in rutas:
        art = Artefacto(p, p.relative_to(raiz).as_posix(), zona)
        try:
            # utf-8-sig: acepta y descarta el BOM si el archivo lo trae.
            campos, cuerpo = parsear_archivo(
                p.read_text(encoding="utf-8-sig"))
            art.campos, art.cuerpo = campos, cuerpo
            art.tipo, art.error_tipo = derivar_tipo(campos)
        except ErrorDeForma as exc:
            art.error_parse = str(exc)
        arts.append(art)
    return arts


def resolver(arts: list[Artefacto], urn: str) -> Artefacto | None:
    """Resuelve un URN en el corpus — incluidos deprecados y retirados."""
    for art in arts:
        if art.urn == urn:
            return art
    return None


# ----------------------------------------------------------------- censo

def construir_censo(arts: list[Artefacto]) -> list[dict]:
    """Catálogo derivado del filesystem. Nunca es autoridad: se regenera."""
    entradas = []
    for art in arts:
        entradas.append({
            "urn": art.urn or "",
            "tipo": art.tipo or "invalido",
            "nombre": str(art.campos.get("nombre", "")),
            "version": str(art.campos.get("version", "")),
            "estado": str(art.campos.get("estado", "")),
            "path": art.rel,
        })
    entradas.sort(key=lambda e: (e["urn"], e["path"]))
    return entradas


def censo_json(entradas: list[dict]) -> str:
    return json.dumps(entradas, ensure_ascii=False, indent=2) + "\n"


# ----------------------------------------------------------- checks de velar

def _campos_permitidos(art: Artefacto) -> set:
    if art.tipo == "conocimiento":
        return CAMPOS_COMUNES | CAMPOS_CONOCIMIENTO
    return CAMPOS_COMUNES | CAMPOS_AGENTICOS


def _es_lista_de_strings(v) -> bool:
    return isinstance(v, list) and all(isinstance(x, str) for x in v)


def chk_forma_valida(arts, raiz):
    fallos = []

    def f(art, msg):
        fallos.append((art.rel, msg))

    for art in arts:
        if art.error_parse:
            f(art, f"no parsea: {art.error_parse}")
            continue
        if art.error_tipo:
            f(art, art.error_tipo)
        permitidos = _campos_permitidos(art)
        for clave in art.campos:
            if clave not in permitidos:
                f(art, f"clave desconocida: '{clave}' (el shape es cerrado)")
        for clave in CAMPOS_OBLIGATORIOS_COMUNES:
            if clave not in art.campos:
                f(art, f"campo obligatorio ausente: '{clave}'")
        for clave in ("urn", "nombre", "version", "estado", "descripcion",
                      "fuente", "autor", "creado", "lang", "arnes", "forma",
                      "familia"):
            if clave in art.campos and not isinstance(art.campos[clave], str):
                f(art, f"el campo '{clave}' debe ser un string escalar")
        for clave in CAMPOS_LISTA:
            if clave in art.campos and not isinstance(art.campos[clave], list):
                f(art, f"el campo '{clave}' debe ser una lista inline")
        version = art.campos.get("version")
        if isinstance(version, str) and not RE_SEMVER.match(version):
            f(art, f"version no es semver X.Y.Z: '{version}'")
        creado = art.campos.get("creado")
        if isinstance(creado, str) and not RE_FECHA.match(creado):
            f(art, f"creado no es fecha YYYY-MM-DD: '{creado}'")
        lang = art.campos.get("lang")
        if lang is not None and lang not in LANGS:
            f(art, f"lang inválido: '{lang}' (esperado: es|en)")
        for clave in CAMPOS_RELACION + ("conocimiento", "componible", "tags",
                                        "herramientas", "targets", "estados"):
            v = art.campos.get(clave)
            if isinstance(v, list) and not _es_lista_de_strings(v):
                f(art, f"el campo '{clave}' debe ser una lista de strings")
        if art.tipo == "conocimiento":
            familia = art.campos.get("familia")
            if familia is None:
                f(art, "campo obligatorio ausente: 'familia'")
            elif familia not in FAMILIAS:
                f(art, f"familia inválida: '{familia}' "
                       f"(esperado: {'|'.join(FAMILIAS)})")
        elif art.tipo in ("skill", "agente"):
            for clave in CAMPOS_OBLIGATORIOS_AGENTICOS:
                if clave not in art.campos:
                    f(art, f"campo obligatorio ausente: '{clave}'")
            arnes = art.campos.get("arnes")
            if isinstance(arnes, str) and arnes not in ARNESES:
                f(art, f"arnes inválido: '{arnes}' "
                       f"(esperado: {'|'.join(ARNESES)})")
            for clave in ("vector", "sigma"):
                v = art.campos.get(clave)
                if isinstance(v, list) and (
                        len(v) != 5 or not all(isinstance(x, int) for x in v)):
                    f(art, f"el campo '{clave}' debe ser una lista de 5 enteros")
            herr = art.campos.get("herramientas")
            if isinstance(herr, list) and herr == [] and \
                    art.campos.get("forma") != "habilidad":
                f(art, "herramientas solo puede ser [] si forma es habilidad")
            targets = art.campos.get("targets")
            if isinstance(targets, list) and not targets:
                f(art, "targets no puede ser una lista vacía")
    return fallos


def chk_nombre_verdadero(arts, raiz):
    fallos = []
    vistos: dict[str, str] = {}
    for art in arts:
        urn = art.urn
        if art.error_parse or urn is None:
            continue
        if not RE_URN.match(urn):
            fallos.append((art.rel, f"URN no cumple la gramática "
                           f"urn:{{ns}}:(kb|artefacto):{{id}} sin versión "
                           f"embebida: '{urn}'"))
            continue
        regimen = urn.split(":")[2]
        if art.tipo == "conocimiento" and regimen != "kb":
            fallos.append((art.rel, f"régimen de URN incoherente: el "
                           f"conocimiento exige 'kb', tiene '{regimen}'"))
        if art.tipo in ("skill", "agente") and regimen != "artefacto":
            fallos.append((art.rel, f"régimen de URN incoherente: lo agéntico "
                           f"exige 'artefacto', tiene '{regimen}'"))
        if urn in vistos:
            fallos.append((art.rel, f"URN duplicado: '{urn}' "
                           f"(también en {vistos[urn]})"))
        else:
            vistos[urn] = art.rel
    return fallos


def chk_lugar_coincide(arts, raiz):
    fallos = []
    zona_de_tipo = {"conocimiento": "conocimiento", "agente": "agentes",
                    "skill": "skills"}
    for art in arts:
        if art.error_parse or art.tipo is None:
            continue
        urn = art.urn
        nombre = art.campos.get("nombre")
        if urn is None or not RE_URN.match(urn) or not isinstance(nombre, str):
            continue
        zona_esperada = zona_de_tipo[art.tipo]
        if art.zona != zona_esperada:
            fallos.append((art.rel, f"zona incoherente: un {art.tipo} debe "
                           f"vivir bajo artefactos/{zona_esperada}/"))
            continue
        ns = urn.split(":")[1]
        partes = Path(art.rel).parts  # ('artefactos', zona, ns, ...)
        if len(partes) < 4 or partes[2] != ns:
            fallos.append((art.rel, f"namespace incoherente: el URN declara "
                           f"'{ns}' y el path no lo refleja"))
            continue
        if art.tipo == "skill":
            if len(partes) != 5 or partes[3] != nombre or \
                    partes[4] != "SKILL.md":
                fallos.append((art.rel, f"path esperado: artefactos/skills/"
                               f"{ns}/{nombre}/SKILL.md"))
        else:
            if len(partes) != 4 or partes[3] != f"{nombre}.md":
                fallos.append((art.rel, f"path esperado: artefactos/"
                               f"{zona_esperada}/{ns}/{nombre}.md"))
    # Vigilancia de la zona skills: cualquier .md fuera de las fibras
    # conocidas es fallo claro, no artefacto fantasma ni crash.
    base_skills = raiz / "artefactos" / "skills"
    if base_skills.is_dir():
        for p in sorted(base_skills.rglob("*.md")):
            partes = p.relative_to(base_skills).parts
            if len(partes) == 3 and partes[2] == "SKILL.md":
                continue  # artefacto legítimo: skills/{ns}/{nombre}/SKILL.md
            if len(partes) >= 3 and partes[2] == "referencias":
                continue  # fibra conocida: referencias/ se ignora
            rel = p.relative_to(raiz).as_posix()
            fallos.append((rel, "archivo .md fuera de lugar bajo artefactos/"
                           "skills/: solo se reconoce skills/{ns}/{nombre}/"
                           "SKILL.md como artefacto y skills/{ns}/{nombre}/"
                           "referencias/ como fibra ignorada; muévelo o "
                           "elimínalo"))
    return fallos


def chk_vector_en_reticulo(arts, raiz):
    fallos = []
    for art in arts:
        if art.tipo not in ("skill", "agente"):
            continue
        vector = art.vector_valido()
        if vector is not None:
            for i, eje in enumerate(EJES):
                if not 0 <= vector[i] <= RANGO_EJE[eje]:
                    fallos.append((art.rel, f"{eje}={vector[i]} fuera del "
                                   f"retículo 0..{RANGO_EJE[eje]}"))
        sigma = art.sigma_valido()
        if sigma is not None:
            for i, v in enumerate(sigma):
                if not 0 <= v <= 3:
                    fallos.append((art.rel, f"sigma.{SIGMA_NOMBRES[i]}={v} "
                                   f"fuera del retículo 0..3"))
    return fallos


def chk_leyes_inter_eje(arts, raiz):
    fallos = []
    for art in arts:
        if art.tipo not in ("skill", "agente"):
            continue
        v, s = art.vector_valido(), art.sigma_valido()
        if v is None or s is None:
            continue
        pi, mu, xi, lam, phi = v
        if pi >= 3 and mu < 1:
            fallos.append((art.rel, f"ley 1 violada: pi>=3 exige mu>=1 "
                           f"(pi={pi}, mu={mu})"))
        if xi == 4 and lam < 1:
            fallos.append((art.rel, f"ley 2 violada: xi=4 exige lambda>=1 "
                           f"(lambda={lam})"))
        if phi >= 2 and mu < 1:
            fallos.append((art.rel, f"ley 3 violada: phi>=2 exige mu>=1 "
                           f"(phi={phi}, mu={mu})"))
        if s[3] >= 2 and s[2] < 2:
            fallos.append((art.rel, f"ley 4 violada: accountability>=2 exige "
                           f"transparency>=2 (accountability={s[3]}, "
                           f"transparency={s[2]})"))
        if lam == 3 and min(s) < 2:
            fallos.append((art.rel, f"ley 5 violada: lambda=3 exige todas las "
                           f"componentes de sigma >= 2 (sigma={s})"))
    return fallos


def chk_dominio_forma(arts, raiz):
    fallos = []
    for art in arts:
        if art.tipo not in ("skill", "agente"):
            continue
        forma = art.campos.get("forma")
        vector = art.vector_valido()
        if forma not in DOMINIO_FORMA or vector is None:
            continue
        dominio = DOMINIO_FORMA[forma]
        for i, eje in enumerate(EJES):
            if vector[i] not in dominio[eje]:
                permitido = ",".join(str(x) for x in sorted(dominio[eje]))
                fallos.append((art.rel, f"fuera del dominio de la forma "
                               f"'{forma}': {eje}={vector[i]} "
                               f"(permitido: {{{permitido}}})"))
    return fallos


def chk_arnes_compatible(arts, raiz):
    fallos = []
    for art in arts:
        if art.tipo not in ("skill", "agente"):
            continue
        arnes = art.campos.get("arnes")
        forma = art.campos.get("forma")
        if arnes not in ARNESES or forma not in ARNES_POR_FORMA:
            continue
        if arnes == "arquetipo":
            fallos.append((art.rel, "el arnés 'arquetipo' no se materializa "
                           "en ninguna forma"))
        elif arnes not in ARNES_POR_FORMA[forma]:
            compat = ", ".join(sorted(ARNES_POR_FORMA[forma]))
            fallos.append((art.rel, f"arnés '{arnes}' incompatible con la "
                           f"forma '{forma}' (compatibles: {compat})"))
    return fallos


def chk_estado_valido(arts, raiz):
    fallos = []
    for art in arts:
        if art.error_parse or art.tipo is None:
            continue
        estado = art.campos.get("estado")
        if estado is not None and estado not in art.cadena_estados:
            cadena = " -> ".join(art.cadena_estados)
            fallos.append((art.rel, f"estado '{estado}' no pertenece a la "
                           f"cadena del tipo {art.tipo}: {cadena}"))
    return fallos


def chk_referencias_resuelven(arts, raiz):
    fallos = []
    urns = {a.urn for a in arts if a.urn}
    for art in arts:
        if art.error_parse:
            continue
        for campo in CAMPOS_RELACION + ("conocimiento", "componible"):
            refs = art.campos.get(campo)
            if not isinstance(refs, list):
                continue
            for ref in refs:
                if not isinstance(ref, str) or ref not in urns:
                    fallos.append((art.rel, f"referencia no resuelve en el "
                                   f"censo: '{ref}' (campo '{campo}')"))
                    continue
                if campo == "conocimiento" and ":kb:" not in ref:
                    fallos.append((art.rel, f"el campo 'conocimiento' solo "
                                   f"admite URNs de régimen kb: '{ref}'"))
                if campo == "componible" and ":artefacto:" not in ref:
                    fallos.append((art.rel, f"el campo 'componible' solo "
                                   f"admite URNs de régimen artefacto: '{ref}'"))
    return fallos


def _ciclos_en(grafo: dict[str, list[str]]) -> list[list[str]]:
    """Detecta ciclos en un digrafo. Devuelve cada ciclo normalizado y único.

    DFS iterativo con pila explícita: cadenas arbitrariamente profundas
    (miles de nodos) no pueden reventar el límite de recursión de Python.
    """
    BLANCO, GRIS, NEGRO = 0, 1, 2
    color = {n: BLANCO for n in grafo}
    ciclos: list[list[str]] = []
    vistos: set[tuple] = set()
    for inicio in sorted(grafo):
        if color[inicio] != BLANCO:
            continue
        color[inicio] = GRIS
        camino = [inicio]
        indice = {inicio: 0}
        pila = [(inicio, iter(grafo.get(inicio, [])))]
        while pila:
            nodo, vecinos = pila[-1]
            avanzado = False
            for vecino in vecinos:
                if vecino not in grafo:
                    continue
                if color[vecino] == GRIS:
                    ciclo = camino[indice[vecino]:]
                    k = ciclo.index(min(ciclo))
                    norm = tuple(ciclo[k:] + ciclo[:k])
                    if norm not in vistos:
                        vistos.add(norm)
                        ciclos.append(list(norm))
                elif color[vecino] == BLANCO:
                    color[vecino] = GRIS
                    indice[vecino] = len(camino)
                    camino.append(vecino)
                    pila.append((vecino, iter(grafo.get(vecino, []))))
                    avanzado = True
                    break
            if not avanzado:
                pila.pop()
                camino.pop()
                del indice[nodo]
                color[nodo] = NEGRO
    return ciclos


def chk_relaciones_legales(arts, raiz):
    fallos = []
    por_urn = {a.urn: a for a in arts if a.urn}
    for campo in ("depende", "reemplaza", "refina"):
        grafo = {}
        for art in arts:
            if art.urn and isinstance(art.campos.get(campo), list):
                grafo[art.urn] = [r for r in art.campos[campo]
                                  if isinstance(r, str)]
        for urn in list(grafo):
            for ref in grafo[urn]:
                grafo.setdefault(ref, [])
        for ciclo in _ciclos_en(grafo):
            origen = por_urn.get(ciclo[0])
            rel = origen.rel if origen else ciclo[0]
            ruta = " -> ".join(ciclo + [ciclo[0]])
            extra = " (viola aciclicidad y antisimetría)" \
                if campo == "reemplaza" and len(ciclo) == 2 else ""
            fallos.append((rel, f"ciclo en '{campo}': {ruta}{extra}"))
    for art in arts:
        refs = art.campos.get("reemplaza")
        if not isinstance(refs, list):
            continue
        for ref in refs:
            objetivo = por_urn.get(ref) if isinstance(ref, str) else None
            if objetivo is None:
                continue  # la resolución la reporta referencias-resuelven
            estado = objetivo.campos.get("estado")
            if estado not in ("deprecado", "retirado"):
                fallos.append((art.rel, f"reemplaza exige target deprecado o "
                               f"retirado: '{ref}' está '{estado}'"))
    return fallos


def chk_targets_conocidos(arts, raiz):
    fallos = []
    for art in arts:
        targets = art.campos.get("targets")
        if not isinstance(targets, list):
            continue
        for t in targets:
            if t not in TARGETS_CONOCIDOS:
                fallos.append((art.rel, f"target desconocido: '{t}' "
                               f"(conocidos: {', '.join(TARGETS_CONOCIDOS)})"))
    return fallos


RE_SELLO = re.compile(r"<!-- kora:sello\n(.*?)\n-->", re.DOTALL)


def chk_sello_fresco(arts, raiz):
    fallos = []
    emision = raiz / "_emision"
    if not emision.is_dir():
        return fallos
    por_urn = {a.urn: a for a in arts if a.urn}
    emitidos: list[Path] = []
    for target_dir in sorted(p for p in emision.iterdir() if p.is_dir()):
        skills = target_dir / "skills"
        if skills.is_dir():
            emitidos.extend(sorted(skills.glob("*/SKILL.md")))
        agents = target_dir / "agents"
        if agents.is_dir():
            emitidos.extend(sorted(agents.glob("*.md")))
    for path in emitidos:
        rel = path.relative_to(raiz).as_posix()
        texto = path.read_text(encoding="utf-8")
        # El sello real es el ÚLTIMO bloque: el cuerpo puede citar sellos
        # de ejemplo (docs, la propia ley) sin volver rancia la emisión.
        sellos = list(RE_SELLO.finditer(texto))
        if not sellos:
            fallos.append((rel, "emisión sin sello kora:sello"))
            continue
        m = sellos[-1]
        lineas = dict(
            l.split(": ", 1) for l in m.group(1).split("\n")
            if ": " in l and not l.startswith(" "))
        urn = lineas.get("fuente", "")
        hash_decl = lineas.get("hash-fuente", "")
        fuente = por_urn.get(urn)
        if fuente is None:
            fallos.append((rel, f"la fuente del sello no resuelve: '{urn}'"))
            continue
        actual = "sha256:" + hashlib.sha256(
            fuente.path.read_bytes()).hexdigest()
        if hash_decl != actual:
            fallos.append((rel, "emisión rancia, re-transmutar (hash-fuente "
                           "no coincide con la fuente actual)"))
    return fallos


def chk_publicacion_digna(arts, raiz):
    fallos = []
    for art in arts:
        if art.error_parse or art.tipo is None:
            continue
        estado = art.campos.get("estado")
        if art.tipo == "conocimiento" and estado == "publicado":
            tags = art.campos.get("tags")
            n = len(tags) if isinstance(tags, list) else 0
            if n < 3:
                fallos.append((art.rel, f"conocimiento publicado exige >=3 "
                               f"tags (tiene {n})"))
        if estado in ("activo", "publicado"):
            for campo in ("descripcion", "fuente"):
                v = art.campos.get(campo)
                if not isinstance(v, str) or not v.strip():
                    fallos.append((art.rel, f"artefacto {estado} exige "
                                   f"'{campo}' no vacío"))
    return fallos


FUNCIONES_CHECK = {
    "forma-valida": chk_forma_valida,
    "nombre-verdadero": chk_nombre_verdadero,
    "lugar-coincide": chk_lugar_coincide,
    "vector-en-reticulo": chk_vector_en_reticulo,
    "leyes-inter-eje": chk_leyes_inter_eje,
    "dominio-forma": chk_dominio_forma,
    "arnes-compatible": chk_arnes_compatible,
    "estado-valido": chk_estado_valido,
    "referencias-resuelven": chk_referencias_resuelven,
    "relaciones-legales": chk_relaciones_legales,
    "targets-conocidos": chk_targets_conocidos,
    "sello-fresco": chk_sello_fresco,
    CHECK_ESTRICTO: chk_publicacion_digna,
}


def velar_todo(raiz: Path, estricto: bool = False) -> dict[str, list]:
    """Corre todos los checks. Devuelve {check_id: [(path, mensaje), ...]}."""
    arts = cargar_corpus(raiz)
    ids = list(CHECKS) + ([CHECK_ESTRICTO] if estricto else [])
    return {cid: FUNCIONES_CHECK[cid](arts, raiz) for cid in ids}


# ------------------------------------------------------- transmutación (§6)

def _m(filas):
    """Construye la matriz de un eje: {valor: (proyectado, fidelidad, razón)}."""
    return dict(filas)


# Matrices de preservación (contrato §6.1, fieles a las runtime-extensions).
MATRICES = {
    "claude-code": {
        "pi": _m({0: (0, "full", None), 1: (1, "full", None),
                  2: (2, "full", None),
                  3: (2, "partial", "fixed-points se aplanan")}),
        "mu": _m({0: (0, "full", None), 1: (1, "full", None),
                  2: (2, "full", None),
                  3: (None, "none",
                      "sin ambiente always-on; usar openclaw")}),
        "xi": _m({0: (0, "full", None), 1: (1, "full", None),
                  2: (2, "full", None),
                  3: (2, "partial", "multi-fase se aplana"),
                  4: (2, "partial", "operad dinámica no soportada")}),
        "lambda": _m({0: (0, "full", None), 1: (1, "full", None),
                      2: (1, "partial",
                          "ecosistema colapsa a organizacional"),
                      3: (None, "none",
                          "society-in-the-loop no soportado")}),
        "phi": _m({0: (0, "full", None), 1: (1, "full", None),
                   2: (2, "full", None),
                   3: (2, "partial", "cognición híbrida no nativa"),
                   4: (None, "none", "co-evolutivo no soportado")}),
        "sigma-max": [3, 2, 3, 2, 1],
    },
    "codex": {
        "pi": _m({0: (0, "full", None), 1: (1, "full", None),
                  2: (2, "full", None),
                  3: (3, "partial", "recursión con budget acotado")}),
        "mu": _m({0: (0, "full", None), 1: (1, "full", None),
                  2: (1, "partial", "session-resumable, sin memoria "
                      "transparente cross-session"),
                  3: (None, "none", "CLI síncrono, no daemon")}),
        "xi": _m({0: (0, "full", None), 1: (1, "full", None),
                  2: (2, "full", None),
                  3: (2, "partial", "multi-fase se aplana"),
                  4: (2, "partial", "operad dinámica no soportada")}),
        "lambda": _m({0: (0, "full", None), 1: (1, "full", None),
                      2: (1, "partial",
                          "ecosistema colapsa a organizacional"),
                      3: (None, "none",
                          "society-in-the-loop no soportado")}),
        "phi": _m({0: (0, "full", None), 1: (1, "full", None),
                   2: (2, "partial", "colaborativo vía resume+approvals, "
                       "sin identidad persistente"),
                   3: (2, "partial", "cognición híbrida no nativa"),
                   4: (None, "none", "co-evolutivo no soportado")}),
        "sigma-max": [3, 2, 2, 2, 1],
    },
    "opencode": {
        "pi": _m({0: (0, "full", None), 1: (1, "full", None),
                  2: (2, "full", None),
                  3: (3, "partial", "steps acotados")}),
        "mu": _m({0: (0, "full", None), 1: (1, "full", None),
                  2: (2, "partial", "contexto parent/child, sin memoria "
                      "transparente"),
                  3: (None, "none", "CLI/TUI síncrono, no daemon")}),
        "xi": _m({0: (0, "full", None), 1: (1, "full", None),
                  2: (2, "full", None),
                  3: (3, "partial", "multi-fase vía subagentes, coreografías "
                      "largas dependen del wrapper"),
                  4: (3, "partial", "operad no soportada")}),
        "lambda": _m({0: (0, "full", None), 1: (1, "full", None),
                      2: (1, "partial",
                          "ecosistema colapsa a organizacional"),
                      3: (None, "none",
                          "society-in-the-loop no soportado")}),
        "phi": _m({0: (0, "full", None), 1: (1, "full", None),
                   2: (2, "full", None),
                   3: (2, "partial", "cognición híbrida no nativa"),
                   4: (None, "none", "co-evolutivo no soportado")}),
        "sigma-max": [3, 2, 2, 2, 1],
    },
}

# Razón por componente de sigma cuando la fuente excede el máximo del target.
SIGMA_RAZONES = {
    "claude-code": {
        "safety": "máximo del runtime",
        "fairness": "declarativo, sin enforcement en runtime",
        "transparency": "máximo del runtime",
        "accountability": "sin audit trail persistente cross-session",
        "sustainability": "solo declarativo",
    },
    "codex": {
        "safety": "máximo del runtime",
        "fairness": "declarativo, sin enforcement en runtime",
        "transparency": "solo logs de output e historial de conversación",
        "accountability": "session-id rastreable, sin audit trail "
                          "cross-session transparente",
        "sustainability": "solo declarativo",
    },
    "opencode": {
        "safety": "máximo del runtime",
        "fairness": "declarativo, sin enforcement en runtime",
        "transparency": "explicabilidad limitada al output de la sesión",
        "accountability": "jerarquía de sesiones parent/child, sin audit "
                          "trail cross-session transparente",
        "sustainability": "solo declarativo",
    },
}

# Quién sí soporta un eje que el target rechaza (para el mensaje de fallo).
QUIEN_SOPORTA = {
    ("mu", 3): "openclaw (reconocido por la ley, no realizado en esta "
               "encarnación; ver GENESIS.md)",
    ("lambda", 3): "ninguno de los runtimes reconocidos",
    ("phi", 4): "ninguno de los runtimes reconocidos",
}

DOCTRINA_DUAL_MODE = """## Modos de invocacion

Este artefacto es dual-mode (arnés persona). Declara su modo efectivo:

- **Modo subagente (batch)**: invocado vía Task() por otro agente. Opera con
  entrada/salida cerrada, sin diálogo HITL intra-tarea; entrega dictamen y
  handoff, no conversación.
- **Modo persona (encarnación)**: cargado como instrucciones del hilo
  principal. Dispone del diálogo HITL nativo, de las skills y de las
  herramientas de la sesión; es el único modo que realiza la fidelidad
  declarada en el sello."""


class ErrorTransmutacion(Exception):
    """La transmutación no procede; el mensaje explica por qué."""


def proyectar(vector: list, sigma: list, target: str) -> dict:
    """Proyecta el vector por la matriz del target.

    Monotonía por construcción: cada eje se proyecta a
    min(valor, proyección de la matriz); nunca hacia arriba.
    Si un eje cae a None, la transmutación FALLA: jamás degradación silenciosa.
    """
    matriz = MATRICES[target]
    proy_vector: list[int] = []
    fidelidad: dict[str, str] = {}
    perdidas: list[tuple[str, str, str, str]] = []
    for i, eje in enumerate(EJES):
        valor = vector[i]
        destino, fid, razon = matriz[eje][valor]
        if destino is None:
            soporta = QUIEN_SOPORTA.get(
                (eje, valor), "ninguno de los runtimes reconocidos")
            raise ErrorTransmutacion(
                f"el eje {eje}={valor} no es proyectable a {target}: {razon}. "
                f"Lo soporta: {soporta}.")
        proyectado = min(destino, valor)  # monotonía por construcción
        proy_vector.append(proyectado)
        fidelidad[eje] = fid
        if fid != "full":
            perdidas.append((eje, str(valor), str(proyectado), razon))
    maximos = matriz["sigma-max"]
    proy_sigma: list[int] = []
    sigma_partial = False
    for i, valor in enumerate(sigma):
        tope = maximos[i]
        proyectado = min(valor, tope)
        proy_sigma.append(proyectado)
        if valor > tope:
            sigma_partial = True
            perdidas.append((f"sigma.{SIGMA_NOMBRES[i]}", str(valor),
                             str(proyectado),
                             SIGMA_RAZONES[target][SIGMA_NOMBRES[i]]))
    fidelidad["sigma"] = "partial" if sigma_partial else "full"
    return {"vector": proy_vector, "sigma": proy_sigma,
            "fidelidad": fidelidad, "perdidas": perdidas}


def _fmt_vector(vector: list, sigma: list) -> str:
    return ("[" + ",".join(str(v) for v in vector) + "] sigma ["
            + ",".join(str(v) for v in sigma) + "]")


def construir_sello(art: Artefacto, target: str, hash_hex: str,
                    proy: dict, perdidas_extra: list | None = None) -> str:
    """El sello proof-carrying inline (contrato §6.3). Sin timestamps."""
    perdidas = list(proy["perdidas"]) + list(perdidas_extra or [])
    fid = proy["fidelidad"]
    lineas = [
        "<!-- kora:sello",
        f"fuente: {art.urn}",
        f"version: {art.campos.get('version')}",
        f"hash-fuente: sha256:{hash_hex}",
        f"target: {target}",
        f"funtor: T-{target}-pneuma-v1",
        f"vector-fuente: {_fmt_vector(art.campos['vector'], art.campos['sigma'])}",
        f"vector-proyectado: {_fmt_vector(proy['vector'], proy['sigma'])}",
        "fidelidad: " + " ".join(
            f"{eje}:{fid[eje]}" for eje in EJES + ("sigma",)),
    ]
    if perdidas:
        lineas.append("perdidas:")
        for etiqueta, a, b, razon in perdidas:
            lineas.append(f"  {etiqueta}: {a}->{b} :: {razon}")
    lineas += [
        "preservado-por-construccion: composicion, identidad, monotonia-pi, "
        "monotonia-mu, monotonia-xi",
        "declarado-no-mecanizado: naturalidad-xi, cierre-safety, "
        "composicion-kleisli",
        "-->",
    ]
    return "\n".join(lineas)


def _fm_str(valor: str) -> str:
    """Serializa un valor de frontmatter emitido, entre comillas dobles."""
    return '"' + str(valor).replace('"', "'") + '"'


def _componer(frontmatter: list[str], cuerpo: str, extra: str,
              sello: str) -> str:
    partes = ["---"] + frontmatter + ["---", "", cuerpo.strip("\n")]
    if extra:
        partes += ["", extra]
    partes += ["", sello, ""]
    return "\n".join(partes)


def emitir(art: Artefacto, target: str, proy: dict,
           hash_hex: str) -> tuple[str, str, list]:
    """Construye la emisión: (path relativo bajo _emision, contenido, extra).

    Devuelve también las pérdidas extra (colapso de forma), ya selladas.
    """
    nombre = art.campos["nombre"]
    descripcion = art.campos.get("descripcion", "")
    herramientas = art.campos.get("herramientas") or []
    perdidas_extra: list = []
    extra = ""
    if art.tipo == "skill":
        fm = [f"name: {nombre}", f"description: {_fm_str(descripcion)}"]
        if target == "claude-code" and herramientas:
            fm.append("allowed-tools: " + ", ".join(herramientas))
        rel = f"{target}/skills/{nombre}/SKILL.md"
    elif target == "codex":
        # Codex no registra agentes: el agente se emite COMO skill.
        perdidas_extra.append(("forma", "agente", "habilidad",
                               "codex no registra agentes"))
        fm = [f"name: {nombre}", f"description: {_fm_str(descripcion)}"]
        rel = f"{target}/skills/{nombre}/SKILL.md"
    elif target == "claude-code":
        fm = [f"name: {nombre}", f"description: {_fm_str(descripcion)}"]
        if herramientas:
            fm.append("tools: " + ", ".join(herramientas))
        if art.campos.get("arnes") == "persona":
            extra = DOCTRINA_DUAL_MODE
        rel = f"{target}/agents/{nombre}.md"
    else:  # opencode, agente
        modo = "subagent" if art.campos.get("forma") == "subagente" \
            else "primary"
        fm = [f"description: {_fm_str(descripcion)}", f"mode: {modo}"]
        rel = f"{target}/agents/{nombre}.md"
    sello = construir_sello(art, target, hash_hex, proy, perdidas_extra)
    return rel, _componer(fm, art.cuerpo, extra, sello), perdidas_extra


def _copiar_referencias(art: Artefacto, destino_dir: Path) -> Path | None:
    """Copia la fibra referencias/ junto a la emisión, conservando su nombre.

    El cuerpo emitido cita paths `referencias/...`; renombrar el directorio
    rompería todos los enlaces, y ningún target exige otro nombre.
    """
    origen = art.path.parent / "referencias"
    if art.tipo == "skill" and origen.is_dir():
        destino = destino_dir / "referencias"
        if destino.exists():
            shutil.rmtree(destino)
        shutil.copytree(origen, destino)
        return destino
    return None


RUTAS_APLICAR = {
    ("claude-code", "skill"): "~/.claude/skills/{nombre}",
    ("claude-code", "agente"): "~/.claude/agents/{nombre}.md",
    ("codex", "skill"): "~/.codex/skills/{nombre}",
    ("codex", "agente"): "~/.codex/skills/{nombre}",
    ("opencode", "skill"): "~/.config/opencode/skills/{nombre}",
    ("opencode", "agente"): "~/.config/opencode/agents/{nombre}.md",
}


def cmd_transmutar(raiz: Path, urn: str, target: str, aplicar: bool,
                   a_stdout: bool) -> int:
    arts = cargar_corpus(raiz)
    art = resolver(arts, urn)
    if art is None:
        print(f"error: el URN '{urn}' no resuelve en el censo.",
              file=sys.stderr)
        return 1
    if target not in TARGETS_REALIZADOS:
        print(f"error: el target '{target}' es reconocido por la ley pero no "
              f"está realizado en esta encarnación; GENESIS.md declara esa "
              f"deuda. Realizados: {', '.join(TARGETS_REALIZADOS)}.",
              file=sys.stderr)
        return 1
    if art.tipo == "conocimiento":
        print("error: el conocimiento no se transmuta — se consume como "
              "contexto. Solo agentes y skills se proyectan.",
              file=sys.stderr)
        return 1
    vector, sigma = art.vector_valido(), art.sigma_valido()
    if art.tipo is None or vector is None or sigma is None or \
            not isinstance(art.campos.get("nombre"), str):
        print(f"error: '{urn}' no tiene un frontmatter agéntico íntegro "
              f"(vector/sigma/nombre); corre `velar` y corrige antes de "
              f"transmutar.", file=sys.stderr)
        return 1
    # Los espacios de emisión por runtime son planos: dos artefactos con el
    # mismo nombre se pisarían en silencio. Colisión = error, no sobrescritura.
    nombre = art.campos["nombre"]
    for otro in arts:
        if otro.urn and otro.urn != urn and \
                otro.tipo in ("skill", "agente") and \
                otro.campos.get("nombre") == nombre:
            print(f"error: colisión de nombre '{nombre}' entre {urn} y "
                  f"{otro.urn}: los espacios de emisión por runtime son "
                  f"planos; renombra uno.", file=sys.stderr)
            return 1
    # Transmutar vela su fuente: los mismos checks ontológicos de `velar`,
    # restringidos al artefacto fuente. Una fuente incoherente no se proyecta.
    fallos_fuente = []
    for cid in ("vector-en-reticulo", "leyes-inter-eje", "dominio-forma",
                "arnes-compatible"):
        fallos_fuente += [(cid, m) for p, m in FUNCIONES_CHECK[cid](arts, raiz)
                          if p == art.rel]
    if fallos_fuente:
        for cid, m in fallos_fuente:
            print(f"error: la fuente no pasa velar: [{cid}] :: {m}; "
                  f"transmutar exige fuente coherente.", file=sys.stderr)
        return 1
    try:
        proy = proyectar(vector, sigma, target)
    except ErrorTransmutacion as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    hash_hex = hashlib.sha256(art.path.read_bytes()).hexdigest()
    rel, contenido, _ = emitir(art, target, proy, hash_hex)
    if a_stdout:
        sys.stdout.write(contenido)
        return 0
    destino = raiz / "_emision" / rel
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(contenido, encoding="utf-8")
    print(f"emitido: _emision/{rel}")
    refs = _copiar_referencias(art, destino.parent)
    if refs:
        print(f"emitido: {refs.relative_to(raiz).as_posix()}/ "
              f"(copia de referencias/)")
    for etiqueta, a, b, razon in proy["perdidas"]:
        print(f"pérdida declarada: {etiqueta}: {a}->{b} :: {razon}")
    if art.tipo == "agente" and target == "codex":
        print("pérdida declarada: forma: agente->habilidad :: codex no "
              "registra agentes")
    if aplicar:
        plantilla = RUTAS_APLICAR[(target, art.tipo)]
        ruta = Path(plantilla.format(nombre=art.campos["nombre"])).expanduser()
        if art.tipo == "skill" or (art.tipo, target) == ("agente", "codex"):
            ruta.mkdir(parents=True, exist_ok=True)
            (ruta / "SKILL.md").write_text(contenido, encoding="utf-8")
            _copiar_referencias(art, ruta)
        else:
            ruta.parent.mkdir(parents=True, exist_ok=True)
            ruta.write_text(contenido, encoding="utf-8")
        print(f"aplicado: {ruta}")
    return 0


# ------------------------------------------------------------- ciclo (§5)

# Línea `estado:` del frontmatter: valor + comentario inline opcional +
# terminador original. La reescritura solo toca el grupo del valor.
RE_LINEA_ESTADO = re.compile(
    r"^(estado:[ \t]+)([^#\r\n]*?)([ \t]*(?:#[^\r\n]*)?)(\r\n|\n|\r|)$")


def cmd_ciclo(raiz: Path, urn: str, nuevo: str) -> int:
    arts = cargar_corpus(raiz)
    art = resolver(arts, urn)
    if art is None:
        print(f"error: el URN '{urn}' no resuelve en el censo.",
              file=sys.stderr)
        return 1
    cadena = art.cadena_estados
    actual = art.campos.get("estado")
    if nuevo not in cadena:
        print(f"error: '{nuevo}' no es un estado de la cadena del tipo "
              f"{art.tipo}: {' -> '.join(cadena)}.", file=sys.stderr)
        return 1
    if actual not in cadena:
        print(f"error: el estado actual '{actual}' no pertenece a la cadena "
              f"del tipo {art.tipo}; corrige el artefacto antes de ciclar.",
              file=sys.stderr)
        return 1
    if cadena.index(nuevo) <= cadena.index(actual):
        print(f"error: transición inválida {actual} -> {nuevo}: el ciclo "
              f"solo avanza ({' -> '.join(cadena)}); lo retirado no se "
              f"reactiva — se emite artefacto nuevo con 'reemplaza'.",
              file=sys.stderr)
        return 1
    # Gate de promoción: nadie asciende a publicado/activo sin pasar velar.
    # Las transiciones hacia deprecado/retirado no exigen gate.
    if nuevo in ("publicado", "activo"):
        resultados = velar_todo(raiz)
        fallos_art = [(cid, m) for cid, fs in resultados.items()
                      for p, m in fs if p == art.rel]
        if fallos_art:
            for cid, m in fallos_art:
                print(f"error: promoción rechazada: el artefacto no pasa "
                      f"velar: [{cid}] :: {m}.", file=sys.stderr)
            return 1
    # Reescritura quirúrgica: solo cambia el valor del campo estado; el
    # terminador de línea original (LF/CRLF) y cualquier comentario inline
    # sobreviven, y el resto del archivo queda byte-idéntico.
    crudo = art.path.read_bytes().decode("utf-8")
    lineas = crudo.splitlines(keepends=True)
    cierre = None
    for i in range(1, len(lineas)):
        if lineas[i].strip() == "---":
            cierre = i
            break
    cambiado = False
    for i in range(1, cierre or 0):
        m = RE_LINEA_ESTADO.match(lineas[i])
        if m:
            lineas[i] = f"{m.group(1)}{nuevo}{m.group(3)}{m.group(4)}"
            cambiado = True
            break
    if not cambiado:
        print("error: no se encontró la línea 'estado:' en el frontmatter.",
              file=sys.stderr)
        return 1
    art.path.write_bytes("".join(lineas).encode("utf-8"))
    print(f"ciclo: {urn} {actual} -> {nuevo}")
    return 0


# --------------------------------------------------------------- ley

PIEZAS_LEY = ("ALMA.md", "ley/0-constitucion.md", "ley/1-ontologia.md",
              "ley/2-forma.md", "ley/3-transmutacion.md",
              "ley/4-koraficacion.md")


def cmd_ley(raiz: Path) -> int:
    rutas = [raiz / pieza for pieza in PIEZAS_LEY]
    faltan = [p for p, ruta in zip(PIEZAS_LEY, rutas) if not ruta.is_file()]
    if faltan:
        print("error: la ley no está completa en esta encarnación; faltan: "
              + ", ".join(faltan) + ".", file=sys.stderr)
        return 1
    borde = "=" * 70
    for pieza, ruta in zip(PIEZAS_LEY, rutas):
        print(borde)
        print(f"==  {pieza}")
        print(borde)
        print(ruta.read_text(encoding="utf-8").rstrip("\n"))
        print()
    return 0


# --------------------------------------------------------------- CLI

def cmd_censo(raiz: Path, como_json: bool, escribir: bool) -> int:
    entradas = construir_censo(cargar_corpus(raiz))
    salida = censo_json(entradas)
    if escribir:
        (raiz / "censo.json").write_text(salida, encoding="utf-8")
        print(f"censo.json escrito ({len(entradas)} artefactos). Recuerda: "
              "es vista derivada, jamás autoridad.")
        return 0
    if como_json:
        sys.stdout.write(salida)
        return 0
    if not entradas:
        print("censo: 0 artefactos (no existe artefactos/ o está vacío).")
        return 0
    for e in entradas:
        print(f"{e['urn'] or '(sin urn)'}  [{e['tipo']}]  "
              f"v{e['version'] or '?'}  {e['estado'] or '?'}  {e['path']}")
    print(f"censo: {len(entradas)} artefactos.")
    return 0


def cmd_nombre(raiz: Path, urn: str) -> int:
    art = resolver(cargar_corpus(raiz), urn)
    if art is None:
        print(f"error: el URN '{urn}' no resuelve en el censo.",
              file=sys.stderr)
        return 1
    estado = art.campos.get("estado", "?")
    marca = f"  [{estado}: el URN de lo muerto sigue resolviendo]" \
        if estado in ("deprecado", "retirado") else ""
    print(f"urn: {urn}")
    print(f"path: {art.rel}")
    print(f"tipo: {art.tipo}")
    print(f"version: {art.campos.get('version', '?')}")
    print(f"estado: {estado}{marca}")
    return 0


def cmd_velar(raiz: Path, estricto: bool) -> int:
    resultados = velar_todo(raiz, estricto)
    total = 0
    for cid, fallos in resultados.items():
        if fallos:
            print(f"== {cid}: {len(fallos)} fallo(s)")
            for path, msg in fallos:
                print(f"[{cid}] {path} :: {msg}")
            total += len(fallos)
        else:
            print(f"== {cid}: ok")
    if total:
        print(f"velar: {total} fallo(s) en {len(resultados)} checks.")
        return 1
    print(f"velar: todo coherente ({len(resultados)} checks).")
    return 0


def principal(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="kora.py",
        description="KORA pneuma — censo, nombre, velar, transmutar, "
                    "ciclo, ley.")
    sub = parser.add_subparsers(dest="gesto", required=True)

    p = sub.add_parser("censo", help="catálogo derivado del filesystem")
    p.add_argument("--json", action="store_true", help="emite JSON")
    p.add_argument("--escribir", action="store_true",
                   help="guarda censo.json (derivado, gitignored)")

    p = sub.add_parser("nombre", help="resuelve un URN a su nombre verdadero")
    p.add_argument("urn")

    p = sub.add_parser("velar", help="corre todos los checks de coherencia")
    p.add_argument("--estricto", action="store_true",
                   help="añade publicacion-digna")

    p = sub.add_parser("transmutar", help="proyección funtorial a un runtime")
    p.add_argument("--urn", required=True)
    p.add_argument("--target", required=True, choices=list(TARGETS_CONOCIDOS))
    p.add_argument("--aplicar", action="store_true",
                   help="instala en los paths del runtime")
    p.add_argument("--stdout", action="store_true",
                   help="imprime la emisión en vez de escribirla")

    p = sub.add_parser("ciclo", help="transición de lifecycle (solo adelante)")
    p.add_argument("urn")
    p.add_argument("estado")

    sub.add_parser("ley", help="concatena ALMA.md + ley/0..4")

    args = parser.parse_args(argv)
    raiz = raiz_corpus()
    if args.gesto == "censo":
        return cmd_censo(raiz, args.json, args.escribir)
    if args.gesto == "nombre":
        return cmd_nombre(raiz, args.urn)
    if args.gesto == "velar":
        return cmd_velar(raiz, args.estricto)
    if args.gesto == "transmutar":
        return cmd_transmutar(raiz, args.urn, args.target, args.aplicar,
                              args.stdout)
    if args.gesto == "ciclo":
        return cmd_ciclo(raiz, args.urn, args.estado)
    if args.gesto == "ley":
        return cmd_ley(raiz)
    parser.error("gesto desconocido")
    return 2


if __name__ == "__main__":
    try:
        codigo = principal()
        sys.stdout.flush()
    except BrokenPipeError:
        # Pipe cerrado aguas abajo (p.ej. `kora.py ley | head`): salida
        # limpia, sin traceback. Se redirige stdout a /dev/null para que el
        # flush del intérprete al salir no vuelva a reventar.
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        codigo = 0
    sys.exit(codigo)
