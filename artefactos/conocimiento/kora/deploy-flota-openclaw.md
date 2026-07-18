---
urn: urn:kora:kb:deploy-flota-openclaw
nombre: deploy-flota-openclaw
version: 1.2.1
estado: publicado
descripcion: "Runbook del deploy pneuma→flota OpenClaw viva: documentación oficial como canon del runtime, diff anti-despotenciación, cambios por superficies soportadas, HITL clínico, canarios frescos, rollback trazable y paridad de cierre."
fuente: "Destilado el 2026-07-06 de la ejecución real de la Fase A del plan tres-frentes (kora-pneuma commits 0d1e76b..e8745ff; openclaw-fleet ec12ac6..3ed79f4); corregido el 2026-07-16 contra OpenClaw 2026.7.1 y el retiro de las skills legacy; v1.2.0 separa capacidad global, membresía fleet, blueprint declarativo y workspace runtime privado; v1.2.1 corrige el estatuto de la transmutación: proyección coreflectiva y emisión determinista, no funtor de artefactos demostrado."
autor: FS
creado: 2026-07-06
lang: es
tags: [deploy, openclaw, flota, runbook, paridad, anti-despotenciacion, canon-runtime, hitl]
cita: [urn:kora:kb:regimen-de-ley]
familia: nota
---

# deploy-flota-openclaw

Runbook del despliegue de agentes pneuma a la flota OpenClaw viva
(`~/openclaw-fleet/blueprints/` → `~/.openclaw/workspaces/`, gateway systemd
`:18790`). El emisor serializa una proyección coreflectiva de la firma
(`ley/3 §7.1`); **desplegar es otra cosa**: instala un derivado sobre un
runtime con estado, memoria y gobernanza propios. Sobrescribir un bot vivo es
producción.

Ruta única: agente capaz → `urn:kora:kb:deploy-flota-openclaw` → `kora.py`
→ `~/openclaw-fleet/CLAUDE.md`. No reinstalar ni invocar
`forjador-openclaw` o `transmute-openclaw`: sus responsabilidades ya tienen
dueño vigente.

## Autoridad y gates de entrada

1. `python3 kora.py velar --estricto` debe cerrar en verde. Nunca transmutar
   con el canon en rojo y nunca fijar en este runbook una cantidad esperada de
   checks: el canon crece.
2. Leer en cada corrida `~/openclaw-fleet/docs/openclaw/`, SSOT oficial local
   de OpenClaw. Antes de usarla, verificar `.upstream-source`,
   `.web-overlay-manifest` y frescura contra Git/web oficiales; una divergencia
   bloquea el deploy y obliga a reparar el sync.
3. Leer `~/openclaw-fleet/CLAUDE.md`, el `AGENTS.md` aplicable y el handoff
   vigente. Inventariar `git status --short` en ambos repos y acordar exclusión
   de archivos con cualquier trabajo concurrente. Los cambios ajenos se
   preservan.
4. Confirmar la superficie exacta del runtime con el CLI instalado
   (`openclaw --version`, `openclaw <comando> --help`) y consultar el schema
   oficial antes de cualquier config. Una página adelantada al binario no
   autoriza a usar un subcomando ausente.
5. Crear un rollback proporcional mediante `openclaw backup create --verify`.
   Si la operación solo cambia config, al menos
   `openclaw backup create --only-config --verify`; si toca estado, exigir el
   respaldo que cubra ese estado. Proteger el artefacto como secreto. Si el
   comando oficial falla, reducir el alcance o bloquear: no sustituirlo en
   silencio por copias crudas de SQLite.

## Diff anti-despotenciación

Antes de aplicar, emitir o inspeccionar la transmutación y comparar
`AGENTS.md`/`SOUL.md` contra el workspace vivo. Clasificar cada capacidad del
vivo como **cubierta** (equivalente en la fuente), **preservada** (vive en un
archivo no reemplazado), **legacy-reemplazada** (infraestructura obsoleta con
destino adjudicado) o **EN RIESGO** (solo existe en el vivo).

Un ítem EN RIESGO bloquea el escalón hasta resolverlo con HITL: absorberlo en
la fuente pneuma, ejecutar `velar`, re-transmutar; o registrar una pérdida
aceptada. Nunca parchear como fuente el workspace derivado. Barrer además:

- identidad o nomenclatura vieja en `USER.md`, `IDENTITY.md`, `BOOT.md` y
  otros preservados que entren al prompt;
- parches del operador presentes solo en el vivo;
- tamaño de cada bootstrap contra los límites documentados para la versión
  instalada; una excepción se configura por la superficie oficial, no
  recortando contenido sin adjudicación;
- referencias path-dependientes y guardias PII mediante `rg`, leyendo y
  adjudicando cada match.

## Escalones y ciclo de despliegue

Ordenar de menor a mayor riesgo y ejecutar uno por vez:

1. blueprint no vivo, con `agentId` y nombre ya alineados;
2. agente vivo no clínico, nombre alineado;
3. agentes clínicos o íntimos al final, cada uno con pausa HITL explícita.

Ciclo de cada escalón:

1. Confirmar que el `agentId` ya pertenece a
   `openclaw.json.reference.agents.list` y que su blueprint preexiste. Un
   `target: openclaw` declara capacidad global, no membresía en esta flota.
2. `python3 kora.py transmutar --urn <URN> --target openclaw --aplicar`.
   El gate actualiza el blueprint autorizado o falla antes de escribir.
3. Materializar el blueprint con el deploy de la flota; KORA nunca escribe
   directamente en el workspace runtime privado.
4. Verificar con pathspec que cambiaron solo los derivados esperados. En la
   flota, stagear archivos concretos; jamás el directorio clínico completo,
   porque puede contener memoria PII no versionable.
5. No reiniciar el gateway por un cambio de archivos del workspace. Abrir un
   canario con `openclaw agent --agent <id> --session-key <clave-nueva> ...`
   para forzar bootstrap fresco y comprobar identidad, frontera y capacidades
   rescatadas. Una sesión antigua no demuestra que el nuevo bootstrap cargó.
6. Si el escalón requiere config, tratarla como transacción separada: consultar
   schema y valor actual; preparar `openclaw config patch` o
   `openclaw config set --batch-json`; ejecutar primero `--dry-run`; aplicar el
   mismo payload; cerrar con `openclaw config validate`. Nunca editar
   `~/.openclaw/openclaw.json` a mano.
7. Respetar el plan de recarga que informa OpenClaw. Reiniciar solo cuando la
   superficie lo requiera o la recarga no se materialice, y entonces usar
   `openclaw gateway restart --safe`; no encadenar reinicios preventivos.
8. Espejar la config ya aplicada en `openclaw.json.reference` y exigir
   `bash scripts/diff-reference.sh` verde.
9. Ejecutar sondas de gateway, agente y canal acordes al blast radius antes de
   commit y push atómicos.

## Cambios de nombre e identidad

No existe una operación genérica de «renombre atómico» del `agentId` vivo.
Separar tres casos:

- **Identidad visible**: usar `openclaw agents set-identity --agent <id> ...`;
  no cambiar el id para corregir un nombre mostrado.
- **Blueprint no registrado**: `git mv` del workspace es una operación de
  repositorio; verificar todas sus referencias y paridad antes de publicar.
- **`agentId` vivo**: operación mayor create→canary→cutover→retire. Crear el
  id nuevo con `openclaw agents add`, desplegar y probar en sesión aislada,
  transferir bindings con `openclaw agents unbind/bind`, observar, y retirar el
  anterior solo con HITL y respaldo. `openclaw agents delete` poda workspace y
  estado: no ejecutarlo como simple paso de renombre.

No mover `~/.openclaw/agents/<id>` ni editar registros SQLite. Las cuentas de
canal y el `agentId` son conceptos distintos; conservar o cambiar un
`accountId` se decide en el cutover y se valida con entrega real.

## Verificación y cierre

La verificación es estratificada; una capa verde no sustituye a la siguiente:

1. canon: `python3 kora.py velar --estricto`;
2. derivación: `python3 kora.py transmutar --paridad` sin desviaciones;
3. config y proceso: `openclaw config validate`, `openclaw doctor --lint`,
   `openclaw gateway status --deep --require-rpc` y `openclaw health`;
4. transporte: probe del canal correspondiente;
5. agente: sesión nueva, sin fallback oculto, validando identidad y capacidad;
6. entrega: canario saliente al destino real cuando el cambio afecta canal;
7. ingreso: mensaje humano benigno cuando se declara E2E. Un probe del token o
   una entrega saliente no demuestra Telegram→gateway→agente→Telegram.

Actualizar el handoff y `~/openclaw-fleet/CLAUDE.md`, revisar
`scripts/diff-reference.sh`, stagear solo el alcance propio, crear commits
semánticos y pushear ambos repos. Cerrar con ambos remotos alineados; un remote
a medias deja al siguiente operador sobre una foto falsa.

## Rollback

- Derivados versionados: revertir el commit causal con `git revert`; no usar
  `checkout`, `reset --hard` ni reescritura de historia como procedimiento.
- Config: aplicar por CLI el parche inverso registrado, validar y obedecer su
  plan de recarga. El backup oficial es la red de seguridad, no permiso para
  editar JSON a mano.
- Bindings: ejecutar la operación inversa con `agents unbind/bind` mientras el
  agente anterior aún existe.
- Estado: no restaurar SQLite en caliente ni copiar sidecars. Usar solamente la
  superficie de verify/restore disponible en el CLI instalado y activar una
  restauración como paso offline explícito.

## Fronteras

Este runbook gobierna la instalación fiel de derivados KORA y solo la config
indispensable para registrar o enrutar esos agentes. No decide upgrades de
OpenClaw o Node, modelos, autenticación, secretos, políticas de Telegram,
retención ni memoria: esas decisiones pertenecen a la gobernanza de la flota,
su `CLAUDE.md` y la documentación oficial viva. El régimen de fondo es
`urn:kora:kb:regimen-de-ley`: pneuma es fuente; la instalación es derivada.
