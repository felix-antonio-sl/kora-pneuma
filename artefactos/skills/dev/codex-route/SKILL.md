---
urn: urn:dev:artefacto:codex-route
nombre: codex-route
version: 2.0.0
estado: activo
descripcion: "Evalua explicitamente una tarea para Codex y recomienda Sol o Luna, esfuerzo low-max y la topologia minima de sesiones. Invocar cuando se necesite una decision de routing; por defecto no ejecuta."
fuente: "Version 1.0.0 creada el 2026-08-11 desde Rediseño codex-route como router de grafos de sesiones, sha256:6a7eebfa997fe1095ed67bd289ee0c1c957523fed19dc978fbe4e1c0e1ca166a. Version 2.0.0 reescrita el 2026-08-11 desde el dictamen operativo Sol-Luna, sha256:c1878d4c1c7d0715b3c88d5ec9a5bd86f7d817111d914f0247d1bebd32a54360, contrastado con documentacion oficial viva de Codex sobre skills, subagentes y modelos. Las rubricas siguen siendo heuristicas no validadas como escalas predictivas."
autor: FS
creado: 2026-08-11
lang: es
tags: [codex, sesiones, routing, grafos, sol, luna, delegacion, concurrencia, worktrees, verificacion]
vector: [2, 0, 2, 0, 1]
sigma: [2, 1, 3, 3, 1]
arnes: disciplina
forma: habilidad
herramientas: [Read, Write, Edit, Glob, Grep, Bash, spawn_agent, send_message, followup_task, wait_agent, interrupt_agent, list_agents]
targets: [codex]
alcance: usuario
estados: [perfilar-global, preflight, construir-grafo, perfilar-nodos, enrutar, ejecutar, integrar, verificar, cerrar]
---
# codex-route

## Propósito y activación

Elegir la organización mínima de sesiones Codex que alcance un resultado
verificable bajo costo, riesgo, contexto y coordinación. Invocar explícitamente
`$codex-route`; la metadata del target impide activación implícita.

Usar solo `gpt-5.6-sol` y `gpt-5.6-luna`. No crear un descendiente sin modelo
fijado si el runtime pudiera escoger fuera de esa allowlist. Preferir S0: un
grafo debe pagar su costo con menor tiempo, contaminación, riesgo o
incertidumbre.

## Modos

### `route-only` — predeterminado

Emitir una recomendación. No crear sesiones, enviar mensajes, abrir worktrees
ni ejecutar el trabajo enrutado.

### `route-and-run` — explícito

Activar solo si la solicitud o una instrucción aplicable autoriza delegar o
usar subagentes. La activación no amplía permisos, alcance ni autoridad.

## Fast path

- Operación literal, fuente y checker exactos: `Luna low · S0`.
- Varios pasos acotados con oráculo fuerte: `Luna medium · S0`.
- Edge cases numerosos bajo contrato estable: `Luna high · S0`.

Emitir una sola línea `SIMPLE_ROUTE`. Si la sesión efectiva difiere, separar
recomendación y ejecución; por ejemplo: `recommended: Luna low · effective:
Sol medium · cost_status: overprovisioned`.

## Routing en dos pasadas

1. Normalizar objetivo, entregable, fuente de verdad, aceptación, restricciones,
   riesgo y autoridad. Incluir beneficiario o presupuesto solo si gobiernan la
   ruta.
2. Calcular la **CEM global residual** con
   [cognitive-epistemic-matrix.md](referencias/cognitive-epistemic-matrix.md).
   Reducir antes la incertidumbre mediante fuente, contrato o aclaración acotada.
3. Hacer una **selección provisional** del modelo de la directora con
   [model-effort-routing.md](referencias/model-effort-routing.md).
4. Trazar el camino crítico. Mantenerlo en la directora si delegarlo solo crea
   espera; delegar sidecars independientes.
5. Aplicar SGM-8 desde
   [session-graph-matrix.md](referencias/session-graph-matrix.md), diseñar el
   grafo y calcular `J`, carga de integración.
6. Ajustar el esfuerzo de la directora usando `J`; no cargar `J` a cada worker.
7. Calcular una **CEM local residual** por nodo y asignar modelo, esfuerzo,
   contexto, autoridad, persistencia y verificación propios.

Luna exige objetivo, entregable, método o búsqueda, fuente de verdad, oráculo e
integración local determinados, sin juicio material de alta consecuencia. Sol
es obligatorio ante ambigüedad residual, arquitectura, novedad conceptual,
evidencia contradictoria, oráculo débil, acoplamiento, integración difícil,
adjudicación o juicio de alta consecuencia. `R` gobierna primero autonomía y
verificación; no eleva modelo o esfuerzo sin razonamiento sustantivo.

## Preflight de ejecución

Antes de `route-and-run`, leer
[communication-protocol.md](referencias/communication-protocol.md) e
inspeccionar el contrato vivo: modelo raíz, overrides de modelo/esfuerzo,
creación, contexto, concurrencia y lifecycle.

- Directora observada fuera de allowlist: `ROUTE_ERROR ·
  director_model_not_allowed` y recomendar reinicio en Sol o Luna.
- Sol requerido e indisponible: bloquear.
- Luna recomendada e indisponible: `collapse`, Sol con `cost_degraded`, o
  `blocked`; nunca fallback silencioso.
- Modelo o esfuerzo efectivo desconocido: `compliance: unknown`; no afirmar
  cumplimiento exacto.
- Sin override permitido en allowlist: no crear ese descendiente.

## Grafo mínimo

Elegir una base S0–S9 en
[topology-catalog.md](referencias/topology-catalog.md). Separar árbol de
gobierno, DAG de trabajo, mensajes parent↔child, aristas peer y write sets.
Usar una topología base; representar otras como fase, modificador o subgrafo
local. Aplicar [domain-overrides.md](referencias/domain-overrides.md) solo si el
dominio estrecha de verdad la ruta.

## Salida

- `SIMPLE_ROUTE`: una línea.
- `COMPACT_GRAPH_ROUTE` — predeterminado para grafos.
- `FULL_GRAPH_ROUTE`: solo si se solicita, se ejecutará, existe riesgo alto,
  delegación recursiva, varios escritores o calibración.
- `ROUTE_ERROR`: causa, evidencia y decisión mínima.

```yaml
route:
  director: {recommended_model: gpt-5.6-sol, available_models: [], effective_model: unknown,
    model_compliance: unknown, recommended_effort: high, available_efforts: [],
    effective_effort: unknown, effort_compliance: unknown}
  orchestration: {mode: director-managed, base_topology: S2}
  sessions:
    - {id: repo-map, cognitive_class: bounded-verifiable, recommended_model: gpt-5.6-luna,
       available_models: [], effective_model: unknown, model_compliance: unknown,
       recommended_effort: medium, available_efforts: [], effective_effort: unknown,
       effort_compliance: unknown, cost_status: unknown}
  critical_path: implementation remains in director
  communication: results to director only
  worktrees: none
  cheaper_route_not_used: graph reduces critical-path uncertainty
  stop: acceptance or two equivalent causal failures
```

El schema completo, incluidos `available_*`, `effective_*`, cumplimiento,
confianza y estado de evidencia, vive en `communication-protocol.md`. Omitir
matrices salvo ruta fronteriza o solicitud expresa.

## Ejecutar, integrar y cerrar

Entregar a cada sesión objetivo, ownership, aceptación, autoridad,
restricciones, salida y verificación. Mantener un escritor cuando sea posible;
worktree solo ante interferencia real de escritura. No habilitar broadcast ni
usar mensajería para sincronizar archivos.

Evaluar resultados antes de incorporarlos, adjudicar contradicciones en la
directora y verificar el objetivo global. Gestionar lifecycle hasta
`integrated`; cerrar solo si el runtime ofrece la operación. Distinguir `PASS`,
`FAIL`, `ABSENT` y `NOT_RUN`.

Leer [calibration.md](referencias/calibration.md) al cambiar umbrales o afirmar ventaja costo/calidad. Paridad material, sesiones creadas o una ruta propuesta
no prueban conducta, menor costo, seguridad, aceptación ni calidad superior.
