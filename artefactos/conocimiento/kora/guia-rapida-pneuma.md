---
urn: urn:kora:kb:guia-rapida-pneuma
nombre: guia-rapida-pneuma
version: 1.8.1
estado: publicado
descripcion: "Guía rápida de KORA pneuma — qué es, qué alberga, qué garantiza, los seis gestos, el shape, las leyes que velar cobra, lifecycle, transmutación, koraficación y deudas."
fuente: "Producida bajo ley/4. v1.0.0 (2026-06-12): korificación de la guía de génesis sobre ley/0..4, GENESIS.md y kora.py al commit 4d44bfc. v1.1.0 (2026-06-14): añade el mapa de corpus albergados y la receta de síntesis tras la primera migración mayor (categorial, OPM, personas, cluster salud) y la síntesis steve-jobs; hechos derivados de los commits 0bf6aad..fa89bef y del censo vigente. v1.1.1 (2026-06-14): completa la enumeración de §Shape con los campos opcionales agénticos (conocimiento/componible/estados), que ley/2 §3 define pero la guía omitía; corrige una incompletitud que podía inducir a creer que componible no es campo válido. v1.2.0 (2026-06-15): refleja las capacidades de la sesión 2026-06-15 — el sello porta `contrato-conocimiento` (ley/3 §5 r6), el patrón de conocimiento web (receta 7), el reporte `censo --huerfanos` (receta 8) y la deuda deep-opm-pro→pneuma tras pneuma tomar la posta de la SSOT OPM. v1.2.1 (2026-06-22): retira `polymath` de la lista de personas (agente retirado; su único valor no-redundante se absorbió en `mente-omega`) y refleja la fusión analista-redes+constructor-tableros→apoyo-decision-sanitaria (evaluación funcional). Fuente interna al repo, sin hash externo. v1.2.2 (2026-07-06): tabla de gestos incorpora el modo --paridad de transmutar (ley/3 v1.4.0 §9.1, paridad de despliegue). v1.3.0 (2026-07-12): sincroniza openclaw realizado y T-codex-pneuma-v2, rutas oficiales, custom agents, paridad completa y despliegue solo de activos (ley/3 v2.0.0). v1.3.1 (2026-07-13): elimina recuentos y estimaciones volátiles; inventario, tamaño y checks se consultan bajo demanda con los gestos vivos. v1.4.0 (2026-07-16): explicita la frontera `herramientas` de Codex y registra `scaffold-repo` como capacidad Codex desplegable (ley/3 v2.1.0). v1.5.0 (2026-07-16): sincroniza ley/3 v2.3.0: fidelidad separada para campos no reticulares, resolución URN por censo, congruencia con el generador incluyendo sidecars/referencias y guard de la colisión personal Codex→managed OpenClaw. v1.5.1 corrige el estatuto categorial del gesto: proyección coreflectiva de firmas seguida por emisión determinista. v1.6.0 (2026-07-18): incorpora semántica operacional, fidelidad contravariante, gate de promoción sobre el destino y contrato formal de ingeniería agéntica. v1.7.0 (2026-08-09): reemplaza inventarios temporales de corpus y targets por resolución viva desde censo y ley/3; incorpora los namespaces vigentes sin persistir conteos. v1.8.0 (2026-08-09): separa checks cotidianos de diagnósticos derivados, retira la cardinalidad mínima de tags y reduce el recorrido normal a validación de fuente más transmutación focal. v1.8.1 (2026-08-10): incorpora la paridad project-level y el filtrado de unidades esperadas por alcance."
autor: FS
creado: 2026-06-12
lang: es
tags: [pneuma, guia-rapida, gestos, shape, vector, transmutacion, koraficacion, lifecycle, migracion, corpus]
cita: [urn:kora:kb:alma-de-kora]
familia: nota
---
# Guía rápida de KORA pneuma

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

## Cómo recorrer el corpus

El inventario vivo se obtiene con `python3 kora.py censo`; esta guía no
persiste conteos ni listas de artefactos. Los namespaces canónicos agrupan:

- `kora`: ley explicada, semántica operacional y gobierno del propio sistema.
- `dev`: ingeniería de software y trabajo agéntico.
- `fxsl`: modelamiento, pensamiento, personas y colaboración humano-agente.
- `salud`: conocimiento y capacidades clínicas, sanitarias y de red.
- `gn`: conocimiento institucional y operacional de Gobierno Regional.
- `openclaw-fleet`: conocimiento del runtime y de su operación gobernada.

Cada objeto se resuelve por URN. La carpeta orienta; el frontmatter y el censo
determinan identidad, tipo, lifecycle y relaciones.

## Garantías

| Garantía | Mecanismo |
|---|---|
| Identidad ontológica | Vector PMI×LFS + 5 leyes inter-eje, mecanizadas en `velar` |
| Nombre verdadero | URN sin versión; resuelve incluso retirado el artefacto |
| Coherencia | `velar` ejecuta el registro vigente de checks; el censo es derivado, jamás autoridad |
| Proyección honesta | Sello inline: hash, fidelidad por eje/campo y pérdidas con razón; congruencia byte a byte con el generador |
| Lifecycle digno | Solo hacia adelante; promoción gateada por checks de fuente y dignidad focal del estado destino; muertos siguen resolviendo |
| Producción con verdad | Koraficación: FS=100%, hechos inventados = fallo (`ley/4`) |

## Los seis gestos

| Comando | Función |
|---|---|
| `python3 kora.py censo [--json] [--escribir]` | Catálogo derivado del filesystem |
| `python3 kora.py nombre <urn>` | Resolver URN — también deprecados y retirados |
| `python3 kora.py velar [--estricto]` | Ejecuta el registro vigente; exit 0 coherente, 1 con fallos |
| `python3 kora.py transmutar --urn U --target T [--stdout\|--aplicar]` | Proyección coreflectiva de firma + emisión determinista con sello |
| `python3 kora.py transmutar --paridad [--urn U] [--target T] [--proyecto PATH]` | Completitud activo→emisión y paridad emisión↔instalación del nivel elegido: sin-emisión/fiel/desviada/no-instalada (ley/3 §9.1) |
| `python3 kora.py ciclo <urn> <estado>` | Transición de lifecycle, solo adelante |
| `python3 kora.py ley` | ALMA + ley/0..4 a stdout |

El recorrido cotidiano es:

```bash
python3 kora.py velar
python3 kora.py transmutar --urn <urn> --target <target>
python3 kora.py transmutar --paridad --urn <urn> --target <target>
```

`velar --estricto` y la paridad sin filtros son auditorías optativas de
derivados o múltiples superficies, no gates de una edición rutinaria.

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
`artefacto`, candidatos, no composición probada) y `estados` (etiquetas de
workflow, no FSM). `herramientas` declara capacidades fuente; el enforcement
depende del target. Conocimiento agrega:
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
- `--estricto` agrega `descripcion` y `fuente` no vacías para artefactos
  activos/publicados, más congruencia exacta de emisiones. `tags` es metadata
  opcional, sin cardinalidad normativa.

## Lifecycle

| Tipo | Cadena |
|---|---|
| conocimiento | `borrador → publicado → deprecado` |
| agéntico | `borrador → activo → deprecado → retirado` |

Saltos hacia adelante válidos; inversas inválidas siempre. `ciclo` hacia
`publicado` o `activo` rechaza si el corpus completo no pasa
`velar` o si el estado destino no satisface
`publicacion-digna`.
`transmutar --aplicar` exige `estado: activo`. Retirado no se reactiva: se
emite artefacto nuevo con `reemplaza`.

Las cadenas son categorías delgadas, pero el comando es parcial sobre
snapshots: jubilar no exige el gate de promoción. En el dominio común, un
camino compuesto y el salto directo dejan los mismos bytes finales.

## Frontera formal agéntica

Un artefacto KORA es `Spec`, no conducta por decreto. Llamarlo coálgebra exige
`I`, `O`, `U`, mónada `M` y `step`; llamarlo componible exige puertos, wiring,
semántica y efectos compatibles; llamarlo seguro exige autoridad runtime
efectiva e invariante cerrado. El sello y la paridad prueban materia, no
bisimulación. Contrato completo:
`urn:kora:kb:cat-contrato-ingenieria-agentica`.

## Transmutación

- Los targets, sus matrices y su estado de realización vigentes viven en
  `ley/3` y `kora.py`; no se duplican en esta guía.
- La fuente debe pasar `velar` y declarar el target; eje fuera del dominio
  del target ⟹ fallo, nunca degradación silenciosa.
- Codex v2 emite skills a `skills/{nombre}/SKILL.md` y agentes como custom
  agents TOML. Una persona dual-mode emite ambos: TOML para delegación y skill
  de invocación explícita para encarnación; no fija modelo.
- Codex permite estrechar sandbox, MCP y skills en un custom agent, pero no una
  allowlist exacta de built-ins por artefacto; además, las overrides vivas del
  padre prevalecen. El sello conserva la lista KORA y declara
  `fidelidad-campos: herramientas:partial`; no finge enforcement inexistente.
- Sin `--aplicar`: emisión a `_emision/{target}/` (gitignored, efímera).
  Con `--aplicar`: instala solo en el destino y bajo las gates definidos por
  `ley/3`; consulta el target vivo antes de operar sobre un runtime.
- Codex y OpenClaw comparten `~/.agents/skills`; como OpenClaw la prioriza
  sobre `~/.openclaw/skills`, KORA no instala debajo un homónimo managed. Las
  sombras agrupadas o por workspace se resuelven en el deploy por agente.
- Todo factor doctrinal es determinista y termina en `<!-- kora:sello ... -->`
  con fuente, hash, fidelidad y pérdidas. Sidecars y `referencias/` quedan
  certificados por congruencia del producto. Si declara
  `conocimiento`/`componible`, `contrato-conocimiento:` resuelve cada URN por
  `kora.py nombre` o búsqueda exacta y única; nunca inventa el path desde el id.

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

Sin ingesta inversa (`Lift`), sin interpretación source→runtime ni testigos
coalgebraicos por artefacto, sin staging de directorios (el estado `borrador`
in-place es la antesala). La migración es **por demanda**, no masiva
(GENESIS: pneuma se gana el corpus, no lo hereda por decreto): artefacto por
artefacto, con URN preservado y `sha256` de la fuente en `fuente:`. Ya
encarnaron los corpus mayores (ver §Qué alberga pneuma hoy); el resto sigue
en la bestia. Registro completo: GENESIS §4. La SSOT OPM ya la autora pneuma
(tomó la posta, `regimen-de-ley`); deuda de coordinación: deep-opm-pro debe
pasar a consumirla desde pneuma.

## Recetas

1. Skill nueva: crear `SKILL.md` con `estado: borrador` → `velar`
   → `ciclo <urn> activo` → `transmutar --urn <urn> --target codex
   --aplicar`.
2. Conocimiento korificado: producir bajo `ley/4` → `velar` →
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
