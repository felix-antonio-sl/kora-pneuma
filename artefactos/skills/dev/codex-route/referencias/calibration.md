# Calibración y estatus epistémico

## Estatus

CEM-8, SGM-8 y S0–S9 son una rúbrica de ingeniería informada por capacidades
observadas y documentación oficial. No son una escala psicométrica ni un
predictor validado. Los umbrales iniciales son hipótesis conservadoras.

No atribuir una mejora al modelo, esfuerzo, topología o comunicación sin una
comparación sobre candidatos y tareas equivalentes.

## Comparaciones prioritarias

1. S0 monosession vs S2 estrella.
2. S2 estrella vs S6 DAG contractual.
3. S4 aislado vs hipótesis con comunicación temprana.
4. S7 map-reduce vs lectura monolítica.
5. S9 con checkout compartido vs aislamiento por dominio de escritura.
6. sesión nueva vs sesión reutilizada.
7. profundidad uno vs supervisoras de profundidad dos.
8. `xhigh` vs `max` en tareas quality-first con evaluador fuerte.

## Experimentos

### Comunicación lateral

Comparar mediación exclusiva de directora contra aristas peer sobre
dependencias. Medir latencia, mensajes, pérdida de contrato, bloqueos, errores
de integración, costo y duplicación.

### Independencia epistemológica

Comparar candidatas aisladas contra candidatas comunicadas. Medir diversidad,
cobertura, errores correlacionados, anclaje y calidad de adjudicación.

### Persistencia local

Comparar sesión nueva contra reutilizada. Medir tokens de reorientación,
supuestos obsoletos, continuidad, tiempo y errores por contexto heredado.

### Profundidad

Comparar directora→hojas contra directora→supervisoras→hojas. Medir carga de
integración central, pérdida durante reducción, tiempo, mensajes y calidad.

### Worktrees

Comparar solo en tareas de escritura. Medir conflictos, merges, tiempo de
integración, pruebas rotas, cambios fuera de alcance y reversibilidad.

## Métricas globales

```text
éxito verificable
errores críticos
completitud
tokens y créditos
wall-clock y tiempo humano
sesiones creadas y profundidad
mensajes y duplicación
defectos de integración
cambios fuera de alcance
intervenciones humanas
```

Función objetivo:

```text
minimizar costo total
sujeto a calidad ≥ umbral y seguridad ≥ umbral
```

No maximizar sesiones, mensajes, paralelismo ni esfuerzo.

## Evidencia mínima de una ruta ejecutada

- árbol y sesiones realmente creadas;
- paquetes entregados;
- modelo/esfuerzo efectivos cuando sean observables;
- resultados y bloqueos por nodo;
- candidato y write sets finales;
- integración en la directora;
- verificación del objetivo global;
- límites de inferencia.

Una demo, un log o una paridad de configuración no prueba generalización,
seguridad, aceptación humana ni ventaja costo/calidad.

## Fuentes de capacidad

- [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees)
- [Model guidance](https://developers.openai.com/api/docs/guides/latest-model)

Revalidar estas fuentes cuando cambien modelos, niveles de razonamiento,
permisos, herramientas, límites de concurrencia o semántica de sesiones.
