---
urn: urn:fxsl:kb:icas-patrones
nombre: icas-patrones
version: 1.1.0
estado: publicado
descripcion: "Pieza 19 del ICAS-BoK: patrones — patrones arquitectónicos y agénticos, anti-patrones y wrapper functors; reconocer y nombrar estructura recurrente."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/19-patrones.md (sha256:a117e270a4e4791d7033f361cbb016f62080564ab8763bcd512077a96a582ef5) el 2026-06-12. Corrección epistémica 1.1.0 (2026-07-18): se distinguen instancias formales de modelos y analogías."
autor: FS
creado: 2026-04-14
lang: es
tags: [patron, construccion-universal, anti-patron, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Patrones

## La intuicion que ya tenia nombre

Los patrones de diseño y las construcciones categoriales pueden compartir
forma, pero el puente no es automáticamente una identificación. Un patrón
concreto es una instancia formal solo cuando se definen categorías, morfismos
y una propiedad universal o leyes que realmente satisface. En los demás casos
la lectura es un modelo o una analogía disciplinada.

Lo que me propongo aqui es hacer explicita esa lectura. Algunos patrones clasicos de diseno tienen una contraparte categorica muy cercana; otros solo admiten una analogia disciplinada. Los anti-patrones pueden describirse como violaciones de propiedades categoricas utiles. Y la tension entre heuristicas y metodos formales -- la tension que define la practica cotidiana de la ingenieria -- se deja leer muy bien con la geometria de una adjuncion, aunque no siempre como una adjuncion literal ya presentada.

## Patrones de diseno como construcciones universales

El patron Observer puede leerse en clave representable. Un sujeto S que notifica a multiples observadores recuerda la situacion de Yoneda: el sujeto induce un funtor Hom(S, -) que a cada objeto O le asigna maneras de observar a S. No necesito afirmar que todo Observer concreto sea literalmente un representable; me basta con que la intuicion correcta sea relacional y externa.

El patron Factory suele acercarse a una construccion libre. La fabrica toma una especificacion minimal (un tipo, unos parametros) y produce el objeto mas general que satisface esa especificacion. Ese gesto se parece mucho al de un funtor libre F : Set -> C: dado un conjunto de generadores, construye el objeto libre en C. La propiedad universal da la intuicion correcta, aunque una factory concreta de software pueda imponer muchas restricciones extras de implementacion.

El patron Adapter se deja modelar como una transformacion natural cuando las dos interfaces realmente son funtores sobre la misma categoria de entradas. En ese caso, un adapter alpha : F => G proporciona, para cada objeto A, un morfismo alpha_A : F(A) -> G(A) tal que la naturalidad se satisface: para todo morfismo f : A -> B, el diagrama conmuta. En codigo, un adapter que traduce de `XMLParser` a `JSONParser` aspira a esa coherencia composicional.

Strategy puede organizarse como una familia parametrizada. Un funtor desde un
producto/tensor de estrategias e inputs exige categorías y una acción que
preserve morfismos; el tensor solo expresa la independencia que su modelo haya
codificado.

Decorator sugiere una lectura monádica solo si envolver define un endofuntor y
hay unit/multiplication naturales con leyes. Los wrappers reales no suelen ser
idempotentes —doble buffering no se elimina necesariamente— y el patrón por sí
solo no suministra una mónada.

El tipo de árboles binarios bien fundados puede construirse como álgebra inicial
de `F(X)=Leaf+Node(X,X)`, y su fold es el catamorfismo. Un Composite de UI
real puede tener listas, sharing, ciclos o efectos; `render` realiza esa lectura
solo si su estructura y álgebra coinciden con el modelo.

## Patrones arquitectonicos categoricamente

Los patrones arquitectónicos motivan modelos categoriales, pero el patrón no
determina por sí solo categorías ni leyes.

Un grafo de microservicios puede generar una categoría libre cuyos objetos son
servicios y cuyos morfismos son caminos de llamadas. Si A llama a B y B a C,
la composición es el camino A-B-C, no necesariamente una llamada directa A-C.
La asociatividad permite reagrupar la concatenación del mismo camino. La
identidad es el camino vacío, no un health-check.

Una arquitectura en capas puede modelar traducciones entre categorías. Solo son
funtores después de definir qué morfismos preservan; una relación de datos no
tiene por qué sobrevivir como relación visual.

Una arquitectura event-driven admite un modelo coalgebraico tras fijar estados,
observaciones y transición `c:S->F(S)`. Publicación/suscripción no vuelve
coalgebraica a la arquitectura, ni «coalgebraico» es el opuesto de invocación.

Un pipeline puede ser composición de Kleisli si todos los stages usan una
mónada común `T`. `Maybe` pierde diagnósticos y no modela por sí solo CI/CD;
`Writer` modela acumulación monoidal de logs, no todos sus efectos.

## Patrones agenticos

Los siguientes son modelos candidatos para patrones agénticos. Cada lectura
debe verificarse contra los datos categoriales que exige; el nombre del patrón
no suministra esos datos.

ReAct (Reason + Act) alterna razonamiento y acción. Puede inspirarse en
pattern-runs-on-matter, pero un loop ReAct no es por eso una mónada libre
actuando sobre una comónada cofree. La instancia formal requiere polinomios,
la categoría `Poly` y la acción de módulo concreta de Libkind-Spivak.

Una traza de razonamiento **puede representarse** como camino en la categoría
libre generada por un grafo de pasos. Esa construcción registra sintaxis de
caminos; no vuelve válidos los razonamientos ni identifica dos caminos por
tener el mismo destino. Tales equivalencias requieren imponer relaciones o
una semántica que las demuestre.

RAG es operacionalmente una tubería de consulta, recuperación, ensamblado de
contexto y generación. Puede modelarse mediante un pullback solo si existen
dos flechas tipadas hacia un objeto común de relevancia y el objeto de pares
compatibles satisface su propiedad universal. Un retriever por similitud no
aporta eso automáticamente; sin la construcción, «pullback» es heurística.

El debate multiagente es un procedimiento deliberativo. Podría modelarse por
un coequalizer si las respuestas son flechas paralelas y el resultado es el
cocono universal que las iguala. El voto, la síntesis o la decisión de un juez
no satisfacen necesariamente esa propiedad. La inexistencia de un coequalizer
en una categoría escogida tampoco implica imposibilidad práctica de consenso.

## Anti-patrones como propiedades categoricas rotas

Si los patrones son construcciones universales, los anti-patrones son violaciones de propiedades categoricas.

El God Object es un objeto con demasiados morfismos entrantes y salientes -- un objeto que participa en casi todos los hom-sets de la categoria. Categoricamente, es un objeto cuyo funtor representable Hom(G, -) tiene demasiada estructura, lo que significa que G "sabe demasiado" sobre el resto de la categoria. La solucion es factorizar: descomponer G en un diagrama de objetos mas pequenos cuyo colimite sea G, de modo que cada parte tenga responsabilidad acotada.

La dependencia circular es un ciclo en un grafo de dependencias. Las
categorías generales permiten ciclos y endomorfismos no triviales; no son
«bien fundadas» por definición. Si el dominio exige un DAG, la aciclicidad es
un invariante del modelo. Si el ciclo es legítimo, debe darse una semántica de
feedback o punto fijo y estudiar su existencia/convergencia por separado.

El tight coupling suele delatar una interfaz mal calibrada. Si el paso de la estructura interna a la interfaz externa colapsa distinciones importantes o deja aparecer dependencias que la interfaz no deberia exponer, tengo acoplamiento fuerte. A veces eso puede describirse con fallas de faithfulness o fullness, pero conviene no usar esos terminos como sinonimos generales de "mal encapsulado".

Feature Envy puede sugerir una factorización a través de la interfaz de otro
módulo. No existe una «categoría equivocada» sin un modelo de módulos,
dependencias y ownership; incluso con la factorización, mover el método sigue
siendo una decisión de cohesión y encapsulamiento, no un teorema.

## Heuristicas versus metodos formales

La tensión entre heurísticas y métodos formales puede sugerir una adjunción
entre relajación y formalización, pero solo es literal tras definir sus
categorías, órdenes de aproximación y la equivalencia natural de hom-sets.

Como esquema de diseño, `L` formaliza y `R` relaja. Llamar `L ⊣ R` a ese
esquema es una hipótesis a probar, no una consecuencia de sus nombres.

Si se construyera `L ⊣ R`, unit y counit expresarían comparaciones en las
categorías elegidas. No miden una distancia salvo que exista además un
enriquecimiento/métrica, ni significan por sí mismas «ruido» o pérdida.

Las heurísticas pueden interferir y los métodos formales pueden aportar pruebas
relativas a un modelo. Ni unas son «morfismos aproximados» por definición ni
formalizar invariantes garantiza que su composición sea válida o que el
compilador los verifique.

## Wrapper functors: integración multi-modelo

Un patrón de integración que combina varias de estas ideas es el **wrapper functor** para entornos multi-modelo. Cuando una arquitectura combina PostgreSQL, MongoDB y Neo4j, cada base de datos tiene su propio "idioma" categorial: tablas y foreign keys, documentos y embedding, nodos y aristas. El patrón consiste en definir un **Schema Category global** cuyos objetos son tipos lógicos unificados y cuyos morfismos son relaciones semánticas, y construir un wrapper functor W_db : DB_specific → SchemaCategory para cada base de datos. W_postgres mapea tablas a tipos, foreign keys a morfismos. W_mongo mapea collections a tipos, nested refs a morfismos. W_neo4j mapea node labels a tipos, edge types a morfismos.

Cada wrapper **se diseña como candidato a funtor** y debe demostrar que
preserva identidad y composición. Solo entonces una traducción de queries
puede heredar garantías functoriales; una capa adaptadora ordinaria no las
obtiene por llamarse wrapper.

## Co-design como lattice de problemas de diseno

La monotone co-design theory de Censi, formalizada en el ACT4E de Fong y Spivak, ofrece un marco donde los problemas de diseno forman una estructura de lattice. Un Design Problem with Implementation (DPI) es una tupla (F, R, I, prov, req) donde F es un poset de funcionalidades, R es un poset de recursos, I es un espacio de implementaciones, prov : I -> F mapea cada implementacion a la funcionalidad que provee, y req : I -> R mapea cada implementacion a los recursos que requiere.

La dualidad entre funcionalidad y recursos es fundamental: la funcionalidad es un lower bound (lo minimo que debo proveer), los recursos son un upper bound (lo maximo que puedo consumir). El diseno es factible cuando existe una implementacion i tal que prov(i) >= f_min y req(i) <= r_max.

Los DPIs se componen: si el motor provee torque y requiere electricidad, y el chasis provee movilidad y requiere torque, la composicion en serie conecta el output del motor al input del chasis. Los DPIs forman una semicategoria donde la composicion preserva la estructura de poset. Y los design problems (sin implementacion, solo la relacion funcionalidad-recursos) forman un lattice: el meet de dos design problems es la interseccion de disenos factibles (ambos constraints se satisfacen), el join es la union (al menos un constraint se satisface).

Esta estructura ordenada formaliza una clase concreta de problemas de
co-diseño. La monotonía preserva el orden de funcionalidad/recursos definido
por el modelo; que sub-diseños factibles compongan en un diseño global factible
depende además de los operadores de composición y sus teoremas.

Heyn et al. extienden esta perspectiva al framework arquitectonico: las vistas arquitectonicas forman un lattice parcialmente ordenado por nivel de detalle, con funtores de correspondencia entre niveles. La consistencia del framework es la condicion de que el producto de vistas en cada nivel sea valido -- que los diagramas conmuten. Un framework arquitectonico composicional permite agregar clusters of concern sin romper la estructura existente, porque la adicion es un join en el lattice.

## La convergencia practica

Lo que emerge es una disciplina de diagnóstico: empezar por la intuición del
patrón y preguntar después qué estructura puede realmente tiparse y probarse.
La composabilidad es una ganancia solo cuando se verifican las leyes; en los
demás casos la categoría orienta, no certifica.

Los anti-patrones pueden reformularse como invariantes verificables cuando el
modelo está definido: aciclicidad de un grafo de dependencias, límites de
acoplamiento o una factorización concreta. El vocabulario categorial obliga a
nombrar la estructura exacta en vez de usar una palabra técnica como
diagnóstico autosuficiente.

## Corrección 1.1.0

Se corrigen cuatro identificaciones universales falsas: patrón de software no
equivale por defecto a construcción universal; RAG no es pullback sin su
propiedad universal; debate no es coequalizer por el mero hecho de buscar
consenso; y una categoría no prohíbe ciclos. El resto se lee con el estatus
más débil suficiente: formal, modelo o heurística.
