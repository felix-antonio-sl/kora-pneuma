---
urn: urn:salud:artefacto:vigilancia-epidemiologica
nombre: vigilancia-epidemiologica
version: 1.2.0
estado: activo
descripcion: "Evalua senales de vigilancia, brotes, IAAS, RAM, alertas sanitarias. Detecta, clasifica, estima riesgo, notifica y propone respuesta inmediata para sistemas de hospitalizacion."
fuente: "Sublimada el 2026-06-12 desde la bestia artifacts/skills/salud/vigilancia-epidemiologica/SKILL.md v1.0.1 (sha256:dd6b666c924f12d9d55630af7bb82ed695627699747367d8e33415be1e0c9936); payload YAML vertido a cuerpo Markdown (consolidacion salud, bump minor). Omitido con razon: target openclaw (no realizado, GENESIS seccion 4). v1.2.0 (2026-06-22): inyeccion de umbrales/criterios operables (evaluacion funcional) — definiciones de caso (sospechoso/probable/confirmado), criterios cuantitativos de brote (incl. IAAS sobre linea de base, tasa de ataque) y campos del formulario de notificacion obligatoria; anclado en RE 60/2022 (citada en urn:salud:kb:hodom-operacional-iaas) y en epidemiologia de campo estandar. Los criterios especificos por evento, plazos y campos oficiales (definiciones ENO, articulado RE 60/2022 no cargado como KB) quedan marcados {{verificar}} para el operador."
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

#### Definiciones de caso (clasificación cuantitativa)

Toda clasificación de un caso individual usa la escala estándar de vigilancia.
Estas son las definiciones genéricas; la definición operativa específica de cada
evento (criterios clínicos, de laboratorio y de nexo epidemiológico exactos) la
fija la circular/protocolo MINSAL vigente para ese agente y debe verificarse
antes de aplicarla:

- **Caso sospechoso**: cuadro clínico compatible con la definición del evento,
  sin confirmación de laboratorio ni nexo epidemiológico establecido.
- **Caso probable**: caso sospechoso CON nexo epidemiológico (contacto con caso
  confirmado, exposición común) o con prueba de laboratorio sugerente pero no
  confirmatoria.
- **Caso confirmado**: caso con confirmación de laboratorio por la técnica de
  referencia del evento (cultivo, PCR, serología pareada, etc.), independiente
  de la clínica.

{{verificar: los criterios clínicos, de laboratorio y de tiempo de cada
definición de caso dependen del evento específico y de la circular MINSAL
vigente (p. ej. circular de vigilancia de IRA grave, definiciones ENO). No
aplicar una definición de caso sin contrastarla con el protocolo vigente del
agente bajo vigilancia.}}

#### Criterios cuantitativos de brote

Umbrales para declarar conglomerado/brote (epidemiología de campo estándar;
ajustar al evento y al denominador local):

- **Brote en general**: dos o más casos epidemiológicamente relacionados
  (mismo tiempo, lugar y exposición) por encima de lo esperado. Para eventos
  de notificación inmediata, **un solo caso confirmado** puede constituir alerta
  (sarampión, cólera, enfermedad de declaración obligatoria inmediata).
- **IAAS — brote**: aumento de casos de una infección por sobre la línea de base
  (endemia) de la unidad, o agrupación inusual en tiempo/lugar (misma sala,
  mismo dispositivo, mismo microorganismo), o aparición de un microorganismo
  epidemiológicamente significativo (p. ej. multirresistente). {{verificar: la
  línea de base se calcula con la tasa histórica de la unidad; fijar el umbral
  (p. ej. tasa observada > media + 2 DE, o > percentil esperado) con el programa
  IAAS local.}}
- **Tasa de ataque** = casos / población expuesta × 100 — cuantifica la magnitud
  y orienta la búsqueda de la fuente.
- **IAAS — indicadores de vigilancia continua** (urn:salud:kb:hodom-operacional-iaas):
  tasa de flebitis, ITU asociada a sonda, infección de herida, neumonía asociada
  a VNI; en HaH la referencia es IAAS domiciliarias < 0.5 × 1000 días-estada
  (urn:salud:kb:gestion-redes-general / herramientas). Superar la línea de base
  de cualquiera de estos dispara la señal.

### estimar-riesgo

Evaluar el impacto sobre el sistema de hospitalización: ocupación esperada,
recursos necesarios, tiempo de respuesta y población en riesgo.

### proponer-respuesta

Proponer acciones inmediatas priorizadas: aislamiento, notificación, refuerzo,
restricción de visitas y coordinación con salud pública.

### notificar

Si aplica lógica de notificación obligatoria (RE 60/2022 para IAAS,
urn:salud:kb:hodom-operacional-iaas; régimen ENO para enfermedades de
notificación obligatoria), estructurar el reporte con los campos requeridos por
la normativa vigente.

**Oportunidad de la notificación.** Distinguir la urgencia según el evento:

- **Notificación inmediata** (vía más rápida disponible, dentro de 24 h):
  eventos de alerta — brote, evento inusual, agente de declaración inmediata.
- **Notificación diaria/semanal**: eventos de vigilancia regular según el
  calendario del evento.

{{verificar: el plazo exacto (inmediato vs. diario vs. semanal) y la vía
(electrónica/telefónica) los fija la normativa ENO y la RE 60/2022 vigentes
para cada evento; confirmar antes de comprometer un plazo.}}

**Campos del formulario de notificación.** Estructurar el reporte con, al menos:

1. **Identificación del paciente**: nombre, RUT/identificador, edad/fecha de
   nacimiento, sexo, domicilio y previsión.
2. **Establecimiento notificador** y profesional responsable (nombre, cargo,
   contacto).
3. **Evento/diagnóstico** notificado y su clasificación (sospechoso / probable /
   confirmado).
4. **Fechas clave**: inicio de síntomas, consulta, hospitalización,
   diagnóstico/confirmación, notificación.
5. **Datos clínicos**: cuadro clínico, gravedad, condición (vivo/fallecido),
   factores de riesgo y antecedentes relevantes.
6. **Laboratorio**: muestra tomada, técnica, resultado y fecha.
7. **Nexo epidemiológico**: contactos, exposición común, conglomerado, viajes.
8. **En IAAS**: tipo de infección, dispositivo asociado, microorganismo y
   patrón de resistencia, unidad/servicio, días-dispositivo.

{{verificar: el set exacto y obligatorio de campos lo define el formulario
oficial vigente (ENO MINSAL; reporte al programa IAAS del hospital según RE
60/2022). La RE 60/2022 está citada como marco en el corpus pero su articulado
no está cargado como KB — confirmar los campos contra el formulario oficial
antes de usarlo como definitivo.}}

## Reglas duras

1. Caracterizar antes de clasificar: tiempo, lugar, magnitud, población,
   severidad.
2. Clasificar la amenaza antes de estimar el riesgo, usando las definiciones de
   caso (sospechoso / probable / confirmado) y los criterios cuantitativos de
   brote. La definición de caso específica del evento se verifica contra la
   circular/protocolo MINSAL vigente antes de aplicarla.
3. WebSearch solo para verificación situacional o de vigencia normativa.
4. Notificar según la normativa vigente (RE 60/2022 para IAAS; régimen ENO),
   respetando la oportunidad (inmediata vs. regular) y los campos del formulario
   oficial. Un número clínico, una definición de caso o un plazo que no se pueda
   fundar en la normativa vigente se marca {{verificar}}, nunca se afirma.

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
