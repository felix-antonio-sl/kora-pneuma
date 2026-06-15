---
urn: urn:fxsl:kb:opm-es
nombre: opm-es
version: 3.0.2
estado: publicado
descripcion: "Núcleo conceptual canónico de OPM (ISO 19450) en español: semántica de objetos, procesos, estados y enlaces — capa semántica de la SSOT OPM-ES de cuatro capas."
fuente: "SSOT OPM v3.0.2. Re-sincronizado desde la bestia (~/kora) artifacts/knowledge/fxsl/opm/opm-ssot-es/opm-iso-19450-es.md (sha256:f3cfd2201282bfa5a364536950214bf6115565804c4fd75ce430d5ed5f22d4ab) el 2026-06-15; cuerpo byte-fiel. DECISION HITL 2026-06-15: pneuma toma la posta como SSOT viva de OPM (urn:kora:kb:regimen-de-ley); la bestia queda como ultimo origen historico, ya no SSOT viva. Reemplaza la migracion snapshot del 2026-06-12 (v3.0.0); incorpora los deltas v1.4.0 del corpus consolidado (6.a familia de enlace Excepcion, abanicos convergentes de habilitadores, ruta sobre habilitadores, R-FAN-PROB-1 A/B/C, R-NOM-PROC-1 deverbal, co-enmiendas de bases)."
autor: FS
creado: 2026-04-27
lang: es
tags: [opm, fundamentos, ingenieria-de-sistemas, modelado-conceptual, representacion-bimodal, mbse, opl-es, v2, ampliada]
familia: bok
cita: [urn:fxsl:kb:manual-metodologico-opm-es, urn:fxsl:kb:opd-es, urn:fxsl:kb:opl-es]
---


# OPM — Núcleo conceptual (v3.0.0)


Lenguaje conceptual compacto y metodología para modelar sistemas y representar conocimiento. Esta edición presenta una adaptación canónica en español técnico natural de OPM y adopta **OPL-ES** como forma textual canónica del corpus.

Esta versión integra los ajustes de la línea `merge-ready`: modelo compuesto por referencia, mecanismo explícito de composición inter-modelo como cuarto par canónico de refinamiento-abstracción, separación entre identidad persistente y etiquetas visibles de navegación, y cláusulas de referencia externa para cosas y OPDs citables.

Es la **capa semántica canónica** del corpus OPM-ES en KORA (v3.0.0). Reemplaza a la línea `ssot/` legacy, ya removida del repositorio.

OPM ofrece dos modalidades semánticamente equivalentes:

- **gráfica**, mediante un conjunto de OPDs;
- **textual**, mediante párrafos de OPL-ES.

La meta sigue siendo la misma: permitir que las personas expertas de dominio comprendan el modelo sin perder precisión formal, unificando función, estructura y comportamiento dentro de un único formalismo.

## Contrato editorial del corpus

Este documento es la **capa semántica y ontológica canónica** del corpus OPM en español. Su responsabilidad es:

- fijar definiciones, clases de elementos y clases de relaciones;
- establecer principios de modelado, conformidad y criterio semántico;
- delimitar qué hechos del modelo existen independientemente de su representación textual o gráfica.

Este documento **no** es la fuente canónica de:

- la realización textual en español, que pertenece a [OPL-ES](urn:fxsl:kb:opl-es);
- la gramática gráfica exhaustiva del OPD, que pertenece a [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es);
- el procedimiento de construcción, refinamiento y gobernanza del modelo, que pertenece a [Manual metodológico de OPM](urn:fxsl:kb:manual-metodologico-opm-es).

Regla editorial: este documento puede nombrar esas capas para ubicar la semántica, pero no debe duplicar sus tablas canónicas ni su casuística operativa.

---

## Alcance y conformidad

OPM se especifica con suficiente detalle como para que quienes modelan puedan producir modelos conceptuales con distintos niveles de profundidad y quienes construyen herramientas puedan implementar software compatible.

**Convención de referencias §:** las referencias `§N` sin prefijo de documento en esta capa remiten a secciones de este mismo documento. Las referencias a otras capas del corpus incluyen el documento destino.

Tres niveles de conformidad:

| Nivel | Requisitos |
|---|---|
| Parcial (simbólico) | Uso exclusivo de símbolos OPM y de elementos con semántica asignada |
| Completo | Parcial + aplicación consistente de principios, contexto y refinamiento |
| Herramienta | Parcial + soporte para conformidad completa + soporte textual OPL según EBNF |

No hay referencias normativas externas.

---

## Glosario

La tabla siguiente consolida el glosario operativo de esta capa. Los términos base conservan su numeración histórica para mantener estabilidad editorial; cualquier adición fuera de esa numeración se marca explícitamente.

| ID | Término | Definición |
|---|---|---|
| 3.1 | Abstracción | Disminución del grado de detalle y de la completitud del modelo del sistema (3.8) para mejorar la comprensión |
| 3.2 | Afectado | Transformado cuyo estado cambia por acción de un proceso; debe ser un objeto con estados |
| 3.3 | Agente | Habilitador que es una persona o un grupo de personas |
| 3.4 | Atributo | Objeto que caracteriza una cosa distinta de sí mismo |
| 3.5 | Comportamiento | Transformación de objetos (3.39) resultante de la ejecución de un modelo OPM compuesto por una colección de cosas (3.76) y enlaces (3.36) |
| 3.6 | Beneficiario | Interesado (3.65) que recibe valor funcional de la operación (3.46) del sistema |
| 3.7 | Clase | Colección de cosas (3.76) con los mismos valores de perseverancia (3.50), esencia y afiliación, y el mismo conjunto de rasgos (3.21) y estados de objeto (3.68) |
| 3.8 | Completitud | Grado en que todos los detalles del sistema están especificados |
| 3.9 | Enlace de condición | Enlace procedimental desde objeto o estado hacia proceso que expresa una restricción procedimental |
| 3.10 | Consumido | Transformado que un proceso consume o elimina |
| 3.11 | Contexto | Porción del modelo OPM representada por un OPD y su párrafo OPL correspondiente |
| 3.12 | Enlace de control | Enlace procedimental con semántica adicional de control |
| 3.13 | Modificador de control | Símbolo sobre un enlace que agrega semántica de control: `e` o `c` |
| 3.14 | Atributo discriminante | Atributo cuyos valores identifican especializaciones |
| 3.15 | Efecto | Cambio de estado de un objeto o de un valor de atributo; solo aplica a objetos con estados |
| 3.16 | Elemento | Cosa o enlace |
| 3.17 | Habilitador | 〈proceso〉 Objeto (3.39) que permite un proceso (3.58) sin ser transformado por este |
| 3.18 | Evento | 〈OPM〉 Instante de creación (o aparición) de un objeto (3.39), o entrada de un objeto a un estado (3.68) particular, cualquiera de los cuales puede iniciar la evaluación de una precondición (3.53) del proceso |
| 3.19 | Enlace de evento | Enlace de control que representa un evento desde objeto o estado hacia proceso |
| 3.20 | Exhibidor | Cosa caracterizada por un rasgo mediante exhibición-caracterización |
| 3.21 | Rasgo | Atributo u operación |
| 3.22 | Plegado | Abstracción que oculta refinadores de un refinable desplegado |
| 3.23 | Función | Proceso que entrega valor funcional a un beneficiario |
| 3.24 | General | Refinable con especializaciones |
| 3.25 | Informacional | Relativo a datos, información o conocimiento |
| 3.26 | Herencia | Asignación de elementos OPM desde un general a sus especializaciones |
| 3.27 | Enlace de entrada | Enlace desde un objeto o estado fuente hacia un proceso transformador |
| 3.28 | Instancia de modelo | Objeto o proceso que actúa como instancia en clasificación-instanciación |
| 3.29 | Instancia operacional | Cosa identificable de forma única durante la operación o simulación |
| 3.30 | Instrumento | Habilitador no humano |
| 3.31 | Invocación | Inicio de un proceso por otro proceso |
| 3.32 | Conjunto de objetos involucrados | Unión del conjunto previo al proceso y del conjunto posterior al proceso |
| 3.33 | Contexto de descomposición | Cosas y enlaces dentro del límite de una cosa descompuesta |
| 3.34 | Descomposición de objeto | Despliegue por partes que muestra el orden espacial de objetos constituyentes |
| 3.35 | Descomposición de proceso | Despliegue por partes que muestra el orden temporal parcial de procesos constituyentes |
| 3.36 | Enlace | Expresión gráfica de una relación estructural o procedimental |
| 3.37 | Metamodelo | Modelo de un lenguaje de modelado |
| 3.38 | Hecho de modelo | Relación entre dos cosas OPM o entre estados |
| 3.39 | Objeto | Elemento del modelo que representa una cosa con existencia física o informacional potencial |
| 3.40 | Clase de objeto | Patrón para objetos con la misma estructura y el mismo patrón de transformación |
| 3.41 | OPD | Representación gráfica OPM de un modelo o parte de un modelo |
| 3.42 | OPL | Representación textual de OPM; en esta edición, OPL-ES es la forma canónica |
| 3.43 | OPM | Lenguaje formal bimodal, gráfico y textual, para especificar sistemas complejos y multidisciplinarios |
| 3.44 | Árbol de objetos OPD | Árbol que muestra la elaboración de un objeto a través del refinamiento |
| 3.45 | Árbol de procesos OPD | Árbol generado desde el SD por descomposición de procesos; principal mecanismo de navegación |
| 3.46 | Operación | Proceso que caracteriza una cosa, es decir, lo que esa cosa hace |
| 3.47 | Enlace de salida (output link) | Enlace desde un proceso transformador hacia el estado de destino (salida) de un objeto. Forma parte del par de efecto con estado especificado junto con el enlace de entrada (3.27) |
| 3.48 | Recomposición de objeto | Inverso de la descomposición de objeto |
| 3.49 | Recomposición de proceso | Inverso de la descomposición de proceso |
| 3.50 | Perseverancia | Propiedad: persistente para objeto, transitoria para proceso |
| 3.51 | Poscondición | Condición que resulta de la finalización exitosa de un proceso |
| 3.52 | Conjunto posterior al proceso | Objetos que permanecen o resultan tras completar un proceso |
| 3.53 | Precondición | Condición para iniciar un proceso |
| 3.54 | Conjunto previo al proceso | Objetos evaluados antes de iniciar un proceso |
| 3.55 | Esencia primaria | Esencia mayoritaria, informacional o física, de las cosas del sistema |
| 3.56 | Enlace procedimental | Notación gráfica de una relación procedimental |
| 3.57 | Relación procedimental | Conexión dependiente del tiempo o de condiciones entre objeto o estado y proceso |
| 3.58 | Proceso | Transformación de uno o más objetos |
| 3.59 | Clase de proceso | Patrón para procesos con el mismo patrón de transformación |
| 3.60 | Propiedad | Anotación de modelado que distingue elementos: cardinalidades, etiquetas y etiquetas de ruta |
| 3.61 | Refinable | Cosa susceptible de refinamiento: todo, exhibidor, general o clase |
| 3.62 | Refinador | Cosa que refina a un refinable: parte, rasgo, especialización o instancia |
| 3.63 | Refinamiento | Elaboración que incrementa detalle y completitud |
| 3.64 | Resultante | Transformado que un proceso crea |
| 3.65 | Interesado | Persona u organización con interés en el sistema |
| 3.66 | Objeto con estados | Objeto con estados especificados |
| 3.67 | Objeto sin estados | Objeto sin estados especificados |
| 3.68 | Estado de objeto | Situación o posición posible de un objeto |
| 3.69 | Estado de sistema | Instantánea del modelo del sistema en un momento dado |
| 3.70 | Expresión de estados | Refinamiento que revela un subconjunto de estados de un objeto |
| 3.71 | Supresión de estados | Abstracción que oculta un subconjunto de estados de un objeto |
| 3.71a | Designación de estado | Calificación que asigna a un estado de objeto un rol persistente dentro de su conjunto de estados. Esta adaptación reconoce cuatro designaciones: **inicial**, **final**, **por defecto** y **`Current` declarado** (ver §Estados iniciales, `Current`, por defecto y finales). |
| 3.72 | Enlace estructural | Notación gráfica de una relación estructural |
| 3.73 | Relación estructural | Conexión operacionalmente invariante entre cosas |
| 3.74 | Estructura | Objetos y relaciones no transitorias del modelo |
| 3.75 | Diagrama de Sistema (SD) | OPD raíz que muestra la función del sistema y su contexto de nivel superior |
| 3.76 | Cosa | Objeto o proceso |
| 3.77 | Transformación | Creación, consumo o cambio de estado de un objeto |
| 3.78 | Transformado | Objeto afectado por un proceso |
| 3.79 | Enlace transformador | Enlace de consumo, efecto o resultado |
| 3.80 | Despliegue | Refinamiento que agrega detalle a refinadores |
| 3.81 | Valor de atributo | Estado de un atributo |
| 3.82 | Valor funcional | Beneficio derivado de la función de un sistema |
| 3.83 | Todo | Agregado |
| E1 | OPPL | Capa de clasificación de oraciones sobre OPL usada para graduar la informatividad del modelo. |

Notas normativas clave:

- **Propiedad vs atributo (3.60):** a diferencia de un atributo, el valor de una propiedad no cambia durante la simulación ni en la implementación operacional. Cardinalidades, etiquetas y etiquetas de ruta son propiedades.
- **No hay estados de proceso:** OPM reserva los estados (3.68) para objetos. No usa estados de proceso como "iniciado", "en proceso" o "terminado". En su lugar se modelan subprocesos como *Iniciar*, *Procesar* o *Finalizar*.
- **Toda cosa implica instancias (3.28/3.29):** al crear una cosa en el modelo conceptual, quien modela implica que al menos una instancia operacional de esa cosa, o de una especialización suya, puede existir durante la operación del sistema.

---

## Principios de modelado

Seis principios gobiernan el modelado OPM:

1. **Actividad al servicio de un propósito.** La función del sistema y el propósito del modelado definen el alcance y el nivel de detalle. Diferentes interesados requieren diferentes vistas del mismo sistema.
2. **Unificación de función, estructura y comportamiento.** Estructura más comportamiento producen función. La estructura reúne objetos físicos e informacionales y sus relaciones estructurales. El comportamiento reúne procesos que transforman objetos a lo largo del tiempo.
3. **Identificación del valor funcional.** El proceso que entrega valor expresa la función tal como la percibe el beneficiario principal. Identificar y nombrar ese proceso es el paso crítico inicial.
4. **Función vs comportamiento.** La función es el valor para el beneficiario; el comportamiento es cómo opera el sistema. La misma función puede implementarse con estructuras y comportamientos distintos.
5. **Definición del límite del sistema.** El entorno es el conjunto de cosas fuera del sistema que pueden interactuar con él. Las cosas sistémicas tienen contorno sólido; las ambientales, contorno discontinuo.
6. **Equilibrio entre claridad y completitud.** Los sistemas reales contienen demasiado detalle para una sola vista. La comprensión requiere balancear claridad y completitud mediante una jerarquía de OPDs.

---

## Conceptos fundamentales

### Representación bimodal

Todo modelo OPM individual se expresa en dos formas equivalentes:

- **OPD**, la representación gráfica;
- **OPL-ES**, la representación textual canónica en español.

Cada OPD tiene un párrafo OPL correspondiente dentro del mismo modelo individual. La redundancia entre la representación gráfica y la textual aprovecha los dos canales cognitivos, visual y verbal.

Cuando un modelo OPM referencia otros modelos OPM como sub-modelos, la equivalencia OPD↔OPL se preserva íntegramente **dentro** de cada modelo individual. La composición **entre** modelos no colapsa esa dualidad en una única especificación cerrada: se regula por referencias explícitas entre fronteras de modelo y por metadatos persistentes de identidad.

### Elementos de modelado

Existen dos clases de elementos:

- **cosas**: objetos y procesos;
- **enlaces**: procedimentales y estructurales.

### Gestión de contexto

El OPD es la unidad fundamental para representar un contexto. Los mecanismos principales de gestión contextual **intra-modelo** son:

- expresión y supresión de estados;
- despliegue y plegado;
- descomposición y recomposición.

Además, un modelo OPM puede gestionar contexto **inter-modelo** mediante composición por referencia a sub-modelos. Esta composición cruza la frontera del modelo como unidad de serialización y no debe confundirse con una vista ad hoc ni con una mera operación de navegación.

Operaciones auxiliares como `bring connected things`, `bring links between selected entities` o equivalentes materializan sobre un OPD hechos ya existentes en el modelo. Son operadores derivados de contexto, no mecanismos ontológicos adicionales.

#### Tabla de equivalencia terminológica (mecanismos de refinamiento)

El corpus usa términos en español como forma canónica. Los términos en inglés se conservan como equivalentes de referencia:

| Español (canónico) | Inglés de referencia | Mecanismo |
|---|---|---|
| Descomposición | In-zooming | Exponer contenido interno de una cosa en un OPD hijo |
| Recomposición | Out-zooming | Ocultar contenido interno, restaurando el OPD padre |
| Despliegue | Unfolding | Exponer refinadores vía relación estructural fundamental |
| Plegado | Folding | Ocultar refinadores de un refinable desplegado |
| Expresión de estados | State expression | Revelar un subconjunto de estados de un objeto |
| Supresión de estados | State suppression | Ocultar un subconjunto de estados de un objeto |
| Contenedor | Container | Cosa refinada agrandada en el OPD hijo |
| Proceso inflado | Inflated process | Elipse del proceso agrandada para contener subprocesos |
| Semi-plegado | Semi-fold | Compresión parcial de refinadores |

### Modelos conceptuales y de ejecución

Los modelos conceptuales describen patrones de estructura y comportamiento. Los modelos de ejecución representan instancias operacionales durante una simulación. Un modelo con un nivel consistente de detalle es implementable como simulación capaz de activar recursos y producir valor funcional; ese es el criterio formal de completitud.

#### Modelos conceptuales vs modelos de ejecución (cfr. ISO 19450 §6.2.6.1)

Quien modela debe distinguir entre el modelo conceptual y una ocurrencia operacional (en tiempo de ejecución) usada para evaluar el comportamiento del sistema. Un modelo OPM es un marco formal donde ocurrencias de objetos y procesos interactúan mediante enlaces. Quien modela puede simular el comportamiento creando instancias operacionales de cosas y siguiendo el flujo de control de ejecución definido por las conexiones y las reglas semánticas de OPM.

La presencia de ocurrencias de cosas traduce el modelo conceptual abstracto en una forma concreta de ejecución. El comportamiento del sistema modelado solo ocurre cuando existen instancias operacionales. Un enlace entre dos cosas no implica comportamiento hasta que existan instancias operacionales. La noción de tiempo de ejecución está implícita en toda declaración de especificación.

#### Realización del modelo (cfr. ISO 19450 §6.2.6.2)

Un modelo que expresa detalle consistente es implementable como simulación capaz de realizar recursos, usar procesos para transformar objetos y producir valor funcional para un beneficiario. Esta es la capacidad de realización del modelo.

#### Navegación de OPD y composición de OPL (cfr. ISO 19450 §6.2.6.3)

Los mecanismos de descomposición y despliegue de esta capa proveen las formas de enlazar diagramas OPD con el OPL correspondiente. En esta adaptación ampliada, la capa sí prescribe la vinculación canónica entre etiquetas visibles de navegación, OPDs relacionados y segmentos OPL locales, manteniendo la distinción entre etiqueta visible e identidad persistente.

---

## Especificación de la notación visual

La capa gráfica de OPM usa un conjunto mínimo de formas, contornos, sombreados y marcas. En la capa base basta distinguir tres **superfamilias**:

- **cosas**: objetos, procesos y estados;
- **enlaces procedimentales**;
- **enlaces estructurales**.

Dentro de la superfamilia procedimental, la partición operativa canónica distingue:

- enlaces transformadores;
- enlaces habilitadores;
- enlaces de invocación.

Dentro de la superfamilia estructural, la partición operativa canónica distingue:

- enlaces estructurales fundamentales;
- enlaces estructurales etiquetados.

En conjunto, estas dos particiones forman cinco familias canónicas de enlace.

La semántica de cada familia pertenece a esta capa base; su geometría, decoración, composición, comportamiento visual entre OPDs e índices de reglas pertenecen a [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es).

Regla editorial:

- este documento solo necesita afirmar que un hecho del modelo tiene representación gráfica obligatoria;
- la tabla exhaustiva de símbolos, variantes, adornos, arcos, contornos y marcas vive exclusivamente en `opm-visual-es`;
- la realización textual de esos mismos hechos vive exclusivamente en `opm-opl-es`.

---

## Cosas: objetos y procesos

### Objetos

Un objeto es una cosa que existe o puede existir física o informacionalmente. Su persistencia se asume por defecto hasta que un proceso actúe sobre él. Se representa con un rectángulo.

### Procesos

Un proceso transforma uno o más objetos creándolos, afectándolos o consumiéndolos. Tiene duración positiva. Se representa con una elipse.

**Procesos persistentes:** esta adaptación reconoce casos límite en los que un proceso explícito mantiene un estado o condición relevante en el tiempo en vez de introducir un cambio neto observable. Estos casos no invalidan la ontología general de OPM, pero tampoco convierten el mantenimiento de estado en patrón por defecto. Deben reservarse para situaciones en que la temporalidad, el esfuerzo sostenido o la condición mantenida formen parte del hecho del modelo. Ejemplos: *Existir*, *Sostener*, *Mantener*, *Conservar*, *Permanecer*, *Esperar*, *Prolongar*, *Extender*, *Demorar*, *Ocupar*, *Persistir*, *Continuar*, *Soportar*, *Retener*. Para objetos biológicos, *Existir* implica *Vivir*.

### Prueba Objeto-Proceso

Tres criterios distinguen proceso de objeto:

- asociación con el tiempo: el proceso ocurre a lo largo del tiempo;
- asociación verbal: el nombre del proceso expresa acción;
- transformación: el proceso debe transformar al menos un objeto.

La política léxica y sintáctica de nombrado en español no se fija en esta capa. La realización textual canónica de nombres de proceso vive exclusivamente en [OPL-ES](urn:fxsl:kb:opl-es) §1.1. Esta capa base solo exige que el nombre denote una acción o transformación identificable del dominio.

### Propiedades genéricas

Todas las cosas tienen tres propiedades genéricas:

| Propiedad | Valores | Convención |
|---|---|---|
| Perseverancia | persistente (objeto) / transitoria (proceso) | determinada por el tipo |
| Esencia | física / informacional | la informacional es el valor por defecto |
| Afiliación | sistémica / ambiental | la sistémica es el valor por defecto |

**Herencia de afiliación:** los atributos de objetos ambientales son ambientales. Los procesos ejecutados por entidades ambientales son procesos ambientales.

---

## Estados de objeto

### Objetos con y sin estados

Un objeto con estados tiene un conjunto de estados permitidos. En cada instante, una instancia del objeto está en un estado o en transición entre estados. Un objeto sin estados no puede ser afectado; solo puede crearse o consumirse.

### Representación

El estado se representa como un rectángulo redondeado dentro del objeto. Su realización textual canónica pertenece a [OPL-ES](urn:fxsl:kb:opl-es) §3.2 y §14.

### Estados iniciales, `Current`, por defecto y finales

Cuatro designaciones califican estados en esta adaptación: **inicial** (estado al crearse el objeto), **final** (estado al consumirse), **por defecto** (estado más probable al inspeccionar aleatoriamente) y **`Current` declarado** (estado marcado persistentemente como actual por el modelador). Un objeto puede tener cero o más estados iniciales, cero o más finales, como máximo uno por defecto y como máximo un estado `Current` declarado. La realización gráfica de cada designación y la distinción entre estado `Current` declarado y estado actual de runtime viven en [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es) §2.2 y §17.2.

### Valores de atributos

Un atributo es un objeto que caracteriza una cosa. Sus valores son estados del atributo. Puede especificarse unidad de medida. También puede declararse un dominio permitido como intervalo simple o como lista de intervalos. Su realización textual canónica pertenece a [OPL-ES](urn:fxsl:kb:opl-es) §14.

---

## Panorama de enlaces

### Enlaces procedimentales

Existen tres clases canónicas:

- **enlaces transformadores**: conectan proceso con transformado (consumo, resultado o efecto);
- **enlaces habilitadores**: conectan habilitador con proceso (agente o instrumento);
- **enlaces de invocación**: conectan proceso con proceso (firma `Proceso → Proceso`).

**Control como modificador y como enlace autónomo:** los modificadores de control `e` (evento) y `c` (condición) no constituyen una familia procedimental adicional: son anotaciones sobre un enlace transformador o habilitador base, y su semántica aplica sobre ese enlace. El enlace de **excepción** (sobretiempo/subtiempo) es distinto: no anota un enlace base, sino que conecta un proceso fuente con un proceso de manejo (firma proceso→proceso) y es un enlace de control autónomo. La realización gráfica de estas marcas vive en [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es).

**Principio de unicidad del enlace procedimental:** un objeto o estado tiene exactamente un rol respecto de un proceso enlazado: transformado o habilitador.

**Enlaces procedimentales con estado especificado:** conectan el proceso con un estado específico de un objeto, no con el objeto completo.

### Enlaces estructurales

Hay dos clases:

- **etiquetados**, cuya semántica la define quien modela;
- **fundamentales**, con semántica fija: agregación-participación, exhibición-caracterización, generalización-especialización y clasificación-instanciación.

Los enlaces estructurales conectan objetos con objetos o procesos con procesos, excepto exhibición-caracterización, que también puede conectar objetos con procesos.

### Control evento-condición-acción

La ejecución de un proceso comienza cuando:

1. ocurre el evento iniciador, si existe;
2. y se satisface la precondición.

Los eventos se pierden tras la evaluación, incluso si la precondición falla.

- **Conjunto previo al proceso**: consumidos + afectados + habilitadores necesarios antes de iniciar el proceso.
- **Conjunto posterior al proceso**: resultantes + objetos afectados después de completar el proceso.

---

## Enlaces transformadores

Tres tipos básicos:

| Enlace | Semántica | Dirección abstracta |
|---|---|---|
| Consumo | El proceso destruye o elimina el objeto. | objeto → proceso |
| Resultado | El proceso crea o genera el objeto. | proceso → objeto |
| Efecto | El proceso cambia el estado del objeto. | objeto ↔ proceso |

**Restricción sobre modificadores de control del enlace de resultado:** no existen las variantes "evento de resultado" ni "condición de resultado". La razón es que el resultado no existe antes del proceso, pues es creado por él, por lo que no puede ser precondición (`c`) ni disparador (`e`). El consumo sí admite ambos modificadores porque el objeto consumido existe en el conjunto previo al proceso. Esta asimetría entre consumo y resultado es inherente a la ontología OPM: el consumo opera sobre el conjunto previo; el resultado opera sobre el conjunto posterior.

> **Nota de capa base:** el conjunto posterior al proceso no admite precondiciones, por lo que los modificadores `c` y `e` no aplican a enlaces de resultado. Esta restricción es absoluta y no admite excepciones.

### Enlaces transformadores con estado especificado

Los enlaces transformadores pueden restringirse a estados concretos del objeto: consumo con estado, resultado con estado, efecto entrada-salida, efecto solo entrada y efecto solo salida.

La realización textual canónica de estas variantes vive en `opm-opl-es` §4. La realización gráfica vive en `opm-visual-es` §3.

Cuando el consumo ocurre a lo largo del tiempo, puede modelarse mediante una propiedad de tasa del enlace y un atributo de cantidad del consumido. Sin esas propiedades, el consumo se interpreta como inmediato al activarse el proceso.

**Resultado hacia un objeto con estado inicial:** el enlace de resultado debe conectarse al rectángulo del objeto o a un estado distinto del inicial, nunca al estado inicial directamente.

**Semántica de transición del afectado:** una vez que el proceso afectador comienza, el afectado sale del estado de entrada. Solo alcanza el estado de salida al completarse el proceso. Si el proceso se aborta antes, el estado del afectado queda indeterminado salvo que exista manejo de excepción.

**Resolución de salida en efecto con solo estado de entrada:** si no se especifica estado de salida, el destino es el estado por defecto del objeto. Si no existe estado por defecto, se usa la distribución de probabilidad de estados.

---

## Enlaces habilitadores

Los habilitadores son necesarios para que ocurra un proceso, pero no son transformados. Hay dos clases:

| Enlace | Tipo de habilitador |
|---|---|
| Agente | Persona o grupo con toma de decisiones. |
| Instrumento | Objeto inanimado sin decisión propia. |

Si un habilitador deja de existir durante la ejecución, el proceso se detiene y el estado del afectado queda indeterminado.

### Enlaces habilitadores con estado especificado

Los habilitadores también pueden restringirse a un estado específico. El proceso ocurre si y solo si el habilitador está en el estado requerido.

La realización textual canónica de estas variantes vive en `opm-opl-es` §5. La realización gráfica vive en `opm-visual-es` §3.

---

## Enlaces de control: eventos

Los enlaces de evento anotan un enlace transformador o habilitador con `e`. Un evento dispara la evaluación de la precondición y luego se pierde, tanto si la precondición se satisface como si no.

### Enlaces de evento transformadores

Las variantes transformadoras incluyen evento de consumo y evento de efecto, con o sin estado especificado.

### Enlaces de evento habilitadores

Las variantes habilitadoras incluyen evento de agente y evento de instrumento, con o sin estado especificado.

La realización textual canónica de todos los eventos vive en `opm-opl-es` §6. La realización gráfica vive en `opm-visual-es` §4.

---

## Enlaces de control: condiciones y excepciones

### Enlaces de condición

Los enlaces de condición anotan un enlace con `c`. Introducen un **mecanismo de omisión condicional** (*bypass*): si la precondición falla, el proceso se omite en vez de esperar.

### Enlaces transformadores condicionales

Los transformadores condicionales introducen omisión condicional: si falla la precondición, el proceso se omite en vez de esperar. Existen variantes de consumo y efecto, con y sin estado especificado.

### Enlaces habilitadores condicionales

Los habilitadores condicionales aplican el mismo patrón a agentes e instrumentos.

### Enlaces condicionales con estado especificado

Las variantes con estado especificado heredan la misma semántica de omisión condicional, restringida a un estado concreto.

La realización textual canónica de todas las condiciones vive en `opm-opl-es` §7. La realización gráfica vive en `opm-visual-es` §4.

### Enlaces de excepción

Conectan un proceso fuente con un proceso de manejo según la duración observada.

| Enlace | Disparador |
|---|---|
| Sobretiempo | La fuente excede su duración máxima. |
| Subtiempo | La fuente queda por debajo de su duración mínima. |

La duración de un proceso puede especializarse en mínima, esperada y máxima. La distribución de duración determina el valor efectivo por instancia.

La realización textual canónica vive en `opm-opl-es` §8.1. La realización gráfica de los enlaces de excepción vive en `opm-visual-es` §4.4; las propiedades de duración que los disparan viven en `opm-visual-es` §14.

---

## Enlaces de invocación

La invocación modela que un proceso inicia otro. Semánticamente puede verse como la creación de un objeto intermedio transitorio consumido de inmediato por el proceso destino.

| Enlace | Semántica |
|---|---|
| Invocación | Un proceso inicia otro proceso. |
| Auto-invocación | Un proceso se reinicia o se reitera a sí mismo. |

**Invocación implícita** dentro de un proceso descompuesto: la terminación de un subproceso invoca al que se encuentra inmediatamente debajo. No hay enlace explícito; la altura relativa determina el orden. Cuando dos o más subprocesos tienen la misma altura superior, comienzan en paralelo y el último en terminar inicia al siguiente.

**Invocación cíclica con omisión condicional:** los enlaces de invocación modelan comportamiento iterativo o cíclico. Después de cada ciclo, un nodo de decisión booleano evalúa si se vuelve a entrar o se continúa. En sistemas de refrigeración, por ejemplo, *Evaporar* invoca al proceso completo de refrigeración por compresión para expresar el ciclo continuo del refrigerante.

La realización textual canónica vive en `opm-opl-es` §8.2. La realización gráfica vive en `opm-visual-es` §9.

---

## Enlaces estructurales

### Enlaces estructurales etiquetados

Los **enlaces estructurales etiquetados** permiten expresar relaciones semánticas definidas por quien modela, no predefinidas por la ontología OPM. Se distinguen cuatro variantes:

- **Unidireccional**: lleva una etiqueta textual que describe la relación desde la fuente al destino.
- **Unidireccional sin etiqueta (null-tagged)**: la etiqueta por defecto es `se relaciona con` (*relates to*). Se usa cuando la relación existe pero no requiere calificación explícita.
- **Bidireccional**: lleva etiquetas independientes en cada dirección.
- **Recíproco**: la misma semántica aplica en ambas direcciones.

### Relaciones estructurales fundamentales

| Relación | Refinable → refinador |
|---|---|
| Agregación-participación | todo → partes |
| Exhibición-caracterización | exhibidor → rasgos |
| Generalización-especialización | general → especializaciones |
| Clasificación-instanciación | clase → instancias |

Las colecciones incompletas usan una barra horizontal bajo el triángulo. Su realización textual canónica pertenece a [OPL-ES](urn:fxsl:kb:opl-es) §9.

**Restricción de perseverancia:** salvo en exhibición-caracterización, el refinable y los refinadores deben tener la misma perseverancia.

Exhibición-caracterización es el único enlace estructural que puede conectar objetos con procesos: el rasgo es atributo si es objeto y operación si es proceso.

**Clasificación-instanciación:** a diferencia de las otras tres relaciones fundamentales, no distingue entre colección completa e incompleta. El número de instancias puede variar durante la operación.

La realización textual canónica de enlaces estructurales y sus variantes básicas vive en `opm-opl-es` §9. La realización gráfica vive en `opm-visual-es` §8.

### Herencia

Las especializaciones heredan del general:

- todas las partes;
- todos los rasgos;
- todos los enlaces estructurales etiquetados;
- todos los enlaces procedimentales.

Se permite herencia múltiple. Un atributo discriminante restringe los valores válidos para las especializaciones. El máximo número de especializaciones con varios atributos discriminantes es el producto cartesiano de sus valores posibles.

**Mecanismo de sobreescritura:** quien modela puede reemplazar un participante heredado especificando una especialización de ese participante con otro nombre y otro conjunto de estados.

**Regla de existencia en ejecución:** una instancia especializada no existe en ausencia de la instancia más general de la que hereda.

**Procedimiento para crear un general a partir de especializaciones existentes:**

1. identificar rasgos y participantes comunes;
2. crear una nueva cosa general con esos elementos;
3. conectarla con sus especializaciones mediante generalización-especialización;
4. eliminar de las especializaciones lo ahora heredado;
5. migrar al general los enlaces procedimentales y estructurales comunes.

### Enlaces estructurales con estado especificado

Estos enlaces asocian objetos especializados con valores concretos de atributos.

Siete clases se agrupan en tres familias:

- estado especificado en el origen;
- estado especificado en el destino;
- estado especificado en origen y destino.

Las variantes bidireccionales y recíprocas no existen para el caso de estado solo en el destino.

La realización textual canónica de estas variantes vive en `opm-opl-es` §9.4. La realización gráfica vive en `opm-visual-es` §8.5.

---

## Cardinalidades de relación

### Multiplicidad de objetos

La multiplicidad restringe el número de instancias de objeto asociadas a un enlace. El valor por defecto es una instancia por extremo. Aplica a enlaces etiquetados, agregación-participación y enlaces procedimentales.

| Símbolo | Límites |
|---|---|
| `?` | 0..1 |
| `*` | 0..* |
| sin símbolo | 1..1 |
| `+` | 1..* |

La sintaxis base de rango es `qmín..qmáx`. Cuando el rango se declara explícitamente en una superficie visible o textual, esta adaptación admite delimitadores de inclusión y exclusión: `[qmín..qmáx]`, `(qmín..qmáx]`, `[qmín..qmáx)` y `(qmín..qmáx)`. Pueden usarse varios intervalos separados por comas y `*` como extremo abierto. Las restricciones usan `=`, `≠`, `<`, `≤`, `≥`, llaves para conjuntos y el operador `∈`.

**Los nombres de parámetros deben ser únicos en todo el modelo.**

**Las restricciones de participación no aplican a procesos.** La repetición secuencial de un proceso se modela con un proceso recurrente y contador de iteración; la repetición paralela, con subprocesos síncronos o asíncronos dentro de una descomposición.

**Declaración de tipo:** un objeto puede declarar tipo computacional. Los tipos comunes incluyen `boolean`, `string`, `integer`, `float`, `double`, `short`, `long` y `enumerated`.

La realización textual canónica de multiplicidades, restricciones, tipos y rangos vive en `opm-opl-es` §12.

---

## Operadores lógicos: AND, XOR, OR

### AND

AND se expresa con enlaces separados, del mismo tipo, sin tocarse entre sí.

### XOR

Un abanico XOR exige exclusión mutua: exactamente una ruta del abanico queda habilitada.

### OR

Un abanico OR exige inclusión: al menos una ruta del abanico queda habilitada.

### Combinatoria de abanicos de enlaces

XOR y OR aplican a todas las familias de enlaces procedimentales. El extremo convergente es el extremo común; el divergente no lo es.
La realización visual de estos abanicos vive en `opm-visual-es` §5. La realización textual canónica vive en `opm-opl-es` §11.

### Abanicos de enlaces con modificadores de control

Los abanicos XOR y OR pueden combinarse con modificadores de evento y condición. La semántica sigue siendo la de selección exclusiva o inclusiva, enriquecida respectivamente con iniciación o omisión condicional.

### Abanicos probabilísticos

Cada enlace del abanico se anota con `Pr=p`, y las probabilidades suman 1. Si no se anotan probabilidades explícitas, la distribución por defecto es uniforme.

### Trayectorias de ejecución y etiquetas de ruta

Las etiquetas de ruta resuelven ambigüedad cuando existen varias opciones de salida. La regla es: al salir de un proceso, se sigue el enlace cuya etiqueta coincide con la etiqueta de entrada.

La realización textual canónica de etiquetas de ruta y escenarios pertenece a [OPL-ES](urn:fxsl:kb:opl-es) §13.

Un **escenario** es un conjunto de una o más etiquetas de ruta que define una variante concreta de ejecución. En sistemas complejos, los escenarios evitan crear un OPD adicional por cada variante.

---

## Gestión de contexto y refinamiento

### Completar el SD

El Diagrama de Sistema debe modelar:

- interesados, especialmente beneficiarios;
- el proceso que entrega valor;
- las cosas ambientales y sistémicas necesarias para producir un párrafo OPL breve y claro.

El SD debe contener solo las cosas centrales e indispensables. El valor funcional puede aparecer explícitamente como cambio de estado de un atributo del beneficiario o de forma implícita si el beneficiario es afectado.

### Mecanismos de refinamiento y abstracción

Los mecanismos canónicos de refinamiento y abstracción se organizan así:

| Ámbito | Refinamiento | Abstracción |
|---|---|---|
| Estados | Expresión de estados | Supresión de estados |
| Estructura | Despliegue | Plegado |
| Comportamiento | Descomposición | Recomposición |
| Composición inter-modelo | Referencia a sub-modelo | Desconexión o retiro de la referencia |

Hay cuatro pares de despliegue-plegado intra-modelo, uno por relación fundamental: agregación, exhibición, generalización y clasificación.

**Despliegue en el mismo diagrama:** refinable y refinadores comparten OPD.

**Despliegue en nuevo diagrama:** se crea OPD hijo; el refinable aparece con contorno grueso en ambos diagramas.

**Descomposición síncrona (*in-zooming*) vs despliegue asíncrono (*unfolding*):** la descomposición de un proceso es síncrona: el proceso padre espera a que todos los subprocesos completen antes de devolver control. El despliegue de una relación estructural es asíncrono respecto del flujo de control del proceso: revela estructura estática sin implicar secuenciación temporal.

**Composición inter-modelo por sub-modelo:** un sub-modelo es un mecanismo explícito de refinamiento que cruza la frontera del modelo OPM como unidad de serialización. Introduce identidad persistente de vínculo, gobernanza propia y reglas de referencia entre modelo propietario y modelo consumidor.

**Operaciones derivadas:** operaciones como `bring connected things`, `bring links between selected entities`, importes asistidos y otras materializaciones automáticas de contexto no constituyen mecanismos de refinamiento ontológico. Son operadores derivados sobre el árbol y el canvas.

**Diagramas de vista (model views):** OPDs que reúnen hechos provenientes de múltiples OPDs para explicar un fenómeno o enfatizar un aspecto concreto. Las herramientas OPM pueden soportar la creación de vistas que filtren por criterios específicos — si esa capacidad es exigencia de conformidad lo decide el canon prescriptivo operativo (`reglas-opm-estrictas-es`) y su familia, no esta capa —, como:

- el camino crítico para la duración mínima de ejecución del sistema;
- los agentes e instrumentos del sistema;
- todos los objetos y procesos vinculados por un tipo específico de enlace;
- la asignación de cosas de varios OPDs a módulos del sistema.

**Mapa del sistema (system map):** un árbol de procesos OPD que muestra explícitamente el contenido (cosas y enlaces) de cada OPD como nodo. Dado que el mapa puede volverse muy grande, los mecanismos de vista permiten acceder al contenido del modelo y a las asociaciones entre elementos. Su semántica de navegación y su estatus como vista anclada pertenecen a la especificación visual.

---

## Árboles OPD y control implícito

**Árbol de procesos OPD:** raíz `SD`, y cada nodo corresponde a un OPD creado por descomposición de un proceso. Es el mecanismo principal de navegación. Etiquetas típicas: `SD`, `SD1`, `SD1.1`, `SD1.1.1`, etc.

**Árbol de objetos OPD:** raíz en un objeto, muestra su elaboración por refinamiento.

La línea temporal dentro de un proceso descompuesto fluye de arriba hacia abajo. Los subprocesos cuyos puntos de referencia superiores tienen la misma altura se ejecutan en paralelo.

### Resumen de enlaces de invocación implícitos

Dos formas gobiernan la ejecución implícita en descomposición síncrona:

| Forma | Semántica | Indicio estructural |
|---|---|---|
| Invocación implícita | Un subproceso invoca al subproceso inmediatamente inferior cuando termina | puntos superiores de elipses ordenados verticalmente |
| Conjunto de invocación implícita paralela | Varios subprocesos comienzan juntos cuando sus puntos superiores están alineados | mismas alturas en el contexto de descomposición |

---

## Distribución de enlaces a través del contexto

Los enlaces conectados al **contorno exterior** de un proceso descompuesto tienen semántica distributiva. La especificación formal completa de las reglas de distribución — tipos de enlace, restricciones de frontera, distribución por posición de subproceso, excepciones para eventos ambientales y reglas de escisión — vive en [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es) §11 y §12.

Invariantes semánticos que esta capa conserva:

- los enlaces de **consumo** y **resultado** no deben conectarse al contorno exterior de un proceso descompuesto;
- los enlaces de agente e instrumento se distribuyen a todos los subprocesos;
- los enlaces de evento desde objetos sistémicos no deben cruzar el límite de la descomposición para iniciar subprocesos — **excepción:** los enlaces de evento desde objetos **ambientales** pueden cruzar este límite; en tal caso la herramienta debería guiar a quien modela para definir cómo manejar la contingencia (véase §12 de la especificación visual);
- si un enlace de condición hace que un subproceso se omita, el control pasa al siguiente.

---

## Enlaces transformadores escindidos con estado especificado

Cuando un enlace de efecto entrada-salida se descompone en subprocesos, el modelo queda subespecificado. La escisión del enlace en un par (entrada al subproceso temprano, salida al subproceso tardío) es el único mecanismo correcto para resolver esa subespecificación.

La especificación formal de los pares escindidos, su tabla de geometría y sus restricciones vive en [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es) §12.

La realización textual de los enlaces escindidos vive en [OPL-ES](urn:fxsl:kb:opl-es) §4 y §7.

**Cambio de rol con la abstracción:** un objeto puede ser instrumento en un nivel abstracto y afectado en un nivel detallado. Esto es válido cuando, a nivel abstracto, el cambio neto del objeto entre entrada y salida del proceso es nulo (estado inicial = estado final); a nivel detallado, el objeto transita por estados intermedios con entrada ≠ salida dentro del proceso descompuesto, sin violar la invariancia declarada a nivel abstracto.

### Instancias operacionales del conjunto de objetos involucrados

Como consecuencia de la distribución de enlaces, las siguientes restricciones se aplican a las instancias operacionales de los transformados:

1. Cada instancia operacional de un **consumido** en el conjunto previo al proceso DEBE dejar de existir al inicio del subproceso más detallado que lo consume, y la instancia operacional no está en el conjunto posterior al proceso.
2. Cada instancia operacional de un **afectado** en el conjunto previo al proceso que cambia de estado DEBE salir de su estado de entrada al inicio del subproceso más detallado que cambia al afectado.
3. Cada instancia operacional de un **afectado** en el conjunto posterior al proceso que cambia de estado DEBE entrar en su estado de salida al completarse el subproceso más detallado que cambia al afectado.
4. Cada instancia operacional de un **resultante** en el conjunto posterior al proceso DEBE comenzar a existir al completarse el subproceso más detallado que lo genera, y la instancia operacional no está en el conjunto previo al proceso.

---

## Precedencia de enlaces durante la recomposición

Al recomponer, los enlaces procedimentales de subprocesos migran al proceso padre. La **fuerza semántica** determina cuál prevalece cuando dos enlaces compiten por el mismo par objeto-proceso.

La especificación formal de la jerarquía completa de precedencia, incluyendo la matriz transformadora, el orden principal `consumo = resultado > efecto > agente > instrumento`, la precedencia secundaria por modificador de control y el orden completo de **12 niveles** de fuerza semántica, vive en [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es) §13.

Los invariantes semánticos que gobiernan la precedencia se formalizan en `opm-visual-es` §13. Esta capa no los re-enuncia para evitar duplicación con divergencia.

---

## Etiquetas OPD y navegación

**El SD contiene exactamente un proceso sistémico**, que expresa la función del sistema. Puede contener uno o más procesos ambientales.

Etiquetas típicas:

- `SD` para nivel 0;
- `SD1`, `SD2`, etc., para niveles descendientes.

Estas etiquetas visibles son **etiquetas de navegación**, no identificadores persistentes. Su forma puede mutar por reordenamiento de hermanos, inserción de nuevos nodos o cambios de layout que alteren el orden de navegación.

Todo OPD DEBE tener además un identificador persistente, estable bajo renumeración de etiquetas y bajo reordenamiento del árbol. La forma concreta del identificador persistente (UUID, slug, URI u otra) pertenece a la serialización del modelo y no necesita imprimirse en la superficie visible del OPD.

**Etiquetas de aristas del árbol OPD:** cada arista del árbol de procesos usa un enlace estructural etiquetado unidireccional con una fórmula de refinamiento equivalente a `se refina por descomposición de NombreProceso en` o `se refina por despliegue de NombreCosa en`. La realización textual canónica de estas sentencias pertenece a [OPL-ES](urn:fxsl:kb:opl-es) §10.

**Orden de especificación OPL:** la secuencia de párrafos OPL sigue en general el orden de navegación del árbol, comenzando desde `SD`. Ese orden puede proyectarse desde el layout del padre, pero no sustituye la identidad persistente del OPD. El procedimiento operativo de recorrido pertenece a [Manual metodológico de OPM](urn:fxsl:kb:manual-metodologico-opm-es).

**Acoplamiento de proyección:** la posición vertical de un subproceso en el canvas, el orden de navegación del árbol y el orden textual del OPL pueden derivarse coherentemente entre sí. Ese acoplamiento es de **proyección**, no de **identidad**. Ninguno de esos tres canales sustituye al identificador persistente.

### OPL del sistema completo

El OPL del sistema completo es la especificación textual total obtenida al recorrer el árbol OPD y concatenar los párrafos OPL locales en orden de navegación. No describe solo el contexto actual, sino la totalidad del sistema. En modelos compuestos, cada modelo individual conserva su OPL local autocontenido y la composición entre modelos requiere referencias explícitas entre fronteras de modelo.

Núcleo recuperable del ejemplo clásico de *Sistema de Lavado de Platos*:

- `**Usuario Doméstico** maneja *Lavar Platos*.`
- `*Lavar Platos* requiere **Lavavajillas**.`
- `*Lavar Platos* consume **Jabón**.`
- `*Lavar Platos* afecta **Conjunto de Platos**.`
- `SD se refina por descomposición de *Lavar Platos* en SD1.`
- `**Lavavajillas** consta de **Compartimento de Jabón** y otras partes.`
- `**Lavavajillas** puede estar \`vacío\` o \`cargado\`.`
- `Estado \`vacío\` de **Lavavajillas** es inicial y final.`
- `**Compartimento de Jabón** puede estar \`vacío\` o \`cargado\`.`
- `Estado \`vacío\` de **Compartimento de Jabón** es inicial.`
- `**Conjunto de Platos** exhibe **Limpieza**.`
- `**Limpieza** de **Conjunto de Platos** puede estar \`sucio\` o \`limpio\`.`
- `Estado \`sucio\` de **Limpieza** de **Conjunto de Platos** es inicial.`
- `Estado \`limpio\` de **Limpieza** de **Conjunto de Platos** es final.`
- `*Lavar Platos* se descompone en *Cargar Platos*, *Insertar Detergente*, *Lavar y Secar Platos* y *Descargar Platos*, en esa secuencia.`
- `*Cargar Platos* cambia **Lavavajillas** de \`vacío\` a \`cargado\`.`
- `*Insertar Detergente* requiere **Jabón**.`
- `*Insertar Detergente* cambia **Compartimento de Jabón** de \`vacío\` a \`cargado\`.`
- `*Lavar y Secar Platos* requiere **Lavavajillas**.`
- `*Lavar y Secar Platos* consume **Jabón**.`
- `*Lavar y Secar Platos* cambia **Limpieza** de **Conjunto de Platos** de \`sucio\` a \`limpio\`.`
- `*Descargar Platos* cambia **Lavavajillas** de \`cargado\` a \`vacío\`.`

**Simplificación de OPD:** la recomposición dentro del mismo diagrama y la descomposición en nuevo diagrama pueden simplificar un OPD sobrecargado. Restricción: un objeto no puede incorporarse al conjunto abstraído si eso crearía enlaces procedimentales directos entre procesos pares sin semántica OPM.

### Principio de consistencia de hechos OPM

Si un hecho aparece en un OPD y contradice otro hecho del mismo modelo en otro OPD, el modelo es inconsistente y la herramienta debería detectarlo. Que un hecho sea refinamiento o abstracción de otro no constituye contradicción.

---

## Diagrama de sistema: procedimiento y componentes

El SD es el OPD de nivel 0 y proporciona una vista de alto nivel comprensible para cualquier interesado, incluso sin especialización técnica. En la capa base solo interesa su función semántica: expresar la función del sistema y su contexto de máximo nivel.

La construcción detallada del SD, sus variantes por tipo de sistema, la secuencia de preguntas, la jerarquía de detalle, los nodos de decisión y las reglas de praxis asociadas pertenecen a [Manual metodológico de OPM](urn:fxsl:kb:manual-metodologico-opm-es).

---

## Ingeniería de sistemas basada en modelos con OPM

### Visión general de MBSE

La Ingeniería de Sistemas Basada en Modelos (MBSE) usa modelos conceptuales para diseñar y desarrollar sistemas complejos. Los enfoques tradicionales basados en texto carecen de lenguaje estandarizado y de verificación o validación formales. OPM resuelve eso mediante especificación formal bimodal.

### Conceptos alternativos de solución

Procedimiento recomendado para generar alternativas:

1. crear al menos tres modelos conceptuales distintos;
2. aplicar pensamiento creativo holístico;
3. destilar el concepto central de cada uno;
4. explicitar los supuestos implícitos.

Un **concepto** es el principio físico o lógico central de una arquitectura. Los **conceptos alternativos de solución** son enfoques arquitectónicos distintos para un mismo problema.

### Revisión preliminar de diseño (PDR)

Una PDR estructurada incluye ocho secciones:

1. portada;
2. formulación del problema;
3. propósito y motivación;
4. supuestos y restricciones;
5. soluciones alternativas;
6. solución seleccionada con justificación;
7. costos de ciclo de vida y cronograma;
8. riesgos y mecanismos de mitigación.

### OPM como plano común

OPM sirve como especificación neutral entre disciplinas para el diseño detallado de sistemas complejos donde cada disciplina tiene su propio lenguaje. Los modelos detallados suelen abarcar entre **5 y 10 niveles de detalle** en el árbol de procesos OPD.

### Integración virtual

La integración virtual combina modelos conceptuales de hardware con módulos de software ejecutable real. El software controla virtualmente los modelos de hardware, lo que permite validar antes del prototipado físico.

---

## Sintaxis formal de OPL: delegación editorial

La gramática formal completa de OPL-ES deja de vivir en esta capa para eliminar solapamiento con la capa textual canónica. La EBNF española completa, incluyendo producción base, oraciones procedimentales, estructurales, condicionales y de gestión de contexto, vive ahora exclusivamente en [OPL-ES](urn:fxsl:kb:opl-es), Apéndice A.

> **Nota:** El Apéndice A de OPL-ES forma parte vinculante de la capa textual canónica. Las producciones EBNF definidas allí son parte de la especificación del corpus.

Este documento conserva solo el contrato semántico que la gramática textual debe preservar:

- la dualidad OPD–OPL;
- la correspondencia entre familia semántica de enlace y plantilla textual;
- la trazabilidad entre refinamiento del modelo y composición textual;
- la equivalencia semántica entre la formulación inglesa de referencia y la formulación canónica española.

---

## Metamodelo OPM

La estructura del modelo OPM se organiza en tres capas relacionadas:

- **Modelo OPM individual** → conjunto de OPDs (gráfico) + especificación OPL (texto) + metadatos persistentes de identidad
- **Conjunto de OPDs** → OPDs → constructos OPD → conjuntos de cosas + conjuntos de enlaces
- **Especificación OPL** → párrafos OPL → oraciones OPL → frases y nombres reservados

Un modelo OPM individual puede, además, referenciar `0..*` modelos OPM adicionales como sub-modelos. Cuando eso ocurre, se obtiene un **modelo OPM compuesto por referencia**.

La dualidad OPD↔OPL se preserva íntegramente dentro de cada modelo individual. La composición entre modelos no colapsa esas dualidades en una única especificación cerrada: se regula por referencias explícitas entre fronteras de modelo y por metadatos de identidad persistente.

Una cosa puede aparecer en otro modelo como **referencia externa** a la misma existencia compartida. La referencia externa no crea una nueva existencia propietaria. La existencia pertenece al modelo propietario; la aparición en el modelo consumidor es una referencia explícita a esa existencia.

Toda cosa que pueda ser referenciada desde otro modelo y todo OPD que pueda ser citado externamente DEBEN exponer un identificador persistente recuperable en la serialización, por ejemplo un URI o handle persistente declarado por la implementación.

Un **constructo básico** contiene exactamente 2 cosas y 1 enlace. Los constructos compuestos incluyen abanicos de enlaces o más de dos refinadores. Las referencias externas y los vínculos entre modelos no alteran esta definición del constructo básico; pertenecen al nivel metamodelo del compuesto.

---

## Modelo de enlace

Un enlace consta de:

- origen;
- destino;
- conector;
- línea;
- símbolo;
- etiqueta opcional;
- nombre de ruta opcional.

La multiplicidad tiene límites inferior y superior: `0..1`, `0..*`, `1..1`, `1..*`.

## Modelo de cosa

Una cosa es:

- **objeto**, o
- **proceso**.

Los objetos pueden ser sin estados o con estados. Los objetos con estados generan referencias a estados específicos.

**Objeto Específico de Estado (State-Specific Object).** Un objeto con estados que tiene `s` estados genera un conjunto de `s` **objetos específicos de estado**, cada uno de los cuales es una especialización sin estados del objeto original que "refiere a" un estado concreto. El concepto permite simplificar el modelo conceptual: cuando se necesita referenciar un objeto en un estado particular, se puede tratar como un objeto independiente sin estados. Por ejemplo, un **Producto** con estados `diseñado`, `fabricado`, `probado`, `comprado` y `usado` genera cinco especializaciones: **Producto Diseñado**, **Producto Fabricado**, etc. Cada una refiere al estado correspondiente de **Producto** mediante un enlace estructural etiquetado `refiere al estado de`.

- Un objeto sin estados tiene un conjunto de estados de cardinalidad `s=0`.
- Un objeto con estados tiene cardinalidad `s≥1`.
- El estado actual es una instancia de **Estado** dentro del **Conjunto de Estados** del objeto.
- Los estados se especializan en **Estado Inicial**, **Estado Final** y **Estado por Defecto**; adicionalmente, esta adaptación admite **Estado `Current` declarado** como designación persistente opcional, distinta del estado actual de runtime.

## Modelo de constructo estructural

Un constructo estructural básico = refinable + refinador + enlace estructural. Cinco variantes:

- agregación-participación;
- exhibición-caracterización;
- generalización-especialización;
- clasificación-instanciación;
- enlace estructural etiquetado.

## Modelo de constructo procedimental

Un constructo procedimental básico = objeto + proceso + enlace procedimental. Preserva la cardinalidad 2 cosas + 1 enlace del constructo básico.

Las semánticas básicas son:

- transformación;
- habilitación.

Cada una admite un modificador de control `e` (evento) o `c` (condición) sobre el enlace, lo que produce variantes derivadas:

- transformación con control;
- habilitación con control.

El modificador no añade una cosa ni un enlace, por lo que la cardinalidad del constructo básico se preserva. La semántica de cada modificador se especifica en [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es).

Los constructos transformadores se descomponen en:

- consumo;
- efecto;
- resultado.

Los habilitadores se descomponen en:

- agente;
- instrumento.

## Modelos de descomposición y recomposición en nuevo diagrama

Esta adaptación modela la descomposición y la recomposición en nuevo diagrama como procesos OPM de primera clase:

- *Descomposición en nuevo diagrama*: requiere `SDn`, realiza *Mostrar Contenido* y luego *Refinar Enlaces*, y genera `SDn+1`.
- *Recomposición en nuevo diagrama*: requiere `SDn+1`, realiza *Abstraer Enlaces* y luego *Ocultar Contenido*, y genera `SDn`.
- **OPD semidescompuesto**: objeto transitorio que existe solo dentro de esas transformaciones.

Las figuras de referencia muestran la migración de enlaces desde un proceso refinado `P` hacia subprocesos `P1`, `P2`, `P3`, reubicando consumidos, agentes, instrumentos y resultantes en el nivel detallado.

## Simplificación de un OPD

Un OPD sobrecargado puede simplificarse abstrayendo un conjunto acotado de procesos y objetos hacia un constructo de nivel superior, siempre que la abstracción no cree enlaces procedimentales ilegales entre procesos pares.

## Modelo de control del desempeño de procesos

Este modelo autorreferencial completo demuestra cómo OPM controla la ejecución de procesos en tiempo de simulación.

Jerarquía principal:

- `SD`
- `SD1`
- `SD1.1`
- `SD1.1.1`
- `SD1.1.1.1`
- `SD1.2`
- `SD1.2.1`
- `SD1.2.2`
- `SD1.2.3`

**SD: Control del Desempeño de Procesos**
Un *Proceso Ejecutable* invoca *Controlar Desempeño de Proceso*, que afecta el **Conjunto de Objetos Involucrados** y genera un **Mensaje de Éxito** o un **Mensaje de Falla**.

**SD1: Descomposición principal**
*Controlar Desempeño de Proceso* se descompone en *Iniciar Proceso* y *Ejecutar Proceso*, en esa secuencia. **Estado del Proceso** recorre `inactivo → iniciado(t=0) → operando(t<n) → completando(t=n) → completado(t=n)` o `abortado`. **Poscondición** pasa de `falsa` a `verdadera`.

**SD1.1: Iniciar Proceso**
Se descompone en *Evaluar Precondición* → (`Cancelar` | `Iniciar`). Si la precondición es falsa, *Cancelar* genera **Mensaje de Cancelación** y devuelve el estado a `inactivo`. Si es verdadera, *Iniciar* consume la precondición, genera poscondición falsa y cambia el estado del proceso a `iniciado(t=0)`.

**SD1.1.1: Evaluar Precondición**
Se descompone en *Verificar Habilitadores* → *Verificar Consumidos y Afectados* → (`Refutar Precondición` | `Confirmar Precondición`). Si alguna verificación falla, se refuta la precondición; si todas pasan, se confirma.

**SD1.2: Ejecutar Proceso**
Se descompone en *Ejecución Inicial* → *Ejecución Principal* → *Ejecución Final*.

- Inicial: en paralelo, *Salir de Estado de Entrada* + *Consumir Conjunto de Consumidos*.
- Principal: ciclo de *Comparar Tiempo y Duración* → *Verificar Habilitadores y Afectados* → *Ejecutar Proceso e Incrementar Tiempo*.
- Final: en paralelo, *Generar Resultantes* + *Entrar en Estado de Salida* + *Notificar Éxito*.

Ese modelo muestra:

- descomposición multinivel;
- transiciones de estado a través de la jerarquía;
- enlaces condicionales y omisión condicional;
- manejo de excepciones;
- subprocesos paralelos;
- cambio de rol entre instrumento y afectado según el nivel de abstracción.

---

## Dinámica y simulación

### Ejecutabilidad

Un modelo OPM puede ser ejecutable: la simulación anima el sistema ejecutando el modelo en un entorno de software.

### Modos de transformación

| Modo | Significado |
|---|---|
| Construcción | El objeto es creado o generado |
| Efecto | El objeto cambia de estado y mantiene identidad |
| Consumo | El objeto es eliminado y deja de existir |

Construcción y consumo son transformaciones más profundas que efecto porque cambian existencia, no solo estado.

### Principio de línea de tiempo

La línea temporal por defecto en una descomposición fluye de arriba hacia abajo. Subprocesos a la misma altura se ejecutan en paralelo. Un proceso de salida por excepción puede provocar salida inmediata sin importar su posición gráfica.

### Eventos temporizados

Los eventos de estado pueden representar eventos temporales. Objetos tipo reloj o temporizador del sistema con valores concretos pueden iniciar procesos en instantes definidos.

### Diagrama de vida útil

Un diagrama de vida útil muestra, para cualquier instante:

- qué objetos existen;
- en qué estado está cada uno;
- qué procesos están activos.

Es útil para seguir transiciones a lo largo de la vida del sistema.

### Propiedades de duración de proceso

Las propiedades de duración de proceso (mínima, esperada, máxima, distribución) son propiedades semánticas del proceso. Su especificación formal y representación gráfica (ubicación dentro de la elipse, formato) viven en [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es) §14.

La unidad temporal del sistema es la unidad por defecto para todos los procesos, salvo que se redefina.

Ejemplo:

- `Procesar [min] (30.0, 45.6, 60.0)` con distribución `normal, media=45.6, desviación=7.3`.

### Ejemplos de duración

Esta adaptación recoge cuatro patrones recuperables:

1. **Metamodelo de duración de proceso:** una notación compacta puede codificar duración mínima, esperada y máxima junto con parámetros de distribución; la duración real sigue siendo propiedad de ejecución.
2. **Variantes de distribución:** un mismo proceso puede parametrizarse con distribuciones exponencial, normal o uniforme.
3. **Excepción por sobretiempo:** si la duración real supera la duración máxima, ocurre el proceso de manejo de sobretiempo.
4. **Excepción por subtiempo:** si la duración real cae por debajo de la mínima, ocurre el proceso de manejo de subtiempo.

Ejemplos canónicos:

- `Procesar [min] (30.0, 45.6, 60.0)` con `uniforme, a=5.0, b=70.0`, duración real `63.3`, instancia `1`, para el caso de sobretiempo.
- El mismo intervalo de duración, con duración real `23.4` e instancia `2`, corresponde al caso de subtiempo.

---

## Convenciones editoriales delegadas

Las siguientes materias dejan de definirse en esta capa para evitar duplicación interna del corpus:

- buenas prácticas de legibilidad, densidad visual, apariencias múltiples y copias visuales: [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es) §15–§16;
- política de nombrado, capitalización, unicidad nominal y patrones de superficie en español: [OPL-ES](urn:fxsl:kb:opl-es) §1;
- reglas operativas para decidir cuándo descomponer, cuándo duplicar una apariencia y cómo resolver ambigüedad durante el modelado: [Manual metodológico de OPM](urn:fxsl:kb:manual-metodologico-opm-es).

Este documento conserva como invariantes semánticos transversales:

- un estado no existe sin su objeto propietario;
- el objeto consumido desaparece al inicio del proceso, no al final;
- un objeto puede además actuar como disparador (`e`) y/o como condicionante (`c`) sin perder su rol principal como transformado o habilitador;
- la importancia relativa de una cosa suele ser proporcional al OPD más alto de la jerarquía en el que aparece.

---

## Ejemplos aplicados

Ejemplos canónicos del corpus que muestran la notación OPM en uso.

### Mecanizado de barra de acero (enlaces con estado especificado)

Objetos: **Barra de Metal** con estados `pre-cortada`, `cortada`; **Pieza** con estados `pre-probada`, `probada`. Procesos: *Cortar* (ambiental), *Mecanizar* (físico), *Probar* (ambiental). Habilitadores: **Operario de Máquina** y **Refrigerante**.

Composición OPL-ES:

- `*Cortar* cambia **Barra de Metal** de \`pre-cortada\` a \`cortada\`.`
- `*Mecanizar* consume **Barra de Metal** en \`cortada\`.`
- `*Mecanizar* genera **Pieza** en \`pre-probada\`.`
- `**Operario de Máquina** maneja *Mecanizar*.`
- `*Mecanizar* requiere **Refrigerante**.`
- `*Probar* cambia **Pieza** de \`pre-probada\` a \`probada\`.`

### Pago con cheque (descomposición con transiciones de estado)

Objeto: **Cheque** con estados `en blanco → firmado → endosado → cobrado y cancelado`. Atributo: **Custodio** con estados `pagador → beneficiario → institución financiera`. Agentes: **Pagador**, **Beneficiario**, **Banco**.

`*Pagar con Cheque*` se descompone en:

1. `*Escribir y Firmar*`
2. `*Entregar y Aceptar*`
3. `*Endosar y Presentar*`
4. `*Cobrar y Cancelar*`

Ejemplos OPL-ES:

- `*Escribir y Firmar* cambia **Cheque** de \`en blanco\` a \`firmado\`.`
- `*Entregar y Aceptar* cambia **Custodio** de \`pagador\` a \`beneficiario\`.`
- `*Endosar y Presentar* cambia **Cheque** de \`firmado\` a \`endosado\`.`
- `*Cobrar y Cancelar* cambia **Cheque** de \`endosado\` a \`cobrado y cancelado\`.`

### Lavado de platos (cambio de rol según nivel de abstracción)

SD:

- `**Usuario Doméstico** maneja *Lavar Platos*.`
- `*Lavar Platos* requiere **Lavavajillas**.`
- `*Lavar Platos* consume **Jabón**.`
- `*Lavar Platos* afecta **Conjunto de Platos**.`

`SD1`:

- `*Lavar Platos* se descompone en *Cargar Platos*, *Insertar Detergente*, *Lavar y Secar Platos* y *Descargar Platos*, en esa secuencia.`
- `*Cargar Platos* cambia **Lavavajillas** de \`vacío\` a \`cargado\`.`
- `*Descargar Platos* cambia **Lavavajillas** de \`cargado\` a \`vacío\`.`

El punto clave es que **Lavavajillas** es instrumento en el nivel abstracto, pero afectado en el nivel detallado.

### Apertura de caja fuerte (operadores lógicos)

Ejemplos:

- XOR: exactamente uno entre **Propietario A** y **Propietario B** maneja *Abrir Caja Fuerte*.
- OR: al menos uno entre **Propietario A** y **Propietario B** maneja *Abrir Caja Fuerte*.
- AND: `*Abrir Caja Fuerte* requiere **Llave A**, **Llave B** y **Llave C**.`

### Especialización de vehículos (atributo discriminante)

- `**Vehículo** exhibe **Medio de Desplazamiento**.`
- `**Medio de Desplazamiento** puede estar \`tierra\`, \`aire\` o \`superficie acuática\`.`
- `**Auto**, **Aeronave** y **Barco** son **Vehículo**.`
- `**Auto** exhibe **Medio de Desplazamiento** en \`tierra\`.`
- `**Aeronave** exhibe **Medio de Desplazamiento** en \`aire\`.`
- `**Barco** exhibe **Medio de Desplazamiento** en \`superficie acuática\`.`

### Seguridad del hogar (proceso asincrónico)

`*Mantener Seguridad del Hogar*` consta de:

- *Atender Robo*;
- *Proteger contra Incendio*;
- *Alertar Terremoto*.

Como no se conoce el orden temporal, se usa despliegue por agregación-participación y no descomposición temporal.

### Preparación de café (estructura-comportamiento-función)

Estructura:

- `**Máquina de Café** consta de **Depósito de Agua**, **Espumador de Leche**, **Calentador de Agua**, **Compartimento de Cápsulas** y **Portataza**.`

Comportamiento:

- `*Preparar Café*` se descompone en *Calentar Agua*, *Espumar Leche*, *Extraer Café* y *Agregar Leche*.

Función:

- el beneficiario es **Persona que Bebe Café**;
- la función cambia **Satisfacción** de `insatisfecha` a `satisfecha`.

### Operación de auto eléctrico (componentes del SD)

Ejemplo de SD:

- propósito: mejorar **Éxito del Negocio** de **Grupo de Interesados de la Empresa**;
- función: `*Operar Auto Eléctrico*` cambia **Auto Eléctrico** de `detenido` a `en movimiento`;
- agente: **Conductor**;
- instrumento: **Sistema Operativo del Auto Eléctrico**;
- entorno: **Tipo de Terreno**, **Regulaciones**.

### Ejemplos sociales y sociotécnicos auxiliares

- **Control de Tráfico Aéreo:** **Piloto** y **Controlador Aéreo** son agentes; **Torre de Control** es instrumento.
- **Aprendizaje MOOC:** **Grupo de Estudiantes** actúa como agente; la plataforma MOOC como instrumento.
- **Gestión de Identidad Profesional en Línea:** el perfil en línea representa a la persona mediante enlace estructural etiquetado.
- **Transporte de Equipaje:** la función principal cambia la ubicación del equipaje del aeropuerto de origen al de destino.
- **Sistema de Conferencia:** **Organizador** y **Acomodadores** son agentes; instalaciones y equipamiento son instrumentos; el clima puede ser ambiental.

Los flujos de interfaz y los detalles específicos de herramienta que no alteren la semántica del modelo deben mantenerse en documentación operacional separada de este SSOT.

---

## Notas para implementadores de herramientas

Las siguientes notas informativas del estándar están dirigidas a quienes desarrollan herramientas compatibles con OPM:

- Una herramienta puede rastrear el conjunto de refinadores de cada refinable y ajustar automáticamente el símbolo gráfico y las oraciones OPL correspondientes cuando quien modela cambia la colección de refinadores.
- Una herramienta puede ofrecer la opción de especificar la esencia primaria del sistema como medio para establecer el valor por defecto del atributo genérico de esencia.
- Una herramienta puede notificar a quien modela cuando se intenta incluir un objeto como refinador en más de un contexto, para que determine la pertinencia de la inclusión.
- Una herramienta puede establecer una sintaxis por defecto para resolver nombres de refinadores ambiguos.
- El OPL correspondiente a un OPD debe expresar solo los estados de los objetos tal como aparecen en ese OPD; la unión de estados de un objeto a través de todos los OPDs constituye el conjunto completo de estados de ese objeto.
- Un enlace de evento desde un objeto o estado sistémico no debe cruzar el límite de un proceso descompuesto para iniciar un subproceso, porque interfiere con el orden temporal prescrito de la descomposición síncrona (véase «Distribución de enlaces a través del contexto»); la severidad con que la herramienta trata ese cruce no conforme la fija el canon prescriptivo operativo (`reglas-opm-estrictas-es`) y su familia. Si el evento proviene de un objeto ambiental, el cruce está permitido y la herramienta debería guiar a quien modela para definir cómo manejar la contingencia.
- Las herramientas de modelado OPM necesitan rastrear el número e identidades de las instancias operacionales de cada objeto y de cada proceso para poder realizar simulaciones.
