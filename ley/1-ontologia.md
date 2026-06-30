# KORA/Ontología — ley pneuma v1.1.0

Estrato 1 de la ley. Define el espacio donde todo artefacto agéntico **es un
punto**: los seis ejes PMI × LFS, las leyes que los acoplan y el arnés que
nombra regiones. Este estrato está en **freeze heredado** (constitución §12):
solo correcciones de verdad, sin nuevos ejes ni expansiones doctrinales.

## 1. El axioma

El axioma viene de Libkind-Spivak:

> **Un sistema agéntico es la interacción entre un plan finito (mónada libre
> `m_p`) y una materia infinita (comónada cofree `c_q`), modulada por una ley
> de interacción `Ξ: m_p ⊗ c_q → m_{p⊗q}`.**

Esta tripleta es la estructura irreducible. Todo lo demás es variación,
contexto o presentación de la tripleta. Formalmente:

```text
Artefacto = (m_p × c_q × Ξ) ⋉ (Contexto)
```

donde `⋉` denota producto semidirecto: el contexto modula la tripleta, no la
sustituye.

## 2. Identidad es posición — de TIPO

KORA canoniza **ontología, no serialización**. Todo artefacto agéntico DEBE
declarar su posición en el espacio (`vector` + `sigma`, ley/2 §3).

Regla (corregida v1.1.0): dos artefactos con el mismo vector ontológico son
**estructuralmente bisimilares** —misma maquinaria de transición (`c`, F): el
**mismo TIPO**—, aunque sus serializaciones difieran. El alcance de esa
equivalencia depende del arnés:

- Arneses **sin `U_phen` individuante** (`utilidad`, `disciplina`, `delegado`,
  `servicio` no-persona): la bisimilaridad estructural arrastra la observable;
  mismo vector ⟹ **mismo objeto**. Aquí la identidad vive en la posición.
- Arneses **con `U_phen`** (`persona`, `orquestador`, `servicio`-persona): la
  bisimilaridad **observable NO se sigue** —la transición `c` lee `U_phen` y
  permea la salida (`urn:kora:kb:cat-agent-coalgebra` §2.2, reformulado en
  `urn:kora:kb:cat-agent-modulo` §3; `urn:kora:kb:aufbau-persona-agente` §3)—:
  **mismo tipo, token distinto**.

La **individuación cualitativa** de una persona (su carácter) reside en
`U_phen`, fibra **no-coordenada** del vector, materializada en el cuerpo del
artefacto + el KB de persona; la individuación **numérica** la da siempre el
URN (constitución §7, §9). **La ley conmensura tipos; no individúa personas.**
`U_phen` no es coordenada nueva del retículo: es la fibra ya definida
(`cat-agent-modulo` §2) que el vector deliberadamente no mide — una población
cualitativa abierta no cabe en un retículo finito acotado.

## 3. Los seis ejes

La tripleta estructural **PMI** (Π, Μ, Ξ) describe el artefacto *en sí*. La
tripleta contextual **LFS** (Λ, Φ, Σ) lo describe *en relación* con lo
humano, lo organizacional y lo ético. Serialización pneuma:
`vector: [pi, mu, xi, lambda, phi]` + `sigma: [s1, s2, s3, s4, s5]`.

### 3.1 Π — Plan (`pi`, 0..3)

Qué sabe hacer el artefacto. Corresponde a la mónada libre `m_p`.

| Nivel | Nombre | Significado |
|---|---|---|
| 0 | sin plan | función pura `T: C → C` |
| 1 | plan lineal | procedimiento secuencial sin ramificación semántica |
| 2 | plan ramificado | mónada libre bien fundada: árbol de decisión finito |
| 3 | plan con fixed-points | mónada libre con recursión (interpretadores, meta-razonamiento) |

### 3.2 Μ — Materia (`mu`, 0..3)

Cómo se sostiene el artefacto en el tiempo. Corresponde a la comónada cofree
`c_q`.

| Nivel | Nombre | Significado |
|---|---|---|
| 0 | sin materia propia | el ejecutor externo provee todo el soporte |
| 1 | materia efímera | scratchpad intra-invocación (coálgebra con carrier acotado) |
| 2 | materia persistente individual | estado cross-session por operador |
| 3 | materia ambiental | comónada cofree bisimilar con eventos externos (always-on) |

### 3.3 Ξ — Interacción (`xi`, 0..4)

Cómo acopla el plan con la materia y con el mundo.

| Nivel | Nombre | Significado |
|---|---|---|
| 0 | sin interacción formal | ejecutor implícito del runtime |
| 1 | interacción atómica | invocación simple con contrato I/O (lente trivial) |
| 2 | interacción bidireccional | lente polinomial `φ: S·y^S → p` |
| 3 | interacción coreografiada | protocolo multi-fase (session types) |
| 4 | interacción composicional | operad dinámica: delegación jerárquica con feedback |

### 3.4 Λ — Nivel sociotécnico (`lambda`, 0..3)

A qué escala opera el artefacto.

| Nivel | Nombre | Significado |
|---|---|---|
| 0 | individual | scope de un operador |
| 1 | organizacional | equipo, workspace compartido |
| 2 | ecosistema | múltiples organizaciones |
| 3 | sociedad | institución, norma pública |

### 3.5 Φ — Acoplamiento humano (`phi`, 0..4)

Cómo se relaciona con la cognición humana.

| Nivel | Nombre | Significado |
|---|---|---|
| 0 | disjunto | no coordina con humano |
| 1 | instrumental | metáfora de herramienta, supertool |
| 2 | colaborativo | teammate con liderazgo humano |
| 3 | híbrido | cognición distribuida |
| 4 | co-evolutivo | adaptación mutua |

### 3.6 Σ — Vector ético (`sigma`, 5 componentes, cada una 0..3)

Σ NO es escalar: es vector de 5 componentes y DEBE declararse en orden fijo,
`sigma: [safety, fairness, transparency, accountability, sustainability]`.

| Componente | Índice | Significado |
|---|---|---|
| safety | 0 | compromiso de no-daño |
| fairness | 1 | no-discriminación, equidad |
| transparency | 2 | explicabilidad de decisiones |
| accountability | 3 | atribución de responsabilidad |
| sustainability | 4 | impacto ecológico y social |

Un agente sin postura sobre estas cinco dimensiones está **incompleto como
objeto**: la ética es una coordenada de la cosa misma, no política
sobreañadida.

Rationale: pneuma renombra `safety_norm` → `safety`. La distinción heredada
entre safety normativa (esta componente: declarada) y safety estructural
(sub-coálgebra cerrada bajo la dinámica, derivada de Μ y Ξ) se conserva como
concepto: la estructural reaparece en la ley de transmutación como obligación
declarada-no-mecanizada (`cierre-safety`, ley/3 §6), no como eje.

## 4. Las cinco leyes inter-eje

Los ejes **no son todos independientes**. Todo vector agéntico DEBE
satisfacer las cinco leyes; un vector que las viola es **mal-formado** — no
inválido por decreto, sino incoherente consigo mismo.

| # | Ley | Lectura |
|---|---|---|
| 1 | `pi >= 3 ⟹ mu >= 1` | la recursión necesita estado que la sostenga |
| 2 | `xi == 4 ⟹ lambda >= 1` | la operad dinámica supone operar sobre múltiples sub-artefactos |
| 3 | `phi >= 2 ⟹ mu >= 1` | sin estado no hay acoplamiento observable |
| 4 | `sigma[3] >= 2 ⟹ sigma[2] >= 2` | accountability ⟹ transparency: no se atribuye responsabilidad sin explicabilidad |
| 5 | `lambda == 3 ⟹ todas las componentes de sigma >= 2` | un artefacto societal exige compromisos éticos completos |

Índices de `sigma` en base 0 (§3.6). Las cinco se verifican sin excepción en
`velar` bajo el check `leyes-inter-eje`.

## 5. Estructura reticular

1. Cada eje es un retículo (poset con join y meet); el espacio total es
   producto reticular.
2. Morfismos del espacio: **elevación** `v → v'` cuando `v ≤ v'` componente a
   componente; **proyección** `v → v''` cuando `v'' ≤ v`; **transmutación a
   runtime**: funtor `T` (ley/3).
3. Las cinco leyes de §4 recortan el subretículo acotado de vectores bien
   formados; pertenecer a él es la definición mecanizable de buen-formado.

Rationale: formalización heredada de la capa formal de la bestia (lattice
producto acotado). La relación entre este retículo y la F-coálgebra de agente
quedó allá como problema abierto, no como morfismo demostrado; esta ley no
hereda el puente, hereda la confesión.

## 6. El arnés

El arnés (`arnes`) nombra la región del espacio que el artefacto ocupa. Enum
cerrado de 7 valores:

| `arnes` | Vector típico | Qué es |
|---|---|---|
| `utilidad` | Π=1, Μ=0, Ξ=1, Λ=0, Φ=1 | función pura portable |
| `disciplina` | Π=2, Μ=0, Ξ=1-2, Λ=0, Φ=1 | cuerpo de conocimiento procedural |
| `delegado` | Π=2, Μ=1, Ξ=2, Λ=0, Φ=1 | ejecutor delegado con scratchpad intra-invocación |
| `persona` | Π=2-3, Μ=2, Ξ=2-3, Λ=0-1, Φ=2 | agente con identidad y estilo |
| `orquestador` | Π=2-3, Μ=2, Ξ=4, Λ=1-2, Φ=2 | coordina sub-artefactos vía operad dinámica |
| `servicio` | Π=2, Μ=3, Ξ=3-4, Λ=1-2, Φ=1-2 | agente always-on con materia ambiental |
| `arquetipo` | meta | plantilla de familia de artefactos; no se materializa |

Los vectores típicos son regiones de referencia (clusters, no particiones);
los dominios duros viven en la forma (ley/2 §7).

### 6.1 Doctrina del arnés

Doctrina heredada intacta:

> **Skills y agentes NO son ontológicamente categorías distintas. Son
> proyecciones operacionales del mismo objeto agéntico, distinguidas por el
> arnés que ocupan en el espacio PMI × LFS.**

Reglas:

1. La identidad **de tipo** de un artefacto agéntico se define por el par
   (`arnes`, vector completo). Mismo arnés y mismo vector: el mismo **tipo** en
   categorías de realización distintas. Para arneses con `U_phen` (`persona`,
   `orquestador`, `servicio`-persona) esto NO implica el mismo **token**: la
   individuación cualitativa reside en `U_phen` (no-coordenada) y la numérica en
   el URN (§2; constitución §7).
2. La `forma` (ley/2) es derivada operacional: dado un arnés, se elige por
   modo de invocación (humano directo, por otro agente, always-on) y por
   dominio de proyección compatible. NO es discriminante ontológico
   independiente.
3. La topología física (`artefactos/skills/` vs `artefactos/agentes/`) es
   convención de nombrado, no taxonomía ontológica.
4. `arquetipo` es **meta-arnés**: NO DEBE materializarse en ninguna forma;
   `velar` lo rechaza (`arnes-compatible`, ley/2 §8).

Rationale: distinguir habilidad de subagente como categorías paralelas creaba
duplicación ontológica. Un mismo objeto puede ser invocado por humano o por
agente sin que cambie lo que es; el arnés captura el objeto, la forma captura
la materialización.

## 7. Validación

| Regla | Detalle | Enforcement |
|---|---|---|
| Rangos del vector | `pi` 0..3, `mu` 0..3, `xi` 0..4, `lambda` 0..3, `phi` 0..4; `sigma` 5 × 0..3 | mecanizado (`vector-en-reticulo`) |
| Leyes inter-eje | las cinco de §4 | mecanizado (`leyes-inter-eje`) |
| Vector dentro del dominio de su forma | ley/2 §7 | mecanizado (`dominio-forma`) |
| Par (arnés, forma) legal | ley/2 §8 | mecanizado (`arnes-compatible`) |
| Equivalencia **de tipo** por vector (§2; solo arneses sin `U_phen`) | §2 | declarado |
| Cierre de safety estructural | §3.6, ley/3 §6 | declarado |

Sublimado de KORA/Harness-Spec v1.1.1 (con el atlas de arnés de autoria-spec
v2.0.0) el 2026-06-11; ver GENESIS.md.

v1.1.0 (HITL 2026-06-30): §2, §6.1 r1 y §7 corrigen un universal falso —el
vector da identidad de TIPO, no de token; para arneses con `U_phen` mismo
vector NO implica mismo objeto (probado por la colisión `steipete`≡`steve-jobs`
en `[2,2,3,1,2]`)—. **Corrección-de-verdad** bajo freeze (constitución §12.2):
alinea §2 con la identidad-token del URN (constitución §7/§9), importa la
distinción estructural/observable de `cat-agent-coalgebra` §2.2 + `aufbau` §3,
y NO introduce eje ni nivel nuevo. Origen: panel consenso-deliberativo, spec
`docs/superpowers/specs/2026-06-30-sistema-componible-agente-design.md`.
