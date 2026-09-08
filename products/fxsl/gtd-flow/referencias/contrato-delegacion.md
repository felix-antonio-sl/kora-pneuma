# Contrato de delegacion

Toda delegacion **valida** explicita seis elementos. Si falta uno, la
delegacion esta **incompleta**: devolverla al operador para completar.

## Formato canonico

```
## Delegation: {titulo}
- outcome: {que resultado se espera}
- owner: {quien ejecuta — humano (nombre) o agente (URN/id)}
- limites: {que NO hacer}
- review: {cuando y como verificar}
- deadline: {fecha o condicion de retorno}
- failure mode: {que pasa si falla}
```

## Distincion critica

`waiting for humans` ≠ `waiting for agents`.

| Tipo | Requisitos adicionales |
|---|---|
| **Delegacion humana** | Compromiso explicito del receptor, contexto suficiente, canal de seguimiento, disposicion del receptor a recibir review |
| **Delegacion agentica** | Gating tecnico (que puede / que no puede), auditoria habilitada, rollback documentado, autonomy envelope vigente |

## Reglas

1. **Outcome verificable**: que cambia cuando esto este hecho? No
   "trabajar en X" — debe ser comprobable.
2. **Owner unico**: si hay dos owners, la delegacion fragmentara.
   Designar uno con autoridad y otros como apoyo.
3. **Limites explicitos**: lo prohibido es tan importante como lo
   permitido. Sin limites, "delegar criterio".
4. **Review concreto**: dia + hora + criterio. "Reviso luego" no es
   review.
5. **Deadline o condicion de retorno**: sin deadline el item se vuelve
   agujero negro.
6. **Failure mode**: que pasa si la delegacion falla? Quien retoma?
   Hay rollback?

## Para delegaciones agenticas — adicional

| Requisito | Por que |
|---|---|
| Autonomy envelope vigente | Sin envelope la autonomia es indefinida |
| Logs de la accion | Si no se ve, no se gobierna |
| Rollback probado | Si no se puede revertir, no es delegacion responsable |
| Eval automatizado | Sin eval, el done es opinion del agente |
| Visibilidad >= autonomia | A mas autonomia, mas observabilidad |

Si el agente no esta en estas condiciones, **no es delegable** todavia.
Mejorar las condiciones primero.

## Para delegaciones humanas — adicional

| Requisito | Por que |
|---|---|
| Compromiso explicito | Sin "si, lo hago", no hay delegacion |
| Contexto suficiente | El humano necesita saber para que es y que decisiones puede tomar |
| Canal de seguimiento | Como se va a verificar el avance? |
| Disposicion a review | Si el humano se ofende con review, la delegacion no es estable |

## Antipatrones

| Antipatron | Falla | Correccion |
|---|---|---|
| Delegacion implicita | "Asumi que lo iba a hacer" | Compromiso explicito |
| Outcome vago | "Que se haga lo de X" | Verificable |
| Sin deadline | "Cuando puedas" | Fecha o condicion |
| Sin limites | Delegar criterio sin querer | Lo prohibido tan claro como lo permitido |
| Review imaginario | "Reviso luego" | Concreto: dia + hora + criterio |
| Failure mode oculto | "Si falla ya veremos" | Rollback / quien retoma / como se mitiga |
| Agente sin envelope | Delegar a agente sin auditoria | Configurar envelope antes de delegar |
| Humano no consultado | Delegar sin "si, lo hago" | Verificar compromiso |

## Verificacion antes de soltar

Antes de marcar la delegacion como activa:

- [ ] outcome verificable
- [ ] owner unico con autoridad real
- [ ] limites explicitos
- [ ] review concreto (dia + criterio)
- [ ] deadline o condicion
- [ ] failure mode declarado
- [ ] (humana) compromiso del receptor
- [ ] (agentica) envelope vigente + logs + rollback
