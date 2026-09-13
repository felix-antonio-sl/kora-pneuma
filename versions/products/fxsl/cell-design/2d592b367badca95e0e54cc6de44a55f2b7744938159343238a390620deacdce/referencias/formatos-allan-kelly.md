# Formatos canonicos Allan Kelly

Plantillas de salida por tipo de solicitud. Mantener fidelidad al
formato; lo estructurado es legible y auditable.

## Diseno de celula

```
## Celula: {nombre}
- Proposito: {outcome esperado}
- Beneficiario: {quien recibe valor}
- Humanos: {roles × personas}
- Agentes: {nombre × capacidad × limites}
- Memoria: {que persiste × donde × cadencia de poda}
- Evals: {que se testea × quien evalua × datos × frecuencia}
- Control plane: {que se ve × donde × frecuencia}
- Rollback: {por flujo × mecanismo}
- Deuda conocida: {eval/context/autonomy/observability}
- Cadencia de recalibracion: {frecuencia}
```

## Intent Contract

```
## Intent Contract: {titulo}
- Beneficiario: {quien}
- Cambio deseado: {que cambia}
- Beneficio esperado: {por que importa}
- Criterios de aceptacion: {lista testable}
- Evals minimos: {que se evalua automaticamente}
- Limites de autonomia: {que puede hacer el agente sin preguntar}
- Aprobacion humana requerida: {para que pasos}
- Riesgo y rollback: {que puede salir mal y como se revierte}
```

## Autonomy Envelope

```
## Autonomy Envelope: {agente o funcion}
- Puede sin preguntar: {acciones libres}
- Requiere aprobacion: {acciones gateadas}
- Prohibido: {acciones bloqueadas}
- Reversion: {mecanismo de rollback}
- Observabilidad: {que se loguea y donde se ve}
- Cadencia de review: {cada cuanto se revisa el envelope}
```

## Debt Audit

```
## Debt Audit: {scope}
| Tipo | Hallazgo | Severidad | Accion sugerida |
|---|---|---|---|
| eval | {descripcion} | {H/M/L} | {recomendacion} |
| context | ... | ... | ... |
| autonomy | ... | ... | ... |
| observability | ... | ... | ... |
```

## Recalibration Plan

```
## Recalibration: {scope}
- Cadencia: {diaria/semanal/mensual/trimestral}
- Quien recalibra: {humano/celula completa}
- Que se evalua:
  - autonomia: limites siguen calzando con riesgo real?
  - memoria: hay que podar o promover entradas?
  - topologia: la asignacion de agentes sigue siendo optima?
  - evals: estamos midiendo lo que importa?
  - control plane: que falta visibilidad?
- Triggers de recalibracion fuera de cadencia: {sintomas que disparan revision}
```

## Reglas de uso

- **No improvisar formato**: estos son los canonicos. Cualquier desviacion
  debe declararse.
- **Si falta un campo**, marcar `pendiente` o `n/a` con razon. No omitir
  silenciosamente.
- **Lista testable**: no aceptar criterios de aceptacion vagos
  ("funciona bien"); deben ser verificables.
- **Severidad explicita**: H/M/L con razon, no por intuicion.
