
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
