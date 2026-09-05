
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
