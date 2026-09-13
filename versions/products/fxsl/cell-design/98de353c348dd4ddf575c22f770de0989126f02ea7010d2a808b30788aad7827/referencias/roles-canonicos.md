# Funciones configurables de una celula humano-agente

Estas funciones ayudan a conservar decisiones distintas. No son cargos, un
organigrama ni un conjunto obligatorio. Pueden combinarse, repartirse entre
personas y agentes existentes u omitirse cuando su decision no aplica.

| Funcion | Decision que conserva | Portadores posibles |
|---|---|---|
| Arquitectura de intencion | Problema, beneficiario, resultado y criterio de cierre | responsable de producto, lider tecnico, operador |
| Curacion de autonomia | Frontera de accion, permisos, escalamiento y respuesta a falla | responsable operativo, plataforma, operador |
| Ingenieria de evaluacion | Evidencia que confirma o refuta el resultado | QA, SRE, revisor, agente especializado |
| Experiencia de dominio | Contexto, restricciones y consecuencias del dominio | experto, fuente primaria, usuario autorizado |
| Integracion del resultado | Reune aportes y sostiene el cierre | una persona o agente con mandato |

## Reglas operativas

1. Distinguir responsabilidad, autoridad y capacidad aunque compartan portador.
2. Separar autor y evaluador cuando la independencia cambie materialmente la
   confianza; si no se separan, declarar el limite.
3. El contexto experto puede errar. Para afirmaciones materiales, comprobar
   fuente, vigencia y alcance; ante tension, conservar el disenso.
4. La autoridad proviene del encargo o de quien puede concederla, no del titulo
   de una funcion.
5. No crear un portador nuevo si la funcion cabe en una responsabilidad vigente.

## Asignacion proporcional

| Artefacto | Funciones que suelen aportar | Autoridad de cierre |
|---|---|---|
| Diseno de celula | intencion, autonomia, integracion | la definida por el encargo |
| Intent contract | intencion, integracion, dominio si aplica | beneficiario o delegado autorizado |
| Autonomy envelope | autonomia, integracion | autoridad sobre los efectos |
| Diseno de evidencia | evaluacion, dominio, intencion | quien acepta el resultado |
| Debt audit | cualquiera que aporte evidencia | responsable del alcance |
| Recalibracion | funciones afectadas | responsable de la operacion |

“Stakeholder”, “curador” o “arquitecto” son nombres utiles si aclaran una
decision. Cambiarlos o no usarlos no degrada el diseno cuando las decisiones y
responsabilidades siguen resolubles.
