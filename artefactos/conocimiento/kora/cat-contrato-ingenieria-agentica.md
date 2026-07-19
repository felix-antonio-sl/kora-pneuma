---
urn: urn:kora:kb:cat-contrato-ingenieria-agentica
nombre: cat-contrato-ingenieria-agentica
version: 1.2.0
estado: publicado
descripcion: "Contrato de rigor para ingeniería agéntica en KORA: testigos mínimos para interfaces, coálgebras con efectos, equivalencia conductual, composición por cableado, capacidades, safety y preservación en runtime."
fuente: "Doctrina propia pneuma formalizada el 2026-07-18. Fuentes primarias: Rutten, Universal Coalgebra, https://fldit-www.cs.tu-dortmund.de/~peter/Rutten/UniversalCoalgebra.pdf; Beohar et al., Predicate and relation liftings for coalgebras with side effects, https://arxiv.org/abs/2110.09911; Vagner, Spivak y Lerman, Algebras of Open Dynamical Systems on the Operad of Wiring Diagrams, https://arxiv.org/abs/1408.1598; Libkind y Spivak, Pattern Runs on Matter, https://arxiv.org/abs/2404.16321. v1.1.0 (2026-07-19): enlaza el primer caso vertical steipete→Codex y conserva explícitamente sus límites. v1.2.0 (2026-07-19): registra obs_r mecanizado para codex exec --json y mantiene fuera de alcance las demás superficies Codex."
autor: FS
creado: 2026-07-18
lang: es
tags: [ingenieria-agentica, teoria-categorias, coalgebra, efectos, composicion, safety, kora]
familia: bok
depende: [urn:kora:kb:cat-agent-coalgebra, urn:kora:kb:cat-agent-modulo, urn:kora:kb:cat-kora-semantica-operacional, urn:fxsl:kb:icas-escala]
---

# Contrato categorial de ingeniería agéntica

## 1. Vocación y frontera

KORA es la fuente canónica de **declaraciones de diseño y artefactos
proyectables** para sistemas LLM. No es su semántica de ejecución.

Un agente KORA contiene hoy:

- identidad nominal por URN;
- firma clasificatoria PMI × LFS;
- arnés, forma, cuerpo y conocimiento permitido;
- herramientas y targets declarados;
- etiquetas opcionales de estados;
- candidatos opcionales de composición.

Estos datos son valiosos para autoría, gobierno y compilación. No definen por
sí solos entradas, salidas, transición, efectos ni observaciones. Por tanto:

```text
artefacto KORA  -/->  coálgebra, por mera declaración
misma firma     -/->  misma conducta
componible      -/->  composición semántica
sello fiel      -/->  bisimulación o safety
```

Este contrato especifica qué testigos adicionales hacen legítima cada
afirmación categorial. No añade campos al shape: inventar un esquema antes de
tener una semántica concreta convertiría notación vacía en deuda obligatoria.

## 2. Tres niveles que no deben colapsarse

Para un artefacto agéntico `a` y target `T`, se distinguen:

```text
Spec(a)          fuente declarativa KORA
Model(a)         modelo matemático explícito, si existe
Runtime_T(a,r)   conducta efectiva bajo contexto runtime r
```

La transmutación actúa sobre `Spec(a)`. Un modelo categorial actúa sobre
`Model(a)`. Un teorema de preservación necesita una interpretación que conecte
ambos con `Runtime_T(a,r)`. Ninguna de las tres capas sustituye a otra.

## 3. Modelo reactivo mínimo

Fijar:

- conjunto de entradas `I`;
- conjunto de salidas/acciones observables `O`;
- conjunto de estados `U`;
- mónada `M` en `Set`, cuyo endofuntor modela los efectos elegidos.

Definir:

```text
H(X) = (M(O × X))^I
H(h)(k)(i) = M(id_O × h)(k(i)).
```

Un agente reactivo effectful es una `H`-coálgebra:

```text
c : U -> H(U)
```

equivalente por currificación a:

```text
step : U × I -> M(O × U).
```

No basta nombrar `M`: hay que dar unidad, multiplicación y leyes de mónada, o
citar una mónada estándar con la instancia exacta. Probabilidad,
no-determinismo, excepciones, estado y logging no son el mismo efecto.

El cuerpo de instrucciones de un LLM no proporciona automáticamente `U` ni
`step`. Una realización puede abstraerlos desde trazas o desde un runtime,
pero debe declarar qué estado oculto omite y qué observables conserva.

## 4. Morfismos y equivalencia conductual

Para dos coálgebras del **mismo** endofuntor `H`,
`(U,c)` y `(V,d)`, un morfismo coalgebraico es:

```text
h : U -> V
H(h) . c = d . h.
```

Este cuadrado demuestra que `h` preserva la conducta modelada. No compone
agentes en serie: relaciona dos sistemas bajo una misma firma de observación.

Una bisimulación puede darse mediante `R ⊆ U × V` con estructura
`r:R→H(R)` cuyas proyecciones sean morfismos de coálgebras. Presentaciones por
lifting relacional requieren las hipótesis correspondientes sobre `H` y, con
efectos, la semántica coalgebraica elegida.

Agentes con distintos `I`, `O` o `M` no son objetos de una misma
`Coalg(H)`. Antes de compararlos se necesitan adaptadores o un cambio de base
explícito. «Ambos usan texto» no identifica sus interfaces: schemas,
protocolos, tool calls y errores también son parte del tipo observable.

## 5. Interfaces y composición

La composición de agentes es una pregunta diferente de los morfismos en
`Coalg(H)`.

Una ruta formal legítima consiste en construir:

1. una categoría monoidal u operad `W` de interfaces y cableados tipados;
2. puertos de entrada/salida para cada componente;
3. una semántica —por ejemplo, un álgebra o funtor monoidal laxo— que asigne
   sistemas a cajas e interprete cableados como composición;
4. una combinación de efectos que haga la transición compuesta bien tipada y
   asociativa;
5. estructura adicional para feedback, si existe: delay, traza, punto fijo o
   guardedness según el modelo concreto.

Vagner, Spivak y Lerman construyen precisamente una categoría monoidal de
wiring diagrams tipados y álgebras para sistemas dinámicos abiertos. Ese
resultado es un **patrón de formalización**; no prueba que los agentes LLM de
KORA pertenezcan a su álgebra.

El campo `componible` aporta solo aristas candidatas:

```text
G_comp : a -> b.
```

Su categoría libre `Path(G_comp)` compone caminos de declaraciones. No aporta
tipos de puerto, adaptadores, semántica de wiring ni compatibilidad de efectos.
Por eso:

```text
camino en Path(G_comp) != agente compuesto.
```

La composición serial de dos agentes requiere al menos un adaptador desde las
salidas observables del primero hacia las entradas del segundo. La composición
paralela requiere producto/tensor y una regla de combinación de efectos. La
delegación requiere además protocolo, retorno, errores y autoridad.

## 6. Pattern runs on matter

El resultado de Libkind y Spivak vive en `Poly`, con:

- polinomios concretos;
- mónada libre;
- comónada cofree;
- acción de módulo bajo el producto de sustitución.

La tríada ordinal `pi,mu,xi` no construye esos objetos. Para aplicar el
resultado a un agente se deben exhibir polinomios con posiciones y
direcciones, la acción y su relación con `I`, `O`, `M` y `step`.

Hasta entonces:

- PMI es un clasificador y modelo de diseño;
- la coálgebra effectful es otro modelo posible;
- el puente PMI → `Poly` → coálgebra permanece abierto.

## 7. Capacidades como orden, no como prueba de safety

Sea `Tool` el conjunto de capacidades nombradas por KORA. Sus subconjuntos
forman el retículo booleano:

```text
(P(Tool), ⊆).
```

Para un agente `a`, `D_a ⊆ Tool` es su declaración `herramientas`. Menor
conjunto significa menor autoridad declarada.

Para target `T` y contexto runtime `r`, definir:

```text
Eff_T(a,r) ⊆ Tool_T
```

como las capacidades efectivamente invocables, y un mapping tipado
`m_T : Tool ⇀ Tool_T`. La condición mínima de no amplificación es:

```text
Eff_T(a,r) ⊆ m_T[D_a]
```

para todo contexto `r` incluido en el alcance. La igualdad puede exigirse si
también importa disponibilidad completa; una inclusión estricta representa
pérdida funcional, no ampliación de autoridad.

Un allowlist en frontmatter, un deny parcial o una instrucción textual solo
prueban esta condición si el runtime los hace efectivos y se inspeccionan
también overrides, herencia, MCPs, skills y autoridad del proceso padre.
KORA declara honestamente las fronteras por target; no posee hoy una prueba
uniforme de `Eff_T`.

## 8. Safety como cierre

En una coálgebra `(U,c)`, sea `S ↪ U` el subobjeto de estados seguros. Safety
por invariancia requiere una estructura `s:S→H(S)` tal que:

```text
H(i) . s = c . i.
```

Con herramientas como salidas, también debe precisarse que el soporte
effectful de `step` permanece en acciones permitidas y estados de `S`. La
noción de soporte depende de `M`.

Esto separa tres afirmaciones:

1. **declaración de capacidad**: `D_a`;
2. **enforcement**: relación entre `Eff_T` y `D_a`;
3. **safety conductual**: cierre del invariante `S`.

Ninguna implica automáticamente las otras dos.

## 9. `estados` no es el estado coalgebraico

El campo `estados` actual es una lista ordenada de etiquetas de proceso. No
declara:

- alfabeto de eventos;
- aristas de transición;
- guards;
- acción;
- estado inicial o final;
- relación con memoria y contexto.

Por tanto no es una FSM ni el conjunto `U` de una coálgebra. Si se necesita
una FSM, el artefacto debe aportar un grafo de transición explícito; su
categoría libre de caminos puede construirse después. La lista puede seguir
siendo una guía de workflow sin recibir un estatus que no sostiene.

Tampoco debe confundirse `estado: activo` del lifecycle de autoría con el
estado interno de ejecución. Uno gobierna la vigencia del artefacto; el otro
pertenece a `Model(a)` o al runtime.

## 10. Preservación source → runtime

Sea:

```text
emit_T       : Spec(a) -> Product_T(a)
interpret_T  : Product_T(a) -> RuntimeModel_T(a)
model        : Spec(a) -> Model(a).
```

KORA solo implementa y prueba propiedades materiales de `emit_T`. Para
afirmar preservación conductual debe definirse `interpret_T` y un criterio que
compare `model(a)` con `RuntimeModel_T(a)`, por ejemplo:

- morfismo de coálgebras;
- bisimulación;
- inclusión/refinamiento de trazas;
- preservación de un conjunto explícito de observables.

El diagrama y sus hipótesis dependen del target. Igualdad byte a byte entre
emisión e instalación solo fija la entrada de `interpret_T`; no demuestra qué
hace el runtime con ella.

## 11. Matriz de testigos

| Afirmación | Testigo mínimo | Estado general en KORA |
|---|---|---|
| «tiene interfaz tipada» | `I`, `O`, schemas/protocolo y adaptadores | no está en el shape |
| «es coálgebra effectful» | `M`, `U`, `step` y acción functorial de `H` | modelo disponible; no instanciado por defecto |
| «preserva conducta» | morfismo coalgebraico o relación observacional definida | abierto por artefacto/target |
| «es bisimilar» | `R`, estructura/lifting e hipótesis sobre `H` | abierto |
| «compone con b» | puertos, wiring, álgebra semántica y efectos compatibles | `componible` solo declara candidato |
| «tools están limitadas» | evidencia de `Eff_T(a,r) ⊆ m_T[D_a]` | depende del runtime; no uniforme |
| «es seguro» | subobjeto `S` cerrado bajo transición | abierto |
| «la emisión preserva semántica» | `interpret_T` + diagrama de preservación | abierto |
| «PMI realiza pattern/matter» | objetos/morfismos en `Poly` y acción de módulo | abierto |

La ausencia de testigo obliga a bajar el enunciado a declaración, modelo,
heurística o metáfora. No autoriza completar la estructura por imaginación.

## 12. Decisión sobre el shape

Este contrato **no** añade `inputs`, `outputs`, `effects`, `transition` ni
`wiring` al frontmatter. Razones:

1. el shape plano no puede expresar con rigor schemas, guards o leyes;
2. los runtimes observados no comparten una semántica de efectos;
3. campos vacíos aparentarían formalización sin realización;
4. un contrato de evidencia debe nacer de al menos un caso operacional
   completo, no de una taxonomía anticipada.

El primer caso ya existe y confirma la forma documental mínima: referenciar
por URN un testigo versionado, no duplicar una teoría completa dentro del
frontmatter. Su observación ya está mecanizada para una superficie estrecha,
`codex exec --json`, pero depende de markers locales y cubre una sola
propiedad. Todavía no justifica ampliar el shape. La honestidad formal vale
más que la cobertura nominal.

## 13. Primer caso vertical

`urn:kora:kb:cat-caso-vertical-steipete-codex` instancia un caso estrecho:

```text
agente      steipete
target      Codex, modo persona
interfaz    eventos observables de trabajo
propiedad   no cerrar sin evidencia verde vigente
```

El objeto coalgebraico demostrado es un **monitor de trazas** con mónada de
excepciones, no el estado cognitivo completo de `steipete`. Para Codex CLI,
la proyección se mecaniza como una extensión por concatenación:

```text
o     : R_ok -> I*
obs_r : R_ok* -> I*
obs_r(r1 ... rn) = o(r1) ... o(rn).
```

Aquí `R_ok` contiene los registros JSONL bien formados que satisfacen el
protocolo local. La tarea del 2026-07-19 aporta una traza aceptada; ello es
evidencia de un caso, no una cuantificación sobre ejecuciones futuras.

Este primer testigo no justifica todavía ampliar el shape: la proyección solo
cubre `codex exec --json`; `estimate` y `feel-review` son autoatestados, y
`change` también puede serlo como fallback de escrituras shell. La propiedad
se limita a loop closure. Sí demuestra el patrón mínimo que debe seguir todo
caso futuro: tipos completos, transición total con efecto explícito,
invariante, prueba, test ejecutable y frontera runtime declarada.

## Fuentes primarias

- Eugenio Moggi, *Notions of computation and monads*:
  https://person.dibris.unige.it/moggi-eugenio/ftp/ic91.pdf
- J. J. M. M. Rutten, *Universal Coalgebra: a Theory of Systems*:
  https://fldit-www.cs.tu-dortmund.de/~peter/Rutten/UniversalCoalgebra.pdf
- H. Beohar et al., *Predicate and relation liftings for coalgebras with side
  effects*:
  https://arxiv.org/abs/2110.09911
- D. Vagner, D. I. Spivak y E. Lerman, *Algebras of Open Dynamical Systems on
  the Operad of Wiring Diagrams*:
  https://arxiv.org/abs/1408.1598
- S. Libkind y D. I. Spivak, *Pattern Runs on Matter*:
  https://arxiv.org/abs/2404.16321
