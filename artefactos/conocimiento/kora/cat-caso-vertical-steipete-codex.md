---
urn: urn:kora:kb:cat-caso-vertical-steipete-codex
nombre: cat-caso-vertical-steipete-codex
version: 1.5.0
estado: deprecado
descripcion: "Antecedente deprecado del caso Steipete sobre Codex CLI: conserva las conclusiones válidas de una observación runtime finita sin mantener monitores ni gates versionados en la suite general."
fuente: "Doctrina propia pneuma iniciada el 2026-07-19 desde urn:dev:artefacto:steipete y urn:kora:kb:cat-contrato-ingenieria-agentica. El caso observó Codex CLI 0.144.6 y App Server 0.144.3 mediante trazas y contratos locales. Deprecado por decisión de simplificación monooperador del 2026-08-09: el mecanismo quedó acoplado a versiones y marcadores efímeros y su costo en la suite general excedía la evidencia vigente. Git conserva el desarrollo y los testigos retirados."
autor: FS
creado: 2026-07-19
lang: es
tags: [ingenieria-agentica, codex, steipete, evidencia-runtime]
familia: bok
depende: [urn:dev:artefacto:steipete, urn:dev:artefacto:ship-discipline, urn:kora:kb:cat-contrato-ingenieria-agentica, urn:kora:kb:cat-agent-coalgebra]
---

# Caso vertical Steipete en Codex — deprecado

## Resultado histórico

El caso observó una ejecución acotada de Steipete sobre una versión concreta
de Codex. Una traza local satisfizo un monitor de loop closure y otra mostró
que la autoridad efectiva no podía deducirse solo desde las herramientas
declaradas en la fuente.

La evidencia permitía afirmar únicamente:

- una traza finita aceptada no cuantifica ejecuciones futuras;
- configuración, capacidad declarada y efectos runtime son capas distintas;
- un contrato endurecido prueba su propio recibo, no safety universal;
- `Spec`, `Model` y `Runtime` no se sustituyen entre sí.

## Motivo de deprecación

El monitor, los probes de autoridad y sus tests quedaron ligados a versiones,
markers y respuestas locales ya históricas. Ejecutarlos en cada cambio del
repositorio no reducía un riesgo vigente del núcleo KORA y convertía una
observación puntual en ceremonia permanente.

No queda un helper activo asociado a este URN. Git conserva el antecedente.

## Regla que permanece

Cuando una decisión real requiera evidencia runtime, el testigo debe vivir
junto al runtime consumidor, declarar versión, entrada, salida, autoridad e
invariante, y ejecutarse focalmente. No se incorpora a la suite general por el
solo hecho de haber sido útil una vez.
