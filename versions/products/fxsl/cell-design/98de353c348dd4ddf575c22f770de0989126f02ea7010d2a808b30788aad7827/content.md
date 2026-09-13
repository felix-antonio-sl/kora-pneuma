# cell-design

## Proposito

Disenar, evaluar o recalibrar una celula humano-agente a partir de su proposito,
trabajo y autoridad. Produce responsabilidades, interfaces, contratos y evidencia
que permitan sostener un resultado. Una celula es una unidad de responsabilidad;
no exige crear un equipo permanente, un organigrama ni infraestructura nueva.

## Cuando usar

- se incorpora agencia a un flujo compartido por humanos y herramientas;
- una delegacion carece de limite, criterio de aceptacion o responsable;
- aparecen solapamientos, esperas o revisiones manuales sin funcion clara;
- una senal sugiere deuda de evaluacion, contexto, autonomia u observabilidad;
- cambia el riesgo, la autoridad o la capacidad y el diseno debe recalibrarse.

No usar para una tarea simple ya asignada ni para imponer una ceremonia completa.
Seleccionar solo los estados y artefactos que cambian el resultado.

## Entradas

- resultado y beneficiario;
- trabajo y decisiones relevantes;
- participantes o capacidades disponibles;
- autoridad concedida y efectos que requieren otra autoridad;
- evidencia, restricciones, incertidumbre y consecuencias.

Resolver vacios menores con supuestos declarados. Preguntar solo si la respuesta
cambia materialmente el diseno; la bateria diagnostica es un repertorio, no una
nueva ronda obligatoria.

## Recorrido

### `diagnosticar`

Elegir las preguntas pertinentes:

- Que cambia, para quien y como se reconoceria?
- Donde esta la espera o decision que domina el flujo?
- Que juicio, fuente o autoridad no puede sustituirse?
- Que puede delegarse con la capacidad realmente disponible?
- Que evidencia distinguiria resultado de actividad?
- Que contexto, interfaz o responsabilidad falta?
- Que consecuencia exige contencion, aprobacion o recuperacion?

No exigir las siete si el encargo ya las responde.

### `posicionar-valor`

Describir outcome, beneficiario y filtro de valor. Usar lead time, throughput u
otra metrica solo cuando representa el resultado pertinente. Que suba el output
sin cambiar una metrica de outcome abre una investigacion; no demuestra por si
solo desperdicio, deuda o culpabilidad.

### `disenar-celula`

Definir la unidad minima capaz de sostener el trabajo:

- proposito y horizonte;
- funciones necesarias y portadores disponibles;
- responsabilidad y autoridad de cada decision;
- interfaces, entradas, salidas y traspasos;
- evidencia y condiciones de cierre;
- riesgos, contencion, recuperacion y revision.

Las funciones de arquitecto de intencion, curador de autonomia, ingeniero de
evaluacion y stakeholder experto son configurables. Una persona o agente puede
portar varias; una funcion puede omitirse o combinarse si se conservan sus
decisiones relevantes. Ver `referencias/roles-canonicos.md`.

### `disenar-contrato`

Usar un contrato de intencion cuando evita ambiguedad:

```
## Intent Contract: {titulo}
- Beneficiario y cambio: {quien / que cambia}
- Resultado suficiente: {criterios verificables}
- Puede decidir: {acciones autorizadas}
- Requiere otra autoridad: {efectos o decisiones}
- Fuera de alcance: {limites}
- Evidencia: {comprobacion pertinente}
- Riesgo y recuperacion: {prevencion, contencion, reversion si existe}
```

Usar una envolvente de autonomia cuando hay acciones delegadas:

```
## Autonomy Envelope: {funcion}
- Puede hacer: {frontera autorizada}
- Debe escalar: {condiciones}
- No puede hacer: {prohibiciones}
- Evidencia y visibilidad: {lo necesario para juzgar}
- Falla: {contencion, recuperacion o rollback posible}
- Revision: {evento o cadencia justificada}
```

No volver a pedir autoridad ya otorgada por el encargo.

### `disenar-evidencia`

Vincular cada afirmacion decisiva a una comprobacion. Elegir entre tests, evals,
revision humana o independiente, caso sintetico, observacion de uso o datos reales
autorizados. Separar autor, evaluador y corpus cuando aporta independencia real;
si comparten contexto, declararlo. Un experto aporta contexto, pero puede errar y
necesita fuentes para afirmaciones materiales.

No exigir datos reales cuando un caso sintetico o una fuente basta. Proteger
privacidad y minimizar datos, especialmente en dominios personales o clinicos.

### `auditar-deuda`

Examinar cuatro lentes sin presuponer que todos aplican:

| Deuda | Pregunta |
|---|---|
| evaluacion | Podemos distinguir cumplimiento de una salida convincente? |
| contexto | Las fuentes son suficientes, vigentes y no contradictorias? |
| autonomia | La accion excede capacidad o autoridad, o carece de respuesta a falla? |
| observabilidad | Falta evidencia necesaria para gobernar el efecto? |

Registrar senal, evidencia, consecuencia, confianza y accion. Los sintomas y
mitigaciones completos viven en `referencias/cuatro-deudas.md`.

### `recalibrar`

Revisar cuando cambien proposito, participantes, capacidad, autoridad, riesgo o
resultados, o cuando una senal material lo justifique. Agregar una cadencia solo
si existe operacion continua y explicar por que. Memoria, logs, tablero o control
plane son medios opcionales: especificarlos cuando la continuidad o gobernanza
los necesita y existe un lugar autorizado.

### `entregar`

Entregar los artefactos seleccionados, decisiones y responsables, evidencia,
deudas comprobadas, incertidumbres y siguiente paso. Marcar `no aplica` solo
cuando ayuda a evitar una interpretacion peligrosa; no rellenar plantillas por rito.

## Invariantes

1. El proposito decide que trabajo merece sostenerse.
2. Responsabilidad, autoridad y capacidad se distinguen.
3. Roles son funciones configurables, no cargos obligatorios.
4. La autonomia se acota por efecto y autoridad; la evidencia escala con riesgo.
5. Se prefiere reversibilidad cuando es viable. Para efectos irreversibles se usa
   prevencion, limite y decision autorizada, sin prometer rollback ficticio.
6. El disenso competente se registra; no se fuerza acuerdo para cerrar una tabla.
7. Una senal no basta para asignar deuda, causa o culpa.
8. El diseno puede concluir que no hace falta una celula o agente nuevo.

## Composicion y fuentes

El perfil legado `urn:fxsl:kb:allan-kelly-gemelo-digital-intelectual` es una
relacion de procedencia y se consulta solo ante una peticion explicita sobre esa
inspiracion. `mente-omega`, `cat-thinking` y `dov-dori` pueden aportar lentes a
problemas que lo requieran; ninguno reemplaza este metodo de organizacion.

## Recursos

- `referencias/formatos-allan-kelly.md`: formatos adaptables y reglas de uso.
- `referencias/roles-canonicos.md`: funciones configurables y autoridad.
- `referencias/cuatro-deudas.md`: senales, contrastes y mitigaciones.

## Salida esperada

Un diseno proporcional que permita saber quien sostiene cada resultado, con que
autoridad, mediante que interfaces, que evidencia lo cierra y como se responde a
fallas o cambios relevantes.
