# Diseño de producto integrado

## Propósito

Convertir una necesidad UI/UX en una decisión de producto opinada, accesible y
verificable. Esta skill dirige el bucle; no sustituye los oficios que ya existen:

- `urn:dev:artefacto:design` materializa sistema visual, tokens, componentes y
  bundle continuable.
- `urn:kora:artefacto:ux-design` audita tareas, heurísticas, arquitectura de
  información y WCAG 2.2 AA.
- `urn:dev:kb:canon-diseno-producto-integrado` aporta criterios, tensiones,
  contrapruebas y preguntas de decisión.

El resultado buscado no es más output. Es más **fit**: una forma que resuelve el
contexto, contiene un punto de vista, completa el bucle real y deja evidencia
para continuar.

## Cuándo usar

- Diseñar o rediseñar un flujo, pantalla, aplicación o feature con impacto
  conjunto en producto, UI y UX.
- Explorar una interacción nueva, incluida IA, voz, gesto, wearable o interfaz
  sin pantalla.
- Resolver una tensión entre simplicidad y poder, marca y familiaridad,
  velocidad y comprensión, o novedad y fiabilidad.
- Convertir un brief ambiguo en alternativas comparables y una dirección
  materializable.
- Revisar una solución visualmente competente que todavía no demuestra ajuste
  al usuario, al workflow o al sistema.

## Cuándo no usar

- Audit UX acotado sin decisión de producto: usar `ux-design`.
- Materialización visual ya decidida: usar `design`.
- Crítica de sustracción pura: usar el agente `steve-jobs`.
- Implementación de backend, despliegue o lógica de negocio.
- Investigación generativa con usuarios que todavía no se ha realizado: esta
  skill puede diseñar el protocolo, pero no inventa hallazgos.

## Contrato observable

`I_self` es:

```text
{
  necesidad: texto obligatorio,
  usuario_y_tarea: evidencia o supuesto explícito,
  contexto: producto, entorno, dominio y workflow,
  restricciones: tecnología, marca, tiempo, riesgo y accesibilidad,
  insumos?: código, capturas, métricas, entrevistas, design system
}
```

`O_self` es exactamente una de dos variantes:

- `DESIGN_PACKET`: encuadre, mapa de fuerzas, tres direcciones, decisión y
  rechazos, bucle completo, sistema, prototipo o especificación, evidencia de
  pruebas, riesgos, deuda y siguiente paso.
- `DESIGN_ERROR`: código estable, evidencia del bloqueo, supuestos no
  autorizables y acción mínima para destrabar.

Códigos de error:

- `insufficient-context`: no puede nombrarse usuario, tarea o contexto sin
  fabricar evidencia;
- `unresolved-reference`: el canon o una skill requerida no resuelve;
- `no-viable-direction`: ninguna alternativa supera los gates mínimos;
- `reality-check-failed`: la propuesta falla uso real y no converge después de
  tres ciclos;
- `handoff-incomplete`: faltan artefacto, sistema, evidencia o continuidad.

Invariantes:

- output no equivale a diseño;
- novedad no equivale a mejora;
- accesibilidad no se pospone;
- una demo no prueba un producto durable;
- la decisión cita evidencia y marca cada supuesto;
- ningún handoff descarga la responsabilidad sobre el receptor.

## Adaptadores de las skills candidatas

Las URN de `componible` son **candidatos declarados**. La arista por sí sola
**no prueba composicion** semántica, invocación efectiva ni preservación de
conducta. Esta skill las usa proceduralmente mediante los siguientes
adaptadores.

### Adaptador visual `design`

`I_design` contiene `brief_decidido`, `direccion`, `design_system_origen`,
`restricciones`, `contenido_real`, `estados_requeridos` y `destino_handoff`.

`O_design` contiene `artefacto`, `tokens`, `componentes`, `trazabilidad`,
`verificacion_estatica`, `deuda` y `handoff`.

Precondición: la dirección ya fue elegida en `decidir`; no se delega a
`design` la decisión de producto. Postcondición: cada decisión visual crítica
mapea a sistema o queda declarada como excepción.

### Adaptador de experiencia `ux-design`

`I_ux` contiene `usuario_y_tarea`, `flujo`, `prototipo`, `contexto_de_uso`,
`estados`, `riesgos` y `criterios_wcag`.

`O_ux` contiene `hallazgos`, `evidencia`, `severidad`, `correcciones`,
`criterios_wcag` y `veredicto`.

Precondición: existe un flujo o prototipo observable. Postcondición: cada
hallazgo traza a heurística, tarea o criterio WCAG; una preferencia estética no
se disfraza de usabilidad.

Si una URN no resuelve, se devuelve `unresolved-reference`; no se copia ni se
inventa su procedimiento.

## Workflow

### 1. `encuadrar`

Nombrar en una página como máximo:

- una persona o rol primario;
- una tarea primaria y el resultado humano esperado;
- contexto físico, social, técnico y temporal;
- fuerzas: necesidades, hábitos, restricciones, riesgos y edge cases;
- evidencia disponible y supuestos;
- qué no se diseñará en este ciclo.

Salida: `FRAME`. Si usuario o tarea no pueden distinguirse, no generar UI:
devolver `insufficient-context`.

### 2. `resolver-tensiones`

Construir `TENSION_MAP` con pares concretos, no eslóganes:

| Tensión | Pregunta de arbitraje |
|---|---|
| coherencia ↔ expresión | ¿qué rasgo propio puede vivir sin romper sistema ni legibilidad? |
| simplicidad ↔ maestría | ¿qué complejidad habilita poder y cuál solo externaliza confusión? |
| familiaridad ↔ paradigma | ¿qué convención ayuda y cuál impide una interacción mejor? |
| velocidad ↔ comprensión | ¿qué se puede acelerar sin confundir output con fit? |
| automatización ↔ agencia | ¿qué hace la IA y cómo ve, corrige o revierte la persona? |
| alcance ↔ completitud | ¿qué corte permite terminar el bucle sin omitir estados reales? |

Cada tensión termina con una regla de decisión y una condición que podría
refutarla.

### 3. `divergir`

Generar exactamente tres direcciones suficientemente distintas:

1. **Sistémica:** maximiza familiaridad, continuidad y eficiencia.
2. **Con carácter:** añade punto de vista de marca y fricción intencional.
3. **Cambio de paradigma:** cuestiona medio o modelo de interacción.

Para cada dirección: tesis de una frase, bucle primario, sistema visual,
fricción conservada, riesgo principal, hipótesis y qué evidencia la mataría.
No producir tres skins de la misma estructura.

### 4. `decidir`

Comparar las direcciones con la matriz:

| Criterio | Gate |
|---|---|
| éxito de tarea | completa el resultado humano con menos error o carga |
| fit contextual | resuelve las fuerzas y desajustes identificados |
| comprensión | jerarquía, affordances y feedback son legibles |
| eficiencia y maestría | novato entra; experto gana velocidad sin ruta paralela incoherente |
| accesibilidad | no hay bloqueo conocido para WCAG 2.2 AA |
| coherencia sistémica | integra producto, marca, componentes y plataforma |
| carácter | contiene una decisión propia defendible |
| factibilidad | cabe en el alcance y declara dependencias |
| confianza | privacidad, reversibilidad y degradación están diseñadas |

Elegir una sola dirección. Registrar por qué gana y por qué se rechazan las
otras. No promediar las tres.

### 5. `prototipar`

Materializar el **menor bucle completo**, con contenido realista:

```text
entrada -> orientación -> acción -> feedback -> resultado -> recuperación
```

Debe incluir como mínimo estados inicial, carga, vacío, éxito, error y
recuperación. Si hay IA o servicio remoto, incluir latencia, timeout,
incertidumbre, permiso, privacidad, reversibilidad y degradación. Si hay voz,
gesto o proyección, probar además descubribilidad, legibilidad ambiental y
alternativa accesible.

Usar el adaptador `I_design -> O_design` cuando se requiera materialización
visual. La primera versión es instrumento de aprendizaje, no entrega.

### 6. `probar`

Ejecutar una prueba de realidad proporcional al riesgo:

1. recorrido de tarea de punta a punta;
2. auditoría mediante `I_ux -> O_ux`;
3. WCAG 2.2 AA;
4. viewport, teclado, lector y reducción de movimiento cuando aplique;
5. latencia, error, estados vacios, offline o pérdida de servicio;
6. legibilidad en el entorno real;
7. control, privacidad, reversibilidad y salida;
8. comparación contra la alternativa actual.

Separar siempre:

- **verificado:** declarado literalmente en los insumos o observado en una
  fuente leída o ejecución de esta invocación, citando insumo, ruta o comando;
- **inferido:** conclusión razonada desde evidencia;
- **pendiente:** requiere humano, dispositivo, usuario o runtime no disponible.

Aplicar un gate de **evidencia cerrada** antes de entregar:

1. Construir primero un `EVIDENCE_LEDGER` numerado `[E1]`, `[E2]`, etc. Solo
   admite entradas literales, artefactos preexistentes leídos y resultados de
   pruebas realmente ejecutadas sobre esos artefactos.
2. Cada afirmación `verificado` debe citar un `[E#]` y su insumo, ruta o comando
   con resultado; ese registro es su fuente observable de esta ejecución.
3. Una especificación, código, token o componente generado en la propia
   respuesta no puede verificarse a sí mismo.
4. No inventar métricas, tests, versiones, participantes, investigación,
   telemetría, capacidades del producto, tokens, decisiones legales, owners ni
   fechas.
5. Patrones conocidos, documentación de librerías no observadas en el producto
   o productos de referencia son `inferido` o `referencia`,
   no pruebas del producto actual.
6. Sin artefacto ejecutable, tratar el resultado como especificación: WCAG,
   teclado, lector de pantalla, contraste, latencia y recuperación permanecen
   `pendiente`.
7. Si la entrada no aporta stack, design system, endpoint o política de datos,
   usar nombres genéricos o placeholders; no completarlos por plausibilidad.
8. Si una afirmación no puede citar una fuente válida independiente de la
   propia salida, degradarla a `inferido` o `pendiente`.

Si no hay `insumos`, artefacto, prototipo o ejecución observable, activar
`SPEC_ONLY`:

- `verificado` se limita a la entrada literal y a referencias resueltas;
- canon y guías se rotulan `normativo`, no cumplimiento del producto;
- la solución diseñada se rotula `propuesto` y sus pruebas `pendiente`;
- no se añaden números, duraciones, conteos, stack, componentes, tokens,
  endpoints, políticas, capacidades, owners ni fechas ausentes de la entrada;
- no se afirma que la propia especificación cumple, funciona o está probada.

Si un fallo crítico persiste tras tres ciclos
`prototipar -> probar -> integrar`, devolver `reality-check-failed`.

### 7. `integrar`

Corregir desde la causa:

- fallo sistémico → token, componente o patrón, no parche local;
- fallo de tarea → flujo o jerarquía, no cosmética;
- fallo de confianza → feedback, control, reversibilidad o arquitectura;
- fallo de alcance → cortar capacidad, no omitir estados;
- falta de carácter → revisar la tesis, no añadir ornamento.

Repetir `prototipar -> probar -> integrar` hasta verde o hasta el techo de tres
ciclos.

### 8. `entregar`

Emitir `DESIGN_PACKET` bien formado:

```text
01_frame.md
02_tension-map.md
03_directions.md
04_decision.md
prototype_or_spec/
design-system/
05_evidence.md
06_handoff.md
```

Para una intervención pequeña, las secciones pueden vivir en un único Markdown;
la estructura semántica se conserva. `06_handoff.md` declara punto de entrada,
qué fue verificado, qué queda pendiente, deuda, riesgos y siguiente decisión.

## Reglas duras

1. Investigar el contexto antes de generar forma.
2. Conservar las tensiones; no fusionar por promedio.
3. Divergir en estructura y modelo de interacción, no solo en estética.
4. Elegir una dirección; el diseño no se entrega como menú sin criterio.
5. El prototipo representa un bucle completo y sus fallos.
6. Toda fricción conservada nombra el poder, seguridad o aprendizaje que habilita.
7. Toda interacción nueva demuestra ventaja sobre una alternativa más simple.
8. IA, nube o hardware singular declaran dependencia, degradación y salida.
9. WCAG 2.2 AA es gate mínimo, no deuda aceptable por novedad.
10. Usar evidencia para corregir juicio; no diseñar por votación.
11. Las herramientas del frontmatter son capacidades declaradas. Su autoridad
    efectiva depende del target y del runtime.
12. Esta skill dirige el proceso; no suplanta la identidad de ningún diseñador.
13. No fabricar evidencia para completar el paquete; lo no observado se declara
    como inferencia, hipótesis o trabajo pendiente.
14. Ninguna salida autogenerada puede servir como evidencia de su propia
    corrección o de capacidades existentes en el producto.
15. En `SPEC_ONLY`, separar siempre `propuesto` de `verificado`; una norma no
    prueba cumplimiento y una especificación no prueba conducta.
