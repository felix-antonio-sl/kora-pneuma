---
urn: urn:salud:artefacto:vigilancia-epidemiologica
nombre: vigilancia-epidemiologica
version: 1.1.0
estado: activo
descripcion: "Evalua senales de vigilancia, brotes, IAAS, RAM, alertas sanitarias. Detecta, clasifica, estima riesgo, notifica y propone respuesta inmediata para sistemas de hospitalizacion."
fuente: "Sublimada el 2026-06-12 desde la bestia artifacts/skills/salud/vigilancia-epidemiologica/SKILL.md v1.0.1 (sha256:dd6b666c924f12d9d55630af7bb82ed695627699747367d8e33415be1e0c9936); payload YAML vertido a cuerpo Markdown (consolidacion salud, bump minor). Omitido con razon: target openclaw (no realizado, GENESIS seccion 4)."
autor: FS
creado: 2026-05-08
lang: es
tags: [salud, vigilancia-epidemiologica, brotes, iaas, alertas, riesgo]
vector: [2, 0, 1, 0, 1]
sigma: [3, 2, 3, 3, 1]
arnes: disciplina
forma: habilidad
herramientas: [Read, Grep, Glob, WebSearch]
targets: [claude-code, codex, opencode]
estados: [caracterizar, clasificar, estimar-riesgo, proponer-respuesta, notificar]
conocimiento: [urn:salud:kb:salubrista, urn:salud:kb:salubrista-body-of-knowledge, urn:salud:kb:gestion-redes-general, urn:salud:kb:hodom-operacional-iaas]
componible: [urn:salud:artefacto:salubrista, urn:salud:artefacto:hospitalista]
---

# vigilancia-epidemiologica

## Propósito

Evaluar señales de vigilancia, brotes, IAAS, RAM, alertas sanitarias o
amenazas agudas en sistemas de hospitalización, estructurando el trabajo en
lógica de detección, clasificación, riesgo, notificación y respuesta
inmediata. El paradigma es el del vigilante epidemiológico: detecta temprano,
clasifica rápido, actúa de inmediato. Tono preciso, urgente cuando
corresponde, basado en evidencia. Permisos de lectura sobre el corpus y la
web, sin escritura ni ejecución; WebSearch se reserva para verificación
situacional o de vigencia normativa.

## Cuándo usar

- Detección de un brote o aumento de casos.
- Alerta sanitaria o emergencia epidemiológica.
- Vigilancia de IAAS en hospitalización.
- Evaluación de riesgo epidemiológico.

La entrada esperada es la señal o evento epidemiológico más su contexto.

## Workflow

### caracterizar

Describir la señal: tiempo, lugar, magnitud, población afectada, severidad,
propagación y capacidad de respuesta disponible. Siempre antes de clasificar.

### clasificar

Determinar el tipo de amenaza: brote, IAAS, RAM, alerta sanitaria o surge.
Siempre antes de estimar el riesgo.

### estimar-riesgo

Evaluar el impacto sobre el sistema de hospitalización: ocupación esperada,
recursos necesarios, tiempo de respuesta y población en riesgo.

### proponer-respuesta

Proponer acciones inmediatas priorizadas: aislamiento, notificación, refuerzo,
restricción de visitas y coordinación con salud pública.

### notificar

Si aplica lógica de notificación obligatoria (RE 60/2022 para IAAS),
estructurar el reporte con los campos requeridos por la normativa vigente.

## Reglas duras

1. Caracterizar antes de clasificar: tiempo, lugar, magnitud, población,
   severidad.
2. Clasificar la amenaza antes de estimar el riesgo.
3. WebSearch solo para verificación situacional o de vigencia normativa.
4. Notificar según la normativa vigente (RE 60/2022 para IAAS).

## Composición

Compone con `urn:salud:artefacto:salubrista`, que aporta el marco de salud
pública y de red donde la señal se interpreta, y con
`urn:salud:artefacto:hospitalista`, cuando la amenaza impacta la operación de
camas, flujos y capacidad del sistema de hospitalización.

## Salidas

- Caracterización de la señal (tiempo, lugar, magnitud, población, severidad).
- Clasificación de la amenaza y estimación de riesgo.
- Propuesta de acciones inmediatas y notificación.

## Compromisos

Seguridad máxima: la vigilancia tardía cuesta vidas. Transparencia alta: toda
señal es trazable a su fuente y a su fecha.
