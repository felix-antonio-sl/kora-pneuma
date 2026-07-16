# Caso aplicado canónico: Asto, Besto y Resto

Procedimiento original del operador (2026-06-03) del cual se generalizó esta
skill. Se conserva como ejemplo vivo de cómo convocar un panel sin confundir la
identidad que cada experto encarna con las capacidades que puede ejercer.

## Panel

| Alias | Identidad | Capacidades |
|---|---|---|
| Asto | `urn:salud:artefacto:salubrista` | `urn:salud:artefacto:hospitalizacion-domiciliaria` |
| Besto | `urn:kora:artefacto:mente-omega` | `urn:kora:artefacto:cat-thinking` |
| Resto | `urn:fxsl:artefacto:dov-dori` | `urn:kora:artefacto:modelamiento-opm` |

El panel ilustra tres invariantes:

- una identidad puede realizarse como agente, persona o skill encarnable; su
  forma runtime no cambia la perspectiva que debe sostener;
- las capacidades son skills que el experto ejerce dentro de su turno, no
  sustitutos de su identidad;
- la diversidad es estructural: salud pública/clínica, razonamiento
  discursivo-estructural y modelado conceptual aportan sesgos distintos.

## Procedimiento original

> Asto, Besto y Resto deben resolver el problema mediante consenso crítico.
>
> Cada uno formulará una propuesta inicial breve con tesis, argumentos,
> supuestos y riesgos. Luego cada uno criticará las propuestas de los otros,
> limitándose a objeciones sustantivas. Con esas críticas construirán una
> síntesis común. Después intentarán refutar esa síntesis como adversarios
> externos. Si aparecen objeciones críticas, corregirán la síntesis y repetirán
> el ciclo hasta que no queden objeciones relevantes.
>
> El consenso solo puede declararse cuando los tres acepten que la síntesis es
> la mejor versión disponible, que no pueden mejorarla materialmente con nuevos
> argumentos y que las discrepancias restantes son menores.
>
> La salida debe incluir síntesis final, razonamiento consolidado, aportes de
> Asto/Besto/Resto, supuestos aceptados, riesgos pendientes, incertidumbres y
> nivel de confianza de cada experto.

## Mapeo al protocolo

| Fragmento | Estado de la skill |
|---|---|
| definir el panel con identidades y capacidades | `convocar` |
| propuesta inicial con tesis, argumentos, supuestos y riesgos | `proponer` |
| objeciones sustantivas cruzadas | `criticar` |
| construir una síntesis común | `sintetizar` |
| atacar la síntesis como adversarios externos | `refutar` |
| incorporar críticas y repetir el ciclo | `corregir` → `refutar` |
| triple aceptación por cada experto | `declarar` |
| documento auditable con ocho secciones | `entregar` |

La skill agrega lo que el procedimiento original dejaba implícito:

- `max_ciclos` y salida de disenso estructurado con decisión HITL;
- gate de diversidad para paneles que no nacen diversos por construcción;
- declaración del modo `encarnacion` u `orquestacion`;
- catálogo de degeneración y reglas contra el consenso de cortesía.
