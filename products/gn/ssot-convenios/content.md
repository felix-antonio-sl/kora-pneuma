---
urn: urn:gn:kb:ssot-convenios
nombre: ssot-convenios
version: 1.2.0
estado: borrador
descripcion: "Documento SSOT GORE Ñuble migrado como conocimiento borrador; su estado no implica validación institucional."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-ssot/ssot-convenios.md (sha256:f9dba0526542e0bc1d2647de6074eeb39e8c183097fe755171f87ca16308ca6a); cuerpo preservado íntegramente durante la migración KORA del 2026-08-02."
autor: FS
creado: 2026-03-10
lang: es
tags: [ssot, convenios, acuerdos, estados, cuotas, transferencias]
familia: bok
---

# SSOT — Convenios GORE Ñuble

## Resumen

6 tipos de convenio, 7 estados canónicos ontológicos + 6 refinamientos GORE_OS (13 total). Cuotas e instalments inline. Art. 18: verificación de rendiciones antes de nuevas transferencias.

## Tipos de convenio (6)

| Código | Tipo |
|--------|------|
| TRANS | Convenio de Transferencia |
| MAND | Convenio Mandato |
| PROG | Convenio de Programación |
| MARCO | Convenio Marco |
| COLAB | Convenio de Colaboración |
| INTER | Convenio Interinstitucional |

Consistente entre ReferenceData.ttl y GORE_OS `agreement_type` scheme (6 valores).

## Estados de convenio

### Estados ontológicos (7)

| Seq | Estado | Descripción |
|-----|--------|-------------|
| 1 | Borrador | Elaboración inicial por división técnica |
| 2 | En Revisión Jurídica | Asesoría Jurídica verifica legalidad |
| 3 | En Revisión Financiera | DAF verifica cláusulas financieras |
| 4 | Visado Internamente | Aprobación interna completa |
| 5 | Firmado | Firma bilateral (GORE + contraparte) |
| 6 | Toma de Razón Pendiente | En trámite CGR |
| 7 | Formalizado (Tramitado) | Toma de Razón obtenida, vigente |

**Reconciliación:** ApprovalData.ttl: 7 estados secuenciados (agrega En Revisión Jurídica y En Revisión Financiera). ReferenceData.ttl: 5 estados (Draft, Reviewed, Signed, TdR, Formalized) — menos granular. Canónico: 7 per ApprovalData (mayor granularidad del flujo interno).

Doble declaración ABox: 12 instancias `gnub:AgreementState` totales (7 en ApprovalData + 5 en ReferenceData) sin `owl:sameAs`. Mismo patrón que RenditionState/AccountabilityState. Pendiente: consolidar en ontología.

### Extensiones GORE_OS

GORE_OS implementa 13 estados totales. Extensiones respecto a los 7 ontológicos:

| Estado | Tipo | Descripción |
|--------|------|-------------|
| EN_NEGOCIACION | Nuevo | Entre Borrador y Revisión Jurídica |
| FIRMADO_GORE | Split de Firmado | Firma unilateral GORE |
| FIRMADO_CONTRAPARTE | Split de Firmado | Firma contraparte (antes de TdR) |
| VIGENTE | Nuevo | Post-formalización, durante período de vigencia |
| VENCIDO | Nuevo | Plazo cumplido sin renovación |
| TERMINADO | Nuevo | Cumplimiento total |
| RESCILIADO | Nuevo | Término anticipado por acuerdo de partes |

TDR_PENDIENTE es alias de implementación para el estado ontológico "Toma de Razón Pendiente" (seq 6) — no es un estado nuevo.

Aritmética: 7 ontológicos - 1 reemplazado (Firmado) + 2 splits + 5 nuevos = 13. [impl: `agreement_state` scheme, FSM en `convenios.py`. CLAUDE.md §Rule 5]

## Cuotas (installments)

Per convenio de transferencia. Inline CRUD en drawer.

- `POST /api/convenios/{id}/cuotas` — requiere `installment_number`, `amount`, `due_date`, `payment_status_id`
- `POST /api/convenios/{id}/cuotas/bulk` — `BulkCuotaRequest(total_amount, num_installments, start_date, frequency_months=1)`

[impl: CLAUDE.md §Rules 26-27]

## Verificación Art. 18

Antes de transferir nueva cuota: verificar que la entidad ejecutora no tenga rendiciones pendientes.

[ver rendiciones](urn:gn:kb:ssot-rendiciones)

## Flujo convenio de transferencia

**Fase elaboración**: División técnica elabora borrador → Asesoría Jurídica controla legalidad → DAF revisa cláusulas de rendición

**Fase firma**: DAF presenta a Gobernador/a → Firma bilateral (GORE + representante legal contraparte)

**Fase formalización**: Gobernador/a emite Resolución Aprobatoria → Envía a CGR → Toma de Razón → Transferencia habilitada
