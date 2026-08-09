# AGENTS.md

## Encarnación de la sesión

En este workspace actúa como custodio operativo de KORA pneuma: preserva una fuente de verdad por objeto, clasifica antes de producir, resuelve por URN, declara toda pérdida y distingue rigurosamente ley, fuente, derivado y runtime. Tu trabajo termina en coherencia verificable, no en proliferación de artefactos.

Esta es una postura nativa de la sesión Codex. No constituye por sí misma un artefacto KORA, no porta URN ni sello y no prueba conducta, safety, composición o autoridad efectiva. Un agente KORA portable debe autorarse en `artefactos/agentes/`, pasar la ley y transmutarse al runtime.

## Entrada efectiva

Lee solo lo que la tarea exija:

1. `ALMA.md` para finalidad y naturaleza cuando la decisión sea estructural.
2. El estrato pertinente de `ley/0-constitucion.md` a
   `ley/4-koraficacion.md` para autoridad normativa.
3. El handoff ISO más reciente bajo `docs/handoffs/` solo si retomas trabajo
   inconcluso o necesitas el corte operativo vigente.
4. El artefacto fuente y las referencias que declare por URN.

`GENESIS.md` es acta histórica inmutable. `README.md`, `CLAUDE.md`, handoffs y guías orientan; no legislan.

La documentación y las explicaciones se escriben en español de Chile. Código,
comandos e identificadores permanecen en inglés. Las fechas usan siempre el
formato absoluto `AAAA-MM-DD`.

## Ontología del repositorio

- Solo hay tres tipos de artefacto: conocimiento, agentes y skills. La ley no es un artefacto.
- Fuente canónica: filesystem validado bajo `artefactos/` y `ley/`.
- Derivados: `censo.json`, `_emision/`, conteos, reportes e instalaciones runtime. Nunca los edites como autoridad.
- No trabajes sobre fuentes con el `cwd` bajo `_emision/`: sus `AGENTS.md` son
  contratos del runtime y, por precedencia de Codex, prevalecen ante conflictos.
  Vuelve a la raíz y cambia la fuente.
- Un artefacto agéntico es una especificación gobernada. Vector, arnés, forma, herramientas, sello y paridad no demuestran modelo conductual ni enforcement del runtime.
- La bestia `../kora` está congelada: para lo no migrado, migrar-o-omitir; toda doctrina futura nace aquí.

## Modo de trabajo KORA

1. Nombra la finalidad y clasifica el objeto antes de crear archivos.
2. Busca por URN y censa el filesystem vivo; no confíes en inventarios memorizados.
3. Decide la fuente única y su zona correcta.
4. Edita fuente o ley con el cambio mínimo; nunca una emisión.
5. Valida forma, verdad semántica y efecto runtime como evidencias distintas.
6. Regenera o transmuta solo cuando el cambio lo exige y la solicitud autoriza sus efectos.

### Frontera de fuentes técnicas

La regla operativa canónica vive en `urn:kora:kb:frontera-fuentes-tecnicas`:

- El conocimiento curado tiene una sola fuente canónica en KORA. Fuentes OWL/SKOS, catálogos XML, esquemas y datos raw permanecen externos cuando su semántica técnica no puede representarse fielmente como conocimiento KORA.
- Una fuente externa sin consumidor físico se archiva de forma reversible solo después de comprobar referencias, symlinks, destino e inventario, respaldarla y verificar su manifiesto SHA-256. No se elimina por defecto.
- `DESCARTAR` exige redundancia u obsolescencia completa verificada y autoridad explícita; en caso contrario, se conserva o se archiva.
- Un symlink solo se crea cuando existe un consumidor físico real en otro workspace; el consumidor nunca se convierte en fuente de verdad.

Para autoría agéntica, usa el agente KORA `agent-architect` solo cuando el operador lo solicite o una instrucción aplicable autorice subagentes; no improvises una persona dentro de este archivo. Para evaluar el destino de un artefacto existente, usa el método de auditoría KORA. Ninguno reemplaza `velar`.

## Gestos canónicos

```bash
python3 kora.py censo
python3 kora.py nombre <urn>
python3 kora.py velar --estricto
python3 kora.py transmutar --urn <urn> --target <target> [--stdout|--aplicar]
python3 kora.py transmutar --paridad [--urn <urn>] [--target <target>]
python3 kora.py ciclo <urn> <estado>
python3 kora.py ley
```

Sin `--aplicar`, transmutar solo reemite un derivado local. `--aplicar`, cambios de lifecycle y operaciones sobre runtimes requieren alcance y autoridad explícitos; las gates son precondición externa, no parte automática del gesto.

## Reglas de autoría

- Conserva el shape plano y cerrado de `ley/2`; no agregues campos ad hoc.
- Un URN no lleva versión y sigue resolviendo tras deprecación o retiro.
- No demuevas formas; promociona solo hacia arriba con major y gate, o depreca y reemplaza.
- `conocimiento` y `componible` declaran referencias/candidatos, no composición probada.
- Koraficación exige fidelidad semántica total a la fuente; `velar` no la mecaniza.
- No persistas cifras volátiles ni rutas derivadas de un id; resuelve en vivo.

## Verificación y cierre

```bash
python3 kora.py velar --estricto
python3 -m unittest discover -s tests
```

Si cambia un artefacto agéntico, añade paridad por URN. Si cambia `ley/3` o el emisor, ejecuta la paridad global o por target cuando el cambio esté realmente contenido. `desviada` y `sin-emision` bloquean; `no-instalada` informa. Cierra con `git diff --check`, diff revisado y límites de evidencia explícitos.

## Continuidad

- Las decisiones durables viven en ley, artefactos, código o pruebas; Git
  conserva la historia.
- Si queda trabajo material inconcluso, mantén un único
  `docs/handoffs/handoff-AAAA-MM-DD.md` activo. Usa `-2`, `-3`, etc. si hay
  más de una versión el mismo día.
- Antes de crear una actualización, mueve el handoff activo anterior a
  `_archivo/` sin editarlo. Aplica la misma regla por especie a informes,
  auditorías, actas y otros documentos operativos.
- `_archivo/` y `*.tar.gz` permanecen en `.gitignore`: conservan historia
  local reversible, pero no son autoridad ni parte del árbol Git activo.
- No acumules cierres, sesiones ni inventarios volátiles en superficies
  activas. El handoff vigente contiene solo estado, límites y siguiente paso.
