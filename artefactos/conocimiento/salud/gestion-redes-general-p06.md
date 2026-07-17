---
urn: urn:salud:kb:gestion-redes-general-p06
nombre: gestion-redes-general-p06
version: 2.0.0
estado: publicado
descripcion: "Gestión de Redes Asistenciales — Marco General - Parte 06"
fuente: "Migrado de la bestia (~/kora @ 9de5dc38b78c23574d24a481a5f84d70173c2203) artifacts/knowledge/salud/salubrista/gestion-redes/01-gestion-redes-general--p06.md (sha256:4edaa357b1d3619fda6709fd0262e904c1ef225598daa10f91d5596a3a5388ea) el 2026-07-17; cuerpo byte-fiel; frontmatter normalizado a ley/2; shard enlazado por cita a urn:salud:kb:gestion-redes-general."
autor: FS
creado: 2026-03-03
lang: es
tags: [gestion-redes, gobernanza, calidad, procesos, digital, finanzas, cambio, red-asistencial]
familia: bok
cita: [urn:salud:kb:gestion-redes-general]
---

# Gestión de Redes Asistenciales — Marco General - Parte 06

## 10.5 Cumplimiento y auditorías

Verificación sistemática de adherencia a normas, protocolos y regulaciones aplicables.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Auditoría programada | Calendario anual, alcance definido, equipos auditores internos |
| Auditoría sorpresa | Sin aviso previo, foco en prácticas de rutina (higiene, identificación) |
| Checklist de cumplimiento | Items verificables por área (farmacia, esterilización, urgencia) |
| Plan de acción correctiva | Hallazgo → causa raíz → acción → responsable → plazo → verificación |
| Auditoría externa | SEREMI, Superintendencia, acreditadores |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Auditorías ejecutadas | Realizadas / Programadas × 100 | ≥95 % | — | Calidad | Semestral |
| No conformidades críticas | NC críticas abiertas | 0 | — | Auditoría | Continuo |
| Cierre NC en plazo | NC cerradas en plazo / Total NC × 100 | ≥90 % | — | Calidad | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Auditoría como inspección punitiva | Enfoque formativo, participación del auditado |
| Hallazgos recurrentes sin solución | Escalamiento a dirección tras segunda recurrencia |

Ref: ISO 19011:2018 (Auditoría de sistemas de gestión); SIC Estándares Acreditación 2023; MINSAL Fiscalización SEREMI.

## 10.6 Análisis de riesgos y BIA

Identificación, evaluación y priorización de riesgos operacionales y su impacto en la continuidad.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Registro de riesgos | Inventario con probabilidad, impacto, score, owner, mitigación |
| Matriz de riesgos | 5×5 (probabilidad × impacto), clasificación por cuadrante |
| BIA (Business Impact Analysis) | Procesos críticos, RTO, RPO, dependencias, recursos mínimos |
| Apetito de riesgo | Declaración formal del consejo directivo |
| Monitoreo continuo | Dashboard de riesgos top-10, revisión trimestral |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Riesgos evaluados | Riesgos con score actualizado / Total riesgos registrados × 100 | 100 % | — | Registro riesgos | Trimestral |
| BIA actualizado | Procesos con BIA ≤12 meses / Total procesos críticos × 100 | 100 % | ISO 22301 | ISO 22301:2019 | Anual |
| Mitigaciones implementadas | Controles implementados / Controles planificados × 100 | ≥85 % | — | Registro riesgos | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Registro estático sin actualización | Trigger de revisión: incidente, cambio organizacional, auditoría |
| BIA teórico sin validación | Ejercicio tabletop anual por proceso crítico |

Ref: ISO 31000:2018 (Gestión de riesgos); ISO 22301:2019 (Continuidad de negocio); ASIS Business Impact Analysis 2019; NHS Risk Management Standards 2023.

## 10.7 Plan de Continuidad (BCP/COOP) y DRP TI

Planes para mantener servicios esenciales durante interrupciones y recuperar sistemas de información.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| BCP/COOP | Plan de continuidad operacional: servicios esenciales, dotación mínima, suministros |
| DRP TI | Disaster Recovery Plan: backup, replicación, sitio alterno, RTO/RPO |
| Servicios esenciales | Urgencia, UCI, pabellón urgencia, farmacia, laboratorio, imagenología |
| Cadena de mando | Sucesión de autoridad ante ausencia de directivos |
| Comunicación de crisis | Protocolo: portavoz único, canales, mensajes clave, frecuencia |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| BCP actualizado | Planes vigentes / Total planes requeridos × 100 | 100 % | ISO 22301 | ISO 22301:2019 | Anual |
| RTO cumplido en ejercicio | Servicios recuperados dentro de RTO / Total servicios × 100 | ≥90 % | — | Ejercicio DRP | Anual |
| Backup verificado | Backups restaurados exitosamente / Total backups × 100 | 100 % | — | TI | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Plan no probado | Ejercicio anual obligatorio (tabletop + funcional) |
| DRP sin sitio alterno | Contrato con proveedor cloud/colocation |

Ref: ISO 22301:2019; NIST SP 800-34 (Contingency Planning); MINSAL Plan de Emergencia Hospitalario; HIMSS DRP Guidelines 2022.

## 10.8 Sistema de Comando de Incidentes (HICS/ICS)

Estructura organizacional estandarizada para gestión de emergencias y desastres en establecimientos de salud.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Comando del incidente | Jefe de incidente (IC), oficial de seguridad, enlace, información pública |
| Sección operaciones | Atención médica, triage, tratamiento, evacuación |
| Sección planificación | Situación, recursos, documentación, desmobilización |
| Sección logística | Suministros, comunicaciones, alimentación, transporte |
| Sección finanzas/admin | Costos, contratos, compensación, registro de tiempo |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Personal capacitado HICS | Personal con curso HICS / Personal clave × 100 | ≥80 % | — | Emergencia | Anual |
| Tiempo activación HICS | Minutos desde declaración hasta equipo operativo | ≤15 min | — | Ejercicios | Por ejercicio |
| Ejercicios HICS realizados | Ejercicios ejecutados / Programados × 100 | ≥90 % | — | Plan emergencia | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Estructura paralela desconocida por personal | Capacitación recurrente, señalética, chalecos de rol |
| HICS activado tardíamente | Criterios de activación explícitos, autoridad delegada |

Ref: HICS (Hospital Incident Command System) 2014; FEMA NIMS 2017; MINSAL Plan Nacional de Emergencias en Salud 2018.

## 10.9 Desastres, CBRNE y eventos masivos

Preparación y respuesta ante desastres naturales, agentes CBRNE y eventos con víctimas masivas.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Amenazas naturales | Terremoto, tsunami, erupción volcánica, aluvión, incendio forestal |
| CBRNE | Químico, Biológico, Radiológico, Nuclear, Explosivo |
| MCI (Mass Casualty Incident) | Evento con víctimas que superan capacidad instalada |
| Triage de desastre | START/JumpSTART, etiquetas de color (rojo/amarillo/verde/negro) |
| Surge capacity | Expansión de capacidad: espacios, personal, insumos, equipos |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Capacidad de surge | Camas expandibles / Camas base × 100 | ≥20 % | — | Plan emergencia | Anual |
| Kit CBRNE disponible | Kits completos / Kits requeridos × 100 | 100 % | — | Emergencia | Semestral |
| Personal capacitado triage desastre | Personal urgencia con curso / Total personal urgencia × 100 | ≥90 % | — | Emergencia | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Stock de emergencia vencido | Rotación FIFO, inventario trimestral |
| Comunicaciones caídas | Redundancia: radio, satélite, mensajería offline |

Ref: ONEMI/SENAPRED Chile; OPS/OMS Hospital Seguro; FEMA NIMS 2017; START Triage System; MINSAL Plan CBRNE 2019.

## 10.10 Ejercicios y simulacros

Programa estructurado de ejercicios para validar planes y mantener preparación operativa.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Tabletop | Ejercicio teórico de discusión, bajo costo, alta participación |
| Funcional | Activación parcial de plan, prueba de comunicaciones y logística |
| Full-scale | Simulacro completo con víctimas simuladas, multiagencia |
| After Action Review (AAR) | Análisis post-ejercicio: qué funcionó, brechas, acciones correctivas |
| Calendario de ejercicios | Mínimo: 1 tabletop trimestral, 1 funcional semestral, 1 full-scale anual |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Ejercicios ejecutados | Ejercicios realizados / Programados × 100 | ≥90 % | — | Plan emergencia | Anual |
| Brechas identificadas | N° brechas por ejercicio | Documentar todas | — | AAR | Por ejercicio |
| Brechas corregidas | Brechas corregidas / Brechas identificadas en AAR previo × 100 | ≥80 % | — | Seguimiento AAR | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Ejercicios rutinarios sin aprendizaje | Escenarios variados, inyectos sorpresa |
| AAR sin seguimiento | Integrar hallazgos en plan de mejora con seguimiento formal |

Ref: HSEEP (Homeland Security Exercise and Evaluation Program) 2020; OPS Hospital Seguro; MINSAL Plan de Emergencia; US Army AAR Framework.

## 11.1 HIS/EHR y módulos de red

Ecosistema de sistemas de información en salud que soporta la operación de la red asistencial.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| HCE (EHR) | Historia clínica electrónica compartida, acceso multi-establecimiento |
| EMPI | Enterprise Master Patient Index: identificación única de pacientes |
| LIS | Laboratory Information System: órdenes, resultados, trazabilidad |
| RIS/PACS | Radiology IS + Picture Archiving: órdenes, imágenes, informes |
| Módulos de red | Referencia/contrarreferencia, gestión de camas, GES, lista de espera |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cobertura HCE | Establecimientos con HCE operativa / Total establecimientos × 100 | 100 % | — | TI red | Semestral |
| Duplicados EMPI | Registros duplicados / Total registros × 100 | ≤2 % | HIMSS ≤1 % | HIMSS 2023 | Trimestral |
| Disponibilidad sistemas críticos | Uptime sistemas core / Tiempo total × 100 | ≥99.5 % | — | TI | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Sistemas heterogéneos no integrados | Bus de integración (ESB/iPaaS), estándares abiertos |
| Caída de HCE sin contingencia | Procedimiento manual documentado, DRP TI |

Ref: HIMSS EMRAM 2023; HL7 International; MINSAL Estrategia Digital en Salud 2023; OMS Digital Health 2020.

## 11.2 Interoperabilidad

Capacidad de sistemas de información para intercambiar datos con significado preservado.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| HL7 FHIR R4 | Estándar de interoperabilidad basado en APIs RESTful |
| HL7 v2/CDA | Mensajería y documentos clínicos (legado, transición) |
| SNOMED CT | Terminología clínica: diagnósticos, procedimientos, hallazgos |
| LOINC | Nomenclatura universal de laboratorio y observaciones clínicas |
| CIE-10/CIE-11 | Clasificación estadística de enfermedades |
| Niveles de interoperabilidad | Técnica → sintáctica → semántica → organizacional |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| APIs FHIR publicadas | APIs operativas / APIs requeridas × 100 | ≥50 % | — | TI red | Semestral |
| Codificación SNOMED | Registros con código SNOMED / Total registros clínicos × 100 | ≥60 % | — | HCE | Trimestral |
| Mensajes HL7 exitosos | Mensajes procesados OK / Total mensajes × 100 | ≥99 % | — | Bus integración | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Mapeo terminológico incorrecto | Validación por comité clínico, mapas de referencia SNOMED |
| Vendor lock-in | Cláusulas de interoperabilidad en contratos, APIs abiertas |

Ref: HL7 FHIR R4; SNOMED International 2023; LOINC (Regenstrief); MINSAL Estándar de Interoperabilidad 2023; OMS Digital Health 2020.

## 11.3 Telemedicina y atención virtual

Prestación de servicios clínicos a distancia mediante tecnologías de información y comunicación.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Teleconsulta sincrónica | Videoconsulta médico-paciente en tiempo real |
| Teleconsultoría | Médico APS–especialista, asincrónica (store & forward) o sincrónica |
| Telemonitoreo | Dispositivos remotos (presión, glicemia, saturación) con alertas |
| Tele-urgencia | Soporte especialista a distancia para urgencias remotas |
| Regulación | Ley 21.541 (Telemedicina Chile), consentimiento específico |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Teleconsultas / Total consultas | Teleconsultas / (Teleconsultas + Presenciales) × 100 | ≥20 % | — | Agendamiento | Trimestral |
| Satisfacción teleconsulta | PREMs teleconsulta | ≥80 % | — | Encuesta | Trimestral |
| Resolución teleconsultoría | IC resueltas por teleconsultoría / Total teleconsultorías × 100 | ≥60 % | — | eReferral | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Brecha digital en pacientes vulnerables | Puntos de telemedicina asistida en APS, capacitación digital |
| Calidad técnica insuficiente | Estándares mínimos de conectividad y equipamiento |

Ref: Ley 21.541 (Telemedicina Chile); OMS Telemedicine Guidelines 2022; ATA Practice Guidelines 2023; MINSAL Orientaciones Telemedicina 2023.

## 11.4 Analítica e IA clínica/operativa

Aplicación de ciencia de datos e inteligencia artificial para mejorar decisiones clínicas y operativas.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Analítica descriptiva | Dashboards, reportería automatizada, data warehouse |
| Analítica predictiva | Modelos de riesgo (readmisión, deterioro, no-show, demanda) |
| Analítica prescriptiva | Optimización de agendas, asignación de recursos |
| IA clínica | Soporte diagnóstico (imagenología, patología), alertas tempranas (NEWS) |
| Model cards | Documentación estandarizada: performance, sesgos, limitaciones, validación |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Modelos en producción | Modelos desplegados / Modelos desarrollados × 100 | ≥30 % | — | Data science | Semestral |
| Alertas accionadas | Alertas que generaron acción clínica / Total alertas × 100 | ≥50 % | — | HCE | Trimestral |
| Sesgo validado | Modelos con análisis de equidad documentado / Total modelos × 100 | 100 % | — | Model cards | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Sesgo algorítmico reproduce inequidad | Análisis de equidad por subgrupo, auditoría periódica |
| Sobre-confianza en predicciones | IA como apoyo, decisión final siempre humana |

Ref: WHO Ethics and Governance of AI for Health 2021; FDA AI/ML Action Plan 2023; NICE Evidence Standards for Digital Health Technologies 2022; MINSAL Estrategia Digital 2023.
