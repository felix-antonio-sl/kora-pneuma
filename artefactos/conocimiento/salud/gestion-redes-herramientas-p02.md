---
urn: urn:salud:kb:gestion-redes-herramientas-p02
nombre: gestion-redes-herramientas-p02
version: 2.0.0
estado: publicado
descripcion: "Gestión de Redes Asistenciales — Herramientas y Anexos - Parte 02"
fuente: "Migrado de la bestia (~/kora @ 9de5dc38b78c23574d24a481a5f84d70173c2203) artifacts/knowledge/salud/salubrista/gestion-redes/05-herramientas-anexos--p02.md (sha256:c0455a6cac56b5c1e5dfa82cb248e3ff30034b7e6387932b80c31e2ea89c4b1a) el 2026-07-17; cuerpo byte-fiel; frontmatter normalizado a ley/2; shard enlazado por cita a urn:salud:kb:gestion-redes-herramientas."
autor: FS
creado: 2026-03-03
lang: es
tags: [gestion-redes, kpi, bpmn, plantillas, fhir, simulacion, madurez, herramientas]
familia: bok
cita: [urn:salud:kb:gestion-redes-herramientas]
---

# Gestión de Redes Asistenciales — Herramientas y Anexos - Parte 02

## C.1 SLA inter-nodos

**SLA 1: Derivación ACV a centro de trombectomía**

```yaml
sla:
 nombre: "Derivación ACV isquémico a centro trombectomía"
 versión: "1.0"
 nodo_origen: "SUH hospital primario"
 nodo_destino: "Centro neurovascular (trombectomía)"
 condición_activación: "ACV isquémico con oclusión gran vaso confirmada (CTA/MRA)"
 métricas:
 - indicador: "Door-in-door-out (DIDO)"
 meta: "≤30 min"
 escalamiento: "≥45 min → alerta jefe turno"
 - indicador: "Onset-to-puncture"
 meta: "≤180 min"
 escalamiento: "≥240 min → revisión proceso"
 - indicador: "Notificación pre-arribo"
 meta: "≥15 min antes llegada"
 escalamiento: "Incumplimiento → reporte incidente"
 responsabilidades:
 origen:
 - "TC/CTA completado antes de traslado"
 - "Trombolisis EV iniciada si indicada (no retrasa traslado)"
 - "Comunicación SBAR al centro receptor"
 destino:
 - "Equipo neurovascular activado pre-arribo"
 - "Sala angiografía disponible"
 - "Retroalimentación resultado ≤24h"
 penalización: "Incumplimiento reiterado (≥3/mes) → auditoría conjunta obligatoria"
 revisión: "Trimestral"
```

**SLA 2: HaH respuesta ante deterioro**

```yaml
sla:
 nombre: "Respuesta ante deterioro clínico HaH"
 versión: "1.0"
 nodo_origen: "Centro comando HaH"
 nodo_destino: "SAMU / SUH referencia"
 condición_activación: "Alerta RPM: SpO2 <90%, FC >120 o <50, PAS <90, T° >39°C; o deterioro clínico evaluado por enfermería remota"
 métricas:
 - indicador: "Tiempo detección → contacto enfermería"
 meta: "≤5 min"
 escalamiento: "≥10 min → alerta supervisor"
 - indicador: "Evaluación remota → decisión escalamiento"
 meta: "≤15 min"
 escalamiento: "≥30 min → reporte incidente"
 - indicador: "Decisión → llegada SAMU a domicilio"
 meta: "≤20 min urbano"
 escalamiento: "≥30 min → coordinación directa con SAMU"
 responsabilidades:
 centro_comando:
 - "Monitoreo 24/7 alertas RPM"
 - "Contacto telefónico/video inmediato con paciente"
 - "Activación SAMU si criterios escalamiento"
 samu:
 - "Priorización despacho (código HaH)"
 - "Traslado a SUH de referencia (no al más cercano)"
 suh_referencia:
 - "Acceso a registro HaH del paciente"
 - "Cama priorizada si requiere hospitalización"
 penalización: "Tiempo respuesta >60 min → auditoría obligatoria + reporte SEREMI"
 revisión: "Mensual"
```

**SLA 3: Derivación crisis SM a unidad psiquiátrica**

```yaml
sla:
 nombre: "Derivación crisis salud mental a unidad psiquiátrica"
 versión: "1.0"
 nodo_origen: "SUH / EMC (equipo móvil crisis)"
 nodo_destino: "Unidad corta estadía psiquiátrica"
 condición_activación: "Riesgo suicida alto (Columbia ≥4) o psicosis aguda con riesgo heteroagresión, sin respuesta a intervención en crisis"
 métricas:
 - indicador: "Evaluación psiquiátrica en SUH"
 meta: "≤60 min desde solicitud"
 escalamiento: "≥90 min → alerta jefe servicio SM"
 - indicador: "Asignación cama unidad SM"
 meta: "≤4 h desde decisión hospitalización"
 escalamiento: "≥6 h → escalamiento a dirección"
 - indicador: "Contacto post-alta (riesgo suicida)"
 meta: "≤72 h"
 escalamiento: "Incumplimiento → reporte crítico"
 responsabilidades:
 suh_emc:
 - "Estabilización médica completada"
 - "Evaluación riesgo estandarizada (Columbia/SAD PERSONS)"
 - "Contención farmacológica según protocolo si necesaria"
 - "Comunicación SBAR a unidad SM"
 unidad_sm:
 - "Cama disponible o plan contingencia activado"
 - "Evaluación integral ≤24h post-ingreso"
 - "Plan de cuidado integral (PCI) ≤48h"
 - "Planificación egreso desde ingreso"
 penalización: "Boarding psiquiátrico >12h → reporte a SEREMI + auditoría red"
 revisión: "Trimestral"
```

## C.2 Matriz RACI

| Actividad | Dir. Servicio | Dir. Hospital | Jefe Unidad | Médico tratante | Enfermería | TI | Farmacia | Calidad | Trabajo social | SAMU | APS |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Gobernanza de red | A | R | I | I | I | I | I | C | I | I | C |
| Gestión de camas | I | A | R | C | R | C | I | I | I | I | I |
| Triaje SUH | I | I | A | R | R | I | I | C | I | C | I |
| Conciliación medicamentosa | I | I | C | R | C | I | A | C | I | I | I |
| Alta segura | I | I | A | R | R | I | C | C | R | I | I |
| eReferral / contrarreferencia | C | A | R | R | C | R | I | I | I | I | R |
| Monitoreo KPI | A | R | R | I | I | R | I | A | I | I | C |
| Respuesta ante desastre/MCI | A | R | R | R | R | C | R | C | R | R | C |
| Admisión HaH | I | A | R | R | R | R | R | C | C | C | C |
| Gestión crisis SM | I | A | R | R | R | I | C | C | R | R | C |
| Interoperabilidad FHIR | C | A | I | I | I | R | I | I | I | I | I |
| Mejora continua (PDSA) | I | A | R | C | C | C | C | R | C | I | C |

Leyenda: **R** = Responsable, **A** = Aprobador, **C** = Consultado, **I** = Informado.

## C.3 Checklist apertura de servicios

**Legal/regulatorio:**
- [ ] Resolución sanitaria SEREMI vigente
- [ ] Autorización Superintendencia de Salud (si aplica)
- [ ] Convenios interinstitucionales firmados

**Dotación:**
- [ ] Dotación mínima definida según normativa (médicos, enfermeras, TENS, administrativos)
- [ ] Credenciales profesionales verificadas (SIS/Registro Nacional)
- [ ] Plan de turnos y contingencia aprobado

**Equipamiento:**
- [ ] Equipamiento biomédico adquirido e instalado
- [ ] Calibración y certificación de equipos críticos
- [ ] Stock de insumos y medicamentos según listado mínimo
- [ ] Cadena de frío verificada (si aplica)

**Sistemas:**
- [ ] HCE operativa y conectada a red
- [ ] Interfaces FHIR configuradas y probadas
- [ ] Sistema de turnos/agenda en producción
- [ ] RPM operativo (si HaH)

**Seguridad:**
- [ ] Plan de emergencia y evacuación aprobado
- [ ] Protocolos de seguridad del paciente implementados
- [ ] Sistema de reporte de incidentes activo
- [ ] Simulacro de contingencia realizado

## C.4 Estructura SOP/WI

```yaml
sop:
 código: "SOP-SUH-001"
 título: "Protocolo de triaje ESI en Servicio de Urgencia Hospitalario"
 versión: "1.0"
 fecha_vigencia: "2026-03-01"
 próxima_revisión: "2027-03-01"
 propietario: "Jefatura SUH"
 aprobado_por: "Dirección médica"
 objetivo: "Estandarizar clasificación de urgencia mediante ESI 5 niveles para asegurar atención oportuna según severidad"
 alcance: "Todos los pacientes que consultan en SUH, incluyendo derivaciones EMS"
 definiciones:
 - "ESI: Emergency Severity Index (5 niveles)"
 - "Door-to-triage: tiempo desde arribo administrativo a clasificación"
 responsabilidades:
 enfermera_triaje: "Clasificación ESI, registro en HCE, activación códigos"
 médico_jefe_turno: "Supervisión, resolución discrepancias, re-triaje"
 procedimiento:
 - paso: 1
 acción: "Recepción del paciente en módulo triaje"
 responsable: "TENS admisión"
 tiempo: "≤2 min"
 - paso: 2
 acción: "Evaluación triaje ESI: aspecto general, signos vitales, motivo consulta"
 responsable: "Enfermera triaje"
 tiempo: "≤5 min"
 - paso: 3
 acción: "Asignación nivel ESI y circuito (crítico/general/fast-track)"
 responsable: "Enfermera triaje"
 tiempo: "Inmediato"
 - paso: 4
 acción: "Registro en HCE + notificación a circuito asignado"
 responsable: "Enfermera triaje"
 tiempo: "≤1 min"
 documentos_asociados:
 - "Algoritmo ESI v4 (Gilboy et al. 2020)"
 - "Protocolo activación código ACV/IAM/Trauma"
 indicadores:
 - "Door-to-triage ≤10 min (meta)"
 - "Tasa sobre/infra-triaje ≤5 %"
 registros: "HCE módulo triaje, libro de novedades turno"
 control_cambios:
 - versión: "1.0"
 fecha: "2026-03-01"
 cambio: "Creación inicial"
 autor: "Jefatura SUH"
```

---

## Anexo D: Salud digital

### D.1 Perfiles FHIR recomendados

| Recurso FHIR | Uso clínico | Perfil / Extensión |
|---------------|-------------|-------------------|
| Patient | Identificación demográfica, RUT, previsión | CL Core Patient (MINSAL) |
| Encounter | Registro atención (ambulatoria, urgencia, hospitalización, HaH) | CL Core Encounter + extensión tipo HaH |
| EpisodeOfCare | Seguimiento longitudinal de episodio (SM, HaH, crónico) | Base R4 + extensión estado red |
| ServiceRequest | eReferral, interconsulta, solicitud exámenes | CL Core ServiceRequest |
| Condition | Diagnósticos CIE-10, problemas activos | CL Core Condition |
| Observation | Signos vitales, RPM, escalas clínicas (PHQ-9, HoNOS, ESI) | Vital Signs Profile R4 + extensión escalas |
| MedicationRequest | Prescripción, conciliación medicamentosa | CL Core MedicationRequest |
| DiagnosticReport | Resultados laboratorio, imagenología | CL Core DiagnosticReport |
| CarePlan | Plan de cuidado integral (PCI), plan de alta, plan de crisis SM | Base R4 + extensión multidisciplinario |

### D.2 Patrón de integración

**Arquitectura**: Event-driven (EDA) con bus de eventos clínicos.

```
Evento clínico (HCE) → Broker mensajería (HL7 FHIR Subscription / Kafka)
 → Cola por tipo: admisión | alta | resultado_crítico | alerta_RPM | derivación
 → Consumidores:
 - Bed management (admisión/alta)
 - Centro coordinación (derivaciones)
 - Centro comando HaH (alertas RPM)
 - Dashboard KPI (todos)
 - Notificaciones paciente (alta, citas)
```

**Principios**:
- Eventos inmutables, idempotentes
- Retry con backoff exponencial (máx 3 reintentos)
- Dead-letter queue para eventos fallidos
- Trazabilidad end-to-end (correlation ID)
- Conformidad HL7 FHIR R4 ≥98 %

### D.3 Terminologías

| Dominio | Estándar | Ejemplo |
|---------|----------|---------|
| Diagnósticos | ICD-10 (CIE-10 adaptación chilena) | J18.9 Neumonía no especificada |
| Procedimientos | ICD-10-PCS / FONASA | 0BJ08ZZ Inspección pulmón |
| Hallazgos clínicos | SNOMED CT | 386661006 Fiebre |
| Laboratorio | LOINC | 2160-0 Creatinina sérica |
| Medicamentos | ATC / Vademécum ISP | N05AH03 Olanzapina |

### D.4 Ciberseguridad: checklist mínimo

1. **MFA obligatorio** para acceso a HCE y sistemas críticos
2. **Cifrado en tránsito** (TLS 1.3) y en reposo (AES-256) para datos clínicos
3. **Segmentación de red**: red clínica aislada de red administrativa y guest
4. **Backups automáticos**: RPO ≤1h, RTO ≤4h para HCE; prueba restauración trimestral
5. **Gestión de parches**: vulnerabilidades críticas parcheadas ≤72h; programadas ≤30d
6. **Control de acceso RBAC**: perfiles por rol, revisión trimestral de privilegios
7. **Auditoría de accesos**: logs inmutables ≥12 meses; alertas acceso anómalo
8. **DRP (Disaster Recovery Plan)**: documentado, probado semestralmente, RTO validado
9. **Capacitación seguridad**: phishing simulado trimestral; formación anual obligatoria
10. **Gestión de dispositivos médicos IoT/RPM**: inventario, firmware actualizado, red dedicada, monitoreo tráfico anómalo

---
