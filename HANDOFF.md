# Handoff vigente — 2026-07-16 — Clawforge

> Memoria operativa auxiliar. No legisla ni sustituye `ALMA.md`, `ley/`, los
> frontmatters canónicos, Git, GitHub ni el estado vivo. El handoff anterior
> quedó en `_archivo/HANDOFF-2026-07-16-forjador-openclaw.md`.

## Resultado

- El agente vivo `main` de OpenClaw fue auditado y **MIGRADO** a una fuente
  KORA-Pneuma fresca: `urn:ops:artefacto:clawforge`.
- `main` permanece como clave runtime; **Clawforge** es la identidad y el
  objeto canónico. No hubo renombre, migración de estado ni nuevo workspace.
- La transmutación desplegó únicamente `workspaces/main/AGENTS.md` y
  `workspaces/main/SOUL.md`; configuración, memoria, scaffolding y sesiones
  quedaron bajo gobierno local de la flota.
- La skill per-agent `openclaw-lifecycle-manager` fue auditada y **RETIRADA**,
  no migrada: su única función válida ya pertenece a Clawforge, el runbook
  KORA y la documentación oficial viva.
- El task encargado de `/home/felix/openclaw-fleet`
  (`019f66de-905c-77a0-81dc-9c91b998e3a4`) recibió y acusó recibo de la
  coordinación. Confirmó que no dependía de las skills retiradas ni tocaría
  los dos bootstraps durante este despliegue.

## Dictámenes de auditoría

### Clawforge vivo previo

| Pilar | Nota | Hallazgo |
|---|---:|---|
| Formalidad KORA | 1/5 | Sin fuente Pneuma, URN ni sello. |
| Calidad funcional | 3/5 | Núcleo útil, pero alcance excesivo y tooling viejo. |
| Valor real | 4/5 | Es el agente default y coordinador efectivo de la flota. |

**Destino: MIGRAR.** Sobrevivieron diagnóstico antes de acción, cambio mínimo,
reversibilidad, evidencia positiva y coordinación dirigida. Se retiraron
autorreferencia, comandos volátiles, administración universal y ownership
doctrinal.

### `openclaw-lifecycle-manager`

| Pilar | Nota | Hallazgo |
|---|---:|---|
| Formalidad runtime | 2/5 | Cargable, pero no KORA y con procedencia local derivada. |
| Calidad funcional | 1/5 | SSOT inexistente, diez rutas `CM-*` ausentes y CLI obsoleta. |
| Valor vigente | 1/5 | La función coordinadora ya está cubierta sin wrapper. |

**Destino: DESCARTAR la emisión activa.** La refutación adversarial cerró con
confianza 0,98 y no encontró una conducta operable única que quedara huérfana.

## Decisiones

1. **No reactivar la URN histórica.** `urn:kora:artefacto:clawforge` fue
   retirada en la bestia y la ley vigente prohíbe reactivarla. La continuidad
   se registra en `fuente`, no falseando identidad jurídica.
2. **Separar identidad de clave runtime.** `nombre: main` preserva el
   `agentId`; la URN y el cuerpo preservan Clawforge. Renombrar habría sido
   una migración create→canary→cutover→retire sin valor para este objetivo.
3. **Forma agente, arnés orquestador.** Vector `[2,2,4,1,2]`, sigma
   `[3,1,3,3,1]`. No es plataforma ni servicio autónomo: coordina por
   solicitud, sin heartbeat efectivo ni materia ambiental propia.
4. **Dos autoridades, una frontera.** Pneuma gobierna identidad y conducta;
   `openclaw-fleet` gobierna config, host, memoria, canales y operación. Para
   semántica OpenClaw manda `https://docs.openclaw.ai/`.
5. **Conocimiento por URN, comandos fuera del agente.** La fuente solo ancla
   `urn:kora:kb:regimen-de-ley` y
   `urn:kora:kb:deploy-flota-openclaw`; no copia procedimientos volátiles.
6. **Sin composición ficticia.** No se declararon `componible` skills que
   Pneuma no pudiera resolver como dependencias canónicas.
7. **Retiro separado.** La eliminación de `openclaw-lifecycle-manager` fue
   otro commit, después de probar cobertura y con reversibilidad Git.

## Estado verificable

### KORA-Pneuma

- Fuente:
  `artefactos/agentes/ops/main.md`, v1.0.0,
  `urn:ops:artefacto:clawforge`.
- Commit fuente publicado:
  `12e89db3c27ad54fe8515ae9a06c7cead150d152`
  (`feat(ops): canonizar Clawforge en Pneuma`).
- El task de flota actualizó después el runbook a v1.1.0 en
  `cd7dd1f` y cerró paridad proporcional en `369508b`; esos commits son
  concurrentes y no forman parte del autorado de Clawforge.
- `python3 kora.py velar --estricto`: 13 checks verdes al cierre.
- `python3 -m unittest discover -s tests`: 120 tests verdes al cierre.
- `python3 kora.py transmutar --paridad --urn
  urn:ops:artefacto:clawforge --target openclaw`: 1 fiel, 0 desviadas,
  0 no instaladas, 0 sin emisión.
- Los informes no versionados
  `informe-desempeno-medico-hospitalista-2026-07-11.md` e
  `informe-turno-urgenciologo-2026-07-10.md` son ajenos y quedaron fuera.

### OpenClaw Fleet

- Deploy derivado publicado:
  `f3195b4530468df4ae78f778722ab56f034fb12d`
  (`refactor(main): desplegar Clawforge desde Pneuma`).
- Retiro de skill publicado:
  `df391f8e5d0c5b216a56ad285ce545100a720a57`
  (`refactor(main): retirar lifecycle OpenClaw obsoleto`).
- `openclaw health --json`: `ok=true`, plugins sin errores, Telegram
  conectado y `main` como agente default. No se reinició el gateway.
- Canario fresco de identidad:
  Clawforge / `main` / `urn:ops:artefacto:clawforge`, evidencia positiva
  antes de éxito y gate humano ante un `stop` no autorizado.
- Canario fresco posterior al retiro: `OK-CLAWFORGE`; 64 skills visibles al
  modelo y `openclaw-lifecycle-manager` ausente del catálogo inyectado.
- El lock ClawHub ignorado quedó sin la entrada retirada. El commit conserva
  los seis archivos versionados eliminados para rollback.
- Cambios ajenos en memorias y bootstraps clínicos permanecieron sin stagear.
- La cola outbound conserva 583 fallos históricos; es deuda previa y quedó
  fuera de alcance.

## Aprendizajes destilados

1. **Identidad humana y clave runtime no son el mismo tipo de cosa.** Separarlas
   evitó convertir una mejora conductual en una migración operativa mayor.
2. **Canonizar no significa absorber el runtime.** Una fuente KORA puede
   gobernar AGENTS/SOUL sin apropiarse de config, memoria, modelos o canales.
3. **Paridad de archivos no prueba encarnación.** Solo una sesión nueva
   demuestra que OpenClaw cargó el bootstrap; las sesiones conservan snapshots.
4. **Elegible no significa operable.** OpenClaw cargaba una skill cuyos
   preflight, router y comando central estaban rotos.
5. **Benigno no significa vigente.** Un gate de distribución ClawHub puede
   aprobar seguridad del paquete sin validar actualidad semántica ni drift
   local.
6. **La solución más KORA puede quitar una capa.** Clawforge + conocimiento +
   CLI oficial cubren el lifecycle; reautorar otro coordinador duplicaría
   autoridad.
7. **La concurrencia se gobierna por path.** Reservar dos archivos y stagear
   pathspecs concretos permitió publicar sin mezclar cambios clínicos ni el
   upgrade paralelo.
8. **Los comandos envejecen más rápido que los contratos.** El agente conserva
   invariantes y gates; el runbook y la documentación viva conservan la
   mecánica.

## Artefactos relevantes

- Fuente Clawforge:
  `artefactos/agentes/ops/main.md`.
- Ley de transmutación: `ley/3-transmutacion.md`.
- Régimen: `artefactos/conocimiento/kora/regimen-de-ley.md`.
- Runbook vigente:
  `artefactos/conocimiento/kora/deploy-flota-openclaw.md`, v1.1.0.
- Emisión instalada:
  `~/openclaw-fleet/workspaces/main/AGENTS.md` y `SOUL.md`.
- Gobernanza runtime: `~/openclaw-fleet/CLAUDE.md` y
  `~/openclaw-fleet/docs/fleet-canon-policy.md`.
- Canon oficial: `https://docs.openclaw.ai/`, especialmente
  `/cli/agents`, `/cli/skills`, `/automation/standing-orders` y
  `/concepts/soul`.

## Cómo retomar

1. Leer `CLAUDE.md`, este handoff y el estado Git vivo.
2. Para cambiar conducta de Clawforge, editar
   `urn:ops:artefacto:clawforge` en Pneuma, ejecutar gates, transmutar,
   revisar diff anti-despotenciación, aplicar y probar con sesión nueva.
3. No editar directamente un `AGENTS.md` o `SOUL.md` sellado y no
   reinstalar `openclaw-lifecycle-manager`, `forjador-openclaw` ni
   `transmute-openclaw`.
4. Auditar por separado `operator`, `troubleshooter`,
   `version-manager` y `KORA-PROVENANCE.md`; fueron observados como posible
   deuda legacy, pero no se adjudicaron ni modificaron en esta sesión.
5. Verificar que el cierre documental concurrente de la flota actualice el
   inventario de Pneuma a 8/10 agentes emitidos; si no, corregir solo esa frase.
6. Tratar dead-letter, modelos, Node, backup, Telegram y config como trabajo de
   flota independiente.

## Rollback

- Fuente: `git revert 12e89db` solo si también se adjudica el derivado vivo.
- Deploy: `git revert f3195b4`.
- Skill retirada: `git revert df391f8`.
- No usar `reset --hard` ni restaurar estado OpenClaw por copia manual.
