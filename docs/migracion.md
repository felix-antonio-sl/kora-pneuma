# Migración del corpus KORA

Inspección y migración del filesystem vivo realizadas el 2026-09-05. Este
documento registra decisiones del importador y la auditoría independiente de
preservación. Las comprobaciones materiales descritas aquí no acreditan
fidelidad semántica, instalación ni conducta de Codex o Hermes. El origen se
mantuvo en solo lectura durante la construcción independiente. Después del
relevo, los originales capturados se conservan en
`/home/felix/kora-pneuma/._local/legacy-before-rebuild`.

## Denominador que debe conservarse

El denominador deriva de los archivos presentes en
`/home/felix/kora-pneuma/artefactos`, incluidos los no confirmados en Git. No se
obtiene del censo ni de `_emision`.

| Contenido observado | Archivos | Identidades URN |
|---|---:|---:|
| Conocimiento | 460 | 460 |
| Agentes | 29 | 29 |
| Skills y recursos empaquetados | 105 | 41 |
| Total | 594 | 530 |

El primer corte observó 12.820.708 bytes y la comprobación posterior del importador
observó 12.824.313 bytes con los mismos 594 archivos y el mismo HEAD. La diferencia
se informó a integración para contrastarla con su base recuperable; cada
ejecución fija su propio digest de contenido. No hay URNs declarativas duplicadas ni enlaces simbólicos
dentro de `artefactos`. Los 64 recursos auxiliares comprenden 57 Markdown,
4 textos, 1 YAML, 1 Python y 1 plantilla de gitignore. Incluyen licencias,
plantillas, índices de documentación, fuentes literales y un script; preservar
solo `SKILL.md` perdería funciones y procedencia.

El conocimiento incluye 373 publicados, 86 borradores y 1 deprecado; hay
28 agentes activos y 1 retirado, y 37 skills activas y 4 deprecadas. Un borrador
es contenido conservable y su estado se preserva; no se transforma en una
publicación aprobada. Los estados no vigentes tampoco autorizan borrar sus
identidades o sus fuentes.

`_archivo` conserva otros 35 archivos y 422.527 bytes. `git ls-files _archivo`
no devuelve archivos: son archivos ignorados, ajenos al corpus versionado. Se
preservan en el origen y en el respaldo privado de integración cuya restauración
se comprobó; no se incorporan automáticamente a `archive` ni a Git. No se
inspeccionó su contenido personal ni clínico para este inventario. `_emision`
contiene 402 derivados y
4.300.482 bytes: es evidencia de realizaciones anteriores, no fuente para
importar. La base recuperable que toma la tarea integradora cubre también Git,
cambios locales y archivos no seguidos. `.remember`, memorias, sesiones,
credenciales y estado personal quedan fuera de la ingesta.

## Forma nueva y preservación

Cada objeto tiene `products/<namespace>/<slug>/object.yaml`, una identidad `id`
URN estable, `kind`, `name`, `description` y un `content` relativo. El importador
y la auditoría de migración interpretan el encabezado anterior en el límite de
entrada. La operación normal lee la forma nueva.

- En conocimiento, `content.md` conserva el archivo original completo, byte a
  byte. El encabezado anterior dentro de ese contenido es procedencia documental;
  los metadatos operacionales se leen solo de `object.yaml`.
- En agentes y skills, `content.md` conserva exactamente el cuerpo, sin el
  frontmatter anterior. `provenance.legacy_header` conserva el prefijo literal,
  delimitadores y saltos de línea incluidos. Su concatenación con el cuerpo debe
  reconstruir los bytes originales.
- `provenance` guarda la ruta de origen, su SHA-256 y el estado original. No
  convierte `version`, vectores, herramientas, forma, sello o targets antiguos
  en requisitos de la maquinaria nueva.
- Los recursos auxiliares conservan bytes, nombres, jerarquía y modo ejecutable
  cuando corresponda. Las referencias relativas siguen junto al objeto.
- Las relaciones tipadas se conservan en `relations`. Las relaciones documentales
  no declaran automáticamente composición, autorización ni instalación.
- Los targets operacionales solo pueden ser Codex o Hermes. La lista antigua
  queda recuperable en la procedencia, sin crear adaptadores para ella.

El importador debe rechazar colisiones, fuentes modificadas durante la lectura y
una segunda importación que pueda pisar ediciones del destino. Un inventario
generado acompaña la ejecución como salida; no se mantiene un segundo registro
manual de objetos.

## Maquinaria que se reconstruye

La clasificación considera la función del contenido, no su carpeta. Estos
objetos enseñan, gobiernan o realizan KORA y recibieron implementación o
contenido nuevo antes de volver a estar activos. Sus originales se preservan
en `archive/previous` para comparación y recuperación.

| Identidad, omitiendo el prefijo URN común | Función observada |
|---|---|
| `kora:artefacto:kora` | Opera los gestos y custodia el canon anterior. |
| `dev:artefacto:agent-architect` | Autora agentes contra la ley, vectores y gates anteriores. |
| `kora:artefacto:autoria-de-persona` | Produce personalidad y mapas de transmutación sujetos a esa maquinaria. |
| `kora:artefacto:auditoria-artefactos-kora` | Decide destinos contra la forma y el ciclo anteriores. |
| `kora:artefacto:auditoria-exposicion-kora` | Su script llama directamente a `kora.py censo --json`. |
| `kora:kb:alma-de-kora` | Describe la identidad y operación fundacionales anteriores. |
| `kora:kb:guia-rapida-pneuma` | Enseña comandos, forma y garantías anteriores. |
| `kora:kb:regimen-de-ley` | Declara la ley anterior como autoridad vigente. |
| `kora:kb:frontera-fuentes-tecnicas` | Regula cómo KORA conserva, archiva y transforma fuentes. |
| `kora:kb:cat-kora-kernel` | Formaliza vectores, sellos y proyecciones del núcleo anterior. |
| `kora:kb:cat-kora-semantica-operacional` | Formaliza las operaciones y estados anteriores. |
| `kora:kb:cat-contrato-ingenieria-agentica` | Fija el contrato y el shape para ingeniería de KORA. |

Las fuentes observadas están en `artefactos/agentes/kora/kora.md`,
`artefactos/agentes/dev/agent-architect.md`, las tres carpetas homónimas bajo
`artefactos/skills/kora/` y los siete Markdown homónimos bajo
`artefactos/conocimiento/kora/`.

Las doce identidades siguen resolviendo a sus sucesores activos. La procedencia
del sucesor señala el original mediante `previous`; las garantías y teorías de
la maquinaria anterior siguen recuperables allí, sin adoptarlas como requisitos
del núcleo nuevo. Los ajustes operacionales de `dov-dori` y
`consenso-deliberativo` también conservan sus dos originales. Estos catorce
antecedentes mantienen encabezados, cuerpos, recursos y modos; la auditoría los
prefiere al sucesor cuando reconstruye el corpus original.

Se conserva como conocimiento el contenido teórico de `cat-foundations`,
`cat-agent-modulo`, `cat-agent-coalgebra`, `aufbau-persona-agente` y
`cat-programacion-agentica-autonoma`. Sus funciones son exponer fundamentos,
modelos, analogías y límites, no operar el núcleo anterior. Sus referencias a
maquinaria deben conducir a identidades reconstruidas o antecedentes declarados;
no convierten una teoría en un requisito del sistema nuevo. Del mismo modo,
`mente-omega`, `cat-thinking`, `modelamiento-opm`, `pensamiento-modelador`,
`consenso-deliberativo` y `ux-design` son productos de uso aunque vivan bajo
`skills/kora`.

## Retiros y límites de realización

Se conservan fuera de instalación automática los seis objetos no vigentes del
origen: `polymath` (retirado), `entrega-kora`, `decision-operable`,
`analista-redes`, `constructor-tableros` y `cat-caso-vertical-steipete-codex`
(deprecados). `apoyo-decision-sanitaria` declara reemplazar a `analista-redes` y
`constructor-tableros`; `conducir-decisiones-hodom` declara reemplazar a
`decision-operable`. Los otros tres no declaran reemplazo. Esto se obtiene de
`estado` y `reemplaza`, sin inferir desaparición de la identidad.

`artefactos/agentes/ops/main.md` declara `urn:ops:artefacto:clawforge`; tiene
función de operador de flota y target exclusivo
OpenClaw. `deploy-flota-openclaw`, `fleet-canon-policy` y `handoff-policy` son
documentación operacional de ese destino. Se conservan como antecedentes o
fuentes de consumidores externos, pero no integran la maquinaria operacional
nueva. No se cambian sus servicios ni instalaciones ajenas.

## Referencias e incompatibilidades concretas

Las 1.243 aristas declaradas resuelven en el origen: 516 `cita`, 168 `depende`,
6 `refina`, 3 `reemplaza`, 436 `conocimiento` y 114 `componible`. Estas aristas no
cubren las menciones del cuerpo.

La procedencia declara 67 URNs KODA históricas. Se preservan como alias hacia
sus URNs actuales. Después de esa correspondencia quedan seis tokens corporales
que requieren tratamiento específico:

| Token o referencia | Tratamiento sustentado |
|---|---|
| `urn:salud:kb:hsc-gcl-1-2-vias-venosas-centrales` | Alias al mismo nombre con sufijo `-2025`; referencia de `hsc-hsc44-1-nutricion-parenteral.md:73`, destino existente con título concordante. |
| `urn:salud:kb:hsc-mo-2q-tele-organizacion-unidad-telemedicina` | Alias al mismo nombre con sufijo `-2023`; referencia de `hsc-pro-186-teletaco-anticoagulante-oral.md:87`, destino existente con título concordante. |
| `urn:fxsl:kb:ifml-` | Es el prefijo del patrón textual `urn:fxsl:kb:ifml-*` en `skills/fxsl/ifml/SKILL.md:240`; no es una identidad ni una referencia rota. |
| `urn:kora:kb:spec:1.0.0` | Dependencia de formato KODA incrustada en fuentes YAML preservadas; antecedente de maquinaria, no dependencia nueva. |
| `urn:kora:kb:transform:1.0.0` | Dependencia del método KODA incrustada en esas fuentes; mismo tratamiento histórico. |
| `urn:gorenuble:gn:bpmn-c4:1.0.0` | Referencia histórica al marco BPMN/C4 en ocho documentos; no hay identidad canónica equivalente demostrada. Se conserva y declara sin inventar un alias. |

Las tres últimas referencias se observan, por ejemplo, en
`artefactos/conocimiento/gn/gn-bpmn-d01-actos-administrativos.md:30` y
`artefactos/conocimiento/gn/bpmn-d08-rendiciones.md:30`. El YAML original se
mantiene en la fuente externa recuperable. La auditoría encontró respectivamente
61, 57 y 8 documentos que las contienen; cada uno conserva una fuente externa
existente cuyo SHA-256 coincide con el declarado. La revisión de los 87 archivos
externos no encontró un campo `urn` o `id` que declarara una de esas tres
identidades. La búsqueda literal en `artifacts/knowledge`, `serialization`,
`ontology` y `governance` del repositorio `kora`, en
`6bfaceb03f954722297a52aee77fc02ab701677b`, tampoco encontró esos identificadores.
Esta búsqueda acotada no demuestra ausencia en toda la historia. Las referencias
quedan como excepciones documentales concretas, sin fabricar alias ni
convertirlas en `requires` actuales.

La referencia secundaria `deep-opm-pro/docs/capa-categorial.md` de
`opm-categorial-es` fue retirada de ese repositorio; el propio KB ya declara el
retiro en su procedencia. Se comprobó `git log --all -- docs/capa-categorial.md`,
el árbol anterior a su eliminación y el blob exacto. Su último contenido antes
del retiro está en el commit `ffb98f3057db266151948a68429a77bb92655b17`, blob
`e53d5e90916a5bf3a7881818682b4b873c24fa8c`; se eliminó en
`2a83c1c59167ee24b7f7c972659c3a0528829c5a` el 2026-06-09.

Los 13.797 bytes del blob se recuperaron exactamente en
`products/fxsl/opm-categorial-es/sources/capa-categorial.md`, modo `0644`, SHA-256
`05aca5e796663980123f35e4ade6cf7b1d8df594dfcd754b82fa613bbf66dce9`.
`provenance.sources` registra ruta, hash, repositorio, commit, blob, retiro y su
rol de antecedente. El contenido vigente del KB permanece byte a byte igual al
original migrado. Esta recuperación de una fuente adicional no modifica el
denominador de 64 recursos que ya existían en pneuma ni restaura como autoridad
actual las afirmaciones del documento retirado.

## Fuentes técnicas y consumidores físicos

Los encabezados citan 87 archivos exactos de `/home/felix/kora-external-sources`
en 91 usos: 68 YAML, 18 Markdown y un texto. Los 87 existen y sus bytes coinciden
con los 87 SHA-256 declarados. Se conservan localizadores y rol como fuentes de
los productos en su procedencia original; el índice derivado de usos y
localizadores queda únicamente en un informe privado bajo `._local`. Esa
correspondencia no acredita por sí sola fidelidad semántica. El repositorio de
fuentes contiene, entre otros formatos, 17 TTL, un XML, PDF, imágenes, YAML y
texto. Ninguno se convierte forzosamente en prosa ni se absorbe completo por
estar junto a una fuente citada.

Las cuatro koraficaciones sustantivas de Langacker y su índice reconocen que
las figuras permanecen en el original; la fuente de texto y los recursos gráficos
existen. La koraficación ISUT de Alter declara recortes de bibliografía y
narración y que sus figuras no tienen equivalencia material con el resumen.
Estas pérdidas anteriores se preservan literalmente en `fuente`; la migración
no las borra ni las convierte en cobertura total.

Hay consumidores mediante enlaces simbólicos, además de rutas en instrucciones:

- `/home/felix/projects/hd-dt/kora-hodom` apunta al directorio
  `artefactos/conocimiento/salud`.
- Tres referencias OPM bajo
  `/home/felix/openclaw-fleet/blueprints/mente-omega/skills/opm-modeler/references/`
  apuntan a conocimiento `fxsl`.
- `/home/felix/openclaw-fleet/docs/fleet-canon-policy.md` y
  `/home/felix/openclaw-fleet/docs/handoff-policy.md` apuntan a las dos fuentes
  homónimas de conocimiento.

El relevo conserva esas rutas de lectura mediante enlaces hacia la única fuente
nueva. No mantiene otra copia editable ni instala un runtime retirado. La
inspección también encontró referencias KORA en `~/.agents/skills`,
`~/.codex/skills`, 13 archivos de `~/.codex/agents` y skills/SOUL de perfiles
Hermes. La presencia de una referencia es un candidato de consumidor; su
vigencia e instalación se comprueban en el trabajo de integración del runtime.
Regenerar solamente `_emision` no demuestra que esos consumidores se actualizaron.

## Consumidores manuales de Hermes

La revisión final de consumidores encontró además seis ubicaciones manuales
activas de Hermes que no pertenecían a la emisión anterior: dos copias de
`cat-thinking`, dos de `kora-pneuma-operations`, `kora-canon-compactacion` y
`research/koraficacion`. Sus 22 archivos, 13 payloads únicos y modos se
preservaron en blobs privados cotejados contra los archivos vivos. Los ejemplos
de configuración y el corte de estado de esa maquinaria permanecen como
antecedentes privados; no se incorporan a la fuente operacional ni a Git.

Los seis recursos de cada `cat-thinking` coincidieron con el producto migrado;
su wrapper abreviaba referencias y ordenaba consultar una ruta anterior. Se
habilita Hermes en el producto existente sin cambiar su contenido de dominio.
La operación de KORA pasa a las skills actuales de autoría, instalación y
koraficación. El método útil de simplificación se incorpora al agente KORA,
conservando función, consumidores, relaciones, costo y recuperación como
criterios. La búsqueda previa para evitar duplicados y la revisión de fragmentos
se incorporan a koraficación.

El auxiliar literal anterior podía aceptar un fragmento inventado presente en
la salida sin advertir su ausencia en la fuente. Su sustituto opcional
`check_fragments.py` contrasta ambos lados, rechaza selecciones vacías y
reconoce encabezados como fragmentos. Las pruebas comprueban esos resultados;
el auxiliar no acredita equivalencia semántica. Los originales manuales se
retiran de descubrimiento al actualizar sus consumidores y quedan recuperables
en el estado privado del relevo.

## Interfaz y comprobación

El importador permite comprobar otro árbol legado preservado contra un destino
nuevo. No se vuelve a importar sobre el catálogo activo:

```bash
python3 -m kora.migrate /ruta/al/legado-preservado /ruta/a/un/catalogo-nuevo --check
python3 -m unittest discover -s tests -p 'test_migrate.py' -v
```

`--check` enumera, interpreta y prepara la importación sin escribir. Devuelve JSON
con el denominador, digest de origen, decisiones de archivo, cambios de targets,
alias y brechas de referencias. No invoca el núcleo anterior ni inspecciona el
contenido de `_archivo`. Al omitir `--check`, publica archivos nuevos con creación
exclusiva: un destino ocupado bloquea la operación antes de escribir. Un fallo
retira solo los archivos propios que siguen iguales y conserva cambios
concurrentes. El origen permanece en solo lectura.

La API es `import_legacy(source: Path, destination: Path, dry_run=False) -> dict`.
Para separar preparación y aplicación se ofrecen `plan_import(source,
destination) -> MigrationPlan` y `apply_import(plan) -> dict`; la aplicación
comprueba otra vez que el conjunto, bytes y modos del origen no cambiaron antes y
después de publicar. Un cambio durante la publicación revierte la importación y
conserva la nueva edición del origen.

Los objetos conservados pero inactivos se ubican en `archive/products`; el
catálogo puede resolverlos y mostrar su procedencia sin instalarlos. La
importación inicial publicó 508 objetos activos y 22 archivados, 64 recursos y
69 alias. Después se reconstruyeron las doce piezas de maquinaria, se añadieron
tres skills de operación y se ajustaron las dos referencias operacionales de
consumidores descritas arriba. Las nueve dependencias hacia conocimiento de
maquinaria ya tienen destino activo. Las tres referencias históricas
incompatibles se mantienen como las excepciones concretas descritas arriba.

Las pruebas focales cubren reconstrucción exacta, lectura tras retirar el origen,
recursos y modos, identidad distinta con nombre igual, archivo sin instalación,
relaciones sin composición automática, rechazo de enlaces externos, exclusión de
estado privado, colisiones, cambio de fuente y recuperación ante fallo conservando
una edición concurrente. La tarea integradora ejecutó la migración real. El
relevo y las instalaciones tienen sus propias comprobaciones.

La auditoría independiente usa `provenance.source_path` para localizar cada
original. Prefiere `archive/previous` cuando existe una reconstrucción o
adaptación, verifica `source_sha256`, reconstruye encabezado y cuerpo según el
tipo y compara bytes y modos contra los archivos vivos. Examina aparte los
recursos, las 1.243 relaciones originales, los enlaces de lectura, los alias,
las referencias declaradas actuales y sus cierres de dependencias. No importa
`kora.migrate` ni usa sus conteos como prueba; el denominador se deriva de los
archivos de entrada. Las procedencias `artifacts/...` del complemento recuperado
desde `kora` quedan fuera del denominador de pneuma y se informan separadamente.

Desde la raíz del sucesor, usando el árbol legado preservado como argumento:

```bash
python3 scripts/audit_migration.py ._local/legacy-before-rebuild
python3 scripts/audit_migration.py ._local/legacy-before-rebuild --details ._local/migration-audit-nuevo.json
```

Antes del relevo, el argumento es el origen vivo; después del relevo debe ser su
árbol original preservado, sin confundir los enlaces del sucesor con los
originales. `--root` permite señalar otro sucesor. El informe detallado se crea
con modo `0600`, sin sobrescribir un informe existente y solamente dentro de
`ROOT/._local`. La API es `audit(source: Path, root: Path) -> (summary, details)`.
El CLI devuelve `0` sin diferencias, `1` cuando detecta diferencias y `2` si no
puede completar la comprobación. Vuelve a leer los archivos y revisar conjuntos
y enlaces al terminar; informa cambios concurrentes y nunca escribe los insumos.

El corte independiente del 2026-09-05 reconstruyó los 530 originales, incluidos
14 antecedentes, comparó los 64 recursos y verificó los 460 enlaces y los 69
alias esperados. No encontró diferencias de bytes o modos con el origen vivo,
referencias declaradas ausentes ni cambios durante la auditoría. Verificó además
los 87 hashes externos y la fuente categorial recuperada. La repetición tras
incorporar los 21 objetos complementarios de `kora` mantuvo esos resultados:
533 objetos activos, 21 archivados, 14 antecedentes de pneuma y 1.013
comprobaciones actuales de cierre por destino, sin referencias declaradas
ausentes. Los bytes de ese complemento tienen su comprobación propia; no se
suman artificialmente al denominador de pneuma. Se probaron doce
escenarios temporales que incluyen modificaciones de cuerpo, recursos, modo,
fuente viva, fuente externa, enlace, referencia, conjunto de archivos y edición
durante la auditoría; las diferencias fueron detectadas y la edición nueva se
conservó. Este corte verifica preservación material y resolución declarada; no
constituye una evaluación semántica del corpus ni una prueba de runtime.

## Preparación del relevo local

El plan exacto se deriva de ambos filesystems y de Git en
`._local/takeover-plan.json`. Contiene los paths, tipos, modos y hashes de los
archivos involucrados, HEAD, índice, estado de trabajo y worktrees registrados.
Es una preparación de solo lectura respecto de los dos árboles operacionales;
no aplica el relevo ni acredita que ya haya ocurrido. Antes de aplicarlo se deben
revalidar sus entradas: cualquier diferencia exige incorporar la edición y
preparar otra base, sin sobrescribirla.

El relevo conserva `.git` y su historia en el repositorio de destino. Los
originales reemplazados o retirados, incluidos los siete archivos no seguidos,
tienen una ubicación de recuperación propuesta bajo
`._local/legacy-before-rebuild`, fuera de la operación y de Git. El conocimiento
continúa accesible mediante los 460 enlaces de lectura hacia productos o
antecedentes conservados. Los agentes y skills originales ya están recuperables
en los productos migrados; sus ubicaciones antiguas dejan de ser una segunda
fuente editable.

`_archivo`, `.remember`, `.superpowers` y `.worktrees` permanecen en sus
ubicaciones. No se leen payloads personales ni se mueve estado privado por
limpieza. El `.gitignore` del sucesor debe excluir explícitamente esas cuatro
ubicaciones antes de revisar o preparar archivos para Git. `_archivo` contiene
antecedentes, incluido un `SKILL.md` histórico, y queda fuera de las rutas que
lee el catálogo nuevo. Los registros de worktrees se conservan; el plan no
cambia sus ramas, archivos ni estado.

La retirada operacional comprende `kora.py`, `ley/`, las entradas documentales
anteriores que ya tienen sucesor y sus pruebas. `_emision` y los bytecodes del
núcleo y pruebas anteriores se apartan a la recuperación privada. `_emision`
contiene instrucciones y perfiles generados para los cinco destinos anteriores;
no queda como árbol de trabajo activo. La revisión acotada de consumidores
encontró seis enlaces a conocimiento y ninguno a `_emision`. Las instalaciones
y servicios de runtimes retirados permanecen fuera del relevo.

## Relevo local realizado

El 2026-09-05 se ejecutó el relevo de 21 entradas superiores del repositorio,
después de ensayar su aplicación y reversión en una copia completa. La base
recuperable comprende el filesystem anterior y su Git. Los doce paths de trabajo
previo de Félix, incluidos siete sin seguimiento, quedaron primero en el commit
local `1899978`, sobre la historia existente. La construcción independiente
proviene del commit `fab5ec5` de `kora-rebuild`; los ajustes de entrada, uso y
comprobación final se integran en la raíz activa.

El intercambio conservó los objetos efectivamente desplazados en
`._local/legacy-before-rebuild`, con su diario de operación. `.git` permaneció
en su ubicación; el conocimiento conserva las 460 rutas de lectura. La raíz
activa contiene el núcleo nuevo y los productos; el núcleo anterior, su ley,
instrucciones reemplazadas y `_emision` quedaron fuera de esa superficie.

La auditoría desde la raíz relevada volvió a comparar los 530 originales, los
64 recursos, las 1.243 relaciones y los 69 alias contra el árbol capturado.
No encontró diferencias ni dependencias declaradas sin destino. Las tres
referencias históricas incompatibles conservan el tratamiento explícito descrito
arriba; no se presentan como referencias actuales resueltas.

El relevo nativo dejó 106 bundles y 300 archivos administrados entre Codex y
Hermes. Retiró 67 archivos anteriores con propiedad acreditada y comprobó 6.405
archivos protegidos. La misma operación completa pasó un ensayo de instalación,
rollback y reaplicación antes de ejecutarse en el home real. Los archivos
desplazados y el estado de recuperación permanecen fuera de Git.

Después de esa operación se adaptaron siete consumidores nativos manuales:
tres wrappers `salubrista-public-health-network`, tres variantes de `hodom-dt`
y el SOUL propio del perfil `hospitalista`. Se cambiaron solo rutas de fuente,
resolución de URNs y recetas de mantenimiento de KORA. Se conservaron sus 61
recursos; las sustituciones inversas reproducen cada archivo original completo.
Los originales efectivamente desplazados quedan en
`._local/clinical-consumer-update`. Estos wrappers continúan como fuentes nativas
editables; no se creó una segunda copia canónica de su contenido sanitario.

El antecedente del panel R01–R14 de `hd-hsc-os` no acreditaba una instalación
vigente: su directorio `.codex/agents` estaba vacío. Se corrigió la receta del
wrapper para distinguir ese antecedente y consultar los consumidores actuales.
No se recreó un panel sin uso demostrado ni se modificó el proyecto.

La conservación material del corpus, la carga nativa de los archivos y los
recorridos de inferencia tienen comprobaciones separadas. La revisión de
consumidores sanitarios no equivale a validar práctica clínica ni conducta de
cada agente de dominio. El estado actual se consulta con `kora_cli.py status`;
los cortes de este documento explican el relevo y no se mantienen como inventario.
