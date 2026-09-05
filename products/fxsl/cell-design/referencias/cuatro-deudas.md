# Las cuatro deudas nuevas

Categorias de deuda que aparecen cuando humanos y agentes operan en
celula. Cada una tiene **senales** y **mitigaciones** especificas.

## Eval debt

Validacion fragil: no podes confiar en que el sistema funcione porque
las pruebas mienten o son insuficientes.

### Senales

- PRs verdes pero regresiones reales en produccion.
- Autor del codigo == autor del test.
- Datasets de eval pequenos, curados o sinteticos.
- Demos brillantes; produccion fragil (prompt theatre).
- Tests pasan pero los usuarios reportan problemas que no se cubren.

### Mitigacion

1. **Separar autor, evaluador y dataset** de los outputs criticos.
2. **Datasets reales**: usuarios reales, datos reales, casos de error
   reales. No solo happy path.
3. **Eval continuo**: no solo en CI; tambien en produccion (canary,
   shadow).
4. **Eval especificado en intent contract**: ningun done sin eval
   minimo declarado.

## Context debt

Contexto pobre, obsoleto o ambiguo que degrada el resultado del agente
sin senales claras.

### Senales

- Contextos enormes pero malos resultados.
- Agente se confunde sobre versiones, rutas, convenciones.
- Misma pregunta, distintas respuestas en sesiones distintas.
- Mucho tiempo perdido en aclarar lo basico.

### Mitigacion

1. **Podar**: el contexto sucio degrada; eliminar lo que no aporta.
2. **Estructurar**: AGENTS.md, CLAUDE.md, indices, plantillas.
3. **Refrescar**: lo que era cierto hace 6 meses puede ser falso ahora.
4. **Versionar**: el contexto cambia con el codigo; tratarlo como
   artefacto productivo.

## Autonomy debt

Delegacion sin limites claros, sin rollback, sin visibilidad. La
autonomia del agente excede la capacidad de auditarla.

### Senales

- Humanos agotados revisando cada output.
- Acciones del agente que no se pueden revertir.
- "El agente lo hizo, pero no se que hizo exactamente."
- Limites no escritos; cada caso decide ad-hoc.
- Rollback no probado o no documentado.

### Mitigacion

1. **Autonomy envelope explicito** por agente: lo permitido, lo gateado,
   lo prohibido.
2. **Rollback obligatorio**: si no se puede revertir, no es delegacion.
3. **Visibilidad >= autonomia**: a mas autonomia, mas observabilidad.
4. **Eval automatizado** sube al techo de la auditabilidad humana.

## Observability debt

Ejecucion sin visibilidad. El sistema corre pero no se ve.

### Senales

- "No se que hizo el agente ayer."
- Logs ausentes o ininterpretables.
- Metricas inexistentes o no actualizadas.
- Riesgo crece mas rapido que el monitoreo.
- Demos brillantes; falta de telemetria real.

### Mitigacion

1. **Control plane vivo**: dashboard, canal, logs estructurados.
2. **Logging por accion** del agente, no por turno.
3. **Metricas de outcome**, no solo de output.
4. **Cadencia de review** del control plane definida y respetada.

## Auditoria conjunta

Una celula sana **NO** acumula las cuatro deudas en silencio. La skill
produce una auditoria que las nombra:

```
## Debt Audit: {scope}
| Tipo | Hallazgo | Severidad | Accion sugerida |
|---|---|---|---|
| eval | autor == evaluador en X | H | Separar; agregar dataset Y |
| context | AGENTS.md desactualizado | M | Refresh + version |
| autonomy | sin rollback en flujo Z | H | Disenar reversion; gatear |
| observability | sin metricas de outcome | M | Definir 3 metricas core |
```

## Antipatrones

| Antipatron | Falla | Correccion |
|---|---|---|
| Negar deuda | "Todo bien" sin auditar | Auditoria periodica |
| Mezclar deudas | Tratar todo como un solo problema | Separar por tipo: cada una tiene mitigacion distinta |
| Solucion universal | "Mas evals" para todo | La mitigacion depende del tipo |
| Auditoria sin accion | Listar deuda sin priorizar | Severidad + accion sugerida |
