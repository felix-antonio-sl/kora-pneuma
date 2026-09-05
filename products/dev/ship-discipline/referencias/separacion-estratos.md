# Separacion de estratos — humano vs agente

Que se delega a agentes ejecutores y que se reserva al humano.

## Tabla canonica

| Estrato | Responsable | Razon |
|---|---|---|
| Decidir **que construir**, como encaja, que dependencia usar, que schema aguanta el futuro, que se siente bien | **Humano** | Taste, product judgement, arquitectura — irreducibles |
| Escribir, transformar, mover, refactorizar, generar, probar, repetir hasta verde | **Agente** | Trabajo mecanico de alta velocidad |
| Evaluar si el resultado **cumple la intencion** | **Humano** (con soporte de evals automatizados) | Juicio de valor |
| Recalibrar autonomia, memoria, topologia, limites | **Celula completa** | Co-agencia |

## Lo irreducible humano

El agente **NO** sustituye estas funciones. Las **escala** y **consulta**:

- **Taste**: la frontera entre "suficiente" y "mal hecho"; entre
  "elegante" y "ostentoso"; entre "directo" y "ceremonial".
- **Product judgement**: que merece existir, que debe morir, en que
  invertir tiempo.
- **Architecture**: que dependencia usar, que schema aguanta el futuro,
  donde poner el boundary.
- **Dependency choice**: que biblioteca traer al proyecto, que evitar.
- **Schema evolution**: como evolucionar un schema sin romper consumidores.
- **Software feel**: el software debe sentirse correcto, no solo funcionar.

## Lo delegable

| Tarea | Delegable | Notas |
|---|---|---|
| Escribir codigo de implementacion guiado por spec | Si | Spec puede ser informal; intent claro |
| Refactorizar mecanicamente | Si | Si el refactor preserva semantica |
| Renombrar / mover archivos | Si | Si la regla es clara |
| Generar tests | Si | Especialmente unit y golden file |
| Generar codigo boilerplate | Si | CRUD, configs, scaffolding |
| Buscar informacion en docs / web | Si | Investigacion acotada |
| Ejecutar build / test / lint | Si | Loop closure mecanico |
| Triage de bugs | Parcial | Diagnostico si; decision de fix puede requerir humano |
| Diseno de arquitectura | No | Humano lidera; agente complementa |
| Eleccion de stack | No | Humano decide |

## Reglas de delegacion

1. **Delegar accion no es delegar criterio**. El agente ejecuta; el
   humano sostiene el sentido.
2. **Toda delegacion tiene rollback**. Si no se puede revertir, no es
   delegacion responsable.
3. **Visibilidad >= autonomia**. Cuanto mas autonomo el agente, mas
   visible debe ser su accion.
4. **Limite humano declarado**: cuando el cuello de botella es de
   autoridad, relacion, cuidado o presencia, **salir** del impulso de
   automatizar.

## Antipatrones

| Antipatron | Falla | Correccion |
|---|---|---|
| Delegar arquitectura | Agente decide schema sin humano | Humano lidera; agente propone |
| Delegar taste | Agente declara "esta bien" | Humano valida feel |
| Humano teclea implementacion | Subutilizacion de agentes | Delegar implementacion guiada |
| Humano lee todo el codigo generado | Desperdicio de atencion senior | Mirar puntos de leverage |
| Agente propone deps sin contexto | Mala eleccion estrategica | Humano decide deps; agente las usa |
