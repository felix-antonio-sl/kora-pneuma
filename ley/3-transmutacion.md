# KORA/Transmutación — ley pneuma v2.0.0

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

1. La proyección del vector la hace `T` sobre la base (matrices §4). El cuerpo
   NO se proyecta: se transporta entero al archivo que el target reserva para la
   operativa (`SKILL.md`, `{nombre}.md`, o `AGENTS.md` en `openclaw`).
2. Este transporte vale para **todos** los targets, sin campo por-emisión que lo
   declare: es la forma del funtor, no un atributo del artefacto.
3. Un target cuyo objeto-runtime es un **producto de archivos** (un workspace,
   p. ej. `openclaw`) recibe el cuerpo en su archivo de operativa y PUEDE además
   proyectar **componentes adicionales** del producto (p. ej. `SOUL.md` = el span
   de `U_phen`); cada componente adicional sale de un **span marcado** del cuerpo
   (`ley/2 §10 r6`), nunca de una segmentación de prosa por el núcleo
   (forma-no-verdad). Esto preserva la bisimulación módulo proyección (§3): el
   cuerpo completo viaja al archivo de operativa en TODOS los targets.

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
| `codex` | agente | `_emision/codex/agents/{nombre}.toml`, custom agent nativo con `name`, `description` y `developer_instructions`; el cuerpo y el sello viajan dentro de `developer_instructions`. Si `forma: agente` (persona dual-mode), emite además `_emision/codex/skills/{nombre}/SKILL.md` y `agents/openai.yaml` con `allow_implicit_invocation: false`: el TOML preserva delegación y el skill preserva encarnación explícita en el hilo principal. Si `forma: subagente`, solo emite TOML. No fija `model`: hereda la selección del runtime |
| `opencode` | skill | `_emision/opencode/skills/{nombre}/SKILL.md` (mismo formato codex) |
| `opencode` | agente | `_emision/opencode/agents/{nombre}.md`; frontmatter `description`, `mode: subagent` (forma `subagente`) o `mode: all` (forma `agente`: persona dual-mode, usable como primario y delegable como subagente; `all` es el default de opencode y preserva ambos modos del sello), y `permission:` con `<tool>: deny` para cada tool de **efecto externo** (`bash`, `webfetch`, `websearch`, `task`) que `herramientas` NO concede — frontera de capacidad en el idiom canónico de opencode (el objeto `tools` está deprecado desde v1.1.1; las read-ish e internas quedan en default). Paridad con el allowlist `tools` de claude-code |
| `openclaw` | skill | `_emision/openclaw/skills/{nombre}/SKILL.md`; frontmatter `name`, `description` (agentskills.io); copia `referencias/`. Las tools de openclaw son config-level (openclaw.json), no van en el frontmatter |
| `openclaw` | agente (forma `subagente`/`agente`/`plataforma`) | **workspace** `_emision/openclaw/workspaces/{nombre}/` con DOS archivos (§7.1): `AGENTS.md` = cuerpo verbatim + sello; `SOUL.md` = span de `U_phen` + sello (sólo si el `arnes` porta `U_phen`) |

### 7.1 La emisión de workspace de `openclaw`

`openclaw` es el único target cuyo objeto-runtime es un **workspace
multi-archivo** name-keyed (`workspaces/{agentId}/`), no un archivo único. La
doc de openclaw exige segregar **`AGENTS.md`** (operating instructions) de
**`SOUL.md`** (voz: «Keep AGENTS.md for operating rules. Keep SOUL.md for
voice»). La emisión:

1. **`AGENTS.md`** = el cuerpo **verbatim** + sello. Siempre. Es el transporte de
   fibra de §1.1: el mismo cuerpo que reciben todos los targets, en el archivo de
   operativa. Sin frontmatter (los workspace files de openclaw son markdown
   plano).
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
3. **Decisión duplicación, no partición**: el span de `U_phen` permanece en
   `AGENTS.md` (es parte del cuerpo verbatim) y se **copia** a `SOUL.md`. Así el
   `AGENTS.md` de openclaw es idéntico al cuerpo que reciben los demás targets, y
   se preserva la **bisimulación módulo proyección** (§3): el agente no cambia de
   doctrina según el runtime. La doc de openclaw es asimétrica —prohíbe operativa
   en `SOUL.md`, no voz en `AGENTS.md`—: la duplicación la honra (`SOUL.md` queda
   voz pura).
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
El sello la declara; el runtime la enforce por config. No es pérdida de eje (no
genera línea `perdidas:`): es arquitectura del target.

`--aplicar`: claude-code → `~/.claude/skills/{nombre}/` y
`~/.claude/agents/{nombre}.md`; codex → `~/.agents/skills/{nombre}/` y
`~/.codex/agents/{nombre}.toml`;
opencode → `~/.config/opencode/skills/{nombre}/` y
`~/.config/opencode/agents/{nombre}.md`; openclaw → workspace
`~/openclaw-fleet/workspaces/{nombre}/` (escribe `AGENTS.md` [+ `SOUL.md`];
name-keyed, sobrescribe por nombre, sin never-overwrite) para el agente, y
`~/.openclaw/skills/{nombre}/` (managed skills) para la skill. En toda emisión y
aplicación la fibra `referencias/` conserva su nombre: el cuerpo emitido cita
paths `referencias/...` y ningún target exige otro nombre.

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

### 9.1 Paridad de despliegue

La frescura tiene dos aguas. `sello-fresco` (§9) vigila **emisión↔fuente**;
la **paridad** vigila **emisión↔instalación**: que lo que corre en el runtime
de nivel usuario sea byte-idéntico a lo emitido. Gesto:
`transmutar --paridad [--urn U] [--target T]` — solo lectura; sin filtros
barre todas las emisiones.

Reglas:

1. Veredictos por unidad de emisión: `fiel` (instalación byte-idéntica),
   `desviada` (instalación presente que difiere — stale porque la fuente
   avanzó, o editada en el runtime: ambas son drift), `no-instalada`
   (informativo: el gesto no decide si un artefacto debe estar instalado), y
   `sin-emision` (un artefacto `activo` promete el target pero no tiene la
   unidad derivada correspondiente).
2. Exit 1 si existe alguna `desviada` o `sin-emision`; el veredicto es
   transmutar lo faltante y re-transmutar `--aplicar` lo desviado (o auditar la
   edición hecha en el runtime). `no-instalada` no falla.
3. Solo se comparan los archivos que la emisión contiene: el scaffolding del
   workspace y la memoria del runtime quedan fuera (frontera no-emitida,
   §7.1).
4. Alcance honesto: la paridad cubre las instalaciones de **nivel
   usuario/flota** (las rutas de `--aplicar`); las instalaciones `--proyecto`
   quedan fuera del barrido (declarado, no mecanizado).
5. La paridad NO es check de `velar` (registro cerrado, constitución §11):
   `velar` vela el corpus; la paridad mira el mundo. Por eso vive como modo
   del gesto `transmutar`, que ya gobierna la relación IR↔runtime.
6. La completitud se deriva de los artefactos agénticos `activos` y sus
   `targets` realizados. Una persona Codex promete dos unidades —custom agent
   y skill explícita—; un subagente Codex promete una.

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
| Emisión de workspace `openclaw` (AGENTS.md + SOUL.md) | §7.1 | mecanizado (`transmutar`) |
| Centinela `kora:soul` requerido para `SOUL.md` de `arnes` con `U_phen` | §7.1, ley/2 §10 r6 | mecanizado (`transmutar`) |
| Sello con formato exacto al emitir | §5 | mecanizado (`transmutar`) |
| Emisión fresca (presencia de sello + `hash-fuente` actual, último bloque) | §9 | mecanizado (`sello-fresco`) |
| Paridad de despliegue (emisión↔instalación de nivel usuario) | §9.1 | mecanizado (`transmutar --paridad`) |
| Completitud artefacto activo→emisión por target | §9.1 | mecanizado (`sin-emision`) |
| Target de transmutación declarado por la fuente | §2 r4 | mecanizado (`transmutar`) |
| Aplicación solo de artefactos activos | §2 r5 | mecanizado (`transmutar --aplicar`) |
| Paridad de instalaciones `--proyecto` | §9.1 r4 | declarado |
| Buena forma completa del sello en emisiones ya escritas | §5, §9 | declarado |
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
