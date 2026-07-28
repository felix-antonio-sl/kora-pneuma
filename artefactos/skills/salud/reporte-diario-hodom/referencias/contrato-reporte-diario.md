# Contrato del reporte diario HODOM

## Productos por modo

| Modo | Producto | Comparación |
|---|---|---|
| `CORTE-0800` | Reporte completo del estado vigente | Establece manifiesto basal |
| `ACTUALIZACION-1100` | Reporte completo actualizado | Delta contra manifiesto de las 08:00 |

Ambos cortes usan fecha y hora de `America/Santiago`. El manifiesto contiene
las llaves necesarias para comparar cortes: identificador, episodio, estado
categorial, pendientes categoriales, barreras de alta, clasificación de
candidatura y hash del bloque clínico. Incluye además el ledger factual de
proveniencia definido en `playbook-hsc-agent-cli.md`. Vive junto al reporte.

## Portada y control

- `USO INTERNO — REPORTE CLÍNICO-OPERACIONAL`.
- Fecha operacional, hora efectiva y modo.
- Destinatario: Dirección Técnica / Médico Regulador HODOM.
- Fuentes consultadas y hora de adquisición.
- Integridad del censo y fuentes no observadas.
- Alcance: apoyo a decisión; requiere validación humana.

## Resumen ejecutivo

- total HODOM observado;
- episodios direccionables y no direccionables;
- estado agregado: mejora, estable, deterioro o no verificable;
- altas posibles sujetas a validación;
- altas bloqueadas y causas principales;
- conflictos de fuente;
- candidatos por servicio y clasificación;
- alertas inmediatas.

Los agregados deben poder rastrearse a bloques individuales, sin copiar la
ficha completa.

Límite editorial: hasta 700 palabras.

## Brief obligatorio por paciente HODOM

```text
Nombre:
RUT:
Edad:
Servicio / ubicación:
Ingreso / días:

En qué estamos
- Motivo y contexto:
- Problema dominante:
- Tendencia:
- Soporte objetivo:
- Tratamiento o soporte relevante:

Pendientes
- Clínicos:
- Diagnósticos:
- Terapéuticos:
- Coordinación / continuidad:

Qué falta para alta HODOM
- Estabilidad o resolución:
- Plan ambulatorio y seguimiento:
- Medicación / insumos:
- Educación y comprensión:
- Red de seguridad / contacto:
- Responsable humano:

Acción inmediata:
Observación:
```

Si un campo no pudo observarse, usar `no verificable con las fuentes
disponibles`; nunca completar por plausibilidad.

Cada brief debe apuntar a sus evidencias del ledger y tener hasta 350 palabras.
Una incidencia técnica sin impacto en la conducta queda en el ledger, no se
repite como observación narrativa.

## Candidatos desde hospital

Agrupar por:

1. Unidad de Emergencia;
2. Medicina;
3. Traumatología;
4. Cirugía / Área Quirúrgica.

Bloque por candidato:

```text
Nombre:
RUT:
Edad:
Servicio / ubicación:
Motivo y estado actual:
Razón de preselección censal:
Clasificación:
Verificaciones faltantes:
Barreras o exclusiones observadas:
Acción / responsable:
Observación:
```

La frase `preselección censal; no constituye aceptación HODOM` debe aparecer
en el encabezado de la sección y en toda conclusión agregada.

El censo liviano no se vuelca al informe. El reporte conserva conteos agregados
por servicio y solo bloques de pacientes profundizados. Cada bloque tiene hasta
180 palabras y un `selection_reason` en el ledger. `informacion-insuficiente`
es una cola de verificación separada, no una candidatura ni una instrucción de
materializar el servicio completo.

## Proveniencia mínima

Cada afirmación factual del brief o de un candidato conserva:

```text
requested_handle
source
fetched_at
state
error_code
identity_status
source_issues
discrepancies
evidence_path
evidence_class
```

`evidence_class` admite `hecho`, `inferencia`, `pendiente` o
`no-verificable`. Una inferencia enlaza los hechos que la sustentan. Los
metadatos técnicos prueban procedencia y adquisición en el alcance declarado;
no prueban utilidad clínica ni aprobación humana.

## Delta de las 11:00

| Dimensión | 08:00 | 11:00 | Cambio | Fuente / límite |
|---|---|---|---|---|
| Censo HODOM |  |  |  |  |
| Altas potenciales |  |  |  |  |
| Alertas |  |  |  |  |
| Conflictos |  |  |  |  |
| Candidatos |  |  |  |  |

Después de la tabla, listar cambios por paciente sin repetir bloques que no
cambiaron. El resto del documento sigue siendo un reporte completo.

## Evidencia y observaciones

Toda discrepancia usa este patrón:

```text
Observación: [fuente A] informa [...] y [fuente B] informa [...].
Impacto: [...]
Pendiente para resolver: [...]
```

Estados epistémicos permitidos:

- `verificado`: observado en esta ejecución;
- `inferido`: conclusión clínica explícitamente fundada;
- `pendiente`: requiere dato o validación humana;
- `no verificable`: fuente requerida no disponible o censo incompleto.

## Gates de cierre

| Gate | Criterio |
|---|---|
| `G2-census` | Conteo de briefs conciliado con censo observado |
| `G3-brief` | Cada paciente tiene estado, pendientes y requisitos de alta |
| `G4-conflict` | Toda discrepancia material aparece como `Observación` |
| `G5-services` | Urgencia, Medicina, Traumatología y Cirugía fueron consultados o declarados no observables |
| `G6-candidates` | Toda candidatura se rotula como preselección censal |
| `G7-delta` | A las 11:00 hay delta verificable o `baseline-unavailable` |
| `G8-docx` | DOCX abre como ZIP válido y contiene las secciones obligatorias |
| `G9-provenance` | Cada afirmación factual conserva handle, fuente, tiempo, estado y ruta de evidencia |
| `G10-utility` | Respeta límites editoriales, no vuelca censos ni repite boilerplate sin impacto decisional |
| `G11-funnel` | Handles materializados de candidatos = handles seleccionados; ningún no candidato recibe conducta de evaluación formal |

Un gate fallido impide declarar el reporte como cerrado.

Para `G5-services`, cada uno de los cuatro servicios aparece como `observado` o
`no observable en este corte` con causa. Una búsqueda sin candidatos sigue
siendo una búsqueda y debe quedar documentada.
