# Operar KORA

Ubica la raíz a partir de la fuente resuelta: sube desde este archivo hasta el
directorio que contiene `kora_cli.py` y `README.md`. Ejecuta allí los comandos
siguientes. Así la guía sigue siendo válida al trasladar el repositorio.
`--root` se coloca antes del subcomando para seleccionar otro corpus; la raíz
por defecto es la del programa invocado.

## Encontrar y leer

```sh
python3 kora_cli.py --help
python3 kora_cli.py list --kind knowledge
python3 kora_cli.py list --kind skill --target codex
python3 kora_cli.py list --archived
python3 kora_cli.py resolve urn:kora:kb:frontera-fuentes-tecnicas
```

`resolve` devuelve `path` y `active`. Lee el archivo indicado antes de usar su
contenido. Un alias lleva a la misma identidad conservada; que un objeto
archivado resuelva no lo habilita para instalación.

## Crear o corregir una fuente

`create` publica un cuerpo ya autorado. No hace la síntesis ni comprueba por sí
solo la fidelidad de una koraficación. Consulta sus argumentos efectivos:

```sh
python3 kora_cli.py create --help
```

Selecciona `knowledge`, `skill` o `agent`; proporciona namespace, nombre,
identidad, descripción y `--body`. Repite `--source` para conservar originales
apropiados dentro del producto y `--requires` para dependencias necesarias.
Agentes y skills usan Codex y Hermes por defecto; `--target` restringe esa
selección. Sus cuerpos no llevan un segundo frontmatter.

Para corregir un objeto existente, resuélvelo y edita su `content` o su
`object.yaml`. Conserva el original que sustenta la corrección y sus límites.
`create` rechaza una identidad o ubicación ocupada; no sirve para sobrescribirla.

## Comprobar, realizar y actualizar

```sh
python3 kora_cli.py check --target codex
python3 kora_cli.py render --help
python3 kora_cli.py install --help
python3 kora_cli.py status
```

`check` informa problemas de referencias y realización. Para revisar un producto
concreto, `render TARGET URN --output DIRECTORIO_NUEVO` produce sus archivos y
dependencias en un directorio inexistente. Usa `codex` o `hermes` como `TARGET`
y los valores reales del objeto y la salida. Inspecciona el resultado; después
`install TARGET URN` lo instala o actualiza. Sin URNs, `install` selecciona todos
los productos activos del destino.

Las actualizaciones incluyen sus consumidores ya administrados en ese mismo
destino. Para mantener una skill dentro de un perfil Hermes existente usa
`install hermes URN --profile NOMBRE`. Su instancia queda registrada, conserva
la personalidad y el estado del perfil, y se retira con el mismo `--profile`.
El flag solo admite skills; la raíz Hermes se opera sin él.

Usa `--home DIRECTORIO_TEMPORAL` en instalación, estado, retiro y recuperación
para probar sin tocar el home real. Un archivo instalado que cambió localmente
detiene la actualización: conserva el cambio y reconcílialo con la fuente.
`--adopt` recibe un mapa JSON revisado de paths y hashes para adoptar archivos
existentes; no evita esa revisión.

## Retirar o recuperar

```sh
python3 kora_cli.py remove --help
python3 kora_cli.py recover
python3 kora_cli.py rollback
```

`remove TARGET URN` retira la instalación propia intacta; la fuente permanece.
Las dependencias compartidas siguen mientras otro conjunto instalado las
necesite. `recover` atiende una transacción interrumpida; `rollback` intenta
volver al estado anterior de la última transacción confirmada y se detiene ante
ediciones posteriores. Conserva esas ediciones antes de reconciliar. No borres
el estado de recuperación para eludir un conflicto.

La [semántica de operaciones](../cat-kora-semantica-operacional/content.md)
explica efectos y límites. Los detalles de realización y descubrimiento están
junto a sus adaptadores: [Codex](../../../docs/codex.md) y
[Hermes](../../../docs/hermes.md). El [README](../../../README.md) indica las
pruebas disponibles. Un comando correcto no acredita por sí solo lectura
efectiva del conocimiento ni conducta del agente.

[Guía anterior conservada](../../../archive/previous/kora/guia-rapida-pneuma/content.md).
