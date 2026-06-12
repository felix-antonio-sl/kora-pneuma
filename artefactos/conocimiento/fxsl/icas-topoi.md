---
urn: urn:fxsl:kb:icas-topoi
nombre: icas-topoi
version: 1.0.0
estado: publicado
descripcion: "Pieza 12 del ICAS-BoK: topoi — presheaves, sheaves, clasificador de subobjetos, lógica intuicionista y morfismos geométricos; verdad no binaria, permisos ricos, eventual consistency y multi-tenancy."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/12-topoi.md (sha256:6702052c2755d880d46a4af66bf9b434cd391191da7c3c8108c405ce4aafd46d) el 2026-06-12; cuerpo byte-fiel. Fuente original: ICAS-BoK corpus — Fong/Spivak, Mac Lane, Barbosa, Awodey, Riehl"
autor: FS
creado: 2026-04-14
lang: es
tags: [topos, logica-interna, sheaf, consistencia, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Topoi

## Cuando "verdadero o falso" no alcanza

Hay una pregunta que me persigue cada vez que modelo un sistema distribuido: ¿este feature flag esta habilitado? La respuesta deberia ser simple -- si o no. Pero en la practica la respuesta es: "si para el 20% de los usuarios en la region EU, no para el resto salvo el grupo canary que tiene su propia logica, y ademas hay un override por tenant que todavia no se propago a todos los nodos." Verdadero o falso no alcanza. Necesito un espacio de valores de verdad mas rico.

Durante anos trate esto como un problema de ingenieria -- mas flags, mas condiciones, mas tablas de decisiones. Pero resulta que hay una estructura matematica que captura exactamente esta situacion: el topos. Y lo que descubri al estudiarlo es que los topoi no son una generalizacion exotica de la teoria de conjuntos. Son la herramienta correcta para razonar sobre sistemas donde la verdad depende del contexto.

## Presheaves: conjuntos que varian

Ya encontre los presheaves en el documento 04, cuando estudie Yoneda. Un presheaf sobre una categoria C es un funtor P : C^op -> Set. Para cada objeto c de C, tengo un conjunto P(c) de "secciones sobre c", y para cada morfismo f : c' -> c, tengo una funcion de restriccion P(f) : P(c) -> P(c') que dice como adaptar la informacion cuando cambio de perspectiva.

Lo que no aprecié plenamente en ese momento es que la categoria de presheaves [C^op, Set] se comporta asombrosamente parecido a Set. Tiene todos los limites y colimites. Tiene exponenciales -- puedo formar el "espacio de funciones" entre dos presheaves. Y tiene algo que Set tiene pero que damos por sentado: un clasificador de subobjetos.

En Set, el clasificador de subobjetos es el conjunto {true, false} con la inclusion true : 1 -> {true, false}. Cada subconjunto S de X corresponde a una unica funcion caracteristica chi_S : X -> {true, false}. Esto es lo que hace funcionar la logica clasica: cada proposicion es verdadera o falsa, punto.

Pero en [C^op, Set], el clasificador de subobjetos Omega ya no es un conjunto de dos elementos. Para un presheaf sobre un espacio topologico, Omega(U) es el conjunto de abiertos contenidos en U. Los valores de verdad son abiertos -- regiones donde una proposicion vale. Una proposicion puede ser verdadera en una region y falsa en otra, y eso no es ambigüedad: es la estructura correcta.

## Sheaves: pegado local-a-global

No todo presheaf es igualmente bien comportado. Un presheaf es un sheaf cuando satisface la condicion de pegado: si tengo secciones locales que son compatibles en sus solapamientos, existe una unica seccion global que las extiende.

La definicion precisa, siguiendo a Schultz y Spivak, requiere la nocion de site -- una categoria C equipada con una coverage que dice que familias de morfismos "cubren" un objeto. Un sheaf sobre un site (C, chi) es un funtor B : C^op -> Set tal que para cada familia cubriente (f_i : U_i -> U), y cada familia compatible de secciones (b_i en B(U_i) que coinciden en las restricciones), existe un unico b en B(U) cuyas restricciones dan los b_i.

Esto es exactamente el patron de configuracion distribuida. En Kubernetes, cada namespace tiene su ConfigMap local. Cuando dos namespaces comparten un servicio, sus configuraciones deben ser compatibles en la interfaz. La condicion de sheaf dice: si todas las configuraciones locales son mutuamente compatibles, se pueden pegar en una configuracion global consistente. Si no se pueden pegar, es porque hay un conflicto genuino en los solapamientos -- y el formalismo te obliga a enfrentarlo.

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
- Un espacio donde las proposiciones tienen grados de verdad contextuales

## El clasificador de subobjetos como logica de permisos

Volvamos a los feature flags. En Set, Omega = {true, false}. Cada predicado sobre un conjunto X es una funcion X -> {true, false}. En mi topos de configuracion, puedo definir un Omega mas rico (en rigor, Omega necesita estructura de algebra de Heyting para que la logica interna funcione -- lo que sigue es una ilustracion del principio, donde los valores de verdad capturan estados mas finos que true/false):

```
Omega = {enabled, disabled, canary, percentage_10, percentage_50, rollback_pending}
```

Un subobjeto de "usuarios con acceso al feature F" ya no es un subconjunto binario. Es un morfismo que asigna a cada usuario un valor de verdad matizado. Y las operaciones logicas se adaptan:

- La conjuncion (AND) de "canary" y "percentage_50" produce un valor que captura ambas restricciones
- La negacion de "enabled" no es simplemente "disabled" -- puede ser "rollback_pending"
- La implicacion "si canary entonces enabled" tiene semantica precisa

El patron de access control encaja naturalmente. Un sistema de permisos es un clasificador de subobjetos sobre la categoria de recursos. Para cada recurso, Omega clasifica el nivel de acceso: read, write, admin, owner, denied, conditional. La composicion de permisos (el AND y el OR logico) se calcula internamente en Omega. Y lo crucial: esta logica es intuicionista.

## Logica intuicionista: lo que no se puede decidir

En la logica de un topos, el principio del tercero excluido (P ∨ ¬P = true) no vale en general. Esto no es un defecto -- es un feature. En un sistema distribuido, hay proposiciones que genuinamente no son ni verdaderas ni falsas en un momento dado. "El nodo X tiene el ultimo estado" puede ser indeterminado durante una particion de red. "La transaccion T se commiteo" puede estar en un estado intermedio durante el two-phase commit.

Fong y Spivak lo explican con el topos de sheaves sobre un espacio topologico. Ahi, la negacion de un abierto U es el interior del complemento: ¬U = int(X \ U). El doble negativo ¬¬U = int(X \ int(X \ U)) no es necesariamente igual a U -- puede ser mas grande. Por eso P ∨ ¬P no necesariamente cubre todo el espacio.

Para la practica de sistemas: la eventual consistency es exactamente una condicion de sheaf sobre el tiempo. Los datos locales son consistentes en cada nodo. La condicion de pegado dice: eventualmente, las vistas locales se reconcilian en una vista global. Pero "eventualmente" es un operador modal, no una garantia instantanea. La logica intuicionista captura esto: "sera verdadero" no es lo mismo que "es verdadero ahora."

## Morfismos geometricos: mapas entre universos

Si tengo dos topoi E y E', el mapa correcto entre ellos no es un simple funtor. Es un morfismo geometrico: un par de funtores adjuntos f* ⊣ f_* donde f* (la "imagen inversa") preserva limites finitos. Esta condicion extra -- preservar limites finitos, no solo ser adjunto izquierdo -- es lo que garantiza que el mapa respeta la estructura logica interna.

En la practica, un morfismo geometrico entre topoi de configuracion es una migracion de esquema que preserva las relaciones logicas entre las configuraciones. No basta con mapear datos de un formato a otro; hay que garantizar que las restricciones de consistencia se preservan.

La relacion con lo que vi en el documento 10 es directa: la sheafification -- el proceso de convertir un presheaf en el sheaf mas cercano -- es el adjunto izquierdo de la inclusion Shv(C) ↪ [C^op, Set]. Es una Kan extension izquierda a lo largo de la inclusion del site. Cada vez que tengo un presheaf (datos locales sin garantia de pegado) y quiero forzar consistencia global, sheafifico: proyecto al universo donde la condicion de sheaf se cumple automaticamente.

## El dominio de intervalos y el topos de comportamientos

Schultz y Spivak construyen algo que me parece esencial para la arquitectura de sistemas temporales. Definen el interval domain IR como el conjunto de intervalos cerrados acotados [d, u] en R, con el orden por refinamiento: [d', u'] ⊑ [d, u] si d ≤ d' y u' ≤ u. Un intervalo mas pequeno es una aproximacion mas precisa de un numero real. Los elementos maximales de IR son los puntos de R (intervalos de longitud cero).

El topos de sheaves sobre IR, Shv(IR), da un universo donde los "tipos" son familias de conjuntos que varian continuamente sobre el tiempo. Un tipo de comportamiento es un sheaf S sobre IR: para cada intervalo temporal [d, u], S([d, u]) es el conjunto de comportamientos posibles durante ese periodo. La condicion de sheaf dice que los comportamientos locales (sobre subintervalos) se pegan en comportamientos globales cuando son compatibles.

Pero hay un refinamiento crucial. El topos Shv(IR) depende de la posicion absoluta en la linea temporal. Un sistema bien disenado no deberia depender de cuando lo arrancas. Schultz y Spivak resuelven esto pasando a un universo de sheaves invariantes por traslacion. Una forma concreta de presentarlo es tomar el cociente de IR bajo la accion de traslacion de R, formar la categoria IR/▷, y escribir B = Shv(IR/▷). En el documento 15 reutilizo la misma intuicion con una notacion de cociente por la accion; aqui me basta fijar la idea: B modela comportamientos donde importa la duracion y el orden relativo, no el origen absoluto.

El clasificador de subobjetos de B no es binario. Como observan, codifica propiedades temporales: "siempre verdadero", "eventualmente verdadero", "verdadero hasta que..." -- estas no son hacks ad hoc sobre la logica clasica. Son los valores de verdad naturales de un universo donde el tiempo es parte de la estructura.

## Multi-tenancy como fibration de topoi

Quiero conectar esto con una estructura que ya conozco del documento 10. En un sistema multi-tenant, cada tenant tiene su propio "universo" de datos, esquemas y reglas de negocio. Puedo modelar esto como una fibration de topoi: un funtor p : E -> B donde B es la categoria de tenants y cada fibra p^{-1}(t) es el topos del tenant t.

Los morfismos en B (migraciones de tenant, merges de cuentas) inducen morfismos geometricos entre las fibras. El reindexing a lo largo de un morfismo f : t1 -> t2 tira de la configuracion de t2 hacia t1, preservando las relaciones logicas. Y el pushforward (la Kan extension izquierda) empuja datos en la otra direccion.

Los namespaces de Kubernetes son un caso concreto: cada namespace es un "slice" del cluster. La categoria de todos los recursos del cluster, indexada por namespace, forma un topos slice E/N para cada namespace N. Los network policies entre namespaces son los morfismos entre estos slices.

## La leccion del topos

Lo que me llevo de todo esto para mi practica como arquitecto es una inversion de perspectiva. No es que los sistemas distribuidos tengan una logica defectuosa que deberiamos reparar para que sea clasica. Es que los sistemas distribuidos habitan naturalmente en topoi donde la logica correcta es intuicionista, donde la verdad tiene grados y contextos, y donde la consistencia es una condicion de sheaf -- local por defecto, global solo cuando el pegado lo permite.

Los feature flags no son un hack. Son un clasificador de subobjetos. Los permisos no son una lista plana. Son la logica interna de un topos de acceso. La configuracion distribuida no es un problema de sincronizacion. Es una condicion de sheaf. Y la eventual consistency no es una limitacion. Es la logica intuicionista haciendo su trabajo: lo que todavia no se decidio, simplemente todavia no se decidio.
