---
_manifest:
  urn: "urn:kora:kb:catalogo-de-barro"
  type: kb
  provenance:
    created_by: "FS"
    created_at: "2026-05-08"
    source: "Derivado de la postura dialectica de modelamiento-opm v1.2.0 + experiencia de modelado OPM con operadores."
version: "1.0.0"
status: activo
nombre: catalogo-de-barro
descripcion: "Catalogo de anti-patrones de modelado OPM (barro) que la skill modelamiento-opm detecta y bloquea. Cada entrada incluye sintoma, regla en juego, pregunta clarificadora y criterio de salida."
tags: [opm, dialectico, anti-patrones, modelado, aclaracion]
lang: es
---

# Catalogo de barro

"Barro" = cualquier ambiguedad, conjetura, primitiva mal aplicada o elemento sin proposito declarado que el operador pretende plasmar en el modelo. La skill `modelamiento-opm` lo detecta, lo cita, lo bloquea y entra al estado `aclarar`.

> **Principio rector**: construir sobre barro produce modelos que se rompen al primer refinamiento. La forma de respetar al operador es devolverle rigor.

## Plantilla de pregunta clarificadora

Toda pregunta de la skill al operador tiene la forma:

```
[BARRO]    <una linea citando lo ambiguo, con la frase exacta del operador entre comillas si aplica>
[REGLA]    <R-*, AP-*, R-CAT-*, spec OPD/OPL, o "metodologia-forja: <regla>">
[PREGUNTA] <una sola pregunta concreta>
[OPCIONES] <2-4 opciones legales segun la SSOT, o "abierta dentro de <constraint>">
```

Una pregunta a la vez. Nunca batch.

## Catalogo

### B1. Nombre pobre

- **Sintoma**: el operador llama a una cosa o proceso `Sistema`, `Modulo`, `Cosa`, `Procesar`, `Gestionar`, `Manejar`, `Atender`, `Operar`, `Hacer`.
- **Regla**: `reglas-opm-estrictas-es R-NOM-*` + `metodologia-forja-opm-es`: nombres de procesos son verbos especificos de transformacion; nombres de objetos son sustantivos concretos del dominio.
- **Pregunta tipica**:
  ```
  [BARRO]    Llamaste al proceso "Procesar"; el verbo no dice que transforma ni como.
  [REGLA]    metodologia: nombre de proceso = verbo concreto de transformacion.
  [PREGUNTA] Que verbo dice exactamente que cambio produce este proceso en su transformee?
  [OPCIONES] (a) un verbo concreto que indiques; (b) cambiar a un sustantivo si lo que tienes es un objeto, no un proceso; (c) declarar que aun no sabes y dejarlo fuera del SD.
  ```
- **Salida**: nombre concreto declarado por el operador, o el operador lo declara explicitamente como placeholder consciente (decision declarada).

### B2. Proceso sin transformee

- **Sintoma**: "Quiero modelar el proceso de X" sin que el operador identifique que cosa cambia por X.
- **Regla**: `reglas-opm-estrictas-es R-PROC-1/R-PROC-2` + `metodologia-forja-opm-es §A1`: todo proceso central del SD debe transformar al menos un objeto. Sin transformee, no hay proceso OPM.
- **Pregunta tipica**:
  ```
  [BARRO]    El proceso "X" no tiene transformee identificado.
  [REGLA]    metodologia §SD: proceso central exige transformee.
  [PREGUNTA] Que objeto entra distinto y sale distinto al ejecutarse "X"?
  [OPCIONES] (a) un objeto que cambia de estado A a B; (b) un objeto que se crea por X; (c) un objeto que se consume por X; (d) ninguno - en ese caso "X" no es un proceso central y debemos revisar el SD.
  ```
- **Salida**: transformee identificado y nombrado, o el operador acepta que "X" no es proceso central.

### B3. Confusion agente / instrumento

- **Sintoma**: el operador llama "agente" a una herramienta (e.g. "el bisturi es agente") o "instrumento" a un humano/organizacion (e.g. "el cirujano es instrumento").
- **Regla**: `reglas-opm-estrictas-es AP-05` y reglas de agencia/instrumento: agente = humano/organizacion con voluntad/responsabilidad sobre la ejecucion del proceso; instrumento = ente usado para ejecutar el proceso.
- **Pregunta tipica**:
  ```
  [BARRO]    Llamaste "agente" a "Bisturi"; un bisturi es usado, no decide ejecutar.
  [REGLA]    reglas-opm-estrictas-es AP-05: agente humano/organizacion; maquina/software/IA = instrumento.
  [PREGUNTA] Quien decide ejecutar el proceso (agente) y que se usa para hacerlo (instrumento)?
  [OPCIONES] (a) agente = "Cirujano", instrumento = "Bisturi"; (b) otra distribucion que indiques; (c) declarar que no hay agente identificable y revisar si el proceso pertenece al SD.
  ```
- **Salida**: roles correctamente asignados.

### B4. Refinamiento sin motivo

- **Sintoma**: "Hagamos in-zoom de Y" sin que el operador diga que detalle se gana.
- **Regla**: `metodologia-forja-opm-es §A3/A8`: cada OPD hijo debe responder una pregunta concreta del modelo padre. Sin pregunta, no hay refinamiento — solo decoracion.
- **Pregunta tipica**:
  ```
  [BARRO]    Pediste in-zoom de "Y" sin declarar que se gana al hacerlo.
  [REGLA]    metodologia §refinamiento: hijo responde pregunta del padre.
  [PREGUNTA] Que pregunta del modelo padre se contesta con el OPD hijo de "Y"?
  [OPCIONES] (a) "como se ejecuta Y" → in-zoom de proceso; (b) "de que esta hecho Y" → unfold de objeto; (c) "en que estados puede estar Y" → state expression; (d) "Y referencia un sub-modelo externo" → sub-model composition; (e) ninguno claro, no refinar.
  ```
- **Salida**: motivo y mecanismo declarados; o el operador acepta no refinar.

### B5. Esencia ambigua

- **Sintoma**: cosa cuya naturaleza fisica vs. informacional no esta declarada y la skill no puede inferirla con certeza.
- **Regla**: `reglas-opm-estrictas-es R-OBJ-*`: toda cosa tiene esencia fisica o informacional; afecta semantica de procesos que la consumen/generan.
- **Pregunta tipica**:
  ```
  [BARRO]    "Receta" no tiene esencia declarada; podria ser objeto fisico (papel firmado) o informacional (entidad de datos).
  [REGLA]    reglas-opm-estrictas-es R-OBJ-3: esencia fisica vs. informacional.
  [PREGUNTA] La "Receta" en este sistema es objeto fisico (papel/material) o informacional (dato/concepto)?
  [OPCIONES] (a) fisica; (b) informacional; (c) ambas a la vez (declarar dos cosas distintas).
  ```
- **Salida**: esencia declarada para cada cosa.

### B6. Mezcla estructura / comportamiento sin razon

- **Sintoma**: el operador propone modelar "todo junto" lo que en realidad son hechos estructurales y procedurales mezclados sin separacion clara.
- **Regla**: `reglas-opm-estrictas-es` + specs OPD/OPL: estructura (relaciones aggregation/exhibition/generalization/classification) y comportamiento (procesos + links procedurales) son ortogonales; mezclarlos sin razon hace ilegible el OPD.
- **Pregunta tipica**:
  ```
  [BARRO]    Estas mezclando relacion estructural ("X es parte de Y") con relacion procedural ("X afecta a Y") en el mismo OPD sin separar.
  [REGLA]    reglas-opm-estrictas-es + bimodalidad OPD/OPL.
  [PREGUNTA] Cual es el OPD que estamos modelando ahora: el estructural (que cosas existen y como se componen) o el procedural (que procesos transforman a esas cosas)?
  [OPCIONES] (a) estructural primero; (b) procedural primero; (c) ambos coexisten en el SD si la cardinalidad es chica; (d) separarlos en SD + OPD hijo.
  ```
- **Salida**: separacion declarada o coexistencia justificada.

### B7. Alcance sin frontera

- **Sintoma**: "Modela el sistema de X" sin frontera explicita.
- **Regla**: `metodologia-forja-opm-es §A1/A4`: el SD declara la funcion del sistema y su frontera; lo que queda fuera es contexto.
- **Pregunta tipica**:
  ```
  [BARRO]    "Sistema de salud" es demasiado amplio sin frontera declarada.
  [REGLA]    metodologia §SD: frontera obligatoria.
  [PREGUNTA] Cual es la unidad concreta que vamos a modelar y que queda explicitamente fuera del modelo?
  [OPCIONES] (a) un servicio clinico especifico; (b) un proceso transversal especifico; (c) un dispositivo o software especifico; (d) acotar a un caso de uso unico.
  ```
- **Salida**: frontera declarada con dentro/fuera explicito.

### B8. Conjetura disfrazada de hecho

- **Sintoma**: "Imagino que asi funciona" / "Debiera ser que" / "Supongo que".
- **Regla**: el operador modela lo que sabe del sistema, no lo que imagina. Lo que imagina pertenece a un modelo aparte (escenario propuesto), no al modelo del sistema actual.
- **Pregunta tipica**:
  ```
  [BARRO]    Dijiste "imagino que el sistema funciona asi"; eso es conjetura, no observacion.
  [REGLA]    rigor: el modelo refleja lo conocido o lo declarado como propuesta, nunca conjetura silenciosa.
  [PREGUNTA] Quieres modelar (a) el sistema como es realmente — lo que requiere investigar primero — o (b) un sistema propuesto / "as if" — lo que requiere declararlo como tal en el reporte?
  [OPCIONES] (a) investigar antes; (b) declarar modelo propuesto; (c) acotar a la zona donde si tienes certeza.
  ```
- **Salida**: el operador o investiga o declara explicitamente que el modelo es propuesta.

### B9. Lenguaje difuso

- **Sintoma**: "algo asi", "mas o menos", "tipo", "como que", "una especie de".
- **Regla**: el modelo OPM es literal; no admite vaguedad. Cada cosa y cada link tienen identidad exacta.
- **Pregunta tipica**:
  ```
  [BARRO]    Dijiste "algo asi como que el doctor ve al paciente". Eso no es modelable literalmente.
  [REGLA]    OPM literal.
  [PREGUNTA] Cual es la version literal del hecho? Que cosa hace que cosa, con que rol?
  [OPCIONES] abierta, pero exige sujeto + verbo + objeto sin "tipo"/"como que".
  ```
- **Salida**: enunciado literal.

### B10. Multifuncion en un solo proceso

- **Sintoma**: proceso que el operador describe haciendo 3 transformaciones distintas a 3 objetos distintos sin orden interno.
- **Regla**: `metodologia-forja-opm-es §A0/A3` + `reglas-opm-estrictas-es R-PROC-*`: un proceso = una transformacion principal. Multifuncion = candidato a in-zoom o a separar en procesos hermanos/realizaciones comparables.
- **Pregunta tipica**:
  ```
  [BARRO]    "Atender" parece hacer al menos 3 cosas: registrar al paciente, evaluar al paciente, prescribir tratamiento.
  [REGLA]    metodologia §granularidad: 1 proceso = 1 transformacion principal.
  [PREGUNTA] Quieres (a) separar "Atender" en 3 procesos hermanos en el SD, o (b) dejar "Atender" como proceso central y hacer in-zoom mostrando los 3 sub-procesos en el OPD hijo?
  [OPCIONES] (a) hermanos; (b) in-zoom; (c) algunas separadas, otras agrupadas — declara cuales.
  ```
- **Salida**: estructura de granularidad declarada.

### B11. Estado mal aplicado

- **Sintoma**: el operador propone un estado para una cosa que es proceso, o pone como cosa lo que en realidad es un estado.
- **Regla**: `reglas-opm-estrictas-es R-PROC-4/R-EST-*`: estados solo aplican a objetos, no a procesos. "Proceso completado" no es un estado, es el final de un proceso.
- **Pregunta tipica**:
  ```
  [BARRO]    Propusiste estados para el proceso "Tramitar"; los procesos no tienen estados en OPM.
  [REGLA]    reglas-opm-estrictas-es R-PROC-4/R-EST-*: solo objetos tienen estados.
  [PREGUNTA] Lo que quieres modelar es (a) estados de un objeto que "Tramitar" transforma, o (b) sub-procesos de "Tramitar" via in-zoom?
  [OPCIONES] (a) identificar el objeto y sus estados; (b) in-zoom motivado.
  ```
- **Salida**: el modelado se reorienta a la primitiva correcta.

### B12. Link mal aplicado

- **Sintoma**: el operador propone un link cuya firma no es legal segun OPM (e.g. "consume" entre dos objetos sin proceso de por medio, "agente" desde un proceso).
- **Regla**: `reglas-opm-estrictas-es` + `spec-forja-opd-es` sobre firmas: cada tipo de link tiene origenes y destinos legales especificos.
- **Pregunta tipica**:
  ```
  [BARRO]    Propusiste un link "consume" entre dos objetos; "consume" exige proceso como destino.
  [REGLA]    reglas-opm-estrictas-es: consume = proceso consume objeto.
  [PREGUNTA] Falta declarar el proceso que consume, o el link que querias era estructural (e.g. agregacion)?
  [OPCIONES] (a) introducir proceso intermedio; (b) cambiar a link estructural; (c) revisar si el hecho que querias expresar es modelable en OPM.
  ```
- **Salida**: link con firma legal y motivo declarado.

## Criterios de cierre del estado `aclarar`

`aclarar` se cierra y devuelve al estado de origen cuando, para cada item de barro detectado:

- **Resuelto**: el operador entrego una definicion concreta y la skill la incorporo al modelo.
- **Decision declarada**: el operador eligio explicitamente una opcion suboptima y la skill registro el supuesto en el reporte.
- **Aplazado con frontera**: el operador acoto el modelo para excluir la zona barrosa, y la skill registro la exclusion en el reporte.

`aclarar` **no se cierra por cansancio**. Si el operador insiste en avanzar sin resolver el barro priorizado, la skill responde citando la regla 12 (anti-barro) y mantiene el bloqueo. La unica forma de avanzar es resolver, decidir o acotar.
