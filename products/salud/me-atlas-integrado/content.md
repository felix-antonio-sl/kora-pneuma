---
urn: urn:salud:kb:me-atlas-integrado
nombre: me-atlas-integrado
version: 1.0.0
estado: publicado
descripcion: "Atlas integrado de Medicina de Emergencia: Este atlas une el corpus `salud/med-emergencia` como un solo cuerpo clinico"
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/salud/med-emergencia/atlas-integrado.md (sha256:1a246d1672840340dc6c381b489a312736532ba4636d4effb00c2f6d653cdcc9) el 2026-06-12; cuerpo byte-fiel (renombrado de atlas-integrado.md a me-atlas-integrado.md por lugar-coincide). Fuente original: Integracion organica de artifacts/knowledge/salud/med-emergencia sin perdida de informacion."
autor: FS
creado: 2026-04-27
lang: es
tags: [medicina-emergencia, atlas, integracion, rutas-clinicas, urgencias, salud]
familia: bok
depende: [urn:salud:kb:med-emergencia]
cita: [urn:salud:kb:me-body-of-knowledge-diferencial, urn:salud:kb:me-toc-body-of-knowledge, urn:salud:kb:me-perfil-urgenciologo, urn:salud:kb:me-razonamiento-clinico, urn:salud:kb:me-evaluacion-primaria, urn:salud:kb:me-sincope, urn:salud:kb:me-dolor-toracico, urn:salud:kb:me-disnea, urn:salud:kb:me-tec-leve, urn:salud:kb:me-compromiso-conciencia, urn:salud:kb:me-mareo-vertigo, urn:salud:kb:me-deficit-neurologico, urn:salud:kb:me-cefalea-convulsiones, urn:salud:kb:me-dolor-abdominal, urn:salud:kb:me-fiebre-sin-foco, urn:salud:kb:me-hemorragia-digestiva, urn:salud:kb:me-infecciones-gastrointestinales, urn:salud:kb:me-infecciones-respiratorias-altas, urn:salud:kb:me-infecciones-respiratorias-bajas, urn:salud:kb:me-sintomas-urinarios, urn:salud:kb:me-traumatismos-frecuentes]
---

# Atlas integrado de Medicina de Emergencia

Este atlas une el corpus `salud/med-emergencia` como un solo cuerpo clinico.
No reemplaza los documentos fuente ni fusiona mecanicamente los shards. Define
como se compone el corpus: que pieza orienta, que pieza razona, que pieza cubre
presentaciones y como se baja desde una consulta clinica a los nodos correctos.

## Principio de integracion

La unidad clinica basica del corpus es:

`presentacion aguda + acuidad + contexto + tiempo + recursos + disposicion`

Cada consulta debe entrar por esa unidad, no por organo aislado ni por
diagnostico definitivo prematuro.

## Capas canonicas

| Capa | URN | Funcion |
|------|-----|---------|
| Entrada canonica | `urn:salud:kb:med-emergencia` | Punto de entrada y contrato de corpus |
| Atlas integrado | `urn:salud:kb:me-atlas-integrado` | Mapa de composicion, rutas y partes |
| BOK diferencial | `urn:salud:kb:me-body-of-knowledge-diferencial` | Doctrina amplia, fundamentos, cobertura y competencias |
| TOC BOK | `urn:salud:kb:me-toc-body-of-knowledge` | Cobertura curricular y navegacion estructural |
| Perfil emergenciologo | `urn:salud:kb:me-perfil-urgenciologo` | Identidad profesional y competencias diferenciales |
| Razonamiento clinico | `urn:salud:kb:me-razonamiento-clinico` | Loop de decision bajo incertidumbre y amenaza vital |
| Evaluacion primaria | `urn:salud:kb:me-evaluacion-primaria` | ABC/ABCDE, primera impresion, estabilizacion y reevaluacion |
| Presentaciones | familia `me-...` | Nodos operativos por motivo de consulta o sindrome |

## Ruta de uso

1. Entrar por `urn:salud:kb:med-emergencia`.
2. Usar este atlas para clasificar la consulta en una ruta.
3. Leer siempre `evaluacion-primaria` y `razonamiento-clinico` cuando haya
   decision clinica, disposicion o incertidumbre.
4. Leer la presentacion canonica correspondiente.
5. Usar BOK y TOC para cubrir lagunas, fundamentos, competencias o temas no
   suficientemente desarrollados en la presentacion.
6. Declarar vacio de corpus cuando no exista nodo operativo publicado.

## Rutas clinicas publicadas

| Ruta | URN canonico | Archivos materiales |
|------|--------------|---------------------|
| Sincope | `urn:salud:kb:me-sincope` | `sincope.md`, `sincope--p02.md` |
| Dolor toracico no traumatico | `urn:salud:kb:me-dolor-toracico` | `dolor-toracico.md`, `dolor-toracico--p02.md` |
| Disnea aguda | `urn:salud:kb:me-disnea` | `disnea.md`, `disnea--p02.md` |
| TEC leve | `urn:salud:kb:me-tec-leve` | `tec-leve.md` |
| Compromiso de conciencia | `urn:salud:kb:me-compromiso-conciencia` | `compromiso-conciencia.md`, `compromiso-conciencia--p02.md`, `compromiso-conciencia--p03.md` |
| Mareo y vertigo | `urn:salud:kb:me-mareo-vertigo` | `mareo-vertigo.md` |
| Deficit neurologico | `urn:salud:kb:me-deficit-neurologico` | `deficit-neurologico.md`, `deficit-neurologico--p02.md`, `deficit-neurologico--p03.md`, `deficit-neurologico--p04.md`, `deficit-neurologico--p05.md`, `deficit-neurologico--p06.md` |
| Cefalea y convulsiones | `urn:salud:kb:me-cefalea-convulsiones` | `cefalea-convulsiones.md` |
| Dolor abdominal | `urn:salud:kb:me-dolor-abdominal` | `dolor-abdominal.md`, `dolor-abdominal--p02.md` |
| Fiebre sin foco | `urn:salud:kb:me-fiebre-sin-foco` | `fiebre-sin-foco.md`, `fiebre-sin-foco--p02.md` |
| Hemorragia digestiva | `urn:salud:kb:me-hemorragia-digestiva` | `hemorragia-digestiva.md`, `hemorragia-digestiva--p02.md` |
| Infecciones gastrointestinales | `urn:salud:kb:me-infecciones-gastrointestinales` | `infecciones-gastrointestinales.md` |
| Infecciones respiratorias altas | `urn:salud:kb:me-infecciones-respiratorias-altas` | `infecciones-respiratorias-altas.md`, `infecciones-respiratorias-altas--p02.md` |
| Infecciones respiratorias bajas | `urn:salud:kb:me-infecciones-respiratorias-bajas` | `infecciones-respiratorias-bajas.md` |
| Sintomas urinarios | `urn:salud:kb:me-sintomas-urinarios` | `sintomas-urinarios.md` |
| Traumatismos frecuentes | `urn:salud:kb:me-traumatismos-frecuentes` | `traumatismos-frecuentes.md`, `traumatismos-frecuentes--p02.md` |

## Agrupacion organica

### Fisiologia y riesgo inmediato

- Evaluacion primaria.
- Razonamiento clinico.
- Disnea.
- Dolor toracico.
- Compromiso de conciencia.
- Sincope.

### Neurologico

- Deficit neurologico.
- Cefalea y convulsiones.
- Mareo y vertigo.
- TEC leve.
- Compromiso de conciencia.

### Dolor y sangrado

- Dolor toracico.
- Dolor abdominal.
- Hemorragia digestiva.
- Sintomas urinarios.
- Traumatismos frecuentes.

### Infeccioso y respiratorio

- Fiebre sin foco.
- Infecciones gastrointestinales.
- Infecciones respiratorias altas.
- Infecciones respiratorias bajas.
- Sintomas urinarios.

### Trauma y lesiones frecuentes

- TEC leve.
- Traumatismos frecuentes.
- Deficit neurologico cuando hay deficit focal post-trauma.
- Dolor abdominal cuando el mecanismo o la exploracion sugieren compromiso abdominal.

## Regla de composicion para respuestas

Una respuesta basada en este corpus debe combinar:

1. acuidad y amenaza vital;
2. ABC/ABCDE y estabilizacion inicial;
3. presentacion clinica especifica;
4. diferencial priorizado por dano, probabilidad y tiempo-dependencia;
5. estudios o intervenciones que cambian conducta;
6. reevaluacion;
7. disposicion;
8. limites del corpus si la pregunta excede los nodos publicados.

## Regla de preservacion

Los archivos `--pNN` son partes materiales del documento raiz indicado por
`extensions.kora.shard_root_urn`. No deben tratarse como corpus independientes
ni como entradas clinicas separadas. La entrada clinica canonica es siempre el
URN sin sufijo `pNN`.

## Limite de seguridad

Este corpus apoya razonamiento y navegacion de conocimiento para profesionales
de urgencia. No prescribe de forma autonoma, no reemplaza guias locales ni
reemplaza el juicio clinico del equipo tratante.
