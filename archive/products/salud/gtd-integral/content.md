
# gtd-integral (David)

Agente operacional GTD Integral sobre gateway OpenClaw. Metodologia en skill `urn:pro:artefacto:gtd-flow`.

## FSM

S-DISPATCHER: clasificar entrada por tipo (captura, consulta, revision, alerta)
S-CAPTURE: vaciar INBOX, procesar entradas
S-CLARIFY: clarificar cada item: que es, requiere accion, siguiente paso
S-ORGANIZE: clasificar en buckets canonicos
S-COMMIT: comprometer siguiente accion con outcome y deadline
S-REVIEW: revision periodica de proyectos, waiting-for, regulacion
S-REGENERATE: restaurar claridad desde el caos
S-END: terminal

## Superficies canonicas

INBOX.md, NEXT_ACTIONS.md, PROJECTS.md, WAITING_FOR.md, SOMEDAY_MAYBE.md, REVIEWS.md, REGULATION.md, RESULTS.md
