---
urn: urn:fxsl:kb:icas-safety-alignment
nombre: icas-safety-alignment
version: 1.1.0
estado: publicado
descripcion: "Pieza 12b del ICAS-BoK: safety y alineamiento categorial — ICAR, ley de Goodhart, coherencia y la distinción verificación/validación para sistemas agénticos."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/12b-safety-alignment.md (sha256:610d51c3c8b5e96d93a5de922db8023813cff74a09276942ede3c2dbfe5988a0) el 2026-06-12. Corrección 1.1.0 contrastada con Riehl, Category Theory in Context, https://emilyriehl.github.io/files/context.pdf, y Stacks Project, Sheafification, https://stacks.math.columbia.edu/tag/007X."
autor: FS
creado: 2026-04-14
lang: es
tags: [safety, alignment, verificacion, agente, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Safety y alignment

## Lo que no debe pasar

Hay una asimetria fundamental entre funcionalidad y seguridad. La funcionalidad dice lo que el sistema debe hacer. La seguridad dice lo que el sistema no debe hacer en las trazas dentro de su alcance. Los tests aportan evidencia y pueden agotar modelos finitos; por sí solos no demuestran una propiedad universal sobre un espacio infinito de trazas.

La teoria de categorias me ofrece algo mejor que testing: estructura. Un sistema es seguro cuando su comportamiento preserva ciertos invariantes bajo todas las transiciones. Y esa condicion de preservacion tiene una formulacion precisa que compone -- que se hereda de las partes al todo cuando la composicion tiene la forma correcta.

## Invariantes como sub-coalgebras

Un sistema con estado **puede modelarse** como coálgebra `c:U->F(U)` después
de fijar el funtor de observación/transición. La pregunta de safety se formula
entonces sobre los estados y comportamientos que ese modelo representa.

Los estados seguros forman un subobjeto `i : S -> U`. Para que sea una
subcoálgebra debe existir `s : S -> F(S)` tal que
`F(i) . s = c . i`; esto expresa cierre bajo las transiciones representadas.
La notación `c|_S` solo es legítima después de construir esa factorización.

La verificacion de safety se reduce a verificar que la inclusion i : (S, c|_S) -> (U, c) es un morfismo de coalgebras. Si lo es, los estados seguros forman un sub-sistema que nunca escapa de si mismo. Si no lo es, existe una transicion que lleva de un estado seguro a uno inseguro -- un bug de safety.

Un sandbox **puede modelarse** mediante esta estructura si se define el estado
del sistema, el funtor de transiciones y el subobjeto seguro. En la práctica,
que una syscall esté bloqueada es una propiedad del enforcement del runtime;
la analogía coalgebraica no la garantiza.

## Safety como sheaf: de lo local a lo global

En un sistema distribuido, cada componente puede declarar invariantes locales:
no cobrar dos veces, no vender stock negativo o no emitir tokens sin
credenciales válidas. Que el servicio realmente los garantice requiere prueba
o evidencia sobre su modelo y runtime.

La pregunta crítica es si las garantías locales componen globalmente. Esto
**puede modelarse** con una condición de sheaf después de definir un site de
componentes/interfaces, un presheaf de garantías y sus mapas de restricción.
Sin esos datos, «local a global» es una analogía, no literalmente un sheaf.

Dentro del modelo anterior, una familia de invariantes locales incompatible
puede manifestarse como fallo de pegado. Fuera de él, una vulnerabilidad entre
servicios no es «un presheaf que falla»: primero deben definirse secciones,
restricciones y cobertura. Por ejemplo, si B confía en la validación de A y A
cambia su contrato, la garantía global puede romperse aunque los checks locales
sigan pasando.

La sheafification es el funtor adjunto izquierdo a la inclusión de sheaves en
presheaves (para el site elegido). Agregar verificaciones de interfaz o aplicar
defense in depth puede inspirarse en el principio local-a-global, pero no es
sheafification salvo que se construya y verifique esa reflexión.

## Alignment como transformacion natural

Una formalización posible empezaría por categorías `World` y `Outcomes`, dos
funtores `G_agent, G_principal : World -> Outcomes` y componentes
`alpha_w : G_agent(w) -> G_principal(w)` que satisfagan naturalidad. Solo bajo
esos datos tendría sentido preguntar si `alpha` es una transformación natural
o un isomorfismo natural.

En sistemas reales, «objetivo», «resultado» y «cambio de mundo» rara vez
vienen ya como esas categorías. Por ello:

- alignment como transformación natural es un **modelo bajo hipótesis**;
- «alignment perfecto = isomorfismo natural» es una definición posible dentro
  de ese modelo, no una caracterización universal del alignment;
- ausencia de una transformación en una presentación elegida no demuestra
  misalignment ontológico: puede indicar que el modelo está mal tipado.

RLHF entrena políticas y reward models a partir de preferencias. No construye
por ese hecho componentes naturales ni demuestra diagramas de naturalidad. La
distancia a un isomorfismo tampoco está definida sin una métrica o estructura
adicional sobre transformaciones.

## Guardrails como sketches

Un guardrail es una restriccion sobre el comportamiento de un agente. "No generes contenido danino." "No ejecutes codigo sin confirmacion del usuario." "No accedas a datos fuera de tu scope." Cada restriccion es un diagrama que debe conmutar en la categoria de comportamientos del agente.

Un guardrail **puede especificarse** mediante un sketch si sus conductas se
presentan como una categoría y la restricción se expresa por los conos,
coconos o ecuaciones del sketch. Un filtro, prompt o clasificador ordinario no
es automáticamente un sketch ni un modelo suyo.

La restriccion "no generes contenido en la categoria X" es un diagrama que debe conmutar: el morfismo de generacion, compuesto con el clasificador de contenido, debe factorizarse por la inclusion de las categorias permitidas. Si el diagrama no conmuta, el contenido generado cae fuera de las categorias permitidas -- violacion del guardrail.

Constitutional AI ofrece una analogía útil con restricciones declarativas, pero
no implementa literalmente sketches categoriales salvo que se dé esa
formalización y se pruebe su satisfacción.

## Grados de seguridad en un topos

En un topos, el clasificador de subobjetos `Omega` porta lógica de Heyting y
sus valores pueden depender del contexto. No son, en general, probabilidades
ni «grados» numéricos de seguridad.

Una afirmación como «seguro bajo la hipótesis de input bien formado» puede
modelarse como verdad contextual. «Seguro con probabilidad 0.99» requiere
además una semántica probabilística; `Omega` no la proporciona por sí solo.

La lógica intuicionista puede modelar información parcial o contextual, pero
un deployment no se convierte automáticamente en objeto de un topos. Hay que
elegir primero el site/presheaf que representa sus observaciones.

## Seguridad composicional

Si el sistema A es seguro y el sistema B es seguro, su composicion A tensor B no es necesariamente segura. La seguridad es una propiedad del subobjeto (los estados seguros), y el producto tensorial no necesariamente preserva subobjetos.

La pregunta categorica es: para que productos tensoriales, que subobjetos se preservan? Si la seguridad de A es la propiedad P_A (un subobjeto de los estados de A) y la de B es P_B, la seguridad de A tensor B deberia ser al menos P_A tensor P_B -- los estados donde A es seguro Y B es seguro. Pero la interaccion puede crear estados inseguros que no existen en ninguno de los componentes aislados.

La condicion suficiente para la composicionalidad de safety es que la propiedad de seguridad sea monoidal -- que P_A tensor P_B sea un subobjeto de los estados seguros de A tensor B. Esto ocurre cuando la seguridad de cada componente no depende del estado del otro. Es decir, cuando no hay interferencia.

Capability-based security puede hacer explícita esta condición si el runtime
impide autoridad ambiental y la composición no amplifica permisos. Esa
preservación depende del modelo concreto de delegación y revocación; no se
sigue solo de usar la palabra capability.

Una slice `C/Cap` es un modelo posible cuando existe una categoría `C` y un
objeto `Cap` adecuados. Preserva los mapas hacia `Cap`; demostrar que eso
coincide con autoridad efectiva sigue siendo una obligación del runtime.

## Alignment a lo largo del tiempo

El alignment no es un estado estatico -- puede degradarse. Un agente que empieza alineado puede driftar a medida que su contexto cambia, que los datos de entrenamiento envejecen, o que los objetivos del principal evolucionan. Si modelo el alignment como una seccion de un sheaf sobre ventanas temporales -- un behavior sheaf donde cada ventana tiene un valor de alignment -- la degradacion se formula con precision.

Una seccion de alignment que existe sobre una ventana de 30 dias pero no se extiende a 90 dias exhibe alignment drift. La condicion de sheaf dice: si el alignment es consistente en cada sub-ventana solapada, se extiende a la ventana completa. Si no se extiende, hay una inconsistencia en algun solapamiento -- un periodo donde los objetivos del agente dejaron de corresponder con los del principal.

Dentro de un modelo temporal explícito, los evals periódicos son observaciones
locales. Su consistencia aporta evidencia, pero una muestra finita no verifica
la condición de sheaf ni la existencia de una sección global; una divergencia
sí puede funcionar como contraevidencia localizada.

Una modalidad temporal "always" (que en la temporal type theory de Schultz y Spivak se denota up) captura la condicion fuerte: "el agente esta always-aligned" exige que el alignment se mantenga para todo tiempo futuro. En la practica, lo que puedo verificar es una version acotada: alignment en los ultimos D dias, donde D es la ventana de evaluacion. El documento 15 desarrolla esta maquinaria temporal en profundidad.

## Reward hacking como pérdida de información

Cuando un agente optimiza una métrica proxy, explota una traducción que pierde
distinciones relevantes. El modelo mínimo usa un espacio de estados `X`, un
proxy `p : X -> P` y un objetivo `g : X -> G`.

El agente busca dentro de fibras de `p`: estados con el mismo valor proxy pero
valores de objetivo distintos, o direcciones donde `p` mejora y `g` no. Hablar
de «kernel» requiere estructura algebraica adicional.

Agregar señales puede refinar las fibras del proxy y reducir ambigüedad.
`faithful` significa inyectivo en cada hom-set de un funtor; no significa
«buen proxy». Incluso un funtor fully faithful no implica que maximizar una
función proxy maximice otra función objetivo. Esa conclusión requiere una
relación de orden/optimización explícita entre `p` y `g`.

## Seguridad como analisis categorico de grafos de ataque

Las taxonomias de ciberseguridad -- CVE, CWE, CAPEC, ATT&CK, CPE -- no son silos independientes sino categorias conectadas por funtores. Valence construye ICAR (Integrated CAtegorical Resource) como un knowledge schema categorico donde los diccionarios de seguridad son objetos, las relaciones entre ellos son morfismos, y las path equivalences capturan restricciones semanticas. Los attack paths son composiciones de morfismos; la defensa es la ruptura de conmutatividad en algun punto de la cadena. El documento 18 desarrolla ICAR en profundidad con queries operativas y conteos concretos; el documento 14 lo situa en el contexto de organizaciones multi-agente.

## Verificacion formal versus validacion empirica

La verificación formal demuestra una propiedad para todos los estados o
ejecuciones cubiertos por un modelo. La validación empírica observa una muestra
finita y aporta evidencia, no universalidad.

Ends y coends tienen fórmulas con sabor universal/existencial en contextos
específicos —por ejemplo, un end puede representar familias naturales—, pero
no son sinónimos genéricos de «todos los tests» y «algún test». Para usar un
end o coend aquí hay que definir un profuntor concreto y demostrar que su
propiedad universal representa la afirmación de seguridad.

Model checking puede verificar exhaustivamente un modelo finito. Que ese
modelo represente el sistema real es una obligación de abstracción aparte; ser
«suficientemente representativo» no convierte por sí solo una prueba local en
una prueba global.

## Seguridad distribuida como sheaf

En un modelo sheaf explícito, cada nodo o interfaz puede indexar una sección
local de garantías y las restricciones describen qué se observa al pasar a
un solapamiento.

La condición de sheaf afirma pegado único para familias compatibles **dentro
de ese presheaf**. No prueba que las garantías declaradas sean verdaderas
respecto del runtime.

Un fallo bizantino no es, por definición, una ruptura de la condición de
sheaf: introduce discrepancia entre declaraciones y comportamiento. Los
protocolos BFT requieren modelos de fallos, quórums y supuestos de red; no son
sheafification automática.

La defensa en profundidad es una estrategia operacional de controles
independientes. Puede complementar un análisis local-a-global, pero no se
identifica con el funtor de sheafification.

## La estructura subyacente

Lo que emerge de todo esto es una vision donde la seguridad y el alignment no son propiedades ad hoc que se verifican con checklists, sino propiedades estructurales que componen (o no componen) segun la geometria de la categoria de comportamientos.

Cada una de estas lecturas es condicional: la seguridad **puede** ser un
subobjeto cerrado bajo una coálgebra; el alignment **puede** modelarse con una
transformación natural; los guardrails **pueden** presentarse por sketches; y
la estabilidad temporal **puede** estudiarse con sheaves de intervalos. Las
categorías y leyes deben construirse antes de heredar garantías.

No estoy introduciendo un vocabulario enteramente distinto. Estoy reutilizando las mismas construcciones que uso para schemas, protocolos y composicion de sistemas, aplicadas al problema de que los agentes hagan lo correcto. La teoria de categorias no resuelve el alignment problem -- pero da un lenguaje donde las preguntas se formulan con precision suficiente para saber cuando una respuesta es respuesta y cuando es wishful thinking.

## Corrección 1.1.0

Se corrigen las identificaciones sheafification=defense-in-depth,
RLHF=transformación natural, proxy fiel=objetivo adecuado y
verificación/validación=end/coend. Estas construcciones quedan disponibles como
modelos solo bajo categorías, funtores y propiedades universales explícitas.
