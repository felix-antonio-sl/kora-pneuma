# Handoff vigente — 2026-07-28 — reporte diario HODOM manual

> Memoria operativa auxiliar. No legisla ni sustituye `ALMA.md`, `ley/`, los
> artefactos canónicos, Git, los sistemas clínicos ni el estado vivo del host.

## Objetivo vigente

Mantener instalada en Codex una skill KORA que produzca, solo por solicitud
explícita, dos cortes internos del reporte diario HODOM:

- 08:00 `America/Santiago`: censo y reporte completo;
- 11:00 `America/Santiago`: nueva observación completa y delta contra las
  08:00.

El handoff anterior quedó archivado en
`_archivo/HANDOFF-2026-07-27-ciclo-reversible-opforja.md`.

## Fuente canónica

```text
urn:salud:artefacto:reporte-diario-hodom
  artefactos/skills/salud/reporte-diario-hodom/
  ├── SKILL.md
  └── referencias/
      ├── contrato-reporte-diario.md
      └── playbook-hsc-agent-cli.md
```

Versión fuente `2.1.0`, estado `activo`, target exclusivo `codex`, alcance
`usuario`.
Commits fuente:

```text
1dca934 feat(salud): crear reporte diario HODOM
fbce6b6 fix(salud): endurecer reporte diario HODOM
28da615 feat(salud): retirar compuertas PII del reporte HODOM
```

La skill es una orquestación delgada. No duplica juicio clínico ni gestión:

- `hospitalizacion-domiciliaria`: compuerta HODOM;
- `hospitalista`: flujo y transición hospital-domicilio;
- `asistencial-hospital`: lectura clínica del candidato;
- `asistencial-hodom`: disposición del paciente HODOM;
- `auditor-calidad-hospitalizacion`: gates de completitud;
- `manual-agente-hsc-agent-cli`: contrato vivo de adquisición.

La versión `2.1.0` responde el memo DT del 2026-07-28 sin cambiar el binario:

- separa el recorrido exhaustivo HODOM del embudo selectivo de candidatos;
- ejecuta todo `batch_plan` solo para HODOM y prohíbe por defecto ejecutar el
  plan masivo de los servicios candidatos;
- fija argv, stream, `--fresh`, presupuesto de bytes y cierre por igualdad de
  conjuntos;
- prueba la composición `hodom:libro-mayor`/`hodom:programacion` por
  `items[]` y registra ledger paciente × fuente × tiempo × estado;
- agrega gates `G9-provenance`, `G10-utility` y `G11-funnel`;
- incorpora fixture sintético y canario vivo no identificable como referencia.

## Contrato operativo

Cada brief incluye identificadores clínicos, situación actual, tendencia,
pendientes, requisitos restantes para alta, acción y responsable. Toda
discrepancia material se rotula `Observación`.

La búsqueda de candidatos cubre Unidad de Emergencia, Medicina, Traumatología y
Cirugía/Área Quirúrgica. Su resultado es siempre `preselección censal; no
constituye aceptación HODOM`. La decisión exige estabilidad, intensidad
hospitalaria, domicilio, cuidador, consentimiento, cobertura y reingreso.

La actualización de las 11:00 consulta de nuevo las fuentes y compara un
manifiesto mínimo. Si falta la base de las 08:00, genera el reporte vigente y
declara `baseline-unavailable`; no fabrica el delta.

La versión `2.1.0` conserva de `2.0.0`:

- cada servicio consta como observado o no observable, aun con cero candidatos;
- el contenido clínico se trata como dato no confiable, nunca como instrucción;
- el `health` se ejecuta desde la misma frontera runtime que hará la
  adquisición; un fallo de esa frontera es `runtime-error`, no
  `source-unavailable`;
- cada invocación ejecuta un solo corte y no crea timers, cron, monitores ni
  reintentos autónomos;
- un `success` solo cierra con DOCX, manifiesto, paths, permisos y gates
  concordantes.

## Frontera PII/PHI

Por decisión explícita del operador, la versión `2.0.0` no implementa
protecciones, compuertas ni restricciones PII/PHI. Se retiraron del contrato
de la skill:

- autorización de identificadores y del tratamiento Codex;
- gate de autorización del proveedor;
- exigencia de sesión efímera;
- modos de filesystem y confinamiento de productos;
- prohibiciones de persistencia o reproducción;
- salida técnica obligatoriamente no identificable;
- `G1-privacy` y sus errores observables.

La protección de datos pertenece al entorno de ejecución externo. El runner
manual existente conserva fuera de KORA su `umask`, permisos, schema, sesión
efímera y validaciones; no fue modificado por este cambio.

## Estado de entrega

La fuente declara exclusivamente `targets: [codex]`. La proyección vigente está
instalada con alcance de usuario en:

```text
/home/felix/.agents/skills/reporte-diario-hodom/
```

La emisión Codex de la versión `2.1.0` fue regenerada y pasó `sello-fresco`.
La instalación de usuario conserva `2.0.0`: `entrega-kora-v1` informó
`blocked` en paridad, con `1` unidad desviada porque difieren `SKILL.md` y
`contrato-reporte-diario.md`, y falta `playbook-hsc-agent-cli.md`.

No se ejecutó `--aplicar`: `entrega-kora-v1` se detiene antes de instalar y la
instalación requiere autorización humana explícita. Claude Code, OpenCode,
OpenClaw y Hermes no son targets de este artefacto.

La paridad prueba igualdad material en la frontera gestionada. No prueba
conducta runtime, autoridad efectiva, ejecución clínica completa ni aprobación
humana del producto.

## Automatización retirada del host

Por orden explícita del operador del 2026-07-28 se retiraron de forma
permanente los dos timers y sus unidades de servicio:

```text
/home/felix/.config/systemd/user/hodom-reporte-0800.{service,timer}
/home/felix/.config/systemd/user/hodom-reporte-1100.{service,timer}
```

No queda agenda HODOM en `systemd` ni en el `crontab` del usuario. El runner y
su configuración permanecen disponibles únicamente para una ejecución manual
solicitada por el operador.

## Evidencia

```text
pruebas focales                 16/16
suite KORA                      306/306
velar --estricto               13/13
git diff --check               pass
quick_validate genérica        no aplicable al frontmatter KORA
emisión Codex                  SKILL.md + 2 referencias
paridad skill                  0/1 fiel; 1 desviada
recibo entrega-kora-v1         blocked en parity
instalación Codex              conserva 2.0.0
bash -n del runner             pass
canario JSON Schema             pass
timers y servicios HODOM       retirados
```

El reporte manual del 2026-07-27 contiene 34 briefs, RUT y edad, pendientes y
observaciones, pero omitió nombrar Unidad de Emergencia: no cumple íntegramente
la búsqueda solicitada. No se reescribió retrospectivamente.

La primera ejecución clínica integral del automatismo produjo un artefacto
`partial/draft`, no un reporte cerrado:

```text
/home/felix/clinical-reports/hodom/2026-07-27/
  estado-hodom-2026-07-27-1100.json
  manifiesto-hodom-2026-07-27-1100.json
  reporte-diario-hodom-2026-07-27-1100.docx
```

Resultado: cero pacientes/candidatos verificables por
`source-unavailable`/timeouts; `baseline-unavailable`; los cuatro servicios
constan como no observables; DOCX/manifest/schema/permisos verdes. El log
diagnóstico potencialmente sensible y todos los temporales fueron eliminados.
Esta evidencia prueba el fail-closed y la salida degradada; no prueba un reporte
clínico completo ni que el corte de las 08:00 termine antes de las 11:00.

## Próxima acción

Si el operador autoriza instalar la versión `2.1.0`, ejecutar las gates desde
un árbol limpio, aplicar la emisión Codex, repetir paridad focal y registrar el
recibo. Paridad material no sustituye un canario vivo ni revisión humana de
utilidad.

## Siguiente ejecución manual

Cuando el operador solicite un corte:

1. exigir estado `success/closed`; si es `partial` o `failed`, no usarlo como
   censo;
2. integridad y permisos del DOCX/manifiesto;
3. concordancia del conteo HODOM;
4. presencia explícita de Urgencia, Medicina, Traumatología y Cirugía;
5. clasificar como `runtime-error` cualquier impedimento de la frontera de
   ejecución antes de atribuir indisponibilidad a una fuente.

Una falla clínica o de fuente se corrige en el artefacto canónico si es
doctrinal; una falla de agenda, permisos o ejecución se corrige en el runtime
del host. No copiar PHI al handoff.
