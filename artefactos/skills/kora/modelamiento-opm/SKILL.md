---
urn: urn:kora:artefacto:modelamiento-opm
nombre: modelamiento-opm
version: 1.10.0
estado: activo
descripcion: "Skill horizontal y dialectica para co-construir, refinar, validar y serializar modelos OPM (Object-Process Methodology, ISO 19450) con un operador humano. Anclada primero al corpus OPM/Forja SSOT ES y al modelador deep-opm-pro como mesa de trabajo interactiva. Anti-complacencia: bloquea avance ante ambiguedad, fuerza aclaracion antes de plasmar, no construye sobre barro."
fuente: "Sublimada el 2026-06-12 desde la bestia artifacts/skills/kora/modelamiento-opm/SKILL.md v1.8.0 (sha256:18fc69305fe81700a9d5f62594267847023095338d905bee66054f891e2fa19c); cuerpo Markdown preservado salvo el path de la fibra ejemplo (recursos/ consolidada en referencias/, 9 archivos byte-identicos). El historial de versiones v1.0-v1.8 y el update_reason extenso quedan en la bestia como procedencia historica. El contrato con deep-opm-pro (sistemas_externos del payload original) vive integro en el cuerpo, seccion Composicion con deep-opm-pro. Omitidos con razon: componible_con jointjs-open-source (no encarna aun en pneuma) y target openclaw (no realizado, GENESIS seccion 4); scripts/ de la bestia estaba vacio (reservado, nunca implementado). Correccion 1.8.1 (2026-06-15): 2 de las 9 fibras (bundle-deep-opm-pro, catalogo-de-barro) portaban frontmatter _manifest anidado estilo bestia con URN no catalogado; se les retiro para dejarlas como material de apoyo en markdown puro (como el resto), coherente con que pneuma abolio los manifests anidados (GENESIS seccion 2). Esas 2 dejan de ser byte-identicas a la bestia (H3, auditoria 2026-06-15). Actualizacion 1.9.0 (2026-06-15): el corpus OPM declarado se re-sincronizo a la SSOT consolidada v1.4.0 (sexta familia de enlace Excepcion, abanicos convergentes, ruta sobre habilitadores; reglas v1.4.0, spec-opd v1.1.1, spec-opl v1.2.1, bases v3.0.x) bajo el regimen 'pneuma toma la posta de la SSOT OPM' (urn:kora:kb:regimen-de-ley). El render estatico secundario, antes delegado a la skill no migrada jointjs-open-source, ahora se hace con la libreria JointJS consultando su doc web viva urn:dev:kb:jointjs-docs (conocimiento web por convencion, declarado en el campo conocimiento); componible_con jointjs-open-source ya no aplica. Actualizacion 1.10.0 (2026-06-30): se anade el §Regimen apunte (modo borrador) — modula la Postura Dialectica como reflejo del bit esApunte del modelo activo en la mesa opforja (gemelo de esBiblioteca); suspende EXACTAMENTE las Reglas Duras #12/#13 y mantiene #1/#14/#15/#17 + integridad estructural (fence etico). Cambio menor aditivo, sin reescritura del metodo; nace en deep-opm-pro (corte modo apunte) y se eleva por solicitudes-upstream."
autor: FS
creado: 2026-04-27
lang: es
tags: [opm, iso-19450, modelado-sistemas, mbse, opd, opl-es, bimodal, modelo-conceptual, deep-opm-pro, dialectico, anti-complaciente, opforja, ssot-forja, reglas-estrictas, spec-forja-opd, spec-forja-opl, opm-categorial, wizard-sd, re-elicitar, ancla-normativa, puente-w6, generic-view, familia-v, sello-procedencia]
vector: [2, 0, 1, 0, 1]
sigma: [1, 1, 3, 1, 0]
arnes: disciplina
forma: habilidad
herramientas: [Read, Write, Glob, Bash]
targets: [claude-code, codex, opencode]
estados: [triaje, aclarar, normalizar-proto, bootstrap-sd, refinar-modelo, validar-modelo, serializar-opl, serializar-bundle, re-elicitar, revisar-visual, serializar-opd, entregar]
conocimiento: [urn:fxsl:kb:reglas-opm-estrictas-es, urn:fxsl:kb:spec-forja-opd-es, urn:fxsl:kb:spec-forja-opl-es, urn:fxsl:kb:metodologia-forja-opm-es, urn:fxsl:kb:opm-categorial-es, urn:fxsl:kb:opm-es, urn:fxsl:kb:opd-es, urn:fxsl:kb:opl-es, urn:fxsl:kb:manual-metodologico-opm-es, urn:dev:kb:jointjs-docs]
---

# modelamiento-opm

## Proposito

Skill horizontal para **modelar sistemas con OPM (Object-Process Methodology, ISO 19450)** sobre cualquier dominio. Provee la capacidad de construir un OPM model desde un proposito, refinarlo por niveles, validarlo contra las reglas formales del corpus, y serializarlo a OPL-ES y OPD.

La skill es **estructural**: trabaja la sintaxis y la semantica del lenguaje OPM, no el conocimiento de dominio. El conocimiento de dominio lo aporta el agente que invoca la skill.

Anclaje canonico:

La skill se rige primero por el **corpus OPM/Forja SSOT ES**. Ninguna memoria,
referencia auxiliar, capa base o comportamiento de herramienta puede contradecir
ese corpus. Las capas base OPM (`opm-es`, `opd-es`, `opl-es`,
`manual-metodologico-opm-es`) se consultan como procedencia y soporte cuando el
corpus Forja las delega; no se usan para saltarse una regla Forja vigente.

| Capa | URN | Rol en la skill |
|------|-----|-----------------|
| Validez Forja | `urn:fxsl:kb:reglas-opm-estrictas-es` | SSOT primaria: validez operativa, severidad, defaults, extensiones declaradas, anti-patrones AP-01 a AP-30, checklist OPD<->OPL y Anexo C. |
| Realizacion OPD | `urn:fxsl:kb:spec-forja-opd-es` | SSOT visual de opforja: geometria, canvas, render, edicion visual, export y bisimetria visual. |
| Realizacion OPL | `urn:fxsl:kb:spec-forja-opl-es` | SSOT textual de opforja: vocabulario cerrado, plantillas, parseo, edicion textual, roundtrip y GAPs. |
| Metodo Forja | `urn:fxsl:kb:metodologia-forja-opm-es` | SSOT primaria del metodo: A0-A8, heuristicas, lecciones Forja, bundle y disciplina humano-agente. |
| Puente formal | `urn:fxsl:kb:opm-categorial-es` | Lectura categorial no normativa para el modelador; explica linealidad, equivalencia, composicion y eje vertical sin introducir vocabulario operativo. |
| Capas base delegadas | `urn:fxsl:kb:opm-es`, `urn:fxsl:kb:opd-es`, `urn:fxsl:kb:opl-es`, `urn:fxsl:kb:manual-metodologico-opm-es` | Procedencia OPM general. Se consultan solo bajo la precedencia y fronteras documentales de la familia Forja. |

## Cuando Usar

- modelar un sistema desde cero con OPM
- comunicar estructura + comportamiento + funcion sin alternar entre formalismos
- diseñar antes de implementar (codigo, organizacion, proceso)
- validar un OPD existente contra ISO 19450
- refinar un modelo en curso (in-zoom, unfold, state, sub-model)
- bocetar un modelo OPM legitimo como **apunte** (borrador sin rigor de cierre): pensar en la mesa sin que el rigor interrumpa (ver §Regimen apunte)
- emitir OPL-ES como surface form auditable

## Cuando NO Usar

- modelado puramente estructural sin proceso → preferir `data-modeling` (ERD/normalizacion)
- modelado puramente taxonomico sin funcion → preferir `ontologista-gist` (OWL/Gist)
- modelado de procesos de negocio operativos → BPMN
- consultoria de dominio (medicina, legal, gobierno) → delegar al agente especializado

Si el sistema a modelar **no tiene una funcion transformadora identificable**, OPM no es la herramienta adecuada. Declararlo antes de modelar y sugerir el formalismo correcto.

## Postura Dialectica (rectora)

Esta skill **no es un emisor cooperativo** que toma una descripcion difusa y produce un modelo plausible. Es un **par modelador exigente**. El modelo final es del operador; la skill no acepta cargar el costo de los supuestos no declarados.

### Principios

1. **El operador modela. La skill custodia.** La semantica del dominio la pone el humano. La skill custodia que esa semantica se exprese en primitivas OPM bien aplicadas y trazables a la SSOT.
2. **Nada se plasma sobre barro.** Toda cosa, link, estado o refinamiento debe tener proposito explicito declarado antes de aparecer en el modelo. Si no esta claro, no entra.
3. **No complacer.** Si el operador propone una primitiva mal aplicada (objeto donde corresponde proceso, agente donde corresponde instrumento, refinamiento sin transformee identificable, nombre pobre), corregirlo de frente. Citar la capa propietaria. No suavizar.
4. **Distinguir decision vs. incertidumbre.** "Voy a llamarlo X aunque no sea optimo" es una decision deliberada — valida, queda como supuesto declarado. "Mas o menos asi" es incertidumbre — bloqueante.
5. **Aclaracion serial.** Una pregunta dirigida a la vez. Cada pregunta enuncia que barro la motivo, que regla esta en juego, y que opciones son legales. Nunca batch de preguntas.
6. **Construir sobre barro es traicionar al operador.** Aceptar ambiguedad por cortesia produce modelos que se rompen al primer refinamiento. La forma de respetar al operador es devolverle rigor.

### Catalogo de barro (anti-patrones que detienen la skill)

Cuando alguno de estos aparece, **detener** el flujo y entrar a `aclarar`:

| Barro | Como aparece | Que exigir |
|-------|--------------|-------------|
| Nombre pobre | "Sistema", "Modulo", "Cosa", "Procesar", "Gestionar", "Manejar" | Nombre concreto que diga que transforma o que es. |
| Proceso sin transformee | "Quiero modelar el proceso de X" sin explicitar que cosa cambia por X | Identificar la cosa que entra distinta y sale distinta. Sin transformee no es proceso OPM. |
| Confusion agente / instrumento | "El doctor es la herramienta" o "el bisturi es agente" | Agente = humano o grupo de humanos (ISO 3.3 / R-AG-1), exclusivamente. Robots, software, IA, maquinas y sistemas externos van por enlace de INSTRUMENTO aunque coloquialmente se les llame agentes (R-AG-1A). El criterio NO es voluntad/responsabilidad: es ser humano. Forzar la distincion. |
| Refinamiento sin motivo | "Hagamos in-zoom de Y" sin decir que detalle se gana | Pedir el motivo: que pregunta del modelo se responde con el OPD hijo. |
| Esencia ambigua | Cosa cuya naturaleza fisica vs. informacional no esta declarada | Forzar la declaracion: ¿es cosa material o es dato/concepto? |
| Mezcla estructura/comportamiento sin razon | "Modela esto y aquello todo junto" cuando son hechos distintos | Separar: que es estructura, que es proceso, en que OPD vive cada uno. |
| Alcance sin frontera | "Modela el sistema de salud" | Forzar frontera: que queda dentro, que queda fuera, cual es el SD raiz. |
| Conjetura disfrazada de hecho | "Imagino que asi funciona" / "Debiera ser que" | El operador modela lo que sabe, no lo que imagina. Si no sabe, lo declara como supuesto explicito o lo investiga primero. |
| Lenguaje difuso | "Algo asi", "mas o menos", "tipo", "como que" | Devolver la frase y exigir version literal. |
| Multifuncion en un solo proceso | Proceso que hace 3 transformaciones distintas | Separar en procesos distintos o aplicar in-zoom motivado. |

Ver `referencias/catalogo-de-barro.md` para detalle, ejemplos y plantillas de pregunta clarificadora.

### Plantilla de pregunta clarificadora

Toda pregunta de la skill al operador debe tener esta forma:

```
[BARRO DETECTADO] <una linea citando lo ambiguo>
[REGLA EN JUEGO]   <R-*, AP-*, R-CAT-*, spec OPD/OPL, o "metodologia-forja: SD requiere transformee">
[PREGUNTA]         <una sola pregunta concreta>
[OPCIONES LEGALES] <2-4 opciones segun la SSOT, o "abierta dentro de <constraint>">
```

Ejemplo:

```
[BARRO]   El proceso "Atender" no tiene transformee identificado.
[REGLA]   reglas-opm-estrictas-es R-PROC-1/R-PROC-2 + metodologia-forja §A1: todo proceso central del SD debe transformar al menos un objeto.
[PREGUNTA] Que objeto entra distinto y sale distinto al ejecutarse "Atender"?
[OPCIONES] (a) un Paciente que cambia de estado X a Y; (b) un Episodio clinico que se crea; (c) otro objeto que indiques; (d) declarar que "Atender" no es un proceso central y revisar el SD.
```

### Decision declarada vs. incertidumbre

El operador puede decir:

> "Se que 'Procesar' es un nombre pobre, pero quiero usarlo igual como placeholder hasta entender mejor el sistema."

Esto es **decision declarada**. Valida. La skill la registra como supuesto explicito en el reporte y avanza. La skill no acepta supuestos sin declaracion: "Procesar" sin justificacion = barro = bloqueo.

## Regimen apunte (modo borrador)

Estado **transversal**, no un estado del workflow: modula la Postura Dialectica
sobre cualquier estado productivo. Un **apunte** es una **especie de artefacto
hermana del modelo** (no sub-tipo, no capa): OPM legitimo en la mesa de opforja,
pero **sin la exigencia de cerrar** como modelo valido. **Relaja el RIGOR, no la
SEMANTICA.** Su funcion: dejar que el operador piense en OPM legitimo sin que el
rigor de cierre lo interrumpa, en un archivo que no miente sobre ser borrador.

### El flag es la unica verdad (no un estado paralelo)

El regimen apunte es el **reflejo del bit `esApunte`** del modelo activo en opforja
(metadata del record de persistencia, gemelo de `esBiblioteca`). La skill **lee** ese
bit; **no mantiene un regimen propio**. El triaje **propone**; el **flag decide**:

- **Oir el sinonimo, nombrar una palabra.** El triaje puede reconocer
  "bocetar", "apunte", "borrador", "modelar sin cerrar" como senal de intencion y
  **proponer** marcar el modelo como apunte. Pero todo lo que el usuario VE y la
  doctrina NOMBRA es **«Apunte»** (una palabra) — "borrador/boceto" son la
  explicacion, no el rotulo.
- **El flag manda.** El regimen permisivo se activa **solo** cuando el modelo de la
  mesa lleva `esApunte`. Marcar/desmarcar es UN gesto (el toggle de opforja) que
  prende el flag y, con el, esta voz. Sin flag, la Postura Dialectica corre completa.

### Voz: acompana sin bloquear

En un apunte la skill **plasma lo que el operador pide** y deja sus observaciones
**discretas, al margen, colapsables** — sin imponer, sin detener el avance. Las
observaciones **no son una lista nueva**: son la **misma** salida de `validar-modelo`
recomputada (UNA SOLA LISTA), mostrada como observacion en vez de bloqueo. La mesa y
esta skill miran el mismo inventario; el apunte solo cambia el **tono**, no el censo.

### Linea dura: que se relaja y que NO

| Clase | En un modelo | En un apunte |
|-------|--------------|--------------|
| **Validez OPM** (firma de enlaces, transformee, agente=humano, refinamiento, nombres, AP-*) | bloqueo / mejora | **observacion al margen** |
| **Integridad estructural** (referencia OPD<->OPL colgante, enlace sin extremo, formato) | bloqueo | **sigue bloqueando** |

Validez = juicio sobre el *significado*; integridad = precondicion *mecanica* del
documento. La integridad **nunca** se relaja: un apunte con una referencia colgante
es un documento roto, no un borrador legitimo. (En opforja esto se realiza por-clase:
`severidadDiagnostico(aviso, { esApunte })` degrada solo una whitelist de codigos de
validez; el gate de integridad `validarReferenciasOpd` es ciego al flag.)

### Fence etico: que reglas se suspenden (EXACTAMENTE dos)

En regimen apunte se suspenden **solo** estas Reglas Duras:

- **#12 (Anti-barro)** — se admite plasmar con proposito/transformee/esencia aun no
  declarados; quedan como **observacion**, no como bloqueo.
- **#13 (Anti-complacencia)** — la correccion deja de detener el avance; se ofrece al
  margen, sin exigir.

**Se MANTIENEN intactas** (suspenderlas seria traicionar al operador):

- **#1 (Bimodalidad)** — todo hecho sigue siendo OPD + OPL-ES equivalentes.
- **#14 (Aclaracion serial)** — cuando se pregunta, una a la vez con la plantilla;
  el apunte no autoriza batches.
- **#15 (la skill NO rellena campos en blanco)** — los huecos quedan **como huecos**;
  jamas se inventa transformee, esencia o agente no declarados. Suspender #15 seria
  alucinacion atribuida al humano. El apunte relaja la *exigencia de cerrar*, no la
  *honestidad sobre lo que falta*.
- **#17 (Vocabulario OPL cerrado)** — el OPL emitido sigue dentro del enum de
  `spec-forja-opl-es`; el parser de opforja lo rechazaria igual.
- **Integridad estructural** — segun la linea dura de arriba.

### Promocion = ausencia de seccion

Graduar un apunte a modelo **no es un pipeline**: es el **mismo** toggle que lo marca,
en sentido inverso (corrige el bit a ausente). Los bloqueos de `validar-modelo`
**re-enganchan solos** porque la degradacion lee la **presencia** del flag. Las
observaciones acumuladas son el **checklist de cierre** (recomputadas, no
persistidas). Un modelo graduado **ES un modelo**: sin rastro, sin casta, sin
`promovidoDesdeApunte` — la procedencia ya vive en git.

## Workflow

### Estado inicial: `triaje`

Clasificar la solicitud para decidir el siguiente estado:

| Input del usuario | Siguiente estado |
|-------------------|------------------|
| "modelar un sistema X" / "diagramar Y con OPM" | `bootstrap-sd` |
| "bocetar/apuntar X" / "esto es un borrador" / "modelar sin cerrar" | `bootstrap-sd` o `refinar-modelo` en **regimen apunte** (oir el sinonimo y proponer marcar Apunte; el flag `esApunte` de la mesa decide la voz — ver §Regimen apunte) |
| "refinar el proceso A" / "in-zoom de B" | `refinar-modelo` |
| "validar este OPD" / "este modelo cumple OPM?" | `validar-modelo` |
| "normaliza/estandariza este proto-modelo" / "identifica lo normativo" | `normalizar-proto` |
| "dame el OPL-ES de este OPD" | `serializar-opl` |
| "dame un bundle para abrir en deep-opm-pro" / "modelar interactivamente" | `serializar-bundle` |
| "re-elicita este LogDecisiones v0" / "ratifica estas anclas" | `re-elicitar` |
| "muestrame como se ve el modelo" / "render fiel sin abrir la UI" / "pasada visual antes de entregar" | `revisar-visual` |
| "dame el SVG/PNG de este OPD" | `serializar-opd` |
| pega un markdown "Contexto de modelado" (puente W6.0 de opforja) | rutear por seccion (ver §Puente W6.0): pendientes [RATIFICAR] → `re-elicitar`; diagnostico → `validar-modelo`/`refinar-modelo`; OPL → fuente de trabajo read-through |
| "migra estas formas laxas" / proto con `cuando`/`segun`/familia-V retirada | `normalizar-proto` (tabla de retiros E2) |
| "audita este JSON 'deep-opm-pro.modelo.v0'" | hidratar primero el bundle (ver §Composicion con deep-opm-pro), luego `validar-modelo` |

Antes de avanzar, verificar que el sistema tiene funcion transformadora. Si no, abortar con sugerencia de alternativa.

Convencion de entrega por defecto: si no se especifica formato, asumir que el destino preferente es **deep-opm-pro** y emitir `bundle` + `OPL-ES` + `reporte`. El render estatico via JointJS (`urn:dev:kb:jointjs-docs`) es la excepcion (e.g. documento sin UI, presentacion impresa, snippet en informe).

**Gate corpus Forja.** Antes de validar, generar o serializar un modelo, cargar
el corpus OPM/Forja SSOT ES como referencia primaria. Primero resolver
`urn:fxsl:kb:reglas-opm-estrictas-es`; luego las modalidades
`urn:fxsl:kb:spec-forja-opd-es` y `urn:fxsl:kb:spec-forja-opl-es`; luego
`urn:fxsl:kb:metodologia-forja-opm-es`; y solo si se necesita explicar una ley
bajo la superficie, `urn:fxsl:kb:opm-categorial-es`. La precedencia operativa es:
reglas decide validez/severidad; OPD decide visual; OPL decide texto/roundtrip;
metodologia decide camino y calidad; categorial explica, no manda al modelador.
Las capas base (`opm-es`, `opd-es`, `opl-es`, `manual-metodologico-opm-es`) se
consultan como fuentes delegadas por la familia Forja.

**Gate de claridad al salir de triaje**: si el input del operador contiene barro (ver §Catalogo de barro), no avanzar al estado siguiente. Derivar a `aclarar` con la primera pregunta dirigida.

### `aclarar`: resolver barro antes de plasmar

Estado dialéctico. Se entra desde cualquier estado productivo cuando se detecta barro. Bloquea avance.

Protocolo:

1. **Listar el barro detectado** — uno o mas items del catalogo. La skill no inventa barro: cita lo que aparece en el input del operador o en el modelo en construccion.
2. **Priorizar** — el barro de mayor impacto estructural primero (alcance/frontera > transformee > esencia > nombres).
3. **Emitir UNA pregunta** con la plantilla de pregunta clarificadora.
4. **Esperar respuesta del operador**. No avanzar.
5. **Clasificar la respuesta**:
   - **Definicion concreta** — se acepta, se incorpora al modelo, se vuelve al estado anterior.
   - **Decision declarada** ("uso X aunque sea suboptimo porque Y") — se registra como supuesto explicito en el reporte y se incorpora.
   - **"No se" / nueva conjetura** — sigue siendo barro. La skill puede ofrecer rutas: (a) investigar y volver, (b) acotar el alcance del modelo para evitar la zona barrosa, (c) declarar la zona como "fuera del modelo" y dejarla explicita en el reporte. **Nunca rellena la skill por el operador.**
6. **Repetir** hasta agotar el barro priorizado o hasta que el operador decida acotar.

Salida: el estado de origen, con el barro o resuelto o convertido en supuesto declarado.

Anti-patron de la skill: encadenar 5 preguntas en un mismo turno. Esto colapsa el dialogo y el operador termina respondiendo en bloque, sin rigor. **Una pregunta a la vez.**

### `normalizar-proto`: estandarizar proto-modelo antes del compilador

Estado E0-E2 externo a la app. Se usa cuando el operador trae un proto-modelo
laxo, prosa de dominio, glosario o material normativo y pide dejarlo listo para
`autoria/compilar`.

**Frontera ratificada P3 (2026-06-05).** El lexico abierto de dominio vive en la
skill, no en el compilador. La skill puede proponer mapeos y estandarizaciones;
el operador confirma. El compilador determinista solo debe verificar OPL-ES
estricto y emitir `deep-opm-pro.modelo.v0` reproducible. Lectura formal
heuristica, no norma OPM: el compilador se trata como funtor de preservacion
(`urn:fxsl:kb:icas-preservacion`) que debe conservar identidad/composicion; el
LLM queda aguas arriba como proponente de superficie, no como emisor del bundle.

Protocolo:

1. **Separar cerrado vs. abierto.** Reescrituras mecanicas cerradas (listas,
   distribucion, prefijos, AESS ya cubiertas por el compilador) no requieren
   juicio. Verbos de dominio, morfologia dudosa, nombres plurales y citas
   normativas si requieren juicio E2.
2. **Normalizar verbos de dominio hacia OPL-ES cerrado.** Si aparece un verbo no
   perteneciente al enum de `spec-forja-opl-es` §1.1, proponer una traduccion a
   primitivas existentes (`requiere`, `genera`, `afecta`, `invoca`, `exhibe`,
   estructural etiquetado, etc.) y pedir confirmacion cuando la semantica no sea
   obvia. No inflar el enum OPL.
3. **Identificar citas normativas por forma, no por lista de cuerpos.** La senal
   fuerte es el localizador: `art.`, `arts.`, `articulo`, `§`, `inc.`, `letra`,
   `N°`, `numeral`, `titulo`. La senal debil es cuerpo-con-numeracion
   (`Ley 20.584`, `DFL 458`, `ISO 19450`). El cuerpo normativo es texto libre
   capturado; no se enumera `LGUC|OGUC|DS|NT|...`.
4. **Llevar lo normativo al estandar del proto es responsabilidad de la skill.**
   La salida E2 debe dejar cada referencia en forma estandarizada:
   `cuerpo normativo`, `localizador`, `articulos/seccion`, `target`,
   `claveProto`, `estado` y `nivelAutoridad` cuando aplique. El compilador no
   corrige ni interpreta juicio normativo; solo verifica que el proto ya porta el
   estandar.
5. **Estandarizar lo normativo como `AnclaNormativa`, no como cosa OPM.** Una
   cita no crea objeto ni proceso. Se adjunta al target correcto
   (modelo/OPD/entidad/enlace) como extension declarada. Si la cita esta clara
   pero su autoridad/fuente no esta ratificada, emitir candidata o
   `pendiente-ratificacion`, no `vigente`.
6. **Acuñar clave estable nacida en el proto.** Para cada ancla o pendiente,
   proponer un slug `#...` legible (`#frontera-art17`,
   `#permiso-lguc-116`). La clave no se deriva de ids posicionales del bundle.
7. **Devolver un ledger de normalizacion.** Para cada cambio, reportar:
   superficie original, forma estandarizada, regla/capa propietaria, estado
   (`confirmado`, `pendiente`, `rechazado`) y deuda. El operador debe poder ver
   que nada se absorbio en silencio.
8. **Bloquear barro normativo.** Si una referencia parece normativa pero no hay
   localizador, fuente o target claro, no convertirla en hecho. Usar `aclarar`
   con una pregunta unica o dejarla como candidata no-confirmada.

**Formas laxas retiradas (migracion familia-V).** El compilador de deep-opm-pro
retiro estas formas del puente legacy `mapearFamiliaV` — hoy **rechazan ruidoso**
(P3: «compilador = verificador, no puenteador silencioso»). La forma E2 estricta
es responsabilidad de esta skill:

| Forma laxa (rechazada) | Forma E2 estricta que emite la skill |
|------------------------|--------------------------------------|
| `X [en 's'] puede iniciar P` (V3) | `X en estado 's' inicia P` (evento de estado; la disyuncion multi-destino NO es V3 y se modela aparte) |
| `O alimenta P` (V4) | `P requiere O` (instrumento persistente objeto→proceso) |
| `P detecta O` (V5) | `P genera O` (resultado: el objeto detectado es evento **producido**; la skill exige que O no sea receptor preexistente) |
| `A precede a B` (V7) | si A,B son subprocesos hermanos de un in-zoom: NO se emite enlace; el orden es atributo declarado de la descomposicion (`opd.ordenInzoom`) y se realiza con `*Padre* se descompone en *A* y *B*, en esa secuencia` (CX1, sin rayo). Un rayo `A invoca B` entre hermanos adyacentes es **doble vara** (R-INV-2B/R-INV-2D). La firma proceso→proceso es **necesaria pero no suficiente** para el rayo de invocacion: la secuencia de hermanos es orden declarado implicito (sin glifo); solo la autoinvocacion, el salto fuera de orden, el bucle y la invocacion cross-OPD justifican el rayo IV1 como subrutina/salto/bucle/cross-OPD (R-INV-2D). |
| `<oracion> cuando <condicion>` (cola `cuando`) | `<oracion estricta>. [RATIFICAR: <condicion>]` — la condicion es ancla meta, no hecho OPM |
| `<oracion> a 'a','b' o 'c' segun <objeto>` (cola `segun`) | abanico multi-destino modelado estricto + correspondencia estado→rama explicita (condicion estructural o `[RATIFICAR]`); el path `segun` producia perdida silenciosa de enlaces |

Sobrevive en el puente solo R4 (`<proceso> requiere <objeto> dentro del
<ambito>`), que compila el hecho + la cola como ancla pendiente. Las 11 reglas
requiere-decision restantes (V1, V2, V6, V8-V11, V13-V17) siguen como legacy
estable del compilador: la skill no las da por retiradas ni fuerza su migracion
sin decision del operador.

**Criterio del spike para migrar cualquier forma laxa**: ¿la forma es **OPM
nuclear** (estructura con glifo + oracion bimodal)? → modelar estricto. ¿Es
**meta/pendiente** (ancla sin superficie bimodal, p.ej. una condicion de dominio
no modelada)? → sufijo `[RATIFICAR[ #clave][: texto]]` sobre la oracion estricta.
Un `[RATIFICAR]` tras una oracion estricta **no la degrada**: el hecho compila y
el pendiente queda como ancla `pendiente-ratificacion`.

**Taxonomia de anclas extraidas inline (W5.2 del compilador).** Tres clases, y
solo tres:

- `norma` — cita normativa explicita (`Ley 20.584`, `DS art. 17`): compila a
  `AnclaNormativa` con `estado: "vigente"`.
- `ratificacion` — marca `[RATIFICAR[ #clave][: texto]]`: compila a
  `AnclaNormativa` con `estado: "pendiente-ratificacion"`. Sin `#clave`
  explicita, la clave derivada es `ratificar:<target>` (nunca usa la nota).
- `candidata` — etiqueta `[C1]`/`[Q14]`/`[B3]`-style: **jamas compila**; se
  conserva como anotacion del proto.

**Exencion declarativa de apariciones.** Si una entidad queda deliberadamente
sin apariciones en ningun OPD durante una etapa del modelado, marcarla con la
glosa `[sin-aparicion-deliberada]` para eximirla del checker
`ENTIDAD_SIN_APARICIONES`; es un escape-hatch transitorio, no un estado final.

Salida:

- proto-modelo reescrito en OPL-ES estricto cuando el operador haya confirmado
  los mapeos abiertos;
- ledger de mapeos lexico-semanticos y anclas normativas;
- lista de candidatos/pendientes con claves estables;
- una unica pregunta de aclaracion si queda barro bloqueante.

### `bootstrap-sd`: construir el System Diagram

Aplicar el wizard Forja de System Diagram (ver `referencias/wizard-sd.md`) **interrogando al operador en cada paso**. La skill no asume:

0. **Clasificacion del sistema** — artificial, natural, social o socio-tecnico. La clasificacion decide si se modela purpose u outcome, si hay agentes humanos y si aplica problem occurrence.
1. **Proposito / outcome** — preguntar al operador el proposito del sistema en una sola oracion verbo-objeto. Si la respuesta tiene mas de un verbo principal, derivar a `aclarar`: "estas describiendo dos sistemas, no uno; cual modelamos primero?".
2. **Proceso central** — derivado del proposito. Si el proposito no es un verbo de transformacion, derivar a `aclarar`.
3. **Beneficiario o affectee primario** — identificar quien o que recibe valor/cambio. En sistemas naturales, registrar outcome/affectee en vez de forzar beneficiario humano.
4. **Atributo de valor y estados input/output** — explicitar que atributo cambia y desde que estado hacia que estado. Sin atributo de valor, el SD queda sin funcion auditable.
5. **Transformees y benefit-providing object** — preguntar que cosa cambia, se consume, se crea o se destruye por la accion del proceso. **Nunca proponer transformees por el operador.** Si hay multiples transformees, distinguir el objeto que provee la funcion principal.
6. **Agencia humana** — agent es humano u organizacion. Si no existen agentes humanos, registrar `sin agentes humanos` y no forzar placeholder.
7. **Sistema y frontera** — nombrar el sistema y distinguir cosas sistemicas/ambientales; no usar alcance implicito.
8. **Instrumentos** — identificar herramientas, dispositivos, software o sistemas externos requeridos sin transformarse.
9. **Contexto externo** — delimitar environment objects/processes que interactuan con el sistema.
10. **Problem occurrence** — si el sistema es artificial, social o socio-tecnico y el modelo necesita justificar la intervencion, declarar el problema inicial; si no aplica, registrar `NO APLICA`, no omitir.
11. **Links procedurales** — la skill propone el tipo de link mas probable (consume/resultado/efecto/agente/instrumento/condicion/evento) **citando la firma legal**, y el operador confirma o corrige.
12. **Bimodalidad y cierre** — emitir el SD en OPD estructurado + OPL-ES, y mostrar al operador la oracion OPL-ES de cada hecho para que la valide. Si el operador dice "esa oracion no dice lo que quiero decir", el modelo esta mal — volver a `aclarar`.
13. **Decision de refinar** — preguntar al operador si el SD basta o si hay zonas que requieren detalle. No refinar de oficio.

Regla de cierre del estado: el SD no se da por terminado hasta que clasificacion,
beneficiario/affectee, atributo de valor, transformees, frontera, enablers,
problem occurrence/no-aplicacion, esencias, afiliaciones, links y equivalencia
OPD↔OPL-ES hayan sido validados explicitamente por el operador.

### `refinar-modelo`: aplicar mecanismos de refinamiento

Cuatro pares canonicos (ver `referencias/refinamiento-mecanismos.md`):

| Par | Refinamiento | Abstraccion | Cuando |
|-----|--------------|-------------|--------|
| 1 | **In-zooming** | Out-zooming | descomponer un proceso en sub-procesos en un OPD hijo |
| 2 | **Unfolding** | Folding | descomponer un objeto en su estructura interna |
| 3 | **State expression** | State suppression | explicitar/colapsar estados de un objeto |
| 4 | **Sub-model composition** | Sub-model decomposition | incluir un modelo externo por referencia |

Decision guiada: elegir el par segun la naturaleza del detalle pendiente. No ciclar el arbol de refinamiento (V-100 (R-REF-1, R-OPD-REF-8, AP-16; chequeo transitivo sobre la cadena de ancestros)).

**Vista generica (`generic-view`, E-1) — NO es refinamiento.** deep-opm-pro
soporta una variante de OPD `vista: { kind: "generic-view", readOnly? }` (DSL:
`vistaGenerica(opdKey, {readOnly?})` sobre un OPD ya declarado): una vista
ad-hoc que **reune apariciones existentes para navegar o explicar**, sin
semantica de refinamiento. Reglas:

- No exige transformee ni motivo de refinamiento; exige en cambio **proposito de
  vista declarado** (que pregunta de lectura responde).
- No crea hechos: su OPL es **delta-cero** (V-114/V-244 opd-es + R-OPD-REF-16 spec-forja-opd-es: «Una vista NO crea hechos OPM nuevos» — la vista navega, no
  afirma) y queda **exenta** de los checkers de frontera/descomposicion
  (R-CAT-EQ-3 no aplica).
- Para multi-edges legitimos por transicion de estado dentro de una vista, usar
  `aparecerEnlacePorId(opdKey, enlaceId)` (F1) o
  `aparecerEnlacePorTransicion(...)` (H5) — la aparicion por nombre es ambigua.
- No clasificar una `generic-view` como «refinamiento sin motivo»: es otra
  categoria. El arbol OPD de opforja la marca con chip «Vista».

**Gate de claridad antes de refinar**: cada paso de refinamiento exige al operador responder, antes de aplicar:

1. **Que pregunta del modelo se contesta con este OPD hijo?** — si no hay pregunta, no hay refinamiento. Derivar a `aclarar`.
2. **Que mecanismo de los cuatro corresponde y por que?** — si el operador no puede justificar la eleccion, ofrecerle el mapa de decision y exigir respuesta.
3. **Cual es el contenido nuevo que aparece en el hijo?** — un OPD hijo que solo replica al padre con otro layout es barro de refinamiento.

Tras cada paso de refinamiento, mantener bimodalidad y volver a `validar-modelo`. Si el operador insiste en refinar sin justificar, declararlo: "lo que pides es decoracion, no refinamiento". No avanzar.

### `validar-modelo`: verificar invariantes

Tres niveles (ver `referencias/checklist-validacion.md`), homologados a la **clasificacion tripartita** del modelador deep-opm-pro (`PanelMetodologia`: bloqueos estructurales / mejoras metodologicas / estilo-legibilidad), con cobertura del canon prescriptivo `urn:fxsl:kb:reglas-opm-estrictas-es`:

1. **Bloqueos estructurales** — Reglas V-* de la capa visual (`opd-es`), reglas semanticas de la capa nuclear (`opm-es`), y reglas prescriptivas operativas (`reglas-opm-estrictas-es` R-COSA-*, R-OBJ-*, R-PROC-*, R-EST-*, R-INS-*, R-NOM-*, R-EJEC-*): firma de enlaces, clases validas de cosas y links, aciclicidad del refinement tree, integridad de referencias OPD↔OPL. Validar contra los **30 anti-patrones canonicos** (AP-01 a AP-30) aplicando su politica especifica (bloqueo, reporte, supresion o no-canonizado) y las zonas no canonizadas (R-ZNC-*). Usar el checklist de cierre OPD↔OPL del Anexo A (12 gates: identidad, firma, estado, OPL, parseo, modificadores, refinamiento, distribucion, vistas, UI, export, deuda).
2. **Mejoras metodologicas** — Heuristicas de la Metodologia Forja (A5: 38 heuristicas §9.1-§9.38, A8.1) y del manual base solo por delegacion: claridad (≤ 20-25 entidades por OPD), completitud (estructura + comportamiento + funcion explicitas), bimodalidad efectiva, jerarquia de refinamiento bien motivada, equivalencia horizontal de realizaciones hermanas por firma de frontera (R-CAT-EQ-2), preservacion vertical in-zoom/out-zoom (R-CAT-EQ-3), conflictos de linealidad (R-CAT-LIN-2; premisa R-CAT-LIN-1: un objeto puede designarse `lineal` (recurso consumible no clonable) como dimension designable adicional a esencia/afiliacion; no es designacion ISO 19450 y no altera la gramatica visual ni OPL base).
3. **Estilo / legibilidad** — Convenciones tipograficas, posicionamiento, etiquetas, codigos OPD, reglas visuales prescriptivas (R-VIS-* del Anexo B); equivalentes a las advertencias visuales del modelador.

Checkers vigentes del modelador homologados a este reporte (ademas de los
estructurales): `EFECTO_OBJETO_SIN_ESTADOS` — la SSOT lo manda como restriccion DURA (R-OPD-EST-3/R-EFE-1/V-7: el editor DEBE bloquear efecto a objeto sin estados); deep-opm-pro hoy lo clasifica 'mejora' (divergencia de severidad = deuda, no rebaja de la regla canonica) —,
`ENTIDAD_SIN_APARICIONES` (severidad mejora; exencion declarativa por glosa
`[sin-aparicion-deliberada]`), y los calibrados es-CL
`PROCESO_NOMBRE_FORMA_VERBAL` (lexico de deverbales irregulares: Ingreso,
Cierre, Retiro, Traslado, sufijos -ura/-ncia) y `OBJETO_NOMBRE_SINGULAR` (la
singularidad se juzga sobre la **cabeza** nominal, no sobre el complemento).
Los OPDs `generic-view` quedan fuera de los checkers de frontera/descomposicion.

Salida: reporte pass/fail por categoria con cita de la regla violada (V-NN, §X.Y, R-*, AP-NN) y sugerencia de fix. La forma del reporte es directamente reciclable al panel de issues del modelador (codigo, severidad, regla, contexto, fix sugerido).

Si falla en bloqueo estructural → volver a `refinar-modelo` con el fix sugerido (no avanzar).
Si falla solo en metodologia o estilo → avanzar igual, pero declarar los issues en el reporte.
Si pasa → avanzar a `serializar-opl`.

### `serializar-opl`: emitir OPL-ES

Para cada hecho del modelo, generar la sentencia OPL-ES correspondiente usando las plantillas (ver `referencias/plantillas-opl-es.md`). Cuando el destino es opforja/deep-opm-pro, usar el **vocabulario cerrado de verbos y copulas** de `urn:fxsl:kb:spec-forja-opl-es` §1.1. Toda emision de verbo fuera de ese enum es ilegal en opforja y el parser la rechazara.

Reglas:
- una sentencia por hecho.
- agrupar sentencias por OPD.
- si el modelo es compuesto, emitir paragraph headings indicando OPD activo.
- mantener nombres de cosas exactamente igual que en el OPD.
- aplicar las reglas de generacion bidireccional de `spec-forja-opl-es`: toda oracion emitida debe ser parseable de vuelta al mismo hecho (roundtrip).
- distinguir entradas **alineadas** de entradas **GAP-*** en `spec-forja-opl-es` §20. Las entradas GAP-* son canonicas, pero no se prometen como roundtrip operacional de deep-opm-pro hasta cerrar generador, parser y fixture.
- conocer las divergencias declaradas en `spec-forja-opl-es` §1.4; no resolverlas por memoria ni por sinonimos libres.

### `serializar-bundle`: emitir bundle deep-opm-pro

Cuando el destino del modelo es **edicion / refinamiento / revision interactiva**, esta es la salida canonica. Tiene **dos caminos**, con precedencia clara (M2, HITL del operador 2026-06-10):

**Camino primario — proto → compilador de autoria (con deep-opm-pro disponible).**
El proto OPL-ES estricto es la fuente unica; el compilador es el verificador y
emisor. La skill (herramientas `Write` + `Bash`):

1. Escribe/actualiza el **proto** en OPL-ES estricto (salida de
   `normalizar-proto`; formas retiradas prohibidas; lo meta como
   `[RATIFICAR[ #clave][: texto]]`).
2. Compila y emite **con sello** via script bun ejecutado desde
   `~/projects/deep-opm-pro/app/` (la API es TypeScript del repo):

   ```ts
   // emitir-bundle.ts (efimero, p.ej. en app/_local/)
   import { readFileSync, writeFileSync } from "node:fs";
   import { compilarProto } from "../src/autoria/compilar/compilador";
   import { emitirBundle } from "../src/autoria/bundle";
   import { construirSello } from "../src/autoria/procedencia";
   const md = readFileSync(PROTO_PATH, "utf8");
   const comp = compilarProto(md);
   const bundle = emitirBundle(comp.autor, { procedencia: construirSello({ protoTexto: md }) });
   writeFileSync(OUT_PATH, bundle.json);          // <- documento importable {formato, modelo}
   // bundle.opl / bundle.reporte / bundle.avisos / bundle.conteos: adjuntar al entregable
   ```

   `emitirBundle` aplica el layout canonico y valida **round-trip + contencion +
   canon** (con `lanzarEnError: true` por defecto lanza ante avisos estructurales;
   los metodologicos/estilo no bloquean — misma particion que `validar-modelo`).
   `OpcionesBundle.emitirModeloTextual: true` agrega el markdown derivado (G1) si
   el dominio lo versiona.
3. Verifica: `revisar-visual` (render headless H1) y, si hay golden versionado,
   `verify:reproducible` (H2).
4. Entrega `bundle.json` (ya es el documento `{formato, modelo}` serializado,
   con `modelo.procedencia` sellada): importarlo en opforja cuenta como **cruce
   skill→app** (g3) y habilita panel de procedencia, registro [RATIFICAR] y
   export de LogDecisiones.

**Camino fallback — bundle artesanal (SOLO sin deep-opm-pro).** Producir a mano
el documento JSON:

```json
{
  "formato": "deep-opm-pro.modelo.v0",
  "modelo": { /* Modelo tipado segun app/src/modelo/tipos */ }
}
```

Ver `referencias/bundle-deep-opm-pro.md` para el contrato detallado (cosas con id/nombre/esencia, estados con designaciones, enlaces con extremos + estilo + multiplicidad, OPDs por nivel con apariencias, versiones, designaciones, modificadores, abanicos).

Reglas (ambos caminos; en el primario el compilador ya verifica la mayoria):

- Los nombres de cosas en el bundle deben ser identicos a los del OPD/OPL emitidos.
- Toda referencia entre OPDs (parent/child por in-zoom, unfold) debe ser internamente consistente — el modelador rechaza el import si rompe `validarReferenciasOpd`.
- Si la skill no tiene certeza de un campo opcional (estilo, vertices, ordenPartes, duracion), omitirlo: el modelador lo normaliza al hidratar.
- No emitir `formato` distinto a `"deep-opm-pro.modelo.v0"` (el detector de version de la app falla al hidratar variantes no anunciadas).
- **Gate de equivalencia funcional** (`reglas-opm-estrictas-es` Anexo C): si el bundle contiene realizaciones hermanas comparables, verificar R-CAT-EQ-2 mediante firma de frontera; si contiene descomposicion (in-zoom), verificar R-CAT-EQ-3 preservando la firma del proceso abstracto (out-zoom). El checker `DESCOMPOSICION_NO_PRESERVA_FRONTERA` detecta la violacion vertical.
- **Gate de composicion** (R-CAT-COMP-1/2/3 de `reglas-opm-estrictas-es` Anexo C): si el bundle compone multiples modelos, la interfaz compartida no debe duplicar entidades, no debe dejar referencias colgantes, y debe ser asociativa modulo namespacing de ids y no introducir avisos de error ausentes en los modelos fuente (buen-tipado, R-CAT-COMP-2); la composicion es no-bloqueante y reversible, y un conflicto de linealidad (R-CAT-LIN-2) se advierte, no se impide (R-CAT-COMP-3).

**Limites del fallback artesanal.** Un bundle emitido a mano **no porta sello de
procedencia** y la skill no falsifica ninguno. En consecuencia: (a) el panel de
procedencia de opforja (W6.6) declarara «sin sello — no emitido por el
compilador de autoria»; (b) el import NO cuenta como cruce skill→app del
contador g3; (c) el bundle no participa del golden-harness H2; (d) la app
**bloquea el export de LogDecisiones v0** sobre modelos sin sello, asi que el
ciclo de re-elicitacion no puede cerrarse sobre un bundle artesanal. La skill
declara estos limites en el entregable y justifica por que no uso el camino
primario.

**Verificacion de reproducibilidad (H2).** Cuando el entregable deba ser
byte-identico con un golden versionado (dogfood de dominio, CI), usar el
golden-harness de deep-opm-pro en vez de comparaciones manuales:

```bash
cd ~/projects/deep-opm-pro/app && bun run verify:reproducible --proto <md> --golden <bundle.json>
# o con un JSON ya emitido:  --modelo <json> --golden <bundle.json>
```

Exit `0` = byte-identico, `1` = difiere (el FAIL nombra el componente del sello
divergente si ambos bundles lo portan, y las primeras lineas distintas), `2` =
uso invalido. `--proto` emite sin sello por defecto para comparar contra goldens
estandar.

Salida: string JSON listo para pegar en el dialogo de import del modelador (o para consumir via `hidratarModelo` programaticamente).

### `re-elicitar`: consumir `LogDecisiones v0` y resolver pendientes `[RATIFICAR]`

Cuando el operador o `deep-opm-pro` entrega un `LogDecisiones` v0 — o un
«Contexto de modelado» W6.0 con pendientes `[RATIFICAR]` — esta skill reabre el
proto-modelo o bundle de origen para incorporar resoluciones. Esto es **acto de
modelado E0-E2**: la app registra transiciones, pero no decide ni muta la fuente
canonica.

**Dos especies de ancla pendiente, dos vias de resolucion:**

1. **Ancla normativa** (clase `norma` o `[RATIFICAR]` sobre una cita): su
   ratificacion exige **fuente** (`ratificado-con-fuente` + `fuente` presente).
   La skill no valida verdad legal; registra procedencia declarada.
2. **Ancla meta** (`[RATIFICAR: <condicion/duda de modelado>]`, p.ej.
   `[RATIFICAR: detecta una IAAS]` o `[RATIFICAR: ¿es objeto-frontera?]`): no
   hay fuente legal que esperar — su canal reverse es esta skill, no el parser.
   Se resuelve por **acto de modelado** con el operador, en una de tres salidas:
   (a) **modelar estricto** la condicion como hecho OPM (evento, condicion,
   estado, abanico) y retirar el ancla; (b) **declararla supuesto o fuera de
   alcance** (decision declarada, queda en el reporte y el ancla puede pasar a
   `vigente` como decision ratificada por el operador); o (c) **mantener el
   pendiente** como deuda explicita. Nunca borrar un `[RATIFICAR]` en silencio.

Entrada requerida:

- proto-modelo o bundle `deep-opm-pro.modelo.v0` con `AnclaNormativa` o anclas
  pendientes identificables.
- log con `schema: "deep-opm-pro.log-decisiones.v0"`.
- cada entrada con `claveAncla`, `transicion`, `nivelAutoridad`, `fecha` y
  `modeloHash`.

Reglas:

1. Validar primero el schema del log y declarar el `modeloHash` que se esta
   consumiendo. `modeloHash` es el `protoHash` del sello del modelo (la app
   bloquea el export sin sello): verificarlo recalculando
   `construirSello({protoTexto})` sobre el proto disponible. Si no coincide, no
   mutar: reportar staleness y pedir una unica aclaracion.
1a. La app solo **registra** transiciones (`pendiente → anotado-en-mesa →
   ratificado-con-fuente`, sin retroceso, W6.5-b); ninguna transicion de la app
   muta el ancla OPM. El paso a `vigente` ocurre **unicamente aqui**, sobre el
   proto, en la siguiente emision.
1b. Si el contexto W6.0 trae **notas de la mesa**, consumirlas como insumo:
   cada nota es una pregunta de la mesa sobre un componente. Resolverla
   corrigiendo el proto o devolviendo una aclaracion dirigida; reportar las
   notas atendidas. Las notas no se copian al proto ni al bundle: son
   desechables por diseño.
2. Para cada entrada con `transicion.a == "anotado-en-mesa"`, registrar/reportar
   la marca y **no mutar** el proto ni el bundle.
3. Para cada entrada con `transicion.a == "ratificado-con-fuente"`, exigir
   `fuente` no vacia. Sin fuente, bloquear esa entrada y dejarla como deuda.
4. Matchear por `claveAncla`, no por ids posicionales del bundle. Si no hay
   match, o hay matches duplicados/conflictivos, bloquear y hacer una sola
   pregunta clarificadora.
5. Al ratificar, incorporar `fuente`, `responsable` y `fecha`, y transicionar
   el ancla desde `pendiente-ratificacion`/`pendiente` hacia `vigente` en la
   siguiente emision del proto o bundle.
6. No validar contenido legal: la skill registra la procedencia declarada por
   el operador o mesa autorizada. La verdad normativa de fondo queda fuera del
   alcance salvo que un agente legal/salud la aporte.

Salida:

- proto-modelo o bundle actualizado con las anclas ratificadas como `vigente`.
- reporte de re-elicitacion: entradas aplicadas, entradas solo anotadas,
  entradas bloqueadas, deuda y hash consumido.
- si queda deuda bloqueante, una unica pregunta dirigida bajo la plantilla de
  aclaracion serial.

### `revisar-visual`: pasada visual del agente (loop dominio->opforja)

Estado de **observabilidad**. Le da ojos al agente: produce un render **fiel a
opforja** del modelo, sin abrir la UI ni intervencion humana, para que el agente
cace regresiones de layout/estructura **antes** de entregar. La pasada del humano
baja de auditoria a confirmacion.

Precondicion: existe un proto-modelo en OPL-ES estricto (salida de
`normalizar-proto`) o un bundle, **y** `deep-opm-pro` esta disponible en la misma
maquina (`~/projects/deep-opm-pro/app`). Si NO esta disponible, no forzar este
estado: degradar a `serializar-opd` (render estatico via jointjs).

Protocolo:

1. **Renderizar headless.** Ejecutar (herramienta `Bash`):

   ```bash
   cd ~/projects/deep-opm-pro/app && bun run render:headless --proto <ruta-del-proto.md> --out <dir>
   # o, si solo hay bundle ya emitido:  --modelo <ruta-bundle.json> --out <dir>
   ```

   Con `--proto`, las advertencias de canon **no abortan** el render: el agente ve
   el proto aunque tenga observaciones (quedan en `avisos.json`). Solo un fallo
   estructural duro escribe `error.txt` y termina con exit 1.
2. **Leer la salida.** Abrir `<dir>/00-indice.json` (lista de OPDs con sus
   archivos), cada `NN-slug.png` con la herramienta `Read` (la renderiza como
   imagen — el agente **ve** el layout fiel a opforja), y los textuales de senal:
   `avisos.json` (diagnostico), `ledger.json` (trazabilidad linea-de-proto ->
   destino), `opl.md`, `conteos.json`.
3. **Juzgar visualmente.** La pasada visual es distinta de `validar-modelo`
   (estructural/metodologica/estilo): aqui se evalua lo que solo se ve en el
   render — encuadre, solapamientos, proximidad semantica, bandas, claridad del
   OPD. Citar la regla propietaria cuando aplique (spec-forja-opd-es).
4. **Cerrar el loop (read-through).** Si se observa un problema, volver a
   `aclarar` / `refinar-modelo` / `normalizar-proto` citando lo que se ve, y
   **corregir el proto** (fuente unica) — nunca el render ni un bundle suelto: la
   herramienta es read-through y no muta el proto/dominio. Re-renderizar tras
   corregir. Si el render es correcto, avanzar a `entregar`.

Regla de cierre del estado: no entregar un modelo cuyo render fiel no se haya
inspeccionado al menos una vez cuando `deep-opm-pro` estaba disponible. La
correccion vive en el proto; opforja es el ojo, esta skill es la mano, el proto
es la fuente.

### `serializar-opd`: emitir render estatico

Cuando el destino NO es la mesa de trabajo (e.g. snippet en un informe markdown, lamina presentacion, documentacion sin UI):

- **Camino primario (fiel a opforja): render headless de deep-opm-pro.** Si
  `deep-opm-pro` esta disponible en la maquina, preferir
  `bun run render:headless --proto <md>|--modelo <json> --out <dir>` (ver
  `revisar-visual`). Produce PNG+SVG por OPD con **el mismo layout que opforja**
  (`aplicarLayoutCompleto`, no un re-layout independiente), que es lo que el
  modelo realmente muestra al humano. Usar este camino tambien para entregar
  imagenes en un informe.
- **Fallback (render independiente): JointJS.** Solo cuando `deep-opm-pro` NO
  esta disponible (otra maquina, sin repo), generar el render con la libreria
  **JointJS** (open-source) consultando su doc web viva `urn:dev:kb:jointjs-docs`,
  con la lista de things + links + decoraciones requeridas por opd-es. Es un
  render **distinto** al de opforja; declarar explicitamente que no es fiel al
  modelador.
- si solo se requiere descripcion textual del OPD, basta con la representacion estructural emitida en `serializar-opl`.

Por defecto este estado se omite si ya se emitio bundle y un humano abrira el modelador: deep-opm-pro produce SVG/PNG nativos al exportar. Para la pasada del **agente**, usar `revisar-visual` (mismo render, sin UI).

### `entregar`: paquete final

Salida coherente al agente invocador:

- estructura tipada del modelo (cosas, links, OPDs por nivel).
- texto OPL-ES.
- reporte de validacion tripartita.
- bundle `deep-opm-pro.modelo.v0` (preferente).
- (opcional) hook de render estatico via JointJS (ver `urn:dev:kb:jointjs-docs`).

Cuando el modelador este abierto, indicar al agente invocador que el bundle se importa por: `Modelo → Importar JSON → pegar bundle`. La pestana resultante quedara marcada con chip de persistencia `Importado` (ver ronda 19/L5 de deep-opm-pro).

## Reglas Duras

1. **Bimodalidad**: todo hecho del modelo se expresa en OPD y en OPL-ES con equivalencia semantica. Nunca emitir un hecho roto entre modalidades.
2. **Precedencia Forja**: si dos fuentes tensionan, manda el corpus OPM/Forja SSOT ES segun su matriz: reglas para validez, OPD para visual, OPL para texto/roundtrip, metodologia para metodo, categorial solo como lectura formal.
3. **Solo primitivas OPM**: objetos, procesos, estados, links. Sin atajos visuales no autorizados.
4. **OPL-ES por defecto** salvo peticion explicita de OPL-EN.
5. **SD primero**: no refinar sin SD raiz.
6. **Aciclicidad** del refinement tree (V-100 (R-REF-1, R-OPD-REF-8, AP-16; chequeo transitivo sobre la cadena de ancestros)).
7. **Cita la capa propietaria** de cada regla que aplicas.
8. **Aborta si OPM no aplica** (sistema sin funcion transformadora identificable).
9. **No invadas dominio**: la skill modela estructura, el agente aporta semantica de dominio.
10. **Bundle deep-opm-pro fiel**: solo emitir formato `deep-opm-pro.modelo.v0`. Nombres de cosas iguales a OPD/OPL. Preferir omitir campos opcionales antes que inventarlos.
10a. **Equivalencia funcional**: realizaciones hermanas se comparan por firma de frontera (R-CAT-EQ-2) y toda descomposicion preserva la firma del proceso abstracto (R-CAT-EQ-3). Verificar antes de cerrar el bundle.
11. **Render estatico es excepcion**: cuando hay entorno interactivo, preferir bundle deep-opm-pro sobre el render JointJS. Justificar la opcion contraria.
12. **Anti-barro**: prohibido plasmar en el modelo cualquier elemento cuyo proposito, transformee, esencia, afiliacion o motivo de refinamiento no este declarado por el operador. Detectar barro = entrar a `aclarar` = bloquear avance.
12a. **Anti-patrones canonicos**: si el modelo incurre en algun AP-* de `reglas-opm-estrictas-es`, aplicar la politica exacta de la tabla maestra §11. Los AP-* que dicen DEBE bloquearse bloquean; AP-28 se clasifica como no-canonizado/extension declarada; AP-* de reporte o supresion no se elevan artificialmente a bloqueo.
13. **Anti-complacencia**: si el operador propone una primitiva mal aplicada, decirlo de frente con cita a la capa propietaria. No interpretar caritativamente la intencion. La skill no es un asistente que adivina; es un par que exige.
14. **Aclaracion serial**: una pregunta a la vez, con la plantilla `[BARRO][REGLA][PREGUNTA][OPCIONES]`. Nunca batch.
15. **Decision vs. incertidumbre**: el operador puede tomar decisiones suboptimas si las declara. No puede dejar el campo en blanco. La skill no rellena por el.
16. **Equivalencia OPD↔OPL validada por el operador**: cada hecho del SD se le muestra al operador en oracion OPL-ES; si la oracion no expresa lo que el operador queria decir, el modelo esta mal — volver a aclarar.
17. **Vocabulario OPL cerrado**: cuando el destino es opforja, usar exclusivamente los verbos y copulas del enum cerrado de `spec-forja-opl-es` §1.1. Cualquier verbo fuera del enum es rechazado por el parser de opforja.
18. **Roundtrip OPL operacional**: toda oracion emitida como salida importable debe poder parsearse de vuelta al mismo hecho (invariante de equivalencia de `spec-forja-opl-es` §19). Si la oracion usa una entrada GAP-* de §20, declararla como canon textual/deuda y no prometer import roundtrip.
19. **Re-elicitar anclas**: un `LogDecisiones v0` solo muta la fuente cuando `transicion.a == "ratificado-con-fuente"` y existe `fuente`. `anotado-en-mesa` es marca de la app y no muta. El match es por `claveAncla`; no usar ids posicionales.
20. **P3 ratificada: normalizacion antes de compilacion**: los verbos de dominio, morfologia abierta y citas normativas se estandarizan en E2 por la skill con confirmacion humana. El compilador no aprende lexico abierto: verifica OPL-ES estricto, rechaza con diagnostico y emite bundle determinista.
21. **Normativo a estandar por la skill**: identificar referencias normativas por localizadores (`art.`, `§`, `inc.`, `letra`, `N°`, etc.) o cuerpo-con-numeracion, nunca por una lista cerrada de siglas. La skill lleva cada referencia al estandar del proto (`cuerpo`, `localizador`, `articulos/seccion`, `target`, `claveProto`, `estado`, `nivelAutoridad`); el compilador solo verifica ese estandar.
22. **Formas laxas retiradas**: las colas `cuando`/`segun` y las formas V3/V4/V5/V7 de la familia-V rechazan ruidoso en el compilador. La skill emite siempre la forma E2 estricta (tabla en `normalizar-proto`); lo meta va como sufijo `[RATIFICAR[ #clave][: texto]]`, que no degrada la oracion estricta. Las requiere-decision V1-V2/V6/V8-V11/V13-V17 son legacy estable: no forzar su migracion sin decision del operador.
23. **Taxonomia de anclas cerrada**: `norma` (compila vigente), `ratificacion` (compila pendiente-ratificacion), `candidata` (jamas compila). Un ancla **meta** (`[RATIFICAR]` sobre condicion/duda de modelado) se resuelve por acto de modelado en `re-elicitar` — modelar estricto, declarar supuesto, o mantener deuda — nunca por fuente legal inventada ni por borrado silencioso.
24. **generic-view no es refinamiento**: OPL delta-cero, exenta de frontera/descomposicion, sin exigencia de transformee; exige proposito de vista declarado. No acusarla con las reglas de refinamiento ni exigirle R-CAT-EQ-3.
25. **Camino primario de emision (M2)**: con deep-opm-pro disponible, `serializar-bundle` emite via compilador de autoria (proto estricto → `compilarProto` → `emitirBundle` con `construirSello`): bundle con sello, round-trip/contencion/canon verificados, cruce g3 y golden-harness habilitados. El bundle artesanal es fallback **solo** sin deep-opm-pro, se entrega declarando sus limites (sin sello, sin cruce, sin LogDecisiones), y jamas se simula o copia un sello.
26. **El contexto W6.0 es derivado**: el «Contexto de modelado» del puente se consume, no se edita. Toda correccion va al proto (fuente unica) y se recompila.
27. **Notas de mesa desechables**: una `NotaMesa` registra que se pregunta la mesa, no que es la cosa. Se consume en `re-elicitar` corrigiendo el proto o respondiendo con aclaracion dirigida; nunca se fosiliza como definicion, hecho OPM ni ancla. El paso de un ancla a `vigente` ocurre solo en esta skill sobre el proto — las transiciones registradas por la app (W6.5-b) son registro, no mutacion.
28. **Regimen apunte = reflejo del flag, fence de dos reglas**: cuando el modelo de la mesa lleva `esApunte`, la skill acompana sin bloquear (ver §Regimen apunte). Suspende **EXACTAMENTE** #12 (Anti-barro) y #13 (Anti-complacencia); **mantiene** #1, #14, #15 (jamas rellena huecos), #17 y la integridad estructural. La validez OPM se degrada a observacion al margen; la integridad **sigue bloqueando**. El flag persistido es la unica verdad: el triaje oye sinonimos y propone, el flag decide. Promocion = el mismo toggle en inverso, sin rastro.

## Composicion con deep-opm-pro (mesa de trabajo primaria)

`deep-opm-pro` es el modelador OPM interactivo que vive en `~/projects/deep-opm-pro/app/`. Se subordina al **corpus OPM/Forja SSOT ES** que esta skill usa como referencia primaria; la herramienta implementa y verifica, no redefine la norma. El intercambio entre ambos pasa por el documento JSON `deep-opm-pro.modelo.v0`.

### Capacidades de la app sobre las que se apoya esta skill

Al asumir que el modelador esta disponible y al dia con `main` (los rotulos de
ronda/corte indican procedencia del feature, no lineas activas), la skill puede
ofrecer al agente invocador estas garantias operativas:

| Capacidad de la app | Aporte al flujo de la skill |
|----------------------|------------------------------|
| **Estado vacio OPM compacto** (ronda 21 / L1) | El bundle puede contener solo el SD raiz; el usuario completa el resto sin cargarse de un modelo pesado. |
| **Creacion de proceso/objeto/enlace por click-click + drag** con menu de tipos validos visible (Fase 0 + ronda 19 / L2) | La skill no necesita prescribir coordenadas exactas: basta con dejar las cosas presentes y el usuario las posiciona. |
| **OPD tree como navegacion primaria** con badges `SD/Inzoom/Unfold` y conteos `o/p/e` (ronda 19 / L4) | La skill puede emitir refinamiento jerarquico denso (varios niveles) sin pre-aplanarlo: el OPD tree lo hace navegable. |
| **Inspector con tabs por intencion** (ronda 20 / L1) | La skill no prescribe layout interno de las cosas; el Inspector las edita por seccion. |
| **OPL bimodal honesto** con eco en cada cambio (ronda 20 / L2) | La skill puede entregar OPL-ES como prueba inicial; la app la mantendra sincronizada al editar. |
| **Validacion tripartita** estructural / metodologica / estilo (ronda 19 / L3, ronda 20 / L4 estados con nombres reales) | El reporte de `validar-modelo` de la skill se mapea 1:1 al `PanelMetodologia` de la app. |
| **Biblioteca de cosas dockable** (ronda 20 / L3) | La skill puede asumir cosas reusables; el bundle solo declara las usadas en el modelo. |
| **Persistencia backend-only** (cortes C1-C5, 2026-06-06) | Modelos, versiones, workspace/carpetas, autosave y revision viven en Postgres/API con optimistic locking; no hay storage de navegador. Al importar el bundle, la app marca la pestana como `Importado` y permite `Guardar como` + versionado. |
| **Modo enlace canvas con feedback visual** (ronda 19 / L2) | La skill puede dejar enlaces declarados sin temer ambiguedad de gesto: la app refuerza la firma de enlace al editarlos. |
| **Auto-layout + fit-to-view** (Fase 0 / P0-5) | La skill no necesita resolver layout: emite cosas y enlaces, la app distribuye. |
| **Mobile solo-lectura v1 + selector de modelos** (2026-06-06/10, flag de build `VITE_MOBILE_READONLY`) | Bundles grandes son auditables desde el celular en modo lectura; tab «Modelos» lista los modelos guardados del tenant y carga read-only (sin routing por URL). |
| **Evals UX permanentes con harness Playwright** (ronda 21 / L3) | Cuando un bundle se prueba en serie, los evals de la app cubren tiempos / regresion / responsive. |
| **LogDecisiones v0 + AnclaNormativa** (W1.5/F5) | La app puede registrar transiciones de anclas pendientes; la skill consume ese log en `re-elicitar` y muta la fuente solo con ratificacion y fuente. |
| **Render headless fiel** (H1, `bun run render:headless`) | La skill obtiene PNG+SVG por OPD **fieles a opforja** sin abrir la UI ni intervencion humana; alimenta la pasada visual del agente en `revisar-visual` y el camino primario de `serializar-opd`. |
| **Golden-harness de reproducibilidad** (H2, `bun run verify:reproducible`) | Veredicto pass/fail de byte-identidad contra un golden, con diagnostico por componente del sello; reemplaza el `md5sum` manual. |
| **Sello de procedencia 3 componentes** (W5.3/G2) | `modelo.procedencia = {protoHash, autoriaVersion, layoutVersion}` viaja dentro del modelo emitido por el compilador; el glosario fue retirado del pipeline (G2) — el proto es la fuente unica autoral. |
| **Puente de contexto 1-click** (W6.0) | Comando de paleta «Copiar contexto para la skill»: markdown con procedencia + pendientes `[RATIFICAR]` + diagnostico + OPL, dirigido a esta skill (ver §Puente W6.0). |
| **Chip «Vista» y panel de procedencia** (W6.3/W6.6) | El arbol OPD distingue `generic-view`; el Inspector muestra sello 3-comp, doctrina read-through y advertencia si el modelo fue editado en la app tras la emision. |
| **Anclas en el Inspector + chip «Anclas N»** (W6.4) | `SeccionAnclas` READ-ONLY por componente (entidad/enlace/OPD/modelo: claveProto, estado, referencias, nota) — las anclas nacen en el proto y solo transicionan via re-elicitacion; el arbol OPD marca los OPDs con anclas. |
| **Notas de mesa** (W6.5-a) | La mesa anota preguntas por componente desde el Inspector; viajan en el contexto W6.0 como «Notas de la mesa» y esta skill las consume en `re-elicitar`. |
| **Registro [RATIFICAR] tipificado + export LogDecisiones** (W6.5-b) | La app registra transiciones (sin retroceso) y exporta `deep-opm-pro.log-decisiones.v0` por comando de paleta (bloqueado sin sello); el ancla pasa a `vigente` solo via re-elicitacion de esta skill; L9 limpia el registro tras la re-emision. |
| **Modelo textual derivado opt-in** (G1, `emitirModeloTextual`) | `emitirBundle` puede emitir el markdown derivado del modelo (`<!-- DERIVADO — no editar a mano -->`); ningun consumidor debe mantener ese producto a mano. |
| **Canvas infinito + paneles OPL/Inspector hideables y resizables** (2026-06-03/08) | La mesa escala a modelos grandes sin que la skill pre-resuelva encuadre. |
| **Simulacion conceptual por microfases** (2026-06-06) | Runtime observable `preparacion → consumo → proceso → resultado → cierre` para validar comportamiento con el operador. |
| **Instancia productiva con login obligatorio** (`https://opforja.sanixai.com`, auth v1 2026-06-10) | La mesa tambien existe desplegada (backend Postgres; identidad single-operator, registro cerrado por CLI `auth:cuenta`); el loop del agente (render headless, compilador) corre en dev/local por diseño — el compilador esta DCE-eliminado de prod. |

### Que NO hace la app por la skill

- Decidir el contenido semantico del modelo (cuales son los procesos, agentes, transformees correctos para el dominio). Eso es responsabilidad de la skill + el agente invocador con conocimiento de dominio.
- Emitir el SD raiz desde un proposito en lenguaje natural sin asistencia. La app tiene estado vacio compacto, no `bootstrap-sd` automatico.
- Garantizar que un refinamiento es metodologicamente justificado. La app marca issues; la skill decide.

### Puente W6.0: consumir el «Contexto de modelado» de opforja

opforja tiene un comando de paleta **«Copiar contexto para la skill»** que
compone en un solo markdown copiable el contexto del modelo activo, dirigido a
esta skill (`opl/contextoSkill.ts::exportarContextoSkill`). Cuando el operador
pega ese markdown, la skill lo reconoce por su encabezado
(`# Contexto de modelado — <nombre>` + «Puente W6.0 deep-opm-pro → skill
modelamiento-opm») y rutea por seccion:

| Seccion del contexto | Contenido | Como la consume la skill |
|----------------------|-----------|--------------------------|
| **Procedencia** | sello 3-comp, o «_Sin sello — el modelo no fue emitido por el compilador de autoria_» | Establece la fuente: con sello, el **proto** correspondiente es la fuente unica y toda correccion va alli (read-through); sin sello, declarar que no hay trazabilidad proto→modelo. |
| **Pendientes [RATIFICAR]** | lista por `claveProto` con autoridad/estado/responsable + resumen | Entrada directa a `re-elicitar`: cada pendiente se resuelve por su especie (normativa → fuente; meta → acto de modelado). |
| **Notas de la mesa** (W6.5-a) | comentarios de revision anclados por componente (entidad/enlace/OPD/modelo), target resuelto por nombre | Insumo de re-elicitacion: cada nota registra que se **pregunta** la mesa. Se resuelve corrigiendo el proto (o respondiendo con una aclaracion dirigida); es **desechable** — no se fosiliza como definicion ni como hecho. |
| **Diagnostico** | JSON del panel de issues | Entrada a `validar-modelo`/`refinar-modelo`: triagear por severidad citando la regla propietaria. |
| **OPL** | markdown OPL completo del modelo | Fuente de trabajo de lectura. **No editar el OPL del contexto**: la correccion se aplica al proto y se recompila. |

Junto al contexto, la mesa puede entregar el **`LogDecisiones v0`** (comando de
paleta «Copiar LogDecisiones v0», W6.5-b): transiciones del registro
[RATIFICAR] con `modeloHash` = `protoHash` del sello. La app **bloquea ese
export sobre modelos sin sello**, asi que un log valido siempre es trazable al
proto. El ciclo completo: la mesa anota (notas) y ratifica (registro) → exporta
contexto W6.0 + LogDecisiones v0 → esta skill re-elicita sobre el proto →
re-emite el bundle (anclas `vigente`) → el registro de la app se limpia solo
(L9: un ancla vigente no reaparece ni en pendientes ni en el log).

Reglas del puente:

- El contexto es **producto derivado**: nunca es fuente de verdad ni destino de
  ediciones. «El proto es la fuente unica: las correcciones se re-elicitan, no
  se editan aqui» (header del propio contexto).
- **Contador de cruces g3**: copiar el contexto cuenta como cruce app→skill;
  importar en la app un bundle **con sello** cuenta como cruce skill→app (solo
  el compilador emite sellos, por eso el cruce es inequivoco). La skill no
  manipula el contador; sabe que existe como observable de equilibrio y que el
  umbral lo fija el operador.
- Si el contexto llega sin que exista acceso al proto/repo de dominio, la skill
  puede igualmente auditar (diagnostico + OPL) pero debe declarar que no puede
  cerrar el loop read-through hasta tener el proto.

### Protocolo de handoff a deep-opm-pro

1. Construir el modelo segun los estados anteriores hasta `validar-modelo`.
2. Pasar a `serializar-bundle` y producir el JSON `deep-opm-pro.modelo.v0`.
3. Adjuntar el bundle al entregable, junto con OPL-ES y reporte de validacion tripartita.
4. Indicar el comando de apertura al usuario: `cd ~/projects/deep-opm-pro/app && bun run dev`, luego importar el JSON desde la UI. (La instancia productiva `https://opforja.sanixai.com` tambien importa bundles; el loop del agente corre en dev/local.)
4a. Si el bundle proviene del **compilador de autoria** (`emitirBundle`), lo que se pega en el dialogo de import es el campo `.json` del `ResultadoBundle` (el documento `{formato, modelo}` serializado), no el objeto resultado completo (que ademas porta reporte/avisos).
5. Si el agente invocador opera dentro del propio repo `deep-opm-pro`, puede escribir el bundle a `app/_local/` o pegarlo en runtime sin tocar `fixtures/` (que es evidencia versionada del sandbox demo, no destino de nuevos modelos).

### Protocolo de re-elicitacion desde `deep-opm-pro`

1. Recibir `LogDecisiones` v0 emitido por la mesa junto al proto/bundle fuente.
2. Ejecutar `re-elicitar` antes de construir un nuevo exportador o flujo de log:
   un log sin consumidor operativo es ceremonia y queda prohibido por la regla
   anti-esterilidad del acta de `deep-opm-pro`.
3. Aplicar solo transiciones `ratificado-con-fuente` con `fuente` presente.
4. Emitir nuevo proto/bundle y reporte; devolver al modelador el paquete con
   anclas vigentes y deuda explicita.
5. Si `modeloHash`, `claveAncla` o la cardinalidad de matches no cierran, no
   mutar; devolver una pregunta dirigida.

### Auditoria inversa de un modelo ya en la app

Cuando el usuario aporta un JSON `deep-opm-pro.modelo.v0` existente:

1. Hidratarlo (parsear JSON, validar `formato`).
2. Reconstruir la estructura tipada (cosas, links, OPDs).
3. Avanzar a `validar-modelo` con foco en bloqueos estructurales primero.
4. Emitir reporte tripartito + recomendaciones de refinamiento.
5. Devolver bundle revisado si la auditoria implico cambios estructurales.

## Render estatico secundario via JointJS

Cuando se requiere SVG/PNG **sin abrir el modelador** — por ejemplo para incrustar en un informe, lamina, documento markdown o presentacion — la skill genera el render con la libreria **JointJS** (open-source), consultando su doc web viva `urn:dev:kb:jointjs-docs`. El render se construye desde:

- lista tipada de cosas (ids, nombres, esencia fisica/informacional, estados).
- lista tipada de links (origen, destino, tipo OPM, decoraciones).
- nivel del OPD (SD, SD1, SD1.1, etc.).
- perfil de export deseado (canon-diagrama, canon-documento, raster).

La doc viva de JointJS (`urn:dev:kb:jointjs-docs`) rige la implementacion concreta del render (su API evoluciona: consultar antes de generar). Esta skill conserva la responsabilidad del modelo correcto.

Si el modelador esta disponible y el destino admite UI, **prefiere bundle deep-opm-pro**: el render JointJS es para casos sin entorno interactivo.

## Recursos

### Scripts

`scripts/` esta reservado para validacion EBNF de OPL-ES (apendice A de `opl-es`). En v1.0.0 esta vacio; se implementara en una iteracion siguiente cuando exista demanda real.

### Referencias

- `referencias/wizard-sd.md` — protocolo SD: del proposito a las cosas iniciales (condensado del manual metodologico).
- `referencias/refinamiento-mecanismos.md` — los 4 pares canonicos + criterios de decision.
- `referencias/checklist-validacion.md` — V-* criticos + reglas prescriptivas (R-COSA-*, R-OBJ-*, R-PROC-*, R-EST-*, R-EJEC-*) + 30 anti-patrones canonicos (AP-01 a AP-30) + checklist de cierre OPD↔OPL (12 gates del Anexo A) + heuristicas de claridad y completitud.
- `referencias/plantillas-opl-es.md` — plantillas de oracion OPL-ES por tipo de hecho (cosas, estados, links procedurales, links estructurales) con el vocabulario cerrado de verbos de `spec-forja-opl-es` §1.1 y la distincion alineado/GAP-* de §20.
- `referencias/precedencia-capas.md` — protocolo de resolucion de tensiones segun el corpus OPM/Forja SSOT ES.
- `referencias/bundle-deep-opm-pro.md` — contrato del bundle JSON `deep-opm-pro.modelo.v0`: campos requeridos / opcionales, normalizaciones aplicadas al hidratar, errores comunes de import, gates de equivalencia funcional y composicion, y contrato `LogDecisiones v0` para `re-elicitar`.
- `referencias/catalogo-de-barro.md` — anti-patrones de modelado que detienen la skill, ejemplos vivos y plantillas de pregunta clarificadora por tipo de barro.

Las referencias son **resumenes operativos curados**, no SSOT. La SSOT primaria de esta skill es el corpus OPM/Forja SSOT ES: `urn:fxsl:kb:reglas-opm-estrictas-es`, `urn:fxsl:kb:spec-forja-opd-es`, `urn:fxsl:kb:spec-forja-opl-es`, `urn:fxsl:kb:metodologia-forja-opm-es` y `urn:fxsl:kb:opm-categorial-es`. Las capas base `opm-es`/`opd-es`/`opl-es`/`manual-metodologico-opm-es` se usan como fuentes delegadas por ese corpus. La SSOT del shape JSON del bundle es el codigo del modelador (`~/projects/deep-opm-pro/app/src/serializacion/json.ts` + `app/src/modelo/tipos/`); si el codigo tensiona con la semantica OPM, manda el corpus Forja y se corrige la herramienta.

### Recursos

- `referencias/ejemplo-minimo-sd.md` — un SD didactico chico (cafetera domestica) ilustrando bootstrap, OPL-ES y bimodalidad. **No es SSOT, solo ilustracion.**
