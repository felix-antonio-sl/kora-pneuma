# Handoff vigente — 2026-07-17 — cierre del ciclo Codex

> Memoria operativa auxiliar. No legisla ni sustituye `ALMA.md`, `ley/`, los
> frontmatters canónicos, Git ni el estado vivo de los runtimes. El informe
> exhaustivo de la transición quedó archivado en
> `_archivo/HANDOFF-2026-07-16-transicion-claude-code-a-codex.md`.

## Estado al cierre

El ciclo de revisión y transición **Claude Code → Codex** queda cerrado en
`master`. No se identificó trabajo técnico adicional que justificara modificar
el corpus después de `ab00f6f`; este cierre solo destila memoria y vuelve a
probar el estado publicado.

- `HEAD` y `origin/master` coincidían en `ab00f6f` antes de este commit de
  memoria.
- Los informes operativos fechados quedaron fuera del corpus vivo y fueron
  desplazados posteriormente a `_archivo/`, conforme a la política documental.
- No se mutaron runtimes ni configuración en este cierre documental.

## Valor entregado durante la sesión

1. **Valor legacy absorbido antes de sobrescribir.** El contenido único de
   `consenso-deliberativo` pasó a la fuente Pneuma; se corrigieron referencias
   activas a `kora-agents`, `custodio-kora` y `claude-md-management`.
2. **Frescura real de la transmutación.** `sello-fresco` pasó de comprobar solo
   `hash-fuente` a verificar fuente → generador → producto completo, incluidos
   sidecars y `referencias/`.
3. **Completitud y tipos honestos.** Se rechazan targets no declarados/no
   realizados, unidades sin archivo raíz y factores residuales. La pérdida
   Codex de `herramientas` se declara como fidelidad parcial no reticular.
4. **Reconciliación.** Se reemitieron las 119 parejas realizadas y se aplicaron
   114 parejas desviadas. El corte final conserva 125 unidades fieles, ninguna
   desviada y ninguna sin emisión.
5. **Superficie Codex saneada.** En `/home/felix/.codex/config.toml` quedó
   `default_permissions = ":workspace"` sin el `sandbox_mode` incompatible; 12
   artefactos legacy/absorbidos quedaron deshabilitados mediante tombstones.
   `gpt-5.6-sol` y esfuerzo `max` se preservaron como decisión explícita del
   operador.
6. **Frontera Codex/OpenClaw visible.** KORA impide instalar una skill managed
   OpenClaw debajo del homónimo personal directo en `~/.agents/skills`, pero no
   finge resolver discovery agrupado, workspaces o config efectiva.

## Decisiones vigentes

1. **Pneuma es la SSOT.** La bestia `~/kora` solo aporta material a migrar o
   descartar; no recibe desarrollo nuevo.
2. **Un producto derivado no se valida contra sí mismo.** Emisión e instalación
   pueden coincidir y estar ambas obsoletas; el generador vigente forma parte
   obligatoria de la prueba.
3. **Fidelidad de ejes y fidelidad de campos son regímenes distintos.** Una
   limitación de tools no inventa un séptimo eje ni se traduce a un codominio de
   otro tipo.
4. **Paridad de bytes no es efectividad runtime.** Discovery, registro de
   agentes, sender, tool policy, gateway y systemd requieren gates separadas.
5. **No instalar debajo de una sombra conocida.** Presencia en una ruta managed
   no equivale a realización si una raíz de mayor precedencia gana.
6. **Tombstone antes que borrado silencioso.** Deshabilitar conserva
   reversibilidad y evita reactivaciones por rollback o reinstalación.
7. **No cambiar modelo por intuición.** La eficiencia de `medium` frente a
   `max` debe decidirse con evals representativos, no con preferencia general.

## Aprendizajes destilados

### 1. La frescura es un diagrama, no un hash

El hash de la fuente solo prueba identidad de entrada. La garantía útil exige:

`fuente actual → generador vigente → producto completo → instalación`.

`velar` gobierna los tres primeros términos; paridad gobierna el último. Una
gate no sustituye a la otra.

### 2. Sidecars y referencias también son producto

Un archivo sin sello puede cambiar conducta. Si el emisor crea
`agents/openai.yaml` o copia `referencias/`, sus paths y bytes pertenecen al
contrato verificable aunque no repitan el proof-carrier.

### 3. La migración correcta empieza por el valor, no por los archivos

Antes de reaplicar 122 unidades desviadas se auditó si el runtime conservaba
conocimiento único. Trece desviaciones eran versiones antiguas; una contenía
valor real. Migrarlo primero evitó que una sincronización técnicamente correcta
destruyera capacidad.

### 4. Los estándares compartidos crean acoplamiento entre runtimes

`~/.agents/skills` es raíz personal tanto para Codex como para OpenClaw. Esa
interoperabilidad también hace porosa la frontera de targets. La solución no es
suponer aislamiento, sino gobernar precedencia y visibilidad por runtime.

### 5. “Read-only” debe verificarse contra el comportamiento del CLI

Una consulta OpenClaw con el flag incorrecto activó una auto-migración de
estado. Se restauró byte-idéntico el archivo original y se conservó evidencia.
Lección operativa: para CLIs con migraciones automáticas, inspección estática,
dry-run, backup y sintaxis exacta preceden incluso a comandos nominalmente de
lectura.

### 6. Un gate debe poder materializar su propia recomendación

Detectar `referencias/` obsoletas y recomendar “re-transmutar” era insuficiente
si el gesto no eliminaba la fibra retirada. Toda recomendación automática debe
cerrar el loop o declarar la intervención manual necesaria.

### 7. La honestidad del alcance es una propiedad de calidad

Este ciclo cierra Codex y el núcleo Pneuma. No cierra la configuración efectiva
de OpenClaw ni realiza T-Hermes. Nombrar esa frontera evita convertir métricas
verdes en afirmaciones falsas.

## Artefactos y commits relevantes

- `37e1f01` — `fix(artefactos): absorber valor legado para Codex`.
- `83a15f0` — `fix(kora): probar congruencia del producto emitido`.
- `ab00f6f` — `docs(kora): memorizar transición a Codex`.
- Núcleo: `kora.py`.
- Ley afectada: `ley/0-constitucion.md` y `ley/3-transmutacion.md`.
- Guía: `artefactos/conocimiento/kora/guia-rapida-pneuma.md`.
- Valor migrado:
  `artefactos/skills/kora/consenso-deliberativo/{SKILL.md,referencias/}`.
- Config externa: `/home/felix/.codex/config.toml`.
- Evidencia del incidente ya corregido:
  `/home/felix/.codex/backups/kora-pneuma-2026-07-16-openclaw-profile-audit/`.

## Verificación repetida el 2026-07-17

- `python3 kora.py velar --estricto`: **13/13**.
- `python3 -m unittest discover -s tests`: **134/134**.
- `python3 kora.py transmutar --paridad`:
  **125 fieles · 0 desviadas · 2 no instaladas · 0 sin emisión**.
- `codex doctor --summary`: **17 correctos · 0 fallos**; persiste únicamente la
  advertencia ambiental previa sobre rollout files ausentes de la base de
  tasks.

## Deuda residual y siguiente orden

### P1 — OpenClaw

- `autoria-de-persona` y `consenso-deliberativo` carecen de instalación managed
  target-correcta; los homónimos de mayor precedencia siguen ganando.
- `main/consenso` conserva una copia workspace legacy con URNs antiguos.
- `agent-architect` y `steve-jobs` tienen workspaces fieles, pero no están
  registrados en `agents.list[]`.
- Las tool policies vivas no realizan necesariamente la allowlist KORA exacta.

Orden recomendado: auditar discovery efectivo por agente → adjudicar la raíz
personal compartida → registrar solo agentes desplegables → contrastar tools y
config viva → recién entonces aplicar/canariar.

### P1 — Hermes

T-Hermes sigue reconocido y no realizado. Los tres bridges clínicos externos
de hospitalista/urgencia son valor vivo sin backup completo verificado; dos
conservan `clinical_warning` ya retirado y los perfiles usan `SOUL.md` genérico.
Veredicto vigente: **CONSERVAR-EXTERNO**, respaldar y auditar antes de transmutar.

### P2 — eficiencia Codex

Medir en tareas nuevas: costo de descripciones, precisión de discovery,
`medium` frente a `max`, defaults read-only para agentes sanitarios y la
duplicación dual-mode de `dov-dori`. Cambios separados, con evals.

## Cómo retomar

1. Leer `CLAUDE.md`, este handoff y el estado Git vivo.
2. Abrir una tarea Codex nueva o reiniciar la app para asegurar que el catálogo
   use los tombstones configurados.
3. Repetir 13/13, 134/134 y paridad antes de tocar ley, generador o artefactos
   agénticos.
4. Tratar OpenClaw y Hermes como frentes separados; no ampliar el alcance del
   cierre Codex por conveniencia.

## Rollback

- Memoria: revertir solo el commit documental de este cierre restaura el
  handoff exhaustivo anterior desde Git; el archivo también queda en `_archivo/`.
- Núcleo/ley: `git revert 83a15f0` y adjudicar después todas las emisiones
  creadas bajo ley/3 v2.3.0.
- Artefactos: `git revert 37e1f01` solo tras preservar el valor rico de
  `consenso-deliberativo`.
- Config Codex: reactivar una skill exige retirar/cambiar su tombstone y
  reiniciar. No reintroducir `sandbox_mode="danger-full-access"` como rollback
  rutinario: volvería a anular el perfil moderno de permisos.
