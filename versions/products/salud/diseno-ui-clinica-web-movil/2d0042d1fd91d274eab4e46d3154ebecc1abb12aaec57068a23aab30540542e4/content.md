# Diseño UI clínica web y mobile web

## Propósito

Convertir una necesidad de TLHD-HEALTH —o de una interfaz clínica comparable
centrada en persona o episodio— en una forma visual calmada, densa y operable
para web responsive y mobile web; llevarla a código sólo con autorización; y
evaluarla con evidencia proporcional al artefacto disponible. Para UI no
clínica usar `diseno-producto-integrado` o `design`. Para apps nativas usar una
capacidad con canon y runners específicos: este contrato devuelve
`unsupported-platform`.

Aplicar una síntesis explícita de criterios públicos:

- **Karri/Linear:** fit antes que output, calidad del bucle completo, calma
  estructural, densidad experta, dirección comparada y detalles invisibles.
- **Vercel Design:** diseño en código, primitives correctas, estados completos,
  responsive semántico, accesibilidad, rendimiento y preview reproducible.

No imitar su estética ni reclamar su autoridad. La skill no fue creada,
revisada ni aprobada por Karri Saarinen, Linear o Vercel.

## Alcance y resultado que gobierna

> Mantener visibles persona, tiempo, procedencia y consecuencia mientras una
> tarea clínica pasa de observación a acción.

La gráfica debe comprimir complejidad sin ocultar conflicto, obsolescencia,
incertidumbre, identidad ni consecuencias. Minimalismo significa menos
competencia visual y más relación visible; no menos información necesaria.
Los objetos, componentes y tres direcciones TLHD de las referencias son
candidatos condicionados a este binding paciente/episodio, no universales para
cualquier UI clínica.

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
  modo?: FRAME | MODEL | DESIGN | BUILD | EVALUATE | FULL,
  necesidad,
  contexto_clinico,
  rol_y_tarea,
  responsabilidad,
  objeto_primario_candidato?,
  plataforma: responsive-web | mobile-web,
  soportes: web | smartphone | ambos,
  data_classification: synthetic | deidentified | phi | unknown,
  domain_authority_receipt?: {
    evidence_id, authority, competent_role, source, scope,
    version_or_date, validity, approved_decisions
  },
  mutation_authorized?: false | true,
  mutation_authority_receipt?: {
    evidence_id, authority, source, repository, paths,
    operations, commands, external_actions
  },
  selected_direction?,
  graphic_spec_binding?,
  implementation_target?: {
    repository, stack, entrypoint, build_command, test_command?, runtime_runner?
  },
  alternativa_actual?,
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

Antes de abrir rutas, URLs, código, logs o runtimes, resolver
`data_classification`. Si falta, tratarla como `unknown`. Con `phi` o `unknown`
no dereferenciar, capturar, registrar ni repetir el contenido: devolver
`phi-boundary` y pedir un fixture sintético o desidentificado autorizado.

Requisitos por modo:

- `BUILD`: `selected_direction`, `graphic_spec_binding`,
  `implementation_target`, `mutation_authorized=true` y
  `mutation_authority_receipt`;
- `EVALUATE`: `artefactos`, `repo_o_url` o evidencia observable;
- `FULL`: satisfacer cada requisito al llegar a su gate; no inferir autoridad
  de mutación desde el cwd, una ruta o el acceso técnico;
- `FRAME`, `MODEL` y `DESIGN`: pueden usar contenido sintético sin autoridad de
  dominio, pero no promover semántica clínica sensible ni integración.

## Errores observables

Devolver `UI_DESIGN_ERROR` con el sobre común, más `code`, `blocking` y
`minimum_action`:

- `insufficient-context` — no se distinguen contexto, rol o tarea;
- `phi-boundary` — el insumo contiene PHI o no está clasificado;
- `domain-authority-required` — una decisión visual depende de política o
  significado clínico no autorizado;
- `unresolved-reference` — marco, canon o skill requerida no resuelve;
- `unsupported-platform` — se pide app nativa, híbrida u otra plataforma no
  cubierta por esta versión;
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

Tras pasar la frontera de datos, leer
`referencias/marco-ui-clinica-web-movil.md` antes de producir una decisión
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

Clasificar toda conclusión y declarar uno o más alcances epistémicos:

`SPEC_ONLY | MODEL_STRUCTURAL | STATIC | RUNTIME_AUTOMATED |
RUNTIME_MANUAL | HUMAN_VALIDATED | DOMAIN_VALIDATED`

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

Los alcances no forman una escalera automática: una observación runtime no
implica validación humana o de dominio. Sin artefacto ejecutable, activar
`SPEC_ONLY`: no declarar funcionamiento, accesibilidad ni rendimiento.

## Composición

Las URN de `componible` son candidatos. Resolver la fuente y leer su
`SKILL.md` completa antes de usarla. La arista no prueba invocación, wiring,
preservación de conducta ni autoridad runtime.

### Dirección de producto

Usar `urn:dev:artefacto:diseno-producto-integrado` en `FRAME`, `DESIGN` y
`FULL` cuando exista una tensión de producto o varias direcciones plausibles.

```text
I_product = {necesidad, usuario_y_tarea, contexto, restricciones, insumos}
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
I_ifml = {plataforma, roles, modelo_dominio_autorizado, vistas, eventos, acciones}
O_ifml = {modelo_tipado, patrones, validacion, supuestos, preguntas_abiertas}
```

Si falta semántica de negocio, conservar el gate de elicitación de IFML; no
fabricar acciones ni transiciones.

### Implementación

Usar `urn:dev:artefacto:ship-discipline` sólo en `BUILD` o en la fase de
implementación de `FULL`.

```text
I_ship = {repo, direccion, graphic_spec_binding, build_contract, alcance,
          mutation_authority_receipt, restricciones}
O_ship = {patch, build, tests, lint, integracion, deuda, cierre}
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

Cuando corresponda, exigir recibos estructurados:

```text
ACCESSIBILITY_RECEIPT = {
  platform, criterion_or_sc, route, state, device_and_at,
  evidence, result, limits
}
PERFORMANCE_RECEIPT = {
  device, network, command, baseline, budget, repetitions,
  measurement, result, limits
}
```

## Workflow común

### `enrutar`

1. Fijar un modo.
2. Clasificar datos antes de abrir cualquier recurso; detener `phi|unknown`.
3. Admitir sólo `responsive-web|mobile-web`; rechazar stacks nativos.
4. Resolver referencias requeridas tras pasar la frontera de datos.
5. Estimar qué acciones son read-only y cuáles mutan código.
6. Registrar los adaptadores activados; el operador invoca sólo esta skill.

### `reunir-evidencia`

1. Construir `EVIDENCE_LEDGER`.
2. Leer sólo brief, spec, código y artefactos clasificados y autorizados.
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
materiales, usar el adaptador IFML. Sin `domain_authority_receipt`, dejar como
preguntas las acciones, guards y políticas clínicas; no fabricarlas.

### `divergir`

Para TLHD o un binding paciente/episodio equivalente, materializar tres
direcciones candidatas con el mismo contenido y estados:

1. `Ledger clínico`;
2. `Hilo de evidencia`;
3. `Escena de decisión`.

Cada una incluye web y smartphone, normal, crítico, vacío, error y recepción
incierta. No tratarlas como respuesta universal ni producir tres skins de la
misma estructura; si el binding no corresponde, enrutar al método general.

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
- `BUILD`: sólo tras G8 verde cuando la semántica sea sensible; exige dirección,
  spec, target y recibo de mutación, luego cierra el loop técnico;
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

Si existe runtime clasificado y autorizado, ejecutar comandos autorizados y
conservar sólo evidencia sin PHI. Si aparece PHI, detener captura/log, no
repetir el contenido y devolver `phi-boundary`. Si no existe runtime, degradar
hallazgos a documental o estático.

### `entregar`

Emitir un único `UI_PACKET` del modo; no omitir bindings, evidencia, deuda,
gates, riesgos ni siguiente acción.

## Salidas

Toda salida exitosa usa un único sobre:

```text
UI_PACKET = {
  mode, input_binding, graphic_spec_binding?, epistemic_status,
  evidence_ledger, gates: {G1..G10}, decision, result,
  debt, risks, next_action
}
```

`UI_DESIGN_ERROR` conserva `mode`, bindings disponibles, `epistemic_status`,
`evidence_ledger` y `gates`, y añade `code`, `blocking` y `minimum_action`.

El `result` tipado por modo es:

- `UI_FRAME_PACKET`: `frame`, `force_map`, hipótesis de objeto, principios,
  invariantes y `GRAPHIC_SPEC_FRAME`;
- `UI_MODEL_PACKET`: candidatos, decisión abierta/elegida, interacción,
  `IFML_MODEL?` y preguntas de dominio;
- `UI_DESIGN_PACKET`: tres direcciones comparables, decisión, sistema,
  composiciones web/mobile web, estados, spec/prototipo y handoff;
- `UI_IMPLEMENTATION_PACKET`: binding de spec y autorización, patch, traza del
  sistema, recibos de build/test/lint y evidencia runtime disponible;
- `UI_EVALUATION_PACKET`: hallazgos, matrices visual/crash,
  `ACCESSIBILITY_RECEIPT[]`, `PERFORMANCE_RECEIPT[]`, dominio y veredicto;
- `UI_FULL_PACKET`: resultados realmente producidos, adaptadores activados y
  primer gate rojo; no agrega secciones vacías para aparentar completitud.

## Gates

IDs y orden canónicos:

1. `G1-problem` — contexto, rol, tarea, responsabilidad y fallo observable;
2. `G2-data-privacy` — clasificación y autorización antes de leer evidencia;
3. `G3-object` — identidad, ciclo, tiempo, procedencia y relaciones;
4. `G4-concepts` — direcciones comparables bajo el mismo fixture;
5. `G5-visual-system` — tokens, primitives y componentes trazables;
6. `G6-states` — crash matrix, asincronía, error e incertidumbre;
7. `G7-responsive` — invariantes y composición web/mobile web;
8. `G8-domain-authority` — recibo competente para promoción sensible;
9. `G9-implementation-access-performance` — target ejecutable y recibos;
10. `G10-evidence` — claims ligados a evidencia y límites explícitos.

No promover por promedio. Un gate rojo mantiene la salida como propuesta o
prototipo. `FRAME` y `DESIGN` sintéticos pueden registrar G8 pendiente; `BUILD`
productivo y `FULL` se detienen antes de implementar semántica sensible sin G8.

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
19. Sin `domain_authority_receipt`, permitir framing y prototipo sintético, pero
    no promover identidad, alertas, órdenes, override, privacidad o corrección.
20. No importar `steve-jobs-principios-salud` por defecto.
21. No abrir recursos con datos `phi` o `unknown`.
22. No inferir autorización de mutación desde acceso técnico, cwd o rutas.
23. No declarar soporte de app nativa desde evidencia web.
