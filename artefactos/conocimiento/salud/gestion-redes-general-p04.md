---
urn: urn:salud:kb:gestion-redes-general-p04
nombre: gestion-redes-general-p04
version: 2.0.0
estado: publicado
descripcion: "Gestión de Redes Asistenciales — Marco General - Parte 04"
fuente: "Migrado de la bestia (~/kora @ 9de5dc38b78c23574d24a481a5f84d70173c2203) artifacts/knowledge/salud/salubrista/gestion-redes/01-gestion-redes-general--p04.md (sha256:cda6299e5d0429718abd35007eaec42e14d9ac6ca783f685bcbb2cf12af48c6b) el 2026-07-17; cuerpo byte-fiel; frontmatter normalizado a ley/2; shard enlazado por cita a urn:salud:kb:gestion-redes-general."
autor: FS
creado: 2026-03-03
lang: es
tags: [gestion-redes, gobernanza, calidad, procesos, digital, finanzas, cambio, red-asistencial]
familia: bok
cita: [urn:salud:kb:gestion-redes-general]
---

# Gestión de Redes Asistenciales — Marco General - Parte 04

## 6.5 Intervenciones de descongestión

Estrategias tácticas para reducir listas de espera y mejorar tiempos de acceso.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Extensión horaria | Turnos vespertinos y fines de semana para electivas |
| Sobrecupo programado | Agendas expandidas temporales con tope de seguridad |
| Compra de servicios | PPV a prestadores privados para especialidades críticas |
| Telemedicina | Teleconsultas para controles y seguimientos |
| Resolución en APS | Transferencia de competencias (ecografía, dermatoscopía, espirometría) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Reducción lista de espera | (LE mes anterior − LE mes actual) / LE mes anterior × 100 | ≥5 %/mes durante intervención | — | Gestión LE | Mensual |
| Producción adicional | Prestaciones extra / Producción base × 100 | ≥20 % durante campaña | — | Gestión producción | Mensual |
| Costo por caso adicional | Costo total intervención / Casos resueltos adicionales | ≤120 % costo estándar | — | Finanzas | Por campaña |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Burnout por sobrecarga sostenida | Intervenciones acotadas (≤3 meses), voluntariedad |
| Efecto rebote post-intervención | Abordar causa raíz simultáneamente |

Ref: MINSAL Plan Nacional de Reducción LE 2023; NHS Elective Recovery Programme 2023; IHI Reducing Waiting Times 2004.

## 7.1 Infraestructura y flujos físicos

Diseño y gestión del espacio físico para optimizar flujos de pacientes, personal e insumos.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Zonificación | Áreas limpias/sucias, flujos unidireccionales, segregación pacientes infecciosos |
| Señalética | Wayfinding estandarizado, código de colores por área |
| Capacidad física | m² por cama (10 m² norma), distancia entre camillas, ventilación |
| Seguridad estructural | Normativa sísmica NCh433, evacuación, sistemas contra incendio |
| Facility management | Mantención preventiva infraestructura, HVAC, gases clínicos |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Mantención preventiva cumplida | MP realizadas / MP programadas × 100 | ≥90 % | Joint Commission ≥95 % | JCI 2023 | Mensual |
| Incidentes infraestructura | N° fallas críticas (electricidad, agua, gases) / mes | 0 | — | Facility management | Mensual |
| Cumplimiento normativa | Items conformes / Total items auditoría SEREMI × 100 | ≥95 % | — | SEREMI Salud | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Infraestructura obsoleta | Plan maestro de inversiones con priorización por riesgo |
| Flujos cruzados contaminación | Auditoría de flujos trimestral, rediseño si necesario |

Ref: MINSAL Norma Técnica Básica de Establecimientos 2017; ASHRAE 170 (ventilación); FGI Guidelines for Design and Construction of Hospitals 2022; NCh433 (sísmica).

## 7.2 Camas, pabellones, box y agendas

Dimensionamiento y gestión de la capacidad instalada para maximizar productividad y acceso.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Gestión de camas | Ocupación óptima 85 %, census tracking, discharge planning |
| Pabellones | Utilización quirúrgica (first case on time, turnover, cancellation rate) |
| Box de atención | Productividad ambulatoria (consultas/box/día) |
| Agendas | Configuración por tipo (nuevas/controles), overbooking calculado |
| Productividad | Benchmarks por especialidad (egresos/cama, CMA/pabellón) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Ocupación de camas | Días-cama ocupados / Días-cama disponibles × 100 | 85 % (±5 %) | OCDE 75 % | OCDE 2023 | Diaria |
| Utilización pabellón | Minutos cirugía / Minutos disponibles × 100 | ≥80 % | — | Gestión quirúrgica | Mensual |
| Suspensión quirúrgica | Cirugías suspendidas / Total programadas × 100 | ≤5 % | — | Gestión quirúrgica | Mensual |
| Productividad ambulatoria | Consultas realizadas / Horas médicas contratadas | ≥4/hora | — | Gestión ambulatoria | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Ocupación >90 % genera boarding y riesgo | Gatillo de contingencia a 90 %, plan de desborde |
| Suspensiones por falta de insumos | Checklist pre-quirúrgico estandarizado |

Ref: IHI Optimizing Patient Flow 2003; OCDE Health at a Glance 2023; Association for Perioperative Practice 2023; MINSAL Norma Gestión del Bloque Quirúrgico 2018.

## 7.3 Teoría de colas y simulación

Modelos matemáticos para dimensionar recursos y predecir congestión en la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| M/M/s | Modelo Erlang-C: tasa de llegada (λ), servicio (μ), servidores (s) |
| Simulación de eventos discretos | Arena, SimPy, AnyLogic para escenarios complejos |
| Ley de Little | L = λ × W (pacientes en sistema = tasa × tiempo estancia) |
| Ley de Kingman | Tiempo espera ∝ (utilización / (1−utilización)) × variabilidad |
| What-if analysis | Escenarios de capacidad ante cambios de demanda |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Utilización del recurso crítico | λ / (s × μ) | ≤85 % | Erlang-C target | Análisis de colas | Mensual |
| Probabilidad de espera (Pw) | P(espera > 0) calculada por Erlang-C | ≤20 % | — | Modelo de colas | Trimestral |
| Validación del modelo | Error predicción vs. real | ≤10 % | — | Simulación | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Modelo demasiado simplificado | Validar con datos reales, iterar complejidad |
| Sobre-inversión basada en peor escenario | Usar percentil 95, no máximo absoluto |

Ref: Erlang-C (Gross & Harris 2008); Little's Law; Kingman's Formula; Litvak 2005 (healthcare queuing); NHS Capacity Planning Tools 2023.

## 7.4 Programación maestra

Planificación integrada de recursos para equilibrar carga y minimizar variabilidad artificial.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Master Surgical Schedule | Asignación semanal fija de pabellones por especialidad |
| Block scheduling | Bloques protegidos para urgencias, electivas, ambulatorias |
| Smoothing | Distribución uniforme de admisiones electivas entre días |
| Overbooking calculado | Tasa de no-show por especialidad → sobrecupo ajustado |
| Reconciliación semanal | Ajuste fino según censo, urgencias y contingencias |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Adherencia al master schedule | Sesiones realizadas según plan / Total sesiones plan × 100 | ≥85 % | — | Gestión quirúrgica | Semanal |
| No-show rate | Pacientes que no asisten / Total citados × 100 | ≤10 % | — | Agendamiento | Mensual |
| Variabilidad admisiones electivas | CV admisiones electivas diarias | ≤0.15 | Litvak target ≤0.10 | Litvak 2005 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Urgencias desplazan electivas crónicamente | Bloques protegidos con política de invasión explícita |
| No-show alto por barreras de acceso | Recordatorios multicanal (SMS, llamada), lista de espera activa |

Ref: Litvak 2005 (surgical smoothing); IHI Patient Flow 2019; AORN Perioperative Standards 2023.

## 7.5 Equipamiento biomédico

Gestión del ciclo de vida de equipos médicos: adquisición, mantención, calibración y baja.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Inventario | Registro completo con código, ubicación, vida útil, riesgo |
| Mantención preventiva (PM) | Programa según fabricante y criticidad (Clase I/II/III) |
| Calibración | Verificación periódica de parámetros de medición |
| Obsolescencia | Evaluación vida útil, costo mantención vs. reposición |
| Tecnovigilancia | Reporte de incidentes ISP, alertas fabricante, recalls |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| PM cumplida | PM realizadas / PM programadas × 100 | ≥95 % | ECRI ≥90 % | ECRI 2023 | Mensual |
| Disponibilidad equipos críticos | Horas operativas / Horas programadas × 100 | ≥98 % | — | Ingeniería biomédica | Mensual |
| Equipos fuera de vida útil | Equipos >vida útil / Total inventario × 100 | ≤10 % | — | Inventario | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Falla equipo crítico sin respaldo | Plan de contingencia, equipos de respaldo para críticos |
| Mantención por personal no calificado | Contratos de servicio con fabricante, certificación técnicos |

Ref: ECRI Institute 2023; ISP Tecnovigilancia Chile; IEC 62353 (pruebas equipos médicos); MINSAL Norma Técnica Equipamiento 2016.

## 8.1 Centro de comando (NOC)

Unidad centralizada de monitoreo y coordinación operacional en tiempo real de la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| War room / NOC | Espacio físico con pantallas, datos RT, equipo dedicado |
| Tableros en tiempo real | Census, ocupación, tiempos espera, alertas, flujo urgencia |
| Reglas de activación | Umbrales predefinidos que gatillan acciones (semáforo) |
| Huddles operacionales | Reuniones breves (≤15 min) a las 09:00 y 14:00 |
| Escalamiento RT | Protocolo quién-contacta-a-quién según nivel de alerta |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo detección-respuesta | Minutos desde alerta hasta acción correctiva | ≤30 min | — | NOC log | Diaria |
| Huddles realizados | Huddles ejecutados / Huddles programados × 100 | ≥95 % | — | NOC log | Semanal |
| Alertas resueltas mismo turno | Alertas cerradas en turno / Total alertas × 100 | ≥80 % | — | NOC log | Diaria |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Fatiga de alertas (alarm fatigue) | Priorización, reducir alertas no accionables a <10 % |
| NOC sin autoridad para actuar | Mandato formal del consejo directivo |

Ref: GE Healthcare Command Centers 2020; IHI Real-Time Demand Capacity Management 2019; NHS Command Centre Model 2022.

## 8.2 Gestión de camas y traslados

Coordinación en tiempo real de asignación de camas, egresos y transferencias entre establecimientos.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Bed board digital | Visualización RT: ocupación, pendientes de alta, limpieza, bloqueos |
| Discharge planning | Predicción de alta (ML o reglas), planificación desde ingreso |
| Limpieza y habilitación | Workflow limpieza → inspección → habilitación, target ≤60 min |
| Traslados inter-establecimientos | Protocolo de solicitud, aceptación, transporte, handoff |
| Código de desborde | Activación cuando ocupación >95 %, plan de contingencia |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo cama vacía a ocupada | Minutos desde egreso hasta ingreso siguiente | ≤120 min | Best practice ≤90 min | IHI 2019 | Diaria |
| Egresos antes mediodía | Altas antes 12:00 / Total altas × 100 | ≥40 % | — | Bed board | Diaria |
| Boarding time urgencia | Horas desde decisión hospitalizar hasta cama asignada | ≤2 h | — | SU-NOC | Diaria |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Boarding prolongado en urgencia | Meta de alta matutina, ronda de alta temprana |
| Traslado sin cama confirmada | Regla: no traslado sin aceptación + cama asignada |

Ref: IHI Patient Flow 2019; ACEP Boarding Position Statement 2022; NHS Discharge Planning Guidance 2023.

## 8.3 Reglas de control de flujo

Mecanismos tipo pull/push y límites de trabajo en proceso para regular el flujo de pacientes.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Sistema pull | Cama disponible "jala" al siguiente paciente (no push desde urgencia) |
| WIP limits | Máximo de pacientes simultáneos por área/profesional |
| FIFO con prioridad | Orden de llegada modulado por urgencia clínica |
| Señales Kanban | Visual: verde (<80 % capacidad), amarillo (80-90 %), rojo (>90 %) |
| Balanceo de carga | Distribución equitativa entre servicios/pisos disponibles |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| WIP promedio por servicio | Pacientes promedio en servicio / Capacidad × 100 | ≤85 % | — | Census RT | Diaria |
| Tiempo en cola interno | Minutos espera entre etapas del flujo | ≤30 min | — | Trazabilidad | Diaria |
| Violaciones WIP limit | Eventos sobre WIP limit / Total turnos × 100 | ≤5 % | — | NOC log | Semanal |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Cultura de push ("no tengo camas pero envío") | Entrenamiento, regla formal de no-push |
| WIP limits rígidos bloquean urgencias | Override protocolizado con escalamiento |

Ref: Lean Healthcare Flow (Graban 2018); Theory of Constraints (Goldratt); IHI Patient Flow 2019.

## 8.4 Alertas operacionales y contingencia

Sistema escalonado de alertas que activa respuestas progresivas ante saturación o eventos adversos.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Nivel verde | Operación normal, indicadores dentro de rango |
| Nivel amarillo | Pre-saturación: ocupación 85-95 %, LE creciente, suspensión electivas parcial |
| Nivel rojo | Saturación: ocupación >95 %, activación plan desborde, desvío ambulancias |
| Nivel negro | Catástrofe: activación HICS, plan de emergencia |
| Comunicación | Notificación automática por nivel a lista de distribución definida |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo en nivel rojo | Horas en nivel rojo / Horas totales × 100 | ≤5 % | — | NOC log | Mensual |
| Activaciones contingencia | N° activaciones plan desborde / mes | Monitorear tendencia | — | NOC log | Mensual |
| Adherencia al protocolo | Acciones ejecutadas según protocolo / Acciones requeridas × 100 | ≥90 % | — | Post-activación review | Por evento |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Demora en escalamiento | Activación automática por regla, no por juicio individual |
| Nivel rojo prolongado normalizado | Análisis de causa raíz obligatorio post >24h en rojo |

Ref: NHS OPEL Framework 2023; ACEP Emergency Department Crowding 2022; IHI Surge Management 2020.
