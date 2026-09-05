# Reglas de formulacion — checklist de auditoria

Las **20 reglas de formular conocimiento** de Piotr Wozniak (SuperMemo), el criterio
contra el que la IA audita cada tarjeta que el operador escribe. No son para que la IA
genere tarjetas: son para que **marque violaciones** y proponga reescrituras que el
operador acepta o rechaza.

## Las 20 reglas (condensadas)

| # | Regla | En una linea |
|---|---|---|
| 1 | No aprender lo que no se entiende | Memorizar sin comprender es la patologia #1. Va a "no entiendo aun", no a tarjeta. |
| 2 | Aprender antes de memorizar | Construye la imagen completa del tema antes de cortar tarjetas. |
| 3 | Construir sobre lo basico | Lo basico parece obvio pero sostiene todo; no lo saltes. |
| 4 | **Minima informacion** | Cada tarjeta, *una* cosa. Lo simple es facil de programar y mantener. |
| 5 | **Cloze deletion** es facil y efectivo | "El [...] rompe el estado compartido" — barato y de alta retencion. |
| 6 | Usar imagenes | Una imagen vale por un parrafo; reduce wording. |
| 7 | Usar mnemotecnia | Para material arbitrario (nombres, fechas, listas inevitables). |
| 8 | Oclusion grafica = cloze | Tapar partes de un diagrama es tan bueno como el cloze textual. |
| 9 | **Evitar conjuntos (sets)** | "¿Que paises hablan espanol?" es un set: enorme, inestable. Reformula. |
| 10 | **Evitar enumeraciones** | "Los 4 tipos de…" se rompe. Usa cloze incremental o varias tarjetas. |
| 11 | **Combatir interferencia** | Si dos tarjetas se confunden, contrastalas explicitamente o fusiona el matiz. |
| 12 | **Optimizar el wording** | Pregunta precisa → respuesta inequivoca. Menos palabras, mas senal. |
| 13 | Referir a otras memorias | Apoyate en lo ya sabido para anclar lo nuevo. |
| 14 | **Personalizar + ejemplos** | Con tus palabras y tu ejemplo: eso ES la codificacion. |
| 15 | Apoyarse en estados emocionales | Lo que emociona se recuerda; usa ejemplos vividos. |
| 16 | El contexto simplifica el wording | Una categoria/tag da contexto sin inflar la tarjeta. |
| 17 | Redundancia no contradice minima-info | Pares pregunta↔respuesta inversos pueden coexistir si ayudan. |
| 18 | Dar fuentes | De donde salio: permite re-verificar y actualizar. |
| 19 | Fechar | Cuando lo aprendiste: la verdad caduca; sabe cuando revisar. |
| 20 | Priorizar | No todo merece el mismo esfuerzo; lo critico primero. |

## Las de mayor rendimiento (auditar siempre)

**Minima informacion + Atomicidad (4).** Si la respuesta tiene comas o "y", probablemente
son dos tarjetas.
- ✗ "¿Que hace una funcion pura?" → "No tiene efectos secundarios y su salida solo depende de su entrada."
- ✓ "¿Que propiedad de salida define a una funcion pura?" → "Su salida solo depende de su entrada."
- ✓ "¿Que NO tiene una funcion pura?" → "Efectos secundarios."

**Pregunta, no enunciado.** El recuerdo activo (recall) supera al reconocimiento.
- ✗ "El estado compartido rompe la pureza."
- ✓ "¿Que rompe la pureza de una funcion?" → "El estado compartido (efectos)."

**Evitar listas/enumeraciones (9, 10).** Las listas tienen retencion pesima.
- ✗ "¿Cuales son los 4 pilares de la OOP?" → "Abstraccion, encapsulamiento, herencia, polimorfismo."
- ✓ cuatro tarjetas tipo "¿Que pilar de OOP oculta el estado interno tras una interfaz?" → "Encapsulamiento."
- ✓ cloze incremental: "Los pilares de OOP: abstraccion, {{c1::encapsulamiento}}, {{c2::herencia}}, {{c3::polimorfismo}}."

**Combatir interferencia (11).** Tarjetas que se parecen demasiado se canibalizan.
- Si "¿capital de Australia?"→Canberra y "¿ciudad mas grande de Australia?"→Sydney se
  confunden, anade el contraste en ambas ("capital, NO la mas grande").

**Contexto minimo + Tuya (12, 14, 16).** Lo justo para ser inequivoca, en tu lenguaje.
- ✗ parrafo de tres lineas que reproduce el libro.
- ✓ una pregunta tuya con tu ejemplo de trabajo.

## Senal de retencion hueca (para el eval de transferencia)

Una tarjeta puede estar "verde" (la recuerdas) y aun asi ser inutil si memorizaste la
*forma* y no el *concepto*. El eval de transferencia (movimiento 7, por un agente
distinto del auditor) reformula la pregunta: si recuerdas la tarjeta literal pero no
aplicas el concepto en una formulacion nueva, la tarjeta se **reformula**, no se fuerza.
