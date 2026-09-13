# Reconstrucción de productos KORA

Fecha: 2026-09-13. **Propuesta de arquitectura y migración; no implementada.**
Base de maquinaria: `695e058f105ad597cd3f85d17da3ac025e7b2ac0`, más las
ediciones locales preexistentes examinadas. Este documento conserva una decisión
propuesta y su fundamento; no gobierna la operación vigente ni mantiene un
catálogo paralelo.

## Dictamen

**Recomiendo reconstruir los contratos de los agentes y métodos como una colección
coherente de 9 agentes y 26 skills, y recomponer selectivamente las síntesis de
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

Los 35 productos propuestos son 24 menos que los 59 activos actuales. Esa cifra
describe la candidata; no mide utilidad ni constituye una cuota. La fusión de
oficios es una hipótesis pendiente de contraste. Si una ruta especializada
pierde profundidad, acceso directo o independencia, se conserva separada.

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

La vigencia impresa tampoco autoriza un retiro automático: el índice HSC conserva
una ratificación D-025BN sobre copias controladas sin sucesor o retiro. Esa
decisión debe mantener fecha, autoridad, alcance y condición, sin inventar una
verificación actual de Drive ni una aplicación institucional observada.
[Índice HSC](/home/felix/kora-knowledge/references/salud/hsc-normativa-hodom-indice/content.md:25).

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
| `director-tecnico-hodom` | Director técnico e integrador HODOM | `director-tecnico-hodom` | `direct-hodom`, `analyze-care-networks` |

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
| `direct-hodom` | Mandato y dependencias → decisión técnica, incremento, evidencia e integración; aceptación institucional y práctica clínica mantienen su autoridad. |
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

Estas doce familias orientan consulta y recomposición. No crean nuevos tipos,
directorios obligatorios ni una cuota de objetos. Los 463 tratamientos
individuales preservan destinos más específicos dentro de ellas.

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
   modos y autoridad independiente. Los tres dominios sanitarios y la dirección
   técnica mantienen responsabilidades distintas.
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
| Fusión de capítulos y borradores con el mismo ID | Conserva las distinciones citables; revisión explícita del contenido elegido y acceso a versiones previas |

La colección estará renovada cuando los contratos admitidos preserven las
funciones necesarias, sus realizaciones independientes carguen lo que prometen y
los casos pertinentes muestren conducta suficiente. La utilidad diferencial sólo
se afirmará donde exista comparación. El dictamen actual es **arquitectura
candidata suficientemente concretada; reconstrucción y validación de productos
pendientes**, con integridad mecánica comprobada en el corpus disponible.
