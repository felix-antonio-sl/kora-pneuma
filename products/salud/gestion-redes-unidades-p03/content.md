---
urn: urn:salud:kb:gestion-redes-unidades-p03
nombre: gestion-redes-unidades-p03
version: 2.0.0
estado: publicado
descripcion: "Gestión de Redes Asistenciales — Gestión por Tipo de Unidad - Parte 03"
fuente: "Migrado de la bestia (~/kora @ 9de5dc38b78c23574d24a481a5f84d70173c2203) artifacts/knowledge/salud/salubrista/gestion-redes/02-unidades-asistenciales--p03.md (sha256:36a53b616c0bdef128597363a89edd273a041eef131679b2a458e3fc786cec6d) el 2026-07-17; cuerpo byte-fiel; frontmatter normalizado a ley/2; shard enlazado por cita a urn:salud:kb:gestion-redes-unidades."
autor: FS
creado: 2026-03-03
lang: es
tags: [gestion-redes, unidades, ambulatorio, hospitalario, hospital-at-home, HaH, asistencial]
familia: bok
cita: [urn:salud:kb:gestion-redes-unidades]
---

# Gestión de Redes Asistenciales — Gestión por Tipo de Unidad - Parte 03

## 16.5 Pediatría

Hospitalización pediátrica con énfasis en seguridad de medicamentos (dosificación por peso), prevención de EA específicos y experiencia niño/familia.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Seguridad medicamento pediátrico | Dosis kg/peso, doble-check, formulario pediátrico, bombas programadas |
| Hospitalización acompañada | Derecho acompañamiento 24h (Ley 20.584), participación cuidador en plan |
| Dolor pediátrico | Escalas edad-específicas (FLACC, Wong-Baker, EVA), protocolo analgesia |
| Juego terapéutico | Preparación procedimientos, distracción, ambiente amigable |
| Transición a adulto | Protocolo para crónicos pediátricos (>15 años), derivación coordinada |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Eventos dosificación | Errores dosis pediátrica / Total prescripciones pediátricas × 1.000 | <3 ‰ | — | ISMP 2022 | Mensual |
| Satisfacción cuidadores | Score encuesta padres/cuidadores | ≥85 % | — | Picker Institute 2022 | Trimestral |
| Reingresos 7d (pediátrico) | Reingresos ≤7d / Egresos pediátricos × 100 | <5 % | — | AHRQ PDI 2022 | Mensual |
| Dolor controlado | Pacientes con score dolor ≤3 / Total evaluados × 100 | ≥80 % | — | IHI 2022 | Mensual |
| Cumplimiento doble-check MAR | Auditoría MAR pediátrico / Total MAR × 100 | 100 % | — | ISMP 2022 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Error dosificación 10× | Peso obligatorio en prescripción, CPOE pediátrico, doble verificación |
| Angustia niño/familia | Preparación pre-procedimiento, juego terapéutico, ambiente |
| Deterioro rápido | PEWS (Pediatric Early Warning Score), escalamiento protocolizado |

Ref: ISMP Pediatric Medication Safety 2022; AHRQ Pediatric Quality Indicators 2022; Picker Institute Patient Experience; PEWS validación.

## 16.6 Oncología integral

Gestión del continuo oncológico: sospecha → confirmación → etapificación → tratamiento → seguimiento. Tiempos como métrica clave (GES oncológicos). Seguridad en quimioterapia.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Tiempos diagnóstico-tratamiento | GES: sospecha→confirmación ≤30d, confirmación→etapificación ≤15d, etapificación→tratamiento según patología |
| Comité oncológico | Multidisciplinario (cirugía, oncología médica, radio, patología, enfermería), decisión consensuada |
| Seguridad quimioterapia | Preparación centralizada (campana flujo laminar), verificación esquema, extravasación, derrames |
| Cuidados de soporte | Antiemesis, dolor, nutrición, psicooncología, rehabilitación |
| Navegación paciente | Navigator oncológico, coordinación exámenes/tratamientos, apoyo GES |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo sospecha→tratamiento | Mediana días desde IC sospecha hasta inicio tratamiento | Según GES por patología | UK 62d cancer target | NHS Cancer Waiting Times 2023 | Mensual |
| Eventos adversos quimioterapia | EA grado ≥3 (CTCAE) / Total ciclos × 100 | <10 % | — | ASCO 2022 | Mensual |
| Mortalidad ≤30d post-quimio | Muertes ≤30d / Total pacientes en QT × 100 | <3 % (curativo) | NCRAS UK 2.5 % | NCRAS 2022 | Trimestral |
| Comité oncológico | Pacientes discutidos en comité / Total pacientes nuevos × 100 | ≥90 % | — | NICE IOG 2022 | Mensual |
| Supervivencia 1 año proxy | Sobrevida 1 año por tipo tumoral | Según registro nacional | — | RNT Chile | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Demora diagnóstica (pérdida ventana) | Vía rápida oncológica, navigator, alerta lista espera |
| Error preparación quimio | Preparación centralizada, doble verificación, código barras |
| Extravasación vesicante | Protocolo extravasación, kit antídoto, capacitación enfermería |

Ref: GES oncológicos MINSAL 2023; ASCO/ONS Chemotherapy Safety Standards 2022; NICE Improving Outcomes Guidance 2022; NHS Cancer Waiting Times.

## 16.7 Gestión de camas

Asignación dinámica de camas, gestión del boarding en SUH, promoción de altas matutinas y coordinación con alternativas a la hospitalización.

> La hospitalización domiciliaria (cap 17) libera camas físicas para pacientes de mayor agudeza — efecto backfill: cada cama HaH permite ingresar un paciente de mayor complejidad, generando margen incremental.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Asignación dinámica | Central de camas 24/7, priorización por gravedad y flujo, matching cama-necesidad |
| Gestión boarding | Tiempo máximo boarding SUH <4h, protocolo escalamiento, expansión camas |
| Altas matutinas | Meta altas antes 12:00, ronda alta 08:00, trámites noche previa |
| Alternativas hospitalización | Hospital at Home (cap 17), hospital de día, alta con seguimiento telefónico |
| Dashboards tiempo real | Ocupación por servicio, camas disponibles, EDD, boarding, flujo entrada/salida |

**IF/THEN — Decisión gestión camas:**

| Condición | Acción |
|-----------|--------|
| IF ocupación ≥90 % | THEN activar protocolo contingencia: acelerar altas, evaluar HaH, suspender electivas |
| IF boarding SUH >4h | THEN escalar a dirección, apertura camas contingencia, redistribución |
| IF ocupación <70 % (sostenido) | THEN consolidar unidades, redistribuir dotación, oferta a red |
| IF paciente elegible HaH | THEN derivar a equipo HaH (cap 17), liberar cama física |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Ocupación camas | Días-cama ocupados / Días-cama disponibles × 100 | 85-90 % | NHS 85 % ideal | NHS 2023 | Diario |
| Boarding SUH >4h | Pacientes con boarding >4h / Total ingresos desde SUH × 100 | <10 % | — | ACEP 2022 | Diario |
| Altas antes 12:00 | Altas ≤12:00 / Total altas del día × 100 | ≥33 % | NHS ECIST 33 % | NHS ECIST 2022 | Diario |
| Camas liberadas por HaH | Pacientes derivados a HaH / Total egresos × 100 | ≥5 % (en programas activos) | — | HaH evidence | Mensual |
| Estancia social (bed-blocking) | Días-cama por causa social / Total días-cama × 100 | <5 % | — | NHS Delayed Transfers 2023 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Sobreocupación (>95 %) → EA | Protocolo contingencia, HaH, compra servicios, derivación red |
| Alta prematura → reingreso | Checklist alta segura, EDD con criterios clínicos, seguimiento 48h |
| Bed-blocking social | Coordinación trabajo social precoz, red sociosanitaria, hogar protegido |

Ref: NHS ECIST (Emergency Care Intensive Support Team) 2022; ACEP Boarding Position Statement 2022; AHRQ Bed Management 2021; evidencia HaH backfill.

---

## 17.1 Modelos y evidencia

Dos modelos principales: evitación de ingreso (admission avoidance) y alta precoz apoyada (early supported discharge). Evidencia robusta de ensayos controlados y revisiones sistemáticas.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Admission avoidance | Paciente identificado en SUH/urgencia, derivado a domicilio en lugar de hospitalización convencional |
| Early supported discharge (ESD) | Paciente estabilizado en hospital (24-72h), completa tratamiento en domicilio |
| Modelo híbrido | Combinación según perfil clínico y capacidad operativa del programa |

**Evidencia síntesis:**

| Desenlace | Hospital at Home | Hospitalización convencional | Fuente |
|-----------|-----------------|------------------------------|--------|
| Mortalidad (RR) | 0.77-0.84 | 1.0 (referencia) | Cochrane Shepperd 2016; Levine 2020 |
| Reingresos 30d | 7-8.6 % | 15.6-23 % | Levine 2020; MGB 2022 |
| Costo por episodio | 19-38 % menor | Referencia | CMS AHCAH 2023; Levine 2020 |
| LOS (días) | 3.2 (mediana) | 4.9-5.5 | Leff 2005; Caplan 2012 |
| Satisfacción (score) | 90.7 % | 83.9 % | Leff 2005; Federman 2018 |
| Delirium | 9 % | 24 % | Caplan 2006; Levine 2020 |
| Caídas | Similar o menor | Referencia | Cochrane 2016 |
| Actividad física (accelerómetro) | +17 min/d ambulando | Referencia | Levine 2020 |

**IF/THEN — Selección de modelo:**

| Condición | Modelo recomendado |
|-----------|-------------------|
| IF paciente en SUH con criterio de ingreso + elegible + sin necesidad UCI | THEN admission avoidance |
| IF paciente hospitalizado ≥24h, estable, en trayectoria mejoría | THEN early supported discharge |
| IF programa incipiente (<6 meses operación) | THEN iniciar con ESD (menor riesgo operacional), escalar a admission avoidance |
| IF domicilio no cumple criterios ambientales | THEN hospitalización convencional (no elegible HaH) |
| IF cuidador no disponible o no capacitable | THEN evaluar caso a caso; considerar cuidador profesional o excluir |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Mortalidad HaH | Muertes / Total episodios HaH × 100 | ≤2 % | Cochrane RR 0.77-0.84 | Cochrane 2016 | Trimestral |
| Reingresos 30d HaH | Reingresos / Egresos HaH × 100 | <10 % | Levine 7-8.6 % | Levine 2020 | Mensual |
| Costo vs. hospitalización convencional | Costo HaH / Costo convencional × 100 | ≤80 % | 62-81 % | CMS 2023 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Deterioro no detectado en domicilio | RPM continuo, escalamiento protocolizado, umbral bajo para re-hospitalización |
| Selección inadecuada de modelo | Criterios estandarizados, experiencia ESD antes de admission avoidance |
| Sesgo de selección (solo pacientes "fáciles") | Ampliar criterios progresivamente, auditoría case-mix |

Ref: Cochrane Shepperd et al. 2016; Levine et al. JAMA IM 2020; Leff et al. JAGS 2005; Caplan et al. MJA 2012; CMS AHCAH 2023.

## 17.2 Elegibilidad y criterios de admisión

Selección rigurosa del paciente: criterios clínicos, funcionales, ambientales y de consentimiento. Patologías prevalentes definidas por evidencia y viabilidad operativa.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Criterio clínico general | Requiere hospitalización (no ambulatorio), no requiere UCI, condición en lista elegible |
| Patologías prevalentes | NAC, ICC descompensada, EPOC exacerbada, celulitis, ITU/pielonefritis, TVP/TEP estable |
| Criterio funcional | Consciente, capaz de comunicar síntomas (o cuidador), cooperador |
| Criterio ambiental | Domicilio con electricidad, agua potable, teléfono/conectividad, radio ≤30 km del hospital |
| Criterio social | Cuidador disponible ≥parte del día, red apoyo, consentimiento informado firmado |
| Exclusiones | Inestabilidad hemodinámica, necesidad monitorización invasiva, riesgo social grave, adicción activa no controlada, psiquiatría aguda |

**IF/THEN — Elegibilidad:**

| Condición | Decisión |
|-----------|----------|
| IF paciente requiere hospitalización + condición en lista + no UCI | THEN evaluar criterios ambientales y sociales |
| IF domicilio sin electricidad o agua potable | THEN excluir HaH |
| IF sin cuidador y paciente autovalente + bajo riesgo | THEN evaluar caso a caso con visita previa |
| IF paciente rechaza o retira consentimiento | THEN hospitalización convencional (derecho irrenunciable) |
| IF radio >30 km y sin base periférica | THEN excluir HaH (tiempo respuesta inseguro) |
| IF adicción activa con riesgo de abandono tratamiento IV | THEN excluir HaH |
| IF paciente con demencia sin cuidador capacitado | THEN excluir HaH |
| IF condición clínica no en lista pero médico tratante fundamenta | THEN evaluar en comité HaH, ampliar criterio si pertinente |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tasa elegibilidad | Pacientes elegibles / Total ingresos hospitalarios × 100 | 10-30 % | Johns Hopkins 25-30 % | Leff 2005 | Mensual |
| Aceptación paciente | Pacientes que aceptan / Pacientes elegibles × 100 | ≥70 % | — | MGB 2022 | Mensual |
| Tasa escalamiento (retorno hospital) | Pacientes retornados / Total HaH × 100 | ≤10 % | 7-10 % | Levine 2020 | Mensual |
| Screening completado | Evaluaciones elegibilidad realizadas / Candidatos identificados × 100 | ≥90 % | — | Buena práctica | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Criterios demasiado restrictivos → bajo volumen | Revisión periódica, benchmarking, ampliación progresiva |
| Criterios laxos → eventos adversos | Auditoría escalamientos, mortalidad, comité calidad |
| Sesgo socioeconómico en elegibilidad | Evaluación equidad, apoyo transporte/conectividad, equipo social |

Ref: Levine et al. Annals IM 2020 (criterios JHH); Leff et al. JAGS 2005; CMS AHCAH Waiver criteria 2023; Hospital Clínic Barcelona protocolo 2022.

## 17.3 Modelo operativo y dotación

Equipo multidisciplinario dedicado con cobertura 24/7, logística de medicamentos e insumos a domicilio y centro de mando como eje coordinador.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Médico | Visita presencial diaria (o cada 48h si estable), disponibilidad 24/7 (telemedicina + presencial urgente) |
| Enfermería | 1-2 visitas/día, ratio 1:4-1:6 pacientes, procedimientos (IV, curación, monitoreo) |
| Paramédico/TENS | Apoyo enfermería, toma muestras, transporte insumos, educación cuidador |
| Kinesiología/TO | Según indicación: rehabilitación respiratoria, movilización, AVD |
| Trabajo social | Evaluación ambiental, apoyo cuidador, gestión red sociosanitaria |
| Centro de mando (command center) | Recepción alertas RPM, coordinación visitas, triage telefónico, despacho emergencia |
| Farmacia | Dispensación y entrega domiciliaria (incl. medicamentos IV), conciliación |
| Logística equipos | Oxígeno domiciliario, bombas infusión, concentrador O2, equipo diagnóstico portátil |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo respuesta emergencia | Minutos desde alerta hasta llegada equipo al domicilio | <60 min | — | Buena práctica HaH | Mensual |
| Visitas cumplidas | Visitas realizadas / Visitas programadas × 100 | ≥95 % | — | Buena práctica | Semanal |
| Ratio enfermería | Pacientes activos / Enfermeras turno | 1:4-1:6 | JHH 1:4 | Johns Hopkins HaH | Diario |
| Disponibilidad 24/7 | Horas con cobertura efectiva / 168 h semana × 100 | 100 % | — | CMS AHCAH requisito | Semanal |
| Medicamentos entregados oportunamente | Entregas en tiempo / Total entregas × 100 | ≥95 % | — | Buena práctica | Semanal |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Dotación insuficiente → sobrecarga | Ratio estricto, pool de relevo, expansión gradual censo |
| Demora respuesta emergencia | Zona geográfica acotada, vehículo dedicado, protocolo SAMU complementario |
| Falla entrega medicamento IV | Stock buffer domicilio, farmacia con delivery, protocolo contingencia oral |

Ref: Johns Hopkins Hospital at Home Model; Mount Sinai HaH operational guide; CMS AHCAH Conditions of Participation 2023; MGB Home Hospital operations 2022.

## 17.4 Infraestructura tecnológica y RPM

Monitorización remota de pacientes (RPM) como pilar de seguridad. Dispositivos, plataforma de telesalud, integración con HCE y sistemas de alerta con soporte de inteligencia artificial.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Dispositivos RPM | SpO2, presión arterial, frecuencia cardíaca, temperatura, frecuencia respiratoria, ECG single-lead, peso, glucómetro |
| Plataforma telesalud | Videollamada paciente-equipo, chat asincrónico, educación multimedia |
| Integración HCE | Flujo bidireccional FHIR R4: signos vitales RPM → HCE, órdenes HCE → dispositivos |
| Alertas y CDS | Umbrales personalizados por patología, escalamiento automático, trending |
| IA predictiva | Modelos de deterioro temprano (MEWS modificado, redes neuronales sobre series temporales RPM) |
| Conectividad | Tablet/smartphone con datos móviles provistos, gateway Bluetooth, hotspot si necesario |

**IF/THEN — Alertas RPM:**

| Condición | Acción |
|-----------|--------|
| IF SpO2 <90 % (o caída >4 % desde basal) | THEN alerta roja → llamada inmediata + evaluar visita presencial/SAMU |
| IF PA sistólica >180 o <90 mmHg | THEN alerta roja → contacto médico, evaluación presencial |
| IF FC >120 o <50 bpm (sostenido >10 min) | THEN alerta naranja → evaluación enfermería telefónica + presencial si persiste |
| IF temperatura >38.5 °C | THEN alerta naranja → contacto enfermería, evaluación foco, hemocultivos si indicados |
| IF peso +1.5 kg en 24h (ICC) | THEN alerta naranja → ajuste diurético, restricción hídrica, evaluación médica |
| IF sin transmisión datos >4h (paciente despierto) | THEN alerta técnica → llamada verificación, visita si no contactable |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Adherencia RPM | Transmisiones recibidas / Transmisiones esperadas × 100 | ≥85 % | — | CMS AHCAH 2023 | Semanal |
| Tiempo respuesta alerta roja | Minutos desde alerta hasta contacto clínico | <15 min | — | Buena práctica | Mensual |
| Falsas alarmas | Alertas sin acción clínica / Total alertas × 100 | <30 % | — | Literature RPM 2022 | Mensual |
| Integración HCE | Datos RPM volcados automáticamente / Total datos × 100 | ≥95 % | — | Estándar FHIR | Trimestral |
| Satisfacción tecnología (paciente) | Score facilidad de uso dispositivos | ≥80 % | — | SUS Scale | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Brecha digital paciente/cuidador | Capacitación in-situ, dispositivos simplificados, soporte técnico 24/7 |
| Fatiga de alertas (alert fatigue) | Umbrales personalizados, IA filtrado, priorización |
| Falla conectividad | Gateway offline con buffer, hotspot respaldo, protocolo llamada |
| Ciberseguridad datos salud | Encriptación end-to-end, cumplimiento HIPAA/Ley 19.628, auditoría accesos |

Ref: CMS AHCAH RPM requirements 2023; Current Health (Best Buy) platform; Biofourmis AI; FHIR R4 Vital Signs IG; Ley 19.628 (Datos Personales Chile).
