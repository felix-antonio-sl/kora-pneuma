---
urn: urn:dev:artefacto:hermes-agent-specialist
nombre: hermes-agent-specialist
version: 3.0.0
estado: activo
descripcion: "Especialista en agentes Hermes (Nous Research) para crear, configurar, desplegar, operar y auditar agentes contra la documentacion oficial viva en hermes-agent.nousresearch.com/docs/. Usar cuando el operador mencione Hermes Agent, SOUL.md, hermes CLI, agentskills, terminal.backend, perfiles o bots, mensajeria sobre Hermes, MCP en Hermes, migracion desde OpenClaw, o cualquier tarea del ciclo de vida de un agente Hermes — aunque no nombre la skill."
fuente: "Rehecha a fidelidad el 2026-06-22 contra la doc oficial viva (hermes-agent.nousresearch.com/docs/, sondeo de estado 2026-06-22). Deriva de la bestia artifacts/skills/dev/hermes-agent-specialist/SKILL.md v0.1.1 (sha256:656d2b29d2c56ce4b50051625ae475b3051ee2b178b5012d1681798198666991): se conservan proposito, doctrina canon-vivo/no-snapshot, regla >=64k tokens y secretos-en-.env (todas vigentes y confirmadas en el canon). Normalizacion pneuma: frontmatter _manifest/extensions.kora anidado -> shape plano ley/2; vector [2,0,2,0,1] preservado (legal para habilidad); conocimiento (urn:kora:kb:hermes-runtime-extension etc.) OMITIDO por migrar-o-omitir (no encarna en pneuma; ademas esta skill ancla su SSOT al canon web vivo, no a kb congelado). Correcciones de fidelidad: SOUL.md SOLO en HERMES_HOME (nunca cwd); paths/limites de memoria (~/.hermes/memories/, MEMORY.md ~2200c, USER.md ~1375c, snapshot congelado); inventario CLI remitido al canon vivo; deploy = valores de terminal.backend (no subpaginas); proveedores con IDs y catch self-hosted; skills progressive-disclosure 3 niveles + skill_manage; MCP stdio/HTTP detallado; mensajeria con allowlists/pairing; seguridad 7 capas; migracion nativa OpenClaw (hermes claw). bump major: reescritura sustantiva. v1.0.1 (2026-06-23): correccion de fidelidad contra la doc viva (verificacion web adversarial, sondeo 2026-06-23) — `OLLAMA_CONTEXT_LENGTH=64000` se reformula de requisito duro a ajuste necesario para alcanzar el piso de 64k que el canon lista como *recomendado* (default Ollama 4096); el anti-patron auditable deja de marcar falso-incumplimiento. Resto de claims (SOUL.md/HERMES_HOME, limites de memoria, terminal.backend, precedencia config, skills 3-niveles, mensajeria deny-by-default, seguridad 7-capas, hermes claw migrate) confirmados sin deriva. v2.0.0 (2026-07-13): decisión HITL retira `openclaw` de targets; la migracion OpenClaw→Hermes es un puente de entrada soportado por Hermes, no equivalencia ni destino de ejecucion. Elimina cifras de catalogo persistidas: comandos, proveedores, tools, modelos y canales se consultan bajo demanda en el canon oficial. v2.1.0 (2026-08-04): sondeo de fidelidad contra el canon vivo (llms-full.txt, 2026-08-04) — correcciones: ya EXISTE ejecucion/instalacion Docker oficial (imagen nousresearch/hermes-agent, doc en /docs/user-guide/docker); terminal.backend ahora son 7 (agregado vercel_sandbox); el modelo de seguridad ahora tiene 8 capas (nueva capa 3: file write safety); claude-marketplace ya no figura en los hub sources del canon. Resto de claims (SOUL.md/HERMES_HOME, memoria 2200/1375 con snapshot congelado, precedencia config, piso 64k, Ollama/vLLM, skills 3 niveles, MCP, mensajeria deny-by-default, hermes claw migrate) confirmados sin deriva. v2.2.0 (2026-08-06): decision HITL del operador — el indice oficial llms.txt (asset llms-faaf9398aa5828403fd56f6be7989c9f.txt, sha256 f502e5ad7b0d0273631be772af4b665addadec066a8a7ff0255804e4796c2e93, sondeo 2026-08-06) se incorpora como base de conocimiento fundamental de la emision Hermes: cache navegable con clausula de staleness (cada URL se resuelve en vivo antes de afirmar; refrescar cuando el hash del asset llms-*.txt cambie). EXCEPCION explicita a la regla dura #3 (no-snapshot): unico snapshot permitido, declarado en esta version; todo otro snapshot sigue prohibido. Copia byte-identica custodiada en referencias/llms-index.txt de este canon; el puente runtime manual entonces vigente la sincronizo en references/official-docs-index.md y declaro metadata.hermes.source apuntando a este canon; no fue una emision KORA. v2.2.1 (2026-08-23): primer refresco del indice por clausula de staleness — el asset hasheado llms-faaf9398aa5828403fd56f6be7989c9f.txt (sha256 f502e5ad..., sondeo 2026-08-06) murio con 404 tras un redeploy del sitio (el hash embebido en el nombre del archivo es efimero); el indice vivo se resuelve SIEMPRE via el atajo estable /docs/llms.txt, nuevo manifiesto sha256 d3e6618022a0a0e3378e827dd30493dda8fc78ff9172ae3b93237fc139c1c9a2 (sondeo 2026-08-23; indice crece de 135 a 247 entradas: Bot Mode, Automation Blueprints, Desktop App/Plugin SDK, secretos 1Password/Bitwarden, A2A, AWS Bedrock, entre otras). Copia byte-identica re-custodiada en referencias/llms-index.txt. Regla dura #3 actualizada en consecuencia: refrescar por atajo estable, nunca reconstruyendo URLs hasheadas. v2.3.0 (2026-08-23): corrige la frontera fuente/derivado/runtime tras realizar T-hermes-pneuma-v1: la emision KORA conserva el nombre hermes-agent-specialist y referencias/llms-index.txt; el skill incorporado hermes-agent permanece externo; elimina el catalogo volatil de backends y alinea perfiles/proyectos con el canon vivo. v3.0.0 (2026-08-23): reafirma KORA como fuente generica y agnostica y el diagnostico como metodo del adaptador; incorpora profile distributions nativas para agentes mediante T-hermes-pneuma-v2; separa distribucion del agente y terminal.backend; modela ownership, paridad abierta, truncacion runtime, precedencia y colisiones de skills; corrige los falsos absolutos detectados por escenario baseline sobre no sobrescritura de SOUL.md y despliegue. Ensayo adversarial post-cambio v3.0.0: distingue agnosticismo del sistema de la allowlist por artefacto; separa distribucion, hosting Docker y backend Docker; relativiza la frontera ante mounts y credenciales; corrige HERMES_HOME de memoria; limita prompt-size a ensamblaje offline y exige procedencia/contenido antes de atribuir un homonimo al URN KORA. Segundo ensayo adversarial v3.0.0: incorpora managed scope y terminal.home_mode, distingue .env/auth.json/secret sources, trata 2200/1375 como defaults configurables, corrige los defaults de contexto Ollama dependientes de VRAM, modela tres planos de despliegue y separa materializacion KORA de procedencia nativa actualizable. Tercer ensayo adversarial v3.0.0: condiciona hardline al guard stack aplicable, separa transporte API de ensamblaje offline y conducta, incorpora AGENTS.override.md y acota la ausencia de telemetria al core frente a identificacion del cliente por proveedores."
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
(MIT; el core no recopila analítica propia, sin atribuir esa garantía a los
proveedores) de agente autonomo persistente que "se vuelve mas capaz
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

**Frontera KORA v3.0.0**: KORA como sistema de autoría —ley, ontología y forma
fuente— sigue siendo genérico y agnóstico. Cada artefacto puede declarar una
allowlist `targets` de compatibilidad mantenida; eso sitúa sus despliegues sin
convertir un runtime en su identidad. El adaptador Hermes realiza dos productos
distintos: una skill mediante
`T-hermes-pneuma-v1` y un agente completo mediante una profile distribution
`T-hermes-pneuma-v2`. Fuente y derivado no son el mismo objeto: igualdad de
bytes o paridad material no demuestran equivalencia semántica ni conducta
runtime. La forma subagente no se proyecta a perfil. El skill incorporado
`hermes-agent` pertenece al runtime y sigue siendo fuente externa, nunca una
emisión KORA.

## Cuando Usar

- crear un agente Hermes desde cero (instalacion, `hermes setup`, proveedor, primer `SOUL.md`).
- configurar despliegue via `terminal.backend` (resolver sus valores vigentes en el canon).
- conectar canales de mensajeria sobre el gateway de Hermes.
- integrar MCP servers (stdio/HTTP) o exponer Hermes como server MCP.
- ciclo de vida de skills (agentskills.io, `skill_manage`, hub, curator, bundles).
- operar memoria/personalidad (`SOUL.md`, `MEMORY.md`, `USER.md`, context files).
- cron, webhooks, delegation, checkpoints/rollback, kanban, profiles, proxy, ACP/LSP.
- crear, instalar, actualizar o auditar una profile distribution, incluida la
  transmutación de un agente KORA mediante el adaptador Hermes.
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
3. **Qué significa desplegar aquí?** Separar: distribución/actualización del
   perfil, hosting de Hermes o backend de herramientas. Si se dice «Docker»,
   preguntar si Hermes completo corre dentro del contenedor o si Hermes corre
   en el host y sólo `terminal.backend` usa Docker; actualizar el perfil es una
   tercera operación independiente.
4. **Qué perfil y `HERMES_HOME` efectivos?** No inferirlos del nombre visible.

### `clasificar-modo`

| Modo | Disparador | URL primaria de canon |
|------|------------|------------------------|
| **Crear** | "instala / arma / dame un SOUL.md" | `/docs/getting-started/quickstart`, `/docs/getting-started/installation` |
| **Configurar y desplegar** | "deploy a X / conecta canal Y" | `/docs/user-guide/configuration`, `/docs/user-guide/messaging/` |
| **Operar y mantener** | troubleshoot, upgrade, recovery | `/docs/reference/cli-commands` |
| **Gestionar skills** | crear/portar/auditar skills | `/docs/user-guide/features/skills` |
| **Distribuir perfil** | empaquetar/instalar/actualizar un agente completo | `/docs/user-guide/profile-distributions`, `/docs/reference/profile-commands` |
| **Auditar existente** | "revisa este Hermes" | combinacion segun inventario |

### `consultar-canon-vivo`

Hacer **fetch vivo** (WebFetch) de la URL primaria antes de producir nada; fetch en
paralelo de las subpaginas que apliquen. Atajo para LLMs: `/docs/llms.txt`
(indice) y `/docs/llms-full.txt` (completo). Esta fuente custodia el índice
cacheado en `referencias/llms-index.txt`; toda transmutación de la skill copia
esa referencia conservando su nombre. Es un atajo de navegación offline, no
reemplaza el fetch vivo. Mapa de canon:

| Pagina | Cubre |
|--------|-------|
| `/docs/getting-started/quickstart` | flujo end-to-end; regla **>=64k tokens** |
| `/docs/getting-started/installation` | instaladores reales por SO |
| `/docs/getting-started/learning-path` | ruta de aprendizaje |
| `/docs/integrations/providers` | proveedores, IDs, requisitos (confirma >=64k) |
| `/docs/user-guide/configuration` | `config.yaml`, `.env`, `terminal.backend`, precedencia |
| `/docs/user-guide/managed-scope` | claves administradas, precedencia efectiva y límites de enforcement |
| `/docs/user-guide/secrets` | `.env`, secret sources y precedencia de credenciales |
| `/docs/user-guide/profiles` | aislamiento por `HERMES_HOME`, estado y límites del perfil |
| `/docs/user-guide/docker` | Hermes dentro de Docker vs Docker como backend de herramientas |
| `/docs/user-guide/security` | modelo de seguridad vigente |
| `/docs/user-guide/features/overview` | catalogo de capacidades |
| `/docs/user-guide/features/tools` | catalogo vivo de tools y toolsets |
| `/docs/user-guide/features/personality` | `SOUL.md` (canonico) |
| `/docs/user-guide/profile-distributions` | distribución completa, ownership y actualización de perfiles |
| `/docs/reference/profile-commands` | CLI nativa de perfiles y distribuciones |
| `/docs/user-guide/features/memory` | `MEMORY.md`, `USER.md`, tool `memory` |
| `/docs/user-guide/features/context-files` | `.hermes.md`/`HERMES.md`/`AGENTS.md`/`CLAUDE.md`/`.cursorrules` |
| `/docs/user-guide/features/skills` | agentskills.io, progressive disclosure |
| `/docs/user-guide/features/mcp` | MCP servers, `hermes mcp` |
| `/docs/user-guide/features/voice-mode` | voz, TTS |
| `/docs/user-guide/messaging/` | canales, allowlists, DM pairing |
| `/docs/reference/cli-commands` | catalogo CLI completo |
| `/docs/reference/faq` | preguntas frecuentes |

### `producir-artefacto`

Generar el artefacto pedido (config, `SOUL.md`, skill, distribución, comando, diagnostico) apoyado
en lo consultado, no en memoria. Disciplina:

- archivos completos, no fragmentos.
- nunca secretos literales en `config.yaml`; usar `.env`, `auth.json` o secret
  sources oficiales según el mecanismo, sin exponer valores.
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
- Hermes intenta inyectar el contenido completo, pero puede truncarlo
  dinámicamente según el presupuesto de contexto. La paridad sólo prueba
  materia instalada. `prompt-size` prueba ensamblaje local y presupuesto del
  prompt —corre offline, sin llamada API—; un canary vivo en sesión nueva sólo
  prueba la conducta observada en esa ejecución. Ninguna de esas evidencias
  demuestra por sí sola atención completa ni equivalencia semántica.
- El transporte API es otro plano: sólo una traza segura del request saliente o
  evidencia equivalente del cliente/proveedor puede demostrar que el payload
  fue enviado. Debe redactar secretos y datos sensibles; si no existe esa
  observación, declarar `NOT_RUN`. Una respuesta o canary no reconstruye por sí
  sola el payload recibido.
- El starter automático no sobrescribe un `SOUL.md` existente. Una instalación
  o actualización de distribución sí puede reemplazar los factores que su
  manifest declara propios. En el puente KORA, sólo se reconcilia un perfil
  cuyo último sello atribuye el mismo `(URN,hermes)`; un homónimo ajeno bloquea.
  Si el SOUL está vacío/ilegible/ausente, Hermes revierte a la identidad por
  defecto (no falla).

### Memoria: `MEMORY.md` y `USER.md`

- Ambos en `$HERMES_HOME/memories/` (`~/.hermes/memories/` sólo en el perfil
  default). Los defaults son `MEMORY.md` 2200 chars (~800 tokens) y `USER.md`
  1375 chars (~500 tokens); los límites efectivos los resuelven
  `memory.memory_char_limit` y `memory.user_char_limit`, incluida cualquier
  clave fijada por managed scope.
- Inyectados al system prompt como **snapshot congelado** al inicio de sesion (preserva
  el prefix cache): un cambio en sesion no aparece hasta la siguiente.
- Tool `memory`: acciones `add` / `replace` / `remove` (match por substring). **No hay
  `read`** — el contenido ya esta inyectado.

### Context files (de proyecto, distintos de `SOUL.md` y memoria)

- Precedencia **first-match-wins**, un solo tipo por sesion:
  `.hermes.md`/`HERMES.md` -> `AGENTS.override.md` -> `AGENTS.md` ->
  `CLAUDE.md` -> `.cursorrules`
  (las reglas `.cursor/rules/*.mdc` se resuelven bajo `.cursorrules`, no como slot aparte).
- Descubrimiento: `.hermes.md`/`HERMES.md` caminan a la git-root;
  `AGENTS.override.md`/`AGENTS.md`/`CLAUDE.md` desde cwd + subdirectorios;
  `.cursorrules`/`.cursor/rules` sólo cwd.
- `SOUL.md` se carga **independiente** de esta cadena.

### Configuracion y despliegue

- Resolver la configuración efectiva, no recitar una precedencia universal.
  Managed scope gana, para las claves que fija, sobre `config.yaml`, `.env` y
  el entorno del usuario; `hermes config` y `hermes doctor` muestran su origen.
  Para claves no administradas, aplicar la precedencia vigente de
  `/docs/user-guide/configuration`.
- `HERMES_HOME` delimita estado Hermes: config, sesiones, memoria, skills, logs
  y gateway. No redefine necesariamente el `HOME` de herramientas externas:
  en host comparten por defecto el home real y sus credenciales; revisar
  `terminal.home_mode: profile` y las reglas específicas del backend.
- **Credenciales**: `.env` guarda claves/tokens locales; `auth.json` guarda
  autenticación OAuth administrada por Hermes; secret sources oficiales pueden
  inyectar valores desde vaults. Nunca mover unas a otras por rutina, imprimir
  valores ni escribir secretos literales en `config.yaml`.
- Hay tres planos de despliegue que no deben colapsarse: una profile
  distribution empaqueta/actualiza el agente; el hosting decide dónde corre
  Hermes; `terminal.backend` decide dónde ejecutan sus herramientas. Resolver
  cada plano aplicable en su subpágina canónica antes de mutar runtime.
  El runtime puede omitir chequeos de comando peligroso en backends
  containerizados porque el contenedor es la frontera prevista. Antes de
  confiar en ella, revisar mounts, credenciales reenviadas, red y argumentos
  extra: un bind mount escribible entrega acceso directo a esos datos del host.

### Proveedores

- Cualquier modelo agentico requiere **>=64000 tokens** de contexto (literal en quickstart
  y providers). IDs canonicos: `nous` (Nous Portal), `openrouter`, `anthropic`, `openai-api`,
  `gemini`, `copilot`/`copilot-acp`, `xai`/`xai-oauth`, `bedrock`, `azure-foundry`,
  `alibaba`, `qwen-oauth`, `kimi-coding`, `zai`, `deepseek`, `minimax`, `novita`, `nvidia`,
  `huggingface`, `ollama-cloud`, y self-hosted `ollama`, `vllm`, `sglang`, `llama-cpp`,
  `lmstudio`, `custom` (la lista crece; verificar viva).
- Self-hosted crítico: **Ollama** debe exponer al menos 64k. Su default depende
  de VRAM (puede ser 4096, 32768 o 256000); verificar el valor efectivo con
  `ollama ps` y ajustar server-side o por Modelfile sólo si queda bajo el piso.
  **vLLM** necesita `--enable-auto-tool-choice --tool-call-parser hermes`.
- **Nous Portal**: verificar en el canon vivo el catalogo disponible y las
  herramientas Tool Gateway antes de configurar.

### Skills (agentskills.io)

- Hermes descubre skills de proyecto (`.hermes/skills/` y `.agents/skills/`,
  sujetos a confianza), locales bajo `HERMES_HOME/skills/` y directorios
  externos configurados. La precedencia es proyecto > local > externo; una
  ambigüedad dentro del nivel ganador debe resolverse, no elegirse por azar.
- El descubrimiento local es recursivo y reconoce bundles por nombre de
  directorio o frontmatter, además del archivo plano legado. Antes de instalar,
  censar todas las definiciones activas del mismo nombre; archivos archivados o
  fuera de las raíces configuradas no constituyen una colisión runtime.
- **Progressive disclosure de 3 niveles**: `skills_list()` ->
  `skill_view(name)` (contenido) -> `skill_view(name, path)`.
- Precedencia y formato no prueban identidad semántica. Si se afirma que el
  ganador realiza un URN KORA, verificar sello/procedencia y contenido; de lo
  contrario, reportarlo como override externo y no presentar `componible` como
  wiring ni equivalencia.
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
Además, cuando aplica el guard stack, la **blocklist hardline** no se evade con
YOLO ni `approvals.mode: off` (wipes irreversibles, fork bombs, escritura a
block-device), y Tirith escanea antes de ejecutar. Los backends aislados pueden
omitir todo ese stack; no prometer la blocklist allí y revisar si mounts,
credenciales o red hacen que el contenedor alcance recursos reales del host.
YOLO se activa vía `--yolo`, `/yolo` o `HERMES_YOLO_MODE=1`.

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
3. **Prohibido snapshot local del canon** (no mirror offline adicional).
   EXCEPCION UNICA v2.2.0 (2026-08-06, HITL): esta fuente KORA custodia
   `referencias/llms-index.txt` (indice llms.txt) y sus transmutaciones lo copian
   con el mismo nombre — cache navegable, NUNCA autoridad: cada URL se resuelve en vivo
   antes de afirmar; refrescar cuando el indice cambie. v2.2.1 (2026-08-23):
   primer refresco por clausula de staleness — el asset hasheado
   llms-faaf9398aa5828403fd56f6be7989c9f.txt (sha256 f502e5ad..., sondeo
   2026-08-06) ya no existe (404 tras redeploy del sitio; el hash del nombre del
   archivo es efimero). El indice vivo se resuelve SIEMPRE via el atajo estable
   `/docs/llms.txt`: manifiesto actual sha256
   d3e6618022a0a0e3378e827dd30493dda8fc78ff9172ae3b93237fc139c1c9a2 (sondeo
   2026-08-23; copia custodiada byte-identica en `referencias/llms-index.txt`
   de este canon). Cualquier otro snapshot sigue prohibido.
4. **Nunca secretos literales en `config.yaml`.** Usar el mecanismo canónico
   correspondiente (`.env`, `auth.json` o secret source) sin exponer valores.
5. **No copiar bloques largos:** citar ruta y sintetizar.
6. **No completar huecos** con certeza falsa: si la doc no resuelve, decirlo.
7. **Hermes Agent != modelos Hermes LLM.** Aclarar si hay ambiguedad.
8. **Comandos destructivos** (`rm -rf ~/.hermes`, borrar `MEMORY.md`) requieren confirmacion explicita.
9. **No inventar flags/subcomandos/archivos.** Lo que no esta en el canon, no existe.
10. **`SOUL.md` sólo en `HERMES_HOME`**, nunca en cwd. No reemplazar uno
    existente salvo por una operación de distribución explícita y con ownership
    demostrado; el nombre compartido no transfiere propiedad.

## Auditoria de un agente Hermes existente

1. Inventario: `SOUL.md`, `config.yaml`, `.env`, presencia/tipo/permisos de
   `auth.json` sin leer valores, context files, memoria, skills, canales,
   MCP servers, `terminal.backend`, perfil y manifest de distribución cuando
   existan.
2. Contraste pieza por pieza contra su subpagina canonica.
3. Reporte de brechas con severidad y accion minima (no reescribir todo).

Anti-patrones que se reportan siempre:

- secretos literales en `config.yaml`, exposición de valores o uso de un
  mecanismo distinto del que el canon prescribe para esa credencial.
- `SOUL.md` fuera de `HERMES_HOME`, generico copiado, o tratado como archivo de proyecto.
- `MEMORY.md`/`USER.md` excediendo los límites efectivos resueltos, no sólo los
  defaults 2200/1375.
- skills duplicando responsabilidad de context files o de `SOUL.md`.
- dos o más definiciones activas del mismo skill dentro del nivel de precedencia
  ganador.
- modelo con contexto efectivo <64k tokens; en Ollama verificar la columna
  `CONTEXT` de `ollama ps` porque el default varía según VRAM.
- MCP servers sin escopado/filtrado claro; secretos MCP sin filtrar.

## Puentes con KORA y OpenClaw

Felix opera tres ecosistemas de agentes con patrones cercanos pero **no intercambiables**:

| Ecosistema | Doctrina | Memoria | Skills | Despliegue |
|------------|----------|---------|--------|------------|
| Hermes Agent | `SOUL.md` (HERMES_HOME) + canon vivo | `MEMORY.md` + `USER.md` (snapshot) | agentskills.io | profile distribution + `terminal.backend` |
| OpenClaw | blueprints + gateway | sesiones gestionadas | `SKILL.md` propio | systemd user units |
| KORA pneuma | `ley/` + custodio | corpus filesystem | skills/agentes versionados | transmutacion |

Reglas de puente:

- **Migracion nativa OpenClaw -> Hermes**: existe `hermes claw migrate` con presets
  (full/user-data), `--migrate-secrets`, `--skill-conflict`. Relevante directo para Felix
  (opera la flota OpenClaw): no improvisar, verificar el comando vivo antes de ejecutar.
- Skills agentskills.io son cercanas a las de Claude Code y a las skills KORA,
  pero **no son intercambiables**. Verificar formato contra
  `/docs/user-guide/features/skills` sólo prueba compatibilidad estructural;
  atribuir un URN KORA exige además procedencia y contenido.
- El skill incorporado `hermes-agent` es una fuente externa mantenida por Hermes;
  el artefacto KORA se emite e instala como `hermes-agent-specialist`. No fusionar
  ambos objetos ni usar una copia manual del primero como prueba de paridad KORA.
- `SOUL.md` (Hermes) != agente KORA != subagente: no mezclar identidad
  ontológica, frontmatter ni garantías. `T-hermes-pneuma-v2` es una traducción
  declarada agente→profile distribution; conserva procedencia y cuerpo, no
  afirma equivalencia semántica ni enforcement runtime.
- En una distribución KORA, `distribution_owned` se limita a `SOUL.md` y
  `distribution.yaml`. Configuración, memoria, credenciales, skills, cron y MCP
  quedan fuera; `componible` no autoriza autoempaquetarlos. `--aplicar` bloquea
  un perfil homónimo no atribuible y la paridad compara sólo esos dos factores.
- La presencia de `distribution.yaml` no prueba que el instalador nativo haya
  registrado una fuente actualizable. Comprobar `hermes profile info`; si KORA
  materializó los factores directamente, llamarlo despliegue KORA y actualizar
  por KORA. Usar `hermes profile update` sólo cuando exista procedencia nativa
  registrada.

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
