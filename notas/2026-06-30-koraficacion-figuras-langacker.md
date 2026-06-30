# nota: koraficación de figuras en KORA — aprendizajes de la sesión 2026-06-30

**Artefactos tocados**: `langacker-cg-fundamentos` (caps. 1-3), `langacker-cg-clases-y-construcciones` (caps. 4-8), `langacker-cg-estructuras` (caps. 9-12), `langacker-cg-fronteras` (caps. 13-14).

## El problema

CG de Langacker (2008) es una fuente sistemática con **~188 figuras** numeradas por capítulo (1.1 a 14.15). El artefacto korificado reemplaza las figuras por blockquotes `> *Recursos gráficos descartados*` que enumeran los temas pero no describen qué contienen los diagramas. Resultado: el lector koral puede seguir la prosa pero pierde completamente el hilo visual de los argumentos (p. ej. qué se profilea en 4.1 vs. 4.2, o cómo se diferencia el grounding clausal del nominal en los caps. 9-10).

La instrucción explícita fue: **descripciones textuales conservadas por capítulo; los diagramas como objetos visuales se consultan en el original fuente**. Es decir, el artefacto debe **nombrar y describir** cada figura en 1-3 frases, manteniendo numeración e orden, sin pretender reemplazar el diagrama visual.

## Procedimiento que funcionó

1. **Localizar captions en el .txt**: `grep -nE "^[fF]igure X\.Y" archivo.txt` da la línea donde el label aparece suelto; suele estar cerca del caption real (encontrado en cuerpo). Algunas captions sólo existen integradas en párrafo (Figure 4.2 shows that…) — ahí `grep -nE "figure X\.Y"` sin `^` los encuentra.
2. **Leer ±30-60 líneas alrededor**: el caption suele venir inmediatamente arriba o abajo (los `.txt` de epub de calibre suelen numerar las figuras como linebreaks independientes).
3. **Validar con imágenes**: las imágenes `000000.jpg`–`000209.jpg` están en `images/`. Abrir varias con Read permite mapear figuras a diagramas CG (con cajas, elipses, flechas, líneas de correspondencia). Las figs. 4.1–8 son de **rango ~000050–000150**, 9–14 son ~**000150–000210**. Esto fue lento pero necesario para figs cuya descripción es ambigua solo desde el texto (p. ej. si el .txt dice "panels (a)–(e)" sin más, las imágenes aclaran cuáles son y qué contienen).
4. **Consolidar paneles**: cuando una figura tiene (a)/(b)/(c)/etc., una sola entrada con `Panel (a): … Panel (b): …`, salvo que un panel sea conceptualmente distinto (entonces entradas separadas `4.4(a)`).
5. **Marcar gaps**: figs. 13.13/14/15 (cap. 13) parecen faltar del epub; merecen `— (no legible en la fuente disponible)` y nota al operador más que inventar.
6. **Editar artefactos por bloque**: 4 artefactos, 1 commit atómico por artefacto (commit messages semánticos con alcance granular).

## Decisiones

- **No inventar contenido que no esté en fuente**. Si el `.txt` no da caption explícito y la imagen es ambigua, marcar `—` antes de fabular primitivos visuales.
- **No tocar el cuerpo korificado**: solo blockquotes `Recursos gráficos descartados` y cláusula de figuras del campo `fuente:`. El resto del artefacto (prosa, secciones) es intocable.
- **Numeración del libro conservada aunque tenga saltos** (instrucción explícita). No reordenar ni "rellenar" huecos.
- **Descartes de Parts/References/Index preservados**; el campo `fuente:` solo cambia la cláusula de figuras.
- **Verificación**: `kora.py velar --estricto` debe pasar 13/13 después de los edits (la prosa sigue siendo pública y los placeholders siguen placeholders en forma lista).

## Formato final

Después del placeholder convertido:

```markdown
## N. Título del capítulo

**Recursos gráficos del capítulo N** (figs. N.1–N.X del fuente; descripciones textuales, los diagramas se consultan en el original):

- **N.1** — [descripción 1-3 frases: primitivos visuales + contenido semántico + función argumentativa]
- **N.2** — [descripción…]
```

Y la cláusula de figuras del campo `fuente:` cambia de:

> "figuras (notación diagramática sistemática de CG —cajas, elipses, flechas, correspondencias, scanning—; no reproducible en KORA/MD; un placeholder por capítulo enumera las figuras omitidas)"

a:

> "figuras (descripciones textuales conservadas por capítulo; los diagramas como objetos visuales se consultan en el original fuente)"

## Atajos que NO funcionaron

- **Subagentes paralelos**: lanzados con instrucción explícita de inspeccionar imágenes junto al texto. Devolvieron `No tengo el JSON` o `JSON vacío` — el contexto del subagente no retiene el contenido de su propia respuesta. Para **~188 figuras** el subagente no es viable: requiere inspección visual + textual sincronizada.
- **Inspección sola del .txt sin imágenes**: imposible para figs. que no traen caption propio (e.g. 4.10, 9.16); el texto dice "Figure X represents…" pero sin describir primitivos visuales. La imagen es la única fuente.
- **Inventar para mantener ordinalidad**: tentación cuando una figura falta en la fuente. Resistir. Marcar `—` y dejar nota.

## Métrica de resultado

- **4 artefactos** modificados (uno por Parte).
- **4 commits atómicos** con mensajes semánticos.
- **13/13 checks** de `kora.py velar --estricto` pasan (entre ellos `publicacion-digna` y `sello-fresco`).
- **~188 figuras** con descripción (de 188 en la enumeración completa; figs. 13.13/14/15 marcadas como no-legibles).
- Cero cambios al cuerpo korificado fuera de los blockquotes y la cláusula de figuras.

## Lección reusable para próximas koraficaciones con figuras

> Cualquier artefacto bok korificado que dependa de un `.txt` con figuras numeradas debe **mantener un mapeo por capítulo** entre la enumeración del placeholder, las líneas del `.txt` donde aparece el label, y las imágenes del directorio. No batch-procesar por figuras individuales: **procesar por capítulos completos con su rango de números** es mucho más eficiente para detectar gaps, omisiones editoriales y numeración no consecutiva.
