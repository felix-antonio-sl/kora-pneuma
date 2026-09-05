---
urn: urn:fxsl:kb:icas-escala
nombre: icas-escala
version: 1.1.0
estado: publicado
descripcion: "Pieza 13 del ICAS-BoK: escala — operads, wiring diagrams, double categories, structured cospans, megamodelos y sistemas de sistemas; jerarquías de composición y verificación composicional."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/13-escala.md (sha256:a88bbf4b393dadc62cf8a14d444d886ce50587f39318ba6ab741f7399bfe5569) el 2026-06-12. v1.1.0 (2026-07-18): corrige operads, Terraform, trazabilidad/faithful, digital twins, SoS, emergencia y operadores de megamodelo."
autor: FS
creado: 2026-04-14
lang: es
tags: [operad, double-category, systems-of-systems, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Escala

## El problema de componer a lo grande

Hay un momento en la vida de todo sistema donde la composicion secuencial -- un morfismo tras otro, un pipeline tras otro -- deja de ser suficiente. Necesito componer jerarquicamente: subsistemas dentro de sistemas, equipos dentro de organizaciones, pods dentro de servicios dentro de namespaces dentro de clusters. Y necesito hacerlo manteniendo interfaces explicitas en cada frontera.

Los funtores y las transformaciones naturales que domine en los primeros documentos me dieron composicion "horizontal" -- un nivel de abstraccion a la vez. Pero la realidad de los sistemas a escala es que hay composicion en multiples dimensiones simultaneas. Una celda en un cuadro de doble categoria, donde un componente (flecha horizontal) se conecta a otro a traves de un conector (flecha vertical), captura algo que un diagrama conmutativo ordinario no puede: la distincion entre lo que el sistema ES y como se COMUNICA.

## Operads: composicion jerarquica

Una operad es una estructura que formaliza la composicion de operaciones con multiples entradas y una salida. Una operacion en una operad tiene aridad n: toma n inputs y produce 1 output. Y lo crucial es que estas operaciones se pueden anidar: si tengo una operacion f de aridad 3 y tres operaciones g1, g2, g3 de aridades 2, 1, 4 respectivamente, puedo componer para obtener una operacion f(g1, g2, g3) de aridad 2+1+4 = 7.

Para una operad no simetrica, unicolor y en `Set`, los datos basicos son:

- Para cada n >= 0, un conjunto O(n) de operaciones de aridad n
- Una operacion identidad id en O(1)
- Composicion: si f tiene aridad n y g_i tiene aridad k_i para i=1..n, entonces f(g_1, ..., g_n) tiene aridad k_1 + ... + k_n
- Leyes de asociatividad y unidad analogas a las de una categoria

Una operad permite sustitucion n-aria. El anidamiento de Kubernetes puede
motivar un algebra sobre una operad, pero la jerarquia sola no define
operaciones, colores, identidades ni leyes:

```
cluster(namespace_1(svc_a(pod_x, pod_y), svc_b(pod_z)),
 namespace_2(svc_c(pod_w)))
```

El esquema anterior es una **heuristica de anidamiento**. Para volverlo formal
hay que especificar que entradas/salida tipa cada operacion y comprobar que la
sustitucion representa semantica de despliegue.

## Wiring diagrams: la sintaxis visual

Los wiring diagrams dan una representacion visual a la composicion operadica. Un wiring diagram es una caja con puertos de entrada y salida, que puede contener cajas internas cableadas entre si. Los cables conectan puertos de salida de unas cajas a puertos de entrada de otras, y los puertos no conectados internamente se exponen como la interfaz externa de la caja contenedora.

El poder de esta representacion es que cada caja es opaca -- solo veo sus puertos. La composicion operadica dice como cablear cajas para formar cajas mas grandes. Y puedo hacer zoom: abrir una caja para ver su estructura interna, o cerrarla para tratarla como un componente atomico.

Un pipeline de CI/CD puede aportar operaciones y cableado candidatos:

```
pipeline(
 build(checkout, compile, test_unit),
 validate(lint, security_scan, test_integration),
 deploy(provision, rollout, healthcheck)
)
```

Cada stage se vuelve una operación operádica solo si tiene colores de
entrada/salida y la sustitución satisface las leyes. Los artefactos que pasan
de una stage a otra motivan los cables; estado mutable, fallos y reintentos
deben quedar incluidos para que la semántica del pipeline esté representada.

## Double categories: componentes y conectores

Hay situaciones donde una sola dimension de morfismos no alcanza. Cuando modelo una arquitectura de microservicios, tengo dos tipos de relacion fundamentalmente distintos:

- Los servicios mismos y sus dependencias funcionales (Service A llama a Service B)
- Los mecanismos de comunicacion (HTTP, gRPC, message queue, shared database)

Una double category D tiene objetos, morfismos horizontales, morfismos verticales, y 2-cells que llenan cuadrados. Lambert, en su trabajo sobre double categories of relations, formaliza esto con precision: los objetos de D_0 son los mismos para ambas direcciones, pero los morfismos horizontales (proarrows) y verticales (arrows) capturan dimensiones distintas.

En la practica, puedo modelar la arquitectura de microservicios como una double category donde:

- Los objetos son los servicios
- Los morfismos horizontales son los flujos de datos (Service A envia eventos a Service B)
- Los morfismos verticales son las dependencias funcionales (Service A requiere Service B para su operacion)
- Las 2-cells capturan la relacion entre ambas: "el flujo de datos de A a B se implementa via la dependencia funcional de A sobre B a traves del protocolo gRPC"

Si la arquitectura se construye como un equipment y las 2-celdas codifican
esas dependencias, sus leyes permiten transportar estructura. Un inventario
ordinario de servicios/flujos no hereda automaticamente analisis de impacto.

## Structured cospans: sistemas abiertos con interfaces compartidas

Un cospan en una categoria C es un diagrama A -> N <- B: dos objetos A y B que se mapean a un objeto intermedio N. Si pienso en A y B como las interfaces de un sistema y N como su implementacion, un cospan dice: "este sistema tiene interfaz izquierda A e interfaz derecha B, y ambas se conectan a la implementacion N."

Los structured cospans refinan esto exigiendo que N tenga estructura adicional -- por ejemplo, que sea un grafo, un tipo algebraico, o un diagrama en alguna categoria. La composicion de structured cospans es via pushout: para componer A -> N1 <- B y B -> N2 <- C, pego N1 y N2 por su interfaz comun B.

Un modulo Terraform puede sugerir el patron interfaz/implementacion:

- Variables de entrada (interfaz izquierda A)
- Outputs (interfaz derecha B)
- Recursos internos (implementacion N)

La conexion output-input de Terraform no es por ello un pushout. Hace falta una
categoria de modulos, un span/cospan con direcciones correctas, existencia del
colimite y prueba de universalidad; el runtime de Terraform no lo garantiza.

```
module_vpc(cidr) -> [vpc_id, subnet_ids]
module_eks(vpc_id, subnet_ids) -> [cluster_endpoint, kubeconfig]

candidate_composition(module_vpc, module_eks, interface: {vpc_id, subnet_ids})
```

## El metodo CMD: ingenieria de sistemas categorica paso a paso

Mordecai y Engel proponen un proceso concreto -- el Categorical Multimodal Design (CMD) -- para aplicar teoria de categorias a la ingenieria de sistemas reales. Lo que me resulta valioso no es solo la formalizacion, sino el proceso iterativo que definen:

**Paso 0: CMD Master.** Un equipo supervisa la consistencia de todo el diseño.
En la formalización CMD, las conexiones con la Common Design Knowledge Base
(CDKB) se representan mediante funtores; el equipo humano no es el funtor.

**Paso 1: Expert Knowledge Bases (EKB).** Cada disciplina (mecánica,
eléctrica, software, seguridad) se presenta como una categoría de diseño con
objetos, morfismos y reglas. Solo forma una fibra sobre una base común si se
construye la fibración y sus lifts cartesianos.

**Paso 2: Expert Models (EM).** Cada disciplina construye sus modelos especificos usando los tipos y relaciones de su EKB. Un EM es un diagrama en la categoria de la disciplina.

**Paso 3: Semantic Integration Model (SIM).** En el modelo, las reglas de
traducción entre disciplinas son candidatas a funtores entre categorías de
diseño y deben probar identidad/composición. La preservación de boundary
objects es una obligación adicional, no una consecuencia automática.

**Paso 4: Integrated Design Graph (IDG).** El IDG se construye como colímite
del diagrama de EMs sobre interfaces compartidas cuando ese colímite existe en
la categoría elegida y satisface la semántica de integración.

**Paso 5: Integrated Design Views (IDV).** Vistas específicas para
stakeholders, modeladas por funtores desde el IDG cuando sus acciones y leyes
están definidas.

## El BEV: un ejemplo concreto de composicion categorica

En el ejemplo del Battery Electric Vehicle que Engel detalla, la categoria base tiene tres tipos fundamentales: Vehicle, PowerSystem y Energy, conectados por los morfismos *has* (Vehicle -> PowerSystem) y *uses* (PowerSystem -> Energy). La composicion has;uses dice: todo vehiculo usa alguna forma de energia, indirectamente a traves de su power system.

En el modelo citado, las especializaciones se conectan mediante morfismos y
ecuaciones declarados; no se derivan automaticamente del nombre de los tipos:

```
BEV --is--> Vehicle --has--> PowerSystem --uses--> Energy
 | |
 canBe canBe
 | |
 BatteryPowerSystem --uses--> ElectricalEnergy
```

La composicion produce `uses''` si el diagrama y sus tipos lo permiten. Las
design rules se transportan solo si su semantica esta incluida y el mapping
preserva la estructura que expresa esas reglas; la functorialidad basica no
basta.

Los boundary objects pueden representar la interfaz común de un cospan. Su
coordinación realiza un pushout solo si la composición satisface la propiedad
universal en la categoría elegida.

## Lambda+ y la verificacion composicional de arquitecturas

Gillet, Leclercq y Cullot atacan un problema que todo arquitecto de datos enfrenta: ¿como garantizar que las propiedades de los componentes individuales se conservan en la composicion? Su formalizacion de la Lambda Architecture con teoria de categorias revela algo que la arquitectura original escondia.

Definen tres categorias: Components (los componentes del sistema), Architecture (las interacciones entre ellos), y ComponentsPS (el power set de componentes para rastrear composiciones). Los funtores CPS-Correctness y CPS-RealTime mapean composiciones de componentes a sus propiedades.

El resultado es brutal en su claridad: la Lambda Architecture original no conserva ni la propiedad de correctness ni la de real-time en la composicion total. Batch tiene Correctness = True, Speed tiene Real-time = True, pero la composicion {Batch, Serving, Speed} tiene ambas en False. La razon es categorica: si un componente individual no soporta una propiedad, la composicion la pierde.

El resultado de Lambda+ pertenece al orden de propiedades definido por ese
modelo. No es una ley general de sistemas: redundancia puede aumentar
confiabilidad y la seguridad no siempre es el minimo componente. Para obtener
una regla de meet hay que construir el preorder y demostrar que el evaluador
de composicion lo preserva.

## Manufactura como colimite

Kovalyov modela, en la categoría elegida para su aplicación de manufactura, un
producto ensamblado de partes `P` y `S` con interfaz `G` mediante un pushout:

```
 P <--f-- G --g--> S
 | |
 v v
 R = pushout(f, g)
```

En la formalizacion citada, R es el pushout del diagrama. Si ese pushout no
existe en la categoria elegida, falla **ese modelo universal**; no se deduce
que las piezas fisicas no puedan ensamblarse.

El problema inverso puede formularse como buscar factorizaciones del modelo.
Refactorizar un monolito no es automaticamente su dual categorial.

## Trazabilidad y functorialidad

Un modelo de trazabilidad puede construir categorias `Requirements`,
`Architecture`, `Code` y funtores entre ellas. Entonces la composicion conserva
identidades y relaciones **segun los morfismos que el modelo haya definido**.

No obstante, *faithful* significa inyectividad en hom-sets, no distincion de
objetos: dos requisitos pueden mapearse al mismo objeto sin que el funtor deje
de ser fiel. Tampoco existe un "kernel del funtor" generico con el sentido
usado para mapas lineales, ni esencial sobreyectividad equivale a cobertura
bidireccional de trazas.

La cobertura operativa se comprueba directamente con una relacion/grafo:
cada requisito exigido tiene al menos una implementacion trazada y cada
artefacto que deba justificarse tiene al menos un requisito. Solo despues, si
las categorias y leyes aportan valor, se estudian fidelidad, imagen o
propiedades adjuntas.

## Simulacion como ejecucion de morfismos

Una simulacion ejecuta un camino especifico de morfismos en la categoria del sistema y observa el resultado. Dado un estado inicial s0 y una secuencia de transiciones f1, f2, ..., fn, la simulacion calcula fn . ... . f2 . f1 (s0) -- la composicion evaluada en el estado inicial.

La simulacion Monte Carlo es el muestreo de caminos aleatorios. Cada camino es una secuencia de morfismos en la categoria de Kleisli de una monada de probabilidad P. El morfismo Kleisli f : A -> P(B) no produce un resultado determinista sino una distribucion sobre resultados. La composicion Kleisli de n pasos produce una distribucion sobre estados finales. Muestrear K caminos y promediar los resultados es la aproximacion Monte Carlo del valor esperado -- la integral sobre la medida que la monada P define.

Un digital twin puede modelarse mediante un funtor de simulacion si se
construyen ambas categorias. Ser fiel solo distingue morfismos dentro de cada
hom-set; no significa que "todo lo fisico" este en el modelo. Calibracion exige
una metrica/relacion entre observaciones reales y simuladas, no se reduce a un
kernel funtorial ni a full faithfulness.

## Systems of Systems formalmente

Un SoS **puede** modelarse mediante una 2-categoria si cada constituyente,
interfaz y adaptacion realiza los tipos y coherencias correspondientes. La
taxonomia de gobernanza no determina por si sola esa estructura.

Los tipos de SoS reconocidos por la ingenieria de sistemas tienen formulaciones 2-categoricas distintas.

Un Acknowledged SoS tiene gobernanza central; esto puede representarse con
morfismos de coordinacion, pero no implica strictness ni naturalidad.

Un Collaborative SoS puede motivar celdas lax/pseudonaturales, siempre que se
construyan. Negociacion organizacional no equivale a debilidad categorial.

Un Virtual SoS carece de coordinacion central, pero puede tener interacciones;
no es por ello un coproducto disjunto ni sus propiedades son una union simple.

Un colimite puede construir un sistema compuesto a partir de un diagrama. La
propiedad universal no crea ni explica automaticamente emergencia, resiliencia
o inteligencia, y la ausencia de un colimite en una categoria elegida no
impide comportamiento emergente en el sistema real.

## Megamodelos: el modelo de los modelos

Un System of Systems tiene una estructura que va más allá de la composición: tiene un **megamodelo** -- un modelo cuyos elementos son otros modelos. Schultz et al. formalizan esta idea en el Algebraic Model Management: un megamodelo es un grafo donde los nodos son modelos (objetos de información) y las aristas son relaciones semánticas entre ellos -- instanciación, transformación, traza, conformidad. En la jerarquía DIK, el megamodelo vive en el nivel de **Knowledge**: no es un modelo del sistema sino un modelo de los modelos del sistema. Es la conciencia del SoS sobre su propia estructura.

Operadores Match/Merge/Diff/Split/Compose pueden recibir realizaciones
categoriales en frameworks concretos. Los nombres no implican
pullback/pushout/complemento, y una propagacion de cambios solo es natural tras
definir los funtores y verificar sus cuadrados.

## Composicion a escala: la perspectiva unificada

Lo que une operads, double categories, structured cospans y el método CMD es
una intuición: componer a escala requiere explicitar interfaces. Jerarquías,
relaciones de varias clases e interfaces compartidas **pueden modelarse**
respectivamente con esas estructuras; los sistemas reales no las realizan por
su forma visual.

El método CMD de Mordecai y Engel traduce esta intuición a un proceso de
ingeniería que construye categorías de diseño, boundary objects y mappings
entre vistas. Su lectura categorial exige verificar cada funtor y cada
propiedad universal del modelo integrado.

Para la práctica diaria, la lección es que la composición se vuelve frágil si
las interfaces son implícitas. La teoría de categorías puede formalizar una
semántica de esas interfaces y verificar propiedades del modelo antes de
construir; no certifica por sí sola la corrección del sistema físico o
operacional.

## Estatuto epistemico

- **Formal:** operads, double categories/equipments y structured cospans bajo
  sus definiciones.
- **Modelo:** CMD, BEV, Lambda+ y manufactura dentro de los papers citados.
- **Heuristica:** Kubernetes/Terraform/SoS/digital twins promovidos a esas
  estructuras sin tipos, leyes y prueba universal.
