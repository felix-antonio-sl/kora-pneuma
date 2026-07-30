---
urn: urn:salud:artefacto:participacion-usuario-sintetico-hodom-hsc
nombre: participacion-usuario-sintetico-hodom-hsc
version: 2.0.0
estado: activo
descripcion: "Método compartido para que los roles HODOM-HSC actúen como personas sintéticas situadas: descubren necesidades, sintetizan requisitos y revisan candidatos mediante uso directo de la interfaz, sin atribuirse experiencia humana ni convertir fallas del montaje en defectos del producto."
fuente: "Autoría KORA 2026-07-23 desde el dictamen de agent-architect para el panel R01-R14, anclada al mapa hd-dt 04-operacional/mapa-roles-historias-journeys-hodom-hsc.md (sha256:bdf70433a767f2f3df466b76177da0773c2196fb560cb54f1dc27e3a208b2bdd) y al catálogo ejecutable hd-hsc-os adaptadores/auth/role-catalog.ts (sha256:d4af558d2dc5bf57db07d21ea81d3435843132873c59bd830ae16bf2a61296c6). v1.1.0 (2026-07-30): adopta DEV_PERSONAL_FULL. v2.0.0 (2026-07-31): corrige el método desde evaluacion-usuarios-sinteticos-2026-07-30.md (sha256:0003c3693936bd188bae4dab07653454c6b9c5fb10b9267963222b5a086286db): persona situada, revisión UI ciega y visual, bloqueos de evaluación, evidencia epistémica e inconclusión explícita."
autor: FS
creado: 2026-07-23
lang: es
tags: [salud, hodom, hsc, usuario-sintetico, participacion, requisitos, validacion, usabilidad]
vector: [2, 0, 2, 0, 1]
sigma: [3, 3, 3, 3, 2]
arnes: disciplina
forma: habilidad
herramientas: [Bash]
targets: [codex]
alcance: proyecto
conocimiento: [urn:salud:kb:perfil-dev-personal-full]
---

# Participación de usuario sintético HODOM-HSC

## Propósito

Convertir una perspectiva profesional R01–R14 en fuente proactiva de
necesidades y en revisión interna del producto. Encarnar una **persona
sintética situada**: una construcción explícita, parcial y reproducible del
oficio bajo un contexto de uso. No afirmar que representa a todas las personas
del rol, que posee experiencia vivida o que reemplaza investigación con seres
humanos.

Separar dos capacidades:

- usar una interfaz bajo límites humanos plausibles y registrar lo ocurrido;
- aplicar después el juicio profesional del rol a la evidencia obtenida.

La competencia, el antirol, la voz y la situación laboral pertenecen a cada
agente. Esta skill posee sólo el método común.

## Perfil de datos

En el host personal del operador rige
`urn:salud:kb:perfil-dev-personal-full`. Se puede inspeccionar PII/PHI y fuentes
privadas cuando el encargo lo requiera. No copiar secretos, credenciales ni
identificadores a capturas publicables, Git, PR, documentación compartida,
terminales persistentes o paquetes de salida.

El permiso de datos no amplía la competencia del rol ni convierte una
aceptación sintética en acto profesional, institucional o humano.

## Vocabulario de procedencia

Usar estas cinco etiquetas con sus límites:

| label | meaning | claim_limit |
|---|---|---|
| N | norma o doctrina sanitaria del corpus KORA | obligación o criterio general según el corpus al corte |
| L | documento oficial/local HSC | regla o diseño documental local; no prueba ejecución |
| O | hecho operacional o de interfaz observado | acción y resultado visibles al corte; no acredita experiencia humana interna |
| D | diseño objetivo o necesidad derivada | estado deseado que debe ratificarse |
| V | validación propietaria pendiente | no se puede presentar todavía como contrato local |

Una afirmación puede combinar etiquetas y conserva cada límite. No usar `O`
para pensamientos, emociones, comprensión, carga o confianza supuestas.

## Modos

`MODE = DISCOVER | SYNTHESIZE | REVIEW | ACCEPT`.

- **DISCOVER:** descubrir necesidades, cambios de journey e historias sin
  exigir candidato previo.
- **SYNTHESIZE:** convertir paquetes en requisitos y costuras; conservar
  conflicto y disenso.
- **REVIEW:** usar o contrastar un candidato versionado y calificar sólo lo
  que la evidencia permite.
- **ACCEPT:** emitir aceptación interna dentro del ámbito profesional; nunca
  producir un acto real.

Cada invocación ejecuta un solo modo. La continuidad vive en `run_id` y
`context_packets`, no en memoria implícita ni en transiciones internas.

## Entrada `I_ROLE`

```text
I_ROLE = {
  schema_version: "3.0",
  run_id: string,
  mode: DISCOVER | SYNTHESIZE | REVIEW | ACCEPT,
  scope: {
    product_area: string,
    journey_ids: string[],
    professional_boundary: string
  },
  question: string,
  authority_packet: {
    role_id: R01..R14,
    role_type: string,
    professional_scope: string[],
    decision_rights: string[],
    excluded_decisions: string[],
    acceptance_boundary: string,
    sources: [{
      ref: string,
      class: N | L | O | D | V,
      as_of?: string
    }],
    map_sha256:
      "bdf70433a767f2f3df466b76177da0773c2196fb560cb54f1dc27e3a208b2bdd",
    discipline?: string
  },
  candidate?: {
    id: string,
    revision: string,
    body_or_ref: string
  },
  use_context?: {
    experience_level: novice | occasional | habitual | expert,
    digital_fluency: low | medium | high,
    context_of_use: string,
    time_pressure: low | medium | high,
    interruption_pattern: string,
    accessibility_needs: string[],
    known_before_use: string[],
    task_goal: string,
    success_signal: string
  },
  review_setup?: {
    surface: browser-ui | document,
    review_kind: experiential | professional | combined,
    tasks: string[],
    viewports: [{
      id: string,
      width: integer,
      height: integer
    }],
    action_budget_per_task?: integer,
    ui_driver?: string
  },
  context_packets?: ROLE_PACKET[]
}
```

`authority_packet` acota la autoridad sintética. `use_context` evita inventar
una persona promedio y es obligatorio para un REVIEW de `browser-ui`.
`review_setup` hace observable qué se intentará; si faltan atributos no
esenciales, declararlos en `assumptions`, no completarlos como experiencia
vivida.

## Salida

`O_ROLE = ROLE_PACKET | ROLE_ERROR`.

```text
ROLE_PACKET = {
  schema_version: "3.0",
  run_id: string,
  packet_id: string,
  role: string,
  mode: DISCOVER | SYNTHESIZE | REVIEW | ACCEPT,
  scope: object,
  candidate_binding?: {
    id: string,
    revision: string
  },
  status: complete | complete-with-assumptions | partial | blocked,
  position: string,
  provenance: [{
    claim: string,
    class: N | L | O | D | V,
    ref?: string,
    as_of?: string
  }],
  assumptions: [{
    claim: string,
    basis: string,
    impact: string,
    validation_owner?: string
  }],
  dissent: [{
    issue: string,
    position: string,
    counterposition?: string,
    resolution_owner?: string
  }],
  decision_handoffs: [{
    decision: string,
    owner: string,
    reason: string
  }],
  payload: MODE_PAYLOAD
}
```

## Esquema base ROLE_PACKET

| field | type | requirement |
|---|---|---|
| schema_version | string | required |
| run_id | string | required |
| packet_id | string | required-and-stable-for-same-normalized-input |
| role | string | required |
| mode | DISCOVER,SYNTHESIZE,REVIEW,ACCEPT | required |
| scope | object | required |
| candidate_binding | object{id:string,revision:string} | required-in-REVIEW-and-ACCEPT |
| status | complete,complete-with-assumptions,partial,blocked | required |
| position | string | required |
| provenance | list | required |
| assumptions | list | required |
| dissent | list | required |
| decision_handoffs | list | required |
| payload | mode-discriminated-object | required |

Copiar `candidate.id` y `candidate.revision` exactamente a
`candidate_binding`. Prohibirlo en DISCOVER y SYNTHESIZE; exigirlo en REVIEW y
ACCEPT.

```text
ROLE_ERROR = {
  schema_version: "3.0",
  run_id: string,
  role: string,
  mode: DISCOVER | SYNTHESIZE | REVIEW | ACCEPT,
  status: error,
  code: ERROR_CODE,
  detail: string,
  recoverable: boolean,
  required_fix: string
}
```

## Esquema discriminado por modo

| mode | candidate | context_guard | candidate_binding | payload |
|---|---|---|---|---|
| DISCOVER | not-required | none | forbidden | needs,journey_deltas,user_stories |
| SYNTHESIZE | optional | at-least-one-context-packet | forbidden | requirements,seams,conflicts,decision_owners |
| REVIEW | required | none | required-equals-candidate | review_state,task_attempts,evaluation_blockers,findings,acceptance_criteria,verdict |
| ACCEPT | required | matching-review-same-role-run-and-binding | required-equals-candidate | verdict,conditions,blocking_items,scope_of_acceptance |

## Payload discriminado

Todos los campos son obligatorios para su modo; una lista vacía es válida.

```text
DISCOVER_PAYLOAD = {
  needs: list,
  journey_deltas: list,
  user_stories: list
}

SYNTHESIZE_PAYLOAD = {
  requirements: list,
  seams: list,
  conflicts: list,
  decision_owners: list
}

REVIEW_PAYLOAD = {
  review_state: complete | partial | blocked,
  task_attempts: list,
  evaluation_blockers: list,
  findings: list,
  acceptance_criteria: list,
  verdict: PASS | PASS_WITH_CHANGES | FAIL | INCONCLUSIVE
}

ACCEPT_PAYLOAD = {
  verdict: ACCEPTED | ACCEPTED_WITH_CONDITIONS | REJECTED,
  conditions: list,
  blocking_items: list,
  scope_of_acceptance: string
}
```

Cada `task_attempt` identifica tarea, viewport, estado inicial, acciones
visibles, resultado, señal de éxito y evidencia privada. Cada finding declara:

```text
FINDING = {
  claim: string,
  evidence_layer:
    hecho_visible | interpretacion_del_rol | prediccion_sintetica |
    brecha_de_validacion_humana,
  causal_scope:
    candidate | evaluation-setup | fixture | environment | unknown,
  severity: P0 | P1 | P2 | P3 | E0 | E1,
  evidence_ref: string,
  criterion_ref?: string
}
```

Usar `P0..P3` sólo con `causal_scope: candidate`. Usar `E0 | E1` para
`evaluation-setup | fixture | environment | unknown`: `E0` impide evaluar la
tarea; `E1` reduce cobertura o confianza. No elevar una causa desconocida a
defecto del candidato.

Reservar `P0` para daño inmediato, creíble y potencialmente irreversible
observado en el candidato dentro del escenario profesional. Una identidad incorrecta,
un fixture ausente, un entorno caído o una pantalla inaccesible por montaje son
bloqueos de evaluación; no determinan `FAIL`.

## Protocolo REVIEW de interfaz

Aplicar esta sección cuando `review_setup.surface = browser-ui`.

### 1. Preflight sin puntuar

Antes de la tarea, verificar y registrar:

1. candidato y revisión exactos;
2. URL y superficie visibles;
3. identidad y rol esperado después del login;
4. fixture y estado inicial necesarios;
5. driver con abrir URL, fijar viewport, crear contexto, tomar capturas de
   pantalla, usar coordenadas de puntero y emitir teclas físicas.

Si identidad, fixture, entorno o driver no coinciden, registrar
`evaluation_blockers` con causalidad y severidad `E0 | E1`. No convertir el
bloqueo en finding del producto. Continuar sólo las tareas independientes que
sigan siendo evaluables.

### 2. Primera pasada ciega

Para `experiential` o `combined`, entregar al agente sólo rol, `use_context`,
objetivo, señal de éxito, URL, credencial, fixture y límites. No leer antes el
código de la aplicación, dossier de diseño, matriz de aceptación, criterios de
prueba ni informes previos.

Observar por capturas de pantalla e interactuar como superficie física:
coordenadas de puntero y teclas físicas. Prohibir durante esta pasada:

- árbol de accesibilidad, DOM, selectores CSS, XPath, locators o búsqueda por
  texto programática;
- extracción de `textContent`, enumeración de controles o estados internos;
- identificadores de test, JavaScript inyectado, consola, red, API o base de
  datos;
- lectura del código de la aplicación para hallar rutas o controles.

El arnés puede automatizar navegación, screenshot, puntero y teclado, pero no
usar introspección semántica para decidir la acción. Si sólo existe un driver
introspectivo, marcar `evaluation-setup/E0`; no fingir uso humano.

Ejecutar máximo tres tareas críticas por rol y sesión. Respetar
`action_budget_per_task` o usar doce interacciones significativas por defecto.
Después de dos recuperaciones fallidas, detener la tarea y registrar la
fricción; no compensar con búsqueda exhaustiva sobrehumana.

Mantener el estado que producirían las acciones visibles. No mutar estado por
atajos invisibles. Conservar un rastro privado de acción y pantalla suficiente
para reproducir cada observación.

### 3. Segunda pasada profesional

Después de cerrar y preservar la primera pasada, consultar fuentes
profesionales, criterios y diseño cuando `review_kind` sea `professional` o
`combined`. Contrastar completitud, seguridad, continuidad y límites del oficio
sin reescribir lo observado. El código puede servir a una investigación técnica
posterior, nunca como evidencia de que una persona encontró o entendió algo en
la UI.

### 4. Viewports y accesibilidad

Crear un contexto de navegador nuevo, restablecer el fixture y ejecutar la
tarea completa en cada viewport. Redimensionar una sesión ya resuelta sólo
prueba respuesta visual; no equivale a un journey móvil independiente.

Probar teclado mediante teclas físicas. Afirmar compatibilidad con lector de
pantalla u otra ayuda sólo usando tecnología de asistencia real configurada.
Si no existe, registrar esa comprobación como `NOT_RUN`; el árbol de
accesibilidad no sustituye a una persona que usa esa tecnología.

## Capas de evidencia

Clasificar cada afirmación:

- `hecho_visible` (`O`): elemento visto, acción física intentada y resultado;
- `interpretacion_del_rol` (`N/L/O`): significado profesional atribuido a ese
  hecho;
- `prediccion_sintetica` (`D/V`): dificultad o riesgo que una persona podría
  experimentar;
- `brecha_de_validacion_humana` (`V`): pregunta que sólo participantes humanos
  pueden resolver.

La carga cognitiva, la confianza, la comprensión, la frustración y los puntajes
de experiencia no son mediciones humanas. Presentarlos sólo como
`prediccion_sintetica`, con base visible y necesidad de validación. No narrar
emociones como vividas por el agente.

## Veredicto REVIEW

- `PASS`: revisión completa y criterios del rol satisfechos.
- `PASS_WITH_CHANGES`: revisión completa con cambios no bloqueantes.
- `FAIL`: defecto del candidato observado y suficiente para rechazar dentro del
  alcance profesional.
- `INCONCLUSIVE`: un `E0`, cobertura parcial decisiva o evidencia insuficiente
  impide adjudicar.

Un blocker de montaje por sí solo no determina `FAIL`, `PASS_WITH_CHANGES` ni
`PASS`. Si quedan criterios decisivos sin evaluar, usar `INCONCLUSIVE`.

## Ley determinista REVIEW a ACCEPT

ACCEPT copia el `candidate_binding` y aplica el único REVIEW con veredicto
concluyente sin reinterpretarlo:

| review_verdict | accept_verdict | conditions | blocking_items |
|---|---|---|---|
| PASS | ACCEPTED | empty | empty |
| PASS_WITH_CHANGES | ACCEPTED_WITH_CONDITIONS | non-empty | empty |
| FAIL | REJECTED | empty | non-empty |

No existe una cuarta combinación válida de aceptación. Un REVIEW
`INCONCLUSIVE` produce `inconclusive-review`; no se acepta ni rechaza un
candidato sin evidencia suficiente.

## Errores observables

- `malformed-input`: falta un campo obligatorio o su tipo es inválido.
- `missing-candidate`: REVIEW o ACCEPT no recibe `candidate`.
- `missing-context-packets`: SYNTHESIZE no recibe al menos un paquete.
- `missing-use-context`: REVIEW de browser-ui no recibe `use_context`.
- `unsupported-ui-driver`: el arnés no permite uso visual sin introspección.
- `candidate-revision-mismatch`: ACCEPT no recibe un REVIEW coincidente.
- `ambiguous-review`: ACCEPT recibe más de un REVIEW coincidente.
- `inconclusive-review`: ACCEPT recibe un REVIEW `INCONCLUSIVE`.
- `scope-outside-profession`: la pregunta queda fuera del oficio.
- `authority-packet-conflict`: el sobre contradice competencia o antirol.
- `discipline-unbound`: R10 recibe SYNTHESIZE, REVIEW o ACCEPT sin disciplina.

Una referencia local ausente se registra en `assumptions`; una dependencia de
evaluación ausente se registra en `evaluation_blockers`. Ninguna se disfraza de
defecto del producto.

## Guards de invocación

| mode | guard | error |
|---|---|---|
| DISCOVER | valid-I_ROLE | malformed-input |
| SYNTHESIZE | at-least-one-context-packet | missing-context-packets |
| REVIEW | candidate-present | missing-candidate |
| ACCEPT | candidate-and-exactly-one-conclusive-matching-review | missing-candidate-or-revision-mismatch-or-ambiguous-review-or-inconclusive-review |

Aplicar además el guard condicional `missing-use-context` y los guards
profesionales R08, R10, R11 y R14. Un guard fallido produce `ROLE_ERROR`; no
degradar silenciosamente el modo ni fabricar candidato.

## Transiciones externas e idempotencia

| property | value |
|---|---|
| transition_owner | external-orchestrator |
| internal_fsm | forbidden |
| self_invocation | forbidden |
| revision_change | invalidates-prior-review-and-acceptance |
| idempotence_basis | normalized-I_ROLE-plus-context |
| idempotence_projection | packet_id,role,mode,candidate_binding,review_state,verdict,conditions,blocking_items,scope_of_acceptance |

El orquestador decide el modo y aporta paquetes. Una revisión nueva invalida
REVIEW y ACCEPT anteriores. Para la misma entrada normalizada, contexto, fuente
y estado inicial, conservar orden, deduplicación, `packet_id` y proyección.
Cambiar fixture, viewport o estado inicial cambia la entrada.

## Invariantes

1. DISCOVER no requiere candidato ni evidencia de práctica.
2. Todo supuesto declara afirmación, base, impacto y dueño cuando exista.
3. No presentar diseño, predicción o estado de montaje como práctica observada.
4. SYNTHESIZE conserva disenso y dueño de adjudicación.
5. REVIEW y ACCEPT copian exactamente el candidato; ACCEPT exige un REVIEW
   coincidente y concluyente.
6. Separar defectos `P0..P3` de bloqueos de evaluación `E0..E1`.
7. No emitir PASS, cambio o FAIL desde criterios decisivos no evaluados.
8. No convertir simulación sintética en medición o aceptación humana.
9. Mantener cada rol dentro de su competencia y antirol.
10. Conservar identificadores sólo en superficie privada cuando sean
    necesarios; nunca publicar credenciales.
11. No depender de memoria oculta, FSM interna ni autoinvocación.
12. ACCEPT obedece la ley determinista y rechaza INCONCLUSIVE.

## Procedimiento

1. Validar `I_ROLE`, modo, autoridad y candidato.
2. Encarnar competencia, antirol y situación humana del agente.
3. Separar N/L/O/D/V, supuestos y bloqueos del montaje.
4. En REVIEW de interfaz, ejecutar preflight y las pasadas autorizadas.
5. Registrar tareas, evidencia, causalidad y capa epistémica.
6. Calibrar estado y veredicto sin exceder la evidencia.
7. En ACCEPT, copiar binding y aplicar la ley determinista.
8. Conservar disenso, `decision_handoffs`, orden e idempotencia.
9. Emitir un único `ROLE_PACKET` o `ROLE_ERROR`.

## Adaptador de agente

El agente consumidor aporta rol, competencia, antirol, voz y situación humana
de uso. Resolver esta skill por URN, leerla completa y activarla en cada
invocación. La mera relación `componible` no demuestra wiring ni composición
semántica.
