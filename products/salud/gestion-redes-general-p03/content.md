---
urn: urn:salud:kb:gestion-redes-general-p03
nombre: gestion-redes-general-p03
version: 2.0.0
estado: publicado
descripcion: "Gestión de Redes Asistenciales — Marco General - Parte 03"
fuente: "Migrado de la bestia (~/kora @ 9de5dc38b78c23574d24a481a5f84d70173c2203) artifacts/knowledge/salud/salubrista/gestion-redes/01-gestion-redes-general--p03.md (sha256:27eaa90a732d49c1cf1362cf70b46c67fe8dd71821337c240683323772b7bc81) el 2026-07-17; cuerpo byte-fiel; frontmatter normalizado a ley/2; shard enlazado por cita a urn:salud:kb:gestion-redes-general."
autor: FS
creado: 2026-03-03
lang: es
tags: [gestion-redes, gobernanza, calidad, procesos, digital, finanzas, cambio, red-asistencial]
familia: bok
cita: [urn:salud:kb:gestion-redes-general]
---

# Gestión de Redes Asistenciales — Marco General - Parte 03

## 5.1 Levantamiento y modelamiento

Técnicas para mapear, documentar y analizar procesos asistenciales y de soporte como base para rediseño.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| SIPOC | Suppliers, Inputs, Process, Outputs, Customers — vista macro |
| VSM (Value Stream Mapping) | Flujo de valor con tiempos de espera, ciclo y % valor agregado |
| BPMN 2.0 | Notación estándar para modelamiento detallado de procesos |
| Diagrama de carriles (swimlane) | Responsabilidades por rol/unidad en cada paso |
| Voz del cliente (VOC) | Requerimientos del paciente traducidos a CTQ (Critical to Quality) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Procesos críticos mapeados | Procesos con VSM / Total procesos críticos × 100 | ≥80 % | — | Gestión procesos | Anual |
| Ratio valor agregado | Tiempo valor agregado / Tiempo total proceso × 100 | ≥30 % | Lean benchmark 25-50 % | Lean Enterprise 2020 | Por proyecto |
| Actualización de mapas | Procesos actualizados ≤24 meses / Total mapeados × 100 | ≥90 % | — | Gestión documental | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Mapeo como ejercicio teórico sin acción | Vincular cada mapeo a proyecto de mejora con sponsor |
| Participación insuficiente del equipo clínico | Gemba walk obligatorio, mapeo in situ |

Ref: Lean Healthcare (Graban 2018); BPMN 2.0 (OMG); IHI Process Improvement 2019; NHS Improvement 2020.

## 5.2 Rediseño Lean/Six Sigma

Metodologías de mejora continua aplicadas a procesos asistenciales y administrativos.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Kaizen (mejora rápida) | Eventos de 3-5 días, equipo multidisciplinario, resultado inmediato |
| 5S | Clasificar, ordenar, limpiar, estandarizar, sostener — áreas clínicas |
| DMAIC | Define, Measure, Analyze, Improve, Control — proyectos Six Sigma |
| A3 Thinking | Formato una página: problema, análisis, contramedidas, plan |
| Gestión visual | Tableros Kanban, semáforos, señalética estandarizada |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Proyectos de mejora activos | N° proyectos en curso / Total áreas críticas | ≥1 por área | — | PMO mejora | Trimestral |
| Resultados sostenidos 6 meses | Proyectos con mejora sostenida a 6m / Total completados × 100 | ≥70 % | — | Auditoría mejora | Semestral |
| ROI proyectos mejora | (Beneficio − Costo proyecto) / Costo proyecto × 100 | ≥200 % | — | Finanzas | Por proyecto |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Herramienta sin cultura de mejora | Formación en pensamiento Lean para liderazgo |
| Mejoras puntuales sin sostenibilidad | Control chart post-proyecto, auditoría a 3, 6, 12 meses |

Ref: Lean Hospitals (Graban 2018); Six Sigma for Healthcare (Lighter 2019); IHI Model for Improvement; NHS QSIR Programme 2023.

## 5.3 Estándares y catálogos transversales

Repositorios centralizados de estándares, nomenclaturas y catálogos maestros que aseguran coherencia en la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Catálogo de prestaciones | FONASA MAI/MAE, codificación única |
| Nomenclaturas clínicas | SNOMED CT, CIE-10/CIE-11, LOINC, ATC |
| Estándares de proceso | SOPs transversales (triage, conciliación, consentimiento) |
| Catálogo de roles | Perfiles de cargo estandarizados por nivel |
| Catálogo de formularios | Formularios clínicos y administrativos normados |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Codificación correcta egresos | Egresos con CIE-10 validado / Total egresos × 100 | ≥95 % | — | GRD/DEIS | Mensual |
| Catálogos actualizados | Catálogos vigentes / Total catálogos × 100 | 100 % | — | Gestión documental | Semestral |
| Adherencia a nomenclatura | Registros con código estándar / Total registros × 100 | ≥90 % | — | HCE | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Proliferación de códigos locales | Gobernanza de terminología centralizada |
| Resistencia a codificación estandarizada | Integración en HCE con asistentes de codificación |

Ref: FONASA Catálogo MAI/MAE; OMS CIE-11 2022; SNOMED International 2023; MINSAL Normas de Codificación GRD 2020.

## 5.4 Gestión documental

Sistema estructurado para crear, aprobar, distribuir, revisar y retirar documentos normativos de la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Jerarquía documental | Política → Norma → SOP → WI (Work Instruction) → Checklist |
| Ciclo de vida | Borrador → Revisión → Aprobación → Vigente → Revisión periódica → Obsoleto |
| Control de versiones | Codificación única, historial de cambios, firma electrónica |
| Distribución controlada | Repositorio digital único, notificación automática de actualizaciones |
| Revisión periódica | Máximo 3 años para políticas, 2 años para SOPs |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Documentos vigentes | Documentos dentro de fecha revisión / Total documentos × 100 | ≥90 % | ISO 9001 100 % | ISO 9001:2015 | Trimestral |
| Accesibilidad | % personal que accede al repositorio en último mes | ≥70 % | — | Analytics repositorio | Mensual |
| Tiempo aprobación | Días promedio desde borrador hasta aprobación | ≤30 días | — | Gestión documental | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Documentos obsoletos en circulación | Marca de agua automática, retiro controlado |
| Exceso burocrático documental | Fast-track para actualizaciones menores |

Ref: ISO 9001:2015 §7.5 (Información documentada); Joint Commission Document Control Standards 2023; NHS Document Control Policy 2022.

## 5.5 Automatización

Aplicación de tecnologías de automatización a procesos administrativos y operativos repetitivos.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| RPA (Robotic Process Automation) | Bots para tareas repetitivas: agendamiento, digitación, conciliación datos |
| Orquestación de procesos | BPM engine para flujos multi-actor (derivaciones, autorizaciones) |
| Formularios inteligentes | Auto-completado, validaciones, ruteo condicional |
| Alertas automatizadas | Triggers por reglas: resultados críticos, vencimientos, quiebres stock |
| Integración API | Conexión entre sistemas (HCE, ERP, LIMS) sin intervención manual |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Horas liberadas por RPA | Horas manuales reemplazadas / mes | ≥100 h/mes | — | Monitoreo RPA | Mensual |
| Tasa de error post-automatización | Errores en proceso automatizado / Total transacciones × 100 | ≤1 % | — | QA procesos | Mensual |
| Procesos automatizados | Procesos con RPA o BPM / Total procesos elegibles × 100 | ≥30 % | — | PMO digital | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Automatizar proceso deficiente | Rediseñar primero, automatizar después |
| Dependencia de proveedor único | Estándares abiertos, contratos con cláusula de portabilidad |

Ref: HIMSS RPA in Healthcare 2022; Gartner Hyperautomation 2023; NHS Digital Automation Programme 2023.

## 6.1 Gestión de la demanda

Predicción y modulación de la demanda de servicios para dimensionar capacidad y reducir variabilidad.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Forecast estadístico | Series temporales (ARIMA, Prophet), horizontes 1-12 meses |
| Estacionalidad | Patrones por mes, día de semana, festivos, epidemias |
| Demanda inducida | Efecto de nuevos programas, campañas, cambios GES |
| Segmentación | Urgente vs. electiva, nueva vs. control, presencial vs. virtual |
| Demand smoothing | Distribución uniforme de electivas para reducir peaks |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Error de pronóstico (MAPE) | Σ|Real−Pronóstico| / Real × 100 / n | ≤15 % | — | Gestión demanda | Mensual |
| Variabilidad artificial | CV demanda electiva diaria | ≤0.20 | — | Agendamiento | Mensual |
| Ratio nueva/control | Consultas nuevas / Consultas control | Según especialidad | — | Gestión ambulatoria | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Pronóstico errado por evento imprevisto | Escenarios múltiples, actualización rolling |
| Demanda reprimida no visible | Encuestas de necesidad insatisfecha, datos Lista de Espera |

Ref: IHI Optimizing Patient Flow 2003; Litvak 2005 (variability methodology); NHS Demand & Capacity Guide 2022.

## 6.2 Criterios de derivación y backlogs

Protocolos explícitos de derivación y gestión de listas de espera acumuladas.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Criterios de derivación | Guías por especialidad con umbrales clínicos para referencia |
| Priorización clínica | Categorías P1 (urgente ≤7d), P2 (semi-urgente ≤30d), P3 (electivo) |
| Validación de interconsultas | Revisión por especialista antes de aceptación (pre-triage) |
| Limpieza de lista | Contacto activo, depuración de duplicados, pacientes fallecidos/resueltos |
| Backlog management | Plan de reducción: sobrecupo, extensión horaria, compra servicios |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Interconsultas rechazadas | IC devueltas / Total IC recibidas × 100 | ≤15 % | — | eReferral | Mensual |
| Lista de espera quirúrgica | N° pacientes en espera / Producción mensual | ≤3 meses de stock | UK NHS ≤18 sem | NHS 2023 | Mensual |
| Depuración lista | Registros depurados / Total lista × 100 | ≥10 %/año | — | Gestión LE | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Derivación inadecuada satura especialidad | Teleconsultoría previa, capacitación APS |
| Lista de espera oculta (intra-servicio) | Registro único centralizado |

Ref: MINSAL Orientaciones Gestión Lista de Espera 2023; NHS RTT Waiting Times 2023; NZ Elective Services 2022.

## 6.3 Centros de coordinación de acceso

Unidades centralizadas que gestionan la demanda entrante, triaje y asignación de recursos.

**IF/THEN para ruteo de triage:**

| Condición | Prioridad | Ruteo |
|-----------|-----------|-------|
| Sospecha patología GES | P1 | Ruta GES directa, confirmación ≤30 días |
| Criterio de derivación urgente | P1 | Agenda preferente especialidad ≤7 días |
| Derivación semi-urgente | P2 | Agenda especialidad ≤30 días |
| Derivación electiva estándar | P3 | Lista de espera con fecha estimada |
| Consulta resoluble por teleconsultoría | — | Retorno a APS con recomendación especialista |
| Información incompleta | — | Devolución a APS con checklist requerido |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Contact center | Canal telefónico + digital para agendamiento y consultas |
| Centro regulador | Gestión de camas, traslados, interconsultas de urgencia |
| eReferral hub | Plataforma de derivación electrónica con triage centralizado |
| Callback system | Rellamada programada para reducir abandono |
| Dashboard de acceso | Tiempos de espera en tiempo real por especialidad |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tasa de abandono llamadas | Llamadas abandonadas / Total llamadas × 100 | ≤5 % | — | Contact center | Mensual |
| Tiempo respuesta eReferral | Días desde recepción hasta aceptación/rechazo | ≤3 días | UK ≤2 días | NHS 2023 | Mensual |
| Derivaciones GES en plazo | GES confirmadas en plazo / Total GES × 100 | ≥98 % | — | SIGGES | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Cuello de botella en centro regulador | Turnos 24/7, automatización de ruteo estándar |
| Triage inadecuado por personal no clínico | Protocolos validados, supervisión clínica |

Ref: MINSAL SIGGES; NHS e-Referral Service 2023; IHI Patient Flow 2019; Australasian Triage Scale.

## 6.4 Tiempos de oportunidad/garantía GES

Gestión de garantías legales de acceso y oportunidad del régimen GES/AUGE.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Garantía de acceso | Derecho a prestación dentro de la red |
| Garantía de oportunidad | Plazo máximo por patología/prestación (DS 4/2013) |
| SIGGES | Sistema de registro y monitoreo de garantías |
| Alerta GES | Notificación automática al 50 %, 75 % y 90 % del plazo |
| Recurso de protección | Consecuencia legal por incumplimiento |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cumplimiento oportunidad GES | Garantías cumplidas en plazo / Total garantías × 100 | ≥98 % | — | SIGGES-FONASA | Mensual |
| GES retrasadas activas | N° garantías vencidas sin resolver | 0 | — | SIGGES | Semanal |
| Tiempo promedio resolución | Días promedio desde activación hasta cierre GES | ≤70 % del plazo máximo | — | SIGGES | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Incumplimiento masivo por capacidad | Plan de contingencia: compra servicios, extensión horaria |
| Subregistro de activación GES | Auditoría cruzada con GRD y egresos |

Ref: Ley 19.966 (GES/AUGE); DS 4/2013; Superintendencia de Salud; FONASA Normas GES 2024.
