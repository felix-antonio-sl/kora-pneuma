# Instalación y mantenimiento

Usa esta skill para realizar productos KORA en Codex o Hermes, diagnosticar
desviaciones, actualizar, retirar o recuperar una operación. Trabaja con el
alcance y la autoridad ya concedidos. Una consulta o revisión por sí sola no
autoriza modificar una instalación; una instalación encargada no requiere
renovar esa aprobación en cada paso.

## Preparar y aplicar

Resuelve las identidades solicitadas y el destino autorizado. Aplica `install`
sobre ellas: el comando comprueba dependencias, realiza archivos nativos y
reconoce cambios locales antes de escribir. La [guía operativa](../../../docs/operacion.md)
contiene la sintaxis, el alcance de perfiles Hermes y la prueba con home temporal.
Sin identidades se actualiza el conjunto del destino; úsalo cuando ese sea el
alcance del encargo.

El conocimiento permanece en la biblioteca seleccionada por `knowledge` o
`--knowledge-root`. Los archivos nativos contienen referencias estables de
lectura, sin incorporar una copia del conocimiento. Una publicación aprobada
queda disponible en esa referencia sin reinstalar sus consumidores. Si cambia
la ubicación de la biblioteca, actualiza las rutas mediante la instalación de
los consumidores afectados. Instalar un agente o skill no aprueba borradores ni
cambia el estado de una referencia.

Usa `render` si necesitas inspeccionar una salida sin instalarla y `check` para
diagnosticar el catálogo completo. No son pasos previos obligatorios de cada
actualización. Los consumidores afectados se seleccionan por sus dependencias
actuales y los archivos que siguen bajo su gestión, incluso si retiraron una
dependencia de la fuente. Un producto ajeno al cambio puede seguir instalado
aunque su fuente esté archivada; si comparte archivos afectados, el conflicto
se debe resolver antes de actualizarlos.

El instalador reconoce archivos por recibos y hashes. Si un archivo existente
no está bajo su gestión, compara contenido, procedencia y consumidores antes de
atribuirle propiedad. Para adoptar una instalación KORA anterior usa
`--adopt ARCHIVO_JSON` con el mapa revisado de rutas relativas al home y sus
SHA-256 actuales. El hash acredita bytes; la procedencia acredita propiedad.

Si hay una edición local, examínala e intégrala en la fuente o consérvala como
trabajo pendiente de forma explícita antes de actualizar. No fuerces una
sobrescritura. Mantén archivos ajenos, memoria, credenciales, configuración y
sesiones fuera del conjunto administrado.

## Recuperar y retirar

`recover` atiende una transacción interrumpida; `rollback` deshace la última
aplicación preservando cambios posteriores. `remove` retira los archivos propios
intactos que ya no requiere otro producto instalado. Examina el resultado y las
rutas conservadas cuando aparezca un conflicto. Los respaldos y recibos viven
en el estado privado del instalador; no los copies a Git ni a evidencia pública.
No uses el borrado completo de un perfil o directorio como retiro de archivos.
Estas operaciones atienden la instalación; no revierten ni retiran publicaciones
de conocimiento. La corrección de una referencia usa un nuevo borrador y su
aprobación en la biblioteca.

## Comprobar en su destino

Comprueba el resultado de la operación y usa `status` para reconocer desvíos o
recuperación pendiente. Si el cambio afecta la carga nativa, comprueba esa carga;
si pretende cambiar conducta, observa la acción y el límite relevante en una
ejecución real. Una corrección editorial no requiere por sí sola inferencia.
Un cambio al instalador requiere probar su operación y recuperación afectadas
en un home temporal. Informa lo observado y los límites concretos: un recibo
limpio acredita archivos administrados, sin acreditar que el modelo los siga.
