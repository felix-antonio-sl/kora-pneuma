---
urn: urn:kora:kb:cat-kora-semantica-operacional
nombre: cat-kora-semantica-operacional
version: 1.0.0
estado: publicado
descripcion: "Semántica formal mínima de las operaciones de KORA: snapshots válidos como subobjetos, lifecycle como cadenas delgadas con gates parciales, fidelidad contravariante y frontera no categorial de censo, emisión, paridad, ley y koraficación."
fuente: "Doctrina propia pneuma formalizada el 2026-07-18 desde kora.py y ley/0..4. Base primaria: Riehl, Category Theory in Context, https://emilyriehl.github.io/files/context.pdf. Las propiedades específicas de KORA se demuestran aquí y se verifican en tests/test_kora.py."
autor: FS
creado: 2026-07-18
lang: es
tags: [kora, semantica-operacional, teoria-categorias, lifecycle, validacion, fidelidad]
familia: bok
depende: [urn:kora:kb:cat-kora-kernel]
---

# Semántica operacional mínima de KORA

## 1. Alcance

Este documento tipa **todo gesto vigente de KORA** con la estructura más débil
que lo explica. No intenta convertir toda función en funtor.

La teoría de categorías aporta valor cuando hace visibles composición,
identidad, orden, universalidad o preservación. Una función puede convertirse
formalmente en funtor entre categorías discretas, pero esa construcción no
explica nada: elimina precisamente los morfismos cuya preservación interesaría.
KORA rechaza esa «categorificación por vaciamiento».

El estatus de cada resultado es uno de:

- **formal**: construcción y leyes demostradas;
- **operacional probado**: propiedad del programa cubierta por tests;
- **declarado**: contrato normativo sin prueba mecánica;
- **abierto**: faltan tipos o leyes para formular la afirmación.

## 2. Dominios observados

Sea `R` el conjunto de snapshots finitos, legibles y regulares del árbol KORA
en los paths que observa el núcleo. Un snapshot fija paths, tipos de nodo y
bytes; cambios concurrentes durante una invocación quedan fuera de este modelo.

Se distinguen además:

```text
A(R)   lista de artefactos parseados o errores de parse
E_T    mapas finitos path-relativo -> bytes emitidos para el target T
W_T    snapshots de la frontera runtime de nivel usuario observada para T
D_i    listas finitas de diagnósticos del check i
```

`W_T` no forma parte de la fuente de verdad: solo la observa `paridad`.
`--aplicar` la muta bajo gates de propiedad y alcance.

Esta separación impide confundir tres clases de igualdad:

1. igualdad de fuente en `R`;
2. igualdad byte a byte de productos en `E_T`;
3. equivalencia de conducta de un runtime, que KORA no define.

## 3. Atlas de operaciones

| Superficie | Tipo mínimo | Estatus |
|---|---|---|
| parsear y derivar tipo | función parcial bytes → campos+cuerpo+tipo, totalizada con diagnósticos de contenido | operacional |
| `censo` | función derivada `R → List(Entry)` | operacional; no funtor sustantivo |
| `nombre` | lookup parcial `Valid × URN ⇀ Entry` | formal como función parcial bajo unicidad |
| `velar` | familia de predicados sobre `R` | subobjetos formales en `Set` |
| `ciclo` | flechas de dos cadenas delgadas + transformaciones parciales de snapshots | formal en estados; parcial en snapshots |
| relaciones | grafos generadores y categorías libres de caminos | formal como construcción derivada |
| proyección de firma | coreflector `P_T : D_T → I_T` | formal |
| fidelidad por demanda | funtor `C_e^op → Q` | formal para matrices vigentes |
| emisión | compilador parcial determinista `R ⇀ E_T` | operacional; no funtor demostrado |
| `--aplicar` | mutación parcial `E_T × W_T ⇀ W_T` | operacional, gobernada por gates |
| paridad | predicado/clasificador sobre `E_T × W_T` | igualdad material gestionada |
| `ley` | concatenación parcial de archivos normativos | operacional; no construcción categorial |
| koraficación | proceso editorial gobernado | declarado; no funtor |

## 4. Validación como intersección de subobjetos

Cada check base determina una función:

```text
q_i : R -> D_i
```

El snapshot pasa el check exactamente cuando `q_i(r) = []`. Sea:

```text
Valid_i = {r en R | q_i(r) = []}
Valid   = intersección de Valid_i, para i en CHECKS
```

Cada inclusión `Valid_i ↪ R` es un monomorfismo en `Set`. La inclusión
`Valid ↪ R` es el meet finito de esos subobjetos: expresa rigurosamente que
`velar` exige la conjunción de todos los checks, sin otorgar semántica de
verdad al cuerpo Markdown.

Para `q_pub = publicacion-digna`:

```text
StrictValid = Valid ∩ {r | q_pub(r) = []}
```

Por construcción:

```text
StrictValid ⊆ Valid.
```

La suite verifica que `velar --estricto` conserva sin modificación la familia
base y añade exactamente `q_pub`. Esto es una afirmación sobre forma y
dignidad declarativa, no sobre verdad factual, safety ni comportamiento.

## 5. Censo y resolución

La carga y el censo son funciones deterministas del snapshot:

```text
load  : R -> List(Artifact + ParseError)
censo : R -> List(Entry).
```

La lista se ordena por `(URN,path)`. No es autoridad ni objeto universal.

En `Valid`, `nombre-verdadero` garantiza unicidad de URN; por ello:

```text
resolver : Valid × URN ⇀ Artifact
```

es una función parcial: devuelve el único artefacto cuando existe. Fuera de
`Valid`, el procedimiento sigue siendo determinista, pero un primer match no
constituye resolución nominal bien definida si existen duplicados.

`censo --huerfanos` calcula candidatos no alcanzados por las aristas
materializadas y por una búsqueda limitada en la ley. Como las raíces de
consumo directo y las citas de prosa no forman un grafo completo, el reporte
es una heurística operacional, no una prueba de inaccesibilidad.

## 6. Lifecycle: categoría de estados y operación parcial

Con el orden reflexivo inducido por su posición, las cadenas:

```text
L_K = borrador <= publicado <= deprecado
L_A = borrador <= activo <= deprecado <= retirado
```

son categorías delgadas. Existe una única flecha `x → y` cuando `x ≤ y`;
identidad y composición son reflexividad y transitividad.

El CLI `ciclo` realiza solo flechas **no identidad** `x < y`: rechazar
`x → x` evita una escritura sin transición, aunque la identidad siga
existiendo en la categoría semántica.

Para cada avance `x < y`, sea:

```text
C_xy : R_x ⇀ R_y
```

la reescritura parcial que sustituye únicamente el valor de `estado`. En el
dominio común de definición y para `x < y < z`:

```text
C_yz(C_xy(r)) = C_xz(r).
```

La igualdad resulta de que ambas rutas dejan todos los bytes salvo `estado`
intactos y terminan con el mismo valor. La suite verifica el camino compuesto
y el salto directo.

No obstante, `x ↦ R_x` y las `C_xy` **no forman hoy un funtor total hacia una
categoría de mapas parciales**. El contraejemplo es intencional:

- `borrador → deprecado` puede jubilar una fuente incoherente sin gate;
- `borrador → activo → deprecado` exige primero promoción y puede fallar.

Las dos flechas hacia `deprecado` tienen dominios distintos. Fingir igualdad
de mapas parciales ocultaría la política de retiro. La formulación correcta
es: categoría delgada en el nivel de estados, acción operacional parcial y
coherencia solo en el dominio común.

La promoción a `publicado` o `activo` exige:

1. snapshot actual aprobado por `velar --estricto`;
2. `publicacion-digna` evaluada como si el artefacto ya estuviera en el estado
   destino;
3. escritura solo después de ambos gates.

Esta segunda condición evita validar el borrador y publicar un destino que
nunca fue sometido a sus obligaciones propias.

## 7. Relaciones

Cada uno de los campos `cita`, `depende`, `reemplaza`, `refina`,
`conocimiento` y `componible` declara su **propio** grafo generador. No se
mezclan etiquetas semánticamente distintas en una sola categoría.

Para un campo `r`, `Path(G_r)` es la categoría libre:

- objetos: URNs;
- flechas: caminos finitos de aristas `r`;
- identidad: camino vacío;
- composición: concatenación.

`velar` valida generadores, no materializa caminos. En los DAG declarados,
la alcanzabilidad reflexiva induce un orden parcial. En particular, un camino
de `componible` sigue siendo un camino de **declaraciones de compatibilidad**:
no es una composición de agentes, efectos o conductas.

## 8. Proyección y fidelidad

La coreflexión de firmas está demostrada en
`urn:kora:kb:cat-kora-kernel`. Las matrices portan además un invariante
independiente.

Sea la cadena de fidelidad:

```text
Q = {none <= partial <= full}.
```

Para cada target `T` y eje `e`, sea `C_e` la cadena completa de demandas
fuente y:

```text
fid_Te : C_e^op -> Q.
```

**Proposición.** `fid_Te` es un funtor entre categorías delgadas.

**Prueba.** Para toda demanda `x ≤ y`, las matrices vigentes satisfacen
`fid_Te(y) ≤ fid_Te(x)`: pedir más nunca mejora la fidelidad. Esto equivale a
monotonía desde la cadena opuesta. Un mapa monótono entre posets preserva
identidades y composición. La suite enumera todas las celdas de todos los
targets y ejes. ∎

Para `sigma`, con techo `c_T`:

```text
fid_Tsigma(s) = full     si s <= c_T
                partial  en otro caso.
```

También es antítona sobre el producto `[0,3]^5` y, por tanto, functorial desde
su opuesto a `Q`.

La fidelidad es dato legislado y contrastado con el runtime; no se deduce solo
del ordinal proyectado. Por ejemplo, preservar un número puede seguir siendo
`partial` si el runtime no realiza toda su semántica. Sí se exige:

```text
full  implica proyección numérica idéntica
none  implica no proyectable
no-full implica razón explícita.
```

## 9. Emisión, aplicación y paridad

Para una fuente válida y target declarado, la emisión es una función parcial
determinista:

```text
emit_T : R ⇀ E_T.
```

KORA prueba:

- mismos bytes de fuente y mismo generador producen los mismos factores;
- el sello atribuye `(URN,target)` y hash de fuente;
- la regeneración reproduce paths y bytes, incluida la fibra de referencias;
- toda pérdida conocida queda declarada.

No hay una categoría de artefactos, una categoría de productos runtime ni
acción sobre morfismos. Por tanto `emit_T` no se promueve a funtor mediante
categorías discretas ad hoc.

`--aplicar` es una mutación parcial gobernada por estado, alcance, ownership,
roster y topología segura. No es la counit de la coreflexión ni un lift.

La paridad compara el submapa de paths que KORA gestiona:

```text
eq_T(e,w)  sii  frontera_gestionada(w) = e
```

con reglas explícitas para superficies cerradas, abiertas, ausentes y
residuales. `fiel` prueba igualdad material atribuida; no prueba equivalencia
observacional, bisimulación, naturalidad ni enforcement de herramientas.

## 10. Ley y koraficación

`ley` concatena una secuencia fija de archivos si todos existen. El orden es
normativo, pero la operación es concatenación textual; no requiere ni obtiene
una construcción categorial.

La koraficación relaciona una fuente documental con un artefacto mediante
preservación de hechos, `FS` y compresión. Mientras la fuente, los hechos y
las transformaciones admisibles no formen categorías con acción sobre
morfismos, «funtor K» permanece nombre histórico. `FS=100%` es obligación
editorial declarada, no propiedad verificada por `velar`.

## 11. Frontera de no invención

KORA no afirma actualmente:

- un funtor artefacto → runtime para la emisión completa;
- una adjunción entre emisión e ingesta;
- una transformación natural entre targets;
- una bisimulación fuente/runtime;
- una composición Kleisli inducida por `componible`;
- una categoría sustantiva para `censo`, `nombre`, `ley` o koraficación.

Una futura ampliación deberá exhibir primero objetos, morfismos, acción y leyes,
y demostrar que la estructura responde a una pregunta operacional real.

## Fuente primaria

- Emily Riehl, *Category Theory in Context*, §§1.3 y 4.1:
  https://emilyriehl.github.io/files/context.pdf
