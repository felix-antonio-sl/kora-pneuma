
# modelamiento-opm

## Propósito

Modelar cualquier dominio con la ontología mínima de OPM: **objetos** que
existen y **procesos** que los transforman. Integrar estructura, comportamiento
y función en un mismo modelo, con representación gráfica OPD y textual OPL
cuando el entregable las requiera.

La skill custodia la semántica OPM; el operador aporta la verdad del dominio.
No inventa hechos para completar una figura ni convierte una incertidumbre en
decisión.

## Revelación progresiva obligatoria

Al activarse, leer sólo este archivo. Clasificar primero el entregable y cargar
una única ruta. No leer todas las referencias ni todo el corpus por prevención.

| Ruta | Disparador | Carga adicional |
|---|---|---|
| `conceptual-textual-minimo` | explicar OPM, identificar función/objetos/procesos, proponer un modelo pequeño o un OPL conceptual | ninguna por defecto |
| `modelado-formal` | validar un modelo, producir OPL-ES parseable, elegir links o refinamientos | el URN propietario y la referencia puntual de la tabla inferior |
| `operacion-forja` | OPD visual, apunte/boceto, bundle, mesa pull/push, W6.0, deep-opm-pro o render | `referencias/operacion-profunda.md` y sólo las fibras que esa operación cite |

Si el pedido cabe en una ruta menor, no escalar. Mesa, bundle, JSON, JointJS,
CLI y render permanecen fuera de `conceptual-textual-minimo`.

## Ruta `conceptual-textual-minimo`

Usarla para responder directamente con un modelo conceptual pequeño y legible.
Los hechos explícitos del prompt ya son entradas válidas: no volver a
preguntarlos. Marcar como `inferido` sólo lo derivado y como `abierto` lo que el
operador no decidió.

Una incertidumbre afecta sólo la afirmación o el efecto que depende de ella.
Avanzar con el resto, usando un supuesto explícito cuando sea reversible. La
presencia de varios verbos tampoco decide por sí sola que existan varios
sistemas: contrastar transformación, transformees, resultado y frontera.

### Núcleo suficiente

1. **Función**: beneficio o transformación que el sistema debe producir.
2. **Transformee**: objeto que cambia por el proceso principal.
3. **Estado inicial y resultado**: cómo se distingue el objeto antes y después.
4. **Agente e instrumento**: sólo si el prompt los aporta o son necesarios para
   explicar quién ejecuta y con qué; no inventarlos.
5. **Entorno**: dejar fuera lo que no participa en la función solicitada.

Prueba mínima de coherencia:

```text
¿Existe un proceso nombrado como transformación?
¿Ese proceso cambia al menos un objeto identificable?
¿La función puede leerse como resultado de esa transformación?
¿Cada entidad agregada está sustentada por el prompt o marcada como propuesta?
```

### Salida mínima

Entregar, según lo pedido:

- una frase de función;
- lista breve de objetos y procesos;
- relación `objeto inicial → proceso → objeto resultante`;
- OPL conceptual breve si ayuda;
- una sola pregunta si falta una decisión que impide identificar la
  transformación.

No afirmar que un OPL conceptual es parseable por opforja. Si el usuario exige
OPL-ES estricto o roundtrip, pasar a `modelado-formal`.

## Ruta `modelado-formal`

Aplicar la misma semilla funcional, pero resolver cada regla desde su fuente
propietaria. Cargar sólo lo necesario:

| Necesidad | Fuente |
|---|---|
| validez, severidad, anti-patrones | `urn:fxsl:kb:reglas-opm-estrictas-es` + `referencias/checklist-validacion.md` |
| vocabulario OPL-ES y roundtrip | `urn:fxsl:kb:spec-forja-opl-es` + `referencias/plantillas-opl-es.md` |
| geometría/semántica OPD | `urn:fxsl:kb:spec-forja-opd-es` |
| refinamiento | `referencias/refinamiento-mecanismos.md` |
| arranque System Diagram | `referencias/wizard-sd.md` |
| conflicto entre capas | `referencias/precedencia-capas.md` |
| barro semántico concreto | `referencias/catalogo-de-barro.md` |

### Postura dialéctica proporcional

- Corregir una primitiva OPM mal aplicada y nombrar la regla propietaria.
- No bloquear por una duda irrelevante al entregable.
- Si falta una decisión material, preguntar **una cosa a la vez**: hecho
  faltante, impacto y alternativas legales.
- Una decisión deliberada del operador se conserva como decisión aunque no sea
  óptima; una aproximación vaga no se presenta como hecho.
- Riesgo o dominio no amplían automáticamente el modelo: sólo aumentan
  verificación y autoridad humana.

Validar primero estructura, luego método y al final legibilidad. Distinguir
`PASS`, `FAIL`, `ABSENT` y `NOT_RUN`.

## Ruta `operacion-forja`

Leer [operacion-profunda.md](referencias/operacion-profunda.md) sólo cuando el
entregable exige opforja o sus productos. Esa referencia conserva el contrato
completo de:

- régimen Apunte y Boceto;
- System Diagram, refinamientos y validación tripartita;
- serialización OPL/OPD;
- bundle `deep-opm-pro.modelo.v0`;
- mesa `pull/push`, Testigo-Base, no-clobber y re-elicitación;
- render secundario con JointJS.

Luego cargar sólo la fibra operacional puntual:

| Operación | Fibra |
|---|---|
| bundle/import | `referencias/bundle-deep-opm-pro.md` |
| validación completa | `referencias/checklist-validacion.md` |
| anti-patrones opforja | `referencias/anti-patrones-opforja.md` |
| OPL estricto | `referencias/plantillas-opl-es.md` |

No ejecutar `mesa push`, escribir bundles ni mutar un runtime si el usuario no
autorizó ese efecto. Un `pull`, bundle emitido, render o paridad material no
demuestra aceptación semántica ni conducta del modelador.

Resolver repositorios, comandos, credenciales y capacidades desde la sesión y
el entorno efectivos. No asumir rutas bajo un home personal. Si la herramienta
no está disponible, conservar el modelo o bundle preparado y declarar qué
comprobación operacional quedó sin ejecutar.

## Reglas duras

1. Sólo objetos y procesos son entidades OPM fundamentales.
2. Todo proceso central transforma al menos un objeto.
3. No inventar conocimiento de dominio.
4. No confundir propuesta, decisión y hecho observado.
5. No declarar OPL parseable sin consultar el contrato OPL vigente.
6. No declarar equivalencia OPD↔OPL sin roundtrip cuando ese gate aplica.
7. No cargar operación Forja para una respuesta conceptual mínima.
8. No crear bundle, render ni mutación de mesa por defecto.
9. La SSOT OPM/Forja prevalece ante memoria, ejemplos y tooling.
10. La verificación del artefacto no sustituye validación humana del significado.

## Cierre

Entregar primero el modelo o dictamen solicitado. Añadir sólo:

- decisiones y supuestos que cambian su interpretación;
- evidencia de validación realmente ejecutada;
- límites (`conceptual`, `OPL estricto`, `bundle`, `runtime`) que evitan una
  falsa afirmación;
- una decisión mínima del operador si sigue bloqueando el resultado.
