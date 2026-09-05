---
urn: urn:kora:kb:cat-agent-modulo
nombre: cat-agent-modulo
version: 2.0.0
estado: publicado
descripcion: "Lectura rigurosa de pattern-runs-on-matter para KORA: resultado formal en Poly, traducción PMI como modelo de diseño y puente aún abierto hacia la coálgebra efectual y la teleología."
fuente: "Doctrina propia pneuma corregida el 2026-07-18. Base primaria: Libkind y Spivak, Pattern Runs on Matter, https://arxiv.org/abs/2404.16321. La aplicación de ese resultado a los ordinales PMI se declara modelo de diseño y no teorema."
autor: FS
creado: 2026-06-30
lang: es
tags: [agente, free-monad, cofree-comonad, poly, plan-materia, teleologia, kora]
familia: bok
depende: [urn:fxsl:kb:icas-agencia, urn:kora:kb:cat-agent-coalgebra]
refina: [urn:kora:kb:cat-agent-coalgebra]
cita: [urn:kora:kb:aufbau-persona-agente, urn:fxsl:kb:icas-safety-alignment]
---

# Plan, materia e interacción: alcance del módulo

## 1. Resultado formal externo

Libkind y Spivak trabajan en la categoría de funtores polinomiales `Poly` con
el producto monoidal de sustitución. Allí construyen la mónada libre sobre un
polinomio como árboles de decisión terminantes, estudian la comónada cofree y
una acción de módulo de la primera sobre la segunda. La lectura es:

```text
pattern runs on matter
```

El resultado depende de objetos y morfismos concretos de `Poly`. No afirma que
cualquier plan sea literalmente una mónada libre ni que cualquier memoria sea
una comónada cofree.

## 2. Traducción de KORA

KORA usa `pi`, `mu` y `xi` como coordenadas ordinales de un clasificador:

- `pi` aproxima complejidad del plan;
- `mu` aproxima persistencia/entorno de la materia;
- `xi` aproxima complejidad del acoplamiento.

Esta traducción es una **heurística estructurada** inspirada en
pattern-runs-on-matter. Los números no contienen:

- un funtor polinomial `p`;
- las posiciones y direcciones de ese polinomio;
- una mónada libre `m_p`;
- una comónada cofree `c_q`;
- una acción de módulo bien tipada.

Por eso son inválidas, sin datos adicionales, las identificaciones
`pi = m_p`, `mu = c_q` o `xi = Ξ`. El vector permite comparar perfiles KORA;
no construye el objeto categorial.

## 3. Puente hacia la coálgebra efectual

`urn:kora:kb:cat-agent-coalgebra` propone el modelo mínimo:

```text
H(X) = (M(O × X))^I
c : U -> H(U).
```

Relacionar este `H` con un polinomio `p`, su mónada libre y su comónada cofree
requeriría al menos:

1. elegir `p` y `q` a partir de interfaces reales;
2. definir funtores desde el dominio PMI hacia las construcciones relevantes
   de `Poly`;
3. exhibir la acción sobre morfismos;
4. demostrar las leyes de módulo;
5. explicar cómo los efectos `M` interactúan con esas construcciones.

KORA no dispone aún de esos datos. El puente retículo↔coálgebra↔`Poly` queda
abierto, no como un morfismo supuesto.

## 4. Personalidad y teleología

La descomposición:

```text
U = U_phen × U_ctx × U_epi × U_sta
```

permite tratar `U_phen` como parámetro de una transición. Es un modelo útil:
el estado fenomenológico puede influir en la elección de salida o siguiente
estado. El producto no demuestra independencia, y esa dependencia impide
inferir bisimulación entre agentes con personalidades distintas.

La *Tektonik* de `urn:kora:kb:aufbau-persona-agente` aporta una dirección de
diseño axiológico. No constituye por sí misma un isomorfismo natural de
objetivos. Para hablar de una transformación
`G_agent ⇒ G_principal` se necesitan una categoría dominio, dos funtores y
componentes naturales; para llamarla isomorfismo, cada componente debe ser
invertible. Entrenamiento, RLHF o una consigna no suministran automáticamente
esa estructura.

Convergencia hacia un fin también es una propiedad dinámica separada. Exige
una noción de trayectoria, objetivo y convergencia; no se sigue de naturalidad
ni de un punto fijo sin propiedad universal.

## 5. Estatus de las afirmaciones

| Afirmación | Estatus |
|---|---|
| mónada libre, comónada cofree y acción de módulo en `Poly` | formal, bajo las hipótesis del artículo |
| PMI como vocabulario plan/materia/interacción | modelo de diseño |
| `pi`, `mu`, `xi` construyen objetos de `Poly` | falso sin datos adicionales |
| puente PMI→`Poly`→coálgebra efectual | problema abierto |
| `U_phen` puede parametrizar la transición | modelo |
| separación de archivos implica independencia conductual | falso |
| alineamiento perfecto es un `α`-iso | metáfora hasta definir los funtores |
| naturalidad implica convergencia | falso |

## Fuente primaria

- Sophie Libkind y David I. Spivak, *Pattern Runs on Matter: The Free Monad
  Monad as a Module over the Cofree Comonad Comonad*:
  https://arxiv.org/abs/2404.16321
