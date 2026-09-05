# Antecedentes de Codex del 2026-09-05

Registro de preparación, adopción y comprobaciones ya realizadas. Los comandos
pertenecen a aquella etapa. El [contrato vigente](../../docs/codex.md) describe
la realización y las comprobaciones actuales.

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

## Instalación y conducta después del relevo

El 2026-09-05 se verificaron los 170 archivos administrados de Codex contra
el renderer de la raíz activa y sus recibos: bytes y modos coincidieron.
App Server descubrió las 72 skills administradas, sin errores; conservó las
doce preferencias de desactivación y mantuvo habilitada la entrada `$kora`.
La configuración existente permaneció intacta.

La apertura nativa de los 29 TOML instalados se observó mediante
[`strace`](https://strace.io/), versión instalada 6.8, restringida a los
syscalls de apertura y a esos 29 paths. El binario utiliza `open`, además
de las variantes que puede emplear su plataforma. No se capturaron buffers
ni paths de autenticación. Esta observación demuestra lectura por el proceso
nativo y ausencia de rechazo de formato; no invocación conductual de cada rol.

Una sesión nueva de App Server confirmó `gpt-6-astra` y esfuerzo `max`,
activó directamente `$kora` y ejecutó seis comandos de lectura exitosos.
Leyó la skill instalada, el README activo, resolvió las URNs de la guía y la
semántica operacional mediante `kora_cli.py` y leyó ambos conocimientos.
La respuesta conservó el criterio de originales recuperables y distinguió
`recover` de `rollback`, incluido el bloqueo ante ediciones posteriores.
No afirmó haber ejecutado una recuperación durante esa lectura.

El proceso utilizó un montaje externo de solo lectura para instalación, fuente
y autenticación, con estado efímero separado. Se omitió el sandbox interno
redundante de Codex porque este kernel rechazó crear otro namespace dentro del
montaje aislado. La protección observada corresponde al montaje externo.
No hubo escrituras en la fuente ni en la instalación, ni delegación; los 170
archivos, la configuración y la metadata de autenticación permanecieron
intactos. No quedó un turno vivo.

Esta evidencia corresponde a la KORA realmente instalada y al uso descrito.
Las pruebas de autoría, actualización, inferencia de ambos destinos y recuperación
están en [independencia](migracion.md#independencia-comprobada); los agentes de dominio
no reciben por extensión una validación conductual individual.
