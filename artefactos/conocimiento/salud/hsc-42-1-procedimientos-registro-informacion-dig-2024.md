---
urn: urn:salud:kb:hsc-42-1-procedimientos-registro-informacion-dig-2024
nombre: hsc-42-1-procedimientos-registro-informacion-dig-2024
version: 1.0.0
estado: publicado
descripcion: "Fuente institucional HSC para registro, validación y reporte de información DIG: GRD, censo de camas, urgencia, REM, IEEH, COMGES y SIGCOM."
fuente: "Hospital de San Carlos Dr. Benicio Arzola Medina, Manual de Procedimientos de Registro de Información Departamento de Información para la Gestión, código HSC 42.1, primera edición, septiembre de 2024; Memorándum 1EH2 N.° 80 de 22-10-2024 comunica aprobación, difusión y vigencia desde septiembre de 2024; revisión y vigencia impresas a septiembre de 2029, salvo página final que dice septiembre de 2028; Google Drive file id 1o6HTa0HwW7N48KCyo6iKFPbX3BFOHf5X; sha256:1373a98a42cc3c4b7108de6c83de446e59bd6fa11c085cb6e3305f1dd46a7682; PDF escaneado de 59 páginas físicas y 13.659.443 bytes: memorándum más manual de 58 páginas. OCR integral en español: 100.323 caracteres, 16.067 palabras y confianza media 86,77%; cotejo visual 59/59. Fracción sustantiva declarada 100%: conserva identidad, autoridad, alcance, actores, definiciones, fuentes, procesos, reglas, plazos, validaciones, flujos, interfaces, defectos y límites; omite 0 unidades sustantivas y añade 0 obligaciones. Excluye nombres, firmas, timbres, contactos, credenciales, endpoints, identificadores de usuarios, capturas pobladas y valores de ejemplo."
autor: Codex
creado: 2026-07-22
lang: es
tags: [hsc, hsc-42-1, dig, registro-informacion, grd, censo-camas, rem, ieeh, sigcom, fuente]
familia: fuente
cita: []
---

# Procedimientos de registro de información DIG — HSC 42.1 (2024)

## Identidad y alcance real

| Elemento | Hecho documental |
|---|---|
| Título impreso | *Manual de Procedimientos de Registro de Información Departamento de Información para la Gestión* |
| Código / edición | HSC 42.1 / primera |
| Elaboración | Septiembre de 2024 |
| Comunicación institucional | Memorándum 1EH2 N.º 80, 22 de octubre de 2024 |
| Vigencia comunicada | Desde septiembre de 2024 |
| Revisión/vigencia de portada | Septiembre de 2029 |
| Extensión | Memorándum más manual interno de 58 páginas |

Aunque el inventario externo lo rotula como “gestión documental/archivo
clínico”, la identidad impresa prevalece: es un manual de **registro de
información DIG**. Contiene interfaces con ficha clínica y Archivo, pero no es
una norma integral de archivo clínico, conservación, expurgo, acceso ni custodia.

Objetivo: definir, estandarizar y uniformar procesos del Departamento de
Información para la Gestión y sus relaciones internas/externas como herramienta
de control de procesos y resultados. Aplica al personal profesional, técnico y
administrativo del DIG y a prestadores de atención abierta y cerrada que originan
registros estadísticos.

Responsables declarados: jefatura DIG, jefaturas de sus secciones,
profesionales/administrativos DIG y profesionales que registran prestaciones.
La fuente prescribe trabajo; por sí sola no demuestra cumplimiento sostenido,
calidad alcanzada ni práctica observada.

El estado KORA describe la madurez del artefacto, no la vigencia ni la
implementación de la fuente.

## Gobierno y arquitectura funcional

El manual sitúa al DIG bajo la Subdirección de Planificación y Control y lo
organiza en tres secciones:

```text
Subdirección de Planificación y Control
  └─ Jefatura DIG
      ├─ Sección GRD
      │   ├─ asesoría médica
      │   ├─ codificación
      │   └─ digitación
      ├─ Sección SIGCOM
      │   └─ análisis SIGCOM
      └─ Sección Estadística
          ├─ atención cerrada, censo y egresos
          ├─ prestaciones ambulatorias y urgencia
          └─ administración de censo hospitalario
```

La introducción declara que DIG recibe, ingresa y digita registros de atención
abierta, cerrada, Urgencia y servicios de apoyo. En 2024 describe una captura
mixta: bases propias, extracción desde aplicaciones y digitación de formularios
en papel, debido a que no existiría un sistema uniforme para todas las áreas.
Esta es una afirmación del documento, no un diagnóstico técnico independiente.

## Autoridad documental citada

El corpus de referencia impreso incluye:

- Ley 18.469; D.S. N.º 38 de 2005;
- resoluciones FONASA N.º 50/2009 para MAI y N.º 277/2011 para MLE;
- Ordinario A15 N.º 2366/2012 sobre créditos incobrables;
- Manual Series REM 2024 y normas DEIS;
- Ordinario C202 N.º 2941/2023 sobre estadísticas hospitalarias;
- Ordinarios B52 N.º 817/2024 sobre producción intrahospitalaria y N.º 721/2024
  sobre registro diario de Urgencia;
- Manual de Censo Diario de Camas y Pacientes/REM 20;
- Norma Técnica N.º 235 y Exento N.º 58/2023 sobre IEEH;
- Ordinario C21 N.º 951/2024 sobre habilitación y ocupación de camas;
- resolución local 4H2 N.º 199/2024 sobre dotación de camas;
- instructivos SIGCOM 2023 y GRD, instrumento EAR/BSC 2024, orientaciones
  COMGES/RISS 2024 y CIE-10;
- resolución local N.º 855/2024 sobre organigrama.

El listado repite tanto el Ordinario C202 N.º 2941 como el Ordinario A15
N.º 2366. Su inclusión no valida aquí la vigencia o jerarquía actual de cada
referencia.

## Conceptos y fronteras de datos

- **Atención abierta/cerrada:** prestaciones ambulatorias versus actividades a
  personas hospitalizadas.
- **Paciente hospitalizado:** persona que ocupa una cama hospitalaria de dotación.
- **Dotación de camas:** camas asignadas por autoridad competente, instaladas y
  disponibles 24 horas en operación normal.
- **Camas disponibles/en trabajo:** camas habilitadas para uso inmediato,
  ocupadas o no.
- **IEEH:** Informe Estadístico de Egreso Hospitalario.
- **HHCC:** ficha/historia clínica; insumo del registro y la codificación.
- **CMBD:** conjunto mínimo básico de datos.
- **GRD/IR-GRD:** agrupación de episodios clínicamente similares y comparables en
  consumo de recursos; TEAM CODER y ALCOR son las plataformas declaradas.
- **REM:** registro/resumen estadístico mensual; REM 20 concentra hospitalización.
- **DAU:** dato/registro de atención de Urgencia.
- **SIGCOM:** sistema MINSAL de gestión de costos.

Indicadores definidos: egresos, unidades de producción hospitalaria, peso medio
GRD, dotación y disponibilidad, índice ocupacional, estancias bruta/depurada y
outliers, índice funcional, IEMA, reingresos urgentes a siete días y mortalidad
hospitalaria/riesgo menor. Estas definiciones no sustituyen las fichas técnicas
vigentes ni prueban que todos los indicadores se calculen hoy del mismo modo.

## 1. Registro clínico-financiero mediante IR-GRD

### Finalidad y recursos declarados

El subproceso organiza egresos por similitud clínica y consumo de recursos para
comparación, pago por evento, análisis de casuística, eficiencia y gestión. El
código IR-GRD se presenta con seis dígitos que combinan categoría diagnóstica
mayor, tipo/número de GRD y severidad. La asignación considera recién nacido,
maternidad, procedimiento significativo o GRD médico; si existen varios
procedimientos se elige el de mayor consumo más relacionado con el diagnóstico
principal.

Dotación declarada para el subproceso: una jefatura profesional, tres
codificadores de enfermería, un administrativo y dos médicos asesores/codificadores
con jornadas parciales. Se declaran cuatro licencias de codificación y una de
análisis. Los datos son una fotografía documental, no prueba de dotación actual.

### Flujo de ficha y datos

1. Censo DIG recibe la ficha desde Recaudación Central y deja trazabilidad en
   cuaderno/archivador.
2. Completa datos administrativos del IEEH.
3. Codificadores leen diariamente el episodio en ficha papel o digital:
   diagnóstico principal, comorbilidades, complicaciones, procedimientos,
   exámenes y contexto relacionado.
4. Diagnósticos se codifican con CIE-10 y procedimientos con CIE-9 según las
   reglas declaradas.
5. La ficha se devuelve a Archivo mediante cuaderno, idealmente el mismo día.
6. Los egresos se incorporan a WIS, se cotejan con IEEH y se exportan a TEAM
   CODER.
7. Se completa CMBD, se agrupa, valida y corrige; los episodios inagrupables no
   pasan a la base nacional.
8. Los datos validados se publican para MINSAL/FONASA y alimentan informes.

El respaldo informático se atribuye a servidores hospitalarios administrados por
TIC. El manual no especifica arquitectura, cifrado, retención, restauración ni
evidencia de pruebas de respaldo.

### Reglas de codificación preservadas

- estado agudo: episodio usualmente menor a 30 días; se prioriza sobre el crónico
  salvo código combinado; subagudo se registra como agudo;
- etiologías múltiples: si al alta siguen siendo sólo alternativas, se usa causa
  desconocida; si se confirman varias, se codifican todas;
- signo/síntoma: sólo se usa como principal cuando no hay diagnóstico final más
  específico; hallazgos propios de una enfermedad no agregan código y laboratorio
  anormal aislado no se codifica si existe diagnóstico confirmado;
- diagnóstico de sospecha al alta: “probable”, “posible”, “por descartar” u otra
  formulación semejante se acepta como definitivo en hospitalización según la
  regla impresa;
- sospecha posteriormente descartada sin afección tratable: se usan códigos de
  observación/evaluación; si existe lesión, signo, síntoma o enfermedad, esa
  afección queda como principal.

Estas son reglas de codificación del documento, no reglas de decisión clínica ni
autorización para alterar lo consignado por el equipo tratante.

## 2. Informes e indicadores GRD

La Sección GRD genera un informe estándar mensual y reportes de BSC, COMGES,
metas sanitarias y solicitudes específicas. El estándar debe remitirse a
dirección/jefaturas/referentes a más tardar el día 30 del mes siguiente y presenta
una “fotografía” al momento de extracción.

Familias de salida preservadas:

- producción por hospitalización, cirugía mayor ambulatoria, hospitalización
  diurna y hospitalización en Urgencia;
- egresos, peso medio, UPH, mortalidad, estancias, ocupación, IEMA e índice
  funcional;
- outliers, reingresos, intervenciones quirúrgicas, ambulatorización, unidades
  críticas y donación;
- bases mensuales para REM 20, pediatría quirúrgica, APS, cobros no FONASA,
  gestión quirúrgica y análisis por servicios.

Tras cerrar y codificar el mes se corrigen errores/inagrupables. ALCOR se usa con
credencial individual, parámetros y filtros; el resultado puede guardarse,
exportarse, imprimirse y compartirse. Las capturas pobladas y valores mensuales
del ejemplo 2024 se excluyen: ilustran la forma, no constituyen reglas ni datos a
preservar.

## 3. Depuración del CMBD

Objetivo: entregar el CMBD sin errores/incoherencias y asegurar correcta
asignación GRD. Se revisan valores nulos o inválidos en episodio, paciente,
atención y otros; además:

- neonatos sin peso, tumores sin morfología, estancias prequirúrgicas ≥2 días y
  estancias ≥60 días;
- concordancia entre episodios, tipo de actividad, especialidad, servicio,
  diagnóstico, procedimiento, sexo, edad y motivo de egreso;
- fallecidos contra Estadística y, si es posible, Registro Civil;
- códigos Z y B95–B96 usados impropiamente como diagnóstico principal;
- fechas de intervención, uso de pabellón, partos, ventilación mecánica y
  estancias negativas;
- procedencia, hospital de origen, servicios inexistentes, duplicados de episodio
  o ficha, egreso y modalidad previsional;
- ingreso urgente versus programado y consistencia diagnóstico–GRD.

Las validaciones se cotejan entre ALCOR, TEAM CODER, Estadística y fuentes
clínicas. El manual no aporta tasa de error, resultado de auditoría ni evidencia
de ejecución mensual.

## 4. Censo diario de camas, pacientes e IEEH

### Unidad de cuenta

El día censal va de 00:00 a 24:00. El proceso cuenta ocupación, disponibilidad,
ingresos, traslados y egresos en camas de dotación y CMA. Exige respaldo mediante
IEEH y ficha clínica. La dotación se fija por resolución del Servicio de Salud y
puede modificarse transitoria o definitivamente mediante solicitud formal.

### Flujo prescrito

- Admisión/DGU genera IEEH en horario hábil; DIG lo confecciona al día siguiente
  para ingresos de horario inhábil.
- El original acompaña la ficha y las copias se ordenan por servicio para seguir
  cama/paciente y validar el censo.
- Cada ingreso se registra en la aplicación local de censo; la planilla SGH diaria
  identifica ocupación, ingresos, traslados y altas.
- De lunes a viernes la planilla se remite a supervisiones/secretarías clínicas
  para corroboración.
- Se evita duplicar ingresos del mismo paciente/día y se cotejan IEEH, ficha y
  sistema clínico.
- Las solicitudes a Archivo usan acuse y libro; toda salida de ficha debe quedar
  registrada. Si no existe ficha se crea una con datos verificados.
- La entrega de documentos al servicio identifica a quien recibe; el manual pide
  nombre legible y evita depender sólo de una firma.
- Traslados y altas actualizan originales/duplicados y planillas; faltantes de fin
  de semana van al libro de novedades.
- El alta se completa al llegar la ficha, se entrega a GRD y se incorpora a REM
  20. La cuadratura diaria declarada es: **existencia = ingresos − egresos**, en
  continuidad con la existencia anterior.

Las interacciones con Archivo describen préstamos, trazabilidad y devolución
dentro de este flujo; no definen todo el gobierno archivístico.

## 5. Vigilancia de atenciones de Urgencia

El DAU electrónico es fuente de atenciones, causas, edades, hospitalizaciones y
cirugía de urgencia. Se conserva digitalmente; se entrega copia al usuario y, si
hay hospitalización, se incorpora a la ficha.

Cada día, incluidos días no hábiles, idealmente durante la mañana, DIG debe:

1. extraer todos los episodios de la fecha en CSV;
2. separar/formatear campos y nombrar el archivo por fecha;
3. importarlo en WIS;
4. obtener el resumen IRA/otras causas;
5. transferir y guardar la información en la plataforma DEIS.

Se excluyen URL, credenciales y capturas pobladas. El procedimiento no demuestra
que las cargas se hayan realizado completas o dentro del plazo.

## 6. Información GRD/REM para COMGES, BSC y metas

DIG extrae antecedentes desde ALCOR/TEAM CODER y REM, configura fecha,
establecimiento, parámetros y análisis, y entrega los resultados a jefaturas,
Servicio de Salud y DEIS/MINSAL. Antes del análisis deben estar disponibles y
codificados los egresos y CMA del mes, y deben concordar TEAM CODER y REM 20.

La fuente contextualiza COMGES en RISS, pero no convierte indicadores de 2024 en
metas vigentes posteriores ni acredita resultados.

## 7. Registro Estadístico Mensual

Los servicios/unidades originan registros en papel o formato electrónico según
su cartera. En papel deben ser legibles, sin abreviaturas ni hojas deterioradas;
en digital deben cumplir requisitos institucionales. Las series declaradas son:

- **REM A:** producción, A01–A33 y REM 20;
- **REM BS/B17:** producción asociada a códigos/arancel FONASA;
- **REM P:** cobertura semestral de programas/población.

Compras de servicio no son producción propia y se registran como compra en las
series señaladas; ventas de servicios se atribuyen como producción del
establecimiento vendedor.

DIG organiza ocho módulos: odontología; profesionales no médicos ambulatorios;
procedimientos médicos ambulatorios; prestaciones médicas abiertas; farmacia;
atención cerrada; IRA/Urgencia; y censo/camas para REM 20. Consolida a fin de mes,
separa beneficiarios, edades y criterios, completa primero serie A y luego B, y
adapta bases ante cambios de REM.

Plazos: servicios/unidades deben entregar al DIG hasta el tercer día hábil del
mes siguiente; el establecimiento envía al Servicio de Salud hasta el séptimo día
hábil.

## 8. Ingreso de IEEH a DEIS

El IEEH completo contiene categorías demográficas, hospitalización, diagnóstico,
procedimientos y, si corresponde, nacimiento. Diagnósticos usan CIE-10 y cirugía
código FONASA. Puede cargarse manualmente o masivamente desde GRD; el archivo
debe respetar estructura/año y superar el validador. Los errores bloquean el
cierre hasta su corrección y cada registro recibe correlativo.

La fuente estima 5–8 minutos por ingreso manual según estabilidad del sistema.
No se reproducen identificadores personales ni credenciales descritos en las
pantallas.

## 9. SIGCOM y costeo por absorción

SIGCOM combina:

- remuneraciones, honorarios, presupuesto, abastecimiento y gastos;
- producción final desde egresos, consultas, atenciones y REM;
- producción de apoyo: cirugía, camas críticas, procedimientos, partos,
  laboratorio, imagenología, kinesiología, farmacia, dolor, anatomía patológica,
  banco de sangre, alimentación, servicios generales, lavandería, mantenimiento
  y esterilización;
- horas disponibles por profesión/oficio y programación clínica.

El costeo distribuye primero costos directos; luego costos entre centros de apoyo
por método escalonado; finalmente los asigna a centros finales mediante unidades
de producción y consumo. El resultado declarado relaciona gastos, producción y
horas con centros de costo y genera informes mensuales/indicadores. No acredita
exactitud contable, conciliación ni uso decisional efectivo.

## Distribución, registro y mejora

Distribución: Servicio de Salud Ñuble, Dirección y servicios HSC. Jefaturas de
sección y DIG velan por cumplimiento y proponen ajustes requeridos por la
práctica. Los registros se declaran en REM y DEIS. La tabla de control de cambios
está vacía; sólo se evidencia la primera edición.

## Contradicciones y defectos preservados

1. El memorándum agrega una página física a las 58 páginas del manual.
2. Portada y páginas 1–57 dicen vigencia/revisión septiembre de 2029; la página
   58 dice septiembre de 2028.
3. Dos referencias aparecen duplicadas en el listado normativo.
4. El texto alterna `HHCC`, “ficha clínica” y, en algunos pasajes, `FFCC` sin
   aclarar si esta última sigla es equivalente o un error.
5. La numeración coloca “6. Desarrollo” y luego “7. Introducción”.
6. La ecuación diaria se imprime como “existencia = ingresos − egresos”; sólo es
   coherente si se entiende agregada a la existencia anterior, detalle no escrito
   en esa fórmula aislada.
7. El manual describe bases propias y digitación desde papel, pero no aporta
   inventario de integraciones, diccionario de datos, responsables de calidad por
   campo ni controles de seguridad verificables.

## Frontera HODOM y hd-hsc-os

La definición impresa de paciente hospitalizado depende de ocupar una cama
hospitalaria de dotación y de contar con IEEH/ficha. No puede proyectarse sin más
a una cama virtual o episodio HODOM. La fuente no define admisión domiciliaria,
ocupación virtual, ubicación del paciente, cuidador, dispositivo en hogar,
visitas, traslado, alta HODOM ni su traducción a REM/IEEH/GRD.

El manual aporta preguntas de interfaz —quién origina el dato, qué episodio se
cuenta, cómo se reconcilia con DIG, qué plazo y qué trazabilidad—, pero no prueba
adopción por HODOM. Tampoco es contrato de datos, arquitectura, API o práctica de
`hd-hsc-os`; esas afirmaciones requieren evidencia contemporánea separada.
