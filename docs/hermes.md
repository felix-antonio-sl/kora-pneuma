# Realización de KORA en Hermes

Decisiones contrastadas el **2026-09-05** con documentación oficial web y la
instalación local. Hermes declara **0.21.0**, fecha de release **2026.8.31**;
el checkout efectivo está limpio en
`9dd6634c5635321cf38840cc30e9b51226689128`, commit del **2026-09-05**. La fecha
de release y la del commit identifican cosas distintas.

Los enlaces permanentes siguientes conservan el corte `79445a49` usado durante
la reconstrucción. Al destilar la maquinaria, `python3 scripts/probe_hermes.py`
repitió en `9dd6634c` las diez observaciones offline de contexto, descubrimiento
y actualización, todas conformes. Esas pruebas no actualizan Hermes ni acreditan
por sí solas una nueva inferencia.

## Traducción que opera en este host

Una skill se realiza como `$HERMES_HOME/skills/<name>/SKILL.md` con sus recursos.
Un agente se realiza como perfil: `SOUL.md`, `distribution.yaml` y las skills
requeridas, bajo `~/.hermes/profiles/<name>/`. Sus recursos propios conservan
bytes, modos y estructura relativa bajo `resources/`, sin ocupar paths de
configuración personal. El renderer puro está en
[`render_hermes.py`](../kora/render_hermes.py). Devuelve bytes y modos de archivos;
el instalador KORA aplica y recupera los cambios.

| Intención fuente | Realización | Consecuencia y límite |
| --- | --- | --- |
| Identidad, propósito y conducta estable del agente | Cuerpo en `SOUL.md` | Se carga desde `HERMES_HOME`, después de escaneo y sujeto al presupuesto de contexto. Su forma no impone una frontera de herramientas ni acredita conducta. |
| Procedimiento reutilizable | Bundle con frontmatter nativo `name`, `description`, metadata de procedencia y cuerpo conservado | Hermes puede descubrirlo y cargarlo mediante `skill_view`; no se presupone que el modelo lo invocará. |
| Conocimiento requerido | Mapa de identificador a ruta absoluta de su contenido fuente | La fuente sigue siendo única y recuperable en el mismo host. Su lectura requiere una herramienta de archivos; `skill_view` solo sirve archivos internos del bundle. |
| Skills requeridas transitivamente | Bundles concretos dentro del perfil o de la raíz de skills | Se comprueba la clausura antes de emitir. Dos identidades que comparten nombre nativo producen un error. |
| Relación con otro agente | Relación fuente o texto de colaboración | `requires` de un agente produce error explícito: un perfil no realiza una invocación de otro perfil por declararla. |
| Modelos, proveedores y preferencias del operador | Configuración efectiva local de Hermes | El renderer no genera ni sobreescribe `config.yaml`, `.env` o `auth.json`. |

La documentación separa personalidad persistente y contexto de proyecto. El
código instalado confirma `SOUL.md` como identidad del perfil y la cadena de
`AGENTS.md` desde la raíz Git al directorio de trabajo; por directorio gana
`AGENTS.override.md` sobre `AGENTS.md`. Un `.hermes.md` encontrado tiene prioridad
sobre esa cadena. Por eso no se emite un `AGENTS.md` dentro del perfil esperando
que gobierne cualquier proyecto. La skill especialista instalada describía una
búsqueda anterior; esta decisión usa el código vigente.
Fuentes: [personalidad](https://hermes-agent.nousresearch.com/docs/user-guide/features/personality),
[contextos](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files),
[implementación contrastada](https://github.com/NousResearch/hermes-agent/blob/79445a496c86a19332ad786494b8384d2167e2d0/agent/prompt_builder.py#L1433).

El frontmatter mínimo respeta `name` y `description`; la procedencia va en
`metadata.kora_id` y `metadata.kora_source`, ambos strings. Recursos binarios y
modos ejecutables se conservan. No se convierte una lista declarativa de
herramientas en una promesa de enforcement.
Fuentes: [Agent Skills](https://agentskills.io/specification),
[skills de Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills).

## Entrada nativa y tamaño efectivo de SOUL

Los perfiles nuevos `fugaz` y `agent-architect` funcionan sin que KORA genere un
`config.yaml`. La entrada nativa comprobada para la ruta de este operador es:

```sh
hermes --profile fugaz chat --provider openai-codex --model gpt-6-astra --reasoning max
hermes --profile agent-architect chat --provider openai-codex --model gpt-6-astra --reasoning max
```

El directorio del perfil basta para seleccionarlo. El modelo y proveedor son
opciones de esa invocación. La configuración raíz **no se hereda** como un
`config.yaml` del perfil; los defaults y el archivo del perfil siguen siendo sus
fuentes de configuración. La autenticación tiene una regla distinta: el resolver
nativo busca primero el proveedor local y después el del `auth.json` raíz. Los
OAuth compartidos no se deben copiar; su refresh pertenece al store de origen.
Fuentes: [perfiles y OAuth compartido](https://hermes-agent.nousresearch.com/docs/user-guide/profiles/),
[opciones de invocación](https://hermes-agent.nousresearch.com/docs/reference/cli-commands),
[selección de perfil](https://github.com/NousResearch/hermes-agent/blob/79445a496c86a19332ad786494b8384d2167e2d0/hermes_cli/profiles.py#L1680),
[fallback de credenciales](https://github.com/NousResearch/hermes-agent/blob/79445a496c86a19332ad786494b8384d2167e2d0/hermes_cli/auth.py#L740).

El ensayo reproducible usa fuentes y token **sintéticos**, bloquea la red y
ejecuta `hermes --profile NAME prompt-size --json`, el parser CLI y la resolución
de credenciales del CLI instalado. Ambos perfiles seleccionaron su propio SOUL,
resolvieron la ruta explícita y el token raíz; ninguno creó configuración ni auth
local, y los archivos raíz conservaron sus bytes. Esto acredita entrada y
resolución offline, sin afirmar una nueva inferencia con esos agentes:

```sh
python3 scripts/probe_hermes.py --profile-entrypoints
```

Se comprobó también el contenido que llega al prompt, además de conservar el
archivo emitido. Con `openai-codex/gpt-6-astra`, el código instalado reconoce una
ventana de **1.050.000 tokens** y deriva un cap de **252.000 caracteres** por
archivo de contexto. Los cuatro perfiles KORA existentes declaran esa ruta y no
fijan `context_file_max_chars`. Los dos perfiles nuevos se abren con las opciones
anteriores. En seis realizaciones temporales del catálogo actual, `load_soul_md`
y el bloque estable del prompt conservaron el SOUL y su mapa completos:

| Agente | Caracteres cargables del SOUL, sin espacio exterior | Cuerpo y mapa íntegros con la ruta actual |
| --- | ---: | --- |
| `agent-architect` | 4.323 | Sí |
| `director-tecnico-hodom` | 23.699 | Sí |
| `dov-dori` | 64.231 | Sí |
| `fugaz` | 11.029 | Sí |
| `kora` | 4.828 | Sí |
| `steipete` | 10.868 | Sí |

El límite varía con la invocación. En un perfil temporal **sin modelo**, el
inspector `prompt-size` usa una ventana de 256.000 y cap de 61.440: recorta el
centro de Dov Dori, aunque conserva completo su mapa final. La llamada de bajo
nivel `load_soul_md()` **sin informar ventana** usa 20.000: recorta Dov Dori y
Director Técnico HODOM, y ambos mapas quedan incompletos. Este último caso no
representa el arranque configurado observado. Cuando hay recorte, el comando
instalado puede anteponer un aviso al JSON incluso en modo quiet; el probe lo
contempla. Su salida distingue los tres escenarios:

```sh
python3 scripts/probe_hermes.py --soul-budgets --catalog-root .
```

El renderer conserva el cuerpo y el mapa como están: no se reproduce pérdida en
la ruta actual. Si cambia modelo o presupuesto, se vuelve a medir; una pérdida
reproducida exige ajustar el cap nativo del operador o una entrada breve que
mande leer las instrucciones completas, antes de afirmar equivalencia. Hermes
aplica 70 % de cabecera y 20 % de cola, con un aviso que indica cómo recuperar el
archivo completo. La documentación vigente describe el cap dinámico, aunque una
tabla secundaria de configuración todavía llama a 20.000 el default. Fuentes:
[contexto y recorte](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files),
[configuración del cap](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/#context-file-truncation),
[cálculo instalado](https://github.com/NousResearch/hermes-agent/blob/79445a496c86a19332ad786494b8384d2167e2d0/agent/prompt_builder.py#L1006),
[inserción en el prompt](https://github.com/NousResearch/hermes-agent/blob/79445a496c86a19332ad786494b8384d2167e2d0/agent/system_prompt.py#L488).

## Descubrimiento efectivo y mantenimiento

El scanner recorre skills del perfil y sigue enlaces a directorios. Excluye
`.archive` y los recursos de soporte dentro de un bundle. Las skills de proyecto
requieren confianza del repositorio. Las externas se agregan mediante
`skills.external_dirs`; configurar una raíz compartida requiere revisar los
homónimos presentes en cada perfil. Las skills externas pueden ser modificadas
por `skill_manage`; una ruta externa no es una protección de escritura.

Hay un límite observable de la precedencia publicada: el listado deduplica por
nombre siguiendo proyecto, local y externo, pero `skill_view` rechaza un nombre
compartido entre local y externo. Solo la prioridad de proyecto elimina los
candidatos de otros niveles. El probe reproduce esa diferencia con dos skills
sintéticas. La instalación debe comprobar tanto discovery como carga efectiva;
un nombre visible en el índice puede fallar al cargar.
Fuentes: [directorios y precedencia](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills#external-skill-directories),
[scanner](https://github.com/NousResearch/hermes-agent/blob/79445a496c86a19332ad786494b8384d2167e2d0/agent/skill_utils.py#L736),
[resolución de colisiones](https://github.com/NousResearch/hermes-agent/blob/79445a496c86a19332ad786494b8384d2167e2d0/tools/skills_tool.py#L466).

El manifiesto emitido enumera **archivos exactos** en `distribution_owned`,
incluyendo `SOUL.md`, `distribution.yaml` y los archivos de cada skill. No declara
propiedad de `skills/` completo. No registra una fuente para `hermes profile update`:
el mantenimiento pertenece al instalador KORA y a sus recibos.

La distribución nativa sigue siendo un formato útil, pero su actualización tiene
consecuencias distintas de las exigidas aquí:

| Comportamiento nativo comprobado con archivos sintéticos | Decisión KORA |
| --- | --- |
| Sin `distribution_owned`, copia cualquier archivo de la fuente salvo exclusiones; supera la lista corta presentada en la tabla documental | Emitir propiedad explícita. |
| Un directorio declarado se elimina y copia de nuevo; una edición y un archivo agregado localmente dentro de él se pierden | Preflight de cambios locales y aplicación por archivo con recuperación. |
| Un archivo cuyo path desaparece del nuevo manifiesto puede permanecer instalado | Calcular también los retiros desde el recibo anterior. |
| Configuración y memoria conservan sus bytes en el update normal | Mantener ese estado fuera de propiedad KORA y verificarlo. |
| Rechaza cualquier symlink dentro de una distribución fuente | Emitir bundles de archivos regulares; referenciar conocimiento por su path canónico. |
| `hermes profile delete` retira también credenciales, memoria y sesiones | Retirar solamente los archivos KORA acreditados; conservar el perfil y su estado ajeno. |

Estas decisiones usan el comportamiento instalado, aunque la documentación
resuma defaults más estrechos. Fuente documental:
[distribuciones](https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions),
[comandos de perfiles](https://hermes-agent.nousresearch.com/docs/reference/profile-commands).
Fuente ejecutada:
[`profile_distribution.py`](https://github.com/NousResearch/hermes-agent/blob/79445a496c86a19332ad786494b8384d2167e2d0/hermes_cli/profile_distribution.py#L335).

Un perfil delimita estado Hermes; no aisla por sí solo el filesystem del host.
El arranque de herramientas depende también de `terminal.cwd` y del backend.
La configuración administrada, si existe, fija sus claves sobre las del usuario.
La realización no altera estas decisiones locales.
Fuentes: [perfiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles),
[configuración](https://hermes-agent.nousresearch.com/docs/user-guide/configuration),
[managed scope](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope).

## Consumidores encontrados antes del relevo

Este es un corte inicial **2026-09-05**, útil para preparar la migración; el
filesystem se vuelve a consultar antes de alterar un consumidor. La siguiente
tabla identifica solo contenido con procedencia KORA. No atribuye a KORA las
otras skills, identidad o configuración de los perfiles mixtos.

| Raíz bajo `~/.hermes` | Identidad KORA | Skills KORA activas observadas |
| --- | --- | --- |
| `skills/` | — | `auditoria-exposicion-kora`, `conducir-decisiones-hodom`, `hermes-agent-specialist`, `hospitalizacion-domiciliaria`, `modelamiento-opm`, `ship-discipline` |
| `profiles/dev/` | — | Las mismas seis de la raíz default |
| `profiles/director-tecnico-hodom/` | `urn:salud:artefacto:director-tecnico-hodom` | `conducir-decisiones-hodom`, `hospitalizacion-domiciliaria` |
| `profiles/dov-dori/` | `urn:fxsl:artefacto:dov-dori` | `modelamiento-opm` |
| `profiles/kora/` | `urn:kora:artefacto:kora` | `util-x` |
| `profiles/steipete/` | `urn:dev:artefacto:steipete` | `ship-discipline`, `util-x` |
| `profiles/hodom-dt/`, `profiles/hospitalista/`, `profiles/telemedicina/`, `profiles/urgencia/` | — | En cada perfil: `hermes-agent-specialist`, `ship-discipline` |

Los cuatro manifiestos de agentes carecen de `source`; `hermes profile update`
no tiene un origen registrado para ellos. `util-x` aparece fuera de las listas
de propiedad de sus perfiles; su nombre no autoriza descartarlo. La raíz default
y `dev` también conservan una versión de `hermes-agent-specialist` en `.archive`,
excluida del discovery. El inventario reproducible no lee `.env`, `auth.json`,
memoria ni sesiones:

```sh
python3 scripts/probe_hermes.py --inventory
```

La preparación de adopción compara **bytes y modos** de cada archivo con
`_emision/hermes` anterior. Para versiones rezagadas identifica el contenido
fuente por el hash del sello en Git y exige igualdad del archivo instalado
completo, incluyendo wrapper y modo. No ejecuta el núcleo antiguo. El script
produce solo un JSON privado bajo `._local/`, con modo `0600`, hashes, paths y
conteos de estado ajeno; no registra sus cuerpos:

```sh
python3 scripts/plan_hermes_adoption.py --legacy-root /ruta/al/repositorio-legado-preservado
```

El origen legado debe indicarse explícitamente y ser distinto del catálogo
activo. Esta utilidad prepara una migración; el mantenimiento normal utiliza
`install`, `status`, `recover` y `rollback`.

El corte de preparación dio **96 archivos adoptables, 4 candidatos a retiro,
0 ambiguos, 26 bundles y 13 archivos nuevos**. Las cuatro versiones antiguas
identificadas exactamente son SOUL Steipete `1.6.0`, Modelamiento OPM `3.0.0`,
Hermes Specialist `2.3.0` y Ship Discipline `1.2.0`. El plan guarda el commit y
hash fuente que justifican cada igualdad. En perfiles mixtos, cada bundle
declara el producto del catálogo nuevo y el prefijo del perfil actual: permite
actualizar sus skills in situ conservando personalidad, configuración y estado.
Incluye también los perfiles nuevos `fugaz` y `agent-architect` y la clausura de
skills de los seis agentes. Estos conteos se regeneran tras cambios de fuente;
constituyen un plan, no un recibo de instalación.

Los candidatos a retiro son dos copias de un script de auditoría que ya no
pertenece al bundle reconstruido y dos copias de `util-x`. Para este último se
acreditó la función: sus metadatos, cuerpo y sello coinciden con la skill
sintética definida en `tests/test_kora.py:29-44` del producto anterior. No existe
como producto activo ni está declarado en los manifiestos de sus perfiles. El
evento que lo instaló **no está acreditado**; no se revisaron conversaciones
personales para atribuirlo. El plan registra sus hashes como candidatos y no
borra archivos. Las skills en `.archive` y el resto del estado ajeno permanecen
fuera de adopción y retiro.

## Evidencia y canario

Los siguientes comandos se ejecutaron con éxito sobre esta instalación:

```sh
python3 -m unittest discover -s tests -p 'test_render_hermes.py' -v
python3 scripts/probe_hermes.py
```

La primera ejecución pasó seis pruebas, incluida la lectura de los archivos
emitidos con los parsers nativos. La segunda reprodujo diez observaciones de
contexto, discovery y actualización. Usa un `HERMES_HOME` temporal, archivos
sintéticos y bloqueo de red dentro del proceso; no llama un modelo.
`hermes prompt-size --json` puede medir el prompt construido y también opera
offline; no demuestra inferencia. Fuente:
[prompt-size](https://hermes-agent.nousresearch.com/docs/reference/cli-commands#hermes-prompt-size).

La medición del CLI no es de solo lectura: en un perfil temporal nuevo creó
base de estado, lock de autenticación, logs, cachés, snapshot de skills y
directorios. Su handler tomó el modelo de `config.yaml` e ignoró las opciones
globales de modelo en ese recorrido. Por eso la comprobación final de perfiles
utiliza las funciones nativas de construcción de prompt y carga de skills en
una vista temporal, con entradas instaladas montadas en lectura, red bloqueada
y credencial dummy. No inicia conversación ni lee autenticación, memoria o
sesiones personales. El control negativo de un SOUL recortado falla como debe.

El enrutamiento no secreto observado en los perfiles es
`openai-codex` / `gpt-6-astra`; los fallos históricos de `commandcode` no describen
esta ruta actual. La presencia de autenticación local no prueba que el proveedor
acepte una petición. Hermes guarda OAuth propio y puede importar o refrescar
credenciales en sus rutas de resolución. Fuentes:
[proveedores](https://hermes-agent.nousresearch.com/docs/integrations/providers/),
[secretos](https://hermes-agent.nousresearch.com/docs/user-guide/secrets),
[resolver instalado](https://github.com/NousResearch/hermes-agent/blob/79445a496c86a19332ad786494b8384d2167e2d0/hermes_cli/auth_codex.py#L379).

El canario real se prepara como ejecución explícita separada: fuente sintética
con condición, excepción y dato desconocido; skill y agente emitidos por KORA;
`HERMES_HOME` y directorio de trabajo temporales; sesión nueva sin memoria
personal. Se permite leer un access token existente dentro del proceso y pasarlo
a `AIAgent` con `api_key` **y** `base_url` explícitos, `quiet_mode=True`,
`skip_memory=True`, `skip_background_review=True` y `save_trajectories=False`.
No se copia auth a la fuente ni a evidencia. Se exige un token no próximo a
expirar, sin invocar el resolver que puede refrescarlo. El canario exige carga de
skill, lectura de conocimiento y resultado fiel; una frase de identidad es
insuficiente. Se ejecuta explícitamente con:

```sh
python3 scripts/probe_hermes.py --live
```

La ejecución **2026-09-05** terminó con código `0`: `openai-codex`,
`gpt-6-astra`, esfuerzo `max`, tres llamadas API registradas por el loop nativo.
Antes de inferir, comprobó que el esquema incluyera únicamente `skills_list`,
`skill_view` y `read_file`. Las respuestas de herramientas acreditaron la carga
del procedimiento emitido y la lectura de la norma sintética desde su fuente.
El resultado fue exactamente:

| Caso sintético | Condición probada | Resultado observado |
| --- | --- | --- |
| A | Sello vigente y cuatro piezas, sin fragilidad | `PREPARADA` |
| B | Cumple la regla general, pero es frágil | `RETENIDA` |
| C | Cantidad de piezas desconocida | `INDETERMINADA` |
| D | Sello vencido | `NO_PREPARADA` |

El canario comprobó que el access token no apareciera en ningún archivo temporal;
el directorio temporal se eliminó al finalizar. Esta evidencia acredita ese
recorrido real del agente y los dos accesos a conocimiento. No demuestra
equivalencia general de agentes, aceptación de un caso de dominio ni conducta
de todas las identidades instaladas. No se retuvo un payload del transporte ni
se inspeccionaron conversaciones personales.

El probe admite además un catálogo temporal producido por la KORA reconstruida,
sin volver a fabricar el canario anterior. El evaluador recibe la respuesta
esperada por un archivo separado que **no se agrega al prompt**:

```sh
python3 scripts/probe_hermes.py --live \
  --catalog-root /ruta/al/catalogo-temporal \
  --agent-id urn:probe:artefacto:inspector-envios \
  --prompt-file /ruta/a/pregunta-sintetica.txt \
  --expected-file /ruta/a/respuesta-esperada.json
```

`--source` y `--auth-store` permiten señalar los mounts autorizados de una prueba
aislada. La respuesta debe coincidir con el **JSON completo**, y las respuestas
de `skill_view` y `read_file` deben contener los cuerpos de una skill requerida
y un conocimiento requerido. El ensayo offline del adaptador ejecutó ambas
herramientas nativas, comprobó que la pregunta llegara sin alteración y rechazó
una respuesta que omitía una clave; la frontera de inferencia fue sustituida
solo en ese ensayo. La ejecución con un catálogo externo requiere `--live`
explícito; esta ampliación y su ensayo offline no acreditan otra inferencia.

El 2026-09-05 el catálogo externo creado y actualizado por la KORA nueva pasó
además **la inferencia real de independencia**. El runtime, la autenticación y
los productos estaban montados en lectura; los repositorios anteriores y el de
construcción eran inaccesibles. Con seis llamadas API, `gpt-6-astra` y esfuerzo
`max`, Hermes cargó `evaluar-envios`, leyó la fuente vigente y devolvió el JSON
completo esperado: `AUTORIZADA`, `DIFERIDA`, `UNKNOWN`, `AUTORIZADA`, `DENEGADA`
para los casos A–E, distancia `UNKNOWN` y versión `PZ_6139_V2`.

El oracle no formó parte del prompt. Los productos y la metadata del auth
permanecieron intactos y no se persistió material de credenciales. La prueba
dispuso solo de herramientas de lectura: leyó el conocimiento por el mapa de
rutas nativo, sin ejecutar el comando `resolve` que la skill también ofrece.
Los pasos de autoría, actualización e instalación de ese mismo corpus, y su
alcance probatorio, están en [independencia](migracion.md#independencia-comprobada).

## Instalación comprobada después del relevo

El 2026-09-05 se actualizaron las realizaciones desde la raíz activa
`/home/felix/kora-pneuma`. Hermes quedó con 37 bundles administrados, incluidas
las instancias de skills en perfiles mixtos. La adopción y el retiro se hicieron
por archivos de propiedad acreditada, conservando los originales desplazados.
Las seis ubicaciones manuales de maquinaria se sustituyeron por sus funciones
vigentes según la [revisión de migración](migracion.md#consumidores-manuales-de-hermes).

La comprobación final leyó los perfiles instalados `agent-architect`,
`director-tecnico-hodom`, `dov-dori`, `fugaz`, `kora` y `steipete` en una vista
temporal de solo lectura, con red bloqueada. Los archivos coincidieron con el
renderer activo en bytes y modos; los seis SOUL y sus mapas completos llegaron
al prompt nativo con `openai-codex/gpt-6-astra`, esfuerzo `max` y ventana
reconocida de 1.050.000 tokens. Las once instancias de skills requeridas se
descubrieron y `skill_view(preprocess=False)` devolvió sus cuerpos completos.

El comprobador registró cero intentos de leer autenticación, memoria o sesiones
personales. Esta revisión no inició conversación; la inferencia real corresponde
al recorrido independiente descrito arriba. Sus recibos privados permanecen bajo
`._local`; no forman un inventario manual de mantenimiento.

El mantenimiento general instaló después las tres skills declaradas que aún
faltaban en la raíz: `auditoria-artefactos-kora`, `autoria-de-persona` y
`mente-omega`. Se comprobaron sus nueve archivos, incluidos los seis recursos
de mente omega, contra fuente y recibos. Las tres pasaron el parser, discovery
y `skill_view` nativos en una vista de solo lectura, sin autenticación personal
ni conversación. El registro final contiene 19 bundles Hermes de raíz y agentes,
más 18 instancias en perfiles mixtos. Repetir la instalación conserva tanto
los archivos como el diario del último rollback.
