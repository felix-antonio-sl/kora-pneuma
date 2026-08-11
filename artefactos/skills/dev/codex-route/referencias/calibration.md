# Calibración y estatus epistémico

CEM-8, SGM-8 y S0–S9 son una rúbrica de ingeniería, no un predictor validado.
Los umbrales son hipótesis conservadoras. No atribuir ventaja a modelo,
esfuerzo o grafo sin comparar tareas y candidatos equivalentes.

## Lectura de la evidencia 2026-08-11

La guía oficial caracteriza Sol como capacidad frontera, Terra como balance
capacidad–costo y Luna como opción eficiente para alto volumen. Los tres
gráficos Artificial Analysis aportados por el operador muestran dos hechos que
deben conservarse juntos: a igual esfuerzo el índice agregado suele ordenar
Sol, Terra y Luna; al comparar costo entre **pares modelo–esfuerzo**, una Luna
con más esfuerzo o una Sol con menos esfuerzo puede dominar a Terra. El
análisis publicado por Artificial Analysis declara a Terra dominada en su
Intelligence Index agregado por algún par Luna/Sol.

Consecuencia: Terra entra a la allowlist por su rol oficial, disponibilidad
runtime y posible ventaja local, pero no como escalón ordinal obligatorio. Los
índices agregados no representan el workload local, cambian en el tiempo y no
prueban costo del runtime Codex. No persistir sus cifras como umbrales.

## Comparaciones prioritarias

```text
Luna max vs Sol high por cada superficie donde ambos sean ejecutables
Luna low/medium/high vs Terra low/medium, incluidos esfuerzos adyacentes
Luna high/xhigh/max vs Terra medium/high
Terra medium/high/xhigh vs Sol low/medium/high
Terra max vs Sol medium/high
Sol high vs Sol xhigh vs Sol max
Sol directora + hojas Luna/Terra vs todo Sol
S0 Sol vs Sol directora + sidecars Luna/Terra
S0 vs S2 estrella
S2 estrella vs S6 DAG contractual
sesión nueva vs sesión reutilizada
current_session vs subagent vs independent_thread
S0 vs S0 + goal nativo para objetivos durables
un escritor vs worktrees por dominios disjuntos
```

La primera comparación es privilegiada por la hipótesis de relación
desempeño–costo señalada por el operador. Debe informar el par descartado y su
razón, pero no presume dominancia: requiere eval representativa local y costo
total comparable. Si un gate Sol vuelve inelegible a Luna o una superficie no
expone uno de los pares, registrar la exclusión en vez de fingir el experimento.

## Métricas de resultado y política

```text
éxito verificable
errores críticos
completitud
tokens, créditos y wall-clock
tiempo humano
defectos de integración
cambios fuera de alcance
model_policy_compliance
execution_surface_compliance
unobserved_model_rate
routing_regret
graph_regret
goal_regret
independent_thread_regret
pareto_dominated_route_rate
cost_degraded_fallback_rate
late_escalation_rate
human_major_correction_rate
```

`routing_regret` es el costo de la configuración elegida menos el costo de la
más barata que habría satisfecho calidad y seguridad. `graph_regret` es el
costo del grafo menos el costo de S0 cuando S0 habría alcanzado el mismo
resultado. `pareto_dominated_route_rate` cuenta rutas cuyo par elegido fue
dominado por otro par ejecutable bajo evidencia representativa disponible.
`goal_regret` compara la ruta con `S0 + goal`; `independent_thread_regret`
incorpora dirección, seguimiento e integración, no solo inferencia.

Medir acuerdo entre evaluadores al puntuar CEM y SGM. Desacuerdo recurrente en
una dimensión indica definición insuficiente, no error del evaluador.

## Experimentos

- Comunicación: mediación central vs peer edges contractuales.
- Independencia: candidatas aisladas vs comunicación temprana.
- Persistencia: sesión nueva vs reuso dentro del runtime observado.
- Superficie: subagente vs thread independiente con el mismo contrato y oráculo.
- Goal: grafo efímero vs `S0 + goal` con igual condición de término.
- Profundidad: directora→hojas vs supervisoras con reducción local.
- Worktrees: checkout local vs worktree solo con escritores concurrentes.

Medir latencia, mensajes, duplicación, anclaje, conflictos, merges, pérdida de
contrato, tiempo de integración y calidad global.

## Función objetivo

```text
minimizar costo total
sujeto a calidad ≥ umbral y seguridad ≥ umbral
```

No maximizar sesiones, paralelismo, mensajes ni esfuerzo. Cada ruta debe
declarar `cheaper_route_not_used` o reconocer que no descartó una alternativa
más barata.

## Evidencia mínima de una ejecución

- preflight vivo y configuración efectiva observable;
- árbol y sesiones realmente creadas;
- paquetes, resultados y bloqueos por nodo;
- integración y verificación del objetivo global;
- límites de inferencia.

Una demo, un log, una configuración o paridad de archivos no prueba
generalización, seguridad, aceptación ni ventaja costo/calidad.

## Fuentes a revalidar

- [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees)
- [Projects and chats](https://learn.chatgpt.com/docs/projects)
- [Follow goals](https://learn.chatgpt.com/use-cases/follow-goals)
- [Models](https://developers.openai.com/api/docs/models)
- [Using GPT-5.6](https://developers.openai.com/api/docs/guides/latest-model)
- [Artificial Analysis: Sol, Terra y Luna](https://artificialanalysis.ai/articles/gpt-5-6-intelligence-vs-cost-across-sol-terra-luna)

Revalidar al cambiar modelos, esfuerzos, herramientas, permisos, límites de
concurrencia o semántica de lifecycle.
