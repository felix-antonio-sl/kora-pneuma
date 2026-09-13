
# ifml

## Proposito

Skill horizontal para **diagnosticar, disenar y aplicar soluciones IFML** durante el desarrollo de aplicaciones interactivas. Provee la capacidad de tomar una descripcion de aplicacion (web, desktop, mobile, multiscreen) y producir un Interaction Flow Diagram tipado, validado contra el estandar OMG, con citas de los patrones aplicables.

La skill es **estructural y horizontal**: trabaja la sintaxis y semantica del lenguaje IFML, no la decision de diseno grafico ni la logica de negocio. El conocimiento de dominio lo aporta el agente o el operador que invoca la skill. Usa la semántica de negocio ya aportada o recuperable en las fuentes autorizadas. Si falta un dato material, pregunta sólo por él y avanza con las partes independientes sin fabricar hechos.

Anclaje canonico: las nueve capas del corpus IFML:

| Capa | URN | Rol en la skill |
|------|-----|-----------------|
| Indice | `urn:fxsl:kb:ifml-corpus-index` | Mapa del corpus |
| Fundamentos | `urn:fxsl:kb:ifml-fundamentos` | MVC, principios, ciclo de desarrollo, ejemplo Bookstore |
| Composicion UI | `urn:fxsl:kb:ifml-view-containers` | ViewContainer, anidamiento, Window, Context, ViewPoint, patrones O-* |
| Contenido y nav | `urn:fxsl:kb:ifml-view-components` | ViewComponent, DataBinding, ParameterBinding, Form, patrones CN/DE/CS |
| Acciones y eventos | `urn:fxsl:kb:ifml-actions-events` | Action, ActionEvent, SystemEvent, patrones CM-* |
| Ext. desktop | `urn:fxsl:kb:ifml-extensiones-desktop` | OnFocusLost, drag/drop, Tree, Table, EditableSelectionField |
| Ext. web | `urn:fxsl:kb:ifml-extensiones-web` | Page, Area, SiteView, WebNavigationFlow, List variants |
| Ext. mobile | `urn:fxsl:kb:ifml-extensiones-mobile` | Context dims, MapView, gestos, multiscreen |
| Patrones | `urn:fxsl:kb:ifml-patrones` | Catalogo cifrado XY-Z (~80 patrones) |

## Cuando Usar

- modelar la interaccion frontend de una aplicacion desde requirements o use cases.
- disenar la jerarquia de ViewContainer y la navegacion entre vistas.
- diagnosticar una UI existente para verificar consistencia estructural antes de implementar cambios.
- elegir un patron IFML aplicable a un problema concreto (master detail, faceted search, multistep wizard, etc.).
- validar que parameter bindings, eventos y flujos respetan las reglas del estandar.
- decidir entre extensiones desktop, web o mobile cuando la plataforma importa.
- modelar adaptacion contextual de la interfaz (multi-rol, multi-device, multi-screen).

## Cuando NO Usar

- disenar **presentacion grafica** (look & feel, layouts pixel-perfect): IFML lo delega; usar herramientas de UX/UI dedicadas.
- modelar **logica de negocio interna** de una accion: IFML referencia, no encapsula. Usar UML sequence/activity, BPMN, BPEL.
- modelar el **domain model** (entidades, atributos, asociaciones): IFML referencia el modelo de contenido pero no lo construye. Usar UML class diagram, ERD, ontologia.
- modelar interaccion entre sistemas no humanos (B2B, microservicios): IFML modela interfaces para usuarios humanos.
- decidir entre arquitecturas backend (PIM/PSM, deployment): ortogonal a IFML.
- consultoria de dominio (medicina, legal, gobierno): la skill no procesa dominio; activar el gate de elicitacion y delegar al agente especializado o al operador.

Si la pregunta es sobre **navegacion entre vistas**, **estructura de pantallas**, **flujo de datos en formularios**, **eventos de UI**, o **patrones de interfaz**: IFML aplica. Si es sobre **estilo visual**, **logica de negocio interna**, o **estructura de datos persistentes**: IFML no aplica directamente.

## Workflow

### Estado inicial: `triaje`

Clasificar la solicitud para decidir el siguiente estado:

| Input del usuario | Siguiente estado |
|-------------------|------------------|
| "modelar la app X con IFML" / "disenar la interaccion de Y" | `encuadrar-aplicacion` |
| "que patron sirve para Z?" / "como hago un wizard / faceted search?" | `seleccionar-patrones` |
| "validar este IFD" / "este modelo cumple IFML?" | `validar-modelo` |
| "que extensiones desktop/web/mobile aplican aqui?" | `aplicar-extensiones` |
| "como modelo el contexto X (rol/device/posicion)?" | `aplicar-extensiones` (rama context) |

Antes de avanzar, dos chequeos:

1. **Alcance estructural.** Verificar que el problema es **estructural de interaccion frontend**. Si es presentación gráfica pura, lógica interna o dominio, usar la capacidad pertinente; conservar IFML sólo para la parte de interacción que sí aporte.

2. **Resolver semántica de negocio/dominio.** La skill es horizontal: posee la sintaxis y semantica de IFML, **no** la semantica de negocio del sistema concreto. Si para modelar hace falta saber QUE hace una `Action` en el dominio, que entidades tiene el domain model, que reglas de negocio condicionan un binding o un flujo, o cualquier decision que dependa del significado del negocio y no del lenguaje IFML: consultar primero el contexto y las fuentes autorizadas; si el dato material sigue faltando, pedir ese mínimo al operador. Nunca fabricar Actions, ParameterBindings, DataBindings ni transiciones de negocio plausibles a partir de supuestos. Es valido continuar con un placeholder explicitamente marcado como pendiente de elicitacion, pero el modelo entregado debe declarar el supuesto y la pregunta abierta. La skill aporta la especialidad de interacción; no convierte al invocador en conocedor del dominio por activarse.

### `encuadrar-aplicacion`: clasificar el espacio de diseno

Determinar caracteristicas que condicionan el modelo:

| Dimension | Pregunta | Lleva a |
|-----------|----------|---------|
| Plataforma | desktop / web / mobile / multiscreen / hibrido | extensiones especificas (`ifml-extensiones-*`) |
| Roles | uno / varios / publicos vs autenticados | `Context`, `UserRole`, `ViewPoint`, `OW-MFE` |
| Adaptacion | estatica / dinamica (device, posicion, network) | `ContextDimension` + `ActivationExpression` |
| Tareas dominantes | navegacion, busqueda, data entry, gestion contenido | familia de patrones aplicable (CN, CS, DE, CM) |

Salida: ficha de encuadre con plataforma elegida, conjunto inicial de roles, dimensiones contextuales relevantes, y familias de patrones probables. Si alguna dimension depende de semantica de negocio que no se conoce, activar el gate de elicitacion antes de fijarla.

### `seleccionar-patrones`: elegir patrones del catalogo

Consultar `urn:fxsl:kb:ifml-patrones` para mapear cada tarea/problema a un patron cifrado:

- problemas de organizacion -> `O*` (`OD-SWA`, `OW-LWSA`, `OM-MSL`, etc.)
- problemas de contenido y navegacion -> `CN-*` (`CN-MD`, `CN-MLMD`, `CN-DEF`, etc.)
- problemas de data entry -> `DE-*` (`DE-FRM`, `DE-WIZ`, `DE-CSF`, etc.)
- problemas de busqueda -> `CS-*` (`CS-SRC`, `CS-MCS`, `CS-FSR`)
- problemas de gestion -> `CM-*` (`CM-OCR`, `CM-ODL`, `CM-AM`, `CM-NOTIF`, etc.)
- problemas de identidad/auth -> `IA-*`
- problemas de sesion -> `SES-*`
- problemas sociales -> `SOC-*`
- problemas geo -> `GEO-*`

Si ningun patron del catalogo calza: declarar el desvio, nombrar la combinacion de constructos base que se va a usar, y dejar la deuda como nota.

### `modelar-composicion`: ViewContainer y anidamiento

Aplicar `urn:fxsl:kb:ifml-view-containers`:

1. Definir `ViewContainer` top-level (uno o varios segun plataforma).
2. Decidir anidamiento conjuntivo (simultaneo) vs XOR (mutually exclusive) por subcontainer.
3. Marcar `Default` el que se muestra por defecto al acceder al padre disyuntivo.
4. Marcar `Landmark` los alcanzables desde todos los hermanos (reduce flechas explicitas).
5. Si requiere ventanas modales/modeless: usar stereotype `Window`/`Modal`/`Modeless`.

### `modelar-contenido`: ViewComponent y bindings

Aplicar `urn:fxsl:kb:ifml-view-components`:

1. Por cada `ViewContainer`, identificar `ViewComponent` (Lists, Details, Forms, MultiChoiceLists).
2. Para cada componente con contenido del domain: especificar `DataBinding` (clase + ConditionalExpression OCL + VisualizationAttributes + OrderBy). La clase del domain y la condicion son semantica de negocio: si no se conocen, activar el gate de elicitacion y no inventarlas.
3. Para componentes con contenido operacional: usar `DynamicBehavior` referenciando UMLBehavior.
4. Identificar dependencias I/O entre componentes: `ParameterBinding` + `ParameterBindingGroup` cuando varios.
5. Decidir si paso de parametros requiere interaccion (`NavigationFlow`) o no (`DataFlow`, flecha discontinua).

### `modelar-eventos-acciones`: Events, Actions, SystemEvents

Aplicar `urn:fxsl:kb:ifml-actions-events`:

1. Por cada `ViewComponent` interactivo, asociar `Event` (`SelectEvent`, `SubmitEvent`, etc.).
2. Cada `Event` debe tener salida: `NavigationFlow` a `ViewContainer`/`ViewComponent`, o flujo a `Action`.
3. Las `Action` se modelan como hexagono con normal/exceptional `ActionEvent`. La logica interna se delega a modelos externos. Que HACE la Action en el dominio es semantica de negocio: nombrarla con lo aportado o verificado en fuentes autorizadas; en su ausencia, placeholder marcado y gate activado.
4. Para notificaciones generadas por sistema/servicios externos: `SystemEvent` + `SystemFlow` + `TriggeringExpression` opcional.
5. Para CRUD del domain: aplicar patrones `CM-*` con sus mecanicas estandar.

### `aplicar-extensiones`: especializaciones por plataforma o contexto

Decidir cuando aplica:

| Necesidad | Extension |
|-----------|-----------|
| events sofisticados de desktop (focus loss, drag/drop, edicion en tabla) | `ifml-extensiones-desktop`: `OnFocusLost`, `OnDragStart`, `OnDrop`, `Tree`, `Table` |
| URLs, RBAC web, links con propiedades hypertext | `ifml-extensiones-web`: `Page`, `Area`, `SiteView`, `WebNavigationFlow` |
| listas avanzadas web (sort dinamico, paging, nested) | `ifml-extensiones-web`: `DynamicSortedList`, `ScrollableList`, `NestedList` |
| sensors, mapas, gestos, multiscreen | `ifml-extensiones-mobile`: `MapView`, `Marker`, `Path`, gestos como event types, multiscreen via `ActivationExpression` |
| adaptacion contextual fuerte (rol, device, network, posicion) | `Context`, `ContextDimension`, `ContextVariable`, `ActivationExpression`, `ViewPoint` |

Regla de parsimonia: usar core IFML cuando alcance. Las extensiones pagan prima cuando la dimension de plataforma o contexto realmente justifica el constructo especializado.

### `validar-modelo`: verificar invariantes

Tres niveles:

1. **Estructurales** (corpus core):
   - **Default y XOR (dos reglas nombradas del metamodelo OMG, ambas duras):**
     `xorMustHaveADefaultParent` — un `ViewContainer` con `isXOR=true` debe tener
     exactamente un hijo con `isDefault=true`; y `defaultMustHaveXorParent` — marcar
     `Default` solo es valido bajo un padre XOR (marcarlo en una familia conjuntiva es
     el error). Caveat de fidelidad: el propio spec OMG IFML v1.0 (formal/2015-02-05,
     §8.3.54) contradice la primera regla en su ejemplo canonico (GMail, Apendice A:
     un XOR sin default «accessed as a consequence of an explicit user's choice») y
     herramientas reales (WebRatio) toleran XOR-sin-default; tratar como error duro si
     se prioriza el estandar formal, como warning si se prioriza la practica del propio
     ejemplo OMG.
   - `Landmark` solo dentro del enclosing comun.
   - todo `Event` interactivo tiene `NavigationFlow` o `Action` saliente.
   - `ParameterBinding` cuando hay dependencia I/O explicita.
   - `DataFlow` con flecha discontinua, `NavigationFlow` con flecha continua.

2. **Semanticas** (corpus core):
   - `Action` es referencia a logica externa, no logica encapsulada.
   - `SystemEvent` no depende de interaccion del usuario.
   - distinguir `ActionEvent` normal vs exceptional cuando aplique.

3. **Catalogo de patrones**:
   - patrones citados con codigo `XY-Z` exacto.
   - extensiones consistentes con la plataforma declarada.

Salida: reporte pass/fail con cita de la regla violada y URN del archivo del corpus.

Si falla -> volver al estado correspondiente con el fix sugerido.
Si pasa -> avanzar a `entregar`.

### `entregar`: paquete final

Salida coherente al agente invocador:

- estructura tipada del modelo: lista de `ViewContainer`, `ViewComponent`, `Event`, `NavigationFlow`, `Action` con sus propiedades.
- patrones aplicados con codigo `XY-Z` y referencia a la URN del corpus.
- reporte de validacion estructural.
- supuestos de dominio declarados y preguntas abiertas de elicitacion pendientes (si las hay).
- (opcional) estructura tipada lista para render visual si el invocador pide diagrama; el render concreto (SVG, interactivo) lo realiza una herramienta externa de render — la skill conserva la responsabilidad del modelo correcto, no del dibujo.

## Reglas Duras

1. **Constructos del estandar**: usar exclusivamente primitivas y extensiones del corpus IFML. Sin invenciones.
2. **Idioma**: nombres de constructos en ingles (ViewContainer, NavigationFlow, etc.); prosa explicativa en espanol.
3. **Eventos con salida**: ningun `Event` interactivo queda colgado. `NavigationFlow`, `DataFlow` o `Action` siempre.
4. **Parameter binding obligatorio cuando el destino depende del origen** para computar contenido.
5. **Anidamiento coherente con realidad operativa**: XOR = mutually exclusive real; conjuntivo = simultaneo real.
6. **Window/Modal/Modeless** solo cuando la semantica de bloqueo de fondo importa.
7. **Action es referencia, no encapsula logica**. Detallar behavior en modelo externo.
8. **Patrones citados con codigo oficial** `XY-Z` o desvio declarado.
9. **DataFlow vs NavigationFlow** segun haya o no interaccion explicita del usuario.
10. **Extensiones cuando justifiquen**, no como decoracion. Core IFML cuando alcance.
11. **Context + ViewPoint solo si la composicion cambia en runtime**, sino `ActivationExpression` sobre elementos individuales.
12. **No invadir dominio**: la skill modela estructura de interaccion, no semantica de negocio ni look & feel.
13. **Gate de elicitacion (regla dura)**: cuando el modelado requiere semantica de negocio/dominio que la skill (horizontal) no posee — que hace una Action, que entidades pueblan el domain model, que regla condiciona un binding o flujo — resolverla desde lo ya aportado o desde fuentes autorizadas y preguntar sólo por el dato material que siga faltando. Prohibido fabricar Actions, bindings, DataBindings o transiciones de negocio a partir de supuestos. Placeholder marcado y pregunta abierta son aceptables; supuesto no declarado, no. Precision: pedir al operador la LISTA de clases del domain model ya dadas (para tipar un binding) no es fabricar — es input estructural que IFML consume del domain modeling; el gate dispara ante fabricar el SIGNIFICADO de negocio (que hace una Action, que regla condiciona un flujo), no ante necesitar el nombre de una clase que el operador puede entregar de inmediato.

## Composicion con otras skills

### Con `modelamiento-opm`

OPM e IFML son complementarios:

- OPM modela el **sistema** (objetos, procesos, transformaciones, funcion). Capa conceptual del dominio.
- IFML modela la **interaccion del usuario con el sistema** (vistas, navegacion, eventos). Capa de interfaz.

Composicion tipica:

1. `modelamiento-opm` produce el OPM model del sistema; identifica los procesos visibles al usuario.
2. IFML modela el front-end que expone esos procesos como `Action` triggered by user events.
3. `Action` IFML referencia al proceso OPM correspondiente como su **behavior externo** (la business logic que IFML trata como black-box), no como `DynamicBehavior` — `DynamicBehavior` es content-source de un `ViewComponent` (otro eje del modelo: publicacion de contenido), no el behavior disparado por una `Action`.

Cuando el OPM model ya aporta la semantica de negocio de un proceso, el gate de elicitacion se satisface con esa fuente en vez de preguntar al operador.

## Recursos

### Referencias

Las referencias se delegan al corpus directo: las 9 URNs `urn:fxsl:kb:ifml-*` declaradas en `conocimiento`. No hay archivos de referencias internas en este momento. Si futuras iteraciones requieren material destilado mas alla del corpus (ej. arboles de decision para seleccion de patrones), se agregan en `referencias/` como resumenes operativos curados — nunca como SSOT alternativo al corpus.

### Recursos

`recursos/` reservado para ejemplos didacticos minimos del estandar (ej. modelo IFML del Bookstore presente en `ifml-fundamentos`). Los ejemplos viven en el corpus mismo; no se duplican aqui.
