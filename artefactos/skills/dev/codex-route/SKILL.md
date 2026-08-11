---
urn: urn:dev:artefacto:codex-route
nombre: codex-route
version: 1.0.0
estado: activo
descripcion: "Router de tareas para Codex que decide modelo, esfuerzo, topologia y grafo de sesiones, comunicacion, contexto, persistencia, concurrencia, aislamiento de escritura, autonomia e integracion. Usar cuando una tarea pueda beneficiarse de subagentes, delegacion recursiva, trabajo paralelo, hipotesis independientes, map-reduce, pipelines o varios escritores; por defecto solo recomienda la ruta y ejecuta un grafo unicamente ante solicitud explicita."
fuente: "Sintesis KORA nueva creada el 2026-08-11 desde la propuesta Rediseño codex-route como router de grafos de sesiones, sha256:6a7eebfa997fe1095ed67bd289ee0c1c957523fed19dc978fbe4e1c0e1ca166a. Capacidades y nomenclatura contrastadas el 2026-08-11 con la documentacion oficial de Codex sobre subagentes, skills y worktrees, y con la superficie viva de herramientas de esta sesion. La rubrica es heuristica de ingenieria no validada como escala predictiva."
autor: FS
creado: 2026-08-11
lang: es
tags: [codex, subagentes, sesiones, routing, grafos, delegacion, concurrencia, worktrees, modelos, verificacion]
vector: [2, 0, 2, 0, 1]
sigma: [2, 1, 3, 3, 1]
arnes: disciplina
forma: habilidad
herramientas: [Read, Write, Edit, Glob, Grep, Bash, spawn_agent, send_message, followup_task, wait_agent, interrupt_agent, list_agents]
targets: [codex]
alcance: usuario
estados: [perfilar, trazar-camino-critico, decidir-sessionizacion, construir-grafos, enrutar, ejecutar, integrar, verificar, cerrar]
---
# codex-route

## Propósito

Convertir una tarea en la organización mínima de sesiones Codex que maximice
resultado verificable bajo restricciones de costo, riesgo, contexto y
coordinación. Diseñar la orquestación como:

```text
tarea
→ perfil cognitivo
→ camino crítico
→ grafo de sesiones
→ modelo y esfuerzo por sesión
→ dependencias y comunicación
→ escritura, autonomía y gates
→ integración y verificación
```

No maximizar sesiones. Preferir una sola sesión cuando un grafo no reduzca
tiempo, contaminación de contexto, riesgo o incertidumbre de forma material.

## Modos

### `route-only` — predeterminado

Evaluar y emitir una ruta. No crear sesiones, enviar mensajes, abrir worktrees,
editar archivos ni ejecutar el trabajo enrutado.

Usar este modo salvo que la persona solicite de forma explícita ejecutar la
ruta, delegar o trabajar con subagentes. Una invocación de la skill por sí sola
no autoriza ejecución.

### `route-and-run` — explícito

Activar únicamente ante una instrucción equivalente a «evalúa, configura y
ejecuta», «usa subagentes» o «delega este trabajo». Ejecutar sin pedir una
segunda confirmación si el alcance y la autoridad ya son claros.

La activación no amplía permisos. Mantener gates humanos para efectos externos,
acciones destructivas, costos extraordinarios, decisiones clínicas aplicadas y
cambios materiales de alcance.

## Resultado observable

La salida es exactamente una de estas variantes:

- `SIMPLE_ROUTE`: una línea para S0 o un sidecar obvio.
- `GRAPH_ROUTE`: ruta estructurada con perfiles, grafos, nodos, autoridad,
  contexto, concurrencia, escritura, escalamiento y verificación.
- `ROUTE_ERROR`: bloqueo, evidencia disponible y decisión mínima necesaria.

En `route-and-run`, añadir al resultado el estado real de ejecución:
`COMPLETE`, `PARTIAL` o `BLOCKED`, con cambios, evidencia y límites. Una ruta
propuesta no cuenta como ejecución y una ejecución no cuenta como resultado
integrado hasta verificar el objetivo global.

## Flujo de routing

### 1. `perfilar`: normalizar la tarea

Extraer objetivo, beneficiario, entregable, fuente de verdad, restricciones,
criterio de aceptación, riesgo, acciones autorizadas y presupuesto conocido.
No inventar una decisión material ausente. Si la incertidumbre es menor,
reversible y no cambia el resultado, declarar el supuesto y continuar.

### 2. Aplicar el fast path

Usar S0 sin desplegar matrices cuando la tarea tenga objetivo exacto, oráculo
fuerte, pocos pasos, un solo escritor y ninguna rama independiente útil.

Emitir una línea como:

```text
SIMPLE_ROUTE · S0 monosession · modelo actual · esfuerzo medium · sin delegación · sin worktree · verificación focal
```

No usar dos matrices para renombrar una tarea simple.

### 3. Calcular CEM-8 cuando la elección cognitiva no sea obvia

Leer [cognitive-epistemic-matrix.md](referencias/cognitive-epistemic-matrix.md)
y puntuar `A,N,E,O,B,C,H,R` de 0 a 4. No promediar: una dimensión extrema puede
gobernar modelo, esfuerzo, autonomía o verificación.

Leer [model-effort-routing.md](referencias/model-effort-routing.md) cuando haya
que escoger o recomendar modelo/esfuerzo. Separar siempre:

- configuración recomendada;
- configuración disponible en la superficie viva;
- configuración efectivamente usada.

No prometer cambiar el modelo de la sesión directora si el runtime no lo
permite. No inventar valores de `model` o `reasoning_effort` que `spawn_agent`
no exponga.

### 4. `trazar-camino-critico`

Identificar el siguiente paso que desbloquea el resultado. Mantenerlo en la
sesión directora cuando delegarlo obligaría a esperar sin trabajo local útil.
Delegar sidecars concretos que puedan avanzar de forma independiente.

### 5. Decidir si sessionizar

Leer [session-graph-matrix.md](referencias/session-graph-matrix.md) y puntuar
`D,K,P,M,W,J,L,I` solo si existe valor plausible de delegación.

Crear sesiones cuando `D ≥ 2`, `K ≥ 2` y además se cumple al menos una:
`P ≥ 2`, `L ≥ 2`, o `B ≥ 3` con valor real de aislar contexto.

No dividir si el ajuste mutuo sería continuo, los write sets se solapan, no
existen entregables independientes o integrar costaría más que ejecutar.

Cada nodo delegado debe producir algo concreto, delimitado, necesario,
verificable y no duplicado.

### 6. `construir-grafos`

Representar la ruta como:

```text
Γ = (V, T_g, D_t, M_c, W_f, Θ)
```

- `V`: sesiones.
- `T_g`: árbol de creación, supervisión y autoridad.
- `D_t`: DAG de dependencias de trabajo.
- `M_c`: aristas de comunicación autorizadas.
- `W_f`: interferencia posible entre write sets o estado externo.
- `Θ`: rol, modelo, esfuerzo, contexto, permisos, persistencia, presupuesto,
  entregable y verificación de cada nodo.

Invariantes:

1. Con más de una sesión, mantener un árbol de gobierno explícito.
2. `D_t` es acíclico por defecto. Dependencia mutua continua indica nodos mal
   separados: fusionar o serializar.
3. Mantener `M_c ⊆ D_t ∪ E_review`. Prohibir broadcast ambiental.
4. La mensajería coordina información; no sincroniza escrituras.
5. La directora conserva objetivo, alcance, presupuesto, riesgo, decisiones,
   integración y aceptación final.

### 7. Elegir topología

Leer [topology-catalog.md](referencias/topology-catalog.md). Elegir una base
S0–S9 y modificarla solo por una dependencia observable.

Preferencias:

```text
S0 antes que grafo
S1 antes que estrella
estrella antes que DAG
DAG antes que árbol profundo
un escritor antes que escritores federados
```

### 8. Definir comunicación, contexto y escritura

Leer [communication-protocol.md](referencias/communication-protocol.md) si hay
mensajería lateral, reuso de sesiones, delegación recursiva o más de un
escritor.

Por defecto:

- `fork_turns: none` para un paquete acotado;
- heredar contexto solo cuando la tarea depende realmente de él;
- resultados destilados, no logs crudos;
- una ronda lateral de aclaración;
- máximo inicial conservador de tres hijas concurrentes y profundidad dos,
  ajustable a los límites vivos y al problema;
- un worktree por dominio independiente de escritura, no por sesión.

No crear worktrees para lectura, revisión, hipótesis, mappers ni un único
escritor.

### 9. Aplicar modificadores de dominio

Leer [domain-overrides.md](referencias/domain-overrides.md) solo para dominios
de alta consecuencia, independencia epistemológica o topologías conocidas.
Los modificadores estrechan la ruta; no sustituyen CEM-8, SGM-8 ni autoridad
humana.

### 10. `enrutar`: emitir la ruta

Para `GRAPH_ROUTE`, emitir como mínimo:

```yaml
ROUTE:
  mode: route-only | route-and-run
  task_profile: {A: 0, N: 0, E: 0, O: 0, B: 0, C: 0, H: 0, R: 0}
  session_profile: {D: 0, K: 0, P: 0, M: 0, W: 0, J: 0, L: 0, I: 0}
  critical_path: texto
  director:
    session: /root
    model: actual | recomendado
    effort: actual | recomendado
    authority: [objective, scope, contracts, budget, risk, integration]
  topology: {code: S0, name: monosession, delegation: explicit}
  sessions: []
  dependencies: []
  communication:
    default: director-mediated
    peer_edges: []
    broadcast: forbidden
  context: {default_fork: none, delivery: bounded-task-packet}
  execution: {max_concurrency: 1, max_depth: 0, worktrees: []}
  autonomy: {allowed: [], confirm: []}
  stop_conditions: []
  escalation: []
  verification: []
  confidence: low | medium | high
  evidence_status: proposed
```

Omit campos vacíos que no ayuden a decidir, salvo que el usuario solicite el
schema completo.

### 11. `ejecutar`: materializar solo en `route-and-run`

Antes de crear cada sesión, verificar:

- que la solicitud o una instrucción aplicable autoriza subagentes;
- que el subtrabajo es independiente y acotado;
- que hay un slot útil disponible;
- que el paquete declara objetivo, ownership, aceptación, autoridad,
  restricciones y salida esperada;
- que escrituras paralelas no solapan archivos ni estado.

Usar únicamente las operaciones y valores expuestos por el runtime actual. No
inventar herramientas ni crear perfiles de agentes, worktrees o ramas que la
ruta no necesite. Continuar trabajo local no solapado mientras las sesiones
avanzan. Esperar solo si el camino crítico está realmente bloqueado.

### 12. `integrar`, `verificar`, `cerrar`

Evaluar los resultados delegados antes de incorporarlos. Resolver
contradicciones en la directora, verificar el objetivo global sobre el
candidato integrado y distinguir `PASS`, `FAIL`, `ABSENT` y `NOT_RUN`.

Interrumpir o redirigir cuando cambie el alcance, aumente el blast radius, se
solapen write sets o la comunicación se vuelva continua. Reutilizar una sesión
solo si su contexto local sigue vigente. Cerrar el trabajo cuando el criterio
de aceptación esté satisfecho; no crear recibos, dashboards ni tareas para
demostrar actividad.

## Límites de evidencia

- CEM-8, SGM-8 y S0–S9 son una rúbrica de ingeniería, no una escala predictiva
  validada. Leer [calibration.md](referencias/calibration.md) al evaluar o
  modificar la rúbrica.
- Una topología propuesta no prueba que el runtime la ejecutó.
- Sesiones creadas no prueban delegación correcta; exigir paquete, autoridad,
  resultado e integración.
- Paridad de archivos o configuración no prueba conducta, seguridad, menor
  costo, aceptación humana ni calidad superior.
- «Persistente» significa reutilizable dentro de la vida observada de la
  sesión/runtime; no implica memoria durable entre tareas salvo evidencia
  explícita.
