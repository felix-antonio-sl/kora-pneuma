# Efectos y fallos de las operaciones KORA

Esta explicación usa el [modelo operativo actual](../cat-kora-kernel/content.md)
y la interfaz `kora_cli.py`. Describe qué cambia y qué puede concluirse de cada
resultado; los estados y operaciones anteriores permanecen como antecedentes.

## Consultar, autorar y realizar

| Operación | Efecto observable | Límite relevante |
|---|---|---|
| `list` | Deriva objetos desde las fichas; `--archived` selecciona los inactivos conservados. | Presencia no prueba consumo. |
| `resolve ID` | Devuelve identidad, archivo y actividad, siguiendo alias. | Resolver un archivado no permite realizarlo. |
| `create` | Publica un producto nuevo con el cuerpo y originales proporcionados. | No sintetiza conocimiento ni acredita fidelidad semántica; rechaza identidad y ubicación ocupadas. |
| `check` | Comprueba referencias declaradas y realiza en memoria los consumibles del destino seleccionado. | No instala ni observa conducta. |
| `render TARGET ID --output DIR` | Produce archivos nativos y dependencias en una salida nueva. | Todavía requiere descubrimiento, carga y ejecución en el runtime. |

La realización compara huellas de fuente antes y después de construir archivos
y comprueba colisiones de paths. Un cambio observado detiene ese plan. No impide
una edición posterior de la fuente; cada actualización vuelve a derivar su plan.

## Instalar, retirar y recuperar

El instalador toma un lock local y compara bytes y modos de los archivos que
administra con el estado anterior. Una edición local o un archivo ajeno no
adoptado detiene la operación. Adoptar archivos existentes requiere un mapa de
hashes revisado; su nombre no demuestra propiedad.

Antes de modificar archivos prepara reemplazos, copias previas y un diario.
Recomprueba cada entrada antes de cambiarla. Conserva la propiedad compartida:
retirar un producto no elimina archivos que otro conjunto instalado necesita.

`status` informa diferencias respecto del estado instalado registrado y si hay
recuperación pendiente. `recover` atiende el diario pendiente: si el estado
confirmado y los archivos corresponden al resultado, reconoce la confirmación;
en otro caso intenta restaurar el estado anterior. `rollback` actúa sobre la
última transacción confirmada cuando el estado no avanzó. La recuperación se
detiene ante una edición posterior ajena a la transacción. Preserva ese cambio
y reconcilia la diferencia antes de insistir.

El diario y sus copias viven bajo `.local/state/kora` del home seleccionado,
fuera de la fuente Git. El retiro conserva directorios y estado personal ajenos.
La instalación usa reemplazos por archivo y recuperación del conjunto; no
promete atomicidad de todo el runtime. La atomicidad documentada por
[Python para os.replace](https://docs.python.org/3.12/library/os.html#os.replace)
corresponde al renombre individual cuando tiene éxito.

## Comprobar la consecuencia necesaria

Revisa lo que necesitaba el encargo: fuente conservada, referencias utilizables,
carga del producto, conducta ante condición y excepción, y recuperación cuando
corresponda. Un comando sin error, un archivo idéntico y una respuesta del modelo
contestan preguntas distintas. Usa el path y la causa reportados para corregir
un fallo; no alteres el registro privado para ocultar una diferencia.

Implementación: [CLI](../../../kora/cli.py) e
[instalación y recuperación](../../../kora/install.py). El
[README](../../../README.md) indica las comprobaciones ejecutables.
[Semántica anterior](../../../archive/previous/kora/cat-kora-semantica-operacional/content.md).
