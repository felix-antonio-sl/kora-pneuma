# Handoff vigente — 2026-07-18 — semántica operacional y contrato agéntico

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
- no amplificación de autoridad
  `Eff_T(a,r) ⊆ m_T[D_a]`;
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

Se elevaron a v1.2.0 las piezas ICAS afectadas y su síntesis:

- `icas-agencia`: distingue `Org_m` de su opuesto agéntico; separa
  profuntores de polinomios; retira la atribución ficticia `Idx:E->A` a
  Fukada. En el paper, las acciones son elementos/primary keys de `Actions`,
  no morfismos.
- `icas-protocolos`: GraphQL no es session type por nombre; un coend no
  implementa rendezvous; Paxos/PBFT no son sheaves sin interpretación.
- `icas-infraestructura`: encapsulación API no es el lema de Yoneda; capacidad
  declarada no es autoridad efectiva.
- `icas-safety-alignment`: safety monoidal exige una inclusión y cierre
  demostrados; no-interferencia es una hipótesis por formalizar; sheaf temporal
  no localiza causalidad por sí solo; mitigar un ataque no significa romper
  conmutatividad.
- `icas-sintesis` y `alma-de-kora`: propagan estas fronteras y dejan de llamar
  categorial a todo gesto.

`cat-thinking` v2.1.1 incorpora la semántica operacional, el contrato agéntico,
la matriz de testigos y nuevos falsos amigos/disparadores.

## Evidencia de cierre

- `python3 kora.py velar --estricto`: 13/13 checks.
- `python3 -m unittest discover -s tests`: 193 pruebas, todas verdes.
- `git diff --check`: verde.
- `python3 -m py_compile kora.py`: verde.
- `cat-thinking`: `3 fiel`, `0 desviadas`, `0 no-instaladas`,
  `0 sin-emisión`.
- Paridad global: `116 fiel`, `0 desviadas`, `11 no-instaladas`,
  `0 sin-emisión`.

Las once unidades `no-instaladas` son ausencias previas y no autorizan
instalación automática.

### Auditoría final de cierre

La comprobación final cubrió el rango completo `4e83b97..03dcb05`, no solo el
último commit. Corrigió tres residuos:

- `cat-agent-coalgebra` v2.1.1 usa el título bibliográfico real de Beohar et al.;
- `icas-patrones` v1.1.1 deja de identificar todo anti-patrón con una propiedad
  categorial rota;
- `cat-thinking` v2.1.1 exige tipos e hipótesis correctos para iteradores,
  bisimulación y DSLs basados en mónadas libres.

Dos límites deben conservarse al comunicar el resultado:

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

## Deudas abiertas y deliberadas

1. No existe una interpretación uniforme `Spec -> RuntimeModel` para los
   targets; por tanto no hay bisimulación fuente/runtime.
2. No hay una instancia de wiring con puertos y efectos para agentes KORA;
   `componible` sigue siendo un grafo de candidatos.
3. No hay prueba uniforme de autoridad efectiva; debe inspeccionarse por
   target y contexto.
4. El puente PMI→`Poly`→coálgebra permanece abierto.
5. El lifecycle no debe forzarse a funtor mientras promoción y retiro tengan
   dominios intencionalmente distintos.
6. No añadir `inputs`, `outputs`, `effects`, `transition` o `wiring` al shape
   hasta disponer de un caso operacional completo y un testigo versionado.

## Cómo retomar

1. Leer `CLAUDE.md`, este handoff y el estado Git vivo.
2. Ejecutar `velar --estricto`, suite completa y paridad del artefacto tocado.
3. Para una afirmación agéntica, identificar primero si habla de `Spec`,
   `Model` o `Runtime`.
4. Exigir el testigo de la matriz del contrato antes de usar «coálgebra»,
   «bisimulación», «compone», «seguro» o «preserva».
5. El siguiente avance formal debe ser un caso vertical pequeño —un agente,
   un target, una interfaz y una propiedad observable—, no una expansión
   taxonómica global.

## Rollback

Usar `git revert`, nunca `reset --hard`. Tras revertir, reemitir y reconciliar
`cat-thinking` con `transmutar --aplicar`, luego repetir `velar`, tests y
paridad global.
