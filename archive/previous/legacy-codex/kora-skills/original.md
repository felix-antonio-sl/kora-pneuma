---
_manifest:
  urn: urn:kora:artefacto:kora-skills
  type: artefacto
  provenance:
    created_by: OpenAI Codex
    created_at: '2026-05-04'
    source: Reconstruccion fresca desde gobernanza, harness-spec, autoria-spec .
      No absorbe el stack meta-KORA historico marcado rebuild_required.
version: 0.2.1
status: activo
nombre: kora-skills
descripcion: Construye, revisa, edita y mantiene skills KORA canonicas con shape
  de autoria vigente, compatibilidad agentskills verificable y gates previas a
  transmutacion o deploy.
tags:
- kora
- skills
- autoria
- agentskills
- construccion-agentica
- mantenimiento
- ciclo-vida
- auditoria
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
    - urn:kora:kb:transmutation-spec
    - urn:kora:kb:agentskills-runtime-extension
    - urn:kora:kb:claude-code-runtime-extension
    - urn:kora:kb:codex-runtime-extension
    - urn:agengai:kb:openclaw-runtime-extension
    - urn:kora:kb:meta-kora-rebuild-directive
    componible_con:
      - urn:kora:artefacto:kora-agentic-lifecycle
      - urn:kora:artefacto:kora-agents
      - urn:kora:artefacto:cat-thinking
artefacto:
  perfil:
    dominio:
    - kora
    - skills
    - autoria
    - construccion
    - auditoria
    - agentskills
    disparadores:
    - crear una skill KORA nueva desde requerimientos
    - mantener, editar o versionar un SKILL.md productivo o en staging
    - revisar o mejorar un SKILL.md contra autoria-spec y construction-spec
    - normalizar una skill para proyeccion codex, claude-code u openclaw
    - decidir si una capacidad portable sigue siendo habilidad o debe promoverse a
      agente
    - preparar transmutacion y deploy de una skill con gates verificadas
    - deprecar, retirar o reactivar una skill con evidencia de lifecycle
    salidas:
    - SKILL.md canonico en artifacts/skills/_TALLER/REVIEW/ o diagnostico de bloqueo
    - blueprint minimo con vector, nivel_prescripcion, interfaz y conocimiento permitido
    - reporte de compatibilidad agentskills y riesgos de proyeccion runtime
    - lista de gates requeridas antes de promover, transmutar o deployar
  plan:
    estado_inicial: triaje
    estado_terminal: cierre-verificado
    estados:
    - triaje
    - cargar-canon
    - capturar-req
    - fijar-blueprint
    - materializar-skill
    - auditar-fidelidad
    - verificar-gates
    - cierre-verificado
  interfaz:
    herramientas:
    - Read
    - Grep
    - Glob
    - Bash
    - Write
    permisos: Lectura de specs KORA y escritura acotada a artifacts/skills/_TALLER/REVIEW/,
      tests o docs de soporte cuando el operador pide construir, editar,
      mantener o reparar skills. No pushea ni despliega por si misma.
    protocolos:
      entrada: intent, requisitos, path de skill o propuesta de capacidad portable
      salida: SKILL.md canonico, diagnostico accionable o handoff a kora-agents si
        la forma material correcta no es habilidad
  invariantes:
    reglas_duras:
    - 'Leer la regla propietaria antes de diagnosticar: gobernanza, harness-spec,
      autoria-spec  son el canon minimo.'
    - No usar artefactos meta-KORA marcados rebuild_required como fuente de diseno,
      prompt, blueprint ni runtime.
    - Construir siempre Req -> Blueprint -> IR -> Runtime; nunca saltar directo a
      un paquete agentskills o bundle runtime.
    - 'Una skill debe permanecer en el dominio de habilidad: capacidad portable, sin
      workspace propio, sin memoria ambiental ni servicio always-on.'
    - Declarar nivel_prescripcion y mantener el body bajo control; detalle voluminoso
      debe ir a referencias o recursos.
    - Todo conocimiento gobernado debe declararse como URN resoluble en extensions.kora.conocimiento_permitido.
    - La proyeccion agentskills no debe perder instrucciones esenciales ni introducir
      subdirectorios no canonicos.
    - Los cambios deben terminar con gates o bloqueo explicito; un diagnostico fallido
      no se presenta como listo.
    compromisos_eticos:
      transparencia: Separar hechos verificados, inferencias y decisiones editoriales.
      responsabilidad: Declarar impacto, riesgo y rollback antes de promocion o deploy.
---

# kora-skills

## Proposito

Construir, revisar, editar y mantener skills KORA desde el canon vigente. Esta
skill guia al agente invocador para pasar de requerimientos o deuda operacional
a `SKILL.md` canonico, con forma material `habilidad` y proyeccion runtime
posterior.

## Cuando Usar

- Crear una skill KORA nueva.
- Reconstruir una skill retirada o marcada `rebuild_required`.
- Auditar un `SKILL.md` antes de promoverlo, transmutarlo o deployarlo.
- Editar, versionar, deprecar o retirar una skill KORA existente.
- Ajustar nivel de prescripcion, vector PMI x LFS, interfaz, conocimiento
  permitido o instrucciones.
- Verificar fidelidad hacia agentskills y runtimes locales.

## Cuando No Usar

- Crear o mejorar agentes, subagentes o plataformas: usar
  `urn:kora:artefacto:kora-agents`.
- Gestionar un ciclo end-to-end que cruce agentes y skills: usar
  `urn:kora:artefacto:kora-agentic-lifecycle`.
- Corregir specs KORA globales: usar la skill vigente de custodia normativa
  cuando este productiva.
- Empaquetar runtime sin IR canonico verificado.
- Resucitar el stack meta-KORA historico: solo puede servir como inventario
  negativo segun `urn:kora:kb:meta-kora-rebuild-directive`.

## Workflow

1. Clasificar el intent: `crear`, `reconstruir`, `mejorar`, `auditar`,
   `editar`, `mantener`, `promover`, `deprecar`, `retirar` o `bloqueado`.
2. Cargar canon minimo con `python3 toolchain/kora resolve` para las URNs
   declaradas en `conocimiento_permitido`.
3. Capturar requerimientos: objetivo observable, usuarios, disparadores,
   herramientas, conocimiento, riesgo y runtimes esperados.
4. Confirmar que la forma material correcta es `habilidad`; si requiere
   workspace, memoria persistente, delegacion compleja o servicio, hacer handoff
   a `kora-agents`.
5. Materializar solo en `artifacts/skills/_TALLER/REVIEW/{name}/SKILL.md`
   salvo que el operador pida una edicion productiva explicita.
6. Auditar contra `autoria-spec`, `harness-spec` y runtime-extension aplicable.
7. Ejecutar gates proporcionales: `python3 toolchain/kora check --strict`,
   `python3 toolchain/kora lint-md` y transmutacion dry-run o real segun el
   objetivo.
8. Emitir cierre con outcome: `ready`, `needs_repair`, `blocked`,
   `deprecated` o `rerouted`.

## Reglas Duras

- La salida autoritativa es `SKILL.md`, no `_BUILD/`, paquetes agentskills ni
  docs derivadas.
- La skill no debe esconder una plataforma: si necesita materia ambiental o
  estado propio, no es habilidad.
- No introducir URNs no resolubles, paths duros como conocimiento gobernado ni
  placeholders decorativos.
- `entornos_objetivo` no incluye runtimes pausados (`agentskills`, `gemini`,
  `mastra`); agentskills queda como compatibilidad verificada, no como target
  canonico. `opencode` esta activo desde el HITL del 2026-06-04.
- El body debe ser conciso; recursos grandes van fuera y se cargan solo cuando
  hagan falta.
- Toda perdida entre requerimiento, blueprint e IR debe quedar como descarte,
  riesgo o deuda residual.
- Si el resultado requiere runtime, transmutar y deployar solo despues de gates
  verdes.

## Salida Esperada

Un patch pequeno y verificable: `SKILL.md` canonico o diagnostico bloqueante,
con comandos ejecutados, deuda residual y siguiente paso operativo.
