---
urn: urn:kora:kb:guia-rapida-pneuma
nombre: guia-rapida-pneuma
version: 1.3.1
estado: publicado
descripcion: "Guía rápida de KORA pneuma — qué es, qué alberga, qué garantiza, los seis gestos, el shape, las leyes que velar cobra, lifecycle, transmutación, koraficación y deudas."
fuente: "Producida bajo ley/4. v1.0.0 (2026-06-12): korificación de la guía de génesis sobre ley/0..4, GENESIS.md y kora.py al commit 4d44bfc. v1.1.0 (2026-06-14): añade el mapa de corpus albergados y la receta de síntesis tras la primera migración mayor (categorial, OPM, personas, cluster salud) y la síntesis steve-jobs; hechos derivados de los commits 0bf6aad..fa89bef y del censo vigente. v1.1.1 (2026-06-14): completa la enumeración de §Shape con los campos opcionales agénticos (conocimiento/componible/estados), que ley/2 §3 define pero la guía omitía; corrige una incompletitud que podía inducir a creer que componible no es campo válido. v1.2.0 (2026-06-15): refleja las capacidades de la sesión 2026-06-15 — el sello porta `contrato-conocimiento` (ley/3 §5 r6), el patrón de conocimiento web (receta 7), el reporte `censo --huerfanos` (receta 8) y la deuda deep-opm-pro→pneuma tras pneuma tomar la posta de la SSOT OPM. v1.2.1 (2026-06-22): retira `polymath` de la lista de personas (agente retirado; su único valor no-redundante se absorbió en `mente-omega`) y refleja la fusión analista-redes+constructor-tableros→apoyo-decision-sanitaria (evaluación funcional). Fuente interna al repo, sin hash externo. v1.2.2 (2026-07-06): tabla de gestos incorpora el modo --paridad de transmutar (ley/3 v1.4.0 §9.1, paridad de despliegue). v1.3.0 (2026-07-12): sincroniza openclaw realizado y T-codex-pneuma-v2, rutas oficiales, custom agents, paridad completa y despliegue solo de activos (ley/3 v2.0.0). v1.3.1 (2026-07-13): elimina recuentos y estimaciones volátiles; inventario, tamaño y checks se consultan bajo demanda con los gestos vivos."
autor: FS
creado: 2026-06-12
lang: es
tags: [pneuma, guia-rapida, gestos, shape, vector, transmutacion, koraficacion, lifecycle, migracion, corpus]
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
La ley entera se obtiene bajo demanda con `kora.py ley`: KORA completa cabe en
un contexto LLM. El alma del sistema: [Alma de KORA](urn:kora:kb:alma-de-kora).

## Qué alberga pneuma hoy

Alberga corpus reales migrados de la bestia, artefacto por artefacto. Familias
presentes (inventario vivo:
`python3 kora.py censo`):

- **Categorial** — Formal Layer (`cat-foundations`, `cat-agent-coalgebra`) +
  el corpus ICAS-BoK; lo consume `cat-thinking`.
- **OPM/Forja ES** — SSOT de modelado: núcleo ISO 19450, OPD, OPL, manual
  metodológico, reglas estrictas, specs forja OPD/OPL, puente categorial;
  la consumen la skill `modelamiento-opm` y la persona `dov-dori`.
- **Personas** — razonamiento (`mente-omega`), modelado
  (`dov-dori`), ejecución y organización (`steipete`+`ship-discipline`,
  `allan-kelly`+`cell-design`), diseño (`steve-jobs` + canon + fibras de
  superficie agéntica/web-AI/salud).
- **Salud** — cluster consolidado con fronteras limpias: `salubrista`
  (macro/meso), `medico-hospitalista` (micro asistencial), `urgenciologo`
  (urgencias adultos) + skills operativas + corpus salubrista, redes, HODOM
  y med-emergencia.

URN idénticos a la bestia, que sigue autoritativa para lo no migrado.

## Garantías

| Garantía | Mecanismo |
|---|---|
| Identidad ontológica | Vector PMI×LFS + 5 leyes inter-eje, mecanizadas en `velar` |
| Nombre verdadero | URN sin versión; resuelve incluso retirado el artefacto |
| Coherencia | `velar` ejecuta el registro vigente de checks; el censo es derivado, jamás autoridad |
| Proyección honesta | Sello inline en cada emisión: hash, fidelidad por eje, pérdidas con razón |
| Lifecycle digno | Solo hacia adelante; promoción gateada por `velar`; muertos siguen resolviendo |
| Producción con verdad | Koraficación: FS=100%, hechos inventados = fallo (`ley/4`) |

## Los seis gestos

| Comando | Función |
|---|---|
| `python3 kora.py censo [--json] [--escribir]` | Catálogo derivado del filesystem |
| `python3 kora.py nombre <urn>` | Resolver URN — también deprecados y retirados |
| `python3 kora.py velar [--estricto]` | Ejecuta el registro vigente; exit 0 coherente, 1 con fallos |
| `python3 kora.py transmutar --urn U --target T [--stdout\|--aplicar]` | Proyección funtorial con sello |
| `python3 kora.py transmutar --paridad [--urn U] [--target T]` | Completitud y paridad fuente↔emisión↔instalación: sin-emisión/fiel/desviada/no-instalada (ley/3 §9.1) |
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
`sigma` (5 componentes), `arnes`, `forma`, `herramientas`, `targets`;
opcionales agénticos: `conocimiento` (URNs `kb`), `componible` (URNs
`artefacto`) y `estados` (plan declarativo). Conocimiento agrega:
`familia` ∈ {`nota`, `fuente`, `bok`}. Relaciones opcionales para todo
tipo: `cita`, `depende`, `reemplaza`, `refina`.

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
`publicado` o `activo` rechaza si el corpus completo no pasa `velar`.
`transmutar --aplicar` exige `estado: activo`. Retirado no se reactiva: se
emite artefacto nuevo con `reemplaza`.

## Transmutación

- Targets realizados: `claude-code`, `codex`, `opencode`, `openclaw`.
  Reconocido sin realizar (rechazo con remisión a GENESIS §4): `hermes`.
- La fuente debe pasar `velar` y declarar el target; eje fuera del dominio
  del target ⟹ fallo, nunca degradación silenciosa. Μ=3 encuentra hogar pleno
  en `openclaw`.
- Codex v2 emite skills a `skills/{nombre}/SKILL.md` y agentes como custom
  agents TOML. Una persona dual-mode emite ambos: TOML para delegación y skill
  de invocación explícita para encarnación; no fija modelo.
- Sin `--aplicar`: emisión a `_emision/{target}/` (gitignored, efímera).
  Con `--aplicar`: instala en `~/.claude/{agents,skills}/`,
  `~/.agents/skills/` + `~/.codex/agents/`,
  `~/.config/opencode/{agents,skills}/` o el workspace/skill OpenClaw.
- Toda emisión es determinista y termina en `<!-- kora:sello ... -->` con
  fuente, hash sha256, fidelidad por eje, pérdidas con razón y —si el artefacto
  declara `conocimiento`/`componible`— un bloque `contrato-conocimiento:` con el
  ancla al repo central y la regla de derivación URN→path (`ley/3 §5 r6`); el
  path es función pura del URN, no se hornea.

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

Sin ingesta inversa (`Lift`), sin target hermes, sin verificación
coalgebraica de FSM, sin staging de directorios (el estado `borrador`
in-place es la antesala). La migración es **por demanda**, no masiva
(GENESIS: pneuma se gana el corpus, no lo hereda por decreto): artefacto por
artefacto, con URN preservado y `sha256` de la fuente en `fuente:`. Ya
encarnaron los corpus mayores (ver §Qué alberga pneuma hoy); el resto sigue
en la bestia. Registro completo: GENESIS §4. La SSOT OPM ya la autora pneuma
(tomó la posta, `regimen-de-ley`); deuda de coordinación: deep-opm-pro debe
pasar a consumirla desde pneuma.

## Recetas

1. Skill nueva: crear `SKILL.md` con `estado: borrador` → `velar --estricto`
   → `ciclo <urn> activo` → `transmutar --urn <urn> --target codex
   --aplicar`.
2. Conocimiento korificado: producir bajo `ley/4` → `velar --estricto` →
   `ciclo <urn> publicado`.
3. Cargar KORA entera a un LLM: `python3 kora.py ley`.
4. Jubilar: `ciclo <urn> deprecado` — el URN sigue resolviendo.
5. Traer un artefacto de la bestia (byte-fiel): reescribir al shape pneuma
   con URN preservado, cuerpo idéntico verificado con diff y `sha256` del
   original en `fuente:` (patrón de las semillas y de la migración mayor).
6. Sintetizar una versión superior desde varias fuentes (NO byte-fiel):
   destilar lo compartido a un canon, dejar lo específico en fibras que
   `depende`/`refina` el canon, emitir el actor que lo encarna. `fuente:`
   declara que no es byte-fiel, el `sha256` de cada origen y la decisión de
   diseño. Verificar completitud y no-redundancia antes de promover (patrón
   de `steve-jobs`).
7. Enlazar conocimiento web: crear un kb familia `fuente` cuyo cuerpo apunta a
   la URL canónica viva (sin copiar el contenido); `fuente:` declara la URL, sin
   `sha256` porque es viva. El agéntico lo declara en `conocimiento` (patrón
   `urn:dev:kb:jointjs-docs`).
8. Auditar conocimiento inalcanzable: `python3 kora.py censo --huerfanos`
   reporta kb publicado que ninguna arista de consumo alcanza (informativo, no
   check; las raíces de consumo directo no son huérfanos reales).
