# Handoff vigente — 2026-07-16

> Memoria operativa auxiliar. No legisla ni sustituye `ALMA.md`, `ley/`, los
> frontmatters canónicos, git o GitHub. Verificar siempre el estado vivo antes
> de actuar. El handoff anterior quedó en
> `_archivo/HANDOFF-2026-07-15-hsc-agent-cli-beta3.md`.

## Resultado de la sesión

- El destino de `forjador-openclaw` se cerró como **OMITIR/DESCARTAR**, no
  migrar. No se creó `urn:dev:artefacto:forjador-openclaw` en Pneuma.
- `transmute-openclaw` tampoco se migra: la transmutación OpenClaw vigente está
  mecanizada por `kora.py transmutar` bajo `ley/3`.
- La ruta operativa única queda:
  **agente capaz → `urn:kora:kb:deploy-flota-openclaw` → `kora.py` → contrato
  local de `~/openclaw-fleet/`**.
- Se retiraron las materializaciones activas obsoletas, preservando la fuente y
  los builds de la bestia como respaldo histórico reversible.

## Estado verificable al cierre

### KORA Pneuma

- No se modificaron artefactos, ley ni `kora.py`; el único cambio de este repo
  es la memoria operativa vigente.
- `python3 kora.py velar --estricto`: 13 checks coherentes.
- `python3 -m unittest discover -s tests`: 120 tests verdes.
- `urn:kora:kb:deploy-flota-openclaw` resuelve a
  `artefactos/conocimiento/kora/deploy-flota-openclaw.md` v1.0.0.
- `urn:dev:artefacto:forjador-openclaw` no resuelve en el censo **por diseño**:
  nunca ingresó al corpus vigente.
- Los informes no versionados
  `informe-desempeno-medico-hospitalista-2026-07-11.md` e
  `informe-turno-urgenciologo-2026-07-10.md` pertenecen al operador y quedaron
  fuera de staging y commits.

### Flota OpenClaw

- Commit `8b499602586ab211678cb0ecbe027eb87bdf6341` en `main`, pusheado a
  `origin/main`: `refactor(fleet): retirar forjador OpenClaw legado`.
- Se retiró el blueprint inactivo
  `~/openclaw-fleet/workspaces/forjador-openclaw/`.
- Se retiró la skill legacy
  `~/openclaw-fleet/workspaces/main/skills/transmute-openclaw/`.
- `~/openclaw-fleet/CLAUDE.md` apunta al runbook canónico y ya no enumera el
  blueprint retirado; la flota conserva 17 workspaces versionados.
- La referencia operativa a `forjador-openclaw` se eliminó de
  `workspaces/main/skills/hermes-agent-specialist/SKILL.md`; la mención de la
  memoria histórica del 2026-04-19 se preservó como historia, no autoridad.
- `scripts/check-symlinks.sh`: verde.
- `scripts/diff-reference.sh`: config viva y reference coinciden.
- `openclaw health`: gateway/event loop y agentes operativos. Persiste una
  advertencia previa por entradas antiguas en dead-letter; no nació de este
  cambio y quedó fuera de alcance.
- El worktree conserva cambios ajenos en memorias y agentes clínicos; el commit
  stageó exclusivamente las rutas del retiro.

### Materializaciones Codex

- Ya no existen como skills activas:
  `~/.codex/skills/forjador-openclaw/` ni
  `~/.codex/skills/transmute-openclaw/`.
- Se archivaron reversiblemente en:
  - `~/_archive/forjador-openclaw-codex-emision-2026-07-16/`
  - `~/_archive/transmute-openclaw-codex-emision-2026-07-16/`
- Hashes preservados:
  - forjador `SKILL.md`:
    `d71931a6f140888f4bc1e94c7aaf712802d5e67cc364f1caab3fbfb224868634`
  - forjador `agents/openai.yaml`:
    `3e4e3e06e8242d7eaf892fb03d88d4aa90d1858e8440789e465ef8410a3be536`
  - transmutador `SKILL.md`:
    `18b5d67813ce3bdb85af642e47cf215d475bf1ccec19593e8ed06f75e115831f`
- `~/.claude/agent-memory/forjador-openclaw/` permanece intacto: no participa
  en resolución ni instalación y su eventual archivo exige una decisión
  separada.

## Decisiones tomadas

1. **La cobertura funcional prevalece sobre el packaging.** Tres contrastes
   independientes verificaron que autoría, transmutación, paridad, deploy,
   HITL, anti-despotenciación y operación de flota ya tienen dueño vigente.
   Un nuevo agente solo agregaría un trigger de enrutamiento.
2. **OMITIR es un resultado KORA legítimo.** `migrar-o-omitir` no obliga a
   importar un URN bestia sin valor diferencial; la dignidad del URN aplica a
   los artefactos que sí entraron al corpus Pneuma.
3. **No se fabrica un tombstone.** Crear un artefacto retirado únicamente para
   registrar que no se migró duplicaría historia sin aportar resolución.
4. **La fuente histórica no se toca.** Permanecen intactos
   `~/kora/artifacts/agents/dev/forjador-openclaw/AGENT.md`,
   `~/kora/artifacts/skills/kora/transmute-openclaw/SKILL.md` y sus `_BUILD/`.
   Se retiraron solo materializaciones descubribles y blueprints inactivos.
5. **`targets` nombra dónde corre un artefacto, no qué runtime administra.**
   Gestionar OpenClaw no justifica por sí solo que el gestor sea target
   `openclaw` ni que exista como workspace de la flota.
6. **No se expandió el alcance.** La memoria Claude residual y la cola
   dead-letter quedaron como observaciones explícitas, no como limpieza
   oportunista.

## Aprendizajes destilados

1. **Instalado no significa vigente.** Antes de invocar una skill, verificar
   procedencia, sello, fecha, URN resoluble y alineación con el canon actual.
2. **`velar` prueba forma, no valor.** Un artefacto puede pasar todos los checks
   y seguir siendo redundante; la decisión de destino exige mapa de cobertura y
   refutación adversarial.
3. **La solución más KORA puede ser no crear.** Si mecanismo + conocimiento +
   gobernanza absorben completamente una función, un wrapper nuevo reintroduce
   duplicación ontológica.
4. **Migrar conserva sustancia, no nostalgia.** Preservar el URN no obliga a
   preservar un rol cuya conducta diferencial desapareció.
5. **Retiro seguro separa fuente de materialización.** Conservar la fuente
   congelada y el historial Git permite retirar instalaciones activas sin
   pérdida histórica ni irreversibilidad.
6. **Cerrar todas las superficies de descubrimiento.** Retirar una skill exige
   revisar instalación global, skills embebidas, blueprints, inventarios y
   referencias vivas; dejar una sola puede reactivar el encuadre obsoleto.
7. **Una recomendación única mejora el diseño.** Al forzar una sola solución,
   la comparación migrar-vs-omitir reveló que el agente ligero era conveniencia
   de packaging, no una entidad con identidad propia.

## Artefactos relevantes

- Canon de régimen:
  `artefactos/conocimiento/kora/regimen-de-ley.md`.
- Ley de transmutación vigente: `ley/3-transmutacion.md`.
- Runbook único:
  `artefactos/conocimiento/kora/deploy-flota-openclaw.md`.
- Autoría ya cubierta:
  `artefactos/agentes/dev/agent-architect.md`.
- Gobernanza de flota: `~/openclaw-fleet/CLAUDE.md` y
  `~/openclaw-fleet/docs/fleet-canon-policy.md`.
- Fuente histórica del forjador:
  `~/kora/artifacts/agents/dev/forjador-openclaw/AGENT.md`.
- Evidencia versionada del retiro: commit fleet `8b49960`.

## Cómo retomar

1. Leer `CLAUDE.md` y este handoff; ante divergencia manda el canon y el estado
   vivo.
2. Ejecutar `git status -sb` y preservar los dos informes del operador.
3. Para un deploy KORA→OpenClaw, resolver y seguir
   `urn:kora:kb:deploy-flota-openclaw`; no reinstalar las skills legacy.
4. No reconsiderar la migración de `forjador-openclaw` salvo que aparezca una
   conducta irreducible no cubierta por `agent-architect`, `kora.py`, el runbook
   o `openclaw-fleet/CLAUDE.md`.
5. Si reaparece alguno de los dos nombres bajo una superficie activa, comparar
   su hash y retirarlo; los archivos en `~/_archive/` son respaldo, no fuente.
6. Tratar la advertencia dead-letter como tarea independiente si el operador la
   prioriza; no mezclarla con lifecycle KORA.
7. Antes de cerrar cambios KORA, ejecutar:

   ```bash
   python3 kora.py velar --estricto
   python3 -m unittest discover -s tests
   ```
