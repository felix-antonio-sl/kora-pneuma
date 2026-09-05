---
urn: urn:salud:kb:hsc-cartera-servicios-2024
nombre: hsc-cartera-servicios-2024
version: 1.0.0
estado: publicado
descripcion: "Cartera de Servicios del Hospital de San Carlos 2024: corpus tabular institucional de 13 hojas y 13 campos, con prestaciones asistenciales, códigos, estado declarado, área de influencia, compra de servicios y observaciones."
fuente: "Resolución Exenta N° 1206/2024, Cartera HSC, archivo XLSX primario /home/felix/projects/hd-dt/01-normativo/hsc/res-exenta-1206-2024-cartera-hsc.xlsx, sha256:ae07668d54a60020cf2994b561dca2c8669fbe6f7a5df000d9c68d23d46ac36a; extracción textual completa /home/felix/projects/hd-dt/02-cartera-y-prestaciones/cartera-servicios-hsc-2024.txt, sha256:5bf6e47168cfe8b1a87658f6f9361d535b4396c2fe7228f15060c4396bdd81f6; el XLSX conserva autoridad primaria y el TXT conserva el corpus tabular normalizado."
autor: Codex
creado: 2026-08-02
lang: es
tags: [hospital-san-carlos, cartera-de-servicios, prestaciones, hsc, hodom, fuente-institucional]
familia: fuente
cita: [urn:salud:kb:hsc-pro-002-hospitalizacion-domiciliaria, urn:salud:kb:hodom-decreto-exento-31-2024]
---

# Cartera de Servicios HSC 2024

## Identidad, estructura y límite probatorio

La fuente es una cartera institucional del Hospital de San Carlos Dr. Benicio
Arzola Medina fechada en 2024. El archivo primario es un libro XLSX con 13
hojas; la extracción TXT conserva 13 campos por fila y todo el orden textual
observado.

La superficie cuantificada en vivo es:

- 13 hojas XLSX;
- 2112 filas no vacías de prestaciones en el XLSX;
- 2125 líneas en la extracción TXT;
- 13 cabeceras en total (una inicial y 12 repetidas) y 2112 filas no cabecera en el TXT;
- 13 campos tabulares por fila.

La cifra de 2124 filas después de la primera cabecera no
equivale por sí sola a prestaciones: incluye 12
cabeceras repetidas de las hojas posteriores. El conteo de prestaciones no
cabecera que reproduce la estructura del XLSX es 2112.

La extracción TXT es una representación textual normalizada, no una copia
byte a byte del XLSX. El XLSX permanece como fuente primaria para formato de
celda, tipos y valores; el TXT se conserva para lectura, búsqueda y revisión
fila por fila. No se usa como autoridad el resumen externo
cartera-prestaciones-hsc-2024.md.

La cartera describe un inventario fechado. No demuestra por sí sola
disponibilidad actual, autorización sanitaria, dotación, agenda, capacidad,
volumen, tiempos de respuesta, contratación vigente ni cumplimiento operativo.

## Distribución por hoja primaria

| Hoja del XLSX | Filas de prestaciones |
|---|---:|
| Endoscopia | 34 |
| Imagenología | 134 |
| Laboratorio | 420 |
| Dental | 118 |
| Psicosocial | 15 |
| U. Emergenca | 126 |
| CAE y Telemedicina  | 246 |
| UCI UTI | 52 |
| SC Medicina,Cirugía y Traumato | 133 |
| Obst. y Gine | 43 |
| Pediatría | 18 |
| UHCIP | 31 |
| Quirurgico | 742 |

## Esquema de la fuente

| # | Campo de la fuente |
|---:|---|
| 1 | USUARIO |
| 2 | MACROPROCESO |
| 3 | PROCESO (UNIDAD O SERVICIO) |
| 4 | SUBPROCESO (TIPO DE PRESTACIÓN) |
| 5 | ESTAMENTO O ESPECIALIDAD |
| 6 | PRESTACIÓN |
| 7 | CÓDIGO MAI |
| 8 | PRESTACIÓN EPH |
| 9 | PRESTACIÓN ACTUAL |
| 10 | PRESTACIÓN NUEVA |
| 11 | ÁREA DE INFLUENCIA |
| 12 | COMPRA DE SERVICIO |
| 13 | OBSERVACIONES |

## Relación observable con HODOM

La extracción contiene cinco filas cuyo nombre de prestación incluye la
expresión Visita a domicilio:

~~~text
Línea 873: prestación=Visita a domicilio por médico; código MAI=s/c; proceso=CAE; subproceso=Consulta o control Médico de Especialidad; área=Hospital; compra=NO
Línea 874: prestación=Visita a domicilio por enfermera; código MAI=0104004; proceso=CAE; subproceso=Consulta o control por Profesional no Médico; área=Hospital; compra=NO
Línea 875: prestación=Visita a domicilio por Auxiliar de enfermería; código MAI=0104003; proceso=CAE; subproceso=Consulta o control por Profesional no Médico; área=Hospital; compra=NO
Línea 2121: prestación=Visita a domicilio por enfermera; código MAI=0104004; proceso=PREQUIRURGICO BOX; subproceso=PROCEDIMIENTO DE ENFERMERIA; área=HOSPITAL DE SAN CARLOS (SSÑ); compra=NO
Línea 2122: prestación=Visita a domicilio por auxiliar de enfermería; código MAI=0104003; proceso=PREQUIRURGICO BOX; subproceso=PROCEDIMIENTO DE ENFERMERIA; área=HOSPITAL DE SAN CARLOS (SSÑ); compra=NO
~~~

Estas cinco filas representan prestaciones de visita domiciliaria ubicadas en
CAE y en el proceso prequirúrgico. En la extracción no aparece una fila cuyo
nombre contenga Hospitalización Domiciliaria. Por tanto, esta cartera aporta
interfaces y prestaciones domiciliarias puntuales, pero no acredita por sí sola
una cartera HODOM, el código de día-cama HODOM, un equipo HODOM, autorización,
criterios de ingreso o continuidad de hospitalización domiciliaria. Esas
afirmaciones deben resolverse con las fuentes HODOM y los actos vigentes.

## Uso correcto en KORA

- Tratar la cartera como fuente institucional fechada, no como estado actual.
- Mantener los códigos, mayúsculas, abreviaturas, valores vacíos y observaciones
  tal como aparecen en el corpus; no corregir silenciosamente errores
  ortográficos o diferencias de formato.
- Para cualquier prestación concreta, citar la fila y el campo de origen.
- Separar la existencia documental de una prestación de su disponibilidad,
  autorización, compra de servicio o ejecución efectiva.
- Derivar una vista HODOM solamente mediante una decisión explícita y trazable;
  este artefacto conserva primero la cartera completa.

## Corpus tabular íntegro

La siguiente sección conserva la extracción TXT completa, incluyendo las
cabeceras repetidas que delimitan las 13 hojas. Cada fila mantiene sus 13 campos y separadores como una secuencia visible formada por barra invertida y la letra t,
que representa un tabulador y conserva los
campos vacíos finales sin depender de espacios al final de línea.

~~~tsv
USUARIO \tMACROPROCESO\tPROCESO (UNIDAD O SERVICIO)\tSUBPROCESO (TIPO DE PRESTACIÓN)\tESTAMENTO O ESPECIALIDAD\tPRESTACIÓN\tCÓDIGO MAI\tPRESTACIÓN EPH\tPRESTACIÓN ACTUAL\tPRESTACIÓN NUEVA\tÁREA DE INFLUENCIA\tCOMPRA DE SERVICIO\tOBSERVACIONES
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tVárices esofágicos, ligadura directa\t17 04 063\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tPrótesis o tubo endoesofágico, colocación de (proc. aut.)\t17 04 059\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tEsofagoscopia\t18 01 002\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tDilatación de estenosis benignas o malignas del tracto digestivo por balón\t18 01 025\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tHemostasia con endoclips\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tConsulta o control Médico de Especialidad\tGastroenterología Adulto \tConsulta Médica de Especialidad en Gastroenterología \t\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tConsulta o control Médico de Especialidad\tMedicina General \tConsulta Médica de Especialidad en Medicina General \t\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tConsulta o control Médico de Especialidad\tAnestesiología \tConsulta Médica de Especialidad en Anestesiología \t\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tGastroduodenoscopía (incluye esofagoscopía)\t18 01 001\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tGastrostomia Endoscopica percutánea (PEG)\t18 02 014\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tInstalación endoscópica de sonda nasogástrica\t18 01 023\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tInstalación endoscópica de sonda enteral\t18 01 024\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tCuerpo extraño de esófago y/o estómago, extracción endoscópica (incluye la endoscopia)\t18 01 028\tEPH\tactual\t\tHospital\tSI\tSe estima inicio de atenciones consultas nuevas a partir de diciembre 2023
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tPolipectomía o Mucosectomía endoscópica alta\t18 01 031\tEPH\tactual\t\tHospital\tSI\tSe estima inicio en Noviembre 2023
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tInyectoterapia hemostática, Hemostasia mecánica, Hemostasia térmica, Ligadura elástica\t18 01 033\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tInstalación Sonda Naso Yeyunal\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tAno-recto-sigmoidoscopia en adultos\t18 01 004\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tColonoscopía larga (incluye sigmoidoscopía y colonoscopía izquierda)\t18 01 006\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tSigmoidoscopía y colonoscopía izquierda con tubo flexible (incluye ano-recto-sigmoidoscopía)\t18 01 007\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tPolipectomía o Mucosectomía endoscópica baja\t18 01 045\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tExtracción cuerpo extraño por vía anal\t18 03 007\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tUreasa, test de (para Helicobacter pylori) o similar\t18 01 037\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tEsofagoscopia\t18 01 002\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tColangiopancreatografía retrógrada c/s papilotomía\t18 01 018\tEPH\t\tNueva \tHospital\tSI\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tDrenaje de la vía biliar transhepática y/o percutáneo \t18 01 019\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tIntubación sonda de Sengstaken\t18 01 022\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tDilatación de estenosis benignas o malignas del tracto digestivo por balón\t18 01 025\tEPH\t\tNueva \tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tDevolvulación de colon por colonoscopía\t18 01 029\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tInyectoterapia hemostática, Hemostasia mecánica, Hemostasia térmica, Ligadura elástica\t18 01 033\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tDilatación de acalasia\t18 01 056\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tProcedimientos endoscópicos \tMédico \tInstalación de prótesis autoexpandibles en tracto digestivo\t18 01 057\tEPH\t\tNueva \tHospital\tSI\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tMisceláneo\tEnfermera\tHemoglucotest\t03 02 047\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tMisceláneo\tEnfermera\tToma de muestra venosa en adulto\t03 07 011\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tEndoscopía \tMisceláneo\tEnfermera\tToma de muestra arterial en adultos\t03 07 009\tEPH\tactual\t\tHospital\tNO\t
USUARIO \tMACROPROCESO\tPROCESO (UNIDAD O SERVICIO)\tSUBPROCESO (TIPO DE PRESTACIÓN)\tESTAMENTO O ESPECIALIDAD\tPRESTACIÓN\tCÓDIGO MAI\tPRESTACIÓN EPH\tPRESTACIÓN ACTUAL\tPRESTACIÓN NUEVA\tÁREA DE INFLUENCIA\tCOMPRA DE SERVICIO\tOBSERVACIONES
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de tórax  frontal o lateral con equipo móvil fuera del departamento de rayos.\t04 01 008\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de las glándulas salivales "sialografía"\t04 01 001\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de partes blandas, laringe lateral, cavum rinofaríngeo (rinofarinx). \t04 01 002\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de tórax, proyección complementaria (oblicuas, selectivas u otras)\t04 01 004\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tEstudio radiológico de corazón (incluye fluoroscopía, telerradiografías frontal y lateral con esofagograma) \t04 01 006\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de tórax simple frontal o lateral \t04 01 009\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de tórax frontal y lateral\t04 01 070\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tMamografía bilateral\t04 01 010\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tMamografía unilateral\t04 01 110\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tMamografía proyección complementaria  (axilar u otras)\t04 01 130\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de Abdomen Simple\t04 01 013\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de abdomen simple, proyección complementaria (lateral y/o oblicua)\t04 01 014\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tColangiografía intra o postoperatoria (por sonda T, o similar)\t04 01 015\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tEnema baritado del colon (incluye llene y control post-vaciamiento)\t04 01 018\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tEnema baritado del colon o intestino delgado, doble contraste\t04 01 019\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tEstudio radiológico de deglución faríngea\t04 01 022\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tEstudio radiológico del intestino delgado\t04 01 023\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de esófago, estómago y duodeno, simple en niños \t04 01 024\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía renal simple (proc. aut.)\t04 01 028\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía vesical simple o perivesical (proc. aut.)\t04 01 029\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía agujeros ópticos, ambos lados\t04 01 030\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de cavidades perinasales, órbitas, articulaciones temporomandibulares, huesos propios de la nariz, malar, maxilar, arco cigomático y cara\t04 01 031\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de cráneo frontal y lateral\t04 01 032\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de Cráneo  proyección especial de  base de cráneo (Towne)\t04 01 033\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de globo ocular, estudio de cuerpo extraño\t04 01 034\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de oído, uno o ambos\t04 01 035\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de silla turca frontal y lateral\t04 01 040\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de columna cervical o atlas-axis (frontal y lateral)\t04 01 042\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de columna cervical (frontal, lateral y oblicuas)\t04 01 043\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de columna cervical  flexión y  extensión (Dinámicas)\t04 01 044\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de columna dorsal o dorsolumbar localizada, parrilla costal adultos (frontal y lateral).\t04 01 045\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía columna lumbar o lumbosacra ( frontal, lateral y focalizada en el 5° espacio)   \t04 01 046\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía columna lumbar o lumbosacra  flexión y  extensión (Dinámicas)\t04 01 047\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía columna lumbar o lumbosacra, oblicuas adicionales \t04 01 048\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de columna total, panorámica con folio graduado  frontal o lateral\t04 01 049\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de pelvis, cadera o coxofemoral\t04 01 051\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de pelvis, cadera o coxofemoral de RN, lactante o niño menor de 6 años.\t04 01 151\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de pelvis, cadera o coxofemoral, proyecciones especiales; (rotación interna, abducción, lateral, Lawenstein u otras)\t04 01 052\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de Sacrocoxis o articulaciones sacroilíacas.\t04 01 053\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de brazo, antebrazo, codo, muñeca, mano, dedos, pie  (frontal y lateral)\t04 01 054\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de clavícula.\t04 01 055\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía Edad Ósea: carpo y mano \t04 01 056\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía Edad ósea : rodilla frontal\t04 01 057\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tEstudio radiológico de escafoides\t04 01 058\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tEstudio radiológico de muñeca o tobillo frontal lateral y oblicuas\t04 01 059\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de hombro, fémur, rodilla, pierna, costilla o esternón Frontal y Lateral\t04 01 060\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de Proyecciones especiales oblicuas u otras en hombro, brazo, codo, rodilla, rótulas, sesamoideos, axial de ambas rótulas o similares\t04 01 062\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de túnel intercondíleo o radio-carpiano\t04 01 063\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tApoyo fluoroscópico a procedimientos intraoperatorios y/o biopsia (no incluye el proc.)\t04 01 064\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tMamografía bilateral digital 3D con tomosíntesis\t04 01 071\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tMamografía unilateral digital 3D con tomosíntesis\t04 01 072\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tVideofluoroscopia para estudio de deglución\t04 01 073\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTránsito colónico con marcadores\t04 01 074\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tRadiografía de pelvis, cadera o coxofemoral de 1er screening  (entre 3 -6 meses)\t50 99 115\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tVía lagrimal (un lado) (2 exp.)\t04 02 001\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tGalactografía, unilateral\t04 02 005\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tInstalación de catéter o sonda intracardíaca, control por radiólogo\t04 02 032\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tCavografía\t04 02 035\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tFlebografía extremidad inferior o superior, un lado cada extremidad.\t04 02 038\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tFlebografía orbitaria o yugular\t04 02 040\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tFlebografía selectiva (suprarrenal y similares)\t04 02 041\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tMielografía por punción lumbar con contraste hidrosoluble\t04 02 050\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tConsulta Médica otras Especialidades\t01 01 300\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada de cráneo encefálica\t04 0 3001\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada de hipotálamo-hipófisis\t04 03 002\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada de fosa posterior\t04 03 003\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada de temporal-oído \t04 03 006\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada de órbitas maxilofacial \t04 03 007\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada de columna cervical \t04 03 008\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada de Columna Dorsal. Incluye mínimo 6 espacios \t04 03 018\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada de Columna Lumbar \t04 03 019\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada de cuello, partes blandas \t04 03 012\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada de Tórax. Incluye además: Esternón, Clavículas, Articulación Acromioclavicular, Escápula, Costillas, Articulación Esternoclavicular. Incluye todo el Tórax o cada segmento o articulación. Incluye bilateralidad\t04 03 013\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada de abdomen (hígado, vías y vesícula biliar, páncreas, bazo, suprarrenales y riñones)\t04 03 014\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada de Pelvis (Además incluye Sacro, Coxis, Caderas, Huesos Pélvicos, Articulaciones Sacro Ilíacas). Bilateral\t04 03 016\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada de Abdomen y Pelvis\t04 03 020\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada Pielografía\t04 03 021\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada Urografía\t04 03 022\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada de Colonoscopía Virtual. No incluye instalación de sonda\t04 03 023\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada Planificación Radioterapia\t04 03 024\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada de Calcio Coronario\t04 03 025\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada Angio de Cuello\t04 03 104\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada Angio de Pelvis\t04 03 105\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada de Angio Cardíaco. Mínimo 64 cortes\t04 03 106\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada Musculoesquelética por zona anatómica. Por cada segmento o articulación: muslo, pierna, rodillas, antebrazo, codo, muñeca, mano, hombro, pie, tobillo u otros. Bilateral sólo para rodillas\t04 03 017\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada angio  de encéfalo\t04 03 101\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada angio de tórax\t04 03 102\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía Computarizada angio de abdomen\t04 03 103\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía computarizada angio de extremidades inferiores (bilateral)\t04 03 107\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía computarizada angio de extremidad superior (unilateral)\t04 03 108\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tTecnología Médica\tTomografía computarizada de enterografía \t04 03 026\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tEcografía obstétrica\t04 04 002\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tEcografía abdominal (incluye hígado, vía biliar, vesícula, páncreas, riñones, bazo, retroperitoneo y grandes vasos)\t04 04 003\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tEcografía como apoyo a cirugía, o a procedimiento (de tórax, muscular, partes blandas, etc.)\t04 04 004\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tEcografía transvaginal o transrectal\t04 04 005\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tEcografía ginecológica, pelviana femenina u obstétrica con estudio fetal\t04 04 006\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tEcografía transvaginal para seguimiento de ovulación, procedimiento completo (6-8 sesiones )\t04 04 007\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tEcografía para seguimiento de ovulación, procedimiento completo (6 a 8 sesiones)\t04 04 008\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tEcografía pélvica masculina (incluye vejiga y próstata)\t04 04 009\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tEcografía renal (bilateral), o de bazo\t04 04 010\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tEcografía encefálica (RN o lactante)\t04 04 011\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tEcografía mamaria bilateral (incluye Doppler)\t04 04 012\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tEcografía ocular, uno o ambos ojos.\t04 04 013\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tEcografía testicular (uno o ambos) (Incluye Doppler)\t04 04 014\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tEcografía tiroidea (Incluye Doppler)\t04 04 015\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tEcografía Partes Blandas o Musculoesquelética (cada zona anatómica)\t04 04 016\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tEcografía axilar\t04 04 017\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tElastografía hepática\t04 04 018\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tEcografía vascular (arterial y venosa) periférica (bilateral)\t04 04 118\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tEcografía doppler de vasos del cuello\t04 04 119\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tEcografía transcraneana\t04 04 120\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tEcografía abdominal o de vasos testiculares\t04 04 121\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tEcografía doppler de vasos placentarios\t04 04 122\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tPunción aspirativa con aguja fina de nódulo tiroideo\t14 01 001\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tAngiotac miembro superior\t04 88 884\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tAngiotac miembro inferior\t04 88 885\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tEcotomografia portátil (traslado desde imagenología al servicio que lo requiere)\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tProcedimiento Bajo Eco (paaf, punción de partes blandas, drenajes)\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tMarcación Ecográfica\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tCavidades para nasales\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tTóracocentesis guíado por ecotomografía\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tLaparocentesis guíado por ecotomografía\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tExtracción de cuerpos extraños guíado por ecotomografía\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tPunción citológica de tiroides por ultrasonido\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tBiopsia de lesiones de partes blandas guíado por ecotomografía\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tBiopsia de tiroides con aguja fina PAAF\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tBiopsia hepática\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tBiopsia muscular\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tInfiltraciones terapéuticas guíado por ecotomografía\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tArtrocentesis (drenaje articular) diagnóstico y terapéutico guíado por ecotomografía\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tDrenaje de colecciones guíado por ecotomografía\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tDrenaje de colecciones guíado por tomografía computada\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tDrenaje Percutaneo bajo TAC con Anestesia General\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tUnidades de apoyo clínico\tImagenología\tProcedimientos imagenológicos\tMédico Radiólogo \tDrenaje Percutaneo bajo TAC sin Anestesia General\ts/c\tEPH\tactual\t\tHospital\tNO\t
USUARIO \tMACROPROCESO\tPROCESO (UNIDAD O SERVICIO)\tSUBPROCESO (TIPO DE PRESTACIÓN)\tESTAMENTO O ESPECIALIDAD\tPRESTACIÓN\tCÓDIGO MAI\tPRESTACIÓN EPH\tPRESTACIÓN ACTUAL\tPRESTACIÓN NUEVA\tÁREA DE INFLUENCIA\tCOMPRA DE SERVICIO\tOBSERVACIONES
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tÁcido úrico\t302005\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tAlbumina\t302085\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tAmilasa\t302008\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tAmonio\t302010\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tBilirrubina directa\t302013\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tBilirrubina indirecta\t302013\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tBilirrubina total\t302012\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tBilirrubina total RN\t302012\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tCalcio\t302015\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tCalcio iónico\t302081\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tCapacidad de fijación total del fierro (TIBC)\t301029\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tCapacidad latente de fijación del hierro (UIBC)\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tCinética del hierro\t301030\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tCK-MB (Creatininquinasa MB)\t302025\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tCK MB + CK total\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tCK total (Creatininquinasa total)\t302026\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tClearence creatinina\t302024\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tColesterol HDL\t302068\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tColesterol LDL\t302091\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tColesterol total\t302067\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tColesterol VLDL \tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tCreatinina\t302023\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tCurva tolerancia glucosa\t302048\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tElectrolitos plasmáticos\t302032\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tFerritina\t301026\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tFierro\t301028\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tFosfatasa alcalina\t302039\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tFosforo\t302042\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tFraccionadas Albumina /Globulina\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tGGT (Gamma glutamiltranspeptidasa)\t302045\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tGases arteriales\t302046\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tGases venosos\t302046\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tGlicemia\t302047\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tGlicemia Post Pandrial\t302093\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tGOT (Glutámico oxalacético transaminasa)\t302063\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tGPT (Glutámico pirúvico transaminasa)\t302063\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tHemoglobina glicada\t301041\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tHOMA (Modelo de evaluación homeostática)\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tLactato\t302004\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tLDH (Lactato deshidrogenasa)\t302030\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tLíquido amniótico\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tLiquido ascítico\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tLíquido cefalorraquídeo\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tLiquido pericárdico\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tLiquido pleural\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tLiquido sinovial/articular\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tLipasa\t302053\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tMagnesio\t302056\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tMagnesio iónico \tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tNitrógeno ureico (BUN)\t302057\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tPrueba Tolerancia Glucosa Oral (PTGO)\t302048\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tProteínas totales\t302100\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tRecuento de glóbulos rojos en LCR\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tRecuento de leucocitos en líquidos\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tTransferrina\t301082\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tTriglicéridos\t302064\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tUremia\t302057\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tBioquímica \tTecnología Médica\tVelocidad de filtración glomerular\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHormonas\tTecnología Médica\tB-HCG (Gonadotropina coriónica humana)\t303014\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHormonas\tTecnología Médica\tCortisol\t303006\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHormonas\tTecnología Médica\tCurva de insulina\t303031\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHormonas\tTecnología Médica\tFolato\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHormonas\tTecnología Médica\tFSH (Hormona folículo estimulante)\t303015\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHormonas\tTecnología Médica\tInsulina basal\t303017\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHormonas\tTecnología Médica\tInsulina postcarga\t303031\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHormonas\tTecnología Médica\tInsulina postprandial\t303031\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHormonas\tTecnología Médica\tLH (Hormona luteinizante)\t303016\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHormonas\tTecnología Médica\tNT- proBNP\t303055\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHormonas\tTecnología Médica\tProcalcitonina\t301096\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHormonas\tTecnología Médica\tProgesterona\t303019\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHormonas\tTecnología Médica\tProlactina\t303020\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHormonas\tTecnología Médica\tT3 total (Triyodotironina)\t303028\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHormonas\tTecnología Médica\tT4 total (Tiroxina)\t303027\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHormonas\tTecnología Médica\tT4 libre (Tiroxina libre)\t303026\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHormonas\tTecnología Médica\tTroponina\t302027\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHormonas\tTecnología Médica\tTSH (hormona estimulante de tiroides)\t303024\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHormonas\tTecnología Médica\tVitamina B12\t302077\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHormonas\tTecnología Médica\tVitamina D\t302078\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tInmunología\tTecnología Médica\tC3 (Complemento C3)\t305012\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tInmunología\tTecnología Médica\tC4 (Complemento C4)\t305012\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tInmunología\tTecnología Médica\tFactor Reumatoide\t305020\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tInmunología\tTecnología Médica\tIgA (inmunoglobulina A)\t305027\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tInmunología\tTecnología Médica\tIgG (Inmunoglobulina G)\t305027\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tInmunología\tTecnología Médica\tIgM (inmunoglobulina M)\t305027\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tInmunología\tTecnología Médica\tPCR (Proteína C reactiva)\t305031\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMarcadores Tumorales\tTecnología Médica\tAFP (Alfa fetoproteína)\t305003\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMarcadores Tumorales\tTecnología Médica\tAnticuerpos antiperoxidasa (TPO)\t305007\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMarcadores Tumorales\tTecnología Médica\tCA 19-9\t305170\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMarcadores Tumorales\tTecnología Médica\tCA 125\t305170\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMarcadores Tumorales\tTecnología Médica\tCEA (Antígeno carcinoembrionario)\t305009\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMarcadores Tumorales\tTecnología Médica\tPSA (Antígeno prostático específico)\t305070\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMarcadores Tumorales\tTecnología Médica\tTiroglobulina\t303025\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tNiveles Séricos de fármacos\tTecnología Médica\tAcetoaminofeno\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tNiveles Séricos de fármacos\tTecnología Médica\tAcido Valproico\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tNiveles Séricos de fármacos\tTecnología Médica\tAmikacina\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tNiveles Séricos de fármacos\tTecnología Médica\tCarbamazepina\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tNiveles Séricos de fármacos\tTecnología Médica\tDigoxina\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tNiveles Séricos de fármacos\tTecnología Médica\tFenitoina\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tNiveles Séricos de fármacos\tTecnología Médica\tFenobarbital\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tNiveles Séricos de fármacos\tTecnología Médica\tGentamicina\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tNiveles Séricos de fármacos\tTecnología Médica\tLitio\t302055\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tNiveles Séricos de fármacos\tTecnología Médica\tVancomicina\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tVirología\tTecnología Médica\tSerología Virus Hepatitis A\t306074\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tVirología\tTecnología Médica\tSerología Virus Hepatitis B\t306074\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tVirología\tTecnología Médica\tSerología Virus Hepatitis C\t306074\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tVirología\tTecnología Médica\tSerología Virus Hepatitis E\t306074\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tVirología\tTecnología Médica\tSerología VIH\t306109\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tÁcido úrico orina 24 horas\t309004\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tAmilasa orina aislada\t309006\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tCalcio orina 24 horas\t309008\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tCreatinina orina 24 horas\t309010\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tCreatinina orina aislada\t309010\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tElectrolitos orina 24 horas\t309012\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tElectrolitos orina aislada\t309012\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tFosforo orina 24 horas\t309015\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tGlucosa orina 24 horas\t302093\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tGlucosa orina aislada\t302093\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tMagnesio orina 24 horas\t309040\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tMicroalbuminuria 24 horas\t309013\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tMicroalbuminuria orina aislada\t309013\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tOrina completa\t309022\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tProteínas orina 24 horas\t309028\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tProteínas orina aislada\t309028\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tRAC (Razón microalbuminuria/creatinuria)\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tRPC (Razón proteinuria/creatinuria)\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tScreening de drogas Anfetaminas\t309031\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tScreening de drogas Benzodiacepina\t309031\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tScreening de drogas Cocaína\t309031\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tScreening de drogas Marihuana\t309031\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tUroanálisis\tTecnología Médica\tTest de embarazo\t309014\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHematología\tTecnología Médica\tHematocrito – Hemoglobina\t308053\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHematología\tTecnología Médica\tHemograma\t301045\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHematología\tTecnología Médica\tRecuento globular\t301045\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHematología\tTecnología Médica\tRecuento de leucocitos\t301065\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHematología\tTecnología Médica\tRecuento de plaquetas\t301067\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHematología\tTecnología Médica\tRecuento de reticulocitos\t301068\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tHematología\tTecnología Médica\tVHS (Velocidad de eritrosedimentacion) \t301086\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tCoagulación\tTecnología Médica\tDimero D\t301095\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tCoagulación\tTecnología Médica\tFactor VIII\t301025\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tCoagulación\tTecnología Médica\tFactor Von Willebrand\t301089\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tCoagulación\tTecnología Médica\tFibrinógeno\t301027\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tCoagulación\tTecnología Médica\tProtrombina + INR\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tCoagulación\tTecnología Médica\tTTPA\t301085\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tInmunohematología\tTecnología Médica\tGrupo ABO y Rh \t301034\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tInmunohematología\tTecnología Médica\tGrupo ABO y Rh Recién nacido\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tInmunohematología\tTecnología Médica\tPruebas de compatibilidad\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tInmunohematología\tTecnología Médica\tTest de Coombs directo\t301014\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tInmunohematología\tTecnología Médica\tTest de Coombs indirecto/ Detección de anticuerpos irregulares\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tInmunohematología\tTecnología Médica\tTransfusión adulto\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tCoprocultivo\t306007\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tCultivo de expectoración\t306008\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tCultivo de aspirado traqueal \t306008\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tCultivo de flujo vaginal\t308044\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tCultivo de hisopado ungueal para portación de S. aureus\t306008\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tCultivo de Lavado broncoalveolar\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tCultivo de levaduras\t306017\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tCultivo de líquidos biológicos\t306101\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tCultivo de punta catéter venoso central\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tCultivo de secreciones\t306008\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tHemocultivos\t306091\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tPortación de Enterococcus resistente a Vancomicina\t0306008+ 0306027\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tPortación de Streptococcus grupo B\t306099\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tUrocultivo\t306011\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tTest Puumala IgM\t306121\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tTest rápido de Chlamydia trachomatis\tS/C\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tLeucocitos fecales\t308005\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tTest de Adenovirus\t306070\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tTest de Rotavirus\t306170\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tTest de Antígeno y Toxina de Clostridium difficile\t306098\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tTest de azúcares reductores\t308001\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tpH en deposición\t308006\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tTest de Helicobacter pylori en deposición\t306108\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tTest de sangre oculta en deposición\t308004\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tASO (Anticuerpos antiestreptolisina O)\t305008\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tPruebas tíficas\t306039\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tRPR (Reagina plasmática rápida)\t306038\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tTest de Ureasa\t1801037\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tTinta china LCR\t306105\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tExamen directo al fresco\t306004\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tMicrobiología\tTecnología Médica\tVDRL\t306042\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tParasitología\tTecnología Médica\tParasitológico seriado de deposiciones\t306048\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tParasitología\tTecnología Médica\tTest de Graham\t306051\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tVirus respiratorios\tTecnología Médica\tTest de antígeno SARS-CoV-2\t306070\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tVirus respiratorios\tTecnología Médica\tTest rápido Influenza A\t306070\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tVirus respiratorios\tTecnología Médica\tTest rápido Influenza B\t306070\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tVirus respiratorios\tTecnología Médica\tTest rápido Virus sincicial\t306270\tEPH\t\t\tHospital\tNO\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCATECOLAMINAS EN ORINA, ug/24 horas\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tDOPAMINA, ug/24 horas\t303051\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tEPINEFRINA, ug/24 horas\t303051\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tNOREPINEFRINA, ug/24 horas\t303051\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANA PROFILE 23 AUTOANTICUERPOS IgG\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tINMUNOGLOBULINA E TOTAL, UI/mL\t305028\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI TIROGLOBULINA, UI/mL\t305007\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI RECEPTOR DE TSH (TRAB), IU/L\t305124\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPEPTIDO CITRULINADO, ANTICUERPOS IgG, RU/mL\t305099\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI DNA\t305005\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI NUCLEARES\t305005\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI CITOPLASMA DE NEUTROFILOS C\t305082\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI CITOPLASMA DE NEUTROFILOS P\t305082\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI MICROSOMALES, UI/mL\t305007\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tHORMONA PARATIROIDEA INTACTA, pg/mL\t303018\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tESTRADIOL, 17 BETA, pg/mL\t303030\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\t17 ALFA HIDROXIPROGESTERONA, ng/mL\t303029\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tINDICE ANDROGENICO LIBRE, %\t303123\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tSEX HORMONE BINDING GLOBULIN, nmol/L\t303046\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tTESTOSTERONA TOTAL, ng/mL\t303022\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tTESTOSTERONA LIBRE, pg/mL\t303023\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPANEL ENFERMEDADES TRANSMISION SEXUAL (ETS) POR PCR-RT\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCHLAMYDIA TRACHOMATIS POR PCR-RT\t306097\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tMYCOPLASMA GENITALIUM POR PCR-RT\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tMYCOPLASMA HOMINIS POR PCR-RT\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tNEISSERIA GONORRHOEAE POR PCR-RT\t306097\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tUREAPLASMA PARVUM POR PCR-RT\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tUREAPLASMA UREALYTICUM POR PCR-RT\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tTRICHOMONAS VAGINALIS POR PCR-RT\t306097\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tELECTROFORESIS DE PROTEINAS\t302061\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tINMUNOFIJACION INMUNOGLOBULINAS\t305025\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPANEL IGEE ESPECIFICA\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI MITOCONDRIALES\t305005\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tELECTROFORESIS DE PROTEINAS EN ORINA\t302061\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tADENOSINDEAMINASA, LIQUIDO PLEURAL, U/L\t302050\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tVIRUS PAPILOMA HUMANO POR PCR-MICROARRAY\t306123\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCADENAS LIVIANAS LIBRES, Razón Kappa/Lamba\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tHEPATITIS B, ANTICUERPOS ANTI CORE IgM (Anti HBc-IgM)\t306076\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI JO-1, UE/mL\t305004\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI RNP, UE/mL\t305004\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI Ro (SS-A), UE/mL\t305004\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI LA (SS-B), UE/mL\t305004\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI SCL-70, UE/mL\t305004\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI Sm, UE/mL\t305004\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTIGENOS NUCLEAR EXTRACTABLE (ENA)\t305004\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI MUSCULO LISO\t305007\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tALFA 1 ANTITRIPSINA, mg/dL\t305001\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCERULOPLASMINA, mg/dL\t302019\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI LKM-1, U/mL\t305085\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCITOMEGALOVIRUS ANTICUERPOS IgM, Index value\t306069\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tRUBEOLA ANTICUERPOS IgM, Index value\t306069\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tTOXOPLASMOSIS, ANTICUERPOS IgM, U\t306066\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tTRANSGLUTAMINASA TISULAR, ANTICUERPOS IgA, U/mL\t305181\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI ENDOMISIAL IgA\t305081\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tHEMOCROMATOSIS, ESTUDIO GENÉTICO MOLECULAR\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPROLACTINA, POOL, ng/mL\t303020\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tTIPIFICACION HLA-B27 POR PCR-MICROARRAY\t305118\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCITOMEGALOVIRUS, ANTICUERPOS IgG, UE/mL\t306069\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPARVOVIRUS B19, ANTICUERPOS IgG, U\t306069\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPARVOVIRUS B19, ANTICUERPOS IgM, U\t306069\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tZINC EN SUERO, ug/dL\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCA 15-3, U/mL\t305170\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCALPROTECTINA CUANTITATIVA, ug/g\t308049\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tINSULIN LIKE GROWTH FACTOR-1 (IGF-1), ng/mL\t303047\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tIGF BINDING PROTEIN-3, ng/mL\t303048\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tMIELOPEROXIDASA (MPO) ANTICUERPOS, Index value\t305107\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tAQUAPORINA 4 - ANTICUERPOS (NMO - IGG)\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPANEL MENINGITIS/ENCEFALITIS POR PCR-RT\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTI-B2-GLICOPROTEINA I, ANTICUERPOS IgG, RU/mL\t305007\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTI-B2-GLICOPROTEINA I, ANTICUERPOS IgM, RU/mL\t305007\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCARDIOLIPINAS, ANTICUERPOS IgG, U/mL\t305084\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCARDIOLIPINAS, ANTICUERPOS IgM, U/mL\t305084\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tVIRUS LINFOTROPICO HUMANO TIPO 1 Y 2\t306111\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tVARICELLA ZOSTER, ANTICUERPOS IgG, U\t306069\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tVARICELLA ZOSTER, ANTICUERPOS IgM, U\t306069\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICOAGULANTE LUPICO RATIO SCRENING (AS)\t301007\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICOAGULANTE LUPICO RATIO CONFIRMATORIO (AC)\t301007\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tHEPATITIS B, ANTICUERPOS CORE (ANTI HBc)\t306076\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tBANDAS OLIGOCLONALES EN SUERO Y LCR\t308020\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tBETA 2 MICROGLOBULINA, mg/L\t305010\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCOBRE EN SUERO, ug/dL\t302020\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCOBRE EN ORINA AISLADA, ug/g creatinina\t309036\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCREATININA EN ORINA AISLADA, mg/dL\t309010\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANDROSTENEDIONA, ng/mL\t303003\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI TREPONEMA (FTA-ABS)\t306041\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tHORMONA ADENOCORTICOTROFICA, pg/mL\t303001\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tADENOVIRUS, ANTICUERPOS IgG, U\t306069\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tADENOVIRUS, ANTICUERPOS IgM, U\t306069\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tHERPES SIMPLE 1, ANTICUERPOS IgG, Index value\t306069\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tHERPES SIMPLE 1, ANTICUERPOS IgM, UE\t306069\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tHERPES SIMPLE 2, ANTICUERPOS IgG, Index value\t306069\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tHERPES SIMPLE 2, ANTICUERPOS IgM, UE\t306069\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tSARAMPION, ANTICUERPOS IgG, U\t306069\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tSARAMPION, ANTICUERPOS IgM, U\t306069\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPNEUMOCYSTIS JIROVECII (CARINII) POR PCR-RT\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\t25-OH-VITAMINA D3 (COLECALCIFEROL), ng/mL\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI CELULAS PARIETALES IgG, RU/mL\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tMARCADORES INMUNOLOGICOS EN DIABETES\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tAC. ANTIDESCARBOXILASA DEL ACIDO GLUTAMICO (GAD)\t305007\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI TIROSIN FOSFATASA (IA-2)\t305007\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI INSULINA (IAA)\t305007\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI CELULAS BETA (ICA)\t305007\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tAUTO AC. ANTI TRANSPORTADOR 8 DEL ZINC (ZnT8)\t305007\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPANEL MIOSITIS AUTOANTICUERPOS IgG\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPANEL EMBARAZADA PLUS POR PCR-RT\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tLEVETIRACETAM, ug/mL\t302035\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tACTIVIDAD RENINA PLASMATICA, ng/mL/hora a pH 6,0 (parado)\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tALDOSTERONA, ng/dL\t303002\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tLINFOCITOS T HELPERS (CD4+)\t305091\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tRUBEOLA ANTICUERPOS IgG, UI/mL\t306069\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tMETANEFRINAS URINARIAS, ug/24 horas\t303050\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\t3-METOXITIRAMINA URINARIAS, ug/24 hrs.\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tNORMETANEFRINAS URINARIAS, ug/24 hrs.\t303050\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tTRANSGLUTAMINASA TISULAR, ANTICUERPOS IgG, U/mL\t305181\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tFACTOR II PROTROMBINA 20210 G>A, MUTACION\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tFACTOR V LEIDEN, MUTACION\t301024\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCREATININA EN ORINA, mg/24 horas\t309010\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tIGF BINDING PROTEIN-1, ng/mL\t303048\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tRENINA PLASMATICA, pg/mL (sentado)\t303021\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPROTEINA C, COAGULACION\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPROTEINA C, RESISTENCIA\t301093\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPROTEINA S LIBRE\t301092\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPANEL CANDIDA TRANSMISION SEXUAL (ETS) POR PCR-RT\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tIGE ESPECÍFICA, ACAROS\t305029\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tIGE ESPECÍFICA, CASPA DE PERRO\t305029\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tIGE ESPECÍFICA, EPITELIO DE PERRO\t305029\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tIGE ESPECÍFICA, MALEZAS\t305029\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tIGE ESPECÍFICA, MEZCLA DE HONGOS\t305029\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tIGE ESPECÍFICA, POLVO DE HABITACION\t305029\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI DNA GENOMICO DOBLE CADENA, IU/Ml\t305007\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tVITAMINA A (RETINOL), mg/L\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tVITAMINA E (ALFA TOCOFEROL), mg/L\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tTIROGLOBULINA, ng/mL\t303025\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tHOMOCISTEINA, umol/L\t302086\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTIGLIADINAS, ANTICUERPOS IgA, U/mL\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTIGLIADINAS, ANTICUERPOS IgG, U/mL\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tHORMONA DE CRECIMIENTO, ng/mL\t303007\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCITOMEGALOVIRUS, CARGA VIRAL POR PCR-RT, UI/mL\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tVIRUS BK, copias/mL\t306088\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPREALBÚMINA,mg/dL\t302085\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTITROMBINA III FUNCIONAL\t301008\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tHEMOGLOBINA, ELECTROFORESIS\t301044\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tHORMONA ANTIMULLERIANA (AMH)\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tRENINA PLASMATICA, pg/mL\t303021\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tMETANEFRINAS LIBRES EN PLASMA, ng/L\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCATECOLAMINA EN PLASMA, pg/mL\t303049\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tDOPAMINA, pg/mL\t303051\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tEPINEFRINA, pg/mL\t303051\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tNOREPINEFRINA, pg/mL\t303051\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tINMUNOGLOBULINA A SECRETORA, mg/dL\t305026\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tBORRELIA BURGDORFERI, ANTICUERPOS IgG, U\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tBORRELIA BURGDORFERI, ANTICUERPOS IgM, U\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPROTEINASA 3 (PR-3) ANTICUERPOS, Index value\t305007\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tBARTONELLA HENSELAE, ANTICUERPOS IgG\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tBARTONELLA HENSELAE, ANTICUERPOS IgM\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPEPTIDO C, ng/mL\t303052\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tTOXOPLASMOSIS, ANTICUERPOS IgG, U\t306061\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPARVOVIRUS B19 POR PCR-RT CUALITATIVO\t306069\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tVIRUS PAROTIDITIS, ANTICUERPOS IgM, Ratio\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCARBAMAZEPINA TOTAL, ug/mL\t302035\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tLAMOTRIGINA, ug/mL\t302035\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tFOSFOLIPIDOS, mg/dL\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tGLUCOSA 6 FOSFATO DESHIDROGENASA, min\t301017\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tINMUNOGLOBULINA DE SUB CLASE IgG1, mg%\t305029\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tINMUNOGLOBULINA DE SUB CLASE IgG2, mg%\t305029\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tINMUNOGLOBULINA DE SUB CLASE IgG3, mg%\t305029\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tTEST GENETICO INTOLERANCIA A LA LACTOSA\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tINMUNOGLOBULINA DE SUB CLASE IgG4, mg%\t305029\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTINEUMOCOCO 23 SEROTIPOS\t305007\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tERITROPOYETINA PLASMATICA, mUI/mL\t303009\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tESTRONA, pg/mL\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tINHIBINA B\t303054\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tDIHIDROTESTOSTERONA, pg/mL\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCITOMEGALOVIRUS, CARGA VIRAL POR PCR-RT, copias/mL\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tEPSTEIN BARR, CARGA VIRAL POR PCR-RT\t306087\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tMYCOPLASMA PNEUMONIAE, ANTICUERPOS IgM, U\t306037\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTIRECEPTORES DE ACETILCOLINA\t305007\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCUANTIFICACION ARN VIRAL VIH, copias/mL\t306086\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tSTREPTOCOCCUS GRUPO B (AGALACTIAE) POR PCR-RT\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tDEHIDROEPIANDROSTERONA SULFATO, ng/mL\t303008\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tBRUCELLA, ANTICUERPOS IgG, U\t306033\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tBRUCELLA, ANTICUERPOS IgM, U\t306033\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI CENTROMERO\t305005\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTIGENO URINARIO DE LEGIONELLA PNEUMOPHILA\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\t22 ALERGENOS\t305029 x22 (c/u)\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tALDOSTERONA EN ORINA, ug/24 horas\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPANEL PATOGENOS VAGINALES TRANSMISION SEXUAL (ETS) POR PCRRT\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCARGA VIRAL HEPATITIS C, copias/mL\t306085\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tHEPATITIS C, VIRUS DETECCION POR PCR-RT\t306182\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tEPSTEIN BARR VIRUS POR PCR-RT\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTIGENO DE GALACTOMANANO DE ASPERGILLUS\t306094\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tELASTASA FECAL CUANTITATIVA, ug/g\t308007\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCOBRE EN ORINA, ug/24 horas\t309036\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTIGENO PROSTATICO ESPECIFICO LIBRE, ng\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPERFIL DE AMINOACIDOS Y ACILCARNITINAS,\t302098\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tEPSTEIN BARR VIRUS, ANTICUERPOS VCA IgG,\t306069\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tEPSTEIN BARR VIRUS, ANTICUERPOS VCA IgM,\t306069\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tLINFOCITOS B TOTALES (CD19)\t305089\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tINHIBIDOR DE C1 ESTERASA CUANTITATIVO, mg/L\t305021\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCOMPONENTE DE COMPLEMENTO C1q, mg/dL\t305012\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANFETAMINA/METANFETAMINA ng/mL\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTIGENO DE NEUMOCOCO EN ORINA\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tVIRUS PAROTIDITIS, ANTICUERPOS IgG, Ratio\t306069\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tLEGIONELLA SPP. POR PCR-RT\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCORTISONA, ng/mL\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tACIDO VAINILLILMANDELICO, mg/24 horas\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPANEL HERPES BK11\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPANEL VIRAL MENINGITIS\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPANEL BACTERIANO MENINGITIS\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI RECEPTOR DE FOSFOLIPASA\t305007\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPANEL GASTROENTERITIS BACTERIANO - VIRAL\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPORFOBILINOGENO EN ORINA 24 HORAS\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tLINFOCITOS T HELPERS (CD3+ TOTALES)\t305091\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tLINFOCITOS T SUPRES (CD8+)\t305091\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tANTICUERPOS ANTI MEMBRANA BASAL\t305081\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tVITAMINA C, mg/L\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tHELICOBACTER PYLORI POR PCR-RT\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tSTREPTOCOCCUS GRUPO B (AGALACTIAE) POR PCR-RT\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tTEST DE SUDAN (Grasas Neutras)\t308003\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tENZIMA CONVERTIDORA DE ANGIOTENSINA, U/L\t302033\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tHIDATIDOSIS, ANTICUERPOS IgG, U\t306061\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tMYCOPLASMA PNEUMONIAE, ANTICUERPOS IgG, U\t306037\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tAC. ANTIPEPTIDO DEAMINADO DE GLIADINA IgA, U/mL\t305086\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tAC. ANTIPEPTIDO DEAMINADO DE GLIADINA IgG, U/mL\t305086\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCATECOLAMINA EN PLASMA, pg/mL (acostado)\t303049\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCHLAMYDIA TRACHOMATIS, ANTICUERPOS IgG, U\t306034\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tCHLAMYDIA TRACHOMATIS, ANTICUERPOS IgM, U\t306034\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tHAPTOGLOBINA, mg/dL\t301035\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación Barnafi Krause\tTecnología Médica\tPANEL GASTROENTERITIS BACTERIANO - PARASITARIO - VIRAL POR PCR\t306095\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación HCHM\tTecnología Médica\tPCR SARS-CoV2\t306082\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación HCHM\tTecnología Médica\tÁcidos Biliares\tS/C\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación HCHM\tTecnología Médica\tTest Rápido Chagas\t306096\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación HCHM\tTecnología Médica\tPanel respiratorio ampliado PCR-RT\t306122\tEPH\t\t\tHospital\tSí\t
Adulto/a / Infantil\tApoyo clínico diagnóstico/ terapéutico\tLaboratorio Clínico \tDerivación UdeChile\tTecnología Médica\tCariograma Ley I.V.E.\tS/C\tEPH\t\t\tHospital\tSí\t
USUARIO \tMACROPROCESO\tPROCESO (UNIDAD O SERVICIO)\tSUBPROCESO (TIPO DE PRESTACIÓN)\tESTAMENTO O ESPECIALIDAD\tPRESTACIÓN\tCÓDIGO MAI\tPRESTACIÓN EPH\tPRESTACIÓN ACTUAL\tPRESTACIÓN NUEVA\tÁREA DE INFLUENCIA\tCOMPRA DE SERVICIO\tOBSERVACIONES
Adulto\tAtención abierta\tDental \tConsulta y atención odontológica \tOdontólogo \tConsulta especialidad Periodoncia\t2701101\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tConsulta y atención odontológica \tOdontólogo \tConsulta especialidad Endodoncia\t2701103\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tConsulta y atención odontológica \tOdontólogo \tConsulta especialidad Imagenología Oral y Maxilofacial \t2701104\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tDental \tConsulta y atención odontológica \tOdontólogo \tConsulta especialidad Implantología Buco Maxilofacial\t2701105\tEPH\tactual\t\tHospital\tNO\t
Infantil\tAtención abierta\tDental \tConsulta y atención odontológica \tOdontólogo \tConsulta especialidad Odontopediatría\t2701106\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tConsulta y atención odontológica \tOdontólogo \tConsulta especialidad Ortodoncia y Ortopedia Dento Maxilofacial\t2701107\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tDental \tConsulta y atención odontológica \tOdontólogo \tConsulta especialidad Patología Oral y Maxilofacial\t2701108\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tDental \tConsulta y atención odontológica \tOdontólogo \tConsulta especialidad Rehabilitación Oral\t2701109\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tDental \tConsulta y atención odontológica \tOdontólogo \tConsulta especialidad Trastornos Temporomandibulares y Dolor Orofacial\t2701110\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tConsulta y atención odontológica \tOdontólogo \tConsulta o control por Odontólogo General\t2701113\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tDental \tConsulta y atención odontológica \tOdontólogo \tConsulta de urgencia odontológica \t2701115\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tAplicación de sellantes\t27 01 001\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tDesgastes selectivos\t27 01 002\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tDestartraje y pulido coronario\t27 01 003\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tAplicación fluoruros\t27 01 007\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tMantenedores de espacio\t27 01 008\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tPulpotomía\t27 01 011\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tExamen de salud oral\t27 01 013\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tAplicación barniz de flúor\t27 01 017\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tExodoncia simple diente permanente\t27 01 005\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tExodoncia diente primario\t27 01 006\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tObturación amalgama \t27 01 009\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tObturación composite\t27 01 010\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tUrgencias\t27 01 012\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tRadiografía retroalveolar y Bite-Wing (por placa)\t27 01 015\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tObturación Vidrio Ionómero\t27 01 016\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tCirugía bucal\t27 02 001\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tObturación Inlay metal (incluye materiales no preciosos, no incluye oro)\t27 02 004\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tConsulta especialidad Periodoncia\t27 02 005\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tPlano alivio oclusal\t27 02 006\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tPrótesis de restitución (fase clínica)\t27 02 007\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tPrótesis metálica\t27 02 008\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tRadiografía extraoral (por placa)\t27 02 009\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tRadiografía oclusal (por placa)\t27 02 010\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tPrótesis de restitución (fase laboratorio)\t27 02 011\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tReparación compuesta de prótesis\t27 02 012\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tReparación corona\t27 02 013\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tReparación o reajuste prótesis\t27 02 014\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tRestitución por corona (combinada)\t27 02 015\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tRestitución por corona provisoria\t27 02 016\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tSialografía (cada lado) (incluye el proc.)\t27 02 017\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tTratamiento ortodoncia con aparatología removible  (incluye aparato)(año 1)\t27 02 019\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tTratamiento ortodoncia con aparatologia fija (incluye aparato) (año 1)\t27 02 020\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tTratamiento ortodoncia con aparatologia fija (incluye aparato) (año 2)\t27 02 021\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tEndodoncia Multirradicular\t27 02 022\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tEndodoncia birradicular\t27 02 023\t\t\t\t\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tEndodoncia unirradicular\t27 02 024\t\t\t\t\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tTelerradiografia\t27 02 025\t\t\t\t\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tRadiografía panorámica u ortopantomografía\t27 02 026\t\t\t\t\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tTomografia Computacional Maxilo Facial Cone Beam\t27 02 027\t\t\t\t\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tSutura intraoral \ts/c\t\t\t\t\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tTratamiento quirúrgico pseudoquiste y quiste odontológico \ts/c\t\t\t\t\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tTratamiento quirúrgico tumor odontológico \ts/c\t\t\t\t\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tFrenectomia \t50 99 022\t\t\t\t\tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tFenestracion\t50 99 023\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tDrenaje Abceso intra-extroral\t50 99 024\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tCirugía preprotesica \t50 99 025\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tDesobturacion de conductos \t 50 99 056 \tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tCirugía ortognática\ts/c\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tDisyunción palatina quirúrgica\t27 03 003\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tExtirpación de pseudoquistes, quistes y tumores\t27 03 004\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tGlosectomías\t27 03 005\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tImplante endodóntico intraóseo\t27 03 006\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tImplantes subperiósticos\t27 03 007\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tExodoncia de dientes retenidos\t27 03 008\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tInjertos en boca\t27 03 009\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tElevación de piso del seno maxilar\t27 03 010\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tPlastía de fístula salival\t27 03 011\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tPreparación quirúrgica de los maxilares con fines protésicos\t27 03 012\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tProfundización de vestíbulo o reconstrucción de rebordes, con o sin injerto\t27 03 013\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tReimplante y trasplante dentario\t27 03 014\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tRemoción de cuerpo extraño y secuestrectomía\t27 03 015\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tSutura completa de herida mayor\t27 03 016\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tSutura completa de herida menor\t27 03 017\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tSutura simple de herida\t27 03 018\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tTratamiento quirúrgico fracturas maxilar superior\t27 03 019\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tTratamiento quirúrgico de fracturas en maxilar inferior\t27 03 020\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tTratamiento de traumatismo dento alveolar simple\t27 03 021\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tTratamiento de traumatismo dento alveolar complejo\t27 03 022\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tImplante oseointegrado\t27 03 023\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tPilar Protésico sobre Implantes\t27 03 024\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tBloqueo Anestesico\t50 99 026\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tActividad interseptiva de anomalias dentomaxilares OPI\t50 99 028\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tInstalacion de aparato intercepcion de anomalias dentomaxilares\t50 99 029\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tExamen diagnostico OPI\t50 99 030\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tAlta mantencion \t50 99 031\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tCorona metalica\t50 99 032\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tInstalacion aparato removible \t50 99 033\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tInstalacion aparato ortopedia prequirurgica (fisura labiopalatina)\t50 99 034\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tOrtopedia prequirurgica actividad (fisura labiopalatina)\t50 99 035\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tInstalación Aparato Fijo en Ortodoncia. (Brackets)\ts/c\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tTratamiento de induccion al cierre\t50 99 036\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tDesobturacion de conductos\t50 99 037\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tMedicación intraconducto (acción de endodoncia)\ts/c\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tTerapia articular especifica\t50 99 038\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tFérula Periodoncia\ts/c\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tTelerradiografia perfil\t50 99 041\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tTelerradiografia frente\t50 99 042\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tRadiografia articulacion temporo mandibular\t50 99 043\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tinstalacion aparotologia fija\t50 99 057\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tinstalacion protesis removible\t50 99 058\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tPrótesis Removible Acrílica\ts/c\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tPrótesis Removible Metálica\ts/c\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tInstalación Aparato de Contención. \ts/c\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tReparación de Prótesis. \ts/c\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tPrótesis Fija Provisoria (unitaria o Plural)\ts/c\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tTratamiento Traumatismo Dentoalveolar \ts/c\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tInstalación de Implante Endo-Oseo Oseointegrable. \ts/c\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tTratamiento Temporo Mandibular \ts/c\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tPrevención odontológica niño discapacitado \ts/c\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tTratamiento aparatología fija niños de 12 a 14 años año 1 \ts/c\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tTratamiento aparatología fija niños de 12 a 14 años año 2 \ts/c\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tObturaciones de vidrio Ionomero en diente temporal\ts/c\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tDestartraje subgingival y Pulido radicular por Sextante\ts/c\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tDesinfección Bucal Total\ts/c\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tExamen y diagnostico ttm eje I  \t50 99 059\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tExamen y diagnostico ttm eje I y II montaje\t50 99 060\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tDental \tActividades clínicas odontológicas \tOdontólogo \tTerapia cognitiva conductual y autocontrol TTM (trastornos temporomandibulares)\t50 99 039\tEPH\tactual\t\tHospital \tNO\t
USUARIO \tMACROPROCESO\tPROCESO (UNIDAD O SERVICIO)\tSUBPROCESO (TIPO DE PRESTACIÓN)\tESTAMENTO O ESPECIALIDAD\tPRESTACIÓN\tCÓDIGO MAI\tPRESTACIÓN EPH\tPRESTACIÓN ACTUAL\tPRESTACIÓN NUEVA\tÁREA DE INFLUENCIA\tCOMPRA DE SERVICIO\tOBSERVACIONES
Adulto\tAtención abierta\tPsicosocial\tConsulta o control por Profesional no Médico\tAsistente Social \tConsulta por Asistente Social\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tPsicosocial\tConsulta o control por Profesional no Médico\tMisceláneo \tEducación de grupo por otro integrante del equipo de salud\t01 03 001\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tPsicosocial\tConsulta o control por Profesional no Médico\tAsistente Social \tEducación de grupo por asistente social\t01 03 003\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tPsicosocial\tConsulta o control por Profesional no Médico\tPsicólogo\tConsulta o control por Psicólogo clínico\t09 03 002\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tPsicosocial\tConsulta o control por Profesional no Médico\tMisceláneo \tConsulta de salud mental por otros profesionales\t09 03 003\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tPsicosocial\tConsulta o control por Profesional no Médico\tPsicólogo\tIntervención psicosocial grupal (4 a 8 pacientes, familiares o cuidadores)\t09 03 004\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tPsicosocial\tConsulta o control por Profesional no Médico\tPsicólogo\tPsicoterapia de grupo (por psicólogo o psiquiatra) (4 a 8 pacientes)\t09 03 005\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tPsicosocial\tConsulta o control Médico de Especialidad\tPsiquiatra \tConsultoría de salud mental por psiquiatra (sesión 4 hrs.) (mínimo 8 pacientes)\t09 03 006\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tPsicosocial\tConsulta o control por Profesional no Médico\tPsicólogo\tTest de Rorschach\t09 02 010\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tPsicosocial\tConsulta o control por Profesional no Médico\tPsicólogo\tTest de relaciones objetales\t09 02 011\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tPsicosocial\tConsulta o control por Profesional no Médico\tPsicólogo\tTest de Apercepción Temática, T.A.T., C.A.T.-H o C.A.T.-A.\t09 02 012\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tPsicosocial\tConsulta o control por Profesional no Médico\tAsistente Social \tConsejerias Individual por profesional de salud\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tPsicosocial\tConsulta o control por Profesional no Médico\tAsistente Social \tConsejerias Familiar por  profesionales de salud\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tPsicosocial\tConsulta o control por Profesional no Médico\tPsicólogo\tConsejerias Individual por profesional de salud\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tPsicosocial\tConsulta o control por Profesional no Médico\tPsicólogo\tConsejerias Familiar por  profesionales de salud\ts/c\tEPH\tactual\t\tHospital\tNO\t
USUARIO \tMACROPROCESO\tPROCESO (UNIDAD O SERVICIO)\tSUBPROCESO (TIPO DE PRESTACIÓN)\tESTAMENTO O ESPECIALIDAD\tPRESTACIÓN\tCÓDIGO MAI\tPRESTACIÓN EPH\tPRESTACIÓN ACTUAL\tPRESTACIÓN NUEVA\tÁREA DE INFLUENCIA\tCOMPRA DE SERVICIO\tOBSERVACIONES
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tConsulta o control Médico de Especialidad\tMedicina Interna \tConsulta Médica de Especialidad en Medicina Interna\t01 01 307\tEPH \tactual \t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tConsulta o control Médico de Especialidad\tCirugía General \tConsulta Médica de Especialidad en Cirugía General \t01 01 312\tEPH \tactual \t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tConsulta o control Médico de Especialidad\tMedicina General \tConsulta Médica de Especialidad en Medicina General\t01 01 001\tEPH \tactual \t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tConsulta o control Médico de Especialidad\tObstetricia y Ginecología \tConsulta Médica de Especialidad en Obstetricia y Ginecología \t01 01 308\tEPH \tactual \t\tHospital \tNO\t
Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tConsulta o control Médico de Especialidad\tPediatría \tConsulta Médica de Especialidad en Pediatría \t01 01 309\tEPH \tactual \t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tConsulta o control Médico de Especialidad\tTraumatología \tConsulta Médica de Especialidad en Anestesiología \t01 01 329\tEPH \tactual\t\tHospital\t\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tConsulta o control Médico de Especialidad\tAnestesiología \tConsulta Médica de Especialidad en Traumatología \t01 01 310\tEPH \tactual \t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tConsulta o control por Profesional no Médico\tMatrona \tConsulta o control por Matrona \t01 02 009\tEPH \tactual \t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tConsulta o control por Profesional no Médico\tEnfermera \tConsulta o control por Enfermera \t01 04 004\tEPH \tactual \t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tConsulta o control por Profesional no Médico\tAuxiliar de Enfermería \tConsulta o control por Auxiliar de Enfermería \t01 02 003\tEPH \tactual \t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tConsulta o control Médico de Especialidad\tNeurología Adulto \tConsulta Médica de Especialidad en Neurología Adulto \t01 01 209\tEPH \tactual \t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tOftalmología \tExtracción de cuerpo extraño conjuntival adulto\t12 01 029\tEPH \tactual \t\tHospital \tNO\t
Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tOftalmología \tExtracción de cuerpo extraño conjuntival niño\t12 01 030\tEPH \tactual \t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tNeurología \tPunción Lumbar \t11 01 003\tEPH \tactual \t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tOtorrinolaringología \tExtracción cuerpo extraño en conducto auditivo externo\t13 02 002\tEPH \tactual \t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tOtorrinolaringología \tExtracción cuerpo Extraño ótico\t13 01 042\tEPH \tactual \t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tOtorrinolaringología \tTaponamiento nasal anterior \t13 01 026\tEPH \tactual \t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tOtorrinolaringología \tTraqueostomia (proc. Aut.) \t13 02 072\tEPH \tactual \t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía Plástica y Reparadora \tHeridas de la cara Complicadas : 1 o varias de más de 5 cms. y/o ubicadas en bordes de párpados, labios ala nasal y/o que comprometen músculos, conductos, vasos o nervios\t1502002\tEPH \tactual \t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía Plástica y Reparadora \tHerida de la cara - Simples : 1 o varias de hasta 5 cms. Que solo comprometen piel.\t15 02 002\tEPH \tactual \t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía Plástica y Reparadora \tEscarectomía hasta 1% sc\t15 02 063\tEPH \tactual \t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía Plástica y Reparadora \tEscarectomía hasta 5% sc\t15 02 064\tEPH \tactual \t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía Plástica y Reparadora \tEscarotomia\t15 02 000\tEPH \tactual \t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía Plástica y Reparadora \tHerida cortante o contusa no complicada, reparación y sutura (una o múltiple hasta 5 cms. de largo total que comprometa solo la piel)\t1602222\tEPH \tactual \t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tDermatología \tExtracción cuerpo extraño cutáneo\t16 02 002\tEPH \tactual \t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tDermatología \tHerida cortante o contusa complicada, reparación y sutura (+ de 5 cm)\t16 02 221\tEPH \tactual \t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tDermatología \tHerida cortante o contusa, reparación y sutura (hasta 5 cm) No complicada\t16 02 222\tEPH \tactual \t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tDermatología \tVaciamiento y curetaje (Desbridamiento) de lesiones quísticas o absesos\t16 02 225\tEPH \tactual \t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tDermatología \tOnicectomia total o parcial simple\t16 02 231\tEPH \tactual \t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tGastroenterología \tGastroduodenoscopía (incluye esofagoscopía)\t18 01 001\tEPH \tactual \t\tHospital \tSI \tA partir del 2024
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tGastroenterología \tPunción de líquido ascítico, diagnóstica\t18 01 041\tEPH \tactual \t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tGastroenterología \tPunción evacuadora de líquido ascítico\t18 01 048\tEPH \tactual \t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tGastroenterología \tIntubación sonda de Sengstaken\t18 01 022\tEPH \tactual \t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tGastroenterología \tPunción evacuadora de absceso intraabdominales (hepático u otros), c/s toma de muestra, c/s inyección de medicamentos\t18 01 038\tEPH \tactual \t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tGastroenterología \tVaciamiento manual de fecaloma\t18 01 042\tEPH \tactual \t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tGastroenterología \tIntubación con sonda gastrica\t18 01 023\tEPH \tactual \t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tGastroenterología \tVaciamiento manual de fecaloma\t18 01 042\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tUrología y Nefrología \tVaciamiento vesical p/punción hipogátrica o cistosotmía p/punción \t19 01 021\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tUrología y Nefrología \tVaciamiento vesical por sonda uretral (proc aut)\t19 01 022\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tUrología y Nefrología \tCistostomía, con sin extracción de cuerpo extraño o cálculo \t19 02 031\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tBroncopulmonar \tToracocentesis evacuadora, c/s toma de muestras c/s inyección de medicamentos  \t17 07 029\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tCardiología\tE.C.G. de reposo (incluye mínimo 12 derivaciones y 4 complejos por derivación)\t17 01 001\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tCardiología\tColocación sonda marcapaso transitorio (proc. Completo)\t17 01 035\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tCardiología\tDenudación venosa \t17 03 023\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tBroncopulmonar \tLaringotraqueobroncoscopía con fibroscopio\t17 07 021\tEPH \t\tnueva\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tBroncopulmonar \tBroncoaspiración, c/s lavado y/o colocación de medicamentos por sonda traqueobronquial (proc. aut.)\t17 07 027\tEPH \t\tnueva\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tBroncopulmonar \tToracocentesis evacuadora, c/s toma de muestras c/s inyección de medicamentos  \t17 07 029\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tBroncopulmonar \tFibrobroncoscopía con biopsia transbronquial\t17 07 061\tEPH \t\tnueva\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tBroncopulmonar \tProcedimiento para determinar gasometría arterial en reposo y ejercicio \t17 07 025\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tBroncopulmonar \tSaturación de O2 en reposo y/o ejercicio (con oxímetro) \t17 07 054\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tBroncopulmonar \tSaturación de O2 en reposo y ejercicio y O2 100% (con oxímetro) \t17 07 055\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tTraumatología \tPunción Intra Articular\ts/c\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tTraumatología \tColocación de Yeso – Luxaciones de articulaciones menores (resto)\t21 04 003\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tTraumatología \tRodillera Bota Larga o Corta de yeso\t21 05 004\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tTraumatología \tColocación de Yeso – Luxaciones de articulaciones medianas (hombro, codo, rodilla, tobillo. Muñeca, tarso y esterno-clavicular\t21 04 003\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tTraumatología \tLuxaciones de articulaciones medianas (hombro, codo, rodilla, tobillo, muñeca, tarso y esternoclavicular)\t21 05 004\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tTraumatología \tLuxaciones de articulaciones  mayores (columna, cadera, pelvis)\t21 07 001\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tTraumatología \tLuxaciones de articulaciones menores (el resto)\t21 07 003\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tTraumatología \tFracturas mayores (columna, pelvis, supracondílea, codo, epífisis femorales)\t21 07 004\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tTraumatología \tFracturas medianas (diáfisis humeral, radial, cubital, diáfisis femoral, tibial, peroneal, clavicular, platillos tibiales)\t21 07 005\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tTraumatología \tFracturas menores (el resto)\t21 07 006\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimiento médico\tMedicina\tIntubación traqueal (proc. Aut.) \t17 07 037\tEPH \tactual\t\tHospital \tNO\t
Adulto \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos imagenológicos\tMedicina \tEcografía como apoyo a cirugía, o a procedimiento (de tórax, muscular, partes blandas, etc.)\t04 04 004\tEPH \t\tnueva\tHospital \tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos imagenológicos\tGinecología y Obsteticia \tEcografía transvaginal o transrectal\t04 04 005\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos imagenológicos\tGinecología y Obsteticia \tEcografía ginecológica, pelviana femenina u obstétrica con estudio fetal\t04 04 006\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tGinecología y Obsteticia \tBiopsia endometrio, vulva, vagina, cuello, c/u (proc. aut.)\t01 05 001\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tGinecología y Obsteticia \tAmniocentesis\t20 01 006\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tGinecología y Obsteticia \tCuldocentesis (punción del Douglas)\t20 01 007\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tGinecología y Obsteticia \tMonitoreo basal con informe\t20 01 009\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tGinecología y Obsteticia \tMonitoreo fetal estresante, con control permanente del especialista y tratamiento de las posibles complicaciones\t20 01 010\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tGinecología y Obsteticia \tColposcopía\t20 01 002\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tProcedimientos diagnósticos y terapéuticos  \tGinecología y Obsteticia \tHisteroscopía diagnóstica (proc. aut.)\t20 01 005\tEPH \tactual\t\tHospital \tNO\t
\t\t\t\t\t\t\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tMisceláneos \tEnfermera \tVacunaciones\ts/c\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tMisceláneos \tEnfermera \tHemoglucotest\t03 02 047\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tMisceláneos \tEnfermera \tCuración simple\t01 06 002\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tMisceláneos \tEnfermera \tPuncion Arterial y Venosa (toma de muestras)\t03 07 023\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tMisceláneos \tEnfermera \tManejo avanzado de heridas (pie diabetico, ulcera venosa, otros)\t03 07 024\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tMisceláneos \tEnfermera \tcuracion avanzada de heridas (enfermera)\t50 99 111\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tMisceláneos \tEnfermera \tTratamiento ulcera venosa, curación pacientes herida tipo 1 y 2 (A) no infectados (enfermera)\t25 05 438\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tMisceláneos \tEnfermera \tTratamiento ulcera venosa, curación pacientes herida tipo 3 y 4 (B) infectados (enfermera)\t25 05 439\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tMisceláneos \tEnfermera \tCuración de Quemados – 5% (enfermera)\tS/C\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tMisceláneos \tEnfermera \tCuración de Quemados + 5% (enfermera)\tS/C\tEPH \tactual\t\tHospital\tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tMisceláneos \tEnfermera \tToma de muestra arterial en adultos\t03 07 009\tEPH \tactual\t\tHospital\tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tMisceláneos \tEnfermera \tToma de muestra arterial en niños y lactantes\t03 07 010\tEPH \tactual\t\tHospital\tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tMisceláneos \tEnfermera \tToma de muestra venosa adulto\t03 07 011\tEPH \tactual\t\tHospital\tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tMisceláneos \tEnfermera \tToma de muestra venosa en niños y lactantes\t03 07 012\tEPH \tactual\t\tHospital\tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tMisceláneos \tEnfermera \tToma de muestra con técnica aséptica para hemocultivo, c/u\t03 07 013\tEPH \tactual\t\tHospital\tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tMisceláneos \tEnfermera \tToma de muestra capilar ( adultos, niños y lactantes )\t03 07 014\tEPH \tactual\t\tHospital\tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tMisceláneos \tEnfermera \tAspirados nasofaríngeo para adulto y niño.\t03 07 023\tEPH \tactual\t\tHospital\tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tMisceláneos \tMédico \tReanimación cardiopulmonar Adulto y Pediátrico\ts/c\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tMisceláneos \tMédico \tTrombolisis arterial periférica \t17 01 039\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía General \tHernia diafragmática por vía abdominal o cualquiera otra hernia con uso de prótesis (no incluye el valor de la prótesis)\t18 02 001\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía General \tHernia incisional o evisceración post-op. sin resección intestinal\t18 02 002\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía General \tHernia inguinal, crural, umbilical, de la línea blanca o similares, recidivada o no,simple o estrangulada s/resección intest.c/u\t18 02 003\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía General \tLaparotomía exploradora, c/s liberación de adherencias, c/s drenaje,c/s biopsias como proc.aut.o como resultado de una herida penetrante abdominal no complicada o de un hemoperitoneo postoperatorio o como tratamiento de una peritonitis (laparostomía contenida -máximo cuatro-, resuturas, etc.)\t18 02 004\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía General \tPeritonitis difusa aguda, trat. quir. (proc. aut.)\t18 02 007\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía General \tPerforación gástrica aguda, trat. quir. (proc. aut.)\t18 02 015\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía General \tColecistectomía por videolaparoscopía, proc. completo\t18 02 081\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía General \tColecistectomía y coledocostomía (sonda T y colangiografía postoperatoria) c/s colangiografía operatoria\t18 02 029\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía General \tHerida traumática de hígado y/o vía biliar, trat. quir.\t18 02 040\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía General \tApendicectomía y/o dren. absceso apendicular (proc. aut.)\t18 02 053\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía General \tOclusión intestinal sin resección\t18 02 066\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía General \tPerforación y/o herida de intestino, única o múltiple,trat. quir (proc. aut.)\t18 02 071\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía General \tAbsceso anorrectal complejo (implica hospitalización y anestesia general)\t18 03 001\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía General \tAbsceso anorrectal simple , trat. quir.\t18 03 002\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía General \tAbsceso sacrocoxígeo, drenaje\t18 03 003\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía General \tCuerpo extraño rectal, extracción por vía abdominal\t18 03 006\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía General \tCuerpo extraño rectal, extracción por vía anal\t18 03 007\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía General \tDesgarros y heridas anorrectales sin compromiso del esfinter\t18 03 009\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía General \tFecaloma, trat. quir.\t18 03 013\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía General \tFisura anal, repar. quir.\t18 03 017\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía General \tHemorroidectomía (incluye otras operaciones complementarias en canal anal)\t18 03 018\tEPH \tactual\t\tHospital\tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía General \tHemorroides, trombectomía (proc. aut.)\t18 03 019\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía Ginecológica \tEmbarazo tubario, trat. quir.\t20 03 003\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía Ginecológica \tDesgarro cervical trat. quir.\t20 03 030\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía Ginecológica \tBartolinitis, vaciamiento y drenaje (proc. aut.)\t20 03 026\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía Ginecológica \t- Aborto retenido, vaciamiento de (incluye la inducción en los casos que corresponda)\t20 04 001\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía Ginecológica \t- Raspado uterino diagnóstico o terapéutico por metrorragia o por restos de aborto\t20 04 002\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía Ginecológica \t- C/s salpingoligadura o salpingectomía\t20 04 006\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía Ginecológica \t- Con histerectomía\t20 04 005\tEPH \tactual\t\tHospital \tNO\t
Adulto\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía Ginecológica \tParto normal\t20 04 103\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía Ginecológica \tParto distósico vaginal\t20 04 113\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía Traumatológica\tFractura expuesta Brazo, antebrazo,  muslo y pierna, c/u\t21 04 010\tEPH \tactual\t\tHospital \tNO\t
Adulto/Infantil\tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tIntervenciones Quirúrgicas y Procedimientos \tCirugía Traumatológica\tFractura expuesta De mano o pié, c/u\t21 04 011\tEPH \tactual\t\tHospital \tNO\t
Infantil \tAtención de urgencia\tUnidad de Emergencia Hospitalaria \tConsulta o control Médico de Especialidad\tPediatría \tAtención médica del recién nacido en sala de parto o pabellón quirúrgico c/s reanimación cardio-respiratoria\t01 01 007\tEPH \tactual\t\tHospital \tNO\t
USUARIO \tMACROPROCESO\tPROCESO (UNIDAD O SERVICIO)\tSUBPROCESO (TIPO DE PRESTACIÓN)\tESTAMENTO O ESPECIALIDAD\tPRESTACIÓN\tCÓDIGO MAI\tPRESTACIÓN EPH\tPRESTACIÓN ACTUAL\tPRESTACIÓN NUEVA\tÁREA DE INFLUENCIA\tCOMPRA DE SERVICIO\tOBSERVACIONES
Adulto\tAtención abierta\tCAE\tConsulta o control Médico de Especialidad\tMedicina Interna\tConsulta Médica de Especialidad en Medicina Interna\t0101307\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tAtención abierta\tCAE\tConsulta o control Médico de Especialidad\tCardiología\tConsulta Médica de Especialidad en Cardiología \t0101301\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tConsulta o control Médico de Especialidad\tCirugía General\tConsulta Médica de Especialidad en Cirugía General \t0101312\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tConsulta o control Médico de Especialidad\tNeurología Adulto \tConsulta Médica de Especialidad en Neurología Adulto \t0101209\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tConsulta o control Médico de Especialidad\tOftalmología \tConsulta Médica de Especialidad en Oftalmología \t0101204\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tConsulta o control Médico de Especialidad\tDermatología \tConsulta Médica de Especialidad en Dermatología \t0101201\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tAtención abierta\tCAE\tConsulta o control Médico de Especialidad\tOtorrinolaringología \tConsulta Médica de Especialidad en Otorrinolaringología \t0101205\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tConsulta o control Médico de Especialidad\tEnfermedades Respiratorias del Adulto \tConsulta Médica de Especialidad en Enfermedades Respiratorias del Adulto \t0101321\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tConsulta o control Médico de Especialidad\tTraumatología y Ortopedia \tConsulta Médica de Especialidad en Traumatología y ortopedia \t0101310\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tConsulta o control Médico de Especialidad\tGastroenterología Adulto \tConsulta Médica de Especialidad en Gastroenterología Adulto \t0101323\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tConsulta o control Médico de Especialidad\tObstetricia y Ginecología \tConsulta Médica de Especialidad en Obstetricia y Ginecología\t0101308\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tCAE\tConsulta o control Médico de Especialidad\tAnestesiología \tConsulta Médica de Especialidad en Anestesiología \t0101329\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tConsulta o control Médico de Especialidad\tNeurocirugía \tConsulta Médica de Especialidad en Neurocirugía \t0101203\tEPH\t\tNueva \tHospital\tSI\tSe estima inicio de atenciones consultas nuevas a partir de diciembre 2023
Adulto\tAtención abierta\tCAE\tConsulta o control Médico de Especialidad\tReumatología \tConsulta Médica de Especialidad en Reumatología  \t0101206\tEPH\t\tNueva \tHospital\tSI\tSe estima inicio en Noviembre 2023
Infantil \tAtención abierta\tCAE\tConsulta o control Médico de Especialidad\tPediatría \tConsulta Médica de Especialidad en Pediatría \t0101309\tEPH\tactual\t\tHospital\tNO\t
Infantil \tAtención abierta\tCAE\tConsulta o control Médico de Especialidad\tNeurología Pediátrica \tConsulta Médica de Especialidad en Neurología Pediátrica\t0101210\tEPH\tactual\t\tHospital\tNO\t
Infantil \tAtención abierta\tCAE\tConsulta o control Médico de Especialidad\tCirugía Pediátrica \tConsulta Médica de Especialidad en Cirugía Pediátrica\t0101317\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tConsulta o control Médico de Especialidad\tMedicina General \tConsulta Médica de Especialidad en Medicina General \t0101001\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil \tAtención abierta\tCAE\tConsulta o control Médico de Especialidad\tMedicina General \tVisita a domicilio por médico \ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tConsulta o control por Profesional no Médico\tEnfermera \tVisita a domicilio por enfermera\t0104004\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tConsulta o control por Profesional no Médico\tAuxikliar de Enfermería \tVisita a domicilio por Auxiliar de enfermería \t0104003\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tAtención abierta\tCAE\tConsulta o control por Profesional no Médico\tNutricionista\tConsulta o control por Nutricionista\t0102010\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tAtención abierta\tCAE\tConsulta o control por Profesional no Médico\tEnfermera \tConsulta o control por Enfermera \t0102008\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tAtención abierta\tCAE\tConsulta o control por Profesional no Médico\tMatrona \tConsulta o control por Matrona \t0102009\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tAtención abierta\tCAE\tConsulta o control por Profesional no Médico\tFonoaudiologo \tConsulta o control por Fonoaudiólogo \t0102005\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tAtención abierta\tCAE\tConsulta o control por Profesional no Médico\tAuxikliar de Enfermería \tConsulta o control por Auxiliar de Enfermería \t0102003\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tConsulta o control por Profesional no Médico\tKinesiólogo \tEvaluación kinesiológica integral \t0601101\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tConsulta o control por Profesional no Médico\tKinesiología\tAtención kinesiológica integral ambulatoria\t0601105\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tConsulta o control por Profesional no Médico\tTerapéuta Ocupacional \tAtención integral de terapia ocupacional\t0602001\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tConsulta o control por Profesional no Médico\tTerapéuta Ocupacional \tIntervención de terapia ocupacional en ayudas técnicas y tecnología asistida\t0602002\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tConsulta o control por Profesional no Médico\tTerapéuta Ocupacional \tIntervención terapia ocupacional en actividades de la vida diaria, básicas, instrumentales y avanzadas\t0602003\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tConsulta o control por Profesional no Médico\tPsicólogo\tConsulta o control por psicólogo clínico\t0903002\t\t\t\t\t\t
Adulto\tAtención abierta\tCAE\tConsulta o control por Profesional no Médico\tAsistente Social \tConsulta de salud mental por otros profesionales\t0903003\t\t\t\t\t\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tNeurología y Neurocirugía \tE.E.G. de 16 o más canales (incluye el cód. 11-01-006)\t1101004\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tNeurología y Neurocirugía \tEEG en vigilia, sueño y post-privación de sueño. Equipo de 16 o mas canales\t1101041\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tNeurología y Neurocirugía \tElectromiografías cualquier región, por ej.: músculos faciales, faringe, paravertebrales, vejiga y periné, test  de miastenia (incluye el estudio clínico y muestreo suficientes para diagnosticar naturaleza del trastorno y estado evolutivo), c/u\t1101010\tEPH\t\tNueva \tHospital\tSI\tPrestación bajo modalidad compra servicio desde el
Adulto\tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tNeurología y Neurocirugía \tVelocidad de conducción nerviosa (incluye reflejo H, onda F y otros)\t1101012\tEPH\t\tNueva \tHospital\tSI\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tCuración simple\t\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tCuretaje de lesiones virales y similares hasta 10 lesiones por sesión\t1601110\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tAplicación de inmunoduladores, quimicos y similares hasta 10 lesiones por sesion.\t1601111\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tCrioterapia hasta 5 lesiones por sesión\t1601116\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tCrioterapia 6 a 10 lesiones por sesión\t1601117\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tCriocirugía en tumor maligno (por cada lesión) por sesión\t1601118\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tInyección intracutánea en áreas hasta 9 cm2 por sesión\t1601119\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tTratamiento abrasivo cutáneo químico por sesión\t1601121\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tBiopsia de piel y/o mucosa por curetaje o sección tangencial c/s electro por 1 lesión\t1602201\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tBiopsia de piel y/o mucosa por curetaje o sección tangencial c/s electro x 1 lesión\t16 02 201\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tExtirpación, reparación o biopsia, total o parcial, de lesiones benignas cutáneas por excisión\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tCabeza, cuello, genitales hasta 3 lesiones: extirpación, reparación o biopsia, total o parcial, de lesiones benignas cutáneas por excisión\t16 02 202\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tResto del cuerpo hasta 3 lesiones: extirpación, reparación o biopsia, total o parcial, de lesiones benignas cutáneas por excisión\t16 02 203\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tCabeza, cuello y genitales desde 4 y hasta 6 lesiones: extirpación, reparación o biopsia, total o parcial, de lesiones benignas cutáneas por excisión\t16 02 204\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tResto del cuerpo desde 4 y hasta 6 lesiones: extirpación, reparación o biopsia, total o parcial, de lesiones benignas cutáneas por excisión\t16 02 205\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tExtirpación de lesiones benignas por sec tangencial, curetaje y/o fulguración hasta 15 lesiones\t16 02 206\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tTratamiento por electro de hemangiomas o telangectasias hasta 15 lesiones\t16 02 207\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tTumor maligno por excisión total o parcial, con o sin sutura, por cada lesión\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tCabeza, cuello, genitales: tratamiento quirúrgico de tumor maligno por escisión total o parcial, con o sin sutura, por cada lesión o melanoma cualquier localización\t16 02 211\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tResto del cuerpo: tratamiento quirúrgico de tumor maligno por escisión total o parcial, con o sin sutura, por cada lesión\t16 02 212\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tAmpliación de márgenes quirúrgicos de tumor maligno extirpado previamente\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tCabeza, cuello, genitales o melanoma cualquier ubicación: ampliación de márgenes quirúrgicos de tumor maligno extirpado previamente \t16 02 213\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tResto del cuerpo: ampliación de márgenes quirúrgicos de tumor maligno extirpado previamente\t16 02 214\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tTumores vasculares profundos Cara, cuero cabelludo, cuello, genitales\t16 02 215\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tTumores Vasculares Profundos Resto del cuerpo\t16 02 216\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tExtirpación de lesión benigna subepidérmica, incluye Tumor sólido, quiste epidérmico y lipoma por lesión\t\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tCabeza, cuello, genitales: extirpación de lesión benigna subepidérmica, incluye tumor sólido, quiste epidérmico y lipoma por lesión \t16 02 223\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tResto del cuerpo: extirpación de lesión benigna subepidérmica, incluye tumor sólido, quiste epidérmico y lipoma por lesión \t16 02 224\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tVaciamiento y curetaje quirúrgico de lesiones quísticas o abscesos\t16 02 225\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tOnicectomía total o parcial simple\t16 02 231\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tCirugía reparadora ungueal por proceso inflamatorio\t16 02 232\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tCorrección quirúrgica de defecto congénito o por tumor ungueal\t16 02 233\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tIntervenciones Quirúrgicas y Procedimientos \tDermatología y Tegumentos \tExtirpación, reparación o biopsia, total o parcial, de lesiones benignas cutáneas por excisión\t1602201\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Dermatología \tDermatología y Tegumentos \tTest de Parche Standard y bateria oral (Dermatologia)\t0307005\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tCardiología \tE.C.G. de reposo (incluye mínimo 12 derivaciones y 4 complejos por derivación)\t1701001\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tCardiología \tE.C.G. continuo (test Holter o similares, por ej. variabilidad de la frecuencia cardíaca y/o alta resolución del ST y/o depolarización tardía); 20 a 24 horas de registro\t1701006\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tCardiología \tEcocardiograma Doppler, con registro (incluye cod 1701008) \t1701007\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tCardiología \tTest de Esfuerzo (electrocardiograma de esfuerzo) \t1701003\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tCardiología\tEcocardiograma bidimensional doppler color\t1701045\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tCardiología\tMonitoreo de presión arterial continuo\t1701009\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos del Aparato Respiratorio \tBroncopulmonar \tEspirometría Basal \t1707001\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos del Aparato Respiratorio \tBroncopulmonar \tEspirometría Basal y con broncodilatador\t1707002\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos del Aparato Respiratorio \tBroncopulmonar \tProvocación con ejercicio, test de\t1707004\tEPH\t\tNueva \tHospital\tNO\tCapacitación de profesional para iniciar en año 2024
Adulto\tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos del Aparato Respiratorio \tBroncopulmonar \tLaringotraqueobroncoscopía con fibroscopio\t1707021\tEPH\t\tNueva \tHospital\t\tProyecto de adquisición del equipo para 2024
Adulto\tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos del Aparato Respiratorio \tBroncopulmonar \tBroncoaspiración, c/s lavado y/o colocación de medicamentos por sonda traqueobronquial (proc. aut.)\t1707027\tEPH\t\tNueva \tHospital\t\tProyecto de adquisición del equipo para 2025
Adulto\tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos del Aparato Respiratorio \tBroncopulmonar \tToracocentesis evacuadora, c/s toma de muestras c/s inyección de medicamentos  \t1707029\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos del Aparato Respiratorio \tBroncopulmonar \tFibrobroncoscopía con biopsia transbronquial\t1707061\tEPH\t\tNueva \tHospital\t\tProyecto de adquisición del equipo para 2025
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos del Aparato Respiratorio \tBroncopulmonar \tProcedimiento para determinar gasometría arterial en reposo y ejercicio \t1707025\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos del Aparato Respiratorio \tBroncopulmonar \tSaturación de O2 en reposo y/o ejercicio (con oxímetro) \t1707054\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos del Aparato Respiratorio \tBroncopulmonar \tSaturación de O2 en reposo y ejercicio y O2 100% (con oxímetro) \t1707055\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tUrología y Nefrología \tVaciamiento vesical por sonda uretral, (proc. aut.)\t1901022\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos de Inmovilización \tTraumatología y Ortopedia \tRodillera, bota larga o corta de yeso\t2105004\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos de Inmovilización \tTraumatología y Ortopedia \tVelpeau\t2105005\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos de Inmovilización \tTraumatología y Ortopedia \tYeso antebraquial c/s férula digital\t2105006\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos de Inmovilización \tTraumatología y Ortopedia \tYeso braquicarpiano\t2105007\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos de Inmovilización \tTraumatología y Ortopedia \tRodillera, bota larga o corta de yeso\t2105004\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos de Inmovilización \tTraumatología y Ortopedia \tVelpeau\t2105005\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos de Inmovilización \tTraumatología y Ortopedia \tYeso antebraquial c/s férula digital\t2105006\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos de Inmovilización \tTraumatología y Ortopedia \tYeso braquicarpiano\t2105007\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos de Inmovilización \tTraumatología y Ortopedia \tYeso pelvipedio bilateral\t2105008\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos de Inmovilización \tTraumatología y Ortopedia \tYeso pelvipedio unilateral\t2105009\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos de Inmovilización \tTraumatología y Ortopedia \tLuxaciones de articulaciones menores (el resto)\t2107003\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Inmovilización \tTraumatología y Ortopedia \tInfiltración local medicamentos (bursas, tendones, yuxtaarticulares y/o intraarticulares), y/o punción evacuadora c/s toma de muestra (en interfalángicas comprende hasta dos por sesión)\t2101001\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Inmovilización \tTraumatología y Ortopedia \tColocación de Yeso – Luxaciones de articulaciones medianas (hombro, codo, rodilla, tobillo. Muñeca, tarso y esterno-clavicular\t21 07 001\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tConsulta o control por Profesional no Médico\tTecnólogo Médico \tConsulta por Tecnólogo médico de Oftalmología\t01 02 001\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tTecnólogo Médico \tCampimetría de proyección, unilateral (proc.aut.)\t1201001\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tTecnólogo Médico \tCampimetría computarizada, unilateral \t1201042\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tTecnólogo Médico \tCurva de tensión aplanática (por cada día), unilateral\t1201004\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tTecnólogo Médico \tPerimetría de Goldman o perimetría cinética, unilateral\t1201010\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tCuerpo extraño conjuntival y/o corneal en adultos\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tCuerpo extraño conjuntival y/o corneal en niños\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tVía lagrimal, cateterismo o sondaje en adultos\t12 01 031\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tVía lagrimal, cateterismo o sondaje en lactantes\t12 01 032\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tVía lagrimal, cateterismo o sondaje en niños\t12 01 033\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tCriocoagulación conjuntival, corneal o palpebral en adultos\t12 01 035\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tCriocoagulación conjuntival, corneal o palpebral en niños\t12 01 036\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tGlaucoma, ciclodiatermia y/o ciclocrioterapia\t12 01 037\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tInyección retrobulbar\t12 01 038\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tPestañas, extirp. por electrocoagulación (cualquier número)\t12 01 039\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tPuntos lagrimales; electrotermocoagulación\t12 01 040\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tAngiografía de retina o de iris, (con fluoresceína o sim.), c/ojo\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tTomografía coherencia óptica, c/ ojo \ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tCampimetría de proyección, c/ojo (proc.aut.)\t12 01 001\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tCampimetría computarizada, c/ojo\t12 01 042\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tCuantificación de lagrimación (test de   Schirmer),  uno o ambos ojos\t12 01 003\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tDiploscopia cuantitativa, ambos ojos\t12 01 005\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tExploración sensoriomotora: estrabismo, estudio completo, ambos ojos\t12 01 009\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tPruebas de provocación para glaucoma (prueba de oscuridad u otras), uno o ambos ojos\t12 01 011\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tTonometría aplanática c/ojo \t12 01 014\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tTratamiento ortóptico y/ o pleóptico (por sesión), ambos ojos\t12 01 015\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tExamen Optométrico c/s Prescripción de Lentes\t12 01 027\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tToma agudeza visual (ambos ojos)\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tAutorefractometria\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tLensometria\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tBiomicroscopía ocular\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tExamen de visión cromática\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos de Oftalmología \tOftalmología \tEcobiometría con cálculo de lente intraocular, bilateral\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tFonoaudiología \tEvaluación de voz\t1303001\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tFonoaudiología \tEvaluación de habla\t1303002\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tFonoaudiología \tEvaluación del lenguaje (incluye voz, habla y aspecto semántico, sintáctico y fonológico, etc. e informe) (incluye 3 sesiones de mínimo 30')\t1303003\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tFonoaudiología \tRehabilitación de la voz \t1303004\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tFonoaudiología \tRehabilitación del habla y/o del lenguaje (máximo 30 sesiones anuales)(cada sesión mínimo 30')      \t1303005\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tFonoaudiología \tRehabilitación de la deglución\t1303006\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tFonoaudiología \tEvaluación clínica de la deglución \t1303007\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tEducación de Grupo \tAsistente Socia \tEducación de grupo por asistente social\t0103003\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tEducación de Grupo \tAuxikliar de Enfermería \tEducación de grupo por auxiliar de enfermería\t0103004\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tEducación de Grupo \tEnfermera\tEducación de grupo por enfermera\t0103005\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tEducación de Grupo \tMatrona \tEducación de grupo por matrona \t0103006\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tEducación de Grupo \tNutricionista\tEducación de grupo por nutricionista\t0103007\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tMisceláneos \tEnfermera\tCuración simple ambulatoria\t0106002\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tMisceláneos \tEnfermera/TENS\tReacción Cutánea a Alergenos  (incluye el valor de los alergenos)\t03 07 005\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tMisceláneos \tEnfermera\tPuncion Arterial y Venosa (toma de muestras)\t03 07 023\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención abierta\tCAE\tMisceláneos \tEnfermera\tManejo avanzado de heridas (pie diabetico, ulcera venosa, otros)\t03 07 024\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tMisceláneos \tEnfermera\tcuracion avanzada de heridas (enfermera)\t50 99 111\tEPH\tactual\t\tHospital \tNO\t
Adulto\tAtención abierta\tCAE\tMisceláneos \tEnfermera\tTratamiento ulcera venosa, curación pacientes herida tipo 1 y 2 (A) no infectados (enfermera)\t25 05 438\tEPH\tactual\t\tHospital \tNO\t
Adulto\tAtención abierta\tCAE\tMisceláneos \tEnfermera\tTratamiento ulcera venosa, curación pacientes herida tipo 3 y 4 (B) infectados (enfermera)\t25 05 439\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tMisceláneos \tEnfermera\tCuración de Quemados – 5% (enfermera)\tS/C\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tMisceláneos \tEnfermera\tCuración de Quemados + 5% (enfermera)\tS/C\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tNasofaringolaringofibroscopia\t13 01 003\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tRinoscopia posterior, con nasofaringoscopia c/s toma de muestras  (proc. aut.)\t13 01 004\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tLaringoscopia y/o traqueoscopia directa c/s toma de muestra, c/s biopsia. Con microscopio\t13 01 006\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tLaringoscopia y/o traqueoscopia directa c/s toma de muestra, c/s biopsia. Sin microscopio\t13 01 007\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tTecnólogo Médico \tAudiometría  en adultos\t13 01 021\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tTecnólogo Médico \tAudiometría niños\t13 01 008\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tTecnólogo Médico \tImpedanciometría\t13 01 009\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tTecnólogo Médico \tCalibración de audífonos o implantes\t13 01 010\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tTecnólogo Médico \tPotenciales evocados auditivos de tronco cerebral clínicos\t13 01 011\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tTecnólogo Médico \tFunción tubaria\t13 01 016\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tTecnólogo Médico \tPrueba calórica o prueba calórica mínima (proc.aut.)\t13 01 017\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tTecnólogo Médico \tExamen funcional de VIII par\t13 01 020\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tBiopsia oído (proc. aut.)\t13 01 044\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tNasofibroscopía de la deglución\t13 01 047\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tEvaluacion de la voz (incluye respiracion, tonicidad     \t13 03 001\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tEvaluacion del habla (incluye articulacion, prosodia,     \t13 03 002\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tEvaluacion del lenguaje (incluye voz, habla y aspecto   \t13 03 003\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tSenos perinasales, punción evacuadora c/s toma de muestras, c/s inyección de medicamentos; cada punción\t13 01 024\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \t** Taponamiento anterior (proc. aut.)\t13 01 025\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \t** Taponamiento posterior\t13 01 026\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tVasos y/o cornetes, electrocauterización (uni o bilateral)\t13 01 028\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tCuerpo extraño en fosas nasales, extraccion en adultos        \t13 01 029\tEPH\tactual\t\tHospital \tNO\t
Adulto/Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tCuerpo extraño en fosas nasales, extraccion en niños        \t13 01 030\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tCuerpo extraño en laringe y/o traquea, extraccion de (incluyela endoscopia con tubo rigido): En adultos\t13 01 035\tEPH\tactual\t\tHospital \tNO\t
Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tCuerpo extraño en laringe y/o traquea, extraccion de (incluyela endoscopia con tubo rigido): En ninos\t13 01 036\tEPH\tactual\t\tHospital \tNO\t
Infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tCuerpo extraño extracción en hipofaringe y/o esófago (por tubo rígido) - En niños\t13 01 038\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tCuerpo extraño extracción en hipofaringe y/o esófago (por tubo rígido) - En adultos\t13 01 039\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tLesiones del oido externo y/o medio, curacion bajo micros\t13 01 040\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tExtracción de cuerpo extraño en oido, (incluye tapón de cerumén) (proc. Aut.) en adultos                                                                             \t13 01 042\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tExtracción de cuerpo extraño en oido, (incluye tapón de cerumén) (proc. Aut.) en niños                                                                            \t13 01 043\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tEmisiones Otoacústicas \t13 01 045\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tRetiro de tubos de ventilación timpánica, uni o bilateral\t13 01 051\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tPotenciales electromiogénicos vestibulares cervicales u oculares\t13 01 052\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tRehabilitacion de la voz (maximo 15 sesiones anuales)  (cada sesion minimo 30'') (Fonoaudiológo)\t13 03 004\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tRehabilitacion del habla y/o del lenguaje (maximo 30 sesiones anuales) (cada sesion minimo 30'') (Fonoaudiológo)\t13 03 005\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tTratamiento rehabilitador/habilitador directo e indirecto de la deglución\t13 03 006\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tRetiro de taponaje anterior\t50 99092\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tRetiro de yeso\t50 99 093\tEPH\tactual\t\tHospital \tNO\t
Adulto/infantil \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tCambio de canula traqueostomia (enfermera Otorrino)\t50 99 094\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tOtorrinolaringología \tEstroboscopia\t50 99 095\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tTecnólogo Médico \tRehabilitación vestibular\ts/c\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tTecnólogo Médico \tManiobras de reposición vestibular \ts/c\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tEvaluación kinesiológica: muscular, articular, postural, neurológica y funcional (máximo 2 por tratamiento)\t06 01 001\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tEvaluación Biomecánica instrumental\t06 01 003\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tEvaluación de la deglución\t01 02 503\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tEvaluación de funciones cognitivas\t01 02 505\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tCurva dosis respuesta a broncodilatadores.\t17 07 051\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tPiscina temperada (incluye ejercicios) (proc.aut.)\t06 01 004\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tRadiación infrarroja, horno, baño parafina, compresas húmedas, c/u (proc.aut.)\t06 01 005\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tTanque de Hubbard con ejercicios (hiper o hipo-termal sobre 1.000 lts de capacidad) (proc.aut.)\t06 01 006\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tTurbión, tanque con remolino (hiper o hipotermal,baño de contraste) (proc.aut.)\t06 01 007\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tTerapia por radiación ultravioleta. (proc.aut.)\t06 01 010\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tLaserterapia (proc.aut.)\t06 01 008\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tOnda corta (ultratermia), microondas, c/u (proc.aut.)\t06 01 009\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tTerapia por ondas mecánicas (proc. aut.)\t06 01 011\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tAnalgesia transcutánea (TENS) (proc.aut.)\t06 01 012\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tEstimulación eléctrica (interferencial, diadinámicas, exponenciales, galvánica, faradica, ultraexcitante) (proc.aut.)\t06 01 013\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \t Iontoforesis (proc.aut.)\t06 01 014\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tRetroalimentación neuromuscular (miofeedback) (proc.aut.)\t06 01 015\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tCompresión neumática (masaje compresivo) (proc.aut.)\t06 01 016\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tTracción cervical y/o lumbar (mecánica o manual) (proc.aut.)\t06 01 027\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tAtención kinesiológica integral\t06 01 029\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tEjercicios respiratorios y procedimientos de kinesiterápia torácica (ventilación pulmonar localizada, estimulación de la tos, bloqueos torácicos, vibraciones, percusiones y tapoteos) (proc.aut.)\t06 01 017\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tEntrenamiento cardiorespiratorio funcional\t06 01 028\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tPrueba de esfuerzo o Entrenamiento ergométrico (porc.aut.)\t06 01 018\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tEntrenamiento funcional con ayudas técnicas (órtesis, ayudas de desplazamiento, etc.) (proc.aut.)\t06 01 019\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tEntrenamiento protésico extremidades (proc.aut.)\t06 01 020\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tManipulación osteopática (liberación articular, manipulación vertebral) (proc.aut.)\t06 01 021\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tMasoterapia, por sesión (proc.aut.)\t06 01 022\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tOrientación y entrenamiento de personas con baja visión o con ceguera (proc.aut.)\t06 01 023\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tReeducación motriz (ejercicios terapéuticos para recuperación muscular, capacidad de trabajo, coordinación, gimnasia ortopédica, reeducación funcional, de marcha) (individual y por sesión, mínimo 30 minutos) (proc.aut.)\t06 01 024\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tTécnicas de facilitación, técnicas de inhibición  (Kabat y/o Bobath) (proc.aut.)\t06 01 025\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tTécnicas de relajación (entrenamiento autógeno Schultz - Jacobson o similar) (proc.aut.)\t06 01 026\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tEntrenamiento ortostático en mesa basculante\t06 01 181\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta\tCAE\tProcedimientos Diagnósticos y Terapéuticos  \tRehabilitación \tReeducación de la tos y respiración en pacientes con traqueostomía\t01 02 501\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta \tTelemedicina \tTeleconsulta\tMedicina General \tTeleconsulta Medicina General\t0108001\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta \tTelemedicina \tTeleconsulta\tDermatología \tTeleconsulta Médica de Especialidad en Dermatología\t0108201\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta \tTelemedicina \tTeleconsulta\tNeurología Adulto \tTeleconsulta Médica de Especialidad en Neurología Adultos\t0108209\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta \tTelemedicina \tTeleconsulta\tCardiología \tTeleconsulta Médica de Especialidad en Cardiología\t0108301\tEPH\t\tNueva \tHospital \tNO\tSe dará inicio con llegada de especialista nuevo desde diciembre 2023
Adulto \tAtención abierta \tTelemedicina \tTeleconsulta\tMedicina Interna \tTeleconsulta Médica de Especialidad en Medicina Interna\t0108307\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta \tTelemedicina \tTeleconsulta\tObstetricia y Ginecología \tTeleconsulta Médica de Especialidad en Obstetricia y Ginecología\t0108308\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta \tTelemedicina \tTeleconsulta\tTraumatología y Ortopedia \tTeleconsulta Médica de Especialidad en Traumatología y Ortopedia\t0108310\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta \tTelemedicina \tTeleconsulta\tEnfermedades Respiratorias del Adulto \tTeleconsulta Médica de Especialidad en Enfermedades Respiratorias Adulto\t0108321\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta \tTelemedicina \tTeleconsulta\tGastroenterología \tTeleconsulta Médica de Especialidad en Gastroenterología Adulto\t0108323\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta \tTelemedicina \tTeleinterconsulta (Telemedicina) \tMedicina \tTeleinterconsulta médica\t0109001\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta \tTelemedicina \tTeleinterconsulta (Telemedicina) \tProfesionales No Médicos \tTeleinterconsulta no médica\t0109002\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta \tTelemedicina \tTelerehabilitación \tKinesiología \tTelerehabilitación: Evaluación Kinesiológica Integral\t0608101\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta \tTelemedicina \tTelerehabilitación \tKinesiología \tTelerehabilitación: Atención Kinesiológica Integral \t0608102\tEPH\tactual\t\tHospital \tNO\t
Adulto \tAtención abierta \tTelemedicina \tTelerehabilitación \tTerapéuta Ocupacional \tTelerehabilitación: Atención integral de terapia ocupacional\t0608201\tEPH\t\tNueva \tHospital \tNO\t
Adulto \tAtención abierta \tTelemedicina \tTelerehabilitación \tTerapéuta Ocupacional \tTelerehabilitación: Intervención de terapia ocupacional en ayudas técnicas y tecnología asistida\t0608202\tEPH\t\tNueva \tHospital \tNO\t
Adulto \tAtención abierta \tTelemedicina \tTelerehabilitación \tTerapéuta Ocupacional \tTelerehabilitación: Intervención terapia ocupacional en actividades de la vida diaria, básicas, instrumentales y avanzadas\t0608203\tEPH\t\tNueva \tHospital \tNO\t
USUARIO \tMACROPROCESO\tPROCESO (UNIDAD O SERVICIO)\tSUBPROCESO (TIPO DE PRESTACIÓN)\tESTAMENTO O ESPECIALIDAD\tPRESTACIÓN\tCÓDIGO MAI\tPRESTACIÓN EPH\tPRESTACIÓN ACTUAL\tPRESTACIÓN NUEVA\tÁREA DE INFLUENCIA\tCOMPRA DE SERVICIO\tOBSERVACIONES
Adulto\tAtención Cerrada\tUCI Adulto\tHospitalización\tCama Crítica\tDía cama hospitalización integral adulto en Unidad de Cuidado Intensivo (U.C.I.) \t0203002\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUTI Adulto\tHospitalización\tCama Crítica\tDía cama hospitalización integral adulto en Unidad de Tratamiento Intermedio (U.T.I)\t02 03 005\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tConsulta Médica de Especialidad en Medicina Interna\t01 01 307\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tConsulta Médica de Especialidad en Cirugía General \t01 01 312\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tConsulta Médica de Especialidad en Medicina General\t01 01 001\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tConsulta Médica de Especialidad en Obstetricia y Ginecología \t01 01 308\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tConsulta Médica de Especialidad en Neurología Adulto\t01 01 209\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tConsulta Médica de Especialidad en Anestesiología \t01 01 329\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tConsulta Médica de Especialidad en Traumatología \t01 01 310\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tConsulta o control por Enfermera \t01 04 004\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tConsulta o control por Auxiliar de Enfermería \t01 02 003\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tConsulta o control por Nutricionista\t01 02 010\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tRadiografía de tórax  frontal o lateral con equipo móvil fuera del departamento de rayos.\t04 01 008\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tEcografía como apoyo a cirugía, o a procedimiento (de tórax, muscular, partes blandas, etc.)\t04 04 004\tEPH\t\tnueva \tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tPunción lumbar c/s manometria c/s queckensted   \t11 01 003\tEPH\t\tnueva \tHospital\tNO\t
Infantil \tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tBloqueo nervio periférico en punto motor\t11 01 026\tEPH\tactual\t\tHospital\tNO\t
Infantil \tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tBloqueo nervio troncular\t11 01 027\tEPH\tactual\t\tHospital\tNO\t
Infantil \tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tInfiltraciones o bloqueo de ramas del trigemino o del facial\t11 01 028\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tInfiltraciones o bloqueo epidural, cervical, lumbar o similares, cada sesión\t11 01 030\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tInfiltraciones o bloqueo intercostales (cualquier numero)\t11 01 031\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tInyeccion toxina botulinica\t50 99 018\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tInfiltración intramuscular (Fenol y Toxina Botulínica)\t50 99 112\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tBloqueo neuromuscular con anestésico (manejo del dolor)\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tEscarectomía hasta 1 % superficie corporal\t15 02 063\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tEscarectomía hasta 5 % superficie corporal\t15 02 064\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tE.C.G. de reposo (incluye mínimo 12 derivaciones y 4 complejos por derivación)\t17 01 001\tEPH\tactual\t\tHospital\tNO\t
Adulto/infantil\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tE.C.G. continuo (test Holter o similares, por ej. variabilidad de la frecuencia cardíaca y/o alta resolución del ST y/o depolarización tardía); 20 a 24 horas de registro                                                             \t17 01 006\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tEcocardiograma bidimensional doppler color\t17 01 045\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tMonitoreo continuo de presion arterial                                                                         \t17 01 009\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tCardioversion\t17 01 034\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tColocación marcapaso transitorio,sonda (proc. completo)\t17 01 035\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tDesfibrilacion\t17 01 036\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tPuncion subclavia o yugular con colocacion de cateter venoso central\t17 01 037\tEPH\tactual\t\tHospital\tNO\t
Adulto/Infantil \tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tInstalación cateter Arterial\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tMonitorización Cardíaca invasiva\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tDenudación venosa (proc. aut.)\t17 03 023\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tLaringotraqueobroncoscopia con fibroscopio\t17 07 021\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tSaturacion de O2 en reposo y/o ejercicio (con oximetro)\t17 07 054\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tToracocentesis evacuadora,c/s toma de muestras\t17 07 029\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tAerosolterapia con aire comprimido y oxigeno (en atencion cerrada, incluida en valor dia cama)    \t17 07 030\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tBiopsia pleural (con aguja)\t17 07 032\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tIntubacion traqueal (proc. Aut.)\t17 07 037\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tTrombólisis arterial periférica\t17 01 039\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tVentilación mecánica invasiva \ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tVentilación mecánica no invasiva \ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tCánula de alto flujo \ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tAtención Kinesiológica Integral UPC (Intensivo e Intermedio) \t0601104\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tAtención integral de terapia ocupacional\t0602001\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tConsulta o control por Fonoaudiólogo \t0102005\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tAtención kinesiológica integral, al enfermo hosp. en UTI o Intermedio (máx. 1 diaria)\t06 01 031\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tAsistencia en IOT, VMNI, cambio de cánula de traqueostomía\t06 01 171\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tUCI-UTI Adulto\tHospitalización\tCama Crítica\tReeducación de la tos y respiración en pacientes con traqueostomía\t01 02 501\tEPH\tactual\t\tHospital\tNO\t
USUARIO \tMACROPROCESO\tPROCESO (UNIDAD O SERVICIO)\tSUBPROCESO (TIPO DE PRESTACIÓN)\tESTAMENTO O ESPECIALIDAD\tPRESTACIÓN\tCÓDIGO MAI\tPRESTACIÓN EPH\tPRESTACIÓN ACTUAL\tPRESTACIÓN NUEVA\tÁREA DE INFLUENCIA\tCOMPRA DE SERVICIO\tOBSERVACIONES
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica \tDia Cama de Hospitalización Integral Cuidados Básicos\t0201010\tEPH\tactual\t\tHospital\tNO\tX
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Media \tDia Cama de Hospitalización Integral Cuidados Medios\t0201110\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina Adulto\tHospitalización\tCama Básica/Media\tConsulta Médica de Especialidad en Medicina Interna\t01 01 307\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tCirugía Adulto\tHospitalización\tCama Básica/Media\tConsulta Médica de Especialidad en Cirugía General \t01 01 312\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía Adulto\tHospitalización\tCama Básica/Media\tConsulta Médica de Especialidad en Medicina General\t01 01 001\tEPH\tactual\t\tHospital\tNO\tx
Adulto\tAtención Cerrada\tTraumatología Adulto\tHospitalización\tCama Básica/Media\tConsulta Médica de Especialidad en Traumatología \t01 01 310\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tConsulta Médica de Especialidad en Neurología Adulto \t01 01 209\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tConsulta o control por Enfermera \t01 04 004\tEPH\tactual\t\tHospital\tNO\tX
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tConsulta o control por Auxiliar de Enfermería \t01 02 003\tEPH\tactual\t\tHospital\tNO\tX
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tConsulta o control por Nutricionista\t0102010\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tConsulta o control por Fonoaudiólogo \t0102005\tEPH\tactual\t\tHospital\tNO\tX
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tAtención Kinesiológica Integral en Pacientes hospitalizados\t0601103\tEPH\tactual\t\tHospital\tNO\tX
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tAtención integral de terapia ocupacional\t0602001\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina Adulto\tHospitalización\tCama Básica/Media\tPunción lumbar c/s manometria c/s queckensted   \t11 01 003\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tE.E.G. de 16 o más canales (incluye el cód.11-01-006)\t11 01 004\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina Adulto\tHospitalización\tCama Básica/Media\tElectroencefalograma (E.E.G.) standard y/o activado "sin privación de sueño" (incluye mono y bipolares, hiperventilación, c/s reactividad auditiva, visual, lumínica, por drogas u otras ). Equipo de 8 canales\t11 01 006\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina Adulto\tHospitalización\tCama Básica/Media\tE.E.G. Post-privacion de sueno (incluye codigo 11-01-006). Equipo de 8 canales\t11 01 040\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina Adulto\tHospitalización\tCama Básica/Media\tE.E.G. Post-privacion de sueno (incluye codigo 11-01-004) equipo de 16 o mas canales\t11 01 041\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina Adulto\tHospitalización\tCama Básica/Media\tE.E.G. Digital (con activaciones) 32 canales\t11 01 043\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina Adulto\tHospitalización\tCama Básica/Media\tE.C.G. de reposo (incluye mínimo 12 derivaciones y 4 complejos por derivación)\t17 01 001\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tReanimación  Cardiopulmonar básica -adultos\ts/c\tEPH\tactual\t\tHospital\tNO\tX
Adulto\tAtención Cerrada\tMedicina Adulto\tHospitalización\tCama Básica/Media\tE.C.G. continuo (test Holter o similares, por ej. variabilidad de la frecuencia cardíaca y/o alta resolución del ST y/o depolarización tardía); 20 a 24 horas de registro                                                             \t17 01 006\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tEcocardiograma bidimensional doppler color\t17 01 045\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tMonitoreo continuo de presion arterial                                                                         \t17 01 009\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tCardioversion\t17 01 034\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina Adulto\tHospitalización\tCama Básica/Media\tColocación marcapaso transitorio,sonda (proc. completo)\t17 01 035\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tDesfibrilacion\t17 01 036\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tPuncion subclavia o yugular con colocacion de cateter\t17 01 037\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tSaturacion de O2 en reposo y/o ejercicio (con oximetro)\t17 07 054\tEPH\tactual\t\tHospital\tNO\tx
Adulto\tAtención Cerrada\tMedicina/Cirugía Adulto\tHospitalización\tCama Básica/Media\tToracocentesis evacuadora,c/s toma de muestras\t17 07 029\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tAerosolterapia con aire comprimido y oxigeno (en atencion cerrada, incluida en valor dia cama)    \t17 07 030\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tIntubacion traqueal (proc. Aut.)\t17 07 037\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía Adulto\tHospitalización\tCama Básica/Media\tInstalación drenaje Pleural\ts/c \tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía Adulto\tHospitalización\tCama Básica/Media\tIntubación sonda de Sengstaken\t18 01 022\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tIntubación con sonda gástrica\t18 01 023\tEPH\tactual\t\tHospital\tNO\tx
Adulto\tAtención Cerrada\tMedicina Adulto\tHospitalización\tCama Básica/Media\tIntubación con sonda de Miller-Abbot o de alimentación enteral\t18 01 024\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía Adulto\tHospitalización\tCama Básica/Media\tPunción evacuadora de líquido ascítico, con colocación de expansores de plasma,c/s toma de muestra,c/s inyección de medicamentos (no incluye el valor de los expansores ni otros medicamentos).\t18 01 041\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía Adulto\tHospitalización\tCama Básica/Media\tPunción evacuadora de líquido ascítico\t18 01 048\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía Adulto\tHospitalización\tCama Básica/Media\tVaciamiento manual de fecaloma\t18 01 042\tEPH\tactual\t\tHospital\tNO\tX
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tInstilacion vesical (incluye colocacion de sonda) proc. Aut.                                      \t19 01 019\tEPH\tactual\t\tHospital\tNO\tx
Adulto\tAtención Cerrada\tMedicina/Cirugía Adulto\tHospitalización\tCama Básica/Media\tVac. Vesical p/puncion hipogastrica o cistostomia p/puncion\t19 01 021\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tVaciamiento vesical por sonda uretral, (proc. aut.)\t19 01 022\tEPH\tactual\t\tHospital\tNO\tx
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tInstalación  de sonda vesical\t 50 99 109 \tEPH\tactual\t\tHospital\tNO\tx
Adulto\tAtención Cerrada\tMedicina/Cirugía Adulto\tHospitalización\tCama Básica/Media\tPunción evacuadora de absceso intraabdominales (hepático u otros), c/s toma de muestra, c/s inyección de medicamentos\t18 01 038\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tHemoglucotest\t03 02 047\tEPH\tactual\t\tHospital\tNO\tx
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tCuración simple\t01 06 002\tEPH\tactual\t\tHospital\tNO\tx
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tAdministración de medicamentos por vía: endovenosa, intramuscular, subcutáneo, oral, ocular, ótica, rectal, inhalatoria.\ts/c\tEPH\tactual\t\tHospital\tNO\tx
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tInstalación de vía venosa\ts/c\tEPH\tactual\t\tHospital\tNO\tx
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tToma de muestras de exámenes de sangre venosa\t03 07 011\tEPH\tactual\t\tHospital\tNO\tx
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tToma de muestra arterial en adultos\t03 07 009\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tToma de muestra con técnica aséptica para hemocultivo, c/u\t03 07 013\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tToma de muestra capilar ( adultos, niños y lactantes )\t03 07 014\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía/Traumatología Adulto \tHospitalización\tCama Básica/Media\tCuración avanzada\t50 99 111\tEPH\tactual\t\tHospital\tNO\tx
Adulto\tAtención Cerrada\tMedicina/Cirugía Adulto\tHospitalización\tCama Básica/Media\tTratamiento ulcera venosa, curación pacientes herida tipo 1 y 2 (A) no infectados \ts/c\tEPH\tactual\t\tHospital\tNO\tx
Adulto\tAtención Cerrada\tMedicina/Cirugía Adulto\tHospitalización\tCama Básica/Media\tTratamiento ulcera venosa, curación pacientes herida tipo 3 y 4 (B) infectados \ts/c\tEPH\tactual\t\tHospital\tNO\tx
Adulto\tAtención Cerrada\tMedicina/Cirugía Adulto\tHospitalización\tCama Básica/Media\tCuración de Quemados – 5%\ts/c\tEPH\tactual\t\tHospital\tNO\tx
Adulto\tAtención Cerrada\tMedicina/Cirugía Adulto\tHospitalización\tCama Básica/Media\tCuración de Quemados + 5%\ts/c\tEPH\tactual\t\tHospital\tNO\tx
Adulto\tAtención Cerrada\tMedicina/Cirugía Adulto\tHospitalización\tCama Básica/Media\tEscarectomía- Hasta 1 % superficie corporal\t15 02 063\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tMedicina/Cirugía Adulto\tHospitalización\tCama Básica/Media\tEscarectomía- Hasta 5 % superficie corporal\t15 02 064\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tInfiltracion local medicamentos (bursas, tendones, yuxtaarticulares y/o intraarticulares\t21 01 001\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tInfiltración intraarticular\t50 99 114\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tCalzon corto de yeso\t21 05 001\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tCorbata tipo schantz\t21 05 002\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tMinerva de yeso\t21 05 003\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tRodillera, bota larga o corta de yeso\t21 05 004\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tVelpeau\t21 05 005\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tYeso antebraquial c/s ferula digital\t21 05 006\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tYeso braquicarpiano\t21 05 007\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tYeso pelvipedio bilateral\t21 05 008\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tYeso pelvipedio unilateral\t21 05 009\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tYeso toracobraquial\t21 05 010\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tCorsets de milwaukee o similares (incluye la toma de molde )\t21 05 011\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tCorsets de risser o similares\t21 05 012\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tCorsets de yeso simple (tipo watson jones)\t21 05 013\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tRetiro de yeso\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tLuxaciones de articulaciones medianas (hombro, codo, rodilla, tobillo, muñeca, tarso y esternoclavicular)\t21 07 001\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tLuxaciones de articulaciones  mayores (columna, cadera, pelvis)\t21 07 002\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tLuxaciones de articulaciones menores (el resto)      \t21 07 003\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tFracturas mayores (columna, pelvis, supracondílea, codo, epífisis femorales)\t21 07 004\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tFracturas medianas (diáfisis humeral, radial, cubital, diáfisis femoral, tibial, peroneal, clavicular, platillos tibiales)\t21 07 005\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tFracturas menores (el resto)\t21 07 006\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tTto.funcional c/técnica Sarmiento y similares- Extremidad inferior\t21 07 007\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tTto.funcional c/técnica Sarmiento y similares- Extremidad superior\t21 07 008\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tOrtesis cervicales (collares blandos y duros)\t23 01 002\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tOrtesis Muslo-Pie o Isquiopedio\t23 01 020\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tArnés de Prótesis (Extremidad Superior)\t23 01 021\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tBastón canadiense o trípode, c/u\t23 01 022\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tRodillera\t23 01 024\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tCojín de abducción o Paulik\t23 01 029\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tCorrea de ortesis\t23 01 030\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tCorrea de Muley (Prótesis bajo rodilla)\t23 01 031\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tOrtesis de columna (Milwaukee, Taylor o similares)\t23 01 032\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tOrtesis lumbosacra (Corset de Knight)\t23 01 033\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tOrtesis palmar activa (UCLA)\t23 01 034\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tOrtesis radial de posición\t23 01 035\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tOrtesis corta de posición (digitales) c/u\t23 01 036\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tOrtesis de uso nocturno de miembro inferior\t23 01 037\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tOrtesis Larga de Posición (Extremidad Superior)\t23 01 038\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tMuletas (par)\t23 01 040\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tOrtesis Larga bilateral con cinturón pélvico (Extremidades Inferiores)\t23 01 041\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tOrtesis Larga unilateral (Extremidad Inferior)\t23 01 042\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tOrtesis mano-muñeca pasiva\t23 01 043\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tOrtesis para rodilla\t23 01 044\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tOrtesis tobillo-pie\t23 01 045\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tTalonera goma (par)\t23 01 067\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tOrtesis parálisis cubital\t50 99 074\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tOrtesis tendones flexores\t50 99 075\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tOrtesis digital dinámica\t50 99 076\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tCanaletas  bipedestación\t50 99 065\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tCorreas desrotadoras \t50 99 066\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tCorrea dorsiflexion pie\t50 99 067\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tFérula abducción hombro\t50 99 068\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tFérula extension codo\t50 99 069\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tFérula extension muñeca\t50 99 070\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tFérula flexion muñeca\t50 99 071\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tPalmeta extensión muñeca y dedos\t50 99 072\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tCorreas desrotadoras parálisis braquial obstétrica\t50 99 073\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tCamiseta manga larga \t50 99 077\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tCamiseta manga corta\t50 99 078\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tManga larga \t50 99 079\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tManga corta\t50 99 080\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tPantalón largo \t50 99 081\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tPantalón corto \t50 99 082\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tMedia larga\t50 99 083\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tMedia corta\t50 99 084\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tMedia tipo calcetín\t50 99 085\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tGuante tipo mitón\t50 99 086\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tGuante con dedos\t50 99 087\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tMáscara\t50 99 088\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tMentonera\t50 99 089\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tCintillo\t50 99 090\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tCollar cervical semirígido\t50 99 061\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tTraumatología  Adulto\tHospitalización\tCama Básica/Media\tCollar cervical blando\t50 99 062\tEPH\tactual\t\tHospital\tNO\t
USUARIO \tMACROPROCESO\tPROCESO (UNIDAD O SERVICIO)\tSUBPROCESO (TIPO DE PRESTACIÓN)\tESTAMENTO O ESPECIALIDAD\tPRESTACIÓN\tCÓDIGO MAI\tPRESTACIÓN EPH\tPRESTACIÓN ACTUAL\tPRESTACIÓN NUEVA\tÁREA DE INFLUENCIA\tCOMPRA DE SERVICIO\tOBSERVACIONES
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica \tDia Cama de Hospitalización Integral Cuidados Básicos\t0201010\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Media \tDia Cama de Hospitalización Integral Cuidados Medios\t0201110\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tConsulta Médica de Especialidad en Obstetricia y Ginecología \t01 01 308\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tConsulta o control por Matrona \t01 02 009\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tConsulta o control por Auxiliar de Enfermería \t01 02 003\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tConsulta o control por Nutricionista\t0102010\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tAmniocentesis\t20 01 006\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tCuldocentesis (punción del Douglas)\t20 01 007\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tHidrotubación y/o insuflación de trompas\t20 01 008\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tMonitoreo basal con informe\t20 01 009\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tMonitoreo fetal estresante, con control permanente del especialista y tratamiento de las posibles complicaciones\t20 01 010\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tCordocentesis\t20 01 021\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tBiopsia endometrio, vulva, vagina, cuello, c/u (proc. aut.)\t20 01 014\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tColocación o extracción de dispositivo intrauterino (no incluye el valor del dispositivo)                    \t20 01 015\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tElectrodiatermo o criocoagulación de lesiones del cuello\t20 01 016\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tTest postcoital\t20 01 020\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tPunción evacuadora de quistes mamarios, c/s toma de muestras, c/s inyección de medicamentos\t20 01 022\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tInsercion Implante Anticonceptivo\t50 99 045\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tRemocion Implante Anticonceptivo\t50 99 046\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tInsercion Pellets subcutáneo \t50 99 047\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tVacunaciones\t01 05 001\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tHemoglucotest\t03 02 047\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tCuración simple\t01 06 002\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tToma de muestras de exámenes de sangre venosa\t03 07 011\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tToma de muestra arterial en adultos\t03 07 009\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tToma de muestra con técnica aséptica para hemocultivo, c/u\t03 07 013\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tToma de muestra capilar ( adultos, niños y lactantes )\t03 07 014\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tAspirados nasofaríngeo para adulto y niño.\t03 07 023\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tE.C.G. de reposo (incluye mínimo 12 derivaciones y 4 complejos por derivación)\t17 01 001\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tEcografía obstétrica\t04 04 002\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tEcotomografía transvaginal o transrectal\t04 04 005\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tEcotomografía ginecológica, pelviana femenina u obstétrica con estudio fetal\t04 04 006\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tEcotomografía transvaginal para seguimiento de ovulación, proc. completo (6-8 sesiones)\t04 04 007\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tEcotomografía para seguimiento de ovulación, procedimiento completo (6 a 8 sesiones)\t04 04 008\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tEcotomografía doppler de vasos placentarios\t04 04 122\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tColposcopía\t20 01 002\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tHisteroscopía diagnóstica (proc. aut.)\t2001005\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tHisterosalpingografía (a.c. 04-02-011)\t2001013\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tCardioversion\t17 01 034\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tDesfibrilacion\t17 01 036\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tReanimación  Cardiopulmonar básica -adultos\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tDía Cama de Hospitalización Integral Obstetricia \t0201410\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención Cerrada\tObstetricia y ginecología\tHospitalización\tCama Básica/Media\tDía Cama de Hospitalización Integral Incubadora\t0201404\tEPH\tactual\t\tHospital\tNO\t
USUARIO \tMACROPROCESO\tPROCESO (UNIDAD O SERVICIO)\tSUBPROCESO (TIPO DE PRESTACIÓN)\tESTAMENTO O ESPECIALIDAD\tPRESTACIÓN\tCÓDIGO MAI\tPRESTACIÓN EPH\tPRESTACIÓN ACTUAL\tPRESTACIÓN NUEVA\tÁREA DE INFLUENCIA\tCOMPRA DE SERVICIO\tOBSERVACIONES
Infantil\tAtención Cerrada\tPediatría\tHospitalización\tCama Básica \tDia Cama de Hospitalización Integral Cuidados Básicos\t0201010\tEPH\tactual\t\tHospital\tNO\t
Infantil\tAtención Cerrada\tPediatría\tHospitalización\tCama Media \tDia Cama de Hospitalización Integral Cuidados Medios\t0201110\tEPH\tactual\t\tHospital\tNO\t
Infantil\tAtención Cerrada\tPediatría\tHospitalización\tIncubadora\tDía Cama de Hospitalización Integral Incubadora\t0201404\tEPH\tactual\t\tHospital\tNO\t
Infantil\tAtención Cerrada\tPediatría\tHospitalización\tCama Básica/media\tConsulta o control por Enfermera \t01 04 004\tEPH\tactual\t\tHospital\tNO\t
Infantil\tAtención Cerrada\tPediatría\tHospitalización\tCama Básica/media\tConsulta o control por Auxiliar de Enfermería \t01 02 003\tEPH\tactual\t\tHospital\tNO\t
Infantil\tAtención Cerrada\tPediatría\tHospitalización\tCama Básica/media\tConsulta o control por Nutricionista\t0102010\tEPH\tactual\t\tHospital\tNO\t
Infantil\tAtención Cerrada\tPediatría\tHospitalización\tCama Básica/media\tConsulta o control por Fonoaudiólogo \t0102005\tEPH\tactual\t\tHospital\tNO\t
Infantil\tAtención Cerrada\tPediatría\tHospitalización\tCama Básica/media\tConsulta o control por psicólogo clínico\t0903002\tEPH\tactual\t\tHospital\tNO\t
Infantil\tAtención Cerrada\tPediatría\tHospitalización\tCama Básica/media\tPunción lumbar c/s manometria c/s queckensted   \t11 01 003\tEPH\tactual\t\tHospital\tNO\t
Infantil\tAtención Cerrada\tPediatría\tHospitalización\tCama Básica/media\tE.E.G. de 16 o más canales (incluye el cód.11-01-006)\t11 01 004\tEPH\tactual\t\tHospital\tNO\t
Infantil\tAtención Cerrada\tPediatría\tHospitalización\tCama Básica/media\tElectroencefalograma (E.E.G.) standard y/o activado "sin privación de sueño" (incluye mono y bipolares, hiperventilación, c/s reactividad auditiva, visual, lumínica, por drogas u otras ). Equipo de 8 canales\t11 01 006\tEPH\tactual\t\tHospital\tNO\t
Infantil\tAtención Cerrada\tPediatría\tHospitalización\tCama Básica/media\tE.E.G. Post-privacion de sueno (incluye codigo 11-01-006). Equipo de 8 canales\t11 01 040\tEPH\tactual\t\tHospital\tNO\t
Infantil\tAtención Cerrada\tPediatría\tHospitalización\tCama Básica/media\tE.E.G. Post-privacion de sueno (incluye codigo 11-01-004) equipo de 16 o mas canales\t11 01 041\tEPH\tactual\t\tHospital\tNO\t
Infantil\tAtención Cerrada\tPediatría\tHospitalización\tCama Básica/media\tPotenciales evocados en corteza ( por ej.: auditivo, ocular\t11 01 011\tEPH\tactual\t\tHospital\tNO\t
Infantil\tAtención Cerrada\tPediatría\tHospitalización\tCama Básica/media\tE.C.G. de reposo (incluye mínimo 12 derivaciones y 4 complejos por derivación)\t17 01 001\tEPH\tactual\t\tHospital\tNO\t
Infantil\tAtención Cerrada\tPediatría\tHospitalización\tCama Básica/media\tReanimación  Cardiopulmonar básica -niños\ts/c\tEPH\tactual\t\tHospital\tNO\t
Infantil\tAtención Cerrada\tPediatría\tHospitalización\tCama Básica/media\tCardioversion\t17 01 034\tEPH\tactual\t\tHospital\tNO\t
Infantil\tAtención Cerrada\tPediatría\tHospitalización\tCama Básica/media\tDesfibrilacion\t17 01 036\tEPH\tactual\t\tHospital\tNO\t
USUARIO \tMACROPROCESO\tPROCESO (UNIDAD O SERVICIO)\tSUBPROCESO (TIPO DE PRESTACIÓN)\tESTAMENTO O ESPECIALIDAD\tPRESTACIÓN\tCÓDIGO MAI\tPRESTACIÓN EPH\tPRESTACIÓN ACTUAL\tPRESTACIÓN NUEVA\tÁREA DE INFLUENCIA\tCOMPRA DE SERVICIO\tOBSERVACIONES
Adulto\tAtención cerrada\tUnidad Corta estadía \tAtención paciente hospitalizado \tPsiquiatría\tConsulta Médica de Especialidad en Psiquiatría adultos\t0101212\tEPH\tnueva \t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tAtención paciente hospitalizado \tPsiquiatría\tConsulta Médica de Especialidad en Psiquiatría pediátrica y de la adolescencia\t0101213\tEPH\tnueva \t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tAtención paciente hospitalizado \tPsiquiatría\tConsulta Médica de Especialidad en Neurología Adultos\t0101209\tEPH\tnueva \t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tAtención paciente hospitalizado \tPsiquiatría\tConsulta Medicina General\t0101001\tEPH\tnueva \t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tAtención paciente hospitalizado \tPsiquiatría\tConsulta Médica otras Especialidades\t0101300\tEPH\tnueva \t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tAtención paciente hospitalizado \tPsiquiatría\tConsulta Médica de Especialidad en Medicina Interna\t0101307\tEPH\tnueva \t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tAtención paciente hospitalizado \tPsiquiatría\tDía Cama de Hospitalización Integral Psiquiatría Cuidados Básicos\t0201405\tEPH\tnueva \t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tAtención paciente hospitalizado \tPsiquiatría\tDía Cama de Hospitalización Integral Psiquiatría Cuidados Medios\t0201406\tEPH\tnueva \t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tAtención paciente hospitalizado \tPsiquiatría\tConsulta de psiquiatría\t0903001\tEPH\tnueva \t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tAtención paciente hospitalizado \tPsiquiatría\tConsulta o control por psicólogo clínico\t0903002\tEPH\tnueva \t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tAtención paciente hospitalizado \tPsiquiatría\tConsulta de salud mental por otros profesionales\t0903003\tEPH\tnueva \t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tAtención paciente hospitalizado \tPsiquiatría\tIntervención psicosocial grupal (4 a 8 pacientes, familiares o cuidadores)\t0903004\tEPH\tnueva \t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tAtención paciente hospitalizado \tPsiquiatría\tPsicoterapia de grupo (por psicólogo o psiquiatra) (4 a 8 pacientes)\t0903005\tEPH\tnueva \t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tAtención paciente hospitalizado \tPsiquiatría\tConsultoría de salud mental por psiquiatra (sesión 4 hrs.) (mínimo 8 pacientes)\t0903006\tEPH\tnueva \t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tAtención paciente hospitalizado \tPsiquiatría\tPrograma de rehabilitación tipo 1 (mensual, grupo 6 a 10 pers.)\t0903007\tEPH\tnueva \t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tAtención paciente hospitalizado \tPsiquiatría\tAtención integral de terapia ocupacional\t0602001\tEPH\tnueva \t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tAtención paciente hospitalizado \tPsiquiatría\tIntervención terapia ocupacional en actividades de la vida diaria, básicas, instrumentales y avanzadas\t0602003\tEPH\tnueva \t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tProcedimientos Diagnósticos y Terapéuticos  \tPsiquiatría\tE.E.G. de 16 o más canales (incluye el cód. 11-01-006)\t1101004\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tProcedimientos Diagnósticos y Terapéuticos  \tPsiquiatría\tEEG en vigilia, sueño y post-privación de sueño. Equipo de 16 o mas canales\t1101041\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tProcedimientos Diagnósticos y Terapéuticos  \tPsiquiatría\tE.C.G. de reposo (incluye mínimo 12 derivaciones y 4 complejos por derivación)\t1701001\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tProcedimientos Diagnósticos y Terapéuticos  \tPsiquiatría\tMonitoreo de presión arterial continuo\t1701009\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tProcedimientos Diagnósticos y Terapéuticos  \tPsiquiatría\tSaturación de O2 en reposo y/o ejercicio (con oxímetro) \t1707054\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tProcedimientos Diagnósticos y Terapéuticos  \tPsiquiatría\tVaciamiento vesical por sonda uretral, (proc. aut.)\t1901022\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tProcedimientos Diagnósticos y Terapéuticos  \tPsiquiatría\tPuncion Arterial y Venosa (toma de muestras)\t03 07 023\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tProcedimientos Diagnósticos y Terapéuticos  \tPsiquiatría\tPunción Lumbar \t11 01 003\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tProcedimientos Diagnósticos y Terapéuticos  \tPsiquiatría\tHemoglucotest\t03 02 047\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tProcedimientos Diagnósticos y Terapéuticos  \tPsiquiatría\tAdministración de medicamentos por vía: endovenosa, intramuscular, subcutáneo, oral, ocular, ótica, rectal, inhalatoria.\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tProcedimientos Diagnósticos y Terapéuticos  \tPsiquiatría\tAdministración de Oxígeno\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tProcedimientos Diagnósticos y Terapéuticos  \tPsiquiatría\tAplicación técnicas de contensión \ts/c\tEPH\tnueva \t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tprocedimientos Diagnósticos y Terapéuticos  \tPsiquiatría\tInstalación de vía venosa\ts/c\tEPH\tactual\t\tHospital\tNO\t
Adulto\tAtención cerrada\tUnidad Corta estadía \tAtención paciente hospitalizado \tPsiquiatría\tReanimación cardiopulmonar adulta y pediátrica\ts/c\tEPH\tactual\t\tHospital\tNO\t
USUARIO \tMACROPROCESO\tPROCESO (UNIDAD O SERVICIO)\tSUBPROCESO (TIPO DE PRESTACIÓN)\tESTAMENTO O ESPECIALIDAD\tPRESTACIÓN\tCÓDIGO MAI\tPRESTACIÓN EPH\tPRESTACIÓN ACTUAL\tPRESTACIÓN NUEVA\tÁREA DE INFLUENCIA\tCOMPRA DE SERVICIO\tOBSERVACIONES
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTumor de nervio periférico, extirp. de\t1103058\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tSección de nervio, reparación con injerto\t1103060\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tSección de nervio, reparación sin injerto\t1103061\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tNeurectomía, cualquier localización, cada zona quirúrgica\t1103068\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tNeurolisis con técnica microquirúrgica\t1103062\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tNeurolisis externa\t1103063\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLiberación quirúrgica de nervio periférico extracraneano (trat. quir. del Síndrome del Túnel Carpiano, tarso u otro)\t1103066\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLiberación de nervio cubital a nivel del codo, cualquier técnica\t1103067\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLiberación quirúrgica de nervio periférico  en el Síndrome del Túnel Carpiano téc. WALANT (anestesia local sin torniquete)\t1103083\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tInjertos  hasta 1% superficie corporal receptora\t1502006\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tInjertos  hasta 5% superficie corporal receptora\t1502007\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tInjertos hasta 10% superficie corporal receptora\t1502008\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tPiel total, cualquier tamaño (incluye tratamiento zona dadora y receptora)\t1502011\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tToma de injertos-óseo (costal, ilíaco, tibial o similares) c/u.\t1502013\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tPlastías en Z, hasta 3\t1502014\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tPlastías en Z, 4 y más\t1502015\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \t- Colgajos libres con microanastomosis (incluye toma del colgajo y las suturas neurovasculares)\t1502017\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \t- Colgajos musculares o musculocutáneos\t1502018\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \t- Colgajos osteomusculocutáneos\t1502019\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \t- Colgajos simples dos o más\t1502020\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \t- Colgajo simple único\t1502021\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tSindactilia, trat. quir. cada espacio con injerto\t1502056\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tSindactilia, trat. quir. cada espacio sin injerto\t1502057\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tPolidactilia, extirpación y plastía unilateral\t1502058\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tReparación quirúrgica de vasos arteriales y/o venosos periféricos c/s injerto (biológicos o sintéticos)\t1703006\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tArtroscopía diagnóstica c/s biopsia, c/s sección de bridas, extracción de cuerpo extraño\t2104001\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tExostosis u osteocondroma, trat. quir.\t2104002\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tQuistes sinoviales de vainas flexoras, bursas\t2104003\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTracción transesquelética o de partes blandas en adultos o en niños (proc. aut.)\t2104006\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tArtrodesis de codo o muñeca, c/u\t2104007\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tArtrodesis de hombro, cadera,rodilla, tobillo o sacroilíaca, c/u\t2104008\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tArtrodesis de mano o pie c/u\t2104009\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTratamiento completo de fracturas expuestas de brazo, antebrazo, muslo y pierna, c/u\t2104010\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTratamiento completo de fracturas expuestas de mano o pie, c/u      \t2104011\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteítis, raspado, c/s secuestrectomía\t2104012\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteomielitis aguda hematógena, drenaje quirúrgico, c/s dispositivos de osteoclisis\t2104013\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteomielitis crónica huesos largos, legrado óseo,  c/s osteosíntesis o aparato de yeso\t2104014\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tArtrotomía hombro o cadera c/u\t2104015\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tArtrotomía de codo, muñeca, tobillo o temporomandibular, c/u\t2104016\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tPseudoartrosis  infectada huesos largos, trat. quir. cualquier técnica, c/s dispositivo de osteoclisis, c/s osteosíntesis o aparato de yeso\t2104017\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tAutotrasplante óseo microquirúrgico\t2104018\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tInjerto esponjoso metafisiario\t2104019\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tInjertos esponjosos o córtico-esponjosos de cresta ilíaca\t2104020\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTransplante óseo (auto u homotrasplante)\t2104021\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLesiones quísticas con fractura patológica: legrado óseo, c/s relleno injerto esponjoso, c/s osteosíntesis y/o aparato de inmovilización postoperatoria\t2104022\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLesiones quísticas intraosea: legrado óseo, c/s relleno de injertos\t2104023\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tMetástasis ósea c/s fractura patológica, legrado tumoral, relleno cemento quirúrgico y osteosíntesis\t2104024\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTumor óseo, resección en bloque, c/s osteosíntesis y/o aparato inmovilización postoperatorio\t2104025\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTumores o quistes o lesiones pseudoquísticas o musculares y/o tendíneas, trat. quir.\t2104026\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTumores óseos: resección en bloque, epifisiaria c/artrodesis o diafisiaria\t2104027\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTumores primarios o metastásicos vertebrales: corporectomía, reemplazo por cemento quir. o injerto óseo, c/s osteosíntesis\t2104028\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tSinovectomías quirúrgicas de codo o muñeca o metacarpofalángicas, c/u\t2104029\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tSinovectomías quirúrgicas de rodilla o cadera u hombro, c/u\t2104030\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tEpineurorrafia microquirúrgica con magnificación cualquier tronco nervioso (con excepción nervios digitales)\t2104031\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tBiopsia ósea por punción\t2104033\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tBiopsia ósea quirúrgica\t2104034\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tBiopsia sinovial o muscular por punción\t2104035\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tBiopsia sinovial o muscular quirúrgica\t2104036\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tRegularización de Muñón de Amputación\t2104038\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteocondrosis o epifisitis, trat. quir.\t2104039\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tAmputación interescápulo-torácica\t2104040\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tDesarticulación escápulo-humeral\t2104041\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tEndoprótesis total de hombro,(cualquier técnica)\t2104042\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tFractura cuello humeral, trat. quir.\t2104044\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tFractura de clavícula, osteosíntesis\t2104045\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tFractura escápula, osteosíntesis\t2104046\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLuxación acromio-clavicular o esterno-clavicular, reducción o plastía cápsuloligamentosa y osteosíntesis\t2104047\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLuxación recidivante de hombro, trat. quir.\t2104048\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLuxación traumática de hombro, reducción cruenta\t2104049\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLuxofractura, reducción y osteosíntesis hombro\t2104050\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tRuptura manguito rotadores, trat. quir. c/s acromiectomía\t2104051\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTransposiciones musculares\t2104052\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tAmputación brazo\t2104053\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tFractura supracondílea niño; tracción esquelética, c/s osteosíntesis y aparato de yeso\t2104054\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteosíntesis diafisiaria de húmero (cualquier técnica) \t2104055\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteosíntesis supra o intercondílea (cualquier técnica)\t2104056\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteotomía húmero (cualquier técnica)\t2104057\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tPseudoartrosis c/s osteosíntesis c/s yeso húmero\t2104058\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tArtroplastía con fascia codo\t2104059\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tCúpula radial, resección\t2104060\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tCúpula radial, (resección con implante de prótesis) artroplastía \t2104061\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tEndoprótesis total de codo, (cualquier técnica)\t2104062\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tEpicondilitis, trat. quir. (cualquier técnica)\t2104063\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLuxación de codo, reducción cruenta \t2104064\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLuxofractura de codo, reducción cruenta c/s resección cúpula radial\t2104065\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteosíntesis epitroclea-epicóndilo (cualquier técnica)\t2104066\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteosíntesis olécranon u osteosíntesis de cúpula radial (proc. aut.) (cualquier técnica)\t2104067\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTraslocación nervio cubital (proc. aut.)\t2104068\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOperación de salvataje radio-procúbito\t2104069\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tAmputación antebrazo\t2104070\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tExtirpación metáfisis distal del cúbito y artrodesis radiocubital inferior\t2104071\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLuxofracturas (Monteggia-Galeazzi), reducc. y osteosíntesis\t2104072\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteosíntesis, fract.cerrada cúbito y/o radio (cualq. tecn.)\t2104073\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteotomía uno o ambos huesos, c/s osteosíntesis c/s yeso o trat. quir. Enf. de Kienbock\t2104074\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tPseudoartrosis  cúbito y/o radio c/s osteosíntesis c/s yeso\t2104075\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tSinostosis radio-cubital, trat. quir., c/s injerto\t2104076\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTrasplantes músculo-tendinosos antebrazo\t2104077\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tContractura isquem. de Volkmann: descenso muscular, neurolisis\t2104078\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tEndoprótesis total de muñeca, (cualquier técnica)\t2104079\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tEstiloides cubital, radial, resección de.\t2104080\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tFractura o pseudoartrosis escafoides, trat. quir. cualq. técn.\t2104081\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLuxación radiocarpiana, trat. quir.\t2104083\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLuxación semilunar ,escafoidea, reducción y osteosíntesis semicruenta o cruenta\t2104084\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteosíntesis radio, (cualquier técnica)\t2104085\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTendovaginosis de De Quervain, trat. quir.\t2104086\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tAmputación dedos (tres o más)\t2104087\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tAmputación dedos (uno o dos)\t2104088\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tAmputación mano o del pulgar\t2104089\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tAmputación pulpejos (plastía Kutler o similares)\t2104090\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tContractura Dupuytren, trat. quir., cada tiempo\t2104091\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tContusión-compresión grave mano, trat. quir. incluye incisiones liberadoras y/o fasciotomía y/o escarectomía y/o injertos piel inmediatos y síntesis percutánea\t2104092\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tDedos en gatillo, trat. quir., cualquier número\t2104093\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tFlegmón mano, trat. quir.\t2104094\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLuxofractura metacarpofalángica o interfalángica, trat. quir.\t2104095\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tMano reumática en ráfaga: traslocaciones tendinosas, plastías capsulares, tenotomías, inmovilización postoperatoria\t2104096\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tMano reumática: implant. silastic, cualq. número (proc. aut.)\t2104097\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tMutilación grave mano, aseo. quir. completo c/s osteosíntesis, c/s injertos \t2104098\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteosíntesis metacarpianas o de falanges, cualquier técnica\t2104099\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tPanadizo, trat. quir.\t2104100\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tPulgarización dedo (índice o anular)\t2104101\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tReimplante mano o dedo(s)\t2104102\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tReparación flexores: primer tiempo espaciador silastic\t2104103\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tReparación nervio digital con injerto interfascicular: cualquier número\t2104104\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tRupturas cerradas cápsulo-ligament. o tendinosas, trat. quir. mano\t2104105\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tSutura nervio(s) digital(es); microcirugía\t2104106\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTenorrafia extensores mano\t2104107\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTenorrafia o injertos flexores mano\t2104108\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTenosinovitis séptica, trat. quir. mano\t2104109\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTrasplante microquirúrgico para pulgar\t2104110\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTransposiciones tendinosas flexoras o extensoras mano\t2104111\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTratamiento quir., dedos en gatillo, cualquier número téc. WALANT (anestesia local sin torniquete)\t2104203\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteosíntesis en fractura de arco anterior de pelvis y disyunciones pubianas\t2104122\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tFractura de pelvis, osteosíntesis quir.\t2104123\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteotomía pelviana (Salter, Chiari o similares)\t2104124\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tDesarticulación cadera\t2104127\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tEndoprótesis parcial de cadera c/s cementación (cualquier técnica) (no incluye prótesis)\t2104128\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tEndoprótesis parcial de cadera c/s cementación (cualquier técnica) (incluye prótesis)\t2104228\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tEndoprótesis total de cadera  (no incluye prótesis)\t2104129\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tEndoprótesis total de cadera (incluye prótesis)\t2104229\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tEpifisiolisis lenta o aguda, trat. quir.\t2104130\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tFractura de cuello de fémur, osteosíntesis, cualquier técnica \t2104131\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tFractura de cuello de fémur, osteosíntesis, cualquier técnica (incluye elementos de osteosíntesis)\t2104231\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tFractura de cuello de fémur, resección epífisis femoral\t2104132\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLuxación traumática de cadera, reducción cruenta\t2104133\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLuxofractura acetabular, trat. quir.\t2104134\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOperación de salvataje cadera, columna o similares\t2104135\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteotomías femorales\t2104136\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tReducción cruenta en luxación congénita o traumática de cadera\t2104137\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tReducción cruenta y acetabuloplastía femoral c/s osteotomía femoral\t2104138\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tReducción cruenta y osteotomía femoral\t2104139\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTenotomía aductores c/s botas, con yugo (proc. aut.)\t2104140\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTrocanteroplastías\t2104141\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tAmputación muslo\t2104142\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tEpifisiodesis (fémur y/o tibia)\t2104143\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteosíntesis diafisiaria o metafisiaria muslo (cualquier técnica)\t2104144\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteotomía correctora muslo\t2104145\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteotomía de alargamiento o acortamiento con osteosíntesis inmediata o distracción instrumental progresiva muslo\t2104146\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tPseudoartrosis, trat. quir. (cualquier técnica) muslo\t2104148\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tRuptura y/o hernia muscular, trat. quir. muslo\t2104149\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tArtrotomía por cuerpos libres, osteocondritis rodilla (proc. aut)\t2104150\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tDesarticulación rodilla\t2104151\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tDisfunción patelo-femoral, realineamiento (cualquier técnica)\t2104152\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tEndoprótesis total de rodilla, (cualquier técnica)\t2104153\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tFractura rótula: osteosíntesis o patelectomía parc. o total\t2104154\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tFracturas condíleas o de platillos tibiales, reducción, osteosíntesis  (cualquier técnica)\t2104155\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tInestabilidad crónica de rodilla, reconstrucción cápsuloligamentosa (cualquier técnica)\t2104156\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLuxación o rotura ligamentos, trat. quir. cápsulo-ligamentoso\t2104157\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tMeniscectomía quirúrgica, interna y/o externa\t2104158\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tMeniscectomía u otras intervenciones por vía artroscópica (incluye artroscopía diagnóstica)\t2104159\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tQuiste poplíteo, trat. quir.\t2104160\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tReconstrucción aparato extensor de rodilla\t2104161\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tReparación quirúrgica ligamentos colaterales y/o cruzados de rodilla\t2104162\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTraslocaciones músculo-tendinosas en rodilla paralítica o espástica\t2104163\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tAmputación pierna\t2104164\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tColgajo cruzado de pierna, trat. quir. completo\t2104165\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tFasciotomía por síndrome compartamental\t2104166\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteosíntesis tibio-peroné  (cualquier técnica)\t2104167\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteotomía correctora de ejes  (cualquier técnica) pierna\t2104168\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteotomía de alargamiento o acortamiento con osteosíntesis inmediata o distracción instrumental progresiva pierna\t2104169\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteotomía del peroné\t2104170\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tPeroné protibia\t2104171\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tPseudoartrosis, c/s osteosíntesis  (cualquier técnica) pierna\t2104172\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tDesarticulación tobillo\t2104173\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tEsguince grave de tobillo, trat. quir. cápsulo-ligamentoso \t2104175\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tFractura astrágalo y/o calcáneo, osteosíntesis (cualq. técn.)\t2104176\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tHuesos supernumerarios, extirpación, uno o más, unilateral\t2104177\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLuxación tibio-astrág.-calcán., reducc. cruenta y osteosínt.\t2104178\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLuxofractura tobillo, cualquier tipo, osteosíntesis y reparación cápsulo-ligamentosa\t2104179\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOsteoplastía tibio-calcánea\t2104180\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tRuptura tendón de Aquiles o tibial posterior, tenorrafia primaria y/o transposiciones tendinosas\t2104181\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tRuptura tibial anterior u otros, tenorrafia\t2104182\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTenorrafia extensores o tenotomía de alargamiento de tendón de Aquiles\t2104183\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTraslocación tendinosa tobillo\t2104184\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tAmputación transmetatarsiana\t2104185\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tAstrágalo vertical, trat. quir.\t2104186\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tEspolón calcáneo, trat. quir.\t2104187\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tExostosis 5° metatarsiano, ("juanetillo")  trat. quir.\t2104188\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tFasciotomía plantar (proc. aut.)\t2104189\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tHallux valgus o rígidus, trat.quir. completo (cualquier téc.)\t2104190\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLuxaciones, luxofracturas, fracturas, reducción cruenta pie\t2104191\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tMal perforante plantar, trat. quir.\t2104192\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tNeuroma de Morton, trat. quir.\t2104193\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOrtejos en garra, trat. quir., cualq. número (cualq. técnica)\t2104194\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tOrtejos, amputación, uno o más, unilateral\t2104195\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tPie bot u otras malformaciones congénitas, trat. quir. (cualquier técnica)\t2104196\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tPie cavo, trat.quir. (cualquier técnica)\t2104197\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tPie plano, trat. quir. (cualquier técnica)\t2104198\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tPie reumatoideo, trat.quir.completo (cualquier técnica)\t2104199\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tSesamoídeos, extirpación de uno o más, unilateral\t2104200\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTenorrafia extensores pie\t2104201\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTrasplantes tendinosos pie (cualquier técnica)\t2104202\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tRetiro de endoprótesis u osteosíntesis internas articulares o de columna vertebral\t2106001\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tRetiro de placas rectas o anguladas\t2106002\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tRetiro de tornillos, clavos, agujas de osteosíntesis o similares\t2106003\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLuxaciones de articulaciones medianas (hombro, codo, rodilla, tobillo, muñeca, tarso y esternoclavicular)\t2107001\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLuxaciones de articulaciones  mayores (columna, cadera, pelvis)\t2107002\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLuxaciones de articulaciones menores (el resto)\t2107003\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tFracturas mayores (columna, pelvis, supracondílea, codo, epífisis femorales)\t2107004\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tFracturas medianas (diáfisis humeral, radial, cubital, diáfisis femoral, tibial, peroneal, clavicular, platillos tibiales)\t2107005\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tFracturas menores (el resto)\t2107006\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTratamiento funcional con técnica de Sarmiento y similares de extremidad inferior\t2107007\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tTratamiento funcional con técnica de Sarmiento y similares de extremidad superior\t2107008\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tLuxación congénita de cadera, trat. ortopédico completo (uni o bilateral)\t2107009\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tTRAUMATOLOGIA \tPie bot, unilateral, hasta 10 cambios de yeso\t2107010\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tInjertos hasta 10% superficie corporal receptora\t1502008\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tInjertos por cada 10% (o su fracción) adicional hasta 50%\t1502009\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tInjertos 51% y más de superficie corporal receptora\t1502010\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tPiel total, cualquier tamaño (incluye tratamiento zona dadora y receptora)\t1502011\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tToma de injertos-óseo (costal, ilíaco, tibial o similares) c/u.\t1502013\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tExpansor de piel (dos o más) primer tiempo\t1502068\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tExpansor de piel (dos o más) segundo tiempo retiro\t1502069\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tExpansor de piel (único) primer tiempo\t1502070\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tExpansor de piel (único) segundo tiempo o retiro\t1502071\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tPlastías en Z, 4 y más\t1502015\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \t- Colgajos complejos (Abbe, Mustarda, Converse, Juri, Bakamjian o similar)\t1502016\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \t- Colgajos libres con microanastomosis (incluye toma del colgajo y las suturas neurovasculares)\t1502017\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \t- Colgajos musculares o musculocutáneos\t1502018\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \t- Colgajos osteomusculocutáneos\t1502019\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \t- Colgajos simples dos o más\t1502020\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \t- Colgajo simple único\t1502021\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tOrejas aladas o en asa, corrección plástica\t1502025\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tGinecomastia, corrección plástica\t1502047\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tEscarectomía con resección ósea c/s colgajo de rotación\t1502054\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tTratamiento de escaras de decubito, con resección ósea y colgajos musculares o musculocutáneos\t1502055\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tEscarotomía\t\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tEscarotomía hasta 10 % superficie corporal\t1502061\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tEscarotomía por cada 10 % adicional (o su fracción)\t1502062\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tEscarectomía\t\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tEscarectomía hasta 1 % superficie corporal\t1502063\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tEscarectomía hasta 5 % superficie corporal\t1502064\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tEscarectomía  hasta 10% superficie corporal\t1502065\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tEscarectomía por cada 10% adicional (o su fracción) (Se cobrará cód. ad. una sóla vez por superficie entre el 11% y 50%).\t1502066\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tBiopsia de piel y/o mucosa por curetaje o sección tangencial c/s electro por 1 lesión\t1602201\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tCabeza, cuello, genitales hasta 3 lesiones: extirpación, reparación o biopsia, total o parcial, de lesiones benignas cutáneas por excisión\t1602202\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tResto del cuerpo hasta 3 lesiones: extirpación, reparación o biopsia, total o parcial, de lesiones benignas cutáneas por excisión\t1602203\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tCabeza, cuello y genitales desde 4 y hasta 6 lesiones: extirpación, reparación o biopsia, total o parcial, de lesiones benignas cutáneas por excisión\t1602204\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tResto del cuerpo desde 4 y hasta 6 lesiones: extirpación, reparación o biopsia, total o parcial, de lesiones benignas cutáneas por excisión\t1602205\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tExtirpación de lesiones benignas por sec tangencial, curetaje y/o fulguración hasta 15 lesiones\t1602206\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tTratamiento por electro de hemangiomas o telangectasias hasta 15 lesiones\t1602207\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tCabeza, cuello, genitales: tratamiento quirúrgico de tumor maligno por escisión total o parcial, con o sin sutura, por cada lesión o melanoma cualquier localización\t1602211\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tResto del cuerpo: tratamiento quirúrgico de tumor maligno por escisión total o parcial, con o sin sutura, por cada lesión\t1602212\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tCabeza, cuello, genitales o melanoma cualquier ubicación: ampliación de márgenes quirúrgicos de tumor maligno extirpado previamente \t1602213\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tResto del cuerpo: ampliación de márgenes quirúrgicos de tumor maligno extirpado previamente\t1602214\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tTumores vasculares profundos cabeza, cuello, genitales\t1602215\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tTumores Vasculares Profundos Resto del cuerpo\t1602216\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tHerida cortante o contusa complicada, reparación y sutura (más de 5 cm)\t1602221\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tHerida cortante o contusa no complicada, reparación y sutura (una o múltiple hasta 5 cms. de largo total que comprometa solo la piel)\t1602222\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tExtirpación de lesión benigna subepidérmica, incluye Tumor sólido, quiste epidérmico y lipoma por lesión\t\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tCabeza, cuello, genitales: extirpación de lesión benigna subepidérmica, incluye tumor sólido, quiste epidérmico y lipoma por lesión \t1602223\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tResto del cuerpo: extirpación de lesión benigna subepidérmica, incluye tumor sólido, quiste epidérmico y lipoma por lesión \t1602224\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tVaciamiento y curetaje quirúrgico de lesiones quísticas o abscesos\t1602225\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tOnicectomía total o parcial simple\t1602231\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tCirugía reparadora ungueal por proceso inflamatorio\t1602232\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tCorrección quirúrgica de defecto congénito o por tumor ungueal\t1602233\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tCuración por Médico, Quemadura o Similar  menor al 5% superficie corporal en pabellón\t1602240\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tCuración por Médico, Quemadura o Similar  5 a 10% superficie corporal en pabellón\t1602241\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tCuración por Médico, Quemadura o Similar mayor al 10 %  superficie corporal en pabellón\t1602242\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tLigadura cayado safena interna, unilateral\t1703026\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tLigadura otros troncos venosos (poplíteo, femoral, ilíacas, humeral, axilar, otros); ligadura de venas comunicantes y/o perforantes, y/o resección de paquetes varicosos, cualquier técnica (una extremidad); c/u\t1703027\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tSafenectomía interna y/o externa, unilateral, o endoablación por cualquier técnica (láser, radiofrecuencia o similar).\t1703030\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tBiopsia quir. ganglionar (cualquier región periférica superficial o profunda) (proc. aut.)\t1703035\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tDisección y extirpación ganglionar regional: axilo-supraclavicular \t1703036\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tDisección y extirpación ganglionar regional: cérvico-torácica\t1703037\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tDisección y extirpación ganglionar regional: ileoinguinal\t1703038\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tDisección y extirpación ganglionar regional: inguinoescrotales\t1703039\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tDisección y extirpación ganglionar regional: yugular simple\t1703044\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tToracotomía exploradora, c/s biopsia, c/s debridación, c/s drenaje\t1704009\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tVideotoracoscopía exploradora \t1704080\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tToracotomía mínima c/s resección costal, c/s biopsia, c/s drenaje\t1704010\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tDecorticación pleuropulmonar (pleurectomía parcial o total)\t1704024\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tDecorticación pleuropulmonar (pleurectomía parcial o total) por videotoracoscopia\t1704072\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tHernia diafragmática por vía abdominal o cualquiera otra hernia con uso de prótesis (no incluye el valor de la prótesis)\t1802001\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tHernia diafragmática por vía abdominal o cualquiera otra hernia con uso de prótesis (incluye el valor de la prótesis)\t1802101\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tHernia incisional o evisceración post-op. sin resección intestinal\t1802002\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tHernia inguinal, crural, umbilical, de la línea blanca o similares, recidivada o no, simple o estrangulada s/resección intest.c/u\t1802003\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tLaparotomía exploradora, c/s liberación de adherencias, c/s drenaje, c/s biopsias como proc. aut. o como resultado de una herida penetrante abdominal no complicada o de un hemoperitoneo postoperatorio o como tratamiento de una peritonitis (laparostomía contenida -máximo cuatro-, resuturas, etc.)\t1802004\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tPeritonitis difusa aguda, trat. quir. (proc. aut.) \t1802007\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tTumor y/o quiste, trat. quir.\t\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tTumor y/o quiste peritoneal (parietal)\t1802008\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tTumor y/o quiste retroperitoneal\t1802009\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tAntrectomía y vagotomía troncular o selectiva (proc. aut.)\t1802010\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tDesgastrectomía y neoanastomosis, c/s vaguectomía\t1802011\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tGastroenteroanastomosis, cualquier técnica. (proc. aut.)\t1802012\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tBy pass gástrico por cirugía abierta\t1802149\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tBy pass gástrico por laparoscopía\t1802150\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tGastrotomía y/o gastrostomía (proc. aut.)\t1802014\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tPerforación gástrica aguda, trat. quir. (proc. aut.)\t1802015\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tPiloroplastía (proc. aut.)\t1802016\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tGastrectomía sub-total distal:\t\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tGastrectomía subtotal con disección ganglionar\t1802017\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tGastrectomía subtotal sin disección ganglionar\t1802018\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tDumping y/o síndrome asa aferente, trat. quir.\t1802019\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tGastrectomía sub-total proximal con esófago-gastro-anastomosis u otra derivación\t1802021\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tGastrectomía total\t1802022\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tGastrectomía total o sub-total ampliada (incluye esplenectomía y pancreatectomía corporocaudal y disección ganglionar)\t1802023\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tGastropexia y/u otra cirugía antirreflujo, c/s vagotomía\t1802024\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tVagotomía selectiva y superselectiva c/s dren. gástrico, c/s piloroplastía (proc. aut.)\t1802025\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tGastrectomía total con ostomías proximal y distal\t1802079\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tReconstitución  de tránsito en 2° tiempo de operación código 18-02-079\t1802080\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tCirugía de la estenosis hipertrófica del píloro. Abierta\t1802083\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tCirugía de la estenosis hipertrófica del píloro. Laparoscopia\t1802084\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tLaparotomía exploradora, instalación de VAC (por procedimiento)\t1802085\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tCirugía antirreflujo más gastrostomía\t1802086\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tCirugía antirreflujo más gastrostomia vía laparoscopia\t1802087\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tCirugia bariátrica By Pass Gastrico por laparoscopia \t1802158\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tCirugia bariátrica Manga Gastrica por laparoscopia\t1802159\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tDrenaje de colecciones líquidas hepáticas\t1802026\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tColecistectomía c/s colangiografía operatoria\t1802028\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tColecistectomía por videolaparoscopía, proc. completo\t1802081\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tColecistectomía y coledocostomía (sonda T y colangiografía postoperatoria) c/s colangiografía operatoria\t1802029\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tColecistostomía (proc. aut.)\t1802031\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tColédoco o hepatoenteroanastomosis\t1802032\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tColedocostomía supraduodenal o hepaticostomía (proc. aut.)\t1802033\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tHerida traumática de hígado y/o vía biliar, trat. quir.\t1802040\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tQuiste hidatídico, único o múltiple, y/o cistoyeyunoanastomosis, trat. quir.\t1802042\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tAbscesos, quistes, pseudoquistes o similares de páncreas, trat. quir.\t1802043\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tHeridas, traumatismos de páncreas, trat.quir.\t1802044\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tSecuestrectomía en pancreatitis aguda\t1802048\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tEsplenectomía por vía laparoscopia\t1802092\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tEsplenectomía total o parcial (proc. aut.)\t1802050\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tSutura esplénica (proc. aut.)\t1802052\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tApendicectomía y/o dren. absceso apendicular (proc. aut.)\t1802053\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tCierre de colostomía (proc. aut.)\t1802054\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tColostomía (proc. aut.)\t1802055\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tColostomía, complicaciones tardías, trat. quir.\t1802056\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tDivertículo de Meckel, trat. quir.\t1802057\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tEntero-enteroanastomosis o enterocoloanastomosis (proc. aut.)\t1802058\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tEnterotomía o enterostomía (yeyunostomía u otra) (proc. aut.)\t1802059\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tIleostomía terminal o en asa (proc. aut.)\t1802060\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tInvaginación intestinal, trat. quir.\t1802061\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tPersistencia conducto onfalomesentérico, trat. quir.\t1802062\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tQuiste uraco, trat. quir.\t1802063\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tOclusión intestinal, trat. quir.:\t\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tOclusión intestinal con resección\t1802065\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tOclusión intestinal sin resección\t1802066\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tColectomía parcial o hemicolectomía\t1802067\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tColectomía total abdominal\t1802068\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tDescenso de colon c/conservación del esfínter, incluye resección de colon\t1802069\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tHartmann, operación de (o similar)\t1802070\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tPerforación y/o herida de intestino, única o múltiple, trat. quir. (proc. aut.)\t1802071\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tQuiste y/o tumor del mesenterio y/o epiplones, único y/o múltiple, trat. quir.\t1802072\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tReconstitución  tránsito post operación de Hartmann o sim.\t1802073\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tResección de intestino y enteroanastomosis (proc. aut.)\t1802074\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tResección intestinal con ostomías proximal y distal\t1802082\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tResección intestinal masiva por trombosis mesentérica u otra etiología\t1802075\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tAbsceso ano rectal complejo, tratamiento quirúrgico\t1803001\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tAbsceso anorrectal simple, trat. quir.\t1803002\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tAbsceso sacrocoxígeo, drenaje\t1803003\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tBiopsia quirúrgica rectal (proc. aut.)\t1803004\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tCuerpo extraño rectal, extracción por vía abdominal\t1803006\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tCuerpo extraño rectal, extracción por vía anal\t1803007\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tDesgarros y heridas anorrectales sin compromiso del esfínter\t1803009\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tEsfinterotomía (proc. aut.)\t1803010\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tFecaloma, trat. quir.\t1803013\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tFístula rectovesical, trat.quir.\t1803014\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tFístula anorrectal, trat.quir.de cualquier tipo\t1803016\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tFisura anal, repar. quir.\t1803017\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tHemorroidectomía (incluye otras operaciones complementarias en canal anal)\t1803018\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tHemorroides, trombectomía (proc. aut.)\t1803019\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tQuiste sacrocoxígeo, trat. quir.\t1803031\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tCondilomas anales, trat. quir. \t1803038\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA GENERAL \tHidrocele y/o hematocele, incluye quistes cordón y/o epidídimo y/o hidatidectomías y/o cirugía intravaginal del mismo lado \t1902064\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tUROLOGIA \tCistoscopía con o sin sondeo de uno o ambos uréteres, con o sin biopsia \t1901002\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tUROLOGIA \tCistoscopia y/o uretrocistoscopia y/o uretroscopia (proc.aut.)\t1901003\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tUROLOGIA \tBiopsia prostática transrectal o transperineal con apoyo ecográfico\t1901005\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tUROLOGIA \tTratamiento integral litiasis urinaria por vía litotripsia extracorpórea\t1902090\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tUROLOGIA \tFístula urétero-vaginal, trat. quir.\t1902017\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tUROLOGIA \tCistostomía, extracción de litiasis o cuerpo extraño, instalación de catéter suprapúbico, por vía abierta o endoscopica, c/s láser\t1902031\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tUROLOGIA \tFlegmón urinoso, drenaje y cistostomía\t1902041\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tUROLOGIA \tAdenoma prostático, trat. quir. cualquier vía o técnica abierta\t1902056\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tUROLOGIA \tDescenso testicular con o sin hernia, cualquier tiempo, cualquier técnica\t1902060\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tUROLOGIA \tDescenso testículo inguinal c/s hernioplastía\t1902061\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tUROLOGIA \tHidatidectomía unilat. c/s eversión de la vaginal (proc. aut.)\t1902063\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tUROLOGIA \tHidrocele y/o hematocele, incluye quistes cordón y/o epidídimo y/o hidatidectomías y/o cirugía intravaginal del mismo lado \t1902064\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tUROLOGIA \tOrquidectomía unilateral\t1902065\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tUROLOGIA \tOrquidopexia unilateral\t1902066\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tUROLOGIA \tCirugía del epidídimo y cordón (proc.aut), incluye cirugía intravaginal y/o varicocele mismo lado\t1902071\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tUROLOGIA \tPlastía epidídimo-deferente (operación de Martín o sim.)\t1902072\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tUROLOGIA \tQuistes del cordón, y/o epidídimo, extirpación; epididimotomía diagnóstica y/o terapéutica (proc. aut.)\t1902073\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tUROLOGIA \tExploración escroto agudo. Incluye hematocele por trauma, destorsión y fijación testículo, hidatidectomía  y eversión bilateral si corresponde \t1902074\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tUROLOGIA \tVaricocele unilateral y/o denervación cordón espermático (incluye quistes, hidátides e hidrocele mismo lado)\t1902075\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tUROLOGIA \tVasectomía bilateral, (proc. aut.) (la vasectomía como tiempo previo a una resección de próstata esta incluida en la prostatectomía)\t1902076\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tUROLOGIA \tCircuncisión (incluye sección de frenillo, y/o de sinequias bálano-prepuciales, y/o incisión dorsal c/s meatotomía)\t1902082\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tUROLOGIA \tMeatotomía hombre y/o sección frenillo y/o incisión dorsal, (proc. aut.)\t1902084\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tColposcopía\t2001002\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tHisteroscopía diagnóstica (proc. aut.)\t2001005\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tAmniocentesis\t2001006\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tCuldocentesis (punción del Douglas)\t2001007\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tMonitoreo basal con informe\t2001009\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tMonitoreo fetal estresante, con control permanente del especialista y tratamiento de las posibles complicaciones\t2001010\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tCordocentesis\t2001021\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tGalactografía (a.c. 04-02-005)\t2001012\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tHisterosalpingografía (a.c. 04-02-011)\t2001013\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tBiopsia endometrio, vulva, vagina, cuello, c/u (proc. aut.)\t2001014\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tColocación o extracción de dispositivo intrauterino (no incluye el valor del dispositivo)\t2001015\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tElectrodiatermo o criocoagulación de lesiones del cuello\t2001016\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tTest postcoital\t2001020\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tPunción evacuadora de quistes mamarios, c/s toma de muestras, c/s inyección de medicamentos\t2001022\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tToma de biopsia con aguja bajo visión ecográfica de la Mama (Biopsia Core)\t2001025\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tAbsceso y/o hematoma de mama, trat.quir.\t2002001\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tTumor benigno y/o quiste y/o mama supernumeraria y/o aberrante o politelia, o biopsia quirúrgica extemporánea, trat. quir. (proc. aut)\t2002005\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tVideolaparoscopía ginecológica exploradora (incluye toma de muestras para biopsias, punción de quistes y liberación de adherencias) (proc. aut.)\t2003031\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tTraquelectomía radical \t2003043\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tTraquelectomía radical laparoscópica \t2003045\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tTraquelectomía simple por vía vaginal\t2003046\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tOoforectomía parcial o total, uni o bilateral (proc. aut.)\t2003001\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tAnexectomía y/o vac. de absceso tubo-ovárico, uni o bilateral.\t2003002\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tEmbarazo tubario, trat. quir.\t2003003\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tLigadura o sección uni o bilateral de las trompas (Madlener, Pomeroy, o similares) (proc. aut.)\t2003004\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tSalpingectomía uni o bilateral\t2003005\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tEsterilidad tubaria, operación plástica, uni o bilateral\t\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tEsterilidad tubaria, operación plástica uni o bilateral con microcirugía\t2003006\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tEsterilidad tubaria, operación plástica uni o bilateral sin microcirugía\t2003007\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tMiomectomía\t2003008\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tExtracción de DIU incrustado, por vía abdominal\t2003041\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tHisterectomía por vía abdominal, c/s anexectomía uni o bilat.\t\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tHisterectomía subtotal por vía abdominal\t2003009\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tHisterectomía total o ampliada por vía abdominal\t2003010\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tLigamento ancho: abscesos y/o hematomas y/o flegmones y/o quistomas y/o várices u otros, trat. quir. (proc. aut.)\t2003011\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tConización y/o amputación del cuello uterino, diagnóstica y/o terapéutica  c/s biopsia\t2003012\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tHisterectomía por vía vaginal\t2003014\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tHisterectomía total c/intervención incontinencia urinaria, cualquier técnica\t2003016\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tHisteropexia\t2003017\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tPlastía uterina (operación de Strassmann o similares)\t2003018\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tPolipectomía (uno o más) (proc. aut.)\t2003019\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tSinequia y/o estenosis cervical, trat. quir.\t2003020\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tDesgarro cervical trat. quir.\t2003030\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tIncompetencia cervical trat. quir.\t2003040\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tColpoceliotomía\t2003021\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tIncontinencia urinaria de esfuerzo, trat. quir. por vía vaginal (proc. aut.)\t2003022\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tProlapso anterior y/o posterior con repar., incontinencia urinaria por vía extravaginal o combinada\t2003023\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tProlapso anterior y/o posterior c/s trat. de incontinencia urinaria por vía vaginal, trat. quir.\t2003024\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tQuiste y/o desgarro y/o tabique vaginal, trat. quir.\t2003025\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tBartolinitis, vaciamiento y drenaje (proc. aut.)\t2003026\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tBartolinocistoneostomía o extirp. de la glándula\t2003027\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tVulvectomía simple\t2003029\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \t- Aborto retenido, vaciamiento de (incluye la inducción en los casos que corresponda)\t2004001\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \t- Raspado uterino diagnóstico o terapéutico por metrorragia o por restos de aborto\t2004002\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tAspiración manual endouterina (AMEU)\t2004007\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tTratamiento Farmacológico Ley IVE (incluye Consulta especialidad en Obstetricia y Ginecología y fármacos)\t2004008\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tCesárea c/s salpingoligadura o salpingectomía\t2004006\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tCesárea con histerectomía\t2004005\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tParto normal\t2004103\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tGINECOLOGIA Y OBSTETRICIA \tParto distócico vaginal\t2004113\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tIntubación vía lagrimal\t1202001\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tPuntos lagrimales, plastía de\t1202002\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tReconstitución de canalículos\t1202003\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tAbsceso, vaciamiento y/o drenaje de saco y/o glándula lagrimal\t1202004\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tDacriocistorrinostomía\t1202005\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tExtirpación de saco y/o glándula lagrimal\t1202006\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tReconstitución vía lagrimal en ausencia del saco\t1202007\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tExtirpación total o parcial de la glándula lagrimal \t1202008\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tTumor maligno  del saco, trat. quir. completo\t1202009\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tAbsceso, trat. quir. párpado o ceja\t1202010\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tBiopsia de párpado y/o anexos (proc. aut.)\t1202011\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tBlefarochalasis, plastía de\t1202012\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tBlefarofimosis, plastía de\t1202013\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tBlefarorrafia con blefarotomía posterior\t1202014\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tCantoplastía\t1202015\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tChalazión y otros tumores benignos (uno o más, unilateral), trat. quir. completo\t1202016\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tColoboma, plastía de\t1202017\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tEctropión, plastía de\t1202018\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tEntropión, plastía de\t1202019\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tEpicanto, plastía de\t1202020\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tPtosis, trat. quir.\t1202021\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tQuiste dermoide de la cola de la ceja, resec. plástica\t1202022\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tTumor maligno de párpado o ceja, trat. quir. completo\t1202023\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tXantelasma, trat. quir.\t1202024\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tHerida o dehiscencia de sutura de párpado, reparación\t1202071\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tTratamiento quirúrgico ptosis de la ceja\t1202080\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tHerida o dehiscencia de la conjuntiva, sutura de (proc. aut.)\t1202025\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tPterigión y/o pseudopterigión o su recidiva, extirpación\t1202026\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tSimbléfaron, resección de adherencias y plastía de\t1202027\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tExtirpación de tumor benigno de la conjuntiva\t1202028\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tAbsceso orbitario, trat. quir.\t1202029\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tCorrección de cavidad anoftálmica trat. completo\t1202030\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tCuerpo extraño orbitario (con orbitotomía)\t1202031\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tExanteración orbitaria o tumor orbitario, trat. quirúrgico completo\t1202032\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tOrbitotomía anterior\t1202033\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tOrbitotomía lateral descompresiva\t1202034\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tReconstrucción de paredes orbitarias\t1202072\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tBiopsia de globo ocular (proc. aut.)\t1202035\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tEnucleación o implante de prótesis ocular (proc. aut.)\t1202036\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tEnucleación con implante\t1202037\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tTratamiento quirúrgico completo del estrabismo unilateral o bilateral\t1202038\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tExanteración ocular (proc. aut.)\t1202039\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tSutura de lesión traumática de globo o musculos oculares (proc. aut.)\t1202040\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tCrioterapia y recesión conjuntival\t1202042\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tExtracción quir. de cuerpo extraño en cornea y/o esclera\t1202044\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tGlaucoma, trat. quir. por cualquier técnica\t1202045\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tHerida corneal o corneo-escleral o dehiscencia de sutura\t1202046\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tQueratectomía laminar\t1202047\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tRecubrimiento conjuntival\t1202050\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tRehabilitación superficie ocular (con injerto de mucosa)\t1202051\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tIridectomía periférica y/u óptica, (proc. aut.)\t1202053\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tTratamiento quirúrgico de lesión tumoral del iris o cuerpo ciliar\t1202054\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tHernia de iris y/o fístulas, reparación de\t1202074\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tDesprendimiento retinal, cirugía convencional (exoimplantes)\t1202056\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tTumor retinal o coroidal, diatermo y/o crio y/o fotocoagulación de\t1202058\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tVasculopatía retinal (excepto retinopatía proliferativa) diatermo y/o crio y/o fotocoagulación ( incluye endofotocoagulación intraquirùrgica)\t1202059\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tVitrectomía c/retinotomía (c/s inyección de gas o silicona)\t1202060\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tVitrectomía con inyección de gas o silicona\t1202061\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tVitrectomía con vitreófago (proc. aut)\t1202062\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tRetinopexia neumática\t1202075\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tDesprendimiento coroídeo o hemorragia coroídea, trat. quir.\t1202077\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \t- Facoéresis intracapsular o catarata secundaria o discisión y aspiración de masas\t1202063\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \t- Facoéresis extracapsular con implante de lente intraocular (incluye el valor de la prótesis)\t1202164\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tImplante secundario de lente intraocular\t1202065\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tAspiración esferular c/s capsulotomía\t1202066\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tExtracción o corrección de desplazamiento de lente intraocular\t1202076\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tFacoemulsificación\t1202079\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tRetinopatía proliferativa, (diabética, hipertensiva, eales y otras) panfotocoagulación trat. completo   (incluye endofotocoagulación intraquirúrgica )\t1202057\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tDiscisión de cápsula posterior\t1202067\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tIridotomía\t1202068\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tTrabeculoplastía o iridoplastía\t1202069\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tCirugía fotorrefractiva o fototerapéutica de córnea, cualquier técnica\t1202078\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tBlefaroplastia párpados inferiores, uni o bilateral\t1502029\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOFTALMOLOGIA \tBlefaroplastia párpados superiores, uni o bilateral\t1502030\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tBiopsia de párpado y/o anexos (proc. aut.)\t1202011\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tQuiste dermoide de la cola de la ceja, resec. plástica\t1202022\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tFístula preauricular complicada, trat. quir.\t1302003\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tExtirpación de tumor de conducto auditivo externo\t1302004\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tBiopsia buco-faríngea (proc. aut.)\t1302022\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tSección y/o resección frenillos cavidad bucal\t1302023\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tExtirpación de quiste o mucocele de glándula salival menor de labios\t1402022\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tQuistes y/o fístulas del conducto tirogloso, y/o branquial, y/o higroma, y/o fístula preauricular complicada, y/u otros quistes y/o tumores benignos, trat. quir.\t1402024\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tHeridas de la cara complicadas: 1 o varias de más de 5 cms. y/o ubicadas en bordes de párpados, labios o ala nasal y/o que comprometen músculos, conductos, vasos o nervios\t1502001\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tHeridas de la cara simples: 1 o varias de hasta 5 cms. que sólo comprometen piel\t1502002\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tImplante de silicona facial (cualquier zona o zonas)\t1502003\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tResección plástica de hasta 2 cicatrices (cualquier localización o tamaño)\t1502004\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tResección plástica de 3 o más cicatrices (cualquier localización o tamaño) \t1502005\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tInjertos  hasta 1% superficie corporal receptora\t1502006\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tInjertos  hasta 5% superficie corporal receptora\t1502007\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tInjertos hasta 10% superficie corporal receptora\t1502008\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tPiel total, cualquier tamaño (incluye tratamiento zona dadora y receptora)\t1502011\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tToma de injertos cartílago (auricular, costal o similares) c/u\t1502012\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tToma de injertos-óseo (costal, ilíaco, tibial o similares) c/u.\t1502013\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tPlastías en Z, hasta 3\t1502014\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tPlastías en Z, 4 y más\t1502015\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\t- Colgajos complejos (Abbe, Mustarda, Converse, Juri, Bakamjian o similar)\t1502016\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\t- Colgajos libres con microanastomosis (incluye toma del colgajo y las suturas neurovasculares)\t1502017\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\t- Colgajos musculares o musculocutáneos\t1502018\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\t- Colgajos osteomusculocutáneos\t1502019\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\t- Colgajos simples dos o más\t1502020\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\t- Colgajo simple único\t1502021\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tRidectomía cérvico-facial, un lado\t1502023\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tOrejas aladas o en asa, corrección plástica\t1502025\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tLóbulo auricular partido, corrección plástica (proc. aut)\t1502026\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tMalformación congénita compleja en orejas, cada plastía o plastías en tiempos diferentes\t1502027\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tPlastia de velo (cualquier técnica)\t1502035\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tGinecomastia, corrección plástica\t1502047\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tMamoplastía de reducción\t1502049\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tAbdominoplastia\t1502053\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tEscarectomía con resección ósea c/s colgajo de rotación\t1502054\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tTratamiento de escaras de decubito, con resección ósea y colgajos musculares o musculocutáneos\t1502055\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tEscarotomía hasta 10 % superficie corporal\t1502061\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tEscarotomía por cada 10 % adicional (o su fracción)\t1502062\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tEscarectomía hasta 1 % superficie corporal\t1502063\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tEscarectomía hasta 5 % superficie corporal\t1502064\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tEscarectomía  hasta 10% superficie corporal\t1502065\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tEscarectomía por cada 10% adicional (o su fracción) (Se cobrará cód. ad. una sóla vez por superficie entre el 11% y 50%).\t1502066\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tBiopsia de piel y/o mucosa por curetaje o sección tangencial c/s electro por 1 lesión\t1602201\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tCabeza, cuello, genitales hasta 3 lesiones: extirpación, reparación o biopsia, total o parcial, de lesiones benignas cutáneas por excisión\t1602202\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tResto del cuerpo hasta 3 lesiones: extirpación, reparación o biopsia, total o parcial, de lesiones benignas cutáneas por excisión\t1602203\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tCabeza, cuello y genitales desde 4 y hasta 6 lesiones: extirpación, reparación o biopsia, total o parcial, de lesiones benignas cutáneas por excisión\t1602204\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tResto del cuerpo desde 4 y hasta 6 lesiones: extirpación, reparación o biopsia, total o parcial, de lesiones benignas cutáneas por excisión\t1602205\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tExtirpación de lesiones benignas por sec tangencial, curetaje y/o fulguración hasta 15 lesiones\t1602206\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tHerida cortante o contusa complicada, reparación y sutura (más de 5 cm)\t1602221\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tHerida cortante o contusa no complicada, reparación y sutura (una o múltiple hasta 5 cms. de largo total que comprometa solo la piel)\t1602222\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tCabeza, cuello, genitales: extirpación de lesión benigna subepidérmica, incluye tumor sólido, quiste epidérmico y lipoma por lesión \t1602223\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tResto del cuerpo: extirpación de lesión benigna subepidérmica, incluye tumor sólido, quiste epidérmico y lipoma por lesión \t1602224\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tVaciamiento y curetaje quirúrgico de lesiones quísticas o abscesos\t1602225\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tOnicectomía total o parcial simple\t1602231\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tCirugía reparadora ungueal por proceso inflamatorio\t1602232\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tCuración por Médico, Quemadura o Similar  menor al 5% superficie corporal en pabellón\t1602240\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tCuración por Médico, Quemadura o Similar  5 a 10% superficie corporal en pabellón\t1602241\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tCuración por Médico, Quemadura o Similar mayor al 10 %  superficie corporal en pabellón\t1602242\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tHernia incisional o evisceración post-op. sin resección intestinal\t1802002\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tHernia inguinal, crural, umbilical, de la línea blanca o similares, recidivada o no, simple o estrangulada s/resección intest.c/u\t1802003\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tLaparotomía exploradora, c/s liberación de adherencias, c/s drenaje, c/s biopsias como proc. aut. o como resultado de una herida penetrante abdominal no complicada o de un hemoperitoneo postoperatorio o como tratamiento de una peritonitis (laparostomía contenida -máximo cuatro-, resuturas, etc.)\t1802004\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tPeritonitis difusa aguda, trat. quir. (proc. aut.) \t1802007\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tReconstitución  de tránsito en 2° tiempo de operación código 18-02-079\t1802080\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tApendicectomía y/o dren. absceso apendicular (proc. aut.)\t1802053\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tCierre de colostomía (proc. aut.)\t1802054\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tColostomía (proc. aut.)\t1802055\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tColostomía, complicaciones tardías, trat. quir.\t1802056\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tDivertículo de Meckel, trat. quir.\t1802057\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tEntero-enteroanastomosis o enterocoloanastomosis (proc. aut.)\t1802058\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tInvaginación intestinal, trat. quir.\t1802061\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tPersistencia conducto onfalomesentérico, trat. quir.\t1802062\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tQuiste uraco, trat. quir.\t1802063\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tOclusión intestinal con resección\t1802065\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tOclusión intestinal sin resección\t1802066\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tColectomía parcial o hemicolectomía\t1802067\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tReconstitución  tránsito post operación de Hartmann o sim.\t1802073\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tAbsceso ano rectal complejo, tratamiento quirúrgico\t1803001\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tAbsceso anorrectal simple, trat. quir.\t1803002\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tAbsceso sacrocoxígeo, drenaje\t1803003\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tBiopsia quirúrgica rectal (proc. aut.)\t1803004\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tFisura anal, repar. quir.\t1803017\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tHemorroidectomía (incluye otras operaciones complementarias en canal anal)\t1803018\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tHemorroides, trombectomía (proc. aut.)\t1803019\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tPólipo rectal, trat.quir. por vía anal\t1803026\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tUretroplastía sin substitución - uretrorrafía\t1902043\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tUretrotomía externa (proc. aut.)\t1902052\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tBiopsia quirúrgica de testículo y/o aspiración epididimaria.\t1902059\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tDescenso testicular con o sin hernia, cualquier tiempo, cualquier técnica\t1902060\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tDescenso testículo inguinal c/s hernioplastía\t1902061\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tEscroto, plastía de, proc. completo\t1902062\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tHidatidectomía unilat. c/s eversión de la vaginal (proc. aut.)\t1902063\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tHidrocele y/o hematocele, incluye quistes cordón y/o epidídimo y/o hidatidectomías y/o cirugía intravaginal del mismo lado \t1902064\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tOrquidectomía unilateral\t1902065\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tOrquidopexia unilateral\t1902066\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tQuistes del cordón, y/o epidídimo, extirpación; epididimotomía diagnóstica y/o terapéutica (proc. aut.)\t1902073\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tExploración escroto agudo. Incluye hematocele por trauma, destorsión y fijación testículo, hidatidectomía  y eversión bilateral si corresponde \t1902074\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tVaricocele unilateral y/o denervación cordón espermático (incluye quistes, hidátides e hidrocele mismo lado)\t1902075\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tCircuncisión (incluye sección de frenillo, y/o de sinequias bálano-prepuciales, y/o incisión dorsal c/s meatotomía)\t1902082\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tCirugía traumatismo peneano o curvaturas  adquiridas de la albugínea\t1902083\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tMeatotomía hombre y/o sección frenillo y/o incisión dorsal, (proc. aut.)\t1902084\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tTumor benigno y/o quiste y/o mama supernumeraria y/o aberrante o politelia, o biopsia quirúrgica extemporánea, trat. quir. (proc. aut)\t2002005\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
INFANTIL\tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tCIRUGIA PEDIATRICA\tQuiste y/o desgarro y/o tabique vaginal, trat. quir.\t2003025\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tAbsceso y/o hematomas oído externo, trat. quir.\t1302001\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tExtracción cuerpo extraño en conducto auditivo externo\t1302002\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tFístula preauricular complicada, trat. quir.\t1302003\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tExtirpación de tumor de conducto auditivo externo\t1302004\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tTumor maligno oído externo, trat. quir.\t1302005\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tEstapedectomía o estapedostomía \t1302006\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tMastoidectomía c/s sección cuerda del tímpano\t1302007\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tTratamiento quirúrgico de Mucositis timpánica, otitis media con efusión uni o bilateral\t1302008\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tOperación radical de oído\t1302009\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tReconstitución funcional de oído radicalizado\t1302011\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tTimpanoplastía funcional (cualquier tipo) c/s mastoidectomía\t1302012\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tPunción timpánica para inyección de medicamentos\t1302076\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tImplante activo de oído medio\t1302077\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tReconstitución plástica de conducto auditivo externo cartilaginoso\t1302013\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tExostosis u osteoma oído medio o externo, resección por cualquier vía  \t1302014\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tNeurectomía de Jacobson\t1302015\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tReconstitución de conducto auditivo externo, c/s timpanoplastía (incluye revisión de cadena osicular)\t1302016\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tTratamiento quirúrgico de tumor glómico timpánico\t1302017\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tLaberintectomía\t1302018\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tNeurinoma del acústico, trat. quir. vía translaberíntica y/o fosa media\t1302019\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tIntervención quirúrgica implante coclear\t1302074\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tDescompresión intraósea nervio facial c/s plastía\t1302020\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tLesiones a nivel del conducto auditivo interno, trat. quir.\t1302021\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tBiopsia buco-faríngea (proc. aut.)\t1302022\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tSección y/o resección frenillos cavidad bucal\t1302023\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tDrenaje de absceso o flegmón de piso de boca\t1302024\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tDrenaje de absceso o flegmón periamigdaliano\t1302025\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tDrenaje de absceso o flegmón retrofaríngeo o faringolaríngeo\t1302026\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tDrenaje de absceso o flegmón de vestíbulo bucal\t1302027\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tAdenoidectomía (proc. aut.)\t1302028\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tAmigdalectomía c/s adenoidectomía, uni o bilateral\t1302029\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tSI\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tExtracción de cálculos o tapones salivales\t1302030\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tTumor benigno de la mucosa bucal,  extirp. c/s  biopsia bucofaríngea\t1302031\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tTumor maligno de las amígdalas, trat. quir.\t1302032\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tExtirpación de  tumor benigno de la base de la lengua                                                                                      \t1302033\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tExtirpación tumor maligno de base de lengua\t1302034\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tFaringoplastía (cualq. técn.), c/s desplazamiento de colgajos\t1302035\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tFibroangioma del rinofarinx, trat. quir.\t1302036\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tGlosectomía total\t1302037\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tAbscesos y hematoma del tabique nasal, trat. quir.\t1302038\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tArteria esfenopalatina, cauterización por vía nasal\t1302039\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tArteria maxilar interna, ligadura de (por vía transmaxilar)\t1302040\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tLigadura de arterias etmoidales anteriores\t1302041\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tTurbinectomía o cauterización de cornetes, cualquier técnica \t1302042\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tConducto y/o seno lagrimal, obstrucción del, trat. quir. por vía nasal\t1302043\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tEtmoidectomía endo o exonasal\t1302044\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tCirugía de fosa pterigo palatina\t1302092\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tTratamiento quirúrgico de las fistulas buco-sinusales o buco-nasales  y/o retiro cuerpos extraños del seno maxilar\t1302045\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tFract. nasal reciente, cerrada o expuesta, reducción c/s inmovilización \t1302046\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tNervio vidiano, sección del (por cualquier vía)\t1302047\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tPerforación del tabique, trat. quir.\t1302048\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tTratamiento quirúrgico pólipo nasal\t1302049\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tRinitis atrófica, trat. por inclusión submucosa, con cualquier material, uni o bilateral\t1302050\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tRinofima, trat. quir.\t1302051\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tRinoplastía y/o septoplastía, cualquier técnica\t1302052\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tSeno esfenoidal, abertura por cualquier vía \t1302053\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tTratamiento quirúrgico de seno frontal, cualquier vía\t1302054\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tAntrostomía seno maxilar, cualquier vía\t1302055\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tSinequia nasal, trat. quir.\t1302056\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tTumor nasal, extirp. por rinotomía lateral\t1302057\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tVaciamiento etmoidal por vía nasal c/s polipectomía\t1302058\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tAritenoidectomía vía endoscópica\t1302059\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tAritenoidectomía vía externa\t1302060\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tAbducción de aritenoides, aritenoidopexia\t1302103\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tDecorticación de cuerdas vocales c/microscopio\t1302061\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tCordectomía, sinequia y otras malformaciones, tratatamiento quirúrgico por endoscópica (incluye laser)\t1302104\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tSubluxación articulación cricotiroídea\t1302105\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tTumor benigno de cuerdas vocales, trat. quirúrgico por vía abierta \t1302062\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tTumor benigno de cuerdas vocales, trat. quirúrgico por vía endoscópica\t1302063\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tCordectomía, resección de sinequia y otras malformaciones, trat. quirúrgico por vía externa \t1302064\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tEstenosis laringotraqueales y/o faríngeas, trat. quir. por vía abierta (incluye reconstrucción laringotraqueal) \t1302065\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tLaringectomía parcial o subtotal (cualquier técnica)\t1302066\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tLaringectomía total más faringectomía parcial\t1302067\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tLaringectomía total más faringectomía total y/o esofagectomía cervical\t1302068\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tLaringocele, trat. quir.\t1302069\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tPapilomas laríngeos, trat. quir. (por sesión)\t1302070\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tParálisis de cuerdas vocales, trat. quir. cualquier técnica\t1302071\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tTraqueostomía (proc. aut.)\t1302072\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tEstenosis laringotraqueales y faríngeas, trat. quir. por vía endoscópica (incluye laser) \t1302073\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPABELLON QUIRURGICO \tINTERVENCION QUIRURGICA \tOTORRINOLARINGOLOGIA \tFractura laríngea, reducción abierta c/s microplacas\t1302075\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO\tPROCESO QUIRURGICO \tPREQUIRURGICO BOX \tCONSULTA ESPECIALIDAD\tCIRUGIA ADULTO\tCONSULTA MEDICA ESPECIALIDAD\t0101312\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO\tPROCESO QUIRURGICO \tPREQUIRURGICO BOX \tCONSULTA ESPECIALIDAD\tGINECOLOGIA  Y OBSTETRICIA\tCONSULTA MEDICA ESPECIALIDAD\t0101308\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO\tPROCESO QUIRURGICO \tPREQUIRURGICO BOX \tCONSULTA ESPECIALIDAD\tMEDICINA INTERNA\tCONSULTA MEDICA ESPECIALIDAD\t0101307\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO\tPROCESO QUIRURGICO \tPREQUIRURGICO BOX \tCONSULTA ESPECIALIDAD\tCARDIOLOGIA\tCONSULTA MEDICA ESPECIALIDAD\t0101301\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPREQUIRURGICO BOX \tCONSULTA ESPECIALIDAD\tANESTESIOLOGIA\tCONSULTA MEDICA ESPECIALIDAD\t0101329\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPREQUIRURGICO BOX \tATENCION DE ENFERMERIA \tENFERMERIA PERIOPERATORIA \tCONSULTA INTEGRAL DE ENFERMERIA \t0101008\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPREQUIRURGICO BOX \tATENCION DE ENFERMERIA \tENFERMERIA PERIOPERATORIA \tCONSULTORIA TELEFONICA \t\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPREQUIRURGICO BOX \tPROCEDIMIENTO DE ENFERMERIA \tENFERMERIA PERIOPERATORIA \tTOMA DE MUESTRA DE SANGRE \t\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPREQUIRURGICO BOX \tPROCEDIMIENTO DE ENFERMERIA \tENFERMERIA PERIOPERATORIA \tTOMA DE MUESTRA DE ORINA \t\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPREQUIRURGICO BOX \tPROCEDIMIENTO DE ENFERMERIA \tENFERMERIA PERIOPERATORIA \tTOMA DE MUESTRA DE ISOPADO NASOFARINGEO\t\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPREQUIRURGICO BOX \tPROCEDIMIENTO DE ENFERMERIA \tENFERMERIA PERIOPERATORIA \tTOMA DE ELECTROCARDIOGRAMA \t1701001\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPREQUIRURGICO BOX \tATENCION PREQUIRURGICA \tENFERMERIA PERIOPERATORIA \tCONSULTORIA TELEFONICA \t\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPREQUIRURGICO PREPARACION  \tHOSPITALIZACION QUIRURGICA \tSALA DE ATENCION PERIOPERATORIA AMBULATORIA \tATENCION INTEGRAL PERIOPERATORIA EN CIRUGIA MAYOR AMBULATORIA \t\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPREQUIRURGICO SALA DE HOSPITALIUZACION  \tHOSPITALIZACION QUIRURGICA \tSALA DE HOSPITALIZACION QUIRURGICA \tDia Cama de Hospitalización Integral Cuidados Básicos area de cuidados perioperatorios\t0201010\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPREQUIRURGICO SALA DE HOSPITALIUZACION  \tHOSPITALIZACION QUIRURGICA \tSALA DE HOSPITALIZACION QUIRURGICA \tDia Cama de Hospitalización Integral Cuidados Medios Aarea cuidados perioperatorios \t0201110\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPREQUIRURGICO SALA DE HOSPITALIUZACION  \tHOSPITALIZACION QUIRURGICA \tSALA DE HOSPITALIZACION \tATENCION EN HOSPITALIZACION TRANSITORIA \t\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPREQUIRURGICO BOX \tPROCEDIMIENTO DE ENFERMERIA \tENFERMERIA PERIOPERATORIA \tVisita a domicilio por enfermera\t0104004\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPREQUIRURGICO BOX \tPROCEDIMIENTO DE ENFERMERIA \tENFERMERIA PERIOPERATORIA \tVisita a domicilio por auxiliar de enfermería\t0104003\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPREQUIRURGICO BOX \tPROCEDIMIENTO DE ENFERMERIA \tENFERMERIA PERIOPERATORIA \tCURACION SIMPLE \t0106002\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPREQUIRURGICO BOX \tPROCEDIMIENTO DE ENFERMERIA \tENFERMERIA PERIOPERATORIA \tCURACION COMPLEJA \t\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
ADULTO/ INFANTIL \tPROCESO QUIRURGICO \tPREQUIRURGICO BOX \tPROCEDIMIENTO DE ENFERMERIA \tENFERMERIA PERIOPERATORIA \tADMINISTRACION DE TRATAMIENTOAMBULOATORIO (EV, IM, SC)\t\t\tACTUAL\t\tHOSPITAL DE SAN CARLOS (SSÑ)\tNO\t
~~~
