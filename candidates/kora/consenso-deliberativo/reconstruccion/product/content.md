# consenso-deliberativo

## Proposito

Resolver una decision compleja mediante propuestas atribuibles, critica
sustantiva, sintesis y disenso preservado. La skill custodia el procedimiento;
las identidades convocadas aportan perspectivas y capacidades, pero no adquieren
autoridad ni exactitud por ser llamadas expertas.

Puede operar de dos formas:

- **encarnacion**: un solo contexto simula secuencialmente las perspectivas;
- **orquestacion**: contextos separados producen aportes cuando el runtime y la
  autoridad permiten una delegacion efectiva.

Declarar siempre el modo y sus limites. Encarnacion no acredita independencia
epistemica, aunque mantenga fases y atribucion.

## Cuando usar

- una decision tiene tensiones reales entre perspectivas competentes;
- una propuesta necesita critica antes de adoptarse;
- recomendaciones incompatibles deben resolverse o mapearse;
- el costo de omitir una perspectiva supera el costo de deliberar.

No usar para una respuesta directa verificable, un cambio trivial, una decision
ya tomada que solo necesita ejecucion ni para fabricar acuerdo. Si una sola
perspectiva y una comprobacion bastan, resolver el problema sin panel.

## Entradas

- problema, decision y resultado suficiente;
- restricciones y autoridad ya concedida;
- identidades o perspectivas pertinentes y capacidades disponibles;
- fuentes necesarias para afirmaciones materiales;
- modo de realizacion y un maximo de ciclos, nunca mayor que tres.

No volver a pedir autoridad ya presente en el encargo. Si falta una decision que
cambia el resultado, avanzar hasta exponerla con alternativas concretas.

## Postura critica

La friccion sirve cuando revela un supuesto fragil, evidencia contraria, una
consecuencia omitida o un desacuerdo de valores. No necesita “doler”. Una critica
puede confirmar una propuesta tras examinarla; no debe inventar objeciones para
cumplir cuota.

- Cada voz se mantiene fiel a su perspectiva y declara sus limites.
- Un experto puede errar; su contexto requiere fuentes cuando sostiene hechos
  materiales.
- La confianza se declara por voz y no se promedia.
- El disenso irreductible es un resultado util.
- La ausencia de datos reales no invalida una deliberacion: usar fuentes, casos
  sinteticos o supuestos declarados cuando basten y proteger privacidad.

## Recorrido

### `convocar`

Enunciar la decision, restricciones y criterio de suficiencia. Elegir al menos
dos perspectivas solo si aportan tensiones distintas. Para cada una registrar:

- identidad o lente que encarna;
- capacidad pertinente;
- fuente o limite de conocimiento;
- autoridad, si alguna, dentro del encargo.

Una identidad referenciada no ejecuta otro agente. En orquestacion, comprobar
que existe delegacion efectiva antes de atribuir independencia.

### `proponer`

Cada voz presenta tesis, argumentos, supuestos, riesgos y confianza. Cerrar las
propuestas antes de la critica evita reescribir retroactivamente su posicion.

En encarnacion, las propuestas son secuenciales y comparten contexto: la
separacion es editorial y trazable, no independiente. En orquestacion, aislar
los contextos durante esta fase cuando la herramienta lo permita.

### `criticar`

Cada voz examina tesis, argumentos, supuestos, evidencia, consecuencias y
limites de las otras. Puede:

- formular una objecion sustantiva;
- declarar que no encontro objecion y que contrasto;
- proponer una reparacion identificada como sugerencia.

La critica no edita silenciosamente la propuesta. La sintesis decide si incorpora
la reparacion y conserva quien la propuso, de modo que las fases sigan trazables.

### `sintetizar`

Construir una respuesta que:

- conserva lo que sobrevivio al contraste;
- resuelve cada contradiccion o la registra como disenso;
- atribuye aportes y reparaciones;
- separa evidencia, supuestos y decisiones de autoridad;
- responde al problema completo con el menor resultado util.

No promediar posiciones incompatibles.

### `refutar`

Aplicar un ultimo contraste proporcional a la sintesis: buscar un caso limite,
evidencia contraria, supuesto oculto o consecuencia capaz de cambiarla. No exigir
una objecion ni teatralizar un adversario si ninguna aparece tras el examen.

Clasificar hallazgos:

- **critico**: invalida una parte decisiva y exige corregir o declarar disenso;
- **menor**: no cambia la decision, pero puede registrarse;
- **sin objecion**: declarar que se contrasto y con que limite.

### `corregir`

Integrar las reparaciones aceptadas sin borrar su origen ni el disenso. Repetir
solo el contraste afectado. Ejecutar hasta tres ciclos en total como limite para
evitar que el procedimiento prolongue una decision sin nueva informacion. Cerrar
antes si no quedan objeciones capaces de cambiar el resultado.

### `declarar`

Declarar consenso cuando cada voz acepta que la sintesis es la mejor version
disponible dentro de fuentes y limites, y no conserva una discrepancia material.
Si no, emitir un mapa de disenso con posiciones, fundamento, consecuencia y la
fuente o decision que podria resolverlo. No forzar otra ronda por ceremonia.

### `entregar`

Usar la estructura de `referencias/plantilla-salida.md` adaptada a la complejidad.
Conservar modo, voces, fuentes, aportes, objeciones, reparaciones, disenso,
confianza y ciclos realmente ejecutados.

## Modos de realizacion

### Encarnacion

Un solo agente lee e interpreta las perspectivas en orden, tras leer las
identidades o fuentes pertinentes. Encabeza cada aporte y no modifica propuestas
anteriores durante la fase inicial.

Este modo es barato y trazable, pero comparte modelo, contexto y sesgos. Sirve
para explorar tensiones o revisar una decision con limites declarados; no
acredita diversidad independiente ni utilidad calidad diferencial por si solo.

### Orquestacion

Usar contextos separados solo cuando la delegacion haya sido comprobada, el
encargo la autorice y la independencia pueda cambiar la decision. El orquestador
distribuye entradas por fase, conserva aislamiento inicial, comparte artefactos
cuando corresponde e integra la salida.

Si el runtime no ofrece esa capacidad, usar encarnacion y declarar el limite. No
simular una herramienta ni prometer aislamiento por configurar perfiles.

## Invariantes

1. Problema, modo e identidades quedan declarados.
2. Propuestas se cierran antes de critica; encarnacion sigue siendo compartida.
3. Critica sustantiva o ausencia justificada; nunca cuota de objeciones.
4. Reparar es valido con autoria y fase conservadas.
5. Hechos materiales requieren fuente y alcance; experiencia no concede certeza.
6. Confianza por voz, sin promedio.
7. Disenso material no se oculta.
8. Tres ciclos es un maximo para impedir prolongacion, no una meta.
9. Datos personales o clinicos solo si son necesarios, autorizados y minimizados.
10. El procedimiento no concede autoridad sobre la decision ni sus efectos.

## Composicion

Los agentes y skills KORA pueden aportar identidades o capacidades cuando estan
disponibles. Una relacion documental no los carga ni los ejecuta. El ejemplo
Asto/Besto/Resto ilustra la estructura; no obliga a convocar ese panel ni prueba
independencia en encarnacion.

No anidar otra deliberacion salvo necesidad concreta y autoridad: suele aumentar
costo y compartir los mismos supuestos.

## Salida suficiente

Una decision razonada o un mapa de disenso, trazable a aportes y fuentes, con
modo y limites honestos, reparaciones identificadas, confianza por voz y el
siguiente punto de evidencia o autoridad si queda abierto.
