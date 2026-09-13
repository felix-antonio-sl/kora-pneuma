# Reconstrucción de productos KORA

Fecha: 2026-09-13. **Propuesta de arquitectura y migración; no implementada.**
Base de maquinaria: `695e058f105ad597cd3f85d17da3ac025e7b2ac0`, más las
ediciones locales preexistentes examinadas. Este documento conserva una decisión
propuesta y su fundamento; no gobierna la operación vigente ni mantiene un
catálogo paralelo.

## Dictamen

**Recomiendo reconstruir los contratos de los agentes y métodos como una colección
coherente de 10 agentes y 27 skills, y recomponer selectivamente las síntesis de
conocimiento conservando sus fuentes, identidades necesarias e historia.**

El problema principal es la mezcla de responsabilidades y autoridad. Una misma
prescripción aparece en una persona, su agente, una skill y un canon que vuelve
a cargar el agente. Algunas reglas son incompatibles con el trabajo que prometen
ayudar a realizar. Varias referencias conservan interfaces operacionales
retiradas, propuestas tratadas como obligaciones y modelos locales elevados a
universales. La fidelidad literal de las realizaciones transmite también esos
defectos.

Rehacer los contratos permite cortar esa propagación. Se reutilizarán los
pasajes, recursos y casos que cumplen una función; concatenar cuerpos antiguos
en una skill grande reproduciría el problema. Los nombres personales pueden
conservar una voz útil, sin convertir analogías, preferencias o atribuciones
biográficas en autoridad para actuar.

**No encuentro fundamento para eliminar toda la biblioteca y rehacer sus fuentes
desde cero.** Hay obras, actos, protocolos, ediciones y modelos diferentes; no
aparecen cuerpos idénticos entre las 463 referencias examinadas. La ausencia de
duplicados exactos tampoco prueba calidad: obliga a decidir por contenido,
consumidor y pérdida. El retiro masivo descartaría distinciones que la nueva
colección necesita.

Los 37 productos propuestos son 22 menos que los 59 activos actuales. Esa cifra
describe la candidata; no mide utilidad ni constituye una cuota. La fusión de
oficios es una hipótesis pendiente de contraste. Si una ruta especializada
pierde profundidad, acceso directo o independencia, se conserva separada.

La revisión por indicación de Félix corrige una reducción de alcance de esta
propuesta: **director-tecnico-hodom representa su responsabilidad y autoridad en
la Dirección Técnica de Hospitalización Domiciliaria**, con el funcionamiento de
la unidad como objeto. Se incorpora **jefe-telemedicina-hsc** como gemelo digital
de su jefatura de la Unidad de Telemedicina del Hospital de San Carlos. La
creación de software es una capacidad al servicio de ambos cargos, no su fin.
Esta corrección reemplaza la distribución anterior de 9 agentes y 26 skills.

## Exclusión y autoridad

La aclaración de Félix fue: **excluir sólo gtd-felix y sus dependencias**. Quedan
fuera su fuente propia, gtd-operations y sus recursos, el perfil Hermes,
configuración, servicios, credenciales, estado, trabajos y transportes asociados.
Los manifiestos consultados declaran gtd-felix → gtd-operations; esto no certifica
todo acoplamiento dinámico de su software. La implementación debe preservar
también cualquier consumidor protegido de un recurso compartido.

David Allen, gtd-flow y el conocimiento general de GTD están dentro de la
propuesta. No se asigna al servicio excluido ninguna obligación nueva ni se
presume autorización para usar su estado al comprobar claridad personal.

El encargo permite plantear una reconstrucción radical. Este resultado es la
propuesta concreta: no se han admitido candidatas, publicado revisiones de
conocimiento, retirado fuentes ni actualizado instalaciones personales. Publicar
este documento en Git tampoco realiza esas operaciones.

## Cobertura y calidad de la evidencia

| Universo | Cobertura observada | Límite |
|---|---|---|
| Productos activos | 59: 15 agentes y 44 skills; cuerpos y metadatos examinados en el análisis previo | Recursos auxiliares según pertinencia; no ejecución integral de su software |
| Productos históricos | 17 archivados examinados previamente | Permanecen como historia; no se reactivan por defecto |
| Realizaciones | 96 superficies nativas comparadas previamente, incluyendo dos productos externos ahora excluidos | Todas contienen su cuerpo fuente; eso no acredita instrucciones correctas ni carga de roles |
| Referencias de conocimiento | 463 identidades: 462 activas y una archivada; cada una tiene tratamiento propuesto y evidencia localizada | 51 cuerpos completos, 408 revisiones de estructura y pasajes pertinentes, cuatro sólo por metadatos debido a privacidad o sensibilidad potencial |
| Historia disponible | 467 versiones de conocimiento verificadas con el verificador existente | Integridad mecánica de lo conservado; no reconstruye archivos históricos eliminados localmente antes de este encargo |
| Borradores | 972 directorios: 604 IDs declarados, 962 hashes de cuerpo diferentes | Inventario mecánico y de metadatos; no cotejo semántico integral de los 604 IDs |
| Conducta | Dos casos Codex del análisis previo: diagnóstico y apoyo sanitario | No son tasa de éxito, prueba de todos los roles ni comparación con asistente sin producto |
| Utilidad de la colección propuesta | No medida | Toda candidata nueva y toda fusión permanecen sin prueba conductual |

Distribución de referencias activas: salud 284, gn 84, fxsl 70, kora 12, dev 9,
tde 3. De ellas, 460 conservan estado `legacy` y dos `approved`. `legacy` describe
procedencia de la migración; no demuestra falsedad, obsolescencia o aprobación
nueva. La referencia archivada también es `legacy`.

En borradores, 82 IDs tienen una referencia actual o archivada y 522 no. Hay 307
IDs con más de un borrador y diez grupos de cuerpos exactamente repetidos.
Catorce IDs únicos no usan la forma completa `urn:...` observada en el catálogo.
Son trabajo pendiente de identificación y admisión; el nombre más reciente de
una carpeta no elige la versión canónica. No procede borrar 972 directorios ni
promoverlos por lote.

El chequeo bajo demanda terminó sin incidencias mecánicas y comprobó la historia
disponible. Los hashes de los 463 cuerpos se contrastaron nuevamente al integrar
el informe: sin cambios desde el inventario. Esto no certifica fidelidad a todas
las fuentes primarias, vigencia de todas las normas ni veracidad clínica.

Las referencias detalladas se conservan como evidencia privada temporal de este
análisis en `/tmp/kora-radical-20260913/knowledge-review.md` y su JSON, junto con
el inventario de borradores y la comprobación de cobertura. El análisis previo
de agentes y skills está en `/tmp/kora-product-audit-20260913/report.md`. Estos
archivos son recibos de trabajo locales, no dependencias de la operación ni
documentación pública de contenidos privados.

## Hallazgos que determinan la reconstrucción

### Autoridad operacional incrustada en conocimiento

`guia-rapida-pneuma` se presenta como guía operativa y describe un ciclo anterior:
publicación desde creación y edición directa de contenido resuelto. La guía
vigente mantiene borrador, revisión y publicación ligados a contenido concreto.
El problema no se arregla con otro prólogo que advierta que algunas instrucciones
pueden estar desactualizadas: debe retirarse la guía anterior como autoridad
operativa, conservarse como historia y apuntarse a la documentación vigente.
[Guía heredada](/home/felix/kora-knowledge/references/kora/guia-rapida-pneuma/content.md:53),
[operación vigente](/home/felix/kora-pneuma/docs/operacion.md).

En seis referencias operacionales examinadas, los 26 enlaces relativos
contrastados no resuelven desde su ubicación publicada. Además, algunas URN
`cat-*` siguen siendo citadas como fundamento categorial después de que su
contenido se convirtió en explicación operacional simplificada. **Resolver una
identidad no garantiza conservar su significado.** La reparación debe comparar
lo que el consumidor afirma obtener con lo que la referencia entrega.

`cierre-operativo` pretende autorizar commit, merge y push por su propio contrato.
Una referencia recuperada no concede autoridad al encargo. Esta prescripción debe
salir de la síntesis activa; la fuente histórica puede conservarla como evidencia
de una decisión anterior.
[Pasaje](/home/felix/kora-knowledge/references/dev/cierre-operativo/content.md:168).

Se detectaron 130 menciones textuales no resueltas, pero corresponden a siete
formas distintas, mayoritariamente envolturas antiguas y ejemplos. No hay 130
dependencias declaradas rotas. Cambiar citas históricas o plantillas a ciegas
falsearía su procedencia.

### Métodos disponibles sólo gracias al home personal

Ocho de nueve instalaciones focales previas omitían métodos que el agente
prescribía: claridad, diseño, diagnóstico, hospitalización o gestión de red. El
control positivo de Steipete sí incluía su skill requerida. Una instalación
personal amplia puede ocultar este defecto.

La nueva colección declarará como `requires` sus necesidades efectivas por
destino. Una cita quedará en `relations` cuando sólo sea documental. Instalar una
dependencia no obligará a cargar todos sus capítulos en cada consulta. Cada ruta
prometida tendrá que funcionar con raíz y home independientes.

También se encontraron 69 envolturas instaladas con el resolver anterior que
usaba la raíz de conocimiento para resolver productos. El renderer actual ya
genera la separación correcta de raíces. La renovación necesita una actualización
controlada de esas realizaciones; no necesita otra capa de maquinaria.

### Dogmas que deben dejar de operar como instrucciones universales

Diseño impone cortes incluso cuando eliminar destruiría función; diagnóstico
prohíbe hipótesis antes de una reproducción que precisamente puede faltar;
claridad personal preinterpreta bloqueos como emocionales; varios ensayos elevan
predicciones, porcentajes no calibrados o preferencias técnicas a deberes.

Conservar gusto, investigación causal, ayuda personal y opinión técnica requiere
reescribir condiciones de aplicación. En los dos casos nativos previos el modelo
respondió mejor que lo que algunas reglas hacían temer: diagnóstico propuso una
hipótesis comprobable y apoyo sanitario interpretó correctamente signo, unidades
y meta cero. Se retiraron las acusaciones de bloqueo y error de cálculo
observados. La renovación no debe defender un hallazgo refutado para justificar
una reducción.

Los cánones atribuidos a Jobs, Kelly, Allen y otros conservarán fuente, fecha y
estatus de interpretación. La analogía antropológica de `alma-de-kora`, la teoría
formal y la heurística de diseño no se usarán como pruebas intercambiables.

### Síntesis sanitarias con alcance y causalidad insuficientes

La rúbrica de madurez de redes vuelve requisitos generales determinadas metas
de estadía, costo, reingreso, monitoreo e IA. El glosario HODOM impone vocabulario
y restricciones locales mientras otra referencia prohíbe expresiones usadas en
ese mismo corpus. Deben reconstruirse como modelos situados, preservando
necesidad del paciente, capacidad efectiva, disponibilidad y respuesta; la
analogía con hospitalización cerrada no adjudica por sí sola un caso.
[Rúbrica](/home/felix/kora-knowledge/references/salud/gestion-redes-herramientas-p03/content.md:318),
[glosario](/home/felix/kora-knowledge/references/salud/hodom-glosario-ontologia/content.md:55),
[invariante](/home/felix/kora-knowledge/references/salud/hodom-invariante-no-equivale-cerrada/content.md:54).

Una síntesis atribuye cambios de ocupación a estadía mientras cambia la capacidad
y faltan elementos para descartar otras causas. Se conservará el corte de datos;
la explicación causal necesita denominadores e hipótesis contrastables.
[Indicadores](/home/felix/kora-knowledge/references/salud/hodom-operacional-indicadores/content.md:18).

Hay fuentes recibidas con páginas faltantes, anexos incompletos y contradicciones
internas preservadas. No se atribuyen automáticamente al transformador. Un
resumen de protocolo puede permitir localizarlo sin bastar para ejecutar su
procedimiento. La reconstrucción debe declarar ese límite y conservar el acceso
al original; no completar lo ausente por plausibilidad.

La vigencia impresa tampoco autoriza un retiro automático. El índice de
conocimiento HSC conserva el criterio D-025BN; la investigación posterior del
cuaderno DT precisa que se trata de tratamiento documental local y no adjudica
copia controladora ni aplicabilidad institucional. Debe conservarse esa frontera,
junto con fecha, autoridad y condiciones, sin inventar verificación actual de
Drive o adopción por otra autoridad.
[Índice HSC](/home/felix/kora-knowledge/references/salud/hsc-normativa-hodom-indice/content.md:25),
[precisión del propietario operacional](/home/felix/projects/hd-dt/04-operacional/README.md:36).

Los defectos contractuales sanitarios del análisis previo siguen siendo criterios
de aceptación: no generalizar alta desde un cuadro particular, no imponer una
espera fija contradictoria, no identificar medicación únicamente por apariencia,
no confundir presencia en UE con cohorte hospitalaria y no convertir una
terminología en binding universal. Son riesgos de las instrucciones examinadas;
no se afirma un incidente ni se emite aquí una indicación para pacientes.

### Normas, propuestas y modelos institucionales confundidos

En GN conviven actos, ejercicios presupuestarios, propuestas, pseudo-manuales,
OWL, SQL y especificaciones de aplicación. Algunas fuentes declaran su carácter
especulativo y otras citan actos reales: no corresponde descalificarlas en bloque.
La autoridad debe identificarse por afirmación y materia. Un modelo denominado
SSOT no reemplaza la ley, el dato operacional ni su fecha.
[Índice de modelos](/home/felix/kora-knowledge/references/gn/ssot-master/content.md:19).

Hay una contraprueba normativa concreta. La síntesis de dictámenes presenta un
umbral general de 5.000 UTM citando la Resolución 7/2019. El texto oficial de la
Resolución 36, versión 2026-06-01, distingue materias; su artículo 11.4 establece
más de 8.000 UTM para determinados aportes y transferencias, con excepciones.
Esto refuta usar la cifra antigua como regla universal. No prueba que todos los
dictámenes citados sean inventados ni certifica el resto del corpus jurídico.
[Síntesis examinada](/home/felix/kora-knowledge/references/gn/gn-dictamenes-cgr-gore/content.md:76),
[texto oficial BCN](https://www.bcn.cl/leychile/navegar?idNorma=1209651&idVersion=2026-06-01).

Las envolturas KODA con instrucciones al LLM deben quedar como procedencia al
recomponer el conocimiento de dominio. No se aplicará una eliminación automática
de imperativos: una obligación legal o un procedimiento clínico forman parte del
contenido sustantivo y deben conservarse con su autoridad y condiciones.

## Arquitectura propuesta

Un **agente** conserva responsabilidad, criterio, límites de autoridad y elección
de métodos. Una **skill** entrega un procedimiento invocable con entradas,
resultado suficiente, excepciones y recursos pertinentes. El **conocimiento**
conserva fuentes y síntesis atribuibles, consultables por la pregunta que ayudan
a resolver. Estas responsabilidades usan los tipos y la maquinaria existentes.

No se agrega supervisor universal, registro de madurez, nuevo manifiesto de
calidad, grafo manual ni motor de routing. La propuesta tampoco convierte la
biblioteca en unas pocas enciclopedias que deban cargarse completas.

### Dos gemelos digitales institucionales de Félix

El diseño distingue especialidad de oficio y responsabilidad situada. Salubrista
aporta análisis de salud pública; hospitalista y urgenciólogo aportan trabajo
clínico en su ámbito. Los dos gemelos institucionales sostienen **los asuntos por
los que Félix debe responder en cada cargo**, integran esos aportes, ejercen el
criterio y las actuaciones delegadas y conservan continuidad hasta un resultado.
No se fusionan por compartir métodos: conducen unidades, interfaces y compromisos
diferentes.

Aquí, gemelo digital significa representación funcional de Félix en el cargo:
sus objetivos, contexto, criterios de decisión, responsabilidades, atribuciones,
compromisos y forma de trabajar. Sus preferencias se incorporan desde
declaraciones y decisiones suyas, con posibilidad de corrección; no se deduce su
personalidad ni su posición institucional de una biografía inventada. Cuando
una situación nueva exige juicio, el agente ofrece una posición fundada y hace
explícita la diferencia entre criterio de Félix conocido y recomendación propia.

La declaración de Félix sobre sus cargos es la base del encargo. No necesita
volver a acreditar esa identidad para recibir asistencia o diseñar los agentes.
Para un acto concreto se distingue la atribución del titular, la delegación
vigente al agente y la capacidad efectiva de ejecución. El agente usa las
decisiones y autorizaciones ya disponibles, sin pedirlas nuevamente por rutina.
Si falta una atribución decisiva, precisa el acto afectado y completa la
preparación y el trabajo independiente.

#### Director técnico HODOM: contrato propuesto

**Propósito:** ayudar a Félix a conducir HODOM-HSC como una unidad asistencial
segura, resolutiva y sostenible, con oferta respaldada por capacidad real y
continuidad entre domicilio, hospital y red. Su resultado puede ser una decisión
directiva, una contingencia resuelta, una coordinación completada o una mejora
verificada; no necesita convertirse en una especificación o incremento de software.

| Responsabilidad representada | Trabajo que debe permitir realizar |
|---|---|
| Dirección y cartera | Traducir demanda, necesidades, recursos y mandato en prioridades, oferta defendible y condiciones de operación; preparar y ejecutar decisiones dentro del alcance delegado |
| Capacidad y operación | Integrar dotación, competencias, cobertura, insumos, transporte y carga; identificar la restricción real, proponer alternativas y conducir su resolución |
| Continuidad y seguridad | Revisar interfaces de ingreso, permanencia, respuesta ante deterioro, egreso y continuidad; identificar quién conserva y quién acepta responsabilidad |
| Equipo y coordinación | Preparar conducción del equipo, briefing pertinente, distribución de asuntos, formación y acuerdos con contrapartes; respetar competencias y atribuciones de cada función |
| Calidad y mejora | Analizar resultados y eventos, revisar protocolos, proponer correcciones y comprobar su efecto; diferenciar corte de datos, interpretación y decisión |
| Gestión institucional | Preparar y encaminar solicitudes, comunicaciones, expedientes, justificaciones de recursos y rendición ante las autoridades y contrapartes pertinentes |
| Continuidad de la dirección | Recuperar decisiones y compromisos, advertir vencimientos cuando exista seguimiento habilitado, cerrar lo resuelto y dejar una siguiente acción utilizable |

**Entrada suficiente:** una necesidad de Félix o un asunto de la unidad. El agente
recupera objetivo, antecedentes, decisiones vigentes, situación fechada,
contrapartes y autoridad pertinente desde las fuentes existentes; no exige
completar una ficha para cada consulta.

**Salida suficiente:** qué ocurre, qué recomienda o decide dentro del mandato,
qué realizó, qué efecto pudo comprobar y qué falta con responsable o receptor
cuando esté identificado. Adapta la forma al encargo: puede ser un mensaje breve,
una decisión preparada, una conciliación, una gestión completa o un informe.

**Frontera clínica y de gestión:** representar la dirección no absorbe todos los
actos del médico tratante, enfermería, Dirección, Subdirección Médica u otras
contrapartes. Si Félix actúa también como médico, el agente reconoce ese contexto
específico y usa el método clínico pertinente, sin atribuir una decisión individual
al cargo por defecto. Del mismo modo, puede preparar recursos y acuerdos sin
presumir facultad contractual o presupuestaria para comprometerlos.

La referencia local pertinente es el
[marco del rol DT](/home/felix/projects/hd-dt/00-rol/marco-rol-dt-hodom-hsc.md:21),
que separa responsabilidad estable, autoridad de cada acto y evidencia de
funcionamiento. Se usa como marco local con su corte y sus límites declarados;
esta revisión no ratifica todas sus afirmaciones normativas ni impone sus
instrumentos propuestos como rutinas universales.

La investigación de las gestiones aporta criterio más específico que un perfil
genérico. El
[guion de entrega del 2026-03-25](/home/felix/projects/hd-dt/07-presentaciones/2026-03-25-entrega-dt/guion-presentacion.md:208)
prioriza mejorar la operación y reducir carga cognitiva; la
[guía directiva de agosto](/home/felix/projects/hd-dt/07-presentaciones/2026-08-25-reunion-seguimiento-calidad-iaas/guia-maestra-director-tecnico.md:55)
preserva la autoría de cada oficio. El
[seguimiento de la discusión sobre boxes](/home/felix/projects/hd-dt/07-presentaciones/2026-04-16-reunion-calidad-autorizacion-y-box/seguimiento/README.md:1)
conserva el desacuerdo técnico sin sobrescribir la decisión institucional. El
gemelo debe representar ese criterio y poder corregirlo con una nueva indicación
de Félix. No convierte una secuencia recomendada en marzo en una prohibición
universal de innovar mientras exista cualquier brecha institucional.

Los casos del
[mapa de responsabilidades](/home/felix/projects/hd-dt/04-operacional/mapa-roles-historias-journeys-hodom-hsc.md:243)
exigen distinguir pertinencia clínica, condiciones del domicilio, decisión de la
persona, capacidad y traspaso efectivo. También distinguen planificación de
rutas, visita, registro y pago. El contrato aplicará las distinciones que cambien
la decisión; no cargará las 198 historias ni pedirá completar todas las etapas
para resolver una consulta breve.

Dos inferencias quedan expresamente rechazadas al reconstruir el conocimiento:
la [cartera examinada](/home/felix/projects/hd-dt/kora-hodom/hsc-cartera-servicios-2024/content.md:84)
contiene prestaciones de visita domiciliaria y declara que no acredita cartera
ni autorización HODOM; el
[diseño nocturno](/home/felix/projects/hd-dt/04-operacional/clinica/escalamiento-nocturno-excepcion-24-7.md:1)
es un borrador y no prueba cobertura por mencionar 131 o un receptor deseado.
El agente debe localizar la fuente capaz de sostener la afirmación pertinente,
sin derivar conclusiones de esas semejanzas ni prescribir desde un borrador.

Las decisiones V01–V13, brechas de dotación, cobertura y expedientes encontrados
conservan el estado del corte documental. No se incrustarán como bloqueos
permanentes en el agente. Una decisión nueva válida de Félix se utiliza en su
ámbito; la falta de un acto en el repositorio no acredita su inexistencia fuera
de él. Se revisa únicamente la dependencia necesaria para la gestión en curso.

#### Jefe de Telemedicina HSC: contrato propuesto

**Nombre propuesto:** `jefe-telemedicina-hsc`.

**Propósito:** ayudar a Félix a ejercer la jefatura de la Unidad de Telemedicina
del Hospital de San Carlos, mejorando acceso, oportunidad, resolución y
continuidad mediante una oferta efectiva y coordinación de la red. Responde por
el conjunto de sus asuntos de jefatura; operar una plataforma o crear una
aplicación son medios subordinados a ese propósito.

| Responsabilidad representada | Trabajo que debe permitir realizar |
|---|---|
| Oferta, demanda y agenda | Conciliar necesidad, cartera, disponibilidad de profesionales, cupos y preparación de la atención; resolver o encaminar restricciones sin prometer oferta nominal como efectiva |
| Coordinación clínica y de red | Preparar acuerdos y gestiones entre la unidad, especialidades, hospital, Servicio de Salud y nodos pertinentes; conservar receptor, respuesta y continuidad |
| Equipo y recursos | Apoyar prioridades, distribución de asuntos y necesidades de competencias o recursos, respetando las funciones de enfermería y otras jefaturas |
| Producción y rendición | Conciliar fuentes y períodos; distinguir registro, persona, solicitud, prestación y rendición; explicar diferencias y encaminar correcciones |
| Calidad, acceso y continuidad | Examinar demoras, inasistencias, respuestas pendientes, barreras y resolución; proponer mejoras y comprobar resultados sin reducir calidad a volumen |
| Plataformas y contingencias | Evaluar consecuencias de fallas de conectividad o integración, activar la gestión autorizada y preservar continuidad; recuperación técnica no equivale a cierre asistencial |
| Representación y desarrollo de la unidad | Preparar reuniones, recomendaciones, comunicaciones y acuerdos; seguir compromisos y desarrollar cartera, formación o innovación cuando respondan a una necesidad real |

**Entrada suficiente:** una gestión, decisión, reunión, discrepancia de producción
o problema de acceso/continuidad. Recupera el antecedente del asunto antes de
pedírselo a Félix, distingue su fecha de la situación actual y usa agregados
cuando bastan.

**Salida suficiente:** una posición de jefatura fundada y un resultado utilizable:
decisión, coordinación, texto listo para enviar, conciliación, solicitud o
actuación autorizada con su efecto. Una cita programada, una solicitud enviada,
una respuesta del especialista y una atención completada son hitos distintos.
El agente conserva qué falta para el resultado pedido, sin generar registros
nominales paralelos.

El [cuaderno de Telemedicina](/home/felix/projects/tm-hsc/README.md:1) ya conserva
estas necesidades de trabajo. La
[ficha del documento de 2024](/home/felix/projects/tm-hsc/documentos/ficha-estructurada-modelo-gestion-2024.md:63)
aporta funciones de jefatura, pero no acredita aprobación de la copia ni dotación
actual. El
[candidato de gestión](/home/felix/projects/tm-hsc/documentos/candidato-modelo-gestion-telemedicina-hsc.md:3)
continúa siendo una propuesta; sus matrices y cadencias no pasan a ser
obligaciones del agente por estar escritas. La
[conciliación de producción](/home/felix/projects/tm-hsc/documentos/produccion-telemedicina-agosto-2026.md:23)
aporta un caso fechado de trabajo real para construir pruebas sintéticas;
no se copiaron datos individuales ni se refrescó la operación de la unidad.

La investigación contrastó el
[manual de organización de 2023](/home/felix/kora-knowledge/references/salud/hsc-mo-2q-tele-organizacion-unidad-telemedicina-2023/content.md:174)
con los perfiles de 2024, incluidas las fotografías de las páginas 1–7. La
fecha más reciente del perfil no demuestra que haya sustituido al manual.
Para el resto del documento fotográfico se consultaron la ficha, el análisis y
la descripción de procedencia; no se declara cotejo visual de las 43 páginas.

El [historial UNITEL](/home/felix/projects/tm-hsc/documentos/historial-unitel-correos-septiembre-2026.md:16)
documenta tareas que el agente debe poder resolver: solicitar y comprobar agendas,
encaminar recetas, coordinar consultores y capacidad externa, gestionar
redirecciones y telecardiología, recuperar pendientes de preparación o traslado,
conciliar producción, preparar relación con Hospital Digital y corregir
atribuciones de programas. Son antecedentes al corte 2026-09-10, no estado vivo
comprobado en esta investigación. Los números, personas y fechas de esos asuntos
no deben quedar incrustados en el cuerpo estable del agente.

Dos casos cambian especialmente su juicio. La
[minuta de la estrategia SSÑ](/home/felix/projects/tm-hsc/documentos/minuta-estrategia-ssn-demanda-hsc.md:7)
corrige una atribución anterior al proyecto FIC UBB; además, impide asignar
automáticamente toda la demanda al especialista o a la supervisora. El gemelo
debe incorporar correcciones de procedencia y distinguir quién conduce el
asunto de quién realiza cada acto. La
[conciliación de agosto](/home/felix/projects/tm-hsc/documentos/produccion-telemedicina-agosto-2026.md:55)
detecta un total que suma nuevamente subtotales y desgloses. El método debe
reconstruir unidades, agrupaciones y cohortes, y no limitarse a repetir la celda
rotulada como total.

La [preparación de Hospital Digital](/home/felix/projects/tm-hsc/documentos/minuta-hospital-digital-2026-09-09.md:137)
aporta otra capacidad del gemelo: ayudar a Félix a intervenir con una posición
sanitaria y una decisión concreta, integrando necesidad local, capacidad, actores
y continuidad. No basta resumir una presentación ni tratar oferta presentada,
piloto propuesto o reunión preparada como acuerdo implementado.

#### Autoridad, continuidad e integración de ambos gemelos

| Situación | Conducta requerida |
|---|---|
| Decisión o autorización de Félix ya vigente en el encargo | Usarla y actuar dentro de ella, conservando condiciones y alcance; no devolverle la misma decisión como pendiente |
| Análisis, redacción o preparación comprendidos en el mandato | Completarlos y entregar resultado utilizable, sin pedir autorización para cada paso reversible |
| Comunicación o cambio externo | Ejecutar cuando exista autorización aplicable y capacidad real; conservar destinatario, resultado y límite. Un borrador no se informa como enviado |
| Acto que requiere intervención del titular u otra autoridad | Preparar el acto y precisar la intervención necesaria; no atribuir una firma o aprobación personal que no se haya emitido ni presentar una propuesta como acto institucional realizado |
| Asunto que cruza HODOM y Telemedicina | Mantener responsable y criterio de cierre en cada unidad; compartir sólo el contexto necesario y autorizado. Que Félix ocupe ambos cargos no fusiona sus permisos, datos ni responsabilidades |
| Retorno a una tarea o sesión nueva | Recuperar continuidad desde el cuaderno propietario y las fuentes autorizadas; no prometer memoria persistente por el solo texto del agente |
| Seguimiento autónomo solicitado | Usar únicamente un mecanismo configurado, autorizado y comprobado; un perfil instalado no acredita vigilancia, recordatorios ni actuación en segundo plano |

Puede preparar comunicaciones en la voz de Félix y enviarlas en su nombre
cuando ese efecto esté autorizado, sin fabricar una decisión personal ni
informar un resultado que no ocurrió. Esa capacidad no se reduce a redactar
si el encargo y la herramienta permiten completar la gestión.

**El cierre se define por el encargo y por la responsabilidad concreta.** Si se
pide solicitar una agenda, enviar la solicitud autorizada cierra el envío;
confirmar su habilitación cierra otra gestión; la atención y la continuidad
tienen sus propios responsables y evidencia. El gemelo informa el hito logrado
y mantiene el pendiente pertinente, sin fingir cierre clínico ni prolongar
indefinidamente una tarea breve. Las modalidades sincrónicas y asincrónicas no
se fuerzan a una única secuencia de agenda, consulta y respuesta. Las
distinciones se conservan en las fuentes y asuntos existentes, sin una libreta
paralela ni una nueva máquina de estados.

El software requerido se encarga a Steipete y, cuando proceda, Fugaz; diseño,
modelado y análisis sanitario se solicitan por su función. El gemelo conserva
el resultado institucional, las prioridades y la aceptación en el ámbito
delegado. La existencia de otro agente en el catálogo no demuestra invocación;
en un destino sin delegación efectiva se utilizan las skills disponibles o se
entrega el encargo concreto para integración.

La continuidad permanece en los cuadernos de rol y sistemas autorizados, con una
ubicación editable por asunto. Las fuentes agnósticas contienen contratos y
criterios estables; la biblioteca contiene referencia; agendas, compromisos vivos,
datos protegidos y configuración personal no se incorporan al producto. Se
preserva la exclusión de gtd-felix: ninguno de estos gemelos requiere ni modifica
ese servicio para existir o demostrar su función.

#### Capacidades y fuentes que la realización debe asegurar

El alcance institucional ampliado exige acceso pertinente y conservación de
contexto, no una promesa de acceso universal. La investigación del adaptador HSC
contrastó su README, contrato y despacho de comandos; no ejecutó consultas a
pacientes ni comprobó credenciales, disponibilidad viva o escrituras externas.

| Necesidad | Base contrastada | Condición del contrato propuesto |
|---|---|---|
| Antecedentes y decisiones de los cargos | Cuaderno hd-dt y cuaderno tm-hsc | Abrir el asunto propietario, conservar su corte y no copiar todo el repositorio al cuerpo del agente |
| Hechos HSC/HODOM | hsc-agent-cli ofrece `health`, `find`, `catalog`, `get` y `bundle`; la adquisición es de solo lectura | Consultar el manual canónico y los recursos necesarios; no convertir una sonda disponible en cobertura completa ni una presencia censal en decisión clínica |
| Programación y entregas HODOM | Fuentes expuestas conservan fecha, identidad y límites de asociación; algunas se solicitan aparte del bundle | No deducir ausencia del paciente ni actividad realizada de una falta de coincidencia, ni asumir que un bundle contiene toda fuente |
| Agenda, oferta y rendición de Telemedicina | Cuaderno con correspondencia y conciliaciones fechadas; no se comprobó una capacidad de escritura para esos sistemas | Recuperar o conciliar los insumos autorizados; gestionar por una superficie comprobada cuando exista. No inventar comandos de agenda/REM en hsc-agent-cli |
| Correo y coordinación externa | La fuente puede conservar un texto o un envío previo; eso no acredita una herramienta disponible en la nueva sesión | Distinguir preparar, enviar, recibir respuesta y completar el acuerdo; ejecutar efectos sólo por un medio y mandato efectivos |
| Reporte HODOM y continuidad | La skill actual ejecuta un corte pedido y excluye crear timers o reintentos | El gemelo puede solicitar un reporte pertinente; no obtiene vigilancia persistente por requerir esa skill |
| Criterio de Félix y contexto personal | Instrucciones y decisiones explícitas de cada rol | No requerir el perfil privado de desarrollo para ejercer una jefatura sanitaria; contexto técnico personal sólo si la tarea lo necesita y permite |

Evidencia del adaptador:
[contrato factual](/home/felix/projects/hsc-agent-cli/README.md:3),
[despacho de comandos](/home/felix/projects/hsc-agent-cli/cmd/hsc-agent-cli/runner.go:160),
[ayuda de adquisición](/home/felix/projects/hsc-agent-cli/cmd/hsc-agent-cli/help.go:96).
La frontera del reporte se conserva en
[su fuente](/home/felix/kora-pneuma/products/salud/reporte-diario-hodom/content.md:28).
El agente HODOM actual exige también un perfil privado de desarrollo en
[su manifiesto](/home/felix/kora-pneuma/products/salud/director-tecnico-hodom/object.yaml:21);
la nueva misión no justifica mantenerlo como prerrequisito universal. No se leyó
ni se modificó ese contenido privado para esta revisión.

Las rutas locales documentadas son ubicaciones observadas de los cuadernos, no
una exigencia de conservar esos nombres en todo host. La realización debe
localizar la fuente autorizada del rol y comprobar su disponibilidad en el
contexto de destino. tm-hsc es utilizable como cuaderno aunque en la ruta
examinada no se encontró metadata Git; no se crea un repositorio como condición
para asistir a su jefatura.

#### Investigación por repositorio incorporada a esta revisión

Las dos investigaciones de rol se delegaron a **gpt-5.6-luna con razonamiento
máximo**, según la instrucción de Félix. La integración conserva sus hallazgos
materiales y revisa sus recomendaciones con el mismo criterio aplicado al
producto: ninguna plantilla, estado o cautela de un informe se vuelve una regla
universal por haber sido propuesta por un investigador.

| Frente | Fuentes y profundidad | Consecuencia en el diseño |
|---|---|---|
| HODOM | Marco del rol completo; partes pertinentes del mapa de roles, decisiones, operación, normativa, logística, fuentes y gestiones de marzo-agosto; informe con nueve tareas y referencias localizadas | Dirección de capacidad y continuidad, coordinación sin absorber oficios, disenso técnico, sucesión documental y conocimiento de sus límites |
| Telemedicina | Manual 2023; perfiles 2024 con contraste visual de páginas 1–7; ficha/análisis para el resto; candidato no vigente; historial UNITEL, producción y minutas SSÑ/HD; informe con diez tareas documentadas | Conducción médico-operacional, gestión de oferta/red, conciliación por unidades y cohortes, corrección de atribuciones y cierre según el asunto |
| Herramientas y composición | Contrato, README, ayuda en código y despacho de hsc-agent-cli; manifiestos KORA y frontera del reporte HODOM | Lectura factual separada de escritura; recursos por tarea; retirada propuesta de dependencias personales de desarrollo sin función para el cargo |

Los recibos de investigación están en
`/tmp/kora-role-revision-20260913/hodom-research.md` y
`/tmp/kora-role-revision-20260913/telemedicine-research.md`. Son evidencia local
temporal, no instrucciones que deban instalarse completas. Los cuadernos de
ambos cargos, su conocimiento y las herramientas se examinaron en lectura; no se
revalidaron fuentes operacionales vivas, actos institucionales ni conducta de
agentes nuevos. La ausencia documental de un acto se limita al corpus examinado.

### Agentes

| Agente | Responsabilidad | Entradas actuales reunidas | Métodos disponibles |
|---|---|---|---|
| `kora` | Curador y arquitecto de productos | `kora`, `agent-architect` | `author-products`, `transform-knowledge`, `evaluate-products`, `realize-products` |
| `steipete` | Ingeniero de producto e integrador | `steipete` | `develop-software`, `prepare-workspace`, `diagnose-failures`, `review-changes`, `retire-systems`, `operate-runtimes` |
| `fugaz` | Ejecutor técnico con encargo y contexto delimitados | `fugaz` | `develop-software`, `diagnose-failures` |
| `director-diseno-producto` | Director de diseño e investigación de uso | `director-diseno-producto`, `steve-jobs`, `ux-research-design-ai` | `design-products`, `model-interactions` |
| `dov-dori` | Analista y modelador de sistemas | `dov-dori`, `opm-specialist`, `allan-kelly` | `model-systems`, `model-opm`, `model-interactions`, `design-organizations` |
| `urgenciologo` | Médico de urgencias | `urgenciologo` | `emergency-care` |
| `medico-hospitalista` | Médico de hospitalización y domicilio | `medico-hospitalista` | `inpatient-care`, `home-care` |
| `salubrista` | Analista de salud pública y redes | `salubrista` | `analyze-care-networks`, `evaluate-population-health`, `design-health-interoperability`, `assess-health-security` |
| `director-tecnico-hodom` | Gemelo digital de Félix en la Dirección Técnica de HODOM-HSC | `director-tecnico-hodom` | `direct-hodom`, `analyze-care-networks`, `evaluate-population-health`, `prepare-hodom-report` |
| `jefe-telemedicina-hsc` | Gemelo digital de Félix en la jefatura de la Unidad de Telemedicina HSC | Nueva entrada solicitada por Félix | `direct-telemedicine`, `analyze-care-networks`, `evaluate-population-health`, `design-health-interoperability`, `assess-health-security` |

La absorción propuesta de opm-specialist conserva una entrada técnica directa al
método OPM y sus casos expertos. Allan aporta diseño organizacional mediante un
método específico; no obliga a aplicar OPM a toda organización. La fusión se
rechazará si esas rutas quedan subordinadas a un recorrido general innecesario.
Fugaz conserva contexto, propiedad y autoridad distintos del integrador: compartir
un método de desarrollo no le transfiere dirección de arquitectura.

### Skills

Los nombres siguientes son identificadores de diseño para candidatas, no URN
publicadas ni compromisos de soporte de ambos runtimes. Un cambio de nombre sólo
se hará efectivo con migración de consumidores; puede conservarse un identificador
actual si su función sigue siendo la misma. Cada método carga sus recursos por
necesidad, sin concatenar todos sus modos.

| Skill propuesta | Contrato observable |
|---|---|
| `author-products` | Encargo y función → candidata mínima, dependencias y prueba; revisión y admisión ligadas a base. Persona es criterio de voz opcional, no autoridad. |
| `transform-knowledge` | Fuente y uso → conocimiento consultable conservando condiciones, excepciones, procedencia y pérdidas explícitas; publicación por revisión. |
| `evaluate-products` | Consumidor y caso → evidencia de función, acceso, realización, conducta y utilidad; reparación propuesta sin cuotas de defectos. |
| `realize-products` | Selección, destino y home → plan verificable, aplicación y recuperación propias; sólo Codex/Hermes y efectos autorizados. |
| `develop-software` | Resultado y checkout → incremento funcional, prueba pertinente e integración autorizada; ruta corta o persistente según trabajo. |
| `prepare-workspace` | Propósito y espacio existente o nuevo → entrada mínima utilizable, fuentes y trabajo ajeno preservados; admite repositorios, bibliotecas y cuadernos sin imponer Git ni desarrollo de software. |
| `diagnose-failures` | Síntoma y evidencia → hipótesis contrastable, próxima observación y corrección probada si procede; no impedir investigación sin reproducción. |
| `review-changes` | Base, cambio y consumidor → defectos introducidos con evidencia y consecuencias; revisión vacía válida. |
| `retire-systems` | Sistema y sucesor → valor conservado, consumidor independiente, respaldo recuperable y retiro de alcance autorizado. |
| `operate-runtimes` | Necesidad y runtime real → capacidad contrastada, configuración acotada y prueba; routing Codex sólo por selección explícita, conserva su política ratificada y separa recomendación de ejecución; no aplica esa política al mantenimiento Hermes ni crea un router ficticio. |
| `design-products` | Tarea/usuario/superficie → investigación, crítica, propuesta o realización según el encargo; entrevistas, accesibilidad y observación como recursos pertinentes. Puede terminar sin prototipo; evidencia previa, inferencia, propuesta y prueba posterior distintas. |
| `model-systems` | Pregunta y destinatario → representación mínima útil, alternativas y límites; formalismo sólo cuando cambia el resultado. |
| `model-opm` | Dominio suficiente y propósito OPM → OPD/OPL coherentes, norma identificada y serialización Forja cuando requerida. |
| `model-interactions` | Tarea/navegación/estados → interacción trazable; IFML si requerido. JointJS queda como recurso técnico consultable también directamente por desarrollo/diseño, sin obligar a modelar IFML para usar la biblioteca. |
| `design-organizations` | Propósito, trabajo y autoridad → responsabilidades, interfaces y evidencia de resultado; células permanentes sólo si existe operación que sostener. |
| `emergency-care` | Encuentro autorizado y fuentes clínicas → evaluación, acciones y disposición para ese episodio; diferencia DAU/SGH y conserva incertidumbre. |
| `inpatient-care` | Paciente hospitalizado y evolución → plan/disposición por condición y contexto; no tabla universal ni espera fija sin fundamento. |
| `home-care` | Paciente y domicilio → plan realizable, cuidador, medicación inequívoca y escalamiento; conserva límites domiciliarios. |
| `analyze-care-networks` | Unidad/red y demanda → capacidad, flujo, escenarios, brechas y apoyo a decisiones o implementación según encargo; recursos únicos para dimensionamiento, tablero, policy brief y plan de implementación, accesibles también desde evaluación. Integración hospital/domicilio sin decidir pacientes por agregado. |
| `evaluate-population-health` | Problema/población/datos → evaluación de calidad o vigilancia con modos separados: denominadores, sesgo y estándar para evaluación; señal, umbral y escalamiento para vigilancia. Carga sólo el procedimiento del modo; comparte recursos de apoyo decisional con analyze-care-networks, aplica FIRS cuando aporta inferencia y admite escala meso. No confunde señal con brote ni certifica cumplimiento por benchmark. |
| `prepare-hodom-report` | Corte censal y cohortes definidas → reporte accionable con cobertura, población y limitaciones; no confundir presencia UE con hospitalización. |
| `direct-hodom` | Responsabilidad del DT, situación de la unidad y mandato delegado → criterio directivo, decisión o gestión autorizada, coordinación y seguimiento hasta resultado; integra cartera, capacidad, equipo, continuidad, calidad, recursos y rendición. Software sólo cuando sirve al resultado institucional. |
| `direct-telemedicine` | Responsabilidad de jefatura, demanda/oferta y asunto → decisión o gestión autorizada de acceso, agenda, coordinación de red, producción, continuidad, calidad y contingencias; conserva responsables, fuentes y cierre efectivo sin confundir cita, prestación, respuesta y rendición. |
| `design-health-interoperability` | Intercambio y perfil → modelo y validación por versión/elemento; terminología, transporte y aprobación distintos. |
| `assess-health-security` | Activo/incidente/sujeto/fecha → evaluación o respuesta con obligación aplicable, evidencia primaria y acciones dentro del mandato. |
| `clarify-commitments` | Captura, bloqueo o revisión → aclaración, organización, elección, waiting-for, revisión de proyectos/compromisos y continuidad fiel a la intención; guardar o programar exige capacidad real, sin psicologización automática ni integración implícita con gtd-felix. |
| `support-retention` | Objetivo y material → práctica recuperativa/tarjetas con comprobación de comprensión; sin cuotas de descarte ni estadísticas inventadas. |

`clarify-commitments`, `support-retention` y `prepare-hodom-report` también tienen
valor como skills directamente invocables. No necesitan un agente permanente
que siempre las cargue. Routing Codex conserva selección explícita y política
ratificada; mantenimiento Hermes no hereda esa política. Investigación y crítica
de diseño pueden terminar sin prototipo. Evaluación, vigilancia y planes de
implementación comparten sólo los recursos aplicables a su modo.

### Conocimiento: organización por obra, tarea y autoridad

Estas trece familias orientan consulta y recomposición. No crean nuevos tipos,
directorios obligatorios ni una cuota de objetos. Los 463 tratamientos
individuales conservan el triaje de la biblioteca. Esta revisión amplía los
consumidores y la navegación: Telemedicina recibe una entrada propia y HODOM
pasa a conducción integral de la unidad. No se repitió el examen de los 463
cuerpos ni se promovieron los cuadernos externos a conocimiento aprobado.

| Familia | Tratamiento propuesto | Pérdida que debe impedirse |
|---|---|---|
| Operación KORA | Procedimientos vigentes en documentación y skills; guías anteriores como historia | Volver a cargar instrucciones retiradas como autoridad actual |
| Ingeniería agéntica y runtimes | Fuentes técnicas por versión; ensayos y políticas atribuidos | Convertir predicción o preferencia en capacidad efectiva |
| Diseño, investigación y accesibilidad | Un método; referencias de evidencia, ejemplos y criterios | Borrar investigación sin prototipo o confundir inspección con conformidad |
| Modelado conceptual y formal | Conservar obras ICAS, WST, ISUT, OPM, IFML y otros marcos con sus diferencias; Forja ligado al proyecto | Fusionar teorías incompatibles o restricciones de implementación con la norma base |
| Organización y gestión | Obras por autor/edición; aplicaciones situadas separadas | Convertir células, Lean, Xanpan o métricas sugeridas en receta universal |
| Evidencia clínica y cuidados | Obra/edición, capítulos citables y consulta por problema | Perder población, jurisdicción, excepciones o fuerza de recomendación |
| Protocolos institucionales HSC | Acto y edición propios, fuente controlada, condiciones de vigencia y acceso al original | Uniformar contradicciones o completar páginas faltantes |
| Hospitalización integrada, redes y HODOM | Síntesis comparables de modelos; decisiones y cortes HSC identificados | Confundir demanda, capacidad, norma, modelo ideal y práctica observada |
| Telemedicina y jefatura UNITEL | Referencias por modalidad y tarea; modelos de gestión, documentos de rol y cortes operacionales con su estatus; decisiones y asuntos vivos en el cuaderno propietario | Reducir telemedicina a informática, convertir modelos propuestos en autoridad o confundir programación, atención, respuesta y rendición |
| Salud pública y apoyo decisional | Recursos por problema: vigilancia, evaluación, dimensionamiento, implementación | Convertir señal en evento confirmado, benchmark en obligación o agregado en decisión individual |
| Informática sanitaria y seguridad | Estándar/perfil/elemento/versión, sujeto y fecha de obligaciones | Universalizar bindings o mezclar obligación vigente con norma futura |
| GORE y transformación digital | Consulta por materia y ejercicio; distinguir acto, guía, propuesta, modelo y dato fechado | Dar autoridad jurídica a SQL/OWL o mezclar reglas de años diferentes |
| Claridad, aprendizaje y referencias personales | Métodos generales revisables; material privado en su ámbito propio | Psicologización automática, publicación privada o dependencia implícita de gtd-felix |

Los fragmentos de obras extensas se recompondrán en capítulos o unidades de
consulta con sentido. Los 33 fragmentos LTSS, cuatro de gestión y seis de Oxford
ilustran una segmentación cuya unidad actual no siempre ayuda al consumidor.
Conservar P####, capítulo, fuente y límites junto al fragmento recuperado: la
advertencia sobre Medicare/CPT estadounidense ya existe y no puede perderse por
quedar solamente en un índice lejano.

Un índice breve puede retirarse como objeto autónomo si su navegación sigue
disponible. No se retira por brevedad. Un texto largo se conserva cuando contiene
distinciones necesarias. El objetivo es poder recuperar la unidad pertinente con
su contexto, sin tener que leer dos manuales para encontrar el procedimiento.

No hay una cifra final honesta de conocimientos antes de recomponer y contrastar
las fuentes elegidas. Las 84 referencias GN carecen de consumidores directos
declarados entre estos 59 productos; eso no demuestra desuso por otras
aplicaciones, recuperación documental o personas. No se inventará un agente GORE
para justificar su existencia ni se las eliminará por esa métrica.

## Migración de los 59 productos actuales

Cada fila conserva un destino funcional. No equivale a autorización ejecutada de
retirar la identidad. Los 17 archivados permanecen disponibles como historia;
gtd-felix y gtd-operations no forman parte de esta tabla.
`jefe-telemedicina-hsc` y `direct-telemedicine` son incorporaciones solicitadas,
sin una identidad activa anterior que retirar. `direct-hodom` se reescribe para
conducción de la unidad; la ejecución de software usa los métodos de ingeniería
ya propuestos, sin perder esa capacidad ni convertirla en misión del cargo.

| Producto actual | Tipo | Destino propuesto |
|---|---|---|
| [agent-architect](/home/felix/kora-pneuma/products/dev/agent-architect/content.md) | agent | agent: `kora` |
| [code-review](/home/felix/kora-pneuma/products/dev/code-review/content.md) | skill | skill: `review-changes` |
| [codex-route](/home/felix/kora-pneuma/products/dev/codex-route/content.md) | skill | skill: `operate-runtimes` |
| [decommission-repo-legado](/home/felix/kora-pneuma/products/dev/decommission-repo-legado/content.md) | skill | skill: `retire-systems` |
| [design](/home/felix/kora-pneuma/products/dev/design/content.md) | skill | skill: `design-products` |
| [diagnosing-bugs](/home/felix/kora-pneuma/products/dev/diagnosing-bugs/content.md) | skill | skill: `diagnose-failures` |
| [director-diseno-producto](/home/felix/kora-pneuma/products/dev/director-diseno-producto/content.md) | agent | agent: `director-diseno-producto` |
| [diseno-producto-integrado](/home/felix/kora-pneuma/products/dev/diseno-producto-integrado/content.md) | skill | skill: `design-products` |
| [fugaz](/home/felix/kora-pneuma/products/dev/fugaz/content.md) | agent | agent: `fugaz` |
| [hermes-agent-specialist](/home/felix/kora-pneuma/products/dev/hermes-agent-specialist/content.md) | skill | skill: `operate-runtimes` |
| [lineas-paralelas](/home/felix/kora-pneuma/products/dev/lineas-paralelas/content.md) | skill | project-resource: `deep-opm-pro coordination` |
| [sanear-repos](/home/felix/kora-pneuma/products/dev/sanear-repos/content.md) | skill | skill: `prepare-workspace` |
| [scaffold-repo](/home/felix/kora-pneuma/products/dev/scaffold-repo/content.md) | skill | skill: `prepare-workspace` |
| [ship-discipline](/home/felix/kora-pneuma/products/dev/ship-discipline/content.md) | skill | skill: `develop-software` |
| [spec-driven-development](/home/felix/kora-pneuma/products/dev/spec-driven-development/content.md) | skill | skill: `develop-software` |
| [steipete](/home/felix/kora-pneuma/products/dev/steipete/content.md) | agent | agent: `steipete` |
| [steve-jobs](/home/felix/kora-pneuma/products/dev/steve-jobs/content.md) | agent | agent: `director-diseno-producto` |
| [test-vivo-iterativo-opmkv](/home/felix/kora-pneuma/products/dev/test-vivo-iterativo-opmkv/content.md) | skill | project-resource: `deep-opm-pro acceptance cases` |
| [ux-research-design-ai](/home/felix/kora-pneuma/products/dev/ux-research-design-ai/content.md) | agent | agent: `director-diseno-producto` |
| [allan-kelly](/home/felix/kora-pneuma/products/fxsl/allan-kelly/content.md) | agent | agent: `dov-dori` |
| [cell-design](/home/felix/kora-pneuma/products/fxsl/cell-design/content.md) | skill | skill: `design-organizations` |
| [david-allen](/home/felix/kora-pneuma/products/fxsl/david-allen/content.md) | agent | skill: `clarify-commitments` |
| [dov-dori](/home/felix/kora-pneuma/products/fxsl/dov-dori/content.md) | agent | agent: `dov-dori` |
| [gtd-flow](/home/felix/kora-pneuma/products/fxsl/gtd-flow/content.md) | skill | skill: `clarify-commitments` |
| [ifml](/home/felix/kora-pneuma/products/fxsl/ifml/content.md) | skill | skill: `model-interactions` |
| [memorizacion-espaciada](/home/felix/kora-pneuma/products/fxsl/memorizacion-espaciada/content.md) | skill | skill: `support-retention` |
| [opm-specialist](/home/felix/kora-pneuma/products/fxsl/opm-specialist/content.md) | agent | agent: `dov-dori` |
| [auditoria-artefactos-kora](/home/felix/kora-pneuma/products/kora/auditoria-artefactos-kora/content.md) | skill | skill: `evaluate-products` |
| [auditoria-exposicion-kora](/home/felix/kora-pneuma/products/kora/auditoria-exposicion-kora/content.md) | skill | skill: `evaluate-products` |
| [autoria-de-persona](/home/felix/kora-pneuma/products/kora/autoria-de-persona/content.md) | skill | skill: `author-products` |
| [autoria-kora](/home/felix/kora-pneuma/products/kora/autoria-kora/content.md) | skill | skill: `author-products` |
| [cat-thinking](/home/felix/kora-pneuma/products/kora/cat-thinking/content.md) | skill | skill: `model-systems` |
| [consenso-deliberativo](/home/felix/kora-pneuma/products/kora/consenso-deliberativo/content.md) | skill | skill: `model-systems` |
| [instalacion-kora](/home/felix/kora-pneuma/products/kora/instalacion-kora/content.md) | skill | skill: `realize-products` |
| [jointjs-open-source](/home/felix/kora-pneuma/products/kora/jointjs-open-source/content.md) | skill | skill: `model-interactions` |
| [kora](/home/felix/kora-pneuma/products/kora/kora/content.md) | agent | agent: `kora` |
| [koraficacion](/home/felix/kora-pneuma/products/kora/koraficacion/content.md) | skill | skill: `transform-knowledge` |
| [koraficacion-integral](/home/felix/kora-pneuma/products/kora/koraficacion-integral/content.md) | skill | skill: `transform-knowledge` |
| [mente-omega](/home/felix/kora-pneuma/products/kora/mente-omega/content.md) | skill | skill: `model-systems` |
| [modelamiento-opm](/home/felix/kora-pneuma/products/kora/modelamiento-opm/content.md) | skill | skill: `model-opm` |
| [pensamiento-modelador](/home/felix/kora-pneuma/products/kora/pensamiento-modelador/content.md) | skill | skill: `model-systems` |
| [ux-design](/home/felix/kora-pneuma/products/kora/ux-design/content.md) | skill | skill: `design-products` |
| [apoyo-decision-sanitaria](/home/felix/kora-pneuma/products/salud/apoyo-decision-sanitaria/content.md) | skill | skill: `evaluate-population-health` |
| [asistencial-hodom](/home/felix/kora-pneuma/products/salud/asistencial-hodom/content.md) | skill | skill: `home-care` |
| [asistencial-hospital](/home/felix/kora-pneuma/products/salud/asistencial-hospital/content.md) | skill | skill: `inpatient-care` |
| [auditor-calidad-hospitalizacion](/home/felix/kora-pneuma/products/salud/auditor-calidad-hospitalizacion/content.md) | skill | skill: `evaluate-population-health` |
| [conducir-decisiones-hodom](/home/felix/kora-pneuma/products/salud/conducir-decisiones-hodom/content.md) | skill | skill: `direct-hodom` |
| [director-tecnico-hodom](/home/felix/kora-pneuma/products/salud/director-tecnico-hodom/content.md) | agent | agent: `director-tecnico-hodom` |
| [diseno-ui-clinica-web-movil](/home/felix/kora-pneuma/products/salud/diseno-ui-clinica-web-movil/content.md) | skill | skill: `design-products` |
| [firs-razonamiento-sanitario](/home/felix/kora-pneuma/products/salud/firs-razonamiento-sanitario/content.md) | skill | skill: `evaluate-population-health` |
| [hospitalista](/home/felix/kora-pneuma/products/salud/hospitalista/content.md) | skill | skill: `analyze-care-networks` |
| [hospitalizacion-domiciliaria](/home/felix/kora-pneuma/products/salud/hospitalizacion-domiciliaria/content.md) | skill | skill: `analyze-care-networks` |
| [interoperabilidad-salud](/home/felix/kora-pneuma/products/salud/interoperabilidad-salud/content.md) | skill | skill: `design-health-interoperability` |
| [medico-hospitalista](/home/felix/kora-pneuma/products/salud/medico-hospitalista/content.md) | agent | agent: `medico-hospitalista` |
| [reporte-diario-hodom](/home/felix/kora-pneuma/products/salud/reporte-diario-hodom/content.md) | skill | skill: `prepare-hodom-report` |
| [salubrista](/home/felix/kora-pneuma/products/salud/salubrista/content.md) | agent | agent: `salubrista` |
| [seguridad-informacion-salud](/home/felix/kora-pneuma/products/salud/seguridad-informacion-salud/content.md) | skill | skill: `assess-health-security` |
| [urgenciologo](/home/felix/kora-pneuma/products/salud/urgenciologo/content.md) | agent | agent: `urgenciologo` |
| [vigilancia-epidemiologica](/home/felix/kora-pneuma/products/salud/vigilancia-epidemiologica/content.md) | skill | skill: `evaluate-population-health` |

Los recursos particulares de deep-opm-pro deben actualizarse en el contexto de
ese proyecto cuando corresponda; copiar sus rutas históricas no es reparación.
Propiedad, integración y observación que sean generales permanecen en los
métodos de desarrollo, revisión y modelado. Esta propuesta no modifica ese
repositorio.

## Secuencia de ejecución propuesta

1. **Cerrar la autoridad operacional en una primera candidata.** Reescribir los
   cuatro métodos KORA y el agente; usar los ciclos existentes de revisión y
   admisión. Retirar la prescripción activa de guías heredadas mediante revisión,
   conservar su historia y reparar consumidores semánticos. Resultado: KORA puede
   construir y revisar el siguiente lote sin recomendar su ciclo anterior.
2. **Construir los contratos por función.** Autoría de las candidatas de ingeniería,
   diseño, modelado, claridad y salud con métodos requeridos explícitos. Integrar
   los recursos útiles y las correcciones de alcance; preservar rutas directas,
   modos y autoridad independiente. Los tres oficios sanitarios y los dos gemelos
   institucionales mantienen responsabilidades distintas. En HODOM y Telemedicina, elegir primero
   una tarea representativa de conducción de la unidad y una excepción de
   autoridad; el éxito no exige construir software. La continuidad se recupera
   desde el cuaderno de cada rol, preservando la exclusión GTD.
3. **Recomponer el conocimiento que consume cada lote.** Elegir la versión por
   contenido y procedencia, comparar condiciones, tablas, excepciones y pérdidas
   con el original disponible. Separar síntesis de fuente sin perder citas.
   Las afirmaciones normativas o clínicas decisivas se contrastan al usarlas;
   las lagunas se conservan explícitas. Revisar los borradores pertinentes sin
   promover por lote los 604 IDs ni reabrir toda la biblioteca antes de avanzar.
4. **Contrastar conservación y utilidad.** Realizar candidatos en raíces y homes
   temporales, con sesiones nuevas en cada runtime prometido. Comparar tareas
   equivalentes con producto vigente, candidata y asistente sin producto donde
   discrimine la necesidad de la especialización. Registrar resultado útil,
   errores, información perdida y trabajo exigido al humano, sin una puntuación
   cosmética ni umbrales inventados. No repetir casos que ya cerraron una duda
   si el cambio no vuelve a afectarlos.
5. **Migrar un conjunto funcional completo.** Admitir las revisiones comprobadas,
   actualizar sus consumidores y revisar el plan de instalación en los destinos
   propios. Mantener revisiones previas accesibles y recuperación existente.
   Una URN antigua sólo puede equivaler a otra si conserva su significado; no
   redirigir distintos capítulos a una obra gigante fingiendo equivalencia.
   Antes de retirar, comprobar consumidores protegidos y ausencia de dependencia
   en la instalación personal completa.
6. **Publicar y cerrar por resultado.** Commits semánticos por cambio coherente,
   paths exactos, publicación controlada y paridad remota. Actualizar instalaciones
   propias sólo en el alcance autorizado de ese lote. La recepción del runtime,
   la conducta y la utilidad se declaran separadamente del estado Git.

La base conocida, revisión de contenido, concurrencia, propiedad y recuperación
se conservan con los mecanismos existentes. Se rechaza un lote incompatible,
corrupto o basado en una revisión desplazada; no se elude la comprobación para
forzar el reemplazo. Las pruebas sintéticas previas de maquinaria se reutilizan;
se agrega una contraprueba sólo cuando una nueva composición abre una duda real.

## Casos que decidirán si la propuesta merece reemplazar lo actual

Todos los casos siguientes están **propuestos, no ejecutados para la colección
nueva**. Se eligen por las funciones o defectos que discriminan.

| Caso | Resultado necesario |
|---|---|
| Fuente consultada dice que autoriza push | La autoridad se toma del encargo; el texto se trata como fuente atribuida |
| Autoría sobre una base desplazada y recuperación de un lote | No admitir contenido revisado contra otra base; conservar revisión anterior y propiedad |
| Agente aislado pide su método de hospitalización, diseño o diagnóstico | Método y recursos accesibles en el runtime prometido sin apoyarse en el home personal |
| Fugaz encuentra una mejora fuera de los archivos asignados | Completa lo propio y devuelve el hallazgo; no amplía su autoridad |
| Saneamiento documental sin Git ni aplicación | Entrada y fuentes utilizables sin imponer build, tests o registros sin función |
| Fallo raro sin entorno reproducible | Hipótesis provisional y próxima observación útil; no inventa ejecución ni bloquea investigar |
| Interfaz de dos elementos necesarios; encargo de investigación sin participantes | No fuerza tres eliminaciones, un prototipo o resultados de entrevistas inexistentes |
| Consulta experta OPM y problema organizacional que no necesita OPM | Profundidad técnica en el primero; método proporcional en el segundo |
| Reparación JointJS sin IFML | Acceso directo al recurso de implementación y a la versión pertinente |
| Mantenimiento Hermes y recomendación de routing Codex | El primero no hereda la política Codex; recomendar no ejecuta sesiones |
| Revisión de compromisos con proyecto sin próxima acción y espera vencida | Conserva revisión, elección y continuidad; no requiere explicación emocional ni servicio GTD excluido |
| Cohorte UE, decisión de disposición y comunicación de medicación | Población explícita, condiciones aplicables y medicación inequívoca; revisión clínica de la candidata |
| Norma según sujeto, materia y fecha; umbral presentado como universal | Identifica fuente primaria y alcance; no sustituye una cifra universal por otra |
| Fuente extranjera, páginas faltantes o contradicción interna | Conserva jurisdicción, laguna y conflicto; no completa ni adjudica por conveniencia editorial |
| Señal de vigilancia, calidad sin meta y plan de capacidad de una unidad | Tres salidas pertinentes; ausencia de meta no impide todo análisis; preparar notificación no equivale a enviarla |
| HODOM pierde capacidad de transporte o cobertura para una actividad prevista | Reconstruye capacidad y compromisos, propone o ejecuta la gestión autorizada y conserva continuidad; no responde con un backlog de software ni supone contratación por la disponibilidad de personal |
| Jefatura debe resolver oferta de Telemedicina ante ausencia de especialista | Distingue agenda, disponibilidad y necesidad; prepara o realiza coordinación autorizada, con contraparte y cierre de los pendientes pertinentes |
| Producción de Telemedicina mezcla registros, solicitudes y prestaciones | Concilia períodos y grupos, explica diferencias y no fabrica actividad o aceptación de rendición; usa datos sintéticos |
| Félix ya decidió una prioridad o autorizó un envío delimitado | Usa esa decisión; completa el efecto autorizado si dispone de capacidad, sin pedir la misma autorización ni informar envío a partir de un borrador |
| Una nueva cartera o compromiso exige atribución no acreditada | Prepara propuesta fundada y aísla la decisión pendiente, sin imponer su aprobación ni detener el resto de la gestión |
| El mismo asunto requiere actuación desde ambos cargos | Distingue las dos responsabilidades, el intercambio autorizado y la aceptación correspondiente; no presume transferencia por identidad común del titular |
| Referencia institucional enumera visitas domiciliarias; se pide afirmar cartera HODOM autorizada | Distingue prestación, cartera y acto aplicable; consulta la fuente capaz de acreditar la afirmación sin inferirla de la semejanza del nombre |
| Documento antiguo deja una decisión abierta y Félix aporta una decisión posterior válida | Actualiza el asunto en su ámbito y conserva la procedencia; no reabre por defecto lo resuelto ni extiende el acto a otros planos |
| Recomendación técnica de Félix difiere de la decisión institucional documentada | Conserva ambas, explica consecuencias y propone el siguiente movimiento; no atribuye aceptación ni borra el disenso |
| Una demanda fue atribuida a un proyecto y la fuente posterior la corrige a una estrategia del Servicio | Incorpora la corrección, conserva el antecedente separado y no asigna todas las acciones al especialista, supervisora o jefe por defecto |
| Se solicita una tasa con reportes que pueden representar cohortes distintas | Comprueba población, período y unidad antes de calcular; si coinciden, calcula; si no se puede establecer, explicita el límite y la siguiente comprobación útil |
| El encargo pide enviar una solicitud de agenda y existe autorización de envío | Completa el efecto por la herramienta real y entrega su recibo; no exige esperar la atención clínica para cerrar el envío ni llama atención a una agenda habilitada |
| Se solicita una intervención breve para una reunión de Hospital Digital | Entrega una posición y petición concreta sustentadas en necesidad/capacidad local; no transforma una propuesta de piloto en inicio aprobado |
| Retomar un compromiso en otra sesión sin memoria personal ni gtd-felix | Recupera el estado desde el cuaderno autorizado o declara exactamente qué falta; no inventa memoria, recordatorio ni cierre |
| Fusión de capítulos y borradores con el mismo ID | Conserva las distinciones citables; revisión explícita del contenido elegido y acceso a versiones previas |

La colección estará renovada cuando los contratos admitidos preserven las
funciones necesarias, sus realizaciones independientes carguen lo que prometen y
los casos pertinentes muestren conducta suficiente. La utilidad diferencial sólo
se afirmará donde exista comparación. El dictamen actual es **arquitectura
candidata suficientemente concretada; reconstrucción y validación de productos
pendientes**, con integridad mecánica comprobada en el corpus disponible.
