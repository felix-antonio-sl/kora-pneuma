# KORA/Ontología — ley pneuma v1.2.0

Estrato 1 de la ley. Define el espacio donde todo artefacto agéntico recibe una
**firma clasificatoria**: los seis ejes PMI × LFS, las leyes que los acoplan y el arnés que
nombra regiones. Este estrato está en **freeze heredado** (constitución §12):
solo correcciones de verdad, sin nuevos ejes ni expansiones doctrinales.

## 1. La hipótesis de diseño

Libkind y Spivak demuestran en la categoría monoidal `Poly` que las mónadas
libres pueden leerse como árboles de decisión terminantes y las comónadas
cofree como patrones de materia que los ejecutan. KORA adopta de ese resultado
la siguiente hipótesis de diseño:

> **Un artefacto agéntico puede clasificarse por su plan, la materia que lo
> sostiene y su régimen de interacción, dentro de un contexto sociotécnico.**

Los ordinales `pi`, `mu` y `xi` no son por sí mismos una mónada, una comónada
ni una transformación natural. La expresión histórica que los combinaba
mediante `×`, `⊗` y `⋉` no definía categorías ni operaciones compatibles y se
retira como fórmula. Construir un puente desde PMI hacia `Poly` queda como
problema abierto, no como axioma heredado.

## 2. La firma clasifica; no individúa

Todo artefacto agéntico DEBE declarar su firma (`vector` + `sigma`, ley/2 §3).
Esa firma ocupa una celda finita del clasificador PMI × LFS. Las reglas son:

1. Misma firma, incluso con el mismo arnés, significa **misma celda
   clasificatoria**. No implica mismo objeto, mismo tipo semántico, misma
   transición, bisimulación ni igualdad de salidas.
2. Firmas distintas significan perfiles distintos **para KORA**. No impiden
   que dos implementaciones sean observacionalmente equivalentes bajo otro
   criterio.
3. El URN da identidad nominal al artefacto (constitución §7 y §9). El cuerpo,
   `conocimiento`, `herramientas`, `estados`, `componible`, arnés y demás
   contenido pueden distinguir habitantes de una misma celda.
4. `U_phen` es una dimensión cualitativa no medida por el retículo, pero no es
   la única fuente posible de individuación.

Contraejemplo vivo: `cat-thinking` e `ifml` comparten arnés, forma, vector y
sigma (`disciplina`, `habilidad`, `[2,0,1,0,1]`,
`[1,1,3,1,0]`), pero tienen URNs, conocimiento, procedimientos y semánticas
distintos. Por tanto la posición no puede ser identidad ni prueba de
bisimulación. **La ley conmensura perfiles; no individúa artefactos.**

## 3. Los seis ejes

La tripleta estructural **PMI** (Π, Μ, Ξ) describe el artefacto *en sí*. La
tripleta contextual **LFS** (Λ, Φ, Σ) lo describe *en relación* con lo
humano, lo organizacional y lo ético. Serialización pneuma:
`vector: [pi, mu, xi, lambda, phi]` + `sigma: [s1, s2, s3, s4, s5]`.

### 3.1 Π — Plan (`pi`, 0..3)

Complejidad operacional del plan. Los nombres categoriales son inspiración
semántica; la coordenada ordinal no construye una mónada.

| Nivel | Nombre | Significado |
|---|---|---|
| 0 | sin plan | sin procedimiento propio |
| 1 | plan lineal | procedimiento secuencial sin ramificación semántica |
| 2 | plan ramificado | árbol de decisión finito |
| 3 | plan con fixed-points | iteración o recursión controlada (interpretadores, meta-razonamiento) |

### 3.2 Μ — Materia (`mu`, 0..3)

Cómo se sostiene el artefacto en el tiempo. La coordenada clasifica persistencia
y entorno; no construye por sí sola una comónada cofree.

| Nivel | Nombre | Significado |
|---|---|---|
| 0 | sin materia propia | el ejecutor externo provee todo el soporte |
| 1 | materia efímera | scratchpad intra-invocación |
| 2 | materia persistente individual | estado cross-session por operador |
| 3 | materia ambiental | estado enlazado a eventos externos (always-on) |

### 3.3 Ξ — Interacción (`xi`, 0..4)

Cómo acopla el plan con la materia y con el mundo. `lente`, `session type` y
`operad` nombran patrones candidatos; solo son formales si el artefacto exhibe
la construcción y sus leyes.

| Nivel | Nombre | Significado |
|---|---|---|
| 0 | sin interacción formal | ejecutor implícito del runtime |
| 1 | interacción atómica | invocación simple con contrato I/O |
| 2 | interacción bidireccional | intercambio de estado o feedback |
| 3 | interacción coreografiada | protocolo multi-fase |
| 4 | interacción composicional | delegación jerárquica dinámica con feedback |

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
| 2 | `xi == 4 ⟹ lambda >= 1` | la delegación jerárquica dinámica supone operar sobre múltiples sub-artefactos |
| 3 | `phi >= 2 ⟹ mu >= 1` | sin estado no hay acoplamiento observable |
| 4 | `sigma[3] >= 2 ⟹ sigma[2] >= 2` | accountability ⟹ transparency: no se atribuye responsabilidad sin explicabilidad |
| 5 | `lambda == 3 ⟹ todas las componentes de sigma >= 2` | un artefacto societal exige compromisos éticos completos |

Índices de `sigma` en base 0 (§3.6). Las cinco se verifican sin excepción en
`velar` bajo el check `leyes-inter-eje`.

## 5. Estructura reticular

1. Cada eje es un retículo (poset con join y meet); el espacio total es
   producto reticular.
2. En la categoría delgada inducida existe una única flecha `v → v'` cuando
   `v ≤ v'`. Si una proyección satisface `P_T(v) ≤ v`, la flecha del orden es
   `P_T(v) → v`, no `v → P_T(v)`.
3. Las cinco leyes de §4 recortan el subretículo acotado de vectores bien
   formados; pertenecer a él es la definición mecanizable de buen-formado.
4. Para cada target, la proyección numérica `P_T` es un funtor y coreflector
   entre categorías delgadas bien delimitadas. La construcción y su prueba
   están en `urn:kora:kb:cat-kora-kernel`; la emisión completa se trata en
   ley/3.

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
| `orquestador` | Π=2-3, Μ=2, Ξ=4, Λ=1-2, Φ=2 | coordina sub-artefactos mediante delegación jerárquica dinámica |
| `servicio` | Π=2, Μ=3, Ξ=3-4, Λ=1-2, Φ=1-2 | agente always-on con materia ambiental |
| `arquetipo` | meta | plantilla de familia de artefactos; no se materializa |

Los vectores típicos son regiones de referencia (clusters, no particiones);
los dominios duros viven en la forma (ley/2 §7).

### 6.1 Doctrina del arnés

Doctrina corregida:

> **Skills y agentes comparten un shape de autoría y un clasificador. La forma
> conserva significado operacional propio; compartir firma no los convierte
> en el mismo objeto.**

Reglas:

1. El par (`arnes`, firma completa) define una **clase de configuración**. No
   define identidad, tipo semántico ni equivalencia conductual (§2).
2. La `forma` (ley/2) es derivada operacional: dado un arnés, se elige por
   modo de invocación (humano directo, por otro agente, always-on) y por
   dominio de proyección compatible. NO es discriminante ontológico
   independiente.
3. La topología física (`artefactos/skills/` vs `artefactos/agentes/`) es
   convención de nombrado, no taxonomía ontológica.
4. `arquetipo` es **meta-arnés**: NO DEBE materializarse en ninguna forma;
   `velar` lo rechaza (`arnes-compatible`, ley/2 §8).

Rationale: un shape común evita duplicar esquema y validadores. No elimina las
diferencias de invocación ni autoriza inferir igualdad entre artefactos; el
arnés y la forma clasifican aspectos distintos de su realización.

## 7. Validación

| Regla | Detalle | Enforcement |
|---|---|---|
| Rangos del vector | `pi` 0..3, `mu` 0..3, `xi` 0..4, `lambda` 0..3, `phi` 0..4; `sigma` 5 × 0..3 | mecanizado (`vector-en-reticulo`) |
| Leyes inter-eje | las cinco de §4 | mecanizado (`leyes-inter-eje`) |
| Vector dentro del dominio de su forma | ley/2 §7 | mecanizado (`dominio-forma`) |
| Par (arnés, forma) legal | ley/2 §8 | mecanizado (`arnes-compatible`) |
| La firma no se usa como identidad ni equivalencia (§2) | revisión semántica + duplicados de firma permitidos | mecanizado parcialmente |
| Cierre de safety estructural | §3.6, ley/3 §6 | declarado |

Sublimado de KORA/Harness-Spec v1.1.1 (con el atlas de arnés de autoria-spec
v2.0.0) el 2026-06-11; ver GENESIS.md.

v1.1.0 (HITL 2026-06-30): §2, §6.1 r1 y §7 intentaron corregir un universal falso —el
vector da identidad de TIPO, no de token; para arneses con `U_phen` mismo
vector NO implica mismo objeto (probado por la colisión `steipete`≡`steve-jobs`
en `[2,2,3,1,2]`)—. **Corrección-de-verdad** bajo freeze (constitución §12.2):
alinea §2 con la identidad-token del URN (constitución §7/§9), importa la
distinción estructural/observable de `cat-agent-coalgebra` §2.2 + `aufbau` §3,
y NO introduce eje ni nivel nuevo. Origen: panel consenso-deliberativo, spec
`docs/superpowers/specs/2026-06-30-sistema-componible-agente-design.md`.

v1.2.0 (2026-07-18): corrección-de-verdad bajo freeze. Una firma es un
clasificador, no identidad de tipo ni prueba de bisimulación; la colisión viva
`cat-thinking`/`ifml` refuta el universal incluso sin `U_phen`. Se restringe
el resultado de Libkind-Spivak a `Poly`, se retiran fórmulas no tipadas y se
formaliza únicamente el subretículo y el coreflector por target en
`urn:kora:kb:cat-kora-kernel`. No se añade eje ni nivel.
