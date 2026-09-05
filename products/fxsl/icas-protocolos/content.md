---
urn: urn:fxsl:kb:icas-protocolos
nombre: icas-protocolos
version: 1.2.0
estado: publicado
descripcion: "Pieza 14b del ICAS-BoK: protocolos y coreografía — session types, coreografía vs orquestación, sagas y tolerancia a fallas en sistemas distribuidos."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/14b-protocolos-coreografia.md (sha256:0018ff36d4790f9f2c3220df8498bf46cf0ea3d781620cf75095f6f0bcb8e54a) el 2026-06-12. v1.1.0 (2026-07-18): separa session types, profuntores, sheaves, retries, sagas y redundancia de sus analogias operacionales. v1.2.0 (2026-07-18): retira las identidades GraphQL=session type y coreografia/profunctor, orquestacion/operad; exige construcciones testigo."
autor: FS
creado: 2026-04-14
lang: es
tags: [session-type, coreografia, saga, multi-agente, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Protocolos y coreografia

## Quien dirige la danza

Cuando compongo microservicios en un sistema distribuido, hay una pregunta que
aparece antes de cualquier decisión técnica: quién coordina. Puedo poner un
servicio central que llame a los demás en orden —un orquestador— o hacer que
los servicios reaccionen a eventos compartidos —una coreografía—. Esta
diferencia operacional **puede** recibir modelos algebraicos distintos; no los
determina por sí sola.

La orquestacion puede modelarse mediante un algebra sobre una operad de wiring
si se especifican operaciones, colores y leyes. Un nodo central no "es la
operad".

Una coreografia puede modelarse con profuntores tras construir categorias de
estados e interacciones. Su composicion horizontal se calcula por coend:

```
(P . Q)(a, c) = ∫^b P(a, b) x Q(b, c)
```

En ese modelo, el coend compone testigos a través de objetos intermedios `b` y
los identifica por la acción de la categoría intermedia. La fórmula no
implementa un rendezvous, no elimina coordinadores de una arquitectura real y
no demuestra propiedades de entrega.

Kafka y un API gateway ejemplifican coreografia/orquestacion operacional. Solo
son composicion profuntorial/operadica si se construyen esos modelos.

## Session types como categorias

Un protocolo de comunicacion entre dos partes tiene una estructura temporal: primero envio un request, luego recibo un response, luego envio una confirmacion. Esta secuencia de send/receive tiene un tipo -- un session type que especifica exactamente que mensajes se esperan en cada paso.

El automata subyacente de un session type genera una categoria libre de
caminos. Session types completos añaden polaridad, branching, recursion,
linealidad y typing; no se reducen a esa categoria.

La dualidad de session types intercambia send/receive y
branching/selection. No es en general solo tomar la categoria opuesta, porque
tambien transforma etiquetas y constructores del tipo.

La linealidad controla uso de endpoints/canales en el programa. No garantiza
entrega exactly-once en una red ni convierte gRPC unary en un objeto lineal sin
semantica adicional.

Una GraphQL subscription es operacionalmente un stream sobre una conexión
persistente. **Puede** tiparse mediante un session type recursivo que repita
`send` hasta la cancelación, pero GraphQL no aporta por sí solo esa derivación
ni las garantías de linealidad, dualidad o progreso. En la categoría libre del
autómata subyacente, el ciclo genera endomorfismos; eso no convierte la
suscripción concreta en un session type por nombre.

## El algebra de los protocolos

Protocolos **pueden** recibir una semantica en una categoria monoidal libre;
cada operador debe probar su propiedad universal en ese lenguaje.

La composicion secuencial es composicion de morfismos en la categoria de sessions. Si el protocolo A termina en estado s y el protocolo B empieza en estado s, puedo componerlos: primero A, luego B. Es el caso trivial -- la composicion que ya conozco.

La composicion paralela puede modelarse por tensor. Un consumer group real
incluye rebalances, fallos y semantica de entrega; no es automaticamente el
producto monoidal de particiones.

Una alternativa `OK | Error` puede representarse por un coproducto en una
semántica de tipos con esas sumas. La elección usa una inyección y el
eliminador satisface la propiedad universal. El branching de un session type
incluye además quién selecciona la rama y la continuación de cada una; no se
reduce siempre al coproducto del payload.

Un DSL libre de pasos puede construirse como monada libre. Un protocolo
multi-step arbitrario no hereda esa representacion ni una "ley Xi" sin definir
el funtor generador y la semantica.

## Errores en protocolos distribuidos

El error en un protocolo distribuido no es un accidente -- es una rama del arbol de decisiones. La pregunta correcta no es "como evito el error" sino "como compongo el error."

`Either e a` modela exito/error tipado. Un status gRPC puede traducirse a esa
estructura, pero transport, cancelacion, deadlines y errores parciales hacen
que no sea una identidad exacta.

Un handler entre capas solo es transformacion natural si existen dos funtores
paralelos y todos sus cuadrados conmutan. Normalmente es una funcion/mapping
cuya cobertura y semantica se prueban directamente.

El retry tiene una lectura coinductiva sugerente. Un retry con exponential
backoff **puede** modelarse mediante una comónada cofree después de fijar el
funtor `p` de observación y continuación. En esa instancia, la counit extrae la
observación actual y la comultiplicación expone el comportamiento desde cada
continuación futura. El pseudocódigo siguiente ilustra esa lectura; no
construye por sí solo la comónada ni demuestra que un retry real la realice.

```
retry_with_backoff : c_p
 extract = try_now -- la counit: el intento actual
 duplicate = \s -> -- la comultiplicacion: el arbol de reintentos
 Cons s (fmap (delay * 2) (duplicate (next_state s)))
```

Un circuit breaker es primero una maquina de estados temporizada. Puede
integrarse en un modelo de sistemas hibridos/sheaves temporales si se define un
sitio, restricciones y pegado. Sus dos modos, umbral y timeout no construyen
por si solos un pushout ni una sheafification.

## El saga pattern como morfismo inverso

Cuando un protocolo multi-paso falla a mitad de camino, puedo ejecutar acciones
compensatorias. Si la reserva de hotel tuvo éxito pero el vuelo falló, cancelo
la reserva. Una compensación no es en general un inverso categorial: puede
tener efectos residuales y solo aproxima la restauración respecto de
observables declarados.

En una categoria donde todos los morfismos tienen inverso -- un groupoid -- la compensacion es exacta: el step 2 se deshace con step_2^{-1}. Pero los efectos reales rara vez son perfectamente reversibles. No puedo "des-enviar" un email. No puedo "des-cobrar" una tarjeta de credito instantaneamente -- puedo emitir un refund, que es una operacion distinta que produce un resultado aproximadamente inverso.

Una saga especifica compensaciones ordenadas. Llamarlas inversos aproximados
es un modelo que necesita una equivalencia observable o una relacion de
compensacion explicita; "`S_i'` isomorfo en lo que importa" no es una
definicion formal.

Un coordinador saga puede implementarse con un DSL/arbol libre y recibir una
semantica operadica, pero esas estructuras deben construirse; no vienen del
patron por nombre.

## Tolerancia a fallas categoricamente

Una tupla de N estados puede ser un producto en una categoria apropiada.
Redundancia tolerante a fallas requiere ademas replica, voter/quorum,
independencia y modelo de fallas; no se obtiene de la propiedad universal del
producto.

El consenso tiene una intuicion de tipo equalizer. Dado un producto de N replicas, el equalizer es el subobjeto donde todas las replicas coinciden. Para un par de replicas con outputs f, g : State -> Output, el equalizer eq(f, g) es el conjunto de estados donde f(s) = g(s). Esa es una buena imagen de acuerdo fuerte. Protocolos como Raft o Paxos implementan nociones de acuerdo mas sutiles, basadas en quorums y temporalidad, no un equalizer literal de outputs punto a punto.

La tolerancia bizantina no es por definicion una condicion de sheaf. Puede
explorarse un modelo de vistas locales sobre un site, pero hay que demostrar
que quorums son coberturas y que compatibilidad/pegado representan las reglas
del protocolo.

Un modelo posterior podría representar votos como secciones, quórums como
coberturas y acuerdo como pegado, siempre que pruebe que las reglas de Paxos o
PBFT se preservan en esa interpretación. Sin esa construcción, el lenguaje de
sites/sheaves es una heurística. FLP conserva sus cuantificadores sobre
asincronía, fallos y terminación; no se deriva de fallar una condición de
sheaf.

## La convergencia con la agencia

Los protocolos no son exteriores a los agentes: fijan parte de sus entradas,
salidas, temporalidad y errores observables. Un modelo puede acoplar árboles de
decisión libres con materia cofree, o representar interacciones por
profunctores y cableados por un álgebra operádica. Sin esos objetos y sus leyes,
coreografía y orquestación siguen siendo patrones operacionales, no resultados
de un coend o de una operad.

Estas lecturas pueden orientar modelos separados; no componen entre si hasta
que se proporcionan funtores/leyes distributivas o una semantica comun.

## Estatuto epistemico

- **Formal:** categorias libres, profuntores, estructuras lineales y
  coproductos bajo sus definiciones.
- **Modelo:** session types, sagas, retries y consenso cuando se construyen
  estados, observaciones y leyes.
- **Heuristica:** Kafka/API gateways, circuit breakers o BFT identificados
  directamente con operads, sheaves o equalizers.

## Corrección 1.2.0

Se retiran las identificaciones GraphQL subscription=session type,
coreografía=composición profuntorial y orquestación=operad. Las tres quedan
como modelos posibles solo cuando se exhiben autómata/tipo, categorías de
interacción o álgebra de wiring, respectivamente.
