# Handoff vigente — 2026-07-18 — cierre Codex y mantenimiento KORA

> Memoria operativa auxiliar. No legisla ni sustituye `ALMA.md`, `ley/`, los
> frontmatters canónicos, Git ni el estado vivo de los runtimes. El informe
> exhaustivo de la transición quedó archivado en
> `_archivo/HANDOFF-2026-07-16-transicion-claude-code-a-codex.md`.

## Estado al cierre

El ciclo de revisión y transición **Claude Code → Codex** permanece cerrado en
`master`. El mantenimiento posterior fortaleció la paridad de las superficies
gestionadas y separó nombre de propiedad sin reabrir esa migración.

- La paridad exacta vigente se define en `ley/3-transmutacion.md` y `kora.py`;
  su historia se consulta en Git cuando sea necesaria.
- Los informes operativos fechados quedaron fuera del corpus vivo y fueron
  desplazados posteriormente a `_archivo/`, conforme a la política documental.
- La única reconciliación externa de este mantenimiento reconstruyó la skill
  Claude Code `cat-thinking` y retiró un duplicado byte-idéntico sin valor único.
- Hermes queda congelado: no se modificaron su canon, emisiones ni
  instalaciones.

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
4. **Reconciliación y paridad exacta.** Toda ruta gestionada se reconcilia
   después de demostrar su propiedad por sello: un homónimo ajeno se preserva
   y bloquea en vez de ser reemplazado. Las skills son directorios cerrados;
   factores sobrantes, emisiones ambiguas, residuos atribuibles y nodos
   incompatibles —también en ancestros— son drift. El barrido residual cubre
   formas históricas del mismo URN sin obligar despliegues ausentes. Los
   blueprints OpenClaw aplicados permanecen abiertos: un contenedor vacío no
   cuenta como instalación y KORA solo gobierna los nombres emitidos y sus
   residuos atribuibles. El workspace runtime privado queda fuera y lo
   materializa el deploy fleet. El estado vigente se consulta bajo demanda.
5. **Superficie Codex saneada.** En `/home/felix/.codex/config.toml` quedó
   `default_permissions = ":workspace"` sin el `sandbox_mode` incompatible;
   los artefactos legacy/absorbidos identificados quedaron deshabilitados
   mediante tombstones.
   `gpt-5.6-sol` y esfuerzo `xhigh` se preservaron como decisión explícita del
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
8. **Nombre no equivale a propiedad.** El slug selecciona una ruta candidata;
   solo el sello `(URN,target)` autoriza reconciliación destructiva. La ausencia
   en otro runtime sigue siendo informativa: emitir capacidad no obliga a
   desplegarla en todos los targets.

## Aprendizajes destilados

### 1. La frescura es un diagrama, no un hash

El hash de la fuente solo prueba identidad de entrada. La garantía útil exige:

`fuente actual → generador vigente → producto completo → instalación`.

`velar` gobierna los tres primeros términos; paridad gobierna el último. Una
gate no sustituye a la otra ni se ejecuta implícitamente dentro de
`--aplicar`.

### 2. Sidecars y referencias también son producto

Un archivo sin sello puede cambiar conducta. Si el emisor crea
`agents/openai.yaml` o copia `referencias/`, sus paths y bytes pertenecen al
contrato verificable aunque no repitan el proof-carrier.

### 3. La migración correcta empieza por el valor, no por los archivos

Antes de reconciliar las instalaciones se auditó si el runtime conservaba
conocimiento único. `consenso-deliberativo` sí lo contenía; migrarlo primero
evitó que una sincronización técnicamente correcta destruyera capacidad.

### 4. Los estándares compartidos crean acoplamiento entre runtimes

`~/.agents/skills` es raíz personal tanto para Codex como para OpenClaw. Esa
interoperabilidad también hace porosa la frontera de targets. La solución no es
suponer aislamiento, sino gobernar precedencia y visibilidad por runtime.

### 5. “Read-only” debe verificarse contra el comportamiento del CLI

Una consulta OpenClaw con el flag incorrecto activó una auto-migración de
estado. La sesión registró una restauración byte-idéntica y preservó una copia
del archivo auto-migrado; esta revisión confirmó la evidencia, pero el estado
actual no basta para volver a demostrar aquella identidad histórica. Lección
operativa: para CLIs con migraciones automáticas, inspección estática, dry-run,
backup y sintaxis exacta preceden incluso a comandos nominalmente de lectura.

### 6. Un gate debe poder materializar su propia recomendación

Detectar `referencias/` obsoletas y recomendar “re-transmutar” era insuficiente
si el gesto no eliminaba la fibra retirada. Toda recomendación automática debe
cerrar el loop o declarar la intervención manual necesaria.

### 7. La honestidad del alcance es una propiedad de calidad

Este ciclo cierra Codex y el núcleo Pneuma. No cierra la configuración efectiva
de OpenClaw. Hermes queda fuera del alcance operativo hasta una decisión
explícita posterior. Nombrar esas fronteras evita convertir gates verdes en
afirmaciones falsas.

## Superficies canónicas y trazabilidad bajo demanda

- Núcleo y contrato: `kora.py`, `ley/0-constitucion.md`,
  `ley/2-forma.md` y `ley/3-transmutacion.md`.
- Guía: `artefactos/conocimiento/kora/guia-rapida-pneuma.md`.
- Valor migrado:
  `artefactos/skills/kora/consenso-deliberativo/{SKILL.md,referencias/}`.
- Config externa: `/home/felix/.codex/config.toml`.
- Evidencia preservada:
  `/home/felix/.codex/backups/kora-pneuma-2026-07-16-openclaw-profile-audit/`.

Usar `git log --oneline -- <ruta>` y `git show <commit> -- <ruta>` para
reconstruir historia o autoría; no mantener catálogos de commits en esta
memoria viva.

## Verificación del cierre — 2026-07-18

Al cerrar se ejecutaron:

- `python3 kora.py velar --estricto`
- `python3 -m unittest discover -s tests`
- `python3 kora.py transmutar --paridad`
- `codex doctor --summary`

Los gates del repositorio quedaron verdes, la paridad no presentó bloqueos y
Codex Doctor no informó fallos; persistió la advertencia ambiental previa
sobre rollout files. Son veredictos históricos: repetir los comandos para
conocer el estado vigente.

## Deuda residual y siguiente orden

### P1 — OpenClaw

- La paridad KORA solo prueba emisión↔instalación gestionada; no prueba
  discovery efectivo, roster, precedencia entre raíces, tool policies ni el
  workspace runtime privado.
- Obtener las unidades ausentes o desviadas bajo demanda con
  `python3 kora.py transmutar --paridad --target openclaw`; no conservar aquí
  una lista nominal que envejezca.
- Contrastar después el resultado con la configuración y los workspaces vivos
  mediante inspección estática segura. No invocar comandos OpenClaw que puedan
  auto-migrar estado solo para consultar.

Orden recomendado: auditar discovery efectivo por agente → adjudicar la raíz
personal compartida → registrar solo agentes desplegables → contrastar tools y
config viva → recién entonces aplicar/canariar.

### Frente congelado — Hermes

Hermes queda fuera del alcance operativo. No modificar su artefacto canónico,
emisiones ni instalaciones, ni realizar T-Hermes, salvo decisión explícita
posterior del operador.

### P2 — eficiencia Codex

Medir en tareas nuevas: costo de descripciones, precisión de discovery,
`medium` frente a `max`, defaults read-only para agentes sanitarios y la
duplicación dual-mode de `dov-dori`. Cambios separados, con evals.

## Cómo retomar

1. Leer `CLAUDE.md`, este handoff y el estado Git vivo.
2. Abrir una tarea Codex nueva o reiniciar la app para asegurar que el catálogo
   use los tombstones configurados.
3. Repetir los gates de mantenimiento y la paridad antes de tocar ley,
   generador o artefactos agénticos.
4. Tratar OpenClaw como un frente separado y mantener Hermes congelado; no
   ampliar el alcance del cierre Codex por conveniencia.

## Rollback

- Resolver el commit exacto bajo demanda con
  `git log --oneline -- <rutas-afectadas>` y revisarlo con
  `git show <commit> -- <rutas-afectadas>`; revertir en orden cronológico
  inverso. No usar hashes guardados en este handoff.
- Tras revertir núcleo o ley, repetir gates y adjudicar cualquier emisión
  afectada antes de aplicar cambios a un runtime.
- Antes de revertir artefactos, preservar cualquier valor único absorbido en
  `consenso-deliberativo`.
- Config Codex: reactivar una skill exige retirar/cambiar su tombstone y
  reiniciar. No reintroducir `sandbox_mode="danger-full-access"` como rollback
  rutinario: volvería a anular el perfil moderno de permisos.
