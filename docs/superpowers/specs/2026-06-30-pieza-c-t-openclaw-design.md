# Spec de diseño — Pieza C: el funtor `T-openclaw-pneuma-v1`

> Fecha: 2026-06-30 · Frente: KORA pneuma (`~/kora-pneuma`) · Estado: validado por panel adversarial (consenso 3/3, 1 ciclo de refutación), autorizado por el operador para plan de implementación.
> Naturaleza: derivado auxiliar de proceso (no es artefacto KORA; sin URN; `ley/0 §5`). No tiene voz normativa. Ante conflicto con `ALMA.md`/`ley/0..4`/`GENESIS.md`, mandan ellos.
> Origen: panel `consenso-deliberativo`, modo orquestación. Expertos: dov-dori (ontología objeto/proceso), cat-thinking (teoría de categorías aplicada, corpus ICAS-BoK), steipete (disciplina de envío). Fundado contra estado real verificado (`kora.py`, `~/openclaw-fleet`, `~/kora` legacy, doc Hermes), no contra reportes.
> Precede a: la tercera y última pieza diferida del spec `2026-06-30-sistema-componible-agente-design.md` (§5 Pieza C). Las Piezas A+B están cerradas y desplegadas (HEAD `17121dc`).

## 1. Propósito

Realizar `T-openclaw-pneuma-v1`: el funtor de transmutación que hoy hace que `transmutar --target openclaw` aborte. Hoy `openclaw` está «reconocido por la ley, no realizado» (`GENESIS.md §4`; `ley/3 §2`). La Pieza C lo mueve a «realizado», saldando esa fila de la deuda — y **solo esa fila**.

Dos sub-problemas que el spec del sistema componible nombró como diferidos:

1. **La mitad always-on `mu=3`**: `openclaw` es el único runtime cuyo techo admite materia ambiental (comónada cofree bisimilar con eventos externos, `ley/1 §3.2`). Los tres funtores vivos abortan `mu=3` (`claude-code` con `none`, «sin ambiente always-on; usar openclaw», `kora.py:851`).
2. **El puente `U_phen → SOUL.md` sin funtor**: la personalidad se proyecta a un `SOUL.md` como puente declarado, no como funtor estructura-preservante. Hay que legislar esa asimetría sin fingir un funtor que no es.

Restricción ya fijada por el operador (decisión rectora previa al panel): **emisión byte-determinista** (la vara de los tres funtores vivos, verificados por tests de emisión, no corriendo el runtime) y **anatomía pneuma-mínima** (un artefacto compacto + sello inline, no el workspace de ~10 archivos + sidecar de la encarnación bestia).

## 2. El hallazgo rector

**`openclaw` no introduce un régimen nuevo: revela uno que ya existía.** `emitir()` hoy hace, para los tres targets vivos, dos operaciones distintas en un mismo acto: la **proyección funtorial del vector** (`proyectar()`, `min` sobre la matriz, `kora.py:979`) y la **copia verbatim del cuerpo** (`_componer(fm, art.cuerpo, …)`, `kora.py:1110`). `U_phen` viaja hoy embebido en el cuerpo markdown — invisible, porque nadie lo extrae.

La formalización (cat-thinking, anclada en `urn:fxsl:kb:icas-extension`): el artefacto-agente no vive en el retículo PMI×LFS; vive en el **espacio total de una fibración de Grothendieck sobre él**. Base `B` = el retículo de vectores (lo que `ley/3` proyecta por `min`). Fibra sobre `v` = el espacio cualitativo **abierto** de los `U_phen` compatibles — exactamente lo que `ley/1 §2 v1.1.0` declara no-coordenado. Espacio total `E` = los artefactos reales `(v, φ)`.

- **El funtor `T` que legisla `ley/3` es el funtor de la BASE** (`T: B_IR → B_runtime`, proyección por `min`).
- **El transporte verbatim del cuerpo no es `T`**: es la componente-sobre-la-fibra de un funtor cartesiano más grande `T̃` que yace sobre `T`. `T̃` es **idéntico** en los cuatro targets; lo único que cambia es que la fibración destino de `openclaw` **está escindida** (`SOUL.md` = fibra, ⊥ `openclaw.json`/config = base). Por eso `openclaw` hace **sintáctica** la asimetría que en `claude-code` queda oculta: no la crea, la materializa en archivo aparte.

Consecuencia de ingeniería: `T-openclaw` resulta casi isomorfo a `T-claude-code` en estructura de emisión —un archivo = cuerpo + sello— difiriendo en (1) la matriz, (2) la ausencia de frontmatter (el `SOUL.md` es markdown libre), (3) la confesión del sello. La pieza «más grande» es una variación acotada de la más pequeña, no un subsistema nuevo.

## 3. Decisiones del panel (registro de alta altura)

| # | Decisión | Resultado | Autor / estatus |
|---|----------|-----------|-----------------|
| 1 | ¿Uno o dos archivos de emisión? | **Un archivo**: `SOUL.md` = cuerpo verbatim **sin frontmatter** + sello inline. El loader `openclaw` arranca de bootstrap-text inyectado + su propio `openclaw.json`; las capabilities son deploy-side; Hermes auto-bootstrapea slots ausentes. Un archivo basta. | cat-thinking concedió su tesis de dos archivos contra estado real; unánime |
| 2 | ¿Reusar la rama `claude-code` de `emitir()`? | **No.** Esa rama envuelve en fences YAML (`_componer()`, `kora.py:1110`); el `SOUL.md` de Hermes es markdown libre **sin** frontmatter, inyectado verbatim en slot #1. Reusarla emitiría `---\nname:…\n---` que Hermes inyecta como ruido de identidad. Requiere `+1 rama en _componer()` (modo sin-frontmatter). | steipete (era CRÍTICA), verificado contra `~/openclaw-fleet/workspaces/steipete/SOUL.md` |
| 3 | ¿Cómo legislar el transporte de `U_phen`? | **Tercera capa, no tercer régimen.** Transporte de fibra (componente fibrada de `T̃` sobre `T`); no componente de `T`, no transformación natural. `U_phen` sin coordenada no cae en los dos baldes de `ley/3 §6`. Legislado **una vez** en `ley/3` como prosa, aplica a todos los targets; **sin** campo por-emisión en el sello (sería falso-por-asimetría). | cat-thinking (nombre); dov-dori cedió su «línea en el sello»; steipete (prosa, no texto categorial) |
| 4 | ¿La pérdida de capacidad vacía la frontera? | **No.** La clausura `F` (tool-SET, portador de `cierre-safety`, **tipo**) se **declara** en el sello; solo el binding (enforcement allow/deny → `openclaw.json`, **token**) se difiere. Si no, `openclaw` sería el único target que deja `cierre-safety` sin referente. | cat-thinking (enmienda MENOR) |
| 5 | ¿`mu:3→3 full` esconde un puente prometido? | **No, si se califica.** `full` = el **techo** del runtime admite always-on sin truncamiento de `min` (*tipo/sintaxis*), no que el always-on conductual esté verificado (*token/semántica*). El substrato `mu=3` es estado de runtime acumulado (`MEMORY.md`/`USER.md` snapshot-inyectados + gateway), inherentemente no-emitible. La calificación es **observable en el sello** (no solo en la ley). | steipete (frontera); dov-dori (CRÍTICA-estrecha: observable en el sello) |
| 6 | ¿`--aplicar` para `openclaw`? | **No en esta Pieza C.** No por minimalismo: Hermes prohíbe sobrescribir un `SOUL.md` existente; el modelo clobber de `RUTAS_APLICAR` lo violaría. Emisión canónica a `_emision/openclaw/agents/{nombre}/SOUL.md`, como la bestia, que tampoco auto-desplegó. | steipete (verificado en doc Hermes) |
| 7 | ¿Qué deuda salda? | **Solo la fila `openclaw` de GENESIS §4.** No la deuda teleológica de `cat-agent-modulo` (convergencia/`α-iso`, residente-de-KB), no el puente `ley/1 §5`, no `hermes`, no `Lift⊣T`. | cat-thinking (nota de vigilancia: evitar error categorial) |

## 4. Arquitectura — qué realiza el funtor

### 4.1 La matriz `openclaw` (la columna nueva de `ley/3 §4`)

Propuesta, heredada de la runtime-extension de la bestia (`~/kora/runtime/openclaw-runtime-extension.md`, verificada por exploración) y sujeta a la regla de veracidad de `ley/3 §4` (las razones de pérdida deben ser veraces respecto del runtime real; su literal vive en `kora.py`, no en la ley):

| Eje | Proyecciones | Nota |
|---|---|---|
| `pi` | 0→0, 1→1, 2→2, 3→3 **full** | soporta recursión/fixed-points |
| `mu` | 0→0, 1→1, 2→2, 3→3 **full** | **único target con materia ambiental always-on** |
| `xi` | 0→0, 1→1, 2→2, 3→3, 4→4 **full** | **único que no aplana la operad dinámica** (federación) |
| `lambda` | 0→0, 1→1, 2→2 full · 3→3 **partial** — society-in-the-loop requiere gobernanza externa no modelada en el runtime | el techo más alto; los 3 vivos abortan `lambda=3` |
| `phi` | 0→0, 1→1, 2→2 full · 3→3 **partial** — cognición híbrida: HOTL presente, no HAJCS completo · 4→∅ **none** — co-evolutivo no soportado | `phi=4` lo abortan todos los runtimes (`QUIEN_SOPORTA` lo confirma) |
| `sigma` | máx soportado `[3,3,3,3,2]` | accountability=3 real (materia persistente cross-session); solo `sustainability` se recorta (no medida directamente) |

`openclaw` es, por construcción, el techo más alto del retículo: el único runtime que realiza `mu=3` y `xi=4` sin recorte. Esa es la capacidad concreta que la Pieza C desbloquea — hoy un agente `servicio`/`plataforma` con `mu=3` **no tiene ningún funtor** que lo emita; tras la Pieza C, `openclaw` lo emite.

### 4.2 La emisión: un archivo, `SOUL.md` sin frontmatter

`T-openclaw` emite `_emision/openclaw/agents/{nombre}/SOUL.md` =

```
{cuerpo del artefacto, verbatim — abre con su propio H1}

<!-- kora:sello … -->
```

- **Sin fence YAML.** El cuerpo no se envuelve en `---…---`. Requiere una rama nueva en `_componer()` que omita los fences cuando no hay frontmatter (hoy `_componer` siempre antepone `---`; con `fm=[]` emitiría `---\n---`, igual ruido).
- **El cuerpo entero va al slot de identidad.** Hermes lo inyecta verbatim como slot #1. La anatomía multi-slot de `openclaw` (`SOUL.md`/`AGENTS.md`/`TOOLS.md`/`MEMORY.md`/…) colapsa a un único `SOUL.md` bajo «pneuma-mínima»: el agente pneuma no porta método-de-proyecto separable, y la materia (`MEMORY.md`/`USER.md`) la auto-bootstrapea el runtime.
- **La base conceptual viaja en el sello inline**: `fuente:urn` (nombre), `vector-proyectado`, `contrato-conocimiento` (los URN del corpus). El sello es el manifiesto de base embebido, proof-carrying; no hace falta un segundo archivo físico.

### 4.3 El sello de `T-openclaw` (proof-carrying, observable)

El sello hereda el formato de `ley/3 §5` (líneas finales fijas intactas) y porta, en la zona variable (antes de las dos líneas fijas), elementos openclaw-específicos:

- **`perdidas:`** del vector (las habituales: `lambda`, `phi`, `sigma.sustainability` cuando la fuente excede el techo).
- **Dos pérdidas de forma** (precedente: codex `forma: agente->habilidad`), testeables como aserción de **ausencia**:
  - `tool-binding->deploy` — el enforcement allow/deny va a `openclaw.json` (deploy-side); el binding no se enforcea desde el `SOUL.md`.
  - `workspace-anatomy->soul-slot` — la anatomía multi-slot de openclaw colapsa a un archivo (no hay `AGENTS.md`/`TOOLS.md`/… hermanos).
- **La clausura `F` declarada** (`cierre-safety`, tipo): el tool-SET intencionado se declara para que `cierre-safety` (`ley/3 §6`) tenga referente; solo el binding se difiere. (Mecanismo exacto — reusar el patrón de `contrato-conocimiento` o una línea propia — a fijar en el plan.)
- **La calificación `mu=3` observable** (dov-dori, CRÍTICA-estrecha):
  ```
  realiza:  emision-mu3-conforme (techo always-on, sin truncamiento de min)
  difiere:  conducta-always-on (gateway/systemd) -> a desplegar
  ```
  Razón: GENESIS es inmutable (dirá «no realizado» para siempre); el proof-carrier debe reconciliar por sí mismo GENESIS↔`realizado`, sin tercerizar la calificación a una ley que no viaja con el artefacto.

### 4.4 El transporte de fibra (legislado una vez, en prosa)

`ley/3` gana una nota (en `§5` y/o `§6`, prosa operativa; el nombre categorial «transporte de fibra» como paréntesis, no como cuerpo de ley) que declara, **para todos los targets**:

> El sello documenta dos operaciones sobre el artefacto: la **proyección funtorial del vector** (las líneas de fidelidad y pérdidas) y el **transporte verbatim del cuerpo** —portador de `U_phen`, fibra no-coordenada (`ley/1 §2`)—. El transporte **no es funtorial**: el cuerpo no se min-proyecta ni se declara-pierde por eje, y **no se re-proyecta** para concordar con el vector. Un consumidor que lee un cuerpo no debe asumir que concuerda automáticamente con el vector proyectado.

El **riesgo de desincronización cuerpo↔vector** (cat-thinking: un cuerpo verbatim puede afirmar capacidad que el vector ya no declara tras `min`) se **nombra** como puntero a la confesión FS-no-mecanizada de `ley/4` — **no** se mecaniza con un check nuevo (eso contradiría `ley/4`, que declara la fidelidad semántica obligación del productor, no del núcleo).

`T̃` es emisión hacia adelante; **no realiza `Lift⊣T`** (`ley/3 §8`, la adjunción inversa sigue abierta).

## 5. Qué pierde de forma declarada

| Pérdida | Tipo | Dónde se declara | Verificable |
|---|---|---|---|
| `lambda=3 → partial` | proyección de base | `perdidas:` del sello | byte (cuando la fuente la excede) |
| `phi=3 → partial`, `phi=4 → none` (aborta) | proyección de base | `perdidas:` / abort honesto | byte |
| `sigma.sustainability → 2` | proyección de base | `perdidas:` del sello | byte |
| `tool-binding → deploy` (token) | forma | pérdida de forma | aserción de ausencia (allowlist no enforced desde `SOUL.md`) |
| `workspace-anatomy → soul-slot` | forma | pérdida de forma | aserción de ausencia (archivo único) |
| transporte de `U_phen` no-funtorial | tercera capa | nota de `ley/3` (universal), **no** campo de sello | conceptual; el byte-determinismo verifica la mecánica, no el carácter |
| conducta always-on (`mu=3`) | semántica/token | `realiza:`/`difiere:` del sello + `ley/3` | declarada, diferida a deploy; no fingida |

## 6. Anclaje de la deuda saldada (GENESIS inmutable)

`GENESIS.md` **no se edita** (acta histórica; seguirá diciendo «openclaw … reconocido, no realizado»). La deuda se salda en `ley/3 v1.3.0`, que **registra** la realización y referencia `GENESIS §4` como saldada-parcialmente:

- `§2`: mover `openclaw` de «reconocido, no realizado» a «realizado»; añadir `T-openclaw-pneuma-v1` a los funtores vigentes.
- `§4`: añadir la sub-sección de la matriz `openclaw` (§4.1 de este spec).
- `§5`: la nota del transporte de fibra; el formato del sello openclaw (`realiza`/`difiere`, las pérdidas de forma, `F`).
- `§6`: la nota de que `U_phen` (fibra no-coordenada) no cae en ninguno de los dos regímenes — es transporte, no garantía sobre la proyección.
- `§7`: la fila de emisión `openclaw` (un `SOUL.md` sin frontmatter; sin `--aplicar`).
- `§10`: actualizar la tabla de validación.

**Lo que la Pieza C NO salda** (deudas que siguen abiertas, declaradas para no fingirlas): `hermes` (reconocido, no realizado); `Lift⊣T` (`ley/3 §8`); la convergencia teleológica y el `α-iso` (residentes-de-KB, `cat-agent-modulo`); el puente retículo↔coálgebra (`ley/1 §5`).

## 7. Mapeo a las leyes (qué estrato se toca)

| Estrato | ¿Se toca? | Notas |
|---|---|---|
| `ley/0` constitución | **No** | registrar un check tocaría §11; no se añade check |
| `ley/1` ontología | **No** | freeze heredado; la fibración base/fibra ya está implícita en `§2 v1.1.0` (U_phen no-coordenada) |
| `ley/2` forma | **No** | el `SOUL.md` no cambia la topología de los agentes-fuente (siguen siendo un `.md`); la opción γ (fibra autorada) que sí tocaría `ley/2` se difiere |
| `ley/3` transmutación | **Sí — único cambio de ley** | `v1.3.0`: §2/§4/§5/§6/§7/§10. Objeto + funtor + columna + transporte de fibra + calificación `mu=3` |
| `ley/4` koraficación | **No** | el riesgo de desync apunta a su confesión FS-no-mecanizada; no la modifica |
| `GENESIS.md` | **No** | inmutable; la realización se registra en `ley/3`, que lo referencia |

## 8. La frontera funtor / deploy

| Capa | Qué es | ¿La realiza el funtor? | ¿Se testea en `kora.py`? |
|---|---|---|---|
| **Funtor** | parse pneuma → `proyectar(vector, openclaw)` → `emitir()` `SOUL.md` byte-determinista + sello | **Sí** | **Sí, byte-a-byte** |
| **Transporte** | `art.cuerpo` (`U_phen`) verbatim al `SOUL.md` | copia, no funtor | sí (queda en los bytes) |
| **Deploy** | systemd + gateway `:18790`, bind-mount KORA read-only, Hermes cargando `~/.hermes/SOUL.md` slot #1, `openclaw.json` concediendo tools/model/secretos, la materia `mu=3` acumulándose en runtime | **No** — infra de `~/openclaw-fleet` + `~/.openclaw` | **No, y no debe** |

`mu:3→3 full` afirma que el **techo** del runtime admite materia always-on, así que el funtor proyecta sin degradar — exactamente como `claude-code xi:3→2 partial` afirma una propiedad del techo `claude-code` sin correr `claude-code`. No afirma que un daemon esté vivo recordando: eso es token de runtime.

**Honestidad a declarar:** `openclaw` queda «realizado-pero-no-ejercitado-en-deploy». La Pieza C no se vende como «agentes pneuma corriendo en Telegram»: es «el funtor `openclaw` emite artefactos tipo-conformes, testeados; conectarlos al fleet es deploy, no hecho aquí».

## 9. Riesgos, incertidumbres, deuda declarada

- **Contrato de borde no ejercitado end-to-end**: si el fleet nunca depliega un `SOUL.md` de pneuma, el formato exacto que Hermes carga no se sanity-checkea contra el runtime. Mitigación: validación **manual, una vez, fuera del test suite** (emitir → soltar en un `HERMES_HOME` de prueba → el gateway lo carga → responde). **Nunca** cablear un smoke-test de gateway en el núcleo stdlib-puro.
- **Matriz a confirmar contra el runtime real**: los valores de §4.1 se heredan de la bestia; las razones de pérdida deben ser veraces respecto del `openclaw` real (`ley/3 §4`). El plan las verifica antes de hornearlas en `kora.py`.
- **Desync cuerpo↔vector**: deuda general preexistente (no openclaw-específica) que `openclaw` revela; se nombra (puntero a `ley/4`), no se mecaniza.
- **La declaración de `F`/`cierre-safety` en el sello**: el mecanismo exacto (línea propia vs extender `contrato-conocimiento`) se fija en el plan; el principio (declarar `F`, diferir binding) es la decisión de diseño.

## 10. Criterios de cierre

- `ley/3 v1.3.0` redactada: `openclaw` realizado en §2, matriz §4, transporte de fibra y sello en §5/§6, emisión en §7, validación §10. Verificada: `python3 kora.py ley` la emite coherente.
- `kora.py`: `+1 columna MATRICES` (con `mu:3→3 full`, `xi:4→4 full`), `+1 rama emitir()` (openclaw → `SOUL.md`), `+1 rama _componer()` (sin-frontmatter), `TARGETS_REALIZADOS 3→4`, `QUIEN_SOPORTA[("mu",3)]` editado (openclaw ya realizado), `SIGMA_RAZONES["openclaw"]`. **Sin** `RUTAS_APLICAR`, **sin** `ley/1`, **sin** `ley/2`, **sin** tocar `GENESIS.md`.
- Tests (byte-deterministas, sin gateway):
  - `test_target_no_realizado_falla_honesto` (`test_kora.py:515`): pasa de iterar `("openclaw","hermes")` a solo `("hermes",)`.
  - `test_mu3_a_claude_code_falla` (`:493`): se mantiene (claude-code sigue abortando `mu=3`).
  - Nuevos: `openclaw` emite `SOUL.md` con `mu:3→3 full` sin pérdida en `mu`; **sin frontmatter** (`not soul.startswith("---")`, `soul.rstrip().endswith("-->")`); archivo único (sin hermanos); byte-determinista (doble emisión idéntica); las pérdidas de forma y la calificación `realiza`/`difiere` presentes en el sello; `xi=4→4 full`.
- Gate de mantenimiento: `python3 kora.py velar --estricto` (13/13) + `python3 -m unittest discover -s tests` (82 + nuevos) verdes.
- Validación de contrato de borde: registrada como manual-una-vez, fuera del suite.

## 11. Procedencia

Panel `consenso-deliberativo`, modo orquestación, 1 ronda de propuestas independientes + 1 ciclo de refutación adversarial. **Consenso 3/3** sin disenso irreductible. Aportes clave: la fibración de Grothendieck y el nombramiento del transporte como componente fibrada de `T̃` sobre `T` (cat-thinking); el corte objeto/proceso y la observabilidad de la calificación `mu=3` en el sello (dov-dori); la corrección del frontmatter roto, el reencuadre `workspace-anatomy→soul-slot`, el `--aplicar`-NO por never-overwrite y la frontera funtor/deploy (steipete). Cada afirmación load-bearing verificada contra estado real (`kora.py`, `~/openclaw-fleet`, doc Hermes, `~/kora` legacy), no contra reportes. Confianza declarada sin promediar: dov-dori alta, cat-thinking alta, steipete envío-aprobado con la corrección del frontmatter como gate dura.
