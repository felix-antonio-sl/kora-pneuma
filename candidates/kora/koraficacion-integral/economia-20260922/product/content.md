# Koraficación integral

Es el criterio único para transformar fuentes en conocimiento autosuficiente,
fiel y económico para su lector: conserva la información sustantiva con el menor
costo de tokens que permita comprenderla y usarla por sí sola. Recibe del producto `koraficacion` las fuentes
identificadas, su alcance, las representaciones disponibles y los recursos
funcionales; devuelve una candidata y la evidencia de su cotejo. No administra
la entrada ni la publicación de la biblioteca.

## Criterio de conservación

Conserva por defecto todo el contenido sustantivo del alcance. Mantén actores,
acciones y objetos; autoridad y atribución; modalidad, negación y tiempo;
vigencia, condiciones y excepciones; causas, secuencias y correspondencias;
cifras, unidades, ejemplos, enlaces y código; incertidumbres, conflictos y
propuestas. Lo ausente sigue desconocido y una propuesta no se convierte en
decisión.

Trabaja sólo con el significado de la fuente. El soporte, la apariencia y el
proceso de extracción quedan fuera del conocimiento, salvo cuando un dato
formal cambie su interpretación o aplicación. Extrae las relaciones que una
tabla, diagrama, conversación o recurso técnico comunique y conserva el
recurso en formato funcional cuando una prosa lo inutilice. No agregues una
explicación para justificar lo que no pertenece al contenido.

Desde la selección e intermedios hasta las preguntas y la salida, excluye
metainformación del soporte y del proceso: «el fondo es colorido», «aquí se hizo
OCR», «esta tipografía era más grande», «hasta aquí llega la página 13», logos,
cabeceras repetidas, apariencia de firmas, notas sobre Markdown o extracción.
Tampoco escribas «se omitió…» ni inventaríes esos elementos como conocimiento.
Omitirlos no es una pérdida que el cotejo deba reparar. Una flecha puede comunicar
una secuencia: expresa esa relación. Un color o un campo exigido por una regla
es contenido por su función, no por la apariencia del ejemplar. Los localizadores
y hashes necesarios quedan sólo en evidencia técnica; no se narran por fragmento.

La economía permite reformular, factorizar y reordenar cuando mantiene las
relaciones y el contexto que el lector necesita. No sustituyas una enumeración
por una categoría, una alternativa por una conjunción, ni una condición por un
alcance más amplio. La reproducción literal sólo se exige cuando la forma
afecta el significado o cuando el pasaje difícil debe conservarse para no
perderlo.

## Recorrido de trabajo

1. **Preparar.** Congela o reutiliza fuentes por identidad de bytes y versión;
   delimita el alcance y el destinatario. Prepara texto, imágenes, tablas,
   turnos o recursos según corresponda. Usa un mapa de regiones sólo cuando
   ayude a reconocer cobertura; distingue material disponible, representado,
   cotejado, ilegible y pendiente. El agente obtiene o reutiliza las
   extracciones mediante las herramientas disponibles; una transcripción no acredita una parte que no
   fue recuperada.

2. **Transformar.** Lee el conjunto completo mientras sea fiable y particiona
   sólo cuando la extensión o complejidad lo exija, respetando unidades
   semánticas, tablas y código. Redacta directamente desde la fuente una forma
   compacta: elimina repeticiones, factoriza reglas comunes con sus excepciones
   y elige prosa, lista, tabla, fórmula o código por su economía y utilidad.
   Evita rótulos sin función y abreviaturas que obliguen a reconstruir contexto.
   Usa notas, correspondencias o inventarios sólo donde protejan una
   relación difícil. Cada parte conserva sus condiciones y definiciones, y el
   artefacto no contiene rótulos del procesamiento.

3. **Cotejar.** Recorre fuente→candidata para encontrar pérdidas y
   candidata→fuente para encontrar adiciones o cambios de sentido. Comprueba
   anexos, títulos, uniones, relaciones entre partes, referencias y recursos.
   Contrasta sujeto, acción completa, objeto, autoridad, modalidad, tiempo,
   condición, excepción, finalidad, causa y valores; prueba casos que
   distingan alternativas, conjunciones, negaciones y alcance. Lee además la
   candidata como producto autónomo y registra límites reales. En este mismo
   cotejo pregunta: ¿puede expresarse el mismo contenido con menos tokens sin
   perder significado ni dificultar su uso? Identifica redundancias o expansión
   sin función y resuélvelas antes de aceptar. Si hay dos representaciones
   plausibles cuya economía no sea evidente, compara sus tokens mediante
   `kora_cli.py measure`, según la [interfaz](references/protocolo.md).
   Elige la menos costosa entre las que conservan significado y legibilidad;
   una salida más corta que pierde contenido queda descartada.

4. **Reparar y cerrar.** Repara los hallazgos materiales juntos y vuelve a
   cotejar lo afectado, incluyendo consumidores de una definición o condición
   compartida aunque sus bytes no hayan cambiado. Conserva las versiones y la
   evidencia necesarias para reanudar. Si un pasaje sigue fallando, conserva su
   formulación sustantiva y declara el límite en vez de forzar una compresión.
   Cierra cuando no queden defectos materiales ni mejoras concretas de economía
   identificadas pendientes. Incluye en la evidencia del cotejo existente una
   frase sobre la mejora aplicada o la razón para conservar la representación;
   sin otro formulario, ronda ni declaración de óptimo universal.
   Devuelve la candidata al ciclo de biblioteca de `koraficacion`.

## Revisión y autoridad

Una reformulación no trivial se revisa en contexto separado del autor cuando
el riesgo lo justifica: consecuencias altas; obligaciones, permisos,
prohibiciones o excepciones; modalidad o negación dudosa; varias fuentes o
autoridades; extracción incierta; tablas, diagramas, conversaciones,
dependencias técnicas o reparaciones materiales. La longitud sola no activa
esa revisión. El revisor recibe fuente y candidata sin un veredicto anticipado,
entrega hallazgos con localizador, diferencia y efecto, y declara su aislamiento
real. Si no existe esa capacidad, el cotejo del autor se declara como tal; nunca
se etiqueta como independiente.
Si la revisión separada es necesaria, configura `--require-independent` al
iniciar el trabajo; su ausencia deja pendiente esa garantía. Usa además
`--independent-repairs` sólo si el encargo exige independencia de cada reparación.

Las preguntas de uso o interpretación se fijan sólo cuando descubren una
dependencia, ambigüedad o excepción. No evalúan soporte excluido y no
reemplazan el cotejo completo. Un control negativo se reserva para la primera
aplicación o un cambio material del método; cuenta únicamente si localiza la
alteración sembrada y explica su efecto.

Un revisor puede aceptar condicionalmente una reparación sólo sobre los bytes
exactos que examinó en el objetivo completo, con su contexto y dependencias.
La igualdad de la candidata liga la decisión al resultado, pero no crea una
revisión nueva. Identifica quién escribió la reparación y conserva base,
objetivo y evidencia; si el alcance o el efecto sigue incierto, la aceptación
queda pendiente y se amplía el cotejo.

## Helper y límites

El helper `scripts/workflow.py` conserva fuentes congeladas, versiones revisadas
y cambios reanudables sobre el cuerpo del borrador KORA. Lee su
[interfaz](references/protocolo.md) al usarlo. El agente obtiene extracciones,
redacta y coteja con las herramientas del runtime; el helper protege identidad,
base, recursos y reanudación, sin hacer OCR, llamar modelos ni publicar.
Sus controles no producen juicios semánticos ni aprobación. Conserva el trabajo
en una carpeta privada fuera del producto, de Git y del borrador; una sola
instancia de trabajo administra cada cuerpo. Tras `init`, cambia el cuerpo
mediante el helper; una edición externa se conserva como conflicto.

La revisión de economía siempre forma parte del cotejo; medir tokens se reserva
para una comparación útil. El costo incluye los recursos que el lector necesita
para interpretar la salida; desplazar texto a otro archivo no es ahorro por sí
solo. No confundas retirada de metainformación con compresión del contenido.
La compresión se informa sólo si aporta evidencia; no hay porcentaje, ahorro
mínimo ni segunda alternativa obligatoria. Un texto ya económico puede
conservarse; no fuerces una alternativa sin beneficio plausible ni atribuyas
ahorro inexistente. Cotejo semántico, validez mecánica, aprobación y publicación son
hechos distintos. Los trabajos legados conservan su protocolo propio en
`references/compatibilidad-integral-3.md` y no se mezclan con este recorrido.
