---
urn: urn:fxsl:kb:opd-es
nombre: opd-es
version: 3.0.2
estado: publicado
descripcion: "Gramática visual canónica del OPD: capa visual de la SSOT OPM-ES con las reglas V-* de representación gráfica de OPM."
fuente: "SSOT OPM v3.0.2. Re-sincronizado desde la bestia (~/kora) artifacts/knowledge/fxsl/opm/opm-ssot-es/opm-visual-es.md (sha256:02506aa8de095c009621879cc95c03d0e93870ef5ffd7af9ccc1402bf125979e) el 2026-06-15; cuerpo byte-fiel. DECISION HITL 2026-06-15: pneuma toma la posta como SSOT viva de OPM (urn:kora:kb:regimen-de-ley); la bestia queda como ultimo origen historico, ya no SSOT viva. Reemplaza la migracion snapshot del 2026-06-12 (v3.0.0); incorpora los deltas v1.4.0 del corpus consolidado (6.a familia de enlace Excepcion, abanicos convergentes de habilitadores, ruta sobre habilitadores, R-FAN-PROB-1 A/B/C, R-NOM-PROC-1 deverbal, co-enmiendas de bases)."
autor: FS
creado: 2026-04-27
lang: es
tags: [opm, especificacion-visual, gramatica-grafica, opd, v2, ampliada]
familia: bok
depende: [urn:fxsl:kb:opm-es]
cita: [urn:fxsl:kb:manual-metodologico-opm-es, urn:fxsl:kb:opl-es, urn:fxsl:kb:opm-es]
---


# OPD — Gramática visual de OPM (v3.0.1)

Reglas completas para construir y evaluar cualquier OPD (Diagrama Objeto‑Proceso, Object-Process Diagram) conforme a esta adaptación española del corpus OPM. Este documento opera primariamente a nivel de **tipo y representación**: define las primitivas, composiciones válidas, restricciones y reglas de precedencia que gobiernan la capa gráfica de OPM, e incluye las convenciones visuales de ejecución, simulación, instanciación, estereotipos, composición inter-modelo, validación y exportación canónica cuando afectan la forma visible del OPD.

Referencia de núcleo: `urn:fxsl:kb:opm-es`.

Esta versión integra los resultados del análisis de corpus OPCloud contra la v1 y aplica las decisiones axiomáticas D1..D6 documentadas en `ssot-decisiones-axiomaticas.md`. Es la **capa visual canónica** del corpus OPM-ES en KORA (v3.0.1). Reemplaza a la línea `ssot/` legacy, ya removida del repositorio.

---

## 0. Alcance y contrato editorial

Este documento es la **capa gráfica canónica** del corpus OPM en español. Su responsabilidad es:

- fijar símbolos, contornos, decoraciones y marcas gráficas;
- definir composición visual válida de enlaces, operadores, estados y refinamientos;
- formalizar reglas de precedencia, distribución y comportamiento visual entre OPDs;
- regular los artefactos canónicos de exportación que determinan qué es conforme;
- admitir extensiones tipadas (estereotipos, capa computacional) y composición inter-modelo.

Este documento **no** define:

- la semántica base de OPM, que pertenece a [OPM — Núcleo conceptual](urn:fxsl:kb:opm-es);
- la realización textual canónica, que pertenece a [OPL-ES](urn:fxsl:kb:opl-es);
- el procedimiento de construcción del modelo, heurísticas de decisión y gobernanza, que pertenecen a [Manual metodológico de OPM](urn:fxsl:kb:manual-metodologico-opm-es).

Regla editorial: cuando una regla visual requiera mencionar nombres, plantillas OPL o secuencias de modelado, este documento solo remite a la capa propietaria de ese contenido.

Las reglas `V-*` de esta capa fijan la gramática visual estable del corpus; cuando resumen semántica base, la reexpresan como parte del contrato gráfico vigente.

Convención de numeración: la numeración `V-*` es **estable por familia conceptual y por historia editorial**, no por orden lineal de aparición en el archivo. Se conserva así para no romper referencias cruzadas del corpus ni citas externas.

Convenciones léxicas: los términos **contorno**, **borde** y **línea** se usan como sinónimos dentro de este documento para referirse a la traza perimetral de una primitiva gráfica. Las formas específicas (por ejemplo "contorno discontinuo", "borde doble", "línea en zigzag") son modificadores que especifican una variante concreta. Cuando la regla canónica depende de una variante determinada, ésta queda explícita en la redacción de la regla.

### 0.1 Regla rectora de canonicidad por exportación

**Regla V-0**: La gramática visual OPM conforme es la que persiste en un **export canónico declarado** por la implementación. Todo elemento visible en canvas que no persiste en ningún export canónico de esa implementación se clasifica como afordance UI, no como gramática OPM.

**Regla V-0a**: Toda implementación conforme DEBE declarar al menos dos perfiles de export:

- **canon-diagrama**: export por OPD, preferentemente vectorial, que preserva la gramática visible del diagrama y su metadato mínimo de identificación;
- **canon-documento**: export por modelo, potencialmente multi-OPD, que puede incluir OPL, diccionarios, portadas, anexos y vistas derivadas además del diagrama.

**Regla V-0b**: Si un elemento persiste en el canon-diagrama, pertenece a la gramática visible del OPD y debe quedar cubierto por alguna regla `V-*` o por un capítulo explícito de esta capa.

**Regla V-0c**: Si un elemento aparece en canvas editable pero desaparece del canon-diagrama y del canon-documento, es UI transitoria. No puede reutilizar sin distinción los canales visuales reservados a la gramática semántica.

**Regla V-0d**: Si un elemento aparece solo en uno de los perfiles canónicos, la implementación debe declararlo como atributo de perfil y la SSOT debe arbitrarlo explícitamente.

**Regla V-0e**: Una captura de pantalla del canvas en modo edición, navegación, modal o simulación pausada no constituye por sí misma evidencia suficiente de canonicidad.

---

## 1. Primitivas gráficas

La capa visual de OPM se construye con un vocabulario cerrado de formas, contornos, sombreados, decoraciones de extremo y marcas textuales. Ningún elemento fuera de este vocabulario es válido en un OPD conforme.

## 1.1 Formas cerradas (cosas)

| Forma | Entidad que representa |
|---|---|
| Rectángulo | Objeto |
| Elipse | Proceso |
| Rectángulo redondeado (EN: rountangle) | Estado (siempre contenido dentro de un objeto) |

## 1.1b Esquema de colores canónico (informativo)

Los colores no codifican semántica por sí mismos; la semántica se fija por forma, contorno y sombreado. El siguiente esquema de colores es solo una convención de referencia del corpus:

| Elemento | Color de borde | Color de fondo |
|---|---|---|
| Objeto | Verde | Transparente (informacional) o blanco |
| Proceso | Azul oscuro | Transparente (informacional) o blanco |
| Estado | Verde oliva | Gris claro |
| Enlace estructural | Negro | — |
| Enlace procedimental | Negro | — |

**Regla V-63 (ampliada)**: Los colores son informativos, no normativos, tanto para bordes y líneas como para las decoraciones internas de los símbolos estructurales. Una implementación puede emplear azul, negro u otra paleta legible, siempre que preserve sin ambigüedad la topología semántica del símbolo (ver §1.7 y V-128).

## 1.2 Atributos de contorno

| Contorno | Codifica |
|---|---|
| Continuo (sólido) | Afiliación sistémica — la cosa pertenece al sistema |
| Discontinuo (punteado) | Afiliación ambiental — la cosa pertenece al entorno |

**Regla V-69**: El contorno grueso (indicador de refinamiento) aplica tanto a la descomposición en nuevo diagrama (`in-zooming`) como al despliegue en nuevo diagrama (`unfolding`): ambos tipos de refinamiento producen contorno grueso en el refinable.

**Regla V-70**: El despliegue en el mismo diagrama (despliegue intradiagrama) NO produce contorno grueso, porque el refinable y los refinadores comparten OPD.

**Regla V-71**: El tipo de contorno (sólido o punteado) persiste en todos los niveles de refinamiento. Un objeto ambiental mantiene contorno discontinuo en el OPD padre y en todos los OPDs hijo donde aparezca como externo.

## 1.3 Atributos de profundidad (sombreado)

| Profundidad | Codifica |
|---|---|
| Sombreado canónico (sombra gris desplazada abajo-derecha) | Esencia física |
| Plano (sin sombra canónica) | Esencia informacional |

La sombra es un canal semántico reservado. Su presencia o ausencia codifica esencia de la cosa cuando el artefacto observado es canónico.

**Regla V-124**: El sombreado visible en el canon-diagrama DEBE corresponder exclusivamente a esencia física. La implementación DEBE suprimir en el export canónico toda sombra decorativa de UI aplicada uniformemente a cosas informacionales.

**Regla V-125**: Si una cosa refinable es física, su contenedor refinado en el OPD hijo DEBE preservar la marca de esencia física. La esencia no puede perderse visualmente por el solo hecho del refinamiento.

**Regla V-126**: La sombra de una cosa puede provenir de tres orígenes operativos distintos en la herramienta: declaración explícita del modelador, propiedad forzada por un estereotipo, o preset de sesión. En el artefacto canónico esos tres orígenes deben colapsar a un mismo resultado semántico visible: sombra si y solo si la cosa es física.

**Regla V-127**: Si una implementación usa reforzadores de canvas para hacer más visible la fisicidad en edición, esos reforzadores deben diferenciarse perceptualmente de la sombra semántica y no pueden persistir en el canon-diagrama.

## 1.4 Producto cartesiano: las ocho representaciones de cosa

Toda cosa OPM se renderiza como Forma x Contorno x Profundidad:

| # | Forma | Contorno | Profundidad | Cosa resultante |
|---|---|---|---|---|
| 1 | Rectángulo | sólido | sombreado | Objeto físico sistémico |
| 2 | Rectángulo | sólido | plano | Objeto informacional sistémico |
| 3 | Rectángulo | discontinuo | sombreado | Objeto físico ambiental |
| 4 | Rectángulo | discontinuo | plano | Objeto informacional ambiental |
| 5 | Elipse | sólido | sombreado | Proceso físico sistémico |
| 6 | Elipse | sólido | plano | Proceso informacional sistémico |
| 7 | Elipse | discontinuo | sombreado | Proceso físico ambiental |
| 8 | Elipse | discontinuo | plano | Proceso informacional ambiental |

**Regla V-1 (revisada)**: Los valores por defecto del modelo son informacional (sin sombra) y sistémico (borde continuo). Si no se especifica, toda cosa es informacional y sistémica. Una herramienta puede exponer configuraciones locales o presets de sesión, pero esos presets no alteran la semántica del modelo salvo que la esencia quede serializada explícitamente y sea recuperable en el canon-diagrama y en OPL.

**Regla V-2**: La perseverancia no es visual — se infiere del tipo: los objetos son persistentes, los procesos son transitorios.

## 1.5 Decoraciones de extremo de enlace

| Decoración | Nombre (ES) | Nombre técnico (EN) | Uso |
|---|---|---|---|
| Punta de flecha cerrada | punta cerrada | arrowhead | Enlaces transformadores (consumo, resultado, efecto) |
| Círculo negro relleno | piruleta negra | black lollipop | Enlace de agente (extremo proceso) |
| Círculo blanco vacío | piruleta blanca | white lollipop | Enlace de instrumento (extremo proceso) |
| Línea en zigzag con punta | rayo | lightning bolt | Enlace de invocación |
| Punta de flecha abierta | punta abierta | open arrowhead | Enlaces estructurales etiquetados unidireccionales |
| Arpón (media punta) | arpón | harpoon | Enlaces estructurales etiquetados bidireccionales y recíprocos |

**Regla V-190**: Una piruleta semántica de agente o instrumento siempre cuelga del extremo de una línea visible. Un círculo aislado sin línea visible no se interpreta como piruleta; debe tratarse como UI, token runtime o error de render según el perfil observado.

**Regla V-191**: Los handles de edición y puntos de anclaje UI no pueden ser visualmente idénticos a las piruletas de §1.5 en el canon-diagrama. Si la implementación los usa en edición, debe distinguirlos por color reservado a UI, posición o tamaño.

## 1.6 Marcas textuales sobre enlaces

| Marca | Significado |
|---|---|
| `e` | Modificador de evento — el objeto inicia el proceso |
| `c` | Modificador de condición — el proceso se omite si la precondición falla |
| `/` | Excepción por sobretiempo |
| `//` | Excepción por subtiempo |
| `Pr=p` | Probabilidad del enlace dentro de un abanico probabilístico |
| Texto itálico sobre el eje | Etiqueta (tag) de enlace estructural |
| Texto sobre enlace procedimental | Etiqueta de ruta (path label) |

## 1.7 Símbolos triangulares (relaciones estructurales fundamentales)

| Símbolo topológico | Relación |
|---|---|
| Triángulo con interior completamente relleno | Agregación-participación |
| Triángulo con triángulo interior distinguible | Exhibición-caracterización |
| Triángulo vacío (sin interior distinguible) | Generalización-especialización |
| Triángulo con círculo interior distinguible | Clasificación-instanciación |

La distinción normativa entre las cuatro relaciones estructurales fundamentales reside primariamente en la **topología interna del símbolo**, no en el matiz cromático empleado por la implementación.

**Regla V-3 (revisada)**: El vértice del triángulo siempre apunta hacia el refinable (todo, exhibidor, general, clase). La base conecta con los refinadores (partes, rasgos, especializaciones, instancias).

**Regla V-128**: La presencia, ausencia o tipo de interior distinguible en el triángulo es un canal normativo. Una implementación no es conforme si elimina, invierte o colapsa la decoración interior de exhibición o clasificación hasta volverlas indistinguibles de generalización.

**Regla V-129**: En un render canónico, todo triángulo estructural DEBE conectar por línea visible al menos con el refinable por el vértice y con un refinador por la base. Un triángulo sin líneas visibles en el canon-diagrama es divergente o debe tratarse como error de render.

**Regla V-130**: Si el canvas editable muestra triángulos auxiliares que desaparecen en export, esos triángulos son afordances UI y deben distinguirse perceptualmente de los triángulos semánticos por tamaño, color reservado a UI o ubicación fuera de la geometría del enlace.

**Regla V-131**: Los símbolos estructurales importados desde otra implementación OPM deben preservar, como mínimo, su topología interna. La retipificación cromática es admisible; la pérdida de interior distinguible no lo es.

## 1.8 Indicadores auxiliares

| Indicador | Representación | Significado |
|---|---|---|
| Colección incompleta | Barra horizontal corta bajo el triángulo | Existen refinadores no mostrados |
| Cosa duplicada | Silueta desplazada detrás del símbolo | Copia visual de la misma cosa en el mismo OPD |
| Supresión de estados | Rectángulo redondeado con `...` en esquina inferior derecha del objeto | El objeto tiene más estados que los mostrados |
| Multiplicidad | Número o expresión junto al extremo del enlace | Cardinalidad de la relación |
| Supresor de enlaces no materializados | Burbuja adyacente con `...` | Existen conexiones hacia cosas no presentes en el OPD actual |

**Regla V-192**: El supresor de enlaces no materializados pertenece a la gramática auxiliar del OPD solo si persiste en el canon-diagrama. No debe confundirse con menús contextuales o botones UI con la misma grafía.

**Regla V-193**: Los triángulos o indicadores estructurales compactados que representen relaciones adicionales hacia cosas ausentes deben quedar anclados geométricamente a la cosa visible correspondiente. Un triángulo flotante sin anclaje visible no es conforme en el canon-diagrama.

## 1.9 Estructura atómica del OPD

**Regla V-60**: Todo OPD se compone de constructos OPD. Un constructo OPD consiste de un conjunto de cosas (2 o más cosas) y un conjunto de enlaces (1 o más enlaces). El átomo mínimo es el constructo básico: exactamente 1 enlace conectando exactamente 2 cosas. Un constructo estructural básico conecta 2 objetos mediante 1 enlace estructural. Un constructo procedimental básico conecta 1 proceso y 1 objeto mediante 1 enlace procedimental.

## 1.10 Anatomía formal de un enlace

**Regla V-61**: Todo enlace consiste de tres componentes: origen (cosa o estado de origen), destino (cosa o estado de destino) y conector. El conector se compone de línea (la línea visible), símbolo (decoración de extremo) y, opcionalmente, etiqueta textual y etiqueta de ruta. Origen y destino son cosas enlazadas; cada una exhibe símbolo (decoración visual) y multiplicidad (cardinalidad).

---

## 2. Estados de objeto

### 2.1 Representación

Los estados se representan como rectángulos redondeados (EN: rountangles) contenidos dentro del rectángulo del objeto propietario, dispuestos horizontalmente en la zona inferior.

**Regla V-4**: Un estado no existe fuera de su objeto propietario. No hay estados flotantes. [Semántica heredada de `opm-es` término 3.68; aquí se fija la restricción de contención visual.]

**Regla V-5**: Un objeto sin estados no puede ser afectado; solo puede ser creado (resultado) o destruido (consumo). [Semántica heredada de `opm-es` §9; aquí se fija la restricción de conectividad gráfica.]

### 2.2 Marcadores de designación de estado

Esta versión incorpora `Current` como cuarta designación persistente del estado, además de las tres designaciones heredadas.

| Designación | Marca gráfica canónica | Significado |
|---|---|---|
| Inicial | Borde grueso simple (bold-contour) | Estado en la creación del objeto |
| Final | Doble borde concéntrico (double-contour) | Estado en el momento de ser consumido |
| Por defecto | Flecha diagonal abierta apuntando al estado | Estado más probable al inspeccionar aleatoriamente |
| `Current` | Marca externa reservada (ver V-54 y V-133) | Estado declarado como actual persistente del objeto |
| Normal | Borde estándar | Estado sin designación especial |

**Regla V-6 (revisada)**: Un objeto puede tener cero o más estados iniciales, cero o más estados finales, como máximo un estado por defecto y como máximo un estado `Current` declarado. [Semántica heredada de `opm-es` §8; aquí se fija la marca gráfica de cada designación.]

**Regla V-237**: La designación `Current` es declarable por el modelador y se serializa en el modelo como propiedad persistente del estado correspondiente. La herramienta que la ofrezca en edición debe garantizar que sobreviva al ciclo save/load y al export canónico.

**Regla V-238**: `Current` como designación persistente de §2.2 es distinta del **estado actual de runtime** durante simulación, regulado por V-54 y V-133. La marca visual puede coincidir, pero la serialización del modelo debe distinguir explícitamente entre designación declarada y marca inducida por ejecución.

### 2.3 Valores de atributo como estados

Los valores de un atributo son estados del objeto-atributo. Pueden expresarse como:
- Valores discretos: `sólido`, `líquido`, `gas`.
- Rangos numéricos: `120..240`.
- Valor concreto (en instancias): `185`.

---

## 3. Taxonomía completa de enlaces procedimentales

### 3.0 Familias canónicas de enlace

Esta versión declara explícitamente cinco familias canónicas de enlace. El resto de §3 a §9 se lee como desarrollo específico de cada familia.

**Regla V-239**: Toda relación expresable por enlace en un OPD conforme pertenece a una y solo una de las siguientes cinco familias:

1. **Transformadora procedimental** — enlaces que transforman al objeto participante (consumo, resultado, efecto), domicilio §3.1–§3.2 y §12.
2. **Habilitadora procedimental** — enlaces que habilitan al proceso sin transformar al objeto participante (agente, instrumento), domicilio §3.3–§3.4.
3. **Invocación procedimental** — enlaces proceso→proceso que delegan control de ejecución al terminar, domicilio §9.
4. **Estructural fundamental** — agregación-participación, exhibición-caracterización, generalización-especialización, clasificación-instanciación, domicilio §8.2.
5. **Estructural etiquetada** — enlaces unidireccionales, bidireccionales o recíprocos con etiqueta textual, domicilio §8.1.

**Regla V-240**: La familia de invocación tiene firma `Proceso → Proceso`, distinta de la firma `Objeto → Proceso` propia de las familias transformadora y habilitadora. Esta distinción de firma justifica el tratamiento como familia autónoma y no como subtipo de habilitación.

**Regla V-241**: Cualquier enlace visible en un OPD conforme pertenece a exactamente una de las cinco familias declaradas. Si una herramienta expone una categoría adicional, debe declararla explícitamente como extensión de implementación, no como familia canónica.

### 3.1 Enlaces transformadores

| Enlace | Dirección gráfica | Decoración fuente | Decoración destino | Semántica |
|---|---|---|---|---|
| Consumo | objeto → proceso | (ninguna) | punta cerrada | El proceso destruye el objeto |
| Resultado | proceso → objeto | (ninguna) | punta cerrada | El proceso crea el objeto |
| Efecto | objeto ↔ proceso | punta cerrada | punta cerrada | El proceso cambia el estado del objeto |

**Regla V-7**: Un enlace de efecto requiere que el objeto tenga al menos un estado definido. [Semántica heredada de `opm-es` §9; aquí se fija la restricción de conectividad gráfica.]

**Regla V-8**: Un enlace de resultado hacia un objeto con estado inicial debe conectar al rectángulo del objeto o a un estado distinto del inicial, nunca directamente al estado inicial. [Semántica heredada de `opm-es` §Resultado hacia un objeto con estado inicial; aquí se fija la restricción de conectividad gráfica.]

**Regla V-115**: Como regla general, todo proceso explícito DEBE transformar (crear, consumir o afectar) al menos un objeto. Los enlaces habilitadores (agente, instrumento) no satisfacen este requisito. Excepción: los procesos persistentes reconocidos por la capa base son válidos cuando el hecho del modelo consiste precisamente en mantener una condición o estado relevante en el tiempo. [Semántica heredada de `opm-es` §9; aquí se fija la restricción mínima de conectividad transformadora.]

### 3.2 Enlaces transformadores con estado especificado

Cuando un enlace parte de o llega a un estado específico dentro del objeto:

| Variante | Geometría |
|---|---|
| Consumo con estado | Flecha desde el estado específico del objeto hacia el proceso |
| Resultado con estado | Flecha desde el proceso hacia el estado específico del objeto |
| Efecto entrada-salida | Flecha de entrada desde el estado-origen hacia el proceso + flecha de salida desde el proceso hacia el estado-destino |
| Efecto solo entrada | Flecha desde el estado-origen hacia el proceso (sin flecha de salida especificada) |
| Efecto solo salida | Flecha desde el proceso hacia el estado-destino (sin flecha de entrada especificada) |

**Regla V-9**: En un efecto solo-entrada sin estado de salida especificado, el destino es el estado por defecto del objeto, o la distribución de probabilidad de estados si no hay defecto.

### 3.3 Enlaces habilitadores

| Enlace | Dirección gráfica | Decoración proceso | Semántica |
|---|---|---|---|
| Agente | agente → proceso | Círculo negro relleno (black lollipop) | Persona que habilita sin ser transformada |
| Instrumento | instrumento → proceso | Círculo blanco vacío (white lollipop) | Objeto inanimado que habilita sin ser transformado |

**Regla V-10**: Si un habilitador deja de existir durante la ejecución, el proceso se detiene y el estado del afectado queda indeterminado. [Semántica heredada de `opm-es` §10; aquí se fija la consecuencia visual: la elipse del proceso deja de exhibir la marca reservada de actividad (V-53), cualquiera sea el canal declarado por la implementación.]

### 3.4 Enlaces habilitadores con estado especificado

El enlace parte del estado específico del agente/instrumento hacia el proceso. El habilitador solo habilita si está en ese estado.

### 3.5 Principio de unicidad del enlace procedimental

**Regla V-11**: Un objeto o estado tiene exactamente un rol respecto de un proceso enlazado: es transformado O habilitador, nunca ambos simultáneamente para el mismo enlace. [Semántica heredada de `opm-es` §9/§10; aquí se fija la restricción de que un solo enlace no puede portar ambos roles gráficamente.]

---

## 4. Modificadores de control

### 4.1 Evento (`e`)

El modificador `e` se coloca sobre los enlaces habilitadores y los transformadores de entrada (consumo, efecto), cerca del extremo del proceso. Semántica: el objeto (o su estado) **inicia** la evaluación de la precondición del proceso.

| Enlace base | + evento = | Geometría adicional |
|---|---|---|
| Consumo | Evento de consumo | Marca `e` sobre el enlace, cerca del proceso |
| Efecto | Evento de efecto | Marca `e` sobre el enlace bidireccional, cerca del proceso |
| Agente | Evento de agente | Marca `e` sobre el enlace con piruleta negra |
| Instrumento | Evento de instrumento | Marca `e` sobre el enlace con piruleta blanca |

**Regla V-12**: El enlace de evento es el segmento desde el objeto/estado hacia el proceso. El segmento desde el proceso hacia el objeto (consumo, efecto) NO es un enlace de evento.

**Regla V-13**: Un evento se pierde tras la evaluación, incluso si la precondición falla. [Semántica heredada de `opm-es` §8.2.1: el evento cesa tras la evaluación.]

### 4.2 Condición (`c`)

El modificador `c` introduce un mecanismo de omisión condicional (*bypass*): si la precondición falla, el proceso se omite y el control pasa al siguiente.

| Enlace base | + condición = | Geometría adicional |
|---|---|---|
| Consumo | Consumo condicional | Marca `c` sobre el enlace |
| Efecto | Efecto condicional | Marca `c` sobre el enlace bidireccional |
| Agente | Agente condicional | Marca `c` sobre el enlace con piruleta negra |
| Instrumento | Instrumento condicional | Marca `c` sobre el enlace con piruleta blanca |

### 4.3 Composición: estado especificado + modificador de control

Los modificadores `e` y `c` se combinan con estado especificado. La geometría resultante: el enlace parte del estado concreto del objeto y lleva la marca `e` o `c` sobre la línea.

### 4.4 Excepción temporal

| Enlace | Marca | Dispara cuando |
|---|---|---|
| Excepción por sobretiempo | `/` (una barra oblicua) | Duración real > duración máxima |
| Excepción por subtiempo | `//` (dos barras oblicuas) | Duración real < duración mínima |

Estos enlaces conectan un proceso fuente con un proceso de manejo de excepción. El proceso de manejo es ambiental (borde discontinuo). A diferencia de los modificadores `e`/`c` (§4.2/§4.3), que anotan un enlace base, la excepción temporal es un **enlace de control autónomo** (firma proceso→proceso), no un modificador; aparece bajo este capítulo por afinidad temática, no porque modifique otro enlace.

---

## 5. Operadores lógicos

### 5.1 AND (conjunción)

**Representación**: Enlaces separados del mismo tipo que no se tocan entre sí. No hay símbolo explícito de AND.

**Regla V-14**: AND es el operador por defecto. Múltiples enlaces del mismo tipo sin arco conector implican AND.

### 5.2 XOR (disyunción exclusiva)

**Representación**: Un arco discontinuo simple sobre el abanico de enlaces, con foco en el extremo convergente.

**Semántica**: Exactamente uno de los enlaces participantes se activa.

### 5.3 OR (disyunción inclusiva)

**Representación**: Dos arcos discontinuos concéntricos sobre el abanico de enlaces.

**Semántica**: Al menos uno de los enlaces participantes se activa.

### 5.4 Reglas de aplicación

**Regla V-15**: XOR y OR aplican a todas las familias de enlaces procedimentales: consumo, resultado, efecto, agente, instrumento e invocación.

**Regla V-16**: El arco se posiciona en el extremo convergente del abanico (el extremo compartido por todos los enlaces).

**Regla V-17**: Un abanico puede ser convergente (múltiples fuentes → un destino) o divergente (una fuente → múltiples destinos).

### 5.5 Combinatoria completa de abanicos

| Familia de enlace | Convergente | Divergente |
|---|---|---|
| Consumo | N objetos → 1 proceso | 1 objeto → N procesos |
| Resultado | N procesos → 1 objeto | 1 proceso → N objetos |
| Efecto | N objetos ↔ 1 proceso | N procesos ↔ 1 objeto |
| Agente | N agentes → 1 proceso | 1 agente → N procesos |
| Instrumento | N instrumentos → 1 proceso | 1 instrumento → N procesos |
| Invocación | N procesos → 1 proceso | 1 proceso → N procesos |

### 5.6 Abanicos con modificadores de control

Los abanicos XOR/OR de enlaces del lado de entrada (consumo, efecto, agente, instrumento) admiten variantes con `e` (evento) y `c` (condición); la marca se coloca sobre cada enlace individual del abanico. Los abanicos de resultado e invocación NO las admiten: el resultado no existe antes del proceso (cfr. §13.5) y la invocación queda fuera del alcance definicional de los modificadores de control (cfr. `reglas-opm-estrictas-es` AP-03/AP-10). La contraparte OR de cualquier XOR se obtiene reemplazando el arco simple por arco doble y la semántica de "exactamente" por "al menos".

### 5.7 Abanicos con estado especificado

Los enlaces del abanico pueden partir de o llegar a estados específicos de los objetos. Cada enlace individual del abanico puede tener o no estado especificado independientemente.

### 5.8 Abanicos probabilísticos

Cada enlace del abanico se anota con `Pr=p`. Las probabilidades de todos los enlaces del abanico deben sumar 1.0. Si no se anotan probabilidades, la probabilidad por defecto es `1/n` donde n es el número de enlaces.

**Regla V-18**: Un abanico probabilístico es siempre XOR — exactamente un enlace se activa por ejecución.

### 5.9 Equivalencia resultado-XOR

**Regla V-19**: Un enlace de resultado simple hacia un objeto con estados es semánticamente equivalente a un abanico XOR de enlaces de resultado con estado especificado, uno por cada estado posible del objeto.

---

## 6. Trayectorias de ejecución y etiquetas de ruta

### 6.1 Definición

Una etiqueta de ruta (path label) es texto colocado sobre un enlace procedimental. Resuelve la ambigüedad cuando un proceso tiene múltiples combinaciones posibles de entrada/salida.

### 6.2 Regla de coincidencia

**Regla V-20**: Al ejecutarse un proceso, se sigue la trayectoria cuya etiqueta de ruta de entrada coincide con la etiqueta de ruta de salida. Todos los enlaces de consumo/resultado con la misma etiqueta forman una trayectoria.

### 6.3 Escenarios

Un escenario es un conjunto de etiquetas de ruta que define una variante concreta de ejecución. Evita crear un OPD adicional por cada variante.

---

## 7. Multiplicidad y cardinalidad

### 7.1 Símbolos de opcionalidad

| Símbolo | Límites | Significado |
|---|---|---|
| `?` | 0..1 | Opcional (cero o una instancia) |
| `*` | 0..* | Opcional, cero a muchos |
| (sin símbolo) | 1..1 | Exactamente uno (por defecto) |
| `+` | 1..* | Al menos uno |

### 7.2 Rangos y expresiones

La multiplicidad soporta:
- Rangos: `3..5`, `8..10`.
- Rangos múltiples separados por coma: `3..5, 8..10`.
- Expresiones aritméticas: `2`, `3*n`.
- Restricciones: `n<=4`, `e >= 1`, `b in {0, 1}`.
- Operadores de restricción: `=`, `!=`, `<`, `<=`, `>=`, `in {conjunto}`.

**Regla V-21**: Los nombres de parámetros de multiplicidad deben ser únicos en todo el modelo.

**Regla V-22**: La multiplicidad se coloca como anotación junto al extremo del enlace o cerca del refinador en relaciones estructurales.

### 7.3 Restricciones de aplicación

**Regla V-23**: La multiplicidad aplica a enlaces etiquetados, agregación-participación y enlaces procedimentales. No aplica a procesos directamente.

---

## 8. Enlaces estructurales

### 8.1 Enlaces etiquetados

| Variante | Geometría | Decoración |
|---|---|---|
| Unidireccional | Línea con punta abierta en destino | Etiqueta itálica sobre la línea |
| Unidireccional sin etiqueta | Línea con punta abierta | Sin etiqueta (semántica: "se relaciona con") |
| Bidireccional | Línea con arpones en ambos extremos | Dos etiquetas (ida y vuelta) |
| Recíproco | Línea con arpones | Una sola etiqueta o sin etiqueta |

**Regla V-56**: Un enlace bidireccional cuyas dos etiquetas son idénticas es semánticamente equivalente a un enlace recíproco con esa misma etiqueta. Ambas representaciones son intercambiables.

### 8.2 Relaciones estructurales fundamentales

| Relación | Símbolo topológico | Dirección vértice→base | Refinable | Refinadores |
|---|---|---|---|---|
| Agregación-participación | Triángulo con interior completamente relleno | Todo → Partes | Todo | Partes |
| Exhibición-caracterización | Triángulo con triángulo interior distinguible | Exhibidor → Rasgos | Exhibidor | Rasgos |
| Generalización-especialización | Triángulo vacío (sin interior distinguible) | General → Especializaciones | General | Especializaciones |
| Clasificación-instanciación | Triángulo con círculo interior distinguible | Clase → Instancias | Clase | Instancias |

### 8.3 Reglas de las relaciones fundamentales

**Regla V-24**: Salvo en exhibición-caracterización, el refinable y los refinadores deben tener la misma perseverancia (ambos objetos o ambos procesos). [Semántica heredada de `opm-es` §12; aquí se fija la restricción de validación gráfica del triángulo.]

**Regla V-25**: Exhibición-caracterización es la única relación estructural que puede conectar objetos con procesos. El rasgo es atributo si es objeto y operación si es proceso. [Semántica heredada de `opm-es` §12.]

**Regla V-26**: Las cuatro combinaciones exhibidor-rasgo son válidas: objeto exhibe atributo, objeto exhibe operación, proceso exhibe atributo, proceso exhibe operación.

**Regla V-27**: Clasificación-instanciación no distingue entre colección completa e incompleta (el número de instancias varía en operación).

**Regla V-57**: Las partes de una agregación pueden ser consumidas, afectadas o producidas de forma independiente sin que el todo sea consumido, afectado o producido. Los enlaces transformadores pueden conectar subprocesos con partes individuales del todo.

### 8.4 Herencia

Las especializaciones heredan del general: todas las partes, todos los rasgos, todos los enlaces estructurales etiquetados, todos los enlaces procedimentales.

**Regla V-28**: Se permite herencia múltiple.

**Regla V-29**: Un atributo discriminante restringe los valores válidos de un atributo para cada especialización. Cada especialización exhibe exactamente un valor del atributo discriminante.

**Regla V-72**: La herencia aplica a través de niveles de refinamiento por despliegue. Cuando un general se despliega en especializaciones, cada especialización hereda automáticamente los enlaces del general en todos los OPDs donde participe.

**Regla V-73**: Los enlaces heredados no son visibles explícitamente en el OPD, pero aplican semánticamente. No se dibujan líneas para enlaces heredados; su efecto se infiere del árbol de generalización-especialización.

**Regla V-74**: Herencia de afiliación: los atributos de objetos ambientales son automáticamente ambientales. Los procesos de entidades ambientales son ambientales. La afiliación se hereda por la cadena estructural.

**Regla V-75**: Sobreescritura: una especialización puede reemplazar un participante heredado con una especialización diferente del mismo participante.

**Regla V-76**: Migración de enlaces comunes: al crear un general a partir de especializaciones existentes, los enlaces comunes a todas las especializaciones se mueven al general.

**Regla V-58**: En clasificación-instanciación, la clase muestra atributos con rangos de valores (estados de rango como `120..240`); la instancia muestra los mismos atributos con valores concretos (estados de valor como `185`). La instancia se nombra con el formato `NombreInstancia : NombreClase`.

### 8.5 Enlaces estructurales con estado especificado

Tres familias por posición de la especificación de estado:

| Posición | Geometría |
|---|---|
| Estado en origen | El enlace parte de un estado específico del objeto origen |
| Estado en destino | El enlace llega a un estado específico del objeto destino |
| Estado en origen y destino | Ambos extremos conectan a estados específicos |

**Regla V-30**: Las variantes bidireccional y recíproco NO existen para el caso de estado solo en destino.

---

## 9. Enlaces de invocación

### 9.1 Tipos

| Enlace | Geometría | Semántica |
|---|---|---|
| Invocación | Línea en zigzag (rayo) con punta, proceso → proceso | Al terminar, el proceso invocante inicia el invocado |
| Auto-invocación | Zigzag que sale y regresa al mismo proceso (bucle) | El proceso se invoca a sí mismo al terminar |

La invocación constituye la tercera familia canónica de enlaces procedimentales (V-239), con firma `Proceso → Proceso` distinta de las otras familias (V-240).

### 9.2 Invocación implícita

Dentro de un proceso descompuesto, la invocación se determina por posición vertical:

**Regla V-31**: La terminación de un subproceso invoca al subproceso inmediatamente inferior (cuyo punto superior de elipse está debajo). No hay enlace explícito. [Semántica heredada de `opm-es` §14; aquí se fija la regla de invocación posicional.]

**Regla V-32**: Subprocesos cuyos puntos superiores de elipse están a la misma altura se ejecutan en paralelo. El último en terminar inicia al siguiente nivel. [Semántica heredada de `opm-es` §14; aquí se fija la regla de paralelismo posicional.]

**Regla V-77**: La invocación implícita por posición vertical (V-31, V-32) solo aplica a descomposición de proceso (`process in-zooming`). En descomposición de objeto no hay orden temporal entre componentes.

**Regla V-78**: En descomposición de objeto, la posición espacial de los componentes codifica disposición semántica: ubicación física (componentes en una sala), organización lógica (secciones de un artículo, campos de un registro), pero no invocación temporal.

### 9.3 Activación asincrónica por eventos

**Regla V-59**: Cuando subprocesos dentro de una descomposición son activados individualmente por enlaces de evento desde estados distintos de un objeto, se ejecutan de forma asincrónica e independiente. No hay orden secuencial ni paralelo entre ellos: cada subproceso se activa exclusivamente cuando ocurre su evento correspondiente. Este patrón modela sistemas reactivos donde los subprocesos compiten por activación según el estado del entorno.

---

## 10.1 Gestión de contexto y refinamiento — Mecanismos de refinamiento y abstracción

Esta versión amplía el esquema vigente de tres pares intra-modelo a cuatro pares canónicos, añadiendo composición inter-modelo.

| Par | Refinamiento | Abstracción |
|---|---|---|
| Estados | Expresión de estados | Supresión de estados |
| Estructura | Despliegue (`unfolding`) | Plegado (`folding`) |
| Comportamiento | Descomposición (`in-zooming`) | Recomposición (`out-zooming`) |
| Composición inter-modelo | Sub-model referenciado | Desconexión de sub-model |

**Regla V-242**: La composición inter-modelo por sub-model es un mecanismo de refinamiento explícito. Se añade a los tres mecanismos clásicos intra-modelo porque cruza la frontera del modelo OPM como unidad de serialización, introduce identidad persistente de vínculo y requiere gobernanza propia documentada en §23.

**Regla V-243**: Operaciones como `bring connected things`, `bring links between selected entities` o equivalentes son operadores derivados que materializan enlaces o cosas ya existentes en el modelo sobre un OPD distinto. No constituyen mecanismos de refinamiento ontológico y se regulan en §26.

## 10.2 Despliegue en el mismo diagrama

El refinable y los refinadores comparten OPD, unidos por enlaces estructurales fundamentales.

## 10.3 Descomposición en nuevo diagrama (`in-zooming`)

**Regla V-33**: El refinable aparece con contorno grueso tanto en el OPD padre como en el OPD hijo.

**Regla V-62**: La descomposición en nuevo diagrama (`in-zooming`) se ejecuta en dos fases: (1) Mostrar Contenido — muestra el contenido interno del refinable, produciendo un OPD semidescompuesto; (2) Refinar Enlaces — refina los enlaces del OPD padre distribuyéndolos a los subprocesos, produciendo el OPD hijo (SDn+1). La recomposición (`out-zooming`) es el inverso: (1) Abstraer Enlaces — abstrae los enlaces de los subprocesos; (2) Ocultar Contenido — oculta el contenido interno, restaurando el OPD padre (SDn).

## 10.3b Contenedor y elementos externos

Al crear un OPD hijo por descomposición (`in-zooming`) o despliegue (`unfolding`), los elementos del OPD padre se clasifican en internos y externos:

**Regla V-79**: En el OPD hijo, la cosa refinada aparece como **contenedor** (elemento interno). En descomposición de proceso la elipse se agranda para contener subprocesos; en descomposición de objeto el rectángulo se agranda para contener componentes.

**Regla V-80**: Las cosas conectadas al refinado vía enlaces en el OPD padre se copian como **elementos externos** en el OPD hijo. Un elemento externo mantiene sus propiedades (esencia, contorno, estados) pero su posición se recalcula.

**Regla V-81**: En la descomposición, se copian al OPD hijo **todas** las cosas conectadas vía cualquier enlace a la cosa refinada que tengan apariencia en el OPD padre.

**Regla V-82**: En el despliegue, se copian al OPD hijo **solo** los hijos estructurales directos (destinos de agregación y exhibición).

**Regla V-83**: No se puede refinar un elemento externo (apariencia con internal=false). Solo el contenedor es refinable en su propio OPD hijo.

**Regla V-84**: Objetos internos — creados dentro de una descomposición, sin apariencia en el OPD padre — se eliminan cuando el proceso padre se elimina (cascada). La eliminación de la cosa refinada elimina el OPD hijo y todos sus contenidos.

**Regla V-85**: Objetos externos — creados en el SD u otro OPD superior — existen independientemente del refinamiento y son referenciables desde cualquier OPD del modelo.

## 10.4 Descomposición de proceso

**Regla V-34**: La elipse del proceso refinable se agranda para contener los subprocesos como elipses menores.

**Regla V-35**: La línea temporal fluye de arriba hacia abajo. La posición vertical determina la secuencia de ejecución.

## 10.5 Descomposición de objeto

El rectángulo del objeto refinable se agranda para mostrar objetos constituyentes.

## 10.6 Supresión de estados

Para simplificar un OPD, se pueden ocultar estados no relevantes. Se indica con el símbolo de supresión (`...` en un rectángulo redondeado en la esquina inferior derecha del objeto).

**Regla V-86**: Un estado `s` de una cosa T se suprime en el OPD padre cuando: existe un OPD hijo de descomposición donde T aparece como externo y existe un enlace entre T y la cosa refinada que referencia `s` como estado de origen o de destino. La supresión se computa bajo demanda, no se almacena.

**Regla V-87**: La supresión de estados solo aplica a descomposición, no a despliegue.

**Regla V-88**: Estados no referenciados en enlaces a la cosa refinada NO se suprimen — permanecen visibles en el OPD padre.

**Regla V-89**: Cuando existen múltiples OPDs hijo de descomposición que suprimen estados del mismo objeto, el conjunto de estados suprimidos es la unión de los estados suprimidos por cada OPD hijo.

**Regla V-90**: Expresión de estados: los estados suprimidos en el OPD padre (SDn) se revelan en el OPD hijo (SDn+1) vinculados a subprocesos específicos. Este es el mecanismo inverso de la supresión.

## 10.7 Simplificación de OPD

Un subconjunto de subprocesos puede reagruparse en un nuevo proceso compacto mediante recomposición, generando un OPD simplificado con menos niveles.

## 10.8 Visibilidad de enlaces en OPD hijo

**Regla V-91**: Los enlaces **estructurales** al contenedor son visibles en el OPD hijo; definen la estructura del despliegue o de la descomposición.

**Regla V-92**: Los enlaces **procedimentales** al contenedor NO son visibles directamente en el OPD hijo — se distribuyen a subprocesos (§11) o se filtran.

**Regla V-93**: Los enlaces entre elementos internos del OPD hijo son visibles normalmente.

**Regla V-94**: Los enlaces que no tocan el contenedor ni ningún elemento interno del OPD hijo son invisibles en ese OPD.

## 10.9 Propiedades invariantes entre niveles

Las siguientes propiedades son inmutables a través de todos los niveles de refinamiento:

**Regla V-95**: La **esencia** (física/informacional) no cambia a través del refinamiento. Es una propiedad estática de la cosa.

**Regla V-96**: La **perseverancia** (persistente/transitoria) no cambia a través del refinamiento. Está determinada por el tipo: los objetos son persistentes, los procesos son transitorios.

**Regla V-97**: Los **nombres** no cambian a través del refinamiento. La convención de capitalización se mantiene consistente en todos los OPDs del modelo.

**Regla V-98**: **Consistencia de hechos del modelo**: un hecho afirmado en un OPD no puede contradecir un hecho afirmado en otro OPD. El refinamiento o la abstracción de hechos no constituye contradicción.

**Regla V-99**: **Importancia proporcional**: la importancia relativa de una cosa es proporcional al OPD más alto de la jerarquía donde aparece. Cosas que aparecen en SD son más importantes que las que aparecen solo en SDn.

## 10.10 Prohibición de refinamiento cíclico

**Regla V-100**: No se puede refinar una cosa desde dentro de su propio árbol de refinamiento. El chequeo es **transitivo**: se verifica toda la cadena de ancestros del OPD. Esto previene loops infinitos en la jerarquía de OPDs.

## 10.11 Instancias visuales entre OPDs

**Regla V-101**: Instancia visual ≠ instancia lógica. Una instancia visual es la misma entidad del modelo mostrada en un OPD diferente (misma identidad, diferente vista). Una instancia lógica es una relación de clasificación o herencia (entidad diferente).

**Regla V-102**: No se puede crear una instancia visual entre tipos diferentes: un objeto no puede ser instancia visual de un proceso, ni viceversa.

## 10.12 Semi-plegado (compresión parcial de estructura)

El semi-plegado es un mecanismo de visualización intermedio entre el plegado completo y el despliegue completo de una relación estructural. Permite mostrar la existencia de refinadores sin expandirlos completamente. No existe plantilla OPL-ES canónica para el semi-plegado; su expresión es exclusivamente visual.

**Regla V-116**: En una relación de agregación-participación, los refinadores (partes) pueden mostrarse como íconos de triángulo con el nombre de la parte dentro del rectángulo del todo (refinable), en lugar de como entidades separadas conectadas por enlaces estructurales explícitos. Esta representación compacta es el semi-plegado.

**Regla V-117**: El semi-plegado es por refinador: algunos refinadores pueden estar semi-plegados (dentro del rectángulo del todo) mientras otros permanecen extraídos (fuera, con enlace estructural explícito visible). No es necesariamente todo-o-nada.

**Regla V-118**: Cuando hay refinadores semi-plegados y otros extraídos, un indicador numérico junto al triángulo de agregación muestra cuántos refinadores permanecen **ocultos** dentro del semi-plegado — no el total de refinadores.

**Regla V-119**: El estado de semi-plegado es por apariencia (por OPD): un objeto puede estar semi-plegado en un OPD y completamente desplegado en otro. Son vistas independientes del mismo hecho estructural.

**Regla V-120**: Los enlaces procedimentales pueden conectarse directamente a un refinador semi-plegado dentro del rectángulo del todo. Visualmente, la flecha entra al borde del rectángulo padre y apunta al nombre del refinador semi-plegado.

---

## 11. Distribución de enlaces

### 11.1 Regla general

**Regla V-36**: Los enlaces conectados al contorno exterior de un proceso descompuesto se interpretan distributivamente. Las familias que se distribuyen a todos los subprocesos son efecto básico, agente e instrumento (cfr. V-104); consumo y resultado se rigen por V-37/V-103 (prohibidos en el contorno exterior, migran al primer/último subproceso); los enlaces estructurales no se distribuyen (V-105). [Semántica heredada de `opm-es` §14.2.2.4; aquí se fija la distribución gráfica de enlaces en descomposición.]

### 11.2 Distribución por tipo de enlace

Cuando un proceso se descompone en subprocesos, los enlaces procedimentales del padre se distribuyen según su tipo:

| Tipo de enlace | Destino de distribución | Justificación |
|---|---|---|
| Consumo (incluye enlace de entrada) | **Primer** subproceso (posición Y mínima) | El consumo ocurre al inicio |
| Resultado (incluye enlace de salida) | **Último** subproceso (posición Y máxima) | La producción ocurre al final |
| Agente, Instrumento | **Todos** los subprocesos | Habilitador distribuido |
| Efecto (básico, sin estado especificado) | **Todos** los subprocesos | Afecta a todos; pero ver V-40 para efecto con estado especificado (enlace escindido) |
| Estructural (agregación, etc.) | **No se distribuye** — permanece en contenedor | Invariante temporal |

**Regla V-103**: Los enlaces de consumo e input se distribuyen al primer subproceso en orden de posición vertical (Y mínimo). Los de resultado y output, al último subproceso (Y máximo). [Semántica heredada de `opm-es` §14.2.2; aquí se fija la distribución posicional de enlaces transformadores.]

**Regla V-104**: Los enlaces de efecto **básico** (sin estado especificado) se distribuyen a todos los subprocesos, al igual que los de agente e instrumento (la distribución a todos los subprocesos es idéntica en resultado pero distinta en razón: el efecto hereda la afectación del padre, mientras que agente e instrumento aplican individualmente a cada subproceso). Cuando el efecto tiene estado especificado (entrada-salida), la distribución se realiza mediante **enlace escindido**: un subproceso temprano saca del estado de entrada y un subproceso tardío pone en el estado de salida (cfr. V-40). [Semántica heredada de `opm-es` §14.2.2; aquí se fija la distribución gráfica de enlaces de efecto.]

**Regla V-105**: Los enlaces estructurales NO se distribuyen — permanecen asociados al contenedor.

**Regla V-106**: Si no hay subprocesos aún dentro de la descomposición, el enlace se muestra conectado al contenedor directamente como respaldo temporal.

**Regla V-107**: La distribución de enlaces solo aplica a descomposición. El despliegue no tiene distribución de enlaces.

### 11.3 Restricciones de distribución

**Regla V-37**: Los enlaces de consumo y resultado NO deben conectarse al contorno exterior de un proceso descompuesto. Deben conectarse directamente al subproceso específico que consume o produce. [Semántica heredada de `opm-es` §14; aquí se fija la restricción de frontera para enlaces transformadores.]

**Regla V-38**: Los enlaces de evento desde objetos sistémicos no deben cruzar el límite de la descomposición para iniciar subprocesos. [Semántica heredada de `opm-es` §14.2.2.4.2; aquí se fija la restricción de cruce de frontera para eventos sistémicos.]

**Regla V-108**: Los enlaces de evento desde objetos **ambientales** pueden cruzar el límite de la descomposición si se modela contingencia explícita. Esta es una excepción a V-38.

**Regla V-39**: Si un enlace de condición causa que un subproceso se omita, el control pasa al siguiente subproceso en la secuencia. [Semántica heredada de `opm-es` §14; aquí se fija el comportamiento visual de omisión condicional.]

**Regla V-109**: Las restricciones de frontera (V-37, V-38, V-39) aplican solo a descomposición, no a despliegue.

---

## 12. Enlaces transformadores escindidos

### 12.1 Problema

Cuando un enlace de efecto entrada-salida (`P cambia A de s1 a s2`) se descompone en subprocesos, queda subespecificado: no se sabe qué subproceso saca al objeto del estado de entrada ni cuál lo coloca en el de salida.

### 12.2 Solución: par escindido

**Regla V-40**: El enlace se escinde en dos:
- El subproceso **temprano** recibe la flecha de entrada (saca al objeto de s1).
- El subproceso **tardío** recibe la flecha de salida (coloca al objeto en s2).

**Regla V-41**: No existen versiones con modificador de control de los enlaces escindidos. [Semántica heredada de `opm-es` §14; aquí se fija la restricción gráfica.]

**Regla V-110**: La escisión es el **único** mecanismo para resolver la subespecificación de enlaces de efecto entrada-salida en descomposición. No hay alternativa.

### 12.3 Cambio de rol con la abstracción

**Regla V-42**: Un objeto puede ser instrumento en un nivel abstracto y afectado en un nivel detallado. Esto es válido si a nivel abstracto los estados inicial y final del objeto coinciden. [Semántica heredada de `opm-es` §14.2.2.4.3; aquí se fija la validación gráfica del cambio de rol entre niveles.]

**Regla V-111**: En el OPD hijo (nivel detallado), el objeto con cambio de rol muestra estados intermedios que no son visibles en el OPD padre. Ejemplo canónico: `Dishwasher` es instrumento en SD (sin cambio de estado aparente) y afectado en SD1 (`empty → loaded → empty`). Es válido porque `empty = empty` entre niveles. [Semántica heredada de `opm-es` §14.2.2.4.3; aquí se fija la visualización de estados intermedios en cambio de rol.]

**Regla V-112**: El cambio de rol solo aplica a descomposición, no a despliegue. [Semántica heredada de `opm-es` §14.2.2.4.3; aquí se fija la restricción de alcance del cambio de rol.]

---

## 13. Precedencia de enlaces durante la recomposición

### 13.1 Matriz de precedencia transformadora

Al recomponer subprocesos en un proceso padre, si dos subprocesos tienen enlaces distintos hacia el mismo objeto, la fuerza semántica determina cuál prevalece:

| B↔P1 \ B↔P2 | Efecto | Resultado | Consumo |
|---|---|---|---|
| **Efecto** | Efecto | Resultado | Consumo |
| **Resultado** | Resultado | **Inválido** | Efecto |
| **Consumo** | Consumo | Efecto | **Inválido** |

**Regla V-43**: Resultado + consumo sobre el mismo objeto es inválido (no se puede crear y destruir como el mismo hecho abstracto). Resultado + resultado y consumo + consumo también son inválidos. [Semántica heredada de `opm-es` §14.2.4; aquí se fija la restricción de validación gráfica de conflicto de enlaces.]

### 13.2 Precedencia entre transformadores y habilitadores

**Regla V-44**: Un enlace transformador siempre prevalece sobre un enlace habilitador al recomponer. [Semántica heredada de `opm-es` §14.2.4; aquí se fija la regla de precedencia gráfica.]

### 13.3 Orden principal de precedencia

```
consumo = resultado > efecto > agente > instrumento
```

### 13.4 Precedencia secundaria por modificador de control

Dentro de cada clase de enlace:

```
evento > sin control > condición
```

### 13.5 Orden completo de fuerza semántica (12 niveles)

Referencia de capa base: `opm-es` §14.2.4.5.

| Nivel | Enlace |
|---|---|
| 1 | Evento de consumo |
| 2 | Consumo = Resultado |
| 3 | Condición de consumo |
| 4 | Evento de efecto |
| 5 | Efecto |
| 6 | Condición de efecto |
| 7 | Evento de agente |
| 8 | Agente |
| 9 | Condición de agente |
| 10 | Evento de instrumento |
| 11 | Instrumento |
| 12 | Condición de instrumento |

Notas:

- Consumo y resultado tienen la misma fuerza (nivel 2) porque §13.3 los declara iguales. En los niveles con modificador de control (1 y 3), solo existe la variante de consumo: **no existen "evento de resultado" ni "condición de resultado"**. La razón es que el resultado no existe antes del proceso, pues es creado por él, por lo que no puede ser precondición ni disparador.
- **Condición de instrumento** (nivel 12) es el enlace más débil del sistema. Existe como variante válida (cfr. `opm-opl-es` §7.2 CH2, §7.3 CS6) aunque raramente aparece en modelos típicos.
- La condición debilita; el evento fortalece.

---

## 14. Propiedades de duración de proceso

### 14.1 Propiedades

| Propiedad | Descripción |
|---|---|
| Duración | Tiempo real transcurrido en ejecución |
| Duración mínima | Tiempo mínimo permitido |
| Duración esperada | Media estadística |
| Duración máxima | Tiempo máximo permitido |
| Distribución de duración | Función probabilística: normal, uniforme, exponencial, etc. |

### 14.2 Representación gráfica

**Regla V-45**: Los valores de duración se muestran dentro de la elipse del proceso, bajo el nombre y la unidad temporal. Formato: `[unidad] {min, esperada, max} {distribución, parámetros}`.

### 14.3 Unidades temporales válidas

`ms`, `sec`, `min`, `hour`, `day`, `week`, `month`, `year`.

---

## 15. Etiquetas OPD y navegación

### 15.1 Etiquetado del árbol de procesos

**Regla V-46**: El SD (System Diagram) contiene exactamente un proceso sistémico. Puede contener procesos ambientales.

Convención de etiquetas: `SD` → `SD1` → `SD1.1` → `SD1.1.1`, etc.

Esta convención es una **proyección humana del orden de navegación** del árbol (ver §15.5). No constituye identidad persistente del OPD.

### 15.2 Árbol de procesos OPD

Raíz en `SD`. Cada nodo corresponde a un OPD creado por descomposición de un proceso. Es el mecanismo principal de navegación del modelo.

### 15.3 Árbol de objetos OPD

Raíz en un objeto. Muestra su elaboración por refinamiento (exhibición, agregación, etc.).

### 15.4 Categorías de OPD y restricciones del árbol

**Regla V-114 (reescrita)**: El árbol de OPDs de un modelo admite tres categorías distintas y mutuamente excluyentes:

| Categoría | Definición |
|---|---|
| OPD jerárquico | Nace por refinamiento de una cosa del modelo (in-zooming u unfolding). Participa del árbol por relación padre-hijo derivada de refinamiento. |
| OPD de vista anclada | Vive en el árbol por posición, pero no por refinamiento. Incluye: `Vista de Sub-modelo` (§23), `Mapa del Sistema` como índice navegable por miniaturas o equivalentes, `Vista de Requisitos` (§19.7) y otras vistas tipificadas por la implementación. |
| OPD de vista ad hoc | Colección editorial transitoria no anclada al árbol jerárquico ni a una vista tipificada. No participa de refinamiento. |

**Regla V-244**: Las tres categorías admiten reglas distintas de creación, eliminación y navegación. La implementación debe declarar en su metadato a qué categoría pertenece cada OPD del modelo.

**Regla V-245**: Eliminabilidad por categoría:

- OPD jerárquico: solo es eliminable si es hoja del subárbol jerárquico.
- OPD de vista anclada: eliminable según la política del tipo de vista; una vista tipificada puede ser regenerable por su fuente.
- OPD de vista ad hoc: eliminable libremente sin afectar la jerarquía.

**Regla V-113 (revisada)**: Solo los OPDs jerárquicos **hoja** son eliminables directamente del árbol jerárquico. Los nodos jerárquicos internos quedan protegidos para preservar la integridad del refinamiento. Las vistas ancladas y ad hoc se eliminan por las reglas propias de su tipo.

### 15.5 Identidad estable del OPD

Esta sección separa explícitamente los tres canales que la coordenada vertical de un subproceso y la etiqueta `SDx.y` habían estado codificando simultáneamente.

**Regla V-246**: Todo OPD conforme distingue operacionalmente tres canales:

- **Orden temporal**: derivado de la coordenada vertical de los subprocesos dentro de una descomposición (§10.4, V-35, V-55);
- **Orden de navegación**: posición del OPD en el árbol (hermano anterior, siguiente, padre, hijo);
- **Identidad persistente**: identificador estable asignado al OPD y usado como ancla de referencia cruzada externa.

**Regla V-247**: La etiqueta `SDx.y` es una proyección humana del **orden de navegación** combinada con la profundidad del árbol. No es identificador persistente. Puede mutar bajo reordenamiento de hermanos o inserción/eliminación de nodos.

**Regla V-248**: Toda implementación conforme DEBE asignar a cada OPD un identificador persistente, estable bajo reordenamiento del árbol y bajo renumeración de etiquetas. La forma concreta (UUID, slug persistente, URI) es elección de implementación, pero la serialización del modelo debe preservarlo.

**Regla V-249**: Toda referencia externa al modelo que cite un OPD concreto (documentos, trazabilidad de requisitos, tests) DEBE usar el identificador persistente de V-248 y no `SDx.y`. La SSOT no admite como referencia estable ninguna designación derivada del layout.

**Regla V-250**: El producto del acoplamiento entre la coordenada vertical del canvas, el orden en OPL y la posición del árbol es un rasgo operacional del sistema. La SSOT lo reconoce como acoplamiento **de proyección**, no como acoplamiento **de identidad**: los tres canales pueden derivarse coherentemente del layout, pero ninguno sustituye al identificador persistente.

---

## 16. Rotulado y buenas prácticas

### 16.1 Reglas de rotulado

La política de denominación del corpus no vive en esta capa. Los nombres canónicos de objetos, procesos, estados y etiquetas pertenecen a [OPL-ES](urn:fxsl:kb:opl-es) y, cuando afectan decisiones de modelado, a [Manual metodológico de OPM](urn:fxsl:kb:manual-metodologico-opm-es).

En la capa visual solo aplican las siguientes reglas de rotulado:

- el rótulo debe ser legible dentro del contenedor visual sin introducir ambigüedad geométrica;
- un alias decorativo PUEDE mostrarse entre paréntesis junto al nombre para referencia compacta en visualizaciones o anotaciones;
- el texto del estado siempre se renderiza dentro del objeto propietario, nunca como entidad flotante.

**Regla V-47**: La unicidad nominal se evalúa a nivel de modelo, pero toda apariencia visual DEBE renderizarse sin ambigüedad respecto de la cosa a la que refiere.

**Regla V-121**: La convención léxica concreta del nombre del proceso se hereda de la capa textual activa del corpus; esta capa visual no introduce una política paralela.

**Regla V-122**: Una cosa puede mostrar un **alias** breve junto al nombre entre paréntesis, por ejemplo `Sistema de Turborreactor (str)`. La decisión de definir ese alias y su política de uso no pertenecen a esta capa visual. Las llaves `{alias}` se reservan exclusivamente al binding computacional regulado por §20.

**Regla V-48**: [Eliminada — contenido absorbido por V-4. Toda referencia externa a V-48 debe redirigirse a V-4.]

**Regla V-49**: El objeto consumido desaparece al inicio del proceso, no al final. [Semántica heredada de `opm-es` §9; aquí se fija la temporalidad de la animación visual.]

**Regla V-194**: El rótulo visible de una cosa debe permanecer íntegro en el canon-diagrama. No se admite truncamiento con elipsis ni corte silencioso del nombre como forma final de render canónico.

**Regla V-195**: El rótulo debe permanecer inscrito dentro del bounding box visible de la cosa, salvo en estilos explícitamente tipificados por la implementación y documentados como variante no por defecto.

### 16.2 Límites de complejidad por OPD

**Regla V-50**: La legibilidad visual de un OPD exige no más de 20-25 cosas por contexto (aproximadamente una página o pantalla utilizable).

**Regla V-51**: No debe haber oclusión entre cosas. Los enlaces no deben atravesar áreas ocupadas por cosas. Minimizar cruces.

La política metodológica sobre cuándo dividir un OPD por complejidad pertenece a `metodologia-opm-es`.

### 16.3 Principio de representación

**Regla V-52**: Cualquier elemento del modelo puede aparecer en cualquier número de OPDs. Solo deben incluirse los elementos necesarios para el aspecto que se muestra.

**Regla V-123 (reescrita) — existencia, apariencia local y referencia externa**: Toda cosa en un modelo OPM tiene **existencia única** dentro del modelo que la declara como propietario. La existencia determina nombre, esencia y conjunto de estados, y se hereda por todas las apariencias locales en OPDs del mismo modelo.

Una cosa puede además tener **apariencia local** en múltiples OPDs del mismo modelo (V-52) y **referencia externa** desde sub-modelos que la usan sin poseer su existencia (§23, V-184).

| Concepto | Dónde vive | Qué codifica |
|---|---|---|
| Existencia | Un modelo único propietario | Identidad, nombre canónico, esencia, estados |
| Apariencia local | Múltiples OPDs del mismo modelo | Vista geométrica específica |
| Referencia externa | Sub-modelos que la usan | Préstamo sin cambio de propiedad |

Eliminar una apariencia de un OPD no elimina la cosa del modelo; eliminar la cosa del modelo elimina todas sus apariencias en todos los OPDs. Las propiedades de la cosa (nombre, esencia, estados) se definen a nivel de existencia.

Las consecuencias del régimen cross-model para el render y la serialización se desarrollan en §18.7 y §23.

### 16.4 Grid y layout mecánico

La grilla, el snap y las guías dinámicas pertenecen a la mecánica de edición del canvas, no a la gramática nuclear del modelo.

**Regla V-196**: La grid del canvas es decoración opcional de edición. No pertenece al modelo OPM y debe suprimirse en exportaciones canónicas.

**Regla V-197**: El snap a grid es transparente al modelo. Dos OPDs con idéntica topología y diferencias de posicionamiento explicables solo por cuantización a grid se consideran visualmente equivalentes.

**Regla V-198**: Si la implementación ofrece smart-guides o líneas temporales de alineación, debe usar un canal visual reservado a UI. No puede reutilizar sin distinción el patrón discontinuo reservado a afiliación ambiental.

**Regla V-199**: La implementación debe auto-ajustar el viewport al exportar para evitar símbolos huérfanos recortados por el borde del artefacto.

---

## 17. Ejecución y simulación

La semántica operacional completa de ejecución sigue perteneciendo a `metodologia-opm-es`. Esta sección fija únicamente qué marcas visuales son conformes cuando el OPD se presenta en modo de simulación o como snapshot de runtime.

### 17.1 Proceso activo

**Regla V-53 (revisada)**: Un proceso en ejecución DEBE exhibir una marca visual reservada de actividad, distinta de cualquier otra marca persistente de la gramática, en especial del contorno grueso de refinamiento.

La implementación puede materializar la marca de proceso activo por cualquiera de estos tres canales:

- relleno sólido reservado;
- contorno reforzado en color reservado;
- halo externo reservado.

**Regla V-132**: El canal visual reservado al proceso activo no puede coincidir exactamente con el canal del refinable definido por V-33 y V-69. Si una implementación usa ambos como contornos reforzados, DEBE diferenciar color, halo o distintivo auxiliar.

### 17.2 Estado actual

**Regla V-54 (revisada)**: El estado actual durante simulación se marca con un glifo externo reservado al borde del estado, distinto del borde grueso de estado inicial, del doble borde de estado final y de la flecha diagonal de estado por defecto.

**Regla V-133**: El glifo recomendado para estado actual es un pin o gota externa anclada al borde del rectángulo redondeado del estado. Cualquier implementación que use un glifo distinto debe preservar la misma separación visual respecto de las designaciones persistentes de §2.2, incluida `Current` declarada.

**Regla V-134**: `Current` como designación persistente (§2.2, V-237) y la marca de estado actual de runtime (V-54) pueden coincidir visualmente, pero la serialización del modelo DEBE distinguirlas. Una herramienta que reutilice el mismo glifo para ambos DEBE exponer, en el metadato recuperable del modelo, el origen de la marca (declaración persistente vs inducción por runtime).

### 17.3 Tokens y marcas transitorias de flujo

**Regla V-135**: Un enlace activo puede mostrar un token transitorio de flujo durante simulación. Ese token no forma parte de la gramática estática del OPD y no debe confundirse con piruletas, handles o puntos de anclaje.

**Regla V-136**: Los tokens transitorios de flujo son marcadores de runtime. No pertenecen al canon-diagrama salvo que el export se declare explícitamente como snapshot de simulación. En un canon-diagrama ordinario deben omitirse.

### 17.4 Estados operacionales del proceso

**Regla V-137**: La implementación puede distinguir, además del estado activo, otros estados operacionales del proceso durante simulación, como suspendido esperando input o completado recientemente. Si lo hace, debe usar marcas reservadas distintas de las de §17.1 y §17.2.

**Regla V-138**: Un proceso suspendido esperando input externo no puede ser visualmente indistinguible de un proceso inactivo si el artefacto se presenta como snapshot de simulación. Debe exhibir una marca propia o un distintivo de modo equivalente.

### 17.5 Modos de simulación

**Regla V-55 (revisada)**: El tiempo fluye de arriba hacia abajo dentro de la descomposición de un proceso. Las posiciones verticales de los subprocesos determinan el orden temporal. Esta regla rige tanto en edición como en simulación.

**Regla V-139**: En modo síncrono la simulación puede exhibir como máximo una marca de proceso activo por **hilo de ejecución visible** — entendido como la secuencia de subprocesos consecutivos invocados implícitamente por posición vertical dentro de un mismo padre descompuesto (§11.2, V-59). En modo asíncrono pueden coexistir múltiples procesos activos si la estructura del OPD los habilita por paralelismo.

**Regla V-140**: El modo headless o equivalente pertenece al ecosistema de simulación, no a la gramática visible del OPD. La ausencia de animación o de marcas runtime en ese modo no altera la semántica estática del diagrama.

### 17.6 Identificación del snapshot

**Regla V-141**: Todo export que pretenda representar un estado de simulación debe declararlo explícitamente como snapshot de runtime. Si no existe esa declaración, el artefacto se interpreta como canon-diagrama estático.

---

## 18. Estructura del metamodelo OPM

Esta sección formaliza la estructura reflexiva del metamodelo OPM dentro de esta adaptación. Define cómo se compone un modelo OPM, la dualidad gráfico-textual, los conceptos de objeto específico de estado y las consecuencias de la composición inter-modelo para la identidad de las cosas.

### 18.1 Composición del modelo OPM

**Regla V-64 (reescrita)**: Un modelo OPM especifica un sistema. Se compone de:

- un conjunto de OPDs (`1..*`);
- una especificación OPL (`1..*` párrafos OPL);
- opcionalmente, un conjunto de referencias a otros modelos OPM como sub-modelos (`0..*`, ver §23).

El conjunto de OPDs y la especificación OPL son duales dentro del modelo: el conjunto de OPDs especifica gráficamente lo que la especificación OPL especifica textualmente, y viceversa. Cuando el modelo referencia sub-modelos, la dualidad OPD↔OPL se preserva íntegramente **dentro** de cada modelo individual y se regula explícitamente **a través** de fronteras de modelo según §23.

**Regla V-251**: La clausura OPD↔OPL es local al modelo. El compuesto resultante es un grafo dirigido acíclico de modelos conectados por referencia, con cada modelo localmente autocontenido.

### 18.2 Dualidad OPD–OPL

**Regla V-65**: Cada OPD tiene su contraparte en un párrafo OPL. Cada constructo OPD tiene su contraparte en una o más oraciones OPL. La dualidad es bidireccional: toda afirmación en un OPD debe ser reproducible como OPL, y toda oración OPL debe ser representable como constructo OPD.

### 18.3 Construcción del OPD Construct

**Regla V-66**: La construcción de un constructo OPD es el proceso *Conectar*, que toma un conjunto de cosas en estado `desconectado` y un conjunto de enlaces como instrumento, y produce un conjunto de cosas en estado `conectado`. La cardinalidad del conjunto de enlaces puede ser `1` (constructo básico) o `≥ 2` (constructo compuesto). La cardinalidad del conjunto de cosas puede ser `2` (básico) o `≥ 3` (compuesto).

### 18.4 Objetos con y sin estados

**Regla V-67**: Todo objeto exhibe un conjunto de estados. Si el tamaño del conjunto de estados es `s = 0`, el objeto es sin estados. Si `s ≥ 1`, el objeto es con estados. Un objeto con estados que tiene `s` estados deriva un conjunto de objetos específicos de estado que contiene exactamente `s` objetos específicos de estado. Cada objeto específico de estado refiere a exactamente un estado del objeto original.

### 18.5 Denominación de instancias específicas de estado

**Regla V-68**: Un objeto específico de estado se nombra concatenando el nombre del estado con el nombre del objeto original (ej.: `Producto Diseñado` para el estado `diseñado` de `Producto`). Este patrón permite referenciar un objeto restringido a un estado particular como entidad independiente en OPL y en enlaces procedimentales.

### 18.6 Nota editorial sobre precedencia

La precedencia entre enlaces transformadores y habilitadores ya queda formalizada en las reglas V-43 y V-44 de la sección 13, por lo que no se necesita una tabla adicional en esta adaptación.

### 18.7 Apariencia, existencia y referencia externa

Esta subsección desarrolla las consecuencias del régimen cross-model para el render y la serialización de cosas referenciadas, complementando V-123 (§16.3).

**Regla V-252**: Toda cosa cuya existencia pueda ser referenciada desde otro modelo DEBE exponer un URI o handle persistente en la serialización del modelo propietario.

**Regla V-253**: La atenuación cromática, el distintivo de procedencia, el nombre alias o cualquier otra marca visual aplicada a una cosa en tanto que referencia externa son parte de la gramática de vista de §23, no de la gramática nuclear §1.1b.

---

## 19. Estereotipos y extensiones del lenguaje

Los estereotipos son extensiones tipadas que se aplican a una cosa OPM existente y le añaden clasificación visible, restricciones, estructura derivada o propiedades forzadas. No sustituyen la clase base de la cosa: un objeto estereotipado sigue siendo objeto; un proceso estereotipado sigue siendo proceso.

### 19.1 Definición

**Regla V-142**: Un estereotipo es una extensión declarada sobre una cosa OPM que puede aportar:

- prefijo textual visible;
- propiedades forzadas de la cosa anfitriona;
- estructura derivada;
- entidades auxiliares derivadas;
- restricciones de aplicabilidad.

**Regla V-143**: Los estereotipos son mixtos por defecto: cada estereotipo debe declarar explícitamente si aplica a objetos, procesos o ambos. No se presume polimorfismo universal.

### 19.2 Sintaxis visible

**Regla V-144**: La representación visual canónica de un estereotipo en canvas usa prefijo ASCII `<<Nombre>>` embebido en el rótulo visible de la cosa o, alternativamente, un distintivo visible que preserve el mismo contenido textual en el canon-diagrama.

**Regla V-145**: La representación textual canónica en OPL puede usar comillas angulares `«Nombre»`. Las formas `<< >>` y `« »` se consideran equivalentes de superficie siempre que remitan al mismo estereotipo.

**Regla V-146**: Un artefacto canónico no puede ocultar por completo la condición estereotipada de una cosa. Si el prefijo se omite del rótulo visible por razones de layout, el estereotipo debe persistir mediante distintivo, icono o metadato explícito de export ligado a la cosa.

### 19.3 Propiedades forzadas y estructura derivada

**Regla V-147**: Un estereotipo puede forzar propiedades de la cosa anfitriona, incluida esencia, conjunto mínimo de partes, o presencia de atributos derivados. Toda propiedad forzada debe ser recuperable en OPL o en el metadato canónico del artefacto.

**Regla V-148**: La remoción del estereotipo no puede dejar residuos semánticos ambiguos. La implementación debe declarar si las propiedades forzadas se revocan, se conservan explícitamente o requieren confirmación del modelador.

**Regla V-149**: La descomposición canónica impuesta por un estereotipo no se presume equivalente a una descomposición voluntaria del modelador. Debe ser trazable como estructura derivada del estereotipo en el modelo o en el export canónico.

### 19.4 Distinguibilidad visual

**Regla V-150**: Un estereotipo no puede depender exclusivamente del OPL para su legibilidad. El OPD exportado debe permitir identificar visualmente que la cosa está estereotipada, aunque no necesariamente todo el detalle de la plantilla.

**Regla V-151**: Cuando un estereotipo fuerce esencia física, la sombra visible sigue interpretándose bajo §1.3 como fisicidad efectiva de la cosa, no como mera decoración del estereotipo. El origen de la fuerza debe ser trazable en el modelo, no en una semántica paralela del render.

### 19.5 Entidades derivadas

**Regla V-152**: Un estereotipo puede generar entidades derivadas con patrón nominal reservado `<Rol> of <HostThing>`. Ese patrón queda reservado para entidades derivadas del estereotipo y no debe reutilizarse arbitrariamente para nombres manuales.

**Regla V-153**: Las entidades derivadas por estereotipo pueden aparecer en el canvas, en ramas auxiliares del árbol o en vistas derivadas. Su ciclo de vida debe depender del host que las originó, salvo que la plantilla declare reutilización explícita.

### 19.6 Caso canónico: `<<Requirement>>`

**Regla V-154**: `<<Requirement>>` se declara como estereotipo canónico de requisito en esta adaptación. Un requisito sigue siendo, gráficamente, un objeto OPM estereotipado.

**Regla V-155**: Todo `<<Requirement>>` debe exponer o derivar, como mínimo, los siguientes atributos:

- `Name`
- `ID`
- `Requirement Essence`
- `Satisfaction`
- `Description`

**Regla V-156**: El atributo `Requirement Essence` del estereotipo `<<Requirement>>` es distinto de la esencia de cosa definida en §1.3. Para evitar sobrecarga terminológica, la documentación canónica no debe usar el nombre desnudo `Essence` para el atributo del requisito.

**Regla V-157**: El conjunto `Satisfied Requirement Set` se admite como colección especializada de requisitos. Si la implementación permite marcarla como ordenada, esa propiedad debe quedar serializada y ser recuperable en el canon-documento.

### 19.7 Vistas de Requisitos (`Requirement Views`)

**Regla V-254**: Las `Vistas de Requisitos` (`Requirement Views`) son OPDs derivados por filtrado semántico desde el modelo. Se clasifican como OPD de vista anclada según V-114 (§15.4) y participan del árbol en esa categoría.

**Regla V-255**: Las `Vistas de Requisitos` (`Requirement Views`) son de solo lectura respecto al contenido OPM que proyectan. Editar sus elementos debe redirigirse a los OPDs jerárquicos fuente del modelo.

---

## 20. Capa computacional y ejecutable

Esta sección formaliza la capa mediante la cual el modelo OPM incorpora bindings, slots de valor, procesos ejecutables y conexiones con fuentes externas de datos o cálculo.

### 20.1 Alias de binding

**Regla V-158**: Un alias entre llaves `{alias}` es un identificador de binding computacional. Su sintaxis canónica es `[a-zA-Z_][a-zA-Z0-9_]*`.

**Regla V-159**: Los alias de binding deben ser únicos dentro del alcance operativo donde el código ejecutable pueda referenciarlos. Ese alcance debe declararse por la implementación y no puede ser implícito.

**Regla V-160**: El alias entre llaves no equivale al alias decorativo entre paréntesis de §16. Cuando coexistan ambos, las llaves se reservan exclusivamente para binding computacional.

### 20.2 Unidad dimensional

**Regla V-161**: Un rótulo puede incluir una unidad dimensional entre corchetes `[u]` inmediatamente después del nombre y antes del alias de binding. Los corchetes en este contexto se reservan a unidades, no a multiplicidad ni a rango de estado.

**Regla V-162**: Los corchetes vacíos `[]` solo son admisibles como placeholder de edición. Deben suprimirse en el canon-diagrama salvo que el modelador los haya confirmado explícitamente como parte del rótulo.

### 20.3 Slot de valor

**Regla V-163**: El slot de valor es una primitiva visible distinta del estado de §2.1, aunque comparta morfología afín. Representa un contenedor de valor mutable asociado a la cosa anfitriona.

**Regla V-164**: Un slot de valor puede contener:

- placeholder literal `value`;
- escalar numérico;
- cadena textual;
- disyunción textual;
- intervalo o lista de intervalos cuando el dominio permitido deba hacerse visible;
- estructura multilínea.

**Regla V-165**: Un objeto no debe exhibir más de un slot de valor primario por defecto salvo que la plantilla computacional lo declare explícitamente.

**Regla V-166**: Cuando un objeto combine estados cualitativos y slot de valor, ambos deben poder distinguirse por al menos uno de los siguientes canales: **posición** (el slot de valor se coloca separado del cluster de estados), **rotulado** (prefijo o etiqueta explícita del slot) o **estilo auxiliar** (marca gráfica distintiva reservada al slot). Se recomienda **posición** como canal preferente; la implementación DEBE declarar qué canal usa y no puede dejar la distinción enteramente a inferencia contextual. Si el slot exhibe un rango permitido, los delimitadores `[]` / `()` y la coma entre intervalos forman parte del token visible y no deben normalizarse ni colapsarse como simple valor de runtime.

### 20.4 Proceso ejecutable

**Regla V-167**: Un proceso con cuerpo ejecutable adjunto exhibe el sufijo `()` inmediatamente después del nombre dentro de la elipse.

**Regla V-168**: La ausencia de `()` indica que el proceso no exhibe cuerpo ejecutable visible, aunque pueda participar en la simulación conceptual del modelo.

### 20.5 Contrato de binding

**Regla V-169**: El código ejecutable adjunto a un proceso solo puede referenciar:

- aliases `{...}` declarados por §20.1;
- slots de valor asociados a esos aliases;
- entradas explícitamente tipadas por la implementación;
- nombres reservados documentados por la propia herramienta.

**Regla V-170**: La relación entre enlaces OPM y parámetros de la función ejecutable debe ser trazable. Una implementación puede resolverla por alias, por orden de enlace o por contrato declarado, pero no puede dejarla totalmente implícita.

### 20.6 Visibilidad y exportación del código

**Regla V-171**: El cuerpo del código ejecutable no forma parte del OPD nuclear y no tiene por qué estar inscrito en el canvas. No obstante, su existencia sí es parte del modelo y debe reflejarse por `()` y por metadato recuperable en export.

**Regla V-172**: Si el canon-documento omite el cuerpo del código ejecutable inline, DEBE ofrecer al menos una de estas salidas recuperables:

- tooltip o anexo computacional;
- tabla de bindings;
- referencia persistente al artefacto ejecutable (URI, hash, versión, identificador interno).

No se exige embutir el cuerpo del código en el formato de intercambio; sí se exige que sea recuperable por referencia estable.

### 20.7 Input getter y procesos externos

**Regla V-173**: Un proceso que obtiene input desde usuario, API, broker o middleware externo sigue siendo proceso OPM. La condición de externidad se expresa por su contrato computacional, no por una clase gráfica distinta de la elipse.

**Regla V-174**: Las integraciones externas como URL, MQTT o ROS pueden materializarse mediante estereotipo, distintivo o metadato de export, pero la gramática nuclear mínima sigue siendo el proceso ejecutable `()` enlazado a cosas OPM.

### 20.8 Gemelo digital y referencias externas

**Regla V-175**: Cuando una cosa OPM represente un gemelo digital o una entidad enlazada a un sistema externo, esa condición debe ser recuperable en el modelo mediante estereotipo, alias, distintivo o metadato canónico. No puede depender solo de convenciones de color o de interfaz.

---

## 21. Indicadores UI y afordances

Esta sección documenta la frontera entre gramática OPM y visualidades auxiliares de edición, navegación, tutorial o gestión modal.

### 21.1 Modos de render del canvas

**Regla V-200**: La implementación distingue, como mínimo, cuatro modos visuales sobre el canvas:

- estático-exportable;
- edición;
- navegación;
- gestión-modal.

Un quinto modo, runtime, queda regulado por §17.

**Regla V-201**: Solo el modo estático-exportable constituye base de conformidad para el canon-diagrama.

### 21.2 Handles, overlays y chrome de edición

**Regla V-202**: Handles de selección, puntos de rotación, menús radiales, toasts, backdrops modales y marcadores transitorios de creación no pertenecen a la gramática OPM y deben omitirse en los exports canónicos.

**Regla V-203**: Los elementos UI de edición deben usar un canal visual reservado y no ambiguo respecto de §1, §2, §3, §8, §10, §17, §19, §20 y §23. Se recomienda color de interfaz diferenciado, opacidad controlada y ubicación fuera del núcleo semántico cuando sea posible.

### 21.3 Notas y anotaciones meta

**Regla V-204**: Las notas libres, sticky notes y anotaciones meta pueden coexistir sobre el canvas, pero no pertenecen a la gramática OPM nuclear. Si la implementación permite exportarlas, debe marcarlas como contenido meta del autor y no como hecho del modelo. Si además reserva una morfología por defecto para ellas, esa morfología DEBE permanecer fuera de los canales semánticos de OPM y puede combinar, por ejemplo, fondo amarillo pálido, pin rojo y anclaje discontinuo corto, siempre que esa combinación no sea reutilizable por estados, enlaces, validaciones o simulación.

### 21.4 Búsqueda y navegación

**Regla V-205**: El resaltado de búsqueda o navegación, si existe, debe usar un canal reservado distinto de las marcas de simulación y de refinamiento. Su ausencia no invalida el modelo, pero su presencia no debe confundirse con actividad o designación.

El `Mapa del Sistema` pertenece a esta misma familia de navegación: puede usar miniaturas de OPDs, flechas meta o marcadores de navegación propios de la vista, siempre que esos elementos no se presenten como enlaces OPM ni como contenido del modelo.

### 21.5 Tutorial y preferencias de asistencia

**Regla V-206**: El render canónico de un OPD se evalúa con tutorial, overlays de ayuda y focos pedagógicos desactivados. Si la implementación ofrece modo tutorial, este pertenece exclusivamente al ecosistema de asistencia.

---

## 22. Estilado autoral

El estilado autoral es una capa paralela de apariencia aplicada por el modelador sobre una representación OPM ya válida. No altera por sí mismo la semántica nuclear del modelo.

### 22.1 Principio general

**Regla V-207**: El estilado autoral es admisible siempre que no colisione con los canales visuales reservados a la gramática OPM, a la simulación, a la validación ni a la UI de edición.

### 22.2 Defaults y coherencia

**Regla V-208**: En ausencia de estilado autoral explícito, toda implementación conforme debe converger a un esquema por defecto coherente con §1.1b, §16.1 y la tipografía canónica declarada.

**Regla V-209**: Dentro de un mismo OPD, las cosas de igual clase semántica deben compartir la misma base cromática y tipográfica salvo variante autoral explícitamente declarada.

### 22.3 Reserva de canales

**Regla V-210**: El estilado autoral no puede reutilizar sin distinción:

- rojo, amarillo de alerta o verde de conformidad como semántica tácita;
- discontinuidad de borde para marcar operaciones transitorias;
- cromatismo o halo reservado a simulación;
- marcas reservadas a validación o error.

### 22.4 Rótulo

**Regla V-211**: La familia tipográfica, peso, tamaño, color y alineación del rótulo pertenecen a la capa autoral. Sin embargo, el rótulo no puede salir del bounding box visible ni perder legibilidad por contraste insuficiente.

**Regla V-212**: El canon-diagrama no admite truncamiento silencioso del rótulo. La herramienta debe expandir, reubicar o rechazar el resize antes que exportar una elipsis no declarada.

### 22.5 Bitmap e interior decorativo

**Regla V-213**: Una implementación puede permitir imagen bitmap decorativa dentro de una cosa, pero esa imagen no puede ocluir contorno, sombreado, estados ni rótulo. Su estatus es decorativo, no semántico, salvo que la SSOT lo promueva explícitamente en una revisión posterior.

**Regla V-214**: Cuando el refinamiento o el contenido interno entre en conflicto con el bitmap decorativo, la prioridad la tiene siempre la geometría OPM interna. La imagen debe suprimirse, atenuarse o quedar excluida del canon exportado.

### 22.6 Tamaño y proporción

**Regla V-215**: El tamaño de una cosa puede variar por decisión autoral, pero no hasta el punto de impedir legibilidad, contención del rótulo o identificación de sus decoraciones. La implementación debe declarar bandas de aspect ratio admisibles o una política de autoajuste equivalente.

### 22.7 Normalización léxica y estilo

**Regla V-216**: La normalización léxica organizacional, los alias de casing o las reescrituras automáticas del rótulo no pueden aplicarse silenciosamente como si fueran mero estilado. Deben ser trazables como política de normalización o como metadato reversible del modelo.

### 22.8 Exportación

**Regla V-217**: Salvo declaración contraria del perfil de export, el canon-documento y el canon-diagrama deben normalizar el estilado autoral hacia el esquema canónico de la SSOT. El estilado autoral se conserva como capa editable del canvas, no como condición de conformidad del artefacto exportado.

---

## 23. Composición inter-modelo y sub-modelos

Esta sección amplía la noción de modelo OPM para admitir composición por referencia entre modelos individuales, sin perder trazabilidad OPD↔OPL ni portabilidad.

### 23.1 Definición de modelo compuesto

**Regla V-176**: Un modelo OPM puede referenciar otros modelos OPM como sub-modelos. El resultado es un grafo dirigido acíclico de modelos individuales.

**Regla V-177**: Cada sub-modelo conserva su propia especificación OPL autocontenida. La dualidad OPD↔OPL se preserva íntegramente dentro de cada modelo individual.

### 23.2 Declaración cruzada padre-hijo

**Regla V-178**: El modelo padre debe contener una declaración explícita de cada sub-modelo referenciado y de la base de selección o derivación que lo vincula al padre.

**Regla V-179**: El sub-modelo debe declarar su modelo de origen o su vista derivada de manera simétrica y persistente.

### 23.3 Vista de sub-modelo

**Regla V-180**: Una vista de sub-modelo anclada al árbol se identifica como `SDx.y: <Nombre> Vista de Sub-modelo` o equivalente declarado. El token `SDx.y` en este patrón es **etiqueta visible interna al árbol del modelo propietario**, no identidad persistente del OPD (V-247 a V-249): las referencias externas al sub-modelo o a sus OPDs deben seguir usando el identificador persistente declarado por V-248. Esta clase de vista participa del árbol por posición, pero no equivale a refinamiento ordinario. Se clasifica como OPD de vista anclada según V-114 (§15.4).

**Regla V-181**: La vista de sub-modelo constituye una categoría distinta del OPD jerárquico ordinario y de la vista ad hoc no anclada. La implementación debe diferenciar estas tres categorías en su metadato de árbol y de export, conforme a V-114.

### 23.4 Lectura desde el padre

**Regla V-182**: Cuando un sub-modelo se visualiza desde el árbol del padre, la implementación puede presentarlo en modo de solo lectura o equivalente. Esa condición pertenece a la gramática de vista, no al contenido del OPD.

**Regla V-183**: El nodo del árbol del padre que referencia un sub-modelo debe llevar un distintivo o indicador explícito de vínculo externo. El mismo vínculo debe ser visible en la pestaña, ruta de navegación o metadato del documento.

### 23.5 Apariencias cross-model

**Regla V-184**: Una cosa visible dentro de un sub-modelo que también aparece en el modelo padre es **referencia externa a la misma existencia compartida** (V-123, §18.7). No es existencia-espejo ni entidad duplicada. La existencia pertenece al modelo propietario original y la aparición en el sub-modelo es apariencia local de una referencia externa.

**Regla V-185**: Si la implementación usa atenuación cromática, alias forzado o distintivos para indicar procedencia cross-model, esos indicadores se clasifican como gramática de vista de §23 y no como semántica nuclear de §1.1b. La atenuación cromática es marca epistémica local ("esta cosa es referencia, no propiedad de este modelo"), no propiedad de la cosa.

**Regla V-256**: La sincronización de cambios entre modelo propietario y sub-modelo referenciador se rige por el ciclo de carga (`cargado y sincronizado`, `cargado y no sincronizado`, `no cargado`) declarado por la implementación. Todos esos estados son propiedades de la **referencia**, no de la cosa subyacente.

### 23.6 Excepción controlada a V-46

**Regla V-186**: Una vista de sub-modelo puede no contener exactamente un proceso sistémico en el sentido de V-46, siempre que declare explícitamente la selección parcial o el criterio de vista que la originó.

### 23.7 Portabilidad

**Regla V-187**: Todo export canónico de un modelo compuesto debe declarar si incluye o no los sub-modelos no cargados y cómo se resuelven las referencias externas.

**Regla V-188**: Un modelo compuesto no puede considerarse portable si la resolución de sus sub-modelos depende de convenciones implícitas de filesystem o sesión. El esquema de resolución debe ser parte del formato de intercambio o del manifiesto de export.

### 23.8 Desconexión

**Regla V-189**: La operación de desconectar un sub-modelo debe cambiar explícitamente el estado del vínculo en el árbol y en el metadato del modelo. No puede dejar un nodo visualmente ambiguo entre vista anclada y OPD ordinario.

---

## 24. Marcas de validación y afordances de error

Esta sección regula cómo una implementación puede comunicar invalidez, advertencia metodológica, conflicto de unicidad o sugerencia automática sin contaminar la gramática del OPD.

### 24.1 Familias de validación

**Regla V-218**: La implementación puede distinguir, al menos, estas familias de validación:

- invalidez gramatical;
- advertencia metodológica;
- conflicto de unicidad o identidad;
- conflicto de contención o pertenencia;
- sugerencia automática o inferida.

### 24.2 Política de canvas limpio

**Regla V-219**: En ausencia de declaración contraria, esta adaptación adopta la política de **canvas limpio**: la validación no deja marcas persistentes sobre el OPD estático una vez cerrado el diálogo o panel de validación. El resultado de validación vive en vistas auxiliares, no en la gramática nuclear del diagrama.

**Regla V-220**: Si una implementación opta por dejar distintivos persistentes de validación sobre el canvas, debe declararlos como gramática de vista separada y no puede mezclarlos con designaciones de estado, actividad de simulación o afordances de edición.

### 24.3 Edición en curso

**Regla V-221**: Durante operaciones de arrastre o creación, un enlace inválido puede exhibir un marcador transitorio de rechazo, como `×` roja sobre el conector. Ese marcador no pertenece al canon-diagrama.

### 24.4 Unicidad nominal

**Regla V-222**: Todo conflicto de unicidad nominal debe resolverse de manera explícita por el modelador o por una opción de autorrenombrado visible. No se admite reescritura silenciosa del nombre como mecanismo de conformidad por defecto.

### 24.5 Metodología y sugerencias

**Regla V-223**: Las comprobaciones metodológicas y las sugerencias automáticas, incluidas las inferidas por analítica o ML, son vistas derivadas del modelo. No forman parte del OPD canónico salvo que una revisión futura de la SSOT les asigne notación propia sobre el canvas.

### 24.6 Separación visual

**Regla V-224**: Los canales de validación, advertencia y sugerencia no pueden reutilizar sin distinción:

- el borde discontinuo de afiliación ambiental;
- el contorno grueso de refinamiento;
- las marcas de simulación;
- las decoraciones de enlace.

---

## 25. Exportación canónica

La exportación canónica fija qué artefactos constituyen evidencia normativa del modelo visible y cómo deben estructurarse.

### 25.1 Taxonomía de perfiles

**Regla V-225**: Esta adaptación reconoce tres familias de salida:

- **canon-documento**: artefacto documental completo por modelo;
- **canon-diagrama**: artefacto por OPD, preferentemente vectorial;
- **previsualización raster**: artefacto no canónico para compatibilidad o miniatura.

### 25.2 Perfil por defecto

**Regla V-226**: Toda implementación conforme debe declarar un perfil por defecto para el canon-documento y otro para el canon-diagrama. La ausencia de perfil declarado invalida la aplicación operativa de V-0.

### 25.3 Canon-diagrama

**Regla V-227**: El canon-diagrama debe preservar la gramática visible del OPD, preferentemente en formato vectorial. No debe incluir handles, grid, overlays modales, toasts ni chrome de edición.

**Regla V-228**: En el canon-diagrama los rótulos dentro del grafo permanecen en negro por defecto, salvo que la SSOT promueva expresamente otro comportamiento. El cromatismo de clase se preserva primariamente en bordes, líneas y decoraciones semánticas.

### 25.4 Canon-documento

**Regla V-229**: El canon-documento puede incluir portada, URL, índice, árbol de OPDs, diagramas, OPL, diccionario de elementos, diccionario de relaciones y vistas derivadas, incluido el `Mapa del Sistema`. Su estructura exacta debe declararse por perfil.

**Regla V-230**: Los listados textuales del canon-documento pueden extender el cromatismo de clase a nombres fuera del grafo, siempre que el propio perfil lo declare y no contradiga el canon-diagrama.

### 25.5 Export parcial

**Regla V-231**: Si el export omite OPDs, sub-modelos o vistas derivadas, el artefacto debe declararse como export parcial e identificar explícitamente el subconjunto incluido.

### 25.6 Código, descripciones y anexos

**Regla V-232**: El canon-documento puede incluir descripciones de entidades, tooltips computacionales, requirement views u otros anexos. Si los omite, debe mantener una referencia recuperable a esos atributos cuando formen parte del modelo.

### 25.7 Resolución y viewport

**Regla V-233**: El canon-diagrama no debe depender de rasterización para conservar sus distinciones esenciales. Si un perfil documental rasteriza los OPDs, debe declarar resolución mínima suficiente para preservar dash, contornos, triángulos y rótulos.

**Regla V-234**: Ningún export canónico debe recortar símbolos de forma que pierdan su anclaje topológico o su objeto contenedor.

### 25.8 Watermarks y overlays editoriales

**Regla V-235**: Marcas de agua, etiquetas de confidencialidad u overlays editoriales son admisibles solo como capa documental adicional. No pueden ocluir primitivas OPM ni confundirse con gramática del diagrama.

### 25.9 Portabilidad de recursos

**Regla V-236**: Si el modelo depende de bitmaps, sub-modelos, descripciones externas o código adjunto, el export canónico debe embutir esos recursos, referenciarlos persistentemente o declarar explícitamente su ausencia.

---

## 26. Operaciones auxiliares inter-OPD

Las operaciones auxiliares son gestos de la herramienta sobre un OPD activo que materializan enlaces o cosas ya existentes en el modelo, sin crear semántica ontológica nueva.

### 26.1 Definición

**Regla V-257**: Una operación auxiliar inter-OPD es un operador derivado que modifica la composición visible de un OPD activo trayendo, retirando o re-materializando apariencias de cosas y enlaces cuya existencia ya está declarada en el modelo. No introduce nuevas cosas, enlaces o relaciones ontológicas.

### 26.2 Bring connected things

**Regla V-258**: `Bring connected things` es la operación que materializa en el OPD activo cosas conectadas directamente por enlace a una cosa seleccionada. La operación puede estar filtrada por familia de enlace (§3, V-239) y por criterio de conectividad directa.

**Regla V-259**: El resultado de `Bring connected things` debe ser indistinguible, en el canon-diagrama, de un OPD construido manualmente con las mismas cosas y enlaces. No se admiten marcas persistentes de "cosa traída" en el export canónico.

### 26.3 Bring links between selected entities

**Regla V-260**: `Bring links between selected entities` es la operación que materializa en el OPD activo los enlaces existentes en el modelo entre un conjunto de cosas ya seleccionadas. No crea enlaces nuevos.

### 26.4 Materialización y visibilidad

**Regla V-261**: Las operaciones auxiliares pueden dejar en el OPD activo supresores de enlaces no materializados (§1.8, V-192) cuando existan conexiones hacia cosas ausentes del OPD. Este indicador no es exclusivo de estas operaciones pero sí se refuerza por su ejecución.

**Regla V-262**: Las operaciones auxiliares pueden crear OPDs derivados nombrados (por ejemplo, `<cosa> unfolded`) sin que esto constituya un mecanismo canónico de refinamiento (§10.1, V-242). Esos OPDs derivados se clasifican como vistas ancladas o ad hoc según V-114 (§15.4).

### 26.5 Reversibilidad

**Regla V-263**: Toda operación auxiliar debe ser reversible o acotada: la herramienta debe permitir revertir o acotar explícitamente el cambio sobre el OPD activo. Bring no puede modificar el modelo subyacente; si lo hiciera, deja de ser operación auxiliar y debe regularse en §10 u otra sección ontológica.

---

## Índice de reglas — V-0 a V-68 (regla rectora y gramática base)

| Regla | Resumen |
|---|---|
| V-0 | Canonicidad por exportación: gramática conforme es la que persiste en export canónico |
| V-0a | Dos perfiles obligatorios: canon-diagrama y canon-documento |
| V-0b | Elemento persistente en canon-diagrama debe tener regla `V-*` o capítulo explícito |
| V-0c | Elemento no canónico es UI transitoria y no reutiliza canales semánticos |
| V-0d | Elemento específico de perfil se declara como atributo de perfil |
| V-0e | Captura de pantalla no es evidencia suficiente de canonicidad |
| V-1 | Valores por defecto: informacional y sistémico; presets no alteran semántica sin serialización |
| V-2 | Perseverancia no es visual, se infiere del tipo |
| V-3 | Vértice del triángulo apunta al refinable |
| V-4 | Los estados no existen fuera de su objeto |
| V-5 | Objeto sin estados: solo creado o destruido |
| V-6 | Máximo un defecto y un `Current`; múltiples iniciales/finales permitidos |
| V-7 | Efecto requiere objeto con al menos un estado |
| V-8 | Resultado no conecta directamente al estado inicial |
| V-9 | Efecto solo-entrada sin salida: destino es estado por defecto |
| V-10 | Habilitador desaparece: proceso se detiene |
| V-11 | Unicidad de rol: transformado XOR habilitador |
| V-12 | Evento es solo el segmento objeto→proceso |
| V-13 | Evento se pierde tras evaluación |
| V-14 | AND es el operador por defecto (sin arco) |
| V-15 | XOR/OR aplican a todas las familias procedimentales |
| V-16 | Arco en extremo convergente del abanico |
| V-17 | Abanicos: convergente o divergente |
| V-18 | Probabilístico es siempre XOR |
| V-19 | Resultado simple equivale a XOR de resultados con estado |
| V-20 | Coincidencia de etiquetas de ruta fija trayectoria |
| V-21 | Parámetros de multiplicidad: nombres únicos |
| V-22 | Multiplicidad: anotación junto al extremo del enlace |
| V-23 | Multiplicidad no aplica a procesos directamente |
| V-24 | Misma perseverancia en refinable y refinadores (excepto exhibición) |
| V-25 | Exhibición puede conectar objetos con procesos |
| V-26 | Cuatro combinaciones exhibidor-rasgo válidas |
| V-27 | Clasificación no distingue colección completa/incompleta |
| V-28 | Herencia múltiple permitida |
| V-29 | Atributo discriminante: un valor por especialización |
| V-30 | Bidireccional/recíproco no existen con estado solo en destino |
| V-31 | Invocación implícita: posición vertical determina secuencia |
| V-32 | Misma altura = ejecución paralela |
| V-33 | In-zooming: contorno grueso en padre e hijo |
| V-34 | Descomposición: elipse agrandada contiene subprocesos |
| V-35 | Línea temporal: arriba → abajo |
| V-36 | Contorno exterior se interpreta distributivamente; familias según V-37/V-103/V-104/V-105 |
| V-37 | Consumo/resultado NO en contorno exterior de descomposición |
| V-38 | Eventos sistémicos no cruzan límite de descomposición |
| V-39 | Condición omite subproceso: control pasa al siguiente |
| V-40 | Enlace escindido: temprano saca de s1, tardío pone en s2 |
| V-41 | No hay enlaces escindidos con modificador de control |
| V-42 | Cambio de rol instrumento→afectado válido si estados coinciden |
| V-43 | Resultado + consumo sobre mismo objeto = inválido |
| V-44 | Transformador prevalece sobre habilitador |
| V-45 | Duración dentro de la elipse: {min, esp, max} |
| V-46 | SD contiene exactamente un proceso sistémico |
| V-47 | Unicidad nominal evaluada a nivel de modelo para cualquier cosa (objeto, proceso, estado) |
| V-48 | [Eliminada — ver V-4] |
| V-49 | Consumido desaparece al inicio del proceso |
| V-50 | Máximo 20-25 cosas por OPD |
| V-51 | Sin oclusión, minimizar cruces |
| V-52 | Un elemento puede aparecer en cualquier número de OPDs |
| V-53 | Proceso activo: marca reservada (relleno/contorno/halo), no elipse rellena estricta |
| V-54 | Estado actual: glifo externo reservado al borde del estado |
| V-55 | Tiempo fluye arriba → abajo, en edición y simulación |
| V-56 | Bidireccional con etiquetas iguales equivale a recíproco |
| V-57 | Partes de agregación pueden transformarse independientemente del todo |
| V-58 | Instancias muestran valores concretos; clases muestran rangos |
| V-59 | Activación asincrónica por eventos: subprocesos independientes |
| V-60 | Átomo del OPD: Constructo Básico = 1 enlace + 2 cosas |
| V-61 | Anatomía de enlace: Origen + Destino + Conector (Línea + Símbolo + Etiqueta? + Etiqueta de Ruta?) |
| V-62 | In-zooming en dos fases: Mostrar Contenido + Refinar Enlaces |
| V-63 | Colores informativos también para decoraciones internas de triángulos; topología interna es canal normativo |
| V-64 | OPM Model = OPD Set + OPL Spec + Sub-models? (composición por referencia) |
| V-65 | Dualidad OPD ↔ OPL: toda afirmación gráfica es reproducible como texto y viceversa |
| V-66 | *Conectar*: Conjunto de Cosas (desconectado→conectado) con Conjunto de Enlaces como instrumento |
| V-67 | Sin estados (s=0) vs con estados (s≥1); con estados deriva Conjunto de Objetos Específicos de Estado |
| V-68 | Objeto Específico de Estado: nombre = estado + nombre del objeto original |

## Índice de reglas — V-69 a V-123 (refinamiento entre OPDs, semi-plegado, metodología)

| Regla | Resumen |
|---|---|
| V-69 | Contorno grueso aplica a descomposición y despliegue en nuevo diagrama |
| V-70 | El despliegue intradiagrama NO produce contorno grueso |
| V-71 | Tipo de contorno (sólido/punteado) persiste en todos los niveles de refinamiento |
| V-72 | Herencia aplica a través de niveles de refinamiento por despliegue |
| V-73 | Enlaces heredados no visibles pero semánticamente activos |
| V-74 | Herencia de afiliación: atributos de objetos ambientales son automáticamente ambientales |
| V-75 | Sobreescritura: especialización puede reemplazar participante heredado |
| V-76 | Migración de enlaces comunes al crear un general desde especializaciones |
| V-77 | Invocación implícita solo aplica a descomposición de proceso, no de objeto |
| V-78 | Descomposición de objeto: posición codifica disposición semántica, no orden temporal |
| V-79 | Refinable aparece como contenedor en OPD hijo; cosas internas contenidas dentro |
| V-80 | Cosas conectadas al refinado se copian como elementos externos en OPD hijo |
| V-81 | En descomposición se copian todas las cosas conectadas vía cualquier enlace |
| V-82 | En despliegue se copian solo hijos estructurales (agregación, exhibición) |
| V-83 | No se puede refinar un elemento externo |
| V-84 | Objetos internos se eliminan al eliminar el proceso padre (cascada) |
| V-85 | Objetos externos existen independientemente del refinamiento |
| V-86 | Estado se suprime cuando un OPD hijo de descomposición lo referencia vía enlace |
| V-87 | Supresión de estados solo aplica a descomposición |
| V-88 | Estados no referenciados en enlaces al refinado NO se suprimen |
| V-89 | Supresión desde múltiples OPDs hijo = unión |
| V-90 | Expresión de estados: suprimidos en padre se revelan en hijo vinculados a subprocesos |
| V-91 | Enlaces estructurales al contenedor son visibles en OPD hijo |
| V-92 | Enlaces procedimentales al contenedor NO son visibles directamente — se distribuyen |
| V-93 | Enlaces entre elementos internos del OPD hijo son visibles normalmente |
| V-94 | Enlaces que no tocan contenedor ni internos son invisibles en OPD hijo |
| V-95 | Esencia (física/informacional) no cambia a través del refinamiento |
| V-96 | Perseverancia (persistente/transitoria) no cambia a través del refinamiento |
| V-97 | Nombres no cambian a través del refinamiento |
| V-98 | Consistencia de hechos: un OPD no puede contradecir a otro OPD |
| V-99 | Importancia proporcional al OPD más alto donde aparece la cosa |
| V-100 | Prohibición de refinamiento cíclico: transitiva en toda la cadena de ancestros |
| V-101 | Instancia visual ≠ instancia lógica |
| V-102 | No se puede crear instancia visual entre tipos diferentes (objeto↔proceso prohibido) |
| V-103 | Consumo/input → primer subproceso; resultado/output → último subproceso |
| V-104 | Efecto, agente, instrumento → todos los subprocesos |
| V-105 | Enlaces estructurales NO se distribuyen — permanecen en contenedor |
| V-106 | Sin subprocesos, enlace al contenedor como respaldo temporal |
| V-107 | Distribución de enlaces solo aplica a descomposición, no a despliegue |
| V-108 | Eventos de objetos ambientales PUEDEN cruzar límite con contingencia explícita |
| V-109 | Restricciones de frontera solo aplican a descomposición |
| V-110 | Escisión es el único mecanismo para subespecificación de efecto en descomposición |
| V-111 | Cambio de rol: objeto muestra estados intermedios en OPD hijo |
| V-112 | Cambio de rol solo aplica a descomposición |
| V-113 | Solo OPDs jerárquicos hoja son eliminables directamente; vistas con política propia |
| V-114 | Tres categorías de OPD (jerárquico, vista anclada, vista ad hoc) |
| V-115 | Regla general: todo proceso explícito transforma al menos un objeto; excepción para procesos persistentes válidos |
| V-116 | Semi-plegado: partes como íconos de triángulo con nombre dentro del todo |
| V-117 | Semi-plegado parcial: por refinador, algunos dentro y otros extraídos |
| V-118 | Indicador numérico de semi-plegado = refinadores ocultos, no total |
| V-119 | Semi-plegado por OPD: estado independiente por apariencia |
| V-120 | Enlaces procedimentales pueden apuntar a refinadores semi-plegados |
| V-121 | El nombre de proceso hereda su política léxica de la capa textual activa |
| V-122 | Alias de cosa: abreviatura entre paréntesis o llaves; llaves reservadas a binding computacional |
| V-123 | Existencia única, apariencias locales múltiples, referencias externas cross-model |

## Índice de reglas — V-124 a V-263 (v2: extensiones y cláusulas nuevas)

| Regla | Resumen |
|---|---|
| V-124 | Sombra en canon-diagrama corresponde exclusivamente a esencia física |
| V-125 | La esencia física se preserva en el contenedor refinado |
| V-126 | Las tres fuentes de sombra colapsan a un mismo resultado semántico en canon |
| V-127 | Reforzadores de canvas no persisten en canon-diagrama |
| V-128 | Topología interna del triángulo es canal normativo |
| V-129 | Triángulo estructural requiere líneas visibles al refinable y al refinador |
| V-130 | Triángulos auxiliares UI se distinguen perceptualmente de semánticos |
| V-131 | Import preserva topología interna; color puede retipificarse |
| V-132 | Proceso activo vs refinable: canales visuales distintos |
| V-133 | Glifo de estado actual: pin/gota externa anclada al borde |
| V-134 | `Current` declarado vs runtime: serialización los distingue |
| V-135 | Token transitorio en enlace activo, distinto de piruletas |
| V-136 | Tokens runtime no en canon-diagrama salvo snapshot declarado |
| V-137 | Estados operacionales distintos de activo usan marcas reservadas |
| V-138 | Proceso suspendido visiblemente distinto de inactivo en snapshot |
| V-139 | Síncrono: máx 1 activo por hilo; asíncrono: múltiples posibles |
| V-140 | Modo headless: ausencia de runtime no altera gramática estática |
| V-141 | Snapshot de runtime declarado explícitamente en export |
| V-142 | Estereotipo: prefijo textual, propiedades forzadas, estructura derivada, entidades derivadas, restricciones |
| V-143 | Estereotipos declaran aplicabilidad (objeto/proceso/ambos) |
| V-144 | Sintaxis canvas: `<<Nombre>>` en rótulo o distintivo equivalente |
| V-145 | Sintaxis OPL: `«Nombre»`; `<< >>` y `« »` equivalentes |
| V-146 | Estereotipo no puede ocultarse; distintivo/icono/metadato si se omite del rótulo |
| V-147 | Propiedades forzadas recuperables en OPL o metadato canónico |
| V-148 | Remoción de estereotipo sin residuos ambiguos |
| V-149 | Descomposición canónica trazable como estructura derivada |
| V-150 | OPD exportado permite identificar visualmente cosa estereotipada |
| V-151 | Estereotipo que fuerza esencia física: sombra es fisicidad efectiva |
| V-152 | Entidades derivadas con patrón reservado `<Rol> of <Host>` |
| V-153 | Ciclo de vida de entidades derivadas depende del host |
| V-154 | `<<Requirement>>`: estereotipo canónico de requisito |
| V-155 | Atributos mínimos: Name, ID, Requirement Essence, Satisfaction, Description |
| V-156 | `Requirement Essence` distinta de §1.3; evitar nombre desnudo `Essence` |
| V-157 | `Satisfied Requirement Set` admitida; orden serializado si aplica |
| V-158 | `{alias}` como identificador de binding computacional |
| V-159 | Alias de binding únicos en alcance operativo declarado |
| V-160 | `{alias}` ≠ alias decorativo entre paréntesis |
| V-161 | Unidad dimensional `[u]` entre corchetes, después del nombre |
| V-162 | `[]` vacío es placeholder; se suprime en canon-diagrama salvo confirmación |
| V-163 | Slot de valor: primitiva visible distinta del estado |
| V-164 | Slot de valor: placeholder `value`, escalar, cadena, disyunción, multilínea |
| V-165 | Un slot primario por objeto por defecto |
| V-166 | Slot vs estado cualitativo: distinguible por posición/rotulado/estilo |
| V-167 | Proceso con cuerpo ejecutable exhibe `()` |
| V-168 | Ausencia de `()` no impide simulación conceptual |
| V-169 | Código ejecutable referencia solo aliases/slots/entradas tipadas/nombres reservados |
| V-170 | Relación enlace OPM ↔ parámetro función trazable |
| V-171 | Cuerpo de código no en canvas, pero reflejado por `()` y metadato |
| V-172 | Si canon-documento omite código: tooltip, tabla o referencia persistente recuperable |
| V-173 | Proceso que obtiene input externo sigue siendo proceso OPM (elipse) |
| V-174 | Integraciones externas: estereotipo/distintivo/metadato, no clase gráfica distinta |
| V-175 | Gemelo digital recuperable en modelo por estereotipo/alias/distintivo/metadato |
| V-176 | Modelo OPM puede referenciar otros como sub-modelos (grafo DAG) |
| V-177 | Cada sub-modelo conserva OPL autocontenida |
| V-178 | Modelo padre declara explícitamente cada sub-modelo |
| V-179 | Sub-modelo declara su origen simétricamente |
| V-180 | `SDx.y: <Nombre> Vista de Sub-modelo`; vista anclada |
| V-181 | Tres categorías (jerárquico/vista anclada/vista ad hoc) diferenciadas en metadato |
| V-182 | Sub-modelo desde padre puede presentarse en solo lectura |
| V-183 | Nodo del árbol del padre con distintivo de vínculo externo |
| V-184 | Cross-model = referencia externa a existencia compartida (no espejo) |
| V-185 | Atenuación/alias/distintivos de procedencia: gramática de vista de §23 |
| V-186 | Vista de sub-modelo puede no tener proceso sistémico único (V-46) |
| V-187 | Export declara inclusión de sub-modelos no cargados |
| V-188 | Portabilidad requiere esquema de resolución explícito |
| V-189 | Desconexión de sub-modelo cambia explícitamente estado del vínculo |
| V-190 | Piruleta semántica siempre cuelga de línea visible |
| V-191 | Handles UI distinguibles de piruletas en canon |
| V-192 | Supresor `...` de enlaces no materializados pertenece a gramática si persiste en canon |
| V-193 | Triángulos compactados deben anclar geométricamente a cosa visible |
| V-194 | Rótulo íntegro en canon-diagrama; sin elipsis ni corte silencioso |
| V-195 | Rótulo dentro del bounding box salvo variante tipificada |
| V-196 | Grid del canvas: decoración opcional, suprimida en canon |
| V-197 | Snap transparente al modelo; OPDs con misma topología son equivalentes |
| V-198 | Smart-guides en canal UI reservado, no patrón discontinuo |
| V-199 | Auto-ajuste de viewport en export evita símbolos huérfanos recortados |
| V-200 | Cuatro modos de canvas: estático/edición/navegación/modal + runtime |

## Índice de reglas — V-201 a V-263 (v2: canon-diagrama, requisitos, sub-modelo y operaciones auxiliares)

| Regla | Resumen |
|---|---|
| V-201 | Solo estático-exportable es base de conformidad |
| V-202 | Handles y chrome UI omitidos en canon |
| V-203 | UI en canal reservado, no ambiguo respecto a §1/§2/§3/§8/§10/§17/§19/§20/§23 |
| V-204 | Notas y sticky notes: contenido meta del autor, no hecho del modelo |
| V-205 | Resaltado de búsqueda en canal reservado distinto de simulación/refinamiento |
| V-206 | Canon evaluado con tutorial/overlays desactivados |
| V-207 | Estilado autoral admisible si no colisiona con canales reservados |
| V-208 | Defaults convergentes al esquema canónico (§1.1b, §16.1) |
| V-209 | Cosas de igual clase comparten base cromática/tipográfica en OPD |
| V-210 | Estilado no reutiliza sin distinción rojo/amarillo/verde, discontinuidad, halo de simulación |
| V-211 | Tipografía y color del rótulo pertenecen a autoral; legibilidad obligatoria |
| V-212 | Canon no admite truncamiento silencioso del rótulo |
| V-213 | Bitmap decorativo admisible si no ocluye contorno/sombreado/estados/rótulo |
| V-214 | Conflicto refinamiento vs bitmap: prioridad a geometría OPM |
| V-215 | Tamaño de cosa con bandas de aspect ratio declaradas |
| V-216 | Normalización léxica trazable, no silenciosa |
| V-217 | Canon normaliza estilado autoral; capa editable persiste en canvas |
| V-218 | Familias de validación: invalidez/advertencia/unicidad/contención/sugerencia |
| V-219 | Política canvas limpio: sin marcas persistentes de validación en OPD |
| V-220 | Distintivos persistentes (opcionales) como gramática de vista, no mezclada |
| V-221 | Marcador `×` roja durante edición inválida, no en canon |
| V-222 | Conflicto de unicidad nominal resuelto explícitamente, no silenciosamente |
| V-223 | Metodología y sugerencias son vistas derivadas, no OPD canónico |
| V-224 | Validación no reutiliza discontinuidad/contorno grueso/simulación/decoraciones |
| V-225 | Tres familias de salida: canon-documento, canon-diagrama, raster |
| V-226 | Perfil por defecto declarado obligatoriamente |
| V-227 | Canon-diagrama preserva gramática visible; sin chrome de edición |
| V-228 | Rótulos en negro por defecto en canon-diagrama |
| V-229 | Canon-documento: portada/índice/árbol/diagramas/OPL/diccionarios/vistas |
| V-230 | Listados textuales admiten cromatismo de clase si el perfil lo declara |
| V-231 | Export parcial declarado y subconjunto identificado |
| V-232 | Descripciones/tooltips/anexos con referencia recuperable si se omiten |
| V-233 | Canon-diagrama no depende de rasterización para distinciones esenciales |
| V-234 | Ningún export recorta símbolos sin anclaje topológico |
| V-235 | Watermarks/overlays editoriales como capa documental, no oclusivos |
| V-236 | Portabilidad: recursos embutidos, referenciados o declarados ausentes |
| V-237 | `Current` como designación persistente declarable; serializada en modelo |
| V-238 | `Current` declarada ≠ marca runtime de V-54; serialización distingue |
| V-239 | Cinco familias canónicas de enlace |
| V-240 | Invocación con firma `Proceso→Proceso` como familia autónoma |
| V-241 | Categorías adicionales son extensiones de implementación, no canónicas |
| V-242 | Sub-model como cuarto par canónico de refinamiento-abstracción |
| V-243 | Bring y operaciones auxiliares como operadores derivados (§26) |
| V-244 | Tres categorías de OPD con reglas distintas de creación/eliminación/navegación |
| V-245 | Eliminabilidad diferenciada por categoría de OPD |
| V-246 | Tres canales independientes del OPD: temporal, navegación, identidad |
| V-247 | `SDx.y` es proyección humana del orden de navegación, no identidad |
| V-248 | Identificador persistente del OPD obligatorio (UUID/slug/URI) |
| V-249 | Referencias externas citan identificador persistente, no `SDx.y` |
| V-250 | Acoplamiento canvas↔OPL↔árbol es de proyección, no de identidad |
| V-251 | Clausura OPD↔OPL local; compuesto como DAG de modelos autocontenidos |
| V-252 | URI/handle persistente obligatorio para cosa referenciable cross-model |
| V-253 | Marcas cross-model son gramática de vista (§23), no nuclear |
| V-254 | `Vistas de Requisitos` (`Requirement Views`) son OPDs de vista anclada (V-114) |
| V-255 | `Vistas de Requisitos` (`Requirement Views`) son de solo lectura sobre OPDs fuente |
| V-256 | Ciclo de carga cross-model (`cargado y sincronizado`/`cargado y no sincronizado`/`no cargado`) es propiedad de la referencia |
| V-257 | Operación auxiliar inter-OPD: materializa apariencias existentes, sin crear semántica |
| V-258 | `Bring connected things` filtrada por familia y conectividad directa |
| V-259 | Canon-diagrama indistinguible: Bring vs OPD manual |
| V-260 | `Bring links between selected entities`: materializa enlaces existentes |
| V-261 | Operaciones auxiliares pueden dejar supresores `...` |
| V-262 | OPDs derivados por Bring se clasifican como vista anclada o ad hoc |
| V-263 | Operaciones auxiliares reversibles; no modifican modelo subyacente |

---

## Anexo A — Ratificación D1..D6 aplicada

Las seis decisiones axiomáticas documentadas en `ssot-decisiones-axiomaticas.md` están aplicadas en las siguientes cláusulas:

| Decisión | Cláusulas donde se aplica |
|---|---|
| D1 Apariencia cross-model = existencia compartida por identificador persistente (`URI` o `handle`) | V-123 reescrita (§16.3); V-184; V-185; V-252; V-253; V-256 |
| D2 Sub-model como cuarto par canónico | V-64 reescrita (§18.1); V-242 (§10.1); §23 completa |
| D3 Bring como operador derivado | V-243 (§10.1); §26 completa (V-257..V-263) |
| D4 Invocación como familia autónoma dentro de las cinco familias canónicas | V-239; V-240; V-241 (§3.0) |
| D5 V-114 tres categorías de OPD | V-114 reescrita (§15.4); V-244; V-245; V-113 revisada; V-180; V-181; V-254 |
| D6 Separación de canales del eje `y` | §15.5 completa (V-246..V-250) |

## Anexo B — Decisiones editoriales cerradas

1. **`Current`**: designación persistente adicional de §2.2 (V-237). Marca de estado actual de runtime (V-54, V-133) puede coincidir visualmente, pero la serialización los distingue (V-134, V-238).
2. **Paleta de triángulos**: estrictamente informativa (V-63 ampliada). Topología interna es el canal normativo (V-128).
3. **Apariencias cross-model**: existencia compartida por URI o handle persistente (V-123, V-184, V-252, V-256).
4. **Código ejecutable en canon-documento**: referenciable persistentemente, no obligatoriamente inline (V-172).
5. **Notas, bitmaps, requirement views**: absorbidos en §21.3, §22.5, §23, §19.7.

## Anexo C — Breaking changes respecto a v1

1. **V-64 reescrita**: modelos pueden referenciar otros modelos. Autocontención estricta es perfil propio de implementación.
2. **V-114 reescrita**: árbol de OPDs con tres categorías.
3. **V-123 reescrita**: apariencia ya no subsume a referencia externa; serialización cross-model usa URI o handle persistente.
4. **V-53 y V-54 reescritas**: marcas de proceso activo y estado actual ya no fijadas a una forma única; implementaciones declaran canal reservado.
5. **V-63 ampliada**: colores informativos también para triángulos; topología interna obliga.
6. **§10.1 ampliada a cuatro pares canónicos**: sub-model es mecanismo explícito, no vista.
7. **§3.0 taxonomía declarada**: invocación es familia autónoma, no habilitación.
8. **§15.5 identidad persistente**: `SDx.y` deja de ser referencia estable.

Implementaciones que deseen preservar comportamiento v1 pueden declarar un perfil "v1-compat". La SSOT no publica ese perfil, pero admite su existencia.

## Anexo D — Decisiones explícitamente aplazadas

1. **Forma exacta del identificador persistente del OPD** (UUID, slug, URI).
2. **Formato exacto de serialización cross-model** (JSON-LD, YAML, propietario).
3. **Semántica coalgebraica completa de simulación** — apéndice categorial posterior.
4. **Apéndice categorial formal** — `opm-iso-19450-es.md §Apéndice B`.
5. **Tests categoriales automáticos** — Fase posterior.
