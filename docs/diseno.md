# Diseño de la maquinaria KORA

La maquinaria relaciona fuentes autoradas con archivos utilizables en Codex y
Hermes. El [modelo de fuente](../products/kora/cat-kora-kernel/content.md)
define productos, identidad y dependencias; la
[guía operativa](../products/kora/guia-rapida-pneuma/content.md) explica su uso.
La construcción y sus comprobaciones del 2026-09-05 se conservan en
[migración](migracion.md).

## Archivos y responsabilidades

Archivos legibles y Git permiten revisar, recuperar y utilizar el corpus
directamente. El catálogo se deriva al operar: una base de datos o un registro
manual agregarían estado mutable sin una necesidad actual. Los recursos técnicos
conservan su formato. La importación interpreta formas anteriores en su límite
de entrada, sin trasladarlas al contrato operativo.

`catalog.py` representa y resuelve; `authoring.py` conserva y publica fuentes;
`render_codex.py` y `render_hermes.py` producen mapas de archivos nativos;
`install.py` reconoce cambios y recupera operaciones; `cli.py` conecta esos
recorridos. `migrate.py` y su auditoría sirven para importar y estudiar originales.
Los realizadores no modifican el home y el núcleo operativo no importa código
de la maquinaria anterior.

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
sesiones y archivos ajenos. Los límites de lo comprobable están en la
[semántica de operaciones](../products/kora/cat-kora-semantica-operacional/content.md).

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
