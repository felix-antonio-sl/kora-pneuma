---
urn: urn:salud:kb:hodom-manual-alta-complejidad
nombre: hodom-manual-alta-complejidad
version: 1.1.1
estado: publicado
descripcion: "Manual de Hospitalizacion Domiciliaria de Alta Complejidad"
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/salud/salubrista/hodom/director/02-manual-alta-complejidad.md (sha256:c8379325ee83d5a91c1a37084c9144ae76d49bec4f78cf01225631699dbd7da3) el 2026-06-12; cuerpo byte-fiel (renombrado de 02-manual-alta-complejidad.md a hodom-manual-alta-complejidad.md por lugar-coincide). Fuente original: source/pro/hodom/manual-general-hodom-2026.md"
autor: FS
creado: 2026-03-10
lang: es
tags: [hodom, hospitalizacion-domiciliaria, alta-complejidad, hospital-at-home, gestion-clinica]
familia: bok
---

# Manual de Hospitalizacion Domiciliaria de Alta Complejidad


## Fundamentos del modelo Hospital at Home

### Definicion y taxonomia

- `Hospital at Home` (`HaH`) = servicio agudo que sustituye hospitalizacion tradicional trasladando personal, equipos, tecnologia, medicacion y capacidades hospitalarias al domicilio.
- No equivale a:
 - `home health` de baja complejidad
 - cuidado ambulatorio esporadico
 - paliativos tradicionales sin soporte agudo equivalente a sala
- Rasgos distintivos:
 - evaluacion medica y de enfermeria diaria
 - terapias intravenosas
 - diagnostico movil
 - monitorizacion continua
- Distincion central:
 - el "hospital" se define por intensidad clinica, tratamientos y outcomes
 - no por infraestructura fisica `brick-and-mortar`

### Evolucion historica y adopcion global

- Primeros ensayos:
 - Reino Unido
 - fines de la decada de `1970`
- Adopcion consolidada:
 - Australia
 - Canada
 - Israel
- Victoria, Australia:
 - todos los hospitales regionales y metropolitanos con programa HaH
 - gestion aproximada de `6%` de los dias-cama del estado
- Estados Unidos:
 - programa fundacional en Johns Hopkins
 - decada de `1990`
 - referencia operativa `1995`
 - liderazgo: Bruce Leff
- Vias clinicas fundacionales:
 - neumonia adquirida en la comunidad
 - insuficiencia cardiaca congestiva
 - `EPOC`
 - celulitis

### Triple objetivo y valor sanitario

| Dimension | Hechos anclados |
| ------------------- | ------------------------------------------------------------------------------------------------------ |
| Experiencia | Mayor confort, mejor sueno, mayor dignidad, mayor apoyo emocional |
| Resultados clinicos | Delirium `24%` a `9%`; readmision a `30` dias `23%` a `7%`; mortalidad menor o no inferior |
| Funcion | Sedentarismo `78.0%` vs `86.0%`; tiempo en cama `18%` vs `55%`; pasos diarios `834` vs `120` |
| Economia | Ahorro por episodio entre `19%` y mas de `30%`; Johns Hopkins `32%` menos costo (`$5,081` vs `$7,480`) |

## Arquitectura de admision

| Modelo | Descripcion | Ventaja principal | Riesgo principal |
| --------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------- |
| Evitacion de ingreso | Admision directa desde urgencias, clinicas comunitarias o derivacion ambulatoria | Menor mortalidad, mayor ahorro, alivio de congestion | Sobreutilizacion o admision inapropiada |
| Alta temprana apoyada | Traslado al hogar tras estancia corta intrahospitalaria | Menor riesgo de admision inadecuada; facilita adopcion inicial | Ahorro mas atenuado por costos iniciales y duplicacion transicional |

- Variante emergente:
 - `Inpatient-at-Home`
 - triaje directo desde atencion primaria o comunidad
 - evita incluso el paso por urgencias
- Diseno operativo recomendado:
 - iniciar con `step-down` para consolidar confianza y logistica
 - expandir luego a `step-up` para maximizar retorno y liberacion de camas

## Criterios de inclusion y exclusion medica

### Inclusion

- Requisito basal:
 - necesidad documentada de cuidados agudos de nivel hospitalario
- Validacion de utilizacion:
 - `InterQual`
 - `MCG Health`
 - `Dragonfly`
- Condiciones de ingreso:
 - estabilidad hemodinamica suficiente para manejo seguro en domicilio
 - ausencia de necesidad de resucitacion o soporte vital continuo
 - plan terapeutico definido
 - trayectoria clinica previsible
- Perfil frecuente:
 - pacientes de `65` anos o mas
 - multimorbilidad
 - alto riesgo de delirium, infeccion nosocomial, caidas o declive funcional si permanecen hospitalizados

### Exclusiones y contraindicaciones absolutas

- shock
- infarto agudo de miocardio
- necesidad de `UCI` o atencion intensiva previsible
- reintervencion quirurgica inminente
- procedimientos invasivos recurrentes:
 - punciones lumbares
 - biopsias multiples
- necesidad continua o repetida de imagenologia avanzada no movilizable:
 - tomografia computarizada
 - resonancia magnetica
- requerimiento rutinario de sustancias controladas no aptas para el domicilio
- dependencia funcional que exige mas de una persona para transferencias basicas

- Exigencia transversal:
 - evaluar la trayectoria probable de la enfermedad
 - anticipar escalamiento o necesidad de reoperacion
 - mantener protocolo de retorno expedito al hospital fisico

## Insuficiencia cardiaca congestiva

- Triaje:
 - sobrecarga de volumen aguda
 - necesidad de diureticos IV
 - sin shock cardiogenico
 - sin isquemia aguda
 - sin necesidad de telemetria intensiva o `UCI`
- Monitorizacion:
 - peso diario
 - presion arterial
 - frecuencia cardiaca
 - oximetria
- Intervenciones:
 - diureticos de asa IV
 - titulacion segun respuesta
 - control de electrolitos con flebotomia domiciliaria
 - restriccion de sodio y fluidos

## EPOC y asma

- Triaje:
 - disnea, tos o esputo con necesidad de intensificacion terapeutica
 - sin intubacion
 - sin ventilacion mecanica no invasiva de soporte vital continuo
- Monitorizacion:
 - `SpO2`
 - frecuencia respiratoria
 - cuestionarios de sintomas
 - nivel de actividad
- Intervenciones:
 - corticosteroides sistemicos
 - antibioticos si hay sospecha bacteriana
 - broncodilatadores nebulizados
 - titulacion dinamica de oxigenoterapia

## Neumonia adquirida en la comunidad

- Triaje:
 - requiere oxigenoterapia y antibioterapia parenteral
 - con estabilidad hemodinamica
 - excluye hipoxemia refractaria severa, sepsis con hipotension o soporte ventilatorio
- Diagnostico y monitoreo:
 - oximetria
 - temperatura
 - frecuencia cardiaca
 - rayos X portatiles con transmision radiologica segura
- Intervenciones:
 - fluidoterapia IV
 - antibioticos IV
 - desescalada rapida a via oral cuando exista respuesta y tolerancia

## ITU complicada y pielonefritis

- Triaje:
 - dolor incontrolable
 - hiperemesis o intolerancia oral
 - necesidad de antibioticos IV por resistencia microbiana
 - posible alta comorbilidad, sin shock septico
- Monitorizacion:
 - temperatura
 - presion arterial
 - frecuencia cardiaca
 - funcion renal
- Intervenciones:
 - antimicrobianos IV
 - fluidoterapia
 - laboratorios seriados domiciliarios
- Referencia de seguridad:
 - Mayo Clinic reporta resultados equivalentes a sala

## Celulitis e infecciones de piel y tejidos blandos

- Triaje:
 - fracaso de tratamiento ambulatorio
 - sintomatologia sistemica moderada
 - excluye fascitis necrotizante o necesidad inminente de desbridamiento
- Monitorizacion:
 - temperatura
 - evaluacion visual directa
 - fotografia clinica o videollamada
- Intervenciones:
 - antibioticos parenterales
 - en algunos protocolos, autoadministracion guiada
 - curaciones complejas in situ

## Expansion a cirugia y oncologia

### Readmisiones posoperatorias y vertical quirurgica

- Justificacion:
 - libera camas quirurgicas de alta demanda
 - aumenta `backfill margin`
- Vias clinicas elegibles:
 - infeccion de sitio quirurgico y espacios profundos
 - ileo paralitico
 - obstruccion intestinal
 - cuidado de sonda nasogastrica a succion
 - deshidratacion por nausea intratable o ileostomia de alto debito
 - cuidado de ostomias
 - recuperacion posquirurgica temprana:
 - bariatrica
 - colectomia laparoscopica
 - reversion de ileostomia
- Requisitos operativos:
 - exclusion absoluta si existe necesidad de reintervencion quirurgica
 - re-triaje y traslado rapido ante sepsis severa o cirugia de rescate
 - derivacion directa desde clinicas quirurgicas con apoyo de navegadores/enfermeras avanzadas

### Manejo agudo en oncologia

- Alcance emergente:
 - quimioterapia domiciliaria
 - soporte agudo post trasplante de celulas madre hematopoyeticas
 - modelos tipo `Home Sweet Home`
- Requisitos:
 - cuidado experto de lineas venosas centrales
 - prevencion de `CLABSI`
 - contencion y manejo de derrames citotoxicos
- Continuidad:
 - puente fluido hacia paliativos domiciliarios de alta intensidad

## Vivienda, determinantes sociales y conectividad

### Idoneidad estructural y geografica

- Servicios basicos obligatorios:
 - electricidad estable
 - agua corriente
 - climatizacion adecuada:
 - aire acondicionado
 - calefaccion
- Inspeccion del hogar:
 - cableado electrico
 - habitabilidad del dormitorio
 - acceso y seguridad del bano
 - riesgos arquitectonicos de caidas
- Riesgos ambientales a descartar:
 - moho
 - humedad
 - acumulacion de polvo
 - roedores
 - toxinas o alergenos severos
- Cobertura geografica:
 - radio delimitado por tiempo de conduccion
 - referencia frecuente: `30` minutos desde hospital base
- Conectividad:
 - banda ancha o red celular confiable
 - `hotspot` si se requiere
 - respaldo electrico local para equipos medicos

### Determinantes sociales de la salud

- Evaluar:
 - hacinamiento
 - seguridad del vecindario
 - seguridad alimentaria
 - acceso a dieta adecuada para restricciones clinicas
 - alfabetizacion en salud
 - idioma primario
 - competencia tecnologica
- Respuesta programatica:
 - articular recursos comunitarios
 - entrega de comidas
 - mitigacion de brecha digital
