
# auditoria-exposicion-kora

## Finalidad y frontera

Determinar si un objeto KORA llega hasta sus beneficiarios sin confundir siete
afirmaciones diferentes:

| Plano | Pregunta que sí responde | Lo que no demuestra |
|---|---|---|
| fuente | ¿existe una fuente canónica? | forma válida o vigencia |
| censo | ¿el URN resuelve de manera única? | que alguien lo use |
| índice | ¿el cuerpo expone textualmente el URN? | inclusión semántica ni exhaustividad |
| alcance | ¿la mención incluye, excluye o contextualiza? | cableado de consumidores |
| consumidor | ¿una fuente declara `conocimiento` o `cita`? | carga efectiva en runtime |
| emisión/instalación | ¿la frontera KORA es materialmente fiel? | interpretación o conducta |
| runtime | ¿discovery o un canario observaron el objeto? | universalidad ni adopción humana |

La auditoría es read-only. No korafica contenido, no decide el destino de una
skill o agente —para eso existe `auditoria-artefactos-kora`— y no repara ni
despliega salvo que el operador amplíe expresamente el encargo. Una arista
documental, una igualdad de bytes y una ejecución son testigos distintos; no
se promueven entre sí.

## 1. Encuadrar el claim

Fijar antes de contar:

- índice o artefacto exacto, resuelto por URN o path;
- familia o prefijos realmente en alcance;
- si el objeto afirma ser exhaustivo o solo curado;
- consumidores y beneficiario esperado;
- target y nivel `usuario|proyecto`, solo si se pidió verificar despliegue.

No inventar un prefijo a partir del nombre. No tratar todo el censo como
contenido que un índice especializado deba listar. Una exclusión explícita es
parte del alcance, no una inclusión semántica.

## 2. Resolver URNs y exposición textual

Usar el script empaquetado desde el directorio efectivo de esta skill:

```text
python3 <skill-dir>/scripts/verify-index-urns.py <artefacto.md> \
  --root <raiz-kora> \
  [--prefix urn:<ns>:kb:<familia>-]... \
  [--require-complete]
```

El script invoca `kora.py censo --json`; nunca extrae URNs desde el formato
humano ni desde `censo.json` persistido. Separa frontmatter y cuerpo sin usar
`split('---')`, excluye el URN identitario del artefacto y reporta:

- `RESOLUCION PASS|FAIL`: toda referencia KB válida del frontmatter o cuerpo
  resuelve una sola vez en el censo vivo; una declaración duplicada es
  `AMBIGUA` y un token que comienza con `urn:` pero no satisface la gramática
  es `URN_INVALIDA`, nunca una coincidencia truncada;
- `DUPLICADOS INFO`: repeticiones en el cuerpo, siempre informativas hasta leer
  su función;
- `COBERTURA_TEXTUAL PASS|GAP|FAIL|ABSENT`: artefactos de conocimiento
  `publicado` bajo cada prefijo que aparecen en el cuerpo; un prefijo sin
  corpus publicado es `ABSENT`, nunca un éxito vacío;
- `SOLO_FRONTMATTER`: relación declarada que no está expuesta en el cuerpo.

`GAP` no cambia el exit code. Usar `--require-complete` únicamente cuando el
predicado esté cerrado: todas las fuentes `publicado` cuyo URN coincide con
cada prefijo explícito deben aparecer en el cuerpo, y la fuente o el operador
afirmaron esa exhaustividad. Un título amplio no basta. El script no decide
cobertura semántica: una URN puede aparecer para ser excluida, como contraste
o como destino de una partición.

## 3. Interpretar alcance y duplicados

Leer el contexto de cada omisión, repetición y mención relevante. Clasificar:

- **incluida**: el índice la ofrece dentro de su alcance;
- **excluida explícitamente**: la nombra para fijar frontera;
- **contextual**: antecedente, shard, reemplazo o contraste;
- **ambigua**: el texto no permite decidir.

Una repetición no es un URN duplicado. Confirmar unicidad declarativa contra el
censo; después decidir si repetir mejora navegación o es ruido. Reportar
separadamente cobertura textual y juicio semántico.

## 4. Trazar consumidores sin inflar el conteo

Buscar la URN propia del índice o artefacto en las fuentes activas pertinentes,
excluyendo la fuente inspeccionada y derivados:

```text
rg -n --fixed-strings '<urn>' \
  --glob '!<ruta-fuente-relativa>' \
  artefactos/agentes artefactos/skills artefactos/conocimiento
```

Clasificar cada aparición:

1. `conocimiento`: cableado declarado de un agente o skill;
2. `cita`: relación documental, no consumo operacional;
3. cuerpo o descripción: navegación, explicación o historia;
4. `_emision/`, runtimes y archivos: derivados o evidencia de otro plano.

Contar consumidores solo en la clase que el claim requiere. `conocimiento` no
prueba auto-carga, lectura ni conducta: declara el conocimiento permitido por
la fuente. Una mención corporal tampoco se eleva a wiring. Si falta cableado,
identificar primero el consumidor real; no añadir la URN a todos los agentes.

## 5. Verificar emisión y runtime solo cuando corresponda

Para una fuente agéntica consumidora, la comprobación material focal es:

```text
python3 kora.py transmutar --paridad --urn <urn-consumidor> --target <target>
```

Agregar `--proyecto <path>` cuando el alcance lo exija. Interpretar
`no-instalada` como información y `fiel` como igualdad de la frontera
gestionada. Discovery, carga de contexto y conducta requieren observaciones o
canarios separados del runtime; si no se ejecutan, registrar `NOT_RUN`.

No aplicar, instalar ni corregir durante una auditoría read-only. Si el encargo
autoriza remediación, cambiar primero la fuente única y transmutar únicamente
los targets y niveles autorizados.

## 6. Remediación mínima por tipo de brecha

| Brecha demostrada | Fuente que se corrige |
|---|---|
| URN corporal no resuelve | índice o fuente retirada/reemplazante, según autoridad |
| falta textual contra un claim exhaustivo | cuerpo del índice existente |
| alcance ambiguo | texto que incluye, excluye o contextualiza la entrada |
| consumidor real no declara conocimiento necesario | fuente de ese consumidor, con bump e historia |
| emisión rancia | re-transmutar la fuente vigente |
| instalación desviada atribuible | reaplicar solo bajo autoridad explícita |

No crear otro índice, KB, dashboard, informe persistente ni gate para tapar una
brecha de exposición que se resuelve editando la fuente gobernante. No cambiar
consumidores por mera coincidencia nominal.

## Cierre

Entregar una tabla breve:

```text
Plano | Estado PASS|FAIL|ABSENT|NOT_RUN | Evidencia | Límite
```

`GAP` e `INFO` son diagnósticos del script, no estados finales de un plano. Un
`GAP` es `FAIL` solo contra el claim exhaustivo ya fijado; sin ese claim informa
la medición y deja explícito que la completitud semántica no fue demostrada.

Después listar solo brechas demostradas, remediación mínima y decisiones
humanas reales. Cerrar cuando resolución, alcance, wiring y el nivel runtime
solicitado estén distinguidos y suficientemente evidenciados; no ampliar la
auditoría por hallazgos circunstanciales.
