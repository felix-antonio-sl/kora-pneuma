---
urn: urn:salud:kb:gestion-redes-urgencias-p03
nombre: gestion-redes-urgencias-p03
version: 2.0.0
estado: publicado
descripcion: "Gestión de Redes Asistenciales — Red de Urgencias - Parte 03"
fuente: "Migrado de la bestia (~/kora @ 9de5dc38b78c23574d24a481a5f84d70173c2203) artifacts/knowledge/salud/salubrista/gestion-redes/03-urgencias--p03.md (sha256:29b083674ecae12e018c76144c654a274415c1625e01e485c72c49912730c00c) el 2026-07-17; cuerpo byte-fiel; frontmatter normalizado a ley/2; shard enlazado por cita a urn:salud:kb:gestion-redes-urgencias."
autor: FS
creado: 2026-03-03
lang: es
tags: [gestion-redes, urgencias, emergencias, EMS, SUH, protocolos, triaje, desastres, MCI]
familia: bok
cita: [urn:salud:kb:gestion-redes-urgencias]
---

# Gestión de Redes Asistenciales — Red de Urgencias - Parte 03

## 21.3 Colas en sala de espera/box

Gestión de colas y tiempos de espera dentro del SUH. Estrategias para reducir waiting time y optimizar throughput sin comprometer seguridad.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Límites WIP (Work In Progress) | Máximo pacientes simultáneos por circuito: reanimación (2-3), estándar (según boxes), fast track (según dotación) |
| Médico de triaje | Evaluación médica inicial en triaje para ESI 2-3: solicitar estudios anticipadamente |
| Pull system | Paciente "jala" al siguiente paso cuando hay capacidad, no empuje desde cola |
| Señalización tiempos | Pantalla pública con tiempo espera estimado por nivel de triaje |
| Rondas de espera | Enfermería revisa pacientes en espera cada 30 min (analgesia, re-evaluación, hidratación) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo espera ESI 3 | Mediana minutos triaje → primer contacto médico (ESI 3) | ≤30 min | ACEP: ≤30 min | ACEP 2023 | Mensual |
| LWBS | Pacientes que abandonan sin ser vistos / Total consultas × 100 | ≤3 % | ACEP: ≤2 % | ACEP 2023 | Mensual |
| Ocupación SUH | Pacientes presentes / Capacidad nominal SUH × 100 | ≤100 % | — | EDIS | Tiempo real |
| Throughput médico | Pacientes dados de alta + hospitalizados por hora / Médicos en turno | ≥1.5 pac/méd/hora | — | EDIS | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Espera prolongada sin re-evaluación | Rondas de enfermería, re-triaje protocolizado |
| WIP excedido sin acción | Gatillo automático de surge al exceder 120 % capacidad |

Ref: IHI Optimizing Patient Flow 2003; Lean Healthcare — Toyota Production System; ACEP Crowding Solutions 2023.

## 21.4 Boarding y exit block

Pacientes con decisión de hospitalización que permanecen en SUH por falta de cama disponible (boarding). Principal causa de saturación y deterioro de indicadores de urgencia.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Boarding | Paciente con orden de hospitalización en SUH esperando cama de destino |
| Exit block | Bloqueo de salida: camas hospitalarias ocupadas por pacientes con alta demorada |
| Early discharge rounds | Ronda 08:00 para identificar altas del día, liberar camas antes de peak SUH |
| Camas swing | Camas polivalentes asignables a cualquier servicio según demanda |
| Full capacity protocol | Distribución de pacientes boarding a pasillos de servicios clínicos (no solo SUH) |
| Smoothing quirúrgico | Programación cirugía electiva lunes-viernes para evitar peak egresos lunes |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Boarding time | Mediana horas decisión hospitalización → salida SUH a cama | ≤2h | ACEP: ≤60 min; UK NHS: ≤4h total | ACEP 2023 | Mensual |
| Pacientes boarding >6h | N° pacientes con boarding >6h / Total boarding × 100 | ≤10 % | — | EDIS | Mensual |
| Hora alta efectiva | Mediana hora del día en que paciente deja cama hospitalaria | ≤11:00 | — | HCE | Mensual |
| Ocupación hospitalaria | Camas ocupadas / Camas habilitadas × 100 | 85-90 % | IHI: ≤85 % para flujo óptimo | IHI 2019 | Diario |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Mortalidad aumentada por boarding | Full capacity protocol, escalamiento a dirección, notificación SEREMI |
| Resistencia de servicios a camas swing | Directriz institucional, gobernanza de camas centralizada |

Ref: ACEP Boarding Statement 2023; IHI Whole-System Flow; Innes et al. 2019 (boarding mortality); NHS England Urgent and Emergency Care.

## 21.5 Gatillos y contingencia (surge)

Sistema de niveles de contingencia con gatillos objetivos y acciones predefinidas para manejo de sobrecarga del SUH.

**IF/THEN — Niveles surge:**

| Nivel | Gatillo | Acciones | Responsable |
|-------|---------|----------|-------------|
| IF VERDE (normal) | Ocupación SUH ≤100 %, boarding ≤5 pacientes, LWBS ≤3 % | THEN operación estándar, monitoreo continuo | Jefe turno SUH |
| IF AMARILLO (alerta) | Ocupación 100-120 %, boarding 6-10 pacientes, espera ESI 3 >45 min | THEN activar médico de triaje, abrir boxes adicionales, ronda early discharge, notificar bed manager | Jefe turno SUH + Bed manager |
| IF ROJO (crisis) | Ocupación >120 %, boarding >10 pacientes, LWBS >5 %, espera ESI 3 >60 min | THEN full capacity protocol, redistribuir boarding a servicios, suspender cirugía electiva, convocar pool de refuerzo, notificar dirección | Director de turno + Dirección |
| IF NEGRO (catastrófico) | MCI o colapso sostenido >12h en nivel rojo | THEN activar plan MCI/HICS, desvío de ambulancias a SUH alternativo, solicitar apoyo inter-SS | Dirección + Centro Regulador |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Tablero surge | Dashboard tiempo real con semáforo automático basado en gatillos |
| Protocolo de desborde | Secuencia de acciones por nivel, checklist ejecutable |
| Comunicación de nivel | Notificación automática a stakeholders según nivel (SMS, email, radio) |
| Revisión post-surge | Debriefing estructurado post-evento para mejora continua |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Horas en nivel rojo | Horas acumuladas en nivel rojo / Horas totales mes × 100 | ≤5 % | — | Dashboard surge | Mensual |
| Tiempo respuesta a gatillo | Minutos entre activación gatillo y primera acción documentada | ≤15 min | — | Registros surge | Mensual |
| Frecuencia surge amarillo | N° activaciones amarillo / mes | Tendencia decreciente | — | Dashboard surge | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Normalización del nivel rojo | Análisis causa raíz mensual, plan de acción institucional |
| Fatiga de alarma | Umbrales calibrados trimestralmente, evitar sobre-gatillos |

Ref: IHI Surge Management; ACEP Crowding Solutions Toolkit 2023; NHS Operational Pressures Escalation Levels (OPEL).

## 22.1 Código ACV (IVT/Trombectomía)

Protocolo de activación y manejo del accidente cerebrovascular isquémico agudo. Ventana IVT ≤4.5h, trombectomía mecánica ≤24h (seleccionados). Cada minuto sin reperfusión = 1.9 millones de neuronas perdidas.

**Hitos tiempo-dependientes:**

| Hito | Meta | Benchmark | Responsable |
|------|------|-----------|-------------|
| Door-to-CT | ≤20 min | AHA/ASA 2024: ≤25 min | Enfermería triaje + radiólogo |
| Door-to-needle (IVT) | ≤60 min | AHA 2024: ≤45 min | Neurólogo/médico SUH |
| Door-to-groin (trombectomía) | ≤90 min | AHA 2024: ≤90 min | Neurointervencionista |
| Door-in-door-out (centro primario→comprensivo) | ≤45 min | AHA 2024 | Equipo SUH |
| NIHSS al ingreso | Documentado en ≤10 min | AHA 2024 | Médico SUH/neurólogo |
| Glicemia capilar | ≤5 min desde ingreso | AHA 2024 | Enfermería triaje |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Activación código ACV | ≥1 criterio Cincinnati + hora inicio conocida → activación |
| Centro ACV primario | IVT disponible 24/7, TC sin contraste, laboratorio urgente |
| Centro ACV comprensivo | IVT + trombectomía mecánica 24/7, neuro-UCI, neurocirugía |
| Telemedicina ACV | Tele-stroke para centros sin neurólogo presencial: evaluación remota NIHSS, decisión IVT |
| Kit ACV | Alteplasa/tenecteplasa pre-preparada, protocolo dosis, checklist contraindicaciones |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tasa IVT | Pacientes con IVT / ACV isquémico elegible × 100 | ≥25 % | AHA: ≥25 % | AHA 2024 | Trimestral |
| Door-to-needle ≤60 min | % IVT con DTN ≤60 min / Total IVT × 100 | ≥75 % | AHA: ≥75 % | AHA 2024 | Trimestral |
| Mortalidad intrahospitalaria ACV | Fallecidos / Total ACV ingresados × 100 | ≤15 % | — | GRD/HCE | Trimestral |
| mRS 0-2 a 90 días | Independencia funcional a 3 meses / Total ACV seguidos × 100 | ≥40 % | Ensayos trombectomía: 46 % | MR CLEAN 2015 | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Hora de inicio desconocida (wake-up stroke) | Protocolo RM-DWI/FLAIR mismatch, selección por imagen avanzada |
| Demora por consultas internas | Protocolo de activación paralela (lab + imagen + neurólogo simultáneos) |

Ref: AHA/ASA Guidelines Acute Ischemic Stroke 2024; ESO Guidelines 2022; MINSAL GES ACV.

## 22.2 Código IAM (STEMI/NSTEMI)

Protocolo de activación y manejo del síndrome coronario agudo. STEMI: reperfusión urgente (ICP primaria o fibrinólisis). NSTEMI: estratificación de riesgo y cateterismo según timing.

**Hitos tiempo-dependientes:**

| Hito | Meta | Benchmark | Responsable |
|------|------|-----------|-------------|
| Door-to-ECG | ≤10 min | AHA/ACC 2023: ≤10 min | Enfermería triaje |
| FMC-to-balloon (ICP primaria) | ≤90 min | ESC 2023: ≤60 min | Hemodinamia |
| Door-to-needle (fibrinólisis) | ≤30 min | AHA 2023: ≤30 min | Médico SUH |
| Door-to-balloon (ICP) | ≤60 min | AHA/ACC 2023 | Hemodinamia |
| ECG seriado si primer ECG no diagnóstico | Cada 15-30 min | AHA 2023 | Enfermería SUH |
| Troponina alta sensibilidad | Resultado ≤60 min (protocolo 0/1h o 0/3h) | ESC 2023 | Laboratorio |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Activación código IAM | Elevación ST en ECG (prehospitalario o SUH) → activación hemodinamia |
| Red STEMI | Hospitales con hemodinamia 24/7 como hubs, SUH periféricos como spokes con fibrinólisis |
| Estrategia farmacoinvasiva | Fibrinólisis en SUH sin ICP + traslado a ICP en 2-24h |
| NSTEMI risk stratification | GRACE score: alto riesgo → cateterismo ≤24h; muy alto riesgo → ≤2h |
| Doble antiagregación | Aspirina + inhibidor P2Y12 según protocolo local |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| FMC-to-balloon ≤90 min | % STEMI con FMC-balloon ≤90 min / Total STEMI reperfundidos × 100 | ≥75 % | AHA: ≥75 % | AHA 2023 | Trimestral |
| Tasa reperfusión STEMI | STEMI reperfundidos (ICP o fibrinólisis) / Total STEMI × 100 | ≥90 % | ESC: ≥90 % | ESC 2023 | Trimestral |
| Mortalidad intrahospitalaria STEMI | Fallecidos / Total STEMI × 100 | ≤7 % | ESC registros: 4-6 % | ESC 2023 | Trimestral |
| Door-to-ECG ≤10 min | % dolor torácico con ECG ≤10 min / Total dolor torácico × 100 | ≥90 % | AHA: ≥90 % | AHA 2023 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Hemodinamia no disponible 24/7 | Estrategia farmacoinvasiva + red de traslado, rotación equipos |
| STEMI no reconocido (ECG atípico) | ECG seriado, segunda lectura remota, umbral bajo activación |

Ref: AHA/ACC STEMI Guidelines 2023; ESC STEMI/NSTEMI Guidelines 2023; MINSAL GES IAM.

## 22.3 Sepsis (bundle 1h/3h)

Protocolo de detección precoz y manejo protocolizado de sepsis y shock séptico. Bundle hora-1 como estándar de atención. Cada hora de retraso en antibióticos aumenta mortalidad en 4-7 %.

**Hitos tiempo-dependientes:**

| Hito | Meta | Benchmark | Responsable |
|------|------|-----------|-------------|
| Lactato sérico | ≤1h desde sospecha | SSC 2021 | Laboratorio/enfermería |
| Hemocultivos (≥2 sets) | Antes de antibiótico | SSC 2021 | Enfermería SUH |
| Antibiótico empírico | ≤1h desde sospecha de sepsis | SSC 2021: ≤1h | Médico SUH |
| Fluidos cristaloides (30 ml/kg) | ≤3h si hipotensión o lactato ≥4 | SSC 2021 | Médico/enfermería SUH |
| Re-evaluación lactato | ≤6h si lactato inicial elevado | SSC 2021 | Médico SUH |
| Vasopresores si PAM <65 post-fluidos | Inicio durante o post-reanimación con fluidos | SSC 2021 | Médico SUH/UCI |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Screening sepsis | qSOFA, NEWS, SIRS modificado — tamizaje en triaje y re-evaluación |
| Bundle hora-1 SSC | Lactato + hemocultivos + antibiótico + fluidos (si indicados) + vasopresores (si indicados) |
| Kit sepsis | Antibióticos empíricos pre-seleccionados, fluidos, sets hemocultivo, POC lactato |
| Alerta electrónica | Gatillo automático en EDIS/HCE al cumplir criterios sepsis (NEWS ≥5, qSOFA ≥2) |
| Escalamiento a UCI | Criterios: vasopresores, ventilación mecánica, falla multiorgánica |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cumplimiento bundle hora-1 | Pacientes con bundle hora-1 completo / Total sepsis × 100 | ≥80 % | SSC: meta global | SSC 2021 | Mensual |
| Antibiótico ≤1h | Sepsis con antibiótico ≤1h / Total sepsis × 100 | ≥90 % | SSC 2021 | SSC 2021 | Mensual |
| Mortalidad sepsis intrahospitalaria | Fallecidos sepsis / Total sepsis × 100 | ≤20 % | SSC registros: 15-25 % | SSC 2021 | Trimestral |
| Lactato POC ≤1h | Lactato obtenido ≤1h / Total sepsis × 100 | ≥90 % | — | EDIS/LIS | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Sepsis no reconocida en adulto mayor (presentación atípica) | Tamizaje NEWS en todos ≥65 años, umbral bajo sospecha |
| Resistencia antibiótica por empírico inadecuado | Antibiograma local actualizado, de-escalación a 48-72h |

Ref: Surviving Sepsis Campaign Guidelines 2021; SSC Bundle Update 2018; MINSAL GES Sepsis.

## 22.4 Trauma mayor (ATLS)

Protocolo de activación y manejo del paciente politraumatizado. Abordaje ATLS estandarizado con activación de equipo trauma. Triada letal: hipotermia, acidosis, coagulopatía.

**Hitos tiempo-dependientes:**

| Hito | Meta | Benchmark | Responsable |
|------|------|-----------|-------------|
| Activación equipo trauma | ≤5 min desde pre-notificación | ACS-COT 2022 | Enfermería triaje/líder trauma |
| Evaluación primaria (ABCDE) | ≤10 min desde ingreso | ATLS 10th ed. | Líder trauma |
| FAST/eFAST | ≤10 min desde ingreso | ATLS 10th ed. | Emergenciólogo/cirujano |
| TC body (pan-scan) | ≤30 min si estable hemodinámicamente | NICE Trauma 2023 | Radiólogo |
| Pabellón (cirugía de control de daños) | ≤60 min si inestable post-reanimación | ACS-COT 2022 | Cirujano de trauma |
| Transfusión masiva | Activación ≤15 min si criterios cumplidos | ACS-COT 2022 | Banco de sangre + equipo trauma |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Equipo trauma | Cirujano, emergenciólogo, anestesista, enfermería, paramédico — roles preestablecidos |
| Protocolo transfusión masiva | 1:1:1 (GR:PFC:plaquetas), ácido tranexámico ≤3h, fibrinógeno |
| Cirugía control de daños | Hemostasia, descontaminación, cierre temporal — UCI para estabilización |
| Prevención triada letal | Calentamiento activo, reanimación hemostática, monitoreo TEG/ROTEM |
| Nivel activación trauma | Nivel 1 (equipo completo) vs. nivel 2 (parcial) según mecanismo y criterios clínicos |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Mortalidad trauma severo (ISS ≥16) | Fallecidos / Total trauma ISS ≥16 × 100 | ≤20 % | TARN UK: 15-20 % | TARN 2023 | Trimestral |
| Tiempo a pabellón (inestable) | Mediana minutos ingreso → inicio cirugía (inestable) | ≤60 min | ACS-COT 2022 | Registros quirúrgicos | Trimestral |
| Tasa sobre-activación trauma | Activaciones nivel 1 sin criterio / Total activaciones nivel 1 × 100 | ≤30 % | ACS-COT: ≤30 % | ACS-COT 2022 | Trimestral |
| Adherencia ATLS | Evaluación primaria documentada completa / Total trauma × 100 | ≥95 % | — | Auditoría clínica | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Demora pabellón por disponibilidad | Pabellón trauma dedicado 24/7 o prioridad absoluta |
| Coagulopatía no detectada precozmente | TEG/ROTEM en reanimación, protocolo transfusión masiva protocolizado |

Ref: ATLS 10th ed. (ACS); ACS-COT Resources for Optimal Care 2022; NICE Major Trauma NG39; CRASH-2 Trial (ácido tranexámico).

## 22.5 Paro cardiorrespiratorio y post-ROSC

Protocolo de reanimación cardiopulmonar avanzada y manejo post-retorno de circulación espontánea (ROSC). Cadena de supervivencia intra y extrahospitalaria.

**Hitos tiempo-dependientes:**

| Hito | Meta | Benchmark | Responsable |
|------|------|-----------|-------------|
| Inicio RCP | ≤1 min (intrahospitalario), inmediato (prehospitalario) | ILCOR 2023 | Primer respondedor |
| Desfibrilación (ritmo desfibrilable) | ≤3 min desde detección | AHA 2023: ≤3 min | Equipo RCP/DEA |
| Adrenalina (ritmo no desfibrilable) | ≤3 min desde inicio RCP | AHA 2023 | Enfermería/médico |
| Adrenalina (ritmo desfibrilable) | Después de 2° descarga | AHA 2023 | Enfermería/médico |
| Manejo avanzado vía aérea | Cuando indicado, sin interrumpir compresiones | ILCOR 2023 | Médico/enfermería |
| Temperatura objetivo (TTM) post-ROSC | 32-36 °C por ≥24h, inicio ≤6h | ILCOR 2023 | UCI |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Cadena supervivencia | Reconocimiento → Activación → RCP precoz → Desfibrilación → Soporte avanzado → Post-paro |
| ACLS algorithms | FV/TV sin pulso → Descarga + RCP. AESP/Asistolia → RCP + causas reversibles (5H/5T) |
| Carro de paro | Estandarizado, verificación diaria, ubicación señalizada |
| Debriefing post-paro | Revisión estructurada ≤24h post-evento: calidad RCP, tiempos, resultados |
| Neuropronóstico | ≥72h post-ROSC, multimodal (clínico + EEG + biomarcadores + imagen) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Sobrevida a alta paro intrahospitalario | Sobrevivientes / Total paro intrahospitalario × 100 | ≥25 % | GWTG-R: 25-30 % | AHA GWTG 2023 | Trimestral |
| ROSC sostenido | ROSC >20 min / Total RCP × 100 | ≥50 % | — | Registros paro | Trimestral |
| Fracción compresiones torácicas | Tiempo con compresiones / Tiempo total RCP × 100 | ≥80 % | AHA: ≥80 % | Desfibrilador (data download) | Por evento |
| Debriefing post-paro | Debriefings realizados / Total paros × 100 | ≥90 % | — | Registros calidad | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| RCP de mala calidad (interrupciones, profundidad insuficiente) | Feedback en tiempo real del desfibrilador, simulación trimestral |
| TTM no iniciado por falta de protocolo | Kit TTM disponible, protocolo escrito, capacitación UCI |

Ref: AHA/ILCOR Guidelines CPR and ECC 2023; ERC Guidelines 2021; TTM2 Trial 2021; MINSAL NT RCP.
