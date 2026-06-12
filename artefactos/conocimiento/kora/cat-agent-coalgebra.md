---
urn: urn:kora:kb:cat-agent-coalgebra
nombre: cat-agent-coalgebra
version: 1.0.0
estado: publicado
descripcion: "El agente KORA como F-coálgebra: categoría de agentes, funtor de autómata reactivo, descomposición del espacio de estados, morfismo de transición, bisimulación como sustituibilidad y wiring diagrams para composición."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/kora/categorical-foundations/01-agent-coalgebra.md (sha256:138e686d4773e1e0b9f073bfc376bff2a8c14b3d39fedbfb04db83d7f26da242) el 2026-06-12; cuerpo byte-fiel. Fuente original: Barbosa (Coalgebra for Working SE), Spivak (Categorical Systems Theory), KORA agent-spec-md v6.0.0."
autor: FS
creado: 2026-02-26
lang: en
tags: [category-theory, coalgebra, agent-model, formal-layer, kora]
familia: bok
depende: [urn:kora:kb:cat-foundations]
---

# The Agent as F-Coalgebra

## Purpose

This document formalizes the KORA agent model as an F-coalgebra in a Kleisli category. It provides the mathematical foundation that the operational spec (agent-spec-md) translates into rules for LLMs. Every claim here is a theorem or definition; every rule in the spec traces to a property here.

## Prerequisites

All notation and definitions from [00-foundations](urn:kora:kb:cat-foundations).

## 1. The Agent Category

### 1.1 Definition

**Definition (Agent).** An agent is an F-coalgebra (U, c: U → F(U)) in Kl(M) where:

```
F(U) = (Out × U)^In
```

- U is the state space (carrier)
- In is the input type (user messages, tool results, system events)
- Out is the output type (responses, tool calls, delegations)
- M is the effect monad (security constraints, logging, nondeterminism)
- c: U → M((Out × U)^In) is the transition morphism

Given state u ∈ U and input i ∈ In, the agent produces c(u)(i) = m(o, u') where o ∈ Out is the output, u' ∈ U is the next state, and the whole thing is wrapped in M.

### 1.2 The Reactive Automaton Functor

F(U) = (Out × U)^In is the **reactive automaton functor** (Barbosa). It captures the essential pattern: an agent is a system that, given its current state, reacts to an input by producing an output and transitioning to a new state.

**Proposition.** F is an endofunctor on Set. Given h: U → V, F(h): F(U) → F(V) is defined by F(h)(f)(i) = (o, h(u')) where f(i) = (o, u').

**Proof.** F(id) = id and F(g ∘ h) = F(g) ∘ F(h) follow from pointwise application.

### 1.3 The Effect Monad M

The transition c does not land in F(U) directly but in M(F(U)). This places the agent in the Kleisli category Kl(M), where composition of transitions includes the effect.

**Definition (Agent Monad Hierarchy).**

| Level | M | Kl(M) morphisms | Agent semantics |
|-------|---|-----------------|-----------------|
| 0 | Identity | A → B | Deterministic, no constraints |
| 1 | Writer(W) | A → B × W | Every transition logs to trace W |
| 2 | Powerset | A → P(B) | Nondeterministic transitions (multiple valid next states) |
| 3 | Distribution | A → Dist(B) | Probabilistic transitions |

**Theorem (M-Immutability).** M is a parameter of the agent, not a variable. The agent cannot modify its own monad. Formally: the functor Forget_M: Kl(M)-Coalg → Set-Coalg that forgets the monadic structure is faithful but not full.

*Consequence for specs:* config.json (M materialization) is pre-compiled and immutable from the LLM's perspective. The LLM operates inside Kl(M) — it can produce M-wrapped outputs but cannot change M itself.

## 2. State Space Decomposition

### 2.1 Fiber Structure

**Definition.** The state space U decomposes as a product of orthogonal fibers:

```
U = U_phen × U_ctx × U_epi × U_sta
```

| Fiber | Symbol | Content | Bootstrap injection | Sub-agent inheritance |
|-------|--------|---------|--------------------|-----------------------|
| Phenomenological | U_phen | Identity, tone, archetype | Always | Never (dissipated) |
| Operator context | U_ctx | User profile, routines, preferences | Main session only | Never (dissipated) |
| Episodic | U_epi | Memory, session logs | Platform-dependent | Platform-dependent |
| Static | U_sta | Metadata, version, classification | Optional | Optional |

### 2.2 Orthogonality

**Theorem (Fiber Independence).** Let π_i: U → U_i be the projection onto fiber i. For any morphism f: U_phen → U_phen that modifies the phenomenological fiber, the transition morphism c satisfies:

```
π_c(f(u)) = π_c(u) for all projections π onto non-phenomenological fibers
```

*Meaning:* Changing the personality does not change the behavior (transition logic). Two agents that differ only in U_phen are bisimilar.

**Corollary (Segregation Principle).** The decomposition U = Π(fibers) implies that each fiber can be materialized as an independent artifact without loss of information. This is the categorical justification for the file topology: SOUL.md = U_phen, USER.md = U_ctx.

### 2.3 Context Asymmetry in Sub-Agents

**Theorem (Dissipation).** When an agent A instantiates a sub-agent A' via adjunction, the fibers dissipate asymmetrically:

```
Sub-agent state: U' = U_c × U_F (inherits control + interface)
 without U_phen × U_ctx (personality + operator context dissipated)
```

*Proof sketch:* The left adjoint L: Agent → Sub-Agent applies Forget to the non-essential fibers. The right adjoint R: Sub-Agent → Agent reconstructs with default fibers. The counit ε: L(R(A')) → A' is the identity on the control/interface components.

## 3. The Transition Morphism c

### 3.1 FSM as Categorical Graph

**Definition.** The transition morphism c is materialized as a finite state machine (FSM). Categorically, the FSM is a finite category **S** where:
- Objects: states S₁, S₂, ..., S_n
- Morphisms: transitions t: S_i → S_j labeled by conditions

The transition morphism c: U → F(U) factors through **S**:

```
c = eval ∘ classify
 classify: U → Ob(S) (determine current state from U)
 eval: Ob(S) × In → M(Out × U) (evaluate transition in current state)
```

### 3.2 Determinism in M

**Theorem.** For M = Identity, c is deterministic: each (state, input) pair yields exactly one (output, next-state). For M = Powerset, c is nondeterministic but bounded: the set of possible transitions is finite and enumerable.

### 3.3 Co-induction at Terminal States

**Definition (Co-inductive Verification).** At terminal states of the FSM, the agent applies a co-inductive check before producing output. Formally, let S_end be a terminal state. The transition from S_end is:

```
c(u)(i) = verify(output) >>= λ o.
 if valid(o) then return (o, u_final)
 else c(u_corrected)(i) -- retry with corrected state
```

where >>= is Kleisli bind in M and verify is a predicate on outputs.

*Categorical interpretation:* This is coinduction — proving a property (output validity) by showing it's a bisimulation invariant. The agent doesn't terminate until the output satisfies the invariant.

## 4. The Interface Functor F

### 4.1 Closed Algebra

**Definition.** F is a **closed algebra**: the set of tools (actions) available to the agent is finite, declared, and immutable at design-time.

```
F_declared = {tool₁, tool₂, ..., tool_n}
```

**Theorem (Closure).** For all states u ∈ U and inputs i ∈ In, the output o ∈ Out produced by c(u)(i) only invokes tools in F_declared. Formally: the image of c under the tool-projection is contained in F_declared.

*This theorem is extended by the Discovery Presheaf (document 04) to allow runtime discovery while preserving design-time closure.*

### 4.2 Semántics, not Implementation

**Theorem (Abstraction).** F describes WHAT actions exist and their types, not HOW they are implemented. Two agents with identical F but different implementations of the same tools are bisimilar if their observable outputs are indistinguishable.

## 5. Bisimulation

### 5.1 Definition for KORA Agents

**Definition.** Two agents (U₁, c₁) and (U₂, c₂) over the same functor F are **bisimilar** (written U₁ ~ U₂) if there exists a relation R ⊆ U₁ × U₂ such that:

For all (u₁, u₂) ∈ R and all inputs i ∈ In:
- If c₁(u₁)(i) = m₁(o₁, u₁') and c₂(u₂)(i) = m₂(o₂, u₂')
- Then o₁ = o₂ and (u₁', u₂') ∈ R

(within the monad M — equality up to M-equivalence)

### 5.2 Bisimulation as Substitutability

**Theorem.** Bisimilar agents are interchangeable: replacing one with the other in any context (wiring diagram) preserves the behavior of the composite system.

*Proof:* Follows from the universal property of the final coalgebra. Bisimilar agents map to the same element of the final coalgebra, hence produce identical behaviors for all possible input sequences.

### 5.3 Application: Version Migration

**Corollary.** An agent migration (v_old → v_new) is correct iff the two versions are bisimilar. The Agentification functor G (document 03, §5) must preserve bisimulation.

## 6. The Wiring Diagram W

### 6.1 Agents as Boxes

**Definition.** An agent with interface (In, Out) is a box in the category WD. The wiring diagram W specifies how multiple agents compose:

```
W: (In₁, Out₁) × (In₂, Out₂) → (In_system, Out_system)
```

connecting outputs of one agent to inputs of another.

### 6.2 Sub-Agent Adjunction

**Definition.** The instantiation of a sub-agent by a master agent is modeled as an adjunction:

```
Instantiate ⊣ Observe : Agent_sub ⇄ Agent_master
```

- Instantiate (left): creates a sub-agent with inherited c and F, dissipated U_phen and U_ctx
- Observe (right): collects the sub-agent's output and incorporates it into the master's state

**Theorem (Compositional Behavior).** The behavior of the composite system (master + sub-agents) is calculable from:
1. The individual transition morphisms c_i
2. The wiring diagram W
3. Without inspecting the internal states U_i

*This is the compositionality guarantee:* you can reason about the whole from the parts and their connections.

### 6.3 Compositionality of Wiring

**Theorem.** Wiring diagrams compose associatively:

```
W₃ ∘ (W₂ ∘ W₁) = (W₃ ∘ W₂) ∘ W₁
```

and have a monoidal structure (parallel composition):

```
W₁ ⊗ W₂: parallel placement without interaction
```

## 7. The Five Components as Categorical Invariants

**Summary Theorem.** The 5 essential components of a KORA agent are categorically determined:

| Component | Categorical object | Invariant property |
|-----------|-------------------|-------------------|
| c (transition) | Structure map of F-coalgebra | Deterministic in M |
| F (interface) | The functor F in F-coalgebra | Closed algebra (design-time) |
| U (state space) | Carrier of F-coalgebra | Product of orthogonal fibers |
| M (effects) | Monad parametrizing Kl(M) | Immutable from within |
| W (wiring) | Morphism in WD category | Preserves compositionality |

**Theorem (Segregation is Necessary).** The product decomposition U = Π(fibers) and the separation of c, F, M, W into independent components is not a design choice but a categorical necessity: mixing them would violate the functoriality of F, the monad laws of M, or the compositionality of W.

*Proof:* If c contained M-constraints (sandbox rules inside FSM logic), then modifying M would require modifying c, violating the independence of the monad parameter. If U_phen were inside c, then changing personality would change transitions, violating the orthogonality theorem (§2.2). If F were inside c, then the tool algebra would not be closed (tools could appear/disappear based on state).

## Sources

- Barbosa, L. "Coalgebra for the Working Software Engineer" — Chapters 2-4
- Spivak, D. "Categorical Systems Theory" — Chapters 3 (lenses), 7 (wiring diagrams)
- Jacobs, B. "Introduction to Coalgebra" — Chapter 5 (bisimulation)
- Rutten, J. "Universal Coalgebra" — coinduction principle
