# Roles canonicos en una celula humano-agente

Roles que la skill reconoce y asigna. Un individuo puede portar varios;
el sistema maduro **no confunde** portar varios sombreros con ausencia
de separacion logica.

## Tabla canonica

| Rol | Funcion | Portador tipico |
|---|---|---|
| **Arquitecto de intencion** | Define problema, beneficiario, beneficio, criterio de exito | PM / Tech Lead |
| **Curador de autonomia** | Disena limites, permisos, topologias, routing, rollback | Platform Engineer / Ops |
| **Ingeniero de evaluacion** | Convierte exito esperado en test, eval, dataset, policy checks | QA / SRE / agente especializado |
| **Stakeholder experto** | Aporta conocimiento de dominio irreductible | Humano con contexto irreducible |
| **Celula humano-agente** | Unidad real de entrega | Equipo estable |

## Reglas operativas

1. **Separacion logica preservada**: aunque una persona porte varios
   roles, los outputs de cada rol deben ser distinguibles.
2. **Anti-confusion**: el "arquitecto de intencion" no es lo mismo que
   el "ingeniero de evaluacion". Si una sola persona los porta, debe
   declarar desde que sombrero opera en cada decision.
3. **Stakeholders expertos**: su contexto es **irreducible**; no se
   comoditiza. Cuando aparece tension, su input prevalece sobre el
   agente.
4. **Curador de autonomia >= todos los agentes**: ningun agente puede
   tener autonomia mayor que la capacidad del curador para auditar.

## Quien hace que en cada artefacto

| Artefacto | Quien lo produce | Quien lo aprueba |
|---|---|---|
| Diseno de celula | Arquitecto + Curador | Stakeholders + humano del PM |
| Intent contract | Arquitecto de intencion | Beneficiario o su representante |
| Autonomy envelope | Curador de autonomia | Arquitecto + humano de control plane |
| Eval architecture | Ingeniero de evaluacion | Curador + Arquitecto |
| Debt audit | Cualquier rol que detecte | Curador (decide remediacion) |
| Recalibration plan | Celula completa | Arquitecto |

## Antipatrones

| Antipatron | Falla | Correccion |
|---|---|---|
| Roles ausentes | Celula sin curador → autonomia salvaje | Asignar curador antes de delegar |
| Auto-evaluacion del autor | Autor == evaluador | Ingeniero de evaluacion separado |
| Stakeholder ignorado | Decision contradice contexto de dominio | Tratar input del experto como irreducible |
| Confusion de sombreros | Portar varios sin distinguir | Declarar desde que rol opera cada decision |
| Curador sin autoridad | Curador sin poder de gateo | Curador necesita autoridad real, no solo titulo |
