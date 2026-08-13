# KORA/Koraficación — ley pneuma v2.0.0

Contrato de producción del dominio documental: transforma fuentes humanas o
documentales en conocimiento KORA denso, trazable y directamente consumible por
sistemas LLM. Sin este proceso, pneuma solo custodiaría documentos; con él,
produce conocimiento sin ocultar lo que preserva, excluye o todavía no auditó.

Posición en la precedencia: estrato de forma, hermano de `ley/2`. `ley/2`
gobierna el artefacto terminado; esta ley gobierna el proceso documental. No
crea un cuarto tipo ni añade campos al frontmatter.

## 1. Función y alcance

1. **Koraficación** — transformación editorial gobernada
   `K_Ω(s) → k`, donde `s` es un snapshot documental identificable, `Ω`
   su alcance semántico declarado y `k` un artefacto de conocimiento válido.
2. La koraficación busca la menor superficie textual que preserve íntegramente
   la semántica pertinente a `Ω`. No promete conservar bytes, estilo humano ni
   información situada fuera del alcance. `Ω` DEBE cubrir todo el contenido de
   la fuente relevante para el propósito declarado; no puede estrecharse para
   ocultar omisiones ni mejorar una métrica de compresión.
3. Aplica solo a conocimiento. Los cuerpos agénticos se autoran conforme a
   `ley/2`; la ley no es artefacto.
4. El productor puede ser humano o sistema LLM. Las obligaciones no cambian.
5. Koraficar, transponer y autorar de forma nativa son procesos de procedencia,
   no tipos excluyentes de artefacto. Una salida koraficada puede alimentar una
   transposición posterior con pérdida declarada.

## 2. Unidades de contraste

- **Fuente `s`** — snapshot de entrada, identificable por referencia estable,
  versión o hash cuando corresponda.
- **Alcance `Ω`** — partes y propósitos incluidos, junto con exclusiones
  explícitas. Una exclusión declarada queda fuera del claim; callarla es pérdida
  oculta.
- **Unidad semántica** — afirmación, definición, condición, negación, umbral,
  cifra, fecha, instrucción, excepción, hipótesis, grado de certeza, referencia
  o relación relevante. Una figura, tabla, orden o repetición también es unidad
  cuando porta estructura, autoridad, énfasis o modalidad.
- **Inventario `I_Ω`** — conjunto finito de unidades semánticas dentro del
  alcance. Puede ser evidencia efímera de trabajo; esta ley no exige un archivo,
  reporte ni campo nuevo.
- **Salida `k`** — artefacto KORA que representa el inventario con menor
  superficie recuperable.
- **Sustento** — correspondencia de una afirmación de salida con su fuente. Si
  se necesita enriquecimiento externo, se incorpora como fuente identificada
  antes del contraste; no se mezcla después como si proviniera de `s`.
- **Superficie removible** — texto o estructura cuya eliminación no altera
  ninguna unidad, relación, modalidad ni procedencia dentro de `Ω`.

## 3. Tres invariantes de integridad semántica

Una koraficación solo puede cerrar `PASS` si satisface simultáneamente:

1. **Cobertura.** Cada unidad de `I_Ω` tiene una representación recuperable en
   `k`. Varias unidades pueden comprimirse juntas si continúan distinguibles.
2. **Sustento.** Cada afirmación de `k` está sustentada por `s`. Inventar,
   mezclar autoridades o elevar una hipótesis a hecho hace fallar el proceso.
3. **Preservación relacional.** `k` conserva negación, modalidad, certeza,
   alcance, orden causal o temporal, condiciones, excepciones, dependencias,
   referencias, atribución y estructura visual relevantes.

La integridad es relativa a una fuente y un alcance declarados, no una
equivalencia semántica universal. La reducción de superficie nunca compensa una
violación de estos invariantes.

Ejemplo correcto: «en la mayoría de los casos observados durante el estudio,
aproximadamente el 70% de los pacientes» → «70% de los pacientes del estudio».

Ejemplo incorrecto: «70% de adultos; no aplica en pediatría» → «70% de los
pacientes». Se perdió una restricción de dominio.

## 4. Estados de evidencia

La auditoría semántica reporta exactamente uno de estos estados:

| Estado | Criterio |
|---|---|
| `PASS` | fuente y alcance disponibles; cobertura, sustento, relaciones y superficie contrastados sin hallazgos |
| `FAIL` | existe omisión, invención, cambio de modalidad/relación o defecto superficial conocido |
| `ABSENT` | falta la fuente, su identidad estable o el material necesario para contrastar |
| `NOT_RUN` | la comparación semántica no se ejecutó |

El estado pertenece a la evidencia de la revisión; no se añade al frontmatter.
Un artefacto puede pasar `velar` y tener auditoría semántica `FAIL`,
`ABSENT` o `NOT_RUN`.

Las declaraciones históricas `FS` o `CR` de artefactos existentes conservan
su valor de procedencia, pero no equivalen a `PASS` bajo v2. No se exige una
migración masiva: se sustituyen solo cuando una auditoría semántica real vuelva
a abrir el artefacto.

Desde v2, una koraficación nueva o reabierta solo puede promoverse o cerrarse
como koraficación con evidencia `PASS`. `FAIL` exige corrección; `ABSENT` y
`NOT_RUN` no autorizan un claim de cierre. Los artefactos publicados antes de
v2 conservan su estado histórico sin adquirir `PASS` retroactivamente.

## 5. Densidad después de integridad

1. Solo después de preservar los tres invariantes se minimiza la superficie.
2. No existe un `FS` escalar ni un umbral universal de compresión: contar
   «hechos» no captura relaciones, modalidad ni estructura y produce precisión
   aparente.
3. La reducción de caracteres puede informarse cuando tenga consumidor. Una
   medición de tokens DEBE nombrar tokenizer y versión; sin eso no es
   reproducible.
4. Una salida poco más corta puede ser `PASS` si no queda superficie removible.
   Una salida muy corta es `FAIL` si altera una sola unidad semántica.
5. Repetición no equivale automáticamente a redundancia: puede expresar énfasis,
   autoridad, contraste o conflicto. Se elimina solo cuando su función es nula
   dentro de `Ω`.

## 6. Transformaciones admisibles

Después de asegurar los invariantes, el productor DEBERIA:

- eliminar introducciones, cierres y transiciones sin función semántica;
- convertir enumeraciones y procedimientos en listas recuperables;
- convertir comparaciones genuinamente matriciales en tablas;
- fusionar duplicados reales bajo una sola fuente de verdad;
- acortar perífrasis y sujetos repetidos;
- mantener lenguaje técnico natural cuando nominalizar o telegrafiar lo degrade.

No se eliminan como «grasa» calificadores como «probable», «en general»,
«según X», «salvo» o «no verificado» cuando modifican certeza, alcance o
autoridad.

Las listas y tablas son medios, no formato obligatorio. Una prosa compacta es
preferible cuando preserva mejor la relación.

## 7. Realización recuperable

1. La salida DEBE leerse como conocimiento curado, no como dump o serialización
   de campos.
2. Headings, listas y tablas se usan para recuperar relaciones, no para decorar.
   Un heading no termina truncado ni reemplaza al sujeto real.
3. El idioma coincide con la fuente, salvo traducción declarada.
4. Diagramas, tablas o imágenes estructurantes dentro de `Ω` DEBEN quedar
   representados o referenciados. Omitirlos sin exclusión explícita es
   `FAIL`.
5. La salida puede optimizarse para consumo de modelos sin renunciar a que un
   humano pueda auditar fuente, alcance y transformaciones decisivas.

## 8. Procedencia y frontera de la fuente

1. `fuente:` DEBE identificar la procedencia documental. Si la fuente vive
   fuera del repositorio, DEBERIA incluir `sha256:` o referencia estable
   equivalente.
2. Toda exclusión de alcance DEBE declararse en `fuente:` o en el cuerpo.
3. El artefacto koraficado no sustituye la evidencia original. Fuentes
   OWL/SKOS, XML, schemas, datos raw o material visual permanecen externas
   cuando KORA/MD no puede representar fielmente su semántica técnica; rige
   `urn:kora:kb:frontera-fuentes-tecnicas`.
4. Una transposición posterior declara sus propias pérdidas y no hereda
   automáticamente el `PASS` de la koraficación que la alimentó.

## 9. Proceso mínimo

1. Identificar el snapshot fuente.
2. Delimitar `Ω` y declarar exclusiones.
3. Establecer `I_Ω`, sin obligación de persistirlo.
4. Producir la salida compacta.
5. Contrastar fuente→salida para cobertura y salida→fuente para sustento.
6. Revisar relaciones, modalidad, contenido visual y superficie removible.
7. Reportar `PASS|FAIL|ABSENT|NOT_RUN` con el hallazgo decisivo.

No se exige plan, dashboard, manifiesto ni recibo persistente. La evidencia
necesaria depende del riesgo y puede vivir en la revisión que decide promoción.

## 10. Validación

| Plano | Criterio | Enforcement |
|---|---|---|
| Forma del artefacto | `ley/2`: gramática, zona, URN y campos | mecanizado por `velar` |
| Dignidad de publicación | `descripcion` y `fuente` no vacías | mecanizado por `velar --estricto` y `ciclo` |
| Integridad semántica | cobertura + sustento + preservación relacional contra `s,Ω` | declarado; auditoría humana o LLM contrastada |
| Cierre o promoción de koraficación nueva o reabierta | evidencia semántica `PASS` | declarado; decisión de promoción, no mecanizada |
| Realización recuperable | §7 | declarado |
| Densidad | reducción posterior a integridad; tokenizer identificado si aplica | opcional, reproducible cuando se reporta |

`velar` garantiza forma, no verdad documental. La ausencia de una auditoría
semántica produce `NOT_RUN`, nunca `PASS` implícito.

## 11. Frontera categorial

`K_Ω` es notación operacional. KORA no ha definido categorías de fuentes,
unidades y transformaciones ni una acción sobre morfismos; por tanto la
koraficación no es un funtor demostrado. «Fiel» en teoría de categorías es una
propiedad de hom-sets, no sinónimo de «sin pérdida documental».

Tampoco se afirma reversibilidad, identidad textual, equivalencia universal ni
que la salida preserve semántica no incluida en `Ω`.

---

Sublimado inicialmente de md-spec el 2026-06-12. La v1 separó koraficación de
«funtor K», añadió procedencia y mecanizó solo la forma y la promoción.

v2.0.0 (2026-08-13): reemplaza `FS=100%` y `CR>1,5` por cobertura, sustento
y preservación relacional respecto de fuente y alcance explícitos; incorpora
`PASS|FAIL|ABSENT|NOT_RUN`, subordina toda métrica de densidad a integridad,
protege modalidad y contenido visual, y elimina la familia documental como
requisito del proceso. No añade campos ni maquinaria ceremonial.
