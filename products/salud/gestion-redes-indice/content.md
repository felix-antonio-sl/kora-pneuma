---
urn: urn:salud:kb:gestion-redes-indice
nombre: gestion-redes-indice
version: 2.0.1
estado: publicado
descripcion: "Gestión de Redes Asistenciales — Índice General: **Qué ES este corpus**: blueprint operativo para diseño, operación y mejora continua de redes y unidades asistenciales"
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/salud/salubrista/gestion-redes/00-indice.md (sha256:6b233275d51c8a951b0ed6aabddc85e159e321d61f99fbffdad508685b1e7e18) el 2026-06-12; cuerpo byte-fiel (renombrado de 00-indice.md a gestion-redes-indice.md por lugar-coincide). Fuente original: Síntesis multi-fuente: OPS, IHI, NICE, AHRQ, MINSAL, Cochrane, NotebookLM 46 fuentes HaH. Corrección normativa 2026-07-17 verificada contra BCN/LeyChile: DS 140/2004 idNorma=237231 y DS 15/2007 idNorma=262240."
autor: FS
creado: 2026-03-03
lang: es
tags: [gestion-redes, asistencial, indice, glosario, normativa, kpi, blueprint]
familia: bok
cita: [urn:salud:kb:gestion-redes-general, urn:salud:kb:gestion-redes-herramientas, urn:salud:kb:gestion-redes-salud-mental, urn:salud:kb:gestion-redes-unidades, urn:salud:kb:gestion-redes-urgencias]
---


# Gestión de Redes Asistenciales — Índice General

## 1. Propósito y alcance

**Qué ES este corpus**: blueprint operativo para diseño, operación y mejora continua de redes y unidades asistenciales. Orientado a decisiones de gestión, no a ejecución clínica.

**Qué NO es**: no es manual de procedimientos clínicos, no constituye texto normativo vinculante, no reemplaza guías clínicas GES/AUGE ni protocolos locales.

**Cobertura**:

| Dominio | Alcance |
|---------|---------|
| Gestión general de redes | Gobernanza, procesos, calidad, transformación digital, finanzas, gestión del cambio |
| Unidades asistenciales | Ambulatorias (APS/CESFAM), hospitalarias (agudos/UCI), hospitalización domiciliaria (HaH) |
| Red de urgencias | EMS, SUH, protocolos tiempo-dependientes, triage, desastres/MCI |
| Salud mental | Continuidad, crisis, TUS, derechos, rehabilitación comunitaria |
| Herramientas/anexos | KPIs, BPMN, plantillas, FHIR, simulación, modelo de madurez |

**Audiencia**:

| Rol | Uso esperado |
|-----|--------------|
| Alta dirección / Dirección de Servicio | Gobernanza, planificación estratégica, asignación de recursos |
| Direcciones de establecimiento | Operación de unidades, gestión de camas, calidad |
| Jefaturas de unidad | Procesos clínico-operativos, KPIs, dotación |
| PMO / Equipos de mejora | BPMN, PDSA, OKR, simulación |
| Equipos clínico-operativos | Protocolos, triage, flujos, bundles |
| TI / Interoperabilidad | FHIR, HL7, HCE, integraciones |

**Principio rector**: Cuádruple Meta (Quadruple Aim) — experiencia del paciente, salud poblacional, costo per cápita, bienestar del equipo clínico.

**Modelo conceptual subyacente**:

| Nivel | Foco | Artefactos corpus |
|-------|------|--------------------|
| Macro (red/sistema) | Gobernanza, asignación recursos, regulación | Cap. 1–5 |
| Meso (establecimiento) | Procesos transversales, calidad, digital, RRHH | Cap. 6–14 |
| Micro (unidad/servicio) | Operación clínico-asistencial por tipo | Cap. 15–36 |
| Instrumentos | Herramientas, plantillas, modelos | Anexos A–K |

## 2. Mapa del corpus

### 2.1 Archivos y dominios

| Archivo | URN | Capítulos | Dominio | Audiencia primaria |
|---------|-----|-----------|---------|--------------------|
| `00-indice.md` | `urn:salud:kb:gestion-redes-indice` | — | Índice, glosario, normativa, contextualización | Todos |
| `01-gestion-redes-general.md` | `urn:salud:kb:gestion-redes-general` | 1–14 | Framework general: gobernanza, procesos, calidad, digital, finanzas, cambio | Alta dirección, PMO, jefaturas |
| `02-unidades-asistenciales.md` | `urn:salud:kb:gestion-redes-unidades` | 15–17 | Gestión por tipo de unidad: ambulatorias, hospitalarias, HaH | Direcciones de establecimiento, jefaturas de unidad |
| `03-urgencias.md` | `urn:salud:kb:gestion-redes-urgencias` | 18–26 | Red de urgencias: EMS, SUH, protocolos tiempo-dependientes, desastres | Jefaturas SUH, EMS, equipos clínicos |
| `04-salud-mental.md` | `urn:salud:kb:gestion-redes-salud-mental` | 27–36 | Red de salud mental: continuidad, crisis, TUS, derechos | Direcciones SM, equipos comunitarios, COSAM |
| `05-herramientas-anexos.md` | `urn:salud:kb:gestion-redes-herramientas` | Anexos A–K | KPIs, BPMN, plantillas, FHIR, simulación, modelo de madurez | PMO, TI, equipos de mejora |

### 2.2 Índice de capítulos detallado

| # | Título capítulo | Archivo | Dominio macro |
|---|----------------|---------|---------------|
| 1 | Gobernanza de red | 01 | Macro |
| 2 | Modelo de atención integrado | 01 | Macro |
| 3 | Gestión por procesos | 01 | Meso |
| 4 | Calidad y seguridad del paciente | 01 | Meso |
| 5 | Indicadores y tableros de control | 01 | Meso |
| 6 | Transformación digital | 01 | Meso |
| 7 | Gestión de RRHH en salud | 01 | Meso |
| 8 | Gestión financiera y costos | 01 | Meso |
| 9 | Abastecimiento y logística | 01 | Meso |
| 10 | Gestión farmacéutica | 01 | Meso |
| 11 | Infraestructura y equipamiento | 01 | Meso |
| 12 | Participación usuario y comunidad | 01 | Macro |
| 13 | Gestión del cambio organizacional | 01 | Meso |
| 14 | Investigación y docencia en red | 01 | Meso |
| 15 | Unidades ambulatorias (APS/CESFAM) | 02 | Micro |
| 16 | Unidades hospitalarias (agudos/UCI) | 02 | Micro |
| 17 | Hospitalización domiciliaria (HaH) | 02 | Micro |
| 18 | Diseño de red de urgencia | 03 | Macro |
| 19 | Sistema EMS/SAMU prehospitalario | 03 | Micro |
| 20 | Triage estructurado (ESI) | 03 | Micro |
| 21 | Protocolos tiempo-dependientes: ACV | 03 | Micro |
| 22 | Protocolos tiempo-dependientes: SCA | 03 | Micro |
| 23 | Protocolos tiempo-dependientes: Sepsis/Trauma | 03 | Micro |
| 24 | Gestión de flujo SUH | 03 | Micro |
| 25 | Boarding y overcrowding | 03 | Micro |
| 26 | MCI y desastres | 03 | Micro |
| 27 | Modelo comunitario SM | 04 | Macro |
| 28 | Red dispositivos SM | 04 | Macro |
| 29 | Continuidad de cuidados SM | 04 | Meso |
| 30 | Intervención en crisis SM | 04 | Micro |
| 31 | TUS: trastornos uso de sustancias | 04 | Micro |
| 32 | SM infanto-juvenil | 04 | Micro |
| 33 | SM adulto mayor | 04 | Micro |
| 34 | Rehabilitación psicosocial | 04 | Micro |
| 35 | Derechos y legislación SM | 04 | Macro |
| 36 | Indicadores y evaluación SM | 04 | Meso |

### 2.3 Navegación

**Referencia cruzada inter-archivo**: `→ urn:salud:kb:gestion-redes-urgencias §22` apunta al capítulo 22 de urgencias.

**Estructura interna de capítulos** (uniforme en todo el corpus):

| Sección | Contenido |
|---------|-----------|
| Encabezado `### N.X` | Título telegráfico del capítulo |
| Párrafo propósito | 1–3 líneas: qué resuelve, a quién sirve |
| Tabla componentes | Elementos del dominio: definición, función, responsable |
| Tabla IF/THEN | Reglas condicionales operativas |
| Tabla KPI | Indicadores con fórmula, meta, benchmark, fuente, periodicidad |
| Tabla riesgos | Riesgo → mitigación |
| Bloque Ref | Normativa CL + guideline internacional + estándar acreditación |

## 3. Leyenda de formato

Convenciones uniformes en todo el corpus:

### 3.1 Tipos de tabla

| Tipo tabla | Columnas | Propósito |
|------------|----------|-----------|
| Componentes | `Componente \| Definición \| Función \| Responsable` | Describir elementos de un dominio |
| KPI (6 cols) | `Indicador \| Fórmula \| Meta \| Benchmark \| Fuente \| Periodicidad` | Medir desempeño cuantitativo |
| IF/THEN | `Condición → Acción → Base` | Codificar reglas decisionales operativas |
| Riesgos | `Riesgo → Mitigación` | Anticipar y gestionar amenazas |
| Comparación | `Criterio \| Opción A \| Opción B \| ...` | Contrastar alternativas |
| Normativa | `Norma \| Tipo \| Alcance \| Capítulos \| Vigencia` | Trazabilidad regulatoria |

### 3.2 Convenciones de escritura

| Convención | Regla |
|------------|-------|
| Densidad | Telegráfico: máxima información por palabra. Sin relleno |
| Prioridad RFC 2119 | DEBE, NO DEBE, DEBERÍA, PUEDE — solo en contexto prescriptivo |
| Referencia cruzada | Formato: URN + sección (ej: `urn:salud:kb:gestion-redes-urgencias` §22) |
| Benchmarks | Fuente + año entre paréntesis: `(IHI, 2023)`, `(MINSAL, 2024)` |
| Unidades | SI + estándares salud: %, ‰, por 1.000 egresos, por 1.000 días-cama |
| Periodicidad KPI | mensual / trimestral / semestral / anual |
| Estado indicador | ✓ cumple / ⚠ alerta / ✗ crítico — umbrales definidos por KPI |

### 3.3 Bloque Ref (ejemplo tipo)

```
**Ref**: Ley 19.937 art. 4 · DS 4/2009 título III · NT Acreditación ámbito Gestión Clínica ·
IHI White Paper (2019) · NICE CG-XXX (2022) · Joint Commission IPSG.3
```

Cada bloque Ref combina: normativa chilena + guideline internacional + estándar acreditación. Mínimo 1 fuente por categoría.

## 4. Glosario y acrónimos

| Término / Acrónimo | Definición telegráfica |
|---------------------|------------------------|
| ACA | Atención Centrada en el Adulto mayor — enfoque geriátrico integral |
| ACLS | Advanced Cardiovascular Life Support — protocolo reanimación avanzada adultos |
| ACV | Accidente Cerebrovascular — evento cerebrovascular agudo (isquémico o hemorrágico) |
| AHRQ | Agency for Healthcare Research and Quality — agencia federal EE.UU. calidad/seguridad |
| APACHE | Acute Physiology And Chronic Health Evaluation — score severidad UCI |
| APS | Atención Primaria de Salud — primer nivel de contacto red asistencial |
| ATLS | Advanced Trauma Life Support — protocolo manejo avanzado de trauma |
| BCP | Business Continuity Plan — plan de continuidad operacional ante disrupciones |
| BIA | Business Impact Analysis — análisis de impacto al negocio para priorización BCP |
| BPMN | Business Process Model and Notation — notación estándar modelado de procesos |
| BSC | Balanced Scorecard — cuadro de mando integral (4 perspectivas) |
| Bundle | Conjunto de intervenciones basadas en evidencia aplicadas conjuntamente (IHI) |
| Burnout | Síndrome de agotamiento profesional — desgaste laboral crónico equipo salud |
| CAE | Centro de Atención de Especialidades — dispositivo ambulatorio secundario |
| CAUTI | Catheter-Associated Urinary Tract Infection — IAAS asociada a catéter urinario |
| CDT | Centro de Diagnóstico Terapéutico — unidad ambulatoria diagnóstica hospitalaria |
| CESFAM | Centro de Salud Familiar — establecimiento APS modelo integral |
| CLABSI | Central Line-Associated Bloodstream Infection — IAAS asociada a CVC |
| CMBD | Conjunto Mínimo Básico de Datos — dataset estandarizado alta hospitalaria |
| COMGES | Compromisos de Gestión — metas anuales entre MINSAL y Servicios de Salud |
| COSAM | Centro de Salud Mental Comunitaria — dispositivo ambulatorio SM |
| CRS | Código Rojo Sanitario — activación emergencia sanitaria masiva |
| C-SSRS | Columbia Suicide Severity Rating Scale — escala riesgo suicida estructurada |
| CVC | Catéter Venoso Central — acceso vascular invasivo central |
| DALY | Disability-Adjusted Life Year — años de vida ajustados por discapacidad |
| DEIS | Departamento de Estadísticas e Información en Salud — unidad MINSAL datos |
| DRG/GRD | Diagnosis Related Groups / Grupos Relacionados por Diagnóstico — clasificación casuística hospitalaria |
| DRP | Disaster Recovery Plan — plan recuperación TI post-desastre |
| EDIS | Emergency Department Information System — sistema información SUH |
| EHR/HCE | Electronic Health Record / Historia Clínica Electrónica |
| EMPI | Enterprise Master Patient Index — índice maestro de pacientes |
| EMS | Emergency Medical Services — sistema de atención médica prehospitalaria |
| ESI | Emergency Severity Index — sistema triage 5 niveles (1 = resucitación, 5 = no urgente) |
| Evento adverso | Daño no intencional al paciente asociado a la atención, no a la enfermedad |
| Evento centinela | Evento adverso grave, inesperado, que causa muerte o daño permanente |
| FHIR | Fast Healthcare Interoperability Resources — estándar interoperabilidad HL7 (REST/JSON) |
| FNDR | Fondo Nacional de Desarrollo Regional — instrumento inversión pública regional |
| FONASA | Fondo Nacional de Salud — seguro público de salud Chile |
| GAD-7 | Generalized Anxiety Disorder 7-item — escala tamizaje ansiedad |
| GES/AUGE | Garantías Explícitas en Salud — régimen garantías acceso/oportunidad/protección financiera/calidad |
| Gestión clínica | Prácticas para mejorar resultados en salud usando evidencia, estándares, medición |
| GRD | Ver DRG/GRD |
| HaH | Hospital at Home — hospitalización domiciliaria como alternativa a cama aguda |
| HCAHPS | Hospital Consumer Assessment of Healthcare Providers and Systems — encuesta PREM estandarizada EE.UU. |
| HCE | Ver EHR/HCE |
| HICS | Hospital Incident Command System — sistema mando incidentes hospitalarios |
| HL7 | Health Level Seven — familia estándares interoperabilidad en salud |
| HoNOS | Health of the Nation Outcome Scales — escala resultados SM (12 dimensiones) |
| IAAS | Infecciones Asociadas a la Atención de Salud — infecciones nosocomiales |
| ICC | Insuficiencia Cardíaca Congestiva — patología índice gestión crónica |
| ICS | Incident Command System — estructura mando estandarizada emergencias |
| IHI | Institute for Healthcare Improvement — referente mundial mejora continua salud |
| Índice ocupacional | % camas ocupadas vs. disponibles en período — indicador capacidad hospitalaria |
| IPC | Infección Prevención y Control — programa IAAS |
| IPR | Indicadores de Procesos y Resultados — sistema medición gestión sanitaria |
| ISAPRE | Institución de Salud Previsional — seguro privado de salud Chile |
| IVT | Intravenous Thrombolysis — trombolisis endovenosa (ACV isquémico, ventana ≤ 4.5 h) |
| KPI | Key Performance Indicator — indicador clave de desempeño |
| Lean | Metodología eliminación desperdicios (muda) en procesos — origen Toyota |
| LE | Lista de espera — pacientes pendientes de atención por prestación GES/no-GES |
| LIS | Laboratory Information System — sistema información laboratorio clínico |
| LOINC | Logical Observation Identifiers Names and Codes — nomenclatura universal observaciones clínicas |
| LWBS | Left Without Being Seen — pacientes que abandonan SUH sin atención |
| MCI | Mass Casualty Incident — incidente con víctimas en masa |
| mhGAP | Mental Health Gap Action Programme — programa OMS cierre brechas SM |
| MINSAL | Ministerio de Salud de Chile |
| Modelo comunitario SM | Paradigma atención SM centrado en comunidad, no institucional |
| NAC | Neumonía Adquirida en la Comunidad — patología índice urgencia/hospitalización |
| NICE | National Institute for Health and Care Excellence — agencia guías clínicas UK |
| NOC | Nursing Outcomes Classification — clasificación resultados enfermería |
| NSTEMI | Non-ST Elevation Myocardial Infarction — infarto sin elevación ST |
| OKR | Objectives and Key Results — marco gestión por objetivos y resultados clave |
| OPS | Organización Panamericana de la Salud — oficina regional OMS para las Américas |
| Overdiagnosis | Diagnóstico de condición que nunca habría causado síntomas ni daño |
| PACS | Picture Archiving and Communication System — sistema archivo/comunicación imágenes |
| PDSA | Plan-Do-Study-Act — ciclo mejora continua (Deming/IHI) |
| PHQ-9 | Patient Health Questionnaire 9-item — escala tamizaje/severidad depresión |
| PPV | Programa de Prestaciones Valoradas — mecanismo pago hospitalario FONASA |
| PREM | Patient-Reported Experience Measures — medidas experiencia reportada por paciente |
| PROM | Patient-Reported Outcome Measures — medidas resultado reportado por paciente |
| Promedio días estada | Días hospitalización total / egresos — indicador eficiencia hospitalaria |
| RCA | Root Cause Analysis — análisis causa raíz (eventos adversos) |
| Red asistencial | Conjunto articulado de establecimientos públicos bajo un Servicio de Salud |
| Referencia | Derivación de paciente desde un nivel de atención a otro de mayor complejidad |
| Contrarreferencia | Retorno de paciente al nivel de origen tras resolución o estabilización |
| RISAI | Redes Integradas de Servicios de Salud — modelo OPS redes asistenciales integradas |
| RIS | Radiology Information System — sistema información radiología |
| RPM | Remote Patient Monitoring — telemonitoreo domiciliario |
| RTO | Recovery Time Objective — tiempo máximo tolerable de indisponibilidad |
| RPO | Recovery Point Objective — pérdida máxima tolerable de datos |
| SAMU | Servicio de Atención Médica de Urgencia — EMS público Chile |
| SAPU | Servicio de Atención Primaria de Urgencia — urgencia de baja complejidad APS |
| SAR | Servicio de Atención de Urgencia Rural — punto urgencia rural |
| SDQ | Strengths and Difficulties Questionnaire — tamizaje SM infanto-juvenil |
| SEREMI | Secretaría Regional Ministerial de Salud — autoridad sanitaria regional |
| Six Sigma | Metodología reducción variabilidad procesos (≤ 3.4 defectos/millón) |
| SLA | Service Level Agreement — acuerdo nivel de servicio entre dispositivos de red |
| SNOMED CT | Systematized Nomenclature of Medicine — Clinical Terms — terminología clínica codificada |
| SOFA | Sequential Organ Failure Assessment — score disfunción orgánica (sepsis) |
| SSI | Surgical Site Infection — infección sitio quirúrgico |
| STEMI | ST-Elevation Myocardial Infarction — infarto con elevación ST (puerta-balón ≤ 90 min) |
| SUH | Servicio de Urgencia Hospitalaria — unidad de emergencia hospitalaria |
| TAT | Turnaround Time — tiempo respuesta (laboratorio, imagenología, farmacia) |
| Telemedicina | Prestación servicios salud a distancia mediante TIC |
| Triage | Clasificación pacientes por gravedad para priorizar atención |
| TUS | Trastorno por Uso de Sustancias — dependencia/abuso sustancias psicoactivas |
| UCI | Unidad de Cuidados Intensivos — unidad pacientes críticos |
| UOCS | Unidad Operativa de Control de Salud — unidad vigilancia epidemiológica local |
| UTI | Unidad de Tratamiento Intermedio — cuidados intermedios entre sala general y UCI |
| VAP | Ventilator-Associated Pneumonia — neumonía asociada a ventilación mecánica |
| VSM | Value Stream Mapping — mapeo cadena de valor (Lean) |
| WHO/OMS | World Health Organization / Organización Mundial de la Salud |

## 5. Marco normativo de referencia

### 5.1 Normativa chilena

| Norma | Tipo | Alcance | Capítulos impactados | Vigencia |
|-------|------|---------|----------------------|----------|
| Ley 19.937 (2004) | Ley | Autoridad Sanitaria, Gestión en Red y Garantías en Salud — crea SEREMI, Superintendencia, red asistencial | 1–14, 18–26 | Vigente (mod. 2023) |
| Ley 20.584 (2012) | Ley | Derechos y deberes pacientes: información, autonomía, acompañamiento, reclamo | Todos | Vigente |
| Ley 21.331 (2021) | Ley | Reconocimiento y protección derechos personas enfermedad/discapacidad mental | 27–36 | Vigente |
| Ley 20.850 (2015) | Ley | Ley Ricarte Soto — sistema protección financiera diagnósticos/tratamientos alto costo | 5, 15–17 | Vigente |
| Ley 20.422 (2010) | Ley | Igualdad de oportunidades e inclusión de personas con discapacidad | 27–36 | Vigente |
| Ley 20.120 (2006) | Ley | Investigación científica en seres humanos y su genoma — bioética | 16 | Vigente |
| Ley 19.966 (2004) | Ley | Régimen de Garantías en Salud — establece GES/AUGE | 1–5, 15–26 | Vigente |
| DFL 725 — Código Sanitario | DFL | Código Sanitario: habilitación prestadores, productos farmacéuticos, higiene | Todos | Vigente (mod. 2024) |
| DFL 1/2005 MINSAL | DFL | Fija texto refundido Ley 18.933 (ISAPRES) y Ley 18.469 (FONASA) | 5, financiamiento | Vigente |
| DS 4/2009 MINSAL | Decreto | Reglamento prestadores institucionales: requisitos infraestructura, RRHH, procesos | 1–17 | Vigente |
| DS 38/2005 MINSAL | Decreto | Reglamento derechos pacientes hospitalizados | 15–17 | Vigente |
| DS 140/2004 MINSAL | Decreto | Reglamento Orgánico de los Servicios de Salud | 1–5 | Vigente |
| DS 15/2007 MINSAL | Decreto | Reglamento del Sistema de Acreditación para los Prestadores Institucionales de Salud | Todos | Vigente |
| DS 58/2008 MINSAL | Decreto | Reglamento de prestaciones de urgencia | 18–26 | Vigente |
| NT Acreditación (Superintendencia de Salud) | Norma Técnica | Estándares acreditación: ámbitos dignidad, gestión clínica, RRHH, registros, seguridad | Todos | Vigente (v3, 2023) |
| GES/AUGE (85 problemas, 2024) | Garantía | Garantías explícitas acceso, oportunidad, protección financiera, calidad | 1–5, 15–26 | Vigente (actualización anual) |
| NT Telemedicina (MINSAL, 2022) | Norma Técnica | Regulación teleconsulta, telemonitoreo, teleasistencia | 6, 15, 17 (HaH) | Vigente |
| NT HCE/Interoperabilidad (MINSAL) | Norma Técnica | Estándares historia clínica electrónica, FHIR, integración | 6, Anexo FHIR | Vigente |
| NT Urgencia (MINSAL) | Norma Técnica | Organización SUH, triage, categorización, tiempos de atención | 18–26 | Vigente |
| NT IAAS (MINSAL) | Norma Técnica | Prevención y control infecciones asociadas a atención de salud | 4, 16 | Vigente |
| NT Programa Nacional de Sangre | Norma Técnica | Estándares banco de sangre, medicina transfusional | 16 | Vigente |
| Norma General Administrativa N°19 (MINSAL) | Norma | Gestión del cuidado de enfermería en red asistencial | 15–17 | Vigente |
| Orientaciones Técnicas SM (MINSAL, 2023) | Orientación | Modelo comunitario SM, continuidad, rehabilitación, infanto-juvenil | 27–36 | Vigente |
| Orientaciones Red de Urgencia (MINSAL) | Orientación | Organización funcional red urgencia: SAPU, SAR, SUH, SAMU | 18–26 | Vigente |
| Política Nacional de Medicamentos (MINSAL) | Política | Acceso, calidad, uso racional de medicamentos | 10, 16 | Vigente |
| Plan Nacional de Salud Mental (MINSAL, 2017–2025) | Plan | Objetivos estratégicos SM: modelo comunitario, SM infanto-juvenil, TUS, suicidio | 27–36 | Vigente |
| NT Programa Nacional Prevención Suicidio (MINSAL, 2023) | Norma Técnica | Detección, intervención y postvención suicidio en red | 30, 32 | Vigente |
| Orientación Técnica HaH (MINSAL, 2021) | Orientación | Criterios inclusión/exclusión, dotación, monitoreo, alta domiciliaria | 17 | Vigente |
| NT Reanimación Cardiopulmonar (MINSAL) | Norma Técnica | Cadena supervivencia, DEA, soporte vital básico/avanzado | 18–22 | Vigente |
| Política Nacional de Seguridad del Paciente (MINSAL, 2022) | Política | Cultura seguridad, notificación EA, gestión riesgo clínico | 4 | Vigente |

### 5.2 Referentes internacionales

| Referente | Tipo | Alcance | Capítulos impactados |
|-----------|------|---------|----------------------|
| OMS — mhGAP Intervention Guide v2.0 | Guía clínica | Manejo brechas SM en nivel primario: depresión, psicosis, TUS, suicidio | 27–36 |
| OMS — Quality of Care Framework | Marco calidad | 6 dimensiones: seguridad, efectividad, centrado en persona, oportuno, eficiente, equitativo | 4–5 |
| OMS — Emergency Care Systems Framework | Marco emergencias | Diseño sistemas emergencia: prehospitalario, triage, cadenas tiempo | 18–26 |
| OMS — WHO-AIMS (Assessment Instrument for MH Systems) | Instrumento | Evaluación sistemas SM: gobernanza, financiamiento, RRHH, servicios, información | 27–36 |
| OPS — RISAI (Redes Integradas Servicios) | Marco conceptual | Modelo redes integradas: 14 atributos, gobernanza, continuidad, primer nivel | 1–5, 15 |
| OPS — Estrategia y Plan de Acción SM | Estrategia | Lineamientos SM región Américas: derechos, comunitario, intersectorial | 27–36 |
| IHI — Triple/Quadruple Aim | Framework | Experiencia, salud poblacional, costo, bienestar equipo | Todos |
| IHI — Bundles (CVC, VAP, Sepsis) | Paquete intervenciones | Prevención IAAS: inserción, mantención, retiro | 16, 18–26 |
| IHI — Whole System Measures | Indicadores sistema | 7 indicadores nivel sistema: mortalidad, readmisión, satisfacción, funcional | 5, Anexo KPI |
| NICE — Clinical Guidelines | Guías clínicas | Manejo basado en evidencia por dominio clínico | 15–26, 27–36 |
| NICE — Quality Standards | Estándares calidad | Estándares priorizados por condición clínica | 4–5 |
| AHRQ — PSNet (Patient Safety Network) | Base conocimiento | Seguridad del paciente: RCA, cultura seguridad, eventos centinela | 4, 16 |
| AHRQ — Quality Indicators (QI) | Indicadores | Prevención, hospitalización, seguridad paciente, pediátricos | 5, Anexo KPI |
| AHRQ — TeamSTEPPS | Framework | Trabajo en equipo, comunicación estructurada, safety culture | 4, 14 |
| Joint Commission | Estándares acreditación | International Patient Safety Goals, estándares hospitalarios | 4, 16, 18 |
| AHA/ACC/ESC | Guías cardiovasculares | STEMI, NSTEMI, ICC, arritmias: protocolos tiempo-dependientes | 20–22 |
| Cochrane Collaboration | Revisiones sistemáticas | HaH (Shepperd et al.), urgencias, SM — evidencia síntesis | 17, 18, 27 |
| Surviving Sepsis Campaign | Guía clínica | Bundles sepsis: hora-1, hora-3, reanimación, antibióticos | 16, 18–26 |
| ECRI Institute | Evaluación tecnología | Top 10 riesgos tecnología sanitaria, evaluación equipamiento | 6, 10 |
| Lean Healthcare / Toyota Production System | Metodología | Eliminación desperdicios, flujo continuo, VSM en salud | 3, Anexo BPMN |
| ISOS / ISO 9001:2015 | Estándar | Sistemas gestión calidad — requisitos, aplicación en salud | 4–5 |
| ISO 31000:2018 | Estándar | Gestión del riesgo — principios y directrices | 4, BCP |
| ISO 27001:2022 | Estándar | Seguridad de la información — aplicación HCE y datos clínicos | 6, TI |
| Donabedian (Estructura-Proceso-Resultado) | Marco teórico | Modelo clásico evaluación calidad atención de salud | 4–5 |
| DMAIC (Define-Measure-Analyze-Improve-Control) | Metodología | Ciclo Six Sigma aplicado a procesos asistenciales | 3, Anexo BPMN |

## 6. Contextualización local

Plantilla para adaptar el corpus a un Servicio de Salud / establecimiento específico. Completar columnas Estado/Responsable/Observaciones según realidad local.

### 6.1 Instrumentos de gobernanza y red

| Instrumento local | Tipo | Estado | Responsable | Observaciones |
|-------------------|------|--------|-------------|---------------|
| Convenio marco red asistencial SS [nombre] | Convenio | _pendiente_ | Dir. Red SS | Define cartera, derivación, contrarreferencia |
| SLA tiempos derivación inter-establecimiento | SLA | _pendiente_ | Subdirección gestión asistencial | Metas TAT referencia-contrarreferencia |
| Resolución dotación camas críticas | Resolución exenta | _pendiente_ | Dir. Establecimiento | Ratio camas UCI/UTI por población |
| Acuerdos COMGES vigentes | Compromiso gestión | _pendiente_ | Subdirección médica | Metas anuales MINSAL-SS |
| Plan de desarrollo red (PDR) | Plan estratégico | _pendiente_ | Dir. Red SS | Inversiones, brechas, proyecciones demográficas |
| Plan anual de inversiones FNDR/sectorial | Plan | _pendiente_ | Dir. Planificación | Proyectos infraestructura, equipamiento |

### 6.2 Protocolos operativos

| Instrumento local | Tipo | Estado | Responsable | Observaciones |
|-------------------|------|--------|-------------|---------------|
| Protocolo local triage SUH | Protocolo | _pendiente_ | Jefatura SUH | Adaptación ESI a realidad local |
| Protocolo derivación SM | Protocolo | _pendiente_ | Coordinación SM red | Flujo APS→COSAM→Hospital |
| Plan de contingencia HaH | Plan | _pendiente_ | Coordinación HaH | Criterios ingreso/exclusión, cobertura geográfica |
| Convenio EMS/SAMU regional | Convenio | _pendiente_ | SAMU regional | Tiempos respuesta, cobertura, protocolos activación |
| Plan emergencia hospitalario | Plan | _pendiente_ | Comité emergencia | HICS adaptado, roles, simulacros |
| Protocolo gestión lista de espera | Protocolo | _pendiente_ | Subdirección médica | Criterios priorización, monitoreo GES/no-GES |
| Protocolo gestión camas | Protocolo | _pendiente_ | Subdirección gestión asistencial | Flujo ingreso-egreso, bed management |

### 6.3 Instrumentos de información y TI

| Instrumento local | Tipo | Estado | Responsable | Observaciones |
|-------------------|------|--------|-------------|---------------|
| Mapa georeferenciado red | Instrumento | _pendiente_ | TI / Planificación | Establecimientos, áreas influencia, isócronas |
| Plan director TI del establecimiento | Plan | _pendiente_ | Jefatura TI | Roadmap HCE, integraciones, infraestructura |
| Política de seguridad de la información | Política | _pendiente_ | Encargado seguridad | ISO 27001, protección datos pacientes |
| Inventario sistemas información clínica | Catastro | _pendiente_ | TI | HCE, LIS, RIS, PACS, EDIS — versiones, integraciones |
| Reglamento interno de orden, higiene y seguridad | Reglamento | _pendiente_ | RRHH / Prevención de riesgos | Obligatorio DS 594 |
| Plan de capacitación continua | Plan | _pendiente_ | Subdirección RRHH | Brechas competencias, simulación, certificaciones |
| Protocolo notificación eventos adversos | Protocolo | _pendiente_ | Calidad / Seguridad paciente | Flujo EA, eventos centinela, RCA |
| Programa IAAS local | Programa | _pendiente_ | Comité IAAS | Vigilancia, bundles, tasas, auditorías |
| Convenio docente-asistencial | Convenio | _pendiente_ | Dir. Establecimiento / Universidad | Campos clínicos, supervisión, investigación |

## 7. Control de versiones

| Versión | Fecha | Cambios | Autor |
|---------|-------|---------|-------|
| v1.0.0 | 2025-09-25 | Cheatsheet original monolítico (`manual_gestion_redes_cheatsheet.md`) — documento único, sin estructura RAG, sin benchmarks internacionales | FS |
| v2.0.0 | 2026-03-03 | Transformación KORA/MD: corpus multi-archivo (00–05), profundización uniforme 36 capítulos + 11 anexos, estructura RAG por sección, benchmarks internacionales, glosario centralizado (~100 términos), marco normativo completo (CL + internacional), plantilla contextualización local | FS |

### Política de actualización

| Aspecto | Regla |
|---------|-------|
| Frecuencia revisión | Semestral o ante cambio normativo relevante |
| Versionado | SemVer: MAJOR (reestructura), MINOR (capítulo nuevo/reescrito), PATCH (correcciones) |
| Responsable | Propietario del corpus (FS) + validación por experto dominio |
| Trazabilidad | Cada cambio registrado en esta tabla con fecha, descripción y autor |
| Sincronización | Tras actualización de cualquier archivo, verificar coherencia con 00-indice.md |
| Glosario | Nuevos términos se agregan alfabéticamente; no se eliminan sin nota de deprecación |
| Normativa | Verificar vigencia al menos anualmente; marcar derogaciones explícitamente |
