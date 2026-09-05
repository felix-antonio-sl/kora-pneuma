---
urn: urn:salud:kb:hodom-manual-alta-complejidad-p02
nombre: hodom-manual-alta-complejidad-p02
version: 1.1.1
estado: publicado
descripcion: "Manual de Hospitalizacion Domiciliaria de Alta Complejidad - Parte 02"
fuente: "Migrado de la bestia (~/kora @ 9de5dc38b78c23574d24a481a5f84d70173c2203) artifacts/knowledge/salud/salubrista/hodom/director/02-manual-alta-complejidad--p02.md (sha256:4fb329742c917861d9b37b1fcb5cfad0ca16d6455383bc659a6524ed2f845733) el 2026-07-17; cuerpo byte-fiel; frontmatter normalizado a ley/2; shard enlazado por cita a urn:salud:kb:hodom-manual-alta-complejidad."
autor: FS
creado: 2026-03-10
lang: es
tags: [hodom, hospitalizacion-domiciliaria, alta-complejidad, hospital-at-home, gestion-clinica]
familia: bok
cita: [urn:salud:kb:hodom-manual-alta-complejidad]
---

# Manual de Hospitalizacion Domiciliaria de Alta Complejidad - Parte 02

## Red de apoyo social y rol del cuidador informal

- Inclusion prioriza:
 - familiares, conyuge o amigos con presencia constante
 - capacidad para apoyar actividades basicas e instrumentales
- Evaluacion de idoneidad:
 - capacidad fisica
 - capacidad cognitiva
 - disposicion emocional
- Tareas esperadas del cuidador:
 - administracion guiada de medicacion pautada
 - reporte de sintomas
 - supervision de equipos simples
- Limite critico:
 - no transferir enfermeria especializada ni procedimientos invasivos
- Vigilancia del programa:
 - monitorizar estres, ansiedad y fatiga del cuidador
 - educacion continua para sostener la red de apoyo

## Centro de comando virtual

- Rol:
 - nucleo clinico-operativo del programa
 - equivalente funcional de estacion de enfermeria centralizada
- Cobertura:
 - `24/7`
 - medicos y enfermeria de forma continua
- Arquitectura:
 - plataforma en nube segura
 - interoperabilidad bidireccional con `EHR`
 - `dashboard` unico para tendencias fisiologicas, alertas `IA`, priorizacion de riesgo y documentacion
- Tecnologia desplegada en domicilio:
 - tableta para videoconferencias
 - telefono de marcacion directa al centro
 - extensores Wi-Fi o conectividad celular `4G/LTE`
 - pulsera o collar de alerta de emergencia
- Funciones:
 - recepcion de datos `RPM`
 - vigilancia de adherencia al envio de datos
 - contacto proactivo si faltan transmisiones
 - coordinacion interdisciplinaria
 - programacion de visitas presenciales

## Equipo multidisciplinario y frecuencia minima

### Medicos hospitalistas y `APPs`

- Responsables de:
 - admision
 - plan de cuidados
 - triaje de agudeza
- Cobertura:
 - disponibilidad `24/7`
- Modelo maduro:
 - visita medica diaria virtual
 - puede ser sincrona con enfermeria presente al lado del paciente

### Enfermeria de atencion directa

- Ejecuta:
 - medicamentos IV
 - oxigenoterapia
 - curaciones complejas
 - flebotomia
 - pruebas en punto de atencion
 - `ECG`
- Carga tipica descrita:
 - cerca de `3` horas totales al dia
 - distribuidas en multiples visitas

### Paramedicos comunitarios / `MIH`

- Funcion:
 - extension de medicina y enfermeria
 - evaluacion presencial
 - tratamientos protocolizados
 - respuesta inmediata ante deterioro
- Regla `AHCAH`:
 - pueden contar para visitas presenciales diarias
 - solo bajo supervision clinica de enfermera registrada o medico
- Barrera regulatoria:
 - ajuste de normativas locales que restringen practica al sistema `911`

### Farmaceuticos clinicos

- Funciones:
 - conciliacion de medicamentos
 - prevencion de interacciones
 - supervision de dispensacion
 - educacion virtual al paciente y red de apoyo

### Trabajo social y gestion de casos

- Funciones:
 - evaluar seguridad del domicilio
 - confirmar soporte social
 - coordinar equipos medicos duraderos
 - conectar con servicios comunitarios
- Transicion:
 - seguimiento posalta de `30` dias en la referencia citada

### Protocolo minimo de contacto

- `1` evaluacion diaria por medico, `NP` o `PA`
- minimo `2` visitas presenciales diarias por enfermeria o personal clinico habilitado
- capacidad de respuesta presencial ante crisis en hasta `30` minutos
- frecuencia titulable segun via clinica y agudeza

## Cadena de suministro y ultima milla

- Dominio logistico:
 - medicamentos
 - terapias de infusion
 - `DME`
 - oxigeno
 - conectividad
 - alimentacion
- Riesgo estructural:
 - cadena no lineal, descentralizada y dependiente de multiples proveedores
- Exigencias:
 - despliegue en horas
 - trazabilidad completa
 - coordinacion de proveedores centralizada

### Logistica farmaceutica

- Riesgos:
 - inestabilidad termica
 - errores de preparacion
 - quiebres de continuidad
- Mitigaciones:
 - indicadores termicos y registradores continuos
 - lotes preparados para ciclos de `24` horas
 - minima manipulacion a la cabecera
 - kits redundantes con medicacion urgente
- Sustancias controladas:
 - cadena de custodia documentada
 - embalaje `tamper-evident`
 - baja visibilidad del contenido

### `DME`, soporte respiratorio y nutricion

- Entrega inmediata de:
 - camas articuladas
 - sillas de ducha
 - concentradores y sistemas de oxigeno
 - nebulizacion
 - tabletas y dispositivos `RPM`
- Requisito:
 - todo instalado, calibrado y operativo al arribo del paciente
- Soporte nutricional:
 - articulacion con recursos comunitarios
 - convenios directos de distribucion
 - referencia operativa: `Meals on Wheels`

### Logistica inversa

- Recoleccion y eliminacion segura de:
 - residuos biologicos
 - insumos de vias intravenosas
 - material de curaciones
- Cumplimiento:
 - normativas de bioseguridad y salud publica

## FMEA, subcontratistas y control de calidad

- Riesgos de tercerizacion:
 - brechas de competencia
 - variabilidad del cuidado
 - capacidad insuficiente `24/7`
 - deficit de gobernanza
 - retraso de un solo proveedor compromete el plan total
- Metodo `FMEA`:
 1. mapear procesos y subprocesos criticos
 2. identificar modos de fallo y calcular `RPN`
 3. intervenir primero sobre eventos de mayor impacto clinico
- Ejemplos de fallos de alto riesgo:
 - retraso de antibioticos IV
 - falla de soporte respiratorio
 - errores de calibracion `RPM`
- Politicas contractuales obligatorias:
 - redundancia sistemica
 - auditoria de competencias y licencias
 - rutas de escalamiento integradas al centro de comando
 - `SLA`, `KPI` logisticos y clinicos
 - mejora continua posterior a la firma del contrato

## Monitorizacion remota de pacientes

- Pilar tecnologico del modelo:
 - sustituye rondas y telemetria hospitalaria con datos fisiologicos en tiempo real
- Exigencia regulatoria:
 - dispositivos autorizados, p. ej. `FDA 510(k)`
 - clase II en la referencia citada
 - diferenciacion explicita frente a `wellness apps`
- Kit biometrico posible:
 - presion arterial
 - frecuencia cardiaca
 - `ECG`
 - oximetria `SpO2`
 - peso
 - glucosa capilar o `CGM`
 - termometria
- Riesgos de uso:
 - mala colocacion del oximetro
 - lecturas espurias
 - necesidad de educacion estructurada y calibracion
- Conectividad recomendada:
 - `4G/LTE/5G`
 - `hub` o tableta central
 - extensores de senal
 - respaldo electrico
- Seguridad:
 - cifrado en transito y reposo
 - autenticacion robusta
 - actualizacion segura de firmware
 - trazabilidad por auditoria

## IA, analitica predictiva y fatiga de alertas

- Problema:
 - sobrecarga de datos y desgaste profesional
 - solo `6.6%` de transmisiones o alertas requiere accion clinica real en cohortes monitorizadas citadas por la fuente
- Rol de la `IA`:
 - convertir datos brutos en `actionable insights`
 - detectar descompensacion preclinica
 - automatizar decisiones rutinarias
 - integrar marcadores conductuales:
 - patrones de sueno
 - uso de smartphone
- Jerarquia de escalamiento:
 - Nivel `1`: filtro algoritmico y recordatorios automatizados
 - Nivel `2`: evaluacion contextual e intervencion protocolizada por enfermeria
 - Nivel `3`: escalamiento medico ante incertidumbre o deterioro refractario
- Regla operacional:
 - umbrales individualizados por fisiologia y trayectoria del paciente
 - ejemplo: `SpO2` basal mas baja en `EPOC` severo

## Diagnostico movil en el domicilio

### Rayos X portatiles

- Equipos digitales compactos:
 - rango referido de `5 kg` a `45 kg`
 - generadores de alta frecuencia
 - baterias de ion-litio
- Requisitos:
 - dosis radiologica baja
 - protocolos de `shielding`
- Usos:
 - neumonia
 - redistribucion de flujo en insuficiencia cardiaca
 - fracturas tras caidas
 - verificacion de vias y sondas
- Flujo:
 - posicionamiento de `DR panel`
 - adquisicion instantanea
 - sin revelado quimico

### `POCUS`

- Equipos:
 - transductores de mano
 - consolas ligeras o dispositivos inteligentes de grado medico
- Usos:
 - ecocardiograma dirigido
 - descarte de `TVP`
 - derrame pleural
 - ascitis
 - tejidos blandos en celulitis y abscesos
 - guiado de accesos venosos perifericos o lineas medias

### `ECG` y telemetria de alta resolucion

- `ECG` de `12` derivaciones:
 - calidad hospitalaria
 - arritmias
 - isquemia aguda
 - seguimiento de `QTc`
- Monitores Holter y parches biometricos:
 - vigilancia continua de `24` horas a varios dias
 - menor carga funcional para el paciente

### Transmision e interoperabilidad diagnostica

- Requisito:
 - encriptacion in situ
 - transmision inmediata por red celular propia del equipo
- Lectura remota:
 - radiologia y cardiologia prioritaria
 - plataformas tipo `MediMatrix` o `PACS` hospitalario
 - informes en `EHR` el mismo dia o en horas
