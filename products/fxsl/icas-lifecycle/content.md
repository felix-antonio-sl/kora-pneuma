---
urn: urn:fxsl:kb:icas-lifecycle
nombre: icas-lifecycle
version: 1.1.0
estado: publicado
descripcion: "Pieza 16 del ICAS-BoK: lifecycle — V-model, DevOps, drift, versionado y deuda técnica con vocabulario categorial; gobierno del ciclo de vida del software."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/16-lifecycle.md (sha256:4e57fe42a3e7c81a27a1853abcdd1b1e6fe0668714e7d746356f211069d42555) el 2026-06-12. Corrección epistémica 1.1.0 (2026-07-18): Git merge no se identifica con pushout y las lecturas adjunta/fibrada/trazada se declaran modelos condicionales."
autor: FS
creado: 2026-04-14
lang: es
tags: [recursion-composicional, v-model, devops, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Lifecycle

## Estatus de la lectura

Este documento propone modelos categoriales para procesos de lifecycle. Los
términos «adjunción», «fibración», «trace» y «transformación natural» son
formales solo cuando se construyen las categorías, funtores y leyes
correspondientes. Un diagrama con forma de V, loop o jerarquía no basta.

## La V no es un diagrama bonito

Un V-model organiza refinamiento y verificación correlativa; su forma no es una
cadena de adjunciones. Cada transición es candidata a funtor solo si las fases
se construyen como categorías y se define su acción sobre morfismos. Una
adjunción adicionalmente exige una biyección natural de hom-sets.

Lo que descubri al leer la tesis de Vidalie es que esta correspondencia izquierda-derecha puede leerse provechosamente con el lenguaje de las adjunciones. El funtor de descomposicion D_k : Phase_k -> Phase_{k+1} que refina el nivel k al nivel k+1 sugiere un companero de verificacion V_k : Phase_{k+1} -> Phase_k que comprueba si la descomposicion preservo los invariantes del nivel superior. Presentarlo como una cadena formal de adjunciones exige hipotesis adicionales; aqui lo uso como lectura estructural de la V, no como teorema ya cerrado.

Vidalie lo formula en terminos de modelos. Un modelo MBSE (la arquitectura del sistema) y un modelo MBSA (el analisis de seguridad) son dos categorias que describen el mismo sistema desde perspectivas distintas. La consistencia entre ambos se expresa mediante morfismos de correspondencia entre submodelos; si esa correspondencia asciende hasta equivalencia o isomorfismo en el nivel adecuado, la coincidencia estructural es especialmente fuerte. Lo importante aqui no es colapsar todas esas nociones en una sola, sino distinguir si hablamos de inclusion, de traduccion fiel o de equivalencia. Los elementos del modelo --- bloques, puertos, conexiones --- se representan como objetos y morfismos en categorias, y los catports y catblocks de S2ML+Cat capturan la estructura jerarquica con precision matematica.

El zigzag entre estructura funcional y física sugiere traducciones en ambos
sentidos. Puede investigarse una adjunción, pero «descomponer y verificar
recupera la función» es aquí un requisito de round-trip, no una unit/counit
demostrada.

## Las fases como categorias

El macro lifecycle de un sistema puede presentarse categorialmente si se
definen composición e identidades para sus trazas. IEEE 15288 organiza los
procesos del ciclo de vida; esa organización aporta datos de dominio, no por sí
sola una categoría.

Una fase puede modelarse como categoría de artefactos y transformaciones. Si
las dependencias son solo aristas de un grafo, primero se toma su categoría
libre de caminos o se especifican ecuaciones entre caminos.

Una transición entre fases puede ser un funtor. Una traceability matrix suele
registrar solo el mapa de objetos; para que `P : Requirements -> Architecture`
sea genuinamente functorial hay que definir y verificar también su acción
sobre morfismos, identidades y composición.

Los phase gates pueden leerse como transformaciones naturales cuando comparan
dos funtores entre las mismas categorías mediante componentes coherentes. Un
review ordinario puede detectar inconsistencias sin realizar esa construcción.

## El micro lifecycle embebido

Dentro de la fase de construcción puede anidarse un lifecycle de software. La
semejanza de fases no prueba que micro y macro compartan exactamente una
estructura categorial; esa relación se modela y verifica caso a caso.

La relación micro/macro **puede aspirar** a una fibración de Grothendieck. Una
mera proyección `pi : MicroLifecycle -> MacroLifecycle` y sus preimágenes no
bastan: una fibración exige lifts cartesianos para las flechas de la base y su
propiedad universal.

Los niveles anidados de un Gantt ilustran preimágenes sobre fases. Llamarlos
fibración es una hipótesis de modelado hasta construir los lifts; la jerarquía
visual por sí sola sigue siendo analogía.

La composición vertical de modelos de requirements, comportamiento y
arquitectura puede motivar una fibración. Para afirmarla hacen falta
proyecciones y lifts cartesianos; «capa sobre capa» no los proporciona.

## DevOps como categoria monoidal trazada

DevOps introduce feedback explícito. Puede modelarse por un trace en una
categoría monoidal trazada solo después de definir el tensor, el morfismo con
feedback y verificar los axiomas de trace; un loop dibujado no es suficiente.

En una categoría monoidal trazada, el operador
`Tr^U_{A,B} : Hom(A tensor U, B tensor U) -> Hom(A,B)` cierra una interfaz de
feedback y satisface axiomas compatibles con composición y tensor. Un loop de
DevOps puede representarse así solo después de codificar development,
operation y su estado como ese morfismo; el dibujo circular no aporta la
traza.

Un sprint ilustra un loop de feedback. Solo es un trace categorial dentro de un
modelo monoidal trazado que satisfaga sus axiomas; backlog, review y
retrospectiva no suministran ese modelo automáticamente.

Un pipeline secuencial genera caminos componibles si cada stage tiene
dominio/codominio. La asociatividad solo dice que reagrupar la **misma**
composición no cambia su valor; no garantiza reproducibilidad de stages con
estado o efectos. Continuous delivery puede modelarse mediante una dinámica
entre versiones. Un estado estable de esa dinámica puede ser un punto fijo,
pero no todo pipeline define un endofuntor ni converge.

Un pipeline de Terraform puede leerse por analogia con una adjuncion, pero no conviene fijarlo como tal sin una categorizacion mucho mas precisa. `terraform plan` expone una diferencia entre estado actual y estado deseado; `terraform apply` intenta realizar esa diferencia en el mundo. La intuicion de ida y vuelta es util, aunque aqui sigue siendo analogica. Los rolling updates de Kubernetes admiten una lectura similar: la actualizacion de un Deployment puede modelarse como una familia coherente de cambios entre versiones, y la naturalidad funciona mejor como criterio deseable de compatibilidad que como propiedad ya demostrada por defecto.

## Evolucion y drift

Un sistema en producción evoluciona. Esa evolución **puede modelarse** mediante
un endofuntor `E : Sys -> Sys` si una misma categoría contiene las versiones y
`E` actúa coherentemente sobre objetos y morfismos.

No existe una transformación natural canónica `eta : Id => E` para todo
endofuntor. Si el proceso proporciona componentes `eta_A : A -> E(A)` y estos
satisfacen naturalidad, entonces sí se obtiene ese test de coherencia.

Dentro de este modelo, una forma específica de incompatibilidad puede
expresarse cuando `eta` deja de ser natural. La definición de naturalidad exige
que para todo morfismo `f : A -> B` en `Sys`, el diagrama

```
 eta_A
 A ---------> E(A)
 | |
 f E(f)
 | |
 v v
 B ---------> E(B)
 eta_B
```

conmute: eta_B . f = E(f) . eta_A. El drift ocurre cuando este diagrama no conmuta para algun morfismo f. En la practica: el componente A evoluciono a E(A), el componente B evoluciono a E(B), pero la dependencia f entre ellos no evoluciono de forma compatible. El sistema "en papel" dice que A y B se conectan de una manera; el sistema real se conecto de otra. La brecha entre el diagrama y la realidad es el drift.

Verificar esos cuadrados detecta drift **representado por el modelo**, no todo
drift operativo. Un rolling update puede idealizarse como transformación
natural si sus componentes tienen el tipo requerido. Un rollback es otra
transición; solo sería `eta^{-1}` si cada componente fuese invertible y se
probara naturalidad del inverso, algo que las actualizaciones ordinarias no
garantizan.

## Versionado como transformacion natural

Vidalie dedica la sección 4.5 de su tesis a simplificar la comparación de
modelos mediante versionado. Una correspondencia entre versiones puede
representarse por un funtor si ambas versiones son categorías y el mapping
preserva identidades y composición. Mapear eliminados a un objeto especial
`{vacio}` no garantiza esas leyes ni captura por sí solo qué permaneció igual;
los elementos nuevos simplemente pueden quedar fuera de la imagen.

Puede construirse una 2-categoría de versiones, funtores de transición y
transformaciones naturales. Su existencia no se desprende del versionado
ordinario. Cantor-Bernstein es un teorema sobre conjuntos (y sobre contextos
adicionales específicos); monomorfismos en ambos sentidos no implican en una
categoría arbitraria que dos objetos sean isomorfos o equivalentes.

Git almacena un DAG de commits y las branches son referencias móviles a
commits. Un merge de tres vías produce contenido y, normalmente, un commit con
dos padres; no es por defecto el pushout de las branches ni un «commit mínimo»
universal. Un conflicto indica que el algoritmo no puede escoger una
reconciliación automática, no que un colímite matemático no exista.

Puede construirse una categoría de snapshots/parches donde cierta operación de
merge satisfaga un pushout, pero hay que definirla y demostrar la propiedad
universal. La resolución manual elige contenido; no la convierte
automáticamente en construcción universal.

Las database migrations forman una secuencia de transformaciones. Pueden ser
morfismos de una categoría de versiones o funtores entre categorías de schema,
según el modelo; esas dos capas no deben confundirse. Reagrupar transformaciones
puras usa asociatividad, mientras que scripts con efectos requieren además una
semántica operacional. Un rollback es inverso solo cuando recupera estructura
y datos en ambos sentidos; `DROP COLUMN` normalmente no lo permite.

## La categoría de versiones

Las database migrations pueden organizarse en una categoría **Ver** de
versiones si se eligen como morfismos las migraciones componibles y se
identifican explícitamente los caminos que deben ser iguales.

Los objetos de `Ver` son versiones del esquema y los morfismos, migraciones.
La identidad es la migración nula y la composición es la aplicación
secuencial. `Ver` solo es un preorden si entre dos versiones hay a lo sumo un
morfismo después de imponer ecuaciones; un DAG de migraciones con caminos
alternativos genera en cambio una categoría libre con morfismos distintos.

Un modelo más rico busca un funtor de esquemas `F : Ver -> Cat` que asigne a
cada versión una categoría y a cada migración un funtor compatible. Cada
versión tiene entonces una categoría de instancias. La precomposición `Delta`
siempre está disponible; sus adjuntos `Sigma` y `Pi` son extensiones de Kan y
existen bajo las hipótesis correspondientes.

```
Inst(S₁) --Σ_F--> Inst(S₂)
 | |
 v v
 v1.0.0 --upgrade--> v1.1.0
```

La composición de migraciones a lo largo de la cadena v₁ → v₂ → ... → vₙ tiene una propiedad que la ingeniería de datos raramente hace explícita: la pérdida de constraints es acumulativa. Si la migración m₁ pierde la constraint de UNIQUE en el campo email (porque usa Σ), y la migración m₃ pierde la constraint de NOT NULL en department_id (porque otra Σ colapsa departamentos), la composición m₅ . ... . m₁ ha perdido ambas constraints. Pero nadie lo sabe, porque cada migración individual fue "correcta" en su contexto.

Esto es **deuda técnica categórica**: la diferencia entre las constraints de la teoría T₁ del esquema original y las constraints de la teoría Tₙ del esquema actual que son todavía satisfechas después de la cadena de migraciones. La deuda se acumula silenciosamente con cada Σ que colapsa distinciones y cada migración ad hoc que no es genuinamente un funtor (no preserva composición o identidad). La detección requiere cargar las constraints de v₁, aplicar la cadena completa m_n . ... . m_1, y verificar cuáles sobreviven en vₙ. La diferencia es la deuda. Cada constraint perdida es una invariante que el código asume pero el esquema ya no garantiza -- y el punto de falla será donde esa asunción invisible choque con la realidad.

## Cambio de doctrina

Myers formaliza algo que va mas alla de la evolucion dentro de un lifecycle: el cambio de doctrina. Una doctrine of dynamical systems, en su terminologia, es una forma particular de responder las preguntas fundamentales sobre que significa ser un sistema: que son los estados, como cambian, que significa componer sistemas, como se comportan los compuestos. Cambiar de una doctrina a otra --- por ejemplo, pasar de sistemas deterministas a sistemas probabilisticos, o de ecuaciones diferenciales a automatas discretos --- es un 2-funtor entre doubly indexed categories de teorias.

El ejemplo que me resulta mas iluminador es la aproximacion de Euler. Un sistema diferencial continuo vive en la doctrina de differential systems theory. Un sistema discreto vive en la doctrina de deterministic systems theory. El metodo de Euler es un cambio de doctrina que aproxima la dinamica continua con pasos discretos de tamano epsilon. Myers demuestra que este cambio de doctrina preserva los steady states --- los puntos fijos del sistema --- pero no preserva las trayectorias generales. Las trayectorias afines se preservan exactamente; las no-afines se aproximan con error del orden de epsilon. La functorialidad del cambio de doctrina es lo que garantiza que la composicion se preserva: si cambio la doctrina de cada subsistema individualmente y luego compongo, obtengo lo mismo que si compongo primero y luego cambio la doctrina del compuesto.

En la práctica, migrar de monolito a microservicios **puede motivar** un cambio
de doctrina. Para llamarlo 2-funtor hay que construir las doctrinas, mapear
componentes, dependencias e invariantes y verificar las coherencias. Preservar
la composición prueba corrección relativa a esa semántica; no prueba por sí
solo entrega, latencia, fallos distribuidos ni que tests de integración no
puedan detectar la divergencia.

## Todo tiene un ciclo de vida

La perspectiva categorial ofrece **modelos candidatos**: fases como
categorías, transiciones como funtores, gates como transformaciones y drift
como fallo de coherencia. Cada uno debe construirse; ninguno se deduce del
nombre del proceso.

Cuando esas estructuras se construyen, permiten formular qué coherencia debe
preservarse entre niveles. Cuando no, el valor del vocabulario es heurístico:
señala interfaces y obligaciones, pero no certifica su propagación.

## Corrección 1.1.0

Se corrigen las identificaciones jerarquía=fibración, loop=trace,
evolución=endofuntor con transformación canónica y Git merge=pushout. Quedan
como modelos válidos únicamente cuando se exhiben las estructuras y leyes
correspondientes.
