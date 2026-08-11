---
urn: urn:dev:artefacto:spec-driven-development
nombre: spec-driven-development
version: 1.0.0
estado: activo
descripcion: "Convierte ideas vagas, requisitos ambiguos o cambios con decisiones de arquitectura, schema, dependencias, boundaries o blast radius alto en una especificacion minima suficiente y una aceptacion observable antes de comprometer la implementacion. Usar al iniciar proyectos, features o cambios significativos cuando falta una fuente de Spec confiable; mantiene la Spec viva sin imponer documentos, tareas ni gates por ceremonia."
fuente: "Reescritura KORA de la skill externa spec-driven-development entregada por el operador el 2026-08-11 (sha256:e1fb4adb5712d2c246b356e283d4d153bbc06770a2a1610cc8e59db50a264d4b; autor y licencia no declarados). Preserva la explicitacion previa de objetivo, aceptacion, limites y supuestos; sustituye el workflow gated y los archivos obligatorios por especificacion proporcional, descubrimiento iterativo y una sola fuente de verdad."
autor: FS
creado: 2026-08-11
lang: es
tags: [dev, sdd, spec-driven-development, requisitos, aceptacion, arquitectura, antiburocracia]
vector: [2, 0, 2, 0, 1]
sigma: [2, 1, 3, 2, 1]
arnes: disciplina
forma: habilidad
herramientas: [Read, Write, Edit, Glob, Grep, Bash]
targets: [codex]
alcance: usuario
estados: [resolver-autoridad, calibrar, descubrir, especificar, decidir-gate, ejecutar, cerrar]
componible: [urn:dev:artefacto:ship-discipline, urn:dev:artefacto:code-review]
---

# spec-driven-development

## Finalidad

Convertir intención incierta en el **contrato mínimo ejecutable** que permita
construir sin adivinar. La Spec gobierna decisiones y aceptación; no es una
plantilla, una fase documental ni una licencia para congelar el aprendizaje.

La fuente de Spec puede ser la solicitud vigente, una issue, un PRD, el canon
del producto o un archivo del repositorio. Debe existir **una sola fuente
autoritaria por decisión**. Planes, tareas y resúmenes son vistas derivadas: no
compiten con ella.

Esta skill no reemplaza la autoridad de producto ni el `AGENTS.md` aplicable,
no obliga a escribir un archivo y no posterga una exploración reversible que
sea necesaria para entender el sistema.

## Flujo

### 1. Resolver la autoridad

1. Leer la solicitud y solo las reglas, Spec existentes y código necesarios
   para conocer el estado real.
2. Si el operador entrega `spec_source`, tratarla como fuente exacta: no
   sustituirla por una inferida ni duplicarla.
3. Separar:
   - **norma existente** — qué ya está decidido;
   - **alcance autorizado** — qué puede cambiar esta tarea;
   - **decisión abierta** — qué aún requiere descubrimiento o juicio humano.
4. Actualizar una fuente existente solo cuando sea canónica y la solicitud
   autorice el cambio. En otro caso, mantener el contrato en la tarea vigente.

### 2. Calibrar cuánta Spec hace falta

Elegir por incertidumbre, riesgo y vida útil; nunca por minutos o número de
archivos.

| Modo | Condición | Superficie mínima |
|---|---|---|
| `directo` | cambio inequívoco, reversible y de bajo riesgo | aceptación explícita en la tarea; devolver ejecución a `ship-discipline` |
| `micro-spec` | ambigüedad material o riesgo medio | contrato compacto en la tarea, issue o superficie ya activa |
| `durable` | arquitectura, schema, dependencias, boundaries, alto blast radius o varios incrementos/actores | fuente versionada en la ubicación que el repositorio ya gobierna |

No crear `tasks/plan.md`, `tasks/todo.md`, ADR, PRD ni carpeta `specs/` por
default. Crear una superficie durable solo si tendrá un consumidor real y no
existe ya otra autoridad.

### 3. Descubrir antes de fijar

Inspeccionar el sistema vivo antes de diseñar contra supuestos. Cuando falte
información que solo el código o un prototipo puede revelar, hacer el menor
spike reversible y etiquetarlo como **descubrimiento**, no como implementación
aceptada.

Clasificar cada afirmación relevante:

- `OBSERVADO` — respaldado por fuente o comportamiento leído;
- `INFERIDO` — conclusión provisional con evidencia citada;
- `ELEGIDO` — decisión de diseño que requiere autoridad.

Declarar los supuestos reversibles y continuar. Preguntar solo cuando una
respuesta cambie materialmente el resultado, el riesgo o la autoridad. No
cruzar una decisión irreversible con un supuesto pendiente.

### 4. Escribir la Spec mínima suficiente

Usar solo los campos que cambian la ejecución:

```text
spec_source: <fuente única o inline>
modo: micro-spec | durable
resultado: <qué comportamiento debe cambiar>
beneficiario: <para quién importa>
estado_observado: <evidencia actual pertinente>
alcance: <incluido>
no_objetivos: <exclusiones que evitan deriva>
aceptacion: <condiciones observables y verificables>
restricciones_y_autoridad: <límites reales>
supuestos: <solo los activos>
decisiones_abiertas: <solo las que bloquean o cambian rumbo>
```

Incluir diseño técnico únicamente donde ya haya una decisión o una alternativa
que decidir. Heredar comandos, estructura, estilo y estrategia de pruebas desde
las fuentes del repositorio; repetir solo la delta específica del cambio.

La aceptación debe describir resultado, no actividad. Añadir umbrales no
funcionales solo cuando exista baseline, necesidad y medición posible; no
inventar cifras para volver precisa una frase vaga.

### 5. Decidir el único gate necesario

Proceder sin revisión por fases cuando la Spec sea suficiente, el siguiente
movimiento sea reversible y esté dentro de la autoridad vigente.

Devolver una decisión concreta al humano antes de cambiar arquitectura,
schema, dependencias, boundaries, alcance de producto, taste o una superficie
difícilmente reversible. La aprobación valida esa decisión; no crea gates
automáticos para plan, tareas, implementación y cierre.

Si falta una decisión material, cerrar `BLOCKED` con la pregunta mínima. Si no
falta, ejecutar: no pedir confirmación ceremonial.

### 6. Planificar solo si reduce riesgo

Crear un plan cuando haya dependencias, varios incrementos o coordinación real.
Mantenerlo como vista derivada y desecharlo al cerrar si no tiene consumidor
durable.

Cada incremento declara únicamente:

```text
resultado + alcance propio + aceptación + verificación + autoridad
```

Ordenar por dependencias y cerrar comportamiento vertical. No imponer límites
arbitrarios de archivos, duración o sesiones. Si el siguiente movimiento seguro
es obvio, ejecutarlo sin descomponerlo en tareas.

### 7. Ejecutar, aprender y cerrar

Aplicar `urn:dev:artefacto:ship-discipline` para blast radius, topología,
ejecución y loop closure.

Durante la implementación:

1. mantener código y Spec alineados en cada decisión material;
2. si la evidencia invalida un supuesto, detenerse en esa frontera, actualizar
   la fuente autoritaria y continuar solo con el rumbo resuelto;
3. no ampliar alcance para aprovechar trabajo incidental;
4. no reescribir la Spec después para legitimar una deriva.

Cuando exista un candidato fijo y una fuente de Spec resoluble, se puede
componer con `urn:dev:artefacto:code-review` para revisar correspondencia. Esa
arista no prueba wiring ni reemplaza la verificación del comportamiento.

Detenerse tan pronto el resultado cumpla la aceptación aplicable y los riesgos
reales estén cubiertos. Una Spec más completa después de ese punto es trabajo
sin beneficiario.

## Reglas duras

1. **Suficiente antes de comprometer, no completa antes de aprender.**
2. **Una decisión, una fuente.** No duplicar canon en specs, planes y tareas.
3. **Rigor proporcional.** Incertidumbre y blast radius gobiernan la profundidad.
4. **Evidencia antes que supuestos.** Leer el sistema vivo antes de fijar diseño.
5. **Lo irreducible humano conserva su gate.** Producto, arquitectura, schema,
   dependencias, boundaries, taste y autoridad no se delegan por inercia.
6. **Aceptación observable.** Una lista de acciones no demuestra resultado.
7. **Ningún archivo por default.** Toda superficie nueva debe tener consumidor.
8. **Antideriva.** Lo no incluido no se implementa sin reencuadrar el contrato.
9. **Stop rule.** Cerrar cuando funciona y está proporcionalmente verificado.

## Anti-patrones

| Anti-patrón | Corrección |
|---|---|
| Waterfall de cuatro gates | un gate solo en la decisión material |
| Spec theatre | contrato mínimo que cambia ejecución o aceptación |
| Copiar comandos y estándares | referenciar la autoridad existente y escribir solo la delta |
| Spec retroactiva | actualizar al decidir, nunca para justificar deriva |
| Task confetti | un incremento vertical o ejecución directa |
| Living document sin dueño | fuente durable solo con consumidor y autoridad |
| Supuesto disfrazado de requisito | etiquetar `OBSERVADO`, `INFERIDO` o `ELEGIDO` |
| Precisión inventada | medir baseline o pedir la decisión; no fabricar umbrales |

## Salida esperada

- `spec_source` y modo efectivo;
- contrato mínimo o decisión que falta;
- siguiente movimiento seguro;
- si hubo implementación, evidencia y límites según `ship-discipline`.

No producir un informe separado si esos datos ya viven en la tarea o en la
fuente autoritaria.
