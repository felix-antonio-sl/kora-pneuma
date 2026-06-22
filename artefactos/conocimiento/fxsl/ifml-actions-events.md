---
urn: urn:fxsl:kb:ifml-actions-events
nombre: ifml-actions-events
version: 1.0.0
estado: publicado
descripcion: Corpus IFML — Action (black box), ActionEvent, SystemEvent/SystemFlow/TriggeringExpression y los siete patrones de content management CM-* (creacion, eliminacion, cascada, modificacion, asociacion, notificacion).
fuente: Ifml-In-A-Nutshell cap. 6 (Modeling business actions) — sha256:a7f6aefe270fe01e00d57437c3c4fbcf1fc0bfc45728a99174a2e45436687e37
familia: bok
tags: [ifml, action, actionevent, systemevent, content-management, omg]
lang: es
cita: [urn:fxsl:kb:ifml-corpus-index, urn:fxsl:kb:ifml-view-components, urn:fxsl:kb:ifml-patrones]
---

# IFML — Acciones y eventos

## Resumen

`Action` modela referencias a logica de negocio disparadas por eventos en la interfaz; sus terminaciones se expresan como `ActionEvent` (normal o exceptional). `SystemEvent` modela ocurrencias generadas por el sistema o servicios externos que afectan la interfaz. IFML no especifica el funcionamiento interno de las acciones (las trata como black boxes); su objetivo es expresar la interaccion entre interfaz y logica de negocio. Cubre los patrones de content management `CM-*` (Object Creation/Deletion/Modification, Cascade Deletion, Association Management, Notification).

## 1. Filosofia de diseño

IFML no reemplaza los lenguajes de behavior specification que describen aspectos algoritmicos. Las business actions son **black boxes** con la informacion minima necesaria para expresar:

- que un evento dispara una accion.
- la dependencia I/O entre interfaz y logica de negocio.
- que la interfaz puede recibir y responder eventos generados por el sistema o servicios externos.
- la dependencia I/O entre la informacion del system event y los elementos afectados.

Para refinar el comportamiento interno, una `Action` IFML puede referenciar un behavior en un modelo externo (UML sequence diagram, activity diagram, BPMN, BPEL).

## 2. Action

**Action** — referencia a logica de negocio disparada por un `Event`.

Notacion: hexagono con nombre.

Ubicacion: server-side o client-side; el modelo PIM no incorpora architectural assumptions, pero el tier de ejecucion puede expresarse como stereotype cuando se requiera.

### 2.1 Patron elementario de triggering

```
Source ViewComponent --(Event)--> InteractionFlow --(parameter binding)--> Action
 |
 v (outgoing flow,
 evento de terminacion)
 Target ViewComponent
```

Componentes:

- `ViewContainer` y `ViewComponent` fuente con un `Event` conectado a la `Action` via `InteractionFlow`.
- `Action` conectada al `ViewComponent` destino por un outgoing flow tipicamente etiquetado por la terminacion normal.
- `ParameterBinding` entre fuente-`Action` y `Action`-destino expresa la dependencia I/O.

Ejemplo conceptual:

- fuente: `Form` para entrar flight request.
- accion: flight brokering business component que toma form data, consulta operadores y devuelve mejores ofertas.
- destino: `List` que muestra las opciones recuperadas.

## 3. ActionEvent

**ActionEvent** — `Event` producido por una `Action` para señalizar terminacion normal o excepcional.

Una accion puede tener multiples `ActionEvent` correspondientes a outcomes alternativos:

| Caso | Modelado |
| --- | --- |
| Normal termination | `ActionEvent` con `InteractionFlow` al destino exitoso |
| Exceptional termination | `ActionEvent` distinto con `InteractionFlow` al destino de error |

Ejemplo conceptual de signup:

- `Form` de signup → `Action` de validacion + token generation.
- Normal: `Details` con token + service terms.
- Exceptional: `Details` con razones del fallo.

### 3.1 Shortcuts de notacion

Cuando no hay outgoing `InteractionFlow` ni `ActionEvent` asociado a la `Action`:

- el destino implicito es el menor `ViewContainer` que comprende el `ViewElement` fuente del que se activo la accion.

Ejemplos en patrones de archivado y reporte (`Archive`, `Report`): la outgoing flow se omite porque el contenedor de la accion permanece visible despues de ejecutarse.

## 4. SystemEvent y SystemFlow

**SystemEvent** — `Event` producido por el sistema que dispara un computo reflejado en la UI. Ejemplos:

- time events (disparados al elapsar un frame de tiempo).
- system alerts (perdida de conexion a database).
- notificaciones de mensaje recibido.

**SystemFlow** — `InteractionFlow` que conecta un `SystemEvent` con el `ViewElement` afectado.

### 4.1 TriggeringExpression

**TriggeringExpression** — expresion que determina cuando o bajo que condiciones un `SystemEvent` debe dispararse.

La causa de un `SystemEvent` puede dejarse no especificada (sistema dispara el evento de manera no determinista en el modelo) o ligarse a una condicion explicita.

## 5. Patrones de gestion de contenido (CM-*) — alcance

Patrones platform-independent que describen la interaccion interfaz-logica para crear, eliminar y modificar instancias del domain model. Historicamente prefijados con `A` (action); en el catalogo final del estandar se renombran a `CM` (content management). El nucleo comun:

- `Action` con input parameters para identificar el objeto y proveer datos.
- output parameters que caracterizan el efecto del update.
- la interfaz suministra el input y visualiza el output como confirmacion.

Las siete subsecciones siguientes (`## 6` a `## 12`) cubren los patrones individuales del set CM.

## 6. CM-OCR: Object Creation

Caracterizacion de la `Action`:

- referencia al dynamic behavior (constructor de clase o factory method).
- input parameters para inicializar atributos del objeto a crear.

Mecanica:

- input tipicamente provisto por `ParameterBindingGroup` asociado al `NavigationFlow` saliente del `Form`.
- atributos sin valor asociado quedan en `null`.
- excepcion: el OID. Si no se suministra, la `Action` genera un nuevo unique value.
- output: el objeto recien creado (OID + valores de atributos). Definido solo en terminacion normal; asociable como `ParameterBindingGroup` al `InteractionFlow` correspondiente.
- shortcut: si no se especifica `ParameterBindingGroup` explicitamente, el default output asociado al normal termination event es la OID del objeto recien creado.

## 7. CM-OACR: Object and Association Creation

Variante de `CM-OCR` que crea un objeto y setea sus asociaciones a otros objetos.

Adicion al `Form`: `SelectionField` correspondiente a la asociacion (preloadeado con todas las instancias del target class).

`NavigationFlow` del `SubmitEvent` lleva `ParameterBinding` adicional para el identifier de la categoria seleccionada, pasado a la `Action`. La `Action` puede:

- referenciar un constructor que setea la categoria del producto.
- referenciar un behavioral diagram (sequence/activity) con todos los pasos de creacion + conexion.

## 8. CM-ODL: Object Deletion

Caracterizacion de la `Action`:

- referencia al dynamic behavior (delete operation del database).
- input parameters para identificar el objeto a eliminar.

Mecanica:

- input via `ParameterBinding` (tipicamente OIDs; tambien atributos no-key cuya logica de retrieval queda encapsulada en la `Action`).
- en runtime el usuario elige un objeto en `Details`, en un item de `List`, o un set de un `MultiChoiceList`.
- `NavigationFlow` saliente del `ViewComponent` con `ParameterBindingGroup` apuntando a la `Action`.

Terminaciones:

| Caso | Output |
| --- | --- |
| Normal | Sin output (todos eliminados) |
| Exceptional | Output parameter con OIDs de objetos no eliminados, util para mostrar lista de fallos + mensaje de error |

Variante multichoice: `MultiChoiceList` con `Delete` event cuyo default `ParameterBinding` lleva el set de OIDs seleccionados; opcionalmente displayed en un `SelectedProducts` `List` con `Confirm` event antes de invocar la `Action`.

## 9. CM-CODL: Cascaded Deletion

Elimina un objeto y todos los relacionados via una o varias asociaciones. Usado para propagar eliminacion a objetos dependientes (asociacion con cardinalidad minima 1, no pueden existir sin el objeto referenciado).

Implementacion:

- secuencia de dos o mas delete operations: una para el objeto principal, otras para los relacionados.
- estructura interna no especificada en IFML; descrita por behavioral diagram (UML sequence) o por mecanismo nativo del data store (`ON DELETE CASCADE` SQL).

Ejemplo: eliminar mensaje + attachments. `Message` `Details` con evento que dispara `CascadeDelete` `Action`. Normal termination redirige al `MessageList` (no al `Message`, que ya no existe), default subcontainer del enclosing `MessageDetails`.

Esta es ilustracion de la interaccion fina entre business logic y interface design: el modelo IFML expresa la consecuencia semantica del action sobre la composicion visible.

## 10. CM-OM: Object Modification

Caracterizacion de la `Action`:

- referencia al dynamic behavior (typically setter method).
- input parameters para identificar los objetos a modificar y suministrar nuevos valores.

Cuando el usuario elige multiples objetos, el mismo update aplica a todos.

Inputs requeridos:

- nuevos valores de atributos: `ParameterBindingGroup` desde el `Form`.
- objetos a modificar: `ParameterBindingGroup` con OID o set de OIDs.
- alternativa: la `Action` retrieve los objetos a partir de criterios logicos provistos como parameters de un `InteractionFlow` entrante (la logica de retrieval queda encapsulada).

Terminaciones:

| Caso | Output |
| --- | --- |
| Normal | Default parameter con set de OIDs modificados |
| Exceptional | Default parameter con set de OIDs no modificados |

Patron tipico (`ProductEditor`):

- `Details` con OID del producto a modificar (input via `DataFlow` a la `Action`).
- `Form` con valores nuevos.
- `SubmitEvent` dispara la accion con `ParameterBindingGroup` que asocia campos del `Form` con input parameters de la `Action`.
- normal: `UpdatedProduct` `ViewContainer` con valores nuevos.
- exceptional: vuelve al `ProductEditor` con valores antiguos.

Caveat: clases con muchos atributos requieren repetir atributos como form fields y como parameter bindings; herramientas pueden auto-generar el patron via wizard insertando todos los atributos automaticamente.

## 11. CM-AM: Association Management

Mantencion de instancias de associations especificadas en el domain model. Crea/reemplaza/elimina instancias de una asociacion conectando o desconectando objetos de las clases source y target.

Caracterizacion de la `Action`:

- referencia al dynamic behavior (setter del atributo que implementa la asociacion en uno o ambos sides).
- input parameters para localizar objetos de la source class y de la target class.

Mecanica:

- la `Action` se dispara con `NavigationFlow` que lleva pares de objetos source-target via `ParameterBindingGroup`.
- output: pares de OIDs source-target para los cuales se gestiono la asociacion; usable en `ParameterBindingGroup` de los normal/exceptional termination events.
- normal termination: todas las associations gestionadas correctamente.
- exceptional termination: al menos una falla.

Ejemplo: actualizar la categoria de un producto (asociacion one-to-many).

- `Product` `Details` muestra el producto actual.
- `CurrentCategory` `Details` muestra su categoria via `DataFlow` con `ParameterBindingGroup` que lleva la primary key del producto.
- `Categories` `List` permite elegir categoria nueva.
- `Assign` `SubmitEvent` dispara `Action` que actualiza la asociacion.
- normal: redespliega `ProductCategories` `ViewContainer` con la categoria actualizada.
- exceptional: alert window antes de retornar al original.

## 12. CM-NOTIF: Notification

Modela la actualizacion asincrona de la interfaz por un evento generado por el sistema.

Estructura:

- `SystemEvent` que dispara display de un `MessageNotification` `ViewComponent` (u otro afectado).
- la produccion del `SystemEvent` puede dejarse indeterminada o ligarse a la terminacion de una `Action` para denotar que la notificacion esta correlacionada con esa terminacion.

Ejemplo: en aplicacion de email, acciones sobre messages (send, delete, move-to) ejecutadas en server-side terminan emitiendo asynchronous notification capturada por la UI como `SystemEvent`.

## 13. Tier de ejecucion como concern arquitectural

El modelo PIM debe permanecer neutro respecto a donde se ejecuta una `Action`. Pero PIM neutral no implica que todas las acciones esten en el mismo tier o que solo modele server-side logic.

Ejemplo: `MessageWriter` ViewComponent con `Body` SimpleField puede embeber un microapplication client-side (rich text editor, spellchecker mixto client-server). El embebido se modela reemplazando el `SimpleField` con un `ViewComponentPart` mas complejo (`RichTextEditor`).

El tier de ejecucion de una `Action` puede expresarse como **stereotype** en el diagrama (ej. `«client»`, `«server»`) cuando la decision arquitectural es relevante para el modelo.
