# Diagnóstico de fallos

Usa esta skill ante un bug, fallo intermitente, salida incorrecta o regresión de
rendimiento cuya causa no esté establecida. Reconstruye el síntoma, produce
hipótesis contrastables y, cuando el encargo lo autorice, lleva una corrección
hasta evidencia suficiente. No la actives para implementar una mejora sin
síntoma, hacer una revisión general de código o explicar un error cuya causa ya
está demostrada y solo requiere una corrección directa.

Recibe el reporte, el candidato o estado observado, el entorno accesible y la
autoridad de la sesión. Devuelve el diagnóstico o estado de investigación que la
evidencia permita, el próximo contraste discriminante y, si corresponde, una
corrección verificada. Distingue siempre:

- **observación**: lo visto en código, salida, traza o medición;
- **hipótesis provisional**: explicación aún no discriminada;
- **diagnóstico sustentado**: causa que explica el síntoma y resistió un
  contraste capaz de refutarla;
- **corrección verificada**: cambio que elimina el síntoma en el candidato
  indicado sin romper las comprobaciones pertinentes.

No presentes una hipótesis como diagnóstico por resultar plausible. Conserva
el alcance autorizado, los cambios concurrentes y los límites de los datos. Lee
las reglas locales y el contexto técnico necesario antes de interpretar un
módulo; no conviertas la existencia convencional de un archivo en un requisito.

## Fijar el síntoma y el candidato

Describe la diferencia entre comportamiento esperado y observado con la mayor
precisión disponible: entrada, salida, entorno, versión, frecuencia, momento y
primer testigo conocido. Identifica qué candidato examinas —árbol, commit,
build, configuración o dataset— y qué evidencia proviene de otro estado.

Comprueba primero que el fallo cercano sea el mismo que se reportó. Un mensaje
parecido, una suite roja o una lentitud percibida pueden tener otra causa. Si
faltan datos, resuelve los vacíos menores con supuestos explícitos y solicita
solo aquello que pueda cambiar el rumbo o permitir un contraste decisivo.

## Construir el bucle de feedback adecuado

Busca la observación más pequeña que atraviese el seam donde aparece el síntoma.
Elige según el sistema, sin convertir este orden en gate:

- test focal que alcanza el call site real;
- petición HTTP reproducible;
- invocación CLI con fixture y salida esperada;
- navegador con aserciones de DOM, consola y red;
- replay de una traza, payload o registro capturado;
- harness descartable con dependencias mínimas;
- propiedades o fuzz con entradas y semilla controladas;
- bisección entre commits, versiones, configuraciones o datasets;
- comparación diferencial entre una ejecución buena y una fallida;
- reproducción guiada por una persona cuando el entorno no puede automatizarse.

Reduce inicialización y controla tiempo, semilla, filesystem, red y concurrencia
cuando influyan. Para fallos no deterministas, mide frecuencia bajo condiciones
comparables; usa repeticiones, stress o paralelismo controlado solo cuando
aumenten la señal. Declara la tasa observada y evita llamar determinista a una
señal variable.

Una reproducción fuerte acelera y eleva la confianza, pero su ausencia no
impide investigar. Si no puedes reproducir, conserva lo intentado y examina lo
que sí está disponible: rutas de código, diffs recientes, contratos, logs,
trazas, dumps, métricas o límites entre componentes. Formula hipótesis
provisionales y propone para cada una la prueba que distinguiría su predicción.
El resultado puede ser investigación útil sin diagnóstico demostrado.

## Reproducir y minimizar cuando sea posible

Ejecuta el bucle y coteja exactamente síntoma, entrada y entorno. Minimiza
quitando un dato, configuración, caller o paso por vez y repitiendo la
observación. Conserva lo que sea necesario para el fallo. Una minimización es
suficiente cuando permite separar hipótesis y sostener la corrección; no
prolongues la reducción si ya no cambia la decisión.

No sustituyas el síntoma original por otro más cómodo. Conserva tanto el caso
mínimo como el recorrido original cuando este último contiene integración,
estado o temporización que podrían refutar una corrección local.

## Formular hipótesis y elegir probes

Genera las hipótesis que la evidencia justifique, sin cantidad prefijada.
Ordénalas por poder explicativo, respaldo observado, costo del contraste y
riesgo de equivocarse. Para cada hipótesis que siga viva declara:

```text
causa propuesta → predicción observable → prueba discriminante → resultado que la refuta
```

Prefiere el probe que separe más alternativas con el menor cambio. Modifica una
variable por observación cuando sea necesario atribuir el resultado. Usa
debugger, REPL o instrumentación dirigida en los límites que separan hipótesis;
evita registrar todo a ciegas. Identifica la instrumentación temporal de manera
que pueda encontrarse y retirarse.

Una objeción o conocimiento de dominio puede reordenar las hipótesis. Incorpora
esa evidencia sin detener automáticamente la investigación mientras existan
contrastes autorizados e independientes de la respuesta.

## Seguir trazas, regresiones y rendimiento

Para errores de datos o control, sigue valores e invariantes a través de los
límites relevantes. Correlaciona eventos mediante identificadores y relojes
adecuados; no infieras causalidad solo por el orden de líneas emitidas desde
procesos concurrentes. Compara una traza fallida con una buena cuando eso permita
ubicar la primera divergencia. No expongas secretos ni datos protegidos al
conservar o compartir esa evidencia.

Para una regresión, delimita primero qué cambió: código, dependencia,
configuración, dato, plataforma o carga. Usa bisección o comparación diferencial
cuando exista una secuencia confiable. Un primer commit correlacionado es un
candidato causal; confírmalo con la predicción específica del cambio.

Para rendimiento, mide antes de modificar. Fija entradas, unidades, warm-up,
número de observaciones y variación relevante. Usa perfilador, reloj monotónico,
plan de consulta, contadores o trazas según el cuello sospechado. Compara estados
bajo condiciones equivalentes y separa latencia, throughput, uso de recursos y
variabilidad. Una impresión de logs o una sola corrida no sustituye una línea
base adecuada al efecto que se afirma.

## Corregir y verificar

Aplica una corrección solo cuando el encargo la incluya y exista evidencia
suficiente para elegirla. Prefiere el menor cambio que actúe sobre la causa sin
ampliar alcance. Si hay un seam estable y el riesgo lo justifica, convierte el
caso mínimo en una prueba de regresión, obsérvala fallar antes del cambio y pasar
después. Si no existe un seam útil, no fabriques una prueba decorativa: explica
el límite y verifica con el mejor bucle disponible.

Después del cambio, ejecuta el caso mínimo, el recorrido original y las
comprobaciones vecinas capaces de revelar efectos secundarios. En rendimiento,
repite la medición comparable e informa magnitud y variación. Una suite verde no
demuestra por sí sola la causa ni corrige una observación que nunca reprodujo.

Retira logs, flags, harnesses y prototipos temporales que no tengan un uso
durable. Conserva un test o fixture cuando prevenga la regresión y pertenezca al
repositorio. Registra un aprendizaje arquitectónico solo si identifica un seam,
acoplamiento o condición concreta que ayude a prevenir o diagnosticar el mismo
tipo de fallo.

## Cerrar al nivel acreditado

Entrega el síntoma y candidato examinados, la evidencia decisiva, las hipótesis
que sobreviven, el estado alcanzado y el siguiente paso útil. Usa tabla o recibo
solo cuando facilite revisar varias observaciones; no son requisitos del
diagnóstico. Declara con precisión uno de estos resultados narrativos:

- investigación incompleta con hipótesis provisionales y prueba siguiente;
- causa sustentada, aún sin corrección autorizada o posible;
- corrección verificada en el alcance observado;
- síntoma no confirmado y qué evidencia permitiría distinguir ausencia de fallo
  de falta de acceso.

El cierre técnico no implica aceptación humana, causalidad universal, seguridad
global ni garantía en entornos que no fueron observados.
