# Reglas de formulacion — checklist de auditoria

Orientaciones condensadas de Piotr Wozniak (SuperMemo) para redactar y revisar
preguntas de recuperación. La IA puede formular tarjetas cuando se le pide y ayudar
al usuario a comprobar comprensión. Las reglas son heurísticas de diseño; su aplicación
no acredita por sí sola retención, transferencia ni una tarjeta correcta.

Fuente: https://www.supermemo.com/en/blog/twenty-rules-of-formulating-knowledge

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
| 8 | Oclusión gráfica | Ocultar elementos de una imagen permite practicar su recuperación; elegir según el contenido. |
| 9 | **Evitar conjuntos (sets)** | "¿Que paises hablan espanol?" es un set: enorme, inestable. Reformula. |
| 10 | **Evitar enumeraciones** | "Los 4 tipos de…" se rompe. Usa cloze incremental o varias tarjetas. |
| 11 | **Combatir interferencia** | Si dos tarjetas se confunden, contrastalas explicitamente o fusiona el matiz. |
| 12 | **Optimizar el wording** | Pregunta precisa → respuesta inequivoca. Menos palabras, mas senal. |
| 13 | Referir a otras memorias | Apoyate en lo ya sabido para anclar lo nuevo. |
| 14 | **Personalizar + ejemplos** | Con tus palabras y tu ejemplo: eso ES la codificacion. |
| 15 | Apoyarse en estados emocionales | Un contexto personal puede ayudar; no inventar experiencias ni exigir revelar material íntimo. |
| 16 | El contexto simplifica el wording | Una categoria/tag da contexto sin inflar la tarjeta. |
| 17 | Redundancia no contradice minima-info | Pares pregunta↔respuesta inversos pueden coexistir si ayudan. |
| 18 | Dar fuentes | De donde salio: permite re-verificar y actualizar. |
| 19 | Fechar | Cuando lo aprendiste: la verdad caduca; sabe cuando revisar. |
| 20 | Priorizar | No todo merece el mismo esfuerzo; lo critico primero. |

## Las de mayor rendimiento (auditar siempre)

**Información mínima y atomicidad (4).** Separar recuperaciones distintas cuando
mejora la práctica. Una coma o una conjunción no demuestran dos conceptos: preservar
condiciones conjuntas, excepciones y relaciones. En el ejemplo siguiente las preguntas
parciales no sustituyen comprobar la definición completa.
- Definición conjunta: "¿Qué caracteriza a una función pura?" → "No tiene efectos secundarios y su salida solo depende de su entrada."
- ✓ "¿Que propiedad de salida define a una funcion pura?" → "Su salida solo depende de su entrada."
- ✓ "¿Que NO tiene una funcion pura?" → "Efectos secundarios."

**Pedir recuperación.** La pregunta o el cloze deben permitir intentar una respuesta
antes de mostrarla. Un enunciado sin tarea de recuperación no basta.
- Poco preciso: "El estado compartido rompe la pureza".
- Más preciso: "¿Qué condición de pureza se rompe si la misma entrada produce
  otra salida al cambiar un estado externo mutable?" → "La salida ya no depende
  sólo de la entrada". Leer datos inmutables no prueba por sí solo impureza.

**Evitar listas/enumeraciones (9, 10).** Las listas largas pueden dificultar recuperación y evaluación; si el orden o el
conjunto completo es el objetivo, conservarlo y practicar también sus relaciones.
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
*forma* y no el *concepto*. La comprobación de transferencia reformula la pregunta o pide una aplicación: si recuerdas la tarjeta literal pero no
aplicas el concepto en una formulacion nueva, examinar comprensión, contexto y formulación antes de ajustar la tarjeta o la práctica.
