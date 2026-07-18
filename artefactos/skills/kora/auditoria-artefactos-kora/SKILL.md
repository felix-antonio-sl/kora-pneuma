---
urn: urn:kora:artefacto:auditoria-artefactos-kora
nombre: auditoria-artefactos-kora
version: 1.2.0
estado: activo
descripcion: "Evalua, decide y actua sobre el DESTINO de agentes y skills frente a kora-pneuma: tres pilares (formalidad kora, calidad funcional, valor en uso real), cuatro veredictos (migrar/descartar/reubicar/conservar-externo), verificacion adversarial y ejecucion con gate. Usar al auditar el ecosistema agentico, decidir que conservar/descartar, o reconciliar artefactos no-controlados con el corpus."
fuente: "Autorada nueva en KORA pneuma el 2026-06-22. Destila el metodo ejecutado en la auditoria del ecosistema ~/.claude: 3 pilares + 4 veredictos + verificacion adversarial + convergencia con velar. v1.1.0 (2026-07-12): generaliza el censo y REUBICAR a Codex/OpenCode. v1.2.0 (2026-07-18): corrige el alcance del sello; certifica procedencia, integridad y congruencia, no teoremas semanticos."
autor: FS
creado: 2026-06-22
lang: es
tags: [kora, auditoria, artefactos, agentes, skills, migrar-o-omitir, evaluacion, gobernanza, lifecycle, veredicto]
vector: [2, 0, 1, 0, 1]
sigma: [2, 1, 3, 2, 1]
arnes: disciplina
forma: habilidad
herramientas: [Read, Grep, Glob, Write, Edit, Bash]
targets: [claude-code, codex, opencode]
alcance: ambos
estados: [encuadrar, evaluar-pilares, detectar-redundancia, verificar-adversarial, dictaminar, ejecutar-con-gate]
componible: [urn:kora:artefacto:consenso-deliberativo, urn:kora:artefacto:cat-thinking]
---

# auditoria-artefactos-kora

## Propósito

Dota a un agente del método para **evaluar, decidir y actuar sobre el destino**
de artefactos agénticos (agentes y skills) frente a kora-pneuma. No autora
artefactos (eso es autoría con juicio) ni vela su forma (eso lo mecaniza
`kora.py velar`): **decide qué hacer con un artefacto que ya existe** —migrarlo,
descartarlo, reubicarlo o conservarlo fuera del régimen— sobre tres pilares,
con evidencia y verificación adversarial, y ejecuta el veredicto bajo gate.

Llena el hueco entre lo mecanizado y lo deliberativo: `velar` responde *¿es
válida la forma?*; esta skill responde *¿vale la pena, es redundante, dónde
pertenece, y qué se hace al respecto?*

## Cuándo usar

- auditar el ecosistema agéntico de un runtime (`~/.claude`, `~/.codex`,
  `~/.agents`, `~/.config/opencode`) contra el corpus pneuma.
- decidir qué conservar, descartar por redundancia/obsolescencia, o migrar.
- reconciliar artefactos no-controlados (transmitidos desde la bestia, nativos, o en zona pre-categorial) con el régimen single-source.
- dictaminar el destino de un artefacto dudoso antes de invertir esfuerzo en él.

## Cuándo NO usar

- **autorar** un agente/skill nuevo o reescribir uno: es autoría con juicio, no evaluación de destino.
- **verificar forma** (frontmatter, vector en dominio, referencias): eso lo mecaniza `kora.py velar` — esta skill lo USA como red, no lo reemplaza.
- **koraficar conocimiento** (producir KB desde una fuente): es otro contrato (ley/4).

## Tipología de procedencia (determina cómo se juzga la formalidad)

Antes de evaluar, clasificar de dónde viene el artefacto — cambia qué significa
"formalidad kora":

| Clase | Qué es | Cómo se juzga la formalidad |
|---|---|---|
| **controlado-pneuma** | fuente en `artefactos/` del corpus | shape ley/2 directo |
| **bestia** | `Source URN` KORA, fuente en la encarnación congelada (~/kora), no en pneuma | evaluar la FUENTE bestia contra ley/2; candidato migrar-o-omitir |
| **taller / pre-categorial** | fuente en `_TALLER`/scriptorium/INBOX, sin URN canónico | no canonizado; juzgar valor antes que forma |
| **nativo (no-KORA)** | sin `Source URN`, del ecosistema del runtime | formalidad = conformidad con el shape del runtime, no con ley/2 |

Regla clave: un artefacto en un runtime (`~/.claude`) es una **emisión**, no una
fuente. No se juzga "le falta `vector`" — el vector vive en la fuente. Se evalúa
la fuente; si no la hay en pneuma, ese hecho ES el hallazgo de formalidad.

## Los tres pilares (puntuar 0-5 con evidencia citada)

1. **Formalidad kora** — ¿la fuente cumple el shape de autoría ley/2 (frontmatter
   plano cerrado; vector dentro del dominio de su forma §7; arnés×forma §8; cinco
   leyes inter-eje §4; URN/zona §6)? ¿Su doctrina/Knowledge Contract está vigente
   (`ley/0..4`) o **desalineada** (cita specs bestia —md-spec, autoria-spec,
   knowledge-spec, harness-spec, gobernanza— ya sublimadas)? ¿El sello de
   procedencia, integridad y congruencia está presente y fresco? El sello no
   prueba naturalidad, safety ni equivalencia semántica.
2. **Calidad funcional** — ¿el cuerpo es sólido, operable, sin errores? ¿La
   descripción dispara bien? ¿Herramientas mínimas y justificadas? ¿Estructura
   recuperable (headings/tablas), sin grasa? ¿Scripts/referencias funcionan?
   ¿Contratos de entrada/salida observables?
3. **Valor en uso real** — ¿Utilidad práctica tangible HOY para el operador?
   ¿**Redundante** con un artefacto pneuma vigente (cruzar contra el censo:
   `find artefactos/`, grep de propósito — verificar solapamiento real, no
   nominal)? ¿Obsoleto (proyecto muerto, doctrina vieja, runtime no realizado)?
   ¿Mal-ubicado (repo-local instalado a global)?

Sin evidencia verificada (path:línea, cita textual, censo), bajar la confianza —
nunca afirmar un veredicto de memoria.

## Los cuatro veredictos

| Veredicto | Condición | Acción |
|---|---|---|
| **MIGRAR** | valor real + NO redundante + fuente sana o reparable | sublimar a pneuma (shape ley/2, doctrina reanclada a ley/0..4, vector corregido si está fuera de dominio); transmutar a los runtimes |
| **DESCARTAR** | redundante con pneuma vigente, U obsoleto, U sin valor | retirar la emisión del runtime; NO migrar; la fuente bestia queda congelada in situ (respaldo reversible) |
| **REUBICAR** | repo-local instalado por error a nivel global | mover a la ruta de proyecto del runtime (`.claude/`, `.codex/`, `.agents/` o `.opencode/`); no canonizar en pneuma |
| **CONSERVAR-EXTERNO** | nativo legítimo del ecosistema del runtime, no-KORA | dejar como está, fuera del régimen pneuma |

Migrar = **reescribir** (forma anidada→plana, reanclar doctrina, corregir vector,
omitir referencias a descartados), no copiar. Descartar por redundancia exige
solapamiento de propósito **verificado**, no inferido.

## Workflow

### encuadrar
Censar el universo a auditar **contra el filesystem** (no contra un reporte
previo). Cruzar por set-difference contra el corpus pneuma para separar
controlados de no-controlados. Clasificar la procedencia (tabla arriba) de cada
no-controlado. Confirmar paths y existencia antes de nombrar nada.

### evaluar-pilares
Por artefacto, leer la emisión y (si existe) su fuente. Puntuar los tres pilares
0-5 con evidencia citada. Paralelizar: un evaluador por artefacto.

### detectar-redundancia
Cruzar el propósito contra el índice pneuma vigente. Confirmar solapamiento real
con `Grep`/`Glob` sobre `artefactos/`. Distinguir redundancia con artefacto
vigente (gatilla DESCARTAR) de complementariedad (no la gatilla).

### verificar-adversarial
Cada veredicto pasa por un verificador de **contexto limpio** cuyo trabajo es
REFUTARLO, no ratificarlo (default escéptico; ver `consenso-deliberativo`).
Atacar especialmente: DESCARTAR-por-redundancia (¿el artefacto pneuma cubre TODA
la función o se perdería algo único?) y MIGRAR (¿de verdad aporta valor no
cubierto?). El veredicto sólo sobrevive si resiste el intento de refutación.

### dictaminar
Emitir, por artefacto: veredicto + acción concreta + scores + redundancia +
confianza. Agrupar por veredicto. Nombrar los hallazgos transversales (patrones
que cruzan varios artefactos).

### ejecutar-con-gate
Las acciones destructivas (DESCARTAR = borrar del runtime; REUBICAR = mover)
exigen, ANTES de tocar: backup, confirmación de reversibilidad (¿la fuente queda
como respaldo?), y `diff` contra el destino si se sobreescribe. Las constructivas
(MIGRAR = escribir en pneuma) cierran con `velar` como red, luego `transmutar` a
cada runtime. Tras cada lote, re-`velar`.

## Reglas duras

1. **Verificar contra estado, no contra reporte.** El censo y los conteos se
   leen del filesystem, no del handoff ni del reporte de un subagente.
2. **`velar` es la red de convergencia.** Garantiza la FORMA, no la verdad del
   contenido: tras escribir migraciones, `velar --estricto` caza frontmatter
   inválido y referencias que no resuelven. Re-velar hasta 13/13.
3. **Frontera destructiva con red.** Nunca borrar/sobreescribir sin backup +
   reversibilidad confirmada; mirar el destino antes de actuar.
4. **Sin evidencia no hay veredicto.** Cada afirmación anclada a lo leído; lo no
   verificado se declara como tal y baja la confianza.
5. **Migrar es reescribir.** Toda fuente bestia usa shape anidado prohibido por
   ley/2 y cita specs sublimadas: aplanar el frontmatter y reanclar a ley/0..4,
   no copiar.
6. **El verificador refuta, no ratifica.** Un veredicto sin intento de
   refutación de contexto limpio no está cerrado.

## Composición

- `urn:kora:artefacto:consenso-deliberativo` — para la fase `verificar-adversarial`: panel de refutación crítica cuando un veredicto consecuente (descarte masivo, migración costosa) exige más de un escéptico.
- `urn:kora:artefacto:cat-thinking` — para el análisis estructural de redundancia y composición (qué artefacto compone/subsume a cuál) cuando el solapamiento no es evidente.

## Salidas

- censo clasificado (controlado / bestia / taller / nativo) del universo auditado.
- por artefacto: scores de los tres pilares con evidencia, redundancia, veredicto verificado, acción concreta, confianza.
- hallazgos transversales (patrones que cruzan artefactos).
- tras ejecución: estado verificado contra filesystem + `velar` 13/13.
