---
urn: urn:salud:kb:gestion-redes-general
nombre: gestion-redes-general
version: 2.0.0
estado: publicado
descripcion: "Gestión de Redes Asistenciales — Marco General: Estructura organizacional que articula establecimientos de distintos niveles de complejidad para garantizar continuidad asistencial longitudinal, relacional e informacional"
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/salud/salubrista/gestion-redes/01-gestion-redes-general.md (sha256:a94a6137630ba03ecd4874d89467d67984d48d4c13be76d9b3fb695a5d3e7704) el 2026-06-12; cuerpo byte-fiel (renombrado de 01-gestion-redes-general.md a gestion-redes-general.md por lugar-coincide). Fuente original: Síntesis multi-fuente: OPS, IHI, NICE, AHRQ, MINSAL, Cochrane"
autor: FS
creado: 2026-03-03
lang: es
tags: [gestion-redes, gobernanza, calidad, procesos, digital, finanzas, cambio, red-asistencial]
familia: bok
---

# Gestión de Redes Asistenciales — Marco General


## 1.1 Red integrada, continuidad, niveles de atención

Estructura organizacional que articula establecimientos de distintos niveles de complejidad para garantizar continuidad asistencial longitudinal, relacional e informacional.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| APS | Puerta de entrada, resolutividad ≥85 %, adscripción territorial |
| Nivel secundario | Especialidades ambulatorias, CDT/CRS, hospital de día |
| Nivel terciario | Alta complejidad, UCI/UTI, cirugía mayor, trasplantes |
| Continuidad informacional | HCE compartida, resumen de alta estandarizado (HL7 CDA) |
| Continuidad relacional | Médico de cabecera, equipo de sector, panel asignado |
| Continuidad gestional | Protocolos de derivación-contrarreferencia bidireccional |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Resolutividad APS | Consultas resueltas APS / Total consultas × 100 | ≥85 % | OCDE 85-90 % | OCDE 2023 | Trimestral |
| Tasa de referencia | Derivaciones / Consultas APS × 100 | ≤15 % | UK NHS 5-10 % | NHS England 2022 | Mensual |
| Continuidad relacional (UPC) | Consultas con mismo médico / Total consultas | ≥0.75 | — | Jee & Cabana 2006 | Semestral |
| Contrarreferencia efectiva | Contrarreferencias recibidas / Derivaciones enviadas × 100 | ≥80 % | — | MINSAL 2019 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Fragmentación de la red | Gobernanza compartida, convenios interinstitucionales |
| Pérdida de seguimiento post-derivación | Trazabilidad electrónica, navigator de pacientes |
| Sobreuso nivel terciario | Fortalecimiento resolutividad APS, telemedicina |

Ref: Ley 19.937 (Autoridad Sanitaria); OPS/OMS RISS 2010; Starfield 1998; WHO Framework on Integrated People-Centred Health Services 2016.

## 1.2 Cuádruple Meta

Marco estratégico que alinea cuatro objetivos simultáneos: experiencia del paciente, salud poblacional, costo per cápita y bienestar del equipo de salud.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Experiencia del paciente | PREMs, NPS, tiempos de espera percibidos |
| Salud poblacional | AVPP, AVISA, prevalencia condiciones crónicas |
| Costo per cápita | Gasto total / población adscrita, ajustado por riesgo |
| Bienestar del equipo | Burnout (MBI), satisfacción laboral, rotación |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| NPS pacientes | % Promotores − % Detractores | ≥50 | Top quartile ≥62 | Press Ganey 2023 | Trimestral |
| AVPP | Años de vida potencial perdidos / 100.000 hab | Reducción ≥2 %/año | OCDE promedio 3.400 | OCDE 2023 | Anual |
| Costo per cápita ajustado | Gasto total / Población ajustada por ACG | Crecimiento ≤IPC+1 % | — | IHI 2019 | Anual |
| Burnout equipo (MBI) | % personal con agotamiento emocional alto | ≤25 % | EE.UU. 44 % (2022) | Shanafelt 2022 | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Optimizar una meta a expensas de otra | Tablero balanceado con las 4 dimensiones |
| Bienestar como retórica sin acción | Indicadores de bienestar en evaluación directiva |

Ref: IHI Triple Aim 2008; Bodenheimer & Sinsky 2014 (Quadruple Aim); OCDE Health at a Glance 2023.

## 1.3 Topología de red

Configuración estructural de nodos asistenciales y sus conexiones según modelo geográfico-funcional.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Hub & spoke | Hospital base (hub) + establecimientos satélite (spokes) |
| Integración vertical | Articulación entre niveles (APS→secundario→terciario) |
| Integración horizontal | Coordinación entre establecimientos del mismo nivel |
| Regionalización | Asignación territorial de población a nodos específicos |
| Redes temáticas | Redes funcionales por patología (oncología, cardiovascular, trauma) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cobertura geográfica | Población a ≤30 min del nodo más cercano / Población total × 100 | ≥90 % | — | OPS 2020 | Anual |
| Densidad de red | Nodos operativos / 100.000 hab | Según norma país | OCDE 3.0 camas/1.000 hab | OCDE 2023 | Anual |
| Índice de conectividad | Enlaces activos / Enlaces posibles entre nodos | ≥0.6 | — | Análisis de red social | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Duplicación de servicios entre nodos | Cartera de servicios diferenciada por nivel |
| Brechas de acceso rural | Telemedicina, postas rurales, rondas médicas |

Ref: OPS Redes Integradas 2010; Shortell 2000; Provan & Milward 1995 (network effectiveness).

## 1.4 Determinantes sociales, equidad e interculturalidad

Incorporación sistemática de factores socioeconómicos, culturales y territoriales en planificación y operación de la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Determinantes estructurales | Ingreso, educación, empleo, vivienda, ruralidad |
| Determinantes intermediarios | Conductas, exposiciones ambientales, acceso a servicios |
| Equidad en acceso | Ajuste de oferta por vulnerabilidad (FONASA A-B priorizado) |
| Pertinencia cultural | Facilitadores interculturales, protocolos pueblos originarios |
| Enfoque de género | Brechas de acceso y resultados por sexo/género |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Brecha de mortalidad evitable | Tasa AVPP quintil I / Tasa AVPP quintil V | ≤1.5 | UK ≤1.3 | MINSAL-DEIS 2023 | Anual |
| Cobertura controles crónicos en FONASA A | % cobertura vs. % población FONASA A | Razón ≥1.0 | — | MINSAL 2023 | Semestral |
| Satisfacción pueblos originarios | PREMs ajustados por pertinencia cultural | ≥70 % | — | MINSAL Intercultural 2021 | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Universalismo sin focalización | Estratificación por ISAPRE/FONASA tramo + índice vulnerabilidad |
| Tokenismo intercultural | Participación vinculante de comunidades indígenas |

Ref: OMS CDSS 2008; Marmot Review 2010; Ley 20.584 art. 7 (pertinencia cultural); MINSAL Política de Salud Intercultural 2006.

## 1.5 Ética, derechos y experiencia del paciente

Marco normativo-ético que garantiza derechos, consentimiento informado, participación y trato digno en la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Derechos del paciente | Información, consentimiento, segunda opinión, acompañamiento, reclamo |
| Consentimiento informado | Proceso documentado, capacidad, voluntades anticipadas |
| Comité de ética asistencial | Consultas caso a caso, proporcionalidad, futilidad |
| Participación ciudadana | Consejos consultivos, encuestas, codiseño |
| Experiencia del paciente | Journey mapping, PREMs, gestión de reclamos OIRS |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Reclamos OIRS | N° reclamos / 1.000 egresos | ≤5 | — | MINSAL 2023 | Mensual |
| Consentimiento documentado | % procedimientos con CI firmado / Total procedimientos | 100 % | 100 % | Ley 20.584 | Mensual |
| Respuesta reclamos ≤15 días | Reclamos respondidos en plazo / Total reclamos × 100 | ≥90 % | — | Ley 19.880 | Mensual |
| Satisfacción global | PREMs score agregado | ≥80 % | NHS 75 % | NHS Patient Survey 2023 | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Consentimiento como trámite burocrático | Capacitación en comunicación, check de comprensión |
| Subregistro de reclamos | Canal digital + presencial, cultura no punitiva |

Ref: Ley 20.584 (Derechos y Deberes); Ley 20.120 (Investigación en humanos); Beauchamp & Childress 2019; NHS Patient Experience Framework 2023.

## 2.1 Modelo de gobierno de la red

Estructura formal de gobernanza que define órganos, roles y mecanismos de toma de decisiones a nivel de red asistencial.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Consejo directivo de red | Directores de establecimientos, Servicio de Salud, representantes APS |
| Gobernanza clínica | Comités técnicos por línea (médico-quirúrgico, materno-infantil, salud mental) |
| Charter de red | Documento constitutivo: misión, alcance, autoridad, rendición de cuentas |
| Secretaría técnica | Equipo permanente de coordinación, agenda, actas, seguimiento |
| Participación comunitaria | Consejo consultivo de usuarios integrado a gobernanza |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Sesiones consejo directivo | N° sesiones realizadas / N° programadas × 100 | ≥90 % | — | Gestión interna | Trimestral |
| Acuerdos implementados | Acuerdos ejecutados / Acuerdos tomados × 100 | ≥80 % | — | Actas consejo | Semestral |
| Participación activa miembros | Asistencia promedio / Miembros totales × 100 | ≥75 % | — | Gestión interna | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Gobernanza nominal sin poder efectivo | Charter con mandato explícito y presupuesto asignado |
| Captura por un establecimiento dominante | Rotación de presidencia, voto ponderado |

Ref: Ley 19.937 (Servicios de Salud); NHS Clinical Governance Framework 2019; OPS Gobernanza RISS 2010.

## 2.2 Arquitectura decisional

Catálogo explícito de decisiones, niveles de autoridad y procesos de escalamiento en la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Catálogo de decisiones | Inventario tipificado: operativas, tácticas, estratégicas |
| Matriz RACI | Responsable, Aprobador, Consultado, Informado por tipo de decisión |
| Niveles de autoridad | Local (establecimiento), red (comité), Servicio de Salud, MINSAL |
| Delegación formal | Resoluciones exentas con límites definidos (monto, alcance) |
| Trazabilidad | Registro digital de decisiones, fundamentos y resultados |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Decisiones con RACI definido | Decisiones con RACI / Total decisiones catálogo × 100 | 100 % | — | Gestión interna | Semestral |
| Tiempo promedio decisión táctica | Días desde solicitud hasta resolución | ≤5 días | — | Sistema de gestión | Mensual |
| Escalamientos fuera de protocolo | N° escalamientos no protocolizados / Total escalamientos × 100 | ≤10 % | — | Registro escalamientos | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Parálisis por exceso de niveles | Simplificar a máximo 3 niveles de aprobación |
| Decisiones sin registro | Sistema digital obligatorio con firma electrónica |

Ref: MINSAL Orientaciones Gestión en Red 2018; ISO 9001:2015 §5.3 (roles y autoridades); RACI framework PMI 2021.

## 2.3 Coordinación interinstitucional

Mecanismos formales de articulación entre instituciones de la red (públicas, privadas, intersectoriales).

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Convenios marco | Acuerdos institucionales con alcance, plazos, financiamiento |
| Convenios docente-asistenciales | Campos clínicos, supervisión, acreditación ASOFAMECH |
| eReferral | Derivación electrónica estandarizada con tracking bidireccional |
| Mesas intersectoriales | Educación, vivienda, desarrollo social (Chile Crece Contigo, SENDA) |
| Compra de servicios | Licitaciones y convenios con prestadores privados (PPV, CAEC) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Convenios vigentes | N° convenios activos / N° convenios requeridos × 100 | ≥90 % | — | Subdirección gestión | Semestral |
| Derivaciones electrónicas | Derivaciones vía eReferral / Total derivaciones × 100 | ≥80 % | NZ 95 % | NZ Health 2022 | Trimestral |
| Cumplimiento SLA convenios | Prestaciones en plazo / Prestaciones comprometidas × 100 | ≥85 % | — | Gestión convenios | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Convenios sin monitoreo | Tablero de seguimiento con alertas automáticas |
| Dependencia excesiva sector privado | Plan de contingencia con capacidad pública de respaldo |

Ref: Ley 19.937 art. 26 (convenios); Ley 19.886 (compras públicas); NHS e-Referral Service 2021; NZ Integrated Care Framework 2022.

## 2.4 Contratos de gestión y SLA

Instrumentos formales que definen compromisos, metas, indicadores y consecuencias entre niveles de la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Compromisos de gestión | Metas anuales Servicio de Salud–MINSAL (Ley 19.937) |
| Convenios de desempeño | Acuerdos director de establecimiento–Servicio de Salud |
| SLA internos | Acuerdos de servicio entre unidades (laboratorio, imagenología, farmacia) |
| Incentivos | Asignación de desempeño colectivo (Ley 19.813), COMGES |
| Penalidades | Planes de mejora obligatorios ante incumplimiento >2 trimestres |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cumplimiento COMGES | Metas cumplidas / Metas comprometidas × 100 | ≥90 % | — | MINSAL-COMGES | Trimestral |
| SLA laboratorio (TAT) | Muestras informadas en plazo / Total muestras × 100 | ≥95 % | CAP ≥90 % | CAP 2023 | Mensual |
| SLA imagenología | Informes entregados ≤24h / Total informes × 100 | ≥90 % | ACR ≥85 % | ACR 2022 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Gaming de indicadores | Auditoría cruzada, indicadores de resultado (no solo proceso) |
| SLA desactualizados | Revisión anual con benchmark externo |

Ref: Ley 19.937 art. 25 (compromisos de gestión); Ley 19.813 (asignación desempeño); MINSAL COMGES 2024; CAP Laboratory Accreditation 2023.

## 2.5 Gestión de conflictos y escalamiento

Protocolos para resolver disputas entre actores de la red, con niveles progresivos de intervención.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Nivel 1 — Negociación directa | Entre jefaturas involucradas, plazo 5 días |
| Nivel 2 — Mediación | Secretaría técnica de red como facilitador, plazo 10 días |
| Nivel 3 — Arbitraje | Consejo directivo de red resuelve con carácter vinculante |
| Nivel 4 — Escalamiento institucional | Director Servicio de Salud / Subsecretaría de Redes |
| Registro de conflictos | Base de datos con tipología, resolución y tiempo |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Resolución en Nivel 1 | Conflictos resueltos N1 / Total conflictos × 100 | ≥60 % | — | Registro conflictos | Trimestral |
| Tiempo medio resolución | Días promedio desde detección hasta cierre | ≤15 días | — | Registro conflictos | Trimestral |
| Recurrencia | Conflictos repetidos misma díada / Total conflictos × 100 | ≤10 % | — | Registro conflictos | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Conflictos no reportados | Canal anónimo, cultura de resolución temprana |
| Escalamiento prematuro | Checklist obligatorio de agotamiento de nivel previo |

Ref: MINSAL Orientaciones Gestión en Red 2018; Thomas-Kilmann Conflict Model; NHS Dispute Resolution Framework 2020.
