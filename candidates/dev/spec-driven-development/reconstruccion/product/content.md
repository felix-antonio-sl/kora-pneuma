# Desarrollo guiado por especificación

Usa esta skill cuando una idea, requisito o cambio todavía no ofrece un contrato
suficiente para implementar sin adivinar, o cuando una decisión material necesita
descubrimiento y aceptación observable. Convierte la intención y las fuentes
aplicables en la especificación mínima que permita actuar dentro de la autoridad
vigente. No la actives para un cambio inequívoco, reversible y de bajo riesgo que
ya tiene alcance y aceptación suficientes.

La salida identifica la fuente de cada decisión, el resultado para su
beneficiario, alcance y exclusiones, aceptación verificable, restricciones,
supuestos y decisiones aún abiertas. Puede vivir en el encargo, issue, PRD,
canon o archivo ya gobernado por el repositorio. No exige crear un documento ni
separar especificación, plan y ejecución por ceremonia.

## Resolver fuentes y autoridad

Lee la solicitud y solo las reglas, especificaciones, código y evidencia
necesarios para conocer el estado real. Declara `spec_source` de forma explícita:
si la fuente es la conversación o tarea vigente, identifícala como tal; si el
usuario entrega una ruta, issue u otro objeto exacto, consérvalo sin sustituirlo
por una fuente inferida.

Una decisión puede tener una fuente gobernante distinta de otra. Identifica,
para cada materia relevante:

- qué ya está decidido y por qué fuente;
- qué permite hacer el encargo vigente;
- qué sigue abierto y qué acto dependería de resolverlo;
- qué evidencia es observada, qué conclusión es inferida y qué alternativa es
  una propuesta.

Planes, tareas y resúmenes son vistas derivadas y no compiten con la fuente
gobernante. Actualiza una fuente durable solo cuando sea canónica para esa
decisión y el encargo autorice modificarla. Conserva el `AGENTS.md` aplicable y
otras reglas locales sin duplicarlas dentro de la especificación.

La autoridad se toma de la sesión y de las fuentes aplicables al acto concreto.
Arquitectura, schema, dependencias, boundaries o taste no crean por su nombre un
gate humano universal. Si el encargo ya autoriza decidirlos o cambiarlos, avanza
dentro de ese alcance. Si una decisión material excede la autoridad disponible,
prepara alternativas, evidencia y trabajo reversible; deja pendiente únicamente
el acto dependiente y formula la decisión mínima necesaria. No cierres todo el
encargo como bloqueado mientras exista trabajo independiente útil.

## Calibrar el rigor

Ajusta la profundidad a incertidumbre, consecuencias del error, reversibilidad,
vida útil y número de consumidores:

| Modo | Cuándo basta | Superficie habitual |
|---|---|---|
| **Directo** | El cambio es inequívoco, acotado y reversible; la aceptación ya está clara. | Una formulación breve en la tarea y ejecución inmediata. |
| **Micro-spec** | Existe ambigüedad material, más de una alternativa o riesgo que exige fijar una decisión explícita. | Contrato compacto en la superficie de trabajo vigente. |
| **Durable** | La decisión gobernará varios incrementos, actores o consumidores, o su reversión será costosa. | Fuente versionada en la ubicación que el repositorio ya usa. |

No elijas por minutos, cantidad de archivos o etiquetas arquitectónicas. No
crees ADR, PRD, carpeta de specs ni plan durable sin consumidor y propietario.
Una micro-spec puede contener una decisión de arquitectura; una fuente durable
puede ser breve.

## Descubrir antes de fijar

Inspecciona el sistema vivo antes de diseñar sobre supuestos que el código o el
comportamiento pueden resolver. Localiza interfaces, consumidores, datos,
restricciones, precedentes y pruebas pertinentes. Cuando falte información que
solo un experimento puede revelar, realiza el menor spike reversible permitido y
marca su resultado como descubrimiento, no como implementación aceptada.

Clasifica las afirmaciones que cambian el diseño:

- **observada**: respaldada por una fuente o comportamiento identificado;
- **inferida**: conclusión provisional con evidencia y límite;
- **propuesta**: elección todavía no ratificada por la autoridad que corresponda;
- **decidida**: elección ya autorizada para este alcance.

Resuelve vacíos menores mediante supuestos explícitos y revisables. Busca una
aclaración cuando distintas respuestas cambiarían materialmente resultado,
riesgo o autoridad. Mientras llega, completa las lecturas, alternativas,
prototipos reversibles y demás trabajo que no dependa de esa decisión.

## Escribir el contrato mínimo

Incluye solo los campos que cambian ejecución o aceptación. Esta forma es una
ayuda, no una plantilla obligatoria:

```text
spec_source: <fuente gobernante o encargo vigente>
resultado: <comportamiento que debe cambiar>
beneficiario: <quién obtiene valor>
estado_observado: <evidencia actual pertinente>
alcance: <incluido>
no_objetivos: <exclusiones que contienen la deriva>
aceptacion: <condiciones observables y verificables>
restricciones_y_autoridad: <límites reales>
supuestos: <solo los activos>
decisiones_abiertas: <decisión y acto que depende de ella>
```

Expresa comportamiento mediante ejemplos concretos cuando reduzcan ambigüedad.
Incluye diseño técnico solo hasta el nivel necesario para ejecutar, elegir una
alternativa o preservar un invariante. Hereda comandos, estructura, estilo y
estrategia de pruebas desde las fuentes del repositorio; escribe solo la delta
del cambio.

La aceptación describe un resultado observable, incluidos límites o casos
negativos relevantes. Una lista de actividades no acredita éxito. Añade umbrales
no funcionales solo cuando exista una necesidad, una medición posible y una base
adecuada; no inventes cifras para aparentar precisión.

## Pasar de especificación a trabajo

Planifica cuando dependencias, coordinación o riesgo hagan más segura la
ejecución. Cada incremento debe producir un comportamiento comprobable y dejar
claros alcance, autoridad y verificación. Ordena por dependencias y evita dividir
por archivos o capas cuando eso posterga el resultado utilizable. Si el siguiente
movimiento seguro es evidente, ejecútalo sin fabricar tareas.

Durante la implementación, contrasta nueva evidencia con la especificación. Si
refuta un supuesto, actualiza la fuente gobernante o deja explícita la decisión
pendiente antes de cruzar esa frontera. No amplíes alcance para aprovechar un
hallazgo incidental ni reescribas la especificación después para legitimar una
deriva. Una relación con `ship-discipline` o `code-review` señala métodos que
pueden ayudar; no obliga a invocarlos ni demuestra que estén cargados.

Detente cuando el resultado cumple la aceptación y los riesgos materiales están
proporcionalmente cubiertos. Entrega `spec_source`, modo efectivo, contrato
suficiente, decisiones pendientes, siguiente movimiento y evidencia de lo que
se haya ejecutado. Mantén ese cierre en la superficie gobernante o en la tarea si
no existe un consumidor para otro informe.
