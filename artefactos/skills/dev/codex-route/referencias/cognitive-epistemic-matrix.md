# CEM-8 — complejidad cognitiva y epistémica residual

Puntuar de 0 a 4 después de usar fuente de verdad, contrato vigente o una
aclaración acotada. La unidad es la tarea global para la directora y cada
subtrabajo local para su sesión. Medir complejidad residual, no dificultad
inicial del prompt. No promediar.

| Dimensión | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| A — Ambigüedad | Operación exacta | Supuestos menores | Decisión material acotada | Varios resultados legítimos | Objetivo emergente o contradictorio |
| N — Novedad | Procedimiento | Patrón conocido | Combinar patrones | Solución no evidente | Construcción frontera |
| E — Especialización | General | Dominio habitual | Fuente especializada | Expertise profundo | Varios dominios profundos |
| O — Debilidad del oráculo | Checker exacto | Tests fuertes | Juicio acotado | Triangulación experta | Sin verificación directa |
| B — Amplitud | Un dato | Pocos elementos | Varios archivos | Subsistema/corpus | Sistema de sistemas |
| C — Acoplamiento | Independiente | Dependencias locales | Varias interfaces | Feedback durante trabajo | Interdependencia no estacionaria |
| H — Horizonte | Una respuesta | Pocos pasos | Un loop completo | Varios loops | Programa adaptativo |
| R — Riesgo | Sin efecto | Local reversible | Relevante revisable | Alto impacto | Daño grave o irreversible |

## Fast path cognitivo

No desplegar la matriz completa si existe objetivo, entregable, fuente,
restricción y checker claros, y se cumple:

```text
A ≤ 1 · N ≤ 2 · E ≤ 2 · O ≤ 1 · C ≤ 2
```

La amplitud no exige por sí sola un modelo más capaz.

## Gate de Luna

Luna exige todas:

- objetivo local y entregable determinados;
- método conocido o búsqueda acotada;
- fuente de verdad identificada;
- oráculo fuerte;
- integración local baja;
- ningún juicio material de alta consecuencia pendiente.

## Gate obligatorio de Sol

Sol exige cualquiera:

- ambigüedad residual material;
- arquitectura, invariantes o novedad conceptual;
- síntesis interdisciplinaria o evidencia contradictoria;
- oráculo débil con juicio sustantivo;
- acoplamiento o integración difícil;
- recomendación de alta consecuencia;
- adjudicación entre resultados rivales.

## Riesgo, autonomía y verificación

`R gobierna autonomía y verificación` antes que modelo o esfuerzo. Solo elevar
capacidad cognitiva si el riesgo contiene juicio sustantivo.

| Señal | Verificación mínima |
|---|---|
| O 0–1 | checker/test focal y candidato exacto |
| O 2 | evidencia objetiva más revisión del juicio |
| O 3–4 | fuentes independientes, incertidumbre y adjudicación competente |
| R 0–1 | loop local reversible |
| R 2 | revisión y rollback posible |
| R 3 | gate humano antes del efecto y evidencia adversarial |
| R 4 | no ejecutar sin autoridad y controles de dominio |

## Salida

En rutas obvias, emitir solo `cognitive_class` y `routing_basis`. Mostrar los
ocho enteros únicamente si una dimensión gobierna una decisión fronteriza o el
usuario pide `FULL_GRAPH_ROUTE`.
