# CEM-8 — Cognitive and Epistemic Matrix

Usar esta matriz para seleccionar profundidad cognitiva, esfuerzo,
verificación y autonomía. Puntuar cada dimensión de 0 a 4 a partir de hechos de
la tarea. No promediar.

| Dimensión | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| A — Ambigüedad | Operación y resultado exactos | Objetivo claro, supuestos menores | Falta una decisión material | Varios resultados o trade-offs legítimos | Objetivo emergente, disputado o contradictorio |
| N — Novedad y abstracción | Ejecutar procedimiento | Aplicar patrón conocido | Combinar patrones | Derivar solución no evidente | Construcción teórica o problema frontera |
| E — Especialización | Conocimiento general | Un dominio habitual | Dominio especializado con fuentes | Expertise profundo o varias disciplinas | Varios dominios profundos, regulados o controvertidos |
| O — Debilidad del oráculo | Checker exacto | Tests o criterios fuertes | Objetivo más juicio acotado | Triangulación experta | Sin verificación directa o resultado disputado |
| B — Amplitud | Un dato o archivo | Pocos elementos | Varios archivos o fuentes | Subsistema o corpus grande | Sistema de sistemas o corpus masivo |
| C — Acoplamiento y dinamismo | Independiente | Dependencias locales estables | Varias interfaces | Feedback o cambio durante el trabajo | Sistema no estacionario, adversarial o muy interdependiente |
| H — Horizonte | Una respuesta | Pocos pasos | Un ciclo inspección–acción–verificación | Varios ciclos con objetivo estable | Programa adaptativo prolongado |
| R — Riesgo | Sin efectos externos | Local y reversible | Consecuencia relevante pero revisable | Alto impacto clínico, legal, financiero, operativo o reputacional | Daño grave, irreversible, sistémico o de seguridad |

## Fast path cognitivo

Tratar como tarea acotada sin desplegar la matriz completa cuando:

```text
A ≤ 1
N ≤ 2
E ≤ 2
O ≤ 1
C ≤ 2
```

y existen objetivo definido, resultado reconocible, fuente de verdad,
restricciones claras y ausencia de acción externa de alto impacto.

La amplitud por sí sola no exige el modelo más capaz. Una transformación de
muchos registros puede ser estrecha si el oráculo es exacto.

## Gate de capacidad frontier

Recomendar el tier más capaz disponible cuando se cumple alguna:

```text
A ≥ 2
N ≥ 3
E ≥ 3
C ≥ 3
O ≥ 2 con juicio sustantivo
R ≥ 3 con recomendación o decisión
```

También para descubrir el problema, arquitectura, integración
interdisciplinaria, diagnóstico, evidencia contradictoria, reconciliación de
interfaces o síntesis global.

No confundir este gate con autorización para actuar. Riesgo alto puede exigir
mejor razonamiento y simultáneamente menor autonomía.

## Verificación por perfil

| Señal | Verificación mínima |
|---|---|
| O 0–1 | Checker o test focal y candidato exacto |
| O 2 | Evidencia objetiva más revisión explícita del juicio |
| O 3–4 | Fuentes independientes, incertidumbre y adjudicador competente |
| R 0–1 | Loop local reversible |
| R 2 | Revisión de diff/resultado y rollback posible |
| R 3 | Gate humano antes del efecto; evidencia adversarial |
| R 4 | No ejecutar sin autoridad específica y controles del dominio |

## Regla de salida

Registrar el perfil como ocho enteros con una justificación breve para las
dimensiones que gobiernan la ruta. No fabricar precisión explicando cada cero
si el caso es obvio.
