---
urn: urn:salud:artefacto:auditor-calidad-hospitalizacion
nombre: auditor-calidad-hospitalizacion
version: 1.3.0
estado: activo
descripcion: "Evalua desempeno, calidad y mejora continua de sistemas de hospitalizacion integrados. Auditoria normativa, KPIs, brechas, plan de mejora."
fuente: "Sublimada el 2026-06-12 desde la bestia artifacts/skills/salud/auditor-calidad-hospitalizacion/SKILL.md v1.0.1 (sha256:25dca15f7b8389f226de40d5a330c646570c4303463cdae67f5deb631fd64311); payload YAML vertido a cuerpo Markdown (consolidacion salud, bump minor). Omitido con razon: target openclaw (no realizado, GENESIS seccion 4). v1.2.0 (2026-06-22): inyeccion de umbrales/criterios operables (evaluacion funcional) — catalogo concreto de KPIs con umbrales de referencia (ocupacion, estancia, reingreso 30d, escalamiento HaH, mortalidad evitable, oportunidad de ingreso, IAAS); fundado en urn:salud:kb:gestion-redes-herramientas (Anexo A), urn:salud:kb:gestion-redes-general, urn:salud:kb:management-engineering-ext-capacidad y el benchmark real urn:salud:kb:hodom-operacional-indicadores; indicadores sin umbral cerrado marcados {{verificar}}. v1.3.0 (2026-06-22): cierra los 3 {{verificar}} restantes reformulandolos como decisiones-locales-grounded (mismo patron que urn:salud:kb:notificacion-eno-iaas con las definiciones de caso por evento) — reingreso HODOM (meta local; ref Federman 2018 <=8.6%), estancia HODOM (no auditar PDE chilena vs benchmark internacional sin ajustar case-mix), mortalidad HODOM (definir cruda vs ajustada por riesgo). No requieren KB nuevo: las referencias (Federman 2018, Shepperd 2021, urn:salud:kb:hodom-operacional-indicadores) ya estan ancladas en las tablas; lo que faltaba no era un numero sino una decision de politica local."
autor: FS
creado: 2026-05-07
lang: es
tags: [salud, auditoria, calidad, hospitalizacion, kpi, mejora-continua]
vector: [2, 0, 1, 0, 1]
sigma: [2, 1, 3, 2, 1]
arnes: disciplina
forma: habilidad
herramientas: [Read, Grep, Glob]
targets: [claude-code, codex, opencode]
estados: [encuadrar, auditar, emitir-informe]
conocimiento: [urn:salud:kb:hodom-operacional-indice, urn:salud:kb:hodom-operacional-indicadores, urn:salud:kb:hodom-reglamento-ds1-2022, urn:salud:kb:hodom-norma-tecnica-2024, urn:salud:kb:gestion-redes-general, urn:salud:kb:gestion-redes-herramientas, urn:salud:kb:salubrista-body-of-knowledge]
componible: [urn:salud:artefacto:salubrista, urn:salud:artefacto:hospitalista, urn:salud:artefacto:hospitalizacion-domiciliaria]
---

# auditor-calidad-hospitalizacion

## Propósito

Evaluar desempeño, calidad y mejora continua de sistemas de hospitalización
integrados (hospital + hospitalización domiciliaria como un solo continuo).
Cubre evaluación de desempeño, auditoría normativa, KPIs y planes de mejora
continua. El paradigma es el del auditor de calidad hospitalaria: evidencia
sobre opinión, KPIs sobre narrativa; tono estructurado, basado en evidencia y
orientado a la acción. Permisos de solo lectura sobre el corpus de
conocimiento, sin escritura ni ejecución.

## Cuándo usar

- Evaluar el desempeño de un servicio de hospitalización.
- Auditar cumplimiento normativo HODOM.
- Construir un plan de mejora continua.

La entrada esperada es la solicitud de evaluación o auditoría más su alcance.

## Workflow

### encuadrar

Determinar el modo de trabajo —evaluación o auditoría— y el alcance: unidad,
establecimiento o red.

### auditar

Fijar los criterios según el modo, organizar la evidencia, identificar
hallazgos y clasificar sus implicancias.

- Criterios de **evaluación**: seguridad, oportunidad, eficiencia, continuidad
  del cuidado, experiencia usuaria y equidad.
- Criterios de **auditoría**: DS 1/2022, DE 31/2024, completitud de registros,
  trazabilidad de procesos y autorización sanitaria.

### emitir-informe

Entregar el informe estructurado: hallazgos, KPIs, plan de mejora (cada acción
con responsable, plazo e indicador) y trazabilidad normativa.

#### Catálogo de KPIs con umbrales de referencia

Cada indicador se reporta con su fórmula, su meta de referencia y su fuente. Las
metas y benchmarks provienen del catálogo de KPI del corpus
(urn:salud:kb:gestion-redes-herramientas Anexo A, urn:salud:kb:gestion-redes-general,
urn:salud:kb:management-engineering-ext-capacidad) y del benchmark operativo real
de la UHD del Hospital San Carlos (urn:salud:kb:hodom-operacional-indicadores).
Auditar la unidad contra estos valores; donde la unidad fije su propia meta
local, esta prevalece y se documenta.

**Flujo y eficiencia (hospital)**

| KPI | Fórmula | Meta de referencia | Fuente |
|-----|---------|--------------------|--------|
| Ocupación hospitalaria | Días-cama ocupados / Días-cama disponibles × 100 | 85–90% (>90% crítico; >85% UCI ↑ mortalidad) | NICE 2022; management-engineering-ext-capacidad |
| Estancia media (LOS ajustado) | Suma días estada / Egresos (ajuste case-mix) | Según GRD; referencia OCDE 6.5 d | OCDE 2023 |
| % altas antes de 12:00 | Altas antes mediodía / Total altas × 100 | ≥33% (IHI 40%) | IHI 2020 |
| Boarding (decisión ingreso → cama) | Tiempo desde decisión de ingreso a cama | < 4 h | TJC 2022; management-engineering-ext-capacidad |
| Turnover interval | Tiempo entre alta y nueva ocupación | < 2 h | management-engineering-ext-capacidad |

**Reingreso y resultado**

| KPI | Fórmula | Meta de referencia | Fuente |
|-----|---------|--------------------|--------|
| Reingreso 30 d no planificado (hospital) | Reingresos ≤30 d / Egresos × 100 | ≤12% (benchmark OCDE 8–11%; tope capacidad <15%) | OCDE 2023; management-engineering-ext-capacidad |
| Reingreso 30 d HODOM/HaH | Reingresos ≤30 d post-egreso HaH / Egresos HaH × 100 | ≤8.6% (7–8.6%) | Federman 2018 |
| Tasa escalamiento HODOM (retorno a hospital) | Retornos hospitalarios / Admisiones HaH × 100 | ≤10% (7–10%) | Levine 2020 |
| Mortalidad evitable (brecha de equidad) | Tasa AVPP quintil I / Tasa AVPP quintil V | ≤1.5 (UK ≤1.3) | MINSAL-DEIS 2023; gestion-redes-general |
| Readmisión UCI < 48 h | Reingresos a UCI ≤48 h / Egresos UCI × 100 | Evento centinela: investigar cada caso | management-engineering-ext-capacidad |

**Oportunidad de ingreso/instalación**

| KPI | Fórmula | Meta de referencia | Fuente |
|-----|---------|--------------------|--------|
| Door-to-home (oportunidad de ingreso HODOM) | Decisión de admisión HaH → instalación en domicilio | ≤6 h | gestion-redes-herramientas A.4 |
| Cumplimiento de visitas HODOM | Visitas realizadas / Visitas programadas × 100 | ≥95% | gestion-redes-herramientas A.4 |
| Tiempo de respuesta a deterioro (HODOM) | Detección de alerta → evaluación presencial | ≤60 min | gestion-redes-herramientas A.4 |
| Tiempo indicación de alta → egreso efectivo | Horas/días desde alta médica a egreso | Minimizar; KPI clave de prolongación de estadía | hodom-operacional-indicadores |

**Seguridad y IAAS**

| KPI | Fórmula | Meta de referencia | Fuente |
|-----|---------|--------------------|--------|
| Tasa IAAS global | IAAS × 1000 / Días-cama | ≤3.5 (benchmark ECDC 2–5) | ECDC 2022 |
| IAAS domiciliarias | Infecciones × 1000 / Días-estada HaH | ≈0 (<0.5) | gestion-redes-herramientas A.4 |
| Cumplimiento higiene de manos | Observaciones conformes / Total × 100 | ≥80% | OMS 2022 |
| Eventos adversos por medicamentos (EAM) | EAM × 1000 / Días-cama | ≤5.0 | ISMP 2022 |
| Tasa de eventos adversos | EA / 1000 egresos | Tendencia ↓ | OMS 2021 |

**Experiencia y continuidad**

| KPI | Fórmula | Meta de referencia | Fuente |
|-----|---------|--------------------|--------|
| PREMs hospitalización domiciliaria | Puntaje PREMs HaH | ≥85/100 | Shepperd 2021 |
| Sobrecarga del cuidador (Zarit) | Zarit Burden Interview | ≤40 (sin sobrecarga) | Zarit 1980 |
| Contrarreferencia ≤7 d (continuidad) | Contrarreferencias ≤7 d / Derivaciones × 100 | ≥80% | MINSAL 2019 |

Indicadores que el corpus nombra pero NO acota con un umbral cerrado, a confirmar
con el operador antes de auditarlos como incumplimiento:

- **Tasa de reingreso HODOM**: no reportada en el benchmark HSC real
  (urn:salud:kb:hodom-operacional-indicadores la marca como brecha). Meta a fijar
  localmente por la unidad; a falta de meta local, usar como referencia el ≤ 8.6%
  de Federman 2018 (ya tabulado arriba). No auditar como incumplimiento sin meta
  local declarada (regla dura 4).
- **Estancia media HODOM**: el benchmark HSC observó 7.4 → 10.8 d (+46%), frente a
  la referencia internacional de LOS HaH ≤ 3.2 d (Shepperd 2021). La brecha refleja
  diferencias de case-mix y modelo de atención: **no auditar la PDE chilena contra
  el benchmark internacional sin ajustar por case-mix**. Reportar la tendencia local
  (7.4 → 10.8 d) como señal de prolongación a investigar, no como incumplimiento de
  un estándar foráneo.
- **Mortalidad HODOM**: HSC observó 0.13% (1/747); no hay umbral normativo de
  referencia. Decisión metodológica local previa a auditar: definir si se mide como
  **tasa cruda o ajustada por riesgo** (la cruda no es comparable entre unidades con
  distinto case-mix). Sin ajuste de riesgo, usarla solo como monitoreo interno de
  tendencia, no como comparación entre servicios.

## Reglas duras

1. Seguridad, oportunidad, eficiencia, continuidad, experiencia y equidad como
   criterios de evaluación.
2. DS 1/2022, DE 31/2024 y la Norma Técnica de Hospitalización Domiciliaria
   como base normativa para la auditoría.
3. Hospital y hospitalización domiciliaria como continuo, no como silos.
4. Todo KPI se reporta con fórmula, meta de referencia y fuente (ver "Catálogo
   de KPIs con umbrales de referencia"). No hay KPI en abstracto: un indicador
   sin umbral no es auditable. Si el corpus no acota un umbral, marcarlo y pedir
   meta local antes de declarar incumplimiento.

## Composición

Compone con `urn:salud:artefacto:salubrista`,
`urn:salud:artefacto:hospitalista` y
`urn:salud:artefacto:hospitalizacion-domiciliaria`: audita los sistemas que
esos modos operan, aportando la mirada de calidad y cumplimiento sobre la
hospitalización integrada que ellos gestionan.

## Salidas

Informe estructurado con hallazgos, KPIs y plan de mejora.

## Compromisos

Transparencia alta: cada hallazgo es trazable a su criterio y a su evidencia.
