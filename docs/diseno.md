# Maquinaria personal KORA

Decisiones de construcción del 2026-09-05. El alcance y el término están en
[MANDATO.md](../MANDATO.md); este documento explica las decisiones que consume el
código. La implementación se comprueba por recorridos, no por cantidad de fichas.

## Fuente y uso

Cada producto vive en `products/<namespace>/<name>/`. `object.yaml` relaciona su
`id` estable, `kind` (`knowledge`, `skill` o `agent`), `name`, `description` y
`content` con un archivo legible. `targets` contiene únicamente los destinos que
se realizan. `requires` enumera dependencias necesarias; `relations` conserva
otros vínculos tipados sin convertir una cita histórica en una instalación.
`provenance` guarda procedencia y fuentes recuperables. Los recursos técnicos
conservan su formato y no se convierten automáticamente en prosa.

Un catálogo se deriva del filesystem al operar. No hay registro manual paralelo.
La identidad debe ser única; un nombre solo colisiona si dos realizaciones
intentan ocupar el mismo destino físico. Las referencias activas se resuelven
antes de producir archivos. Una ficha no acredita fidelidad semántica.

La alternativa de conservar los frontmatter anteriores como contrato operativo
arrastraría su ontología y sus adaptadores. La alternativa de una base de datos
agregaría estado mutable sin un consumidor que lo necesite. Archivos y Git
permiten revisar, recuperar y utilizar el corpus directamente.

## Realización e instalación

Los realizadores puros producen archivos nativos de Codex y Hermes con sus modos.
El catálogo y la instalación no importan el núcleo ni la ley anteriores. Las
dependencias de conocimiento se exponen con rutas comprobadas y resolución por
identidad; no se promete que un modelo lea o atienda todo el contenido.

El instalador opera únicamente los paths del plan y sus archivos previamente
gestionados. Guarda hashes de lo instalado, detecta edición local y conserva el
estado ajeno. Prepara archivos antes de reemplazar y registra la intención antes
de un intercambio atómico de nombres. Conserva el inode desplazado para no
perder escrituras concurrentes, incluidas las hechas mediante un descriptor ya
abierto. El diario permite recuperar el conjunto a partir de las identidades de
los inodes, aun si el proceso termina entre el syscall y su registro posterior.
La atomicidad de un renombre no vuelve atómica una instalación de varios
archivos. El retiro mueve solo archivos propios intactos a recuperación y
conserva memoria, credenciales, sesiones y archivos ajenos.

La implementación utiliza `renameat2` de Linux con `RENAME_NOREPLACE` para
publicar nombres nuevos y `RENAME_EXCHANGE` para conservar ambas entradas en
una actualización. Abre cada directorio padre con `O_NOFOLLOW`, de modo que un
enlace aparecido durante la operación no desvíe la escritura. Los destinos y el
estado privado requieren el mismo filesystem. No existe fallback de
sobrescritura. La autoría serializa la comprobación de identidad y publicación
por raíz mediante `flock`, sin añadir un registro separado.

Python instalado: 3.12.3. PyYAML instalado: 6.0.1. La biblioteca estándar aporta
filesystem, hashing, TOML y pruebas; PyYAML lee y serializa YAML sin ejecutar
objetos. Se serializa el frontmatter mediante la biblioteca y se vuelve a leer
antes de instalar: las barras inversas no se escapan a mano. Fuentes consultadas:
[Linux renameat2](https://man7.org/linux/man-pages/man2/rename.2.html),
[Linux openat y O_NOFOLLOW](https://man7.org/linux/man-pages/man2/open.2.html),
[Python flock](https://docs.python.org/3.12/library/fcntl.html#fcntl.flock),
[PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation) y
[Agent Skills](https://agentskills.io/specification).

Los contratos específicos y el contraste con las versiones instaladas se
documentan junto a cada destino: [Codex](codex.md) y [Hermes](hermes.md).

## Orden de realización y pruebas

1. Preservar el repositorio vivo, incluidos Git, archivos sin seguimiento y
   cambios locales. El respaldo privado se coteja por bytes y enlaces; el relevo
   vuelve a comprobar que la base no se haya movido.
2. Construir catálogo, autoría y resolución; probar procedencia, conservación de
   recursos, identidad y referencias faltantes en raíces temporales.
3. Realizar skill y agente en ambos destinos; probar lectura por parsers nativos,
   nombres en destinos disjuntos, recursos y descubrimiento efectivo.
4. Instalar, actualizar, detectar divergencia, retirar y recuperar ante fallos
   de escritura e interrupción; comprobar el contenido observable y el estado
   ajeno después de cada recorrido.
5. Importar todo el corpus conservable y reconstruir productos de maquinaria;
   cotejar contenido, vínculos y procedencia contra la base. Las excepciones
   concretas quedan en [migración](migracion.md), con fuente recuperable.
6. Ejecutar koraficación y autoría desde fuentes nuevas sin acceso al núcleo
   anterior, y observar canarios reales de los dos runtimes.
7. Efectuar el relevo local preservando la historia, actualizar consumidores,
   verificar instalaciones y recuperación, y cerrar commits semánticos. Solo
   entonces la raíz de construcción deja de ser autoridad activa.

Responsabilidades de código: `catalog.py` representa y resuelve; `authoring.py`
crea fuentes; `render_codex.py` y `render_hermes.py` realizan; `install.py`
reconcilia y recupera; `migrate.py` entiende exclusivamente la entrada anterior;
`cli.py` ofrece el recorrido operable. Las pruebas viven con estos límites.

## Independencia comprobada

El 2026-09-05 `scripts/probe_independence.py` ejecutó la KORA reconstruida en
Codex `gpt-6-astra`, esfuerzo `max`, dentro de un namespace de montajes que
ocultó `/home` y `/tmp`. Solo quedaron disponibles la copia nueva, el binario
nativo y la autenticación montada en lectura. El núcleo anterior, su ley y el
repositorio de construcción no fueron accesibles. Se utilizó
[bubblewrap](https://github.com/containers/bubblewrap#usage), versión instalada
0.9.0; el aislamiento corresponde a ese proceso, sin cambiar los montajes del host.

La KORA invocada mediante su skill nativa creó conocimiento desde un manual
ficticio, conservó su original, autoró un skill y un agente agnósticos y los
instaló en ambos destinos. Una sesión nueva resolvió cinco casos. Después se
cambió el umbral de masa del manual de 12 a 15 kg: la KORA conservó las dos
versiones, actualizó los productos y sus instalaciones, y otra sesión cambió
solo la decisión correspondiente a la pieza de 13 kg. Se conservaron la
prioridad del permiso revocado, la excepción de lluvia y `UNKNOWN` para los
datos ausentes. Los archivos instalados coincidieron con ambas realizaciones
y el estado del instalador quedó limpio.

Hermes ejecutó el mismo agente y corpus actualizado en otro montaje aislado,
con runtime y autenticación en lectura. Su loop nativo realizó seis llamadas
API con `openai-codex/gpt-6-astra`, esfuerzo `max`, cargó el skill y leyó el
conocimiento completo. El JSON de los cinco casos coincidió con el oracle
separado del prompt. La prueba ofreció solo herramientas de lectura; utilizó
la ruta resuelta del mapa nativo y no ejecutó la alternativa CLI `resolve`.

Las pruebas de instalación y recuperación por interrupción también pasaron en
el entorno sin núcleo anterior. Esta evidencia cubre el recorrido descrito;
no acredita por extensión la conducta de todos los productos de dominio.
Los recibos y logs sintéticos se conservan en el respaldo privado, sin material
de autenticación. Los originales migrados tienen su cotejo independiente en
[migración](migracion.md).
