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

## Autoría de agentes y skills

Usa `autoria-kora` para preparar la conducta y las capacidades necesarias.
`create skill` y `create agent` reciben namespace, nombre, `--id`, `--description`
y `--body`, con la misma forma del ejemplo anterior. Publican la fuente en
`products/<namespace>/<name>` de la maquinaria. Los cuerpos no llevan un segundo
frontmatter. Codex y Hermes son los destinos por defecto; `--target` permite
restringirlos.

`requires` declara skills necesarias y conocimientos publicados que deben poder
consultarse. `relations` conserva vínculos documentales que no implican
instalación. Los conocimientos permanecen en la biblioteca; no se copian dentro
del agente o skill. Conserva junto al cuerpo los scripts, ejemplos y otros
recursos propios que necesite el procedimiento.

Para actualizar un agente o skill, resuelve su identidad y edita esa fuente,
preservando cambios concurrentes y su versión anterior en Git. `create` rechaza
una identidad o ubicación ocupada. Revisa también ejemplos y plantillas cuando
puedan reintroducir instrucciones que acabas de corregir.

## Instalar o actualizar

Con Codex o Hermes disponibles, instala KORA y sus skills necesarias en el
destino que uses:

```sh
python3 kora_cli.py install codex urn:kora:artefacto:kora
python3 kora_cli.py install hermes urn:kora:artefacto:kora
```

`install TARGET URN` valida las dependencias afectadas, realiza archivos nativos
y reconcilia la instalación. Sin URNs procesa todos los productos activos del
destino. Una actualización focal incluye consumidores administrados que
comparten archivos o dependencias afectadas, considerando instalación previa y
fuente actual. Cada destino se actualiza por separado.

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
una edición local, consérvala o intégrala en la fuente antes de actualizar.
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

`recover` atiende una instalación interrumpida. `rollback` intenta volver al
estado anterior de la última transacción y se detiene ante ediciones posteriores.
Estas operaciones no revierten publicaciones de conocimiento. Conserva los
cambios antes de reconciliar; no borres el estado privado para eludir conflictos.

El estado y las copias de recuperación viven en `.local/state/kora` del home
seleccionado, fuera de Git y en el mismo filesystem que los archivos gestionados.
`status` muestra en `preserved_changes` las escrituras posteriores detectadas en
archivos desplazados, con su ruta recuperable. Los respaldos no se eliminan
automáticamente.

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

`check` diagnostica referencias y realizaciones del conjunto; `--target codex` o
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
