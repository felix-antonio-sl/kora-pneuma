---
urn: urn:salud:artefacto:analista-redes
nombre: analista-redes
version: 1.1.0
estado: deprecado
descripcion: "Analiza o disena unidades, establecimientos, redes, modelos territoriales, flujos, capacidad, accesibilidad y gobernanza en sistemas de salud."
fuente: "Sublimada el 2026-06-12 desde la bestia artifacts/skills/salud/analista-redes/SKILL.md v1.0.1 (sha256:18e7b6e3a41191c782a794fc8f3c679afb5312809762b4768330cd28f11391ea); payload YAML vertido a cuerpo Markdown (consolidacion salud, bump minor). Omitido con razon: target openclaw (no realizado, GENESIS seccion 4)."
autor: FS
creado: 2026-05-08
lang: es
tags: [salud, redes-asistenciales, capacidad, accesibilidad, gobernanza, diseno-de-unidades]
vector: [2, 0, 1, 0, 1]
sigma: [2, 1, 3, 2, 1]
arnes: disciplina
forma: habilidad
herramientas: [Read, Grep, Glob]
targets: [claude-code, codex, opencode]
estados: [iniciar, procesar, entregar]
conocimiento: [urn:salud:kb:salubrista, urn:salud:kb:gestion-redes-general, urn:salud:kb:gestion-redes-unidades, urn:salud:kb:gestion-redes-urgencias, urn:salud:kb:health-systems-science-operativa, urn:salud:kb:management-engineering-ext-capacidad]
componible: [urn:salud:artefacto:salubrista]
---

# analista-redes

## Propósito

Analizar o diseñar unidades, establecimientos, redes asistenciales, modelos
territoriales, flujos, capacidad, accesibilidad y gobernanza en sistemas de
salud. Opera en dos modos: **análisis** (mapear lo existente) y **diseño**
(definir arquitectura nueva). Es una skill operativa portada desde OpenClaw,
con tono técnico y estructurado, y permisos de solo lectura sobre el corpus de
conocimiento.

## Cuándo usar

Ante cualquier solicitud de análisis o diseño de redes asistenciales: estudiar
una unidad o establecimiento, mapear una red o un modelo territorial, evaluar
flujos, capacidad o accesibilidad, o definir la gobernanza de un sistema de
salud. La entrada esperada es la solicitud más su contexto.

## Workflow

### iniciar

Recibir la solicitud y su contexto. Posicionar la escala de trabajo —unidad,
establecimiento, red o territorio— y determinar el modo de operación: análisis
o diseño.

### procesar

En modo análisis: mapear demanda, oferta, capacidad, flujos, cuellos de botella
y brechas. En modo diseño: definir la arquitectura de la red —nodos, roles,
niveles de complejidad, reglas de derivación y gobernanza.

### entregar

Producir el producto estructurado con recomendaciones acompañadas de KPIs.
Los tradeoffs deben quedar explícitos: eficiencia vs equidad vs resiliencia.

## Reglas duras

1. Corpus KORA primero.

## Composición

Compone con `urn:salud:artefacto:salubrista`: el salubrista la invoca como
capacidad especializada de análisis y diseño de redes dentro de trabajos
sanitarios más amplios.

## Salidas

Producto estructurado de análisis o diseño de red (mapa de situación o
arquitectura propuesta, con KPIs y tradeoffs explícitos).

## Compromisos

Transparencia alta: el razonamiento y las recomendaciones son trazables.
