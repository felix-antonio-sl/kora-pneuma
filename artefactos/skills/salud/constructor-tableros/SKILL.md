---
urn: urn:salud:artefacto:constructor-tableros
nombre: constructor-tableros
version: 1.1.0
estado: deprecado
descripcion: "Construye artefactos estructurados de apoyo a decision: mapas de brechas, mapas de riesgo, dashboards, policy briefs, escenarios."
fuente: "Sublimada el 2026-06-12 desde la bestia artifacts/skills/salud/constructor-tableros/SKILL.md v1.0.1 (sha256:66566651cefa33ed8d4ce74e29682a521363c91f0a47bb0ec76db2c135db47f5); payload YAML vertido a cuerpo Markdown (consolidacion salud, bump minor). Omitido con razon: target openclaw (no realizado, GENESIS seccion 4)."
autor: FS
creado: 2026-05-08
lang: es
tags: [salud, tableros, decision-support, dashboards, policy-brief, escenarios]
vector: [2, 0, 1, 0, 1]
sigma: [2, 1, 3, 2, 1]
arnes: disciplina
forma: habilidad
herramientas: [Read, Grep, Glob]
targets: [claude-code, codex, opencode]
estados: [iniciar, procesar, entregar]
conocimiento: [urn:salud:kb:salubrista, urn:salud:kb:gestion-redes-herramientas, urn:salud:kb:hodom-operacional-indicadores]
componible: [urn:salud:artefacto:salubrista]
---

# constructor-tableros

## Propósito

Construir artefactos estructurados de apoyo a decisión en salud. Los productos
que domina son: mapa de brechas (gap map), mapa de riesgo (risk map), dashboard
de monitoreo, policy brief y escenarios de decisión. Es una skill operativa
portada desde OpenClaw, con tono técnico y estructurado, y permisos de solo
lectura sobre el corpus.

## Cuándo usar

Cuando se necesita convertir un análisis acumulado en un producto estructurado
de apoyo a decisión: visualizar brechas o riesgos, montar un tablero de
monitoreo, redactar un policy brief o plantear escenarios para una decisión.
La entrada esperada es la solicitud más su contexto.

## Workflow

### iniciar

Recibir el análisis acumulado del dominio correspondiente —el insumo sobre el
que se construirá el producto— e identificar la audiencia: quién usará el
producto y qué decisión debe tomar con él.

### procesar

Construir el producto (mapa de brechas, mapa de riesgo, dashboard, policy
brief o escenarios) con trazabilidad, supuestos explícitos y criterio de uso.

### entregar

Entregar el producto estructurado declarando sus límites: qué muestra, qué no
muestra y cómo debe interpretarse.

## Reglas duras

1. Corpus KORA primero.

## Composición

Compone con `urn:salud:artefacto:salubrista`: el salubrista produce el análisis
de dominio y esta skill lo convierte en el artefacto de decisión que la
audiencia necesita.

## Salidas

Producto estructurado de apoyo a decisión (gap map, risk map, dashboard de
monitoreo, policy brief o escenarios), con trazabilidad, supuestos y límites
declarados.

## Compromisos

Transparencia alta: todo producto declara sus fuentes, supuestos y límites de
interpretación.
