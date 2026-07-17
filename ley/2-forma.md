# KORA/Forma — ley pneuma v1.5.0

Estrato 2 de la ley. Define cómo se escribe un artefacto: **un solo shape
para los tres tipos**. Todo artefacto consta de exactamente dos capas:
frontmatter (gramática §1, campos §§2-4) y cuerpo (§10).

## 1. La gramática del frontmatter

El frontmatter es un **subconjunto regular de YAML**, cerrado y completo. No
es YAML general: lo que esta gramática no admite, no pertenece al shape.

```text
frontmatter = "---" NL { linea } "---" NL
linea       = vacia | comentario | campo
campo       = clave ":" SP valor [ SP comentario ] NL
clave       = [a-z] { [a-z0-9] | "-" }
valor       = escalar | lista
lista       = "[" [ escalar { "," SP escalar } ] "]"
escalar     = entero | fecha | cadena
fecha       = AAAA "-" MM "-" DD
cadena      = texto-sin-comillas | '"' texto '"'
```

Reglas duras:

1. Cada línea de contenido es `clave: valor`. NO DEBE haber anidamiento,
   bloques multilínea (`|`, `>`) ni objetos `{}`.
2. Claves: ASCII `[a-z][a-z0-9-]*`, sin tildes.
3. Valores: escalar (string sin comillas o con comillas dobles, entero, fecha
   `YYYY-MM-DD`) o lista inline `[a, b, c]` de escalares.
4. Comentarios `# ...` PUEDEN ir en línea propia o al final de un campo; las
   líneas en blanco están permitidas.
5. Clave duplicada: ERROR de parse.
6. Clave desconocida (fuera de §§2-4): ERROR en `velar`. El sobre es
   **cerrado**; no hay `extensions`.

Correcto:

```yaml
---
urn: urn:kora:artefacto:mente-omega
nombre: mente-omega
version: 1.0.1
estado: activo
vector: [2, 0, 2, 0, 1]   # [pi, mu, xi, lambda, phi]
---
```

Incorrecto:

```yaml
---
vector:
  pi: 2              # anidamiento: prohibido
descripcion: |       # bloque multilínea: prohibido
  texto largo
urn: urn:a:kb:x
urn: urn:a:kb:y      # clave duplicada: error de parse
Extensiones: {}      # mayúscula y clave desconocida: error
---
```

Rationale: la bestia cargaba un parser YAML completo para leer claves planas.
Pneuma cierra la gramática para que el núcleo la parsee con stdlib pura y
para que ningún artefacto esconda estructura fuera de la ley.

## 2. Campos comunes (todos los tipos)

| Clave | Oblig. | Tipo | Notas |
|---|---|---|---|
| `urn` | sí | string | regex de constitución §7; SIN versión embebida |
| `nombre` | sí | string | slug ASCII seguro (§2.1) |
| `version` | sí | semver `X.Y.Z` | fuera del URN |
| `estado` | sí | enum | según la cadena del tipo (constitución §8) |
| `descripcion` | sí | string 1 línea | disparador y uso |
| `fuente` | sí | string | procedencia; si viene de la bestia DEBE incluir `sha256:<hex>` del archivo fuente original |
| `autor` | no | string | |
| `creado` | no | `YYYY-MM-DD` | |
| `lang` | no | `es` \| `en` | default `es` |
| `tags` | cond. | lista | obligatoria con ≥3 ítems para conocimiento `publicado`; opcional en el resto |
| `cita` | no | lista URNs | relación libre; admite ciclos (§9) |
| `depende` | no | lista URNs | DAG estricto (§9) |
| `reemplaza` | no | lista URNs | poset estricto; target muerto (§9) |
| `refina` | no | lista URNs | acíclico (§9) |

### 2.1 Nombre material

El `nombre` de **todo artefacto**, sin distinción de tipo, DEBE cumplir la
regex:

```text
^[a-z0-9]+(?:-[a-z0-9]+)*$
```

Es un slug ASCII minúsculo formado por segmentos alfanuméricos no vacíos
separados por un solo guion. Por construcción es un único componente de ruta:
no admite espacios, controles, puntos, separadores, NUL, `.` ni `..`.
`forma-valida` mecaniza esta gramática antes de que cualquier gesto derive una
ruta; `lugar-coincide` verifica después su correspondencia con el filesystem
(§6).

El nombre localiza una ruta candidata, pero **no prueba su propiedad**. Cuando
esa ruta ya existe en una instalación, la atribución a KORA se demuestra por
el sello `(URN,target)` conforme a `ley/3 §7`.

## 3. Campos agénticos (agentes y skills)

| Clave | Oblig. | Tipo | Notas |
|---|---|---|---|
| `vector` | sí | lista 5 enteros | `[pi, mu, xi, lambda, phi]`; rangos: `pi` 0..3, `mu` 0..3, `xi` 0..4, `lambda` 0..3, `phi` 0..4 |
| `sigma` | sí | lista 5 enteros | `[safety, fairness, transparency, accountability, sustainability]`, cada uno 0..3 |
| `arnes` | sí | enum | `utilidad\|disciplina\|delegado\|persona\|orquestador\|servicio\|arquetipo` |
| `forma` | sí | enum | `habilidad\|subagente\|agente\|plataforma` |
| `herramientas` | sí | lista | herramientas/permisos; PUEDE ser `[]` solo si `forma` = `habilidad` |
| `targets` | sí | lista no vacía | subconjunto de `{claude-code, codex, opencode, openclaw, hermes}` |
| `conocimiento` | no | lista URNs `kb` | conocimiento permitido |
| `componible` | no | lista URNs `artefacto` | artefactos componibles |
| `estados` | no | lista | plan declarativo simple (sin FSM mecanizado) |
| `alcance` | no | enum | `usuario\|proyecto\|ambos`; ausente = `ambos`. Gobierna qué destino de `--aplicar` admite el artefacto (instalación user-general vs proyecto). Lo respeta y valida el gesto de transmutación (ley/3 §7). Es un atributo del artefacto, no del runtime: ortogonal a `targets` |

Renombres pneuma sobre la bestia: `agente-propiamente-tal` → `agente`,
`agente-plataforma` → `plataforma`. Estos campos NO DEBEN aparecer en un
artefacto de conocimiento (serían claves no permitidas para su tipo).

## 4. Campo de conocimiento

| Clave | Oblig. | Tipo | Notas |
|---|---|---|---|
| `familia` | sí | enum | `nota\|fuente\|bok` |

- `nota` — descriptiva, catch-all: lo que se lee como contexto general.
- `fuente` — material fuente preservado para trazabilidad.
- `bok` — body of knowledge: corpus extendido.

La familia `spec` **NO existe como artefacto**: la ley vive en `ley/`
(constitución §4).

## 5. Derivación de tipo

No hay campo `tipo`: el tipo no se declara, **se es**. Regla mecanizada:

| Condición | Tipo | Régimen URN |
|---|---|---|
| `vector` presente y `forma` = `habilidad` | skill | `artefacto` |
| `vector` presente y `forma` ∈ {`subagente`, `agente`, `plataforma`} | agente | `artefacto` |
| `vector` ausente | conocimiento (requiere `familia`) | `kb` |

Reglas:

1. `vector` presente sin `forma`: ERROR (`forma-valida`).
2. Coherencias mecanizadas: régimen URN ⟺ tipo; zona del filesystem ⟺ tipo
   (§6); namespace del URN ⟺ primer subdirectorio bajo la zona.

## 6. Zonas del filesystem

```text
artefactos/
├── conocimiento/{ns}/{nombre}.md
├── agentes/{ns}/{nombre}.md
└── skills/{ns}/{nombre}/SKILL.md    (+ referencias/ opcional)
```

1. El nombre de archivo DEBE ser `SKILL.md` para skills (cada skill en su
   propio directorio) y `{nombre}.md` para agentes y conocimiento.
2. El namespace del URN DEBE coincidir con el primer subdirectorio bajo la
   zona. Check: `lugar-coincide`.

Correcto: `artefactos/agentes/dev/polymath.md` ⟷ `urn:dev:artefacto:polymath`.
Incorrecto: `artefactos/agentes/kora/polymath.md` con URN de namespace `dev`.

## 7. Dominios de proyección por forma

El vector DEBE caer dentro del dominio de su `forma`. Check: `dominio-forma`.

| `forma` | `pi` | `mu` | `xi` | `lambda` | `phi` |
|---|---|---|---|---|---|
| `habilidad` | {1,2} | {0,1} | {1,2} | 0 | 1 |
| `subagente` | {1,2,3} | {0,1,2} | {1,2,3} | {0,1} | {1,2} |
| `agente` | {2,3} | {2,3} | {2,3,4} | {0,1,2} | {1,2,3} |
| `plataforma` | {2,3} | 3 | {3,4} | {1,2,3} | {1,2,3} |

Rationale: la forma es el cuerpo operacional del objeto; un cuerpo que no
puede sostener el vector (una habilidad con memoria persistente, una
plataforma sin materia ambiental) es una incoherencia, no una variante.

### 7.1 Promoción de forma

Doctrina heredada de la bestia, esencial según ALMA: **"Se nace hacia
arriba."** La promoción de forma sigue la cadena `habilidad → subagente →
agente → plataforma`:

1. La promoción DEBE preservar el URN: asciende el cuerpo, no cambia el
   nombre verdadero.
2. La promoción DEBE bumpear versión **major**.
3. El vector DEBE caber en el dominio de la nueva forma (§7).
4. La DEMOCIÓN **NO ESTÁ PERMITIDA**: descender perdería estructura de forma
   no funtorial, rompiendo trazabilidad. El camino legal es deprecar el
   artefacto y emitir uno nuevo con `reemplaza`.

Pneuma no tiene comando de promoción: la transición se hace editando `forma`
y `version` en la fuente, y el resultado DEBE pasar `velar` (el encaje del
vector lo mecaniza `dominio-forma`; el resto de esta doctrina es declarado).

## 8. Compatibilidad arnés × forma

| `forma` | Arneses válidos |
|---|---|
| `habilidad` | `utilidad`, `disciplina`, `delegado` |
| `subagente` | `delegado`, `persona` |
| `agente` | `persona`, `orquestador` |
| `plataforma` | `orquestador`, `servicio` |

`arquetipo` NO DEBE materializarse: es ERROR en cualquier forma (ley/1
§6.1 r4). Check: `arnes-compatible`.

## 9. Relaciones y sus leyes algebraicas

Cada relación define una subcategoría con leyes propias; la única sin
estructura de orden es `cita`.

| Campo | Estructura | Acíclica | Antisimétrica | Ley adicional |
|---|---|---|---|---|
| `cita` | relación binaria libre | no | no | solo resolubilidad |
| `depende` | DAG estricto | **sí** | irreflexiva | ciclo = ERROR |
| `reemplaza` | poset estricto | **sí** | **sí** | target DEBE estar `deprecado` o `retirado` |
| `refina` | preorden estricto | **sí** | no exigida | ciclo = ERROR |

Reglas:

1. Toda referencia URN — las cuatro relaciones más `conocimiento` y
   `componible` — DEBE resolver en el censo, **incluyendo artefactos
   deprecados y retirados** (dignidad del URN, constitución §9). Check:
   `referencias-resuelven`.
2. `reemplaza` NO DEBE usarse como sinónimo de "menciona": la sucesión es
   orientada en el tiempo. `A reemplaza B` y `B reemplaza A` simultáneos:
   ERROR.
3. `refina` NO DEBE contradecir lo refinado; si lo reemplaza, corresponde
   `reemplaza`.
4. Ciclos en `depende` o `refina`, antisimetría violada o target vivo en
   `reemplaza`: check `relaciones-legales`.

Correcto: `reemplaza: [urn:kora:artefacto:atomize]` donde el target tiene
`estado: retirado`.
Incorrecto: `reemplaza: [urn:kora:artefacto:atomize]` con target `activo` —
no se reemplaza a los vivos.

## 10. El cuerpo

1. Tras el frontmatter, el cuerpo es Markdown libre.
2. El cuerpo DEBE privilegiar estructura recuperable sobre prosa ornamental:
   headings, listas, tablas, definiciones, ejemplos mínimos.
3. El cuerpo NO DEBE contradecir el frontmatter; en conflicto, el frontmatter
   prevalece.
4. La disciplina de compresión de la bestia se hereda como DEBERIA, no DEBE:
   el cuerpo DEBERIA eliminar grasa (introducciones vacías, transiciones,
   hedging) y conservar siempre toda condición, umbral, excepción, fecha,
   cifra o referencia. No hay telegrafía impuesta ni métricas de compresión
   mecanizadas — con una excepción: el producto de una koraficación se rige
   por `ley/4`, donde la disciplina completa es DEBE.

5. Un agente cuyo `arnes` porta `U_phen` (`persona`, `orquestador`,
   `servicio`-persona) DEBERIA portar su `U_phen` —su disposición de
   personalidad— en el cuerpo; su **estructura** la define la KB de persona
   (`urn:kora:kb:aufbau-persona-agente`). La ley señala el **locus** (el cuerpo);
   el KB define la estructura y la skill de autoría la controla. `velar` NO lo
   verifica (forma-no-verdad): es oficio, no check. Funda en la corrección de
   `ley/1 §2` v1.1.0 (la persona vive en `U_phen`, no en el vector).

6. El span de `U_phen` en el cuerpo PUEDE delimitarse con un **centinela
   canónico**, un par de comentarios HTML literales:

   ```text
   <!-- kora:soul -->
   ... el span de U_phen (la voz) ...
   <!-- kora:soul:fin -->
   ```

   Reglas:

   a. El centinela es **opcional** en general; un cuerpo sin él queda
      byte-idéntico (extensión aditiva). Pero los targets que **segregan voz**
      —hoy `openclaw`, cuyo `SOUL.md` es voz separada de la operativa de
      `AGENTS.md`— lo **EXIGEN** para emitir el `SOUL.md` de un `arnes` que porta
      `U_phen` (`ley/3 §7`): el núcleo no segmenta prosa (forma-no-verdad), así
      que el span lo delimita el autor.
   b. El núcleo lo halla por **match literal** (predicado decidible sobre el
      texto), nunca interpretando la prosa. Es el mismo régimen de
      `<!-- kora:sello -->`.
   c. A lo sumo **un** par por cuerpo. Cero pares, o pares desbalanceados o
      múltiples, hacen **fallar la emisión** (no `velar`) en el target que lo
      exige; `velar` NO lo verifica (oficio, validado al emitir por
      `transmutar`).
   d. Los comentarios HTML son **invisibles al renderizar**: el cuerpo viaja
      verbatim al archivo de operativa (transporte de fibra, `ley/3 §1`) con los
      centinelas dentro, sin mutación. La realización de la voz es la KB de
      persona y la skill `urn:kora:artefacto:autoria-de-persona`.

Rationale: la prueba ácida heredada sigue siendo buen criterio editorial — si
al borrar texto cambia solo el tono, sobra; si desaparece un hecho, no se
borra — pero pneuma la quiere como oficio, no como ley mecanizada.

## 11. Validación

| Regla | Detalle | Enforcement |
|---|---|---|
| Gramática y campos del shape | §§1-5: parse, obligatorios por tipo, claves desconocidas, enums, semver | mecanizado (`forma-valida`) |
| `nombre` seguro para todo tipo | §2.1: slug ASCII y componente único de ruta | mecanizado (`forma-valida`) |
| URN: gramática, régimen, unicidad | constitución §7 | mecanizado (`nombre-verdadero`) |
| Zona, namespace y nombre de archivo | §6 | mecanizado (`lugar-coincide`) |
| Rangos del vector | §3 | mecanizado (`vector-en-reticulo`) |
| Leyes inter-eje | ley/1 §4 | mecanizado (`leyes-inter-eje`) |
| Dominio por forma | §7 | mecanizado (`dominio-forma`) |
| Promoción de forma: URN preservado, bump major, sin democión | §7.1 | declarado (el encaje del vector en la nueva forma lo mecaniza `dominio-forma` vía `velar`) |
| Arnés compatible con forma | §8 | mecanizado (`arnes-compatible`) |
| Estado en la cadena del tipo | constitución §8 | mecanizado (`estado-valido`) |
| Referencias resuelven (incluso muertos) | §9 r1 | mecanizado (`referencias-resuelven`) |
| Leyes de relaciones | §9 r2-r4 | mecanizado (`relaciones-legales`) |
| Targets reconocidos | §3, ley/3 §2 | mecanizado (`targets-conocidos`) |
| Publicación digna | con `--estricto`: tags ≥3 en conocimiento `publicado`; `descripcion` y `fuente` no vacías en todo artefacto `activo`/`publicado` | mecanizado (`publicacion-digna`) |
| Cuerpo subordinado al frontmatter | §10 r3 | declarado |
| Compresión sin grasa | §10 r4 | declarado |
| Centinela `kora:soul` bien formado (≤1 par balanceado) | §10 r6 | declarado (validado al emitir por `transmutar`, no por `velar`) |

Sublimado de autoria-spec v2.0.0, md-spec v12.0.0, knowledge-spec v3.0.0 y
spec-md v1.0.0 el 2026-06-11; ver GENESIS.md.

v1.3.0 (HITL 2026-06-30): §10 r5 — `DEBERIA` orientador de `U_phen`-en-el-cuerpo
para arneses con personalidad (locus en la ley, estructura en
`urn:kora:kb:aufbau-persona-agente`, control en la skill de autoría). Sin campo,
sin check, sin eje. Complementa la corrección de `ley/1` §2 v1.1.0. Origen:
panel consenso-deliberativo.

v1.4.0 (HITL 2026-07-01): §10 r6 — centinela canónico opcional
`<!-- kora:soul -->…<!-- kora:soul:fin -->` que delimita el span de `U_phen` en
el cuerpo, para los targets que segregan voz (`openclaw`, `ley/3 §7`). Aditivo:
sin centinela el cuerpo queda byte-idéntico. Predicado literal decidible
(forma-no-verdad: el núcleo no segmenta prosa). Sin campo, sin check; validado al
emitir, no por `velar`. Habilita la realización de `T-openclaw-pneuma-v1`.

v1.5.0 (2026-07-17): §2.1 precisa de forma compatible la gramática de
`nombre` para los tres tipos: slug ASCII minúsculo y componente único de ruta.
`forma-valida` la mecaniza antes de derivar paths; la propiedad de una
instalación homónima sigue siendo una cuestión distinta, demostrada por sello
en `ley/3`.
