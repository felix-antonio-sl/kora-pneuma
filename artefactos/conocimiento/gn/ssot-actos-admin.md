---
urn: urn:gn:kb:ssot-actos-admin
nombre: ssot-actos-admin
version: 1.1.1
estado: borrador
descripcion: "Documento SSOT GORE Ñuble migrado como conocimiento borrador; su estado no implica validación institucional."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-ssot/ssot-actos-admin.md (sha256:d34a63b33b0d5a31af85c5fec1e5b3e3251b20ea5460c200ac655d46cf656a1f); cuerpo preservado íntegramente durante la migración KORA del 2026-08-02."
autor: FS
creado: 2026-03-10
lang: es
tags: [ssot, actos-administrativos, aprobacion, visacion, toma-razon, decretos]
familia: bok
---

# SSOT — Actos administrativos

## Resumen

3 tipos de acto administrativo, 8 etapas de aprobación canónicas, reglas de exención por umbral UTM. Flujo DIPIR modelado con 3 eventos ontológicos (Visación, Aprobación, Toma de Razón).

## Tipos de acto

| Tipo | Sujeto a TdR | Subtipos |
|------|--------------|----------|
| Decreto | Sí | — |
| Resolución | Depende del monto | Exenta, Afecta |
| Oficio | No | — |

GORE_OS agrega DECRETO_ALCALDICIO — gap ontológico, no presente en ningún TTL.

[impl: `core.administrative_act`. Tipos: DECRETO, RESOLUCION, DECRETO_ALCALDICIO. CLAUDE.md §Rule 13]

**Reconciliación:** ApprovalData.ttl define 3 subtipos (Resolución Exenta, Resolución Afecta, Oficio). Decreto proviene de ReferenceData.ttl (`_DocType_Decree`), no de ApprovalData. Ontología NO modela DECRETO_ALCALDICIO. GORE_OS lo implementa para actos de municipios en convenios de mandato. Pendiente: agregar a ontología.

ReferenceData.ttl define 9 `AdministrativeDocumentType`: Resolución (base) + 5 subtipos (Modificación, Rectificación, Rescisión, Revocación, Recurso Administrativo) + Decreto + Convenio + Informe. ApprovalData.ttl refina con Resolución Exenta/Afecta + Oficio. Canónico: taxonomía completa de ReferenceData + subtipos de ApprovalData.

## Etapas de aprobación (8)

| Seq | Etapa | Actor |
|-----|-------|-------|
| 1 | Elaboración (Borrador) | Unidad competente |
| 2 | V.B. Jurídico | Asesoría Jurídica |
| 3 | V.B. Control | Unidad de Control |
| 4 | V.B. Jefatura División | Jefe/a de División |
| 5 | V.B. Administrador/a Regional | Administrador/a Regional |
| 6 | Firma Gobernador/a (FEA) | Gobernador/a Regional |
| 7 | Toma de Razón CGR | Contraloría General |
| 8 | Notificación y Archivo | Oficina de Partes |

**Reconciliación:** Canónico: ApprovalData.ttl (8 etapas secuenciadas). Omega describe 7 pasos para Resolución Exenta (sin distinguir VB Jurídico / VB Control / VB Jefatura como etapas separadas). GORE_OS implementa 7-step FSM (BORRADOR→EN_REVISION→VISADO→FIRMADO→ENVIADO_CGR→OBSERVADO/TOMADO_RAZON + ANULADO cross-cutting) — agrupa V.B. Jurídico+Control+Jefatura+Administrador en "EN_REVISION→VISADO".

### Mapeo GORE_OS

| Ontología (8 etapas) | GORE_OS (7 steps) |
|----------------------|-------------------|
| 1. Elaboración | BORRADOR |
| 2-4. VB Jurídico + Control + Jefatura | EN_REVISION |
| 5. VB Administrador | VISADO |
| 6. Firma Gobernador | FIRMADO |
| 7. Toma de Razón CGR | ENVIADO_CGR → TOMADO_RAZON / OBSERVADO |
| 8. Notificación | (post-TOMADO_RAZON, no modelado como estado) |
| — | ANULADO (cross-cutting, cualquier punto) |

## Eventos DIPIR (ontología)

3 clases de evento en `goreNubleDipirOntology.ttl`:

| Evento | Superclase | Descripción |
|--------|-----------|-------------|
| VisaciónEvent | gist:Event | Actor valida documento antes de aprobación final |
| AprobacionEvent | gist:Event | Aprobación definitiva (firma/autorización). Típicamente Gobernador/a |
| TomaRazonEvent | gist:Event | Control de legalidad CGR. Solo Resoluciones Afectas y Decretos |

Propiedades: `dipir:approvesAct` (AprobacionEvent → AdministrativeAct), `dipir:visatesAct` (VisaciónEvent → AdministrativeAct). Ambas subproperties de `gist:affects`.

Gap ontológico: `TomaRazonEvent` carece de propiedad dedicada (no existe `tomaRazonAct`). Se vincula al acto vía `gist:affects` genérico, a diferencia de `approvesAct` y `visatesAct` que son específicos.

## Regla de exención Toma de Razón

| Parámetro | Valor |
|-----------|-------|
| Umbral | DipirRules.ttl usa 5.000 UTM (ejemplo genérico, varía por región/año) |
| Operador | Menor que (<) |
| Aplica a | Resoluciones |
| Base legal | Res. 7/2019 CGR |
| Vigencia | Desde 2019-03-26 |

Para GORE Ñuble, umbral operativo: 2.500 UTM (Omega).

[impl: Track enforcement via `_check_track_amount_gates()`. `cgr_res30_utm` en JSONB de `core.financing_track`. CLAUDE.md §Rule 34]

## Operadores de comparación (ontología)

5 instancias de `ComparisonOperator` en DipirRules.ttl: `<`, `<=`, `>`, `>=`, `=`. Usados en `ExemptionRule` (subClass `gist:Specification`) para definir condiciones de exención.
