# Ejemplo minimo — SD de "Cafetera domestica"

Ilustracion didactica de un OPM model de un solo nivel (SD) construido con esta skill. **No es SSOT ni norma; es solo ilustracion.**

## Proposito del sistema

> "Transformar agua y cafe molido en cafe hecho, mediante una persona y una cafetera."

## Cosas

| Nombre | Tipo | Esencia |
|--------|------|---------|
| Agua | objeto | fisico |
| Cafe Molido | objeto | fisico |
| Cafe Hecho | objeto | fisico |
| Persona | objeto | fisico (agent) |
| Cafetera | objeto | fisico (instrument) |
| Hacer Cafe | proceso | fisico |

## Estados

Modelo minimo: sin estados explicitos en este SD. Si quisieramos modelar `Cafe Hecho` con estados `caliente` / `tibio` / `frio`, abririamos en SD1 con state expression sobre `Cafe Hecho`.

## Enlaces (procedurales)

| Origen | Tipo | Destino |
|--------|------|---------|
| Hacer Cafe | consumption | Agua |
| Hacer Cafe | consumption | Cafe Molido |
| Hacer Cafe | result | Cafe Hecho |
| Persona | agent | Hacer Cafe |
| Hacer Cafe | instrument | Cafetera |

## OPL-ES equivalente (bimodal)

```
SD del sistema Hacer Cafe.

**Agua** es un objeto fisico.
**Cafe Molido** es un objeto fisico.
**Cafe Hecho** es un objeto fisico.
**Persona** es un objeto fisico.
**Cafetera** es un objeto fisico.
*Hacer Cafe* es un proceso fisico.

*Hacer Cafe* consume **Agua** y **Cafe Molido**.
*Hacer Cafe* genera **Cafe Hecho**.
**Persona** maneja *Hacer Cafe*.
*Hacer Cafe* requiere **Cafetera**.
```

## Validacion (resumen)

- `reglas-opm-estrictas-es` R-COSA/R-PROC/R-OBJ: pasan.
- `spec-forja-opd-es` + V-* base delegadas: las firmas visuales pasan.
- `spec-forja-opl-es` §1.1: verbos `consume`, `genera`, `maneja`, `requiere` pertenecen al enum cerrado.
- Agente humano: pasa — Persona es agent valido.
- Heuristica claridad (≤ 7±2 cosas): 6 cosas, OK.
- Heuristica completitud: estructura (cosas + enlaces estructurales implicitos por agregacion implicita) + comportamiento (Hacer Cafe transforma) + funcion (proposito declarado). OK.
- Bimodalidad: cada hecho del OPD tiene su sentencia OPL-ES. OK.

## Posibles refinamientos (no aplicados)

Para uso real podrias refinar:

- **In-zooming** de `Hacer Cafe` → `Calentar Agua`, `Filtrar Cafe`, `Servir`.
- **Unfolding** de `Cafe Hecho` → `Liquido` + `Aroma`.
- **State expression** de `Cafe Hecho` → estados `caliente | tibio | frio`.

Cada refinamiento abre un OPD hijo (SD1, SD1.1, etc.) preservando bimodalidad.

## Notas de uso

- Este ejemplo cabe en un SD porque tiene **una sola funcion** y **pocos transformees**.
- Sistemas reales (clinicos, gubernamentales, organizacionales) raramente caben en SD; necesitan al menos un nivel de in-zooming.
- Cuando el SD parece "trivial", es senal de que el modelo esta correctamente abstraido al nivel cero.
