---
urn: urn:fxsl:kb:ifml-extensiones-web
nombre: ifml-extensiones-web
version: 1.0.0
estado: publicado
descripcion: "Extensiones web de IFML: container types direccionables (Page/Area/SiteView), RBAC via Security/Protection/ActivationExpression, WebNavigationFlow (Rel/Target) y variantes de List (DynamicSortedList/ScrollableList/NestedList)."
fuente: "Migrado de la bestia (~/kora) artifacts/knowledge/fxsl/ifml/ifml-extensiones-web.md (sha256:62c77be84b5634e066db827a8fce7707ef977581ab6a6e1a9ce088cdfe653ecf); cuerpo integro, solo se aplano el frontmatter. Fuente original: Ifml-In-A-Nutshell cap.7 (Web Extensions), estandar IFML/OMG."
autor: FS
creado: 2026-05-07
lang: es
tags: [ifml, web, page, area, siteview, webnavigationflow, rbac, omg]
familia: bok
cita: [urn:fxsl:kb:ifml-corpus-index, urn:fxsl:kb:ifml-view-containers, urn:fxsl:kb:ifml-view-components]
---

# IFML — Extensiones web

## Resumen

Extensiones IFML para aplicaciones web: container types con direccionamiento (`Page`, `Area`, `SiteView`), navigation flow especializado (`WebNavigationFlow`) con propiedades hypertext, y componentes refinados (`DynamicSortedList`, `ScrollableList`, `NestedList`). El modelado web fusiona conceptos de hypertext (page, link), multimedia y form-based GUIs, y agrega concerns de seguridad (HTTPS, RBAC) ausentes en desktop puro.

## 1. Container extensions: Page, Area, SiteView

### 1.1 Page

**Page** — extension de `ViewContainer` que denota una unidad de interfaz web direccionable.

Caracteristicas:

- producida estaticamente por editor humano o generada dinamicamente en server-side (page template, server-side script).
- como interfaz: embebe comandos de navegacion.
- como recurso del sistema documental: tiene URL legible.
- en aplicaciones grandes: puede arreglarse jerarquicamente para facilitar navegacion.

### 1.2 Area

**Area** — extension de `ViewContainer` disjunctivo (XOR) que denota una coleccion de `Page` u otros `Area`, agrupados por proposito application-specific.

Ejemplos en e-commerce: products, special deals, shipping rates, returns and complaints.

### 1.3 SiteView

**SiteView** — extension de `ViewContainer` disjunctivo (XOR) que denota areas y pages agrupadas por proposito application-specific, tipicamente porque sirven a un `UserRole`.

Caracteristicas:

- el `SiteView` es el item tipicamente referenciado por un `ViewPoint`.
- activation rules definen: `SiteView` activado para un `UserRole` particular.
- `SiteView` sin role asociado se trata como publico (accesible incluso con `UserRole` indeterminado).

### 1.4 Pipeline de RBAC en web app

```
SiteView/Area/Page ----associated with----> ActivationExpression --on--> UserRole
 |
 +-- as resource of role-based access control
 +-- referenced by ViewPoint
 +-- ViewPoint enabled when Context active

Definicion de activation rules sobre SiteView/Area/Page == permiso de acceso para ese UserRole.
```

Ejemplo en e-commerce: `SiteView` distintos para `registered customer`, `product content manager`, `sales manager`. Public `SiteView` para non-registered customers.

## 2. Propiedades adicionales de Page/Area/SiteView

| Propiedad | Significado |
| --- | --- |
| URL label | String que denota la parte fija de la direccion. Para template dinamico se concatena con parameters de computo. URL de `SiteView`/`Area` es alias del home/default `Page` interno |
| Security | Si valor `secured`: todas las pages se sirven via HTTPS |
| Protection | Si valor `protected`: las pages estan sujetas a control de acceso definido por `ActivationExpression` con `UserRole` |

Concepto de redundancia intencional: la asociacion de `UserRole` con multiples niveles de nesting (`Page`, `Area`, `SiteView`) es redundante y permite expresion incremental de access control. Ejemplo: `SiteView` accesible a `Role1` y `Role2`; `Area` o `Page` interno con `ViewPoint` mas restrictivo (solo `Role1`).

**Home page** — pagina servida cuando se accede sin solicitar recurso especifico. Concepto crucial en web apps.

## 3. WebNavigationFlow

**WebNavigationFlow** — extension de `NavigationFlow` que incorpora propiedades especificas de hypertext links.

Propiedades adicionales:

| Propiedad | Funcion |
| --- | --- |
| `Rel` | Relacion entre el documento actual y el linkeado; valores codificados por estandar HTML |
| `Target` | Donde abrir el documento linkeado, tipicamente browser window: misma o nueva |

Caso tipico: link saliente desde technical manual a licensing information, abriendo en nueva ventana e informando a search engines la naturaleza del enlace via `Rel`.

Tradeoff explicit del estandar: `Rel` y `Target` dependen de la version de HTML, que es lenguaje de implementacion. Como un code generator puede explotar esa info para inyectar atributos HTML correctos en miles de links auto-generados, el estandar elige **utilidad sobre pureza** (las propiedades son definibles directamente en el modelo). Alternativa pura seria factorizarlas y entrelazarlas con el code generator.

## 4. Component extensions: List variants

El `List` core ofrece funcionalidad minimalista. Tres extensiones lo enriquecen para necesidades web reales.

### 4.1 DynamicSortedList

`OrderBy` core (en `ifml-view-components`) define sort criteria en design-time, no permite que el usuario reordene en runtime.

**DynamicSortedList** — extension de `List` que permite ordenar datos usando visualization attributes en runtime.

Componentes:

- asociacion one-to-many `SortAttributes` con la metaclass `VisualizationAttribute`.
- `SortAttributes` denota el subset de visualization attributes usables para sort.

Default ordering puede definirse por `OrderBy` `ViewComponentPart`; el usuario lo sobreescribe usando `SortAttributes`.

### 4.2 ScrollableList

Comportamiento de paging: lista larga particionada en bloques de tamaño fijo con comandos de scroll. Variante: scroll de bloques de objetos individuales (image gallery).

**ScrollableList** — extension de `List` que permite acceso a instancias `DataBinding` ordenadas, agrupadas en bloques.

Componentes:

| Elemento | Funcion |
| --- | --- |
| Atributo `block size` | Numero de instancias por bloque |
| Implicit parameter `current` | Bloque actualmente en vista |
| Implicit events | Moverse a primero, ultimo, i-esimo, siguiente, anterior |

Caso tipico: search engine results paginados; el patron de search basico (`CS-SRC`) se reformula con `ScrollableList` para soportar paging.

### 4.3 NestedList

Compactacion del patron multilevel master detail (`CN-MLMD`) en un unico `ViewComponent`.

**NestedList** — extension de `List` que denota nesting de multiples lists, una dentro de otra.

Modelo de datos:

- top-level `DataBinding` que referencia una clase del domain.
- dentro: uno o mas first-level `NestedDataBinding` referencias a association roles de la clase.
- cada first-level `NestedDataBinding` puede contener one o mas second-level `NestedDataBinding`.
- second-level referencia un association role de la clase target del first-level.

Ejemplo tres niveles: catalogo de productos. Top: `Category`. Segundo: `Product` por categoria. Tercero (dentro de `Product`): dos nested lists, `accessories` y `frequently bought together`. Seleccion en segundo o tercer nivel publica el objeto en `ProductDescription` o `AccessoryDescription` `ViewContainer`.

## 5. Razon de fondo de las extensiones web

Las web applications fusionaron areas previamente separadas: hypertext (paginas, links), multimedia y form-based GUIs. Los conceptos fundamentales son `Page` y `link`, originalmente de hypertext documents. Ambos son especializaciones de conceptos core IFML (`ViewContainer` y `NavigationFlow`).

Las web apps multi-usuario sobre arquitectura multi-tier client-server agregan dos concerns nuevos:

- **seguridad de transmision** — entrega via HTTPS.
- **control de acceso** — autenticacion, identificacion, permission control.

Estas dimensiones se modelan via `Security` y `Protection` en `Page`/`Area`/`SiteView` y via `Context`/`ViewPoint`/`UserRole` (ya cubiertos en `ifml-view-containers`).

## 6. Implicaciones de diseño

- usar `Page` cuando importe el direccionamiento (URL); usar `ViewContainer` plano cuando no.
- `Area` es la herramienta natural para modularizar sites grandes; preferirla sobre nested `ViewContainer` sin proposito.
- `SiteView` paga su prima cuando hay multiple roles con interfaces distintas; sino, un `ViewContainer` simple basta.
- `WebNavigationFlow` solo es necesario cuando `Rel` o `Target` aportan al code generation; sino, `NavigationFlow` core es suficiente.
- `NestedList` reduce la verbosidad de `CN-MLMD` cuando los tres niveles caben semanticamente en un solo componente.
