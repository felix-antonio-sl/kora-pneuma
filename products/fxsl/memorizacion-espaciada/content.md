
# memorizacion-espaciada

## Proposito

Skill para sostener un **loop de memorizacion por repeticion espaciada** (Anki +
scheduler FSRS) que no muere de bancarrota de repaso. Da al agente invocador la
capacidad de **acompanar al operador en el ciclo capturar→triar→formular→repasar→
revisar**, donde la IA **audita la formulacion pero el humano la escribe** —
porque formular es el acto de aprender, no un tramite a delegar.

No construye herramientas: **adopta** Anki/FSRS y se limita a lo minimo. El metodo
es reusable para cualquier fuente: una clase, un libro, un paper, NotebookLM, una
conversacion.

## El norte

> **No es retencion ni streak. Es: ¿puedes soltar lo que aprendes y confiar en que
> el sistema lo sostiene, sin culpa de fondo?**

Brujula para toda decision sobre el sistema: ***"¿esto me ayuda a soltar, o me da
una cosa mas que vigilar?"*** Si un anadido no ayuda a soltar, no entra.

## Cuando Usar

- el operador aprende de cualquier fuente y quiere **retener** lo que importa.
- hay un INBOX de semillas de aprendizaje **sin triar**.
- toca **formular** tarjetas (el operador escribe, la IA audita contra las reglas).
- el repaso diario necesita **anclaje + valvula** (sobre todo en un dia malo).
- el due se **acumulo** y hay riesgo de bancarrota de repaso → drenar sin culpa.

## Cuando NO Usar

- **memorizar lo que no se entiende** (la patologia #1 de Anki): si no lo entiendes,
  NO es tarjeta — va a "no entiendo aun" y se vuelve pregunta para un agente o
  NotebookLM. Primero entender, despues memorizar.
- **construir tooling** en vez de adoptar Anki/FSRS (anti-patron de steipete).
- usar el sistema como **streak de vanidad** (Review Heatmap esta prohibido).
- **desregulacion/crisis** del operador → eso es regulacion (`urn:fxsl:artefacto:gtd-flow`
  / cuidado humano), no esta skill. Chequear estado antes de operar (movimiento 6).
- material efimero que **no merece memoria permanente** → la mayoria del INBOX: borrar.

## Workflow — los siete movimientos

1. **`capturar`** — en caliente, sucio, 10 segundos. Durante el aprendizaje NO se
   formulan tarjetas: se tiran **semillas** al INBOX (insight crudo, duda, frase,
   screenshot). Capturar no compromete a nada (puede morir en el triage). **Una sola
   superficie de captura**, friccion cero, Mac↔iPhone; con dos no se confia en
   ninguna.
2. **`triage`** — en frio, bloque dedicado (2-3x/semana). Por cada semilla:
   ¿merece memoria permanente? (**la mayoria NO; borrar es resultado valido y
   frecuente**) · ¿es atomica o un tema con 5 ideas? (se descompone) · ¿la entiendo?
   (si no, no es tarjeta).
3. **`formular`** — solo sobre el ~20% que sobrevive. **El operador redacta la tarjeta
   atomica con sus palabras**; la IA sugiere candidatos, audita contra las reglas
   (abajo + `referencias/reglas-formulacion.md`), marca violaciones y propone
   reescrituras que el operador acepta o rechaza. **Ninguna tarjeta entra sin la mano
   del operador.**
4. **`organizar`** — al mazo de dominio grande (no por fuente ni sesion; fragmentar
   mata). Minimo. FSRS maneja la dificultad.
5. **`repasar`** — diario, anclado. **1 ancla obligatoria (manana, sagrada) + 2 de
   oportunidad.** Dia bueno: 3 toques. Dia malo: 1. Ninguno es fracaso. El estado
   manda sobre el contador.
6. **`valvula`** — el dia malo, **pre-decidido** (ver pseudocodigo). Topes de carga,
   modo-drenaje, "un dia perdido no es deuda". Es el riesgo #1 (95% de los sistemas
   Anki mueren por bancarrota de repaso, no por fallo tecnico).
7. **`revisar`** — semanal (15 min) + mensual. Semanal: ¿el INBOX drena o se acumula?
   Podar **leeches** (suspender las que fallan siempre → reformular, no forzar) +
   **eval de transferencia**. Mensual (generacion): *"¿lo que memorizo me acerca al
   profesional que quiero ser, o me volvi coleccionista de tarjetas?"*

**El loop en una linea:** *capturo sucio en caliente → trio en frio y borro la mayoria
→ formulo con mis palabras solo lo que sobrevive → repaso anclado con valvula → reviso
semanal y podo.*

## Reglas de formulacion (lo que la IA audita)

Las de mayor rendimiento (Wozniak, condensadas); las 20 completas con ejemplos en
`referencias/reglas-formulacion.md`:

| Regla | En una linea |
|---|---|
| **Minima informacion** | Cada tarjeta, *una* cosa. Si la respuesta tiene comas, dividela. |
| **Atomicidad** | Una pregunta → una respuesta inequivoca. |
| **Pregunta, no enunciado** | "¿Que propiedad rompe el estado compartido?" > "El estado compartido rompe X". |
| **Evita listas/enumeraciones** | No "los 4 tipos de…". Usa *cloze* incremental o varias tarjetas. |
| **Evita interferencia** | Si dos tarjetas se confunden entre si, reformula para contrastarlas. |
| **Contexto minimo** | Suficiente para ser inequivoca, sin parrafos. |
| **Tuya** | Con tus palabras y ejemplos — eso es la codificacion. |

## La valvula del dia malo

```
para cada sesion de repaso:
    estado ← chequear_estado()              // 5 segundos
    si estado = "fundido":
        repasar(solo_lo_esencial, corto)
    sino:
        repasar(due_de_hoy)
    si cantidad(due) > UMBRAL:              // p.ej. 60
        postergar_excedente()               // FSRS Helper (add-on 759844606)
        nuevas_por_dia ← 0                   // hasta drenar el atraso
    // regla de oro: NO arrastrar la deuda de ayer; hoy repaso lo de hoy
```

## Roles humano-agente

- **El operador formula** cada tarjeta con su mano y sus palabras: es el acto de
  aprender, no se delega.
- **El agente-auditor** sugiere candidatos, audita contra las reglas, marca
  violaciones y propone reescrituras — nunca escribe la tarjeta final solo.
- **El agente-evaluador de transferencia DEBE ser distinto del auditor** (separacion
  autor/evaluador): hace 3-5 preguntas reformuladas sobre lo aprendido. Si el operador
  recuerda la tarjeta pero no usa el concepto → **retencion hueca**, se reformula.

## Metricas

| Prohibidas como exito | Reales |
|---|---|
| streak, tarjetas/dia, heatmap de vanidad | true retention (~90%, *desired retention* 0.90 en FSRS) |
| | eval de transferencia (concepto usado, no solo recordado) |
| | el INBOX **drena** (no se acumula) |

## Reglas Duras

1. **Capturar ≠ formular**: la semilla entra en caliente; la tarjeta se formula en frio.
2. **Borrar es resultado valido** y frecuente del triage (protege tu atencion de repaso).
3. **No se memoriza lo que no se entiende.**
4. **El humano formula; la IA audita.** Ninguna tarjeta sin la mano del operador.
5. **El estado manda sobre el contador**: chequeo de 5 segundos antes de repasar.
6. **No arrastrar la deuda de ayer**: el dia malo esta pre-decidido (valvula).
7. **Adoptar, no construir**: add-ons minimos; sin heatmap de vanidad.
8. **Transferencia, no recuerdo hueco**: evalua el concepto en uso, con autor≠evaluador.

## Composicion

| Componible con | Cuando |
|---|---|
| `urn:fxsl:artefacto:gtd-flow` | el movimiento 6 (chequeo de estado / valvula) comparte la disciplina de regulacion: si el operador viene fundido o desregulado, se compone gtd-flow para recuperar estado antes de repasar — no se duplica la regulacion. |

Es el mismo loop genealogico que `gtd-flow` (capturar→triar→...→revisar con envelope),
aplicado al dominio de la memoria; comparte la valvula y el chequeo de estado.

## Prerequisito

La **habilitacion** (instalar Anki desde apps.ankiweb.net — nunca "AnkiApp"; build
Apple Silicon/Intel; cuenta AnkiWeb + sync; AnkiMobile US$24.99; activar FSRS +
*desired retention* 0.90; add-on **FSRS Helper** `759844606`; limites diarios 5-10
nuevas; mazos por dominio; una superficie de captura) es setup humano de una vez: vive
en el cuaderno del operador `~/projects/formacion-continua/00-rol/sistema-memorizacion-*`.
Esta skill asume Anki/FSRS ya operativo y conduce el **metodo**, no la instalacion.
