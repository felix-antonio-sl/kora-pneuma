---
urn: urn:kora:kb:cat-kora-kernel
nombre: cat-kora-kernel
version: 1.0.0
estado: publicado
descripcion: "Núcleo categorial mínimo y demostrado de KORA: retículo de firmas, proyección por target como funtor entre categorías delgadas, coreflexión, alcance del sello y semántica de relaciones como grafos generadores."
fuente: "Doctrina propia pneuma, formalizada el 2026-07-18 a partir de ley/1 y ley/3. Base externa primaria: Riehl, Category Theory in Context (posets como categorías y adjunciones), https://emilyriehl.github.io/files/context.pdf; Lawvere, Metric Spaces, Generalized Logic, and Closed Categories, https://www.math.buffalo.edu/~sww/0papers/lawveres-metric-space-paper.pdf. La prueba específica de KORA se da completa en este cuerpo."
autor: FS
creado: 2026-07-18
lang: es
tags: [kora, teoria-categorias, reticulo, proyeccion, adjuncion, rigor-formal]
familia: bok
depende: [urn:kora:kb:cat-foundations]
---

# Núcleo categorial mínimo de KORA

## 1. Estatus y frontera

Este documento contiene la parte de KORA que sí está formulada y demostrada
categorialmente. Su alcance es deliberadamente estrecho:

- **formal**: orden de firmas y proyección numérica por target;
- **operacional probado**: serialización determinista, hash y congruencia de
  emisiones;
- **no demostrado como categorial**: emisión completa de artefactos, transporte
  del cuerpo, bisimulación, naturalidad de la interacción, safety y composición
  de efectos.

La lectura más débil suficiente evita dos errores: llamar «funtor» a una
función sin categorías declaradas y llamar «prueba» a un certificado de
integridad.

## 2. El retículo de firmas

Sea

```text
L = [0,3] × [0,3] × [0,4] × [0,3] × [0,4] × [0,3]^5
```

con orden componente a componente. Sus coordenadas son
`(pi, mu, xi, lambda, phi, sigma[0..4])`. `L` es un retículo producto:
el meet es el mínimo componente a componente y el join es el máximo.

Sea `V ⊆ L` el subconjunto de firmas que satisfacen las cinco leyes inter-eje
de `ley/1 §4`.

**Proposición 1.** `V` es un subretículo acotado de `L`.

**Prueba.** Cada ley tiene forma de umbral:

```text
x >= a  implica  y >= b
```

(la igualdad con el máximo, como `xi == 4`, es el mismo caso en una cadena
finita). Para el join, si el antecedente se activa en el máximo, se activaba
en al menos uno de los operandos y el máximo de los consecuentes satisface el
umbral. Para el meet, si el antecedente se mantiene en el mínimo, se activaba
en ambos operandos y el mínimo de los consecuentes satisface el umbral. Esto
vale también para la ley `lambda == 3`, aplicada a cada componente de
`sigma`. El mínimo y el máximo globales satisfacen las leyes. ∎

`V` se considera como **categoría delgada**: sus objetos son firmas y existe
una única flecha `v → w` exactamente cuando `v ≤ w`. La identidad y la
composición provienen de reflexividad y transitividad. Una firma clasifica;
no individúa artefactos ni prueba equivalencia conductual.

## 3. Dominio e imagen de cada target

Para un target realizado `T`, sea `D_T ⊆ V` el conjunto de firmas cuyos valores
no caen en `∅` en la matriz de `ley/3 §4`. Cada soporte por coordenada es un
segmento inicial; por tanto `D_T` es un downset y un subretículo de `V`.

La proyección numérica es

```text
P_T(v)_i = min(v_i, c_T,i)
```

para cada coordenada soportada, incluidos los cinco componentes de `sigma`.
Los rótulos `full` y `partial` describen fidelidad operacional y no forman
parte del objeto de `V`.

Sea `I_T = P_T(D_T)`, con el orden heredado, y
`J_T : I_T ↪ D_T` su inclusión.

**Proposición 2.** `P_T : D_T → I_T` es un funtor.

**Prueba.** Si `v ≤ w`, entonces
`min(v_i,c_T,i) ≤ min(w_i,c_T,i)` en cada coordenada; luego
`P_T(v) ≤ P_T(w)`. Todo mapa monótono entre posets induce un funtor entre sus
categorías delgadas: envía la única flecha `v → w` a la única flecha
`P_T(v) → P_T(w)`, preservando identidades y composición. Las cinco leyes
inter-eje siguen satisfechas porque sus umbrales se preservan por las matrices
vigentes; esta propiedad se verifica en la suite por cada ley. ∎

Además:

```text
P_T(v) <= v
P_T(P_T(v)) = P_T(v)
```

La primera ecuación declara que nunca se proyecta hacia arriba; la segunda,
que reproyectar no agrega pérdida numérica.

## 4. La coreflexión

**Proposición 3.** `J_T` es adjunto izquierdo de `P_T`:

```text
J_T ⊣ P_T
```

**Prueba.** Para `a ∈ I_T` y `d ∈ D_T`, toda coordenada de `a` está bajo el
techo `c_T`. Por ello:

```text
J_T(a) <= d    si y solo si    a <= min(d, c_T) = P_T(d).
```

En categorías delgadas esta equivalencia de desigualdades es exactamente la
biyección natural de hom-sets. La unidad es identidad porque
`P_T(J_T(a)) = a`; la counit es la flecha `J_T(P_T(d)) → d` inducida por
`P_T(d) ≤ d`. ∎

Así, `I_T` es una subcategoría **coreflexiva** de `D_T` y `P_T` es el
coreflector. Esta es la formulación categorial precisa de «recortar al máximo
que el target soporta».

## 5. Lo que la prueba no cubre

El emisor completo toma un artefacto validado, calcula `P_T`, serializa
frontmatter/cuerpo/sidecars y produce un conjunto finito de archivos. KORA
prueba propiedades operacionales de esa transformación:

- determinismo byte a byte;
- hash de la fuente;
- congruencia fuente-generador-producto;
- declaración tipada de pérdidas;
- paridad de la superficie gestionada cuando se inspecciona el runtime.

No se han definido una categoría de artefactos, una categoría de productos de
runtime ni la acción del emisor sobre sus morfismos. Por eso la emisión
completa se llama **compilación/serialización determinista**, no funtor. Copiar
el cuerpo o repartir un span entre archivos tampoco es un lift cartesiano
mientras no se exhiba una fibración y su propiedad universal.

El campo histórico `funtor: T-...` del sello es un identificador estable de
contrato. Las líneas `composicion` e `identidad` del sello se refieren
exclusivamente a `P_T` entre categorías delgadas. El sello es un certificado
de procedencia, proyección y congruencia; no es un objeto de prueba de
naturalidad, bisimulación, safety ni composición Kleisli.

## 6. Relaciones

Cada campo relacional del frontmatter almacena **aristas generadoras**
`A → B`; no almacena identidades, composiciones ni cierre transitivo.

Para cualquier relación `R`, el grafo dirigido `G_R` genera una categoría
libre `Path(G_R)`:

- objetos: URNs;
- morfismos: caminos finitos de aristas;
- identidad: camino vacío;
- composición: concatenación de caminos.

`velar` valida el grafo declarado, no materializa `Path(G_R)`. En
`depende`, `reemplaza` y `refina`, la aciclicidad hace que la alcanzabilidad
reflexiva induzca un orden parcial. La ausencia de una arista transitiva
directa no es error: `A → B → C` ya determina un camino `A → C`.

## 7. Regla epistémica

Toda afirmación categorial del corpus debe llevar uno de estos estatus:

| Estatus | Exigencia |
|---|---|
| **formal** | categorías, objetos, morfismos y leyes definidos; prueba o fuente primaria precisa |
| **modelo bajo hipótesis** | construcción bien tipada, con hipótesis y alcance declarados |
| **heurística** | analogía estructural útil, sin garantía teoremática |
| **metáfora** | recurso explicativo; no autoriza inferencias formales |

Una URN aporta trazabilidad interna. No convierte por sí sola una analogía en
teorema.

## Fuentes primarias

- Emily Riehl, *Category Theory in Context*, introducción y capítulo 4:
  https://emilyriehl.github.io/files/context.pdf
- F. William Lawvere, *Metric Spaces, Generalized Logic, and Closed
  Categories*, pp. 1-2:
  https://www.math.buffalo.edu/~sww/0papers/lawveres-metric-space-paper.pdf
