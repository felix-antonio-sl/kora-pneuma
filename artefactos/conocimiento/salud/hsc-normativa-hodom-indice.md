---
urn: urn:salud:kb:hsc-normativa-hodom-indice
nombre: hsc-normativa-hodom-indice
version: 1.0.0
estado: publicado
descripcion: "Normativa y protocolos HSC de relevancia para HODOM: indice del corpus koraficado, resuelto por URN"
fuente: "Corpus KORA pneuma artefactos/conocimiento/salud (hsc-*, minsal-*, hodom-*) censado con kora.py censo al 2026-08-05; curaduria hd-dt 01-normativo/hsc/INDICE.md y subarbol-candidatos-koraficacion-hodom-2026-07-20.md; regla de autoridad D-025BN (fuentes primarias en Drive institucional HSC = oficiales y vigentes)"
autor: FS
creado: 2026-08-05
lang: es
tags: [salud, hodom, hsc, hospital-san-carlos, normativa, protocolos, indice]
familia: bok
cita: [urn:salud:kb:hodom-reglamento-ds1-2022, urn:salud:kb:hodom-decreto-exento-31-2024, urn:salud:kb:hodom-norma-tecnica-2024, urn:salud:kb:hodom-direccion-tecnica, urn:salud:kb:hodom-glosario-ontologia, urn:salud:kb:hodom-rpe-34-criterios-tecnicos, urn:salud:kb:hodom-manual-alta-complejidad, urn:salud:kb:hodom-situacion-chile-2026, urn:salud:kb:hodom-invariante-no-equivale-cerrada, urn:salud:kb:hsc-pro-002-hospitalizacion-domiciliaria, urn:salud:kb:hsc-pro-110-hodom-historico-2019, urn:salud:kb:hsc-cartera-servicios-2024, urn:salud:kb:hsc-arsenal-farmacoterapeutico-2026, urn:salud:kb:minsal-decreto-exento-74-2024-mcc, urn:salud:kb:hsc-mo-ugdp-mov-002-organizacion-copia-observada, urn:salud:kb:hsc-pro-134-gestion-pacientes-recorte-hodom, urn:salud:kb:hsc-aoc-2-1-derivacion-pacientes, urn:salud:kb:hsc-apt-1-2-transporte-pacientes-historico, urn:salud:kb:minsal-contactabilidad-nucleo-operativo, urn:salud:kb:hsc-dp-2-1-consentimiento-informado, urn:salud:kb:hsc-14-2-prestamo-catres-clinicos, urn:salud:kb:hsc-14-3-riesgo-biopsicosocial, urn:salud:kb:hsc-aoc-1-1-emergencia-riesgo-vital, urn:salud:kb:hsc-gcl-2-3-vigilancia-eventos-adversos, urn:salud:kb:hsc-reg-1-1-ficha-clinica-unica, urn:salud:kb:hsc-reg-1-2-estandarizacion-registros-clinicos, urn:salud:kb:hsc-gcl-1-12-identificacion-pacientes, urn:salud:kb:minsal-nt-245-identificacion-pacientes]
---

# Normativa y protocolos HSC de relevancia para HODOM

Índice del corpus koraficado: organiza y disponibiliza la normativa nacional y
los protocolos locales del Hospital de San Carlos (HSC) que inciden sobre
HODOM-HSC. Cada entrada resuelve por URN a un artefacto de conocimiento
publicado; el cuerpo de cada uno vive en su fuente y no se duplica aquí.

## Reglas de lectura

- **Autoridad (D-025BN):** las fuentes primarias alojadas en el Drive
  institucional «Gestión Documental HSC» son oficiales y vigentes en HSC, aun
  con fecha impresa terminada, cuando no se identifica actualización, sucesor
  o retiro. Esta ratificación no prueba aplicabilidad HODOM, práctica ni
  cumplimiento, y no desplaza normativa superior.
- **Fuentes tipadas, no evidencia:** los artefactos `hsc-*` preservan norma,
  procedimiento o formulario local; no demuestran circuito HODOM adoptado,
  práctica observada ni autorización de actos.
- **Selección del programa:** los horizontes H0/H1/H2 y las familias PF/FN/FH/FC
  provienen de la curaduría en `hd-dt`
  (`01-normativo/hsc/INDICE.md`, `subarbol-candidatos-koraficacion-hodom-2026-07-20.md`),
  que sigue siendo el instrumento de selección y adquisición; este índice
  resuelve su estado koraficado en Pneuma.
- **Resolución:** `python3 kora.py nombre <urn>` desde la raíz de pneuma.

## 1. Canon nacional HODOM

| URN | Documento | Uso |
|---|---|---|
| `urn:salud:kb:hodom-reglamento-ds1-2022` | DS 1/2022 — Reglamento HODOM | marco reglamentario base |
| `urn:salud:kb:hodom-decreto-exento-31-2024` | Decreto Exento 31/2024 | aprobación de la Norma Técnica HODOM 2024 |
| `urn:salud:kb:hodom-norma-tecnica-2024` | Norma Técnica HODOM 2024 | requisitos técnicos de la modalidad |
| `urn:salud:kb:hodom-direccion-tecnica` | Manual de dirección técnica HODOM | rol, responsabilidades y doctrina del DT |
| `urn:salud:kb:hodom-glosario-ontologia` | Glosario y ontología HODOM | vocabulario de dominio |
| `urn:salud:kb:hodom-rpe-34-criterios-tecnicos` | RPE-34 — criterios técnicos HODOM | criterios de programación y cartera |
| `urn:salud:kb:hodom-manual-alta-complejidad` | Manual HODOM de alta complejidad | modalidad de alta complejidad |
| `urn:salud:kb:hodom-situacion-chile-2026` | Situación HODOM Chile 2026 | contexto y estado de la modalidad |
| `urn:salud:kb:hodom-invariante-no-equivale-cerrada` | Invariante HODOM ≠ hospitalización cerrada | invariante de dominio |

Los cuerpos largos del canon se particionan en shards que continúan el mismo
documento; los raíces no los listan, por lo que se declaran aquí:

| Partición | Continúa |
|---|---|
| `urn:salud:kb:hodom-direccion-tecnica-p02`, `urn:salud:kb:hodom-direccion-tecnica-p03` | `urn:salud:kb:hodom-direccion-tecnica` |
| `urn:salud:kb:hodom-manual-alta-complejidad-p02`, `urn:salud:kb:hodom-manual-alta-complejidad-p03`, `urn:salud:kb:hodom-manual-alta-complejidad-p04` | `urn:salud:kb:hodom-manual-alta-complejidad` |
| `urn:salud:kb:hodom-situacion-chile-2026-p02`, `urn:salud:kb:hodom-situacion-chile-2026-p03`, `urn:salud:kb:hodom-situacion-chile-2026-p04`, `urn:salud:kb:hodom-situacion-chile-2026-p05` | `urn:salud:kb:hodom-situacion-chile-2026` |

El corpus operacional de la unidad (`urn:salud:kb:hodom-operacional-indice`,
`urn:salud:kb:hodom-operacional-iaas`, `urn:salud:kb:hodom-operacional-indicadores`)
queda **fuera del alcance** de este índice: describe la operación real
observada, no normativa ni protocolos.

## 2. Núcleo situado HSC — H0

| URN | Documento | Uso |
|---|---|---|
| `urn:salud:kb:hsc-pro-002-hospitalizacion-domiciliaria` | PRO 002 (2022) | dispositivo local HODOM: campaña de invierno, horarios y escalamiento |
| `urn:salud:kb:hsc-pro-110-hodom-historico-2019` | HSC 34.1 PRO-110 (2019) | versión anterior; relación controladora con PRO 002 abierta |
| `urn:salud:kb:hsc-cartera-servicios-2024` | Res. Exenta 1206/2024 | cartera de servicios HSC 2024, prestaciones HODOM por estamento |
| `urn:salud:kb:hsc-pro-167-aplicacion-indice-barthel` | PRO-167 (2022, vigencia nov 2027) | Índice de Barthel ≥65 años al ingreso (Enfermería) y egreso (Médico): métrica de dependencia para egreso a domicilio y traspaso APS vía CAE |
| `urn:salud:kb:hsc-pro-053-hospitalizacion-desde-unidad-emergencia` | PRO-053 (2013, Res. Ex. 0378/2014) | compuerta UE→cama: orden en DAU, recetón 24 h, cama vía UGCC hábil/enfermería fuera de hora, categorización de riesgo y hoja de ruta con 4 tiempos |
| `urn:salud:kb:hsc-pro-076-carga-combustible-ambulancias` | PRO-076 (2016, Res. Ex. 4292/2016) | flota SAMU/traslado: registro de kilometraje y combustible por móvil, tarjeta en convenio y circuito Mantención→Abastecimiento→Finanzas; línea base decisión #10 |
| `urn:salud:kb:hsc-pro-126-rehabilitacion-pulmonar` | PRO-126 (2019) | programa de rehabilitación pulmonar (EPOC/ERA): inclusión/exclusión, TM6M, 24 sesiones al 70% de carga; escalamiento y egreso kinésico del paciente HD respiratorio |
| `urn:salud:kb:hsc-pro-091-gestion-eliminacion-medicamentos-vencidos` | PRO-091 (2022, Res. Ex. 1365) | ciclo de mermas: CAF mensual, ajuste SIGBO, comisión ministros de fe, resolución semestral, segregación REAS y SIDREP; destino del fármaco devuelto desde domicilio |
| `urn:salud:kb:hsc-pro-023-manejo-brotes-iaas` | PRO-023 (2022, 4ª ed.) | brotes IAAS: definiciones y umbrales, notificación SICARS/SEREMI, estudio en 10 pasos; régimen aplicable a conglomerados infecciosos en pacientes HD |
| `urn:salud:kb:hsc-pro-186-teletaco-anticoagulante-oral` | PRO 186 (2024) | teleanticoagulación UNITEL: TEP/TVP, FA, prótesis valvulares; INR + CHA₂DS₂-VASc/HAS-BLED; facilitador en CESFAM o domicilio; continuidad INR del paciente HD |
| `urn:salud:kb:hsc-pro-187-telediabetes` | PRO 187 (2024) | telediabetes UNITEL: ajuste de insulina/fármacos vía teleconsulta; exige declarar dependencia, red de apoyo y hospitalizaciones recientes; precedente de atención con facilitador a domicilio |
| `urn:salud:kb:hsc-pro-085-atencion-farmaceutica-programa-anticoagulantes` | PRO-085 (2022) | atención farmacéutica TACO (~650 px): inclusión por INR fuera de rango/adherencia/ERC, Morisky-Green, conciliación farmacéutica post-hospitalización y PRM; cierre del ciclo farmacológico del paciente HD anticoagulado |
| `urn:salud:kb:hsc-pro-170-plan-anual-prevencion-control-infecciones` | PRO-170 (2023, 3ª ed.) | programa anual IAAS obligatorio institucional: 9 actividades con umbrales (SICARS cuatrimestral, prevalencia, brotes/ARAISP, EPP, capacitación); rector de la prevención en HD |
| `urn:salud:kb:hsc-pro-099-acogida-informacion-visitas-acompanamiento` | PRO-099 (2023, 4ª ed.) | figuras de Familiar Responsable y Acompañante 12/24 h, circuito de información acreditado y horarios por servicio; anclaje institucional del rol del cuidador que HD traslada al domicilio |
| `urn:salud:kb:hsc-pro-043-ingreso-de-usuarios` | PRO-043 (2019, 3ª ed.) | proceso madre de ingreso HSC: vías, orden escrita, camas UGCC hábil/enfermería fuera de hora y egreso con epicrisis + devolución de ficha en 72 h |
| `urn:salud:kb:hsc-pro-046-pielonefritis-aguda` | PRO-046 (2013) | PNA en Urgencia/Medicina: ITU complicada y criterios de ingreso (SIRS/sepsis, complicación local, condiciones especiales); diagnóstico frecuente de egreso a HD |
| `urn:salud:kb:hsc-pro-048-pancreatitis-aguda` | PRO-048 (2013) | PA en UE/Medicina/Cirugía: definiciones, Ranson/APACHE/Balthazar y derivación a centro de referencia; perfil típico de egreso precoz con continuidad domiciliaria |
| `urn:salud:kb:hsc-arsenal-farmacoterapeutico-2026` | Arsenal Farmacoterapéutico HSC 2026 | repertorio; no es stock, guía terapéutica ni autorización HODOM |
| `urn:salud:kb:minsal-decreto-exento-74-2024-mcc` | Decreto Exento 74/2024 | marco modificatorio del modelo de cuidado (MCC) |

## 3. Ingreso, traslado y responsabilidad — H0

| URN | Documento | Uso |
|---|---|---|
| `urn:salud:kb:hsc-mo-ugdp-mov-002-organizacion-copia-observada` | MO U.G.D.P. y Mov. 002 | gestión centralizada de camas (copia observada) |
| `urn:salud:kb:hsc-pro-134-gestion-pacientes-recorte-hodom` | HSC 30.1 PRO-134 | gestión centralizada de pacientes (recorte HODOM) |
| `urn:salud:kb:hsc-aoc-2-1-derivacion-pacientes` | AOC 2.1 | sistema de derivación de pacientes |
| `urn:salud:kb:hsc-apt-1-2-transporte-pacientes-historico` | APT 1.2 | transporte de pacientes (histórico) |

Ninguna fuente define por sí sola el hito de cambio de responsabilidad: la
koraficación preserva qué dice cada propietario y mantiene visibles las
contradicciones.

## 4. Paciente, cuidador y domicilio — H0

| URN | Documento | Uso |
|---|---|---|
| `urn:salud:kb:minsal-contactabilidad-nucleo-operativo` | OT Contactabilidad de Usuarios | contacto y localización de usuarios |
| `urn:salud:kb:hsc-dp-2-1-consentimiento-informado` | DP 2.1 — Consentimiento Informado | contrato institucional; no equivale a aceptación del Cuidador |
| `urn:salud:kb:hsc-14-2-prestamo-catres-clinicos` | HSC 14.2 — Préstamo de Catres Clínicos | soporte material en domicilio |
| `urn:salud:kb:hsc-14-3-riesgo-biopsicosocial` | HSC 14.3 — Riesgo Biopsicosocial | atención integral de riesgo biopsicosocial |

Brecha documental declarada: no existe fuente vigente que defina
integralmente el contrato del Cuidador Responsable HODOM (ver §15).

## 5. Respuesta, rescate y continuidad — H0

| URN | Documento | Uso |
|---|---|---|
| `urn:salud:kb:hsc-aoc-1-1-emergencia-riesgo-vital` | AOC 1.1 | sistema de alerta y organización de emergencia vital |
| `urn:salud:kb:hsc-gcl-2-3-vigilancia-eventos-adversos` | GCL 2.3 | sistema de vigilancia de eventos adversos |
| `urn:salud:kb:hsc-gcl-2-2-prevencion-caidas-2023` | GCL 2.2 | prevención de caídas |
| `urn:salud:kb:hsc-pro-045-contingencia-unidad-emergencia-2013` | HSC 7.2 PRO-045 | plan de contingencia de Emergencia (2013; no doctrina vigente sin revisión) |

## 6. Identidad, plan y registro — H0

| URN | Documento | Uso |
|---|---|---|
| `urn:salud:kb:hsc-reg-1-1-ficha-clinica-unica` | REG 1.1 | manejo de ficha clínica única |
| `urn:salud:kb:hsc-reg-1-2-estandarizacion-registros-clinicos` | REG 1.2 | estandarización de registros clínicos |
| `urn:salud:kb:hsc-gcl-1-12-identificacion-pacientes` | GCL 1.12 | identificación de pacientes |
| `urn:salud:kb:minsal-nt-245-identificacion-pacientes` | NT 245 | norma técnica nacional de identificación (autoridad de GCL 1.12) |

## 7. Continuidad farmacológica — H1

| URN | Documento | Uso |
|---|---|---|
| `urn:salud:kb:hsc-17-2-estupefacientes-psicotropicos` | HSC 17.2 | estupefacientes y psicotrópicos |
| `urn:salud:kb:hsc-17-4-solicitud-medicamentos-uso-restringido` | HSC 17.4 | solicitud de medicamentos de uso restringido |
| `urn:salud:kb:hsc-apf-1-4-rotulacion-envasado-despacho` | APF 1.4 | rotulación, envasado y despacho |
| `urn:salud:kb:hsc-apf-1-5-almacenamiento-conservacion-2023` | APF 1.5 | almacenamiento y conservación de medicamentos |
| `urn:salud:kb:hsc-apf-1-5-almacenamiento-conservacion-insumos` | APF 1.5 (insumos) | devolución, almacenamiento y conservación de insumos |
| `urn:salud:kb:hsc-apf-1-5-formato-recetas-prescripcion` | APF 1.5 | formato de prescripción y recetas |
| `urn:salud:kb:hsc-apf-1-5-notificacion-reacciones-adversas-medicamentos` | APF 1.5 | notificación de reacciones adversas a medicamentos |
| `urn:salud:kb:hsc-apf-1-5-solicitud-devolucion-medicamentos` | APF 1.5 | solicitud y devolución de medicamentos |

Subarsenal HODOM, condiciones de transporte y cobertura por horario: no
existen en estas fuentes hasta que Farmacia las valide expresamente.

## 8. Muestras y resultados — H1

| URN | Documento | Uso |
|---|---|---|
| `urn:salud:kb:minsal-rpe-33-unidades-laboratorio` | RPE-33 | unidades de laboratorio |
| `urn:salud:kb:hsc-apl-1-2-toma-traslado-muestras-2025` | APL 1.2 | etapa preanalítica: toma y traslado de muestras |
| `urn:salud:kb:hsc-pro-090-almacenamiento-muestras-historico` | HSC 20.2 PRO-090 | almacenamiento de muestras (histórico) |
| `urn:salud:kb:hsc-pro-089-resultados-vih-historico` | HSC 20.1 PRO-089 | notificación de resultados confidenciales (histórico) |

## 9. IAAS, dispositivos y seguridad situada — H1

| URN | Documento | Uso |
|---|---|---|
| `urn:salud:kb:hsc-gcl-3-3-precauciones-estandar` | GCL 3.3 | precauciones estándar |
| `urn:salud:kb:hsc-gcl-3-3-prevencion-infecciones-torrente-sanguineo-2025` | GCL 3.3 | prevención de infección del torrente sanguíneo |
| `urn:salud:kb:hsc-gcl-3-3-prevencion-itu-cup-2024` | GCL 3.3 | prevención de infección asociada a CUP |
| `urn:salud:kb:hsc-24-8-aseo-desinfeccion` | HSC 24.8 | aseo y desinfección |
| `urn:salud:kb:hsc-pro-031-manejo-residuos-hospitalarios` | HSC 27.A.1 | manejo de residuos hospitalarios |
| `urn:salud:kb:hsc-gcl-1-2-vias-venosas-centrales-2025` | GCL 1.2 (CVC) | manejo de catéter venoso central |
| `urn:salud:kb:hsc-gcl-1-2-administracion-medicamentos-endovenosos-2024` | GCL 1.2 (EV) | administración de medicamentos endovenosos |

No se infiere aplicabilidad domiciliaria desde copias de Medicina, Urgencia o
UPC: el recorte HODOM lo fija la autoridad IAAS.

## 10. Entrega de turno — H1

| URN | Documento | Uso |
|---|---|---|
| `urn:salud:kb:hsc-aoc-2-2-entrega-turno-medico-medicina` | AOC 2.2 — Medicina, entrega médica | emisores, receptores y contenido de la entrega |
| `urn:salud:kb:hsc-aoc-2-2-entrega-turno-enfermeria-matroneria` | AOC 2.2 — Medicina, Enfermería/Matronería | idem |
| `urn:salud:kb:hsc-aoc-2-2-entrega-turno-medico-urgencia` | AOC 2.2 — Urgencia, entrega médica | idem |
| `urn:salud:kb:hsc-aoc-2-2-entrega-turno-enfermeria-urgencia` | AOC 2.2 — Urgencia, Enfermería | idem |

Corpus de contraste: una entrega documentada no demuestra por sí sola el
cambio efectivo de responsabilidad.

## 11. Modelos de organización — H2 (PF-01/PF-03)

| URN | Documento | Uso |
|---|---|---|
| `urn:salud:kb:hsc-mo-med-02-organizacion-servicio-clinico-medicina-2022` | Modelo de Medicina | ecosistema y red |
| `urn:salud:kb:hsc-mo-ue-organizacion-unidad-emergencia-adulta-pediatrica-2022` | Modelo de Emergencia | ecosistema y red |
| `urn:salud:kb:hsc-mo-uci-01-organizacion-unidad-cuidados-intensivos-2022` | Modelo UCI | ecosistema y red |
| `urn:salud:kb:hsc-mo-uti-3-organizacion-unidad-tratamiento-intermedio-2022` | Modelo UTI | ecosistema y red |
| `urn:salud:kb:hsc-mo-cae-02-organizacion-consultorio-adosado-especialidades-2022` | Modelo CAE | ecosistema y red |
| `urn:salud:kb:hsc-mo-2q-tele-organizacion-unidad-telemedicina-2023` | Modelo de Telemedicina | ecosistema y red |
| `urn:salud:kb:hsc-mo-reha-01-organizacion-servicio-rehabilitacion-2020` | Modelo de Rehabilitación | ecosistema y red |
| `urn:salud:kb:hsc-mo-psic-03-organizacion-seccion-psicosocial-2022` | Modelo Psicosocial | paciente, cuidador y experiencia |
| `urn:salud:kb:hsc-mo-farm-001-modelo-organizacion-farmacia-2023` | Modelo de Farmacia | recursos clínicos y logística |
| `urn:salud:kb:hsc-mo-lab-03-modelo-organizacion-laboratorio-2022` | Modelo de Laboratorio | recursos clínicos y logística |
| `urn:salud:kb:hsc-mo-imag-014-modelo-organizacion-imagenologia-2023` | Modelo de Imagenología | recursos clínicos y logística |
| `urn:salud:kb:hsc-mo-sa-est-002-modelo-organizacion-esterilizacion-2022` | Modelo de Esterilización | recursos clínicos y logística |
| `urn:salud:kb:hsc-mo-abast-01-organizacion-abastecimiento-2022` | Modelo de Abastecimiento | recursos clínicos y logística |

Los modelos describen organizaciones: no fijan por sí solos la función común,
la dotación vigente ni el valor al Paciente.

## 12. Gobierno, calidad, personas, equipos e instalaciones — H2 (PF-02/PF-04/PF-05)

| URN | Documento | Uso |
|---|---|---|
| `urn:salud:kb:hsc-1e-mg-cal-modelo-gestion-dcsp-2024` | Modelo DCSP | gobierno y administración |
| `urn:salud:kb:hsc-cdg-02-organizacion-unidad-control-gestion-2022` | Control de Gestión | gobierno y desempeño |
| `urn:salud:kb:hsc-mo-daiu-003-organizacion-atencion-integral-usuario-2022` | Atención Integral al Usuario | derechos y experiencia |
| `urn:salud:kb:hsc-mo-rrhh-01-organizacion-gestion-personas-2022` | Gestión de las Personas | capacidad y fuerza laboral |
| `urn:salud:kb:hsc-mo-cap-02-organizacion-capacitacion-desarrollo-2022` | Capacitación y Desarrollo | capacidad y fuerza laboral |
| `urn:salud:kb:hsc-mo-fin-044-organizacion-finanzas-2022` | Finanzas | gobierno y economía |
| `urn:salud:kb:hsc-mo-2p-dciye-organizacion-control-infecciones-epidemiologia-2024` | DCIYE | control de infecciones y epidemiología |
| `urn:salud:kb:hsc-rh-2-1-programa-induccion-2024` | Programa de inducción | formación |
| `urn:salud:kb:hsc-rh-3-1-programa-capacitacion-iaas-rcp-2023` | Programa de capacitación institucional | formación |
| `urn:salud:kb:hsc-dp-1-2-gestion-reclamos-2022` | Gestión de reclamos | derechos y calidad |
| `urn:salud:kb:hsc-dp-1-3-evaluacion-respeto-derechos-usuarios-2024` | Evaluación del respeto a los derechos | derechos y calidad |
| `urn:salud:kb:hsc-dp-5-1-presentacion-casos-comite-etica-asistencial-2024` | Comité de Ética Asistencial | ética |
| `urn:salud:kb:hsc-dp-3-1-solicitud-autorizacion-investigacion-seres-humanos-2024` | Autorización de estudios en seres humanos | ética e investigación |
| `urn:salud:kb:hsc-cal-1-1-politica-calidad-seguridad-paciente-2020` | Política de Calidad 2020 | calidad |
| `urn:salud:kb:hsc-cal-1-1-programa-calidad-seguridad-paciente-2025` | Programa de Calidad 2025 | calidad |
| `urn:salud:kb:hsc-rh-4-2-accidentes-sangre-fluidos-riesgo-2023` | Accidentes con sangre o fluidos de riesgo | seguridad del trabajador |
| `urn:salud:kb:hsc-eq-1-1-adquisicion-equipamiento-2024` | Adquisición de equipamiento | equipamiento |
| `urn:salud:kb:hsc-eq-1-2-seguimiento-vida-util-equipamiento-critico-2023` | Vida útil de equipamiento | equipamiento |
| `urn:salud:kb:hsc-eq-2-1-mantenimiento-preventivo-equipos-criticos-2024` | Mantenimiento preventivo de equipos | equipamiento |
| `urn:salud:kb:hsc-eq-3-1-perfil-operador-equipamiento-relevante-2024` | Perfil de operador | equipamiento |
| `urn:salud:kb:hsc-ins-1-1-plan-prevencion-incendios-2023` | Prevención de incendios | instalaciones |
| `urn:salud:kb:hsc-ins-2-1-plan-evacuacion-2023` | Evacuación | instalaciones |
| `urn:salud:kb:hsc-ins-3-1-mantenimiento-preventivo-instalaciones-2025` | Mantenimiento de instalaciones | instalaciones |
| `urn:salud:kb:hsc-ins-3-2-contingencia-agua-potable-estanques-2026` | Contingencia de agua potable | contingencias |
| `urn:salud:kb:hsc-ins-3-2-contingencia-energia-electrica-2022` | Contingencia de energía eléctrica | contingencias |

## 13. Información, documentos y ecosistema digital — H2 (PF-06)

| URN | Documento | Uso |
|---|---|---|
| `urn:salud:kb:hsc-pro-024-elaboracion-documentacion-gestion-documental-2023` | HSC 1.2 — Elaboración de Documentos | ciclo documental |
| `urn:salud:kb:hsc-42-1-procedimientos-registro-informacion-dig-2024` | HSC 42.1 — Registros DIG | registros e información |
| `urn:salud:kb:hsc-mo-tic-03-modelo-organizacion-tic-2022` | Modelo TIC | ecosistema digital |
| `urn:salud:kb:hsc-mo-dig-005-modelo-organizacion-dig-2023` | Modelo DIG | ecosistema digital |

Los contratos vivos de datos, integración y operación de `hd-hsc-os`/SGH/CLI
no viven en Drive ni en este índice: se resuelven en sus repos propietarios.

## 14. Fuentes nacionales y condicionadas — FN/FH/FC

| URN | Documento | Uso |
|---|---|---|
| `urn:salud:kb:minsal-nt-243-clasificacion-establecimientos-hospitalarios-2025` | NT 243 (2025) | seguridad del paciente y clasificación; contraste del sistema HSC de eventos adversos (FN-01) |
| `urn:salud:kb:minsal-orientaciones-planificacion-programacion-red-2025` | OT Planificación y Programación 2025 | programación anual (FN-02) |
| `urn:salud:kb:minsal-orientaciones-tecnicas-comges-2026` | OT COMGES 2026 | compromisos de gestión (FN-03) |
| `urn:salud:kb:minsal-rpe-9-telemedicina` | RPE-9 — Telemedicina | soporte asistencial remoto (FN-04) |
| `urn:salud:kb:minsal-rpe-14-rehabilitacion` | RPE-14 — Rehabilitación | trayectoria y cartera (FN-05) |
| `urn:salud:kb:minsal-rpe-25-cuidados-paliativos-universales` | RPE-25 — Cuidados Paliativos | cartera o trayectoria paliativa (FN-06) |
| `urn:salud:kb:minsal-rpe-27-imagenologia` | RPE-27 — Imagenología | interfaz de Imagenología (FN-07) |
| `urn:salud:kb:superintendencia-salud-compendio-beneficios-2026` | Compendio de beneficios 2026 | cobertura financiera (FN-08) |
| `urn:salud:kb:minsal-plan-campana-invierno-2025` | Plan Ministerial de Invierno 2025 | contraste estacional; nunca regla permanente (FH-01) |
| `urn:salud:kb:minsal-instructivo-pauta-autorizacion-sanitaria-hodom-2024` | Instructivo/pauta de autorización sanitaria HODOM | expediente de autorización sanitaria |
| `urn:salud:kb:minsal-pauta-chequeo-nt-247-trazabilidad-dispositivos-medicos` | Pauta de chequeo NT 247 | trazabilidad de dispositivos médicos |
| `urn:salud:kb:minsal-rem-2026` | REM 2026 | definiciones REM e indicadores |

## 15. Brechas de adquisición (no koraficadas)

Fuentes autoritativas necesarias antes de modelar; **no se inventan por
inferencia documental**:

- Contrato vigente del Cuidador Responsable HODOM (designación,
  voluntariedad, tareas, límites, relevo y retiro). PRO 002, PRO-110, la OT de
  contactabilidad y DP 2.1 aportan hechos parciales y no deben fusionarse.
- Cobertura territorial y red: acuerdos con APS, receptores, rutas y
  transporte.
- Capacidad y fuerza laboral: dotación aprobada, competencias, turnos y
  cobertura real por franja.
- Operación HODOM: contratos estables de programación, despacho, inventario,
  cadena de frío y logística inversa.
- Datos e interoperabilidad: diccionarios, linaje y contratos SGH/CLI/`hd-hsc-os`.
- Desempeño: fichas de indicadores con propósito, numerador, denominador y
  procedencia.
- Software: contratos vivos de dominio, requisito, prueba, release y operación.

### Brechas de koraficación PRO en unidades de interfaz HODOM (recenso vivo 2026-08-23)

Re-recenso completo de la biblioteca Drive (906 carpetas, 1396 archivos,
comparación por Drive ID contra el censo 2026-07-20): **cero altas, cero
bajas** — la fuente viva no cambió desde el corte de julio. La brecha no es de
drift sino de cobertura: la familia **PRO** (protocolos de unidad) tiene ~9%
de cobertura en el ámbito HD. Candidatura curada Tier A (interfaz operativa
directa), pendiente de gates de lectura íntegra por fuente:

- Medicina: ~~PRO-046/PRO-048~~ **koraficadas 2026-08-23** (`urn:salud:kb:hsc-pro-046-pielonefritis-aguda`, `urn:salud:kb:hsc-pro-048-pancreatitis-aguda`). ~~PRO-053~~ **koraficada 2026-08-23** (`urn:salud:kb:hsc-pro-053-hospitalizacion-desde-unidad-emergencia`).
- Farmacia: ~~PRO-085 anticoagulantes~~ **koraficada 2026-08-23**
  (`urn:salud:kb:hsc-pro-085-atencion-farmaceutica-programa-anticoagulantes`);
  ~~PRO-091~~ **koraficada 2026-08-23** (`urn:salud:kb:hsc-pro-091-gestion-eliminacion-medicamentos-vencidos`).
- DCIYE: ~~PRO-23 manejo de brotes~~ **koraficada 2026-08-23**
  (`urn:salud:kb:hsc-pro-023-manejo-brotes-iaas`); ~~PRO-170 plan anual de
  prevención y control de infecciones~~ **koraficada 2026-08-23**
  (`urn:salud:kb:hsc-pro-170-plan-anual-prevencion-control-infecciones`).
- Rehabilitación: ~~PRO-126 rehabilitación pulmonar~~ **koraficada 2026-08-23**
  (`urn:salud:kb:hsc-pro-126-rehabilitacion-pulmonar`); queda PRO-152 crítico VMI
  (kinesioterapia domiciliaria).
- UGCC: ~~PRO-076 carga de combustible de ambulancias~~ **koraficada 2026-08-23** (`urn:salud:kb:hsc-pro-076-carga-combustible-ambulancias`) — insumo decisión #10.
- DAIU: ~~PRO-099 visitas y acompañamiento~~ **koraficada 2026-08-23**
  (`urn:salud:kb:hsc-pro-099-acogida-informacion-visitas-acompanamiento`);
  ~~PRO-043 ingreso de usuarios~~ **koraficada 2026-08-23**
  (`urn:salud:kb:hsc-pro-043-ingreso-de-usuarios`); queda PRO-156 atención
  preferente PM/PCD.
  PRO-187 telediabetes~~ **koraficadas 2026-08-23**
  (`urn:salud:kb:hsc-pro-186-teletaco-anticoagulante-oral`,
  `urn:salud:kb:hsc-pro-187-telediabetes`); queda PRO-185 telegastro.


## 16. Límites del índice

- No es un censo de Drive ni un inventario curatorial: eso vive en hd-dt
  (`censo-gestion-documental-hsc-2026-07-20.md`,
  `inventario-gestion-documental-hsc.md`).
- No autoriza compras, pilotos, traslados ni actos clínicos.
- No declara vigencia por título: la autoridad se resuelve con D-025BN y la
  lectura de cada fuente.
- Un artefacto aquí citado puede deprecarse o retirarse; su URN sigue
  resolviendo (dignidad del URN).
