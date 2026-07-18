# Handoff vigente — 2026-07-18 — agentes clínicos KORA → OpenClaw

> Memoria operativa auxiliar. No legisla ni sustituye `ALMA.md`, `ley/`, los
> artefactos canónicos, Git ni el estado vivo de OpenClaw. La continuidad
> detallada del despliegue está en
> `/home/felix/openclaw-fleet/docs/handoffs/handoff-2026-07-18.md`; el recibo
> verificable está en
> `/home/felix/openclaw-fleet/docs/deploy-receipt-full-profile-urgenciologo-medico-hospitalista-2026-07-18.md`.

## Objetivo y alcance

Actualizar canónicamente `urgenciologo` y `medico-hospitalista`, incorporar
`agent-autonomy-5`, modelar el boarding de hospitalizados en UE sin crear un
tercer régimen, liberar su superficie técnica completa bajo Guardian y propagar
la cadena fuente → emisiones → Fleet → runtime de forma verificable y sin PHI.

El alcance KORA comprendió tres fuentes canónicas, sus cuatro targets y la
paridad de cinco instalaciones por agente. El alcance OpenClaw comprendió
blueprints, materialización, configuración efectiva, memoria autorizada,
canarios sintéticos y documentación de despliegue. No incluyó consultar un
paciente real, enviar mensajes, ejercitar elevado ni resolver disaster recovery
off-host.

## Estado comprobado

- `master` contiene y publicó `35f34e5`
  (`feat(salud): incorporar boarding UE y autonomy 5`).
- `urn:salud:artefacto:urgenciologo` quedó en v3.12.0.
- `urn:salud:artefacto:medico-hospitalista` quedó en v1.9.0.
- `urn:salud:kb:manual-agente-hsc-agent-cli` quedó en v1.0.18.
- Ambos agentes alcanzaron `5 fiel`, `0 desviadas`, `0 no-instaladas` y
  `0 sin-emisión`.
- KORA cerró con `velar --estricto` 13/13 y 185 pruebas.
- Fleet publicó el contrato clínico en `74080d3`, el espejo documental en
  `07dd9dd` y el recibo final en `684bcb6`.
- Al cierre de ese incremento, el gate Fleet vivo pasó 33/33 y los canarios
  ejecutaron `gpt-5.6-sol` mediante el arnés Codex, sin fallback.

Estos resultados son evidencia histórica de los commits indicados. El estado
actual se vuelve a consultar; no se infiere desde este handoff.

## Decisiones consolidadas

1. **UE boarding es ubicación, no régimen.**
   `S-HOSPITAL_UE_BOARDING` es subestado micro-asistencial de `S-HOSPITAL`.
   Sale a `S-HOSPITAL` cuando termina el boarding, a `S-END` al cerrar el pase
   y deriva a urgencias si el caso no está hospitalizado.
2. **SGH demuestra hospitalización.** `find --hospitalizados` es fuente
   primaria; DAU complementa y nunca prueba por sí solo hospitalización.
3. **El estado vivo resuelve salas.** No se congelan IDs ni nombres observados
   en pruebas.
4. **Autonomía factual, juicio clínico humano.** El CLI expone hechos,
   handles y planes de consulta. Priorización, SOAP, inferencia, propuesta y
   decisión final permanecen fuera del CLI.
5. **Contrato masivo explícito.** `batch_plan.requests[].command_args` se sigue
   en serie. Un singleton puede omitir `batch_plan` y usar `entry.handle` o
   `best_current_context`. En stream mandan `envelope.state` y
   `envelope.error_code`; `summary` es opcional.
6. **Capacidad técnica no es autoridad.** `profile=full` habilita web,
   escritura, memoria, mensajería, sesiones y subagentes, pero no autoriza
   acciones clínicas, destructivas o externas.
7. **Guardian es la postura normal de shell.** `tools.exec.mode=auto` se
   materializa en Codex como shell nativo `bash` con revisión Guardian. La
   allowlist durable contiene solo `hsc-agent-cli` y `rg`; los misses pasan por
   revisión y terminan en deny si no existe aprobación.
8. **Memoria clínica no se promueve.** La búsqueda usa KORA y memoria curada;
   `sessionMemory=false`. `/new` separa contexto, pero no borra transcripciones.
   El delta del pase es efímero y no se convierte en tabla, memoria, log,
   mensaje, repo o delegación.
9. **La cadena de autoridad se preserva.** Un archivo sellado se corrige en
   KORA, se reemite, se lleva al blueprint y recién después se materializa.
   Runtime y blueprint no son fuentes doctrinales.

## Aprendizajes duraderos

### Hechos comprobados

- La policy efectiva de shell es la intersección entre config y approvals del
  host. Un warning estático de `security=full` global no reemplaza
  `openclaw exec-policy show` para conocer la postura del agente.
- En el arnés Codex, pedir literalmente una herramienta llamada `exec` puede
  producir un falso negativo; la ejecución nativa se observa como `bash`, aun
  cuando su gobierno siga siendo `tools.exec.mode`.
- `sessionMemory=false` evita indexar conversaciones; no garantiza que el
  runtime no conserve archivos de transcript.
- El espejo oficial puede avanzar durante un despliegue. La frescura se cierra
  sincronizando y repitiendo el gate vivo al final, no confiando en el SHA
  observado al inicio.
- Un archivo runtime no gestionado con evidencia de prueba no se copia al
  blueprint ni a Git. Se retira una vez que su valor reusable está canonizado.
- El estado Git debe revisarse otra vez justo antes de stage y push: un árbol
  limpio puede recibir trabajo concurrente después de un gate verde.

### Decisiones adoptadas

- Mantener el perfil `full` pedido, pero conservar Guardian, owner-only para
  elevado y prohibición de propagación de PHI.
- Mantener la skill `asistencial-hospital` única y componible; no duplicarla
  dentro de hospitalista.
- Tratar las pruebas sin pacientes reales como una garantía de privacidad, no
  como una demostración de HCC completo.

### Hipótesis no promovidas

- No se concluye que HCC esté indisponible: su health es parcial porque una
  prueba real requiere un caso autorizado.
- No se concluye que el build post-tag de HSC sea release: `de1e0b7` está limpio
  y contiene `agent-autonomy-5`, pero sigue siendo posterior a v3.1.1.

## Alternativas descartadas

- Crear un tercer modo asistencial para UE: confunde ubicación con régimen.
- Usar DAU como prueba primaria de hospitalización: degrada la verdad factual.
- Mover priorización al CLI: mezcla adquisición de hechos con juicio clínico.
- Ejecutar lotes en paralelo: aumenta tormentas y contradice el contrato.
- Persistir el tablero delta: crea una segunda fuente con riesgo de PHI.
- Habilitar shell sin revisión: contradice la preferencia explícita por
  Guardian.
- Copiar el informe de prueba a memoria o repositorio: duplica doctrina y puede
  transportar identificadores.

## Artefactos canónicos afectados

- `artefactos/agentes/salud/urgenciologo.md`: v3.12.0 y
  `agent-autonomy-5`.
- `artefactos/agentes/salud/medico-hospitalista.md`: v1.9.0,
  `S-HOSPITAL_UE_BOARDING`, transiciones y fronteras.
- `artefactos/conocimiento/salud/manual-agente-hsc-agent-cli.md`: v1.0.18,
  lote/singleton/stream y procedencia del build HSC.
- `_emision/` e instalaciones de Claude Code, Codex, OpenCode y OpenClaw:
  derivados regenerables, no fuentes.
- `HANDOFF.md`: única memoria operativa vigente de KORA.

Los artefactos Fleet y runtime se enumeran en el handoff Fleet; no se duplican
aquí.

## Riesgos y pendientes

- Publicar un release HSC que incorpore formalmente `agent-autonomy-5`.
- HCC continúa parcialmente probado hasta que exista un caso legítimo.
- El perfil `full`, sesiones visibles y escritura fuera del workspace amplían
  el blast radius; los controles conductuales no son DLP.
- Falta backup full-state off-host y restore ensayado.
- Mensajería, elevado y entrega Telegram no se probaron mediante efectos reales.
- Al cerrar esta memoria, Fleet contiene un patch concurrente no atribuido de
  hardening de memoria. No pertenece a este incremento y no debe stagearse
  desde KORA; consultar su handoff antes de intervenir.

## Siguiente acción recomendada

Adjudicar el patch concurrente de memoria en Fleet como una tarea separada:
identificar owner, esperar un estado estable, revisar el diff completo, reparar
su gate si corresponde, ejecutar validación estática/viva y publicar solo
cuando constituya una unidad propia. Después, priorizar backup off-host con
restore ensayado; HCC se prueba únicamente dentro de atención autorizada.

## Cómo retomar

1. Leer `CLAUDE.md`, este `HANDOFF.md` y el estado Git vivo.
2. Resolver las tres URN anteriores con `python3 kora.py nombre <URN>`.
3. Ejecutar `python3 kora.py velar --estricto` y
   `python3 -m unittest discover -s tests`.
4. Para cualquier cambio agéntico, repetir paridad por URN antes de tocar Fleet.
5. Leer el handoff vigente de Fleet y adjudicar sus cambios concurrentes antes
   de materializar o modificar config.

## Rollback

Usar `git revert`, nunca `reset --hard`. Revertir primero el incremento Fleet y
después `35f34e5` solo si se decide retirar también la doctrina. Tras cualquier
reversión, reemitir, comprobar paridad, materializar y ejecutar canarios nuevos.
No volver a workspaces clínicos históricos ni restaurar memoria episódica como
atajo.
