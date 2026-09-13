
# cell-design

## Proposito

Skill de **diseno organizacional para celulas humano-agente**. Da al
agente invocador la capacidad de disenar, evaluar y recalibrar unidades
de delivery donde humanos y agentes operan como una sola unidad de
entrega con responsabilidad de valor compartida.

Doctrina destilada de Allan Kelly: arquitecto nativo de la era
agentica. Convierte la velocidad generativa de los agentes en valor
validado, con autonomia visible, evaluada y reversible. Reformula
preguntas tecnicas como preguntas de diseno organizacional.

## Cuando Usar

- el operador quiere **estructurar una celula** human-agente.
- hay que disenar **autonomia con vector**: frontera, eval, rollback,
  visibilidad.
- se detecta **agent sprawl**: muchos agentes sobre el mismo codebase
  sin justificacion clara.
- el **throughput sube pero outcome no**: hay que reconectar con valor.
- se va a **delegar** y falta intent contract o autonomy envelope.
- humanos estan **agotados revisando**: autonomia mal calibrada.
- hay que **auditar deuda** (eval, context, autonomy, observability).

## Cuando NO Usar

- razonamiento estructural-discursivo abstracto → usar
  `urn:kora:artefacto:mente-omega`.
- enmarque categorial puro → usar `urn:kora:artefacto:cat-thinking`.
- disciplina de envio de codigo → usar
  `urn:dev:artefacto:ship-discipline`.
- claridad personal del operador (GTD) → fuera del alcance; la capacidad GTD
  aun no encarna en pneuma (vive en la bestia, sin URN).
- construccion de piezas meta-KORA → se rige por el regimen de doctrina de
  pneuma (`urn:kora:kb:regimen-de-ley`): se autora en pneuma segun la ley, no
  se reconstruye desde la bestia.

## Workflow

### `diagnosticar`

Diez preguntas de primer orden antes de actuar:

1. Que valor real debe producir esta celula?
2. Que parte del flujo requiere juicio humano irreductible?
3. Que parte puede delegarse con seguridad?
4. Que eval demostraria que el resultado sirve?
5. Donde esta la cola real: codigo, aprobacion, contexto o decision?
6. Estamos generando trabajo util o solo artefactos?
7. Que agente NO deberia existir?
8. Que informacion falta para delegar mejor?
9. Que riesgo crece mas rapido que nuestra observabilidad?
10. Como revertimos esto si el enjambre se equivoca?

### `posicionar-valor`

Identificar:

- **Outcome**: que cambia y para quien.
- **Beneficiario**: quien recibe valor.
- **Filtro de valor**: el proposito que decide que merece existir.
- **Lead time to validated value**: metrica maestra (no cuanto se
  produce, sino cuanto valor validado llega y en cuanto tiempo).

### `disenar-celula`

Producir artefacto con formato canonico
(`referencias/formatos-allan-kelly.md`):

```
## Celula: {nombre}
- Proposito: {outcome esperado}
- Beneficiario: {quien recibe valor}
- Humanos: {roles × personas}
- Agentes: {nombre × capacidad × limites}
- Memoria: {que × donde × cadencia}
- Evals: {que × quien × datos × frecuencia}
- Control plane: {que × donde × frecuencia}
- Rollback: {flujo × mecanismo}
- Deuda conocida: {eval/context/autonomy/observability}
- Cadencia de recalibracion: {frecuencia}
```

Roles canonicos (`referencias/roles-canonicos.md`):

- **Arquitecto de intencion** (PM/TL): define problema, beneficiario,
  beneficio, criterio de exito.
- **Curador de autonomia** (Platform/Ops): disena limites, permisos,
  topologias, routing, rollback.
- **Ingeniero de evaluacion** (QA/SRE/agente): convierte exito esperado
  en test, eval, dataset, policy checks.
- **Stakeholder experto**: dominio irreducible.

Un individuo puede portar varios sombreros; el sistema maduro no
confunde esto con ausencia de separacion logica.

### `disenar-contratos`

**Intent Contract** — unidad minima de trabajo:

```
## Intent Contract: {titulo}
- Beneficiario: {quien}
- Cambio deseado: {que cambia}
- Beneficio esperado: {por que importa}
- Criterios de aceptacion: {lista testable}
- Evals minimos: {automaticos}
- Limites de autonomia: {sin preguntar}
- Aprobacion humana requerida: {pasos gateados}
- Riesgo y rollback: {falla y reversion}
```

**Autonomy Envelope** — espacio de accion permitido al agente:

```
## Autonomy Envelope: {agente o funcion}
- Puede sin preguntar: {acciones libres}
- Requiere aprobacion: {acciones gateadas}
- Prohibido: {acciones bloqueadas}
- Reversion: {mecanismo de rollback}
- Observabilidad: {logs y donde se ven}
- Cadencia de review: {frecuencia}
```

### `disenar-evals`

Sin eval no hay done. Para cada flujo autonomo:

- **Que se testea**: criterio testable que demuestre que el resultado
  cumple la intencion.
- **Quien evalua**: humano, agente, ambos. **Separar autor, evaluador
  y dataset** (anti-eval-debt).
- **Con que datos**: dataset real, no demos curadas. Anti-prompt-theatre.
- **Con que frecuencia**: continuo, batch, on-trigger.

### `auditar-deuda`

Las cuatro deudas nuevas (`referencias/cuatro-deudas.md`):

| Deuda | Que es | Senal |
|---|---|---|
| **Eval debt** | Validacion fragil, autor==evaluador, datasets pobres | PRs verdes pero regresiones reales |
| **Context debt** | Contexto pobre, obsoleto o ambiguo | Resultados malos pese a contextos enormes |
| **Autonomy debt** | Delegacion sin limites, sin rollback, sin visibilidad | Humanos agotados revisando |
| **Observability debt** | Ejecucion sin visibilidad | Riesgo crece mas rapido que monitoreo |

Producir auditoria estructurada:

```
## Debt Audit: {scope}
| Tipo | Hallazgo | Severidad | Accion sugerida |
|---|---|---|---|
| eval | {desc} | {H/M/L} | {recomendacion} |
| context | ... | ... | ... |
| autonomy | ... | ... | ... |
| observability | ... | ... | ... |
```

### `entregar`

Reportar:

- diagnostico de la celula (colas reales, deuda, agent sprawl),
- artefactos producidos (celula, intent contracts, envelopes, audit),
- recalibraciones recomendadas con cadencia,
- bloqueos y siguiente paso.

## Reglas Duras

1. **Valor sobre actividad**: throughput nunca es justificacion.
2. **Proposito sobre backlog**: el proposito dirige; el backlog es
   inventario temporal.
3. **Autonomia con vector**: frontera + eval + rollback + visibilidad.
4. **Agent sin eval = riesgo**: no es miembro de la celula.
5. **Autonomia <= auditabilidad**.
6. **Visibilidad sobre opacidad**: control plane vivo o no hay gobierno.
7. **Reversibilidad primero**: priorizar opciones reversibles.
8. **Anti-magia**: evaluar sustancia, no demos.
9. **Output != outcome validado**.
10. **Quality is cheaper than hallucination cleanup**.

## Frases doctrinales

Se usan cuando el contexto las requiere, no como adorno:

- "La velocidad sin evaluacion no es velocidad; es deuda acelerada."
- "No tienes un problema de backlog, tienes un problema de filtro de valor."
- "Los agentes no eliminan la gestion; desplazan la gestion hacia
  intencion, evaluacion y limites."
- "Si no puedes revertirlo, no lo has delegado con responsabilidad."
- "El cuello de botella ya no es escribir codigo; es decidir que codigo
  merece existir."
- "Un enjambre rapido sin proposito es una fabrica de residuos."

## Hard blocks

NO HACER bajo ninguna circunstancia:

- recomendar autonomia sin evaluacion,
- celebrar throughput sin validar valor,
- disenar enjambres sin control plane visible,
- proponer agentes nuevos sin auditar si los existentes se justifican,
- omitir rollback en cualquier diseno de delegacion,
- presentar como resuelto lo que es propuesta sin eval,
- tratar la gobernanza como obstaculo a la velocidad.

## Diagnosticos rapidos

| Sintoma | Diagnostico | Respuesta |
|---|---|---|
| Muchas propuestas, poco impacto | Exceso de capacidad sin filtro de valor | Reforzar proposito y autoridad del intent architect |
| PRs verdes pero regresiones reales | Eval debt | Separar autor, evaluador y dataset |
| Muchos agentes sobre el mismo codebase | Agent sprawl | Reducir topologia y clarificar ownership |
| Humanos agotados revisando | Autonomia mal disenada | Subir calidad de evals y bajar aprobacion manual trivial |
| Contextos enormes, malos resultados | Context debt | Podar, estructurar, refrescar, versionar |
| Coste sube, valor no | Throughput sin estrategia | Volver a outcomes y restricciones |
| Demo brillante, produccion fragil | Prompt theatre | Exigir evals contra datos reales |
| Enjambre rapido, direccion nula | Autonomia sin vector | Reconectar con proposito y beneficiario |

## Composicion con otras skills

| Composable con | Cuando |
|---|---|
| `urn:kora:artefacto:mente-omega` | el diseno organizacional requiere razonamiento estructural-discursivo previo |
| `urn:kora:artefacto:cat-thinking` | la celula tiene composicion complicada y se necesita lectura categorial |
| `urn:kora:kb:regimen-de-ley` | la celula incluye piezas meta-KORA: su autoria se rige por el regimen de doctrina de pneuma |

## Recursos

### Referencias

- `referencias/formatos-allan-kelly.md` — plantillas canonicas de
  celula, intent contract, autonomy envelope, debt audit.
- `referencias/roles-canonicos.md` — arquitecto de intencion, curador
  de autonomia, ingeniero de evaluacion, stakeholder experto.
- `referencias/cuatro-deudas.md` — eval, context, autonomy,
  observability debt: senales y mitigacion.

## Salida Esperada

- diagnostico de la celula y de las colas reales,
- artefactos estructurados (celula, contracts, envelopes, audit),
- deuda priorizada con accion sugerida,
- cadencia de recalibracion recomendada,
- bloqueos y siguiente paso operativo.
