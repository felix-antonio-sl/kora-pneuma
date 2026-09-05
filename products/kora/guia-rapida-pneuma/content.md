# Operar KORA

Esta es la guía operativa de la maquinaria. Ubica la raíz desde este archivo:
sube hasta el directorio que contiene `kora_cli.py` y `README.md`, y ejecuta allí
los comandos siguientes. `--root` se coloca antes del subcomando para seleccionar
otro corpus; por defecto se usa la raíz del programa invocado.

El núcleo requiere Linux con `renameat2`, Python 3.12 y PyYAML 6.0.1; la
dependencia Python está en [requirements.txt](../../../requirements.txt).
Los comandos entregan JSON y un código distinto de cero ante un conflicto.
`python3 kora_cli.py COMANDO --help` muestra los argumentos disponibles.

## Encontrar y mantener fuentes

```sh
python3 kora_cli.py list --kind knowledge
python3 kora_cli.py list --kind skill --target codex
python3 kora_cli.py list --archived
python3 kora_cli.py resolve urn:kora:kb:frontera-fuentes-tecnicas
```

`resolve` devuelve `path` y `active`. Lee el archivo indicado antes de usar su
contenido. Un alias lleva a la misma identidad conservada; resolver un objeto
archivado no lo habilita para instalación.

`create` publica un cuerpo ya autorado y conserva los originales indicados con
`--source`. La síntesis y la comprobación de fidelidad forman parte de la autoría.
Ejemplo con rutas de entrada que debes proporcionar:

```sh
python3 kora_cli.py create knowledge personal tema --id urn:personal:kb:tema \
  --description 'Alcance y condiciones de la fuente' \
  --body /ruta/al/conocimiento.md --source /ruta/a/la/fuente.pdf
```

Selecciona `knowledge`, `skill` o `agent`. Repite `--source` para conservar otros
originales y `--requires` para dependencias necesarias. Agentes y skills usan
Codex y Hermes por defecto; `--target` restringe esa selección. Sus cuerpos no
llevan un segundo frontmatter. El [modelo de fuente](../cat-kora-kernel/content.md)
explica campos, recursos y relaciones.

Para corregir un objeto existente, resuélvelo y edita su contenido, recursos o
`object.yaml`, conservando los originales pertinentes. `create` rechaza una
identidad o ubicación ocupada. Las fuentes técnicas mantienen su formato cuando
lo necesitan; la [frontera de fuentes](../frontera-fuentes-tecnicas/content.md)
orienta esa decisión.

## Instalar o actualizar

`install` valida las dependencias afectadas, realiza los archivos nativos y
reconcilia la instalación. Puedes usarlo directamente para el destino autorizado:

```sh
python3 kora_cli.py install codex urn:kora:artefacto:autoria-kora
```

Usa `hermes` para ese destino. Sin URNs, `install TARGET` procesa todos sus
productos activos. Una actualización focal incluye los consumidores administrados
que comparten archivos o dependencias afectadas, considerando su instalación
previa y la fuente actual. El otro destino se actualiza por separado. Si retiras
una dependencia de un consumidor instalado solo en otro perfil, actualiza ese
consumidor para retirar su copia anterior: el nombre de una skill por sí solo
no acredita identidad entre perfiles.

Cuando necesites inspeccionar archivos antes de instalarlos,
`render TARGET URN --output DIRECTORIO_NUEVO` los produce junto con sus
dependencias en una salida inexistente. Sus paths son relativos al home.

Codex recibe skills en `.agents/skills` y agentes TOML en `.codex/agents`.
Hermes recibe skills en `.hermes/skills` y agentes como perfiles en
`.hermes/profiles`. El conocimiento se lee desde su fuente resuelta.

Una skill también puede mantenerse dentro de un perfil Hermes existente:

```sh
python3 kora_cli.py install hermes urn:kora:artefacto:instalacion-kora --profile dev
python3 kora_cli.py remove hermes urn:kora:artefacto:instalacion-kora --profile dev
```

Esa instancia se registra por separado y conserva el SOUL, la configuración y el
estado del perfil. `--profile` admite solo skills; la raíz Hermes se opera sin él.
Si el perfil pertenece a un agente KORA que también administra esos archivos,
actualiza el agente por su identidad para mantener su conjunto coherente.
Los perfiles de agentes nuevos se abren con opciones nativas explícitas, por
ejemplo `hermes --profile kora chat --provider openai-codex --model gpt-6-astra --reasoning max`.
Hermes puede compartir el auth raíz; no hereda su configuración.

La actualización compara bytes y permisos con lo instalado anteriormente. Una
edición local detiene la operación para conservarla y reconciliarla en la fuente.
`--adopt archivo.json` permite adoptar archivos existentes mediante un mapa de
paths y SHA-256 cuya propiedad se haya revisado. Conserva el alcance acreditado;
la adopción no fuerza el borrado ni el reemplazo de cambios ajenos.

## Consultar estado, retirar y recuperar

```sh
python3 kora_cli.py status
python3 kora_cli.py recover
python3 kora_cli.py rollback
```

Usa `status` para reconocer diferencias materiales o recuperación pendiente.
`remove TARGET URN` retira archivos propios intactos; conserva la fuente y las
dependencias que otro conjunto instalado necesita. Los directorios, memoria,
credenciales, sesiones y archivos ajenos permanecen.

`recover` atiende una transacción interrumpida. `rollback` intenta volver al
estado anterior de la última transacción confirmada y se detiene ante ediciones
posteriores. Conserva esas ediciones antes de reconciliar; no borres el estado
privado para eludir un conflicto.

El estado y las copias de recuperación viven en `.local/state/kora` del home
seleccionado, fuera de Git y en el mismo filesystem que los archivos gestionados.
`status` muestra como `preserved_changes` las escrituras posteriores detectadas
en archivos desplazados, con su ruta recuperable. Los respaldos se retienen sin
eliminación automática. La [semántica de operaciones](../cat-kora-semantica-operacional/content.md)
explica los límites de atomicidad y recuperación.

## Comprobar según el cambio

La comprobación responde a lo que cambió y a la afirmación que necesitas sostener.
En una corrección editorial basta revisar el contenido y, si corresponde, su
conservación en la realización. Un cambio que pretende modificar conducta requiere
observar un caso representativo y el límite relevante. Para instalación o
recuperación, ejercita el mecanismo afectado y sus condiciones de fallo.

`check` sirve para diagnosticar referencias y realizaciones del conjunto; admite
`--target codex` o `--target hermes` para acotar el destino. Las pruebas del núcleo
se ejecutan desde la raíz:

```sh
python3 kora_cli.py check
python3 -m unittest discover -s tests -v
git diff --check
```

Selecciona las pruebas pertinentes al cambiar maquinaria; la suite completa
sirve para cambios transversales. Usa un corpus temporal con `--root` y
`--home DIRECTORIO_TEMPORAL` en instalación, estado, retiro y recuperación para
ensayar fuera del home real. Una operación ordinaria no requiere repetir toda
la suite ni la auditoría histórica de migración.

Los contratos de [Codex](../../../docs/codex.md) y
[Hermes](../../../docs/hermes.md) contienen sus comprobaciones nativas y fuentes
oficiales. Un archivo válido, una instalación coherente y una conducta observada
acreditan propiedades distintas; el [contrato de autoría](../cat-contrato-ingenieria-agentica/content.md)
ayuda a elegir la evidencia necesaria.

[Guía anterior conservada](../../../archive/previous/kora/guia-rapida-pneuma/content.md).
