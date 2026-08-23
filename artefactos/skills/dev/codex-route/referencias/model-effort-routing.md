# Routing cerrado de modelo y esfuerzo

## Política ratificada

Esta skill sólo recomienda y utiliza tres pares:

```yaml
model_policy:
  allowed_pairs:
    - {model: gpt-5.6-sol, effort: high}
    - {model: gpt-5.6-sol, effort: max}
    - {model: gpt-5.6-luna, effort: max}
  terra: forbidden
  unpinned_descendants: forbidden
  silent_fallback: forbidden
```

Es una decisión del operador, no una afirmación de disponibilidad universal ni
un ranking de toda la familia GPT-5.6. Quedan prohibidos Terra, Sol en
`low|medium|xhigh|ultra`, Luna por debajo de `max` y cualquier otro modelo. Un
par soportado por el proveedor pero fuera de esta lista sigue fuera de política.

## Unidad de decisión

Seleccionar un triple `superficie × par permitido`, no modelo, esfuerzo o
superficie por inercia:

```text
route_candidate = (execution_surface, model, effort)
```

Separar recomendación de realidad observada:

```text
recommended_model / available_models / effective_model / model_compliance
recommended_effort / available_efforts / effective_effort / effort_compliance
recommended_execution_surface / available_execution_surfaces
effective_execution_surface / execution_surface_compliance
cost_status / routing_basis
```

Cumplimiento: `exact | degraded | unknown | blocked`. Si el par efectivo es
desconocido, declarar `unknown`; no inferirlo desde la recomendación. En
`route-and-run`, un par efectivo conocido fuera de política bloquea nuevas
creaciones o continuaciones con override.

## Gates

### Luna Max

Elegible sólo si todas son verdaderas para el nodo local:

```text
objetivo y entregable determinados
método conocido o búsqueda acotada
fuente de verdad identificada
oráculo fuerte
integración local baja
sin adjudicación ni juicio de alta consecuencia pendiente
```

Es la ruta de ejecución específica y verificable. Amplitud o volumen no elevan
por sí solos a Sol.

### Sol High

Es la ruta normal para juicio, arquitectura acotada, revisión adversarial,
síntesis y una integración que exige contexto central. También es el fallback
permitido de Luna Max cuando Luna no está disponible o deja de pasar su gate,
siempre declarado.

### Sol Max

Usar sólo si High resulta insuficiente por alguna de estas señales:

```text
síntesis difícil de varios dominios
arquitectura o invariantes materialmente no resueltos
evidencia contradictoria que exige adjudicación
oráculo débil con juicio sustantivo
integración excepcional o alta consecuencia
```

`max` no compensa un método malo, un objetivo ambiguo resoluble ni falta de
fuente. Reducir incertidumbre primero.

## Comparación privilegiada

Cuando ambos triples sean ejecutables y Luna pase su gate, comparar:

```yaml
privileged_comparison:
  candidates: [gpt-5.6-luna:max, gpt-5.6-sol:high]
  executable_surfaces: []
  evidence: []
  selected_candidate: id | unknown
  discarded_candidate_reason: text | evidence_missing
```

Luna Max es candidata prioritaria para ejecución determinada; Sol High para
juicio e integración. Explicar por qué se descarta una. Sin eval representativa
y costo comparable, `cost_status` y dominancia permanecen `unknown`.

## Preflight y fallback

Inspeccionar el contrato vivo de cada superficie. No inferir disponibilidad
desde documentación general, memoria o otra sesión.

- Par efectivo de la directora fuera de política:
  `ROUTE_ERROR · director_pair_not_allowed`.
- Par solicitado fuera de política:
  `ROUTE_ERROR · requested_pair_not_allowed`.
- Par efectivo no observable en `route-and-run`:
  `ROUTE_ERROR · director_pair_unobserved`.
- Sol requerido y ninguno de `high|max` disponible:
  `ROUTE_ERROR · sol_required_unavailable`.
- Luna Max indisponible: reevaluar Sol High y luego Sol Max sólo si pasa su
  gate; si no, colapsar o bloquear.
- Sol High insuficiente: usar Sol Max sólo con señal explícita del gate.
- Ningún par exacto fijable: no crear ni reconfigurar el descendiente.

No existe fallback silencioso. Toda sustitución permitida declara
`recommended ≠ effective`, causa y consecuencia. Nunca se cruza a Terra ni a
otro esfuerzo.

## Dos pasadas

```text
director_route = route(CEM_global_residual, available_triples)
SGM = design_graph(task)
integration_load = J(SGM)
director_route = adjust_pair(director_route, integration_load)
node_route_i = route(CEM_local_residual_i, available_triples_i)
```

La carga de integración puede mover `Luna max → Sol high → Sol max`; no crea
pares nuevos. Registrar sólo las bases que gobiernan una ruta fronteriza.

## Fuente y límite

- [Guía oficial GPT-5.6](https://developers.openai.com/api/docs/guides/latest-model):
  describe las familias y esfuerzos disponibles; la política de esta skill es
  más estrecha y prevalece para su uso.
- [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents).

Modelos, contratos de herramientas y disponibilidad cambian. Revalidar en vivo
y con evals representativas; no persistir precios ni rankings como umbrales.
