---
urn: urn:kora:artefacto:entrega-kora
nombre: entrega-kora
version: 1.0.0
estado: activo
descripcion: "Prepara y verifica la entrega de un artefacto KORA ya existente hacia Codex: descubre su URN desde nombre, path o URN exacta; ejecuta gates; regenera la emisión derivada; comprueba paridad material y devuelve un recibo tipado. Usar ante llevar, entregar, preparar, comprobar o desplegar un artefacto KORA a Codex. Se detiene antes de instalar: nunca ejecuta --aplicar."
fuente: "Autorada nueva en KORA pneuma el 2026-07-20 como primer corte vertical de UX agéntica sobre los seis gestos constitucionales; no añade gesto ni campo al shape. El helper consume kora.py como autoridad y materializa el contrato entrega-kora-v1."
autor: FS
creado: 2026-07-20
lang: es
tags: [kora, entrega, codex, ux-agentica, paridad, recibo]
vector: [2, 0, 2, 0, 1]
sigma: [2, 1, 3, 2, 1]
arnes: disciplina
forma: habilidad
herramientas: [Bash]
targets: [codex]
alcance: usuario
conocimiento: [urn:kora:kb:guia-rapida-pneuma, urn:kora:kb:cat-kora-semantica-operacional, urn:kora:kb:cat-contrato-ingenieria-agentica]
---

# entrega-kora

## Propósito y frontera

Convertir una petición como «lleva `cat-thinking` a Codex» en una resolución
canónica, gates reproducibles, emisión derivada, paridad focalizada y un recibo
breve. El operador no necesita recordar la URN ni el orden de comandos.

Esta skill entrega **un artefacto ya existente y activo**. No autora, migra,
audita ni cambia lifecycle. No instala: `--aplicar` queda fuera de
`entrega-kora-v1` hasta que exista un contrato de rollback explícito.

El helper es una superficie derivada, no una nueva autoridad:

- `censo --json` descubre candidatos;
- `nombre <urn>` confirma el nombre verdadero;
- la suite verifica el núcleo antes de regenerar;
- `transmutar` regenera únicamente `_emision/`;
- `velar --estricto` valida después la fuente y el sello fresco, no la verdad
  semántica;
- `transmutar --paridad` compara emisión e instalación gestionada.

## Ejecución

1. Extraer de la petición un identificador literal: URN, `nombre` o path del
   artefacto. No convertir una descripción libre en una elección silenciosa.
2. Fijar la raíz: `${KORA_RAIZ:-$HOME/kora-pneuma}`.
3. Ejecutar:

   ```bash
   python3 "${KORA_RAIZ:-$HOME/kora-pneuma}/artefactos/skills/kora/entrega-kora/referencias/entrega.py" \
     --raiz "${KORA_RAIZ:-$HOME/kora-pneuma}" \
     --query "<identificador>" \
     --target codex
   ```

4. Interpretar el JSON emitido conforme a la tabla siguiente.
5. Comunicar primero el resultado y después evidencia, límite y próxima acción.
   No volcar el censo ni los logs verdes completos salvo petición expresa.

## Recibo `entrega-kora-v1`

| `status` | Significado | Acción |
|---|---|---|
| `knowledge-validated` | el artefacto es conocimiento; pasó gates y no se transmuta | consumir como contexto |
| `parity-faithful` | emisión e instalación Codex coinciden en la frontera gestionada | ninguna |
| `not-installed` | emisión vigente, instalación ausente | informar; no instalar |
| `partially-installed` | algunas unidades gestionadas están ausentes | informar; no instalar |
| `ambiguous` | más de un artefacto coincide exactamente | pedir elección de URN |
| `not-found` | no hay coincidencia exacta | mostrar sugerencias; no elegirlas |
| `blocked` | lifecycle, gate, emisión o paridad impiden cerrar | nombrar etapa y evidencia |
| `observation-error` | no fue posible construir un recibo válido | declarar incertidumbre |
| `unsupported-target` | el target pedido no pertenece al corte v1 | detener |

Los estados son variantes de un recibo operacional etiquetado. No amplían el
shape KORA ni constituyen por sí solos una FSM o coálgebra.

## Salida humana

Usar cuatro líneas:

```text
Resultado: <artefacto> → Codex: <status>.
Evidencia: resolución <URN>; gates <estado>; paridad <conteos o no-aplica>.
Límite: paridad material gestionada; conducta y autoridad runtime no verificadas.
Acción: <next_action>.
```

En `ambiguous` o `not-found`, sustituir evidencia por candidatos o sugerencias.
No llamar «desplegado» a `not-installed`, ni «seguro» o «equivalente» a
`parity-faithful`.

## Reglas duras

1. Nunca ejecutar `--aplicar`, `ciclo`, edición de fuentes, commit o push.
2. Nunca seleccionar una sugerencia ni resolver por semejanza. Solo una
   coincidencia exacta y única habilita `nombre`.
3. Nunca cambiar de target: esta versión cubre únicamente `codex`.
4. Nunca presentar `velar` como prueba de verdad semántica.
5. Nunca presentar paridad como preservación conductual, bisimulación, safety
   o prueba de autoridad efectiva.
6. Nunca ocultar un exit no cero. Convertirlo en `blocked` u
   `observation-error` con la etapa exacta.
7. Si el operador pide instalar, informar que la instalación requiere una
   acción exterior a esta skill y aprobación humana explícita.
8. Exigir `publicado` para conocimiento y `activo` para agentes o skills.
