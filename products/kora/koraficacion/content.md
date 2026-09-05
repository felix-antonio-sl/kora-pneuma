# Koraficación

Transforma una o varias fuentes en conocimiento que ayude a comprender o actuar.
Parte del uso esperado y de la fuente completa dentro de ese alcance. La salida
debe poder leerse, comprobarse, recuperarse y actualizarse sin depender de la
memoria de quien la escribió.

## Leer y componer

Identifica procedencia, fecha o versión pertinente y alcance de cada fuente.
Conserva los originales recuperables. Consulta fuentes oficiales vigentes cuando
el conocimiento técnico, normativo o de producto pueda haber cambiado; distingue
lo documentado de la capacidad instalada o de la práctica observada.

Extrae afirmaciones y relaciones que cambian el uso del conocimiento. Conserva
condiciones, unidades, excepciones, límites, incertidumbres y discrepancias.
Separa hechos de la fuente, interpretación y propuestas propias. Un dato ausente
queda desconocido; no se convierte en cero, falso ni una conclusión negativa.
Si dos fuentes discrepan, muestra el desacuerdo y su alcance antes de decidir
si hay evidencia suficiente para resolverlo.

Escribe el cuerpo con el detalle que requiere su consumidor. Incluye referencias
localizables cerca de afirmaciones materiales. La compresión se detiene cuando
elimina una condición relevante o vuelve imposible reconstruir el fundamento.
Un esquema, dataset, imagen, binario o script conserva su formato cuando
convertirlo en prosa destruiría su función; el cuerpo explica cómo usarlo.

Antes de crear un objeto, busca por su identidad y por términos distintivos en
los productos existentes. Si el conocimiento ya está representado, decide si
corresponde ampliarlo o relacionarlo. Cuando la entrada sea texto recibido en
la conversación, conserva una copia literal del texto disponible y registra
su origen y alcance; no afirmes haber recuperado un archivo original ausente.
Si conoces un archivo candidato pertinente, contrástalo con la entrada antes
de tratarlo como la misma fuente.

Cuando la literalidad sea relevante —por ejemplo, negaciones, cifras, unidades
o campos de una plantilla— prepara una lista efímera de fragmentos decisivos.
Contrasta cada fragmento con fuente y salida. El recurso opcional
`python3 scripts/check_fragments.py FUENTE SALIDA FRAGMENTOS`, ejecutado desde
el directorio de esta skill, ayuda a encontrar
ausencias; solo normaliza espacios y devuelve índices de fragmentos, sin imprimir el
contenido. No acredita cobertura total, equivalencia semántica ni conservación
de relaciones, y no es un requisito para toda koraficación. Revisa por separado
lo que la salida afirma sin sustento y las condiciones que cambian el uso.

## Guardar una fuente útil

Localiza la raíz operativa desde la ruta de esta fuente y lee su `README.md`.
`create` publica una fuente nueva y conserva cada `--source` como bytes originales
con su hash y origen. El comando no sintetiza ni acredita fidelidad por sí solo.
Ejemplo con archivos autorados y revisados previamente:

```bash
python3 kora_cli.py create knowledge ejemplo criterios-entrega \
  --id urn:ejemplo:kb:criterios-entrega \
  --description 'Criterios de entrega y sus excepciones, derivados de la fuente indicada.' \
  --body /ruta/cuerpo.md --source /ruta/fuente.txt
python3 kora_cli.py resolve urn:ejemplo:kb:criterios-entrega
```

Para actualizar, resuelve primero la identidad existente y edita esa fuente.
Conserva la versión anterior mediante Git o un original recuperable según el
alcance. Registra la nueva procedencia en `object.yaml`; preserva identidades y
relaciones que sus consumidores aún necesitan. Declara dependencias operativas
en `requires` y vínculos documentales en `relations`, sin confundir ambos usos.

## Comprobar el resultado

Coteja el cuerpo con los originales, especialmente condiciones y excepciones.
Responde desde el producto una pregunta de uso normal, otra que active una
excepción y otra cuyo dato no exista. Compara esas respuestas con la fuente:
una respuesta fluida no acredita fidelidad. Verifica que cada recurso técnico
necesario se pueda abrir y que las referencias declaradas resuelvan mediante
`python3 kora_cli.py check`.

Entrega el producto recuperable, su procedencia y cualquier pérdida o
incompatibilidad concreta. Distingue la revisión semántica hecha de la validez
de archivos. Si falta una parte material de la fuente, conserva y explica esa
ausencia; no presentes la transformación como completa.
