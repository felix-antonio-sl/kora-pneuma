---
urn: urn:kora:kb:cat-contrato-ingenieria-agentica
nombre: cat-contrato-ingenieria-agentica
version: 1.5.0
estado: publicado
descripcion: "Contrato de rigor para ingeniería agéntica en KORA: testigos mínimos para interfaces, coálgebras con efectos, equivalencia conductual, composición por cableado, capacidades, safety y preservación en runtime."
fuente: "Doctrina propia pneuma formalizada el 2026-07-18. Fuentes primarias: Rutten, Universal Coalgebra, https://fldit-www.cs.tu-dortmund.de/~peter/Rutten/UniversalCoalgebra.pdf; Beohar et al., Predicate and relation liftings for coalgebras with side effects, https://arxiv.org/abs/2110.09911; Vagner, Spivak y Lerman, Algebras of Open Dynamical Systems on the Operad of Wiring Diagrams, https://arxiv.org/abs/1408.1598; Libkind y Spivak, Pattern Runs on Matter, https://arxiv.org/abs/2404.16321. Las versiones v1.1.0-v1.4.0 desarrollaron el caso Steipete-Codex, autoridad efectiva y la monografía integrada; Git conserva el detalle. v1.5.0 (2026-08-09): depreca el caso runtime versionado como gate general y conserva solo sus conclusiones epistémicas."
autor: FS
creado: 2026-07-18
lang: es
tags: [ingenieria-agentica, teoria-categorias, coalgebra, efectos, composicion, safety, kora]
familia: bok
depende: [urn:kora:kb:cat-agent-coalgebra, urn:kora:kb:cat-agent-modulo, urn:kora:kb:cat-kora-semantica-operacional, urn:fxsl:kb:icas-escala]
cita: [urn:kora:kb:cat-programacion-agentica-autonoma]
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

como las capacidades efectivamente invocables. La traducción entre nombres
fuente y familias target no tiene por qué ser univaluada: una escritura puede
realizarse mediante una tool de parche o mediante shell, y varias tools fuente
pueden colapsar en la misma familia runtime. Por tanto el testigo general es
una **relación tipada**, no un funtor ni una función forzada:

```text
R_T ⊆ Tool × Tool_T
R_T[D] = { q ∈ Tool_T | existe p ∈ D : (p,q) ∈ R_T }.
```

Una función parcial `m_T : Tool ⇀ Tool_T` es solo el caso especial en que
`R_T` es univaluada. La condición mínima de no amplificación es:

```text
Eff_T(a,r) ⊆ R_T[D_a]
```

para todo contexto `r` incluido en el alcance. La igualdad puede exigirse si
también importa disponibilidad completa; una inclusión estricta representa
pérdida funcional, no ampliación de autoridad.

Una traza finita `τ` aporta únicamente éxitos observados:

```text
Succ_T(a,r,τ) ⊆ Eff_T(a,r).
```

Para una familia finita de sonda `P ⊆ Tool_T`, basta un elemento de

```text
Succ_T(a,r,τ) ∩ P - R_T[D_a]
```

para refutar la no amplificación en ese contexto. La ausencia de tal elemento
solo significa **sin amplificación observada**; no demuestra la inclusión de
`Eff_T`. Un sobre de configuración resuelto `Cfg_T(r)` puede estrechar la cota

```text
Succ_T(a,r,τ) ⊆ Eff_T(a,r) ⊆ Cfg_T(r),
```

pero solo para controles que el runtime aplica realmente. Tool ausente,
intento denegado, fallo de autenticación y tool disponible no usada son
estados distintos y no deben colapsarse.

`Cfg_T(r)` solo puede usarse como cota si el runtime resuelve y atestigua esa
superficie. Unir por cuenta propia listas de configuración, features, plugins,
MCPs o tools dinámicas no produce necesariamente el conjunto visible al
modelo: sin una regla oficial de resolución sería un manifiesto sintético.

La separación sigue siendo necesaria aunque todas las respuestas provengan
del mismo proceso. Por ejemplo, para un App Server puede haber:

```text
CapProv(r) ∈ 2^K
McpInv(r)  = Σ (s : Server_r). Tool_s
A(r)       = tools finalmente visibles al modelo, si el runtime las atestigua
```

`CapProv(r)` clasifica capacidades del proveedor y `McpInv(r)` es un inventario
MCP etiquetado por servidor. Son objetos de tipos distintos. Sin mapas de
comparación ni un operador de resolución documentado hacia `A(r)`, no existe
base para identificar una unión, producto, coproducto o colímite de
inventarios con la autoridad visible al modelo. La mera coexistencia de
endpoints no aporta esa estructura.

Cuando no existe ese manifiesto, todavía puede fijarse un contrato operacional
versionado. Sea `Raw_C` el conjunto de ejecuciones recolectadas,
`norm_C:Raw_C⇀E_C` un normalizador parcial y `Sat_C:E_C→2` un predicado
decidible sobre recibos finitos normalizados. Una precondición o traza inválida
queda fuera del dominio de `norm_C`; sobre su dominio, `Sat_C(e)=1` prueba
únicamente que el recibo pertenece al subobjeto `S_C ↪ E_C`. No identifica
`Cfg_T(r)`, no enumera `Eff_T(a,r)` y no convierte ausencia de éxito observado
en ausencia de autoridad.

Este contrato compara **familias de capacidad nombradas**. No debe confundirse
con autoridad por efecto y recurso. Para esta última harían falta, como
mínimo, operaciones, recursos, scopes y modos explícitos —por ejemplo
lectura/escritura, path o dominio, alcance y local/remoto— más la política que
los ordena. `Bash` sin scope puede realizar filesystem y red; observar una
familia `web_search` adicional refuta la inclusión entre nombres, pero no
demuestra por sí solo un efecto de red que `Bash` no tuviera ya. El shape
actual no permite formular esa proposición más fuerte.

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
| «tools están limitadas» | evidencia de `Eff_T(a,r) ⊆ R_T[D_a]` | depende del runtime; el antecedente Codex aportó un contraejemplo y el contrato endurecido solo probó su recibo |
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

El primer caso histórico confirmó la forma documental mínima: referenciar por
URN un testigo acotado, no duplicar una teoría completa dentro del
frontmatter. También mostró que un monitor ligado a markers y versiones
locales no debe convertirse en gate permanente del repositorio. La honestidad
formal vale más que la cobertura nominal.

## 13. Antecedente vertical deprecado

`urn:kora:kb:cat-caso-vertical-steipete-codex` conserva el antecedente de una
observación estrecha de Steipete sobre Codex. Su resultado válido fue
epistémico: una traza finita no prueba ejecuciones futuras; una declaración de
tools no determina autoridad efectiva; un contrato endurecido prueba su
recibo, no safety universal.

El monitor y los probes ligados a aquel runtime fueron retirados de la suite
general cuando dejaron de representar una frontera vigente. Un nuevo testigo
runtime debe vivir junto a su consumidor, declarar versión e invariante y
ejecutarse focalmente. El antecedente no justifica ampliar el shape ni imponer
sus gates a cambios ordinarios de KORA.

## 14. Recorrido integrado de programación agéntica

`urn:kora:kb:cat-programacion-agentica-autonoma` reúne este contrato y las
URNs conceptuales en una monografía continua. Es la entrada adecuada cuando
un problema cruza más de una tensión; no reemplaza las piezas atómicas ni las
fuentes primarias que sostienen una afirmación formal.

| Problema | Recorrido en la monografía | Testigos que deben salir |
|---|---|---|
| plan, effects y loop | capítulos 3, 5 y 6 | `I`, `O`, `U`, `M`, `step`, signatura e intérprete |
| composición y delegación | capítulos 10 a 12 | puertos, adaptadores, protocolo, autoridad, misión y receipt |
| evals y tiempo | capítulos 13 y 14 | observables, equivalencia, cobertura, safety, liveness y cancelación |
| adecuación y lifecycle | capítulos 16 y 17 | separación Spec/Model/Runtime, ledger, snapshot, gate y publicación |
| diseño completo y refutación | capítulos 18 y 19 | instancia acotada, invariante, Goal, contraejemplo y claims calibrados |

Cada claim agéntico atómico usa una clase de naturaleza:

- `F`: formal, dentro de una estructura matemática y con prueba o fuente
  primaria precisa;
- `E`: observación empírica reproducible y acotada;
- `M`: relación de modelado bajo hipótesis explícitas;
- `H`: heurística de ingeniería refutable;
- `X`: analogía, conjetura o frontera de investigación.

Las clases no forman una escalera. Fuerza formal, evidencia runtime y
adecuación al dominio son coordenadas separadas. En el vocabulario abreviado
de `cat-thinking`, `X` contiene la lectura metafórica y `E` se reporta como
evidencia, no como estatus matemático.

La sección 11.5 de la monografía conserva un antecedente retirado sobre
delegación jerárquica en `Poly`; su nota editorial lo degrada a `X`. Para
decisiones operativas mandan el contrato de misión, el protocolo, el wiring y
la autoridad efectiva, no aquella construcción.

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
- OpenAI, *Codex non-interactive mode*:
  https://learn.chatgpt.com/docs/non-interactive-mode
- OpenAI, *Codex App Server*:
  https://learn.chatgpt.com/docs/app-server
