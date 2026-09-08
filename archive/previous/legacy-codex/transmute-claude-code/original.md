---
_manifest:
  urn: urn:kora:artefacto:transmute-claude-code
  type: artefacto
  provenance:
    created_by: FS
    created_at: '2026-04-23'
    source: 'Migracion desde artifacts/skills/_TALLER/INBOX/transmute-claude-code/SKILL.md
      (legacy skill-overlay v1) a shape unified autoria-spec v1.2; URN regimen artefacto:'
version: 2.0.1
status: activo
nombre: transmute-claude-code
descripcion: Transmuta un AGENT.md KORA a un archivo .md de Claude Code (persona o
  subagente). Lee las 6 dimensiones categoricas del IR y compila cada una al idiom
  de Claude Code, preservando maxima fidelidad y emitiendo _transmutation.yml proof-carrying.
tags:
- transmutacion
- claude-code
- proyeccion
- runtime
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
      - 1
      - 0
    presentacion: accion-primaria
    atlas:
      arnes_categorico: utilidad
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo:
    - claude-code
    - codex
    - opencode
    - openclaw
    nivel_prescripcion: alto
    conocimiento_permitido:
    - urn:kora:kb:autoria-spec
    - urn:kora:kb:transmutation-spec
    - urn:kora:kb:claude-code-runtime-extension
    componible_con: []
artefacto:
  perfil:
    descripcion: Habilidad de transmutacion que proyecta artefactos KORA/MD a archivos
      Claude Code preservando fidelidad y registrando perdidas.
    dominio:
    - transmutacion de runtime
    - Claude Code
    - proof-carrying projection
    salidas:
    - archivo Markdown Claude Code
    - registro _transmutation.yml
    - diagnostico de fidelidad
  interfaz:
    herramientas: []
    permisos:
      allow: []
      deny: []
  invariantes:
    reglas_duras:
    - "Toda perdida estructural respecto al IR canonico DEBE registrarse en _transmutation.yml; nunca silenciar."
    - "URN del artefacto fuente DEBE preservarse en metadata del output runtime; la transmutacion no reescribe identidad."
    - "Si el vector cae fuera del dominio declarado por claude-code-runtime-extension, abortar antes de emitir output."
---

# Transmute Claude Code

Funtor T_{claude-code} : IR_KORA -> Claude Code. Proyecta un artefacto agentico unified a un archivo `.md` consumible por Claude Code como persona o subagente, preservando composicion e identidad y declarando toda perdida de fidelidad.

## Objetivo

Emitir un archivo Claude Code (`~/.claude/agents/{nombre}.md` o `.claude/agents/{nombre}.md`) a partir de un workspace KORA (`artifacts/agents/{ns}/{nombre}/AGENT.md`). La transmutacion es functorial: preserva composicion y documenta explicitamente perdidas.

## Cuando Usar

- Generar o regenerar un agente Claude Code desde su fuente KORA.
- Validar que un artefacto KORA se proyecta correctamente al runtime target.
- Producir artefactos de distribucion cuando un agente se publica en el runtime.
- Verificar fidelidad de proyeccion (round-trip `ingest` despues de `transmute`).

## Entrada / Salida

### Entrada

- Path al directorio del agente: `artifacts/agents/{ns}/{nombre}/`.
- Modo de proyeccion: `persona` (default) o `subagente`.

### Salida

- Archivo principal: `_BUILD/claude-code/{ns}/{nombre}.md` (o ruta declarada).
- Registro de fidelidad: `_transmutation.yml` con hash IR, target, perdida declarada.

## Workflow

### 1. Leer fuente

1. Leer `AGENT.md` del agente. Parsear YAML frontmatter.
2. Extraer dimensiones `artefacto.{perfil, plan, interfaz, contexto, composicion, invariantes}`.
3. Extraer `extensions.claude_code.*` si existe (fibra runtime-especifica).
4. Leer body Markdown completo para preservar secciones ## directamente portables.

### 2. Compilar frontmatter Claude Code

```yaml
---
name: {nombre, kebab-case sin namespace}
description: {descripcion}
tools: {lista de artefacto.interfaz.herramientas join ", "}
model: {extensions.claude_code.model | default "sonnet"}
memory: {si extensions.claude_code.memory presente}
effort: {extensions.claude_code.effort | "high"}
---
```

Campos opcionales segun disponibilidad:

- `maxTurns` desde `extensions.claude_code.max_turns`.
- `color` desde `extensions.claude_code.color`.
- `model` usa slug short de Claude Code, no el ID largo.

### 3. Compilar body: Identidad

Desde `artefacto.perfil`:

```markdown
Eres **{nombre}** — {descripcion}.

{narrativa del perfil: dominio, disparadores, salidas}

Tono: {tono declarado o inferido del arnes}
```

### 4. Compilar body: Plan (FSM)

Desde `artefacto.plan`:

```markdown
## Workflow

Estado inicial: `{estado_inicial}`. Estado terminal: `{estado_terminal}`.

{para cada estado en plan.estados:}
- **{id}**: {accion}
  - Transiciones: {lista condicion -> destino}
```

### 5. Compilar body: Interfaz y Invariantes

```markdown
## Herramientas

{lista de artefacto.interfaz.herramientas con descripcion breve}

## Invariantes

{lista de artefacto.invariantes.reglas_duras}

{lista de artefacto.invariantes.compromisos_eticos condensados}
```

### 6. Emitir `_transmutation.yml`

```yaml
ir_hash: "{sha256 del AGENT.md fuente}"
target: claude-code
target_mode: {persona|subagente}
output_path: "_BUILD/claude-code/{ns}/{nombre}.md"
transmuted_at: "{YYYY-MM-DD}"
fidelity:
  preserved:
    - nombre, descripcion, plan.estados, interfaz.herramientas
  lost:
    - {lista de campos que no mapean al runtime, con razon}
  partial:
    - {lista de campos proyectados con perdida semantica}
```

### 7. Validar round-trip (opcional)

Invocar `kora ingest --target claude-code --input {output_path}` para recuperar IR del artefacto Claude Code. Comparar con el IR original. Divergencias distintas a las declaradas en `fidelity.lost` son error.

## Matriz de fidelidad por forma material

| Forma material | Fidelidad | Observacion |
|----------------|-----------|-------------|
| `habilidad` | fiel | Proyecta a skill de Claude Code con frontmatter nativo. |
| `subagente` | fiel | Proyecta a `.claude/agents/{nombre}.md`. |
| `agente-propiamente-tal` | fiel | Proyecta como persona con memoria user. |
| `agente-plataforma` | no soportado | Claude Code no soporta Mu=3 ambiental. |

## Recursos

Este skill es autocontenido: no requiere recursos auxiliares. La spec gobernante es `urn:kora:kb:claude-code-runtime-extension`.

## Invariantes

- La transmutacion **DEBE** preservar URN (`_manifest.urn` constante en `fidelity.preserved`).
- `extensions.claude_code` tiene precedencia sobre defaults al compilar frontmatter.
- Si `forma_material` no esta soportada por el runtime, **DEBE** abortar con error claro.
- El artefacto emitido **DEBE** validar con `claude --config` antes de publicarse.

## Salida Esperada

- Un archivo `.md` en `_BUILD/claude-code/{ns}/{nombre}.md`.
- Un archivo `_transmutation.yml` con registro de fidelidad adjunto al workspace fuente.
- Log estructurado con status `ok|degraded|error` y lista de campos preservados / perdidos.
