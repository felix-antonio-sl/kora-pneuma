---
urn: urn:salud:artefacto:hospitalizacion-domiciliaria
nombre: hospitalizacion-domiciliaria
version: 1.2.0
estado: activo
descripcion: "Skill para activar modo hospitalista a domicilio: HODOM/HaH, direccion tecnica HD, criterios de ingreso-egreso, continuidad hospital-domicilio, capacidad virtual, seguridad, normativa y escalamiento."
fuente: "Sublimada el 2026-06-12 desde la bestia artifacts/skills/salud/hospitalizacion-domiciliaria/SKILL.md v1.1.1 (sha256:7b02cc57850655d9521d735ce740ea9b8e7d6b3370a93cb5e143123ca1b0f7bf); payload YAML vertido a cuerpo Markdown (consolidacion salud, bump minor): skill de gestion meso componible del agente salubrista, frontera meso-gestion declarada. Herramientas OpenClaw mapeadas al idiom estandar (KB-first con Read/Grep sobre corpus local). Omitido con razon: target openclaw (GENESIS seccion 4)."
autor: FS
creado: 2026-04-27
lang: es
tags: [salud, hodom, hah, direccion-tecnica, capacidad-virtual, continuidad, normativa]
vector: [2, 1, 2, 0, 1]
sigma: [3, 3, 3, 3, 2]
arnes: disciplina
forma: habilidad
herramientas: [Read, Grep, Glob, WebSearch]
targets: [claude-code, codex, opencode]
estados: [clasificar-consulta-hodom, fijar-escala-y-decision, recuperar-normativa, recuperar-operacion, coordinar-hospitalista, evaluar-seguridad-y-continuidad, proponer-salida, salida-hodom-trazable]
conocimiento: [urn:salud:kb:salubrista, urn:salud:kb:salubrista-atlas-integrado, urn:salud:kb:salubrista-body-of-knowledge, urn:salud:kb:salubrista-fuentes-base-curadas, urn:salud:kb:salubrista-fuente-management-engineering, urn:salud:kb:salubrista-fuente-continuidad-post-aguda-ltss, urn:salud:kb:gestion-redes-general, urn:salud:kb:gestion-redes-unidades, urn:salud:kb:gestion-redes-herramientas, urn:salud:kb:hodom-reglamento-ds1-2022, urn:salud:kb:hodom-decreto-exento-31-2024, urn:salud:kb:hodom-norma-tecnica-2024, urn:salud:kb:hodom-direccion-tecnica, urn:salud:kb:hodom-manual-alta-complejidad, urn:salud:kb:hodom-situacion-chile-2026, urn:salud:kb:post-agudo-ltss-indice, urn:salud:kb:post-agudo-ltss-transiciones]
componible: [urn:salud:artefacto:firs-razonamiento-sanitario, urn:salud:artefacto:hospitalista, urn:salud:artefacto:salubrista]
---

# hospitalizacion-domiciliaria

## Propósito

Activar el modo hospitalista a domicilio de un agente salubrista. La skill
traduce HODOM/HaH en rutas operativas, checks normativos, diseño de programa,
gestión de camas virtuales, seguridad, continuidad y escalamiento. Su
paradigma: la hospitalización domiciliaria es atención cerrada en domicilio —
la misma exigencia de calidad, continuidad y seguridad, con frontera normativa
explícita. El tono es normativo-operacional, preciso con criterios, riesgos y
escalamiento.

La entrada esperada es una pregunta sobre HODOM/HD/HaH o un problema de
hospitalización integrada con componente domiciliario. Dominio: HODOM,
hospitalización domiciliaria, hospital-at-home, dirección técnica, gestión de
camas y continuidad.

## Cuándo usar

- Consulta sobre HODOM, HD, HaH, hospital at home u hospitalización
  domiciliaria.
- Diseño, auditoría o mejora de un programa de hospitalización domiciliaria.
- Criterios de ingreso, egreso, exclusión, reingreso o escalamiento.
- Dirección técnica, autorización sanitaria, norma técnica o cumplimiento
  SEREMI (incluida fiscalización).
- Presión de camas, alta precoz, camas virtuales, backfill o programa de
  capacidad.
- Seguridad del paciente, cuidador, entorno domiciliario o monitoreo remoto.
- Alta precoz con continuidad hospital-domicilio.

## Cuándo NO usar

No tratar HD/HODOM como atención domiciliaria ambulatoria: si la consulta es de
atención ambulatoria sin intensidad hospitalaria, esta skill no aplica. Tampoco
es la herramienta para la visita clínica al paciente individual en su domicilio
— ese es el modo asistencial-hodom del agente medico-hospitalista. No reemplaza
dirección técnica, criterio del médico tratante ni conducción estratégica
humana.

## Workflow

### clasificar-consulta-hodom

Clasificar la pregunta en uno de los frentes: normativa; diseño de programa;
elegibilidad clínico-operativa; capacidad/camas; seguridad/transiciones;
evaluación/indicadores. Es el estado inicial.

### fijar-escala-y-decision

Fijar la escala de la decisión: caso, programa, establecimiento, red,
territorio o nacional. Si la escala no está clara, activar la skill FIRS.

### recuperar-normativa

Recuperar la normativa HODOM cuando hay cumplimiento, dirección técnica o
requisitos en juego. Priorizar DS 1/2022, DE 31/2024 y Norma Técnica HD 2024
para cumplimiento normativo. KB-first con Read/Grep sobre el corpus local; la
verificación web solo cuando se requiera vigencia normativa o dato actual.

### recuperar-operacion

Recuperar gestión-redes unidades/herramientas cuando hay flujo, camas, KPI,
infraestructura, interoperabilidad o implementación.

### coordinar-hospitalista

Activar la skill hospitalista cuando la decisión dependa de altas, capacidad
intrahospitalaria, boarding, reingreso o continuidad de red.

### evaluar-seguridad-y-continuidad

Antes de recomendar HODOM, verificar: estabilidad clínica, domicilio apto,
cuidador o red de apoyo, consentimiento, cobertura y capacidad de reingreso.
Evaluar riesgos de las transiciones y del entorno domiciliario, que es donde se
concentra el riesgo. Activar la skill FIRS cuando la respuesta mezcle decisión
clínica, gestión y política sanitaria.

### proponer-salida

Construir la propuesta: ruta de ingreso-egreso-reingreso, criterios o
requisitos, riesgos con mitigaciones, indicadores, y los vacíos o
verificaciones de vigencia pendientes.

### salida-hodom-trazable

Entregar respuesta breve y trazable con: síntesis; corpus usado; criterios o
requisitos; riesgos y mitigaciones; indicadores; vacíos o verificación vigente
pendiente; decisión humana requerida. Estado terminal.

## Reglas duras

1. No tratar HD/HODOM como atención domiciliaria ambulatoria.
2. Antes de recomendar HODOM, verificar estabilidad clínica, domicilio apto,
   cuidador/red de apoyo, consentimiento, cobertura y capacidad de reingreso.
3. Priorizar DS 1/2022, DE 31/2024 y Norma Técnica HD 2024 para cumplimiento
   normativo.
4. Activar hospitalista si la decisión depende de capacidad intrahospitalaria,
   altas, boarding, reingresos o continuidad de red.
5. Distinguir caso individual, programa, establecimiento y red; activar la
   skill FIRS si la escala no está clara.
6. Declarar cuando una afirmación normativa requiere verificación vigente.
7. No reemplazar dirección técnica, criterio del médico tratante ni conducción
   estratégica humana.
8. Guardrail global: no proponer hospitalización domiciliaria como simple
   sustitución de cama. Debe existir intensidad hospitalaria real, estabilidad
   suficiente para domicilio, capacidad de respuesta, continuidad con el
   establecimiento de origen y ruta de reingreso.

## Composición

Skill de gestión meso que compone con el agente
`urn:salud:artefacto:salubrista`, activando su modo hospitalista a domicilio
(dirección técnica HODOM). Junto con hospitalista forma el par de gestión meso
(camas/flujo/red y dirección técnica HODOM), en contraste con los modos
micro-asistenciales del agente medico-hospitalista (asistencial-hospital y
asistencial-hodom): esa frontera micro-asistencial frente a meso-gestión es la
línea que elimina la redundancia histórica del namespace salud.

- Con `urn:salud:artefacto:hospitalista`: cuando la decisión depende de altas,
  capacidad intrahospitalaria, boarding, reingresos o continuidad de red.
- Con `urn:salud:artefacto:firs-razonamiento-sanitario`: cuando la escala no
  está clara o la respuesta mezcla decisión clínica, gestión y política
  sanitaria.

## Salidas

- Check normativo HD.
- Ruta de ingreso-egreso-reingreso.
- Criterios de elegibilidad y exclusión.
- Matriz de riesgos y mitigaciones.
- Tablero de capacidad y seguridad.
- Plan de implementación o mejora HODOM.

## Compromisos

- Seguridad alta: las transiciones y el domicilio concentran riesgo.
- Equidad alta: la HD puede ampliar acceso o profundizar inequidad territorial
  si se implementa mal.
- Transparencia alta: citar corpus, supuestos y vacíos.
- Responsabilidad alta: el responsable humano siempre queda explícito.
