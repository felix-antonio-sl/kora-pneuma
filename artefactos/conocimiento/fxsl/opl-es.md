---
urn: urn:fxsl:kb:opl-es
nombre: opl-es
version: 3.0.1
estado: publicado
descripcion: "Gramática canónica del OPL en español: capa textual de la SSOT OPM-ES — léxico, plantillas de oraciones y localización es de la bimodalidad OPD↔OPL."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/opm/opm-ssot-es/opm-opl-es.md (sha256:c62ca64c310a65b19d1de7339720a20ca8943ed711f1aaaed4b92c486b9e34b1) el 2026-06-12; cuerpo byte-fiel (renombrado de opm-opl-es.md a opl-es.md por la regla lugar-coincide). Fuente original: Consolidacion SSOT OPM v3.0.0: capa textual canonica del corpus OPM-ES (gramatica OPL en espanol)."
autor: FS
creado: 2026-04-27
lang: es
tags: [opm, opl, spanish, es, grammar, i18n, bimodal, localization, v2, ampliada]
familia: bok
depende: [urn:fxsl:kb:opm-es]
cita: [urn:fxsl:kb:manual-metodologico-opm-es, urn:fxsl:kb:opd-es, urn:fxsl:kb:opm-es]
---


# OPL-ES — Lenguaje Objeto-Proceso en Español (v3.0.0)


Especificación completa de la gramática OPL en español, diseñada para que herramientas de modelado OPM generen y analicen sentencias OPL en español manteniendo equivalencia semántica total con la forma inglesa de referencia.

Esta versión integra los ajustes de la línea `merge-ready`: composición inter-modelo explícita, referencia externa de cosas, separación entre etiqueta visible de OPD e identidad persistente y ampliaciones mínimas de soporte de herramienta para modelos compuestos.

Es la **capa textual canónica** del corpus OPM-ES en KORA (v3.0.0). Reemplaza a la línea `ssot/` legacy, ya removida del repositorio.

Referencia de núcleo: `urn:fxsl:kb:opm-es`.

---

## 0. Alcance y contrato editorial

Este documento es la **capa textual canónica** del corpus OPM en español. Su responsabilidad es:

- fijar la superficie léxica y sintáctica de OPL-ES;
- definir plantillas textuales canónicas para los hechos del modelo;
- preservar equivalencia semántica de ida y vuelta entre OPL-EN y OPL-ES.

Este documento **no** define:

- la semántica base de OPM, que pertenece a [OPM — Núcleo conceptual](urn:fxsl:kb:opm-es);
- la gramática gráfica del OPD, que pertenece a [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es);
- el procedimiento de construcción, refinamiento y gobernanza del modelo, que pertenece a [Manual metodológico de OPM](urn:fxsl:kb:manual-metodologico-opm-es).

Regla editorial: cuando este documento menciona enlaces, refinamientos, cardinalidades u operadores, lo hace **solo** para fijar su realización textual canónica en español. La semántica del hecho y su geometría visual se heredan del corpus base.

---

## 1. Decisiones de Diseño

### 1.1 Denominación de Procesos

En OPL-EN los procesos usan gerundio (-ing): "Cooking", "Driving", "Data Processing". En OPL-ES los procesos pueden usar **infinitivo** (-ar, -er, -ir): "Cocinar", "Conducir", "Procesar Datos", o una **nominalización verbal** encabezada por una primera palabra terminada en `-ción`: "Ampliación", "Verificación de Datos".

El infinitivo español es el equivalente funcional más directo del gerundio sustantivado inglés: funciona como sustantivo sujeto ("Cocinar consume..."). Sin embargo, en español técnico también es plenamente válida una forma nominal encabezada por `-ción`, cuando el dominio prefiera un nombre de acción en vez de un infinitivo.

**Validación de nombre**: un nombre de proceso OPL-ES válido cumple al menos una de estas condiciones:

1. La primera palabra está en infinitivo y termina en `-ar`, `-er` o `-ir`
2. La primera palabra termina en `-ción`
3. En dominios que lo justifiquen, la primera palabra termina en `-miento`

Ejemplos válidos: "Procesar Datos", "Preparar Empanadas", "Ampliación de Cobertura", "Verificación de Identidad", "Mantenimiento Preventivo".

**Patrones de nombre de proceso** (paralelos a EN):

| Patrón EN | Ejemplo EN | Patrón ES | Ejemplo ES |
|-----------|-----------|-----------|-----------|
| verb-ing | Making | Infinitivo o nominalización | Hacer / Fabricación |
| noun verb-ing | Cake Making | Infinitivo sustantivo o nominalización con complemento | Preparar Torta / Preparación de Torta |
| adj verb-ing | Automatic Responding | Infinitivo + adverbio o nominalización | Responder Automáticamente / Respuesta Automática |
| adj noun verb-ing | Automatic Crash Responding | Infinitivo complejo o nominalización encabezada por `-ción` | Responder a Colisión Automáticamente / Atención Automática de Colisión |

Preferentemente entre 2 y 4 palabras. Se aceptan nombres más largos cuando el dominio lo exige y no introducen ambigüedad. Se capitalizan las palabras léxicas; artículos y preposiciones breves PUEDEN permanecer en minúscula cuando mejora la naturalidad del español.

### 1.2 Denominación de Objetos

Sin cambio respecto a OPL-EN: sustantivo singular, con capitalización en las palabras léxicas del nombre.

Plurales: sufijo "Conjunto" para inanimados (EN: "Set"), "Grupo" para humanos (EN: "Group").

Ejemplos: **Ingrediente**, **Conjunto de Ingredientes**, **Grupo de Comensales**, **Torta de Manzana**.

### 1.3 Denominación de Estados

Sin cambio respecto a OPL-EN: minúsculas, forma pasiva o descriptiva del objeto que los contiene.

Ejemplos: `pintado`, `inspeccionado`, `pre-cortado`, `vacío`, `cargado`, `satisfecho`.

### 1.4 Género Gramatical

Las plantillas usan masculino como género por defecto. El modelador ajusta al género natural del sustantivo en instancias concretas. El género afecta artículos y participios pero no la estructura de la sentencia.

Ejemplo: "es un **Sistema**" (masc.) → "es una **Máquina**" (fem.).

### 1.5 Ser vs Estar

- **estar** para estados de objetos (condición temporal, mutable): "**Objeto** está en `estado`"
- **ser** para propiedades invariantes (tipo, clasificación, esencia): "**Objeto** es de tipo X", "**X** es un **Y**"

Justificación: los estados OPM son situaciones temporales de un objeto (estar), mientras que tipo, clasificación y esencia son propiedades permanentes del modelo (ser). Esta distinción gramatical del español se alinea con la semántica OPM.

### 1.6 Artículos y Preposiciones

OPL-ES omite artículos en las sentencias, siguiendo la convención de OPL-EN, excepto donde la gramática española los requiere:

- "es un/una" en clasificación-instanciación y generalización-especialización individual
- "de lo contrario" en condiciones
- "al menos" en operadores lógicos y cardinalidades

Preposición "a" personal: omitida para objetos directos, ya que las entidades OPM son típicamente inanimadas. Ejemplo: "*Cocinar* consume **Masa**" (no "consume a Masa").

### 1.7 Convenciones Tipográficas (Markdown OPL)

| Entidad | Convención | Ejemplo |
|---------|-----------|---------|
| Objeto | **negrita** | **Ingrediente** |
| Proceso | *cursiva* | *Cocinar* |
| Estado | `monoespaciado` | `crudo` |

Estas convenciones aplican a la representación textual en Markdown. Los colores, contornos, sombreados y demás atributos del OPD pertenecen a la capa visual y no forman parte del contrato de OPL-ES.

### 1.8 Orden Canónico

OPL-ES preserva el orden sujeto-verbo-complemento de cada plantilla OPL-EN. No se reordena la oración. Esto garantiza correspondencia estructural estable entre ambas superficies y simplifica el análisis sintáctico bidireccional.

### 1.9 Con Estado Especificado: Posición del Estado

En OPL-EN el estado precede al objeto como modificador: "`specified-state` Object". En OPL-ES el estado sigue al objeto con la preposición "en": "**Objeto** en `estado`".

- EN: `active User handles Processing.`
- ES: **Usuario** en `activo` maneja *Procesar*.

### 1.10 Voz Pasiva

OPL-ES usa la pasiva refleja ("se consume", "se omite") en lugar de la pasiva perifrástica ("es consumido"), por naturalidad y concisión.

---

## 2. Vocabulario de Verbos OPL-ES

Verbos fijos de la gramática, conjugados en tercera persona singular del presente indicativo.

| Función | EN | ES | Infinitivo ES |
|---------|----|----|--------------|
| Consumo | consumes | consume | consumir |
| Resultado | yields | genera | generar |
| Efecto | affects | afecta | afectar |
| Cambio de estado | changes … from … to | cambia … de … a | cambiar |
| Agente | handles | maneja | manejar |
| Instrumento | requires | requiere | requerir |
| Iniciación | initiates | inicia | iniciar |
| Invocación | invokes | invoca | invocar |
| Ocurrencia | occurs | ocurre | ocurrir |
| Existencia | exists | existe | existir |
| Omisión (pasiva) | is skipped | se omite | omitir |
| Consumo (pasiva) | is consumed | se consume | consumir |
| Agregación | consists of | consta de | constar |
| Exhibición | exhibits | exhibe | exhibir |
| Especialización (pl.) | are | son | ser |
| Especialización (sg.) | is a | es un/una | ser |
| Instanciación | is an instance of | es una instancia de | ser |
| Relación | relates to | se relaciona con | relacionar |
| Variación de rango | ranges from … to | varía de … a | variar |
| Tipo | is of type | es de tipo | ser |
| Declaración de estados | can be | puede estar | poder + estar |
| Descomposición | zooms into … in that sequence | se descompone en … en esa secuencia | descomponerse |
| Despliegue | unfolds into | se despliega en | desplegarse |
| Refinamiento | is refined by in-zooming … in | se refina por descomposición de … en | refinarse |

### Palabras Clave Fijas

| EN | ES |
|----|----|
| if | si |
| in which case | en cuyo caso |
| otherwise / else | de lo contrario |
| from | de |
| to | a |
| and | y (e ante i-, hi-) |
| or | o (u ante o-, ho-) |
| as well as | así como |
| exactly one of | exactamente uno de |
| at least one of | al menos uno de |
| at least one other | al menos otro/a |
| an optional | un/una opcional |
| at least one | al menos un/una |
| following path | por ruta |
| duration of | duración de |
| exceeds | excede |
| falls short of | es menor que |
| in that sequence | en esa secuencia |
| can be | puede estar |
| is initial | es inicial |
| is final | es final |
| is default | es por defecto |
| is initial and final | es inicial y final |

---

## 3. Plantillas OPL-ES — Descripción de Entidades

### 3.1 Propiedades Genéricas

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| D1 | Thing is Physical. | **Cosa** es física. |
| D2 | Thing is Informatical. | **Cosa** es informacional. |
| D3 | Thing is Environmental. | **Cosa** es ambiental. |
| D4 | Thing is Systemic. | **Cosa** es sistémica. |
| D11 | Thing is Persistent. | **Cosa** es persistente. |
| D12 | Thing is Transient. | **Cosa** es transitoria. |

### 3.2 Enumeración de Estados

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| D5 | Object can be state1, state2, or state3. | **Objeto** puede estar `estado1`, `estado2` o `estado3`. |
| D6 | Object can be state1, …, and other states. | **Objeto** puede estar `estado1`, …, y otros estados. |

### 3.3 Designación de Estados

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| D7 | State s of Object is initial. | Estado `s` de **Objeto** es inicial. |
| D8 | State s of Object is final. | Estado `s` de **Objeto** es final. |
| D9 | State s of Object is default. | Estado `s` de **Objeto** es por defecto. |
| D10 | State s of Object is initial and final. | Estado `s` de **Objeto** es inicial y final. |
| D13 | State s of Object is declared current. | Estado `s` de **Objeto** es declarado `Current`. |

### 3.4 Nota sobre procesos persistentes

Esta adaptación reconoce procesos que mantienen un estado o condición sin introducir cambio neto observable relevante. Ejemplos: *Existir*, *Sostener*, *Mantener*, *Conservar*.

Para mantener cerrada la superficie canónica, OPL-ES adopta la siguiente convención textual:

- cuando el proceso persistente permanece explícito en el modelo, su realización canónica es una oración de cambio con **estado de entrada = estado de salida**, por ejemplo: `*Mantener Presión* cambia **Tanque** de \`presurizado\` a \`presurizado\`.` Esta forma preserva el hecho del modelo sin introducir verbos especiales fuera de la gramática base;
- cuando la temporalidad sostenida no es semánticamente central, el modelo PUEDE simplificarse editorialmente mediante un enlace estructural etiquetado, según la política metodológica de `metodologia-opm-es` §9.1.

No existe una familia verbal adicional exclusiva para procesos persistentes: la canonicidad se obtiene reutilizando la plantilla transformadora ya existente con estado de entrada y salida coincidentes.

---

## 4. Plantillas OPL-ES — Enlaces Transformadores

### 4.1 Básicos

| ID | Tipo | OPL-EN | OPL-ES |
|----|------|--------|--------|
| T1 | Consumo | Processing consumes Consumee. | *Procesar* consume **Consumido**. |
| T2 | Resultado | Processing yields Resultee. | *Procesar* genera **Resultado**. |
| T3 | Efecto | Processing affects Affectee. | *Procesar* afecta **Afectado**. |

### 4.2 Con Estado Especificado

| ID | Tipo | OPL-EN | OPL-ES |
|----|------|--------|--------|
| TS1 | Consumo s-s | Process consumes specified-state Object. | *Proceso* consume **Objeto** en `estado`. |
| TS2 | Resultado s-s | Process yields specified-state Object. | *Proceso* genera **Objeto** en `estado`. |
| TS3 | Efecto entrada-salida | Process changes Object from input-state to output-state. | *Proceso* cambia **Objeto** de `estado-entrada` a `estado-salida`. |
| TS4 | Efecto solo entrada (enlace de entrada) | Process changes Object from input-state. | *Proceso* cambia **Objeto** de `estado-entrada`. |
| TS5 | Efecto solo salida (enlace de salida) | Process changes Object to output-state. | *Proceso* cambia **Objeto** a `estado-salida`. |

Nota: TS4 y TS5 son la **realización textual del enlace escindido**. Cuando un efecto entrada-salida (TS3) se distribuye a una descomposición, se escinde en un TS4 temprano (subproceso que saca del estado de entrada) y un TS5 tardío (subproceso que pone en el estado de salida). La geometría visual de esta escisión se define en `opm-visual-es` V-40.

---

## 5. Plantillas OPL-ES — Enlaces Habilitadores

### 5.1 Básicos

| ID | Tipo | OPL-EN | OPL-ES |
|----|------|--------|--------|
| H1 | Agente | Agent handles Processing. | **Agente** maneja *Proceso*. |
| H2 | Instrumento | Processing requires Instrument. | *Proceso* requiere **Instrumento**. |

### 5.2 Con Estado Especificado

| ID | Tipo | OPL-EN | OPL-ES |
|----|------|--------|--------|
| HS1 | Agente s-s | Specified-state Agent handles Processing. | **Agente** en `estado` maneja *Proceso*. |
| HS2 | Instrumento s-s | Processing requires specified-state Instrument. | *Proceso* requiere **Instrumento** en `estado`. |

---

## 6. Plantillas OPL-ES — Enlaces de Evento

### 6.1 Eventos Transformadores

| ID | Tipo | OPL-EN | OPL-ES |
|----|------|--------|--------|
| ET1 | Consumo evento | Object initiates Process, which consumes Object. | **Objeto** inicia *Proceso*, que consume **Objeto**. |
| ET2 | Efecto evento | Object initiates Process, which affects Object. | **Objeto** inicia *Proceso*, que afecta **Objeto**. |

### 6.2 Eventos Habilitadores

| ID | Tipo | OPL-EN | OPL-ES |
|----|------|--------|--------|
| EH1 | Agente evento | Agent initiates and handles Process. | **Agente** inicia y maneja *Proceso*. |
| EH2 | Instrumento evento | Instrument initiates Process, which requires Instrument. | **Instrumento** inicia *Proceso*, que requiere **Instrumento**. |

### 6.3 Eventos Transformadores con Estado Especificado

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| ETS1 | Specified-state Object initiates Process, which consumes Object. | **Objeto** en `estado` inicia *Proceso*, que consume **Objeto**. |
| ETS2 | Input-state Object initiates Process, which changes Object from input-state to output-state. | **Objeto** en `estado-entrada` inicia *Proceso*, que cambia **Objeto** de `estado-entrada` a `estado-salida`. |
| ETS3 | Input-state Object initiates Process, which changes Object from input-state. | **Objeto** en `estado-entrada` inicia *Proceso*, que cambia **Objeto** de `estado-entrada`. |
| ETS4 | Object in any state initiates Process, which changes Object to destination-state. | **Objeto** en cualquier estado inicia *Proceso*, que cambia **Objeto** a `estado-destino`. |

### 6.4 Eventos Habilitadores con Estado Especificado

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| EHS1 | Specified-state Agent initiates and handles Processing. | **Agente** en `estado` inicia y maneja *Proceso*. |
| EHS2 | Specified-state Instrument initiates Processing, which requires specified-state Instrument. | **Instrumento** en `estado` inicia *Proceso*, que requiere **Instrumento** en `estado`. |

---

## 7. Plantillas OPL-ES — Enlaces de Condición

### 7.1 Condición Transformadores

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| CT1 | Process occurs if Object exists, in which case Object is consumed, otherwise Process is skipped. | *Proceso* ocurre si **Objeto** existe, en cuyo caso **Objeto** se consume, de lo contrario *Proceso* se omite. |
| CT2 | Process occurs if Object exists, in which case Process affects Object, otherwise Process is skipped. | *Proceso* ocurre si **Objeto** existe, en cuyo caso *Proceso* afecta **Objeto**, de lo contrario *Proceso* se omite. |

### 7.2 Condición Habilitadores

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| CH1 | Agent handles Process if Agent exists, else Process is skipped. | **Agente** maneja *Proceso* si **Agente** existe, de lo contrario *Proceso* se omite. |
| CH2 | Process occurs if Instrument exists, else Process is skipped. | *Proceso* ocurre si **Instrumento** existe, de lo contrario *Proceso* se omite. |

### 7.3 Condición con Estado Especificado

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| CS1 | Process occurs if Object is specified-state, in which case Object is consumed, otherwise Process is skipped. | *Proceso* ocurre si **Objeto** está en `estado`, en cuyo caso **Objeto** se consume, de lo contrario *Proceso* se omite. |
| CS2 | Process occurs if Object is input-state, in which case Process changes Object from input-state to output-state, otherwise Process is skipped. | *Proceso* ocurre si **Objeto** está en `estado-entrada`, en cuyo caso *Proceso* cambia **Objeto** de `estado-entrada` a `estado-salida`, de lo contrario *Proceso* se omite. |
| CS3 | Process occurs if Object is input-state, in which case Process changes Object from input-state, otherwise Process is skipped. | *Proceso* ocurre si **Objeto** está en `estado-entrada`, en cuyo caso *Proceso* cambia **Objeto** de `estado-entrada`, de lo contrario *Proceso* se omite. |
| CS4 | Process occurs if Object exists, in which case Process changes Object to output-state, otherwise Process is skipped. | *Proceso* ocurre si **Objeto** existe, en cuyo caso *Proceso* cambia **Objeto** a `estado-salida`, de lo contrario *Proceso* se omite. |
| CS5 | Agent handles Process if Agent is specified-state, else Process is skipped. | **Agente** maneja *Proceso* si **Agente** está en `estado`, de lo contrario *Proceso* se omite. |
| CS6 | Process occurs if Instrument is specified-state, otherwise Process is skipped. | *Proceso* ocurre si **Instrumento** está en `estado`, de lo contrario *Proceso* se omite. |

---

## 8. Plantillas OPL-ES — Excepción e Invocación

### 8.1 Enlaces de Excepción

| ID | Tipo | OPL-EN | OPL-ES |
|----|------|--------|--------|
| EX1 | Overtime | Handling occurs if duration of Source exceeds max-duration time-units. | *Manejo* ocurre si duración de *Fuente* excede máx-duración unidades-tiempo. |
| EX2 | Undertime | Handling occurs if duration of Source falls short of min-duration time-units. | *Manejo* ocurre si duración de *Fuente* es menor que mín-duración unidades-tiempo. |

### 8.2 Enlaces de Invocación

| ID | Tipo | OPL-EN | OPL-ES |
|----|------|--------|--------|
| IV1 | Invocación | Invoking invokes Invoked. | *Invocador* invoca *Invocado*. |
| IV2 | Auto-invocación | Invoking invokes itself. | *Invocador* se invoca a sí mismo. |

---

## 9. Plantillas OPL-ES — Enlaces Estructurales

### 9.1 Etiquetados

| ID | Tipo | OPL-EN | OPL-ES |
|----|------|--------|--------|
| SE1 | Unidireccional etiquetado | Source tag Destination. | **Origen** etiqueta **Destino**. |
| SE2 | Unidireccional sin etiqueta | Source relates to Destination. | **Origen** se relaciona con **Destino**. |
| SE3 | Bidireccional etiquetado | Source f-tag Dest. / Dest b-tag Source. | **Origen** etiqueta-f **Destino**. / **Destino** etiqueta-b **Origen**. |
| SE4 | Recíproco etiquetado | Source and Destination are tag. | **Origen** y **Destino** son etiqueta. |
| SE5 | Recíproco sin etiqueta | Source and Destination are related. | **Origen** y **Destino** se relacionan. |

Nota: en SE1, SE3 y SE4, "etiqueta" es la forma definida por el modelador en español (ej. "emplea", "pertenece a", "supervisa"). La etiqueta actúa como verbo o predicado nominal de la oración.

### 9.2 Relaciones Estructurales Fundamentales

| ID | Relación | OPL-EN | OPL-ES |
|----|----------|--------|--------|
| RF1 | Agregación-participación | Whole consists of Part1, Part2 and Part3. | **Todo** consta de **Parte1**, **Parte2** y **Parte3**. |
| RF2 | Exhibición-caracterización (solo atributos) | Exhibitor exhibits Attribute1 and Attribute2. | **Exhibidor** exhibe **Atributo1** y **Atributo2**. |
| RF2b | Exhibición-caracterización (atributos + operaciones) | Exhibitor exhibits Attribute1 as well as Operation1. | **Exhibidor** exhibe **Atributo1** así como *Operación1*. |
| RF3 | Generalización-especialización (compuesto) | Specialization1 and Specialization2 are General. | **Especialización1** y **Especialización2** son **General**. |
| RF3b | Generalización-especialización (individual) | Specialization is a General. | **Especialización** es un **General**. |
| RF4 | Clasificación-instanciación | Instance is an instance of Class. | **Instancia** es una instancia de **Clase**. |

### 9.3 Colecciones Incompletas

| OPL-EN | OPL-ES |
|--------|--------|
| …and at least one other part. | …y al menos otra parte. |
| …and at least one other feature. | …y al menos otro rasgo. |
| …and at least one other specialization. | …y al menos otra especialización. |

### 9.4 Estructurales con Estado Especificado

| ID | Grupo | OPL-EN | OPL-ES |
|----|-------|--------|--------|
| SSE1 | Estado en origen (uni) | Specified-state Source tag Destination. | **Origen** en `estado` etiqueta **Destino**. |
| SSE2 | Estado en destino (uni) | Source tag specified-state Destination. | **Origen** etiqueta **Destino** en `estado`. |
| SSE3 | Estado en ambos (uni) | Sa Source tag Sb Destination. | **Origen** en `sa` etiqueta **Destino** en `sb`. |
| SSE4 | Estado en origen (bidi, f-tag) | Sa Source f-tag Destination. | **Origen** en `sa` etiqueta-f **Destino**. |
| SSE5 | Estado en origen (bidi, b-tag) | Destination b-tag Sa Source. | **Destino** etiqueta-b **Origen** en `sa`. |
| SSE6 | Estado en ambos (recíproco) | Sa Source and Sb Dest are tag. | **Origen** en `sa` y **Destino** en `sb` son etiqueta. |
| SSE7 | Estado en origen (recíproco) | Dest and Sa Source are tag. | **Destino** y **Origen** en `sa` son etiqueta. |

---

## 10. Plantillas OPL-ES — Gestión de Contexto

### 10.1 Descomposición (In-Zooming)

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| CX1 | Process zooms into P1, P2 and P3, in that sequence. | *Proceso* se descompone en *P1*, *P2* y *P3*, en esa secuencia. |
| CX2 | Process zooms into parallel P1 and P2. | *Proceso* se descompone en paralelo *P1* y *P2*. |

### 10.2 Despliegue (Unfolding)

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| CX3 | Thing unfolds in SD1 into T1, T2 and T3. | **Cosa** se despliega en SD1 en **T1**, **T2** y **T3**. |

### 10.3 Refinamiento entre OPDs

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| CX4 | SD is refined by in-zooming Process in SD1. | SD se refina por descomposición de *Proceso* en SD1. |

Las etiquetas visibles de OPD (`SD`, `SD1`, `SD1.1`, etc.) son referencias humanas de navegación. No constituyen por sí mismas la identidad persistente del OPD. Toda oración de refinamiento entre OPDs debe mapearse a un identificador persistente recuperable en la serialización del modelo, por ejemplo un URI o handle persistente declarado por la implementación.

### 10.4 Composición inter-modelo

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| CM1 | SD1.1 is a sub-model view of Subsystem Model. | SD1.1 es una vista de sub-modelo de Modelo Subsistema. |
| CM2 | SD1.1 references sub-model Subsystem Model from SD1. | SD1.1 referencia el sub-modelo Modelo Subsistema desde SD1. |
| CM3 | Thing in SD1.1 is an external reference to Thing of owner model Main Model. | **Cosa** en SD1.1 es referencia externa a **Cosa** del modelo propietario Modelo Principal. |

Estas oraciones no reemplazan la gramática del hecho interno del modelo. Describen la composición entre modelos y la referencia externa de elementos a través de fronteras de modelo.

### 10.5 Plegado y Recomposición

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| CX5 | Process folds into parent OPD. | *Proceso* se pliega en el OPD padre. |
| CX6 | Object folds into parent OPD. | **Objeto** se pliega en el OPD padre. |
| CX7 | Process recomposes from diagram. | *Proceso* se recompone desde `diagrama`. |
| CX8 | Object recomposes from diagram. | **Objeto** se recompone desde `diagrama`. |

---

## 11. Operadores Lógicos

### 11.1 AND

AND se expresa implícitamente mediante sentencias OPL separadas para cada enlace. No hay operador explícito — cada enlace genera su propia oración. Gráficamente: enlaces separados (no se tocan) en el contorno del proceso.

Ejemplo AND de agentes:

- EN: `Safe Owner A handles Safe Opening.` / `Safe Owner B handles Safe Opening.`
- ES: **Dueño de Caja Fuerte A** maneja *Abrir Caja Fuerte*. / **Dueño de Caja Fuerte B** maneja *Abrir Caja Fuerte*.

### 11.2 XOR

Gráficamente: arco discontinuo simple. EN: "exactly one of". ES: "exactamente uno de".

| Familia | OPL-EN | OPL-ES |
|---------|--------|--------|
| Consumo conv. | P consumes exactly one of A, B, or C. | *P* consume exactamente uno de **A**, **B** o **C**. |
| Consumo div. | Exactly one of P, Q, or R consumes B. | Exactamente uno de *P*, *Q* o *R* consume **B**. |
| Resultado conv. | Exactly one of P, Q, or R yields B. | Exactamente uno de *P*, *Q* o *R* genera **B**. |
| Resultado div. | P yields exactly one of A, B, or C. | *P* genera exactamente uno de **A**, **B** o **C**. |
| Efecto (objetos) | P affects exactly one of A, B, or C. | *P* afecta exactamente uno de **A**, **B** o **C**. |
| Efecto (procesos) | B is affected by exactly one of P, Q, or R. | **B** es afectado por exactamente uno de *P*, *Q* o *R*. |
| Agente | B handles exactly one of P, Q, or R. | **B** maneja exactamente uno de *P*, *Q* o *R*. |
| Instrumento | Exactly one of P, Q, or R requires B. | Exactamente uno de *P*, *Q* o *R* requiere **B**. |
| Invocación div. | P invokes exactly one of Q or R. | *P* invoca exactamente uno de *Q* o *R*. |
| Invocación conv. | Exactly one of P or Q invokes R. | Exactamente uno de *P* o *Q* invoca *R*. |

### 11.3 OR

Misma estructura que XOR, reemplazando:

- EN: "exactly one of" → "at least one of"
- ES: "exactamente uno de" → "al menos uno de"

Gráficamente: arco doble (dos arcos concéntricos discontinuos).

### 11.4 XOR/OR con Modificadores de Control

Los abanicos XOR y OR se combinan con modificadores evento ("e") y condición ("c"). Regla de composición:

**Evento + XOR** — insertar "inicia" antes del verbo principal:

- EN: `B initiates exactly one of P, Q, or R, and is affected by the occurring process.`
- ES: **B** inicia exactamente uno de *P*, *Q* o *R*, y es afectado por el proceso que ocurre.

**Condición + XOR** — insertar "si … existe/está en estado … de lo contrario … se omite":

- EN: `Exactly one of P, Q, R occurs if B exists, in which case it affects B, otherwise skipped.`
- ES: Exactamente uno de *P*, *Q* o *R* ocurre si **B** existe, en cuyo caso afecta **B**, de lo contrario se omite.

Reemplazar "exactamente" por "al menos" para obtener la variante OR.

### 11.5 Probabilístico

Anotación `Pr=p` en cada enlace del abanico. Suma de probabilidades = 1. Notación numérica universal, sin cambio entre EN y ES.

---

## 12. Cardinalidad y Multiplicidad

| Símbolo | Rango | OPL-EN | OPL-ES |
|---------|-------|--------|--------|
| ? | 0..1 | an optional | un/una opcional |
| * | 0..* | optional (none to many) | opcional (cero o más) |
| (ninguno) | 1..1 | (default) | (por defecto) |
| + | 1..* | at least one | al menos un/una |

Rango parametrizado base: `qmín..qmáx`. Cuando el rango se emite como estado o como valor visible del atributo, esta adaptación admite intervalos con delimitadores de inclusión y exclusión: `[qmín..qmáx]`, `(qmín..qmáx]`, `[qmín..qmáx)` y `(qmín..qmáx)`, además de listas de intervalos separadas por comas y `*` como extremo abierto. Restricciones con =, ≠, <, ≤, ≥, ∈. Sin cambio sintáctico entre EN y ES (notación matemática universal).

**Ejemplo de multiplicidad parametrizada**:

- EN: `Jet Engine consists of b Installed Blades.`
- ES: **Motor a Reacción** consta de b **Paletas Instaladas**.

### 12.1 Tipo

| OPL-EN | OPL-ES |
|--------|--------|
| Object is of type type-id. | **Objeto** es de tipo tipo-id. |

Tipos: boolean, string, integer, float, double, short, long, enumerated. Sin traducción (identificadores de tipo universales).

Producción formal: véase Apéndice A.4 (`oracion_de_tipo_de_dato`).

---

## 13. Etiquetas de Ruta

| OPL-EN | OPL-ES |
|--------|--------|
| Following path label, Process consumes Object. | Por ruta etiqueta, *Proceso* consume **Objeto**. |
| Following path label, Process yields Object. | Por ruta etiqueta, *Proceso* genera **Objeto**. |

"Por ruta" es la expresión fija. "etiqueta" es el nombre de la ruta definido por el modelador.

**Ejemplo (Preparar Alimento)**:

- EN: `Following path carnivore, Food Preparing consumes Meat, yields Stew and Steak.`
- ES: Por ruta carnívoro, *Preparar Alimento* consume **Carne**, genera **Estofado** y **Bistec**.

- EN: `Following path herbivore, Food Preparing consumes Cucumber and Tomato, yields Salad.`
- ES: Por ruta herbívoro, *Preparar Alimento* consume **Pepino** y **Tomate**, genera **Ensalada**.

---

## 14. Atributos y Valores

| OPL-EN | OPL-ES |
|--------|--------|
| Attribute of Object is value. | **Atributo** de **Objeto** es valor. |
| Attribute of Object ranges from X to Y. | **Atributo** de **Objeto** varía de X a Y. |
| Attribute of Object can be value1, value2, or value3. | **Atributo** de **Objeto** puede estar `valor1`, `valor2` o `valor3`. |

**Ejemplo**:

- EN: `Cleanliness of Dish Set can be dirty or clean.`
- ES: **Limpieza** de **Conjunto de Platos** puede estar `sucia` o `limpia`.

- EN: `State dirty of Cleanliness of Dish Set is initial.`
- ES: Estado `sucia` de **Limpieza** de **Conjunto de Platos** es inicial.

---

## 15. Reglas de Transformación Sistemática EN → ES

Para implementadores de herramientas. Reglas aplicadas en secuencia sobre una sentencia OPL-EN para producir OPL-ES:

| # | Regla | EN | ES |
|---|-------|----|----|
| R1 | Verbo principal | consumes, yields, affects, handles, requires, initiates, invokes, occurs, exists | consume, genera, afecta, maneja, requiere, inicia, invoca, ocurre, existe |
| R2 | State-specified: posición | `state Object` (estado antes del objeto) | **Objeto** en `estado` (estado después del objeto con "en") |
| R3 | Estado condicional | Object is state | **Objeto** está en `estado` |
| R4 | Declaración de estados | can be | puede estar |
| R5 | Conjunción copulativa | and | y (e ante i-/hi-) |
| R6 | Conjunción disyuntiva | or | o (u ante o-/ho-) |
| R7 | Preposición de origen | from | de |
| R8 | Preposición de destino | to | a |
| R9 | Preposición posesiva | of | de |
| R10 | Cuantificador XOR | exactly one of | exactamente uno de |
| R11 | Cuantificador OR | at least one of | al menos uno de |
| R12 | Condicional | if … exists | si … existe |
| R13 | Consecuencia | in which case | en cuyo caso |
| R14 | Alternativa | otherwise / else | de lo contrario |
| R15 | Pasiva refleja | is consumed / is skipped | se consume / se omite |
| R16 | Ruta | Following path | Por ruta |
| R17 | Artículo en instanciación | is an instance of | es una instancia de |
| R18 | Artículo en especialización (sg.) | is a | es un/una |
| R19 | Secuencia | in that sequence | en esa secuencia |
| R20 | Designación de estado | is initial / is final / is default / is declared current | es inicial / es final / es por defecto / es declarado `Current` |
| R21 | Nombres de entidad | (sin cambio — definidos por el modelador) | (sin cambio) |

**Nota para analizadores**: el verbo principal (R1) es el ancla léxica para detectar el idioma de la sentencia. Un analizador puede determinar EN vs ES verificando si el primer verbo conjugado pertenece al conjunto EN o ES.

---

## 16. Ejemplo Completo: Sistema de Preparación de Empanadas

### Contexto

Sistema doméstico de preparación de empanadas de pino (tradicionales chilenas). Modela el SD completo con los 5 componentes de un sistema artificial.

### Componentes del SD

| Componente | Elemento |
|-----------|---------|
| 1. Propósito | Cambiar **Nivel de Satisfacción** de **Grupo de Comensales** de `insatisfecho` a `satisfecho` |
| 2. Función principal | *Preparar Empanadas* (proceso principal) + **Grupo de Comensales** (operando) |
| 3. Habilitadores | **Cocinero** (agente), **Sistema de Preparación de Empanadas** (instrumento principal), **Horno**, **Utensilios de Cocina** (instrumentos) |
| 4. Entorno | **Receta** (informacional, ambiental) |
| 5. Ocurrencia del problema | *Cocinar sin Sistema* (proceso ambiental) causa estado `insatisfecho` |

### Tabla de Elementos

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Preparar Empanadas* | Físico | Sistémico | — |
| Objeto | **Grupo de Comensales** | Físico | Sistémico | — |
| Objeto | **Nivel de Satisfacción** | Informacional | Sistémico | `insatisfecho`, `satisfecho` |
| Objeto | **Cocinero** | Físico | Sistémico | — |
| Objeto | **Sistema de Prep. de Empanadas** | Físico | Sistémico | — |
| Objeto | **Horno** | Físico | Sistémico | — |
| Objeto | **Utensilios de Cocina** | Físico | Sistémico | — |
| Objeto | **Masa Cruda** | Físico | Sistémico | — |
| Objeto | **Relleno de Pino** | Físico | Sistémico | — |
| Objeto | **Empanada** | Físico | Sistémico | — |
| Objeto | **Receta** | Informacional | Ambiental | — |

### Tabla de Enlaces

| Tipo | Origen | Destino | ID |
|------|--------|---------|-----|
| Efecto (entrada-salida) | *Preparar Empanadas* | **Nivel de Satisfacción** | TS3 |
| Exhibición-caracterización | **Grupo de Comensales** | **Nivel de Satisfacción** | RF2 |
| Agente | **Cocinero** | *Preparar Empanadas* | H1 |
| Instrumento | **Sistema de Prep. de Empanadas** | *Preparar Empanadas* | H2 |
| Instrumento | **Horno** | *Preparar Empanadas* | H2 |
| Instrumento | **Utensilios de Cocina** | *Preparar Empanadas* | H2 |
| Consumo | **Masa Cruda** | *Preparar Empanadas* | T1 |
| Consumo | **Relleno de Pino** | *Preparar Empanadas* | T1 |
| Resultado | *Preparar Empanadas* | **Empanada** | T2 |
| Etiquetado (nulo) | **Receta** | *Preparar Empanadas* | SE2 |

### OPL-ES del SD

```
*Preparar Empanadas* afecta **Grupo de Comensales**.
**Grupo de Comensales** exhibe **Nivel de Satisfacción**.
**Nivel de Satisfacción** puede estar `insatisfecho` o `satisfecho`.
Estado `insatisfecho` de **Nivel de Satisfacción** es inicial.
Estado `satisfecho` de **Nivel de Satisfacción** es final.
*Preparar Empanadas* cambia **Nivel de Satisfacción** de `insatisfecho` a `satisfecho`.
**Cocinero** maneja *Preparar Empanadas*.
*Preparar Empanadas* requiere **Sistema de Preparación de Empanadas**.
*Preparar Empanadas* requiere **Horno**.
*Preparar Empanadas* requiere **Utensilios de Cocina**.
*Preparar Empanadas* consume **Masa Cruda**.
*Preparar Empanadas* consume **Relleno de Pino**.
*Preparar Empanadas* genera **Empanada**.
**Receta** es ambiental.
**Receta** se relaciona con *Preparar Empanadas*.
```

### OPL-EN Equivalente

```
Preparing Empanadas affects Diner Group.
Diner Group exhibits Satisfaction Level.
Satisfaction Level can be unsatisfied or satisfied.
State unsatisfied of Satisfaction Level is initial.
State satisfied of Satisfaction Level is final.
Preparing Empanadas changes Satisfaction Level from unsatisfied to satisfied.
Cook handles Preparing Empanadas.
Preparing Empanadas requires Empanada Preparation System.
Preparing Empanadas requires Oven.
Preparing Empanadas requires Kitchen Utensils.
Preparing Empanadas consumes Raw Dough.
Preparing Empanadas consumes Pino Filling.
Preparing Empanadas yields Empanada.
Recipe is Environmental.
Recipe relates to Preparing Empanadas.
```

### SD1: Descomposición de Preparar Empanadas

```
SD se refina por descomposición de *Preparar Empanadas* en SD1.
*Preparar Empanadas* se descompone en *Preparar Masa*, *Preparar Relleno*,
 *Armar Empanadas* y *Hornear Empanadas*, en esa secuencia.
*Preparar Masa* consume **Masa Cruda**.
*Preparar Masa* genera **Masa Estirada**.
*Preparar Relleno* consume **Relleno de Pino**.
*Preparar Relleno* genera **Relleno Cocido**.
*Armar Empanadas* consume **Masa Estirada**.
*Armar Empanadas* consume **Relleno Cocido**.
*Armar Empanadas* genera **Empanada** en `cruda`.
**Horno** puede estar `frío` o `precalentado`.
*Hornear Empanadas* requiere **Horno** en `precalentado`.
*Hornear Empanadas* cambia **Empanada** de `cruda` a `horneada`.
```

---

## 17. Adaptaciones de la EBNF al español

La EBNF de esta capa textual define la superficie canónica de OPL en español. Frente a la formulación inglesa de referencia, requiere las siguientes adaptaciones.

Esta sección es **explicativa**: describe cómo se obtienen las producciones ES partiendo de las EN de referencia, usando nombres de no-terminales con espacios por legibilidad (por ejemplo `identificador de proceso`). La forma **normativa** y mecanizable vive en el Apéndice A, donde los no-terminales se escriben en snake_case (por ejemplo `identificador_de_proceso`). Cuando exista cualquier divergencia entre §17 y Apéndice A, prevalece el Apéndice.

### 17.1 Terminales Léxicos

Sustituir cada terminal reservado EN por su equivalente ES según la tabla de la sección 2.

### 17.2 Identificadores

```ebnf
(* EN *)
process identifier = singular process name | singular process name, " process" ;
(* ES *)
identificador de proceso = nombre singular de proceso | nombre singular de proceso, " proceso" ;
```

Nombre de proceso EN: frase en gerundio capitalizada (-ing). Nombre de proceso ES: frase capitalizada encabezada por infinitivo (`-ar`, `-er`, `-ir`) o por nominalización en `-ción`; `-miento` también se acepta cuando el dominio lo requiere.

```ebnf
(* EN *)
state identifier = non capitalized word ;
(* ES — sin cambio *)
identificador de estado = palabra no capitalizada ;
```

### 17.3 Participación

```ebnf
(* EN *)
lower single = "a" | "an" | "an optional" | "at least one" ;
(* ES *)
singular inferior = "un" | "una" | "un opcional" | "una opcional" | "al menos un" | "al menos una" ;
```

### 17.4 Sentencias de Cambio de Estado

```ebnf
(* EN *)
in out object change phrase = object identifier, " from ", input state, " to ", output state ;
(* ES *)
frase de cambio entrada-salida = identificador de objeto, " de ", estado entrada, " a ", estado salida ;
```

### 17.5 Estructura de Producción

Las reglas de producción de alto nivel no cambian. En OPL-ES se sustituyen los terminales léxicos y se introducen alias de no terminales auxiliares para mantener claridad en español. El criterio normativo es que la gramática quede cerrada y semánticamente equivalente, no que replique literalmente todos los identificadores internos del anexo inglés.

---

## Apéndice A.0 — Gramática formal OPL-ES completa: alcance del apéndice

Este apéndice reúne la EBNF completa de OPL-ES. Se traslada aquí desde la capa base para eliminar solapamiento editorial: la semántica del hecho sigue perteneciendo a `opm-es`, pero la definición formal de su superficie textual canónica pertenece a OPL-ES. Todos los no-terminales del apéndice se escriben en snake_case; cualquier forma con espacios que aparezca en §17 es explicativa y no normativa.

## A.1 Estructura del documento

```ebnf
parrafo_opl_es = oracion_opl_es, { salto_de_linea, oracion_opl_es } ;
oracion_opl_es = oracion_formal_opl_es, "." ;
oracion_formal_opl_es = oracion_de_descripcion_de_cosa
 | oracion_procedimental
 | oracion_estructural
 | oracion_de_gestion_de_contexto ;
```

## A.2 Declaraciones base

```ebnf
digito_no_cero = '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' ;
digito_decimal = '0' | digito_no_cero ;
entero_positivo = digito_no_cero, {digito_decimal} ;
nombre_simple = letra, {caracter_de_cadena} ;
nombre = nombre_simple, { " ", nombre_simple } ;
segmento_etiqueta_opd = "SD", [entero_positivo] ;
palabra_capitalizada = letra_mayuscula, {caracter_de_cadena} ;
palabra_no_capitalizada = letra_minuscula, {caracter_de_cadena} ;
frase_no_capitalizada = palabra_no_capitalizada, { " ", palabra_no_capitalizada } ;
letra = letra_mayuscula | letra_minuscula ;
letra_mayuscula = 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z'
 | 'Á' | 'É' | 'Í' | 'Ó' | 'Ú' | 'Ñ' | 'Ü' ;
letra_minuscula = 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z'
 | 'á' | 'é' | 'í' | 'ó' | 'ú' | 'ñ' | 'ü' ;
(* OPL-ES amplía el alfabeto básico para cubrir caracteres propios del español:
 vocales acentuadas, eñe y diéresis. *)
caracter_de_cadena = letra | digito_decimal | '-' | '_' ;
identificador_de_tipo = "boolean" | "string" | tipo_numerico | "enumerated" ;
tipo_numerico = [prefijo], "integer" | "float" | "double" | "short" | "long" ;
restriccion_de_participacion = singular_inferior | singular_superior | plural_inferior | plural_superior
 | ( "0" | limite_de_participacion, [ " a ", limite_de_participacion ] ) ;
singular_inferior = "un" | "una" | "un opcional" | "una opcional" | "al menos un" | "al menos una" ;
singular_superior = "exactamente un" | "exactamente una" ;
plural_inferior = "al menos dos" ;
plural_superior = "dos o más" ;
limite_de_participacion = entero_positivo | nombre_simple ;
prefijo = "unsigned " | "signed " ;
unidad_de_medida = nombre_simple ;
numero_decimal = [ "-" ], ( "0" | entero_positivo ), [ ".", digito_decimal, {digito_decimal} ] ;
nombre_de_valor = nombre_simple | numero_decimal ;
limite_de_rango = nombre_de_valor | "*" ;
delimitador_inferior_de_rango = "[" | "(" ;
delimitador_superior_de_rango = "]" | ")" ;
intervalo_de_rango = delimitador_inferior_de_rango, limite_de_rango, "..", limite_de_rango, delimitador_superior_de_rango ;
expresion_de_rango = intervalo_de_rango, { ", ", intervalo_de_rango } ;
clausula_de_rango = " es ", ( nombre_de_valor | expresion_de_rango )
 | " varía de ", nombre_de_valor, " a ", nombre_de_valor ;
```

## A.3 Identificadores

```ebnf
identificador_de_objeto = nombre_singular_de_objeto, [ " en ", unidad_de_medida ], [ clausula_de_rango ] ;
identificador_de_proceso = nombre_singular_de_proceso | nombre_singular_de_proceso, " proceso" ;
identificador_de_cosa = identificador_de_objeto | identificador_de_proceso ;
identificador_de_estado = palabra_no_capitalizada ;
expresion_de_etiqueta = frase_no_capitalizada ;
nombre_singular_de_objeto = palabra_capitalizada, { " ", palabra_capitalizada | palabra_no_capitalizada } ;
nombre_singular_de_proceso = palabra_capitalizada, { " ", palabra_capitalizada | palabra_no_capitalizada } ;
estado_de_entrada = identificador_de_estado ;
estado_de_salida = identificador_de_estado ;
objeto_con_opcion_de_estado = identificador_de_objeto, [ " en ", identificador_de_estado ] ;
objeto_con_opcion = identificador_de_objeto ;
proceso_con_opcion = identificador_de_proceso ;
objeto_origen = identificador_de_objeto ;
objeto_destino = identificador_de_objeto ;
proceso_origen = identificador_de_proceso ;
proceso_destino = identificador_de_proceso ;
objeto_todo = identificador_de_objeto ;
proceso_todo = identificador_de_proceso ;
objeto_general = identificador_de_objeto ;
proceso_general = identificador_de_proceso ;
clase_de_objeto = identificador_de_objeto ;
clase_de_proceso = identificador_de_proceso ;
objeto_especial = identificador_de_objeto ;
objeto_con_estado = identificador_de_objeto, " en ", identificador_de_estado ;
nombre_de_modelo = nombre ;
etiqueta_visible_de_opd = segmento_etiqueta_opd, { ".", entero_positivo } ;
opd_padre = etiqueta_visible_de_opd ;
opd_hijo = etiqueta_visible_de_opd ;
identificador_de_proceso_activo = identificador_de_proceso ;
max_duracion_unidades_tiempo = nombre_de_valor, " unidades-tiempo" ;
min_duracion_unidades_tiempo = nombre_de_valor, " unidades-tiempo" ;
lista_de_estados = identificador_de_estado, { ", ", identificador_de_estado }, [ " o ", identificador_de_estado ] ;
lista_de_objetos = identificador_de_objeto, { ", ", identificador_de_objeto }, [ " y ", identificador_de_objeto ] ;
lista_de_procesos = identificador_de_proceso, { ", ", identificador_de_proceso }, [ " y ", identificador_de_proceso ] ;
lista_de_atributos = identificador_de_objeto, { ", ", identificador_de_objeto }, [ " y ", identificador_de_objeto ] ;
lista_de_operadores = identificador_de_proceso, { ", ", identificador_de_proceso }, [ " y ", identificador_de_proceso ] ;
lista_de_objetos_especiales = lista_de_objetos ;
lista_de_procesos_especiales = lista_de_procesos ;
lista_de_objetos_instancia = lista_de_objetos ;
lista_de_procesos_instancia = lista_de_procesos ;
lista_de_objetos_con_estado = objeto_con_estado, { ", ", objeto_con_estado }, [ " y ", objeto_con_estado ] ;
etiqueta_directa = expresion_de_etiqueta ;
etiqueta_nula_definida_por_usuario = expresion_de_etiqueta ;

(* La identidad persistente del OPD no forma parte de la superficie oracional.
   Debe preservarse en el metadato asociado a la serialización. *)
```

Convenciones:

- nombres de objeto: sintagmas nominales en singular, con mayúscula en palabras léxicas;
- nombres de proceso: infinitivo o nominalización técnica canónica del dominio;
- nombres de estado: en minúscula;
- etiquetas: frases breves en minúscula.

## A.4 Oraciones de descripción de cosas

```ebnf
oracion_de_descripcion_de_cosa = oracion_de_propiedad_generica
 | oracion_de_enumeracion_de_estados
 | oracion_de_estados_iniciales
 | oracion_de_estados_finales
 | oracion_de_estado_por_defecto
 | oracion_de_estado_current
 | oracion_de_tipo_de_dato ;

oracion_de_tipo_de_dato =
 identificador_de_objeto, " es de tipo ", identificador_de_tipo ;

oracion_de_propiedad_generica = identificador_de_cosa, " es ", ( esencia | afiliacion | perseverancia ) ;
oracion_de_enumeracion_de_estados = identificador_de_objeto, " puede estar ", lista_de_estados, [", y otros estados"] ;
oracion_de_estados_iniciales = "Estado ", identificador_de_estado, " de ", identificador_de_objeto, " es inicial" ;
oracion_de_estados_finales = "Estado ", identificador_de_estado, " de ", identificador_de_objeto, " es final" ;
oracion_de_estado_por_defecto = "Estado ", identificador_de_estado, " de ", identificador_de_objeto, " es por defecto" ;
oracion_de_estado_current = "Estado ", identificador_de_estado, " de ", identificador_de_objeto, " es declarado `Current`" ;
esencia = "física" | "informacional" ;
afiliacion = "ambiental" | "sistémica" ;
perseverancia = "persistente" | "transitoria" ;
```

Esencia: `física` o `informacional`. Afiliación: `sistémica` o `ambiental`. Perseverancia: `persistente` o `transitoria`. (La glosa mantiene los valores en minúscula tal como los emiten las plantillas D1–D4, D11, D12; los backticks marcan que se trata de tokens canónicos del lenguaje, no de glosas en lenguaje natural.)

## A.5 Oraciones procedimentales

```ebnf
oracion_procedimental = oracion_transformadora | oracion_habilitadora | oracion_de_invocacion | oracion_de_control ;
oracion_transformadora = oracion_de_consumo | oracion_de_resultado | oracion_de_efecto | oracion_de_cambio ;

oracion_de_consumo = identificador_de_proceso, " consume ", objeto_con_opcion_de_estado ;
oracion_de_resultado = identificador_de_proceso, " genera ", objeto_con_opcion_de_estado ;
oracion_de_efecto = identificador_de_proceso, " afecta ", lista_de_objetos ;
oracion_de_cambio = oracion_de_cambio_entrada_salida | oracion_de_cambio_solo_entrada
 | oracion_de_cambio_solo_salida ;

frase_de_cambio_entrada_salida = identificador_de_objeto, " de ", estado_de_entrada, " a ", estado_de_salida ;
frase_de_cambio_solo_entrada = identificador_de_objeto, " de ", estado_de_entrada ;
frase_de_cambio_solo_salida = identificador_de_objeto, " a ", estado_de_salida ;
oracion_de_cambio_entrada_salida = identificador_de_proceso, " cambia ", frase_de_cambio_entrada_salida ;
oracion_de_cambio_solo_entrada = identificador_de_proceso, " cambia ", frase_de_cambio_solo_entrada ;
oracion_de_cambio_solo_salida = identificador_de_proceso, " cambia ", frase_de_cambio_solo_salida ;

oracion_habilitadora = oracion_de_agente | oracion_de_instrumento ;
oracion_de_agente = objeto_con_opcion_de_estado, " maneja ", identificador_de_proceso ;
oracion_de_instrumento = identificador_de_proceso, " requiere ", objeto_con_opcion_de_estado ;

oracion_de_control = oracion_de_evento | oracion_de_condicion | oracion_de_excepcion ;
oracion_de_evento = oracion_de_evento_de_consumo | oracion_de_evento_de_efecto
 | oracion_de_evento_de_agente | oracion_de_evento_de_instrumento ;
oracion_de_evento_de_consumo = objeto_con_opcion_de_estado, " inicia ", identificador_de_proceso,
 ", que consume ", identificador_de_objeto ;
oracion_de_evento_de_efecto = identificador_de_objeto, " inicia ", identificador_de_proceso,
 ", que afecta ", identificador_de_objeto ;
oracion_de_evento_de_agente = objeto_con_opcion_de_estado, " inicia y maneja ", identificador_de_proceso ;
oracion_de_evento_de_instrumento = objeto_con_opcion_de_estado, " inicia ", identificador_de_proceso,
 ", que requiere ", objeto_con_opcion_de_estado ;

oracion_de_invocacion = identificador_de_proceso, " invoca ", lista_de_procesos
 | identificador_de_proceso, " se invoca a sí mismo" ;
oracion_de_excepcion_por_sobretiempo = identificador_de_proceso_activo,
 " ocurre si duración de ", identificador_de_proceso, " excede ", max_duracion_unidades_tiempo ;
oracion_de_excepcion_por_subtiempo = identificador_de_proceso_activo,
 " ocurre si duración de ", identificador_de_proceso, " es menor que ", min_duracion_unidades_tiempo ;
oracion_de_excepcion = oracion_de_excepcion_por_sobretiempo | oracion_de_excepcion_por_subtiempo ;

(* Etiquetas de ruta *)

oracion_de_ruta =
 "Por ruta ", cadena_etiqueta, ", ", oracion_procedimental ;

cadena_etiqueta = nombre ;
```

Las variantes XOR y OR usan `exactamente uno de` y `al menos uno de`. Las oraciones de condición siguen el patrón `ocurre si ... en cuyo caso ... de lo contrario ... se omite`.

## A.6 Oraciones de condición

```ebnf
oracion_de_condicion = oracion_transformadora_condicional | oracion_habilitadora_condicional ;

oracion_transformadora_condicional = oracion_de_consumo_condicional
 | oracion_de_consumo_condicional_con_estado
 | oracion_de_efecto_condicional ;

oracion_de_consumo_condicional = ( identificador_de_proceso, " ocurre si ", identificador_de_objeto,
 " existe, en cuyo caso ", identificador_de_objeto, " se consume, de lo contrario ",
 identificador_de_proceso, " se omite" )
 | ( "Si ", identificador_de_objeto, " existe entonces ", identificador_de_proceso,
 " ocurre y consume ", identificador_de_objeto, ", de lo contrario se omite ",
 identificador_de_proceso ) ;

oracion_de_consumo_condicional_con_estado = ( identificador_de_proceso, " ocurre si ",
 identificador_de_objeto, " está en ", estado_de_entrada, ", en cuyo caso ",
 identificador_de_objeto, " se consume, de lo contrario ", identificador_de_proceso, " se omite" ) ;

oracion_de_efecto_condicional = oracion_de_efecto_condicional_simple
 | oracion_de_efecto_entrada_salida_condicional
 | oracion_de_efecto_entrada_condicional
 | oracion_de_efecto_salida_condicional ;

oracion_de_efecto_condicional_simple = identificador_de_proceso, " ocurre si ",
 identificador_de_objeto, " existe, en cuyo caso ", identificador_de_proceso,
 " afecta ", identificador_de_objeto, ", de lo contrario ", identificador_de_proceso, " se omite" ;

oracion_de_efecto_entrada_salida_condicional = identificador_de_proceso, " ocurre si ",
 identificador_de_objeto, " está en ", estado_de_entrada, ", en cuyo caso ",
 identificador_de_proceso, " cambia ", identificador_de_objeto, " de ", estado_de_entrada,
 " a ", estado_de_salida, ", de lo contrario ", identificador_de_proceso, " se omite" ;

oracion_de_efecto_entrada_condicional = identificador_de_proceso, " ocurre si ",
 identificador_de_objeto, " está en ", estado_de_entrada, ", en cuyo caso ",
 identificador_de_proceso, " cambia ", identificador_de_objeto, " de ", estado_de_entrada,
 ", de lo contrario ", identificador_de_proceso, " se omite" ;

oracion_de_efecto_salida_condicional = identificador_de_proceso, " ocurre si ",
 identificador_de_objeto, " existe, en cuyo caso ", identificador_de_proceso,
 " cambia ", identificador_de_objeto, " a ", estado_de_salida,
 ", de lo contrario ", identificador_de_proceso, " se omite" ;

oracion_habilitadora_condicional = oracion_de_agente_condicional
 | oracion_de_instrumento_condicional ;

oracion_de_agente_condicional = ( objeto_con_opcion_de_estado, " maneja ",
 identificador_de_proceso, " si ", identificador_de_objeto, " existe, de lo contrario ",
 identificador_de_proceso, " se omite" )
 | ( objeto_con_opcion_de_estado, " maneja ", identificador_de_proceso, " si ",
 identificador_de_objeto, " está en ", identificador_de_estado, ", de lo contrario ",
 identificador_de_proceso, " se omite" ) ;

oracion_de_instrumento_condicional = ( identificador_de_proceso, " ocurre si ",
 identificador_de_objeto, " existe, de lo contrario ", identificador_de_proceso, " se omite" )
 | ( identificador_de_proceso, " ocurre si ", identificador_de_objeto, " está en ",
 identificador_de_estado, ", de lo contrario ", identificador_de_proceso, " se omite" ) ;
```

## A.7 Producciones adicionales

```ebnf
(* --- Restricciones de expresión para multiplicidad --- *)

restriccion_de_expresion = "donde ", nombre, ( ( operacion_logica, nombre_de_valor )
 | ( inicio_conjunto, ( nombre | nombre_de_valor ),
 { ",", ( nombre | nombre_de_valor ) }, fin_conjunto ) ) ;

operacion_logica = "=" | "<" | ">" | "<=" | ">=" ;
inicio_conjunto = " en {" ;
fin_conjunto = "}" ;

(* --- Listas bifurcadas con orden --- *)

conjunto_de_cosas_objeto = cosa_objeto, [ { ", ", cosa_objeto } ],
 " y ", ( cosa_objeto | "más" ),
 [ ( ", ordenados por ", criterio_de_orden ) | ( ", en esa secuencia" ) ] ;

conjunto_de_cosas_proceso = cosa_proceso, [ { ", ", cosa_proceso } ],
 " y ", ( cosa_proceso | "más" ),
 [ ( ", ordenados por ", criterio_de_orden ) | ( ", en esa secuencia" ) ] ;

criterio_de_orden = nombre ;
cosa_objeto = [ restriccion_de_participacion, " " ], objeto_con_opcion_de_estado ;
cosa_proceso = [ restriccion_de_participacion, " " ], identificador_de_proceso ;

(* --- Especialización XOR y herencia múltiple --- *)

oracion_de_especializacion_xor_objeto = oracion_basica_xor_objeto
 | oracion_xor_objeto_separada_por_comas ;
oracion_basica_xor_objeto = objeto_especial, " puede ser ",
 identificador_de_objeto, " o ", identificador_de_objeto ;
oracion_xor_objeto_separada_por_comas = objeto_especial, " puede ser uno de ",
 identificador_de_objeto, { ", ", identificador_de_objeto }, " o ", identificador_de_objeto ;

oracion_de_herencia_multiple_objeto = objeto_especial, " es ",
 lista_de_objetos_generales ;
lista_de_objetos_generales = " un ", identificador_de_objeto,
 [ { " un ", identificador_de_objeto } ], " y un ", identificador_de_objeto ;
```

## A.8 Oraciones estructurales

```ebnf
oracion_estructural = oracion_de_enlace_estructural_etiquetado | oracion_de_agregacion
 | oracion_de_caracterizacion
 (* | oracion_de_exhibicion — eliminada de oracion_estructural: alias de oracion_de_caracterizacion, genera ambiguedad *)
 | oracion_de_especializacion | oracion_de_instanciacion ;

(* --- Oraciones de enlace estructural etiquetado --- *)

oracion_de_enlace_estructural_etiquetado = oracion_etiquetado_unidireccional
 | oracion_etiquetado_bidireccional ;

oracion_etiquetado_unidireccional = oracion_etiquetado_unidireccional_simple
 | oracion_etiquetado_bifurcada ;

oracion_etiquetado_unidireccional_simple =
 oracion_etiquetado_nullTag_objeto
 | oracion_etiquetado_nullTag_proceso
 | oracion_etiquetado_nonNullTag_objeto
 | oracion_etiquetado_nonNullTag_proceso ;

oracion_etiquetado_nullTag_objeto = [restriccion_de_participacion, " "],
 objeto_origen, etiqueta_nula_unidireccional, [restriccion_de_participacion, " "], objeto_destino ;
oracion_etiquetado_nullTag_proceso = [restriccion_de_participacion, " "],
 proceso_origen, etiqueta_nula_unidireccional, [restriccion_de_participacion, " "], proceso_destino ;
oracion_etiquetado_nonNullTag_objeto = [restriccion_de_participacion, " "],
 objeto_origen, " ", etiqueta_directa, " ", [restriccion_de_participacion, " "], objeto_destino,
 [", ", restriccion_de_expresion] ;
oracion_etiquetado_nonNullTag_proceso = [restriccion_de_participacion, " "],
 proceso_origen, " ", etiqueta_directa, " ", [restriccion_de_participacion, " "], proceso_destino ;

etiqueta_nula_unidireccional = " se relaciona con "
 | etiqueta_nula_definida_por_usuario ;

(* Variantes bifurcadas: listas de refinadores con orden o secuencia *)
oracion_etiquetado_bifurcada = oracion_bifurcada_nullTag_objeto
 | oracion_bifurcada_nullTag_proceso
 | oracion_bifurcada_nonNullTag_objeto
 | oracion_bifurcada_nonNullTag_proceso ;

oracion_bifurcada_nullTag_objeto = [restriccion_de_participacion, " "], objeto_origen,
 etiqueta_nula_unidireccional, conjunto_de_cosas_objeto ;
oracion_bifurcada_nullTag_proceso = [restriccion_de_participacion, " "], proceso_origen,
 etiqueta_nula_unidireccional, conjunto_de_cosas_proceso ;
oracion_bifurcada_nonNullTag_objeto = [restriccion_de_participacion, " "], objeto_origen,
 " ", etiqueta_directa, " ", conjunto_de_cosas_objeto ;
oracion_bifurcada_nonNullTag_proceso = [restriccion_de_participacion, " "], proceso_origen,
 " ", etiqueta_directa, " ", conjunto_de_cosas_proceso ;

(* conjunto_de_cosas_objeto y conjunto_de_cosas_proceso ya definidos en A.7 — no redefinir aquí *)

(* Variantes bidireccionales *)
oracion_etiquetado_bidireccional = oracion_bidireccional_asimetrica_objeto
 | oracion_bidireccional_asimetrica_proceso
 | oracion_bidireccional_simetrica_objeto
 | oracion_bidireccional_simetrica_proceso ;

oracion_bidireccional_asimetrica_objeto = ( [restriccion_de_participacion, " "],
 objeto_origen, etiqueta_directa_bidireccional, [restriccion_de_participacion, " "], objeto_destino,
 [", ", restriccion_de_expresion] )
 | ( [restriccion_de_participacion, " "], objeto_destino, etiqueta_inversa_bidireccional,
 [restriccion_de_participacion, " "], objeto_origen, [", ", restriccion_de_expresion] ) ;
oracion_bidireccional_simetrica_objeto = ( [restriccion_de_participacion, " "],
 objeto_origen, " y ", [restriccion_de_participacion, " "], objeto_destino, " son ", etiqueta_simetrica )
 | ( [restriccion_de_participacion, " "], objeto_origen, " y ", [restriccion_de_participacion, " "],
 objeto_destino, etiqueta_nula_bidireccional ) ;

oracion_bidireccional_asimetrica_proceso = ( [restriccion_de_participacion, " "],
 proceso_origen, etiqueta_directa_bidireccional, [restriccion_de_participacion, " "], proceso_destino )
 | ( [restriccion_de_participacion, " "], proceso_destino, etiqueta_inversa_bidireccional,
 [restriccion_de_participacion, " "], proceso_origen ) ;
oracion_bidireccional_simetrica_proceso = ( [restriccion_de_participacion, " "],
 proceso_origen, " y ", [restriccion_de_participacion, " "], proceso_destino, " son ", etiqueta_simetrica )
 | ( [restriccion_de_participacion, " "], proceso_origen, " y ", [restriccion_de_participacion, " "],
 proceso_destino, etiqueta_nula_bidireccional ) ;

etiqueta_simetrica = expresion_de_etiqueta ;
etiqueta_directa_bidireccional = expresion_de_etiqueta ;
etiqueta_inversa_bidireccional = expresion_de_etiqueta ;
etiqueta_nula_bidireccional = " se relacionan"
 | etiqueta_nula_definida_por_usuario ;

```

## A.9 Oraciones de estructuras fundamentales

```ebnf
oracion_de_agregacion = oracion_de_agregacion_objeto | oracion_de_agregacion_proceso ;
oracion_de_agregacion_objeto = objeto_todo, " consta de ", lista_de_partes_objeto ;
oracion_de_agregacion_proceso = proceso_todo, " consta de ", lista_de_partes_proceso ;
lista_de_partes_objeto = parte_objeto, [ { ", ", parte_objeto } ], " y ", ( parte_objeto | "al menos otra parte" ) ;
lista_de_partes_proceso = parte_proceso, [ { ", ", parte_proceso } ], " y ", ( parte_proceso | "al menos otra parte" ) ;
parte_objeto = [restriccion_de_participacion, " "], identificador_de_objeto ;
parte_proceso = [restriccion_de_participacion, " "], identificador_de_proceso ;

oracion_de_caracterizacion = oracion_de_caract_objeto | oracion_de_caract_proceso ;
oracion_de_caract_objeto = identificador_de_objeto, " exhibe ",
 ( lista_de_atributos | lista_de_operadores
 | lista_de_atributos, ", así como ", lista_de_operadores ) ;
oracion_de_caract_proceso = identificador_de_proceso, " exhibe ",
 ( lista_de_operadores | lista_de_atributos
 | lista_de_operadores, ", así como ", lista_de_atributos ) ;

(* Alias conservado como documentacion; no referenciado desde oracion_estructural para evitar ambiguedad *)
oracion_de_exhibicion = oracion_de_caract_objeto | oracion_de_caract_proceso ;

oracion_de_especializacion = oracion_de_especializacion_objeto | oracion_de_especializacion_proceso
 | oracion_de_especializacion_estado
 | oracion_de_especializacion_individual
 | oracion_de_especializacion_xor_objeto
 | oracion_de_herencia_multiple_objeto ;
oracion_de_especializacion_objeto = lista_de_objetos_especiales, " son ", identificador_de_objeto ;
oracion_de_especializacion_proceso = lista_de_procesos_especiales, " son ", identificador_de_proceso ;
oracion_de_especializacion_estado = lista_de_objetos_con_estado, " son ", objeto_con_estado ;

oracion_de_especializacion_individual =
 identificador_de_objeto, " es ", articulo, identificador_de_objeto ;

articulo = "un " | "una " ;

oracion_de_instanciacion = oracion_de_instanciacion_objeto | oracion_de_instanciacion_proceso ;
oracion_de_instanciacion_objeto = identificador_de_objeto, " es una instancia de ", identificador_de_objeto
 | lista_de_objetos_instancia, " son instancias de ", identificador_de_objeto ;
oracion_de_instanciacion_proceso = identificador_de_proceso, " es una instancia de ", identificador_de_proceso
 | lista_de_procesos_instancia, " son instancias de ", identificador_de_proceso ;

atributo = identificador_de_objeto ;
operador = identificador_de_proceso ;
rasgo = atributo | operador ;
```

## A.10 Oraciones de gestión de contexto

```ebnf
oracion_de_gestion_de_contexto = oracion_de_despliegue | oracion_de_plegado
 | oracion_de_descomposicion | oracion_de_recomposicion
 | oracion_de_composicion_intermodelo | oracion_de_referencia_externa ;

oracion_de_composicion_intermodelo =
  opd_hijo, " es una vista de sub-modelo de ", nombre_de_modelo
 | opd_hijo, " referencia el sub-modelo ", nombre_de_modelo, " desde ", opd_padre ;

oracion_de_referencia_externa =
  identificador_de_objeto, " en ", opd_hijo, " es referencia externa a ",
  identificador_de_objeto, " del modelo propietario ", nombre_de_modelo ;

(* --- Oraciones de despliegue (unfolding) --- *)

oracion_de_despliegue = oracion_de_despliegue_objeto | oracion_de_despliegue_proceso ;

oracion_de_despliegue_objeto = oracion_de_despliegue_objeto_inespecificado
 | oracion_de_despliegue_objeto_todo
 | oracion_de_despliegue_objeto_general
 | oracion_de_despliegue_objeto_clase
 | oracion_de_despliegue_objeto_exhibidor ;

oracion_de_despliegue_objeto_inespecificado = identificador_de_objeto,
 " se despliega en ", lista_de_atributos, [", así como ", lista_de_operadores] ;
oracion_de_despliegue_objeto_todo = objeto_todo, " desde ", opd_padre,
 " se despliega por partes en ", opd_hijo, " en ", lista_de_partes_objeto ;
oracion_de_despliegue_objeto_general = objeto_general, " desde ", opd_padre,
 " se despliega por especialización en ", opd_hijo, " en ", lista_de_objetos_especiales ;
oracion_de_despliegue_objeto_clase = clase_de_objeto, " desde ", opd_padre,
 " se despliega por instanciación en ", opd_hijo, " en ", lista_de_objetos_instancia ;
oracion_de_despliegue_objeto_exhibidor = identificador_de_objeto, " desde ", opd_padre,
 " se despliega por rasgos en ", opd_hijo, " en ", lista_de_atributos, [", así como ", lista_de_operadores] ;

oracion_de_despliegue_proceso = oracion_de_despliegue_proceso_inespecificado
 | oracion_de_despliegue_proceso_todo
 | oracion_de_despliegue_proceso_general
 | oracion_de_despliegue_proceso_clase
 | oracion_de_despliegue_proceso_exhibidor ;

oracion_de_despliegue_proceso_inespecificado = identificador_de_proceso,
 " se despliega en ", lista_de_operadores, [", así como ", lista_de_atributos] ;
oracion_de_despliegue_proceso_todo = proceso_todo, " desde ", opd_padre,
 " se despliega por partes en ", opd_hijo, " en ", lista_de_partes_proceso ;
oracion_de_despliegue_proceso_general = proceso_general, " desde ", opd_padre,
 " se despliega por especialización en ", opd_hijo, " en ", lista_de_procesos_especiales ;
oracion_de_despliegue_proceso_clase = clase_de_proceso, " desde ", opd_padre,
 " se despliega por instanciación en ", opd_hijo, " en ", lista_de_procesos_instancia ;
oracion_de_despliegue_proceso_exhibidor = identificador_de_proceso, " desde ", opd_padre,
 " se despliega por rasgos en ", opd_hijo, " en ", lista_de_operadores, [", así como ", lista_de_atributos] ;

(* --- Oraciones de plegado (folding) --- *)

oracion_de_plegado = oracion_de_plegado_objeto | oracion_de_plegado_proceso ;
oracion_de_plegado_objeto = identificador_de_objeto, " se pliega en ", opd_padre ;
oracion_de_plegado_proceso = identificador_de_proceso, " se pliega en ", opd_padre ;

(* --- Oraciones de descomposición (in-zooming) --- *)

oracion_de_descomposicion = oracion_de_descomposicion_en_diagrama
 | oracion_de_descomposicion_en_nuevo_diagrama
 | oracion_de_descomposicion_objeto_en_diagrama
 | oracion_de_descomposicion_objeto_en_nuevo_diagrama ;

oracion_de_descomposicion_en_diagrama = ( identificador_de_proceso, " se descompone en ",
 lista_de_procesos, ", en esa secuencia", [", así como ", lista_de_objetos_en_zoom] )
 | ( identificador_de_proceso, " se descompone en paralelo ", lista_de_procesos,
 [", así como ", lista_de_objetos_en_zoom] )
 | ( identificador_de_proceso, " se descompone en ", lista_de_procesos,
 " y en paralelo ", lista_de_procesos, ", en esa secuencia",
 [", así como ", lista_de_objetos_en_zoom] ) ;

oracion_de_descomposicion_en_nuevo_diagrama = ( identificador_de_proceso, " desde ", opd_padre,
 " se descompone en ", opd_hijo, " en ", lista_de_procesos, ", en esa secuencia",
 [", así como ", lista_de_objetos_en_zoom] )
 | ( identificador_de_proceso, " desde ", opd_padre,
 " se descompone en ", opd_hijo, " en paralelo ", lista_de_procesos,
 [", así como ", lista_de_objetos_en_zoom] )
 | ( identificador_de_proceso, " desde ", opd_padre,
 " se descompone en ", opd_hijo, " en ", lista_de_procesos,
 " y en paralelo ", lista_de_procesos, ", en esa secuencia",
 [", así como ", lista_de_objetos_en_zoom] ) ;

oracion_de_descomposicion_objeto_en_diagrama = ( identificador_de_objeto, " se descompone en ",
 lista_de_objetos, ", en esa secuencia", [", así como ", lista_de_procesos_en_zoom] ) ;

oracion_de_descomposicion_objeto_en_nuevo_diagrama = ( identificador_de_objeto, " desde ", opd_padre,
 " se descompone en ", opd_hijo, " en ", lista_de_objetos, ", en esa secuencia",
 [", así como ", lista_de_procesos_en_zoom] ) ;

lista_de_objetos_en_zoom = lista_de_objetos ;
lista_de_procesos_en_zoom = lista_de_procesos ;

(* --- Oraciones de recomposición (out-zooming) --- *)

oracion_de_recomposicion = oracion_de_recomposicion_proceso | oracion_de_recomposicion_objeto ;
oracion_de_recomposicion_proceso = identificador_de_proceso, " se recompone desde ", opd_hijo ;
oracion_de_recomposicion_objeto = identificador_de_objeto, " se recompone desde ", opd_hijo ;
```

Para subprocesos paralelos, la forma abreviada es:

- `*Proceso* se descompone en paralelo *A* y *B*.`

Para subprocesos mixtos (secuenciales y paralelos):

- `*Proceso* se descompone en *A*, paralelo *B* y *C*, y *D*, en esa secuencia.`

---

## 18. Notas de Implementación

### 18.1 Análisis Sintáctico Bidireccional

Una herramienta OPM bilingüe debería:

1. Detectar idioma de la sentencia OPL por verbo principal (consume/consumes, genera/yields, etc.)
2. Permitir cambio de idioma global del modelo (re-generar todas las sentencias OPL)
3. Mantener el modelo semántico (OPD) independiente del idioma OPL
4. Permitir modelos mixtos solo si el usuario lo habilita explícitamente (no recomendado)

### 18.2 Soporte de herramienta

Una herramienta OPM multilingüe puede implementar OPL-ES como idioma textual alternativo del mismo modelo semántico.

A nivel de superficie textual, una implementación operativa DEBERÍA además permitir:

1. Elegir idioma OPL a nivel de usuario/modelo sin alterar el OPD subyacente
2. Mostrar todas las sentencias o solo las de esencia no predeterminada
3. Alternar numeración y, cuando la implementación proyecte rótulos computacionales o decoraciones de la capa visual, alias y visualización de unidades sin afectar la semántica del OPL subyacente
4. Regenerar el párrafo OPL completo al cambiar idioma, manteniendo invariantes de ida y vuelta
5. Asociar cada referencia visible a OPD (`SD`, `SD1`, `SD1.1`, etc.) con un identificador persistente recuperable en la serialización
6. Mantener el OPL local autocontenido de cada modelo individual cuando existan sub-modelos
7. Emitir la composición inter-modelo mediante oraciones explícitas o metadatos equivalentes, sin colapsar el compuesto en un único árbol textual implícito
8. Preservar la frontera entre modelo propietario y modelo consumidor cuando una cosa aparezca como referencia externa

En modelos compuestos, la especificación textual global no debe inferirse únicamente desde la navegación visible del árbol OPD. Debe conservar explícitamente la frontera entre modelos individuales y el vínculo entre etiqueta visible de OPD e identificador persistente.

### 18.3 Compatibilidad Semántica

OPL-ES no modifica la semántica OPM. Un modelo creado con OPL-ES es semánticamente idéntico a su equivalente OPL-EN. La traducción es puramente léxica y sintáctica, no semántica. El modelo interno (constructos OPD, conjuntos de enlaces, conjuntos de cosas) permanece invariante.

### 18.4 Equivalencia de Ida y Vuelta

Toda sentencia OPL-EN en forma canónica tiene al menos una sentencia OPL-ES semánticamente equivalente y viceversa. La transformación EN→ES→EN DEBE preservar la semántica original, aunque la superficie española pueda realizarse con infinitivo o con nominalización encabezada por `-ción` (y, cuando aplique, `-miento`). La herramienta DEBERÍA respetar la forma elegida por el modelo o normalizarla al registro configurado, pero NO forzar exclusivamente infinitivo.

**Nota normativa sobre ida y vuelta y superficie:** preservar ida y vuelta NO significa imponer una única forma superficial en español. Significa preservar el mismo hecho del modelo y la misma estructura argumental. Por lo tanto, si dos nombres de proceso en OPL-ES son semánticamente equivalentes y válidos en el dominio, ambos PUEDEN mapear al mismo proceso interno, siempre que el modelo conserve un nombre canónico interno por cosa. Ejemplo: `Verificar Identidad` y `Verificación de Identidad` PUEDEN representar el mismo proceso. Al volver de ES a EN, la herramienta DEBE recuperar un nombre inglés semánticamente equivalente, aunque la superficie española original no haya sido la única posible. La normalización de superficie, si existe, DEBERÍA ser configurable por política editorial del modelo, no una imposición semántica fija del lenguaje.

### 18.5 Política de Modelos Mixtos

Un modelo con prosa de apoyo en español y OPL canónica en inglés es aceptable como artefacto editorial, pero una herramienta bilingüe NO DEBERÍA mezclar OPL-EN y OPL-ES dentro del mismo párrafo generado salvo habilitación explícita del usuario. La política recomendada es:

1. Un idioma OPL canónico por modelo activo
2. Cambio de idioma mediante re-generación completa, no edición parcial
3. Mezcla EN/ES solo para revisión o migración, nunca como estado estable por defecto
