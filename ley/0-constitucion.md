# KORA/Constitución — ley pneuma v1.4.0

Estrato 0 de la ley. Por encima de él no hay norma; por debajo, toda norma se
le subordina. Define qué es KORA, qué gestiona y qué no, cómo se ordena la
ley, cómo viven y mueren los artefactos, y cómo cambia la ley misma.

## 1. Definición

**KORA** es el repositorio, catálogo y sistema de producción y mantenimiento
de los artefactos que consumen o ejecutan sistemas LLM. No es una aplicación:
produce artefactos bajo esta ley, los cataloga y resuelve por URN, los
mantiene coherentes en el tiempo (checks, lifecycle, deprecación) y proyecta
los ejecutables a runtimes.

**pneuma** es el cuerpo vigente de KORA. La entidad sigue siendo KORA: el
cuerpo cambia, el nombre verdadero no. El principio rector se hereda intacto,
como garantía formal y no como definición:

> KORA = vector ontológico PMI × LFS + shape unificado de autoría +
> transmutación funtorial.

`ALMA.md` es el documento fundacional del que esta ley desciende. Ante
silencio de la ley, ALMA orienta la interpretación; ante regla explícita,
manda la ley según la precedencia de §5.

Desde el 2026-06-14, por decisión HITL del operador, **pneuma es la fuente
única de doctrina futura de KORA**: toda evolución doctrinal se autora en esta
ley (`ley/0..4`); la ley de la encarnación anterior (la bestia, `~/kora`)
queda congelada salvo correcciones de verdad. El régimen completo —freeze de
la bestia, estatus delegado legacy de `openclaw`/`hermes` y disparadores de
migración— se declara en `urn:kora:kb:regimen-de-ley`.

## 2. Definiciones

- **Artefacto** — unidad gobernada por esta ley: archivo con frontmatter
  válido (ley/2) bajo `artefactos/`.
- **Censo** — catálogo derivado del corpus, producido por el gesto `censo`.
- **Emisión** — proyección de un artefacto a un runtime, producida por el
  gesto `transmutar` (ley/3).
- **Enforcement `mecanizado`** — la regla la verifica el núcleo `kora.py`;
  violarla produce fallo con exit distinto de 0.
- **Enforcement `declarado`** — la regla obliga, pero ningún gesto la
  verifica. La ley lo dice en voz alta y NO DEBE fingir lo contrario.

## 3. Tres tipos de artefacto, y solo tres

KORA gestiona **tres tipos de artefacto, y solo tres**:

1. **conocimiento** — `.md` para *consumo* de sistemas LLM: se lee como
   contexto, no se ejecuta.
2. **agentes** — actores; se *proyectan a runtimes* vía transmutación.
3. **skills** — capacidades; se proyectan igual que los agentes.

El término "conocimiento" designa solo el tipo 1; NO DEBE usarse como
paraguas de los otros dos. El tipo no se declara: se deriva mecánicamente del
shape (ley/2 §5). Agentes y skills son el mismo objeto ontológico variando
por arnés (ley/1 §6); su separación en tipos es operacional, no categorial.

## 4. La ley no es artefacto

Los documentos de `ley/` **no son artefactos**: son la ley que define qué
cuenta como artefacto válido. NO DEBEN llevar URN ni frontmatter de artefacto;
un encabezado con versión en el título basta. NO DEBEN residir en
`artefactos/` ni aparecer en el censo.

Rationale: la frontera entre la materia y la ley sobre la materia es la
distinción que constituye a KORA. Sin esa frontera no hay KORA; hay solo una
carpeta de archivos.

## 5. Precedencia

Cuando dos fuentes parezcan contradecirse, prevalece la de estrato menor:

1. `ley/0-constitucion.md` — constitución.
2. `ley/1-ontologia.md` — ontología.
3. `ley/2-forma.md` y `ley/4-koraficacion.md` — forma (serialización y
   producción; comparten estrato: entre ambas prevalece la más específica
   para el objeto — `ley/2` para la forma del artefacto terminado, `ley/4`
   para el proceso que produce conocimiento korificado).
4. `ley/3-transmutacion.md` — transmutación.
5. Derivados: censo, `_emision/`, mensajes del núcleo, docs auxiliares.

Un estrato inferior PUEDE estrechar reglas del superior; NO DEBE relajarlas
ni por declaración ni por omisión. Los derivados no tienen voz normativa.

## 6. Fuente de verdad

1. El filesystem con frontmatters válidos es la **única fuente de verdad**.
2. El censo es **siempre derivado**: se regenera desde el filesystem en cada
   invocación, jamás es autoridad y NO DEBE versionarse (`censo.json` vive en
   `.gitignore`). Si censo y filesystem divergen, el censo está mal y se
   regenera; el filesystem no se discute.
3. Las emisiones (`_emision/`) son derivadas y regenerables; NUNCA son fuente
   primaria y NO DEBEN versionarse.
4. Un derivado NO DEBE editarse a mano.

Rationale: el gesto de catalogar no crea autoridad; la refleja. KORA no
confunde el mapa con el territorio.

## 7. Régimen de URN

Existen **dos regímenes, y solo dos**, ambos sin versión embebida:

| Régimen | Gramática | Tipo |
|---|---|---|
| conceptual | `urn:{ns}:kb:{id}` | conocimiento |
| artefacto agéntico | `urn:{ns}:artefacto:{id}` | agentes y skills |

Reglas:

1. Todo URN DEBE cumplir la regex
   `^urn:[a-z0-9]+(-[a-z0-9]+)*:(kb|artefacto):[a-z0-9]+(-[a-z0-9]+)*$`.
2. El URN NO DEBE llevar versión embebida. La versión es accidente del
   tiempo, no de la esencia: vive en el campo `version` del frontmatter.
   Toda referencia usa la forma sin versión; la resolución de versión es
   responsabilidad del censo, no del nombre.
3. Un artefacto NO DEBE declarar URN en dos regímenes; el régimen DEBE
   coincidir con el tipo derivado (kb ⟺ conocimiento, artefacto ⟺ agéntico).
4. El URN DEBE ser único en todo el corpus.

Correcto:

```text
urn:kora:kb:alma-de-kora
urn:dev:artefacto:polymath
```

Incorrecto:

```text
urn:kora:kb:alma-de-kora:1.0.0    # versión embebida
urn:kora:spec:gobernanza          # régimen inexistente
urn:kora:artefacto:Mente_Omega    # mayúsculas y guion bajo
```

## 8. Lifecycle

Cadenas de estados, una por tipo:

- conocimiento: `borrador → publicado → deprecado`
- agéntico (agentes y skills): `borrador → activo → deprecado → retirado`

Reglas:

1. Toda transición DEBE ser estrictamente hacia adelante en la cadena del
   tipo. **Cualquier salto hacia adelante es válido** (`borrador →
   deprecado`, `activo → retirado`).
2. Las transiciones inversas son SIEMPRE inválidas. Un retirado no se
   reactiva: se emite un artefacto nuevo con `reemplaza` apuntando al muerto.
3. El gesto `ciclo` es el único camino mecanizado de transición; edita el
   campo `estado` in-place preservando el resto del archivo byte-idéntico.

Rationale: la encarnación anterior declaraba las cadenas y prohibía las
inversas, pero callaba sobre los saltos hacia adelante. Esta ley PRECISA esa
ambigüedad que la bestia dejó abierta: el orden de la cadena es un orden
estricto, y avanzar es legal desde cualquier estado hacia cualquier estado
posterior.

## 9. Dignidad del URN

1. El URN de los deprecados y retirados **sigue resolviendo** en `censo` y en
   `nombre` (con marca de estado). Ningún gesto excluye un artefacto del
   censo por su estado.
2. Toda referencia URN resuelve también contra muertos (ley/2 §9).

KORA no borra: jubila. Morir bajo esta ley es dejar de ejecutarse sin dejar
de poder ser nombrado.

## 10. Los seis gestos

El núcleo `kora.py` realiza la ley con seis gestos:

| Gesto | Qué hace |
|---|---|
| `censo` | cataloga el corpus; vista derivada, jamás autoridad (§6) |
| `nombre <urn>` | resuelve el nombre verdadero: path, tipo, versión, estado; también muertos, con marca (§9) |
| `velar [--estricto]` | corre el registro completo de checks (§11) |
| `transmutar` | proyecta un artefacto a un target vía funtor (ley/3) |
| `ciclo <urn> <estado>` | transición de lifecycle, solo hacia adelante (§8) |
| `ley` | concatena `ALMA.md` + los cuatro estratos: KORA cabe en un contexto |

Exit codes: `0` ok; `1` fallo de validación u operación; `2` error de uso o
Python < 3.11.

## 11. Registro de checks

El registro es **cerrado**: `velar` corre exactamente estos checks; añadir,
quitar o renombrar uno es cambio de ley (§12). Cada estrato detalla los suyos.

| # | Check | Vela por | Estrato |
|---|---|---|---|
| 1 | `forma-valida` | gramática y campos del shape | ley/2 |
| 2 | `nombre-verdadero` | URN: gramática, régimen, unicidad | ley/0 §7 |
| 3 | `lugar-coincide` | zona, namespace y nombre de archivo | ley/2 |
| 4 | `vector-en-reticulo` | rangos de los seis ejes | ley/1 |
| 5 | `leyes-inter-eje` | las cinco leyes de coherencia | ley/1 |
| 6 | `dominio-forma` | vector dentro del dominio de su forma | ley/2 |
| 7 | `arnes-compatible` | par (arnés, forma) legal | ley/2 |
| 8 | `estado-valido` | estado en la cadena del tipo | ley/0 §8 |
| 9 | `referencias-resuelven` | toda referencia URN resuelve en el censo | ley/2 |
| 10 | `relaciones-legales` | aciclicidad, antisimetría, estado del target de `reemplaza` | ley/2 |
| 11 | `targets-conocidos` | `targets` ⊆ los cinco reconocidos | ley/3 |
| 12 | `sello-fresco` | presencia del sello y frescura del `hash-fuente` en emisiones; no su buena forma completa, que queda declarada (ley/3 §9) | ley/3 |
| + | `publicacion-digna` | solo con `--estricto`: exigencias de publicación | ley/2 |

## 12. Cambio de la propia ley

1. Cada estrato versiona en su título (semver). Corrección editorial: patch;
   precisión compatible: minor; cambio de enums, rangos, ids de checks,
   cadenas de lifecycle o **ruptura del formato del sello** (que altera o
   invalida emisiones previas): major. Una **extensión aditiva del sello** —un
   campo que solo aparece para los artefactos que lo declaran y deja
   byte-idénticas las emisiones que no lo declaran— es precisión compatible:
   minor.
2. `ley/1-ontologia.md` está en **freeze heredado**: solo se permiten
   correcciones de verdad necesarias. NO DEBE recibir nuevos ejes, nuevos
   niveles ni expansiones doctrinales durante el freeze; todo cambio se
   justifica como fix puntual, no como rediseño conceptual.
3. Todo cambio major de cualquier estrato DEBE mediar decisión humana
   explícita del operador.
4. Un cambio de ley NO DEBE relajar el canon para encubrir un artefacto mal
   formado.

## 13. Validación

| Regla | Detalle | Enforcement |
|---|---|---|
| Régimen URN coincide con tipo | kb ⟺ conocimiento; artefacto ⟺ agéntico | mecanizado (`nombre-verdadero`) |
| URN bien formado y único | regex §7, sin versión embebida | mecanizado (`nombre-verdadero`) |
| Estado pertenece a la cadena del tipo | §8 | mecanizado (`estado-valido`) |
| Transición solo hacia adelante | §8 | mecanizado (gesto `ciclo`) |
| Dignidad del URN | muertos resuelven en `censo` y `nombre` | mecanizado (`censo`, `nombre`) |
| Censo jamás versionado | `censo.json` en `.gitignore` | mecanizado (`.gitignore`) |
| Derivados sin voz normativa | §5, §6 | declarado |
| La ley no es artefacto | `ley/` sin URN ni frontmatter | declarado |
| Freeze de la ontología | §12 r2 | declarado |

Sublimado de KORA/Gobernanza v6.2.0 (con el lifecycle de knowledge-spec
v3.0.0 y autoria-spec v2.0.0) el 2026-06-11; ver GENESIS.md.

v1.3.0 (HITL 2026-06-14): §1 declara a pneuma fuente única de doctrina futura
y congela la ley de la bestia; régimen completo en `urn:kora:kb:regimen-de-ley`.

v1.4.0 (HITL 2026-06-15): §12.1 distingue **ruptura** del formato del sello
(major) de **extensión aditiva byte-idéntica** (minor), cerrando la categoría
que faltaba; habilita el bump minor de `ley/3` v1.2.0 (contrato-conocimiento).
