---
urn: urn:dev:artefacto:scaffold-repo
nombre: scaffold-repo
version: 2.0.0
estado: activo
descripcion: "Andamia repositorios nuevos con una entrada humana durable en README.md, un contrato operativo nativo y especifico para Codex en AGENTS.md, y CLAUDE.md como import exacto de AGENTS.md salvo una necesidad Claude-especifica real. Usala cuando el operador quiera crear, iniciar o scaffoldear un repositorio, proyecto, corpus, cuaderno de rol o modelo OPM. Distingue cuatro arquetipos: desarrollo, conocimiento, cuaderno de rol y modelamiento. HANDOFF.md es unico, estable y condicional al trabajo material inconcluso; no crea MEMORY.md, continuidades fechadas, bitacoras de sesion ni archivos de sesion."
fuente: "Autorada runtime-first en ~/.claude/skills/scaffold-repo/ el 2026-06-21 (SKILL.md sha256:8d91319442a4232185ece0b28505b8c2d62a47d5b5306b0939bae15bdd12dd2d; assets/ preservados verbatim) y absorbida como fuente canónica en KORA pneuma ese día; no proviene de la bestia. Normalización inicial: assets/ -> referencias/ y frontmatter KORA cerrado. La evolución 1.x incorporó arquetipos, Codex y AGENTS.md autónomo; Git conserva su detalle histórico. v2.0.0 (2026-08-03): adopta la arquitectura documental README humano -> AGENTS Codex repo-specific -> CLAUDE import exacto; reemplaza handoffs fechados por un único HANDOFF.md estable y eliminable; retira MEMORY.md, continuidades fechadas, BITACORA/CHANGELOG obligatorios, archivos de sesión y _archivo/ del scaffold; mueve las variantes por arquetipo a plantillas de AGENTS.md."
autor: FS
creado: 2026-06-21
lang: es
tags: [scaffold, repo, agents-md, claude-md, readme, codex, claude-code, bootstrap, handoff]
vector: [2, 0, 2, 0, 1]
sigma: [1, 1, 2, 1, 1]
arnes: disciplina
forma: habilidad
herramientas: [Read, Write, Bash]
targets: [claude-code, codex]
alcance: usuario
estados: [resolver-parametros, clasificar-destino, escribir-entradas, verificar]
---

# scaffold-repo

Crea el mínimo contrato documental de un repositorio nuevo. Cada superficie tiene
un consumidor y una responsabilidad:

- `README.md` — entrada humana durable: qué es, para quién y cómo orientarse.
- `AGENTS.md` — contrato operativo nativo de Codex, específico del repositorio.
- `CLAUDE.md` — import exacto `@AGENTS.md`; solo diverge ante una necesidad
  Claude-específica real, declarada y mínima.
- `HANDOFF.md` — continuidad excepcional: único, estable y solo mientras exista
  trabajo material inconcluso.

La jerarquía es `global -> host -> repositorio`: cada nivel añade únicamente lo
propio de su alcance y la regla más cercana manda localmente. Git conserva la
narrativa cerrada; el scaffold no crea memoria paralela ni documentación de sesión.

## Cuándo no aplicar

- Un workspace o blueprint de OpenClaw donde `AGENTS.md` define al agente runtime:
  no es un contrato de autoría del repositorio y no se sobreescribe.
- Un directorio derivado, emitido, materializado, archivado o de build: vuelve a su
  fuente autoritativa.
- Un repositorio que ya tiene `AGENTS.md`, `CLAUDE.md` o `README.md`: no los pises.
  Léelos, clasifica su función y modifica solo con una solicitud explícita de
  auditoría o migración.

## Flujo

### 1. Resolver el repositorio

Fija tres datos:

- `nombre` — kebab-case, sin tildes.
- `ubicación` — normalmente `~/projects/{{nombre}}/`; corpus de primer nivel como
  KORA pueden vivir directamente bajo `~`.
- `arquetipo` — `desarrollo`, `conocimiento`, `cuaderno-rol` o `modelamiento`.

Pregunta el arquetipo solo si el contexto no permite inferirlo y la diferencia cambia
materialmente el resultado.

### 2. Clasificar el destino

Antes de escribir:

1. Resuelve el Git root y los contratos globales, de host y de repositorio aplicables.
2. Distingue fuente, derivado, runtime y archivo histórico.
3. Preserva archivos y cambios existentes; no conviertas un consumidor en fuente.
4. Confirma que no estás dentro de un workspace runtime cuyo `AGENTS.md` tenga otra
   semántica.

### 3. Instanciar las entradas

Usa las referencias según el arquetipo:

| Salida | Referencia |
|---|---|
| `README.md` | `referencias/README.md` |
| `AGENTS.md` desarrollo | `referencias/agents-desarrollo.md` |
| `AGENTS.md` conocimiento | `referencias/agents-conocimiento.md` |
| `AGENTS.md` cuaderno de rol | `referencias/agents-cuaderno-rol.md` |
| `AGENTS.md` modelamiento | `referencias/agents-modelamiento.md` |
| `CLAUDE.md` | `referencias/claude-import.md` |
| `.gitignore` | `referencias/gitignore-base` |

Reglas de instancia:

- Sustituye cada `{{placeholder}}`; si falta un dato, usa un pendiente honesto en
  vez de inventarlo.
- Elimina comentarios guía y secciones que aún no apliquen.
- `AGENTS.md` contiene misión, autoridad, arquitectura, verificaciones y límites
  reales del repositorio; no repite instrucciones globales o de host.
- `CLAUDE.md` debe contener exactamente `@AGENTS.md` y un salto de línea final. Solo
  añade una delta cuando Claude necesite realmente una regla que Codex no deba leer;
  explica esa excepción en el diff y conserva `@AGENTS.md` como primera línea.
- Añade al `.gitignore` únicamente residuos del runtime real. `*.tar.gz` y secretos
  básicos permanecen protegidos.

### 4. Continuidad

No crees continuidad por ceremonia.

- Si al cerrar queda trabajo material inconcluso que otra sesión debe retomar, crea o
  actualiza un único `HANDOFF.md` en la raíz.
- El nombre es siempre `HANDOFF.md`: sin fecha, sufijo, copia ni carpeta de sesiones.
- Contiene solo estado actual, pendiente material, riesgos y próxima acción; se
  revalida contra Git y el estado vivo.
- Se edita in-place mientras siga abierto y se elimina cuando ya no queda trabajo
  material inconcluso. Git conserva su historia.
- No crees `MEMORY.md`, `BITACORA.md`, continuidades fechadas, cierres fechados ni
  archivos de sesión. Un `CHANGELOG.md` de producto solo se añade si el producto lo
  necesita explícitamente; no forma parte del scaffold mínimo.

### 5. Verificar y cerrar

El scaffold mínimo contiene `README.md`, `AGENTS.md`, `CLAUDE.md` y `.gitignore`.
Para `modelamiento`, crea además `models/`, `opl/` y `scripts/` cuando correspondan.

Verifica:

1. No quedan placeholders ni comentarios guía.
2. `CLAUDE.md` es byte-equivalente a `@AGENTS.md\n`, salvo delta justificada.
3. `AGENTS.md` declara solo comandos reales; si no existen, usa
   `Verificación automatizada: ABSENT`.
4. No se crearon `MEMORY.md`, handoffs fechados, bitácoras o archivos de sesión.
5. El diff contiene solo el repositorio objetivo y no toca derivados o runtimes.

Si el repositorio llevará Git y aún no está inicializado, ofrece `git init` y primer
commit; no publiques ni crees efectos externos sin autoridad. Reporta qué se creó,
dónde y qué pendiente humano real queda.

## Criterio de diseño

Una fuente por decisión y una entrada por consumidor. `README.md` orienta a personas;
`AGENTS.md` gobierna a Codex; Claude importa el mismo contrato; `HANDOFF.md` solo
transporta trabajo abierto. Todo lo demás debe justificar su existencia por una
necesidad actual.
