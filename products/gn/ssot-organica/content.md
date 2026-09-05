---
urn: urn:gn:kb:ssot-organica
nombre: ssot-organica
version: 1.3.1
estado: borrador
descripcion: "Documento SSOT GORE Ñuble migrado como conocimiento borrador; su estado no implica validación institucional."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-ssot/ssot-organica.md (sha256:a53f9547566b90eb15b479cfb8f691c801eb1d8f53ca239e494d4a26c14e7ea6); cuerpo preservado íntegramente durante la migración KORA del 2026-08-02."
autor: FS
creado: 2026-03-10
lang: es
tags: [ssot, organica, divisiones, estructura-gore, jerarquia]
familia: bok
---

# SSOT — Estructura orgánica GORE Ñuble

## Resumen

Estructura orgánica canónica del Gobierno Regional de Ñuble. 6 divisiones, 13 departamentos, 10 unidades, 11 unidades de staff, 3 cuerpos asesores. Jerarquía 3 niveles: GORE → Divisiones → Departamentos → Unidades. Reconcilia organigrama legal con ontología formal.

## Autoridad ejecutiva

| Cargo | Rol institucional |
|-------|-------------------|
| Gobernador/a Regional | Órgano ejecutivo del Gobierno Regional. Electo/a por votación popular |
| Administrador/a Regional | Colaborador/a directo/a del Gobernador/a. Gestión administrativa |

El Delegado/a Presidencial Regional (gobierno interior) NO es parte del GORE — representante del Presidente de la República en la región.

## Tipos de cargo (8)

| Tipo | URI ontología |
|------|---------------|
| Gobernador/a Regional | `_PositionType_Gobernador` |
| Administrador/a Regional | `_PositionType_AdministradorRegional` |
| Jefe/a de División | `_PositionType_JefeDivision` |
| Jefe/a de Departamento | `_PositionType_JefeDepartamento` |
| Jefe/a de Unidad | `_PositionType_JefeUnidad` |
| Consejero/a Regional | `_PositionType_ConsejeroRegional` |
| Secretario/a Ejecutivo/a | `_PositionType_SecretarioEjecutivo` |
| RTF (Referente Técnico-Financiero) | `_PositionType_RTF` |

Fuente: OrgData.ttl, 8 instancias `gnub:PositionType`.

## Tipos de organización postulante (5)

| Tipo | URI ontología |
|------|---------------|
| Gobierno Regional | `_OrgType_GobiernoRegional` |
| Municipalidad | `_OrgType_Municipalidad` |
| ONG | `_OrgType_ONG` |
| Universidad | `_OrgType_Universidad` |
| Servicio Público | `_OrgType_ServicioPublico` |

Fuente: OrgData.ttl, 5 instancias `gnub:ApplicantInstitution`.

## Divisiones (6)

| Sigla | Nombre oficial | URI ontología |
|-------|---------------|---------------|
| DIPLADE | División de Planificación y Desarrollo Regional | `_Div_DIPLADE` |
| DIPIR | División de Presupuesto e Inversión Regional | `_Div_DIPIR` |
| DIDESO | División de Desarrollo Social y Humano | `_Div_DIDESO` |
| DIFOI | División de Fomento e Industria | `_Div_DIFOI` |
| DIT | División de Infraestructura y Transportes | `_Div_DIINF` |
| DAF | División de Administración y Finanzas | `_Div_DAF` |

**Reconciliación:** Nombre canónico "Infraestructura y Transportes" (plural) per organigrama y OrgData.ttl. Sigla: OrgData.ttl declara `skos:altLabel "DIT"` — no existe label "DIINF" en la ontología (solo el URI `_Div_DIINF`, que es convención de naming, no sigla semántica). GORE_OS usa DIT en test users y base de datos. Omega usa "DIINF" — descartado por no coincidir con la declaración ontológica.

## Departamentos (13)

| Departamento | División | URI ontología |
|-------------|----------|---------------|
| Planificación Estratégica y Ordenamiento Territorial | DIPLADE | `_Dept_DIPLADE_PlanificacionEstrategica` |
| Desarrollo de Proyectos Estratégicos | DIPLADE | `_Dept_DIPLADE_ProyectosEstrategicos` |
| Zonas en Desarrollo | DIPLADE | `_Dept_DIPLADE_ZonasDesarrollo` |
| Análisis y Evaluación | DIPIR | `_Dept_DIPIR_AnalisisEvaluacion` |
| Presupuesto | DIPIR | `_Dept_DIPIR_Presupuesto` |
| Fondos Concursables y Programas Sociales | DIDESO | `_Dept_DIDESO_FondosConcursables` |
| Gestión Territorial | DIDESO | `_Dept_DIDESO_GestionTerritorial` |
| Fomento y Desarrollo Productivo | DIFOI | `_Dept_DIFOI_FomentoDesarrolloProductivo` |
| Ciencia, Tecnología e Innovación | DIFOI | `_Dept_DIFOI_CTI` |
| Infraestructura y Conectividad | DIT | `_Dept_DIINF_InfraestructuraConectividad` |
| Ejecución y Supervisión de Proyectos de Inversión | DIT | `_Dept_DIINF_EjecucionSupervision` |
| Gestión y Desarrollo de Personas | DAF | `_Dept_DAF_GestionPersonas` |
| Finanzas | DAF | `_Dept_DAF_Finanzas` |

## Unidades (10)

| Unidad | Padre directo | División |
|--------|---------------|----------|
| Comité de Pertinencia y Vinculación Estratégica | DIPLADE (directo) | DIPLADE |
| Municipalidades y Conservaciones | Depto. Análisis y Evaluación | DIPIR |
| Proyectos y Programas | Depto. Análisis y Evaluación | DIPIR |
| Oficina de Partes | DAF (directo) | DAF |
| Tesorería | Depto. Finanzas | DAF |
| Contabilidad y Finanzas | Depto. Finanzas | DAF |
| Control de Rendiciones (UCR) | Depto. Finanzas | DAF |
| Adquisiciones | Depto. Finanzas | DAF |
| Operaciones (TIC) | Depto. Finanzas | DAF |
| OIRS | DGI (StaffUnit) | — |

## Unidades de staff (11)

Dependencias directas del Gobernador/a o del Administrador/a Regional. Clasificadas como `gnub:StaffUnit` en la ontología.

| Unidad | Dependencia de | URI ontología |
|--------|---------------|---------------|
| Gabinete y Participación Social | Gobernador/a | `_Staff_Gabinete` |
| Depto. de Comunicaciones | Gobernador/a | `_Staff_Comunicaciones` |
| Control | Gobernador/a | `_Staff_Control` |
| Depto. Jurídico | Administrador/a Regional | `_Staff_Juridica` |
| Auditoría Interna | Administrador/a Regional | `_Staff_Auditoria` |
| Depto. de Gestión Institucional (DGI) | Administrador/a Regional | `_Staff_DGI` |
| Depto. Ñuble 250 | Administrador/a Regional | `_Staff_Nuble250` |
| URAI (Asuntos Institucionales) | Administrador/a Regional | `_Staff_URAI` |
| Depto. Coordinación Integral de Emergencia y Seguridad (CIES) | Órganos Especiales | `_Staff_EmergenciaSeguridad` |
| Corporación Regional de Desarrollo | Administrador/a Regional | `_Staff_Corporacion` |
| Secretaría Ejecutiva del CORE | CORE | `_Unit_CORE_SecretariaEjecutiva` |

**Reconciliación — Clasificación tipológica:** El organigrama nombra Comunicaciones, Jurídica, DGI, Ñuble 250 y CIES como "Departamento". La ontología (OrgData.ttl) los clasifica como `gnub:StaffUnit` porque: (1) `gnub:Department` y `gnub:StaffUnit` son `owl:disjointWith`; (2) estas entidades dependen directamente del Gobernador/a o Administrador/a, no de una División; (3) un `gnub:Department` es `gist:isDirectPartOf` una `gnub:Division`. Prevalece la clasificación ontológica por mayor precisión tipológica. El título formal "Departamento" del organigrama se preserva en los nombres como convención institucional.

**DGI** específicamente: contiene OIRS como `gnub:Unit` hija. [impl: GORE_OS modela DGI como population="dgi" separada de operativa]

**Control vs Auditoría**: entidades separadas con funciones distintas — Control (fiscalización interna continua) vs Auditoría (evaluación independiente).

## Cuerpos asesores (3)

| Cuerpo | Tipo ontológico | URI |
|--------|----------------|-----|
| COSOC (Consejo de la Sociedad Civil) | AdvisoryBody | `_Advisory_COSOC` |
| Comité CTCI (Ciencia, Tecnología, Conocimiento e Innovación) | AdvisoryBody | `_Advisory_ComiteCTCI` |
| CDR (Comité Directivo Regional) | AdvisoryBody | `_Advisory_CDR` |

**Reconciliación:** COSOC aparece en organigrama y ontología. CDR y Comité CTCI existen en OrgData.ttl como `gnub:AdvisoryBody` pero están ausentes del organigrama (resolución exenta). Práctica habitual en sector público chileno — cuerpos funcionales no formalizados en resolución organizacional. CQs los referencian (CQ-007, CQ-011, CQ-012, CQ-027). Canónicos por ontología. CDR carece de composición modelada (`gist:hasMember` vacío) — irrespondible quién lo preside.

## CORE (Consejo Regional)

16 Consejeros/as Regionales electos/as por votación popular. Secretaría Ejecutiva del CORE como soporte administrativo.

Quórum canónico per GORE_OS:
- Simple: 9/16
- Calificado: 11/16

Periodicidad: mínimo 2 sesiones ordinarias por mes (≥24 anuales). Sesiones extraordinarias adicionales según necesidad.

### Mandatos

| Cargo | Duración | Reelección | Base legal |
|-------|----------|-----------|-----------|
| Gobernador/a Regional | 4 años (sufragio universal) | 1 período consecutivo (max 8 años) | Ley 21.073 |
| Consejeros/as Regionales | 4 años (sufragio universal) | Hasta 2 períodos consecutivos (max 12 años) | LOC GORE |

[impl: CLAUDE.md §Rule 31 — CORE sessions, gate F3→F4 >7K UTM]

## Jerarquía completa

```
GORE Ñuble
├── Gobernador/a Regional
│   ├── Gabinete y Participación Social (Staff)
│   ├── Depto. Comunicaciones (Staff)
│   └── Control (Staff)
├── Administrador/a Regional
│   ├── Depto. Jurídico (Staff)
│   ├── Auditoría Interna (Staff)
│   ├── Depto. Gestión Institucional/DGI (Staff) → OIRS (Unit)
│   ├── Depto. Ñuble 250 (Staff)
│   ├── URAI/Asuntos Institucionales (Staff)
│   └── Corporación Regional (Staff)
├── CORE → Secretaría Ejecutiva (Staff)
├── DIPLADE (División)
│   ├── Depto. Planificación Estratégica y Ordenamiento Territorial
│   ├── Depto. Desarrollo Proyectos Estratégicos
│   ├── Depto. Zonas en Desarrollo
│   └── Comité de Pertinencia (Unidad)
├── DIPIR (División)
│   ├── Depto. Análisis y Evaluación
│   │   ├── Unidad Municipalidades y Conservaciones
│   │   └── Unidad Proyectos y Programas
│   └── Depto. Presupuesto
├── DIDESO (División)
│   ├── Depto. Fondos Concursables y Programas Sociales
│   └── Depto. Gestión Territorial
├── DIFOI (División)
│   ├── Depto. Fomento y Desarrollo Productivo
│   └── Depto. CTI
├── DIT (División Infraestructura y Transportes)
│   ├── Depto. Infraestructura y Conectividad
│   └── Depto. Ejecución y Supervisión
├── DAF (División)
│   ├── Oficina de Partes (Unidad)
│   ├── Depto. Gestión y Desarrollo de Personas
│   └── Depto. Finanzas
│       ├── Tesorería (Unidad)
│       ├── Contabilidad y Finanzas (Unidad)
│       ├── UCR (Unidad)
│       ├── Adquisiciones (Unidad)
│       └── Operaciones/TIC (Unidad)
├── Depto. CIES (Staff, Órganos Especiales)
└── Cuerpos Asesores
    ├── COSOC
    ├── Comité CTCI
    └── CDR
```
