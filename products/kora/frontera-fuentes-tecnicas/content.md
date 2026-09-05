# Conservar fuentes y transformar conocimiento

Una koraficación hace una fuente más utilizable conservando las distinciones
relevantes para el encargo. Elige la representación por su capacidad de preservar
significado y función. El resumen puede coexistir con el original que permite
comprobarlo.

## Qué representar y qué conservar

Describe fuente, destinatario, uso y parte cubierta. Conserva condiciones,
excepciones, relaciones, unidades, fechas pertinentes e incertidumbre. Si
excluyes un aspecto relevante para ese uso, explica la exclusión junto al
contenido que puede verse afectado.

Mantén el formato original cuando tenga una función que la prosa no realiza:
ontologías OWL/SKOS, tablas de datos, esquemas, catálogos XML, código, diagramas
con relaciones espaciales o archivos consumidos por otra herramienta. El
conocimiento puede explicar cómo utilizarlos y sus límites. Una descripción
textual de una figura no acredita equivalencia con la figura.

Conserva una ruta recuperable y, cuando corresponda identificar una versión
concreta, su hash. Antes de trasladar una fuente externa, comprueba qué la consume
realmente, incluidos los enlaces simbólicos. Una fuente sin consumo visible
puede seguir siendo necesaria para comprobar procedencia; esa ausencia no
demuestra redundancia.

## Paso por la interfaz

`create --source` copia los originales indicados al directorio `sources` del
producto y registra origen y SHA-256 en `provenance`. `--body` incorpora el
conocimiento ya autorado. La operación conserva esos bytes; la comparación
semántica sigue siendo trabajo del autor. La implementación está en
[authoring.py](../../../kora/authoring.py) y los argumentos vigentes en
`python3 kora_cli.py create --help`, desde la raíz del repositorio.

Ese directorio forma parte del producto. Incorpora allí solo material apropiado
para su conservación en el repositorio; secretos, datos sensibles y estado
personal permanecen fuera de Git y de las realizaciones. Si el original debe
permanecer externo, conserva en la procedencia la referencia necesaria sin
copiarlo por comodidad. La maquinaria no inspecciona ni autoriza su contenido
por el nombre o la extensión.

## Comprobar la transformación

Vuelve desde las afirmaciones decisivas al pasaje, tabla, figura o dato que las
sostiene. Contrasta también una excepción y una incertidumbre cuando existan.
Comprueba que el conocimiento se recupere con `resolve` y que sus recursos sean
accesibles desde la fuente o la realización pertinente.

Un hash igual prueba igualdad de bytes; la existencia del archivo prueba una
ubicación disponible. Ninguno demuestra cobertura, interpretación correcta ni
vigencia de lo que dice. Si falta una fuente o su versión, declara ese límite
concreto y preserva lo que sí puede recuperarse.

Los recursos empaquetados de una skill siguen la estructura soportada por
[Agent Skills](https://agentskills.io/specification#optional-directories); el
contrato efectivo de copia y acceso está en [Codex](../../../docs/codex.md) y
[Hermes](../../../docs/hermes.md). Las fuentes técnicas no se convierten en
skills por tener archivos auxiliares.
