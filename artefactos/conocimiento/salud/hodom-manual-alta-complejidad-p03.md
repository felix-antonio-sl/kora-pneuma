---
urn: urn:salud:kb:hodom-manual-alta-complejidad-p03
nombre: hodom-manual-alta-complejidad-p03
version: 1.1.1
estado: publicado
descripcion: "Manual de Hospitalizacion Domiciliaria de Alta Complejidad - Parte 03"
fuente: "Migrado de la bestia (~/kora @ 9de5dc38b78c23574d24a481a5f84d70173c2203) artifacts/knowledge/salud/salubrista/hodom/director/02-manual-alta-complejidad--p03.md (sha256:d01c8525b1b8c3b43c593a57a14d39fe1491fc2f462aeb01968356b73c4a15ae) el 2026-07-17; cuerpo byte-fiel; frontmatter normalizado a ley/2; shard enlazado por cita a urn:salud:kb:hodom-manual-alta-complejidad."
autor: FS
creado: 2026-03-10
lang: es
tags: [hodom, hospitalizacion-domiciliaria, alta-complejidad, hospital-at-home, gestion-clinica]
familia: bok
cita: [urn:salud:kb:hodom-manual-alta-complejidad]
---

# Manual de Hospitalizacion Domiciliaria de Alta Complejidad - Parte 03

## Interoperabilidad, `EHR` y facturacion `CPT`

### Arquitectura y gobernanza

- Estandares:
 - `FHIR`
 - `HL7`
 - `RESTful APIs`
- Reglas de datos `PGHD`:
 - definir si ingresan automaticamente al `EHR`
 - o si requieren validacion previa
- Requisito de interfaz:
 - distinguir metricas tomadas en domicilio vs mediciones presenciales
- Documentacion automatizada:
 - `time-stamp`
 - `audit logs`
 - control de acceso por roles
 - cumplimiento `HIPAA`

### Codigos `CPT`

| Codigo | Hecho operativo preservado |
| ------- | ------------------------------------------------------------------------------------------------- |
| `99453` | Configuracion inicial del dispositivo y educacion estructurada al paciente |
| `99454` | Provision del dispositivo y transmision diaria; requiere al menos `16` dias de datos en `30` dias |
| `99457` | Primeros `20` minutos mensuales de comunicacion interactiva y gestion clinica |
| `99458` | Cada bloque adicional de `20` minutos |
| `99091` | Recoleccion, analisis e interpretacion de datos fisiologicos continuos |

- Capacidad minima del sistema:
 - reportes de fin de mes
 - dias monitorizados
 - tendencias
 - minutos documentados
 - justificacion clinica continua

## Calidad, seguridad y outcomes

### Mortalidad y morbilidad iatrogenica

- Metaanalisis:
 - `61` ensayos controlados aleatorizados
 - `OR 0.81`
 - `IC 95% 0.69-0.95`
 - `P = 0.008`
 - `NNT = 50`
- `CMS` / `AHCAH`:
 - mortalidad inferior en los `25` `MS-DRG` mas frecuentes
 - diferencia estadisticamente significativa en `11` de esos `25`
- Cohortes especificas:
 - `0.93%` en HaH vs `3.4%` hospitalario
- Infecciones asociadas a la atencion:
 - tasas inferiores frente a hospital fisico
 - menor exposicion a patogenos nosocomiales y multirresistentes
- Delirium:
 - `24%` en hospital tradicional
 - `9%` en HaH

### Readmisiones, urgencias y `SNF`

| Indicador | Hospital tradicional | HaH | Nota |
| ---------------------------------------- | -------------------- | ------- | ----------------------------------- |
| Readmision a `30` dias | `23%` | `7%` | Ensayo pivotal de Brigham |
| Readmision a `30` dias | `15.60%` | `8.60%` | `MACT` Mount Sinai |
| Visitas a urgencias | `13%` | `7%` | Menor uso posalta |
| Visitas a urgencias | `11.70%` | `5.80%` | Resultado institucional concordante |
| Derivacion a `SNF` | `10.40%` | `1.70%` | Menor institucionalizacion |
| Riesgo relativo de ingreso a largo plazo | `1` | `0.16` | Menor dependencia institucional |

- Metaanalisis:
 - riesgo relativo de readmision a `30` dias: `0.74`
- Matiz `CMS`:
 - cohorte analizada: mas de `11,000` pacientes bajo `AHCAH`
 - resultados de readmision varian por `MS-DRG`
 - hubo `2` `MS-DRG` con readmision significativamente mas alta en HaH
 - y `3` `MS-DRG` con tasas muy altas en hospital fisico
- Implicacion:
 - el beneficio depende de seleccion rigurosa por patologia

### Estado funcional y movilidad

- `HAD`:
 - prevalencia cercana a `30%` en adultos mayores hospitalizados
- Acelerometria:
 - sedentarismo `78.0%` vs `86.0%`
 - tiempo en cama `18%` vs `55%`
 - pasos diarios `834` vs `120`
 - actividad ligera `21.25%` vs `13.92%`
- Cohortes asiaticas:
 - `79.7%` reporta menos tiempo en cama
 - `73.2%` aumenta deambulacion
- Efecto clinico:
 - preservacion de `AVD` y `AIVD`
 - menor necesidad de `SNF`
 - menor cascada de dependencia institucional

### Seguridad del paciente y escalamiento clinico

#### Medicacion

- Riesgos criticos:
 - errores de medicacion
 - polifarmacia
 - preparacion compleja en domicilio
- Mitigaciones:
 - prescripcion integrada con `EHR`
 - lotes de `24` horas
 - minima preparacion a la cabecera
 - escaneo de codigos de barras en punto de atencion
 - evaluacion formal de capacidad de autoadministracion
 - pastilleros bicolores cuando aplique
 - enfermeria virtual para supervisar tomas

#### Transporte y almacenamiento de farmacos

- Requisitos:
 - monitoreo termico activo
 - contenedores de cadena de frio
 - condiciones de almacenamiento domiciliario validadas
 - kits de rescate en vivienda para farmacos urgentes

#### Sustancias controladas

- Reglas:
 - cadena de custodia ininterrumpida
 - empaque `tamper-evident`
 - baja visibilidad en transporte
 - `lock boxes` en domicilio

#### Tasas de escalamiento

- Definicion:
 - retorno no planificado al hospital por deterioro, fracaso terapeutico o complicacion no manejable en casa
- Datos:
 - `AHCAH`: `7.2%` en cohorte de mas de `11,000` pacientes
 - cohorte de pielonefritis aguda: `4.8%`
- Lectura operacional:
 - tasas inferiores a `10%` confirman soporte remoto efectivo
 - una tasa demasiado cercana a `0%` puede indicar triaje excesivamente conservador
- Respaldo reglamentario:
 - capacidad de desplegar respuesta presencial en hasta `30` minutos
 - articulacion con `911` y paramedicos comunitarios

## Economia de la salud, capacidad y reembolso

### Costos directos e indirectos

| Hallazgo | Magnitud |
| ------------------- | ----------------------------------------------------------------------------- |
| Johns Hopkins | `32%` menos costo total (`$5,081` vs `$7,480`) |
| Presbyterian | `19%` menos costo medio |
| Brigham and Women's | `38%` menos costo ajustado por episodio |
| Singapur | `42%` menos costo por dia-cama; `24%` menos por episodio; ahorro de `\$1,665` |

- Impulsores del ahorro:
 - menor `overhead`
 - menos laboratorios: mediana `3` vs `15`
 - menor uso de imagenes: `14%` vs `44%`
 - menos interconsultas: `2%` vs `31%`
 - menor estancia media en datos fundacionales: `3.2` vs `4.9` dias
 - menor utilizacion posaguda costosa
- Extension del beneficio:
 - a `30` dias, la brecha total puede ampliarse hasta `25%`

### Capacidad instalada y `backfill margin`

- Premisa:
 - HaH funciona como valvula de escape para sistemas saturados
- Dato contextual:
 - hospitales con programas HaH muestran ocupacion media `20` puntos porcentuales mayor que hospitales tradicionales
- Mecanismo:
 - trasladar casos medicos de baja o moderada agudeza al hogar
 - liberar cama fisica
 - rellenar con casos mas rentables:
 - quirurgicos
 - alta complejidad
- Tension financiera:
 - dificil reemplazar una admision de `$10,000` o `$12,000` si no existe certeza de `backfill`

#### Casos cuantificados

- Readmisiones quirurgicas elegibles:
 - `30.1%` a `60` dias
- Dias-cama liberados:
 - `4,152`
- Margen potencial por nueva capacidad:
 - `\$8.8` millones
- Expansion virtual:
 - `250` camas
 - ahorro de capital cercano a `\$500` millones
 - supuesto: `\$2` millones por cama fisica nueva
- Programas maduros:
 - Advocate Health: `33,000` dias-cama liberados tras mas de `9,400` pacientes desde `2020`
 - Contessa: mas de `32,000` dias-cama liberados desde `2016`
 - Atrium Health: proyeccion de liberar `10%` de sus camas al tratar `100` pacientes diarios para `2025`

### Marco regulatorio y reembolso en Estados Unidos

- Programa:
 - `Acute Hospital Care at Home` (`AHCAH`) de `CMS`
- Marco legislativo referido en la fuente:
 - Ley de Asignaciones Consolidadas de `2026`
 - paridad de pago `DRG`
 - extension de exenciones hasta `30 de septiembre de 2030`
- Exigencia operativa:
 - documentacion robusta
 - codificacion correcta
 - capacidad de auditoria

### Atencion basada en valor

- Sinergias:
 - `ACO`
 - pagos capitados
 - `Medicare Advantage`
 - pagadores privados alineados con valor
- Logica economica:
 - evita urgencias y hospitalizaciones fisicas costosas
 - reduce uso posagudo y `SNF`
 - alinea incentivos clinicos y financieros

## Experiencia del paciente, cuidador y equidad

### Satisfaccion del paciente

| Indicador | Hospital tradicional | HaH |
| ------------------------------------------ | -------------------- | ------- |
| `Picker` | `11.0` | `13.4` |
| `NPS` | `45.5` | `88.4` |
| Disposicion a reutilizar servicio | n/a | `97.5%` |
| Pacientes "extremadamente" o "muy" comodos | `60.9%` | `84.4%` |

- Calidad del sueno:
 - `74.8%` reporta sueno superior en domicilio
- Beneficios percibidos:
 - privacidad
 - flexibilidad de rutina
 - mayor dignidad
 - cercania con familia y mascotas
 - menor ansiedad y depresion asociadas al ingreso

### Carga del cuidador

- Riesgos:
 - ansiedad
 - alteracion del sueno
 - carga de vigilancia
 - descuido del autocuidado
 - ocultamiento del estres por temor a institucionalizacion
- Aceptabilidad poblacional:
 - `47.2%` considera aceptable el modelo
 - `16.6%` lo considera inaceptable por preocupacion de sobrecarga familiar
- Delimitacion obligatoria:
 - `ADL` y soporte emocional = rol del cuidador
 - vias IV, medicacion compleja, interpretacion de datos y decisiones = rol exclusivo del equipo clinico
- Soportes requeridos:
 - entrenamiento en dispositivos
 - planes de contingencia y primeros auxilios
 - centro de comando `24/7`
 - videoconferencia o contacto de un solo toque
 - `Zarit Burden Interview` para monitoreo de sobrecarga

### Consideraciones culturales

- Integrar valores que priorizan el cuidado familiar
- Mitigar resistencia a la impersonalidad tecnologica
- Hallazgos referidos en comunidades asiaticas y latinas
- Presentar apoyos y tecnologia como complemento del cuidado familiar, no como reemplazo

### Equidad, diversidad y acceso en areas rurales

#### Contexto estructural

- `14%` de la poblacion de EE. UU. vive en areas rurales
- `23%` reporta el acceso a salud como problema mayor
- tiempo medio hacia hospital fisico: `34` minutos
- mas de `150` hospitales rurales cerrados desde `2010`

#### Resultados de equidad

- No se observan diferencias estadisticamente significativas en:
 - mortalidad
 - escalamiento
 - readmision
 - entre grupos etnicos o raciales historicamente marginados
- Pacientes con discapacidad o elegibilidad dual:
 - resultados comparables a hospital fisico
- Beneficio adicional:
 - el hogar permite detectar `SDOH` ocultos durante una hospitalizacion convencional

#### Ruralidad y hospitales de acceso critico

- Aceptabilidad:
 - rechazo urbano previo hasta `63%`
 - rechazo rural `31%`
 - satisfaccion superior al `90%` en sistemas como Marshfield Clinic
- Resultados:
 - paridad clinica y de costos frente a hospital fisico
 - pacientes rurales menos sedentarios y mas activos
- Adaptaciones necesarias:
 - medicina predominantemente remota tras evaluacion inicial
 - apoyo presencial de enfermeria o `MIH`
 - traslado intermitente al hospital para imagenes avanzadas o accesos complejos cuando sea necesario
