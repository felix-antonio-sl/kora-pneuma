---
urn: urn:gn:kb:ssot-relaciones-dominio
nombre: ssot-relaciones-dominio
version: 2.0.0
estado: borrador
descripcion: "Documento SSOT GORE Ñuble migrado como conocimiento borrador; su estado no implica validación institucional."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-ssot/ssot-relaciones-dominio.md (sha256:93171ba7b6b428a9f7e2b37ab9d0bdc98de7e1c43c63f2f214a743bb54918652); cuerpo preservado íntegramente durante la migración KORA del 2026-08-02."
autor: FS
creado: 2026-03-10
lang: es
tags: [ssot, relaciones, dominio, ipr, convenio, resolucion, morfismos, categorico]
familia: bok
---

# SSOT — Relaciones de dominio

## Resumen

Modelo relacional categórico del dominio GORE Ñuble. Parte I: triángulo IPR–Convenio–Resolución (5 entidades centrales, 8 morfismos, 5 path equations). Parte II: IPR como objeto terminal (13 satélites entrantes), alerta polimórfica, cadena de gobernanza CORE, budget mediator chain, DGI cartera colímite, user→role→population fibración. Transversal a todos los satélites del bundle.

## Objetos y superclases gist

| Objeto | Superclase gist | Naturaleza | Tabla GORE_OS |
|--------|----------------|-----------|---------------|
| `gnub:IPR` | `gist:Agreement` | El QUÉ — inversión pública regional | `core.ipr` |
| `gnub:GOREAgreement` | `gist:Contract` | El CÓMO — vehículo legal bilateral | `core.agreement` |
| `gnub:AdministrativeAct` | `gist:Agreement` | La AUTORIZACIÓN — acto formal unilateral | `core.administrative_act` |
| `gnub:BudgetaryCommitment` | `gist:Commitment` | La OBLIGACIÓN — compromiso presupuestario sostenido | `core.budget_commitment` |
| `gnub:Rendition` | `gist:Event` | La RENDICIÓN — prueba de uso correcto de fondos | `core.rendition` |

### Distinción GOREAgreement vs AdministrativeAct

Ambos son `gist:Agreement` pero con semántica disjunta:

| Concepto | Superclase | Bilateralidad | Ejemplos |
|----------|-----------|---------------|----------|
| GOREAgreement | `gist:Contract` | BILATERAL — partes explícitas (GORE + Ejecutor) | Convenio Mandato, Convenio Transferencia |
| AdministrativeAct | `gist:Agreement` | UNILATERAL — acto formal sin contraparte bilateral | Resolución Exenta, Decreto |

Fuente: goreNubleOntology.ttl scopeNote (línea 1010). La Resolución NO es parte del Convenio — lo autoriza externamente. El Convenio NO es un acto administrativo — es un contrato bilateral.

### Subtipos disjuntos

GOREAgreement: `TransferAgreement` ⊥ `MandateAgreement`
- Transferencia: recursos upfront → rendición SISREC posterior
- Mandato: estados de pago contra avance de obra

AdministrativeAct: `Resolution` ⊥ `Decree`
- Resolución: exenta o afecta a TdR CGR
- Decreto: sujeto a TdR CGR (modificaciones Partida 31)

## Morfismos

| Morfismo | Dominio | Rango | Definición |
|----------|---------|-------|-----------|
| `isExecutedVia` | IPR | GOREAgreement | Convenio a través del cual se ejecuta la IPR |
| `approvesAct` | Resolution | TransferAgreement | Resolución que aprueba y formaliza un convenio |
| `triggeredBy` | IPRStateTransition | AdministrativeAct | Acto que gatilla transición de estado IPR |
| `confers` | CommitmentEvent | BudgetaryCommitment | Evento que confiere compromiso presupuestario |
| `rendersFor` | Rendition | TransferAgreement | Convenio al que corresponde la rendición |
| `requiresAccountability` | GOREAgreement | AccountabilityProcess | Convenio que requiere proceso de rendición |
| `hasApprovalStage` | AdministrativeAct | ApprovalFlowStage | Etapa actual en flujo de aprobación |
| `governs` / `isGovernedBy` | GOREAgreement ↔ IPR | (inversa) | Convenio gobierna la IPR |

### Dualidad Acto / Documento

La ontología distingue el acto abstracto del documento físico:

```
Resolution (acto) ──isExpressedIn──→ FormattedContent (documento)
                   ──isCategorizedBy──→ AdministrativeDocumentType
```

El acto confiere compromisos. El documento registra el acto.

## Diagrama de composición

```
                 Resolution ───approvesAct───→ GOREAgreement
                     |                             ↑    |
                hasApprovalStage             isExecutedVia  requiresAccountability
                     ↓                             |    ↓
              ApprovalFlowStage                   IPR  AccountabilityProcess
                                                   ↑
                                                   |
               CommitmentEvent ──confers──→ BudgetaryCommitment
                (CDP emisión)

              Rendition ──rendersFor──→ TransferAgreement (≡ GOREAgreement)
```

## Path equations

### PE-1: Formalización de transferencia

El path `IPR → GOREAgreement ← Resolution` conmuta: la Resolución Aprobatoria autoriza el Convenio que ejecuta la IPR.

`approvesAct ∘ emit_resolution = authorize ∘ isExecutedVia`

Emitir una resolución que aprueba un convenio es equivalente a autorizar la ejecución de la IPR vía ese convenio.

### PE-2: Ciclo de rendición

`requiresAccountability ∘ rendersFor⁻¹ = accountability_of`

Rendir por un convenio ES el proceso de accountability de ese convenio.

### PE-3: Morfismo parcial isExecutedVia

`isExecutedVia: IPR → GOREAgreement` es parcial — solo aplica a IPRs con mecanismo de transferencia.

| Modo ejecución | isExecutedVia | Formalización |
|----------------|:-------------:|---------------|
| Transferencia (FRIL, Transfer, Subv8) | Definido → GOREAgreement | Convenio bilateral |
| Ejecución directa (SNI, C33, Glosa 06) | ∅ (no aplica) | Solo Resolución + CDP |

IPRs de ejecución directa generan Resoluciones y CDPs pero NO Convenios.

### PE-4: Transición IPR gatillada por acto

`triggeredBy: IPRStateTransition → AdministrativeAct`

Las transiciones de estado F3→F4 y F4→F5 son gatilladas por actos administrativos:

| Transición | Acto gatillante |
|-----------|-----------------|
| Aprobación CORE → CDP Emitido | Resolución (Acuerdo CORE) |
| CDP Emitido → Decreto Tramitado | Decreto (asignación presupuestaria) |
| Decreto → Convenio Formalizado | Resolución Aprobatoria + Convenio bilateral |
| Convenio → Tomado de Razón | Resolución → TdR CGR |

### PE-5: BudgetaryCommitment como mediador

El `BudgetaryCommitment` vincula Agreement con recursos:

```
CommitmentEvent (PreCommitment/CDP)
    ──confers──→ BudgetaryCommitment
                     hasGiver = GORE
                     hasGetter = Ejecutor/Municipalidad
                     hasMagnitude = Monto (CLP)
```

La obligación sostenida (Commitment) es independiente del evento que la creó. Permite compromisos multi-año cuyo estado de cumplimiento evoluciona independientemente.

## Composición: ciclo completo por fase

| Fase | Entidades involucradas | Morfismos activos |
|------|----------------------|------------------|
| F0-F2 | IPR | — (evaluación, sin formalización) |
| F3 | IPR + BudgetaryCommitment + AdministrativeAct | triggeredBy, confers |
| F4 (directa) | IPR + Resolution + BudgetaryCommitment | triggeredBy, confers |
| F4 (transferencia) | IPR + GOREAgreement + Resolution + BudgetaryCommitment | isExecutedVia, approvesAct, triggeredBy, confers |
| F5 | Rendition + GOREAgreement + IPR | rendersFor, requiresAccountability |

## Cardinalidades

| Relación | Cardinalidad | Nota |
|----------|:------------:|------|
| IPR → GOREAgreement | 0..N | Una IPR puede tener múltiples convenios (cuotas, mandatos parciales) |
| GOREAgreement → Resolution | 1..1 | Todo convenio tiene exactamente 1 Resolución Aprobatoria |
| IPR → BudgetaryCommitment | 1..N | Una IPR puede tener múltiples CDPs (por año, por línea) |
| GOREAgreement → Rendition | 1..N | Un convenio puede tener múltiples rendiciones (parciales) |
| Resolution → ApprovalFlowStage | 1..1 | Una resolución está en exactamente 1 etapa |

[impl: `core.budget_commitment.ipr_id` FK, `core.budget_commitment.agreement_id` FK (ambos opcionales). `core.rendition` → `core.agreement` vía convenio. CLAUDE.md §Rule 28]

## IPR como objeto terminal

IPR es el pullback del dominio — 13 entidades tienen morfismos entrantes hacia ella. Cada morfismo se materializa como una tab en la UI de detalle IPR (`tab-*.tsx`).

```
                OperationalCommitment ──ipr_id──→ IPR
                IprProblem ──ipr_id──→ IPR
                Alert ──subject_id (polymorphic)──→ IPR
                ProgressReport ──ipr_id──→ IPR
                IprParty ──ipr_id──→ IPR (junction M:N con Organization)
                IprTerritory ──ipr_id──→ IPR (junction M:N con Territory)
                IprMilestone ──ipr_id──→ IPR
                EvaluationAssignment ──ipr_id──→ IPR
                KinshipDeclaration ──ipr_id──→ IPR
                AdmissibilityCheck ──ipr_id──→ IPR
                BudgetCommitment ──ipr_id──→ IPR (opcional)
                GOREAgreement ──isGovernedBy──→ IPR
                Rendition ──ipr_id──→ IPR (opcional)
```

### Morfismos directos en IPR

| Propiedad | Rango | Cardinalidad | Función |
|-----------|-------|:------------:|---------|
| `sponsor_division_id` | Organization (División) | 1..1 | División patrocinadora. Determina filtrado JEFE_DIVISION |
| `assignee_id` | User | 0..1 | ENCARGADO asignado. Determina filtrado ENCARGADO |
| `executor_id` | Organization | 0..1 | Entidad ejecutora. Usado en FRIL fraccionamiento |
| `mechanism_id` | ref.category (financing_mechanism) | 1..1 | Mecanismo de financiamiento → determina track gates |
| `funding_source_id` | ref.category (funding_source) | 1..1 | Fuente (FNDR, FRPD, etc.) → Glosa 03 prohibition |
| `status_id` | ref.category (ipr_status) | 1..1 | Estado fino (28 estados) |
| `mcd_phase_id` | ref.category (ipr_phase) | 1..1 | Fase MCD (F0-F5) |

Fibración `STATUS_PHASE_FIBER`: cada status mapea a exactamente una phase. El par (status, phase) es consistente por invariante.

[impl: `core.ipr` con FKs. 13 tabs en detalle IPR: Compromisos, Problemas, Alertas, Convenios, CDPs, Avances, Partes, Territorio, Hitos, Resoluciones, Evaluación, Parentesco, Admisibilidad. CLAUDE.md §Rule 49]

## Alert — coproducto polimórfico

Alert tiene un morfismo `hasSubject` con rango variable (coproducto):

```
Alert.subject_type ∈ {core.ipr, core.operational_commitment,
                       core.ipr_problem, core.agreement, core.organization}
```

| Campo | Función |
|-------|---------|
| `subject_type` | Discriminador fully-qualified (`core.` prefix obligatorio) |
| `subject_id` | UUID del objeto referenciado |
| `severity_id` | CRITICO / ALTO / ATENCION / INFO |
| `alert_type_id` | SEC / THR / EXP / CMP / OPS / REP |

Navegación: `AlertCard.onViewSubject` resuelve `subject_type` → ruta UI apropiada.

**Reconciliación:** La ontología modela esto via `gnub:triggersAlert` (Event → Alert) y `gnub:hasSeverity` / `gnub:hasAlertType`. GORE_OS invierte la dirección: Alert apunta al subject (no el event a la alert). La inversión es una decisión de implementación (FK en Alert, no en cada subject).

[impl: `core.alert`. subject_type siempre con prefijo `core.`. CLAUDE.md §Rule 3]

## Cadena de gobernanza CORE

Path más largo del dominio — conecta democracia representativa con decisión de inversión:

```
Committee ──hasSession──→ Session ──hasAgreement──→ SessionAgreement
    |                        |                           |
    |                   hasMinute (1:1)             linksToIPR (F3→F4 gate)
    |                        ↓                           |
    |                     Minute                    hasVote (1:N)
    |                                                    ↓
    |                                              SessionVote
    |                                              castBy → User (CONSEJERO_REGIONAL)
    |                                              voteOption → A_FAVOR/EN_CONTRA/ABSTENCION
    |
    2 instancias: CONSEJO-REGIONAL (quórum 9/16, 11/16)
                  COMITE-CRISIS (auto-creado)
```

### Path equation PE-6: Aprobación CORE

`approve_IPR = linksToIPR ∘ hasAgreement ∘ hasSession`

La aprobación CORE de una IPR es un acuerdo de sesión vinculado al IPR. Solo aplica a IPRs > 7.000 UTM (gate F3→F4).

### Quórum como restricción categórica

| Tipo | Fórmula | Uso |
|------|---------|-----|
| Simple | 9/16 consejeros | Aprobaciones estándar |
| Calificado | 11/16 consejeros | Materias especiales (ERD, PROT) |

El quórum es un **equalizer**: filtra sesiones donde `count(votos_favor) ≥ threshold`.

[impl: `core.committee` + `core.session` + `core.session_agreement` + `core.session_vote`. Gate `_check_core_approval()`. CLAUDE.md §Rules 22, 31]

## Budget mediator chain

El presupuesto conecta estructura organizacional con inversión vía una cadena de 3 objetos:

```
Organization (División)
    ↑ ownedBy (N:1)
BudgetProgram ──classifiedBy──→ {Subtitle, Item, Allocation, ProgramType, ProgramCode, FundingSource}
    ↑ belongsToProgram (N:1)
BudgetCommitment (CDP)
    ├── linkedToIPR (N:1, opcional) ──→ IPR
    └── linkedToAgreement (N:1, opcional) ──→ GOREAgreement
```

### Path equation PE-7: Validación CDP

`amount(CDP) ≤ current_amount(BudgetProgram) - committed_amount(BudgetProgram)`

El CDP es válido solo si el monto no excede el saldo disponible del programa presupuestario. Advisory lock `pg_advisory_xact_lock` serializa emisiones concurrentes.

### Cadena de ejecución por programa

Cada BudgetProgram tiene 5 aspectos de magnitud que forman un orden parcial:

`initial ≤ current` (post-modificaciones)
`committed ≤ current` (CDPs no pueden exceder vigente)
`accrued ≤ committed` (no se devenga sin compromiso previo)
`paid ≤ accrued` (no se paga sin devengo previo)

### Carryover como morfismo temporal

`BudgetCarryover: BudgetProgram(año T) → BudgetProgram(año T+1)`

Arrastre = saldo no ejecutado que se incorpora al siguiente año fiscal vía SIC (Saldo Inicial de Caja).

[impl: `core.budget_program` (25.761), `core.budget_commitment` (4.617), `core.budget_carryover` (13.378). `POST /api/presupuesto/{id}/cdps`. CLAUDE.md §Rules 25, 28]

## DGI cartera — colímite computado

La señal de salud de cada IPR en la cartera DGI es un colímite de 5 observaciones cruzadas:

```
health_signal = _compute_health_signal(
    cuotas_vencidas:     Agreement.installments WHERE due_date < NOW()
    alertas_criticas:    Alert WHERE subject_type='core.ipr' AND severity=CRITICO
    brecha_avance:       IPR.physical_progress - IPR.planned_progress
    staleness:           NOW() - MAX(ProgressReport.created_at)
    compromisos_vencidos: OperationalCommitment WHERE status=PENDIENTE AND due_date < NOW()
)
```

| Señal | Condición |
|-------|-----------|
| ROJO | Cualquier componente en estado crítico |
| AMARILLO | Al menos un componente requiere atención |
| VERDE | Todos los componentes normales |

Es la única relación en el dominio que agrega datos de 5 entidades distintas en un solo valor. Cockpit drill-down: `/cartera?health_signal=ROJO`.

[impl: `dgi_cartera.py`. `_compute_health_signal()`. 3 endpoints: cartera, resumen, cuotas-vencidas. CLAUDE.md §DGI Layer]

## User → Role → Population fibración

El par (role, division) determina completamente el contexto operativo de un usuario:

```
User ──hasRole──→ SystemRole (ref.category, 13 roles)
  |                    |
  |               determines → Population {operativa, dgi}
  |                    |
  └──belongsTo──→ Organization (División)
                       |
                  determines → sidebar, dashboard, filtrado
```

### Fibración por population

| Population | Roles | Sidebar | Dashboard |
|-----------|-------|---------|-----------|
| operativa | ADMIN_SISTEMA, ADMIN_REGIONAL, JEFE_DIVISION, ENCARGADO, GOBERNADOR, SECRETARIO_EJECUTIVO, CONSEJERO_REGIONAL, JEFE_DEPARTAMENTO, JEFE_UNIDAD | 10 ítems operativos + role-specific | dashboard + ejecutivo / mi-división / mis-compromisos |
| dgi | JEFE_DGI, ESP_CONTROL_GESTION, ESP_PROCESOS, ESP_TD | 7 ítems DGI | cockpit DGI |

### Path equation PE-8: Routing determinístico

`sidebar(user) = population(role(user))`
`dashboard(user) = population(role(user)) × role_level(role(user))`

El routing es un funtor `F: User → UIContext` completamente determinado por el role. No hay ambigüedad.

[impl: `lib/auth.tsx` → `useAuth()`. `User.population` drives routing. `components/sidebar.tsx` → `operationalNav` vs `dgiNav`. CLAUDE.md §Rules 11, 23]
