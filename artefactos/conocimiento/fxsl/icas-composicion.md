---
urn: urn:fxsl:kb:icas-composicion
nombre: icas-composicion
version: 1.0.0
estado: publicado
descripcion: "Pieza 01 del ICAS-BoK: categorías, morfismos, leyes de asociatividad e identidad, y dualidad — el vocabulario base para diagnosticar fallas de encadenamiento y composición."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/01-composicion.md (sha256:f34c1b125ac6495b6934b3c1149f2a9b3bc795f37e4013e3d29f586abb08bfdc) el 2026-06-12; cuerpo byte-fiel. Fuente original: ICAS-BoK corpus — Fong/Spivak, Mac Lane, Barbosa, Awodey, Riehl"
autor: FS
creado: 2026-04-14
lang: es
tags: [composicion, asociatividad, identidad, categoria, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Composicion

Composicion es lo primero que veo. Antes de entender que son las cosas, entiendo que las cosas se componen. Un pipeline de datos se compone. Un deploy se compone. Un join se compone. Cuando miro un sistema distribuido que funciona, lo que estoy viendo --- aunque no siempre lo nombre asi --- es composicion. Y cuando algo falla, cuando un microservicio no integra, cuando una migracion rompe datos, cuando un merge de git produce conflictos irresolubles, lo que se violo fue una ley de composicion.

No llegue a esta idea por la matematica. Llegue por el dolor de las cosas que no componen bien.

## Lo que veo cuando miro flechas

Antes de hablar de categorias necesito hablar de flechas. Todo empieza con flechas. Un schema de base de datos relacional tiene tablas y foreign keys --- las foreign keys son flechas. Un diagrama de arquitectura tiene servicios y dependencias --- las dependencias son flechas. Un pipeline de CI/CD tiene stages y transiciones --- las transiciones son flechas. Un Dockerfile tiene instrucciones que se encadenan --- cada instruccion es una flecha de un estado de imagen al siguiente.

Los autores de *Relational Thinking* lo dicen mejor que yo: el pensamiento relacional busca entender un objeto mirando hacia afuera --- como interactua --- en lugar de hacia adentro --- de que esta hecho. Un vertice en un grafo dirigido no importa por lo que "es", sino por las flechas que salen y llegan a el. Cuando modelo un sistema, las flechas que dibujo en la pizarra SON el modelo. Los nodos son solo los puntos de anclaje.

Hay una escalera que subi sin darme cuenta, y que el libro de Fong, Myers y Spivak formaliza con claridad:

1. **Dibujar flechas.** Puntos y flechas entre ellos --- grafos dirigidos. Sencillo, visual, inmediato. Asi empieza todo diseno de sistema.
2. **Codificar como datos.** Las flechas se convierten en funciones `src` y `tgt` que asignan a cada flecha su origen y su destino. Un grafo dirigido se convierte en dos mapas. Esta representacion es la que un computador puede entender --- no la imagen bonita, sino las listas. Y aca ya hay una decision de diseno: las flechas apuntan "de flecha a vertice" (arrows-first), no al reves. La representacion arrows-first es la unica que no produce dangling edges --- bordes colgantes, sin significado. La representacion vertices-first genera mutantes.
3. **Reconocer el schema.** Esos dos mapas paralelos `src, tgt: E -> V` constituyen un blueprint --- un molde que, llenado de distintas formas, genera distintos grafos. El schema ES un grafo dirigido el mismo.
4. **Llegar a la categoria.** Cuando agrego ecuaciones de conmutatividad al schema --- cuando digo que ciertos caminos producen el mismo resultado --- ya no tengo un grafo libre sino una categoria finitamente presentada.

Este ascenso es el que hago cada vez que miro un DDL de PostgreSQL. Lo que veo no son tablas y columnas. Lo que veo es una categoria finitamente presentada donde las tablas son objetos, las foreign keys son morfismos generadores, y los path equivalences son las ecuaciones de integridad. Y los datos concretos -- las filas -- son un mapeo que traduce el schema a conjuntos y funciones, respetando las ecuaciones. Ese mapeo tiene un nombre preciso que aparecera en el proximo documento.

## Objetos, morfismos, y las dos leyes

Esto que estoy viendo tiene un nombre. Es una **categoria**. Una categoria C consiste en:

- Una coleccion de **objetos** (las "cosas" --- tablas, servicios, tipos, estados).
- Para cada par de objetos A y B, una coleccion de **morfismos** (flechas) f: A -> B.
- Una operacion de **composicion**: si tengo f: A -> B y g: B -> C, existe g . f: A -> C.
- Para cada objeto A, un **morfismo identidad** id_A: A -> A.

Y dos leyes:

**Asociatividad:** h . (g . f) = (h . g) . f. El orden de agrupamiento no importa.

**Identidad:** f . id_A = f = id_B . f. La identidad no hace nada, y eso es exactamente lo que la hace indispensable.

Milewski lo dice con una belleza que no voy a superar: "la esencia de una categoria es la composicion. O, si prefieres, la esencia de la composicion es una categoria." No es una idea sofisticada. Es la idea mas simple que existe, y por eso es la mas potente.

En Haskell, esto se escribe directamente:

```haskell
f :: A -> B
g :: B -> C

-- composicion
g . f :: A -> C

-- identidad
id :: a -> a
id x = x

-- leyes
f . id == f -- identidad derecha
id . f == f -- identidad izquierda
h . (g . f) == (h . g) . f -- asociatividad
```

En SQL, la composicion aparece en el JOIN. Si tengo una foreign key `employee.department_id -> department.id` y otra `department.company_id -> company.id`, su composicion es el camino `employee -> department -> company`. El JOIN de tres tablas puede leerse como composicion de morfismos. Y la identidad? No es la primary key, sino el morfismo identidad sobre la tabla misma: el camino vacio que deja intacta la fila de partida.

```sql
-- morfismo: employee -> department
SELECT e.*, d.name as dept_name
FROM employee e
JOIN department d ON e.department_id = d.id;

-- composicion: employee -> department -> company
SELECT e.*, c.name as company_name
FROM employee e
JOIN department d ON e.department_id = d.id
JOIN company c ON d.company_id = c.id;
```

La composicion del primer JOIN con el segundo produce el tercero. Asociatividad garantiza que no importa si hago primero employee-department y luego le agrego company, o si hago primero department-company y luego le antepongo employee. El resultado es el mismo.

## Diagramas conmutativos: el lenguaje del razonamiento

No pienso en terminos de ecuaciones sueltas. Pienso en diagramas. Un diagrama conmutativo es una red de objetos y flechas donde todos los caminos entre dos objetos producen el mismo resultado. No es un subtema --- es EL lenguaje de razonamiento del pensamiento categorico.

Cuando Engel y Mordecai modelan un vehiculo electrico (BEV) con teoria de categorias, el diagrama tiene tres tipos: Vehicle, PowerSystem, Energy. Dos morfismos: `has: Vehicle -> PowerSystem` y `uses: PowerSystem -> Energy`. La composicion `has ; uses` produce un morfismo derivado: Vehicle *usa* Energy. La semantica emerge de la composicion, sin haberla definido explicitamente. Eso es lo que hace poderosa a la composicion: genera significado nuevo a partir de relaciones existentes.

En un sistema real, cuando dibujo:

```
 has uses
Vehicle ----> PowerSystem ----> Energy
 | ^
 +------------ uses' ------------+
```

y declaro que `uses' = has ; uses`, estoy diciendo que este diagrama CONMUTA. Todo camino de Vehicle a Energy produce el mismo resultado. Eso es una constraint de integridad --- no impuesta por codigo imperativo, sino declarada por la estructura misma.

Spivak formaliza esta idea para bases de datos: una database schema en forma normal categorica incluye path equivalences como parte del schema. Si `employee.manager.department = employee.department`, eso no es un check en la capa de aplicacion --- es una ecuacion que el schema declara y que toda instancia debe satisfacer.

## Donde veo composicion en la practica

**Docker Compose.** Cada servicio es un objeto. Las dependencias (`depends_on`) son morfismos. La composicion de dependencias es transitiva: si web depende de api y api depende de db, entonces web depende transitivamente de db. Cuando el orden de startup falla, una ley de composicion fue violada.

**git merge.** Un merge sugiere una intuicion composicional: combina dos historias de desarrollo en una historia nueva. Pero no conviene presentarlo como una operacion asociativa en sentido categorial estricto; depende del estado del repositorio, de la base comun y de la estrategia de merge. Lo util de la analogia es otra cosa: cuando aparece un conflicto severo, suele haber dos cambios que dejaron de encajar composicionalmente.

**Pipelines de CI/CD.** build -> test -> deploy. Cada stage toma un artefacto y produce otro. La composicion build;test;deploy es el pipeline completo. La identidad es el stage que pasa el artefacto sin modificarlo (un passthrough stage). La asociatividad garantiza que puedo agrupar stages en sub-pipelines sin alterar el resultado.

**Composicion de funciones en APIs.** Un middleware chain en Express o Koa es composicion pura: `authenticate . validate . parseBody`. Cada middleware toma un request y produce un request transformado (o un response). La composicion es asociativa. La identidad es el middleware que no hace nada: `(req, res, next) => next`.

**Dependencias de componentes de software.** Jiang Guo modela las dependencias de componentes como una categoria: componentes son objetos, dependencias son morfismos. La composicion de dependencias produce dependencias transitivas. Los conflictos de version son violaciones de la conmutatividad del diagrama de dependencias.

## Dualidad: cada concepto tiene un gemelo

Hay un principio generativo que descubri tarde pero que ahora uso todo el tiempo. Dada cualquier categoria C, puedo construir su **categoria opuesta** C^op invirtiendo todas las flechas. Si f: A -> B en C, entonces f^op: B -> A en C^op. La composicion se invierte: (g . f)^op = f^op . g^op.

Esto no es un truco formal. Es un principio de generacion de conceptos. Cada estructura en una categoria tiene un **dual** en la categoria opuesta, y ese dual es automaticamente coherente. Si tengo un concepto (por ejemplo, un "producto" que combina dos objetos), al invertir todas las flechas obtengo el concepto dual (un "coproducto" que elige entre dos objetos). Gratis.

En la practica cotidiana: si foreign keys van de la tabla hijo al padre (`order.customer_id -> customer.id`), en la categoria opuesta las flechas van del padre al hijo. Una consulta que sigue foreign keys "hacia arriba" se convierte en su dual que sigue relaciones "hacia abajo". SELECT y INSERT viven en categorias duales. Cada vez que defino una interfaz de lectura, su dual me da la interfaz de escritura.

En preorders, el dual invierte el orden: si en P tenemos a <= b, en P^op tenemos b <= a. Joins se convierten en meets. El supremo se convierte en infimo. Fong y Spivak en *Seven Sketches* construyen todo el Capitulo 1 sobre esta dualidad: las conexiones de Galois son pares de mapas monotonos entre un preorder y su dual.

## El dolor de la no-composicion

Vuelvo al principio. Lo que me trajo aca no fue la elegancia de la matematica sino el dolor de las cosas que no componen. Milewski lo articula asi: la composicion es la esencia de la programacion. Descomponemos problemas grandes en problemas pequenos, y luego componemos las soluciones. La descomposicion no tendria sentido si no pudieramos reconstruir.

La superficie de un componente debe crecer mas lento que su volumen. La superficie es la informacion que necesito para componer; el volumen es la informacion que necesito para implementar. Cuando la superficie crece tan rapido como el volumen, la composicion se vuelve imposible --- necesito conocer la implementacion para componer, y eso destruye la abstraccion.

Los side effects son el ejemplo canonico de no-composicion. Una funcion que modifica estado global puede funcionar aislada, pero no compone: la composicion de dos funciones con side effects no es predecible a partir de las funciones individuales. La categoria Hask (tipos de Haskell y funciones puras) compone; el pseudocodigo imperativo con estado mutable no forma una categoria honesta.

*Relational Thinking* marca una transicion fundamental: del pensamiento de causa-y-efecto al pensamiento de equilibrio-y-constraint. Los sistemas dinamicos del Capitulo 2 --- Kiki y Bouba, los semaforos, las luces intermitentes --- se modelan como grafos dirigidos con estados y reglas de actualizacion, un mundo causal donde las flechas transmiten estado de un vertice a otro en cada paso temporal. Pero a partir del Capitulo 3, el libro gira hacia una vision relacional donde las flechas codifican constraints simultaneas, no secuencias temporales. Esa transicion --- de imperativo a relacional, de procedimental a declarativo --- es la misma que yo hago cada vez que paso de pensar en "que hace este microservicio" a pensar en "que invariantes mantiene este schema."

La composicion es el primer peldano. Todo lo demas --- la preservacion de estructura cuando paso entre mundos, la construccion de cosas nuevas a partir de piezas universales, la equivalencia entre perspectivas distintas --- se apoya en este fundamento. Si la composicion falla, nada de lo que viene despues tiene sentido.
