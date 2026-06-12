---
urn: urn:kora:kb:guia-rapida-pneuma
nombre: guia-rapida-pneuma
version: 1.0.0
estado: publicado
descripcion: "Guía rápida de KORA pneuma — qué es, qué garantiza, los seis gestos, el shape, las leyes que velar cobra, lifecycle, transmutación, koraficación y deudas."
fuente: "Primera producción bajo ley/4 (2026-06-12). Korificación de la guía rápida emitida en la sesión de génesis; hechos derivados de ley/0..4, GENESIS.md y kora.py vigentes al commit 4d44bfc. Fuente interna al repo, sin hash externo."
autor: FS
creado: 2026-06-12
lang: es
tags: [pneuma, guia-rapida, gestos, shape, vector, transmutacion, koraficacion, lifecycle]
cita: [urn:kora:kb:alma-de-kora]
familia: nota
---
# guia-rapida-pneuma

## Qué es

KORA pneuma (`~/kora-pneuma`) — encarnación leve de KORA: repositorio,
catálogo y fábrica de los tres tipos de artefacto que consumen sistemas LLM.

- **Conocimiento** — se lee como contexto.
- **Agentes y skills** — se proyectan a runtimes por transmutación.

Núcleo único `kora.py` (stdlib puro, Python ≥ 3.11, cero dependencias). Ley
en 4 estratos y 5 documentos. URN idénticos a la encarnación anterior
(`~/kora`, "la bestia"), que sigue autoritativa para su corpus no migrado.
La ley entera (`kora.py ley`) ≈ 17k tokens: KORA completa cabe en un
contexto LLM. El alma del sistema: [Alma de KORA](urn:kora:kb:alma-de-kora).

## Garantías

| Garantía | Mecanismo |
|---|---|
| Identidad ontológica | Vector PMI×LFS + 5 leyes inter-eje, mecanizadas en `velar` |
| Nombre verdadero | URN sin versión; resuelve incluso retirado el artefacto |
| Coherencia | 13 checks; censo siempre derivado, jamás versionado ni autoridad |
| Proyección honesta | Sello inline en cada emisión: hash, fidelidad por eje, pérdidas con razón |
| Lifecycle digno | Solo hacia adelante; promoción gateada por `velar`; muertos siguen resolviendo |
| Producción con verdad | Koraficación: FS=100%, hechos inventados = fallo (`ley/4`) |

## Los seis gestos

| Comando | Función |
|---|---|
| `python3 kora.py censo [--json] [--escribir]` | Catálogo derivado del filesystem |
| `python3 kora.py nombre <urn>` | Resolver URN — también deprecados y retirados |
| `python3 kora.py velar [--estricto]` | Los 13 checks; exit 0 coherente, 1 con fallos |
| `python3 kora.py transmutar --urn U --target T [--stdout\|--aplicar]` | Proyección funtorial con sello |
| `python3 kora.py ciclo <urn> <estado>` | Transición de lifecycle, solo adelante |
| `python3 kora.py ley` | ALMA + ley/0..4 a stdout |

## Shape y zonas

Un artefacto = un archivo: frontmatter plano + cuerpo Markdown. Gramática:
sin anidación, sin multilínea, listas inline `[a, b]`, claves desconocidas =
error. El tipo se deriva, no se declara:

| Condición | Tipo | Zona y archivo | Régimen URN |
|---|---|---|---|
| `vector` + `forma: habilidad` | skill | `artefactos/skills/{ns}/{nombre}/SKILL.md` (+ `referencias/`) | `urn:{ns}:artefacto:{id}` |
| `vector` + otra `forma` | agente | `artefactos/agentes/{ns}/{nombre}.md` | `urn:{ns}:artefacto:{id}` |
| sin `vector` (exige `familia`) | conocimiento | `artefactos/conocimiento/{ns}/{id}.md` | `urn:{ns}:kb:{id}` |

Campos comunes obligatorios: `urn`, `nombre`, `version` (semver), `estado`,
`descripcion`, `fuente`. Agénticos agregan: `vector` `[pi,mu,xi,lambda,phi]`,
`sigma` (5 componentes), `arnes`, `forma`, `herramientas`, `targets`.
Conocimiento agrega: `familia` ∈ {`nota`, `fuente`, `bok`}. Relaciones
opcionales para todo tipo: `cita`, `depende`, `reemplaza`, `refina`.

## Leyes que velar cobra

- Rangos: Π, Μ, Λ ∈ 0..3; Ξ, Φ ∈ 0..4; σ = 5 componentes ∈ 0..3.
- Leyes inter-eje: Π≥3 ⟹ Μ≥1 · Ξ=4 ⟹ Λ≥1 · Φ≥2 ⟹ Μ≥1 ·
  σ.accountability≥2 ⟹ σ.transparency≥2 · Λ=3 ⟹ todas las σ ≥ 2.
- Dominio por forma:

| Forma | Π | Μ | Ξ | Λ | Φ | Arnés compatible |
|---|---|---|---|---|---|---|
| habilidad | 1-2 | 0-1 | 1-2 | 0 | 1 | utilidad, disciplina, delegado |
| subagente | 1-3 | 0-2 | 1-3 | 0-1 | 1-2 | delegado, persona |
| agente | 2-3 | 2-3 | 2-4 | 0-2 | 1-3 | persona, orquestador |
| plataforma | 2-3 | 3 | 3-4 | 1-3 | 1-3 | orquestador, servicio |

- `arquetipo` no se materializa en ninguna forma.
- Relaciones: todo URN citado debe resolver en el censo local; `depende` sin
  ciclos; `reemplaza` acíclico, antisimétrico y solo hacia artefactos
  deprecados o retirados; `refina` acíclico; `cita` libre.
- `--estricto` agrega: conocimiento publicado con ≥3 `tags`, `descripcion`
  y `fuente` no vacías.

## Lifecycle

| Tipo | Cadena |
|---|---|
| conocimiento | `borrador → publicado → deprecado` |
| agéntico | `borrador → activo → deprecado → retirado` |

Saltos hacia adelante válidos; inversas inválidas siempre. `ciclo` hacia
`publicado` o `activo` rechaza si `velar` falla. Retirado no se reactiva: se
emite artefacto nuevo con `reemplaza`.

## Transmutación

- Targets realizados: `claude-code`, `codex`, `opencode`. Reconocidos sin
  realizar (rechazo con remisión a GENESIS §4): `openclaw`, `hermes` — para
  Μ=3, usar la bestia.
- La fuente debe pasar `velar`; eje fuera del dominio del target ⟹ fallo,
  nunca degradación silenciosa. Μ=3 no proyecta a ninguno de los tres.
- Agente → codex colapsa a skill; el colapso queda declarado en el sello.
- Sin `--aplicar`: emisión a `_emision/{target}/` (gitignored, efímera).
  Con `--aplicar`: instala en `~/.claude/{agents,skills}/`,
  `~/.codex/skills/`, `~/.config/opencode/{agents,skills}/`.
- Toda emisión es determinista y termina en `<!-- kora:sello ... -->` con
  fuente, hash sha256, fidelidad por eje y pérdidas con razón.

## Koraficación

Contrato de producción de conocimiento (`ley/4`); no aplica a cuerpos
agénticos ni a la ley.

| Obligación | Criterio |
|---|---|
| FS = 100% | Todo hecho de la fuente preservado o comprimido; un `omitido` sin recorte declarado falla |
| Hecho `agregado` | Inventar un hecho hace fallar la koraficación por sí solo |
| CR > 1,5 | Objetivo; CR < 1,5 solo con FS=100% + sin grasa + superficie válida |
| Telegrafización T1-T7 | DEBE para el producto korificado (cuerpos en general: DEBERIA, `ley/2` §10) |
| Superficie | Sin labelese, frases mecánicas, headings-campo ni headings truncados |
| Procedencia | `fuente:` declara origen; hash `sha256:` si la fuente es externa |

`velar` mecaniza la forma del resultado, no la verdad del contenido: la
fidelidad es obligación declarada del productor contra la fuente.

## Deudas confesadas

Sin ingesta inversa (`Lift`), sin targets openclaw/hermes, sin verificación
coalgebraica de FSM, sin staging de directorios (el estado `borrador`
in-place es la antesala), sin migración masiva: el corpus de la bestia migra
artefacto por artefacto, con URN preservado y `sha256` de la fuente en
`fuente:`. Registro completo: GENESIS §4.

## Recetas

1. Skill nueva: crear `SKILL.md` con `estado: borrador` → `velar --estricto`
   → `ciclo <urn> activo` → `transmutar --urn <urn> --target claude-code
   --aplicar`.
2. Conocimiento korificado: producir bajo `ley/4` → `velar --estricto` →
   `ciclo <urn> publicado`.
3. Cargar KORA entera a un LLM: `python3 kora.py ley`.
4. Jubilar: `ciclo <urn> deprecado` — el URN sigue resolviendo.
5. Traer un artefacto de la bestia: reescribir al shape pneuma con URN
   preservado y `sha256` del original en `fuente:` (patrón de las semillas).
