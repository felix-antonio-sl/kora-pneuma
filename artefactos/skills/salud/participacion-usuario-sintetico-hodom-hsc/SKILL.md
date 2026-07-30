---
urn: urn:salud:artefacto:participacion-usuario-sintetico-hodom-hsc
nombre: participacion-usuario-sintetico-hodom-hsc
version: 1.1.0
estado: activo
descripcion: "Método compartido para que los roles profesionales HODOM-HSC actúen como usuarios sintéticos ideales: descubren necesidades, sintetizan requisitos y costuras, revisan diseño y emiten aceptación interna dentro de su ámbito."
fuente: "Autoría KORA 2026-07-23 desde el dictamen de agent-architect para el panel R01-R14, anclada al mapa hd-dt 04-operacional/mapa-roles-historias-journeys-hodom-hsc.md (sha256:bdf70433a767f2f3df466b76177da0773c2196fb560cb54f1dc27e3a208b2bdd) y al catálogo ejecutable hd-hsc-os adaptadores/auth/role-catalog.ts (sha256:d4af558d2dc5bf57db07d21ea81d3435843132873c59bd830ae16bf2a61296c6). v1.1.0 (2026-07-30): adopta DEV_PERSONAL_FULL para investigación y validación con fuentes reales en el host privado; conserva la frontera Git/publicación y la autoridad profesional humana."
autor: FS
creado: 2026-07-23
lang: es
tags: [salud, hodom, hsc, usuario-sintetico, participacion, requisitos, validacion]
vector: [2, 0, 2, 0, 1]
sigma: [3, 3, 3, 3, 2]
arnes: disciplina
forma: habilidad
herramientas: []
targets: [codex]
alcance: proyecto
conocimiento: [urn:salud:kb:perfil-dev-personal-full]
---

# Participación de usuario sintético HODOM-HSC

## Propósito

Convierte una perspectiva profesional R01–R14 en una fuente proactiva de
necesidades y en un validador interno del producto. El usuario sintético ideal
representa el oficio completo aunque el artefacto, la práctica o la dotación
local todavía no existan. Lo que no esté demostrado se declara como supuesto;
esa ausencia no impide diseñar.

Esta skill posee el método común. La competencia, el antirol, la voz y los
límites de aceptación pertenecen a cada agente profesional.

## Perfil de datos

En el host personal del operador rige
`urn:salud:kb:perfil-dev-personal-full`. El rol puede inspeccionar PII/PHI,
fuentes Drive, salidas de `hsc-agent-cli`, extracts, archivos privados y bases
locales cuando sean necesarios para descubrir una necesidad, reconciliar
identidad o validar una migración. No exige desidentificar antes de razonar ni
una segunda persona para aprobar el trabajo local.

El paquete distingue superficie de trabajo y destino. PII/PHI puede permanecer
en un artefacto privado o gitignored; el resultado que vaya a Git, PR,
documentación compartida o evidencia publicable se emite sin identificadores.
La relajación no amplía la competencia del rol ni convierte la aceptación
sintética en acto profesional o institucional.

## Vocabulario de procedencia

Estas cinco etiquetas son autosuficientes dentro del contrato:

| label | meaning | claim_limit |
|---|---|---|
| N | norma o doctrina sanitaria del corpus KORA | obligación o criterio general según el corpus al corte |
| L | documento oficial/local HSC | regla o diseño documental local; no prueba ejecución |
| O | práctica operacional observada | funcionamiento de facto al corte; la superficie de salida determina si debe desidentificarse |
| D | diseño objetivo o necesidad derivada | estado deseado que debe ratificarse |
| V | validación propietaria pendiente | no se puede presentar todavía como contrato local |

Una afirmación puede combinar etiquetas. La combinación conserva cada límite:
por ejemplo, N/O/D distingue expectativa normativa, práctica observada y diseño
objetivo. V obliga a declarar la validación pendiente, pero no impide producir
el diseño.

## Modos

`MODE = DISCOVER | SYNTHESIZE | REVIEW | ACCEPT`.

- **DISCOVER:** descubre necesidades, cambios de journey e historias de usuario
  sin exigir candidato ni artefacto previo.
- **SYNTHESIZE:** convierte paquetes propios o pares en requisitos y costuras;
  conserva conflictos y disenso sin fabricar consenso.
- **REVIEW:** contrasta un candidato versionado contra criterios profesionales.
- **ACCEPT:** emite aceptación interna final dentro del ámbito profesional del
  rol; no produce actos clínicos, administrativos, directivos o regulatorios
  reales.

Cada invocación ejecuta un modo solicitado por un orquestador externo. La
continuidad vive en `run_id` y `context_packets`, no en memoria implícita ni en
transiciones internas.

## Entrada `I_ROLE`

```text
I_ROLE = {
  schema_version: "2.0",
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
  context_packets?: ROLE_PACKET[]
}
```

`authority_packet` acota la autoridad sintética ejercida en el diseño; no
acredita delegación institucional ni convierte al artefacto en titular real.

## Salida

`O_ROLE = ROLE_PACKET | ROLE_ERROR`.

```text
ROLE_PACKET = {
  schema_version: "2.0",
  run_id: string,
  packet_id: string,
  role: string,
  mode: DISCOVER | SYNTHESIZE | REVIEW | ACCEPT,
  scope: object,
  candidate_binding?: {
    id: string,
    revision: string
  },
  status: complete | complete-with-assumptions,
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
| status | complete,complete-with-assumptions | required |
| position | string | required |
| provenance | list | required |
| assumptions | list | required |
| dissent | list | required |
| decision_handoffs | list | required |
| payload | mode-discriminated-object | required |

`candidate_binding` copia exactamente `candidate.id` y `candidate.revision`.
Está prohibido en DISCOVER y SYNTHESIZE, y es obligatorio en REVIEW y ACCEPT.

```text
ROLE_ERROR = {
  schema_version: "2.0",
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
| REVIEW | required | none | required-equals-candidate | findings,acceptance_criteria,verdict |
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
  findings: list,
  acceptance_criteria: list,
  verdict: PASS | PASS_WITH_CHANGES | FAIL
}

ACCEPT_PAYLOAD = {
  verdict: ACCEPTED | ACCEPTED_WITH_CONDITIONS | REJECTED,
  conditions: list,
  blocking_items: list,
  scope_of_acceptance: string
}
```

## Ley determinista REVIEW a ACCEPT

ACCEPT copia el `candidate_binding` del candidato y aplica el veredicto del
único REVIEW admisible sin reinterpretarlo:

| review_verdict | accept_verdict | conditions | blocking_items |
|---|---|---|---|
| PASS | ACCEPTED | empty | empty |
| PASS_WITH_CHANGES | ACCEPTED_WITH_CONDITIONS | non-empty | empty |
| FAIL | REJECTED | empty | non-empty |

No existe una cuarta combinación válida. `conditions` contiene cambios
exigibles y verificables; `blocking_items` contiene defectos que impiden la
aceptación dentro del alcance profesional.

## Errores observables

- `malformed-input`: falta un campo obligatorio o su tipo es inválido.
- `missing-candidate`: REVIEW o ACCEPT no recibe `candidate`.
- `missing-context-packets`: SYNTHESIZE no recibe al menos un paquete.
- `candidate-revision-mismatch`: ACCEPT no recibe un REVIEW del mismo rol y
  `run_id` con `candidate_binding` idéntico al candidato.
- `ambiguous-review`: ACCEPT recibe más de un REVIEW que satisface ese mismo
  binding y no puede identificar un antecedente único.
- `scope-outside-profession`: la pregunta queda fuera del oficio encarnado.
- `authority-packet-conflict`: el sobre contradice la competencia o antirol.
- `discipline-unbound`: R10 recibe SYNTHESIZE, REVIEW o ACCEPT sin
  `authority_packet.discipline`.

Una referencia local ausente no es un error. Se registra en `assumptions` y se
clasifica lo diseñado o pendiente mediante N/L/O/D/V.

## Guards de invocación

| mode | guard | error |
|---|---|---|
| DISCOVER | valid-I_ROLE | malformed-input |
| SYNTHESIZE | at-least-one-context-packet | missing-context-packets |
| REVIEW | candidate-present | missing-candidate |
| ACCEPT | candidate-and-exactly-one-matching-review | missing-candidate-or-revision-mismatch-or-ambiguous-review |

Los guards profesionales R08, R10, R11 y R14 se aplican además de esta tabla.
Un guard fallido produce `ROLE_ERROR`; nunca se degrada silenciosamente a otro
modo ni fabrica un candidato.

## Transiciones externas e idempotencia

| property | value |
|---|---|
| transition_owner | external-orchestrator |
| internal_fsm | forbidden |
| self_invocation | forbidden |
| revision_change | invalidates-prior-review-and-acceptance |
| idempotence_basis | normalized-I_ROLE-plus-context |
| idempotence_projection | packet_id,role,mode,candidate_binding,verdict,conditions,blocking_items,scope_of_acceptance |

La skill no es una FSM y el agente no se autoinvoca. El orquestador decide qué
modo solicitar y aporta explícitamente los paquetes que habilitan el siguiente.
Una revisión nueva del candidato invalida todo REVIEW y ACCEPT de revisiones
anteriores; esa aceptación no se transfiere ni se actualiza por inferencia.

Ante la misma `I_ROLE` normalizada, los mismos `context_packets` y la misma
fuente del rol, una repetición conserva la proyección de idempotencia de la
tabla. Las listas se deduplican y mantienen orden estable. `packet_id` es una
identidad determinista de esa entrada normalizada, no un valor aleatorio ni una
marca de tiempo.

## Invariantes

1. DISCOVER no requiere candidato, historia previa ni evidencia de práctica.
2. Todo supuesto declara afirmación, base, impacto y, cuando exista,
   `validation_owner`; por sí solo no impide REVIEW ni ACCEPT.
3. Cada afirmación trazable porta una o más etiquetas N/L/O/D/V según el
   vocabulario de este contrato y vigencia cuando corresponda. Diseño no se
   presenta como práctica.
4. SYNTHESIZE conserva `dissent`, conflictos y posiciones minoritarias. Los
   `decision_owners` adjudican; el agente no borra el desacuerdo.
5. REVIEW y ACCEPT requieren `candidate` y devuelven `candidate_binding`
   idéntico. ACCEPT requiere además exactamente un REVIEW del mismo rol,
   `run_id`, candidato y revisión dentro de `context_packets`.
6. `decision_handoffs` asigna decisiones externas sin suspender el trabajo que
   sí pertenece al rol.
7. `blocking_items` contiene defectos del candidato dentro del ámbito
   profesional, no la mera falta de evidencia local.
8. La aceptación es interna y queda delimitada por `scope_of_acceptance`.
9. Los identificadores se conservan en la superficie privada cuando sostienen
   identidad, trazabilidad o conciliación; se omiten del producto versionado o
   compartido cuando no son necesarios.
10. El paquete es autocontenido: no depende de memoria oculta entre
    invocaciones.
11. ACCEPT obedece la tabla REVIEW a ACCEPT; sus listas no pueden contradecir el
    veredicto.
12. No hay FSM interna, autoinvocación ni aceptación transferible entre
    revisiones.
13. Una repetición de la misma entrada normalizada conserva la proyección de
    idempotencia declarada.

## Procedimiento

1. Validar `I_ROLE`, condiciones del modo y coherencia de
   `authority_packet`.
2. Encarnar competencia y antirol del agente que ejerce la skill.
3. Separar hechos y propuestas mediante N/L/O/D/V; convertir lagunas en
   `assumptions`.
4. Aplicar los guards del modo y la excepción profesional correspondiente.
5. Ejecutar exactamente el modo solicitado y producir su payload.
6. En REVIEW y ACCEPT, copiar el candidato a `candidate_binding`; en ACCEPT,
   aplicar sin reinterpretación la tabla determinista.
7. Conservar disenso y tipar decisiones externas en `decision_handoffs`.
8. Estabilizar orden, deduplicación e identidad para entradas idempotentes.
9. Emitir un único `ROLE_PACKET` o, sólo ante un error observable, un
   `ROLE_ERROR`.

## Adaptador de agente

El agente consumidor aporta su `role`, competencia, antirol, voz y excepción
profesional. La entrada de esta skill es su `I_ROLE`; la salida se devuelve sin
cambiar el discriminador de modo. La relación declarada en `componible` es un
candidato procedural y necesita esta activación explícita en cada invocación.
