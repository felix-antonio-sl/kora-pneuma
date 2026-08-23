---
urn: urn:dev:artefacto:codex-route
nombre: codex-route
version: 3.0.0
estado: activo
descripcion: "Evalua explicitamente una tarea para Codex y recomienda superficie, uno de tres pares permitidos (Sol high, Sol max o Luna max), goal nativo y topologia minima. Excluye Terra y toda degradacion silenciosa. Invocar para decidir routing; por defecto no ejecuta."
fuente: "Version 1.0.0 creada el 2026-08-11 desde Rediseño codex-route como router de grafos de sesiones, sha256:6a7eebfa997fe1095ed67bd289ee0c1c957523fed19dc978fbe4e1c0e1ca166a. Version 2.0.0 reescrita el 2026-08-11 desde el dictamen operativo Sol-Luna, sha256:c1878d4c1c7d0715b3c88d5ec9a5bd86f7d817111d914f0247d1bebd32a54360. Version 2.1.0 incorpora Terra y seleccion conjunta modelo-esfuerzo desde documentacion oficial GPT-5.6 y tres graficos Artificial Analysis aportados el 2026-08-11. Version 2.2.0 incorpora superficies de ejecucion, threads independientes, evaluacion de goal nativo y comparacion privilegiada Luna Max frente a Sol High desde documentacion oficial Codex revalidada el 2026-08-11. Version 2.2.1 separa autorizacion de crear un thread y de fijar su modelo. La evidencia agregada calibra, no gobierna disponibilidad ni sustituye evals locales; las rubricas siguen siendo heuristicas no validadas como escalas predictivas. Version 3.0.0 (2026-08-23) ratifica una politica cerrada del operador: Terra queda excluida; Sol se usa solo en high o max y Luna solo en max. Actualiza las superficies al contrato vivo codex_app__*, hace worktree el default para proyectos Git, reserva local para solicitud explicita o proyecto no Git, e incorpora wait, handoff y share sin confundirlos con delegacion ni autorizacion. Baseline previo: proponia Luna low/medium y Terra, nombraba primitivas sin namespace y sustituyo un thread independiente por subagentes; ensayo post-cambio requerido antes de despliegue."
autor: FS
creado: 2026-08-11
lang: es
tags: [codex, sesiones, threads, routing, grafos, goal, sol, luna, delegacion, concurrencia, worktrees, verificacion]
vector: [2, 0, 2, 0, 1]
sigma: [2, 1, 3, 3, 1]
arnes: disciplina
forma: habilidad
herramientas: [Read, Write, Edit, Glob, Grep, Bash, spawn_agent, send_message, followup_task, wait_agent, interrupt_agent, list_agents, codex_app__create_thread, codex_app__fork_thread, codex_app__list_projects, codex_app__list_threads, codex_app__list_archived_threads, codex_app__read_thread, codex_app__read_thread_terminal, codex_app__send_message_to_thread, codex_app__wait_threads, codex_app__handoff_thread, codex_app__get_handoff_status, codex_app__share_thread, codex_app__open_in_codex, codex_app__set_thread_archived, codex_app__set_thread_pinned, codex_app__set_thread_title, create_goal, get_goal, update_goal]
targets: [codex]
alcance: usuario
estados: [perfilar-global, preflight, construir-grafo, perfilar-nodos, enrutar, ejecutar, integrar, verificar, cerrar]
---
# codex-route

## Propósito y activación

Elegir la organización mínima de sesiones Codex que alcance un resultado
verificable bajo costo, riesgo, contexto y coordinación. Cada candidata es
`superficie × par-modelo-esfuerzo`; evaluar además si el goal nativo mejora la
continuidad. Invocar explícitamente `$codex-route`; la metadata impide
activación implícita.

La política es cerrada y no negociable dentro de esta skill:

```text
gpt-5.6-sol:high
gpt-5.6-sol:max
gpt-5.6-luna:max
```

Terra y cualquier otro esfuerzo quedan excluidos. No recomendar, crear,
continuar ni reconfigurar una sesión con un par distinto. No omitir un override
si eso puede heredar un par fuera de política, y nunca degradar silenciosamente.
Preferir S0: un grafo debe pagar su costo con menor tiempo, contaminación,
riesgo o incertidumbre.

## Modos

### `route-only` — predeterminado

Emitir una recomendación. No crear sesiones, enviar mensajes, abrir worktrees
ni ejecutar el trabajo enrutado.

### `route-and-run` — explícito

Activar solo si la solicitud o una instrucción aplicable autoriza delegar o
usar subagentes. `codex_app__create_thread` crea otra tarea visible al usuario:
usarlo únicamente si pidió explícitamente una tarea nueva. Fijar modelo o
esfuerzo en esa tarea exige que haya pedido el par concreto; una allowlist o la
mera autorización de crear no eligen el par. Si falta esa autorización, emitir
`ROUTE_ERROR · model_override_not_authorized` y no crear. La activación no
amplía permisos, alcance ni autoridad.

## Fast path

- Operación determinada, fuente y checker exactos: `current_session · Luna max · S0`.
- Juicio acotado o integración revisable: `current_session · Sol high · S0`.
- Síntesis difícil, adjudicación o integración excepcional: `current_session · Sol max · S0`.

Emitir una sola línea `SIMPLE_ROUTE`. Si la sesión efectiva difiere, separar
recomendación y ejecución; por ejemplo: `recommended: Luna max · effective:
unknown · compliance: unknown`.

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
7. Ajustar el par de la directora usando `J`; no cargar `J` a cada worker.
8. Calcular una **CEM local residual** por nodo y asignar superficie, modelo,
   esfuerzo, contexto, autoridad, persistencia y verificación propios.

Luna Max exige trabajo determinado, oráculo fuerte e integración baja. Comparar
obligatoriamente Luna Max ↔ Sol High si ambos triples son ejecutables. Sol High
es la ruta de juicio e integración normal. Sol Max se reserva para síntesis,
adjudicación o integración excepcional que High no cubra con confianza. `R`
gobierna primero autonomía y verificación.

## Preflight de ejecución

Antes de `route-and-run`, leer
[execution-surfaces.md](referencias/execution-surfaces.md) y
[communication-protocol.md](referencias/communication-protocol.md), e
inspeccionar por superficie: creación, modelo, esfuerzo, contexto, concurrencia,
goal y lifecycle.

- Directora observada fuera de los tres pares: `ROUTE_ERROR ·
  director_pair_not_allowed` y recomendar reinicio en uno permitido.
- Par solicitado fuera de los tres permitidos: `ROUTE_ERROR ·
  requested_pair_not_allowed`; no reinterpretar la solicitud como autorización
  de otro par.
- Sol requerido e indisponible en High y Max: bloquear.
- Par recomendado indisponible: reevaluar sólo los otros pares permitidos y
  declarar el cambio, o bloquear; nunca sustituir silenciosamente.
- Modelo o esfuerzo efectivo desconocido: `compliance: unknown`; no afirmar
  cumplimiento exacto.
- Sin override permitido para un par exacto: no crear ese descendiente.

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
       recommended_model: gpt-5.6-luna,
       available_models: [], effective_model: unknown, model_compliance: unknown,
       recommended_effort: max, available_efforts: [], effective_effort: unknown,
       effort_compliance: unknown, cost_status: unknown}
  critical_path: implementation remains in director
  communication: results to director only
  worktrees: none
  privileged_comparison: {candidates: [gpt-5.6-luna:max, gpt-5.6-sol:high],
    discarded_candidate_reason: luna gate not satisfied}
  cheaper_route_not_used: graph reduces critical-path uncertainty
  stop: acceptance or two equivalent causal failures
```

El schema completo, incluidos `available_*`, `effective_*`, cumplimiento,
confianza y estado de evidencia, vive en `communication-protocol.md`. Omitir
matrices salvo ruta fronteriza o solicitud expresa.

## Ejecutar, integrar y cerrar

Entregar a cada sesión objetivo, ownership, aceptación, autoridad,
restricciones, salida y verificación. Para subagentes, usar las primitivas de
colaboración expuestas. Para tareas independientes, descubrir primero las
primitivas `codex_app__*`, llamar `codex_app__list_projects` y, si el proyecto
es Git, crear en worktree por defecto; `local` sólo para proyecto no Git o
solicitud explícita de usar el checkout guardado. No habilitar broadcast ni
usar mensajería para sincronizar archivos.

Esperar tareas independientes con `codex_app__wait_threads`; dirigirlas con
`codex_app__read_thread` y `codex_app__send_message_to_thread`. Handoff, share,
título, pin y archivo son efectos separados y requieren necesidad y autoridad
propias. No sustituir un thread solicitado por un subagente ni viceversa.

Evaluar resultados antes de incorporarlos, adjudicar contradicciones en la
directora y verificar el objetivo global. Gestionar lifecycle hasta
`integrated`; cerrar solo si el runtime ofrece la operación. Distinguir `PASS`,
`FAIL`, `ABSENT` y `NOT_RUN`.

Leer [calibration.md](referencias/calibration.md) al cambiar umbrales o afirmar ventaja costo/calidad. Paridad material, sesiones creadas o una ruta propuesta
no prueban conducta, menor costo, seguridad, aceptación ni calidad superior.
