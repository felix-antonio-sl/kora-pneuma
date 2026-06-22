# Reporte de auditoría — agentes y skills de ~/.claude no controlados por kora-pneuma

**Fecha**: 2026-06-22 · **Alcance**: los 27 elementos de `~/.claude/{agents,skills}` sin contraparte en el corpus pneuma (8 agentes + 19 skills) · **Método**: workflow de 54 agentes — 27 auditorías (3 pilares + redundancia, leyendo emisión runtime + fuente bestia) → 27 verificaciones adversariales de contexto limpio. **27/27 veredictos sostenidos por el verificador (0 corregidos).**

## Veredicto

| Veredicto | N | Significado |
|---|---|---|
| **DESCARTAR** | 16 | Redundante con pneuma vigente (ley+kora.py o artefacto activo) u obsoleto → retirar de `~/.claude`, no migrar |
| **MIGRAR** | 7 | Valor real, no redundante, dominio sin cobertura → sublimar a pneuma con shape ley/2 |
| **REUBICAR** | 3 | Repo-local de deep-opm-pro instalado por error a global → mover al `.claude/` del proyecto |
| **CONSERVAR-EXTERNO** | 1 | Nativo legítimo de Claude Code (ai-fluency) → dejar como está |

## Hallazgos transversales

1. **Las mega-personas de diseño ya fueron unificadas por el operador (HITL 2026-06-14).** Cuatro agentes/skills (`steve-jobs-agentic-designer`, `jobs-healthcare-ux`, `jobs-web-ux`, `ux-research-design-ai`) son encarnaciones de origen del agente pneuma `steve-jobs` + sus KB-lente (`-principios-salud`, `-principios-web-ai`). Verificado por **hash sha256 coincidente** citado en la fuente de steve-jobs. Su deploy en `~/.claude` es residuo pre-unificación.
2. **El toolchain meta-KORA de la bestia fue sublimado a ley + mecanizado en kora.py.** Siete skills (`custodio-kora`, `kora-agents`, `kora-skills`, `kora-agentic-lifecycle`, `koraficacion-knowledge`, `transmute-claude-code`, `transmute-openclaw`) enseñaban a mano lo que hoy `ley/0..4` legisla y `kora.py` (gestos velar/transmutar/ciclo/censo) ejecuta. Redundancia 1:1 verificada contra líneas de `kora.py` y secciones de `ley/`.
3. **Desalineación doctrinal sistémica.** TODAS las fuentes bestia usan el shape anidado (`_manifest`/`extensions.kora`/`atlas`) que `ley/2 §1` prohíbe, y su Knowledge Contract cita specs bestia (md-spec, autoria-spec, knowledge-spec, harness-spec, gobernanza) ya sublimadas a `ley/0..4`. Es el costo de la posta incompleta bestia→pneuma: cada MIGRAR implica reescribir el frontmatter al shape plano y reanclar a la ley vigente.
4. **Mal-formación de vector recurrente.** Varios agentes bestia declaran `mu=1`, fuera del dominio de `forma: agente` (ley/2 §7 exige mu∈{2,3}). Al migrar hay que corregir el vector, no copiarlo.
5. **Los 3 REUBICAR son todos de deep-opm-pro** (`hu-progress-auditor`, `lineas-paralelas`, `test-vivo-iterativo-opmkv`): repo-local que su propio cuerpo declara no-global, instalado por error a `~/.claude`.

## Acciones — MIGRAR (7): sublimar a pneuma

Cada uno: reescribir frontmatter al shape plano ley/2, reanclar Knowledge Contract a ley/0..4, corregir vector si está fuera de dominio, `velar`, `transmutar`. **`ifml-architect` es migración GATED**: primero migrar la skill `ifml` + su corpus KB `ifml-*`, luego el agente que delega en ella.

### agent-architect `[AGENTE]` — F2/C4/V4, conf alta
*Acción:* Sublimar a pneuma como agente bajo artefactos/agentes/dev/agent-architect.md con el shape de autoria ley/2 (frontmatter plano cerrado: urn, nombre, version, estado, descripcion, fuente con sha256:cb746b66..., vector, sigma, arnes=orquestador, forma=agente, herramientas, targets). CORREGIR el vector al migrar: mu=1 esta fuera del dominio de agente — elevar a mu>=2 (un orquestador de autoria con memoria y juicio justifica mu>=2; ademas phi=2 implica mu>=1 por ley/1 §4-regla3, y agente exige mu{2,3}). REEMPLAZAR el...

### ifml-architect `[AGENTE]` — F2/C2/V3, conf alta
*Acción:* Migracion GATED, no aislada. Orden obligatorio: (1) primero sublimar a pneuma la skill ifml (desde /home/felix/kora/artifacts/skills/kora/ifml) y el corpus de conocimiento ifml-* (9 KBs en /home/felix/kora/artifacts/knowledge/fxsl/ifml/) — sin ellos el agente queda colgante. (2) Luego sublimar ifml-architect a /home/felix/kora-pneuma/artefactos/agentes/dev/ifml-architect.md con shape plano ley/2 (urn, nombre, version, estado, descripcion, fuente con sha256:e2bcb6de..., vector, sigma, arnes, forma, herramientas, ...

### consenso-deliberativo `[SKILL]` — F3/C5/V5, conf alta
*Acción:* Sublimar a pneuma como artefactos/skills/kora/consenso-deliberativo/SKILL.md con shape de autoria ley/2 (frontmatter plano cerrado): urn:kora:artefacto:consenso-deliberativo, nombre, version (subir desde 1.0.1), estado activo, descripcion 1-linea, fuente con sha256:bfe841fa... apuntando a la bestia; vector [2,0,1,0,1], sigma [1,1,3,1,0], arnes disciplina, forma habilidad, herramientas [Read,Glob,Grep], targets {claude-code,codex,opencode,openclaw}. ACTUALIZAR DOCTRINA: re-anclar el Knowledge Contract de specs be...

### graphic-design `[SKILL]` — F3/C3/V4, conf alta
*Acción:* Sublimar a /home/felix/kora-pneuma/artefactos/skills/dev/graphic-design/SKILL.md via 'kora transmutar' (o autoria manual) con: (1) reescribir frontmatter al shape plano cerrado de ley/2 — urn:kora:artefacto:graphic-design, nombre, version, estado=activo, descripcion 1 linea, fuente con sha256 de la bestia (fe261c35...), vector [2,0,1,0,1], sigma [1,1,2,1,0], arnes=disciplina, forma=habilidad, herramientas=[], targets={claude-code,codex,opencode,openclaw}; eliminar _manifest/extensions.kora/atlas/vector_ontologic...

### hermes-agent-specialist `[SKILL]` — F3/C5/V4, conf alta
*Acción:* Sublimar a pneuma en artefactos/skills/dev/hermes-agent-specialist/SKILL.md re-autorando el frontmatter del shape bestia (_manifest anidado) al shape plano cerrado de ley/2: urn, nombre, version (subir desde 0.1.1), estado=activo, descripcion (1 linea), fuente con sha256:656d2b29... de la bestia, vector [2,0,2,0,1], sigma [2,0,2,2,0], arnes=disciplina, forma=habilidad, herramientas [Read,Write,Edit,Glob,Grep,Bash,WebFetch], targets {claude-code,codex,opencode} (excluir hermes y openclaw como target propio: son l...

### ifml `[SKILL]` — F4/C5/V5, conf alta
*Acción:* Sublimar a pneuma como artefactos/skills/fxsl/ifml/SKILL.md (ns fxsl, coherente con su corpus urn:fxsl:kb:ifml-*) reescribiendo el frontmatter anidado de la bestia al shape plano cerrado de ley/2: urn, nombre, version (subir desde 1.0.1), estado=activo, descripcion (1 linea), fuente con sha256, vector [2,0,1,0,1], sigma [1,1,3,1,0], arnes=disciplina, forma=habilidad, herramientas [Read,Grep,Glob], targets {claude-code,codex,opencode,openclaw} (revisar inclusion de hermes). CO-MIGRAR como prerequisito el corpus d...

### ux-design `[SKILL]` — F3/C5/V4, conf alta
*Acción:* Sublimar a /home/felix/kora-pneuma/artefactos/skills/dev/ux-design/SKILL.md con shape de autoria ley/2: frontmatter YAML plano cerrado (urn:kora:artefacto:ux-design o reasignar ns a dev; nombre, version, estado=activo, descripcion 1-linea, fuente con sha256:c52c436ed4febe7c3fab00eeafb9ab4a4a9a1d9551085088e10d8e65deb05379, vector [2,0,1,0,1], sigma [1,2,2,1,0], arnes=disciplina, forma=habilidad, herramientas=[], targets={claude-code,codex,opencode,openclaw}). Conservar el cuerpo intacto (Nielsen/WCAG/patrones/inv...

## Acciones — REUBICAR (3): mover al proyecto

Mover de `~/.claude/skills/<n>/` al `.claude/skills/` de deep-opm-pro; no canonizar en pneuma.

### hu-progress-auditor `[SKILL]` — F2/C5/V3, conf alta
*Acción:* Retirar la emision global /home/felix/.claude/skills/hu-progress-auditor (rm del directorio) por violar la propia regla dura 'repo-local, nunca global'. NO canonizar en pneuma (es repo-local de un proyecto, no doctrina transversal de KORA). La copia legitima YA existe en /home/felix/projects/deep-opm-pro/.claude/skills/hu-progress-auditor; verificar que ese repo-local este al dia respecto a la version 0.1.1 de la fuente bestia y dejar solo esa. Si se quiere preservar reproducibilidad, mantener la fuente congelad...

### lineas-paralelas `[SKILL]` — F4/C4/V3, conf alta
*Acción:* Retirar la instalacion global erronea: rm -rf /home/felix/.claude/skills/lineas-paralelas/ (y equivalentes globales en ~/.codex/skills, ~/.opencode/skills si existieran). La skill ya vive correctamente en /home/felix/projects/deep-opm-pro/.claude/skills/lineas-paralelas/SKILL.md; si esa copia repo-local debe actualizarse, re-transmutar desde la fuente bestia con alcance_despliegue=/home/felix/projects/deep-opm-pro. NO canonizar en kora-pneuma (es repo-local con paths hardcodeados, no doctrina KORA). NO migrar su...

### test-vivo-iterativo-opmkv `[SKILL]` — F3/C5/V4, conf alta
*Acción:* Mover la skill al .claude/ del proyecto: instalar en /home/felix/projects/deep-opm-pro/.claude/skills/test-vivo-iterativo-opmkv/SKILL.md (junto a sus hermanas hu-progress-auditor y lineas-paralelas que ya viven ahi) y RETIRAR la emision global /home/felix/.claude/skills/test-vivo-iterativo-opmkv/. No canonizar en pneuma (no es doctrina del corpus; es QA repo-local). Idealmente: tambien reubicar las dos hermanas globales (hu-progress-auditor, lineas-paralelas) que estan igualmente duplicadas en ~/.claude. La FUEN...

## Acciones — CONSERVAR-EXTERNO (1)

### ai-fluency `[SKILL]` — F4/C5/V3, conf alta
*Acción:* Dejar como esta en /home/felix/.claude/skills/ai-fluency/ (SKILL.md + insight.py + reference/), fuera del regimen pneuma. No crear URN, no migrar a artefactos/skills/, no asignar vector/sigma/arnes. No requiere intervencion: es un plugin nativo legitimo del ecosistema Claude Code. Opcional: si en el futuro el censo de kora.py marca ~/.claude global, anotarla en una allowlist de 'nativos no-KORA' para que el velar no la confunda con una emision huerfana.

## Acciones — DESCARTAR (16): retirar del runtime

Retirar la emisión de `~/.claude`; la fuente bestia queda congelada in situ (régimen de bestia, no se toca). **Acción destructiva — requiere visto bueno del operador antes de ejecutar.**

### forjador-openclaw `[AGENTE]` — F2/C3/V1, conf alta
*Acción:* Retirar la emision del runtime: rm /home/felix/.claude/agents/forjador-openclaw.md. No migrar a pneuma mientras el target openclaw siga 'reconocido, no realizado' (ley/3): un agente que forja un runtime inexistente no tiene contrato ejecutable. Dejar la fuente bestia congelada en /home/felix/kora (no tocar). Si en el futuro pneuma realiza T-openclaw-pneuma-v1 (sale del estado GENESIS), reconsiderar su migracion reescribiendo shape a ley/2, actualizando Knowledge Contract de autoria-spec/gobernanza a ley/0..4, co...

### fugaz `[AGENTE]` — F1/C3/V1, conf alta
*Redundante con:* urn:dev:artefacto:steipete + urn:dev:artefacto:ship-discipline (ambos activos en pneuma)
*Acción:* Retirar la emision del runtime: eliminar /home/felix/.claude/agents/fugaz.md. NO migrar a pneuma. La fuente bestia /home/felix/kora/artifacts/agents/dev/fugaz/AGENT.md queda congelada en su sitio (no se toca, regimen de bestia). Si en algun futuro se quiere un perfil 'ejecutor ligero', se logra invocando steipete con ship-discipline en modo acotado, no con un agente dedicado redundante."

### jobs-healthcare-ux `[AGENTE]` — F1/C4/V1, conf alta
*Redundante con:* urn:dev:artefacto:steve-jobs (agente activo) + urn:dev:kb:steve-jobs-principios-salud (kb publicado, lente clinica)
*Acción:* Retirar la emision del runtime: eliminar /home/felix/.claude/agents/jobs-healthcare-ux.md. No migrar la fuente bestia a pneuma — su valor ya esta sublimado en steve-jobs (agente) + steve-jobs-principios-salud (kb lente). Para cubrir el caso de uso clinico-UX en runtime, asegurar que la EMISION de steve-jobs este desplegada a claude-code (transmutacion desde urn:dev:artefacto:steve-jobs). El kb fuente principios-constitucionales.md de la bestia tampoco migra: su contenido vive integro en el kb pneuma de lente sal...

### opm-specialist `[AGENTE]` — F2/C3/V1, conf alta
*Redundante con:* urn:fxsl:artefacto:dov-dori (dov-dori.md, activo, v1.5.0)
*Acción:* Retirar la emision /home/felix/.claude/agents/opm-specialist.md del runtime de Claude Code y NO migrar a pneuma. Su funcion ya esta cubierta y superada por dov-dori (modo subagente-batch para dictamenes OPM). La fuente bestia /home/felix/kora/artifacts/agents/fxsl/opm-specialist/AGENT.md queda congelada sin sublimar. Antes de borrar la emision, confirmar con el operador que no hay invocaciones externas hardcodeadas a 'opm-specialist'; si las hubiera, redirigir a dov-dori en modo subagente."

### steve-jobs-agentic-designer `[AGENTE]` — F2/C4/V1, conf alta
*Redundante con:* urn:dev:artefacto:steve-jobs (/home/felix/kora-pneuma/artefactos/agentes/dev/steve-jobs.md)
*Acción:* Retirar la emision /home/felix/.claude/agents/steve-jobs-agentic-designer.md del runtime Claude Code (su fuente bestia ya quedo congelada y conceptualmente superseida). No migrar a pneuma: la funcion ya vive, mejorada, en el agente vigente steve-jobs. Verificar que steve-jobs este emitido/transmutado a ~/.claude/agents/ como reemplazo antes de borrar, para no dejar hueco de capacidad.

### ux-research-design-ai `[AGENTE]` — F2/C3/V2, conf alta
*Redundante con:* agente pneuma steve-jobs + skills ux-design/jobs-web-ux
*Acción:* Retirar la emision /home/felix/.claude/agents/ux-research-design-ai.md del runtime y NO migrar a pneuma. Su funcion (critica/diagnostico UX para productos con IA) ya esta cubierta por el agente vigente steve-jobs (lente steve-jobs-principios-web-ai) mas las skills ux-design y jobs-web-ux. Su forma esta mal asignada (vector de subagente etiquetado como agente), su Knowledge Contract apunta a kb tde que el operador dejo deliberadamente en la bestia, y sus dos dependencias de composicion (ux-design, ifml) no existe...

### custodio-kora `[SKILL]` — F1/C3/V1, conf alta
*Redundante con:* kora.py (gesto velar + censo/ley) y ley/0..4 en /home/felix/kora-pneuma
*Acción:* Retirar la emision del runtime: eliminar /home/felix/.claude/skills/custodio-kora/ (SKILL.md + 3 referencias). No migrar a pneuma: su funcion ya la cumplen kora.py (gesto velar, 11 checks mecanizados) + ley/0..4, y su fuente bestia /home/felix/kora/artifacts/skills/kora/custodio-kora/ queda congelada/omitida. Si en el futuro se quisiera una guia de custodia no-mecanizada, debe nacer desde cero contra ley/0..4 y el toolchain kora.py de 6 gestos, no migrarse desde este artefacto cuyo Knowledge Contract entero apun...

### database-designer `[SKILL]` — F1/C4/V2, conf alta
*Acción:* Retirar la emision del runtime: eliminar /home/felix/.claude/skills/database-designer/ (SKILL.md + references/). No migrar a pneuma: la fuente vive en _TALLER/INBOX nunca promovido y carece de shape de autoria; su valor es generico no anclado y el operador ya la dejo sin curar. Dejar la fuente en la bestia congelada como esta (no requiere correccion de verdad). Si en el futuro emerge una necesidad real de diseno de BD, autorar de cero una skill kora-pneuma con shape ley/2 (forma=habilidad, arnes=utilidad) destil...

### jobs-web-ux `[SKILL]` — F1/C4/V0, conf alta
*Redundante con:* urn:dev:artefacto:steve-jobs [activo] + urn:dev:kb:steve-jobs-principios-web-ai [publicado]
*Acción:* Retirar la emision /home/felix/.claude/skills/jobs-web-ux/SKILL.md del runtime de Claude Code (rm del directorio /home/felix/.claude/skills/jobs-web-ux/). NO migrar: su valor ya esta sublimado en pneuma como agente steve-jobs + kb steve-jobs-principios-web-ai. La fuente _TALLER/INBOX queda congelada en la bestia (ya marcada como no-migrante en la procedencia de ambos artefactos pneuma). Si el operador quiere la capacidad UX web-AI en runtime, transmutar el agente steve-jobs vigente (que ya targetea claude-code) ...

### jointjs-open-source `[SKILL]` — F2/C4/V1, conf alta
*Redundante con:* urn:dev:kb:jointjs-docs (conocimiento, publicado) + urn:kora:artefacto:modelamiento-opm (skill, activo)
*Acción:* Retirar la emision del runtime: borrar /home/felix/.claude/skills/jointjs-open-source/ (toda la carpeta). NO sublimar a pneuma. La funcion ya esta cubierta por dos artefactos pneuma vigentes (kb urn:dev:kb:jointjs-docs publicado + skill modelamiento-opm activa que la reabsorbio explicitamente). La fuente bestia /home/felix/kora/artifacts/skills/kora/jointjs-open-source/ queda congelada in situ (no se toca: regimen de congelacion de la bestia). Si en el futuro se necesita un especialista JointJS dedicado (no solo...

### kora-agentic-lifecycle `[SKILL]` — F1/C1/V1, conf alta
*Redundante con:* kora.py (gestos ciclo/transmutar/velar/censo) + ley/0..4 (shape, formas, leyes inter-eje, gobernanza de targets)
*Acción:* Retirar la emision del runtime: rm -rf /home/felix/.claude/skills/kora-agentic-lifecycle/. No migrar a pneuma: su funcion ya esta mecanizada por kora.py (ciclo+transmutar+velar+censo) y legislada en ley/0..4. La fuente bestia (~/kora/artifacts/skills/kora/kora-agentic-lifecycle/) queda congelada en su repo; no sublimar. Si se quisiera guia narrativa del ciclo de vida para humanos, vive como conocimiento derivado de ley/3, no como skill que ordena comandos inexistentes (kora check/index/transmute/deploy-builds) n...

### kora-agents `[SKILL]` — F1/C3/V1, conf alta
*Redundante con:* ley/0..4 (0-constitucion, 1-ontologia §arnes/leyes-inter-eje, 2-forma §forma-material/arnes-x-forma) + toolchain kora.py (gesto velar valida el shape de autoria)
*Acción:* Retirar la emision del runtime: eliminar /home/felix/.claude/skills/kora-agents/ (junto al cluster meta-bestia kora-skills/kora-agentic-lifecycle/custodio-kora/koraficacion-knowledge si comparten el mismo destino). NO migrar a pneuma: su funcion ya esta cubierta por ley/0..4 + kora.py velar. La fuente bestia (~/kora/artifacts/skills/kora/kora-agents) queda congelada in situ; no se sublima. Si en una auditoria futura el operador detecta que falta GUIA NARRATIVA de autoria no-mecanizada que la ley no capture, abri...

### kora-skills `[SKILL]` — F1/C2/V1, conf alta
*Redundante con:* ley/2-forma.md (gramática de autoría de skills) + kora.py gestos velar/transmutar/ciclo (mecanización de auditoría, proyección y lifecycle)
*Acción:* Retirar la emisión del runtime: eliminar /home/felix/.claude/skills/kora-skills/ (rm -rf del directorio). NO migrar a pneuma: su función (autoría y auditoría de skills) ya está cubierta por ley/2-forma.md (la gramática) y kora.py velar/transmutar/ciclo (la mecanización). La fuente bestia /home/felix/kora/artifacts/skills/kora/kora-skills/ permanece congelada in situ; no se sublima. Si el operador quiere una guía narrativa de autoría futura, esa guía es la propia ley/2, no una skill.

### koraficacion-knowledge `[SKILL]` — F1/C2/V1, conf alta
*Redundante con:* ley/4-koraficacion.md (pneuma, v1.0.0 vigente)
*Acción:* Retirar la emision del runtime: eliminar /home/felix/.claude/skills/koraficacion-knowledge/ (SKILL.md + referencias/ + scripts/). NO migrar a pneuma: la funcion ya vive en ley/4-koraficacion.md. La fuente bestia /home/felix/kora/artifacts/skills/kora/koraficacion-knowledge/ queda congelada (sin cambios). Si en el futuro se quiere una skill operativa que OPERE bajo ley/4 (vs la ley que solo legisla), seria una autoria FRESCA en pneuma con shape ley/2, doctrina ley/4 y frontmatter plano — no una migracion de esta ...

### transmute-claude-code `[SKILL]` — F2/C2/V1, conf alta
*Redundante con:* ley/3-transmutacion.md (funtor T-claude-code-pneuma-v1) + kora.py gesto transmutar (cmd_transmutar)
*Acción:* Retirar la emision del runtime: eliminar /home/felix/.claude/skills/transmute-claude-code/. No migrar a pneuma: su funcion (transmutacion a claude-code) ya esta legislada en ley/3-transmutacion.md y mecanizada en kora.py (cmd_transmutar). La fuente bestia en ~/kora/artifacts/ queda congelada como esta; no requiere correccion de verdad. Si se desea conservar guia narrativa de fidelidad por forma, ya vive en ley/3 par4.1 y la tabla de targets.

### transmute-openclaw `[SKILL]` — F2/C4/V0, conf alta
*Redundante con:* ley/3-transmutacion.md + gesto transmutar de kora.py (toolchain pneuma)
*Acción:* Retirar la emision del runtime: borrar /home/felix/.claude/skills/transmute-openclaw/. No migrar a pneuma. La fuente bestia (/home/felix/kora/artifacts/skills/kora/transmute-openclaw/) queda congelada in situ sin sublimar; su funcion ya esta cubierta-y-negada por ley/3-transmutacion.md (openclaw = target reconocido no realizado, transmutar falla exit 1) y el gesto transmutar de kora.py. Si en el futuro el operador decide realizar el target openclaw, se legisla en ley/3 (registrar T-openclaw-pneuma-v1 y proyeccio...
