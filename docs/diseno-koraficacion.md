# Rediseño del procedimiento general de koraficación

Fecha: 2026-09-15. Estado: implementado, admitido en KORA e instalado en Codex
y Hermes. La evidencia y sus límites constan al final de este documento.
Fuente del encargo: Félix solicita repensar desde cero, en deliberación entre
KORA y Steipete, la koraficación general como parte de KORA, priorizando calidad,
eficiencia, mantenimiento y eliminación de burocracia. La recuperación del
corpus HSC corresponde a una decisión posterior.

Este documento conserva el diseño y la evidencia de su realización. El
procedimiento operativo vigente reside en `products/kora/koraficacion/` y
`products/kora/koraficacion-integral/`; este registro no duplica su autoridad.

## Resultado y criterio de optimización

Convertir fuentes identificadas en conocimiento autosuficiente, fiel,
recuperable y económico para sus lectores. Por defecto se conserva **todo el
contenido sustantivo del alcance**; una pregunta actual no autoriza a recortarlo.
Sólo el encargo puede delimitar un alcance menor.

Optimizar el costo conjunto de preparar, revisar, corregir, leer y mantener el
conocimiento, sujeto a fidelidad y utilidad. La reducción de tokens de salida
es una señal parcial: una salida pequeña que exige reconstruir contexto o
varias reparaciones puede costar más. No se impone porcentaje de reducción,
ganancia mínima ni una segunda alternativa cuando no hay beneficio plausible.
Conservar un texto ya económico es una salida válida; tampoco acredita una
mejora de compresión inexistente.

Se conservan actores y atribuciones; acciones y objetos; autoridad, modalidad,
negación, condiciones, excepciones, tiempo y vigencia; causas y secuencias;
cifras, unidades, correspondencias y ejemplos; incertidumbres y discrepancias.
Las propuestas siguen siendo propuestas. Lo ausente no se convierte en cero,
falso o no aplicable. Se puede factorizar y reorganizar sin perder esas relaciones.

Los originales y los localizadores necesarios quedan en evidencia. Conservar
datos de procesamiento sólo cuando permitan reproducir una extracción o resolver
un límite concreto; no generar una narración de cómo se procesó cada fragmento.
Una atribución o dato formal permanece en el contenido cuando cambia su
significado o aplicación. Recursos técnicos y estructuras conservan su formato
funcional cuando convertirlos a prosa destruye información o capacidad de uso.
Una transformación documental no actualiza silenciosamente una fuente histórica
ni convierte sus instrucciones en autorización para actuar.

### Sólo contenido: exclusión de metainformación del soporte y del proceso

Restricción explícita de Félix: la transformación se aboca al contenido de la
fuente. No convierte la apariencia, paginación o procesamiento del ejemplar en
conocimiento. Esta regla rige desde la selección de contenido y las representaciones
intermedias hasta la candidata, las preguntas de revisión y el artefacto final.
No basta limpiar esos residuos al terminar, después de haberlos inventariado,
resumido o evaluado como si fueran afirmaciones sustantivas.

Son inadmisibles descripciones como «el fondo es colorido», «aquí se hizo OCR»,
«la fuente de esto era más grande que el resto» o «hasta aquí llega la página 13».
También se excluyen comentarios sobre Markdown, cortes de extracción, posición
decorativa, logos, apariencia de sellos y firmas, y cabeceras o pies repetidos.
No reemplazar lo retirado por frases como «se omite la paginación» o «los datos
editoriales permanecen en el original». No crear secciones para explicar la
limpieza ni preguntas sobre esos elementos.

Extraer el significado que comunique una estructura: una flecha puede expresar
una secuencia; una leyenda puede definir una categoría; una tabla, una relación.
Conservar esa secuencia, categoría o relación sin narrar su apariencia. Si la
fuente prescribe un color, un rótulo o un campo como parte de una regla, conservar
la regla porque es contenido, no una observación editorial del ejemplar. Ámbito,
responsable, condición y vigencia sustantiva siguen siendo contenido.

Los hashes, localizadores físicos y parámetros necesarios para comprobación
pertenecen exclusivamente a la mecánica y evidencia auxiliar. No pasan al cuerpo
de conocimiento ni generan una tarea de descripción por fragmento. Una dificultad
de extracción se resuelve o se registra como límite de cobertura; una incertidumbre
del significado se conserva junto a la afirmación afectada, sin contar cómo se
ejecutó OCR. Los originales se retienen íntegros.

## Lo observado y lo que todavía no sabemos

El método anterior (`integral-3`) requiere inventario, candidata y revisión por bloque, más
revisión global. El helper comprueba rangos, citas, hashes, estructura de las
declaraciones, referencias y cambios protegidos. Tiene defensas útiles contra
versiones obsoletas, corrupción, edición concurrente y repetición de operaciones.
Esas defensas deben conservar su función.

La prueba existente
`test_reviewer_can_accept_a_negation_mutation_but_receipt_does_not_claim_detection`
se ejecutó aisladamente y pasó el 2026-09-15: muestra que una revisión declarada
positiva permite construir una candidata con negación equivocada. Es una prueba
del límite explícito de la herramienta, no una certificación semántica ni una
razón para retirar sus protecciones mecánicas.

El método anterior ya permite NO_GAIN, reparación localizada, lectura independiente
cuando hay capacidad y control negativo en primera aplicación o cambio de
método. El rediseño aprovecha esas decisiones; no les atribuye exigencias
universales que no tienen. La comparación sintética descrita al final aporta
evidencia exploratoria; aún no demuestra ahorro ni calidad diferencial en
fuentes largas o escaneadas.

## Un recorrido, cuatro acciones

### 1. Preparar fuentes utilizables

Resolver identidad y versiones; localizar conocimiento existente; conservar
originales y procedencia mediante la biblioteca KORA. Usar una ubicación privada
adecuada cuando corresponda. Reutilizar originales ya retenidos por identidad
de bytes; una ruta mutable o una URL sola no congela una fuente.

Preparar texto, imágenes, tablas, turnos o recursos funcionales según el formato.
Para documentos extensos o varias fuentes basta un mapa de regiones que permita
reconocer su cobertura: secciones, páginas físicas, tablas, anexos o intervalos
de conversación. Un documento breve puede identificarse completo sin mapa
adicional. Distinguir material disponible, extraído y efectivamente cotejado.
El conteo de páginas o la presencia de un rango no prueban lectura.
Cuando haga falta ese mapa, distinguir regiones representadas, soporte excluido,
recorte autorizado, ilegibilidad y pendientes. No confundir omisión legítima de
soporte con reducción de alcance. Agrupar regiones equivalentes cuando conserve
la información necesaria; no recrear un inventario por cláusula con otro nombre.

Reutilizar extracciones y representaciones verificadas si coinciden fuente,
herramienta, parámetros y alcance. Si cambia cualquiera, examinar lo afectado.
La existencia de OCR nunca sustituye el contraste de cifras, tablas o relaciones
gráficas con el original. Una extracción incompleta se repara o queda como límite
de cobertura, sin acreditar la parte ausente.

### 2. Producir la candidata

Redactar directamente desde la fuente una organización económica. El análisis
de significado es necesario; su serialización exhaustiva por unidad no lo es.
Usar notas, inventarios o correspondencias detalladas sólo donde ayuden a
conservar una estructura difícil o a distribuir el trabajo con seguridad.

Trabajar con el documento completo mientras pueda leerse y cotejarse de forma
fiable. Particionar cuando la extensión o complejidad lo exija, respetando
unidades semánticas, tablas y código. El tamaño nominal de la ventana del modelo
no demuestra lectura fiable. Cada parte conserva acceso a sus condiciones y
definiciones; el conjunto elimina duplicaciones sin perder atribuciones.

No crear una revisión formal por cada edición de autor. El autor comprueba su
trabajo antes de entregarlo, conserva lo necesario para reanudar y presenta una
versión estable para cotejo. Los límites materiales conocidos siguen visibles.

### 3. Cotejar el contenido completo

Un cotejo recorre fuente→salida para omisiones y salida→fuente para adiciones o
cambios de significado. Incluye anexos, ejemplos, exclusiones, títulos,
condiciones heredadas y relaciones entre partes. El mapa o inventario ayuda a
navegar; nunca reemplaza el original como autoridad.
La ausencia de metainformación del soporte o del proceso es correcta y no genera
hallazgos de pérdida. Su inclusión como contenido sí exige corrección. Las
comprobaciones automáticas de literales no deben forzar a restaurar números de
página, rótulos de extracción u otros elementos ajenos al significado.

Leer también la salida como producto autónomo. Hacer preguntas de uso o pruebas
de interpretación cuando permitan descubrir una dependencia oculta, ambigüedad
o excepción; no exigir un cuestionario serializado a todo documento.

Para reformulación sustantiva no trivial, obtener por defecto un revisor en
contexto separado del autor. Recibe fuente y candidata sin veredicto anticipado
ni justificaciones de autor antes de su primer examen. En trabajo sencillo de
bajo riesgo puede bastar cotejo del autor, declarado como tal. Si falta una
capacidad de revisión necesaria, continuar lo útil y entregar el borrador con
esa garantía pendiente; no presentar autorrevisión como independiente.

Disparadores concretos de esa revisión separada: consecuencia alta; reformulación
de obligaciones, permisos, prohibiciones o excepciones; modalidad o negación
ambigua; conciliación de varias fuentes o autoridades; extracción incierta;
transformación de correspondencias de tablas o diagramas, atribuciones de
conversación o dependencias técnicas; reparación de una relación material.
La longitud sola no decide el riesgo: una instrucción de una línea puede ser
crítica. La mera copia de una tabla sin alterar relaciones no equivale a
reformularla, aunque exige comprobar integridad y contexto.

Separación del autor y lectura ciega a la fuente son propiedades distintas.
Las preguntas con respuestas congeladas se usan cuando se necesita evaluar
comprensión sin fuente, no como pasaporte general de fidelidad. Los controles
negativos prueban el método o una capacidad de revisión nueva o materialmente
alterada; se conservan sus resultados y límites, sin repetirlos por lote o pieza.

El revisor entrega juntos los hallazgos materiales de la versión examinada,
con localizador, diferencia y efecto sobre el significado. No se añade un
supervisor habitual ni una segunda revisión integral por haber terminado los
bloques. Si hubo partición, el cotejo completo incluye las uniones.

### 4. Reparar y entregar

Reparar juntos los hallazgos materiales, preservar lo correcto y comprobar los
cambios con sus relaciones. Si una formulación sigue fallando, conservar el
pasaje sustantivo literal con su contexto necesario antes de seguir iterando
por una mejora marginal de compresión. No declarar resuelto un defecto ilegible.

Reutilizar evidencia anterior sólo si siguen identificadas las fuentes, la
versión cotejada y las partes no afectadas. Un cambio de definición, condición,
título, atribución o recurso puede afectar texto byte-idéntico. Examinar esas
dependencias; si no se puede acotar el efecto, ampliar el cotejo hasta resolverlo.
El diff local y un grafo de referencias declarado no prueban independencia semántica.

La máquina puede aplicar una reparación en una operación que compruebe base,
fuentes, cambios y resultado esperado, conserve la versión anterior y actualice
las vistas derivadas. Si un revisor ya cotejó y aceptó explícitamente una
propuesta exacta, su decisión puede estar condicionada a que se instalen esos
bytes; la igualdad liga la decisión al resultado, no produce un juicio nuevo.
Para ello debe haber examinado el objetivo reconstruido completo en relación
con las fuentes, el contexto y las dependencias afectadas, incluida su lectura
como producto. Conservar base, objetivo y evidencia de ese examen. Si nada
pertinente cambió, no se repite el cotejo ya efectuado; si la revisión sólo
examinó instrucciones de sustitución o el impacto sigue incierto, queda pendiente.
Una propuesta sin aceptación sigue pendiente. Si el revisor escribió el delta,
se declara esa intervención; no se presenta como revisión independiente de su
propia corrección. Un encargo que requiera independencia de cada reparación
necesita otro revisor para ese delta.

Entregar borrador, recursos, alcance, revisión y límites. La publicación usa
`review` y `approve --reviewed` con la autoridad vigente y conserva la referencia
anterior hasta su reemplazo. El hash de revisión KORA puede abarcar más que los
bytes del cuerpo: no intercambiarlo con el SHA del texto. Revisado semánticamente,
mecánicamente válido y publicado son hechos distintos.

## Adaptación sin un segundo procedimiento exhaustivo

| Dificultad observada | Instrumento que aporta evidencia |
|---|---|
| PDF escaneado o extracción dudosa | Contraste con imagen; recuperación de zonas faltantes; localizadores físicos y límites. |
| Tablas o formularios | Cotejo de encabezados, filas, columnas, unidades, opciones y correspondencias; conservar la estructura útil. |
| Condición, excepción o modalidad difícil | Comparar formulaciones completas y probar el caso que distingue ambas lecturas. |
| Documento largo o contexto insuficiente | Partición semántica, cobertura por regiones y cotejo de relaciones entre partes. |
| Fuentes múltiples o ediciones | Identidad y atribución por afirmación o conjunto, conflictos y condiciones de aplicación conservados. |
| Conversación | Atribución, secuencia y estado de propuesta, decisión, compromiso o pendiente. |
| Código, datos o esquema | Recurso funcional conservado y comprobación técnica pertinente; explicarlo no exige ejecutar instrucciones ajenas. |
| Nueva capacidad de revisión | Ensayo con defectos conocidos y observación de sus límites. |

Ningún disparador activa por sí solo inventario exhaustivo, cuestionario ciego,
calibración y varias revisiones globales. La profundidad aumenta donde hay una
dificultad concreta; la cobertura sustantiva sigue siendo completa.

## Integración en KORA y persistencia mínima

- `koraficacion`: entrada única para orientar, localizar, preparar y entregar o
  publicar conocimiento mediante la CLI existente. Remite al criterio de
  transformación sin repetirlo.
- `koraficacion-integral`: única fuente del criterio de conservación, cotejo y
  reparación; instrucciones breves con recursos específicos cargados según
  necesidad. Su helper administra el trabajo, sin exigir el autómata de tres
  formularios por bloque.
- Biblioteca de conocimiento: propietaria de originales, borrador vigente,
  recursos y versiones publicadas. Se reutilizan `intake`, `create`/`revise`,
  `review`, `approve` y `resolve`; no se crea otro catálogo ni ciclo de aprobación.

Un trabajo tiene una candidata vigente y un registro propietario de revisión
con historia. El registro identifica fuentes/representaciones, alcance, versión
del contenido y recursos necesarios, cotejo realizado, exposición real del
revisor, hallazgos, límites y reparaciones. Detalle por región sólo cuando aporta
continuidad. Las explicaciones se conservan como evidencia; las decisiones que
consume software usan campos explícitos, sin interpretar prosa mediante regex.

La biblioteca no debe suponerse capaz de versionar automáticamente cada edición
del borrador: la operación de reparación debe conservar las revisiones previas
que sustentan la cadena de cotejo. Son historia, no candidatas vigentes paralelas.
Los recibos, resúmenes y estado se derivan de ese registro; el operador no copia
hashes, contadores ni declaraciones entre ellos. No se descarta evidencia
necesaria para interpretar una revisión al limpiar temporales.

La mecánica comprueba identidad, integridad, cobertura estructural disponible,
versiones obsoletas, referencias, escritura concurrente y reanudación. Hallazgos
automáticos sobre números o palabras son señales para cotejar, no prueba de
equivalencia ni reglas universales contra reformulación. No genera respuestas,
lecturas ni aprobaciones semánticas a partir de mapeos o valores por defecto.

La transición vincula fuentes congeladas, base, objetivo y recursos revisados.
Si esos insumos cambian, rechaza sin sustituir el borrador ni la referencia
activa. Una interrupción entre contenido y evidencia debe poder recuperarse
sin dos estados vigentes; repetir la misma transición no duplica su historia.
Un cambio posterior de la fuente externa no altera retroactivamente una copia
histórica congelada, aunque puede motivar otra revisión de conocimiento vigente.

El modelo, esfuerzo y canal de delegación pertenecen al runtime y preferencias
del operador. El procedimiento no depende de AGY, Gemini, Luna o un equipo fijo
de agentes. Tampoco incorpora colas o contadores de un corpus particular.

## Qué se retira del recorrido obligatorio

Inventario exhaustivo serializado, mapeo uno-a-uno por unidad, preguntas por cada
bloque, bloques de tamaño fijo, declaraciones positivas repetidas, revisión
global duplicada, rondas de optimización sin beneficio plausible y reportes
manuales que copian estado. La comprobación pertinente conserva su función;
una automatización debe retirar trabajo existente, no añadir un coordinador.

Las identidades y estados antiguos conservan interpretación y recuperación.
Versionar el contrato nuevo; no reinterpretar estados `integral-3` silenciosamente
ni convertir viejos resultados en conformidad nueva. La compatibilidad sirve
para continuar o consultar trabajos existentes y tiene alcance explícito; no
obliga a mantener dos procedimientos normativos en paralelo.

## Realización y aceptación

1. Preparar candidatas de ambos productos mediante `autoria-kora`, coherentes
   con este contrato. Afinar primero instrucciones y recursos necesarios.
2. Realizar un recorrido completo pequeño sobre fuentes sintéticas con el helper
   y la biblioteca: preparar, transformar, revisar, reparar, entregar y reanudar.
   Reutilizar defensas mecánicas existentes; reemplazar los contratos que fuerzan
   formularios innecesarios. Evitar compatibilidad o infraestructura especulativa.
3. Contrastar con el procedimiento vigente antes de afirmar mejora. Ampliar a
   fuente escaneada, tabla, conversación, varias versiones y recurso técnico.
   Usar mismo alcance, entradas y configuración de modelo; contextos separados
   y adjudicación sin conocer el método cuando sea factible. Conservar fallos.
4. Admitir e instalar por los mecanismos KORA, con simulación de instalación y
   comprobación en destino dentro de la autoridad del encargo. Registrar qué se
   probó en Codex y Hermes; la validez de archivos no prueba conducta de ambos.

Criterios de aceptación del diseño realizado:

- Conservar contenido sustantivo y detectar omisiones, adiciones o cambios
  materiales en los casos comparados. Un promedio favorable no compensa perder
  una condición decisiva. Evaluar uso autónomo, además de defectos sembrados.
- Reducir intervenciones manuales, turnos, contexto enviado y/o tiempo hasta
  entrega revisada, con el costo de correcciones incluido. No fijar porcentajes
  de mejora sin línea base ni exigir que todos los indicadores bajen a la vez.
- Un texto ya económico cierra sin fabricar reescritura, inventario o ganancia.
- Un ejemplar con fondo de color, diferencias tipográficas, numeración de página
  y marcas de OCR produce sólo su contenido: esos datos no se inventarían como
  unidades sustantivas, no se preguntan al revisor y no aparecen en la salida ni
  como explicación de su omisión. Una secuencia gráfica y los campos exigidos por
  una regla sí se conservan por su significado.
- Una celda vacía no se convierte en cero; números conservados pero reasignados
  a otra fila se detectan en cotejo semántico. «Reserva o invitación» no se
  acepta como «reserva e invitación» por conservar las mismas palabras.
- Una página sustantiva faltante impide acreditar cobertura completa; un cambio
  de condición compartida obliga a cotejar los consumidores aunque no cambien
  sus bytes. Una conversación conserva propuesta pendiente como tal.
- Cambio de fuente o base obsoleta rechaza la operación sin destruir trabajo;
  repetir una reparación es idempotente; una interrupción permite recuperación.
- Cotejo del autor nunca se exporta como independiente; falta de revisión nunca
  aparece como aceptación. La publicación conserva revisión exacta y autoridad.
- Una consulta puntual que sólo pide una respuesta no activa una transformación
  integral ni un flujo de publicación: prueba vecina contra deriva del método.

Estos ensayos acotan la evidencia; no prueban equivalencia universal ni
acreditan automáticamente un corpus previo. Si retirar un instrumento aumenta
defectos materiales, reintroducir el instrumento para el riesgo demostrado,
sin restaurar por defecto todo el procedimiento anterior.

## Deliberación y fundamento

Dos contextos separados, roles KORA y Steipete, modelo Luna con esfuerzo máximo;
propuestas iniciales sin ver la propuesta de la otra voz. Comparten modelo y
fuentes, por lo que no constituyen diversidad de modelos ni evaluación empírica
del método. Dirección integra y somete la síntesis a crítica de ambas voces.

KORA aporta el contrato semántico y la adaptación por tipo de información.
Steipete aporta el recorrido mínimo, la reutilización del ciclo de biblioteca y
la separación entre mecánica y juicio. Dirección objeta activar todo el aparato
exhaustivo ante longitud/OCR y precisa la revisión condicionada de parches y la
conservación de versiones de borrador. KORA acepta sustituir esa escalada por
instrumentos específicos al riesgo. La crítica final se registra al cerrar la
deliberación a continuación; las propuestas no acreditan implementación.

La crítica produjo tres precisiones incorporadas: cobertura localizada sin
inventario universal; disparadores semánticos de revisión separada; y aceptación
condicionada sólo sobre un objetivo ya cotejado, con contexto y dependencias.
Steipete precisó conservar instantáneas de los borradores revisados, distinguir
declaración del revisor de autorización y proteger la transición contra cambios
de insumos e interrupciones. KORA aceptó el cierre sin repetir un cotejo ya
realizado sobre el objetivo exacto bajo esas condiciones. Se hicieron propuestas,
crítica cruzada sobre la síntesis y un último contraste acotado con KORA.

Hay acuerdo de diseño con esas condiciones y sin disenso material pendiente.
KORA declara confianza media en la suficiencia del recorrido hasta compararlo;
Steipete, alta en simplificar contratos obligatorios y pendiente de medición en
costo y frecuencia de revisión. Dirección adopta la propuesta para implementación
y conserva como hipótesis la mejora de eficiencia y calidad. No se promedian
esas confianzas ni se presenta el acuerdo como prueba de eficacia.

Fuentes locales contrastadas:

- [Contrato de koraficación](../products/kora/koraficacion/content.md).
- [Método integral vigente](../products/kora/koraficacion-integral/content.md) y
  [protocolo](../products/kora/koraficacion-integral/references/protocolo.md).
- [Helper](../products/kora/koraficacion-integral/scripts/integral.py) y
  [pruebas](../tests/test_koraficacion_integral.py).
- [Operación KORA](operacion.md), [biblioteca](../kora/knowledge.py) y
  [autoría de productos](../products/kora/autoria-kora/content.md).


## Implementación y evidencia — 2026-09-15

Ambos productos recorrieron `edit → review → admit` con la candidata
`flujo-20260915`. Revisiones admitidas:

- `koraficacion-integral`: `f6e176cca94cc2729ff8b9a782bf5fadd76389d0a0db57d6cfae7796d0b59ee0`.
- `koraficacion`: `075825fd898fb7b776b3a0458c9cb8ae2ae91c1e8df4eeccce2de9cadd4c71b4`.

La realización añade `scripts/workflow.py`, contrato `integral-4`, al producto
integral y lo hace recorrido por defecto de sus instrucciones. Utiliza el cuerpo
del borrador KORA como salida, conserva snapshots y dictámenes en el trabajo
privado, y permite reparación condicionada a bytes exactos. La biblioteca
conserva su autoridad de revisión y publicación; no se creó otra biblioteca,
cola ni servicio. `integral.py` permanece idéntico para trabajos existentes,
con su protocolo delimitado en `references/compatibilidad-integral-3.md`.

Instalaciones ejecutadas sobre planes revisados, sin conflictos:

- Codex: transacción `0f8a79ffea5a452e91a72e2a9e3876a2`, cinco archivos cambiados
  en `.agents/skills/koraficacion*`.
- Hermes: transacción `75a8b89d13fc4132a19b9fc93c74d56a`, once archivos cambiados
  entre skills globales y perfil `kora`, incluido su manifiesto de distribución.
- SHA-256 de `workflow.py` en producto y las tres copias instaladas:
  `2dd35bc86e0ce7253569d002c74d50b164eb5eb1500caaeb6c723294e824138a`.

Validación mecánica: 56 pruebas de `test_koraficacion_integral`,
`test_koraficacion_fragments`, `test_koraficacion_workflow` y
`test_koraficacion_workflow_recovery` pasan (26,852 s). Las 22 pruebas nuevas
cubren flujo simple, reparaciones, revisiones negativas y supersesión,
independencia declarada, fuentes binarias, insumos obsoletos, idempotencia,
interrupciones y el recorrido hasta publicación de una biblioteca sintética.
Una prueba adicional de exportación pasa desde el helper instalado en Codex;
una de reparación con negativo preservado pasa desde el perfil KORA de Hermes.
La primera selección del nombre de clase para la prueba instalada fue errónea;
se corrigió el comando, sin modificar implementación. `kora_cli.py check` pasa
con 527 objetos activos, 18 archivados y ninguna incidencia. La revisión separada
de código detectó y permitió corregir cuatro defectos antes de admitir:
independencia mal rotulada, aceptación tras negativo sin resolución,
sobrescritura del original mediante alias de ruta y una ventana de recuperación
ante edición ajena. Los escritores externos que no respeten el lock aún tienen
una garantía limitada, explicitada en el protocolo.

Prueba conductual exploratoria: dos contextos Luna max transformaron la misma
fuente sintética, bajo el procedimiento anterior y el nuevo. Los archivos de
entrada, ambas salidas y el control están en
[`tests/fixtures/koraficacion-flujo`](../tests/fixtures/koraficacion-flujo/).
El cotejo de dirección conserva las reglas, alternativas, excepciones,
atribuciones, tabla, incertidumbre y significado funcional de OCR/rojo de ambas
salidas. El nuevo expresa por separado la condición del aviso verbal; el anterior
la agrupa bajo «Unidad cerrada», una presentación menos explícita. Ninguna salida
incorpora las notas de apariencia/extracción como conocimiento. La consulta
vecina atómica se respondió sin crear otro trabajo.

| Observación | Anterior | Nuevo |
|---|---:|---:|
| Operaciones del helper en recorrido | 13 | 7 (8 contando ayuda preliminar) |
| Tiempo informado init→entrega | 182,610 s | 83,791 s |
| Bytes de salida | 720 | 920 |
| Reintentos | 0 | 0 |

Estos tiempos son informes de una ejecución por método, con variación de contexto
y arranque; el agente nuevo tuvo exposición previa al procedimiento anterior,
declarada. El piloto no mide tokens ni acredita una mejora de compresión; la
salida nueva es más larga. Los dictámenes del recorrido fueron del propio autor,
sin atribuirles independencia. La comparación ofrece una señal de menor trámite,
no una estimación de ahorro para un corpus ni una demostración de superioridad.

Control negativo: dirección sembró dos alteraciones en una copia de la salida
nueva (alternativa convertida en conjunción y propuesta convertida en acuerdo).
Un revisor separado de la autoría, con exposición previa sólo al código, recibió
fuente y candidata sin conocer las alteraciones ni otras versiones. Detectó las
dos y explicó sus efectos, emitiendo `repair`; recibo exacto conservado en
`cotejo-control.md`. No se admitió esa copia como conocimiento. Este control
acredita únicamente detección en el caso ensayado, no calibración universal.

Límites pendientes de evaluación empírica: PDFs escaneados y extensos,
extracciones reales, diversidad de formatos/modelos y conducta de Hermes como
agente. Los archivos instalados y la ejecución de su helper están comprobados;
no se afirma recarga automática de sesiones abiertas ni uso efectivo por todo
runtime. El corpus HSC no fue migrado, recontado ni acreditado con este cambio.
