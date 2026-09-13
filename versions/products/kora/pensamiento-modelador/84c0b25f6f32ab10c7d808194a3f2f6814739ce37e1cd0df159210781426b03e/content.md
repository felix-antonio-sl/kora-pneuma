
# pensamiento-modelador

## Proposito

Skill de **pensamiento modelador**. Dota al agente —o al operador— de la
capacidad de leer cualquier acto de modelado como **navegacion explicita de
tensiones**: nombrar la tension en juego, ver sus dos polos, declarar el
criterio y elegir con su por-que.

No es una skill de construccion ni de ejecucion: no dibuja diagramas, no
escribe DDL, no serializa. Es una skill **introspectiva** anclada al marco de
las 52 tensiones (`urn:fxsl:kb:tensiones-modelamiento`), en tres capas
anidadas:

```text
A  sustantivas   (que debe decidirse)        las resuelve el formalismo
B  praxis        (como decide el modelador)   las navega el modelador
C  contexto      (que modula)                 modula profundidad, no correccion
```

Conviccion rectora: **un formalismo es un sistema de resoluciones congeladas
de las tensiones sustantivas**; las de praxis y contexto no las resuelve ningun
formalismo —las navega el modelador, nombrandolas—. Resolver una tension por
inercia puede ocultar una decisión relevante. Este marco es una lente de análisis,
no una prueba de negligencia ni una taxonomía universal: usa sólo las tensiones
que cambien la comprensión o la decisión.

## Cuando Usar

- **destrabar una decision de modelado**: convertirla en tension explicita
  (polos, pregunta, criterio, eleccion).
- **diagnosticar** que tensiones estan en juego en un acto de modelado o en un
  modelo ya construido.
- detectar **tensiones resueltas por inercia** (un polo elegido sin criterio).
- **elegir o comparar formalismos** leyendo que tensiones sustantivas congela
  cada uno (ERD, BPMN, OWL, state machines, OPM, IFML).
- **calibrar profundidad** por contexto (capa C) sin romper la correccion.

## Cuando NO Usar

- **ejecutar la mecanica de un formalismo** (construir el OPD, dibujar el ERD,
  escribir el DDL, axiomatizar el OWL) → derivar al especialista. Para OPM:
  `urn:kora:artefacto:modelamiento-opm`.
- **consultoria del dominio** del sistema (medicina, derecho, finanzas) →
  delegar al agente de dominio. La skill razona la forma, no la verdad del
  dominio.
- **decision arbitraria** sin estructura de modelado (ruido, gusto puro) →
  declarar que no aplica y declinar.
- cuando un agente ya conduce el modelado con su propia disciplina y solo falta
  la mecanica (p. ej. `dov-dori` para OPM): esta skill aporta la lente, no
  reemplaza al conductor.

## Anclaje a la SSOT

La SSOT es el kb `urn:fxsl:kb:tensiones-modelamiento` (las 52 tensiones, sus
polos y preguntas, en tres capas). La skill lo consulta en tiempo de ejecucion;
no responde de memoria. El kb es **agnostico al formalismo**: cada formalismo
aporta sus resoluciones de la capa A (OPM las trae `dov-dori`; otros, sus
especialistas).

## Workflow

### `triaje`

¿Hay un acto de modelado con una o mas decisiones en juego? ¿Admite lectura por
tensiones? Si es ruido o gusto arbitrario sin estructura → declinar y declarar.
Salida: el conjunto de decisiones a navegar.

### `ubicar-capa`

Para cada decision, situarla: **sustantiva** (A, que debe decidirse del sistema),
**praxis** (B, como decide el modelador) o **contexto** (C, condiciones que
modulan). No confundir capas: una decision de praxis tratada como sustantiva
busca en el formalismo una respuesta que el formalismo no da.

### `nombrar-tension`

Identificar la(s) tension(es): los dos polos y la pregunta, **citando el kb por
URN**. Nombrar antes de resolver: enunciar polos + pregunta es el acto que
separa elegir de derivar por inercia.

### `situar-resolucion`

- **Capa A**: ¿el formalismo del operador ya resuelve esta tension (resolucion
  congelada)? Declararlo. Si ningun formalismo elegido la cubre, es supuesto
  explicito del modelo.
- **Capas B/C**: ningun formalismo las decide. Las navega el modelador. El
  contexto (C) modula profundidad, alcance y ritmo —nunca la correccion—.

### `declarar-criterio-elegir`

Explicitar el **criterio** y elegir (o recomendar) un polo, con su por-que.
Nunca por inercia ni por "siempre lo hago asi". Si la decision puede esperar a
su nivel de refinamiento, declararlo (tension *ahora ↔ despues*).

### `entregar`

Diagnostico estructurado al invocador:

1. tension(es) nombradas, con polos y pregunta, **trazadas a la URN del kb**.
2. capa de cada una (A/B/C).
3. para las sustantivas: que formalismo las resuelve o que supuesto queda.
4. criterio declarado y polo elegido/recomendado, con por-que.
5. lo que queda como supuesto explicito o deuda.

## Reglas Duras

1. **Nombrar la tension antes de resolverla**: polos + pregunta + criterio.
   Hazlo explícito para las decisiones relevantes; no etiquetes cada elección rutinaria.
2. **Citar la URN del kb** que define cada tension. No de memoria.
3. **Distinguir las tres capas**: las sustantivas las resuelve el formalismo;
   praxis y contexto las navega el modelador. No confundirlas.
4. **No resolver praxis/contexto** como si un formalismo las decidiera.
5. **No invadir** la mecanica del formalismo ni el dominio: la skill nombra y
   razona la tension; el formalismo o el agente de dominio aporta la resolucion.
6. **Elegir la lectura mas debil** que cumpla el trabajo: no desplegar las 52
   tensiones cuando la decision toca dos.
7. **No forzar la lente**: si no aporta, resuelve directamente el encargo dentro
   de la capacidad disponible; deriva sólo lo que requiera otra especialidad.
8. **Consultar el kb en tiempo de skill** (Read/Grep). No responder de memoria.

## Composicion con otras skills y agentes

| Componible con | Cuando |
|---|---|
| `urn:kora:artefacto:cat-thinking` | una tension sustantiva (composicion, identidad, efectos) merece lectura categorial antes de elegir polo. |

Invocadores-expertos naturales (la skill es horizontal; el dominio lo aporta
quien la invoca):

- `urn:fxsl:artefacto:dov-dori` la compone para OPM: Dori aporta las
  resoluciones congeladas de la capa A; la skill aporta la lente de tensiones.
- el especialista de cada formalismo (ERD, IFML, BPMN) la usa para nombrar que
  tension resuelve su lenguaje y cuales quedan a la praxis.

## Recursos

`referencias/` son mapas operativos, no SSOT. Si una referencia tensiona con el
kb, manda el kb.

- `referencias/disparadores.md` — sintoma de decision trabada → capa/tension a
  consultar.
- `referencias/checklist-navegacion.md` — checks de que la navegacion esta
  completa.
