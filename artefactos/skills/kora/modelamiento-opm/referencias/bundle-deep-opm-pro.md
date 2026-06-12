---
_manifest:
  urn: "urn:kora:kb:bundle-deep-opm-pro"
  type: kb
  provenance:
    created_by: "FS"
    created_at: "2026-05-08"
    source: "Derivado de ~/projects/deep-opm-pro/app/src/serializacion/json.ts y app/src/modelo/tipos/* al 2026-05-08. v1.1.0 incorpora el diseno AnclaNormativa y LogDecisiones v0 documentado en el diseno adjudicado de deep-opm-pro al 2026-06-04. v1.2.0 deriva ademas de app/src/autoria/{procedencia,bundle,compilar/tipos,dsl}.ts al 2026-06-10."
    updated_at: "2026-06-10"
    update_reason: "v1.2.0 sincroniza con los cortes W5.2/W5.3/G2/E-1 de deep-opm-pro: sello de procedencia de 3 componentes dentro de modelo.procedencia (glosario retirado en G2), taxonomia de anclas extraidas inline (norma/ratificacion/candidata), variante de OPD generic-view, e import del campo .json del ResultadoBundle cuando el bundle proviene del compilador. v1.3.0 absorbe W6.5 y M2: extension aditiva NotaMesa (meta de la mesa, V-204), LogDecisiones v0 con modeloHash=protoHash del sello y export bloqueado sin sello (transiciones registradas por la app sin retroceso; L9), y el camino compilador como protocolo primario de emision (compilarProto + construirSello + emitirBundle)."
version: "1.3.0"
status: activo
nombre: bundle-deep-opm-pro
descripcion: "Contrato del bundle JSON 'deep-opm-pro.modelo.v0' que la skill modelamiento-opm emite para que el modelador deep-opm-pro lo importe. Incluye extensiones meta opcionales AnclaNormativa y LogDecisiones v0 para el ciclo re-elicitar."
tags: [opm, deep-opm-pro, contrato, json, importable, ancla-normativa, log-decisiones, re-elicitar]
lang: es
---

# Bundle deep-opm-pro — contrato de import

Documento JSON canonico que la skill `modelamiento-opm` emite cuando el destino es **edicion / refinamiento / revision** en el modelador `~/projects/deep-opm-pro/app/`.

> **SSOT del shape JSON**: el codigo del modelador. **SSOT semantica de la skill**:
> corpus OPM/Forja SSOT ES. Si esta referencia tensiona con
> `app/src/serializacion/json.ts` o `app/src/modelo/tipos/*` sobre campos, manda
> el codigo; si el codigo tensiona con validez OPM, manda el corpus Forja y se
> corrige la herramienta.

## 1. Forma raiz

```json
{
  "formato": "deep-opm-pro.modelo.v0",
  "modelo": { /* Modelo */ },
  "carpetaId": "..."
}
```

- `formato`: literal exacto `"deep-opm-pro.modelo.v0"`. El detector de la app rechaza cualquier otro valor.
- `modelo`: objeto `Modelo` (ver §4).
- `carpetaId`: opcional, `string | null`. Solo lo usa el workspace local de la app; la skill puede omitirlo.

## 2. Reglas globales de emision

1. Identidades (`id`, `opdId`, `entidadId`, etc.) son strings cualquiera, no necesariamente UUIDs. Deben ser **internamente consistentes**: toda referencia debe resolver dentro del mismo modelo.
2. `nextSeq` de `Modelo` es un contador interno; emitir `0` o el numero de cosas + 1.
3. Toda apariencia visual (`Apariencia`, `AparienciaEnlace`) es opcional en sus campos no requeridos: si no hay certeza, **omitir**, no inventar. La app normaliza al hidratar.
4. Nombres de cosas son humanos y deben coincidir con los emitidos en OPL-ES y en el OPD.
5. No referenciar OPDs huerfanos: el OPD raiz es `opdRaizId` y todo OPD declarado debe ser alcanzable desde el (via `padreId`).
6. `validarReferenciasOpd` se aplica al hidratar: si una entidad referencia un OPD inexistente o un estado pertenece a una entidad ausente, el import falla con error legible.

## 3. Extensiones meta opcionales

Estas extensiones **no son OPM nuclear**. Viven como metadata declarada del
autor o de la mesa, bajo `R-DOC-7`/`V-204`/`R-BR-4`: no crean objeto, proceso,
estado ni enlace, y no emiten OPL nuclear.

### 3.0 Sello de procedencia (`modelo.procedencia`)

Desde W5.3 (y reducido a 3 componentes en G2, que retiro el glosario del
pipeline), el bundle emitido por el **compilador de autoria** porta un sello
que viaja **dentro** del modelo serializado:

```ts
interface SelloProcedencia {
  protoHash: string;       // hash del proto fuente
  autoriaVersion: string;  // version de la libreria de autoria
  layoutVersion: string;   // version del layout determinista
}
// Modelo.procedencia?: SelloProcedencia
```

Reglas:

- **Solo el compilador emite sellos** (`emitirBundle` con `opciones.procedencia`).
  La skill jamas fabrica, copia ni simula un sello: un bundle artesanal se
  emite sin `procedencia` y opforja lo declara «sin sello».
- El deserializador es tolerante a bundles viejos con `glosarioHash` (campo
  huerfano descartado); la skill no emite ese campo.
- El sello habilita el panel de procedencia (W6.6), el golden-harness H2
  (`verify:reproducible` nombra el componente divergente) y el cruce skill→app
  del contador g3.

### 3.1 `AnclaNormativa`

`AnclaNormativa` es la extension aditiva que porta procedencia normativa o
pendientes de ratificacion. Su molde sigue el patron de
`SatisfaccionRequisito.target`, extendido a entidad, enlace, OPD o modelo:

```ts
type TargetAncla =
  | { tipo: "entidad"; id: Id }
  | { tipo: "enlace"; id: Id }
  | { tipo: "opd"; id: Id }
  | { tipo: "modelo" };

interface AnclaNormativa {
  id: Id;
  claveProto?: string;
  target: TargetAncla;
  estado: "vigente" | "pendiente-ratificacion";
  referencias?: { norma: string; articulos?: string[]; seccion?: string }[];
  nota?: string;
  ratificacion?: {
    nivelAutoridad: "operador-modelado" | "mesa" | "dt-seremi-legal";
    estadoRatificacion: "pendiente" | "anotado-en-mesa" | "ratificado-con-fuente";
    fuente?: string;
    responsable?: string;
    anotadoEn?: string;
    ratificadoEn?: string;
  };
}
```

Reglas:

- `claveProto` es la clave estable nacida en el proto; no depende de ids
  posicionales del bundle.
- `estado: "pendiente-ratificacion"` representa `[RATIFICAR]`; no existe un
  tipo hermano `DecisionPendiente`.
- **Extraccion inline del proto (W5.2)**: el compilador extrae anclas de las
  lineas de hecho en tres clases, y solo tres — `norma` (cita explicita →
  compila `vigente`), `ratificacion` (`[RATIFICAR[ #clave][: texto]]` →
  compila `pendiente-ratificacion`; clave derivada `ratificar:<target>` si no
  hay `#clave`) y `candidata` (`[C1]`/`[Q14]`-style → **jamas compila**, se
  conserva como anotacion). Un `[RATIFICAR]` tras una oracion estricta no la
  degrada: el hecho compila y el pendiente queda como ancla.
- `target.tipo == "enlace"` es valido y necesario para anclas de frontera.
- un bundle sin `anclasNormativas` debe conservar compatibilidad con bundles
  previos.
- las anclas se exhiben como capa meta rotulada, nunca como frase OPL nuclear.

### 3.2 `LogDecisiones v0`

La mesa puede exportar un log para que `modelamiento-opm` lo consuma en estado
`re-elicitar`.

```ts
interface EntradaLogDecision {
  claveAncla: string;
  transicion: {
    de: "pendiente" | "anotado-en-mesa" | "ratificado-con-fuente";
    a: "pendiente" | "anotado-en-mesa" | "ratificado-con-fuente";
  };
  nivelAutoridad: "operador-modelado" | "mesa" | "dt-seremi-legal";
  fuente?: string;
  responsable?: string;
  fecha: string;
  modeloHash: string;
}

interface LogDecisiones {
  schema: "deep-opm-pro.log-decisiones.v0";
  emitidoEn: string;
  modeloHash: string;
  entradas: EntradaLogDecision[];
}
```

Contrato de consumo:

- `anotado-en-mesa` registra una marca de la app; **no muta** el proto/bundle.
- `ratificado-con-fuente` exige `fuente`; si falta, la skill bloquea esa
  entrada.
- solo `ratificado-con-fuente` con `fuente` presente puede mover un ancla a
  `vigente`.
- el match se hace por `claveAncla`/`claveProto`, nunca por ids posicionales.
- `modeloHash` divergente se reporta como staleness y bloquea mutacion hasta
  aclaracion.
- **`modeloHash` = `protoHash` del sello** (W6.5-b): la app bloquea ruidoso el
  export del log sobre modelos sin sello, asi que todo log valido es trazable
  al proto. Verificar recalculando `construirSello({protoTexto})`.
- la app registra transiciones **sin retroceso**
  (`pendiente → anotado-en-mesa → ratificado-con-fuente`) en
  `ancla.ratificacion`; son registro, no mutacion del ancla OPM. El paso a
  `vigente` ocurre solo en la re-emision de la skill.
- **L9**: tras la re-emision con anclas `vigente`, el registro de la app se
  limpia solo — un ancla vigente no reaparece ni en pendientes ni en el log.

Errores especificos de re-elicitacion:

| Error | Causa | Fix en la skill |
|-------|-------|-----------------|
| `schema` invalido | el log no es `deep-opm-pro.log-decisiones.v0` | rechazar log y pedir version correcta |
| `modeloHash` stale | el log proviene de otra version del modelo | no mutar; pedir proto/bundle correspondiente o ratificar staleness |
| `fuente` ausente | transicion a `ratificado-con-fuente` sin fuente | bloquear entrada; pedir fuente |
| `claveAncla` desconocida | no existe ancla matching en la fuente | bloquear y preguntar si se acuna, corrige o descarta |
| matches duplicados | dos anclas comparten clave estable | bloquear hasta desambiguar |
| transicion invalida | cambio no contemplado por el ciclo | registrar deuda; no mutar |

### 3.3 `NotaMesa` (W6.5-a)

Comentario de revision de la mesa anclado a un componente. Extension **aditiva**
del `modelo.v0` con el mismo estatuto meta que las anclas (V-204): no emite OPL,
no cuenta como cosa, no altera `validarModelo`.

```ts
interface NotaMesa {
  id: Id;
  target: TargetAncla;  // entidad | enlace | opd | modelo
  texto: string;        // que se PREGUNTA la mesa (no que ES la cosa)
  fecha: string;
}
```

Reglas:

- La `descripcion` de una entidad dice que **es**; la nota registra que se
  **pregunta** la mesa. Son categorias distintas — no fusionar.
- Las notas viajan en el contexto W6.0 (seccion «Notas de la mesa», target
  resuelto por nombre) como **insumo de re-elicitacion**: se resuelven
  corrigiendo el proto y son desechables (no se fosilizan).
- La skill no emite notas en sus bundles: las notas nacen en la mesa (UI
  Inspector de opforja).

## 4. Tipo `Modelo`

```ts
interface Modelo {
  id: string;
  nombre: string;
  descripcion?: string;
  opdRaizId: string;
  opds: Record<Id, Opd>;
  entidades: Record<Id, Entidad>;
  estados: Record<Id, Estado>;
  enlaces: Record<Id, Enlace>;
  abanicos?: Record<Id, Abanico>;
  archivado?: boolean;
  archivadoEn?: string;
  versiones?: VersionResumen[];
  crearVersionAlGuardar?: boolean;
  procedencia?: SelloProcedencia;
  nextSeq: number;
}
```

`procedencia` solo aparece en bundles emitidos por el compilador de autoria
(ver §3.0); la skill no lo emite en bundles artesanales.

## 5. Subtipos relevantes

### 5.1 Entidad

- `tipo: "objeto" | "proceso"`
- `esencia?: "informacional" | "fisica"` (default `"informacional"`)
- `afiliacion?: "sistemica" | "ambiental"` (default `"sistemica"`)
- `refinamientos?: { descomposicion?: { opdId, ... }, despliegue?: { opdId, modo? } }` — slots por tipo de refinamiento.
- Metadata extendida (`alias`, `unidad`, `descripcion`, `urls[]`, `valor`) opcional.

### 5.2 Estado

- `entidadId` obligatorio; debe apuntar a una `Entidad` tipo `"objeto"`.
- `nombre` humano, equivalente al usado en OPL-ES.
- `designaciones?: ("inicial" | "final" | "default" | "current")[]` — la app aplica exclusiones de `reglas-opm-estrictas-es` y su politica runtime/canon.
- `duracion?: { unidad, min, nominal, max }` — solo si la SSOT lo justifica.

### 5.3 Enlace

- `tipo` ∈ {`agregacion`, `exhibicion`, `generalizacion`, `clasificacion`, `agente`, `instrumento`, `consumo`, `resultado`, `efecto`, `invocacion`}
- `extremoOrigen`, `extremoDestino`: `{ kind: "entidad" | "estado", id }`. Los estructurales solo permiten `entidad-entidad`; los procedurales pueden involucrar estados segun la SSOT.
- `modificador?`, `subtipoModificador?` — opcionales; relevantes solo en procedurales.
- `multiplicidadOrigen?`, `multiplicidadDestino?` — strings cortos (e.g. `"1..n"`).
- `derivacion?`: marcado de enlaces externos derivados de refinamiento; emitir solo si el caso lo amerita.
- `estilo?: { color?, strokeWidth?, dashArray? }` — usar `tokens` del modelador, no inventar; preferible omitir.

### 5.4 OPD

- `padreId: Id | null` — `null` solo para el OPD raiz.
- `vista?: { kind: "generic-view"; readOnly?: boolean }` (E-1) — marca el OPD
  como **vista ad-hoc sin semantica de refinamiento**: reune apariciones
  existentes para navegar/explicar, no emite OPL (delta-cero) y queda exenta de
  los checkers de frontera/descomposicion. `readOnly: true` la vuelve solo
  lectura en la app. DSL del compilador: `vistaGenerica(opdKey, {readOnly?})`;
  para multi-edges por transicion dentro de la vista usar
  `aparecerEnlacePorId(opdKey, enlaceId)` (F1) o
  `aparecerEnlacePorTransicion(...)` (H5).
- `apariencias: Record<Id, Apariencia>` — un slot por entidad visible en este OPD (posicion + tamaño + estilo opcional).
- `enlaces: Record<Id, AparienciaEnlace>` — un slot por enlace visible (vertices, etiqueta, ruta).
- `ordenLocal?: number` — orden entre OPDs hermanos del mismo padre.

### 5.5 Apariencia y AparienciaEnlace

- `posicion: { x, y }` cuando se conoce; si no, **omitir** y dejar que el auto-layout de la app la asigne en `fit-to-view`.
- `tamaño: { ancho, alto }` opcional; el modelador usa 135x60 canonico cuando falta.
- `vertices`, `rutaEtiqueta`, `ordenPartes`, `modoPlegado`: especialistas — emitir solo cuando ya se exporto desde la propia app o se conoce con certeza.

### 5.6 Abanico

- Emitir solo si hay un `O`/`XOR` real entre enlaces que comparten puerto en una entidad de un OPD.
- `enlaceIds` debe listar enlaces ya declarados en `enlaces` y presentes en el OPD.

## 6. Errores comunes al importar

| Error | Causa | Fix en emision |
|--------|--------|-----------------|
| "JSON invalido" | parseo falla | revisar serializacion; usar `JSON.stringify(doc, null, 2)` |
| "formato no soportado" | `formato` distinto al literal | emitir exactamente `"deep-opm-pro.modelo.v0"` |
| "OPD raiz no existe" | `opdRaizId` no esta en `opds` | declarar el OPD raiz con `padreId: null` |
| "entidad referencia OPD inexistente" | refinamiento apunta a OPD no declarado | declarar el OPD destino antes de cerrar el bundle |
| "estado de entidad inexistente" | `entidadId` del estado roto | revisar consistencia |
| "extremo de enlace invalido" | `kind` o `id` incorrecto | re-validar con `validarFirmaEnlace` mental antes de emitir |
| "referencias OPD ciclicas" | refinement tree con ciclo | aplicar `reglas-opm-estrictas-es` y `spec-forja-opd-es` (con V-* base delegadas) |

## 7. Protocolo de uso desde la skill

**Camino primario (M2): proto → compilador.** Con deep-opm-pro disponible, no
construir el JSON a mano: escribir el proto OPL-ES estricto y emitir via
`compilarProto` + `construirSello` + `emitirBundle` (script bun desde
`~/projects/deep-opm-pro/app/`; snippet en SKILL.md §serializar-bundle). El
campo `bundle.json` del `ResultadoBundle` ES el documento importable
`{formato, modelo}` con `modelo.procedencia` sellada; `bundle.opl`,
`bundle.reporte`, `bundle.avisos` y `bundle.conteos` acompañan el entregable.

**Camino fallback (sin deep-opm-pro):**

1. Construir el `Modelo` en memoria respetando los tipos.
2. Aplicar `validar-modelo` antes de serializar; corregir bloqueos estructurales.
3. Serializar con `JSON.stringify(doc, null, 2)` (la app espera 2-space indentation por convencion, pero acepta cualquier whitespace valido).
4. Adjuntar el bundle al entregable y dar al usuario el camino de import: `cd ~/projects/deep-opm-pro/app && bun run dev` → UI → `Modelo / Importar JSON` → pegar.
5. Si la sesion ya tiene la app abierta y el bundle es chico, basta con copiar al portapapeles.
6. Si la mesa entrega `LogDecisiones v0`, ejecutar `re-elicitar` antes de emitir
   un nuevo bundle. Un log sin consumidor operativo queda prohibido por la regla
   anti-esterilidad de `deep-opm-pro`.
7. Si el bundle proviene del **compilador de autoria** (`emitirBundle`), lo que
   se pega en el import es el campo `.json` del `ResultadoBundle` (el documento
   `{formato, modelo}` ya serializado), no el objeto resultado completo.
8. Si el flujo exige byte-identidad con un golden versionado, verificar con
   `bun run verify:reproducible --proto <md>|--modelo <json> --golden <bundle.json>`
   (H2; exit 0 = identico, 1 = difiere con diagnostico, 2 = uso invalido).

## 8. Cuando NO emitir bundle

- El destino es un documento estatico (markdown, PDF, lamina): preferir `serializar-opd` via jointjs-open-source.
- El usuario solo pide OPL-ES: emitir solo la serializacion textual.
- El modelo es solo conceptual y no se va a editar: documentar OPL + descripcion textual del OPD.

## 9. Ejemplo minimo

```json
{
  "formato": "deep-opm-pro.modelo.v0",
  "modelo": {
    "id": "modelo-cafetera",
    "nombre": "Cafetera domestica",
    "opdRaizId": "opd-sd",
    "opds": {
      "opd-sd": {
        "id": "opd-sd",
        "nombre": "SD",
        "padreId": null,
        "apariencias": {
          "ap-cafe-grano": { "entidadId": "ent-cafe-grano" },
          "ap-cafe-bebida": { "entidadId": "ent-cafe-bebida" },
          "ap-preparar": { "entidadId": "ent-preparar" }
        },
        "enlaces": {
          "ap-l1": { "enlaceId": "l1" },
          "ap-l2": { "enlaceId": "l2" }
        }
      }
    },
    "entidades": {
      "ent-cafe-grano": { "id": "ent-cafe-grano", "nombre": "Cafe en grano", "tipo": "objeto", "esencia": "fisica" },
      "ent-cafe-bebida": { "id": "ent-cafe-bebida", "nombre": "Cafe bebida", "tipo": "objeto", "esencia": "fisica" },
      "ent-preparar": { "id": "ent-preparar", "nombre": "Preparar", "tipo": "proceso" }
    },
    "estados": {},
    "enlaces": {
      "l1": { "id": "l1", "tipo": "consumo", "extremoOrigen": { "kind": "entidad", "id": "ent-cafe-grano" }, "extremoDestino": { "kind": "entidad", "id": "ent-preparar" } },
      "l2": { "id": "l2", "tipo": "resultado", "extremoOrigen": { "kind": "entidad", "id": "ent-preparar" }, "extremoDestino": { "kind": "entidad", "id": "ent-cafe-bebida" } }
    },
    "nextSeq": 4
  }
}
```

Este bundle es importable directo por el modelador y se renderiza con auto-layout sin necesidad de declarar posiciones.
