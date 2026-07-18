# KORA/Koraficación — ley pneuma v1.2.0

Contrato de **producción** de artefactos de conocimiento: la transformación
gobernada de fuentes humanas o documentales en KORA/MD con fidelidad medible.
Esta ley convierte a pneuma en fábrica, no solo en repositorio, catálogo y
transmutador.

Posición en la precedencia: documento del **estrato de forma** — hermano de
`ley/2`. `ley/2` gobierna la forma del artefacto terminado; esta ley gobierna
el proceso que lo produce. Entre ambas, para el producto de una koraficación,
prevalece la más específica: esta.

Rationale: en la encarnación anterior este contrato vivía en md-spec como
régimen de koraficación y se llamaba «funtor K». Aquí se reconoce como
transformación editorial gobernada: no se han definido categorías, morfismos
ni leyes functoriales, y la preservación de verdad se audita mediante FS. La maquinaria que lo rodeaba
(familias retiradas, productor atomize, perfiles por familia) no regresa; el
contrato sí, porque sin él KORA no produce — solo custodia.

## 1. Definición y alcance

1. **Koraficación** — proceso que toma una fuente (documento humano, corpus
   externo, transcripción, nota técnica) y emite un artefacto de tipo
   conocimiento conforme a `ley/2`, preservando el 100% de los hechos de la
   fuente con menor superficie textual.
2. Esta ley aplica SOLO a la producción de artefactos de **conocimiento**.
   NO DEBE aplicarse a cuerpos agénticos (los rige `ley/2` §10) ni a la ley
   misma (que no es artefacto).
3. El productor PUEDE ser humano o sistema LLM. El contrato obliga igual a
   ambos: la fidelidad no es negociable por modo de producción.

## 2. Definiciones

- **Fuente** — material de entrada de la koraficación.
- **Salida** — el artefacto de conocimiento emitido.
- **Hecho** — unidad de verdad de la fuente: condición, umbral, excepción,
  fecha, cifra, dependencia, referencia, definición o relación.
  Rationale: la encarnación anterior enumeraba las siete primeras; pneuma
  añade definición y relación — estrecha la protección, no la relaja.
- **Clases de hecho** — todo hecho de la fuente se clasifica en una de
  cuatro: `preservado` (literal en la salida), `comprimido` (reformulado sin
  pérdida), `omitido` (ausente — hace fallar FS), `agregado` (presente en la
  salida sin existir en la fuente — hecho inventado: hace fallar la
  koraficación por sí solo, aunque FS de los demás sea 100%).
- **FS (fidelity score)** — `FS = (preservados + comprimidos) / N_hechos × 100`.
- **CR (compression ratio)** — `CR = len(fuente) / len(salida)`.
- **Esqueleto** — la estructura de la fuente (jerarquía, orden, agrupación).
- **Carne** — los hechos.
- **Grasa** — todo lo que puede eliminarse sin perder hechos ni estructura.

## 3. Preservación de verdad — la prueba ácida

La regla central de toda koraficación:

1. Si al eliminar un texto cambia solo el tono o la fluidez, **DEBE**
   eliminarse.
2. Si al eliminar un texto desaparece una condición, umbral, excepción,
   fecha, cifra, dependencia o referencia, **NO DEBE** eliminarse.

Metáfora operativa: el esqueleto se preserva como estructura, la carne se
preserva siempre, la grasa se elimina siempre.

Correcto: comprimir "en la mayoría de los casos observados durante el
estudio, aproximadamente el 70% de los pacientes" a "70% de los pacientes
(del estudio)".
Incorrecto: comprimir "70% de los pacientes adultos; en pediatría no aplica"
a "70% de los pacientes" — desapareció una excepción: eso es carne, no grasa.

## 4. Métricas de cierre

1. `FS = 100%` es el criterio obligatorio de fidelidad. Si `FS < 100%`, la
   koraficación **falla** — sin excepciones.
2. `CR > 1,5` es el objetivo de compresión normal.
3. `CR < 1,5` **PUEDE** aceptarse solo si se cumplen las tres a la vez:
   `FS = 100%`, no queda grasa eliminable, y la realización superficial (§6)
   es válida.
4. Si la calidad de superficie falla, la koraficación falla aunque
   `FS = 100%`.

Rationale: la asimetría es deliberada — la compresión es objetivo, la
fidelidad es ley. Un artefacto fiel y poco comprimido es deuda menor; un
artefacto comprimido e infiel es veneno catalogado.

## 5. Telegrafización — T1 a T7

Para el producto de una koraficación, estas reglas son **DEBE** (a
diferencia de los cuerpos en general, donde `ley/2` §10 las hereda como
DEBERIA):

| Regla | Obligación |
|---|---|
| T1 | Eliminar perífrasis y verbos de enlace sin contenido. |
| T2 | Nominalizar acciones cuando mejore la densidad — válido solo si no destruye la naturalidad técnica. |
| T3 | Colapsar subordinadas condicionales a lista o tabla `Condición \| Resultado \| Base`. |
| T4 | Eliminar marcadores discursivos sin reemplazo. |
| T5 | Comprimir enumeraciones embebidas en prosa a listas. |
| T6 | Sujeto una vez (en el heading); luego implícito. |
| T7 | Promover comparaciones y matrices de condiciones a tablas. |

Patrones estructurales obligatorios:

1. Definiciones: `**Término** — descripción compacta`.
2. Procedimientos: lista secuencial numerada.
3. Comparaciones: tabla — NUNCA párrafo si la relación ya es matricial.
4. Enumeraciones: lista con marcadores — NUNCA embebidas en prosa.

Grasa prohibida (cada elemento NO DEBE aparecer en la salida):
introducciones vacías ("En este documento veremos…"), transiciones ("A
continuación", "Por otro lado"), hedging sin contenido ("probablemente",
"en general", "suele"), preguntas retóricas, saludos y cierres, duplicación
de hechos (un hecho vive una sola vez; SSOT también dentro del documento).

## 6. Realización superficial

1. La salida **DEBE** sonar a conocimiento curado, no a dump comprimido.
2. La salida **NO DEBE** producir labelese, frases mecánicas ni
   headings-campo (serializar campos como encabezados).
3. Un heading **NO DEBE** terminar truncado con `...`.
4. Listas y tablas se usan solo si mejoran recuperación o comparabilidad —
   no como decoración ni como serialización cruda.

Correcto: `## Criterios de ingreso a HODOM` seguido de la tabla de criterios.
Incorrecto: `#### Título` / `#### Path` / `#### Valor` — eso es un registro
disfrazado de documento.

## 7. Estructura recuperable

1. Jerarquía máxima `####`; un `###` NO DEBE existir sin `##` padre.
2. Cada `##` **DEBE** poder leerse de forma casi aislada, con sujeto y
   alcance explícitos — el heading primario expresa el sujeto; el mero
   ordinal no basta.
3. El idioma de la salida **DEBE** coincidir con el de la fuente, salvo
   traducción explícita declarada en `fuente:`.

## 8. Procedencia

1. El campo `fuente:` del artefacto producido **DEBE** declarar la
   procedencia documental de la koraficación.
2. Si la fuente vive fuera del repo, `fuente:` **DEBERIA** incluir su hash
   (`sha256:`) o una referencia estable equivalente.
3. Si la koraficación descarta secciones enteras de la fuente por estar
   fuera de alcance, el descarte **DEBE** declararse en `fuente:` o en el
   cuerpo — el recorte de alcance no es pérdida de fidelidad, pero callarlo
   sí es pérdida oculta.

## 9. Obligaciones deterministas del productor

Antes de dar por cerrada una koraficación, el productor **DEBE** verificar:

1. Cada hecho de la fuente clasificado en su clase (§2); ningún `omitido`
   sin recorte de alcance declarado (§8.3) y ningún `agregado`.
2. Cifras de la fuente presentes en la salida.
3. Fechas de la fuente presentes en la salida.
4. Listas y tablas de la fuente no degradadas a prosa.
5. Referencias de la fuente preservadas o declaradas como descartadas (§8.3).
6. Headings sin truncar; sin headings-campo.
7. Frontmatter conforme a `ley/2` (eso sí lo mecaniza `velar`).

## 10. Validación

| Verificación | Criterio | Enforcement |
|---|---|---|
| Forma del artefacto producido | `ley/2` completa (gramática, campos, zona, URN) | mecanizado (`velar`: forma-valida, nombre-verdadero, lugar-coincide…) |
| Dignidad de publicación | ≥3 tags, descripción y fuente no vacías | mecanizado (`velar --estricto`: publicacion-digna) |
| Gate de promoción | borrador → publicado solo si el snapshot pasa `velar --estricto` y el destino satisface `publicacion-digna` | mecanizado (`ciclo`) |
| `FS = 100%` | prueba ácida §3 contra la fuente | declarado |
| `CR > 1,5` o justificación §4.3 | medición contra la fuente | declarado |
| Telegrafización T1-T7 | §5 | declarado |
| Realización superficial | §6 | declarado |
| Obligaciones deterministas | §9 | declarado |

Nota de honestidad (heredada de la doctrina de esta casa): pneuma **NO
mecaniza** FS, CR ni telegrafización — verificarlas exige acceso a la
fuente, que no vive en el repo. Son obligación declarada del productor, no
garantía verificada por `velar`. Esta ley NO DEBE citarse como si `velar`
garantizara fidelidad de koraficación: `velar` garantiza la forma del
resultado; la verdad del contenido la garantiza el proceso — y quien lo
ejecuta responde por él.

## 11. Relación con la encarnación anterior

Esta ley sublima el régimen de koraficación de md-spec. No regresan: las
familias documentales retiradas, el productor canónico atomize, los perfiles
de chunk por familia ni las métricas de tamaño por archivo. La familia del
producto se declara según `ley/2` §familias (`nota`, `fuente`, `bok`).

---

Sublimado de md-spec (régimen de koraficación: prueba ácida, FS/CR y clases
de hecho, telegrafización, realización superficial) el 2026-06-12; ver
GENESIS.md. El §8 (procedencia con hash y descarte declarado) es ley nueva
de pneuma, no sublimación: la encarnación anterior no lo legislaba así.

v1.1.0 (2026-07-18): corrección de estatus epistémico. «Funtor K» queda como
nombre histórico; la koraficación es una transformación editorial con
fidelidad auditada, no un funtor demostrado.

v1.2.0 (2026-07-18): precisa el gate de promoción sin alterar el shape:
`ciclo` exige el registro estricto del snapshot actual y evalúa
`publicacion-digna` sobre el estado destino antes de publicar.
