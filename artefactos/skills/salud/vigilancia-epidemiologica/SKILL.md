---
urn: urn:salud:artefacto:vigilancia-epidemiologica
nombre: vigilancia-epidemiologica
version: 1.2.1
estado: activo
descripcion: "Evalua senales de vigilancia, brotes, IAAS, RAM, alertas sanitarias. Detecta, clasifica, estima riesgo, notifica y propone respuesta inmediata para sistemas de hospitalizacion."
fuente: "Sublimada el 2026-06-12 desde la bestia artifacts/skills/salud/vigilancia-epidemiologica/SKILL.md v1.0.1 (sha256:dd6b666c924f12d9d55630af7bb82ed695627699747367d8e33415be1e0c9936); payload YAML vertido a cuerpo Markdown (consolidacion salud, bump minor). Omitido con razon: target openclaw (no realizado, GENESIS seccion 4). v1.2.0 (2026-06-22): inyeccion de umbrales/criterios operables (evaluacion funcional) — definiciones de caso (sospechoso/probable/confirmado), criterios cuantitativos de brote (incl. IAAS sobre linea de base, tasa de ataque) y campos del formulario de notificacion obligatoria; anclado en RE 60/2022 (citada en urn:salud:kb:hodom-operacional-iaas) y en epidemiologia de campo estandar. Los criterios especificos por evento, plazos y campos oficiales (definiciones ENO, articulado RE 60/2022 no cargado como KB) quedan marcados {{verificar}} para el operador. v1.2.1 (2026-06-22): cierra los {{verificar}} anclando a urn:salud:kb:notificacion-eno-iaas (sintesis de fuentes oficiales verificadas: BCN/LeyChile, MINSAL); CORRIGE la cita 'RE 60/2022' — el reglamento ENO vigente es el Decreto 7/2019 (deroga DS 158/2004) y la norma IAAS es el Decreto Exento 60/2022 que aprueba la Norma Tecnica 225 (deroga NT 124); la incertidumbre irreducible (definiciones de caso por evento, que viven en circulares por enfermedad) queda como referencia grounded al KB, no como placeholder."
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
conocimiento: [urn:salud:kb:salubrista, urn:salud:kb:salubrista-body-of-knowledge, urn:salud:kb:gestion-redes-general, urn:salud:kb:hodom-operacional-iaas, urn:salud:kb:notificacion-eno-iaas]
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

> El **Decreto 7/2019 no define transversalmente** sospechoso/probable/confirmado:
> la definición operativa por evento (criterios clínicos, de laboratorio y de nexo)
> vive en la Norma Técnica/circular MINSAL de cada enfermedad. El marco normativo
> (modalidades, plazos, plataforma) está en `urn:salud:kb:notificacion-eno-iaas`;
> los criterios por agente se toman de su circular específica antes de aplicarlos.

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
  epidemiológicamente significativo (p. ej. multirresistente). Criterio **NT 225**
  (Decreto Exento 60/2022): casos por sobre ~el doble de lo esperado, acúmulos en
  tiempo/servicio, o aislamiento de patógeno específico/resistente. La línea de base
  es la tasa histórica de la unidad; el umbral estadístico (p. ej. > media + 2 DE) lo
  fija el programa IAAS (PCI) local.
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

Si aplica notificación obligatoria, estructurar el reporte según la normativa
vigente (`urn:salud:kb:notificacion-eno-iaas`): **ENO** por el **Decreto 7/2019**
(vía EPIVIGILA); **IAAS** por el **Decreto Exento 60/2022 (Norma Técnica 225)**
(reporte mensual a SICARS), con la regla puente: un **brote de IAAS escala a
notificación inmediata vía EPIVIGILA** (Decreto 7, Art. 1.d).

**Oportunidad de la notificación.** Distinguir la urgencia según el evento:

- **Inmediata** (Decreto 7/2019 Art. 1.a/1.d): ante sospecha, vía más expedita a la
  SEREMI; formalización en EPIVIGILA ≤ 24 h. Cubre los agentes de la lista inmediata
  y **todos los brotes**.
- **Dentro de 24 h** (Art. 1.b): ≤ 24 h desde confirmación/clasificación final.
- **Centinela semanal** (Art. 1.c): solo establecimientos centinela definidos por la SEREMI.
- **IAAS**: reporte **mensual** a SICARS (NT 225); el brote IAAS escala a inmediata vía EPIVIGILA.

La modalidad y el plazo por evento están tabulados en `urn:salud:kb:notificacion-eno-iaas`.

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

Los grupos de campos siguen el formulario **EPIVIGILA** (detalle en
`urn:salud:kb:notificacion-eno-iaas`). El **set exacto por cada ENO** lo fija la
Norma Técnica/circular de la enfermedad y el instructivo oficial de EPIVIGILA; en
IAAS, las definiciones e indicadores los fijan las circulares C37 (reporte a SICARS).
Tomar la lista de arriba como estructura, no como transcripción literal del
formulario oficial.

## Reglas duras

1. Caracterizar antes de clasificar: tiempo, lugar, magnitud, población,
   severidad.
2. Clasificar la amenaza antes de estimar el riesgo, usando las definiciones de
   caso (sospechoso / probable / confirmado) y los criterios cuantitativos de
   brote. La definición de caso específica del evento se verifica contra la
   circular/protocolo MINSAL vigente antes de aplicarla.
3. WebSearch solo para verificación situacional o de vigencia normativa.
4. Notificar según la normativa vigente (`urn:salud:kb:notificacion-eno-iaas`):
   **Decreto 7/2019** (ENO, EPIVIGILA) y **Decreto Exento 60/2022 / NT 225** (IAAS,
   SICARS), respetando la oportunidad (inmediata vs. regular) y los campos del
   formulario oficial. Un número clínico, una definición de caso o un plazo que no
   se pueda fundar en la normativa vigente se marca {{verificar}}, nunca se afirma.

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
