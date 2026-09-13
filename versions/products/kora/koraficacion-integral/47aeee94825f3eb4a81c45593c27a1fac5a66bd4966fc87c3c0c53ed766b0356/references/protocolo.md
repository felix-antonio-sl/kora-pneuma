# Protocolo de compresión semántica integral

El helper `integral-3` administra fuentes, partición, inventarios, exclusiones de soporte, candidatas, revisiones e historia. `artifact.md` entrega contenido sustantivo autosuficiente; estado y recibo conservan procedencia y decisiones. Los hashes acreditan identidad; los rangos, cobertura de lectura; los booleanos registran juicios del modelo. Ninguno demuestra por sí mismo equivalencia semántica ni que una exclusión sea correcta. No edites `state.json` ni las entregas para adelantar pasos. Usa otra carpeta para fuentes, parámetros o versión diferentes.

## Operaciones de compresión

Parte de las unidades de significado para elegir una forma, en vez de copiar cada párrafo y sustituir conectores. Un conjunto de atributos suele admitir un sujeto común; roles distintos, una lista actor→función; transiciones, una secuencia con sus condiciones; estados o configuraciones comparables, correspondencias explícitas. Estas formas son opciones: usa la que reduzca costo conservando todas las relaciones. El sujeto tácito sólo sirve mientras su referente sea inequívoco.

**Reformular.** «Será responsabilidad de X proceder a registrar Y» puede ser «X debe registrar Y». Conserva modalidades informativas: «puede», «debe», «se recomienda», «sólo si» y «habitualmente» no son intercambiables. No conviertas descripción en obligación.

**Factorizar.** Expresa una vez un sujeto, predicado o condición compartido exactamente, manteniendo valores y alcance. Ejemplo:

> Fuente: Cuando la unidad está cerrada, el coordinador debe registrar la hora del aviso. Cuando la unidad está cerrada, el coordinador debe registrar el canal del aviso. Si el aviso es verbal, el coordinador debe confirmar por escrito su recepción antes de iniciar la asignación. La confirmación no transfiere la responsabilidad de asignar.
>
> Candidata: Unidad cerrada: el coordinador debe registrar hora y canal del aviso. Aviso verbal: el coordinador debe confirmar por escrito su recepción antes de iniciar la asignación. Confirmar no transfiere la responsabilidad de asignar.

«Unidad cerrada» gobierna sólo los dos registros. Si agrupas también la confirmación bajo ese encabezado, agregas una condición que la fuente no impuso. La puntuación y el anidamiento transmiten alcance.

Ejemplo de cambio de representación:

> Fuente: El depósito A recibe piezas y puede solicitar revisión del lote. El depósito B recibe herramientas y puede solicitar revisión del lote. Una revisión sólo se realiza si la responsable la autoriza. La recepción no constituye autorización.
>
> Candidata: Recepción: depósito A→piezas; B→herramientas. Ambos pueden solicitar revisión del lote; realizarla exige autorización de la responsable. Recibir no autoriza la revisión.

Permanecen las dos correspondencias, la facultad de ambos depósitos, el objeto revisado, la condición de ejecución y la negación. «Ambos revisan» perdería quién solicita y quién autoriza. Cambiar sólo «y» por «;» habría conservado casi toda la repetición original.

**Deduplicar.** Expresa una vez el contexto o la definición compartida que necesita el contenido. No describas las ocurrencias de una cabecera ni conserves dónde se imprimió. Referencia bloques anteriores para incluir una sola definición en el ensamblado. Compartir título no fusiona documentos, ediciones aplicables ni autoridades.

**Representar estructuras.** Si un procedimiento exige registrar nombre, cargo y firma, conserva esos campos y sus relaciones; la cantidad de renglones vacíos de la plantilla normalmente es soporte. Si el documento exige cinco registros, ese número es contenido. Una celda vacía no significa «no aplica». Convierte un diagrama en sus relaciones; conserva posición, color o disposición sólo cuando comunican una distinción sustantiva.

**Conservar correspondencias.** «A, B y C» no equivale a «elementos pertinentes»; «A revisa, B aprueba» no equivale a «revisión y aprobación». Una tabla compacta sirve si deja inequívocos sujeto, acción, condición y valor. Define abreviaturas sólo si se reutilizan con ahorro neto; evita claves opacas que exijan un diccionario adicional.

**Conservar la afirmación completa.** «Se aplicará» conserva su futuro; «se aplica» afirma otra situación temporal. «Se recomienda iniciar la transferencia» conserva recomendación, inicio y acción, no sólo el objeto transferido. Dos hechos junto a «debido a» expresan una relación causal que una enumeración puede perder. «Vigencia: junio de 2028» no autoriza agregar «hasta» si la fuente no define ese campo. Mantén literalmente una formulación ambigua cuando aclararla exigiría inventar su sentido.

Ejemplo de contenido científico:

> Fuente: En el ensayo con la versión B, la dispersión puede aumentar debido a la variabilidad del sensor. Se recomienda repetir la medición si la dispersión supera el umbral. La repetición no demuestra que el sensor sea defectuoso. Registros: serie de medidas; informe de ensayo.
>
> Candidata: Ensayo con versión B: la variabilidad del sensor puede aumentar la dispersión. Si la dispersión supera el umbral, se recomienda repetir la medición; repetirla no demuestra un defecto del sensor. Registros: serie de medidas e informe de ensayo.

«La variabilidad aumenta la dispersión» perdería posibilidad y alcance. «Repetir y registrar» añadiría obligaciones. «Resultados anómalos» sustituiría una condición concreta por una categoría más amplia. El ejemplo se evalúa por lo que permite afirmar, no por su parecido verbal.

Conserva nombres, valores, unidades, fechas, versiones, enlaces y código que formen parte del contenido o condicionen su interpretación. Un plazo o una vigencia declarada no son equivalentes a un número de página o una fecha de escaneo. Los autores del ejemplar y su trámite de aprobación pueden quedar sólo en la procedencia; los responsables y autorizaciones que el procedimiento exige deben permanecer. Mantén contradicciones e incertidumbres sustantivas. La compresión no resuelve lo que el original dejó abierto.

## Inventario: antes de redactar

`next` entrega texto, líneas y esquema. `lines` usa numeración de la fuente. Una unidad expresa una afirmación o conjunto coherente con todos sus elementos y relaciones, no una descripción de tema. Un párrafo puede requerir varias unidades; una tabla regular puede ser una unidad si conserva todos los campos y correspondencias. No fijes una cuota de unidades.

Los rangos de `units` deben cubrir todas las líneas no vacías tras retirar las exclusiones declaradas. `evidence` es opcional y, si se añade, debe existir en su rango. La cobertura de líneas no detecta una cláusula omitida dentro del rango: vuelve al original tras escribir `statement`.

`exclusions` contiene sólo soporte o procedencia que no necesita el lector: `id` único `x01`, `lines`, `quote` exacta y `reason` concreta. El helper exige una única ocurrencia de la cita en ese rango y rechaza exclusiones solapadas. En una línea que mezcla contenido y metadata, cita únicamente la parte formal; excluir la línea completa podría borrar una condición. La fuente permanece intacta y `next.content_source` muestra el texto restante con los números de línea originales. No excluyas excepciones, ejemplos, bibliografía argumentada, cláusulas o incertidumbres sustantivas por parecer accesorios.

Omite paginación, observaciones sobre OCR/Markdown, logotipos y firmas como objetos gráficos, formularios administrativos sin contenido, contactos del pie, historial de producción y fundamentos que sólo formalizan el ejemplar. Mantén un título útil y el ámbito o vigencia que cambien su aplicación, expresados una sola vez. No agregues un preámbulo para explicar esta limpieza. Si un bloque es sólo soporte, admite `units:[]`, `questions:[]`, candidata `text:""` y `mapping:[]`, con exclusiones completas y revisadas.

Aplica el criterio a cada fragmento, también cuando tiene palabras y parece informativo:

| Fragmento de la fuente | Tratamiento |
|---|---|
| «Resolución N.º 8: apruébese el procedimiento X del hospital Y; entra en vigencia en marzo de 2026» | Expresa procedimiento, ámbito e inicio declarado una vez. Conserva el número y el acto cuando identifican la autoridad aplicable, distinguen ediciones o permiten citar la obligación; sólo quedan en procedencia cuando no afectan interpretación ni uso. La fórmula gráfica de tramitación no exige una sección. |
| Tabla vacía de control editorial: modificación, fecha, código y edición | Omite la tabla y la descripción de sus columnas si ninguna instrucción sustantiva exige completar esos datos. Tener encabezados no convierte un formulario administrativo vacío en contenido obligatorio. |
| Tres viñetas muestran una bolsa enrollándose desde el colgador hacia las entradas | Conserva la dirección del movimiento en la instrucción correspondiente. Tres ilustraciones no establecen tres etapas obligatorias ni justifican narrar cada dibujo. |
| Un estudio histórico explica qué cambió una resolución y quién la firmó | Conserva resolución, cambios, actor y fecha pertinentes: son hechos estudiados, aunque esos mismos campos sean procedencia en otro documento. |
| «La versión 2.4 cambió el valor por defecto de `retry` de 0 a 3; la migración conserva el valor configurado» | Conserva versión, cambio, correspondencia de valores y excepción de migración. Un historial con efecto técnico es contenido. |
| «Ana propone activar el servicio en octubre; Luis posterga la decisión hasta recibir el ensayo» | Conserva atribuciones, propuesta, fecha prevista y condición de decisión pendiente. La existencia del acta no acredita activación ni acuerdo. |

La partición tampoco crea categorías del dominio: reúne bajo un mismo título los responsables o pasos divididos entre bloques. Rótulos como «responsabilidades iniciales» y «continuadas» sólo se justifican si esa distinción existe en el contenido.

`questions` contiene preguntas discriminantes con respuestas esperadas fijadas desde el contenido fuente. Habitualmente bastan 2–5 para un bloque ordinario; una para uno trivial. Abarca negación, condición, autoridad, secuencia o ambigüedad. No evalúes la recuperación de metadata excluida ni dependas de localizadores que desaparecen al reformular. `dependencies` contiene ids de bloques que necesitas consultar.

Fuente ilustrativa de dos líneas:

```text
PDF página 7 de 12.
El archivo debe retenerse durante 30 días. Está prohibido borrarlo antes de que termine ese plazo.
```

```json
{
  "stage":"inventory",
  "units":[
    {"id":"u01","lines":[2,2],"statement":"El archivo se retiene 30 días; está prohibido borrarlo antes de ese plazo."}
  ],
  "exclusions":[
    {"id":"x01","lines":[1,1],"quote":"PDF página 7 de 12.","reason":"Paginación del soporte; no expresa un plazo ni una condición del archivo."}
  ],
  "questions":[
    {"id":"q01","question":"¿Se puede borrar el archivo antes de 30 días?","expected":"No; se prohíbe borrarlo antes de ese plazo."}
  ],
  "dependencies":[],
  "source_rechecked":true,
  "source_review":"Cotejados objeto, plazo y prohibición; sólo la paginación queda fuera del contenido."
}
```

## Candidata y contexto compartido

`text` sustituye el bloque por su contenido. `mapping` tiene exactamente una entrada por unidad sustantiva y ninguna por exclusión. Su `quote` debe existir en `text`; si está en otro bloque, añade `block` y declara ese bloque y su hash en `references`. Sólo se admiten bloques anteriores aceptados de la misma fuente. Usa una cita que exprese la unidad, no una palabra genérica. Si una unidad combina definición previa y afirmación nueva, expresa localmente la relación y mapea esa frase: apuntar sólo a la definición omite lo nuevo.

`transformations` describe brevemente las operaciones efectivas. `issues` queda vacío sólo sin pérdidas conocidas abiertas. El cotejo inverso revisa toda la salida, incluidos títulos y conectores, aunque no se pida otro JSON que los copie carácter por carácter.

```json
{
  "stage":"candidate",
  "text":"Archivo: retener 30 días; prohibido borrarlo antes.\n",
  "mapping":[{"unit":"u01","quote":"Archivo: retener 30 días; prohibido borrarlo antes."}],
  "references":[],
  "transformations":["Una frase conserva objeto, plazo y prohibición con referente explícito."],
  "issues":[]
}
```

Para una unidad realmente repetida, usa por ejemplo `{"unit":"u02","quote":"Definición completa ya expresada.","block":"b0001"}` y `references:[{"block":"b0001","sha256":"HASH_ACEPTADO"}]`. El contexto queda dentro del documento y del costo total. En `text`, remite a un título, campo o declaración que el lector pueda identificar; `b0001` sólo identifica estado del helper. No añadas notas de continuidad del procesamiento. No borres una relación nueva porque parte de sus palabras aparezcan antes. Se admite `text:""` si todas las unidades remiten a referencias o el bloque carece de contenido sustantivo.

El helper protege los números, literales en línea y enlaces del contenido no excluido. Una cita formal omitida no dispensa otro uso del mismo número: excluir «Página 30» mantiene la exigencia de conservar el plazo «30 días» del texto restante. Los bloques de código cercado siguen protegidos en la fuente completa. Para una equivalencia numérica real admite `literal_changes` con `literal`, `quote` presente en salida y `reason`; por ejemplo, una enumeración de tres etapas representada como rango 1–3. Coteja cada aparición y conserva los valores de dominio. La metadata de soporte se declara en `exclusions`, no como una equivalencia numérica ficticia.

## Revisión y reparación

Toma `candidate_sha256` de `next`: incluye la identidad del contexto referenciado. `unit_checks` cubre unidades; `questions`, ids del cuestionario. Las respuestas son las obtenidas desde la candidata, no copias automáticas de `expected`. Cada razón identifica atributos o relaciones realmente cotejados.

```json
{
  "stage":"review",
  "candidate_sha256":"HASH_DEVUELTO_POR_NEXT",
  "unit_checks":[{"id":"u01","preserved":true,"reason":"Mismos archivo, plazo de 30 días y prohibición anterior al plazo."}],
  "exclusion_checks":[{"id":"x01","justified":true,"reason":"Se excluyen 7 y 12 como paginación; el plazo de 30 días permanece."}],
  "source_rechecked":true,
  "backward_complete":true,
  "relations_preserved":true,
  "relations_review":"Antes refiere al plazo del archivo; no se añadió obligación de borrar al cumplirse.",
  "questions":[{"id":"q01","answer":"No puede borrarse antes de los 30 días.","satisfied":true}],
  "literal_changes":[],
  "isolation":"same_context",
  "issues":[]
}
```

Usa `independent_context` sólo si la respuesta proviene de una ejecución sin fuente, oráculo ni conversación anterior. Para quien redactó o vio la fuente en su conversación, usa `same_context`; si no sabes, `unknown`. Una etiqueta no prueba independencia.

Cada exclusión requiere una entrada en `exclusion_checks`, con `id`, `justified` booleano y `reason`. Revisa su cita original: no debe eliminar contenido necesario para comprender o aplicar el documento. Una revisión negativa impide aceptar. Si la clasificación quedó equivocada en el inventario congelado, prepara otra ejecución con inventario corregido y conserva la anterior; no ocultes el problema declarando la exclusión válida.

Haz el cotejo sobre la fuente completa del bloque, no sólo sobre sus unidades. Para cada afirmación condensada contrasta sujeto, acción completa, objeto, modalidad, tiempo, condición, finalidad o causa y valores. Comprueba si algún título o conector añadió alcance o secuencia. Prueba una interpretación alternativa: si la candidata permite responder «obligatorio», «ya ocurrió», «siempre» o «es la causa» donde la fuente sólo permite «recomendado», «previsto», «bajo esta condición» o «puede causarlo», repara antes de aceptar. Registra defectos reales y sus reparaciones; no generes todos los `true` desde el mapeo.

Para cada regla, permiso, prohibición y excepción, escribe en la evidencia su condición y consecuencia en fuente y candidata. Compara conjunción, alternativa, negación y alcance de «sólo», «salvo», «antes» o «después». Cuando hay varias condiciones, prueba combinaciones que distingan las lecturas: cumplir sólo una, ninguna o todas. Por ejemplo, «se permite si existe reserva o invitación» admite dos vías; «requiere reserva e invitación» exige ambas. Una revisión puede encontrar los mismos sustantivos y aun así omitir esa diferencia. Conserva las formulaciones y el caso que cambia la decisión como evidencia; no hace falta añadir esa tabla de cotejo al artefacto.

Un control negativo se prepara en una copia aislada, con una alteración material conocida y su registro fuera de los insumos del revisor. No le adelantes dónde está ni el dictamen esperado. Después contrasta su informe con la alteración: sólo cuenta como detectada si localiza esa diferencia y explica qué afirmación o decisión cambia. Un rechazo por otro motivo no valida el control. Conserva los intentos fallidos; al repetir, declara si el revisor ya había visto ese caso o recibió orientación adicional.

Si la candidata declaró cambios de números, añade sus cotejos a `literal_changes`, con `literal`, `preserved` y `reason`. Debe haber un cotejo por cambio real; con ninguno, usa `[]`.

Una revisión negativa conserva la candidata rechazada y vuelve a `candidate`, con inventario congelado. Repara la condición, atributo o relación fallida y conserva lo demás. Tras dos reparaciones infructuosas sobre un pasaje, incorpora su texto literal dentro de la candidata compacta. `retain --block ID --reason ...` conserva el bloque entero cuando sea necesario; con exclusiones se rechaza para evitar reintroducir soporte. En ese caso presenta el `content_source` pertinente como candidata, con sus mapeos y cotejo.

Si el inventario omitió significado, la candidata debe restaurarlo desde la fuente. No reduzcas el oráculo para hacerla pasar. Registra la omisión; para rehacer el inventario prepara otra ejecución, conservando la anterior. Un inventario bien formado no tiene autoridad sobre la fuente.

Para reparar un bloque aceptado:

```sh
python3 scripts/integral.py show --work /ruta/trabajo --block b0001
python3 scripts/integral.py reopen --work /ruta/trabajo --block b0001 --candidate-sha256 HASH_ACEPTADO --reason 'Restaurar la condición que restringe la autorización.'
```

Usa el `sha256` de `accepted` mostrado por `show`. La operación archiva la revisión, conserva inventario e invalida consumidores de ese texto y revisión global. Repetir la misma operación no la aplica dos veces. No regeneres partes aceptadas que no dependían del cambio.

## Conjunto y entrega

Al terminar, `next` entrega texto y hash del ensamblado y pide el paso global. También puedes verlo con `show --block global`, sin construir una entrega aceptada. Lee el ensamblado y coteja originales, incluidos anexos. Comprueba contenido conservado y exclusiones justificadas, condiciones entre bloques, definiciones compartidas, secuencia, referencias, contradicciones y alcance de atribuciones. Revisa `literal_changes` y unidades remitidas. Elimina del artefacto notas sobre la transcripción, páginas, la limpieza realizada o cómo se procesaron los bloques.

```json
{
  "stage":"global",
  "assembly_sha256":"HASH_DEVUELTO_POR_NEXT",
  "block_checks":[{"id":"b0001","preserved":true,"reason":"Objeto, plazo y prohibición conservados al ensamblar."}],
  "source_rechecked":true,
  "relations_review":"Sin otras secciones; mismo plazo de retención y prohibición.",
  "issues":[],
  "limits":"Cotejo del autor; sin lectura independiente. No acredita equivalencia universal.",
  "negative_control":{"status":"NOT_RUN","reason":"No se ejecutó un revisor sobre una copia alterada."}
}
```

`negative_control` registra una declaración de la revisión. El helper actual
no exige ni valida este campo; cuando se incluye, queda conservado en la
revisión global de `state.json`, identificada por el hash del recibo. Su ausencia
no acredita ejecución y su presencia tampoco. La primera aplicación o un cambio
del método requieren realizar el control indicado en la skill o declarar el
límite pendiente. El recibo no exporta directamente este campo: conserva la
revisión y la observación del ensayo cuando sustentan una afirmación de control.

`block_checks` cubre todos los bloques. Una pérdida conocida impide aceptar. Repara y revisa el nuevo hash; no reutilices un juicio sobre otra versión. `build` conserva la entrega previa hasta revisión aceptada y protege ediciones ajenas.

El recibo distingue conteo y juicio. Registra `source_tokens`, `content_source_tokens` (fuente tras exclusiones), `excluded_source_tokens` y `candidate_tokens`. `saving_vs_content_tokens` separa compresión del contenido de retiro de soporte. También mide versiones normalizadas. `GAIN_OBSERVED` exige ahorro frente al contenido normalizado con transformaciones declaradas; excluir metadata por sí solo no acredita ese resultado. `NO_GAIN` indica ausencia de mejora adicional y `NOT_MEASURED`, ausencia de contador. Cuenta todo contexto que el lector necesite. La evidencia auxiliar queda fuera de ese texto; si alguna parte es necesaria para entenderlo, incorpórala y cuenta su costo.

El primer `NO_GAIN` invita a revisar la representación. Si aún no comparaste una alternativa sustantiva, prueba factorizar el contexto, reunir correspondencias o expresar las relaciones con una forma más breve; no basta retirar saltos de línea. Reabre sólo los bloques que cambies y vuelve a cotejar cada unidad y exclusión. Guarda en `transformations` y en la revisión global la alternativa efectivamente comparada, el resultado y por qué conservas una versión. Si no mejora sin pérdidas, puedes cerrar con `NO_GAIN` sustentado en esa comparación; nunca completes las pruebas con afirmaciones inventadas.

Informa reducción total, retiro de soporte, compresión del contenido, cotejo, aislamiento real y límites en la entrega al operador, sin anteponerlos al artefacto de conocimiento. Medir el documento completo no acredita un recuperador por fragmentos: cada fragmento necesita sus condiciones y definiciones heredadas.
