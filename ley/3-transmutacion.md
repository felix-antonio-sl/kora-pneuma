# KORA/Transmutación — ley pneuma v1.2.0

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
| `openclaw` | reconocido, no realizado | falla (exit 1) con mensaje honesto |
| `hermes` | reconocido, no realizado | falla (exit 1) con mensaje honesto |

1. `targets` DEBE ser subconjunto de los cinco reconocidos (check
   `targets-conocidos`, ley/2).
2. Un artefacto PUEDE declarar `openclaw` o `hermes` en `targets` — la ley
   los reconoce — pero transmutar hacia ellos DEBE fallar con mensaje que
   remita a `GENESIS.md`. La ley no nombra capacidades inexistentes como si
   existieran.
3. El identificador del funtor DEBE ser `T-{target}-pneuma-v1`. Funtores
   vigentes: `T-claude-code-pneuma-v1`, `T-codex-pneuma-v1`,
   `T-opencode-pneuma-v1`.

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

`--aplicar`: claude-code → `~/.claude/skills/{nombre}/` y
`~/.claude/agents/{nombre}.md`; codex → `~/.codex/skills/{nombre}/`;
opencode → `~/.config/opencode/skills/{nombre}/` y
`~/.config/opencode/agents/{nombre}.md`. En toda emisión y aplicación la
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
