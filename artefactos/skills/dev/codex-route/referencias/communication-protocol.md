# Runtime, comunicación, schema y lifecycle

## Preflight obligatorio para `route-and-run`

Inspeccionar la superficie viva antes de crear sesiones:

```yaml
runtime_preflight:
  root_model_observed: true | false
  root_model_allowed: true | false
  available_execution_surfaces: []
  current_session_available: true | false
  spawn_available: true | false
  model_override_available: true | false
  luna_override_available: true | false
  terra_override_available: true | false
  sol_override_available: true | false
  effort_override_available: true | false
  fork_control_available: true | false
  lifecycle_controls: []
  independent_thread_surface:
    create_available: true | false
    project_resolved: true | false
    available_models: []
    available_efforts: []
    creation_authorized: true | false
    model_override_authorized: true | false
  native_goal_controls: []
```

No inferir una superficie u override desde documentación o ejecuciones pasadas.
Si la directora no es observable o permitida, o el triple requerido no puede
fijarse, aplicar los fallos cerrados de `model-effort-routing.md`.
Para un thread independiente, autorización de creación y de override son
distintas: si el usuario no pidió el modelo concreto, emitir `ROUTE_ERROR ·
model_override_not_authorized` y no crear el thread.

## Planos del grafo

```text
T_g = árbol de autoridad y control
M_parent = mensajes parent↔child permitidos por T_g
M_peer ⊆ E_dependency ∪ E_review
M_c = M_parent ∪ M_peer
```

`E_dependency` contiene dependencias de conocimiento o trabajo; `E_review`
contiene aristas dirigidas de revisión. El árbol de gobierno no se finge como
dependencia de datos.

Plano de control:

```text
TASK · BLOCKER · INTERRUPT · LOCAL_DECISION · GLOBAL_DECISION · CLOSE
```

Plano de conocimiento:

```text
CONTRACT · EVIDENCE · RESULT · CHALLENGE
```

Una supervisora puede emitir `LOCAL_DECISION` dentro de autoridad delegada.
Solo `/root` emite `GLOBAL_DECISION` sobre objetivo, alcance, interfaces
globales, presupuesto, riesgo y aceptación.

Formato:

```text
TYPE | petición o afirmación | evidencia | impacto | qué bloquea
```

Autorizar un peer edge solo si una dependencia explícita surgió después del
paquete, la respuesta cambia el trabajo receptor y el intercambio es acotado.
No usar broadcast, conversación ambiental ni mensajería para sincronizar
archivos.

## Contrato de sesión y routing efectivo

Toda sesión delegada recibe y reporta:

```yaml
id: slug
role: responsabilidad local
objective: resultado local
source_of_truth: []
scope: []
non_scope: []
deliverable: []
verification: []
write_set: none | []
authority: []
allowed_message_edges: []
stop_conditions: []
escalation_conditions: []
cognitive_class: bounded-verifiable | judgment-intensive
routing_basis: []
recommended_execution_surface: current_session | subagent | independent_thread
available_execution_surfaces: []
effective_execution_surface: id | unknown
execution_surface_compliance: exact | degraded | unknown | blocked
recommended_model: gpt-5.6-sol | gpt-5.6-terra | gpt-5.6-luna
available_models: []
effective_model: id | unknown
model_compliance: exact | degraded | unknown | blocked
recommended_effort: low | medium | high | xhigh | max
available_efforts: []
effective_effort: level | unknown
effort_compliance: exact | degraded | unknown | blocked
cost_status: optimal | cost_degraded | overprovisioned | unknown
```

`recommended ≠ effective` exige declarar degradación y consecuencia. Un valor
efectivo o costo desconocido impide afirmar cumplimiento u optimalidad. Para
escritura, añadir workspace, candidato, ownership exclusivo y prohibición de
revertir trabajo ajeno.

## Schema completo de ruta

```yaml
route:
  mode: route-only | route-and-run
  evidence_status: proposed | preflighted | executed | verified
  confidence: low | medium | high
  native_goal:
    fit: yes | no | unknown
    scope: thread | objective | none
    activation: proposed | active | not_authorized | blocked_existing_goal
    reason: text
    stopping_condition: text | none
  director:
    global_profile: optional
    integration_load: 0..4
    recommended_execution_surface: current_session
    available_execution_surfaces: []
    effective_execution_surface: id | unknown
    execution_surface_compliance: exact | degraded | unknown | blocked
    recommended_model: gpt-5.6-sol | gpt-5.6-terra | gpt-5.6-luna
    available_models: []
    effective_model: id | unknown
    model_compliance: exact | degraded | unknown | blocked
    recommended_effort: low | medium | high | xhigh | max
    available_efforts: []
    effective_effort: level | unknown
    effort_compliance: exact | degraded | unknown | blocked
    cost_status: optimal | cost_degraded | overprovisioned | unknown
  orchestration:
    mode: none | director-managed
    base_topology: S0..S9
    phases: []
    modifiers: []
  sessions: []
  dependencies: []
  peer_edges: []
  worktrees: []
  candidate_triples: []
  privileged_comparison:
    candidates: [gpt-5.6-luna:max, gpt-5.6-sol:high]
    selected_candidate: id | unknown
    discarded_candidate_reason: text | evidence_missing
  cheaper_route_not_used: text | none
  stop: []
  verification: []
```

`confidence` expresa confianza en que la ruta es adecuada, no confianza en la
solución de la tarea. `evidence_status` distingue diseño, capacidad observada,
ejecución y resultado global verificado.

## Goal nativo

Toda propuesta `COMPACT_GRAPH_ROUTE` o `FULL_GRAPH_ROUTE` evalúa `native_goal`;
`S0 + goal` es una ruta válida y puede ser menor que un grafo. Usarlo cuando un
objetivo durable de varios turnos tiene una condición de término verificable y
la continuidad aporta más que el costo de seguimiento.

La activación requiere autorización explícita. Antes de `create_goal`, llamar
`get_goal`: un goal inconcluso impide crear otro. Presupuesto o token budget solo
se fija si el usuario lo pide. `update_goal` marca `complete` únicamente con el
objetivo logrado, o `blocked` según el contrato vivo; no inventar pausa o resume.

El Goal no reemplaza el objetivo, el DAG, el contrato de sesión, la aceptación,
la verificación ni el ownership. Su scope es el thread donde se crea y su
condición de término debe formar parte de la ruta, incluso si la activación queda
`proposed` o `not_authorized`.

## Contexto y operaciones vivas

Preferir contexto mínimo para tareas delimitadas si el runtime ofrece control
de fork. Heredar todo solo si es una entrada load-bearing; si el nodo siempre
necesita todo, `K` es baja y probablemente no debe delegarse.

- `spawn_agent`: crear una sesión concreta con modelo permitido fijado;
- `send_message` no inicia por sí mismo un turno; entrega información a una
  sesión que ya trabaja;
- `followup_task`: asignar trabajo nuevo o reactivar una sesión inactiva;
- `wait_agent`: esperar solo por una dependencia del camino crítico;
- `list_agents`: observar estado y slots;
- `interrupt_agent`: detener y redirigir sin descartar automáticamente contexto.

Para threads independientes, resolver primero con `list_projects`; crear con
`create_thread` solo tras solicitud explícita de la superficie y del modelo
concreto; observar con `list_threads` y `read_thread`; dirigir seguimientos con
`send_message_to_thread`. Título, pin y archivo requieren operaciones expuestas
y autoridad específica. Un `route-and-run` genérico no autoriza crear un thread
de propiedad del usuario ni fijar su modelo.

Para goal nativo, usar solo `get_goal`, `create_goal` y `update_goal` según sus
precondiciones observadas.

Usar solo operaciones expuestas. No inventar nombres, campos o lifecycle.

## Lifecycle

```text
planned → spawned → acknowledged → running → completed → integrated → closed
```

No tratar `completed` como integrado. Evaluar el resultado, incorporarlo y
verificar el objetivo global antes de `integrated`. Si `close_agent` está
expuesto, cerrar L0/L1 después de integrar. Si no está expuesto, no inventarlo
y declarar la limitación de lifecycle.

Un thread independiente sigue `planned → created → running → completed →
integrated`; no se vuelve hijo ni se archiva por completar. Permanece bajo
propiedad del usuario y la directora registra qué evidencia integró.

## Concurrencia, escritura y worktrees

Comenzar con hasta tres hijas y profundidad dos solo si el runtime tiene slots,
la tarea lo justifica y las instrucciones aplicables autorizan subagentes. Son
heurísticas, no límites oficiales.

```text
workspace compartido + un escritor → sin worktree adicional
dos escritores + write sets realmente disjuntos → considerar worktrees
interfaces inestables → serializar aunque existan worktrees
```

Un worktree por dominio independiente de escritura, nunca por sesión. Si los
write sets dejan de ser disjuntos, detener S9 y volver a un escritor.

## Autonomía y detención

Los descendientes no reciben más autoridad que la directora. Exigir gate humano
para efectos externos, destrucción irreversible, gasto extraordinario, cambio
material de alcance y decisiones aplicadas de alta consecuencia.

Detener ante aceptación, presupuesto o iteraciones agotadas, dos fallos
causales equivalentes, oráculo ausente, blast radius creciente, write sets
solapados, comunicación continua o nueva autoridad necesaria. Devolver estado,
evidencia y decisión mínima: continuar, redirigir, fusionar, serializar o
bloquear.
