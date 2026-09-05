---
urn: urn:salud:artefacto:conducir-decisiones-hodom
nombre: conducir-decisiones-hodom
version: 1.0.0
estado: activo
descripcion: "Usar cuando una pregunta de dirección técnica, producto, protocolo u operación HODOM sea ambigua, burocrática o difícil de adoptar; transforma hechos y fuentes disponibles en una decisión clara, actor-completa, recuperable y lista para ratificar, sin inventar práctica clínica, permisos institucionales ni operación productiva. No usar para diagnóstico o tratamiento de un paciente individual."
fuente: "Autoría de novo KORA del 2026-08-25 desde el dictamen de cristalización cognitiva HODOM entregado por el operador (snapshot sha256:2b8c69ddbc8ec755c030330e2c7ad302339fe58301af5546b2861d89e4a390d7). Alcance: método decisional HODOM, planos de autoridad, gramática operacional, ontología práctica, temporalidad, recuperación, antiburocracia, salida y evaluación. Excluye decisiones locales concretas, copia de Esmeralda o del cuestionario y autoría del agente futuro Faro."
autor: FS
creado: 2026-08-25
lang: es
tags: [salud, hodom, direccion-tecnica, decision, autoridad, pre-respuesta, continuidad, antiburocracia]
vector: [2, 1, 2, 0, 1]
sigma: [3, 3, 3, 3, 2]
arnes: disciplina
forma: habilidad
herramientas: [Read, Grep, Glob]
targets: [codex, hermes]
alcance: usuario
estados: [identificar-objeto, fijar-plano-autoridad, recuperar-realidad, separar-estados, reconstruir-cadena, buscar-fracturas, modelar-tiempo, elegir-estado, redactar, validar-antiburocracia, validar-recuperacion]
conocimiento: [urn:salud:kb:hodom-glosario-ontologia, urn:salud:kb:hsc-normativa-hodom-indice, urn:salud:kb:hodom-direccion-tecnica]
componible: [urn:salud:artefacto:salubrista, urn:salud:artefacto:hospitalizacion-domiciliaria]
reemplaza: [urn:kora:artefacto:decision-operable]
---

# conducir-decisiones-hodom

## Finalidad

Convertir la realidad incompleta de una unidad HODOM en decisiones
comprensibles, materialmente completas y adoptables, sin inventar capacidades,
autoridad ni seguridad, y sin devolver al Director Técnico trabajo que el
propio sistema puede resolver.

La skill conduce una proposición por vez. Usa el conocimiento HODOM y las
fuentes gobernantes que estén disponibles, pero no los duplica. Su capacidad
propia es **predecidir sin usurpar autoridad**: explica el objeto, recomienda
una solución y prepara una respuesta que el humano puede ratificar o corregir.

## Cuándo usar

- Cuestionarios y decisiones G0, M0 o V01–V13 sobre HODOM.
- Especificaciones, journeys, protocolos y diseño de producto HODOM.
- Decisiones de desarrollo o preproducción HODOM que mezclan fuentes,
  autoridad, práctica, implementación o validación.
- Preguntas que nombran una función, cobertura, receptor, propietario,
  beneficiario o usuario sin decir de qué acto o resultado hablan.
- Respuestas que se refugian en «definir», «levantar» o «necesita evidencia»
  aunque el Director Técnico ya declaró la realidad operacional pertinente.

No usar para diagnóstico o tratamiento de un paciente individual. No autoriza
práctica clínica, permisos institucionales, ingreso al inventario ni operación
productiva. Para clínica domiciliaria individual corresponde el modo
asistencial HODOM; esta skill trabaja en dirección técnica, producto y operación
meso.

## Entrada mínima

Recuperar, sin convertir la ausencia de un campo en otro formulario:

```text
pregunta original
plano de decisión
autoridad disponible
hechos operacionales declarados
fuentes aplicables
estado actual del producto o práctica
```

Un hecho operacional declarado por la autoridad competente se usa. No vuelve
convertido en pregunta burocrática ni en exigencia genérica de evidencia. Se
pide evidencia cuando puede cambiar validez, seguridad, vigencia, autoridad o
el estado de la decisión.

## Workflow

### 1. Identificar el objeto real

Reformular hasta poder responder:

> ¿Quién hace qué, sobre qué, para quién, en qué momento y con qué consecuencia?

Completar desde el contexto «beneficiario de qué», «usuario de qué superficie»,
«acceso a qué», «capaz para qué acto», «cobertura de qué prestación»,
«propietario de qué registro» y «autoridad sobre qué decisión». Preguntar solo
si falta una elección humana material que no puede recuperarse de las fuentes.

### 2. Fijar el plano y la autoridad

Toda afirmación se ubica en uno de estos planos:

| Plano | Qué puede cerrar |
|---|---|
| `ESPECIFICACIÓN` | significado y comportamiento requerido del producto |
| `DESARROLLO` | diseño e implementación dentro de la delegación técnica |
| `PREPRODUCCIÓN` | candidata preparada para evaluación controlada |
| `PRÁCTICA CLÍNICA` | práctica emitida por la autoridad clínica competente |
| `AUTORIZACIÓN INSTITUCIONAL` | permisos, aprobación de seguridad e incorporación institucional |
| `OPERACIÓN PRODUCTIVA` | habilitación y funcionamiento real en producción |

Una decisión puede quedar `RESPONDIDA` para desarrollo y preproducción sin
afirmar que cambió la práctica clínica o que existe autorización institucional
u operación productiva.

La fuente informa. La evidencia acredita. La declaración del Director Técnico
decide dentro de su delegación. La institución autoriza su esfera. El software
materializa. La prueba verifica un comportamiento delimitado. Ninguna de estas
cosas sustituye automáticamente a las demás.

### 3. Recuperar la realidad operacional

Priorizar los hechos actuales de dotación, horario, función, medios, cobertura,
circuito y capacidad. Diseñar para la unidad que existe, no para una
organización ideal. La ausencia se conserva como ausencia: no crear un rol
ficticio, una cobertura nominal ni una capacidad futura para completar la
respuesta.

### 4. Separar los estados epistémicos

No fusionar:

| Clase | Significado |
|---|---|
| Hecho observado | respaldado directamente por una fuente o comportamiento |
| Declaración del Director Técnico | hecho o decisión válida dentro de su delegación declarada |
| Inferencia | conclusión dependiente de supuestos visibles |
| Propuesta | solución recomendada todavía no adoptada |
| Decisión ratificada | propuesta adoptada por la autoridad del plano indicado |
| Implementación | comportamiento materializado por el software o la práctica |
| Validación | resultado de una prueba delimitada sobre esa implementación |

No elevar una propuesta a práctica, una implementación a autorización ni una
prueba a operación real.

### 5. Reconstruir la cadena material

Para todo efecto o transferencia de responsabilidad, comprobar:

```text
función → acto → objeto → autorización → resultado
→ receptor capaz → acuse → obligación sucesora
→ recuperación ante falla
```

El receptor es capaz para **ese acto sucesor**, no en abstracto. En entrega,
notificación, traslado, contrarreferencia o cierre, la pre-respuesta incluye:

```text
quién entrega qué resultado
→ quién lo acepta y qué obligación asume
→ quién conserva responsabilidad mientras falta el acuse
→ qué ocurre ante rechazo, silencio o falla
```

### 6. Buscar fracturas ontológicas

Aplicar como pruebas de consistencia solo los contrastes pertinentes:

- Caso ≠ episodio HODOM.
- Atención domiciliaria ≠ hospitalización domiciliaria.
- Visita ≠ prestación realizada.
- GPS ≠ atención.
- Registro local ≠ ficha clínica institucional.
- Médico regulador ≠ médico de atención directa, aunque una persona pueda
  ejercer ambas funciones.
- Autoría clínica ≠ coordinación administrativa.
- Egreso ≠ cierre longitudinal.
- Envío a APS ≠ transferencia de responsabilidad.
- Dato provisional REM ≠ cierre mensual oficial.
- Indicador agregado ≠ juicio clínico individual.
- «Otro profesional» ≠ permiso universal.

No copiar esta lista a la salida. Usarla para detectar una fusión que cambiaría
la decisión.

### 7. Modelar tiempo y responsabilidad

Una decisión HODOM representa una trayectoria, no solo un instante. Resolver:

- ¿Cuándo comienza esta responsabilidad?
- ¿Qué la mantiene activa?
- ¿Qué resultado la transfiere?
- ¿Qué condición permite cerrarla?
- ¿Qué ocurre ante silencio, rechazo, deterioro o información pendiente?

El término de un episodio no elimina automáticamente las obligaciones del
Caso, la continuidad, el seguimiento postegreso ni los pendientes aceptados.

### 8. Elegir el estado correcto

| Estado | Criterio |
|---|---|
| `RESPONDIDA` | la autoridad y los hechos permiten adoptar la respuesta en el plano indicado |
| `ABIERTA` | la autoridad competente todavía debe adjudicar el contenido |
| `BLOQUEADA` | no existe un siguiente movimiento seguro antes de resolver una dependencia nombrada |
| `DIFERIBLE` | decidir ahora no cambia el incremento ni un riesgo actual |
| `NECESITA EVIDENCIA` | una afirmación requiere respaldo que puede cambiar validez, vigencia o autoridad |

No dejar abierta una decisión ya adjudicada dentro de su plano. No cerrar una
decisión fuera del plano autorizado. `NECESITA EVIDENCIA` no es una respuesta
por defecto.

### 9. Redactar para adopción

La salida tiene esta forma y omite las secciones sin contenido material:

```markdown
Pregunta clara

Contexto necesario
Dos a cinco frases con la realidad y la consecuencia necesarias para decidir.

Recomendación
Una decisión concreta y su frontera.

Pre-respuesta
Texto listo para adoptar o modificar.

Estado propuesto
RESPONDIDA | ABIERTA | BLOQUEADA | DIFERIBLE | NECESITA_EVIDENCIA

Evidencia decisiva
Solo la que cambia la validez o permite salir de un estado abierto.

Límite
Qué no autoriza, implementa ni demuestra esta respuesta.
```

Si el operador solicita solo la redacción final, entregar únicamente la
pre-respuesta y el límite indispensable.

### 10. Validar antiburocracia

Conservar toda distinción que pueda cambiar la decisión y eliminar todo lo que
solo agrega carga cognitiva. Una lectura debe bastar para entender el objeto,
la recomendación y la frontera.

### 11. Validar recuperación

Identificar la falla principal del mecanismo propuesto. La solución todavía no
está completa si no dice quién conserva responsabilidad y cómo recupera el
proceso cuando esa falla ocurre.

## Reglas duras

1. No pedir nuevamente un hecho ya declarado por la autoridad competente.
2. No convertir una declaración técnica válida en `NECESITA EVIDENCIA` por
   reflejo.
3. No inventar autoridad clínica, institucional o productiva.
4. No dejar abierta una decisión resuelta dentro de su plano ni cerrarla fuera
   de él.
5. No crear un rol nuevo para llenar una brecha.
6. No tratar disponibilidad nominal como capacidad real.
7. No llamar receptor capaz a alguien sin facultad para realizar el acto
   sucesor.
8. No confundir envío, recepción, aceptación, ejecución y transferencia.
9. No imponer plazos clínicos genéricos sin fuente o decisión competente.
10. No construir módulos sobre problemas hipotéticos sin consumidor actual.
11. No introducir preguntas sobre el cuestionario cuando no cambian HODOM.
12. No pedirle al operador una decisión de implementación que el sistema puede
    resolver dentro de su autoridad.
13. No convertir al paciente o cuidador en responsable de reparar una falla de
    la red.
14. No producir una respuesta que obligue a releer la pregunta para saber de
    qué habla.
15. Detenerse cuando exista una decisión simple, completa, segura y adoptable.

## Composición

`urn:salud:artefacto:salubrista` aporta la lectura sistémica y la
representación sanitaria de dirección técnica.
`urn:salud:artefacto:hospitalizacion-domiciliaria` aporta dominio, normativa,
continuidad y operación HODOM. Esta skill convierte ese material en una
proposición adoptable.

Las aristas `componible` nombran candidatos declarados. Su presencia no prueba wiring,
invocación automática ni composición conductual. El agente o runtime consumidor
debe cargar las piezas pertinentes y la evaluación debe observar la salida
integrada.

## Evaluación mínima

Probar en contexto limpio, sin reutilizar respuestas de la conversación:

| Familia | Invariante observable |
|---|---|
| Beneficiario, usuario o acceso sin objeto | especifica resultado y superficie concretos |
| Autoridad de desarrollo | acepta delegación técnica sin fabricar autorización productiva |
| M0 sin acto material | mantiene abierto solo el tuple que carece de autoridad semántica |
| Admisión | separa decisión clínica, registro y comunicación |
| Cobertura nocturna cero | diseña contingencia sin fingir un turno inexistente |
| Traslado | no atribuye transporte a HODOM y completa entrega y recepción |
| Registro institucional | separa captura local de incorporación autoritativa |
| Evento adverso | protege primero al paciente y después analiza y cierra |
| Brechas de dotación | conserva la brecha sin inventar equivalencia profesional |
| APS como sucesor | distingue envío, aceptación y primer acto de continuidad |
| REM y tablero vivo | produce REM sin convertirlo en tablero operativo diario |
| Regulación longitudinal | separa Caso, episodio, egreso y seguimiento postegreso |
| Pregunta irrelevante | la elimina en vez de perfeccionarla |
| Evidencia burocrática | usa la declaración válida en su plano sin exigir otra prueba decorativa |

Puntuar comprensión en una lectura, autoridad preservada, completitud
operacional, carga cognitiva, ausencia de invención, recuperación y utilidad
inmediata.

## Ejemplo sintético

**Entrada:** una continuidad fue enviada a un equipo sucesor, pero no existe
acuse. La pregunta dice «¿quién recibe el cierre?».

**Transformación:** aclarar qué resultado se entrega, asignar un receptor capaz
para el primer acto sucesor, mantener la responsabilidad en el origen hasta la
aceptación y definir devolución o escalamiento ante silencio. El estado no es
`RESPONDIDA` si la autoridad competente todavía no adjudica esa función.

El ejemplo demuestra la gramática. No adjudica qué función real debe recibir
una continuidad en una institución concreta.

## Errores frecuentes

| Error | Corrección |
|---|---|
| Repetir la pregunta con palabras más solemnes | nombrar objeto, resultado, tiempo y consecuencia |
| Responder «definir» o «levantar» | proponer lo decidible y abrir solo lo irreducible |
| Tratar toda cautela como evidencia | pedir solo el respaldo que cambia el estado |
| Diseñar la organización ideal | usar dotación, medios y circuitos realmente declarados |
| Dar por cerrado un envío | exigir aceptación, obligación sucesora y recuperación |
| Confundir producto con práctica | declarar el plano exacto que la respuesta cierra |
| Convertir la miniapp en fuente | mantener inteligencia y verdad en KORA y fuentes gobernantes |
