# Calibración y estatus epistémico

CEM-8, SGM-8 y S0–S9 son una rúbrica de ingeniería, no un predictor validado.
Los umbrales son hipótesis conservadoras. No atribuir ventaja a modelo,
esfuerzo o grafo sin comparar tareas y candidatos equivalentes.

## Comparaciones prioritarias

```text
Luna low vs Luna medium
Luna medium vs Luna high
Luna high vs Sol medium
Luna xhigh vs Sol medium, solo con oracle fuerte
Sol high vs Sol xhigh
Sol xhigh vs Sol max
Sol directora + Luna hojas vs todo Sol
S0 Sol vs Sol directora + Luna sidecars
S0 vs S2 estrella
S2 estrella vs S6 DAG contractual
sesión nueva vs sesión reutilizada
un escritor vs worktrees por dominios disjuntos
```

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
unobserved_model_rate
routing_regret
graph_regret
cost_degraded_fallback_rate
late_escalation_rate
human_major_correction_rate
```

`routing_regret` es el costo de la configuración elegida menos el costo de la
más barata que habría satisfecho calidad y seguridad. `graph_regret` es el
costo del grafo menos el costo de S0 cuando S0 habría alcanzado el mismo
resultado.

Medir acuerdo entre evaluadores al puntuar CEM y SGM. Desacuerdo recurrente en
una dimensión indica definición insuficiente, no error del evaluador.

## Experimentos

- Comunicación: mediación central vs peer edges contractuales.
- Independencia: candidatas aisladas vs comunicación temprana.
- Persistencia: sesión nueva vs reuso dentro del runtime observado.
- Profundidad: directora→hojas vs supervisoras con reducción local.
- Worktrees: solo tareas con escritores realmente concurrentes.

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
- [Models](https://developers.openai.com/api/docs/models)

Revalidar al cambiar modelos, esfuerzos, herramientas, permisos, límites de
concurrencia o semántica de lifecycle.
