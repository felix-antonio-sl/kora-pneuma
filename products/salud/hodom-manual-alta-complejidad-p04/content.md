---
urn: urn:salud:kb:hodom-manual-alta-complejidad-p04
nombre: hodom-manual-alta-complejidad-p04
version: 1.1.1
estado: publicado
descripcion: "Manual de Hospitalizacion Domiciliaria de Alta Complejidad - Parte 04"
fuente: "Migrado de la bestia (~/kora @ 9de5dc38b78c23574d24a481a5f84d70173c2203) artifacts/knowledge/salud/salubrista/hodom/director/02-manual-alta-complejidad--p04.md (sha256:3f17d74a6c4dd5d8d90244a19d29aba0f522d9792254e919f955a0914e17c84f) el 2026-07-17; cuerpo byte-fiel; frontmatter normalizado a ley/2; shard enlazado por cita a urn:salud:kb:hodom-manual-alta-complejidad."
autor: FS
creado: 2026-03-10
lang: es
tags: [hodom, hospitalizacion-domiciliaria, alta-complejidad, hospital-at-home, gestion-clinica]
familia: bok
cita: [urn:salud:kb:hodom-manual-alta-complejidad]
---

# Manual de Hospitalizacion Domiciliaria de Alta Complejidad - Parte 04

## Barreras estructurales de implementacion

### Resistencia cultural, profesional y medico-legal

- Barrera central:
 - percepcion de que el hogar es clinicamente inferior al hospital fisico
- Foco de resistencia:
 - medicos de urgencias
 - especialistas derivadores
- Causas:
 - temor a deterioro subito fuera del hospital
 - mayor carga de decision y coordinacion en urgencias
 - ambiguedad sobre responsabilidad legal en `RPM`
 - preocupacion por mala praxis y cobertura de seguro
- Mitigaciones:
 - presentar HaH como unidad hospitalaria integrada, no como servicio domiciliario ambulatorio
 - demostrar cobertura `24/7` y algoritmos claros de escalamiento
 - retroalimentar resultados del programa en reuniones clinicas
 - generar publicaciones e informes internos
 - incorporar formacion sobre medicina aguda en el hogar en pregrado y residencia

### Integracion de flujos de trabajo

- Cuellos de botella:
 - identificar candidatos a tiempo
 - explicar modelo a la familia
 - coordinar transicion en entornos de urgencias saturados
- Hallazgo operativo:
 - el compromiso del medico de urgencias es el factor mas critico
- Mitigaciones:
 - estrategias `push-pull`
 - alertas automatizadas e `IA` en el `EHR`
 - rol de navegador clinico para recibir referencias y asumir la coordinacion
- Carga de coordinacion:
 - red fragmentada de proveedores
 - cientos de domicilios unicos
 - dependencia de `ultima milla`
- Dato anclado:
 - hasta `20.5%` del tiempo fuera de las visitas puede destinarse a coordinacion no reembolsable
- Ecosistema hibrido:
 - comunicacion en tiempo real entre centro virtual y equipo presencial
 - reglas estrictas sobre que alerta exige visita, ajuste remoto o escalamiento medico
 - interoperabilidad bidireccional `RPM` + logistica + `EHR`

### Brecha digital, alfabetizacion e idioma

- Riesgos:
 - falta de banda ancha
 - conectividad celular insuficiente
 - baja alfabetizacion digital
 - baja literacidad en salud
 - barreras idiomaticas
- Mitigaciones de infraestructura:
 - no depender de internet del paciente
 - kits con conectividad celular integrada
 - `hotspots`
 - dispositivos sin costo para el paciente
- Mitigaciones de usabilidad:
 - equipos de un solo toque o `plug-and-play`
 - herramientas por voz para discapacidad visual o motora
 - `onboarding` estructurado para paciente y cuidador
 - soporte tecnico continuo
- Mitigaciones idiomaticas:
 - software e instrucciones multilingues
 - personal multilingue en centro de comando
 - interpretacion simultanea `24/7`
 - soporte de lengua de senas
 - confirmacion por `teach-back`

## Perspectivas 2026-2030

### Inpatient-at-Home

- Evolucion:
 - elimina dependencia estructural del departamento de urgencias
 - desplaza el triaje aguas arriba hacia comunidad y atencion primaria
- Mecanismo:
 - el paciente es evaluado in situ por `PCP` o equipos moviles
 - si requiere nivel hospitalario, ingresa directo a HaH
 - sin cruzar las puertas del hospital
- Requisitos para APS y grupos medicos:
 - acceso `24/7`
 - triaje de descompensaciones complejas
 - logistica expedita de laboratorio e imagen portatil
 - entrega oportuna de tratamientos agudos
 - personal para visitas domiciliarias de alto contacto
- Barrera financiera:
 - HaH hospitalario retiene ingresos `DRG` superiores a `\$8,000` por episodio
 - `IAH` puro sustituye eso por honorarios profesionales cercanos a `\$717`
- Implicacion:
 - su expansion depende del crecimiento de `VBC`, capitacion y riesgo compartido

### Innovacion biomedica y analitica

- Evolucion esperada:
 - de monitorizacion fisiologica a monitorizacion bioquimica en tiempo real
 - biosensores portatiles
 - `lab-on-a-patch`
 - marcadores metabolicos
 - `IA` predictiva

### Ecosistema ampliado de atencion en hogar

- Horizonte:
 - hasta `25%` de la atencion posaguda y a largo plazo podria entregarse en domicilio
- Verticales proyectadas:
 - quimioterapia domiciliaria
 - `SNF-at-home`
 - rehabilitacion intensiva en el hogar
 - paliativos domiciliarios avanzados
- Fundamentos operativos:
 - reutiliza `RPM`
 - reutiliza logistica de ultima milla
 - permite transicion continua sin cambiar de entorno fisico
- Oncologia:
 - menor exposicion a patogenos nosocomiales
 - deteccion temprana de neutropenia febril o sepsis con monitorizacion continua
- Paliativos:
 - proyeccion demografica `2050`: `1` de cada `6` personas tendra `65` anos o mas
 - cerca de `80%` de adultos mayores vive con `2` o mas enfermedades cronicas
 - `advance care planning` en los primeros `30` dias facilita transicion oportuna a hospicio
- Sinergia organizacional:
 - portafolio combinado `HaH` + `SNF-at-home` + rehabilitacion + paliativos
 - alineacion directa con `ACO` y `bundled payments`

## Tesis operativa del manual

- `HaH` no es simplificacion de cuidados domiciliarios; es extension de hospitalizacion aguda al hogar.
- La fidelidad del modelo depende de:
 - elegibilidad estricta
 - centro de comando virtual `24/7`
 - minimo `1` evaluacion diaria de alto nivel + `2` visitas presenciales
 - logistica de ultima milla robusta
 - interoperabilidad auditable
 - capacidad de escalamiento rapido al hospital fisico
