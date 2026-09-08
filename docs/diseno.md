# Diseño de la maquinaria KORA

La maquinaria transforma recursos en conocimiento de referencia y realiza
agentes y skills en Codex y Hermes. La [guía operativa](operacion.md) contiene el
recorrido vigente. El conocimiento se conserva en una biblioteca independiente;
los agentes y skills declaran qué referencias necesitan leer.

## Archivos y responsabilidades

Archivos legibles y Git permiten revisar, recuperar y utilizar las fuentes
directamente. El catálogo se deriva al operar. No requiere un servicio, una base
de datos ni un registro manual. Los recursos técnicos conservan su formato.
`intake` guarda recursos de entrada y `create --source` conserva los originales
necesarios para reconstruir el fundamento de un producto.

`catalog.py` representa y resuelve; `authoring.py` conserva y crea fuentes;
`knowledge.py` recibe recursos, prepara borradores y publica referencias;
`render_codex.py` y `render_hermes.py` producen mapas de archivos nativos;
`install.py` reconoce cambios y recupera operaciones; `cli.py` conecta esos
recorridos. Los realizadores no modifican el home.

## Biblioteca de referencia

En h289, `/home/felix/kora-knowledge` contiene solo conocimiento y sus fuentes,
sin agentes, skills ni adaptadores. `inbox` recibe originales; `drafts` contiene
trabajo en preparación. `versions/<namespace>/<name>/<revision>` conserva cada
publicación y `references/<namespace>/<name>` apunta a la última disponible.
`archive/references` conserva referencias retiradas. Los alias preservan
identidades de consulta anteriores.

La koraficación requiere lectura, composición y comparación con las fuentes.
La CLI conserva archivos y verifica la publicación de la revisión examinada;
no hace aquella revisión semántica ni acredita por sí sola la aprobación de
Félix. `review` devuelve un hash del borrador y su revisión base. `approve` exige
ese hash para evitar publicar contenido distinto de lo revisado. El cambio de
referencia ocurre después de conservar la versión nueva: un borrador en curso
no reemplaza la referencia publicada.

`list` y `resolve` excluyen borradores. Una URN identifica el conocimiento; una
revisión identifica una versión exacta. Los consumidores nativos reciben rutas
estables de lectura: una publicación posterior queda disponible sin reinstalar
el agente o skill. Una consulta que necesite reproducir una respuesta puede
resolver la revisión exacta. Los conocimientos heredados permanecen disponibles
con estado `legacy`; su traslado no equivale a una aprobación nueva.

Las dependencias de conocimiento se resuelven dentro de la biblioteca. Los
vínculos documentales hacia un agente o skill conservan su sentido sin hacer
que la biblioteca dependa de su instalación. Git conserva historia de los
archivos; un commit no aprueba su contenido.

Los hashes nuevos usan los permisos portables de Git: archivo normal o
ejecutable. Los permisos locales de lectura y escritura no cambian la identidad
del contenido. Las versiones anteriores conservan sus hashes, archivos y rutas;
`legacy-modes.yaml` en la biblioteca registra los modos originales necesarios
para verificarlas después de una clonación. Ese registro conserva procedencia
inmutable de las versiones anteriores; las publicaciones nuevas no lo amplían.
Cambiar bytes, metadatos, nombres o ejecutabilidad sigue invalidando la revisión.

## Raíces y traslado

La raíz de maquinaria se deriva del programa invocado y se reemplaza con
`--root`. El enlace `knowledge -> ../kora-knowledge` da acceso directo a la
biblioteca; `--knowledge-root` permite elegir otra. Núcleo, métodos de operación,
agentes, skills y comprobaciones se mantienen en la maquinaria. La biblioteca es
una dependencia explícita de los consumidores que requieren conocimiento, y
puede consultarse sin el repositorio de agentes y skills.

Las realizaciones nativas señalan fuentes y referencias de esas raíces. Si
cambia su ubicación absoluta, se reinstalan los consumidores para actualizar las
rutas. El diario del instalador pertenece al home del operador y permanece allí
durante ese traslado. La guía explica cómo probar con raíces y home temporales.

Los instrumentos, instrucciones y resultados de la construcción concluida se
conservan en `archive/reconstruction`, fuera del núcleo y de la suite vigente.
Los originales reemplazados conservan su procedencia en `archive/previous`.
Los consumidores leen directamente `references/<namespace>/<name>` en la
biblioteca seleccionada. La capa histórica de enlaces de
`artefactos/conocimiento` fue retirada y no participa en la resolución ni en las
realizaciones. Las guías antiguas del corpus se conservan como antecedentes;
esta documentación y los métodos vigentes describen la operación actual.

El ensayo de independencia usa una copia de la maquinaria y una biblioteca
explícita en un montaje sin red, home personal ni archivo de reconstrucción.
Comprueba catálogo, instalación en ambos destinos, traslado y recuperación.
Requiere `bubblewrap` solo para ese ensayo. La variante con inferencia permite
observar también el trabajo de KORA con un proveedor disponible.

Una cita externa de un producto de dominio conserva su propia dependencia de
fuente. No se absorben bibliotecas, repositorios o archivos personales por estar
citados. Eso limita la comprobación de aquel producto cuando el original no está
disponible; la operación de la maquinaria no depende de leerlo.

## Actualización y recuperación

La CLI reúne las fuentes afectadas por la actualización y los consumidores
administrados que comparten sus archivos. Considera tanto los paths previamente
instalados como la realización actual: quitar una dependencia de la fuente no
borra su propiedad previa. Un producto ajeno a ese alcance se puede mantener por
separado.

El instalador guarda hashes y modos de sus archivos, detecta edición local y
conserva el estado ajeno. Prepara reemplazos y registra la intención antes de
intercambiar nombres. Conserva el inode desplazado para no perder escrituras
concurrentes, incluidas las hechas mediante un descriptor abierto. El diario
permite recuperar el conjunto a partir de esas identidades, aun si el proceso
termina entre el syscall y su registro posterior. Un renombre atómico no vuelve
atómica una instalación de varios archivos.

Se utiliza `renameat2` de Linux con `RENAME_NOREPLACE` para publicar nombres
nuevos y `RENAME_EXCHANGE` para conservar ambas entradas en una actualización.
Cada directorio padre se abre con `O_NOFOLLOW`, de modo que un enlace aparecido
durante la operación no desvíe la escritura. Destinos y estado privado deben
estar en el mismo filesystem; no hay fallback de sobrescritura. La autoría
serializa identidad y publicación por raíz mediante `flock`, sin otro registro.

Estas garantías protegen el trabajo local ante errores, interrupciones y agentes
concurrentes en el host de Félix. El retiro conserva memoria, credenciales,
sesiones y archivos ajenos. Recuperar una instalación no revierte una referencia
de conocimiento; para corregirla se prepara y publica una nueva revisión.

## Dependencias y contratos nativos

La biblioteca estándar de Python aporta filesystem, hashing, TOML y pruebas.
PyYAML lee y serializa YAML sin ejecutar objetos. El frontmatter generado se
vuelve a leer antes de instalar; las barras inversas no se escapan a mano.
Los requisitos para operar están en la guía. Los contratos específicos y su
contraste con los runtimes se documentan en [Codex](codex.md) y [Hermes](hermes.md).

Fuentes técnicas: [Linux renameat2](https://man7.org/linux/man-pages/man2/rename.2.html),
[Linux openat y O_NOFOLLOW](https://man7.org/linux/man-pages/man2/open.2.html),
[Python flock](https://docs.python.org/3.12/library/fcntl.html#fcntl.flock),
[PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation) y
[Agent Skills](https://agentskills.io/specification).
