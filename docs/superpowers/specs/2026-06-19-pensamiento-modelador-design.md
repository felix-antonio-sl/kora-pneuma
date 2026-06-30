# Spec de diseño — skill `pensamiento-modelador` + kb `tensiones-modelamiento`

> Fecha: 2026-06-19 · Frente: KORA pneuma (`~/kora-pneuma`) · Estado: aprobado por el operador, pendiente de plan de implementación.
> Naturaleza: derivado auxiliar de proceso (no es artefacto KORA; sin URN; `ley/0 §5`). No tiene voz normativa.

## 1. Propósito

Elaborar una **skill de pensamiento modelador** que dote a cualquier agente u operador de la
capacidad de leer un acto de modelado como **navegación explícita de tensiones**, anclada al marco
de las 52 tensiones del documento fuente del operador (`/home/felix/_TEMP_BORRAR/tensiones_modelamiento.md`,
"Tensiones del Modelamiento de Sistemas" v2.2, 2025-12-13).

## 2. Decisiones HITL (registro de las preguntas de alta altura)

| # | Decisión | Resultado |
|---|----------|-----------|
| 1 | **Función-semilla** de la skill | **Lente meta-cognitiva horizontal**: dota de la capacidad de *leer* un acto de modelado como navegación de tensiones (nombrar tensión, ver polos, declarar criterio, elegir). No conduce ni ejecuta mecánica. Análoga a `cat-thinking`. |
| 2 | **SSOT del marco de 52 tensiones** | **kb único, referenciado por URN** (patrón `cat-thinking` → corpus ICAS). El marco es conocimiento; la skill aporta el método. |
| 3 | **Blast radius respecto a `dov-dori`** (que hoy duplica el marco acoplado a OPM) | **Reconciliar dov-dori en el mismo trabajo**: su capa A se adelgaza a referenciar el kb y conservar solo sus resoluciones OPM. |
| 4 | **Namespace del kb** (nombre verdadero, perenne) | **fxsl** (`urn:fxsl:kb:tensiones-modelamiento`): el namespace del kb sigue el **dominio** del conocimiento (modelado conceptual, vecino de `dov-dori` y el corpus OPM en `fxsl`), no la horizontalidad. La skill queda en `kora`. Precedente: `cat-thinking` (kora) → corpus `icas-*` (fxsl). `kora` se reserva a meta-conocimiento de KORA. |

Confirmaciones finales del operador: **skill** en namespace `kora`, **kb** en namespace `fxsl`
(decisión 4); vector de la skill idéntico a `cat-thinking` `[2,0,1,0,1]`; bump de `dov-dori` como
**minor** (1.5.0).

## 3. Principio rector

Realiza la distinción constitucional `ley/0 §3`: **conocimiento se lee, skills se proyectan**. El
marco (qué tensiones existen, sus polos y preguntas) es *conocimiento*; la capacidad de navegarlo
(nombrar, situar, elegir, declarar) es la *skill*. La SSOT son los URN, jamás el cuerpo. Telos KORA:
*una sola fuente de verdad por objeto; abolir la duplicación ontológica* — de ahí la reconciliación
de `dov-dori`.

## 4. Arquitectura — 3 piezas

### Pieza 1 · kb `urn:fxsl:kb:tensiones-modelamiento`

Conocimiento puro y **formalismo-agnóstico**. Sin `vector`/`sigma` (solo los agénticos ocupan PMI×LFS).

Frontmatter (shape de conocimiento, molde `icas-composicion`):

```yaml
urn: urn:fxsl:kb:tensiones-modelamiento
nombre: tensiones-modelamiento
version: 1.0.0
estado: publicado            # nace borrador → publicado
descripcion: "..."           # el marco de 52 tensiones del modelado, las 3 capas anidadas
fuente: "Koraficado del documento del operador 'Tensiones del Modelamiento de Sistemas' v2.2 (2025-12-13); sin sha256 (fuente humana externa, no la bestia)."
autor: FS
creado: 2026-06-19
lang: es
tags: [tensiones-modelamiento, modelado-conceptual, praxis-de-modelado, ...]  # ≥3 bajo --estricto
familia: bok                 # a confirmar contra ley/2 (no obligatorio)
```

Contenido del cuerpo:

- Las **3 capas anidadas**: A sustantivas (qué decidir) ⊂ B praxis (cómo decide el modelador) ⊂
  C contexto (condiciones que modulan).
- Las **12 categorías** y las **52 tensiones** con polo A / polo B / pregunta, en español pleno.
- Una **clave de lectura** general (no-OPM): *un formalismo es un sistema de resoluciones
  congeladas de las tensiones **sustantivas**; las de **praxis** y **contexto** no las resuelve
  ningún formalismo — las navega el modelador, nombrándolas.*

**No incluye**: ninguna resolución OPM (valor propio de `dov-dori`).

### Pieza 2 · skill `urn:kora:artefacto:pensamiento-modelador`

Molde = `cat-thinking`. Frontmatter:

```yaml
urn: urn:kora:artefacto:pensamiento-modelador
nombre: pensamiento-modelador
version: 1.0.0
estado: activo               # nace borrador → activo
descripcion: "Skill de pensamiento modelador: lente horizontal que lee cualquier acto de modelado como navegación explícita de las 52 tensiones (sustantivas/praxis/contexto), nombrando la tensión, sus polos y el criterio antes de elegir. Anclada al kb tensiones-modelamiento."
autor: FS
creado: 2026-06-19
lang: es
tags: [pensamiento-modelador, tensiones-modelamiento, modelado-conceptual, praxis-de-modelado, ...]
vector: [2, 0, 1, 0, 1]      # idéntico a cat-thinking: Π2 plan ramificado, Μ0 sin estado, Ξ1 atómica, Λ0 individual, Φ1 instrumental
sigma: [1, 1, 3, 1, 0]       # transparency=3: nombra tensión, declara criterio, cita URN
arnes: disciplina
forma: habilidad
herramientas: [Read, Grep, Glob]
targets: [claude-code, codex, opencode]
estados: [triaje, ubicar-capa, nombrar-tension, situar-resolucion, declarar-criterio-elegir, entregar]
conocimiento: [urn:fxsl:kb:tensiones-modelamiento]
componible: [urn:kora:artefacto:cat-thinking]
```

Workflow (estados):

1. `triaje` — ¿hay un acto de modelado con decisión(es) en juego? ¿admite lectura por tensiones?
   Si no → declinar y declarar.
2. `ubicar-capa` — ¿la decisión es sustantiva (A), de praxis (B) o de contexto (C)?
3. `nombrar-tension` — identificar la(s) tensión(es): polos + pregunta, citando el kb por URN.
4. `situar-resolucion` — si es sustantiva: ¿el formalismo del operador ya la resuelve (resolución
   congelada)? si es praxis/contexto: ningún formalismo la decide, la navega el modelador.
5. `declarar-criterio-elegir` — explicitar el criterio y elegir/recomendar polo con su por-qué.
   Nunca por inercia.
6. `entregar` — diagnóstico estructurado: tensión(es) nombradas, polos, criterio, elección/
   recomendación, qué queda como supuesto/deuda. Trazable al kb.

Reglas duras (núcleo):

1. **Nombrar la tensión antes de resolverla** (polos + pregunta + criterio). Elegir por inercia es
   negligencia de praxis (regla #8 de Dori, ahora horizontal).
2. **Citar la URN del kb** que define cada tensión. No de memoria.
3. **Distinguir las 3 capas**: las sustantivas las resuelve el formalismo; praxis y contexto las
   navega el modelador. No confundir capas.
4. **No resolver praxis/contexto** como si un formalismo las decidiera.
5. **No invadir** la mecánica del formalismo ni el dominio: la skill nombra y razona la tensión;
   el formalismo (OPM/ER/IFML) o el agente de dominio aporta la resolución concreta.
6. **Elegir la lectura más débil** que cumpla el trabajo: no desplegar 52 tensiones cuando la
   decisión toca 2.
7. **Abortar si no aplica** (decisión arbitraria sin estructura): declarar y delegar.
8. **Consultar el kb en tiempo de skill** (Read/Grep). No responder de memoria.

Recursos (`referencias/`, mapas operativos, no SSOT):

- `referencias/disparadores.md` — tabla "síntoma de decisión trabada → capa/tensión a consultar".
- `referencias/checklist-navegacion.md` — checks de que la navegación está completa (capa ubicada,
  tensión nombrada, criterio declarado, elección con por-qué).

### Pieza 3 · reconciliación de `dov-dori` (1.4.0 → 1.5.0)

- Su capa A pierde las columnas tensión/polos/pregunta (ahora en el kb) y **conserva solo** la tabla
  *"tensión sustantiva → Resolución OPM / lectura de Dori"* — su valor propio.
- Capas B y C (agnósticas) pasan a **citar el kb**; Dori conserva solo su lectura OPM-específica
  (p. ej. "top-down porque OPM es función-primero").
- `conocimiento:` += `urn:fxsl:kb:tensiones-modelamiento`.
- `componible:` += `urn:kora:artefacto:pensamiento-modelador`.
- **Bump minor**: la posición ontológica (vector, arnés, forma) y la capacidad observable de Dori
  no cambian — sigue navegando tensiones, ahora componiendo en vez de duplicar. Refactor aditivo de
  cuerpo → minor (`ley/0 §12`; major se reserva a enums/rangos/checks/sello).
- Registrar la reconciliación en el campo `fuente:` de dov-dori (procedencia honesta del cambio).

## 5. Plan de implementación (orden)

1. **kb primero** (`tensiones-modelamiento`): koraficar el doc fuente a conocimiento de alta
   fidelidad (skill `koraficacion-knowledge`: FS/CR, dedup, ortografía plena). Material crudo
   permanece fuera del repo.
2. **skill** (`pensamiento-modelador`): construir con shape de autoría vigente (skill `kora-skills`),
   referenciando el kb ya existente para que `referencias-resuelven` pase.
3. **dov-dori**: editar el cuerpo (adelgazar capa A, citar kb en B/C), añadir `conocimiento`/
   `componible`, bump 1.5.0, actualizar `fuente:`.
4. **Gates**: `python3 kora.py velar --estricto` 13/13 + `python3 -m unittest discover -s tests` +
   censo **144 → 146**. Verificar `referencias-resuelven` con las nuevas URN.
5. **Verificación de proceso** (doctrina pneuma): `git status --short` + `git diff --stat` + medir
   censo — confirmar alcance exacto (2 altas + 1 modificación), sin cambios fuera de mandato.

## 6. Consumidores de la skill — estado verificado

**Corrección (2026-06-19):** una versión previa de este spec declaraba como deuda "cablear
`ifml-architect` y `database-designer` para que compongan la skill". Verificación contra el censo:
**ninguno de los dos es artefacto KORA en pneuma** — `ifml-architect` vive solo en la bestia
(`~/kora`, congelada) y como emisión en `~/.claude`; `database-designer` ni siquiera se promovió allá
(está en `_TALLER/INBOX`, pre-categorial). No hay consumidores pneuma que cablear. La skill nace **sin
composición entrante declarada**. Si en el futuro se migra a pneuma alguna capacidad de modelado,
podrá componer la skill en su propio acto de autoría — no es deuda de esta iteración.

## 7. Riesgos y notas

- **Vector idéntico a cat-thinking**: por `ley/1 §2`, ambas skills son categóricamente equivalentes
  *como tipo de capacidad*; se distinguen por cuerpo/dominio, no por posición. Honesto, no defecto.
- **`familia` del kb**: `bok` tentativo; confirmar contra `ley/2` (campo no obligatorio).
- **Fidelidad del kb**: el cuerpo debe preservar las 52 tensiones sin pérdida; la reescritura es
  ortográfica/estructural, no semántica. La prueba ácida de koraficación aplica.
- **dov-dori sublimado byte-fiel**: el adelgazamiento diverge del cuerpo de la bestia; legítimo
  (pneuma es fuente única de doctrina futura), se declara en `fuente:`.
