---
urn: urn:kora:kb:cat-agent-coalgebra
nombre: cat-agent-coalgebra
version: 2.1.1
estado: publicado
descripcion: "Modelo coalgebraico mínimo y bien tipado para agentes con efectos: funtor reactivo en Set, bisimulación y límites de estado, FSM, tools y composición; enlazado al contrato de testigos KORA."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/kora/categorical-foundations/01-agent-coalgebra.md (sha256:138e686d4773e1e0b9f073bfc376bff2a8c14b3d39fedbfb04db83d7f26da242) el 2026-06-12. Reescritura correctiva 2.0.0 (2026-07-18): Rutten, Universal Coalgebra, https://fldit-www.cs.tu-dortmund.de/~peter/Rutten/UniversalCoalgebra.pdf; Beohar et al., Predicate and relation liftings for coalgebras with side effects, https://arxiv.org/abs/2110.09911. v2.1.0 enlaza el contrato operacional de testigos agénticos. v2.1.1 (2026-07-18) corrige el título bibliográfico de Beohar et al.; sin cambio matemático."
autor: FS
creado: 2026-02-26
lang: en
tags: [category-theory, coalgebra, agent-model, effects, formal-layer, kora]
familia: bok
depende: [urn:kora:kb:cat-foundations]
---

# The Agent as an Effectful Coalgebra

## Purpose and epistemic status

This document gives KORA a **minimal, well-typed model** for reactive agents.
It does not claim that every KORA artifact is thereby a coalgebra. Applying the
model requires concrete sets of inputs, outputs and states, a monad, and a
transition function.

`urn:kora:kb:cat-contrato-ingenieria-agentica` turns this boundary into an
operational witness matrix for KORA artifacts: interfaces, wiring,
capabilities, safety and runtime interpretation remain separate evidence.

The previous version conflated:

```text
U -> M((O × U)^I)
```

with a transition that could be applied as `c(u)(i)`. That application is not
well typed: the effect `M` still surrounds the whole function space. It also
called the result a coalgebra in `Kl(M)` without lifting the automaton functor
to that Kleisli category. This version uses the weakest construction that is
already valid in `Set`.

## 1. Minimal effectful model

Let:

- `I` be a set of inputs;
- `O` be a set of outputs;
- `M : Set -> Set` be the endofunctor of a monad;
- `U` be a set of states.

Define the endofunctor:

```text
H(X) = (M(O × X))^I
```

For `h : X -> Y`:

```text
H(h)(k)(i) = M(id_O × h)(k(i)).
```

Functoriality follows from functoriality of `M`, products and exponentials.
An effectful reactive agent is an `H`-coalgebra:

```text
c : U -> H(U)
```

equivalently, by currying:

```text
step : U × I -> M(O × U).
```

Now `c(u)(i)` is well typed. It yields an effectful output/next-state pair.
The familiar deterministic automaton is the special case `M = Id`.

An `H`-coalgebra morphism from `(U,c)` to `(V,d)` is a function `h : U -> V`
such that:

```text
H(h) . c = d . h.
```

This equation, not a shared KORA vector, is what establishes preservation of
the modeled behavior.

## 2. Alternative Kleisli formulation

One may instead seek a coalgebra for `F(X) = (O × X)^I` **inside** `Kl(M)`.
That requires an endofunctor lifting of `F` to `Kl(M)`, commonly obtained from
compatible distributive/lifting data. Such data is not automatic for an
arbitrary monad and has not been specified by KORA.

The types

```text
U -> M(F(U))
U -> (M(O × U))^I
```

are not generally isomorphic: a monad need not commute with exponentiation.
KORA therefore uses the second type as its baseline and treats a Kleisli
coalgebra as a possible refinement under explicit hypotheses.

Choosing `Writer`, powerset or distribution for `M` models logging,
nondeterminism or probability. It does **not** prove that a runtime enforces
security or that an agent cannot mutate configuration. Those are runtime
properties.

## 3. Behavioral equivalence and bisimulation

A coalgebraic bisimulation between `(U,c)` and `(V,d)` can be given by a
relation `R ⊆ U × V` equipped with a coalgebra structure
`r : R -> H(R)` whose projections to `U` and `V` are coalgebra morphisms.

Equivalent relation-lifting presentations require hypotheses on `H` (for
example, suitable weak-pullback preservation). They are not available for
every effect monad without qualification. Likewise:

- a final `H`-coalgebra may or may not exist in the chosen category;
- when it exists, every coalgebra has a unique map into it;
- identifying bisimilarity with equality of final semantics needs the usual
  assumptions for the selected functor.

Consequently:

```text
same KORA signature  -/->  same coalgebra
same KORA signature  -/->  bisimilar
```

An actual bisimulation relation or equality of an established final semantics
is required.

## 4. State decomposition is a model, not independence

KORA may model state as:

```text
U = U_phen × U_ctx × U_epi × U_sta.
```

This product supplies projections and a way to store components. It does not
make the components orthogonal: an arbitrary `c` may read every factor and
make outputs or next states depend on all of them.

Independence of `U_phen`, for example, requires a non-interference equation or
a factorization of `c` that explicitly excludes it from the relevant
observable. No such general equation follows from the product alone. Copying
components into separate files preserves marked bytes, not behavior.

Likewise, dropping personality or operator context for a sub-agent is a
runtime policy. Calling that operation an adjoint requires two categories,
two functors and a natural hom-set bijection (or unit/counit with triangle
identities); KORA has not supplied them.

## 5. Finite-state control

A finite-state machine is initially a labeled directed graph, not a category.
If categorical path semantics is useful, the graph generates a free category:

- objects are control states;
- morphisms are finite transition paths;
- identities are empty paths;
- composition is path concatenation.

An implementation can factor its transition through a finite control-state
set, but this is a design choice to be demonstrated for that implementation.

A retry loop such as:

```text
while not valid(output):
    output = correct(output)
```

is iteration with a validation invariant. It is not, merely by being a loop,
coinduction. It may diverge. Coinduction proves properties of potentially
infinite behavior by exhibiting a bisimulation or a post-fixed invariant for
a specified coalgebra.

## 6. Tools and safety boundaries

Let `allowed ⊆ O` denote outputs that invoke permitted tools. The closure
condition:

```text
for every u and i, support(step(u,i)) ⊆ allowed × U
```

is a meaningful property only after the effect-specific notion of `support`
is defined. It can be guaranteed by construction of `O`, proved about `step`,
or enforced by the runtime. A prompt-level allowlist is a declaration, not a
proof of closure.

Safety can be modeled by a subobject `S ↪ U` closed under transition, but the
closure statement must include which inputs, effects and outputs are allowed.
Preservation across serialization is a separate theorem and is not implied by
the KORA seal.

## 7. Composition

Agents can be composed with typed wiring diagrams only after declaring:

- the interface type of each component;
- the category/operad of wirings;
- an algebra that interprets each wiring as a composite coalgebra;
- compatibility of effects and feedback.

Parallel files, a `componible` edge or a delegation prompt do not supply these
data automatically. They are useful operational declarations, not categorical
composition proofs.

## 8. Status ledger

| Claim | Status |
|---|---|
| `H(X) = (M(O × X))^I` is an endofunctor on `Set` | formal |
| `c : U -> H(U)` is equivalent to `U × I -> M(O × U)` | formal |
| a concrete artifact realizes such a coalgebra | model under supplied data |
| product decomposition of agent state | design model |
| independence of the factors | open until a factorization/non-interference proof is given |
| FSM generates a path category | formal |
| retry is coinduction | false; corrected |
| tool closure and safety closure | policy/property to enforce or prove |
| sub-agent creation is an adjunction | open hypothesis |
| same PMI × LFS signature implies bisimulation | false |

## Primary sources

- J. J. M. M. Rutten, *Universal Coalgebra: a Theory of Systems*:
  https://fldit-www.cs.tu-dortmund.de/~peter/Rutten/UniversalCoalgebra.pdf
- H. Beohar et al., *Predicate and relation liftings for coalgebras with side
  effects: an application in coalgebraic modal logic*:
  https://arxiv.org/abs/2110.09911
- Emily Riehl, *Category Theory in Context*:
  https://emilyriehl.github.io/files/context.pdf
