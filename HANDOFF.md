# Handoff vigente — 2026-07-20 — contrato `steipete` y contraste App Server

> Memoria operativa auxiliar. No legisla ni sustituye `ALMA.md`, `ley/`, los
> artefactos canónicos, Git ni el estado vivo de los runtimes.

## Objetivo

Continuar la auditoría categorial integral de `kora-pneuma`, con foco en
ingeniería agéntica, y convertir en formalismo solo aquello que admite objetos,
morfismos, composición y leyes genuinos. Remediar falsedades y sobreafirmaciones
sin expandir el shape ni fabricar una semántica runtime inexistente.

El handoff anterior quedó archivado en
`_archivo/HANDOFF-2026-07-18-auditoria-categorial-integral.md`.

## Veredicto

KORA no necesita que todos sus gestos sean funtores. Su formalización útil se
divide ahora en tres estratos explícitos:

1. **fuente declarativa**: firma, shape, lifecycle, relaciones y capacidades;
2. **modelo matemático**: solo cuando se exhiben tipos, estado, transición,
   efectos, observaciones y leyes;
3. **runtime efectivo**: conducta y autoridad que requieren una interpretación
   específica por target.

La ganancia de rigor consiste tanto en las pruebas nuevas como en las
obstrucciones documentadas. Categorías discretas ad hoc, analogías nominales y
URNs no convierten una función o un patrón en teorema.

## Núcleo formal añadido

### Semántica operacional de KORA

`urn:kora:kb:cat-kora-semantica-operacional` tipa los seis gestos vigentes:

- `velar` es una intersección finita de subobjetos de snapshots en `Set`;
- `censo` es una vista determinista, no un funtor sustantivo;
- `nombre` es resolución parcial bajo unicidad de URN;
- cada lifecycle es una categoría delgada de estados;
- `ciclo` realiza transformaciones parciales de snapshots y compone solo en su
  dominio común;
- el retiro sin gate y la promoción con gate impiden legítimamente una acción
  functorial total del lifecycle;
- las relaciones generan categorías libres de caminos por campo;
- la fidelidad por target es un funtor contravariante desde la demanda hacia
  `none <= partial <= full`;
- emisión, aplicación, paridad, `ley` y koraficación conservan su estatuto
  operacional o editorial, sin categorías fabricadas.

`urn:kora:kb:cat-kora-kernel` v1.1.0 incorpora la prueba de fidelidad
contravariante y conserva la coreflexión de la proyección numérica.

### Contrato categorial de ingeniería agéntica

`urn:kora:kb:cat-contrato-ingenieria-agentica` separa:

```text
Spec(a)          fuente declarativa KORA
Model(a)         modelo matemático explícito, si existe
Runtime_T(a,r)   conducta efectiva bajo contexto runtime r
```

El modelo reactivo mínimo queda tipado como:

```text
H(X) = (M(O × X))^I
c : U -> H(U)
step : U × I -> M(O × U)
```

El contrato exige testigos distintos para:

- morfismo coalgebraico y bisimulación;
- wiring tipado y composición de agentes;
- compatibilidad de efectos y feedback;
- realización de *pattern runs on matter* en `Poly`;
- no amplificación de autoridad mediante una relación tipada
  `Eff_T(a,r) ⊆ R_T[D_a]`;
- cierre de safety como subcoálgebra;
- preservación source→runtime mediante una interpretación por target.

`componible`, `herramientas`, `estados`, el sello y la paridad quedan
explícitamente limitados a lo que sí declaran o prueban.

## Corrección ejecutable

`ciclo` tenía un falso verde: al promover un conocimiento desde `borrador`,
`publicacion-digna` evaluaba el estado de origen y podía publicar un destino
con menos de tres tags.

Ahora una promoción:

1. ejecuta el registro completo de `velar --estricto`;
2. evalúa dignidad sobre el **estado destino** antes de escribir;
3. preserva el retiro/deprecación sin gate para no impedir jubilar una fuente
   incoherente.

La suite cubre el fallo y la coherencia entre camino compuesto y salto directo
en el dominio común.

## Correcciones adversariales del corpus

Se elevaron a v1.2.x las piezas ICAS afectadas y su síntesis:

- `icas-agencia`: distingue `Org_m` de su opuesto agéntico; separa
  profuntores de polinomios; retira la atribución ficticia `Idx:E->A` a
  Fukada. En el paper, las acciones son elementos/primary keys de `Actions`,
  no morfismos.
- `icas-protocolos`: GraphQL no es session type por nombre; un coend no
  implementa rendezvous; Paxos/PBFT no son sheaves sin interpretación.
- `icas-infraestructura` v1.2.1: encapsulación API no es el lema de Yoneda;
  capacidad declarada no es autoridad efectiva; la relación entre familias no
  tipa efectos sobre recursos.
- `icas-safety-alignment` v1.2.1: safety monoidal exige una inclusión y cierre
  demostrados; no-interferencia es una hipótesis por formalizar; la cota usa
  `R_T` y no expresa scopes de recursos; sheaf temporal no localiza causalidad
  por sí solo; mitigar un ataque no significa romper conmutatividad.
- `icas-sintesis` y `alma-de-kora`: propagan estas fronteras y dejan de llamar
  categorial a todo gesto.

`cat-thinking` v2.1.1 incorpora la semántica operacional, el contrato agéntico,
la matriz de testigos y nuevos falsos amigos/disparadores.

## Primer caso vertical

`urn:kora:kb:cat-caso-vertical-steipete-codex` instancia la recomendación
pendiente con un corte deliberadamente pequeño:

```text
agente      steipete
target      Codex, modo persona
interfaz    eventos observables de trabajo
propiedad   no cerrar sin evidencia verde vigente
```

El objeto formal es un monitor finito en `Set`:

```text
M(X) = X + V
H(X) = (M(O × X))^I
step : U × I -> M(O × U)
```

Su invariante impide alcanzar `closed` sin todos los gates del contexto y
vacía la evidencia ante cualquier cambio posterior o gate rojo. El test
exhaustivo recorre 6.144 pares estado/evento y verifica cierre de la
subcoálgebra segura en 5.136 pares cuyo estado inicial satisface el invariante.

`tests/steipete_codex_observer.py` mecaniza la observación para la superficie
pública `codex exec --json`:

```text
o     : R_ok -> I*
obs_r : R_ok* -> I*
```

Proyecta eventos nativos de turno, cambio y comandos, más markers explícitos
para `estimate`, `feel-review` y el fallback de cambios hechos por shell. Una
traza real instrumentada produjo los diez eventos de referencia y alcanzó
`closed`; una traza real sin protocolo fue rechazada. Esto no extiende la
prueba a Codex app, IDE, cloud ni a la conducta universal del LLM.

## Corte de autoridad efectiva

El mapping funcional `m_T : Tool ⇀ Tool_T` era demasiado estrecho: una tool
fuente puede realizarse por varias familias target y varias tools pueden
colapsar en una. El contrato v1.3.0 usa ahora una relación tipada:

```text
R_T ⊆ Tool × Tool_T
Eff_T(a,r) ⊆ R_T[D_a].
```

`tests/steipete_codex_authority.py` clasifica las cinco familias públicas de
capability item en `codex exec --json` y separa intento, éxito, fallo, declive
e incompletitud. Una traza solo aporta la cota inferior
`Succ(r,τ) ⊆ Eff(r)`: un éxito fuera de la imagen declarada refuta la
inclusión; no observarlo no la demuestra.

En el contexto personal vivo —`codex-cli 0.144.6`, user config heredada que
declara `danger-full-access`, approvals `never` y web `live`— la skill
`steipete` fue leída explícitamente y la sonda obtuvo:

```text
command_execution: 2 éxitos
web_search:         4 éxitos
R_codex[D_steipete] ∩ P = {command_execution, file_change}
```

`web_search` es un contraejemplo constructivo. Por tanto la no amplificación
es **falsa en ese contexto y vocabulario finito**. MCP, plugins y colaboración
no fueron invocados y permanecen desconocidos como autoridad efectiva, aunque
existan configuraciones habilitadas.

El veredicto compara familias de tool, no efectos sobre recursos. Como `Bash`
carece de scope fuente, podría realizar red por shell; no está demostrado que
`web_search` añada un efecto de red nuevo. El caso muestra también que el shape
vigente no tipa least-privilege por path, dominio, operación o modo.

Una segunda ejecución con `--ignore-user-config`, sandbox `read-only`, web y
multiagente deshabilitados produjo solo dos comandos exitosos. El parche de
sonda fue rechazado y no dejó archivo, pero la denegación apareció en
`stderr`, no en JSONL. El veredicto es únicamente
`no-observed-amplification`: sobre de mitigación reejecutable, no prueba
universal. La invocación también usó `--strict-config`.

Las trazas crudas se mantuvieron en `/tmp` solo durante la observación y no se
versionaron. No se modificaron `steipete`, el transmutador, el shape, las
instalaciones ni la configuración personal.

## Contrato operacional endurecido

Se inspeccionaron la ayuda, `codex exec --json`, `codex doctor --json` y el
esquema generado de App Server para `codex-cli 0.144.6`. No se halló en esas
superficies públicas una salida que enumere de forma unificada las tools
resueltas y visibles al modelo. El resultado es acotado a versión y
superficies: no afirma que tal manifiesto sea imposible ni que otra interfaz
no lo exponga. Tampoco se fabricó uno uniendo listas parciales.

`tests/steipete_codex_hardened_contract.py` convierte el sobre mitigado en
`steipete-codex-hardened-v1`. Fija:

- `codex-cli 0.144.6`, repo y `/usr/bin/zsh`;
- configuración y reglas de usuario ignoradas;
- sandbox `read-only`, approvals `never` y web deshabilitada;
- apps, browsers, plugins, multiagente, computer use, imágenes, hooks y
  dependencias de workspace deshabilitados; configuración MCP de usuario
  ignorada y dependencias/elicitación MCP deshabilitadas;
- exactamente dos comandos permitidos: lectura de la skill instalada y `pwd`;
- solicitud de intento nativo de parche y web sin fallbacks; solo el parche
  aporta denegación observable;
- denegación completa de escritura y ausencia del archivo testigo.

El runner conserva stdout/stderr solo en memoria, emite un recibo normalizado
y retorna `0/1/2` para satisfecho/violado/error de observación. Falla cerrado
ante versión distinta, item desconocido, terminal no exitoso, comando extra o
limpieza fallida.

Formalmente implementa un normalizador parcial `norm_C:Raw_C⇀E_C` y decide
`Sat_C:E_C→2`, equivalente al subobjeto de recibos válidos `S_C ↪ E_C` en
`Set`. La ejecución viva del 2026-07-20 produjo dos comandos exitosos
permitidos, denegación de escritura, ninguna otra familia exitosa, archivo
testigo ausente y `contract-satisfied`.

Esto prueba pertenencia del recibo a `S_C` y
`no-observed-amplification` para esa ejecución. No prueba
`Eff_P ⊆ R_codex[D_steipete]`, no enumera tools ausentes y no amplía el shape,
el emisor, la configuración ni las instalaciones.

## Contraste vivo de App Server

Se distinguieron dos contextos que no deben combinarse:

```text
r_cli = (codex exec, 0.144.6, configuración de la sonda)
r_app = (app-server daemon, 0.144.3, socket y clientes vivos)
```

El gestor ya apuntaba a `0.144.6`, pero el proceso dueño del socket seguía en
`0.144.3`. La sonda abrió dos conexiones efímeras e invocó solo métodos de
consulta: cada una hizo el handshake e inicializó el protocolo; en total se
consultaron capacidades de proveedor y estado MCP sin crear hilo ni turno. La
salida se normalizó en memoria; la sonda no guardó ni versionó nombres,
descripciones, schemas de tools o payloads crudos.

El resultado tipado fue:

```text
CapProv(r_app) ∈ 2^{ {namespaceTools,imageGeneration,webSearch} }
McpInv(r_app)  = Σ (s : Server_r). Tool_s
```

Los booleanos de proveedor, el inventario MCP por servidor y las listas
separadas de skills, hooks, plugins, apps, features y permisos no constituyen
el conjunto desconocido `A(r_app)` de tools visibles al modelo. Falta una regla
oficial de resolución y mapas de comparación; no se fabricó una unión.

Los schemas exactos de `0.144.3` y `0.144.6` tenían el mismo conjunto de 122
métodos y eran idénticos en las respuestas relevantes de `thread/start`,
capacidades de proveedor y estado MCP. En el momento de decidir había siete
conexiones establecidas al daemon. Reiniciarlo habría interrumpido clientes sin
añadir la interfaz buscada, por lo que se conservó `0.144.3`.

La alineación a `0.144.6` queda como higiene operacional para una ventana sin
clientes, no como paso categorial ni como medio para obtener un manifiesto. Al
hacerla se debe repetir la sonda porque el nuevo proceso será otro contexto
runtime.

## Evidencia de cierre

- `python3 kora.py velar --estricto`: 13/13 checks.
- `python3 -m unittest discover -s tests`: 228 pruebas, todas verdes.
- `git diff --check`: verde.
- `py_compile` sobre `kora.py`, los tres testigos y sus tests, con bytecode
  bajo `/tmp`: verde.
- `python3 -m tests.steipete_codex_hardened_contract`:
  `contract-satisfied`, sin archivo testigo residual.
- App Server: dos handshakes y dos consultas contra el daemon `0.144.3`,
  schemas relevantes `0.144.3`/`0.144.6` idénticos y siete conexiones activas
  al decidir; no se creó hilo, turno ni reinicio.
- `steipete`: `5 fiel`, `0 desviadas`, `0 no-instaladas`,
  `0 sin-emisión`.
- `cat-thinking`: `3 fiel`, `0 desviadas`, `0 no-instaladas`,
  `0 sin-emisión`.
- Paridad global: `116 fiel`, `0 desviadas`, `11 no-instaladas`,
  `0 sin-emisión`.

Las once unidades `no-instaladas` son ausencias previas y no autorizan
instalación automática.

### Auditoría final de cierre

La comprobación final del corte categorial anterior cubrió el rango completo
`4e83b97..03dcb05`, no solo su último commit. El corte de autoridad actual se
auditó adicionalmente desde la base `7501849`. El contrato operacional de este
handoff se auditó íntegramente desde la base `d96f854`; su evidencia vigente
está en el bloque anterior. Aquel cierre corrigió tres residuos:

- `cat-agent-coalgebra` v2.1.1 usa el título bibliográfico real de Beohar et al.;
- `icas-patrones` v1.1.1 deja de identificar todo anti-patrón con una propiedad
  categorial rota;
- `cat-thinking` v2.1.1 exige tipos e hipótesis correctos para iteradores,
  bisimulación y DSLs basados en mónadas libres.

Tres límites deben conservarse al comunicar el resultado:

1. la coreflexión demostrada concierne exclusivamente a la **proyección numérica
   de firmas** `P_T`; no alcanza al cuerpo, los sidecars ni la emisión completa;
2. las once unidades `no-instaladas` son ausencias previas. No se ha establecido
   que esa ausencia sea intencional;
3. `GENESIS.md` conserva, como acta inmutable, formulaciones históricas hoy
   superadas —identidad por firma, transmutación funtorial, bisimulación
   declarada y lifecycle total—. Para el estado vigente prevalecen `ALMA.md`,
   `ley/` y los tres artefactos formales nuevos; no debe citarse `GENESIS.md`
   como garantía runtime actual.

## Emisiones e instalaciones

Se reemitió y aplicó `cat-thinking` en sus tres targets declarados ya
instalados:

- `/home/felix/.claude/skills/cat-thinking`;
- `/home/felix/.agents/skills/cat-thinking`;
- `/home/felix/.config/opencode/skills/cat-thinking`.

Las pérdidas declaradas de Codex/OpenCode permanecen explícitas en sus sellos.

## Fuentes primarias contrastadas

- Emily Riehl, *Category Theory in Context*:
  https://emilyriehl.github.io/files/context.pdf
- Rutten, *Universal Coalgebra*:
  https://fldit-www.cs.tu-dortmund.de/~peter/Rutten/UniversalCoalgebra.pdf
- Beohar et al., *Predicate and relation liftings for coalgebras with side
  effects*: https://arxiv.org/abs/2110.09911
- Vagner, Spivak y Lerman, *Algebras of Open Dynamical Systems on the Operad
  of Wiring Diagrams*: https://arxiv.org/abs/1408.1598
- Libkind y Spivak, *Pattern Runs on Matter*:
  https://arxiv.org/abs/2404.16321
- Libkind y Spivak, *Dynamic task delegation for hierarchical agents*:
  https://arxiv.org/abs/2410.08373
- Shapiro y Spivak, *Dynamic Operads, Dynamic Categories*:
  https://arxiv.org/abs/2205.03906
- Niu y Spivak, *Polynomial Functors*:
  https://arxiv.org/abs/2312.00990
- Fukada, *Action is the primary key*:
  https://arxiv.org/abs/2409.04793
- OpenAI, *Codex non-interactive mode*:
  https://learn.chatgpt.com/docs/non-interactive-mode
- OpenAI, *Codex App Server*:
  https://learn.chatgpt.com/docs/app-server
- OpenAI, *Subagents*:
  https://learn.chatgpt.com/docs/agent-configuration/subagents
- OpenAI, *Agent approvals & security*:
  https://learn.chatgpt.com/docs/agent-approvals-security
- OpenAI, *Configuration reference*:
  https://learn.chatgpt.com/docs/config-file/config-reference
- OpenAI, esquema fuente de eventos `codex exec`:
  https://github.com/openai/codex/blob/main/codex-rs/exec/src/exec_events.rs

## Deudas abiertas y deliberadas

1. No existe una interpretación uniforme `Spec -> RuntimeModel` para los
   targets; por tanto no hay bisimulación fuente/runtime.
2. No hay una instancia de wiring con puertos y efectos para agentes KORA;
   `componible` sigue siendo un grafo de candidatos.
3. No hay manifiesto unificado ni prueba uniforme de autoridad efectiva. El
   contexto personal vivo de `steipete` en Codex tiene un contraejemplo
   `web_search`; el contrato endurecido decide su recibo, y el App Server vivo
   solo expone inventarios parciales, pero ninguno prueba exhaustivamente
   `Eff`.
4. El puente PMI→`Poly`→coálgebra permanece abierto.
5. El lifecycle no debe forzarse a funtor mientras promoción y retiro tengan
   dominios intencionalmente distintos.
6. El primer caso versionado no basta para añadir `inputs`, `outputs`,
   `effects`, `transition` o `wiring` al shape: `obs_r` solo cubre Codex CLI
   instrumentado y todavía falta evidencia de semántica común entre más casos.

## Cómo retomar

1. Leer `CLAUDE.md`, este handoff y el estado Git vivo.
2. Ejecutar `velar --estricto`, suite completa y paridad del artefacto tocado.
3. Para una afirmación agéntica, identificar primero si habla de `Spec`,
   `Model` o `Runtime`.
4. Exigir el testigo de la matriz del contrato antes de usar «coálgebra»,
   «bisimulación», «compone», «seguro» o «preserva».
5. El primer caso vertical ya cubre `obs_r`, un contraste finito de autoridad,
   el contrato operacional endurecido para Codex CLI y el contraste de
   inventarios del App Server vivo. Alinear el daemon solo en una ventana sin
   clientes y repetir la sonda; en una actualización de Codex, reauditar
   primero la disponibilidad de un manifiesto oficial y actualizar
   deliberadamente el pin y las sondas. No ampliar todavía el shape.

## Rollback

Usar `git revert`, nunca `reset --hard`. Este incremento no modifica fuentes
de agentes/skills ni instalaciones, por lo que revertirlo no exige reemisión.
Después del revert, repetir `velar`, tests y paridad global.
