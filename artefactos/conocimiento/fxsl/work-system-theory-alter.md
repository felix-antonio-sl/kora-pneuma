---
urn: urn:fxsl:kb:work-system-theory-alter
nombre: work-system-theory-alter
version: 1.0.0
estado: publicado
descripcion: "Work System Theory (WST) de Steven Alter: el work system como unidad natural de análisis de los sistemas en organizaciones. Cubre la definición de work system, el information system como caso especial (IS↔WS), el work system framework (9 elementos), el work system life cycle (WSLC), el work system method (WSM), las 11 funciones que un IS presta a un work system, las formas de overlap IS↔WS, y las extensiones (principles, design spaces, metamodel, facets, axioms)."
fuente: "Koraficado (traducción es-CL declarada; términos canónicos en inglés) de tres fuentes documentales de Steven Alter, University of San Francisco: (1) 'Work System Theory: Overview of Core Concepts, Extensions, and Challenges for the Future', Journal of the Association for Information Systems (JAIS), vol. 14, iss. 2, art. 1, 2013; (2) 'Applying Socio-technical Thinking...', Complex Systems Informatics and Modeling Quarterly (CSIMQ), no. 18, pp. 1-22, 2019, DOI 10.7250/csimq.2019-18.01; (3) 'A Proposed Theoretical Foundation for the Information Systems Discipline (version 1.1)', 2021. Fuentes externas (PDF aportados por el operador), sin sha256. Recorte de alcance declarado (ley/4 §8.3): se korafica el MARCO (conceptos, frameworks, método, funciones, overlaps, extensiones); se descartan por estar fuera de alcance la comparación con otras siete teorías (GST, STS, ANT, organizational routines, SSM, activity theory, UML), la evaluación académica (relevancia/novedad/claridad/utilidad), los next-steps de investigación, el aparato de citas/referencias, los use cases aplicados del TFIS (IS user satisfaction, IS security, AI, enterprise systems, outsourcing) y los catálogos de atributos del TFIS (characteristics, performance variables, phenomena, forces, portrayals)."
autor: FS
creado: 2026-06-23
lang: es
tags: [work-system-theory, work-system-framework, work-system-method, information-system, sistemas-sociotecnicos, modelado-de-sistemas, steven-alter, is-discipline]
familia: bok
---

# Work System Theory (WST)

**Work System Theory** (Steven Alter, University of San Francisco) es un cuerpo
integrado de teoría para **describir los sistemas en organizaciones y su
evolución en el tiempo**. Su valor central es soportar el *work system thinking*:
una perspectiva que mira los sistemas distinto de la asunción tecno-céntrica
("el sistema es una configuración de hardware/software usada por usuarios")
común en la práctica y la investigación de IS.

WST cumple un rol **map-like** (Clarke & Primo, 2012): *"Theories are like maps:
the test of a map lies not in arbitrarily checking random points but in whether
people find it useful to get somewhere"*. No describe relaciones entre variables;
ofrece un mapa para llegar a algún lado.

En las categorías de teoría de Gregor (2006), WST es un cuerpo integrado que
combina una teoría analítica Tipo 1 (el **work system framework**) y una teoría
explicativa Tipo 2 (el **work system life cycle model**), que juntas dan base a
una teoría de diseño Tipo 5 (el **work system method, WSM**).

WST tiene **tres partes**: (1) la definición de work system, (2) el work system
framework, (3) el work system life cycle model.

## El concepto de work system

**Work** (en contextos organizacionales) — uso de recursos humanos,
informacionales, físicos y otros para producir productos/servicios.

**Work system** — definición canónica de Alter:

> *"A system in which human participants and/or machines perform work (processes
> and activities) using information, technology, and other resources to produce
> products/services for internal and/or external customers."*

Es la **unidad natural de análisis** para pensar los sistemas en organizaciones.
Implicaciones inmediatas:

- **Alineamiento** — por su naturaleza sistémica, componentes e interacciones
  deben alinearse con los objetivos del work system. Desalineamientos y brechas
  de desempeño son razones primarias para modificar un work system.
- **Doble evaluación** — el desempeño se evalúa en parte por la eficiencia y
  otros aspectos de los procesos internos, en parte por la evaluación que los
  clientes hacen de los productos/servicios.
- **Sociotécnico por defecto** — los work systems son sistemas sociotécnicos en
  que personas ejecutan procesos y actividades. Diverge de los textos de systems
  analysis & design donde "el sistema" es un artefacto computarizado usado por
  usuarios.
- **Cobertura de lo totalmente automatizado** — la definición también cubre
  sistemas totalmente automatizados (sin participantes humanos), incluidos los
  revelados por descomposición de work systems sociotécnicos. Aplicar WST
  simétricamente a ambos tiende un puente entre los científicos sociales del IS
  y los especialistas técnicos.
- **Evolución** — los work systems evolucionan por combinación de cambio
  planificado y cambio emergente (no planificado); cambian no solo hardware y
  software, sino todos los componentes.

**Dominio útil**: aunque una empresa entera puede verse como work system, el
dominio útil del análisis son **work systems específicos dentro de la
organización** (p. ej. renovar pólizas, aprobar préstamos hipotecarios, operar
un call center de ingeniería, agendar y seguir citas de salud). Regla práctica:
el work system del análisis es **el más pequeño que exhibe el problema u
oportunidad** que lo motivó.

## Information system como caso especial de work system

Definición canónica:

> *"An information system is a work system whose processes and activities are
> devoted to processing information."*

El procesamiento de información comprende estas **operaciones** (definen qué es
un IS): **capturar, almacenar, recuperar, eliminar, transmitir, manipular y
mostrar** información (*capturing, storing, retrieving, deleting, transmitting,
manipulating, displaying*).

Relación IS↔WS: muchos IS existen **para soportar otros work systems**. Un IS de
distribución soporta el work system de distribuir bienes; un IS de contabilidad
soporta work systems contables cuyos participantes son contadores (caso en que
el work system soportado es a su vez un IS).

Otros **casos especiales de work system** (heredan la mayoría de las propiedades
del caso general):

| Caso especial | Definición |
|---|---|
| Information system | Work system cuyas actividades se dedican a procesar información. |
| Supply chain | Work system inter-organizacional que provee insumos y recursos para la operación de organizaciones que usan lo que la cadena produce. |
| Project | Work system temporal diseñado para producir un conjunto de productos/servicios; al terminar, deja de existir. |
| Self-service work system | Work system cuyos participantes primarios son los clientes (p. ej. comprar en un sitio ecommerce usando recursos provistos para su uso). |
| Totally automated work system | Work system donde todos los procesos y actividades los ejecutan programas, máquinas y dispositivos; quienes los crean/mantienen no son participantes de él, sino de otros work systems. |

ERP y CRM: los paquetes de software comercial se ven mejor como **infraestructura
compartida por múltiples work systems**; los programas usados en un work system
específico son parte de la *technology* de ese work system.

## Work System Framework — vista estática (9 elementos)

El work system framework representa un work system en términos de **nueve
elementos** de su forma, función y entorno durante un período en que es
relativamente estable (aunque ocurran cambios incrementales). Enfatiza lo de
negocio sobre lo de IT; cubre situaciones con o sin proceso bien definido, con o
sin intensidad de IT.

Posición de cada elemento respecto del límite del work system:

- **Completamente dentro**: processes and activities, participants, information,
  technologies.
- **Parcialmente dentro/fuera**: customers y products/services (los clientes a
  menudo participan; los productos/servicios toman forma dentro).
- **Largamente fuera** (con efectos directos dentro): environment,
  infrastructure, strategies.

Razón de inclusión de cada elemento:

| Elemento | Razón de inclusión |
|---|---|
| Processes and activities | Ocurren para producir productos/servicios; un work system debe tener al menos una actividad. "Processes and activities" reconoce que el trabajo puede no ser pasos secuenciales bien definidos; muchos work systems dependen de juicio humano e improvisación (semi-estructurados). Se ven desde una perspectiva **performativa** (cómo se ejecuta el trabajo realmente), no **ostensiva** (cómo debería ejecutarse). |
| Participants | Personas que ejecutan el trabajo, usuarios y no-usuarios de IT. "Participant" en vez de "user" evita ignorar a quienes no usan computadores y la confusión de llamar usuarios a stakeholders. Los clientes suelen ser participantes, sobre todo en service systems. |
| Information | Entidades informacionales usadas/creadas, capturadas, transmitidas, almacenadas, recuperadas, manipuladas, actualizadas, mostradas y/o eliminadas (p. ej. órdenes, facturas, garantías, historias médicas). Incluye información no computarizada (conversaciones, compromisos verbales, conocimiento tácito). La distinción dato/información no importa para entender un work system. |
| Technologies | Casi todo work system significativo depende de tecnología. Incluye **tools** (usadas por participantes) y **automated agents** (configuraciones hw/sw que ejecutan actividades totalmente automatizadas). Distinción crucial al descomponer en subsistemas. |
| Products/services | Razón de ser del work system. Ignorar lo que produce equivale a ignorar su efectividad. Consisten en información, cosas físicas y/o acciones para el beneficio de los clientes. El término evita la controversia producto-vs-servicio del marketing. |
| Customers | Receptores de los productos/servicios para fines distintos de ejecutar trabajo dentro del work system. **Externos** (clientes de la empresa) o **internos** (empleados, p. ej. de un work system de nómina). A menudo son también participantes (pacientes, estudiantes, clientes de consultoría). |
| Environment | Entorno organizacional, cultural, competitivo, técnico, regulatorio y demográfico que afecta efectividad y eficiencia. Incluye stakeholders, políticas, historia y política organizacional. Ignorarlo puede ocultar causas de degradación o falla. |
| Infrastructure | Recursos humanos, informacionales y técnicos usados por el work system pero gestionados fuera de él y compartidos con otros work systems. Incluye infraestructura humana, informacional y técnica (visión de Star & Bowker, no puramente técnica). |
| Strategies | Estrategias de empresa, departamento y work system. Deben alinearse entre niveles; las del work system deben soportar las de departamento y empresa. Pueden no estar articuladas o ser inconsistentes con la realidad. |

**Reglas de alineamiento** (flechas del framework): los elementos deben estar en
alineamiento. Las relaciones principales y necesidades de alineamiento son
**proceso↔participantes**, **proceso↔información** y **proceso↔tecnologías**.
*No* hay flecha que ligue participantes y tecnología en el framework (sí la hay
en el metamodelo, vía la relación "uses" entre participant y tool). El cliente se
ubica arriba: los work systems existen para producir productos/servicios para
clientes, lo que implica un trade-off entre las preocupaciones internas de
gestión (eficiencia, moral) y las del cliente (costo total, calidad).

## Work System Life Cycle Model (WSLC) — vista dinámica

El WSLC representa el proceso **iterativo** por el cual los work systems
evolucionan en el tiempo combinando **cambio planificado** (proyectos formales)
y **cambio emergente** (no planificado, vía adaptaciones, *bricolage* y
*workarounds*). Los cambios pueden afectar cualquier elemento del framework.

**Cuatro fases**:

| Fase | Qué ocurre |
|---|---|
| Initiation | Chartering del proyecto: articular visión, fijar objetivos, asignar recursos, evaluar factibilidad. |
| Development | Creación o adquisición de los recursos para implementar los cambios: desarrollo/adquisición/configuración de software, creación de procedimientos, documentación, materiales de capacitación, y otros recursos. |
| Implementation | Implementación **en la organización** (no de algoritmos en computadores): plan de despliegue, gestión del cambio, capacitación, conversión, pruebas de aceptación. |
| Operation and maintenance | Operación, monitoreo de desempeño, identificación de excepciones, adaptaciones y workarounds, mejora continua. |

**Cambio emergente** (flechas hacia adentro en cada fase): adaptaciones,
bricolage y workarounds que cambian aspectos del work system sin asignación
separada de recursos de proyecto. La emergencia ocurre en las cuatro fases, no
solo en operación.

**Contraste con el SDLC** (system development life cycle): el SDLC es básicamente
un **modelo de proyecto** cuyo "sistema" es un artefacto técnico que se crea; sus
iteraciones son dentro de un proyecto. El WSLC describe la **evolución de un work
system** a lo largo de múltiples iteraciones, vía proyectos definidos *y* cambios
incrementales. A diferencia de las versiones de control del SDLC, el WSLC trata
el cambio no planificado como parte de la evolución natural del work system.

## Work System Method (WSM)

**WSM** es un método de systems analysis & design flexible y **semiformal**,
basado en WST, creado para **business professionals** (usable en conjunto con
profesionales de IT). Analiza un work system "as-is" y diseña una versión
mejorada "to-be". Su rasgo más notable: los sistemas as-is y to-be son **work
systems**, no configuraciones de hardware/software usadas por usuarios. Puede
usarse a alto nivel o como análisis detallado con templates.

**Seis pasos** (núcleo común a todas las versiones):

1. Identificar el work system más pequeño que tiene el problema u oportunidad;
   resumir brechas de desempeño, fortalezas, vulnerabilidades, incidentes clave.
2. Resumir el work system "as-is" usando un **work system snapshot**.
3. Evaluar la operación del work system con métricas, incidentes clave,
   relaciones sociales y otros factores.
4. Profundizar (drill down) según sea necesario.
5. Proponer cambios resumidos en un work system snapshot del "to-be" que debería
   desempeñarse mejor.
6. Describir las mejoras probables y justificar el proyecto de cambio.

El alcance del work system es **una elección, no un dato**: típicamente el más
pequeño que exhibe el problema. Técnicas de Six Sigma (Pareto, fishbone, value
stream mapping) son tan relevantes como métodos orientados a IT. La producción o
instalación de software puede ser o no requerida.

### Work System Snapshot

Resumen formateado de **una página** del work system en **seis elementos
centrales** del framework: **customers, products/services, processes and
activities, participants, information, technologies**. Los otros tres elementos
(environment, infrastructure, strategies) se excluyen del snapshot por
simplicidad y se consideran al profundizar. El límite de una página enfoca la
atención en el alcance correcto.

**Reglas de consistencia** del snapshot:

1. Cada proceso/actividad se enuncia como oración completa que especifica qué
   participantes ejecutan el trabajo y qué hacen.
2. Cada grupo de participantes participa en al menos un paso.
3. Los clientes se ven como participantes si participan en al menos un paso.
4. Cada entidad informacional y tecnológica listada se crea o usa en al menos un
   paso.
5. Cada producto/servicio es output de al menos un paso.
6. Cada producto/servicio es recibido y usado por al menos un grupo de clientes.
7. Cada grupo de clientes recibe y usa al menos un producto/servicio.

## Las 11 funciones que un IS presta a un work system (F1–F11)

Un IS puede prestar una variedad de **funciones** que contribuyen a la operación
de los work systems que soporta (algunos de los cuales son IS a su vez). Esta es
la lista canónica de funciones que un IS realiza para otro work system:

| # | Función |
|---|---|
| F1 | Proveer acceso a información. |
| F2 | Definir y hacer cumplir reglas para recolectar o compartir información. |
| F3 | Proveer métodos para agregar información. |
| F4 | Proveer métodos para analizar información. |
| F5 | Controlar la secuencia de actividades en workflows. |
| F6 | Hacer cumplir el compliance con reglas de negocio. |
| F7 | Producir alarmas cuando ocurren condiciones predefinidas. |
| F8 | Controlar o facilitar la coordinación. |
| F9 | Sugerir o evaluar decisiones. |
| F10 | Disparar funciones automatizadas. |
| F11 | Ejecutar tareas automatizadas. |

Un entendimiento completo de un IS específico exige identificar qué funciones
presta, evaluar qué tan bien las presta, identificar otras funciones que debería
prestar, e identificar cambios beneficiosos costo-efectivos. Que un IS preste
muchos tipos de función demuestra la **limitación** de pensar el IS como mera
herramienta usada por usuarios, como entidad que procesa información, o como
representación de la realidad. (Alter usa *function* en vez de *role* porque
*role* se asocia a responsabilidades de participantes individuales.)

> **No confundir** estas 11 funciones (lo que un IS *hace para* otro work system)
> con las **operaciones de procesamiento de información** que *definen* qué es un
> IS (capturar, almacenar, recuperar, eliminar, transmitir, manipular, mostrar).
> Son dos listas distintas.

## Formas de overlap entre un IS y el work system que soporta

Existen muchos grados de overlap posibles entre un IS y el work system que
soporta. Cuando el overlap es solo una interfaz simple, el reto de diseño es
hacerla simple y conveniente; los demás casos son más difíciles, sobre todo
cuando las personas tienen responsabilidades simultáneas en work systems
separados.

| Forma de overlap | Descripción | Ejemplo |
|---|---|---|
| Interfaz simple | Interacción a través de una interfaz simple. | Uso de un cajero ATM (A = work system del dueño del ATM; B = work system del usuario que lo busca e interactúa para obtener efectivo). |
| Separación / overlap mínimo | El IS provee información externa al work system soportado. | Sitio de reservas de viaje (A = work system automatizado del sitio; B = work system del usuario que busca el mejor trade-off costo/conveniencia). |
| Overlap sustancial | El IS sirve múltiples funciones y hace mucho más que responder consultas y almacenar datos. | Sistema EMR usado por un médico (A = work system EMR multifunción; B = work system de prestar atención médica). |
| Enclosure | Un work system encierra a otro. | Cierre financiero periódico (A = IS totalmente automatizado que genera reportes contables; B = IS contable sociotécnico que toma decisiones y produce estados financieros). |

Caso paradigmático de overlap sustancial: los **EMR** han aumentado el burnout
en médicos de atención primaria que participan simultáneamente en dos work
systems, alternando entre tratar pacientes, buscar datos en el EMR e ingresar
datos en él en un tiempo limitado.

## Extensiones de WST

WST tiene un núcleo (concepto, framework, WSLC) y un conjunto de extensiones
desarrolladas para superar limitaciones observadas en el uso de WSM. Se tratan
como desarrollos útiles fuera del núcleo de WST.

### Work system principles (24)

Principios de diseño que aplican a la mayoría de los work systems sociotécnicos.
Desarrollados iterativamente; incorporan nueve principios sociotécnicos de Cherns
(1976); sanity-checked con Executive MBA students. Son **mutuamente
inconsistentes** en algunas situaciones (p. ej. "complacer al cliente" vs "hacer
el trabajo eficientemente").

| # | Principio | Elemento |
|---|---|---|
| 1 | Complacer a los clientes. | Customers / Products-services |
| 2 | Balancear prioridades de distintos clientes. | Customers / Products-services |
| 3 | Igualar la flexibilidad del proceso con la variabilidad del producto. | Processes & activities |
| 4 | Ejecutar el trabajo eficientemente. | Processes & activities |
| 5 | Alentar el uso apropiado del juicio. | Processes & activities |
| 6 | Controlar los problemas en su fuente. | Processes & activities |
| 7 | Monitorear la calidad y el timing de inputs y outputs. | Processes & activities |
| 8 | Los límites entre pasos deben facilitar el control. | Processes & activities |
| 9 | Igualar las prácticas de trabajo con los participantes. | Processes & activities |
| 10 | Servir a los participantes. | Participants |
| 11 | Alinear los incentivos de los participantes con los objetivos del sistema. | Participants |
| 12 | Operar con roles y responsabilidades claros. | Participants |
| 13 | Proveer información donde afectará la acción. | Information |
| 14 | Proteger la información de uso inapropiado. | Information |
| 15 | Usar tecnología costo-efectiva. | Technologies |
| 16 | Minimizar el esfuerzo consumido por la tecnología. | Technologies |
| 17 | Aprovechar plenamente la infraestructura. | Infrastructure |
| 18 | Minimizar el conflicto innecesario con el entorno externo. | Environment |
| 19 | Soportar la estrategia de la firma. | Strategies |
| 20 | Mantener compatibilidad y coordinación con otros work systems. | Work system como todo |
| 21 | Incorporar objetivos, medición, evaluación y feedback. | Work system como todo |
| 22 | Minimizar riesgos innecesarios. | Work system como todo |
| 23 | Mantener el balance entre los elementos del work system. | Work system como todo |
| 24 | Mantener la capacidad de adaptarse, cambiar y crecer. | Work system como todo |

### Work system design spaces (6)

Conjuntos organizados de cambios comunes, direcciones de cambio y/o factores cuya
naturaleza problemática puede impulsar el cambio. Ayudan a analistas a considerar
caminos de mejora que de otro modo no imaginarían.

1. **Work system principles** — usados como checklist; las brechas "as-is" /
   "to-be" / "should-be" señalan direcciones de mejora.
2. **Tipos genéricos de cambios** — para cada uno de los seis elementos del
   snapshot (p. ej. agregar/combinar/eliminar pasos, cambiar reglas de negocio,
   cambiar la relación con el cliente).
3. **Design characteristics** — para cada elemento y para el work system como
   todo, tratadas como dimensiones de diseño (simple↔complejo,
   no-estructurado↔estructurado, manual↔automatizado).
4. **Common risks and obstacles** — asociados a cada elemento y al work system
   como todo.
5. **Alternative locations of information and knowledge** — dónde y en qué forma
   debe residir el conocimiento (tácito en participantes, en la lógica de
   procesos, en reglas de negocio, en sistemas expertos, en hw/sw).
6. **Direct and indirect interactions with other work systems** — interacciones
   esenciales para la operación o que pueden degradarla; base de la *system
   interaction theory*.

### Work system metamodel

Especificación más detallada del work system framework, en forma de modelo
conceptual con **31 entity types** y numerosas relaciones (Alter, 2010a).
Reinterpreta cada elemento en forma más detallada: *information* → *informational
entity*; *technology* → *technological entity*, dividida en **tools** y
**automated agents**; las actividades las ejecuta uno de **tres tipos de actor
role** (non-customer participant, customer participant, automated agent). Incluye
la relación "uses" entre *participant* y *tool* (el framework no incluye el
término *user*). Soporta análisis detallado cercano al de los profesionales de
IT; fue extendido como metamodelo para diseño de service systems y para convertir
work system snapshots en diagramas de casos de uso UML.

### Facets of work (18)

Aspectos genéricos relacionados con *processes and activities* (análogos a las
facetas de un diamante), que representan un gran cuerpo de conocimiento práctico
e investigativo apenas mencionado en los métodos de SA&D: making decisions,
communicating, processing information, thinking, representing reality, providing
information, applying knowledge, learning, planning, controlling execution,
improvising, coordinating, performing physical work, performing support work,
interacting socially, providing service, creating value, maintaining security.
(La idea se extiende a *facets of work system elements* para los demás
elementos.)

### Work system axioms (25)

Axiomas que se asumen verdaderos para todos los work systems (parte del Proposed
Theoretical Foundation for IS, 2021); pueden desafiarse exhibiendo un work system
que no los cumpla. Agrupados en cinco bloques:

- **Work systems in context (A1–A4)**: sistema abierto con inputs/outputs;
  intenciones de resultados beneficiosos para beneficiarios; stakeholders =
  beneficiarios + otros que se interesan; importan las interacciones con el
  entorno.
- **Work systems in operation (A5–A11)**: ejecuta actividades; requiere recursos
  (organizacionales, técnicos, informacionales, societales); regulación implícita
  o explícita; interacciones internas; interacciones externas para transferir
  beneficios; la gestión/mantención consume recursos; un work system no trivial
  es un sistema de sistemas.
- **Goals and goal attainment (A12–A18)**: el logro de múltiples objetivos
  depende de forma, características y operación; trade-offs por conflictos
  interno/externo; alineamiento interno y externo; congruencia; fit operacional;
  requisite variety.
- **Uncertainties (A19–A21)**: la agencia de actores humanos y automatizados
  implica que un work system puede o no perseguir los objetivos declarados;
  compliance y noncompliance pueden ser beneficiosos o dañinos; incertidumbre de
  resultados.
- **Change (A22–A25)**: design incompletion; evolución por cambio planificado y
  no planificado; path dependence; absorptive capacity.

### Theory of workarounds

Extensión de WST que explica el cambio emergente. **Workaround**: *"goal-driven
adaptation, improvisation, or other change to one or more aspects of an existing
work system in order to overcome, bypass, or minimize the impact of obstacles,
exceptions, anomalies, mishaps, established practices, management expectations, or
structural constraints"* percibidos como impedimento para alcanzar el nivel
deseado de eficiencia/efectividad u otros objetivos. Reconoce que un workaround
puede ser **noncompliance beneficiosa** (y, recíprocamente, que el compliance
puede ser detrimental). Los workarounds pueden volverse, con el tiempo, rutinas y
luego mejoras planificadas (improvisación → bricolage → cambio planificado).

## Glosario de conceptos clave de WST

| Concepto | Definición |
|---|---|
| Work | En contextos organizacionales, uso de recursos humanos, informacionales, físicos y otros para producir productos/servicios. |
| Work system | Sistema en que participantes humanos y/o máquinas ejecutan work (procesos y actividades) usando información, tecnología y otros recursos para producir productos/servicios para clientes internos y/o externos. Sociotécnico por defecto; la definición también abarca work systems totalmente automatizados sin participantes humanos. |
| Special cases of work systems | Information systems, supply chains, projects, self-service work systems, totally automated work systems, entre otros. Heredan la mayoría de los conceptos del caso general. |
| Work system theory (WST) | Cuerpo integrado: teoría analítica Tipo 1 (work system framework) + teoría explicativa Tipo 2 (WSLC), que juntas dan base a una teoría de diseño Tipo 5 (WSM). |
| Work system approach | Sinónimo de work system theory. |
| Work system framework | Representación de los 9 elementos de un entendimiento básico de un work system mientras mantiene su identidad e integridad, aunque cambios incrementales modifiquen detalles de forma/función. |
| Work system life cycle model (WSLC) | Representación del proceso iterativo por el que los work systems evolucionan combinando cambio planificado (proyectos) y cambio emergente (bricolage, adaptaciones, workarounds). |
| Work system method (WSM) | Método de systems analysis & design basado en analizar un work system "as-is" y diseñar una versión mejorada "to-be". |
| Work system snapshot | Herramienta básica de WSM: resumen formateado de una página del work system en seis elementos (processes & activities, participants, information, technologies, products/services, customers). |
| Work system principles | Principios generales que deberían aplicar a todos los work systems (24). |
| Work system design spaces | Conjunto de espacios de diseño basados en el framework que ayudan a identificar posibilidades de mejora (6). |
| Work system metamodel | Modelo conceptual que identifica entity types y relaciones para describir un work system con más detalle que el framework (31 entity types). |

## Relevancia para la práctica

WST aporta una alternativa a la asunción tecno-céntrica de que los sistemas son
configuraciones de hardware/software usadas por usuarios. Es útil a quienes deben
enfocarse en operación y resultados de negocio más que en usos de tecnología, y
puede mejorar la colaboración entre profesionales de negocio y de IT al dar una
base común de entendimiento. En el Proposed Theoretical Foundation for IS (2021),
Alter postula que **un IS es un caso especial de work system** y que IS, proyectos
y sus casos especiales **heredan** la mayoría de los conceptos y generalizaciones
de los work systems en general — base para organizar un body of knowledge de la
disciplina IS.
