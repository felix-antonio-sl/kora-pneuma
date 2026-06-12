# Reformulacion categorial — protocolo de traduccion

Antes de aplicar un patron del ICAS-BoK, **traducir el problema** del lenguaje de ingenieria al vocabulario categorial. El protocolo tiene cuatro pasos.

## Paso 1 — Identificar la categoria implicita

Toda situacion concreta vive en alguna categoria. Pregunta clave:

> "¿Cuales son los **objetos** y cuales los **morfismos** en este problema?"

Patrones de respuesta:

| Situacion | Objetos | Morfismos |
|-----------|---------|-----------|
| arquitectura de servicios | servicios | llamadas/dependencias |
| schema relacional | tablas | foreign keys (generadores); ecuaciones de path |
| tipos en un lenguaje | tipos | funciones |
| valores con efectos | tipos efectados (T A) | funciones Kleisli |
| sistemas dinamicos | estados | transiciones / observaciones |
| modelos de un sistema | versiones | migraciones |
| espacios de configuracion | configuraciones | refinamientos |

Si no logras identificar objetos y morfismos coherentes, el problema no es estructural y la skill no aplica.

## Paso 2 — Identificar la operacion en juego

¿Que se esta haciendo con esos objetos/morfismos? Patrones tipicos:

| Verbo del problema | Operacion categorial |
|--------------------|---------------------|
| "compongo X y luego Y" | composicion `g ∘ f` |
| "traduzco de X a Y" | funtor `F: X → Y` |
| "X y Y son lo mismo" | isomorfismo, equivalencia, transformacion natural invertible |
| "el resultado de combinar X e Y bajo Z" | pullback, pushout, producto, coproducto, limite |
| "X queda determinado por sus relaciones" | Yoneda, hom-funtor, representabilidad |
| "X explota a Y; Y comprime a X" | adjuncion `X ⊣ Y` |
| "X tiene efecto colateral" | monada, Kleisli |
| "X observa estado interno" | comonada, coalgebra |
| "X corre sobre Y" | pattern runs on matter (free monad sobre cofree comonad) |
| "X tiene grados de verdad" | topos, clasificador de subobjetos no-booleano |
| "X dura en el tiempo" | sheaf sobre dominio temporal |

Cada verbo apunta a una pieza del corpus distinta.

## Paso 3 — Reformular la pregunta

Convertir la pregunta de ingenieria en una pregunta categorial. Ejemplos:

| Pregunta de ingenieria | Pregunta categorial |
|------------------------|---------------------|
| "¿por que el ORM pierde datos al deserializar?" | "¿que axioma de funtor falla en la traduccion `relacional → objetos`? ¿composicion, identidad, faithful, full?" |
| "¿como migro este schema sin romper datos?" | "¿hay un funtor `F: schema_viejo → schema_nuevo` que preserve constraints? ¿cual es la triple Sigma-Delta-Pi inducida?" |
| "¿como compongo dos servicios sin acoplarlos?" | "¿cual es el coproducto en la categoria de servicios? ¿el pushout sobre la interfaz compartida?" |
| "¿como verifico que el refactor preservo el comportamiento?" | "¿son los servicios bisimilares? ¿las observaciones generadas por la coalgebra son las mismas?" |
| "¿que tipo es el schema de mi base?" | "¿que categoria finitamente presentada modela este schema? ¿cuales son las path equivalences?" |
| "¿como modelo permisos ricos?" | "¿estamos en un topos donde el clasificador de subobjetos no es 2 = {true, false}?" |

## Paso 4 — Identificar la pieza del corpus

Con la pregunta categorial reformulada, consulta `disparadores-canonicos.md` o `mapa-corpus.md` para encontrar la pieza del ICAS-BoK que cubre el patron correspondiente.

Si la pregunta categorial no encuentra pieza:

1. Reformula otra vez con vocablo distinto. (max 2 iteraciones)
2. Si sigue sin encajar, el corpus no cubre el caso. Declarar.

## Heuristicas de buena reformulacion

- **No sobre-formalices**. Si la pregunta admite respuesta directa sin estructura, dala. La skill se activa cuando la estructura aporta.
- **Empieza por la categoria mas simple** que sirva. Si **Set** alcanza, usa **Set**. Si necesitas categoria enriquecida, declara la base.
- **Distingue lo formal de lo heuristico**. "Esto se parece a una monada" es heuristica; "esto cumple las leyes de monada porque ..." es formal.
- **Explicita lo que se pierde**. Toda traduccion entre dominios pierde algo. Nombra que se pierde.
- **No confundas isomorfismo con igualdad**. La igualdad on-the-nose casi nunca es lo que se quiere; lo que se quiere es equivalencia.

## Anti-patrones de reformulacion

- "Esto es como un funtor pero no exactamente" → si no cumple las leyes, **no es funtor**. Llamarlo de otra forma.
- "Aplico monada al servicio X" → las monadas no se aplican a servicios; se aplican a categorias de tipos efectados.
- "El servicio Y es la identidad de Z" → la identidad es un morfismo `id: A → A`, no un servicio.
- "El refactor preserva todo" → si no demuestras que algun funtor faithful preserva la estructura relevante, no preservas todo.
- "Esto vive en el topos de mi aplicacion" → declara cual topos, sus aberturas/cierres, su clasificador.
