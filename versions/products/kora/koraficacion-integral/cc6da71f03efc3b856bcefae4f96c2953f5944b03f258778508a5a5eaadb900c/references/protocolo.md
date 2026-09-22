# Protocolo del recorrido integral

Este protocolo concreta el criterio de `koraficacion-integral`. `koraficacion`
conserva la entrada, procedencia y ciclo de biblioteca; aquí se transforma y
coteja el contenido. El helper `workflow.py` mantiene el trabajo y su historia,
pero no llama modelos, genera extracciones ni publica. El agente prepara
las representaciones, candidatas y revisiones con las herramientas disponibles.

La interfaz CLI vigente es la que sigue. No inventes opciones, campos ni
salidas. Los trabajos antiguos se rigen sólo por
[compatibilidad-integral-3.md](compatibilidad-integral-3.md).

## Contrato CLI

`init` recibe un trabajo privado, una o más fuentes originales (`--source`),
un cuerpo de borrador fuera del trabajo (`--body`) y `--scope`. Puede recibir
`--resource` repetido, `--require-independent` y `--independent-repairs`.
Congela los originales en el trabajo; no extrae ni altera el cuerpo. Un flujo
inicial típico es:

```sh
python3 scripts/workflow.py init --work PRIVATE \
  --source /ruta/original --body /ruta/borrador.md --scope 'alcance completo'
python3 scripts/workflow.py candidate --work PRIVATE --file /ruta/candidata.md
python3 scripts/workflow.py review --work PRIVATE --file /ruta/juicio.json
python3 scripts/workflow.py export --work PRIVATE
```

`candidate` instala una candidata completa como versión pendiente; si ya existe
una versión, exige `--base-revision ID`. `preview --file objetivo.md` devuelve
la revisión exacta y su diff sin mutar el trabajo. `status`, `next` y `recover`
consultan o reanudan; `export` sólo entrega una versión revisada y declara que
la publicación no se realizó.

El juicio de `review` es JSON sobre el objetivo exacto:

```json
{
  "revision": "REVISION_ACTUAL",
  "reviewer": "persona-o-contexto",
  "isolation": "separate_context",
  "authored_target": false,
  "scope": "full",
  "coverage": "complete",
  "result": "accepted",
  "evidence": "Cotejo completo de contenido y relaciones; regla repetida factorizada conservando sus excepciones.",
  "issues": [],
  "limits": []
}
```

`isolation` admite `author_context`, `separate_context` o `unknown`; `scope`
admite `full` o `changes`, y `coverage`, `complete` o `incomplete`. `accepted`
exige cobertura completa y `issues: []`; `repair` exige hallazgos; `limited`
exige un límite, hallazgo o cobertura incompleta. Una revisión `changes` añade
`basis` con la última revisión completa de la versión padre e `impact` con las
relaciones y el alcance cotejados. El helper valida su estructura y vinculación, no demuestra su verdad.
El ejemplo ilustra el esquema: evidence debe describir el cotejo realmente
ejecutado, nunca copiarse para fabricar una lectura.

Si se rectifica un hallazgo o límite sin cambiar la candidata, el nuevo juicio
`accepted` debe indicar `supersedes` (último review_id) y `resolution` con la
razón concreta. Se conservan ambos dictámenes; vaciar issues sin resolver el
dictamen previo no permite aceptar. Una corrección real del contenido pasa por
una nueva candidata o por `repair`, con su base y evidencia.

## Reparación sobre cambios

Aplica el criterio semántico de [koraficacion-integral](../content.md), incluida
la exclusión de metainformación desde los intermedios. El juicio `changes` debe
explicar cierre de hallazgos, relaciones afectadas y cualquier consumidor cuyo
texto permanezca idéntico. El helper no puede delimitar ese efecto por sí solo.

Una reparación se prepara con `preview` y se instala sólo sobre la base vigente:

```sh
python3 scripts/workflow.py preview --work PRIVATE --file /ruta/objetivo.md
python3 scripts/workflow.py repair --work PRIVATE --file /ruta/objetivo.md \
  --base-revision BASE --review /ruta/juicio-objetivo.json
```

El juicio de reparación debe ser `accepted` para esos bytes exactos. Una
aceptación condicionada es válida sólo si el revisor ya examinó el objetivo
completo, sus fuentes y dependencias; la coincidencia liga la decisión al
resultado y no crea una revisión nueva. Para `--independent-repairs`, quien
revisa el delta declara `separate_context` y `authored_target: false`. Si quien
repara escribió el delta, decláralo; no lo presentes como revisión independiente
de su propia corrección.

## Comparar economía cuando cambia la decisión

Reutiliza `measure` de la CLI KORA desde la raíz del repositorio, con el Python
que tenga `tiktoken` disponible; en este host, `.venv/bin/python`. Para dos
representaciones del mismo contenido:

```sh
.venv/bin/python kora_cli.py measure --source anterior.md --body propuesta.md \
  --encoding cl100k_base
```

Compara `total.source` y `total.candidate` sólo si `status` es `MEASURED`.
Incluye mediante `--auxiliary` y `--wrapper` el texto adicional que requiere
la propuesta; si la base también depende de otros textos, repite `--source`.
Usa la misma codificación en ambas alternativas: si no corresponde al modelo
destinatario, informa el conteo como referencia, no como su consumo exacto.
`NOT_MEASURED` no se reemplaza por una estimación de caracteres como tokens.
El conteo no decide equivalencia: primero descarta pérdidas y luego elige la
representación económica y legible. Compara cuerpos de igual alcance sin
metainformación; no inventaríes ni cuentes lo excluido como información ganada.
Registra sólo la conclusión útil en `evidence` del juicio existente. No cambian
el esquema de revisión ni los trabajos anteriores; no crees otro informe.

## Continuidad y límites

El helper conserva snapshots, revisiones, recursos, bases e historia; rechaza
insumos obsoletos o ediciones concurrentes sin destruir el trabajo y permite
reanudar una transición interrumpida. Repetir la misma transición no duplica su
historia. Estas defensas mecánicas no juzgan fidelidad ni autorizan publicación.
La exclusión mutua cubre procesos que usan el mismo trabajo. Cada cuerpo tiene
un solo trabajo propietario; una edición externa detectada detiene la operación.
La comprobación previa al reemplazo no es un bloqueo compartido con editores
externos que ignoran este protocolo.

Entrega a `koraficacion` la candidata, recursos, procedencia, alcance,
revisión, reparaciones, hallazgos y límites. Distingue compresión del contenido
de retiro de soporte. Cotejar economía es parte de la revisión; medir es
opcional cuando no cambia la decisión. No hay porcentaje, ahorro mínimo ni
segunda alternativa obligatoria; `NO_GAIN` permite conservar una representación
ya económica sin inventar una ganancia ni exigir otra alternativa. La publicación sigue el ciclo de
biblioteca y su autoridad.

El cuerpo de `--body` pertenece al borrador de biblioteca; la entrada de
`--file` es una propuesta temporal, no otra candidata vigente. Después de
`init` no edites directamente el destino. Las fuentes admiten binarios y se
conservan por bytes en `objects/`; el texto de candidata requiere UTF-8. Los
recursos de `--resource` se congelan por versión y sus paths vigentes se
comprueban antes de aceptar o exportar. `candidate` registra una nueva versión
cuando cambia un recurso. Un cambio del original externo no modifica la copia
histórica congelada; verifica el alcance vigente antes de reutilizarla.

`--require-independent` exige separación real del autor. Un revisor que
escribió el delta (`authored_target: true`) sólo hereda el cotejo separado
inicial mediante `changes` y `basis`; esa intervención se declara. Con
`--independent-repairs` tampoco se admite esa herencia. Una aceptación declarada
sin la separación exigida conserva estado `limited` y no permite `export`.

`export` imprime el recibo derivado con fuentes, hashes, revisiones e historia;
no lo copies al cuerpo de conocimiento. Conserva el trabajo y sus snapshots
mientras sustenten la revisión. Registra sólo el recibo auxiliar que tenga
consumidor. Si una escritura se interrumpe, `recover` completa la misma versión
si sus precondiciones siguen vigentes; una edición ajena detiene la recuperación.
