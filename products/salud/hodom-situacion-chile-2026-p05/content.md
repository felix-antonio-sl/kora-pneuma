---
urn: urn:salud:kb:hodom-situacion-chile-2026-p05
nombre: hodom-situacion-chile-2026-p05
version: 1.0.1
estado: publicado
descripcion: "Situacion de la Hospitalizacion Domiciliaria en Chile 2024-2026 - Parte 05"
fuente: "Migrado de la bestia (~/kora @ 9de5dc38b78c23574d24a481a5f84d70173c2203) artifacts/knowledge/salud/salubrista/hodom/director/03-situacion-chile-2026--p05.md (sha256:9ea98b37851771e5b9caa0de33a912902d329a86f808eebcd0909869322f47f6) el 2026-07-17; cuerpo byte-fiel; frontmatter normalizado a ley/2; shard enlazado por cita a urn:salud:kb:hodom-situacion-chile-2026."
autor: FS
creado: 2026-03-10
lang: es
tags: [hodom, hospitalizacion-domiciliaria, chile, salud-publica, analisis-situacional]
familia: bok
cita: [urn:salud:kb:hodom-situacion-chile-2026]
---

# Situacion de la Hospitalizacion Domiciliaria en Chile 2024-2026 - Parte 05

## Anexo B. Consentimiento informado y protocolos de urgencia domiciliaria

### I. Modelo estructural de consentimiento informado

- La firma informada es requisito clinico y legal.
- La negativa a firmar excluye ingreso a HD.
- Dominios minimos:
 - identificacion del paciente:
 - nombre
 - `RUT`
 - fecha de nacimiento
 - domicilio exacto
 - prevision
 - identificacion del cuidador o tutor:
 - nombre
 - `RUT`
 - parentesco o relacion
 - declaracion de informacion clinica:
 - diagnostico principal
 - condicion actual
 - plan terapeutico
 - estada estimada
 - riesgos, beneficios y alternativas
 - compromisos del cuidador y paciente:
 - mantener habitabilidad, luz, agua y conectividad
 - presencia continua del cuidador
 - apoyo en medicamentos basicos
 - alerta precoz al equipo
 - autorizacion de ingreso del equipo clinico
 - certificacion de entrega normativa:
 - carta de derechos y deberes
 - mecanismo formal de reclamos
 - resumen clinico en domicilio con diagnosticos, evolucion breve, cuidados a seguir y telefonos de contacto para emergencia
 - firmas:
 - paciente
 - cuidador o tutor
 - profesional de ingreso
 - lugar, fecha y hora

### II. Protocolos de urgencia domiciliaria

#### 1. Emergencia clinica

- Sistema de alerta continua:
 - telefonico o radial
 - registro auditable de llamadas
 - fecha, hora, motivo, emisor y derivacion
- Triage y teleasistencia:
 - evaluacion de riesgo vital inminente
- Activacion de rescate medico:
 - traslado basico o avanzado a urgencias
 - hospitales comunitarios sin unidades criticas deben estabilizar transitoriamente con oxigenoterapia, soporte ventilatorio y farmacos de reanimacion hasta concretar traslado efectivo
- Manejo de caidas:
 - evaluacion de contusiones
 - riesgo de fractura
 - tecnicas seguras de levantamiento

#### 2. Adecuacion del esfuerzo terapeutico y ordenes de no reanimar

- Riesgo critico:
 - intervencion de urgencias externas en paliativos terminales
- Requisitos:
 - voluntades anticipadas o directrices medicas claras en ficha domiciliaria
 - evitar obstinacion terapeutica
 - coordinar informacion con `SAMU` o agencias de rescate
 - priorizar analgesia y confort sobre maniobras invasivas

#### 3. Agresiones al equipo de salud

- Riesgos:
 - violencia verbal
 - violencia fisica
 - presencia de armas
- Medidas:
 - evaluacion previa del entorno
 - mecanismos de escape y alerta
 - evacuacion inmediata si procede
 - georreferenciacion y monitoreo satelital de vehiculos

## Anexo C. Mapas de georreferenciacion y brechas territoriales

### 1. Fundamentacion metodologica y epidemiologica

- La georreferenciacion permite analizar:
 - distribucion geografica de oferta de camas
 - correlacion con demanda poblacional
 - accesibilidad al hospital base del cual depende HD
- El modelo espacial usa tres niveles de cobertura:
 - Cobertura `1`:
 - misma comuna del hospital base
 - Cobertura `2`:
 - comunas adyacentes
 - Cobertura `3`:
 - comunas no adyacentes o derivaciones distantes

### 2. Macro-gestion: brechas estructurales

- El mapa nacional confirma deficit historico:
 - `2.1` camas por `1.000` habitantes
- De `37.548` camas:
 - privado aporta `33%` (`12.565`)
- Desigualdad territorial:
 - `RM`: `50%` de dotacion en sector privado
 - resto del pais: promedio `21%`
 - Aysen: `0%` privado
- Lectura:
 - la carga asistencial recae en la red publica de macrozonas extremas
 - la HD debe asumir rol de soporte vital en atencion cerrada

### 3. Tipologia de cobertura territorial

Base metodologica: analisis cluster `K-Means` sobre `177` hospitales publicos.

| Clase | N | Cobertura observada | Lectura operativa |
| ----- | ----- | -------------------------------- | ---------------------------------------------------------------- |
| `1` | `32` | `57.6%` local, `23.7%` adyacente | Alta y mediana complejidad urbana; radio domiciliario provincial |
| `2` | `15` | `64.4%` local, `23.6%` adyacente | Alta complejidad regional con mayor capacidad de derivacion a HD |
| `3` | `112` | `81.9%` local | Hospitales Comunitarios; alta ruralidad; brecha de especialistas |
| `4` | `4` | Alta variabilidad | Centros de referencia con gestion de altas a comunas distantes |
| `5` | `14` | Muy alta variabilidad | Referencia nacional, alta carga adyacente y no adyacente |

- Clases `4` y `5`:
 - cobertura local minoritaria entre `41.2%` y `47.1%`
 - proporcion de pacientes adyacentes y no adyacentes hasta `16.5%`
- Lectura:
 - los Hospitales Comunitarios son frontera de atencion cerrada en zonas extremas
 - los centros de referencia requieren articulacion inter-redes y telecomunicaciones robustas

### 4. Micro-gestion y logistica clinica dinamica

- El piloto del Hospital Sotero del Rio muestra que mapas de isocronas y georreferenciacion en tiempo real son imperativos operativos.
- Variables integradas:
 - accesibilidad y trafico
 - condiciones climaticas
 - seguridad en ruta
 - distribucion espacial de pacientes
 - requerimiento de especialidad
 - score de complejidad
 - tipo de atencion
- Resultado:
 - reconfiguracion de rutas ante imprevistos
 - oportunidad asistencial
 - mayor integridad del personal clinico

### 5. Implicancias para planificacion y reduccion de brechas

1. Focalizar telemedicina sincronica y asincronica en los `112` hospitales de Clase `3`.
2. Priorizar `PAO` en macrozonas con baja densidad de camas y alta ruralidad.
3. Estandarizar georreferenciacion y coordinacion de traslados a nivel nacional con escalamiento del modelo `Raylex`/Sotero del Rio.

## Anexo D. Glosario de terminos tecnicos y acronimos

| Termino | Definicion compacta |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CAEC` | Cobertura adicional de `ISAPRES` para eventos de alto costo; por regla general excluye HD y solo admite excepciones calificadas con derivacion formal |
| `CMBD` | Conjunto Minimo Basico de Datos; base de clasificacion del episodio y financiamiento bajo `GRD`; exige codificacion completa `CIE-10` y `CIE-9MC` |
| `GES` | Regimen legal de garantias explicitas; en HD destaca `GES-4` para alivio del dolor y cuidados paliativos por cancer avanzado |
| `GRD` | Grupos Relacionados por el Diagnostico; mecanismo principal de pago por resolucion integral del episodio; en Chile usa familia `IR-GRD` |
| `HD` | Modalidad alternativa a atencion cerrada para pacientes agudos o cronicos reagudizados con cuidados hospitalarios en domicilio |
| `IAAS` | Infecciones Asociadas a la Atencion de Salud; control critico en HD; direccion tecnica y coordinacion deben acreditar curso de `80` horas |
| `Inliers` y `Outliers` | Clasificacion de duracion del episodio bajo `GRD`; `Outliers Superiores` generan carencias o deducibles perjudiciales |
| `IoT` y wearables | Dispositivos conectados que transmiten constantes vitales a ficha clinica electronica para telemonitorizacion continua |
| `MCC` | Modalidad de Cobertura Complementaria de `FONASA`; permite acceso a red privada definida mediante prima voluntaria e incluye arancel HD `0201408` |
| Score de Categorizacion de Complejidad | Herramienta objetiva para clasificar atenciones HD en basicas, intermedias y complejas segun visitas, oxigenoterapia y procedimientos invasivos |
