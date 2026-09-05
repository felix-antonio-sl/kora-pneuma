---
urn: urn:fxsl:kb:ifml-extensiones-desktop
nombre: ifml-extensiones-desktop
version: 1.0.1
estado: publicado
descripcion: "Extensiones IFML para aplicaciones desktop (Java Swing, Windows Forms, RIA): nuevos events (OnFocusLost, OnDragStart/OnDrop), componentes Tree/Table y EditableSelectionField, con criterios para extender y caveats de notacion."
fuente: "Migrado de la bestia (~/kora) artifacts/knowledge/fxsl/ifml/ifml-extensiones-desktop.md (sha256:4339ea54dead75f384dc80705a15fc2464550fa53ea6b3c3d3fae63b45c4e3f3); cuerpo IFML ya koraficado, preservado integro (FS=100%, sin recomprimir; solo se aplano el frontmatter anidado). Fuente original: Ifml-In-A-Nutshell, capitulo 7 seccion Desktop Extensions, manual del estandar IFML/OMG. v1.0.1 (2026-06-23): correccion de fidelidad OMG (revision adversarial dov-dori, verificada contra corpus) — el portador de los dos input parameters del OnDrop (seccion 4) es `ParameterBindingGroup`, no `DataBindingGroup`; este ultimo no es primitiva IFML (`DataBinding` es content-source al domain, no agrupacion de parametros de un InteractionFlow). Consistente con el uso del constructo en el resto del corpus."
autor: FS
creado: 2026-05-07
lang: es
tags: [ifml, desktop, extensions, dragdrop, tree, table, omg]
familia: bok
cita: [urn:fxsl:kb:ifml-corpus-index, urn:fxsl:kb:ifml-view-components, urn:fxsl:kb:ifml-actions-events]
---

# IFML — Extensiones desktop

## Resumen

Extensiones IFML para aplicaciones desktop (Java Swing, Windows Forms, rich Internet apps): nuevos tipos de event (`OnFocusLost`, `OnDragStart`, `OnDrop`), componentes especializados (`Tree`, `Table`) y refinamiento de fields (`EditableSelectionField`). Las extensiones se justifican por el control fino del usuario sobre la interfaz tipico de desktop y por el aporte concreto a model checking y code generation.

## 1. Mecanismo de extension

El estandar IFML viene como core + extensiones. El mecanismo aplica a todos los conceptos principales: `ViewContainer`, `ViewComponent`, `ViewComponentPart`, `Event`, `ContextDimension`, expressions.

Extensiones ya provistas en el estandar:

- `ViewContainer`: `Window`.
- `ViewComponent` y `ViewComponentPart`: `Details`, `Field`, `Form`, `List`, `SelectionField`, `SimpleField`, `Slot`.
- `Event`: `SelectEvent`, `SubmitEvent`, `SystemEvent`.
- `ContextDimension`: `Device`, `Position`, `UserRole`.
- `Expression`: `ValidationRule`.

Custom extensions adicionales son admisibles para todos los main concepts. Propositos de las extensiones:

- agregar poder expresivo al lenguaje.
- hacer conceptos y notacion menos abstractos, mas cercanos a la intuicion.
- distinguir visualmente conceptos especializados (mejor legibilidad).
- asignar semantica precisa para enable model checking, formalizacion y executability.

## 2. Criterios para extender un Event type

Preguntas de diseño cuando se considera un nuevo event type:

- con que `ViewElement` puede asociarse: `ViewContainer`, `ViewComponent`, `ViewComponentPart`, especializaciones, mix?
- restriccion en el tipo de `ViewElement` que puede ser destino del `InteractionFlow`?
- que parameters pueden asociarse al `InteractionFlow` conectado al evento?

## 3. OnFocusLost

**OnFocusLost** — extension de `ViewElementEvent` que captura la perdida de foco de un `SimpleField` en un `Form`. Se dispara cuando el usuario sale del field (tab, click en otro field).

Caracteristicas:

- asociable a un `SimpleField` o a un `Form` completo.
- outgoing `InteractionFlow` puede tener cualquier `ViewElement` como destino.
- `ParameterBindingGroup` asociado puede llevar como input el valor del `SimpleField` o todos los valores de los `SimpleField` del `Form`.

Casos tipicos:

- validacion al salir del campo (ej. checking de username availability).
- auto-save al perder foco.

## 4. Drag and drop

Comportamiento que abarca una secuencia de interacciones, modelado por correlacion de dos events: `OnDragStart` y `OnDrop`.

### 4.1 OnDragStart

**OnDragStart** — extension de `ViewElementEvent` que captura el inicio de la interaccion drag.

Caracteristicas:

- asociable a `Details` o `List` ViewComponents (y especializaciones).
- sin outgoing `InteractionFlow`.
- propiedad obligatoria `OnDropEvent` que denota el evento `OnDrop` destino.

### 4.2 OnDrop

**OnDrop** — extension de `ViewElementEvent` que captura la terminacion de drop.

Caracteristicas:

- asociable a `Details` o `List` ViewComponents (y especializaciones).
- debe aparecer como valor de la propiedad `OnDropEvent` del `OnDragStart` source.
- un outgoing `InteractionFlow`, con cualquier `ViewElement` como destino.
- `ParameterBindingGroup` con dos input parameters:
 1. instancia(s) del `ViewComponent` asociado al `OnDragStart`.
 2. instancia(s) del `ViewComponent` asociado al `OnDrop`.

Caso tipico: arrastrar mensajes de la lista al mailbox destino. El drop dispara `MoveTo` `Action` que mueve los mensajes al mailbox seleccionado.

## 5. Tree

**Tree ViewComponent** — extension de `List` que muestra datos jerarquicos.

Componentes:

- `DataBinding` que referencia una clase del domain model (tipo comun de los nodos).
- `RecursiveNestedDataBinding` que referencia una asociacion one-to-many sobre instancias de la clase (la jerarquia).

Modelo de datos: clase + asociacion recursiva. Interaccion basica: seleccion de un nodo a la vez.

Caso tipico: lista seleccionable de nested mailboxes. `SelectEvent` permite elegir un elemento en el tree y mostrar su detalle.

## 6. Table

**Table ViewComponent** — extension de `ViewComponent` que muestra datos tabulares y permite editarlos.

Componentes:

- `DataBinding` que referencia una clase del domain model.
- atributos de la clase mapeados a columnas via `ColumnAttribute` `ViewComponentPart`.

Eventos asociables:

| Evento | Semantica |
| --- | --- |
| `CellUpdate` | Edicion de una celda |
| `RowInsertion` | Insercion de fila |
| `RowDeletion` | Eliminacion de fila |

Mecanica tipica:

- `CellUpdate` → `Action` data update con `ParameterBinding` del valor modificado.
- `RowDeletion` → `Action` que elimina la instancia identificada por `ParameterBinding`.
- `RowInsertion` → `Action` de creacion con valores entrados en la fila.
- por default, el `InteractionFlow` regresa al source element tras la `Action` (puede omitirse del diagrama).

Eventos adicionales tipicos: `Refresh`, `SaveAll` para sincronizacion explicita; parameters compactos para representar contenido de fila completa o tabla completa.

## 7. EditableSelectionField

**EditableSelectionField** — extension de `Field` que denota un input field editable y seleccionable simultaneamente. Mezcla funcionalidad de `SimpleField` y `SelectionField`: el usuario edita el valor o lo elige de una lista de opciones existentes.

Caso tipico: `ProductCreator` form con `Category` `EditableSelectionField`. Permite elegir categoria existente o inventar una nueva. La `Action` `CreateProductAndCategory` distingue ambos casos: si la categoria es nueva, la crea junto con el product. Behavior detallado en diagrama UML separado.

## 8. Caveat sobre estereotipos textuales

Las extensiones de IFML se representan con **stereotypes** sobre el `ViewComponent`. Por conformidad al estandar, se usa textual stereotyping. Esto puede ser cumbersome para `ViewComponent` con nombres largos. Una herramienta puede reemplazar la notacion textual con representacion mas concisa: iconos pequeños, font colors, texturas.

## 9. Tradeoff conceptual: alcance de extensiones desktop

La equivalencia entre **desktop applications** (window-based, java swing, windows forms) y **rich Internet applications** (JavaScript + HTML 5) es imprecisa desde el punto de vista de programacion, pero suficiente para identificar features cross-platform que dan buenos candidatos a extension. Los eventos desktop son tan numerosos que revisarlos exhaustivamente no es factible: el corpus prioriza criterios para extender (`§2`) y ejemplos representativos (`OnFocusLost`, drag/drop) sobre cobertura completa.
