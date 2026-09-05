# Autoría de agentes y skills

Escribe una fuente reutilizable desde la función que necesita Félix. Un agente
aporta una perspectiva y conducta sostenidas; una skill aporta un procedimiento
que se activa dentro de una sesión. Ambos pueden requerir conocimiento y skills
existentes. Elige por el uso real y conserva una sola fuente de cada producto.

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
vínculos documentales que no impliquen instalación. Lee cada dependencia y
comprueba que realmente sirve al procedimiento. Un enlace a otro agente no
ejecuta una delegación por sí solo.

## Crear o actualizar

Localiza la raíz que contiene `kora_cli.py` desde la ruta de esta fuente. Consulta
su `README.md` si necesitas la sintaxis completa. Crea desde un cuerpo preparado:

```bash
python3 kora_cli.py create skill ejemplo revisar-entrega \
  --id urn:ejemplo:artefacto:revisar-entrega \
  --description 'Revisa una entrega aplicando condiciones, excepciones y datos desconocidos.' \
  --body /ruta/procedimiento.md --target codex --target hermes \
  --requires urn:ejemplo:kb:criterios-entrega
```

Para un agente usa `create agent` con su cuerpo y dependencias. Para actualizar,
resuelve la identidad existente y cambia `content.md`, `object.yaml` o sus
recursos en esa fuente. Conserva cambios concurrentes y la versión anterior
mediante Git. El catálogo no necesita regenerar un índice manual.

## Realizar y probar

Ejecuta `check` y `render codex ID --output DIRECTORIO_NUEVO` o la variante
`hermes`. Revisa el cuerpo y los recursos nativos, incluidos los conocimientos
requeridos. Codex produce skills y roles de agente, con una activación directa
derivada para cada agente. Hermes produce skills y perfiles de agente. Las
capacidades actuales se documentan con fuentes en `docs/codex.md` y
`docs/hermes.md`; verifica cambios cuando dependas de ellas.

Con un encargo que autorice instalación, usa `instalacion-kora`. Prueba un caso
normal y una excepción decisiva en el destino real. Distingue carga del archivo,
conservación de contenido, disponibilidad de herramientas y conducta observada.
Entrega la fuente que se puede continuar, los comandos usados y los límites
concretos de comprobación.
