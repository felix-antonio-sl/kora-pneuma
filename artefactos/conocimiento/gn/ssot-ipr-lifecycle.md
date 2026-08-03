---
urn: urn:gn:kb:ssot-ipr-lifecycle
nombre: ssot-ipr-lifecycle
version: 1.2.1
estado: borrador
descripcion: "Documento SSOT GORE Ñuble migrado como conocimiento borrador; su estado no implica validación institucional."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-ssot/ssot-ipr-lifecycle.md (sha256:48f82fcc7c61f756d2666b1647a8c57bcb7def6928df31f5dc82fbf2755d2408); cuerpo preservado íntegramente durante la migración KORA del 2026-08-02."
autor: FS
creado: 2026-03-10
lang: es
tags: [ssot, ipr, ciclo-vida, fases, estados, tracks, evaluacion]
familia: bok
---

# SSOT — Ciclo de vida IPR

## Resumen

Modelo canónico de estados (MCD) de la Intervención Pública Regional. 6 fases (F0-F5), 28 estados (17 universales + 9 proyecto + 2 programa), 7 mecanismos de financiamiento, 7 tracks de evaluación. IPR es polimórfica: Proyecto, Programa de Inversión, Programa Operativo, Estudio Básico.

## Fases canónicas (6)

| Fase | Nombre canónico | Descripción |
|------|----------------|-------------|
| F0 | Postulación | Formulación e ingreso de la iniciativa |
| F1 | Admisibilidad | Verificación de requisitos formales |
| F2 | Evaluación | Evaluación técnica según track |
| F3 | Priorización | Aprobación presupuestaria y asignación CORE |
| F4 | Formalización | Convenio, decreto, ejecución |
| F5 | Cierre | Rendición final y cierre administrativo |

**Reconciliación:** Canónico: ReferenceData.ttl (6 fases F0-F5), alineado con TBox (skos:definition en goreNubleOntology.ttl:622) y Omega MCD.

Descartado: IPRData.ttl modela 8 fases (F0-F7) donde F5=Ejecución, F6=Modificaciones, F7=Cierre. Resolución: F6 y F7 son estados operativos dentro de F4/F5, no fases del ciclo de vida. La ejecución y las modificaciones ocurren durante F4 (Formalización); el cierre con rendición es F5.

Nombres canónicos: ReferenceData.ttl prevalece (Postulación, Evaluación, Priorización) sobre IPRData (Formulación e Ingreso, Evaluación Técnica, Aprobación Presupuestaria) y Omega (Formulación & Ingreso, Priorización & Asignación).

## Tipos IPR (4 subclases)

| Tipo | Subtítulo | Crea activo | Superclase |
|------|-----------|-------------|------------|
| IPRProject (Proyecto) | 31/33 | Sí | IPR |
| InvestmentProgram (Programa de Inversión) | 31 ítem 03 | Sí | IPR |
| OperationalProgram (Programa Operativo) | 24 | No | IPR |
| BasicStudy (Estudio Básico) | 22 | No | IPR |

Clases `owl:disjointWith` en TBox.

**Reconciliación:** Ontología define 4 subclases. Omega muestra solo 2 supertypes (PROYECTO capital, PROGRAMA corriente). InvestmentProgram y BasicStudy sin representación en Omega — gap documental del Omega, no del modelo. Canónico: 4 subclases per ontología.

La ontología define además `gnub:ANFAcquisition` como sub-subclase de `IPRProject` (adquisición de activos no financieros, Circular 33). No es subclase directa de IPR.

## Estados IPR (28)

### Estados universales (17)

| Seq | Estado | Fase |
|-----|--------|------|
| 1 | Pre-Admisible CDR | F1 |
| 2 | Para Revisión Técnica | F1 |
| 3 | Admisible | F1 |
| 4 | Inadmisible | F1 |
| 28 | Rechazado | F1 |
| 12 | Cartera Enviada a CORE | F3 |
| 13 | Certificado CORE OK | F3 |
| 14 | CDP Emitido | F3 |
| 15 | Decreto Tramitado | F4 |
| 16 | Convenio Formalizado | F4 |
| 17 | Tomado de Razón CGR | F4 |
| 20 | En Obra/Ejecución | F4 |
| 26 | Paralizado | F4 |
| 23 | Rendición Pendiente | F5 |
| 24 | Rendición Aprobada | F5 |
| 25 | IPR Cerrada | F5 |
| 27 | Terminado Anticipadamente | F5 |

### Estados proyecto (9)

| Seq | Estado | Fase |
|-----|--------|------|
| 5 | Enviado a MDSF | F2 |
| 6 | Recomendación Satisfactoria (RS) | F2 |
| 7 | Falta Información (FI) | F2 |
| 8 | Objetado Técnicamente (OT) | F2 |
| 11 | Admisibilidad Directa (AD) | F2 |
| 18 | En Licitación | F4 |
| 19 | Contrato Firmado | F4 |
| 21 | Recepción Provisoria | F4 |
| 22 | Recepción Definitiva | F5 |

### Estados programa (2)

| Seq | Estado | Fase |
|-----|--------|------|
| 9 | Recomendación Favorable (RF) | F2 |
| 10 | Informe Técnico Favorable (ITF) | F2 |

## Mecanismos de financiamiento (7)

| Mecanismo | Track | Fuente | Evaluador | Subtítulo |
|-----------|-------|--------|-----------|-----------|
| SNI General | A | FNDR | MDSF | S31 |
| FRIL | C | FNDR | GORE (DIPIR) | S33 |
| Circular 33 | B | — | MDSF/GORE | S31 |
| Glosa 06 (Ejecución Directa) | D1 | — | DIPRES/SES | S24 |
| Transferencia PPR | D2 | — | GORE (Comité/DAE) | S24 |
| Subvención 8% | E1 | FNDR | GORE (Comisión Evaluadora) | S24 |
| FRPD | E2 | FRPD | ANID/CORFO/GORE | S31/S33 |

**Reconciliación:** ReferenceData.ttl modela 7 mecanismos (FRPD unificado). IPRData.ttl modela 8 (FRPD split en CTCI y Fomento). Canónico: 7 mecanismos en ReferenceData (FRPD unificado). El split CTCI/Fomento es detalle operativo (líneas dentro del mecanismo), no mecanismos separados. GORE_OS `core.financing_track` tiene 7 tracks alineados.

## Tracks de evaluación (7)

| Track | Mecanismo | Evaluador | Dictamen |
|-------|-----------|-----------|----------|
| A — SNI General | SNI | MDSF | RS (Recomendación Satisfactoria) |
| B — Circular 33 | C33 | MDSF/GORE | AD (Admisibilidad) |
| C — FRIL | FRIL | GORE (DIPIR) | AT (Aprobación Técnica) |
| D1 — Glosa 06 | Glosa 06 | DIPRES/SES | RF (Recomendación Favorable) |
| D2 — Transferencias | Transfer | GORE (Comité/DAE) | ITF (Informe Técnico Favorable) |
| E1 — Subvención 8% | Subv8 | GORE (Comisión) | Puntaje/Ranking |
| E2 — FRPD | FRPD | ANID/CORFO/GORE | Elegibilidad + RS/RF |

**Reconciliación:** Omega define 7 tracks (A-E2). IPRData.ttl modela 4 tracks (RATE, Glosa06, LocalGORE, CTCI) — granularidad menor que agrupa sub-tracks del Omega bajo tracks amplios. Canónico: 7 tracks del Omega por mayor resolución operativa. Relación `skos:broader` pendiente en ontología.

Excepción al criterio de autoridad: se adoptan los 7 tracks del Omega (prioridad 3) sobre los 4 tracks de la ontología (prioridad 2) porque la granularidad del Omega refleja mejor la realidad operativa de GORE_OS. La ontología agrupa tracks bajo categorías amplias (RATE, LocalGORE) que pierden la distinción entre mecanismos.

## Resultados de evaluación (10)

| Código | Nombre completo | Track |
|--------|----------------|-------|
| RS | Recomendación Satisfactoria | A (SNI) |
| FI | Falta Información | A (SNI) |
| OT | Objetado Técnicamente | A (SNI) |
| AD | Admisible | B (C33), C (FRIL) |
| RF | Recomendación Favorable | D1 (G06) |
| ITF | Informe Técnico Favorable | D2 (Transfer) |
| AT | Aprobación Técnica | C (FRIL) |
| Elegible | Elegible (FRPD/FIC) | E2 (FRPD) |
| NV | No Viable | Transversal |
| Puntaje | Puntaje (concursos) | E1 (8%), E2 (FRPD) |

**Reconciliación:** ReferenceData.ttl: 6 resultados (RS, FI, OT, RF, ITF, AD). IPRData.ttl: 10 resultados (agrega AT, Elegible, NV, Puntaje). Canónico: 10 per IPRData (set más completo). RS = "Recomendación Satisfactoria" (IPRData, CQs, uso institucional), NO "Rentabilidad Social" (ReferenceData.ttl — descartado).

## Fuentes de financiamiento (FundingSource)

| Código | Nombre | URI ReferenceData | URI IPRData |
|--------|--------|-------------------|-------------|
| FNDR | Fondo Nacional de Desarrollo Regional | ✓ | ✓ |
| FRPD | Fondo Regional para la Productividad y el Desarrollo | ✓ | ✓ |
| ISAR | Inversiones Sectoriales de Asignación Regional | ✓ | ✓ |
| FIC | Fondo de Innovación para la Competitividad | ✓ | ✓ (como FIC) |
| FATC (Ref) | Fondo de Apoyo a la Transferencia de Competencias | ✓ | — |
| FATC (IPR) | Fondo de Apoyo al Transporte y Conectividad | — | ✓ |
| FRIL | Fondo Regional de Iniciativa Local | ✓ (solo Ref) | — |
| PROPIR | Programa Público de Inversiones Regionales | ✓ (solo Ref) | — |
| SECT | Fondos Sectoriales | ✓ (solo Ref) | — |
| FEI | Fondo de Equidad Interregional | — | ✓ (solo IPR) |
| FEIRR | Fondo de Inversión y Reconversión Regional | — | ✓ (solo IPR) |

**Reconciliación:** ReferenceData.ttl: 8 fuentes. IPRData.ttl: 7 fuentes. Sets no son superconjuntos — cada uno tiene exclusivas. Canónico: unión de ambos (11 fuentes, incluyendo FATC como 2 fondos distintos). `FundingSource` es `gnub:Category` (concepto categorial), distinto de `FinancingMechanism` que es `gnub:CatalogItem`. GORE_OS `ref.category` scheme `funding_source` tiene 11 — incluye fuentes adicionales de implementación.

FATC: colisión de acrónimos — ReferenceData usa "Transferencia de Competencias", IPRData usa "Transporte y Conectividad". Son fondos distintos. Canónico: ambos incluidos con nombre completo, nunca solo "FATC".

## Niveles de proporcionalidad SNI (4)

| Nivel | Umbral | Etapas |
|-------|--------|--------|
| 0 | < 5.000 UTM | Solo Ejecución (exención evaluación) |
| 1 | Baja complejidad | Perfil → Ejecución |
| 2 | Estándar | Perfil → Prefactibilidad → Ejecución |
| 3 | Alta complejidad | Idea → Perfil → Prefactibilidad → Factibilidad → Ejecución |

[impl: `core.sni_level_config` (4 niveles, admin CRUD). `_check_sni_proporcionalidad()` gate F1→F2. CLAUDE.md §Rule 38]

## Categorías FRIL (12)

| Grupo | Código | Nombre | Exención límite comunal |
|-------|--------|--------|------------------------|
| A — Desarrollo Territorial | A1 | Integración Rural | No |
| | A2 | Acceso al Agua | Sí |
| | A3 | Vial | Sí |
| B — Servicios | B1 | Edificación Pública | No |
| | B2 | Gestión Riesgos | No |
| | B3 | Seguridad | No |
| C — Desarrollo Social y Económico | C1 | Inclusión | No |
| | C2 | Género | No |
| | C3 | Turismo | No |
| D — Medio Ambiente | D1 | Deportes | No |
| | D2 | Áreas Verdes | No |
| | D3 | Sustentabilidad | No |

[impl: `core.fril_category` (12, `is_exempt_commune_limit` para A2/A3). `_check_fril_max_per_comuna()` gate F0→F1. CLAUDE.md §Rule 38]

## Fondos temáticos Subv. 8% (7)

| Fondo | Techo |
|-------|-------|
| Cultura | $5M |
| Deporte | $5M |
| Social | $5,5M |
| Seguridad Ciudadana | $8M |
| Medio Ambiente | $5M |
| Adulto Mayor | $4M |
| Género | $6,5M |

[impl: `core.subv8_fund` (7) + `core.subv8_fund_ceiling` (~22). Admin CRUD. CLAUDE.md §Rule 45]

## Estados de admisibilidad (5)

PRE-ADMISIBLE CDR, NO PRE-ADMISIBLE CDR, ADMISIBLE, ADMISIBLE CON OBSERVACIONES, INADMISIBLE.

[impl: `core.admissibility_item` + `core.admissibility_check`. Gate PRE_ADMISIBLE→ADMISIBLE. CLAUDE.md §Rule 41]

## Tipologías de inversión (5)

Determinan requisitos RIS (Requisitos de Información Sectorial) en evaluación F2.

| Tipología | Aplicación |
|-----------|-----------|
| Edificación Pública | Construcción/ampliación edificios públicos |
| Patrimonio | Restauración/conservación patrimonial |
| Infraestructura Deportiva | Recintos deportivos |
| Estudios PMDT | Planes maestros de desarrollo territorial |
| Salud | Infraestructura sanitaria |

Fuente: IPRData.ttl, 5 instancias `gnub:InvestmentTypology`.

## Modos de ejecución (2)

| Modo | Descripción | Mecanismos asociados |
|------|------------|---------------------|
| Ejecución Directa GORE | GORE ejecuta directamente (S31) | SNI, C33, Glosa 06 |
| Transferencia | GORE transfiere a terceros (S24, S33) | FRIL, Transfer, Subv8 |

Fuente: IPRData.ttl, 2 instancias `gnub:ImplementationMode`.

## Etapas de preinversión (4)

| Etapa | Seq | Nivel SNI asociado |
|-------|-----|-------------------|
| Idea | 1 | Nivel 3 (alta complejidad) |
| Perfil | 2 | Nivel 1-3 |
| Prefactibilidad | 3 | Nivel 2-3 |
| Factibilidad | 4 | Nivel 3 |

Fuente: IPRData.ttl, 4 instancias `gnub:PreinvestmentStage`. [ver niveles SNI en este documento](#niveles-de-proporcionalidad-sni-4)
