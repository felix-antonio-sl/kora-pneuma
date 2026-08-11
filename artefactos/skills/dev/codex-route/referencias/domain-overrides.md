# Modificadores por dominio

Aplicar después de CEM-8 y SGM-8. Son defaults refutables, no recetas.

| Dominio | Topología inicial | Restricción dominante |
|---|---|---|
| Matemática rutinaria | S0/S1 | oráculo exacto |
| Demostración abstracta | S4 | candidatas aisladas, adjudicación posterior |
| Demostración formal | S4 + S8 | proof checker separado de candidatas |
| Cambio de código local | S0 | un escritor y test focal |
| Bug con causa desconocida | S4 | hipótesis falsables e independientes |
| Feature modular | S6 o S9 | interfaces y write sets explícitos |
| Arquitectura | S2 o S6 | perspectivas independientes, decisión central |
| Diseño de datos | S6 | integridad, workload, operaciones y seguridad |
| Migración productiva | S2 preflight → S3 ejecución | lectura paralela, cambio serial, gate humano |
| Diagnóstico clínico | S4 | hipótesis independientes, evidencia, profesional decide |
| Manejo clínico | S3 | evidencia→contraindicaciones→monitorización→síntesis; gate clínico |
| Interoperabilidad | S5 + S6 | aristas de gobernanza, organización, semántica, técnica y seguridad |
| Ideas creativas | S4 | divergencia aislada, crítica y selección posterior |
| Investigación profunda | S6/S7 | evidencia estructurada, no conversación libre |
| Corpus de conocimiento | S7 | mappers homogéneos, reducer y auditor |
| Producto y UX | S4 → S6 | separar alternativas de implementación |
| Datos masivos | S7 | mappers sin comunicación |
| Optimización | S8 | baseline, métrica fija, keep/revert |
| Auditoría de repositorio | S2/S7 | resultados con rutas al integrador |

## Alta consecuencia

Para salud, legal, seguridad, finanzas o producción:

- aumentar verificación y reducir autonomía;
- separar evidencia, inferencia y decisión;
- mantener candidatas independientes cuando el anclaje sea un riesgo;
- reservar la decisión aplicada a la autoridad humana competente;
- no convertir consenso de agentes en autorización.

## Diagnóstico clínico

Primera fase: hipótesis no se comunican. Segunda: evidencia común puede
entregarse a cada hipótesis. Tercera: la directora sintetiza incertidumbre y un
profesional decide. No ejecutar manejo clínico solo por convergencia del grafo.

## Interoperabilidad

Ejemplo de árbol:

```text
/root
├── governance
├── organizational
├── semantic
│   ├── terminology
│   └── data-model
├── technical
└── security
```

Aristas laterales siguen interfaces: governance→organizational,
organizational→semantic, semantic→technical y security→contratos relevantes.
No habilitar una malla libre.

## Arquitectura de software

Seguridad, rendimiento, datos, operabilidad y mantenibilidad pueden trabajar
como perspectivas S2. La directora adjudica trade-offs. Abrir `CHALLENGE`
selectivo después de la primera entrega, no consenso continuo.
