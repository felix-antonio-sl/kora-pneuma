
# Graphic Design — Identidad Visual Sistemica

Skill para disenar identidades visuales como sistemas coherentes, transformables y trazables. Opera con fundamento categorico interno pero entrega artefactos practicos: specs, design tokens ejecutables y assets SVG.

## Axioma estetico

> **Belleza = max(informacion / simpleza)**

Cada decision visual se evalua contra esa razon. Un elemento se justifica solo si la informacion que aporta excede la complejidad que introduce. El diseno optimo es la presentacion mas compacta del sistema: minimos generadores, maxima estructura preservada.

## Objetivo

Producir identidades visuales materializadas como design tokens ejecutables, SVGs y brand specs listos para consumo por `frontend-design` u otros skills downstream.

## Cuando Usar

- Crear identidades o marcas desde cero a partir de un brief.
- Definir paletas de color, tipografia, grillas o sistemas de espaciado.
- Generar design tokens (JSON, CSS custom properties, Tailwind config).
- Adaptar identidad a nuevo soporte (web, print, mobile, senaletica).
- Auditar coherencia de sistema visual existente.

## Distincion con skills relacionadas

| graphic-design | frontend-design | ux-design |
|----------------|-----------------|-----------|
| QUE se ve (sistema) | COMO se implementa | COMO se usa |
| Identidad, operadores, tokens | Componentes, codigo, motion | Flujos, heuristicas, accesibilidad |
| Produce los tokens | Consume los tokens | Evalua la experiencia |

Es **upstream** de `frontend-design` e independiente de `arquitecto-categorico` (vocabulario categorico propio adaptado al dominio visual).

## Workflow

### Modo `create` — Identidad nueva

1. Capturar brief: contexto, restricciones, audiencia, soportes destino.
2. Si existe identidad previa, ejecutar modo `audit` primero.
3. Definir operadores atomicos (ver `§Operadores`).
4. Declarar reglas de composicion: jerarquias, contrastes, ritmos.
5. Declarar invariantes: propiedades que deben sobrevivir toda transformacion.
6. Materializar como design tokens (JSON + CSS + Tailwind).
7. Generar SVGs (logo, patrones, iconografia).
8. Escribir guia de uso con correcto/incorrecto.
9. Validar ratio informacion/simpleza del sistema completo.

### Modo `audit`

1. Listar operadores presentes en la identidad existente.
2. Medir redundancia: dos tokens que expresan el mismo concepto cuentan como grasa.
3. Identificar inconsistencias: valores fuera del sistema declarado.
4. Proponer compresion: reducir generadores sin perder expresividad.
5. Entregar informe con score `info/simpleza`, hallazgos por operador, recomendaciones priorizadas.

### Modo `adapt`

1. Cargar identidad origen (tokens + invariantes).
2. Analizar restricciones del soporte destino (contraste minimo, tamano tipografia, limitacion de color).
3. Ejecutar funtor de adaptacion preservando invariantes.
4. Declarar explicitamente perdidas (fidelity loss report).

### Modo `tokenize`

1. Leer identidad conceptual (descripcion, referencia visual o brand existente).
2. Extraer operadores latentes.
3. Materializar como tokens ejecutables en JSON + CSS + Tailwind.

## Operadores visuales

| Operador | Que captura | Materializacion |
|----------|-------------|-----------------|
| Color | Paleta + semantica | `color-primary`, `color-surface`, `color-danger`, ... |
| Tipografia | Familias + escala + peso | `font-display`, `font-body`, `font-mono`, escala type |
| Grilla | Columnas + gutters + breakpoints | `grid-cols-12`, `gap-4`, `sm/md/lg/xl/2xl` |
| Espaciado | Ritmo de separacion | Escala `space-1..space-24` base 4/8 px |
| Forma | Radios, sombras, bordes | `rounded-sm`, `shadow-md`, `border-1` |
| Iconografia | Familia + peso + tamano | `icon-sm`, `icon-md`, stroke 1.5 px |
| Marca | Logo + isotipo + clearspace | SVG con variantes horizontal/vertical/marca |

## Reglas de composicion

- Contraste minimo WCAG 2.2 AA: 4.5:1 texto normal, 3:1 texto grande y UI.
- Jerarquia tipografica: al menos 3 niveles distinguibles por peso + tamano.
- Escala modular: preferir progresion geometrica (1.125, 1.25, 1.333, 1.5) sobre ad-hoc.
- Paleta: 1 primario, 1 secundario, N neutros, 3 semanticos (danger/warning/success).
- Espaciado: base 4 px o 8 px; prohibir valores fuera del sistema.

## Recursos

### Referencias

- `referencias/escalas-modulares.md`: proporciones armonicas y tipograficas.
- `referencias/paletas-accesibles.md`: paletas WCAG AA/AAA predisenadas.

### Recursos

- `recursos/design-tokens.schema.json`: JSON Schema para validar tokens.
- `recursos/plantilla-brand-spec.md`: plantilla de brand specification.

## Invariantes

- Todo design token **DEBE** tener nombre semantico (`color-primary`, no `color-blue-500`).
- El sistema **DEBE** ser cerrado: cualquier valor usado en componentes **DEBE** mapear a un token.
- Los SVG **DEBEN** ser optimizables (no inline styles cuando se pueden extraer).
- Una identidad **DEBE** sobrevivir al test de adaptacion: preservar reconocibilidad a monocromo.

## Salida Esperada

1. Brand Spec en Markdown con operadores, invariantes y ejemplos correcto/incorrecto.
2. Design tokens en JSON (`tokens.json`) + CSS custom properties (`tokens.css`) + Tailwind config snippet.
3. SVGs (logo, patrones, iconografia) en `assets/`.
4. Guia de transformacion en Markdown.
