---
urn: urn:dev:artefacto:hermes-agent-specialist
nombre: hermes-agent-specialist
version: 2.2.0
estado: activo
descripcion: "Especialista en agentes Hermes (Nous Research) para crear, configurar, desplegar, operar y auditar agentes contra la documentacion oficial viva en hermes-agent.nousresearch.com/docs/. Usar cuando el operador mencione Hermes Agent, SOUL.md, hermes CLI, agentskills, terminal.backend (local/docker/ssh/modal/daytona/vercel_sandbox/singularity), mensajeria sobre Hermes, MCP en Hermes, migracion desde OpenClaw, o cualquier tarea del ciclo de vida de un agente Hermes — aunque no nombre la skill."
fuente: "Rehecha a fidelidad el 2026-06-22 contra la doc oficial viva (hermes-agent.nousresearch.com/docs/, sondeo de estado 2026-06-22). Deriva de la bestia artifacts/skills/dev/hermes-agent-specialist/SKILL.md v0.1.1 (sha256:656d2b29d2c56ce4b50051625ae475b3051ee2b178b5012d1681798198666991): se conservan proposito, doctrina canon-vivo/no-snapshot, regla >=64k tokens y secretos-en-.env (todas vigentes y confirmadas en el canon). Normalizacion pneuma: frontmatter _manifest/extensions.kora anidado -> shape plano ley/2; vector [2,0,2,0,1] preservado (legal para habilidad); conocimiento (urn:kora:kb:hermes-runtime-extension etc.) OMITIDO por migrar-o-omitir (no encarna en pneuma; ademas esta skill ancla su SSOT al canon web vivo, no a kb congelado). Correcciones de fidelidad: SOUL.md SOLO en HERMES_HOME (nunca cwd); paths/limites de memoria (~/.hermes/memories/, MEMORY.md ~2200c, USER.md ~1375c, snapshot congelado); inventario CLI remitido al canon vivo; deploy = valores de terminal.backend (no subpaginas); proveedores con IDs y catch self-hosted; skills progressive-disclosure 3 niveles + skill_manage; MCP stdio/HTTP detallado; mensajeria con allowlists/pairing; seguridad 7 capas; migracion nativa OpenClaw (hermes claw). bump major: reescritura sustantiva. v1.0.1 (2026-06-23): correccion de fidelidad contra la doc viva (verificacion web adversarial, sondeo 2026-06-23) — `OLLAMA_CONTEXT_LENGTH=64000` se reformula de requisito duro a ajuste necesario para alcanzar el piso de 64k que el canon lista como *recomendado* (default Ollama 4096); el anti-patron auditable deja de marcar falso-incumplimiento. Resto de claims (SOUL.md/HERMES_HOME, limites de memoria, terminal.backend, precedencia config, skills 3-niveles, mensajeria deny-by-default, seguridad 7-capas, hermes claw migrate) confirmados sin deriva. v2.0.0 (2026-07-13): decisión HITL retira `openclaw` de targets; la migracion OpenClaw→Hermes es un puente de entrada soportado por Hermes, no equivalencia ni destino de ejecucion. Elimina cifras de catalogo persistidas: comandos, proveedores, tools, modelos y canales se consultan bajo demanda en el canon oficial. v2.1.0 (2026-08-04): sondeo de fidelidad contra el canon vivo (llms-full.txt, 2026-08-04) — correcciones: ya EXISTE ejecucion/instalacion Docker oficial (imagen nousresearch/hermes-agent, doc en /docs/user-guide/docker); terminal.backend ahora son 7 (agregado vercel_sandbox); el modelo de seguridad ahora tiene 8 capas (nueva capa 3: file write safety); claude-marketplace ya no figura en los hub sources del canon. Resto de claims (SOUL.md/HERMES_HOME, memoria 2200/1375 con snapshot congelado, precedencia config, piso 64k, Ollama/vLLM, skills 3 niveles, MCP, mensajeria deny-by-default, hermes claw migrate) confirmados sin deriva. v2.2.0 (2026-08-06): decision HITL del operador — el indice oficial llms.txt (asset llms-faaf9398aa5828403fd56f6be7989c9f.txt, sha256 f502e5ad7b0d0273631be772af4b665addadec066a8a7ff0255804e4796c2e93, sondeo 2026-08-06) se incorpora como base de conocimiento fundamental de la emision Hermes: cache navegable con clausula de staleness (cada URL se resuelve en vivo antes de afirmar; refrescar cuando el hash del asset llms-*.txt cambie). EXCEPCION explicita a la regla dura #3 (no-snapshot): unico snapshot permitido, declarado en esta version; todo otro snapshot sigue prohibido. Copia byte-identica custodiada en referencias/llms-index.txt de este canon; la emision Hermes la sincroniza en references/official-docs-index.md y declara metadata.hermes.source apuntando a este canon."
autor: FS
creado: 2026-05-12
lang: es
tags: [hermes-agent, nous-research, soul-md, agentskills, mcp, terminal-backend, mensajeria, canon-vivo, no-snapshot, agente-autonomo, openclaw-migracion]
vector: [2, 0, 2, 0, 1]
sigma: [2, 0, 2, 2, 0]
arnes: disciplina
forma: habilidad
herramientas: [Read, Write, Edit, Glob, Grep, Bash, WebFetch]
targets: [claude-code, codex, opencode, hermes]
componible: [urn:kora:artefacto:mente-omega, urn:dev:artefacto:ship-discipline]
estados: [triaje, clasificar-modo, consultar-canon-vivo, producir-artefacto, citar-y-etiquetar, cierre]
alcance: ambos
---
# hermes-agent-specialist

## Proposito

Especialista operativo en **Hermes Agent** (Nous Research): plataforma open-source
(MIT, sin telemetria) de agente autonomo persistente que "se vuelve mas capaz
cuanto mas corre" — learning loop con memoria curada, creacion autonoma de skills
y auto-mejora, vive donde lo pongas (VPS, cluster GPU, serverless).

**Contrato duro**: antes de afirmar, generar o modificar cualquier artefacto Hermes
(`SOUL.md`, `config.yaml`, memoria, context files, skills, integraciones, MCP,
backend de despliegue, comandos CLI), **consulta la doc oficial viva** en
`https://hermes-agent.nousresearch.com/docs/`. El canon evoluciona rapido:
proveedores, comandos y capacidades cambian; la memoria de entrenamiento no califica
como fuente. Esta skill no es un mirror ni un mantenedor con autoridad propia: es la
disciplina que mantiene a un agente anfitrion alineado al canon vigente, sin deriva
ni comandos inventados.

**Distincion canonica**: **Hermes Agent** (plataforma CLI) != **modelos Hermes LLM**
de Nous Research. Si el intent es ambiguo, pedir aclaracion antes de seguir.

## Cuando Usar

- crear un agente Hermes desde cero (instalacion, `hermes setup`, proveedor, primer `SOUL.md`).
- configurar despliegue via `terminal.backend` (local, docker, ssh, modal, daytona, vercel_sandbox, singularity).
- conectar canales de mensajeria sobre el gateway de Hermes.
- integrar MCP servers (stdio/HTTP) o exponer Hermes como server MCP.
- ciclo de vida de skills (agentskills.io, `skill_manage`, hub, curator, bundles).
- operar memoria/personalidad (`SOUL.md`, `MEMORY.md`, `USER.md`, context files).
- cron, webhooks, delegation, checkpoints/rollback, kanban, profiles, proxy, ACP/LSP.
- migrar desde OpenClaw (`hermes claw migrate`) o desde modelos retirados (`hermes migrate`).
- auditar un agente Hermes existente contra el canon.

## Cuando NO Usar

- agentes que **no** son Hermes (OpenClaw, kora-agents, subagentes Claude Code) salvo puente declarado.
- los **modelos Hermes LLM** como tema (otra cosa: declinar o redirigir).
- ciclo de vida meta-KORA o de skills KORA: usar el canon de KORA (`ley/`).
- diseno organizacional de celulas humano-agente: usar `urn:fxsl:artefacto:cell-design`.

## Workflow

### `triaje`

1. **Es Hermes Agent (plataforma) y no los modelos Hermes LLM?** Ambiguo -> aclarar.
2. **Agente existente o nuevo?**
3. **Backend objetivo?** (`terminal.backend`: local/docker/ssh/modal/daytona/vercel_sandbox/singularity, o por decidir).

### `clasificar-modo`

| Modo | Disparador | URL primaria de canon |
|------|------------|------------------------|
| **Crear** | "instala / arma / dame un SOUL.md" | `/docs/getting-started/quickstart`, `/docs/getting-started/installation` |
| **Configurar y desplegar** | "deploy a X / conecta canal Y" | `/docs/user-guide/configuration`, `/docs/user-guide/messaging/` |
| **Operar y mantener** | troubleshoot, upgrade, recovery | `/docs/reference/cli-commands` |
| **Gestionar skills** | crear/portar/auditar skills | `/docs/user-guide/features/skills` |
| **Auditar existente** | "revisa este Hermes" | combinacion segun inventario |

### `consultar-canon-vivo`

Hacer **fetch vivo** (WebFetch) de la URL primaria antes de producir nada; fetch en
paralelo de las subpaginas que apliquen. Atajo para LLMs: `/docs/llms.txt`
(indice) y `/docs/llms-full.txt` (completo). La emision Hermes (skill vivo
`hermes-agent`) porta el indice cacheado con manifiesto (`referencias/llms-index.txt`
de este canon, sondeo 2026-08-06); es atajo de navegacion offline, no reemplaza
el fetch vivo. Mapa de canon:

| Pagina | Cubre |
|--------|-------|
| `/docs/getting-started/quickstart` | flujo end-to-end; regla **>=64k tokens** |
| `/docs/getting-started/installation` | instaladores reales por SO |
| `/docs/getting-started/learning-path` | ruta de aprendizaje |
| `/docs/integrations/providers` | proveedores, IDs, requisitos (confirma >=64k) |
| `/docs/user-guide/configuration` | `config.yaml`, `.env`, `terminal.backend`, precedencia |
| `/docs/user-guide/security` | modelo de seguridad de 7 capas |
| `/docs/user-guide/features/overview` | catalogo de capacidades |
| `/docs/user-guide/features/tools` | catalogo vivo de tools y toolsets |
| `/docs/user-guide/features/personality` | `SOUL.md` (canonico) |
| `/docs/user-guide/features/memory` | `MEMORY.md`, `USER.md`, tool `memory` |
| `/docs/user-guide/features/context-files` | `.hermes.md`/`HERMES.md`/`AGENTS.md`/`CLAUDE.md`/`.cursorrules` |
| `/docs/user-guide/features/skills` | agentskills.io, progressive disclosure |
| `/docs/user-guide/features/mcp` | MCP servers, `hermes mcp` |
| `/docs/user-guide/features/voice-mode` | voz, TTS |
| `/docs/user-guide/messaging/` | canales, allowlists, DM pairing |
| `/docs/reference/cli-commands` | catalogo CLI completo |
| `/docs/reference/faq` | preguntas frecuentes |

### `producir-artefacto`

Generar el artefacto pedido (config, `SOUL.md`, skill, comando, diagnostico) apoyado
en lo consultado, no en memoria. Disciplina:

- archivos completos, no fragmentos.
- secretos en `.env` (chmod 600); todo lo no-secreto en `config.yaml`.
- modelo con **>=64000 tokens** de contexto (regla dura del canon).
- comandos/flags exactos verificados; nunca inventados.

### `citar-y-etiquetar`

- citar la(s) ruta(s) `/docs/...` consultada(s) en la sesion.
- etiquetar como inferencia todo lo que el canon no resuelva.
- declarar puentes con KORA u OpenClaw cuando aplique.

### `cierre`

Reportar: modo aplicado, artefacto/diagnostico, URLs citadas, inferencias y deuda
residual, siguiente paso si la tarea es multi-incremento.

## Conceptos canonicos clave

### Identidad: `SOUL.md`

- Vive **SOLO** en `HERMES_HOME` (`~/.hermes/SOUL.md` por defecto, o `$HERMES_HOME/SOUL.md`).
  Hermes **NO** lo busca en el cwd. Distinto de los context files.
- Ocupa el **slot #1** del system prompt, reemplazando la identidad por defecto.
- **Nunca se sobrescribe** si ya existe; Hermes solo genera un starter si no hay ninguno.
  Si esta vacio/ilegible/ausente, revierte a la identidad por defecto (no falla).

### Memoria: `MEMORY.md` y `USER.md`

- Ambos en `~/.hermes/memories/`. Limites duros: `MEMORY.md` ~2200 chars (~800 tokens,
  notas del agente); `USER.md` ~1375 chars (~500 tokens, perfil del usuario).
- Inyectados al system prompt como **snapshot congelado** al inicio de sesion (preserva
  el prefix cache): un cambio en sesion no aparece hasta la siguiente.
- Tool `memory`: acciones `add` / `replace` / `remove` (match por substring). **No hay
  `read`** — el contenido ya esta inyectado.

### Context files (de proyecto, distintos de `SOUL.md` y memoria)

- Precedencia **first-match-wins**, un solo tipo por sesion:
  `.hermes.md`/`HERMES.md` -> `AGENTS.md` -> `CLAUDE.md` -> `.cursorrules`
  (las reglas `.cursor/rules/*.mdc` se resuelven bajo `.cursorrules`, no como slot aparte).
- Descubrimiento: `.hermes.md`/`HERMES.md` caminan a la git-root; `AGENTS.md`/`CLAUDE.md`
  desde cwd + subdirectorios; `.cursorrules`/`.cursor/rules` solo cwd.
- `SOUL.md` se carga **independiente** de esta cadena.

### Configuracion y despliegue

- Precedencia de resolucion: **CLI > `config.yaml` > `.env` > defaults**. `HERMES_HOME`
  redefine la raiz de todo el estado.
- **Secretos en `.env`** (API keys, tokens, passwords). Todo lo demas (modelo, backend,
  compresion, limites de memoria, toolsets) en `config.yaml`. Un secreto en `config.yaml`
  es brecha que se reporta.
- **Despliegue = valor de `terminal.backend`** en `config.yaml`, no subpaginas aparte
  (son 7 backends en el canon): `local | docker | ssh | modal | daytona | vercel_sandbox | singularity`.
  Los chequeos de comando peligroso se **OMITEN** en backends containerizados (docker/singularity/modal/daytona):
  el contenedor es la frontera de seguridad.

### Proveedores

- Cualquier modelo agentico requiere **>=64000 tokens** de contexto (literal en quickstart
  y providers). IDs canonicos: `nous` (Nous Portal), `openrouter`, `anthropic`, `openai-api`,
  `gemini`, `copilot`/`copilot-acp`, `xai`/`xai-oauth`, `bedrock`, `azure-foundry`,
  `alibaba`, `qwen-oauth`, `kimi-coding`, `zai`, `deepseek`, `minimax`, `novita`, `nvidia`,
  `huggingface`, `ollama-cloud`, y self-hosted `ollama`, `vllm`, `sglang`, `llama-cpp`,
  `lmstudio`, `custom` (la lista crece; verificar viva).
- Self-hosted critico: **Ollama** debe arrancar con `OLLAMA_CONTEXT_LENGTH=64000` para alcanzar el piso de 64k (la doc lo lista como *recomendado*, no como flag obligatorio; su default es 4096 tokens, que no califica para uso agentico con tools);
  **vLLM** necesita `--enable-auto-tool-choice --tool-call-parser hermes`.
- **Nous Portal**: verificar en el canon vivo el catalogo disponible y las
  herramientas Tool Gateway antes de configurar.

### Skills (agentskills.io)

- Viven en `~/.hermes/skills/` (SSOT). **Progressive disclosure de 3 niveles**:
  `skills_list()` (~3k tokens) -> `skill_view(name)` (contenido) -> `skill_view(name, path)`.
- `SKILL.md` con frontmatter `name`/`description`/`version` + `metadata.hermes`
  (`tags`, `category`, `platforms`, `config`, y activacion condicional via
  `requires_toolsets`/`fallback_for_toolsets`).
- Tool `skill_manage`: el agente crea/parchea/edita/borra skills. Con
  `skills.write_approval: true`, los writes hacen staging en `~/.hermes/pending/skills/`.
- Hub multi-fuente (official, skills-sh, well-known, github, clawhub, lobehub, browse-sh,
  url; verificar tabla viva) + `curator` para mantenimiento en background.

### MCP

- `mcp_servers` en `config.yaml`: stdio (`command`/`args`/`env`) o HTTP (`url`/`headers`/`auth`).
- Auth oauth/header/mTLS; tokens en `~/.hermes/mcp-tokens/`; naming `mcp_<server>_<tool>`;
  filtrado include/exclude. `hermes mcp serve` expone Hermes como server MCP.

### Mensajeria

- Gateway unico, con plataformas documentadas en el indice vivo (Telegram, Discord,
  Slack, WhatsApp, Signal, SMS, Email, Matrix, Teams, Mattermost, Home Assistant,
  BlueBubbles/iMessage, LINE, ntfy, Google Chat, Raft, y asiaticas: DingTalk,
  Feishu/Lark, WeCom, Weixin, QQ, Yuanbao).
- Autorizacion **deny-by-default**: allowlists (`TELEGRAM_ALLOWED_USERS`, ...) o **DM pairing**
  (codigos de 8 chars, expiran 1h, rate-limited; aprobar via `hermes pairing approve`).

### Seguridad — 8 capas de defense-in-depth

1. Autorizacion de usuario (allowlists + DM pairing). 2. Aprobacion de comandos peligrosos
(`approvals.mode`: `manual`/`smart`/`off`). 3. Seguridad de escritura de archivos (denylist
y sandbox opcional para `write_file`/`patch`). 4. Aislamiento por contenedor (docker/singularity/
modal con hardening). 5. Filtrado de credenciales MCP. 6. Escaneo de prompt-injection en
context files. 7. Aislamiento cross-session. 8. Sanitizacion de entrada/working-dir.
Ademas: **blocklist hardline siempre-on** (wipes irreversibles, fork bombs, escritura a
block-device) y **escaneo Tirith** pre-ejecucion (homografos, pipe-to-interpreter, inyeccion
de terminal). YOLO via `--yolo`, `/yolo` o `HERMES_YOLO_MODE=1`.

## CLI (catalogo vivo en `/docs/reference/cli-commands`)

No persistir ni memorizar el recuento: verificar el catalogo vivo. Familias frecuentes:
`setup`, `model`, `chat`, `gateway`, `doctor`, `status`, `logs`, `config`, `update`,
`uninstall`; `cron`, `kanban`, `webhook`, `checkpoints`, `curator`, `bundles`, `profile`,
`proxy`, `acp`, `lsp`, `plugins`, `memory`, `secrets` (Bitwarden), `fallback`, `auth`,
`insights`, `dashboard`, `computer-use`, `pairing`, `send`, `backup`, `import`, `hooks`,
`sessions`, `mcp`, `skills`, `tools`, `prompt-size`, `security audit`, `portal`;
`claw` (migracion desde OpenClaw, ej. `hermes claw migrate`) y `migrate` (desde modelos
retirados, ej. `hermes migrate xai`). **No inventar flags ni subcomandos**: lo que no
esta en `/docs/reference/cli-commands` u otra subpagina vigente, no existe.

## Instalacion

- Linux/macOS/WSL2/Termux: `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`
  (tambien modo root: `sudo curl ... | sudo bash`, layout FHS bajo `/usr/local/`).
- Windows: `iex (irm https://hermes-agent.nousresearch.com/install.ps1)`
- **Docker**: la imagen oficial `nousresearch/hermes-agent` corre Hermes completo en un
  contenedor montando `~/.hermes` en `/opt/data` (`docker run ... nousresearch/hermes-agent setup`,
  luego `gateway run` supervisado por s6-overlay). Distinto de Docker como backend de `terminal`.
- Nix tiene guia propia (flake/NixOS) pero el canon lo marca best-effort, no ruta soportada.
- El instalador trae sus runtimes (Python via uv, Node, ripgrep, ffmpeg); launcher en
  `~/.local/bin/hermes`, estado en `~/.hermes/`.

## Reglas Duras

1. **Fetch vivo antes de afirmar.** Memoria de entrenamiento != fuente.
2. **Canon = SSOT.** Fuente externa que contradice -> gana el canon.
3. **Prohibido snapshot local del canon** (no `referencias/`, no mirror offline).
   EXCEPCION UNICA v2.2.0 (2026-08-06, HITL): la emision Hermes porta
   `references/official-docs-index.md` (indice llms.txt, sha256 f502e5ad...2e93,
   sondeo 2026-08-06; copia custodiada en `referencias/llms-index.txt` de este canon)
   como base de conocimiento fundamental — cache navegable, NUNCA autoridad: cada
   URL se resuelve en vivo antes de afirmar; refrescar cuando el hash del asset
   llms-*.txt cambie. Cualquier otro snapshot sigue prohibido.
4. **Secretos en `.env`, nunca en `config.yaml`.**
5. **No copiar bloques largos:** citar ruta y sintetizar.
6. **No completar huecos** con certeza falsa: si la doc no resuelve, decirlo.
7. **Hermes Agent != modelos Hermes LLM.** Aclarar si hay ambiguedad.
8. **Comandos destructivos** (`rm -rf ~/.hermes`, borrar `MEMORY.md`) requieren confirmacion explicita.
9. **No inventar flags/subcomandos/archivos.** Lo que no esta en el canon, no existe.
10. **`SOUL.md` solo en `HERMES_HOME`**, nunca en cwd; nunca sobrescribir uno existente.

## Auditoria de un agente Hermes existente

1. Inventario: `SOUL.md`, `config.yaml`, `.env`, context files, memoria, skills, canales,
   MCP servers, `terminal.backend`.
2. Contraste pieza por pieza contra su subpagina canonica.
3. Reporte de brechas con severidad y accion minima (no reescribir todo).

Anti-patrones que se reportan siempre:

- secretos en `config.yaml` en vez de `.env`.
- `SOUL.md` fuera de `HERMES_HOME`, generico copiado, o tratado como archivo de proyecto.
- `MEMORY.md`/`USER.md` excediendo sus limites de chars.
- skills duplicando responsabilidad de context files o de `SOUL.md`.
- modelo con contexto <64k tokens (incluye Ollama en su default 4096 sin `OLLAMA_CONTEXT_LENGTH=64000`, que la doc recomienda para alcanzar el piso; reportar como ajuste necesario, no como flag obligatorio del canon).
- MCP servers sin escopado/filtrado claro; secretos MCP sin filtrar.

## Puentes con KORA y OpenClaw

Felix opera tres ecosistemas de agentes con patrones cercanos pero **no intercambiables**:

| Ecosistema | Doctrina | Memoria | Skills | Despliegue |
|------------|----------|---------|--------|------------|
| Hermes Agent | `SOUL.md` (HERMES_HOME) + canon vivo | `MEMORY.md` + `USER.md` (snapshot) | agentskills.io | `terminal.backend` |
| OpenClaw | blueprints + gateway | sesiones gestionadas | `SKILL.md` propio | systemd user units |
| KORA pneuma | `ley/` + custodio | corpus filesystem | skills/agentes versionados | transmutacion |

Reglas de puente:

- **Migracion nativa OpenClaw -> Hermes**: existe `hermes claw migrate` con presets
  (full/user-data), `--migrate-secrets`, `--skill-conflict`. Relevante directo para Felix
  (opera la flota OpenClaw): no improvisar, verificar el comando vivo antes de ejecutar.
- Skills agentskills.io son cercanas a las de Claude Code y a las skills KORA pero **no
  intercambiables sin verificacion** de formato contra `/docs/user-guide/features/skills`.
- `SOUL.md` (Hermes) != agente KORA != subagente Claude Code: no mezclar frontmatter ni
  convenciones sin declarar la traduccion.

## Composicion

| Composable con | Cuando |
|----------------|--------|
| `urn:kora:artefacto:mente-omega` | la decision de diseno del agente Hermes requiere razonamiento estructural-discursivo previo |
| `urn:dev:artefacto:ship-discipline` | el deploy/operacion de Hermes implica cambios de codigo con blast radius a estimar |

## Salida Esperada

- respuesta breve y accionable; comandos y rutas exactos verificados contra la doc.
- archivos completos cuando se pide generacion.
- referencia(s) a la(s) ruta(s) `/docs/...` consultada(s).
- inferencias y areas no cubiertas por la doc, etiquetadas.
- en auditorias: tabla de brechas con severidad y accion minima propuesta.
