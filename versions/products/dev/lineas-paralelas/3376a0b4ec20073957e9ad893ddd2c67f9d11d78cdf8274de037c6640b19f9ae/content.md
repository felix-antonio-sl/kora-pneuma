
# Lineas-Paralelas

## Proposito

Estructurar el trabajo pendiente de un repo en **N lineas de desarrollo
paralelas** con ownership, dependencias explicitas, contratos y convergencia
controlada: quien sostiene cada linea, que puede tocar, en que orden se
integra y que evidencia cierra cada parte.

Punto de partida: la entrega minima que cubra ownership, dependencias y
convergencia para el caso concreto. Puede ser un unico documento para dos
lineas simples, o README maestro + briefs + prompt cuando una delegacion
efectiva los necesita. Nada de esto es default: la forma la decide el
encargo, no la skill. El formato de la ronda 3 del repo de origen es un
ejemplo situado y reutilizable, nunca una obligacion.

N se deriva del trabajo y de la capacidad autorizada; el operador lo fija
cuando quiere, sin pregunta forzada. El repo objetivo y la autoridad
vigente pueden venir del contexto actual. La incertidumbre material si se
aclara con el operador antes de codificar. Esta skill no veta ni recorta
un permiso ya otorgado por el operador.

## Cuando Usar

- El operador pide estructurar trabajo pendiente para ejecucion concurrente.
- Hay pendientes priorizados que necesitan particion con responsables.
- Se quiere convergencia controlada con orden de integracion declarado.
- Se necesita asignacion a agentes independientes con scope estricto.

## Cuando No Usar

- Tarea unica de una sola linea: escribir directo, sin documentos.
- Decision arquitectural pura sin trabajo de implementacion: usar
  `urn:dev:artefacto:steipete` o un agente de pensamiento.
- Generar codigo: esta skill emite documentos de instrucciones, no codigo.

## Workflow

### 1. Capturar intent

Identificar lo que falte y sea material:

- **N**: se deriva del pendiente y la capacidad; el operador puede fijarlo.
  Sin rangos ni cuotas.
- **Ronda**: solo si el trabajo necesita estructura de ronda. En ese caso
  se usa la siguiente existente (`ronda<N+1>` es solo un nombre posible,
  no una formula que mezcle cantidad de lineas con historial). No crear
  directorios ni estructura por defecto.
- **Pendientes**: lista explicita, backlog vivo o referencia al HANDOFF.
- **Restricciones**: orden de integracion sugerido, lineas excluidas,
  prioridades.

### 2. Leer pendientes y precedentes

- Fuente de requisito suficiente del repo objetivo: backlog HU u otro
  requisito (no forzar HU si otra fuente basta).
- HANDOFF y backlog se leen por defecto; se escriben solo con autorizacion
  del operador o de la skill que los custodia.
- README de ronda previa, si existe: precedente a revisar, no herencia
  automatica. Comprobar vigencia y autoridad de sus reglas antes de
  reutilizarlas; lo obsoleto se deja con rationale.

Identificar: que debe cerrarse, su fuente, archivos clave y su estado,
decisiones vigentes que obligan a las lineas.

### 3. Mapear corpus reusable

Antes de inventar, verificar las fuentes reusables del repo objetivo
(codigo, patrones, assets, SSOT cuando el trabajo la necesite, briefs
previos). Revision en profundidad, no busqueda superficial. Cada linea
recicla lo razonablemente reutilizable y declara la evidencia concreta;
cada brief cita los recursos pertinentes.

### 4. Particionar en N lineas

- **Ownership**: responsable, alcance y entregable por linea.
- **Disjuntez conveniente**: archivos disjuntos por dominio cuando conviene;
  archivos compartidos con reglas lectura/escritura cuando conviene. Sin
  forzar archivos nuevos.
- **Dependencias explicitas** y secuencia de integracion con rationale.
- **Riesgo visible**: blast radius declarado por linea y trato acorde. Sin
  reparto fijo.
- **Cierre verificable** por linea contra su fuente de requisito.

Si dos lineas chocan mas alla de lo declarado: rebalancear o fundir.

### 5. README maestro (solo si la ronda lo necesita)

Repertorio seleccionable, no checklist obligatoria: encabezado, filosofia
declarada de ESTA ronda, reglas duras de ESTA ronda (las que el operador
fija o las del precedente tras comprobar vigencia; obligan a las lineas y
solo se cambian con rationale en el README), stack y comandos, vision de
lineas, mapa de colisiones con lectores/escritores e interfaces marcadas,
secuencia de integracion, anclaje a fuente de requisito, aceptacion con
evidencia y verificador.

### 6. Briefs por linea (solo si la delegacion los necesita)

Repertorio seleccionable: mision y slice minimo; requisito base (una o
varias fuentes segun el caso, sin inventar ni imponer cantidad); anclaje a
evidencia con paths; archivos permitidos con tipos; no-colisiones; slice
por capa cuando ayuda; tests y verificacion pertinentes al trabajo (la
planificacion no ejecuta tests: declara las comprobaciones que la linea
corre al cerrar); decisiones bloqueadas y libres; forma del entregable sin
imposiciones (sin footers ni formatos obligatorios). Sin orden impuesto ni
secciones por cuota.

### 7. Prompt de asignacion (opcional)

La plantilla extensa con placeholders e invocaciones es un ejemplo
disponible, no el default. Se usa cuando hay ruteo real a agentes.

## Reglas Duras

- Cada linea ancla fuentes vivas. No inventar.
- El contrato de la ronda lo declara el README o el operador para el caso;
  sin defaults de documentos, secciones, ordenes ni cuotas.
- La skill no impone filosofia, aditividad, archivos, tests, formatos ni
  vetos: propone; el operador y la ronda disponen.
- HANDOFF y backlog: lectura por defecto, escritura solo autorizada.
- Decisiones semanticas citan su fuente cuando la hay.
- Documentos en es-CL; identificadores y comandos en forma original.

## Alcance y realización

Esta skill opera sobre el repo objetivo claro en el contexto vigente o
confirmado por el operador (contexto de origen:
`/home/felix/projects/deep-opm-pro`). Escribe unicamente dentro de
`<repo-objetivo>/docs/instrucciones-lineas-dev/<ronda>/` cuando hay ronda,
o el documento acordado en rondas simples; fuera de ahi solo lee, salvo
autorizacion. Sin repo objetivo claro, no hay escritura.
La instalación personal de Codex permite descubrirla; no amplía ese alcance.
Su fuente vigente es el producto KORA `urn:dev:artefacto:lineas-paralelas`.
Para resolverlo se usa `python3 kora_cli.py resolve urn:dev:artefacto:lineas-paralelas`
desde la raíz de KORA. La realización se administra con
`python3 kora_cli.py install codex urn:dev:artefacto:lineas-paralelas`.

## Salida Esperada

La entrega minima acordada que cubra ownership, dependencias y
convergencia: un documento unico cuando basta; README, briefs y prompt
como repertorio opcional cuando hay ronda con delegacion que los
requiera. El ejemplo de la ronda 3 del repo de origen es reutilizable,
no default.

Reporte breve al operador al cerrar: tabla de lineas con requisito,
riesgo y archivos; secuencia de integracion con rationale; metricas
esperadas si el repo las define; cuidado de HANDOFF/backlog segun lo
autorizado.
