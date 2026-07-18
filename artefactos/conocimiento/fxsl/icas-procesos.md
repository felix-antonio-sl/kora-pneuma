---
urn: urn:fxsl:kb:icas-procesos
nombre: icas-procesos
version: 1.1.0
estado: publicado
descripcion: "Pieza 17 del ICAS-BoK: procesos de ingeniería — requirements, design, testing y maintenance leídos como procesos categóricos, con factorización de la actividad misma."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/17-procesos.md (sha256:c950fa627bf98e9f2134a095c156549ef210369aa0431d47e382e1c9f7b291a4) el 2026-06-12. v1.1.0 (2026-07-18): corrige viewpoints, requirements/pullback, testing/end/bisimulacion, realizacion, mantenimiento y deuda."
autor: FS
creado: 2026-04-14
lang: es
tags: [requirements, design, testing, maintenance, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Procesos

## Lo que realmente hacemos cuando hacemos ingenieria

Cada proceso de ingenieria de software y sistemas --- elicitar requirements, disenar arquitectura, construir codigo, testear comportamiento, mantener en produccion --- tiene una estructura interna que rara vez hacemos explicita. Usamos herramientas, seguimos metodologias, escribimos documentos. Pero la pregunta que Bakirtzis plantea en su disertacion es mas profunda: cual es la algebra de cada proceso, y como se componen esas algebras entre si.

Su respuesta es que los modelos de requirements, los modelos de comportamiento y los modelos de arquitectura son algebras distintas sobre una categoria comun de wiring diagrams. Los requirements restringen. Los comportamientos especifican dinamica. Las arquitecturas descomponen. Cada uno tiene su propia nocion de composicion. Y la composicion vertical --- la traza formal que conecta un requirement con el comportamiento que lo satisface y la arquitectura que lo implementa --- es el aporte que la teoria de categorias hace posible. No como metafora, sino como estructura matematica verificable. Bakirtzis lo dice con claridad: la impedancia principal para construir sistemas cyber-fisicos seguros es la falta de relaciones formales entre los distintos tipos de modelos. La teoria de categorias es candidata natural para hacer esas relaciones explicitas, porque puede relacionar, comparar, y unificar algebras distintas.

## Stakeholders como objetos en una categoria de concerns

Todo sistema comienza con personas que necesitan cosas. Cada stakeholder --- el usuario final, el regulador, el equipo de operaciones, el equipo de seguridad --- tiene una perspectiva distinta sobre el mismo sistema. Vidalie lo documenta en detalle para la aeronautica: el equipo MBSE ve bloques, puertos y conexiones en SysML; el equipo MBSA ve componentes, modos de falla y arboles de falla en AltaRica 3.0. Ambos describen el mismo tren de aterrizaje, pero desde categorias distintas. El problema real que motiva su tesis es que estos modelos evolucionan independientemente --- los analistas de seguridad modifican su modelo para ajustarlo a los resultados del analisis, y esas modificaciones introducen inconsistencias con el modelo de arquitectura que nadie detecta hasta que es demasiado tarde.

Una perspectiva puede modelarse como viewpoint functor **si** existen
categorias `System`, `Concern_s`, accion sobre morfismos y leyes. Los viewpoints
DoDAF no son funtores por el solo hecho de proyectar informacion.

La compatibilidad de viewpoints puede formularse mediante limites tras definir
un diagrama comun. Requirements no "emergen" automaticamente como pullback:
necesidades conflictivas, prioridades y negociacion requieren semantica de
dominio y un objeto de comparacion tipado.

Subrahmanian y Keraron llevan esta idea al nivel de la practica industrial. Las tres estructuras fundamentales de un sistema --- funcional (que hace), fisica (de que esta hecho) y de ubicacion (donde esta) --- son tres categorias conectadas por funtores de asignacion. ISO/IEC 81346-1 formaliza estas tres estructuras como arboles de referencia con designaciones multi-nivel, y el zigzagging entre la estructura funcional y la de producto es un par de funtores que Suh teorizo como Axiomatic Design. Un requirement "la bomba debe entregar 50 m3/h en condiciones normales" se formaliza como un predicado sobre las propiedades de un objeto en la categoria funcional: [When C] -> val(O.P) in D subset Im(P). La relacion entre las categorias funcional, fisica y de ubicacion es un sistema de funtores que constituye el skeleton del information system de la ingenieria.

## Requirements como constraints formales

Un requirement suele nacer en lenguaje natural y **puede formalizarse** como
predicado/subobjeto de comportamientos si se construye el topos y su semantica.
No todo requirement (coste, proceso, obligacion social) cabe en ese objeto sin
trabajo adicional.

Una specification **puede codificarse** como sketch cuando sus constraints se
expresan mediante diagramas y límites/colímites distinguidos. Un modelo del
sketch es un funtor que satisface esas declaraciones. Esto demuestra
conformidad con la parte formalizada, no con requisitos textuales u operativos
que quedaron fuera.

Engel y Mordecai construyen un ejemplo concreto con el vehiculo electrico. La categoria del BEV tiene tipos --- Vehicle, PowerSystem, Energy --- y morfismos --- `has : Vehicle -> PowerSystem`, `uses : PowerSystem -> Energy`. La composicion `has ; uses` produce el morfismo derivado "Vehicle usa Energy." Cada requirement del BEV --- autonomia de 380 km, potencia de 239 kW, vida util de 15 anos, 12000 horas de operacion --- es un predicado sobre los atributos de los objetos de esta categoria. La Expert Knowledge Base (EKB) codifica estos predicados como design rules: un power system exhibits OpHrs, OpHrs es un Attribute con cota gteq 12000hr; un power system exhibits Lifespan, Lifespan gteq 15yr. Estas reglas forman subsets of relationship patterns que representan perspectivas integradas sobre el diseno. El conjunto de requirements forma un sub-sketch: un subgrafo del sketch completo con sus propios predicados.

Un acceptance criterion puede traducirse a una ecuacion de caminos o predicado
de sketch cuando los eventos/estados estan formalizados. Un escenario
Given-When-Then ordinario no construye por si solo el diagrama ni exige que
todos sus caminos sean iguales.

Bakirtzis formaliza los requirements como contracts. Un static contract es un predicado sobre los estados del sistema que restringe cuales son aceptables. Un assume-guarantee contract es un par (A, G) donde A son las assumptions sobre el entorno y G son las garantias del componente: si el entorno satisface A, el componente garantiza G. La composicion de contracts sigue las leyes de la categoria de wiring diagrams W: si conecto dos componentes con contracts (A_1, G_1) y (A_2, G_2) a traves de un wiring diagram, el contract del compuesto se deriva composicionalmente. Esta es la composicion horizontal --- la capacidad de componer contracts dentro de una misma algebra.

## Diseno como factorizacion de morfismos

Hay una idea en la tesis de Bakirtzis que cambio como pienso sobre el diseno. El dice que los requirements son una flecha R : Needs -> Capabilities. El diseno consiste en factorizar esa flecha a traves de una arquitectura intermedia: Needs -> Architecture -> Capabilities. La arquitectura es el "objeto intermedio" en la factorizacion.

Dentro del modelo de wiring de Bakirtzis, diseños pueden compararse como
factorizaciones. Monolito, microservicios o event-driven no son literalmente
esas flechas/productos hasta definir la categoria y demostrar que la
factorizacion realiza el mismo morfismo de requerimiento.

La calidad del diseno se mide por las propiedades de la factorizacion. Si el paso Needs -> Architecture retiene las distinciones relevantes entre requirements, la arquitectura captura lo que importa del problema. Si el paso Architecture -> Capabilities no sobrepromete y realiza solo capacidades que la arquitectura justifica, la factorizacion es sana. En el extremo ideal, esta ida y vuelta se acerca a una equivalencia de representaciones: misma estructura esencial, distinto nivel de abstraccion.

Un ADR documenta una decision y puede registrar una factorizacion categorial si
el diseño usa ese modelo. Normalmente compara tradeoffs operacionales, no
propiedades de funtores ya demostrados.

Engel formaliza esto con la Categorical Multidisciplinary Collaborative Design
(C-MCD). Las categorías de cada disciplina se integran mediante boundary
objects y funtores en el modelo citado. Los funtores `F1 : SRCat -> BOM` y
`F2 : SRCat -> ICD` llevan información común a dos representaciones, mientras
otros mappings conectan CKB, Expert Models, SIM e IDG. Comprobar compatibilidad
sobre los boundary objects es una verificación categorial del modelo; un code
review ordinario puede revisar esa obligación, pero no es idéntico a ella.

## Construccion como funtor de realizacion

La realizacion puede modelarse como funtor `R : Design -> Code` solo tras
construir categorias y una accion que preserve identidades/composicion. Es una
obligacion del modelo, no una propiedad de toda implementacion.

Si R existe, *faithful/full* describen sus mapas de hom-sets; no garantizan que
objetos, requisitos o toda semantica sobrevivan. Preservar equivalencia
observacional requiere coalgebras/observables y un teorema adicional, no solo
functorialidad.

En la practica, el funtor de realizacion rara vez es una equivalencia. Los frameworks imponen dependencias no previstas en el diseno, lo que introduce morfismos entre artefactos implementados que el diseno nunca nombro. Las limitaciones de tiempo dejan funcionalidades sin implementar o solo parcialmente realizadas. Las decisiones de implementacion agregan componentes auxiliares --- caches, loggers, circuit breakers --- que no aparecian en el diseno original. Cada desviacion entre Design y R(Design) es un punto donde la trazabilidad se pierde.

Lo que Bakirtzis llama "composicion horizontal" es la capacidad de componer modelos dentro de una misma algebra --- componer dos Moore machines para obtener una Moore machine mayor, o componer dos compositional state-space models via el algebra M sobre wiring diagrams en W. Lo que llama "composicion vertical" es la capacidad de conectar las algebras entre si: verificar que el comportamiento compuesto es consistente con los requirements, que la arquitectura descompuesta realiza el comportamiento. Una buena forma de leer esa composicion vertical es a traves del funtor de realizacion y, cuando existen, sus companeros de comparacion y verificacion. El capitulo 6 de su disertacion --- "On unification" --- argumenta que esta composicion vertical es el problema central abierto de la ingenieria de sistemas cyber-fisicos.

## Testing como verificacion de conmutatividad

Un test ejecuta casos y aporta evidencia sobre una ecuacion/comportamiento. Se
puede organizar como comprobacion de diagramas, pero un test finito no prueba
que un diagrama conmute para todos los objetos/morfismos.

Para una coalgebra explicita y un lifting adecuado, una bisimulacion puede
probar equivalencia conductual (bajo las hipotesis del funtor). Un test de
comportamiento normal comprueba trazas finitas; no verifica una bisimulacion
completa salvo que construya y cierre la relacion.

Property-based testing **muestrea/genera** muchos valores; QuickCheck no
cuantifica exhaustivamente todos los inputs. Un end requiere un bifuntor y
dinaturalidad, no solo la palabra "`forall`".

Regression testing compara observaciones en escenarios seleccionados. Puede
refutar una equivalencia conductual, pero pasar la suite no construye una
bisimulación. En una coálgebra explícita, sí puede probarse bisimilaridad
exhibiendo una relación cerrada que contenga ambos estados; los tests aportan
solo evidencia finita salvo exhaustividad demostrada.

Bakirtzis lleva esta idea al dominio de la seguridad con lo que el llama "the algebra of security tests." Un test de seguridad verifica que un ataque --- una secuencia de morfismos en la categoria del atacante --- no logra componer con los morfismos del sistema para producir un comportamiento peligroso. El razonamiento en clave Yoneda ofrece una buena forma de modelar el aprendizaje del atacante: la exploracion (attacker learning) se parece a la construccion progresiva del representable Hom(-, S) observando respuestas, y la explotacion (attacker hijacking) a la composicion exitosa de un attack path con el comportamiento del sistema.

## Mantenimiento como endofuntor evolutivo

Una secuencia de versiones y cambios puede modelarse en una categoria. Un unico
endofuntor M requiere una regla uniforme sobre todos los objetos/morfismos; el
hecho de mantener software no lo proporciona.

Algunos bugs pueden especificarse como ecuaciones de caminos rotas; otros son
rendimiento, seguridad, usabilidad o ausencia de comportamiento y no tienen esa
forma.

Agregar un feature puede extender una presentacion/cambiar una coalgebra si el
sistema fue modelado asi. Preservar diagramas existentes es una obligacion
posible, no una caracterizacion completa de compatibilidad.

Un refactor busca preservar una equivalencia observable elegida. Puede
formalizarse por isomorfismo natural o bisimulacion solo cuando existen los
funtores/coalgebras y la prueba; un morfismo de coalgebras no es
automaticamente una bisimulacion invertible.

Deuda tecnica es un concepto socio-tecnico medible por coste/riesgo de cambio.
"Non-naturality acumulada" es como maximo una metafora hasta definir dos
funtores paralelos, componentes y cuadrados concretos.

## La convergencia de los procesos

Estos procesos se retroalimentan. Pueden recibir modelos funtoriales o
algebras sobre wiring diagrams, pero no son funtores por definicion.

La teoria de categorias aporta lenguajes formales **cuando se construyen**:
subobjetos/contracts para requirements, factorizaciones para diseño, funtores
de realizacion y coalgebras de comportamiento. Testing y mantenimiento siguen
aportando evidencia/operacion; no quedan convertidos automaticamente en
ends, bisimulaciones o naturales.

## Estatuto epistemico

- **Formal:** los modelos particulares citados dentro de sus categorias y
  algebras declaradas.
- **Modelo:** traducciones de requirements, diseño, realizacion y conducta
  cuando se prueban tipos/leyes.
- **Heuristica:** acceptance criteria, tests, refactors o deuda nombrados como
  sketch/end/bisimulacion/naturalidad sin construccion.
