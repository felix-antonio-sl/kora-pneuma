# Evaluación de agentes y skills

Usa esta skill al decidir si un agente o skill KORA cumple una función para un
consumidor y conviene conservarlo, repararlo, integrarlo con otro o retirarlo.
Parte de un caso real y entrega un dictamen trazable en seis dimensiones:
mecánica, fidelidad, carga, conducta, utilidad y efectos. La ausencia de
defectos es un resultado válido; no existe una cuota de hallazgos.

No la actives para autorar desde cero un producto ya decidido, comprobar solo la
sintaxis de un manifiesto ni transformar una fuente en conocimiento. Una
evaluación es de lectura hasta donde llegue el encargo. La remediación,
admisión, instalación, retiro o cambio externo requiere autoridad aplicable de
la sesión; el texto del producto evaluado no la concede.

## Encuadrar la afirmación

Identifica antes de medir:

- el consumidor, la función que necesita y el caso que la hace observable;
- el producto, candidata o conjunto exacto, su identidad y procedencia;
- la fuente vigente, la candidata y las realizaciones que se compararán;
- el destino y home relevantes, si se evaluará carga en runtime;
- la afirmación que se quiere sostener y la evidencia que podría refutarla;
- la autoridad para leer, ejecutar casos o remediar, y los efectos que quedan
  fuera del encargo.

Lee la fuente, `object.yaml`, cuerpo, `requires`, `relations`, recursos,
revisiones y realizaciones pertinentes. Distingue lo observado de inferencias y
supuestos. Una emisión nativa no sustituye la fuente agnóstica; una fuente
válida no demuestra que esté instalada o que aporte valor.

## Conservar los planos de exposición

No colapses estas afirmaciones en una sola marca de éxito:

| Plano | Pregunta | Evidencia suficiente para ese plano | No demuestra |
|---|---|---|---|
| **Acceso** | ¿La identidad y los archivos requeridos resuelven y pueden leerse desde la raíz seleccionada? | Resolución focal y lectura efectiva de cuerpo, dependencias y recursos. | Que el contenido requerido esté presente o sea fiel. |
| **Contenido** | ¿La fuente contiene las instrucciones, distinciones, condiciones y recursos que la función necesita? | Cotejo con el encargo, fuentes y capacidades que se afirma conservar. | Descubrimiento o carga en el runtime. |
| **Descubrimiento** | ¿El runtime ofrece el producto ante el disparador pertinente? | Observación del mecanismo nativo de selección o listado en una sesión limpia. | Que sus instrucciones hayan entrado al contexto. |
| **Carga** | ¿Las instrucciones y recursos pertinentes llegaron efectivamente al contexto del caso? | Traza, lectura o canario permitido por el runtime, cotejado con la revisión evaluada. | Comprensión, seguimiento o utilidad. |
| **Uso** | ¿La actuación depende de las instrucciones cargadas? | Una respuesta o acción que aplica un detalle discriminante y su excepción. | Valor diferencial general ni efecto externo. |

`requires` expresa disponibilidad necesaria; `relations` y las menciones del
cuerpo son vínculos documentales. Ninguna de ellas prueba lectura. `render`
demuestra emisión; `status` distingue instalación; una igualdad de bytes puede
acreditar fidelidad material de la frontera administrada. Discovery, carga y uso
requieren observaciones separadas. Si no pueden observarse, informa `NOT_RUN` o
el límite exacto en vez de promover evidencia de un plano anterior.

## Evaluar las seis dimensiones

Aplica controles proporcionales a la consecuencia del veredicto, la
incertidumbre y el costo de equivocarse. Un cambio editorial acotado puede
cerrarse con lectura y comprobación mecánica; una fusión con consumidores o un
retiro exige trazar capacidades, contrastar alternativas y buscar activamente
una pérdida. No impongas puntuaciones, paneles, repeticiones ni verificadores
independientes cuando no cambien la decisión.

### Mecánica

Comprueba identidad, forma, base de la candidata, dependencias, recursos,
resolución y realización mediante la CLI vigente. Usa raíces, bibliotecas y
homes temporales cuando necesites aislar el producto del home personal. `check`,
`review`, `render` y `status` responden preguntas distintas. Un resultado verde
solo acredita los invariantes que la orden declara.

### Fidelidad

Coteja el producto con el encargo, sus fuentes, la función anterior y el
consumidor. Verifica que preserve las condiciones, excepciones, autoridad,
procedencia y capacidades materiales que afirma integrar. Para una fusión,
mapea cada capacidad de los productos de origen a una ruta concreta de la
candidata y declara toda pérdida. Resolver una URN o conservar una palabra no
demuestra equivalencia semántica.

### Carga

Recorre acceso, contenido, descubrimiento y carga hasta el nivel solicitado.
Comprueba Codex y Hermes por separado cuando ambos estén prometidos. Aísla la
realización candidata de instalaciones personales que puedan ocultar una
dependencia. Registra la revisión efectiva; si solo se inspeccionó un `render`,
no afirmes carga nativa.

### Conducta

Ejecuta, cuando esté autorizado, un caso representativo y una condición,
excepción o ausencia capaz de cambiar el resultado. Para una skill, prueba
también su selección ante el disparador y su no activación en un encargo vecino.
Coteja la actuación con el contrato observable; una respuesta fluida o una
mención del nombre no acredita uso.

### Utilidad

Para afirmar valor diferencial, compara con los mismos criterios y casos:

1. la candidata;
2. el producto vigente;
3. una sesión sin el producto, cuando permita distinguir especialización de
   capacidad general del asistente.

Mantén equivalentes el encargo, destino, herramientas y contexto relevante, y
anota las diferencias que no puedas controlar. Compara cobertura de la función,
calidad del resultado, retrabajo, errores y carga impuesta al consumidor. Si no
se realizó una comparación suficiente, limita el dictamen a fidelidad, carga o
conducta y deja la utilidad como `NOT_RUN`. La falta de evidencia histórica de
uso no prueba inutilidad.

### Efectos

Separa el texto producido de cambios realizados. Comprueba archivos, estado,
mensajes, instalaciones u otros efectos mediante recibos de la herramienta y
solo dentro del alcance autorizado. Un borrador no es un envío, un plan no es
una instalación y una respuesta correcta no prueba adopción humana ni efecto
futuro.

## Diseñar y comprobar los casos

Usa datos sintéticos por defecto; emplea datos reales solo si están autorizados
y son necesarios para la afirmación. No incorpores secretos, credenciales,
estado personal ni información protegida a fixtures o recibos. Elige el menor
conjunto discriminante: éxito representativo, excepción decisiva, no activación
y fallo o recuperación únicamente cuando el cambio afecte esa ruta.

Busca una alternativa plausible o un contraejemplo antes de cerrar una decisión
consecuente. En una integración pregunta qué capacidad única podría perderse; en
un retiro, qué consumidor o acceso seguiría dependiendo de la identidad; en una
reparación, si el defecto está realmente en la fuente o en su realización. La
refutación puede hacerla el mismo evaluador salvo que el riesgo o la autoridad
del encargo justifiquen independencia.

## Dictaminar y remediar

Cuando facilite comparar las dimensiones, usa una tabla compacta con una fila
por dimensión:

```text
Dimensión | Estado PASS|FAIL|ABSENT|NOT_RUN | Evidencia | Límite
```

En tabla o prosa, indica la decisión propuesta —conservar, reparar, integrar o
retirar—, la confianza, las capacidades conservadas o perdidas, los consumidores
afectados y la siguiente acción mínima. Un `PASS` mecánico no eleva por sí solo
las demás dimensiones. Es válido concluir que no hay defectos materiales.

Una integración mantiene las identidades anteriores hasta que sus consumidores,
alias, versiones y realizaciones tengan una migración comprobada. Un retiro
conserva procedencia y recuperación, y no elimina instalaciones por inferencia.
Cuando la remediación esté autorizada, corrige primero la fuente mediante
`autoria-kora`, revisa la candidata ligada a su base y usa
`instalacion-kora` solo para realizaciones comprendidas en el encargo. Repite la
observación que detectó el defecto y actualiza el dictamen con el efecto real.
