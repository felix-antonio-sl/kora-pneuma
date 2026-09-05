# KORA

Maquinaria personal de Félix Korvo para convertir fuentes en conocimiento útil,
autorar agentes y skills agnósticos, y realizarlos en **Codex y Hermes**.

Esta es la única raíz de uso de KORA. Contiene el núcleo independiente y el
corpus migrado bajo el [mandato autorizado](MANDATO.md). La historia Git anterior
y el trabajo local previo se conservan. `/home/felix/kora-rebuild` registra la
construcción de origen; las actualizaciones se realizan aquí.

## Operación

En Codex, `$kora` activa KORA en la conversación actual. Los agentes también
disponen de su rol nativo para delegación explícita. En Hermes, abre el perfil
`kora` con el comando indicado más abajo. La CLI permite las mismas operaciones
de archivos y mantenimiento sin depender de una conversación.

Requiere Linux con `renameat2`, Python 3.12 y PyYAML 6.0.1, presentes en este host.
La dependencia Python está en `requirements.txt`. Desde cualquier directorio:

```sh
python3 /home/felix/kora-pneuma/kora_cli.py --help
python3 /home/felix/kora-pneuma/kora_cli.py list
python3 /home/felix/kora-pneuma/kora_cli.py check
```

Los comandos entregan JSON y retornan código distinto de cero ante un conflicto.
`--root` permite trabajar un corpus independiente. `resolve URN` devuelve el
archivo que debe leerse y señala si la identidad está activa o archivada.

Cada producto vive en `products/<namespace>/<name>/object.yaml` y mantiene su
cuerpo en el archivo indicado por `content`. Los campos necesarios son `id`,
`kind`, `name`, `description` y `content`; agentes y skills declaran `targets`.
`requires` contiene dependencias necesarias que deben existir y realizarse en el
destino elegido. `relations` conserva otros vínculos sin instalarlos.

`create` recibe un cuerpo ya autorado y conserva originales indicados con
`--source`. No inventa una síntesis ni acredita su fidelidad por copiarla. Ejemplo
con rutas de entrada que el autor debe proporcionar:

```sh
python3 kora_cli.py create knowledge personal tema --id urn:personal:kb:tema \
  --description 'Alcance y condiciones de la fuente' \
  --body /ruta/al/conocimiento.md --source /ruta/a/la/fuente.pdf
```

El mismo comando con `skill` o `agent` crea una fuente agnóstica. Por defecto se
realiza en Codex y Hermes; `--target codex` o `--target hermes` restringe esa
decisión. `--requires URN` puede repetirse. Los cuerpos de skills y agentes no
llevan un segundo frontmatter.

## Realización, instalación y recuperación

`render` produce archivos nativos en un directorio nuevo y comprueba dependencias
antes de escribir. Sus paths son relativos al home del operador. `install`
instala o actualiza los identificadores solicitados; sin identificadores procesa
todos los productos activos del destino. También actualiza los consumidores ya
administrados que comparten dependencias afectadas, incluidas las instancias de
skills en perfiles Hermes. No modifica el otro destino implícitamente.

```sh
python3 kora_cli.py render codex --output /ruta/nueva/realizacion
python3 kora_cli.py install codex
python3 kora_cli.py install hermes
python3 kora_cli.py status
python3 kora_cli.py recover
python3 kora_cli.py rollback
```

`--home /ruta/temporal` permite probar instalación y recuperación sin tocar el
home real. Codex recibe skills en `.agents/skills` y agentes TOML en
`.codex/agents`. Hermes recibe skills en `.hermes/skills` y perfiles en
`.hermes/profiles`. El conocimiento se lee desde rutas resueltas del catálogo.

Para mantener una skill en un perfil Hermes existente, usa su identidad y el
nombre del perfil. Esa instancia se registra por separado y conserva el SOUL,
la configuración y el estado del perfil:

```sh
python3 kora_cli.py install hermes urn:kora:artefacto:instalacion-kora --profile dev
python3 kora_cli.py remove hermes urn:kora:artefacto:instalacion-kora --profile dev
```

`--profile` admite solo skills de Hermes; la raíz usa el comando sin ese flag.
Un agente Hermes recibe su propio perfil. Los perfiles nuevos se pueden abrir
con opciones nativas explícitas, por ejemplo
`hermes --profile kora chat --provider openai-codex --model gpt-6-astra --reasoning max`.
Hermes puede utilizar el auth raíz compartido; no hereda la configuración raíz.

La actualización compara bytes y permisos con lo previamente instalado. Un
cambio local detiene la operación para conservarlo y reconciliarlo en la fuente.
`--adopt archivo.json` sirve para relevar archivos existentes cuya propiedad y
SHA-256 se hayan revisado; no es un modo de forzar el borrado.

`remove codex URN` o `remove hermes URN` retira archivos propios intactos y
conserva dependencias aún compartidas. Los directorios, memoria, credenciales,
sesiones y archivos ajenos permanecen. `recover` resuelve una transacción
interrumpida; `rollback` deshace la última instalación confirmada, conservando
cualquier edición local posterior.

El estado y las copias de recuperación viven en `~/.local/state/kora`, fuera de
Git y en el mismo filesystem que los archivos administrados. El instalador
rechaza otro filesystem antes de cambiar archivos vivos. El diario permite
recuperar el conjunto; un lector concurrente puede observar un estado intermedio
entre renombres de archivos.

Los intercambios conservan el archivo efectivamente desplazado, incluso si otro
proceso continúa escribiéndolo por un descriptor abierto. `status` muestra esas
variaciones como `preserved_changes`, con la ruta recuperable. Los objetos
desplazados se retienen; no hay eliminación automática de respaldos. La
recuperación ensayada cubre interrupciones de procesos, sin afirmar resistencia
a fallas físicas de almacenamiento.

## Comprobación y continuidad

```sh
python3 -m unittest discover -s tests -v
git diff --check
```

Las pruebas incluyen el recorrido CLI desde fuente nueva hasta ambos destinos,
actualización y rollback, además de fallo de escritura y término abrupto de un
proceso. Se complementan con parsers, descubrimiento e inferencia de los runtimes;
ninguno de esos planos por sí solo prueba el mandato completo.

- [Instrucciones de ejecución](AGENTS.md).
- [Decisiones de diseño y orden de realización](docs/diseno.md).
- [Contrato efectivo de Codex](docs/codex.md).
- [Contrato efectivo de Hermes](docs/hermes.md).
- [Migración, referencias y excepciones concretas](docs/migracion.md).

El relevo local se completó el 2026-09-05. El catálogo contiene 533 objetos
activos y 21 archivados; la auditoría reconstruyó los 530 originales de pneuma
y verificó por separado el complemento de 21 objetos recuperados. Las 76 pruebas
del núcleo pasaron desde esta raíz. El recorrido independiente creó conocimiento,
skill y agente, los instaló y actualizó en ambos destinos, observó inferencia
real y comprobó recuperación sin acceso al núcleo anterior.

Las instalaciones quedaron con 106 bundles y 300 archivos administrados.
Codex descubrió sus 72 skills, abrió los 29 TOML nativos y una sesión nueva de
`$kora` utilizó la CLI y el conocimiento actuales. Hermes cargó los seis
perfiles completos y sus skills requeridas. `status` no informó cambios locales
ni recuperación pendiente al cierre. Los límites de cada comprobación y las
tres excepciones de referencias históricas están en los documentos enlazados.

La historia anterior y los doce cambios previos de Félix están conservados;
el relevo se integró en la rama local `fxai/relevo-kora-2026-09-05`.
`kora-rebuild` conserva la historia de origen y sus respaldos privados, sin
otra implementación activa. No se publicó Git remotamente.
