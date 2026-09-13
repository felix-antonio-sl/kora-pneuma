# Formatos adaptables de diseno organizacional

Usar solo el formato que evita una ambiguedad o conserva una decision. Se pueden
reducir, combinar o extender si se preservan proposito, responsabilidad,
autoridad, evidencia y respuesta a falla.

## Diseno de celula

```
## Celula: {nombre o alcance}
- Proposito y beneficiario: {resultado / quien}
- Horizonte: {temporal o sostenido}
- Trabajo e interfaces: {entradas, decisiones, salidas, traspasos}
- Funciones y portadores: {responsabilidad / persona o agente}
- Autoridad: {puede decidir / debe escalar / fuera de alcance}
- Evidencia: {como se reconoce el resultado}
- Riesgo y respuesta a falla: {prevencion, contencion, recuperacion}
- Revision: {evento o cadencia justificada}
```

Agregar memoria, logs, metricas o control plane solo si la continuidad y el
riesgo los necesitan y existe un lugar autorizado.

## Intent Contract

```
## Intent Contract: {titulo}
- Beneficiario y cambio: {quien / que cambia}
- Resultado suficiente: {criterios verificables}
- Entradas y supuestos: {minimos}
- Puede decidir: {acciones autorizadas}
- Requiere otra autoridad: {efectos}
- Fuera de alcance: {limites}
- Evidencia: {prueba, revision, caso, observacion o fuente}
- Riesgo y recuperacion: {respuesta viable}
```

## Autonomy Envelope

```
## Autonomy Envelope: {funcion}
- Puede hacer: {frontera autorizada}
- Debe escalar: {condiciones}
- No puede hacer: {prohibiciones}
- Evidencia y visibilidad: {solo lo necesario}
- Ante falla: {contencion, recuperacion o rollback posible}
- Revision: {trigger o cadencia justificada}
```

## Debt Audit

```
## Debt Audit: {alcance}
| Lente | Senal | Evidencia | Consecuencia | Confianza | Accion |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |
```

## Recalibracion

```
## Recalibracion: {alcance}
- Motivo: {cambio o senal}
- Proposito vigente: {si/no y evidencia}
- Responsabilidades e interfaces: {ajustes}
- Autoridad y capacidad: {ajustes}
- Evidencia: {sigue discriminando?}
- Riesgo y recuperacion: {ajustes}
- Siguiente revision: {evento o cadencia con razon}
```

## Reglas de uso

- No es obligatorio llenar todos los formatos ni campos.
- Un campo omitido que pueda cambiar autoridad, seguridad o cierre debe
  explicitarse como pendiente.
- Los criterios deben poder comprobarse de forma proporcional.
- Una severidad necesita consecuencia y evidencia, no intuicion.
- No volver a pedir una autoridad que el encargo ya concede.
