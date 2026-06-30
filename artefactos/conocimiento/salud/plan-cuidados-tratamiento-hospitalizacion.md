---
urn: urn:salud:kb:plan-cuidados-tratamiento-hospitalizacion
nombre: plan-cuidados-tratamiento-hospitalizacion
version: 1.0.0
estado: publicado
descripcion: "Modelo documental integrado de plan de cuidados y tratamiento en hospitalizacion cerrada y domiciliaria (HODOM): seis columnas como lazo de control, dotacion en dos anillos y gatillos de escalamiento, para registro clinico chileno."
fuente: "Koraficado del documento del operador 'Estructura integrada de Plan de Cuidados + Tratamiento en Hospitalizacion' (2026-06-19), plantilla para registro medico-sanitario chileno (es-CL); fuente humana externa, sin sha256. FS=100% por prueba acida, sin descartes de alcance. Perfil fuente-ya-densa (la masa son tablas clinicas: carne incompresible); CR aproximado 1.0, sin grasa significativa eliminable; la metadata de procedencia explica que el total no baje. Telegrafizacion y dedup aplicadas a la prosa; tablas preservadas integras."
autor: FS
creado: 2026-06-19
lang: es
tags: [plan-de-cuidados, tratamiento, hospitalizacion, hodom, nanda-noc-nic, dos-anillos, registro-clinico-chile, interconsulta, escalamiento]
familia: nota
---

# Plan de Cuidados y Tratamiento Integrado en Hospitalización

Plantilla reutilizable para el registro médico-sanitario chileno (es-CL).
Aplica a hospitalización cerrada y a Hospitalización Domiciliaria (HODOM /
HOSAD / HaH).

## Idea rectora

Un plan es un **lazo de control con objetivo declarado**, no una lista de
indicaciones: cada fila lleva su propio criterio de revisión —continuar,
ajustar, escalar o cerrar—. La integración de cuidados y tratamiento usa **una
sola lista de problemas común**; cada problema aparece **una vez**, con sus dos
lecturas:

- **Tratamiento** — actúa sobre la enfermedad (autoría médica).
- **Cuidado** — actúa sobre la respuesta de la persona a la enfermedad y a la
  hospitalización (autoría de enfermería; lenguaje NANDA-NOC-NIC).

Son ejes que se cruzan, no una jerarquía: ninguno subsume al otro.

## Dotación: dos anillos de recurso humano

| | Anillo 1 — Dotación de la unidad | Anillo 2 — Acceso por interconsulta / derivación |
|---|---|---|
| Roles | Médico (tratante / becado), Enfermera/o, TENS, Kinesiólogo/a, Fonoaudiólogo/a | Otras especialidades médicas, Nutricionista, Químico farmacéutico clínico, Psicólogo/a, Terapeuta ocupacional, Matrón/a, etc. |
| Disponibilidad | Día a día; ejecutan a pie de cama / en domicilio | No de planta; bajo solicitud |
| Acceso | Indicación / plan directo | Interconsulta (apoyo sin mover al paciente) o derivación / traslado (cambia de unidad / establecimiento) |
| ¿Puede ser "Responsable" de una fila? | Sí — siempre | No — su aporte se modela como fila de "solicitar interconsulta / derivación", responsable = médico de la unidad |

**Principio operativo:** el responsable de ejecución de toda fila es un rol del
Anillo 1. Cuando se necesita el Anillo 2, la fila no lo nombra como responsable:
se crea una acción de **solicitar interconsulta o derivación**, cuyo responsable
es el médico de la unidad que la solicita, y cuyo resultado **retorna a la
unidad** para que el Anillo 1 lo ejecute o lo integre al plan.

## Las seis columnas (mínima y suficiente)

| # | Columna | Qué contiene |
|---|---------|--------------|
| 1 | Problema / Dx | Problema activo. Diagnóstico médico (CIE-10) y/o etiqueta de enfermería (NANDA). Integra la lectura terapéutica y la de cuidado. Marca origen del dato: documentado / referido / observado / inferencia. |
| 2 | Objetivo / Resultado (NOC) + plazo | Estado observable y medible a alcanzar: objetivo terapéutico o resultado NOC, con indicador y valor diana. |
| 3 | Intervención / Tratamiento (NIC + médico) | El acto. Tratamiento: fármaco con indicación – dosis – vía – frecuencia – duración (producto de conciliación de medicamentos), con contraindicaciones/precauciones en línea. Cuidado: intervención NIC. Dosis específicas → guía vigente / QF clínico; no inventar. |
| 4 | Frecuencia / Parámetros a monitorear | Cada cuánto se ejecuta y qué se vigila: signos vitales, balance, escalas, RAM. |
| 5 | Responsable (Anillo 1) + Temporalidad | Responsable siempre del Anillo 1. Si requiere Anillo 2 → "solicitar interconsulta a [X] / derivar a [X]", responsable = médico de la unidad, resultado retorna. Temporalidad: inicio, turno/frecuencia, vigencia. |
| 6 | Criterio de evaluación / cierre + gatillos | Umbral medible que dispara la decisión; es a la vez el monitoreo. Gatillos escalonados: (a) ajuste interno por la unidad; (b) interconsulta (Anillo 2 sin mover al paciente); (c) derivación / traslado o escalamiento a UPC/UCI (el paciente sale; en HODOM → SAMU 131). |

**Por qué no más ni menos columnas:** "Diagnóstico" vive en *Problema*; el
lenguaje (terapéutico vs NANDA) lo determina el eje del problema; "estado
activo/resuelto" es consecuencia del *Criterio de cierre* (se fecha la fila); el
"monitoreo" es la columna 6; la "contraindicación" va inline en *Intervención*.
Quitar cualquier columna rompe el lazo de control o la integración; agregar
cualquiera duplica.

## Plantilla vacía

| Problema / Dx (CIE-10 / NANDA) | Objetivo / Resultado (NOC) + plazo | Intervención / Tratamiento (NIC + médico) | Frecuencia / Parámetros a monitorear | Responsable (Anillo 1) + Temporalidad | Criterio de evaluación / cierre + gatillos (a) interno / (b) interconsulta / (c) derivación-traslado |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Instructivo de llenado

1. **Una fila por problema activo.** No repetir el problema entre médico y
   enfermería: un problema, dos ejes integrados en la misma fila o en filas
   hermanas claramente etiquetadas.
2. **Columna 1:** codificar en CIE-10 lo médico y NANDA para lo de enfermería.
   Anotar el origen del dato.
3. **Columna 2:** meta medible y con plazo. Si no se puede medir, no es meta.
4. **Columna 3:** no inventar dosis → remitir a guía vigente / QF clínico.
   Contraindicaciones inline.
5. **Columna 5:** responsable siempre Anillo 1. ¿Se necesita al Anillo 2? Crear
   una fila/acción de "solicitar interconsulta/derivación", responsable = médico
   de la unidad.
6. **Columna 6:** definir los tres gatillos. El gatillo (c) debe decir
   explícitamente a dónde sale el paciente: UPC/UCI/otro establecimiento; SAMU
   131 en HODOM.
7. **Revisión diaria:** en la evolución SOAP se recorre toda la tabla; la
   columna 6 es el "A" (análisis del día) y las columnas 3-5 son el "P" (plan
   del día).

## Ejemplo: mujer 78 años, NAC (CIE-10 J18.9) + IC crónica + HTA

Fármacos y dosis ilustrativos; la selección y dosis se ajustan a guía vigente /
protocolo institucional y a la función renal (vía QF clínico). No constituye
prescripción para un paciente real.

| Problema / Dx | Objetivo + plazo | Intervención (NIC + médico) | Frecuencia / Monitoreo | Responsable (Anillo 1) + Temporalidad | Criterio / gatillos |
|---|---|---|---|---|---|
| NAC (J18.9) [documentado: Rx + clínica] / NANDA *Deterioro del intercambio gaseoso* | SpO2 ≥ 92% aire ambiente a 48-72 h; afebril 48 h; descenso de PCR | ATB empírico según guía/protocolo (dosis y ajuste renal → QF vía interconsulta); O2 para SpO2 ≥ 92%; antipirético | SV c/turno; SpO2; T° c/6 h; balance hídrico | Médico (Rx, ATB, O2) + Enfermera (administración, SV) + TENS (control SV, registro, confort). Revisión en visita diaria | Cierre: afebril + SpO2 estable + tolerancia VO. (a) ajuste de O2/antipirético por la unidad. (b) interconsulta microbiología/infectología si no responde a 72 h. (c) SpO2 < 90% con O2, FR > 30, deterioro de conciencia → escalar a UPC/UCI |
| Riesgo de aspiración por disfagia en AM con NAC [observado: tos al deglutir] / NANDA *Riesgo de aspiración* | Deglución segura; vía/consistencia segura definida en 24 h; cero eventos de aspiración | Evaluación clínica de deglución; prueba de consistencias; recomendación de textura + espesante; técnicas de deglución segura; educación a paciente/cuidador y enfermería | Reevaluar cada visita; vigilar tos/atragantamiento, voz húmeda, SpO2 al comer | Fonoaudiólogo/a (evaluación y manejo de disfagia, plan de textura, técnicas) + Enfermera/TENS (cumplen indicación en alimentación). Inicio en 24 h | Cierre: deglución segura sostenida. (a) ajuste de consistencia por fonoaudiólogo/a. (b) interconsulta a nutricionista para adecuación de dieta espesada. (c) aspiración con compromiso respiratorio → escalar |
| Riesgo de desacondicionamiento / TVP por reposo + IC [inferencia clínica] / NANDA *Deterioro de la movilidad física* | Movilización progresiva; sin TVP; tolerancia a sedestación/bipedestación en 72 h | Kinesioterapia respiratoria (higiene bronquial, reexpansión) + movilización precoz (sedestación, marcha asistida) + profilaxis de TVP según protocolo | Sesión diaria; tolerancia al esfuerzo, SpO2 y FC al ejercicio; signos de TVP | Kinesiólogo/a (KTR + movilización) + TENS (apoyo en traslados) + Enfermera (profilaxis indicada). Sesión diaria | Cierre: movilidad funcional recuperada. (a) ajuste de carga por kinesiólogo/a. (b) interconsulta a terapia ocupacional si déficit funcional para AVD persiste. (c) sospecha de TVP/TEP → escalar y derivar |
| IC crónica (riesgo de descompensación) [documentado] / NANDA *Exceso de volumen de líquidos* | Euvolemia; peso estable; sin signos congestivos en 72 h | Manejo de diuréticos y fármacos de IC (dosis → guía/QF); restricción hídrica/sodio según indicación | Peso diario; balance; edema; PA; función renal y electrolitos seriados | Médico (ajuste farmacológico) + Enfermera (balance, peso, SV) + TENS (registro). Revisión diaria | Cierre: euvolemia estable. (a) ajuste de diurético por la unidad. (b) interconsulta a cardiología si descompensación que no responde / arritmia nueva (responsable: médico; retorna a la unidad). (c) EPA, hipotensión sintomática → escalar a UPC/UCI |
| Polifarmacia + función renal límite [documentado] / NANDA *Conocimiento deficiente sobre régimen terapéutico* | Esquema farmacológico conciliado, seguro y ajustado a función renal en 48 h | Conciliación de medicamentos por la unidad; solicitar interconsulta a QF clínico (interacciones, ajuste renal); educación al paciente/cuidador | Revisar listado en cada visita; vigilar RAM; función renal | Médico (concilia y solicita interconsulta) + Enfermera (pesquisa y registra RAM en hoja de enfermería). Inicio en 48 h | Cierre: esquema conciliado y validado. (a) la unidad concilia lo evidente. (b) interconsulta a QF + nutrición (responsable: médico; retorna). (c) RAM grave / falla renal aguda → escalar |

**Lectura del modelo:** kinesiólogo/a y fonoaudiólogo/a son responsables reales
(Anillo 1). Cardiología, QF, nutrición y TO aparecen solo como gatillo (b) de
interconsulta o (c) derivación, con el médico de la unidad como responsable de
solicitarla y del retorno a la unidad.

## Variante HODOM (Hospitalización Domiciliaria)

Mismas seis columnas + **cuidador co-ejecutor** del Anillo 1, que ejecuta lo
delegado entre visitas y **no sustituye** al profesional. La dotación de la
unidad visita el domicilio; el Anillo 2 sigue siendo interconsulta/derivación;
el escalamiento que saca al paciente de casa activa **SAMU 131**.

**Triple elegibilidad HODOM** (verificar antes de aceptar o mantener): (1)
estabilidad clínica; (2) domicilio y cuidador aptos; (3) ruta factible de
reingreso/escalamiento (SAMU 131 + servicio receptor coordinado). Si falla
cualquiera de las tres, no se ingresa o se reevalúa el alta de HODOM.

| Problema / Dx | Objetivo + plazo | Intervención (NIC + médico) | Frecuencia / Parámetros | Responsable (Anillo 1) + cuidador co-ejecutor | Criterio / gatillos + SAMU 131 |
|---|---|---|---|---|---|
| NAC en domicilio (J18.9) + IC + HTA [referido: más cansada hoy] | SpO2 ≥ 92%; afebril; tolerancia VO sostenida | ATB VO según guía (dosis → guía/QF); O2 domiciliario si indicado; antipirético | Visita médica/enfermería programada; cuidador: SpO2 y T° 3×/día, registra | Médico (plan, ATB, disposición) + Enfermera (visita, educa) + TENS. Cuidador: administra fármacos, mide SpO2/T° | (a) ajuste de O2/antipirético en visita. (b) interconsulta QF clínico (ajuste renal) — médico solicita, retorna. (c) SpO2 < 90% con O2, FR > 30, conciencia alterada → activar SAMU 131 + reingreso a servicio receptor coordinado |
| Riesgo de aspiración / disfagia en domicilio | Deglución segura en casa; cero aspiraciones | Evaluación de deglución en domicilio; plan de textura + espesante; educación al cuidador para alimentación segura | Reevaluar en visita; cuidador vigila tos/atragantamiento al comer | Fonoaudiólogo/a (evalúa, fija plan, visita) + Enfermera. Cuidador: prepara consistencia indicada, posición segura | (a) ajuste de consistencia por fonoaudiólogo/a. (b) interconsulta nutricionista. (c) atragantamiento con cianosis/apnea → SAMU 131 |

### Anexo del cuidador (lenguaje no experto + teach-back + ruta)

- **Qué hacer:** "Dele los remedios a las horas marcadas. Mídale el oxígeno y la
  temperatura 3 veces al día y anótelo. Para comer, siéntela derecha y use la
  comida con el espesante."
- **Cuándo llamar a la unidad:** "Si la nota más cansada, con fiebre que no baja,
  o tose mucho al comer."
- **Cuándo llamar al 131 (SAMU):** "Si se pone morada, le cuesta mucho respirar,
  no responde bien, o se atora y no puede respirar — llame al 131 y avise a la
  unidad."
- **Teach-back:** el cuidador repite con sus palabras qué mide, cuándo llama a la
  unidad y cuándo al 131. Registrar que comprendió.
- **Ruta de reingreso:** SAMU 131 → servicio receptor coordinado (origen HODOM,
  responsable médico de la unidad, próximo contacto definido).

## Integración con el registro clínico chileno

- **Evolución (SOAP):** la tabla es el P del SOAP; cada fila se evoluciona a
  diario. El A compara contra el Objetivo (col. 2) y aplica el Criterio (col. 6);
  el P recoge las intervenciones (col. 3-5). Las solicitudes de Anillo 2 se
  documentan como interconsulta / derivación en la ficha y su respuesta retorna
  al P.
- **Indicaciones médicas:** lo del Anillo 1 baja a la hoja de indicaciones
  (fármacos → dosis por guía/QF; O2; KTR; plan de deglución; movilización). La
  interconsulta/derivación se registra como indicación de solicitud, responsable
  médico.
- **Hoja de enfermería / RAM:** enfermera y TENS registran SV, balance, peso,
  cumplimiento de NIC y RAM; la pesquisa de RAM gatilla (b) hacia QF clínico.
- **Codificación:** CIE-10 en Dx; NANDA-NOC-NIC en columnas 1-3; vigilancia IAAS
  en dispositivos/curaciones (col. 4 y gatillos).
- **Contrarreferencia APS:** al alta (hospital o HODOM), el cierre de transición
  —origen, destino, responsable, próximo contacto, signos de alarma, ruta de
  reingreso (SAMU 131 en HODOM)— se vuelca a la contrarreferencia a la atención
  primaria y a la epicrisis del paciente/cuidador.

## Salvedades

- **Dosis no inventadas:** toda dosis específica se delega a la guía vigente /
  químico farmacéutico clínico (vía interconsulta). Las dosis del ejemplo son
  ilustrativas.
- **Normativa no inventada:** las dependencias locales se marcan como "según
  protocolo institucional / norma vigente". Verificar las referencias normativas
  HODOM contra el texto oficial vigente del MINSAL antes de uso formal.
- **Composición de la unidad:** este modelo define el Anillo 1 como médico,
  enfermera/o, TENS, kinesiólogo/a y fonoaudiólogo/a (decisión del operador).
  Todo otro rol —incluido trabajador social— se accede por
  interconsulta/derivación (Anillo 2).
- **Decisión clínica:** esta es una estructura documental de soporte; el médico
  tratante decide y firma.
