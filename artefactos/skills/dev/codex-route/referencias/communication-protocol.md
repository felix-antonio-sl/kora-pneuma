# Comunicación, contexto, escritura y control

## Principio

```text
la capacidad de comunicarse no implica que deban comunicarse
```

Autorizar una arista lateral solo si existe dependencia explícita, el dato no
cabía razonablemente en el paquete inicial, la respuesta puede cambiar el
trabajo receptor, la retransmisión central perdería precisión o tiempo y el
intercambio puede mantenerse acotado.

## Tipos de mensaje

```text
ASK
CONTRACT
EVIDENCE
BLOCKER
RESULT
CHALLENGE
DECISION
```

Formato:

```text
TYPE | petición o afirmación | evidencia o referencia | impacto | qué bloquea
```

Solo la directora emite `DECISION` sobre objetivo, alcance, interfaces
globales, presupuesto, riesgo y aceptación final.

No habilitar mensajería lateral para actualizaciones periódicas, conversación
general, consenso previo a una evaluación independiente, compartir todas las
notas, compensar una mala descomposición o sincronizar archivos.

## Paquete de sesión

Toda sesión delegada recibe:

```yaml
task_name: slug
role: responsabilidad local
objective: resultado local
inputs: []
source_of_truth: []
scope: []
non_scope: []
deliverable: []
verification: []
write_set: none | []
allowed_actions: []
allowed_message_edges: []
stop_conditions: []
escalation_conditions: []
authority: []
```

Para una sesión que escribe, añadir explícitamente: workspace, candidato,
ownership exclusivo, criterios de aceptación y prohibición de revertir cambios
ajenos.

## Contexto

La directora conserva objetivo global, restricciones, aceptación, decisiones,
contratos, riesgos, grafo, presupuesto y estado resumido.

Por defecto, usar `fork_turns: none` y entregar el paquete mínimo. Usar
`fork_turns: all` solo cuando la conversación completa sea una entrada
load-bearing. Si el nodo necesita siempre todo el contexto, su separabilidad
`K` es baja y probablemente no debe delegarse.

Una sesión devuelve conclusión, evidencia, incertidumbre, impacto, archivos o
artefactos modificados, verificaciones y bloqueos. No devuelve la narración
completa ni logs crudos salvo que sean el artefacto solicitado.

## Operaciones vivas

Usar solo las herramientas expuestas en la sesión actual:

- `spawn_agent`: crear una sesión para una tarea concreta e independiente;
- `send_message`: entregar información sin iniciar por sí sola una nueva
  tarea;
- `followup_task`: asignar trabajo nuevo a una sesión existente;
- `wait_agent`: esperar solo cuando el camino crítico esté bloqueado;
- `list_agents`: inspeccionar sesiones vivas y slots;
- `interrupt_agent`: detener el turno actual para redirigir o contener riesgo.

No inventar `close_agent` ni otra llamada ausente. Si el runtime ofrece una
capacidad adicional, verificar su contrato vivo antes de usarla.

## Concurrencia y profundidad

Default conservador inicial:

```text
máximo 3 sesiones hijas concurrentes
profundidad normal máxima 2
una ronda lateral de aclaraciones
```

Son heurísticas, no límites oficiales. Reducirlas ante integración difícil,
escritura o riesgo; ampliarlas solo si existen slots, independencia y valor de
tiempo de pared.

No esperar de forma refleja. Mientras un descendiente trabaja, continuar el
camino local no solapado.

## Escritura y worktrees

`W_f` modela interferencia; la mensajería no da exclusión mutua.

No requieren worktree: lectura, revisión, mappers, hipótesis, arquitectura,
adjudicación o un único escritor.

Pueden requerirlo: escritores simultáneos con dominios disjuntos, ramas
especulativas, implementaciones alternativas o cambios descartables por
separado.

Regla:

```text
un worktree por dominio independiente de escritura
no un worktree por sesión
```

Mantener un integrador único y pruebas de contrato. Si los write sets dejan de
ser disjuntos, detener S9 y volver a un escritor o serializar.

## Autonomía

Acciones locales normales dentro de autoridad: leer, buscar, analizar, crear
sesiones autorizadas, enviar mensajes contractuales, editar dentro de
ownership, ejecutar pruebas no destructivas, reparar fallos locales e integrar.

Exigir confirmación para despliegue no autorizado, escritura externa,
migración productiva, eliminación irreversible, gasto extraordinario, cambio
material de alcance, comunicación externa, decisión clínica aplicada o acción
legal/financiera.

Los descendientes no reciben más autoridad que la sesión directora. Las
permisiones y overrides vivos del runtime prevalecen sobre el contrato textual.

## Condiciones de detención

- aceptación satisfecha;
- presupuesto o límite de iteraciones agotado;
- fallos causales equivalentes repetidos;
- oráculo indisponible;
- dependencias contradictorias;
- blast radius mayor al previsto;
- write sets ya no disjuntos;
- comunicación continua;
- efecto externo o irreversible emergente;
- nueva evidencia invalida el contrato.

Al detener, devolver estado, evidencia y decisión mínima: continuar,
redirigir, fusionar, serializar o bloquear.
