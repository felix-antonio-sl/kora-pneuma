# Plan de implementación: tres frentes — higiene documental, deploy openclaw, posta OPM

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development
> (recommended) or superpowers:executing-plans to implement this plan task-by-task.
> Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Dejar `~/kora-pneuma` limpio (Fase C), entregar los 9 workspaces openclaw
emitidos a la flota viva bajo los nombres de pneuma sin duplicar equivalentes (Fase A),
y cerrar la posta OPM: la ley OPM vive siempre en pneuma, nunca en la bestia (Fase B).

**Arquitectura:** Tres fases **independientes entre sí** — cada una es delegable por
separado, produce commits atómicos propios y cierra con su propio gate. El orden
recomendado es C → A → B (barato → valor retenido → estructural), pero no hay
dependencia técnica entre ellas. Ningún paso edita `GENESIS.md` ni relaja la ley.

**Tech stack:** `kora.py` (stdlib puro), git multi-repo (`~/kora-pneuma`,
`~/openclaw-fleet`, `~/kora`, `~/projects/hd-opm`, `~/projects/hodom-opm`),
systemd user units, CLI `openclaw`.

## Decisiones del operador (taxativas — no re-litigar)

1. **Fase C**: archivar specs ejecutadas y notas destiladas tal como está planificado.
2. **Fase A**: la flota adopta **los nombres de pneuma**. Los equivalentes existentes
   se **renombran preservando su memoria** — jamás debe quedar el par viejo/nuevo
   conviviendo (cero duplicados).
3. **Fase B**: **la ley OPM debe estar siempre en pneuma, no en la bestia.** La bestia
   queda congelada para autoría OPM; los consumidores se repuntan a pneuma.

## Global Constraints

- **Gate universal pneuma**: `python3 ~/kora-pneuma/kora.py velar --estricto` debe dar
  13/13 y `python3 -m unittest discover -s ~/kora-pneuma/tests` 93 tests OK **antes y
  después** de cada tarea que toque `~/kora-pneuma`.
- **Delegation principle del host**: antes de tocar un repo ajeno, leer su
  `CLAUDE.md` (`~/openclaw-fleet/CLAUDE.md`, `~/kora/CLAUDE.md`,
  `~/projects/hd-opm/CLAUDE.md`, `~/projects/hodom-opm/CLAUDE.md`). Sus reglas de
  dominio prevalecen sobre este plan en lo local; si contradicen un paso, detenerse
  y reportar al operador en vez de improvisar.
- **Commits atómicos** por tarea, en el repo que corresponda, siguiendo la convención
  de mensajes de ese repo (ver su `git log`). Nunca commits cruzados multi-repo.
- **Prohibido `sed` global / reemplazo ciego**: todo renombre o repunteo se hace
  leyendo cada match (`rg -n`) y editando dirigido. Motivo concreto: `hospitalista`
  es substring de `medico-hospitalista`; `gtd-integral` puede aparecer en bindings.
- **Verificar contra estado real**, nunca contra el reporte de un subagente: censo,
  `git diff`, `ls`, line-refs.
- **HITL obligatorio** (human-in-the-loop): los escalones marcados ⚠️HITL (agentes
  clínicos/íntimo en Fase A; veredictos migrar-o-omitir en Fase B) requieren
  validación explícita del operador antes de continuar.
- **Canon del runtime en cada transmutación** (directiva del operador 2026-07-06):
  toda transmutación/deploy se ancla a la documentación OFICIAL y VIGENTE del
  runtime destino, leída desde las bases en cada corrida — el canon muta. Para
  openclaw: mirror local `~/openclaw-fleet/docs/openclaw/` (sync diario 10:30 vía
  `openclaw-docs-sync.timer`; páginas clave: `agent-runtime-architecture.md`,
  `openclaw-agent-runtime.md`, `reference/templates/`) + políticas propias de la
  flota (`docs/fleet-canon-policy.md`, `docs/memory-policy.md`). Si la emisión
  T-openclaw contradice el canon vigente, NO aplicar: reportar el drift al
  operador (el fix va en la fuente/funtor, no en el workspace).
- **Anti-despotenciación** (directiva del operador 2026-07-06): el deploy no debe
  despotenciar agentes vivos. Antes de pisar un `AGENTS.md` vivo, diff funcional
  obligatorio (Task A0 Step 4); una capacidad operativa que solo exista en el
  vivo se **absorbe upstream en la fuente pneuma** (y se re-emite) o se declara
  **pérdida aceptada** con el operador (⚠️HITL) — jamás se aplica «y se reza», y
  jamás se edita el workspace o la emisión a mano (eso es drift).
- **Idioma**: es-CL, fechas ISO absolutas (`AAAA-MM-DD`).
- **`_archivo/` está gitignored**: mover un archivo trackeado allí aparece en git
  como deletion. Es el diseño (red de seguridad reversible en filesystem, fuera del
  árbol vivo) — no "corregirlo".

---

## FASE C — Higiene documental de `~/kora-pneuma`

Contexto para el ejecutor: la doctrina de vigencia del repo ordena que los docs
operativos muertos (specs ya ejecutadas, informes cerrados) se desplacen a
`_archivo/` (gitignored). Hay 3 specs ejecutadas en `docs/superpowers/specs/` y 2
notas de aprendizaje en `notas/` cuyo contenido vivo ya fue absorbido por la ley,
las skills o la bitácora externa. Verificado 2026-07-05: las 3 specs corresponden a
trabajo cerrado (`pensamiento-modelador` existe como skill activa; el sistema
componible está legislado en `ley/1`; T-openclaw está realizado en `ley/3 §7.1`).

### Task C1: Archivar las tres specs ejecutadas

**Files:**
- Move: `docs/superpowers/specs/2026-06-19-pensamiento-modelador-design.md` → `_archivo/specs-superpowers/`
- Move: `docs/superpowers/specs/2026-06-30-sistema-componible-agente-design.md` → `_archivo/specs-superpowers/`
- Move: `docs/superpowers/specs/2026-07-01-t-openclaw-rediseno-design.md` → `_archivo/specs-superpowers/`

- [ ] **Step 1: Confirmar que las tres specs están ejecutadas** (no confiar en este plan)

```bash
cd ~/kora-pneuma
python3 kora.py censo | grep pensamiento-modelador   # debe existir, activo
rg -c "sistema componible|módulo" ley/1-ontologia.md  # >0: legislado
rg -c "workspace" ley/3-transmutacion.md              # >0: T-openclaw realizado
```

Expected: las tres verificaciones positivas. Si alguna falla, NO archivar esa spec;
reportar al operador.

- [ ] **Step 2: Desplazar a `_archivo/`**

```bash
cd ~/kora-pneuma
mkdir -p _archivo/specs-superpowers
mv docs/superpowers/specs/2026-06-19-pensamiento-modelador-design.md \
   docs/superpowers/specs/2026-06-30-sistema-componible-agente-design.md \
   docs/superpowers/specs/2026-07-01-t-openclaw-rediseno-design.md \
   _archivo/specs-superpowers/
rmdir docs/superpowers/specs
```

- [ ] **Step 3: Verificar el efecto en git**

```bash
git status --short
```

Expected: exactamente 3 líneas `D docs/superpowers/specs/...` (deletions). Nada más.

- [ ] **Step 4: Commit**

```bash
git add -A docs/superpowers/specs
git commit -m "docs(vigencia): archivar 3 specs superpowers ejecutadas (pensamiento-modelador, sistema-componible, t-openclaw)"
```

### Task C2: Destilar y archivar las dos notas de 2026-06-30

Contexto: `notas/2026-06-30-koraficacion-figuras-langacker.md` y
`notas/2026-06-30-aprendizajes-agente.md` son notas *del agente* (ellas mismas lo
declaran). Su valor reusable debe quedar en la bitácora externa de koraficación
antes de archivarlas.

**Files:**
- Verify/append: `/home/felix/kora-external-sources/bitacora-koraficacion-langacker.md`
- Move: `notas/2026-06-30-*.md` → `_archivo/notas/`

- [ ] **Step 1: Verificar qué lecciones ya están destiladas en la bitácora externa**

```bash
rg -c "figura|subagente|inventar" /home/felix/kora-external-sources/bitacora-koraficacion-langacker.md
```

Criterio: las 4 lecciones clave que deben existir en la bitácora (buscarlas por
concepto, no por string exacto, leyendo la bitácora):
1. Inspección visual de imágenes obligatoria para figuras sin caption (el atajo
   solo-texto es falsa economía).
2. Subagentes paralelos no sirven para producción masiva de artefactos grandes
   (retención de output falla); procesar por capítulos completos, secuencial.
3. Figura faltante se marca `— (no legible en la fuente disponible)`, jamás se
   rellena con descripción genérica.
4. Mapeo por capítulo (placeholder ↔ líneas del .txt ↔ imágenes) en vez de
   batch por figura individual.

- [ ] **Step 2: Apendizar a la bitácora las lecciones que falten** (sección nueva
  `## Aprendizajes de sesión 2026-06-30 (rescatados de notas pneuma)` al final del
  archivo, redactadas en 1-3 líneas cada una, solo las ausentes)

- [ ] **Step 3: Archivar ambas notas**

```bash
cd ~/kora-pneuma
mkdir -p _archivo/notas
mv notas/2026-06-30-aprendizajes-agente.md notas/2026-06-30-koraficacion-figuras-langacker.md _archivo/notas/
rmdir notas
git add -A notas
git commit -m "docs(vigencia): archivar notas de agente 2026-06-30 (lecciones destiladas a bitácora langacker)"
```

### Task C3: Higiene de `.gitignore`

**Files:**
- Modify: `.gitignore`

- [ ] **Step 1: Añadir `.pytest_cache/`** al bloque de derivados

```
# Derivados — regenerables, jamás autoridad (ley/0 §6)
censo.json
_emision/
__pycache__/
*.pyc
.pytest_cache/
```

- [ ] **Step 2: Borrar el caché local (regenerable) y commit**

```bash
cd ~/kora-pneuma
rm -rf .pytest_cache
git add .gitignore
git commit -m "chore(higiene): .pytest_cache/ explícito en .gitignore"
```

### Task C4: Gate de cierre de fase

- [ ] **Step 1: Gate completo**

```bash
cd ~/kora-pneuma
python3 kora.py velar --estricto           # Expected: 13/13, "todo coherente"
python3 -m unittest discover -s tests      # Expected: 93 tests OK
git status --short                         # Expected: vacío
```

---

## FASE A — Deploy openclaw: nombres de pneuma, cero duplicados

Contexto para el ejecutor: los 9 agentes activos de pneuma tienen workspace emitido
en `_emision/openclaw/workspaces/<nombre>/` (AGENTS.md + SOUL.md con sello
`kora:sello`). `kora.py transmutar --target openclaw --aplicar` instala **directo**
en `~/openclaw-fleet/workspaces/{nombre}/` (name-keyed, `kora.py:1317`), escribiendo
SOLO `AGENTS.md` y `SOUL.md` — los otros 5 archivos del workspace (`BOOT.md`,
`IDENTITY.md`, `MEMORY.md`, `TOOLS.md`, `USER.md`) se preservan. El gateway
registra agentes en `openclaw.json.reference` (`.agents.list[]`) con campos `id`,
`name`, `workspace` (ruta absoluta), `agentDir` (`~/.openclaw/agents/<id>/agent`,
estado runtime también keyed por nombre) e `identity.name`.

**Mapa de despliegue (verificado contra estado real el 2026-07-05):**

| Esc. | URN pneuma | Workspace flota hoy | ¿Registrado en gateway? | Acción | HITL |
|---|---|---|---|---|---|
| 1 | `urn:dev:artefacto:agent-architect` | `agent-architect` | no | aplicar directo (piloto) | — |
| 2 | `urn:dev:artefacto:steve-jobs` | `steve-jobs-agentic-designer` | no | renombrar dir → aplicar | — |
| 3 | `urn:dev:artefacto:steipete` | `steipete` | sí | aplicar | — |
| 4 | `urn:fxsl:artefacto:allan-kelly` | `allan-kelly` | sí | aplicar | — |
| 5 | `urn:fxsl:artefacto:dov-dori` | `dov-dori` | sí | aplicar | — |
| 6 | `urn:salud:artefacto:salubrista` | `salubrista` | sí | aplicar | — |
| 7 | `urn:salud:artefacto:urgenciologo` | `urgenciologo` | sí | aplicar | ⚠️HITL clínico |
| 8 | `urn:salud:artefacto:medico-hospitalista` | `hospitalista` | sí | renombre completo → aplicar | ⚠️HITL clínico |
| 9 | `urn:fxsl:artefacto:david-allen` | `gtd-integral` | sí | renombre completo → aplicar | ⚠️HITL íntimo |

**Fuera de alcance explícito** (no tocar): workspaces de la flota sin fuente pneuma
(`mente-omega` — en pneuma es skill, no agente —, `fugaz`, `main`,
`forjador-openclaw`, `ifml-architect`, `jobs-healthcare-ux`, `opm-specialist`,
`polymath`, `ux-research-design-ai`). Su destino es gobernanza de la flota, otra
conversación.

**Regla de escalonamiento**: un escalón a la vez, en el orden de la tabla; entre
escalones, `openclaw health` verde es condición de avance. Clínicos e íntimo al
final, jamás primero. **Condición previa de cada aplicación**: el diff funcional
del agente (A0 Step 4) sin ítems EN RIESGO pendientes. Sonda conversacional:
puede ejecutarse sin Telegram con `openclaw agent` (un turno vía gateway;
sintaxis exacta con `openclaw agent --help`) — la validación de carácter/voz en
los ⚠️HITL sigue siendo del operador. Si un escalón falla, detenerse,
`git -C ~/openclaw-fleet checkout -- <workspace>` para revertir, y reportar.

### Task A0: Canon del runtime + gobernanza de la flota + diff anti-despotenciación

**Files:**
- Read: `~/openclaw-fleet/docs/openclaw/agent-runtime-architecture.md`, `.../openclaw-agent-runtime.md`, `.../reference/templates/`
- Read: `~/openclaw-fleet/docs/fleet-canon-policy.md`, `~/openclaw-fleet/docs/memory-policy.md`
- Read: `~/openclaw-fleet/CLAUDE.md`
- Read: `~/openclaw-fleet/openclaw.json.reference` (solo `.agents.list[]` y `bindings`)

- [ ] **Step 0: Anclar el canon vigente.** Verificar frescura del mirror
  (`systemctl --user list-timers openclaw-docs-sync.timer` — último sync < 48 h;
  si está rancio, correr el sync o leer docs.openclaw.ai). Leer las páginas de
  canon listadas arriba y validar contra ellas la anatomía que la emisión pneuma
  asume: (a) `AGENTS.md` y `SOUL.md` siguen siendo los archivos de instrucciones
  y voz del workspace; (b) qué otros archivos reconoce el runtime hoy y cuáles
  genera/posee él (frontera no-emitida); (c) cualquier campo/convención nueva de
  `agents.list[]` desde la realización de T-openclaw (2026-07-01). Anotar
  conformidad o drift; con drift, DETENERSE (regla global de canon).

- [ ] **Step 1: Leer `~/openclaw-fleet/CLAUDE.md` completo.** Extraer y anotar:
  (a) el procedimiento oficial de sincronización `openclaw.json.reference` ↔
  `~/.openclaw/openclaw.json` (el runtime NO versionado); (b) cómo se
  reinicia/recarga el gateway; (c) cualquier regla propia de renombre o retiro de
  agentes. Si el procedimiento (a) no existe documentado, detenerse y preguntar al
  operador antes de tocar config.

- [ ] **Step 2: Inventariar dónde aparece cada id a renombrar**

```bash
rg -n "gtd-integral|\"hospitalista\"|steve-jobs-agentic-designer" ~/openclaw-fleet/openclaw.json.reference
rg -n "gtd-integral|hospitalista|steve-jobs-agentic-designer" ~/.openclaw/openclaw.json
```

Anotar CADA match con su contexto (agents.list, bindings, channels, commands). Esta
lista es el checklist de los escalones 8 y 9. Cuidado: `"hospitalista"` con comillas
para no matchear `salubrista` ni contaminarse con futuros `medico-hospitalista`.

- [ ] **Step 3: Gate previo en pneuma**

```bash
cd ~/kora-pneuma && python3 kora.py velar --estricto   # 13/13 antes de transmutar (doctrina)
```

- [ ] **Step 4: Diff funcional anti-despotenciación, por agente (los 9).**
  Comparar el `AGENTS.md` VIVO de cada workspace contra la emisión
  `_emision/openclaw/workspaces/<nombre>/AGENTS.md` (para los 3 renombres,
  contra el workspace del nombre viejo). Inventariar cada capacidad operativa
  del vivo — contratos de conocimiento con rutas, fronteras/prohibiciones,
  procedimientos, referencias a herramientas — y clasificarla:
  1. **cubierta**: presente (equivalente funcional) en la emisión;
  2. **preservada**: vive en un archivo que el deploy NO pisa (`BOOT.md`,
     `IDENTITY.md`, `MEMORY.md`, `TOOLS.md`, `USER.md`) — sin riesgo;
  3. **EN RIESGO**: solo existe en el `AGENTS.md` vivo y la emisión no la trae.
  Producto: tabla por agente. Los ítems EN RIESGO bloquean su escalón hasta
  resolverse (⚠️HITL): absorber upstream en la fuente pneuma (editar el
  artefacto agente, `velar`, re-transmutar) o pérdida declarada aceptada por el
  operador. Si se delega este diff a subagentes, spot-checkear sus hallazgos
  contra los archivos reales antes de decidir (doctrina: verificar contra
  estado, no contra reporte).

### Task A1: Escalón 1 — piloto `agent-architect` (blueprint no-vivo)

Por qué piloto: workspace existente, nombre ya alineado, NO registrado en el
gateway → blast radius mínimo.

- [ ] **Step 1: Aplicar**

```bash
cd ~/kora-pneuma
python3 kora.py transmutar --urn urn:dev:artefacto:agent-architect --target openclaw --aplicar
```

Expected: `aplicado: /home/felix/openclaw-fleet/workspaces/agent-architect`

- [ ] **Step 2: Verificar no-destructividad y sello**

```bash
cd ~/openclaw-fleet
git status --short workspaces/agent-architect/
# Expected: SOLO 'M workspaces/agent-architect/AGENTS.md' y 'M .../SOUL.md'
tail -8 workspaces/agent-architect/AGENTS.md   # Expected: bloque <!-- kora:sello ... --> con hash-fuente
```

Si aparece modificado cualquier otro archivo del workspace → ABORTAR, revertir con
`git checkout -- workspaces/agent-architect/`, reportar.

- [ ] **Step 3: Commit en la flota**

```bash
git add workspaces/agent-architect
git commit -m "feat(agent-architect): AGENTS.md+SOUL.md desde pneuma v2.3.0 (sello kora, escalón 1)"
```

### Task A2: Escalón 2 — `steve-jobs` (renombre de dir no-registrado)

- [ ] **Step 1: Renombrar el workspace preservando historia git**

```bash
cd ~/openclaw-fleet
git mv workspaces/steve-jobs-agentic-designer workspaces/steve-jobs
```

- [ ] **Step 2: Verificar que el nombre viejo no queda referenciado en config**
(según inventario A0; si `steve-jobs-agentic-designer` aparecía en algún binding,
actualizarlo dirigido ahora)

- [ ] **Step 3: Aplicar y verificar** (mismo patrón que A1 Step 1-2, con
`--urn urn:dev:artefacto:steve-jobs`)

- [ ] **Step 4: Commit**

```bash
git add -A workspaces/
git commit -m "feat(steve-jobs): renombre a nombre pneuma + AGENTS.md+SOUL.md v1.1.0 (escalón 2)"
```

(El rename ya quedó staged por `git mv`; el `git add -A workspaces/` recoge además
los dos archivos aplicados.)

### Task A3: Escalones 3-6 — vivos nombre-alineado (`steipete`, `allan-kelly`, `dov-dori`, `salubrista`)

Repetir **uno a uno, en ese orden**, el ciclo completo por agente (no batch):

- [ ] **Step 1: Aplicar** (URN de la tabla, mismo comando que A1)
- [ ] **Step 2: Verificar no-destructividad** (`git status --short workspaces/<n>/`
  → solo AGENTS.md y SOUL.md; `MEMORY.md` jamás debe aparecer)
- [ ] **Step 3: Recargar y verificar salud**

```bash
openclaw gateway restart    # hot-reload de workspaces
openclaw health             # Expected: gateway + agentes + Telegram verdes
```

- [ ] **Step 4: Sonda conversacional ligera**: enviar al agente un mensaje de prueba
  vía Telegram (p. ej. "¿quién eres y cuál es tu método?") y verificar que responde
  en su voz sin errores de arranque. No se valida el carácter aquí — solo que vive.
- [ ] **Step 5: Commit por agente** (mensaje: `feat(<nombre>): AGENTS.md+SOUL.md desde pneuma v<X.Y.Z> (escalón <n>)`)

Condición de avance: health verde antes de pasar al siguiente.

### Task A4: Escalón 7 — `urgenciologo` ⚠️HITL clínico

- [ ] **Step 1-3**: mismo ciclo que Task A3 (aplicar, verificar, restart+health).
- [ ] **Step 4 (HITL)**: PAUSA. El operador conversa con el agente y valida
  explícitamente: (a) voz clínica correcta, (b) frontera pediátrica intacta
  (deriva, no atiende), (c) corpus med-emergencia accesible. Solo el operador
  autoriza continuar.
- [ ] **Step 5: Commit.**

### Task A5: Escalón 8 — `hospitalista` → `medico-hospitalista` ⚠️HITL clínico + renombre completo

- [ ] **Step 1: Detener el gateway** (renombre de estado runtime en caliente = corrupción)

```bash
systemctl --user stop openclaw-gateway
```

- [ ] **Step 2: Renombrar workspace (repo flota) y estado runtime**

```bash
cd ~/openclaw-fleet
git mv workspaces/hospitalista workspaces/medico-hospitalista
mv ~/.openclaw/agents/hospitalista ~/.openclaw/agents/medico-hospitalista   # preserva sesiones/memoria runtime
```

- [ ] **Step 3: Actualizar config dirigido** — en `openclaw.json.reference`, entrada
  `.agents.list[]` con `"id": "hospitalista"`: cambiar `id`, `name`,
  `workspace` (→ `/home/felix/openclaw-fleet/workspaces/medico-hospitalista`),
  `agentDir` (→ `/home/felix/.openclaw/agents/medico-hospitalista/agent`) e
  `identity.name` a `medico-hospitalista`. Luego recorrer el inventario A0: cada
  match restante de `"hospitalista"` (bindings, channels, commands) se edita leído,
  uno a uno. Verificación:

```bash
rg -n '"hospitalista"' ~/openclaw-fleet/openclaw.json.reference   # Expected: 0 matches
python3 -c "import json; json.load(open('/home/felix/openclaw-fleet/openclaw.json.reference')); print('JSON válido')"
```

- [ ] **Step 4: Sincronizar al runtime** `~/.openclaw/openclaw.json` según el
  procedimiento documentado en A0 Step 1 (mismas ediciones; verificación `rg` igual).
- [ ] **Step 5: Aplicar emisión** (`--urn urn:salud:artefacto:medico-hospitalista`)
  y verificar no-destructividad (MEMORY.md intacto: `git status --short` solo
  AGENTS.md+SOUL.md dentro del dir renombrado).
- [ ] **Step 6: Arrancar y verificar**

```bash
systemctl --user start openclaw-gateway
openclaw health                    # verde total
journalctl --user -u openclaw-gateway -n 30   # sin errores de workspace/agentDir
```

- [ ] **Step 7 (HITL)**: PAUSA. Operador valida: voz clínica, modos
  hospital/HODOM, y que el agente **conserva su memoria previa** (preguntarle por
  algo que `hospitalista` sabía de sesiones anteriores).
- [ ] **Step 8: Commit flota** (`feat(medico-hospitalista): renombre desde hospitalista (nombres pneuma) + AGENTS.md+SOUL.md v1.3.0 (escalón 8)`).

### Task A6: Escalón 9 — `gtd-integral` → `david-allen` ⚠️HITL íntimo + renombre completo

Mismo procedimiento que Task A5, sustituyendo: `hospitalista`→`gtd-integral`,
`medico-hospitalista`→`david-allen`, URN `urn:fxsl:artefacto:david-allen`.
Atención especial en Step 3: `gtd-integral` apareció en el inventario A0 con
`heartbeat` activo y `tts` configurado — esos bloques se conservan tal cual (solo
cambian los 5 campos de identidad/rutas). En el paso HITL el operador valida
además la frontera detect-not-administer (detecta desregulación, deriva crisis,
no interviene clínicamente) y la continuidad de la memoria GTD.

### Task A7: Gate de cierre de fase

- [ ] **Step 1: Cero duplicados**

```bash
ls ~/openclaw-fleet/workspaces/ | rg "gtd-integral|^hospitalista$|steve-jobs-agentic-designer"
```

Expected: sin matches (exit 1).

- [ ] **Step 2: Salud global + sellos frescos**

```bash
openclaw health                                        # verde
cd ~/kora-pneuma && python3 kora.py velar --estricto   # 13/13 (sello-fresco incluido)
```

- [ ] **Step 3: Repo flota limpio y pusheado según su convención** (`git -C ~/openclaw-fleet status --short` vacío).
- [ ] **Step 4: Handoff al operador**: tabla de los 9 escalones con resultado
  (aplicado/validado-HITL) y cualquier observación de las sondas.

---

## FASE B — Posta OPM: la ley OPM vive siempre en pneuma

Contexto para el ejecutor: pneuma tiene 10 KB OPM en fxsl + 1 skill kora
(verificado contra censo 2026-07-05): `opm-es` v3.0.2,
`manual-metodologico-opm-es` v3.0.1, `metodologia-forja-opm-es` v1.5.1,
`opm-categorial-es` v1.2.5, `reglas-opm-estrictas-es` v1.4.1, `opd-es` v3.0.2,
`opl-es` v3.0.3, `spec-forja-opd-es` v1.1.2, `spec-forja-opl-es` v1.2.2
(todos `urn:fxsl:kb:*`), más `urn:kora:artefacto:modelamiento-opm` v1.10.0.

**Mapeo de nombres bestia→pneuma** (NO es 1:1; establecido en syncs previos y
verificado contra el censo): `reglas-opm-estrictas-es`→igual;
`spec-forja-opd-es`→igual; `spec-forja-opl-es`→igual;
`metodologia-forja-es`→`metodologia-forja-opm-es`;
`metodologia-opm-es`→`manual-metodologico-opm-es`; `opm-iso-19450-es`→`opm-es`;
`opm-visual-es`→`opd-es`; `opm-opl-es`→`opl-es`; `opm-categorial-es`→igual.
**No migrados por decisión previa** (bestia era autoritativa para ellos):
`manual-opforja-es.md`, `manual-opforja-es--p02.md`, `README.md` — la decisión
taxativa de hoy los reabre (ver B1 Step 5).

La bestia **siguió autorando después de la migración** (commits verificados
2026-07-05: `aa2e2f14` docs modelamiento-opm, `fccd1f51` opm-ssot R-INV-2D,
`607b31d4` reglas v1.4.0, `017d…` spec-forja-opd-es v1.0.4) — es al menos el
tercer sync recurrente desde la posta declarada. Consumidores externos apuntando
HOY a rutas de la bestia (verificado): `~/projects/hd-opm/CLAUDE.md:513`,
`~/projects/hodom-opm/CLAUDE.md:58`,
`~/projects/hd-opm/scripts/generar-bundle-hodom.ts:129` (cita
`urn:fxsl:kb:spec-forja-opl-es` v1.2.1 en ruta bestia; pneuma ya va en v1.2.2).

**Fuera de alcance explícito**: la normativa HODOM
(`~/kora/artifacts/knowledge/salud/salubrista/hodom/normativa/`, citada en
`hd-opm/CLAUDE.md:558` y `hodom-opm/CLAUDE.md:57`) es SSOT de dominio salud, no
OPM. **No tocarla ni repuntarla** en esta fase.

### Task B1: Inventario y diff fechado bestia ↔ pneuma

**Files:**
- Read: `~/kora/artifacts/knowledge/fxsl/opm/opm-ssot-es/*.md`
- Read: cláusulas `fuente:` de los 5 KB OPM pneuma + skill

- [ ] **Step 1: Hash actual de cada archivo OPM de la bestia**

```bash
find /home/felix/kora/artifacts/knowledge/fxsl/opm -name "*.md" -exec sh -c 'echo "$(sha256sum "$1" | cut -c1-16)  $1"' _ {} \;
```

- [ ] **Step 2: Hash declarado en la procedencia de cada KB pneuma**

```bash
cd ~/kora-pneuma
for kb in opm-es manual-metodologico-opm-es metodologia-forja-opm-es opm-categorial-es reglas-opm-estrictas-es opd-es opl-es spec-forja-opd-es spec-forja-opl-es; do
  echo "== $kb =="; rg -o "sha256:[a-f0-9]+" "artefactos/conocimiento/fxsl/$kb.md" | tail -1
done
rg -o "sha256:[a-f0-9]+" artefactos/skills/kora/modelamiento-opm/SKILL.md | tail -1
```

(Leer además la cláusula `fuente:` completa de cada uno — confirma el mapeo de
nombres declarado al sublimar y cuál sha256 es el de la última reconciliación.)

- [ ] **Step 3: Deltas post-migración de la bestia, fechados**

```bash
git -C ~/kora log --oneline --since=2026-06-11 -- artifacts/knowledge/fxsl/opm artifacts/skills/kora/modelamiento-opm
```

- [ ] **Step 4: Construir la tabla de reconciliación** con una fila por archivo
  bestia, usando el mapeo de nombres del contexto de esta fase: `archivo bestia |
  sha256 actual | KB pneuma (mapeo) | sha256 declarado | veredicto`. Veredictos:
  - **sin-delta**: hashes coinciden → nada que hacer.
  - **delta-a-absorber**: KB pneuma existe pero la bestia cambió después → Task B2.
  - **no-migrado-por-decisión-previa**: `manual-opforja-es.md`,
    `manual-opforja-es--p02.md`, `README.md` → Step 5.

- [ ] **Step 5 (⚠️HITL): Presentar la tabla al operador.** Para los 3
  no-migrados, la decisión taxativa «la ley OPM vive siempre en pneuma» reabre su
  omisión: proponer **migrar** `manual-opforja-es` (+`--p02`) si algún consumidor
  vivo lo usa como doctrina, u **omitir de nuevo con razón registrada** si es
  manual de herramienta y no ley (el README de la bestia se omite: es orientación
  local de aquel repo). El operador es soberano sobre valor-en-uso; esperar su
  veredicto por fila antes de B3.

### Task B2: Absorber deltas a los KB pneuma existentes

Por cada fila **delta-a-absorber**, uno a uno:

- [ ] **Step 1: Leer el delta real** (`git -C ~/kora show <sha> -- <path>` de cada
  commit posterior a la última reconciliación registrada en `fuente:`).
- [ ] **Step 2: Aplicar el delta byte-fiel** al cuerpo del KB pneuma: las mismas
  hunks del diff, NO copiar el archivo entero (el frontmatter pneuma es propio).
  Verificar con diff cuerpo-a-cuerpo vacío: extraer el cuerpo de ambos (todo
  después del segundo `---`) y compararlos —

```bash
awk 'BEGIN{fm=0} /^---$/{fm++; next} fm>=2' ~/kora/artifacts/knowledge/fxsl/opm/opm-ssot-es/<archivo>.md > /tmp/cuerpo-bestia.md
awk 'BEGIN{fm=0} /^---$/{fm++; next} fm>=2' ~/kora-pneuma/artefactos/conocimiento/fxsl/<kb>.md > /tmp/cuerpo-pneuma.md
diff /tmp/cuerpo-bestia.md /tmp/cuerpo-pneuma.md   # Expected: vacío (o solo diferencias declaradas en fuente:)
```
- [ ] **Step 3: Actualizar `version:`** (bump minor si cambia contenido normativo,
  patch si es corrección) **y la cláusula `fuente:`**: añadir línea de
  reconciliación con fecha ISO, commits bestia absorbidos y el sha256 NUEVO del
  archivo bestia (patrón ya usado en esos mismos KB — leer su `fuente:` como
  plantilla).
- [ ] **Step 4: Gate + commit atómico por KB**

```bash
cd ~/kora-pneuma && python3 kora.py velar --estricto   # 13/13
git add artefactos/conocimiento/fxsl/<kb>.md
git commit -m "kb(<id>): vX.Y.Z — absorbe deltas bestia <shas> (posta OPM: SSOT en pneuma)"
```

### Task B3: Migrar los no-migrados con veredicto «migrar»

Por cada archivo aprobado por el operador en B1 Step 5, patrón de **sublimación**
ya establecido:

- [ ] **Step 1: Crear** `artefactos/conocimiento/fxsl/<id>.md` usando como
  plantilla de frontmatter un hermano OPM existente (p. ej.
  `reglas-opm-estrictas-es.md` — mismos campos, gramática `ley/2`).
- [ ] **Step 2: Cuerpo** vertido desde la bestia; `fuente:` con el patrón:
  `"Sublimada el 2026-07-XX desde la bestia artifacts/knowledge/fxsl/opm/opm-ssot-es/<archivo>.md vX.Y.Z (sha256:<hash completo>); <qué se preservó/omitió con razón>."`
- [ ] **Step 3: Estado inicial** según la cadena de conocimiento (nace `borrador`;
  publicar con `python3 kora.py ciclo urn:fxsl:kb:<id> publicado` tras velar verde).
- [ ] **Step 4: Gate + commit por artefacto** (mismo gate que B2 Step 4).
- Para los veredictos **omitir**: registrar la razón en el mensaje de commit de la
  Task B4 (la cláusula de congelamiento), no crear artefacto.

### Task B4: Congelar la autoría OPM en la bestia

**Files:**
- Modify: `~/kora/CLAUDE.md` (leerlo completo primero — delegation principle)

- [ ] **Step 1: Añadir la cláusula de posta** en la sección de gobernanza/estado
  que el propio archivo tenga (adaptar ubicación a su estructura real):

```markdown
## Posta OPM — cerrada 2026-07-XX

La autoría OPM/Forja en este repo está **CERRADA**. La SSOT de doctrina OPM vive
en `~/kora-pneuma` (urn:fxsl:kb:reglas-opm-estrictas-es, urn:fxsl:kb:opm-es y
hermanos; skill urn:kora:artefacto:modelamiento-opm). Este corpus
(`artifacts/knowledge/fxsl/opm/`, `artifacts/skills/kora/modelamiento-opm/`)
queda congelado como referencia histórica: solo correcciones de verdad, ninguna
doctrina nueva. Todo delta previo al cierre fue reconciliado (ver kora-pneuma,
commits «posta OPM»).
```

- [ ] **Step 2: Commit en la bestia**

```bash
git -C ~/kora add CLAUDE.md
git -C ~/kora commit -m "docs(gobernanza): posta OPM cerrada — SSOT OPM vive en pneuma"
```

### Task B5: Repuntar consumidores externos a pneuma

Regla: cambiar solo punteros **operativos** (instrucciones de leer/consumir);
las citas de procedencia históricas (p. ej. "auditado contra … 2026-06-14") se
actualizan solo si el consumidor re-audita — si no, se anota la nueva ruta al lado,
no se falsifica la historia.

- [ ] **Step 1: `~/projects/hd-opm/CLAUDE.md:513`** — repuntar el corpus OPM de
  `~/kora/artifacts/knowledge/fxsl/opm/opm-ssot-es/` a
  `~/kora-pneuma/artefactos/conocimiento/fxsl/` (URNs OPM pneuma). NO tocar la
  línea 558 (normativa HODOM, fuera de alcance).
- [ ] **Step 2: `~/projects/hodom-opm/CLAUDE.md:58`** — ídem. NO tocar línea 57.
- [ ] **Step 3: `~/projects/hd-opm/scripts/generar-bundle-hodom.ts:129`** — leer
  primero `hd-opm/CLAUDE.md` para entender el ciclo del bundle; actualizar la ruta
  y, si `spec-forja-opl-es` fue migrada (B3), el URN ya resuelve en pneuma. Si el
  repo manda regenerar el bundle tras cambiar la cita, hacerlo según su runbook;
  si no lo manda, no regenerar.
- [ ] **Step 4: Barrido exhaustivo de residuos**

```bash
rg -ln "opm-ssot-es|artifacts/knowledge/fxsl/opm" ~/projects ~/.claude ~/openclaw-fleet ~/KORVONESTO 2>/dev/null
```

Leer CADA match y repuntar solo los operativos OPM (criterio de la regla de arriba).

- [ ] **Step 5: Commit por repo consumidor** (`docs(opm): repuntar SSOT OPM a kora-pneuma (posta OPM)` en cada repo tocado, por separado).

### Task B6: Gate de cierre de fase

- [ ] **Step 1: Gates pneuma**

```bash
cd ~/kora-pneuma
python3 kora.py velar --estricto           # 13/13
python3 -m unittest discover -s tests      # 93 OK
```

- [ ] **Step 2: Cero punteros operativos residuales** (re-correr el barrido B5
  Step 4; los únicos matches admisibles son cláusulas de procedencia histórica y
  la propia bestia).
- [ ] **Step 3: Handoff al operador**: tabla de reconciliación final (qué se
  absorbió, qué se migró, qué se omitió y por qué), commits por repo, y
  recordatorio de actualizar las memorias del agente (`posta-opm-no-operativa` →
  cerrada; `deploy-fleet-vivo-riesgos` → ejecutado, si la Fase A ya corrió).

---

## Cierre del plan (tras completar las tres fases)

- [ ] Este plan es un doc operativo: al quedar ejecutado, desplazarlo a
  `_archivo/planes/` (mismo patrón que Fase C) y commit
  `docs(vigencia): archivar plan tres-frentes ejecutado`.
