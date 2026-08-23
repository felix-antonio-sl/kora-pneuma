---
urn: urn:dev:artefacto:ship-discipline
nombre: ship-discipline
version: 1.2.0
estado: activo
descripcion: "Skill de disciplina de envio: blast radius, loop closure, ship-beats-perfect, architecture-over-implementation, repo-shaping para agent-friendliness, agent-foreman. Para cualquier agente que produzca o intervenga software con velocidad de inferencia manteniendo steerability, taste y reversibilidad."
fuente: "Sublimada el 2026-06-12 desde la bestia artifacts/skills/dev/ship-discipline/SKILL.md v1.0.1 (sha256:a5193d217901f2f23bc1d6a43e4446d7ac9b710212b8cc14c5a866084c4b5577). Correccion 1.0.2 (2026-06-15): referencias de doctrina bestia se reapuntaron al regimen de pneuma; 4 referencias quedaron byte-identicas. v1.1.0 (2026-08-09): reemplaza el checklist universal build-test-lint por verificaciones aplicables y proporcionales al riesgo; ABSENT no obliga a crear tooling. Target openclaw sigue omitido porque no esta realizado para esta skill. v1.2.0 (2026-08-23): incorpora hermes a targets — target realizado para forma habilidad en ley/3 v3.0.0 (T-hermes-pneuma-v1); la emision Hermes porta frontmatter oficial name/description/version y declara la ausencia de allowlist de herramientas como perdida del sello."
autor: FS
creado: 2026-04-28
lang: es
tags: [ship, blast-radius, loop-closure, agentic-engineering, repo-shaping, steinberger, just-talk-to-it, taste]
vector: [2, 0, 2, 0, 1]
sigma: [2, 1, 3, 2, 1]
arnes: disciplina
forma: habilidad
herramientas: [Read, Write, Edit, Glob, Grep, Bash]
targets: [claude-code, codex, opencode, hermes]
estados: [triaje, estimar-blast-radius, decidir-topologia, ejecutar-o-delegar, cerrar-loop, cierre]
conocimiento: [urn:dev:kb:peter-steinberger-ingeniero-agentico-prodigio]
componible: [urn:kora:artefacto:mente-omega, urn:kora:artefacto:cat-thinking]
---

# ship-discipline

## Proposito

Skill de **disciplina de envio agentic-engineering**. Da al agente
invocador la capacidad de mover ideas a software con velocidad de
inferencia preservando **steerability**, **loop closure**, **blast
radius** controlado, **taste** y **reversibilidad**.

Doctrina destilada de Peter Steinberger: ingeniero de producto
aumentado por enjambres de agentes — no programador que usa IA. El
software se descubre construyendolo en vivo, con agentes como mano de
obra cognitiva y el humano como sistema de direccion, gusto y
correccion.

## Cuando Usar

- el agente va a modificar codigo y se necesita decidir topologia
  (secuencial cuidadoso, paralelo moderado, maximo paralelismo).
- una tarea cambia archivos y antes de declararla hecha debe cerrar el
  loop con evidencia proporcional al riesgo y a la aceptacion.
- se va a estructurar un repositorio para que sea agent-friendly o se
  detecta que un repo existente penaliza a los agentes.
- hay que distinguir lo que delegar a agentes vs lo irreducible humano.
- se va a producir CLI, MCP o tooling reusable: sube el rigor.
- el contexto del modelo se esta ensuciando y hay que podar.

## Cuando NO Usar

- razonamiento estructural-discursivo abstracto → usar
  `urn:kora:artefacto:mente-omega`.
- enmarque categorial puro → usar `urn:kora:artefacto:cat-thinking`.
- ciclo de vida meta-KORA → se rige por el regimen de doctrina de pneuma
  (`urn:kora:kb:regimen-de-ley`): se autora en pneuma segun la ley, no se
  reconstruye desde la bestia.
- diseno de celulas humano-agente organizacionales → usar
  `urn:fxsl:artefacto:cell-design`.

## Workflow

### `triaje`

Tres preguntas guia:

1. **Hay codigo a producir/modificar?** Si no, declinar la skill.
2. **Cuanto sabe el operador del cambio?** (idea borrosa vs requerimiento concreto vs spec completa)
3. **Que tipo de cambio es?** (feature, refactor, fix, cleanup, tooling reusable)

### `estimar-blast-radius`

Antes de ejecutar cualquier cambio no trivial:

1. Identificar archivos directos e indirectos tocados.
2. Clasificar:

| Nivel | Criterio | Ruta |
|---|---|---|
| **Bajo** | 1-3 archivos, reversible, sin deps cruzadas | Ejecutar directo |
| **Medio** | 4-10 archivos, reversible, algunas deps | Tests + patch listo; commit si esta autorizado |
| **Alto** | 10+ archivos, potencialmente irreversible, multiples deps | Plan antes de ejecutar + validacion humana |

3. Documentar la estimacion en una linea antes de actuar.

**Defaults**:
- Ante duda, estimar hacia arriba.
- Schema, dependencias, boundaries → siempre alto.
- Estilo, formatting, docs → siempre bajo.

Detalle en `referencias/blast-radius-checklist.md`.

### `decidir-topologia`

| Tipo de trabajo | Topologia |
|---|---|
| Feature principal con riesgo medio | 1-2 acciones secuenciales |
| Cleanup, tests, UI, satelite | Paralelo moderado |
| Refactor pesado o cambios con alto conflicto | Secuencial cuidadoso |
| Multiples features independientes | Maximo paralelismo |

### `ejecutar-o-delegar`

**Lo irreducible humano** (no delegar a agentes ejecutores):

- system design, distributed systems, dependencias, boundaries
- DB schema, server/client split
- UX feel, naming, seleccion de plataforma
- product judgement, taste, frontera "suficiente vs mal hecho"

**Lo delegable** (a agentes ejecutores via exec/codigo):

- escribir, transformar, mover, refactorizar
- generar, probar, repetir hasta verde
- shaping mecanico de codigo

Detalle en `referencias/separacion-estratos.md`.

### `cerrar-loop`

Una tarea **NO** esta lista hasta que la aceptacion y los riesgos reales estan
cubiertos sobre el arbol exacto:

1. **Comportamiento** — verificar el outcome o journey solicitado.
2. **Checks aplicables** — ejecutar primero la prueba focal; ampliar a build,
   tests, typecheck, lint o integracion solo cuando existen y el cambio puede
   afectarlos.
3. **Estado honesto** — un `FAIL` relevante bloquea. `ABSENT` o `NOT_RUN` no
   aportan evidencia: si el check cubre aceptacion o un riesgo real, bloquean;
   si no, se declaran sin inventar tooling.
4. **Feel** — usar o revisar la solucion; no basta con que compile.
5. **Patch listo** — cambio coherente y verificable; commit solo autorizado.

Detalle en `referencias/loop-closure-checklist.md`.

### `cierre`

Reportar:

- blast radius estimado y topologia elegida,
- cambio aplicado con paths,
- loop cerrado con las comprobaciones aplicables y su estado,
- patch listo o commit hash autorizado,
- siguiente paso si la tarea es multi-incremento.

## Reglas Duras

1. **Blast radius antes de exec**.
2. **Loop closure obligatorio**: aceptacion + checks proporcionales +
   integracion + patch listo; commit solo con autorizacion explicita.
3. **Ship beats perfect**: util hoy > ideal hipotetico.
4. **Architecture over implementation**: humano en deps/schema/boundaries.
5. **Less is more**: cada capa justifica existencia.
6. **Just talk to it**: prompts cortos, lenguaje natural.
7. **Context cost**: poda lo que no aporta.
8. **Lo irreducible humano no se delega**.
9. **Sube rigor cuando produces tooling reusable** (CLI, MCP, lib).
10. **No invadir dominio**: la skill da disciplina, no semantica del campo.

## Anti-patrones

| Anti-patron | Falla | Correccion |
|---|---|---|
| Prompt charade | Sustituye claridad por teatro | Just talk to it; prompt corto |
| MCP para todo | Costo permanente de contexto | CLI cuando alcanza |
| Worktree mania | Carga cognitiva innecesaria | Trabajar en main si cabe |
| Subagent soup | Empaqueta complejidad manejable | Una sesion |
| Background-first | Pierde steerability | Foreground por defecto |
| Spec completa antes de tocar sistema | No calza con descubrimiento iterativo | Prototipar temprano |
| Leer todo el codigo generado | Desperdicia atencion senior | Mirar puntos de leverage |
| Loop abierto | Tarea declarada hecha sin evidencia aplicable | Cerrar siempre |

## Composicion con otras skills

| Composable con | Cuando |
|---|---|
| `urn:kora:artefacto:mente-omega` | la decision de arquitectura requiere razonamiento estructural-discursivo previo |
| `urn:kora:artefacto:cat-thinking` | la composicion del repo o la integracion entre subsistemas tensiona y se necesita lectura categorial |
| `urn:kora:kb:regimen-de-ley` | se va a producir o reemplazar una pieza meta-KORA: su autoria se rige por el regimen de doctrina de pneuma |

## Recursos

### Referencias

- `referencias/blast-radius-checklist.md` — checklist de estimacion +
  defaults + criterios.
- `referencias/loop-closure-checklist.md` — pasos del loop, gotchas y
  reglas.
- `referencias/repo-shaping-checklist.md` — checklist agent-friendly:
  estructura, naming, docs, CLI, ejemplos.
- `referencias/separacion-estratos.md` — humano-vs-agente: que delegar
  y que no, con criterios.

## Salida Esperada

- diagnostico de tarea + tipo de cambio,
- blast radius estimado con topologia,
- decision de delegacion humano/agente declarada,
- cambio aplicado,
- loop cerrado con evidencia proporcional y estados honestos,
- siguiente paso operativo.
