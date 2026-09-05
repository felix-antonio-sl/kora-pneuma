# Puente desde KODA legacy

## Absorbido

Del sistema KODA antiguo se conserva el nucleo operacional:

- `skeleton/meat/fat`: estructura y contenido sustantivo se preservan; grasa se
  elimina.
- telegrafizacion: compresion semantica, no resumen.
- deduplicacion intensiva: un hecho/concepto, un lugar.
- FS/IDC: fidelidad obligatoria y compresion contextualizada por tipo documental.
- auditoria iterativa: original vs salida hasta cerrar.
- rechazo de transformaciones formalmente validas pero semanticamente pobres.

## Descartado

No se conserva:

- formato YAML KODA como destino productivo.
- lexicon `Req`, `Def`, `Act`, `Ref` como obligacion de serializacion.
- `LLM_Parsing_Instructions` embebido.
- catalogo KODA legacy como SSOT.
- agente KODA legacy como blueprint runtime.
- familia `atomic` ni productor `atomize`.

## Traduccion conceptual

| KODA legacy | KORA vigente |
| --- | --- |
| YAML KODA | Markdown KORA/MD |
| Metadata KODA | frontmatter `_manifest` KORA |
| `Ref` interno obligatorio | headings, tablas, `relations` cuando aplica |
| Keyword markup | prosa tecnica, listas y tablas KORA/MD |
| KODA catalog | `kora index` + `docs/generated/catalog.yml` |
| Published/Review | `borrador -> publicado` via `kora promote` |
| FS/CR | `md-spec §6.11`; en operacion se reporta como IDC contextual |

## Regla de compatibilidad

Si una practica legacy mejora fidelidad, compresion o auditoria sin tensionar
KORA/MD, se puede absorber. Si introduce YAML KODA, familia retirada,
catalogo externo o runtime como fuente, se rechaza.
