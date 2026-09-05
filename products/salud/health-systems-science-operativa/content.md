---
urn: urn:salud:kb:health-systems-science-operativa
nombre: health-systems-science-operativa
version: 1.0.0
estado: publicado
descripcion: "Logica operativa de salud: demanda, oferta y acceso: Lillrank caracteriza healthcare como:"
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/salud/health-systems-science/logica-operativa-salud.md (sha256:d229729e1f1a2bfb452ef6013332b807c3cd3caf9ea01d69499a37e3138dbd86) el 2026-06-12; cuerpo byte-fiel (renombrado de logica-operativa-salud.md a health-systems-science-operativa.md por lugar-coincide). Fuente original: The Logics of Healthcare (Lillrank 2018), Caps. 5-6. pdftotext conversion."
autor: FS
creado: 2026-05-07
lang: es
tags: [salud, demanda, oferta, colas, triaje, capacidad, acceso, estratificacion]
familia: bok
cita: [urn:salud:kb:health-systems-science-indice, urn:salud:kb:management-engineering-ext-capacidad, urn:salud:kb:gestion-redes-urgencias, urn:salud:kb:gestion-redes-general]
---

# Logica operativa de salud: demanda, oferta y acceso

## Healthcare como tipo especial de servicio

Lillrank caracteriza healthcare como:

1. **Necesidad, no deseo**: el paciente no "quiere" estar enfermo
2. **Asimetria de informacion**: el medico sabe mas que el paciente
3. **Incertidumbre radical**: el resultado no es deterministico
4. **Coproduccion obligatoria**: el paciente debe participar en su cuidado
5. **Externalidades**: la salud individual afecta a la comunidad (vacunas, TB)
6. **Bien de merito**: la sociedad decide que todos deben tener acceso

Estas caracteristicas hacen que el "mercado" de salud no funcione como otros
mercados. Los precios no equilibran oferta y demanda naturalmente.

## Demanda en salud

### Componentes de la demanda

- **Necesidad**: condicion que se beneficiaria de atencion medica (objetiva)
- **Demanda expresada**: necesidad que busca atencion (subjetiva)
- **Utilizacion**: atencion efectivamente recibida
- **Demanda inducida por oferta (SID)**: atencion generada por el sistema, no
 por necesidad del paciente (Roemer's law: "a bed built is a bed filled")

### Estratificacion de la demanda

No toda la demanda es igual:

| Nivel | Poblacion | Estrategia |
|-------|-----------|-----------|
| Alto riesgo (5%) | Cronicos complejos, multimorbidos | Gestion intensiva de casos |
| Riesgo medio (15%) | Cronicos estables | Gestion de enfermedades |
| Bajo riesgo (80%) | Sanos, agudos leves | Autocuidado, atencion primaria |

Kaiser Permanente pyramid adaptado por Lillrank para sistemas universales.

## Oferta y capacidad

### Tipos de capacidad

- **Capacidad nominal**: camas, consultorios, quirofanos (infraestructura)
- **Capacidad efectiva**: personal disponible, equipamiento funcional
- **Capacidad real**: la que se puede usar considerando variabilidad

### Barreras de acceso

Lillrank distingue:
- **Acceso fisico**: distancia, transporte
- **Acceso financiero**: costo, seguro
- **Acceso cultural**: lenguaje, creencias, estigma
- **Acceso administrativo**: burocracia, horarios, listas de espera
- **Acceso clinico**: triaje, criterios de inclusion

## Colas y espera en salud

La cola NO es necesariamente ineficiente. Es una herramienta de gestion cuando
la demanda excede la oferta instantanea.

### Tipos de colas en salud

1. **Cola de acceso**: espera para primera consulta (GP, especialista)
2. **Cola de procedimiento**: espera para cirugia electiva, imagenologia
3. **Cola de cama**: espera en urgencias por cama disponible (boarding)
4. **Cola de alta**: espera por cupo en post-agudo, HODOM, rehabilitacion

### Priorizacion y triaje

No es FIFO (first-in-first-out). La salud usa:
- **Triaje clinico**: severidad, riesgo vital (ESI 1-5, Manchester)
- **Priorizacion por necesidad**: tiempo maximo de espera clinica
- **Priorizacion por eficiencia**: pacientes "rapidos" que liberan capacidad

### Gestion de colas

Estrategias para reducir espera sin aumentar capacidad:
1. **Pooling**: compartir recursos entre servicios
2. **Load leveling**: distribuir demanda en el tiempo (cirugia electiva vs emergencia)
3. **Fast track**: carril rapido para casos simples
4. **See and treat**: atencion en el primer contacto sin derivacion
5. **Reducir variabilidad**: protocolos, estandarizacion de procesos

## Implicaciones para HODOM

La hospitalizacion domiciliaria actua como valvula de capacidad en el sistema:
- **Descongestiona camas**: pacientes que no requieren infraestructura hospitalaria
- **Reduce cola de alta**: acelera egreso de pacientes cronicos estables
- **Crea capacidad virtual**: "camas" que no requieren espacio fisico
- **Segmenta la demanda**: pacientes HODOM vs hospitalizados tradicionales
