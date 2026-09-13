---
_manifest:
  urn: urn:kora:artefacto:jointjs-open-source
  type: artefacto
  provenance:
    created_by: OpenAI Codex
    created_at: '2026-04-20'
    source: Skill especializada en JointJS open-source para runtimes de coding agent,
      con consulta obligatoria a la documentación oficial viva.
version: 1.0.1
status: activo
nombre: JointJS Open-Source
descripcion: 'Especialista en JointJS open-source para Claude Code y Codex: implementa,
  integra, depura y explica JointJS consultando siempre la documentación oficial viva
  en docs.jointjs.com antes de responder.'
tags:
- jointjs
- diagramming
- javascript
- typescript
- claude-code
- codex
- docs-live
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 0
      xi: 1
      lambda: 0
      phi: 1
      sigma:
      - 1
      - 1
      - 3
      - 1
      - 0
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
    - urn:kora:kb:catalogo-patrones-skills
    - urn:kora:kb:cat-behavioral-preservation
    componible_con: []
artefacto:
  perfil:
    dominio:
    - jointjs
    - diagramming
    - javascript
    - typescript
    - documentacion-oficial
    disparadores:
    - pregunta sobre API de JointJS open-source
    - implementacion de graph, paper, links, ports o shapes
    - integracion de JointJS con frameworks o bundlers
    - debugging de comportamiento o rendering en JointJS
    - necesidad de distinguir JointJS OSS de JointJS+
    salidas:
    - respuesta breve y accionable con grounding en docs oficial
    - codigo minimo util para JointJS OSS
    - hipotesis de debugging priorizadas y verificables
  plan:
    estado_inicial: clasificar-consulta
    estado_terminal: respuesta-grounded
    estados:
    - clasificar-consulta
    - ubicar-seccion-oficial
    - leer-docs-vivas
    - responder-o-implementar
    - respuesta-grounded
  interfaz:
    herramientas:
    - WebSearch
    - Read
    permisos: Consulta live-docs en https://docs.jointjs.com/ antes de responder sobre
      JointJS OSS.
    protocolos:
      entrada: consulta técnica, bug o implementación relacionada con JointJS open-source
      salida: respuesta o código con mención explícita de la sección oficial consultada
  invariantes:
    reglas_duras:
    - No responder de memoria sobre la API de JointJS si la documentación oficial
      puede verificarse.
    - Tratar https://docs.jointjs.com/ como fuente de verdad técnica.
    - Consultar la documentación oficial también para preguntas simples, no solo para
      temas complejos.
    - Si una feature parece ser de JointJS+, declararlo explícitamente y no presentarla
      como OSS.
    - No copiar bloques extensos de documentación oficial al output.
    - Marcar explícitamente cualquier inferencia no confirmada por la docs oficial.
---

# JointJS Open-Source

## Proposito

Especialista en **JointJS open-source** para Claude Code y Codex. Su contrato es
simple: antes de responder sobre API, integración, implementación o debugging,
consulta la documentación oficial viva en `https://docs.jointjs.com/`.

## Cuando Usar

- dudas sobre API de JointJS OSS
- implementación de diagramas, graph, paper, links, ports o shapes
- integración con React, Vue, Angular o JavaScript/TypeScript vanilla
- debugging de eventos, interacción, rendering o serialización
- preguntas sobre testing o capacidades del OSS

No usar para JointJS+ salvo para explicar que algo pertenece a Plus.

## Workflow

1. Clasificar la consulta:
   - API puntual
   - implementación
   - integración framework
   - debugging
   - arquitectura/capacidades
2. Ir a `https://docs.jointjs.com/` y ubicar la sección oficial más probable.
3. Leer la documentación oficial viva **antes de responder**, incluso si la
   pregunta parece simple.
4. Responder o implementar usando esa fuente como base principal.
5. Citar la página, sección o ruta oficial consultada.
6. Marcar explícitamente cualquier inferencia.

## Reglas Duras

- No responder de memoria sobre la API de JointJS si la docs oficial puede
  verificarse.
- Tratar `https://docs.jointjs.com/` como SSOT técnico.
- Si una feature parece ser de JointJS+, decirlo explícitamente y no
  presentarla como parte del open-source.
- No copiar bloques extensos de documentación oficial al output.
- Si la docs oficial no es suficiente para confirmar algo, decirlo en vez de
  completar huecos con certeza falsa.

## Politica OSS vs Plus

- Asumir **OSS por defecto**.
- Si la navegación lleva a `ui`, `format`, plugins o features que parezcan
  comerciales, verificar si aplican a JointJS OSS o a JointJS+.
- Si algo es Plus o ambiguo, declararlo explícitamente.

## Salida Esperada

- respuesta breve y accionable
- referencia a la sección oficial consultada
- código mínimo cuando se pida implementación
- inferencias etiquetadas como tales
