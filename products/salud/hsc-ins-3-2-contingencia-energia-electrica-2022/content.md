---
urn: urn:salud:kb:hsc-ins-3-2-contingencia-energia-electrica-2022
nombre: hsc-ins-3-2-contingencia-energia-electrica-2022
version: 1.0.0
estado: publicado
descripcion: "Plan HSC frente a cortes eléctricos internos o externos, con UPS, grupos electrógenos, verificación de cargas críticas y pruebas periódicas."
fuente: "Hospital de San Carlos Dr. Benicio Arzola Medina, Plan de contingencia frente a interrupción del Suministro de Energía Eléctrica y pruebas de funcionamiento, código INS 3.2, cuarta edición, julio de 2022, aprobado por Resolución Exenta N.° 3770 de 27-07-2022; Google Drive file id 1ontsh6RdTVwhvgPzU8x1WuOJOLqpEeZB; sha256:22cbae17380088de31c1c8594f53a127e94530a97d975b4b71a2c4ec0694e4d5; PDF digital de 13 páginas físicas y 589.063 bytes: una resolución no numerada más 12 páginas internas. Extracción nativa por página, OCR complementario Tesseract spa+eng y cotejo visual 13/13, incluidos resolución, flujograma y pauta semanal. Recorte institucional-operativo: se excluyen logos, paginación, geometría, repetición literal, recitados jurídicos no decisorios, explicación genérica sin efecto sobre una regla, nombres, firmas, contactos y campos vacíos; se conservan identidad, alcance, actos de aprobación, roles, definiciones operativas, decisiones, condiciones, excepciones, tiempos, capacidades, referencias y estructura abstracta de registros."
autor: Codex
creado: 2026-07-22
lang: es
tags: [hsc, energia-electrica, contingencia, ups, grupo-electrogeno, continuidad-operativa, infraestructura]
familia: fuente
cita: []
---

# Contingencia de energía eléctrica y pruebas — HSC INS 3.2

## Identidad, aprobación y vigencia

| Elemento | Hecho documental |
|---|---|
| Título literal | *Plan de contingencia frente a interrupción del Suministro de Energía Eléctrica y pruebas de funcionamiento* |
| Código impreso | INS 3.2 |
| Edición | Cuarta |
| Fecha | Julio de 2022 |
| Vigencia impresa | Julio de 2027 |
| Acto aprobatorio | Resolución Exenta N.º 3770, de 27 de julio de 2022 |
| Acto dejado sin efecto | Resolución Exenta N.º 3204, de 30 de julio de 2019 |
| Extensión | 13 páginas físicas: resolución más documento interno de 12 páginas |
| Alcance | Todas las actividades y procesos del establecimiento que dependan del suministro eléctrico |

La fuente estaba dentro de su vigencia impresa al 22 de julio de 2026. Esto no
demuestra que equipos, capacidades, ubicaciones o cargas sigan iguales ni que
las pruebas se hayan ejecutado. El estado KORA describe la madurez del
artefacto, no la vigencia ni la implementación de la fuente.

El plan de agua potable de 2026 también imprime **INS 3.2**, aunque es otro
documento. Título, fecha, acto aprobatorio, contenido y hash prueban que no son
ediciones sucesivas de una misma especie. Se mantienen identidades KORA
separadas para no sobrescribir conocimiento por una colisión del código local.

HODOM no aparece como actor ni carga. El artefacto permite estudiar cómo una
falla hospitalaria afecta continuidad, comunicaciones, farmacia, Urgencia y
capacidad de apoyo; no acredita respaldo eléctrico de dispositivos ubicados en
domicilios.

## Propósito y taxonomía de cortes

El objetivo es estandarizar la respuesta a fallas de distribución externa,
siniestros o fallas internas y sostener áreas críticas.

| Estado | Definición documental |
|---|---|
| Corte interno local | Una o varias unidades quedan sin energía y dependen de un tablero común. |
| Corte interno general | Uno o varios tableros quedan sin energía y dependen de un tablero común; la redacción conserva una relación jerárquica poco precisa. |
| Corte externo | El tablero principal queda sin energía e inician equipos de respaldo y paquetes de baterías. |
| Apagón total | Pérdida igual o superior al 70 % de la demanda abastecida por desmembramiento incontrolado del sistema, según la definición citada. |
| Carga crítica | Consumo esencial cuya pérdida o operación incorrecta amenaza seguridad de pacientes o personal o produce perjuicio económico relevante. |
| Grupo de respaldo | Equipo industrial capaz de generar autónomamente electricidad para la red crítica. |

La secuencia es:

`alarma de pérdida → detección de origen → corte local/general/externo → maniobra interna o entrada de respaldo → recorrido y verificación de cargas → reparación/restauración → informe y registro`.

## Gobierno y funciones

| Actor | Función preservada |
|---|---|
| Jefatura de Ingeniería y Mantención Industrial | Informar a Dirección conforme a gravedad y extensión; mantener comunicación con Mantención; apoyar reposición; emitir informe; velar por cumplimiento. |
| Personal de Mantención | Recibir aviso, determinar origen, recorrer instalaciones, maniobrar según procedimiento, verificar cargas y registrar. |
| Guardias | Informar cortes; fuera de horario, avisar al personal de llamada y a la jefatura de Ingeniería y Mantención. |
| Unidades clínicas y no clínicas | Durante corte externo, monitorizar operación, desconectar equipos innecesarios e informar sectores que carecen de energía pese a corresponderles respaldo. |
| Dirección | Recibir información e informe de contingencia; la fuente no detalla una comisión específica para electricidad. |

El índice anuncia “Responsabilidad de Evaluación”, pero el cuerpo no desarrolla
una sección separada con ese título. La responsabilidad explícita se concentra
en Ingeniería y Mantención y en los registros de prueba; no se inventa un actor
evaluador ausente.

## Respuesta a corte interno

El plan se activa con aviso del personal clínico, Mantención o guardias sobre
una interrupción en cualquier área. Mantención acude, identifica el origen y
recorre las instalaciones para normalizar el suministro. Antes de reenergizar,
verifica qué cargas están conectadas y adopta los cuidados pertinentes. El
documento no define tiempos máximos ni una secuencia técnica detallada de
maniobras, por lo que deben permanecer bajo competencia eléctrica autorizada.

## Respuesta a corte externo

Ante pérdida externa general se asegura suministro alternativo a servicios
críticos y Mantención recorre el establecimiento. UPS o baterías ingresan de
inmediato para sostener aproximadamente **15 segundos**, tiempo impreso para el
encendido y sincronización de grupos electrógenos, y para amortiguar fenómenos
de arranque en ciertas cargas.

### UPS declaradas en 2022

| Área | Ubicación y cargas impresas |
|---|---|
| UTI | 4.º piso, edificio B, sector 2: informática, 1 UPS de 10 kVA |
| UCI | 3.º piso, edificio B, sector 1: cinco columnas, 2 UPS de 20 kVA; informática, 1 UPS de 10 kVA |
| Pediatría | 3.º piso, edificio B, sector 2: informática, 1 UPS de 10 kVA |
| Cirugía Hombres | 2.º piso, edificio B, sector 1: informática, 1 UPS de 10 kVA |
| Cirugía Mujeres | 2.º piso, edificio B, sector 2: informática, 1 UPS de 10 kVA |
| Pabellón | 2.º piso, edificio A: cada OR, 1 UPS de 20 kVA para dos transformadores de aislación de 5 kVA; Recién Nacido/URA, 2 UPS de 20 kVA; informática, 1 UPS de 10 kVA |
| Ginecología y Obstetricia, sector 1 | 1.º piso, edificio B: informática, 1 UPS de 10 kVA |
| Ginecología y Obstetricia, sector 2 | 1.º piso, edificio B: salas de parto, 1 UPS de 20 kVA por OR para dos transformadores de 5 kVA; informática, 1 UPS de 10 kVA |
| Emergencia | 1.º piso, edificio A: columnas, 1 UPS de 6 kVA; informática, 1 UPS de 10 kVA |
| Archivo / DIG | 1.º piso, edificio D: informática, 1 UPS de 15 kVA |

La tabla es inventario documental, no certificación de presencia, autonomía,
batería o mantenimiento actual. La fuente usa la sigla OR sin definirla.

### Verificación de respaldo y dependencias

Mantención comprueba grupos electrógenos —frecuencia, tensión, combustible y
otros parámetros— y luego verifica:

- switch automático, tablero de transferencia y estabilizador de tensión;
- bombas de agua potable;
- manifolds de gases clínicos, aire medicinal, vacío, alarmas y tomas;
- caldera, calefacción y agua caliente sanitaria;
- comunicaciones e internet;
- red de incendios e iluminación de emergencia;
- operatividad de Pabellón, Laboratorio, Urgencia, Farmacia, Esterilización,
  Imagenología, servicios clínicos, Alimentación y oficinas administrativas.

Esta lista muestra dependencias en cascada: electricidad no es sólo una carga
clínica, sino condición de agua, gases, climatización, información, incendio y
producción asistencial.

## Flujo gráfico preservado

El flujograma parte de una alarma por pérdida de energía y detección de falla.
Distingue una falla interna local, una falla interna general y una externa;
conduce a maniobras o entrada de respaldo y finaliza en restauración. Su texto
es de baja legibilidad y algunas conexiones se cruzan. La koraficación conserva
la semántica confirmada por el cuerpo, no reproduce como reglas las ramas cuya
geometría no permite certeza.

## Informe de contingencia

La jefatura de Ingeniería y Mantención informa a Dirección:

- características y duración del corte;
- áreas afectadas;
- estado del sistema de emergencia;
- maniobras de reposición;
- deficiencias eléctricas detectadas;
- reserva de combustible y necesidad de reposición;
- estado de instalaciones industriales críticas;
- observaciones generales.

El informe distingue restauración de aprendizaje: recuperar energía no cierra
el evento si no quedan documentadas deficiencias, reserva y estado de los
soportes críticos.

## Mantenimiento y pruebas

| Sistema | Frecuencia | Criterios mínimos |
|---|---|---|
| Grupo electrógeno como sistema de respaldo | Semanal | Pauta del Anexo 1; prueba semanal sin carga para no generar cortes internos |
| Grupo electrógeno | Anual | Refrigerante y temperatura, aceite, batería, combustible, filtro, mangueras/conexiones, fugas, calefactor y mantenedor, funcionamiento, limpieza y estructura |
| Paquetes de baterías / UPS | Anual | Estructura, voltaje de entrada y salida, condición de carga, pruebas y limpieza |
| Iluminación de emergencia | Anual | Estructura, voltaje de entrada, funcionamiento y limpieza |

La pauta semanal añade:

- horómetro y tablero;
- niveles de refrigerante, aceite, batería y combustible;
- filtro, mangueras, conexiones, fugas, calefactor, estanques de reserva y
  alarmas;
- prueba semanal en vacío, máximo 10 minutos;
- prueba con carga mediante selector TTA, al menos 30 minutos una vez al mes;
- observaciones y validación funcional.

El formulario imprime dos veces “prueba en vacío” y vuelve a resumir frecuencia
semanal/mensual. Se registra como duplicación de diseño, no como exigencia de
dos pruebas en vacío distintas. La prueba mensual con carga complementa —no
contradice— la prueba semanal sin carga del cuerpo.

Los trabajos se archivan con la hoja de vida de cada equipo o sistema y se
planifican en una carta Gantt mensual. Los formatos estaban vacíos: no se
conservan nombre, firma, timbre ni lecturas pobladas.

## Referencias y control de cambios

El plan cita los pliegos técnicos RIC de la SEC y la *Norma Técnica de Seguridad
y Calidad de Servicio* de 2005. Esta koraficación no verifica externamente qué
ediciones rigen en 2026 ni sustituye la evaluación de un profesional eléctrico.

El historial registra segunda edición en julio de 2016 —modificó frecuencias de
grupos electrógenos e iluminación—, tercera en julio de 2019 y cuarta en julio
de 2022 por término de vigencia. La resolución de 2022 deja sin efecto la de
2019.

## Cautelas de uso

- El intervalo aproximado de 15 segundos no es autonomía garantizada: depende
  de UPS, baterías, transferencia y generadores operativos.
- La lista de cargas y ubicaciones es un corte de 2022; requiere inventario y
  pruebas actuales antes de una decisión operacional.
- La definición de corte interno general repite la dependencia de un “tablero
  común” con sintaxis ambigua; no se reconstruye una topología eléctrica.
- La vigencia impresa se extiende hasta julio de 2027. Si llegara a expirar sin
  sucesor disponible, la política operativa indicada por el usuario exige
  conservarla como referencia provisional hasta actualización, mostrando
  claramente la fecha; al corte de esta koraficación todavía no está vencida.
- El código INS 3.2 colisiona con agua potable y nunca debe usarse solo para
  resolver identidad.

## Valor para el modelamiento HODOM

El documento permite modelar objetos y estados críticos del hospital: red
normal, pérdida local/general/externa, UPS activa, generador sincronizado,
combustible disponible, carga respaldada/no respaldada, servicio operativo y
restauración. Para HODOM aporta efectos de interfaz sobre Urgencia, Farmacia,
Esterilización, comunicaciones, internet, gases, agua y capacidad de hospital.
No acredita que dispositivos domiciliarios estén conectados a la red crítica ni
define un plan de respaldo energético para pacientes en casa; esa rama requiere
fuente y diseño propios.
