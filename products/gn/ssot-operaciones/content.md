---
urn: urn:gn:kb:ssot-operaciones
nombre: ssot-operaciones
version: 1.0.1
estado: borrador
descripcion: "Documento SSOT GORE Ñuble migrado como conocimiento borrador; su estado no implica validación institucional."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-ssot/ssot-operaciones.md (sha256:b1561241de71e895fdb63164ec2a03743b51ab7415a5107a054611dc87686786); cuerpo preservado íntegramente durante la migración KORA del 2026-08-02."
autor: FS
creado: 2026-03-10
lang: es
tags: [ssot, operaciones, alertas, compromisos, problemas, hitos, reuniones]
familia: bok
---

# SSOT — Procesos operativos GORE Ñuble

## Resumen

Procesos operativos transversales a la gestión IPR. 7 entidades: alertas (ontología), compromisos operacionales (GORE_OS), problemas IPR (GORE_OS), hitos (ontología), avances (ontología), reuniones de crisis (GORE_OS), partes IPR (GORE_OS). 4 de 7 carecen de clase ontológica — son constructos de implementación.

## Alertas

### Tipos de alerta (6)

| Código | Tipo | Descripción |
|--------|------|-------------|
| SEC | Seguridad | Evento de seguridad informática o física |
| THR | Umbral | Superación de umbral predefinido (presupuesto, indicador) |
| EXP | Vencimiento | Proximidad de fecha límite (convenio, garantía, plazo) |
| CMP | Cumplimiento | Incumplimiento normativo o de compromisos |
| OPS | Operacional | Sistemas y operaciones (error, indisponibilidad) |
| REP | Reputacional | Riesgo de imagen institucional |

Fuente: ReferenceData.ttl, 6 instancias `gnub:AlertType`.

### Severidades (5)

| Código | Nivel | Acción requerida |
|--------|-------|-----------------|
| P1 | Crítica | Acción inmediata |
| P2 | Alta | Atención prioritaria |
| P3 | Media | Atención programada |
| P4 | Baja | Cuando sea posible |
| P5 | Informativa | Sin acción |

Fuente: ReferenceData.ttl, 5 instancias `gist:Category`.

**Reconciliación:** GORE_OS usa 4 severidades (CRITICO, ALTO, ATENCION, INFO) — mapeo no 1:1 con ontología (5 niveles P1-P5). P3 (Media) y P4 (Baja) de la ontología se comprimen en ATENCION en GORE_OS. Naming distinto (P1-P5 vs descriptivo).

### Modelo ontológico

`gnub:Alert` (subClass `gist:Event`). Propiedades: `hasSeverity` (→ `gist:Category`), `hasAlertType` (→ `AlertType`), `triggersAlert` (inversa: evento → alerta).

`gnub:Notification` (subClass `gist:Event`) — mensaje informativo menos urgente que una alerta. Sin instancias en reference data.

`gnub:Risk` (subClass `gist:Category`) — categoría de riesgo: operacional, financiero, reputacional, legal, seguridad.

[impl: `core.alert`. `subject_type` fully-qualified: `'core.ipr'`, `'core.operational_commitment'`, etc. Severidad CRITICO/ALTO/ATENCION/INFO. `AlertCard.onViewSubject` navega a cualquier `subject_type`. CLAUDE.md §Rule 3]

## Compromisos operacionales

Sin clase ontológica. Constructo GORE_OS (`core.operational_commitment`).

### FSM

PENDIENTE → EN_PROGRESO → COMPLETADO → VERIFICADO

Historial: `commitment_history`.

### Entidades relacionadas

- Vinculado a IPR vía `ipr_id`
- CRUD: `/compromisos/nuevo` + inline vía `IprCompromisoDrawer`
- Drawer muestra link clickeable a IPR (`ipr_codigo_bip`)

**Reconciliación:** La ontología modela `gnub:BudgetaryCommitment` (compromiso financiero/presupuestario) como subclase de `gist:Commitment`, pero NO modela compromisos operacionales (tareas, acuerdos de gestión). Gap ontológico.

[impl: CLAUDE.md §Operational Layer. 16 tests en `test_compromisos.py`]

## Problemas IPR

Sin clase ontológica. Constructo GORE_OS (`core.ipr_problem`).

### FSM

ABIERTO → EN_GESTION → RESUELTO | CERRADO_SIN_RESOLVER

### Tipos

TECNICO, FINANCIERO, LEGAL, ADMINISTRATIVO, SOCIAL, AMBIENTAL.

Vinculado a IPR vía `ipr_id`. Timeline de estados. CRUD: `/problemas/nuevo` + inline vía `IprProblemaDrawer`.

**Reconciliación:** El Omega menciona "problemas" solo en contexto F0 (identificación del problema social que justifica la IPR), NO como entidad de tracking operacional. Gap ontológico y documental.

[impl: CLAUDE.md §Operational Layer. 8 tests en `test_problemas.py`]

## Hitos IPR

### Modelo ontológico

`gnub:ProjectMilestone` (subClass `gist:ScheduledTask`). Tiene fecha planificada y fecha real. Propiedad `triggersPayment` (→ `PaymentEvent`) — hito cumplido gatilla pago de cuota.

Aspectos relacionados:
- `gnub:PhysicalProgressAspect` — porcentaje avance físico actual (0-100%)
- `gnub:PlannedProgressAspect` — porcentaje avance planificado según cronograma

### Implementación GORE_OS

`core.ipr_milestone`. 13 tipos. Campos: planned/actual dates, auto `deviation_days` (GENERATED). Admin-only write.

[impl: `GET/POST/PATCH /api/ipr/{id}/hitos`. CLAUDE.md §Operational Layer]

## Avances (informes de ejecución)

### Modelo ontológico

`gnub:ExecutionReport` (subClass `gist:Event`) — reporte mensual de ejecución física y financiera per IPR.

### Implementación GORE_OS

`core.progress_report`. Auto-incremented `report_number` per IPR.

[impl: `POST/GET /api/ipr/{id}/avances`. CLAUDE.md §Operational Layer]

## Reuniones de crisis

Sin clase ontológica. Constructo GORE_OS.

### FSM

PROGRAMADA → EN_CURSO → FINALIZADA

### Modelo GORE_OS

Usa tablas existentes: `core.committee` + `core.session` + `core.crisis_meeting` + `core.minute` + `core.session_agreement`.

Comité `COMITE-CRISIS` auto-creado en primer uso. Auto-sugerencias desde: alertas críticas, compromisos vencidos, problemas abiertos. Badges BIP vinculan a IPR.

**Reconciliación:** El Omega describe "Sesión CORE" (proceso PROC-006, 3-6 hrs) pero NO reuniones de crisis como entidad separada. CORE sessions modeladas en `ssot-organica` (quórum). Gap ontológico.

[impl: `core_sessions.py` (CORE: committee `CONSEJO-REGIONAL`). CLAUDE.md §Rules 22, 31]

## Partes IPR

### Modelo ontológico

No existe como entidad reificada. Ontología modela participación vía propiedades directas: `gnub:hasApplicant`, `gnub:hasExecutor` (IPR → `gist:Organization`).

### Implementación GORE_OS

`core.ipr_party` — entidad reificada con 9 roles:

POSTULANTE, EJECUTOR, FORMULADOR, SUPERVISOR, CONTRAPARTE, BENEFICIARIO, GARANTE, REFERENTE_TECNICO, MANDATARIO.

UNIQUE constraint `uq_ipr_party_role`. Admin-only write.

**Reconciliación:** GORE_OS reifica la relación IPR-persona-rol como entidad (permite múltiples partes con roles distintos por IPR). La ontología usa propiedades directas (solo 2 roles: postulante, ejecutor). Gap ontológico para los 7 roles restantes.

[impl: `GET/POST/DELETE /api/ipr/{id}/partes`. CLAUDE.md §Operational Layer. Person columns: `names`, `paternal_surname`]

## Cobertura ontológica

| Entidad | Clase ontológica | Instancias ABox | GORE_OS |
|---------|-----------------|-----------------|---------|
| Alertas | `gnub:Alert` + `AlertType` + Severity | 6 + 5 | `core.alert` |
| Hitos | `gnub:ProjectMilestone` | 2 (ejemplo) | `core.ipr_milestone` (13 tipos) |
| Avances | `gnub:ExecutionReport` | 0 | `core.progress_report` |
| Compromisos op. | — | — | `core.operational_commitment` |
| Problemas | — | — | `core.ipr_problem` |
| Reuniones crisis | — | — | `core.crisis_meeting` |
| Partes | — (propiedades) | — | `core.ipr_party` (9 roles) |
