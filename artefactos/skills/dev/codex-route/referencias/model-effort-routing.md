# Routing de modelo y esfuerzo

La selección de modelo es una decisión runtime y volátil. La skill recomienda;
solo configura un descendiente cuando `spawn_agent` expone ese valor.

## Gate de capacidad viva

Antes de emitir o ejecutar una asignación:

1. inspeccionar los modelos y esfuerzos permitidos por la superficie actual;
2. separar modelo recomendado, disponible y efectivamente usado;
3. si el recomendado no está disponible, escoger el fallback más cercano y
   declarar la pérdida;
4. omitir el override cuando heredar sea más fiel que inventar soporte;
5. no crear perfiles TOML ni cambiar configuración global salvo solicitud
   explícita.

La sesión directora activa normalmente no puede cambiarse desde una skill.
Presentar su modelo como `actual` y una alternativa como `recomendado`, no como
aplicada.

## Familia GPT-5.6 vigente al 2026-08-11

La documentación oficial distingue:

- `gpt-5.6` / `gpt-5.6-sol`: capacidad frontier para trabajo ambiguo,
  multietapa, con planificación, herramientas, validación e integración;
- `gpt-5.6-terra`: balance de capacidad, velocidad y costo; preferente para
  exploración, lectura amplia y workers que reducen resultados;
- `gpt-5.6-luna`: trabajo rápido, estrecho, repetible o de alto volumen.

No asumir que los tres están expuestos por cada cliente o herramienta. En la
superficie de esta autoría, `spawn_agent` expone Sol y Terra; por tanto Luna es
una recomendación condicionada, no un override ejecutable garantizado.

## Selección por trabajo

| Trabajo | Tier inicial |
|---|---|
| Búsqueda, mapeo, extracción, logs, corpus | Luna si está disponible; si no, Terra |
| Implementación con contrato estable | Terra medium/high |
| Arquitectura local o revisión adversarial | Sol medium/high |
| Diagnóstico, evidencia contradictoria, integración interdisciplinaria | Sol high/xhigh |
| Síntesis global extremadamente difícil y evaluable | Sol xhigh/max |

Escalar de tier cuando el fallo sea causal, arquitectónico o de integración.
No sustituir un modelo inadecuado aumentando esfuerzo indefinidamente.

## Esfuerzo

Usar `peak = max(A,N,E,O,C,J)` y contar cuántas de esas dimensiones son ≥3.

| Esfuerzo | Uso |
|---|---|
| low | Operación directa, oráculo exacto, velocidad prioritaria |
| medium | Default equilibrado para trabajo delimitado |
| high | Lógica compleja, edge cases, revisión o varios ciclos |
| xhigh | Varias dimensiones difíciles, riesgo o síntesis profunda |
| max | Problema quality-first excepcional, evaluable y esencialmente serial |

`max` no se justifica por archivos numerosos, logs extensos, duración o mala
especificación. Comparar `xhigh` y `max` sobre tareas representativas cuando el
costo importe.

## Ultra

Ultra es una política de ejecución, no una topología. Combina razonamiento
máximo y delegación proactiva cuando el producto/cliente lo soporta.

Recomendarla solo si la descomposición debe descubrirse dinámicamente, existe
paralelismo amplio, importa el tiempo de pared, el presupuesto tolera más
trabajo y las acciones están acotadas.

No recomendarla para grafo conocido, trabajo serial, escritura compartida,
riesgo alto, independencia cegada o presupuesto restringido. En Codex local,
la delegación sigue requiriendo solicitud directa o una instrucción aplicable;
no presentar la etiqueta Ultra como herramienta invocable si no existe.

## Fuentes oficiales consultadas

- [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Model guidance](https://developers.openai.com/api/docs/guides/latest-model)

Estas páginas describen capacidad del producto y recomendaciones actuales; no
prueban disponibilidad para una cuenta, cliente o turno específico.
