---
urn: urn:gn:kb:ssot-rendiciones
nombre: ssot-rendiciones
version: 1.2.1
estado: borrador
descripcion: "Documento SSOT GORE Ñuble migrado como conocimiento borrador; su estado no implica validación institucional."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-ssot/ssot-rendiciones.md (sha256:337dc033ef41849242553705e84722e0e349d24cf89c12cff555c26945eeacb5); cuerpo preservado íntegramente durante la migración KORA del 2026-08-02."
autor: FS
creado: 2026-03-10
lang: es
tags: [ssot, rendiciones, sisrec, cgr, sla, estados]
familia: bok
---

# SSOT — Rendiciones SISREC

## Resumen

Sistema de rendición de cuentas. 6 estados canónicos ontológicos, 5 roles SISREC, SLAs definidos en implementación. 8-phase CGR en GORE_OS. Flujo: Ejecutor presenta → RTF revisa → Jefe DAF visa → UCR contabiliza.

## Estados canónicos (6)

| Seq | Estado | Descripción |
|-----|--------|-------------|
| 1 | Pendiente | No presentada por entidad ejecutora |
| 2 | En Revisión | Recibida, en revisión por RTF/Analista Otorgante |
| 3 | Observada | Devuelta para subsanación |
| 4 | Aprobada Parcialmente | Aprobada con transacciones observadas |
| 5 | Aprobada Totalmente | Aprobada en totalidad, firmada con FEA |
| 6 | Contabilizada | Registrada en SIGFE, archivada por UCR/DAF |

**Reconciliación:** Canónico: RenditionData.ttl (6 estados `gnub:RenditionState`), más granular.

Descartado: ReferenceData.ttl (5 `gnub:AccountabilityState`: Pending, InReview, Observed, Approved, Rejected). Clases `RenditionState` y `AccountabilityState` duplicadas en TBox (`goreNubleOntology.ttl`) misma superclase (`gist:Category`) pero dominios distintos (`Rendition` vs `AccountabilityProcess`) sin `owl:equivalentClass`. Pendiente: deprecar `AccountabilityState` en ontología.

Diferencias clave: RenditionData distingue Aprobada Parcial vs Total (la realidad CGR). ReferenceData solo tiene "Approved" genérico y agrega "Rejected" que RenditionData no incluye.

### Refinamientos GORE_OS (2 adicionales)

GORE_OS implementa 8 estados:

| Estado GORE_OS | Mapeo ontológico |
|----------------|-----------------|
| PENDIENTE | Pendiente |
| EN_REVISION_RTF | En Revisión (split fase RTF) |
| VISADA_RTF | — (estado intermedio GORE_OS) |
| EN_REVISION_UCR | — (estado intermedio GORE_OS) |
| OBSERVADA | Observada |
| APROBADA | Aprobada Totalmente |
| RECHAZADA | — (de ReferenceData, no en RenditionData) |
| Archivada | Contabilizada (vía `archived_at`) |

GORE_OS granulariza "En Revisión" en 3 fases (RTF → VISADA_RTF → UCR) y agrega RECHAZADA. "Aprobada Parcialmente" (estado ontológico 4) no tiene mapeo directo — GORE_OS subsume aprobación parcial y total bajo APROBADA. La ontología no distingue estas subfases.

## Roles SISREC (5)

| Rol | Entidad | Función |
|-----|---------|---------|
| Analista Ejecutor | Ejecutora | Crea y registra transacciones en SISREC |
| Ministro de Fe | Ejecutora | Certifica autenticidad de documentos digitalizados |
| Encargado Ejecutor | Ejecutora | Representante legal, firma con FEA, envía al GORE |
| Analista Otorgante (RTF) | GORE | Referente Técnico-Financiero, revisa/aprueba/observa |
| Encargado Otorgante (Jefe DAF) | GORE | Jefatura DAF, firma Informe de Aprobación con FEA |

## SLAs

Definidos en GORE_OS (no en ontología).

| Etapa | Plazo | Responsable |
|-------|-------|-------------|
| Presentación rendición | 15 del mes siguiente | Entidad Ejecutora |
| Revisión técnica (RTF) | 7 días hábiles | Analista Otorgante |
| Devolución por observación | 1 día | Jefe DAF |
| Contabilización | 2 días | UCR/DAF |
| Resubsanación (OBSERVADA) | 15 días | Entidad Ejecutora |

Meta CGR: 14 días totales.

[impl: SLAs en `ipr.py`. `phase_entered_at` para cálculo SLA-accurate. `core.rendition_phase` (8 seed). Escalation: `core.rendition_escalation` (3 niveles: 1x, 1.5x, 2x SLA). CLAUDE.md §Rule 44]

## Normas aplicables

- Art. 18 Res. 30 CGR: no transferir nuevos fondos si rendiciones pendientes
- Art. 31 Res. 30 CGR: obligación de restitución
- Res. Ex. 1858/2023 CGR: SISREC obligatorio para Subtítulos 24 y 33

## Rendición por fondo

| Fondo | Plataforma | Requisito especial | Documentos clave |
|-------|-----------|-------------------|-----------------|
| FNDR S.31 | BIP + SISREC | Estado de pago ITO | Certificado recepción provisoria/definitiva |
| FNDR S.33 | BIP + SISREC | Convenio vigente | Informe avance + comprobantes |
| FRIL | BIP + SISREC | Convenio transferencia | Estado de pago municipal |
| FRPD CTCI | SISREC | Acreditación hitos I+D+i | Informes técnicos ANID/CORFO |
| Subvención 8% | SISREC (≤500 UTM: papel) | Pagaré notarial vigente | Rendición detallada por ítem |
| Glosa 06 Directa | SISREC | Informe evaluación SES | Rendición mensual ejecución |
| C33 Conservación | SISREC | Certificación estado actual | Informe técnico conservación |

## Documentación auténtica

4 tipos válidos para SISREC: Papel original, Copia autenticada, Electrónico (Ley 19.799), Digitalizado con certificación Ministro de Fe.

## Principios rectores rendición

Legalidad, Veracidad-Fidelidad, Acreditación, Exactitud, Oportunidad, Transparencia, Eficiencia-Eficacia, Probidad.

## Responsabilidades por incumplimiento

| Tipo | Consecuencia | Base legal |
|------|-------------|-----------|
| Administrativa | Censura, multa, suspensión, destitución | Ley 18.834 |
| Civil | Restitución fondos vía Juicio de Cuentas CGR | Ley 10.336 |
| Penal | Malversación, fraude al fisco | Código Penal |
