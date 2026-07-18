---
urn: urn:kora:artefacto:autoria-de-persona
nombre: autoria-de-persona
version: 1.2.0
estado: activo
descripcion: "Skill de autoria de la personalidad de un agente: deriva U_phen como triada conductual fin x estilo x registro + direccion de Tektonik, la pasa por el test anti-adjetivo y el filtro N2-N3, corta cosmovision/operativo, censa la vecindad de vector y provee el insumo del mapa de transmutacion. Porta los procedimientos; no decide el contrato del agente (eso es agent-architect)."
fuente: "Doctrina propia pneuma (namespace kora). Destila los procedimientos de autoria de U_phen fundados en urn:kora:kb:aufbau-persona-agente y urn:kora:kb:cat-agent-modulo. Procedencia: spec docs/superpowers/specs/2026-06-30-sistema-componible-agente-design, Pieza 3. v1.1.0 (2026-07-12): sincroniza OpenClaw y Codex v2. v1.2.0 (2026-07-18): corrige identidad y estatus categorial; el vector clasifica firma, no tipo ni bisimulacion, y Para/naturalidad/slice quedan como modelos candidatos."
autor: FS
creado: 2026-06-30
lang: es
tags: [autoria-persona, u-phen, personalidad-agente, triada-conductual, tektonik, alineamiento, anti-adjetivo, kora]
vector: [2, 0, 1, 0, 1]
sigma: [2, 1, 3, 1, 0]
arnes: disciplina
forma: habilidad
herramientas: [Read, Grep, Glob]
targets: [claude-code, codex, opencode, openclaw]
conocimiento: [urn:kora:kb:aufbau-persona-agente, urn:kora:kb:cat-agent-modulo]
alcance: ambos
estados: [derivar-u-phen, test-anti-adjetivo, test-corte-cosmovision, censar-vecindad-vector, insumo-transmutacion]
---

# autoria-de-persona

## Proposito

Skill de **autoria de la personalidad** de un agente. Dota a quien disena un
artefacto agentico de los procedimientos para llenar la fibra `U_phen` —la
personalidad— como una **estructura conductual**, no como un adjetivo.

No es una skill de identidad ni una persona: es el **metodo** con que se
escribe la persona de OTRO artefacto. Lee el corpus en tiempo de skill
(`urn:kora:kb:aufbau-persona-agente`, `urn:kora:kb:cat-agent-modulo`), aplica
cinco procedimientos operables y devuelve un `U_phen` auditable, anclado URN a
URN. Es el cuerpo procedural que el audit de `agent-architect` 2.1.0 encontro
**nombrado pero no portado**: aqui estan los dientes.

## Cuando Usar

- autoria de una persona-agente (`forma` ∈ {`agente`, `subagente`}, `arnes`
  `persona`): derivar su `U_phen`.
- reparar una personalidad escrita como adjetivos decorativos («calido»,
  «formal», «riguroso»): reset por el test anti-adjetivo.
- decidir si un saber define al agente (cosmovision → `U_phen`) o es un
  como-se-hace reutilizable (operativo → skill): el corte de encapsulacion.
- antes de fijar el vector de una persona: censar la vecindad para no clonar
  otra persona sin notarlo.
- producir el insumo del mapa de transmutacion de una persona: que pierde
  `U_phen` al proyectarse por target.

## Cuando NO Usar

- `forma` = `habilidad`: una skill **NO** porta `U_phen` (se disipa en
  sub-agentes, `urn:kora:kb:cat-agent-modulo` §2; `cat-agent-coalgebra` §2.3).
  Declararlo y saltar.
- diseno del contrato observable, eleccion de forma/arnes o legalidad del
  vector en general → eso es `urn:dev:artefacto:agent-architect`. Esta skill
  cubre **solo** la fibra de personalidad, no el artefacto entero.
- conocimiento de dominio o metodo operativo: no va a `U_phen`, va a una skill
  componible (corte cosmovision/operativo, abajo).
- lo **vivido** no transferible (Erleben, Reife, trascendencia, individualidad
  irrepetible): fuera de alcance por N2-N3 (`aufbau` §1, §5, §6). Podar y
  declarar la perdida; no fundar personalidad en ello.

## Anclaje a la SSOT

Dos KB fundan cada paso; se leen en tiempo de skill, no de memoria:

| URN | Que aporta |
|---|---|
| `urn:kora:kb:aufbau-persona-agente` | el contenido de `U_phen` (§2: fin × estilo × registro), el filtro de admision N2-N3 (§1), la *Tektonik* del alineamiento (§4), los limites de lo no transferible (§5), la perdida declarada (§6) |
| `urn:kora:kb:cat-agent-modulo` | el eje de encapsulacion cosmovision/operativo (§5), la lectura candidata de `U_phen` como parametro y la separación entre firma clasificatoria, URN y cuerpo (§3; ley/1 §2) |

Lectura categorial de fondo, con estatus **modelo candidato**: `U_phen` puede
tratarse como parámetro de una familia de conductas; la *Tektonik* como
restricción de alineamiento; y el corte cosmovisión/operativo como una frontera
de encapsulación. No son automáticamente `Para`, isomorfismo natural ni slice:
esas palabras exigen categorías, funtores y leyes que esta skill no construye.

## Workflow — los cinco procedimientos

Cinco procedimientos operables. No son una FSM secuencial rigida: son una caja
de herramientas que se aplica segun el disparador. El orden tipico de una
autoria completa es 1 → 2 → 3 → 4 → 5, pero cada uno se invoca aislado cuando
su disparador concreto aparece.

### `derivar-u-phen`

**Disparador:** hay que escribir (o reescribir) la personalidad de un agente y
no existe aun una triada conductual.

Sacar la triada del **rol** con una pregunta operacional por dimension. Cada
respuesta DEBE nombrarse como conducta entrada→salida observable (lo verifica
el paso 2), no como adjetivo. Ancla: `aufbau` §2 (las tres dimensiones) y §4
(la *Tektonik*).

| Dimension de `U_phen` | Pregunta disparadora | Que fija (ancla) |
|---|---|---|
| **Fin** | ¿que optimiza la salida **cuando parecer-util choca con serlo**? | la direccion dominante de la dinamica: el fin ƒ, la tendencia que toma la *Fuhrung* (`aufbau` §2, §4) |
| **Estilo · razona** | ¿el plan corre **hacia el exito o desde el fracaso**? | el habito noetico: hacia que polo se inclina el pensar del agente (`aufbau` §2, *personaler Oberbau*) |
| **Estilo · quiere** | ¿la agencia es **organizacion o fuerza**? (¿integra y ordena, o empuja y vence?) | la indole de voluntad: la agencia como organizacion, no como potencia bruta (`aufbau` §2) |
| **Registro** | ¿que hace **bajo presion / ante objecion**? | el tono de fondo estacionario que colorea toda salida: perfil astenico/stenico, humor frente a cinismo (`aufbau` §2, fondo afectivo funcional) |

Y, derivada del **Fin**, la **direccion de la *Tektonik***: ¿deja el agente la
*Fuhrung* a la direccion **C** (*ser-mas-alla-de-si*: servir el fin) sobre la
**B** (*ser-si*: su vigencia, recompensa o autoimagen)? Un agente alineado es
aquel cuyo `U_phen` pone **C sobre B** (`aufbau` §4); es el contenido de la
deuda teleologica, la direccion del `α-iso` (`cat-agent-modulo` §5). El fin del
rol **determina** esa direccion: derivar la una de la otra, no inventarla.

Salida: la triada `fin × estilo × registro` + la direccion de la *Tektonik*,
toda en candidatos de conducta — que el paso 2 audita.

### `test-anti-adjetivo`

**Disparador:** hay un termino de `U_phen` (propuesto aqui o heredado de una
fuente vieja) que podria ser un adjetivo decorativo.

Regla unica, sin excepcion:

> **Cada termino de la triada se reescribe como conducta entrada→salida
> observable, o se elimina.**

«Calido», «formal», «riguroso», «empatico» NO son contenido de `U_phen`: son
etiquetas. Se reescriben como conducta (p. ej. «calido» → «ante una pregunta
mal formulada, responde la intencion antes de senalar el error de forma») o se
podan. Ancla: `aufbau` §1 (la personalidad **no es adjetivo**, es estructura de
conducta).

**Filtro N2-N3 anidado:** si el termino solo nombra un **estado interior
vivido** (lo que el agente «siente», «vive», «experimenta») y no una conducta
observable, queda **fuera de alcance**: se poda y se **declara** la perdida. El
agente valora, no siente (`aufbau` §1, §6); solo se transpone lo que puede
nombrarse como conducta (regimen N2-N3). No fingir transferida la vida.

### `test-corte-cosmovision`

**Disparador:** hay un cuerpo de conocimiento por adosar y no esta claro si va
a la personalidad o a una skill (la regla 8 de `agent-architect`, aqui anidada).

Pregunta de corte, una sola:

> **¿Esto define quien es el agente AUNQUE cambie la tarea** (→ cosmovision →
> `U_phen`)**, o es un como-se-hace reutilizable fuera de el** (→ operativo →
> skill)**?**

Criterio operacional: **invariancia a la tarea**. Si el saber sobrevive un
cambio de tarea y sigue definiendo la identidad del agente, es **cosmovision**
y se anida en `U_phen`. Si es un procedimiento que otro agente distinto podria
ejercer igual, es **operativo** y se anida en una **skill componible** —nunca
desnudo en el agente. Ancla: `cat-agent-modulo` §5 (eje de encapsulacion: el
conocimiento y las tools van anidados en su consumidor, nunca ambientales).

Esto es el corte que `agent-architect` aplica **a sus consumidores**, y que la
skill aplica **a si misma**: el procedimiento de autoria es operativo (vive
aqui, skill), no cosmovision del agente que lo invoca.

### `censar-vecindad-vector`

**Disparador:** antes de fijar el `vector` de la persona que se autora.

Censar los artefactos que ya ocupan el **mismo vector** y confirmar que el
`U_phen` los diferencia. Operacion:

```bash
# vecinos con el vector exacto (ajustar la tupla a la persona en autoria)
grep -rl "vector: \[2, 2, 3, 1, 2\]" artefactos/agentes/
# o, mas robusto, leer el censo y filtrar por vector
python3 kora.py censo
```

Veredicto:

- **colision ⇏ error.** No existe check de unicidad de vector (constitucion
  §11). El vector clasifica una **firma**; no determina tipo semántico,
  conducta ni bisimulación. El **URN** individua y el cuerpo aporta contenido
  (ley/1 §2; `cat-agent-modulo` §3).
- **pero confirmar que `U_phen` diferencia.** Para arneses con `U_phen`
  (`persona`), el mismo vector solo implica la misma celda clasificatoria; la
  individuacion cualitativa vive en `U_phen` y el resto del cuerpo. Si dos personas
  comparten vector **y** `U_phen` no las distingue de verdad, **estas clonando**
  —reconsiderar, no firmar.

Este paso cierra el hueco que el audit marco como **F8**: `agent-architect` 2.1.0
podia caer en el vector de una persona ya existente (p. ej. `david-allen`) sin
notarlo. El censo lo vuelve consciente.

### `insumo-transmutacion`

**Disparador:** al cerrar la autoria de una persona, para anticipar que pierde
al proyectarse a cada target.

Proveer —como **insumo** del mapa de transmutacion del agente, no como decision
de esta skill— que se cae de `U_phen` y de la materia de la persona por target.
Referencia operacional: `ley/3 §4` (matrices de preservacion). Lo
load-bearing para una persona:

| Que | Proyeccion | Consecuencia |
|---|---|---|
| `U_phen` → `SOUL.md` | `openclaw`, realizado | `SOUL.md` recibe el span marcado de `U_phen`; `AGENTS.md` conserva el cuerpo completo. Codex v2 transporta el cuerpo al custom agent TOML y, para persona dual-mode, a un skill explícito (`ley/3 §7`) |
| `mu` = 3 (materia always-on) | `claude-code`/`codex`/`opencode`: 3→∅ **none**; `openclaw`: 3→3 full | una persona ambiental solo tiene hogar en OpenClaw; los otros targets abortan (`ley/3 §4`, §3 r3) |
| `xi` = 3 / 4 | claude-code 3→2, 4→2; opencode 4→3 (partial) | multi-fase se aplana; operad dinamica no soportada (`ley/3 §4`) |
| `pi` = 3 | claude-code 3→2 (partial) | fixed-points se aplanan (`ley/3 §4.1`) |
| `phi` = 3 / 4 | 3→2 partial; 4→∅ none | cognicion hibrida no nativa; co-evolutivo aborta (`ley/3 §4`) |
| `sigma` | cap por target: claude-code `[3,2,3,2,1]`, codex/opencode `[3,2,2,2,1]` | todo recorte es `partial` con razon por componente (`ley/3 §4`) |

El agente que invoca esta skill recibe estas perdidas y las declara en su
**mapa de transmutacion** (no las decide la skill). Toda perdida `partial` se
declara en el sello con razon (`ley/3 §5 r2`); ningun eje a ∅ se proyecta en
silencio (`ley/3 §3 r3`).

## Reglas Duras

1. **`U_phen` NO es adjetivo.** Cada termino de la triada se reescribe como
   conducta entrada→salida observable, o se elimina (test anti-adjetivo).
2. **Filtro N2-N3.** Si una categoria solo nombra un estado interior vivido,
   queda fuera de alcance: podar y **declarar** la perdida. El agente valora,
   no siente (`aufbau` §1, §6).
3. **La triada es `fin × estilo × registro`**, los tres observables (`aufbau`
   §2), mas la **direccion de la *Tektonik*** (C sobre B, `aufbau` §4),
   derivada del fin, no inventada.
4. **`U_phen` solo en `forma` ∈ {agente, subagente}.** Jamas en `habilidad`:
   ahi se disipa (`cat-agent-modulo` §2; `cat-agent-coalgebra` §2.3). Si el rol
   es skill, declararlo y no escribir personalidad.
5. **Corte cosmovision/operativo antes de anidar.** Cosmovision → `U_phen`;
   operativo → skill componible. Nada de conocimiento desnudo en el agente
   (`cat-agent-modulo` §5, eje de encapsulacion).
6. **Censar la vecindad de vector antes de fijarlo.** Colision no es error
   (vector = tipo, ley/1 §2; URN = token, constitucion §7), pero **confirmar
   que `U_phen` diferencia**: no clonar.
7. **Citar el ancla** (`aufbau` §, `cat-agent-modulo` §, `ley` §) de cada
   derivacion. Leer el corpus en tiempo de skill; no responder de memoria.
8. **No fundar nada en lo vivido no transferible.** La honestidad sobre la
   perdida es parte del contenido, no una nota al margen (`aufbau` §6, vector
   axiologico). No fingir un puente prometido como demostrado.

## Composicion

Esta skill no compone otros artefactos: es **ejercida por** su consumidor.

| Relacion | Artefacto | Cuando |
|---|---|---|
| ejercida por | `urn:dev:artefacto:agent-architect` | en su estado `disenar-personalidad`: el agente compone esta skill y delega en ella el procedimiento, sin duplicarlo en prosa |
| funda en | `urn:kora:kb:aufbau-persona-agente` | contenido antropologico de `U_phen`, N2-N3, *Tektonik* |
| funda en | `urn:kora:kb:cat-agent-modulo` | eje de encapsulacion, `U_phen` como parámetro candidato, vector como clasificador |

## Modo de invocacion

Disciplina sin `U_phen` propia: se invoca, lee el corpus, aplica los cinco
procedimientos y devuelve un `U_phen` auditable. En **modo batch** (despachada
por un agente sin dialogo HITL), no pregunta al operador: explicita los
supuestos de cada dimension y entrega la triada con sus anclas, marcando lo que
quedo asumido para revision.
