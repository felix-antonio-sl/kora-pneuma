# Handoff vigente — 2026-07-22 — panel agéntico de roles HODOM-HSC

> Memoria operativa auxiliar. No legisla ni sustituye `ALMA.md`, `ley/`, los
> artefactos canónicos, Git ni el estado vivo de los runtimes.

## Objetivo

Continuar la auditoría categorial integral de `kora-pneuma`, con foco en
ingeniería agéntica, y convertir en formalismo solo aquello que admite objetos,
morfismos, composición y leyes genuinos. Remediar falsedades y sobreafirmaciones
sin expandir el shape ni fabricar una semántica runtime inexistente.

El corte de entrega guiada convirtió los gates KORA ya existentes en una
preparación segura hacia Codex: resuelve un artefacto, valida su fuente,
regenera su emisión derivada, contrasta instalación y devuelve un recibo
tipado. `entrega-kora` conserva su frontera: no aplica cambios al runtime, no
cambia lifecycle y no amplía el shape.

El corte más reciente materializa en Codex, con alcance de proyecto, las 14
perspectivas institucionales provisionables de HODOM-HSC. Son interlocutores de
diseño y validación; no sustituyen titulares humanos, autoridad clínica o
fiscalizadora, políticas RBAC ni evidencia de práctica.

El handoff anterior quedó archivado en
`_archivo/HANDOFF-2026-07-18-auditoria-categorial-integral.md`.

## Corte más reciente: panel R01–R14 para `hd-hsc-os`

Se publicaron 14 fuentes `urn:salud:artefacto:hodom-hsc-*`, una por cada
`roleType` provisionable del catálogo DT: Dirección Técnica, Enfermería
Coordinadora, Médico de Atención Directa, Médico Regulador, Enfermería Clínica,
Kinesiología, TENS, Trabajo Social, Fonoaudiología, Otro Profesional, Conductor,
Administrativo, Administrador de Seguridad y SEREMI. `superusuario-dev`,
paciente/cuidador y los actores de interfaz externos quedan fuera porque no son
roles provisionables de esta configuración.

La decisión arquitectónica, revisada adversarialmente por `agent-architect`
v2.7.0, es homogénea:

```text
forma       subagente
arnes       persona
vector      [2,1,2,1,2]
sigma       [3,3,3,3,2]
herramientas [Read,Grep,Glob]
target      codex
alcance     proyecto
```

El vector clasifica cómo opera el artefacto y no la jerarquía del oficio. Cada
persona se diferencia mediante un `U_phen` conductual y el conflicto propio de
su rol. Todas reciben fase, artefacto/diff, journey, evidencia N/L/O/D/V y
pregunta; emiten `ROLE_REVIEW` con postura, evidencia, hallazgos, costuras,
riesgos, criterios, pruebas, disenso y `human_decision_required`. Los errores
comunes son `missing-context`, `outside-role`, `authority-gap`,
`non-demonstrated-practice` y `phi-detected`.

Los cuerpos incorporan una guardia temporal: dotación, funciones absorbidas,
horarios y estado de V01–V13 pertenecen al corte fuente 2026-07-22 y solo se
tratan como vigentes con evidencia viva competente en la entrada. Trabajo
Social conserva su condición de rol objetivo sin fingir dotación; Otro
Profesional rehúsa inventar una disciplina; SEREMI declara que es una
perspectiva regulatoria simulada y externa.

Estado material:

```text
fuentes       artefactos/agentes/salud/hodom-hsc-*.md
test          tests/test_hodom_hsc_role_agents.py
commit KORA   5d7ce0e88c8de80d6a01842911aa475133e9f8ce
emisión       _emision/codex/agents/hodom-hsc-*.toml
instalación   hd-hsc-os/.codex/agents/hodom-hsc-*.toml
commit app    5a0c5fee9514c3704b0df1c29bded819bc29ba63
manifest      sha256:b31621159ffb28cf26d54c2db8c13b3e7eee2d1afa714238451a993cca8a1207
```

Las 14 instalaciones son byte-idénticas a sus emisiones y sus TOML parsean con
los campos Codex obligatorios. Los gates cerraron `velar --estricto` 13/13,
suite KORA 253/253 y pre-push de cumplimiento de `hd-hsc-os` 113/113. Codex CLI
0.145.0 cargó el proyecto con `--strict-config`.

Dos canarios efímeros bajo sandbox `read-only` devolvieron la postura esperada
ante un falso cierre de E2E-01: `brecha`, práctica no demostrada o brecha de
autoridad, decisión humana requerida y cero intento de mutación. La traza JSON
no expuso inequívocamente el hilo hijo —el primer intento además fue rechazado
por combinar `agent_type` con fork de historial completo—, por lo que esta
salida es **compatible con la persona pero no demuestra todavía identidad de
invocación ni fidelidad conductual**. El próximo smoke debe crear el subagente
sin fork de historial desde un turno padre `read-only` y conservar una traza con
identidad del receptor.

`herramientas: [Read,Grep,Glob]` es una frontera fuente, no enforcement. Codex
no materializa una allowlist exacta de built-ins y el subagente hereda los
overrides vivos del padre. Hasta que exista enforcement propio por agente, el
panel se invoca únicamente desde turnos `read-only`. Sello y bytes iguales
prueban procedencia y paridad material; no prueban autoridad, safety ni práctica
HSC.

## Corte previo relevante: `agent-architect` v2.7.0 en Codex

`urn:dev:artefacto:agent-architect` se conserva como un KORA agente válido en
su forma exacta de **subagente persona** (`forma=subagente`, `arnes=persona`,
vector `[2, 1, 2, 0, 2]`). La puesta a punto no lo ascendió artificialmente a
agente persistente ni lo degradó a skill.

Su despliegue canónico quedó restringido a `targets: [codex]` sin recortar el
dominio de autoría: desde Codex puede diseñar artefactos KORA para cualquier
target declarado por el artefacto en trabajo. El contrato ahora:

- clasifica habilidad, subagente, agente y plataforma primero por modo de
  invocación y luego valida la firma completa; no usa materia como discriminante
  único porque los dominios de `mu` se solapan;
- integra `urn:kora:kb:cat-contrato-ingenieria-agentica` y separa `Spec(a)`,
  `Model(a)` y `Runtime_T(a,r)`;
- declara su propio `I_self`, `O_self`, protocolo, adaptador, errores e
  invariantes observables;
- usa `autoria-de-persona` como candidato procedural con `I_persona` y
  `O_persona`, sin presentar la arista `componible` como composición semántica;
- reancla identidad, personalidad y firma a las secciones vigentes de ley y
  rebaja el corte cosmovisión/operativo a política editorial explícita;
- distingue herramientas declaradas, alcance normativo y autoridad efectiva
  del runtime;
- emite solo el custom agent TOML que corresponde a un subagente Codex, sin
  skill compañera ni proyecciones a otros targets.

La corrección se condujo en rojo-verde y pasó una refutación adversarial de
contexto limpio. La suite completa está verde, `velar --estricto` informa todo
coherente y el recibo final `entrega-kora-v1` es `parity-faithful`. Los conteos
vivos se consultan con los gestos; no se fijan en este handoff.

`entrega-kora` preparó y verificó cada emisión y se detuvo ante la deriva
esperada antes de aplicar. La instalación se ejecutó fuera de esa skill, bajo la
orden explícita del operador, mediante `transmutar --aplicar`; el recibo se
repitió después de la aplicación. Estado material final:

```text
fuente          artefactos/agentes/dev/agent-architect.md v2.7.0
hash-fuente     db27a0f4dac42b5e206e6d71b61a750174aca6e87987e0019adc9696d96a69ca
emisión         _emision/codex/agents/agent-architect.toml
instalación     /home/felix/.codex/agents/agent-architect.toml
sha256-producto 59b677cb80902971ca56b01d3647fc9864ad7355b9c4441ce499401df88420b6
commit-producto 360efbadc6518c5dd27626c709a95a75c0393674
```

Emisión e instalación son byte-idénticas y el TOML contiene exactamente los
campos obligatorios documentados por Codex (`name`, `description` y
`developer_instructions`). Codex CLI 0.145.0 cargó su configuración en modo
estricto, reportó instalación consistente y `multi_agent` estable y activo.
Esta evidencia prueba fuente, emisión, instalación y paridad material; **no
prueba todavía la conducta del agente ni su autoridad efectiva dentro de una
invocación real**. La comprobación conductual debe hacerse en una sesión nueva
para no asumir un hot reload no documentado, no porque se haya demostrado que
Codex exija reinicio.

Las emisiones derivadas obsoletas de Claude Code, OpenCode y OpenClaw se
retiraron después de reducir el target. No había instalaciones de
`agent-architect` en esos runtimes; ningún otro artefacto instalado fue tocado.

### Cierre seguro, decisiones y relevo

El alcance final de esta sesión fue únicamente la puesta a punto del agente,
su regresión ejecutable, la continuidad viva y su proyección derivada a Codex.
No se modificaron la ley, el transmutador, otros artefactos,
`/home/felix/.codex/config.toml` ni runtimes distintos de Codex.

Decisiones consolidadas y alternativas descartadas:

- se conserva `forma=subagente` y `arnes=persona` porque su hogar operacional
  es la delegación; llamarlo agente persistente o reducirlo a habilidad habría
  contradicho cuerpo, invocación y firma;
- `targets: [codex]` limita dónde vive `agent-architect`, no los targets para
  los que puede diseñar; equiparar despliegue con dominio de autoría habría
  introducido una restricción funcional no solicitada;
- `autoria-de-persona` se usa mediante un adaptador procedural explícito;
  declarar composición semántica sin wiring, leyes ni testigos fue rechazado;
- no se añadió skill compañera ni configuración propia de modelo, sandbox o
  MCP: el custom agent hereda esas capacidades de la sesión Codex y no debe
  prometer una autoridad que la fuente no controla;
- no se corrigió parcialmente `autoria-de-persona`: su fuente se proyecta a
  Claude Code, Codex y OpenCode, y un parche solo en Codex dejaría instalaciones
  divergentes y excedería este corte.

Artefactos del corte:

- `artefactos/agentes/dev/agent-architect.md`: fuente KORA v2.7.0;
- `tests/test_agent_architect.py`: regresiones de forma, contrato, anclas,
  alcance de autoría, herramientas y uso procedural de personalidad;
- `HANDOFF.md`: única continuidad operativa vigente;
- `_emision/codex/agents/agent-architect.toml` y
  `/home/felix/.codex/agents/agent-architect.toml`: producto derivado e
  instalación Codex, no fuentes de autoridad;
- `/home/felix/.codex/memories/extensions/ad_hoc/notes/20260722T111628Z-kora-agent-architect-cierre.md`:
  destilación durable para incorporar al índice de memoria, subordinada al
  canon y al estado vivo.

El cierre repitió suite completa, `velar --estricto`, paridad focal, parseo TOML
y carga estricta de Codex; todos los gates del artefacto quedaron verdes. El
único aviso de `codex doctor` fue una diferencia entre inventarios de rollouts
y base de estado, sin evidencia de causalidad con este agente. Git quedó limpio
y sin divergencia antes de esta actualización; los commits de producto y
auditoría ya estaban confirmados en `origin/master`. Este cierre documental se
publica como unidad separada y debe comprobarse siempre contra el remoto vivo.

Riesgo conocido: `artefactos/skills/kora/autoria-de-persona/SKILL.md` conserva
anclas y glosas incompatibles con la doctrina vigente —entre ellas
`vector = tipo`, una sección inexistente de `cat-agent-coalgebra`, una lectura
no sustentada de `cat-agent-modulo` y el tratamiento de `componible` como
composición—. `agent-architect` v2.7.0 amortigua esas afirmaciones, pero no sana
la dependencia. La siguiente acción recomendada es reparar esa skill como una
unidad multiruntime coordinada, reemitir sus targets instalados y verificar
paridad global. Después, una sesión Codex nueva debe invocar `agent-architect`
en un caso acotado para cerrar la evidencia conductual aún desconocida.

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

La revalidación de continuidad del 2026-07-22 repitió `velar --estricto`, la
suite completa y la paridad focalizada de `entrega-kora`; los tres gates
quedaron verdes. No repitió las sondas vivas de autoridad ni App Server: su
evidencia fechada permanece como antecedente, no como observación actual.

- `python3 kora.py velar --estricto`: 13/13 checks.
- `python3 -m unittest discover -s tests`: 237 pruebas, todas verdes.
- `git diff --check`: verde.
- `py_compile` sobre `kora.py`, los testigos, el helper de entrega y sus tests,
  con bytecode bajo `/tmp`: verde.
- Validador genérico de skills sobre la emisión Codex de `entrega-kora`:
  `Skill is valid!`.
- `python3 -m tests.steipete_codex_hardened_contract`:
  `contract-satisfied`, sin archivo testigo residual.
- App Server: dos handshakes y dos consultas contra el daemon `0.144.3`,
  schemas relevantes `0.144.3`/`0.144.6` idénticos y siete conexiones activas
  al decidir; no se creó hilo, turno ni reinicio.
- `steipete`: `5 fiel`, `0 desviadas`, `0 no-instaladas`,
  `0 sin-emisión`.
- `cat-thinking`: `3 fiel`, `0 desviadas`, `0 no-instaladas`,
  `0 sin-emisión`.
- `entrega-kora`: `1 fiel`, `0 desviadas`, `0 no-instaladas`,
  `0 sin-emisión`.
- Paridad global: `117 fiel`, `0 desviadas`, `11 no-instaladas`,
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

Se emitió y aplicó `entrega-kora` únicamente a su target v1:

- `/home/felix/.agents/skills/entrega-kora`.

Las pérdidas declaradas de Codex/OpenCode permanecen explícitas en sus sellos.

## Corte productivo: `entrega-kora` v1

`urn:kora:artefacto:entrega-kora` es una skill activa, acotada a Codex, que
compone gates canónicos sin introducir un séptimo gesto:

```text
consulta exacta
  -> resolución por censo/nombre
  -> gate de lifecycle
  -> suite completa
  -> emisión derivada
  -> velar --estricto
  -> paridad del artefacto
  -> recibo JSON + resumen humano
```

Para conocimiento publicado no hay emisión ni paridad: el recorrido termina
después de la suite y `velar`. La skill nunca ejecuta `--aplicar`, `ciclo`,
edición de fuente, commit ni push. Las sugerencias por coincidencia parcial no
se seleccionan automáticamente y una identidad ambigua falla cerrada.

El recibo distingue `knowledge-validated`, `parity-faithful`,
`not-installed`, `partially-installed`, `ambiguous`, `not-found`, `blocked`,
`observation-error` y `unsupported-target`. Formalmente, estas variantes forman
una unión etiquetada de registros en `Set`; esto tipa los resultados del
adaptador, pero no demuestra un funtor, una coálgebra ni una semántica de
ejecución del artefacto entregado.

La prueba viva desde la instalación Codex cubrió:

- `cat-thinking` y su variante de mayúsculas: `parity-faithful`;
- `cat-kora-semantica-operacional`: `knowledge-validated`;
- `steve-jobs`: `partially-installed`, sin instalación automática;
- `entrega-kora`: detectó primero una instalación desviada, bloqueó sin
  aplicar y, tras una aplicación explícita externa al comportamiento de la
  skill, devolvió `parity-faithful`.

El corte reúne en una invocación controles que antes se coordinaban por
separado, pero todavía no hay medición de tiempo, errores de operador o
usabilidad. La mejora UX es una hipótesis instrumentable, no un resultado
probado.

### Artefactos y decisiones persistentes

- Fuente canónica: `artefactos/skills/kora/entrega-kora/SKILL.md`.
- Helper ejecutable:
  `artefactos/skills/kora/entrega-kora/referencias/entrega.py`.
- Contrato verificable: `tests/test_entrega_kora.py`.
- Instalación derivada observada: `/home/felix/.agents/skills/entrega-kora`;
  no es fuente de verdad.
- Producto y primer cierre documental: commits `d03d876` y `291c223`.

Se conservan cuatro decisiones: Codex es el único target v1; la emisión
derivada sí pertenece al flujo; `--aplicar` exige una acción externa y
explícita; ni el recibo ni la paridad autorizan ampliar el shape o afirmar
conducta runtime.

### Aprendizajes destilados

1. La vía productiva más pequeña fue componer los gestos existentes, no crear
   otro gesto constitucional ni una abstracción categorial nueva.
2. El orden es parte del contrato: suite, emisión derivada, `velar` y paridad.
   Validar frescura antes de emitir bloquea precisamente el caso que la entrega
   debe reparar. El conocimiento, que no se emite, termina en suite y `velar`.
3. Resolución exacta, ambigüedad explícita y fallo cerrado son semántica de
   producto: evitan entregar el artefacto equivocado aunque exista una
   sugerencia plausible.
4. Una fibra cerrada no debe incorporar residuos del intérprete. Un
   `__pycache__` accidental altera materialmente emisión e instalación; la
   suite impide que vuelva a introducirse bytecode en esa fibra.
5. `not-installed` y `partially-installed` son diagnósticos completos, no
   permisos de despliegue. Separar observación de mutación mantiene la acción
   reversible y la autoridad visible.
6. La unión etiquetada del recibo tipa alternativas en `Set`; no prueba por sí
   sola functorialidad, coálgebra, equivalencia, safety ni autoridad efectiva.
7. El siguiente dato valioso no es otro campo del shape: es evidencia de uso
   real —duración, estado obtenido y corrección manual necesaria—. Los conteos
   globales de paridad no se memorizan; se consultan en vivo.

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
7. `entrega-kora` v1 solo cubre Codex y no mide todavía tiempo de entrega,
   errores de operador ni satisfacción. No se debe ampliar a otros targets ni
   automatizar `--aplicar` antes de observar uso real.
8. El helper interpreta el resumen textual actual de
   `transmutar --paridad`; falla cerrado si no lo reconoce, pero una salida
   JSON canónica reduciría este acoplamiento.
9. `urn:kora:artefacto:autoria-de-persona` v1.2.0 conserva deuda doctrinal
   preexistente: equipara vector con tipo en una regla, cita secciones que ya no
   sostienen `U_phen` o el supuesto eje de encapsulación, describe mal la
   partición OpenClaw y habla de composición sin interfaz. Su fuente y sus
   instalaciones actuales son materialmente fieles, por lo que la corrección
   debe ser una unidad multiruntime separada: reparar fuente, reemitir, aplicar
   solo a destinos previamente instalados y cerrar con paridad global.

## Campaña HODOM–HSC: koraficación del subárbol 2026-07-20

### Resultado

Se ejecutó el corte curatorial de
`/home/felix/projects/hd-dt/01-normativo/hsc/subarbol-candidatos-koraficacion-hodom-2026-07-20.md`
sin modificar `10-modelamiento-opm/`.

El inventario vivo no se fija en este handoff: se obtiene bajo demanda con
`python3 kora.py censo`. Este corte registra decisiones, límites y rutas de
retoma, no un conteo paralelo al filesystem canónico.

No se confundió publicación del artefacto con vigencia clínica de su fuente:
PRO-110, PRO-134, APT 1.2, PRO 89 y PRO 90 quedaron expresamente históricos.
Los recortes declaran páginas o secciones excluidas. El Arsenal conserva el PDF
como autoridad primaria y no afirma un subarsenal HODOM.

Por decisión del DT de 2026-07-20, una fecha de término declarada no produce
baja automática si no se identifica reemplazo, instrucción contraria o
incompatibilidad superior. En ese caso se conserva aplicación operativa
provisional hasta la actualización, manteniendo visibles la fecha impresa, el
estado de búsqueda y el carácter local de la decisión. Esta continuidad no
demuestra por sí sola adopción efectiva ni aplicabilidad específica a HODOM.

### H0 resuelto

El corte H0 quedó resuelto:

- **Publicadas:** PRO 002; PRO-110 histórico; RPE-34; Arsenal 2026;
  PRO-134 recorte HODOM; AOC 2.1; APT 1.2 histórico; núcleo de
  contactabilidad; HSC 14.2; HSC 14.3; AOC 1.1; REG 1.1; GCL 1.12; NT 245;
  GCL 2.3; REG 1.2; DP 2.1; copia observada de MO U.G.D.P. y Mov. 002.
- **Excluidas por contenido:** la cartera 2024 no identifica una cartera
  HODOM —solo cinco prestaciones genéricas de visita—; Decreto Exento 74/2024
  regula Modalidad de Cobertura Complementaria y no modifica HODOM.
- **Sin bloqueos remanentes:** los PDF inicialmente escaneados recibieron OCR,
  cotejo visual y koraficación. DP 2.1 conserva por separado la vigencia
  impresa hasta mayo de 2025 y la extensión de la Resolución Exenta 87 hasta
  mayo de 2027. El PDF rotulado Modelo UGCC se publicó deliberadamente como
  **copia observada** de MO U.G.D.P. y Mov. 002: mantiene aplicación operativa
  provisional, pero no oculta la discordancia de título ni reconstruye las
  páginas internas 25 a 31 ausentes.

AOC 1.1 aporta una frontera negativa importante: Código Azul solo cubre
emergencias **dentro del recinto** y no constituye rescate domiciliario.

### H1 y fuentes nacionales admitidas

- Entrega de turno: Medicina, Enfermería/Matronería, Enfermería de Urgencia y
  Medicina de Urgencia publicadas por separado. El último PDF, completamente
  escaneado y con siete páginas rotadas, se recuperó mediante OCR y cotejo
  visual de sus 14 páginas y cinco formularios.
- Laboratorio: RPE-33, los históricos PRO 89/90 y APL 1.2 publicados. APL 1.2
  se recuperó completo sobre 184/184 páginas y 169/169 prestaciones del
  catálogo, manteniendo separados auto-toma domiciliaria, contacto confidencial
  en domicilio y una cadena profesional HODOM que la fuente no define.
- RPE nacionales publicados: 9 Telemedicina, 14 Rehabilitación, 25 Cuidados
  Paliativos, 27 Imagenología, 33 Laboratorio y 34 HODOM.
- Farmacia se abrió por fuente para continuidad farmacológica. IAAS, aseo y
  residuos también se publicaron por fuente, sin construir una norma HODOM
  sintética. El Arsenal no demuestra subarsenal, transporte ni cobertura
  HODOM, y los protocolos intrahospitalarios no se trasladan al domicilio sin
  validación propietaria de aplicabilidad.

### Continuidad farmacéutica H1 publicada el 2026-07-21

Se publicaron como fuentes separadas, sin fusionar códigos ni convertirlas en
práctica HODOM:

```text
urn:salud:kb:hsc-apf-1-4-rotulacion-envasado-despacho
urn:salud:kb:hsc-apf-1-5-almacenamiento-conservacion-2023
urn:salud:kb:hsc-apf-1-5-formato-recetas-prescripcion
urn:salud:kb:hsc-apf-1-5-solicitud-devolucion-medicamentos
urn:salud:kb:hsc-apf-1-5-almacenamiento-conservacion-insumos
urn:salud:kb:hsc-apf-1-5-notificacion-reacciones-adversas-medicamentos
urn:salud:kb:hsc-17-2-estupefacientes-psicotropicos
urn:salud:kb:hsc-17-4-solicitud-medicamentos-uso-restringido
```

Los anexos gráficos se recuperaron como campos, relaciones y listas; no se
trasladaron valores poblados ni identificadores clínicos. Se preservaron la
colisión real de varias fuentes distintas bajo `APF 1.5`, las discordancias
internas y la diferencia de dos frente a tres días para recetas DAU. La fuente
de solicitud/devolución de medicamentos conserva su vigencia impresa vencida
y la aplicación operativa provisional decidida por el DT mientras no aparezca
sucesora, instrucción contraria o incompatibilidad superior.

Ninguna de estas fuentes demuestra subarsenal, stock, transporte o entrega al
domicilio, custodia domiciliaria, cobertura horaria efectiva, receta HODOM ni
adopción real. Esas interfaces siguen requiriendo validación de Farmacia,
Abastecimiento, Calidad y Dirección Técnica HODOM según corresponda.

### IAAS, residuos y entrega médica de Urgencia publicados el 2026-07-22

Se publicaron como fuentes institucionales separadas:

```text
urn:salud:kb:hsc-gcl-3-3-precauciones-estandar
urn:salud:kb:hsc-gcl-3-3-prevencion-infecciones-torrente-sanguineo-2025
urn:salud:kb:hsc-gcl-3-3-prevencion-itu-cup-2024
urn:salud:kb:hsc-24-8-aseo-desinfeccion
urn:salud:kb:hsc-pro-031-manejo-residuos-hospitalarios
urn:salud:kb:hsc-aoc-2-2-entrega-turno-medico-urgencia
```

Se preservaron tres documentos diferentes que imprimen `GCL 3.3`, sin
fusionarlos. El plan de residuos conserva `Pro-031` como identidad interna y
`HSC 27.A.1` como rótulo externo discordante. Su OCR y cotejo cubrieron las
69 páginas, incluidas tablas, flujos, planos, formularios y anexos. La entrega
médica de Urgencia completa el corpus AOC 2.2 de contraste, pero sus libros y
firmas no demuestran por sí solos transferencia efectiva de responsabilidad.

Las cinco fuentes IAAS/aseo/REAS regulan ámbitos institucionales impresos. No
prueban que HODOM use los dispositivos descritos, ni definen limpieza,
vigilancia, insumos, segregación, retiro o logística inversa en el domicilio.
Requieren un recorte validado por los propietarios IAAS, REAS, clínicos y la
Dirección Técnica HODOM antes de convertirse en práctica domiciliaria.

Este lote tampoco valida ni reemplaza
`urn:salud:kb:hodom-operacional-iaas`: ese BOK legado atribuye su contenido a
un manual HODOM que no fue localizado en la biblioteca auditada. Sus reglas
operativas y sus consumidores requieren una auditoría propietaria separada
antes de uso asistencial; las nuevas fuentes no deben citarse como
corroboración indirecta.

### H2 nacional, seguridad clínica y resiliencia publicados el 2026-07-22

Se publicaron fuentes separadas para planificación, desempeño, beneficios,
autorización, clasificación, trazabilidad, terapia endovenosa y continuidad
hospitalaria:

```text
urn:salud:kb:minsal-nt-243-clasificacion-establecimientos-hospitalarios-2025
urn:salud:kb:minsal-pauta-chequeo-nt-247-trazabilidad-dispositivos-medicos
urn:salud:kb:minsal-instructivo-pauta-autorizacion-sanitaria-hodom-2024
urn:salud:kb:minsal-orientaciones-planificacion-programacion-red-2025
urn:salud:kb:minsal-orientaciones-tecnicas-comges-2026
urn:salud:kb:superintendencia-salud-compendio-beneficios-2026
urn:salud:kb:hsc-apl-1-2-toma-traslado-muestras-2025
urn:salud:kb:hsc-gcl-1-2-vias-venosas-centrales-2025
urn:salud:kb:hsc-gcl-1-2-administracion-medicamentos-endovenosos-2024
urn:salud:kb:hsc-gcl-2-2-prevencion-caidas-2023
```

También se publicaron cinco fuentes institucionales de seguridad ocupacional y
resiliencia:

```text
urn:salud:kb:hsc-rh-4-2-accidentes-sangre-fluidos-riesgo-2023
urn:salud:kb:hsc-ins-1-1-plan-prevencion-incendios-2023
urn:salud:kb:hsc-ins-2-1-plan-evacuacion-2023
urn:salud:kb:hsc-ins-3-2-contingencia-agua-potable-estanques-2026
urn:salud:kb:hsc-ins-3-2-contingencia-energia-electrica-2022
```

Las orientaciones 2025 no equiparan APS domiciliaria, PADDS, telemedicina o
seguimiento remoto con HODOM. COMGES 1.13 preserva por separado la razón de
cumplimiento del Servicio y el promedio de estada por establecimiento; `8,5`
no es criterio clínico individual de alta. El compendio mantiene separados plan
complementario, CAEC, GES, Fonasa y Ley Ricarte Soto.

NT 243 es clasificación hospitalaria, no una norma de seguridad del paciente.
La pauta HODOM está rotulada `Borrador revisión final` y no demuestra
autorización de HODOM-HSC. La pauta NT 247 no es la norma completa y su
`director técnico de la institución` no se reasigna al DT HODOM por inferencia.

Las dos fuentes de contingencia que imprimen `INS 3.2` —agua y energía— se
conservan separadas por título, fecha, acto y hash. Incendio, evacuación, agua,
energía y accidente ocupacional regulan ámbitos hospitalarios impresos; no
definen respuesta ante incendio residencial, respaldo de dispositivos en casa
ni aplicación domiciliaria del circuito ocupacional.

### H2 institucional y cierre del subárbol publicados el 2026-07-22

El último lote material publicó gobierno, personas, soporte y recursos clínicos
como fuentes separadas:

```text
urn:salud:kb:hsc-1e-mg-cal-modelo-gestion-dcsp-2024
urn:salud:kb:hsc-mo-daiu-003-organizacion-atencion-integral-usuario-2022
urn:salud:kb:hsc-cdg-02-organizacion-unidad-control-gestion-2022
urn:salud:kb:hsc-mo-rrhh-01-organizacion-gestion-personas-2022
urn:salud:kb:hsc-mo-cap-02-organizacion-capacitacion-desarrollo-2022
urn:salud:kb:hsc-rh-2-1-programa-induccion-2024
urn:salud:kb:hsc-rh-3-1-programa-capacitacion-iaas-rcp-2023
urn:salud:kb:hsc-mo-fin-044-organizacion-finanzas-2022
urn:salud:kb:hsc-mo-abast-01-organizacion-abastecimiento-2022
urn:salud:kb:hsc-mo-2p-dciye-organizacion-control-infecciones-epidemiologia-2024
urn:salud:kb:hsc-mo-farm-001-modelo-organizacion-farmacia-2023
urn:salud:kb:hsc-mo-lab-03-modelo-organizacion-laboratorio-2022
urn:salud:kb:hsc-mo-imag-014-modelo-organizacion-imagenologia-2023
urn:salud:kb:hsc-mo-sa-est-002-modelo-organizacion-esterilizacion-2022
urn:salud:kb:minsal-plan-campana-invierno-2025
```

La cobertura fue 404/404 páginas o diapositivas. Gestión de Personas conserva
la ausencia material de las páginas internas 22–23; Finanzas, la página 8; y
Capacitación, sus tres hojas físicas en blanco. Los quince artefactos declaran
FS 100 % dentro de sus recortes, CR reproducible superior a 1,5 y exclusión de
personas, firmas, contactos y valores poblados.

Calidad, Atención Integral, Control de Gestión, Personas, Capacitación,
Finanzas, Abastecimiento y DCIYE aportan capacidades institucionales e
interfaces. No acreditan adopción HODOM, presupuesto, stock, competencia
disponible, SLA o práctica actual. Farmacia, Laboratorio, Imagenología y
Esterilización tampoco crean subarsenal, toma de muestras, adquisición de
imágenes ni circuito limpio–sucio domiciliario. La visita domiciliaria de
investigación epidemiológica no es atención clínica HODOM.

El Plan de Invierno es una presentación macro, nacional y estacional de 2025;
no es regla permanente ni prueba de capacidad HSC/HODOM en 2026. Conserva
lineamientos, cifras y defectos documentales sin transformar metas en resultados.

La reconciliación final del corte arrojó 96 unidades seleccionadas para
koraficación: 79/79 fuentes Drive y 15/15 locales admitidas produjeron **94
artefactos fuente publicados**. Cartera HSC 2024 y Decreto Exento 74/2024 son
las dos exclusiones por contenido ya justificadas. Los cinco artefactos `R`
resuelven publicados sin duplicación; REG 1.2 y GCL 2.3 conservan sus copias
byte-idénticas como procedencia de un solo artefacto por fuente. No quedan IDs
Drive ausentes o ambiguos ni hashes de fuente huérfanos.

El PDF primario del Arsenal 2026 permanece intacto y controlador. Su
transcripción de trabajo se conserva; una edición de formato cambió su hash
respecto del corte fechado, sin pérdida de la fuente primaria ni creación de un
segundo artefacto.

### URN publicadas antes del lote farmacéutico

```text
urn:salud:kb:hodom-rpe-34-criterios-tecnicos
urn:salud:kb:hsc-arsenal-farmacoterapeutico-2026
urn:salud:kb:hsc-pro-002-hospitalizacion-domiciliaria
urn:salud:kb:hsc-pro-110-hodom-historico-2019
urn:salud:kb:hsc-pro-134-gestion-pacientes-recorte-hodom
urn:salud:kb:hsc-aoc-2-1-derivacion-pacientes
urn:salud:kb:hsc-aoc-1-1-emergencia-riesgo-vital
urn:salud:kb:hsc-apt-1-2-transporte-pacientes-historico
urn:salud:kb:hsc-14-2-prestamo-catres-clinicos
urn:salud:kb:hsc-14-3-riesgo-biopsicosocial
urn:salud:kb:hsc-reg-1-1-ficha-clinica-unica
urn:salud:kb:hsc-gcl-1-12-identificacion-pacientes
urn:salud:kb:minsal-nt-245-identificacion-pacientes
urn:salud:kb:minsal-contactabilidad-nucleo-operativo
urn:salud:kb:hsc-aoc-2-2-entrega-turno-medico-medicina
urn:salud:kb:hsc-aoc-2-2-entrega-turno-enfermeria-matroneria
urn:salud:kb:hsc-aoc-2-2-entrega-turno-enfermeria-urgencia
urn:salud:kb:minsal-rpe-9-telemedicina
urn:salud:kb:minsal-rpe-14-rehabilitacion
urn:salud:kb:minsal-rpe-25-cuidados-paliativos-universales
urn:salud:kb:minsal-rpe-27-imagenologia
urn:salud:kb:minsal-rpe-33-unidades-laboratorio
urn:salud:kb:hsc-pro-089-resultados-vih-historico
urn:salud:kb:hsc-pro-090-almacenamiento-muestras-historico
urn:salud:kb:hsc-gcl-2-3-vigilancia-eventos-adversos
urn:salud:kb:hsc-reg-1-2-estandarizacion-registros-clinicos
urn:salud:kb:hsc-dp-2-1-consentimiento-informado
urn:salud:kb:hsc-mo-ugdp-mov-002-organizacion-copia-observada
```

Se reutilizan sin duplicación:

```text
urn:salud:kb:hodom-reglamento-ds1-2022
urn:salud:kb:hodom-decreto-exento-31-2024
urn:salud:kb:hodom-norma-tecnica-2024
urn:salud:kb:hodom-direccion-tecnica
urn:salud:kb:hodom-glosario-ontologia
```

### Cierre y próxima admisión

Cada lote pasó `velar --estricto` y la suite completa. Los artefactos de
conocimiento no tienen emisión derivada, por lo que no requieren
`transmutar --paridad`.

La campaña del subárbol 2026-07-20 quedó **cerrada**: 94/94 artefactos fuente
seleccionados publicados, dos exclusiones por contenido y cinco canónicos
reutilizados. No queda candidato material pendiente dentro de ese corte. Una
nueva admisión debe responder a una brecha o decisión HODOM concreta, aplicar
los mismos gates por fuente y no convertir esta biblioteca en koraficación por
catálogo.

Siguen fuera de este cierre la validación propietaria de práctica/adopción y las
fuentes aún no adquiridas que el corte identifica para Cuidador, territorio,
capacidad real, operación, datos, desempeño y software. También permanece
abierta la auditoría de `urn:salud:kb:hodom-operacional-iaas`; las nuevas fuentes
institucionales no validan el manual HODOM no localizado que ese BOK declara.

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
6. Usar `entrega-kora` en tareas reales y registrar duración, estado del recibo
   y correcciones manuales. El siguiente corte debe decidir con esa evidencia
   si conviene mejorar el contrato JSON de paridad; no añadir targets ni
   aplicación automática por anticipado.
7. Para cerrar la dimensión `Runtime_T(a,r)` de `agent-architect`, abrir una
   sesión Codex nueva —evitando asumir hot reload—, invocarlo sobre un caso de
   autoría acotado y observar entradas, salidas, límites de herramientas y
   no-coordinación. No convertir la paridad material ya verde en evidencia
   conductual.
8. Reparar `autoria-de-persona` en una unidad separada y coordinada con sus
   instalaciones Claude Code, Codex y OpenCode; no parchear solo la copia
   runtime ni dejar targets instalados en deriva.

## Rollback

Usar `git revert`, nunca `reset --hard`. Para retirar este corte, revertir el
commit de producto `d03d876`, eliminar solo la instalación derivada
`/home/felix/.agents/skills/entrega-kora` y regenerar `_emision/` desde las
fuentes restantes. Después, repetir `velar`, tests y paridad global. Eliminar
la fuente no retira por sí solo una instalación ya materializada.

Para retirar únicamente `agent-architect` de Codex, eliminar solo
`/home/felix/.codex/agents/agent-architect.toml`; es una proyección derivada y
se recupera con `transmutar --urn urn:dev:artefacto:agent-architect --target
codex --aplicar`. Para volver al corte defectuoso v2.6.0, revertir `360efba`;
para retirar toda esta puesta a punto y volver al estado anterior a la sesión,
revertir primero `360efba` y después `c395257`, junto con la continuidad
documental correspondiente. En ambos casos repetir suite, `velar`, emisión,
aplicación y paridad focal. No retirar ni reescribir otros custom agents.
