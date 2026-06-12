---
urn: urn:fxsl:kb:icas-lifecycle
nombre: icas-lifecycle
version: 1.0.0
estado: publicado
descripcion: "Pieza 16 del ICAS-BoK: lifecycle — V-model, DevOps, drift, versionado y deuda técnica con vocabulario categorial; gobierno del ciclo de vida del software."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/16-lifecycle.md (sha256:4e57fe42a3e7c81a27a1853abcdd1b1e6fe0668714e7d746356f211069d42555) el 2026-06-12; cuerpo byte-fiel. Fuente original: ICAS-BoK corpus — Fong/Spivak, Mac Lane, Barbosa, Awodey, Riehl"
autor: FS
creado: 2026-04-14
lang: es
tags: [recursion-composicional, v-model, devops, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Lifecycle

## La V no es un diagrama bonito

Cada vez que un project manager dibuja un V-model en una pizarra, lo que dibuja --- sin saberlo --- es una cadena de adjunciones. La rama izquierda de la V desciende de los stakeholder requirements a la system specification, de ahi al preliminary design, del preliminary design al detailed design, y del detailed design a la construccion de componentes. Cada paso es un funtor que refina: agrega detalle, descompone subsistemas, concretiza interfaces. La rama derecha asciende: integracion de componentes, verificacion de subsistemas, validacion del sistema, y finalmente aceptacion del producto integrado. Cada paso de la derecha verifica que el paso correspondiente de la izquierda fue correcto.

Lo que descubri al leer la tesis de Vidalie es que esta correspondencia izquierda-derecha puede leerse provechosamente con el lenguaje de las adjunciones. El funtor de descomposicion D_k : Phase_k -> Phase_{k+1} que refina el nivel k al nivel k+1 sugiere un companero de verificacion V_k : Phase_{k+1} -> Phase_k que comprueba si la descomposicion preservo los invariantes del nivel superior. Presentarlo como una cadena formal de adjunciones exige hipotesis adicionales; aqui lo uso como lectura estructural de la V, no como teorema ya cerrado.

Vidalie lo formula en terminos de modelos. Un modelo MBSE (la arquitectura del sistema) y un modelo MBSA (el analisis de seguridad) son dos categorias que describen el mismo sistema desde perspectivas distintas. La consistencia entre ambos se expresa mediante morfismos de correspondencia entre submodelos; si esa correspondencia asciende hasta equivalencia o isomorfismo en el nivel adecuado, la coincidencia estructural es especialmente fuerte. Lo importante aqui no es colapsar todas esas nociones en una sola, sino distinguir si hablamos de inclusion, de traduccion fiel o de equivalencia. Los elementos del modelo --- bloques, puertos, conexiones --- se representan como objetos y morfismos en categorias, y los catports y catblocks de S2ML+Cat capturan la estructura jerarquica con precision matematica.

Subrahmanian y Keraron lo ven desde la practica industrial. El V-model no es un flujo lineal sino un proceso recursivo: en cada nivel del system breakdown, se repite el ciclo Requirements -> Architecture -> Design -> Implementation con su correspondiente Integration -> Verification -> Validation. El zigzagging entre la estructura funcional y la estructura de producto --- entre lo que el sistema hace y de que esta hecho --- es un par de funtores que van y vienen entre dos categorias: la categoria funcional y la categoria fisica. Suh lo teorizo como Axiomatic Design; yo lo veo como una adjuncion entre el dominio funcional y el dominio fisico. La unit de esta adjuncion dice: si descompongo una funcion en componentes fisicos y luego verifico que los componentes cumplen la funcion, recupero la funcion original. La counit dice: si un componente fisico ya realiza exactamente la funcion especificada, la descomposicion no lo altera.

## Las fases como categorias

El macro lifecycle de un sistema --- del concepto a la disposicion --- tiene una estructura categorial precisa. IEEE 15288 define los procesos del ciclo de vida en cuatro secciones: Agreement, Organizational Project-Enabling, Technical Management, y Technical Processes. Los Technical Processes incluyen catorce actividades desde Business/Mission Analysis hasta Disposal. Vidalie detalla esta estructura en su capitulo sobre el estado del arte, mostrando como los ocho subprocesos del Systems Engineering Process (SEP) se descomponen en tareas, flujos de proceso generales, y actividades asociadas.

Cada fase del lifecycle es una categoria. Los objetos son los artefactos de esa fase --- documentos de requirements, diagramas de arquitectura, modelos de simulacion, codigo fuente, resultados de test. Los morfismos son las transformaciones y dependencias entre artefactos: un requirement traza a una funcion, una funcion traza a un componente, un componente traza a un test case. La composicion de trazas es transitiva: si el requirement R traza a la funcion F y F traza al componente C, entonces R tiene trazabilidad transitiva a C.

La transicion entre fases es un funtor. El funtor de "preliminary design" P : Requirements -> Architecture toma cada requirement y lo mapea a un elemento arquitectonico que lo satisface. Este funtor no es arbitrario --- debe preservar la estructura de composicion: si dos requirements se componen (uno depende del otro), sus realizaciones arquitectonicas deben componerse de forma compatible. Lo que los systems engineers llaman "traceability matrix" es la tabla de la funcion sobre objetos del funtor P. Lo que llaman "consistency check" es la verificacion de que P preserva composicion --- de que es genuinamente un funtor y no solo un mapeo ad hoc.

Los phase gates --- esos reviews formales donde un panel decide si el proyecto puede avanzar a la siguiente fase --- pueden leerse como transformaciones naturales. Un phase gate verifica que el funtor de transicion entre fases es consistente: que cada componente del mapeo respeta la estructura. La naturalidad dice que no importa por que camino llegue al artefacto verificado --- via descomposicion funcional o via descomposicion fisica --- el resultado de la verificacion es el mismo. Si el gate falla, lo que se detecto es una violacion de la naturalidad: un camino por la izquierda da un resultado distinto que un camino por la derecha.

## El micro lifecycle embebido

Dentro de la fase de "construction" del macro lifecycle vive un lifecycle completo de software: requirements -> design -> implementation -> testing -> deployment -> maintenance. Este micro lifecycle tiene exactamente la misma estructura categorial que el macro --- fases como categorias, transiciones como funtores, gates como transformaciones naturales --- pero a menor escala y mayor velocidad.

La relacion entre el micro y el macro lifecycle es una Grothendieck fibration. Formalmente, hay un funtor de proyeccion pi : MicroLifecycle -> MacroLifecycle que mapea cada fase del ciclo de software a la fase "construction" del ciclo de sistema. La fibra sobre "construction" --- la pre-imagen de esa fase via pi --- es todo el micro lifecycle de software. Pero hay fibras sobre otras fases tambien: la fase de "system requirements" tiene su propia fibra de analisis de requirements de software; la fase de "integration" tiene su propia fibra de integracion de software con hardware.

Esto es lo que veo cuando miro un proyecto real. El Gantt chart del proyecto de sistema tiene barras gruesas: Concept, Development, Production, Utilization, Support, Retirement. Dentro de la barra de Development hay un Gantt mas fino con sprints de software. Dentro de cada sprint hay un Gantt aun mas fino con tareas individuales. Cada nivel de zoom es una fibra sobre el nivel superior. La fibracion captura esta estructura recursiva de forma precisa: para cada punto del macro lifecycle, hay un micro lifecycle completo funcionando. El software lifecycle IS la fibra sobre la fase "construction" --- no es una analogia, es la definicion misma de fibra en el sentido de Grothendieck.

Bakirtzis articula esta idea desde la seguridad: los modelos de safety del sistema (MBSA) y los modelos de comportamiento del software (behavioral specifications) viven en categorias distintas pero deben ser consistentes. La composicion vertical --- entre las algebras de requirements, comportamiento y arquitectura --- es el aporte central de su teoria composicional de sistemas cyber-fisicos. Lo que yo reconozco en esta composicion vertical es exactamente la fibracion: la capa de seguridad es una fibra sobre la capa de arquitectura, que es una fibra sobre la capa de requirements. Las tres capas se proyectan unas sobre otras a traves de funtores que preservan la estructura composicional de los wiring diagrams.

## DevOps como categoria monoidal trazada

El lifecycle clasico --- waterfall o V-model --- tiene una topologia lineal: va del concepto a la disposicion sin volver atras. DevOps rompe esa linealidad con un feedback loop explicito: la operacion del sistema alimenta al desarrollo con datos sobre comportamiento real, y el desarrollo produce nuevas versiones que se despliegan en operacion. Este loop es un trace en una traced monoidal category.

En una categoria monoidal con trace, puedo "doblar" un cable de salida y reconectarlo a una entrada, creando un feedback loop que sigue siendo composicional. El loop de DevOps dobla la salida de "operation" y la reconecta a la entrada de "development". El trace garantiza que esta reconexion preserva la estructura composicional --- que puedo seguir componiendo stages dentro del loop sin romper las leyes de la categoria. Formalmente, el trace Tr^U_{A,B} : Hom(A x U, B x U) -> Hom(A, B) toma un morfismo con feedback (el loop) y produce un morfismo sin feedback (el comportamiento observable del loop), y esta operacion es compatible con la composicion.

Un sprint de Agile es un traced loop. El sprint toma el product backlog como input, produce un incremento como output, y el feedback del sprint review se reconecta al backlog para el proximo sprint. La composicion de sprints es asociativa: sprint_3 . sprint_2 . sprint_1 produce el mismo resultado independientemente de como agrupe los sprints. La identidad es el sprint nulo --- un sprint donde no se cambia nada, que deja el sistema intacto. La retrospectiva es la meta-observacion del trace: no modifica el sistema, modifica el proceso --- cambia el funtor, no los objetos.

CI/CD es la composicion de deployment morphisms. El pipeline --- build, test, package, deploy --- es una cadena de morfismos en la categoria de artefactos: source -> binary -> tested_binary -> packaged_artifact -> deployed_service. La composicion es estricta: el artefacto producido por build -> test -> deploy es el mismo independientemente de como agrupe los stages, porque cada stage tiene precondiciones y postcondiciones explicitas que encajan como la fuente y el target de un morfismo. Continuous delivery es un endofuntor CD : SystemCat -> SystemCat que mapea cada version del sistema a la siguiente. La iteracion CD^n produce la n-esima version. La convergencia de CD --- si las versiones se estabilizan --- es la existencia de un fixed point del endofuntor.

Un pipeline de Terraform puede leerse por analogia con una adjuncion, pero no conviene fijarlo como tal sin una categorizacion mucho mas precisa. `terraform plan` expone una diferencia entre estado actual y estado deseado; `terraform apply` intenta realizar esa diferencia en el mundo. La intuicion de ida y vuelta es util, aunque aqui sigue siendo analogica. Los rolling updates de Kubernetes admiten una lectura similar: la actualizacion de un Deployment puede modelarse como una familia coherente de cambios entre versiones, y la naturalidad funciona mejor como criterio deseable de compatibilidad que como propiedad ya demostrada por defecto.

## Evolucion y drift

Un sistema en produccion evoluciona. Cada release, cada hotfix, cada cambio de configuracion transforma el sistema de una version a la siguiente. Esta evolucion es un endofuntor E : Sys -> Sys donde Sys es la categoria del sistema (objetos = componentes, morfismos = dependencias). Cada aplicacion de E produce una nueva version del sistema: E^n(Sys_0) = Sys_n.

La pregunta critica es: la evolucion preserva los invariantes. Formalmente, hay una transformacion natural canonica eta : Id -> E que dice como cada componente de la version actual se mapea a su version evolucionada. Si eta es un isomorfismo natural, la evolucion es reversible y preserva toda la estructura. Si eta es simplemente natural (pero no iso), la evolucion preserva las relaciones pero puede perder informacion --- componentes que se fusionan, interfaces que se simplifican, funcionalidad que se depreca.

El drift es lo que ocurre cuando eta deja de ser natural. La definicion de naturalidad requiere que para todo morfismo f : A -> B en Sys, el diagrama

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

Detectar drift es verificar naturalidad. Para cada dependencia f del sistema, verifico que eta_B . f = E(f) . eta_A. Si falla para alguna f, encontre drift. Un Kubernetes rolling update exitoso puede idealizarse como una transformacion natural eta : v_old -> v_new donde cada componente transiciona de forma compatible con sus dependencias. Un rolling update fallido --- donde algunos pods estan en v_old y otros en v_new con dependencias incompatibles --- es un eta que fallo la naturalidad. La solucion es un rollback: aplicar eta^{-1} para restaurar la naturalidad, o reparar los morfismos rotos para que el diagrama vuelva a conmutar.

## Versionado como transformacion natural

Vidalie dedica la seccion 4.5 de su tesis a simplificar la comparacion de modelos mediante versionado. Su idea central es que cuando los modelos evolucionan de la version n a la version n+1, la mayor parte de la estructura permanece intacta. El funtor F_n : V_n -> V_{n+1} que mapea cada elemento del modelo en su version n a su correspondiente en la version n+1 captura exactamente que cambio y que permanecio igual. Los elementos eliminados se mapean a un objeto especial {vacio}; los elementos nuevos no tienen pre-imagen. La estructura de consistency relations entre versiones se simplifica dramaticamente: en vez de comparar modelos completos, solo comparo los deltas.

Lo que Vidalie construye se deja describir muy bien como una 2-categoria. Los objetos son las versiones del modelo. Los 1-morfismos son los funtores de transicion F_n entre versiones. Los 2-morfismos son las transformaciones naturales que comparan dos formas de transicionar. Si tengo dos caminos de V_1 a V_3 --- uno directo F_{1,3} y otro compuesto F_{2,3} . F_{1,2} --- la transformacion natural entre ambos dice si los dos caminos producen el mismo resultado. La consistencia entre versiones puede medirse justamente por la naturalidad de estos 2-morfismos. Vidalie demuestra que esta simplificacion funciona gracias a la propiedad de Cantor-Bernstein para modelos categoricos: si A se inyecta en B y B se inyecta en A, entonces A y B son equivalentes.

Git branching es una fibracion sobre este esquema. El repositorio es un funtor de la categoria de commits a la categoria de snapshots del codigo. Cada branch es una fibra --- una sub-categoria de commits que comparte un ancestor comun. Un merge es un colimite (un pushout) en la categoria de branches: dados dos branches que divergieron de un commit comun, el merge produce el commit minimo que integra ambos. Un merge conflict es la ausencia de ese colimite --- los dos branches modificaron la misma estructura de formas incompatibles, y el pushout no existe. La resolucion del conflicto es la construccion manual del pushout: el desarrollador decide como combinar los cambios para que el diagrama conmute.

Las database migrations forman una cadena functorial. Cada migracion M_k : Schema_k -> Schema_{k+1} es un funtor que transforma el schema. La composicion M_n . ... . M_2 . M_1 produce la migracion total de Schema_1 a Schema_{n+1}. La asociatividad de la composicion garantiza que puedo aplicar las migraciones en bloques sin alterar el resultado. Un rollback es un intento de inverso: M_k^{-1} que deshace la migracion k. Si el inverso existe, la migracion es reversible; si no, el cambio es irreversible --- un DROP COLUMN no se puede deshacer. La secuencia de migraciones forma un path en la categoria finitamente presentada del schema, exactamente cada migracion es un morfismo, y la composicion de migraciones debe satisfacer las path equivalences del dominio. Bakirtzis formaliza esta estructura de composicion vertical -- la integracion de artefactos de distintas fases -- y composicion horizontal -- la coordinacion de disciplinas dentro de una fase -- como un algebra de wiring diagrams que el documento 17 desarrolla en detalle.

## La categoría de versiones

Las database migrations que acabo de describir no son morfismos aislados. Forman una categoría propia: **Ver**, la categoría de versiones.

Los objetos de Ver son las versiones del esquema: v1.0.0, v1.1.0, v2.0.0. Los morfismos son las migraciones: upgrade_{n,n+1} : v_n → v_{n+1}. La identidad es la migración nula (no-op). La composición es la aplicación secuencial de migraciones: upgrade_{n,n+2} = upgrade_{n+1,n+2} . upgrade_{n,n+1}. Ver es típicamente un preorder -- hay a lo sumo un camino canónico entre dos versiones.

Lo que convierte esto en una estructura rica es el funtor de esquema **F : Ver → Cat** que asigna a cada versión su esquema como categoría. F(v1.0.0) = S₁ con {Employee, Department}; F(v1.1.0) = S₂ con {Employee, Department, Project}; F(upgrade) = un funtor de migración F_{1,2} : S₁ → S₂. Cada versión tiene su propia categoría de instancias Inst(F(v)), y cada migración induce los tres funtores adjuntos Δ/Σ/Π entre categorías de instancias.

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

En la practica, cambio de doctrina ocurre cada vez que cambio el paradigma de desarrollo. Migrar de un monolito a microservicios es cambiar la doctrina: los objetos pasan de ser modulos a ser servicios, los morfismos de ser llamadas a funciones a ser llamadas HTTP, la composicion de ser secuencial y sincrona a ser asincrona y eventualmente consistente. El 2-funtor de migracion debe mapear componentes a servicios, dependencias a endpoints, invariantes a contratos. Si preserva la estructura composicional --- si el comportamiento del compuesto se puede calcular a partir del comportamiento de las partes y el patron de composicion, como dice el big theorem de Myers en el capitulo 5 --- la migracion es correcta. Si no, introduje bugs estructurales que ningun test unitario va a encontrar, porque el error no esta en un componente sino en la composicion misma.

## Todo tiene un ciclo de vida

Lo que emerge de esta perspectiva es que el lifecycle no es una fase del proyecto --- es la estructura recursiva del proyecto mismo. Cada componente, cada servicio, cada modelo tiene su propio lifecycle embebido en el lifecycle del sistema mayor. Las fases son categorias. Las transiciones son funtores. Los gates son transformaciones naturales. La evolucion es un endofuntor. El drift es la perdida de naturalidad. El versionado es la 2-categoria de historias de cambio. Y el cambio de doctrina es el nivel superior: cuando no solo cambia el sistema sino las reglas mismas bajo las cuales el sistema se construye.

Esta estructura fractal --- lifecycles dentro de lifecycles, funtores entre funtores, naturalidad que debe preservarse en cada nivel --- es lo que hace posible gobernar la complejidad de un sistema real. Sin ella, cada nivel de abstraccion es un silo. Con ella, los silos se conectan composicionalmente: la consistencia del micro lifecycle se propaga al macro lifecycle a traves de la fibracion, y la consistencia del macro lifecycle se propaga a la evolucion a traves de la naturalidad del endofuntor de evolucion. La ingenieria de sistemas, vista desde aqui, no es una coleccion de procesos secuenciales. Es una recursion composicional --- un pattern que se aplica a si mismo en cada nivel de abstraccion, y cuya coherencia total depende de que cada nivel preserve la estructura del nivel que lo contiene.
