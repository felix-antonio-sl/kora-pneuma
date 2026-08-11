# Restricciones y fases por dominio

Aplicar después de CEM-8 y SGM-8. El dominio no decide por sí solo un grafo.
Declarar una base y separar fases, modificadores y subgrafos:

```yaml
base_topology: S6
phases:
  - {name: discovery, topology: S2}
  - {name: implementation, topology: S6}
modifiers: [hierarchical-governance]
local_subgraphs: []
```

No sumar códigos en un campo `topology`.

| Dominio o señal | Base inicial | Restricción |
|---|---|---|
| Operación matemática rutinaria | S0 Luna | checker exacto |
| Demostración abstracta rival | S4 Sol | candidatas aisladas, adjudicación posterior |
| Cambio de código local | S0 | un escritor y test focal |
| Bug con causa desconocida | S4 Sol | hipótesis falsables independientes |
| Feature modular | S6 o S9 | interfaces y write sets demostrablemente estables |
| Diseño de datos | S6 | integridad, workload, operación y seguridad |
| Migración productiva | S3 | discovery S2 como fase previa; ejecución serial y gate humano |
| Investigación o corpus | S7 | schema homogéneo, reducer y auditor |
| Optimización | S8 | oracle fijo, iteración acotada y rollback |

## Clínica

- Caso simple o resumen diagnóstico: S0; Sol o Luna según juicio residual.
- Diferencial complejo con hipótesis rivales: S4 Sol, candidatas aisladas y
  profesional adjudicador.
- Manejo clínico: **Sol monosession** con integración central. Añadir sidecars
  de farmacología, evidencia o contraindicaciones solo si aportan una entrada
  independiente. Un pipeline no debe fragmentar la visión del paciente.

Separar evidencia, inferencia y decisión. Un grafo nunca autoriza una decisión
clínica aplicada.

## Arquitectura

Una decisión local puede ser `S0 · Sol high`. Usar S2 solo si perspectivas
independientes reducen sesgo; usar S6 solo con contratos cruzados estables. La
directora adjudica seguridad, datos, rendimiento, operabilidad y mantenibilidad.

## Creatividad

Ideas rutinarias: `S0 · Luna medium`. Usar S4 solo si la diversidad
independiente justifica candidatas aisladas y crítica posterior.

## Interoperabilidad

Usar S6 como base. Añadir `hierarchical-governance` solo si el sistema tiene
capas reales de gobernanza, organización, semántica, técnica y seguridad. Las
aristas laterales siguen interfaces; no habilitar una malla por el nombre del
dominio.

## Alta consecuencia

En salud, legal, seguridad, finanzas o producción: aumentar verificación,
reducir autonomía, conservar autoridad humana y no convertir consenso de
sesiones en autorización.
