# decommission-repo-legado

Retira un repositorio que ya tiene sucesor, conservando el valor necesario y
comprobando que sus consumidores pueden continuar. Sirve también para preparar
la consolidación cuando el encargo todavía no autoriza el retiro. Distingue el
legado, el sucesor y los consumidores concretos; incorpora KORA solo cuando
exista conocimiento compartido que mantener allí.

Si no hay sucesor, el trabajo puede ser un archivo con respaldo. Si el legado
sigue prestando una función sin reemplazo comprobado, conserva esa operación y
precisa qué falta para retirarla. No atribuyas autorización de borrado externo
a una solicitud de ordenar documentación.

## Encontrar lo que debe continuar

Identifica el trabajo único del legado, sus cambios locales y las dependencias
efectivas del sucesor. Busca referencias por nombre, ruta e identidades; lee el
contexto para distinguir homónimos y menciones dentro del nombre del sucesor.
Considera código, ejecución, datos y documentación según lo que contenga el
repositorio. El alcance de búsqueda debe cubrir los consumidores conocidos y
los lugares donde razonablemente pueda existir una dependencia.

Una referencia histórica registra lo que ocurrió y se conserva. Una instrucción
que todavía dirige a una fuente retirada debe actualizarse. Las menciones
marcadas explícitamente como legado no son dependencias activas. Conserva esta
distinción al revisar resultados de búsqueda; el total de coincidencias no
acredita retiro ni dependencia.

## Preservar antes de retirar

Antes de una acción destructiva, deja una copia recuperable fuera del árbol que
se retirará y fuera de repositorios publicados. Si existe historia Git, un
`git bundle create /ruta/privada/legado.bundle --all` conserva sus referencias;
verifícalo con `git bundle verify /ruta/privada/legado.bundle`. El bundle no
incluye cambios locales ni archivos sin seguimiento: conserva también el árbol
necesario mediante un archivo o una copia verificable. Incluye repositorios
anidados o datos externos cuando formen parte del valor que se retirará.

Comprueba que puedes recuperar los contenidos relevantes, no solo que existe
un archivo de respaldo. Protege credenciales y estado personal en el destino
privado correspondiente; documenta la localización suficiente para recuperar
sin compartir sus contenidos. Ajusta la copia al material existente; un
repositorio sin commits no necesita un bundle vacío.

## Integrar el valor y sus referencias

Lleva al sucesor los contenidos únicos que necesita. Conserva originales,
licencias e información de procedencia; evita copiar algo que ya tiene una
fuente vigente suficiente. Actualiza las referencias activas a su destino
correcto y registra la procedencia en el lugar donde ayude a usar ese material.
No crees un índice paralelo si esa información ya está en la fuente.

Si una guía mantiene supuestos retirados, corrige las partes afectadas contra
el funcionamiento del sucesor. Un traslado no obliga a reescribir el documento
completo ni a ingresarlo a KORA. Cuando el conocimiento pertenezca a KORA, usa
la [guía vigente](../../../docs/operacion.md): resuelve la referencia con
`python3 kora_cli.py resolve URN` y prepara su edición con `revise URN`.
El borrador se conserva en la biblioteca central y se publica cuando su contenido
está aprobado. Conserva la identidad cuando sigue siendo el mismo conocimiento.
`python3 kora_cli.py check` comprueba referencias y realizaciones; la fidelidad
del contenido se comprueba contra las fuentes y el sucesor.

Revisa los consumidores afectados dentro de la autoridad del encargo. Las
realizaciones de productos KORA se mantienen con `instalacion-kora`; no edites
sus copias nativas para corregir la fuente. Una referencia ajena que no puedas
actualizar sigue siendo una condición abierta, no un retiro completado.

## Comprobar independencia y ejecutar el retiro

Comprueba el recorrido que justifica al sucesor con el legado fuera de alcance.
Puedes usar un entorno temporal que no lo incluya o, si está autorizado, mover
el legado de forma reversible. Usa build y pruebas cuando sea software; para
un corpus o cuaderno, prueba la recuperación de fuentes y la operación que
necesita su consumidor. Una compilación correcta no cubre por sí sola una
ruta de datos o un enlace usado durante la ejecución.

Con respaldo recuperable, consumidores atendidos e independencia comprobada,
ejecuta el retiro autorizado. Resuelve la ruta exacta y preserva material ajeno.
No borres caches, servicios o remotos por asociación de nombre: cada retiro
necesita una razón y autoridad suficientes. Una disposición externa irreversible
requiere autorización explícita para ese destino; aprovecha la ya existente
en la sesión y consulta solo la que falte.

Si aparece una dependencia pendiente, recupera la operación necesaria y
corrígela antes de afirmar que el sucesor es independiente. Revisa las
referencias activas afectadas y el funcionamiento después del retiro.

## Cerrar con continuidad suficiente

Entrega qué se absorbió, dónde quedó el respaldo recuperable, qué consumidores
se actualizaron, qué se retiró y qué prueba acredita la independencia. Declara
los pendientes y límites materiales. Actualiza la documentación vigente que
necesite el operador; un único `HANDOFF.md` corresponde solo si queda trabajo
material que otra sesión deba retomar. No escribas memoria personal por rutina.

Si hay autoridad para commits, agrupa por intención, prepara rutas exactas y
revisa el diff preparado para conservar el trabajo ajeno. La publicación remota
requiere su propia autoridad y no es una condición universal para completar el
retiro local.
