
# ship-discipline

## Proposito

Procedimiento para llevar un encargo de software a un incremento utilizable,
comprobado e integrado dentro de su alcance. Comprende consecuencias y
recuperación, decide cómo ejecutar y verifica el resultado antes de cerrarlo.

La inspiración en prácticas de Peter Steinberger conserva descubrimiento
iterativo, dirección humana y ejecución asistida. Es una interpretación de
trabajo situada, no evidencia de que una topología o herramienta sea superior
para todo encargo.

## Cuando Usar

- el agente va a modificar codigo y se necesita decidir topologia
  (secuencial cuidadoso, paralelo moderado, maximo paralelismo).
- una tarea cambia archivos y antes de declararla hecha debe cerrar el
  loop con evidencia proporcional al riesgo y a la aceptacion.
- se va a estructurar un repositorio para que sea agent-friendly o se
  detecta que un repo existente penaliza a los agentes.
- hay que distinguir lo que puede resolver el agente de lo que requiere una
  decisión del operador.
- se va a producir CLI, MCP o tooling reusable: sube el rigor.
- el contexto del modelo se esta ensuciando y hay que podar.

## Cuando NO Usar

- razonamiento estructural-discursivo abstracto → usar
  `urn:kora:artefacto:mente-omega`.
- enmarque categorial puro → usar `urn:kora:artefacto:cat-thinking`.
- autoría o instalación de productos KORA → usar `autoria-kora` o
  `instalacion-kora`, con la guía operativa de la fuente vigente.
- diseno de celulas humano-agente organizacionales → usar
  `urn:fxsl:artefacto:cell-design`.

## Workflow

### `triaje`

Aclara con el contexto disponible, sin imponer un cuestionario:

1. **Hay codigo a producir/modificar?** Si no, declinar la skill.
2. **Cuanto sabe el operador del cambio?** (idea borrosa vs requerimiento concreto vs spec completa)
3. **Que tipo de cambio es?** (feature, refactor, fix, cleanup, tooling reusable)

### `estimar-blast-radius`

Identificar qué conducta, datos, consumidores e interfaces puede afectar el
cambio y cómo recuperar el estado anterior. El número de archivos orienta la
inspección, pero no determina riesgo ni crea una aprobación pendiente.

Ejecutar directamente cuando el alcance y la reversión sean claros. Si hay
acoplamientos o incertidumbre material, ordenar el cambio y comprobar primero
la condición que pueda invalidarlo. Ampliar las pruebas según las consecuencias
de un fallo. Un cambio de schema o dependencia puede necesitar ensayo de
compatibilidad; un cambio documental puede alterar una instrucción decisiva.

Conservar la autorización ya concedida. Consultar al operador cuando una
decisión exceda el encargo o falte una preferencia que cambie materialmente el
resultado; mientras tanto, completar lo independiente que siga siendo útil.
Explicar el riesgo relevante cuando ayude a revisar o continuar el trabajo.

Detalle en `referencias/blast-radius-checklist.md`.

### `decidir-topologia`

Decide por independencia, costo de coordinación, contexto y riesgo de conflicto.
Estas opciones orientan cuando repartir el trabajo aporta valor. Una sesión
puede cerrar el encargo completo; el paralelismo depende de tareas independientes
y de la autoridad vigente.

| Tipo de trabajo | Topologia |
|---|---|
| Pasos dependientes | Ejecución secuencial que conserve contexto |
| Porciones independientes y autoridad de delegación | Paralelismo acotado con propiedad explícita |
| Refactor pesado o cambios con alto conflicto | Secuencial cuidadoso |
| Múltiples resultados independientes | Repartir sólo cuando reduzca trabajo total o mejore evidencia |

### `ejecutar-o-delegar`

**Decisiones que conserva el operador**:

- propósito, prioridades y aceptación personal del resultado;
- cambios de alcance, costo o efectos que el encargo no autoriza;
- preferencias de producto que no pueden resolverse con el contexto disponible.

El agente puede concretar arquitectura, dependencias, schemas, nombres y diseño
dentro de un encargo que le otorgue esa responsabilidad. Presenta sus decisiones
y evidencia sin atribuir al operador una aceptación que no observó.

**Trabajo que puede delegarse**, con herramientas reales y autorización aplicable:

- escribir, transformar, mover, refactorizar
- generar, probar, repetir hasta verde
- shaping mecanico de codigo

Detalle en `referencias/separacion-estratos.md`.

### `cerrar-loop`

Una tarea **NO** esta lista hasta que la aceptacion y los riesgos reales estan
cubiertos sobre el arbol exacto:

1. **Comportamiento** — verificar el outcome o journey solicitado.
2. **Checks aplicables** — ejecutar primero la prueba focal; ampliar a build,
   tests, typecheck, lint o integracion solo cuando existen y el cambio puede
   afectarlos.
3. **Estado honesto** — un `FAIL` relevante bloquea. `ABSENT` o `NOT_RUN` no
   aportan evidencia: si el check cubre aceptacion o un riesgo real, bloquean;
   si no, se declaran sin inventar tooling.
4. **Feel** — usar o revisar la solucion; no basta con que compile.
5. **Patch listo** — cambio coherente y verificable; commit solo autorizado.

Detalle en `referencias/loop-closure-checklist.md`.

### `cierre`

Reportar:

- blast radius estimado y topologia elegida,
- cambio aplicado con paths,
- loop cerrado con las comprobaciones aplicables y su estado,
- patch listo o commit hash autorizado,
- siguiente paso si la tarea es multi-incremento.

## Reglas Duras

1. **Blast radius antes de exec**.
2. **Cierre comprobado**: aceptación + pruebas proporcionales + integración;
   commit y publicación según la autoridad vigente del encargo.
3. **Ship beats perfect**: util hoy > ideal hipotetico.
4. **Architecture over implementation**: resolver las decisiones que gobiernan
   el cambio antes de multiplicar implementación.
5. **Less is more**: cada capa justifica existencia.
6. **Just talk to it**: prompts cortos, lenguaje natural.
7. **Context cost**: poda lo que no aporta.
8. **Autoridad del encargo**: ejecutar lo autorizado y devolver al operador las
   decisiones materiales que excedan ese alcance.
9. **Sube rigor cuando produces tooling reusable** (CLI, MCP, lib).
10. **No invadir dominio**: la skill da disciplina, no semantica del campo.

## Anti-patrones

| Anti-patron | Falla | Correccion |
|---|---|---|
| Prompt charade | Sustituye claridad por teatro | Just talk to it; prompt corto |
| MCP para todo | Costo permanente de contexto | CLI cuando alcanza |
| Worktrees por rutina | Carga sin necesidad de aislamiento | Elegir checkout por conflictos, reversión y reglas del repositorio |
| Subagent soup | Empaqueta complejidad manejable | Una sesion |
| Background-first | Pierde steerability | Foreground por defecto |
| Spec completa antes de tocar sistema | No calza con descubrimiento iterativo | Prototipar temprano |
| Revisar sólo el volumen de código | Omite comportamiento o consumidores decisivos | Inspeccionar lo necesario para comprobar aceptación, seguridad e integración |
| Loop abierto | Tarea declarada hecha sin evidencia aplicable | Cerrar siempre |

## Composicion con otras skills

| Composable con | Cuando |
|---|---|
| `urn:kora:artefacto:mente-omega` | la decision de arquitectura requiere razonamiento estructural-discursivo previo |
| `urn:kora:artefacto:cat-thinking` | la composicion del repo o la integracion entre subsistemas tensiona y se necesita lectura categorial |
| `urn:kora:artefacto:autoria-kora` | se va a producir o actualizar la fuente de un agente o skill KORA |
| `urn:kora:artefacto:instalacion-kora` | se van a mantener realizaciones de KORA en Codex o Hermes |

## Recursos

### Referencias

- `referencias/blast-radius-checklist.md` — checklist de estimacion +
  consecuencias + recuperación.
- `referencias/loop-closure-checklist.md` — pasos del loop, gotchas y
  reglas.
- `referencias/repo-shaping-checklist.md` — checklist agent-friendly:
  estructura, naming, docs, CLI, ejemplos.
- `referencias/separacion-estratos.md` — decisiones y responsabilidades según
  el encargo del operador.

## Salida Esperada

- diagnostico de tarea + tipo de cambio,
- blast radius estimado con topologia,
- decision de delegacion humano/agente declarada,
- cambio aplicado,
- loop cerrado con evidencia proporcional y estados honestos,
- siguiente paso operativo.
