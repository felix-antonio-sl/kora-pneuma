# Reformulacion categorial — protocolo de traduccion

Antes de aplicar un patron del ICAS-BoK, **traducir el problema** del lenguaje de ingenieria al vocabulario categorial. El protocolo tiene cuatro pasos.

## Paso 1 — Proponer y comprobar una categoria

Una situacion concreta **puede** admitir un modelo categorial; no lo trae dado. Pregunta clave:

> "¿Cuales son los **objetos** y cuales los **morfismos** en este problema?"

Modelos candidatos:

| Situacion | Objetos | Morfismos |
|-----------|---------|-----------|
| arquitectura de servicios | servicios | llamadas/dependencias |
| schema relacional | tablas | foreign keys (generadores); ecuaciones de path |
| tipos en un lenguaje | tipos | funciones |
| computaciones con efectos de una mónada T | objetos A de la categoría base | flechas Kleisli A → T B |
| sistemas dinamicos | estados | transiciones / observaciones |
| agentes reactivos ya modelados | coálgebras `U -> H(U)` para un `H` fijo | morfismos coalgebraicos; no delegaciones |
| redes de agentes con interfaces | cajas/puertos tipados | wiring diagrams, si su composición y semántica están definidas |
| modelos de un sistema | versiones | migraciones |
| espacios de configuracion | configuraciones | refinamientos |

Antes de llamar categoria al modelo, comprueba tipos, identidades y composicion asociativa. Si no cierran, conserva el grafo, relacion o mapping mas debil que si este justificado; no fuerces una categoria.

## Paso 2 — Identificar la operacion en juego

¿Que se esta haciendo con esos objetos/morfismos? Patrones tipicos:

| Verbo del problema | Hipotesis categorial que conviene evaluar |
|--------------------|---------------------|
| "compongo X y luego Y" | composicion `g ∘ f` |
| "traduzco de X a Y" | candidato a funtor `F: X → Y`, si actua sobre morfismos y preserva las dos leyes |
| "X y Y son lo mismo" | elegir y demostrar el criterio pertinente: igualdad, isomorfismo, equivalencia o equivalencia observacional |
| "el resultado de combinar X e Y bajo Z" | preguntar si existe un problema universal de pullback, pushout, producto, coproducto o limite |
| "X queda determinado por sus relaciones" | Yoneda, hom-funtor, representabilidad |
| "X explota a Y; Y comprime a X" | posible adjuncion `X ⊣ Y`, solo con biyeccion natural o unidad/counit y leyes |
| "X tiene efecto colateral" | monada, Kleisli |
| "X observa estado interno" | comonada, coalgebra |
| "X corre sobre Y" | *Pattern Runs on Matter* solo tras construir los polinomios y las estructuras en `Poly` |
| "el agente A compone con B" | pedir puertos, wiring, álgebra semántica y compatibilidad de efectos; `componible` solo propone candidato |
| "el agente está limitado/seguro" | separar capacidad declarada, autoridad efectiva e invariante cerrado bajo transición |
| "X tiene grados de verdad" | empezar por un poset o algebra de Heyting; usar topos solo si se exhibe su estructura |
| "X dura en el tiempo" | posible presheaf/sheaf sobre un sitio temporal, con restricciones y pegado explicitos |

Cada verbo apunta a una pieza del corpus distinta.

## Paso 3 — Reformular la pregunta

Convertir la pregunta de ingenieria en una pregunta categorial. Ejemplos:

| Pregunta de ingenieria | Pregunta categorial |
|------------------------|---------------------|
| "¿por que el ORM pierde datos al deserializar?" | "¿existe un funtor bien tipado `relacional → objetos`? Si existe, ¿es fiel o pleno en los hom-sets relevantes? Si no, ¿que mapping concreto pierde que informacion?" |
| "¿como migro este schema sin romper datos?" | "¿hay un funtor `F: schema_viejo → schema_nuevo` que preserve constraints? ¿cual es la triple Sigma-Delta-Pi inducida?" |
| "¿como compongo dos servicios sin acoplarlos?" | "¿hay una categoria de servicios bien definida y un cospan tipado cuya propiedad universal produzca el pushout? Si no, ¿que contrato de interfaz basta?" |
| "¿como verifico que el refactor preservo el comportamiento?" | "¿que equivalencia observacional pide el sistema? Si hay coalgebras y lifting relacional explicitos, ¿existe una bisimulacion?" |
| "¿puedo encadenar estos agentes?" | "¿cuáles son sus interfaces tipadas y qué wiring con semántica functorial interpreta la conexión? ¿cómo combinan sus efectos y autoridad?" |
| "¿el allowlist hace seguro al agente?" | "¿qué capacidades son efectivas en runtime y qué subobjeto de estados seguros queda cerrado bajo la transición?" |
| "¿que tipo es el schema de mi base?" | "¿que categoria finitamente presentada modela este schema? ¿cuales son las path equivalences?" |
| "¿como modelo permisos ricos?" | "¿basta un reticulo/algebra de Heyting? Solo si no basta: ¿hay un topos identificado cuyo clasificador modela estos permisos?" |

## Paso 4 — Identificar la pieza del corpus

Con la pregunta categorial reformulada, consulta `disparadores-canonicos.md` o `mapa-corpus.md` para encontrar la pieza del ICAS-BoK que cubre el patron correspondiente.

Si la pregunta categorial no encuentra pieza:

1. Reformula otra vez con vocablo distinto. (max 2 iteraciones)
2. Si sigue sin encajar, el corpus no cubre el caso. Declarar.

## Heuristicas de buena reformulacion

- **No sobre-formalices**. Si la pregunta admite respuesta directa sin estructura, dala. La skill se activa cuando la estructura aporta.
- **Empieza por la categoria mas simple** que sirva. Si **Set** alcanza, usa **Set**. Si necesitas categoria enriquecida, declara la base.
- **Distingue lo formal de lo heuristico**. "Esto se parece a una monada" es heuristica; "esto cumple las leyes de monada porque ..." es formal.
- **Explicita lo que se pierde, si se pierde algo**. No presupongas perdida: identificala con un contraejemplo o una propiedad no preservada.
- **Elige el criterio de sameness requerido**. Igualdad, isomorfismo, equivalencia categorial y equivalencia observacional responden preguntas distintas.

## Anti-patrones de reformulacion

- "Esto es como un funtor pero no exactamente" → si no cumple las leyes, **no es funtor**. Llamarlo de otra forma.
- "Aplico monada al servicio X" → hay que identificar categoría base, endofuntor, unidad y multiplicación; la etiqueta de servicio no los determina.
- "El servicio Y es la identidad de Z" → la identidad es un morfismo `id: A → A`, no un servicio.
- "El refactor preserva todo" → declara la semantica observable y demuestra la equivalencia correspondiente; *faithful* por si solo no significa "preserva todo".
- "Esto vive en el topos de mi aplicacion" → declara la categoria, limites finitos, exponenciales y clasificador de subobjetos.
