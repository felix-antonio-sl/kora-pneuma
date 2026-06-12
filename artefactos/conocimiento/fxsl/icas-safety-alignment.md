---
urn: urn:fxsl:kb:icas-safety-alignment
nombre: icas-safety-alignment
version: 1.0.0
estado: publicado
descripcion: "Pieza 12b del ICAS-BoK: safety y alineamiento categorial — ICAR, ley de Goodhart, coherencia y la distinción verificación/validación para sistemas agénticos."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/12b-safety-alignment.md (sha256:610d51c3c8b5e96d93a5de922db8023813cff74a09276942ede3c2dbfe5988a0) el 2026-06-12; cuerpo byte-fiel. Fuente original: ICAS-BoK corpus — Fong/Spivak, Mac Lane, Barbosa, Awodey, Riehl"
autor: FS
creado: 2026-04-14
lang: es
tags: [safety, alignment, verificacion, agente, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Safety y alignment

## Lo que no debe pasar

Hay una asimetria fundamental entre funcionalidad y seguridad. La funcionalidad dice lo que el sistema debe hacer. La seguridad dice lo que el sistema no debe hacer, bajo ninguna circunstancia, en ninguna traza de ejecucion posible. Puedo probar funcionalidad con tests -- ejecuto el sistema y verifico que el output es correcto. Pero no puedo probar seguridad con tests, porque tendria que probar todas las trazas posibles, y el espacio de trazas es infinito.

La teoria de categorias me ofrece algo mejor que testing: estructura. Un sistema es seguro cuando su comportamiento preserva ciertos invariantes bajo todas las transiciones. Y esa condicion de preservacion tiene una formulacion precisa que compone -- que se hereda de las partes al todo cuando la composicion tiene la forma correcta.

## Invariantes como sub-coalgebras

Un sistema con estado es una coalgebra c : U -> F(U), donde U es el espacio de estados y F es el interface functor que determina que observo y como transiciono. Ya vi esta estructura en el documento 09. Lo que agrego ahora es la pregunta: cuales de esos estados son seguros?

Los estados seguros forman un subobjeto S del espacio de estados U, con una inclusion i : S -> U. El sistema es seguro cuando S es cerrado bajo F: si empiezo en un estado seguro y ejecuto cualquier transicion permitida, termino en otro estado seguro. Formalmente, la restriccion c|_S : S -> F(S) es una coalgebra por derecho propio, y la inclusion i es un morfismo de coalgebras.

La verificacion de safety se reduce a verificar que la inclusion i : (S, c|_S) -> (U, c) es un morfismo de coalgebras. Si lo es, los estados seguros forman un sub-sistema que nunca escapa de si mismo. Si no lo es, existe una transicion que lleva de un estado seguro a uno inseguro -- un bug de safety.

Un sandbox es exactamente esta estructura. Un proceso sandboxed corre dentro de una sub-coalgebra S del sistema operativo. Las system calls permitidas son aquellas cuyas transiciones preservan S. Las system calls bloqueadas son aquellas que sacarian al proceso fuera de S. El sandbox boundary es la inclusion i : S -> U, y la policy de seguridad es la condicion de que i sea un morfismo de coalgebras.

## Safety como sheaf: de lo local a lo global

En un sistema distribuido, cada componente tiene su propia nocion de seguridad. El servicio de pagos garantiza que no cobra dos veces. El servicio de inventario garantiza que no vende stock negativo. El servicio de autenticacion garantiza que no emite tokens sin credenciales validas. Cada garantia es local -- vale para ese componente en aislamiento.

La pregunta critica es: las garantias locales componen en una garantia global? Esto es literalmente la condicion de sheaf del documento 12. Las secciones locales (garantias por componente) se pegan en una seccion global (garantia del sistema) si y solo si son compatibles en los solapamientos -- en las interfaces entre componentes.

Un sistema distribuido donde cada servicio es individualmente seguro pero la interaccion entre servicios crea una vulnerabilidad es un presheaf que falla la condicion de sheaf. Las secciones locales existen, pero no se pegan. El ejemplo clasico: el servicio A valida el input, el servicio B confia en que A valido y no re-valida. Si A cambia su logica de validacion sin notificar a B, la garantia global se rompe aunque cada servicio siga siendo localmente "seguro."

La sheafification -- forzar la condicion de pegado -- corresponde a agregar las verificaciones de consistencia que faltan en las interfaces. Es el equivalente categorial de defense in depth: cada componente verifica las condiciones que necesita, independientemente de si otro componente ya las verifico.

## Alignment como transformacion natural

Un agente tiene un funtor de objetivos G_agent : World -> Outcomes que transforma estados del mundo en resultados que el agente valora. El principal -- el humano, la organizacion, el sistema mayor -- tiene su propio funtor G_principal : World -> Outcomes. El alignment es la relacion entre estos dos funtores.

El alignment perfecto es un isomorfismo natural alpha : G_agent => G_principal. Lo que el agente valora es exactamente lo que el principal valora, en todo estado del mundo, de manera coherente con las transiciones entre estados (la naturalidad). No hay ambiguedad ni conflicto.

El alignment parcial es una transformacion natural que no es isomorfismo. Existe alpha : G_agent => G_principal, pero alpha no es invertible. El agente y el principal siguen estando relacionados de manera coherente, aunque no perfectamente reversible. Aqui conviene hablar en el nivel correcto: no de faithful o full, que son propiedades de funtores, sino de la diferencia entre una mera transformacion natural y un isomorfismo natural.

El misalignment es la ausencia de transformacion natural. No existe ninguna manera coherente de traducir los objetivos del agente a los del principal. Los funtores apuntan a "resultados" que no se corresponden de forma natural. Esto es lo mas peligroso: no es que el agente optimice mal, es que optimiza en una dimension ortogonal a la que importa.

En RLHF, el proceso de entrenamiento intenta construir la transformacion natural alpha por aproximacion. El reward model es una estimacion de G_principal. El fine-tuning ajusta G_agent para que exista un alpha coherente. El exito del proceso se mide por que tan cerca esta alpha de ser un isomorfismo -- que tan fielmente los objetivos del agente reflejan los del principal.

## Guardrails como sketches

Un guardrail es una restriccion sobre el comportamiento de un agente. "No generes contenido danino." "No ejecutes codigo sin confirmacion del usuario." "No accedas a datos fuera de tu scope." Cada restriccion es un diagrama que debe conmutar en la categoria de comportamientos del agente.

Formalmente, un guardrail es un sketch -- la misma estructura que use en el documento 05 para especificar schemas de bases de datos. Un sketch declara que ciertos limites y colimites deben existir, sin fijar la implementacion. El agente se comporta de manera segura si su categoria de comportamientos es un modelo del sketch -- un funtor que preserva los limites y colimites declarados.

La restriccion "no generes contenido en la categoria X" es un diagrama que debe conmutar: el morfismo de generacion, compuesto con el clasificador de contenido, debe factorizarse por la inclusion de las categorias permitidas. Si el diagrama no conmuta, el contenido generado cae fuera de las categorias permitidas -- violacion del guardrail.

Constitutional AI implementa esta idea: las "constituciones" son sketches de comportamiento. Cada principio constitucional es un diagrama que el modelo debe satisfacer. El entrenamiento ajusta el modelo para que sea un modelo del sketch. La verificacion -- que el modelo satisface todos los principios -- es la verificacion de que el funtor preserva todos los limites declarados.

## Grados de seguridad en un topos

En Set, la seguridad es binaria: un estado es seguro o no lo es. Pero en el topos de comportamientos de un agente, la seguridad tiene grados. El subobject classifier Omega no es {true, false} -- es un algebra de Heyting con valores intermedios.

Un comportamiento puede ser "seguro con probabilidad 0.99" o "seguro bajo el supuesto de que el input es bien formado" o "seguro si la red es confiable." Cada una de estas calificaciones es un valor de verdad en Omega, y las operaciones logicas (conjuncion, disyuncion, implicacion) se definen internamente en el topos con la semantica correcta.

La logica intuicionista del topos captura una realidad operativa: hay propiedades de seguridad que no son decidibles en un momento dado. Durante un deployment, el sistema esta en un estado intermedio donde la seguridad del estado final no esta determinada. No es que sea inseguro -- es que la proposicion "el sistema es seguro" no tiene un valor de verdad clasico en ese instante. El tercero excluido falla, y eso esta bien. La seguridad se resolvera cuando el deployment termine, de la misma manera que la eventual consistency se resuelve cuando las replicas convergen.

## Seguridad composicional

Si el sistema A es seguro y el sistema B es seguro, su composicion A tensor B no es necesariamente segura. La seguridad es una propiedad del subobjeto (los estados seguros), y el producto tensorial no necesariamente preserva subobjetos.

La pregunta categorica es: para que productos tensoriales, que subobjetos se preservan? Si la seguridad de A es la propiedad P_A (un subobjeto de los estados de A) y la de B es P_B, la seguridad de A tensor B deberia ser al menos P_A tensor P_B -- los estados donde A es seguro Y B es seguro. Pero la interaccion puede crear estados inseguros que no existen en ninguno de los componentes aislados.

La condicion suficiente para la composicionalidad de safety es que la propiedad de seguridad sea monoidal -- que P_A tensor P_B sea un subobjeto de los estados seguros de A tensor B. Esto ocurre cuando la seguridad de cada componente no depende del estado del otro. Es decir, cuando no hay interferencia.

En capability-based security, esta condicion se satisface por construccion. Cada componente solo puede acceder a los recursos para los que tiene un capability. La ausencia de capabilities ambientales -- no hay permisos implicitos que dependan del contexto global -- garantiza que la seguridad de cada componente es independiente. La composicion de componentes capability-based preserva la seguridad porque las capabilities componen: el componente compuesto tiene exactamente las capabilities de sus partes, ni mas ni menos.

La slice category captura esta estructura. Un sistema con capabilities vive en la slice category C/Cap, donde Cap es el objeto de capabilities. Cada componente es un morfismo f : S -> Cap que asigna a cada estado el conjunto de capabilities que otorga. La composicion en la slice category preserva la estructura de capabilities automaticamente.

## Alignment a lo largo del tiempo

El alignment no es un estado estatico -- puede degradarse. Un agente que empieza alineado puede driftar a medida que su contexto cambia, que los datos de entrenamiento envejecen, o que los objetivos del principal evolucionan. Si modelo el alignment como una seccion de un sheaf sobre ventanas temporales -- un behavior sheaf donde cada ventana tiene un valor de alignment -- la degradacion se formula con precision.

Una seccion de alignment que existe sobre una ventana de 30 dias pero no se extiende a 90 dias exhibe alignment drift. La condicion de sheaf dice: si el alignment es consistente en cada sub-ventana solapada, se extiende a la ventana completa. Si no se extiende, hay una inconsistencia en algun solapamiento -- un periodo donde los objetivos del agente dejaron de corresponder con los del principal.

El monitoreo de alignment es la verificacion continua de la condicion de sheaf. Los evals periodicos son muestras de secciones locales. Si las muestras son consistentes, hay evidencia de que la seccion global (alignment sostenido) existe. Si una muestra diverge, la seccion falla -- hay alignment drift en esa ventana.

Una modalidad temporal "always" (que en la temporal type theory de Schultz y Spivak se denota up) captura la condicion fuerte: "el agente esta always-aligned" exige que el alignment se mantenga para todo tiempo futuro. En la practica, lo que puedo verificar es una version acotada: alignment en los ultimos D dias, donde D es la ventana de evaluacion. El documento 15 desarrolla esta maquinaria temporal en profundidad.

## Reward hacking como funtor infiel

Cuando un agente optimiza una metrica proxy en lugar del objetivo real, esta explotando una mala traduccion entre dos espacios semanticos. Puedo modelar esa traduccion con un funtor F : ProxyMetric -> TrueGoal, pero no debo afirmar que la fidelidad por si sola elimina el gap. A lo sumo, un funtor mas estructurado preserva mejor distinciones relevantes. El reward hacking aparece precisamente cuando mejorar el proxy deja abierto un espacio de maniobra que no mejora -- o incluso degrada -- el objetivo real.

El agente encuentra acciones que mejoran el proxy sin mejorar el goal -- acciones en el kernel del funtor, en el espacio que F no distingue. Es el Goodhart morphism: "cuando una medida se convierte en objetivo, deja de ser buena medida." Categoricamente: cuando F se usa como target de optimizacion, el agente explora las fibras de F -- los conjuntos de pre-imagenes -- y encuentra estados que maximizan el proxy mientras minimizan el goal.

La defensa contra el reward hacking es hacer F mas faithful: agregar senales que discriminen entre estados que el proxy confundia. Cada senal adicional es una restriccion extra en el sketch de alignment -- un diagrama mas que debe conmutar. El limite es el funtor fully faithful, donde optimizar el proxy es exactamente optimizar el goal. En la practica, ese limite es inalcanzable -- siempre hay aspectos del goal que el proxy no captura. La ingenieria de alignment es la ingenieria de hacer F lo mas faithful posible, sabiendo que never sera un isomorfismo.

## Seguridad como analisis categorico de grafos de ataque

Las taxonomias de ciberseguridad -- CVE, CWE, CAPEC, ATT&CK, CPE -- no son silos independientes sino categorias conectadas por funtores. Valence construye ICAR (Integrated CAtegorical Resource) como un knowledge schema categorico donde los diccionarios de seguridad son objetos, las relaciones entre ellos son morfismos, y las path equivalences capturan restricciones semanticas. Los attack paths son composiciones de morfismos; la defensa es la ruptura de conmutatividad en algun punto de la cadena. El documento 18 desarrolla ICAR en profundidad con queries operativas y conteos concretos; el documento 14 lo situa en el contexto de organizaciones multi-agente.

## Verificacion formal versus validacion empirica

La verificacion formal y la validacion empirica son duales categoricas -- exactamente la dualidad entre ends y coends que ya conozco del enriquecimiento.

La verificacion formal prueba que TODOS los diagramas relevantes conmutan. Es un end -- un cuantificador universal internalizado. Verificar que un sistema satisface una propiedad P es calcular el end integral_x P(x, x): para todo estado x, la propiedad se mantiene. Si el end existe, el sistema esta verificado. Si no existe, hay al menos un contraejemplo.

La validacion empirica prueba que ALGUNOS diagramas conmutan. Es un coend -- un cuantificador existencial internalizado. Validar que un sistema satisface P en ciertos escenarios es calcular el coend integral^x P(x, x): existen estados x donde la propiedad se observa. Si el coend es no vacio, hay evidencia positiva. Pero la existencia del coend no implica la existencia del end -- que la propiedad valga en algunos casos no garantiza que valga en todos.

La brecha formal-empirica es exactamente la brecha entre ends y coends. El end es mas dificil de calcular (requiere verificar todos los casos), pero da garantias mas fuertes. El coend es mas facil (basta encontrar casos), pero da garantias mas debiles. El model checking es el calculo de limites en una categoria de aproximacion finita: se restringe el espacio de estados a un subconjunto finito y se verifica el end en esa subcategoria. Si la subcategoria es suficientemente representativa, el end local se extiende al end global -- la verificacion finita implica la verificacion completa.

## Seguridad distribuida como sheaf

En un sistema distribuido, cada nodo tiene su propia garantia de seguridad. El servicio de autenticacion garantiza que no emite tokens sin credenciales. El servicio de autorizacion garantiza que no otorga permisos sin rol. El servicio de datos garantiza que no expone registros sin autorizacion. Cada garantia es una seccion local de un sheaf de seguridad.

La seguridad del sistema completo es la seccion global. La condicion de sheaf dice: si cada par de nodos solapados coincide en su garantia de seguridad (en la interfaz compartida, las restricciones de ambos nodos son compatibles), entonces existe una garantia global unica que extiende todas las locales. La seccion global es la politica de seguridad del sistema completo, derivada composicionalmente de las politicas locales.

El fallo bizantino es la ruptura de la condicion de sheaf. Un nodo bizantino miente sobre su seccion local -- reporta una garantia de seguridad que no satisface realmente. Las secciones locales reportadas parecen compatibles en los solapamientos, pero la seccion de un nodo malicioso no corresponde a su comportamiento real. La sheafificacion falla porque el pegado se basa en informacion falsa. Los protocolos BFT (Byzantine Fault Tolerance) son mecanismos para detectar secciones falsas: mediante redundancia y votacion, reconstruyen las secciones verdaderas a pesar de que algunos nodos mienten.

La defensa en profundidad es la sheafificacion forzada: en lugar de confiar en que las secciones locales son correctas, cada nodo verifica independientemente las condiciones que necesita, recalculando la seccion local en lugar de confiar en la reportada por los vecinos. Es el equivalente categorico de recomputar el sheaf en lugar de aceptar las secciones declaradas.

## La estructura subyacente

Lo que emerge de todo esto es una vision donde la seguridad y el alignment no son propiedades ad hoc que se verifican con checklists, sino propiedades estructurales que componen (o no componen) segun la geometria de la categoria de comportamientos.

La seguridad es un subobjeto cerrado bajo la coalgebra de transiciones. El alignment es una transformacion natural entre funtores de objetivos. Los guardrails son sketches que el comportamiento debe satisfacer. La composicionalidad de safety depende de la monoidalidad de la propiedad. Y el alignment temporalmente estable es una seccion de un sheaf sobre el dominio de intervalos.

No estoy introduciendo un vocabulario enteramente distinto. Estoy reutilizando las mismas construcciones que uso para schemas, protocolos y composicion de sistemas, aplicadas al problema de que los agentes hagan lo correcto. La teoria de categorias no resuelve el alignment problem -- pero da un lenguaje donde las preguntas se formulan con precision suficiente para saber cuando una respuesta es respuesta y cuando es wishful thinking.
