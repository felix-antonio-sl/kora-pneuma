# Cuatro lentes de deuda

Estas categorias ayudan a investigar fragilidad en una celula humano-agente.
Una senal abre una hipotesis; no prueba por si sola la deuda, su causa ni quien
es responsable. Aplicar solo los lentes pertinentes y registrar evidencia,
consecuencia y confianza.

## Deuda de evaluacion

La evidencia disponible no permite juzgar una afirmacion o resultado con la
confianza que su consecuencia exige.

**Senales posibles**

- pruebas verdes y fallas no cubiertas;
- criterios de exito ambiguos;
- autor y evaluador comparten sesgos decisivos;
- demos seleccionadas tratadas como representativas;
- usuarios observan un efecto que la evaluacion no mide.

**Contraste**

Precisar que afirmacion debe sostenerse, que podria refutarla y si la fuente de
evaluacion es suficientemente independiente. Autor igual a evaluador no es una
falla automatica: separar funciones cuando la independencia cambia la decision.

**Respuestas posibles**

- agregar un caso que discrimine el riesgo;
- usar revision independiente o una fuente distinta;
- observar uso autorizado;
- declarar el limite si no existe evidencia suficiente.

Datos reales son una opcion, no una obligacion. Usar sintesis, fixtures o fuentes
cuando basten; minimizar datos personales y clinicos.

## Deuda de contexto

Las fuentes que orientan la accion son insuficientes, obsoletas, contradictorias
o dificiles de localizar.

**Senales posibles**

- versiones o autoridades confundidas;
- instrucciones incompatibles sin precedencia;
- resultados inconsistentes por contexto faltante;
- material abundante que oculta la fuente decisiva.

**Contraste**

Localizar la afirmacion afectada y cotejar procedencia, vigencia y autoridad. El
tamano del contexto no diagnostica calidad.

**Respuestas posibles**

- podar duplicados sin perder excepciones;
- indexar o declarar la fuente vigente;
- conservar contradicciones y pedir la decision que falta;
- versionar junto al sistema cuando corresponda.

## Deuda de autonomia

La accion delegada no calza con la capacidad, autoridad o respuesta a falla
disponible.

**Senales posibles**

- nadie sabe quien puede decidir un efecto;
- revisiones humanas repetidas no agregan juicio;
- el agente actua fuera de su encargo;
- una falla carece de contencion o recuperacion adecuada.

**Contraste**

Comparar efecto, autoridad, capacidad efectiva y evidencia. Una accion
irreversible no invalida toda delegacion: puede requerir prevencion, ensayo,
segregacion o aprobacion antes del efecto. No prometer un rollback inexistente.

**Respuestas posibles**

- acotar la frontera de accion;
- asignar la decision a la autoridad correspondiente;
- automatizar controles que realmente discriminen;
- definir contencion y recuperacion proporcional.

## Deuda de observabilidad

Falta evidencia necesaria para comprender el estado o gobernar efectos
relevantes.

**Senales posibles**

- no puede reconstruirse una accion material;
- un resultado se declara sin comprobante;
- una falla recurrente no deja datos para contrastar causas;
- las metricas disponibles miden volumen y no el efecto en cuestion.

**Contraste**

Preguntar que decision cambiaria con la observacion. Ausencia de dashboard o
telemetria continua no es deuda si un recibo, prueba o consulta puntual basta.

**Respuestas posibles**

- emitir un recibo correlacionable;
- agregar logs o metricas acotadas;
- observar un hito o condicion de cierre;
- usar un control plane solo cuando hay operacion distribuida que gobernar.

## Auditoria conjunta

```
## Debt Audit: {alcance}
| Lente | Senal | Evidencia o contraevidencia | Consecuencia | Confianza | Accion |
|---|---|---|---|---|---|
| evaluacion | ... | ... | ... | alta/media/baja | ... |
```

No es obligatorio llenar las cuatro filas. Si una categoria no cambia el
diagnostico, omitirla. Priorizar por consecuencia y posibilidad de reducir
incertidumbre; revisar por eventos o cadencia justificada.

## Antipatrones

| Antipatron | Correccion |
|---|---|
| Etiquetar deuda desde un solo sintoma | Contrastar causas alternativas. |
| Convertir throughput sin outcome en culpa | Tratarlo como senal y revisar metrica, horizonte y valor. |
| Exigir mas evals para todo | Elegir la comprobacion que cambia la decision. |
| Exigir rollback para lo irreversible | Disenar prevencion, limite y autoridad previa. |
| Exigir dashboard a todo agente | Usar visibilidad proporcional a efecto y coordinacion. |
