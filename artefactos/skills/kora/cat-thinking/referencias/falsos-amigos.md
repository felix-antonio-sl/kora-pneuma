# Falsos amigos — vocablos categoricos vs analogias informales

Cuando el vocabulario categorial entra al lenguaje cotidiano de ingenieria, sus palabras se diluyen. Esta tabla preserva la **distincion estricta**: lo que parece pero no es. La skill **debe** usar el termino preciso o renombrar el caso.

## Funtor

| Lo que parece | Lo que es |
|---------------|-----------|
| "una funcion entre dos cosas" | un mapeo `F: C → D` que preserva **composicion** (`F(g ∘ f) = F(g) ∘ F(f)`) e **identidad** (`F(id_A) = id_F(A)`). Sin esas dos leyes no es funtor. |
| "como un map de listas" | un `map` cumple las leyes para una categoria especifica (`Set` con funciones); no toda funcion entre estructuras es funtor. |

**Si el "funtor" propuesto no preserva composicion o identidad, no es funtor.** Llamarlo "transformacion" o "mapping" hasta que se demuestre que cumple las leyes.

## Transformacion natural

| Lo que parece | Lo que es |
|---------------|-----------|
| "un map" | una familia de morfismos `α_A: F(A) → G(A)` indexada por objetos, **uniforme** en el sentido de que conmuta con los morfismos del dominio. |
| "polimorfismo paramétrico" | en `Set`-like, si. Pero la *naturalidad* es la condicion mas fuerte: el cuadrado de naturalidad debe conmutar para todo morfismo. |

**Si los componentes no conmutan con los morfismos, no es transformacion natural; es una familia de morfismos sin garantia.**

## Monada

| Lo que parece | Lo que es |
|---------------|-----------|
| "un pipeline con efectos" | un endofuntor `T: C → C` con dos transformaciones naturales `η: Id → T` (unit) y `μ: T² → T` (multiplication) que cumplen leyes de asociatividad e identidad. |
| "una clase con `then`" | la clase con `then` cumple las leyes solo cuando `then` es la operacion de Kleisli `>>=` y satisface coherencia. |
| "wrapper de errores" | hay una monada de errores (`Maybe`, `Either`), pero "envolver errores" en general no es la monada. |

**Si las leyes de monada (left identity, right identity, asociatividad) no se cumplen, no es monada. Es una abstraccion sin garantias de composicion.**

## Coalgebra

| Lo que parece | Lo que es |
|---------------|-----------|
| "una clase con metodo `next`" | una funcion `α: A → F(A)` para un endofuntor `F`. La estructura captura **observacion**: estado produce observaciones via interface functor. |
| "un iterador" | un iterador es un caso particular de coalgebra (sobre `F(A) = 1 + A × A`). No toda clase con `next()` lo es. |

## Bisimulacion

| Lo que parece | Lo que es |
|---------------|-----------|
| "dos cosas que parecen iguales" | una relacion `R ⊆ A × B` que se preserva bajo observaciones: si `(a, b) ∈ R` y `α(a) = (..., a')`, entonces existe `b'` tal que `β(b) = (..., b')` y `(a', b') ∈ R`. |
| "los outputs son iguales" | mas fuerte: las **transiciones** producen estados que tambien son bisimilares. |

**"Hace lo mismo" no es bisimulacion sin coalgebra de soporte.**

## Adjuncion

| Lo que parece | Lo que es |
|---------------|-----------|
| "F y G son inversos" | tener `Hom(F(X), Y) ≅ Hom(X, G(Y))` natural en X y Y. **No** son inversos: F y G casi nunca componen a la identidad. |
| "F construye, G destruye" | F construye libremente, G olvida. La unidad y counit miden cuanto pierde cada lado. |

**No declarar adjuncion sin verificar el iso natural de hom-sets.**

## Limite / colimite

| Lo que parece | Lo que es |
|---------------|-----------|
| "el resultado de combinar varios" | el objeto **universal** que satisface el diagrama: cualquier otra solucion factoriza unicamente a traves de el. |
| "el conjunto interseccion" | la interseccion es un caso particular (pullback en Set sobre conjuntos con inclusion). |

**Sin universalidad explicita, no es limite. Es solo "una solucion".**

## Yoneda

| Lo que parece | Lo que es |
|---------------|-----------|
| "puedo entender un objeto por su API" | un objeto `A` queda determinado salvo isomorfismo natural por el funtor representable `Hom(A, -)`. |
| "duck typing" | duck typing es heuristica; Yoneda es teorema bajo categoria correcta. |

**Yoneda no autoriza confundir objetos distintos con la misma API. Autoriza tratar isomorfismos de hom-funtores como isomorfismos de objetos.**

## Topos

| Lo que parece | Lo que es |
|---------------|-----------|
| "una categoria con logica" | una categoria con limites finitos, exponenciales y clasificador de subobjetos `Ω`. |
| "feature flags" | feature flags se *modelan* en algunos topos, pero "tener flags" no implica trabajar en un topos. |

**No nombrar topos sin identificar limites finitos, exponenciales y clasificador.**

## Sheaf

| Lo que parece | Lo que es |
|---------------|-----------|
| "datos distribuidos que cuajan" | un presheaf que satisface la **condicion de pegado**: secciones locales compatibles tienen una unica seccion global. |
| "log distribuido" | un log distribuido **puede** ser sheaf si cumple pegado; sin verificar la condicion, es solo un presheaf. |

## Free monad

| Lo que parece | Lo que es |
|---------------|-----------|
| "monada cualquiera" | la monada *libre* sobre un funtor `F`: la mas general posible, sin operaciones extra. |
| "DSL de comandos" | un DSL de comandos **es** un free monad sobre el funtor de comandos, si las leyes se respetan. |

## Cofree comonad

| Lo que parece | Lo que es |
|---------------|-----------|
| "stream infinito" | una *instancia* de cofree comonad sobre el funtor adecuado. |
| "tipo recursivo lazy" | un tipo recursivo no necesariamente es cofree; lo es bajo construccion explicita y leyes verificadas. |

## Operad

| Lo que parece | Lo que es |
|---------------|-----------|
| "estructura jerarquica" | una operad es una familia de **espacios de operaciones** con composicion sustitutiva y unidades. |
| "tree de containers" | la operad puede capturar la composicion entre niveles, no es la jerarquia misma. |

## Polynomial functor

| Lo que parece | Lo que es |
|---------------|-----------|
| "una API" | un polinomio `Σ_{i∈I} y^{A_i}` donde `I` son posiciones (lo que la API muestra) y `A_i` son direcciones (lo que la API acepta). |
| "un product type" | un product type puede ser polynomial; no todo product type lo es ni todo polynomial es product. |

## Reglas de uso

1. **Siempre escribir el termino preciso**, no el termino que parece.
2. **Si el termino preciso no aplica**, usar un termino mas debil ("mapping", "transformacion") y declarar que las leyes no se han verificado.
3. **No "promover" una analogia a teorema** sin verificar las leyes correspondientes.
4. **Si la skill dice "esto es una monada"**, debe poder citar las tres leyes y declarar que se cumplen.
5. **Si el agente invocador usa un falso amigo**, la skill lo corrige antes de modelar.
