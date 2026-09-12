# Operar KORA

Ejecuta los comandos desde la raíz que contiene `kora_cli.py` y `README.md`.
En h289, la maquinaria vive en `/home/felix/kora-pneuma` y la biblioteca central
en `/home/felix/kora-knowledge`. El enlace `knowledge` conecta ambas. Los agentes
y skills se mantienen en la maquinaria; los conocimientos se consultan desde la
biblioteca, donde cada publicación conserva su versión anterior.

El núcleo requiere Linux con `renameat2`, Python 3.12 y las dependencias de
[requirements.txt](../requirements.txt). El [README](../README.md) contiene la
preparación del entorno. La CLI funciona localmente sin modelo ni red y entrega
JSON; un conflicto produce un código distinto de cero. Usa
`python3 kora_cli.py COMANDO --help` para consultar argumentos.

## Seleccionar las fuentes y encontrar referencias

`--root RUTA` selecciona otra raíz de agentes y skills. `--knowledge-root RUTA`
selecciona otra biblioteca y reemplaza el enlace de esa raíz para la operación,
sin modificarlo. Ambas opciones van antes del subcomando.

```sh
python3 kora_cli.py list --kind knowledge
python3 kora_cli.py list --kind skill --target codex
python3 kora_cli.py list --kind skill --query 'recuperación'
python3 kora_cli.py list --archived
python3 kora_cli.py resolve urn:kora:kb:frontera-fuentes-tecnicas
```

Lee el `path` devuelto antes de usar el contenido. Las referencias publicadas
aparecen en consulta; los borradores no. Un alias lleva a la identidad conservada
y resolver una referencia archivada no la vuelve activa. `resolve URN --revision
SHA` recupera una versión exacta cuando la respuesta o cita debe ser reproducible.

Para encontrar contenido sin recorrer borradores ni versiones anteriores, usa
`rg --follow -l 'término' knowledge/references`. La búsqueda lee las referencias
vigentes directamente; no requiere mantener un índice adicional.

`list --query TEXTO` busca en identidad, nombre, descripción, propósito, ámbito,
palabras clave y relaciones presentes en la ficha. `resolve URN --target codex`
explica el cierre dirigido y la disponibilidad de sus necesidades. Una falla
ajena solo se contiene si su identidad puede distinguirse sin colisión; `check`
reúne los defectos que encuentra. Si un archivo mal formado deja indeterminada
su identidad, la resolución focal informa esa incertidumbre.

La biblioteca conserva conocimientos heredados como `legacy`. Siguen disponibles
con ese estado; su traslado no acredita una aprobación nueva de Félix. Una
revisión posterior sigue el flujo de borrador y aprobación que se describe abajo.

## De recursos a conocimiento consultable

Guarda los recursos de entrada cuando los recibas. `intake` conserva los
originales y devuelve dónde quedaron; repite `--source` para incorporar varios:

```sh
python3 kora_cli.py intake tema --source /ruta/a/la/fuente.pdf
```

Lee los originales, localiza conocimiento existente y aplica `koraficacion`, que
usa `koraficacion-integral` como procedimiento por defecto para cualquier fuente.
El cuerpo conserva todo el contenido sustantivo con economía; procedencia y
soporte quedan en la evidencia auxiliar salvo lo necesario para interpretarlo.
Coteja y repara antes de entregar. La CLI no sintetiza el contenido. Para crear un conocimiento nuevo
con el cuerpo preparado y las fuentes recuperables:

```sh
python3 kora_cli.py create knowledge personal tema --id urn:personal:kb:tema \
  --description 'Alcance y condiciones de la fuente' \
  --body /ruta/al/conocimiento.md --source /ruta/a/la/fuente.pdf
```

El resultado queda en `drafts/<namespace>/<name>`, con `object.yaml`, contenido y
originales copiados con su hash y origen. Puedes usar como `--source` la ruta que
entregó `intake`. Repite `--requires URN` para los conocimientos necesarios para
su uso; conserva otros vínculos en `relations`. Un recurso técnico mantiene su
formato cuando pasarlo a prosa destruiría su función.

Para cambiar un conocimiento existente, prepara su borrador y edita los archivos
que entrega el comando:

```sh
python3 kora_cli.py revise urn:personal:kb:tema
```

Conserva su identidad, los originales pertinentes y la procedencia actualizada.
La referencia publicada sigue disponible durante ese trabajo. No edites
directamente `references` ni las versiones conservadas en `versions`.

Coteja el borrador con sus originales y comprueba una pregunta que dependa de su
contenido, incluyendo una excepción o ausencia cuando cambie el uso. Después
obtén la revisión concreta:

```sh
python3 kora_cli.py review urn:personal:kb:tema
```

`review` devuelve rutas, `reviewed_sha256` y revisión base. Presenta a Félix el
contenido revisado, su procedencia y las pérdidas o incertidumbres materiales.
Cuando haya aprobado ese contenido, o delegado explícitamente esa decisión,
publica usando el hash devuelto:

```sh
python3 kora_cli.py approve urn:personal:kb:tema --reviewed SHA_REVISADO
python3 kora_cli.py resolve urn:personal:kb:tema
```

El permiso para modificar maquinaria no aprueba conocimiento. `approve` comprueba
que publica el borrador revisado; no verifica por sí solo quién lo autorizó ni
su fidelidad semántica. Si el borrador o su revisión base cambió, vuelve a revisar
el contenido afectado antes de publicarlo.

La publicación conserva una versión en `versions` y actualiza su enlace estable
en `references`. Agentes y skills que leen esa referencia encuentran la nueva
versión sin reinstalarse. Para corregir un conocimiento publicado, prepara otra
revisión; las versiones anteriores siguen disponibles para consulta exacta.

`--candidate NOMBRE` permite mantener alternativas explícitas en `create
knowledge`, `revise`, `review` y `approve`. Cada una conserva la revisión base y
el nombre canónico de publicación. Publicar una alternativa no sobrescribe las
otras; la siguiente aprobación detecta si su base quedó obsoleta. Sin ese
argumento se mantiene el recorrido habitual de un borrador.

`intake --provenance ARCHIVO_JSON` recibe una lista de metadata en el orden de
los `--source`: localizador, fecha de obtención, versión o vista y límites de
extracción cuando se conocen. Los originales se conservan por bytes. Obtener o
calcular el hash de un archivo no acredita que fue extraído, leído o revisado.
Los valores presentes, ausentes, cero, falso y nulo se mantienen en el original.

`measure --source TEXTO --body CANDIDATA --auxiliary AUXILIAR --wrapper ENVOLTURA`
mide textos UTF-8 comparables. `--source` y `--auxiliary` pueden repetirse. El
resultado identifica tokenizer, versión, encoding y costo de cada componente;
el costo completo incluye los auxiliares requeridos y la envoltura. El contador
`tiktoken` es optativo y se instala en el entorno Python que ejecute esa orden.
Sin contador, encoding disponible o texto comparable, la salida dice
`NOT_MEASURED` y explica por qué. Medir no demuestra fidelidad ni autoriza
publicación; los binarios requieren una representación comparable identificada.

## Autoría de agentes y skills

Usa `autoria-kora` para preparar la conducta y las capacidades necesarias.
`create skill` y `create agent` reciben namespace, nombre, `--id`, `--description`
y `--body`, con la misma forma del ejemplo anterior. Conservan una candidata,
validan los destinos declarados y admiten la fuente en
`products/<namespace>/<name>` de la maquinaria. Los cuerpos no llevan un segundo
frontmatter. Codex y Hermes son los destinos por defecto; `--target` permite
restringirlos.

`requires` declara skills necesarias y conocimientos publicados que deben poder
consultarse. `relations` conserva vínculos documentales que no implican
instalación. Los conocimientos permanecen en la biblioteca; no se copian dentro
del agente o skill. Conserva junto al cuerpo los scripts, ejemplos y otros
recursos propios que necesite el procedimiento.

En agentes y skills, `resources` puede declarar archivos o directorios relativos
acotados, sin globs ni enlaces. Por ejemplo:

```yaml
resources:
  - scripts
  - references/plantilla.json
  - assets/ejemplo.bin
  - .env.example
```

Una declaración vacía significa que el producto no distribuye auxiliares. Sin
ese campo, la compatibilidad conserva recursos de `referencias`, `references`,
`scripts`, `agents` y `sources`. Los originales identificados en la procedencia
se conservan en la fuente, fuera del bundle, salvo selección operativa explícita.
Un auxiliar fuera de estos contenedores requiere declaración. Cachés, bytecode,
temporales y estado privado quedan excluidos; una plantilla declarada puede
conservar su formato nativo. El cuerpo, la ficha y los recursos seleccionados
determinan la huella distribuible. Las revisiones de conocimiento mantienen su
algoritmo de integridad y sus archivos históricos.

Una necesidad simple sigue siendo una URN incondicional que consulta la versión
vigente. Los campos ampliados son optativos y no reescriben esa forma anterior:

```yaml
requires:
  - urn:ejemplo:skill:metodo
  - id: urn:ejemplo:kb:regla
    kind: knowledge
    revision: <SHA-256 de la versión conservada>
  - id: urn:ejemplo:skill:analisis
    kind: product
    target: codex
    condition: el encargo requiere analizar una excepción
    purpose: aplicar el procedimiento especializado
```

`kind` puede ser `product`, `knowledge` o `capability`; si se omite, se deriva del
objeto resuelto. `target` restringe el destino y `condition` identifica un caso;
el núcleo no interpreta esa frase como código. Una necesidad condicional
satisfacible queda disponible anticipadamente; si falta ella o su cierre, las
instrucciones nativas señalan ese recorrido como no disponible. Una necesidad
obligatoria ausente impide realizar el producto. Dos revisiones incompatibles
de una misma identidad se informan como conflicto.

Las capacidades se comprueban con evidencia del entorno. `--capability IDENTIDAD`
declara al preparar, comprobar o explicar que el llamador ya la contrastó; la
salida conserva ese origen y no concede permisos ni credenciales. Tener archivos
de una skill disponibles tampoco ejecuta sus helpers.

Cada preparación reutiliza bytes y verificaciones dentro de una fase. `check`
devuelve trabajo por objetos, referencias, bytes y tiempo. Las fases posteriores
leen de nuevo; antes de producir efectos se contrastan los archivos, las
identidades y los enlaces relevantes. En la API Python, `Catalog.phase()` permite
agrupar una preparación coherente y `Catalog.revalidate()` comprueba que continúa
vigente mientras esa fase sigue abierta.

Para preparar antes de admitir, añade `--prepare-only` a `create`. La salida
identifica la candidata conservada; `--candidate NOMBRE` permite nombrarla.
Para revisar una fuente existente conservando su versión activa:

```sh
python3 kora_cli.py revise urn:ejemplo:skill:metodo --candidate ajuste
python3 kora_cli.py review urn:ejemplo:skill:metodo --candidate ajuste
python3 kora_cli.py admit urn:ejemplo:skill:metodo --candidate ajuste --reviewed SHA_REVISADO
```

Edita el cuerpo y los auxiliares de la candidata indicada por `revise`. `review`
informa su hash y los límites formales de cada destino. `admit` exige que esa
revisión y su base sigan vigentes; un error conserva la candidata y el diagnóstico.
Una realización válida no acredita la semántica ni la utilidad del procedimiento.
`--kind skill|agent|knowledge` permite desambiguar una candidata nueva en `review`.

La caché y el bytecode regenerables quedan fuera de la revisión publicada y no
bloquean las candidatas nuevas. Los archivos privados y temporales siguen
protegidos. Las candidatas anteriores con su huella antigua intacta son compatibles;
si cambió un residuo que aquella huella agregada no puede distinguir, conserva
el trabajo y prepara otra candidata desde la fuente vigente. Repetir la misma
revisión no repara una base de residuos incompatible.

Las revisiones completas de agentes y skills se conservan en
`versions/products/<namespace>/<name>/<hash>`, fuera del catálogo activo, con su
procedencia y recursos. `resolve URN --revision HASH` consulta esa revisión sin
reconstruirla desde Git. La huella distribuible sigue delimitando qué llega al
runtime. `create` rechaza una identidad o ubicación ocupada. Revisa también
ejemplos y plantillas cuando puedan reintroducir instrucciones corregidas.

`alias IDENTIDAD_ANTERIOR IDENTIDAD_CONSERVADA` mantiene una entrada alternativa
sin duplicar el producto. `retire URN --reason MOTIVO --replacement OTRA_URN`
conserva versiones y registra el motivo y la sustitución opcional. `--dry-run`
expone los consumidores afectados. El retiro archiva la fuente o referencia,
mantiene su identidad reservada y deja sus consumidores disponibles para
reconciliación explícita; no elimina sus instalaciones nativas. `remove`, en
cambio, actúa sobre los archivos administrados del home seleccionado.

## Instalar o actualizar

Con Codex o Hermes disponibles, instala KORA y sus skills necesarias en el
destino que uses:

```sh
python3 kora_cli.py install codex urn:kora:artefacto:kora
python3 kora_cli.py install hermes urn:kora:artefacto:kora
```

`install TARGET URN` valida las dependencias afectadas, realiza archivos nativos
y reconcilia la instalación. Sin URNs procesa todos los productos activos del
destino. Una actualización focal prepara el producto y sus dependencias
materiales. Lleva los recursos compartidos a sus copias administradas y ajusta
su propiedad, conservando el cuerpo y las demás dependencias pendientes de los
consumidores no seleccionados. Compartir una referencia de conocimiento no
amplía la selección. Cada destino se actualiza por separado.

Puedes examinar esa misma operación antes de aplicarla:

```sh
python3 kora_cli.py install codex urn:ejemplo:skill:metodo --home /tmp/kora-home --dry-run
python3 kora_cli.py remove codex urn:ejemplo:skill:metodo --home /tmp/kora-home --dry-run
```

La simulación no crea el home ni escribe estado. Su JSON muestra efectos por
archivo, cambios de propiedad, conflictos y precondiciones. Si guardas el JSON,
`--plan ARCHIVO` exige que siga vigente al aplicar. La aplicación recalcula bajo
lock y contrasta fuentes, recibos y destinos. Un cambio material exige preparar
de nuevo; la simulación no es autorización de publicación ni evidencia de carga.

Un cambio de nombre nativo o una revisión fijada incompatible puede requerir
seleccionar explícitamente los consumidores afectados. Si no se puede atribuir
un archivo anterior con certeza, la operación informa el conflicto. Los recibos
anteriores siguen siendo legibles; la procedencia por archivo se conserva al
realizar nuevas instalaciones.

`render TARGET URN --output DIRECTORIO_NUEVO` permite inspeccionar una salida sin
instalarla. Genera el producto y sus dependencias en un directorio inexistente,
con paths relativos al home. Codex recibe skills en `.agents/skills` y agentes
TOML en `.codex/agents`. Hermes recibe skills en `.hermes/skills` y agentes como
perfiles en `.hermes/profiles`. El conocimiento se lee por referencia estable.

Una skill puede instalarse en un perfil Hermes existente:

```sh
python3 kora_cli.py install hermes urn:kora:artefacto:instalacion-kora --profile dev
python3 kora_cli.py remove hermes urn:kora:artefacto:instalacion-kora --profile dev
```

Esa instancia se registra por separado y conserva SOUL, configuración y estado
del perfil. `--profile` admite solo skills. Si el perfil pertenece a un agente
KORA que administra esos mismos archivos, actualiza el agente por su identidad.
Si retiras una dependencia de un consumidor instalado solo en otro perfil,
actualiza ese consumidor para retirar su copia anterior; un nombre compartido
no acredita identidad. Consulta [Hermes](hermes.md) para abrir perfiles con su
proveedor y modelo explícitos; memoria, configuración y autenticación pertenecen
al operador.

La actualización compara bytes y permisos con lo instalado anteriormente. Ante
una edición local de un archivo que va a cambiar, consérvala o intégrala en la
fuente antes de actualizar. Un archivo sin efecto físico conserva su edición
local y el estado sigue mostrándola.
`--adopt archivo.json` permite adoptar archivos existentes mediante un mapa
revisado de paths relativos al home y SHA-256 actuales. La comparación de bytes
no acredita propiedad por sí sola ni autoriza sobrescribir trabajo ajeno.

## Trasladar, retirar y recuperar

Si cambian las rutas absolutas de la maquinaria o biblioteca, ejecuta desde la
nueva ubicación `install TARGET URN` para actualizar los consumidores que usas.
Para renovar conjuntos administrados, incluidos perfiles Hermes, selecciónalos
por las identidades que entrega `status`. Conserva `.local/state/kora` del home
para reconocer propiedad, ediciones y recuperación. En otro host, instala en su
home nuevo y configura el runtime allí.

```sh
python3 kora_cli.py status
python3 kora_cli.py recover
python3 kora_cli.py rollback
```

`status` reconoce diferencias y recuperación pendiente. `remove TARGET URN`
retira archivos propios intactos y conserva la fuente y las dependencias que
otro conjunto necesita. Memoria, credenciales, sesiones y archivos ajenos
permanecen. Retirar un agente o skill no retira sus referencias de conocimiento.

`status --compare-source` añade la comparación con las fuentes. Puedes acotarla
con `--target codex|hermes`, `--id URN` repetible y, para skills de Hermes,
`--profile NOMBRE`. Distingue fuente vigente, cambiada, ausente, retirada o no
realizable; dependencias pendientes; cambios nativos; y carga `not_observed`.
Una referencia de conocimiento viva puede cambiar de contenido sin alterar los
archivos nativos ni este estado. Para reproducir una evaluación, conserva las
revisiones realmente consultadas junto al caso y la configuración pertinente;
no hace falta fijar toda la biblioteca para el uso ordinario.
El estado ordinario y la recuperación funcionan aunque las fuentes no estén
disponibles. Comparar archivos no demuestra qué leyó una sesión del runtime.

`recover` atiende una instalación interrumpida. `rollback` intenta volver al
estado anterior de la última transacción y se detiene ante ediciones posteriores.
Estas operaciones no revierten publicaciones de conocimiento. Conserva los
cambios antes de reconciliar; no borres el estado privado para eludir conflictos.

El estado y las copias de recuperación viven en `.local/state/kora` del home
seleccionado, fuera de Git y en el mismo filesystem que los archivos gestionados.
`status` muestra en `preserved_changes` las escrituras posteriores detectadas en
archivos desplazados, con su ruta recuperable. Los respaldos no se eliminan
automáticamente.

Al retirar de la distribución un caché, bytecode o temporal anteriormente
administrado, una modificación se conserva como objeto recuperable con su hash
real y motivo. El recibo deja de distribuirlo; `status` conserva el localizador
y `rollback` puede restaurarlo. Esta excepción no adopta archivos privados como
`.env` ni elimina sus conflictos.

## Comprobar según el cambio

Comprueba lo que el cambio pretende conseguir. Una corrección editorial necesita
revisión del contenido y de su conservación donde se realiza. Un cambio de
conducta requiere observar un caso representativo y el límite relevante. Para
instalación, publicación o recuperación, prueba el mecanismo afectado y sus
condiciones de fallo.

```sh
python3 kora_cli.py check
python3 -m unittest discover -s tests -v
git diff --check
```

`check` diagnostica referencias y realizaciones del conjunto; devuelve su alcance
y lo no comprobado junto a `ok`. No revisa fidelidad, conducta, ventaja frente a
una instrucción breve ni todas las versiones históricas conservadas. Rechaza una
raíz inexistente; un directorio vacío existente es un catálogo vacío válido.
`check --history` añade la comprobación mecánica de todas las revisiones presentes
en `versions/products` de la maquinaria y `versions` de las bibliotecas leídas,
incluidas versiones anteriores, identidades retiradas y versiones sin referencia
vigente. Reutiliza las huellas y verificadores de revisión; informa cantidades
verificadas y defectos por ruta, también ante entradas malformadas o enlazadas.
No escribe ni repara la historia. Su alcance es lo conservado en disco: no acredita
que nunca se haya eliminado una versión, ni aprobación o fidelidad semántica.
Este recorrido solo ocurre al pedir `--history`; las consultas y el `check`
ordinario mantienen su alcance y costo habituales.
`--target codex` o
`--target hermes` acota el destino. Selecciona las pruebas pertinentes al cambiar
maquinaria; una operación ordinaria no requiere repetir la suite. Usa raíces
temporales con `--root` y `--knowledge-root`, y `--home DIRECTORIO_TEMPORAL` para
instalación, estado, retiro y recuperación fuera del home real.

El ensayo de independencia de la maquinaria usa una biblioteca explícita y un
montaje aislado con `bubblewrap`. Es una comprobación del sistema, no un paso de
cada instalación. Los contratos de [Codex](codex.md) y [Hermes](hermes.md)
contienen comprobaciones nativas y fuentes oficiales. Forma válida, fidelidad a
la fuente, aprobación, instalación coherente y conducta observada acreditan
propiedades distintas.

Los probes nativos separan descubrimiento de inferencia. `probe_codex.py` y
`probe_hermes.py` sin flags de inferencia comprueban capacidades del runtime;
`probe_independence.py --offline` prueba la copia aislada y los fixtures sin modelo.
Para observar recursos, un helper expresamente autorizado y actualización entre
sesiones, usa canarios sintéticos:

```sh
python3 scripts/probe_codex.py --canary --scenario resources --direct
python3 scripts/probe_codex.py --canary --scenario update
python3 scripts/probe_hermes.py --live --scenario resources
python3 scripts/probe_hermes.py --live --scenario update
```

`--model` y `--effort` identifican la configuración solicitada y el recibo muestra
la efectiva cuando el runtime la expone. Los homes y catálogos del ensayo son
temporales. El canario `incomplete` exige observar el resultado del hijo y el
cierre del padre; el perfil de prueba Hermes no expone delegación y rechaza ese
escenario antes de inferir. Una respuesta que imita el JSON esperado no acredita
un intercambio entre agentes.

El escenario `update` instala dos versiones contrastantes del rol y repite la
misma tarea en sesiones nuevas. La política de ordenamiento está solo en el rol:
la primera versión ordena de menor a mayor y la segunda de mayor a menor. El
prompt no revela esa política ni pide leer el archivo del rol. Codex usa su rol
personalizado mediante delegación; `--direct` activa una skill y no sirve para
esta comprobación de carga del rol. Hermes incorpora el SOUL mediante su
constructor nativo de prompt. Los recibos distinguen instalación, lectura de
conocimiento, instrucciones observadas en resultados de herramientas y conducta
contrastante. Los fixtures mecánicos sin inferencia solo comprueban fuentes y
realización; tampoco una respuesta que repite un marcador acredita carga nativa.
Este caso sintético no evalúa la utilidad de los productos reales.

La aceptación de maquinaria del 2026-09-13 comprobó este contraste en Codex
0.154.0 y Hermes con `gpt-6-astra` y esfuerzo `max`, además del traslado y los
recorridos mecánicos en raíces y homes temporales. La renovación y evaluación de
agentes, skills y conocimientos requiere el encargo posterior.
