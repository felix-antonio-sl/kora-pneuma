# Autoría de agentes y skills

Escribe o corrige una fuente desde la función que necesita Félix. Busca primero
un producto que ya la cumpla. El [contrato de ingeniería agéntica](../cat-contrato-ingenieria-agentica/content.md)
orienta la elección entre agente y skill y la evidencia necesaria para el cambio.

## Escribir el contrato suficiente

Describe cuándo usar el producto, qué recibe, qué resultado utilizable produce,
qué condiciones cambian su actuación y qué hace ante información ausente o un
fallo relevante. Las instrucciones deben permitir actuar. Evita una colección
de adjetivos, taxonomías o promesas de autonomía sin mecanismo comprobado.

Expresa capacidades como acciones con herramientas que existen en el destino.
La fuente no concede permisos por declarar una herramienta. Conserva el modelo,
credenciales, configuración y estado personal del operador fuera del producto.
Si una diferencia de Codex y Hermes cambia el comportamiento, descríbela y
compruébala; no agregues destinos hipotéticos.

Mantén recursos junto al cuerpo cuando sean necesarios. Usa `requires` para
conocimiento o skills que deban llegar a la realización; usa `relations` para
vínculos documentales que no impliquen instalación. Lee las dependencias que
cambias y comprueba que sirven al procedimiento. Un enlace a otro agente no
ejecuta una delegación por sí solo.

## Crear o actualizar

Usa `create skill` o `create agent` con el cuerpo preparado; la sintaxis y los
campos están en la [guía operativa](../guia-rapida-pneuma/content.md). Para
actualizar, resuelve la identidad existente y edita su cuerpo, metadata o
recursos. Revisa también descripciones, ejemplos y plantillas que puedan
reintroducir instrucciones corregidas. Conserva cambios concurrentes y la
versión anterior mediante Git.

## Realizar y probar

Cuando el encargo comprende instalación, usa `instalacion-kora`: la operación
ya comprueba las dependencias y realiza los archivos afectados. Genera `render`
por separado si necesitas inspeccionar la salida sin instalarla. Usa `check`
cuando el diagnóstico requiera revisar el conjunto del catálogo.

Comprueba aquello que el cambio pretende conseguir. Una corrección editorial
requiere revisar el contenido y su conservación donde se realiza. Si cambias
conducta, observa un caso representativo y la excepción o ausencia que pueda
refutar la mejora. Si cambias una capacidad de destino, contrasta su contrato
en `docs/codex.md` o `docs/hermes.md`, versión instalada y fuente oficial vigente.
Entrega la fuente utilizable, lo comprobado y sus límites; la validez de los
archivos por sí sola no acredita conducta.
