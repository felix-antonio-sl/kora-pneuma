---
urn: urn:gn:kb:ssot-master
nombre: ssot-master
version: 1.5.0
estado: borrador
descripcion: "Documento SSOT GORE Ñuble migrado como conocimiento borrador; su estado no implica validación institucional."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-ssot/ssot-master.md (sha256:25dc9a067b39a6adcc8e4ebd239420d7e5892dfde6591baa45f2439e24ebc581); cuerpo preservado íntegramente durante la migración KORA del 2026-08-02."
autor: FS
creado: 2026-03-10
lang: es
tags: [ssot, gore-nuble, reconciliacion, fundamentos, indice]
familia: bok
---

# SSOT GORE Ñuble — Índice Maestro

## Resumen

Fuente de verdad reconciliada del dominio GORE Ñuble. Bundle de 15 artefactos KORA/MD (este master + 14 satélites). Reconcilia 4 capas documentales con jerarquía de autoridad fija. Consumidores: agentes KODA/RAG y diseño/implementación de GORE_OS.

## Jerarquía de autoridad

| Prioridad | Fuente | Naturaleza | Ubicación |
|-----------|--------|------------|-----------|
| 1 (máxima) | Organigrama GORE 2026 | Resolución exenta — acto administrativo legal | `staging/organigrama_gore_2026.md` |
| 2 | Ontología goreNubleBundle | Modelo formal OWL/SKOS (12 TTL) | `ontologies/onto_gorenuble/` |
| 3 | Omega Mermaid v2.6.0 | Modelo de referencia descriptivo | `domains/gn/01_fundamentos/intro/omega_gore_nuble_mermaid.md` |
| 4 (mínima) | CQs Master v1.0.1 | 472 preguntas de competencia | `ontologies/onto_gorenuble/goreNubleCQs_Master.yml` |

**Criterio de resolución**: ante conflicto entre fuentes, prevalece la de mayor prioridad. Las fuentes mantienen su ciclo de vida propio — este SSOT es una vista reconciliada, no un reemplazo.

## Mapa de artefactos

| URN | Título | Fuentes primarias | Status |
|-----|--------|-------------------|--------|
| `urn:gn:kb:ssot-organica` | Estructura orgánica | Organigrama > OrgData.ttl > Omega | draft |
| `urn:gn:kb:ssot-territorio` | Territorio | OrgData.ttl > Omega > CQs | draft |
| `urn:gn:kb:ssot-legal` | Marco normativo | LegalData.ttl > Omega | draft |
| `urn:gn:kb:ssot-ipr-lifecycle` | Ciclo de vida IPR | ReferenceData.ttl + IPRData.ttl > Omega > CQs | draft |
| `urn:gn:kb:ssot-presupuesto` | Presupuesto | LegalData.ttl > Omega > ReferenceData.ttl | draft |
| `urn:gn:kb:ssot-convenios` | Convenios | ApprovalData.ttl > ReferenceData.ttl > Omega | draft |
| `urn:gn:kb:ssot-rendiciones` | Rendiciones SISREC | RenditionData.ttl > ReferenceData.ttl > Omega | draft |
| `urn:gn:kb:ssot-actos-admin` | Actos administrativos | ApprovalData.ttl > DipirOntology.ttl > DipirRules.ttl | draft |
| `urn:gn:kb:ssot-operaciones` | Procesos operativos | Ontology.ttl + ReferenceData.ttl + GORE_OS | draft |
| `urn:gn:kb:ssot-mecanismos` | Reglas operativas por mecanismo | Omega v2.6.0 + IPRData.ttl + GORE_OS | draft |
| `urn:gn:kb:ssot-ecosistema` | Ecosistema institucional externo | Omega v2.6.0 + LOC GORE | draft |
| `urn:gn:kb:ssot-relaciones-dominio` | Relaciones de dominio (modelo categórico) | Ontology.ttl TBox + DipirOntology.ttl | draft |
| `urn:gn:kb:ssot-tde` | Transformación Digital del Estado | Ley 21.180 + Ley 19.799 + digital.gob.cl | draft |
| `urn:gn:kb:ssot-dgi` | DGI | OrgData.ttl (orgánica) + GORE_OS (funcional) | draft |

## Glosario de reconciliación

Términos donde las fuentes difieren. El valor canónico es el declarado aquí.

| Término | Canónico | Alternativas descartadas | Fuente autoritativa |
|---------|----------|--------------------------|---------------------|
| Sigla Div. Infraestructura | DIT | DIINF (URI convention, Omega) | OrgData.ttl `skos:altLabel`, GORE_OS |
| Nombre Div. Infraestructura | Infraestructura y Transportes (plural) | Infraestructura y Transporte (singular, Omega) | Organigrama, OrgData.ttl |
| Clasificación DGI | StaffUnit | Departamento (Organigrama) | OrgData.ttl (mayor granularidad tipológica) |
| RS (sigla evaluación) | Recomendación Satisfactoria | Rentabilidad Social (ReferenceData.ttl) | IPRData.ttl, CQs, uso institucional |
| F0 (nombre fase) | Postulación | Formulación e Ingreso (IPRData), Formulación & Ingreso (Omega) | ReferenceData.ttl (alineado con TBox) |
| F2 (nombre fase) | Evaluación | Evaluación Técnica (IPRData, Omega) | ReferenceData.ttl |
| F3 (nombre fase) | Priorización | Aprobación Presupuestaria (IPRData), Priorización & Asignación (Omega) | ReferenceData.ttl |
| FundingSource | Concepto categorial (Category) | — | Ontology.ttl TBox |
| FinancingMechanism | Concepto de catálogo (CatalogItem) | — | Ontology.ttl TBox (distinto de FundingSource) |
| RenditionState | 6 estados (RenditionData.ttl) | AccountabilityState 5 estados (ReferenceData.ttl) | RenditionData.ttl (más granular) |
| FRPD | Fondo Regional para la Productividad y el Desarrollo | "Fondo Regional Productividad y Desarrollo" (Omega, sin "para la") | Nombre legal completo |
| FRPD mecanismo | Unificado (1 mecanismo) | Split CTCI + Fomento (IPRData.ttl) | ReferenceData.ttl (split es detalle operativo bajo mecanismo único) |
| DIDESO vs DIDECO | DIDESO | DIDECO (GORE_OS test users) | Organigrama, OrgData.ttl, Omega |

## Conflictos transversales

### Doble declaración ABox

**Diagnóstico raíz**: `ReferenceData.ttl` y los archivos de dominio (`IPRData.ttl`, `RenditionData.ttl`, `ApprovalData.ttl`) declaran instancias del mismo tipo con URIs, cardinalidades y granularidades incompatibles. Un SPARQL `SELECT ?s WHERE { ?s a gnub:IPRPhase }` retorna 14 resultados (6+8) en vez de un set canónico.

**Afecta**: fases IPR (6 vs 8), estados rendición (5 vs 6), estados convenio (5 vs 7), fuentes financiamiento (8 vs 7), mecanismos financiamiento (7 vs 8), resultados evaluación (6 vs 10).

**Resolución SSOT**: cada satélite declara el set canónico. El set más granular prevalece cuando es consistente con la jerarquía de autoridad.

### Fases IPR: 6 vs 8

6 fases canónicas (F0-F5). [ver análisis completo](urn:gn:kb:ssot-ipr-lifecycle)

### Clases duplicadas en TBox

`BudgetModificationEvent` (subClass BudgetaryTransaction) y `BudgetModification` (subClass gist:Event) — mismo concepto, jerarquías incompatibles. `RenditionState` y `AccountabilityState` — misma superclase (`gist:Category`) pero dominios distintos (`Rendition` vs `AccountabilityProcess`). Sin `owl:equivalentClass`. Pendiente: deprecar `AccountabilityState` en ontología.

## Alineación GORE_OS

| Concepto canónico | Tabla/Entidad GORE_OS | Endpoint | Nota |
|-------------------|----------------------|----------|------|
| 6 divisiones | `core.organization` (org_type=DIVISION) | `GET /api/catalogs/divisions` | DIT es sigla canónica per OrgData.ttl `skos:altLabel` |
| 13 system roles | `ref.category` scheme `system_role` | — | 5 operativos + 4 DGI + 4 governance |
| 6 fases IPR (F0-F5) | `ref.category` scheme `ipr_phase` | — | IPRData F6/F7 no implementados |
| 7 financing tracks | `core.financing_track` | `GET /api/admin/financing-tracks` | Alineado con ReferenceData.ttl |
| 13 agreement states | `ref.category` scheme `agreement_state` | — | 7 ontológicos + 6 refinamiento GORE_OS |
| 8 rendition states | `ref.category` scheme `rendition_status` | — | 6 ontológicos + 2 refinamiento GORE_OS |
| 7 admin act steps | `core.administrative_act` FSM | `PATCH /api/actos/{id}/transition` | Ontología 8 etapas; GORE_OS 7 steps |
| 5 DGI dimensions | `ref.category` scheme `dgi_indicator_dimension` | `POST /api/dgi/data/indicators/refresh` | Solo en GORE_OS, no en Omega |
| 12 FRIL categories | `core.fril_category` | `GET /api/admin/financing-tracks` | Alineado con IPRData.ttl |
| 7 subv8 funds | `core.subv8_fund` | `GET /api/admin/financing-tracks` | Alineado con IPRData.ttl |
| 6 alert types + 5 severities | `ref.category` schemes | — | Ontología 5 severidades vs GORE_OS 4 |
| Compromisos operacionales | `core.operational_commitment` | `GET/POST /api/compromisos` | Sin clase ontológica |
| Problemas IPR | `core.ipr_problem` | `GET/POST /api/problemas` | Sin clase ontológica |
| 5 transacción presupuestaria | `core.budget_commitment` (CDP) | `POST /api/presupuesto/{id}/cdps` | Ontología 5 eventos; GORE_OS solo CDP |
| Arrastre presupuestario | `core.budget_carryover` | — | Sin clase ontológica (13K+ filas) |
