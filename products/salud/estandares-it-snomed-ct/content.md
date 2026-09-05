---
urn: urn:salud:kb:estandares-it-snomed-ct
nombre: estandares-it-snomed-ct
version: 1.0.0
estado: publicado
descripcion: "SNOMED CT Chile — Servicios Terminologicos MINSAL: SNOMED CT (Systematized Nomenclature of Medicine — Clinical Terms) es el"
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/salud/estandares-it/snomed-ct-chile.md (sha256:8fda2e835d4b482574224eb1afc440fedf15752359e40d4891961bdb0f7d6d76) el 2026-06-12; cuerpo byte-fiel (renombrado de snomed-ct-chile.md a estandares-it-snomed-ct.md por lugar-coincide). Fuente original: Servicios Terminologicos MINSAL. interoperabilidad_minsal_servicios_terminologicos.html. TEI IG 0.1.6."
autor: FS
creado: 2026-05-08
lang: es
tags: [salud, snomed-ct, terminologia, chile, codificacion, minsal]
familia: bok
cita: [urn:salud:kb:estandares-it-indice]
---

# SNOMED CT Chile — Servicios Terminologicos MINSAL

## SNOMED CT en Chile

SNOMED CT (Systematized Nomenclature of Medicine — Clinical Terms) es el
estandar terminologico adoptado por MINSAL para codificacion clinica en
todos los sistemas de salud publica chilenos.

### Componentes

| Componente | Descripcion | Ejemplo HODOM |
|-----------|-------------|---------------|
| **Conceptos** | Unidades de significado clinico (conceptId) | 444896004 |Neumonia| |
| **Descripciones** | Terminos asociados a cada concepto | Neumonia, Pneumonia, Pulmonia |
| **Relaciones** | Vinculos entre conceptos (is-a, finding-site, causative-agent) | Neumonia is-a Infeccion respiratoria |
| **Refsets** | Subconjuntos para uso especifico | Refset Chileno de Diagnosticos HODOM |

### Jerarquias principales para HODOM

- **Procedimiento** (71388002): curacion, administracion de medicamentos, manejo de dispositivos
- **Trastorno** (64572001): diagnosticos de ingreso y egreso HODOM
- **Hallazgo clinico** (404684003): signos vitales, examen fisico
- **Situacion** (243796009): contexto social, cuidador, entorno domiciliario
- **Objeto fisico** (260787004): dispositivos medicos, insumos domiciliarios

### Criterios de uso para HODOM-HSC

1. **Diagnostico de ingreso**: concepto SNOMED CT del motivo de hospitalizacion
2. **Diagnostico de egreso**: concepto SNOMED CT al alta (puede diferir del ingreso)
3. **Procedimientos HODOM**: curaciones, manejo de cateteres, administracion de medicamentos
4. **Dispositivos**: cateteres, sondas, BIPAP, oxigeno domiciliario
5. **Evaluacion social**: presencia de cuidador, condiciones del domicilio

### Servicios terminologicos MINSAL

- **API de validacion**: verificar que un conceptId es valido y esta activo
- **API de busqueda**: encontrar conceptos por termino (espanol)
- **API de refsets**: obtener subconjuntos especificos (ej. diagnosticos HODOM)
- **Endpoint base**: `https://terminologias.minsal.cl/fhir/`

### Mapeo con CIE-10

Para cumplimiento con DEIS (estadisticas), SNOMED CT debe mapear a CIE-10:
- Todo diagnostico de egreso requiere codigo CIE-10
- MINSAL publica tablas de equivalencia SNOMED-CT ↔ CIE-10
- El mapeo es 1:N (un concepto SNOMED puede equivaler a varios CIE-10)
