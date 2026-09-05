---
_manifest:
  urn: "urn:kora:artefacto:koraficacion-knowledge"
  type: artefacto
  provenance:
    created_by: "OpenAI Codex"
    created_at: "2026-06-04"
    source: "Construccion fresca KORA/MD para recuperar la capacidad legacy KODA de curacion y deshidratacion documental. La autoridad normativa es md-spec + knowledge-spec; las specs legacy KODA y agent_koda_transformer solo aportan patrones operativos verificados: skeleton/meat/fat, telegrafizacion, deduplicacion, FS/CR contextualizado e iteracion auditada. v1.0.1 reemplaza el umbral rigido CR>1.5 por IDC: Indice de Deshidratacion Contextual."
version: "1.0.1"
status: activo
nombre: koraficacion-knowledge
descripcion: "Transforma, audita e itera documentos humanos hacia artefactos de conocimiento KORA/MD con alta fidelidad, compresion semantica, deduplicacion y control FS/IDC."
tags: [kora, knowledge, koraficacion, curacion, deshidratacion, fidelidad, compresion, markdown]
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 0
      xi: 2
      lambda: 0
      phi: 1
      sigma: [2, 1, 3, 3, 1]
    presentacion: accion-primaria
    atlas:
      arnes_categorico: disciplina
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo: [claude-code, codex, opencode, openclaw]
    nivel_prescripcion: alto
    conocimiento_permitido:
      - "urn:kora:kb:gobernanza"
      - "urn:kora:kb:md-spec"
      - "urn:kora:kb:knowledge-spec"
      - "urn:kora:kb:autoria-spec"
      - "urn:fxsl:kb:icas-preservacion"
      - "urn:fxsl:kb:icas-adjunciones"
      - "urn:fxsl:kb:icas-calidad-riesgo"
    componible_con:
      - "urn:kora:artefacto:custodio-kora"
      - "urn:kora:artefacto:cat-thinking"
      - "urn:dev:artefacto:ship-discipline"
artefacto:
  perfil:
    dominio:
      - kora
      - knowledge
      - KORA/MD
      - curacion-documental
      - deshidratacion-semantica
      - auditoria-fidelidad
    disparadores:
      - "transformar un documento fuente a artefacto de conocimiento KORA/MD"
      - "curar, deshidratar, koraficar o reducir tokens preservando informacion"
      - "auditar original vs artefacto KORA/MD por perdida de informacion"
      - "iterar una transformacion hasta FS=100% e IDC coherente con el perfil documental"
      - "recuperar calidad legacy KODA sin volver a YAML KODA"
    salidas:
      - "borrador KORA/MD en artifacts/knowledge/_SCRIPTORIUM/REVIEW/{ns}/"
      - "reporte de fidelidad con hechos preservados, comprimidos, omitidos y agregados"
      - "metricas FS/IDC y hallazgos de auditoria mecanica"
      - "plan de iteracion o rechazo si la transformacion perdio meat"
  plan:
    estado_inicial: triaje-fuente
    estado_terminal: draft-auditado-o-rechazado
    estados:
      - triaje-fuente
      - inventariar-skeleton-meat-fat
      - segmentar-si-corresponde
      - comprimir-semantica
      - deduplicar-ssot
      - realizar-superficie
      - inyectar-frontmatter
      - auditar-fidelidad
      - iterar-o-emitir
  interfaz:
    herramientas: [Read, Grep, Glob, Bash, Write]
    permisos: "Lectura del documento fuente y specs KORA; escritura acotada a artifacts/knowledge/_SCRIPTORIUM/REVIEW/, reportes de auditoria, tests o docs de soporte cuando el operador pide curacion. No promueve ni publica sin instruccion explicita."
    protocolos:
      entrada: "path o contenido fuente, namespace/id destino opcional, familia documental, criterio de cierre y permiso de escritura"
      salida: "artefacto KORA/MD borrador, reporte FS/CR, evidencia de auditoria y deuda residual"
  invariantes:
    reglas_duras:
      - "La salida es Markdown KORA/MD; no emitir YAML KODA ni familia atomic retirada."
      - "La fuente normativa es md-spec + knowledge-spec; legacy KODA es solo antecedente operacional."
      - "Preservar skeleton y meat; eliminar fat. Estructura, tablas, listas, cifras, fechas, condiciones, excepciones y referencias son meat."
      - "FS=100% es obligatorio. Si hay hechos omitidos o agregados no justificados, la transformacion falla."
      - "El CR crudo no es gate rigido. Medir eficiencia con IDC: CR observado calibrado contra expectativa del perfil documental."
      - "No resumir hechos distinguibles para comprimir. Deduplicar solo por equivalencia semantica real."
      - "No cortar documentos grandes dentro de tablas, listas o parrafos; segmentar por fronteras naturales."
      - "La realizacion superficial debe sonar a conocimiento curado, no a dump de campos ni labelese."
      - "Todo borrador con URN debe entrar en _SCRIPTORIUM/REVIEW/{ns}/ con status=borrador hasta promote."
      - "Antes de cerrar, ejecutar auditoria mecanica disponible y una auditoria semantica original vs salida."
    compromisos_eticos:
      transparency: "Alta; separar hecho preservado, compresion editorial, inferencia y deuda residual."
      accountability: "Alta; no publicar conocimiento curado sin declarar fuente, metricas y limitaciones de fidelidad."
---

# koraficacion-knowledge

## Proposito

Transformar documentos humanos en artefactos de conocimiento KORA/MD con la
calidad que antes se obtenia con KODA: alta fidelidad, menor token footprint,
estructura recuperable y revision iterativa contra el original.

La skill no revive el lenguaje YAML KODA. El destino es siempre Markdown
KORA/MD conforme a `urn:kora:kb:md-spec` y el pipeline de
`urn:kora:kb:knowledge-spec`.

## Cuando Usar

- Convertir PDF/OCR/TXT/MD/DOCX exportado o texto humano a KORA/MD.
- Curar y deshidratar documentos manteniendo `FS=100%`.
- Comparar original vs borrador KORA/MD y reparar perdida de informacion.
- Preparar drafts en `_SCRIPTORIUM/REVIEW/{ns}/` antes de `kora promote`.
- Iterar transformaciones largas por segmentos con auditoria acumulada.

## Cuando No Usar

- Crear agents o skills: usar `kora-agentic-lifecycle`.
- Emitir specs normativas: usar `custodio-kora` y `spec-md`.
- Publicar directo en `artifacts/knowledge/{ns}/` sin pasar por REVIEW.
- Reintroducir `atomic`, `atomize` o YAML KODA como formato productivo.

## Canon Minimo

Antes de cambiar un artefacto, leer o resolver:

1. `urn:kora:kb:md-spec` para envelope, telegrafizacion, familias,
   koraficacion, FS, CR e IDC.
2. `urn:kora:kb:knowledge-spec` para URN, lifecycle, REVIEW, promote y
   relations.
3. `urn:kora:kb:gobernanza` si hay duda de precedencia, namespace o lifecycle.

Lectura categorial: `DocHumano -> KORA/MD` debe comportarse como un funtor
fiel sobre los hechos relevantes. Preserva identidad estructural y composicion
de relaciones; olvida solo fat declarado. Esta conclusion se apoya en
`urn:fxsl:kb:icas-preservacion`. La relacion ida/vuelta entre original y
auditoria es heuristica tipo adjuncion, no teorema; ver
`urn:fxsl:kb:icas-adjunciones`.

## Workflow

### 1. Triage de fuente

Clasificar:

- tipo: texto limpio, OCR/export roto, tabla, procedimiento, corpus largo,
  documento legal/normativo, guia, libro, paper.
- largo y necesidad de segmentacion.
- densidad: cifras/fechas/tablas/listas/referencias.
- destino: namespace, slug, familia (`note` por defecto; `bok` si corpus
  extendido).

Si falta destino, proponer `artifacts/knowledge/_SCRIPTORIUM/REVIEW/{ns}/{slug}.md`
y pedir confirmacion solo si hay riesgo de namespace incorrecto.

### 2. Inventario skeleton/meat/fat

Antes de escribir, inventariar:

- `skeleton`: titulos, jerarquia, tablas, listas, orden, dependencias.
- `meat`: hechos, definiciones, cifras, fechas, condiciones, excepciones,
  requisitos, ejemplos, referencias y relaciones.
- `fat`: saludos, transiciones, hedging, retorica, repeticiones, boilerplate.

No transformar un documento largo sin inventario. Si el documento excede el
contexto practico, segmentar por fronteras naturales y mantener ledger global
de hechos.

### 3. Compresion semantica

Aplicar `md-spec §5.4`:

- eliminar fat sin tocar meat.
- promover condiciones a tablas.
- promover enumeraciones embebidas a listas.
- nominalizar solo si mejora densidad sin destruir naturalidad tecnica.
- preservar idioma.
- preservar todas las cifras, fechas, plazos, excepciones y referencias.

### 4. Deduplicacion SSOT

La reduccion de tokens viene sobre todo de deduplicar, no de resumir.

Reglas:

- Si un concepto aparece varias veces con el mismo significado, definirlo una
  vez y referenciarlo estructuralmente por heading, tabla o frase breve.
- Si dos ocurrencias difieren en condicion, alcance, fecha o excepcion, son
  hechos distintos.
- Si hay tension entre fuentes o secciones, conservar la tension; no fusionar.

### 5. Realizacion superficial

La salida debe ser KORA/MD legible:

- headings recuperables, sin `...`.
- listas/tablas solo cuando aportan estructura.
- nada de `Campo | Valor` salvo catalogo real.
- nada de labelese tipo `Asunto`, `Contenido`, `Tipo`, `Path`.
- prose tecnica breve cuando sea mas clara que una lista forzada.

### 6. Frontmatter al final

Agregar frontmatter solo cuando el cuerpo esta estable:

```yaml
---
_manifest:
  urn: "urn:{ns}:kb:{slug}"
  provenance:
    created_by: "FS"
    created_at: "YYYY-MM-DD"
    source: "{path, hash o descripcion de fuente}"
version: "0.1.0"
status: borrador
tags: [{tag1}, {tag2}, {tag3}]
lang: "es"
extensions:
  kora:
    family: note
---
```

Usar `status: borrador` en REVIEW. `publicado` solo despues de `kora promote`.

### 7. Auditoria de fidelidad e IDC

Ejecutar dos capas:

1. Auditoria mecanica:
   `python3 artifacts/skills/kora/koraficacion-knowledge/scripts/audit_korafication.py <fuente> <artefacto> --json`
2. Auditoria semantica:
   revisar ledger de hechos original vs salida.

El script detecta perdida mecanica de cifras, fechas, URLs, frontmatter ausente,
headings truncados y labelese. Tambien reporta `IDC`:

```text
CR  = len(fuente) / len(salida)
IDC = CR observado / CR esperado para el perfil documental
```

Perfiles orientativos:

| Perfil | CR esperado | Uso |
| --- | ---: | --- |
| `prosa-redundante` | 1.70 | narrativa, ensayos, documentos con transiciones y repeticion |
| `mixto` | 1.40 | guias, notas tecnicas, politicas con secciones y listas |
| `denso-estructurado` | 1.15 | tablas, normas, procedimientos, documentos con muchas cifras |
| `fuente-ya-densa` | 1.00 | markdown tecnico, outlines, glosarios o corpus ya comprimido |

Interpretacion:

- `IDC>=1.00`: deshidratacion adecuada para el perfil.
- `0.85<=IDC<1.00`: aceptable con revision editorial.
- `IDC<0.85`: buscar grasa, redundancia o realizacion superficial pobre.

No reemplaza el juicio semantico: solo bloquea errores baratos y orienta la
revision de eficiencia.

### 8. Iterar o emitir

Cerrar como:

- `draft-auditado`: FS=100%, IDC aceptable o justificado, lint limpio.
- `needs-rework`: omisiones, agregados, labelese, CR bajo con grasa remanente.
- `blocked`: fuente ilegible, namespace ambiguo, texto incompleto o falta de
  permiso para escribir.

## Criterios De Rechazo

Rehacer si ocurre cualquiera:

- se perdio una condicion, excepcion, cifra, fecha, referencia o item de lista.
- se agrego una inferencia no declarada como inferencia.
- se fusionaron hechos distinguibles para mejorar CR.
- el output parece dump de campos.
- se filtro ruido OCR como contenido sustantivo.
- IDC<0.85 y queda grasa evidente, redundancia no deduplicada o mala realizacion superficial.
- `lint-md` falla.

## Recursos

### Referencias

- `referencias/playbook-koraficacion.md`: procedimiento operativo ampliado.
- `referencias/auditoria-fidelidad.md`: ledger, FS/CR y loop de reparacion.
- `referencias/legacy-koda-bridge.md`: que se absorbe del KODA legacy y que se
  descarta.

### Scripts

- `scripts/audit_korafication.py`: auditoria mecanica determinista.
