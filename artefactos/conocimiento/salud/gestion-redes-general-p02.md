---
urn: urn:salud:kb:gestion-redes-general-p02
nombre: gestion-redes-general-p02
version: 2.0.0
estado: publicado
descripcion: "Gestión de Redes Asistenciales — Marco General - Parte 02"
fuente: "Migrado de la bestia (~/kora @ 9de5dc38b78c23574d24a481a5f84d70173c2203) artifacts/knowledge/salud/salubrista/gestion-redes/01-gestion-redes-general--p02.md (sha256:c96c99a36926327587fd54963ee0272623147884c70e2b85a7ebb5e521572b47) el 2026-07-17; cuerpo byte-fiel; frontmatter normalizado a ley/2; shard enlazado por cita a urn:salud:kb:gestion-redes-general."
autor: FS
creado: 2026-03-03
lang: es
tags: [gestion-redes, gobernanza, calidad, procesos, digital, finanzas, cambio, red-asistencial]
familia: bok
cita: [urn:salud:kb:gestion-redes-general]
---

# Gestión de Redes Asistenciales — Marco General - Parte 02

## 3.1 Análisis poblacional

Caracterización demográfica, epidemiológica y socioeconómica de la población adscrita como base de planificación.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Pirámide poblacional | Estructura etaria, proyecciones INE, envejecimiento |
| Carga de enfermedad | AVISA, AVPP, principales GBD por territorio |
| Perfil epidemiológico | Prevalencia crónicas (DM2, HTA, EPOC, SM), incidencia cáncer |
| Mapa socioeconómico | Quintiles ingreso, Registro Social de Hogares, ruralidad |
| Demanda histórica | Series temporales de consultas, egresos, urgencias (≥3 años) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tasa de uso servicios | Consultas (o egresos) / Población adscrita × 1.000 | Según norma | OCDE 6.8 consultas/hab | OCDE 2023 | Anual |
| Razón de dependencia | (Pob <15 + Pob ≥65) / Pob 15-64 × 100 | Monitorear tendencia | Chile 52 % (2023) | INE 2023 | Anual |
| Brechas de prevalencia vs. bajo control | % bajo control / % prevalencia estimada × 100 | ≥60 % | UK QOF 70-80 % | MINSAL ENS 2017 | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Datos desactualizados | Actualización anual con DEIS, INE, Registro Social |
| Subregistro epidemiológico | Cruce fuentes (GRD, GES, notificación obligatoria) |

Ref: MINSAL-DEIS Estadísticas; INE Proyecciones Poblacionales 2023; GBD Study 2019; OCDE Health at a Glance 2023.

## 3.2 Estratificación de riesgo

Clasificación poblacional por nivel de riesgo clínico-social para asignación diferenciada de recursos y seguimiento.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Modelos clínicos | ACG (Johns Hopkins), CDPS, HCC (CMS), Charlson |
| Modelos sociales | Índice de vulnerabilidad territorial, Registro Social de Hogares |
| Pirámide de Kaiser | Nivel 1 (prevención), Nivel 2 (autogestión), Nivel 3 (gestión de caso), Nivel 4 (cuidados complejos) |
| Registros clínicos | Panel management, registros de crónicos por CESFAM |
| Segmentación operativa | Bajo riesgo (80 %), riesgo moderado (15 %), alto riesgo (5 %) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Población estratificada | Población con score de riesgo / Población adscrita × 100 | ≥80 % | UK NHS 100 % | NHS England 2023 | Anual |
| Concordancia modelo | C-statistic del modelo predictivo | ≥0.70 | ACG 0.75-0.80 | Johns Hopkins 2022 | Anual |
| Cobertura alto riesgo | Pacientes alto riesgo con plan activo / Total alto riesgo × 100 | ≥90 % | — | Panel management | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Sesgo del modelo por datos incompletos | Validación local, calibración anual |
| Estigmatización por etiqueta de riesgo | Comunicación centrada en necesidades, no en categorías |

Ref: Kaiser Permanente Risk Stratification; Johns Hopkins ACG System 2022; NHS England Population Health Management 2023; MINSAL MAIS 2013.

## 3.3 Cartera de servicios por nivel

Definición explícita de prestaciones ofertadas en cada nodo de la red según nivel de complejidad y normativa.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Cartera APS | MAIS, PSCV, control sano, salud mental comunitaria, urgencia rural |
| Cartera secundaria | 56 especialidades, CDT, procedimientos ambulatorios, hospital de día |
| Cartera terciaria | UCI, neurocirugía, cardiocirugía, trasplantes, neonatología |
| Cartera GES | 87 patologías con garantías de acceso, oportunidad, protección financiera |
| Brechas | Análisis oferta vs. demanda por prestación y territorio |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cobertura cartera normada | Prestaciones disponibles / Prestaciones normadas × 100 | ≥95 % | — | MINSAL 2023 | Anual |
| Brecha GES | Garantías incumplidas / Total garantías activadas × 100 | ≤2 % | — | FONASA-GES | Mensual |
| Resolución quirúrgica ambulatoria | CMA / Total cirugías elegibles × 100 | ≥60 % | OCDE 60-80 % | OCDE 2023 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Cartera desalineada con perfil epidemiológico | Revisión bienal basada en carga de enfermedad local |
| Duplicación entre niveles | Protocolos de derivación con criterios explícitos |

Ref: DS 4/2013 (Reglamento GES); MINSAL Norma Cartera de Servicios 2018; OCDE Health at a Glance 2023.

## 3.4 Topología de la red (mapa SIG, tiempos, regionalización)

Representación geoespacial de la red con análisis de accesibilidad temporal y asignación territorial.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Mapa SIG | Georreferenciación de establecimientos, población, vías |
| Isócronas | Mapas de tiempo de viaje (30, 60, 120 min) a nodos críticos |
| Micro-redes | Agrupación funcional de establecimientos por territorio |
| Puntos ciegos | Zonas sin cobertura dentro de isócrona normada |
| Infraestructura crítica | Establecimientos con rol de respaldo ante contingencia |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Acceso ≤60 min a urgencia | Población a ≤60 min de SU / Población total × 100 | ≥95 % | UK 95 % (8 min ambulancia) | NHS 2023 | Anual |
| Puntos ciegos identificados | Zonas sin cobertura / Total zonas × 100 | ≤5 % | — | SIG Servicio de Salud | Anual |
| Actualización SIG | Fecha última actualización | ≤12 meses | — | Gestión interna | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Datos geográficos desactualizados | Convenio con IGM/INE, actualización anual |
| Accesibilidad teórica vs. real | Validación con tiempos reales (GPS flota SAMU) |

Ref: MINSAL Orientaciones Planificación de Red 2019; OPS Mapeo de Redes 2015; UK NHS Ambulance Response Programme 2023.

## 3.5 Roadmap y priorización

Hoja de ruta estratégica con priorización de iniciativas por valor, factibilidad y urgencia.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Matriz valor/esfuerzo | 4 cuadrantes: quick wins, proyectos estratégicos, relleno, evitar |
| Quick wins | Implementables en ≤90 días, alto impacto, bajo costo |
| Horizonte temporal | Corto (1 año), mediano (2-3 años), largo (5+ años) |
| Dependencias | Mapa de prerequisitos entre iniciativas |
| Gobernanza del roadmap | Revisión trimestral en consejo directivo |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Avance roadmap | Hitos completados / Hitos planificados × 100 | ≥80 % | — | PMO red | Trimestral |
| Quick wins ejecutados | QW completados ≤90 días / QW identificados × 100 | ≥70 % | — | PMO red | Trimestral |
| Inversión alineada | Presupuesto en iniciativas priorizadas / Presupuesto total × 100 | ≥75 % | — | Finanzas red | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Roadmap estático ante cambio de contexto | Revisión trimestral con ventana de ajuste |
| Priorización política sobre técnica | Criterios explícitos documentados y publicados |

Ref: Eisenhower Matrix; Lean Portfolio Management (SAFe 2023); NHS Long Term Plan 2019.

## 4.1 Rutas asistenciales integradas

Secuencias estandarizadas de actividades clínicas que articulan múltiples niveles y disciplinas para una condición específica.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Ruta E2E | Desde sospecha diagnóstica hasta seguimiento post-tratamiento |
| Bundles de cuidado | Paquetes de intervenciones basadas en evidencia (3-5 elementos) |
| Variabilidad clínica | Monitoreo de adherencia a ruta y análisis de desviaciones |
| Ownership | Líder clínico responsable por ruta (champion) |
| Revisión basada en evidencia | Actualización ≤3 años o ante nueva evidencia nivel I |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Adherencia a ruta | Pacientes con ≥80 % de hitos cumplidos / Total pacientes ruta × 100 | ≥75 % | — | HCE/auditoría | Trimestral |
| Bundle compliance | Pacientes con 100 % elementos del bundle / Total elegibles × 100 | ≥95 % | IHI ≥95 % | IHI 2019 | Mensual |
| Tiempo E2E | Mediana días desde ingreso a ruta hasta resolución | Según patología | — | Sistema trazabilidad | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Rutas desactualizadas | Trigger de revisión: nueva GPC, alerta AHRQ, >2 años |
| Baja adherencia por desconocimiento | Capacitación al ingreso, recordatorios en HCE |

Ref: NHS Map of Medicine; IHI Bundles 2019; NICE Pathways; MINSAL GPC por patología GES.

## 4.2 Coordinación APS–especialidad–hospital–comunidad

Mecanismos operativos de articulación entre niveles asistenciales y recursos comunitarios.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Consultorías | Especialista en APS (presencial/teleconsultoría), transferencia de conocimiento |
| Gestión de caso | Coordinador asignado para pacientes complejos (≥3 comorbilidades) |
| Reuniones clínicas integradas | Caso conjunto APS-especialista, frecuencia quincenal mínima |
| Recursos comunitarios | Mapeo y derivación a organizaciones locales (social prescribing) |
| Contrarreferencia activa | Informe estructurado + plan de seguimiento + próximo control |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Teleconsultorías realizadas | N° teleconsultorías / Total interconsultas elegibles × 100 | ≥30 % | — | MINSAL Telemedicina 2023 | Trimestral |
| Pacientes con gestor de caso | Pac. complejos con gestor / Total pac. complejos × 100 | ≥80 % | UK 100 % para alto riesgo | NHS 2023 | Trimestral |
| Reuniones integradas realizadas | Reuniones realizadas / Reuniones programadas × 100 | ≥90 % | — | Gestión interna | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Especialista no contrarreferencia | Indicador en COMGES, auditoría |
| Recursos comunitarios no mapeados | Directorio actualizado semestralmente |

Ref: MINSAL MAIS 2013; NHS Social Prescribing 2023; Wagner Chronic Care Model 2001; Starfield Primary Care 1998.

## 4.3 Gestión de transiciones (alta segura)

Proceso estructurado para garantizar continuidad y seguridad durante transferencias entre niveles o servicios.

**IF/THEN por tipo de alta:**

| Tipo alta | Condición | Acción |
|-----------|-----------|--------|
| Alta médica estándar | Paciente estable, red de apoyo presente | Epicrisis + recetas + control APS ≤72h + educación al paciente/cuidador |
| Alta desde SUH | Consulta urgencia sin hospitalización | Informe de atención urgencia → APS en 24h, teleconsulta seguimiento si alto riesgo |
| Hospitalización domiciliaria (HaD) | Criterios HaD cumplidos, cuidador capacitado | Equipo HaD asume, visita ≤24h, protocolo de re-hospitalización definido |
| Alta psiquiátrica | Estabilización aguda, plan ambulatorio listo | Contacto COSAM ≤48h, control psiquiatría ≤7 días, plan de crisis entregado |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Checklist de alta segura | Medicación conciliada, educación, control agendado, alerta a APS |
| Conciliación medicamentosa | Revisión farmacéutica al ingreso, traslado y alta |
| Teach-back | Verificación comprensión del paciente sobre plan de alta |
| Handoff estandarizado | I-PASS o SBAR entre equipos |
| Seguimiento post-alta | Llamada ≤48h, control ≤7 días para alto riesgo |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Readmisión 30 días | Reingresos ≤30 días / Total egresos × 100 | ≤12 % | CMS 15.6 % (2023) | CMS 2023 | Mensual |
| Conciliación medicamentosa al alta | Altas con conciliación / Total altas × 100 | ≥95 % | ISMP 100 % | ISMP 2022 | Mensual |
| Llamada post-alta ≤48h | Llamadas realizadas ≤48h / Total altas elegibles × 100 | ≥80 % | — | Gestión interna | Mensual |
| Control APS ≤7 días post-alta | Controles realizados / Total altas × 100 | ≥70 % | — | Trazabilidad red | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Alta prematura por presión de camas | Criterios de alta explícitos, auditoría de reingresos precoces |
| Paciente no acude a control post-alta | Navegación activa, rescate telefónico |

Ref: Project RED (Boston University); IHI STAAR Initiative 2019; NICE NG27 Transition between inpatient and community 2015; MINSAL Norma Alta Segura 2019.

## 4.4 Coproducción del cuidado y navegación

Modelo de atención que integra al paciente como socio activo y provee apoyo para navegar la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Planes de cuidado compartidos | Objetivos definidos conjuntamente paciente-equipo |
| Navegadores de pacientes | Rol dedicado para acompañar trayectoria en la red |
| Herramientas de autogestión | Planes de acción, apps, material educativo validado |
| Grupos de pares | Programas de apoyo entre pacientes (diabetes, oncología) |
| Decisiones compartidas | Herramientas de ayuda a la decisión (option grids) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Pacientes con plan compartido | Pac. crónicos con plan / Total pac. crónicos × 100 | ≥60 % | UK NHS ≥50 % | NHS Personalised Care 2023 | Semestral |
| Activación del paciente (PAM) | Score PAM promedio | ≥60 | — | Insignia Health PAM | Anual |
| Navegación efectiva | Pac. navegados que completan ruta / Total navegados × 100 | ≥80 % | — | Programa navegación | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Carga adicional sobre paciente vulnerable | Adaptar nivel de coproducción a capacidad del paciente |
| Navegadores sin formación | Programa de capacitación estandarizado ≥40 horas |

Ref: NHS Personalised Care 2023; Hibbard PAM 2004; NICE Shared Decision Making 2021; Freeman Navigation Model 2012.

## 4.5 Comorbilidad y multimorbilidad

Gestión integrada de pacientes con ≥2 condiciones crónicas simultáneas, superando la lógica de enfermedad única.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Panel management | Registro activo de población a cargo con condiciones indexadas |
| PCI (Plan de Cuidados Integrado) | Plan unificado priorizando carga de tratamiento y preferencias |
| Polimedicación | Revisión farmacéutica estructurada (STOPP/START, Beers) |
| Complejidad clínica | Escalas INTERMED, Patient Complexity Tool |
| Coordinación multiprofesional | Ronda clínica semanal para pacientes de alta complejidad |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cobertura PCI | Pac. multimórbidos con PCI / Total pac. multimórbidos × 100 | ≥70 % | — | Panel management | Trimestral |
| Polifarmacia revisada | Pac. ≥5 fármacos con revisión ≤12 meses / Total polifarmacia × 100 | ≥80 % | UK QOF ≥80 % | NICE MO 2016 | Semestral |
| Hospitalizaciones evitables (ACSCs) | Egresos por ACSCs / Total egresos × 100 | ≤10 % | OCDE 5-8 % | OCDE 2023 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Fragmentación por múltiples especialistas | Médico de cabecera como integrador, PCI único |
| Carga de tratamiento excesiva | Minimally Disruptive Medicine, priorización con paciente |

Ref: NICE NG56 Multimorbidity 2016; Muth 2014 (Multimorbidity guidelines); OCDE Health at a Glance 2023; May 2009 (Minimally Disruptive Medicine).
