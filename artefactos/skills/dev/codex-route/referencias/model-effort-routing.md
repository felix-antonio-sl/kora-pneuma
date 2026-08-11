# Routing trifamiliar de superficie, modelo y esfuerzo

## Política cerrada

Esta skill solo recomienda y utiliza:

```yaml
model_policy:
  allowed: [gpt-5.6-sol, gpt-5.6-terra, gpt-5.6-luna]
  unpinned_descendants: forbidden
  fallback_outside_allowlist: forbidden
```

La allowlist estricta es una restricción deliberada del producto, no una
afirmación sobre todos los modelos existentes. No crear un descendiente sin
modelo fijado cuando el runtime pueda seleccionar automáticamente fuera de la
allowlist. No omitir el override para heredar una selección incierta. Todo
fallback fuera de la allowlist está prohibido.

## Unidad de decisión

Seleccionar un **triple superficie–modelo–esfuerzo**, no una familia, esfuerzo o
superficie por inercia. La forma canónica vive en `execution-surfaces.md`:
`route_candidate = (execution_surface, model, effort)`. El triple candidato más
barato debe satisfacer primero calidad, seguridad y aceptación. Sin contabilidad
comparable, enrutar por gates y declarar costo `unknown`. Comparar esfuerzos
iguales entre familias no prueba eficiencia: una Luna con más esfuerzo o una Sol
con menos esfuerzo puede superar a Terra.

Un triple está **dominado en sentido de Pareto** cuando otro triple ejecutable no es
peor en calidad ni seguridad, cuesta lo mismo o menos y mejora al menos una de
esas dimensiones. No recomendar un triple dominado dentro del conjunto disponible.
Solo una evaluación representativa o evidencia operacional comparable prueba
esa dominancia para el workload local; un índice agregado es un prior de
calibración, no un oráculo de la tarea.

Separar para la directora y cada sesión:

```text
recommended_model / available_models / effective_model / model_compliance
recommended_effort / available_efforts / effective_effort / effort_compliance
recommended_execution_surface / available_execution_surfaces
effective_execution_surface / execution_surface_compliance
cost_status / routing_basis
```

Cumplimiento: `exact | degraded | unknown | blocked`. Costo:
`optimal | cost_degraded | overprovisioned | unknown`. Si lo efectivo o la contabilidad
son desconocidos, declarar `unknown`; nunca inferirlos desde una recomendación.

## Comparación privilegiada Luna Max ↔ Sol High

Cuando **ambos pares ejecutables** existen en alguna superficie permitida y el
gate de Luna se satisface, registrar una **comparación privilegiada Luna Max ↔
Sol High**. Luna Max es candidata prioritaria para implementación y ejecución
específica, determinada, con oráculo fuerte e integración baja; Sol High es la
referencia para juicio, arquitectura, adjudicación e integración difícil.

```yaml
privileged_comparison:
  candidates: [gpt-5.6-luna:max, gpt-5.6-sol:high]
  executable_surfaces: []
  evidence: []
  selected_candidate: id | unknown
  discarded_candidate_reason: text | evidence_missing
```

La ruta debe explicar por qué descarta uno de los dos. Si persiste un gate
obligatorio de Sol, Luna queda inelegible y se registra esa razón; si Luna pasa
su gate, comparar costo total, calidad, latencia, corrección humana e integración
con una eval representativa local. Sin evidencia comparable se puede decidir por
gates y prior oficial, pero `cost_status` y dominancia quedan `unknown`. Esta
preferencia **no establece dominancia universal** ni prueba por sí sola que Luna
sea más barata o Sol mejor para el workload.

## Preflight y fallos cerrados

Inspeccionar el contrato vivo de cada superficie. No inferir disponibilidad desde una
ejecución anterior, documentación general o el catálogo de la cuenta.

- Directora efectiva observada fuera de allowlist:
  `ROUTE_ERROR · director_model_not_allowed`.
- Directora efectiva no observable en `route-and-run`:
  `ROUTE_ERROR · director_model_unobserved`.
- Sol requerido y no disponible:
  `ROUTE_ERROR · sol_required_unavailable`; Terra y Luna no lo sustituyen.
- Luna preferida e indisponible en la superficie propuesta: reevaluar otra
  superficie autorizada; después Terra si pasa su gate, Sol, `collapse` o
  `blocked`. Declarar `cost_degraded` solo con costo observado; de otro modo
  `cost_status: unknown`.
- Terra preferida e indisponible: comparar Luna con más esfuerzo y Sol con
  menos esfuerzo; usar el triple más barato que todavía cumpla aceptación.
- Ningún override permitido en allowlist: no crear el descendiente.

No existe fallback fijo por nombre de familia. Recalcular sobre triples
ejecutables y declarar `recommended ≠ effective`. Sol→Terra o Sol→Luna está
prohibido mientras persista un gate obligatorio de Sol.

## Gate de Luna

Luna es elegible solo si todas son verdaderas para el nodo local:

```text
objetivo y entregable determinados
método conocido o búsqueda acotada
fuente de verdad identificada
oráculo fuerte
integración local baja
sin juicio de alta consecuencia no resuelto
```

Es el punto de partida para operaciones literales, trabajo verificable y alto
volumen. La amplitud por sí sola no justifica Terra ni Sol.

## Gate de Terra

Terra es elegible solo si no existe gate Sol y todas son verdaderas:

```text
objetivo, aceptación, arquitectura e invariantes determinados
método conocido o combinación acotada de patrones
oráculo al menos revisable
acoplamiento e integración locales o moderados
sin adjudicación ni juicio de alta consecuencia pendiente
```

Además debe cumplirse al menos una: el nodo excede el gate Luna por juicio
acotado, especialización o interfaces estables; Luna no está disponible, Terra
pasa su gate y Sol no es obligatorio; o una eval representativa favorece
explícitamente el par Terra. Terra no es un fallback automático ni un escalón
ordinal entre Luna y Sol.

## Gate obligatorio de Sol

Usar Sol si persiste cualquiera: ambigüedad material, arquitectura o
invariantes no resueltos, novedad conceptual, síntesis interdisciplinaria,
oráculo débil con juicio sustantivo, evidencia contradictoria, acoplamiento,
integración difícil, recomendación de alta consecuencia o adjudicación entre
resultados rivales.

## Esfuerzo por familia

| Familia | `low` | `medium` | `high` | `xhigh` / `max` |
|---|---|---|---|---|
| Luna | operación literal | varios pasos acotados | edge cases verificables | solo con oráculo fuerte y ventaja medida |
| Terra | fallback literal o tarea muy clara | juicio acotado bajo contrato | tarea estrecha compleja y revisable | solo si vence pares Luna/Sol vecinos en eval local |
| Sol | problema claro no delegable abajo | problema moderado | trade-offs o revisión adversarial | síntesis difícil; `max` solo para lo excepcional y serial |

No aumentar esfuerzo para compensar un modelo inadecuado. Comparar al menos el
par vecino Luna con mayor esfuerzo y Sol con menor esfuerzo antes de elegir
Terra `high` o superior. Riesgo alto con transformación determinista puede
seguir en Luna o Terra con gate humano y verificación fuerte; riesgo alto con
juicio exige Sol y gate humano.

## Dos pasadas

```text
director_route = route(CEM_global_residual, available_triples)
SGM = design_graph(task)
integration_load = J(SGM)
director_route = adjust_effort(director_route, integration_load)
node_route_i = route(CEM_local_residual_i, available_triples_i)
```

`integration_load` ajusta el esfuerzo de la directora, no el de cada worker.
Registrar solo las bases que gobernaron una ruta fronteriza.

## Fuentes y estatus

- [Guía oficial GPT-5.6](https://developers.openai.com/api/docs/guides/latest-model):
  Sol prioriza capacidad frontera, Terra balance capacidad–costo y Luna volumen
  eficiente; validar cada workload con evals representativas.
- [Artificial Analysis: Sol, Terra y Luna](https://artificialanalysis.ai/articles/gpt-5-6-intelligence-vs-cost-across-sol-terra-luna):
  evidencia agregada externa para calibración Pareto, no autoridad runtime.
- [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents).

El contrato vivo decide qué override puede ejecutarse. Precios, índices y
ranking son volátiles: no persistir cifras como umbrales de routing.
