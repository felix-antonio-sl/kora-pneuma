# Handoff vigente — 2026-07-30 — perfil de datos personal del ecosistema

> Memoria operativa auxiliar. No legisla ni sustituye `ALMA.md`, `ley/`, los
> artefactos canónicos, Git, los sistemas clínicos ni el estado vivo del host.

## Objetivo vigente

`urn:salud:kb:perfil-dev-personal-full` es la doctrina canónica para el host
privado y mono-usuario del operador durante desarrollo, preparación,
conciliación, migración, pruebas locales y soporte personal.

El perfil permite:

- procesar, persistir, recuperar, cruzar y visualizar PII/PHI sin
  desidentificación previa;
- usar Drive, `hsc-agent-cli`, extracts, archivos privados, memoria, sesiones y
  bases locales como fuentes;
- conservar staging y cuarentena, usar la protección del host/volumen y
  concentrar iniciación, ejecución y aprobación en el mismo operador;
- transferir el mínimo pertinente a proveedores y conectores ya configurados.

No relaja secretos, Git/publicación, mutación de fuentes, destinos nuevos,
identidad, procedencia, temporalidad, idempotencia ni autoridad clínica final.
Una superficie compartida, piloto o productiva usa
`INSTITUTIONAL_CONTROLLED`.

## Fuente y consumidores

```text
urn:salud:kb:perfil-dev-personal-full                    v1.0.0
urn:ops:artefacto:clawforge                             v1.2.0
urn:salud:artefacto:urgenciologo                        v3.14.0
urn:salud:artefacto:medico-hospitalista                 v1.11.0
urn:salud:artefacto:salubrista                          v3.4.0
urn:salud:artefacto:seguridad-informacion-salud         v1.2.0
urn:salud:artefacto:participacion-usuario-sintetico-hodom-hsc v1.1.0
urn:salud:artefacto:reporte-diario-hodom                v2.2.0
```

Clawforge y los tres agentes de salud resuelven el perfil antes de imponer una
compuerta de privacidad. La skill de seguridad distingue perfil personal de
entorno institucional. Los usuarios sintéticos pueden inspeccionar fuentes
reales privadas, pero su aceptación no se convierte en acto profesional. El
reporte diario puede contener PHI en su artefacto protegido; chat, Git y
salidas publicables conservan solo estado, conteos y rutas.

## Emisión e instalación

- `main`, `urgenciologo`, `medico-hospitalista` y `salubrista` fueron
  retransmutados a sus targets y aplicados donde corresponde.
- `seguridad-informacion-salud` fue aplicada en Claude Code, Codex y OpenCode.
- `reporte-diario-hodom` fue aplicada en Codex.
- `participacion-usuario-sintetico-hodom-hsc` fue aplicada con alcance de
  proyecto en `/home/felix/projects/hd-hsc-os`.
- Las emisiones OpenClaw de `main` y los tres agentes de salud quedaron
  actualizadas en `openclaw-fleet`; la materialización de los workspaces
  pertenece al contrato de ese repo.

## Evidencia

```text
velar --estricto                 13/13
suite KORA                       309 passed; 224 subtests passed
paridad global                   0 desviadas
eval focal del perfil            4/4
```

Los targets declarados pero no instalados por decisión de alcance se informan
como `no-instalada`; no equivalen a desviación.

## Próxima acción

Usar `DEV_PERSONAL_FULL` para inventariar y ensayar la migración real en
superficies privadas. Antes de compartir, incorporar otro usuario o desplegar
fuera del host, cambiar explícitamente a `INSTITUTIONAL_CONTROLLED` y ejecutar
los controles del entorno receptor.
