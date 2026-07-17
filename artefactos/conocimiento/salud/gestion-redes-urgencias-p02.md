---
urn: urn:salud:kb:gestion-redes-urgencias-p02
nombre: gestion-redes-urgencias-p02
version: 2.0.0
estado: publicado
descripcion: "Gestión de Redes Asistenciales — Red de Urgencias - Parte 02"
fuente: "Migrado de la bestia (~/kora @ 9de5dc38b78c23574d24a481a5f84d70173c2203) artifacts/knowledge/salud/salubrista/gestion-redes/03-urgencias--p02.md (sha256:6f33fb8bcb06fc276ce4e519a614a7f0ef25fc4b2df4f86c5cc81d89b53d728c) el 2026-07-17; cuerpo byte-fiel; frontmatter normalizado a ley/2; shard enlazado por cita a urn:salud:kb:gestion-redes-urgencias."
autor: FS
creado: 2026-03-03
lang: es
tags: [gestion-redes, urgencias, emergencias, EMS, SUH, protocolos, triaje, desastres, MCI]
familia: bok
cita: [urn:salud:kb:gestion-redes-urgencias, urn:salud:kb:gestion-redes-unidades]
---


# Gestión de Redes Asistenciales — Red de Urgencias - Parte 02

## 20.1 Pre-arribo y pre-notificación

Comunicación estandarizada entre EMS y SUH previo a la llegada del paciente. Permite activación anticipada de recursos y reducción de tiempos puerta-intervención.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Códigos de activación | Código IAM (STEMI), Código ACV, Código Trauma, Código Sepsis — cada uno con criterios de activación definidos |
| Canal de aviso | Radio dedicada, aplicación móvil, línea directa SUH — redundancia mínima 2 canales |
| Formato SBAR | Situation-Background-Assessment-Recommendation — estructura estandarizada de comunicación |
| Pre-activación equipo | Notificación automática a especialistas de guardia según código activado |
| Preparación box/sala | Equipamiento listo en box de reanimación o sala procedimientos según código |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tasa pre-notificación | Ingresos con pre-notificación / Total ingresos EMS × 100 | ≥90 % | — | Registros SUH | Mensual |
| Tiempo pre-aviso → llegada | Minutos entre pre-notificación y arribo ambulancia | ≥10 min | — | Registros EMS/SUH | Mensual |
| Activación código en pre-arribo | Códigos activados pre-arribo / Total códigos activados × 100 | ≥80 % | — | Registros SUH | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Sobre-activación de códigos (falsos positivos) | Auditoría concordancia código vs. diagnóstico final, feedback a EMS |
| Falla comunicación radio | Redundancia celular + radio, protocolos de contingencia |

Ref: AHA Mission: Lifeline 2023; NAEMSP Pre-notification Guidelines; Joint Commission NPSG.

## 20.2 Recepción y triaje (ESI/CTAS/MTS/SAT)

Clasificación estructurada de pacientes al ingreso del SUH mediante sistema validado de triaje en 5 niveles. Determina prioridad de atención, circuito asignado y tiempo máximo de espera.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| ESI (Emergency Severity Index) | 5 niveles basados en agudeza + recursos esperados; más usado en Chile |
| MTS (Manchester Triage System) | 5 niveles por flujogramas por queja principal + discriminadores |
| CTAS (Canadian Triage and Acuity Scale) | 5 niveles, queja principal + modificadores primer/segundo orden |
| SAT (Sistema de Atención de Triage) | Adaptación chilena MINSAL, compatible con ESI |
| Triaje electrónico | Soporte decisional informatizado, registro estructurado, timestamps automáticos |
| Re-evaluación | Protocolo de re-triaje según tiempos definidos por nivel |

**IF/THEN — Niveles ESI:**

| Nivel ESI | Condición | Acción | Tiempo máximo espera |
|-----------|-----------|--------|---------------------|
| IF ESI 1 (Resucitación) | Riesgo vital inminente: paro, shock, compromiso vía aérea | THEN atención inmediata en box reanimación | 0 min |
| IF ESI 2 (Emergencia) | Alto riesgo: dolor torácico, déficit neurológico, intoxicación grave | THEN atención prioritaria, monitorización continua | ≤10 min |
| IF ESI 3 (Urgencia) | Requiere ≥2 recursos, signos vitales estables pero alterados | THEN circuito estándar, evaluación completa | ≤30 min |
| IF ESI 4 (Menos urgente) | Requiere 1 recurso (laboratorio o imagen) | THEN fast track si disponible | ≤60 min |
| IF ESI 5 (No urgente) | No requiere recursos, consulta simple | THEN fast track, considerar derivación a APS | ≤120 min |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Door-to-triage | Mediana minutos ingreso → clasificación triaje | ≤10 min | ACEP: ≤5 min | ACEP 2023 | Mensual |
| Concordancia inter-evaluador triaje | Kappa de Cohen entre enfermeras de triaje | ≥0.70 | ESI validación ≥0.80 | Tanabe 2004 | Semestral |
| Sobre-triaje ESI 1-2 | % ESI 1-2 dados de alta sin intervención crítica / Total ESI 1-2 | ≤15 % | — | Auditoría clínica | Trimestral |
| Sub-triaje | Eventos adversos en pacientes clasificados ESI 4-5 / Total ESI 4-5 | ≤1 % | — | Registros seguridad | Trimestral |
| LWBS (Left Without Being Seen) | Pacientes que abandonan sin ser vistos / Total consultas SUH × 100 | ≤3 % | ACEP: ≤2 % | ACEP 2023 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Sub-triaje en adultos mayores (presentación atípica) | Protocolo geriátrico de triaje, discriminadores ajustados por edad |
| Sesgo en triaje (género, etnia, idioma) | Algoritmo estandarizado, auditoría de equidad, facilitador intercultural |

Ref: ESI Implementation Handbook v4 (AHRQ 2020); Manchester Triage Group 2014; NT Urgencia MINSAL; ACEP Policy Statement Triage 2023.

## 20.3 Circuitos (fast track, estándar, reanimación)

Diferenciación de flujos internos del SUH según severidad y tipo de atención requerida. Streaming clínico para optimizar tiempos y evitar contaminación cruzada de circuitos.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Circuito reanimación | ESI 1, box dedicado, equipo trauma/paro, acceso inmediato a imagenología y laboratorio |
| Circuito estándar | ESI 2-3, boxes de evaluación, acceso a diagnóstico completo |
| Fast track | ESI 4-5, atención rápida, médico dedicado, alta en ≤2h |
| Circuito pediátrico | Separación física, personal pediátrico, ambiente diferenciado |
| Circuito psiquiátrico | Espacio seguro, contención disponible, evaluación psiquiátrica dedicada |
| Sala de procedimientos menores | Suturas, drenajes, reducción fracturas simples — evita ocupar box estándar |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Estadía fast track | Mediana minutos ingreso → alta (ESI 4-5) | ≤120 min | UK NHS: ≤120 min | NHS England 2023 | Mensual |
| Estadía circuito estándar | Mediana minutos ingreso → decisión destino (ESI 2-3) | ≤240 min | ACEP: 240 min | ACEP 2023 | Mensual |
| Uso fast track | % consultas ESI 4-5 atendidas en fast track / Total ESI 4-5 | ≥80 % | — | EDIS | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Fast track colapsado por volumen | Límite WIP, derivación a SAPU, médico de refuerzo |
| Mezcla de circuitos por falta de espacio | Diseño físico con separación, señalética, protocolos de desborde |

Ref: ACEP Emergency Department Design Guidelines 2023; NHS Emergency Care Standard; Australasian College for Emergency Medicine 2022.

## 20.4 Diagnóstico y apoyo urgente

Servicios de apoyo diagnóstico con disponibilidad 24/7 para SUH. Laboratorio point-of-care, imagenología urgente y teleradiología para SUH sin radiólogo presencial.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Laboratorio POC (point-of-care) | Troponina, lactato, gasometría, hemoglucotest, βHCG — resultado ≤15 min |
| Laboratorio central urgente | Panel completo: hemograma, bioquímica, coagulación, toxicología |
| Radiología convencional 24/7 | Rx tórax/extremidades/abdomen disponible en SUH |
| TC urgente | Scanner dedicado o prioridad SUH, protocolo ACV/politrauma/TEP |
| Ecografía POCUS | Point-of-care ultrasound en box de reanimación (FAST, ecocardiograma) |
| Teleradiología | Lectura remota para SUH sin radiólogo presencial nocturno |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| TAT laboratorio POC | Mediana minutos solicitud → resultado disponible (troponina, lactato) | ≤15 min | CAP: ≤15 min POC | CAP 2023 | Mensual |
| TAT laboratorio central urgente | Mediana minutos solicitud → resultado panel básico | ≤45 min | — | LIS | Mensual |
| TAT TC urgente | Mediana minutos solicitud → informe preliminar | ≤30 min | NICE: ≤60 min trauma | NICE 2023 | Mensual |
| Disponibilidad POCUS | % turnos con operador POCUS certificado | ≥80 % | — | RRHH SUH | Mensual |
| TAT teleradiología nocturna | Mediana minutos envío imagen → informe preliminar | ≤30 min | — | RIS | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| TAT excesivo en laboratorio central | Tubo neumático, corredor dedicado, priorización muestras SUH |
| Falta POCUS nocturno | Capacitación cruzada médicos SUH, programa certificación POCUS |

Ref: CAP Point-of-Care Testing Guidelines 2023; ACR Appropriateness Criteria; ACEP Ultrasound Guidelines 2023.

## 20.5 Interconsultas y enlace

Gestión de interconsultas desde SUH a especialidades intrahospitalarias. SLA definidos por prioridad, sistemas de comunicación estandarizados y registro de tiempos.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| SLA interconsulta urgente | Respuesta especialista ≤30 min para ESI 1-2, ≤60 min ESI 3 |
| Sistema paging/código | Llamado directo a especialista de guardia, escalonamiento automático |
| eConsult | Consulta electrónica asincrónica para casos no urgentes, resolución sin presencia física |
| Handoff estructurado | SBAR para transferencia de información entre SUH y especialidad |
| Registro de tiempos | Timestamp solicitud → aceptación → presencia física → resolución |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo respuesta interconsulta urgente | Mediana minutos solicitud → presencia especialista (ESI 1-2) | ≤30 min | — | EDIS | Mensual |
| Cumplimiento SLA interconsulta | Interconsultas respondidas en plazo / Total × 100 | ≥90 % | — | EDIS | Mensual |
| Tasa eConsult resolutiva | eConsults resueltas sin presencia física / Total eConsults × 100 | ≥60 % | — | Sistema eConsult | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Especialista no responde en plazo | Escalonamiento automático a jefatura, registro de incumplimiento |
| Interconsulta innecesaria | Criterios de interconsulta explícitos, protocolos de manejo SUH |

Ref: ACEP Policy on Consultations 2022; Joint Commission Standard PC.02.02.01.

## 20.6 Observación de Corta Estadía (UOCS)

Unidad de observación con permanencia protocolizada ≤24h para pacientes que requieren evaluación seriada, tratamiento breve o espera de resultados antes de decisión de destino.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Criterios de ingreso | Dolor torácico bajo riesgo, crisis asmática, deshidratación, TEC leve, intoxicación leve |
| Criterios de exclusión | Necesidad de UCI, cirugía urgente, inestabilidad hemodinámica |
| Bundles UOCS | Evaluación seriada protocolizada por patología (ej. troponina seriada 0/3h) |
| Límite estadía | ≤24h; excedido → decisión formal (hospitalización o alta) |
| Criterios de egreso | Mejoría clínica, resultados negativos, plan de seguimiento ambulatorio |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Estadía UOCS | Mediana horas ingreso → egreso UOCS | ≤18h | ACEP: ≤24h | ACEP 2023 | Mensual |
| Tasa alta desde UOCS | Altas desde UOCS / Total ingresos UOCS × 100 | ≥70 % | — | EDIS | Mensual |
| Readmisión 72h post-UOCS | Reconsulta SUH ≤72h post-alta UOCS / Total altas UOCS × 100 | ≤5 % | — | EDIS | Mensual |
| Tasa conversión a hospitalización | Hospitalizados desde UOCS / Total ingresos UOCS × 100 | ≤30 % | — | EDIS | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| UOCS como "cama de boarding encubierta" | Auditoría de estadía, límite estricto 24h, dashboard en tiempo real |
| Alta prematura desde UOCS | Protocolos de egreso, control ambulatorio precoz, instrucciones claras |

Ref: ACEP Observation Medicine Section; American College of Observation Medicine 2022.

## 20.7 Decisión de destino

Punto de decisión crítico post-evaluación en SUH. Reglas explícitas para alta, hospitalización, traslado o derivación a hospitalización domiciliaria según condición clínica y disponibilidad de recursos.

**IF/THEN — Decisión de destino:**

| Condición | Destino | Criterio | Responsable |
|-----------|---------|----------|-------------|
| IF estable, diagnóstico cerrado, plan ambulatorio viable | THEN alta con instrucciones + control | Criterios de alta seguros, teach-back completado | Médico SUH |
| IF requiere monitoreo continuo, tratamiento IV, diagnóstico pendiente | THEN hospitalización (sala general o UTI/UCI según gravedad) | Criterios de ingreso por patología | Médico SUH + Bed manager |
| IF estable, requiere tratamiento ≤14 días, domicilio adecuado | THEN hospitalización domiciliaria (HaH) | Criterios inclusión HaH (→ `urn:salud:kb:gestion-redes-unidades` cap 17) | Coordinación HaH |
| IF requiere capacidad no disponible en SUH actual | THEN traslado a SUH de mayor complejidad | Protocolo derivación + coordinación Centro Regulador | Médico SUH + Centro Regulador |
| IF ESI 4-5 sin patología aguda | THEN derivación a APS/SAPU con hora garantizada ≤48h | Convenio red, disponibilidad confirmada | Médico SUH |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Bed management | Gestión centralizada camas: solicitud, asignación, liberación anticipada |
| Early discharge rounds | Ronda matinal de egresos tempranos para liberar camas antes de peak SUH |
| Dashboard ocupación | Visualización en tiempo real: camas libres por servicio, UCI/UTI, UOCS |
| Criterios explícitos por patología | Guías de ingreso/alta por condición (NAC, ICC, dolor torácico, etc.) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo decisión de destino | Mediana minutos ingreso SUH → decisión (alta/hospitalización/traslado) | ≤240 min | UK NHS: 4h target | NHS England 2023 | Mensual |
| Boarding time | Mediana minutos decisión hospitalización → salida SUH a cama | ≤60 min | ACEP: ≤60 min | ACEP 2023 | Mensual |
| Derivación HaH desde SUH | Pacientes derivados a HaH / Total hospitalizaciones × 100 | ≥10 % | — | EDIS + HaH | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Boarding prolongado por falta de camas | Early discharge, camas swing, escalamiento surge |
| Alta insegura por presión de flujo | Checklist de alta segura, criterios explícitos, re-evaluación si duda |

Ref: NHS 4-Hour Standard; ACEP Boarding Policy 2023; IHI Flow and Capacity Management.

## 21.1 Predicción de demanda

Modelos predictivos de afluencia al SUH para planificación de dotación, insumos y capacidad instalada. Variables: día de la semana, hora, estacionalidad, clima, eventos masivos y epidemias.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Series temporales | ARIMA, Prophet: predicción demanda diaria/horaria con estacionalidad |
| Variables exógenas | Temperatura, lluvia, festividades, eventos deportivos, brotes epidémicos |
| Segmentación por triaje | Predicción separada ESI 1-2 vs. ESI 3-5 (perfiles de demanda distintos) |
| Horizonte de predicción | Corto plazo (24-72h) para dotación, mediano plazo (3-6 meses) para planificación |
| Dashboard predictivo | Visualización demanda esperada vs. capacidad disponible por turno |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Error predicción demanda | MAPE (Mean Absolute Percentage Error) | ≤15 % | — | Modelo predictivo | Mensual |
| Cobertura del modelo | % turnos con predicción disponible | 100 % | — | Dashboard | Mensual |
| Ajuste dotación a demanda | Correlación dotación real vs. demanda predicha | r ≥0.80 | — | RRHH + Modelo | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Evento no anticipado (MCI, brote) | Protocolo surge independiente del modelo, capacidad de reserva |
| Modelo obsoleto | Reentrenamiento trimestral con datos actualizados |

Ref: Wargon et al. 2009 (ED demand forecasting); IHI Flow and Capacity; Jones 2009 (forecasting models).

## 21.2 Staff planning y turnos

Planificación de dotación y programación de turnos del equipo SUH alineada con demanda predicha, competencias requeridas y normativa laboral.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Skill mix | Proporción médicos emergenciólogos, médicos generales, enfermería, paramédicos por turno |
| Reglas de cobertura mínima | Mínimo por turno según volumen: ≥1 emergenciólogo, ≥2 enfermeras triaje, ≥1 POCUS |
| Turnos escalonados | Inicio de turnos desfasado para cubrir peaks (11:00-23:00 refuerzo) |
| Pool de refuerzo | Personal de reserva activable en ≤2h para surge |
| Normativa laboral | Ley 19.378 (APS), Código del Trabajo: descanso, jornada máxima, turnos nocturnos |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Ratio médico/consulta-hora | Consultas por hora / Médicos en turno | ≤2.5 pac/méd/hora | ACEP: 2.0-2.5 | ACEP 2023 | Mensual |
| Cobertura turnos críticos | Turnos con dotación completa / Turnos programados × 100 | ≥95 % | — | RRHH | Mensual |
| Horas extra no programadas | Horas extra / Horas totales × 100 | ≤10 % | — | RRHH | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Déficit crónico de emergenciólogos | Formación de especialistas, incentivos retención, telemedicina de apoyo |
| Fatiga por turnos extendidos | Límite jornada, descanso mínimo inter-turno, monitoreo bienestar |

Ref: ACEP Workforce Policy 2023; Código del Trabajo Chile; EUNACOM — requisitos formación emergencia.
