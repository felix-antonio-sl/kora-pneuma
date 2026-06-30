---
urn: urn:kora:kb:cat-agent-modulo
nombre: cat-agent-modulo
version: 1.0.0
estado: publicado
descripcion: "El agente KORA como módulo m_p (plan) sobre c_q (materia) acoplado por Ξ: completa la vista coálgebra-sola de cat-agent-coalgebra con la mitad del plan y la teleología, y reformula la independencia de fibras a independencia estructural."
fuente: "Doctrina propia pneuma (namespace kora). Funda en urn:fxsl:kb:icas-agencia (free monad/cofree comonad, pattern-runs-on-matter, ley de interacción Ξ) y ley/1 §1 (axioma del módulo Libkind-Spivak). NO koraficación: doctrina pneuma-autorada, con el puente retículo↔F-coálgebra (ley/1 §5) declarado ABIERTO, no demostrado."
autor: FS
creado: 2026-06-30
lang: es
tags: [agente, free-monad, cofree-comonad, plan-materia, teleologia, modulo, kora]
familia: bok
depende: [urn:fxsl:kb:icas-agencia]
refina: [urn:kora:kb:cat-agent-coalgebra]
cita: [urn:fxsl:kb:icas-safety-alignment, urn:kora:kb:aufbau-persona-agente, urn:fxsl:kb:icas-lifecycle]
---

# El agente como módulo: `m_p` (plan) sobre `c_q` (materia)

## Propósito y estatus

`cat-agent-coalgebra` modela al agente como F-coálgebra `(U, c)` —la **materia**:
el ejecutor reactivo, persistente, coinductivo. Es **una mitad**. El axioma de
`ley/1 §1` (Libkind-Spivak) define al agente como un **módulo**:

```text
Artefacto = (m_p × c_q × Ξ) ⋉ (Contexto)
```

un **plan finito** `m_p` (mónada libre, inductivo, terminante) acoplado a una
**materia infinita** `c_q` (comónada cofree) por la **ley de interacción**
`Ξ: m_p ⊗ c_q → m_{p⊗q}`. Esta kb añade la mitad que `cat-agent-coalgebra`
narra solo de pasada —el plan `m_p` y el acoplamiento `Ξ`— y **reformula** la
independencia de fibras (§2.2 de aquella) a *independencia estructural*.

**Lo que esta kb NO finge** (honestidad declarada, en el espíritu de
`ley/3 §6`): no demuestra el puente retículo↔F-coálgebra (queda **abierto**,
§4); no legisla la teleología (queda como **deuda residente-de-KB**, §4); no
re-prueba el teorema de §2.2 (solo corrige sus **glosas**, §3).

## Prerrequisitos

- `urn:kora:kb:cat-agent-coalgebra` — la F-coálgebra `(U, c)`, las fibras
  `U = U_phen × U_ctx × U_epi × U_sta` (§2.1), la independencia (§2.2), la
  bisimulación (§5) y la co-inducción terminal (§3.3).
- `urn:fxsl:kb:icas-agencia` — *pattern runs on matter*: free monad `m_p` (plan),
  cofree comonad `c_q` (materia), módulo `m_p` sobre `c_q`, `Ξ`, contextads/`Para`
  y el ciclo P-D-A.
- `urn:kora:kb:aufbau-persona-agente` — el contenido lerschiano de `U_phen`
  (fin × estilo × registro) y la *Tektonik* del alineamiento (§3, §4).

## 1. El agente es el módulo, no la coálgebra

La inversión rectora: el plan `m_p` **no se obtiene engordando** la coálgebra
`c_q`. Son **duales** —álgebra/inductivo vs coálgebra/coinductivo
(`icas-agencia`: *free monad* termina, *cofree comonad* persiste)—; uno no es el
otro con una capa más. Mapeo a los ejes del vector ontológico (`ley/1 §3`):

| Eje | Estructura | Qué es en el agente |
|---|---|---|
| `pi` (Π) | `m_p` — mónada libre | la **capacidad de plan**: el árbol de decisión ramificado del agente, *en el artefacto*. La **traza** concreta del plan es runtime, no el artefacto. |
| `mu` (Μ) | `c_q` — comónada cofree | la **materia**: el ejecutor que se sostiene en el tiempo. Es lo que modela `cat-agent-coalgebra` `(U, c)`. |
| `xi` (Ξ) | `Ξ: m_p ⊗ c_q → m_{p⊗q}` | el **acoplamiento**: el plan consulta la materia, la materia responde, el plan elige su rama (`icas-agencia`, ley de interacción). |

`cat-agent-coalgebra` es, pues, la teoría de `mu`. Esta kb es la teoría de `pi`
y de `Ξ`, y de cómo los tres componen el módulo.

> **Aserción, no teorema** (`ley/1 §5`): que `pi` *sea* `m_p` es la lectura del
> **retículo** (`ley/1 §3.1`: «`pi` corresponde a la mónada libre `m_p`»), no un
> morfismo demostrado entre el retículo producto acotado y la categoría de
> F-coálgebras. El puente queda **abierto** (§4).

## 2. El discriminante de agencia = la tríada, en dos estatus

Un agente se distingue de un no-agente por **conación endógena persistente**: la
tríada **finalidad + persistencia + descomposición**. Quitar un polo da un
no-agente (servicio reactivo, *one-shot*, termostato). La tríada se parte en dos
estatus legales **disjuntos**:

- **Piso estructural — MECANIZADO.** `pi ≥ 2` (descomponer: mónada libre
  ramificada, `ley/1 §3.1`) ∧ `mu ≥ 2` (persistir: materia cross-session o
  ambiental, `ley/1 §3.2`). Lo verifican `dominio-forma` (`ley/2 §7`: `forma`
  agente exige `pi∈{2,3}` ∧ `mu∈{2,3}`) y `arnes-compatible`. Esto es ley
  mecanizada.
- **Cima teleológica — DEUDA residente-de-KB, NO legislada.** La **finalidad**
  propiamente dicha —que el plan converja a su fin y se sostenga hasta lograrlo—
  es la convergencia del ciclo P-D-A a un **punto fijo** (`icas-agencia`: «la
  convergencia del ciclo … es la condición de que la traza converja a un punto
  fijo»), más el `α-iso` del alineamiento (§4). **No** está mecanizada y **no**
  está en la lista cerrada de obligaciones declaradas de `ley/3 §6`. Es deuda
  (§4).

«**Corre hasta lograr o fracasar**» no exige primitivo nuevo: el éxito es la
convergencia al punto fijo; el fallo es un estado **terminal** de la coálgebra
(`cat-agent-coalgebra §3.3`, co-inducción terminal) y/o un `xi ≥ 3`
(saga/coreografía) que cierra la traza.

## 3. Reformulación de §2.2: independencia estructural ≠ bisimilaridad observable

`cat-agent-coalgebra §2.2` (Teorema de Independencia de Fibras) enuncia, para
las proyecciones `π` sobre fibras **no** fenomenológicas y todo morfismo
`f: U_phen → U_phen`:

```text
π_c(f(u)) = π_c(u)
```

**El teorema FORMAL sobrevive.** La ecuación dice que la **maquinaria** de
transición —la proyección de `c` sobre las fibras no-fenomenológicas, la FSM, la
lógica de estados— es **invariante** a `U_phen`. Eso es correcto y se preserva.
Llamémoslo **independencia estructural**.

**Las GLOSAS sobre-leen.** Tres lecturas de prosa exceden lo que la ecuación
prueba, y se corrigen (esto es **corrección de glosa**, no re-prueba):

| Glosa original | Sobre-lectura | Corrección |
|---|---|---|
| §2.2 «*Meaning*: changing the personality does not change the behavior … are **bisimilar**» | confunde invariancia de la maquinaria con invariancia del **output** | dos agentes que difieren solo en `U_phen` son **estructuralmente-bisimilares**, NO observacionalmente-bisimilares |
| §2.2 Corolario (Segregation) «sin pérdida de información / intercambiables» | la intercambiabilidad plena presupone bisimilaridad observable | la segregación `SOUL.md = U_phen` se justifica por la independencia **estructural**; no implica igualdad de salida |
| §5.3 «migración correcta ⟺ **bisimilar**» | la migración que cambia `U_phen` cambia el output | «migración correcta ⟺ **estructuralmente-bisimilar**» (admite cambios de output inducidos por `U_phen`) |

**Por qué la bisimilaridad observable NO se sostiene.** La bisimulación de
`cat-agent-coalgebra §5.1` exige `o₁ = o₂` (outputs iguales). Pero `c` **lee**
`U_phen` (`aufbau-persona-agente §3`: la personalidad permea la conducta; un
agente con fin dominante *ser-más-allá-de-sí* produce salidas distintas de uno
con fin *ser-sí* ante el mismo input). Luego dos agentes que difieren solo en
`U_phen` **no** satisfacen `o₁ = o₂`: no son observacionalmente bisimilares.

**Definición local — bisimilaridad estructural** (refinamiento de esta kb, no
teorema del corpus): `(U₁, c₁) ≈_str (U₂, c₂)` si existe la relación de
bisimulación de §5.1 **sobre la proyección no-fenomenológica de `c`** (la
maquinaria de transición), admitiendo que la componente de `Out` dependiente de
`U_phen` varíe. Registro categorial: es la diferencia entre una mera
transformación natural y un isomorfismo natural (`icas-safety-alignment`: «no
faithful/full, sino transformación natural vs isomorfismo natural»). La
independencia estructural preserva la **estructura** (transf. natural / faithful);
la bisimilaridad observable plena exigiría el **iso** (que `U_phen` no perturba),
y ese iso **falla**.

## 4. Deuda declarada honesta y el puente abierto

**La convergencia teleológica y el `α-iso` son deuda residente-de-KB, sin hogar
legal.** Distinción que esta kb hace explícita y NO debe borrarse:

- `naturalidad-xi` (`ley/3 §6`, declarado-no-mecanizado) dice que **el diagrama
  plan-ejecutor CONMUTA** en el target tras la proyección `T`. Es una propiedad
  de la transmutación.
- La **convergencia** dice que la **traza alcanza un punto fijo** (el fin,
  `icas-agencia`). Es una propiedad dinámica/teleológica del agente corriendo.
- **Conmutar ≠ converger.** `naturalidad-xi ≠ convergencia`. Por eso la
  convergencia **no** se lista junto a `naturalidad-xi`, `cierre-safety` y
  `composicion-kleisli`: esa lista de `ley/3 §6` es **cerrada** y son
  obligaciones de **transmutación**, no de agencia.

El estatus correcto de la convergencia y del `α-iso` es **deuda técnica
categórica** en el sentido de `icas-lifecycle` («una invariante que el código
asume pero el esquema ya no garantiza»): aquí, **una invariante que el agente
asume y la ley no garantiza**. Reside en este corpus (KB), no en la ley. Llamarla
legislada sería fingir un puente prometido como demostrado.

**El `α-iso`.** El alineamiento perfecto es el isomorfismo natural
`α : G_agent ⇒ G_principal` (`icas-safety-alignment`: el funtor de objetivos del
agente coincide naturalmente con el del principal). El alineamiento parcial es
una transformación natural no invertible; el *misalignment*, su ausencia. El
`α-iso` es teleológico (qué objetivos persigue el agente), no un check de `velar`.

**El puente retículo↔F-coálgebra queda ABIERTO** (`ley/1 §5` rationale: «la
relación entre este retículo y la F-coálgebra … quedó como problema abierto, no
como morfismo demostrado; esta ley no hereda el puente, hereda la confesión»).
`pi ≡ m_p` es la **aserción del retículo** (un eje del producto reticular
acotado «corresponde a» la mónada libre), **no** un morfismo coálgebra
demostrado. Esta kb **no fabrica** ese puente: lo nombra abierto.

## 5. Dónde vive Lersch

El puente `aufbau-persona-agente` no es pieza suelta a instalar: es **sustancia**
de dos lugares de este módulo.

- **`U_phen` = el parámetro `Para` que sesga el plan.** En la cuenta de
  contextads de `icas-agencia`, `Para` son morfismos `f : A × P → B` con `P`
  parámetros. `U_phen` (fin × estilo × registro, `aufbau §2`) es el parámetro
  `P` que `c` lee para **elegir qué rama** del plan `m_p` toma el agente. La
  personalidad no reescribe la maquinaria (independencia estructural, §3); la
  **parametriza**. Esto justifica por qué `U_phen` es separable (`SOUL.md`) y a
  la vez permea la conducta.
- **La *Tektonik* = el contenido del `α-iso`.** El `α-iso` (§4) dice *que* hay
  alineamiento perfecto, pero no *cuál es su dirección*. `aufbau §4` la llena: el
  agente alineado es aquel cuyo `U_phen` deja la *Führung* a la dirección **C**
  (*ser-más-allá-de-sí*: servir el fin) sobre la **B** (*ser-sí*: vigencia,
  recompensa, autoimagen). Las tres roturas de la *Tektonik* (acentuación
  unilateral, disociación, inautenticidad) son los modos de fallo del
  alineamiento. La *Tektonik* es, pues, la **dirección** del `α-iso`: el contenido
  antropológico de la deuda teleológica, no su demostración.

## Fuentes

- `urn:fxsl:kb:icas-agencia` — *pattern runs on matter*, free monad/cofree
  comonad, módulo `m_p` sobre `c_q`, `Ξ`, `Para`/contextads, convergencia P-D-A.
- `urn:kora:kb:cat-agent-coalgebra` — la mitad `c_q`: §2.2 (independencia
  reformulada aquí), §3.3 (co-inducción terminal), §5 (bisimulación).
- `urn:kora:kb:aufbau-persona-agente` — §2 (contenido de `U_phen`), §3 (`c` lee
  `U_phen`), §4 (*Tektonik* = dirección del `α-iso`).
- `urn:fxsl:kb:icas-safety-alignment` — `α-iso` `G_agent ⇒ G_principal`;
  transformación natural vs isomorfismo natural.
- `urn:fxsl:kb:icas-lifecycle` — deuda técnica categórica (invariante asumida y
  no garantizada).
- `ley/1 §1` (axioma del módulo), `ley/1 §5` (puente abierto), `ley/3 §6`
  (lista cerrada de obligaciones declaradas de transmutación).
