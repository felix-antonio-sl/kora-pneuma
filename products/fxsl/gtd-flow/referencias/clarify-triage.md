# Clarify-triage protocol

Procesamiento item por item del INBOX. **Capturar y triage estan
separados.** Capturar acepta sin juicio; triage aplica preguntas.

## Preguntas de triage en orden

Para cada item:

### 1. Que es?

Nombrar la naturaleza: idea, recordatorio, compromiso, sentimiento,
referencia, ruido. Si no se puede nombrar, es candidato a archivar
(reference) o descartar.

### 2. Que capa es?

| Capa | Senales |
|---|---|
| **Regulacion** | Lenguaje emocional, cuerpo, energia, amenaza identitaria |
| **Operacion** | Tarea, compromiso, output, resultado |
| **Generacion** | Vision, sentido, direccion, valores, identidad |

Sin esta clasificacion el item se pierde.

### 3. Requiere accion?

- **Si**: continuar al paso 4.
- **No**: ir a `reference` (util tener), `someday/maybe` (quiza si),
  o descartar.

### 4. Cual es el outcome?

Que pasa cuando esto este hecho? **Verificable**, no vago.

- Vago: "trabajar en X"
- Verificable: "X publicado en Y con criterio Z"

### 5. Cual es la next action visible?

El paso fisico, ejecutable, concreto.

- Vago: "pensar en X"
- Visible: "abrir doc X, leer hasta seccion Y"

### 6. Quien es el owner correcto?

| Owner | Bucket destino |
|---|---|
| Yo, ahora o pronto | `next actions` |
| Yo, fecha fija | `calendar` |
| Yo, multiples acciones encadenadas | `projects` |
| Humano | `waiting for humans` |
| Agente | `waiting for agents` |

### 7. Que review lo vuelve confiable?

Cadencia de check para el item:

- compromisos rapidos: revision diaria
- proyectos: revision semanal
- delegaciones: revision al deadline + 1 dia
- vision/anti-vision: revision mensual o trimestral

## Decisiones rapidas

Si el item:

| Tarda menos de 2 minutos | hacerlo ahora, no clasificar |
| Es ruido (no aplica) | descartar |
| Es referencia util | `reference` con tags |
| Tiene fecha vinculante | `calendar` |
| Es delegable | preparar contrato de delegacion (ver `contrato-delegacion.md`) |
| Es ambiguo despues de triage | volver al operador con pregunta puntual |

## Reglas

- **Captura no juzga**; clasificacion juzga.
- **Outcome-owner-review** completos antes de soltar el item.
- **Si despues de 2 intentos** el item sigue ambiguo, devolverlo al
  operador con pregunta concreta (no especular).
- **Costo psiquico minimo**: si clasificar el item esta agotando, hay
  algo emocional debajo — escalar a `recuperar-estado`.

## Antipatrones

| Antipatron | Falla | Correccion |
|---|---|---|
| Triage sin clarificar | Items sin outcome ni owner van a buckets | Completar las 7 preguntas |
| Outcome vago | "Trabajar en X" | Verificable: que cambia cuando este hecho |
| Next action no visible | "Pensar en Y" | Paso fisico, ejecutable, concreto |
| Triage como ritual | Procesar todo aunque sea ruido | Descartar sin culpa |
| Mezcla capas | Items emocionales como tarea | Diagnosticar capa primero |
