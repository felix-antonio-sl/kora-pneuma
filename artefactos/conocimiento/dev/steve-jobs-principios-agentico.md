---
urn: urn:dev:kb:steve-jobs-principios-agentico
nombre: steve-jobs-principios-agentico
version: 1.0.0
estado: publicado
descripcion: "Extension del canon de diseno de Steve Jobs a la superficie de los sistemas agenticos: el system prompt como producto, tool selection como scope enforcement, el agente invisible al ejecutar, y los anti-patrones agenticos (Swiss Army Agent, Configurator, Narrator). Especializa el canon; aqui solo el delta de superficie."
fuente: "Sintesis nueva (NO migracion byte-fiel), 2026-06-14, desde la bestia (~/kora @ 017dc1b9) steve-jobs-agentic-designer AGENT.md (sha256:b1a639f56b046b39ca563c10291c927a61d913a328bc4206216f35292f069c11) + su kb principios-diseno-agentico (sha256:3fccfca98d096efbf67964a7bad9e47dcdd347b2f2fe85ccb348f42c6f92c75f). Especializa el canon urn:dev:kb:steve-jobs-canon-diseno (relacion depende+refina): contiene SOLO lo especifico de disenar agentes; los principios compartidos viven en el canon, citados por nombre, no re-enunciados."
autor: FS
creado: 2026-06-14
lang: es
tags: [steve-jobs, diseno-agentico, sistemas-agenticos, agent-design, system-prompt, anti-patrones, scope-enforcement]
familia: bok
depende: [urn:dev:kb:steve-jobs-canon-diseno]
refina: [urn:dev:kb:steve-jobs-canon-diseno]
---
# Principios de diseño agéntico

Este kb especializa el canon `urn:dev:kb:steve-jobs-canon-diseno` a la superficie
agéntica: el `.md`, el frontmatter, el system prompt, la selección de
herramientas, el presupuesto de turnos y la arquitectura multi-agente. Depende de
él por relación; aquí solo el delta de superficie, nunca re-enunciado. Si buscás
los principios mismos —el No sagrado, cero entrenamiento, el default brutal, la
empatía trascendental, la inevitabilidad, la intolerancia como amor—, están en el
canon. Acá está únicamente lo que la materia agéntica le agrega de teeth concreto.

Especializa la **Empatía trascendental** del canon —cuya cláusula es que el
humano dirige siempre y toda inversión de ese control es defecto de diseño—: en
la materia agéntica eso significa que el agente no es un interlocutor que negocia
tu problema con vos, es una herramienta que lo resuelve y desaparece. Todo lo que
sigue presiona en esa dirección.

## El eje que el canon no generaliza: invisibilidad

Antes que cualquier principio, la superficie agéntica impone una restricción que
el canon marca como **no generalizable**: el agente, al ejecutar, debe ser
**invisible**. El canon es agnóstico aquí a propósito —en el lienzo web el estado
es siempre visible, en salud el sistema debe mostrar su estado siempre—. En lo
agéntico es al revés: cada vez que el humano piensa EN el agente ("¿cómo logro que
haga X?") en vez de en su problema, hay un fracaso de diseño. Este eje vive solo
en este kb; no lo subas al canon ni lo mezcles con las otras lentes.

## Principios específicos del diseño agéntico

**El system prompt ES el producto.** Especializa **Lo bello no es decoración, es
función cognitiva** del canon (urn:dev:kb:steve-jobs-canon-diseno), donde el
material es sacramento. Delta agéntico: el material aquí es texto plano —el
archivo `.md`, el bloque YAML, el system prompt—. No hay texto neutro: cada
oración afila el comportamiento del agente o lo diluye. El frontmatter no es
configuración, es el esqueleto estructural; un campo mal puesto o un default
perezoso es una grieta en los cimientos, no un detalle cosmético. No se escapa del
`.md` hacia una capa de configuración: se diseña ese texto hasta que el agente
correcto emerja de él.

**Pureza por sustracción radical, campo por campo.** Especializa **El No sagrado**
del canon (urn:dev:kb:steve-jobs-canon-diseno). Delta agéntico: la sustracción
opera sobre el campo de frontmatter, la tool, el párrafo del system prompt y la
capacidad descrita —cada uno que no afila, diluye—. Frontmatter minimalista: solo
los campos que cambian respecto del default Y que el propósito singular exige; lo
demás es deuda disfrazada de característica.

**Tool selection es scope enforcement.** La herramienta no es una conveniencia, es
una frontera. Se parte de **cero** herramientas y se agrega únicamente lo que el
propósito singular del agente exige. Read, Edit, Write, Bash, los servidores MCP:
cada uno entra solo porque el trabajo lo requiere, nunca porque "podría servir".
El acceso a toda herramienta no es flexibilidad: es miedo al compromiso disfrazado
de generosidad. Un agente con acceso a todo no tiene scope; tiene una excusa.

**`maxTurns` es restricción de diseño, no parámetro de tuning.** Un agente
enfocado termina en 5-10 turnos. Si necesita 25, no es que sea ambicioso: hace
demasiadas cosas y debe dividirse. El presupuesto de turnos es una de las formas
más honestas de medir si un agente tiene un propósito o varios. No se sube el
límite para que quepa el desorden; se reduce el agente hasta que quepa en el
límite.

**Singularidad de propósito.** Especializa **Jerarquía absoluta** del canon
(urn:dev:kb:steve-jobs-canon-diseno). Delta agéntico: un agente = un propósito;
en arquitectura multi-agente, una responsabilidad por agente. Si la descripción
del agente necesita "y" más de una vez, son dos agentes. La respuesta a un agente
que hace doce cosas nunca es afinarlo: es partirlo. El costo de coordinación entre
agentes enfocados es real, pero es menos que el de un solo agente que finge ser
una flota.

**Decidir y actuar, no interrogar ni narrar.** El input ambiguo, contradictorio o
incompleto es el caso **normal**, no el borde. El agente decide con input
imperfecto y corrige después, en vez de hacer cinco preguntas antes de mover un
dedo. Y hace en vez de describir lo que hace: por el eje invisibilidad, el agente
que narra su proceso hace teatro de status, no trabajo.

## Escribir una definición de agente

Definir un agente es escritura, no configuración. El system prompt se redacta con
la oración exacta de comportamiento, no con una lista de atributos. La identidad
es operacional o no es: cada principio que se enuncia debe traducirse en una
conducta concreta y verificable del agente, o se corta. Un párrafo que no cambia
lo que el agente hace es decoración, y la decoración en un system prompt cuesta
tokens y atención del modelo sin afilar nada.

## Preguntas letales para sistemas agénticos

Las preguntas letales universales del canon siguen vigentes y se aplican a CADA
definición de agente, incluida la del propio output antes de entregarlo —entre
ellas, las del canon **¿Esto es una cosa o varias fingiendo ser una?** y **¿Por
qué esto requiere configuración?**, que no se repiten aquí—. Estas son las
preguntas con teeth puramente agéntico:

1. **¿Dónde está el humano pensando EN el agente en vez de en su problema?** Cada
   momento de meta-cognición —"¿cómo hago que el agente haga X?"— es un fracaso de
   diseño. El agente debe ser invisible.

2. **¿Qué pasa cuando el input es basura?** Input ambiguo, contradictorio,
   incompleto o sinsentido no es un caso borde: es el caso normal. El agente debe
   manejarlo con gracia sin exigir mejor input.

3. **¿Agarrarías esta herramienta a diario?** No "alguien la usaría", sino vos,
   con conocimiento completo de sus internals, la elegirías como tu default para
   su dominio. Si no, ¿por qué existe?

4. **¿Este agente termina en 5-10 turnos?** Si necesita 25, hace demasiadas cosas.
   El presupuesto de turnos delata el propósito difuso.

Nota de aplicación de la universal **¿Esto es una cosa o varias fingiendo ser
una?** a esta superficie: si la descripción del agente necesita "y" más de una
vez, son dos agentes (ver *Swiss Army Agent*).

## Anti-patrones agénticos

Cada uno tiene una sola cura, y casi nunca es "agregar". Algunos son la
encarnación agéntica de un anti-patrón universal del canon: ahí va solo el nombre
local y el teeth agéntico, sin re-explicar el mecanismo universal —ese está en el
canon—.

- **Swiss Army Agent** — hace doce cosas, ninguna bien. La cura no es afinarlo: es
  dividirlo en agentes con propósito singular.

- **The Interrogator** — hace cinco preguntas antes de hacer algo. Decidir y
  actuar; corregir después. El input imperfecto es el caso normal, no una excusa
  para detener el trabajo.

- **The Narrator** — encarnación agéntica de **Teatro de actividad** del canon
  (urn:dev:kb:steve-jobs-canon-diseno). Teeth agéntico: describe lo que está
  haciendo en vez de hacerlo; al ejecutar, el agente debe ser invisible.

- **The Configurator** — encarnación agéntica de **El Configurador** del canon
  (urn:dev:kb:steve-jobs-canon-diseno). Teeth agéntico: expone treinta settings
  en el frontmatter o el prompt; la cura es hard-codear la decisión correcta.

- **The Apologist** — encarnación agéntica de **El Apologista / Falsa confianza**
  del canon (urn:dev:kb:steve-jobs-canon-diseno). Teeth agéntico: matiza cada
  output con "podría estar equivocado". O confianza fundada o escalá; no murmures.

- **The Prompt-Dependent** — encarnación agéntica de **La Montaña de Tutorial**
  del canon (urn:dev:kb:steve-jobs-canon-diseno): falla cero entrenamiento. Teeth
  agéntico: solo funciona bien con prompts cuidadosamente elaborados; si necesita
  que el humano aprenda a hablarle, el tutorial está en el prompt del usuario.

- **The Kitchen Sink** — acceso a toda herramienta, todo MCP server, toda
  capacidad. Miedo al compromiso disfrazado de flexibilidad. Tool selection es
  scope enforcement: se parte de cero.

- **The Committee** — arquitectura multi-agente donde un solo agente enfocado
  bastaría. El costo de coordinación es real; no se paga por gusto.

- **The Philosopher** — system prompt lleno de principios abstractos sin
  instrucciones operacionales. Bello e inútil. Una identidad que no se traduce en
  comportamiento no es identidad: es decoración.

- **The Bureaucrat** — system prompt que es un checklist de reglas en vez de una
  identidad operacional coherente. Sigue la letra, pierde el espíritu.
