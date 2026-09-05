# Calibración y estatus epistémico

CEM-8, SGM-8 y S0–S9 son rúbricas de ingeniería, no predictores validados. Los
umbrales son hipótesis conservadoras. No atribuir ventaja a un par o grafo sin
comparar tareas y candidatas equivalentes.

## Frontera de política

La política ratificada el 2026-08-23 reduce el experimento a:

```text
gpt-5.6-luna:max
gpt-5.6-sol:high
gpt-5.6-sol:max
```

Terra y todos los demás esfuerzos quedan fuera aunque el runtime los ofrezca.
La documentación oficial demuestra disponibilidad potencial, no autoriza su uso
en esta skill. Los análisis agregados previos que incluían Terra conservan valor
histórico para explicar la decisión, pero ya no gobiernan rutas ni evals.

## Comparaciones prioritarias

```text
Luna max vs Sol high por superficie donde ambos sean ejecutables
Sol high vs Sol max en tareas excepcionalmente difíciles
Sol directora + hojas Luna max vs todo Sol high
S0 Sol high vs Sol high + sidecars Luna max
S0 vs S2 estrella
S2 estrella vs S6 DAG contractual
sesión nueva vs sesión reutilizada
current_session vs subagent vs independent_thread
S0 vs S0 + goal nativo para objetivos durables
un escritor vs worktrees por dominios disjuntos
```

La primera comparación es privilegiada. Registrar el par descartado y su razón,
sin presumir dominancia. Si un gate Sol vuelve inelegible a Luna o una superficie
no expone uno de los pares, registrar la exclusión.

## Métricas

```text
éxito verificable
errores críticos
completitud
tokens, créditos y wall-clock
tiempo humano
defectos de integración
cambios fuera de alcance
pair_policy_compliance
execution_surface_compliance
unobserved_pair_rate
routing_regret
graph_regret
goal_regret
independent_thread_regret
pareto_dominated_route_rate
late_escalation_rate
human_major_correction_rate
```

`routing_regret` compara la ruta elegida con la más barata que habría satisfecho
calidad y seguridad dentro de la política. `graph_regret` compara con S0.
`goal_regret` compara con `S0 + goal`. Una ruta fuera de política no es una
candidata más barata: es inválida.

## Experimentos

- Comunicación: mediación central vs peer edges contractuales.
- Independencia: candidatas aisladas vs comunicación temprana.
- Superficie: subagente vs thread independiente con igual contrato y oráculo.
- Goal: grafo efímero vs `S0 + goal` con igual condición de término.
- Worktrees: checkout local vs worktree sólo con escritores concurrentes.

Medir latencia, mensajes, duplicación, conflictos, tiempo de integración y
calidad global. Una demo, configuración, ruta propuesta o paridad de archivos no
prueba generalización, seguridad, aceptación ni ventaja costo/calidad.

## Función objetivo

```text
minimizar costo total dentro de los tres pares permitidos
sujeto a calidad >= umbral y seguridad >= umbral
```

No maximizar sesiones, paralelismo ni esfuerzo. Cada ruta declara
`cheaper_route_not_used` o reconoce que no descartó una alternativa permitida
más barata.

## Fuentes a revalidar

- [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees)
- [Projects and chats](https://learn.chatgpt.com/docs/projects)
- [Follow goals](https://learn.chatgpt.com/use-cases/follow-goals)
- [Using GPT-5.6](https://developers.openai.com/api/docs/guides/latest-model)

Revalidar al cambiar modelos, esfuerzos, herramientas, permisos, límites de
concurrencia o semántica de lifecycle.
