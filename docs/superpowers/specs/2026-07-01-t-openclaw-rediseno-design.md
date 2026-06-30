# Rediseño de `T-openclaw-pneuma-v1` — design

Fecha: 2026-07-01. Autor: steipete (encarnado, vía cat-thinking).
Estado: spec aprobada para implementar. Reemplaza el intento revertido en
`8ef7c6e` (Pieza C anclada en Hermes).

> **Por qué este rediseño.** El primer intento modeló openclaw sobre **Hermes**
> (runtime primo de `SOUL.md` monolítico): emitió un `SOUL.md` con el cuerpo
> entero, omitió `AGENTS.md`, pasó `velar` 13/13 + 88 tests y se revirtió. Causa
> raíz: no se verificó la anatomía del runtime TARGET real; `velar`=forma-no-verdad
> y los tests verificaban la emisión inventada. Este rediseño cierra el loop
> **contra openclaw real** (`~/openclaw-fleet/` + `docs.openclaw.ai`), no contra
> tests propios.

## 1. Anatomía real de openclaw (verificada, no supuesta)

Leído directo de `~/openclaw-fleet/workspaces/{salubrista,steipete,main}/`, el
espejo `docs/openclaw/concepts/{agent-workspace,soul,system-prompt}.md` y la
config `openclaw.json.reference`. Cada agente openclaw es un **WORKSPACE
multi-archivo name-keyed** en `workspaces/{agentId}/`:

| Archivo | Rol (doc autoritativa) | ¿Lo posee KORA? |
|---|---|---|
| `AGENTS.md` | operating instructions: rules, priorities, how to behave. Loaded every session; **también inyectado a subagentes**. | **SÍ** — es el cuerpo del agente |
| `SOUL.md` | persona, tono, límites, **voz**. Loaded every session. La doc PROHÍBE meter operativa: «Keep AGENTS.md for operating rules. Keep SOUL.md for voice». | **SÍ** — es `U_phen` |
| `IDENTITY.md` | nombre, vibe, emoji; **bootstrap ritual**. | parcial (sólo el nombre) → no se emite |
| `USER.md` | quién es el operador. | no (operador) |
| `TOOLS.md` | convenciones locales; **«does not control tool availability; only guidance»**. | no (la frontera de capacidad vive en openclaw.json) |
| `HEARTBEAT.md`, `BOOT.md` | checklists de runtime, opcionales. | no (runtime) |
| `MEMORY.md`, `memory/` | memoria curada y diaria. | no (runtime) |
| `skills/` | skills de workspace. | sí, vía emisión de skills KORA |

Hechos load-bearing verificados:

1. **Config/tools/auth/model NO van en el workspace**: viven en
   `~/.openclaw/openclaw.json` (`agents.list[].workspace`). El funtor **no** los
   toca (deploy, operador).
2. **Missing-file es tolerado**: «If any bootstrap file is missing, OpenClaw
   injects a missing-file marker and continues»; `openclaw setup` siembra los
   faltantes **sin sobrescribir** los existentes. ⇒ el funtor emite sólo lo que
   KORA posee; el resto lo siembra openclaw.
3. **Deploy name-keyed, sin never-overwrite**: el gateway hot-reloadea
   `workspaces/{agentId}/` en `gateway restart`. `--aplicar` a
   `workspaces/{nombre}/` es viable (sobrescribe por nombre).
4. **El SOUL.md de la flota actual NO es voz pura** (lo produjo el funtor de la
   bestia: tiene `## Domain` y `## Hard Rules`). Es **deuda heredada**, no el
   contrato: la doc viva manda voz pura. El rediseño **mejora** sobre la bestia.

## 2. El problema central y su resolución (cat-thinking)

openclaw EXIGE `SOUL.md`=voz segregado de `AGENTS.md`=operativa. Pero el cuerpo
de un agente pneuma es **markdown monolítico** (operativa + `U_phen`
entremezclados; `ley/2 §10 r5` pone `U_phen` EN el cuerpo). ¿De dónde sale
`SOUL.md`? `U_phen` no es mecánicamente separable de la prosa
(forma-no-verdad: el núcleo **no entiende** prosa).

> El framing categorial siguiente es **heurístico-estructural** (guía de diseño),
> no demostración formal; lo marco como tal (regla cat-thinking «distingue formal
> de heurístico»). Las URN citan el corpus ICAS-BoK que apoya cada lectura.

### 2.1 Transporte de fibra = lift cartesiano (doctrina universal)

`urn:fxsl:kb:icas-extension` (fibraciones, Grothendieck) +
`urn:fxsl:kb:icas-interaccion` (base/fibra). El funtor `T_target` actúa sobre la
**base** —el retículo de vectores PMI×LFS— proyectando por `min`. El **cuerpo**
es la **fibra** sobre el punto-base; `T̃` es el **lift cartesiano** sobre `T`:
carga la fibra **verbatim**, sin reescribirla (transporte NO-funtorial). Esto ya
ocurre en los tres targets realizados (el cuerpo viaja entero al archivo único).
Se **legisla en `ley/3` para TODOS los targets**, sin campo por-emisión.

### 2.2 Workspace = producto; cuerpo = coproducto marcado

`urn:fxsl:kb:icas-universales` (productos y coproductos). El objeto-runtime
openclaw es un **producto** de archivos (`AGENTS.md × SOUL.md × …`). La fibra
(cuerpo `B`) mapea al producto. La componente `SOUL.md` exige una **inyección de
coproducto** desde `B`: `B ⊇ B_phen`, el span de `U_phen`. forma-no-verdad ⟹ el
núcleo **no puede computar** la descomposición (no lee prosa): la inyección es
**dato que aporta el autor**, no inferencia. El **centinela** es ese dato.

### 2.3 El centinela = predicado decidible (no juicio semántico)

`urn:fxsl:kb:icas-topoi` (clasificador de subobjetos χ). El marcador
`<!-- kora:soul -->` … `<!-- kora:soul:fin -->` es un **predicado literal
decidible** sobre el flujo de caracteres del cuerpo (string-match), no un juicio
«¿esta prosa es voz?» (indecidible para el núcleo). El núcleo evalúa χ (encuentra
dos centinelas y corta); jamás interpreta. Es la realización honesta de
forma-no-verdad. Mismo estilo que `<!-- kora:sello -->` y
`<!-- felix:recomendacion-unica -->` ya en el corpus.

### 2.4 Decisión: duplicación (no partición) — preserva bisimulación

Dos sub-opciones para emitir el workspace:

- **partición**: `AGENTS.md = B − B_phen`, `SOUL.md = B_phen`. El cuerpo se
  parte; `AGENTS.md ⊔ SOUL.md = B`.
- **duplicación** (ELEGIDA): `AGENTS.md = B` (cuerpo verbatim, idéntico
  transporte-de-fibra que todo target), `SOUL.md = B_phen` (copia del span
  marcado, proyección de voz adicional).

`urn:fxsl:kb:icas-efectos` (bisimulación) + `ley/3 §3` (bisimulación módulo
proyección). La **partición** haría que el `AGENTS.md` de openclaw fuese un
subconjunto estricto del cuerpo: el MISMO agente tendría doctrina distinta en
openclaw vs claude-code (el span de voz desaparecería de AGENTS.md), **rompiendo
la bisimulación entre targets**. La **duplicación** la preserva: el cuerpo viaja
entero al archivo de operativa en TODOS los targets; `SOUL.md` es una **inyección
de voz adicional**, nativa de openclaw. Además, la flota real (el target de
conformidad) **no particiona** — su `AGENTS.md` lleva las instrucciones
completas. Particionar nos alejaría de la flota; duplicar coincide.

La doc de openclaw es **asimétrica**: exige que `SOUL.md` NO sea un dump de
operativa; **no** prohíbe que `AGENTS.md` lleve su sección de estilo (de hecho
`ley/2 §10 r5` quiere `U_phen` en el cuerpo). Duplicación satisface ambas:
`SOUL.md` = voz pura (sólo el span marcado); `AGENTS.md` = operativa completa con
su `U_phen`-en-cuerpo. El costo (voz inyectada dos veces) es exactamente el patrón
de la flota real, y es aceptable.

### 2.5 `SOUL.md = U_phen` ya es doctrina del corpus

`urn:kora:kb:aufbau-persona-agente §3`: «Esto justifica la segregación
`SOUL.md = U_phen` separado de la lógica». `urn:kora:artefacto:autoria-de-persona`
(`insumo-transmutacion`): «`U_phen` → `SOUL.md`: openclaw, NO realizado … la
segregación `SOUL.md = U_phen` es la realización openclaw, aún sin funtor». El
funtor **realiza** lo que el corpus ya nombró. `U_phen` como `Para` que `c` lee:
`urn:fxsl:kb:icas-agencia`.

## 3. Qué emite el funtor (contrato de emisión)

Sea `A` el artefacto fuente (frontmatter + cuerpo `B`). `T-openclaw-pneuma-v1`:

### 3.1 `forma: habilidad` (skill) → `openclaw/skills/{nombre}/SKILL.md`

Frontmatter `name` + `description`; cuerpo `B` verbatim; sello. (agentskills.io +
overlay KORA; las tools de openclaw son config-level, no van en el frontmatter.)
Copia `referencias/` si existe. Idéntico patrón a codex/opencode skill.

### 3.2 `forma ∈ {subagente, agente, plataforma}` → workspace `openclaw/workspaces/{nombre}/`

- **`AGENTS.md`** = `B` verbatim + sello. **Siempre**. (= transporte-de-fibra, el
  mismo cuerpo que reciben todos los targets, en el archivo de operativa.)
- **`SOUL.md`** = span de `U_phen` + sello. Emitido **sólo si** `arnes` porta
  `U_phen` (`persona | orquestador | servicio`):
  - centinela presente y único → `SOUL.md` = span entre centinelas (stripped) +
    sello.
  - centinela **ausente** (con `arnes` de `U_phen`) → `transmutar` **falla**
    (exit 1) con mensaje honesto: el núcleo no segmenta prosa; el autor debe
    delimitar `U_phen` con `<!-- kora:soul -->…<!-- kora:soul:fin -->`
    (ver `ley/2 §10`, skill `autoria-de-persona`). **No se fabrica voz.**
  - centinela duplicado (>1 par) → falla (ambigüedad).
- `arnes` sin `U_phen` (`delegado`) → sólo `AGENTS.md`, sin `SOUL.md` (correcto:
  no hay persona que segregar; openclaw tolera el missing-file).

Ambos archivos portan el **mismo sello** (misma fuente, misma proyección): el
`hash-fuente` y los vectores son los del artefacto fuente completo. Cada archivo
emitido se auto-certifica (`ley/3 §5`: «todo archivo emitido DEBE terminar con un
sello»).

### 3.3 Lo que el funtor NO emite (frontera declarada, honesta)

`IDENTITY.md`, `USER.md`, `TOOLS.md`, `HEARTBEAT.md`, `BOOT.md`, `MEMORY.md`,
`memory/`, y la **config** (`openclaw.json`: model, tools, auth, telegram,
systemd). Razón: no son doctrina KORA — son scaffolding de workspace
(bootstrap ritual / `openclaw setup`) y deploy (operador). La **frontera de
capacidad** (`herramientas`) NO se materializa en el workspace (TOOLS.md «only
guidance»); se realiza en `openclaw.json` a nivel deploy. El sello declara
`herramientas`; el workspace no las enforce. Esto es asimetría de arquitectura
del target, no pérdida de eje — no genera línea `perdidas:`; se documenta en
`ley/3 §7`.

## 4. Matriz de preservación openclaw (§4.4 de `ley/3`)

Fiel a `~/kora/runtime/openclaw-runtime-extension.md §3` y confirmada contra el
openclaw real (ACP meta-runtime, systemd always-on, agentToAgent):

| Eje | Proyecciones |
|---|---|
| `pi` | 0→0,1→1,2→2,3→3 **full** — delegación jerárquica recursiva vía ACP dispatch |
| `mu` | 0→0,1→1,2→2,3→3 **full** — always-on vía systemd+Telegram; **único runtime con μ=3 full** |
| `xi` | 0→0,1→1,2→2,3→3,4→4 **full** — operad dinámica `Org^#_m` vía ACP+agentToAgent |
| `lambda` | 0→0,1→1,2→2 full · 3→3 **partial** — society-in-the-loop requiere gobernanza externa no modelada en runtime |
| `phi` | 0→0,1→1,2→2 full · 3→3 **partial** — cognición híbrida parcial (no HAJCS completo) · 4→∅ **none** — co-evolutivo no modelado |
| `sigma` | máx `[3,3,3,3,2]` — sustainability ambiental no medida (model routing + budget) |

openclaw es el **techo más alto** de los cinco targets: único con μ=3 y ξ=4 full,
y único que proyecta λ=3 (partial). Sólo φ=4 aborta (none, igual que el resto).
Consecuencia: agentes `plataforma`/`servicio` (μ=3) — sin hogar en
claude-code/codex/opencode — **encuentran hogar en openclaw**. Cierra la deuda
`GENESIS §4` (μ=3).

Las razones textuales y los mensajes «quién soporta» son **datos del núcleo**
(`ley/3 §4`), no texto legislado. Se actualizan: `mu=3`→openclaw realizado;
`lambda=3`→openclaw (parcial); `phi=4`→ninguno (openclaw también ∅).

## 5. Qué estrato de ley se toca y por qué (legislar antes de código)

- **`ley/2-forma.md` v1.3.0 → v1.4.0** (minor, aditivo): `§10` legisla el
  **centinela canónico opcional** `<!-- kora:soul -->…<!-- kora:soul:fin -->` que
  delimita el span de `U_phen` en el cuerpo, para targets que segregan voz. El
  núcleo lo halla por match literal (decidible), nunca entendiendo prosa. `velar`
  NO lo verifica (oficio; validado al emitir por `transmutar`). Sin campo, sin
  check, sin eje. Aditivo: artefactos sin centinela quedan byte-idénticos.
- **`ley/3-transmutacion.md` v1.2.0 → v1.3.0** (minor, realización aditiva):
  §1/§3 legisla el **transporte de fibra universal** (lift cartesiano); §2 pasa
  openclaw a **realizado**, añade `T-openclaw-pneuma-v1`; §4.4 la matriz; §7 la
  emisión de workspace (AGENTS.md+SOUL.md), el centinela requerido para `U_phen`,
  la frontera no-emitida, y `--aplicar` a `~/openclaw-fleet/workspaces/{nombre}/`;
  §10 validación. Nota de changelog: realiza openclaw, **registra** el cierre de
  `GENESIS §4` aquí (GENESIS **no se edita**), reintroduce matriz+transporte con
  la anatomía CORRECTA (workspace multi-archivo, no monolito Hermes).
- **`ley/0`**: **sin cambio**. No se añade/quita/renombra ningún check del
  registro cerrado (§11). La lógica interna de `sello-fresco` se amplía (escanea
  `workspaces/`) pero su id y contrato no cambian.
- **`ley/1`**: **sin cambio** (freeze). El vector y los ejes intactos.
- **`GENESIS.md`**: **NO se toca** (acta histórica inmutable). La realización se
  registra en `ley/3`.
- **`README.md`**: actualizar la línea «targets realizados» (auxiliar, honesto).

## 6. Cambios en `kora.py`

`TARGETS_REALIZADOS += "openclaw"`; `ARNESES_CON_UPHEN`; centinela `RE_SOUL` +
constantes; `MATRICES["openclaw"]` + `SIGMA_RAZONES["openclaw"]`; `QUIEN_SOPORTA`
(mu3/lambda3 actualizados); `_componer_plano`; `_extraer_soul`;
`_emitir_openclaw`; `emitir()` refactor a lista de `(rel, contenido)` +
`perdidas_extra`; `cmd_transmutar` multi-archivo (stdout/_emision/aplicar);
`RUTAS_APLICAR` openclaw; `chk_sello_fresco` escanea `workspaces/`. Byte-
determinista, sin timestamps.

## 7. Gate y prueba de conformidad REAL (loop-closure)

1. `python3 kora.py velar --estricto` → 13/13.
2. `python3 -m unittest discover -s tests` → todos verdes. Tests nuevos verifican
   EMISIÓN CONFORME: workspace con AGENTS.md+SOUL.md (no monolito), operativa en
   AGENTS.md / voz en SOUL.md, matriz μ:3/ξ:4 full, centinela ausente falla,
   delegado sin SOUL.md, byte-determinismo, skill→SKILL.md, sello-fresco sobre
   workspace, φ=4 aborta.
3. **Conformidad real**: emitir `steipete` (persona, vector `[2,2,3,1,2]` que
   proyecta a openclaw **full** en todos los ejes) a `_emision/openclaw/` y
   demostrar isomorfismo estructural con `~/openclaw-fleet/workspaces/steipete/`:
   mismos archivos canónicos doctrina+voz (AGENTS.md, SOUL.md), operativa en
   AGENTS.md, voz en SOUL.md. **NO `--aplicar`** a la flota viva (evita tocar
   otro repo); la prueba es por `_emision` + diff estructural.

## 8. Lo que queda como deuda declarada (honesto)

- `IDENTITY/USER/TOOLS/HEARTBEAT/BOOT/MEMORY` no se emiten: scaffolding de
  bootstrap/operador, fuera del alcance del funtor (por diseño, no olvido).
- Agentes que ya declaran openclaw sin centinela (`agent-architect`): su emisión
  a openclaw **falla honesto** hasta que el autor añada el centinela `kora:soul`.
  Es comportamiento correcto (forma-no-verdad), no bug; se añade en autoría
  posterior.
- `Lift_openclaw` (ingesta inversa): no realizado (igual que el resto;
  `ley/3 §8`).
- La frontera de capacidad (`herramientas`) en openclaw vive en `openclaw.json`
  (deploy), no en el workspace: el sello la declara, el runtime la enforce a
  nivel config (operador).
