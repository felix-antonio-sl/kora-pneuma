---
urn: urn:fxsl:kb:icas-topoi
nombre: icas-topoi
version: 1.1.0
estado: publicado
descripcion: "Pieza 12 del ICAS-BoK: topoi — presheaves, sheaves, clasificador de subobjetos, lógica intuicionista y morfismos geométricos; modelos condicionales para permisos, consistencia y multi-tenancy."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/12-topoi.md (sha256:6702052c2755d880d46a4af66bf9b434cd391191da7c3c8108c405ce4aafd46d) el 2026-06-12. Corrección 1.1.0 contrastada con Stacks Project, Sheafification, https://stacks.math.columbia.edu/tag/007X."
autor: FS
creado: 2026-04-14
lang: es
tags: [topos, logica-interna, sheaf, consistencia, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Topoi

## Cuando "verdadero o falso" no alcanza

Hay una pregunta que me persigue cada vez que modelo un sistema distribuido: ¿este feature flag esta habilitado? La respuesta deberia ser simple -- si o no. Pero en la practica la respuesta es: "si para el 20% de los usuarios en la region EU, no para el resto salvo el grupo canary que tiene su propia logica, y ademas hay un override por tenant que todavia no se propago a todos los nodos." Verdadero o falso no alcanza. Necesito un espacio de valores de verdad mas rico.

Un topos ofrece una semántica precisa para verdad interna dependiente del
contexto **cuando el dominio se representa en él**. Un feature-flag gradual o
distribuido no determina por sí solo ese topos.

## Presheaves: conjuntos que varian

Ya encontre los presheaves en el documento 04, cuando estudie Yoneda. Un presheaf sobre una categoria C es un funtor P : C^op -> Set. Para cada objeto c de C, tengo un conjunto P(c) de "secciones sobre c", y para cada morfismo f : c' -> c, tengo una funcion de restriccion P(f) : P(c) -> P(c') que dice como adaptar la informacion cuando cambio de perspectiva.

Lo que no aprecié plenamente en ese momento es que la categoria de presheaves [C^op, Set] se comporta asombrosamente parecido a Set. Tiene todos los limites y colimites. Tiene exponenciales -- puedo formar el "espacio de funciones" entre dos presheaves. Y tiene algo que Set tiene pero que damos por sentado: un clasificador de subobjetos.

En Set, el clasificador de subobjetos es el conjunto {true, false} con la inclusion true : 1 -> {true, false}. Cada subconjunto S de X corresponde a una unica funcion caracteristica chi_S : X -> {true, false}. Esto es lo que hace funcionar la logica clasica: cada proposicion es verdadera o falsa, punto.

Pero en `[C^op, Set]`, el clasificador de subobjetos `Omega` ya no es en
general un conjunto de dos elementos: `Omega(c)` es el conjunto de cribas
(*sieves*) sobre `c`. En el topos de sheaves sobre un espacio topológico,
`Omega(U)` se identifica con los abiertos contenidos en `U`. Los valores de
verdad son entonces contextuales: expresan dónde vale una proposición, no
grados probabilísticos de verdad.

## Sheaves: pegado local-a-global

No todo presheaf es igualmente bien comportado. Un presheaf es un sheaf cuando satisface la condicion de pegado: si tengo secciones locales que son compatibles en sus solapamientos, existe una unica seccion global que las extiende.

La definicion precisa, siguiendo a Schultz y Spivak, requiere la nocion de site -- una categoria C equipada con una coverage que dice que familias de morfismos "cubren" un objeto. Un sheaf sobre un site (C, chi) es un funtor B : C^op -> Set tal que para cada familia cubriente (f_i : U_i -> U), y cada familia compatible de secciones (b_i en B(U_i) que coinciden en las restricciones), existe un unico b en B(U) cuyas restricciones dan los b_i.

Esto puede modelar configuración distribuida después de definir un site de
contextos, restricciones y cobertura. Namespaces y ConfigMaps de Kubernetes no
aportan automáticamente esos datos, y un fallo de gluing matemático no
identifica por sí solo la causa operacional del conflicto.

La categoria de sheaves sobre un site se denota Shv(C, chi). El teorema clave: Shv(C, chi) es un topos.

## Que es un topos

Un topos E es una categoria que tiene:

1. Todos los limites finitos (productos, equalizadores, pullbacks)
2. Exponenciales (puedo formar el objeto de morfismos B^A)
3. Un subobject classifier Omega con un morfismo true : 1 -> Omega

Estas tres condiciones implican que E tiene tambien todos los colimites finitos. Set es el topos mas simple. [C^op, Set] es un topos para cualquier categoria pequena C. Shv(X) para un espacio topologico X es un topos. Cada uno con su propio Omega, su propia nocion de verdad.

La potencia de esta definicion es que un topos es simultaneamente:

- Un universo de "conjuntos generalizados" donde hacer matematica
- Una logica interna de orden superior con sus propias reglas de inferencia
- Un espacio donde las proposiciones tienen valores de verdad contextuales

## El clasificador de subobjetos como logica de permisos

Volvamos a los feature flags. En `Set`, `Omega = {true, false}`. Cada predicado
sobre un conjunto `X` es una función `X -> Omega`. Para proponer un topos de
configuración no basta inventar un conjunto de estados; habría que construir
la categoría/topología y calcular su clasificador. La siguiente lista es solo
un dominio operacional candidato, que además necesitaría un orden de Heyting
si se quisiera usar como álgebra de políticas:

```
Omega = {enabled, disabled, canary, percentage_10, percentage_50, rollback_pending}
```

Una política puede asignar esos estados a usuarios, pero eso no la convierte
todavía en mapa característico de un subobjeto. Si el dominio se realiza como
álgebra de Heyting o como valores de `Omega` en un topos concreto, las
operaciones lógicas quedan determinadas por esa estructura:

- La conjuncion (AND) de "canary" y "percentage_50" produce un valor que captura ambas restricciones
- La negacion de "enabled" no es simplemente "disabled" -- puede ser "rollback_pending"
- La implicacion "si canary entonces enabled" tiene semantica precisa

Un sistema de permisos **puede modelarse** mediante subobjetos de sujetos con
acceso. Su mapa característico toma valores en el `Omega` del topos elegido.
Los niveles `read/write/admin` no son automáticamente valores de ese
clasificador; pueden requerir un retículo de políticas adicional. Cuando el
modelo es un topos, conjunción, disyunción e implicación se interpretan en su
álgebra de Heyting interna.

## Logica intuicionista: lo que no se puede decidir

En la logica de un topos, el principio del tercero excluido (P ∨ ¬P = true) no vale en general. Esto no es un defecto -- es un feature. En un sistema distribuido, hay proposiciones que genuinamente no son ni verdaderas ni falsas en un momento dado. "El nodo X tiene el ultimo estado" puede ser indeterminado durante una particion de red. "La transaccion T se commiteo" puede estar en un estado intermedio durante el two-phase commit.

Fong y Spivak lo explican con el topos de sheaves sobre un espacio topologico. Ahi, la negacion de un abierto U es el interior del complemento: ¬U = int(X \ U). El doble negativo ¬¬U = int(X \ int(X \ U)) no es necesariamente igual a U -- puede ser mas grande. Por eso P ∨ ¬P no necesariamente cubre todo el espacio.

Para sistemas, la consistencia eventual **puede modelarse** con datos locales
sobre un site temporal, pero no es exactamente la condición de sheaf. El
«eventualmente» requiere dinámica/modalidad adicional; el pegado de un sheaf
es una propiedad estática del presheaf elegido.

## Morfismos geometricos: mapas entre universos

Si tengo dos topoi E y E', el mapa correcto entre ellos no es un simple funtor. Es un morfismo geometrico: un par de funtores adjuntos f* ⊣ f_* donde f* (la "imagen inversa") preserva limites finitos. Esta condicion extra -- preservar limites finitos, no solo ser adjunto izquierdo -- es lo que garantiza que el mapa respeta la estructura logica interna.

Una migración de configuración **puede** representarse por un morfismo
geométrico si se construyen los topoi y el par adjunto con imagen inversa
left-exact. Una migración de schema ordinaria no lo es por definición.

La sheafification es el adjunto izquierdo de la inclusión
`Sh(C,J) ↪ PSh(C)` para el site elegido. No se identifica en general con «la
Kan extension izquierda a lo largo de la inclusión del site». Tampoco repara
automáticamente un sistema distribuido: construye el sheaf asociado al
presheaf matemático, no la ejecución que hace verdaderos sus datos.

## El dominio de intervalos y el topos de comportamientos

Schultz y Spivak construyen algo que me parece esencial para la arquitectura de sistemas temporales. Definen el interval domain IR como el conjunto de intervalos cerrados acotados [d, u] en R, con el orden por refinamiento: [d', u'] ⊑ [d, u] si d ≤ d' y u' ≤ u. Un intervalo mas pequeno es una aproximacion mas precisa de un numero real. Los elementos maximales de IR son los puntos de R (intervalos de longitud cero).

El topos de sheaves sobre IR, Shv(IR), da un universo donde los "tipos" son familias de conjuntos que varian continuamente sobre el tiempo. Un tipo de comportamiento es un sheaf S sobre IR: para cada intervalo temporal [d, u], S([d, u]) es el conjunto de comportamientos posibles durante ese periodo. La condicion de sheaf dice que los comportamientos locales (sobre subintervalos) se pegan en comportamientos globales cuando son compatibles.

Pero hay un refinamiento crucial. El topos Shv(IR) depende de la posicion absoluta en la linea temporal. Un sistema bien disenado no deberia depender de cuando lo arrancas. Schultz y Spivak resuelven esto pasando a un universo de sheaves invariantes por traslacion. Una forma concreta de presentarlo es tomar el cociente de IR bajo la accion de traslacion de R, formar la categoria IR/▷, y escribir B = Shv(IR/▷). En el documento 15 reutilizo la misma intuicion con una notacion de cociente por la accion; aqui me basta fijar la idea: B modela comportamientos donde importa la duracion y el orden relativo, no el origen absoluto.

El clasificador de subobjetos de B no es binario. Como observan, codifica propiedades temporales: "siempre verdadero", "eventualmente verdadero", "verdadero hasta que..." -- estas no son hacks ad hoc sobre la logica clasica. Son los valores de verdad naturales de un universo donde el tiempo es parte de la estructura.

## Multi-tenancy como fibration de topoi

Un sistema multi-tenant **puede modelarse** mediante una fibración cuyas fibras
sean topoi, pero eso exige reindexación coherente y lifts cartesianos; agrupar
datos por tenant no basta.

En una fibración sobre una categoría `Tenant`, un morfismo
`f : t1 -> t2` induce reindexación entre fibras según la varianza elegida.
Que esa reindexación forme la imagen inversa de un morfismo geométrico exige
un adjunto derecho y preservación de límites finitos. Un pushforward o
extensión de Kan existe solo bajo hipótesis adicionales.

Los namespaces de Kubernetes motivan esa analogía, pero no son literalmente
topoi slice sin una categoría de recursos con límites, exponenciales y
clasificador de subobjetos adecuados.

## Corrección 1.1.0

Se separan sheafification, Kan extension y reconciliación dinámica, y se
condiciona la lectura fibrada/topos de multi-tenancy a las estructuras que
realmente exige.

## La leccion del topos

La lección rigurosa es condicional: cuando un dominio distribuido se presenta
como un site y sus datos satisfacen restricción y pegado, los sheaves separan
consistencia local de existencia/unicidad global. Si además se trabaja en su
topos, la lógica interna es intuicionista en general.

Feature flags, permisos, sincronización y consistencia eventual son problemas
operacionales que **pueden** beneficiarse de ese modelo. No son por definición
clasificadores, sheaves ni lógica intuicionista; el site, los subobjetos, la
dinámica y la correspondencia semántica deben construirse.
