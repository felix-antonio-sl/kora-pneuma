
# decommission-repo-legado

## Proposito

Skill de **disciplina de retiro**. Conduce el decommission seguro de un
repositorio **legado (L)** que ya tiene **sucesor (S)**: absorbe el valor vivo de
L hacia S, canoniza la doc sesgada en el store **K**, repunta a todos los
**consumidores (C)**, elimina L sin perder lo historico, y cierra con handoff y
commits atomicos verificados.

Es la **inversa conceptual de `scaffold-repo`**: aquella nace repos, esta los
retira. No invade la semantica del campo de L ni de S — da disciplina de
transicion, no decide qué codigo es bueno.

## Abstraccion por roles

| Rol | Qué es |
|---|---|
| **L** | repo legado a eliminar |
| **S** | sucesor que ya existe y absorbe el valor de L |
| **K** | store de doc canonica (SSOT por URN; en este host, KORA) |
| **C** | consumidores que citan/dependen de L (repos, agentes, docs, configs) |

## Cuando aplicar

- El operador quiere retirar, decomisar, jubilar, «matar» o eliminar un repo o
  proyecto viejo **cuyo reemplazo ya existe**.
- Hay que consolidar un sucesor absorbiendo lo vivo del antecesor.

## Cuando NO aplicar

- **No existe sucesor**: esto no es decommission, es archivar un repo muerto sin
  herencia — no apliques absorber/canonizar; respalda y archiva.
- L sigue vivo y en produccion sin reemplazo: detente, no hay disposicion segura.
- El operador pide solo limpiar ramas o tags dentro de un repo que se queda:
  fuera de alcance.

## Principios rectores

1. **La autonomia se prueba, no se asume.** S no es autonomo hasta que compila y
   pasa tests con L **ya borrado** (o renombrado fuera de su ruta). Verificar, no
   confiar.
2. **Lo irreversible se hace reversible antes de tocar.** Backup primero: `git
   bundle --all` + `tar`, ambos verificados, fuera del arbol del repo. Nada
   destructivo ocurre antes del respaldo.
3. **Distinguir historico de documental vivo.** El **historico** (`memory/`,
   `sessions/`, auditorias fechadas, traces, logs) registra lo que paso y se
   **preserva intacto**. Solo se repunta o elimina lo **documental vivo**: un
   puntero que presenta lo muerto como fuente actual.
4. **Confirmar el punto sin retorno externo.** Borrar un remoto, un servicio o un
   DNS es decision del dueño. El agente prepara y propone; el operador confirma la
   disposicion externa irreversible.
5. **Cirugia sobre fuerza bruta.** Rutas explicitas (nunca `git add -A` en repos
   con sesiones paralelas), `Read`+`Edit` (nunca `sed -i` masivo sobre arboles con
   historicos), push **ff-only** (nunca `--force`).

## Invariante que ordena todo

**historico ≠ documental.** Una mencion en log, memoria o auditoria fechada
registra lo que paso → se preserva. Un puntero que presenta lo muerto como fuente
viva → se repunta o elimina. Toda decision de barrido y borrado se resuelve
clasificando cada match en uno de los dos lados de esta linea.

## Fases

Cada fase tiene un **gate**: no se avanza hasta cumplirlo.

### `descubrir` (read-only)

No escribe nada. Mapea el terreno.

1. **Valor de L**: qué docs/codigo/datos de L tienen valor unico que S aun no
   tiene.
2. **Consumidores (C)**: quién cita o depende de L. Buscar por todos los tokens de
   L (nombre, ruta, URN, alias).
3. **Canon (K)**: dónde vive la doc canonica que presenta a L, si la hay.
4. **Clasificar cada referencia en 4 planos**: **compilacion** (imports, build,
   deps) · **runtime** (paths, configs, servicios) · **datos** (caches, fixtures,
   dumps) · **documental** (docs, manuales, punteros).
5. **Desambiguar el ruido**: S suele contener el nombre de L (sucesion); cuidado
   con homonimos. Un match del token de L dentro de S no es necesariamente una
   referencia a L.

**Gate**: inventario escrito de valor-de-L, lista de C clasificada en 4 planos, y
ubicacion del canon. Cero escrituras hasta aqui.

### `respaldar`

1. `git bundle --all` de L → **verificar** (`git bundle verify`).
2. `tar` del arbol de trabajo de L → **verificar** (`tar tzf` lista contenido).
3. Ambos artefactos **fuera del arbol** de cualquier repo versionado (el host
   ignora `*.tar.gz`; el bundle igual va fuera).
4. **Archivar, no borrar**, binarios/derivados pesados (mover a `_archivo/` o
   destino externo).

**Gate**: bundle y tar existen y verifican. Recien aqui se permite lo destructivo.

### `absorber`

Mueve el valor vivo unico de L hacia S.

1. Copiar **verbatim** los docs de valor unico L → `S/docs/reference/` (o destino
   acordado en S).
2. Escribir un **indice de procedencia**: qué se copio, de dónde, por qué.
3. **Repuntar** dentro de S toda cita que apuntaba a L hacia las copias locales.
4. No copiar lo que S ya tiene mejor; no copiar historico (eso se preserva en L
   hasta el backup, no se migra como doc viva).

**Gate**: build de S **verde** tras absorber.

### `canonizar` (condicional)

Solo si el doc legado tiene **sesgo** (presenta L como sistema actual, idiom
viejo, supuestos muertos). Si el doc de L es neutro y reusable, basta absorber.

1. Reescribir el manual **de novo** en K, **agent-first**, **una sola fuente por
   URN** (los C **referencian** ese URN, no copian el texto).
2. Validar contra el **esquema/lint del store** (en KORA: `velar`).
3. **Verificacion adversarial contra la realidad**: contrastar el manual nuevo
   con el binario/tests/comportamiento real de S; corregir todo drift entre lo
   escrito y lo que el sistema hace.

**Gate**: canon pasa lint/`velar` del store **y** no contradice la realidad
verificada de S.

### `propagar`

Repunta a **todos** los C.

1. Cada C → S (para codigo/runtime/datos) y → canon por URN (para documental).
2. **Guardarrail duro**: **jamas** tocar historico (`memory/`, `sessions/`,
   auditorias fechadas, traces). Repuntar solo punteros vivos.
3. Si C son muchos, **fan-out por cluster** (agrupar por tipo/ubicacion y aplicar
   en lote, pero con rutas explicitas, no `add -A`).

**Gate**: ningun C vivo apunta ya a L; ningun historico fue modificado.

### `verificar-vestigios`

Barrido del arbol por todos los tokens de L.

1. `Grep` por cada token de L en cada C y en S.
2. Clasificar cada match en: **historico** (se queda) · **anotado-muerto** (texto
   que dice explicitamente «retirado/legado/eliminado» — se queda) · **vivo** (lo
   presenta como actual — debe ser 0).
3. **LEER cada match.** Contar no basta: `grep -c` no separa anotado-muerto de
   vivo. Abrir cada ocurrencia con `Read` y clasificar a mano.

**Gate**: referencias documentales **vivas = 0** (leidas, no contadas).

### `eliminar`

1. **Confirmar disposicion externa irreversible** con el operador (remoto,
   servicio, DNS, registro). Sin confirmacion, no se toca lo externo.
2. Borrar L **local** (`sudo` solo si es root-owned; preferir el minimo
   privilegio).
3. Limpiar **caches** asociados (no historial: caches de build/runtime, no
   `memory/` ni git history de los repos que se quedan).

**Gate final**: S **compila con L inexistente**. Aqui se prueba la autonomia
(principio 1).

### `documentar-commit-push`

1. **Handoff** en S/K: estado · decisiones **con fundamento** · artefactos
   (bundle/tar, dónde) · verificacion (qué se probo) · pendientes.
2. **Consolidar memoria** operativa.
3. **Commits semanticos atomicos por repo**, con **rutas explicitas**. En repos
   con sesiones paralelas, **separar tu trabajo del ajeno**: `git add <rutas>`,
   nunca `git add -A`.
4. **Verificar el `--stat` de cada commit** antes de declarar exito: cada commit
   contiene **solo tus archivos**.
5. **Push controlado ff-only** (nunca `--force`).

**Gate**: `--stat` revisado por commit; push ff-only exitoso.

## Checklist de gates

- [ ] Backup (bundle + tar) verificado **antes** de cualquier destruccion.
- [ ] Build de S **verde** con L borrado.
- [ ] Canon pasa lint/`velar` (si hubo canonizacion).
- [ ] **Cero** referencias documentales vivas — **leidas, no contadas**.
- [ ] Cada commit contiene **solo tus archivos** (`--stat` verificado).
- [ ] Push **ff-only**.

## Anti-patrones

| Anti-patron | Falla | Correccion |
|---|---|---|
| `git add -A` en repos con sesiones paralelas | Mezcla tu trabajo con el ajeno | Rutas explicitas en `git add` |
| `sed -i` sobre arboles con historicos | Corrompe memoria/auditorias que debian preservarse | `Read`+`Edit` puntero a puntero |
| `rm -rf` sin bundle | Destruccion irreversible sin respaldo | Backup verificado primero |
| Hard-delete remoto sin confirmar | Decision externa del dueño tomada sin permiso | Confirmar disposicion externa |
| «0 matches = limpio» | El historico tambien matchea; o se cuenta sin leer | Leer cada match; vivos=0, no total=0 |
| Asumir autonomia sin compilar tras borrar | S puede depender de L de forma oculta | Compilar/probar S con L inexistente |

## Composicion

| Composable con | Cuando |
|---|---|
| `urn:dev:artefacto:ship-discipline` | la fase `absorber`/`eliminar` toca codigo y conviene cerrar loop (build+test+lint) y estimar blast radius del repunte antes de actuar |

## Salida esperada

- inventario de valor-de-L y mapa de C en 4 planos,
- backup verificado (paths del bundle y tar),
- valor absorbido a S con indice de procedencia y build verde,
- canon emitido/validado si hubo sesgo (URN),
- todos los C repuntados, cero vivos (leidos),
- L eliminado, S compila con L inexistente,
- handoff + commits atomicos verificados + push ff-only.
