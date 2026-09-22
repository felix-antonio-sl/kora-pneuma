# Resultado del cotejo conductual

Veredicto: **repair**.

La candidata conserva buena parte del contenido sustantivo, pero contiene dos
defectos materiales que deben repararse antes de aceptarla: cambia una
alternativa por una conjunción en la regla de acceso e inventa un acuerdo de
apertura que la fuente niega explícitamente.

## Alcance y exposición

Realicé un cotejo bidireccional fuente→candidata y candidata→fuente usando el
criterio admitido de `koraficacion-integral`. Leí la fuente completa y la
candidata completa como producto autónomo, incluyendo la tabla, la regla de
acceso, el procedimiento de aviso, el soporte técnico y el intercambio entre
Ana y Luis.

Esta revisión se ejecutó en contexto separado de la autoría de la candidata.
`authored_target: false`. Mi única exposición previa en este encargo fue una
revisión de código del helper; no redacté ni revisé semánticamente esta
candidata antes de este cotejo.

## Identidad de los artefactos

- Procedimiento admitido: `/home/felix/kora-pneuma/products/kora/koraficacion-integral/content.md`
  — SHA-256 `67ea9f4be0395a62322b79755ec91083b64c39293428e3a97d8115e82d5a8a96`.
- Fuente cotejada: `/tmp/kora-flujo-prueba-_y_ye_aq/source.md` — SHA-256
  `6a1fe8b153e3c88c69d4f4e800ed24fe419724053b61c5b4b184e7eab25a184c`.
- Candidata cotejada: `/tmp/kora-flujo-prueba-_y_ye_aq/control/candidata.md`
  — SHA-256 `53c100fc91af60996dcc84c3902161ba4dcbea3af0d93026de36c3f935d5788c`.

## Hallazgos materiales

1. **La regla de acceso cambia `o` por `y`.**

   La fuente, línea 4, permite que el coordinador autorice si hay **reserva o
   invitación**, salvo revocación. La candidata, línea 5, exige que existan
   **una reserva y una invitación**. Conserva los mismos sustantivos, pero
   cambia la relación lógica: una sola de las dos condiciones ya no basta.
   Esto restringe materialmente la autorización y debe repararse conservando
   la alternativa `reserva o invitación`, junto con la excepción de permiso
   revocado. La candidata también conserva correctamente que recibir una
   solicitud no constituye autorización.

2. **La candidata inventa un acuerdo de apertura y contradice el estado de la
   conversación.**

   La fuente, línea 10, dice que Ana propone abrir en octubre, que Luis posterga
   la decisión hasta recibir el ensayo y que **no se registra un acuerdo de
   apertura**. La candidata, líneas 23–25, conserva las dos atribuciones y la
   postergación, pero añade «Se acuerda abrir el depósito en octubre».
   Esa oración no tiene respaldo en la fuente y contradice su declaración
   explícita de que no existe acuerdo. Debe eliminarse; la propuesta de Ana y
   la decisión pendiente de Luis deben permanecer como tales.

## Contenido conservado y exclusiones correctas

La candidata mantiene el título, la condición de unidad cerrada, la obligación
del auxiliar de registrar hora y canal, la confirmación escrita previa a
asignar y la no transferencia de responsabilidad. Conserva sin cambio
material la tabla, incluidos `A / Piezas / 30 días` y `B / Herramientas / No
especificado`; la celda no especificada no fue convertida en cero ni en una
prohibición. También mantiene que el módulo OCR admite PNG y que el indicador
rojo significa acceso suspendido.

La nota de OCR, la paginación, el fondo y la tipografía de las líneas 1–2 de la
fuente son metainformación del soporte o del proceso y su ausencia en la
candidata es correcta. No deben reincorporarse ni convertirse en preguntas o
explicaciones de limpieza.

## Cotejo inverso y límites

En el recorrido candidata→fuente, todas las afirmaciones salvo la conjunción
de la línea 5 y el acuerdo de la línea 25 tienen correspondencia sustantiva en
la fuente. La conjunción queda registrada como cambio de sentido y el acuerdo
como adición contradictoria. Los títulos y conectores de la candidata no
introducen otros alcances materiales.

Este resultado es un juicio de cotejo de contenido y no una comprobación
automática del helper. No acredita fidelidad universal fuera de estos artefactos
y no decide publicación; tras reparar ambos puntos debe efectuarse un nuevo
cotejo de la versión corregida.
