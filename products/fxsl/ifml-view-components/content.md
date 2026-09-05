---
urn: urn:fxsl:kb:ifml-view-components
nombre: ifml-view-components
version: 1.0.0
estado: publicado
descripcion: Corpus IFML — ViewComponents, bindings al domain model, ParameterBinding/DataFlow, subclases (List/Details/Form/MultiChoiceList) y patrones CN/DE/CS.
fuente: Ifml-In-A-Nutshell cap. 5 (Modeling interface content and navigation) — sha256:7f745a18b79183247e237fbe499e2f3687b838984eb05b49586946e6f972a8cb
familia: bok
tags: [ifml, viewcomponent, databinding, parameterbinding, form, omg]
lang: es
cita: [urn:fxsl:kb:ifml-corpus-index, urn:fxsl:kb:ifml-view-containers, urn:fxsl:kb:ifml-actions-events, urn:fxsl:kb:ifml-patrones]
---

# IFML — Contenido y navegacion: ViewComponents

## Resumen

`ViewComponent` modela contenido publicado y entrada del usuario dentro de un `ViewContainer`. Permite navegacion content-dependent (con `ParameterBinding` entre componente fuente y destino), data binding al domain model (`ContentBinding`, `DataBinding`, `DynamicBehavior`) e input via formularios (`Form` con `SimpleField` / `SelectionField`). Tres niveles de abstraccion: `ViewComponent` generico (caja con nombre), bindings al domain model, y subclases especializadas (`List`, `Details`, `Form`, `MultiChoiceList`). Cubre patrones `CN-*` (content/navigation), `DE-*` (data entry) y `CS-*` (content search).

## 1. Niveles de precision del modelado

| Nivel | Detalle | Cuando usar |
| --- | --- | --- |
| Abstracto | `ViewComponent` es solo `box with a name` | Modelo preliminar, exploracion |
| Intermedio | Binding al domain model via `ContentBinding`/`DataBinding` | Consistencia entre IFML y domain model; query generation automatica |
| Refinado | Subclases especializadas con propiedades domain-dependent (List, Details, Form, MultiChoiceList) | Model checking profundo, code generation completo |

## 2. ViewComponent y ViewComponentPart

**ViewComponent** — elemento que muestra contenido en la UI o acepta input del usuario.

Ejemplos: visualizacion de un objeto, lista de objetos, data entry form, grid editable, image gallery.

**ViewComponentPart** — elemento de interfaz o propiedad estructural que no vive fuera del contexto de un `ViewComponent`.

La semantica concreta de ambos es deliberadamente abierta: la fija el diseñador via el nombre. Niveles superiores de especializacion la endurecen.

## 3. Navegacion content-dependent

Casos:

- seleccion de un item de una lista para ver su detalle.
- display de resultado de busqueda por keyword.
- drill-down en una jerarquia.

Diferencias con la navegacion content-independent (capitulo `ViewContainers`):

| Aspecto | Content-independent | Content-dependent |
| --- | --- | --- |
| Origen / destino | Tipicamente `ViewContainer` | Tipicamente `ViewComponent` |
| Dependencia de datos | No requiere | El destino requiere input del origen, expresado por `ParameterBinding` |

### 3.1 Mecanica del NavigationFlow entre ViewComponents

El evento de navegacion en `ViewComponent` causa display del `ViewContainer` destino y triggering del computo de los `ViewComponent` que contiene.

Efecto sobre el origen:

- si fuente y destino estan en `ViewContainer` mutually-exclusive (directo o por anidamiento): el destino reemplaza al origen.
- caso contrario: el destino se muestra ademas del origen.

Si origen y destino estan en el mismo `ViewContainer`, la seleccion en el origen causa display del detalle en el mismo contenedor.

## 4. ContentBinding y especializaciones

**ContentBinding** — representacion general del content source de un `ViewComponent`. Atributo: URI del recurso del cual se obtiene el contenido.

Ejemplo basico: feed reader cuyo `ContentBinding` es la URL del feed provider.

Especializaciones:

- **DataBinding** — provenance desde objetos del domain model.
- **DynamicBehavior** — provenance desde invocacion operacional de servicio o metodo.

### 4.1 DataBinding

**DataBinding** — provenance del contenido desde objetos del domain model. Caracterizado por:

- referencia a un concepto del domain model (UML classifier, XML element, tabla relacional, etc.).
- **ConditionalExpression** (OCL) que selecciona instancias.
- una o varias **VisualizationAttribute** que indican atributos a publicar.
- **OrderBy** opcional (`ViewComponentPart`) con criterios de sort: atributo + direccion (ASC/DESC).

Ejemplo:

```ocl
self.isRead = false
```

Aplicada al `DataBinding` de `MailMessage`, restringe la publicacion a mensajes no leidos. El contexto OCL queda implicito como la entidad referenciada por el `DataBinding`.

### 4.2 DynamicBehavior

**DynamicBehavior** — representa el data access de un `ViewComponent` de forma operacional (invocacion de servicio o metodo que retorna contenido).

Puede expresarse referenciando cualquier `UMLBehavior` o `UMLBehavioralFeature`. Ejemplo: `TweetList` cuyo contenido se obtiene de la web API de un servicio externo.

## 5. ParameterBinding y ParameterBindingGroup

**ParameterBinding** — asocia el valor de un parametro (output de un `ViewComponent`) con el valor de otro parametro (input de otro `ViewComponent` o `Action`).

**ParameterBindingGroup** — agrupacion cuando la dependencia involucra varios parametros simultaneos.

Ejemplo (mailbox → message list):

```ocl
self.MailMessageGroup = MailBox
```

`SelectedMailBox` (output de `MBoxList`) → `MailBox` (input de `MessageList`). El OCL selecciona `MailMessage` instances asociadas via association role `MailMessageGroup` con el objeto identificado por `MailBox`.

### 5.1 DataFlow

**DataFlow** — `InteractionFlow` que especifica que algunos parametros se pasan de origen a destino sin interaccion del usuario; los parametros se especifican via `ParameterBindingGroup` asociado al `DataFlow`.

Caracteristicas:

- emana directamente de `ViewComponent` (no de eventos).
- notacion: flecha discontinua (vs `NavigationFlow` con flecha continua).

Caso tipico: en un detail-multidetail (`CN-MMD`), seleccionar un `Contact` causa display de `ContactInfo` y display simultaneo de `Addresses` y `Emails` cuyo input (ID del contacto) se provee por `DataFlow` desde `ContactInfo`.

## 6. Especializaciones de ViewComponent

### 6.1 List

**List ViewComponent** — muestra una lista de objetos retrieved via `ContentBinding`. Asociado a un `Event`, cada objeto puede disparar el evento. Al disparar, las instancias elegidas se pasan como parameter al destino.

### 6.2 Details

**Details ViewComponent** — muestra los valores de atributos de un objeto via `ContentBinding`. Asociado a un evento, la instancia mostrada puede disparar el evento.

### 6.3 SelectEvent

**SelectEvent** — extension de `Event` que soporta seleccion de uno o varios elementos de un set. Al disparar, pasa el valor o valores como parameter al destino del `NavigationFlow`.

Una variante adicional de `SelectEvent` (introducida en el capitulo de actions) soporta `select all`: seleccion del set completo.

### 6.4 MultiChoiceList

**MultiChoiceList** — habilita seleccion y submission de multiples instancias. Soporta varios eventos:

| Evento | Semantica |
| --- | --- |
| `select` | Seleccion estandar de un elemento |
| `check` / `uncheck` | Aplicar o remover marca de seleccion en cualquier elemento |
| `set selection` | Submission del set entero |
| `submit` | Submission de los objetos actualmente seleccionados |

### 6.5 Form

**Form ViewComponent** — representa un data entry form. Comprende uno o varios `ViewComponentPart` etiquetados como `Field`.

**Field** — subelemento de `Form` que denota un valor tipado entrado por el usuario o mostrado al usuario. Representa parametros para pasar valores a otros elementos IFML. Dos clases: `SimpleField` y `SelectionField`.

| Tipo | Funcion |
| --- | --- |
| `SimpleField` | Captura valor tipado entrado por usuario. Puede ser read-only o hidden. Output parameter pasable a otros ViewElement o `Action` |
| `SelectionField` | Permite eleccion de uno o varios valores desde un conjunto predefinido |

Ambos pueden preloadearse:

- `SimpleField` preloadeado: muestra valor que el usuario puede sobreescribir.
- `SelectionField` preloadeado: muestra varios valores que el usuario puede elegir.
- preload via `ContentBinding` (desde domain) o via `ParameterBinding` (desde otro elemento de la interfaz, asociado al `Form` que contiene el `Field`).

### 6.6 SubmitEvent

**SubmitEvent** — extension de `Event` que denota submission de uno o varios valores. Dispara parameter passing del `ViewComponent` que lo posee al `ViewComponent` o `Action` destino del `NavigationFlow`.

Ejemplo: form `MessageKeywordSearch` con `SearchKey` SimpleField y `Search mail` SubmitEvent. El submit dispara display de `MessageList` con OCL:

```ocl
if (keyword.size <= title.size) then
 Sequence(1..title.size- Keyword.size) -> exists(i|
 title.substring(i,i+Keyword.size) = Keyword)
 else
 false
```

## 7. Patrones de contenido y navegacion (CN-*)

Patrones platform-independent de content/navigation. Prefijo `CN`.

### 7.1 CN-MD: Master Detail; CN-MMD: Master Multidetail

**Master Detail (`CN-MD`)** — patron mas simple de data access. `List` presenta master list; `SelectEvent` accede al detalle de una instancia a la vez.

**Master Multidetail (`CN-MMD`)** — variante donde el objeto seleccionado se publica en mas de un `ViewComponent` simultaneamente.

### 7.2 CN-MLMD: Multilevel Master Detail

Tambien llamado `cascaded index`. Secuencia de `List` sobre clases distintas; cada `List` cambia el foco de un objeto seleccionado al set de objetos relacionados via association role. Termina en un `Details` de un objeto unico, o en un `List` de varios objetos.

Caso tipico: usar access classes para construir un navigation path hacia instancias de una core class. Ejemplo: `Category` → `Product`.

### 7.3 CN-DEF: Default Selection

Resuelve la inestabilidad del basic master detail al inicio: cuando el `ViewContainer` se accede por primera vez, el `Details` o `List` dependiente de un parameter aun no provisto exhibe `empty hole`; al primer click del usuario el hueco se llena causando shift visual no deseado.

Solucion del patron:

- elegir un valor por defecto en el `ViewComponent` fuente y usarlo para definir el parameter del destino.
- agregar un `DataFlow` (ademas del `NavigationFlow` del `SelectEvent`) que expresa parameter passing inicial sin interaccion del usuario.

## 8. Patrones de data entry (DE-*)

Prefijo `DE`. Basados en `Form` con sus extensiones.

### 8.1 DE-FRM: Multifield Forms

`Form` con varios fields correspondientes a propiedades del objeto a crear/actualizar, criterios de busqueda, o parametros de servicio externo.

Asignar tipos a los fields agrega informacion para code generation: text editor rich text, blob field con file chooser, boolean como radio, date como calendar.

### 8.2 DE-PLDF: Preloaded Field

Aplicable cuando el data entry modifica informacion existente (update de descripcion de producto, edicion de perfil).

Dos formas de preload:

- via `DataBinding` en el field (extrae valores del domain model).
- via `ParameterBinding` asociado a `DataFlow` desde otro componente.

### 8.3 DE-PASF: Pre-assigned Selection Field

Inferencia del valor desde profile data, choices previas o context. `SelectionField` inicializado via `ParameterBinding`.

Ejemplo: `UserCountry` `Details` retrieve el pais por defecto del `Locale` ContextVariable, expone `UserCountry` como output, lo pasa al `Form` como input parameter `CountryPreselect` que setea el valor del `Country` SelectionField. Conexion via `DataFlow` por no requerir interaccion.

### 8.4 DE-DLKP: Data Lookup

Util cuando el data entry involucra eleccion entre muchas opciones (catalogo grande). Un `SelectionField` se respalda con un `ViewContainer` de data lookup que contiene un patron como master detail.

Ejemplo: form `FillRequest` con `ProductCode` `SimpleField`. El evento `Pick` abre `ViewContainer` (modal window) donde el usuario navega la taxonomia y selecciona el codigo. El codigo elegido se asigna al `SimpleField` via `ParameterBinding`.

### 8.5 DE-CSF: Cascade Selection Fields

Aplica cuando el data entry involucra selecciones con dependencia. Caso tipico: address con country → state/province → city.

Mecanica: la seleccion de un elemento en un `SelectionField` dispara el calculo de la lista del siguiente. La lista de states depende del country seleccionado; la lista de cities depende del state.

### 8.6 DE-WIZ: Wizard

Particion de un data entry procedure en pasos logicos secuenciales. El usuario puede ir adelante y atras sin perder selecciones parciales.

Mecanica:

- en cada step, el `Form` muestra un `Field` y cachea valores de inputs anteriores en `Parameter`.
- eventos de navegacion entre steps llevan `ParameterBinding` con valores acumulados.
- diseño alternativo equivalente: asociar copia unica de todos los wizard parameters al `ViewContainer` enclosing y actualizar globalmente en cada previous/next event.

## 9. Patrones de busqueda (CS-*)

Prefijo `CS`.

### 9.1 CS-SRC: Basic Search

`Form` con un `SimpleField` para keyword. La key se usa como parameter en la `ConditionalExpression` de un `List` que muestra todas las instancias que contienen el keyword.

Variante multi-attribute con disjunctive subclauses:

```ocl
if (keyword.size <= title.size) then
 Sequence(1..title.size - Keyword.size) -> c(i|
 title.substring(i, i + Keyword.size) = Keyword)
 else
 false
```

`OR`

```ocl
if (keyword.size <= body.size) then
 Sequence(1..body.size - Keyword.size) -> exists(i|
 body.substring(i, i + Keyword.size) = Keyword)
 else
 false
```

Busca el keyword en title o body del mensaje.

### 9.2 CS-MCS: Multicriteria Search

`Form` con multiples `Field` que expresan criterio compuesto. `ParameterBindingGroup` asigna los field values a parametros de la `ConditionalExpression` del `List` destino.

### 9.3 CS-FSR: Faceted Search

Modalidad de retrieval para datos estructurados multidimensionales. Refinamiento progresivo restringiendo el match por valores de propiedades llamadas **facets**.

Ejemplo aplicado a bibliografia: `ViewContainer` con `Form` para keywords, `List` para `Results`, dos `MultiChoiceList` (`Years`, `Venues`) para facet values.

Mecanica:

- al primer acceso, `Results`, `Years`, `Venues` no se muestran (`ConditionalExpression` evalua false).
- al submit del keyword, los tres componentes se computan con los matches.
- check/uncheck de facets dispara eventos que bindean `Years` y `Venues` parameters.
- la `ConditionalExpression` de `Results` re-evalua usando esos parameters; si no son vacios, restringe el set.

`VisualizationAttribute` de `Years`/`Venues` comprende un solo atributo cuyo distinct values se muestra como facets.

## 10. Aspectos de inferencia automatica

Cuando los componentes son especializados (`List`, `Details` con un `SelectEvent` que pasa instancias seleccionadas), la herramienta o el lector humano puede inferir `ParameterBinding` y `ConditionalExpression` sin que el modelador los explicite. Esto reduce la verbosidad del modelo manteniendo la semantica.

Ejemplo: un `List` que publica instancias de `MailMessage` + `Details` que publica una instancia + `SelectEvent` que pasa el item elegido. El binding implicito es trivial; el modelo puede omitirlo.

## 11. Paso de parametros sin interaccion (DataFlow)

Cuando dos `ViewComponent` correlacionados deben mostrarse simultaneamente al seleccionar un objeto en una lista (master multidetail), el paso de parametros entre ellos no requiere interaccion: se modela con `DataFlow` y `ParameterBinding`. Conexion `Details` → `Details` o `Details` → `List` que recibe instancias asociadas via association role del domain model.
