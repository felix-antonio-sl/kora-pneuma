# KORA/Forma — ley pneuma v1.12.0

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
| `tags` | no | lista | metadata opcional, sin cardinalidad normativa |
| `cita` | no | lista URNs | relación libre; admite ciclos (§9) |
| `depende` | no | lista URNs | aristas de DAG (§9); en una fuente agéntica, los destinos agénticos son requisitos de disponibilidad runtime conforme a ley/3 §7.6 |
| `reemplaza` | no | lista URNs | aristas de DAG temporal; target muerto (§9) |
| `refina` | no | lista URNs | aristas de DAG (§9) |

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
| `herramientas` | sí | lista | capacidades fuente declaradas; su enforcement es específico del target; PUEDE ser `[]` solo si `forma` = `habilidad` |
| `targets` | no | lista no vacía | allowlist explícita de compatibilidad mantenida; ausente = especificación agnóstica al runtime (ley/3 §2) |
| `conocimiento` | no | lista URNs `kb` | conocimiento permitido |
| `componible` | no | lista URNs `artefacto` | candidatos declarados de composición; la arista no prueba interfaces ni composición semántica |
| `estados` | no | lista | etiquetas ordenadas de workflow; no son FSM ni estado coalgebraico |
| `alcance` | no | enum | `usuario\|proyecto\|ambos`; ausente = `ambos`. Gobierna qué destino de `--aplicar` admite el artefacto (instalación user-general vs proyecto). Lo respeta y valida el gesto de transmutación (ley/3 §7). Es un atributo del artefacto, no del runtime: ortogonal a `targets` |

Renombres pneuma sobre la bestia: `agente-propiamente-tal` → `agente`,
`agente-plataforma` → `plataforma`. Estos campos NO DEBEN aparecer en un
artefacto de conocimiento (serían claves no permitidas para su tipo).

`targets` no forma parte de la identidad ni del modelo conductual. Si está
presente, restringe la transmutación a los destinos enumerados y declara que
esa compatibilidad se mantiene. Si está ausente, la fuente permanece agnóstica:
Codex es solo la selección operacional ordinaria y cualquier otro target
realizado requiere selección explícita conforme a `ley/3`. Ninguna de las dos
formas prueba instalación ni conducta runtime.

### 3.1 Frontera semántica agéntica

El shape agéntico es una especificación declarativa y fuente de compilación.
No constituye por sí solo un modelo de conducta.

1. `vector`, `sigma`, `arnes` y `forma` clasifican y gobiernan. No definen
   conjuntos de entradas, salidas o estados ni una transición.
2. `estados` no declara eventos, aristas, guards, acciones ni estado inicial;
   por tanto no es una máquina de estados ni una coálgebra.
3. `depende` y `componible` no son sinónimos. Una dependencia agéntica exige
   disponibilidad del requisito en los targets compatibles que la realizan;
   no prueba invocación ni composición. `componible` genera sólo un grafo de
   **candidatos**: incluso su categoría libre de caminos compone declaraciones,
   no agentes.
4. `herramientas` es un subconjunto de capacidades declaradas. Probar
   least-privilege exige comparar ese conjunto con la autoridad efectiva del
   runtime bajo todos los overrides incluidos en el alcance.
5. Un sello fresco o una instalación paritaria prueban procedencia e igualdad
   material; no bisimulación, safety ni preservación conductual.

Los testigos mínimos para promover cada afirmación —`I`, `O`, `U`, mónada
`M`, transición, lifting de relaciones, interfaces de wiring, álgebra de
composición, capacidades efectivas e interpretación runtime— viven en
`urn:kora:kb:cat-contrato-ingenieria-agentica`.

No se añaden campos conductuales vacíos al frontmatter. Una futura extensión
deberá nacer de un caso operacional completo y referenciar un testigo
versionado por URN; el shape plano no debe fingir que serializa una semántica
que todavía no existe.

## 4. Metadata opcional de conocimiento

| Clave | Oblig. | Tipo | Notas |
|---|---|---|---|
| `familia` | no | enum | metadata heredada `nota\|fuente\|bok`; sin efecto operacional |

- `nota` — etiqueta descriptiva general.
- `fuente` — etiqueta histórica; no prueba procedencia ni fidelidad.
- `bok` — etiqueta histórica de corpus extendido.

`familia` puede conservarse por compatibilidad, pero no decide tipo, lifecycle,
koraficación, resolución ni consumo. No se reemplaza por otro enum. La
procedencia vive en `fuente:` y la ley `spec` **NO existe como artefacto**: la
ley vive en `ley/` (constitución §4).

## 5. Derivación de tipo

No hay campo `tipo`: el tipo no se declara, **se es**. Regla mecanizada:

| Condición | Tipo | Régimen URN |
|---|---|---|
| `vector` presente y `forma` = `habilidad` | skill | `artefacto` |
| `vector` presente y `forma` ∈ {`subagente`, `agente`, `plataforma`} | agente | `artefacto` |
| `vector` ausente | conocimiento | `kb` |

Reglas:

1. `vector` presente sin `forma`: ERROR (`forma-valida`).
2. Coherencias mecanizadas: régimen URN ⟺ tipo; zona del filesystem ⟺ tipo
   (§6); namespace del URN ⟺ primer subdirectorio bajo la zona.

## 6. Zonas del filesystem

```text
artefactos/
├── conocimiento/{ns}/{nombre}.md
├── agentes/{ns}/{nombre}.md
└── skills/{ns}/{nombre}/
    ├── SKILL.md
    ├── referencias/                (opcional)
    ├── scripts/                    (opcional)
    └── agents/openai.yaml          (opcional, metadata Codex)
```

1. El nombre de archivo DEBE ser `SKILL.md` para skills (cada skill en su
   propio directorio) y `{nombre}.md` para agentes y conocimiento.
2. El namespace del URN DEBE coincidir con el primer subdirectorio bajo la
   zona. Check: `lugar-coincide`.
3. `agents/openai.yaml` PUEDE existir solo como sidecar de metadata del target
   Codex. No es un artefacto, no amplía el shape ni porta URN: pertenece al
   mismo producto cerrado que `SKILL.md` y `ley/3` gobierna su transporte.
4. `referencias/` y `scripts/` son fibras opcionales del mismo producto, no
   artefactos ni campos del shape. `scripts/` contiene utilidades ejecutables o
   invocables por intérprete que la skill usa de forma determinista. Al
   transmutar, ambas fibras exigen directorios reales con descendientes
   regulares y conservan sus nombres y bytes; no se siguen enlaces.

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
4. La DEMOCIÓN **NO ESTÁ PERMITIDA**: es una decisión de lifecycle para evitar
   pérdida ambigua de estructura y preservar trazabilidad, no la conclusión de
   un teorema categorial. El camino legal es deprecar el artefacto y emitir uno
   nuevo con `reemplaza`.

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

## 9. Relaciones como grafos generadores

Cada campo relacional declara aristas de un dígrafo. No declara identidades,
composiciones ni cierre transitivo.

| Campo | Grafo declarado | Acíclico | Ley adicional |
|---|---|---|---|
| `cita` | aristas libres | no | solo resolubilidad |
| `depende` | DAG | **sí** | ciclo = ERROR |
| `reemplaza` | DAG temporal | **sí** | target DEBE estar `deprecado` o `retirado` |
| `refina` | DAG | **sí** | ciclo = ERROR |

Todo dígrafo `G` genera, si se necesita razonar categorialmente, la categoría
libre de caminos `Path(G)`: los objetos son URNs, las flechas son caminos
finitos, la identidad es el camino vacío y la composición concatena caminos.
El núcleo valida solo las aristas fuente. En los tres DAG, la alcanzabilidad
reflexiva induce un orden parcial; no hace falta materializarlo.

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
4. Ciclos en `depende`, `reemplaza` o `refina`, o target vivo en
   `reemplaza`: check `relaciones-legales`.
5. No se exige cierre transitivo. Si `A → B` y `B → C` están declaradas, el
   camino `A → C` existe en `Path(G)` aunque no haya una arista directa
   `A → C`.

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
4. El cuerpo DEBERIA eliminar superficie sin función actual y preservar toda
   unidad semántica pertinente: condiciones, modalidad, incertidumbre,
   excepciones, fechas, cifras, relaciones y procedencia. No hay telegrafía ni
   umbral de compresión universal. El producto de una koraficación se rige por
   los invariantes y el alcance explícito de `ley/4`.

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
| Fibras `referencias/` y `scripts/` dentro de una skill | §6 r4 | zona mecanizada (`lugar-coincide`); regularidad validada por `transmutar` |
| Rangos del vector | §3 | mecanizado (`vector-en-reticulo`) |
| Leyes inter-eje | ley/1 §4 | mecanizado (`leyes-inter-eje`) |
| Dominio por forma | §7 | mecanizado (`dominio-forma`) |
| Promoción de forma: URN preservado, bump major, sin democión | §7.1 | declarado (el encaje del vector en la nueva forma lo mecaniza `dominio-forma` vía `velar`) |
| Arnés compatible con forma | §8 | mecanizado (`arnes-compatible`) |
| Estado en la cadena del tipo | constitución §8 | mecanizado (`estado-valido`) |
| Referencias resuelven (incluso muertos) | §9 r1 | mecanizado (`referencias-resuelven`) |
| Leyes de relaciones | §9 r2-r5 | mecanizado (`relaciones-legales`) |
| Targets reconocidos, si se declaran | §3, ley/3 §2 | mecanizado (`targets-conocidos`) |
| Publicación digna | con `--estricto`: `descripcion` y `fuente` no vacías en todo artefacto `activo`/`publicado`; `tags` es metadata sin cardinalidad normativa | mecanizado (`publicacion-digna`) |
| Cuerpo subordinado al frontmatter | §10 r3 | declarado |
| Integridad semántica y economía superficial | §10 r4 | declarado |
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

v1.6.0 (2026-07-18): corrige el estatus de las relaciones. El frontmatter
declara grafos generadores, no subcategorías ni posets materializados; la
categoría libre de caminos y el orden por alcanzabilidad se derivan cuando
corresponde. Se explicita que el cierre transitivo no es obligatorio y que la
prohibición de democión es política de lifecycle, no teorema.

v1.7.0 (2026-07-18): precisa la frontera semántica agéntica sin expandir el
shape. `herramientas`, `componible` y `estados` quedan tipados como
declaraciones; coálgebra, composición, enforcement y preservación runtime
requieren testigos externos explícitos.

v1.8.0 (2026-08-09): retira la cardinalidad arbitraria de tres `tags` para
conocimiento publicado. La dignidad conserva solo `descripcion` y `fuente` no
vacías; `tags` vuelve a ser metadata opcional y no un sustituto de calidad.

v1.9.0 (2026-08-11): reconoce `agents/openai.yaml` como sidecar opcional de
metadata Codex dentro de una skill. No agrega campos al shape ni crea un cuarto
tipo de artefacto; `ley/3` lo transporta como factor del producto cerrado.

v1.10.0 (2026-08-13): hace opcionales `familia` y `targets` sin cambiar los
tres tipos ni invalidar fuentes existentes. `familia` queda como metadata
heredada sin efecto operacional. Una fuente agéntica sin `targets` es agnóstica
al runtime; una lista presente sigue siendo allowlist de compatibilidad
mantenida. No se añade ningún enum sustituto.

v1.11.0 (HITL 2026-08-23): tipa el efecto ya expresable de `depende` para
fuentes agénticas: una referencia a conocimiento sigue siendo una relación
semántica, mientras una referencia a otro artefacto agéntico exige su
disponibilidad runtime donde el adaptador la realiza. No demuestra invocación,
wiring ni composición y no altera `componible`. El primer contrato operacional
de ley/3 realiza dependencias de forma habilidad, exige estado activo y target
compatible, y falla cerrado para agentes requeridos.

v1.12.0 (2026-08-24): reconoce `scripts/` como fibra opcional de una skill,
junto a `referencias/`, sin abrir el shape ni crear otro tipo de artefacto.
Ambas permanecen dentro del producto cerrado, conservan nombre y bytes y deben
ser directorios reales con materia regular para transmutarse.
