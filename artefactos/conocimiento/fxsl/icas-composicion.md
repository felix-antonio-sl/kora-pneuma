---
urn: urn:fxsl:kb:icas-composicion
nombre: icas-composicion
version: 1.1.0
estado: publicado
descripcion: "Pieza 01 del ICAS-BoK: categorías, morfismos, leyes de asociatividad e identidad, y dualidad — el vocabulario base para diagnosticar fallas de encadenamiento y composición."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/01-composicion.md (sha256:f34c1b125ac6495b6934b3c1149f2a9b3bc795f37e4013e3d29f586abb08bfdc) el 2026-06-12. v1.1.0 (2026-07-18): separa grafos de categorias y corrige analogias operacionales sobre JOIN, side effects, pipelines y dependencias."
autor: FS
creado: 2026-04-14
lang: es
tags: [composicion, asociatividad, identidad, categoria, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Composicion

Composicion es lo primero que veo. Antes de entender que son las cosas, entiendo que las cosas se componen. Un pipeline de datos se compone. Un deploy se compone. Un join se compone. Cuando algo falla, una lectura composicional puede localizar incompatibilidades, pero no toda falla operacional viola asociatividad o identidad categorial.

No llegue a esta idea por la matematica. Llegue por el dolor de las cosas que no componen bien.

## Lo que veo cuando miro flechas

Antes de hablar de categorias necesito hablar de flechas. Un schema, un diagrama de arquitectura o un pipeline aporta **aristas candidatas**. Solo son morfismos despues de declarar identidades, composicion, tipos y ecuaciones. Si se parte de un grafo, la categoria libre de caminos es una construccion posible, no una propiedad inherente del dibujo.

Los autores de *Relational Thinking* lo dicen mejor que yo: el pensamiento relacional busca entender un objeto mirando hacia afuera --- como interactua --- en lugar de hacia adentro --- de que esta hecho. Un vertice en un grafo dirigido se caracteriza, dentro de ese grafo, por las flechas que salen y llegan a el. Cuando dibujo un sistema, esas flechas forman el grafo generador del modelo; aún debo decidir cuáles se componen y qué ecuaciones satisfacen.

Hay una escalera que subi sin darme cuenta, y que el libro de Fong, Myers y Spivak formaliza con claridad:

1. **Dibujar flechas.** Puntos y flechas entre ellos --- grafos dirigidos. Sencillo, visual, inmediato. Asi empieza todo diseno de sistema.
2. **Codificar como datos.** Las flechas se convierten en funciones `src` y `tgt` que asignan a cada flecha su origen y destino. Es una representacion total y util; otras codificaciones tambien pueden impedir aristas colgantes mediante tipos o constraints.
3. **Reconocer el schema.** Esos dos mapas paralelos `src, tgt: E -> V` constituyen un blueprint --- un molde que, llenado de distintas formas, genera distintos grafos. El schema ES un grafo dirigido el mismo.
4. **Llegar a la categoria.** Primero genero la categoria libre (caminos, identidades y concatenacion) y luego, si corresponde, cociento por las ecuaciones de caminos. El resultado es una categoria presentada por generadores y relaciones.

Este ascenso puede aplicarse a un fragmento de DDL bajo el modelo categorial de bases de datos: tablas como objetos, claves foraneas totales como generadores y ciertas constraints como ecuaciones de caminos. `NULL`, multiplicidades, constraints no ecuacionales y semantica SQL completa requieren tratamiento adicional.

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

En el modelo de instancias como funtores, dos foreign keys totales se componen como funciones. Un JOIN puede **realizar o consultar** ese camino, pero el operador SQL no es por ello la composicion categorial; `NULL`, bags y variantes de JOIN importan. La identidad es el camino vacio sobre la tabla.

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

La composicion de las funciones de claves es asociativa. La equivalencia de planes JOIN concretos exige ademas las hipotesis de la semantica relacional elegida; no se deduce solo de la ley categorial.

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

**Docker Compose.** `depends_on` genera un digrafo de dependencias. Su categoria libre contiene caminos y su relacion de alcanzabilidad es transitiva. Un fallo de startup puede deberse a readiness, timing o configuracion; no demuestra que haya fallado una ley categorial.

**git merge.** Un merge sugiere una intuicion composicional: combina dos historias de desarrollo en una historia nueva. Pero no conviene presentarlo como una operacion asociativa en sentido categorial estricto; depende del estado del repositorio, de la base comun y de la estrategia de merge. Lo util de la analogia es otra cosa: cuando aparece un conflicto severo, suele haber dos cambios que dejaron de encajar composicionalmente.

**Pipelines de CI/CD.** Si cada stage se modela como funcion total entre estados de artefacto, la composicion es asociativa y el passthrough es identidad. Efectos, fallos, caches y entorno deben entrar al tipo o modelarse, por ejemplo, en una categoria de Kleisli; de otro modo reagrupar puede cambiar el comportamiento.

**Composicion de funciones en APIs.** Un middleware chain puede modelarse composicionalmente, pero callbacks, respuestas tempranas y efectos impiden llamarlo composicion pura sin una semantica explicita.

**Dependencias de componentes de software.** Un grafo de dependencias puede generar una categoria de caminos o un orden de alcanzabilidad si es aciclico. Los conflictos de version son incompatibilidades de constraints; solo son fallas de conmutatividad si se ha construido un diagrama semantico que deba conmutar.

## Dualidad: cada concepto tiene un gemelo

Hay un principio generativo que descubri tarde pero que ahora uso todo el tiempo. Dada cualquier categoria C, puedo construir su **categoria opuesta** C^op invirtiendo todas las flechas. Si f: A -> B en C, entonces f^op: B -> A en C^op. La composicion se invierte: (g . f)^op = f^op . g^op.

Esto no es un truco formal. Es un principio de generacion de conceptos. Cada estructura en una categoria tiene un **dual** en la categoria opuesta, y ese dual es automaticamente coherente. Si tengo un concepto (por ejemplo, un "producto" que combina dos objetos), al invertir todas las flechas obtengo el concepto dual (un "coproducto" que elige entre dos objetos). Gratis.

En la categoria opuesta se invierte formalmente la direccion de las claves. Esto puede sugerir lecturas descendentes, pero `SELECT` e `INSERT` no forman automaticamente un par dual: hay que definir las categorias y demostrar la correspondencia.

En preorders, el dual invierte el orden: si en P tenemos a <= b, en P^op tenemos b <= a. Joins se convierten en meets. El supremo se convierte en infimo. Fong y Spivak en *Seven Sketches* construyen todo el Capitulo 1 sobre esta dualidad: las conexiones de Galois son pares de mapas monotonos entre un preorder y su dual.

## El dolor de la no-composicion

Vuelvo al principio. Lo que me trajo aca no fue la elegancia de la matematica sino el dolor de las cosas que no componen. Milewski lo articula asi: la composicion es la esencia de la programacion. Descomponemos problemas grandes en problemas pequenos, y luego componemos las soluciones. La descomposicion no tendria sentido si no pudieramos reconstruir.

La superficie de un componente debe crecer mas lento que su volumen. La superficie es la informacion que necesito para componer; el volumen es la informacion que necesito para implementar. Cuando la superficie crece tan rapido como el volumen, la composicion se vuelve imposible --- necesito conocer la implementacion para componer, y eso destruye la abstraccion.

Los efectos no destruyen necesariamente la composicion: pueden hacerse explicitos como transformaciones de estado, flechas de Kleisli u otra semantica. El problema aparece cuando el modelo omite el estado/efecto relevante y pretende razonar como si las funciones fueran puras.

*Relational Thinking* marca una transicion fundamental: del pensamiento de causa-y-efecto al pensamiento de equilibrio-y-constraint. Los sistemas dinamicos del Capitulo 2 --- Kiki y Bouba, los semaforos, las luces intermitentes --- se modelan como grafos dirigidos con estados y reglas de actualizacion, un mundo causal donde las flechas transmiten estado de un vertice a otro en cada paso temporal. Pero a partir del Capitulo 3, el libro gira hacia una vision relacional donde las flechas codifican constraints simultaneas, no secuencias temporales. Esa transicion --- de imperativo a relacional, de procedimental a declarativo --- es la misma que yo hago cada vez que paso de pensar en "que hace este microservicio" a pensar en "que invariantes mantiene este schema."

La composicion es el primer peldano. Todo lo demas --- la preservacion de estructura cuando paso entre mundos, la construccion de cosas nuevas a partir de piezas universales, la equivalencia entre perspectivas distintas --- se apoya en este fundamento. Si la composicion falla, nada de lo que viene despues tiene sentido.

## Estatuto epistemico

- **Formal:** definicion de categoria, categoria opuesta, categoria libre y
  cociente por ecuaciones.
- **Modelo:** schemas, pipelines y dependencias solo despues de tipar sus
  objetos, flechas y leyes.
- **Heuristica:** llamar "falla de composicion" a un sintoma operacional antes
  de construir ese modelo.
