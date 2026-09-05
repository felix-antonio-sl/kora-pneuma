# Instalación y mantenimiento

Usa esta skill para realizar productos KORA en Codex o Hermes, diagnosticar
desviaciones, actualizar, retirar o recuperar una operación. Trabaja con el
alcance y la autoridad ya concedidos. Una consulta o revisión por sí sola no
autoriza modificar una instalación; una instalación encargada no requiere
renovar esa aprobación en cada paso.

## Preparar y aplicar

Resuelve las identidades solicitadas desde la raíz de fuente que contiene
`kora_cli.py`. Comprueba referencias y archivos con `check`. Genera `render` en
un directorio nuevo cuando necesites revisar la realización antes de instalar.
El resultado se deriva de la fuente; no se edita como una segunda autoridad.

```bash
python3 kora_cli.py check --target codex
python3 kora_cli.py render codex ID --output /ruta/salida-nueva
python3 kora_cli.py status
python3 kora_cli.py install codex ID
```

Sustituye `ID` por una identidad resoluble y usa `hermes` para ese destino.
`--home DIRECTORIO` permite operar una instalación aislada. Sin identidades,
`install` selecciona todos los productos del destino; úsalo solo cuando el
alcance comprende ese conjunto. Consulta el `README.md` actual antes de una
operación que no conoces.

Una actualización también vuelve a realizar los consumidores ya administrados
del mismo destino que comparten dependencias afectadas. Así las copias dentro
de perfiles y agentes conservan una versión coherente. Para una skill instalada
en un perfil Hermes existente usa `install hermes ID --profile NOMBRE`; su retiro
con `remove hermes ID --profile NOMBRE` afecta solo esa instancia. El flag no
renombra agentes ni administra el SOUL, la configuración o el estado del perfil.
La raíz Hermes se opera sin `--profile`.

El instalador reconoce archivos por recibos y hashes. Si un archivo existente
no está bajo su gestión, no asumas propiedad por su nombre: compara contenido,
procedencia y consumidores. Para adoptar una instalación KORA anterior usa
`--adopt ARCHIVO_JSON` con el mapa revisado de rutas relativas al home y sus
SHA-256 actuales. Un hash acredita los bytes revisados, no acredita por sí solo
que sean propios. Conserva una base recuperable y excluye estado personal.

Si hay una edición local, examínala e intégrala en la fuente o consérvala como
trabajo pendiente de forma explícita antes de actualizar. No fuerces una
sobrescritura. Mantén archivos ajenos, memoria, credenciales, configuración y
sesiones fuera del conjunto administrado.

## Recuperar y retirar

```bash
python3 kora_cli.py recover
python3 kora_cli.py rollback
python3 kora_cli.py remove codex ID
python3 kora_cli.py status
```

`recover` atiende una transacción interrumpida; `rollback` deshace la última
aplicación preservando cambios posteriores. `remove` retira los archivos propios
intactos que ya no requiere otro producto instalado. Examina el resultado y las
rutas conservadas cuando aparezca un conflicto. Los respaldos y recibos viven
en el estado privado del instalador; no los copies a Git ni a evidencia pública.
No uses el borrado completo de un perfil o directorio como retiro de archivos.

## Comprobar en su destino

Revisa `status` y carga los productos con la superficie nativa efectiva.
Comprueba en una ejecución real la acción que motivó el cambio y un fallo
relevante. Un recibo limpio acredita archivos administrados; no acredita que el
modelo haya seguido las instrucciones. Registra versión, recorrido, resultado
observado y límites, sin secretos ni datos personales. Cierra con el estado
utilizable y una ruta de recuperación comprobada.
