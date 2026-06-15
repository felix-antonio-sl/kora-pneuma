---
urn: urn:fxsl:kb:manual-metodologico-opm-es
nombre: manual-metodologico-opm-es
version: 3.0.1
estado: publicado
descripcion: "Manual metodológico canónico de OPM: capa procedimental de la SSOT OPM-ES — construcción del SD, refinamiento, gestión de complejidad, patrones y anti-patrones de modelado."
fuente: "SSOT OPM v3.0.1. Re-sincronizado desde la bestia (~/kora) artifacts/knowledge/fxsl/opm/opm-ssot-es/metodologia-opm-es.md (sha256:bc793ad4151f525cdab013fd2a52a8a3e0ea54e392e1d3ba49dcfb637e4772ee) el 2026-06-15; cuerpo byte-fiel. DECISION HITL 2026-06-15: pneuma toma la posta como SSOT viva de OPM (urn:kora:kb:regimen-de-ley); la bestia queda como ultimo origen historico, ya no SSOT viva. Reemplaza la migracion snapshot del 2026-06-12 (v3.0.0); incorpora los deltas v1.4.0 del corpus consolidado (6.a familia de enlace Excepcion, abanicos convergentes de habilitadores, ruta sobre habilitadores, R-FAN-PROB-1 A/B/C, R-NOM-PROC-1 deverbal, co-enmiendas de bases)."
autor: FS
creado: 2026-04-27
lang: es
tags: [opm, methodology, system-modeling, sd-construction, refinement, complexity-management, modeling-protocol, patrones, antipatterns, control-flow, error-handling, quantitative, simulation, executable-modeling, v2, ampliada]
familia: bok
depende: [urn:fxsl:kb:opm-es, urn:fxsl:kb:opl-es, urn:fxsl:kb:opd-es]
cita: [urn:fxsl:kb:opd-es, urn:fxsl:kb:opl-es, urn:fxsl:kb:opm-es]
---


# Manual metodológico de OPM (v3.0.0)

Esta versión integra los ajustes de la línea `merge-ready`: taxonomía revisada de mecanismos, organización del árbol OPD y del modelo compuesto, tipología fuerte de vistas, ejecución compuesta sin asumir un árbol global único e invariantes adicionales para identidad persistente y referencias inter-modelo.

Es la **capa procedimental canónica** del corpus OPM-ES en KORA (v3.0.0). Reemplaza a la línea `ssot/` legacy, ya removida del repositorio.

## 1 Alcance y contrato editorial

Esta especificación define la **capa metodológica canónica** del corpus OPM en español. Su responsabilidad es:

- fijar el procedimiento para construir el SD y sus refinamientos;
- establecer reglas de decisión para clasificar sistemas, distribuir enlaces y controlar complejidad;
- consolidar heurísticas, patrones y prácticas de gobernanza y simulación;
- operacionalizar el uso de herramienta sin alterar la semántica del lenguaje.

Este documento **no** redefine:

- la semántica base de OPM, que pertenece a [OPM — Núcleo conceptual](urn:fxsl:kb:opm-es);
- la realización textual canónica, que pertenece a [OPL-ES](urn:fxsl:kb:opl-es);
- la gramática gráfica y topológica del OPD, que pertenece a [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es).

Orden de precedencia del corpus:

1. [OPM — Núcleo conceptual](urn:fxsl:kb:opm-es): semántica, ontología y clases de hecho del modelo.
2. [OPL-ES](urn:fxsl:kb:opl-es): superficie textual canónica en español.
3. [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es): geometría, composición y comportamiento visual de los OPDs.
4. Esta metodología: procedimiento de modelado, criterios de decisión, gobernanza y praxis editorial-operativa.

Regla de resolución:

- si una regla metodológica contradice la semántica del lenguaje, prevalece la capa base;
- si una formulación textual contradice el contrato sintáctico de OPL-ES, prevalece OPL-ES;
- si una heurística procedimental contradice la gramática gráfica o topológica del OPD, prevalece la capa visual;
- las capacidades de herramienta NO redefinen por sí solas la semántica OPM; solo la operacionalizan.

## 2 Base heredada del corpus

Esta metodología hereda y asume como ya definidos los siguientes bloques:

| Bloque | Fuente canónica | Uso en este documento |
|--------|------------------|------------------------|
| Ontología mínima objeto-proceso | `opm-es` | fundamento semántico del procedimiento |
| Glosario base de OPM | `opm-es` | terminología estable; no se repite aquí |
| Principios de modelado OPM | `opm-es` | restricciones de alto nivel sobre toda decisión metodológica |
| Gramática textual OPL en español | `opm-opl-es` | nombres válidos y oraciones canónicas |
| Gramática visual y composición de OPDs | `opd-es` | símbolos, distribución de enlaces, refinamiento y precedencia |

Regla editorial: este documento solo reexpone una regla heredada cuando es imprescindible para tomar una decisión metodológica local. En todos los demás casos, referencia la fuente canónica correspondiente.

## 3 Definiciones operativas propias

| Término | Definición |
|---------|-----------|
| SD1 | OPD descendiente de `SD` donde el proceso principal se refina exponiendo subprocesos u objetos asociados relevantes para el siguiente nivel de detalle. |
| Objeto proveedor de beneficio | Transformado principal cuya mejora o generación materializa el valor funcional del sistema para el beneficiario. |
| Arquitectura | Combinación de estructura y comportamiento que habilita la función y hace posible emergencia a nivel de sistema. |
| Emergencia | Capacidad del sistema completo que ninguna parte individual exhibe aisladamente. |
| Objeto transiente | Objeto de vida corta creado y consumido inmediatamente entre dos procesos, sin papel observacional independiente. |
| Fuerza semántica | Criterio operativo para decidir qué enlace prevalece durante recomposición o colisión de roles; la jerarquía formal vive en `opm-visual-es`. |
| Asistente agnóstico de construcción del SD | Protocolo ordenado de interacción para cerrar las decisiones mínimas del SD sin depender de una herramienta o interfaz concreta. |
| Contenedor | Cosa refinada que aparece agrandada en el OPD hijo para contener sus refinadores. Sinónimo operativo de "refinable en contexto de OPD hijo" (cfr. `opm-visual-es` V-79). |
| Proceso inflado | Elipse del proceso agrandada para contener subprocesos en una descomposición. Es la realización visual del contenedor cuando la cosa refinada es un proceso. |

## 4 Principio metodológico rector

La metodología parte de una regla rectora única:

> El modelado DEBE comenzar por la función del sistema, continuar con la delimitación de su valor, agentes, entorno y transformados, y solo después profundizar en estructura, control, simulación y gobernanza.

Consecuencias operativas:

- la función es la semilla del modelo;
- el SD precede a cualquier refinamiento;
- la claridad local del OPD no puede lograrse violando completitud global del conjunto de OPDs;
- toda heurística de esta metodología está subordinada a la equivalencia semántica OPD–OPL y a la unicidad del hecho del modelo dentro del corpus.

## 5 Clasificación del Sistema

Antes de construir el SD, el modelador DEBE clasificar el sistema. La clasificación determina qué componentes del SD aplican.

Reglas prescriptivas por categoría:

- **Artificial**: DEBE modelarse con los 5 componentes completos
- **Natural**: NO DEBE modelarse propósito (usar "resultado"). NO DEBE modelarse ocurrencia del problema. NO hay agentes humanos — solo instrumentos. Componentes aplicables del SD: función principal (sí), habilitadores del proceso (sí, solo instrumentos), entorno (sí), propósito (no → resultado), ocurrencia del problema (no)
- **Social**: DEBE modelarse con los 5 componentes completos. Se PUEDE usar enlaces habilitadores con estado especificado para condiciones ambientales
- **Socio-técnico**: DEBE modelarse con los 5 componentes completos. Se PUEDE usar enlaces estructurales etiquetados para relaciones no fundamentales

### 5.1 Patrones de Referencia por Categoría

Los siguientes patrones sintetizan casos pedagógicos recurrentes. Son útiles para clasificar el sistema antes de construir el SD:

| Categoría | Patrón de referencia | Lección operativa |
|-----------|----------------------|-------------------|
| Artificial | `Airplane Flying`, `Battery Charging` | Hay propósito explícito, ocurrencia del problema, agentes humanos y un objeto proveedor de beneficio claramente identificable |
| Natural | `Fetus Developing`, `Rain Storm Forming` | Se modela resultado en vez de propósito; el resultado puede ser beneficioso o perjudicial; no hay agentes humanos |
| Social | `Conference Occurring` | Las condiciones ambientales PUEDEN expresarse con enlaces habilitadores con estado especificado, por ejemplo `good Weather` |
| Socio-técnico | `Online Professional Identity Managing` | Los enlaces estructurales etiquetados suelen ser necesarios para relaciones no fundamentales, por ejemplo `Profile represents User` |
| Físico con partes informacionales (sub-caso de artificial) | `Baggage Transporting` | Un sistema con seguimiento o software auxiliar SIGUE clasificándose como físico si la transformación dominante es física |

## 6 Construcción del SD — Nivel 0

El SD DEBE ser simple y claro, con mínimos detalles técnicos. Todos los interesados DEBEN poder comprender el SD sin pericia técnica.

### 6.0 Asistente Agnóstico de Construcción del SD

El asistente del SD es un **protocolo de interacción** agnóstico de herramienta. No presupone formularios, interfaz gráfica ni asistente conversacional. Cualquier implementación válida DEBE guiar al modelador por una secuencia ordenada de puntos de control y producir, al final, un SD semánticamente completo. Este asistente organiza la construcción del SD con etapas explícitas de clasificación (etapa 0), resolución de agencia (etapa 5) y verificación formal (etapa 11).

**Implementaciones válidas:** entrevista guiada, formulario estructurado, lista de verificación operativa, asistente conversacional, complemento de modelado o flujo de trabajo humano moderado.

**Regla central:** cada etapa del asistente DEBE cerrar con un hecho del modelo explicitado y listo para representarse en OPD/OPL. El asistente NO termina cuando el usuario "entiende" el sistema; termina cuando los hechos mínimos del SD quedaron decididos.

**Pre-etapa obligatoria:** antes de iniciar el asistente, el modelador DEBE clasificar el sistema según §5. La clasificación determina si se habla de propósito o resultado y si la `Ocurrencia del Problema` aplica.

| Etapa | Objetivo | Salida mínima obligatoria | Mapeo metodológico |
|-------|----------|---------------------------|---------------------|
| 0 | Clasificar sistema | Tipo: artificial / natural / social / socio-técnico | §5 |
| 1 | Fijar proceso principal | Nombre canónico del proceso principal | §6.1 |
| 2 | Identificar interesado primario | Grupo beneficiario o afectado equivalente | §6.2 |
| 3 | Fijar valor a transformar | Atributo del beneficiario/resultado + estados de entrada/salida | §6.3 |
| 4 | Fijar función principal | Objeto proveedor de beneficio + atributo funcional, si aplica | §6.4 |
| 5 | Resolver agencia humana | Conjunto de agentes válido o declaración explícita de ausencia | §6.5 |
| 6 | Delimitar el sistema | Nombre del sistema + exhibición del proceso principal | §6.6 |
| 7 | Identificar habilitadores no humanos | Conjunto de instrumentos | §6.7 |
| 8 | Fijar transformados y resultados | Entradas, afectados y salidas | §6.8 |
| 9 | Delimitar contexto externo | Objetos/procesos del entorno | §6.9 |
| 10 | Modelar problema inicial, si aplica | Ocurrencia del problema o decisión explícita de no-aplicación | §6.10 |
| 11 | Cerrar con compuerta de consistencia | Lista de verificación SD `PASA/FALLA` | §6.11 |

**Semántica de cierre por etapa:**

- Si una etapa no puede cerrarse, el asistente DEBE retroceder a la etapa anterior que bloquea la decisión.
- Si el sistema es **natural**, la etapa 10 DEBE cerrarse como `NO APLICA`, no como omisión silenciosa.
- Si el sistema transforma múltiples objetos, la etapa 4 DEBE dejar explicitado cuál es el `Objeto Proveedor de Beneficio`.
- Si no existen agentes humanos, la etapa 5 DEBE registrar `sin agentes humanos` en vez de forzar un marcador de posición.

**Contrato de salida del asistente:** un asistente agnóstico correcto entrega, como mínimo, un paquete de decisiones equivalente a:

1. tipo de sistema
2. proceso principal
3. beneficiario/afectado
4. atributo de valor + transición de estados
5. función principal
6. agentes
7. sistema + exhibición
8. instrumentos
9. conjunto de entradas/salidas
10. entorno
11. ocurrencia del problema o no-aplicación
12. verificación SD

Una herramienta PUEDE dividir o fusionar etapas por conveniencia de experiencia de uso, pero NO DEBE perder ninguna de estas salidas semánticamente necesarias.

### 6.1 Paso 1: Identificación del Proceso Principal

El nombre del proceso principal DEBE cumplir el contrato nominal de la capa correspondiente:

- en inglés, la convención canónica del corpus sigue la realización gerundiva recuperada por la capa base;
- en español, la forma canónica se rige por [OPL-ES](urn:fxsl:kb:opl-es) §1.1.

Regla metodológica: antes de aceptar un nombre, el modelador DEBE validar que expresa **acción transformadora**, no clase de objeto ni etiqueta administrativa.

**Correcto:** `Battery Charging`, `Airplane Flying`, `Preparar Empanadas`, `Verificación de Identidad`

**Incorrecto:** `Charge Battery`, `Fly Airplane`, `Batería`, `Proceso Principal`

### 6.2 Paso 2: Grupo Beneficiario

El nombre DEBE ser singular según el Principio del Nombre Singular de OPM:

- En inglés: sufijo "Group" para humanos y "Set" para inanimados
- En español: sufijo "Grupo" para humanos y "Conjunto" para inanimados

El grupo beneficiario DEBE representarse como objeto físico.

### 6.3 Paso 3: Atributo del Beneficiario y Estados

El modelador DEBERÍA definir un atributo informacional del beneficiario con exactamente dos estados (dos estados representan el escenario base — problemático y mejorado —, pero el modelador puede usar más estados si la situación lo requiere):

- **Estado de entrada** (actual/problemático)
- **Estado de salida** (deseado/mejorado)

OPL-ES: `*Proceso Principal* cambia **Atributo del Beneficiario** de **Grupo Beneficiario** de \`entrada\` a \`salida\`.` (cfr. opm-opl-es TS3)

### 6.4 Paso 4: Función Principal

El modelador DEBE identificar el transformado principal (objeto proveedor de beneficio). DEBERÍA agregar un atributo proveedor de beneficio cuyo valor cambia de problemático a satisfactorio.

Cuando el proceso transforma múltiples transformados, solo el objeto proveedor de beneficio define la función. Otros transformados (consumidos/producidos) DEBEN modelarse pero NO son parte de la función.

### 6.5 Paso 5: Identificación de Agentes

El término "agente" y el enlace de agente (círculo negro relleno) DEBEN usarse exclusivamente para humanos o grupos humanos [Semántica base: opm-es glosario 3.3]. Robots, agentes de software y sistemas IA DEBEN usar enlace de instrumento. Un robot PUEDE describirse como "agente de software embebido" en prosa, pero en el modelo DEBE usar enlace de instrumento.

Cuando el beneficiario es también agente del proceso, el modelador DEBE elegir el enlace según la precedencia semántica del corpus: si el beneficiario es transformado, el enlace transformador prevalece sobre el habilitador. La identidad humana del beneficiario se preserva en el nombre de la cosa y en su ubicación en el OPD, no mediante un segundo enlace procedimental simultáneo al mismo proceso.

OPL-ES: `**Agente** maneja *Proceso Principal*.` (cfr. opm-opl-es H1)

**Doble rol en procesos distintos:** Un objeto PUEDE ser agente de un proceso y transformado de otro proceso distinto simultáneamente. Ejemplo: Learner es agente de MOOC Learning pero también transformado (Knowledge Level cambia). Esto es distinto de la colisión agente-afectado del mismo proceso, donde prevalece el rol transformador.

## 6b Completación y Verificación del SD

Las secciones `Nb` (6b, 7b, 8b) agrupan actividades de completación y verificación asociadas al paso `N` sin incrementar la numeración principal. Cada `Nb` aloja subsecciones de paso (`§N.6`, `§N.7`, ...) que cierran el bloque de trabajo de `N` antes de pasar al siguiente paso.

### 6.6 Paso 6: Nombre del Sistema y Exhibición

El nombre por defecto DEBERÍA ser el nombre del proceso + "Sistema". El modelador PUEDE usar un nombre aceptado en su lugar.

El proceso principal DEBE modelarse como operación del sistema vía exhibición-caracterización.

### 6.7 Paso 7: Identificación de Instrumentos

El modelador DEBE identificar habilitadores no humanos requeridos durante toda la duración del proceso. Cada instrumento DEBE conectarse vía enlace de instrumento (círculo blanco vacío).

**Reclasificación por desgaste:** Cuando el desgaste, degradación o amortización de un instrumento es relevante al alcance del sistema, el modelador DEBE reclasificarlo como afectado, agregando un atributo (ej: Amortization Level) que el proceso cambia. Se DEBE modelar un proceso de mantenimiento separado.

**Correcto:** Machine es afectado de Metal Cutting (Amortization Level cambia); Machine Maintaining es proceso separado.

**Incorrecto:** Machine es instrumento de Metal Cutting cuando su desgaste es relevante al sistema (el mantenimiento queda oculto).

### 6.8 Paso 8: Objetos de Entrada/Salida

Cada objeto consumido DEBE conectarse vía enlace de consumo. Cada objeto creado DEBE conectarse vía enlace de resultado. Si un objeto es afectado (no consumido), DEBE conectarse vía par entrada-salida especificando la transición de estados.

### 6.9 Paso 9: Objetos Ambientales

Los objetos ambientales DEBEN representarse con contorno discontinuo. Un mismo objeto PUEDE ser sistémico en un modelo y ambiental en otro.

### 6.10 Paso 10: Ocurrencia del Problema

Para sistemas artificiales y sociales, el modelador DEBE modelar la ocurrencia del problema — imagen espejo del propósito. Se DEBE agregar un proceso ambiental que causa el estado problemático.

Para sistemas naturales, la ocurrencia del problema NO DEBE modelarse.

### 6.11 Verificación del SD

Las tablas de verificación de este manual usan una escala `CRÍTICA / ALTA / MEDIA / BAJA` que refleja el peso operativo de la verificación y **no es equivalente** a las marcas `DEBE / DEBERÍA / PUEDE` del cuerpo normativo. Una verificación con severidad `CRÍTICA` típicamente corresponde a una regla `DEBE`; una `ALTA` a `DEBERÍA`; pero la correspondencia no es estricta y cada tabla usa la escala que se ajuste a su grano.

| Verificación | Condición | Severidad |
|--------------|-----------|----------|
| Propósito definido | Beneficiario + atributo + transición de estados | CRÍTICA |
| Función definida | Proceso principal + transformado principal | CRÍTICA |
| Habilitadores presentes | ≥1 agente o instrumento | ALTA |
| Entorno identificado | ≥1 objeto ambiental | MEDIA |
| Ocurrencia del problema (si aplica) | Proceso ambiental causa estado negativo | MEDIA |
| OPL legible | Sentencias OPL correctas | ALTA |
| Nombres conformes | Política léxica y nominal conforme a la capa textual canónica | ALTA |
| Exhibición | Sistema exhibe proceso como operación | ALTA |
| Agentes = humanos | Ningún instrumento con enlace de agente | ALTA |

## 7 Construcción de SD1 — Refinamiento Nivel 1

SD1 refina el SD exponiendo subprocesos y objetos asociados.

### 7.1 Refinamiento de Proceso Síncrono (Descomposición)

Aplica cuando los subprocesos tienen un orden fijo y predefinido.

**Procedimiento:**

1. Crear nuevo OPD etiquetado SD1
2. Inflar el proceso principal en el centro
3. Agregar subprocesos verticalmente según **Principio de Línea de Tiempo de OPM** (primero arriba, último abajo)
4. Cada subproceso DEBE estar conectado a al menos un transformado
5. Verificar agregación-participación implícita por contención gráfica

**En el mismo diagrama vs en diagrama nuevo:**

| Variante | Descripción | Usar cuando |
|----------|-------------|-------------|
| En el mismo diagrama | El refinable aparece descompuesto en el mismo OPD (no se crea OPD nuevo) | OPD tiene espacio suficiente; pocos subprocesos |
| En diagrama nuevo | Nuevo OPD descendiente; refinable con contorno grueso en ambos OPDs | Caso prevalente; el acercamiento requiere espacio sustancial |

**Identidad semántica de la descomposición:** Cuando un proceso se descompone, sus subprocesos = partes (agregación-participación + ordenabilidad positiva), y los objetos que el proceso exhibe (vía exhibición-caracterización) = atributos del proceso. Objetos que ingresan al contexto por migración de enlaces mantienen su identidad independiente y NO son atributos del proceso. Simétricamente, cuando un objeto se descompone: objetos internos = partes, procesos internos = operaciones del objeto.

**Refinamiento no trivial:** Un proceso descompuesto DEBE contener al menos 2 subprocesos. Un despliegue DEBE revelar al menos 2 refinadores. Un refinamiento con un solo elemento hijo no agrega información al modelo y DEBERÍA eliminarse o postergarse hasta que se identifiquen más elementos.

**Elaboración progresiva de SD1:** La construcción del OPD hijo DEBERÍA seguir esta secuencia:

1. Inflar el proceso principal (contorno grueso en padre e hijo)
2. Agregar subprocesos (mínimo 2) en posición vertical según línea de tiempo
3. Renombrar subprocesos con nombres de dominio significativos (reemplazando los nombres placeholder genéricos)
4. Traer elementos externos conectados al proceso padre (objetos que participan en links del nivel superior)
5. Crear objetos internos necesarios (operandos locales del proceso)
6. Agregar estados a los objetos que participan en transformaciones
7. Crear enlaces internos entre subprocesos y objetos

**Paralelismo implícito:** Cuando dos o más subprocesos tienen el borde superior de sus elipses a la misma altura, DEBEN interpretarse como ejecutándose en paralelo. El siguiente subproceso inicia cuando el último de los paralelos termina. OPL usa la palabra clave `en paralelo` para expresar concurrencia.

**Correcto:** Subprocesos de arriba hacia abajo; paralelos a la misma altura.

**Incorrecto:** Subprocesos fuera del proceso inflado; paralelos a alturas distintas sin intención de secuencia.

### 7.2 Refinamiento de Proceso Asíncrono (Despliegue)

Aplica cuando los subprocesos son independientes y PUEDEN ocurrir en cualquier orden.

**Cuatro pares de despliegue-plegado** (uno por cada relación estructural fundamental de §7.2). Estos pares son operaciones de refinamiento-abstracción sobre relaciones estructurales; no debe confundirse su conteo con los **cuatro pares canónicos** enumerados en §8.1 (tres intra-modelo y uno inter-modelo), que categorizan las operaciones de toda la capa base y pertenecen a un nivel taxonómico distinto:

| Relación | Despliegue | Plegado |
|----------|------------|---------|
| Agregación-participación | Exponer partes del todo | Ocultar partes |
| Exhibición-caracterización | Exponer rasgos del exhibidor | Ocultar rasgos |
| Generalización-especialización | Exponer especializaciones del general | Ocultar especializaciones |
| Clasificación-instanciación | Exponer instancias de la clase | Ocultar instancias |

**Despliegue parcial:** Cuando no todos los refinadores se muestran, el símbolo de colección incompleta indica que el despliegue es incompleto.

**Caso de uso del despliegue de proceso:** Sistemas orientados a servicios y de tiempo real con funciones paralelas o auxiliares independientes de la función principal DEBERÍAN usar despliegue en vez de descomposición para refinamiento de proceso.

**Regla de decisión — Agregación vs Generalización:**

| Pregunta | Si → | No → |
|----------|------|------|
| ¿Cada subproceso es una variante/tipo del mismo patrón de transformación? | Generalización-especialización | Agregación-participación |
| ¿El todo necesita todas las partes para funcionar? | Agregación-participación | Generalización-especialización |

**Correcto:** Road Danger Warning → Vehicle Crash Alerting, Pedestrian Crash Alerting, Lane Deviation Alerting (son *tipos* de alerta → generalización).

**Incorrecto:** Usar agregación para tipos/variantes (implica que el todo necesita todas las partes simultáneamente).

### 7.3 Refinamiento de Objetos

Los objetos se refinan vía descomposición (composición espacial/estructural) y despliegue (taxonomías, rasgos, instancias). La descomposición de objetos expone partes y operaciones siguiendo el mecanismo formal de §7.1; el despliegue expone refinadores mediante las cuatro relaciones estructurales de §7.2. La posición espacial de constituyentes en una descomposición de objeto PUEDE tener significado semántico (disposición física, orden lógico).

**Proceso ambiental (patrón de ciclo de vida):** Cuando un proceso opera sobre el sistema pero no es parte de su función primaria — típicamente procesos de ciclo de vida como diseño, fabricación, mantenimiento, venta o instalación — el modelador DEBERÍA modelarlo como **proceso ambiental** (contorno discontinuo). Ejemplo canónico: el proceso de gestión del ciclo de vida de un electrodoméstico (conceptualizar, diseñar, fabricar, vender, instalar) es ambiental porque gestiona el ciclo de vida del sistema pero no entrega valor funcional directo al beneficiario. **Regla de decisión:** si el proceso no entrega valor funcional directo al beneficiario del sistema, es candidato a proceso ambiental.

**Alcance de objeto interior vs exterior:** Un objeto creado dentro de un proceso descompuesto (objeto interior) existe solo en el alcance de ese proceso y se elimina si el proceso padre se elimina. Un objeto creado a nivel SD (objeto exterior) existe independientemente y es referenciable entre múltiples OPDs. El modelador DEBE decidir el alcance basándose en si la existencia del objeto depende del proceso (interior) o es independiente (exterior). Mover un objeto exterior dentro de un proceso inflado NO lo convierte en interior — el alcance del objeto no cambia por su posición visual; el reposicionamiento es envolvimiento gráfico sin efecto semántico.

## 7b Distribución de Enlaces y Verificación de SD1

### 7.4 Distribución y Migración de Enlaces

La especificación formal completa de distribución de enlaces vive en `opm-visual-es` §11. Esta subsección extrae solo el resumen operativo necesario para la decisión metodológica:

| Tipo de enlace | Contorno exterior | Migración por defecto |
|-------------|---------------|-------------------|
| Enlace de agente | PERMITIDO (distribuye a todos) (V-36, V-104) | — |
| Enlace de instrumento | PERMITIDO (distribuye a todos) (V-36, V-104) | — |
| Enlace de efecto | PERMITIDO (distribuye a todos) (V-104) | — |
| Enlace de consumo | PROHIBIDO (V-103) | Migra al primer subproceso (V-103); reasignar |
| Enlace de resultado | PROHIBIDO (V-103) | Migra al último subproceso (V-103); reasignar |
| Enlace de evento sistémico | PROHIBIDO (V-38) | La prohibición aplica solo a eventos sistémicos; los eventos originados en objetos **ambientales** (contorno discontinuo) sí pueden cruzar el límite del proceso descompuesto para disparar subprocesos internos, conforme a V-38 |

**Procedimiento de migración de enlaces** (al hacer descomposición):

1. Al dibujar el primer subproceso `P1` dentro del proceso descompuesto `P`, la herramienta DEBE adjuntar provisionalmente a `P1` los enlaces de **consumo** y los enlaces de **entrada** con estado especificado, y adjuntar provisionalmente al último subproceso los enlaces de **resultado** y los enlaces de **salida** con estado especificado, según `opm-visual-es` V-103
2. Al agregar subprocesos subsiguientes, el modelador DEBE reasignar cada enlace transformador al subproceso específico que realmente consume, produce o completa el efecto
3. Los enlaces habilitadores DEBEN distribuirse a los subprocesos concretos donde el habilitador es necesario; si aplican a todos, pueden permanecer al nivel del contorno conforme a la capa visual
4. Ningún resumen operativo de esta subsección sustituye la regla visual canónica: ante conflicto, prevalece `opm-visual-es` §11–§12

**Enlaces de invocación implícitos** (no visibles gráficamente, implícitos por disposición vertical):

| Tipo | Semántica |
|------|-----------|
| Proceso → primer(os) subproceso(s) | Control transferido al subproceso superior al entrar al contexto descompuesto |
| Subproceso → siguiente(s) subproceso(s) | La terminación del origen inicia el siguiente |
| Último subproceso → proceso contenedor | Control retorna al proceso descompuesto tras la terminación del último subproceso |

Cuando dos o más subprocesos tienen sus bordes superiores a la misma altura, inician en paralelo; sincronización: el último en terminar inicia el siguiente.

**Antipatrón — Evento a subproceso no-primero:** El modelador NO DEBERÍA conectar un enlace de evento a un subproceso que no sea el primero (superior) dentro de una descomposición, excepto si ha verificado que todos los subprocesos anteriores pueden omitirse sin dejar precondiciones insatisfechas. Conectar a un subproceso intermedio salta los anteriores, potencialmente dejando el sistema en estado inconsistente.

**Escisión de enlaces transformadores con estado especificado:** Cuando `*P* cambia **A** de \`s1\` a \`s2\`` se descompone en P1 y P2, el modelo queda subespecificado. Resolución (cfr. opm-opl-es TS3):

1. `*P1* cambia **A** de \`s1\`.` (escisión de entrada — saca A de s1)
2. `*P2* cambia **A** a \`s2\`.` (escisión de salida — pone A en s2)

Los enlaces escindidos con modificador de control NO están permitidos (saltear un subproceso de una escisión distorsionaría la semántica del efecto).

### 7.5 Expresión y Supresión de Estados

Los estados DEBERÍAN suprimirse en el SD cuando no están conectados a ningún proceso. Los estados DEBERÍAN expresarse en SD1 donde se conectan a subprocesos.

**Estado indeterminado durante proceso activo:** Mientras un proceso que afecta está activo, el afectado está "en transición" entre estado de entrada y estado de salida. Su estado es indeterminado y NO disponible para uso por otros procesos. Si el proceso se detiene prematuramente, el afectado permanece en estado indeterminado a menos que un manejador de excepciones lo resuelva.

### 7.6 Verificación de SD1

| Verificación | Condición | Severidad |
|-------|-----------|----------|
| Subprocesos transforman | Cada subproceso ≥ 1 transformado | CRÍTICA |
| Refinamiento correcto | Síncrono → descomposición; asíncrono → despliegue | ALTA |
| Enlaces distribuidos | Consumo/resultado NO en contorno exterior | CRÍTICA |
| Sin evento a no-primero | Enlace de eventos solo al primer subproceso (o justificación explícita) | ALTA |
| Enlaces escindidos resueltos | Ningún enlace de efecto subespecificado en descomposición con múltiples subprocesos | ALTA |
| Estados expresados | Estados relevantes visibles y conectados | ALTA |
| Sin redundancia | Sin duplicación innecesaria de hechos del SD | MEDIA |

## 8 Gestión de Complejidad — Niveles 2+

### 8.1 Mecanismos de Refinamiento, Abstracción y Composición

[Semántica heredada de `opm-es` y alineada con la versión vigente ampliada del corpus. Esta sección distingue mecanismos ontológicos, artefactos contextuales y operadores derivados.]

| Mecanismo | Refinamiento | Abstracción | Uso principal | Referencia de capa base |
|-----------|-------------|-------------|---------------|--------------------------|
| Descomposición / Recomposición | Expone contenido interno | Oculta contenido interno | Procesos síncronos; objetos con partes espaciales | `opm-es` |
| Despliegue / Plegado | Expone refinadores vía relación estructural | Oculta refinadores | Procesos asíncronos; taxonomías; rasgos | `opm-es` |
| Expresión / Supresión de estados | Muestra estados | Oculta estados irrelevantes | Simplificación contextual | `opm-es` |
| Composición inter-modelo por sub-modelo | Referencia a sub-modelo | Retiro o desconexión de la referencia | Trabajo concurrente; encapsulación; compuesto por referencia | `opm-es` |

Las vistas no constituyen un mecanismo ontológico del mismo rango que los anteriores. Son artefactos contextuales para navegación, explicación o inspección.

Operaciones como `Bring`, `bring connected things`, `bring links between selected entities` y materializaciones equivalentes son operadores derivados sobre el canvas y el árbol. No deben tratarse como mecanismos de refinamiento nuevos.

**Decisión descomposición vs despliegue para procesos síncronos:** Descomposición DEBERÍA preferirse porque: (a) requiere menos símbolos, (b) genera OPL más corto, (c) reemplaza eventos/enlaces de invocación explícitos con invocación implícita de la línea de tiempo. El despliegue de procesos síncronos es semánticamente equivalente pero más verboso.

**Plegado en puertos:** variante de plegado donde la operación (proceso rasgo) se desplaza al contorno del exhibidor (objeto). Es útil cuando el modelador quiere que los rectángulos de objetos representen disposición física y tamaños relativos. El plegado en puertos también aplica a atributos de procesos.

**Resumen operativo de semi-plegado:** la semántica y las restricciones canónicas del semi-plegado viven en `opm-visual-es`. En esta capa solo aplica la decisión de uso: el modelador DEBERÍA usar semi-plegado para inspección rápida de estructura sin proliferación de OPDs y DEBERÍA evitarlo cuando oculte relaciones necesarias para el propósito del modelo.

**Refinamiento dual (ramas hermanas):** Un SD PUEDE tener ramas hermanas de distinto tipo de refinamiento. Ejemplo: SD1 como descomposición del proceso principal y SD2 como despliegue del objeto sistema. Ambos son refinamientos del mismo SD pero exploran dimensiones ortogonales: comportamiento y estructura.

**Heurística de profundidad:** Si un OPD de nivel N no agrega transformados, estados ni enlaces nuevos al modelo respecto de su padre, la refinación es probablemente innecesaria.

### 8.2 Organización del Árbol OPD y del Modelo Compuesto

Convención de etiquetado visible: `SD`, `SD1`, `SD1.1`, `SD1.2`, `SD2`, etc. Estas etiquetas son útiles para navegación humana y referencia editorial local.

Las etiquetas visibles `SDx.y` NO constituyen identidad persistente del OPD. Cada OPD DEBE tener además un identificador persistente recuperable en la serialización, por ejemplo un URI o handle persistente declarado por la implementación. Metodológicamente, quien modela NO DEBE usar `SDx.y` como identificador estable para trazabilidad externa, integración entre modelos o auditoría.

Cada modelo OPM individual tiene su propio árbol OPD. Cuando existen sub-modelos, el resultado no es un único super-árbol ontológico, sino un modelo compuesto por referencia entre modelos individuales. La regla práctica es:

- árbol OPD local para refinamiento dentro del modelo individual;
- referencias explícitas entre modelos para composición inter-modelo.

**Resumen operativo del árbol:** la regla canónica de integridad del árbol vive en `opm-visual-es`. Metodológicamente, quien modela DEBE tratar los OPDs hoja como única clase eliminable y DEBERÍA usar OPDs de vista solo como artefactos de navegación, no como nodos de refinamiento.

**Mapa del Sistema:** vista anclada al árbol que muestra el contenido de cada OPD como índice navegable mediante miniaturas o equivalentes de vista. No constituye refinamiento ni reabre el contrato OPD⇄OPL local: durante su uso, el foco metodológico es navegación, no lectura textual del modelo. Esencial para navegación en modelos complejos. El modelador DEBERÍA generarlo para modelos con más de 10 OPDs (ver §16).

**OPD Último:** representación plana obtenida por aplanamiento recursivo del árbol OPD local. Es útil para uso automatizado, pero no sustituye la identidad persistente ni la estructura explícita de referencias entre modelos.

**Especificación Completa del Sistema** — tres constructos complementarios por modelo individual:

| Constructo | Contenido |
|-----------|-----------|
| Especificación de modelo OPD | Colección de OPDs sucesivos dentro del modelo individual |
| Especificación de modelo OPL | Colección de párrafos OPL correspondientes del modelo individual, con sentencias duplicadas eliminadas |
| Especificación de modelo OPM | Presentación lado a lado: cada OPD local con su párrafo OPL a la derecha |

En modelos compuestos, la especificación global DEBE preservar estas especificaciones locales por modelo individual y declarar explícitamente la composición entre modelos. NO DEBE inferirse un único texto global solamente desde la numeración visible del árbol.

**Sub-modelos para trabajo concurrente:** Cuando múltiples modeladores trabajan en subsistemas simultáneamente, el modelador DEBERÍA separar subsistemas en sub-modelos. Las conexiones entre el modelo principal y los sub-modelos DEBEN mantenerse mínimas para reducir acoplamiento y conflictos de edición concurrente.

**Contrato de interfaz de sub-modelo:** La creación de un sub-modelo requiere un mínimo de: un objeto + un proceso conectados por exhibición-caracterización y enlace de instrumento, con un solo proceso por sub-modelo, y las cosas compartidas DEBEN estar sin refinar. Una vez creado el sub-modelo:

- Las cosas compartidas en el modelo principal NO PUEDEN recibir nuevos enlaces de refinamiento ni nuevas conexiones.
- Las cosas compartidas en el sub-modelo NO PUEDEN renombrarse, recibir nuevos estados ni eliminarse.
- NO PUEDEN agregarse nuevas cosas compartidas después de la creación del sub-modelo; si la interfaz es incorrecta, DEBE destruirse y recrearse.
- Los sub-modelos PUEDEN anidarse recursivamente, aplicando las mismas reglas de contrato en cada nivel.
- La autoridad semántica de una cosa compartida pertenece al modelo propietario; el modelo consumidor solo la referencia.
- La referencia entre modelo propietario y modelo consumidor DEBE poder resolverse mediante identificador persistente, por ejemplo URI o handle persistente, no solo mediante posición en el árbol o etiqueta visible.

### 8.3 Creación de Vistas

Metodológicamente conviene distinguir tres categorías:

| Categoría | Función | Regla de uso |
|-----------|---------|--------------|
| OPD jerárquico | Nodo del árbol local de refinamiento | Es el único que participa directamente en refinamiento y abstracción |
| Vista anclada | Artefacto de navegación ligado al árbol o a la composición | Ayuda a recorrer, resumir o inspeccionar el modelo sin crear hechos nuevos |
| Vista ad hoc | Artefacto explicativo transversal | Reúne hechos existentes para explicar un aspecto concreto |

Ejemplos típicos de vista anclada: mapa del sistema, árbol de procesos, árbol de objetos, vista de sub-modelo.

Ejemplos típicos de vista ad hoc: vista de asignación, vista motivada por simulación, vista temática para revisión de un requisito o escenario.

Reglas metodológicas:

- solo el OPD jerárquico DEBE tratarse como nodo de refinamiento;
- una vista anclada PUEDE facilitar navegación, pero NO sustituye identidad persistente;
- una vista ad hoc NO DEBE usarse como ancla de identidad ni como fuente única de trazabilidad;
- las vistas NO DEBEN editarse cuando eso altere hechos cuyo origen pertenece a OPDs jerárquicos o a modelos propietarios externos.

### 8.4 Precedencia de Enlaces durante Recomposición

La precedencia formal durante recomposición pertenece a [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es) §13. Esta metodología no la re-declara para evitar duplicación.

Reglas metodológicas de uso:

- cuando dos enlaces compiten por el mismo par cosa-proceso durante abstracción o recomposición, el modelador DEBE resolver el conflicto usando la jerarquía formal de `opm-visual-es`;
- si la recomposición produce una combinación marcada allí como inválida, el refinamiento DEBE corregirse en el nivel hijo antes de seguir abstrayendo;
- la fuerza semántica solo se usa para resolver colisiones entre hechos candidatos al mismo enlace abstracto; no autoriza a fusionar hechos distintos ni a borrar evidencia semántica legítima.

## 8b Práctica de Modelado y Gobernanza

### 8.5 Práctica Desde el Nivel Medio y Simplificación

Las prácticas de esta subsección condensan experiencia pedagógica y de modelado. Su función es operativa: ayudar a decidir cómo simplificar, recorrer y cerrar el modelo.

**Desde el nivel medio**: el modelador comienza por el nivel que mejor entiende y refina/abstrae en ambas direcciones.

**Procedimiento de simplificación de OPD sobrecargado:**

1. Identificar conjunto TO de cosas a extraer
2. Nombrar un nuevo proceso interino que los contenga
3. Ejecutar in-diagram recomposición (abstracción de enlaces + ocultamiento de contenido)
4. Crear nuevo OPD descendiente con los hechos extraidos
5. Renumerar OPDs hijos afectados

Reducción neta: `procesos_removidos + objetos_removidos + enlaces_removidos - 1` (el proceso interino agregado).

**Recorrido en profundidad para documentos complejos:** Al modelar estándares, regulaciones o documentos extensos, el modelador DEBERÍA seguir una estrategia en profundidad: profundizar completamente en una sección o cláusula antes de avanzar a la siguiente. Esto contrasta con el recorrido en anchura y permite descubrir inconsistencias locales más rápidamente.

**Cierre de la brecha objeto-proceso:** Documentos y estándares frecuentemente separan la descripción de objetos (estructura) de la descripción de procesos (comportamiento) en cláusulas independientes sin integración. El modelador DEBE conectar ambas vistas usando OPM, enlazando cada proceso con los objetos que transforma. Esta integración revela vacíos y objetos implícitos que el texto omite.

### 8.6 Emergencia como Criterio de Validación Arquitectural

El concepto de emergencia pertenece a la ingeniería de sistemas en general y aquí se adopta como criterio de validación arquitectural.

El modelador DEBE verificar que la arquitectura del sistema (estructura + comportamiento) produce al menos una capacidad emergente: una funcionalidad que el sistema completo exhibe pero ninguna parte individual posee. Si no existe emergencia, la colección de partes no constituye un sistema en el sentido de la ingeniería de sistemas basada en modelos (MBSE).

### 8.7 Gobernanza del Modelo

Las capacidades de gobernanza de esta subsección pertenecen al manual metodológico del corpus. **OPPL** (Object-Process Pseudo-Language) se usa aquí como capa de clasificación de informatividad del modelo. Su domicilio canónico es `opm-es` §3 (entrada de glosario E1).

**Aplicación de ontología:** Para consistencia terminológica en equipos, el modelador DEBERÍA configurar aplicación de ontología organizacional en tres niveles:

| Nivel | Comportamiento |
|-------|---------------|
| Ninguno | Sin restricción terminológica |
| Sugerir | Sugiere término estándar; el modelador puede ignorar |
| Forzar | Impide confirmar términos no estandarizados sin elegir una forma canónica |

Toda sustitución motivada por ontología organizacional DEBE ser trazable como política de normalización o como metadato reversible. No debe confundirse con estilado ni con corrección ortográfica silenciosa.

**Clasificación de informatividad del modelo:** Las sentencias OPPL se clasifican en: Definición, Estructural, Procedimental, Meta, Desconocida. Métricas: nivel informativo, puntaje ponderado, promedio INF, total de sentencias OPPL. El modelador DEBERÍA ejecutar clasificación periódicamente para identificar enlaces de precedencia faltantes y procesos sin entradas/salidas.

**Comparación de versiones:** El modelador DEBERÍA comparar versiones del modelo para seguimiento de mejoras y detección de regresiones. La diferencia entre versiones revela hechos agregados, modificados o eliminados.

**Resumen operativo de instancias visuales:** la regla canónica de identidad visual vive en `opm-visual-es` V-101 y V-102. Metodológicamente, ante nombres duplicados, el modelador DEBE decidir entre reutilizar la cosa existente como nueva apariencia visual, renombrar con nombre único o descartar la nueva cosa. La opción "cerrar" sin resolver NO DEBERÍA usarse.

### 8.8 Operaciones de Gestión del Modelo en Herramientas

Las siguientes capacidades son relevantes para el ciclo de vida del modelo, pero no alteran la semántica OPM:

- **Persistencia:** el modelador DEBERÍA tratar guardar/cargar como operaciones regulares de punto de control durante sesión. Compartir expone el modelo a otros usuarios con permisos de lectura o edición.
- **Permisos:** el propietario/administrador PUEDE compartir con usuarios o grupos completos, pero NO entre organizaciones distintas. Lectura precede a escritura. El modelador DEBERÍA verificar permisos antes de colaboración concurrente.
- **Exportación:** OPL puede exportarse con o sin numeración. Los OPDs pueden exportarse como imagen o PDF, ya sea para el OPD actual, el árbol completo o solo el SD. Las exportaciones DEBEN tratarse como instantáneas publicables, no como fuente de verdad del modelo.
- **Plantillas:** una herramienta puede soportar plantillas privadas, organizacionales y globales. Insertar una plantilla crea una copia local; las actualizaciones posteriores de la plantilla fuente NO se propagan a las inserciones ya hechas.
- **Reubicación del modelo:** mover modelos vía cortar/pegar conserva autoguardado e historial de versiones. El modelador DEBERÍA revisar versiones antes y después de mover o fusionar trabajo.
- **Búsqueda y navegación asistida:** operaciones como buscar, traer conectados y traer filtrado DEBERÍAN usarse para inspección localizada de un subgrafo antes de editar, especialmente en modelos con alta densidad de enlaces.

## 9 Heurísticas de Modelado Avanzado

Las heurísticas de esta sección integran práctica pedagógica, experiencia de modelado y patrones operativos consistentes con la semántica del corpus.

### 9.1 Proceso Persistente → Enlace Estructural Etiquetado

Cuando un proceso mantiene un objeto en su estado actual sin introducir un cambio neto relevante para el propósito del modelo (*Sostener*, *Mantener*, *Almacenar*, *Contener*, *Conectar*), el modelador DEBERÍA considerar reemplazarlo por un enlace estructural etiquetado.

**Justificación:** En muchos casos, un proceso de mantenimiento de estado aporta menos claridad que una relación estructural etiquetada. El enlace estructural etiquetado es más compacto y expresa mejor una relación estable cuando la temporalidad sostenida no es semánticamente central.

**Correcto:** `Cimentación soporta Casa.` (enlace estructural etiquetado, una sentencia OPL)

**Incorrecto:** `Soportar` como proceso explícito con `Cimentación` como instrumento y `Casa` como afectado cuando no se quiere modelar esfuerzo sostenido, duración o condición mantenida (múltiples enlaces y OPL más complejo sin ganancia semántica).

**Excepción:** Si mantener el estado requiere esfuerzo no trivial (ej.: el vuelo estacionario de un helicóptero requiere propulsión activa), el modelador DEBE modelar el proceso explícitamente.

### 9.2 Objeto Transiente → Enlace de Invocación

Cuando un proceso crea un objeto que el siguiente proceso consume inmediatamente sin intervención, el modelador DEBERÍA suprimir el objeto transiente y reemplazar el par creación-consumo con un enlace de invocación (forma de rayo).

**Correcto:** `Object Detecting invokes Threat Assessing.` (enlace de invocación, Spark suprimido)

**Incorrecto:** Mantener Detection Signal como objeto explícito cuando nunca es observado ni transformado por otro proceso.

### 9.3 Dualidad Estructural

Los patrones §9.1 y §9.2 son duales: enlaces estructurales etiquetados suprimen procesos que preservan estado innecesarios; enlaces de invocación suprimen objetos transientes innecesarios. El modelador DEBE aplicar ambos consistentemente.

### 9.4 Cambio de Rol entre Niveles de Detalle

Un objeto PUEDE ser instrumento en un nivel abstracto (ej: SD) y afectado en un nivel detallado (ej: SD1), siempre que el estado inicial y final sean iguales en el nivel abstracto (cambio neto = cero).

**Correcto:** Dishwasher es instrumento de Dish Washing en SD. En SD1: Loading cambia Dishwasher de empty a loaded; Unloading cambia de loaded a empty (neto = sin cambio → instrumento válido en SD).

**Incorrecto:** Declarar un objeto como instrumento en SD cuando su estado neto cambia en SD1 (debe ser afectado en ambos niveles).

### 9.5 Árbol de Decisión de Propiedades de Atributos

Al definir un atributo, el modelador DEBERÍA clasificarlo en cuatro dimensiones binarias:

| Dimensión | Valores | Criterio |
|-----------|---------|----------|
| Explicitud | explícito (por defecto) / implícito | ¿Es un objeto separado? |
| Modo | cualitativo (por defecto) / cuantitativo | ¿Valores numéricos? |
| Contacto | duro (por defecto) / blando | ¿Computable desde otros atributos? |
| Emergencia | inherente (por defecto) / emergente | ¿Al menos una parte lo exhibe? |

Atributos blandos son derivables → PUEDEN no requerir seguimiento independiente. Atributos emergentes existen solo a nivel del todo → definen la arquitectura del sistema.

### 9.6 Homogeneidad de Enlaces

Enlaces estructurales DEBEN ser homogéneos (objeto↔objeto o proceso↔proceso). Enlaces procedimentales DEBEN ser no homogéneos (objeto↔proceso). Única excepción: exhibición-caracterización permite las 4 combinaciones de perseverancia (objeto exhibe atributo-objeto, objeto exhibe operación-proceso, proceso exhibe atributo-objeto, proceso exhibe operación-proceso).

### 9.7 Enlaces Estructurales Etiquetados con Estado Especificado

Cuando un estado de un objeto corresponde o se asocia con otro objeto, el modelador DEBERÍA usar un enlace estructural etiquetado con estado especificado (conectando el estado al objeto asociado) en vez de crear procesos o objetos intermedios.

### 9.8 Atributos Discriminantes y Caracterización con Estado Especificado

Cuando las especializaciones se distinguen por un valor de atributo, el modelador DEBERÍA usar un atributo discriminante con enlaces de caracterización con estado especificado. Esto produce un OPD significativamente más compacto que repetir el atributo para cada especialización.

### 9.9 Alcance de Herencia OPM

Cada especialización DEBE heredar del general: (1) todas las partes (agregación-participación), (2) todos los rasgos (exhibición), (3) todos los enlaces estructurales etiquetados, (4) todos los enlaces procedimentales. Los estados también se heredan. Una especialización PUEDE sobreescribir estados heredados especificando estados propios.

## 9b Heurísticas de Clasificación, Detección y Patrones Avanzados

### 9.10 Relatividad de Instancia e Instancias Visuales vs Lógicas

"Instancia" es relativo al sistema de discurso. Lo que es instancia en un sistema (ej: "Taurus 2015" en comparación de autos) PUEDE ser clase con especializaciones en otro sistema (ej: autos individuales con VIN en un concesionario).

**Resumen operativo de instancia visual vs instancia lógica:** la definición formal vive en `opm-visual-es` V-101 y V-102. En esta capa solo aplica la regla de trabajo: el modelador NO DEBE confundir una nueva apariencia de la misma cosa con una relación clasificación-instanciación entre cosas distintas.

### 9.11 Clasificación de Esencia para Cosas Mixtas

Cuando una cosa tiene partes física e informacional, el modelador DEBE clasificarla como **física**. La esencia dominante del componente tangible prevalece. Ejemplo: un sistema de *Transportar Equipaje* tiene componentes informacionales (seguimiento de ubicación) pero se clasifica como físico porque el proceso involucra transporte físico.

### 9.12 Estados Directos vs Atributo + Valores (Simplificación)

Cuando un objeto tiene un solo atributo relevante, el modelador PUEDE simplificar el modelo asignando los valores del atributo como **estados directos del objeto**, eliminando el atributo intermedio.

**Correcto (simplificado):** `Fetus can be embryo or baby.` (estados directos del objeto)

**Correcto (completo):** `Fetus exhibits Developmental Stage. Developmental Stage of Fetus can be embryo or baby.` (atributo + valores)

**Regla de decisión:** Usar la forma simplificada cuando el objeto tiene un solo atributo relevante al alcance del modelo y la legibilidad mejora. Usar la forma completa cuando el objeto tiene múltiples atributos o cuando el nombre del atributo agrega información semántica no obvia.

### 9.13 Generalización como Abstracción del SD

Cuando múltiples objetos específicos del SD1 compartirían el mismo tipo de relación con el proceso principal en el SD, el modelador DEBERÍA crear un objeto general que los englobe y agregar solo ese objeto al SD, manteniendo los específicos en SD1.

**Correcto:** Road Danger Representation (general) en SD; Vehicle-in-Front Representation, Pedestrian-in-Front Representation, Lane Set Representation (específicos) en SD1 conectados vía generalización-especialización.

**Incorrecto:** Las tres representaciones específicas en SD (sobrecarga del diagrama de nivel superior).

### 9.14 Hacer Explícitos los Objetos Implícitos

Al modelar sistemas a partir de texto (estándares, regulaciones, especificaciones), el modelador DEBE identificar y modelar explícitamente los objetos que el texto menciona implícitamente. En documentos orientados a procesos, los objetos transformados por los procesos frecuentemente no se nombran. El acto de forzar la pregunta "¿qué objeto transforma este proceso?" revela entidades críticas omitidas por el autor del texto.

### 9.15 Detección de Sinónimos/Homónimos mediante Modelado Formal

OPM exige una correspondencia 1:1 entre cosas y **nombres canónicos** dentro del modelo. El modelador DEBE usar este formalismo para detectar: (a) **sinónimos**, es decir, múltiples palabras para el mismo concepto, y (b) **homónimos**, es decir, la misma palabra para conceptos distintos. Cada sinónimo detectado DEBE resolverse eligiendo un término canónico. Las variantes de superficie admitidas por OPL-ES pueden coexistir editorialmente, pero DEBEN mapear al mismo nombre canónico interno. Cada homónimo DEBE resolverse creando cosas separadas con nombres distintos.

### 9.16 Detección de Inconsistencias Texto-Diagrama

El modelado OPM de un documento existente produce como subproducto la detección de inconsistencias entre el texto principal y sus diagramas. El modelador DEBERÍA documentar estas inconsistencias como hallazgos de calidad. Ejemplo: un mismo recuadro puede representar "sistemas" en un diagrama y "procesos" en otro, sin justificación. El modelo OPM resuelve estas ambigüedades asignando perseverancia correcta (objeto vs proceso) a cada cosa.

### 9.17 Etiquetado de OPD por Cláusula de Referencia

Al modelar documentos normativos, el modelador DEBERÍA etiquetar los OPDs con las cláusulas del documento fuente (ej: `[5.2.2] System`, `[6.1] Acquisition`). Esto permite trazabilidad directa entre el modelo y el texto fuente, facilita revisión por pares, y soporta validación de cobertura.

### 9.18 Co-Agentes

Cuando un proceso requiere la participación simultánea de dos o más agentes humanos, el modelador PUEDE conectar múltiples enlaces de agente al mismo proceso. La semántica es AND implícito: todos los agentes deben estar presentes para que el proceso se habilite.

**Correcto:** `Driver and OnStar Advisor handle Call Handling.` (dos enlaces de agente al mismo proceso)

**Incorrecto:** Crear un objeto general "Agent Group" para agrupar agentes distintos — esto pierde la identidad individual de cada agente.

**Regla de decisión:** Usar co-agentes cuando los agentes participan en la misma actividad simultáneamente. Si participan en momentos distintos del proceso, el modelador DEBERÍA descomponer el proceso en subprocesos y asignar un agente a cada uno.

### 9.19 Estado Cíclico (Inicial y Final Simultáneo)

Un estado PUEDE ser simultáneamente inicial y final, modelando objetos que retornan a su estado original tras un ciclo completo de vida. No es un error — es el patrón correcto para ciclos cerrados.

**Correcto:** Dishwasher con estado `empty` marcado como inicial Y final (empty → loaded → running → empty). El ciclo cerrado confirma que el objeto retorna a su condición original.

**Incorrecto:** Duplicar estados (`empty_start`, `empty_end`) para evitar la coexistencia de marcadores — esto introduce un sinónimo falso y rompe la coherencia semántica del estado.

### 9.20 Atributos Cuantitativos con Unidad y Tipo

Todo atributo cuantitativo DEBERÍA declarar unidad de medida y tipo de dato como parte de su especificación, independientemente de si el modelo se simula. En la superficie visual o computacional, la convención recomendada es: nombre del atributo seguido de unidad entre corchetes y alias entre llaves: `Pressure [kPa] {p}`, `Height [in] {h}`, `Cost [$] {c}`. La serialización textual canónica de OPL-ES puede proyectar esa misma información sin reproducir necesariamente esa decoración literal.

**Tipos válidos:** boolean, string, integer, float, double, short, long, enumerated. El tipo restringe los valores admisibles del atributo y permite validación de rangos.

**Rangos:** El modelador DEBERÍA asignar rangos a atributos con dominio acotado. Convención canónica del corpus: intervalos con `..` y delimitadores de inclusión/exclusión, por ejemplo `[0..100]`, `(0..*)`, `[1..10], [20..30]`. Cuando un atributo hereda un rango desde una plantilla o clase, una ocurrencia más concreta PUEDE restringirlo mediante un sub-rango compatible; NO DEBERÍA ampliarlo silenciosamente sin declarar override explícito.

## 10 Control de Flujo Avanzado

### 10.1 Esperar vs Omitir — Enlaces Condicionales vs No Condicionales

| Tipo de enlace | Si el objeto/estado está ausente | Uso |
|-------------|----------------------------------|-----|
| Sin condición (sin `c`) | Proceso ESPERA indefinidamente | Proceso obligatorio — el sistema se detiene |
| Con condición (con `c`) | Proceso se SALTA | Proceso opcional — la ejecución avanza |

**Regla de decisión:** Usar enlace con condición (con `c`) cuando el proceso es opcional; usar enlace sin condición cuando el proceso es obligatorio. Error común: usar enlace sin condición para un recurso que puede no aparecer → deadlock.

### 10.2 Precedencia de Omisión sobre Espera

Cuando el conjunto de objetos previo al proceso contiene tanto enlaces de condición como enlaces sin condición, la omisión DEBE tener precedencia sobre la espera. Si cualquier objeto/estado vinculado por condición está ausente, el proceso se salta independientemente de la satisfacción de los enlaces sin condición.

### 10.3 Semántica de Enlaces de Evento (OR) vs Enlaces de Condición (AND/OR)

- **Múltiples enlaces de evento** al mismo proceso: semántica OR (cualquier evento individual basta para disparar)
- **Múltiples enlaces de condición** al mismo proceso: semántica AND para ejecución (todos deben cumplirse) pero semántica OR para omisión (falla de cualquiera causa omisión)

### 10.4 Abanicos de Enlaces XOR vs OR

| Abanico | Símbolo | Semántica | Uso |
|-----|---------|-----------|-----|
| XOR | Arco discontinuo simple | Exactamente una de las rutas | Decisiones mutuamente excluyentes |
| OR | Arco discontinuo doble | Al menos una de las rutas | Concurrencia condicional |

Para cualquier tamaño de abanico (f ≥ 2), XOR usa "exactamente uno de" y OR usa "al menos uno de". La fórmula de cardinalidad combinatorial m-de-f se desarrolla en §10.5.

### 10.5 XOR/OR Combinatorial (m-de-f)

Para f > 2, el modelador PUEDE generalizar: "exactamente m de f" (XOR combinatorial) o "al menos m de f" (OR combinatorial), donde m < f. El número m se registra junto al arco en el OPD. Modela escenarios como "2 de 3 custodios de llave deben estar presentes."

### 10.6 NOT mediante Existente/No-Existente

OPM no tiene símbolo NOT dedicado. Para modelar "proceso P ejecuta solo cuando objeto S está ausente," el modelador DEBERÍA crear estados implícitos `existente` y `no-existente` para S, y conectar `no-existente` a P con enlace de instrumento o enlace de condición de instrumento.

### 10.7 Etiquetas de Ruta para Desambiguación de Escenarios

Cuando un proceso tiene múltiples enlaces procedimentales entrantes y salientes y se necesita especificar cuál entrada mapea a cuál salida, el modelador DEBE usar etiquetas de ruta. El enlace seguido a la salida es el que tiene la misma etiqueta que el enlace de entrada. Las etiquetas de ruta proveen memoria entre entrada y salida y eliminan el requisito AND para objetos previos al proceso: solo objetos con la misma etiqueta deben coexistir.

### 10.8 Patrones de Iteración

**Patrón Conjunto-Miembro:** Adjuntar dos enlaces procedimentales del mismo tipo a un proceso — uno a un conjunto de n miembros y otro a un miembro — produce iteración automática n veces.

**Patrón Bucle:** Un enlace de invocación desde el último subproceso hacia el proceso padre descompuesto crea un bucle. Para intervalos entre iteraciones, insertar un proceso *Esperar* con restricciones de tiempo.

**Patrón Nodo de Decisión:** Para iteración con condición de terminación, usar un nodo de decisión booleano que evalúa después de cada ciclo; si "No", el enlace de invocación repite el bucle; si "Sí", la ejecución avanza al siguiente subproceso.

### 10.9 Semántica Temporal de Enlaces Transformadores

La semántica temporal de los enlaces transformadores (consumo inmediato al inicio, resultado al término, efecto con transición entre estados) se define en `opm-es` §Instancias operacionales del conjunto de objetos involucrados y en `opm-es` §Enlaces transformadores.

**Consecuencia metodológica**: esta semántica temporal es crítica para simulación y para entender la disponibilidad de objetos entre subprocesos. Al modelar, el modelador DEBE tener en cuenta que un objeto consumido NO está disponible para subprocesos posteriores, y un objeto resultante NO está disponible para subprocesos anteriores.

### 10.10 Objetos Booleanos y Ramificación

Un **objeto booleano** es un objeto informacional de doble estado generado por un proceso de decisión. Sus estados forman un par booleano (sí/no, verdadero/falso, aprobado/denegado, `≥x`/`‹x`). Cada estado se conecta vía enlaces de condición a procesos alternativos subsiguientes, implementando control si-entonces-sino.

**Generalización:** Cualquier objeto con n estados funciona como una selección de casos — cada estado PUEDE servir como origen de un enlace de condición o de instrumento para un proceso subsiguiente distinto.

**No-determinismo por defecto:** Cuando un proceso produce un objeto con n estados y no se especifica qué estado asignar (sin enlace de resultado con estado especificado), cada estado tiene probabilidad 1/n por defecto. Para forzar determinismo, el modelador DEBE conectar el enlace de resultado a un estado específico. Para asignar probabilidades distintas, el modelador DEBE usar un abanico XOR con anotaciones de probabilidad.

### 10.11 Escenarios y Repertorio de Comportamiento

Un **escenario** (hilo de ejecución) es una ruta específica a través de la jerarquía de procesos del sistema, trazada siguiendo el estado de cada objeto. En cada punto de ramificación (objeto booleano, enlaces de condición, abanico XOR), exactamente una ruta se materializa. El conjunto completo de escenarios constituye el **repertorio de comportamiento** del sistema — la totalidad de comportamientos posibles.

### 10.12 Enlaces Transformadores Condicionales (Taxonomía Completa)

[Compilación operativa — fuente canónica: opm-opl-es §7]

| Enlace | Semántica | OPL-ES |
|--------|-----------|--------|
| Consumo condicional | Si consumido existe, proceso lo consume; si no, se omite | `*Proceso* ocurre si **Objeto** existe, en cuyo caso **Objeto** se consume, de lo contrario *Proceso* se omite.` (cfr. opm-opl-es TS6) |
| Efecto condicional | Si afectado existe, proceso lo afecta; si no, se omite | `*Proceso* ocurre si **Objeto** existe, en cuyo caso *Proceso* afecta **Objeto**, de lo contrario *Proceso* se omite.` (cfr. opm-opl-es TS6) |
| Agente condicional | Si agente existe, proceso opera con agente; si no, se omite | `**Agente** maneja *Proceso* si **Agente** existe, de lo contrario *Proceso* se omite.` (cfr. opm-opl-es CH1) |
| Instrumento condicional | Si instrumento existe, proceso opera; si no, se omite | `*Proceso* ocurre si **Instrumento** existe, de lo contrario *Proceso* se omite.` |

Cada uno de estos TIENE versión con estado especificado (proceso opera si objeto está en estado específico; si no, se omite).

### 10.13 Enlaces Procedimentales con Valor Especificado

| Enlace | Semántica |
|--------|-----------|
| Enlace de establecimiento de valor | Unidireccional; establece valor de atributo independiente del valor previo |
| Enlace de efecto de valor | Bidireccional; cambia valor de atributo de uno no especificado a otro |
| Par de enlace de efecto de valor entrada-salida especificado | Cambia valor de atributo de valor de entrada específico a valor de salida específico |

Estos enlaces aplican a **valores** (estados de atributos), no a estados de objetos no-atributo.

### 10.14 Abanicos Probabilísticos

En un abanico XOR divergente probabilístico, cada enlace DEBE anotarse con una probabilidad. La suma de todas las probabilidades DEBE ser exactamente 1. Por defecto sin abanico: si un proceso crea un objeto con n estados, cada estado tiene probabilidad 1/n.

## 11 Manejo de Errores Temporales

### 11.1 Enlaces de Excepción por Sobretiempo

Cuando un proceso tiene duración máxima, el modelador DEBERÍA adjuntar un enlace de excepción por sobretiempo a un proceso de manejo de sobretiempo. Si el proceso excede su tiempo máximo, el manejador de excepciones se activa y resuelve los objetos en transición a estados permisibles.

### 11.2 Enlaces de Excepción por Subtiempo

Cuando un proceso tiene duración mínima, el modelador DEBERÍA adjuntar un enlace de excepción por subtiempo. Si el proceso se completa antes del mínimo (o es omitido, duración = 0), el manejador de subtiempo se activa.

**Patrón — Undertime como detector de omisión:** Un enlace de excepción por subtiempo en un proceso con duración mínima detecta cuando el proceso no se ejecutó (duración efectiva = 0 < mínimo positivo), activando lógica de recuperación. Esto provee un mecanismo formal para "proceso no ejecutado."

### 11.3 Resolución de Estado Indeterminado

Todo afectado en transición durante un proceso activo permanece en estado indeterminado si el proceso falla. Los manejadores de excepciones (sobretiempo/subtiempo) DEBEN resolver el objeto a un estado permisible. Sin manejo de excepciones, el objeto queda indefinido y el modelo es incompleto para simulación.

## 12 Modelado Cuantitativo y Simulación

La capa base define propiedades cuantitativas como tasa, duración y multiplicidad, pero no prescribe flujos de trabajo computacionales ni de simulación específicos. Las secciones §12.4-12.6 y §12.9 fijan la guía operativa de este manual para esos casos.

### 12.1 Tasa de Transformación

Cuando consumo, creación o cambio de estado ocurre como flujo continuo u operación multiunidad en el tiempo, el modelador DEBERÍA asignar una propiedad de tasa de transformación al enlace procedimental relevante. Tres especializaciones: tasa de consumo, tasa de generación y tasa de efecto.

### 12.2 Computación con OPM — Claridad de Roles de Operandos

Cuando se modelan operaciones aritméticas no conmutativas (*Dividir*, *Restar*), el modelador DEBE designar explícitamente los roles de operandos (dividendo vs divisor, minuendo vs sustraendo). OPM puede incrustar fórmulas en nombres de proceso (ej.: `Calcular Residuo (residuo=il-u)`) para concisión.

### 12.3 Distribución de Duración para Simulación Estocástica

El modelador PUEDE especificar una distribución de duración en la propiedad de duración de un proceso, identificando una función de distribución de probabilidad. En ejecución, cada instancia del proceso muestrea su duración independientemente. Sin distribución de duración, todas las instancias ejecutan en exactamente la duración esperada (irrealista para sistemas reales).

### 12.4 Flujo de Trabajo Computacional

Cuando se implemente el modelo en una herramienta con soporte computacional, el modelador DEBE seguir este patrón de 5 pasos:

1. **Definir objetos** con atributos computacionales (tipo: `boolean`, `string`, `integer`, `float`, `double`, `short`, `long` o `enumerated`)
2. **Asignar alias** a cada atributo computacional (ej.: `x1`, `y1`) para uso en fórmulas
3. **Crear proceso de cálculo** representado con llaves `{}` en el OPD, indicando naturaleza computacional
4. **Definir fórmula** usando los alias (ej.: `pendiente = (y2-y1)/(x2-x1)`)
5. **Conectar proceso** a objetos vía enlace de consumo/efecto para flujo de datos

**Estereotipos computacionales:** plantillas de parámetros reutilizables para patrones computacionales comunes. La herramienta puede distinguir niveles global y organizacional. Al remover un estereotipo de una cosa, el modelador DEBE elegir entre desenlazar (conservar componentes) o desenlazar y eliminar (eliminar componentes agregados).

### 12.5 Validación de Rangos

El modelador DEBERÍA asignar rangos a atributos computacionales para validación durante simulación. Sintaxis canónica: `[incluido..incluido]`, `(exclusivo..exclusivo)` y combinaciones mixtas cuando corresponda. Múltiples rangos: `[1..10], [20..30]`. `*` puede usarse como extremo abierto. El sistema valida automáticamente que los valores permanezcan en rangos válidos, distinguiendo entre la declaración persistente del rango y el valor concreto de runtime.

### 12.6 Flujo de Simulación con Entrada de Usuario

Para simulación con entrada de usuario, el modelador DEBE seguir estos 6 pasos:

1. Crear usuario como objeto físico
2. Conectar usuario al proceso vía **enlace de agente**
3. Marcar proceso para recibir entrada de usuario durante simulación
4. Crear objeto de entrada computacional para recibir valores
5. Conectar proceso al objeto de entrada vía **enlace de efecto** (requerido para actualizar objetos computacionales con valores de usuario)
6. En la computación, usar función **Entrada de Usuario** de la API predefinida

Sin los pasos 5-6, el objeto entrada no recibirá valores durante simulación.

### 12.7 Semántica Operacional en Contextos Descompuestos

Ejecutar un proceso con contexto descompuesto transfiere control recursivamente al subproceso superior del nivel más profundo. El control retorna al proceso descompuesto tras terminación del último subproceso.

**Transformaciones del conjunto de objetos involucrados por instancia:** la semántica temporal detallada por tipo de transformado (consumido, afectado, resultante) se define en `opm-es` §Instancias operacionales del conjunto de objetos involucrados. **Consecuencia metodológica:** un objeto con estados en transición (ha dejado su estado de entrada pero aún no ha llegado al de salida) es indisponible para otros procesos durante ese periodo.

### 12.8 Espacio de Estados Compuesto y Precondiciones Compuestas

El espacio de estados de un objeto es el producto cartesiano de los conjuntos de estados de todos sus atributos y partes con estados. El modelador DEBE reconocer que no todos los puntos del espacio de estados son factibles; los estados compuestos infactibles DEBERÍAN identificarse mediante modelado de procesos. Para precondiciones compuestas que abarcan múltiples atributos, el modelador DEBE usar sentencias OPL con múltiples cláusulas de condición, con cláusulas XOR numeradas conectadas por AND lógico.

### 12.9 Integración Externa e Ingesta de Datos

Cuando el modelo deja de ser solo conceptual y debe intercambiar datos con entorno externo, el modelador PUEDE usar las siguientes capacidades:

- **MQTT:** adecuado para sensores y actuadores IoT con tópicos de publicación/suscripción. Requiere configurar un servidor base y un servidor MQTT. El modelador DEBERÍA usarlo para acoplar variables computacionales a telemetría o comandos ligeros.
- **ROS:** adecuado para robots y sistemas con maestro ROS. El flujo de trabajo mínimo DEBE incluir definición de mensaje, publicación, suscripción y manejo del bucle de retroalimentación vía condiciones o iteración.
- **Importación CSV para atributos:** útil para carga masiva de instancias y valores de atributos. Restricción: el objeto destino NO DEBE ser una instancia conectada vía clasificación-instanciación. El modelador DEBERÍA previsualizar la importación y decidir si ignora existentes o crea atributos faltantes.

## 13 Modelado de Requisitos

En este corpus, el modelado de requisitos se trata como una capacidad metodológica del entorno de modelado. Las siguientes reglas aplican cuando el modelo incorpora requisitos como artefactos trazables.

### 13.1 Operaciones Disponibles

Una herramienta compatible puede agregar, remover y visualizar requisitos sobre elementos, enlaces o diagramas completos. Las relaciones mínimas recuperables en esta guía son:

- Exhibición-caracterización
- Agregación-participación

### 13.2 Convención de Trazabilidad

Cuando se use trazabilidad de requisitos, el enlace estructural etiquetado con etiqueta **`satisface`** DEBERÍA usarse como convención de trazabilidad entre artefacto y requisito cuando la capa textual activa sea OPL-ES. Si la capa textual activa es OPL-EN, la forma equivalente es **`satisfies`**.

**Correcto (OPL-ES):** `Asiento satisface Requisito RQ1 Asiento del Conductor.`

**Incorrecto:** Conectar requisitos a artefactos vía enlaces procedimentales (los requisitos no transforman ni habilitan procesos; la relación es estructural).

### 13.3 Ejemplo Mínimo

Ejemplo recuperable desde el tutorial, normalizado al registro español del corpus:

- Mirilla de puerta: la mirilla es parte de la puerta
- Restricciones dimensionales: 56-64 pulgadas
- Componentes: lente y manguitos
- Componente opcional: cubierta de mirilla
- Función: vista unidireccional para ver visitantes

### 13.4 Análisis de Vacíos y Generación Asistida

El entorno de modelado puede ofrecer capacidades auxiliares que el modelador PUEDE usar para detectar vacíos y acelerar derivación de requisitos:

- **Identificación de conocimiento faltante:** DEBERÍA usarse como heurística de detección de vacíos, no como verdad del modelo. `Pistol` sirve para filtrado rápido; `RGCN`, cuando esté disponible, ofrece mayor precisión. El umbral de confianza DEBERÍA ajustarse explícitamente antes de aceptar sugerencias.
- **Generación asistida de requisitos:** toma OPPL como insumo y genera texto de requisito, tipo de verificación, criterios de aceptación y tripletas del modelo. La salida DEBE revisarse manualmente antes de integrarla al corpus o al modelo.
- **Comparación de versiones:** el modelador DEBERÍA comparar resultados del análisis entre versiones sucesivas para distinguir mejoras reales de ruido introducido por cambios de disposición o renombrado.

## 14 Simulación y Ejecución del Modelo

### 14.1 Recorrido en Profundidad para Ejecución

La ejecución animada de un modelo OPM individual sigue un recorrido **en profundidad** de su árbol OPD local. Los tokens fluyen a lo largo de los enlaces: al llegar a un proceso descompuesto, el control se transfiere recursivamente al subproceso más profundo del modelo individual. El control retorna al nivel padre tras completar el último subproceso aplicable.

Los tokens se visualizan como valores que se pasan entre objetos y procesos: consumido (eliminado del origen), instrumento (solo lectura, permanece), resultante (creado en destino). Tokens computacionales llevan valores numéricos.

Cuando el comportamiento cruza a un sub-modelo, el cruce NO DEBE interpretarse como mera continuación implícita de un árbol global único. Debe tratarse como una transición explícita entre fronteras de modelo, gobernada por la composición inter-modelo y por la referencia persistente al sub-modelo correspondiente.

Consecuencia metodológica:

- el orden visible de `SDx.y` ayuda a navegar, pero no gobierna por sí solo la ejecución compuesta;
- si la herramienta soporta ejecución compuesta, el modelador DEBE explicitar el punto de handoff entre modelo consumidor y modelo propietario;
- si la herramienta no soporta ejecución compuesta, el modelador DEBERÍA ejecutar o simular cada modelo individual por separado y tratar la frontera como punto explícito de coordinación.

### 14.2 Transición Conceptual → Computacional

El modelador DEBE reconocer el punto en el árbol OPD donde la transición de modelado conceptual puro a modelado computacional es necesaria. Indicadores:

- Los valores numéricos específicos se vuelven necesarios para decisión de diseño
- Los estudios de compromiso requieren parámetros cuantitativos
- El proceso físico tiene una fórmula matemática subyacente (ej.: `V = V0 - (F/m)*t`)

En este punto, el modelador DEBE convertir procesos conceptuales a procesos computacionales y usar la realización soportada por la herramienta. En esta adaptación, la señal visual recuperable de proceso computacional es el uso de `{}` en el OPD.

### 14.3 Simulación Conceptual vs Ejecución Computacional

El modelador DEBE distinguir entre:

- **Simulación conceptual:** animación visual del flujo de tokens para validar orden, precondiciones y cobertura del comportamiento
- **Ejecución computacional:** corrida efectiva de fórmulas, atributos computacionales y actualización de valores

Reglas operativas:

- La velocidad de animación DEBERÍA ajustarse para hacer visibles procesos rápidos o bucles
- Si el orden observado no coincide con el esperado, el modelador DEBE revisar altura relativa de subprocesos, enlaces de control y condiciones
- Los tokens computacionales transportan valores; los conceptuales solo evidencian disponibilidad, consumo, creación o cambio de estado

## 15 Invariantes

Los invariantes se verifican operativamente en §16, donde se organizan por nivel con severidad asignada. Esta sección es un **índice compilado de verificación**, no una segunda fuente normativa: cada fila hereda su autoridad de la columna **Capa propietaria**. Esa columna indica qué capa del corpus gobierna el invariante: `opm-es`, `opl-es`, `opd-es` o `manual`.

| Invariante | Aplicación | Capa propietaria |
|-----------|-------------|------------------|
| Nombre del proceso principal cumple la política léxica de la capa textual activa del corpus | automático | `opl-es` |
| Todos los nombres de cosas son singulares | automático | `opl-es` |
| Grupo beneficiario es objeto físico | automático | `manual` |
| Atributo del beneficiario es objeto informacional | automático | `manual` |
| Exactamente un proceso principal por SD | esquema | `manual` |
| Enlace de agentes solo conecta a humanos (exclusividad) | manual | `opm-es` |
| Enlace de instrumentos solo conecta a no humanos | manual | `opm-es` |
| Todo habilitador persiste sin cambio neto tras el proceso | manual | `opm-es` |
| Objetos ambientales tienen contorno discontinuo | automático | `opd-es` |
| Sistema exhibe proceso principal vía exhibición-caracterización | manual | `manual` |
| Enlace de consumo/resultado no en contorno exterior de proceso descompuesto | automático | `opd-es` |
| Todo subproceso conectado a al menos un transformado | automático | `manual` |
| Modelo bimodal: todo OPD tiene párrafo OPL equivalente | esquema | `opm-es` |
| Un hecho del modelo aparece en al menos un OPD | esquema | `opm-es` |
| Enlaces estructurales son homogéneos (excepción: exhibición-caracterización) | automático | `opm-es` |
| Habilitadores y afectados pertenecen a Pre(P) ∩ Post(P); consumidos solo a Pre(P); resultantes solo a Post(P) — donde Pre(P) es el conjunto de objetos/estados requeridos antes de ejecutar el proceso P y Post(P) el conjunto de objetos/estados presentes tras su ejecución | manual | `opm-es` |
| Probabilidades en abanico XOR divergente probabilístico suman exactamente 1 | automático | `opm-es` |
| Subprocesos paralelos tienen borde superior de elipse a la misma altura | manual | `opd-es` |
| Enlaces escindidos con modificador de control no están permitidos | automático | `opd-es` |
| Arquitectura del sistema produce al menos una capacidad emergente | manual | `manual` |
| Los enlaces no deben cruzar áreas ocupadas por cosas | manual | `opd-es` |
| Las cosas no deben ocultarse mutuamente (excepción: plegado en puertos) | manual | `opd-es` |
| Minimizar número de enlaces y cruces de enlaces en cada OPD | manual | `manual` |
| Si se usan requisitos, la trazabilidad usa enlaces estructurales y la convención `satisface` en OPL-ES | manual | `manual` |
| Los procesos computacionales se distinguen visualmente con `{}` en el OPD | automático | `manual` |
| Sinónimos de superficie resueltos a un nombre canónico por cosa | manual | `manual` |
| Refinamiento no trivial: descomposición ≥ 2 subprocesos; despliegue ≥ 2 refinadores | automático | `manual` |
| Proceso que no entrega valor funcional directo al beneficiario DEBERÍA ser ambiental | manual | `manual` |
| Interfaz de sub-modelo congelada tras creación: sin nuevas cosas compartidas, sin renombrar, sin agregar estados | manual | `manual` |
| Cada OPD tiene identificador persistente distinto de su etiqueta visible `SDx.y` | esquema | `opm-es` |
| Toda referencia inter-modelo explicita modelo propietario y modelo consumidor | manual | `opm-es` |
| La especificación textual de un modelo compuesto preserva OPL local autocontenido por modelo individual | esquema | `opl-es` |
| Las cosas referenciadas externamente no se renombran ni reciben estados nuevos en el modelo consumidor | manual | `manual` |
| Estado cíclico (initial+final simultáneo) es válido para objetos con ciclos cerrados | manual | `manual` |
| Salida no-determinista por defecto: sin estado especificado → probabilidad 1/n por estado | manual | `manual` |

## 16 Lista de verificación de Validación

Todos los invariantes de §15 DEBEN verificarse en el nivel aplicable que indica su contexto (SD, SD1, SD2+, Cuant, Global, Requisitos). Esta tabla lista verificaciones operativas adicionales organizadas por nivel en la primera columna. La columna **Capa propietaria** usa las mismas claves que §15: `opm-es`, `opl-es`, `opd-es` y `manual`.

| Nivel | Verificación | Condición | Severidad | Capa propietaria |
|-------|-------|-----------|----------|------------------|
| SD | Sistema clasificado | Tipo determinado (artificial/natural/social/socio-técnico) | CRÍTICA | `manual` |
| SD | Propósito/resultado definido | Beneficiario + atributo + transición estados | CRÍTICA | `manual` |
| SD | Función definida | Proceso principal + transformado principal | CRÍTICA | `manual` |
| SD | Habilitadores presentes | ≥1 agente o instrumento | ALTA | `manual` |
| SD | Entorno identificado | ≥1 objeto ambiental | MEDIA | `manual` |
| SD | Ocurrencia del problema (si aplica) | Proceso ambiental causa estado negativo | MEDIA | `manual` |
| SD | Reclasificación de instrumentos | Instrumentos con desgaste relevante reclasificados a afectado | MEDIA | `manual` |
| SD1 | Refinamiento correcto | Síncrono → descomposición; asíncrono → despliegue | ALTA | `manual` |
| SD1 | Sin evento a no-primero | Enlaces de evento no a subprocesos intermedios (o justificación) | ALTA | `manual` |
| SD1 | Enlaces escindidos resueltos | Ningún enlace de efecto subespecificado en descomposición con múltiples subprocesos | ALTA | `opd-es` |
| SD1 | Estados expresados | Estados relevantes visibles y conectados | ALTA | `opd-es` |
| SD1 | Tipo asíncrono correcto | Agregación para partes; generalización para tipos | ALTA | `manual` |
| SD1 | Sin redundancia | Sin duplicación innecesaria de hechos del SD | MEDIA | `manual` |
| SD2+ | Precedencia de enlaces | Recomposición aplica matriz de precedencia | ALTA | `opd-es` |
| SD2+ | Árbol OPD válido | Etiquetado secuencial correcto | MEDIA | `opd-es` |
| SD2+ | Etiqueta visible vs identidad | `SDx.y` se usa solo para navegación y existe identificador persistente recuperable | ALTA | `opm-es` |
| SD2+ | Coherencia de cambio de rol | Instrumento en abstracto = afectado en detallado solo si cambio neto = 0 | ALTA | `manual` |
| Cuant | Operandos explícitos | Operaciones no conmutativas con roles designados | MEDIA | `manual` |
| Cuant | Flujo computacional | Atributos computacionales con tipo, alias y fórmula | MEDIA | `manual` |
| Cuant | Validación de rangos | Rangos definidos para atributos con dominio acotado | MEDIA | `manual` |
| Error | Manejo de excepciones | Procesos con límites de tiempo tienen enlaces de excepción por sobretiempo/subtiempo | MEDIA | `opm-es` |
| Error | Resolución de estado indeterminado | Afectados en transición resueltos por manejador de excepciones | MEDIA | `opm-es` |
| Global | Claridad | Ningún OPD excede 20-25 entidades | MEDIA | `manual` |
| Global | Alcance interior/exterior | Objetos interiores solo existen en alcance de su proceso padre | MEDIA | `opm-es` |
| Global | Coherencia de nombres | Sin nombres duplicados no resueltos | ALTA | `manual` |
| Global | Aplicación de ontología | Nivel configurado para organización (Sugerir o Aplicar) | MEDIA | `manual` |
| Global | Informatividad del modelo | Clasificación ejecutada; sin enlaces de precedencia faltantes críticos | MEDIA | `manual` |
| Global | Mapa del sistema | Generado para modelos con >10 OPDs | MEDIA | `manual` |
| Global | Constructos de especificación | OPD + OPL + OPM spec completos en orden en anchura | MEDIA | `manual` |
| Global | Referencia inter-modelo explícita | Sub-modelos y referencias externas declarados explícitamente; no inferidos desde layout o numeración visible | ALTA | `opm-es` |
| Global | OPL local por modelo | Cada modelo individual conserva especificación textual autocontenida | MEDIA | `opl-es` |
| Global | Refinamiento no trivial | Descomposición ≥ 2 subprocesos; despliegue ≥ 2 refinadores | ALTA | `manual` |
| Global | Profundidad justificada | Cada nivel de refinamiento agrega ≥ 1 transformado/estado/enlace nuevo | MEDIA | `manual` |
| Global | Procesos ambientales | Procesos de ciclo de vida sin valor funcional directo son ambientales | MEDIA | `manual` |
| Global | Contrato de sub-modelo | Interfaz congelada; sin adiciones post-creación | ALTA | `manual` |
| Global | Frontera propietario/consumidor | El consumidor no renombra ni agrega estados a referencias externas | ALTA | `manual` |
| Global | Plegado en puertos | Usado donde disposición física de componentes es relevante | BAJA | `manual` |
| Global | Objetos implícitos | Objetos implícitos en texto fuente identificados y modelados explícitamente | ALTA | `manual` |
| Requisitos | Trazabilidad estructural | Si se usan requisitos, se ocupan enlaces estructurales y la convención `satisface` en OPL-ES | MEDIA | `manual` |
