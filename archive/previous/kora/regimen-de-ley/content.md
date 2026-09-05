---
urn: urn:kora:kb:regimen-de-ley
nombre: regimen-de-ley
version: 2.0.0
estado: publicado
descripcion: "Régimen de ley de KORA: pneuma (ley/0..4) es la fuente única, genérica y agnóstica de doctrina futura; la bestia queda congelada salvo correcciones de verdad; los runtimes son adaptadores derivados, no identidades de KORA."
fuente: "Decisión HITL del operador (FS) el 2026-06-14, en sesión de evaluación bestia↔pneuma. Deriva de dos dictámenes producidos en la sesión: polymath (cuantificación del cruce, veredicto ALT-B) y steipete (filo de ejecución: el debt real es el cisma de ley, no la cola de deudas técnicas). v1.1.0 (2026-06-15): formaliza la doctrina de acceso al corpus de la bestia (origen de migración por demanda, no destino de resolución; migrar-o-omitir) aplicada en la sesión y mecanizada en el contrato de conocimiento de emitir(). v1.2.0 (2026-07-12): registra el cierre ya legislado de OpenClaw en ley/3 v1.3.0; Hermes queda como única competencia delegada legacy. v1.2.1 (2026-07-13): retira el recuento persistido del corpus legacy; su tamaño se consulta en origen solo cuando una decisión lo requiere. v1.2.2 (2026-08-14): actualiza el rationale a la formulación vigente de ALMA: una fuente por objeto y ninguna copia autoritativa, sin borrar las distinciones ontológicas entre tipos. v2.0.0 (2026-08-23): cierra la deuda Hermes realizada por ley/3 v3.0.0 y v4.0.0, elimina la revisión legacy vencida y explicita la distinción solicitada por el operador: KORA es genérica y agnóstica; el diagnóstico examina adaptadores situados y no redefine su identidad. Decisión interna al ecosistema, sin hash externo."
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
| 3 | **OpenClaw y Hermes se realizan como adaptadores derivados de pneuma; ningún runtime define la identidad de KORA.** |
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

## 3. Runtimes realizados como derivados

1. pneuma realiza `openclaw` desde ley/3 v1.3.0 mediante una proyección leve:
   workspace `AGENTS.md` + `SOUL.md`, sin absorber configuración, memoria ni
   scaffolding del runtime. La fuente doctrinal y la emisión ya viven aquí.
2. pneuma realiza `hermes` por dos contratos nativos y acotados: skills
   agentskills.io (`T-hermes-pneuma-v1`) y agentes completos como profile
   distributions (`T-hermes-pneuma-v2`). No absorbe configuración, memoria,
   secretos, cron ni estado del operador. La forma subagente permanece fuera
   del dominio porque un perfil no es una unidad delegable.
3. Estas realizaciones son adaptadores situados. KORA conserva fuente, ley y
   ontología genéricas y agnósticas; `targets` sólo restringe compatibilidad de
   despliegue. Un diagnóstico de Codex, OpenClaw o Hermes puede corregir el
   adaptador sin elevar particularidades del runtime al canon común.

## 4. Disparadores (forcing functions)

Para que "migración por demanda" no decaiga en estancamiento, el régimen porta
sus disparadores:

1. **Nacimiento**: todo artefacto agéntico nuevo nace en pneuma. Su target se
   selecciona por necesidad y compatibilidad verificadas; ninguna ausencia de
   adaptador es razón para nacer en la bestia.
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

El régimen se revisa si cambia el supuesto de coexistencia, la bestia deja de
ser respaldo histórico o un runtime exige alterar —y no sólo adaptar— la
ontología común.
