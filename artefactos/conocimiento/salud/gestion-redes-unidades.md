---
urn: urn:salud:kb:gestion-redes-unidades
nombre: gestion-redes-unidades
version: 2.0.0
estado: publicado
descripcion: "Gestión de Redes Asistenciales — Gestión por Tipo de Unidad: Primer contacto y resolutividad"
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/salud/salubrista/gestion-redes/02-unidades-asistenciales.md (sha256:bbd7582af8f19aae327a1d5436d6e5f2c0ae253db2b6f00a5e5532e944b6c0f4) el 2026-06-12; cuerpo byte-fiel (renombrado de 02-unidades-asistenciales.md a gestion-redes-unidades.md por lugar-coincide). Fuente original: Síntesis multi-fuente: OPS, IHI, NICE, AHRQ, MINSAL, Cochrane, NotebookLM 46 fuentes HaH"
autor: FS
creado: 2026-03-03
lang: es
tags: [gestion-redes, unidades, ambulatorio, hospitalario, hospital-at-home, HaH, asistencial]
familia: bok
---

# Gestión de Redes Asistenciales — Gestión por Tipo de Unidad


## 15.1 APS/CESFAM/Clínicas comunitarias

Primer contacto y resolutividad. Modelo de Atención Integral de Salud (MAIS) con enfoque familiar y comunitario, equipos de sector adscritos territorialmente, cartera APS definida por norma. Continuidad longitudinal como eje.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Modelo MAIS | Enfoque biopsicosocial, equipo de cabecera, ciclo vital, participación comunitaria |
| Cartera APS | Prestaciones definidas MINSAL: controles, crónicos, EMPA/EFAM, GES, urgencia |
| Equipo de sector | Médico, enfermera, matrona, TENS, trabajador social — panel 3.500-5.000 inscritos |
| Continuidad longitudinal | Médico de cabecera asignado, agenda protegida, seguimiento proactivo |
| Derivación-contrarreferencia | Protocolo bidireccional con nivel secundario, trazabilidad electrónica |
| Programa crónicos | PSCV, DM2, HTA, asma/EPOC — estratificación riesgo, controles programados |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cobertura efectiva PSCV | Compensados / Total inscritos PSCV × 100 | ≥50 % | OCDE 55-65 % | MINSAL 2023 | Trimestral |
| Contrarreferencia oportuna | Contrarreferencias recibidas ≤7d / Total derivaciones × 100 | ≥80 % | — | MINSAL 2019 | Mensual |
| Control crónicos compensados | HbA1c <7 % (DM2) + PA <140/90 (HTA) / Total inscritos × 100 | ≥50 % | UK QOF 60-70 % | NHS QOF 2023 | Trimestral |
| Resolutividad APS | Consultas resueltas sin derivar / Total consultas × 100 | ≥85 % | OCDE 85-90 % | OCDE 2023 | Trimestral |
| Consultas urgencia evitable | Consultas SUH categoría C4-C5 de población inscrita / Total consultas SUH × 100 | ≤30 % | — | MINSAL 2022 | Mensual |
| EMPA/EFAM cobertura | Exámenes realizados / Población meta × 100 | ≥50 % | — | MINSAL 2023 | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Baja resolutividad → sobreuso urgencia | Telemedicina, eConsult, ecografía point-of-care en APS |
| Pérdida de seguimiento crónicos | Alerta automática en HCE, rescate telefónico, visita domiciliaria |
| Rotación profesional alta | Incentivos zona, formación en servicio, ratio ≤1:4.000 inscritos |
| Fragmentación información | HCE compartida con nivel secundario, interoperabilidad FHIR |

Ref: Modelo de Atención Integral de Salud Familiar y Comunitaria MINSAL 2013; Ley 19.378 (Estatuto APS); OMS PHC 2018; Starfield 1998.

## 15.2 Centros de especialidad ambulatoria/CRS

Concentración de especialidades ambulatorias con modelo de triaje de interconsultas, gestión activa de listas de espera y maximización de productividad por box. eConsult como estrategia de resolución sin presencialidad.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Triaje de interconsultas | Priorización clínica (P1: <30d, P2: <90d, P3: <180d), rechazo justificado con retroalimentación a APS |
| Gestión listas de espera | Tablero por especialidad, depuración periódica, contactabilidad, oferta-demanda |
| Productividad box | Rendimiento hora/médico, agendas protegidas, control ausentismo |
| eConsult/telemedicina | Resolución asincrónica especialista-APS, evita derivación innecesaria |
| Coordinación SOME | Central de agendamiento integrada, confirmación telefónica/SMS |
| Exámenes previos | Protocolo de preparación, paquetes diagnósticos por patología |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Espera mediana por especialidad | Mediana días desde IC aceptada hasta atención | ≤90 d (P2) | UK RTT 62 % <18 wk | MINSAL-SIGTE 2023 | Mensual |
| Productividad agenda | Pacientes atendidos / Cupos agendados × 100 | ≥85 % | — | MINSAL 2022 | Mensual |
| eConsult resolución | eConsult resueltas sin presencial / Total eConsult × 100 | ≥30 % | UCSF 40-70 % | AHRQ 2021 | Trimestral |
| Ausentismo consulta | Inasistencias / Citados × 100 | ≤15 % | NHS 5-8 % | NHS England 2023 | Mensual |
| IC rechazadas con retroalimentación | IC rechazadas con informe / Total IC rechazadas × 100 | 100 % | — | Buena práctica | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Listas de espera crecientes | Priorización clínica, oferta complementaria (telemedicina, compra servicios) |
| Ausentismo alto | Confirmación 48h antes (SMS/IVR), sobre-agendamiento controlado |
| IC innecesarias | Protocolos de referencia APS, eConsult, capacitación bidireccional |

Ref: Orientaciones Técnicas Listas de Espera MINSAL 2022; NICE NG94 referral guidelines 2023; AHRQ eConsult evidence 2021.

## 15.3 Hospital de día médico/quirúrgico

Atención de procedimientos y tratamientos que requieren observación <12h sin pernocta. Selección rigurosa de casos, protocolos fast-track y alta segura mismo día.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Selección de casos | Criterios ASA I-II, procedimiento compatible, red apoyo domiciliario |
| Protocolos fast-track | Ayuno mínimo, analgesia multimodal, movilización precoz, alta criterios |
| Circuito paciente | Admisión → preparación → procedimiento → recuperación → alta con indicaciones |
| Gestión de sillones/camas día | Programación por bloques, rotación AM/PM, overbooking controlado |
| Quimioterapia ambulatoria | Protocolos oncología, premedicación, monitoreo reacciones |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cancelaciones mismo día | Cancelaciones / Programados × 100 | <5 % | BADS UK 3-5 % | BADS 2022 | Mensual |
| Complicaciones <72h | Pacientes con complicación / Total atendidos × 100 | <2 % | BADS UK 1-2 % | AHRQ 2021 | Mensual |
| Ocupación silla/cama día | Horas ocupadas / Horas disponibles × 100 | ≥80 % | — | NICE 2019 | Mensual |
| Conversión a hospitalización | Pacientes que requieren pernocta / Total × 100 | <3 % | — | BADS 2022 | Mensual |
| Satisfacción paciente | Score encuesta post-atención | ≥85 % | — | IHI 2022 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Complicación post-alta sin supervisión | Llamada telefónica 24h, indicaciones escritas, línea emergencia |
| Selección inadecuada de pacientes | Checklist criterios estandarizado, evaluación preanestésica |
| Cancelaciones por falta de insumos | Stock mínimo protegido, gestión abastecimiento dedicada |

Ref: BADS (British Association of Day Surgery) Directory 2022; NICE CG45; IAAS International Association for Ambulatory Surgery 2021.

## 15.4 Imagenología, teleradiología

Servicios de diagnóstico por imagen (RX, US, CT, RM) con priorización clínica, integración RIS/PACS/HIS y cobertura teleradiología para centros remotos.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Priorización clínica | Urgente (<1h informe), preferente (<24h), rutina (<48-72h) |
| RIS/PACS/HIS | Integración trazabilidad solicitud-imagen-informe, DICOM, HL7/FHIR |
| Teleradiología | Lectura remota para centros sin radiólogo presencial, 24/7 |
| Protocolos contraste | Evaluación función renal, consentimiento, manejo reacción adversa |
| Control dosis radiación | DLP/CTDIvol registro, auditoría ALARA, niveles referencia diagnósticos |
| Mantención equipos | Plan mantención preventiva, certificación ISP, obsolescencia programada |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Turnaround informe (urgente) | Mediana tiempo solicitud→informe definitivo | <1 h | ACR <1h crítico | ACR 2020 | Mensual |
| Turnaround informe (rutina) | Mediana tiempo solicitud→informe definitivo | <48 h | — | ACR 2020 | Mensual |
| Repeat rate | Exámenes repetidos / Total exámenes × 100 | <5 % | ACR <5 % | ACR 2020 | Trimestral |
| Incidentes contraste | Reacciones adversas / Total exámenes con contraste × 100 | <1 % | 0.2-0.7 % | ACR Manual Contrast 2021 | Trimestral |
| Disponibilidad equipos | Horas operativas / Horas programadas × 100 | ≥95 % | — | OMS 2017 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Demora informes críticos | Alerta automática hallazgos críticos (ACR), comunicación directa con clínico |
| Falla PACS/pérdida imagen | Redundancia almacenamiento, backup diario, disaster recovery |
| Sobreuso CT/RM | Criterios de pertinencia (ACR Appropriateness Criteria), auditoría |

Ref: ACR Practice Parameters 2020; ACR Appropriateness Criteria; MINSAL Orientaciones Imagenología 2019; ISP regulación equipos.

## 15.5 Laboratorio clínico y bancos de sangre

Gestión del ciclo pre-analítico → analítico → post-analítico con control TAT por tipo de prueba, seguridad transfusional y acreditación.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Fase pre-analítica | Identificación positiva, toma de muestra estandarizada, transporte cadena frío |
| TAT por tipo | Urgentes <1h, rutina <4h ambulatorio / <24h hospitalizado, especializados según protocolo |
| Control calidad | QC interno diario, programa externo (PEEC), acreditación ISO 15189 |
| Banco de sangre | Tamizaje, tipificación, compatibilidad, hemovigilancia, stock mínimo por grupo |
| LIS/HIS integración | Resultados automáticos en HCE, alertas valores críticos, delta-check |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| TAT p90 (urgente) | Percentil 90 tiempo recepción→resultado | <60 min | CAP <60 min | CAP 2022 | Mensual |
| Tasa hemólisis | Muestras hemolizadas / Total muestras × 100 | <2 % | CAP <2 % | CAP 2022 | Mensual |
| Stock hemocomponentes | Días cobertura por grupo sanguíneo | ≥3 d | OMS ≥3d | OMS Blood Safety 2022 | Semanal |
| Valores críticos notificados <30 min | Notificados en tiempo / Total valores críticos × 100 | ≥95 % | CAP 95 % | CAP 2022 | Mensual |
| Reacciones transfusionales | Reacciones / Total transfusiones × 100 | <0.5 % | 0.1-0.3 % | AABB 2023 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Error identificación muestra | Pulsera + verificación positiva en cabecera, código de barras |
| Desabastecimiento hemocomponentes | Red de bancos, convenios interinstitucionales, stock seguridad |
| Resultado erróneo por interferencia | Delta-check automático, QC diario, repetición ante discordancia |

Ref: ISO 15189:2022; CAP Accreditation Checklist 2022; AABB Standards 2023; MINSAL Norma Técnica Bancos de Sangre.

## 15.6 Farmacia clínica y logística de medicamentos

Trazabilidad completa del medicamento, conciliación en transiciones asistenciales, gestión diferenciada de medicamentos de alto riesgo (MAR) y dispensación segura.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Trazabilidad | Recepción → almacenamiento → dispensación → administración, código de barras/RFID |
| Conciliación medicamentosa | Ingreso, traslado, alta — listado completo verificado con paciente/cuidador |
| Medicamentos alto riesgo (MAR) | ISMP lista, almacenamiento segregado, doble verificación, etiquetado especial |
| Dispensación unitaria | Dosis unitaria, carro automatizado (Pyxis/Omnicell), verificación farmacéutica |
| Farmacovigilancia | Notificación RAM, análisis causalidad, reporte ISP |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Errores medicación | Errores detectados / 1.000 prescripciones | <5 ‰ | ISMP <5 ‰ | ISMP 2022 | Mensual |
| Stock-out medicamentos esenciales | Días con quiebre / Días totales × 100 | <2 % | — | OMS 2022 | Mensual |
| Conciliación al ingreso | Pacientes con conciliación completa / Ingresos × 100 | ≥90 % | IHI 95 % | IHI 2022 | Mensual |
| Conciliación al alta | Pacientes con conciliación + educación / Altas × 100 | ≥85 % | — | NICE NG5 2015 | Mensual |
| Cumplimiento MAR | Auditoría doble-check MAR cumplido / Total MAR × 100 | ≥95 % | — | ISMP 2022 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Error de prescripción | CPOE con alertas, farmacéutico clínico en ronda |
| Quiebre stock crítico | Stock seguridad, alternativas terapéuticas predefinidas, compra de emergencia |
| Omisión conciliación en transiciones | Automatización alerta HCE en ingreso/traslado/alta |

Ref: ISMP High-Alert Medications 2022; NICE NG5 Medicines Optimisation 2015; OMS Medication Without Harm 2017; Ley 20.724 (Farmacovigilancia Chile).

## 15.7 Esterilización (CME)

Central de mezclas estériles y esterilización de instrumental. Flujos unidireccionales sucio→limpio, trazabilidad completa set-paciente-procedimiento, control biológico.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Flujo sucio-limpio | Unidireccional: recepción → lavado → inspección → empaque → esterilización → almacén estéril |
| Trazabilidad | Código de barras por set, registro ciclo-autoclave-lote, vinculación paciente-procedimiento |
| Control biológico | Indicador biológico cada carga (Geobacillus stearothermophilus), integrador químico clase 5/6 |
| Mantención autoclaves | Plan preventivo, calificación IQ/OQ/PQ, registro parametría cada ciclo |
| Instrumental externo/préstamo | Protocolo recepción, reprocesamiento completo, cuarentena |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Fallas esterilidad | Indicadores biológicos positivos / Total cargas × 100 | 0 % | 0 % | AAMI ST79 | Por carga |
| Rotación set quirúrgico | Sets utilizados / Sets disponibles | ≥2 rotaciones/d | — | AORN 2022 | Mensual |
| No conformidades | Incidentes proceso / Total sets procesados × 1.000 | <2 ‰ | — | ISO 17665 | Mensual |
| Tiempo reprocesamiento | Tiempo recepción sucio → disponible estéril | <4 h estándar | — | AAMI 2017 | Mensual |
| Trazabilidad completa | Sets con registro completo ciclo+paciente / Total × 100 | 100 % | — | Buena práctica | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Contaminación post-esterilización | Almacenamiento sellado, control ambiental, caducidad empaque |
| Falla autoclave sin detección | Indicador biológico obligatorio, cuarentena hasta resultado |
| Rotura cadena trazabilidad | Código barras obligatorio, auditoría semanal |

Ref: AAMI ST79:2017; ISO 17665-1:2006; AORN Guidelines Perioperative 2022; MINSAL Norma Técnica CME.

## 15.8 Rehabilitación/Kinesiología

Servicios de rehabilitación integral (kinesiología, fonoaudiología, terapia ocupacional) con énfasis en adherencia, continuidad hospital-domicilio y medición de resultados funcionales (PROMs).

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Evaluación funcional estandarizada | FIM, Barthel, TUG, 6MWT según condición |
| Plan rehabilitación individualizado | Metas SMART, frecuencia, modalidad (presencial/tele/domiciliario) |
| Continuidad hospital-domicilio | Alta kinésica con plan domiciliario, derivación CESFAM, tele-rehabilitación |
| Adherencia | Monitoreo asistencia, rescate inasistentes, ajuste plan según barreras |
| PROMs | Medición al inicio, intermedia y alta con instrumentos validados |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Asistencia a sesiones | Sesiones asistidas / Sesiones programadas × 100 | ≥80 % | — | OMS Rehab 2030 | Mensual |
| PROMs funcionales (mejora) | Pacientes con mejora ≥MCID / Total × 100 | ≥70 % | — | ICHOM 2022 | Trimestral |
| Alta oportuna rehabilitación | Altas dentro plazo plan / Total altas × 100 | ≥75 % | — | NHS Rehab 2022 | Trimestral |
| Derivación continuidad APS | Pacientes derivados con plan a APS / Total altas × 100 | ≥90 % | — | Buena práctica | Mensual |
| Inicio rehabilitación precoz | Inicio ≤48h post-evento (ACV, cirugía) / Total indicados × 100 | ≥80 % | ESO 2022 <24h ACV | ESO Guidelines 2022 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Abandono tratamiento | Tele-rehabilitación, horarios flexibles, educación al paciente |
| Pérdida funcional por inicio tardío | Protocolo movilización precoz, alerta automática en HCE |
| Falta de continuidad post-alta | Coordinación APS, plan escrito al paciente, control telefónico |

Ref: OMS Rehabilitation 2030; ESO Guidelines ACV 2022; ICHOM Standard Sets; NHS Rehabilitation Framework 2022.

## 15.9 Odontología

Atención odontológica programada (GES odontológico: 6 años, embarazada, 60 años, urgencia) y de urgencia. Control riguroso IPC por aerosoles.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| GES odontológico | Salud oral integral 6 años, embarazada, 60 años — canasta prestaciones definida |
| Urgencia dentaria | Triage odontológico, atención <24h dolor/infección/trauma |
| Control IPC | Precauciones estándar + aerosoles, esterilización rotatorio, barrera ambiental |
| Odontología comunitaria | Programa preventivo escolar (sellantes, flúor), educación |
| Registro clínico | Odontograma digital, integración HCE, trazabilidad materiales |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Oportunidad GES odontológico | Pacientes atendidos en plazo GES / Total garantías × 100 | 100 % | Garantía legal | MINSAL-GES 2023 | Mensual |
| TAT urgencia odontológica | Mediana tiempo consulta→resolución | <24 h | — | MINSAL 2022 | Mensual |
| IAAS asociada procedimiento dental | Infecciones post-procedimiento / Total procedimientos × 1.000 | <1 ‰ | — | CDC Dental IPC 2016 | Trimestral |
| Cobertura sellantes 6 años | Niños sellados / Población meta × 100 | ≥70 % | OMS 80 % | MINSAL 2023 | Anual |
| Cumplimiento protocolo IPC | Auditoría cumplimiento / Total auditorías × 100 | ≥95 % | — | CDC 2016 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Contaminación cruzada aerosoles | Aspiración alto volumen, ventilación, EPP completo |
| Incumplimiento GES por demanda | Extensión horaria, listas de espera con priorización |
| Falla esterilización instrumental rotatorio | Autoclave clase B dedicado, trazabilidad por ciclo |

Ref: MINSAL Norma Técnica Odontológica GES 2023; CDC Guidelines Dental IPC 2016; FDI Vision 2030.
