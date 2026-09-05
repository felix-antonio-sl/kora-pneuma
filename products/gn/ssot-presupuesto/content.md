---
urn: urn:gn:kb:ssot-presupuesto
nombre: ssot-presupuesto
version: 1.4.1
estado: borrador
descripcion: "Documento SSOT GORE Ñuble migrado como conocimiento borrador; su estado no implica validación institucional."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-ssot/ssot-presupuesto.md (sha256:0aee347c54ebe3faca7d891b50e67c4b3bc0c6ed9e00aeb91b4fe0b5f7746167); cuerpo preservado íntegramente durante la migración KORA del 2026-08-02."
autor: FS
creado: 2026-03-10
lang: es
tags: [ssot, presupuesto, clasificador, subtitulos, umbrales, ciclo]
familia: bok
---

# SSOT — Presupuesto GORE Ñuble

## Resumen

Clasificador presupuestario de 6 niveles, 6 subtítulos operativos, umbrales financieros, ciclo presupuestario. Partida 31 → Capítulo 01 → Programa 19 (GORE Ñuble). Fuente autoritativa: LegalData.ttl + Ley de Presupuestos 2026.

## Clasificador presupuestario (6 niveles)

| Nivel | Tipo | Ejemplo |
|-------|------|---------|
| 1 | Partida | 31 — Gobiernos Regionales |
| 2 | Capítulo | 01 |
| 3 | Programa | 19 — GORE Ñuble |
| 4 | Subtítulo | 31 — Iniciativas de Inversión |
| 5 | Ítem | 03 — Programas de Inversión |
| 6 | Asignación | Específica por proyecto/programa |

[impl: GORE_OS 6-level classifier completo. `budget_item`(14), `budget_allocation`(15), `program_type`(5). Admin CRUD `budget_program_code`. CLAUDE.md §Rule 37]

## Subtítulos operativos (6)

| Subtítulo | Nombre | Uso principal | División |
|-----------|--------|---------------|----------|
| 21 | Gastos en Personal | Remuneraciones planta/contrata | DAF |
| 22 | Bienes y Servicios de Consumo | Gastos operativos | DAF |
| 24 | Transferencias Corrientes | Programas G06, 8% FNDR, transferencias | DIPIR |
| 29 | Adquisición Activos No Financieros | Compra activos propios | DAF |
| 31 | Iniciativas de Inversión | Ejecución directa: proyectos propios | DIPIR |
| 33 | Transferencias de Capital | Ejecución indirecta: transferencias a municipios/FRIL | DIPIR |

**Reconciliación:** 6 subtítulos consistentes entre IPRData.ttl (S21, S22, S24, S29, S31, S33) y Omega. GORE_OS `budget_subtitle` scheme tiene 8 — incluye subtítulos adicionales de implementación.

## Ejecución presupuestaria

Cadena de ejecución per programa:

Inicial → Vigente → Comprometido → Devengado → Pagado

[impl: `core.budget_program` (25.761 registros). Campos: `initial_amount`, `current_amount`, `committed_amount`, `accrued_amount`, `paid_amount`. CLAUDE.md §Rule 28]

## Umbrales financieros

| Concepto | Umbral | Fuente |
|----------|--------|--------|
| Exención RS (FRIL Ñuble) | < 4.545 UTM | Glosa 12 |
| Licitación pública (obras) | > 1.000 UTM | Art. 6 Ley 2026 |
| Licitación pública (estudios/servicios) | > 500 UTM | Art. 6 Ley 2026 |
| Toma de Razón CGR | > 2.500 UTM | Res. 7/2019 CGR |
| Aprobación CORE | > 7.000 UTM | GORE_OS parametric |
| Evaluación SNI obligatoria | > 15.000 UTM | Omega |
| Trato directo (monto ínfimo) | < 10 UTM | Omega |

**Reconciliación:** DipirRules.ttl modela exención Toma de Razón con umbral 5.000 UTM (ejemplo genérico) con operador "menor que". Omega especifica 2.500 UTM para GORE Ñuble. Canónico: 2.500 UTM per Omega (regional) + GORE_OS.

Operador: `<` (menor que) per DipirRules.ttl. Omega es inconsistente internamente (usa "<=" en tabla y "<" en árbol de decisión). Canónico: `<` per ontología.

[impl: `core.financial_threshold` (10 filas: 4 UTM + 5 glosa% + UTM_VALUE). `_get_utm_value()`, `_check_utm_threshold()`. CLAUDE.md §Rules 34-35]

## Ciclo presupuestario

| Período | Fase |
|---------|------|
| T-1 (Jul-Dic) | Formulación |
| T (Ene-Dic) | Ejecución (4 trimestres) |
| T+1 (Ene-Jun) | Rendición y auditoría |

Fases del ciclo:

Formulación → Aprobación → Ejecución → Modificaciones → Control → Cierre

[impl: `core.budget_cycle_milestone` (17 seed) + `core.budget_cycle_tracking`. 5 endpoints `/presupuesto/ciclo/*`. CLAUDE.md §Rule 43]

### Hitos trimestrales del ciclo

| Período | Mes | Hito |
|---------|-----|------|
| T-1 | Jul-Ago | Instrucciones DIPRES |
| T-1 | Sep | Gobernador/a presenta a CORE |
| T-1 | Oct-Nov | CORE analiza y aprueba |
| T-1 | Dic | Ley de Presupuestos promulgada |
| T Q1 | Ene | Decreto inicial |
| T Q1 | Feb-Mar | Primera distribución FNDR |
| T Q2 | Abr | Informe trimestral CORE |
| T Q2 | May-Jun | Evaluación primer semestre |
| T Q3 | Jul | Informe semestral |
| T Q3 | Ago | Solicitud modificaciones |
| T Q3 | Sep | CORE aprueba ajustes |
| T Q4 | Oct | Aceleración ejecución |
| T Q4 | Nov | Última distribución |
| T Q4 | Dic | Cierre ejercicio |
| T+1 | Ene-Mar | Rendición de cuentas |
| T+1 | Abr | Cuenta Pública Gobernador/a |
| T+1 | May-Jun | Auditoría CGR |

### Definiciones de fases del ciclo

| Fase | Definición |
|------|-----------|
| Formulación Presupuestaria | Elaboración del proyecto de presupuesto (ARI, PROPIR, coordinación DAF-DIPIR) |
| Aprobación y Distribución | Aprobación CORE, envío DIPRES, Toma de Razón CGR |
| Ejecución Presupuestaria | Programación de caja, compromisos, devengos, pagos en SIGFE |
| Modificaciones | Suplementos, reasignaciones, incorporación SIC, transferencias consolidables |
| Control y Seguimiento | Control interno, CGR, seguimiento DIPRES, transparencia |
| Cierre Presupuestario | Deuda flotante, SIC, cierre SIGFE/BIP, evaluación |

Fuente: IPRData.ttl, 6 instancias `gnub:BudgetCyclePhase`.

### Asignaciones presupuestarias 2026

| Fondo | Monto (M$CLP) |
|-------|---------------|
| FNDR Ñuble | 41.562.476 |
| FRPD Ñuble | 12.829.611 |
| Total región | 85.752.331 |

Fuente: IPRData.ttl, magnitudes `BudgetedAmountAspect`.

Total incluye ISAR, FATC, FIC y otras fuentes no desglosadas individualmente.

## Unidades de medida (4)

| Unidad | Símbolo | Uso |
|--------|---------|-----|
| Porcentaje | % | Avance físico, glosa caps |
| UTM (Unidad Tributaria Mensual) | UTM | Umbrales legales, exenciones |
| Peso chileno | CLP / M$ | Montos presupuestarios (M$ = miles) |
| Mes | mes | Plazos de ejecución |

Fuente: OrgData.ttl, 4 instancias `gist:UnitOfMeasure`. M$ (ThousandsCLP) tiene `conversionFactor: 1000`.

## Modificaciones presupuestarias

Aumentos ≤ 10% del costo aprobado NO requieren nueva aprobación CORE (Glosa 10/11).

Traspaso permitido entre subtítulos de inversión, excepto hacia S22 (IPRData.ttl, Glosa 04).


## Cadena transaccional presupuestaria

5 eventos secuenciales modelados en ontología (subclases de `gnub:BudgetaryTransaction` → `gist:Event`):

| Seq | Evento | Clase ontológica | Descripción |
|-----|--------|-----------------|-------------|
| 1 | Pre-Compromiso (CDP) | `PreCommitmentEvent` | Emisión de CDP que reserva saldo presupuestario |
| 2 | Compromiso | `CommitmentEvent` | Acto administrativo (OC, Contrato) que reserva recursos definitivamente |
| 3 | Devengo | `AccrualEvent` | Recepción conforme que genera obligación de pago y pasivo contable |
| 4 | Pago | `PaymentEvent` | Egreso efectivo (TEF/Cheque) que extingue la obligación |
| 5 | Modificación | `BudgetModificationEvent` | Reasignación, suplemento o transferencia de recursos |

Relación: cada transacción `affectsAccount` → `gnub:BudgetaryAccount`.

`gnub:BudgetaryCommitment` (subClass `gist:Commitment`) es la obligación sostenida (distinta del evento). Un `PreCommitmentEvent` confiere un `BudgetaryCommitment` con `hasGiver`=GORE, `hasGetter`=receptor, `hasMagnitude`=monto.

[impl: GORE_OS implementa solo PreCommitment (CDP) completamente. `core.budget_commitment` (4.617 filas). `POST /api/presupuesto/{id}/cdps` — advisory-locked `CDP-{year}-{seq:04d}`. Valida `amount ≤ current - committed`. Auto EMITIDO. CLAUDE.md §Rule 28]

## Aspectos de magnitud presupuestaria (7)

Patrón ontológico `gist:Aspect` para tracking de ejecución:

| Aspecto | Clase | Estado |
|---------|-------|--------|
| Presupuestado inicial | `BudgetedAmountAspect` | Activo |
| Vigente (post-modificaciones) | `CurrentBudgetAspect` | Activo |
| Pre-afectado (CDPs emitidos) | `PreCommittedAmountAspect` | Activo |
| Comprometido (OC, contratos) | `CommittedAmountAspect` | Activo |
| Devengado (obligación exigible) | `AccruedAmountAspect` | Activo |
| Pagado (egreso efectivo) | `PaidAmountAspect` | Activo |
| Disponible (vigente - comprometido) | `AvailableBalanceAspect` | Activo |

`ExecutedAmountAspect` — DEPRECATED, usar `AccruedAmountAspect`.

**Reconciliación:** GORE_OS materializa 5 de 7 aspectos como campos directos en `core.budget_program` (`initial_amount`, `current_amount`, `committed_amount`, `accrued_amount`, `paid_amount`). Pre-afectado y Disponible se calculan en runtime. La ontología modela todos como aspectos de magnitud sobre `BudgetaryAccount`.

## Tipos de modificación presupuestaria (7)

| Tipo | Afecta Partida 31 | Acto requerido | Excepción CORE |
|------|-------------------|----------------|----------------|
| Reasignación interna | No | Resolución GORE | — |
| Creación iniciativas FRPD | No | Resolución GORE | — |
| Suplementación presupuestaria | Sí | Decreto Supremo + Resolución | — |
| Transferencia otros organismos | Sí | Decreto Supremo + Resolución | — |
| Emergencias 3% SUBINT | Sí | Decreto Supremo + Resolución | Traspasable a Subsecretaría Interior |
| Emergencias 2% GORE | Sí | Resolución GORE | Uso interno GORE |
| Aumento ≤10% costo aprobado | No | Resolución GORE | Glosa 10/11: no requiere nueva aprobación CORE |

Fuente: Omega v2.6.0. Flujo: DIPIR prepara → DAF revisa → Gobernador/a presenta → CORE aprueba → DIPRES visa → CGR TdR → vigencia (ajuste SIGFE).

**Reconciliación:** La ontología define dos clases para modificaciones — `BudgetModificationEvent` (subClass `BudgetaryTransaction`) y `BudgetModification` (subClass `gist:Event`) — con jerarquías incompatibles. Pendiente: deprecar una. Los 7 tipos provienen del Omega; no están enumerados como instancias en ningún TTL.

## Arrastre presupuestario

Recursos remanentes del año anterior:
- **SIC** (Saldo Inicial de Caja): requiere incorporación formal mediante resolución
- **Deuda flotante**: obligaciones devengadas no pagadas al 31/12

Sin clase ontológica. GORE_OS: `core.budget_carryover` (13.378 filas).

**Reconciliación:** Gap ontológico. La ontología no modela arrastre ni SIC. El Omega los define en glosario pero sin modelo formal.

## Esquemas financieros GORE_OS

| Scheme | Instancias | Descripción |
|--------|-----------|-------------|
| `budget_commitment_status` | 5 | Estados CDP (incluye EMITIDO) |
| `payment_status` | 5 | Estados de pago |
| `cgr_outcome` | 7 | Resultados Toma de Razón CGR |

Sin respaldo ontológico — constructos de implementación.

[ver glosas detalladas](urn:gn:kb:ssot-legal)
