---
urn: urn:kora:kb:cat-caso-vertical-steipete-codex
nombre: cat-caso-vertical-steipete-codex
version: 1.0.0
estado: publicado
descripcion: "Primer caso vertical de ingeniería agéntica en KORA: steipete sobre Codex observado por una coálgebra finita de trazas que impide declarar cierre sin evidencia verde vigente."
fuente: "Doctrina propia pneuma instanciada el 2026-07-19 desde urn:dev:artefacto:steipete y urn:kora:kb:cat-contrato-ingenieria-agentica. Base primaria: Moggi, Notions of computation and monads, https://person.dibris.unige.it/moggi-eugenio/ftp/ic91.pdf; Rutten, Universal Coalgebra, https://fldit-www.cs.tu-dortmund.de/~peter/Rutten/UniversalCoalgebra.pdf. Testigo ejecutable: tests/test_steipete_vertical.py."
autor: FS
creado: 2026-07-19
lang: es
tags: [ingenieria-agentica, coalgebra, trazas, codex, steipete, safety]
familia: bok
depende: [urn:dev:artefacto:steipete, urn:dev:artefacto:ship-discipline, urn:kora:kb:cat-contrato-ingenieria-agentica, urn:kora:kb:cat-agent-coalgebra]
---

# Caso vertical: steipete en Codex

## 1. Pregunta y alcance

Este caso responde una sola pregunta observable:

> ¿Puede una ejecución de `steipete` declarar cierre antes de registrar como
> verdes todos los gates vigentes después del último cambio?

La prueba se aplica a un **monitor de trazas**, no al estado oculto del LLM.
Una traza aceptada aporta evidencia de esa ejecución. No demuestra que toda
ejecución futura de Codex obedezca el monitor, ni bisimulación, enforcement de
tools o safety general del agente.

Estatus:

| Capa | Testigo | Estatus |
|---|---|---|
| `Spec` | `urn:dev:artefacto:steipete` exige blast radius antes de actuar y loop closure | declaración fuente |
| `Product_codex` | custom agent y skill instalados con sello/paridad | congruencia material |
| `Model` | monitor finito `step` definido abajo | formal |
| `Runtime_codex(r)` | proyección manual de esta tarea a eventos observables | evidencia de un caso |

## 2. Interfaz observable

Sea el conjunto finito de gates del contexto de esta tarea:

```text
G = {
  py-compile,
  tests,
  velar,
  diff-check,
  paridad-steipete,
  feel-review
}.
```

`feel-review` es una atestación cualitativa explícita. En este run corresponde
a la auto-revisión adversarial del agente, no a una ratificación independiente.
El monitor verifica que existe y está vigente; no convierte gusto
arquitectónico en prueba automática. KORA no tiene build separado ni linter
configurado, por lo que no se inventan gates nominales para esas superficies.

El alfabeto de entradas es:

```text
I =
  {capture, estimate, change, close}
  + (G × {pass, fail}).
```

Sea `R_r` el conjunto de registros observables de esta tarea Codex. Cada
registro puede portar evidencia textual. La observación manual y parcial

```text
obs_r : R_r ⇀ I
```

contrasta esa evidencia y proyecta solo los registros interpretables,
conservando tipo, gate y resultado. El testigo ejecutable implementa ese `I`
finito; verificar la verdad de la evidencia sigue siendo una obligación
externa a `step`.

Las salidas son acknowledgements finitos:

```text
O = {
  intent-captured,
  blast-radius-estimated,
  evidence-invalidated,
  gate-passed,
  gate-failed,
  closed
}.
```

## 3. Estado y efecto

Trabajamos en `Set`. Sea:

```text
Phase = {
  start, intent, estimated, dirty, validating, closed
}

U = Phase × P(G).
```

La segunda componente registra gates verdes desde el último cambio. Sea el
conjunto finito de violaciones del modelo:

```text
V =
  {
    already-closed,
    intent-out-of-order,
    estimate-out-of-order,
    change-out-of-order,
    gate-out-of-order,
    close-out-of-order
  }
  + { close-without(K) | ∅ != K ⊆ G }.
```

Tiene 69 elementos: seis violaciones de orden y una por cada subconjunto no
vacío de gates faltantes. Elegimos la mónada estándar de excepciones:

```text
M(X) = X + V
η_X(x) = inl(x)

μ_X(inl(inl(x))) = inl(x)
μ_X(inl(inr(v))) = inr(v)
μ_X(inr(v))      = inr(v).
```

Las leyes de unidad y asociatividad se verifican por los casos `inl`/`inr`;
esta es la instancia de excepciones `T(A)=A+E` de Moggi.

Definimos:

```text
H(X) = (M(O × X))^I
M(f)(inl(x)) = inl(f(x))
M(f)(inr(v)) = inr(v)
H(h)(k)(i) = M(id_O × h)(k(i))

step : U × I -> M(O × U).
```

Por currificación, `step` determina una `H`-coálgebra
`c : U -> H(U)`. El monitor es effectful solo en el sentido preciso de que una
entrada ilegal retorna una violación en la mónada de excepciones.
Identidad y composición de `H` se siguen de las de `M`, producto y
exponenciación; aquí no se postula una acción sobre el runtime Codex.

## 4. Transición

Las transiciones aceptadas son:

```text
start      --capture--> intent
intent     --estimate--> estimated
estimated --change--> dirty,       passed := ∅
dirty|validating --gate(g,pass)--> validating, passed := passed ∪ {g}
dirty|validating --gate(g,fail)--> dirty,       passed := ∅
validating --close--> closed        solo si passed = G
```

Un nuevo `change` desde `dirty` o `validating` vuelve a `dirty` y vacía toda
evidencia. Cualquier otro par estado/evento produce `inr(v)` y no un estado
siguiente. En particular, una violación no se disfraza de transición válida.

## 5. Propiedad de safety

Sea:

```text
S = { (phase, passed) ∈ U
    | phase != closed o passed = G }.
```

**Proposición.** Todo resultado exitoso de `step` que parte de `S` vuelve a
`S`; además, `closed` solo es alcanzable con `passed = G`.

**Prueba.**

1. `capture` y `estimate` producen fases no cerradas.
2. `change` y `gate(_,fail)` producen `dirty` con conjunto vacío.
3. `gate(_,pass)` produce `validating`, nunca `closed`.
4. La única rama que produce `closed` exige literalmente `passed = G`.
5. Las demás entradas retornan una excepción y no producen estado sucesor.

Por análisis exhaustivo de casos, la inclusión `S ↪ U` es cerrada respecto de
las transiciones exitosas del monitor. La restricción `step_S` conserva las
excepciones y usa el sucesor ya demostrado en `S`; por currificación induce
`s:S→H(S)` y satisface `H(i) . s = c . i` para la inclusión `i:S↪U`.

`tests/test_steipete_vertical.py`
enumera además los 6.144 pares estado/evento del modelo; para los 5.136 pares
con estado inicial seguro comprueba mecanizadamente que todo sucesor aceptado
sigue siendo seguro. El código añade rechazos defensivos para valores Python
fuera de `U × I`; no amplían el alfabeto formal ni la demostración. ∎

## 6. Traza vertical de referencia

La ejecución de cierre tiene esta forma:

```text
capture
estimate
change
gate(py-compile, pass)
gate(tests, pass)
gate(velar, pass)
gate(diff-check, pass)
gate(paridad-steipete, pass)
gate(feel-review, pass)
close
```

El testigo ejecutable acepta esa traza y rechaza:

- cierre con cualquier gate faltante;
- cierre después de un cambio que hizo rancia la evidencia;
- continuidad como si un gate rojo preservara los verdes anteriores;
- eventos fuera de orden o después del cierre.

La correspondencia con esta tarea se cierra solo después de ejecutar los
comandos y revisar el patch final. El test de la traza demuestra el monitor; el
registro de esos resultados aporta la evidencia empírica de esta ejecución.

### Observación 2026-07-19

Después del último cambio sustantivo del caso se observaron estos resultados:

| Gate | Evidencia | Resultado |
|---|---|---|
| `py-compile` | `python3 -m py_compile tests/test_steipete_vertical.py` | pass |
| `tests` | `python3 -m unittest discover -s tests` | 198 pass |
| `velar` | `python3 kora.py velar --estricto` | 13/13 pass |
| `diff-check` | `git diff --check` | pass |
| `paridad-steipete` | `transmutar --paridad --urn urn:dev:artefacto:steipete` | 5 fiel |
| `feel-review` | auto-revisión adversarial de tipos, frontera y subcoálgebra; sin ratificación externa | pass |

La tabla es una atestación durable del run. La salida de comandos en la tarea
Codex es la evidencia primaria de ejecución; KORA todavía no la ingiere ni la
firma automáticamente.

## 7. Qué se ganó y qué sigue abierto

Este caso sí aporta:

- un agente y target concretos;
- una interfaz observable finita;
- `I`, `O`, `U`, `M` y `step`;
- una propiedad de safety cerrada;
- prueba local y test exhaustivo;
- una traza runtime concreta contrastable.

No aporta:

- una coálgebra del estado cognitivo completo de `steipete`;
- extracción automática de eventos desde Codex;
- prueba sobre todas las ejecuciones;
- no amplificación de autoridad efectiva;
- composición con otros agentes;
- bisimulación source/runtime.

Por eso el caso no autoriza todavía ampliar el shape KORA. El siguiente paso,
si aporta valor real, es mecanizar la observación de trazas del runtime; no
añadir más vocabulario categorial.

## Fuentes primarias

- Eugenio Moggi, *Notions of computation and monads*, Example 1.1:
  https://person.dibris.unige.it/moggi-eugenio/ftp/ic91.pdf
- J. J. M. M. Rutten, *Universal Coalgebra: a Theory of Systems*, §2:
  https://fldit-www.cs.tu-dortmund.de/~peter/Rutten/UniversalCoalgebra.pdf
