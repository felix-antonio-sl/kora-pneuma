---
urn: urn:fxsl:kb:ifml-fundamentos
nombre: ifml-fundamentos
version: 1.0.0
estado: publicado
descripcion: "Fundamentos de IFML (Interaction Flow Modeling Language, OMG/MDA): aspectos del front-end que cubre, artefactos del estandar, principios de diseno, rol en MVC, constructos centrales, anidamiento conjuntivo/disyuntivo, ejemplo Bookstore y rol en el ciclo de desarrollo."
fuente: "Migrado de la bestia (~/kora) artifacts/knowledge/fxsl/ifml/ifml-fundamentos.md (sha256:bfaf82278134423808aa2e3ec9937f0936e5b758255464baceabf27bf4431258); cuerpo IFML ya koraficado, preservado integro (FS=100%, sin recomprimir). Fuente original: Ifml-In-A-Nutshell, capitulos 1-2 (Introduction, IFML in a Nutshell), manual del estandar IFML/OMG."
autor: FS
creado: 2026-05-07
lang: es
tags: [ifml, omg, mda, mvc, modeling, fundamentos]
familia: bok
cita: [urn:fxsl:kb:ifml-corpus-index, urn:fxsl:kb:ifml-view-containers]
---

# IFML — Fundamentos

## Resumen

**IFML (Interaction Flow Modeling Language)** es un estandar OMG basado en MDA para especificar el front-end de aplicaciones interactivas independientemente de los detalles de su realizacion tecnologica. Modela la View del patron MVC (composicion, contenido, eventos, transiciones, parameter bindings) en un unico tipo de diagrama llamado **Interaction Flow Diagram**, conectandola con Model y Controller via referencias externas.

## 1. Aspectos del front-end que IFML cubre

| Aspecto | Pregunta de modelado |
| --- | --- |
| Composicion de la vista | Que unidades de visualizacion componen la interfaz, como se organizan, cuales se muestran simultaneamente o en exclusion mutua |
| Contenido de la vista | Que elementos se publican al usuario, que input se acepta del usuario y se entrega a la aplicacion |
| Comandos | Que eventos de interaccion soporta la interfaz |
| Acciones | Que componentes de negocio se disparan al ocurrir un evento |
| Efectos de la interaccion | Como cambia el estado de la interfaz tras un evento o tras la ejecucion de una accion |
| Parameter binding | Que datos se comunican entre elementos de la interfaz y las acciones disparadas |

## 2. Artefactos tecnicos del estandar OMG

IFML especifica cinco artefactos:

- **Metamodelo IFML** — estructura y semantica de los constructos via OMG MOF (Meta Object Facility).
- **Perfil UML para IFML** — sintaxis basada en componentes UML, clases y estructuras jerarquicas.
- **Sintaxis visual** — representacion concreta basada en un unico diagrama. Compacta lo que en UML se expresa con multiples diagramas (clase, state machine, composite structure).
- **Sintaxis textual** — alternativa textual equivalente a la visual.
- **IFML XMI** — formato de intercambio para portabilidad entre herramientas.

El corpus KORA se ancla en la **sintaxis visual** por proximidad a UML y compactacion.

## 3. Principios de diseño de IFML

Cinco reglas doradas explicitas del estandar:

| Principio | Compromiso |
| --- | --- |
| Concision | Numero minimo de tipos de diagrama y conceptos para expresar la interfaz; un solo diagrama compacto |
| Inferencia desde el contexto | Reglas automaticas aplican patrones por defecto cuando algo se deduce del modelo (ej. parameter passing) |
| Extensibilidad | Conjunto pequeño de conceptos core extensibles para nuevos requirements, modalidades y plataformas |
| Implementabilidad | Modelos PIM con executability en mente; transformaciones a codigo y generadores soportados |
| No-todo-en-el-modelo | IFML omite presentacion grafica (`adversarial to abstraction`) y delega a otros modelos lo no propio de la interfaz (logica de accion, modelo de datos) |

Lo que IFML **delega** y no modela:

- presentacion grafica (graphic design, pixel-perfect)
- logica interna de las `Action` (delega a UML class methods, SoaML, sequence/activity diagrams)
- modelo de contenido (delega a UML class diagram, CWM, ER, ontologia)

## 4. IFML en el patron MVC

IFML describe principalmente la **View**. Los hooks con Controller y Model:

- **Controller** — IFML representa los efectos de la interaccion. Define eventos producidos en la View y el curso de accion del Controller (disparar un componente de negocio, actualizar la View).
- **Model** — IFML describe el data binding entre elementos de la interfaz y los objetos que encarnan el estado de la aplicacion, mas las acciones disparadas por la interaccion.

## 5. Constructos centrales

Definiciones operativas del nucleo:

- **ViewContainer** — elemento de la interfaz que agrega otros view containers o view components que muestran contenido. Puede representar artefacto fisico (window, web page) o agregacion logica (seccion de portal con paginas homogeneas).
- **ViewComponent** — elemento que muestra contenido (lista de objetos) o acepta input (formulario). Puede tener estructura interna de `ViewComponentPart`.
- **Event** — ocurrencia que afecta el estado de la interfaz. Producido por interaccion del usuario (`ViewElementEvent`), por una accion al terminar (`ActionEvent`), o por el sistema (`SystemEvent`).
- **NavigationFlow** — arco dirigido que conecta un evento con su `ViewContainer` o `ViewComponent` destino. Expresa cambio de estado de la interfaz.
- **InteractionFlow** — generalizacion que cubre `NavigationFlow` (con interaccion del usuario) y `DataFlow` (sin interaccion, solo paso de parametros).
- **ParameterBinding** — dependencia input-output entre elementos. Cuando involucra varios parametros simultaneos: `ParameterBindingGroup`.
- **Action** — referencia a logica de negocio disparada por un evento. Representada como hexagono.

Renderizacion: los eventos IFML se mapean a *interactors* en la aplicacion implementada. La forma concreta (link HTML, swipe gesture, click event) depende de la transformacion PIM-PSM.

## 6. Anidamiento conjuntivo y disyuntivo

`ViewContainer` puede anidar otros con dos formas:

- **Conjuntiva** (default) — los hijos se muestran simultaneamente.
- **Disyuntiva** (XOR) — el despliegue de uno reemplaza al otro. Notacion: etiqueta `XOR` antes del nombre.

Si la familia es disyuntiva, uno puede marcarse como **default**: el que se muestra al acceder al padre. Notacion: `[D]` en la esquina superior izquierda.

## 7. Ejemplo completo: Bookstore

Aplicacion online donde el usuario navega productos (libros, musica, software) y los agrega al carrito. Caso de uso `Browse books`:

- Home page con lista de categorias.
- Click en una categoria abre pagina con summary de items.
- Click en `See more` abre pagina con detalle del item.

Caso de uso `Manage cart`:

- En la vista de detalle, boton `Add to cart` abre modal con cantidad.
- Submit de la cantidad genera pop-up de confirmacion.

Modelo IFML resultante:

- 5 `ViewContainer` con stereotypes: `H` (Home), `L` (Landmark), `Modal`, `Modeless`.
- `ViewComponent` por contenedor: `CategoryList`, `ProductList`, `ProductDetails`, formulario `Quantity`, confirmacion.
- `SelectCategory` event en `CategoryList` → `NavigationFlow` con `ParameterBinding` (`SelectedCategory` output → `Category` input) hacia `ProductOfCategory`.
- Patron equivalente para `SelectProduct` → `ProductDetails`.
- `Add to cart` event dispara `Action` con dos inputs: `Quantity` (de la Form, asociado a `NavigationFlow`) y `DisplayedProduct` (de `ProductDetails`, asociado a `DataFlow` por no requerir interaccion del usuario).
- Action completada → `ConfirmationWindow` abierta.

Distincion clave: **NavigationFlow vs DataFlow**:

| Tipo | Origen | Fuente del paso de parametros |
| --- | --- | --- |
| `NavigationFlow` | submit/select event del usuario | interaccion explicita |
| `DataFlow` | `ViewComponent` directamente | sin intervencion del usuario, solo dependencia I/O |

`DataFlow` se denota con flecha discontinua para distinguirlo de `NavigationFlow`.

## 8. Rol de IFML en el ciclo de desarrollo

Pipeline tipico iterativo:

1. **Requirements specification** — captura roles, use cases, data dictionary, workflow.
2. **Domain modeling** — entidades, atributos, asociaciones (UML class diagram, ER, ontologia).
3. **Front-end modeling** — IFML mapea use cases a `ViewContainer` + `ViewComponent` + eventos + acciones.
4. **Business logic modeling** — UML static/dynamic, BPMN, BPEL para acciones.
5. **Architecture design** — UML deployment, hardware, red, software components.
6. **Implementation** — data, business logic, interfaz; mapeo a plataformas.
7. **Testing & evaluation** — funcional, usabilidad, performance.
8. **Deployment** — instalacion en arquitectura.
9. **Maintenance & evolution** — cambios al sistema en produccion.

Las fases 2-4 son interdependientes y suelen ejecutarse iterativamente; el orden lineal es ilustrativo.

Implicaciones cruzadas de IFML:

| Fase | Implicacion del modelo IFML |
| --- | --- |
| Domain modeling | Entidades para categorizacion y retrieval surgen al diseñar la interfaz |
| Business logic | Las `Action` referenciadas en IFML disciplinan el diseño de operaciones |
| Implementation | Code generation desde IFML produce prototipos o codigo funcional |
| Testing | Model checking sobre IFML detecta inconsistencias antes de codigo (estados inalcanzables, falta de patrones uniformes) |
| Maintenance | Cambios al diseño se propagan via model-to-code transformations |

## 9. Requirements no funcionales relevantes a IFML

Cuando la aplicacion se dirige al publico general, los requirements de **look & feel** y **usabilidad** asumen prominencia entre los no funcionales. Practicas user-centered con mock-ups realistas validan conceptos de interfaz tempranamente y sirven como base para especificaciones tecnicas posteriores en la fase de front-end modeling.
