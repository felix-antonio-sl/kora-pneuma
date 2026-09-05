---
urn: urn:salud:kb:umbrales-clinicos-hospitalizacion
nombre: umbrales-clinicos-hospitalizacion
version: 1.0.0
estado: publicado
descripcion: "Umbrales clinicos operables para hospitalizacion de adultos: criterios de estabilidad para alta (IDSA/ATS, Halm), metas de saturacion de oxigeno (BTS 2017), tiempo a antibiotico y tamizaje de sepsis (Surviving Sepsis Campaign 2021, qSOFA vs NEWS2/SIRS/MEWS). Funda los cortes que las skills asistencial-hospital y asistencial-hodom aplican al pie de cama."
fuente: "Sintesis de fuentes OFICIALES (web, 2026-06-22) para anclar los umbrales {{verificar}} de la skill asistencial-hospital; no es koraficacion de un solo documento sino sintesis multi-fuente con citacion (patron conocimiento-web, igual que urn:salud:kb:notificacion-eno-iaas). Fuentes primarias: BTS Guideline for oxygen use in adults in healthcare and emergency settings (2017, Thorax 72:i1-i90; brit-thoracic.org.uk; PMC5531304); criterios de estabilidad clinica de Halm (JAMA 1998) validados en Aliberti et al. Eur Respir J 2013;42:742 y recogidos por las guias ATS/IDSA de neumonia adquirida en la comunidad (2007 y Metlay et al. Am J Respir Crit Care Med 2019;200:e45-e67); Surviving Sepsis Campaign 2021 (Evans et al. Intensive Care Med 2021;47:1181-1247, DOI 10.1007/s00134-021-06506-y; PMC8486643). Anclado ademas al corpus local de medicina de emergencia (urn:salud:kb:me-infecciones-respiratorias-bajas, urn:salud:kb:me-fiebre-sin-foco) que ya funda parte de estos cortes desde el lado de urgencias. Perfil mixto: sintesis tecnica con tablas; todas las cifras y citas verificadas en fuente. Caveat: los numeros son de guia internacional — el protocolo local del establecimiento prevalece y se documenta."
autor: FS
creado: 2026-06-22
lang: es
tags: [salud, hospitalizacion, estabilidad-clinica, alta, oxigenoterapia, sepsis, surviving-sepsis-2021, qsofa, news2, idsa-ats, bts, umbrales]
cita: [urn:salud:kb:me-infecciones-respiratorias-bajas, urn:salud:kb:me-fiebre-sin-foco, urn:salud:kb:management-engineering-ext-capacidad]
familia: nota
---

# Umbrales clínicos operables para hospitalización de adultos

Cortes cuantitativos que gobiernan dos decisiones de pie de cama: **cuándo el
paciente está estable para el alta** y **cuándo escalar**. Cada umbral cita su
guía. Son referencias de guía internacional: donde el establecimiento fije un
protocolo local, este prevalece y se documenta. Cohorte adulta; no aplica a
pediatría ni obstetricia.

## Estabilidad clínica para el alta (IDSA/ATS — criterios de Halm)

Los criterios de estabilidad clínica de Halm (JAMA 1998), validados por Aliberti
2013 y adoptados por las guías ATS/IDSA de neumonía adquirida en la comunidad
(2007; Metlay 2019), son el estándar objetivo para decidir el alta hospitalaria.
El paciente alcanza estabilidad cuando, **respirando aire ambiente**, cumple
todos:

| Parámetro | Umbral de estabilidad |
|---|---|
| Temperatura | ≤ 37.8 °C (afebril) |
| Frecuencia cardíaca | ≤ 100 lpm |
| Frecuencia respiratoria | ≤ 24 rpm |
| Presión arterial sistólica | ≥ 90 mmHg |
| SatO₂ periférica | ≥ 90% sin O₂ suplementario |
| Estado mental | normal / basal |
| Tolerancia a vía oral | conservada |

Dos precisiones de la guía 2019 que corrigen prácticas tradicionales:

- **No se requiere un período fijo de observación tras alcanzar la estabilidad.**
  Metlay 2019 recomienda el alta una vez el paciente está clínicamente estable,
  tolera la vía oral y no tiene otro problema médico activo; prolongar la estancia
  «para observar 24–48 h más» no está respaldado. El «afebril 48 h antes del alta»
  es práctica heredada, no requisito de guía; lo fundado es la **tendencia afebril
  (T ≤ 37.8 °C) sostenida** dentro del set de estabilidad.
- **El umbral de estabilidad (SatO₂ ≥ 90%) no es lo mismo que el piso operativo de
  alta.** ≥ 90% es el corte por debajo del cual el paciente es inestable. Un piso
  de alta domiciliaria por encima de ese mínimo (p. ej. ≥ 92%) es margen de
  seguridad clínico explícito, no un número de guía: declararlo como tal, no
  presentarlo como criterio IDSA/ATS.

## Oxigenoterapia — metas de saturación (BTS 2017)

La guía BTS de oxígeno en adultos fija el rango objetivo según el riesgo de
insuficiencia respiratoria hipercápnica:

| Población | Meta SatO₂ |
|---|---|
| Sin riesgo de fallo hipercápnico | **94–98%** |
| Riesgo de fallo hipercápnico (EPOC u otros) | **88–92%**, pendiente gasometría |

SatO₂ ~92–93% equivale a PaO₂ ~10 kPa; por encima de ese nivel la mayoría de los
hipercápnicos asociaba acidosis, de ahí el techo de 92% en el grupo de riesgo. Si
la PCO₂ resulta normal, la meta puede ajustarse a 94–98% salvo historia de fallo
respiratorio con soporte ventilatorio. El corpus local ya funda este 88–92% para
la exacerbación de EPOC en urn:salud:kb:me-infecciones-respiratorias-bajas.

## Sepsis — tiempo a antibiótico (Surviving Sepsis Campaign 2021)

La SSC 2021 estratifica el tiempo a antimicrobiano por probabilidad de sepsis y
presencia de shock (Evans 2021):

| Escenario | Ventana a antibiótico |
|---|---|
| Shock séptico, o sepsis con **alta probabilidad** | **≤ 1 hora** — inmediato (recomendación fuerte) |
| Sepsis **posible sin shock** | evaluación rápida de causas infecciosas/no infecciosas; decidir **≤ 3 horas** si administrar o diferir vigilando |

Distinguir de la neumonía hospitalizada **sin** sepsis: la ventana práctica de
antibiótico en NAC es ≤ 4 h desde la valoración inicial, con hemocultivos antes o
≤ 1 h tras el inicio del antibiótico (ATS/IDSA 2019), tal como recoge
urn:salud:kb:me-infecciones-respiratorias-bajas. La regla de 1 h es de sepsis con
shock, no de toda infección.

## Tamizaje de deterioro y sepsis — qSOFA vs NEWS2/SIRS/MEWS (SSC 2021)

Recomendación **fuerte, evidencia moderada**: **la SSC 2021 recomienda EN CONTRA
de usar qSOFA, comparado con SIRS, NEWS o MEWS, como herramienta única de tamizaje
de sepsis o shock séptico.**

- qSOFA es **más específico pero menos sensible**: en la derivación original solo
  el 24% de los infectados tenía qSOFA ≥ 2, aunque ese grupo concentraba el 70% de
  los malos desenlaces.
- Por eso su rol es **predecir desenlace una vez sospechada/diagnosticada la
  sepsis**, no detectarla de entrada. Para el tamizaje y la detección temprana de
  deterioro se prefieren **NEWS2** (o MEWS/SIRS) junto con la medición de lactato.
- Implicación operable: qSOFA ≥ 2 ante sospecha de infección marca **alto riesgo y
  obliga a evaluación de gravedad/escalamiento**; no debe ser el filtro único que
  decide si se busca sepsis. El protocolo de sepsis del corpus vive en
  urn:salud:kb:me-fiebre-sin-foco.

## Caveats de verificación

- Los umbrales son de **guía internacional**; el protocolo local del establecimiento
  (servicio de medicina, comité de IAAS/sepsis) prevalece y se documenta.
- Los criterios de estabilidad de Halm se derivaron y validaron principalmente en
  **neumonía adquirida en la comunidad**; se usan como referencia general de
  estabilidad pero un paciente con otra patología puede requerir criterios
  adicionales propios de su diagnóstico.
- El piso de alta por SatO₂ por encima de 90% (margen) es decisión clínica local,
  no un número de guía.

## Fuentes oficiales

- BTS Guideline for oxygen use in adults in healthcare and emergency settings
  (2017): https://www.brit-thoracic.org.uk/clinical-resources/guidelines/emergency-oxygen/
  ; PMC5531304.
- Surviving Sepsis Campaign 2021 (Evans et al., Intensive Care Med 2021;47:1181-1247):
  https://link.springer.com/article/10.1007/s00134-021-06506-y ; PMC8486643 ; SCCM
  https://www.sccm.org/clinical-resources/guidelines/guidelines/surviving-sepsis-guidelines-2021
- Criterios de estabilidad clínica (Halm et al., JAMA 1998; validación Aliberti et al.,
  Eur Respir J 2013;42:742): https://publications.ersnet.org/content/erj/42/3/742
- ATS/IDSA CAP guideline 2019 (Metlay et al., Am J Respir Crit Care Med 2019;200:e45-e67):
  https://www.atsjournals.org/doi/10.1164/rccm.201908-1581ST
