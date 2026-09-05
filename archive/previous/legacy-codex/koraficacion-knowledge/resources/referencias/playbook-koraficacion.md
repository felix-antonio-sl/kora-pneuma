# Playbook de koraficacion KORA/MD

## Objetivo

Convertir `DocHumano` en KORA/MD preservando verdad y reduciendo entropia
comunicativa. La salida es un borrador en `_SCRIPTORIUM/REVIEW/{ns}/`.

## Secuencia operativa

1. Leer la fuente completa o una muestra representativa si es larga.
2. Declarar tipo documental, idioma, densidad y destino probable.
3. Inventariar skeleton/meat/fat.
4. Segmentar solo por fronteras naturales.
5. Comprimir semanticamente cada segmento.
6. Deduplicar conceptos repetidos por equivalencia real.
7. Ensamblar el artefacto con headings recuperables.
8. Inyectar frontmatter KORA/MD.
9. Ejecutar auditoria mecanica y semantica.
10. Iterar hasta `FS=100%` o rechazar.

## Segmentacion

Segmentar cuando el documento no quepa en una transformacion controlada.

Reglas:

- cortar entre capitulos, secciones, anexos o tablas completas.
- no cortar dentro de tabla, lista, procedimiento o parrafo.
- mantener un ledger global de conceptos ya definidos para deduplicar entre
  segmentos.
- si la salida requiere varios artefactos, crear un indice con `relations`
  claras y segmentos tematicos.

## Compresion semantica

Aplicar estas transformaciones:

| Fuente | Salida KORA/MD |
| --- | --- |
| Parrafo condicional largo | Tabla `Condicion | Resultado | Base` |
| Enumeracion embebida | Lista con items completos |
| Definicion repetida | Definicion unica + referencias locales |
| Comparacion narrativa | Tabla comparativa |
| Retorica o transicion | Eliminacion |
| Frase tecnica simple | Prosa breve, no lista artificial |

## Deduplicacion

Usar SSOT por concepto:

- mismo concepto, mismo alcance: una definicion.
- mismo concepto, distinto alcance: conservar variantes.
- misma regla, distinta excepcion: conservar ambas.
- distintas fuentes en tension: declarar tension, no fusionar.

## Salida esperada

Un artefacto KORA/MD debe tener:

- frontmatter valido.
- `status: borrador` si vive en REVIEW.
- al menos tres tags.
- `extensions.kora.family` cuando ayude a la clasificacion.
- `#` unico y `##` tematicos recuperables.
- cuerpo sin saludos, transiciones, hedging ni labelese.

## Cierre minimo

No cerrar sin:

- `lint-md` limpio.
- auditoria mecanica sin faltantes numericos/fechas/URLs.
- ledger semantico sin omisiones ni agregados no declarados.
- CR e IDC reportados.
- deuda residual declarada si IDC<0.85.
