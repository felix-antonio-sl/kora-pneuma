---
urn: urn:fxsl:kb:ifml-view-containers
nombre: ifml-view-containers
version: 1.0.0
estado: publicado
descripcion: "Composicion de la interfaz en IFML: ViewContainer (anidamiento conjuntivo/disyuntivo, navegacion content-independent, Default/Landmark, Window/Modal/Modeless), adaptacion contextual (Context/ViewPoint) y patrones de organizacion OD/OW/OM."
fuente: "Migrado de la bestia (~/kora) artifacts/knowledge/fxsl/ifml/ifml-view-containers.md (sha256:5a6c423d424c0a68e21a6ce81ff75b75e94149773a91d8c7d384cc5298d6aff5); cuerpo integro, solo se aplano el frontmatter. Fuente original: Ifml-In-A-Nutshell cap.4 (Modeling the composition of the user interface), estandar IFML/OMG."
autor: FS
creado: 2026-05-07
lang: es
tags: [ifml, viewcontainer, navegacion, contexto, viewpoint, omg]
familia: bok
cita: [urn:fxsl:kb:ifml-corpus-index, urn:fxsl:kb:ifml-fundamentos, urn:fxsl:kb:ifml-patrones]
---

# IFML — Composicion de la interfaz: ViewContainers

## Resumen

`ViewContainer` modeliza la composicion jerarquica de la interfaz en IFML: contenedores anidados (conjuntiva o disyuntiva), navegacion content-independent, propiedades de relevancia (`Default`, `Landmark`), especializaciones (`Window` con `Modal`/`Modeless`) y mecanismos de adaptacion contextual (`Context`, `ContextDimension`, `ActivationExpression`, `ContextVariable`, `ViewPoint`). Este capitulo cubre los patrones de organizacion `OD-*` (desktop), `OW-*` (web) y `OM-MSL` (mobile).

## 1. Definicion de ViewContainer

**ViewContainer** — elemento de la interfaz que agrega otros view containers o view components.

Puede representar:

- artefacto fisico: window, page de aplicacion web.
- agregacion logica: seccion de portal compuesta por varias paginas con tema homogeneo.

Soporta navegacion (cambio de foco de un contenedor a otro). Para que sea fuente de un comando de navegacion debe asociarsele un `Event`.

### 1.1 Constructos asociados de navegacion

- **Event** — ocurrencia que afecta el estado. Tipos: `ViewElementEvent` (interaccion del usuario), `ActionEvent` (terminacion de accion), `SystemEvent` (notificacion del sistema).
- **ViewElementEvent** — evento disparado por el usuario al interactuar con `ViewContainer`, `ViewComponent` o `ViewComponentPart`.
- **NavigationFlow** — arco dirigido que conecta el evento con el `ViewContainer` destino. Conecta eventos de containers, components, parts o actions con otros containers, components, parts o actions.

Notacion: el evento como circulo asociado al contenedor; `NavigationFlow` como flecha sin etiqueta. Caracteristicas del modelo (nombres de containers, nombres de eventos) pueden reutilizarse en la implementacion: titulo de window, URL/nombre de pagina, texto de hyperlink anchor o boton.

## 2. Anidamiento de ViewContainers

Las interfaces organizan contenido en estructuras regulares para usabilidad. Ejemplos: paginas web con area central + columnas laterales; ventanas con paneles tabulados.

### 2.1 Plataformas: dos extremos

| Plataforma | Composicion tipica |
| --- | --- |
| Window-based (Java Swing, .NET Forms) | Un `ViewContainer` top-level que contiene todo |
| Pure HTML web | Conjunto de page templates independientes; no hay top-level; uno se elige como `Home Page` |
| Rich Internet / single page apps | Hibrido entre los dos extremos |

### 2.2 Forma conjuntiva vs disyuntiva

| Forma | Comportamiento | Notacion |
| --- | --- | --- |
| Conjuntiva (default) | Hijos se muestran simultaneamente | Sin etiqueta especial |
| Disyuntiva (XOR) | Mostrar uno reemplaza al otro | Etiqueta `XOR` antes del nombre del contenedor enclosing |

Al acceder a un padre disyuntivo, alguno puede marcarse como **default**: se muestra cuando no hay seleccion explicita.

## 3. Navegacion content-independent

`ViewContainer` soporta navegacion content-independent: cambio de foco que no depende del contenido del origen ni del destino.

Caracteristicas:

- expresada por un `Event` asociado al contenedor + `InteractionFlow` al destino.
- no requiere `ParameterBinding` para computar el contenido del destino.
- se contrasta con la navegacion content-dependent (capitulo de `ViewComponents`), donde fuente y destino son `ViewComponent` y la dependencia I/O es explicita.

## 4. Propiedades de relevancia

### 4.1 Default ViewContainer

`Default` — se muestra automaticamente cuando se accede al contenedor padre.

Notacion: `[D]` en la esquina superior izquierda.

### 4.2 Landmark ViewContainer

`Landmark` — alcanzable desde todos los contenedores hermanos y sus subcontenedores anidados dentro del enclosing comun.

Notacion: `[L]` en la esquina superior izquierda.

Equivalencia con flujos explicitos: marcar `Landmark` equivale a tener `NavigationFlow` implicitos desde cada contenedor hermano hacia el. La propiedad `Landmark` no aumenta poder expresivo, pero reduce la carga visual del diagrama y mejora legibilidad cuando hay muchos contenedores.

## 5. Window y especializaciones

`Window` es una especializacion de `ViewContainer` que representa una ventana de UI. Variantes via stereotype:

| Stereotype | Comportamiento de navegacion |
| --- | --- |
| `Window` (default) | El contenedor destino reemplaza al origen en pantalla |
| `Modal` | Se superpone al origen y deshabilita la interaccion con la(s) ventana(s) de fondo |
| `Modeless` | Se superpone al origen pero permite interaccion con otras piezas de la UI |

Notacion: stereotype del clasificador `ViewContainer`. Ejemplos tipicos: wizard step (`Window`), submission confirmation (`Modal`), tools menu (`Modeless`).

## 6. Adaptacion contextual

La interfaz puede no ser estatica: muchas aplicaciones la actualizan en runtime segun el contexto (posicion del usuario, perfil, dispositivo, hora). IFML provee constructos para distinguir adaptaciones de design-time y los valores de runtime usados para decidirlas.

### 6.1 Context y ContextDimension

- **Context** — descriptor de los aspectos runtime que determinan como se adapta la interfaz.
- **ContextDimension** — componente de un `Context`. La nocion es deliberadamente amplia: identidad, rol, posicion geografica, dispositivo, conectividad de red, hora, etc.

Extensiones predefinidas en el estandar:

- **UserRole** — rol que cumple el usuario; atributos del perfil para habilitar el contexto.
- **Device** — caracteristicas del dispositivo (tamaño, resolucion, capacidad).
- **Position** — disponibilidad de location y orientation.

Las extensiones predefinidas se pueden refinar para representar dimensiones mas finas (network connectivity, aspectos temporales).

### 6.2 ActivationExpression

**ActivationExpression** — condicion booleana en OCL que determina si el `Context` (u otro elemento IFML) esta activo (true) o inactivo (false).

Notacion: anotacion stereotyped asociada al elemento. Ejemplo de OCL conceptual:

```ocl
self.UserRole.RoleName = 'Customer' and
self.Device.Type = 'Tablet' and self.Device.Size = 'Small'
```

La evaluacion requiere que los valores de las `ContextDimension` se registren en runtime.

### 6.3 ContextVariable

**ContextVariable** — variable runtime que mantiene informacion del usage context.

Especializa en:

- **SimpleContextVariable** — valor de tipo primitivo.
- **DataContextVariable** — referencia a un `DataBinding`.

Usos:

- en `ActivationExpression` asociadas a `ViewElement` para condicionar visibilidad por situacion (adaptacion fina).
- como parametros para publicar contenido del schema de personalizacion (perfil del usuario, permisos del role).

### 6.4 ViewPoint

**ViewPoint** — especificacion de un modelo de interfaz completo activo solo cuando un `Context` especifico esta habilitado.

Habilitacion dinamica gobernada por la `ActivationExpression` del `Context` asociado. Permite definir variantes de la interfaz por rol, plataforma u otro criterio. Cuando el contexto se activa, todos los `ViewElement` y `Event` del `ViewPoint` se vuelven activos.

### 6.5 Pipeline de adaptacion

```
ContextDimensions -> dimensiones habilitantes
ActivationExpression -> requisitos sobre las dimensiones
ContextVariables -> valores runtime del usuario actual
match dimensions = required -> Context activo -> ViewPoint activado
```

Adaptacion fina: usar `ContextVariable` directamente en `ActivationExpression` de elementos individuales (visibilidad por situacion).

Acoplamiento con personalizacion:

- `ContextVariable` con identidad (ej. `username`) → lookup de instancia `User`, retrieve de profile data, publicacion en interfaz.
- `ContextVariable` con role → lookup de instancia `Group`, retrieve de permisos, adaptacion del contenido y acciones.

## 7. Patrones de organizacion de interfaz

Convencion de nombres: `XY-Z` donde X es categoria (`O` para organization), Y es plataforma (`D`/`W`/`M`/`G`), Z es mnemonico.

### 7.1 Patrones desktop (OD-*)

`ViewContainer` topmost unico con jerarquia interna de subcontenedores.

| Codigo | Nombre | Estructura |
| --- | --- | --- |
| `OD-SWA` | Simple Work Area | Top-level con sub-`ViewContainer`: un work area + uno o varios service areas (menus, tool bars, console) |
| `OD-MWA` | Multiview Work Area | Extension de `OD-SWA` con multiples vistas alternativas del item en el work area (ej. normal vs zoom de imagen) |
| `OD-CWA` | Composite Work Area | Work area dividida en subregions devotas a subtareas presentadas simultaneamente (ej. main editor + side panels) |
| `OD-MCWA` | Multiview Composite | Combinacion de `OD-MWA` y `OD-CWA`: perspectivas alternativas, cada una con vistas parciales simultaneas (ej. IDE con edit view + debug view) |

### 7.2 Patrones web (OW-*)

`ViewContainer` anidados expresan dos roles posibles:

- regiones de pagina (HTML frames, JavaScript layouts).
- clusters logicos de paginas con caracteristicas comunes (modularizacion, cross-site navigation).

| Codigo | Nombre | Caso |
| --- | --- | --- |
| `OW-MFE` | Multiple Front-Ends | Multiples roles sobre el mismo domain model (CMS con editor + reader). Top-level por rol; pagina de login publica comun. Ventajas: modularizacion, RBAC por contenedor, separacion de assets/deployment |
| `OW-LWSA` | Large Web Sites Organized into Areas | Site con jerarquia hierarchical de areas/subareas (`ViewContainer` anidados como site areas), tipico en sites grandes con barra de navegacion por areas |

`OW-MFE` se combina tipicamente con `Context` + `ViewPoint`: cada rol tiene su `Context` con `ActivationExpression` sobre `UserRole`, asociado a su `ViewPoint`.

### 7.3 Patron mobile (OM-*)

| Codigo | Nombre | Estructura |
| --- | --- | --- |
| `OM-MSL` | Mobile Screen Layout | Grid top-level con tres regiones: header (menus, notificaciones del SO), content area (layout simple, scroll en una sola dimension), footer (system commands, settings) |

Caracteristicas dominantes en mobile:

- pantalla reducida → uso consistente del espacio.
- contexto de uso incomodo (de pie, caminando) → minimizar interacciones.
- header parcialmente reservado al SO (notificaciones), fijo cross-application.
- content area limita perspectivas multiples y nested panes; scroll vertical predominante.

Las extensiones mobile especificas (sensor-aware, gestos, multiscreen) se cubren en su capitulo dedicado.

## 8. Implicaciones de diseño

- la propiedad `Landmark` reduce sustancialmente el numero de eventos y `NavigationFlow` que un diagrama debe contener; preferir cuando hay alta inter-conectividad sibling.
- la distincion `XOR` vs conjuntiva es decisiva para determinar si un destino reemplaza o coexiste con el origen.
- `Window` con `Modal`/`Modeless` debe reservarse cuando la semantica de bloqueo de fondo importa; no es un sustituto de navegacion ordinaria.
- el `Context` + `ViewPoint` solo paga su prima si la aplicacion realmente cambia su composicion en runtime; sobreestructura para cambios estaticos (que pueden modelarse con `ActivationExpression` sobre elementos individuales).
