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
import stat
import tomllib
from pathlib import Path

# ------------------------------------------------------------------ constantes

TARGETS_CONOCIDOS = ("claude-code", "codex", "opencode", "openclaw", "hermes")
TARGETS_REALIZADOS = ("claude-code", "codex", "opencode", "openclaw")
TARGET_PRINCIPAL = "codex"

# Arneses que portan U_phen (ley/2 §10 r5): su personalidad se segrega a SOUL.md
# en los targets que separan voz de operativa (openclaw, ley/3 §7.1).
ARNESES_CON_UPHEN = ("persona", "orquestador", "servicio")

ESTADOS_CONOCIMIENTO = ("borrador", "publicado", "deprecado")
ESTADOS_AGENTICO = ("borrador", "activo", "deprecado", "retirado")

FORMAS = ("habilidad", "subagente", "agente", "plataforma")
ARNESES = ("utilidad", "disciplina", "delegado", "persona",
           "orquestador", "servicio", "arquetipo")
FAMILIAS = ("nota", "fuente", "bok")
# Alcance de instalación (opcional; ausente = "ambos"). Gobierna qué destinos de
# --aplicar admite el artefacto: usuario-general, proyecto (.opencode/.claude) o
# ambos. El gesto `transmutar --aplicar [--proyecto]` lo respeta y valida.
ALCANCES = ("usuario", "proyecto", "ambos")
LANGS = ("es", "en")

EJES = ("pi", "mu", "xi", "lambda", "phi")
RANGO_EJE = {"pi": 3, "mu": 3, "xi": 4, "lambda": 3, "phi": 4}  # máximo; mínimo 0
SIGMA_NOMBRES = ("safety", "fairness", "transparency",
                 "accountability", "sustainability")

# Dominio de proyección por forma; fuente normativa: ley/2-forma.md.
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

# Compatibilidad arnés × forma; fuente normativa: ley/2-forma.md.
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
RE_NOMBRE_RUTA = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def _nombre_ruta_seguro(nombre: str) -> bool:
    return RE_NOMBRE_RUTA.fullmatch(nombre) is not None


CAMPOS_COMUNES = {
    "urn", "nombre", "version", "estado", "descripcion", "fuente",
    "autor", "creado", "lang", "tags", "cita", "depende", "reemplaza", "refina",
}
CAMPOS_AGENTICOS = {
    "vector", "sigma", "arnes", "forma", "herramientas", "targets",
    "conocimiento", "componible", "estados", "alcance",
}
CAMPOS_CONOCIMIENTO = {"familia"}

CAMPOS_OBLIGATORIOS_COMUNES = ("urn", "nombre", "version", "estado",
                               "descripcion", "fuente")
CAMPOS_OBLIGATORIOS_AGENTICOS = ("vector", "sigma", "arnes", "forma",
                                 "herramientas")
CAMPOS_LISTA = ("tags", "cita", "depende", "reemplaza", "refina",
                "herramientas", "targets", "conocimiento", "componible",
                "estados", "vector", "sigma")
CAMPOS_RELACION = ("cita", "depende", "reemplaza", "refina")

CHECKS = ("forma-valida", "nombre-verdadero", "lugar-coincide",
          "vector-en-reticulo", "leyes-inter-eje", "dominio-forma",
          "arnes-compatible", "estado-valido", "referencias-resuelven",
          "relaciones-legales", "targets-conocidos")
CHECKS_ESTRICTOS = ("publicacion-digna", "sello-fresco")


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


class ErrorResolucion(Exception):
    """Un URN no identifica unívocamente una fuente del corpus."""


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

    Gramática de artefacto: subconjunto regular de YAML. Sin anidamiento,
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
    coincidencias = [art for art in arts if art.urn == urn]
    if len(coincidencias) > 1:
        rutas = ", ".join(art.rel for art in coincidencias)
        raise ErrorResolucion(
            f"URN ambiguo '{urn}': resuelve a {len(coincidencias)} fuentes: "
            f"{rutas}. Corrige el duplicado antes de operar")
    return coincidencias[0] if coincidencias else None


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
        nombre = art.campos.get("nombre")
        if isinstance(nombre, str) and not _nombre_ruta_seguro(nombre):
            f(art, "nombre inseguro para una ruta: debe ser un slug "
              "minúsculo con segmentos alfanuméricos separados por guiones")
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
            if familia is not None and familia not in FAMILIAS:
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
            alcance = art.campos.get("alcance")
            if isinstance(alcance, str) and alcance not in ALCANCES:
                f(art, f"alcance inválido: '{alcance}' "
                       f"(esperado: {'|'.join(ALCANCES)})")
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


def _mapa_archivos(raiz: Path) -> dict[str, bytes]:
    """Mapa relativo→bytes de una fibra; los directorios vacíos no son materia."""
    if not raiz.is_dir():
        return {}
    return {
        p.relative_to(raiz).as_posix(): p.read_bytes()
        for p in sorted(raiz.rglob("*")) if p.is_file()
    }


def _tipo_nodo(path: Path) -> str | None:
    """Tipo POSIX sin seguir enlaces; `None` significa ausencia real."""
    try:
        modo = path.lstat().st_mode
    except FileNotFoundError:
        return None
    if stat.S_ISLNK(modo):
        return "enlace simbólico"
    if stat.S_ISDIR(modo):
        return "directorio"
    if stat.S_ISREG(modo):
        return "archivo regular"
    return "nodo especial"


def _inventario_nodos(raiz: Path) -> dict[str, str]:
    """Inventario relativo→tipo sin seguir enlaces ni leer contenido."""
    inventario: dict[str, str] = {}
    pendientes = [(raiz, Path())]
    while pendientes:
        actual, prefijo = pendientes.pop()
        with os.scandir(actual) as entradas:
            ordenadas = sorted(entradas, key=lambda entrada: entrada.name)
        for entrada in ordenadas:
            rel = prefijo / entrada.name
            path = Path(entrada.path)
            tipo = _tipo_nodo(path)
            if tipo is None:
                continue
            inventario[rel.as_posix()] = tipo
            if tipo == "directorio":
                pendientes.append((path, rel))
    return inventario


def _campos_ultimo_sello(path: Path) -> dict[str, str]:
    """Campos escalares del último sello de un archivo regular real."""
    try:
        tipo = _tipo_nodo(path)
    except OSError:
        return {}
    if tipo != "archivo regular":
        return {}
    try:
        texto = path.read_text(encoding="utf-8")
        if path.suffix == ".toml":
            texto = tomllib.loads(texto).get("developer_instructions", "")
        if not isinstance(texto, str):
            return {}
        sellos = list(RE_SELLO.finditer(texto))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError,
            AttributeError):
        return {}
    if not sellos:
        return {}
    return dict(
        linea.split(": ", 1) for linea in sellos[-1].group(1).split("\n")
        if ": " in linea and not linea.startswith(" ")
    )


def _sello_atribuye(path: Path, urn: str, target: str) -> bool:
    """Verdadero si el último sello atribuye el factor a ese par KORA."""
    lineas = _campos_ultimo_sello(path)
    return lineas.get("fuente") == urn and lineas.get("target") == target


def chk_sello_fresco(arts, raiz):
    fallos = []
    emision = raiz / "_emision"
    try:
        tipo_emision = _tipo_nodo(emision)
    except OSError:
        return [("_emision", "emisión ilegible; no se recorrió")]
    if tipo_emision is None:
        return fallos
    if tipo_emision != "directorio":
        return [("_emision", f"emisión es {tipo_emision}; no se recorrió")]
    try:
        inventario = _inventario_nodos(emision)
    except OSError:
        return [("_emision", "emisión ilegible; no se recorrió")]
    irregulares = [
        (rel, tipo) for rel, tipo in inventario.items()
        if tipo not in ("directorio", "archivo regular")
    ]
    if irregulares:
        return [
            (f"_emision/{rel}",
             f"emisión contiene {tipo}; no se siguió")
            for rel, tipo in irregulares
        ]
    por_urn = {a.urn: a for a in arts if a.urn}
    emitidos: list[Path] = []
    for target_dir in sorted(p for p in emision.iterdir() if p.is_dir()):
        skills = target_dir / "skills"
        if skills.is_dir():
            emitidos.extend(sorted(skills.glob("*/SKILL.md")))
        agents = target_dir / "agents"
        if agents.is_dir():
            emitidos.extend(sorted(agents.glob("*.md")))
            emitidos.extend(sorted(agents.glob("*.toml")))
        # openclaw: el agente es un workspace; AGENTS.md y SOUL.md portan sello.
        workspaces = target_dir / "workspaces"
        if workspaces.is_dir():
            emitidos.extend(sorted(workspaces.glob("*/AGENTS.md")))
            emitidos.extend(sorted(workspaces.glob("*/SOUL.md")))
    pares: dict[tuple[str, str], dict] = {}
    for path in emitidos:
        rel = path.relative_to(raiz).as_posix()
        crudo = path.read_text(encoding="utf-8")
        texto = crudo
        if path.suffix == ".toml":
            try:
                datos = tomllib.loads(crudo)
                texto = datos.get("developer_instructions", "")
            except (tomllib.TOMLDecodeError, AttributeError):
                fallos.append((rel, "emisión TOML inválida"))
                continue
            if not isinstance(texto, str):
                fallos.append((rel, "emisión TOML inválida"))
                continue
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
        target_ruta = path.relative_to(emision).parts[0]
        target_sello = lineas.get("target", "")
        fuente = por_urn.get(urn)
        if fuente is None:
            fallos.append((rel, f"la fuente del sello no resuelve: '{urn}'"))
            continue
        info = pares.setdefault(
            (urn, target_ruta),
            {"fuente": fuente, "paths": [], "regenerable": True},
        )
        info["paths"].append(path)
        if target_sello != target_ruta:
            fallos.append((rel, f"target del sello '{target_sello}' no coincide "
                           f"con la ruta de emisión '{target_ruta}'"))
            info["regenerable"] = False
        targets_fuente = fuente.campos.get("targets")
        if targets_fuente is not None and (
                not isinstance(targets_fuente, list)
                or target_ruta not in targets_fuente):
            fallos.append((rel, f"target de emisión '{target_ruta}' no "
                           "declarado por la fuente"))
            info["regenerable"] = False
        actual = "sha256:" + hashlib.sha256(
            fuente.path.read_bytes()).hexdigest()
        if hash_decl != actual:
            fallos.append((rel, "emisión rancia, re-transmutar (hash-fuente "
                           "no coincide con la fuente actual)"))
            info["regenerable"] = False

    # El hash prueba identidad de la fuente principal, no identidad del
    # generador. Regenerar en memoria cierra ese segundo diagrama y cubre el
    # producto completo: factores doctrinales, sidecars y fibra referencias/.
    for (urn, target), info in sorted(pares.items()):
        if not info["regenerable"]:
            continue
        fuente = info["fuente"]
        if target not in TARGETS_REALIZADOS:
            rel = info["paths"][0].relative_to(raiz).as_posix()
            fallos.append((rel, f"emisión residual para target no realizado: "
                           f"'{target}'; retirar o realizar el target"))
            continue
        vector, sigma = fuente.vector_valido(), fuente.sigma_valido()
        if vector is None or sigma is None:
            continue  # los checks propietarios reportan la fuente inválida
        try:
            proy = proyectar(vector, sigma, target)
            hash_hex = hashlib.sha256(fuente.path.read_bytes()).hexdigest()
            archivos, _ = emitir(fuente, target, proy, hash_hex)
        except (ErrorTransmutacion, KeyError, TypeError) as exc:
            rel = info["paths"][0].relative_to(raiz).as_posix()
            fallos.append((rel, f"emisión no regenerable con el generador "
                           f"vigente: {exc}"))
            continue

        esperados = {rel: contenido.encode("utf-8")
                     for rel, contenido in archivos}
        for rel_esperado, bytes_esperados in sorted(esperados.items()):
            path = emision / rel_esperado
            rel = path.relative_to(raiz).as_posix()
            if not path.is_file():
                fallos.append((rel, "factor de emisión ausente; re-transmutar"))
            elif path.read_bytes() != bytes_esperados:
                fallos.append((rel, "emisión no coincide con el generador "
                               "vigente; re-transmutar"))
        # El par es dueño de todas las formas homónimas del espacio plano. Así
        # también se ven sidecars extra y formas residuales sin sello propio.
        nombre = fuente.campos["nombre"]
        observados = set(info["paths"])
        for sufijo in (".md", ".toml"):
            candidato = emision / target / "agents" / f"{nombre}{sufijo}"
            if candidato.is_file():
                observados.add(candidato)
        for directorio in (
            emision / target / "skills" / nombre,
            emision / target / "workspaces" / nombre,
        ):
            if not directorio.is_dir():
                continue
            for path in directorio.rglob("*"):
                if not path.is_file():
                    continue
                relativo = path.relative_to(directorio)
                if fuente.tipo == "skill" and \
                        directorio.parent.name == "skills" and \
                        relativo.parts[0] == "referencias":
                    continue  # se compara como fibra, con diagnóstico propio
                observados.add(path)
        for path in sorted(observados):
            rel_producto = path.relative_to(emision).as_posix()
            if rel_producto not in esperados:
                fallos.append((path.relative_to(raiz).as_posix(),
                               "factor obsoleto para el generador vigente; "
                               "re-transmutar"))

        if fuente.tipo == "skill":
            origen_refs = fuente.path.parent / "referencias"
            destino_refs = (emision / target / "skills" /
                            fuente.campos["nombre"] / "referencias")
            refs_fuente = _mapa_archivos(origen_refs)
            refs_emision = _mapa_archivos(destino_refs)
            if refs_fuente != refs_emision:
                faltan = sorted(refs_fuente.keys() - refs_emision.keys())
                sobran = sorted(refs_emision.keys() - refs_fuente.keys())
                cambian = sorted(k for k in refs_fuente.keys() & refs_emision.keys()
                                 if refs_fuente[k] != refs_emision[k])
                detalle = []
                if faltan:
                    detalle.append("faltan " + ", ".join(faltan))
                if sobran:
                    detalle.append("sobran " + ", ".join(sobran))
                if cambian:
                    detalle.append("difieren " + ", ".join(cambian))
                rel = (destino_refs.relative_to(raiz).as_posix() + "/")
                fallos.append((rel, "fibra referencias/ no coincide con la "
                               "fuente; re-transmutar (" + "; ".join(detalle)
                               + ")"))
    return fallos


def _fallos_publicacion_art(art, estado=None):
    """Exigencias de dignidad para un artefacto en el estado indicado.

    `estado` permite que `ciclo` evalúe el estado destino antes de escribirlo.
    """
    fallos = []
    if art.error_parse or art.tipo is None:
        return fallos
    estado = art.campos.get("estado") if estado is None else estado
    if estado in ("activo", "publicado"):
        for campo in ("descripcion", "fuente"):
            v = art.campos.get(campo)
            if not isinstance(v, str) or not v.strip():
                fallos.append((art.rel, f"artefacto {estado} exige "
                               f"'{campo}' no vacío"))
    return fallos


def chk_publicacion_digna(arts, raiz):
    fallos = []
    for art in arts:
        fallos.extend(_fallos_publicacion_art(art))
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
    "publicacion-digna": chk_publicacion_digna,
    "sello-fresco": chk_sello_fresco,
}


def velar_todo(raiz: Path, estricto: bool = False) -> dict[str, list]:
    """Corre todos los checks. Devuelve {check_id: [(path, mensaje), ...]}."""
    arts = cargar_corpus(raiz)
    ids = list(CHECKS)
    if estricto:
        ids.extend(CHECKS_ESTRICTOS)
    return {cid: FUNCIONES_CHECK[cid](arts, raiz) for cid in ids}


# ------------------------------------------------------- transmutación (§6)

def _m(filas):
    """Construye la matriz de un eje: {valor: (proyectado, fidelidad, razón)}."""
    return dict(filas)


# Matrices de preservación; fuente normativa: ley/3-transmutacion.md.
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
    # openclaw: el techo más alto de los cinco targets (ley/3 §4.4). Meta-runtime
    # ACP + systemd always-on. Único con mu=3 y xi=4 full; único que proyecta
    # lambda=3 (partial). Fiel a la runtime-extension openclaw de la bestia y
    # confirmada contra el openclaw real (~/openclaw-fleet/, docs.openclaw.ai).
    "openclaw": {
        "pi": _m({0: (0, "full", None), 1: (1, "full", None),
                  2: (2, "full", None),
                  3: (3, "full", None)}),  # delegación jerárquica vía ACP
        "mu": _m({0: (0, "full", None), 1: (1, "full", None),
                  2: (2, "full", None),
                  3: (3, "full", None)}),  # always-on systemd + Telegram
        "xi": _m({0: (0, "full", None), 1: (1, "full", None),
                  2: (2, "full", None), 3: (3, "full", None),
                  4: (4, "full", None)}),  # delegación jerárquica vía ACP
        "lambda": _m({0: (0, "full", None), 1: (1, "full", None),
                      2: (2, "full", None),
                      3: (3, "partial", "society-in-the-loop requiere "
                          "gobernanza externa no modelada en runtime")}),
        "phi": _m({0: (0, "full", None), 1: (1, "full", None),
                   2: (2, "full", None),
                   3: (3, "partial", "cognición híbrida parcial, no HAJCS "
                       "completo"),
                   4: (None, "none", "co-evolutivo no modelado")}),
        "sigma-max": [3, 3, 3, 3, 2],
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
    "openclaw": {
        "safety": "hard_rules en AGENTS.md + approval gates + policy en gateway",
        "fairness": "declarativo + bias audits manuales; sin enforcement runtime",
        "transparency": "historial persistente + logs + audit trails por sesión",
        "accountability": "git log del fleet + logs por sesión + Telegram",
        "sustainability": "sustainability ambiental no medida; model routing + "
                          "budget tracking",
    },
}

# Quién sí soporta un eje que el target rechaza (para el mensaje de fallo).
# openclaw realizado desde ley/3 v1.3.0: sostiene mu=3 (full) y lambda=3 (partial).
QUIEN_SOPORTA = {
    ("mu", 3): "openclaw (transmutar --target openclaw)",
    ("lambda", 3): "openclaw (parcial; transmutar --target openclaw)",
    ("phi", 4): "ninguno de los runtimes reconocidos",
}

# Centinela canónico que delimita el span de U_phen en el cuerpo (ley/2 §10 r6).
# Predicado literal decidible: el núcleo NO segmenta prosa (forma-no-verdad);
# el autor marca el span y el emisor lo transporta a SOUL.md (openclaw, ley/3 §7.1).
SOUL_ABRE = "<!-- kora:soul -->"
SOUL_CIERRA = "<!-- kora:soul:fin -->"
RE_SOUL = re.compile(
    re.escape(SOUL_ABRE) + r"\n(.*?)\n" + re.escape(SOUL_CIERRA), re.DOTALL)

DOCTRINA_DUAL_MODE = """## Modos de invocacion

Este artefacto es dual-mode (arnés persona). Declara su modo efectivo:

- **Modo subagente (batch)**: invocado por otro agente mediante el mecanismo
  nativo de delegación del runtime. Opera con entrada/salida cerrada, sin
  diálogo HITL intra-tarea; entrega dictamen y handoff, no conversación.
- **Modo persona (encarnación)**: cargado como instrucciones del hilo
  principal. Dispone del diálogo HITL nativo, de las skills y de las
  herramientas de la sesión; es el único modo que realiza la fidelidad
  declarada en el sello."""


# Frontera de capacidad KORA -> opencode: el allowlist `herramientas` se traduce
# al idiom canonico de opencode `permission: <key>: deny` (el objeto `tools` esta
# deprecado desde opencode v1.1.1, doc oficial /docs/permissions). Solo se
# deniegan las tools de EFECTO EXTERNO que la fuente NO concede; las read-ish
# (read/edit/glob/grep) e internas (question/list/lsp) quedan en default para no
# romper la operacion. Pares (key KORA, key opencode).
OPENCODE_TOOLS_ELEVADAS = (("Bash", "bash"), ("WebFetch", "webfetch"),
                           ("WebSearch", "websearch"), ("Task", "task"))


class ErrorTransmutacion(Exception):
    """La transmutación no procede; el mensaje explica por qué."""


def proyectar(vector: list, sigma: list, target: str) -> dict:
    """Proyecta el vector por la matriz del target.

    Monotonía por construcción: cada eje y cada componente de sigma se proyecta a
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


# El contrato de conocimiento NO lista paths: el path se resuelve desde el
# censo vivo por URN. Con Bash, el consumidor usa el gesto `nombre`; con acceso
# de solo lectura, localiza la línea de frontmatter exacta y exige unicidad.
# Esto evita fingir que el id del URN coincide con `nombre` (ley/2 §6 sólo
# vincula el path a `nombre`). El ancla nombra la convención del repo central y
# su override de entorno, sin atarse a un CWD concreto.
ANCLA_CONTRATO = "~/kora-pneuma  (o $KORA_RAIZ)"
RESOLUCION_BASH_CONTRATO = (
    "  resolucion-bash: python3 {ancla}/kora.py nombre <URN>")
RESOLUCION_LECTURA_CONTRATO = (
    "  resolucion-lectura: Grep exacto '^urn: <URN>$' bajo "
    "{ancla}/artefactos; exigir coincidencia unica")


def _bloque_contrato(art: Artefacto) -> list[str]:
    """El contrato de conocimiento del sello: ancla + resolución por censo +
    los URN declarados, sin materializar paths (ley/3 §5 r6; cierra GENESIS §4).

    Proyecta `conocimiento` (kb a leer como contexto) y `componible` (otros
    artefactos declarados como componibles). Esa relación no prueba una
    composición de Kleisli. Devuelve [] si el artefacto
    no declara ninguno: un agéntico sin corpus no carga un bloque vacío, y la
    emisión queda byte-idéntica a la previa al contrato.
    """
    conocimiento = art.campos.get("conocimiento")
    componible = art.campos.get("componible")
    conocimiento = conocimiento if isinstance(conocimiento, list) else []
    componible = componible if isinstance(componible, list) else []
    if not conocimiento and not componible:
        return []
    lineas = [
        "contrato-conocimiento:",
        f"  ancla: {ANCLA_CONTRATO}",
        RESOLUCION_BASH_CONTRATO.format(ancla="{ancla}"),
        RESOLUCION_LECTURA_CONTRATO.format(ancla="{ancla}"),
    ]
    if conocimiento:
        lineas.append("  conocimiento: " + " ".join(conocimiento))
    if componible:
        lineas.append("  componible: " + " ".join(componible))
    return lineas


def construir_sello(art: Artefacto, target: str, hash_hex: str,
                    proy: dict, perdidas_extra: list | None = None) -> str:
    """Certificado inline de procedencia y congruencia (ley/3 §5)."""
    perdidas_extra = list(perdidas_extra or [])
    perdidas = list(proy["perdidas"]) + perdidas_extra
    fid = proy["fidelidad"]
    lineas = [
        "<!-- kora:sello",
        f"fuente: {art.urn}",
        f"version: {art.campos.get('version')}",
        f"hash-fuente: sha256:{hash_hex}",
        f"target: {target}",
        f"funtor: T-{target}-pneuma-v{'2' if target == 'codex' else '1'}",
        f"vector-fuente: {_fmt_vector(art.campos['vector'], art.campos['sigma'])}",
        f"vector-proyectado: {_fmt_vector(proy['vector'], proy['sigma'])}",
        "fidelidad: " + " ".join(
            f"{eje}:{fid[eje]}" for eje in EJES + ("sigma",)),
    ]
    if perdidas_extra:
        campos = dict.fromkeys(p[0] for p in perdidas_extra)
        lineas.append("fidelidad-campos: " + " ".join(
            f"{campo}:partial" for campo in campos))
    if perdidas:
        lineas.append("perdidas:")
        for etiqueta, a, b, razon in perdidas:
            lineas.append(f"  {etiqueta}: {a}->{b} :: {razon}")
    # Calificación mu=3 observable (ley/3 §7.1): para un agente con materia
    # ambiental always-on (mu=3), el emisor REALIZA el workspace conforme al
    # techo always-on (mu:3 full) y DIFIERE la conducta always-on
    # (daemon/gateway/systemd) al deploy del fleet.
    # En el portador del sello, no sólo en la ley: reconcilia el "openclaw no
    # realizado" inmutable de GENESIS con el realizado registrado en ley/3.
    if target == "openclaw" and art.campos.get("vector", [0, 0])[1] == 3:
        lineas += [
            "realiza: workspace-mu3-conforme (AGENTS.md+SOUL.md; techo "
            "always-on, sin recorte de min)",
            "difiere: conducta-always-on (gateway/systemd/openclaw.json) -> "
            "deploy del fleet",
        ]
    if target == "openclaw":
        herramientas = art.campos.get("herramientas") or []
        declaradas = ",".join(str(h) for h in herramientas)
        lineas += [
            f"frontera-herramientas-declarada: [{declaradas}]",
            "frontera-herramientas-realizacion: openclaw.json/deploy "
            "(fuera del funtor; no verificada por este sello)",
        ]
    # El contrato de conocimiento va ANTES de las dos líneas fijas (ley/3 §5
    # r6, cf. r4): nada se interpone jamás entre ellas y el cierre `-->`.
    lineas += _bloque_contrato(art)
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


def _componer_plano(cuerpo: str, sello: str) -> str:
    """Composición sin frontmatter: los workspace files de openclaw (AGENTS.md,
    SOUL.md) son markdown plano + sello. Byte-determinista, sin timestamps."""
    return "\n".join([cuerpo.strip("\n"), "", sello, ""])


def _componer_codex_agent(art: Artefacto, sello: str, extra: str) -> str:
    """Serializa un custom agent Codex como TOML determinista.

    `json.dumps` produce basic strings compatibles con TOML y evita inventar
    delimitadores que puedan colisionar con el Markdown transportado.
    """
    instrucciones = art.cuerpo.strip("\n")
    if extra:
        instrucciones += "\n\n" + extra
    instrucciones += "\n\n" + sello
    return "\n".join([
        "name = " + json.dumps(art.campos["nombre"], ensure_ascii=False),
        "description = " + json.dumps(
            art.campos.get("descripcion", ""), ensure_ascii=False),
        "developer_instructions = " + json.dumps(
            instrucciones, ensure_ascii=False),
        "",
    ])


def _emitir_codex(art: Artefacto, proy: dict,
                   hash_hex: str) -> tuple[list[tuple[str, str]], list]:
    """Codex v2: skills nativas y custom agents TOML.

    Las personas (`forma: agente`) conservan además una entrada explícita como
    skill para encarnación en el hilo principal. `openai.yaml` impide que ese
    modo persona sea invocado implícitamente por el runtime.
    """
    nombre = art.campos["nombre"]
    descripcion = art.campos.get("descripcion", "")
    herramientas = art.campos.get("herramientas") or []
    perdidas_extra: list = [(
        "herramientas",
        "allowlist[" + ",".join(str(h) for h in herramientas) + "]",
        "sin-allowlist-builtins-local",
        "Codex permite estrechar sandbox, MCP y skills por custom agent, pero "
        "no ofrece una allowlist exacta de herramientas built-in; las "
        "overrides vivas de la sesión padre prevalecen al delegar",
    )]
    sello = construir_sello(art, "codex", hash_hex, proy, perdidas_extra)
    if art.tipo == "skill":
        fm = [f"name: {nombre}", f"description: {_fm_str(descripcion)}"]
        archivos = [(f"codex/skills/{nombre}/SKILL.md",
                     _componer(fm, art.cuerpo, "", sello))]
        sidecar = art.path.parent / "agents/openai.yaml"
        try:
            tipo_sidecar = _tipo_nodo(sidecar)
        except OSError as exc:
            raise ErrorTransmutacion(
                f"sidecar Codex ilegible '{sidecar}': {exc}") from exc
        if tipo_sidecar is not None:
            if tipo_sidecar != "archivo regular":
                raise ErrorTransmutacion(
                    "agents/openai.yaml debe ser un archivo regular")
            try:
                contenido_sidecar = sidecar.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as exc:
                raise ErrorTransmutacion(
                    f"sidecar Codex ilegible '{sidecar}': {exc}") from exc
            archivos.append((
                f"codex/skills/{nombre}/agents/openai.yaml",
                contenido_sidecar,
            ))
        return archivos, perdidas_extra

    extra = DOCTRINA_DUAL_MODE if art.campos.get("forma") == "agente" else ""
    archivos = [(f"codex/agents/{nombre}.toml",
                 _componer_codex_agent(art, sello, extra))]
    if art.campos.get("forma") == "agente":
        fm = [f"name: {nombre}", f"description: {_fm_str(descripcion)}"]
        archivos.extend([
            (f"codex/skills/{nombre}/SKILL.md",
             _componer(fm, art.cuerpo, extra, sello)),
            (f"codex/skills/{nombre}/agents/openai.yaml",
             "policy:\n  allow_implicit_invocation: false\n"),
        ])
    return archivos, perdidas_extra


def _extraer_soul(cuerpo: str) -> tuple[str | None, str | None]:
    """Extrae el span de U_phen delimitado por el centinela kora:soul (ley/2
    §10 r6). Devuelve (span | None, error | None). Match literal, sin
    interpretar prosa (forma-no-verdad). A lo sumo un par balanceado."""
    matches = list(RE_SOUL.finditer(cuerpo))
    n_abre = cuerpo.count(SOUL_ABRE)
    n_cierra = cuerpo.count(SOUL_CIERRA)
    if n_abre == 0 and n_cierra == 0:
        return None, "ausente"
    if n_abre != 1 or n_cierra != 1 or len(matches) != 1:
        return None, ("desbalanceado o múltiple "
                      f"({n_abre} aperturas, {n_cierra} cierres)")
    return matches[0].group(1).strip("\n"), None


def _emitir_openclaw(art: Artefacto, proy: dict,
                     hash_hex: str) -> tuple[list[tuple[str, str]], list]:
    """openclaw: el objeto-runtime es un WORKSPACE multi-archivo name-keyed,
    no un archivo único (ley/3 §7.1). skill -> SKILL.md; agente -> workspace con
    AGENTS.md (cuerpo operativo sin el span de U_phen) + SOUL.md (ese span,
    sólo si el arnes lo porta; sale del centinela kora:soul, ley/2 §10 r6).
    El producto conserva la materia completa sin duplicar voz en operativa."""
    nombre = art.campos["nombre"]
    perdidas_extra: list = []
    sello = construir_sello(art, "openclaw", hash_hex, proy, perdidas_extra)
    if art.tipo == "skill":
        descripcion = art.campos.get("descripcion", "")
        fm = [f"name: {nombre}", f"description: {_fm_str(descripcion)}"]
        contenido = _componer(fm, art.cuerpo, "", sello)
        return [(f"openclaw/skills/{nombre}/SKILL.md", contenido)], perdidas_extra
    # agente / subagente / plataforma -> workspace
    arnes = art.campos.get("arnes")
    cuerpo_agents = art.cuerpo
    span = None
    if arnes in ARNESES_CON_UPHEN:
        span, err = _extraer_soul(art.cuerpo)
        if err:
            raise ErrorTransmutacion(
                f"el agente '{nombre}' (arnes '{arnes}', con U_phen) declara "
                f"target openclaw, que segrega SOUL.md (voz) de AGENTS.md "
                f"(operativa), pero su cuerpo no delimita U_phen con el "
                f"centinela {SOUL_ABRE} ... {SOUL_CIERRA} (centinela {err}). El "
                f"núcleo no segmenta prosa (forma-no-verdad): delimita el span "
                f"de U_phen en el cuerpo (ley/2 §10 r6; skill "
                f"autoria-de-persona) y reintenta. No se fabrica voz.")
        marca = RE_SOUL.search(art.cuerpo)
        antes = art.cuerpo[:marca.start()].rstrip("\n")
        despues = art.cuerpo[marca.end():].lstrip("\n")
        cuerpo_agents = "\n\n".join(p for p in (antes, despues) if p)
    archivos = [(f"openclaw/workspaces/{nombre}/AGENTS.md",
                 _componer_plano(cuerpo_agents, sello))]
    if span is not None:
        archivos.append((f"openclaw/workspaces/{nombre}/SOUL.md",
                         _componer_plano(span, sello)))
    return archivos, perdidas_extra


def emitir(art: Artefacto, target: str, proy: dict,
           hash_hex: str) -> tuple[list[tuple[str, str]], list]:
    """Construye la emisión: (lista de (path relativo bajo _emision, contenido),
    pérdidas extra ya selladas — colapso de forma).

    Casi todos los targets emiten UN archivo; openclaw emite un WORKSPACE
    (AGENTS.md [+ SOUL.md]). La lista uniforma ambos casos.
    """
    if target == "openclaw":
        return _emitir_openclaw(art, proy, hash_hex)
    if target == "codex":
        return _emitir_codex(art, proy, hash_hex)
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
    elif target == "claude-code":
        fm = [f"name: {nombre}", f"description: {_fm_str(descripcion)}"]
        if herramientas:
            fm.append("tools: " + ", ".join(herramientas))
        if art.campos.get("arnes") == "persona":
            extra = DOCTRINA_DUAL_MODE
        rel = f"{target}/agents/{nombre}.md"
    else:  # opencode, agente
        # forma subagente -> subagent; forma agente (persona dual-mode, ver
        # DOCTRINA_DUAL_MODE) -> all: usable como modo primario Y delegable como
        # subagente. 'all' es el default de opencode y preserva ambos modos;
        # 'primary' perderia la delegabilidad declarada en el sello.
        modo = "subagent" if art.campos.get("forma") == "subagente" \
            else "all"
        fm = [f"description: {_fm_str(descripcion)}", f"mode: {modo}"]
        # Frontera de capacidad: deniega via `permission` las tools elevadas
        # que `herramientas` no concede (paridad con el allowlist `tools` de
        # claude-code, en el idiom canonico de opencode).
        hset = set(herramientas)
        denegadas = [op for kt, op in OPENCODE_TOOLS_ELEVADAS if kt not in hset]
        if denegadas:
            fm.append("permission:")
            fm.extend(f"  {op}: deny" for op in denegadas)
        rel = f"{target}/agents/{nombre}.md"
    sello = construir_sello(art, target, hash_hex, proy, perdidas_extra)
    return [(rel, _componer(fm, art.cuerpo, extra, sello))], perdidas_extra


def _copiar_referencias(art: Artefacto, destino_dir: Path) -> Path | None:
    """Copia la fibra referencias/ junto a la emisión, conservando su nombre.

    El cuerpo emitido cita paths `referencias/...`; renombrar el directorio
    rompería todos los enlaces, y ningún target exige otro nombre.
    """
    if art.tipo != "skill":
        return None
    origen = art.path.parent / "referencias"
    destino = destino_dir / "referencias"
    if destino.exists():
        shutil.rmtree(destino)
    if origen.is_dir():
        shutil.copytree(origen, destino)
        return destino
    return None


def _limpiar_derivados_codex_v1(raiz: Path, art: Artefacto,
                                archivos: list[tuple[str, str]]) -> None:
    """Retira solo proyecciones Codex incompatibles del mismo nombre.

    El cambio v1→v2 deja un skill huérfano al reemitir un subagente como TOML;
    `_emision` es derivado, por lo que conservar ambas formas falsificaría la
    completitud. No toca instalaciones runtime ni nombres ajenos.
    """
    nombre = art.campos["nombre"]
    rels = {rel for rel, _ in archivos}
    skill = raiz / "_emision/codex/skills" / nombre
    agente = raiz / "_emision/codex/agents" / f"{nombre}.toml"
    if not any(rel.startswith(f"codex/skills/{nombre}/") for rel in rels) \
            and _tipo_nodo(skill) is not None:
        _retirar_ruta_gestionada(skill)
        print(f"retirado derivado huérfano: {skill.relative_to(raiz)}")
    if f"codex/agents/{nombre}.toml" not in rels \
            and _tipo_nodo(agente) is not None:
        _retirar_ruta_gestionada(agente)
        print(f"retirado derivado huérfano: {agente.relative_to(raiz)}")


def _retirar_ruta_gestionada(path: Path) -> None:
    """Retira solo la ruta de producto que KORA está reconciliando."""
    tipo = _tipo_nodo(path)
    if tipo == "directorio":
        shutil.rmtree(path)
    elif tipo is not None:
        path.unlink()


def _recrear_directorio_gestionado(path: Path) -> None:
    """Materializa un directorio cerrado sin conservar factores anteriores."""
    _retirar_ruta_gestionada(path)
    path.mkdir(parents=True)


def _conflicto_propiedad_skill(path: Path, urn: str,
                               target: str) -> str | None:
    """Rechaza adquirir por homonimia una ruta que KORA no puede atribuirse."""
    try:
        tipo = _tipo_nodo(path)
    except OSError:
        tipo = "nodo ilegible"
    if tipo is None:
        return None
    if tipo != "directorio" or not _sello_atribuye(
            path / "SKILL.md", urn, target):
        return (
            f"conflicto de propiedad en '{path}': la skill existente "
            f"no porta un sello atribuible a ({urn}, {target}); "
            "no se reemplazó"
        )
    return None


def _conflicto_propiedad_archivo(path: Path, urn: str,
                                 target: str) -> str | None:
    """Rechaza sobrescribir un factor file-based no atribuible a KORA."""
    try:
        tipo = _tipo_nodo(path)
    except OSError:
        tipo = "nodo ilegible"
    if tipo is None:
        return None
    if tipo != "archivo regular" or not _sello_atribuye(path, urn, target):
        return (
            f"conflicto de propiedad en '{path}': el factor existente "
            f"({tipo}) no porta un sello atribuible a ({urn}, {target}); "
            "no se reemplazó"
        )
    return None


def _conflicto_ancestros(path: Path) -> str | None:
    """Exige directorios reales en toda la jerarquía previa al destino."""
    absoluta = path if path.is_absolute() else Path.cwd() / path
    actual = Path(absoluta.anchor)
    for parte in absoluta.parent.parts[1:]:
        actual /= parte
        try:
            tipo = _tipo_nodo(actual)
        except OSError:
            tipo = "nodo ilegible"
        if tipo is None:
            return None
        if tipo != "directorio":
            return (
                f"jerarquía insegura: el ancestro '{actual}' es {tipo}; "
                "no se siguió"
            )
    return None


def _directorios_emitidos(raiz: Path,
                          archivos: list[tuple[str, str]]) -> list[Path]:
    """Directorios que constituyen una unidad cerrada de emisión."""
    directorios = set()
    for rel, _ in archivos:
        partes = Path(rel).parts
        if len(partes) >= 4 and partes[1] in ("skills", "workspaces"):
            directorios.add(
                raiz / "_emision" / partes[0] / partes[1] / partes[2])
    return sorted(directorios)


RUTAS_APLICAR = {
    ("claude-code", "skill"): "~/.claude/skills/{nombre}",
    ("claude-code", "agente"): "~/.claude/agents/{nombre}.md",
    ("codex", "skill"): "~/.agents/skills/{nombre}",
    ("codex", "agente"): "~/.codex/agents/{nombre}.toml",
    ("opencode", "skill"): "~/.config/opencode/skills/{nombre}",
    ("opencode", "agente"): "~/.config/opencode/agents/{nombre}.md",
    # openclaw: KORA aplica agentes solo sobre blueprints fleet autorizados;
    # el materializador fleet los proyecta luego al workspace runtime privado.
    ("openclaw", "skill"): "~/.openclaw/skills/{nombre}",
    ("openclaw", "agente"): "~/openclaw-fleet/blueprints/{nombre}",
}

# Instalacion a nivel proyecto (--proyecto): el artefacto vive en el .opencode/
# .claude/.codex/.agents del proyecto, no en el home del operador. Paths
# relativos a la raiz del proyecto.
RUTAS_APLICAR_PROYECTO = {
    ("claude-code", "skill"): ".claude/skills/{nombre}",
    ("claude-code", "agente"): ".claude/agents/{nombre}.md",
    ("codex", "skill"): ".agents/skills/{nombre}",
    ("codex", "agente"): ".codex/agents/{nombre}.toml",
    ("opencode", "skill"): ".opencode/skills/{nombre}",
    ("opencode", "agente"): ".opencode/agents/{nombre}.md",
}


def _skill_personal_sombrea_openclaw(nombre: str) -> Path | None:
    """Detecta la colisión global creada por la ruta personal de Codex.

    OpenClaw prioriza ~/.agents/skills sobre ~/.openclaw/skills. KORA conoce
    exactamente su layout directo; el discovery agrupado o por workspace
    pertenece al gate de deploy del runtime, no a esta comprobación.
    """
    ruta = Path(RUTAS_APLICAR[("codex", "skill")].format(
        nombre=nombre)).expanduser()
    return ruta if (ruta / "SKILL.md").is_file() else None


def _validar_blueprint_openclaw(nombre: str, ruta: Path) -> str | None:
    """Gate fail-closed de pertenencia a la flota OpenClaw.

    `targets: [openclaw]` expresa capacidad global de proyección. Aplicar sobre
    esta flota exige además pertenecer a su roster positiva y que el blueprint
    ya exista; KORA nunca crea membresía por efecto colateral.
    """
    if ruta.name != nombre or ruta.parent.name != "blueprints":
        return (
            "el destino OpenClaw de agentes debe ser "
            f"<fleet>/blueprints/{nombre}; recibido '{ruta}'"
        )
    if ruta.is_symlink() or not ruta.is_dir():
        return (
            f"el blueprint autorizado debe preexistir como directorio real: "
            f"'{ruta}'"
        )

    reference = ruta.parent.parent / "openclaw.json.reference"
    try:
        tipo_reference = _tipo_nodo(reference)
    except OSError:
        tipo_reference = "nodo ilegible"
    if tipo_reference != "archivo regular":
        return (
            "no se pudo derivar una roster válida desde un archivo regular "
            f"real en '{reference}'; aplicación bloqueada"
        )
    try:
        datos = json.loads(reference.read_text(encoding="utf-8"))
        agentes = datos["agents"]["list"]
        ids = [agente["id"] for agente in agentes]
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, KeyError,
            TypeError):
        return (
            "no se pudo derivar una roster válida desde "
            f"'{reference}'; aplicación bloqueada"
        )
    if not isinstance(agentes, list) or any(
            not isinstance(agent_id, str) or not agent_id for agent_id in ids):
        return f"roster inválida en '{reference}'; aplicación bloqueada"
    if len(ids) != len(set(ids)):
        return f"roster con IDs duplicados en '{reference}'; aplicación bloqueada"
    if nombre not in ids:
        return (
            f"'{nombre}' puede emitirse para OpenClaw, pero no pertenece a la "
            f"roster de esta flota ({reference})"
        )
    return None


def cmd_transmutar(raiz: Path, urn: str, target: str, aplicar: bool,
                   a_stdout: bool, proyecto: str | None = None) -> int:
    if proyecto and not aplicar:
        print("error: --proyecto requiere --aplicar (instala a nivel "
              "proyecto, no afecta la emision canonica en _emision/).",
              file=sys.stderr)
        return 1
    arts = cargar_corpus(raiz)
    try:
        art = resolver(arts, urn)
    except ErrorResolucion as exc:
        print(f"error: {exc}.", file=sys.stderr)
        return 1
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
    targets = art.campos.get("targets")
    if targets is not None and (
            not isinstance(targets, list) or target not in targets):
        print(f"error: el artefacto '{urn}' no declara el target '{target}'; "
              "la transmutacion no puede ampliar su contrato de despliegue.",
              file=sys.stderr)
        return 1
    if aplicar and art.campos.get("estado") != "activo":
        print(f"error: --aplicar exige estado 'activo'; '{urn}' esta "
              f"'{art.campos.get('estado')}'. La emision historica sigue "
              "disponible sin --aplicar.", file=sys.stderr)
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
    if not _nombre_ruta_seguro(nombre):
        print(f"error: nombre inseguro para una ruta de runtime: '{nombre}'; "
              "debe ser un slug minúsculo con segmentos alfanuméricos "
              "separados por guiones.", file=sys.stderr)
        return 1
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
        hash_hex = hashlib.sha256(art.path.read_bytes()).hexdigest()
        archivos, perdidas_extra = emitir(art, target, proy, hash_hex)
    except ErrorTransmutacion as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    if a_stdout:
        for i, (rel, contenido) in enumerate(archivos):
            if len(archivos) > 1:
                sys.stdout.write(("\n" if i else "") + f"=== {rel} ===\n")
            sys.stdout.write(contenido)
        return 0
    destinos_emision = [
        raiz / "_emision" / rel for rel, _ in archivos
    ]
    if target == "codex":
        rels = {rel for rel, _ in archivos}
        skill_anterior = raiz / "_emision/codex/skills" / nombre
        agente_anterior = (
            raiz / "_emision/codex/agents" / f"{nombre}.toml")
        if not any(
                rel.startswith(f"codex/skills/{nombre}/") for rel in rels):
            destinos_emision.append(skill_anterior)
        if f"codex/agents/{nombre}.toml" not in rels:
            destinos_emision.append(agente_anterior)
    for destino in destinos_emision:
        conflicto = _conflicto_ancestros(destino)
        if conflicto is not None:
            print(f"error: emisión bloqueada: {conflicto}.", file=sys.stderr)
            return 1
    if target == "codex":
        _limpiar_derivados_codex_v1(raiz, art, archivos)
    for directorio in _directorios_emitidos(raiz, archivos):
        _recrear_directorio_gestionado(directorio)
    skill_dir = None
    for rel, contenido in archivos:
        destino = raiz / "_emision" / rel
        destino.parent.mkdir(parents=True, exist_ok=True)
        if _tipo_nodo(destino) not in (None, "archivo regular"):
            _retirar_ruta_gestionada(destino)
        destino.write_text(contenido, encoding="utf-8")
        print(f"emitido: _emision/{rel}")
        if rel.endswith("/SKILL.md"):
            skill_dir = destino.parent
    if art.tipo == "skill" and skill_dir is not None:
        refs = _copiar_referencias(art, skill_dir)
        if refs:
            print(f"emitido: {refs.relative_to(raiz).as_posix()}/ "
                  f"(copia de referencias/)")
    for etiqueta, a, b, razon in list(proy["perdidas"]) + list(perdidas_extra):
        print(f"pérdida declarada: {etiqueta}: {a}->{b} :: {razon}")
    if aplicar:
        return _aplicar(art, target, archivos, proyecto)
    return 0


def _aplicar(art: Artefacto, target: str,
             archivos: list[tuple[str, str]], proyecto: str | None) -> int:
    """Instala la emisión en el runtime real, honrando el `alcance` (ley/3 §7).
    Las skills son productos cerrados; el blueprint OpenClaw preserva todo lo
    ajeno a sus factores KORA; los agentes file-based solo pisan su archivo."""
    nombre_art = art.campos["nombre"]
    alcance = art.campos.get("alcance", "ambos")
    if proyecto and alcance == "usuario":
        print(f"error: '{nombre_art}' declara alcance 'usuario'; no admite "
              f"instalacion a nivel proyecto (--proyecto).", file=sys.stderr)
        return 1
    if not proyecto and alcance == "proyecto":
        print(f"error: '{nombre_art}' declara alcance 'proyecto'; requiere "
              f"--proyecto PATH (no se instala a nivel usuario).",
              file=sys.stderr)
        return 1
    if proyecto:
        base = Path(proyecto).expanduser()
        if not base.is_dir():
            print(f"error: el proyecto '{proyecto}' no es un directorio.",
                  file=sys.stderr)
            return 1
        if (target, art.tipo) not in RUTAS_APLICAR_PROYECTO:
            soportados = ", ".join(
                sorted({t for t, _ in RUTAS_APLICAR_PROYECTO}))
            print(f"error: el target '{target}' no soporta instalacion a "
                  f"nivel proyecto (soportados: {soportados}).",
                  file=sys.stderr)
            return 1
        ruta = base / RUTAS_APLICAR_PROYECTO[(target, art.tipo)].format(
            nombre=nombre_art)
    else:
        ruta = Path(RUTAS_APLICAR[(target, art.tipo)].format(
            nombre=nombre_art)).expanduser()
    conflicto_jerarquia = _conflicto_ancestros(ruta)
    if conflicto_jerarquia is not None:
        print(f"error: {conflicto_jerarquia}.", file=sys.stderr)
        return 1
    if not proyecto and target == "openclaw" and art.tipo == "agente":
        error_blueprint = _validar_blueprint_openclaw(nombre_art, ruta)
        if error_blueprint is not None:
            print(f"error: {error_blueprint}", file=sys.stderr)
            return 1
    if not proyecto and target == "openclaw" and art.tipo == "skill":
        sombra = _skill_personal_sombrea_openclaw(nombre_art)
        if sombra is not None:
            print("error: la skill personal de mayor precedencia "
                  f"'{sombra}' ya sombrea la instalación managed OpenClaw "
                  f"'{ruta}'. No se aplicó una copia inefectiva; resuelve el "
                  "propietario del target en el deploy por agente.",
                  file=sys.stderr)
            return 1
    if target == "codex" and art.tipo == "agente":
        if proyecto:
            agente = ruta
            skill = base / RUTAS_APLICAR_PROYECTO[("codex", "skill")].format(
                nombre=nombre_art)
        else:
            agente = ruta
            skill = Path(RUTAS_APLICAR[("codex", "skill")].format(
                nombre=nombre_art)).expanduser()
        conflicto_jerarquia = _conflicto_ancestros(skill)
        if conflicto_jerarquia is not None:
            print(f"error: {conflicto_jerarquia}.", file=sys.stderr)
            return 1
        hay_skill = any(
            len(Path(rel).parts) >= 4 and Path(rel).parts[1] == "skills"
            for rel, _ in archivos
        )
        factores_agente = [
            (agente, contenido)
            for rel, contenido in archivos
            if len(Path(rel).parts) >= 3
            and Path(rel).parts[1] == "agents"
        ]
        for destino, _ in factores_agente:
            conflicto = _conflicto_propiedad_archivo(
                destino, art.urn or "", "codex")
            if conflicto is not None:
                print(f"error: {conflicto}.", file=sys.stderr)
                return 1
        if hay_skill:
            conflicto = _conflicto_propiedad_skill(
                skill, art.urn or "", "codex")
            if conflicto is not None:
                print(f"error: {conflicto}.", file=sys.stderr)
                return 1
            _recrear_directorio_gestionado(skill)
        elif _tipo_nodo(skill) == "directorio" and _sello_atribuye(
                skill / "SKILL.md", art.urn or "", "codex"):
            _retirar_ruta_gestionada(skill)
            print(f"retirado: {skill}")
        instalados = []
        for rel, contenido in archivos:
            partes = Path(rel).parts
            if len(partes) >= 3 and partes[1] == "agents":
                agente.parent.mkdir(parents=True, exist_ok=True)
                agente.write_text(contenido, encoding="utf-8")
                instalados.append(agente)
            elif len(partes) >= 4 and partes[1] == "skills":
                relativo = Path(*partes[3:])
                destino = skill / relativo
                destino.parent.mkdir(parents=True, exist_ok=True)
                destino.write_text(contenido, encoding="utf-8")
                instalados.append(skill)
        for destino in dict.fromkeys(instalados):
            print(f"aplicado: {destino}")
        return 0
    dir_based = (art.tipo == "skill"
                 or (art.tipo, target) == ("agente", "openclaw"))
    if dir_based:
        if art.tipo == "skill":
            conflicto = _conflicto_propiedad_skill(
                ruta, art.urn or "", target)
            if conflicto is not None:
                print(f"error: {conflicto}.", file=sys.stderr)
                return 1
            _recrear_directorio_gestionado(ruta)
        else:
            for rel, _ in archivos:
                destino = ruta / Path(rel).name
                conflicto = _conflicto_propiedad_archivo(
                    destino, art.urn or "", "openclaw")
                if conflicto is not None:
                    print(f"error: {conflicto}.", file=sys.stderr)
                    return 1
            emitidos = {Path(rel).name for rel, _ in archivos}
            soul = ruta / "SOUL.md"
            if "SOUL.md" not in emitidos and _sello_atribuye(
                    soul, art.urn or "", "openclaw"):
                soul.unlink()
        for rel, contenido in archivos:
            partes = Path(rel).parts
            if art.tipo == "skill" and len(partes) >= 4 \
                    and partes[1] == "skills" \
                    and partes[2] == nombre_art:
                relativo = Path(*partes[3:])
            else:
                relativo = Path(rel).name
            destino = ruta / relativo
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_text(contenido, encoding="utf-8")
        if art.tipo == "skill":
            _copiar_referencias(art, ruta)
    else:
        conflicto = _conflicto_propiedad_archivo(
            ruta, art.urn or "", target)
        if conflicto is not None:
            print(f"error: {conflicto}.", file=sys.stderr)
            return 1
        ruta.parent.mkdir(parents=True, exist_ok=True)
        ruta.write_text(archivos[0][1], encoding="utf-8")
    print(f"aplicado: {ruta}")
    return 0


# ---------------------------------------------------- paridad (ley/3 §9.1)

def _unidades_emision(emision: Path):
    """Descubre unidades sin seguir enlaces.

    Devuelve `(unidades, anomalías)`. Una anomalía es
    `(target|None, nombre|None, detalle)` y nunca deriva rutas runtime.
    """
    unidades = []
    anomalias = []
    try:
        tipo_emision = _tipo_nodo(emision)
    except OSError:
        tipo_emision = "nodo ilegible"
    if tipo_emision is None:
        return unidades, anomalias
    if tipo_emision != "directorio":
        anomalias.append((
            None, None, f"_emision es {tipo_emision}; no se recorrió"))
        return unidades, anomalias

    try:
        targets = sorted(Path(e.path) for e in os.scandir(emision))
    except OSError:
        anomalias.append((None, None, "_emision es ilegible"))
        return unidades, anomalias
    for target_dir in targets:
        target = target_dir.name
        try:
            tipo_target = _tipo_nodo(target_dir)
        except OSError:
            tipo_target = "nodo ilegible"
        if tipo_target != "directorio":
            anomalias.append((
                target, None,
                f"raíz de target es {tipo_target}; no se recorrió"))
            continue
        for coleccion, tipo_unidad, raiz_unidad, extensiones in (
                ("skills", "skill", "SKILL.md", ()),
                ("agents", "agente", None, (".md", ".toml")),
                ("workspaces", "agente", "AGENTS.md", ())):
            contenedor = target_dir / coleccion
            try:
                tipo_contenedor = _tipo_nodo(contenedor)
            except OSError:
                tipo_contenedor = "nodo ilegible"
            if tipo_contenedor is None:
                continue
            if tipo_contenedor != "directorio":
                anomalias.append((
                    target, None,
                    f"{coleccion}/ es {tipo_contenedor}; no se recorrió"))
                continue
            try:
                entradas = sorted(Path(e.path) for e in os.scandir(contenedor))
            except OSError:
                anomalias.append((
                    target, None, f"{coleccion}/ es ilegible"))
                continue
            for entrada in entradas:
                nombre = entrada.stem if extensiones else entrada.name
                if extensiones and entrada.suffix not in extensiones:
                    continue
                if not _nombre_ruta_seguro(nombre):
                    anomalias.append((
                        target, nombre,
                        f"nombre inseguro en {coleccion}/; no se derivó ruta"))
                    continue
                try:
                    tipo_entrada = _tipo_nodo(entrada)
                    tipo_raiz = (
                        _tipo_nodo(entrada / raiz_unidad)
                        if raiz_unidad is not None
                        and tipo_entrada == "directorio"
                        else None
                    )
                except OSError:
                    tipo_entrada = "nodo ilegible"
                    tipo_raiz = None
                if raiz_unidad is not None \
                        and tipo_entrada == "directorio" \
                        and tipo_raiz is None:
                    continue
                unidades.append((target, tipo_unidad, nombre, entrada))
    return unidades, anomalias


def _alcance_admite(art: Artefacto, proyecto: bool) -> bool:
    alcance = art.campos.get("alcance", "ambos")
    return alcance in (("proyecto", "ambos") if proyecto
                       else ("usuario", "ambos"))


def _unidades_esperadas(arts: list[Artefacto], proyecto: bool = False,
                        target_solicitado: str | None = None):
    """Unidades operacionales prometidas por fuentes agénticas activas.

    Una lista `targets` presente restringe la fuente. Si se omite, la fuente es
    agnóstica: promete Codex en la operación ordinaria y el target realizado que
    el operador solicite explícitamente en una auditoría focal.
    """
    for art in arts:
        if art.tipo not in ("skill", "agente") or \
                art.campos.get("estado") != "activo" or \
                not _alcance_admite(art, proyecto):
            continue
        nombre = art.campos.get("nombre")
        targets = art.campos.get("targets")
        if targets is None:
            targets = [target_solicitado or TARGET_PRINCIPAL]
        if not isinstance(nombre, str) or not isinstance(targets, list):
            continue
        for target in targets:
            if target not in TARGETS_REALIZADOS:
                continue
            if art.tipo == "skill":
                yield target, "skill", nombre, art
            else:
                yield target, "agente", nombre, art
                if target == "codex" and art.campos.get("forma") == "agente":
                    yield target, "skill", nombre, art


def _unidades_runtime_posibles(arts: list[Artefacto], proyecto: bool = False):
    """Rutas del nivel donde el mismo URN puede persistir como residual."""
    rutas = RUTAS_APLICAR_PROYECTO if proyecto else RUTAS_APLICAR
    for art in arts:
        nombre = art.campos.get("nombre")
        if art.tipo not in ("skill", "agente") or not art.urn \
                or not isinstance(nombre, str) \
                or not _nombre_ruta_seguro(nombre):
            continue
        for target in TARGETS_REALIZADOS:
            for tipo in ("skill", "agente"):
                if (target, tipo) in rutas:
                    yield target, tipo, nombre, art


def _campos_sello_unidad(path: Path, tipo: str) -> dict[str, str]:
    """Lee el proof-carrier de una unidad solo tras validar su raíz real."""
    try:
        tipo_path = _tipo_nodo(path)
    except OSError:
        return {}
    if tipo == "skill":
        if tipo_path != "directorio":
            return {}
        sello = path / "SKILL.md"
    elif tipo_path == "directorio":
        sello = path / "AGENTS.md"
    elif tipo_path == "archivo regular":
        sello = path
    else:
        return {}
    return _campos_ultimo_sello(sello)


def _sello_atribuye_unidad(path: Path, tipo: str,
                            urn: str, target: str) -> bool:
    campos = _campos_sello_unidad(path, tipo)
    return campos.get("fuente") == urn and campos.get("target") == target


def _sello_atribuye_residuo(path: Path, tipo: str,
                             urn: str, target: str) -> bool:
    """Atribuye una unidad histórica por cualquiera de sus proof-carriers."""
    if _sello_atribuye_unidad(path, tipo, urn, target):
        return True
    try:
        es_directorio = _tipo_nodo(path) == "directorio"
    except OSError:
        es_directorio = False
    return tipo == "agente" and es_directorio \
        and _sello_atribuye(path / "SOUL.md", urn, target)


def _conflictos_propiedad_blueprint(origen: Path, destino: Path,
                                     urn: str, target: str) -> list[str]:
    """Replica el preflight factor-a-factor de `--aplicar` en paridad."""
    conflictos = []
    for nombre in ("AGENTS.md", "SOUL.md"):
        try:
            tipo_origen = _tipo_nodo(origen / nombre)
            tipo = _tipo_nodo(destino / nombre)
        except OSError:
            conflictos.append(f"nodo ilegible {nombre}")
            continue
        if tipo_origen is None:
            continue
        if tipo is not None and (
                tipo != "archivo regular"
                or not _sello_atribuye(destino / nombre, urn, target)):
            conflictos.append(f"{tipo} {nombre} no atribuible")
    return conflictos


def _archivos_iguales(origen: Path, destino: Path) -> bool:
    """Igualdad byte a byte con memoria acotada."""
    with origen.open("rb") as fuente, destino.open("rb") as instalado:
        while True:
            bloque_fuente = fuente.read(64 * 1024)
            bloque_instalado = instalado.read(64 * 1024)
            if bloque_fuente != bloque_instalado:
                return False
            if not bloque_fuente:
                return True


def _diferencias_materia(origen: Path, destino: Path,
                         esperados: dict[str, str],
                         observados: dict[str, str]) -> list[str]:
    materia_esperada = {
        rel for rel, tipo in esperados.items() if tipo != "directorio"
    }
    difieren: list[str] = []
    for rel in sorted(materia_esperada):
        tipo_esperado = esperados[rel]
        tipo_observado = observados.get(rel)
        if tipo_observado is None:
            difieren.append(f"falta {rel}")
        elif tipo_esperado != "archivo regular":
            difieren.append(f"emisión contiene {tipo_esperado} {rel}")
        elif tipo_observado != "archivo regular":
            difieren.append(f"{tipo_observado} {rel}")
        elif not _archivos_iguales(origen / rel, destino / rel):
            difieren.append(f"difiere {rel}")
    return difieren


def _diferencias_skill_cerrada(origen: Path, destino: Path) -> list[str]:
    """Compara la fibra cerrada sin seguir enlaces ni leer sus sobrantes."""
    esperados = _inventario_nodos(origen)
    observados = _inventario_nodos(destino)
    difieren = _diferencias_materia(
        origen, destino, esperados, observados)
    materia_esperada = {
        rel for rel, tipo in esperados.items() if tipo != "directorio"
    }
    materia_observada = {
        rel for rel, tipo in observados.items() if tipo != "directorio"
    }
    for rel in sorted(materia_observada - materia_esperada):
        tipo = observados[rel]
        etiqueta = rel if tipo == "archivo regular" else f"{tipo} {rel}"
        difieren.append(f"sobra {etiqueta}")
    return difieren


def _diferencias_blueprint(origen: Path, destino: Path) -> list[str]:
    """Compara solo factores emitidos; el resto del blueprint es runtime."""
    esperados = _inventario_nodos(origen)
    observados = {}
    for rel, tipo in esperados.items():
        if tipo == "directorio":
            continue
        observado = _tipo_nodo(destino / rel)
        if observado is not None:
            observados[rel] = observado
    return _diferencias_materia(origen, destino, esperados, observados)


def cmd_paridad(raiz: Path, target: str | None, urn: str | None,
                proyecto: str | None = None) -> int:
    """Paridad emisión↔instalación user-level o project-level (ley/3 §9.1). Solo
    lectura: `fiel` = frontera KORA gestionada byte-idéntica a la emisión;
    `desviada` = instalación presente que difiere (stale o editada);
    `no-instalada` = informativo (el gesto no decide si debe instalarse).
    Las skills se comparan como directorios cerrados. En blueprints OpenClaw
    solo gobierna AGENTS.md y el SOUL.md atribuible al mismo par KORA; el
    scaffolding y la memoria del runtime quedan fuera."""
    if target is not None and target not in TARGETS_REALIZADOS:
        print(f"error: el target '{target}' es reconocido por la ley pero no "
              f"está realizado en esta encarnación; GENESIS.md declara esa "
              f"deuda. Realizados: {', '.join(TARGETS_REALIZADOS)}.",
              file=sys.stderr)
        return 1
    emision = raiz / "_emision"
    arts = cargar_corpus(raiz)
    base_proyecto = None
    rutas_runtime = RUTAS_APLICAR
    if proyecto is not None:
        base_proyecto = Path(proyecto).expanduser()
        if not base_proyecto.is_dir():
            print(f"error: el proyecto '{proyecto}' no es un directorio.",
                  file=sys.stderr)
            return 1
        rutas_runtime = RUTAS_APLICAR_PROYECTO
        if target is not None and not any(
                tgt == target for tgt, _ in rutas_runtime):
            soportados = ", ".join(sorted({t for t, _ in rutas_runtime}))
            print(f"error: el target '{target}' no soporta instalacion a "
                  f"nivel proyecto (soportados: {soportados}).",
                  file=sys.stderr)
            return 1
    nombre_filtro = None
    if urn:
        try:
            art = resolver(arts, urn)
        except ErrorResolucion as exc:
            print(f"error: {exc}.", file=sys.stderr)
            return 1
        if art is None:
            print(f"error: el URN '{urn}' no resuelve en el censo.",
                  file=sys.stderr)
            return 1
        if art.tipo == "conocimiento":
            print("error: el conocimiento no se transmuta ni tiene "
                  "instalación cuya paridad verificar.", file=sys.stderr)
            return 1
        if art.tipo not in ("skill", "agente"):
            print(f"error: '{urn}' no tiene un frontmatter agéntico íntegro; "
                  "corre `velar` y corrige antes de verificar paridad.",
                  file=sys.stderr)
            return 1
        targets = art.campos.get("targets")
        if target is not None and targets is not None and (
                not isinstance(targets, list) or target not in targets):
            print(f"error: el artefacto '{urn}' no declara el target "
                  f"'{target}'; la paridad no puede ampliar su contrato de "
                  "despliegue.", file=sys.stderr)
            return 1
        if not _alcance_admite(art, proyecto is not None):
            alcance = art.campos.get("alcance", "ambos")
            if proyecto is not None:
                print(f"error: '{art.campos.get('nombre')}' declara alcance "
                      f"'{alcance}'; no admite instalacion a nivel proyecto "
                      "(--proyecto).", file=sys.stderr)
            else:
                print(f"error: '{art.campos.get('nombre')}' declara alcance "
                      f"'{alcance}'; requiere --proyecto PATH (no se instala "
                      "a nivel usuario).", file=sys.stderr)
            return 1
        nombre_filtro = art.campos.get("nombre")
    for fuente in arts:
        if fuente.tipo not in ("skill", "agente"):
            continue
        if urn is not None and fuente.urn != urn:
            continue
        nombre = fuente.campos.get("nombre")
        if nombre_filtro is not None and nombre != nombre_filtro:
            continue
        if not isinstance(nombre, str) or not _nombre_ruta_seguro(nombre):
            print("error: paridad no deriva rutas desde un nombre inseguro: "
                  f"'{nombre}'. Corrige `forma-valida` primero.",
                  file=sys.stderr)
            return 1
    esperadas = list(_unidades_esperadas(
        arts, proyecto is not None, target_solicitado=target))
    esperadas = [u for u in esperadas
                 if (target is None or u[0] == target)
                 and (urn is None or u[3].urn == urn)
                 and (u[0], u[1]) in rutas_runtime]
    unidades, anomalias_emision = _unidades_emision(emision)
    unidades = [u for u in unidades
                if (target is None or u[0] == target)
                and (nombre_filtro is None or u[2] == nombre_filtro)
                and (u[0], u[1]) in rutas_runtime]
    por_urn = {art.urn: art for art in arts if art.urn}
    unidades = [
        unidad for unidad in unidades
        if (fuente := _campos_sello_unidad(
            unidad[3], unidad[1]).get("fuente")) not in por_urn
        or _alcance_admite(por_urn[fuente], proyecto is not None)
    ]
    if urn is not None:
        claves_esperadas = {u[:3] for u in esperadas}
        unidades = [
            u for u in unidades
            if u[:3] in claves_esperadas
            or _sello_atribuye_unidad(u[3], u[1], urn, u[0])
        ]
    anomalias_emision = [
        a for a in anomalias_emision
        if (target is None or a[0] is None or a[0] == target)
        and (a[0] is None or any(
            tgt == a[0] for tgt, _ in rutas_runtime))
        and (nombre_filtro is None or a[1] is None
             or a[1] == nombre_filtro)
    ]
    fuentes = {(t, tipo, nombre): art
               for t, tipo, nombre, art in esperadas}
    grupos_emision = {}
    for unidad in unidades:
        grupos_emision.setdefault(unidad[:3], []).append(unidad)
    ambiguas = {
        clave: grupo for clave, grupo in grupos_emision.items()
        if len(grupo) > 1
    }
    unidades = [
        grupo[0] for clave, grupo in grupos_emision.items()
        if clave not in ambiguas
    ]
    sellos_emision = {}
    historicas = []
    for tgt, tipo, nombre, origen in unidades:
        sello = _campos_sello_unidad(origen, tipo)
        sellos_emision[(tgt, tipo, nombre)] = sello
    claves_emitidas = set(grupos_emision)
    claves_emitidas_validas = {
        clave for clave, sello in sellos_emision.items()
        if clave in fuentes
        and sello.get("fuente") == (fuentes[clave].urn or "")
        and sello.get("target") == clave[0]
    }
    faltantes = [u for u in esperadas if u[:3] not in claves_emitidas]
    sin_unidades_activas = not grupos_emision and not esperadas
    for tgt, tipo, nombre, _ in faltantes:
        print(f"paridad: sin-emision    {tgt}  {nombre} ({tipo})")
    fiel = ausentes = 0
    desviadas = len(anomalias_emision) + len(ambiguas)
    for tgt, nombre, detalle in anomalias_emision:
        print(f"paridad: desviada      {tgt or '_emision'}  "
              f"{nombre or '(estructura)'} :: {detalle}")
    for (tgt, _tipo, nombre), grupo in ambiguas.items():
        rutas = ", ".join(
            p.relative_to(emision).as_posix() for *_, p in grupo)
        print(f"paridad: desviada      {tgt}  {nombre} :: "
              f"emisión ambigua: {rutas}")
    jerarquias_inseguras = set()
    for tgt, tipo, nombre, origen in unidades:
        clave = (tgt, tipo, nombre)
        plantilla = rutas_runtime.get((tgt, tipo))
        if plantilla is None:
            continue
        destino_rel = Path(plantilla.format(nombre=nombre))
        destino = ((base_proyecto / destino_rel)
                   if base_proyecto is not None
                   else destino_rel.expanduser())
        conflicto_jerarquia = _conflicto_ancestros(destino)
        if conflicto_jerarquia is not None:
            jerarquias_inseguras.add(conflicto_jerarquia)
            desviadas += 1
            print(f"paridad: desviada      {tgt}  {nombre} :: "
                  f"{conflicto_jerarquia}")
            continue
        fuente_esperada = fuentes.get(clave)
        if fuente_esperada is not None and clave not in claves_emitidas_validas:
            desviadas += 1
            print(f"paridad: desviada      {tgt}  {nombre} :: "
                  "el sello de emisión no atribuye la unidad activa "
                  f"a ({fuente_esperada.urn}, {tgt})")
            continue
        try:
            tipo_origen = _tipo_nodo(origen)
            tipo_destino = _tipo_nodo(destino)
        except OSError as exc:
            ilegible = Path(exc.filename).name if exc.filename else nombre
            desviadas += 1
            print(f"paridad: desviada      {tgt}  {nombre} :: "
                  f"ilegible {ilegible}")
            continue
        if fuente_esperada is None:
            historicas.append(clave)
            continue
        if tipo_destino is None:
            ausentes += 1
            print(f"paridad: no-instalada  {tgt}  {nombre}")
            continue
        if tipo_destino != tipo_origen:
            desviadas += 1
            print(f"paridad: desviada      {tgt}  {nombre} :: "
                  f"tipo incompatible: esperado {tipo_origen}, "
                  f"observado {tipo_destino}")
            continue
        es_blueprint = tgt == "openclaw" and tipo == "agente" \
            and tipo_destino == "directorio"
        if es_blueprint:
            factores_emitidos = [
                factor for factor in ("AGENTS.md", "SOUL.md")
                if _tipo_nodo(origen / factor) is not None
            ]
            hay_factor_emitido = any(
                _tipo_nodo(destino / factor) is not None
                for factor in factores_emitidos
            )
            hay_soul_residual = "SOUL.md" not in factores_emitidos \
                and _sello_atribuye(
                    destino / "SOUL.md",
                    fuente_esperada.urn or "", tgt)
            if not hay_factor_emitido and not hay_soul_residual:
                ausentes += 1
                print(f"paridad: no-instalada  {tgt}  {nombre}")
                continue
        conflictos_blueprint = (
            _conflictos_propiedad_blueprint(
                origen, destino, fuente_esperada.urn or "", tgt)
            if es_blueprint else []
        )
        if conflictos_blueprint:
            desviadas += 1
            print(f"paridad: desviada      {tgt}  {nombre} :: "
                  "conflicto de propiedad: "
                  + ", ".join(conflictos_blueprint))
            continue
        if not es_blueprint and not _sello_atribuye_unidad(
                destino, tipo, fuente_esperada.urn or "", tgt):
            desviadas += 1
            print(f"paridad: desviada      {tgt}  {nombre} :: "
                  "conflicto de propiedad: el proof-carrier no atribuye la "
                  f"instalación a ({fuente_esperada.urn}, {tgt})")
            continue
        if proyecto is None and tgt == "openclaw" and tipo == "skill":
            sombra = _skill_personal_sombrea_openclaw(nombre)
            if sombra is not None:
                desviadas += 1
                print(f"paridad: desviada      {tgt}  {nombre} :: "
                      f"instalación managed sombreada globalmente por {sombra}")
                continue
        try:
            if tipo_origen == "directorio":
                if tipo == "skill":
                    difieren = _diferencias_skill_cerrada(origen, destino)
                else:
                    difieren = _diferencias_blueprint(origen, destino)
                    fuente = fuentes.get((tgt, tipo, nombre))
                    soul = destino / "SOUL.md"
                    if tgt == "openclaw" \
                            and _tipo_nodo(origen / "SOUL.md") is None \
                            and fuente is not None and _sello_atribuye(
                                soul, fuente.urn or "", tgt):
                        difieren.append("sobra SOUL.md")
            elif not _archivos_iguales(origen, destino):
                difieren = [f"difiere {destino.name}"]
            else:
                difieren = []
        except OSError as exc:
            ilegible = Path(exc.filename).name if exc.filename else destino.name
            difieren = [f"ilegible {ilegible}"]
        if difieren:
            desviadas += 1
            print(f"paridad: desviada      {tgt}  {nombre} :: "
                  + ", ".join(difieren))
        else:
            fiel += 1
            print(f"paridad: fiel          {tgt}  {nombre}")
    posibles = list(_unidades_runtime_posibles(arts, proyecto is not None))
    posibles = [
        unidad for unidad in posibles
        if (target is None or unidad[0] == target)
        and (urn is None or unidad[3].urn == urn)
    ]
    residuos_reportados = set()
    for tgt, tipo, nombre, fuente in posibles:
        clave = (tgt, tipo, nombre)
        if clave in fuentes:
            continue
        plantilla = rutas_runtime.get((tgt, tipo))
        if plantilla is None:
            continue
        destino_rel = Path(plantilla.format(nombre=nombre))
        destino = ((base_proyecto / destino_rel)
                   if base_proyecto is not None
                   else destino_rel.expanduser())
        conflicto_jerarquia = _conflicto_ancestros(destino)
        if conflicto_jerarquia is not None:
            if conflicto_jerarquia not in jerarquias_inseguras:
                jerarquias_inseguras.add(conflicto_jerarquia)
                desviadas += 1
                print(f"paridad: desviada      {tgt}  (estructura) :: "
                      f"{conflicto_jerarquia}")
            continue
        if _sello_atribuye_residuo(
                destino, tipo, fuente.urn or "", tgt):
            if clave in residuos_reportados:
                continue
            residuos_reportados.add(clave)
            desviadas += 1
            if tgt == "codex" and tipo == "skill" \
                    and fuente.tipo == "agente":
                detalle = "sobra skill complementaria gestionada"
            else:
                detalle = "instalación residual de unidad no vigente"
            print(f"paridad: desviada      {tgt}  {nombre} :: {detalle}")
    for tgt, tipo, nombre in dict.fromkeys(historicas):
        if (tgt, tipo, nombre) in residuos_reportados:
            continue
        ausentes += 1
        print(f"paridad: no-instalada  {tgt}  {nombre} "
              "(emisión histórica)")
    if sin_unidades_activas and not desviadas:
        print("paridad: sin artefactos activos que verificar.")
        return 0
    print(f"paridad: {fiel} fiel · {desviadas} desviadas · "
          f"{ausentes} no-instaladas · {len(faltantes)} sin-emision.")
    if desviadas or faltantes:
        print("veredicto: transmutar las unidades sin-emision; reaplicar solo "
              "drift activo atribuible; adjudicar los conflictos de propiedad "
              "y retirar manualmente las unidades residuales.")
        return 1
    return 0


# ------------------------------------------------------------- ciclo (§5)

# Línea `estado:` del frontmatter: valor + comentario inline opcional +
# terminador original. La reescritura solo toca el grupo del valor.
RE_LINEA_ESTADO = re.compile(
    r"^(estado:[ \t]+)([^#\r\n]*?)([ \t]*(?:#[^\r\n]*)?)(\r\n|\n|\r|)$")


def cmd_ciclo(raiz: Path, urn: str, nuevo: str) -> int:
    arts = cargar_corpus(raiz)
    try:
        art = resolver(arts, urn)
    except ErrorResolucion as exc:
        print(f"error: {exc}.", file=sys.stderr)
        return 1
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
    # Gate de promoción: el corpus actual pasa los checks de fuente y el
    # artefacto satisface `publicacion-digna` EN EL ESTADO DESTINO. Evaluar
    # solo el borrador de origen dejaría pasar una publicación indigna.
    # Las transiciones hacia deprecado/retirado no exigen gate.
    if nuevo in ("publicado", "activo"):
        resultados = velar_todo(raiz)
        resultados["publicacion-digna"] = _fallos_publicacion_art(art, nuevo)
        fallos = [(cid, p, m) for cid, fs in resultados.items()
                  for p, m in fs]
        if fallos:
            for cid, p, m in fallos:
                print("error: promoción rechazada: el corpus completo no "
                      f"pasa velar o el estado destino no es digno: "
                      f"[{cid}] {p} :: {m}.", file=sys.stderr)
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

def _huerfanos(arts: list, raiz: Path) -> list:
    """KB publicados no alcanzados por ninguna arista de consumo (las 6:
    cita/depende/reemplaza/refina/conocimiento/componible). Reporte
    informativo, NO check del registro cerrado (ley/0 §11): las raíces de
    consumo directo —guías leídas con `nombre`, registros citados solo en la
    prosa de la ley— pueden aparecer sin ser huérfanos reales. Solo `publicado`
    (un `deprecado` sin citadores es legítimo por la dignidad del URN, ley/0 §9).
    """
    referenciados = set()
    for a in arts:
        for campo in CAMPOS_RELACION + ("conocimiento", "componible"):
            v = a.campos.get(campo)
            if isinstance(v, list):
                referenciados.update(v)
    prosa = ""
    leydir = raiz / "ley"
    if leydir.is_dir():
        for f in sorted(leydir.glob("*.md")):
            prosa += f.read_text(encoding="utf-8")
    huerf = []
    for a in arts:
        if a.tipo == "conocimiento" and a.campos.get("estado") == "publicado" \
                and a.urn and a.urn not in referenciados:
            huerf.append((a, a.urn in prosa))
    return huerf


def cmd_censo(raiz: Path, como_json: bool, escribir: bool,
              huerfanos: bool = False) -> int:
    arts = cargar_corpus(raiz)
    if huerfanos:
        huerf = _huerfanos(arts, raiz)
        if not huerf:
            print("huerfanos: 0 — todo kb publicado es alcanzable.")
            return 0
        print("kb publicados no alcanzados por arista de consumo "
              "(cita/depende/reemplaza/refina/conocimiento/componible):\n")
        for a, en_ley in huerf:
            marca = "[raiz-ley: lo cita la prosa de ley/]" if en_ley \
                else "[revisar: ni arista ni cita en ley]"
            print(f"  {a.urn}  {marca}")
        print(f"\nhuerfanos: {len(huerf)} candidato(s) — reporte informativo, "
              "no check. Las raices de consumo directo (guias leidas con "
              "`nombre`, registros citados solo por la ley) no son huerfanos "
              "reales; juzgar el resto.")
        return 0
    entradas = construir_censo(arts)
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
    try:
        art = resolver(cargar_corpus(raiz), urn)
    except ErrorResolucion as exc:
        print(f"error: {exc}.", file=sys.stderr)
        return 1
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
    p.add_argument("--huerfanos", action="store_true",
                   help="reporta kb publicado no alcanzado por arista de "
                        "consumo (informativo, no check)")

    p = sub.add_parser("nombre", help="resuelve un URN a su nombre verdadero")
    p.add_argument("urn")

    p = sub.add_parser("velar", help="corre todos los checks de coherencia")
    p.add_argument("--estricto", action="store_true",
                   help="añade dignidad de publicación y frescura de emisiones")

    p = sub.add_parser(
        "transmutar", help="proyección reticular y emisión a un runtime")
    p.add_argument("--urn")
    p.add_argument("--target", choices=list(TARGETS_CONOCIDOS),
                   help=(f"runtime destino; en emisión, ausente = "
                         f"{TARGET_PRINCIPAL}; en paridad, ausente = barrido global"))
    p.add_argument("--aplicar", action="store_true",
                   help="instala en los paths del runtime")
    p.add_argument("--stdout", action="store_true",
                   help="imprime la emisión en vez de escribirla")
    p.add_argument("--proyecto", metavar="PATH",
                   help="selecciona nivel proyecto en PATH para --aplicar "
                        "o --paridad, en vez del home del operador")
    p.add_argument("--paridad", action="store_true",
                   help="verifica emisión↔instalación (user-level por defecto; "
                        "project-level con --proyecto, ley/3 §9.1): fiel / "
                        "desviada / no-instalada; exit 1 si hay desviadas o "
                        "sin-emision. "
                        "Sin --urn ni --target barre todo")

    p = sub.add_parser("ciclo", help="transición de lifecycle (solo adelante)")
    p.add_argument("urn")
    p.add_argument("estado")

    sub.add_parser("ley", help="concatena ALMA.md + ley/0..4")

    args = parser.parse_args(argv)
    raiz = raiz_corpus()
    if args.gesto == "censo":
        modos = [
            nombre for nombre, activo in (
                ("--json", args.json),
                ("--escribir", args.escribir),
                ("--huerfanos", args.huerfanos),
            )
            if activo
        ]
        if len(modos) > 1:
            print("error: modos de salida incompatibles para censo: "
                  + ", ".join(modos) + ".", file=sys.stderr)
            return 2
        return cmd_censo(raiz, args.json, args.escribir, args.huerfanos)
    if args.gesto == "nombre":
        return cmd_nombre(raiz, args.urn)
    if args.gesto == "velar":
        return cmd_velar(raiz, args.estricto)
    if args.gesto == "transmutar":
        if args.paridad:
            if args.aplicar or args.stdout:
                print("error: --paridad es verificación de solo lectura; no "
                      "admite --aplicar ni --stdout.",
                      file=sys.stderr)
                return 1
            return cmd_paridad(
                raiz, args.target, args.urn, args.proyecto)
        if not args.urn:
            print("error: transmutar requiere --urn (salvo en modo "
                  "--paridad).", file=sys.stderr)
            return 2
        target = args.target or TARGET_PRINCIPAL
        return cmd_transmutar(raiz, args.urn, target, args.aplicar,
                              args.stdout, args.proyecto)
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
