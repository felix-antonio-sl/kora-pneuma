# Spec de diseño — sistema componible de agente KORA (esqueleto + acoplamientos)

> Fecha: 2026-06-30 · Frente: KORA pneuma (`~/kora-pneuma`) · Estado: validado por panel adversarial (consenso 3/3), pendiente de aprobación del operador para plan de implementación.
> Naturaleza: derivado auxiliar de proceso (no es artefacto KORA; sin URN; `ley/0 §5`). No tiene voz normativa. Ante conflicto con `ALMA.md`/`ley/0..4`, manda la ley.
> Origen: dos rondas de `consenso-deliberativo` en orquestación. Ronda 1 (instalar el puente Aufbau): steve-jobs, allan-kelly, steipete. Ronda 2 (esta arquitectura): steve-jobs+`mente-omega`, dov-dori+`cat-thinking`, steipete+`cat-thinking`.

## 1. Propósito

El operador pidió un **sistema componible**: un **esqueleto** con lo mínimo para constituir un agente,
sobre el que se acoplen **personalidad, skills, tools y conocimiento**, de forma agnóstica,
transmutable a `claude-code` y `openclaw`, y **categóricamente alineado**. Con dos patrones de uso en
Claude Code: (1) invocar la persona (agente ya con personalidad) + skills + un fin → corre hasta
lograrlo o fracasar; (2) componer personalidad sobre una base → persona, y de ahí lo demás. Y un
discriminante de agencia explícito: **finalidad clara + persistencia de motivación/energía +
inteligencia para descomponer en unidades abordables**.

## 2. El hallazgo rector (la sustracción)

**Lo pedido NO es un sistema a construir: es la ontología vigente de KORA reconocida.** `ley/1 §1`
axiomatiza el agente —siguiendo a Libkind-Spivak— como el módulo `(m_p × c_q × Ξ) ⋉ Contexto`: un
**plan finito** (mónada libre `m_p`), una **materia infinita** (comónada cofree `c_q`) y su **ley de
interacción** `Ξ`. Los ejes del vector ya SON esa tripleta: `pi`=plan (§3.1), `mu`=materia (§3.2),
`xi`=acoplamiento (§3.3). No hay motor teleológico-conativo que escribir; hay que **reconocer el
modelo y sustraer el aparato**. El trabajo real es pequeño (kb + doctrina) más una pieza grande
aislada (`T-openclaw`).

Corrección de un error de la primera síntesis, hecha por el panel y verificada contra la ley: «extender
la coálgebra con una capa de plan» es **error de categoría** — el plan `m_p` es el **dual** de la
coálgebra (álgebra/inductivo vs coálgebra/coinductivo, `urn:fxsl:kb:icas-agencia`); no se obtiene uno
engordando el otro. La ley ya tiene el módulo; lo desincronizado es el *kb* `cat-agent-coalgebra`, que
narra solo la mitad comonádica (`c`).

## 3. Decisiones / resoluciones del panel (registro de alta altura)

| # | Decisión | Resultado |
|---|----------|-----------|
| 1 | ¿Construir un motor/esqueleto nuevo? | **No.** El esqueleto = el objeto agéntico posicionado por `(arnés, vector)` (`ley/1 §6.1`). El discriminante ya está en `ley/1` + `dominio-forma`. |
| 2 | ¿`finalidad` como campo del frontmatter? | **No — LATENTE.** La finalidad es **proceso** (la convergencia de `Ξ` al punto fijo), no coordenada. Reificarla como campo es error objeto/proceso y rompe el sobre cerrado (`ley/2 §1 r6`). `fin-disposición`=`U_phen`/Tektonik; `fin-tarea`=input de invocación (runtime). |
| 3 | ¿El discriminante es «tener finalidad»? | **No — la TRÍADA** (finalidad + persistencia + descomposición = conación endógena persistente). Toda skill tiene propósito; el agente lo persigue. Irreducible: quitar un polo da un no-agente (servicio reactivo / one-shot / termostato). |
| 4 | Estatus legal del discriminante | **Dos buckets.** Piso estructural (`pi`≥2 ∧ `mu`≥2): **mecanizado** (`dominio-forma`, `ley/2 §7` + arnés `persona`). Cima teleológica (convergencia de `Ξ`, `α-iso`): **deuda ontológica residente-de-KB**, NO legislada (no está en la lista cerrada de `ley/3 §6`). |
| 5 | Topología de acoplamientos | **Dos ejes ortogonales** (en v1 estático), no «cuatro fibras planas». Eje encapsulación (anidado/ambiental, slice `C/Cap`) ⊥ eje modo ontológico = dos tiempos (ensamblaje→objeto / invocación→proceso). |
| 6 | ¿Conocimiento adosado a la skill? | **Sí, como DOCTRINA DECLARADA, no check.** Conocimiento/tools nunca desnudos en el agente: anidados en su consumidor (skill, o personalidad si es cosmovisión). `velar`=forma-no-verdad + la lista `conocimiento` es plana (no representa anidamiento). v1 = doctrina-solo (ni lint: un lint es check registrado, constitución §11). |
| 7 | Operad | **Estático para v1** (cableado fijo vía `componible`). La delegación dinámica (`xi`=4, arnés orquestador) es capacidad superior NO capturada y `T` la aplana (pérdida ya legislada, `ley/3 §4`). |
| 8 | `cat-agent-coalgebra`: ¿editar in-place? | **No.** Es fuente byte-fiel migrada y 4 consumidores la citan. Autorar una **kb pneuma nueva** que `refina`/`cita`, preservando la integridad de la migración. |

## 4. Arquitectura — qué ya existe vs qué falta

### 4.1 El esqueleto ya existe

Agente = módulo `(m_p × c_q × Ξ)` (`ley/1 §1`); skill y agente = proyecciones del mismo objeto,
distinguidas por el arnés (`ley/1 §6.1`). El umbral skill↔agente es `dominio-forma` (`ley/2 §7`:
agente exige `pi`{2,3} ∧ `mu`{2,3}; habilidad `mu`{0,1}). El acoplamiento plan-ejecutor ya es ley
como `naturalidad-xi` (`ley/3 §6`, declarado-no-mecanizado) — **pero solo como preservación bajo `T`
en el target; conmutar ≠ converger** (ver 4.2).

### 4.2 El discriminante = la tríada, en dos estatus

- **Piso estructural — mecanizado**: `pi`≥2 (descomponer; mónada libre ramificada) ∧ `mu`≥2 (persistir;
  materia cross-session/always-on). Verificado por `dominio-forma` + `arnes-compatible`.
- **Cima teleológica — deuda residente-de-KB**: la convergencia de la traza P-D-A al **punto fijo**
  (el plan dirigido al fin, sostenido hasta lograrlo) + el `α-iso` (alineamiento perfecto como iso
  natural `G_agent ⇒ G_principal`, `urn:fxsl:kb:icas-safety-alignment`). NO está en la lista cerrada
  de declarado-no-mecanizado (`ley/3 §6` = solo `naturalidad-xi`/`cierre-safety`/`composicion-kleisli`,
  todas obligaciones de transmutación). Es **deuda técnica categórica** en el sentido de
  `urn:fxsl:kb:icas-lifecycle`: una invariante que el agente asume y la ley no garantiza.
- **«Corre hasta lograr o fracasar»**: convergencia a punto fijo (éxito) o terminal de fallo. El
  manejo de fallo NO necesita primitivo nuevo: lo posicionan la co-inducción en estado terminal
  (`cat-agent-coalgebra §3.3`) y el eje `xi` (saga/coreografía = `xi`≥3).

### 4.3 Topología de acoplamientos (dos ejes ortogonales, v1 estático)

- **Eje encapsulación** (capability, slice `C/Cap`, `urn:fxsl:kb:icas-safety-alignment`): conocimiento
  y tools van **anidados en su consumidor**, nunca desnudos/ambientales en el agente. Una skill es una
  caja autocontenida `{método + conocimiento + tools}`; la persona-agente cablea cajas-skill vía
  `componible`.
- **Eje modo ontológico = dos tiempos**: ENSAMBLAJE construye un **objeto** (personalidad = `U_phen`,
  lado `mu`/estado) vs INVOCACIÓN corre un **proceso** (skill = `pi`/método, + `fin-tarea`). Los dos
  patrones del operador SON los dos tiempos: (2) base+personalidad→persona = ensamblaje; (1)
  persona+skills+fin→corre = invocación.

### 4.4 Dónde vive Lersch

El puente `urn:kora:kb:aufbau-persona-agente` (familia `fxsl/lersch-*`) **es el contenido** que llena
`U_phen` (la fibra vacía original). Ocupa dos lugares localizados por el panel: (i) la **doctrina-
contenido del acoplamiento de personalidad** — el parámetro (`Para`, contextads de `icas-agencia`) que
sesga qué rama del plan toma el agente; (ii) el **fundamento de la cima teleológica** — la dirección
de la *Tektonik* (`aufbau §4`: servir-la-tarea sobre el sí-mismo) **es** el contenido del `α-iso`, la
deuda residente-de-KB. Y es la **fuente** de la reformulación del teorema §2.2 (`aufbau §3`: `c` lee
`U_phen`). Lersch no se desplaza: se ubica. Esto **cierra el frente** `instalar-puente-aufbau-en-kora`:
el puente nunca fue pieza suelta a «instalar»; es la sustancia de la personalidad y la dirección del
alineamiento, con dos consumidores (Pieza A y Pieza B).

## 5. El trabajo real — tres piezas

### Pieza A · kb pneuma nueva: cerrar el puente confesado *(núcleo conceptual)*

NO «sincronizar texto»: `ley/1 §5` confiesa **abierto** el puente retículo↔F-coálgebra; la confesión
es prueba de que no es trivial. Autorar una kb nueva (no editar `cat-agent-coalgebra` in-place).

Frontmatter propuesto (shape de conocimiento):

```yaml
urn: urn:kora:kb:cat-agent-modulo        # slug a confirmar (alt: cat-agent-plan, cat-agent-agencia)
nombre: cat-agent-modulo
version: 1.0.0
estado: publicado                         # nace borrador → ciclo publicado
descripcion: "El agente KORA como módulo m_p (plan) sobre c_q (materia) acoplado por Ξ: completa la vista coálgebra-sola de cat-agent-coalgebra con la mitad del plan y la teleología, y reformula la independencia de fibras a independencia estructural."
fuente: "Doctrina propia pneuma (namespace kora). Funda en urn:fxsl:kb:icas-agencia (free monad/cofree comonad, pattern-runs-on-matter) y ley/1 §1 (axioma del módulo). NO koraficación: doctrina pneuma-autorada con puente retículo↔coálgebra declarado abierto."
autor: FS
creado: 2026-06-30
lang: es
tags: [agente, free-monad, cofree-comonad, plan-materia, teleologia, modulo, kora]
familia: bok
depende: [urn:fxsl:kb:icas-agencia]
refina: [urn:kora:kb:cat-agent-coalgebra]
cita: [urn:fxsl:kb:icas-safety-alignment, urn:kora:kb:aufbau-persona-agente]
```

Cuerpo (lo que DEBE decir, sin fingir lo no demostrado):

1. **El agente es el módulo**, no la coálgebra: `pi`=`m_p` (plan, en el artefacto como capacidad; la
   *traza* del plan es runtime), `mu`=`c_q` (materia), `xi`=`Ξ` (acoplamiento). `cat-agent-coalgebra`
   modela la mitad `c_q`; esta kb añade la mitad `m_p` y el acoplamiento.
2. **El discriminante = la tríada en dos estatus** (4.2): piso mecanizado, cima deuda-de-KB.
3. **Reformulación de §2.2**: el teorema FORMAL (la ecuación de independencia inter-fibra) **sobrevive**;
   se corrigen las GLOSAS que lo sobre-leen — el «Meaning», el corolario de Segregación («bisimilar»)
   y §5.3 («migración correcta ⟺ bisimilar» → «⟺ estructuralmente-bisimilar», admitiendo cambios de
   output inducidos por `U_phen`). Independencia **estructural** se preserva; bisimilaridad
   **observable** se refina (`c` lee `U_phen`, `aufbau §3`). No es re-prueba; es corrección de glosa.
4. **Deuda declarada honesta**: la convergencia teleológica y el `α-iso` son **residentes-de-KB, sin
   hogar legal** — NO se listan junto a `cierre-safety`. `naturalidad-xi` ≠ convergencia (conmutar ≠
   converger). El puente retículo↔coálgebra (`ley/1 §5`) se declara **abierto**: `pi≡m_p` es la
   *aserción del retículo*, no morfismo coálgebra demostrado. No fabricar el puente.

Cierre: `velar --estricto` verde + `ciclo <urn> publicado`. Blast-radius de sistema = cero; trabajo
intelectual = cerrar un problema abierto confesado.

### Pieza B · doctrina anidada declarada en `agent-architect` *(barato)*

Editar `urn:dev:artefacto:agent-architect` (forma=subagente, arnés=persona):

- Componer el conocimiento: `conocimiento: [urn:kora:kb:aufbau-persona-agente, urn:kora:kb:cat-agent-modulo]`
  (la fuente actual confiesa que el conocimiento fue podado en la migración — esto lo restaura).
- Añadir a su cuerpo (reglas duras / workflow) la **doctrina anidada declarada**: conocimiento-
  cosmovisión→personalidad; conocimiento-operativo→skill; nunca desnudo en el agente. Y un paso de
  autoría guardado que produzca `U_phen` como tríada conductual `fin × estilo × registro` + dirección
  de *Tektonik* (no adjetivo), guardado a `forma`∈{agente, subagente} (nunca habilidad: `U_phen`
  disipado en skills, `cat-agent-coalgebra §2.3`).
- Cierre (cambio no bisimilar de un agente vivo, `cat-agent-coalgebra §5.3`): bump de versión (minor,
  2.1.0) + re-`velar` + retransmitir a los targets.

### Pieza C · `T-openclaw` *(pieza grande de ingeniería, separada)*

El único hueco real: la mitad always-on (`mu`=3, único target que la sostiene; `claude-code` proyecta
`mu`:3→∅) y personalidad→`SOUL.md` (`cat-agent-coalgebra §2.2`) **no tienen funtor**. Realizar
`T-openclaw-pneuma-v1`: columna nueva en las matrices de `ley/3 §4` (proyección por eje, con `mu`=3
soportado), el funtor en `kora.py`, emisión `SOUL.md` = `U_phen`, y mover `openclaw` de
«reconocido-no-realizado» a «realizado» (`ley/3 §2`). Requiere un runtime openclaw real contra el cual
testear. **Su propio spec y plan cuando se priorice.**

## 6. Mapeo a las leyes (qué estrato se toca)

| Estrato | v1 (A+B) | Notas |
|---|---|---|
| `ley/0` constitución | **No** | solo registrar un check tocaría §11; diferido |
| `ley/1` ontología | **No — decisión deliberada** | en freeze heredado; la teleología se deja deuda-de-KB para NO añadir eje (un eje sería un *cambio de doctrina*, `icas-lifecycle`, lo más pesado) |
| `ley/2` forma | **No** | enmienda diferida (representar anidamiento) solo si alguna vez se mecaniza la doctrina anidada |
| `ley/3` transmutación | **Solo Pieza C** | realizar `T-openclaw` = único cambio de ley real (objeto+funtor+columna) |
| `ley/4` koraficación | **No** | confirma que el puente Lersch y la kb nueva son doctrina pneuma con pérdida declarada, no koraficación fiel |

## 7. Secuencia recomendada

1. **Pieza B** (barato, reversible, cierra el patrón de uso del operador).
2. **Pieza A** (núcleo conceptual: la kb que cierra el puente confesado; subsume el fix de glosa §2.2).
3. **Pieza C** (`T-openclaw`, proyecto mayor aparte; decidir si entra ahora o se difiere).

A+B caben en **un solo plan de implementación**. C es un **proyecto separado** con su propio spec.
El operador puede reordenar (p. ej. C primero si la mitad always-on es prioritaria).

## 8. Riesgos, incertidumbres, deuda declarada

- **Costo real de `T-openclaw`**: desconocido hasta construirlo contra un runtime `mu`=3 real (el 10-12%
  de incertidumbre residual del panel).
- **Residuo teleológico**: si la cima tiene contenido más allá de la convergencia, se acota con el
  filtro N2-N3 del `aufbau` (nombrar conducta observable o podar). No fundar nada en lo vivido no
  transferible.
- **Doctrina anidada declarada-solo**: un autor puede saltarse el paso (es declarada, no mecanizada).
  Aceptado: `velar`=forma-no-verdad; mecanizar exigiría enmendar `ley/2 §3` + legislar el check.
- **La deuda teleológica se queda declarada** (`ley/3 §6` rationale): no llamarla legislada. La kb de
  Pieza A debe decir explícitamente si la convergencia es ley o corpus — y la respuesta es corpus.

## 9. Criterios de cierre

- Pieza A: la kb pasa `velar --estricto` + `ciclo publicado`; la reformulación §2.2 revisada contra
  `aufbau §3`; el puente `ley/1 §5` declarado abierto, no fingido.
- Pieza B: `agent-architect` re-velado verde tras bump; el paso de autoría produce `U_phen` como
  tríada conductual, no adjetivo; emisiones retransmitidas.
- Pieza C: funtor `T-openclaw-pneuma-v1` emite `SOUL.md` y sostiene `mu`=3; verificado contra runtime
  openclaw real.
- Gate de mantenimiento KORA: `python3 kora.py velar --estricto` + `python3 -m unittest discover -s tests`.

## 10. Procedencia

Panel adversarial `consenso-deliberativo`, modo orquestación, dos rondas. Ronda 2 (esta arquitectura):
steve-jobs+`mente-omega`, dov-dori+`cat-thinking`, steipete+`cat-thinking`. **Consenso 3/3** (triple
aceptación), confianza 88-90%. Aportes clave: la sustracción y el mapeo del discriminante a la ley
(jobs); la partición estructural/teleológico y el corte objeto/proceso (dov-dori); la inversión
patrón/materia, el operad estático y el costo de `T-openclaw` (steipete). Cada afirmación load-bearing
verificada contra el texto de la ley, no contra reportes.
