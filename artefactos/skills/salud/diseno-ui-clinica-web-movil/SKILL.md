---
urn: urn:salud:artefacto:diseno-ui-clinica-web-movil
nombre: diseno-ui-clinica-web-movil
version: 1.0.0
estado: activo
descripcion: "Diseña, implementa y evalúa la gráfica y estética funcional de interfaces clínicas densas para web y smartphones mediante una lente sintética Karri/Linear y Vercel: fit antes que output, calma, jerarquía, detalle invisible, sistema visual trazable, diseño en código, responsive semántico, estados completos y evidencia runtime. Usar al encuadrar, rediseñar, materializar o auditar UI clínica; no atribuye participación ni aprobación a esas personas o equipos."
fuente: "Síntesis nueva creada el 2026-07-26 desde la especificación SYSTEM TLHD-HEALTH sha256:7b745468294a3a55bc5a20b8af7951cac67c481dd05f0e2c7ea842396bdd0b61, DESIGN PACKET v2 sha256:34a6f80ab006342532e59b391fd51b0a5405ab3e8284f219523baedff43a1103 y auditoría Linear-Vercel sha256:ee991086faa8655c9a6fda1587fd1fd0fcb136f759b1cdcc93d16e249ad50a5f; destila fuentes públicas citadas en referencias/marco-ui-clinica-web-movil.md. La síntesis es inferencia operativa, no opinión, participación ni aprobación de Karri Saarinen, Linear o Vercel. Reutiliza capacidades KORA mediante adaptadores explícitos; componible declara candidatos y no prueba wiring ni conducta."
autor: FS
creado: 2026-07-26
lang: es
tags: [diseno-ui, ui-clinica, diseno-grafico, web, smartphone, responsive, linear, vercel, design-system, accesibilidad, evaluacion-runtime]
vector: [2, 0, 2, 0, 1]
sigma: [3, 2, 3, 3, 2]
arnes: disciplina
forma: habilidad
herramientas: [Read, Write, Edit, Glob, Grep, Bash]
targets: [codex]
conocimiento: [urn:dev:kb:canon-diseno-producto-integrado]
componible: [urn:dev:artefacto:diseno-producto-integrado, urn:dev:artefacto:design, urn:kora:artefacto:ux-design, urn:fxsl:artefacto:ifml, urn:dev:artefacto:ship-discipline]
alcance: usuario
estados: [enrutar, reunir-evidencia, encuadrar, modelar, divergir, decidir, sistematizar, materializar, implementar, evaluar, integrar, entregar]
---
# Diseño UI clínica web y móvil

## Propósito

Convertir una necesidad de interfaz clínica en una forma visual calmada, densa,
propia y operable para web y smartphone; llevarla a componentes y código cuando
el repositorio está en alcance; y evaluarla con evidencia proporcional al
artefacto disponible.

Aplicar una síntesis explícita de criterios públicos:

- **Karri/Linear:** fit antes que output, calidad del bucle completo, calma
  estructural, densidad experta, dirección comparada y detalles invisibles.
- **Vercel Design:** diseño en código, primitives correctas, estados completos,
  responsive semántico, accesibilidad, rendimiento y preview reproducible.

No imitar su estética ni reclamar su autoridad. La skill no fue creada,
revisada ni aprobada por Karri Saarinen, Linear o Vercel.

## Resultado que gobierna

> Mantener visibles persona, tiempo, procedencia y consecuencia mientras una
> tarea clínica pasa de observación a acción.

La gráfica debe comprimir complejidad sin ocultar conflicto, obsolescencia,
incertidumbre, identidad ni consecuencias. Minimalismo significa menos
competencia visual y más relación visible; no menos información necesaria.

## Modo

Ejecutar exactamente uno:

| Modo | Usar cuando | Salida |
|---|---|---|
| `FRAME` | falta convertir problema y contexto en marco visual | `UI_FRAME_PACKET` |
| `MODEL` | deben precisarse objetos, vistas, eventos o navegación | `UI_MODEL_PACKET` |
| `DESIGN` | se requieren direcciones, sistema y especificación/prototipo | `UI_DESIGN_PACKET` |
| `BUILD` | existe dirección elegida y repo autorizado | `UI_IMPLEMENTATION_PACKET` |
| `EVALUATE` | existe spec, captura, prototipo o runtime que criticar | `UI_EVALUATION_PACKET` |
| `FULL` | debe recorrerse el bucle completo hasta el primer gate rojo | `UI_FULL_PACKET` |

Si el operador no declara modo, inferirlo cuando la acción pedida sea
inequívoca; en otro caso usar `FULL`. `FULL` se detiene en el primer gate rojo,
no completa vacíos con output.

## Input

```text
UI_INPUT = {
  modo: FRAME | MODEL | DESIGN | BUILD | EVALUATE | FULL,
  necesidad,
  contexto_clinico,
  rol_y_tarea,
  responsabilidad,
  objeto_primario_candidato?,
  plataforma: responsive-web | mobile-web | native-ios | native-android |
              react-native | flutter | otra,
  soportes: web | smartphone | ambos,
  domain_authority_packet?: {
    hechos_autorizados,
    decisiones_pendientes,
    politicas_aplicables,
    frontera_de_aprobacion
  },
  alternativa_actual?,
  contenido_sintetico_o_desidentificado?,
  estados_requeridos?,
  restricciones?,
  sistema_visual?,
  artefactos?,
  repo_o_url?,
  comandos_runtime?,
  evidencia?,
  supuestos?,
  fuera_de_alcance?
}
```

No leer ni retener PHI como insumo de diseño. Usar datos sintéticos o
desidentificados. Si el trabajo depende de contenido clínico identificable,
detenerse y pedir una vía autorizada.

## Errores observables

Devolver `UI_DESIGN_ERROR` con `codigo`, `evidencia`, `bloqueo` y
`accion_minima`:

- `insufficient-context` — no se distinguen contexto, rol o tarea;
- `domain-authority-required` — una decisión visual depende de política o
  significado clínico no autorizado;
- `unresolved-reference` — marco, canon o skill requerida no resuelve;
- `unsupported-platform` — “móvil” no distingue web responsive de stack nativo;
- `no-comparable-directions` — no existen tres formas materialmente comparables;
- `no-selected-direction` — se pide implementar sin decisión;
- `no-authorized-repository` — se pide mutar código sin repo en alcance;
- `missing-implementation-target` — falta stack, entrypoint o comando de build;
- `no-observable-artifact` — se pide evaluar conducta sin artefacto;
- `missing-runtime-runner` — se pide evidencia viva sin URL/comando ejecutable;
- `build-failed` — la implementación no cierra build;
- `evaluation-incomplete` — falta un gate exigido por el alcance;
- `safety-boundary` — la tarea pide inventar o aprobar semántica clínica.

## Carga progresiva del marco

Leer `referencias/marco-ui-clinica-web-movil.md` antes de producir una decisión
visual. Completar
`referencias/frame-guia-especificacion-grafica.md` en `FRAME` o `DESIGN` y
usarlo como índice de trazabilidad en los otros modos. No copiar las referencias
completas en la salida; usar sólo las secciones del modo:

| Modo | Secciones mínimas |
|---|---|
| `FRAME` | 0–4, 7, 15–18 |
| `MODEL` | 0–4, 8–10, 13–16 |
| `DESIGN` | 0–11, 13–18 |
| `BUILD` | 0–5, 8–13, 15–18 |
| `EVALUATE` | 0–4, 8–18 |
| `FULL` | marco completo |

Para una microedición local, leer además el contrato del componente afectado.
Para un cambio transversal, leer el marco completo.

## Evidencia

Crear primero un `EVIDENCE_LEDGER`:

```text
[E1] tipo=input|archivo|comando|runtime|humano
     fuente=<ruta, URL, comando o identidad de la sesión>
     observacion=<hecho literal>
     alcance=<qué demuestra y qué no>
```

Clasificar toda conclusión:

- `verificado` — traza a `[E#]` independiente de la propia salida;
- `propuesto` — decisión producida en esta invocación;
- `inferido` — conclusión razonada desde evidencia o fuente normativa;
- `pendiente` — requiere artefacto, runtime, persona o autoridad ausente.

Reglas:

1. Una salida, token, componente o spec no se verifica a sí misma.
2. Una fuente pública es referencia normativa; no prueba el producto.
3. Una captura prueba una apariencia puntual; no prueba interacción.
4. Código leído prueba estructura; no prueba render.
5. Build verde prueba build; no prueba experiencia.
6. Tests automáticos no sustituyen teclado, tacto, lector ni juicio humano.
7. Validación clínica sólo proviene de autoridad competente identificada.
8. No inventar métricas, tests, usuarios, políticas, stack, owners ni plazos.

Sin artefacto ejecutable, activar `SPEC_ONLY`: no declarar cumplimiento,
funcionamiento, accesibilidad ni rendimiento.

## Composición

Las URN de `componible` son candidatos. Resolver la fuente y leer su
`SKILL.md` completa antes de usarla. La arista no prueba invocación, wiring,
preservación de conducta ni autoridad runtime.

### Dirección de producto

Usar `urn:dev:artefacto:diseno-producto-integrado` en `FRAME`, `DESIGN` y
`FULL` cuando exista una tensión de producto o varias direcciones plausibles.

```text
I_product = {
  necesidad, usuario_y_tarea, contexto, restricciones, insumos
}
O_product = DESIGN_PACKET | DESIGN_ERROR
```

Esta skill estrecha su salida: las tres direcciones deben materializarse con
el mismo fixture, estados y soportes antes de elegir.

### Forma visual

Usar `urn:dev:artefacto:design` en `DESIGN`, `BUILD` o `FULL`.

```text
I_design = {
  direccion_elegida, marco, fixture_comun, estados, soportes,
  sistema_origen, restricciones, destino_handoff
}
O_design = {
  artefacto, tokens, primitives, componentes, trazabilidad,
  verificacion_estatica, deuda, handoff
}
```

`design` produce forma y bundle continuable. No usar su salida como prueba de
build o runtime.

### Interacción formal

Usar `urn:fxsl:artefacto:ifml` en `MODEL` o `FULL` sólo si el problema exige
modelar navegación multivista, eventos, bindings o adaptación multiscreen. No
cargar IFML para ajustes puramente visuales.

```text
I_ifml = {
  plataforma, roles, modelo_dominio_autorizado, vistas, eventos, acciones
}
O_ifml = {
  modelo_tipado, patrones, validacion, supuestos, preguntas_abiertas
}
```

Si falta semántica de negocio, conservar el gate de elicitación de IFML; no
fabricar acciones ni transiciones.

### Implementación

Usar `urn:dev:artefacto:ship-discipline` sólo en `BUILD` o en la fase de
implementación de `FULL`.

```text
I_ship = {
  repo, direccion, build_contract, alcance, restricciones
}
O_ship = {
  patch, build, tests, lint, integracion, deuda, cierre
}
```

La implementación realiza la dirección ya elegida. No reabre gusto o modelo de
producto de forma silenciosa. Si descubre una contradicción, vuelve a
`decidir`.

### Evaluación UX

Usar `urn:kora:artefacto:ux-design` en `EVALUATE` o `FULL` cuando exista flujo,
prototipo o UI.

```text
I_ux = {
  artefacto, tarea, flujo, contexto, estados, riesgos, criterios_wcag
}
O_ux = {
  hallazgos, evidencia, severidad, correcciones, veredicto
}
```

Rotular el nivel de evidencia: `documental`, `estático`, `automatizado`,
`runtime-manual`, `humano` o `dominio`.

## Workflow común

### `enrutar`

1. Fijar un modo.
2. Identificar soporte y tipo de implementación.
3. Distinguir web responsive de app nativa; “móvil” no las vuelve equivalentes.
4. Resolver referencias requeridas.
5. Estimar qué acciones son read-only y cuáles mutan código.
6. Registrar los adaptadores activados; el operador invoca sólo esta skill.

### `reunir-evidencia`

1. Construir `EVIDENCE_LEDGER`.
2. Leer brief, spec, sistema visual, código y artefactos autorizados.
3. Separar decisiones existentes, hipótesis y gaps.
4. Identificar política clínica o institucional faltante.
5. Activar `SPEC_ONLY` si no hay runtime.

### `encuadrar`

Nombrar:

- un contexto clínico;
- un rol;
- una tarea;
- una responsabilidad;
- un resultado;
- una alternativa actual;
- un objeto primario candidato;
- fallos observables;
- fuera de alcance.

No comenzar por paneles. Si el objeto no puede explicarse sin nombrar la UI,
permanece hipótesis.

### `modelar`

Comparar objetos candidatos y describir identidad, ciclo, tiempo, procedencia,
evidencia, acción y relaciones. Si navegación, eventos o multiscreen son
materiales, usar el adaptador IFML. Sin `domain_authority_packet`, dejar como
preguntas las acciones, guards y políticas clínicas; no fabricarlas.

### `divergir`

Materializar exactamente tres direcciones con el mismo contenido y estados:

1. `Ledger clínico`;
2. `Hilo de evidencia`;
3. `Escena de decisión`.

Cada una incluye web y smartphone, normal, crítico, vacío, error y recepción
incierta. No producir tres skins de la misma estructura.

### `decidir`

Comparar función, jerarquía, densidad, coherencia, carácter, transformación
web/smartphone, estados, acceso, rendimiento y riesgo clínico. Elegir una o
rechazar las tres. Registrar ganancias, pérdidas y evidencia que podría
refutar la decisión.

### `sistematizar`

Definir:

- tesis visual;
- planos `Contexto`, `Trabajo`, `Foco`, `Consecuencia`;
- tokens primitivos, semánticos y de componente;
- tipografía y números;
- espacio y densidad;
- bordes, elevación, iconografía y movimiento;
- primitives;
- componentes y estados;
- contratos responsive;
- reglas de truncación;
- matriz de crash tests.

Color trabaja después de posición, agrupación, espacio, alineación, tamaño y
peso. Selección, foco, warning y critical deben ser distinguibles.

### `materializar`

Según modo:

- `FRAME`: marco y gates, sin fingir UI;
- `MODEL`: modelo de objetos e interacción, sin decidir estética;
- `DESIGN`: especificación o prototipo con sistema trazable;
- `BUILD`: patch sobre repo autorizado y loop técnico cerrado;
- `EVALUATE`: no mutar salvo que el operador pida también corregir;
- `FULL`: recorrer en orden y detenerse en el primer gate rojo.

El smartphone recibe una escena propia; nunca un escritorio reducido.

### `evaluar`

Aplicar:

1. matriz visual del marco;
2. crash tests;
3. coherencia token–primitive–componente;
4. web + smartphone;
5. estados y asincronía;
6. teclado, foco, tacto, zoom y reflow;
7. accesibilidad;
8. estabilidad y rendimiento;
9. validación de dominio cuando corresponda.

Si existe runtime, ejecutar comandos autorizados y conservar capturas/logs. Si
no existe, degradar hallazgos a documental o estático.

### `entregar`

Emitir un único paquete del modo con:

- binding del artefacto evaluado o modificado;
- decisión;
- evidencia;
- resultado;
- deuda;
- gates verdes/rojos;
- siguiente acción mínima.

## Salidas

### `UI_FRAME_PACKET`

```text
FRAME
FORCE_MAP
PRIMARY_OBJECT_HYPOTHESES
GRAPHIC_PRINCIPLES
PLATFORM_INVARIANTS
GATES
EVIDENCE_LEDGER
RISKS_AND_NEXT_GATE
```

### `UI_DESIGN_PACKET`

```text
FRAME
VISUAL_DIRECTIONS[3]
DECISION_RECORD
VISUAL_SYSTEM
COMPONENT_CONTRACTS
WEB_COMPOSITION
SMARTPHONE_COMPOSITION
STATE_MATRIX
PROTOTYPE_OR_SPEC
EVALUATION_CONTRACT
EVIDENCE_LEDGER
HANDOFF
```

### `UI_MODEL_PACKET`

```text
INPUT_BINDING
OBJECT_MODEL_CANDIDATES
SELECTED_OBJECT_OR_OPEN_DECISION
INTERACTION_CONTRACT
IFML_MODEL?
DOMAIN_QUESTIONS
EVIDENCE_LEDGER
NEXT_GATE
```

### `UI_IMPLEMENTATION_PACKET`

```text
ARTIFACT_BINDING
PATCH
DESIGN_SYSTEM_TRACE
BUILD_RECEIPT
TEST_RECEIPT
LINT_RECEIPT
RUNTIME_EVIDENCE
DEBT
HANDOFF
```

### `UI_EVALUATION_PACKET`

```text
ARTIFACT_BINDING
EVIDENCE_LEVEL
FINDINGS
VISUAL_MATRIX
CRASH_MATRIX
WCAG_EVIDENCE
PERFORMANCE_EVIDENCE
DOMAIN_PENDING
VERDICT
CORRECTIONS
```

### `UI_FULL_PACKET`

Contiene los paquetes anteriores realmente producidos, los adaptadores
activados, el primer gate rojo si existe y `RISKS_AND_NEXT_GATE`. No crea
secciones vacías para aparentar completitud.

## Gates

Orden obligatorio:

1. problema;
2. objeto;
3. conceptos comparables;
4. sistema visual;
5. estados;
6. responsive;
7. implementación;
8. accesibilidad y rendimiento;
9. dominio;
10. evidencia.

No promover por promedio. Un gate rojo mantiene la salida como propuesta o
prototipo.

## Reglas duras

1. No diseñar desde “dashboard”; diseñar desde contexto, objeto y tarea.
2. No imitar Linear o Vercel ni reclamar su aprobación.
3. No crear un agente-persona Karri/Linear/Vercel.
4. No convertir una referencia pública en evidencia del producto.
5. No convertir preferencia visual en regla clínica.
6. No usar PHI para fixtures de diseño.
7. No elegir una dirección antes de materializar comparables.
8. No tratar paleta como sistema visual.
9. No usar color como único canal.
10. No confundir selección, foco, warning y critical.
11. No esconder procedencia, vigencia, conflicto o incertidumbre por limpieza.
12. No usar un inspector para detalle, workflow, alerta y confirmación.
13. No usar command palette como arquitectura primaria.
14. No reducir escritorio para producir smartphone.
15. No declarar verificado lo que sólo está escrito o generado.
16. No implementar sin dirección, repo y alcance autorizados.
17. No declarar experiencia verde por build o tests automáticos.
18. No cerrar sin deuda, evidencia y siguiente gate.
19. Sin `domain_authority_packet`, permitir framing y prototipo sintético, pero
    no promover identidad, alertas, órdenes, override, privacidad o corrección.
20. No importar `steve-jobs-principios-salud` por defecto.
