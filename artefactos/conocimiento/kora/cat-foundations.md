---
urn: urn:kora:kb:cat-foundations
nombre: cat-foundations
version: 1.1.0
estado: publicado
descripcion: "Fundamentos matemáticos de la capa formal de KORA: categorías, funtores, transformaciones naturales, adjunciones, mónadas, coálgebras y construcciones universales."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/kora/categorical-foundations/00-foundations.md (sha256:d5999f525ff2298043cb59d459429a8fe4ac173951ea9d944f24fc41c8b3ba71) el 2026-06-12. Corrección 1.1.0 (2026-07-18) contrastada con Riehl, Category Theory in Context, https://emilyriehl.github.io/files/context.pdf, y Rutten, Universal Coalgebra, https://fldit-www.cs.tu-dortmund.de/~peter/Rutten/UniversalCoalgebra.pdf."
autor: FS
creado: 2026-02-26
lang: en
tags: [category-theory, foundations, formal-layer, kora]
familia: bok
---

# Categorical Foundations for KORA

## Purpose

This document establishes reference prerequisites for the KORA formal layer.
It does not make downstream analogies formal merely by supplying vocabulary.
Each application must still define its categories, morphisms and laws.

## Notation Convention

Throughout this formal layer:
- Objects are denoted by capital letters: A, B, C
- Morphisms by lowercase: f, g, h
- Functors by capital: F, G, T
- Natural transformations by Greek: α, β, η, ε
- Categories by bold or calligraphic: **C**, **D**, Set
- Monads by M
- Composition by ∘ (right-to-left) or ; (left-to-right, diagrammatic)

## 1. Category

**Definition.** A category **C** consists of:
- A collection Ob(**C**) of objects
- For each pair A, B ∈ Ob(**C**), a set Hom(A, B) of morphisms
- For each A, an identity morphism id_A: A → A
- A composition operation ∘: Hom(B, C) × Hom(A, B) → Hom(A, C)

satisfying:
- Associativity: h ∘ (g ∘ f) = (h ∘ g) ∘ f
- Identity: f ∘ id_A = f = id_B ∘ f

**Key instances in KORA:**
- Set: objects = sets, morphisms = functions
- Cat: objects = small categories, morphisms = functors
- Any poset `P` induces a thin category whose objects are elements of `P` and
  with one morphism `x -> y` exactly when `x <= y`
- **Pos**: objects = posets, morphisms = monotone maps

## 2. Functor

**Definition.** A functor F: **C** → **D** assigns:
- To each object A ∈ **C**, an object F(A) ∈ **D**
- To each morphism f: A → B in **C**, a morphism F(f): F(A) → F(B) in **D**

preserving:
- Identity: F(id_A) = id_{F(A)}
- Composition: F(g ∘ f) = F(g) ∘ F(f)

**Endofunctor.** A functor F: **C** → **C** (same source and target category).

**Contravariant functor.** F: **C**^op → **D**. Reverses morphism direction: if f: A → B then F(f): F(B) → F(A).

## 3. Natural Transformation

**Definition.** Given functors F, G: **C** → **D**, a natural transformation α: F ⇒ G assigns to each object A ∈ **C** a morphism α_A: F(A) → G(A) in **D** such that for every f: A → B:

```
 F(f)
 F(A) -----→ F(B)
 | |
 | α_A | α_B
 ↓ ↓
 G(A) -----→ G(B)
 G(f)
```

commutes: α_B ∘ F(f) = G(f) ∘ α_A.

**Natural isomorphism.** α where every α_A is an isomorphism.

## 4. Adjunction

**Definition.** An adjunction L ⊣ R between categories **C** and **D** consists of:
- Functors L: **C** → **D** (left adjoint) and R: **D** → **C** (right adjoint)
- Unit η: Id_**C** ⇒ R ∘ L (natural transformation)
- Counit ε: L ∘ R ⇒ Id_**D** (natural transformation)

satisfying the triangle identities:
- (ε_L) ∘ (L η) = id_L
- (R ε) ∘ (η_R) = id_R

**Equivalent characterization.** Bijection natural in A, B:
Hom_**D**(L(A), B) ≅ Hom_**C**(A, R(B))

**Properties of interest:**
- η iso ⟹ L is full and faithful
- ε iso ⟹ R is full and faithful
- η iso and ε iso ⟹ equivalence of categories

## 5. Monad

**Definition.** A monad on **C** is a triple (M, η, μ) where:
- M: **C** → **C** is an endofunctor
- η: Id ⇒ M is the unit (embeds pure values)
- μ: M ∘ M ⇒ M is the multiplication (flattens nested effects)

satisfying:
- μ ∘ M(μ) = μ ∘ μ_M (associativity)
- μ ∘ η_M = id = μ ∘ M(η) (unit laws)

**Kleisli category.** Kl(M) has:
- Same objects as **C**
- Morphisms A → B in Kl(M) are morphisms A → M(B) in **C**
- Composition: g ∘_Kl f = μ_C ∘ M(g) ∘ f (Kleisli composition, denoted >=>)

**Key monads in KORA:**

| Monad | M(A) | Effect | Agent meaning |
|-------|------|--------|---------------|
| Identity | A | None | Pure transitions; sandboxing is orthogonal |
| Writer W | A × W | Logging | Audit trail on every transition |
| Powerset P | P(A) | Nondeterminism | Multiple valid next states |
| Distribution D | Dist(A) | Probability | Stochastic sampling |

## 6. Coalgebra

**Definition.** Given an endofunctor F: **C** → **C**, an F-coalgebra is a pair (U, c) where:
- U ∈ Ob(**C**) is the carrier (state space)
- c: U → F(U) is the structure map (transition morphism)

**F-coalgebra morphism.** Given (U, c) and (V, d), a morphism h: U → V such that F(h) ∘ c = d ∘ h:

```
 c
 U ------→ F(U)
 | |
 | h | F(h)
 ↓ ↓
 V ------→ F(V)
 d
```

**Bisimulation.** A relation R ⊆ U × V for which there exists a coalgebra
structure on R making both projections coalgebra morphisms. Equivalent
relation-lifting characterizations require suitable hypotheses on F.

**Final coalgebra.** A terminal object in the category of F-coalgebras, when
one exists. It receives a unique morphism from any coalgebra. Under the usual
conditions on F, bisimilar states have equal final semantics; the converse
also needs the relevant behavioral-equivalence hypotheses.

**Coinduction principle.** To prove two states behaviorally equivalent, it is
often enough to exhibit a bisimulation containing them. A validation retry
loop is not by itself coinduction.

## 7. Lens

**Definition.** A lens between state spaces S and T is a pair:
- get: S → T (expose the view)
- put: S × T → S (update the state)

satisfying:
- GetPut: put(s, get(s)) = s
- PutGet: get(put(s, t)) = t
- PutPut: put(put(s, t₁), t₂) = put(s, t₂)

**Effectful variants.** Replacing `put` by `S × T -> M(S)` gives a candidate
effectful update type. The appropriate lens laws and composition depend on the
chosen effectful-lens framework and compatibility with `M`; the pure laws do
not transfer merely by changing the codomain.

**Composition.** Lenses compose:
- get_{l₂ ∘ l₁} = get_{l₂} ∘ get_{l₁}
- put_{l₂ ∘ l₁}(s, c) = put_{l₁}(s, put_{l₂}(get_{l₁}(s), c))

## 8. Fiber Product and Coproduct

**Product.** A × B with projections π₁: A×B → A, π₂: A×B → B satisfying the universal property: for any C with f: C → A and g: C → B, exists unique h: C → A×B.

**Coproduct.** A + B with injections ι₁: A → A+B, ι₂: B → A+B satisfying the dual universal property.

**Pushout.** Given `f: C -> A` and `g: C -> B`, a pushout is a cocone
`A -> P <- B` universal among cocones satisfying compatibility over `C`.
In `Set`, it can be constructed from the disjoint union `A+B` by the
equivalence relation generated by `f(c) ~ g(c)`. The elementwise quotient is
not the definition in an arbitrary category.

## 9. Presheaf

**Definition.** A presheaf on **C** is a functor P: **C**^op → Set.

**Yoneda embedding.** y: **C** → [**C**^op, Set] defined by y(A) = Hom(−, A). Fully faithful (Yoneda lemma): Nat(y(A), P) ≅ P(A).

**Interpretation.** A presheaf assigns to each object a "set of things visible from that object" and to each morphism a "restriction map." Contravariance means: a morphism f: A → B induces P(f): P(B) → P(A) — moving "toward" B restricts what's visible.

## 10. 2-Category

**Definition.** A 2-category **K** consists of:
- 0-cells (objects): A, B, C, ...
- 1-cells (morphisms between objects): f, g: A → B
- 2-cells (morphisms between morphisms): α: f ⇒ g

with two composition operations:
- Horizontal composition of 1-cells: g ∘ f (as in a category)
- Vertical composition of 2-cells: β • α (composing transformations)
- Horizontal composition of 2-cells: β ∗ α (whiskering)

satisfying the **interchange law**: (β' • α') ∗ (β • α) = (β' ∗ β) • (α' ∗ α).

**Examples:**
- **Cat**: 0-cells = categories, 1-cells = functors, 2-cells = natural transformations
- **Pos**: 0-cells = posets, 1-cells = monotone maps, 2-cells = pointwise ≤

## 11. Free Construction

**Definition.** Given a forgetful functor U: **D** → **C**, a left adjoint F: **C** → **D** (when it exists) is called the **free construction**. F ⊣ U.

The free construction F(A) is the "simplest" object in **D** generated by A ∈ **C** — it has exactly the structure needed to be an object of **D** and nothing more.

**Properties:**
- Unit η: A → U(F(A)) maps generators into the free object. Injectivity is an
  additional property, not a consequence of an arbitrary adjunction.
- Counit ε: F(U(D)) → D evaluates the free object on the underlying object of
  D. Surjectivity likewise needs additional algebraic hypotheses.
- η iso means the left adjoint F is full and faithful.
- When ε is a quotient map in a concrete algebraic setting, **D is a quotient
  of F(U(D))**, not the other way around.

## 12. Wiring Diagram

**Definition (Spivak).** A wiring diagram is a morphism in the category WD of typed interfaces. An interface is a pair (In, Out) of types. A wiring diagram φ: (In₁, Out₁) × ... × (In_n, Out_n) → (In, Out) specifies how the outputs of inner boxes connect to inputs of other inner boxes or the outer interface.

**Composition.** Wiring diagrams compose by substitution: plugging a wired system into a slot of another wiring diagram.

**Monoidal structure.** Parallel composition ⊗ places systems side by side without interaction.

## Sources

- Mac Lane, S. "Categories for the Working Mathematician" — §1-4 (categories, functors, natural transformations, adjunctions)
- Barbosa, L. "Coalgebra for the Working Software Engineer" — §6 (coalgebras, bisimulation, coinduction)
- Spivak, D. "Categorical Systems Theory" — §7 (lenses), §12 (wiring diagrams)
- Fong & Spivak. "Seven Sketches in Compositionality" — §8 (limits, colimits, presheaves, Yoneda)
- Awodey, S. "Category Theory" — §10 (monads, Kleisli categories)
- Riehl, E. *Category Theory in Context*:
  https://emilyriehl.github.io/files/context.pdf
- Rutten, J. *Universal Coalgebra*:
  https://fldit-www.cs.tu-dortmund.de/~peter/Rutten/UniversalCoalgebra.pdf

## Correction note

Version 1.1.0 corrects the definition of `Pos`, removes unsupported
injectivity/surjectivity claims for arbitrary adjunctions, reverses the
misstated quotient direction, and qualifies final-coalgebra/bisimulation
claims by their existence and preservation hypotheses.
