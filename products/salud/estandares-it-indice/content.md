---
urn: urn:salud:kb:estandares-it-indice
nombre: estandares-it-indice
version: 1.0.0
estado: publicado
descripcion: "Estandares IT en Salud — Chile: Catalogo de estandares tecnicos vigentes para interoperabilidad en salud en Chile"
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/salud/estandares-it/indice-estandares-it-salud.md (sha256:1323816c9b8ad972351c1615679a7d19def01705c7ac61a6a0cf43730217a268) el 2026-06-12; cuerpo byte-fiel (renombrado de indice-estandares-it-salud.md a estandares-it-indice.md por lugar-coincide). Fuente original: Web MINSAL interoperabilidad (marzo-abril 2026). HL7 Chile Connectathon 2026. Consolidacion web 03_web_fuentes."
autor: FS
creado: 2026-05-08
lang: es
tags: [salud, estandares, fhir, hl7, snomed-ct, minsal, interoperabilidad, chile]
familia: bok
cita: [urn:salud:kb:informatica-medica-indice, urn:salud:kb:informatica-medica-normativa-chilena]
---

# Estandares IT en Salud — Chile

Catalogo de estandares tecnicos vigentes para interoperabilidad en salud en Chile.
Fuentes: documentacion oficial MINSAL, HL7 Chile, CENS.

## Guias de Implementacion FHIR MINSAL

| Guia | Version | Estado | URL |
|------|---------|--------|-----|
| **Core CL** | 1.9.4 | trial-use | Perfil FHIR base chileno (Paciente, Prestador, Organizacion, Direccion) |
| **NID** | 0.4.8 | draft | Nucleo de Interoperabilidad de Datos: MPI (paciente), HPD (profesional) |
| **SNRE** | 0.9.6 | draft | Sistema Nacional de Receta Electronica |
| **TEI** | 0.1.6 | draft | Terminologias y Estandares de Interoperabilidad |

## Servicios Transversales

| Servicio | Proposito | Estado |
|----------|-----------|--------|
| **EMPI** | Enterprise Master Patient Index — identidad unica del paciente | Activo |
| **Servicios Terminologicos** | SNOMED CT Chile, CIE-10, CIE-11 | Activo |
| **PISEE** | Plataforma de Integracion de Sistemas de Informacion | Activo |
| **DEIS** | Norma EIS para estadisticas e indicadores en salud | Activo |

## Arquitectura Nacional

La arquitectura de interoperabilidad MINSAL define:
- Capa de datos: FHIR R4 como formato de intercambio
- Capa de identidad: EMPI como fuente unica de paciente
- Capa terminologica: SNOMED CT Chile como estandar
- Capa de seguridad: autenticacion, autorizacion, auditoria
- Capa de intercambio: HIE (Health Information Exchange) nacional

## HL7 Chile

- **Connectathon 2026**: evento de pruebas de interoperabilidad con perfiles Core CL
- **Perfiles activos**: Paciente, Prestador, Organizacion, Documento Clinico, Receta
- **Proximo**: Observacion, Diagnostico, Procedimiento, Alergia, Inmunizacion

## Archivos derivados

- `urn:salud:kb:estandares-it-core-cl` — Core CL v1.9.4 (perfil FHIR chileno)
- `urn:salud:kb:estandares-it-snomed-ct` — SNOMED CT Chile y servicios terminologicos
- `urn:salud:kb:estandares-it-receta-electronica` — SNRE y receta electronica
