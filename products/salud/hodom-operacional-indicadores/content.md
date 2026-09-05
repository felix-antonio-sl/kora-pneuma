---
urn: urn:salud:kb:hodom-operacional-indicadores
nombre: hodom-operacional-indicadores
version: 1.0.0
estado: publicado
descripcion: "Indicadores de produccion HODOM — Benchmark operativo real: Datos reales de 14 meses (dic 2024 - ene 2026) de la UHD del Hospital San Carlos"
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/salud/hodom-operacional/indicadores-produccion.md (sha256:e33009c4151d7e6f5637be1f74f547f7367bc7468e955ad1715697ee0175d019) el 2026-06-12; cuerpo byte-fiel (renombrado de indicadores-produccion.md a hodom-operacional-indicadores.md por lugar-coincide). Fuente original: Informe resumen mensual HODOM HSC 14 meses (salubrista-hah output). INBOX/consolidacion_temp/"
autor: FS
creado: 2026-05-07
lang: es
tags: [salud, hodom, indicadores, produccion, ocupacion, estadia, benchmarking]
familia: bok
cita: [urn:salud:kb:hodom-operacional-indice, urn:salud:kb:hodom-direccion-tecnica]
---

# Indicadores de produccion HODOM — Benchmark operativo real

Datos reales de 14 meses (dic 2024 - ene 2026) de la UHD del Hospital San Carlos.
726 ingresos, 747 altas, 1 fallecido en 427 dias operativos.

## Indicadores clave

| Indicador | Valor | Tendencia | Alerta |
|-----------|-------|-----------|--------|
| Indice Ocupacional promedio | 89.8% | Descendente (137% → 70%) | Baja |
| Estadia promedio (PDE) | 7.4 → 10.8 dias | +46% | Alta |
| Dias paciente agudo (DPA) | Variable | Estable | — |
| Tasa de reingreso | No reportada | — | Brecha |
| Mortalidad | 0.13% (1/747) | — | Bajo |

## Hallazgo principal

**Estancamiento por prolongacion de estadia, no por falta de demanda.**
El indice ocupacional baja porque los pacientes permanecen mas tiempo, no porque
ingresen menos. Esto es opuesto a un problema de "falta de camas": hay camas
disponibles pero los pacientes no egresan oportunamente.

## Interpretacion operativa

1. La PDE subio de 7.4 a 10.8 dias (+46%): posible cambio en el case mix
 (pacientes mas complejos), insuficiente gestion de altas, o barreras en la
 transicion al egreso (falta de cuidador, tramites administrativos, espera
 de insumos).
2. El IO descendente NO es un problema de subutilizacion — es consecuencia del
 alargamiento de estadia. Las camas estan ocupadas mas tiempo por los mismos
 pacientes.
3. La expansion de 16 a 20 camas (sep 2025) debe evaluarse contra la PDE:
 mas camas con estadia prolongada = mas pacientes simultaneos = mayor
 carga operativa sin necesariamente mayor productividad.

## KPIs recomendados para monitoreo continuo

- PDE por grupo diagnostico (seguimiento semanal)
- Tasa de reingreso a hospitalizacion tradicional <30d
- Tiempo desde indicacion de alta medica hasta egreso efectivo
- Motivos de prolongacion de estadia categorizados
- Indice ocupacional ajustado por complejidad (case mix index)
