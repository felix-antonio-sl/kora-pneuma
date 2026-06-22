---
urn: urn:kora:artefacto:ux-design
nombre: ux-design
version: 1.0.1
estado: activo
descripcion: "Evalua y mejora la experiencia de usuario aplicando heuristicas de Nielsen, flujos de tarea, accesibilidad WCAG 2.2 AA, arquitectura de informacion y patrones UX institucionales. Usar al auditar UX, disenar formularios, mejorar navegacion o revisar accesibilidad."
fuente: "Migrado de la bestia (~/kora) artifacts/skills/kora/ux-design/SKILL.md v1.0.1 (sha256:c52c436ed4febe7c3fab00eeafb9ab4a4a9a1d9551085088e10d8e65deb05379) el 2026-06-22 (regimen migrar-o-omitir). Frontmatter _manifest/extensions.kora/atlas/artefacto.{perfil,interfaz} anidado -> shape plano ley/2; vector bestia [2,0,1,0,1] y sigma [1,2,2,1,0] preservados (legales para habilidad/disciplina). Conocimiento bestia (urn:tde:kb:guia-calidad-web, recomendaciones-diseno-servicios-estado, guia-voz-y-tono) OMITIDO: no encarna en el censo pneuma. Distincion con graphic-design/frontend-design (no migradas) reescrita hacia design (urn:dev:artefacto:design) y steve-jobs (urn:dev:artefacto:steve-jobs), que SI resuelven. Componible declarada: design (forma visual) y steve-jobs (gusto), ambos resuelven en pneuma y steve-jobs ya deriva a esta skill para el audit generico."
autor: FS
creado: 2026-04-23
lang: es
tags: [ux, usabilidad, accesibilidad, wcag, heuristicas-nielsen, arquitectura-informacion, disciplina]
vector: [2, 0, 1, 0, 1]
sigma: [1, 2, 2, 1, 0]
arnes: disciplina
forma: habilidad
herramientas: [Read, Grep, Glob]
targets: [claude-code, codex, opencode]
estados: [auditar, disenar, validar-wcag, entregar]
componible: [urn:dev:artefacto:design, urn:dev:artefacto:steve-jobs]
---

# ux-design

## Proposito

Skill para evaluar, disenar y mejorar la experiencia de usuario en interfaces web. Aplica principios de usabilidad, accesibilidad y arquitectura de informacion con enfoque en aplicaciones institucionales y gobierno digital.

Produce audits UX con hallazgos trazables a heuristicas formales (Nielsen, WCAG 2.2 AA, ley de Hick, ley de Fitts) y entrega mejoras accionables por componente.

## Cuando Usar

- Auditar UX de pagina o componente existente.
- Disenar formularios, flujos de tarea o navegacion.
- Revisar accesibilidad WCAG 2.2 AA.
- Evaluar carga cognitiva, densidad de informacion o estados vacios.
- Crear user flows o mapas de interaccion.

## Cuando NO Usar

- Definir la **forma visual** (sistema de diseno, tokens, identidad, prototipo, codigo frontend) -> usar `urn:dev:artefacto:design`. Esta skill evalua usabilidad; design da forma.
- Buscar un **veredicto de gusto** que sustraiga y exija inevitabilidad -> usar el agente `urn:dev:artefacto:steve-jobs`. Esta skill aplica heuristicas y WCAG; no reparte juicio estetico.

### Distincion con artefactos relacionados

| ux-design (esta skill) | design (`urn:dev:artefacto:design`) | steve-jobs (`urn:dev:artefacto:steve-jobs`) |
|------------------------|-------------------------------------|---------------------------------------------|
| Como se USA | QUE se ve y COMO se implementa | Si MERECE existir |
| Flujos, tareas, errores | Sistema visual, tokens, codigo | Veredicto de gusto, sustraccion |
| WCAG, heuristicas, IA | Componentes, identidad, handoff | Inevitabilidad, cero entrenamiento |

## Workflow

### Estado `auditar` (modo auditoria)

1. Leer HTML/JSX del componente o pagina a auditar.
2. Aplicar las 10 heuristicas de Nielsen como checklist.
3. Validar WCAG 2.2 AA contra la lista de §Checklist WCAG 2.2 AA.
4. Medir densidad de informacion y carga cognitiva por region.
5. Clasificar hallazgos por severidad: critico, alto, medio, bajo.
6. Entregar reporte con tabla `heuristica | hallazgo | evidencia | severidad | correccion`.

### Estado `disenar` (modo diseno)

1. Capturar tarea objetivo y audiencia del usuario.
2. Elegir patron UX segun tipo de interfaz (formulario, tabla, dashboard, wizard).
3. Mapear flujo de tarea con puntos de decision, errores y recuperacion.
4. Definir jerarquia visual, agrupacion semantica y affordances.
5. Producir wireframe textual o componente JSX/HTML.
6. Validar contra heuristicas antes de entregar (`validar-wcag`).

## Heuristicas de Nielsen

| # | Heuristica | Pregunta clave |
|---|-----------|----------------|
| H1 | Visibilidad del estado | El usuario sabe donde esta y que pasa? |
| H2 | Correspondencia mundo real | Usa lenguaje del dominio, no tecnico? |
| H3 | Control del usuario | Puede deshacer, cancelar, volver? |
| H4 | Consistencia y estandares | Sigue patrones establecidos en la app? |
| H5 | Prevencion de errores | Evita errores antes de que ocurran? |
| H6 | Reconocer vs recordar | La info necesaria esta visible? |
| H7 | Flexibilidad y eficiencia | Hay atajos para expertos? |
| H8 | Diseno minimalista | Solo muestra lo necesario? |
| H9 | Recuperacion de errores | Los mensajes son claros y accionables? |
| H10 | Ayuda y documentacion | Hay tooltips, placeholders, guias contextuales? |

## Checklist WCAG 2.2 AA

- Contraste texto: >= 4.5:1 (normal), >= 3:1 (grande/bold).
- Contraste UI: >= 3:1 (bordes, iconos, controles).
- Focus visible en todos los interactivos (outline o ring).
- Orden de tab logico (izq -> der, arriba -> abajo).
- Labels en todos los inputs (`<label for>` o `aria-label`).
- Roles ARIA correctos (`dialog`, `alert`, `navigation`, etc.).
- `alt` text en imagenes informativas.
- Estados (`disabled`, `error`, `loading`) comunicados a screen readers.
- No depender solo del color para transmitir significado.
- Target size minimo 24x24 px (WCAG 2.2 Target Size).
- Reduccion de movimiento respetada (`prefers-reduced-motion`).
- Errores de formulario: identificar campo + descripcion del error.

## Patrones UX por tipo de interfaz

### Formularios

- Agrupar campos relacionados con `fieldset` semantico.
- Labels siempre visibles (NO solo placeholder).
- Validacion inline al salir del campo (`onBlur`), NO al escribir.
- Errores: rojo + icono + texto bajo el campo.
- Boton primario a la derecha, secundario (cancelar) a la izquierda.
- Indicar campos obligatorios (asterisco o texto).
- Progress indicator para formularios multi-paso.

### Tablas de datos

- Encabezados sticky en scroll.
- Alinear texto a la izquierda, numeros a la derecha, estados al centro.
- Filas clickeables con hover state.
- Empty state contextual (NO "No hay datos").
- Paginacion o virtual scroll para > 100 filas.
- Filtros por columna y busqueda global.

### Dashboards

- Jerarquia Z: lo critico arriba-izquierda.
- Grupos de tarjetas con proximidad visual.
- Alertas criticas destacadas con color + icono + texto.
- Acciones primarias fijas, secundarias al alcance.

### Wizards multi-paso

- Stepper visible con paso actual.
- Permitir ir atras sin perder datos.
- Confirmacion antes de enviar.
- Resumen previo al submit final.

## Reglas Duras

1. Un hallazgo UX **DEBE** trazar a una heuristica o criterio WCAG concreto.
2. Una recomendacion **DEBE** ser accionable en codigo: nombre el componente afectado, el cambio exacto, y la severidad.
3. No usar hedging ("podria mejorar", "seria bueno"); usar RFC 2119 cuando aplique.
4. Accesibilidad NO es feature opcional: los criterios WCAG 2.2 AA son piso, no techo.
5. No invadir la forma visual ni el veredicto de gusto: derivar a `design` o `steve-jobs` cuando el problema deje de ser usabilidad.

## Composicion con otras skills

| Composable con | Cuando |
|----------------|--------|
| `urn:dev:artefacto:design` | el hallazgo de usabilidad necesita una bajada visual concreta (tokens, componente, codigo). ux-design dicta el criterio de usabilidad; design lo materializa. |
| `urn:dev:artefacto:steve-jobs` | el audit revela que la solucion no es ajustar sino sustraer. ux-design entrega la evidencia heuristica; steve-jobs emite el veredicto de gusto. |

## Salida Esperada

Reporte en Markdown con:

1. Tabla de hallazgos con columnas `id | heuristica | hallazgo | evidencia | severidad | correccion`.
2. Lista de criterios WCAG violados con referencia al criterio (e.g. `SC 1.4.3`).
3. Recomendaciones priorizadas por severidad.
4. Ejemplos de correccion en HTML/JSX cuando aplique.
