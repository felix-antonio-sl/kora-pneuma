# Frame guía de especificación gráfica UI

## Índice

- [Uso](#uso)
- [Contrato](#contrato)
- [00. Binding y estatus](#00-binding-y-estatus)
- [01. Frame](#01-frame)
- [02. Tesis gráfica](#02-tesis-gráfica)
- [03. Contenido y atención](#03-contenido-y-atención)
- [04. Composición web](#04-composición-web)
- [05. Composición smartphone](#05-composición-smartphone)
- [06. Sistema visual](#06-sistema-visual)
- [07. Componentes](#07-componentes)
- [08. Estados y microinteracción](#08-estados-y-microinteracción)
- [09. Accesibilidad y rendimiento](#09-accesibilidad-y-rendimiento)
- [10. Materialización](#10-materialización)
- [11. Evaluación](#11-evaluación)
- [12. Decisión y continuidad](#12-decisión-y-continuidad)

## Uso

Completar las secciones pertinentes de este frame al ejecutar `FRAME` o `DESIGN`. En `MODEL`, usar sus
bindings; en `BUILD`, como contrato de trazabilidad; en `EVALUATE`, como índice
de cobertura; y en `FULL`, durante cada gate. Modos canónicos:
`FRAME | MODEL | DESIGN | BUILD | EVALUATE | FULL`.

No rellenar campos con contenido plausible. Usar:

- `verificado [E#]`;
- `propuesto`;
- `inferido [E#]`;
- `pendiente`;
- `no aplica` con razón.

Eliminar una sección sólo si su ausencia no oculta una decisión, estado, riesgo
o dependencia.

## Contrato

```text
GRAPHIC_SPEC_FRAME = {
  binding,
  data_classification,
  status,
  frame,
  graphic_thesis,
  attention_model,
  web_composition,
  smartphone_composition,
  visual_system,
  components,
  states,
  accessibility,
  performance,
  materialization,
  evaluation,
  decision,
  continuity
}
```

La salida completa es una especificación visual. No es evidencia runtime.

---

## 00. Binding y estatus

### Identidad

| Campo | Valor |
|---|---|
| Producto/feature | `<nombre>` |
| Revisión | `<id o hash>` |
| Modo | `FRAME | MODEL | DESIGN | BUILD | EVALUATE | FULL` |
| Soportes | `web | smartphone | ambos` |
| Plataforma | `responsive-web | mobile-web` |
| Artefactos de entrada | `<paths, URLs, hashes>` |
| Sistema visual de origen | `<path/versión o ausente>` |
| Clasificación de datos | `synthetic | deidentified | phi | unknown` |
| Recibo de autoridad de dominio | `<E#, autoridad, rol competente, fuente, alcance, versión/fecha, vigencia, decisiones>` |
| Recibo de mutación | `<E#, repo, paths, operaciones, comandos, acciones externas o no aplica>` |
| Estado epistémico | `SPEC_ONLY | MODEL_STRUCTURAL | STATIC | RUNTIME_AUTOMATED | RUNTIME_MANUAL | HUMAN_VALIDATED | DOMAIN_VALIDATED` |

Esta versión no cubre apps nativas o híbridas. No abrir ni capturar recursos con
clasificación `phi` o `unknown`; devolver `phi-boundary`.

### Evidencia

```text
[E1] tipo=<input|archivo|comando|runtime|humano>
     fuente=<identificador estable>
     observacion=<hecho literal>
     alcance=<demuestra / no demuestra>
```

### Límites

- Verificado:
- Propuesto:
- Inferido:
- Pendiente:
- Fuera de alcance:

---

## 01. Frame

### Contexto

- Entorno:
- Momento de uso:
- Restricciones físicas:
- Restricciones técnicas:
- Riesgos:

### Rol y tarea

- Rol primario:
- Responsabilidad:
- Tarea:
- Resultado humano:
- Alternativa actual:
- Fallos observables:

### Objeto primario

- Objeto candidato:
- Identidad:
- Ciclo de vida:
- Relaciones:
- Estado:
- Tiempo:
- Procedencia:
- Acción:
- Hipótesis no resueltas:

### Función esencial

Completar en una frase:

> `<verbo + objeto + resultado + condición crítica>`

### Alcance del ciclo

- Incluye:
- Excluye:
- Siguiente capacidad:

**Gate:** contexto, tarea, responsabilidad y objeto pueden explicarse sin
nombrar paneles.

---

## 02. Tesis gráfica

### Tesis

> `<relación visual propia que debe hacer inevitable la tarea>`

### Carácter

- Tres adjetivos con conducta observable:
- Tres adjetivos rechazados:
- Qué debe sentirse:
- Qué nunca debe parecer:

### Lentes

| Lente | Decisión concreta | Contraprueba |
|---|---|---|
| Fit Karri/Linear | `<qué fuerza resuelve>` | `<qué la refutaría>` |
| Calma Linear | `<qué deja de competir>` | `<qué no puede desaparecer>` |
| Detalle invisible Linear | `<foco, puntero, retorno, update>` | `<fallo observable>` |
| Design engineering Vercel | `<qué llega a código>` | `<qué recibo lo prueba>` |
| Componentes/estados Vercel | `<contrato>` | `<estado que lo rompe>` |
| Responsive Vercel | `<transformación>` | `<pérdida semántica>` |

### Direcciones candidatas TLHD/paciente-episodio

Completar esta sección sólo cuando exista una decisión comparativa material. Una
dirección única fundada o una especificación `SPEC_ONLY` no exige fabricar las otras.

| Dirección | Tesis | Gana | Pierde | Evidencia que la mata |
|---|---|---|---|---|
| Ledger clínico |  |  |  |  |
| Hilo de evidencia |  |  |  |  |
| Escena de decisión |  |  |  |  |

**Gate:** cuando se comparan direcciones y el binding corresponde, usar fixture,
estados y soportes idénticos. No son una taxonomía universal para toda UI clínica.

---

## 03. Contenido y atención

### Planos

| Plano | Contenido | Prioridad | Expresión |
|---|---|---|---|
| Contexto |  |  |  |
| Trabajo |  |  |  |
| Foco |  |  |  |
| Consecuencia |  |  |  |

### Jerarquía

Ordenar los elementos visibles:

1.
2.
3.
4.
5.

Justificar cada nivel por tarea o consecuencia.

### Densidad

- Siempre visible:
- Bajo demanda:
- Nunca oculto:
- Truncable:
- No truncable:
- Datos comparables:
- Narrativa:
- Historia:

### Presupuesto de atención

| Elemento | Nivel `A0–A4` | Canal principal | Segundo canal |
|---|---:|---|---|
|  |  |  |  |

**Gate:** selección, foco, warning y critical no se confunden.

---

## 04. Composición web

### Modo amplio

```text
<wireframe textual>
```

- Objeto primario:
- Regiones simultáneas:
- Dueño de scroll:
- Contexto persistente:
- Relación selección–detalle:
- Acción primaria:

### Modo compacto

- Región que permanece:
- Región que se transforma:
- Patrón de detalle:
- Patrón de filtros:
- Datos que nunca se ocultan:

### Anchos funcionales

No declarar breakpoints de dispositivo sin contenido. Para cada región:

| Región | Contenido límite | Ancho funcional candidato | Transformación al fallar |
|---|---|---:|---|
|  |  |  |  |

### Teclado y puntero

- Orden de foco:
- Atajos:
- Retorno de foco:
- Hover:
- Selección:
- Actualización durante lectura:

---

## 05. Composición smartphone

### Escena vertical

```text
Contexto
  ↓
Objeto/tarea
  ↓
Evidencia
  ↓
Acción
  ↓
Estado/retorno
```

Completar:

- Tarea primaria:
- Contexto fijo:
- Navegación de primer nivel:
- Rutas:
- Sheets:
- Diálogos:
- Acción al alcance:
- Restauración al volver:

### Transformación

| Contenido/patrón web | Forma smartphone | Invariante preservado |
|---|---|---|
|  |  |  |

### Tacto y entorno

- Targets:
- Teclado virtual:
- Safe areas:
- Orientación:
- Uso con una mano:
- Privacidad ambiental:
- Conectividad:

**Gate:** el smartphone no es el layout web reducido.

---

## 06. Sistema visual

### Tokens

#### Primitivos

| Familia | Escala |
|---|---|
| Color |  |
| Espacio |  |
| Tamaño |  |
| Radio |  |
| Sombra |  |
| Duración |  |

#### Semánticos

| Token | Valor candidato | Rol | Contraste pendiente |
|---|---:|---|---|
|  |  |  |  |

#### Componente

| Token | Deriva de | Componente/estado |
|---|---|---|
|  |  |  |

No permitir primitivas directas en instancias salvo excepción.

### Tipografía

| Rol | Familia | Tamaño/line-height | Peso | Uso |
|---|---|---:|---:|---|
|  |  |  |  |  |

- Numerales:
- Unidades:
- Timestamps:
- Truncación:
- Idioma:
- Glifos ambiguos:

### Superficie

- Canvas:
- Trabajo:
- Selección:
- Foco:
- Warning:
- Critical:
- Elevación:
- Overlay:

### Iconografía

- Familia:
- Caja óptica:
- Tamaños:
- Icon-only permitido:
- Reglas críticas:

### Movimiento

| Transición | Propósito | Reduced motion | Falla prohibida |
|---|---|---|---|
|  |  |  |  |

**Gate:** todo valor resuelve a token, primitive, componente o excepción.

---

## 07. Componentes

Inventario mínimo:

| Componente | Función | Web | Smartphone | Estados |
|---|---|---|---|---|
| PatientContextBar |  |  |  |  |
| WorkList |  |  |  |  |
| DataTable |  |  |  |  |
| DetailInspector |  |  |  |  |
| ActionFlow |  |  |  |  |
| ReviewAndRelease |  |  |  |  |
| ClinicalAlert |  |  |  |  |
| StatusMessage |  |  |  |  |
| CommandPalette |  |  |  |  |
| FilterControl |  |  |  |  |

Contrato por componente:

```text
COMPONENT = {
  purpose,
  anatomy,
  inputs,
  outputs,
  tokens,
  states,
  focus,
  keyboard,
  touch,
  responsive,
  long_content,
  loading,
  empty,
  error,
  disabled,
  synthetic_example,
  tests,
  debt
}
```

### Primitives compartidas

- Typography
- Icon
- FocusRing
- Button
- Input
- Status
- Row
- Surface
- Divider
- Overlay

**Gate:** no hay componente que signifique simultáneamente detalle, workflow,
alerta y confirmación.

---

## 08. Estados y microinteracción

### Estado asincrónico

```text
idle → editing → validating → ready → sending
     → confirmed | failed | uncertain | conflict
```

Para cada transición:

| Desde | Evento | En vuelo | Resultado | Persistencia | Recuperación |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

### Datos

| Estado | Expresión | Acción | Anuncio |
|---|---|---|---|
| carga |  |  |  |
| vacío |  |  |  |
| parcial |  |  |  |
| obsoleto |  |  |  |
| error |  |  |  |
| offline |  |  |  |
| conflicto |  |  |  |
| actualizado |  |  |  |

### Detalles invisibles

- Selección:
- Retención de scroll:
- Expansión:
- Trayectoria de puntero:
- Retorno de foco:
- Actualización concurrente:
- Doble envío:
- Navegación durante envío:
- Recepción incierta:
- Corrección posterior:

---

## 09. Accesibilidad y rendimiento

### Accesibilidad

| Dimensión | Criterio | Evidencia requerida | Estado |
|---|---|---|---|
| Contraste |  | cálculo por componente |  |
| Teclado |  | recorrido manual |  |
| Foco |  | recorrido manual |  |
| Tacto |  | dispositivo/emulación |  |
| Zoom/reflow |  | viewport ejecutable |  |
| Lector |  | prueba manual |  |
| Movimiento |  | modo reducido |  |
| Semántica |  | DOM/accessibility tree web |  |

### Rendimiento

| Dimensión | Baseline | Presupuesto | Medición | Estado |
|---|---:|---:|---|---|
| Respuesta de interacción |  |  |  |  |
| Estabilidad de layout |  |  |  |  |
| Carga esencial |  |  |  |  |
| Lista densa |  |  |  |  |
| Recursos visuales |  |  |  |  |

No inventar presupuestos sin hardware, red, tarea y baseline.

```text
ACCESSIBILITY_RECEIPT = {
  platform, criterion_or_sc, route, state, device_and_at,
  evidence, result, limits
}
PERFORMANCE_RECEIPT = {
  device, network, command, baseline, budget, repetitions,
  measurement, result, limits
}
```

---

## 10. Materialización

### Bundle

```text
tokens/
primitives/
components/
patterns/
scenes/web/
scenes/smartphone/
HANDOFF.md
```

Las rutas reales dependen del stack.

### Trazabilidad

| Decisión | Token/primitive/componente | Archivo | Prueba |
|---|---|---|---|
|  |  |  |  |

### Recibos

- Build:
- Tests:
- Lint:
- Integración:
- Preview:
- Capturas:
- Runtime:

Build verde no prueba UX. Una captura no prueba interacción.

---

## 11. Evaluación

### Matriz visual

| Dimensión | Evidencia | Hallazgo | Severidad | Corrección |
|---|---|---|---|---|
| Función |  |  |  |  |
| Jerarquía |  |  |  |  |
| Densidad |  |  |  |  |
| Coherencia |  |  |  |  |
| Carácter |  |  |  |  |
| Web |  |  |  |  |
| Smartphone |  |  |  |  |
| Estados |  |  |  |  |
| Acceso |  |  |  |  |
| Rendimiento |  |  |  |  |
| Dominio |  |  |  |  |

### Crash matrix

- [ ] normal
- [ ] crítico
- [ ] vacío
- [ ] denso
- [ ] texto largo
- [ ] parcial
- [ ] obsoleto
- [ ] actualización durante lectura
- [ ] desconexión
- [ ] error
- [ ] conflicto
- [ ] recepción incierta
- [ ] zoom
- [ ] alto contraste
- [ ] reducción de movimiento
- [ ] teclado
- [ ] lector
- [ ] smartphone estrecho
- [ ] teclado virtual
- [ ] orientación

### Nivel de evidencia

Marcar uno por hallazgo:

- `documental`;
- `estático`;
- `automatizado`;
- `runtime-manual`;
- `humano`;
- `dominio`.

---

## 12. Decisión y continuidad

### Decisión

- Dirección elegida:
- Razón:
- Direcciones rechazadas:
- Evidencia:
- Hipótesis:
- Condición de reversión:

### Gates

Registrar sólo los gates pertinentes al modo y a la promoción pedida. En
`SPEC_ONLY`, un gate de runtime, acceso o dominio pendiente limita las afirmaciones,
pero no impide entregar una especificación sintética dentro de ese alcance.

| Gate canónico | Estado | Evidencia | Bloqueo |
|---|---|---|---|
| `G1-problem` |  |  |  |
| `G2-data-privacy` |  |  |  |
| `G3-object` |  |  |  |
| `G4-concepts` |  |  |  |
| `G5-visual-system` |  |  |  |
| `G6-states` |  |  |  |
| `G7-responsive` |  |  |  |
| `G8-domain-authority` |  |  |  |
| `G9-implementation-access-performance` |  |  |  |
| `G10-evidence` |  |  |  |

### Cierre

- Verificado:
- Propuesto:
- Inferido:
- Pendiente:
- Deuda:
- Riesgo:
- Siguiente gate:
- Acción mínima:

Un gate rojo conserva el resultado como propuesta o prototipo. No se maquilla
con un promedio ni se promueve por calidad de la documentación.
