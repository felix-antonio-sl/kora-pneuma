# Realización nativa en Codex

Investigación y pruebas: **2026-09-05**, **Codex CLI 0.153.4**. El adaptador se
implementa en `kora/render_codex.py`; `scripts/probe_codex.py` contrasta la
interfaz instalada con datos sintéticos y entrega salida saneada.

## Decisiones y contrato

Una skill se realiza en `.agents/skills/<name>/SKILL.md`, con frontmatter YAML
que contiene `name` y `description`. Sus archivos auxiliares conservan bytes,
rutas relativas y permisos. El cuerpo de origen permanece como prefijo exacto
del cuerpo realizado; se agrega una nota con identidad, fuente y dependencias.
La descripción se limita a 1024 caracteres en esta frontera nativa. Codex
descubre metadata primero y carga las instrucciones completas cuando usa la
skill. La invocación explícita en CLI usa `$<name>`; la elección implícita depende
del encargo y de la descripción. Estas decisiones siguen
[Build skills](https://learn.chatgpt.com/docs/build-skills) y la
[especificación Agent Skills](https://agentskills.io/specification), y se
comprueban con YAML real, recursos binarios y `skills/list`.

Un agente se realiza en `.codex/agents/<name>.toml`, con los tres campos nativos
`name`, `description` y `developer_instructions`. Las instrucciones contienen
el cuerpo íntegro de origen y el mismo mapa de recursos. **No requiere una
entrada en `config.toml`**: Codex descubre los archivos standalone. El campo
`name` define su identidad nativa, aunque el archivo puede llamarse distinto.
El renderer utiliza la convención de hacer coincidir ambos nombres. La fuente
oficial es [Custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents).

El mismo producto agente genera además `.agents/skills/<name>/SKILL.md` para
conservar la activación directa `$<name>` ya usada por el operador. Ambas formas
derivan de una sola fuente. La descripción de esta skill delimita la activación
directa y su cuerpo agrega una explicación precisa: carga perspectiva y conducta
en la sesión actual, sin crear otra sesión ni aplicar opciones de modelo o
sandbox del rol personalizado. No se crea otra identidad de producto ni una
política nueva de invocación implícita.

`render(catalog, product)` devuelve `dict[str, File]` con paths relativos al home
del operador y el cierre de dependencias realizables. Es una función pura: no
instala archivos ni modifica preferencias. `File` conserva bytes y modo. Toda
dependencia `requires` debe existir y admitir Codex cuando corresponda; una
colisión de realizaciones distintas detiene el render antes de sobrescribir.
El instalador común decide la escritura, la propiedad compartida de archivos,
la detección de cambios locales y la recuperación.

El conocimiento permanece en el catálogo fuente accesible en este host. Los
archivos realizados incluyen el mapa `identidad → ruta absoluta del contenido`;
la fuente agnóstica conserva identidades y dependencias. Codex no ofrece un
resolutor nativo de URNs KORA. Las rutas concretas son la realización de esa
relación y permiten que la lectura funcione con un catálogo temporal
independiente. Las referencias relativas del cuerpo se resuelven desde el
directorio de su archivo fuente. Los auxiliares de una skill también se copian
en su instalación; los auxiliares de un agente también se copian a su skill de
activación directa y permanecen accesibles junto a su fuente.

El adaptador no fija modelo, esfuerzo, sandbox ni credenciales por producto.
Los agentes heredan esas opciones del entorno salvo configuración nativa
explícita. El archivo de un agente admite opciones de sesión, pero los overrides
efectivos y la precedencia dependen del runtime. Un texto de instrucciones o una
dependencia declarada no constituye un control de permisos. Véanse
[Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) y
[Configuration Reference](https://learn.chatgpt.com/docs/config-file/config-reference).

## Descubrimiento e invocación

| Superficie | Comportamiento pertinente |
| --- | --- |
| `$HOME/.agents/skills` | Descubrimiento personal de skills; ruta de instalación elegida. |
| `.agents/skills` del repositorio | Descubrimiento desde el directorio actual hasta su raíz Git; útil para pruebas aisladas y productos de un proyecto. |
| `$CODEX_HOME/skills` | Ruta de compatibilidad todavía observada en 0.153.4; no se usa para instalaciones nuevas KORA. |
| `$CODEX_HOME/agents/*.toml` | Descubrimiento personal de agentes standalone; no requiere registros por agente. |
| `.codex/agents/*.toml` del repositorio | Agentes locales del proyecto cuando este es confiable; superficie usada por el canario sintético. |
| `skills/list` con `forceReload: true` | Vuelve a leer skills y reporta paths, scope, habilitación y errores; no prueba su ejecución. |
| `spawn_agent` con el tipo nativo | Selecciona el agente personalizado y aplica su configuración a la sesión hija. |
| `$<agente>` con la skill generada | Activa la conducta en la sesión actual; no aplica la configuración de un rol nuevo. |

La CLI instalada no anuncia `--agent`; `codex agents` y `/agent` administran
sesiones. `thread/start` tampoco expone `agentType` en su esquema generado.
Por ello la realización ofrece **un rol nativo para delegación y una skill para
activación directa**. Pedir un nombre en lenguaje natural no prueba que se cargó
el archivo del rol. La API admite `developerInstructions` al iniciar una sesión,
pero implementar otro lanzador no es necesario para el recorrido actual. Las
interfaces se contrastan con [Codex App Server](https://learn.chatgpt.com/docs/app-server)
y la ayuda de la CLI instalada.

Codex mantiene su cadena de instrucciones globales y de proyecto. KORA no
reescribe `AGENTS.md` global para seleccionar cada producto. La cadena se
describe en [Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

## Diferencias comprobadas entre documentación e instalación

La entrada inicial [developers.openai.com/codex](https://developers.openai.com/codex/)
redirigía a [ChatGPT Learn](https://learn.chatgpt.com/docs/) en la fecha de
investigación. Se siguieron las páginas oficiales y se exportaron los esquemas
del binario instalado; la web por sí sola no define su capacidad efectiva.

- `model/list` devuelve `gpt-6-astra` con `low`, `medium`, `high`, `xhigh`, `max`
  y `ultra`. Una sesión efímera iniciada sin inferencia confirma modelo
  `gpt-6-astra` y esfuerzo `max`. La página
  [GPT-6 Astra](https://developers.openai.com/api/docs/models/gpt-6-astra)
  también documenta `max`; el catálogo local no prueba disponibilidad de cuenta.
- El `sandbox` de `thread/start` acepta `read-only`, `workspace-write` y
  `danger-full-access`. El valor `readOnly` fue rechazado por el runtime. Deben
  usarse los enums de su esquema, aunque un ejemplo web use otra forma.
- La página de App Server anuncia `perCwdExtraUserRoots` en `skills/list`;
  el esquema generado de 0.153.4 no contiene ese parámetro. El adaptador no
  depende de él.
- `agents/openai.yaml` sí proporciona metadata de interfaz a `skills/list`.
  En una prueba sintética, `SKILL.json` por sí solo no la proporcionó; con ambos
  archivos prevaleció `agents/openai.yaml`. Esto difiere de la mención de
  `SKILL.json` en la página y en comentarios del esquema. El renderer conserva
  auxiliares existentes y no crea un segundo formato de metadata.
- Un `CODEX_HOME` temporal aísla configuración, agentes y estado de Codex,
  pero **no elimina el descubrimiento de `$HOME/.agents/skills`**. El canario
  deshabilita esas rutas por overrides de la invocación y comprueba que no
  aparecen en el contexto inicial. No modifica su habilitación persistida.
- Los agentes del proyecto requieren confianza del proyecto. Un TOML sintético
  mal formado bajo `.codex/agents` fue ignorado sin diagnóstico cuando el
  proyecto no era confiable; al declarar `projects.<path>.trust_level="trusted"`
  se observó su lectura y rechazo por el loader. La confianza del canario se
  declara únicamente como override de esa invocación.

## Comprobaciones reproducibles

Desde la raíz del repositorio:

```sh
python3 -m unittest discover -s tests -p 'test_render_codex.py' -v
python3 scripts/probe_codex.py
python3 scripts/probe_codex.py --inventory
python3 scripts/probe_codex.py --canary
python3 scripts/probe_codex.py --canary --direct
```

Las nueve pruebas del renderer comprueban YAML con caracteres especiales, cuerpo
conservado, auxiliares binarios y ejecutables, TOML nativo, cierre transitivo,
referencias ausentes, colisiones, límite de descripción y wrapper directo con
sus auxiliares. Utilizan solamente
catálogos temporales nuevos.

El probe predeterminado crea un repositorio y un `CODEX_HOME` temporales, exporta
esquemas del binario, inicia App Server por stdio, ejecuta `model/list`,
`skills/list` y `thread/start` efímero, y termina el proceso. Un archivo de agente
sintético mal formado produce el diagnóstico observable del loader standalone
sin registro global; otro compara el loader del proyecto con y sin confianza.
También contrasta los formatos opcionales de metadata. Este probe **no envía
un turno al modelo**. Sus recursos
temporales se eliminan al terminar.

`--inventory` inspecciona las tres superficies personales y emite solamente
nombres, hashes, tamaños, enlaces, overrides de habilitación y marcadores de
relación con KORA. Un marcador `KORA` o una URN acredita relación textual, no
propiedad para reemplazar o retirar un archivo. El inventario se calcula del
filesystem actual; no es un registro mantenido a mano ni incluye cuerpos,
historiales o configuración completa.

`--canary` **consume inferencia real**. Requiere autenticación local existente,
vinculada solo dentro de un `CODEX_HOME` temporal; el probe no lee ni muestra
su contenido. Genera conocimiento, skill y agente desde un catálogo sintético
nuevo, realiza sus archivos, comprueba el contexto inicial y ejecuta
`codex exec --ephemeral` con `gpt-6-astra`, esfuerzo `max`, sandbox `read-only`
y aprobación `never`. Los flags globales `-a`, `-s` y `-m` preceden a `exec`.
El proyecto temporal se declara confiable mediante un override CLI, necesario
para descubrir su agente local.

El recorrido conductual exige una delegación real al tipo personalizado, lectura
de la skill y de su fuente, conservación de la excepción de lluvia, estado
`diferida` y distancia `UNKNOWN`. Tres marcas distintas están presentes solo en
las instrucciones del agente, la skill y el conocimiento, respectivamente.
El reporte saneado distingue la delegación observada de los valores devueltos.
En 0.153.4 la salida JSON de `exec` entregó el evento nativo de espera del
subagente; no entregó un evento separado llamado `spawn_agent`. El canario
reporta esa evidencia sin inventar el evento ausente.

Con `--direct`, el prompt solicita `$kora-canary-witness` en la sesión principal.
Se comprueban el mismo resultado y las marcas de las fuentes, junto con la
ausencia de eventos de delegación. Ambos canarios comprueban antes la detección
nativa de la skill requerida y la skill de activación del agente. Estas muestras
acreditan esos recorridos; no demuestran equivalencia conductual de todo el corpus.

El **2026-09-05** terminaron **PASS** las nueve pruebas del renderer, el probe
sin inferencia y ambos canarios reales con `gpt-6-astra` y esfuerzo `max`.
El canario de rol produjo los eventos de espera del subagente; el directo
produjo lecturas en la sesión principal y ningún evento de colaboración.
Ambos devolvieron `diferida`, conservaron la excepción de lluvia y `UNKNOWN`, y
reprodujeron las tres marcas presentes solo en sus fuentes. Los procesos
terminaron con código cero y sus directorios temporales se eliminaron.

Los canarios deben correrse sobre la realización que se quiera acreditar.
La prueba conductual aquí corresponde a productos sintéticos independientes;
la inspección de instalaciones KORA existentes fue de solo lectura.

## Preparación de la adopción

```sh
python3 scripts/plan_codex_adoption.py --legacy-root /ruta/al/repositorio-legado-preservado
```

El planificador inspecciona `.agents/skills`, `.codex/skills` y `.codex/agents`
y compara sus archivos con el renderer actual y con productos y emisiones de
los repositorios anteriores. Los orígenes se indican explícitamente repitiendo
`--legacy-root`; deben existir y ser distintos del catálogo activo. Esta utilidad
sirve para preparar una migración desde un árbol preservado. El mantenimiento
normal utiliza `install`, `status`, `recover` y `rollback`.
`--root` y `--home` permiten comprobar el recorrido
en un entorno temporal. No modifica instalaciones, configuración ni fuentes.

Cada ejecución crea `._local/codex-adoption-<fecha>/plan.json`, en un directorio
privado con modo `0700`. Sus archivos tienen modo `0600`. La captura conserva
los bytes completos de los archivos inspeccionados en blobs SHA256, sus modos,
los directorios y los destinos de enlaces sin seguirlos. También conserva las
fuentes concretas usadas para acreditar propiedad. Los bytes de configuración,
credenciales, historial y skills de sistema quedan fuera de esta captura; solo
se registran el hash de configuración y las preferencias pertinentes.

La atribución admite coincidencia exacta con el renderer, el manifiesto del
instalador, una emisión anterior o un `_BUILD/codex`. Cuando una emisión está
adelantada respecto de la instalación, busca en Git la fuente cuyo SHA256
coincide con el sello instalado y comprueba el archivo nativo completo después
de sustituir exclusivamente cuerpo, versión, hash y descripción de esa fuente.
Una fecha de generación diferente se registra como tal. Los marcadores o URNs
por sí solos no autorizan la adopción; una diferencia no demostrada permanece
ambigua. No se ejecuta el núcleo anterior para producir esta evidencia.

El JSON contiene los archivos esperados y sus consumidores, `adopt` como mapa
`path → SHA256` compatible con `Installer.apply(..., adopt=digests)`, propuestas
de retiro con hashes y pruebas, archivos ambiguos y preferencias que conservar.
El retiro requiere verificar primero la preservación y el sucesor funcional
o archivo inactivo correspondiente. Una skill directa y el TOML del mismo
agente son superficies complementarias; las skills de igual nombre en raíces
diferentes se informan por separado. Los auxiliares no heredan propiedad solo
por estar dentro de un directorio KORA.

Dos capturas detectan cambios de bytes, modos, archivos agregados o eliminados
y enlaces durante la inspección. También se verifica que el catálogo no cambie
entre render y atribución. Si falla esa estabilidad, el resultado no habilita
adopción ni retiro y el comando termina con código distinto de cero. Antes de
aplicar un plan, el instalador vuelve a contrastar los hashes revisados.

Las entradas `skills.config` desactivadas se conservan incluso si su ruta ya
no existe. El plan no habilita automáticamente un sucesor. Los archivos
`agents/openai.yaml` generados por un emisor anterior se atribuyen mediante sus
bytes; su política anterior no se convierte por inferencia en una preferencia
nueva del operador.

## Complemento desde consumidores legacy

El **2026-09-05** se recuperaron **21 objetos adicionales** desde productos de
`kora`: cinco funciones que permanecían activas en `.codex/skills`, cinco
documentos requeridos por ellas y once funciones desactivadas. Este complemento
se distingue de los 530 objetos procedentes de `kora-pneuma` mediante
`provenance.source_repository: kora`, `source_path: artifacts/...` y
`migration: legacy-codex-consumers-2026-09-05`. No reutiliza su núcleo ni su ley.

Las cinco funciones conservan sus identidades y se realizan únicamente para
Codex, que es su consumo comprobado. Los agentes OPM y UX recuperados generan
rol nativo y skill directa desde una sola fuente. Los originales completos
quedan en `sources/original.md`, con hash y cabecera en procedencia; ese nombre
evita que el descubridor interprete un segundo `SKILL.md` anidado. Los cinco
documentos conservan íntegros sus bytes en `content.md`. Las once funciones
desactivadas permanecen en `archive/products` con sus originales y recursos
en `archive/previous/legacy-codex`; no generan una realización activa.

Las adaptaciones se registran junto a cada producto: resolución actual del
corpus OPM y sustitución de la sección de despliegue antigua de
`lineas-paralelas`; URL de desarrollo explícita en la plantilla de
`test-vivo-iterativo-opmkv`; referencia IFML actual con mapa de procedencia;
y traslado de las instrucciones funcionales de las cabeceras de los agentes
OPM y UX a sus cuerpos. Vector, arnés y configuración de otros runtimes
permanecen en la fuente preservada. El conocimiento de dominio no se reformatea.

La comprobación del complemento contrasta los 21 originales por SHA256,
resuelve sus dependencias y valida YAML/TOML nativos. App Server descubrió en
un proyecto temporal las diez skills de su cierre, incluidos los dos wrappers
de agente, sin errores. La sesión efímera confirmó `gpt-6-astra` y `max`; esta
comprobación no envió un turno al modelo. Una prueba temporal del
planificador verifica que un auxiliar sin origen se conserva, que un enlace
no se sigue, que una preferencia disabled permanece y que la configuración
ajena no se filtra al plan. Estas comprobaciones no sustituyen la revisión de
la adopción real ni acreditan conducta de todo el corpus.
