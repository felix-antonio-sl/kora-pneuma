---
urn: urn:gn:kb:ssot-dgi
nombre: ssot-dgi
version: 1.1.0
estado: borrador
descripcion: "Documento SSOT GORE Ñuble migrado como conocimiento borrador; su estado no implica validación institucional."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-ssot/ssot-dgi.md (sha256:6510c566fcaa3505aea4dfdfb1c1367f37d2a044df8e25e917f5941d1e028ebf); cuerpo preservado íntegramente durante la migración KORA del 2026-08-02."
autor: FS
creado: 2026-03-10
lang: es
tags: [ssot, dgi, indicadores, iniciativas, reportes, senales]
familia: bok
---

# SSOT — DGI (Gestión Institucional)

## Resumen

Departamento de Gestión Institucional — unidad de staff del Administrador Regional. Gestiona indicadores, iniciativas de mejora, reportes y cartera IPR con señal de salud. Dominio mayoritariamente definido en GORE_OS; la ontología y el Omega proveen solo la estructura organizacional.

## Posición orgánica

[ver detalle en estructura orgánica](urn:gn:kb:ssot-organica)

## Roles DGI (4)

| Rol | sort_order | Función |
|-----|---------------|---------|
| JEFE_DGI | 5 | Liderazgo estratégico, supervisión indicadores |
| ESP_CONTROL_GESTION | 6 | Control de gestión, indicadores, cockpit |
| ESP_PROCESOS | 7 | Procesos institucionales, BPMN, DMAIC |
| ESP_TD | 8 | Transformación Digital del Estado |

Population: `"dgi"`. Routing: sidebar DGI (7 ítems) + dashboard DGI cockpit.

[impl: CLAUDE.md §Rules 11, 23]

## Indicadores (5 dimensiones × 3 señales)

| Dimensión | Qué mide | Refresh |
|-----------|---------|---------|
| PRESUPUESTO | Ejecución presupuestaria agregada | Automático |
| CARTERA_IPR | Estado de salud del portafolio IPR | Automático |
| CONVENIOS | Cumplimiento de plazos y estados | Automático |
| TDE | Avance Transformación Digital | Estático (manual) |
| RIESGOS | Alertas y problemas activos | Automático |

Señales: VERDE (normal), AMARILLO (atención), ROJO (crítico).

`POST /api/dgi/data/indicators/refresh` — idempotente, refresca 4/5 dimensiones (TDE estático).

[impl: `ref.category` schemes: `dgi_indicator_dimension`, `dgi_signal`. CLAUDE.md §DGI Layer]

## Iniciativas de mejora

Kanban con WIP limits server-side:

| Columna | WIP máximo |
|---------|-----------|
| EN_CURSO | 5 |
| REVISION | 2 |

`POST /api/dgi/initiatives/{id}/move` → 409 si límite excedido.

Paginación opcional: con `?page=1&page_size=N` → respuesta paginada. Sin parámetros → array plano (Kanban depende de esto).

[impl: CLAUDE.md §Rule 11 — NUNCA cambiar default de paginación]

## Reportes (4 tipos × 6 secciones)

| Tipo | Frecuencia |
|------|-----------|
| FLASH | Ad-hoc |
| SEMANAL | Semanal |
| MENSUAL | Mensual |
| TEMATICO | Por tema |

6 secciones auto-populated: resumen, tabla_indicadores, alertas, avance_dgi, decisiones, prioridades.

Edición de secciones: atomic `jsonb_set` en `metadata` (no read-modify-write). Contenido auto-populated se regenera en cada GET; solo ediciones usuario persisten.

[impl: CLAUDE.md §Rule 21]

## Cartera IPR (portafolio DGI)

Vista unificada de todas las IPR con datos agregados + señal de salud:

| Señal | Significado |
|-------|------------|
| VERDE | Sin problemas |
| AMARILLO | Requiere atención |
| ROJO | Crítico |

Calculada por `_compute_health_signal()`.

3 endpoints: `GET /dgi/cartera` (paginada, post-filter), `GET /dgi/cartera/resumen`, `GET /dgi/cartera/cuotas-vencidas`.

Cockpit drill-down: `/cartera?health_signal=ROJO`.

[impl: CLAUDE.md §DGI Layer — dgi_cartera]

## Esquemas DGI en ref.category

11 schemes: `dgi_initiative_status`, `dgi_indicator_dimension`, `dgi_signal`, `dgi_report_type`, `dgi_report_status`, `dgi_bpmn_status`, `dgi_dmaic_phase`, `dgi_session_status`, `dgi_alert_status`, `dgi_decree_status`, `dgi_source_status`.

Estos schemes NO están en `goreos_seed.sql` — solo en `goreos_model`, copiados a `goreos_test` via COPY.
