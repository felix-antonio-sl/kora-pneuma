---
urn: urn:salud:kb:gestion-redes-general-p07
nombre: gestion-redes-general-p07
version: 2.0.0
estado: publicado
descripcion: "Gestión de Redes Asistenciales — Marco General - Parte 07"
fuente: "Migrado de la bestia (~/kora @ 9de5dc38b78c23574d24a481a5f84d70173c2203) artifacts/knowledge/salud/salubrista/gestion-redes/01-gestion-redes-general--p07.md (sha256:12068bbdfa56603b92d3468fe5d6187bd9e3617759263d7725baf4adde0ba052) el 2026-07-17; cuerpo byte-fiel; frontmatter normalizado a ley/2; shard enlazado por cita a urn:salud:kb:gestion-redes-general."
autor: FS
creado: 2026-03-03
lang: es
tags: [gestion-redes, gobernanza, calidad, procesos, digital, finanzas, cambio, red-asistencial]
familia: bok
cita: [urn:salud:kb:gestion-redes-general]
---

# Gestión de Redes Asistenciales — Marco General - Parte 07

## 11.5 Gobierno de datos y seguridad

Marco de gobernanza para gestionar datos como activo estratégico con protección de privacidad y seguridad.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Data stewards | Responsables de calidad y uso de datos por dominio |
| Diccionario de datos | Catálogo con definiciones, formatos, reglas de validación |
| Privacidad | Ley 19.628 (Datos personales), Ley 20.584 (Ficha clínica), anonimización |
| Seguridad | ISO 27001, control de acceso, cifrado, monitoreo de brechas |
| Continuidad | ISO 22301, backup, DRP, pruebas de restauración |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Incidentes de seguridad datos | N° brechas de datos / año | 0 | — | CISO | Anual |
| Completitud diccionario | Variables documentadas / Total variables sistemas × 100 | ≥80 % | — | Data governance | Semestral |
| Cumplimiento ISO 27001 | Controles conformes / Total controles Anexo A × 100 | ≥90 % | — | Auditoría TI | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Fuga de datos clínicos | DLP (Data Loss Prevention), cifrado, auditoría de accesos |
| Datos sin dueño | Asignación obligatoria de data steward por sistema |

Ref: Ley 19.628 (Datos Personales Chile); Ley 20.584 art. 12-13 (Ficha clínica); ISO 27001:2022; ISO 22301:2019; HIPAA (referencia internacional).

## 12.1 Modelo de datos y calidad

Arquitectura de datos que asegura disponibilidad, integridad y trazabilidad para la toma de decisiones.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Data warehouse / data lake | Repositorio centralizado para analítica (star schema / raw) |
| Diccionario de datos | Definición, formato, dominio, fuente, responsable por variable |
| Linaje de datos | Trazabilidad origen→transformación→consumo |
| Calidad de datos (DQ) | Dimensiones: completitud, exactitud, oportunidad, consistencia |
| ETL/ELT | Procesos de extracción, transformación y carga con validación |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Completitud datos clave | Campos obligatorios completos / Total campos obligatorios × 100 | ≥95 % | — | DQ report | Mensual |
| Oportunidad | Datos disponibles en plazo / Total datos × 100 | ≥90 % | — | ETL monitoring | Mensual |
| Score DQ compuesto | Promedio ponderado 4 dimensiones | ≥85 % | — | Data governance | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Silos de datos no integrados | Bus de integración, catálogo de fuentes autoritativas |
| Datos de baja calidad generan malas decisiones | Reglas de validación en origen, DQ dashboard |

Ref: DAMA DMBOK 2.0 (Data Management); HIMSS Data Quality Framework 2023; MINSAL Estándar de Datos en Salud 2023.

## 12.2 KPI clínicos y operativos

Catálogo estandarizado de indicadores clave para monitorear desempeño clínico y operativo de la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| KPI clínicos | Mortalidad ajustada, readmisión, IAAS, bundle compliance, PROMs |
| KPI operativos | Ocupación, estancia media, lista espera, tiempo puerta-aguja, productividad |
| KPI financieros | Costo por egreso, costo por case-mix, ejecución presupuestaria |
| KPI experiencia | NPS, PREMs, reclamos, tiempo espera percibido |
| Ficha técnica del indicador | Nombre, definición, fórmula, fuente, periodicidad, responsable, meta, benchmark |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Catálogo KPI documentado | KPI con ficha técnica / Total KPI × 100 | 100 % | — | Calidad/gestión | Anual |
| KPI con dato disponible | KPI con medición ≤1 mes / Total KPI × 100 | ≥90 % | — | BI | Mensual |
| KPI en meta | KPI que cumplen meta / Total KPI medidos × 100 | ≥70 % | — | BSC | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Exceso de indicadores sin priorización | Máximo 20 KPI por nivel (operativo/táctico/estratégico) |
| Definiciones inconsistentes entre establecimientos | Ficha técnica única y validada por comité de red |

Ref: AHRQ Quality Indicators 2023; OCDE Health Care Quality Indicators; NHS Outcomes Framework 2023; MINSAL Indicadores de Gestión Hospitalaria.

## 12.3 Tableros y BSC/OKR

Herramientas de visualización y marcos de gestión para alinear desempeño con estrategia.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Dashboard operativo | Actualización diaria/RT: flujo, camas, urgencia, alertas |
| Dashboard táctico | Actualización semanal/mensual: producción, listas espera, calidad |
| Dashboard estratégico | Actualización trimestral: Cuádruple Meta, BSC, avance roadmap |
| BSC (Balanced Scorecard) | 4 perspectivas: paciente, procesos, aprendizaje, financiera |
| OKR (Objectives & Key Results) | Ciclos trimestrales, alineamiento vertical y horizontal |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Uso de dashboards | Usuarios activos / Usuarios con acceso × 100 | ≥60 % | — | BI analytics | Mensual |
| BSC actualizado | Indicadores BSC con dato vigente / Total indicadores BSC × 100 | ≥95 % | — | BSC | Trimestral |
| OKR completados | KR logrados (≥70 %) / Total KR × 100 | ≥70 % | — | OKR review | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Dashboard no consultado | Integrar en huddles, hacer accionable |
| OKR desalineados con estrategia | Cascada desde dirección, revisión trimestral |

Ref: Kaplan & Norton BSC 1996; Doerr OKR 2018; NHS Model Hospital Dashboard 2023; Few 2006 (Dashboard Design).

## 12.4 Evaluación de impacto

Métodos para medir el efecto real de intervenciones, proyectos y programas en la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Antes-después | Comparación pre/post con serie temporal interrumpida (ITS) |
| Grupo control | Diseño cuasi-experimental cuando sea factible |
| Análisis costo-efectividad | Costo por AVAC ganado, costo por caso evitado |
| Evaluación de beneficios | Tangibles (ahorro, producción) + intangibles (satisfacción, clima) |
| Framework RE-AIM | Reach, Effectiveness, Adoption, Implementation, Maintenance |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Proyectos con evaluación de impacto | Proyectos evaluados / Proyectos completados × 100 | ≥50 % | — | PMO | Anual |
| ROI promedio proyectos | (Beneficio − Inversión) / Inversión × 100 promedio | ≥100 % | — | Finanzas | Anual |
| Evaluaciones publicadas | N° evaluaciones con reporte formal | ≥3/año | — | Calidad/investigación | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Atribución incorrecta de causalidad | Métodos rigurosos (ITS, difference-in-differences) |
| Evaluación solo de éxitos | Incluir proyectos fallidos en análisis |

Ref: RE-AIM Framework (Glasgow 2019); Campbell & Stanley (quasi-experimental); NICE Guidelines Manual (economic evaluation); Drummond 2015.

## 12.5 Transparencia y rendición de cuentas

Mecanismos para comunicar resultados a la comunidad, autoridades y stakeholders.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Cuenta pública | Presentación anual obligatoria (Ley 20.285) |
| Portal de transparencia | Indicadores publicados, presupuesto, dotación |
| Reporte a Superintendencia | Indicadores de acreditación, reclamos, GES |
| Participación ciudadana | Consejos consultivos con acceso a datos de desempeño |
| Benchmarking público | Comparación entre establecimientos (anonimizado o nominal) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Solicitudes transparencia respondidas | Solicitudes respondidas en plazo / Total solicitudes × 100 | ≥95 % | Ley 20.285 | Portal Transparencia | Mensual |
| Indicadores publicados | KPI publicados en portal / KPI del catálogo × 100 | ≥50 % | — | Portal web | Semestral |
| Cuenta pública realizada | Cumplimiento anual | 100 % | — | Dirección | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Transparencia selectiva (solo buenos resultados) | Publicación de todos los indicadores, incluidos rojos |
| Datos sin contexto generan alarma | Acompañar con explicación y plan de mejora |

Ref: Ley 20.285 (Transparencia); Ley 20.730 (Lobby); Superintendencia de Salud; OCDE Government at a Glance 2023.

## 12.6 Modelos de madurez

Rúbricas escalonadas para evaluar el nivel de desarrollo de capacidades de gestión de la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Nivel 1 — Inicial | Procesos ad hoc, reactivo, sin estandarización |
| Nivel 2 — Repetible | Procesos documentados en algunas áreas, incipiente medición |
| Nivel 3 — Definido | Procesos estandarizados transversalmente, KPI operativos |
| Nivel 4 — Gestionado | Decisiones basadas en datos, mejora continua sistemática |
| Nivel 5 — Optimizado | Innovación proactiva, benchmarking, learning organization |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Score de madurez global | Promedio ponderado de dimensiones evaluadas (1-5) | ≥3.0 | — | Autoevaluación | Anual |
| Dimensiones en nivel ≥3 | Dimensiones ≥3 / Total dimensiones × 100 | ≥60 % | — | Autoevaluación | Anual |
| Progresión anual | Score año actual − Score año anterior | ≥+0.3 | — | Serie temporal | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Autoevaluación inflada | Validación cruzada con evidencia documental |
| Modelo genérico no aplica | Adaptar dimensiones al contexto de red asistencial chilena |

Ref: HIMSS EMRAM (digital maturity); NHS Improvement Maturity Matrix 2022; CMMI Institute; EFQM Excellence Model 2020.

## 12.7 Auditorías clínicas y operativas

Revisión sistemática de prácticas contra estándares definidos para identificar brechas y mejorar.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Auditoría de ficha clínica | Completitud, calidad registro, adherencia a GPC |
| Auditoría de codificación | Calidad CIE-10, GRD, coherencia diagnóstico-procedimiento |
| Auditoría de procesos | Cumplimiento SOP, tiempos, flujos |
| Peer review | Revisión entre pares de casos complejos o con resultado adverso |
| Auditoría de uso de recursos | Pertinencia de exámenes, estadía, derivaciones |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Fichas auditadas | Fichas revisadas / Total egresos × 100 | ≥10 % | — | Calidad | Trimestral |
| Concordancia codificación | Concordancia auditor-codificador / Total auditados × 100 | ≥85 % | — | GRD | Semestral |
| Peer reviews realizados | Casos revisados / Casos elegibles × 100 | ≥80 % | — | Comité clínico | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Auditoría percibida como persecución | Marco formativo, confidencialidad, feedback constructivo |
| Hallazgos sin plan de acción | Cierre obligatorio con AC verificada |

Ref: NHS Clinical Audit Standards 2023; NICE Clinical Audit Criteria; MINSAL Norma Auditoría Médica 2018; ACHS Estándares Acreditación.

## 12.8 Benchmarking y Learning Health System

Comparación sistemática de desempeño entre establecimientos y ciclo de aprendizaje organizacional continuo.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Benchmarking interno | Comparación entre servicios/establecimientos de la misma red |
| Benchmarking externo | Comparación con redes similares nacionales e internacionales |
| Learning Health System | Ciclo: datos→conocimiento→práctica→datos (IOM/NAM) |
| Comunidades de práctica | Grupos inter-establecimiento por tema (GPC, gestión, TI) |
| Transferencia de buenas prácticas | Repositorio de innovaciones con evaluación de replicabilidad |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| KPI con benchmark externo | KPI comparados con referente externo / Total KPI × 100 | ≥30 % | — | BI | Anual |
| Buenas prácticas transferidas | Prácticas replicadas de otra unidad / Prácticas identificadas × 100 | ≥20 % | — | Gestión conocimiento | Anual |
| Comunidades de práctica activas | Comunidades con ≥4 sesiones/año / Total comunidades × 100 | ≥80 % | — | Gestión conocimiento | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Comparación injusta por case-mix diferente | Ajuste por riesgo (GRD, ACG) |
| Benchmark sin acción | Plan de mejora para KPI bajo percentil 25 |

Ref: NAM Learning Health System 2013; NHS Model Hospital Benchmarking 2023; IHI Collaborative Model; Wenger Communities of Practice 1998.

## 12.9 Lecciones aprendidas (AAR)

Proceso estructurado para capturar, documentar y difundir aprendizajes de eventos, proyectos y ejercicios.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| After Action Review | ¿Qué debía ocurrir? ¿Qué ocurrió? ¿Por qué? ¿Qué haremos diferente? |
| Formato estandarizado | Evento, participantes, hallazgos, acciones, responsable, plazo |
| Repositorio de lecciones | Base de datos búsqueda por tema, área, tipo de evento |
| Difusión | Resumen ejecutivo a toda la red, incorporación en capacitación |
| Cierre de ciclo | Verificación de que la lección se incorporó a procesos/protocolos |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| AAR realizados | AAR post-evento o proyecto / Eventos elegibles × 100 | ≥80 % | — | Gestión conocimiento | Trimestral |
| Lecciones incorporadas | Lecciones que modificaron proceso / Total lecciones × 100 | ≥50 % | — | Gestión conocimiento | Semestral |
| Repositorio consultado | Consultas al repositorio / mes | ≥10 | — | Analytics | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| AAR como trámite sin aprendizaje | Facilitador entrenado, participación de involucrados |
| Lecciones no accesibles | Repositorio digital con búsqueda, tags, alertas |

Ref: US Army AAR Framework; NASA Lessons Learned; NHS After Action Review Guide 2022; Collison & Parcell 2004.
