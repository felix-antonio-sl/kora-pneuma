---
urn: urn:salud:kb:gestion-redes-herramientas
nombre: gestion-redes-herramientas
version: 2.0.0
estado: publicado
descripcion: "Gestión de Redes Asistenciales — Herramientas y Anexos: Notación: `**[ROL]** Acción → Decisión? {Sí: ruta / No: ruta} → Siguiente`"
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/salud/salubrista/gestion-redes/05-herramientas-anexos.md (sha256:3b543412df41ef06d746319db5023a988b92ac9b303d1b2722776b22e04d985c) el 2026-06-12; cuerpo byte-fiel (renombrado de 05-herramientas-anexos.md a gestion-redes-herramientas.md por lugar-coincide). Fuente original: Síntesis multi-fuente: OPS, IHI, NICE, AHRQ, MINSAL, Cochrane, NotebookLM HaH"
autor: FS
creado: 2026-03-03
lang: es
tags: [gestion-redes, kpi, bpmn, plantillas, fhir, simulacion, madurez, herramientas]
familia: bok
---

# Gestión de Redes Asistenciales — Herramientas y Anexos


## Anexo A: Catálogo de KPI

### A.1 KPI de red general

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Continuidad contrarreferencia ≤7d | Contrarreferencias ≤7 días / Total derivaciones × 100 | ≥80 % | NHS 85 % | MINSAL 2019 | Mensual |
| Productividad ambulatoria | Consultas realizadas / Horas agenda disponible | ≥3.5/h | OCDE 4/h | OCDE 2023 | Mensual |
| No-show ambulatorio | Inasistencias / Citas agendadas × 100 | ≤10 % | 5-8 % IHI | IHI 2022 | Mensual |
| Reingreso 30d no planificado | Reingresos ≤30d / Egresos × 100 | ≤12 % | 8-11 % OCDE | OCDE 2023 | Mensual |
| Costo por caso ajustado (DRG) | Costo total / Egresos ponderados DRG | Tendencia ↓ | Mediana nacional | FONASA-IR-GRD | Trimestral |
| Espera mediana por especialidad | Mediana días desde derivación a primera atención | ≤30d | NHS RTT 18w | NHS England 2023 | Mensual |
| Cobertura efectiva | Población atendida / Población adscrita × 100 | ≥90 % | — | OPS 2020 | Anual |
| Satisfacción usuaria (PREMs) | Puntaje PREMs estandarizado | ≥80/100 | OCDE 82 | PREMs MINSAL | Semestral |
| Derivaciones con contrarreferencia | Contrarreferencias recibidas / Derivaciones enviadas × 100 | ≥80 % | — | MINSAL 2019 | Trimestral |
| Ocupación hospitalaria | Días-cama ocupados / Días-cama disponibles × 100 | 85-90 % | 85 % NICE | NICE 2022 | Diario |
| Promedio estancia (LOS ajustado) | Suma días estada / Egresos (ajuste case-mix) | Según GRD | OCDE 6.5d | OCDE 2023 | Mensual |
| % altas antes 12:00 h | Altas antes mediodía / Total altas × 100 | ≥33 % | IHI 40 % | IHI 2020 | Mensual |
| Cancelación quirúrgica | Cirugías canceladas / Cirugías programadas × 100 | ≤5 % | 2-5 % | AHRQ 2021 | Mensual |
| TMO contact center | Tiempo medio operación (seg) | ≤180 s | 120-150 s | — | Mensual |
| Resolución primer contacto | Consultas resueltas 1er contacto / Total consultas × 100 | ≥70 % | 72-80 % | — | Mensual |
| Cumplimiento GES/AUGE | Garantías cumplidas / Garantías activadas × 100 | 100 % | — | MINSAL-GES | Mensual |
| Adherencia guías clínicas | Auditorías conformes / Total auditorías × 100 | ≥85 % | — | AHRQ 2022 | Trimestral |
| NPS global red | Promotores − Detractores (escala −100 a +100) | ≥50 | — | — | Semestral |
| Incidentes seguridad reportados | N.° reportes / 1000 egresos | Tendencia ↑ (cultura reporte) | — | OMS 2021 | Mensual |
| % procesos con SOP vigente | SOPs actualizados / Total SOPs × 100 | ≥90 % | — | ISO 9001 | Trimestral |

### A.2 KPI de urgencias

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Door-to-triage | Tiempo arribo → clasificación (min) | ≤10 min | ACEP ≤5 min ESI-1 | ACEP 2023 | Continuo |
| Door-to-doctor | Tiempo arribo → evaluación médica (min) | ≤30 min | Median 28 min | ACEP 2023 | Continuo |
| LWBS (Left Without Being Seen) | Retiros sin atención / Consultas SUH × 100 | ≤2 % | 1-3 % | ACEP 2022 | Mensual |
| LOS SUH mediana | Mediana tiempo total en SUH (h) | ≤4 h | NHS 4h target | NHS 2023 | Mensual |
| LOS SUH p90 | Percentil 90 tiempo total en SUH (h) | ≤6 h | — | NICE 2022 | Mensual |
| Boarding time | Tiempo decisión admisión → salida de SUH (h) | ≤2 h | TJC ≤4h | TJC 2022 | Diario |
| Retorno 72h SUH | Reconsultas ≤72h / Egresos SUH × 100 | ≤3 % | 2-4 % | AHRQ 2021 | Mensual |
| Sepsis: antibiótico <1h | AB administrado ≤1h detección sepsis / Casos sepsis × 100 | ≥90 % | SSC ≥95 % | SSC 2021 | Mensual |
| Door-to-ECG en IAM | Tiempo arribo → ECG (min) | ≤10 min | AHA ≤10 min | AHA 2023 | Continuo |
| FMC-to-balloon (ICP) | Primer contacto médico → balón (min) | ≤90 min | ESC ≤90 min | ESC 2023 | Mensual |
| Door-to-needle ACV | Arribo → trombolisis (min) | ≤60 min | AHA ≤45 min | AHA 2022 | Mensual |
| Door-in-door-out (DIDO) | Arribo centro derivador → salida a ICP (min) | ≤30 min | AHA ≤30 min | AHA 2023 | Mensual |
| ROSC sostenido PCR | Retorno circulación espontánea ≥20min / PCR atendidos × 100 | ≥30 % | 25-35 % | AHA-Utstein 2023 | Mensual |
| Activación trauma team | Tiempo activación protocolo trauma (min) | ≤15 min | ATLS <15 min | ATLS 2022 | Continuo |
| Tiempo despacho EMS | Recepción llamada → despacho (min) | ≤2 min | NFPA ≤60s | NFPA 2021 | Continuo |
| Tiempo respuesta EMS p90 | Recepción llamada → escena p90 (min) | ≤8 min urbano | NFPA 8 min | NFPA 2021 | Mensual |
| Tasa sobre/infra-triaje | Discordancia triaje vs severidad real / Total triajes × 100 | ≤5 % combinado | — | ACEP 2022 | Trimestral |
| Analgesia oportuna <30min | Analgesia administrada ≤30min / Pacientes con dolor × 100 | ≥80 % | 75-85 % | AHRQ 2022 | Mensual |
| Caídas/1000 visitas SUH | Eventos caída × 1000 / Visitas SUH | ≤1.0 | 0.5-1.5 | AHRQ 2021 | Mensual |
| EAM en SUH | Eventos adversos medicamentos SUH × 1000 / Visitas | ≤2.0 | — | ISMP 2022 | Mensual |
| PREMs urgencias | Puntaje PREMs específico urgencias | ≥70/100 | — | MINSAL | Semestral |

### A.3 KPI de salud mental

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cobertura efectiva SM | Población con trastorno atendida / Prevalencia estimada × 100 | ≥50 % | OMS 40-60 % | OMS-mhGAP 2022 | Anual |
| Retención ≥4 atenciones 90d | Usuarios con ≥4 contactos en 90d / Ingresos × 100 | ≥70 % | — | NICE 2023 | Trimestral |
| Seguimiento post-alta <7d | Contacto ≤7d post-egreso / Egresos SM × 100 | ≥80 % | HEDIS 60 % | HEDIS 2023 | Mensual |
| Eventos críticos/1000 usuarios | (Suicidio + intento + agresión grave) × 1000 / Usuarios activos | Tendencia ↓ | — | OMS 2021 | Trimestral |
| Cambio clínico PHQ-9 ≥5 pts | Usuarios con reducción PHQ-9 ≥5 / Usuarios con PHQ-9 basal × 100 | ≥50 % | IAPT 50 % recovery | IAPT/NHS 2023 | Trimestral |
| Espera primera atención SM | Mediana días desde derivación a 1ra atención SM | ≤15d | NHS 28d | NHS 2023 | Mensual |
| Abandonos de tratamiento | Abandonos / Usuarios activos × 100 | ≤20 % | 15-25 % | — | Trimestral |
| Contenciones/1000 días-cama | Episodios contención × 1000 / Días-cama SM | Tendencia ↓ cero | — | Safewards 2022 | Mensual |
| Contacto post-alta suicidio <72h | Contacto ≤72h post-alta riesgo suicida / Egresos riesgo suicida × 100 | 100 % | NICE 100 % | NICE 2023 | Mensual |
| Reintentos suicidio 30d | Reintentos ≤30d / Altas post-intento × 100 | Tendencia ↓ | — | OMS 2021 | Mensual |
| PREMs salud mental | Puntaje PREMs específico SM | ≥75/100 | — | MINSAL | Semestral |
| HoNOS cambio promedio | Δ HoNOS ingreso-egreso promedio | ≥4 pts | NHS ≥4 | NHS-MHSDS 2023 | Trimestral |
| PCI vigentes (%) | Planes cuidado integral actualizados / Usuarios activos × 100 | ≥90 % | — | NICE 2022 | Mensual |
| Crisis resueltas in situ por EMC | Crisis resueltas sin traslado / Total activaciones EMC × 100 | ≥60 % | 50-70 % | — | Mensual |
| Readmisión psiquiátrica 30d | Reingresos ≤30d / Egresos SM × 100 | ≤15 % | 10-18 % | AHRQ 2022 | Mensual |

### A.4 KPI de hospitalización domiciliaria

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tasa escalamiento (retorno hospital) | Retornos hospitalarios / Admisiones HaH × 100 | ≤10 % | 7-10 % | Levine 2020 | Mensual |
| Readmisión 30d HaH | Reingresos ≤30d post-egreso HaH / Egresos HaH × 100 | ≤8.6 % | 7-8.6 % | Federman 2018 | Mensual |
| Costo por episodio HaH | Costo total episodio HaH / Costo DRG equivalente × 100 | 62-81 % | 19-38 % menor | Levine 2020 | Mensual |
| LOS equivalente HaH | Promedio días en programa HaH | ≤3.2d | 3.0-3.5d | Shepperd 2021 | Mensual |
| Door-to-home | Tiempo decisión admisión HaH → instalación domicilio (h) | ≤6 h | — | — | Continuo |
| Cumplimiento visitas HaH | Visitas realizadas / Visitas programadas × 100 | ≥95 % | — | — | Semanal |
| Tiempo respuesta deterioro | Tiempo detección alerta RPM → evaluación presencial (min) | ≤60 min | — | — | Continuo |
| PREMs HaH | Puntaje PREMs hospitalización domiciliaria | ≥85/100 | — | Shepperd 2021 | Trimestral |
| IAAS domiciliarias/1000 días | Infecciones asociadas × 1000 / Días-estada HaH | ≈0 | <0.5 | — | Mensual |
| Satisfacción cuidador (Zarit) | Puntaje Zarit Burden Interview | ≤40 (sin sobrecarga) | — | Zarit 1980 | Trimestral |

### A.5 KPI transversales

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tasa eventos adversos | EA / 1000 egresos | Tendencia ↓ | — | OMS 2021 | Trimestral |
| IAAS global | IAAS / 1000 días-cama | ≤3.5 | 2-5 ECDC | ECDC 2022 | Mensual |
| EAM/1000 días-cama | Eventos adversos medicamentos × 1000 / Días-cama | ≤5.0 | — | ISMP 2022 | Mensual |
| Cumplimiento hand hygiene | Observaciones conformes / Total observaciones × 100 | ≥80 % | OMS ≥80 % | OMS 2022 | Mensual |
| Uptime HCE | Horas disponibilidad / Horas totales × 100 | ≥99.5 % | 99.9 % tier-3 | — | Mensual |
| Mensajes FHIR conformes | Mensajes válidos / Total mensajes × 100 | ≥98 % | — | HL7 FHIR R4 | Mensual |
| Horas formación per cápita | Horas capacitación / Dotación (FTE) | ≥40 h/año | — | OIT 2022 | Anual |
| Rotación personal | Desvinculaciones / Dotación promedio × 100 | ≤15 % | 10-18 % salud | — | Anual |
| Ausentismo | Días ausencia / Días programados × 100 | ≤5 % | 3-6 % | — | Mensual |
| % staff certificado | Personal con certificación vigente / Total × 100 | ≥90 % | — | — | Anual |
| Cumplimiento presupuestario | Ejecución presupuestaria / Presupuesto asignado × 100 | 95-100 % | — | DIPRES | Trimestral |
| Costo por caso DRG | Costo real / Costo esperado DRG | ≤1.0 | — | FONASA IR-GRD | Mensual |
| NPS interno | Promotores − Detractores staff (−100 a +100) | ≥30 | — | — | Anual |
| Adopción de mejoras (stick rate) | Mejoras sostenidas ≥6m / Total mejoras implementadas × 100 | ≥70 % | IHI 60-70 % | IHI 2022 | Semestral |
| Beneficios capturados vs prometidos | Beneficios realizados / Beneficios proyectados × 100 | ≥80 % | — | PMI 2021 | Semestral |

---

## Anexo B: Mapas de procesos (BPMN textual)

Notación: `**[ROL]** Acción → Decisión? {Sí: ruta / No: ruta} → Siguiente`

## B.1 Flujo SUH completo

```
**[EMS]** Pre-notificación (radio/MPDS) → Transmite datos: mecanismo, signos vitales, ETA
 → Código activación? {Trauma/ACV/IAM: activa equipo receptor / Estándar: continúa}

**[TRIAJE]** Recepción paciente → Registro administrativo (≤2 min)
 → Clasificación ESI (≤10 min arribo)
 → ESI-1/2? {Sí: circuito crítico / No: circuito general}

**[MÉDICO SUH]** Evaluación médica (≤30 min door-to-doctor)
 → Solicita exámenes? {Sí: orden apoyo diagnóstico / No: diagnóstico clínico}
 → Protocolo tiempo-dependiente? {IAM: ECG ≤10min, ICP ≤90min / ACV: TC ≤25min, TNK ≤60min / Sepsis: AB ≤1h}

**[APOYO DIAGNÓSTICO]** Procesamiento lab/imagen
 → Resultados críticos? {Sí: notificación activa ≤15min / No: resultado a HCE}

**[MÉDICO SUH]** Integración resultados → Diagnóstico
 → Requiere interconsulta? {Sí: solicitud / No: plan tratamiento}

**[ESPECIALISTA]** Evaluación interconsulta (≤60 min ESI-2, ≤4h ESI-3)
 → Asume manejo? {Sí: traslado a servicio / No: recomendaciones a SUH}

**[BED MANAGEMENT]** Gestión destino
 → ¿Observación/UOCS? {Sí: ingreso observación ≤24h / No: continúa}
 → Decisión destino: Alta SUH? {Sí: alta + contrarreferencia APS /
 Hospitalización? {Sí: cama asignada ≤2h boarding /
 Traslado? {Sí: coordinación SAMU + centro receptor}}}

**[MÉDICO SUH]** Documentación cierre → Indicaciones alta / ingreso → Fin
```

## B.2 Referencia / contrarreferencia

```
**[APS]** Detección necesidad derivación → Evaluación criterios referencia
 → Cumple criterios? {No: manejo APS / Sí: genera eReferral (FHIR ServiceRequest)}

**[CENTRO COORDINACIÓN]** Recepción eReferral → Validación pertinencia (≤48h)
 → Pertinente? {No: rechaza + feedback a APS / Sí: priorización clínica}
 → Asignación especialidad + agendamiento → Notificación a paciente

**[ESPECIALIDAD]** Atención especialista → Diagnóstico/plan terapéutico
 → Requiere seguimiento especialidad? {Sí: agenda control / No: contrarreferencia}

**[ESPECIALIDAD]** Genera contrarreferencia (≤7d) → FHIR DiagnosticReport + CarePlan
 → Envío a centro coordinación

**[CENTRO COORDINACIÓN]** Distribución contrarreferencia a APS origen

**[APS]** Recepción contrarreferencia → Actualización plan de cuidado
 → Seguimiento según indicaciones → Fin ciclo
```

## B.3 Alta segura

```
**[MÉDICO TRATANTE]** Decisión de alta (criterios clínicos cumplidos)
 → Redacción epicrisis + diagnósticos CIE-10
 → Indicaciones ambulatorias (medicamentos, controles, alertas)

**[FARMACIA]** Conciliación medicamentosa → Diferencias detectadas?
 {Sí: revisión con médico tratante / No: preparación recetas}
 → Dispensación medicamentos al alta

**[ENFERMERÍA]** Educación al paciente/cuidador (método teach-back)
 → Comprensión verificada? {No: repite educación / Sí: firma consentimiento}
 → Entrega carta de alta + material educativo

**[TRABAJO SOCIAL]** Evaluación necesidades sociales
 → Requiere apoyo? {Sí: coordinación red social / No: continúa}
 → Gestión transporte si necesario

**[MÉDICO TRATANTE]** Genera eReferral a APS (FHIR ServiceRequest + CarePlan)
 → Agenda control si requerido

**[APS]** Recepción notificación alta → Contacto paciente 48-72h
 → Visita domiciliaria si alto riesgo → Seguimiento activo → Fin
```

## B.4 Crisis de salud mental

```
**[COMUNIDAD/APS]** Detección crisis (auto-reporte, familia, APS, policía)
 → Activación EMC (equipo móvil de crisis)

**[EMC]** Desplazamiento al lugar → Evaluación inicial seguridad escena
 → Evaluación riesgo suicida/heteroagresión (Columbia/SAD PERSONS)
 → Riesgo inminente? {No: intervención in situ (contención verbal, plan de seguridad) /
 Sí: ¿Acepta traslado voluntario? {Sí: traslado asistido / No: evaluación involuntaria según Ley 20.584}}

**[EMC]** Resolución in situ? {Sí: plan de seguimiento <72h → notificación APS → Fin /
 No: traslado a SUH}

**[SUH]** Recepción → Triaje psiquiátrico → Estabilización médica
 → Requiere hospitalización SM? {No: alta + plan crisis + seguimiento EMC /
 Sí: solicitud cama unidad SM}

**[UNIDAD SM]** Ingreso → Evaluación psiquiátrica integral (≤24h)
 → Estabilización farmacológica + psicoterapéutica
 → Plan de cuidado integral (PCI) → Preparación egreso

**[UNIDAD SM]** Egreso → Contacto post-alta ≤72h (si riesgo suicida: obligatorio)
 → Derivación a programa ambulatorio SM → Seguimiento APS → Fin
```

## B.5 Admisión hospitalización domiciliaria (HaH)

```
**[SUH/APS]** Identificación candidato HaH → Screening elegibilidad
 → Cumple criterios clínicos? {No: manejo convencional / Sí: continúa}
 → Cumple criterios domiciliarios? {No: manejo convencional / Sí: continúa}

**[EQUIPO HaH]** Evaluación presencial → Consentimiento informado paciente/cuidador
 → Acepta? {No: manejo convencional / Sí: ingreso HaH}

**[LOGÍSTICA]** Setup domiciliario: equipamiento, medicamentos, conectividad RPM
 → Instalación dispositivos monitoreo (SpO2, PA, T°, FC)
 → Verificación conectividad → Prueba alarmas

**[CENTRO COMANDO]** Ingreso en sistema → Asignación equipo tratante
 → Configuración alertas RPM → Monitoreo 24/7

**[EQUIPO HaH]** Visitas programadas (médico + enfermería)
 → Tratamiento según protocolo (EV, O2, kinesioterapia)
 → Alerta RPM deterioro? {Sí: evaluación remota → ¿Escalamiento?
 {Sí: retorno hospital (SAMU) / No: ajuste tratamiento} /
 No: continúa protocolo}

**[EQUIPO HaH]** Criterios egreso cumplidos → Egreso HaH
 → Transición: eReferral a APS destino + plan seguimiento

**[APS DESTINO]** Contacto post-egreso 48-72h → Seguimiento ambulatorio → Fin
```

---
