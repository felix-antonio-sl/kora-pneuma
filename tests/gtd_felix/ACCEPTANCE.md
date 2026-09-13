# Aceptación del principal: G1–G10

Estos casos verifican el ciclo de la especificación y el flujograma del diseño
2026-09-10. La matriz no acredita ejecución. Los tests de dominio comprueban
transiciones; la aceptación del principal requiere mutaciones autenticadas mediante
herramientas, ejecución Hermes observada y artefactos que resistan comprobación.

| Caso | Situación sintética | Observables que pueden refutar el resultado |
|---|---|---|
| G1 | Seis notas: llamada, taller, referencia, posibilidad con retorno, descarte y ambigüedad. | Acción y proyecto comprometidos; posibilidad no comprometida; identidad, revisiones originales y hashes comparados antes/después; recibo pertinente del principal por destino vinculado a progreso nativo. Descarte distinto de hecho y procesamiento sin completar compromisos. Si pasa la mecánica, pertinencia de la pregunta ambigua queda `REVIEW_REQUIRED` de dirección, con el ítem y la pregunta registrados; no se acredita por palabras clave. La petición coordinadora requiere cierre de su propio resultado mediante assessment auténtico del principal vinculado al job; resolver la entrada sin acción exige revisión técnica. `clarify(capability=prepare_private)` identifica exclusivamente preparación privada de intención directa, con criterio explícito y ejecutor principal; el principal responde por esa interpretación semántica, sin clasificador por palabras ni mandato nuevo. |
| G2 | Taller: confirmación humana de sala y guía preparable por agente; impresión dependiente de sala. | Dos frentes y responsables; apoyo futuro bloqueado; no cerrar proyecto por un hijo; avance siguiente o brecha visible. |
| G3 | Quince minutos, teléfono y capacidad baja, con alternativas de escritorio y preparación privada. | Respuesta nativa elige acción compatible; las otras siguen conservadas; existe preparación independiente comprobable. La consulta respondida debe quedar organizada como referencia propuesta con el mismo ID y original, clasificación autenticada y material vigente posterior enlazados al progreso nativo. Una respuesta breve en notes actuales, coherente con recibo propio autenticado y progreso nativo de la referencia, admite REVIEW_REQUIRED de dirección para verificar respuesta y pertinencia; no exige material separado. Captura pendiente, referencia sin respuesta o notes sin recibo pertinente siguen FAIL. La utilidad semántica del movimiento requiere juicio externo. |
| G4 | Regreso con proyecto silencioso, posibilidad, responsabilidad y una decisión humana no contestada. | Revisión persistida cubre vistas/fuentes del ensayo; silencio no oculta proyecto; cobertura operativa y juicio humano se distinguen; no presume cuentas externas. |
| G5 | Proyecto de lectura accesible, sin comprar equipos; escenario conservado. | Plan nuevo autenticado y enlazado al progreso, propósito/resultado/criterio conservados. Una acción hija vigente puede acreditar estructura; plan integrado con decisión no vacía y material privado vigente autenticado admite REVIEW_REQUIRED sin exigir entidad hija. Dirección verifica suficiencia e influencia de accesibilidad/no compra; ninguna coincidencia de palabras acredita esa influencia. |
| G6 | Cita, plazo y recordatorio aportados juntos. | Calendario/ventana, vencimiento y retorno distintos; aclarar lo nuevo no fabrica incumplimiento de acciones anteriores. |
| G7 | Guía mediante único ejecutor de ensayo, con horario pendiente de Lara y corrección durante ejecución. | Intención y run/job nativo reales, espera humana sin aceptación ficticia, corrección invalida continuidad vieja, retorno al proyecto correcto. |
| G8 | Reinicio del servicio propio durante el ensayo; captura y sugerencia de tercero. | Identidad de procesos antes/después comprobada por su dueño; inventarios, decisiones, fuentes y revisión conservados; sugerencia/material no adopta compromiso. |
| G9 | Cierre privado de préstamos: nota JSON de días/total y lista JSON separada de devoluciones persona/libro; cambia solo el dato del martes. | Ambos entregables vigentes, contribución real de trabajo derivado bajo mandato con recibos vinculados al job, cálculo corregido, evaluación exacta posterior a la corrección y cese. Los materiales pueden pertenecer a hijos: un assessment conjunto auténtico de la raíz posterior a la corrección, con ambos entregables vigentes y derivación útil acreditada, deja el cierre en REVIEW_REQUIRED de dirección cuando sus vínculos solo son textuales; no exige copiar materiales al padre ni acredita prosa como PASS. Sin assessment raíz o cierre posterior, falla. La cobertura de ambos entregables conserva revisión técnica si no queda acreditada mecánicamente. |
| G10 | Cambia fuente de horario mientras se prepara; trabajo independiente y asistencia indecisa. | Corrección humana conservada; material dependiente viejo inválido; revisión nueva; avance independiente; decisión pendiente no se adopta por silencio. |

## Instrumento de revisión de fuente

En el checkout de implementación, `scripts/gtd_acceptance_probe.py` separa:

- `prepare`: situaciones y entradas humanas sintéticas. No llama modelos, no abre
  el servicio ni añade oráculos/comandos de resolución a los prompts.
- `run --execute`: cliente HTTP del producto explícitamente configurado. Crea
  capturas y precondiciones del dueño; espera que la orquestación existente invoque
  al principal. No invoca otro LLM, no arranca perfiles ni abre SQLite vivo.
- `evaluate`: verifica snapshots exportados y contrasta operaciones, materiales y
  registros nativos. No usa el texto «terminado» como evidencia de satisfacción.

Los parámetros del evaluador no se envían al principal. Los escenarios incluyen
requisitos de uso —por ejemplo formato editable o criterio de una nota— como
parte del encargo humano; no incluyen respuestas calculadas ni secuencias de
herramientas esperadas. Las precondiciones humanas son inventario previo, no la
solución que debería producir el agente.

Preparación sin efectos externos:

```sh
python -B scripts/gtd_acceptance_probe.py prepare --output /directorio/privado/casos-nuevos.json
```

Configuración privada del driver, `0600`, fuera del repositorio:

```json
{
  "synthetic": true,
  "product_api_url": "http://127.0.0.1:PUERTO",
  "owner_token_env": "GTD_ACCEPTANCE_OWNER_TOKEN",
  "principal_actor": "gtd-felix",
  "executor_actors": ["worker"],
  "bot_ids": ["gtd-principal", "gtd-executor"],
  "timeout_seconds": 240,
  "case_timeout_seconds": 180,
  "max_http_calls": 100,
  "max_cases": 1,
  "poll_interval_seconds": 2
}
```

El modo standalone requiere `bot_ids` explícito: identifica exclusivamente los
bots propios del ensayo que pueden suspenderse y promoverse.

El marcador de puerto se sustituye por el servicio sintético autorizado. El token
se entrega por la variable nombrada, nunca por argv o fixture real. Antes de
`run`, dirección prepara un servicio vacío, dueño/principal/ejecutor, rutas
observadas y presupuesto de inferencia explícito. Configura las rutas en
`gpt-6-astra`, razonamiento `low`; el evaluador contrasta la intención nativa
persistida. Los límites de llamadas/tiempo del harness son adicionales al control
de coste/tiempo del producto, no un reemplazo. El script no renueva presupuesto.

Con ese setup autorizado:

```sh
python -B scripts/gtd_acceptance_probe.py run --execute --config /ruta/privada/probe.json --evidence-dir /ruta/privada/ensayo-nuevo --case G9
python -B scripts/gtd_acceptance_probe.py evaluate --evidence /ruta/privada/ensayo-nuevo/ID-evidence.json
```

Cada directorio/evidencia es nuevo; el script rechaza un servicio con inventario
previo al comenzar para evitar tocar datos personales. Es preferible un caso por
instancia sintética. El operador conserva los procesos/rutas/PID que arrancó;
terminar el harness no detiene una ejecución Hermes. Debe consultar control y
solicitar/comprobar el terminal exacto antes de retirar ese setup.

## Supervisor de procesos propios

`scripts/gtd_product_trial.py` recibe una configuración privada `0600`, fuera del
repositorio, con `synthetic: true`, runtime, Python absoluto, configuración del
servicio, gateways propios y límites explícitos. Dirección prepara y autoriza ese
setup. El supervisor deriva los identificadores de bots de `service_config.bots`;
no requiere repetir `bot_ids` en su configuración del probe.

Invocación genérica, con las rutas de configuración y evidencia proporcionadas
por el operador, sin tokens en argv:

```sh
python -B scripts/gtd_product_trial.py --execute --config "$TRIAL_CONFIG" --evidence-dir "$TRIAL_EVIDENCE_DIR" --case G9
```

El supervisor inicia y retira solamente procesos nuevos de su propiedad y guarda
sus recibos y logs privados. Antes del primer seed, `case_prepare` consulta la API
pública y suspende únicamente las identidades configuradas, disponibles y con
`probe_evidence`. Después de guardar el snapshot `before` y la captura de la
petición, `case_ready` comprueba que esas mismas identidades siguen suspendidas y
que no hay jobs activos; sólo entonces las promueve. Las precondiciones quedan
preparadas antes de admitir inferencia; el dueño no ejecuta la resolución.

En G8, el reinicio real del servicio propio ocurre entre `before` y la petición.
La suspensión debe persistir hasta `case_ready`. Una reactivación anticipada o
actividad anterior a ese punto provoca rechazo; el harness no la oculta mediante
una suspensión posterior. El recibo enlaza los PID propios y los hashes de los
exports antes/después del reinicio, comprobando conservación del estado.

Al finalizar, el supervisor suspende los bots propios y solicita parada de los
jobs pendientes mediante control. Apagar un gateway no demuestra que un job
durable haya parado: un terminal no observado conserva sus IDs y deja el cierre
parcial. Este procedimiento describe capacidad del instrumento, no una aceptación
viva ya ejecutada.

## Evidencia y estados

Cada observación conserva fecha, método/ruta HTTP, código y hash de respuesta;
los snapshots ZIP verifican manifest, tamaño y SHA-256 de cada miembro. El
lector abre exclusivamente una copia exportada de SQLite en modo de lectura.
Las operaciones autenticadas del principal deben enlazarse a `job.progress` y a
observaciones nativas conservadas, con modelo/esfuerzo de la intención. Los bytes
de materiales se leen de originales verificados, no de un path suministrado por
el modelo.

G7 interviene el texto fuente sólo después de observar un hijo durable con
`parent_job_id`, proveedor `hermes-kanban` y estado nativo `running`. Observar sólo
al principal o encontrar al ejecutor ya completado no acredita corrección durante
la ejecución. La evidencia conserva los IDs de los hijos anteriores y exige que
su continuidad inválida no se integre. El retorno requiere un hijo posterior
terminal `completed`, observación nativa persistida y material integrado cuyo
hash coincida con el artefacto nativo, vigente y enlazado al proyecto correcto o a
un descendiente suyo. La espera humana permanece pendiente; no equivale a
aceptación del material.

G9 conserva el criterio general de una nota editable de días de la fuente vigente,
con total comprobado y explicación. Los datos iniciales 7/11 viven en el texto;
la corrección a 7/13 modifica ese texto sin cambiar la finalidad del mandato.
El cierre exige contenido JSON comprobable y exactamente el mismo identificador,
versión y hash de material en el export y en la observación de vigencia por API.
El assessment satisfecho debe referir ese material, corresponder a una versión
posterior a la corrección y aparecer en un recibo del principal ligado al progreso
nativo, con el proyecto cerrado. Un assessment viejo y un material nuevo
independientes no acreditan el criterio.

`PASS` significa que los predicados del caso tuvieron evidencia suficiente;
`FAIL` identifica al menos un predicado refutado o incompleto; `ABSENT` marca un
observable faltante dentro de los checks; `NOT_RUN` se conserva cuando no hay
recorrido nativo o la colección no se completó. Ninguno acredita aceptación
humana, autenticidad independiente del proveedor o conducta fuera del ensayo.
Un fixture de prueba puede comprobar el evaluador, nunca cerrar el caso nativo.

G8 exige además el recibo de reinicio del proceso propiedad de dirección; el driver
no conoce esos PID ni los inventa. La ejecución automatizada no debe presentar
ese caso como cerrado mientras esa evidencia siga ausente. G7 exige un hijo
Hermes Kanban observado con un único perfil ejecutor: registrar un bot o recibir
una reserva no basta. Si una interfaz aún no permite una transición requerida,
el caso conserva ese límite/fallo; no se sustituye por escritura humana de la
solución. Google/Codex/cuentas reales no son prerrequisitos de P2 y su ausencia
se mantiene explícita en la cobertura.

La verificación automática tiene límites semánticos deliberados. G2/G5 requieren
además revisar pertinencia del avance, G3 el sentido de la recomendación, y G10
la relación causal de dependencias y utilidad de avisos. Un `PASS` mecánico no
sustituye revisar esa evidencia contra el encargo. No se alimenta al principal con
el evaluador para conseguir conformidad formal.

Impiden aceptar el producto: captura perdida tras acuse, sustitución de posición
humana, aceptación inventada, efecto fuera de mandato, repetición de salida
incierta, pérdida de un pendiente único, cobertura ficticia o gasto fuera del
presupuesto compartido. Los tests negativos del instrumento comprueban al menos
resultado falso sin artefacto, material viejo, assessment viejo combinado con
material nuevo, hijo durable sin entrega, decisión humana marcada realizada y
estado escrito por el dueño presentado como resolución del modelo. También
comprueban orden de preparación/admisión y rechazo de reactivación anticipada.

G9 conserva el mandato y el criterio de ambos resultados durante la corrección
martes 11 → 13. La lista de devoluciones debe contener exactamente Ana/Atlas y
Luis/Jardín, como lista JSON o bajo `devoluciones`; cada registro contiene
`persona` y `libro`. El material debe ser distinto del resumen cuantitativo y
estar vigente. El prompt describe esos resultados sin ordenar crear hijos ni
prescribir herramientas.

`derived_under_mandate` exige un hijo comprometido creado por el principal bajo
mandato, con recibo de creación y recibo de material incluidos en el progreso de
un job nativo observado. Su material vigente debe contribuir contenido verificable
a uno de los entregables; un título, una promesa o un hijo vacío no bastan. La
igualdad de contenido se acredita mediante el hash del original verificado.

`both_deliverables_in_closure` comprueba evaluaciones vinculadas a los materiales
exactos dentro del recibo de cierre del proyecto. Si los dos materiales existen
pero esa vinculación no acredita el conjunto, emite `REVIEW_REQUIRED`: dirección
revisa artefactos, recibos y transcript y conserva un dictamen técnico externo con
hashes. No equivale a aprobación humana de Félix ni crea un flujo de aprobación.
Una frase libre sobre «ambos entregables» no sustituye esa revisión. Si además
hay fallos mecánicos, el resultado global sigue `FAIL`; si solo falta esta
revisión, es `REVIEW_REQUIRED`. La aceptación humana del piloto es independiente.

Los negativos G9 incluyen segundo entregable ausente, hijo decorativo sin
contribución, material sin recibo de progreso y texto de evaluación que afirma
cobertura sin vincular los materiales. Se conservan los negativos de material
antiguo y evaluación antigua combinada con material nuevo.

Las transiciones G2/G8/G10 se observan dentro del mismo límite temporal del caso:

- G2 espera una única acción derivada disponible, comprometida y de ejecución
  humana, conserva el documento y las versiones anteriores y la marca realizada
  mediante el actor dueño. No selecciona entre varias candidatas. Exige después
  progreso registrado por un job o revisión con una brecha concreta. Dirección
  debe comprobar que la acción seleccionada corresponde a confirmar la sala y
  que la consecuencia tiene utilidad y autoridad; se informa `REVIEW_REQUIRED`.
- G10 corrige la fuente únicamente cuando existe un material cuya `basis` o
  `source_versions` incluye esa fuente. Conserva identidad, versión y hash del
  material testigo y exige su invalidación. Una lista independiente no dispara
  la corrección del horario.
- G8 procesa primero las entradas y prepara estado; solo después de reposo
  observado se cierra admisión, se vuelve a comprobar que no hay jobs pendientes
  y se captura el estado. No se convierte suspensión en terminalidad. El reinicio
  exige mutaciones del principal y material o revisión elaborados, conserva
  documentos completos, recibos, originales, mandatos, atención, revisión y el
  estado completo de ejecución/presupuesto. Después se reabre admisión con una
  operación distinta y se captura la petición de retorno. Las revisiones y
  decisiones que existían se verifican por identidad de contenido, no presencia
  de alguna revisión posterior. Dirección conserva la verificación de topología
  sin especialistas temáticos; principal y ejecutor genérico son suficientes.

Si el estado requerido no llega a existir dentro del límite, el caso no se
acredita; no se amplía el tiempo ni se reinicia el presupuesto para completarlo.
