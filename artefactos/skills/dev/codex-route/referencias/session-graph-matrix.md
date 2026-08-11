# SGM-8 — Session Graph Matrix

Usar esta matriz solo cuando exista valor plausible de delegación. Decide si
crear sesiones, cuánta comunicación admitir y si la persistencia local vale su
costo.

| Dimensión | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| D — Descomponibilidad | Atómica | Sidecar opcional | 2–3 entregables distinguibles | Varias unidades delimitadas | Descomposición recursiva natural |
| K — Separabilidad del contexto | Estado compartido continuo | Casi toda la conversación | Contrato estable basta | Paquete acotado basta | Unidades independientes |
| P — Holgura paralela | Secuencia estricta | Paralelismo marginal | Dos ramas útiles | Varias ramas concurrentes | Map-reduce o fan-out amplio |
| M — Comunicación necesaria | Ninguna hasta resultado | Entrega final | Consultas ocasionales o contratos | Coordinación iterativa | Ajuste mutuo continuo |
| W — Contención de escritura | Solo lectura | Un escritor | Write sets disjuntos | Solapamiento parcial | Mismo estado vivo |
| J — Integración | Concatenar o comprobar | Elegir o fusionar simple | Sintetizar o normalizar | Reconciliar contradicciones o interfaces | Consistencia global difícil |
| L — Valor de persistencia | Una tarea y cierre | Seguimiento breve | Tareas posteriores probables | Especialista reutilizable varios ciclos | Programa autónomo acotado |
| I — Independencia epistemológica | Razonamiento compartido necesario | Comunicación neutral | Primera pasada independiente | Soluciones cegadas antes de síntesis | Comunicación temprana invalida la comparación |

## Gate de sessionización

Crear sesiones cuando:

```text
D ≥ 2
K ≥ 2
```

y además al menos una:

```text
P ≥ 2
L ≥ 2
B ≥ 3 y aislar contexto aporta valor
```

Cada sesión debe producir un entregable concreto, delimitado, necesario,
verificable y no duplicado.

## Contraindicaciones

No dividir cuando se cumple alguna:

```text
K ≤ 1
M = 4
W ≥ 3
P = 0 y L ≤ 1
```

O cuando cada sesión necesita a las demás continuamente, la directora debe
retransmitir todo, no hay entregables independientes, todos tocarían las mismas
abstracciones o el costo de integración supera el paralelismo.

Si el siguiente paso inmediato espera el resultado delegado y no queda trabajo
local útil, mantener ese paso en la directora.

## Persistencia local

| Nivel | Contrato | Uso |
|---|---|---|
| P0 desechable | crear → tarea → resultado → terminar | búsqueda, mapper, crítica puntual |
| P1 retenida | una o dos consultas posteriores | aclarar evidencia o revisar corrección |
| P2 especialista | varios ciclos dentro de la tarea/runtime | datos, seguridad, dominio clínico o regulatorio |
| P3 supervisora | puede integrar un subárbol | sistema de sistemas o corpus grande |
| P4 programa acotado | objetivo estable, presupuesto, oráculo, checkpoints, stop y rollback | solo si el runtime y la autoridad lo soportan |

No usar «persistente» como promesa de memoria cross-task. Verificar el alcance
real de vida y reuso de la sesión.

## Independencia epistemológica

Con `I ≥ 2`, impedir comunicación entre candidatas hasta su primera entrega.
Abrir después una ronda de `CHALLENGE` si un adjudicador la necesita. No pasar
a cada candidata las conclusiones o sospechas de las otras.

## Regla de salida

Registrar ocho enteros y explicar únicamente los factores que justifican
crear, no crear, fusionar o serializar sesiones.
