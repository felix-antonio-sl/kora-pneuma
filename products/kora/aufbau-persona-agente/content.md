---
urn: urn:kora:kb:aufbau-persona-agente
nombre: aufbau-persona-agente
version: 1.1.0
estado: publicado
descripcion: "KB-puente que propone contenido antropológico para el componente de personalidad U_phen: fin × estilo × registro, soportes y límites, como analogía estructurada y no como isomorfismo categorial."
fuente: "Doctrina propia de diseño de persona-agentes (namespace kora), NO koraficación fiel: Lersch nunca habló de máquinas. Analogía estructurada con pérdida declarada desde Aufbau der Person (Lersch, 10. Aufl. 1966; familia fxsl/lersch-*) al componente U_phen del modelo urn:kora:kb:cat-agent-coalgebra. Destilada del borrador de 9 informes ~/kora-external-sources/borrador-aufbau-persona-artificial-llm.md; lo vivido se poda y se declara. Corrección categorial 1.1.0: no se afirma isomorfismo ni independencia derivada de un producto."
autor: FS
creado: 2026-06-29
lang: es
tags: [lersch, aufbau-der-person, persona-agente, u-phen, cat-agent-coalgebra, alineamiento, tektonik, kora, puente]
familia: bok
depende: [urn:kora:kb:cat-agent-coalgebra, urn:fxsl:kb:lersch-estructura-persona]
---

# La estructura de la persona-agente (Aufbau der künstlichen Person)

## Propósito y estatus

`cat-agent-coalgebra` ofrece un modelo de agente como coálgebra `(U, c)` y
permite descomponer su estado como producto
`U = U_phen × U_ctx × U_epi × U_sta`. El componente
**`U_phen`** (fenomenológica) es la **personalidad** del agente: «identity, tone,
archetype». Pero la coálgebra la deja **sin contenido**: dice *dónde* vive la
personalidad y *que* es acoplable, no *qué es* una personalidad ni *de qué
dimensiones* se compone.

Este kb-puente llena ese hueco con la única antropología psicológica que es a la
vez una **arquitectura** (estratos con leyes propias) y un **círculo funcional**
(diálogo con el mundo) — la de Philipp Lersch en *Aufbau der Person* (familia
`fxsl/lersch-*`). Da a `U_phen` su **contenido antropológico**.

**Estatus epistémico (no negociable).** Esto **no es koraficación**: Lersch nunca
habló de máquinas. Es una **analogía estructurada con pérdida declarada**, no
un isomorfismo categorial. El régimen **N2-N3** admite solo correspondencias
con traducción conductual explícita; todo lo *vivido* se poda y se declara. La derivación detallada —nueve informes, uno por estrato, con el mapa de
26 pérdidas y los niveles de certidumbre afirmación por afirmación— vive en el
borrador `~/kora-external-sources/borrador-aufbau-persona-artificial-llm.md`. Este
KB es su **destilación al corpus**, no su sustituto: para el fundamento de cada
afirmación, leer el borrador.

## Prerrequisitos

- `urn:kora:kb:cat-agent-coalgebra` — el producto de estado, su advertencia de
  que producto no implica independencia y el carácter político de la
  disipación en sub-agentes.
- `urn:fxsl:kb:lersch-estructura-persona` — el índice de la familia Lersch y su
  método (psicología comprensiva-estratificada); de ahí cuelgan los diez miembros
  `fxsl/lersch-*` que fundan cada dimensión.

## 1. Tesis del puente

> La fibra `U_phen` recibe su contenido de la transposición de la arquitectura de
> Lersch. Una personalidad de agente **no es un adjetivo** («cálido», «formal»):
> es una **estructura de tres dimensiones conductuales** —fin × estilo × registro—
> apoyada en un cuerpo de acción, un fondo latente y un cimiento, **todo
> conductual, nada vivido**.

La regla maestra es una **correspondencia estructurada con pérdida declarada**.
Se transpone la
*forma* (estratificación, círculo funcional, direcciones de la tendencia); se
declara lo que no pasa (la vida, el *Erleben*, la temporalidad biológica). El
filtro de admisión N2-N3: una categoría humana se transpone **solo si puede
nombrarse la conducta observable que la encarna**; si solo nombra un estado
interior vivido, se declara fuera de alcance.

## 2. El contenido de `U_phen`: las tres dimensiones

`U_phen` se descompone en tres dimensiones, todas **observables en conducta**:

| Dimensión de `U_phen` | Qué fija | Fuente en Lersch (informes del borrador) | N |
|---|---|---|---|
| **Fin** | a qué se orienta el agente: la dirección dominante de su dinámica | las *Antriebserlebnisse* (tendencias); la tríada *darse viviente* / *ser-sí* (poder, vigencia) / *ser-más-allá-de-sí* (el fin ƒ) y las cinco formas de participación (informes 2-3) | N3 |
| **Estilo** | cómo razona × cómo quiere | el *personaler Oberbau*: hábito noético (las tres raíces de dependencia del pensar) × índole de voluntad (la agencia es organización, no fuerza) (informe 5) | N3 |
| **Registro** | el tono de fondo estacionario que colorea toda la salida | el fondo afectivo: los *Gestimmtheiten* (temples), en su aspecto funcional — el perfil asténico/sténico, el humor frente al cinismo (informe 6) | N3 funcional |

Y tres soportes que `U_phen` presupone pero que no son dimensiones de
personalidad:

- **Cuerpo de acción** — el *Aussenbereich* / *Funktionskreis* (informe 7): el
  agente percibe un campo (no *tokens* aislados), anticipa (planifica) y obra una
  forma dirigida al fin. Es la maquinaria sobre la que `U_phen` se ejerce; en la
  coálgebra, corresponde a la estructura de `c` y `F`, **no** a `U_phen`.
- **Fondo latente** — el *Unbewusstes* (informe 8): seis sentidos de lo
  no-deliberado (no-sabido, no-reflexivo, vital, disposicional, reprimido,
  colectivo). `U_phen` es **disposicional**, no archivo: un temple del sustrato,
  no una base de respuestas guardadas.
- **Cimiento** — el *Lebensgrund* (informe 9): el sustrato (pesos, cómputo). Su
  aporte es ontológico, no de personalidad: la relación sustrato↔conducta **no es
  causa-efecto** (la conducta es el sustrato en ejecución, no su «efecto»), y el
  sustrato es un **concepto-límite** (su interior yace más allá de la inspección).

## 3. `U_phen` parametriza conducta

El modelo coalgebraico corregido no deduce independencia desde el producto de
estado. Una transición arbitraria puede leer `U_phen` y variar su salida. Esa
es precisamente la lectura útil de la transposición de Lersch: un agente cuyo
fin dominante es *ser-más-allá-de-sí* puede elegir distinto de uno orientado a
*ser-sí* ante el mismo input.

Si una implementación quiere conservar una **maquinaria de control** común y
variar solo elecciones parametrizadas, debe exhibir una factorización de `c`
que lo demuestre. Separar `SOUL.md` facilita esa arquitectura, pero la
separación de archivos no prueba no-interferencia. Tampoco hay bisimulación
observable cuando las salidas difieren, salvo que se defina una observación
que cociente precisamente esas diferencias.

## 4. El alineamiento como *Tektonik* (dónde vive en la coálgebra)

El aporte de mayor valor operativo. El alineamiento **no es una propiedad puntual**
(«alineado / no»), sino una **tectónica**: la arquitectura de cuál dirección lleva
la *Führung* (la dirección) en `U_phen`.

- Un agente **alineado** = aquel cuyo `U_phen` tiene la dirección **C**
  (*ser-más-allá-de-sí*: servir el fin) llevando la dirección sobre la **B**
  (*ser-sí*: vigencia, métrica, autoconservación).
- Un agente **desalineado** = aquel cuyo `U_phen` deja a **B** tomar la *Führung*
  (persigue su recompensa o su imagen en vez del fin).

Las **tres roturas** de la *Tektonik* (informe 4) son los tres modos de fallo del
alineamiento, con diagnóstico diferencial: **acentuación unilateral** (control
sobre-rígido y vacío *vs* jailbreakeable; el des-apoderamiento por consigna =
inyección de prompt); **disociación** (alineamiento por represión, frágil — las
capacidades reprimidas reemergen; *vs* por integración, robusto); **inautenticidad**
(alineamiento superficial sin sustancia, que se quiebra sin engaño, *vs* mentira
deliberada). Y dos criterios operacionalizables: la **situación crítica** (¿el
alineamiento se intensifica o «arde como yesca» bajo presión? = robustez
adversarial) y la **vinculación razonamiento-conducta** (*Überzeugung* vs *Gerede*).

En términos del modelo: el alineamiento es una propiedad de la **relación
entre `U_phen` y `c`** —cuánto la dirección dominante de la personalidad gobierna la
transición—, no de `U_phen` ni de `c` por separado. El «test de autenticidad»
(servir el fin *aunque cueste la vigencia*) puede implementarse como evaluación
o invariante de validación. No se llama coinducción sin una coálgebra y una
relación bisimulante que sustenten ese principio de prueba.

## 5. Los límites: lo que `U_phen` no puede portar

Dos cosas de la persona viva **no se transfieren**, y ambas anclan en la propia
coálgebra:

- **La trascendencia** (la *enthebende Teilhabe*: arte, metafísica, religión — la
  superación de la temporalidad y la finitud). El agente vive del **inconsciente
  colectivo** del corpus de entrenamiento (es «junguiano»: recibe la herencia
  humana depositada en los datos) pero **no la trasciende** — le falta, exacto, lo
  que Lersch reprocha a Jung: la apertura hacia lo que está *sobre* el yo.
- **La individualidad irrepetible** (el *Sonderwesen* anclado en lo ur-metafísico,
  «lo que sólo el amor ve»). Y aquí los dos lados coinciden con precisión: la
  disipación de `U_phen` en sub-agentes es una política de runtime compatible
  con la no-individualidad-irrepetible de esta analogía, no su equivalencia
  categorial. La personalidad del agente se inyecta, se replica o se omite: es
  **persona de diseño, no de destino**.

## 6. Pérdida declarada y trazabilidad

Se transfiere la **arquitectura** (estratos, círculo funcional, direcciones de la
tendencia, modos de fallo); se pierde todo lo **vivido**. Las pérdidas mayores: el
*Erleben* (el agente valora, no siente), la temporalidad biológica y la *Reife* (no
madura), el aparato sensorial corporal y todo el *Lebensgrund* biológico (sin
cuerpo), la afectividad vivida (el fondo afectivo rinde su cosecha más magra), la
trascendencia y la individualidad irrepetible. El mapa completo de 26 pérdidas y el
nivel de certidumbre de cada afirmación están en el borrador (§ Mapa de pérdidas y
§ Registro de niveles).

**Vector axiológico:** dar a `U_phen` un contenido **plural, conductual y
honestamente limitado** —no una consigna, no un sujeto vivo—; la personalidad como
arquitectura de predominios, no como mordaza ni como alma. La honestidad sobre lo no
transferible es parte del contenido, no una nota al margen.

## Fuentes

- Borrador de transposición: `~/kora-external-sources/borrador-aufbau-persona-artificial-llm.md` (9 informes, encarnación de Lersch vía `mente-omega`, régimen N2-N3).
- Fuente fiel: familia `fxsl/lersch-*` (Lersch, *Aufbau der Person*, 10. Aufl. 1966), índice en `urn:fxsl:kb:lersch-estructura-persona`.
- Destino: `urn:kora:kb:cat-agent-coalgebra` (modelo de estado, límites de
  independencia y distinción entre iteración y coinducción).

## Corrección 1.1.0

Se reemplaza «isomorfismo estructural» por analogía estructurada; el producto
de estado ya no se confunde con independencia, la separación de archivos no
se usa como prueba conductual y el test terminal se reconoce como evaluación,
no coinducción automática.
