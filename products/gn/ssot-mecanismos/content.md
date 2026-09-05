---
urn: urn:gn:kb:ssot-mecanismos
nombre: ssot-mecanismos
version: 1.1.1
estado: borrador
descripcion: "Documento SSOT GORE Ñuble migrado como conocimiento borrador; su estado no implica validación institucional."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-ssot/ssot-mecanismos.md (sha256:df48e19ed4fc7e4ac0b3452f3892ac7d76623cc7c48f3fa2771738b5771eb593); cuerpo preservado íntegramente durante la migración KORA del 2026-08-02."
autor: FS
creado: 2026-03-10
lang: es
tags: [ssot, mecanismos, tracks, fril, frpd, subv8, c33, ppr, sni, evaluacion]
familia: bok
---

# SSOT — Reglas operativas por mecanismo de financiamiento

## Resumen

Reglas de negocio detalladas para cada uno de los 7 mecanismos de financiamiento. Complementa [ssot-ipr-lifecycle](urn:gn:kb:ssot-ipr-lifecycle) (clasificación y tracks) con plazos, criterios de evaluación, admisibilidad y restricciones operativas por mecanismo. Fuente principal: Omega v2.6.0.

## Definiciones transversales

### Conceptos SNI

**Ficha IDI** — Formulario estándar del SNI con información básica de una Iniciativa de Inversión: datos de formulación, resultados evaluación ex-ante, programa de inversiones, resumen de resultados esperados, avance ejecución presupuestaria. Vehículo principal para solicitar financiamiento vía BIP. IDI = nomenclatura SNI para "Proyecto" (no es un mecanismo separado).

**BIP** (Banco Integrado de Proyectos) — Plataforma SNI del MDSF para registro y seguimiento de iniciativas de inversión pública. Toda IDI debe registrarse con código BIP (`^[0-9]{8}-[0-9]$`).

**BIPS** (Banco Integrado de Programas Sociales) — Registro del catálogo de oferta programática del Estado y resultados de evaluaciones M&E. Administrado por Subsecretaría de Evaluación Social y DIPRES. Distinto de BIP.

**Situación Base Optimizada** — Proyección optimizada de la situación actual con acciones de bajo costo antes de justificar inversión. Representa la "Situación Sin Proyecto" mejorada. Si optimizaciones menores resuelven el problema, no se justifica proyecto.

**Precios sociales** — Factores de corrección para transformar precios de mercado en precios sociales (eliminan impuestos, subsidios, externalidades). Publicados anualmente por MDSF (Subsecretaría de Evaluación Social). Incluyen TSD 5,5%, precio social mano de obra, precio social divisa, precio social carbono.

**Indicador SMART** — Indicador de desempeño en gestión pública: eSpecífico, Medible, Alcanzable, Relevante, Temporal. Exigido por DIPRES en PMG y evaluación de programas públicos.

### Conceptos generales

**ITO** (Inspector Técnico de Obra) — Profesional que supervisa ejecución de obras conforme a especificaciones del proyecto aprobado. Controla calidad, documentación y avance financiero. Regulado por Ley 20.703 y OGUC. En GORE: ITO GORE supervisa obras FRIL municipales (estados de pago, recepciones).

**BNUP** (Bien Nacional de Uso Público) — Bienes cuyo dominio pertenece a la nación y cuyo uso corresponde a todos los habitantes (Art. 589 Código Civil). Ejemplos: calles, plazas, caminos, playas. Municipalidades administran los BNUP en su territorio. Requisito de admisibilidad acreditar condición de terreno en FRIL/SNI.

**Garantía de fiel cumplimiento** — Caución exigida al adjudicado en compras públicas para resguardar cumplimiento del contrato. 5% del precio neto para contrataciones >1.000 UTM. Instrumentos: boleta bancaria, póliza de seguro, vale vista. Base legal: Ley 19.886 de Compras Públicas.

**PLADECO** (Plan de Desarrollo Comunal) — Instrumento de planificación indicativa municipal (Ley Orgánica de Municipalidades). Mínimo 4 años, aprobado por Concejo Municipal. Los PLADECO deben ser coherentes con ERD y PROT regionales. DIPLADE coordina articulación regional-comunal.

### Plazos de evaluación

| Proceso | Plazo | Responsable |
|---------|-------|-------------|
| Admisibilidad MDSF (SNI) | 10 días hábiles | MDSF |
| Análisis técnico-económico completo (SNI) | 45-90 días típico | MDSF |
| Respuesta a observaciones FI/OT | 60 días hábiles | Institución patrocinadora |
| Identificación presupuestaria post-RS | 20 días hábiles | DIPRES |
| Toma de Razón CGR | 15 días hábiles (no perentorio) | CGR |
| Actos exentos: registro CGR | 15 días hábiles desde emisión | Órgano emisor |
| Documentación faltante CGR | 2 días hábiles | Órgano emisor |

### Certificados de pertinencia sectorial

| Tipo proyecto | Servicio emisor | Organismo |
|--------------|----------------|-----------|
| Infraestructura deportiva | IND (Instituto Nacional de Deportes) | Mindep |
| Infraestructura sanitaria | Servicio de Salud regional | Minsal |
| Vialidad rural (caminos) | Dirección de Vialidad | MOP |
| Vialidad urbana (pavimentación) | SERVIU | MINVU |
| Edificación pública | SERVIU | MINVU |
| Estudios del giro (S22) | DIPRES (autorización) | Hacienda |

### Validez de documentos

| Documento | Antigüedad máxima práctica |
|-----------|--------------------------|
| Certificado dominio vigente | 30 días |
| Certificado avalúo fiscal | Año fiscal vigente |
| Cotizaciones (SNI/C33) | 6 meses |

## Track A — SNI General

### Evaluación MDSF

Metodología ex-ante obligatoria. 4 indicadores económicos:

| Indicador | Criterio | Uso |
|-----------|----------|-----|
| VAN (Valor Actual Neto) | ≥ 0 | Proyectos con beneficios cuantificables |
| TIR (Tasa Interna de Retorno) | ≥ TSD | Comparación entre alternativas |
| VAC (Valor Actual de Costos) | Menor = preferido | Proyectos sociales (costo-eficiencia) |
| CAE (Costo Anual Equivalente) | Menor = preferido | Comparar proyectos con vidas útiles distintas |

TSD 2025: 5,5% (Tasa Social de Descuento).

### Subsistemas SNI

4 subsistemas con retroalimentación:

Evaluación Ex Ante → Formulación Presupuestaria → Ejecución Presupuestaria → Evaluación Ex Post → (feedback)

### Vigencia RS ("Regla de Oro")

RS válido por 3 años presupuestarios consecutivos (año obtención + 2 siguientes). Si no se identifica presupuesto en ese plazo, RS caduca — requiere re-evaluación.

### Formulación SNI

- Problema de Cobertura vs Problema de Calidad (tipos de brecha social)
- Análisis Sin Proyecto / Con Proyecto (flujo incremental)
- Separabilidad de Componentes: Independientes, Unificados, Separables

### Tipos IDI Subtítulo 31

| Ítem | Tipo | Ejemplos |
|------|------|----------|
| 01 | Estudios Básicos | Diagnóstico, Exploración, Investigación |
| 02 | Proyectos | Obras civiles, Equipamiento, Consultorías |
| 03 | Programas Inversión | Capacitación, Transferencia, Prevención |

### RIS (Requisitos de Información Sectorial)

8 tipos: RIS-PROYINV, RIS-PROGINV, RIS-EDPUB, RIS-EB-PMDT, RIS-EMPUB, RIS-ARTCULT, RIS-DEPORTES, RIS-PATRIMONIO. Determinan documentación requerida según tipo de iniciativa.

[impl: `_check_sni_proporcionalidad()` gate F1→F2. `_check_evaluation_type_match()` F2→F3. CLAUDE.md §Rule 38]

## Track B — Circular 33

### Categorías C33 (5)

| Categoría | Subtítulo | Evaluación |
|-----------|-----------|------------|
| Estudios del Giro | S22 | Sin RATE |
| Adquisición ANF | S29 | Sin RATE. Subtipos: Terrenos, Edificios, Vehículos, Mobiliario, Máquinas, Equipos, Software |
| Conservación Caminos | S31 | Sin RATE si ≤30% costo reposición |
| Conservación Infraestructura | S31 | ≤30% costo reposición → Sin RATE; >30% o vida útil → Requiere SNI |
| Gastos Emergencia | S31 | Rehabilitación = GASTO (no C33); Reconstrucción = INVERSIÓN (sí C33) |

### Reglas operativas C33

- Cofinanciamiento ANF: 20% aporte propio obligatorio ([ver regla](urn:gn:kb:ssot-legal))
- Plazo postulación: 31 de octubre de cada año
- Metodología conservación/reposición: CAE o Costo-Eficiencia

### Matriz de documentación C33

10 documentos × 5 categorías. Documentos: Oficio Conductor, Ficha IDI, Ficha C33 Anexo 1, TDR, EETT+Presupuesto, 3 Cotizaciones/Tasaciones, Decreto Emergencia, Evaluación Económica, Cert. Mal Estado, Cert. Conservación 30%.

[impl: `_check_c33_conservation()` gate F1→F2 (informational). `categoria_c33` scheme. CLAUDE.md §Rule 42]

## Track C — FRIL

### Caracterización

| Parámetro | Valor |
|-----------|-------|
| Umbral máximo | 4.545 UTM (Ñuble; incluye 10% variacional) |
| Monto mínimo | M$100 piso de postulación |
| Máximo por comuna | 5 proyectos (A2/A3 exentos) |
| Evaluación | Técnica GORE (exento SNI/MDSF) |
| Subtítulo | S33 FNDR |

### Ciclo de ejecución FRIL (3 fases)

**Fase 1 — Postulación**: Municipalidad formula proyecto (EETT, Presupuesto, Planos) → Ingresa postulación + BIP → DIPIR admisibilidad (5 días) → Evaluación técnica (60 días) → Subsanación (30 días)

**Fase 2 — Aprobación**: DIPIR presenta para aprobación CORE → CORE aprueba marco → Convenio de transferencia

**Fase 3 — Ejecución**: Licitación (45 días) → Adjudicación + Contrato → Entrega terreno → Loop [Informe estado de pago / Transferencia recursos] → Recepción provisoria + Ficha cierre

### Restricciones FRIL

| Prohibición | Fundamento |
|-------------|------------|
| Gastos personal/consumo | Solo obras civiles |
| Proyectos con fines de lucro | Naturaleza pública |
| Fraccionamiento de obras | Evasión de umbrales |
| 2+ proyectos mismo terreno/año | Control duplicidad |
| ANF sin proyecto asociado | Solo complemento de obras |
| Multiubicación sin objetivo común | Deben compartir objetivo y licitarse juntas |

[impl: `_check_fril_max_per_comuna()` F0→F1. `_check_fril_fraccionamiento()` F1→F2 (±90d). `_check_fril_tender_deadline()` F3→F4. CLAUDE.md §Rule 38]

## Track D1 — Glosa 06 (Ejecución Directa PPR)

### Reglas de oro PPR

- Ejecución directa: GORE implementa (no transfiere)
- Instrumentos oficiales: Formularios de Perfil y Diseño PPR GORE (NO Ficha IDI SNI)
- No inversión: prohibido crear activos físicos como propósito principal

### Marco Lógico (MML)

Jerarquía vertical obligatoria:

Fin → Propósito → Componentes → Actividades

### Ciclo de vida PPR (3 fases)

Diseño y Formulación → Ejecución → Evaluación (con feedback)

### Criterios evaluación DIPRES/SES

| Criterio | Qué evalúa |
|----------|-----------|
| Atingencia | Pertinencia del programa al problema identificado |
| Coherencia | Consistencia interna del diseño (MML) |
| Consistencia | Alineación con políticas sectoriales y regionales |

### Tipos de población (3)

| Tipo | Definición |
|------|-----------|
| Potencial | Universo total con el problema |
| Objetivo | Subconjunto que el programa pretende atender |
| Beneficiaria | Efectivamente atendidos |

Fuente: IPRData.ttl, 3 instancias `gnub:PopulationType`. Requeridos para programas PPR (Tracks D1, D2).

[impl: Track Glosa06 en `core.financing_track`. CLAUDE.md §Rule 38]

## Track D2 — Transferencias PPR

### Caracterización

- Plataforma digital (NO usa BIP)
- MML obligatorio
- ITF (Informe Técnico Favorable) como dictamen

### Kit de postulación (9 documentos)

Oficio Conductor, Diseño de Programa, Presupuesto Detallado, Cotizaciones Respaldo, Perfil de Cargos, Patrocinio GORE, DJ Rendiciones/SISREC, DJ No Fraccionamiento, Compromiso Financiero.

### Evaluación interna (3 pasos)

Admisibilidad Documental (DAE) → Pertinencia Estratégica (Comité) → Evaluación Técnica (DAE) → dictamen ITF/Subsanar/Rechazado → Aprobación CORE

### Restricciones

- Honorarios max 5% del monto total
- Probidad: parentesco 3er grado consanguinidad / 2do afinidad
- Rendición SISREC obligatoria
- Prohibiciones: préstamos, instrumentos financieros, constituir sociedades

[impl: Track Transfer en `core.financing_track`. `check_glosa07_transfer_limits()`. CLAUDE.md §Rule 38]

## Track E1 — Subvención 8%

### Caracterización

| Parámetro | Privados | Municipios |
|-----------|----------|-----------|
| Monto total 2025 | M$4.850.000 | M$730.000 |
| Plazo ejecución | Max 8 meses | Max 9 meses |

### Reglas operativas

- **Unicidad**: max 1 iniciativa por institución. Excepciones: Cultura/Deporte 2da de Representación; Colaboradores Mejor Niñez múltiples residencias
- **Asignación directa**: ≤10% del fondo, previo acuerdo CORE (Res. 72/2025 DIPRES)
- **Pagaré notarial**: 100% monto + 18 meses vigencia — requisito habilitante, sin pagaré no hay desembolso
- **Excepción SISREC**: ≤500 UTM puede rendir fuera de SISREC (papel)
- **Coordinación**: actividades coordinadas con GORE (DIDESO) 10 días anticipación

### Admisibilidad (9 ítems)

Oficio Conductor, RUT Institución, Cédula Rep. Legal, Directorio Vigente (<60 días), Cert. Receptor Fondos Ley 19.862, Cuenta Bancaria institucional, Declaraciones Juradas, Cotizaciones, Carta Respaldo.

Inadmisibilidad inmediata si monto formulario ≠ carta ≠ presupuesto.

[impl: `_check_pagare_notarial()` F2→F3. `_check_directorio_certificate()` F2→F3. `_check_morosos_sisrec()` F3→F4+F4→F5. `_check_ranking_persistence()` F2→F3. CLAUDE.md §Rule 38]

## Track E2 — FRPD (Royalty Minero)

### Marco

Origen: Ley 21.591 (Royalty Minero). Habilitación: Res. Ex. 33/2024 (SUBCTCI). Alineación: ERD + Estrategia Regional CTCI obligatoria.

### Bifurcación post-selección

| Línea | Evaluación | Derivación |
|-------|-----------|-----------|
| CTCI | Exenta evaluación ex-ante | Directa a formalización |
| Fomento — Proyecto | Requiere evaluación SNI/MDSF | → Track A |
| Fomento — Programa | Requiere evaluación PPR | → Track D1 |

### Sectores prioritarios 2025 (4)

Atracción de Inversiones, Desarrollo Empresarial, Turismo y Medioambiente, Energía y Conectividad.

### Admisibilidad (6 criterios)

- Max 2 iniciativas por postulante
- Plazo ejecución ≤ 30 meses
- Cobertura regional (21 comunas) o territorial justificado
- Max remuneraciones 30%
- Min 1 profesional local (residente en Ñuble)
- Gastos admin max 5% (Art. 25 Ley 21.796)

### Restricciones

- Garantía privados: >1.000 UTM → 5% total, vigencia 90 días post-término
- Puntaje elegibilidad: mínimo 5 puntos promedio ponderado
- Vigencia RS: 3 años
- Aprobación CORE: >7.000 UTM
- Prohibidos: viáticos, alimentación, pasajes, peajes, estacionamiento
- Parentesco: inhabilidad hasta 4to consanguinidad / 3ro afinidad con Gobernador, CORE o directivos

### Ponderación evaluación técnica

| Criterio | Peso |
|----------|------|
| Mérito Innovador | 40% |
| Coherencia Regional (ERD) | 30% |
| Coherencia Componentes | 20% |
| Coherencia Global | 10% |

[impl: Track FRPD en `core.financing_track`. CLAUDE.md §Rule 38]

## Árbol de decisión para routing IPR→Track

Lógica simplificada de routing:

1. ¿Crea activo físico durable? → Sí: PROYECTO (S31/S33); No: PROGRAMA (S24)
2. Si PROYECTO: ¿Monto < 4.545 UTM + ejecutor municipal? → Sí: **FRIL** (Track C)
3. Si PROYECTO no-FRIL: ¿Es conservación/reposición/ANF? → Sí: **C33** (Track B)
4. Si PROYECTO estándar: **SNI** (Track A)
5. Si PROGRAMA: ¿Ejecución directa GORE? → Sí: **Glosa 06** (Track D1)
6. Si PROGRAMA transferencia: ¿Concurso 8%? → Sí: **Subv8** (Track E1); No: **Transferencia** (Track D2)
7. FRPD: routing especial post-selección (ver bifurcación arriba)

[impl: `GET /api/admin/financing-tracks/routing?ipr_id=X`. CLAUDE.md §Rule 45]

## Restricciones operativas cruzadas

| Mecanismo | Restricción | Consecuencia |
|-----------|------------|--------------|
| FRIL | Fraccionamiento prohibido | Rechazo postulación |
| FRIL | Plazo licitación 90 días | Caducidad asignación |
| Glosa 06 | Admin GORE max 5% | Rechazo DIPRES |
| Transfer | Honorarios max 5% | Ajuste o rechazo |
| Subv8 | Rendiciones pendientes | Inhabilidad total (bloqueo) |
| C33 | Cofinanciamiento ANF 20% ([ver legal](urn:gn:kb:ssot-legal)) | Requisito habilitante |
| FRPD | Garantía >1.000 UTM | 5% total + 90d post-término |

## Catálogo unificado de mecanismos

| Track | Costo típico | Ejecutor | Plazo ejecución |
|-------|-------------|----------|----------------|
| A — SNI | >15K UTM | GORE/Terceros | 12-36 meses |
| B — C33 | Variable | GORE | Variable |
| C — FRIL | <4.545 UTM | Municipalidad | 12-18 meses |
| D1 — Glosa 06 | Variable | GORE (directo) | 8-12 meses |
| D2 — Transfer | <$15M típico | Entidad pública | 8-12 meses |
| E1 — Subv8 | <$8M | OSC/Municipio | 8-9 meses |
| E2 — FRPD | Variable | Inst. habilitada | ≤30 meses |
