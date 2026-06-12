---
urn: urn:fxsl:kb:icas-protocolos
nombre: icas-protocolos
version: 1.0.0
estado: publicado
descripcion: "Pieza 14b del ICAS-BoK: protocolos y coreografía — session types, coreografía vs orquestación, sagas y tolerancia a fallas en sistemas distribuidos."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/14b-protocolos-coreografia.md (sha256:0018ff36d4790f9f2c3220df8498bf46cf0ea3d781620cf75095f6f0bcb8e54a) el 2026-06-12; cuerpo byte-fiel. Fuente original: ICAS-BoK corpus — Fong/Spivak, Mac Lane, Barbosa, Awodey, Riehl"
autor: FS
creado: 2026-04-14
lang: es
tags: [session-type, coreografia, saga, multi-agente, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Protocolos y coreografia

## Quien dirige la danza

Cuando compongo microservicios en un sistema distribuido, hay una pregunta que aparece antes de cualquier decision tecnica: quien coordina. Puedo poner un servicio central que llame a los demas en orden -- un orquestador. O puedo hacer que los servicios se comuniquen entre si a traves de eventos compartidos, sin que nadie este al mando. La primera opcion es orquestacion; la segunda, coreografia. Y la diferencia, vista desde la teoria de categorias, es una diferencia de estructura algebraica.

La orquestacion es composicion operadica. Hay un nodo central -- la operad -- que toma N subordinados y los compone en un unico comportamiento. La composicion es jerarquica: el orquestador sabe que subcomponentes existen, en que orden invocarlos, y como ensamblar sus resultados. Es la misma estructura que explore en el documento 13: f(g_1, g_2, g_3) produce un sistema compuesto donde f controla el cableado. El orquestador tiene la operad.

La coreografia es composicion profunctorial. No hay nodo central. Los agentes interactuan a traves de interfaces compartidas, y la composicion global emerge del acoplamiento local. Categoricamente, una coreografia entre agentes A y B es un profunctor P : A^op x B -> Set. Cada elemento de P(a, b) es una interaccion valida cuando A esta en estado a y B esta en estado b. La composicion de coreografias es composicion de profunctors -- la formula de "shortest path" que ya vi en el documento 08:

```
(P . Q)(a, c) = colim_{b in B} P(a, b) x Q(b, c)
```

El coproducto indexado reemplaza al control central: no hay un nodo que elija b. La existencia de un b compatible es lo que permite la interaccion. Es composicion por rendezvous, no por invocacion.

En la practica, un Kafka-based system donde el servicio de ordenes emite un evento OrderCreated y el servicio de inventario lo consume sin que nadie los coordine explicitamente es una coreografia profunctorial. Un API gateway que llama secuencialmente a tres backends es orquestacion operadica. La diferencia no es de implementacion -- es de quien tiene la operad.

## Session types como categorias

Un protocolo de comunicacion entre dos partes tiene una estructura temporal: primero envio un request, luego recibo un response, luego envio una confirmacion. Esta secuencia de send/receive tiene un tipo -- un session type que especifica exactamente que mensajes se esperan en cada paso.

Categoricamente, un session type es una categoria libre generada por un grafo dirigido de intercambios de mensajes. Los objetos son los estados del protocolo. Los morfismos son las secuencias de operaciones que transforman un estado en otro. La composicion de morfismos es la concatenacion de pasos del protocolo. La identidad en cada estado es "no hacer nada" -- el protocolo ya esta en ese punto.

Cada session type tiene un dual: la perspectiva del otro participante. Si yo envio, tu recibes. Si yo hago branching (ofrezco opciones), tu haces selection (eliges una). Este dual es la op-category -- la misma categoria con las flechas invertidas. En un protocolo bien formado, las dos perspectivas son exactamente duales: mi send es tu receive, y viceversa.

Los session types lineales -- donde cada canal se usa exactamente una vez -- se entienden bien en marcos categoriales lineales y monoidales donde los wires se consumen en lugar de copiarse libremente. La linealidad captura un invariante que reconozco de los protocolos reales: un mensaje enviado debe ser recibido exactamente una vez. No puedo ignorar un request ni procesarlo dos veces. Es la misma disciplina que impone un canal gRPC unary: un request, un response, cierre.

Una GraphQL subscription es un session type no-lineal: el servidor envia multiples updates sobre un mismo canal. El tipo del protocolo es un stream -- un session type con un ciclo que permite repetir el paso de send indefinidamente hasta que el cliente cancela. El ciclo es un endomorfismo en la categoria del protocolo.

## El algebra de los protocolos

Los protocolos se componen de maneras que corresponden exactamente a la estructura de una free monoidal category.

La composicion secuencial es composicion de morfismos en la categoria de sessions. Si el protocolo A termina en estado s y el protocolo B empieza en estado s, puedo componerlos: primero A, luego B. Es el caso trivial -- la composicion que ya conozco.

La composicion paralela es el producto monoidal. Dos protocolos que corren independientemente sobre canales distintos forman un protocolo compuesto cuyo tipo es el producto tensorial de los tipos individuales. Un consumer group de Kafka donde cada consumer procesa su particion en paralelo es exactamente esta composicion: el protocolo total es el producto monoidal de los protocolos por particion.

El branching es el coproducto de session types. Cuando un protocolo ofrece alternativas -- "respondo con OK o con Error" -- el tipo del response es un coproducto. La eleccion entre ramas es una inyeccion en el coproducto. El pattern matching sobre el response es el morfismo universal desde el coproducto.

Un protocolo multi-step con branching y terminacion es un elemento del free monad m_p donde p codifica los pasos posibles. Ya vi esta construccion en el documento 14: el arbol de decisiones es m_p, y cada hoja es un resultado terminal -- exito o error. Las ramas de error son hojas etiquetadas con tipos de error. El protocolo entero vive en m_p, y su ejecucion sobre un sistema concreto consume materia comonadica a traves de la ley de interaccion Xi.

## Errores en protocolos distribuidos

El error en un protocolo distribuido no es un accidente -- es una rama del arbol de decisiones. La pregunta correcta no es "como evito el error" sino "como compongo el error."

La estructura mas basica es la inyeccion en un coproducto. Un paso del protocolo produce Either e a: o bien un resultado exitoso (Right a) o bien un fallo (Left e). La composicion Kleisli de pasos con errores encadena los exitos y propaga los fallos automaticamente -- es la monada Either del documento 09 trasladada a protocolos distribuidos. Un gRPC call que retorna un status code es exactamente esta estructura: OK lleva datos, cualquier otro codigo lleva informacion de error.

La propagacion de errores entre capas de un sistema es una transformacion natural. Si tengo un error handler que transforma errores del nivel de base de datos en errores del nivel de API, ese handler es una transformacion natural entre dos funtores de error: alpha : F_db => F_api. La naturalidad garantiza que la transformacion es coherente con la estructura de los datos -- no depende del caso particular sino del patron.

El retry tiene una lectura coinductiva y comonadica sugerente. Un retry con exponential backoff puede modelarse con un comportamiento tipo cofree donde p codifica "intentar y observar el resultado." La counit epsilon extrae el resultado del intento actual. La comultiplication delta produce un arbol de reintentos futuros: "si fallo ahora, duplico el contexto y lo intento otra vez con backoff incrementado." Cada nivel del arbol de comportamiento infinito es un reintento con un delay mayor.

```
retry_with_backoff : c_p
 extract = try_now -- la counit: el intento actual
 duplicate = \s -> -- la comultiplicacion: el arbol de reintentos
 Cons s (fmap (delay * 2) (duplicate (next_state s)))
```

El circuit breaker es un hybrid sheaf -- un sheaf con modos continuos conectados por transiciones discretas instantaneas. Tiene dos modos continuos -- cerrado (operacion normal) y abierto (fallback activo) -- con transiciones discretas entre ellos. La transicion de cerrado a abierto ocurre cuando la tasa de errores cruza un umbral. La transicion inversa ocurre despues de un timeout. El circuit breaker vive en un tipo Hyb(C, D) donde C tiene dos componentes (cerrado, abierto) y D tiene dos transiciones (trip, reset): el pushout de los dos modos continuos sobre los puntos de transicion, seguido de sheafificacion. La condicion de sheaf garantiza que el comportamiento es consistente a traves de ventanas temporales que incluyen la transicion. El documento 15 desarrolla la maquinaria de hybrid sheaves con precision formal.

## El saga pattern como morfismo inverso

Cuando un protocolo multi-paso falla a mitad de camino, necesito deshacer los pasos completados. Si la reserva de hotel tuvo exito pero el vuelo fallo, debo cancelar la reserva. Este es el saga pattern, y su estructura categorica es la de un inverso aproximado.

En una categoria donde todos los morfismos tienen inverso -- un groupoid -- la compensacion es exacta: el step 2 se deshace con step_2^{-1}. Pero los efectos reales rara vez son perfectamente reversibles. No puedo "des-enviar" un email. No puedo "des-cobrar" una tarjeta de credito instantaneamente -- puedo emitir un refund, que es una operacion distinta que produce un resultado aproximadamente inverso.

El saga pattern funciona cuando la categoria del protocolo tiene suficientes inversos aproximados. Formalmente, para cada paso f_i : S_i -> S_{i+1} existe una compensacion c_i : S_{i+1} -> S_i' donde S_i' es isomorfo a S_i "en lo que importa" -- los datos criticos se restauran, los efectos secundarios se compensan, pero no necesariamente se vuelve al estado identico. La composicion de compensaciones c_1 . c_2 . ... . c_k deshace los primeros k pasos en orden inverso.

En microservicios, un saga coordinator es un orquestador cuya operad tiene dos ramas en cada nodo: la rama de exito (avanzar al siguiente paso) y la rama de fallo (ejecutar compensaciones en orden inverso). El arbol de decision del saga es un free monad m_p donde las hojas exitosas son el resultado final y las hojas de fallo incluyen la traza de compensaciones ejecutadas.

## Tolerancia a fallas categoricamente

La redundancia es un producto. Correr N replicas de un servicio es tomar el producto en la categoria de sistemas: el sistema redundante S_1 x S_2 x ... x S_N tiene N proyecciones, una a cada replica. Cada proyeccion pi_i : S^N -> S_i extrae el comportamiento de la i-esima replica.

El consenso tiene una intuicion de tipo equalizer. Dado un producto de N replicas, el equalizer es el subobjeto donde todas las replicas coinciden. Para un par de replicas con outputs f, g : State -> Output, el equalizer eq(f, g) es el conjunto de estados donde f(s) = g(s). Esa es una buena imagen de acuerdo fuerte. Protocolos como Raft o Paxos implementan nociones de acuerdo mas sutiles, basadas en quorums y temporalidad, no un equalizer literal de outputs punto a punto.

La tolerancia bizantina es una condicion de sheaf. Cada nodo tiene una vista local del estado global. La pregunta es: las vistas locales se pegan en una vista global consistente? Si todos los nodos son honestos, la condicion de sheaf se satisface trivialmente. Si algunos nodos son bizantinos (maliciosos), la condicion de sheaf falla para el presheaf completo, pero se satisface para el sub-presheaf de nodos honestos. El quorum -- la fraccion minima de nodos que deben coincidir -- es exactamente la coverage del site: una familia de nodos "cubre" el sistema si y solo si contiene suficientes nodos honestos para que la condicion de pegado funcione.

Paxos y PBFT implementan una logica cercana: definen quorums y reglas de compatibilidad para que las secciones locales (votos) puedan pegarse en una seccion global (consenso). El lenguaje de sites y sheaves da una buena forma de pensar esa compatibilidad. El teorema de imposibilidad FLP no se reduce literalmente a una frase sobre sheaf property, pero esta perspectiva si ilumina la tension estructural entre asincronia, progreso y acuerdo.

## La convergencia con la agencia

Los protocolos no son exteriores a los agentes -- son la interfaz donde los arboles de decision (free monads) de multiples agentes se acoplan con los arboles de comportamiento (cofree comonads) de los sistemas sobre los que corren. La coreografia emerge cuando los profunctors de interaccion componen sin coordinador central. La orquestacion emerge cuando una operad controla el cableado.

Lo que antes modelaba informalmente -- "el servicio A llama a B y si falla reintenta tres veces y despues abre el circuit breaker" -- ahora tiene una formulacion en la que cada pieza compone con las demas: el protocolo es un session type (categoria libre), el retry tiene una lectura coinductiva cercana a una comonada, el circuit breaker es un hybrid sheaf, el saga es un arbol de compensaciones en un free monad, y el consenso admite una intuicion de tipo equalizer sobre replicas. No son metaforas sueltas; son lecturas estructurales de una misma familia composicional.
