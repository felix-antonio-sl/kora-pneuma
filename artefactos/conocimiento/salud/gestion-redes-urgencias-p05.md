---
urn: urn:salud:kb:gestion-redes-urgencias-p05
nombre: gestion-redes-urgencias-p05
version: 2.0.0
estado: publicado
descripcion: "Gestión de Redes Asistenciales — Red de Urgencias - Parte 05"
fuente: "Migrado de la bestia (~/kora @ 9de5dc38b78c23574d24a481a5f84d70173c2203) artifacts/knowledge/salud/salubrista/gestion-redes/03-urgencias--p05.md (sha256:b1b22d0e38e50c8872010a6f0dbd16bcfafd84009e4fe3226df4e253e66b3845) el 2026-07-17; cuerpo byte-fiel; frontmatter normalizado a ley/2; shard enlazado por cita a urn:salud:kb:gestion-redes-urgencias."
autor: FS
creado: 2026-03-03
lang: es
tags: [gestion-redes, urgencias, emergencias, EMS, SUH, protocolos, triaje, desastres, MCI]
familia: bok
cita: [urn:salud:kb:gestion-redes-urgencias]
---

# Gestión de Redes Asistenciales — Red de Urgencias - Parte 05

## 24.1 EDIS y triaje electrónico

Sistema de información específico del SUH (Emergency Department Information System) que gestiona flujo de pacientes, triaje, órdenes, resultados y métricas en tiempo real.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| EDIS core | Registro ingreso, triaje, tracking paciente, órdenes, resultados, alta — timeline completo |
| Triaje electrónico | Soporte decisional algorítmico (ESI/MTS), timestamps automáticos, discriminadores |
| Integración HCE | Bidireccional: EDIS → HCE (episodio urgencia) y HCE → EDIS (antecedentes, alergias, medicación) |
| Tablero tiempo real | Visualización de todos los pacientes por estado, tiempo en SUH, pendientes, alertas |
| Alertas clínicas | Gatillos automáticos: sepsis (NEWS ≥5), deterioro (MEWS), tiempo excedido por triaje |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Adopción EDIS | % consultas registradas en EDIS / Total consultas SUH × 100 | 100 % | — | EDIS | Mensual |
| Disponibilidad EDIS | Uptime EDIS / Horas totales × 100 | ≥99.5 % | — | TI | Mensual |
| Timestamp automático triaje | % triajes con timestamp automático / Total triajes × 100 | ≥98 % | — | EDIS | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Caída EDIS (single point of failure) | Contingencia con formulario papel + ingreso retrospectivo, infraestructura redundante |
| Alert fatigue | Priorización de alertas, revisión periódica de umbrales, supresión de alertas de bajo valor |

Ref: ACEP Health IT Policy; HIMSS EDIS Selection Guide; NT HCE MINSAL.

## 24.2 RTLS y dashboards RT

Sistemas de localización en tiempo real (Real-Time Location Systems) y dashboards para gestión visual del flujo SUH.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| RTLS pacientes | Tags en pulsera identificatoria, tracking por zona (sala espera, box, imagenología, UOCS) |
| RTLS equipos | Localización de equipos compartidos (ecógrafo, bombas infusión, monitores portátiles) |
| Dashboard flujo | Mapa visual SUH en tiempo real: ocupación por zona, tiempos acumulados, alertas |
| Dashboard surge | Semáforo automático verde/amarillo/rojo/negro basado en métricas de flujo |
| Reporting automatizado | Generación automática de indicadores mensuales desde datos RTLS + EDIS |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Precisión RTLS | Localización correcta / Total lecturas × 100 | ≥95 % | — | RTLS | Mensual |
| Uso dashboard por jefatura | Accesos dashboard / Turnos × 100 | ≥90 % | — | Log sistema | Mensual |
| Reducción búsqueda equipos | Tiempo promedio localización equipo post-RTLS vs. pre-RTLS | Reducción ≥50 % | — | Estudio pre-post | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Costo implementación alto | ROI documentado: reducción tiempos búsqueda, mejora flujo, reducción LWBS |
| Resistencia del personal (percepción de vigilancia) | Comunicación transparente: foco en flujo y seguridad, no control individual |

Ref: RTLS in Healthcare (HIMSS); IHI Flow Improvement; ACEP Technology Policy.

## 24.3 Tele-urgencias (apoyo remoto SAR/APS)

Soporte remoto especializado a SAPU/SAR y puntos de urgencia rurales mediante teleconsulta sincrónica con emergenciólogo o especialista.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Teleconsulta sincrónica | Videoconsulta SAPU/SAR → emergenciólogo SUH para apoyo decisional |
| Tele-triaje | Evaluación remota para definir necesidad de traslado vs. resolución local |
| Tele-procedimiento | Guía remota para procedimientos (intubación, drenaje, cardioversión) |
| Tele-ECG desde APS | Transmisión ECG 12 derivaciones desde SAPU/SAR a cardiólogo |
| Plataforma integrada | Videoconferencia + compartir pantalla (imagen, laboratorio) + registro en HCE |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Teleconsultas urgencia realizadas | N° teleconsultas / mes | Tendencia creciente | — | Plataforma telemedicina | Mensual |
| Traslados evitados por teleconsulta | Pacientes resueltos localmente post-teleconsulta / Total teleconsultas × 100 | ≥40 % | — | Registros telemedicina | Trimestral |
| Satisfacción equipo remoto | Encuesta satisfacción profesional SAPU/SAR con soporte | ≥80 % | — | Encuesta interna | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Conectividad insuficiente en zona rural | Conexión satelital de respaldo, modo store-and-forward |
| Responsabilidad legal difusa | Protocolo claro de responsabilidades, registro de teleconsulta en HCE |

Ref: NT Telemedicina MINSAL 2022; OMS Telemedicine Guidelines; ACEP Telemedicine Policy 2023.

## 24.4 IA para clasificación/predicción

Aplicaciones de inteligencia artificial en urgencias para apoyo a triaje, predicción de deterioro y optimización de flujo.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| IA triaje | Modelos ML como soporte decisional al enfermero de triaje (no reemplazo) |
| Predicción deterioro | NEWS/MEWS automatizado + modelos predictivos de deterioro a 4-12h |
| Predicción demanda | ML para forecast de afluencia horaria (complementa modelos estadísticos) |
| NLP en triaje | Procesamiento de lenguaje natural para texto libre de triaje → códigos estructurados |
| Interpretación imagen IA | Soporte radiológico IA para fracturas, hemorragia intracraneal, neumotórax |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Sensibilidad IA deterioro | VP / (VP + FN) para predicción deterioro clínico | ≥85 % | — | Validación modelo | Semestral |
| Especificidad IA triaje | VN / (VN + FP) | ≥80 % | — | Validación modelo | Semestral |
| Aceptación clínica | % recomendaciones IA aceptadas por clínico / Total recomendaciones × 100 | ≥70 % | — | Registros EDIS | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Sesgo algorítmico (edad, género, etnia) | Validación con datos locales, auditoría de equidad, dataset representativo |
| Sobreconfianza en IA (automation bias) | IA como soporte, decisión final siempre del clínico, formación en limitaciones |

Ref: FDA AI/ML Medical Devices Framework; WHO Ethics & Governance of AI for Health 2021; ACEP AI Policy 2023.

## 24.5 Seguridad y continuidad TI 24/7

Garantía de disponibilidad y seguridad de sistemas de información críticos para operación continua del SUH.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Redundancia infraestructura | Servidores espejo, UPS, generador respaldo, conectividad dual |
| RTO/RPO SUH | RTO ≤15 min (restauración servicio), RPO ≤5 min (pérdida máxima datos) |
| Soporte TI 24/7 | Guardia TI con respuesta ≤15 min para sistemas críticos SUH |
| Contingencia sin sistema | Formularios papel, protocolos manuales, re-ingreso datos post-restauración |
| Ciberseguridad | Segmentación red SUH, antimalware, parches, auditoría acceso |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Uptime sistemas críticos SUH | Horas operativas / Horas totales × 100 | ≥99.9 % | — | TI | Mensual |
| Incidentes TI críticos SUH | N° incidentes con impacto en atención / mes | 0 | — | Mesa ayuda TI | Mensual |
| Tiempo restauración (RTO real) | Mediana minutos desde falla → restauración | ≤15 min | — | TI | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Ransomware con impacto en SUH | Backup offline, segmentación de red, plan DRP específico SUH |
| Falla eléctrica prolongada | UPS + generador + prueba mensual, protocolo operación manual |

Ref: ISO 27001:2022; ECRI Top 10 Health Technology Hazards; HIPAA Security Rule; NT HCE MINSAL.

## 25.1 HICS para urgencias

Hospital Incident Command System adaptado al SUH. Define roles, cadena de mando y activación escalonada ante incidentes con múltiples víctimas o desastres.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Comandante de incidente (IC) | Director de turno o jefe SUH; autoridad máxima durante MCI |
| Oficial de operaciones | Coordina áreas clínicas: triaje, tratamiento (rojo/amarillo/verde), transporte |
| Oficial de logística | Insumos, equipos, alimentación, comunicaciones, refuerzo personal |
| Oficial de planificación | Registro pacientes, seguimiento recursos, proyección |
| Oficial de enlace | Comunicación con bomberos, policía, ONEMI/SENAPRED, medios, familiares |
| Niveles de activación | Nivel I (parcial): ≤10 víctimas; Nivel II (total): 11-50; Nivel III (regional): >50 o CBRNE |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Simulacros MCI realizados | Simulacros ejecutados / Simulacros programados × 100 | ≥2/año | Joint Commission: ≥2/año | Joint Commission 2023 | Anual |
| Tiempo activación HICS | Minutos desde notificación MCI → HICS operativo | ≤15 min | — | Registros ejercicios | Por ejercicio |
| Personal que conoce su rol HICS | % personal SUH con rol asignado y capacitado / Total personal SUH × 100 | ≥90 % | — | RRHH | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Plan desactualizado | Revisión anual + post-ejercicio, incorporación lecciones aprendidas |
| Rotación de personal sin capacitación | Inducción HICS obligatoria para todo personal nuevo SUH |

Ref: HICS 2014 (CHA); Joint Commission Environment of Care Standards; SENAPRED protocolos; DS 58/2008 MINSAL.

## 25.2 Triage START/JumpSTART/CBRNE

Sistemas de triaje masivo para asignación rápida de prioridad en escena con múltiples víctimas. Algoritmos simplificados para primera respuesta.

**Categorías de triaje masivo:**

| Categoría | Color | Criterio START | Acción |
|-----------|-------|---------------|--------|
| Inmediata | ROJO | Respiración presente post-apertura vía aérea, FR >30 o <10, llenado capilar >2s, no obedece órdenes | Tratamiento prioritario, traslado urgente |
| Retardada | AMARILLO | Respiración normal, llenado capilar ≤2s, obedece órdenes, lesiones que requieren atención pero toleran espera | Tratamiento diferido, monitoreo |
| Menor | VERDE | Ambulatorio, lesiones menores, puede caminar | Autotriaje, zona de espera |
| Expectante/Fallecido | NEGRO | No respira post-apertura vía aérea (START), o pronóstico incompatible con sobrevida en contexto MCI | Cuidados paliativos o morgue |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| START | Simple Triage and Rapid Treatment — adultos, algoritmo 30-2-can do (FR, perfusión, estado mental) |
| JumpSTART | Adaptación pediátrica de START — incluye ventilaciones de rescate |
| SALT | Sort-Assess-Lifesaving interventions-Treatment/Transport — alternativa validada |
| CBRNE triage | Triaje específico para Chemical-Biological-Radiological-Nuclear-Explosive: decontaminación antes de clasificación |
| Tarjetas de triaje | Tarjetas físicas codificadas por color, resistentes al agua, con datos mínimos |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Sobre-triaje MCI | Pacientes triaje rojo sin criterio / Total rojo × 100 | ≤50 % | ACS-COT: ≤50 % (aceptable en MCI) | ACS-COT 2022 | Por evento |
| Sub-triaje MCI | Pacientes críticos clasificados amarillo/verde / Total críticos × 100 | ≤5 % | ACS-COT: ≤5 % | ACS-COT 2022 | Por evento |
| Tiempo triaje por víctima | Segundos promedio por víctima en triaje START | ≤30 seg | — | Ejercicio simulación | Por ejercicio |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Personal no entrenado en triaje masivo | Capacitación anual obligatoria, tarjetas con algoritmo impreso |
| Colapso emocional del triador | Rotación de triadores, apoyo psicológico post-evento |

Ref: START Triage (Newport Beach Fire Dept. 1983); JumpSTART (Romig 2002); SALT (CDC 2011); ACS-COT MCI Guidelines.

## 25.3 Zonas caliente/tibia/fría; descontaminación

Delimitación de zonas operativas en incidentes HAZMAT/CBRNE para protección del personal y prevención de contaminación cruzada.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Zona caliente (Hot zone) | Área contaminada, acceso solo personal con EPP nivel A/B, rescate y extracción |
| Zona tibia (Warm zone) | Corredor de descontaminación, EPP nivel B/C, triaje primario post-decon |
| Zona fría (Cold zone) | Área limpia, puesto médico avanzado, triaje secundario, tratamiento, transporte |
| Descontaminación masiva | Estación portátil con duchas, desvestido, retención de efluentes |
| Descontaminación técnica | Individual, detallada, para personal de primera respuesta post-exposición |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo montaje descontaminación | Minutos desde activación → estación operativa | ≤30 min | — | Ejercicio simulación | Por ejercicio |
| Throughput descontaminación | Víctimas descontaminadas / hora | ≥60 / hora (masiva) | — | Ejercicio simulación | Por ejercicio |
| Contaminación secundaria | Casos contaminación secundaria personal / Total personal expuesto × 100 | 0 % | — | Registros incidente | Por evento |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Víctimas llegan directamente a SUH sin descontaminación | Protocolo lock-down SUH, descontaminación en acceso, señalética |
| EPP insuficiente | Stock EPP CBRNE en SUH, revisión trimestral, ejercicio con EPP |

Ref: OSHA HAZWOPER 1910.120; NFPA 473; CHEMPACK (CDC); MINSAL Plan CBRNE.

## 25.4 Comando unificado (EMS/bomberos/policía)

Estructura de comando multi-agencia para coordinación en escena de incidentes complejos. Unifica toma de decisiones entre servicios de emergencia.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Comando unificado (UC) | EMS + bomberos + policía + SENAPRED en un solo puesto de mando |
| Comunicaciones interoperables | Radio multi-frecuencia, canal común designado, lenguaje estandarizado |
| Sectorización de escena | División geográfica: sector rescate, sector triaje, sector transporte, sector morgue |
| Plan de acción del incidente (IAP) | Objetivos, estrategia, recursos, comunicaciones — actualizado cada período operacional |
| Ejercicios conjuntos | Simulacros multi-agencia ≥1/año con evaluación formal |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Ejercicios conjuntos realizados | Ejercicios multi-agencia / año | ≥1 | NIMS: ≥1 | FEMA NIMS 2017 | Anual |
| Tiempo establecimiento UC | Minutos desde arribo primera agencia → UC operativo | ≤20 min | — | Registros ejercicios | Por ejercicio |
| Interoperabilidad radio | % incidentes con canal común operativo / Total incidentes multi-agencia × 100 | 100 % | — | Registros comunicaciones | Por evento |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Conflicto de autoridad entre agencias | Protocolos pre-establecidos de jurisdicción, entrenamiento conjunto |
| Falla comunicaciones en terreno | Radio satelital de respaldo, mensajeros físicos |

Ref: NIMS (FEMA 2017); ICS 100/200/300 (FEMA); SENAPRED protocolos inter-agenciales.
