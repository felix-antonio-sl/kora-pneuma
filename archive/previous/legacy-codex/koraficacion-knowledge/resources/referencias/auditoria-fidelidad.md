# Auditoria de fidelidad

## Principio

`FS=100%` significa que todo hecho sustantivo del original esta preservado o
comprimido sin perdida semantica. No significa copiar texto.

## Ledger de hechos

Usar una tabla durante auditorias largas:

| ID | Fuente | Tipo | Hecho original | Estado | Evidencia en KORA/MD |
| --- | --- | --- | --- | --- | --- |
| F001 | seccion/pagina/linea | cifra/condicion/definicion/etc. | texto minimo | preservado/comprimido/omitido/agregado | heading, tabla o frase |

Estados:

- `preservado`: aparece sin cambio sustantivo.
- `comprimido`: aparece con redaccion mas densa, misma verdad.
- `omitido`: falta en salida; bloquea cierre.
- `agregado`: aparece en salida sin fuente; bloquea salvo inferencia declarada.

## Calculo

```text
FS = (preservados + comprimidos) / N_hechos * 100
CR = len(fuente) / len(salida)
IDC = CR observado / CR esperado para el perfil documental
```

Targets:

- `FS=100%`: obligatorio.
- `IDC>=1.00`: deshidratacion adecuada para el perfil.
- `0.85<=IDC<1.00`: aceptable con revision editorial.
- `IDC<0.85`: revisar fat residual, redundancia o mala realizacion superficial.

## IDC: Indice de Deshidratacion Contextual

El CR crudo se conserva como dato, pero no se usa como umbral universal. La
compresion esperable cambia por tipo documental:

| Perfil | CR esperado | Criterio |
| --- | ---: | --- |
| `prosa-redundante` | 1.70 | Texto narrativo con repeticiones, transiciones y retorica. |
| `mixto` | 1.40 | Guia, politica o nota tecnica con secciones, listas y prosa explicativa. |
| `denso-estructurado` | 1.15 | Procedimiento, norma, tabla, documento con alta carga de cifras/fechas. |
| `fuente-ya-densa` | 1.00 | Markdown tecnico, outline, glosario o corpus previamente curado. |

Regla: no castigar una fuente densa por no comprimir como prosa redundante. Si
`FS=100%` y `IDC` es bajo, revisar primero si el perfil elegido es correcto; si
lo es, buscar grasa remanente o declarar que la fuente ya era informacionalmente
densa.

## Auditoria mecanica

Ejecutar:

```bash
python3 artifacts/skills/kora/koraficacion-knowledge/scripts/audit_korafication.py SOURCE ARTIFACT --json
```

Bloquea cierre si hay:

- cifras del original ausentes en salida.
- fechas del original ausentes en salida.
- URLs del original ausentes en salida.
- frontmatter ausente.
- headings truncados.
- labelese evidente.

La auditoria mecanica es conservadora. Puede dar falsos positivos por cambios
de formato numerico; revisar manualmente antes de declarar perdida.

## Muestreo semantico

Para documentos grandes revisar como minimo:

- inicio del cuerpo sustantivo.
- una seccion media.
- una seccion tardia.
- toda tabla o lista de alta densidad.
- una muestra de definiciones deduplicadas.

## Respuesta a fallos

| Falla | Accion |
| --- | --- |
| Omision | volver al segmento fuente y reincorporar hecho |
| Agregado | eliminar o marcar como inferencia con justificacion |
| IDC bajo | revisar perfil, fat residual, redundancia y realizacion superficial |
| Labelese | rehacer realizacion superficial |
| Tabla/lista degradada | restaurar estructura |
