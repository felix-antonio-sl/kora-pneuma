# Protocolo De Mejora De Specs

Usar este protocolo cuando el diagnostico indique que la norma, y no solo un
artefacto, necesita cambiar.

## 1. Causa Raiz

Clasificar el problema antes de editar:

| Tipo | Senal | Accion |
|------|-------|--------|
| Artefacto invalido | la spec es clara y el archivo no cumple | corregir artefacto |
| Check desalineado | la spec dice una cosa y el check valida otra | corregir toolchain y test |
| Spec incompleta | no hay regla propietaria suficiente | ampliar spec propietaria |
| Contradiccion entre capas | dos reglas tensionan | aplicar precedencia y corregir capa inferior |
| Derivado obsoleto | `docs/generated/*` o `_BUILD/` difiere | regenerar, no editar a mano |

## 2. Diseno Del Cambio

- Elegir la capa propietaria mas alta necesaria y mas baja suficiente.
- Mantener el cambio pequeno: una regla, un enum, una matriz o un check por
  vez cuando sea posible.
- Si una regla cambia behavior ejecutable, actualizar toolchain y tests.
- Si una regla crea excepcion, declarar condicion, propietario y enforcement.
- Si la mejora afecta runtime, declarar fidelidad y perdida segun
  `transmutation-spec`.

## 3. Edicion

- Specs: conservar frontmatter KORA/MD, `relations`, version y secciones de
  validacion.
- Artefactos agenticos: conservar `autoria-spec` y `artefacto:*`.
- Knowledge: conservar URNs resolubles y relations.
- Toolchain: preferir checks deterministas y mensajes con `fix_hint`.

## 4. Verificacion

Ejecutar segun alcance:

```bash
python3 toolchain/kora check --strict --path <subtree>
python3 toolchain/kora lint-md <subtree>
```

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict
python3 -m unittest discover -s tests
python3 toolchain/kora kb-graph --json --orphans
```

Los dos primeros comandos son la puerta local para artefactos en staging. Los
demas son gates de repositorio o de knowledge graph. No todos aplican siempre:
si alguno no se ejecuta, declarar por que no era necesario o que bloqueo lo
impidio. Si `lint-md` global falla por deuda ajena al subtree, reportarlo como
deuda preexistente y no mezclarlo con el cierre del artefacto bajo prueba.

## 5. Cierre

El cierre debe decir:

- que regla o artefacto cambio.
- que invariantes se preservaron.
- que gates pasaron.
- que deuda queda abierta, si existe.
