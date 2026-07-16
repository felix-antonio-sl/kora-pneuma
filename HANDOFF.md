# Handoff vigente — 2026-07-16 — Clawforge 1.1.0

> Memoria operativa auxiliar. No legisla ni sustituye `ALMA.md`, `ley/`, los
> frontmatters canónicos, Git ni el estado vivo de OpenClaw. Conserva el cierre
> de la migración iniciada en `_archivo/HANDOFF-2026-07-16-forjador-openclaw.md`.

## Resultado

- `urn:ops:artefacto:clawforge` permanece como fuente KORA del agente runtime
  `main`; la identidad visible sigue siendo Clawforge y no hubo migración de id,
  workspace, estado ni canal.
- La fuente subió a v1.1.0 y declara la allowlist OpenClaw exacta. El runtime la
  realiza con perfil `full` cerrado por esa lista y `exec.mode: auto` (Guardian),
  manteniendo `elevated` como break-glass del owner.
- OpenClaw recibe ahora `AGENTS.md` operativo sin duplicar la voz y `SOUL.md`
  con el único span `U_phen`. Los demás targets conservan el cuerpo completo.
- El sello ya no inventa paths desde el id de la URN: declara resolución por el
  censo (`kora.py nombre`) o por coincidencia exacta y única de frontmatter; el
  consumidor ejecuta ese contrato.
- Cada sello OpenClaw porta la frontera declarada y confiesa que su realización
  vive en `openclaw.json` y no queda probada por la paridad de archivos.
- `operator`, `troubleshooter` y `version-manager` fueron retiradas del
  workspace. Esas tres y `openclaw-lifecycle-manager` tienen tombstone
  `skills.entries.<name>.enabled=false`, por lo que una copia reinstalada no
  vuelve silenciosamente al prompt.
- La emisión Codex `kora-agentic-lifecycle` también fue retirada: Pneuma ya la
  había dictaminado DESCARTAR (F1/C1/V1) por duplicar `ley/0..4 + kora.py` y
  conservar rutas/comandos de la bestia. No se creó una fuente sustituta.
- No se envió ningún mensaje externo ni se reinició el gateway.

## Correcciones adjudicadas

| Hallazgo | Corrección |
|---|---|
| `urn:ops:artefacto:clawforge` usa `nombre: main`; el sello derivaba el path inexistente `ops/clawforge.md` | Resolución por censo, con prueba URN id ≠ `nombre`. |
| La voz aparecía en `AGENTS.md` y `SOUL.md` | Partición nativa: operativa en AGENTS, voz en SOUL. |
| La frontera `herramientas` no viajaba en el proof-carrier | Dos líneas nuevas distinguen declaración y realización de deploy. |
| `main` declaraba tools filtradas por el perfil global `coding` | Perfil per-agent `full` + allowlist exacta; 19 tools en la frontera owner. |
| `exec` efectivo era `full/off` | `auto` produce `allowlist/on-miss` y Guardian; elevated queda explícito como break-glass. |
| `TOOLS.md` describía ACP obligatorio, rutas falsas y gateway/systemd obsoletos | Scaffolding reescrito contra el host y runtime instalados. |
| Tres wrappers operativos repetían comandos volátiles e inexistentes | Retiro físico, reparación de su único consumidor y tombstones globales por nombre. |
| El retiro de `openclaw-lifecycle-manager` no sobrevivía a una reinstalación o rollback parcial de ClawHub | Tombstone durable; el rollback completo exige quitarlo y restaurar provenance revisada. |
| Codex aún exponía `kora-agentic-lifecycle`, descartada por la auditoría Pneuma | Retiro de la emisión runtime; el ciclo vigente es ley + `kora.py`, sin segunda skill coordinadora. |

No se añadió `reemplaza` a la nueva URN: el Clawforge histórico de la bestia fue
retirado sin sucesor jurídico; la fuente vigente reconstruye el agente runtime
vivo y conserva esa procedencia en `fuente`.

## Decisiones vigentes

1. **URN y nombre son tipos distintos.** La URN identifica; `nombre` fija el
   path y la clave de emisión. Un consumidor resuelve por censo, no por fórmula.
2. **El workspace OpenClaw es un producto.** La materia completa se conserva en
   `AGENTS.md × SOUL.md`; no hace falta duplicar `U_phen` para ser fiel.
3. **Proof-carrying no equivale a enforcement.** El sello transporta la
   allowlist; config viva, sender y runtime deciden la disponibilidad efectiva.
4. **La frontera declarada es máxima, no universal.** `gateway`, `cron` y
   `nodes` son además owner-only. La CLI local/token compartido parte como owner;
   sólo una identidad explícita no-owner debe perderlas.
5. **Mutación por superficie nativa.** `gateway` 2026.7.1 admite lectura y una
   lista estrecha de mutaciones tipadas, pero no `tools.*`; este hardening se
   hizo por CLI oficial con dry-run y backup.
6. **Menos capas, más gobierno.** Clawforge + KORA + `CLAUDE.md` + docs oficiales
   cubren operación y upgrades sin tres skills que congelaban comandos.
7. **No ampliar por conveniencia.** `codexDynamicToolsLoading` permanece global
   en `searchable`; no se cambió a `direct` para toda la flota solo para facilitar
   un canario local.

## Estado verificable

### KORA-Pneuma

- Fuente: `artefactos/agentes/ops/main.md`, v1.1.0,
  `urn:ops:artefacto:clawforge`.
- Ley/toolchain: `6939a0b` (`fix(kora): corregir proyeccion OpenClaw`).
- Fuente Clawforge: `d2c115f` (`feat(ops): endurecer frontera de Clawforge`).
- `python3 kora.py velar --estricto`: 13 checks verdes.
- `python3 -m unittest discover -s tests`: 123 tests verdes.
- Paridad Clawforge: 1 fiel, 0 desviadas, 0 no instaladas, 0 sin emisión.
- El commit concurrente `f8a79f6` de Salud y los dos informes no versionados
  de ese dominio son ajenos a este cierre.

### OpenClaw-Fleet

- Deploy derivado: `a9864b1` (`refactor(main): desplegar Clawforge 1.1.0`).
- Frontera runtime y tombstones: `a0ff96f`
  (`fix(main): cerrar frontera runtime de Clawforge`).
- Retiro de wrappers: `bf8ac51`
  (`refactor(main): retirar wrappers operativos obsoletos`).
- Config viva válida y sin drift contra `openclaw.json.reference`.
- Backup previo verificado, modo 0600:
  `/var/backups/openclaw-felix/2026-07-16T04-26-38.642+02-00-openclaw-backup.tar.gz`,
  SHA-256 `ddade05fb5bc06f3ab7aee3a127db787f4c07f21a68185790d681e67f66d3cb9`.
- Política efectiva de `main`: `auto`, security `allowlist`, ask `on-miss`.
- La sesión Telegram owner reporta exactamente las 19 herramientas declaradas
  en `tools.effective`. No se produjo un turno Telegram ni entrega externa.
- Canario CLI fresco: cargó identidad Clawforge, principio de voz y workspace,
  y ejecutó `pwd` bajo Guardian. Otro canario observó un filtro owner-only, pero
  no conservó provenance suficiente del sender y no prueba que la CLI local sea
  no-owner.
- `skills check --agent main`: los cuatro nombres retirados están ausentes de
  model-visible.

## Aprendizajes destilados

1. **Una fórmula elegante pero falsa es peor que una búsqueda explícita.** El
   censo ya era la autoridad; el sello debía señalarlo, no duplicar un esquema.
2. **Fidelidad no exige repetición textual.** En un target producto, distribuir
   por rol nativo preserva más semántica que copiar todo a cada componente.
3. **Paridad de bytes, política efectiva y sender son gates distintas.** Las
   tres deben nombrarse por separado para no confundir presencia con permiso.
4. **El binario instalado arbitra contradicciones documentales de su versión.**
   La guía de seguridad llama read-only a `gateway`, mientras 2026.7.1 registra
   mutaciones fail-closed; el hardening usó el schema/código efectivo y evitó
   atribuirle cambios de `tools.*` que no admite.
5. **Un tombstone convierte un retiro local en una decisión reproducible.** Git
   conserva bytes; config impide reactivación silenciosa; provenance sigue
   siendo un problema separado.
6. **Un filtro sin provenance del sender no es una gate.** Un canario negativo
   debe entrar con identidad no-owner explícita; la CLI local es owner por
   defecto.
7. **La memoria auxiliar también puede sobreafirmar.** La coordinación previa
   confirmó ausencia de dependencia para `forjador-openclaw` y
   `transmute-openclaw`; para `openclaw-lifecycle-manager` solo hubo acuse y
   respeto de paths. Este handoff ya no generaliza esa confirmación.
8. **Una skill instalada no recupera autoridad por estar disponible.** Si el
   censo Pneuma ya la descartó y su mecánica está legislada, se retira la
   emisión obsoleta en vez de modernizar una capa redundante.

## Deuda residual

- Active Memory agotó su ventana de 30 s en los dos canarios de `main` y omitió
  recall; ambos turnos principales terminaron. Diagnosticarlo corresponde a la
  gobernanza del plugin/memoria, no a la transmutación Clawforge.
- La prueba de tool control-plane fue read-only: `tools.effective` sobre la
  sesión Telegram owner. Falta tanto la invocación owner como un negativo con
  identidad no-owner explícita; no se generaron turnos de canal.
- Los warnings y deuda generales de la flota (backup full-state, dead-letter,
  paridad global y material legacy) permanecen bajo el handoff del fleet.

## Artefactos relevantes

- Fuente: `artefactos/agentes/ops/main.md`.
- Ley: `ley/3-transmutacion.md`.
- Régimen: `artefactos/conocimiento/kora/regimen-de-ley.md`.
- Runbook: `artefactos/conocimiento/kora/deploy-flota-openclaw.md`.
- Derivados: `~/openclaw-fleet/workspaces/main/AGENTS.md` y `SOUL.md`.
- Scaffolding: `~/openclaw-fleet/workspaces/main/TOOLS.md`.
- Runtime versionado: `~/openclaw-fleet/openclaw.json.reference`.
- Handoff fleet vigente: `~/openclaw-fleet/docs/handoffs/handoff-2026-07-16-3.md`.

## Cómo retomar

1. Leer `CLAUDE.md`, este handoff y el estado Git vivo de ambos repos.
2. Cambiar conducta en Pneuma, ejecutar gates, transmutar, revisar el diff,
   aplicar y validar en sesión fresca.
3. Contrastar `frontera-herramientas-declarada` con config viva y con el sender
   del canario; paridad no realiza ese contrato.
4. No reactivar `forjador-openclaw`, `transmute-openclaw`,
   `openclaw-lifecycle-manager`, `operator`, `troubleshooter` ni
   `version-manager` sin una nueva auditoría de uso y provenance.
5. No reinstalar `kora-agentic-lifecycle`; usar `kora.py ciclo`, `transmutar`,
   `velar` y `censo` bajo la ley vigente.
6. Diagnosticar Active Memory por separado si vuelve a agotar la ventana.

## Rollback

- Ley/toolchain KORA: `git revert 6939a0b` solo después de adjudicar emisiones
  producidas con v2.2.0.
- Fuente KORA: `git revert d2c115f` y retransmutar.
- Fleet: revertir en orden `bf8ac51`, `a0ff96f`, `a9864b1` según la superficie
  que se quiera deshacer; no usar `reset --hard`.
- Config viva: aplicar por CLI el inverso versionado, validar y sincronizar el
  reference. Restaurar `security: full/ask: off` elimina Guardian y requiere una
  decisión explícita, no es un rollback inocuo.
- Skills: revertir archivos no quita tombstones. Para reactivar una, retirar
  también su entrada `skills.entries`; para `openclaw-lifecycle-manager`, una
  recuperación completa requiere reinstalación owner-qualified/version-pinned
  tras revisar provenance, no solo `git revert df391f8`.
