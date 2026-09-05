---
urn: urn:salud:kb:estandares-it-receta-electronica
nombre: estandares-it-receta-electronica
version: 1.0.0
estado: publicado
descripcion: "Receta Electronica — SNRE v0.9.6: Sistema Nacional de Receta Electronica"
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/salud/estandares-it/receta-electronica-snre.md (sha256:016f8b53843c598312b8428774a7f176ed8982be197efc954ef8c01e1551a933) el 2026-06-12; cuerpo byte-fiel (renombrado de receta-electronica-snre.md a estandares-it-receta-electronica.md por lugar-coincide). Fuente original: SNRE IG 0.9.6 (MINSAL, draft). Ley 21.541 Salud Digital. consulta_reglamento_receta_electronica.pdf"
autor: FS
creado: 2026-05-08
lang: es
tags: [salud, receta-electronica, snre, fhir, interoperabilidad, chile]
familia: bok
cita: [urn:salud:kb:estandares-it-indice, urn:salud:kb:informatica-medica-normativa-chilena]
---

# Receta Electronica — SNRE v0.9.6

Sistema Nacional de Receta Electronica. Guia de Implementacion FHIR para
prescripcion electronica en Chile.

## Marco legal

- **Ley 21.541** (Salud Digital, 2024): establece la receta electronica como obligatoria
- **Reglamento en consulta publica** (2026): detalla requisitos tecnicos
- **SNRE** v0.9.6: guia FHIR para implementacion

## Recursos FHIR involucrados

| Recurso | Uso |
|---------|-----|
| **MedicationRequest** | Prescripcion del medico |
| **Medication** | Medicamento especifico |
| **MedicationDispense** | Dispensacion en farmacia |
| **Patient** | Paciente (con RUN) |
| **Practitioner** | Medico prescriptor (con RUN) |
| **PractitionerRole** | Rol y lugar de prescripcion |
| **Coverage** | Cobertura (FONASA, ISAPRE) |

## Flujo de receta electronica

1. **Prescripcion**: medico crea MedicationRequest en sistema clinico (HODOM)
2. **Validacion**: CDSS verifica interacciones, alergias, dosis
3. **Firma**: firma electronica avanzada del medico
4. **Transmision**: a repositorio nacional (SNRE)
5. **Dispensacion**: farmacia consulta SNRE y dispensa
6. **Registro**: MedicationDispense confirma dispensacion

## Implicaciones para HODOM-HSC

- El medico HODOM prescribe en domicilio → receta electronica obligatoria
- Medicamentos administrados por cuidador → deben quedar registrados en SNRE
- Medicacion EV ambulatoria → prescribe igual que cualquier receta
- Opioides y controlados → receta retenida con receta electronica (doble via)
- Firma electronica: el medico HODOM necesita token o clave unica
