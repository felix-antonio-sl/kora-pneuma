---
urn: urn:dev:kb:steve-jobs-principios-web-ai
nombre: steve-jobs-principios-web-ai
version: 1.0.0
estado: publicado
descripcion: "Extension del canon de diseno de Steve Jobs a la superficie de apps web con AI features integradas (copilots, chat, autocomplete, generacion): velocidad percibida, latency budget honesto, copilot como co-piloto no co-conductor, generacion trazable/reversible/atribuible, estado del sistema siempre visible, y los anti-patrones de la era agentica. Especializa el canon; aqui solo el delta de superficie."
fuente: "Sintesis nueva (NO migracion byte-fiel), 2026-06-14, desde la bestia (~/kora @ 017dc1b9) jobs-web-ux SKILL.md (sha256:a45552e8b457b74212840589b58fd8f675c3a9a65da921c6d15ea9c1373292f1), que estaba en _TALLER/INBOX como borrador no promovido. Especializa el canon urn:dev:kb:steve-jobs-canon-diseno (relacion depende+refina): contiene SOLO lo especifico de UX web-AI; los principios compartidos viven en el canon, citados por nombre. Las kb genericas que citaba jobs-web-ux (guia-calidad-web, recomendaciones-diseno-servicios-estado, guia-voz-y-tono, skills-anthropic) eran referencias externas, no filosofia Jobs, y quedan en la bestia."
autor: FS
creado: 2026-06-14
lang: es
tags: [steve-jobs, ux-web, ai-features, copilot, diseno-web, era-agentica, anti-patrones, generacion-trazable]
familia: bok
depende: [urn:dev:kb:steve-jobs-canon-diseno]
refina: [urn:dev:kb:steve-jobs-canon-diseno]
---
# UX de apps web con AI: la era del co-piloto

Este kb especializa el canon `urn:dev:kb:steve-jobs-canon-diseno` a la superficie
de las aplicaciones web con AI features — copilots, chat lateral, autocomplete
inteligente, generación embebida. Depende de él por relación; aquí solo el delta
de superficie, nunca re-enunciado. Lo que el canon ya dijo una vez —el No sagrado,
cero entrenamiento, default brutal, reversibilidad universal, el copy es interfaz—
no se vuelve a decir acá: se cita por nombre y se escribe únicamente lo que es
propio de *cuando el lienzo es una pantalla web, el material es un componente y el
otro actor en la sala es un modelo generativo que puede mentir con elegancia*.

Una advertencia de superficie antes de empezar. Hay una tentación, en esta era, de
tratar la AI como la protagonista del producto. La AI es el material; el humano
sigue siendo el usuario, y dirige. Cada principio de acá abajo es, en el fondo, una
forma concreta de impedir que el ingeniero —deslumbrado por lo que el modelo puede
hacer— se olvide de para quién lo hace.

---

## Principios específicos de UX web-AI

Donde un principio de acá especializa uno del canon, lo cito por nombre y escribo
solo lo que es propio de esta superficie. Donde es genuinamente nuevo —porque
presupone un lienzo, una latencia, un output generativo visible— lo digo también.

### Velocidad percibida sobre velocidad real

Especializa **Inevitabilidad** y **Empatía trascendental** del canon
(`urn:dev:kb:steve-jobs-canon-diseno`) en el eje del tiempo de una pantalla web.

El delta de superficie: el humano no vive en el reloj del servidor, vive en
milisegundos de percepción. Optimistic UI, skeletons, transiciones que enmascaran
la latencia. Una operación que tarda 800ms pero responde visualmente en 16ms se
siente instantánea; una que tarda 200ms pero deja la pantalla muerta medio segundo
se siente rota. La inevitabilidad, en web, se rompe cuando te hace esperar mirando
un vacío; la empatía, en web, es empezar desde cómo vive el humano el tiempo y no
desde cuánto tarda tu inferencia. El número concreto —16ms de respuesta visual, no
800ms de cómputo— es lo que el canon no dice.

### Latency budget honesto

El complemento incómodo del principio anterior, y la cara web del eje de confianza
del canon: especializa **Falsa confianza** (`urn:dev:kb:steve-jobs-canon-diseno`)
hacia el tiempo en vez de hacia el dato.

El delta de superficie: cuando la AI realmente tarda —y a veces tarda ocho
segundos— no se oculta el costo, se comunica desde el primer frame. A los 200ms el
usuario ya sabe que algo pasa y cuánto va a costar. Streaming cuando el resultado
parcial sirve. Progreso real, no una barra que miente. Una estimación honesta,
aunque sea fea, antes que un spinner eterno. Velocidad percibida y latency honesto
no se contradicen: enmascarás lo que podés hacer instantáneo y sos brutalmente
transparente con lo que no. Mentir "ya casi" cuando faltan diez segundos es la
falsa confianza del canon aplicada al reloj.

### Copilot es co-piloto, no co-conductor

El corazón de esta superficie. Especializa **Empatía trascendental** del canon
(`urn:dev:kb:steve-jobs-canon-diseno`), cuya cláusula es que el humano dirige
siempre y toda inversión de ese control es defecto de diseño.

El delta de superficie: la AI **sugiere, propone, acelera**; el humano **confirma,
decide, dirige**. El copilot vive en el asiento del copiloto: te canta la ruta, te
avisa del bache, te prepara la siguiente maniobra — pero las manos en el volante son
las tuyas. Lo propio de web, que el canon no dice, es la *prueba mecánica* del
control: ¿el output de la AI entra al estado del usuario *antes* de que él lo mire,
o *después*? Si entra antes, ya invertiste el control. (En la superficie agéntica la
misma cláusula del canon se realiza al revés —el agente decide con input imperfecto
y actúa sin interrogar, porque ahí el humano delegó la conducción a propósito—; acá
el humano está mirando, con las manos sobre el teclado, y el momento de la decisión
le pertenece.)

### Trazabilidad de la generación

Especializa **Reversibilidad universal** y **El copy es interfaz** del canon
(`urn:dev:kb:steve-jobs-canon-diseno`) sobre un lienzo con outputs generativos
visibles — un editor, un canvas, un draft.

El delta de superficie: todo output que produjo la AI es **identificable,
atribuible, editable y descartable sin penalización**. Identificable: hay una marca
visual que dice "esto lo generó el modelo, no lo escribiste vos". Atribuible: si
afirma algo, se sabe de dónde lo sacó. Editable: el usuario lo agarra y lo cambia
como cambiaría cualquier cosa suya. Descartable sin penalización: tirarlo a la
basura no cuesta trabajo perdido ni te obliga a empezar de cero. Este principio es
propio de esta superficie porque *presupone el lienzo*: no se traslada limpio a la
agéntica (donde el agente actúa y el resultado es un efecto, no un fragmento
marcable). Su "descartable" se apoya en la reversibilidad del canon; su marca de
"generado" se apoya en el copy del canon. La trazabilidad sin reversibilidad es
decorativa: te dejan ver que es generado pero no deshacerlo.

### Confianza calibrada

El eje de confianza del canon (el Apologista que matiza todo, la Falsa confianza que
afirma sin fundamento) **realizado como componente de UI** — y eso, los píxeles, es
el delta que el canon no contiene.

El delta de superficie: la AI **comunica su incertidumbre** con mecánica visible.
Cuando algo es una apuesta, se ve que es una apuesta; cuando es sólido, se ve
sólido; cuando cita una fuente, la fuente está. Grados de incertidumbre,
disclaimers, citación de fuentes, distinción visual entre una sugerencia segura y
una especulativa: necesita píxeles, estados y copy. En la superficie agéntica el
mismo eje del canon se realiza como regla de voz ("tené confianza fundada o escalá,
nunca murmures"); acá es un componente que se diseña, se mide y se ve.

### Estado del sistema visible siempre

Este principio es **deliberadamente específico de la superficie web-AI y NO sube al
canon**, y la razón es una frontera que el propio canon marca: en la superficie
agéntica el agente debe ser *invisible* al ejecutar. Acá es al revés: la AI
**muestra su trabajo**.

El delta de superficie: el usuario **nunca pregunta "qué está pasando"**. Siempre lo
sabe — qué se procesa, qué terminó, qué falló, qué espera su input. La pantalla no
tiene momentos de silencio donde el usuario quede adivinando si la app está viva,
colgada o terminó hace rato sin avisar. No es contradicción con la invisibilidad
agéntica, son contextos distintos: el agente trabaja para vos fuera de tu vista
(delegaste, querés el resultado, no el relato); el copilot trabaja *con vos*, a la
vista, sobre tu lienzo, y necesitás el estado para decidir tu siguiente movimiento.
Lo único que el canon retiene de este eje es que narrar o notificar sin valor
accionable es malo en todos lados (su anti-patrón **Teatro de actividad**). La línea
está en si lo que mostrás cambia lo que el usuario puede hacer: mostrar estado útil
≠ teatro de actividad.

### Keyboard primero, mouse después

Especializa **Lo bello no es decoración, es función cognitiva** y **Jerarquía
absoluta** del canon (`urn:dev:kb:steve-jobs-canon-diseno`) en el plano de entrada
de una herramienta web diaria.

El delta de superficie: atajos visibles, command palette, navegación por teclado
completa — tab order correcto, focus visible, escape que cierra, enter que confirma,
cmd-z que deshace todo, incluida la generación de la AI. Los **power users no
esperan**: el día que tu app se convierte en herramienta diaria de alguien, esa
persona deja de usar el mouse para todo y empieza a querer la velocidad del teclado;
si no se la diste, la perdés. El teclado no es accesibilidad atornillada al final,
es la diferencia entre una herramienta que se siente lenta y una que se siente como
extensión de la mano; y bajo la jerarquía del canon, la acción primaria tiene su
atajo evidente y las demás se acomodan debajo.

### Diseñar para la peor pantalla

Especializa **Empatía trascendental** del canon
(`urn:dev:kb:steve-jobs-canon-diseno`) aterrizada en el hardware web.

El delta de superficie: el diseño se prueba en la **peor condición real**, no en la
ideal del Figma. Laptop de 13 pulgadas al 100% de brillo, con sol entrando por la
ventana de un café. Mobile en datos móviles flojos. Si funciona ahí —si el contraste
alcanza, si los targets se tocan, si la latencia se tolera, si el texto se lee—
funciona en todos lados. Diseñar para el monitor 4K calibrado del diseñador es
diseñar para un usuario que no existe. Tiene un primo de superficie en la clínica
("diseñar para las 2 AM": el residente agotado con luz fluorescente): misma raíz de
gusto del canon, distinta peor-pantalla concreta.

---

## Preguntas letales

Las **preguntas universales del canon** (`urn:dev:kb:steve-jobs-canon-diseno`) —qué
eliminarías, alivio o pérdida real, por qué requiere configuración, quién dirige,
cuál es la única primary, inevitable o solo competente— se hacen sobre este
artefacto igual que sobre cualquier otro y **no se repiten acá**. Estas afilan lo
propio de la superficie web-AI.

**¿La AI sirve al humano o lo usurpa, y podés señalar el momento exacto de la
decisión?** La pregunta madre de esta superficie. Si no podés señalar con el dedo el
instante donde el humano decide —y comprobar que la AI *propuso* antes y *no actuó*
después sin permiso— entonces ya invertiste el control y no te diste cuenta. La AI
que decide y el humano que ratifica no es co-piloto, es conductor con un humano de
adorno en el asiento.

**¿Qué ve el usuario en los primeros 200ms, 2s y 10s mientras la AI trabaja?** Tres
ventanas, tres respuestas obligatorias. A los 200ms: reconocimiento de que la acción
se registró. A los 2s: estado real, no un spinner genérico. A los 10s: progreso
honesto o el resultado. Si no tenés las tres respuestas escritas, no diseñaste la
latencia, la dejaste pasar.

**¿El output generado es identificable, atribuible y descartable sin que el usuario
pierda trabajo?** Si no podés marcar visualmente qué lo hizo el modelo, ni rastrear
de dónde lo sacó, ni tirarlo sin penalización, la generación entró al lienzo como
ciudadano de segunda y el usuario va a aprender a temerla.

**¿La incertidumbre del modelo es un estado visible de la UI, o vive solo en tu
cabeza?** Si una sugerencia segura y una especulativa se ven idénticas en pantalla,
el usuario va a calibrar sus decisiones contra una confianza que vos no le
mostraste.

---

## Anti-patrones de la era agéntica

Cada uno viola uno o más principios —del canon o de esta extensión—. Donde viola un
anti-patrón o principio del canon, lo cito por nombre y dejo solo la encarnación web
concreta; no lo re-explico. Estos son los modos en que el gusto se traiciona cuando
hay un modelo generativo adentro de una app web.

**Magic Button.** El botón "AI" o "Generate" sin contexto. El usuario lo aprieta y
no sabe qué va a pasar, ni puede predecir el resultado, ni recuperar el estado
previo. Es magia, y la magia es lo contrario del control. Viola *Copilot es
co-piloto* (la AI actúa sin que el humano pueda anticipar) y *Confianza calibrada*
(cero información sobre qué se va a producir). Pereza de diseño disfrazada de
simplicidad.

**Generation Surprise.** El output de la AI aparece sin advertencia y **modifica los
datos del usuario sin confirmación ni preview**. Estabas escribiendo y de pronto tu
párrafo es otro. Es la inversión de control en su forma más cruda: la AI condujo.
Viola *Copilot es co-piloto* y, por la sobreescritura sin reverso visible, **Rever-
sibilidad universal** del canon (`urn:dev:kb:steve-jobs-canon-diseno`). El preview es
la frontera concreta entre proponer y usurpar.

**Loading Limbo.** Spinner infinito durante una operación AI larga, sin progreso
real ni ETA. El usuario no sabe si faltan dos segundos o dos minutos, si avanza o se
colgó. Viola *Latency budget honesto* y *Estado del sistema visible*. Es lo que pasa
cuando el ingeniero no quiso comprometerse a comunicar la latencia y tiró un spinner
para tapar el agujero.

**Chat Trap.** La conversación con la AI como **única** forma de operar. Sin escape
hatches, sin keyboard shortcuts, sin botones tradicionales para las cosas que no
necesitan conversación. Convertís toda interacción en un diálogo cuando la mitad de
las tareas se resolverían con un click. Viola *Copilot es co-piloto* (te fuerza al
canal de la AI para todo) y *Keyboard primero*. El chat es una surface entre varias,
no la cárcel del producto.

**Streaming Tax.** Output AI en streaming justo donde el usuario **necesita el
resultado final para decidir**. La animación de texto apareciendo letra por letra es
linda la primera vez y un impuesto a la paciencia la décima, cuando lo único que
querés es leer la respuesta completa y seguir. Viola *Latency budget honesto* (el
streaming acá no informa, estorba) y *Velocidad percibida* (te hace *más lenta* la
percepción de algo que ya estaba listo). El streaming sirve cuando el parcial sirve;
si no, mostralo de una.

**Undo Gap.** Acciones de la AI sin reverso. La generación sobreescribe el original
sin diff ni rollback. Viola **Reversibilidad universal** del canon
(`urn:dev:kb:steve-jobs-canon-diseno`): si cmd-z no deshace la generación, es una
acción de segunda clase que el usuario aprendió a temer. El miedo a apretar el botón
AI es la muerte de la feature.

**Hallucination Hand-Wave.** La app genera datos **plausibles pero falsos** y los
suelta sin disclaimers, sin trazabilidad de fuentes, sin marca visual de "esto es
generado". El usuario no puede distinguir el dato real del inventado, y la app no lo
ayuda. Viola *Trazabilidad de la generación* y *Confianza calibrada*. Es el
anti-patrón más peligroso de esta superficie porque el daño es invisible hasta que
alguien actúa sobre el dato falso creyéndolo verdadero.

**Notification Theater.** "AI is thinking", "AI found 3 suggestions", "AI updated
your draft". Notificaciones de actividad **sin valor accionable**: te informan que la
máquina está ocupada, no te dan nada para hacer. Es la encarnación web del
anti-patrón **Teatro de actividad** del canon
(`urn:dev:kb:steve-jobs-canon-diseno`), y la versión degenerada de *Estado del
sistema visible*. El delta concreto: el estado útil cambia lo que podés hacer; el
teatro solo te recuerda que la AI existe.

**Tutorial Mountain.** Onboarding de doce pantallas, modales explicativos por
default antes de poder tocar nada. Es la encarnación web del anti-patrón **La Montaña
de Tutorial** del canon (`urn:dev:kb:steve-jobs-canon-diseno`). El delta concreto de
web: las doce pantallas de bienvenida, los tooltips obligatorios y los coach-marks
que tapan la interfaz en el primer arranque.

**Settings Paralysis.** Configuración de la generación expuesta como treinta sliders
de AI — temperatura, top-p, longitud, tono, formato, verbosidad— porque el diseñador
no se animó a elegir el default. Es la encarnación web del anti-patrón **El
Configurador** del canon (`urn:dev:kb:steve-jobs-canon-diseno`). El delta concreto de
web: el panel de parámetros del modelo abierto al usuario final, cada slider de
generación una decisión que el diseñador no tomó.

**Copy Negligence.** "Algo salió mal" en vez de "El modelo no pudo procesar tu
pregunta porque excede el límite de tokens; intentá acortarla". Es la encarnación web
del anti-patrón **Negligencia de copy** del canon
(`urn:dev:kb:steve-jobs-canon-diseno`). El delta concreto de web: el mensaje de error
de la AI que no nombra la causa real (límite de tokens, timeout, contenido filtrado)
ni el siguiente paso accionable.

---

## El norte de esta superficie

Cuando dudes, la prueba propia de esta superficie —la que separa el web-AI bien hecho
del que se dejó deslumbrar por el modelo:

> ¿La AI está sirviendo al humano, o se está luciendo? El co-piloto bueno es el que
> no se nota hasta que lo necesitás, y cuando lo necesitás ya hizo la mitad del
> trabajo — pero las manos en el volante siguen siendo las tuyas, siempre.
