# code-review

Revisa un cambio sin modificarlo desde dos perspectivas:

- **Standards**: reglas documentadas aplicables y, cuando ayuden, juicios de
  diseño apoyados en el baseline auxiliar de smells.
- **Spec**: correspondencia con el encargo, issue, PRD o especificación que
  originó el cambio.

Conserva la distinción entre ambas perspectivas y las evidencias que sostienen
cada hallazgo. Una misma sesión puede realizar la revisión completa. Delega
subtareas solo cuando su independencia o extensión lo justifique y la autoridad
vigente permita hacerlo; define el alcance y reúne sus resultados. El método
no requiere roles, cantidad de agentes ni recibos predeterminados.

## Delimitar el cambio

Usa el repositorio y la referencia indicados en el encargo. Si la base no fue
declarada, intenta derivarla de la PR, la rama de destino o el contexto Git;
explica la evidencia que permite elegirla. Consulta únicamente cuando queden
alternativas que cambien materialmente qué se revisa. No elijas una base solo
porque se llame `main` o porque produzca un diff pequeño.

Resuelve las referencias Git a commits y elige la comparación pertinente:
`git diff BASE...HEAD` muestra lo introducido desde el ancestro común;
`git diff BASE HEAD` compara los dos estados. Si se pidieron cambios locales,
incluye explícitamente el estado preparado, las ediciones y los archivos nuevos
del alcance. Identifica qué estado se revisó y mantén sus citas consistentes.
Un diff vacío significa que no hay cambios en esa comparación; no es un fallo
del código ni motivo para inventar hallazgos.

La revisión permite lectura, búsquedas y comprobaciones sin efectos sobre el
trabajo o instalaciones. Cuando una prueba necesita escribir, usa un entorno
temporal autorizado o declara ese límite. La revisión por sí sola no autoriza
correcciones, commits, instalaciones ni publicación.

## Encontrar el criterio

Lee primero la fuente de requisitos indicada y las instrucciones locales
aplicables. Si no se indicó una especificación, busca el encargo disponible,
referencias en la PR o commits y documentación pertinente del repositorio.
Una coincidencia de nombre no acredita que un documento gobierne el cambio.

Si una fuente explícita falta o contradice otra fuente con autoridad, precisa
el problema y continúa la revisión independiente que siga siendo útil. Pide
aclaración cuando su resolución pueda cambiar el juicio. Si no existe una
especificación identificable, declara **Spec: fuente ausente**; conserva las
observaciones sobre implementación como tales, sin fabricar requisitos.

## Examinar y contrastar

En **Standards**, separa el incumplimiento de una regla aplicable del juicio de
diseño. Carga `referencias/smell-baseline.md` solo cuando ese análisis aporte
algo al encargo. Un smell necesita una consecuencia concreta y una mejora cuyo
beneficio compense su costo. Respeta las formas aceptadas expresamente por el
repositorio y evita repetir como hallazgos lo ya informado por sus herramientas.

En **Spec**, busca requisitos ausentes o parciales, comportamiento fuera del
alcance y requisitos aparentemente cubiertos cuya implementación falle. Lee el
contexto necesario para entender cómo se alcanza el código cambiado; un hunk
aislado puede ocultar una precondición o un consumidor decisivo.

Para cada posible hallazgo, intenta refutarlo: comprueba el escenario que lo
activa, las condiciones que podrían impedirlo y si el problema ya existía en la
base. Ajusta las pruebas a la incertidumbre y al efecto. Distingue el resultado
observado del razonamiento estático y de lo que quedó sin comprobar.

## Entregar hallazgos utilizables

Cada hallazgo identifica su perspectiva, impacto, condición de aparición,
ubicación precisa y evidencia. Cita la regla o requisito cuando corresponda y
explica una dirección de corrección suficiente, sin aplicar el cambio. Ordena
por impacto cuando facilite decidir; conserva visible si el fundamento es un
requisito, una regla local o un juicio de diseño.

Verifica que las citas sostengan el hallazgo en el estado revisado. Si el árbol
cambió durante la revisión, actualiza las observaciones afectadas o informa que
corresponden al estado fijado; no mezcles líneas de estados distintos ni
descartes análisis inmutable por un avance ajeno de `HEAD`.

La salida identifica el alcance revisado, los hallazgos de cada perspectiva y
las comprobaciones y límites relevantes. Si no hay hallazgos sustentables,
dilo; una fuente ausente o una prueba no ejecutada permanece visible. Adapta el
formato al tamaño del cambio, sin conteos, tablas o formularios obligatorios.
