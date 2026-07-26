# SYSTEM TLHD-HEALTH — marco de diseño gráfico UI

**Lentes:** Karri Saarinen / Linear × Vercel Design Team

**Soportes:** aplicación web de escritorio y aplicación web/móvil en smartphone

**Estado:** `SPEC_ONLY · marco normativo propuesto · no validado en producto`

**Foco:** forma visual, densidad, componentes, estados y traducción responsive

**Fuente original:** `sha256:7b745468294a3a55bc5a20b8af7951cac67c481dd05f0e2c7ea842396bdd0b61`

**DESIGN PACKET v2:** `sha256:34a6f80ab006342532e59b391fd51b0a5405ab3e8284f219523baedff43a1103`

**Auditoría Linear × Vercel:** `sha256:ee991086faa8655c9a6fda1587fd1fd0fcb136f759b1cdcc93d16e249ad50a5f`

> Este marco no fue escrito ni aprobado por Karri Saarinen, Linear ni Vercel.
> No reconstruye su voz ni les atribuye decisiones sobre TLHD-HEALTH. Traduce
> criterios publicados por esas personas y equipos a una disciplina de diseño
> para este producto. Toda regla clínica, regulatoria o institucional permanece
> pendiente de validación competente.

## Índice

- [0. Cómo debe leerse](#0-cómo-debe-leerse)
- [1. Veredicto y tesis](#1-veredicto-y-tesis)
- [2. Las dos lentes como operadores](#2-las-dos-lentes-como-operadores-de-decisión)
- [3. Modelo de atención](#3-modelo-de-atención)
- [4. Arquitectura por soporte](#4-arquitectura-gráfica-por-soporte)
- [5. Sistema visual](#5-sistema-visual)
- [6. Información minimalista](#6-gramática-de-información-minimalista)
- [7. Direcciones gráficas](#7-direcciones-gráficas-a-comparar)
- [8. Contratos de componentes](#8-contratos-de-componentes)
- [9. Estados y microinteracción](#9-estados-y-microinteracción)
- [10. Responsive y smartphone](#10-responsive-y-smartphone-en-detalle)
- [11. Accesibilidad](#11-accesibilidad-como-sistema-gráfico)
- [12. Rendimiento](#12-rendimiento-como-percepción)
- [13. Implementación visual](#13-contrato-de-implementación-visual)
- [14. Evaluación](#14-evaluación-del-diseño-gráfico)
- [15. Bucle de trabajo](#15-bucle-de-trabajo-recomendado)
- [16. Composición humana y agéntica](#16-composición-humana-y-agéntica)
- [17. Antipatrones](#17-antipatrones)
- [18. Decisiones actuales](#18-decisiones-actuales)
- [19. Fuentes públicas](#19-fuentes-públicas-de-las-lentes)
- [20. Próxima acción](#20-próxima-acción)

---

## 0. Cómo debe leerse

Este documento no es una pantalla, un tema visual ni una promesa de
cumplimiento. Es el marco que debe gobernar la exploración, implementación y
evaluación de la UI.

Cada afirmación pertenece a una de estas clases:

| Clase | Significado |
|---|---|
| **Invariante de marco** | condición que toda dirección debe satisfacer para seguir siendo candidata |
| **Hipótesis de producto** | supuesto que exige investigación o arbitraje de dominio |
| **Dirección gráfica** | elección visual propuesta para prototipar y comparar |
| **Token candidato** | valor inicial para materializar; no es token aprobado |
| **Gate** | evidencia necesaria antes de promover una decisión |
| **Runtime** | comportamiento observado en una implementación ejecutable |

Una especificación puede verificar que una condición está escrita. No puede
verificar que una interfaz sea usable, accesible, rápida o clínicamente segura.
Esas propiedades requieren un artefacto ejecutado y, cuando corresponda,
personas y autoridad de dominio.

Las palabras `DEBE`, `NO DEBE`, `DEBERÍA` y `PUEDE` expresan fuerza normativa
dentro de este marco; no equivalen por sí solas a una exigencia legal.

---

## 1. Veredicto y tesis

### 1.1 Veredicto

La propuesta anterior debe conservarse como investigación acumulada, pero no
como sistema visual cerrado. Tiene una intención acertada —calma, densidad,
procedencia y seguridad—, aunque todavía describe una estética B2B competente
sin una relación gráfica propia entre:

- la persona;
- el tiempo;
- el cambio;
- la evidencia;
- la acción;
- la consecuencia.

El replanteamiento no comienza por una paleta. Comienza por esa relación.

### 1.2 Función visual esencial

> **Mantener visibles persona, tiempo, procedencia y consecuencia mientras una
> tarea clínica pasa de observación a acción.**

La UI debe ayudar a reconocer qué se está mirando, de cuándo es, de dónde
proviene, qué cambió, qué exige atención y qué ocurrirá al actuar. No debe
presuponer que el sistema conoce relevancia clínica si esa capacidad no está
demostrada.

### 1.3 Tesis gráfica candidata

> **Continuidad clínica visible.**

La forma debe hacer perceptible un hilo continuo entre contexto, dato,
evidencia y consecuencia. El fondo permanece calmado; la estructura organiza;
la selección conecta; el color advierte; la interrupción se reserva para lo que
cumple una política clínica autorizada.

“Continuidad” no significa dibujar líneas por todas partes. Significa que la
persona nunca tenga que reconstruir mentalmente:

- a quién pertenece el dato;
- qué instante o período representa;
- qué fuente lo produjo;
- qué objeto está seleccionado;
- qué acción está en curso;
- si la consecuencia se confirmó, falló o quedó incierta.

### 1.4 Antiobjetivo

No se busca:

- imitar Linear, Geist o el dashboard de otra empresa;
- presentar toda la ficha a la vez;
- conseguir minimalismo ocultando contexto;
- convertir cada objeto en tarjeta;
- usar color para decorar normalidad;
- llevar el layout de escritorio al teléfono por reducción;
- exhibir sofisticación con animación, glassmorphism o gráficos innecesarios;
- tratar una paleta como design system;
- declarar terminada una decisión porque fue documentada.

---

## 2. Las dos lentes como operadores de decisión

### 2.1 Lente Karri / Linear

| Operador | Pregunta que impone | Consecuencia para TLHD-HEALTH |
|---|---|---|
| **Fit antes que output** | ¿Qué fuerzas del contexto resuelve esta forma? | no diseñar shell completo sin contexto, tarea y objeto primario |
| **Calidad de experiencia completa** | ¿Quién posee también errores, estados y detalles invisibles? | diseño, código y prueba comparten el bucle |
| **Dirección antes que sistema** | ¿Se compararon conceptos reales o sólo argumentos? | materializar tres direcciones con el mismo caso |
| **Calma estructural** | ¿Lo secundario dejó de competir sin desaparecer? | jerarquía por tipografía, posición y espacio antes que color |
| **Densidad para expertos** | ¿La densidad reduce navegación o sólo comprime? | cada dato visible debe servir a comparación, orientación o decisión |
| **Detalles invisibles** | ¿Qué ocurre con foco, puntero, retorno y actualización? | microinteracción y retención de contexto forman parte del diseño |
| **Defaults con criterio** | ¿Qué es invariante, default, adaptación o preferencia? | seguridad no se personaliza; densidad y ayudas pueden admitir preferencia |

### 2.2 Lente Vercel Design

| Operador | Pregunta que impone | Consecuencia para TLHD-HEALTH |
|---|---|---|
| **Diseño en código** | ¿La intención sobrevive a componentes y estados reales? | cada concepto termina en slice vertical ejecutable |
| **Complejidad disponible** | ¿El poder experto existe sin bloquear la ruta básica? | progresión de detalle, atajos descubiertos y acciones contextuales |
| **Primitivas correctas** | ¿Es tabla, lista, descripción, sheet, diálogo o ruta? | no disfrazar cuatro patrones como “inspector” |
| **Estados completos** | ¿Qué se ve antes, durante, después y al fallar? | carga, vacío, parcial, obsoleto, conflicto e incertidumbre son UI de primera clase |
| **Responsive semántico** | ¿Cambia la composición o sólo se encoge? | el teléfono recibe una arquitectura propia |
| **Accesibilidad material** | ¿Foco, contraste, zoom y target alteran la forma? | accesibilidad entra en tokens, layout y componentes |
| **Rendimiento percibido** | ¿La superficie permanece estable y responde? | skeleton, layout estable y feedback inmediato se diseñan |
| **Preview y comparación** | ¿Puede verse la diferencia en la misma tarea? | conceptos alternables con el mismo contenido sintético |

### 2.3 Síntesis: doce leyes gráficas

1. **Contexto antes que píxel.** Ninguna forma asciende sin tarea, entorno y
   responsabilidad explícitos.
2. **Un objeto primario por escena.** Una pantalla puede mostrar relaciones,
   pero debe declarar qué entidad gobierna su jerarquía.
3. **Consecuencia antes que decoración.** El peso visual sigue impacto y tarea,
   no disponibilidad de datos.
4. **La estructura se siente antes de verse.** Alineación, ritmo y proximidad
   hacen la mayor parte del trabajo; bordes y fondos sólo lo necesario.
5. **Densidad es compresión semántica.** Menos espacio no equivale a más
   información.
6. **Sistema antes que pantalla.** Todo valor visual debe resolver a token,
   primitive, componente o excepción documentada.
7. **Un componente incluye sus estados.** El estado feliz aislado no cuenta
   como componente diseñado.
8. **Responsive transforma.** Los invariantes viajan; la geometría se adapta.
9. **Gráfica y conducta son inseparables.** Selección, foco, scroll,
   actualización y confirmación pertenecen a la forma percibida.
10. **Procedencia y vigencia son material visual.** No quedan relegadas a
    tooltip si condicionan una decisión.
11. **Accesibilidad y rendimiento son materiales.** No son auditorías tardías.
12. **La calidad no cruza un handoff.** La misma célula compara, implementa,
    observa y corrige el slice.

---

## 3. Modelo de atención

### 3.1 Cuatro planos

La interfaz se construye con cuatro planos perceptivos. No son paneles
obligatorios; son roles visuales.

| Plano | Contenido | Expresión |
|---|---|---|
| **Contexto** | persona, episodio, tiempo, fuente, ubicación autorizada | estable, compacto, persistente |
| **Trabajo** | datos, lista, tabla, formulario, narrativa | neutro, denso, desplazable |
| **Foco** | selección, evidencia relacionada, acción actual | conexión inequívoca sin alarma |
| **Consecuencia** | riesgo, bloqueo, confirmación, recepción incierta | contraste y fricción proporcionales |

La mayor parte de la pantalla debe vivir en `Contexto + Trabajo`. `Foco` aparece
cuando existe una selección o tarea. `Consecuencia` no se usa como estilo
general.

### 3.2 Presupuesto de atención

| Nivel | Uso | Recursos permitidos |
|---|---|---|
| `A0 · ambiente` | estructura y datos estables | espacio, alineación, texto neutro |
| `A1 · orientación` | encabezados, agrupación, metadato | peso, tamaño, separador |
| `A2 · foco` | selección o tarea activa | superficie + marcador + relación espacial |
| `A3 · acción` | cambio accionable o decisión pendiente | acento, copy y acción visible |
| `A4 · interrupción` | riesgo autorizado que exige detenerse | diálogo/bloqueo, color, icono, texto y consecuencia |

Reglas:

- un elemento `A4` NO DEBE competir con otro `A4`;
- `A3` NO DEBE parecer crítico sólo para aumentar conversión;
- selección (`A2`) NO DEBE confundirse con warning;
- hover nunca eleva el nivel de atención;
- la llegada de datos no promueve automáticamente un elemento a interrupción.

### 3.3 Canales de jerarquía

Usar en este orden:

1. posición;
2. agrupación;
3. espacio;
4. alineación;
5. tamaño;
6. peso tipográfico;
7. superficie y borde;
8. color;
9. movimiento.

Si la jerarquía sólo funciona con color o movimiento, la composición está
incompleta.

---

## 4. Arquitectura gráfica por soporte

### 4.1 Invariantes entre web y smartphone

En ambos soportes DEBEN conservarse:

- identidad de la persona y alcance del episodio;
- tiempo y vigencia del objeto activo;
- procedencia cuando afecta interpretación;
- selección actual;
- estado de la acción;
- confirmación, fallo o incertidumbre;
- forma segura de volver;
- nombre y consecuencia de una acción crítica.

Pueden transformarse:

- cantidad de regiones simultáneas;
- densidad;
- ubicación de navegación;
- patrón de inspector;
- número de columnas;
- modo de comparación;
- acceso a acciones secundarias.

No se exige paridad de layout. La paridad relevante es semántica.

### 4.2 Web de escritorio: superficie de investigación

Propósito candidato: comparar, revisar evidencia, redactar y verificar con
varias relaciones visibles.

Composición base:

```text
┌─────────────────────────────────────────────────────────────────────┐
│ Contexto de persona · episodio · vigencia · fuente global          │
├──────────────┬───────────────────────────────┬──────────────────────┤
│ Orientación  │ Trabajo principal             │ Evidencia / acción   │
│ y filtros    │ tabla, lista o narrativa      │ del objeto activo    │
│              │                               │                      │
└──────────────┴───────────────────────────────┴──────────────────────┘
```

No es un mandato de tres paneles. Cada región sólo permanece simultánea si
conserva su ancho funcional. Cuando una región deja de poder expresar su
contenido sin truncar información crítica, la composición cambia.

Reglas:

- el centro porta el objeto primario;
- la derecha muestra detalle o acción, no ambas a la vez;
- la izquierda orienta y filtra; no replica el centro;
- el encabezado de contexto no se desplaza fuera de la tarea;
- cada región tiene un único dueño de scroll;
- abrir detalle conserva selección, foco lógico y posición;
- actualizar datos no reordena una lista bajo lectura sin aviso y control.

### 4.3 Web compacta o tablet: superficie de transición

Cuando no caben tres regiones:

- `Orientación + Trabajo` permanecen;
- `Evidencia` entra como panel persistente si hay ancho suficiente;
- `Acción` se convierte en ruta o sheet modal según consecuencia;
- filtros secundarios se condensan en una capa no destructiva;
- el contexto de persona sigue visible en forma compacta;
- no se oculta la fuente activa sólo para ganar ancho.

El cambio se decide por ancho mínimo del contenido, no por una etiqueta de
dispositivo.

### 4.4 Smartphone: superficie de foco

El teléfono NO DEBE reproducir el mosaico. Su unidad gráfica es una escena
vertical:

```text
Contexto fijo
    ↓
Objeto o tarea actual
    ↓
Evidencia esencial
    ↓
Acción contextual
    ↓
Estado y retorno
```

Propósitos candidatos:

- orientarse durante movilidad;
- reconocer cambios;
- consultar evidencia esencial;
- completar acciones acotadas autorizadas;
- verificar el estado de una acción;
- volver al punto de origen.

No se presupone que toda orden o decisión clínica de escritorio deba estar
disponible en móvil. La autorización funcional es una decisión de producto y
dominio, no gráfica.

Reglas:

- una tarea primaria por pantalla;
- contexto de persona visible antes de cualquier acción;
- navegación inferior sólo para destinos estables de primer nivel;
- acciones de escena cerca del pulgar, sin desplazar contenido crítico;
- sheets para opciones o detalle transitorio; rutas completas para workflows;
- un diálogo bloqueante sólo para consecuencia verdaderamente bloqueante;
- tablas anchas se transforman por prioridad semántica, no por scroll
  horizontal como default;
- no depender de hover, atajo físico ni menú contextual;
- respetar safe areas, teclado virtual, zoom y orientación;
- al volver, restaurar escena, selección y posición.

### 4.5 Matriz de transformación

| Patrón | Escritorio | Smartphone |
|---|---|---|
| Contexto de persona | barra persistente completa | barra compacta persistente, expandible |
| Lista de trabajo | región lateral o central | pantalla de lista |
| Detalle de dato | inspector lateral | ruta de detalle o sheet |
| Comparación tabular | tabla | lista priorizada + detalle; tabla sólo si conserva comprensión |
| Filtros | visibles o popover | sheet con resumen de filtros activos |
| Redacción compleja | panel o página | ruta completa; guardar borrador |
| Revisión crítica | panel/página dedicada | pantalla dedicada, no sheet frágil |
| Confirmación ligera | inline o popover | inline o sheet |
| Alerta interruptiva | diálogo | diálogo/pantalla bloqueante |
| Command palette | acelerador experto | búsqueda/acción explícita, no atajo oculto |

---

## 5. Sistema visual

### 5.1 Arquitectura de tokens

El sistema DEBE separar:

```text
primitivo → semántico → componente → instancia
```

Ejemplo:

```text
blue-600
  → focus-ring
    → data-row-focus-ring
      → fila seleccionada en Resultados
```

Una instancia NO DEBE consumir un color primitivo directamente salvo excepción
documentada.

Capas:

| Capa | Contiene | Ejemplo |
|---|---|---|
| Primitiva | escalas sin significado de producto | `gray-50`, `red-700`, `space-3` |
| Semántica | rol estable | `surface-canvas`, `text-muted`, `status-critical` |
| Componente | aplicación local | `row-selected-border`, `alert-critical-icon` |
| Modo | densidad, contraste o plataforma | `compact`, `touch`, `high-contrast` |

### 5.2 Color

#### Principios

- el neutro construye; el color significa;
- una categoría semántica mantiene significado entre componentes;
- estado NO se comunica sólo por color;
- selección no usa el mismo lenguaje que alerta;
- foco de teclado no usa el mismo lenguaje que selección;
- rojo no significa “importante”; significa consecuencia crítica autorizada;
- verde confirma resultado, no decora normalidad;
- amarillo/ámbar exige texto que explique la condición;
- dark mode no se obtiene invirtiendo la paleta.

#### Semilla candidata

| Token semántico | Valor candidato | Rol |
|---|---:|---|
| `surface-canvas` | `#F7F7F5` | entorno de aplicación |
| `surface-work` | `#FFFFFF` | contenido de trabajo |
| `surface-subtle` | `#F4F4F2` | agrupación secundaria |
| `surface-selected` | `#E8EEF7` | selección, junto a marcador |
| `text-primary` | `#111113` | dato principal |
| `text-secondary` | `#52525B` | metadato |
| `text-tertiary` | `#71717A` | ayuda no esencial |
| `border-subtle` | `#D4D4D8` | estructura |
| `border-strong` | `#71717A` | límite activo |
| `focus-ring` | `#005FCC` | foco de teclado |
| `selection-marker` | `#3B6FA8` | continuidad de objeto seleccionado |
| `critical-surface` | `#FEF2F2` | riesgo crítico |
| `critical-text` | `#991B1B` | texto crítico |
| `warning-surface` | `#FFFBEB` | condición que exige revisión |
| `warning-text` | `#78350F` | texto de warning |
| `success-surface` | `#F0FDF4` | resultado confirmado |
| `success-text` | `#14532D` | texto de éxito |
| `info-surface` | `#F0F9FF` | información contextual |
| `info-text` | `#075985` | texto informativo |

Todos son tokens candidatos. Antes de aprobación se calculan combinaciones
reales por componente y estado: texto, icono, borde, foco, hover, disabled,
selección y superposición.

#### Selección

La selección DEBE combinar al menos:

- cambio de superficie;
- marcador estructural;
- continuidad espacial con el detalle;
- estado programático;
- foco visible cuando corresponda.

Hover sólo anticipa interactividad. Nunca sustituye selección.

### 5.3 Tipografía

#### Familias

- una sans de interfaz, variable si el stack lo permite;
- fallback de sistema probado;
- mono sólo para columnas numéricas comparables, horas e identificadores cuando
  mejore alineación;
- `font-variant-numeric: tabular-nums` para series comparables;
- glifos ambiguos y convenciones de dosis requieren revisión institucional.

No usar tipografías de Linear o Vercel para simular su identidad.

#### Escala candidata

| Rol | Escritorio | Smartphone | Uso |
|---|---:|---:|---|
| `display-compact` | 24/30 | 22/28 | título de escena excepcional |
| `heading` | 18/24 | 18/24 | sección principal |
| `subheading` | 15/20 | 16/22 | grupo o entidad |
| `body` | 14/20 | 16/24 | lectura y formularios |
| `dense` | 13/18 | 14/20 | tabla/lista compacta |
| `meta` | 12/16 | 13/18 | procedencia y tiempo |

Formato `tamaño/line-height` en píxeles, como semilla de prototipo. Los inputs
de smartphone usan texto suficiente para evitar zoom involuntario del
navegador. Ningún dato crítico se obliga a caber truncando.

#### Peso

- `400`: narrativa y datos regulares;
- `500`: labels, acciones y selección;
- `600`: encabezados y consecuencia;
- `700`: sólo énfasis crítico breve si supera pruebas de legibilidad.

Mayúsculas sostenidas sólo para siglas aprobadas o estados críticos breves.
Sentence case por defecto.

#### Números y unidades

- alinear decimales en columnas comparables;
- mantener valor y unidad como una unidad semántica;
- diferenciar visualmente unidad sin volverla ilegible;
- no truncar dosis, vía, frecuencia, identidad ni timestamp relevante;
- usar formato temporal consistente y fuente visible;
- reglas de ceros, decimales y LASA son políticas de dominio pendientes, no
  decisiones autónomas de tipografía.

### 5.4 Espaciado y densidad

Escala candidata: `4, 8, 12, 16, 24, 32`.

| Modo | Fila candidata | Control candidato | Uso |
|---|---:|---:|---|
| `compact` | 36 px | 32 px | estación con puntero y teclado |
| `comfortable` | 44 px | 40 px | lectura mixta |
| `touch` | ≥44 px | ≥44 px | smartphone y entrada táctil |

Reglas:

- el alto puede crecer por contenido, zoom o idioma;
- densidad NO reduce targets táctiles;
- el espacio agrupa antes que el borde;
- una superficie no se convierte en card sólo para crear padding;
- datos de seguridad no se ocultan por conservar altura;
- preferencias pueden afectar densidad y escala, no la visibilidad de
  invariantes de seguridad.

### 5.5 Bordes, radios y elevación

- bordes de `1 px` para estructura y estados;
- radios pequeños y consistentes; la geometría comunica pertenencia, no
  amabilidad genérica;
- sombra sólo cuando una capa se separa físicamente del flujo: popover, sheet,
  menú o diálogo;
- una superficie permanente NO DEBE usar sombra para fingir jerarquía;
- no existe dogma “sin sombras”: existe relación entre elevación y
  comportamiento;
- z-index se define por roles (`base`, `sticky`, `popover`, `dialog`,
  `critical`) y no por números improvisados.

### 5.6 Iconografía

- familia única, trazo y caja óptica coherentes;
- tamaños candidatos `16`, `20` y `24 px`;
- icono crítico siempre acompañado por texto;
- icono-only requiere nombre accesible y affordance conocida;
- no usar íconos distintos para el mismo estado entre web y móvil;
- no usar símbolos clínicos como decoración;
- badge, icono y color no deben triplicar el mismo significado sin aportar
  precisión.

### 5.7 Movimiento

Movimiento permitido:

- confirmar relación causa–efecto;
- mostrar origen y destino de una capa;
- preservar orientación al cambiar de escena;
- indicar actualización sin desplazar foco;
- comunicar progreso real.

Movimiento prohibido:

- ornamentar normalidad;
- reordenar datos bajo lectura;
- pulsar continuamente para llamar atención;
- hacer que éxito parezca confirmado antes de respuesta del sistema;
- depender de animación para entender jerarquía.

Toda transición respeta `prefers-reduced-motion`. Duración y curva se fijan
desde prototipos ejecutables, no desde prosa.

---

## 6. Gramática de información minimalista

### 6.1 Minimalismo semántico

Minimalismo no significa menos datos. Significa:

- menos niveles compitiendo;
- menos codificaciones redundantes;
- menos navegación para comparar;
- menos decisiones visuales locales;
- menos incertidumbre oculta;
- más relación visible entre los datos que quedan.

Una UI puede ser densa y minimalista si cada elemento posee un rol claro.
También puede ser vacía y ruidosa si cada tarjeta, icono y borde reclama
atención.

### 6.2 Regla de compresión

> **Cada elemento visible debe mejorar orientación, comparación, decisión,
> trazabilidad o recuperación.**

Si no cumple una de esas funciones:

1. se elimina;
2. se incorpora al elemento que ya porta el significado;
3. se mueve a detalle bajo demanda;
4. se conserva como excepción justificada.

### 6.3 Elección del patrón

| Naturaleza de la información | Patrón preferido |
|---|---|
| valores homogéneos comparables | tabla |
| objetos heterogéneos priorizados | lista |
| atributos de una entidad | description list |
| evolución temporal | timeline o serie |
| relación dato–evidencia–acción | inspector o ruta enlazada |
| tarea con pasos y consecuencia | workflow/página |
| opciones breves | menu/popover |
| detalle transitorio | sheet |
| decisión bloqueante | diálogo |

No usar tabla para descripción narrativa, card grid para datos comparables ni
sheet para una tarea que necesita navegación, persistencia y recuperación.

### 6.4 Progressive disclosure

La complejidad puede permanecer disponible, pero no obligatoria.

Siempre visible:

- identidad;
- valor o título principal;
- estado;
- tiempo relevante;
- procedencia cuando condiciona interpretación;
- acción primaria de la escena.

Bajo demanda:

- metadatos técnicos;
- historia extensa;
- acciones raras;
- explicación adicional;
- configuración personal legítima.

Nunca oculto por “limpieza”:

- conflicto;
- obsolescencia;
- dato parcial;
- recepción incierta;
- consecuencia de acción crítica;
- relación paciente–episodio–objeto.

### 6.5 Reglas de truncación

NO DEBE truncarse:

- nombre o identificador requerido para confirmar identidad;
- dosis, unidad, vía o frecuencia;
- valor crítico;
- estado de entrega;
- timestamp que cambia interpretación;
- nombre de la acción crítica.

PUEDE truncarse:

- texto secundario recuperable;
- descripción larga con expansión accesible;
- identificador técnico no decisional.

Todo truncamiento recuperable debe permitir leer el contenido completo con
teclado, tacto y tecnología asistiva; tooltip por hover no basta.

---

## 7. Direcciones gráficas a comparar

Las direcciones son experimentos, no skins. Usan el mismo paciente ficticio,
los mismos datos sintéticos, el mismo momento y los mismos estados.

### 7.1 Dirección A — Ledger clínico

**Tesis:** la continuidad emerge de una matriz ordenada y silenciosa.

Rasgos:

- tabla/lista como superficie dominante;
- fuerte alineación temporal y numérica;
- detalle vinculado a selección;
- baja cantidad de superficies;
- jerarquía por ritmo, no cards;
- alta eficiencia con teclado.

Riesgo: convertirse en una ficha electrónica genérica o favorecer sólo a
expertos de escritorio.

Prueba decisiva: localizar cambio, fuente y acción sin abrir navegación
adicional y sin perder legibilidad en smartphone.

### 7.2 Dirección B — Hilo de evidencia

**Tesis:** una continuidad gráfica une cambio, procedencia, evidencia y acción.

Rasgos:

- objeto seleccionado porta un marcador persistente;
- el mismo marcador reaparece en detalle y revisión;
- tiempo y fuente forman una “costura” visual;
- el layout reduce ambigüedad entre dato y consecuencia;
- color secundario; relación espacial primaria.

Riesgo: convertir la costura en ornamento o forzar relaciones que el modelo de
dominio no sostiene.

Prueba decisiva: una persona puede explicar por qué está viendo una acción y de
qué dato proviene sin seguir migas de navegación.

### 7.3 Dirección C — Escena de decisión

**Tesis:** cada escena se organiza alrededor de una decisión pendiente y su
evidencia suficiente.

Rasgos:

- una tarea primaria;
- evidencia esencial junto a la acción;
- progreso y consecuencias explícitos;
- navegación histórica en segundo plano;
- traducción natural a smartphone.

Riesgo: ocultar contexto, promover falsas decisiones o fragmentar la revisión
longitudinal.

Prueba decisiva: completa mejor el bucle sin perder comparación, historia ni
procedencia.

### 7.4 Condición de elección

Ninguna dirección gana por preferencia verbal. Deben existir:

- tres composiciones materializadas;
- contenido idéntico;
- estados idénticos;
- viewport web y smartphone;
- interacción básica;
- crash tests;
- registro de qué se ganó y qué se perdió.

Una cuarta salida válida es rechazar las tres.

---

## 8. Contratos de componentes

### 8.1 `PatientContextBar`

**Función:** anclar la identidad y el alcance de todo lo visible.

Anatomía:

- nombre preferido;
- identificadores necesarios para confirmación;
- episodio o contexto vigente;
- edad u otro discriminante sólo si está autorizado;
- ubicación como contexto, nunca como identidad;
- estado de privacidad o restricción cuando aplique;
- indicador de vigencia global si existe.

Web: barra persistente; puede compactarse sin perder discriminantes.

Smartphone: encabezado compacto expandible; siempre visible antes de acción.

Estados: normal, información restringida, dato parcial, episodio cerrado,
conflicto de identidad, carga.

NO DEBE:

- usar cama como nombre;
- ocultar que existe contenido restringido;
- convertir todos los atributos en chips;
- desplazar el objeto primario con una ficha demográfica completa.

### 8.2 `WorkList`

**Función:** orientar hacia objetos heterogéneos que requieren revisión.

Cada fila:

- título u objeto;
- razón observable de presencia;
- estado;
- tiempo;
- fuente;
- relación con tarea;
- affordance de detalle.

Selección:

- superficie + marcador + estado programático;
- persiste al abrir detalle;
- no se pierde por actualización;
- no se confunde con foco o alerta.

Estados: carga, vacía, error, parcial, obsoleta, actualizada, filtros sin
resultado.

NO DEBE:

- presentar un ranking opaco como “relevancia”;
- mezclar alertas, tareas, resultados y decisiones sin distinguir el tipo;
- reordenar bajo lectura sin aviso;
- ocultar por qué un objeto aparece.

### 8.3 `DataTable`

**Función:** comparar entidades homogéneas.

Contrato mínimo:

- propósito y unidad de fila;
- columnas obligatorias y opcionales;
- orden inicial explicable;
- orden y filtro visibles;
- alineación por tipo;
- encabezado persistente;
- selección independiente de hover;
- expansión sin perder contexto;
- navegación de teclado;
- relación programática entre encabezado y celda;
- estrategia de contenido largo;
- todos los estados de datos.

Estados:

| Estado | Expresión |
|---|---|
| Cargando | geometría estable + texto de estado |
| Vacía | razón y siguiente acción, si existe |
| Parcial | campos ausentes identificados |
| Obsoleta | antigüedad y fuente visibles |
| Error | alcance, causa observable y recuperación |
| Offline | última sincronización; capacidades reales |
| Conflicto | versiones comparables; ninguna elección silenciosa |
| Actualizada | cambio visible sin mover foco ni selección |

Smartphone:

- conservar sólo columnas esenciales en la fila;
- llevar el resto a detalle semántico;
- permitir comparación si la tarea lo exige;
- scroll horizontal sólo cuando preserve mejor la estructura que una
  transformación y haya sido probado.

### 8.4 `DetailInspector`

**Función:** inspeccionar el objeto seleccionado sin abandonar el contexto.

Es sólo para lectura o acciones ligeras. Debe tener:

- título y tipo de objeto;
- tiempo y fuente;
- estado;
- evidencia;
- acciones contextuales;
- cierre con retorno de foco.

Web: panel lateral vinculado a la selección.

Smartphone: ruta o sheet de detalle según profundidad.

NO DEBE contener un workflow complejo, una alerta bloqueante y una confirmación
crítica a la vez.

### 8.5 `ActionFlow`

**Función:** conducir una tarea con borrador, revisión, consecuencia y
recuperación.

Debe declarar:

- inicio;
- datos heredados y editables;
- validación;
- borrador;
- revisión;
- envío;
- confirmación;
- fallo;
- recepción incierta;
- corrección posterior;
- retorno.

Web y smartphone usan página o región con navegación propia. Un sheet sólo es
válido si cerrar no pone en riesgo progreso o comprensión.

### 8.6 `ReviewAndRelease`

**Función:** separar redacción de liberación.

Visualmente distingue:

- contenido redactado;
- cambios desde la versión anterior;
- identidad de destinatario;
- consecuencia;
- autorizaciones pendientes;
- acción de firmar;
- acción de liberar, si son actos distintos;
- estado después del envío.

NO DEBE mostrar éxito antes de confirmación. Una recepción incierta conserva
el contenido, evita doble envío accidental y ofrece verificación segura.

### 8.7 `ClinicalAlert`

Niveles:

| Nivel | Patrón |
|---|---|
| informativo | texto contextual o inline |
| requiere revisión | banner/section con acción |
| interruptivo autorizado | diálogo o escena bloqueante |

Una alerta interruptiva candidata debe ser específica, vigente, accionable,
explicable, trazable y autorizada. El componente siempre muestra:

- riesgo;
- evidencia;
- tiempo y fuente;
- acción;
- alternativa;
- consecuencia de continuar;
- justificación, cuando corresponda.

### 8.8 `StatusMessage`

Para feedback de sistema:

- inline si pertenece a un campo u objeto;
- banner si afecta una región;
- toast sólo para confirmación no crítica y recuperable;
- diálogo sólo si bloquea o exige decisión.

Un toast NO DEBE ser el único portador de fallo, conflicto o incertidumbre.

### 8.9 `CommandPalette`

Es un acelerador para comandos ya descubribles.

DEBE:

- mostrar alcance;
- agrupar por intención;
- nombrar consecuencias;
- aceptar teclado y puntero;
- mantener contexto;
- excluir acciones críticas ambiguas o exigir revisión dedicada.

NO DEBE ser la puerta principal de funciones básicas ni la única forma de
descubrirlas.

### 8.10 `FilterControl`

Debe mostrar:

- filtros activos;
- resultado que afectan;
- forma de limpiar;
- persistencia;
- diferencia entre preferencia personal y criterio del sistema.

Smartphone: sheet con resumen visible al cerrar.

Web: controles inline o popover según frecuencia.

---

## 9. Estados y microinteracción

### 9.1 Estado percibido

Cada acción asincrónica debe distinguir:

```text
idle → editing → validating → ready → sending
     → confirmed | failed | uncertain | conflict
```

Este diagrama es un contrato candidato, no un modelo clínico final.

### 9.2 Reglas de asincronía

- una acción recibe feedback inmediato de que fue solicitada;
- `sending` no parece `confirmed`;
- doble activación se previene o se hace idempotente en implementación;
- navegar durante envío tiene conducta explícita;
- timeout no se presenta automáticamente como fracaso;
- recepción incierta ofrece verificar antes de repetir;
- conflicto muestra versiones y procedencia;
- el resultado permanece visible después de desaparecer el indicador
  transitorio.

### 9.3 Foco

- foco visual inequívoco;
- orden equivalente a jerarquía y tarea;
- abrir una capa mueve foco a su título o primer control pertinente;
- cerrar restaura foco al origen;
- actualizar datos no roba foco;
- error lleva a un resumen y al campo afectado sin encerrar a la persona;
- smartphone preserva foco lógico al volver de detalle;
- los atajos aparecen junto a su acción y pueden descubrirse sin manual.

### 9.4 Puntero y tacto

- toda fila clickeable tiene una zona coherente;
- acciones internas no activan accidentalmente la fila;
- menús toleran trayectorias diagonales sin cerrarse de forma frágil;
- hover anticipa, no confirma;
- touch targets no se reducen por densidad visual;
- gesto nunca es el único acceso a una acción;
- swipe destructivo requiere alternativa y confirmación proporcional.

### 9.5 Scroll y actualización

- un dueño de scroll por región;
- sticky sólo para contexto necesario;
- volver restaura posición;
- expansión no hace saltar el objeto fuera de vista;
- inserciones nuevas no desplazan lectura activa;
- un contador o affordance permite ir a lo nuevo;
- virtualización preserva foco, lectura y alturas previsibles.

---

## 10. Responsive y smartphone en detalle

### 10.1 Jerarquía móvil

Orden recomendado:

1. identidad y contexto;
2. título de escena;
3. estado o cambio;
4. evidencia esencial;
5. acción primaria;
6. detalle secundario;
7. navegación de retorno.

La acción primaria puede permanecer fija sólo si no oculta contenido, teclado,
errores ni controles del sistema.

### 10.2 Navegación

- destinos estables y pocos: navegación de primer nivel;
- tarea o entidad: push route con back;
- detalle breve: sheet;
- decisión bloqueante: diálogo o pantalla;
- historial profundo: página, no pila infinita de sheets;
- deep links restauran contexto suficiente;
- back nunca descarta borrador sin advertencia.

### 10.3 Densidad móvil

En smartphone se reduce simultaneidad, no significado:

- una fila porta identidad, valor/estado y tiempo;
- fuente o metadato decisional permanece visible;
- detalle amplía sin reconstruir contexto;
- agrupación usa espacio y headings, no card por objeto;
- acciones secundarias viven en menú explícito;
- filtros activos quedan resumidos;
- listas densas mantienen targets táctiles.

### 10.4 Teclado virtual

- el input enfocado permanece visible;
- la acción fija se desplaza o adapta;
- errores no quedan detrás del teclado;
- campos numéricos usan modo de entrada adecuado sin impedir caracteres
  válidos;
- cerrar teclado no envía;
- orientación y cambio de viewport no pierden borrador.

### 10.5 Privacidad móvil

El teléfono se usa en entornos compartidos. La UI debe diseñar:

- mínimo dato visible en listados;
- transición consciente hacia detalle sensible;
- timeout y reautenticación según arquitectura real;
- capturas, multitarea y notificaciones según política;
- ocultación explícita, nunca silenciosa.

No se inventa “modo pasillo” sin política, amenaza y prueba ambiental.

---

## 11. Accesibilidad como sistema gráfico

Objetivo propuesto: WCAG 2.2 AA para la implementación web.

### 11.1 Color y contraste

- contraste calculado por combinación real, no por token aislado;
- texto normal, texto grande y componentes se evalúan con su criterio
  correspondiente;
- color siempre tiene segundo canal;
- high contrast se trata como modo del sistema;
- selection, focus, warning y critical siguen siendo distinguibles entre sí.

### 11.2 Reflow y zoom

- lectura y operación sin pérdida de información;
- ninguna región requiere ambos ejes de scroll salvo datos bidimensionales
  justificables;
- sticky no consume el viewport;
- contenido crítico crece antes de truncarse;
- el sistema conserva relaciones al ampliar texto.

### 11.3 Semántica

- jerarquía HTML equivalente a jerarquía visual;
- relaciones de tabla programáticas;
- labels persistentes;
- nombres accesibles específicos;
- estados dinámicos anunciados con prioridad proporcional;
- iconos informativos con alternativa;
- gráficos con resumen textual;
- orden del DOM no contradice la composición.

### 11.4 Modos de entrada

- operación completa por teclado;
- targets táctiles adecuados;
- puntero de precisión no obligatorio;
- gesto con alternativa;
- lector de pantalla y magnificación incluidos en prueba;
- reducción de movimiento;
- foco visible incluso en superficies de estado.

Una checklist no prueba cumplimiento. Cada gate exige recorrido manual sobre el
slice ejecutable.

---

## 12. Rendimiento como percepción

### 12.1 Invariantes

- la geometría principal no salta al cargar;
- la respuesta a una acción se reconoce de inmediato;
- contenido esencial no espera recursos decorativos;
- fuentes y iconos no bloquean orientación;
- listas extensas preservan interacción;
- animación no compite con render;
- error de red mantiene contexto y contenido recuperable.

### 12.2 Skeleton y carga

El skeleton:

- replica la geometría, no inventa contenido;
- conserva altura;
- no simula datos críticos;
- incluye texto de estado cuando la espera importa;
- se reemplaza sin desplazar foco.

### 12.3 Presupuesto

Los umbrales de tiempo y tamaño se fijan tras:

- identificar hardware y red objetivo;
- medir baseline;
- elegir tarea crítica;
- instrumentar el slice.

Este marco no inventa cifras de rendimiento. Sí exige que existan y se
verifiquen antes de promoción.

---

## 13. Contrato de implementación visual

### 13.1 Capas

```text
tokens/
  primitives
  semantic
  component
  modes

primitives/
  typography
  icon
  focus
  surface
  overlay

components/
  context
  data-display
  navigation
  input
  feedback
  overlay

patterns/
  inspect
  compare
  review-release
  uncertain-delivery
  conflict-resolution

scenes/
  web
  smartphone
```

La estructura es conceptual; las rutas reales dependen del stack.

### 13.2 Requisitos por componente

Cada componente implementado entrega:

- propósito;
- anatomía;
- API/props;
- tokens consumidos;
- estados;
- comportamiento de foco;
- teclado y tacto;
- responsive;
- contenido largo;
- carga, vacío, error y disabled;
- ejemplo con datos sintéticos;
- pruebas;
- deuda conocida.

### 13.3 Primitivas antes que composición

Construir primero:

- texto y numerales;
- foco;
- botón;
- input;
- badge/status;
- row;
- surface;
- divider;
- icon;
- overlay.

Luego componentes de dominio. No comenzar por una pantalla monolítica que
codifique decisiones visuales localmente.

### 13.4 Diseño–código

El bucle mínimo:

```text
concepto visual
  → tokens y primitives
  → componente con estados
  → escena ejecutable
  → screenshot + interacción
  → hallazgo
  → corrección sistémica
```

Una corrección de color, espacio o foco se hace en token/primitive/componente,
no en la escena aislada, salvo excepción explícita.

### 13.5 Previews

La implementación debe permitir:

- alternar dirección actual y candidata;
- fijar mismo dataset;
- fijar mismo viewport;
- capturar mismos estados;
- revisar diff visual;
- ejecutar teclado y tacto;
- observar carga y fallo.

No se exige una herramienta específica; se exige comparación reproducible.

---

## 14. Evaluación del diseño gráfico

### 14.1 Matriz visual

| Dimensión | Pregunta | Falla bloqueante |
|---|---|---|
| Función | ¿La forma hace visible contexto, tiempo, fuente y consecuencia? | obliga a reconstruirlos |
| Jerarquía | ¿Se distingue ambiente, foco, acción e interrupción? | selección parece alerta o foco desaparece |
| Densidad | ¿Cada elemento mejora una tarea? | compresión sin comprensión |
| Coherencia | ¿Tokens y componentes gobiernan la escena? | estilos locales o patrones duplicados |
| Carácter | ¿Existe una relación propia y sistémica? | estética B2B intercambiable |
| Web | ¿La simultaneidad ayuda a comparar? | paneles compiten o pierden ancho funcional |
| Smartphone | ¿La composición es nativa a una escena vertical? | escritorio encogido |
| Estados | ¿Cada componente sobrevive fuera del happy path? | error, vacío o incertidumbre sin forma |
| Acceso | ¿La forma soporta teclado, zoom, tacto y contraste? | bloqueo de tarea |
| Rendimiento | ¿Permanece estable y responsiva? | saltos, congelación o feedback ambiguo |
| Dominio | ¿Contenido y consecuencia fueron validados? | regla clínica inventada |

### 14.2 Crash tests obligatorios

Cada concepto se captura y opera con:

- dato normal;
- dato crítico;
- lista vacía;
- lista densa;
- texto largo;
- unidad o nombre largo;
- actualización durante lectura;
- dato parcial;
- dato obsoleto;
- fuente desconocida;
- desconexión;
- error;
- conflicto;
- recepción incierta;
- zoom;
- alto contraste;
- reducción de movimiento;
- teclado;
- lector de pantalla;
- smartphone estrecho;
- teclado virtual abierto;
- cambio de orientación.

### 14.3 Gates de promoción

#### Gate 1 — Problema

Existe contexto, tarea, responsabilidad, alternativa actual y fallos
observables o explícitamente autorizados.

#### Gate 2 — Objeto

El objeto primario y su ciclo pueden explicarse sin nombrar paneles.

#### Gate 3 — Concepto

Tres direcciones materializadas usan el mismo contenido; una gana o las tres se
rechazan con razones observables.

#### Gate 4 — Sistema

Tokens, primitives y componentes resuelven la escena sin valores mágicos ni
duplicación.

#### Gate 5 — Estados

El concepto sobrevive al crash matrix sin ocultar contexto, error o
incertidumbre.

#### Gate 6 — Responsive

Web y smartphone conservan invariantes y transforman composición de forma
comprensible.

#### Gate 7 — Implementación

El slice es ejecutable; foco, teclado, tacto, scroll, async y rendimiento
pueden observarse.

#### Gate 8 — Accesibilidad

Pruebas automáticas de apoyo y recorridos manuales sobre el slice.

#### Gate 9 — Dominio

Autoridad competente valida identidad, alertas, órdenes, corrección,
procedencia, privacidad y riesgos. Este gate no se delega a la UI.

---

## 15. Bucle de trabajo recomendado

### Fase 0 — Enmarcar

Entregables:

- brief de una página;
- contexto clínico único;
- persona/rol;
- tarea;
- responsabilidad;
- objeto primario candidato;
- alternativa actual;
- evidencia y supuestos;
- fuera de alcance.

### Fase 1 — Explorar forma

Entregables:

- tres direcciones;
- mismo contenido sintético;
- web + smartphone;
- estado normal + crítico + vacío + error;
- tesis y condición de rechazo por dirección.

### Fase 2 — Elegir sistema

Entregables:

- decisión;
- rechazos;
- tokens candidatos;
- tipografía;
- grid;
- primitives;
- contratos de componentes;
- reglas responsive.

### Fase 3 — Construir slice

Escena mínima:

> abrir una persona ya seleccionada → reconocer un cambio → revisar procedencia
> y evidencia → iniciar una acción → revisar consecuencia → enfrentar una
> recepción incierta.

Entregables:

- frontend ejecutable con datos sintéticos;
- concepto anterior y candidato comparables;
- estados;
- teclado y tacto;
- instrumentación;
- handoff continuable.

### Fase 4 — Refutar

Ejecutar:

- crash matrix;
- audit visual;
- audit UX;
- WCAG;
- rendimiento;
- revisión clínica;
- prueba en hardware y luz reales.

### Fase 5 — Integrar

Corregir desde la causa:

- incoherencia → token o primitive;
- fallo repetido → componente;
- fallo de tarea → flujo;
- fallo móvil → transformación responsive;
- falsa alarma → política y dominio;
- lentitud → arquitectura/render;
- ausencia de carácter → tesis sistémica, no ornamento.

### Fase 6 — Promover

Sólo después de gates verdes:

- congelar versión del sistema;
- registrar decisiones;
- publicar componentes;
- declarar evidencia y límites;
- expandir a la siguiente escena;
- conservar comparador y regresiones.

---

## 16. Composición humana y agéntica

La célula mínima necesita responsabilidades distintas aunque una persona pueda
portar más de una:

| Responsabilidad | Posee |
|---|---|
| Dirección de producto | problema, tensiones, concepto y decisión |
| Diseño gráfico UI | gramática visual, tokens, composición y detalle |
| Diseño de interacción/UX | tarea, navegación, estados y accesibilidad |
| Ingeniería de interfaz | componentes, responsive, rendimiento y pruebas |
| Dominio clínico | significado, riesgo, políticas y autorización |
| Evaluación independiente | evidencia, severidad y gate |

La IA puede:

- sintetizar fuentes;
- generar direcciones;
- producir tokens y componentes;
- crear estados;
- automatizar capturas;
- revisar coherencia;
- ejecutar pruebas técnicas.

La IA NO puede declarar por sí sola:

- pertinencia clínica;
- seguridad de una alerta;
- conformidad institucional;
- comprensión de usuarios no observados;
- accesibilidad no probada;
- funcionamiento no ejecutado.

### 16.1 Contrato de entrada

```text
UI_FRAME_INPUT = {
  contexto,
  rol_primario,
  tarea,
  responsabilidad,
  objeto_primario_candidato,
  soportes: web | smartphone | ambos,
  contenido_sintetico_o_desidentificado,
  estados_requeridos,
  restricciones,
  sistema_existente?,
  artefacto_ejecutable?,
  evidencia,
  supuestos,
  fuera_de_alcance
}
```

### 16.2 Contrato de salida

```text
UI_GRAPHIC_PACKET = {
  frame,
  tension_map,
  directions[3],
  decision,
  visual_thesis,
  tokens,
  primitives,
  components,
  web_composition,
  smartphone_composition,
  state_matrix,
  prototype_or_spec,
  evidence_ledger,
  evaluation,
  debt,
  handoff
}
```

Sin artefacto ejecutable, `prototype_or_spec` es `spec` y todo cumplimiento
permanece pendiente.

---

## 17. Antipatrones

- **Linear cosplay:** oscuro, compacto y monocromo sin fit.
- **Geist cosplay:** componentes limpios copiados sin modelo de producto.
- **Dashboard por reflejo:** empezar por paneles antes que por objeto y tarea.
- **Card soup:** una tarjeta por dato para simular orden.
- **Tab soup:** módulos sin relación como arquitectura primaria.
- **Minimalismo por ocultación:** esconder procedencia, tiempo o conflicto.
- **Semáforo:** convertir estado clínico en una paleta roja/amarilla/verde.
- **Inspector universal:** usar un panel para detalle, alerta, edición y
  confirmación.
- **Command palette como IA de navegación:** mover ahí lo que no se pudo
  organizar.
- **Móvil miniaturizado:** reducir columnas y tamaños sin recomponer.
- **Acción flotante sin contexto:** CTA que permanece aunque cambie el objeto.
- **Toast crítico:** feedback importante que desaparece.
- **Skeleton ficticio:** shimmer que no conserva geometría.
- **Happy-path system:** componentes sin error, vacío, conflicto o disabled.
- **Responsive por breakpoint nominal:** cambiar sólo porque “es tablet”.
- **Token theatre:** muchas variables sin decisiones semánticas.
- **Sombra prohibida:** dogma estético que impide expresar capas reales.
- **Color como evidencia:** tono que sugiere certeza inexistente.
- **Prototipo como prueba:** interacción simulada presentada como producto.
- **Handoff exculpatorio:** diseño “terminado” antes de implementación y test.

---

## 18. Decisiones actuales

### Se conserva

- prioridad de identidad, procedencia, vigencia e incertidumbre;
- separación entre consulta y liberación;
- color subordinado a significado;
- densidad como capacidad valiosa;
- teclado y foco como parte del producto;
- menor bucle completo como unidad de avance;
- honestidad `SPEC_ONLY`.

### Se reemplaza

| Antes | Ahora |
|---|---|
| “Plano de señales” como dirección elegida | tres direcciones materializadas antes de elegir |
| sistema visual = paleta + tipografía + espacio | tokens + primitives + componentes + estados + modos |
| responsive = ocultar paneles | transformación semántica por soporte |
| inspector único | patrones separados por profundidad y consecuencia |
| command palette como acceso central | acelerador de acciones ya descubribles |
| “sin sombras” | elevación sólo para capas reales |
| lista de estados | contrato observable de transición y recuperación |
| mobile como superficie estrecha | smartphone como escena de foco |

### Permanece abierto

- contexto clínico inicial;
- rol primario;
- objeto primario;
- política de relevancia;
- política de alertas;
- autorización móvil;
- hardware;
- stack;
- identidad visual institucional;
- tipografía definitiva;
- tema oscuro;
- preferencias de densidad;
- umbrales de rendimiento;
- validación clínica y accesible.

---

## 19. Fuentes públicas de las lentes

Consultadas para la auditoría que origina este marco:

### Karri Saarinen / Linear

- [Output isn’t design](https://linear.app/now/output-isn-t-design)
- [Design is more than code](https://linear.app/now/design-is-more-than-code)
- [Why is quality so rare?](https://linear.app/now/why-is-quality-so-rare)
- [How we redesigned the Linear UI](https://linear.app/now/how-we-redesigned-the-linear-ui)
- [A calmer interface for a product in motion](https://linear.app/now/behind-the-latest-design-refresh)
- [Settings are not a design failure](https://linear.app/now/settings-are-not-a-design-failure)
- [Invisible details](https://linear.app/now/invisible-details)

### Vercel Design

- [Design Engineer Principles](https://vercel.com/design/engineer)
- [Design Engineering at Vercel](https://vercel.com/blog/design-engineering-at-vercel)
- [Web Interface Guidelines](https://vercel.com/design/guidelines)
- [Geist Table](https://vercel.com/geist/table)
- [Geist Sheet](https://vercel.com/geist/sheet)

Estas fuentes respaldan los criterios atribuidos. La aplicación concreta,
síntesis y decisiones para TLHD-HEALTH son inferencias de este marco.

---

## 20. Próxima acción

No ampliar la especificación. Materializar el mismo caso sintético en las tres
direcciones:

```text
Ledger clínico
Hilo de evidencia
Escena de decisión
```

Para cada una:

- web;
- smartphone;
- normal;
- crítico;
- vacío;
- error;
- recepción incierta.

La salida siguiente debe ser visual y comparable: composiciones, tokens,
componentes y un slice ejecutable. Si sólo agrega prosa, no reduce la
incertidumbre que este marco deja abierta.
