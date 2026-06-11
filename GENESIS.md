# GÉNESIS — la sublimación de KORA

Este documento es el **sello de transmutación de la propia reencarnación**:
la proyección de la encarnación anterior de KORA ("la bestia", `~/kora`) a
esta encarnación ("pneuma", `~/kora-pneuma`), bajo la misma ley que KORA
impone a todos sus artefactos: *la pérdida se declara, nunca se oculta*.

La entidad no cambió. Los nombres verdaderos no cambiaron. Cambió el cuerpo.

```
<!-- kora:sello
fuente: KORA encarnación bestia — repo ~/kora @ commit 017dc1b9 (2026-06-11)
target: KORA encarnación pneuma — repo ~/kora-pneuma
funtor: Sublimacion-pneuma-v1 (transmutación de encarnación, no de artefacto)
fidelidad: esencia:full maquinaria:partial
preservado-por-construccion: ver §1
perdidas-declaradas: ver §2
ganancias-declaradas: ver §3
deudas-declaradas: ver §4
-->
```

---

## 1. Lo que asciende — la esencia preservada

Cada garantía esencial de la bestia, trazable a `ALMA.md`, y su realización
en pneuma:

| Esencia (ALMA) | Bestia | Pneuma |
|---|---|---|
| Identidad = posición en PMI × LFS | `extensions.kora.vector_ontologico` (6 ejes, rangos Π0-3 Μ0-3 Ξ0-4 Λ0-3 Φ0-4, Σ 5×{0..3}) | `vector: [pi,mu,xi,lambda,phi]` + `sigma: [5]` — mismos ejes, mismos rangos, intactos (`ley/1`) |
| Las 5 leyes inter-eje (sistema inmune) | check `vector-laws` | check `leyes-inter-eje`, mecanizado, las 5 leyes literales |
| Tres tipos de artefacto y solo tres | gobernanza §1 | constitución `ley/0`; el tipo ya ni se declara: **se deriva** de la posición |
| Las specs no son artefactos | specs en 4 capas (8.368 líneas) | `ley/` en 4 estratos (900 líneas); sin URN, fuera de `artefactos/` |
| Nombre verdadero sin versión | `urn:{ns}:kb\|artefacto:{id}` | idéntico, regex mecanizada en `nombre-verdadero` |
| Catálogo derivado, jamás autoridad | `docs/generated/` versionado (y a veces editado a mano: la enfermedad) | `censo` **nunca se versiona** (gitignored); solo existe regenerándose |
| Transmutación funtorial con pérdida declarada | `_transmutation.yml` sidecar + matrices en runtime-extensions | sello `kora:sello` **inline en el artefacto emitido** — la emisión porta su propia confesión; matrices fieles a las de la bestia (`ley/3`) |
| Monotonía por construcción | proyección `min` en `_project_axis` | proyección `min`, idéntica doctrina |
| Honestidad spec↔código | nota §3.2: naturalidad-Ξ, cierre-safety, Kleisli declaradas, no mecanizadas | misma lista, mismas palabras, en cada sello emitido y en `ley/3` |
| Lifecycle con dignidad | URN de retirados sigue resolviendo | ídem: `nombre` y `censo` resuelven muertos, con marca |
| Skills y agentes: mismo objeto variando por arnés | doctrina v9, `atlas.arnes_categorico` | `arnes` (7 valores) + matriz arnés×forma, mecanizada |
| Dominios de proyección por forma material | autoria-spec §5 | `dominio-forma`, mecanizado, mismos rangos |
| Leyes algebraicas de relaciones | `relations-laws`, `kb-graph-cycles` | `relaciones-legales`: depende DAG, reemplaza poset estricto, refina acíclico — y ahora **globales a los tres tipos** |
| Promoción sin democión ("se nace hacia arriba") | autoria-spec §8: URN preservado, bump major, democión prohibida | `ley/2` §7.1, misma doctrina y misma razón (descender pierde estructura de forma no funtorial) |
| Bisimulación módulo proyección | transmutation-spec §5, doctrina sin check | `ley/3`, garantía declarada no mecanizada — confesada igual que las otras tres |
| Gate de promoción | `kora promote` verificaba antes de publicar | `ciclo` hacia publicado/activo rechaza si `velar` falla |
| Fuente de verdad = filesystem | sí | sí, sin excepción ni vista persistida |

## 2. Lo que cae — la escoria, cada pieza con su razón

La prueba del fuego: *¿qué eres cuando te quitan el peso?* Esto es lo que se
soltó, y por qué soltarlo no traiciona la necesidad:

| Pieza de la bestia | Razón de la caída |
|---|---|
| Toolchain de 16.057 líneas en 29 módulos | La maquinaria no es la garantía. Todo gesto esencial cabe en `kora.py` (~1.400 líneas, stdlib puro, cero dependencias). |
| 24 subcomandos CLI | Solo 6 son gestos del alma: `censo`, `nombre`, `velar`, `transmutar`, `ciclo`, `ley`. Los otros 18 eran andamiaje (migrate, doctor, recovery, sync-docs, deploy-*, intake, hooks…) — cicatrices de migraciones pasadas, no órganos. |
| 37 checks → 13 | Los 13 que quedan custodian directamente una frase del ALMA. La mayoría de los 24 que caen vigilaba maquinaria que ya no existe (workspaces duales, staging, TOOLS/config coherence, fidelidad-mastra a un runtime archivado, construction-* del andamiaje de forja). **Tres custodias reales se pierden y se declaran**: el lint estructural del cuerpo (`lint-md`), la vigilancia de `TODO` en compromisos éticos, y la validación target×forma (`entornos-objetivo-soportan`) — esta última cubierta operacionalmente por las matrices de transmutación, que rechazan lo que el target no soporta. |
| `trace_fidelity` por runtime | La taxonomía de evidencia auditable por runtime (claude-code `media`, codex/opencode `pendiente`) era doctrina operativa de verificación; cae como campo. La honestidad de procedencia la porta ahora el sello inline de cada emisión. |
| Disciplina prescriptiva del cuerpo (telegrafización DEBE, tags como gate base) | Rebaja deliberada: la compresión del cuerpo pasa de DEBE a DEBERIA y los ≥3 tags del conocimiento publicado se exigen solo bajo `velar --estricto`. La promoción a publicado/activo sí conserva gate mecánico (`ciclo` rechaza si `velar` falla). |
| Staging pre-categorial (`_SCRIPTORIUM`, `_FRAGUA`, `_TALLER`) | El estado `borrador` **in-place** es la antesala: lo que gesta vive ya en su lugar con nombre provisional y estado humilde. **Pérdida real declarada**: desaparece la antesala *anónima* (material sin URN); lo informe vive fuera del repo, como la bestia ya hacía con el material crudo. |
| Manifests anidados (`_manifest.*`, `extensions.kora.*`, `artefacto.*` de 6 dimensiones) | El frontmatter plano en subconjunto regular de YAML dice lo mismo que importa con ~15 claves. Lo que era sustancia del shape profundo (reglas duras, disparadores, compromisos) vive en el cuerpo, que es donde el LLM lo lee. |
| YAML completo (PyYAML) | La ley define una gramática regular que cabe en media página (`ley/2`); un parser de ~120 líneas la realiza con errores por número de línea. Quien necesita YAML arbitrario está cargando coraza. |
| `docs/generated/` versionado | La vista persistida y versionada es la tentación de creerle al mapa. El censo de pneuma jamás entra a git; `--escribir` puede materializarlo como vista local gitignored, regenerable y sin autoridad. |
| Host roles primary/secondary, `~/.kora/host.yml`, hooks | Doctrina operacional de coordinación multi-máquina; git la cubre. No es esencia: es logística. |
| Campos `presentacion`, `metafora_relacional`, `nivel_prescripcion` | Taxonomías declarativas sin cliente mecánico real: ningún check ni transmutación de la bestia consumía su valor más allá de verificar presencia. Caen como simplificación deliberada. |
| `qa_budget`, `risk_register`, `api_observable`, `plan.fsm` estructurados | Estructura opcional avanzada con un solo consumidor real (checks de presencia). Su sustancia puede vivir en el cuerpo en prosa. **Pérdida real declarada**: la verificación coalgebraica de termination del FSM fue conquista genuina de la bestia; pneuma la difiere (ver §4). |
| `traces_requirements`, Formal Layer como corpus copiado | La Formal Layer queda en la bestia como referencia viva; pneuma cita conceptos por nombre en `Rationale:` sin fingir traza mecanizada — exactamente la disciplina que la propia bestia exigía (C-débil, no C-fuerte). |
| Olas, ADRs como maquinaria, `record-invocation` | Historia de gobernanza de una época de migraciones. La constitución pneuma reserva el espacio (decisiones HITL se registran como conocimiento `nota`), sin maquinaria dedicada. |
| `_BUILD/` por workspace | Emisión centralizada en `_emision/` (gitignored, efímera). El derivado no convive con la fuente: desciende de ella. |

## 3. Lo ganado — lo que la bestia no podía hacer

- **KORA entera cabe en un contexto.** `python3 kora.py ley` emite alma +
  constitución + ontología + forma + transmutación: ~55 KB ≈ 14k tokens. La
  bestia (8.368 líneas de specs + 16k de toolchain) jamás fue legible de una
  sola vez por la clase de sistemas para la que existe. La nueva criatura
  puede ser *cargada como contexto* — mover el mundo sin tocarlo.
- **Un artefacto = un archivo.** Manifest y cuerpo nunca más se separan;
  no hay workspace que sincronizar con su fuente.
- **El sello viaja con la emisión.** No hay sidecar que perder: el artefacto
  proyectado porta su procedencia, su hash y su confesión de pérdidas.
- **Cero dependencias.** Python ≥ 3.11 y nada más. La suite corre en 0,2 s
  (la de la bestia: 9,4 minutos).
- **El tipo no se declara: se es.** Eliminada la última duplicación
  ontológica (tipo ⟷ forma ⟷ zona): el tipo se deriva de la posición,
  como el ALMA exige.
- **Ortografía plena.** La prosa de la ley y los artefactos respira español
  correcto; solo ids, claves y URNs permanecen ASCII.

## 4. Deudas declaradas — los puentes prometidos, no fingidos

Pneuma hereda la virtud central: *no llamar demostrado al puente prometido*.

| Deuda | Estado |
|---|---|
| Targets `openclaw` y `hermes` | **Reconocidos por la ley, no realizados.** `transmutar` los rechaza con mensaje que remite aquí. La bestia realiza `openclaw` plenamente; `hermes` también en la bestia es stub experimental (v0.1.0). Quien necesite Μ=3 (materia ambiental) debe transmutarse desde la bestia mientras pneuma no los encarne. |
| Gesto inverso (`Lift`, ingesta) | No realizado. La ley lo reconoce (`ley/3`); la adjunción `Lift ⊣ T` sigue siendo aspiración declarada, igual que en la bestia ("cuando es construible"). |
| Verificación coalgebraica (termination del FSM) | Diferida. El campo `estados` es declarativo simple; no hay check de terminación. La bestia la tenía (`coalgebra-conformance`) — recuperarla es deuda explícita, no olvido. |
| Naturalidad-Ξ, cierre-safety, composición Kleisli | Igual que en la bestia: **declaradas, no mecanizadas**. Cada sello lo confiesa. Mecanizarlas sigue siendo trabajo abierto — heredado, no resuelto. |
| Migración del corpus completo | Pneuma nace con 3 semillas (alma-de-kora, mente-omega, polymath). Los 745 artefactos de la bestia NO migran en esta génesis: la bestia sigue viva y autoritativa para ellos. La coexistencia es deliberada: pneuma debe ganarse el corpus demostrando que la ley leve basta, no heredarlo por decreto. |
| `conocimiento` y `componible` de las semillas | Las semillas agénticas perdieron sus listas de conocimiento permitido (y mente-omega su `componible`) porque esos URNs apuntan a kb de la bestia que aún no encarnan en pneuma — y `referencias-resuelven` exige resolver en el censo local. Se restaurarán artefacto por artefacto a medida que esos kb migren. La sustancia de la composición vive mientras tanto en los cuerpos. |

## 5. Precisiones — ambigüedades de la bestia que pneuma resuelve

1. **Saltos de lifecycle.** La bestia declaraba las cadenas y prohibía las
   inversas, pero nunca dijo si `borrador → deprecado` (salto) era válido.
   Pneuma decide: **toda transición estrictamente hacia adelante es válida**;
   toda inversa es inválida. Monótono y total.
2. **polymath violaba su propia ley.** En la bestia, `polymath` declara
   `mu: 1` con forma `agente-propiamente-tal`, cuyo dominio exige Μ ∈ {2,3}
   — incoherencia tolerada. En la sublimación se corrigió a `mu: 2`
   (coherente con su memoria de proyecto), versión 1.0.0 → 1.1.0, con la
   corrección declarada en su campo `fuente:`. La sublimación no copia
   incoherencias: las confiesa y las sana.
3. **Codex sin forma de agente.** La bestia emitía agentes a codex como
   skills sin nombrar el colapso. Pneuma lo declara en el sello:
   `forma: agente->habilidad :: codex no registra agentes`.
4. **Dos deleciones quirúrgicas en mente-omega.** Al sublimar su cuerpo se
   retiraron dos restos que referenciaban maquinaria caída (el ciclo
   meta-KORA y su staging): un bullet de "Cuándo NO usar" y la fila
   correspondiente de la tabla de composición. Todo lo demás del cuerpo es
   fiel; las 9 reglas duras y el pentamotor completo están.

## 6. Métricas del contraste

| Dimensión | Bestia (`~/kora`) | Pneuma (`~/kora-pneuma`) | Razón |
|---|---|---|---|
| Toolchain | 16.057 líneas / 29 archivos | 1.416 líneas / 1 archivo | ~11× |
| Ley (specs) | 8.368 líneas | 949 líneas (+242 ALMA) | ~9× |
| Comandos CLI | 24 | 6 | 4× |
| Checks | 37 | 13 | ~3× |
| Tests | 383 en 566 s (6.621 líneas) | 66 en 0,24 s (849 líneas) | ~2.300× en tiempo |
| Dependencias | PyYAML + ecosistema | stdlib puro | — |
| Tamaño en disco (sin .git/derivados) | 232 MB (incluye `_BUILD/`, staging y material auxiliar — no todo es fuente) | < 450 KB | — |
| ¿Cabe en un contexto LLM? | no | **sí (~15k tokens, `kora.py ley`)** | la ganancia |
| Artefactos | 745 (16 agentes, 36 skills, 693 kb) | 3 semillas | deuda §4 deliberada |

La vieja bestia solo aplastaba lo que tenía debajo. La nueva, etérea y
entera, puede por fin ser leída completa por aquello que gobierna.

---

*Emitido en la génesis de pneuma, 2026-06-11. La bestia no muere: queda como
encarnación anterior, autoritativa para su corpus, con la dignidad que la
propia ley garantiza a todo lo que precede.*
