# hermes-agent-specialist

Especialista operativo en **Hermes Agent** de Nous Research para Félix: crear,
configurar, mantener y diagnosticar perfiles, skills, contexto, memoria e
integraciones nativas. Úsalo cuando el resultado dependa del funcionamiento de
Hermes. Si el encargo se refiere a los modelos Hermes LLM, identifica esa
frontera antes de aplicar instrucciones de la plataforma.

Para autorar o mantener productos KORA, usa la
[guía vigente](../../../docs/operacion.md) e `instalacion-kora`. Esta skill aporta el
contraste con Hermes. KORA conserva la fuente agnóstica y realiza sus productos
en Codex y Hermes; un archivo nativo, una carga correcta y una conducta
observada acreditan hechos distintos.

## Resolver el caso y su evidencia

Identifica el resultado buscado, el perfil y `HERMES_HOME` efectivos y la
superficie afectada. Distingue instalar o actualizar un perfil, alojar el
proceso Hermes y elegir dónde ejecutan sus herramientas mediante
`terminal.backend`. Si se menciona Docker, resuelve cuál de esas operaciones
se necesita a partir del contexto; pregunta solo si la diferencia sigue
abierta y cambia la actuación.

Cuando una decisión dependa de una capacidad o formato vigente, consulta la
página oficial pertinente y contrástala con la instalación: `hermes --version`,
la ayuda del comando y, si hace falta, el código o una prueba acotada. Reutiliza
la evidencia ya obtenida si corresponde a la misma versión y condición. Una
corrección editorial no necesita repetir un inventario completo de Hermes.
Si la documentación y el comportamiento observado difieren, informa ambos y
resuelve la operación con evidencia; no declares inexistente algo solo porque
falta en una página.

Parte de la documentación necesaria, sin cargar el sitio completo:

| Necesidad | Fuente oficial |
|---|---|
| Instalar o actualizar Hermes | [Instalación](https://hermes-agent.nousresearch.com/docs/getting-started/installation) |
| Perfil, configuración y backend | [Perfiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles), [configuración](https://hermes-agent.nousresearch.com/docs/user-guide/configuration) |
| Identidad y contexto de proyecto | [SOUL.md](https://hermes-agent.nousresearch.com/docs/user-guide/features/personality), [context files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files) |
| Skills y recursos | [Skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) |
| Distribuir o actualizar un perfil | [Distribuciones](https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions), [comandos de perfiles](https://hermes-agent.nousresearch.com/docs/reference/profile-commands) |
| Memoria | [Memoria](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory) |
| Proveedor, MCP, canales u otra integración | [Índice oficial](https://hermes-agent.nousresearch.com/docs/llms.txt), luego la página de la integración |

`referencias/llms-index.txt` conserva una copia del índice recibida como recurso
original. Puede ayudar a localizar temas; sus descripciones, ejemplos y enlaces
pueden haber cambiado. Confirma la información utilizada en el sitio vigente.
No requiere mantener un segundo inventario manual de comandos o capacidades.

## Identidad, contexto y memoria

`SOUL.md` se carga desde el `HERMES_HOME` efectivo; no es una entrada de proyecto.
El contexto del repositorio puede usar `AGENTS.md`. Comprueba la precedencia de
los archivos presentes y el directorio de arranque cuando una instrucción no
llegue al agente. No crees copias de la misma instrucción en varias superficies
para intentar forzar su carga.

La carga de contexto puede aplicar escaneo y recorte según la configuración y
el modelo. Usa `prompt-size` cuando necesites inspeccionar el ensamblaje local;
no acredita por sí solo una llamada al proveedor ni la conducta del agente.
El inspector puede crear estado, logs y cachés al arrancar: cuando baste una
comprobación de carga, úsalo en un home temporal o reutiliza el probe de
`docs/hermes.md`, sin iniciar ni copiar memoria o credenciales personales.
Comprueba el contenido requerido, no solo la existencia o el tamaño del archivo.

La memoria personal vive bajo `HERMES_HOME/memories/`. Su snapshot inicial y los
cambios persistidos durante una sesión no son el mismo estado. Si el encargo
afecta memoria, revisa el mecanismo nativo y los límites efectivos, preservando
el contenido ajeno al cambio. Instalar un agente no autoriza a reemplazar la
memoria de Félix.

## Perfiles, configuración y ejecución

El perfil delimita el estado Hermes; por sí solo no aisla el filesystem del
host. `terminal.backend`, directorio de trabajo y política de home de las
herramientas determinan dónde se ejecutan comandos y qué datos alcanzan.
Comprueba mounts o credenciales reenviadas cuando esa frontera afecte el
encargo. En el host personal, conserva la configuración adecuada que ya usa
Félix sin imponer una arquitectura de aislamiento nueva.

Resuelve la configuración efectiva de las claves que vas a cambiar, incluidas
opciones de invocación y claves administradas si existen. Los secretos usan el
mecanismo nativo correspondiente: `.env`, `auth.json` o una fuente de secretos.
No imprimas valores ni los incorpores en productos, ejemplos o evidencia. Una
selección de perfil no demuestra que herede la configuración del perfil raíz.

Para proveedores, canales y MCP, consulta solo la integración necesaria y
comprueba su disponibilidad y configuración efectiva. Evita fijar catálogos de
modelos, plataformas o límites numéricos en esta skill. Un comando documentado
puede depender de versión, herramientas habilitadas o credenciales disponibles.

## Skills y distribuciones

Las skills se descubren desde las raíces de proyecto, perfil y directorios
externos configurados. Su visibilidad y precedencia dependen de la confianza
y configuración efectivas. Ante un nombre duplicado, identifica sus archivos y
comprueba la carga de la skill elegida; aparecer en el listado no garantiza
que `skill_view` la resuelva. `skill_view(name, path)` recupera recursos del
bundle, no archivos arbitrarios del host.

Mantén instrucciones y recursos en la fuente que realmente los administra.
Hermes puede modificar skills mediante `skill_manage`; una skill realizada por
KORA necesita reconciliar esos cambios en su fuente antes de actualizarla.
El nombre igual no prueba procedencia ni permite sobrescribir una instalación
ajena. La skill incorporada `hermes-agent` y este producto
`hermes-agent-specialist` conservan identidades y mantenimiento distintos.

Una distribución declara qué archivos reemplaza. Antes de un update nativo,
comprueba la procedencia registrada y el efecto de `distribution_owned` sobre
ediciones existentes; la propiedad de un directorio puede incluir archivos que
el usuario agregó. Para productos administrados por KORA, sigue
`instalacion-kora`: su estado y recuperación deciden qué archivos actualizar.
El detalle contrastado del adaptador está en `docs/hermes.md`, dentro de la raíz
que contiene `kora_cli.py`; no mantengas aquí otra especificación del instalador.

La presencia de `distribution.yaml` no acredita que `hermes profile update`
tenga una fuente registrada. Tampoco uses `hermes profile delete` para retirar
solo un producto: ese comando elimina el perfil y su estado. Resuelve el
alcance y la autoridad de la operación antes de actuar, aprovechando la
instrucción ya otorgada para ese destino.

## Comprobar y entregar

Realiza el menor cambio que resuelva el caso y comprueba su efecto pertinente:
formato y lectura para una entrada nativa; configuración efectiva para una
opción; operación representativa y límite decisivo cuando se cambie conducta.
Una prueba de red o un mensaje a un canal necesita la autoridad correspondiente;
no envíes mensajes de prueba por rutina. Usa entornos temporales cuando basten
para observar el mecanismo sin afectar el estado personal.

En una auditoría, inspecciona las piezas que expliquen la necesidad o el fallo.
No conviertas cada consulta en un censo de memoria, credenciales, canales y
servicios. Reporta el problema, la evidencia y la corrección suficiente.

Entrega los cambios utilizables, las fuentes consultadas, el efecto observado
y los límites materiales. Si falta una comprobación, indica qué afirmación
queda pendiente. No presentes un archivo válido, un prompt ensamblado o una
respuesta aislada como equivalencia conductual general.
