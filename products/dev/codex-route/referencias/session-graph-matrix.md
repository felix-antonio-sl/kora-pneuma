# SGM-8 — Session Graph Matrix

Aplicar solo si existe valor plausible de delegación. Decide sessionización,
comunicación, interferencia y persistencia; `J` alimenta después el esfuerzo de
integración de la directora.

| Dimensión | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| D — Descomponibilidad | Atómica | Sidecar opcional | 2–3 entregables | Varias unidades | Recursión natural |
| K — Separabilidad | Estado continuo | Casi todo el contexto | Contrato estable | Paquete acotado | Independiente |
| P — Holgura paralela | Serial | Marginal | Dos ramas útiles | Varias ramas | Fan-out amplio |
| M — Comunicación | Nada hasta resultado | Entrega final | Consultas acotadas | Coordinación iterativa | Ajuste continuo |
| W — Contención de escritura | Solo lectura | Un escritor | Write sets disjuntos | Solape parcial | Mismo estado vivo |
| J — Integración | Comprobar | Elegir/fusión simple | Sintetizar | Reconciliar interfaces | Consistencia global difícil |
| L — Valor de persistencia | Una tarea | Seguimiento breve | Varios ciclos | Especialista reutilizable | Programa acotado |
| I — Independencia epistémica | Compartida | Comunicación neutral | Primera pasada aislada | Candidatas cegadas | Contacto invalida comparación |

## Gate de sessionización

Crear sesiones si:

```text
D ≥ 2
K ≥ 2
y al menos una: P ≥ 2 · L ≥ 2 · B ≥ 3 con valor de aislar contexto
```

Cada sesión produce un entregable concreto, necesario, verificable y no
duplicado. Mantener el camino crítico en la directora si delegarlo impide todo
trabajo local útil.

## Contraindicaciones

No dividir con `K ≤ 1`, `M = 4`, `W ≥ 3`, o `P = 0 y L ≤ 1`; tampoco si el
costo de integrar supera el beneficio o todos tocarían las mismas interfaces.

## Persistencia local

| Nivel | Contrato | Uso |
|---|---|---|
| L0 desechable | crear → resultado → integrar → cerrar | búsqueda, mapper, crítica |
| L1 retenida | una o dos consultas | aclarar evidencia o revisar |
| L2 especialista | varios ciclos del mismo runtime | datos, seguridad, dominio |
| L3 supervisora | integra un subárbol dentro de autoridad local | sistema de sistemas |
| L4 programa acotado | objetivo, presupuesto, oracle, checkpoints, stop y rollback | solo con runtime y autoridad |

No prometer memoria cross-task. Si existe operación de cierre, liberar L0/L1
después de integrar; si no, declarar el límite de lifecycle.

## Independencia epistemológica

Con `I ≥ 2`, impedir comunicación entre candidatas hasta su primera entrega.
Después permitir una ronda dirigida de `CHALLENGE` si la adjudicación lo exige.

## Salida

Registrar los ocho enteros solo en `FULL_GRAPH_ROUTE` o cuando expliquen una
decisión fronteriza. El formato compacto declara la topología y los factores
que justifican crear, fusionar o serializar sesiones.
