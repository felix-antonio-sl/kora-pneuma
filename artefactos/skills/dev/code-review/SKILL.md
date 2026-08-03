---
urn: urn:dev:artefacto:code-review
nombre: code-review
version: 1.0.0
estado: activo
descripcion: "Revisa de forma read-only un cambio desde un punto fijo en dos ejes independientes: Standards, contra los estandares locales y un baseline auxiliar de smells, y Spec, contra la especificacion de origen."
fuente: "Reescritura KORA de mattpocock/skills/skills/engineering/code-review/SKILL.md; upstream commit: 2ab958093e83e0ec752e6c1c5932da465bf23e0c; sha256:6a65cc61114f96db07ec41e3920e67c9c5bf70dd6e0901eb9460ebcb2bdc209f; licencia MIT: referencias/mattpocock-skills-MIT.txt"
autor: FS
creado: 2026-08-03
lang: es
tags: [dev, code-review, standards, spec, read-only]
vector: [2, 0, 2, 0, 1]
sigma: [2, 1, 3, 2, 1]
arnes: disciplina
forma: habilidad
herramientas: [Read, Glob, Grep, Bash]
targets: [codex]
estados: [fijar-punto, localizar-fuentes, revisar-standards, revisar-spec, validar-citas, unir-recibos]
---

# code-review

## Finalidad y frontera

Revisar el delta entre `HEAD` y un punto fijo declarado, manteniendo dos
paquetes independientes:

- **Standards**: conformidad con las reglas documentadas del repositorio y
  los smells del baseline auxiliar inspirado en Fowler.
- **Spec**: correspondencia con la issue, PRD o especificación que originó el
  cambio.

La revisión es read-only: leer, buscar y ejecutar comandos de inspección no
modifica el árbol, no instala nada y no publica resultados. El estándar local
documentado prevalece sobre el baseline; un smell siempre es un juicio
etiquetado, nunca una violación dura, y se omite lo que ya impone una
herramienta.

La skill no es un agente ni un suborquestador. Steipete es la central: crea dos
sesiones o `agent threads` Fugaz nuevos y aislados, uno por eje, y hace el
`join` de sus recibos. Las sesiones son de un solo nivel: no se coordinan
lateralmente, no comparten continuidad implícita y no crean descendencia. No
fijar nombres de modelo ni niveles de esfuerzo; esa selección pertenece al
runtime.

## Contrato de las sesiones

Steipete entrega a cada sesión un `I_task` completo, mapeado así:

| Campo | Contenido común |
|---|---|
| `objective` | revisar solo el eje asignado en el cambio desde el punto fijo |
| `workspace` | raíz exacta del repositorio o worktree |
| `candidate` | ref resuelta, `HEAD`, comando triple-dot y lista de commits |
| `context` | punto fijo y `spec_source` opcional entregados por la central |
| `owned_scope` | paquete de análisis del eje; ninguna escritura |
| `acceptance` | hallazgos trazables, citas verificadas y conteo por eje |
| `authority` | read-only; sin editar, instalar, commit, push ni efectos externos |
| `forbidden_scope` | el otro eje, coordinación lateral y delegación descendiente |
| `constraints` | separar Standards/Spec, preservar estados de evidencia y no rerankear |

Cada sesión devuelve un `O_task` individual con `status` `COMPLETE`, `PARTIAL`
o `BLOCKED`, además de `candidate`, `changes`, `evidence`, `limits`,
`blocker` y `assumptions`. `evidence` usa exactamente `PASS`, `FAIL`,
`ABSENT` o `NOT_RUN`. El recibo debe incluir la evidencia de los comandos, sus
límites y las citas de cada hallazgo; en read-only `changes` es `[]`.

## Protocolo común

### 1. Fijar el candidato

Exigir un punto fijo proporcionado por el operador. Resolverlo antes de
analizar:

```text
git rev-parse --verify <fixed-point>^{commit}
git rev-parse --verify HEAD^{commit}
git diff <fixed-commit>...<head-commit>
git log <fixed-commit>..<head-commit> --oneline
```

Capturar una sola vez ambos commits resueltos, el diff triple-dot y la lista de
commits, y usar esos hashes inmutables en las consultas posteriores. Si alguna
ref no resuelve, cerrar ambos paquetes con `FAIL` y `BLOCKED` antes de crear
hallazgos. Si el diff es vacío, cerrar el análisis con `FAIL` y `BLOCKED`; no
inventar una revisión sobre ausencia de cambios. Ligar todo el recibo a ambos
commits resueltos y al estado vivo observado.

### 2. Localizar las fuentes

Buscar la especificación de origen en este orden:

1. la ruta o referencia exacta `context.spec_source` entregada por el operador
   o la central;
2. referencias a issues o PRs en los mensajes de commit, si la fuente está
   disponible en el alcance read-only;
3. un archivo pertinente bajo `docs/`, `specs/` o `.scratch/`.

Si se declaró `context.spec_source` y no resuelve o es ambiguo, devolver el
paquete **Spec** como `FAIL` y `BLOCKED`; no sustituir silenciosamente la fuente
autoritaria por una inferida. Si no se declaró una fuente y ninguna alternativa
existe, no preguntar ni rellenar el hueco por inferencia: devolver **Spec** como
`ABSENT`, sin hallazgos, y conservar ese estado en el `O_task`. Buscar para
**Standards** solo la documentación aplicable del repositorio (`AGENTS.md`,
`CONTRIBUTING.md`, `CODING_STANDARDS.md` y equivalentes locales), sin tratar
guías no aplicables como norma.

### 3. Ejecutar el eje Standards

Leer las fuentes locales aplicables y, condicionalmente, cargar
`referencias/smell-baseline.md` cuando se evalúen smells. Para cada archivo o
hunk relevante devolver por separado:

- incumplimiento duro de una regla local, citando archivo y regla;
- smell del baseline, citando el hunk y marcándolo como juicio heurístico;
- `PASS` cuando no haya hallazgo sustentable, o `NOT_RUN` cuando falte una
  comprobación necesaria.

Una regla local que acepta expresamente una forma suprime el smell del
baseline en conflicto. No llamar violación a un smell ni corregirlo durante
la revisión.

### 4. Ejecutar el eje Spec

Con una spec disponible, informar por separado: requisito ausente o parcial,
comportamiento no solicitado (scope creep) y requisito aparentemente cubierto
pero implementado de forma incorrecta. Cada hallazgo debe citar la spec y el
hunk del cambio. Sin spec, conservar `Spec: ABSENT`; no convertir su ausencia
en `PASS`, `FAIL` ni en una opinión sobre el código.

### 5. Validar citas y revalidar el candidato

Antes de emitir cada recibo, resolver `HEAD` otra vez y compararlo con
`<head-commit>`. Si cambió, descartar los dos paquetes y devolverlos como
`BLOCKED` con `candidate-mismatch`; no unir hallazgos de estados distintos.
Comprobar cada path, línea o hunk del cambio contra el árbol Git del commit
resuelto, no contra una copia mutable del working tree. Calcular al leer y
revalidar al cerrar el hash de cada fuente local de Standards o Spec que no
pertenezca a ese árbol; si cambia, bloquear únicamente el paquete que depende
de ella.

Cada cita restante debe existir y sostener el hallazgo, y la fuente de Spec
debe seguir siendo exactamente la que se leyó. Una cita ausente, ambigua o
stale se retira del hallazgo o queda como `NOT_RUN`; nunca se fabrica una línea
ni se cita el estado memorizado. Las citas no convierten una observación en
autorización, aprobación humana ni prueba de comportamiento fuera del diff.

## Join y salida

Steipete integra los dos recibos sin mezclar sus pruebas, sin fusionar
hallazgos y sin rerankearlos entre ejes. La salida conserva dos secciones,
`Standards` y `Spec`, en ese orden o en el orden acordado por la central.
Terminar cada eje con su propio conteo y su propio peor hallazgo según impacto
en ese eje; si no hay hallazgo, decirlo. Si Spec está ausente, informar
`count: ABSENT` y `worst: ABSENT`. No elegir un ganador global ni producir una
clasificación única entre Standards y Spec; sin ganador global.

El recibo final identifica el candidato exacto revisado, mantiene los estados
`PASS`/`FAIL`/`ABSENT`/`NOT_RUN`, enumera los límites de la evidencia y deja
claro que el resultado es una revisión read-only, no un cambio aplicado.
