---
urn: urn:kora:artefacto:entrega-kora
nombre: entrega-kora
version: 1.1.0
estado: deprecado
descripcion: "Skill deprecada: duplicaba los gestos nativos de KORA mediante gates y recibos sin aportar una frontera funcional distinta. Usa nombre, velar y transmutar directamente."
fuente: "Autorada en KORA pneuma el 2026-07-20 como corte vertical de UX agéntica. Deprecada por decisión de simplificación monooperador del 2026-08-09: el helper y su recibo duplicaban los seis gestos constitucionales."
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

# entrega-kora — deprecada

Esta skill duplicaba los gestos nativos mediante gates y un recibo operacional.
En el contexto personal monooperador, su costo excede su valor.

Usa directamente:

```bash
python3 kora.py nombre <urn>
python3 kora.py velar
python3 kora.py transmutar --urn <urn> --target <target>
python3 kora.py transmutar --paridad --urn <urn> --target <target>
```

La instalación sigue requiriendo `--aplicar` explícito.
