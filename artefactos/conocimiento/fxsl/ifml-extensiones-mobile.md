---
urn: urn:fxsl:kb:ifml-extensiones-mobile
nombre: ifml-extensiones-mobile
version: 1.0.0
estado: publicado
descripcion: "Extensiones IFML para apps mobile y multiscreen: dimensiones contextuales (Device/Network/Position), containers «system», sensors/camera/NFC, MapView/Marker/Path, gestures como events y adaptacion dinamica multiscreen."
fuente: "Migrado de la bestia (~/kora) artifacts/knowledge/fxsl/ifml/ifml-extensiones-mobile.md (sha256:650b91ab8c71cc860668e336c6a80283abc5464e5a7d78b56925cc2041817fd3); cuerpo integro, solo se aplano el frontmatter anidado. Fuente original: Ifml-In-A-Nutshell (Brambilla & Fraternali) cap.7 secciones Mobile Extensions y Multiscreen Extensions, estandar IFML/OMG."
autor: FS
creado: 2026-05-07
lang: es
tags: [ifml, mobile, multiscreen, mapview, gestures, omg]
familia: bok
cita: [urn:fxsl:kb:ifml-corpus-index, urn:fxsl:kb:ifml-view-containers, urn:fxsl:kb:ifml-extensiones-web]
---

# IFML — Extensiones mobile y multiscreen

## Resumen

Extensiones IFML para aplicaciones mobile: dimensiones contextuales especializadas (Device, Network, Position), `ViewContainer` y `ViewComponent` system-level (`«system»`), interaccion con sensors (camera, NFC, position), visualizacion geografica (`MapView`, `Marker`, `Path`), gestos como events extendidos. Cierra con multiscreen extensions para adaptacion dinamica a multiples factores de pantalla.

## 1. Context extensions

El `Context` (definido en `ifml-view-containers`) cobra protagonismo en mobile: la interfaz debe explotar todas las dimensiones disponibles para entregar interacciones eficientes.

### 1.1 Device

Dimensiones para adaptar la UI al dispositivo. Usadas tipicamente como `ContextDimension`:

| ContextDimension | Significado |
| --- | --- |
| `DiagonalSize` | Tamaño fisico de la pantalla, medido como diagonal |
| `SizeCategory` | Clases de tamaño tratadas homogeneamente: `SMALL`, `NORMAL`, `LARGE`, `EXTRA LARGE` |
| `DensityCategory` | Clases de densidad: `LOW`, `MEDIUM`, `HIGH`, `EXTRA HIGH` |

Como `ContextVariable` (calibracion fina basada en valor):

| ContextVariable | Significado |
| --- | --- |
| `PixelSize` | Tamaño horizontal y vertical en pixels |
| `Density` | Pixels por unidad de area (dpi) |

Otras caracteristicas (memoria, processing power, battery) son tipicamente irrelevantes para la composicion de UI.

### 1.2 Network connectivity

Adapta cantidad/calidad del contenido segun capacidad del link.

`ContextDimension` relevante:

- **`ConnectivityType`** — tipo de red disponible. Valores: `NONE`, `BLUETOOTH`, `NFC`, `ETHERNET`, `MOBILE` (E, G, 3G, 4G, ...), `WIFI`, `WIMAX`.

Caso tipico: en `MOBILE`, mostrar attachments de mensaje on-demand con `ScrollableList` en lugar de bajarlos automaticamente; reduce bandwidth y latency.

### 1.3 Position

Adapta la interfaz a la actividad presunta del usuario o publica contenido dependiente de location.

`ContextDimension`:

| Elemento | Valores |
| --- | --- |
| `SensorStatus` | `ACTIVE`, `INACTIVE` |
| `Activity` | `still`, `walking`, `running`, `cycling`, `in-vehicle` |

`ContextVariable` (cuando `SensorStatus = ACTIVE`):

| Variable | Semantica |
| --- | --- |
| `Location` | Posicion del dispositivo (latitude, longitude) |
| `Accuracy` | Accuracy de la posicion |
| `Speed` | Speed terrestre del dispositivo |
| `Altitude` | Altitud sobre nivel del mar |

## 2. System ViewContainer y ViewComponent

Los mobile interfaces (y desktop, menos pervasivamente) usan containers predefinidos del SO o framework, devotos a funcionalidades especificas con economia de espacio y consistencia cross-application.

**System ViewContainer** — `ViewContainer` stereotyped como `«system»`. Denota una region fija manejada por el SO o framework cross-application.

Ejemplos: `Notifications` area, `Settings` panel.

`ViewComponent` analogos: `«system»` denota uso de componentes built-in del SO (ej. media gallery por defecto).

## 3. Cameras y sensors

Interaccion basica con camera requiere modelar:

- `ViewContainer` para la imagen y comandos.
- invocacion de `Action` para tomar la foto.
- evento asincrono que notifica que la foto esta lista.
- visualizacion en system-level media gallery.

Patron `PhotoShooter`:

- system `ViewContainer` `CameraCanvas` (visor de la camera).
- `Settings` event abre modal para parametros.
- `Shoot` event toma la foto.
- al estar lista, viewer activado; un evento permite abrir la foto en system media gallery.
- internal viewer modelado como `ScrollableList` con `block size = 1` (una imagen a la vez) y `OrderBy` por timestamp (mas recientes primero).

## 4. Communication

Aspectos de comunicacion que afectan la UI:

| Aspecto | Modelado |
| --- | --- |
| Connectivity update notifications | `SystemEvent` que expresa update de una o mas `ContextDimension` |
| Devices in range | `SystemEvent` que señaliza descubrimiento de un device |
| Data transfer | `Action` que encapsula detalles del protocolo |

Ejemplo NFC (Near Field Communication):

- **NFCCardSender** — interfaz minima (NFC requiere proximidad). Presenta data personal al usuario; confirma intencion. `SendViaNFC` `Action` arma el record y notifica readiness.
- **NFCCardReceiver** — recibe payload como evento asincrono que abstrae el parseo NFC y triggering de la app registrada. UI minima: confirmar y guardar, o discardar.

Patron de adaptacion por connectivity:

- dos versiones de la misma interfaz (`Read message`).
- v1: attachments descargados automaticamente.
- v2: comando explicito por attachment + `ScrollableList` mostrandolos uno a uno.
- la eleccion via `ActivationExpression` que testea `ConnectivityType`. On-demand cuando `MOBILE`.

## 5. Position tracking

Patron de uso del position sensor (`Tracker`):

- `Start` event en `Tracker` `ViewContainer` activa el continuous tracking.
- `Form` permite especificar parametros (accuracy, frequency).
- `ActivatePositionUpdates` `Action` comunica los parametros al servicio.
- la app empieza a escuchar `SystemEvent` asincronos con position updates a la frecuencia establecida.
- cada evento lleva timestamp + coordenadas, dispara `Action` background que almacena `Point`.
- lista de puntos visible en `TrackingPoints` `List`.
- comandos: clear, save as track, stop tracking.

## 6. Maps

Las maps son interfaces over geographic data muy usadas en mobile. Caracteristicas comunes:

- conexion al mapping service y descarga de tiles.
- controles: pan, zoom.
- map type: normal, satellite, hybrid, 3D.
- viewpoint (camera): location, zoom, bearing, tilt.

### 6.1 MapView

**MapView** — extension de `ViewContainer` que denota una map view. Soporta events para panning, zooming, change de map type y camera parameters.

### 6.2 Marker

**Marker** — extension de `ViewComponent` usable en `MapView` containers. Denota que las instancias del `DataBinding` poseen un atributo location renderizable como marcadores interactivos.

Events soportados: select, drag, drop.

Notacion: stereotype `«marker»` agregado a `Details` o `List`.

### 6.3 Path

**Path** — extension de `List` usable en `MapView` containers. Presenta las instancias del `DataBinding` (que deben tener atributo location) como polilinea en el mapa.

Events soportados: seleccion del path entero o de un punto individual.

Caso tipico: visualizacion de tracking points como `Marker` set o como `Path` (en lugar de plain list).

## 7. Gestures

Touchscreens permiten gestos de manipulacion directa de objetos en pantalla. Conjunto soportado:

- touch, double touch, press, swipe, fling, drag, pinch in/out, etc.

Cada gesto tiene semantica bien definida y convenciones consolidadas que el diseño debe respetar.

Modelado: extender el core `Event`.

Caso tipico (master detail con gestos):

| Gesto | Efecto |
| --- | --- |
| `«touch»` | Activa default action sobre el objeto (apertura del detail) |
| `«press»` | Activa selection mode; subsequent `touch` permite seleccionar uno o varios; toolbar de comandos disponible para actuar sobre seleccionados |

Convencion ligada a sistemas mobile populares (Android 4 y similares). Se modela combinando `«press»` y `«touch»` extensions con `ActivationExpression` que condiciona el efecto del touch a la existencia de objeto previamente seleccionado.

## 8. Multiscreen extensions

Single-screen apps definen la composicion en design-time para una sola clase de devices. **Multiscreen apps** se diseñan para devices distintos con caracteristicas variables; objetivo: layout flexible que se adapta dinamicamente a tamaño, orientacion, density.

### 8.1 Patron tipico

`Settings` `ViewContainer` con dos subcontenedores que cubren la misma tarea de dos formas:

- `Tablet Settings` — dos `ViewComponent` simultaneos (`Preferences` `List` + `PreferenceEditor` `Form`).
- `Phone Settings` — un `ViewComponent` a la vez.

Cada subcontainer tiene `ActivationExpression` que asegura que el patron de composicion correcto se activa segun device info del `Context`.

### 8.2 Caveat de duplicacion

El patron multiscreen duplica `ViewComponent`, `Event`, `InteractionFlow` y `Action` que especifican contenido y comportamiento en las dos configuraciones. Esto:

- carga al diseñador con repeticion.
- genera misalignment errors potenciales.

Solucion mencionada en el estandar: uso de **modules** (mecanismo no cubierto en este corpus, ver capitulo 8 del libro original).

## 9. Caveats arquitecturales sobre extensiones mobile

- la lista de `ContextDimension`/`ContextVariable` para mobile es **ejemplificadora, no exhaustiva**. El estandar referencia bibliografia para catalogos completos. La meta es mostrar como features contextuales se representan como IFML extensions.
- la asignacion de extensiones a clases de aplicacion (desktop/web/mobile) es algo arbitraria. La convergencia de plataformas hace imposible distinguir features sharply. Cada extension se ubica donde se origino o donde se usa mas frecuentemente.
- `«system»` containers/components transfieren responsabilidad al SO/framework, lo que reduce control del diseñador pero gana consistencia cross-application.
