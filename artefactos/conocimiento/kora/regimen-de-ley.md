---
urn: urn:kora:kb:regimen-de-ley
nombre: regimen-de-ley
version: 1.2.2
estado: publicado
descripcion: "Régimen de ley de KORA: pneuma (ley/0..4) es la fuente única de doctrina futura; la ley de la encarnación bestia queda congelada salvo correcciones de verdad; OpenClaw ya es realizado por pneuma y Hermes permanece como competencia legacy pendiente."
fuente: "Decisión HITL del operador (FS) el 2026-06-14, en sesión de evaluación bestia↔pneuma. Deriva de dos dictámenes producidos en la sesión: polymath (cuantificación del cruce, veredicto ALT-B) y steipete (filo de ejecución: el debt real es el cisma de ley, no la cola de deudas técnicas). v1.1.0 (2026-06-15): formaliza la doctrina de acceso al corpus de la bestia (origen de migración por demanda, no destino de resolución; migrar-o-omitir) aplicada en la sesión y mecanizada en el contrato de conocimiento de emitir(). v1.2.0 (2026-07-12): registra el cierre ya legislado de OpenClaw en ley/3 v1.3.0; Hermes queda como única competencia delegada legacy. v1.2.1 (2026-07-13): retira el recuento persistido del corpus legacy; su tamaño se consulta en origen solo cuando una decisión lo requiere. v1.2.2 (2026-08-14): actualiza el rationale a la formulación vigente de ALMA: una fuente por objeto y ninguna copia autoritativa, sin borrar las distinciones ontológicas entre tipos. Decisión interna al ecosistema, sin hash externo."
autor: FS
creado: 2026-06-14
lang: es
tags: [regimen-de-ley, freeze, doctrina, pneuma, bestia, forcing-function]
cita: [urn:kora:kb:alma-de-kora]
familia: nota
---

# Régimen de ley de KORA — fuente única de doctrina futura

Declaración de gobernanza meta sobre la relación entre las dos encarnaciones de
KORA: la bestia (`~/kora`) y pneuma (`~/kora-pneuma`). Cierra el cisma de ley —
dos cuerpos de doctrina editables que divergen sin que ningún check lo detecte —
fijando una sola fuente de doctrina y congelando la otra.

## Decisión

| # | Declaración |
|---|---|
| 1 | **pneuma es la fuente única de doctrina futura de KORA.** |
| 2 | **La ley de la encarnación bestia queda congelada.** |
| 3 | **OpenClaw ya es realizado por pneuma; Hermes permanece como competencia delegada legacy**, con fecha de revisión. |
| 4 | **El corpus de la bestia es origen de migración por demanda, nunca destino de resolución**: migrar-o-omitir, jamás enlazar. |

## 1. Fuente única de doctrina futura

1. Toda evolución doctrinal de KORA se autora en `ley/0..4` de pneuma: enums,
   rangos de ejes, matrices de transmutación, cadenas de lifecycle, registro de
   checks, shape de autoría, contrato de koraficación.
2. Ningún cambio doctrinal nace ya en la bestia. La bestia no recibe specs
   nuevas ni enmiendas de doctrina.
3. El cambio de la ley de pneuma se rige por su propia constitución
   (`ley/0` §12): semver por estrato, freeze heredado de `ley/1-ontologia`,
   HITL obligatorio para todo cambio major.

## 2. Freeze de la encarnación bestia

1. La ley de la bestia (`governance/`, `ontology/`, `serialization/`,
   `runtime/`) queda **congelada** al 2026-06-14.
2. Solo se admiten **correcciones de verdad necesarias**: errores factuales,
   typos que cambian sentido, rupturas de coherencia con la realidad. NO se
   admite evolución doctrinal, specs nuevas ni expansión conceptual.
3. Es el espejo del freeze que el propio `ALMA.md` venera (§V, freeze ⇄
   evolución): un núcleo quieto para que la periferia gire. Aquí el núcleo
   quieto es la encarnación entera.
4. La bestia conserva su corpus y su realización de runtimes; sigue siendo
   autoritativa para todo lo no migrado. Congelar la ley no jubila
   el cuerpo: lo fija como referencia estable.
5. El corpus de la bestia es **origen de migración por demanda, nunca destino
   de resolución en runtime**. Un artefacto de pneuma no referencia la bestia
   (ni por path ni por URN no catalogado): el conocimiento se **migra** a pneuma
   (byte-fiel o adaptado, URN preservado, `sha256` en `fuente:`) y se cataloga
   localmente, o se **omite con razón declarada** (la sustancia vive en el
   cuerpo mientras tanto). Migrar-o-omitir, jamás enlazar.
6. Esto no duplica: la bestia congelada es respaldo inmutable, no segunda
   fuente viva. El contrato de conocimiento del sello (función pura del URN,
   blindada por `lugar-coincide`) deriva siempre contra el catálogo central de
   pneuma, nunca contra la estructura de la bestia.

## 3. OpenClaw realizado; Hermes delegado legacy

1. pneuma realiza `openclaw` desde ley/3 v1.3.0 mediante una proyección leve:
   workspace `AGENTS.md` + `SOUL.md`, sin absorber configuración, memoria ni
   scaffolding del runtime. La fuente doctrinal y la emisión ya viven aquí.
2. `hermes` sigue reconocido pero no realizado; transmutar falla honestamente
   y remite a GENESIS mientras esta deuda permanezca.
3. **No-limbo**: en la fecha de revisión se decide si Hermes se encarna en
   forma leve o se declara competencia permanentemente archivada de la bestia.

## 4. Disparadores (forcing functions)

Para que "migración por demanda" no decaiga en estancamiento, el régimen porta
sus disparadores:

1. **Nacimiento**: todo artefacto agéntico nuevo nace en pneuma. Si exige Μ=3,
   se proyecta a `openclaw`; la falta de Hermes no es razón para nacer en la
   bestia.
2. **Flota**: todo agente de flota que se toque se realiza desde pneuma. No se
   realiza nada nuevo desde la bestia por inercia.

## 5. Rationale

El ALMA de KORA exige **una sola fuente de verdad por objeto** y que ninguna
fuente tenga copias autoritativas. Dos leyes editables violan ese principio:
no hay transformación natural entre las dos realizaciones, sus dominios de
salida divergen en `openclaw`/`hermes`, y toda enmienda doctrinal aterrizaría
en una sola encarnación dejando la otra desincronizada en silencio. KORA, por
su alma, no puede tener dos almas. Este régimen restaura el principio: **una
fuente de verdad, proyecciones derivadas.**

## 6. Revisión

- Fecha de revisión del destino de `hermes` (§3): **2026-09-14**.
- El régimen se revisa si cambia el supuesto de coexistencia (p. ej. la flota
  migra de runtime, o pneuma encarna `openclaw` leve).
