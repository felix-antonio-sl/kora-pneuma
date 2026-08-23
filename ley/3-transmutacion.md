# KORA/Transmutación — ley pneuma v5.1.0

Estrato 3 de la ley. Gobierna el gesto `transmutar`: la proyección reticular
de una firma y la serialización del artefacto para un runtime concreto.

## 1. Principio

> **La proyección de firmas es un coreflector; la emisión es determinista y
> toda pérdida se declara, nunca se oculta.**

Para cada target realizado `T`, las firmas proyectables forman una categoría
delgada `D_T`; la imagen soportada forma `I_T`. La operación componente a
componente

```text
P_T(v) = min(v, techo_T)
```

es un funtor `P_T: D_T → I_T`, derecho adjunto a la inclusión
`J_T: I_T ↪ D_T`. La prueba completa vive en
`urn:kora:kb:cat-kora-kernel`.

El emisor toma después el artefacto validado y produce archivos de runtime. Es
una compilación/serialización determinista, no un funtor demostrado: KORA no
ha definido categorías de artefactos y productos runtime ni la acción del
emisor sobre morfismos. Encarnar viene acompañado de evidencia verificable en
el sello (§5).

### 1.1 Transporte de contenido (todos los targets)

La implementación trata la firma como datos proyectables y el cuerpo como
contenido. En targets monolíticos el cuerpo viaja **verbatim** al archivo de
operativa. «Base» y «fibra» pueden servir como intuición de diseño, pero no se
declara una fibración ni un lift cartesiano: faltan la categoría total, la
proyección y la propiedad universal correspondiente.

Reglas:

1. La proyección de la firma la hace `P_T` (matrices §4). En targets
   monolíticos el cuerpo NO se proyecta: se transporta entero al archivo que el
   target reserva para el contrato (`SKILL.md`, `{nombre}.md` o el `SOUL.md`
   de un perfil Hermes).
2. Este transporte vale para **todos** los targets, sin campo por-emisión que lo
   declare: es una regla del emisor, no un atributo del artefacto.
3. Un target cuyo objeto-runtime es un **producto de archivos** PUEDE distribuir
   un componente marcado del cuerpo al archivo nativo que le corresponde. En
   `openclaw`, `AGENTS.md` recibe la operativa sin el span `U_phen` y `SOUL.md`
   recibe ese span. El producto conserva la materia completa sin duplicarla;
   cada componente sale de un **span marcado** (`ley/2 §10 r6`), nunca de una
   segmentación de prosa por el núcleo (forma-no-verdad). Los demás targets
   conservan el cuerpo completo verbatim. Una distribución de perfil Hermes
   también es multiarchivo, pero `distribution.yaml` es metadata derivada y el
   cuerpo completo viaja monolítico en `SOUL.md`: no se infiere una partición.

## 2. Targets reconocidos y realizados

| Target | Estatus | `transmutar` |
|---|---|---|
| `claude-code` | realizado | emite |
| `codex` | realizado | emite |
| `opencode` | realizado | emite |
| `openclaw` | realizado | emite (workspace, §7) |
| `hermes` | realizado (habilidad y agente completo, §7.5) | emite; `subagente` falla cerrado |

1. `targets` es opcional. Si se declara, DEBE ser una lista no vacía y
   subconjunto de los cinco reconocidos (check `targets-conocidos`, ley/2).
2. `hermes` está **realizado** desde v3.0.0 para la forma habilidad mediante
   `T-hermes-pneuma-v1` y desde v4.0.0 para la forma `agente` mediante una
   distribución nativa de perfil `T-hermes-pneuma-v2` (§7.5). La forma
   `subagente` sigue fallando cerrada: un perfil es un agente completo, no un
   delegado invocable dentro de otro. Esto cierra la deuda histórica de
   `GENESIS §4` sin editar el acta. `openclaw` está realizado desde v1.3.0 por
   la misma regla de cierre.
3. El campo histórico `funtor` del sello identifica la versión del contrato de
   emisión; el nombre se conserva para no invalidar productos. Identificadores
   vigentes: `T-claude-code-pneuma-v1`, `T-codex-pneuma-v2`,
   `T-opencode-pneuma-v1`, `T-openclaw-pneuma-v1`,
   `T-hermes-pneuma-v1` (skill) y `T-hermes-pneuma-v2` (perfil). La v2 de Codex reemplaza
   el antiguo colapso agente→skill por custom agents nativos (§7).
4. Una fuente sin `targets` es agnóstica al runtime. `transmutar --urn U` elige
   **Codex** como target operacional principal; otro target realizado solo se
   usa mediante `--target T` explícito. Esta selección situada no altera la
   identidad ni el dominio de autoría de la fuente.
5. Si la fuente declara `targets`, la lista es una allowlist de compatibilidad
   mantenida y `transmutar --target T` exige que contenga `T`. Codex es el único
   camino principal; los demás adaptadores se conservan y verifican bajo
   demanda, sin que su estado redefina la salud ordinaria de Codex.
6. La emisión histórica puede producirse desde cualquier estado válido, pero
   `--aplicar` exige `estado: activo`. Un artefacto deprecado o retirado se
   conserva y resuelve; no se reinstala como si siguiera vigente.

## 3. Leyes de la proyección reticular

| Ley | Enunciado | Garantía |
|---|---|---|
| Composición | `P_T(f ∘ g) = P_T(f) ∘ P_T(g)` en las categorías delgadas | por monotonía |
| Identidad | `P_T(id_v) = id_{P_T(v)}` | por monotonía |
| Monotonía | si `v1 ≤ v2`, entonces `P_T(v1) ≤ P_T(v2)` en los cinco ejes y cinco componentes de `sigma` | por `min` |
| Descenso | `P_T(v) ≤ v` | por `min` |
| Idempotencia | `P_T(P_T(v)) = P_T(v)` | por `min` |
| Coreflexión | `J_T(a) ≤ d ⇔ a ≤ P_T(d)` para `a ∈ I_T`, `d ∈ D_T` | demostrada |
| Antitonicidad de fidelidad | si la demanda `x ≤ y`, entonces `fid_T(y) ≤ fid_T(x)` en `none ≤ partial ≤ full` | matrices exhaustivamente verificadas |

Reglas:

1. NUNCA se proyecta hacia arriba: ningún eje emite un valor mayor que el
   declarado en la fuente.
2. Composición e identidad se refieren solo a `P_T` entre categorías delgadas,
   no a la emisión de archivos.
3. Si algún eje proyecta a ∅ (sin valor target), la firma está fuera de `D_T`
   y la transmutación DEBE fallar
   (exit 1) con mensaje que nombre el eje, el valor fuente y el runtime que
   sí lo soporta. NUNCA degradación silenciosa.
4. Toda pérdida —reticular o de campo no reticular— DEBE declarar fidelidad
   `partial` en su régimen y aparecer en el sello con razón.
5. NO DEBE declararse fidelidad `full` para la dimensión donde hay pérdida
   real. La fidelidad de campos no inventa ejes nuevos (§5 r3).

La última ley equivale a un funtor:

```text
fid_Te : C_e^op -> {none <= partial <= full}
```

para cada cadena de demanda fuente `C_e`; `sigma` satisface la misma ley desde
el opuesto del producto `[0,3]^5`. Este funtor califica preservación y no
reemplaza `P_T`: una celda puede conservar el ordinal y seguir siendo
`partial` por semántica incompleta del runtime. La prueba vive en
`urn:kora:kb:cat-kora-kernel` §5.

La frase heredada **bisimulación módulo proyección** se conserva solo como
hipótesis de investigación. No hay funtor de conducta, lifting de relaciones
ni equivalencia observacional definidos que permitan formularla como
proposición; el sello no la afirma ni la prueba.

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

La frase histórica `operad dinámica` que persiste en algunas razones de
pérdida es una etiqueta estable para el nivel ordinal `xi=4`; no afirma que el
runtime ni KORA construyan una operad matemática.

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

El **techo transportable más alto** de los cinco targets: meta-runtime ACP +
systemd always-on + agentToAgent. Es el único adaptador vigente que transporta
una fuente `mu`=3, el único con `xi`=4 full y el único que proyecta
`lambda`=3 (partial). Fiel a la runtime-extension openclaw de la bestia y
confirmada contra el openclaw real (`~/openclaw-fleet/`, `docs.openclaw.ai`).

| Eje | Proyecciones |
|---|---|
| `pi` | 0→0, 1→1, 2→2, 3→3 full — delegación jerárquica recursiva vía ACP dispatch |
| `mu` | 0→0, 1→1, 2→2, 3→3 full — always-on vía systemd + Telegram; único adaptador vigente que transporta una fuente μ=3 |
| `xi` | 0→0, 1→1, 2→2, 3→3, 4→4 full — delegación jerárquica dinámica vía ACP + agentToAgent; preservar el ordinal no realiza una operad matemática |
| `lambda` | 0→0, 1→1, 2→2 full · 3→3 partial — society-in-the-loop requiere gobernanza externa no modelada en runtime |
| `phi` | 0→0, 1→1, 2→2 full · 3→3 partial — cognición híbrida parcial (no HAJCS completo) · 4→∅ none — co-evolutivo no modelado |
| `sigma` | máx soportado `[3,3,3,3,2]` — sustainability ambiental no medida directamente |

Consecuencia: agentes `plataforma`/`servicio` (μ=3) — sin hogar en los otros
targets, que abortan μ=3 — encuentran hogar pleno en `openclaw`. Sólo `phi`=4
aborta (none, igual que el resto).

### 4.5 `hermes`

Igual a `claude-code` en todos sus ejes salvo `mu`: el gateway siempre-activo
modela materia ambiental (`mu:3 full`) en la capacidad del runtime. Fuente
canónica del contrato: la documentación oficial de skills, perfiles y gateway
en `hermes-agent.nousresearch.com/docs`, verificada en vivo el 2026-08-23.

| Eje | Proyecciones |
|---|---|
| `pi` | 0→0, 1→1, 2→2 full · 3→2 partial — delegación jerárquica acotada por toolset, sin árbol nativo de perfiles |
| `mu` | 0→0, 1→1, 2→2 full · 3→3 full — always-on vía gateway systemd; techo de RUNTIME: una fuente habilidad sigue limitada por `dominio-forma` (ley/2, mu ∈ {0,1}) |
| `xi` | 0→0, 1→1, 2→2 full · 3→2 partial (multi-fase se aplana) · 4→2 partial (operad dinámica no soportada) |
| `lambda` | 0→0, 1→1, 2→1 partial — ecosistema colapsa a organizacional · 3→∅ none — society-in-the-loop no soportado |
| `phi` | 0→0, 1→1 full · 2→2 partial — colaborativo vía Bot Mode y grupos, con continuidad efectiva dependiente del deploy · 3→2 partial — cognición híbrida no nativa · 4→∅ none — co-evolutivo no soportado |
| `sigma` | máx soportado `[3,2,2,2,1]` |

El contrato `T-hermes-pneuma-v1` cubre sólo la forma habilidad y, por
`dominio-forma`, no alcanza `mu=3`. `T-hermes-pneuma-v2` cubre la forma
`agente`: si la fuente declara `mu=3`, el perfil se emite conforme al techo,
pero el sello difiere la conducta always-on al gateway y a la configuración
del deploy (§7.5). Preservar el ordinal prueba compatibilidad de tipo, no un
daemon vivo. La forma `subagente` no pertenece al dominio de este transporte.

## 5. El sello

Todo factor doctrinal emitido (`SKILL.md`, agente, `AGENTS.md`, `SOUL.md`) DEBE
terminar con un sello de procedencia y congruencia: comentario HTML, formato
EXACTO, **sin timestamp** — el hash identifica los bytes de la fuente, no una
identidad semántica. Los sidecars de runtime —incluidos
`agents/openai.yaml` de una skill Codex y `distribution.yaml` de un perfil
Hermes— y el contenido auxiliar
`referencias/` no duplican el sello; pertenecen al mismo producto y
`sello-fresco` prueba sus bytes contra el generador (§9).

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

Si el artefacto declara `conocimiento`, `depende` o `componible`, el sello incluye
además —entre `perdidas:` y las dos líneas fijas— un bloque
`contrato-conocimiento:` (r6):

```text
contrato-conocimiento:
  ancla: ~/kora-pneuma  (o $KORA_RAIZ)
  resolucion-bash: python3 {ancla}/kora.py nombre <URN>
  resolucion-lectura: Grep exacto '^urn: <URN>$' bajo {ancla}/artefactos; exigir coincidencia unica
  conocimiento: urn:fxsl:kb:icas-sintesis
  depende: urn:dev:artefacto:ship-discipline
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
   a la lista de preservadas (§6). El campo histórico `funtor` y estas líneas
   son identificadores estables del contrato; su literal no amplía el alcance
   matemático definido en §1 y §3.
5. Determinismo: misma fuente → emisión byte-idéntica. Ninguna emisión lleva
   timestamp ni estado de máquina.
6. `contrato-conocimiento:` aparece **solo si** el artefacto declara
   `conocimiento`, `depende` o `componible`, e inmediatamente **antes** de las dos líneas
   fijas (r4). Porta `ancla` (raíz del repo central / `$KORA_RAIZ`),
   `resolucion-bash`, `resolucion-lectura` y las listas
   `conocimiento`/`depende`/`componible` de URN. El path NO se deriva del id del URN:
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
   overrides vivas del turno padre prevalecen al delegar. El emisor conserva la
   lista fuente sin presentar una restricción instruccional como enforcement.

## 6. La nota de honestidad (heredada)

El sello conserva dos listas históricas; esta ley precisa su alcance:

- **preservado-por-construccion**: `composicion`, `identidad`,
  `monotonia-pi`, `monotonia-mu`, `monotonia-xi`. El núcleo las realiza
  al proyectar con `min`. Composición e identidad se refieren exclusivamente a
  `P_T`; la suite verifica además monotonía en `lambda`, `phi` y `sigma`, aunque
  esos nombres no estén en la línea fija.
- **declarado-no-mecanizado**: `naturalidad-xi`, `cierre-safety` y
  `composicion-kleisli` son nombres históricos de deuda. Hoy no constituyen
  proposiciones bien tipadas: faltan categorías, morfismos, un modelo
  coalgebraico/lifting y una categoría de Kleisli concreta.

Reglas:

1. Hoy **NO existe check** que verifique esas tres deudas. Se verifica solo que
   la línea fija esté presente y bien formada, no que exista o conmute un
   diagrama en el runtime.
2. Formalizar una de las tres exige primero tiparla y declarar sus hipótesis;
   mecanizarla exige después escribir el check, registrarlo en el
   registro cerrado (constitución §11, cambio de ley) y solo entonces moverla
   de lista.

Rationale: un nombre de ley no es una ley. La frontera queda explícita entre
el núcleo demostrado, la evidencia operacional y los puentes por formalizar.

## 7. Emisión por target

Firma del gesto: `transmutar --urn U [--target T] [--aplicar] [--stdout] [--proyecto PATH]`,
o en modo verificación `transmutar --paridad [--urn U] [--target T] [--proyecto PATH]`
(§9.1).
Default de emisión: `T=codex`. Escribe bajo `_emision/{target}/...` (derivado,
gitignored) y reporta. `--stdout` imprime; `--aplicar` instala en el runtime
real. En paridad, omitir `--target` conserva el barrido global (§9.1).

| Target | Forma | Emisión |
|---|---|---|
| `claude-code` | skill | `_emision/claude-code/skills/{nombre}/SKILL.md`; frontmatter `name`, `description` (+ `allowed-tools` como lista separada por comas si `herramientas` no es vacía); copia `referencias/` conservando su nombre si existe |
| `claude-code` | agente | `_emision/claude-code/agents/{nombre}.md`; frontmatter `name`, `description`, `tools` (lista separada por comas); body = body fuente; si `arnes` = `persona`, sección final `## Modos de invocacion` con la doctrina dual-mode (modo subagente batch vs modo persona por encarnación) |
| `codex` | skill | `_emision/codex/skills/{nombre}/SKILL.md`; frontmatter `name`, `description`; copia `referencias/` conservando su nombre y, si la fuente lo declara, transporta byte-idéntico `agents/openai.yaml` como metadata e invocation policy del mismo producto cerrado |
| `codex` | agente | `_emision/codex/agents/{nombre}.toml`, custom agent nativo con `name`, `description` y `developer_instructions`; el cuerpo y el sello viajan dentro de `developer_instructions`. Si `forma: agente` (persona dual-mode), emite además `_emision/codex/skills/{nombre}/SKILL.md` y el sidecar `agents/openai.yaml` con `allow_implicit_invocation: false`: el TOML preserva delegación y el skill preserva encarnación explícita en el hilo principal. Si `forma: subagente`, solo emite TOML. No fija `model`: hereda la selección del runtime. Codex permite estrechar configuración del custom agent, pero no una allowlist exacta de built-ins; el sello declara la pérdida de campo sin fingir enforcement |
| `opencode` | skill | `_emision/opencode/skills/{nombre}/SKILL.md` (mismo formato codex) |
| `opencode` | agente | `_emision/opencode/agents/{nombre}.md`; frontmatter `description`, `mode: subagent` (forma `subagente`) o `mode: all` (forma `agente`: persona dual-mode, usable como primario y delegable como subagente; `all` es el default de opencode y preserva ambos modos del sello), y `permission:` con `<tool>: deny` para cada tool de **efecto externo** (`bash`, `webfetch`, `websearch`, `task`) que `herramientas` NO concede — frontera de capacidad en el idiom canónico de opencode (el objeto `tools` está deprecado desde v1.1.1; las read-ish e internas quedan en default). Paridad con el allowlist `tools` de claude-code |
| `openclaw` | skill | `_emision/openclaw/skills/{nombre}/SKILL.md`; frontmatter `name`, `description` (agentskills.io); copia `referencias/`. Las tools de openclaw son config-level (openclaw.json), no van en el frontmatter |
| `openclaw` | agente (forma `subagente`/`agente`/`plataforma`) | **workspace** `_emision/openclaw/workspaces/{nombre}/` con DOS archivos (§7.1): `AGENTS.md` = cuerpo sin el span `U_phen` + sello; `SOUL.md` = span de `U_phen` + sello (sólo si el `arnes` porta `U_phen`) |
| `hermes` | skill | `_emision/hermes/skills/{nombre}/SKILL.md`; frontmatter `name`, `description`, `version`; copia `referencias/`; contrato `T-hermes-pneuma-v1` (§7.5) |
| `hermes` | agente (sólo forma `agente`) | **profile distribution** `_emision/hermes/profiles/{nombre}/`: `SOUL.md` = cuerpo completo + sello y `distribution.yaml` = manifest nativo que declara ambos nombres y, si existen, los subárboles exactos de skills requeridas por `depende` como `distribution_owned`; contrato `T-hermes-pneuma-v2` (§7.5-§7.6). `subagente` falla cerrado |

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
   pareja `AGENTS.md`/`SOUL.md` conserva todos los bytes marcados del cuerpo
   fuente, sin que esa conservación sintáctica implique bisimulación, mientras los targets monolíticos
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

   El emisor **realiza** el workspace conforme al techo always-on
   (`mu:3→3 full` es enunciado de **TIPO**: el techo lo admite sin recorte); la
   **conducta** always-on —el daemon vivo recordando entre sesiones (**TOKEN**)—
   es deploy del fleet, no función del emisor. La calificación vive en el
   **portador del sello** (no sólo en esta ley): reconcilia el «openclaw no realizado»
   inmutable de `GENESIS §4` con el realizado registrado aquí, sin tercerizar la
   honestidad a una ley que no viaja con el artefacto. `mu<3` no porta la
   calificación (no hay always-on que diferir).

**Frontera declarada — lo que el emisor NO produce.** `IDENTITY.md`, `USER.md`,
`TOOLS.md`, `HEARTBEAT.md`, `BOOT.md`, `MEMORY.md`, `memory/`, y la config de
deploy (`openclaw.json`: model, tools, auth, telegram, systemd). No son doctrina
KORA: son scaffolding de workspace (bootstrap ritual / `openclaw setup`, que
siembra los faltantes sin sobrescribir) y deploy (operador). La **frontera de
capacidad** (`herramientas`) NO se materializa en el workspace —`TOOLS.md` es
guía, no controla disponibilidad—: se realiza en `openclaw.json` a nivel deploy.
El sello la declara en cada archivo OpenClaw con:

```text
frontera-herramientas-declarada: [<allowlist KORA>]
frontera-herramientas-realizacion: openclaw.json/deploy (fuera del emisor; no verificada por este sello)
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
`~/.openclaw/skills/{nombre}/` (managed skills) para la skill; hermes →
`$HERMES_HOME/skills/{nombre}/` para la skill del perfil efectivo y
`<raíz-hermes>/profiles/{nombre}/` para el agente completo. En toda emisión y
aplicación el contenido auxiliar `referencias/` conserva su nombre: el cuerpo emitido cita
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
factor raíz portador del sello debe atribuir la instalación al mismo `(URN,target)`.
`--aplicar` PUEDE crear una ruta ausente y PUEDE reemplazar o retirar una ruta
ya atribuida a ese par. Si el destino existe pero carece de ese sello —o porta
otro par— es un homónimo no atribuible: conflicto bloqueante, preservado sin
mutación. La regla cubre el `SKILL.md` raíz, los agentes de archivo único, el
TOML Codex, cada `AGENTS.md`/`SOUL.md` emitido para OpenClaw y el `SOUL.md`
portador de un perfil Hermes. Todos los
factores se validan antes de mutar uno; un directorio incompatible, symlink o
nodo especial tampoco transfiere propiedad y NUNCA se sigue, aunque aparezca
en un ancestro de la ruta final. La skill complementaria Codex obedece la misma
regla. Esta adquisición rige destinos instalados; `_emision/` ya es una zona
derivada y cerrada propiedad de KORA (constitución §6).
Esa propiedad autoriza reemplazar con `lstat` un leaf incompatible dentro de
`_emision/`, pero no atravesar un ancestro enlazado: todos los destinos de
emisión y toda limpieza de derivados se preflightan antes de mutar uno.

Toda unidad bajo `_emision/` es un derivado cerrado. El **blueprint OpenClaw
aplicado** y el **perfil Hermes aplicado**, en cambio, son superficies abiertas.
En OpenClaw, KORA gobierna únicamente `AGENTS.md` y el `SOUL.md` efectivamente
emitido. Si el producto vigente deja de emitir `SOUL.md`, sólo retira el
residual cuando su sello lo atribuye al mismo `(URN,target)`; preserva
scaffolding y material ajeno. El workspace runtime privado queda fuera. En
Hermes, KORA gobierna exactamente `SOUL.md`, `distribution.yaml` y los
subárboles `skills/{nombre}/` declarados por dependencias agénticas realizadas
(§7.6); preserva `config.yaml`, `.env`, memoria, sesiones, las demás skills,
cron y cualquier otro estado del perfil. Un perfil preexistente sólo se
reconcilia cuando su `SOUL.md` atribuye el mismo `(URN,hermes)`. Los agentes de
archivo único administran su archivo exacto y no tocan hermanos del directorio.

`--aplicar --proyecto PATH` redirige la instalación al nivel
**proyecto** — el `.opencode/`/`.claude/` del proyecto, no el home del operador.
claude-code → `PATH/.claude/skills/{nombre}/` y `PATH/.claude/agents/{nombre}.md`;
codex → `PATH/.agents/skills/{nombre}/` y `PATH/.codex/agents/{nombre}.toml`;
opencode → `PATH/.opencode/skills/{nombre}/` y `PATH/.opencode/agents/{nombre}.md`
(subdirectorios en **plural**, convención canónica de opencode: el `.opencode/` y
`~/.config/opencode/` usan nombres plurales; singular solo por retrocompat).
hermes → `PATH/.hermes/skills/{nombre}/`; los perfiles Hermes y `openclaw` NO
soportan nivel proyecto porque son unidades user/gateway o user/fleet. La
emisión canónica en `_emision/` no cambia; `--proyecto`
solo redirige el destino de `--aplicar`.

Codex y OpenClaw comparten la raíz personal Agent Skills
`~/.agents/skills`. OpenClaw le da mayor precedencia que a su raíz managed
`~/.openclaw/skills`. Por eso `--aplicar` rechaza una skill OpenClaw cuando ya
existe el homónimo en el layout directo que KORA usa para Codex
(`~/.agents/skills/{nombre}/SKILL.md`): instalar debajo no cambiaría la skill
efectiva en ningún agente. Este guard NO pretende resolver layouts personales
agrupados ni precedencias por workspace; el gate de deploy DEBE inspeccionar el
discovery efectivo por agente.

Hermes descubre recursivamente skills y resuelve por nombre de directorio o
por `name` del frontmatter. Por eso aplicar o declarar `fiel` una skill Hermes
exige que no exista otro candidato activo con el mismo nombre dentro de la
raíz local efectiva; a nivel proyecto se inspeccionan conjuntamente
`.hermes/skills/` y `.agents/skills/`. Los directorios que el runtime excluye y
las fibras de soporte de una skill no cuentan. KORA no sigue enlaces durante
el preflight: un enlace activo no evaluable bloquea en vez de ampliar la
lectura. `skills.external_dirs`, plugins y el trust efectivo del proyecto
permanecen como gate de deploy del runtime; este guard no los presenta como
verificados.

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

### 7.5 Las emisiones nativas de `hermes`

Hermes Agent (Nous Research) es target realizado para dos formas distintas,
sin convertir sus primitivos en ontología KORA:

- **habilidad** desde v3.0.0: skill agentskills.io, contrato
  `T-hermes-pneuma-v1`;
- **agente completo** desde v4.0.0: profile distribution nativa, contrato
  `T-hermes-pneuma-v2`.

El canon oficial consultado el 2026-08-23 establece que una distribución de
perfil empaqueta un agente completo y puede portar `SOUL.md`, configuración,
skills, cron y MCP; también distingue los factores propiedad de la distribución
de los factores propiedad del usuario. KORA usa ese primitivo con una frontera
mínima: sólo transporta doctrina agéntica y su manifest, no absorbe estado ni
configuración del operador.

| Forma KORA | Emisión Hermes |
|---|---|
| `habilidad` | `_emision/hermes/skills/{nombre}/SKILL.md`; frontmatter oficial `name`, `description`, `version`; copia `referencias/`. El frontmatter no expresa la allowlist KORA: `herramientas` se registra como pérdida de campo y permanece disciplina del cuerpo |
| `agente` | `_emision/hermes/profiles/{nombre}/SOUL.md` con cuerpo completo y sello, más `distribution.yaml` determinista con `name`, `version`, `description` y propiedad exacta de `SOUL.md`, `distribution.yaml` y, si existen, `skills/{nombre-dependencia}/` realizadas conforme a §7.6 |
| `subagente` | fuera del dominio: falla cerrado porque un perfil es el agente completo, no una unidad delegable dentro de otro perfil |

Reglas:

1. **Transporte del agente**: `SOUL.md` recibe el cuerpo fuente completo. En
   Hermes es el primer slot de identidad/instrucciones del agente; el archivo
   conserva los bytes transportados, pero su inyección efectiva puede truncarse
   dinámicamente por presupuesto de contexto. No existe un archivo global
   paralelo que permita separar operativa y `U_phen` sin inventar semántica.
   `distribution.yaml` es sidecar derivado, no segundo portador doctrinal.
2. **Frontera del perfil**: la emisión NO incluye `config.yaml`, `.env`, MCP,
   cron, memoria, sesiones ni credenciales. Sólo empaqueta las skills activas
   exigidas mediante `depende`, cada una bajo `skills/{nombre}/` y con su propio
   sello (§7.6). `componible` declara candidatos y no autoriza
   autoempaquetarlos. El perfil instalado es superficie abierta: KORA reconcilia
   `SOUL.md`, `distribution.yaml` y sólo esos subárboles de dependencia cuando
   cada destino es ausente o atribuible al mismo `(URN-dependencia,hermes)`;
   todo lo demás se preserva. Al reaplicar, el manifest instalado anterior
   identifica los subárboles que la distribución gestionaba: si uno deja de
   estar declarado, KORA lo retira sólo cuando su sello todavía lo atribuye a
   Hermes; una edición o pérdida de sello bloquea toda la mutación.
3. **Nombre nativo**: la forma `agente` rechaza los nombres reservados por
   Hermes (`hermes`, `default`, `test`, `tmp`, `root`, `sudo`) y nombres de más
   de 64 caracteres. Nunca se deriva una ruta nativa inválida desde un slug KORA
   más permisivo.
4. **Materia always-on**: `mu:3 full` es capacidad del gateway. Para una skill
   sigue inalcanzable por `dominio-forma`; para un agente v2 el sello declara
   `profile-mu3-conforme` y difiere la conducta del gateway/systemd/config al
   deploy. La emisión ni la paridad prueban que el perfil esté servido.
5. **Herramientas**: ni `SKILL.md` ni `SOUL.md` implementan una allowlist exacta
   por artefacto. Si `herramientas` no es vacía, el sello declara
   `herramientas -> sin-allowlist-runtime`; la configuración efectiva de
   toolsets permanece fuera del emisor.
6. **Aplicación de skills**: sin override usa
   `~/.hermes/skills/{nombre}`; con `HERMES_HOME`,
   `$HERMES_HOME/skills/{nombre}`. `--proyecto PATH` usa
   `PATH/.hermes/skills/{nombre}` sin fingir que concede confianza. Aplicación y
   paridad inspeccionan las colisiones nominales dentro de las raíces explícitas
   descritas en §7.
7. **Aplicación de agentes**: usa
   `<raíz-hermes>/profiles/{nombre}`. Si `HERMES_HOME` ya apunta a
   `<raíz>/profiles/<perfil-activo>`, la raíz se resuelve como `<raíz>`; un
   perfil no se anida dentro de otro. No hay instalación project-level de un
   agente completo.
8. **Paridad y límite runtime**: una skill se compara como producto cerrado. Un
   perfil compara sus dos factores raíz y los subárboles exactos de dependencia
   declarados, y tolera configuración/estado adicional fuera de esa propiedad.
   La igualdad de bytes no prueba que Hermes haya cargado el SOUL: el runtime
   aplica un límite dinámico según la ventana de contexto y puede truncarlo;
   esa observación pertenece al canario runtime, no al sello.

### 7.6 Dependencias agénticas

`depende` conserva su semántica genérica de arista DAG. Cuando el origen es un
artefacto agéntico y el destino también lo es, el adaptador realiza además una
obligación mínima: la unidad requerida debe quedar disponible en el mismo
target. Esta disponibilidad no demuestra invocación, orden de ejecución,
wiring ni composición.

Reglas:

1. Una dependencia hacia conocimiento permanece relación semántica y no copia
   corpus al runtime. `componible` permanece un grafo de candidatos y nunca
   produce emisión o instalación implícita.
2. El primer dominio realizado acepta sólo destinos de forma `habilidad`, en
   estado `activo` y compatibles con el target solicitado. Una dependencia
   hacia `agente` o `subagente` falla cerrado: la arista no porta contrato de
   invocación ni composición.
3. El cierre es transitivo, acíclico y se ordena desde las hojas. Cada skill se
   emite como unidad propia, conserva su URN, hash, sello y pérdidas y pasa las
   mismas validaciones que una transmutación focal. Una incompatibilidad aborta
   antes de escribir o aplicar el producto padre.
4. En Codex y en los targets de archivo independientes, cada requisito se
   instala en la raíz canónica de skills del target como producto separado. El
   agente no incorpora paths absolutos ni duplica el cuerpo requerido.
5. En Hermes, la distribución del agente empaqueta cada requisito bajo
   `skills/{nombre}/` y declara exactamente ese subárbol en
   `distribution_owned`. La aplicación adquiere propiedad por el sello propio
   de la skill, retira requisitos anteriormente gestionados que dejaron de
   pertenecer al cierre y preserva todas las demás skills y el estado del
   perfil. El retiro exige a la vez propiedad previa en el manifest instalado y
   sello KORA Hermes vigente en el subárbol.
6. Antes de cualquier mutación runtime, `--aplicar` preflighta la propiedad y
   compatibilidad de todas las unidades del cierre y del padre. Un conflicto
   bloquea el conjunto; no se entrega una dependencia parcial.

La materialización expresa disponibilidad requerida. La conducta emergente
sólo puede afirmarse con evidencia runtime de discovery e invocación; la
paridad de bytes no la sustituye.

## 8. El gesto inverso (Lift)

La inclusión reticular `J_T: I_T ↪ D_T` ya es adjunta izquierda de `P_T`
(§1); no debe confundirse con ingerir archivos de runtime.

`Lift_target` nombra una **candidata** de ingesta que reconstruiría una fuente
desde un artefacto foráneo. Esta encarnación no la implementa y no afirma una
adjunción para ella. Demostrar `Lift_target ⊣ E_target` exigiría definir las
categorías de runtime e IR, ambos funtores, una biyección natural de hom-sets
o unidad/counit y sus identidades triangulares. Las ecuaciones históricas
«módulo pérdida» no satisfacían por sí solas esa obligación.

## 9. Frescura

Si existe `_emision/`, cada unidad descubierta DEBE ser congruente con tres
fuentes de identidad: archivo fuente actual, target de su ruta y generador
vigente. Check diagnóstico: `sello-fresco`, ejecutado por
`velar --estricto`; no pertenece a la validación cotidiana de fuentes.

Antes de leer contenido, el check enumera `_emision/` sin seguir enlaces:
la raíz y todos sus descendientes DEBEN ser directorios o archivos regulares
reales. Un symlink, nodo especial o nodo ilegible invalida la frescura.

Cada archivo regular DEBE poder atribuirse a una raíz de producto reconocible:
un agente, una skill o un workspace emitido. Un archivo suelto o un factor sin
esa raíz invalida la frescura; estar bajo `_emision/` no le confiere autoridad
KORA por ubicación.

El check lee el **último** bloque `kora:sello` de cada factor doctrinal —el
cuerpo puede citar sellos de ejemplo— y verifica:

1. el sello existe, su `target` coincide con la ruta, está permitido por la
   allowlist `targets` cuando esta existe y realizado por esta encarnación, y
   `hash-fuente` coincide con el sha256 actual del archivo fuente principal;
2. al regenerar en memoria el par `(URN,target)`, el conjunto y los bytes de
   todos los factores coinciden, incluidos sidecars sin sello; para una skill
   Codex, `agents/openai.yaml` se lee desde la fuente y se transporta sin
   reinterpretarlo;
3. para skills, los paths y bytes de `referencias/` coinciden con el contenido
   fuente, aunque esos archivos no participen en `hash-fuente`.

Una diferencia implica re-transmutar. Alcance honesto: si una unidad completa
no existe, este check no tiene un sello desde el cual descubrirla; la
completitud `activo→emisión` sigue perteneciendo a paridad (§9.1). La
congruencia byte a byte prueba forma producida, no verdad semántica ni las leyes
declaradas de §6.

### 9.1 Paridad de despliegue

La frescura tiene dos aguas. `sello-fresco` (§9) vigila **emisión↔fuente**;
la **paridad** vigila **emisión↔instalación**: que la frontera KORA gestionada
en el runtime elegido sea byte-idéntica a lo emitido. Gesto:
`transmutar --paridad [--urn U] [--target T] [--proyecto PATH]` — solo lectura;
sin `--proyecto` audita nivel usuario/flota y con él usa exactamente el layout
project-level de `--aplicar --proyecto` sin mutar el proyecto ni `_emision/`.

Reglas:

1. Veredictos por unidad: `fiel` (frontera KORA gestionada byte-idéntica),
   `desviada` (drift bloqueante), `no-instalada` (la unidad KORA no está
   materializada; informativo, porque el gesto no decide dónde desplegar) y
   `sin-emision` (un artefacto `activo` promete el target pero no tiene la
   unidad derivada correspondiente). Son `desviada`, entre otros: bytes distintos, factor
   gestionado sobrante, nodo de tipo incompatible, symlink o nodo especial,
   homónimo no atribuible en una ruta que KORA necesitaría adquirir y residuo
   atribuible de una fuente que ya no está activa o cuyo producto vigente ya no
   contiene esa unidad, y colisión nominal activa en el discovery Hermes que
   vuelve ambigua la skill efectiva.
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
   aplicado sólo se comparan los nombres emitidos y un `SOUL.md` residual cuyo
   sello lo atribuya al mismo `(URN,target)`; los demás nombres y el workspace
   runtime privado quedan fuera (§7.1). En un perfil Hermes se comparan
   `SOUL.md`, `distribution.yaml` y cada subárbol de skill que el manifest
   emitido declara en `distribution_owned`; configuración, memoria, skills no
   declaradas y demás estado quedan fuera (§7.5). Una skill complementaria Codex
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
4. Alcance honesto: el barrido user-level espera unidades activas con
   `alcance: usuario|ambos`; el barrido `--proyecto` espera
   `alcance: proyecto|ambos` (ausente = `ambos`). Un `--urn` focal incompatible
   con el nivel falla como `--aplicar`. `PATH` DEBE ser un directorio existente
   y un target explícito DEBE tener layout project-level; OpenClaw no lo tiene.
5. La paridad NO es check de `velar` (registro cerrado, constitución §11):
   `velar` vela el corpus; la paridad mira el mundo. Por eso vive como modo
   del gesto `transmutar`, que ya gobierna la relación IR↔runtime.
6. La completitud se deriva de los artefactos agénticos `activos`. Una lista
   `targets` presente promete sus destinos realizados. Si falta, el barrido
   ordinario promete Codex y un `--target T` focal promete ese target realizado
   durante la auditoría explícita. Un target explícito no realizado falla; con
   `--urn U`, un target fuera de la allowlist presente en `U` también falla.
   Ninguna selección inválida se degrada a un barrido vacío exitoso. Una persona
   Codex promete dos unidades —custom agent y skill explícita—; un subagente
   Codex promete una. Un directorio sin su archivo raíz (`SKILL.md` o
   `AGENTS.md` o `SOUL.md` de perfil) no constituye una unidad emitida. Esta promesa exige **emisión**,
   no instalación: cada runtime se despliega de forma independiente y una
   unidad ausente puede seguir siendo `no-instalada` sin conflicto.
7. Si una skill managed OpenClaw existe pero el homónimo del layout personal
   Codex/KORA también existe, la unidad es `desviada`, no `fiel`. Otras fuentes
   de precedencia permanecen fuera de este barrido y pertenecen al deploy.
   Para Hermes, un homónimo activo en la raíz local efectiva o dentro de las
   dos raíces project-level explícitas también es `desviada`; external dirs,
   plugins y confianza efectiva siguen siendo evidencia separada de deploy.
Rationale (2026-07-06): cinco agentes corrieron días desactualizados en los
runtimes de escritorio sin que ningún gesto lo viera — la fuente avanzó, la
emisión se regeneró, la instalación quedó atrás. `velar` verde no lo detecta
por diseño (vela la forma del corpus, no el mundo); este modo cierra esa
clase de fallos sin fingir que la instalación es corpus.

## 10. Validación

| Regla | Detalle | Enforcement |
|---|---|---|
| Eje a ∅ aborta | §3 r3: exit 1 nombrando eje, valor y runtime alternativo | mecanizado (`transmutar`) |
| Target no realizado falla honesto | §2 r2, §9.1 r6 | mecanizado (`transmutar`, incluida paridad) |
| Monotonía de los cinco ejes y cinco componentes de Σ | proyección `min` sobre matriz | mecanizado (por construcción y tests exhaustivos por ley) |
| Descenso e idempotencia | §3 | mecanizado (por construcción y tests) |
| Composición e identidad de `P_T` | §3, categorías delgadas | mecanizado (por monotonía y tests) |
| Coreflexión `J_T ⊣ P_T` | §1 y núcleo categorial | demostrada; igualdad de orden cubierta por tests |
| Pérdidas declaradas si `partial` | §5 r2 | mecanizado (`transmutar`) |
| Fuente coherente antes de proyectar | checks ontológicos de `velar` sobre la fuente | mecanizado (`transmutar`) |
| Colisión de `nombre` en el espacio plano de emisión | §7 | mecanizado (`transmutar`) |
| `nombre` seguro como componente de ruta antes de reconciliar | ley/2 §2.1, §7 | mecanizado (`forma-valida`, `transmutar`) |
| Propiedad de toda ruta instalada antes de reemplazar o retirar | §7: sello `(URN,target)`; homónimo preservado; preflight de factores y ancestros | mecanizado (`transmutar --aplicar`) |
| Frontera `herramientas` de Codex declarada como pérdida no reticular tipada | §5 r3/r7, §7 | mecanizado (`transmutar`) |
| Frontera `herramientas` de OpenClaw declarada; realización config diferenciada | §7.1 | declaración mecanizada (`transmutar`); realización verificada en deploy |
| Emisión de workspace `openclaw` (AGENTS.md + SOUL.md) | §7.1 | mecanizado (`transmutar`) |
| Centinela `kora:soul` requerido para `SOUL.md` de `arnes` con `U_phen` | §7.1, ley/2 §10 r6 | mecanizado (`transmutar`) |
| Emisión Hermes por forma: skill v1, profile distribution v2, subagente fuera de dominio | §7.5 | mecanizado (`transmutar`) |
| Nombre nativo y propiedad abierta del perfil Hermes | §7.5 r2-r3 | mecanizado (`transmutar --aplicar`, paridad) |
| Colisión nominal en discovery local/project-level de skills Hermes | §7, §7.5 r6 | mecanizado (`transmutar --aplicar`, paridad); external dirs/plugins/trust quedan en deploy |
| Calificación `mu=3` de perfil separada de gateway vivo | §4.5, §7.5 r4 | declaración mecanizada en sello; conducta verificada en deploy |
| Cierre transitivo de dependencias agénticas realizables | §7.6: skill activa, target compatible, unidad propia; agentes requeridos fallan cerrado | mecanizado (`transmutar`, `transmutar --aplicar`) |
| Reconciliación de dependencias retiradas del perfil Hermes | §7.5 r2, §7.6 r5-r6: manifest previo + sello de skill; preflight antes de retirar | mecanizado (`transmutar --aplicar`) |
| `componible` sin efecto de despliegue implícito | §7.6 r1 | mecanizado por construcción y tests |
| Sello con formato exacto al emitir | §5 | mecanizado (`transmutar`) |
| Congruencia fuente↔generador↔producto (sidecars y `referencias/` incluidos) | §9 | mecanizado (`sello-fresco`) |
| Sidecar fuente `agents/openai.yaml` de skill Codex conservado en emisión, aplicación y paridad | §7, §9, ley/2 §6 | mecanizado (`transmutar`, `sello-fresco`, `transmutar --paridad`) |
| Paridad exacta y tipada de la superficie KORA (emisión↔instalación user-level o project-level) | §9.1: incluye residuos atribuibles, conflictos de propiedad y nodos no regulares | mecanizado (`transmutar --paridad [--proyecto PATH]`) |
| Completitud artefacto activo→emisión por target | §9.1 | mecanizado (`sin-emision`) |
| Target permitido por allowlist opcional; Codex por defecto si falta | §2 r4-r5, §9.1 r6 | mecanizado (`transmutar`, incluida paridad focal) |
| Aplicación solo de artefactos activos | §2 r6 | mecanizado (`transmutar --aplicar`) |
| Determinismo byte-idéntico | §5 r5 | mecanizado (sin timestamps; cubierto por tests) |
| `naturalidad-xi` | §6 | deuda por tipar |
| `cierre-safety` | §6 | deuda por tipar |
| `composicion-kleisli` | §6 | deuda por tipar |
| Bisimulación módulo proyección | §3 | hipótesis de investigación, no garantía |

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

v2.6.1 (2026-07-18): corrige `sello-fresco` para preflightar `_emision/` con
`lstat` antes de leerla. Enlaces simbólicos, nodos especiales o ilegibles ya no
pueden producir frescura aparente ni provocar lectura fuera de la emisión.

v2.7.0 (2026-07-18): corrección de rigor categorial sin cambiar el formato ni
los bytes del sello. Se demuestra y delimita `P_T` como coreflector entre
categorías delgadas; la emisión completa pasa a llamarse serialización
determinista. Se retiran las atribuciones no demostradas de lift cartesiano,
bisimulación y adjunción de ingesta. Los nombres fijos del sello se conservan
como identificadores históricos de contrato y se acota expresamente su alcance.

v2.8.0 (2026-07-18): formaliza la fidelidad como funtor contravariante desde
las cadenas de demanda hacia `none ≤ partial ≤ full`. La suite verifica que
mayor demanda nunca mejora fidelidad y que `full`, `none` y las razones de
pérdida son coherentes. No cambia matrices, sello ni bytes emitidos.

v2.9.0 (2026-08-09): mueve `sello-fresco` desde el registro cotidiano de
fuentes al diagnóstico optativo `velar --estricto`. La comparación exacta de
fuente, generador, sidecars y `referencias/` no cambia; solo deja de bloquear
validaciones y promociones no relacionadas con un derivado rancio. No cambia
matrices, formato de sello ni bytes emitidos.

v2.10.0 (2026-08-10): mecaniza la paridad project-level con
`transmutar --paridad --proyecto PATH`, usando el mismo layout que
`--aplicar --proyecto` y conservando la inspección de solo lectura, atribución,
tipos e igualdad byte a byte. Cada nivel deriva sus unidades esperadas desde
`alcance` (`usuario|ambos` o `proyecto|ambos`; ausente = `ambos`) y los focales
incompatibles fallan cerrados. Extensión aditiva del modo de verificación.

v2.11.0 (2026-08-11): transporta el sidecar fuente opcional
`agents/openai.yaml` de una skill Codex como factor byte-idéntico del producto
cerrado. Emisión, aplicación, frescura y paridad conservan su ruta anidada;
otros targets y skills sin sidecar mantienen sus bytes previos.

v2.12.0 (2026-08-13): separa especificación agnóstica de selección
operacional. `targets` pasa a ser una allowlist opcional: si falta, Codex es el
target principal por defecto y cualquier otro realizado exige selección
explícita; si existe, conserva la restricción vigente. Paridad global promete
Codex para fuentes agnósticas y una auditoría focal promete el target solicitado.
Una selección focal inválida falla en vez de convertirse en éxito vacío. No
cambia matrices, adaptadores, formato de sello ni bytes de fuentes existentes.

v2.12.1 (2026-08-14): corrige el cierre de `_emision/`: `sello-fresco` rechaza
todo archivo regular que no pueda atribuirse a una raíz de producto KORA
reconocible. Precisa y mecaniza el carácter derivado cerrado ya vigente; no
cambia matrices, adaptadores, formato de sello ni bytes emitidos.

v3.0.0 (HITL 2026-08-23): **realiza `hermes` para la forma habilidad** —
contrato `T-hermes-pneuma-v1`, matriz §4.5 y emisión §7.5. Cierra el tramo
habilidad de la deuda declarada en `GENESIS §4` sin editar GENESIS (misma regla que openclaw
v1.3.0). La forma agéntica NO se mecaniza: Hermes no tiene primitivo nativo
de archivo-agente (los agentes-persona son perfiles gateway con SOUL.md), así
que `transmutar --target hermes` sobre un agente falla cerrado y el puente
manual queda como camino gobernado — lección aplicada de `T-openclaw`
(revert `8ef7c6e`). Verificación viva contra el canon oficial
(hermes-agent.nousresearch.com/docs: SKILL.md frontmatter `name`,
`description`, `version` opcional; skills por perfil; gateway siempre-activo).
Extensión aditiva
(constitución §12.1): nueva matriz, nuevo adaptador, nuevas rutas de
instalación; no cambia bytes ni contratos de targets previos.

v3.1.0 (2026-08-23): corrige la frontera Spec/Runtime de la realización Hermes.
`--aplicar` y paridad honran `HERMES_HOME`, por lo que perfiles y bots ya no se
desvían silenciosamente al perfil default; `--proyecto` materializa en
`.hermes/skills/` sin fingir que concede el trust gate del runtime. Aclara que
`mu:3 full` es capacidad del gateway, no fidelidad alcanzable por el transporte
v1 de habilidades, y deja de recomendar Hermes para fuentes `mu=3`. Retira del
texto normativo el recuento de canales y la versión instalada, ambos volátiles.
No cambia el formato ni los bytes emitidos por `T-hermes-pneuma-v1`.

v4.0.0 (2026-08-23): realiza la forma `agente` de Hermes mediante el primitivo
nativo **profile distribution** y el contrato `T-hermes-pneuma-v2`:
`SOUL.md` transporta el cuerpo completo y `distribution.yaml` declara sólo esos
dos factores como propiedad de la distribución. La forma `subagente` sigue
fuera del dominio. Aplicación y paridad preservan configuración, memoria,
skills, cron, secretos y demás estado del perfil, bloquean perfiles homónimos
no atribuibles y detectan colisiones nominales activas de skills en las raíces
locales/project-level explícitas. El sello de un agente `mu=3` separa perfil
conforme de gateway vivo. Es major porque sustituye el fallo cerrado de toda
forma agéntica por un producto, ruta, propiedad y contrato de paridad nuevos;
no altera los bytes de skills Hermes v1 ni la identidad agnóstica de KORA.

v5.0.0 (HITL 2026-08-23): realiza el efecto operacional de `depende` entre
artefactos agénticos como disponibilidad runtime de skills activas y
compatibles, sin confundirlo con invocación ni composición. El cierre es
transitivo y cada requisito conserva unidad, URN y sello. Codex y los targets
de archivo instalan la skill por separado; Hermes la empaqueta bajo el subárbol
exacto `skills/{nombre}/` de la distribución y preserva todo estado ajeno. Un
destino de forma agente, una incompatibilidad o un conflicto de propiedad
fallan cerrado antes de mutar el runtime. Es major porque amplía la propiedad,
emisión y aplicación observables de una fuente agéntica que declara `depende`;
`componible` permanece sin efecto automático.

v5.1.0 (2026-08-24): completa la reconciliación de `depende` en perfiles
Hermes. Al reaplicar, `distribution_owned` del manifest instalado aporta la
frontera previa y KORA retira sólo las skills que dejaron de ser requisito y
que conservan sello Hermes atribuible. Una ruta editada o no atribuible bloquea
antes de mutar; las skills ajenas permanecen fuera de la frontera. Precisa
además que la paridad del perfil incluye los subárboles de dependencia
declarados, sin convertir el resto del estado del perfil en propiedad KORA.
