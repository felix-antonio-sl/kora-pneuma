# Autoría de agentes y skills

Usa esta skill al crear o actualizar un agente o una skill KORA. Convierte el
encargo, la función que debe cumplirse y las capacidades efectivas de Codex o
Hermes en una candidata mínima, revisable y comprobable. La salida incluye su
fuente agnóstica, dependencias y recursos justificados, casos de prueba y el
estado de revisión o admisión alcanzado dentro de la autoridad de la sesión.

La autoría no concede permisos, no aprueba conocimiento y no autoriza por sí
misma una admisión, instalación, comunicación ni cambio externo. Usa las
decisiones y autorizaciones ya presentes en el encargo, sin pedirlas de nuevo;
si falta una decisión que cambia materialmente el producto, prepara lo
independiente y señala el punto exacto que requiere resolución.

## Elegir qué autorar

Busca primero si un producto o conocimiento vigente ya cumple la función. Elige
la forma por el trabajo que debe sostener:

| Forma | Úsala cuando | Debe conservar |
|---|---|---|
| **Agente** | Hace falta una responsabilidad estable, criterio para elegir entre cursos de acción, límites de autoridad y selección de métodos según la situación. | Propósito, destinatario, responsabilidad, decisiones que puede tomar o preparar, límites, conducta ante incertidumbre y métodos disponibles. |
| **Skill** | Hace falta un procedimiento reconocible y reutilizable dentro del trabajo de uno o más agentes. | Disparador, entradas, resultado suficiente, pasos o decisiones, excepciones, herramientas y recursos pertinentes. |
| **Conocimiento** | Hace falta conservar fuentes o una síntesis atribuible que varias tareas puedan consultar, sin imponer una conducta. | Alcance, condiciones, excepciones, procedencia, incertidumbres y acceso a los originales necesarios. Se prepara y publica mediante el flujo de conocimiento, no mediante esta skill. |

No conviertas una referencia en skill solo para hacerla visible, ni un conjunto
de procedimientos en agente si nadie necesita delegarle una responsabilidad.
Una skill no requiere una persona independiente; un agente no debe duplicar en
su cuerpo los métodos completos que ya puede invocar.

## Escribir el contrato suficiente

Parte de una entrada o situación concreta y del resultado que necesita el
consumidor. Define:

- el disparador que debe permitir seleccionar el producto y un encargo vecino
  en que no debe activarse;
- las entradas indispensables y los supuestos menores que pueden quedar
  explícitos;
- el resultado utilizable y una condición que permita reconocer que está
  completo;
- las decisiones y excepciones que cambian la actuación;
- la respuesta a información ausente, contradicción, fallo de una herramienta
  o límite de autoridad;
- la evidencia que podría confirmar o refutar que el producto cumple su
  función.

Escribe instrucciones que permitan actuar. Los adjetivos, taxonomías y promesas
de autonomía solo sirven cuando se traducen en una elección observable. Mantén
la fuente agnóstica; describe diferencias de Codex y Hermes únicamente cuando
cambien el uso o el resultado. Contrasta una capacidad cambiante con
`docs/codex.md`, `docs/hermes.md`, la versión instalada y, cuando sea necesario,
la fuente oficial vigente. Declarar una herramienta no la instala, no concede
sus permisos y no demuestra que funcione.

El modelo, credenciales, memoria, configuración y estado personal pertenecen al
operador. El producto solo puede prometer acciones realizables mediante las
herramientas disponibles en el destino y dentro de la autoridad de la sesión.

## Integrar persona cuando aporta a un agente

La persona es una ruta opcional de la autoría de agentes. Úsala cuando una pauta
estable de juicio o expresión cambie de forma útil la actuación del rol; omítela
si el contrato y los métodos bastan. El autor o integrador seleccionado conserva
la responsabilidad por el contrato completo y por integrar esta ruta. La pauta
de [persona](references/persona.md) aporta el procedimiento específico, sin
crear otra dependencia ni transferir autoridad desde una persona real.

## Delimitar dependencias y recursos

Declara en `requires` solo aquello que debe estar disponible para usar el
producto:

- una skill cuyo procedimiento el agente o skill necesita invocar;
- un conocimiento publicado que el consumidor debe poder consultar;
- una capacidad de destino efectivamente requerida, con condición y propósito
  cuando corresponda.

Usa `relations` para procedencia, reemplazos, afinidad, contraste o navegación
documental que no deban instalarse ni resolverse para ejecutar el producto. Una
cita en el cuerpo tampoco constituye una dependencia. Comprueba que cada
`requires` resuelva, aporte lo que el consumidor afirma obtener y no forme un
ciclo. Una referencia a otro agente no ejecuta una delegación.

Conserva scripts, plantillas, ejemplos o referencias propias junto al cuerpo
solo cuando el procedimiento los necesita. Decláralos expresamente en
`resources` con rutas relativas acotadas. Prefiere instrucciones en el cuerpo;
usa un script para una operación determinista o repetible y carga una referencia
extensa solo en la rama que la necesita. Los originales de conocimiento
permanecen en su biblioteca y no se copian al producto por comodidad.

## Preparar, revisar y admitir sin editar la fuente activa

La [guía operativa vigente](../../../docs/operacion.md) es la autoridad para la
sintaxis completa. Mantén siempre una fuente activa intacta mientras se revisa
su reemplazo.

Para un producto nuevo, prepara el cuerpo y crea una candidata sin admitirla:

```sh
python3 kora_cli.py create skill namespace nombre \
  --id urn:namespace:artefacto:nombre \
  --description 'Usar al…' --body /ruta/content.md \
  --candidate ajuste --prepare-only
```

Usa `agent` en lugar de `skill` cuando corresponda. Edita únicamente el
`product/` de la candidata que devuelve la orden. Para una identidad vigente,
parte de su revisión activa:

```sh
python3 kora_cli.py revise urn:namespace:artefacto:nombre --candidate ajuste
# editar solo la candidata indicada
python3 kora_cli.py review urn:namespace:artefacto:nombre --candidate ajuste
python3 kora_cli.py admit urn:namespace:artefacto:nombre \
  --candidate ajuste --reviewed SHA_REVISADO
```

`review` identifica el contenido, manifiesto y recursos concretos, además de su
base; no acredita semántica, conducta ni utilidad. Ejecuta `admit` solo cuando
la sesión autorice admitir esa revisión. Si la candidata cambia, vuelve a
revisarla. Si otra persona o proceso cambia la fuente activa, no sobrescribas su
trabajo ni fuerces una base obsoleta: inspecciona ambos cambios, conserva la
candidata y prepara o reconcilia una revisión sobre la nueva base. Nunca edites
directamente `products/`, versiones conservadas o realizaciones nativas para
eludir este ciclo.

## Comprobar el resultado

Revisa primero el contrato contra el encargo y las fuentes pertinentes. Usa las
comprobaciones mecánicas de la CLI para detectar identidad, dependencia,
recursos o realización inválidos. `render` permite inspeccionar Codex y Hermes
sin instalar; `instalacion-kora` corresponde cuando el encargo comprende
realización o actualización de un home. La validez de archivos no demuestra
que el runtime haya descubierto, cargado o aplicado las instrucciones.

Cuando cambia conducta, prueba en una sesión limpia un caso representativo, una
excepción o ausencia decisiva y un encargo vecino en que la skill no debe
seleccionarse. Usa datos sintéticos salvo que el encargo autorice otros. Compara
la observación con el resultado suficiente y corrige contradicciones, recursos
inaccesibles o promesas no realizadas. Entrega la candidata concreta, su base,
lo revisado, las comprobaciones ejecutadas y los límites de evidencia.
