---
urn: urn:kora:kb:cat-caso-vertical-steipete-codex
nombre: cat-caso-vertical-steipete-codex
version: 1.1.0
estado: publicado
descripcion: "Primer caso vertical de ingeniería agéntica en KORA: steipete sobre Codex CLI observado por una coálgebra finita y un transductor de JSONL que impiden declarar cierre sin evidencia verde vigente."
fuente: "Doctrina propia pneuma instanciada el 2026-07-19 desde urn:dev:artefacto:steipete y urn:kora:kb:cat-contrato-ingenieria-agentica. Base primaria: Moggi, Notions of computation and monads, https://person.dibris.unige.it/moggi-eugenio/ftp/ic91.pdf; Rutten, Universal Coalgebra, https://fldit-www.cs.tu-dortmund.de/~peter/Rutten/UniversalCoalgebra.pdf. Superficie runtime: OpenAI, Codex non-interactive mode, https://learn.chatgpt.com/docs/non-interactive-mode; esquema primario, https://github.com/openai/codex/blob/main/codex-rs/exec/src/exec_events.rs. Testigos ejecutables: tests/steipete_codex_observer.py y tests/test_steipete_vertical.py. v1.1.0 mecaniza obs_r para codex exec --json sin extender la afirmación a otras superficies Codex."
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
| `Runtime_codex-cli-exec(r)` | `tests/steipete_codex_observer.py` sobre `codex exec --json` | mecanizado bajo el protocolo local |
| `Runtime_codex-app(r)` | conversación y tool outputs de esta tarea | observación manual; fuera del adaptador |

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

OpenAI documenta que `codex exec --json` emite un stream JSONL con eventos
`thread.*`, `turn.*` e `item.*`. Sea `R` el conjunto de registros JSON
bien formados de esa superficie y `R_ok ⊆ R` el subconjunto que satisface el
protocolo local de markers y comandos canónicos.

```text
o     : R_ok -> I*
obs_r : R_ok* -> I*

obs_r(r1 ... rn) = o(r1) ... o(rn).
```

`I*` es el monoide libre de palabras de eventos. `obs_r` es la extensión de
`o` por concatenación: el único morfismo de monoides libres
`R_ok* -> I*` inducido por `o`. Esta capa vive en `Mon`; no convierte al
runtime Codex en coálgebra. Por construcción preserva palabra vacía y
concatenación:

```text
obs_r(ε) = ε
obs_r(xy) = obs_r(x) obs_r(y).
```

La proyección local es:

| Registro JSONL | Palabra observada |
|---|---|
| `turn.started` | `[capture]` |
| marker exacto `{"kind":"estimate"}` en `agent_message` | `[estimate]` |
| `file_change` nativo no vacío o marker `{"kind":"change"}` | `[change]` |
| `command_execution` de un gate canónico | `[gate(g, status=completed ∧ exit_code=0)]` |
| marker exacto `{"kind":"feel-review","passed":b}` | `[gate(feel-review,b)]` |
| `turn.completed` | `[close]` |
| registro no observado | `ε` |

`turn.failed`, `error`, JSON inválido, markers inválidos y comandos que parecen
gates pero no tienen la forma canónica quedan fuera de `R_ok` y producen un
error de observación. El adaptador nunca ejecuta el texto de `command`: solo
lo clasifica y lee `status`/`exit_code`.

La mecanización prueba la extracción conforme a este protocolo. No verifica
por sí sola la verdad de `estimate`, `change` o `feel-review`: los markers
siguen siendo autoatestaciones. Tampoco observa una escritura realizada dentro
de un shell si Codex no emite `file_change`; esa escritura debe portar marker
`change` para invalidar la evidencia.

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

`tests/steipete_codex_observer.py` implementa el monitor y `obs_r`.
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

Para una traza `codex exec` instrumentada, el flujo es:

```text
codex exec --json ... > trace.jsonl
python3 tests/steipete_codex_observer.py trace.jsonl
```

El proceso retorna `0` solo si la observación es válida y el monitor alcanza
`closed`; retorna `1` ante violación del monitor y `2` ante error de
observación. Su salida contiene únicamente eventos normalizados y veredicto:
no reproduce prompts, razonamiento, outputs de comandos ni mensajes libres.

### Observación 2026-07-19

Después del último cambio sustantivo del caso se observaron estos resultados:

| Gate | Evidencia | Resultado |
|---|---|---|
| `py-compile` | `PYTHONPYCACHEPREFIX=/tmp/kora-observer-pyc python3 -m py_compile kora.py tests/steipete_codex_observer.py tests/test_steipete_vertical.py` | pass |
| `tests` | `python3 -m unittest discover -s tests` | 204 pass |
| `velar` | `python3 kora.py velar --estricto` | 13/13 pass |
| `diff-check` | `git diff --check` | pass |
| `paridad-steipete` | `transmutar --paridad --urn urn:dev:artefacto:steipete` | 5 fiel |
| `feel-review` | auto-revisión adversarial de tipos, frontera y subcoálgebra; sin ratificación externa | pass |

Una primera traza real no instrumentada produjo solo `[capture, close]` y fue
rechazada con `close-out-of-order`. Una segunda traza real, efímera y
instrumentada sobre `codex-cli 0.144.6`, produjo los diez eventos de referencia
y alcanzó `closed`. El JSONL crudo no se versionó porque contiene identificador
de hilo y mensajes; solo se conserva este resultado desidentificado.

La tabla es una atestación durable del run. El adaptador ingiere la traza solo
cuando se invoca explícitamente; KORA no lo ejecuta como gesto, no firma el
JSONL y no aplica enforcement automático.

## 7. Qué se ganó y qué sigue abierto

Este caso sí aporta:

- un agente y target concretos;
- una interfaz observable finita;
- `I`, `O`, `U`, `M` y `step`;
- una propiedad de safety cerrada;
- prueba local y test exhaustivo;
- una traza runtime concreta contrastable;
- extracción mecanizada para `codex exec --json` bajo protocolo explícito.

No aporta:

- una coálgebra del estado cognitivo completo de `steipete`;
- extracción desde Codex app, IDE, cloud o rollout JSONL privado;
- detección completa de mutaciones realizadas dentro de comandos shell;
- autenticidad criptográfica o resistencia a markers adversariales;
- atestación de directorio, binario o entorno efectivo más allá del texto
  canónico registrado;
- prueba sobre todas las ejecuciones;
- no amplificación de autoridad efectiva;
- composición con otros agentes;
- bisimulación source/runtime.

Por eso el caso no autoriza todavía ampliar el shape KORA. El siguiente paso,
si aporta valor real, es contrastar autoridad efectiva en un contexto Codex
acotado; no añadir más vocabulario categorial.

## Fuentes primarias

- Eugenio Moggi, *Notions of computation and monads*, Example 1.1:
  https://person.dibris.unige.it/moggi-eugenio/ftp/ic91.pdf
- J. J. M. M. Rutten, *Universal Coalgebra: a Theory of Systems*, §2:
  https://fldit-www.cs.tu-dortmund.de/~peter/Rutten/UniversalCoalgebra.pdf
- OpenAI, *Codex non-interactive mode*:
  https://learn.chatgpt.com/docs/non-interactive-mode
- OpenAI, esquema fuente de eventos `codex exec`:
  https://github.com/openai/codex/blob/main/codex-rs/exec/src/exec_events.rs
