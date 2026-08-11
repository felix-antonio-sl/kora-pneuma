# Superficies de ejecución Codex

## Unidad de ruta

Modelo y esfuerzo no bastan: la disponibilidad, el aislamiento, la propiedad y
el costo de coordinación cambian según la superficie.

```text
route_candidate = (execution_surface, model, effort)
execution_surface = current_session | subagent | independent_thread
```

Evaluar el triple completo. Un par modelo–esfuerzo disponible en una superficie
no se presume disponible en otra. Si el runtime no expone una capacidad,
registrarla como `unknown` o `unavailable`, nunca inferirla por catálogo.

## Catálogo

| Superficie | Usarla cuando | Propiedad y límite |
|---|---|---|
| `current_session` | S0, camino crítico, integración intensa o una sola unidad de decisión | conserva contexto y autoridad en la directora; no crea sesión |
| `subagent` | subtrabajo acotado, resultado devuelto a la directora y lifecycle breve | descendiente de la sesión actual; solo modelos y esfuerzos expuestos por `spawn_agent` |
| `independent_thread` | resultado independiente, durable o en segundo plano; aislamiento de contexto; o par no expuesto a subagentes | thread Codex de propiedad del usuario, visible en su lista de tareas y dirigido por la sesión directora |

La sesión independiente es de primera clase, no un fallback informal. Puede
hacer ejecutable a Luna Max cuando la superficie de subagentes no la expone;
esa disponibilidad debe comprobarse en vivo. No elegirla solo para acceder a un
par barato si la coordinación, la integración o el seguimiento borran la
ventaja.

## Autoridad para threads independientes

- `route-only` propone; nunca llama `create_thread`. La falta de autoridad de
  creación no elimina la candidata en route-only; separar recomendación de activación y registrar `not_authorized`.
- `route-and-run` genérico tampoco basta para crear un thread de propiedad del
  usuario: se requiere una solicitud explícita de crear, abrir o ejecutar en
  una sesión independiente o en segundo plano.
- Autorizar el thread no autoriza fijar su modelo: el usuario debe pedir ese
  modelo concreto. Si no lo hace, `model_override_not_authorized` y no crear el
  thread; no omitir el override para heredar un default fuera de la allowlist.
- Antes de `create_thread`, usar `list_projects` y resolver el proyecto exacto.
- Un thread creado queda bajo propiedad del usuario. La directora puede
  observarlo y dirigirlo, pero no archivar automáticamente al terminar.
- `fork_thread` exige una solicitud explícita de bifurcar un thread existente;
  no sustituye la creación normal de un trabajo nuevo.

## Checkout local o worktree

Elegir el target por interferencia real de escritura:

```text
solo lectura o un único escritor sin concurrencia → checkout local
escritor independiente concurrente con riesgo de interferencia → worktree
interfaces o write sets solapados → serializar, no ocultar el conflicto
```

Un worktree se asigna por dominio independiente de escritura, no por thread.
Confirmar proyecto, rama/base, ownership y aceptación antes de crear una ruta
con escritura.

## Preflight y dirección

Para `independent_thread`, comprobar en vivo:

```yaml
thread_surface:
  create_available: true | false
  project_resolved: true | false
  available_models: []
  available_efforts: []
  local_target_available: true | false
  worktree_target_available: true | false
  creation_authorized: true | false
  model_override_authorized: true | false
```

Operaciones canónicas:

- `create_thread`: crear solo con `creation_authorized` y
  `model_override_authorized`, modelo concreto y esfuerzo fijados;
- `list_projects`: resolver el destino antes de crear;
- `list_threads`: observar threads del alcance autorizado;
- `read_thread`: inspeccionar progreso y evidencia;
- `send_message_to_thread`: entregar contrato, corrección o seguimiento;
- `set_thread_title` y `set_thread_pinned`: solo si el encargo lo requiere;
- `set_thread_archived`: solo por solicitud del usuario, nunca como cierre
  automático.

La directora conserva objetivo global, adjudicación e integración. El thread
recibe el mismo contrato observable que un subagente y devuelve resultado,
evidencia, límites y estado. Su lifecycle no se confunde con el de un
descendiente: que el trabajo termine no transfiere propiedad ni autoriza
archivarlo.

## Regla de elección

Elegir la superficie más simple que satisfaga aceptación. Preferir
`current_session` si la separación no reduce tiempo, riesgo, contaminación o
incertidumbre; `subagent` para sidecars breves dentro de la orquestación viva;
`independent_thread` cuando su aislamiento, durabilidad, ejecución en segundo
plano o acceso comprobado al triple recomendado compensa el costo de dirección.

## Fuentes

[Projects and chats](https://learn.chatgpt.com/docs/projects) y [Worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees).
