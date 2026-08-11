---
urn: urn:dev:artefacto:codex-route
nombre: codex-route
version: 2.2.1
estado: activo
descripcion: "Evalua explicitamente una tarea para Codex y recomienda superficie de ejecucion, modelo Sol/Terra/Luna, esfuerzo low-max, goal nativo y topologia minima. Invocar para decidir routing; por defecto no ejecuta."
fuente: "Version 1.0.0 creada el 2026-08-11 desde Rediseño codex-route como router de grafos de sesiones, sha256:6a7eebfa997fe1095ed67bd289ee0c1c957523fed19dc978fbe4e1c0e1ca166a. Version 2.0.0 reescrita el 2026-08-11 desde el dictamen operativo Sol-Luna, sha256:c1878d4c1c7d0715b3c88d5ec9a5bd86f7d817111d914f0247d1bebd32a54360. Version 2.1.0 incorpora Terra y seleccion conjunta modelo-esfuerzo desde documentacion oficial GPT-5.6 y tres graficos Artificial Analysis aportados el 2026-08-11. Version 2.2.0 incorpora superficies de ejecucion, threads independientes, evaluacion de goal nativo y comparacion privilegiada Luna Max frente a Sol High desde documentacion oficial Codex revalidada el 2026-08-11. Version 2.2.1 separa autorizacion de crear un thread y de fijar su modelo. La evidencia agregada calibra, no gobierna disponibilidad ni sustituye evals locales; las rubricas siguen siendo heuristicas no validadas como escalas predictivas."
autor: FS
creado: 2026-08-11
lang: es
tags: [codex, sesiones, threads, routing, grafos, goal, sol, terra, luna, delegacion, concurrencia, worktrees, verificacion]
vector: [2, 0, 2, 0, 1]
sigma: [2, 1, 3, 3, 1]
arnes: disciplina
forma: habilidad
herramientas: [Read, Write, Edit, Glob, Grep, Bash, spawn_agent, send_message, followup_task, wait_agent, interrupt_agent, list_agents, create_thread, fork_thread, list_projects, list_threads, read_thread, send_message_to_thread, set_thread_archived, set_thread_pinned, set_thread_title, create_goal, get_goal, update_goal]
targets: [codex]
alcance: usuario
estados: [perfilar-global, preflight, construir-grafo, perfilar-nodos, enrutar, ejecutar, integrar, verificar, cerrar]
---
# codex-route

## Propósito y activación

Elegir la organización mínima de sesiones Codex que alcance un resultado
verificable bajo costo, riesgo, contexto y coordinación. Cada candidata es
`superficie × modelo × esfuerzo`; evaluar además si el goal nativo mejora la
continuidad. Invocar explícitamente `$codex-route`; la metadata impide
activación implícita.

Usar solo `gpt-5.6-sol`, `gpt-5.6-terra` y `gpt-5.6-luna`. No crear un descendiente sin modelo
fijado si el runtime pudiera escoger fuera de esa allowlist. Preferir S0: un
grafo debe pagar su costo con menor tiempo, contaminación, riesgo o
incertidumbre.

## Modos

### `route-only` — predeterminado

Emitir una recomendación. No crear sesiones, enviar mensajes, abrir worktrees
ni ejecutar el trabajo enrutado.

### `route-and-run` — explícito

Activar solo si la solicitud o una instrucción aplicable autoriza delegar o
usar subagentes. Crear un thread independiente exige además solicitud explícita
para esa superficie; fijar su modelo exige que el usuario haya pedido ese
modelo concreto. Si falta esa autorización, emitir `ROUTE_ERROR ·
model_override_not_authorized` y no crear el thread. La activación no amplía
permisos, alcance ni autoridad.

## Fast path

- Operación literal, fuente y checker exactos: `current_session · Luna low · S0`; Terra low si Luna no está disponible.
- Varios pasos acotados con oráculo fuerte: `current_session · Luna medium · S0`; comparar Terra como triple ejecutable.
- Juicio acotado bajo contrato estable, sin gate Sol: `current_session · Terra medium · S0`.

Emitir una sola línea `SIMPLE_ROUTE`. Si la sesión efectiva difiere, separar
recomendación y ejecución; por ejemplo: `recommended: Luna low · effective:
Sol medium · cost_status: overprovisioned`.

## Routing en dos pasadas

1. Normalizar objetivo, entregable, fuente de verdad, aceptación, restricciones,
   riesgo y autoridad. Incluir beneficiario o presupuesto solo si gobiernan la
   ruta.
2. Evaluar siempre `native_goal`: fit, scope, activación autorizada, razón y
   condición de término. `S0 + goal` puede vencer a un grafo.
3. Calcular la **CEM global residual** con
   [cognitive-epistemic-matrix.md](referencias/cognitive-epistemic-matrix.md).
   Reducir antes la incertidumbre mediante fuente, contrato o aclaración acotada.
4. Hacer una **selección provisional** de superficie, modelo y esfuerzo con
   [execution-surfaces.md](referencias/execution-surfaces.md) y
   [model-effort-routing.md](referencias/model-effort-routing.md).
5. Trazar el camino crítico. Mantenerlo en la directora si delegarlo solo crea
   espera; delegar sidecars independientes.
6. Aplicar SGM-8 desde
   [session-graph-matrix.md](referencias/session-graph-matrix.md), diseñar el
   grafo y calcular `J`, carga de integración.
7. Ajustar el esfuerzo de la directora usando `J`; no cargar `J` a cada worker.
8. Calcular una **CEM local residual** por nodo y asignar superficie, modelo,
   esfuerzo, contexto, autoridad, persistencia y verificación propios.

Luna exige trabajo determinado, oráculo fuerte e integración baja. Comparar
obligatoriamente Luna Max ↔ Sol High si ambos triples son ejecutables. Terra exige
juicio acotado o fallback de disponibilidad, sin gate Sol. Sol es obligatorio
ante ambigüedad, arquitectura, novedad conceptual, evidencia contradictoria,
oráculo débil, acoplamiento, integración difícil, adjudicación o juicio de alta
consecuencia. `R` gobierna primero autonomía y verificación.

## Preflight de ejecución

Antes de `route-and-run`, leer
[execution-surfaces.md](referencias/execution-surfaces.md) y
[communication-protocol.md](referencias/communication-protocol.md), e
inspeccionar por superficie: creación, modelo, esfuerzo, contexto, concurrencia,
goal y lifecycle.

- Directora observada fuera de allowlist: `ROUTE_ERROR ·
  director_model_not_allowed` y recomendar reinicio en Sol, Terra o Luna.
- Sol requerido e indisponible: bloquear.
- Par recomendado indisponible: reevaluar pares permitidos, declarar fallback
  y costo, o bloquear; nunca sustituir silenciosamente.
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
  native_goal: {fit: yes, scope: thread, activation: proposed,
    stopping_condition: acceptance}
  director: {recommended_model: gpt-5.6-sol, available_models: [], effective_model: unknown,
    model_compliance: unknown, recommended_effort: high, available_efforts: [],
    effective_effort: unknown, effort_compliance: unknown,
    recommended_execution_surface: current_session}
  orchestration: {mode: director-managed, base_topology: S2}
  sessions:
    - {id: repo-map, cognitive_class: bounded-verifiable, recommended_execution_surface: subagent,
       recommended_model: gpt-5.6-terra,
       available_models: [], effective_model: unknown, model_compliance: unknown,
       recommended_effort: medium, available_efforts: [], effective_effort: unknown,
       effort_compliance: unknown, cost_status: unknown}
  critical_path: implementation remains in director
  communication: results to director only
  worktrees: none
  privileged_comparison: {candidates: [luna-max, sol-high],
    discarded_candidate_reason: luna gate not satisfied}
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
