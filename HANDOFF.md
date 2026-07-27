# Handoff vigente — 2026-07-27 — reporte diario HODOM automatizable

> Memoria operativa auxiliar. No legisla ni sustituye `ALMA.md`, `ley/`, los
> artefactos canónicos, Git, los sistemas clínicos ni el estado vivo del host.

## Objetivo cerrado

Crear e instalar en Codex una skill KORA que produzca dos cortes confidenciales
del reporte diario HODOM:

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
      └── contrato-reporte-diario.md
```

Versión `1.0.0`, estado `activo`, target exclusivo `codex`, alcance `usuario`.
Commit fuente:

```text
1dca934 feat(salud): crear reporte diario HODOM
```

La skill es una orquestación delgada. No duplica juicio clínico ni gestión:

- `hospitalizacion-domiciliaria`: compuerta HODOM;
- `hospitalista`: flujo y transición hospital-domicilio;
- `asistencial-hospital`: lectura clínica del candidato;
- `asistencial-hodom`: disposición del paciente HODOM;
- `auditor-calidad-hospitalizacion`: gates de completitud;
- `manual-agente-hsc-agent-cli`: contrato vivo de adquisición.

## Contrato operativo

Cada brief incluye identificadores autorizados en el producto confidencial,
situación actual, tendencia, pendientes, requisitos restantes para alta, acción
y responsable. Toda discrepancia material se rotula `Observación`.

La búsqueda de candidatos cubre Unidad de Emergencia, Medicina, Traumatología y
Cirugía/Área Quirúrgica. Su resultado es siempre `preselección censal; no
constituye aceptación HODOM`. La decisión exige estabilidad, intensidad
hospitalaria, domicilio, cuidador, consentimiento, cobertura y reingreso.

La actualización de las 11:00 consulta de nuevo las fuentes y compara un
manifiesto confidencial mínimo. Si falta la base de las 08:00, genera el reporte
vigente y declara `baseline-unavailable`; no fabrica el delta.

## Privacidad

- Cero PHI en esta fuente, pruebas, Git, emisión, memoria o salida técnica.
- DOCX y manifiesto solo fuera de repositorios, bajo
  `/home/felix/clinical-reports/hodom/YYYY-MM-DD/`.
- Directorios `0700`; archivos `0600`.
- Ejecución Codex `--ephemeral`, sin stdout/stderr en journal.
- Estado final restringido por JSON Schema a rutas, conteos, gates y avisos no
  identificables.

La autorización del operador para nombre, RUT y edad rige solo el reporte
clínico. No amplía la frontera de persistencia.

## Automatización materializada en el host

Los factores runtime no son fuente KORA y viven fuera del repo:

```text
/home/felix/.local/bin/hodom-reporte-diario
/home/felix/.config/hodom-reporte-diario/
/home/felix/.config/systemd/user/hodom-reporte-0800.{service,timer}
/home/felix/.config/systemd/user/hodom-reporte-1100.{service,timer}
```

Ambos timers están habilitados y activos. `Persistent=true` permite recuperar
un corte omitido tras reinicio; un lock serializa los trabajos si coinciden.
El usuario tiene `Linger=yes`, por lo que el user manager puede ejecutarlos sin
una sesión gráfica abierta.

## Evidencia

```text
pruebas focales                 10/10
suite KORA                      300/300
velar --estricto               13/13
git diff --check               pass
quick_validate emitida         valid
emisión Codex                  SKILL.md + 1 referencia
paridad skill                  1/1 fiel
permisos instalados            0600
bash -n del runner             pass
systemd-analyze verify         pass
canario Codex no interactivo   AUTOMATION_OK
timers                         enabled + active
```

Próximas ejecuciones observadas al cierre:

```text
2026-07-28 08:00 America/Santiago
2026-07-28 11:00 America/Santiago
```

La validación prueba forma, instalación, agenda y capacidad de invocación no
interactiva. No adelanta ni simula el resultado clínico de mañana. El primer
cierre real debe comprobarse en los archivos de estado y DOCX del directorio
confidencial.

## Siguiente acción

Después de los primeros dos cortes, revisar:

1. estado técnico `success|partial|failed`;
2. integridad y permisos del DOCX/manifiesto;
3. concordancia del conteo HODOM;
4. calidad clínica de briefs y candidatos;
5. duración real para confirmar que el corte de las 08:00 termina antes de las
   11:00.

Una falla clínica o de fuente se corrige en el artefacto canónico si es
doctrinal; una falla de agenda, permisos o ejecución se corrige en el runtime
del host. No copiar PHI al handoff.
