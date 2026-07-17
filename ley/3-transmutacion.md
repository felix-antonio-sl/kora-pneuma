# KORA/Transmutación — ley pneuma v2.6.0

Estrato 3 de la ley. Gobierna el gesto `transmutar`: la proyección de un
artefacto agéntico desde el espacio ideal hacia un runtime concreto.

## 1. Principio

> **La transmutación es funtor. Preserva composición e identidad; la pérdida
> se declara, nunca se oculta.**

Un artefacto vive como vector en el IR; para correr en un mundo concreto se
proyecta vía el funtor `T_target: IR → Runtime_target`. Encarnar, bajo esta
ley, es un acto que viene acompañado de su propia confesión: el sello (§5).

### 1.1 Transporte de fibra (doctrina universal, todos los targets)

> El funtor `T_target` actúa sobre la **base** —el retículo de vectores PMI×LFS—
> proyectando cada eje por `min` (§3). El **cuerpo** del artefacto es la
> **fibra** sobre el punto-base; viaja **verbatim** al archivo de operativa del
> runtime, sin reescribirse. Ese transporte de fibra es **NO-funtorial** (el
> cuerpo no es una flecha que se componga): es el lift cartesiano `T̃` sobre `T`.

Reglas:

1. La proyección del vector la hace `T` sobre la base (matrices §4). En targets
   monolíticos el cuerpo NO se proyecta: se transporta entero al archivo que el
   target reserva para la operativa (`SKILL.md` o `{nombre}.md`).
2. Este transporte vale para **todos** los targets, sin campo por-emisión que lo
   declare: es la forma del funtor, no un atributo del artefacto.
3. Un target cuyo objeto-runtime es un **producto de archivos** PUEDE distribuir
   un componente marcado del cuerpo al archivo nativo que le corresponde. En
   `openclaw`, `AGENTS.md` recibe la operativa sin el span `U_phen` y `SOUL.md`
   recibe ese span. El producto conserva la materia completa sin duplicarla;
   cada componente sale de un **span marcado** (`ley/2 §10 r6`), nunca de una
   segmentación de prosa por el núcleo (forma-no-verdad). Los demás targets
   conservan el cuerpo completo verbatim.

## 2. Targets reconocidos y realizados

| Target | Estatus | `transmutar` |
|---|---|---|
| `claude-code` | realizado | emite |
| `codex` | realizado | emite |
| `opencode` | realizado | emite |
| `openclaw` | realizado | emite (workspace, §7) |
| `hermes` | reconocido, no realizado | falla (exit 1) con mensaje honesto |

1. `targets` DEBE ser subconjunto de los cinco reconocidos (check
   `targets-conocidos`, ley/2).
2. Un artefacto PUEDE declarar `hermes` en `targets` — la ley lo reconoce — pero
   transmutar hacia él DEBE fallar con mensaje que remita a `GENESIS.md`. La ley
   no nombra capacidades inexistentes como si existieran. `openclaw` está
   **realizado** desde v1.3.0 (cierra la deuda de `GENESIS §4`, registrada aquí
   sin editar GENESIS).
3. El identificador del funtor DEBE corresponder a la versión de su contrato.
   Funtores vigentes: `T-claude-code-pneuma-v1`, `T-codex-pneuma-v2`,
   `T-opencode-pneuma-v1`, `T-openclaw-pneuma-v1`. La v2 de Codex reemplaza
   el antiguo colapso agente→skill por custom agents nativos (§7).
4. `transmutar --target T` exige que la fuente declare `T` en `targets`:
   proyectar hacia un destino no declarado ampliaría silenciosamente el
   contrato de despliegue del artefacto.
5. La emisión histórica puede producirse desde cualquier estado válido, pero
   `--aplicar` exige `estado: activo`. Un artefacto deprecado o retirado se
   conserva y resuelve; no se reinstala como si siguiera vigente.

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
4. Toda pérdida —reticular o de campo no reticular— DEBE declarar fidelidad
   `partial` en su régimen y aparecer en el sello con razón.
5. NO DEBE declararse fidelidad `full` para la dimensión donde hay pérdida
   real. La fidelidad de campos no inventa ejes nuevos (§5 r3).

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

El **techo más alto** de los cinco targets: meta-runtime ACP + systemd
always-on + agentToAgent. Único con `mu`=3 y `xi`=4 full; único que proyecta
`lambda`=3 (partial). Fiel a la runtime-extension openclaw de la bestia y
confirmada contra el openclaw real (`~/openclaw-fleet/`, `docs.openclaw.ai`).

| Eje | Proyecciones |
|---|---|
| `pi` | 0→0, 1→1, 2→2, 3→3 full — delegación jerárquica recursiva vía ACP dispatch |
| `mu` | 0→0, 1→1, 2→2, 3→3 full — always-on vía systemd + Telegram; único runtime con μ=3 full |
| `xi` | 0→0, 1→1, 2→2, 3→3, 4→4 full — operad dinámica `Org^#_m` vía ACP + agentToAgent |
| `lambda` | 0→0, 1→1, 2→2 full · 3→3 partial — society-in-the-loop requiere gobernanza externa no modelada en runtime |
| `phi` | 0→0, 1→1, 2→2 full · 3→3 partial — cognición híbrida parcial (no HAJCS completo) · 4→∅ none — co-evolutivo no modelado |
| `sigma` | máx soportado `[3,3,3,3,2]` — sustainability ambiental no medida directamente |

Consecuencia: agentes `plataforma`/`servicio` (μ=3) — sin hogar en los otros
targets, que abortan μ=3 — encuentran hogar pleno en `openclaw`. Sólo `phi`=4
aborta (none, igual que el resto).

## 5. El sello

Todo factor doctrinal emitido (`SKILL.md`, agente, `AGENTS.md`, `SOUL.md`) DEBE
terminar con un sello proof-carrying: comentario HTML, formato EXACTO, **sin
timestamp** — el hash ancla la identidad, el tiempo es mundano. Los sidecars
de runtime y la fibra `referencias/` no duplican el sello; pertenecen al mismo
producto y `sello-fresco` prueba sus bytes contra el generador (§9).

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
  resolucion-bash: python3 {ancla}/kora.py nombre <URN>
  resolucion-lectura: Grep exacto '^urn: <URN>$' bajo {ancla}/artefactos; exigir coincidencia unica
  conocimiento: urn:fxsl:kb:icas-sintesis
  componible: urn:kora:artefacto:cat-thinking
```

Reglas:

1. `hash-fuente`: sha256 del archivo fuente completo (bytes).
2. `perdidas:` aparece solo si hay alguna; una línea por pérdida con formato
   `etiqueta: a->b :: razón`. Las pérdidas de eje usan el nombre del eje; las
   de `sigma` se nombran por componente (`sigma.accountability`,
   `sigma.transparency`, ...), y las de fronteras no reticulares conservan el
   nombre del campo afectado (p. ej. `herramientas`).
3. `fidelidad:` contiene exclusivamente los cinco ejes reticulares y `sigma`.
   Si una frontera no reticular pierde fidelidad, aparece además
   `fidelidad-campos: <campo>:partial`; cada campo listado DEBE tener su línea
   homónima en `perdidas:`. No se convierte ese campo en un eje. En ambos
   regímenes la fidelidad emitida solo toma `full` o `partial`: un eje `none`
   aborta (§3 r3) y `none` jamás llega al archivo.
4. Las líneas `preservado-por-construccion` y `declarado-no-mecanizado` son
   **FIJAS**, carácter por carácter. NO DEBE moverse jamás una ley declarada
   a la lista de preservadas (§6).
5. Determinismo: misma fuente → emisión byte-idéntica. Ninguna emisión lleva
   timestamp ni estado de máquina.
6. `contrato-conocimiento:` aparece **solo si** el artefacto declara
   `conocimiento` o `componible`, e inmediatamente **antes** de las dos líneas
   fijas (r4). Porta `ancla` (raíz del repo central / `$KORA_RAIZ`),
   `resolucion-bash`, `resolucion-lectura` y las listas
   `conocimiento`/`componible` de URN. El path NO se deriva del id del URN:
   `ley/2 §6` lo vincula al campo `nombre`, que puede diferir. Con Bash se usa
   el gesto canónico `kora.py nombre <URN>`; con acceso de solo lectura se busca
   la línea de frontmatter exacta `^urn: <URN>$` bajo `artefactos/` y se exige
   una única coincidencia. **Cero paths materializados**: el URN es la autoridad
   y el censo vivo resuelve el path. Es extensión aditiva (constitución §12.1):
   un artefacto sin corpus no porta el bloque y su emisión queda byte-idéntica.
   Encarna la doctrina de acceso de `urn:kora:kb:regimen-de-ley`.
7. Toda emisión `codex` declara
   `fidelidad-campos: herramientas:partial` y la pérdida tipada
   `herramientas: allowlist[<tools KORA>]->sin-allowlist-builtins-local`.
   Un custom agent puede estrechar sandbox, MCP y skills, pero no expresa una
   allowlist exacta de herramientas built-in por artefacto; además, las
   overrides vivas del turno padre prevalecen al delegar. El funtor preserva la
   lista fuente sin presentar una restricción instruccional como enforcement.

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

Firma del gesto: `transmutar --urn U --target T [--aplicar] [--stdout] [--proyecto PATH]`,
o en modo verificación `transmutar --paridad [--urn U] [--target T]` (§9.1).
Default: escribe bajo `_emision/{target}/...` (derivado, gitignored) y
reporta. `--stdout` imprime; `--aplicar` instala en el runtime real.

| Target | Forma | Emisión |
|---|---|---|
| `claude-code` | skill | `_emision/claude-code/skills/{nombre}/SKILL.md`; frontmatter `name`, `description` (+ `allowed-tools` como lista separada por comas si `herramientas` no es vacía); copia `referencias/` conservando su nombre si existe |
| `claude-code` | agente | `_emision/claude-code/agents/{nombre}.md`; frontmatter `name`, `description`, `tools` (lista separada por comas); body = body fuente; si `arnes` = `persona`, sección final `## Modos de invocacion` con la doctrina dual-mode (modo subagente batch vs modo persona por encarnación) |
| `codex` | skill | `_emision/codex/skills/{nombre}/SKILL.md`; frontmatter `name`, `description`; copia `referencias/` conservando su nombre |
| `codex` | agente | `_emision/codex/agents/{nombre}.toml`, custom agent nativo con `name`, `description` y `developer_instructions`; el cuerpo y el sello viajan dentro de `developer_instructions`. Si `forma: agente` (persona dual-mode), emite además `_emision/codex/skills/{nombre}/SKILL.md` y el sidecar `agents/openai.yaml` con `allow_implicit_invocation: false`: el TOML preserva delegación y el skill preserva encarnación explícita en el hilo principal. Si `forma: subagente`, solo emite TOML. No fija `model`: hereda la selección del runtime. Codex permite estrechar configuración del custom agent, pero no una allowlist exacta de built-ins; el sello declara la pérdida de campo sin fingir enforcement |
| `opencode` | skill | `_emision/opencode/skills/{nombre}/SKILL.md` (mismo formato codex) |
| `opencode` | agente | `_emision/opencode/agents/{nombre}.md`; frontmatter `description`, `mode: subagent` (forma `subagente`) o `mode: all` (forma `agente`: persona dual-mode, usable como primario y delegable como subagente; `all` es el default de opencode y preserva ambos modos del sello), y `permission:` con `<tool>: deny` para cada tool de **efecto externo** (`bash`, `webfetch`, `websearch`, `task`) que `herramientas` NO concede — frontera de capacidad en el idiom canónico de opencode (el objeto `tools` está deprecado desde v1.1.1; las read-ish e internas quedan en default). Paridad con el allowlist `tools` de claude-code |
| `openclaw` | skill | `_emision/openclaw/skills/{nombre}/SKILL.md`; frontmatter `name`, `description` (agentskills.io); copia `referencias/`. Las tools de openclaw son config-level (openclaw.json), no van en el frontmatter |
| `openclaw` | agente (forma `subagente`/`agente`/`plataforma`) | **workspace** `_emision/openclaw/workspaces/{nombre}/` con DOS archivos (§7.1): `AGENTS.md` = cuerpo sin el span `U_phen` + sello; `SOUL.md` = span de `U_phen` + sello (sólo si el `arnes` porta `U_phen`) |

### 7.1 La emisión de workspace de `openclaw`

`openclaw` es el único target cuyo objeto-runtime es un **workspace
multi-archivo** name-keyed (`workspaces/{agentId}/`), no un archivo único. La
doc de openclaw exige segregar **`AGENTS.md`** (operating instructions) de
**`SOUL.md`** (voz: «Keep AGENTS.md for operating rules. Keep SOUL.md for
voice»). La emisión:

1. **`AGENTS.md`** = el cuerpo sin el span delimitado de `U_phen` + sello.
   Siempre. Es la componente operativa del producto, sin frontmatter (los
   workspace files de openclaw son markdown plano).
2. **`SOUL.md`** = el span de `U_phen` + sello, emitido **sólo si** el `arnes`
   porta `U_phen` (`persona`, `orquestador`, `servicio`). El span sale del
   **centinela** `<!-- kora:soul -->…<!-- kora:soul:fin -->` del cuerpo
   (`ley/2 §10 r6`). Realiza la doctrina ya declarada del corpus
   (`urn:kora:kb:aufbau-persona-agente §3`, `urn:kora:artefacto:autoria-de-persona`):
   `SOUL.md = U_phen`.
   - Centinela ausente, desbalanceado o múltiple con `arnes` de `U_phen` ⇒
     `transmutar` FALLA (exit 1) nombrando que el núcleo no segmenta prosa y que
     el autor debe delimitar `U_phen`. **NUNCA se fabrica voz.**
   - `arnes` sin `U_phen` (`delegado`): se emite sólo `AGENTS.md`; no hay persona
     que segregar (openclaw tolera el `SOUL.md` ausente con un missing-file
     marker).
3. **Partición por rol nativo**: el centinela y su span se retiran de
   `AGENTS.md`; el contenido del span viaja una sola vez, en `SOUL.md`. El
   producto `AGENTS.md × SOUL.md` conserva la materia semántica completa y la
   **bisimulación módulo proyección** (§3), mientras los targets monolíticos
   conservan el cuerpo fuente verbatim. La voz no se inyecta dos veces ni se
   hereda como regla operativa por consumidores que sólo cargan `AGENTS.md`.
4. Ambos archivos portan el **mismo sello** (misma fuente, misma proyección):
   `hash-fuente` y vectores son los del artefacto fuente completo. Cada archivo
   se auto-certifica (§5).
5. **Calificación `mu=3` observable.** Si el artefacto fuente porta `mu=3`
   (materia ambiental always-on), el sello porta en la zona variable dos líneas:

   ```text
   realiza: workspace-mu3-conforme (AGENTS.md+SOUL.md; techo always-on, sin recorte de min)
   difiere: conducta-always-on (gateway/systemd/openclaw.json) -> deploy del fleet
   ```

   El funtor **realiza** la emisión del workspace conforme al techo always-on
   (`mu:3→3 full` es enunciado de **TIPO**: el techo lo admite sin recorte); la
   **conducta** always-on —el daemon vivo recordando entre sesiones (**TOKEN**)—
   es deploy del fleet, no función del funtor. La calificación vive en el
   **proof-carrier** (no sólo en esta ley): reconcilia el «openclaw no realizado»
   inmutable de `GENESIS §4` con el realizado registrado aquí, sin tercerizar la
   honestidad a una ley que no viaja con el artefacto. `mu<3` no porta la
   calificación (no hay always-on que diferir).

**Frontera declarada — lo que el funtor NO emite.** `IDENTITY.md`, `USER.md`,
`TOOLS.md`, `HEARTBEAT.md`, `BOOT.md`, `MEMORY.md`, `memory/`, y la config de
deploy (`openclaw.json`: model, tools, auth, telegram, systemd). No son doctrina
KORA: son scaffolding de workspace (bootstrap ritual / `openclaw setup`, que
siembra los faltantes sin sobrescribir) y deploy (operador). La **frontera de
capacidad** (`herramientas`) NO se materializa en el workspace —`TOOLS.md` es
guía, no controla disponibilidad—: se realiza en `openclaw.json` a nivel deploy.
El sello la declara en cada archivo OpenClaw con:

```text
frontera-herramientas-declarada: [<allowlist KORA>]
frontera-herramientas-realizacion: openclaw.json/deploy (fuera del funtor; no verificada por este sello)
```

El runtime la realiza por config. Ni el sello ni la paridad de archivos prueban
esa realización: el gate de deploy DEBE contrastar la declaración con la config
viva. `--aplicar` solo instala los factores emitidos y NO constituye ese gate.
No es pérdida de eje (no genera línea `perdidas:`): es arquitectura del target.

`--aplicar`: claude-code → `~/.claude/skills/{nombre}/` y
`~/.claude/agents/{nombre}.md`; codex → `~/.agents/skills/{nombre}/` y
`~/.codex/agents/{nombre}.toml`;
opencode → `~/.config/opencode/skills/{nombre}/` y
`~/.config/opencode/agents/{nombre}.md`; openclaw →
`~/openclaw-fleet/blueprints/{nombre}/` (escribe `AGENTS.md` [+ `SOUL.md`])
para el agente, y
`~/.openclaw/skills/{nombre}/` (managed skills) para la skill. En toda emisión y
aplicación la fibra `referencias/` conserva su nombre: el cuerpo emitido cita
paths `referencias/...` y ningún target exige otro nombre.

La aplicación de un agente OpenClaw es **fail-closed**: el nombre debe figurar
en `openclaw.json.reference.agents.list` de esa flota y el directorio
`blueprints/{nombre}/` debe preexistir como directorio real. KORA no lo crea.
Así `targets: [openclaw]` conserva la capacidad global de proyección sin
convertirse en membresía accidental de una flota. El blueprint sigue siendo
derivado declarativo; el deploy fleet lo materializa por copia en un workspace
runtime privado, preservando memoria y estado mutable.

Una **skill** es un producto cerrado: KORA administra el directorio
`skills/{nombre}/` completo, tanto en `_emision` como en el destino de
`--aplicar`. Re-transmutar y reaplicar lo materializan como el mapa exacto
`ruta-relativa → bytes` del producto vigente; ningún factor KORA anterior
sobrevive.

La exactitud comienza **después de adquirir la propiedad**, no antes. `nombre`
selecciona una ruta candidata; el último bloque `kora:sello` legible del
proof-carrier raíz debe atribuir la instalación al mismo `(URN,target)`.
`--aplicar` PUEDE crear una ruta ausente y PUEDE reemplazar o retirar una ruta
ya atribuida a ese par. Si el destino existe pero carece de ese sello —o porta
otro par— es un homónimo no atribuible: conflicto bloqueante, preservado sin
mutación. La regla cubre el `SKILL.md` raíz, los agentes de archivo único, el
TOML Codex y cada `AGENTS.md`/`SOUL.md` emitido para OpenClaw. Todos los
factores se validan antes de mutar uno; un directorio incompatible, symlink o
nodo especial tampoco transfiere propiedad y NUNCA se sigue, aunque aparezca
en un ancestro de la ruta final. La skill complementaria Codex obedece la misma
regla. Esta adquisición rige destinos instalados; `_emision/` ya es una zona
derivada y cerrada propiedad de KORA (constitución §6).
Esa propiedad autoriza reemplazar con `lstat` un leaf incompatible dentro de
`_emision/`, pero no atravesar un ancestro enlazado: todos los destinos de
emisión y toda limpieza de derivados se preflightan antes de mutar uno.

Toda unidad bajo `_emision/` es un derivado cerrado. El **blueprint OpenClaw
aplicado**, en cambio, es una superficie abierta: KORA gobierna por nombre
únicamente `AGENTS.md` y el `SOUL.md` efectivamente emitido. Si el producto
vigente deja de emitir `SOUL.md`, solo retira el residual cuando su sello lo
atribuye al mismo `(URN,target)`. Preserva los demás nombres del blueprint,
incluidos scaffolding y material ajeno. El workspace runtime privado queda
fuera: lo materializa el deploy fleet preservando memoria y estado mutable. Los
agentes de archivo único solo administran su archivo exacto y no tocan hermanos
del directorio.

`--proyecto PATH` (requiere `--aplicar`): redirige la instalación al nivel
**proyecto** — el `.opencode/`/`.claude/` del proyecto, no el home del operador.
claude-code → `PATH/.claude/skills/{nombre}/` y `PATH/.claude/agents/{nombre}.md`;
codex → `PATH/.agents/skills/{nombre}/` y `PATH/.codex/agents/{nombre}.toml`;
opencode → `PATH/.opencode/skills/{nombre}/` y `PATH/.opencode/agents/{nombre}.md`
(subdirectorios en **plural**, convención canónica de opencode: el `.opencode/` y
`~/.config/opencode/` usan nombres plurales; singular solo por retrocompat).
`openclaw` NO soporta nivel proyecto porque sus workspaces son user/fleet-level,
no de proyecto. La emisión canónica en `_emision/` no cambia; `--proyecto`
solo redirige el destino de `--aplicar`.

Codex y OpenClaw comparten la raíz personal Agent Skills
`~/.agents/skills`. OpenClaw le da mayor precedencia que a su raíz managed
`~/.openclaw/skills`. Por eso `--aplicar` rechaza una skill OpenClaw cuando ya
existe el homónimo en el layout directo que KORA usa para Codex
(`~/.agents/skills/{nombre}/SKILL.md`): instalar debajo no cambiaría la skill
efectiva en ningún agente. Este guard NO pretende resolver layouts personales
agrupados ni precedencias por workspace; el gate de deploy DEBE inspeccionar el
discovery efectivo por agente.

El gesto `--aplicar` **respeta y valida el campo `alcance`** del artefacto (ley/2
§3; ausente = `ambos`): un artefacto con `alcance: usuario` rechaza `--proyecto`;
uno con `alcance: proyecto` exige `--proyecto` (falla en la instalación
user-general); `ambos` admite cualquiera. El alcance es propiedad del artefacto,
ortogonal a `targets`: se determina en autoría, no en el gesto — el gesto solo lo
honra. La emisión canónica en `_emision/` es siempre alcance-neutral.

Los espacios de emisión por runtime son **planos** (un directorio por
`nombre`): dos artefactos con el mismo `nombre` y URN distinto NO DEBEN
emitirse — `transmutar` falla nombrando la colisión; renombra uno.
Antes de construir o retirar una ruta, `transmutar` exige el slug canónico
definido en `ley/2 §2.1`; cualquier otro `nombre` aborta sin mutar el producto.
`forma-valida` denuncia la misma incoherencia en el corpus.

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

Si existe `_emision/`, cada unidad descubierta DEBE ser congruente con tres
fuentes de identidad: archivo fuente actual, target de su ruta y generador
vigente. Check: `sello-fresco`.

El check lee el **último** bloque `kora:sello` de cada factor doctrinal —el
cuerpo puede citar sellos de ejemplo— y verifica:

1. el sello existe, su `target` coincide con la ruta, está declarado por la
   fuente y realizado por esta encarnación, y `hash-fuente` coincide con el
   sha256 actual del archivo fuente principal;
2. al regenerar en memoria el par `(URN,target)`, el conjunto y los bytes de
   todos los factores coinciden, incluidos sidecars sin sello;
3. para skills, los paths y bytes de `referencias/` coinciden con la fibra
   fuente, aunque esos archivos no participen en `hash-fuente`.

Una diferencia implica re-transmutar. Alcance honesto: si una unidad completa
no existe, este check no tiene un sello desde el cual descubrirla; la
completitud `activo→emisión` sigue perteneciendo a paridad (§9.1). La
congruencia byte a byte prueba forma producida, no verdad semántica ni las leyes
declaradas de §6.

### 9.1 Paridad de despliegue

La frescura tiene dos aguas. `sello-fresco` (§9) vigila **emisión↔fuente**;
la **paridad** vigila **emisión↔instalación**: que la frontera KORA gestionada
en el runtime de nivel usuario sea byte-idéntica a lo emitido. Gesto:
`transmutar --paridad [--urn U] [--target T]` — solo lectura; sin filtros
barre todas las emisiones.

Reglas:

1. Veredictos por unidad: `fiel` (frontera KORA gestionada byte-idéntica),
   `desviada` (drift bloqueante), `no-instalada` (la unidad KORA no está
   materializada; informativo, porque el gesto no decide dónde desplegar) y
   `sin-emision` (un artefacto `activo` promete el target pero no tiene la
   unidad derivada correspondiente). Son `desviada`, entre otros: bytes distintos, factor
   gestionado sobrante, nodo de tipo incompatible, symlink o nodo especial,
   homónimo no atribuible en una ruta que KORA necesitaría adquirir y residuo
   atribuible de una fuente que ya no está activa o cuyo producto vigente ya no
   contiene esa unidad.
   La enumeración tampoco sigue enlaces en `_emision/`: una raíz, colección o
   unidad no regular produce drift. Dos productos emitidos que colapsen al
   mismo `(target,tipo,nombre)` producen un único veredicto `desviada` por
   emisión ambigua, nunca veredictos contradictorios. La inspección runtime
   aplica el mismo no-seguimiento a todos los ancestros de la ruta.
2. Exit 1 si existe alguna `desviada` o `sin-emision`; el veredicto es
   transmutar lo faltante y, solo para drift activo en una ruta ausente o
   atribuida, re-transmutar `--aplicar`. Un conflicto de propiedad exige
   adjudicación y un residual no vigente exige retirada manual: la recomendación
   automática NO DEBE destruir un homónimo ni fingir que una fuente inactiva
   admite reaplicación. `no-instalada` no falla.
3. En una skill, `fiel` exige igualdad exacta del mapa
   `ruta-relativa → bytes`, una vez demostrada la atribución del directorio: un
   factor instalado sobrante también es drift. En un blueprint OpenClaw
   aplicado solo se comparan los nombres emitidos y un `SOUL.md` residual cuyo
   sello lo atribuya al mismo `(URN,target)`; los demás nombres y el workspace
   runtime privado quedan fuera (§7.1). Una skill complementaria Codex
   histórica que siga atribuida a la misma fuente pero ya no forme parte del
   producto vigente es
   `desviada`; su limpieza no presupone ni legitima una democión de forma
   (`ley/2 §7.1`). El barrido residual prueba ambos tipos de ruta por cada URN:
   así una promoción legal de forma no oculta el producto anterior, sin
   convertir su ausencia en obligación de despliegue. La atribución se deriva
   del corpus y la instalación, no de la presencia ni salud de `_emision/`.
   En la superficie abierta OpenClaw, un blueprint preexistente sin ninguno de
   los factores KORA emitidos ni residuales atribuibles es `no-instalada`: el
   scaffolding contenedor no equivale a despliegue. Un factor ajeno presente
   bloquea solo si ocupa un nombre que el producto intenta gestionar.
4. Alcance honesto: la paridad cubre las instalaciones de **nivel
   usuario/flota** (las rutas de `--aplicar`); las instalaciones `--proyecto`
   quedan fuera del barrido (declarado, no mecanizado).
5. La paridad NO es check de `velar` (registro cerrado, constitución §11):
   `velar` vela el corpus; la paridad mira el mundo. Por eso vive como modo
   del gesto `transmutar`, que ya gobierna la relación IR↔runtime.
6. La completitud se deriva de los artefactos agénticos `activos` y sus
   `targets` realizados. Una persona Codex promete dos unidades —custom agent
   y skill explícita—; un subagente Codex promete una. Un directorio sin su
   archivo raíz (`SKILL.md` o `AGENTS.md`) no constituye una unidad emitida.
   Esta promesa exige **emisión**, no instalación: cada runtime se despliega de
   forma independiente y una unidad ausente puede seguir siendo
   `no-instalada` sin conflicto.
7. Si una skill managed OpenClaw existe pero el homónimo del layout personal
   Codex/KORA también existe, la unidad es `desviada`, no `fiel`. Otras fuentes
   de precedencia permanecen fuera de este barrido y pertenecen al deploy.
Rationale (2026-07-06): cinco agentes corrieron días desactualizados en los
runtimes de escritorio sin que ningún gesto lo viera — la fuente avanzó, la
emisión se regeneró, la instalación quedó atrás. `velar` verde no lo detecta
por diseño (vela la forma del corpus, no el mundo); este modo cierra esa
clase de fallos sin fingir que la instalación es corpus.

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
| `nombre` seguro como componente de ruta antes de reconciliar | ley/2 §2.1, §7 | mecanizado (`forma-valida`, `transmutar`) |
| Propiedad de toda ruta instalada antes de reemplazar o retirar | §7: sello `(URN,target)`; homónimo preservado; preflight de factores y ancestros | mecanizado (`transmutar --aplicar`) |
| Frontera `herramientas` de Codex declarada como pérdida no reticular tipada | §5 r3/r7, §7 | mecanizado (`transmutar`) |
| Frontera `herramientas` de OpenClaw declarada; realización config diferenciada | §7.1 | declaración mecanizada (`transmutar`); realización verificada en deploy |
| Emisión de workspace `openclaw` (AGENTS.md + SOUL.md) | §7.1 | mecanizado (`transmutar`) |
| Centinela `kora:soul` requerido para `SOUL.md` de `arnes` con `U_phen` | §7.1, ley/2 §10 r6 | mecanizado (`transmutar`) |
| Sello con formato exacto al emitir | §5 | mecanizado (`transmutar`) |
| Congruencia fuente↔generador↔producto (sidecars y `referencias/` incluidos) | §9 | mecanizado (`sello-fresco`) |
| Paridad exacta y tipada de la superficie KORA (emisión↔instalación de nivel usuario) | §9.1: incluye residuos atribuibles, conflictos de propiedad y nodos no regulares | mecanizado (`transmutar --paridad`) |
| Completitud artefacto activo→emisión por target | §9.1 | mecanizado (`sin-emision`) |
| Target de transmutación declarado por la fuente | §2 r4 | mecanizado (`transmutar`) |
| Aplicación solo de artefactos activos | §2 r5 | mecanizado (`transmutar --aplicar`) |
| Paridad de instalaciones `--proyecto` | §9.1 r4 | declarado |
| Determinismo byte-idéntico | §5 r5 | mecanizado (sin timestamps; cubierto por tests) |
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

v1.3.0 (HITL 2026-07-01): **realiza el target `openclaw`** (`T-openclaw-pneuma-v1`).
§1.1 legisla el transporte de fibra universal (lift cartesiano); §2 pasa
`openclaw` a realizado; §4.4 la matriz (μ:3, ξ:4 full — techo más alto;
σ-max `[3,3,3,3,2]`); §7/§7.1 la emisión de **workspace** multi-archivo
(`AGENTS.md` = cuerpo verbatim, `SOUL.md` = span de `U_phen` por el centinela
`kora:soul`), la decisión duplicación-no-partición (preserva bisimulación), la
frontera no-emitida (IDENTITY/USER/TOOLS/HEARTBEAT/BOOT/config = scaffolding y
deploy), `--aplicar` a `~/openclaw-fleet/workspaces/{nombre}/`, y la
**calificación `mu=3` observable** en el sello (§7.1 r5: `realiza`/`difiere` —
el funtor realiza la emisión conforme al techo always-on, difiere la conducta
always-on al deploy; reconcilia GENESIS↔realizado en el proof-carrier).
**Registra el cierre de la deuda de `GENESIS §4` (μ=3) sin editar GENESIS** (acta inmutable).
Reintroduce, con la anatomía openclaw REAL verificada (workspace multi-archivo,
no el monolito tipo-Hermes del intento revertido `8ef7c6e`), la matriz y el
transporte que ya eran correctos. `hermes` sigue reconocido-no-realizado.

v1.4.0 (HITL 2026-07-06): §9.1 legisla la **paridad de despliegue**
(`transmutar --paridad`) — la segunda agua de la frescura: emisión↔instalación
de nivel usuario, con veredictos `fiel`/`desviada`/`no-instalada` y exit 1
ante drift. Es modo del gesto existente: no altera los seis gestos (`ley/0
§10`) ni el registro cerrado de checks (`ley/0 §11`). Extensión aditiva
(constitución §12.1): minor. Motivada por el deploy 2026-07-06, que halló
cinco instalaciones stale silenciosas en runtimes de escritorio.

v2.0.0 (HITL 2026-07-12): reemplaza `T-codex-pneuma-v1` por
`T-codex-pneuma-v2`. El target Codex deja de colapsar agentes a skills: usa
custom agents TOML nativos y conserva el modo persona con un skill explícito
no invocable implícitamente; adopta las rutas oficiales globales y de proyecto,
sin fijar modelo. Añade enforcement de `targets`, despliegue solo desde
`estado: activo` y completitud `activo→emisión` en paridad. Es major porque
cambia rutas, forma de emisión y el identificador del sello Codex; medió la
decisión explícita del operador de ejecutar la migración Claude Code→Codex.

v2.1.0 (2026-07-16): corrige dos pérdidas ocultas del despliegue Codex. La
doctrina dual-mode deja de nombrar `Task()` (mecanismo exclusivo de Claude
Code) y pasa a describir la delegación nativa del runtime. Toda emisión Codex
porta ahora la allowlist KORA `herramientas` como pérdida declarada hacia la
superficie/permisos heredados de la sesión padre: el runtime no ofrece
allowlist nativa de built-ins por artefacto. Extensión proof-carrying aditiva y
precisión compatible; `T-codex-pneuma-v2` conserva su identidad major.

v2.2.0 (2026-07-16): corrige el contrato de resolución del sello: el id del URN
no se confunde con `nombre`; el consumidor usa `kora.py nombre <URN>` o búsqueda
exacta y única en el corpus. OpenClaw pasa de duplicar `U_phen` a distribuir el
producto nativo (`AGENTS.md` operativa, `SOUL.md` voz), sin alterar el cuerpo de
los demás targets. Cada sello OpenClaw porta además la frontera `herramientas`
declarada y confiesa que su realización en `openclaw.json` sólo se verifica en
deploy. Corrección compatible del workspace vigente; conserva
`T-openclaw-pneuma-v1`.

v2.3.0 (2026-07-16): separa la fidelidad reticular de la fidelidad de campos;
Codex declara `herramientas:partial` con codominio homogéneo
`sin-allowlist-builtins-local`. `sello-fresco` regenera cada par `(URN,target)`
y compara el producto completo, incluidos sidecars y `referencias/`, cerrando
el drift silencioso del generador; también rechaza targets no declarados o no
realizados. Paridad deja de contar como emitida una unidad sin archivo raíz.
La aplicación/paridad evita además la copia managed OpenClaw que quedaría bajo
la skill personal Codex homónima. Precisión compatible; conserva los ids de
funtor y del check.

v2.4.0 (2026-07-17): hace cerrados y exactos los directorios de skills en
emisión, aplicación y paridad; un factor instalado sobrante deja de producir
un falso `fiel`, y re-transmutar/reaplicar cierra el ciclo retirándolo. Mantiene
abiertas las superficies OpenClaw: solo retira un `SOUL.md` no emitido cuando el
sello lo atribuye al mismo par KORA, y preserva memoria,
scaffolding y material ajeno. También retira de forma atribuida una skill
complementaria Codex histórica ausente del producto vigente, y rechaza nombres
que no sean componentes de ruta seguros antes de cualquier limpieza. Endurece
la frontera name-keyed sin cambiar los ids de funtor ni del check.

v2.5.0 (2026-07-17): distingue capacidad global de proyección y membresía de
una flota. Un agente con `target: openclaw` puede emitirse para cualquier
consumidor, pero `--aplicar` sobre `openclaw-fleet` exige roster positiva en
`openclaw.json.reference` y un blueprint real preexistente; nunca crea
membresía por efecto colateral. La aplicación escribe el blueprint declarativo
y deja la materialización del workspace privado al deploy fleet. No cambia los
ids de funtor ni el carácter informativo de `no-instalada`.

v2.6.0 (2026-07-17): separa identidad nominal de propiedad operacional. Toda
ruta instalada solo puede reconciliarse destructivamente tras atribuir su sello
al mismo `(URN,target)`; el preflight es completo y un homónimo no atribuible se
preserva y bloquea. Paridad trata como drift los conflictos de tipo o propiedad,
symlinks, nodos especiales, emisiones ambiguas y residuos atribuibles aun sin
derivado local o tras promoción de forma, manteniendo `no-instalada`
informativo y el despliegue independiente por runtime. Precisa además la
frontera abierta OpenClaw —un blueprint vacío sigue no instalado—, preflighta
emisión e instalación sin seguir ancestros y describe la limpieza de companions
históricos sin normalizar la democión prohibida por `ley/2`.
