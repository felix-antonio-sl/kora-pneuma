---
urn: urn:salud:kb:notificacion-eno-iaas
nombre: notificacion-eno-iaas
version: 1.0.0
estado: publicado
descripcion: "Marco operativo de notificacion epidemiologica obligatoria en Chile: ENO (Decreto 7/2019, plataforma EPIVIGILA) e IAAS (Decreto Exento 60/2022 = Norma Tecnica 225, plataforma SICARS) — modalidades, plazos, lista, definiciones de caso, criterios de brote y campos de notificacion."
fuente: "Sintesis de fuentes OFICIALES (web, 2026-06-22) para anclar la skill vigilancia-epidemiologica; no es koraficacion de un solo documento sino sintesis multi-fuente con citacion (patron conocimiento-web). Fuentes primarias: Decreto 7/2019 reglamento ENO (BCN/LeyChile idNorma=1141549, no derogado; deroga DS 158/2004; publicado 2020), confirmado en FAOLEX chi206424; Decreto Exento 60/2022 que aprueba la Norma Tecnica 225 de IAAS (BCN idNorma=1181226, no derogado; deroga NT 124). Fuentes operativas: guia MINSAL ANEXO-04-2022, circulares C37 N08/N09 2021 y C37 N02 2023, plataformas EPIVIGILA y SICARS. Caveat de acceso: epi.minsal.cl (definiciones de caso por enfermedad e instructivo EPIVIGILA) y las circulares C37 (PDF escaneados) NO fueron accesibles en fuente primaria (Cloudflare/WAF); su contenido se confirmo via documentos oficiales equivalentes (GCL 3.2 6a ed., informes MINSAL). Los detalles por evento deben verificarse en la circular/NT especifica antes de uso normativo estricto."
autor: FS
creado: 2026-06-22
lang: es
tags: [salud, vigilancia-epidemiologica, notificacion-obligatoria, eno, iaas, epivigila, decreto-7-2019, norma-tecnica-225, sicars]
familia: nota
---

# Notificación epidemiológica obligatoria en Chile — ENO e IAAS

## Cadena normativa vigente (junio 2026)

Código Sanitario (DFL 725/1968) → **Decreto 7/2019** (Reglamento sobre Notificación
de Enfermedades Transmisibles de Declaración Obligatoria y su Vigilancia; deroga el
DS 158/2004; publicado 2020) → plataforma **EPIVIGILA** + Normas Técnicas/circulares
por enfermedad. Para IAAS: **Decreto Exento N° 60/2022** = aprueba la **Norma Técnica
N° 225** (deroga la NT 124/DS 350-2011) → circulares **C37 N°08 y N°09 (2021)**, **C37
N°02 (2023)** → plataforma **SICARS**.

> **Corrección de identidad** (error frecuente): lo citado coloquialmente como "RE
> 60/2022" es el **Decreto N° 60 EXENTO de 2022** (aprueba la NT 225 de IAAS), NO una
> resolución del régimen ENO. El reglamento ENO vigente es el **Decreto 7/2019**.

## ENO — cuatro modalidades, plazos y lista (Decreto 7/2019, Art. 1)

| Modalidad | Plazo / vía | Eventos |
|---|---|---|
| **a) Inmediata** | comunicación inmediata por la vía más expedita a la SEREMI ante **sospecha**; SEREMI avisa de inmediato al MINSAL; formalización en EPIVIGILA **≤ 24 h** (Art. 4) | Botulismo, Carbunco, Chagas aguda, Chikungunya, Cólera, Dengue, Difteria, Fiebre amarilla, Hantavirus, *H. influenzae* invasor, IRA grave inusitada, Leptospirosis, Malaria, Meningitis bacterianas, *N. meningitidis* invasor, fiebres hemorrágicas virales (Ébola/Marburg/Lassa), Peste, Parálisis flácida aguda (Polio), Rabia, Rubéola, Sarampión, Sd. rubéola congénita, Triquinosis, Virus Nilo Occidental, Zika |
| **b) Dentro de 24 h** | **≤ 24 h** desde confirmación/clasificación final; SEREMI reporta diariamente al MINSAL | Brucelosis, Chagas crónica, Cisticercosis, Creutzfeldt-Jakob, Coqueluche, Fiebre tifoidea/paratifoidea, Fiebre Q, Hepatitis virales (A,B,C,E), Hidatidosis, Gonorrea, Leishmaniasis, Lepra, Listeriosis, Parotiditis, Psitacosis, Rickettsiosis, Sífilis, Sd. hemolítico urémico, *S. pneumoniae* invasor, Tétanos, Tuberculosis, VIH |
| **c) Centinela** | **semanal**, solo establecimientos definidos centinela por la SEREMI | Diarrea aguda en <5 años; Influenza/IRA virales; VPH; Varicela |
| **d) Otros eventos inmediatos** | **inmediata** | **Brotes de cualquier etiología transmisible (incluye ETA y brotes de IAAS)**; enfermedad/brote de causa desconocida de presunto origen infeccioso; muertes por presunta causa infecciosa no identificada; sospecha de contaminación intrínseca de fármacos/insumos; sospecha de enfermedad erradicada (Viruela, Polio) |

**Vigilancia de laboratorio** (Art. 5): los laboratorios envían **semanalmente** cepa/muestra al ISP (lista de ~33 agentes); un laboratorio que detecta agente ENO comunica **el mismo día** a la SEREMI / Delegado de Epidemiología.

## EPIVIGILA — la plataforma

Sistema informático nacional de notificación (`epivigila.minsal.cl`), en producción nacional desde marzo 2020; ingresa casos sospechosos y confirmados. El Art. 4 del Decreto 7 no enumera campos: remite a la Norma Técnica y a los formularios electrónicos en EPIVIGILA.

## Definiciones de caso — dónde viven

El Decreto 7/2019 **NO define transversalmente** sospechoso/probable/confirmado: remite a *"las definiciones establecidas en la Norma Técnica respectiva para cada enfermedad"* (Art. 1.b). Por tanto las definiciones de caso viven en las **circulares y normas técnicas por enfermedad** del Departamento de Epidemiología MINSAL, no en el reglamento.

Ejemplo verificado (Sarampión, circular B51/27): caso **sospechoso** = cuadro exantemático + un segundo criterio (fiebre, conjuntivitis, artralgia o linfoadenopatías); caso **altamente probable** = sospechoso con criterio clínico compatible o nexo epidemiológico; notificación inmediata + EPIVIGILA ≤ 24 h, investigación y control ≤ 48 h.

## Criterios de brote (guía MINSAL ANEXO-04-2022)

Brote = *"la ocurrencia de toda agrupación de casos de enfermedad infecciosa relacionados en el tiempo y en el espacio"*. **Todos los brotes se notifican de forma inmediata** (Decreto 7, Art. 1.d) — incluye ETA y brotes de IAAS.

## IAAS — Decreto Exento 60/2022 / Norma Técnica 225

La NT 225 organiza el Programa de Control de IAAS (PCI), su dotación, la **vigilancia epidemiológica activa y selectiva** como función institucional, prevención, y el estudio/manejo de brotes. El **decreto no enumera** en su texto las IAAS notificables ni los plazos a MINSAL: eso lo fijan las circulares C37.

- **IAAS bajo vigilancia/notificación** (indicadores definidos por MINSAL; detalle en circulares C37): infección torrente sanguíneo asociada a CVC (ITS/CVC); ITS asociada a catéter de hemodiálisis; ITU asociada a catéter urinario permanente (ITU/CUP); infección de herida operatoria en cirugías trazadoras (colecistectomía, hernia, cesárea); endometritis puerperal; neumonía/IRA viral baja asociada; síndrome diarreico en lactantes/neonatos; diarrea por *C. difficile*; SARS-CoV-2 nosocomial. Vigilancia **activa** por enfermera de PCI con criterios diagnósticos estandarizados.
- **Plataforma y plazo**: reporte **mensual** al sistema nacional **SICARS** (~180 hospitales). Roles: registrador = enfermera PCI; validador = médico PCI (dentro de los primeros 15 días del mes siguiente); autorizador = director. Tasas mensuales por indicador.
- **Criterio de brote IAAS** (NT 225, indicativo): nº de casos sobre ~el doble de lo observado/esperado, acúmulos en tiempo/servicio, o aislamiento de patógenos específicos/resistentes.
- **Conexión con ENO**: los **brotes de IAAS escalan a notificación inmediata vía EPIVIGILA** (Decreto 7, Art. 1.d) — además del reporte SICARS mensual.

## Campos del formulario de notificación (EPIVIGILA — grupos)

Estructura indicativa (el set exacto por ENO lo fija cada Norma Técnica/circular; ver caveat):

1. **Establecimiento / Servicio de Salud** notificador.
2. **Paciente**: nombre, RUN, ficha clínica, domicilio, teléfono, edad, sexo (y nacionalidad/previsión en EPIVIGILA).
3. **Evento/diagnóstico**: enfermedad ENO, clasificación del caso (sospechoso/confirmado), fecha de inicio de síntomas, fecha de notificación/diagnóstico.
4. **Antecedentes clínicos y epidemiológicos**: lugar probable de contagio, antecedente de vacunación, nexo epidemiológico, viaje.
5. **Laboratorio**: exámenes practicados / confirmación.
6. **Notificador**: profesional, RUT, firma.

## Caveats de verificación (no confirmado en fuente primaria — no inventar)

- El **texto íntegro de las circulares C37 N°09/2021 y C37 N°02/2023** (lista exacta y umbrales anuales de IAAS notificables) son PDF escaneados; tomados de documento hospitalario oficial (GCL 3.2) que las cita.
- El **set exacto y completo de campos del formulario EPIVIGILA por cada ENO** vive en el instructivo de epi.minsal.cl (no accesible); la estructura de arriba es indicativa.
- Las **definiciones de caso por enfermedad** son por circular individual (verificado Sarampión como ejemplo).
- El **detalle ampliado de la NT 225** (anexos de indicadores) puede ser más extenso en la versión PDF de minsal.cl.

## Fuentes oficiales

- Decreto 7/2019 (reglamento ENO): BCN/LeyChile idNorma=1141549 — https://www.bcn.cl/leychile/navegar?idNorma=1141549 ; FAOLEX chi206424.
- Decreto Exento 60/2022 (NT 225 IAAS): BCN/LeyChile idNorma=1181226 — https://www.bcn.cl/leychile/navegar?idNorma=1181226.
- Guía MINSAL ANEXO-04-2022 — https://www.minsal.cl/wp-content/uploads/2021/09/ANEXO-04-2022.pdf
- EPIVIGILA — https://epivigila.minsal.cl ; Departamento de Epidemiología — http://epi.minsal.cl
- Vigilancia IAAS (definiciones MINSAL reproducidas): GCL 3.2 6ª ed. (2023) — https://www.hospitalsanfranciscodepucon.cl/wp-content/uploads/2023/04/GCL-3.2-SISTEMA-DE-VIGILANCIA-DE-IAAS-6.pdf
