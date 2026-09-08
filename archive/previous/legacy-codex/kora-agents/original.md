---
_manifest:
  urn: urn:kora:artefacto:kora-agents
  type: artefacto
  provenance:
    created_by: OpenAI Codex
    created_at: '2026-05-04'
    source: Reconstruccion fresca desde gobernanza, harness-spec, autoria-spec .
      No absorbe el stack meta-KORA historico marcado rebuild_required.
version: 0.2.1
status: activo
nombre: kora-agents
descripcion: Construye, revisa, edita y mantiene agentes KORA canonicos antes
  de transmutarlos, conservando forma material, vector PMI x LFS, conocimiento
  permitido, lifecycle y gates alineados con las specs vigentes.
tags:
- kora
- agentes
- autoria
- construccion-agentica
- mantenimiento
- ciclo-vida
- auditoria
- transmutacion
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 0
      xi: 2
      lambda: 0
      phi: 1
      sigma:
      - 2
      - 1
      - 3
      - 3
      - 1
    presentacion: accion-primaria
    atlas:
      arnes_categorico: disciplina
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo:
    - claude-code
    - codex
    - opencode
    - openclaw
    nivel_prescripcion: alto
    conocimiento_permitido:
    - urn:kora:kb:gobernanza
    - urn:kora:kb:harness-spec
    - urn:kora:kb:autoria-spec
    - urn:kora:kb:md-spec
    - urn:kora:kb:qa-spec
    - urn:kora:kb:risk-register-spec
    - urn:kora:kb:runtime-spec-md
    - urn:kora:kb:multiagente-spec
    - urn:kora:kb:transmutation-spec
    - urn:kora:kb:claude-code-runtime-extension
    - urn:kora:kb:codex-runtime-extension
    - urn:agengai:kb:openclaw-runtime-extension
    - urn:kora:kb:meta-kora-rebuild-directive
    componible_con:
      - urn:kora:artefacto:kora-agentic-lifecycle
      - urn:kora:artefacto:kora-skills
      - urn:kora:artefacto:cat-thinking
artefacto:
  perfil:
    dominio:
    - kora
    - agentes
    - autoria
    - construccion
    - auditoria
    - transmutacion
    disparadores:
    - crear o reconstruir un agente KORA desde requerimientos
    - mantener, editar o versionar un AGENT.md productivo o en staging
    - auditar un AGENT.md contra autoria-spec, harness-spec y construction-spec
    - mejorar vector, forma material, interfaz, conocimiento permitido o invariantes
      de un agente
    - preparar un agente para transmutacion runtime sin saltarse el IR canonico
    - deprecar, retirar o reactivar un agente con evidencia de lifecycle
    - decidir si una capacidad debe ser skill, subagente, agente o plataforma
    salidas:
    - AGENT.md canonico en artifacts/agents/_FRAGUA/REVIEW/ o diagnostico de bloqueo
    - blueprint minimo con vector PMI x LFS, forma material, interfaz y conocimiento
      permitido
    - reporte de hallazgos con regla propietaria, impacto y fix recomendado
    - lista de gates KORA requeridas antes de transmutar o promover
  plan:
    estado_inicial: triaje
    estado_terminal: cierre-verificado
    estados:
    - triaje
    - cargar-canon
    - capturar-req
    - fijar-blueprint
    - materializar-ir
    - auditar-ir
    - verificar-gates
    - cierre-verificado
  interfaz:
    herramientas:
    - Read
    - Grep
    - Glob
    - Bash
    - Write
    permisos: Lectura de specs KORA y escritura acotada a artifacts/agents/_FRAGUA/REVIEW/,
      tests o docs de soporte cuando el operador pide construir, editar,
      mantener o reparar agentes. No pushea ni despliega por si misma.
    protocolos:
      entrada: intent, requisitos, path de agente o propuesta de forma material
      salida: AGENT.md canonico, diagnostico accionable o handoff a kora-skills si
        la forma material correcta es habilidad
  invariantes:
    reglas_duras:
    - 'Leer la regla propietaria antes de diagnosticar: gobernanza, harness-spec,
      autoria-spec  son el canon minimo.'
    - No usar artefactos meta-KORA marcados rebuild_required como fuente de diseno,
      prompt, blueprint ni runtime.
    - Construir siempre Req -> Blueprint -> IR -> Runtime; nunca saltar directo a
      un bundle runtime.
    - 'Elegir la forma material mas baja que satisface el trabajo: habilidad, subagente,
      agente-propiamente-tal o agente-plataforma.'
    - Todo conocimiento gobernado debe declararse como URN resoluble en extensions.kora.conocimiento_permitido.
    - El vector PMI x LFS debe estar dentro del dominio de realizabilidad de la forma
      material y runtime objetivo.
    - Un agente con memoria, delegacion o riesgo no trivial debe declarar interfaz,
      invariantes y deuda residual verificables.
    - Los cambios deben terminar con gates o bloqueo explicito; un diagnostico fallido
      no se presenta como listo.
    compromisos_eticos:
      transparencia: Separar hechos verificados, inferencias y decisiones editoriales.
      responsabilidad: Declarar impacto, riesgo y rollback antes de promocion o deploy.
---

# kora-agents

## Proposito

Construir, revisar, editar y mantener agentes KORA desde el canon vigente. Esta
skill guia al agente invocador para pasar de requerimientos o deuda operacional
a `AGENT.md` canonico, sin usar artefactos historicos como fuente ni tratar
bundles runtime como autoridad.

## Cuando Usar

- Crear un agente KORA nuevo.
- Reconstruir un agente retirado o marcado `rebuild_required`.
- Auditar un `AGENT.md` antes de promoverlo o transmutarlo.
- Editar, versionar, deprecar o retirar un agente KORA existente.
- Ajustar forma material, vector PMI x LFS, interfaz, conocimiento permitido o
  invariantes.
- Decidir si una capacidad debe seguir siendo skill o subir a agente.

## Cuando No Usar

- Crear o mejorar una skill portable: usar `urn:kora:artefacto:kora-skills`.
- Gestionar un ciclo end-to-end que cruce agentes y skills: usar
  `urn:kora:artefacto:kora-agentic-lifecycle`.
- Corregir specs KORA globales: usar la skill vigente de custodia normativa
  cuando este productiva.
- Desplegar runtime directamente: primero debe existir IR canonico verificado.
- Resucitar el stack meta-KORA historico: solo puede servir como inventario
  negativo segun `urn:kora:kb:meta-kora-rebuild-directive`.

## Workflow

1. Clasificar el intent: `crear`, `reconstruir`, `mejorar`, `auditar`,
   `editar`, `mantener`, `promover`, `deprecar`, `retirar` o `bloqueado`.
2. Cargar canon minimo con `python3 toolchain/kora resolve` para las URNs
   declaradas en `conocimiento_permitido`.
3. Capturar requerimientos: rol, usuario, objetivo observable, forma material,
   conocimiento, interfaz, estado, riesgos y runtime esperado.
4. Fijar blueprint: vector PMI x LFS, atlas, shape requerido, salidas,
   invariantes y gates.
5. Materializar solo en `artifacts/agents/_FRAGUA/REVIEW/{ns}/{name}/AGENT.md`
   salvo que el operador pida una edicion productiva explicita.
6. Auditar contra `autoria-spec`, `harness-spec` y runtime-extension aplicable.
7. Ejecutar gates proporcionales: `python3 toolchain/kora check --strict`,
   `python3 toolchain/kora validate --profile strict` y tests relevantes.
8. Emitir cierre con outcome: `ready`, `needs_repair`, `blocked`,
   `deprecated` o `rerouted`.

## Reglas Duras

- La salida autoritativa es `AGENT.md`, no `_BUILD/`, prompts runtime ni docs
  derivadas.
- La forma material se deriva del vector y del trabajo real, no del packaging
  preferido.
- No declarar `agente-plataforma` si no hay materia ambiental y runtime capaz
  de sostenerla.
- No introducir URNs no resolubles, paths duros como conocimiento gobernado ni
  placeholders decorativos.
- `entornos_objetivo` no incluye runtimes pausados (`agentskills`, `gemini`,
  `mastra`); esos targets solo se usan con `--force-paused` e HITL. `opencode`
  esta activo desde el HITL del 2026-06-04.
- Toda perdida entre requerimiento, blueprint e IR debe quedar como descarte,
  riesgo o deuda residual.
- Si el resultado requiere runtime, transmutar solo despues de gates verdes.

## Salida Esperada

Un patch pequeno y verificable: `AGENT.md` canonico o diagnostico bloqueante,
con comandos ejecutados, deuda residual y siguiente paso operativo.
