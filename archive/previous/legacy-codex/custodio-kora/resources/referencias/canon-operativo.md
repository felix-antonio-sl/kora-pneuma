# Canon Operativo KORA

Usar esta referencia cuando la tarea requiera decidir que documento manda o
que URNs hay que cargar antes de auditar o modificar KORA.

## Precedencia

| Orden | Capa | URNs principales | Uso |
|-------|------|------------------|-----|
| 1 | Constitucion | `urn:kora:kb:gobernanza`, `urn:kora:kb:host-roles` | identidad, source of truth, lifecycle, host primary/secondary |
| 2 | Ontologia | `urn:kora:kb:harness-spec`, `urn:kora:kb:qa-spec`, `urn:kora:kb:procesos-spec`, `urn:kora:kb:risk-register-spec`, `urn:kora:kb:canario-spec` | vector PMI x LFS, calidad, procesos y riesgo |
| 3 | Serializacion | `urn:kora:kb:autoria-spec`, `urn:kora:kb:md-spec`, `urn:kora:kb:spec-md`, `urn:kora:kb:knowledge-spec` | shape de artefactos, KORA/MD, knowledge y construccion |
| 4 | Runtime | `urn:kora:kb:runtime-spec-md`, `urn:kora:kb:multiagente-spec`, `urn:kora:kb:transmutation-spec` | ejecucion, coordinacion y proyeccion |
| 5 | Runtime extensions canonicas (KORA v7) | `urn:kora:kb:claude-code-runtime-extension`, `urn:kora:kb:codex-runtime-extension`, `urn:agengai:kb:openclaw-runtime-extension`, `urn:kora:kb:hermes-runtime-extension` | dominio y fidelidad por target |
| 6 | Artefactos | `urn:{ns}:artefacto:{id}` | agentes, skills y workspaces |
| 7 | Derivados | `docs/generated/*`, `_BUILD/` | vistas materializadas y outputs regenerables |

## Regimenes De Identidad

| Tipo | URN | Version |
|------|-----|---------|
| Knowledge/spec | `urn:{ns}:kb:{id}` | campo `version` fuera del URN |
| Artefacto agentico | `urn:{ns}:artefacto:{id}` | campo `version` fuera del URN |

No usar regimenes retirados como `urn:{ns}:agent:{id}` o URNs de skill con
version embebida.

## Mapa De Propiedad

| Pregunta | Documento propietario |
|----------|-----------------------|
| Que es fuente primaria | `urn:kora:kb:gobernanza` |
| Que valores puede tener el vector | `urn:kora:kb:harness-spec` |
| Como se escribe `SKILL.md` o `AGENT.md` | `urn:kora:kb:autoria-spec` |
| Como construir un artefacto antes de transmutar | `urn:kora:kb:autoria-spec` (absorbe metodologia desde v2.0) |
| Como validar KORA/MD o traces | `urn:kora:kb:md-spec` |
| Como viven relations y knowledge graph | `urn:kora:kb:knowledge-spec` |
| Que gate ejecutar | `urn:kora:kb:procesos-spec` y toolchain |
| Como proyectar a runtime | `urn:kora:kb:transmutation-spec` y runtime-extension |
| Que host puede pushear a `origin/master` | `urn:kora:kb:host-roles` |

## Comandos De Carga

```bash
python3 toolchain/kora resolve "urn:kora:kb:gobernanza"
python3 toolchain/kora resolve "urn:kora:kb:harness-spec"
python3 toolchain/kora resolve "urn:kora:kb:autoria-spec"
python3 toolchain/kora resolve "urn:kora:kb:autoria-spec"
python3 toolchain/kora check --list
```

## Restriccion Meta-KORA

La decision vigente exige reconstruir el stack meta-KORA historico desde cero.
No usar `kora/custodio`, `kora/guardian`, `kora/clawforge`, curator,
forgemaster ni skills historicas como fuente de diseno, runtime, blueprint,
prompt operativo o transmutacion. La unica fuente permitida de esa regla es
`urn:kora:kb:meta-kora-rebuild-directive`.
