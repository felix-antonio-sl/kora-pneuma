# Productos KORA: estado y dirección

Fecha de corte: 2026-09-14. Fuente gobernante: encargo de Félix de fijar y
publicar una línea de estado, repensar la reconstrucción y proponer su ejecución
con `steipete` y `cat-thinking`, para un usuario y desarrollador en un host.
La [especificación confirmada](kora-version-oro.md) conserva los requisitos;
la [guía](operacion.md), la operación; este documento reúne el corte y el plan
de productos. La [propuesta anterior](propuesta-refactorizacion-productos.md)
conserva diagnóstico y evidencias por lote, sin gobernar el siguiente paso.

## Línea de estado publicada

**Contratos reconstruidos y admitidos, maquinaria comprobada, instalaciones
personales coherentes, cuatro reparaciones de Diseño admitidas por ciclos KORA
completos, transformación integral demostrada en instancia sintética con
medición completa y cobertura viva por promesa y superficie con un vacío
declarado; conformidad parcial en seis agentes sin sesión en este ciclo.**
Tres veredictos distintos sin contradicción: (a) cierre técnico de lo
ejecutado —defectos materiales resueltos, instalaciones coherentes,
publicación cerrada—; (b) conformidad parcial del alcance —lo no evaluado
conserva ese estatus y no se suma a la mejora—; (c) aceptación personal
recibida como incremento válido con conformidad parcial el 2026-09-14, con la
aceptación final del plan pendiente de Félix. No corresponde declarar
terminada la misión: lo pendiente conserva ese estatus.

El corte de fuentes es `49d9292` en pneuma/master y `9af3696` en
knowledge/main. Los commits `2e225cd` y `49d9292` admiten la evidencia
proporcional en `diseno-producto-integrado` (revisión `21e671cb`) y la
tricotomía estática/ejecución/corroboración en `director-diseno-producto`
(revisión `63058f56`); no cambian el resto de las fuentes activas. Las historias
conservadas por `f827636` y `03d4a5f` siguen disponibles sin cambios.

| Parte | Hecho comprobado o antecedente identificado | Límite / pendiente |
|---|---|---|
| Colección | 61 fuentes activas: 16 agentes y 45 skills. 58 declaran ambos destinos; 3 sólo Codex. | Cantidad descriptiva, sin cuota de reducción. `codex-route` se conserva; los otros 60 están integrados en lotes de reconstrucción. |
| Lotes | KORA operativo, ingeniería, salud, GTD general, compatibilidad, organización, especialidades de proyecto, modelado y Diseño están admitidos y confirmados en Git. Diseño suma cuatro reparaciones admitidas (`5dd3e3b`, `c5336b1`, `2e225cd`, `49d9292`). | Admisión y documentación de ensayos no equivalen a utilidad general demostrada; los recorridos de este corte cubren sus casos, no todo el corpus. |
| Maquinaria | `check`: 523 activos, 18 archivados, 0 incidencias. Suite ejecutada en este corte: 251 pruebas, OK. | No acredita fidelidad de toda la biblioteca, carga de todos los cuerpos o utilidad. |
| Codex personal | 61 instancias gestionadas en alcance: fuente y dependencias `current`, incluida la reparación de Diseño instalada. | Estado material más sesiones vivas de este corte (retoma, rutas de Diseño, gemelos, niveles, OPM, autoría, claridad); no equivale a conducta futura. |
| Hermes personal | 62 instancias en alcance `current` (58 productos y 4 instancias adicionales de skills en perfiles); `gtd-felix` ausente excluido por encargo. Sin cambios nativos ni recuperación pendiente. | Carga verificada por instalación, render y presupuestos SOUL 16/16; uso vivo sólo por canario sintético. La cifra anterior de 33 pendientes queda reconciliada. |
| Conservación | Se incorporan candidatas admitidas y 12 versiones de los seis productos GTD/compatibilidad. Candidata, fuente activa y revisión registrada coinciden en los seis. | Se verificaron estas versiones con el verificador nativo; no se auditó toda la historia ni se atribuye aprobación nueva. |
| Biblioteca | Sigue en `9af3696`; incluye cuatro referencias Jobs publicadas y revisiones anteriores conservadas. | El corpus general heredado conserva su estatus. No se declara reconstruido, íntegramente revisado ni optimizado en tokens. |
| Git | El corte de fuentes estaba publicado y en paridad 0/0 tras fetch. La línea de estado y conservación se publica con este incremento. | Los cambios locales archivados OpenClaw y material privado en knowledge quedan fuera; `.hermes/` local se conserva. Paridad Git no implica igualdad del workspace completo con el remoto. |

Las seis historias son `fxsl/{david-allen,gtd-flow,memorizacion-espaciada}`,
`dev/agent-architect` y `kora/{autoria-de-persona,auditoria-exposicion-kora}`.
Se conservaron `product`, `state.yaml` y las versiones publicables. Los
directorios `displaced-*` permanecen locales e ignorados según la política
existente; no son una fuente operativa nueva.

### Qué evidencia tiene cada afirmación

| Dimensión | Estado defendible |
|---|---|
| Integridad mecánica | PASS en el catálogo actual y 251 pruebas de maquinaria; verificación focal de las 12 versiones preservadas. |
| Fidelidad semántica | Revisiones y correcciones documentadas por lote. Hay tensiones focales aún examinables; no se releyeron todos los cuerpos para este corte. |
| Carga nativa | Sesiones vivas de este corte en Codex (activación directa de skills) más presupuestos SOUL Hermes 16/16 completos con mapas intactos y una sesión viva del director en Hermes con instalación temporal desde fuente. KORA mediante skill directa Codex y SOUL Hermes; rol personalizado KORA no acreditado en su campaña. Dori Codex sólo lectura parcial observada; Hermes con margen estrecho bajo Sol/272K. |
| Conducta | Casos sintéticos de los lotes más sesiones vivas de este corte: retomas del gate reparado (3, incluida tricotomía con ejecución real observada), rutas de Diseño A/B, gemelos (3 con retoma), niveles micro/meso/macro (3), OPM experto y vecino (2), agent-architect (1), claridad agente/método (2) y director en Hermes (carga PASS; juicio conductual neutro abajo). Sin actos clínicos, institucionales ni envíos. La evaluación técnica de estas sesiones es juicio del ejecutor (Codex como integrador incluido) y no constituye aceptación personal de Félix. |
| Utilidad | Cuatro reparaciones admitidas por defectos demostrados; evidencia proporcional flexibilizada por tarea (una afirmación admite cita directa; el packet de la ruta A conserva su valor por decisión, rechazos y deuda, no por existir); gemelos con métodos propietarios cargados y aplicados; comparación director+método frente a método directo (empate funcional, aporte en trazabilidad, costo ~2x/1,7x); david-allen frente a gtd-flow inconclusa (se conserva sin afirmar ventaja). Transformación integral: instancia sintética con medición completa (o200k_base, tiktoken 0.14.0 en venv temporal). Fallo v3 conservado como evidencia: “mismo criterio si ese jueves es festivo” desanclaba “hábil inmediato anterior” del jueves y habilitó inferir miércoles (lectura R3b); no se clasificó como mera inferencia del lector. Reparación v4 desde la fuente sin resolver ni ampliar: criterio con ancla al jueves + marca “la fuente no ejemplifica el caso de jueves festivo”. Re-cotejo (excepción y relaciones intactas), re-medición (138 → 110 → 87 tokens; contenido −20,91 %, total −36,96 %, artefacto `a66a284e`) y lectura independiente R-v4 sobre el texto final exacto: q01–q04 correctas, q05 correctamente indeterminada sin día inventado; la tensión excepción/negación (día del operador en festivo) es de la fuente, se conserva sin resolver y no es defecto. Control negativo PASSED conservado (no depende del cambio). No valida el procedimiento en general ni la publicación sintética equivale a validación. |
| Efectos | Fuentes admitidas y publicadas (`5dd3e3b`, `c5336b1`, `2e225cd`, `49d9292`); instalaciones personales coherentes en ambos destinos (Codex 61, Hermes 62 en alcance). Conocimiento sintético de prueba en biblioteca temporal, nunca en la personal. |

La cobertura se apoya en los dictámenes por lote de la propuesta anterior y en
la ejecución mecánica de este corte. Los recibos temporales son evidencia
auxiliar: antes de reutilizar una afirmación decisiva se comprueba que existan y
correspondan al caso, revisiones y entorno. Si faltan, se declara la limitación;
no se reconstruyen logs ni se repiten campañas enteras para llenar un archivo.

### Cobertura por promesa y superficie (2026-09-14)

`PASS`/`FAIL` observados; `PRIOR` reutiliza el lote admitido sin repetirlo;
`NOT_RUN` conserva estatus sin sumarse a la mejora. Superficies: `CX-D`
skill directa Codex, `CX-R` rol TOML Codex, `H-P` perfil Hermes, `H-S`
skill Hermes.

| Promesa y producto | CX-D | CX-R | H-P | H-S | Base |
|---|---|---|---|---|---|
| Gate de evidencia reparado (skill+método) | PASS (3 sesiones) | — | — | PASS (skill_view + JSON exacto) | Instalación + render ambos |
| Director reparado (tricotomía) | PASS (2 sesiones) | Instalado, invocación no ejercida | Carga PASS; formato PASS; juicio conductual neutro FAIL acotado (1 sesión, ver nota) | — | soul-budgets 16/16 |
| Gemelos + métodos propietarios | PASS (3 sesiones, retoma incluida) | — | Instalado | Instalado | Lote salud + soul-budgets |
| Niveles micro/meso/macro | PASS (3 sesiones) | — | Instalado | Instalado | Lote salud |
| OPM experto + vecino | PASS (2 sesiones) | — | Instalado | Instalado | Lote modelado |
| agent-architect, david-allen, gtd-flow | PASS (3 sesiones; agente/método inconclusa) | — | Instalado | Instalado | Lotes respectivos |
| `steve-jobs`, `ux-research-design-ai`, `allan-kelly`, `dov-dori`, agente `kora` | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | PRIOR (lotes admitidos) |
| `fugaz` | NOT_RUN (frontera: delegación sólo Codex, OpenCode retiene) | PRIOR | Instalado | Instalado | Fuente + lote ingeniería |
| Transformación integral (instancia sintética) | PASS (helper + lectura R1 5/5 + control PASSED + medición; v3 fallida y reparada, R-v4 sobre texto final) | — | PRIOR (sesión 09-13: helper + publicación ficticia) | — | Tests + recibo `a66a284e` |

Un canario genérico o un SOUL admisible no se usan como conducta de otro
producto. La conformidad formal Hermes del director con prompt prescriptivo
(JSON exacto) vale como carga + conformidad, no como prueba conductual pura.

Diagnóstico corregido del caso neutro (sustituye al impedimento declarado
antes, que se conserva aquí como fallo del ejecutor): sí hubo respuestas JSON
parseadas en los 3 intentos neutros —lo prueban sus `unexpected_answer_fields`
(`hermes-neutro3.json`: 4 campos; `hermes-neutro4.json` y
`hermes-neutro-max.json`: 6 campos)—, pero sus valores se perdieron con los
homes temporales y el recibo sólo proyecta `answer` a las claves del
`expected-file` (que contenía sólo `_nota`): de ahí `{"_nota": null}`. El
fallo fue triple y mío: leí `.get('final_response')` ausente como respuesta
ausente sin comprobar las claves del recibo, ignoré `unexpected_answer_fields`
presentes desde el primer recibo y declaré impedimento del harness sin causa
observable. El impedimento estaba en el contrato y la salida del comprobador
(`scripts/probe_hermes.py`, líneas 1214–1229), no demostrado en Hermes.

Repetición neutra única con proyección corregida (mismo prompt, `sol/high`,
`expected` con las 6 claves en nulo —el modelo nunca lo ve—): disponibilidad
PASS, formato PASS (JSON con las 6 claves). Juicio post-hoc contra el criterio
fijado antes de ejecutar —(i) sin citas colgadas y verificado trazable; (ii)
`huso_v` distinto de verificado con alcance externo—: (i) PASS (sin `[E#]`,
fuente literal identificada); (ii) FAIL (`huso_v` = verificado sobre uso real
sin corroboración, aunque el fundamento niega esa corroboración). Conducta:
FAIL acotado a 1 sesión en rincón sólo-literal. La cláusula `SPEC_ONLY` ya
excluye hechos del mundo como adopción del verificado, así que no hay cambio
de texto: es no-conformidad conductual estrecha (etiqueta/alcance), no laguna
del producto ni refutación de la evidencia Codex (tareas distintas, ejecución
real). Futuros casos neutros deben fijar la lectura mundo/enunciado sin
filtrar reglas.

Caso único de uso para cerrar la duda sobre atribución (ficha pública de un
módulo ficticio, criterio prefijado por escrito antes de ejecutar, sin
clasificaciones ni respuestas indicadas): PASS en los cinco puntos —“40
equipos”, “a la mitad” y “99,9 %” atribuidos al proveedor sin elevarlos;
versión publicada 2.3.1 (observada) con la discrepancia del brief señalada;
capacidades con evidencia citada; `run-check.sh` ejecutado de verdad con su
límite declarado (sólo `echo`); log del proveedor atribuido sin apropiación.
La discrepancia del neutro5 se conserva como historia de otro rincón
sólo-literal; este caso no la convierte retrospectivamente en PASS ni cambia
el producto, y no hay más rondas de variantes.

### Registro durable mínimo del caso integral

Fuente sintética (sha256 `02747567…a7cd9430`): regla viernes hábil semanal;
negación en festivos; condición viernes festivo → jueves hábil anterior;
excepción con prevalencia del operador; tabla A 72 h sin frío, B 24 h sin
frío, C 12 h con frío. Procedimiento `koraficacion-integral` con helper
(`init/next/submit/reopen/build`, encoding `o200k_base`): inventario de 5
unidades y 5 preguntas, revisión `same_context`, reapertura por dos pérdidas
genuinas halladas en cotejo (`de entrega`, ausencia overstated), bloqueo
`TOKEN_REGRESSION` resuelto con representación densa, revisión global con
control negativo `PASSED` (alteración jueves→miércoles detectada con efecto).
Artefacto final v4 (sha256 `a66a284e…5aaf`): cuatro frases con el criterio
anclado al jueves y el borde marcado como no ejemplificado, sin regla añadida
ni cómputo invitado. Medición: 138 → 110 → 87 tokens; contenido −20,91 %,
total −36,96 %. Lectura independiente R1 5/5 sobre v1; R-v4 sobre el texto
final exacto: q01–q04 correctas, q05 indeterminada sin día inventado; la
interacción excepción/negación es tensión de la fuente y se conserva sin
resolver. El fallo v3 (artefacto `226ee3c7`, “mismo criterio”, lectura R3b con
miércoles) queda conservado en el historial del helper y aquí como evidencia
del defecto y su reparación. Esto acredita la instancia, no el procedimiento
en general.

### Reproducir y mantener el corte

Usar `python3 kora_cli.py check`, `python3 -m unittest discover -s tests -v`
y `git diff --check`. Derivar productos desde `products/*/*/object.yaml`,
seleccionar sus identidades con `status --compare-source --id URN` repetible,
excluyendo `gtd-felix` y `gtd-operations`, y resumir `source_comparison` por
destino, perfil y estado. Las instancias adicionales son `ship-discipline` y
`hermes-agent-specialist` en los perfiles `hospitalista` y `urgencia`.
No publicar recibos completos del home, credenciales o respaldos privados.

Esta tabla es un **corte fechado**, no un inventario manual que deba acompañar
cada instalación. El estado vivo se deriva por CLI. Sólo se actualiza el
dictamen cuando cambie una conclusión material; Git conserva el corte anterior.

## Decisiones del corte

1. Conservar la colección admitida y su historia como punto de partida.
2. Corregir la declaración prematura de cierre. Instalación actualizada,
   conducta acotada y utilidad comparada son afirmaciones diferentes.
3. Mantener el núcleo, la biblioteca separada, las fuentes agnósticas y los dos
   adaptadores. No hay evidencia que justifique una nueva plataforma.
4. La reconciliación personal era el primer incremento del plan posterior;
   quedó ejecutada el 2026-09-14 sin reinstalación ciega (planes dry-run por
   destino, 66 actualizaciones Hermes, cero conflictos, protegidos intactos).
5. `gtd-felix`/`gtd-operations`, sus dependencias protegidas, los espacios
   institucionales y los datos privados conservan las exclusiones del encargo.
   Un solo usuario no elimina errores, interrupciones o procesos concurrentes;
   sí elimina la necesidad de diseñar tenants, roles empresariales o servicios
   de coordinación sin consumidor.
6. Forma final 2026-09-14: ninguna fusión, simplificación o retiro justificado
   por los resultados; las separaciones ejercidas (gemelos, niveles, director /
   método, agentes de claridad) mostraron diferencias o quedaron inconclusas y
   se conservan provisionalmente sin afirmar ventajas no medidas. Sin alias
   nuevos: un alias no probaría invocación nativa. Lectura pendiente menor y
   documentada: `director-diseno-producto` §Salida mínima item 8 admite
   "EVIDENCE_LEDGER" como sección de evidencia numerada inline, según el gate
   reparado; se reabre sólo ante divergencia observada.

## Estado al que queremos llegar

Félix puede entregar una fuente, un problema o un compromiso a KORA, escoger una
ruta comprensible y obtener un resultado utilizable con menos corrección y
coordinación manual, manteniendo profundidad, autoridad y continuidad. Puede
mejorar un producto y usar la nueva revisión en Codex o Hermes sin perseguir
copias, perder recursos ni reconstruir la conversación anterior.

El resultado incluye tres promesas diferentes:

- **Conocimiento:** transformación íntegra del contenido definido por KOR-01,
  con procedencia y mínima expresión practicable medida junto con los recursos
  necesarios. No basta resumir ni medir sólo el cuerpo corto.
- **Agentes y skills:** responsabilidad o tarea reconocible, conocimiento
  oportuno y conducta que complete trabajo autorizado. El agente debe justificar
  su aporte frente al método directo o una instrucción breve; una especialidad
  puede conservarse sin necesidad de convertirla en un agente.
- **Realización:** lo necesario llega y se usa en la superficie prometida;
  actualizar y recuperar sigue siendo una operación local comprensible.

Se conserva el alcance de productos y conocimientos necesarios para sus
recorridos. Renovar toda la biblioteca heredada sería otro encargo. El límite se
explicita por capacidad: conservar un conocimiento `legacy` no lo hace inválido,
pero tampoco acredita una revisión editorial nueva o economía óptima de tokens.

La renovación editorial fue selectiva: referencias operacionales KORA, cierre
de ingeniería, conocimiento sanitario y lentes Jobs. El cierre de este plan no
debe presentarse como renovación integral de la biblioteca. Tampoco se excluye
de revisión un conocimiento necesario sólo porque sea heredado: cada recorrido
debe examinar el contenido que sustenta sus decisiones, no únicamente comprobar
que su URN resuelve. Se prioriza lo que determina una acción, presenta una
contradicción o ha quedado desactualizado; se conserva lo suficiente y se
recompone lo defectuoso mediante el ciclo editorial existente. El dictamen
identifica las referencias revisadas y los límites del resto, sin inventario
paralelo ni promoción masiva de `legacy`.

## Descomposición estructural con cat-thinking

La pregunta reformulada es: **¿qué debe conservar cada transformación y qué
conexiones necesitan evidencia para que una intención llegue a un resultado?**
La lectura suficiente es un modelo de relaciones tipadas (`M`) y criterios de
ingeniería (`H`), contrastados con observaciones (`E`). No se construye aquí una
categoría formal, ni se afirma functorialidad, bisimulación o equivalencia entre
LLM. El vocabulario no reemplaza pruebas de uso.

```mermaid
flowchart LR
    N["Necesidad de Félix"] --> C["Contrato de resultado"]
    C --> P["Producto: agente o skill"]
    K["Conocimiento y recursos"] --> P
    P --> A["Adaptador Codex / Hermes"]
    A --> I["Instalación gestionada"]
    I --> U["Carga y ejecución"]
    U --> R["Resultado y continuidad"]
    C -. "criterio de aceptación" .-> R
    R -. "defecto o mejora observada" .-> P
```

Cada flecha del dibujo identifica una dependencia o transformación que hay que
examinar; no representa automáticamente un morfismo demostrado. La ruta inferior
de comparación entre contrato y resultado es la que falta cerrar en varias
familias. Fuente correcta y archivos actuales sólo cubren tramos intermedios.

| Relación y clase | Qué tenemos | Qué falta / decisión |
|---|---|---|
| Necesidad → responsabilidad → producto (`M/H`) | 16 agentes y 45 métodos/accesos con contratos explícitos. | Contrastar si la separación ayuda a Félix. No decidir por nombre, prestigio, tamaño o cuota. |
| Fuente → versión revisada (`E/H`) | Candidatas, revisión concreta, procedencia, admisión y versiones; correcciones semánticas documentadas. | En cada cambio nuevo, cotejar también recursos y referencias que puedan reintroducir el defecto. Preservar contenido no exige conservar cada duplicación prescriptiva. |
| Producto + dependencias → realización (`E/M`) | Cierre de `requires`, recursos seleccionados y adaptadores. | Una condición escrita no es un dispatcher; `relations` no ejecuta llamadas. Probar la conexión realmente usada y su autoridad. |
| Realización → instalación (`E`) | Propiedad, planes, recuperación y comparación de fuentes funcionan en la suite; 33 instancias Hermes cambiadas. | Reconciliar el conjunto afectado sin tocar consumidores protegidos. |
| Instalación → conducta (`E/H`) | Sesiones sintéticas por lotes; límites de rol y contexto identificados. | No transferir evidencia de skill directa a rol delegado ni de lectura parcial a especialidad completa. Probar el tramo positivo ausente. |
| Conducta → utilidad y continuidad (`M/H`) | Criterios EVA existentes y casos parciales. | Comparar resultado, retrabajo, errores y costo; retomar asuntos desde su dueño en sesiones nuevas. |

Trazabilidad de las conclusiones estructurales:

- Identidad, dependencia y realización: `urn:kora:kb:cat-kora-kernel`,
  secciones «Actividad e identidad» y «Dependencias y realización».
- Preservación y pérdidas al traducir (`H`): `urn:fxsl:kb:icas-preservacion`,
  «El patrón que aparece en todas partes». No se traslada su definición formal
  de funtor a estos adaptadores sin construir las estructuras y probar leyes.
- Instalación, efecto y recuperación (`E/H`):
  `urn:kora:kb:cat-kora-semantica-operacional`, «Fuente, realización e instalación»
  y «Transacción y recuperación»; la evidencia de este corte está arriba.
- Separación Spec/Model/Runtime (`M/H`):
  `urn:kora:kb:cat-programacion-agentica-autonoma`, §4.4–4.5. La comparación
  conducta/contrato exige un testigo propio, no paridad de archivos.
- Agente, método y evidencia proporcional (`H`):
  `urn:kora:kb:cat-contrato-ingenieria-agentica`, «Elegir y expresar el producto»
  y «Evidencia según la afirmación».

Coherencia de esta aplicación: distingue identidades de sus versiones, consulta
de ejecución, aprobación editorial de autoridad institucional y publicación de
instalación. No postula leyes formales ni promueve la delegación dinámica
retirada de la monografía. Las observaciones pertenecen a su runtime y revisión;
las decisiones de arquitectura son hipótesis contrastables, no teoremas.

### Alternativas y decisión

| Alternativa | Beneficio | Costo o pérdida | Decisión |
|---|---|---|---|
| Reescribir todo con una arquitectura nueva | Uniformidad aparente. | Descarta aprendizaje, mueve demasiadas variables y posterga el uso sin evidencia de necesidad. | Descartada para este encargo. |
| Declarar terminado tras instalación y tests | Cierre rápido de la maquinaria. | Omite el aporte del producto y confunde artefactos con resultados. | Insuficiente. |
| Reducir de inmediato a una colección mínima por número | Menos entradas. | Puede destruir profundidad, disparadores y acceso directo aún no comparados. | Descartada como criterio. |
| Conservar la base y mejorar por recorridos completos | Reutiliza evidencia y hace observable el valor de cada cambio. | Requiere escoger casos y aceptar resultados inconclusos sin inventar éxito. | Elegida. |

## Plan de implementación

La unidad de trabajo es un resultado completo con sus dependencias. Los
incrementos siguientes conservan una sola dirección e integración; escrituras
compartidas se serializan. No se abren agentes, ramas, tableros o documentos por
fase automáticamente. El plan es propuesto para ejecución posterior a este
corte; su publicación no significa que se hayan realizado estas mejoras.

### 1. Dejar consistente el uso personal

**Cambio:** derivar nuevamente las instancias gestionadas cambiadas, preparar
planes por destino y consumidor, inspeccionar efectos y actualizar las
seleccionadas. Incluir las instancias de skills en perfiles existentes; no sólo
las instalaciones raíz. Preservar ediciones locales, versiones y recuperación.

**Propiedad:** operación del instalador existente; `kora/install.py` y sus tests
sólo si un defecto reproducido impide la operación. No cambiar configuración
global ni actualizar Hermes/Codex por rutina. Las 33 diferencias del corte son
un punto de partida, no una lista fija que prevalezca sobre el estado real.

Separar diferencias de realización de defectos de contenido: el cambio de
envoltura Hermes de `3e52279` explica actualizaciones pendientes sin implicar
que cada cuerpo esté roto. Contrastar los efectos actuales antes de atribuirles
esa causa. Una diferencia sólo de envoltura no justifica reautoría del producto
ni una campaña conductual por instancia; sí exige conservar rutas, condiciones,
recursos y carga efectiva donde el cambio pueda afectarlos.

**Aceptación:** todas las instancias en alcance seleccionadas y sus consumidores
materiales quedan `current`, sin recuperación pendiente, o con conflicto
protegido concreto aislado. Contrastar el ensamblaje afectado; el tamaño de
Dori se evalúa respecto del contexto efectivo, sin recortar contenido para
obtener verde. Reutilizar evidencia nativa compatible y repetir sólo el tramo
que cambió materialmente. No confundir este resultado con utilidad.

### 2. Cerrar un ciclo útil de KORA sobre sus propios productos

**Cambio:** usar KORA para llevar una reparación real y acotada del incremento
3 desde el problema hasta candidata, revisión, admisión, instalación y uso en
una sesión nueva. Añadir un caso de transformación de una fuente pública o
sintética con negación, condición, excepción y contenido estructurado: conservar
el original, producir conocimiento consultable y comprobar comprensión y costo
completo. Un caso sintético no se publica en la biblioteca personal por rutina.

**Propiedad:** `products/kora/{kora,autoria-kora,koraficacion,
koraficacion-integral,auditoria-artefactos-kora,instalacion-kora}` y sólo los
recursos/referencias necesarios para un defecto observado. Cambios desde sus
candidatas; el conocimiento publicado usa su ciclo editorial, nunca edición
directa de versiones. El objetivo no es reescribir los seis.

**Aceptación:** el cambio llega al consumidor con su semántica conservada y una
retoma que reconoce la revisión nueva. El conocimiento mantiene la información
y el resultado de consultas discriminantes; tokens totales medidos cuando
exista contador compatible, o `NOT_MEASURED` con la afirmación de economía aún
pendiente. Contrastar la ruta KORA con el método directo donde decida su aporte.
Se reutiliza la prueba de recuperación de maquinaria salvo que el cambio la
afecte. Este incremento y el siguiente pueden compartir el mismo caso y recibo.

### 3. Conseguir una entrega positiva de Diseño sin trámites superfluos

**Cambio:** encargo pequeño y completo con contexto suficiente, por ejemplo
mejorar una página local de ayuda de KORA en un fixture temporal. Debe producir
un artefacto funcional inspeccionable y una comprobación real. Comparar la ruta
director + método con método directo; usar asistencia sin producto cuando sea
necesaria para decidir el aporte. Misma tarea, materiales y herramientas, en
sesiones nuevas y sin revelar criterios esperados como respuestas.

**Propiedad:** las siete fuentes de Diseño y sus dependencias afectadas.
Inspección focal inicial: `diseno-producto-integrado` combina ledger opcional
con exigencia universal de `[E#]` y paquete de ocho secciones;
`director-diseno-producto` admite pruebas sobre artefactos propios y exige luego
una fuente independiente de su propia salida. Son tensiones textuales, todavía
no fallos runtime observados. Resolver la ambigüedad distinguiendo el artefacto
generado de la prueba ejecutada sobre él y haciendo proporcional la entrega.

**Aceptación:** produce una mejora utilizable y comprueba lo que afirma, conserva
recuperación y accesibilidad necesarias, no inventa investigación y no exige
documentos sin función. Se observa tanto el recorrido positivo como la excepción
afectada. `SPEC_ONLY` sigue siendo válido cuando ése sea el encargo; no sustituye
este caso materializado. Conservar, simplificar o combinar entradas según
resultado y carga real, preservando acceso a investigación y crítica.

### 4. Comprobar continuidad y profundidad donde cambian el resultado

Los frentes siguientes se realizan según dependencia y utilidad, aprovechando
el trabajo de los incrementos anteriores. No son campañas por archivo.

| Frente y fuentes principales | Caso que falta discriminar | Criterio de salida |
|---|---|---|
| DT HODOM y Telemedicina, con sus métodos propietarios | Asunto sintético con decisión autorizada, compromiso con dueño, cambio posterior y retoma en otra sesión desde el mismo cuaderno. | Conserva el cargo y la decisión vigente, realiza la contribución autorizada y mantiene continuidad sin libreta paralela. Probar la diferencia de responsabilidad del segundo gemelo; sin actos institucionales reales. |
| Medicina hospitalaria, urgencia y salud pública | Mismo problema sintético visto desde las responsabilidades respectivas, con fuentes públicas suficientes. | Cada producto conserva el nivel micro/meso/macro y entrega el resultado propio sin invadir autoridad; reutiliza los casos sanitarios previos y añade sólo la diferencia faltante. No acredita eficacia clínica. |
| Dori y OPM, con métodos y recursos expertos | Consulta técnica que necesite contenido sustantivo o tardío y un recurso especializado, más el caso vecino que no necesita OPM. | Acceso efectivo al conocimiento decisivo, resultado técnico contrastable y proporcionalidad. Separar corrección formal, premisa de dominio y ejecución de herramienta; no prometer roundtrip no ejecutado. |
| Steipete, Fugaz y acceso agent-architect | Reparación y comprobación real del propio ciclo KORA; autoría por acceso especializado frente al método directo. | Trabajo integrado, conservación de autoridad y cierre sobre candidato correcto. No duplicar los ensayos de los incrementos 2–3. |
| David Allen, Allan Kelly y métodos de claridad/organización | Compromiso personal o célula sintética con responsabilidades cruzadas y una decisión pendiente concreta. | Claridad y siguiente acción útiles, sin apropiarse del trabajo ajeno ni imponer registros. Comparar acceso agente con método suficiente; GTD protegido excluido. |

En los gemelos, elegir un caso que requiera realmente
`conducir-decisiones-hodom` y `conducir-telemedicina-hsc`, respectivamente, y
observar su carga y aplicación, además de la conducta del agente. Los ensayos
sanitarios previos no acreditan por sí solos esas dos skills: el recibo agregado
declara cobertura por casos, no ejercicio individual de todos los productos.
La evaluación histórica aportada por Félix señala que los casos de los gemelos
no exigieron cargar esos métodos; antes de reutilizar esa evidencia, comprobar
las trazas pertinentes. Resolver esta brecha dentro del recorrido de continuidad,
sin dos campañas adicionales por archivo.

La retoma debe reconocer una decisión posterior desde el mismo asunto y
preservar la separación de autoridades de ambos cargos. Instalar un perfil no
crea memoria persistente ni seguimiento autónomo. No añadir un servicio de
seguimiento para hacer pasar un caso de continuidad entre sesiones.

**Cobertura:** los frentes, junto con KORA y Diseño, incluyen las 16 identidades
de agente activas. No exigen 16 campañas aisladas: se reutiliza evidencia sólo
cuando la responsabilidad, el caso y la configuración la hagan aplicable.
Cada promesa distinta de una skill debe estar cubierta por un recorrido propio
o evidencia previa pertinente. Si permanece sin evaluar, conserva ese estatus;
no puede sumarse a una afirmación de mejora completa.

### 5. Decidir la forma final y comprobar ambos destinos

**Cambio:** con los resultados anteriores, resolver cada duplicación o
especialización que cambie una ruta de uso. Agente para responsabilidad y juicio
persistentes; skill para procedimiento reutilizable; conocimiento para contenido
consultable con valor propio. Una relación documental no crea orquestación.
Evitar prólogos y reglas generales duplicadas cuando no aporten conducta.

**Propiedad:** sólo productos, recursos, referencias y consumidores afectados
por la decisión. Una fusión o retiro exige mapa concreto de capacidad conservada,
acceso alternativo comprobado, versiones disponibles y reconciliación de
consumidores. Un alias en el catálogo no prueba invocación nativa equivalente.

**Aceptación:** cada agente del alcance tiene una razón de conservación,
recomposición o retiro sustentada en evidencia proporcional. Si una comparación
es inconclusa, se conserva provisionalmente sin afirmar ventaja; se limita
explícitamente la promesa y queda pendiente la decisión necesaria. Las rutas
prometidas funcionan en ambos runtimes declarados, con superficie efectiva
identificada (skill directa, rol invocado o perfil). No hay matriz universal de
todos los modelos: se usan configuraciones reales contrastadas y se declaran
sus límites. No se elimina un destino prometido para evitar una prueba fallida.

### 6. Cerrar una colección útil y mantenible

**Cambio:** integrar y publicar cada resultado por intención, revisar la
documentación vigente y conservar el mínimo recibo no sensible de los nuevos
casos en recursos/tests/docs existentes según quién lo use. Caso, revisión,
runtime/configuración pertinente, resultado y límite bastan; no duplicar logs,
fichas y matrices. Los temporales no deben ser la única prueba de una afirmación
decisiva que deba sobrevivir al host. El commit conserva decisión y aprendizaje;
la guía expresa la operación vigente.

**Aceptación final:** fuentes y recursos preservados; revisiones admitidas
coherentes; casos positivos y límites materiales cubiertos; decisiones de
arquitectura pendientes resueltas o alcance de conformidad explícitamente parcial;
instalaciones autorizadas coherentes; cambios propios publicables en Git y
paridad verificada. El dictamen separa las seis dimensiones del corte y explica
lo reconstruido, conservado, retirado y aún no evaluado. La aceptación personal
de Félix se distingue del juicio técnico del ejecutor.

No se declara «misión completa» mientras falte una promesa necesaria para el
alcance acordado. Sí se puede cerrar un incremento o informar conformidad parcial
sin mantener activo todo el corpus. Tras cierre material, la documentación
canónica conserva lo necesario y este plan pasa a antecedente fechado; si hay
interrupción, sólo `HANDOFF.md` temporal conserva el siguiente paso.

## Cómo controlar el esfuerzo sin perder la complejidad

- El ejecutor decide el menor caso que pueda refutar la afirmación importante.
  No repite una prueba por cambiar de fase o recibir otro nombre de lote.
- Compara el resultado entregado, errores materiales, correcciones e
  intervenciones humanas, tiempo y tokens/costo si el runtime los expone.
  Mide la ruta completa, incluidos auxiliares y repetición de intentos. No usa
  longitud, retórica, test verde o un puntaje compuesto como sustitutos de valor.
- Usa igual contexto, configuración y herramientas al comparar rutas. El
  criterio se fija antes de mirar la respuesta; un juicio propio no se llama
  aceptación de Félix. Una diferencia pequeña o variable queda inconclusa;
  repite sólo si la incertidumbre impide decidir una arquitectura relevante.
- La evidencia de una negativa correcta no sustituye el resultado positivo
  prometido. La evidencia de un método no acredita automáticamente el agente
  que lo envuelve. La composición se prueba donde puede perder información,
  responsabilidad o continuidad.
- Un fallo de proveedor se separa de un defecto de producto. No se cambia un
  prompt para facilitarle la respuesta ni se amplía infraestructura por una
  incidencia aislada. Un límite de herramienta se declara o resuelve dentro de
  autoridad; no se simula el efecto ausente.
- No se estiman semanas o presupuestos de inferencia sin datos. El primer caso
  comparable informa el costo de los restantes; se ajusta orden y profundidad
  con esa evidencia. Un gasto o efecto fuera de la autoridad se plantea con
  alcance concreto, continuando lo independiente.
- No se implementan multi-tenancy, RBAC empresarial, scheduler, dashboard de
  evals, base de estado paralela o catálogo duplicado. Se conservan locks,
  propiedad, revisión y recuperación porque incluso un usuario puede tener dos
  procesos y ediciones que no deben perderse.

**Siguiente movimiento (tras el ajuste focal Hermes/integral):**
el juicio conductual neutro quedó rendido (FAIL acotado, sin cambio de texto);
sesiones vivas para `steve-jobs`, `ux-research-design-ai`, `allan-kelly`,
`dov-dori` y el agente `kora` sólo cuando un caso discriminante las requiera.
La aceptación final de Félix sigue distinguida del cierre técnico, de la
conformidad parcial recibida y de toda evaluación técnica del ejecutor.
No hace falta otra auditoría general ni una especificación nueva para continuar.
