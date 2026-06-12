---
urn: urn:salud:kb:informatica-medica-normativa-chilena
nombre: informatica-medica-normativa-chilena
version: 1.0.0
estado: publicado
descripcion: "Normativa Chilena de IT en Salud — HODOM-HSC: Obliga interoperabilidad entre todos los prestadores"
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/salud/informatica-medica/normativa-chilena-it-salud.md (sha256:13139d9df5697546978d0271c43dee7dd0781df1aae97440a6f12020e63918a9) el 2026-06-12; cuerpo byte-fiel (renombrado de normativa-chilena-it-salud.md a informatica-medica-normativa-chilena.md por lugar-coincide). Fuente original: Zotero + web MINSAL. Leyes 21.663, 21.719, 21.541, 21.668, 21.180, 21.331. Decreto 12. RIS/SNI 2025."
autor: FS
creado: 2026-05-07
lang: es
tags: [salud, normativa, chile, interoperabilidad, ciberseguridad, hodom]
familia: bok
cita: [urn:salud:kb:informatica-medica-indice, urn:salud:kb:hodom-reglamento-ds1-2022]
---

# Normativa Chilena de IT en Salud — HODOM-HSC

## Leyes aplicables

### Ley 21.668 — Interoperabilidad Ficha Clinica
Obliga interoperabilidad entre todos los prestadores. HODOM debe interoperar
con el sistema hospitalario. Estandares: HL7 FHIR R4, SNOMED CT, EMPI.

### Ley 21.541 — Salud Digital
Telemedicina reconocida. Receta electronica. Identidad digital del paciente.

### Ley 21.663 — Ciberseguridad
HODOM como servicio esencial: SGSI continuo, planes de continuidad certificables,
reporte de incidentes al CSIRT en <3h.

### Ley 21.719 — Datos Personales
Datos de salud = sensibles. Consentimiento, confidencialidad, derechos ARCO.

### Decreto 12 — Interoperabilidad
Arquitectura nacional, perfiles FHIR Core CL, servicios terminologicos.

### RIS/SNI 2025
Conjunto minimo de datos, estandares de codificacion, formatos de intercambio.

## Implicaciones para software HODOM-HSC

1. FHIR R4 nativo con perfiles Core CL chileno
2. SNOMED CT para codificacion clinica
3. SGSI + planes de continuidad documentados
4. Consentimiento informado digital y confidencialidad
5. Interoperabilidad bidireccional HODOM ↔ hospital
