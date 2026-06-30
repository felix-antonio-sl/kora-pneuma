# KORA/Transmutación — ley pneuma v1.3.0

Estrato 3 de la ley. Gobierna el gesto `transmutar`: la proyección de un
artefacto agéntico desde el espacio ideal hacia un runtime concreto.

## 1. Principio

> **La transmutación es funtor. Preserva composición e identidad; la pérdida
> se declara, nunca se oculta.**

Un artefacto vive como vector en el IR; para correr en un mundo concreto se
proyecta vía el funtor `T_target: IR → Runtime_target`. Encarnar, bajo esta
ley, es un acto que viene acompañado de su propia confesión: el sello (§5).

## 2. Targets reconocidos y realizados

| Target | Estatus | `transmutar` |
|---|---|---|
| `claude-code` | realizado | emite |
| `codex` | realizado | emite |
| `opencode` | realizado | emite |
| `openclaw` | realizado | emite |
| `hermes` | reconocido, no realizado | falla (exit 1) con mensaje honesto |

1. `targets` DEBE ser subconjunto de los cinco reconocidos (check
   `targets-conocidos`, ley/2).
2. Un artefacto PUEDE declarar `hermes` en `targets` — la ley lo reconoce —
   pero transmutar hacia él DEBE fallar con mensaje que remita a `GENESIS.md`.
   La ley no nombra capacidades inexistentes como si existieran. `openclaw`
   pasa de «reconocido, no realizado» (estado de `GENESIS.md §4`, acta
   inmutable) a **realizado** por `T-openclaw-pneuma-v1`: la realización se
   **registra aquí**, reconciliando `GENESIS.md` (que seguirá diciendo «no
   realizado») sin editarlo. `openclaw` es el único runtime cuyo techo admite
   materia ambiental `mu=3` y operad dinámica `xi=4` sin recorte.
3. El identificador del funtor DEBE ser `T-{target}-pneuma-v1`. Funtores
   vigentes: `T-claude-code-pneuma-v1`, `T-codex-pneuma-v1`,
   `T-opencode-pneuma-v1`, `T-openclaw-pneuma-v1`.

## 3. Leyes del funtor

| Ley | Enunciado | Garantía |
|---|---|---|
| Composición | `T(f ∘ g) = T(f) ∘ T(g)` | por construcción |
| Identidad | `T(id) = id` | por construcción |
| Monotonía Π, Μ, Ξ | proyección por eje = `min(valor, máximo soportado)`; si `v1 ≤ v2` entonces `T(v1) ≤ T(v2)` | por construcción |

Reglas:

1. NUNCA se proyecta hacia arriba: ningún eje emite un valor mayor que el
   declarado en la fuente.
2. Violar composición o identidad rompe la transmutación: es error
   categorial, no "pérdida declarada".
3. Si algún eje proyecta a ∅ (sin valor target), la transmutación DEBE fallar
   (exit 1) con mensaje que nombre el eje, el valor fuente y el runtime que
   sí lo soporta. NUNCA degradación silenciosa.
4. Toda pérdida (fidelidad `partial`) DEBE declararse en el sello con razón.
5. NO DEBE declararse fidelidad `full` cuando hay pérdida real.

Garantía declarada adicional, heredada de la bestia — **bisimulación módulo
proyección**: si `A₁ ∼ A₂` en el IR (equivalencia observacional), entonces
`T(A₁) ∼ T(A₂)` módulo pérdida declarada. Ningún check la verifica; esta ley
la confiesa en el mismo régimen que las tres leyes declaradas de §6, y NO se
añade al sello, cuyas líneas finales son fijas (§5 r4).

## 4. Matrices de preservación

Estructura por celda: `valor fuente → (proyectado | ∅, fidelidad
full|partial|none, razón si no-full)`. Para `sigma`: proyección por
componente = `min(componente, máximo soportado)`; todo recorte es `partial`
con razón por componente.

Las razones textuales de pérdida por componente de `sigma` y los mensajes de
qué runtime sí soporta un eje rechazado son **datos del núcleo**, no texto
legislado: la ley fija máximos, proyecciones y fidelidades; las razones DEBEN
ser veraces respecto de la runtime-extension de origen, pero su literal vive
en `kora.py`. (Esto evita el drift de duplicar quince strings entre ley y
núcleo.)

### 4.1 `claude-code`

| Eje | Proyecciones |
|---|---|
| `pi` | 0→0, 1→1, 2→2 full · 3→2 partial — fixed-points se aplanan |
| `mu` | 0→0, 1→1, 2→2 full · 3→∅ none — sin ambiente always-on; usar openclaw |
| `xi` | 0→0, 1→1, 2→2 full · 3→2 partial — multi-fase se aplana · 4→2 partial — operad dinámica no soportada |
| `lambda` | 0→0, 1→1 full · 2→1 partial — ecosistema colapsa a organizacional · 3→∅ none — society-in-the-loop no soportado |
| `phi` | 0→0, 1→1, 2→2 full · 3→2 partial — cognición híbrida no nativa · 4→∅ none — co-evolutivo no soportado |
| `sigma` | máx soportado `[3,2,3,2,1]` |

### 4.2 `codex`

| Eje | Proyecciones |
|---|---|
| `pi` | 0→0, 1→1, 2→2 full · 3→3 partial — recursión con budget acotado |
| `mu` | 0→0, 1→1 full · 2→1 partial — session-resumable, sin memoria transparente cross-session · 3→∅ none — CLI síncrono, no daemon |
| `xi` | 0→0, 1→1, 2→2 full · 3→2 partial — multi-fase se aplana · 4→2 partial — operad dinámica no soportada |
| `lambda` | 0→0, 1→1 full · 2→1 partial — ecosistema colapsa a organizacional · 3→∅ none — society-in-the-loop no soportado |
| `phi` | 0→0, 1→1 full · 2→2 partial — colaborativo vía resume+approvals, sin identidad persistente · 3→2 partial — cognición híbrida no nativa · 4→∅ none — co-evolutivo no soportado |
| `sigma` | máx soportado `[3,2,2,2,1]` |

### 4.3 `opencode`

| Eje | Proyecciones |
|---|---|
| `pi` | 0→0, 1→1, 2→2 full · 3→3 partial — steps acotados |
| `mu` | 0→0, 1→1 full · 2→2 partial — contexto parent/child, sin memoria transparente · 3→∅ none — CLI/TUI síncrono, no daemon |
| `xi` | 0→0, 1→1, 2→2 full · 3→3 partial — multi-fase vía subagentes, coreografías largas dependen del wrapper · 4→3 partial — operad no soportada |
| `lambda` | 0→0, 1→1 full · 2→1 partial — ecosistema colapsa a organizacional · 3→∅ none — society-in-the-loop no soportado |
| `phi` | 0→0, 1→1, 2→2 full · 3→2 partial — cognición híbrida no nativa · 4→∅ none — co-evolutivo no soportado |
| `sigma` | máx soportado `[3,2,2,2,1]` |

### 4.4 `openclaw`

Techo más alto del retículo: meta-runtime ACP multi-backend, único con
materia ambiental always-on (systemd + bots Telegram). Heredado de la
runtime-extension de origen (`urn:agengai:kb:openclaw-runtime-extension`),
verificado contra el runtime real; su literal vive en `kora.py` (§4).

| Eje | Proyecciones |
|---|---|
| `pi` | 0→0, 1→1, 2→2, 3→3 **full** — delegación jerárquica recursiva vía ACP dispatch y sub-agentes |
| `mu` | 0→0, 1→1, 2→2, 3→3 **full** — **único target con materia ambiental always-on** (systemd + Telegram; `MEMORY.md`/`USER.md` + memoria declarativa) |
| `xi` | 0→0, 1→1, 2→2, 3→3, 4→4 **full** — **único que no aplana la operad dinámica**: federación `Org^#_m` vía ACP dispatch + agent-to-agent |
| `lambda` | 0→0, 1→1, 2→2 full · 3→3 partial — society-in-the-loop requiere gobernanza externa no modelada en el runtime |
| `phi` | 0→0, 1→1, 2→2 full · 3→3 partial — cognición híbrida parcial: HOTL presente, sin HAJCS completo · 4→∅ none — co-evolutivo no soportado |
| `sigma` | máx soportado `[3,3,3,3,2]` — accountability=3 real (materia persistente cross-session); solo `sustainability` se recorta (no medida directamente) |

## 5. El sello

Todo archivo emitido DEBE terminar con un sello proof-carrying: comentario
HTML, formato EXACTO, **sin timestamp** — el hash ancla la identidad, el
tiempo es mundano.

```text
<!-- kora:sello
fuente: urn:kora:artefacto:mente-omega
version: 1.0.1
hash-fuente: sha256:abc123...
target: claude-code
funtor: T-claude-code-pneuma-v1
vector-fuente: [2,0,2,0,1] sigma [3,2,3,3,1]
vector-proyectado: [2,0,2,0,1] sigma [3,2,3,2,1]
fidelidad: pi:full mu:full xi:full lambda:full phi:full sigma:partial
perdidas:
  sigma.accountability: 3->2 :: sin audit trail persistente cross-session
preservado-por-construccion: composicion, identidad, monotonia-pi, monotonia-mu, monotonia-xi
declarado-no-mecanizado: naturalidad-xi, cierre-safety, composicion-kleisli
-->
```

Si el artefacto declara `conocimiento` o `componible`, el sello incluye
además —entre `perdidas:` y las dos líneas fijas— un bloque
`contrato-conocimiento:` (r6):

```text
contrato-conocimiento:
  ancla: ~/kora-pneuma  (o $KORA_RAIZ)
  derivacion: urn:{ns}:kb:{id} -> {ancla}/artefactos/conocimiento/{ns}/{id}.md ; urn:{ns}:artefacto:{id} -> {ancla}/artefactos/skills/{ns}/{id}/SKILL.md (skill) | {ancla}/artefactos/agentes/{ns}/{id}.md (agente)
  conocimiento: urn:fxsl:kb:icas-sintesis
  componible: urn:kora:artefacto:cat-thinking
```

Reglas:

1. `hash-fuente`: sha256 del archivo fuente completo (bytes).
2. `perdidas:` aparece solo si hay alguna; una línea por pérdida con formato
   `eje: a->b :: razón`. Las pérdidas de `sigma` se nombran por componente
   (`sigma.accountability`, `sigma.transparency`, ...).
3. En un sello emitido la fidelidad solo toma valores `full` o `partial`: un
   eje `none` aborta la emisión (§3 r3); `none` jamás llega al archivo.
4. Las líneas `preservado-por-construccion` y `declarado-no-mecanizado` son
   **FIJAS**, carácter por carácter. NO DEBE moverse jamás una ley declarada
   a la lista de preservadas (§6).
5. Determinismo: misma fuente → emisión byte-idéntica. Ninguna emisión lleva
   timestamp ni estado de máquina.
6. `contrato-conocimiento:` aparece **solo si** el artefacto declara
   `conocimiento` o `componible`, e inmediatamente **antes** de las dos líneas
   fijas (r4). Porta `ancla` (raíz del repo central / `$KORA_RAIZ`),
   `derivacion` y las listas `conocimiento`/`componible` de URN. La regla de
   derivación URN→path **no se re-legisla aquí: es la biyección de `ley/2 §6`
   que `lugar-coincide` blinda**; el sello la *imprime* para que un consumidor
   con solo lectura la evalúe por sustitución, sin acceso a la ley. **Cero
   paths materializados**: el URN es la autoridad, el path se deriva. Es
   extensión aditiva (constitución §12.1): un artefacto sin corpus no porta el
   bloque y su emisión queda byte-idéntica. Encarna la doctrina de acceso de
   `urn:kora:kb:regimen-de-ley`.

### 5.1 Extensión del sello para `openclaw`

La emisión `openclaw` es un `SOUL.md` sin frontmatter (§7); su sello porta, en
la **zona variable** (antes de las dos líneas fijas, que NO se mueven —r4), tres
elementos propios, todos observables en el archivo (el proof-carrier reconcilia
`GENESIS.md`↔`realizado` por sí mismo, sin tercerizar la calificación a una ley
que no viaja con el artefacto):

1. **Dos pérdidas de forma** bajo `perdidas:` (precedente: codex
   `forma: agente->habilidad`), verificables como aserción de **ausencia**:
   - `forma: tool-binding->deploy` — el enforcement allow/deny vive en
     `openclaw.json` (deploy-side); el binding NO se enforcea desde el `SOUL.md`.
   - `forma: workspace-anatomy->soul-slot` — la anatomía multi-slot de openclaw
     (`SOUL.md`/`AGENTS.md`/`TOOLS.md`/`MEMORY.md`/…) colapsa a un único
     `SOUL.md` bajo «pneuma-mínima» (archivo único, sin hermanos).
2. **La calificación `mu=3` observable** (dos líneas):

   ```text
   realiza: emision-mu3-conforme (techo always-on, sin truncamiento de min)
   difiere: conducta-always-on (gateway/systemd) -> a desplegar
   ```

   `mu:3→3 full` afirma que el **techo** del runtime admite materia always-on
   sin truncamiento de `min` (*tipo/sintaxis*); NO que el always-on conductual
   esté verificado (*token/semántica*). El substrato `mu=3` es estado de runtime
   acumulado (`MEMORY.md`/`USER.md` snapshot-inyectados + gateway), inherentemente
   no-emitible. La realización del funtor es la emisión tipo-conforme; la conducta
   always-on es deploy del fleet, declarada y diferida, no fingida.
3. **La clausura `F` declarada** (`clausura-F`): el tool-SET intencionado se
   declara para que `cierre-safety` (§6) tenga **referente** —de lo contrario
   `openclaw` sería el único target que deja `cierre-safety` sin portador—; solo
   el binding (enforcement allow/deny → `openclaw.json`, *token*) se difiere.

### 5.2 El transporte de fibra (universal, en prosa)

El sello documenta **dos operaciones** distintas sobre el artefacto, y esto vale
para **todos los targets**, no solo `openclaw`:

- la **proyección funtorial del vector** (las líneas de `fidelidad` y `perdidas`):
  `min` sobre la matriz, mecanizada;
- el **transporte verbatim del cuerpo** —portador de `U_phen`, fibra
  no-coordenada (`ley/1 §2`)—: el cuerpo NO se min-proyecta, NO se declara-pierde
  por eje y **NO se re-proyecta** para concordar con el vector.

El transporte **no es funtorial** (es la componente sobre la fibra de un
funtor cartesiano `T̃` que yace sobre el `T` de base; `openclaw` lo hace
sintáctico al escindir `SOUL.md`=fibra ⊥ `openclaw.json`=base, sin crear un
régimen nuevo). Un consumidor que lee un cuerpo **no debe asumir** que concuerda
automáticamente con el vector proyectado. El **riesgo de desincronización
cuerpo↔vector** (un cuerpo verbatim puede afirmar capacidad que el vector ya no
declara tras `min`) se **nombra** como puntero a la confesión FS-no-mecanizada de
`ley/4` —obligación del productor, no del núcleo—; **NO** se mecaniza con un check
nuevo (eso contradiría `ley/4`). `T̃` es emisión hacia adelante: **no realiza
`Lift⊣T`** (§8 sigue abierta).

## 6. La nota de honestidad (heredada)

Dos regímenes de garantía, y la ley los distingue en voz alta:

- **preservado-por-construccion**: `composicion`, `identidad`,
  `monotonia-pi`, `monotonia-mu`, `monotonia-xi`. El núcleo las realiza
  mecánicamente al proyectar con `min` sobre la matriz; no pueden violarse
  sin que `transmutar` falle.
- **declarado-no-mecanizado**: `naturalidad-xi` (el diagrama plan-ejecutor
  conmuta en el target), `cierre-safety` (la sub-coálgebra segura sigue
  cerrada tras la proyección), `composicion-kleisli` (la composición de
  efectos declarada en `componible` se refleja en el target).

Hay un **tercero que no es ninguno de los dos**: el transporte verbatim del
cuerpo —portador de `U_phen`, fibra no-coordenada (`ley/1 §2`)— no es garantía
sobre la proyección (no se preserva-por-construcción ni se declara-no-mecanizado
como las cinco/tres de arriba): es copia de contenido, legislada en §5.2. No
entra en ninguna de las dos listas fijas del sello (r4) precisamente porque no es
una garantía del funtor, sino su acompañante cartesiano.

Reglas:

1. Hoy **NO existe check** que verifique las tres leyes declaradas. Lo que se
   verifica es que la declaración esté presente y bien formada en el sello,
   no que la ley se cumpla en el runtime destino. Son obligación declarada,
   no garantía verificada, y esta ley lo dice sin eufemismo.
2. Mecanizar una de las tres exige: escribir el check, registrarlo en el
   registro cerrado (constitución §11, cambio de ley) y solo entonces moverla
   de lista.

Rationale: esta es la diferencia entre el puente demostrado y el puente
prometido. La virtud de KORA no es carecer de puentes prometidos; es no
llamarlos demostrados.

## 7. Emisión por target

Firma del gesto: `transmutar --urn U --target T [--aplicar] [--stdout] [--proyecto PATH]`.
Default: escribe bajo `_emision/{target}/...` (derivado, gitignored) y
reporta. `--stdout` imprime; `--aplicar` instala en el runtime real.

| Target | Forma | Emisión |
|---|---|---|
| `claude-code` | skill | `_emision/claude-code/skills/{nombre}/SKILL.md`; frontmatter `name`, `description` (+ `allowed-tools` como lista separada por comas si `herramientas` no es vacía); copia `referencias/` conservando su nombre si existe |
| `claude-code` | agente | `_emision/claude-code/agents/{nombre}.md`; frontmatter `name`, `description`, `tools` (lista separada por comas); body = body fuente; si `arnes` = `persona`, sección final `## Modos de invocacion` con la doctrina dual-mode (modo subagente batch vs modo persona por encarnación) |
| `codex` | skill | `_emision/codex/skills/{nombre}/SKILL.md`; frontmatter `name`, `description`; copia `referencias/` conservando su nombre |
| `codex` | agente | se emite **como skill**; el colapso de forma se declara en el sello como pérdida adicional: `forma: agente->habilidad :: codex no registra agentes` |
| `opencode` | skill | `_emision/opencode/skills/{nombre}/SKILL.md` (mismo formato codex) |
| `opencode` | agente | `_emision/opencode/agents/{nombre}.md`; frontmatter `description`, `mode: subagent` (forma `subagente`) o `mode: all` (forma `agente`: persona dual-mode, usable como primario y delegable como subagente; `all` es el default de opencode y preserva ambos modos del sello), y `permission:` con `<tool>: deny` para cada tool de **efecto externo** (`bash`, `webfetch`, `websearch`, `task`) que `herramientas` NO concede — frontera de capacidad en el idiom canónico de opencode (el objeto `tools` está deprecado desde v1.1.1; las read-ish e internas quedan en default). Paridad con el allowlist `tools` de claude-code |
| `openclaw` | skill | `_emision/openclaw/skills/{nombre}/SKILL.md` (superficie agentskills; mismo formato que codex/opencode) |
| `openclaw` | agente | `_emision/openclaw/agents/{nombre}/SOUL.md`; **sin frontmatter** — markdown libre, slot #1 de Hermes inyectado verbatim (un fence YAML `---…---` se inyectaría como ruido de identidad); body = body fuente verbatim (abre con su propio H1); la anatomía multi-slot de openclaw colapsa a este **único** `SOUL.md` (pneuma-mínima; sin `AGENTS.md`/`TOOLS.md`/… hermanos); sello inline con la extensión §5.1 (pérdidas de forma, `realiza`/`difiere`, `clausura-F`) |

`--aplicar`: claude-code → `~/.claude/skills/{nombre}/` y
`~/.claude/agents/{nombre}.md`; codex → `~/.codex/skills/{nombre}/`;
opencode → `~/.config/opencode/skills/{nombre}/` y
`~/.config/opencode/agents/{nombre}.md`. **`openclaw` NO admite `--aplicar`** en
esta encarnación: Hermes prohíbe sobrescribir un `SOUL.md` existente
(never-overwrite), que el modelo clobber de `--aplicar` violaría; la instalación
en un `HERMES_HOME` / workspace del fleet es **deploy**, no función del funtor
(como la bestia, que tampoco auto-desplegó: emitió a `_BUILD/` + `DEPLOY.md`
manual). `transmutar --target openclaw --aplicar` falla (exit 1) con mensaje
honesto; la emisión canónica a `_emision/openclaw/` sí procede. En toda emisión y
aplicación la
fibra `referencias/` conserva su nombre: el cuerpo emitido cita paths
`referencias/...` y ningún target exige otro nombre.

`--proyecto PATH` (requiere `--aplicar`): redirige la instalación al nivel
**proyecto** — el `.opencode/`/`.claude/` del proyecto, no el home del operador.
claude-code → `PATH/.claude/skills/{nombre}/` y `PATH/.claude/agents/{nombre}.md`;
opencode → `PATH/.opencode/skills/{nombre}/` y `PATH/.opencode/agents/{nombre}.md`
(subdirectorios en **plural**, convención canónica de opencode: el `.opencode/` y
`~/.config/opencode/` usan nombres plurales; singular solo por retrocompat).
`codex` NO soporta nivel proyecto (sin convención verificada): `transmutar` falla
nombrando los targets soportados. La emisión canónica en `_emision/` no cambia;
`--proyecto` solo redirige el destino de `--aplicar`.

El gesto `--aplicar` **respeta y valida el campo `alcance`** del artefacto (ley/2
§3; ausente = `ambos`): un artefacto con `alcance: usuario` rechaza `--proyecto`;
uno con `alcance: proyecto` exige `--proyecto` (falla en la instalación
user-general); `ambos` admite cualquiera. El alcance es propiedad del artefacto,
ortogonal a `targets`: se determina en autoría, no en el gesto — el gesto solo lo
honra. La emisión canónica en `_emision/` es siempre alcance-neutral.

Los espacios de emisión por runtime son **planos** (un directorio por
`nombre`): dos artefactos con el mismo `nombre` y URN distinto NO DEBEN
emitirse — `transmutar` falla nombrando la colisión; renombra uno.

## 8. El gesto inverso (Lift)

La ley reconoce el gesto inverso — `Lift_target: Runtime ⇢ IR`, la ingesta
que eleva un artefacto foráneo al espacio ideal — y su aspiración de
adjunción `Lift ⊣ T`:

```text
T ∘ Lift = id   (módulo pérdida declarada)
Lift ∘ T ≤ id   (módulo encaje)
```

Esta encarnación NO lo realiza: ningún gesto del núcleo lo implementa (ver
`GENESIS.md`). Reconocerlo sin realizarlo es deliberado: es ley pendiente de
cuerpo, no capacidad fingida.

## 9. Frescura

Si existe `_emision/`, cada emisión DEBE portar un sello cuyo `hash-fuente`
coincida con el sha256 **actual** de su fuente. Si no coincide, la emisión
está rancia y el veredicto es: re-transmutar. Check: `sello-fresco`.

Alcance honesto del check: `sello-fresco` verifica **presencia del sello y
frescura del `hash-fuente`**, leyendo el **último** bloque `kora:sello` del
archivo (el cuerpo puede citar sellos de ejemplo sin volver rancia la
emisión). NO verifica la buena forma completa del sello — formato exacto y
líneas fijas de §5 quedan garantizados al emitir y declarados después, no
mecanizados sobre emisiones ya escritas.

## 10. Validación

| Regla | Detalle | Enforcement |
|---|---|---|
| Eje a ∅ aborta | §3 r3: exit 1 nombrando eje, valor y runtime alternativo | mecanizado (`transmutar`) |
| Target no realizado falla honesto | §2 r2 | mecanizado (`transmutar`) |
| Monotonía Π, Μ, Ξ | proyección `min` sobre matriz | mecanizado (por construcción) |
| Composición e identidad | §3 | mecanizado (por construcción) |
| Pérdidas declaradas si `partial` | §5 r2 | mecanizado (`transmutar`) |
| Fuente coherente antes de proyectar | checks ontológicos de `velar` sobre la fuente | mecanizado (`transmutar`) |
| Colisión de `nombre` en el espacio plano de emisión | §7 | mecanizado (`transmutar`) |
| Sello con formato exacto al emitir | §5 | mecanizado (`transmutar`) |
| Emisión fresca (presencia de sello + `hash-fuente` actual, último bloque) | §9 | mecanizado (`sello-fresco`) |
| Buena forma completa del sello en emisiones ya escritas | §5, §9 | declarado |
| Determinismo byte-idéntico | §5 r5 | mecanizado (sin timestamps; cubierto por tests) |
| `openclaw` realizado: emisión `SOUL.md` sin frontmatter, archivo único | §4.4, §7 | mecanizado (`transmutar`) + tests |
| Pérdidas de forma openclaw (`tool-binding`, `workspace-anatomy`) | §5.1 | mecanizado (sello); test por aserción de ausencia |
| Calificación `mu=3` observable (`realiza`/`difiere`) y `clausura-F` | §5.1 | mecanizado (sello) |
| `openclaw` rechaza `--aplicar` (never-overwrite) | §7 | mecanizado (`transmutar`) + tests |
| Transporte de fibra `U_phen` (no funtorial, universal) | §5.2 | declarado (prosa) |
| `naturalidad-xi` | §6 | declarado |
| `cierre-safety` | §6 | declarado |
| `composicion-kleisli` | §6 | declarado |
| Bisimulación módulo proyección | §3 | declarado |

Sublimado de transmutation-spec v1.2.1 y las runtime-extensions claude-code,
codex y opencode de la bestia el 2026-06-11; ver GENESIS.md.

v1.2.0 (HITL 2026-06-15): §5 legisla el bloque `contrato-conocimiento` del
sello (extensión aditiva, constitución §12.1 r1); la regla de derivación
URN→path se cita a `ley/2 §6`, no se re-legisla. Cierra el drift prosa↔código
del contrato de conocimiento implementado en cbc7652.

v1.3.0 (HITL 2026-06-30, Pieza C): realiza `T-openclaw-pneuma-v1`. §2 mueve
`openclaw` a realizado (registrando la deuda de `GENESIS.md §4`, que no se
edita); §4.4 fija su matriz (techo más alto: `mu=3` y `xi=4` full, único con
materia ambiental always-on; razones veraces de
`urn:agengai:kb:openclaw-runtime-extension`); §5.1 extiende el sello (dos
pérdidas de forma, calificación `mu=3` observable `realiza`/`difiere`,
`clausura-F` como referente de `cierre-safety`); §5.2 legisla el transporte de
fibra `U_phen` como tercera capa universal (no funtorial, no campo por-emisión;
desync cuerpo↔vector = puntero a `ley/4`, no mecanizado); §6 reconoce ese
transporte como tercero ajeno a las dos listas fijas; §7 fija la emisión
`SOUL.md` sin frontmatter (archivo único) y el rechazo de `--aplicar`
(never-overwrite de Hermes; deploy del fleet, no del funtor). Sin tocar
`ley/0/1/2/4`, `RUTAS_APLICAR` ni `GENESIS.md`. Deudas que NO salda, declaradas:
`hermes`, `Lift⊣T` (§8), convergencia teleológica y `α-iso` (`cat-agent-modulo`),
puente retículo↔coálgebra (`ley/1 §5`).
