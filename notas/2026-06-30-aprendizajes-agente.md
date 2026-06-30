# nota: aprendizajes de agente — sesión 2026-06-30 (koraficación Langacker figs)

Esta nota es **del agente, no del artefacto** — registra tácticas y decisiones
para próximas sesiones equivalentes. No entra en el censo KORA.

## Tácticas operativas

### 1. "Inspeccionar imágenes (+lento)" fue la respuesta correcta a mi pregunta
El operador me preguntó si para 188 figuras debía (a) generar descripciones
solo desde el `.txt` (~148 captions explícitas) o (b) inspeccionar 210 jpgs
además. Yo propuse (b) como preferible. La realidad mostró que:

- ~40 figuras intermedias **no traen caption propio** — el `.txt` solo las
  referencia ("Figure X represents that…"); sin la imagen, la descripción
  sería hueca o inventada.
- El agente usó Read para abrir los jpgs con visión y describió 99 figs de
  caps. 4-8 de una pasada. Tiempo medido: ~3-5 min por bloque de 20 figs.

**Conclusión**: ante instrucciones tipo "no inventar", la inspección visual
es obligatoria para corpus técnicos con figuras. **El atajo de solo-texto
es una falsa economía que degrada la calidad del artefacto**.

### 2. Subagentes paralelos fallaron en retención de output
Lancé 2 subagentes esperando velocidad. Resultado:

- Ambos devolvieron `El mensaje no incluye el JSON` o devolvieron respuesta
  vacía — el contexto del subagente no persiste su propia salida entre
  invocaciones de tool cuando las respuestas son grandes.
- Para trabajo de **escritura continua de muchas figuras** (~188 entradas),
  el subagente paralelo **no escala**. Es mejor hacer bloques secuenciales
  uno mismo, con el `.txt` ya cargado en mi contexto.

**Lección**: subagentes son útiles para **exploración**, **búsqueda**, o
**tareas con respuesta corta** (1-5 items). Para **tareas que requieren
producir grandes artefactos estructurados**, el agente principal conserva
el contexto y la fidelidad.

### 3. Un usuario que ya sabe qué es mentira no te ahorra verificación

Aún con la instrucción explícita "no inventar" y el operador vigilante
sobre gaps, descubrí figs. 13.13/14/15 inexistentes solo al final (por ins-
pección directa del `.txt`). El agente no había marcado esos huecos como
`—` — los había "completado" con lenguaje genérico. **La descripción
genérica sin anclaje es tan peligrosa como la invención directa**; ambas
degradan la utilidad del artefacto sin flagrancia detectable.

**Lección**: cuando una figura falta, **debe notarse como falta**, no
rellenarse. Respetar la instrucción del operador al pie de la letra aunque
sea incómoda (más líneas, más "—", más distancias).

### 4. El `grep -n` por sección de capítulo es más rápido que por figura
Con 188 figs dispersas en 8200 líneas, `grep -n "^[fF]igure"` global dio 148
matches. Filtrar por capítulo-sección (caps 1-3, 4-8, etc.) toma 5-10
segundos y reduce a 30-50 matches, que se leen en batch con Read. **El
usuario prefiere velocidad y delimitar por capítulo** es fast-forward.

### 5. La verificación final con `kora.py velar --estricto` (13/13) capturó
exactamente lo que importaba

`publicacion-digna` verifica que `fuente:` sigue teniendo contenido
sustantivo. Es el check que protege contra "vacié el bloque mientras editaba".
`sello-fresco` verifica que la edición no esté descentrada temporalmente.
Combinados, son mínimo viable.

**Lección**: la verificación final es **la última línea de defensa**.
Si un artefacto pasa 13/13 después de una edición masiva, lo más probable
es que esté bien; si falla, hay una pista clara (cuál check falló, qué
campo quedó vacío).

## Decisiones que tomé sin preguntar

Estas son decisiones en las que apliqué el modo "una sola recomendación"
del CLAUDE.md del operador (comprométete con tu mejor juicio, defende el
porqué). El operador las aceptó pasivamente (continuó la sesión sin disputar).

1. **No inventar primitivos visuales** cuando el `.txt` es ambiguo y la
   imagen no es accesible. Marcar `— (no legible en la fuente disponible)`.
   Razón: el operador lo dijo explícitamente y la integridad del artefacto
   gana sobre completitud.

2. **Recortar cada cápsula a ~3 frases máximo**, aunque cabría más. Razón:
   el placeholder decía "una entrada por figura, encabezada con X.Y en
   negrita" — el espíritu es concisión para legibilidad; descripciones
   largas saturan el bloque y pierden la ventaja del formato lista.

3. **Marcar 13.13/14/15 como `—` con nota al final del handoff**, en lugar
   de inventarlas o reventar la numeración para "tapar el hueco". Razón:
   la instrucción del operador fue "no Inventar etiquetas o controles
   visuales no verificables en el original".

4. **Hacer un commit por artefacto (4 total) en lugar de un commit
   monolítico**. Razón: commits atómicos = mejor bisección = reversión
   granular. El operador lo pidió explícitamente.

## Para próximas sesiones

- Si la tarea es **koraficar un libro con figuras desde epub**: usar
  este flujo: (1) `grep` por capítulo → (2) leer contexto del `.txt` →
  (3) abrir imágenes por rango → (4) consolidar por capítulo → (5) commit
  por libro/parte. No delegar a subagentes.
- Si el **operador da rango de tiempo** ("5 min por bloque"): respetar
  e iterar. Si no da rango: trabajar exhaustivamente con check de calidad.
- **Anclar en artefacto, no en sesión**: el trabajo es el artefacto
  korificado, no mi narrativa. Esta nota es _del agente_, no del
  artefacto; vive fuera de `_emision/` precisamente porque kora.py no
  debe censarla.
