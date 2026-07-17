---
urn: urn:kora:artefacto:modelamiento-opm
nombre: modelamiento-opm
version: 2.0.1
estado: activo
descripcion: "Skill horizontal y dialectica para co-construir, refinar, validar y serializar modelos OPM (Object-Process Methodology, ISO 19450) con un operador humano. Anclada primero al corpus OPM/Forja SSOT ES y al modelador deep-opm-pro como mesa de trabajo interactiva; lee y escribe la mesa directamente via CLI (mesa pull/push) ademas del puente W6.0. Anti-complacencia: bloquea avance ante ambiguedad, fuerza aclaracion antes de plasmar, no construye sobre barro."
fuente: "Sublimada el 2026-06-12 desde la bestia artifacts/skills/kora/modelamiento-opm/SKILL.md v1.8.0 (sha256:18fc69305fe81700a9d5f62594267847023095338d905bee66054f891e2fa19c); cuerpo Markdown preservado salvo el path de la fibra ejemplo (recursos/ consolidada en referencias/, 9 archivos byte-identicos). El historial de versiones v1.0-v1.8 y el update_reason extenso quedan en la bestia como procedencia historica. El contrato con deep-opm-pro (sistemas_externos del payload original) vive integro en el cuerpo, seccion Composicion con deep-opm-pro. Omitidos con razon: componible_con jointjs-open-source (no encarna aun en pneuma) y target openclaw (no realizado, GENESIS seccion 4); scripts/ de la bestia estaba vacio (reservado, nunca implementado). Correccion 1.8.1 (2026-06-15): 2 de las 9 fibras (bundle-deep-opm-pro, catalogo-de-barro) portaban frontmatter _manifest anidado estilo bestia con URN no catalogado; se les retiro para dejarlas como material de apoyo en markdown puro (como el resto), coherente con que pneuma abolio los manifests anidados (GENESIS seccion 2). Esas 2 dejan de ser byte-identicas a la bestia (H3, auditoria 2026-06-15). Actualizacion 1.9.0 (2026-06-15): el corpus OPM declarado se re-sincronizo a la SSOT consolidada v1.4.0 (sexta familia de enlace Excepcion, abanicos convergentes, ruta sobre habilitadores; reglas v1.4.0, spec-opd v1.1.1, spec-opl v1.2.1, bases v3.0.x) bajo el regimen 'pneuma toma la posta de la SSOT OPM' (urn:kora:kb:regimen-de-ley). El render estatico secundario, antes delegado a la skill no migrada jointjs-open-source, ahora se hace con la libreria JointJS consultando su doc web viva urn:dev:kb:jointjs-docs (conocimiento web por convencion, declarado en el campo conocimiento); componible_con jointjs-open-source ya no aplica. Actualizacion 1.10.0 (2026-06-30): se anade el §Regimen apunte (modo borrador) — modula la Postura Dialectica como reflejo del bit esApunte del modelo activo en la mesa opforja (gemelo de esBiblioteca); suspende EXACTAMENTE las Reglas Duras #12/#13 y mantiene #1/#14/#15/#17 + integridad estructural (fence etico). Cambio menor aditivo, sin reescritura del metodo; nace en deep-opm-pro (corte modo apunte) y se eleva por solicitudes-upstream. Correccion 1.10.1 (2026-07-05): se absorbe el delta bestia aa2e2f14 (2026-06-16) en la fibra referencias/bundle-deep-opm-pro.md — el wrapper LogDecisiones v0 alinea el campo emitidoEn->generadoEl al emisor real (deep-opm-pro app/src/modelo/logDecisiones.ts, hallazgo logdec-01 de la auditoria adversarial 2026-06-15); correccion de verdad, la SSOT del shape JSON es el codigo del modelador. Ultimo delta post-migracion pendiente; los 9 KB OPM ya estaban reconciliados al sync del 2026-06-16. Actualizacion 1.11.0 (2026-07-06, corte D3 del compuesto opforja, HITL custodio): anclaje canonico con versiones vivas adjuntas (reglas v1.4.1, spec-opd v1.2.0 —enmienda que amplia R-OPD-ROT-6 estereotipos y agrega R-OPD-ROT-9 Anclaje a Pieza/Centinela—, spec-opl v1.2.2, metodologia v1.5.1); nueva seccion Limites de la mesa (frontera de capacidad, con el estado real del frente Anclaje tras PUERTA+C4); tabla de capacidades actualizada (estereotipos/vitrinas D6, superficie Piezas con Calcar/Anclar y Centinela de Drift; el dock de biblioteca fue retirado por la PUERTA). Cierra la solicitud D3 de deep-opm-pro (2026-06-24) y la peticion 2 de la solicitud de estereotipos (2026-06-22). Cambio menor aditivo, sin reescritura del metodo. Actualizacion 1.12.0 (2026-07-07, enmienda bottom-up, HITL custodio): re-sync de versiones vivas citadas (spec-opd v1.2.0->v1.3.0 con R-OPD-REF-20 Taller bottom-up, metodologia v1.5.1->v1.6.0 con A1.5 arranque bottom-up de primera clase) + nueva subseccion §Regimen bosquejo dentro de §Regimen apunte (relaja la Regla Dura #5 SD-primero durante el bosquejo; acompana OPDs sueltos sin exigir SD, integridad nunca se relaja; cuando proponer reconciliacion/graduar; adopcion via el gesto «adoptar» de la mesa, mismo constructor que el top-down, convergencia en el vinculo no en el contenido) + nota de excepcion en la Regla Dura #5. Realiza la peticion 2 de la solicitud del puente v1.12.0 y la doctrina bottom-up RESUELTA 2026-07-06; nace en deep-opm-pro (corte de apuntes + Taller bottom-up). Cambio menor aditivo, sin reescritura del metodo. Actualizacion 1.13.0 (2026-07-09, auditoria integral skill↔mesa↔SSOT↔ecosistema): nueva seccion §Puente directo mesa↔skill — CLI mesa (bun run mesa modelos|pull|push desde deep-opm-pro/app, token Bearer ~/.config/opforja/agent-token contra la instancia productiva; verificado contra app/scripts/mesa-cli.ts + src/mesa/{contextoPull,validarPush,esSinDelta}.ts): pull emite el MISMO contexto W6.0 (ley de determinismo del generador — un generador, dos consumidores) con encabezado Especie/Fuente; push con disciplina de escritura (contrato de import duro, biblioteca solo-lectura, carril por procedencia —destino sellado exige bundle del compilador—, base autosave exige confirmacion del operador, clausura sin-delta = no-op exit 4, 409 = re-pull exit 3, version etiquetada agente·nota que la vitrina colapsa como hito). W6.0 copy/paste queda como transporte fallback. Nueva Regla Dura #29 (disciplina de no-clobber del push). Tabla de capacidades actualizada: todo-nace-apunte + graduacion + gestor «Modelos» dos zonas (B'⊕D), Taller bottom-up en UI (banda «Taller», + OPD suelto, Adoptar), vitrina de revision del agente (chip + Sesion de agente · N revisiones), version visible en footer. Protocolo de handoff: push directo como camino primario con carril disponible; manual = dialogo «Modelos» → «Importar JSON». Limites de la mesa re-fechados 2026-07-09 (T1-T4 intactos; el puente directo serializa agente/operador via optimistic locking + vitrina, no es multiusuario). Higiene: §Scripts retirada (autodescripcion v1.0.0 fosil; scripts/ no existe en la fuente pneuma), anti-patrones-opforja.md indexada en §Referencias (estaba distribuida pero invisible), fibra wizard-sd.md con nota de arranques hermanos (A1.5), fibra bundle-deep-opm-pro.md con los 2 rechazos de import vigentes (estereotipoId irresoluble, ordenInzoom con ids no internos). Nace del cierre del programa mesa↔skill en deep-opm-pro (4 lineas integradas y desplegadas 2026-07-08). Cambio menor aditivo, sin reescritura del metodo. Actualizacion 1.14.0 (2026-07-14, issue #1): resincroniza spec-forja-opl-es v1.3.0/R-ENT-2-APUNTE desde kora-pneuma 4ae6428 y su realizacion opforja 6ae55b52; corrige UI contra ficha continua, CintaApunte->DialogoGraduar y el comando visible en deep-opm-pro be3ac65c; actualiza la fibra bundle contra app/src/modelo/tipos y R-OPD-REF-20. Cambio minor compatible: doctrina operacional y fibras, sin semantica OPM nueva. Actualizacion 1.15.0 (2026-07-17, cierre Testigo-Base): el puente directo liga cada actualizacion al pull que origino el bundle mediante un testigo opaco de guardado y autosave (incluida su ausencia); el servidor lo revalida dentro del commit atomico de modelo + version + consolidacion del autosave; 409 queda definido como deriva de cualquiera de ambas ramas sin escritura. La creacion omite --base y mantiene la marca apunte como segundo gesto explicito del workspace. Se clasifico erroneamente como cambio minor compatible. Actualizacion 2.0.0 (2026-07-17, correccion de contrato): reconoce como breaking el protocolo fail-closed — las actualizaciones exigen Testigo-Base y un backend sin commit atomico ya no acepta el push—; la creacion omite --base, exige especie y registra modelo + version + especie del workspace en una sola transaccion. La semantica OPM no cambia."
autor: FS
creado: 2026-04-27
lang: es
tags: [opm, iso-19450, modelado-sistemas, mbse, opd, opl-es, bimodal, modelo-conceptual, deep-opm-pro, dialectico, anti-complaciente, opforja, ssot-forja, reglas-estrictas, spec-forja-opd, spec-forja-opl, opm-categorial, wizard-sd, re-elicitar, ancla-normativa, puente-w6, generic-view, familia-v, sello-procedencia, mesa-cli, taller-bottom-up, apunte, vitrina-agente]
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
| Validez Forja | `urn:fxsl:kb:reglas-opm-estrictas-es` (v1.4.1) | SSOT primaria: validez operativa, severidad, defaults, extensiones declaradas, anti-patrones AP-01 a AP-30, checklist OPD<->OPL y Anexo C. |
| Realizacion OPD | `urn:fxsl:kb:spec-forja-opd-es` (v1.3.0) | SSOT visual de opforja: geometria, canvas, render, edicion visual, export y bisimetria visual. v1.3.0 agrega §10.4 R-OPD-REF-20 (Taller bottom-up: OPD suelto, verbo «adoptar», «OPD sin adoptar» como condicion del gate de export). |
| Realizacion OPL | `urn:fxsl:kb:spec-forja-opl-es` (v1.3.0) | SSOT textual de opforja: vocabulario cerrado, plantillas, parseo, edicion textual, roundtrip y GAPs. v1.3.0 agrega §2.0 R-ENT-2-APUNTE: en apuntes los placeholders emiten OPL en toda superficie. |
| Metodo Forja | `urn:fxsl:kb:metodologia-forja-opm-es` (v1.6.0) | SSOT primaria del metodo: A0-A8, heuristicas, lecciones Forja, bundle y disciplina humano-agente. v1.6.0 agrega A1.5 (arranque bottom-up de primera clase, hermano del SD-primero). |
| Puente formal | `urn:fxsl:kb:opm-categorial-es` | Lectura categorial no normativa para el modelador; explica linealidad, equivalencia, composicion y eje vertical sin introducir vocabulario operativo. |
| Capas base delegadas | `urn:fxsl:kb:opm-es`, `urn:fxsl:kb:opd-es`, `urn:fxsl:kb:opl-es`, `urn:fxsl:kb:manual-metodologico-opm-es` | Procedencia OPM general. Se consultan solo bajo la precedencia y fronteras documentales de la familia Forja. |

Las versiones adjuntas son las vivas al momento de esta emision (v2.0.1, 2026-07-18);
el resolutor vivo por URN es `docs/canon-opm/resolutor-urn.json` en deep-opm-pro.

## Cuando Usar

- modelar un sistema desde cero con OPM
- comunicar estructura + comportamiento + funcion sin alternar entre formalismos
- diseñar antes de implementar (codigo, organizacion, proceso)
- validar un OPD existente contra ISO 19450
- refinar un modelo en curso (in-zoom, unfold, state, sub-model)
- bocetar un modelo OPM legitimo como **apunte** (borrador sin rigor de cierre): pensar en la mesa sin que el rigor interrumpa (ver §Regimen apunte)
- trabajar directamente contra la mesa opforja: traer un modelo (`mesa pull`), auditarlo/refinarlo y devolver la revision (`mesa push`) sin que el humano transporte bytes (ver §Puente directo mesa↔skill)
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
  mesa lleva `esApunte`. La ruta visible para salir del regimen es unica:
  `CintaApunte → DialogoGraduar`; el toggle que modifica `esApunte` es un
  mecanismo interno, no un gesto alternativo expuesto. Sin flag, la Postura
  Dialectica corre completa.
- **Todo nace apunte en la mesa vigente** (corte B′⊕D, 2026-07-08): la puerta
  «Nuevo» crea un apunte instantaneo sin dialogo (auto-nombre `Apunte AAAA-MM-DD`,
  autosave desde el primer trazo). Graduar es un gesto explicito desde
  `CintaApunte` mediante `DialogoGraduar`: muestra el nombre actual (el
  autogenerado se puede conservar), una carpeta opcional —incluida «Sin
  carpeta»— y la validez con severidad de modelo. El reporte informa, pero no
  bloquea la graduacion; no existe un toggle directo expuesto. Consecuencia
  para la skill: un modelo recien nacido en la mesa ES apunte — no exigirle SD
  ni cierre de entrada;
  **proponer** graduar segun los criterios del §Regimen bosquejo. En el gestor
  «Modelos» (dos zonas rigor×rol: Trabajo · Bibliotecas) el chip de rigor muta
  in-situ al graduar.

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

### OPL de placeholders en apuntes (spec-opl R-ENT-2-APUNTE)

En una especie apunte, los objetos, procesos y estados con nombre placeholder
**DEBEN emitir OPL** —existencia y enlaces— en todas las superficies: panel,
editor libre, exports Markdown/documento canonico, puente skill
(`mesa pull`/contexto W6.0) y lectura movil. La excepcion es de regimen, no de
superficie: no se admite que el canvas y una salida textual diverjan. El
diagnostico de nominacion sigue como observacion. Al graduar mediante
`CintaApunte → DialogoGraduar`, vuelve a regir R-ENT-2; la autoria headless
permanece en regimen riguroso.

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

### Regimen bosquejo: bottom-up de primera clase (metodologia §A1.5, spec-opd R-OPD-REF-20)

Hermano del regimen apunte por el otro eje: el apunte relaja el *cierre* (#12/#13); el
bosquejo relaja el *orden de arranque* (#5 SD-primero). Conviven: un apunte es el lugar
natural del bosquejo bottom-up.

- **Acompanar fragmentos sin exigir SD.** Cuando el operador explora sin comprometer un
  SD, la skill NO fuerza el SD-primero (relaja #5 mientras dura el bosquejo). Plasma
  **OPDs sueltos** —fragmentos OPM legitimos fuera del arbol de refinamiento— como hechos
  locales; la validez de metodo queda en **observacion**; la **integridad nunca se relaja**
  (un suelto con referencia colgante se rechaza igual). Los hechos de un OPD suelto SI
  emiten OPL.
- **Cuando proponer reconciliacion.** La skill **propone** graduar (bosquejo → modelo)
  cuando: (a) el bosquejo tiene >=1 OPD suelto adoptable a una cosa existente; (b) emerge
  un candidato claro a proceso sistemico (semilla-funcion); o (c) el operador pide cerrar
  o exportar canonico (donde «OPD sin adoptar» bloquea el documento). Graduar es HITL del
  operador; la skill **no gradua por su cuenta**.
- **Adopcion via mesa, nunca a mano.** Declarar un suelto como refinamiento (in-zoom /
  unfold) de una cosa se hace por el gesto **«adoptar»** de la mesa —fija padre + declara
  refinamiento en un gesto, el MISMO constructor que el top-down (convergencia en el
  **VINCULO**; el contenido del hijo difiere: top-down auto-andamia la frontera, adoptar
  toma el suelto tal cual, R-OPD-REF-20)—; la skill nunca fabrica el refinamiento editando
  el JSON. Realizacion en la mesa: banda **«Taller»** al pie del arbol OPD (region
  derivada, no persistida), gesto **«+ OPD suelto»** y verbo **«Adoptar»**.
- **Bosquejo por el puente directo.** Un bosquejo que la skill crea en la mesa via
  `mesa push` sin destino previo se declara `--especie apunte` (el lugar natural del
  bosquejo); jamas `--especie modelo` para fragmentos sin SD reconciliado.

### Graduacion = ausencia de seccion

Graduar un apunte a modelo **no es un pipeline**: `CintaApunte` abre
`DialogoGraduar`, que muestra el nombre actual, la carpeta opcional y la
validez con su severidad real de modelo. El operador puede conservar el nombre
autogenerado, dejar el modelo sin carpeta y graduar aun con observaciones o
bloqueos: el reporte informa y deja decidir. Al confirmar, `esApunte` pasa a
ausente y los bloqueos de `validar-modelo` **re-enganchan solos** porque la
degradacion lee la **presencia** del flag. Las observaciones acumuladas son el
**checklist de cierre** (recomputadas, no persistidas), no una precondicion del
gesto. Un modelo graduado **ES un modelo**: sin rastro, sin casta, sin
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
| "trae/lee el modelo X de la mesa" / "revisa lo que hay en opforja" | `mesa pull <ref>` (§Puente directo) y rutear su cuerpo como contexto W6.0 (mismo documento, encabezado `Especie`/`Fuente` adicional) |
| "empuja/sube la revision a la mesa" / "deja esto en opforja" | tras `validar-modelo` (+ `serializar-bundle` si el origen es proto), `mesa push` bajo la Regla Dura #29 (§Puente directo) |
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
5. Con el carril de agente disponible, la entrega puede ser **directa**:
   `bun run mesa push <ref> <bundle.json> --base <Testigo-Base> --nota "…"`
   (ver §Puente directo; `Testigo-Base` proviene del pull que originó el bundle).
   El carril por procedencia del push se satisface por construccion en este
   camino (bundle sellado del compilador); un destino sellado **rechaza**
   bundles artesanales — coherente con la Regla Dura #25.
   El sello es procedencia estructural y guard contra accidentes: sus hashes
   detectan divergencia, pero no llevan firma ni autentican autoria. La skill
   usa solo el sello generado al compilar el proto actual; nunca lo copia,
   simula ni presenta como attestation criptografica.

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
«Contexto de modelado» W6.0 con pendientes `[RATIFICAR]`, llegue pegado por el
operador o traido por la propia skill via `mesa pull` (§Puente directo) — esta
skill reabre el proto-modelo o bundle de origen para incorporar resoluciones. Esto es **acto de
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

Con carril de agente disponible, la entrega preferente es `mesa push` (§Puente
directo). Para el camino manual, el bundle se importa por: gestor **«Modelos»**
→ accion **«Importar JSON»** → pegar bundle. La pestana resultante quedara
marcada con chip de persistencia `Importado` (ver ronda 19/L5 de deep-opm-pro).

## Reglas Duras

1. **Bimodalidad**: todo hecho del modelo se expresa en OPD y en OPL-ES con equivalencia semantica. Nunca emitir un hecho roto entre modalidades.
2. **Precedencia Forja**: si dos fuentes tensionan, manda el corpus OPM/Forja SSOT ES segun su matriz: reglas para validez, OPD para visual, OPL para texto/roundtrip, metodologia para metodo, categorial solo como lectura formal.
3. **Solo primitivas OPM**: objetos, procesos, estados, links. Sin atajos visuales no autorizados.
4. **OPL-ES por defecto** salvo peticion explicita de OPL-EN.
5. **SD primero**: no refinar sin SD raiz. **Excepcion (metodologia §A1.5): regimen bosquejo (bottom-up)** — el operador PUEDE trazar fragmentos sueltos antes del SD y reconciliarlos despues; al graduar, el SD vuelve a ser exigible para el modelo y sus operaciones de cierre, pero su ausencia no bloquea el gesto de graduacion (ver §Regimen apunte → Regimen bosquejo).
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
25. **Camino primario de emision (M2)**: con deep-opm-pro disponible, `serializar-bundle` emite via compilador de autoria (proto estricto → `compilarProto` → `emitirBundle` con `construirSello`): bundle con sello, round-trip/contencion/canon verificados, cruce g3 y golden-harness habilitados. El sello es procedencia estructural y guard antiaccidente, no firma ni attestation criptografica. El bundle artesanal es fallback **solo** sin deep-opm-pro, se entrega declarando sus limites (sin sello, sin cruce, sin LogDecisiones), y jamas se simula o copia un sello.
26. **El contexto W6.0 es derivado**: el «Contexto de modelado» del puente se consume, no se edita — llegue pegado por el operador o traido por `mesa pull` (es el mismo documento). Toda correccion va al proto (fuente unica) y se recompila.
27. **Notas de mesa desechables**: una `NotaMesa` registra que se pregunta la mesa, no que es la cosa. Se consume en `re-elicitar` corrigiendo el proto o respondiendo con aclaracion dirigida; nunca se fosiliza como definicion, hecho OPM ni ancla. El paso de un ancla a `vigente` ocurre solo en esta skill sobre el proto — las transiciones registradas por la app (W6.5-b) son registro, no mutacion.
28. **Regimen apunte = reflejo del flag, fence de dos reglas**: cuando el modelo de la mesa lleva `esApunte`, la skill acompana sin bloquear (ver §Regimen apunte). Suspende **EXACTAMENTE** #12 (Anti-barro) y #13 (Anti-complacencia); **mantiene** #1, #14, #15 (jamas rellena huecos), #17 y la integridad estructural. La validez OPM se degrada a observacion al margen; la integridad **sigue bloqueando**. Por R-ENT-2-APUNTE los placeholders emiten OPL en todas las superficies, con diagnostico de nominacion preservado. El flag persistido es la unica verdad: el triaje oye sinonimos y propone, el flag decide. Graduacion = `CintaApunte → DialogoGraduar`; el toggle es interno, no gesto alternativo.
29. **Puente directo con disciplina de no-clobber**: nunca `mesa push` sin `validar-modelo` local verde (en apunte: sin bloqueos de integridad); todo push a un destino existente porta, sin modificar, el `Testigo-Base` emitido por el `mesa pull` que originó ese bundle; jamas push a una biblioteca (solo-lectura); un destino con sello solo recibe bundle sellado del compilador (el proto sigue siendo la fuente); si la fuente elegida por ese pull fue autosave exige `--confirmado-por-operador`, que la skill suministra solo despues de una decision real del operador y nunca infiere. La bandera es un guard estructural contra la consolidacion accidental, no firma ni attestation criptografica; un push sin delta semantico es no-op deliberado (no fabrica revisiones); un 409 significa que cambió el guardado o el autosave y se resuelve con re-pull, jamas forzando; `--nota` siempre significativa (rotulo del hito que vera el humano); crear nuevo omite `--base`, declara `--especie` y los bosquejos nacen `apunte`. Sin carril/token, degradar a W6.0 manual sin improvisar transportes.

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
| **Inspector como ficha continua sin tabs** (Codex v2 / L3) | Las secciones permanecen apiladas y montadas; la skill no prescribe layout interno de las cosas. |
| **OPL bimodal honesto** con eco en cada cambio (ronda 20 / L2) | La skill puede entregar OPL-ES como prueba inicial; la app la mantendra sincronizada al editar. |
| **Validacion tripartita** estructural / metodologica / estilo (ronda 19 / L3, ronda 20 / L4 estados con nombres reales) | El reporte de `validar-modelo` de la skill se mapea 1:1 al `PanelMetodologia` de la app. |
| **Superficie «Piezas»: Calcar / Anclar desde bibliotecas** (2026-06-30, la PUERTA; retira el dock de biblioteca de ronda 20 / L3) | La skill puede asumir cosas reusables desde bibliotecas designadas (`esBiblioteca`, solo-lectura): **Calcar** trae una copia desacoplada (default); **Anclar** crea una referencia viva vigilada. El bundle solo declara las usadas en el modelo. |
| **Estereotipos en vitrinas + injerto de plantillas de subgrafo** (D6, 2026-06-22/23) | Catalogo aditivo `Modelo.estereotipos?` con vitrinas e injerto 1-clic (`injertarEstereotipo` clona-e-injerta con identidad fresca) + captura de seleccion como estereotipo nuevo. Contenido meta: se realiza `<<Nombre>>` en canvas y NO emite OPL nuclear (R-OPD-ROT-6); un `estereotipoId` irresoluble rechaza al importar. |
| **Anclaje a Pieza + Centinela de Drift** (2026-06-29/30, R-OPD-ROT-9) | Una cosa anclada a una Pieza de una biblioteca gobernada porta chip de 3 estados (`sincronizado` / `no-resuelto` / `divergente`); el drift se evalua a grano biblioteca (`frozenAtHash`) o Pieza (`frozenAtPieza`, vecindad radio-1); Re-sincronizar re-congela. Soltar desancla y el Ctrl+Z inmediato revierte ese gesto; una reconversion posterior no es directa. El Anclaje NO emite OPL nuclear. |
| **Puente directo mesa↔skill — CLI `mesa`** (A′, 2026-07-06/08; cierre transaccional 2026-07-17) | La skill lee (`mesa pull` = contexto W6.0 + encabezado Especie/Fuente/Testigo-Base) y escribe (`mesa push --base <Testigo-Base>`) la mesa por token, sin transporte humano. En actualizaciones, el servidor revalida guardado + autosave y consolida modelo + versión + autosave en una transacción. En creaciones, registra modelo + versión + especie del workspace en una sola transacción. Ver §Puente directo. |
| **Todo nace apunte + graduacion** (B′⊕D, 2026-07-08) | La puerta «Nuevo» crea un apunte instantaneo (`Apunte AAAA-MM-DD`, autosave desde el primer trazo); la unica ruta visible de graduacion es `CintaApunte → DialogoGraduar`, que permite conservar el nombre autogenerado, dejar «Sin carpeta» y muestra la validez real sin bloquear la decision; gestor **«Modelos»** de dos zonas rigor×rol (Trabajo con chip de rigor que muta in-situ · Bibliotecas) con accion «Importar JSON». |
| **Taller bottom-up en la UI** (B′⊕D, 2026-07-08; R-OPD-REF-20) | Banda «Taller» al pie del arbol OPD (region derivada), gesto «+ OPD suelto», verbo «Adoptar» (mismo constructor que el top-down); «OPD sin adoptar» bloquea el export canonico como condicion del gate existente, no como severidad nueva. |
| **Vitrina de revision del agente** (A′-vitrina, 2026-07-08) | Cada `mesa push` aparece al operador como chip de revision en el chrome (recargar sin perdida / ver la del agente / descartar con costo explicito, segun haya cambios locales); el historial colapsa corridas `agente·` en «Sesion de agente · N revisiones». El push jamas pisa al operador (`Testigo-Base` + 409 + dirty-bit honesto). |
| **Persistencia backend-only** (cortes C1-C5, 2026-06-06) | Modelos, versiones, workspace/carpetas, autosave y revision viven en Postgres/API con optimistic locking; no hay storage de navegador. Al importar el bundle, la app marca la pestana como `Importado` y permite `Guardar como` + versionado. |
| **Modo enlace canvas con feedback visual** (ronda 19 / L2) | La skill puede dejar enlaces declarados sin temer ambiguedad de gesto: la app refuerza la firma de enlace al editarlos. |
| **Auto-layout + fit-to-view** (Fase 0 / P0-5) | La skill no necesita resolver layout: emite cosas y enlaces, la app distribuye. |
| **Mobile solo-lectura v1 + selector de modelos** (2026-06-06/10, flag de build `VITE_MOBILE_READONLY`) | Bundles grandes son auditables desde el celular en modo lectura; tab «Modelos» lista los modelos guardados del tenant y carga read-only (sin routing por URL). |
| **Evals UX permanentes con harness Playwright** (ronda 21 / L3) | Cuando un bundle se prueba en serie, los evals de la app cubren tiempos / regresion / responsive. |
| **LogDecisiones v0 + AnclaNormativa** (W1.5/F5) | La app puede registrar transiciones de anclas pendientes; la skill consume ese log en `re-elicitar` y muta la fuente solo con ratificacion y fuente. |
| **Render headless fiel** (H1, `bun run render:headless`) | La skill obtiene PNG+SVG por OPD **fieles a opforja** sin abrir la UI ni intervencion humana; alimenta la pasada visual del agente en `revisar-visual` y el camino primario de `serializar-opd`. |
| **Golden-harness de reproducibilidad** (H2, `bun run verify:reproducible`) | Veredicto pass/fail de byte-identidad contra un golden, con diagnostico por componente del sello; reemplaza el `md5sum` manual. |
| **Sello de procedencia 3 componentes** (W5.3/G2) | `modelo.procedencia = {protoHash, autoriaVersion, layoutVersion}` viaja dentro del modelo emitido por el compilador; es trazabilidad estructural y guard antiaccidente, no firma ni attestation criptografica. El glosario fue retirado del pipeline (G2) — el proto es la fuente unica autoral. |
| **Puente de contexto 1-click** (W6.0) | Comando de paleta «Copiar contexto para la skill»: markdown con procedencia + pendientes `[RATIFICAR]` + diagnostico + OPL, dirigido a esta skill (ver §Puente W6.0). Mismo generador que `mesa pull` (ley de determinismo — un generador, dos consumidores). |
| **Chip «Vista» y panel de procedencia** (W6.3/W6.6) | El arbol OPD distingue `generic-view`; el Inspector muestra sello 3-comp, doctrina read-through y advertencia si el modelo fue editado en la app tras la emision. |
| **Anclas en el Inspector + chip «Anclas N»** (W6.4) | `SeccionAnclas` READ-ONLY por componente (entidad/enlace/OPD/modelo: claveProto, estado, referencias, nota) — las anclas nacen en el proto y solo transicionan via re-elicitacion; el arbol OPD marca los OPDs con anclas. |
| **Notas de mesa** (W6.5-a) | La mesa anota preguntas por componente desde el Inspector; viajan en el contexto W6.0 como «Notas de la mesa» y esta skill las consume en `re-elicitar`. |
| **Registro [RATIFICAR] tipificado + export LogDecisiones** (W6.5-b) | La app registra transiciones (sin retroceso) y exporta `deep-opm-pro.log-decisiones.v0` por comando de paleta (bloqueado sin sello); el ancla pasa a `vigente` solo via re-elicitacion de esta skill; L9 limpia el registro tras la re-emision. |
| **Modelo textual derivado opt-in** (G1, `emitirModeloTextual`) | `emitirBundle` puede emitir el markdown derivado del modelo (`<!-- DERIVADO — no editar a mano -->`); ningun consumidor debe mantener ese producto a mano. |
| **Canvas infinito + paneles OPL/Inspector hideables y resizables** (2026-06-03/08) | La mesa escala a modelos grandes sin que la skill pre-resuelva encuadre. |
| **Simulacion conceptual por microfases** (2026-06-06) | Runtime observable `preparacion → consumo → proceso → resultado → cierre` para validar comportamiento con el operador. |
| **Instancia productiva con login obligatorio** (`https://opforja.sanixai.com`, auth v1 2026-06-10) | La mesa tambien existe desplegada (backend Postgres; identidad single-operator, registro cerrado por CLI `auth:cuenta`). El **carril de token del agente** (2026-07-06) autentica `mesa pull/push` contra el backend configurado; `push` solo opera cuando ese backend expone el commit atomico compatible (ver §Puente directo). El loop de compilacion/render headless sigue corriendo en dev/local por diseño — el compilador esta DCE-eliminado de prod. La version desplegada es visible en el footer de «Ayuda › Atajos» (fecha de build + short SHA). |

### Que NO hace la app por la skill

- Decidir el contenido semantico del modelo (cuales son los procesos, agentes, transformees correctos para el dominio). Eso es responsabilidad de la skill + el agente invocador con conocimiento de dominio.
- Emitir el SD raiz desde un proposito en lenguaje natural sin asistencia. La app tiene estado vacio compacto, no `bootstrap-sd` automatico.
- Garantizar que un refinamiento es metodologicamente justificado. La app marca issues; la skill decide.

### Limites de la mesa (capacidad, 2026-07-09)

Frontera de **capacidad del sistema de trabajo** (que la mesa NO puede hacer hoy),
distinta de la division de labor de arriba (que la app no hace POR la skill). El
agente que ejerce esta skill NO debe prometer:

- **out-zoom automatico** (descomposicion reversa generada): el in-zoom se declara; el out-zoom es manual.
- **diff de modelos / versiones** (comparacion estructural visual): `diff.ts` fue retirado como cola colgante.
- **export a PDF real**: la exportacion canonica es Markdown determinista (`emitirDocumentoCanonico`).
- **cosimulacion numerica federada** (techo T2): la simulacion es de un modelo a la vez, no co-simulacion.
- **federacion de modelos** (techo T3) ni **multiusuario concurrente por modelo** (techo T1). El puente directo NO lo cambia: agente y operador se **serializan** (`Testigo-Base` + 409 + vitrina de revision), no co-editan en vivo.
- **razonamiento / inferencia automatica** OWL-DL u OPM (techo T4): la mesa modela y valida, no infiere.
- Del frente **Anclaje** (Calco/Anclaje/Pieza): anclar por el gesto, Calcar, el Centinela de Drift (grano biblioteca y grano Pieza) y las bibliotecas pragmaticas (`esBiblioteca`) SI estan desplegados; NO existen aun el verbo de fundacion formal `promover-a-Pieza` (registro global gobernado, admin-only), la forma OPL/render del Anclaje (C6/C7), la resolucion completa de bibliotecas externas ni la herencia mutacional (C9/C10).

### Puente directo mesa↔skill (CLI `mesa`) — camino primario de transporte

Desde 2026-07-06/08 la skill puede **leer y escribir la mesa sin que el humano
transporte bytes** (norte del programa mesa↔skill). El CLI vive en el repo del
modelador (`app/scripts/mesa-cli.ts`; alias `mesa` en `package.json`) y habla
con la instancia (productiva por defecto) por el carril de token del agente:

```bash
cd ~/projects/deep-opm-pro/app
bun run mesa modelos                    # listar: id · especie · rev · nombre
bun run mesa pull <ref>                 # contexto W6.0 + Testigo-Base a stdout
bun run mesa push <ref> <bundle.json> --base <Testigo-Base> --nota "…" [--confirmado-por-operador]
# crear nuevo: omitir --base y declarar --especie apunte|modelo
```

Configuracion: `OPFORJA_API_URL` (default `https://opforja.sanixai.com`) +
token Bearer en `~/.config/opforja/agent-token` (chmod 600; override
`OPFORJA_AGENT_TOKEN_FILE`). El carril se habilita del lado servidor con
`MODEL_AGENT_TOKEN`; si esta deshabilitado o no hay token, **degradar sin
drama al transporte manual W6.0** (siguiente seccion) — el formato es el mismo.
Si el backend aun no expone el commit atomico de revisiones, `push` recibe
404/405/501 y aborta sin escribir: usar tambien W6.0, nunca recurrir al endpoint
antiguo ni simular atomicidad con dos llamadas. **La produccion actual sigue
usando W6.0 como transporte efectivo hasta desplegar un backend compatible con
este contrato 2.0.0**; que el CLI apunte a produccion por defecto no demuestra
que ese endpoint ya este desplegado.

**`pull` ES el contexto W6.0.** Ley de determinismo del generador (un
generador, dos consumidores): el cuerpo del pull, quitando el encabezado, es
byte-igual a `exportarContextoSkill` — el mismo markdown del comando de paleta
«Copiar contexto para la skill». Se rutea con la MISMA tabla del §Puente W6.0.
El encabezado agrega tres hechos que la skill debe honrar:

- `Especie: apunte|modelo|biblioteca` — activa/desactiva el §Regimen apunte y
  el carril de solo-lectura (biblioteca).
- `Fuente: guardado rev N` **o** `Fuente: autosave no consolidado (no
  ratificado) — <fecha>` — la base del pull es el autosave **solo** si es
  estrictamente mas nuevo que lo guardado; una base autosave exigira
  confirmacion del operador al hacer push.
- `Testigo-Base: mesa-v1.…` — testigo opaco del modelo, del guardado y del
  autosave observado (incluida su ausencia). Conservarlo sin modificar junto
  al bundle: no es secreto ni permiso, sino la base que el servidor volvera a
  comprobar.

**`push` = escritura con disciplina.** El veredicto (`src/mesa/validarPush.ts`)
aplica, en orden: (1) contrato de import duro — el bundle debe hidratar a
modelo legitimo, mismo gate que el dialogo de import; (2) al **crear** (ref no
resuelto) es obligatorio declarar `--especie apunte|modelo`; (3) destino
**biblioteca = solo-lectura**, rechazo; (4) **carril por procedencia**: un
destino con sello (nacido de proto) solo acepta bundle sellado del compilador
— «edita el proto y recompila», jamas un artesanal encima; (5) base autosave
no ratificada exige `--confirmado-por-operador`: la skill solo suministra la
bandera despues de una decision real del operador y nunca la infiere. Es un
guard estructural contra un accidente, no una attestation criptografica.
Ademas, del lado cliente: **clausura sin-delta** — el bundle
se compara con la fuente exacta elegida por ese pull y, si es semanticamente
identico, NO crea revision (exit 4, no-op deliberado). Para un destino
existente, `--base <Testigo-Base>` es obligatorio. El CLI comprueba el testigo
y el servidor vuelve a comprobar guardado y autosave dentro de la misma
transaccion que guarda modelo, crea la version `agente·<nota>` y consolida el
autosave. Al crear, esa misma transaccion registra modelo, version y especie
(`apunte|modelo`) en el workspace: no existe un segundo gesto parcial. Si
cualquiera cambió, responde **409** sin escribir (exit 3): re-pull y reintentar,
jamas forzar. En `--nota`, usar un rotulo util para el humano: es lo que la mesa
muestra al colapsar la corrida como «Sesion de agente · N revisiones».

**El operador ve llegar el push (vitrina de revision).** El push no interrumpe
ni pisa al operador: la mesa muestra un chip de revision del agente en el
chrome (sin cambios locales → recargar sin perdida; con cambios locales → ver
la version del agente o descartar lo propio con costo explicito); el historial
colapsa la sesion del agente en un hito expandible. La skill no gestiona ese
lado: le basta saber que **empujar no es publicar sobre el operador** — el
`Testigo-Base`, el commit transaccional y la vitrina garantizan el no-clobber
en ambas direcciones.

Reglas del puente directo:

- **Preservar el testigo**: cada push a un destino existente usa, sin
  modificar, el `Testigo-Base` del pull que originó ese bundle. Ante 409,
  re-pull; nunca sustituir el testigo ni forzar.
- El pull es **producto derivado** (mismas reglas que el contexto W6.0):
  jamas fuente de verdad ni destino de ediciones; con sello, la correccion va
  al proto y se recompila.
- `--nota` siempre significativa (es el rotulo del hito para el humano).
- Un bosquejo nuevo se crea `--especie apunte`; `--especie modelo` solo para
  un modelo que ya cierra (o que el operador ordeno crear como tal). La
  creación omite `--base`.
- El CLI preserva metadata del record (descripcion, carpeta, archivado,
  versiones) por construccion — la skill no la re-declara ni la limpia.

### Puente W6.0: consumir el «Contexto de modelado» de opforja (transporte manual, fallback)

opforja tiene un comando de paleta **«Copiar contexto para la skill»** que
compone en un solo markdown copiable el contexto del modelo activo, dirigido a
esta skill (`opl/contextoSkill.ts::exportarContextoSkill`). Cuando el operador
pega ese markdown, la skill lo reconoce por su encabezado
(`# Contexto de modelado — <nombre>` + «Puente W6.0 deep-opm-pro → skill
modelamiento-opm») y rutea por seccion:

| Seccion del contexto | Contenido | Como la consume la skill |
|----------------------|-----------|--------------------------|
| **Procedencia** | sello 3-comp, o «_Sin sello — el modelo no fue emitido por el compilador de autoria_» | Declara la fuente estructural: con sello, el **proto** correspondiente es la fuente unica y toda correccion va alli (read-through); sin sello, declarar que no hay trazabilidad proto→modelo. El sello no autentica autoria. |
| **Pendientes [RATIFICAR]** | lista por `claveProto` con autoridad/estado/responsable + resumen | Entrada directa a `re-elicitar`: cada pendiente se resuelve por su especie (normativa → fuente; meta → acto de modelado). |
| **Notas de la mesa** (W6.5-a) | comentarios de revision anclados por componente (entidad/enlace/OPD/modelo), target resuelto por nombre | Insumo de re-elicitacion: cada nota registra que se **pregunta** la mesa. Se resuelve corrigiendo el proto (o respondiendo con una aclaracion dirigida); es **desechable** — no se fosiliza como definicion ni como hecho. |
| **Diagnostico** | JSON del panel de issues | Entrada a `validar-modelo`/`refinar-modelo`: triagear por severidad citando la regla propietaria. |
| **OPL** | markdown OPL completo del modelo | Fuente de trabajo de lectura. **No editar el OPL del contexto**: la correccion se aplica al proto y se recompila. |

Junto al contexto, la mesa puede entregar el **`LogDecisiones v0`** (comando de
paleta «Copiar log de decisiones para la skill», W6.5-b): transiciones del registro
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
  importar en la app un bundle **con sello** cuenta como cruce skill→app. En el
  flujo honesto, solo el compilador genera ese sello; la skill no lo copia ni
  falsifica y no interpreta el contador como autenticacion. La skill no
  manipula el contador; sabe que existe como observable de equilibrio y que el
  umbral lo fija el operador.
- Si el contexto llega sin que exista acceso al proto/repo de dominio, la skill
  puede igualmente auditar (diagnostico + OPL) pero debe declarar que no puede
  cerrar el loop read-through hasta tener el proto.

### Protocolo de handoff a deep-opm-pro

1. Construir el modelo segun los estados anteriores hasta `validar-modelo`.
2. Pasar a `serializar-bundle` y producir el JSON `deep-opm-pro.modelo.v0`.
3. Adjuntar el bundle al entregable, junto con OPL-ES y reporte de validacion tripartita.
4. **Camino primario con carril de agente**: entregar directo a la mesa con
   `bun run mesa push <ref> <bundle.json> --base <Testigo-Base> --nota "…"`
   (§Puente directo; el testigo viene del pull que originó el bundle; crear
   nuevo omite `--base` y exige `--especie`). El operador ve llegar la revision
   por la vitrina.
4a. **Camino manual (sin carril/token)**: indicar la apertura al usuario —
   `cd ~/projects/deep-opm-pro/app && bun run dev` (o la instancia productiva
   `https://opforja.sanixai.com`), gestor **«Modelos»** → accion **«Importar
   JSON»** → pegar el bundle. Si el bundle proviene del **compilador de
   autoria** (`emitirBundle`), lo que se pega es el campo `.json` del
   `ResultadoBundle` (el documento `{formato, modelo}` serializado), no el
   objeto resultado completo (que ademas porta reporte/avisos).
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

### Referencias

- `referencias/wizard-sd.md` — protocolo SD: del proposito a las cosas iniciales (condensado del manual metodologico).
- `referencias/refinamiento-mecanismos.md` — los 4 pares canonicos + criterios de decision.
- `referencias/checklist-validacion.md` — V-* criticos + reglas prescriptivas (R-COSA-*, R-OBJ-*, R-PROC-*, R-EST-*, R-EJEC-*) + 30 anti-patrones canonicos (AP-01 a AP-30) + checklist de cierre OPD↔OPL (12 gates del Anexo A) + heuristicas de claridad y completitud.
- `referencias/plantillas-opl-es.md` — plantillas de oracion OPL-ES por tipo de hecho (cosas, estados, links procedurales, links estructurales) con el vocabulario cerrado de verbos de `spec-forja-opl-es` §1.1 y la distincion alineado/GAP-* de §20.
- `referencias/precedencia-capas.md` — protocolo de resolucion de tensiones segun el corpus OPM/Forja SSOT ES.
- `referencias/bundle-deep-opm-pro.md` — contrato del bundle JSON `deep-opm-pro.modelo.v0`: campos requeridos / opcionales, normalizaciones aplicadas al hidratar, errores comunes de import, gates de equivalencia funcional y composicion, y contrato `LogDecisiones v0` para `re-elicitar`.
- `referencias/catalogo-de-barro.md` — anti-patrones de modelado que detienen la skill, ejemplos vivos y plantillas de pregunta clarificadora por tipo de barro.
- `referencias/anti-patrones-opforja.md` — los 30 AP-* con su accion canonica en opforja, zonas no canonizadas (R-ZNC-*) y etiquetas de ruta; complemento operativo de `checklist-validacion.md`.

Las referencias son **resumenes operativos curados**, no SSOT. La SSOT primaria de esta skill es el corpus OPM/Forja SSOT ES: `urn:fxsl:kb:reglas-opm-estrictas-es`, `urn:fxsl:kb:spec-forja-opd-es`, `urn:fxsl:kb:spec-forja-opl-es`, `urn:fxsl:kb:metodologia-forja-opm-es` y `urn:fxsl:kb:opm-categorial-es`. Las capas base `opm-es`/`opd-es`/`opl-es`/`manual-metodologico-opm-es` se usan como fuentes delegadas por ese corpus. La SSOT del shape JSON del bundle es el codigo del modelador (`~/projects/deep-opm-pro/app/src/serializacion/json.ts` + `app/src/modelo/tipos/`); si el codigo tensiona con la semantica OPM, manda el corpus Forja y se corrige la herramienta.

### Recursos

- `referencias/ejemplo-minimo-sd.md` — un SD didactico chico (cafetera domestica) ilustrando bootstrap, OPL-ES y bimodalidad. **No es SSOT, solo ilustracion.**
