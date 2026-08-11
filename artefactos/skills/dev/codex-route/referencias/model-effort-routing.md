# Routing binario de modelo y esfuerzo

## Política cerrada

Esta skill solo recomienda y utiliza:

```yaml
model_policy:
  allowed: [gpt-5.6-sol, gpt-5.6-luna]
  unpinned_descendants: forbidden
  fallback_outside_allowlist: forbidden
```

La allowlist estricta es una restricción deliberada del producto, no una
afirmación sobre todos los modelos existentes. No crear un descendiente sin
modelo fijado cuando el runtime pueda seleccionar automáticamente fuera de la
allowlist. No omitir el override para heredar una selección incierta. Todo
fallback fuera de la allowlist está prohibido.

Separar para la directora y cada sesión:

```text
recommended_model / available_models / effective_model / model_compliance
recommended_effort / available_efforts / effective_effort / effort_compliance
```

Cumplimiento: `exact | degraded | unknown | blocked`. Si lo efectivo es
desconocido, declarar `unknown`; nunca inferir ejecución exacta desde una
recomendación o configuración.

## Preflight y fallos cerrados

Inspeccionar el contrato vivo de creación. No inferir disponibilidad desde una
ejecución anterior, documentación general o el catálogo de la cuenta.

- Directora efectiva observada fuera de allowlist:
  `ROUTE_ERROR · director_model_not_allowed`.
- Directora efectiva no observable en `route-and-run`:
  `ROUTE_ERROR · director_model_unobserved`.
- Sol requerido y no disponible:
  `ROUTE_ERROR · sol_required_unavailable`.
- Luna recomendada y no disponible: elegir explícitamente una:
  - `collapse`: mantener el nodo en una directora permitida;
  - `cost_degraded`: usar Sol y declarar mayor costo;
  - `blocked`: recomendar abrir una sesión Luna.
- Ningún override permitido en allowlist: no crear el descendiente.

El fallback Luna→Sol puede degradar costo, no capacidad. Sol→Luna está
prohibido cuando permanecen arquitectura, integración difícil o juicio de alta
consecuencia.

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

Esfuerzo:

| Nivel | Uso |
|---|---|
| `low` | operación literal y checker exacto |
| `medium` | varios pasos acotados y oracle fuerte |
| `high` | tarea estrecha con edge cases o varios ciclos verificables |
| `xhigh` / `max` | solo con oráculo fuerte y ventaja medida frente a Sol |

## Gate obligatorio de Sol

Usar Sol si persiste cualquiera: ambigüedad material, arquitectura o
invariantes no resueltos, novedad conceptual, síntesis interdisciplinaria,
oráculo débil con juicio sustantivo, evidencia contradictoria, acoplamiento,
integración difícil, recomendación de alta consecuencia o adjudicación entre
resultados rivales.

| Nivel | Uso |
|---|---|
| `low` | excepcional, problema claro pero no delegable a Luna |
| `medium` | problema moderado y delimitado |
| `high` | lógica compleja, trade-offs o revisión adversarial |
| `xhigh` | varias dimensiones difíciles o síntesis interdisciplinaria |
| `max` | problema excepcional, evaluable y esencialmente serial |

No aumentar esfuerzo para compensar un modelo inadecuado. Riesgo alto con
transformación determinista puede seguir en Luna con gate humano y verificación
fuerte; riesgo alto con juicio exige Sol y gate humano.

## Dos pasadas

```text
director_model = route(CEM_global_residual)
SGM = design_graph(task)
integration_load = J(SGM)
director_effort = adjust_effort(CEM_global_residual, integration_load)
node_model_i = route(CEM_local_residual_i)
node_effort_i = effort(CEM_local_residual_i)
```

`integration_load` ajusta el esfuerzo de la directora, no el de cada worker.
Registrar solo las bases que gobernaron una ruta fronteriza.

## Fuentes oficiales

- [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Models](https://developers.openai.com/api/docs/models)

Las páginas describen capacidades generales; el contrato vivo decide qué
override puede ejecutarse en el turno actual.
