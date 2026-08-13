---
urn: urn:salud:kb:gestion-redes-urgencias
nombre: gestion-redes-urgencias
version: 2.0.1
estado: publicado
descripcion: "Gestión de Redes Asistenciales — Red de Urgencias: Red escalonada de dispositivos de urgencia articulados por nivel de complejidad, cobertura territorial y capacidad resolutiva"
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/salud/salubrista/gestion-redes/03-urgencias.md (sha256:947c5ef69a2f4768e0f4600de97d8841979c70dcacb4bb8192631aea76cc40e4) el 2026-06-12; cuerpo byte-fiel (renombrado de 03-urgencias.md a gestion-redes-urgencias.md por lugar-coincide). Fuente original: Síntesis multi-fuente: OPS, IHI, NICE, AHRQ, MINSAL, AHA, ACC, ESC, Cochrane. v2.0.1 (2026-08-14): enlaza desde esta raíz las continuaciones p02-p06 para que el corpus completo sea descubrible por URN sin depender de nombres de archivo."
autor: FS
creado: 2026-03-03
lang: es
tags: [gestion-redes, urgencias, emergencias, EMS, SUH, protocolos, triaje, desastres, MCI]
familia: bok
cita: [urn:salud:kb:gestion-redes-herramientas, urn:salud:kb:gestion-redes-urgencias-p02, urn:salud:kb:gestion-redes-urgencias-p03, urn:salud:kb:gestion-redes-urgencias-p04, urn:salud:kb:gestion-redes-urgencias-p05, urn:salud:kb:gestion-redes-urgencias-p06]
---


# Gestión de Redes Asistenciales — Red de Urgencias


## 18. Arquitectura de la red de urgencias

### 18.1 Dispositivos (EMS, SAPU/SAR, SUH)

Red escalonada de dispositivos de urgencia articulados por nivel de complejidad, cobertura territorial y capacidad resolutiva. Cada nodo tiene cartera definida y rutas preferentes de derivación.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| SAPU | Urgencia APS baja complejidad, 24/7 zonas urbanas, resolución C4-C5 |
| SAR | Punto urgencia rural, horario extendido, estabilización y derivación |
| SUH baja complejidad | Hospital comunitario, cirugía menor, laboratorio básico, imagenología convencional |
| SUH mediana complejidad | Hospital base, especialidades de guardia, pabellón 24/7, UCI/UTI |
| SUH alta complejidad | Centro de referencia regional, hemodinamia, neurocirugía, centro trauma |
| EMS/SAMU | Sistema prehospitalario: despacho, ambulancias BLS/ALS, helicóptero (según red) |
| Centro Regulador | Coordinación despacho, gestión camas urgencia, derivaciones inter-SUH |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cobertura territorial urgencia | Población a ≤30 min de SUH / Población total × 100 | ≥90 % | OMS ≥80 % | OMS Emergency Care 2019 | Anual |
| Resolutividad SAPU | Consultas resueltas SAPU / Total consultas SAPU × 100 | ≥85 % | — | MINSAL 2023 | Trimestral |
| Tasa derivación SAPU→SUH | Traslados a SUH / Consultas SAPU × 100 | ≤15 % | — | MINSAL 2023 | Mensual |
| Disponibilidad SUH alta complejidad | Horas operativas reales / Horas programadas × 100 | ≥99 % | — | Gestión interna | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Saturación SUH por consultas no urgentes | Fortalecimiento resolutividad SAPU, educación comunitaria, triaje telefónico |
| Brecha cobertura rural | SAR con telemedicina, ambulancias posicionadas en hotspots rurales |
| Fragmentación sin coordinación | Centro Regulador con visibilidad en tiempo real de camas y recursos |

Ref: Ley 19.937; DS 58/2008 (prestaciones de urgencia); OMS Emergency Care Systems Framework 2019; NT Urgencia MINSAL.

### 18.2 Regionalización y derivaciones

Asignación territorial de población a dispositivos de urgencia según complejidad y patología tiempo-dependiente. Rutas preferentes definidas por protocolo, no por proximidad geográfica exclusiva.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Mapa isócrono | Cobertura por tiempo de traslado (15/30/60 min) para cada nivel |
| Cartera diferenciada | Prestaciones por nivel de SUH, actualizadas anualmente |
| Bypass autorizado | Derivación directa a centro de referencia saltando SUH intermedio (IAM, ACV, trauma mayor) |
| Convenios inter-red | Acuerdos entre Servicios de Salud para patologías de baja frecuencia |

**IF/THEN — Destino según condición:**

| Condición | Destino | Base |
|-----------|---------|------|
| IF STEMI o sospecha ACV con déficit focal | THEN SUH con hemodinamia/neurointervención (bypass SUH intermedio) | AHA/ACC 2023; AHA/ASA 2024 |
| IF trauma mayor (ISS ≥16) o politraumatizado | THEN centro trauma nivel I/II (bypass) | ACS-COT 2022 |
| IF quemadura ≥20 % SCT o vía aérea comprometida | THEN centro quemados regional (bypass) | ABA 2023 |
| IF emergencia obstétrica (eclampsia, DPPNI, rotura uterina) | THEN SUH con maternidad de alta complejidad y UCIN | MINSAL GES |
| IF C4-C5 sin criterios de bypass | THEN SAPU/SAR más cercano | NT Urgencia MINSAL |
| IF paciente pediátrico crítico sin SUH pediátrico cercano | THEN estabilización en SUH más cercano + traslado a centro pediátrico | MINSAL 2023 |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cumplimiento ruta preferente | Pacientes derivados según protocolo / Total derivaciones × 100 | ≥90 % | — | Centro Regulador | Mensual |
| Tiempo traslado inter-SUH | Mediana tiempo salida SUH origen → llegada SUH destino | ≤60 min (urbano) | — | EMS registros | Mensual |
| Bypass efectivo STEMI | STEMI con bypass directo a hemodinamia / Total STEMI × 100 | ≥75 % | AHA: ≥80 % | AHA 2023 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Bypass a centro colapsado | Consulta en tiempo real al Centro Regulador antes de despacho |
| Desactualización de cartera | Revisión anual de cartera + auditoría de capacidad resolutiva real |

Ref: ACS Committee on Trauma — Resources for Optimal Care 2022; AHA Mission: Lifeline 2023; NT Urgencia MINSAL.

### 18.3 Centro Regulador y despacho

Unidad operativa 24/7 que coordina despacho EMS, gestión de camas de urgencia y derivaciones inter-SUH mediante comunicación estandarizada y geolocalización.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Central telefónica 131 | Recepción llamadas, clasificación telefónica, despacho |
| Plataforma CAD (Computer-Aided Dispatch) | Geolocalización ambulancias, asignación automática por proximidad y competencia |
| Panel de camas SUH | Visibilidad en tiempo real: ocupación, disponibilidad por tipo (reanimación, observación, box) |
| Protocolos despacho | Algoritmos por categoría de llamada (A-D), priorización |
| Interoperabilidad | Integración con EDIS de SUH, registros EMS, HCE |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo respuesta telefónica | Tiempo ring → contestación p90 | ≤15 seg | NENA: ≤15 seg (90 %) | NENA 2020 | Mensual |
| Tiempo despacho | Tiempo contestación → salida ambulancia p90 | ≤90 seg | NFPA 1710: ≤80 seg | NFPA 2020 | Mensual |
| Precisión clasificación telefónica | Concordancia categoría telefónica vs. categoría real en escena | ≥85 % | — | Auditoría interna | Trimestral |
| Uso geolocalización | % despachos con asignación automática GPS | ≥95 % | — | CAD | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Sobrecarga telefónica en MCI | Protocolos de escalamiento, líneas dedicadas MCI, desborde a SAPU |
| Falla sistema CAD | Respaldo manual con mapas y radio, redundancia TI |
| Descoordinación inter-Servicios de Salud | Convenios operativos, protocolos unificados, radio interoperable |

Ref: NFPA 1710/1720 (tiempos respuesta); NENA 911 Standards; MINSAL Orientaciones Red Urgencia.

## 19.1 Forecast y cobertura geoespacial

Planificación dinámica de cobertura EMS basada en demanda histórica, análisis geoespacial y posicionamiento estratégico de unidades para optimizar tiempos de respuesta.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Posts dinámicos | Ubicación de ambulancias ajustada por hora/día/estacionalidad según hotspots de demanda |
| Análisis hotspots | Mapeo de calor de eventos por geolocalización, concentración temporal |
| Modelo predictivo demanda | Series temporales + variables exógenas (clima, eventos masivos, festivos) |
| Isócronas de cobertura | Polígonos de tiempo-respuesta desde cada post (8/15/30 min) |
| System Status Management (SSM) | Reposicionamiento proactivo según nivel de disponibilidad |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo respuesta urbano p90 | Minutos desde despacho → llegada a escena (percentil 90) | ≤10 min | NFPA 1710: ≤9 min (ALS) | NFPA 2020 | Mensual |
| Tiempo respuesta rural p90 | Minutos desde despacho → llegada a escena (percentil 90) | ≤20 min | NFPA 1720: variable | NFPA 2020 | Mensual |
| Cobertura 8 min | % población cubierta en ≤8 min por unidad ALS | ≥90 % urbano | UK Ambulance: 75 % Cat 1 en 8 min | NHS England 2023 | Trimestral |
| Unit Hour Utilization (UHU) | Tiempo en misión / Tiempo total disponible | 0.25–0.35 | NASEMSO: 0.25–0.40 | NASEMSO 2021 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Modelo predictivo desactualizado | Recalibración trimestral, validación con datos reales |
| Déficit de unidades en picos | Convenios con transporte privado, ambulancias de reserva |

Ref: NFPA 1710/1720; NASEMSO Model EMS Guidelines 2021; Stout 1983 (SSM).

## 19.2 Tipología de ambulancias y dotación

Clasificación de recursos móviles EMS según capacidad resolutiva, equipamiento y competencias del equipo a bordo.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| BLS (Basic Life Support) | Técnicos paramédicos, DEA, inmovilización, O₂, traslado |
| ALS (Advanced Life Support) | Médico/enfermero + paramédico, monitorización, fármacos IV, intubación, cardioversión |
| Ambulancia de rescate | Equipo extricación vehicular, rescate en altura, HAZMAT básico |
| Helicóptero sanitario (HEMS) | Traslado crítico larga distancia, equipo ALS + intervención avanzada |
| Vehículo primera respuesta (VPR) | Respuesta rápida movilidad alta, sin capacidad traslado, estabilización inicial |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Ratio ALS/población | Unidades ALS / 100.000 hab | ≥1.0 | Variable por país | NASEMSO 2021 | Anual |
| Disponibilidad operativa flota | Unidades operativas / Unidades totales × 100 | ≥90 % | — | Gestión EMS | Mensual |
| Certificaciones vigentes tripulación | % personal con ACLS/PHTLS vigente / Total personal EMS | 100 % | — | RRHH EMS | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Ambulancia ALS no disponible en zona rural | Cross-training BLS en procedimientos críticos, telemedicina en ruta |
| Equipamiento vencido o sin mantención | Checklist diario, mantenimiento preventivo programado |

Ref: NASEMSO 2021; NAEMSP Position Statements; DS 58/2008 MINSAL.

## 19.3 Protocolos clínicos prehospitalarios

Protocolos estandarizados de intervención prehospitalaria por patología tiempo-dependiente. Cada protocolo define intervención, meta temporal, criterio activación código y nivel de tripulación requerido.

**Protocolos por condición:**

| Condición | Intervención clave | Meta temporal | Activación código | Tripulación mínima |
|-----------|-------------------|---------------|-------------------|-------------------|
| IAM STEMI | ECG 12 derivaciones, aspirina, heparina, nitroglicerina, activar código IAM | ECG ≤10 min desde contacto | Elevación ST en ECG prehospitalario | ALS |
| ACV (sospecha) | Escala Cincinnati/RACE, glicemia, hora inicio, pre-notificación | Hora inicio síntomas documentada | ≥1 criterio Cincinnati positivo | ALS |
| Trauma mayor | ABCDE, control hemorragia (torniquete), inmovilización, fluidoterapia restrictiva | Tiempo en escena ≤10 min (load & go) | ISS estimado ≥16, mecanismo alto impacto | ALS |
| Sepsis | qSOFA prehospitalario, acceso venoso, fluidos, lactato POC si disponible | Fluidos iniciados en ruta | qSOFA ≥2 | ALS |
| Paro cardiorrespiratorio | RCP alta calidad, DEA/desfibrilación, adrenalina, manejo vía aérea | Desfibrilación ≤3 min desde llegada | Paciente en paro | BLS/ALS |
| Intoxicación aguda | Identificar tóxico, antídoto específico si disponible, descontaminación, monitorización | Antídoto ≤30 min si indicado | Exposición tóxica confirmada/sospechada | ALS |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| ECG prehospitalario en dolor torácico | ECG realizado / Dolor torácico atendido × 100 | ≥95 % | AHA: ≥90 % | AHA 2023 | Mensual |
| Pre-notificación código IAM/ACV | Casos con pre-notificación / Total códigos × 100 | ≥90 % | — | Registros EMS | Mensual |
| Tiempo en escena trauma | Mediana minutos en escena (trauma penetrante/contuso mayor) | ≤10 min | PHTLS: ≤10 min | NAEMT 2020 | Mensual |
| Sobrevida paro extrahospitalario (ROSC) | ROSC al ingreso SUH / Total paros atendidos × 100 | ≥30 % | Cardiac Arrest Registry: 30-35 % | CARES 2023 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Variabilidad en adherencia a protocolos | Auditoría de registros, feedback individual, simulación trimestral |
| ECG de mala calidad | Entrenamiento técnico, transmisión a cardiólogo para validación remota |

Ref: AHA/ACC STEMI Guidelines 2023; AHA/ASA Stroke Guidelines 2024; PHTLS 10th ed.; Surviving Sepsis Campaign 2021; ILCOR 2023.

## 19.4 Telemedicina prehospitalaria

Soporte remoto especializado al equipo EMS en terreno mediante telecomunicaciones en tiempo real. Permite diagnóstico precoz, activación de códigos y orientación de manejo avanzado.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Tele-ECG | Transmisión ECG 12 derivaciones desde ambulancia a cardiólogo, interpretación remota, activación hemodinamia |
| Tele-stroke | Videoconsulta con neurólogo desde escena o ambulancia, escala NIHSS remota, decisión IVT/trombectomía |
| Tele-trauma | Guía remota por cirujano/emergenciólogo para estabilización avanzada en escena |
| Videoconferencia en ruta | Enlace audiovisual ambulancia→SUH para handoff anticipado |
| Consentimiento telemedicina | Registro verbal documentado, excepto urgencia vital (consentimiento presunto) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tele-ECG transmitidos | ECG transmitidos / ECG realizados en ambulancia × 100 | ≥90 % | — | Registros EMS | Mensual |
| Concordancia diagnóstica tele-ECG | Diagnóstico remoto concordante con diagnóstico final / Total × 100 | ≥95 % | — | Auditoría clínica | Trimestral |
| Tiempo interpretación remota | Mediana tiempo envío ECG → informe especialista | ≤5 min | — | Plataforma telemedicina | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Falla conectividad en zona rural | Redundancia satelital, transmisión diferida con store-and-forward |
| Responsabilidad médico-legal en teleconsulta | Protocolos documentados, registro audio/video, consentimiento |

Ref: NT Telemedicina MINSAL 2022; AHA Policy Statement Telemedicine 2021; ESC Position Paper Telecardiology 2022.

## 19.5 Seguridad operativa y del paciente

Protocolos de seguridad para protección del equipo EMS y del paciente durante la atención prehospitalaria.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Checklist pre-turno | Revisión vehículo, equipamiento, fármacos, comunicaciones |
| EPP escalonado | Precauciones estándar → contacto → aerosol según riesgo |
| IPC prehospitalario | Higiene de manos, limpieza ambulancia post-traslado, manejo cortopunzante |
| Seguridad en escena | Evaluación de riesgo ambiental (violencia, HAZMAT, estructura colapsada) antes de ingreso |
| Conducción segura | Velocidad regulada, uso cinturón, paciente asegurado, escolta policial si necesario |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Incidentes ocupacionales EMS | Eventos lesión/exposición / 1.000 misiones | ≤2.0 | — | Prevención de riesgos | Mensual |
| Cumplimiento checklist pre-turno | Checklists completos / Turnos totales × 100 | ≥98 % | — | Supervisión | Mensual |
| Accidentes vehículo EMS | Colisiones / 100.000 km recorridos | ≤1.0 | — | Gestión flota | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Agresión al equipo EMS | Protocolo escena insegura, escolta policial, botón de pánico |
| Exposición a patógenos | EPP disponible en ambulancia, protocolo post-exposición, vacunación completa |

Ref: OSHA EMS Worker Safety Guidelines; NAEMSP Crew Resource Management; MINSAL IPC.

## 19.6 Indicadores EMS

Tablero consolidado de indicadores prehospitalarios. Sistema de medición integral del desempeño EMS alineado con estándares internacionales.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Indicadores de despacho | Tiempo contestación, tiempo despacho, precisión categorización |
| Indicadores de respuesta | Tiempo respuesta, cobertura geográfica, disponibilidad unidades |
| Indicadores de escena | Tiempo en escena, adherencia protocolos, intervenciones realizadas |
| Indicadores de transporte | Tiempo transporte, destino correcto, pre-notificación |
| Indicadores de resultado | ROSC, sobrevida a alta, satisfacción usuario |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo total llamada-hospital | Llamada 131 → llegada SUH (mediana) | ≤45 min urbano | — | Registros EMS | Mensual |
| Tasa LWBS prehospitalario | Pacientes que rechazan traslado / Total atenciones × 100 | ≤10 % | — | Registros EMS | Mensual |
| Mortalidad ajustada prehospitalaria | Fallecidos prehospitalarios / Total atenciones ajustado por gravedad | Benchmark local | Utstein ≤50 % paro | Utstein 2015 | Trimestral |
| Documentación completa | Registros con campos obligatorios completos / Total registros × 100 | ≥95 % | NEMSIS ≥90 % | NEMSIS 2023 | Mensual |

Para tablero completo de indicadores y plantillas de medición, → `urn:salud:kb:gestion-redes-herramientas` Anexo A.

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Subregistro de datos EMS | Registro electrónico obligatorio, validación automática campos |
| Indicadores sin acción correctiva | Revisión mensual con plan de mejora por indicador en rojo |

Ref: NEMSIS Data Dictionary 2023; Utstein Style Guidelines; NASEMSO Model EMS Guidelines 2021.
