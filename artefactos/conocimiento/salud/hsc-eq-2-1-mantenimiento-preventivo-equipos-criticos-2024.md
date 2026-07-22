---
urn: urn:salud:kb:hsc-eq-2-1-mantenimiento-preventivo-equipos-criticos-2024
nombre: hsc-eq-2-1-mantenimiento-preventivo-equipos-criticos-2024
version: 1.0.0
estado: publicado
descripcion: "Programa HSC de clasificación, planificación, ejecución y registro del mantenimiento preventivo de equipos clínicos críticos y ambulancias."
fuente: "Hospital de San Carlos Dr. Benicio Arzola Medina, Programa de Mantenimiento Preventivo de Equipos Críticos, código EQ 2.1, octava edición, enero de 2024, vigencia enero de 2029; Google Drive file id 1wulRh3lv7mxheSN6YC44BrzshZVowwQ0; sha256:23e785d8c1ae67122a904f5052a1c6979f8e88c3b403776bc371f52ab1d1d9e2; PDF digital de 14 páginas y 494.437 bytes. Extracción nativa por página y cotejo visual 14/14. Recorte institucional-operativo: excluye logos, paginación, geometría, repetición literal, nombres, firmas y campos vacíos; conserva identidad, alcance, método de riesgo, puntajes, frecuencias, criterios, flujos, registros y contradicciones."
autor: Codex
creado: 2026-07-22
lang: es
tags: [hsc, equipamiento-critico, mantenimiento-preventivo, riesgo, fennigkoh-smith, ambulancias, carta-gantt]
familia: fuente
cita: []
---

# Mantenimiento preventivo de equipos críticos — HSC EQ 2.1

## Identidad, alcance y frontera

| Elemento | Hecho documental |
|---|---|
| Código / edición | EQ 2.1 / octava |
| Fecha / vigencia impresa | Enero de 2024 / enero de 2029 |
| Alcance | Monitores hemodinámicos con al menos SpO2, ECG y presión no invasiva; desfibriladores y DEA; ventiladores fijos/transporte; anestesia; incubadoras neonatales; ambulancias de Urgencia |
| Aprobación visible | Portada firmada; sin resolución separada en el PDF |

La fuente estaba vigente al 22 de julio de 2026. El estado KORA describe la
madurez del artefacto, no la vigencia ni la implementación de la fuente. El
alcance es una clase documental, no un inventario verificado.

El programa gobierna equipos y vehículos institucionales. No acredita
mantenimiento, factor de riesgo, proveedor ni respaldo de dispositivos
domiciliarios de HODOM.

## Propósito, gobierno y referencias

Busca reducir fallas y tiempo muerto, proteger vida, seguridad, disponibilidad
y vida útil, mantener equipos operativos y controlar costo. Equipos Médicos
ejecuta y propone cambios; la jefatura de Ingeniería y Mantención aprueba y hace
cumplir el programa.

Referencias: pauta MINSAL 2016 para planes de equipos; norma de seguridad y
calidad sobre mantenimiento crítico; pautas de fabricantes; NCh 2893; Norma
Técnica de Mantenimiento Hospitalario–Equipos Médicos, Decreto Exento N.º 290
de 2017.

**Electromédico** — equipo conectado a red que diagnostica, trata o vigila bajo
supervisión y contacta o intercambia energía con el paciente, según NCh 2893.  
**Preventivo** — frecuencia predeterminada para prevenir falla.  
**Correctivo** — acción para resolver problema funcional.

## Factor de riesgo Fennigkoh y Smith

`factor = función + riesgo físico + requerimiento de mantenimiento`.

| Función | Puntaje |
|---|---:|
| Soporte vital | 10 |
| Quirúrgica / intensivo | 9 |
| Terapia y tratamiento | 8 |
| Monitorización quirúrgica/intensiva | 7 |
| Monitorización y diagnóstico fisiológico | 6 |
| Analítica de laboratorio | 5 |
| Accesorio de laboratorio | 4 |
| Procesamiento de datos | 3 |
| Otra relacionada con paciente | 2 |
| No relacionada con paciente | 1 |

| Consecuencia física | Puntaje |
|---|---:|
| Muerte | 5 |
| Lesión de paciente u operador | 4 |
| Terapia inapropiada o diagnóstico perdido | 3 |
| No significativo / insignificante | 2 / 1 |

| Mantenimiento | Puntaje |
|---|---:|
| Extensivo, componentes | 5 |
| Avanzado, calibración rutinaria | 4 |
| Medio, lubricación | 3 |
| Bajo, limpieza interna | 2 |
| Mínimo, inspección visual no relacionada con paciente | 1 |

Índice `>10` ingresa al plan; `>15` se considera crítico. Ejemplos impresos:
anestesia 20, ventilador 20, hemodinámico 14, desfibrilador 20, incubadora 20;
ambulancia “no aplica”. El monitor de 14 está en el alcance de “equipos
críticos” aunque no supera `>15`: discordancia taxonómica preservada.

Antigüedad, uso, pautas de acreditación, estado y fabricante complementan el
puntaje; no se usa como decisión única.

## Planificación anual

| Equipo | Frecuencia | Período |
|---|---|---|
| Monitor hemodinámico | 2/año | 2.º y 4.º trimestre |
| Ventilador fijo/transporte | 2/año | 2.º y 4.º trimestre |
| Máquina de anestesia | 2/año | 2.º y 4.º trimestre |
| Desfibrilador | 2/año | 2.º y 4.º trimestre |
| DEA | 1/año | 2.º trimestre |
| Incubadora | 2/año | 2.º y 4.º trimestre |
| Ambulancia | Cada 10.000 km | Según kilometraje |

La Carta Gantt digital anual identifica tipo, marca, modelo, inventario y
unidad; estado operativo, respaldo o alta de inventario; frecuencia y período.
“Operación” significa uso permanente en servicio; “back-up”, resguardo
disponible para falla, con frecuencia más baja.

## Criterios mínimos

| Equipo | Verificaciones preservadas |
|---|---|
| Ambulancia | Cambio de aceite y filtro |
| Desfibrilador | Exterior; display; energía de desfibrilación; sincronismo/cardioversión; frecuencia/energía de marcapaso; ECG; seguridad eléctrica; alarmas; batería/AC; limpieza |
| Incubadora | Exterior/display; temperatura; humedad; oxígeno; balanza; seguridad eléctrica; alarmas; batería/AC; limpieza |
| Anestesia | Exterior/display; circuitos inspiratorio/espiratorio; sensor de flujo/trampa; distribución/control/monitoreo de gases medicinales y anestésicos; vaporizadores; alarmas; batería/AC; limpieza |
| Monitor hemodinámico | Exterior/display; simulación ECG, SpO2, NIBP y temperatura; seguridad eléctrica; alarmas; batería/AC; limpieza |
| Ventilador | Exterior/display; presiones; flujo; humidificador; seguridad eléctrica; alarmas; batería/AC; limpieza |

## Ejecución, informe y reprogramación

El preventivo puede ser interno —Equipos Médicos— o externo —convenio,
representante o proveedor—. Se coordina con enfermería de la unidad. Puede
realizarse en proveedor o HSC conforme a contrato/cotización.

El proveedor emite informe; Equipos Médicos contrasta orden de trabajo,
protocolo de fábrica y mínimos, archiva en hoja de vida y planilla. Una anomalía
mayor con repuesto fuera de convenio pasa a correctivo y nueva solicitud de
compra.

Reprogramación procede por falla previa, diagnóstico externo o sobredemanda,
importación de repuestos, stock clínico limitado/demanda o indisponibilidad del
proveedor. Puede adelantarse máximo un mes. La factibilidad se evalúa, se avisa
a supervisión y la gestión completa debe ocurrir dentro de máximo un mes según
el texto.

Equipos nuevos ingresan sólo tras instalación, puesta en marcha y capacitación.

## Ambulancias

Aceite y filtro cada 10.000 km, con tolerancia de ±4.000 km sólo si necesidades
del servicio lo exigen y no existe riesgo visible para personas, operación o
bienes. Cada vehículo tiene hoja de vida con kilometraje e intervenciones. Los
conductores informan anomalías en hoja de ruta diaria; Equipos Críticos evalúa y,
si excede recursos internos, deriva a proveedor mediante circuito equivalente
al preventivo.

## Registros, distribución e historia

Registros: hoja de vida física/digital y planilla de seguimiento. Distribución:
Dirección, subdirecciones Médica, Recursos Físicos y Gestión del Cuidado,
servicios implicados, Ingeniería/Mantención, Abastecimiento y Calidad.

| Fecha | Edición resultante |
|---|---|
| Agosto de 2013 | Tercera |
| Junio de 2015 | Cuarta |
| Abril de 2017 | Quinta |
| Abril de 2019 | Sexta |
| Abril de 2022 | Séptima |
| Enero de 2024 | Octava; incorpora criterios mínimos |

## Valor y frontera HODOM

Aporta puntuación de criticidad, calendario, estados operativo/back-up,
preventivo/correctivo, reprogramación e ingreso de equipo nuevo. No debe usarse
para afirmar que un dispositivo domiciliario está mantenido, es crítico o tiene
back-up; esas propiedades requieren evidencia por equipo y circuito HODOM.
