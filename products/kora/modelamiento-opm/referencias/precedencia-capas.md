# Precedencia del corpus OPM/Forja SSOT ES

Cuando dos fuentes aparentan dar instrucciones distintas para un mismo hecho, la
skill resuelve la tension primero dentro del corpus OPM/Forja SSOT ES. Las capas
base OPM se consultan como procedencia o soporte solo cuando el corpus Forja las
delega.

## Matriz operativa

| Plano | URN propietaria | Manda sobre |
|-------|-----------------|-------------|
| Validez | `urn:fxsl:kb:reglas-opm-estrictas-es` | que hechos son validos, severidad, defaults, extensiones declaradas, AP-*, gates OPD<->OPL y Anexo C |
| Visual | `urn:fxsl:kb:spec-forja-opd-es` | geometria, canvas, render, interaccion visual, export OPD y bisimetria visual |
| Textual | `urn:fxsl:kb:spec-forja-opl-es` | vocabulario OPL, plantillas, parseo, edicion textual, roundtrip y GAPs |
| Metodo | `urn:fxsl:kb:metodologia-forja-opm-es` | camino de modelamiento, heuristicas, calidad, lecciones Forja y uso humano-agente |
| Formal | `urn:fxsl:kb:opm-categorial-es` | explicacion categorial bajo la superficie; no introduce reglas para el modelador |
| Base delegada | `opm-es`, `opd-es`, `opl-es`, `manual-metodologico-opm-es` | semantica y procedencia general cuando la familia Forja las invoca |

Regla corta: **reglas decide si se puede; OPD/OPL deciden como se realiza;
metodologia decide como se llega; categorial explica por que; herramienta no
decide norma.**

## Tensiones tipicas

| Tension | Quien manda | Razonamiento |
|---------|-------------|--------------|
| Una heuristica recomienda un hecho que reglas prohibe | `reglas-opm-estrictas-es` | el metodo no autoriza hechos invalidos |
| Un ejemplo OPL usa verbo fuera del enum cerrado | `spec-forja-opl-es` | la superficie textual de opforja es cerrada |
| Una figura OPD usa glifo o canal visual no canonico | `spec-forja-opd-es` si es visual; `reglas-opm-estrictas-es` si altera validez | separar modalidad de semantica |
| OPD y OPL expresan hechos distintos | volver al hecho; luego aplicar `spec-forja-opd-es` + `spec-forja-opl-es` | la bimodalidad exige equivalencia, no eleccion |
| Dos realizaciones hermanas difieren internamente | `reglas-opm-estrictas-es` R-CAT-EQ-2 | equivalen solo si comparten firma de frontera |
| Un in-zoom cambia roles de frontera | `reglas-opm-estrictas-es` R-CAT-EQ-3 | la descomposicion debe preservar la firma del out-zoom |
| El codigo de deep-opm-pro acepta algo que el corpus rechaza | corpus Forja | la herramienta implementa; no legisla |
| La capa base parece permitir algo que Forja restringe | corpus Forja, salvo correccion documental explicita | Forja operacionaliza/restringe para opforja |

## Empate entre realizaciones OPD y OPL

OPD y OPL no compiten por autoridad semantica. Si parecen contradecirse:

1. Identificar el hecho subyacente.
2. Validar el hecho contra `reglas-opm-estrictas-es`.
3. Realizarlo visualmente segun `spec-forja-opd-es`.
4. Realizarlo textualmente segun `spec-forja-opl-es`.
5. Si no puede expresarse en ambas modalidades sin perdida, el hecho esta mal
   capturado o pertenece a una zona GAP/deuda que debe declararse.

## Cuando consultar al usuario

Consultar antes de modelar cuando:

- el hecho del usuario admite mas de una interpretacion semantica;
- el dominio impone restricciones externas que OPM no decide;
- el corpus Forja declara una zona no canonizada o GAP y el usuario debe elegir
  entre aplazar, acotar o aceptar deuda declarada.

La consulta cita la regla Forja propietaria. Las citas a capas base van despues,
como procedencia.

## Anti-patrones de precedencia

- **"El corpus base lo permite, entonces Forja lo permite"**:
  NO. La familia Forja es el perfil operativo primario.
- **"El manual recomienda algo, por tanto no bloquea"**: NO. La validez vive en
  `reglas-opm-estrictas-es`.
- **"OPD y OPL difieren; elijo la modalidad mas comoda"**: NO. Se corrige el
  hecho hasta restaurar equivalencia.
- **"La app lo importa, entonces es canonico"**: NO. Importar no equivale a
  cumplir canon.
- **"Si no encuentro una regla, asumo que esta permitido"**: NO. Declarar vacio,
  GAP o extension; no inventar.

## Como citar la capa propietaria

Preferir este orden de cita:

- "Por `reglas-opm-estrictas-es` R-PROC-2, el proceso explicito debe declarar
  transformee; no puedo cerrar el SD sin objeto afectado."
- "Por `spec-forja-opl-es` §1.1, la frase usa `genera`, no `produce`, porque el
  enum OPL de opforja es cerrado."
- "Por `spec-forja-opd-es`, este glifo es visual; si cambia validez, vuelvo a
  reglas."
- "Por `urn:fxsl:kb:metodologia-forja-opm-es` A0.4, dos alternativas de solucion solo son la
  misma funcion si comparten firma de frontera."
- "Por `opm-categorial-es`, esto se lee como equivalencia por frontera, pero ese
  vocabulario no se expone al modelador."
