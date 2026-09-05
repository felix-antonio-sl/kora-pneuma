# Efectos y límites de las operaciones KORA

Esta explicación complementa el [modelo de fuente](../cat-kora-kernel/content.md).
Los comandos y su uso están en la [guía operativa](../guia-rapida-pneuma/content.md).

## Fuente, realización e instalación

Publicar un cuerpo y conservar sus originales hace recuperable lo autorado;
no acredita su fidelidad. Resolver una identidad permite encontrar ese contenido,
incluidos antecedentes archivados, sin demostrar consumo ni habilitarlos para
realización.

La realización comprueba dependencias, colisiones de paths y huellas de fuente
antes y después de generar archivos. Un cambio observado detiene el plan; una
edición posterior requiere otra realización. Los archivos producidos todavía
necesitan ser descubiertos, cargados y utilizados por el runtime.

La instalación relaciona el plan actual, la propiedad registrada y los archivos
efectivos. Una edición local o un archivo ajeno sin adopción detiene la operación.
La propiedad compartida se conserva: retirar un producto no elimina archivos
que otro conjunto instalado necesita.

## Transacción y recuperación

El instalador serializa sus operaciones y prepara reemplazos antes de modificar
archivos. Registra un diario y conserva cada archivo desplazado, incluidas las
escrituras que otro proceso haga por un descriptor que ya tenía abierto.

El reemplazo es atómico por archivo; un lector concurrente puede observar un
estado intermedio del conjunto. Ante una interrupción, la recuperación reconoce
una confirmación cuyo estado y archivos corresponden al resultado; de otro modo
intenta restaurar el estado anterior. El rollback actúa sobre la última
transacción confirmada mientras el estado no haya avanzado. Una edición posterior
se conserva y puede impedir esa restauración hasta reconciliarla.

El diario y los archivos desplazados permanecen en el estado privado del home,
fuera de Git. La recuperación ensayada cubre interrupciones de procesos; no
acredita resistencia a fallas físicas de almacenamiento. Una instalación coherente
tampoco acredita conducta del agente ni equivalencia entre modelos.

Implementación: [instalación y recuperación](../../../kora/install.py) y
[decisiones de filesystem](../../../docs/diseno.md).
[Semántica anterior](../../../archive/previous/kora/cat-kora-semantica-operacional/content.md).
