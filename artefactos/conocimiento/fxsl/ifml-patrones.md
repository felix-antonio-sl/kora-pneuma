---
urn: urn:fxsl:kb:ifml-patrones
nombre: ifml-patrones
version: 1.0.0
estado: publicado
descripcion: "Catalogo cifrado de los patrones de diseno IFML del estandar OMG, organizados en nueve familias (organizacion, navegacion, data entry, busqueda, gestion de contenido, identidad/autorizacion, sesion, social, geo) con su convencion de codigo XY-Z."
fuente: "Migrado de la bestia (~/kora @ aa2e2f14) artifacts/knowledge/fxsl/ifml/ifml-patrones.md (sha256:e200306cb77362a6fbe6db49305edb0ba1edd263347f897f2ec007321701c544) el 2026-06-22; cuerpo preservado integro (solo se aplano el frontmatter anidado). Fuente original: Ifml-In-A-Nutshell (Brambilla & Fraternali), capitulo final 'List of IFML design patterns'."
autor: FS
creado: 2026-05-07
lang: es
familia: bok
tags: [ifml, patrones, catalogo, omg, design-patterns]
cita: [urn:fxsl:kb:ifml-corpus-index, urn:fxsl:kb:ifml-view-containers, urn:fxsl:kb:ifml-view-components, urn:fxsl:kb:ifml-actions-events, urn:fxsl:kb:ifml-extensiones-web]
---
# IFML — Catalogo de patrones

## Resumen

Catalogo cifrado de los patrones IFML del estandar. Cada patron se identifica con codigo `XY-Z` donde X es la categoria, Y la plataforma de origen y Z el mnemonico especifico. El catalogo organiza los patrones en nueve familias: organizacion de interfaz, contenido y navegacion, data entry, busqueda, gestion de contenido, identificacion y autorizacion, manejo de sesion, funciones sociales y geo. La columna `urn` referencia el archivo del corpus que cubre cada patron en detalle.

## Convencion de codigo

| Componente | Significado |
| --- | --- |
| `X` | Categoria del patron (`O`, `CN`, `DE`, `CS`, `CM`, `IA`, `SES`, `SOC`, `GEO`) |
| `Y` | Plataforma de origen o uso predominante (`D` desktop, `W` web, `M` mobile). Omitido si el patron es cross-platform |
| `Z` | Mnemonico especifico del patron |

Ejemplo: `OD-SWA` = Organization, Desktop, Simple Work Area.

## Patrones de organizacion de interfaz (O*)

Categoria `O` (interface organization). Cubiertos en `urn:fxsl:kb:ifml-view-containers` y `urn:fxsl:kb:ifml-extensiones-web`.

| Codigo | Titulo | Descripcion |
| --- | --- | --- |
| `OD-SWA` | Simple work area | Distingue un work area donde se realizan las tareas principales junto con uno o varios service areas |
| `OD-MWA` | Multiview work area | Extension de `OD-SWA` para multiples vistas alternativas del item en el work area |
| `OD-CWA` | Composite work area | Divide el work area en subregions devotas a perspectivas distintas del item, presentadas simultaneamente |
| `OD-MCWA` | Multiview composite work area | Combina la descomposicion del work area en perspectivas alternativas con vistas parciales simultaneas |
| `OW-MFE` | Multiple front ends on the same domain model | Provee interfaces distintas para distintos user roles sobre la misma informacion |
| `OW-LWSA` | Large web sites organized into areas | Aplicaciones con estructura jerarquica donde las pages se agrupan en secciones por sujeto homogeneo |
| `OM-MSL` | Mobile screen layout | Mapea la interfaz a un grid top-level con tres regiones: header, content area, footer |

## Patrones de contenido y navegacion (CN-*)

Categoria `CN` (content and navigation). Cubiertos en `urn:fxsl:kb:ifml-view-components`.

| Codigo | Titulo | Descripcion |
| --- | --- | --- |
| `CN-MD` y `CN-MMD` | Master detail y Master multidetail | Presentan items y la seleccion permite acceder al detalle de una instancia a la vez |
| `CN-MLMD` | Multilevel master detail | Tambien llamado cascaded index; secuencia de lists sobre clases distintas, cada list cambia el foco de un objeto seleccionado al set de objetos relacionados via association role; termina en un objeto unico |
| `CN-DEF` | Default selection | Simula una eleccion del usuario al primer acceso a una list, seleccionando una instancia por defecto |
| `CN-SOT` | Single object toolbar | Toolbar content-dependent que soporta comandos sobre un objeto |
| `CN-MOT` | Multiple object toolbar | Toolbar content-dependent con comandos aplicables a multiples objetos |
| `CN-DT` | Dynamic toolbar | Toolbar con comandos que pueden variar en runtime segun el estado de la interaccion |
| `CN-MSC` | Multistep commands | Comandos que involucran multiples interaction steps |
| `CN-CII` | Commands with inline input | Colapsa varios pasos de un command en la toolbar |
| `CN-CIM&B` | Content-independent navigation bar and menu | Agrupa comandos que no actuan sobre objetos especificos pero acortan la navegacion o ayudan a volver atras |
| `CN-UP` | Up navigation | Refiere a una estructura jerarquica asociada a la interfaz; lleva al elemento superior en la jerarquia visual |
| `CN-BACK` | Back navigation | Refiere a la cronologia de la interaccion; lleva al ultimo `ViewElement` visitado |
| `CN-BREAD` | Breadcrumbs | Aid de navegacion que muestra la ubicacion del usuario en la interfaz |
| `CN-PG` | Paging | Muestra un bloque de objetos a la vez y permite scroll rapido por la coleccion |
| `CN-PR` | Collection preview | Usado con `CN-PG`; provee preview de la posicion del objeto en la secuencia y de lo anterior y siguiente |
| `CN-ALPHA` | Alphabetical filter | Filtro alfabetico para particionar la coleccion en chunks |

## Patrones de data entry (DE-*)

Categoria `DE` (data entry). Cubiertos en `urn:fxsl:kb:ifml-view-components`.

| Codigo | Titulo | Descripcion |
| --- | --- | --- |
| `DE-FRM` | Multifield forms | Form para enviar informacion via varios fields |
| `DE-PLDF` | Preloaded field | Variante de `DE-FRM` con fields preloadeados con valor existente |
| `DE-PASF` | Pre-assigned selection field | Form con valor de selection field preseleccionado |
| `DE-DLKP` | Data lookup | Data entry que involucra lookup de informacion para llenar fields |
| `DE-CSF` | Cascade selection fields | Data entry con selecciones que tienen dependencia entre si |
| `DE-WIZ` | Wizard | Particion de data entry en pasos logicos secuenciales |
| `DE-TDFP` | Type-dependent field properties | Provee facilities de data entry para fields de tipos especificos |
| `DE-RTE` | Rich text editing | Field de texto enriquecido como microaplicacion con comandos aplicables al texto |
| `DE-AUTO` | Input auto-completion | Sugerencias automaticas para completar input segun lo ya tipeado |
| `DE-DYN` | Dynamic selection fields | La aplicacion requiere data con dependencias |
| `DE-INPL` | In-place editing | Permite editar contenido sin abandonar la vista actual hacia un data entry form |
| `DE-VAL` | User input validation | Verifica correccion del input contra reglas de validacion y retorna mensajes de notificacion |

## Patrones de busqueda de contenido (CS-*)

Categoria `CS` (content search). Cubiertos en `urn:fxsl:kb:ifml-view-components`.

| Codigo | Titulo | Descripcion |
| --- | --- | --- |
| `CS-SRC` | Basic search | Busqueda por keyword sobre coleccion de items |
| `CS-MCS` | Multicriteria search | Criterio compuesto de busqueda sobre coleccion de items |
| `CS-FSR` | Faceted search | Refinamiento progresivo de resultados sobre datos multidimensionales restringiendo por valores de propiedades |
| `CS-RSRC` | Restricted search | Restringe el foco de busqueda a subcollections especificas en colecciones grandes |
| `CS-SRCS` | Search suggestions | Explota auto-completion logueando keywords previos; los matching se muestran sorted por frecuencia |
| `GEO-LAS` | Location-aware search | Busqueda de items relacionados y cercanos a la posicion actual del usuario |

## Patrones de gestion de contenido (CM-*)

Categoria `CM` (content management). Cubiertos en `urn:fxsl:kb:ifml-actions-events`.

| Codigo | Titulo | Descripcion |
| --- | --- | --- |
| `CM-OCR` | Object creation | Habilita creacion de un objeto nuevo en data storage |
| `CM-OACR` | Object and association creation | Crea un objeto nuevo y setea sus asociaciones a otros objetos |
| `CM-ODL` | Object deletion | Elimina uno o mas objetos de una clase dada |
| `CM-CODL` | Cascaded deletion | Elimina un objeto y todos los asociados a el via una o mas asociaciones |
| `CM-OM` | Object modification | Actualiza uno o mas objetos de una clase dada |
| `CM-AM` | Association management | Crea, reemplaza o elimina instancias de una asociacion conectando o desconectando objetos source y target |
| `CM-NOTIF` | Notification | La interfaz se actualiza tipicamente asincronamente por la ocurrencia de un evento generado por el sistema |
| `CM-CBCM` | Class-based content management | Cubre creacion, modificacion y eliminacion de objeto con sus association instances |
| `CM-PBCM` | Page-based content management | Soporta blogs y CMS basados en pages; permite gestion de pages completas |

## Patrones de identificacion y autorizacion (IA-*)

Categoria `IA` (identity and authorization). Algunos referenciados en la seccion de `Context`/`UserRole` (`urn:fxsl:kb:ifml-view-containers`).

| Codigo | Titulo | Descripcion |
| --- | --- | --- |
| `IA-LOGIN` | Login | Reconoce y verifica la validez de la identidad provista por el usuario |
| `IA-LOGOUT` | Logout | Limpia la authenticated identity preservada en el navigation context bajo request explicito |
| `IA-CEX` | Context expiration notification | El sistema limpia la authenticated identity por seguridad o timeout |
| `IA-SPLOG` | Login to a specific ViewContainer | Verifica identidad y habilita acceso a una parte especifica de la interfaz |
| `IA-ROLE` | User role display and switching | Muestra el rol del usuario y permite cambiarlo |
| `IA-RBP` y `IA-NRBP` | (Negative) role-based permissions for view elements | Implementa permisos de acceso (posiblemente negativos) a nivel de view, dependientes del rol |
| `IA-OBP` | Object-based permissions | Control de acceso expresado sobre objetos de contenido y associations de personalization en el content model |
| `IA-PRO` | User profile display and management | Muestra y permite editar informacion application-dependent asociada a la identidad del usuario authenticado |
| `IA-IPSI` | In-place sign-in | Cuando el usuario intenta disparar una accion, se le advierte la necesidad de sign-in y se enruta al login form |

## Patrones de manejo de sesion (SES-*)

Categoria `SES` (session management).

| Codigo | Titulo | Descripcion |
| --- | --- | --- |
| `SES-CR` | Creating session data from persistent data | Almacena informacion en la navigation session collectandola desde un persistent data source |
| `SES-PER` | Persisting session data | Crea persistent data desde data de la user navigation session |
| `SES-EXC` | Session data expiration catching | Maneja la notificacion asincrona de expiry de session causando refresh automatico del contenido |

## Patrones de funciones sociales (SOC-*)

Categoria `SOC` (social functions).

| Codigo | Titulo | Descripcion |
| --- | --- | --- |
| `SOC-AW` | Activity wall | Loguea la actividad social tipica de una plataforma social |
| `SOC-SH` | Sharing, liking, and commenting | Habilita posting, commenting, liking, sharing de contenido producido por otros miembros de la community |
| `SOC-FR` | Friendship management | Maneja una asociacion simetrica (friendship) o asimetrica (following) entre usuarios |

## Notas sobre el catalogo

- los codigos `OD-*`, `OW-*`, `OM-*` son los que aparecen en cada plataforma de origen; al agregarse al catalogo unificado mantienen el prefijo de origen.
- los patrones `A-*` (action patterns) historicos se renombraron a `CM-*` (content management) en el catalogo final del estandar.
- patrones cross-platform de search sin prefijo de plataforma: `CS-SRC`, `CS-MCS`, `CS-FSR`, `CS-RSRC`, `CS-SRCS`. La excepcion `GEO-LAS` migra a su propia categoria `GEO` por ser intrinsecamente location-dependent.
- el catalogo no es exhaustivo: el estandar admite extensiones custom para todos los main concepts de IFML, lo cual genera familias de patrones especificos a dominio o plataforma fuera del set base.
