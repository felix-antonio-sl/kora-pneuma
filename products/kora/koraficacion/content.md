# Koraficación

Transforma una o varias fuentes en conocimiento que ayude a comprender o actuar.
El tratamiento por defecto conserva todo su contenido sustantivo y lo expresa
con economía, cualquiera sea su formato o dominio. Sólo una selección de alcance
explícita permite dejar contenido fuera; una pregunta actual no redefine por sí
sola qué merece conservarse. La salida
debe poder leerse, comprobarse, recuperarse y actualizarse sin depender de la
memoria de quien la escribió. El artefacto resultante es una referencia de la
biblioteca de conocimiento, separada de agentes y skills.

## Leer y componer

Aplica `koraficacion-integral` como procedimiento de transformación en toda
koraficación. Lee su [fuente](../koraficacion-integral/content.md) o su `SKILL.md`
instalado y sigue el inventario, compresión, cotejo y reparación que establece.
Esta skill conduce la entrada y publicación en KORA; el método integral mantiene
en un solo lugar el criterio de contenido y el trabajo por bloques.

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

Escribe para las decisiones de su consumidor, no siguiendo por inercia los
encabezados de la fuente. Fusiona obligaciones repetidas cuando no aporten una
condición, autoridad o énfasis distinto; conserva cada regla en un lugar y
remite a ella donde haga falta. Pasar listas a párrafos no elimina redundancia.
La compresión se detiene antes de perder una condición relevante o su fundamento.
Mantén la procedencia y los localizadores comprobables en la evidencia auxiliar.
Incluye en el cuerpo la atribución o referencia que el lector necesite para
interpretar una afirmación, distinguir versiones o resolver una discrepancia;
no arrastres el soporte del ejemplar. Un esquema,
dataset, imagen, binario o script conserva su formato si la prosa destruye su
función; el cuerpo explica cómo usarlo.

Antes de crear un objeto, busca por su identidad y por términos distintivos en
las referencias existentes. Si el conocimiento ya está representado, decide si
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

## Preparar y publicar una referencia

Consulta la [guía operativa](../../../docs/operacion.md) desde la raíz de la
maquinaria. La biblioteca se selecciona mediante `knowledge` o
`--knowledge-root`. `intake` conserva recursos de entrada en `inbox`; úsalo al
recibir originales que aún no tienen un lugar recuperable dentro del flujo.
`create knowledge` guarda un borrador y conserva cada `--source` como bytes
originales con su hash y origen. Ninguno de esos comandos sintetiza, aprueba ni
deja el borrador disponible como referencia publicada.

Para actualizar, resuelve la identidad existente y usa `revise` para preparar su
borrador. Edita ese contenido, sus recursos y `object.yaml`; registra la nueva
procedencia y preserva identidades y relaciones que sus consumidores necesitan.
Declara conocimientos necesarios en `requires` y vínculos documentales en
`relations`. La versión anterior sigue consultable mientras trabajas. No edites
directamente versiones publicadas ni enlaces de referencia.

## Comprobar el resultado

Coteja fuente→salida para detectar omisiones y salida→fuente para detectar
adiciones o cambios de sentido. Comprueba condiciones, excepciones y modalidad:
«si basta» no equivale a «siempre basta». Revisa también las repeticiones que
quedan, antes de afirmar que eliminaste redundancia. Para comprobar utilidad,
responde desde el producto una pregunta y contrástala con la fuente; incluye
una excepción o dato ausente cuando cambien su uso. Una respuesta fluida no
acredita fidelidad. Abre los recursos técnicos necesarios y resuelve las
referencias cambiadas; el diagnóstico del catálogo es una comprobación distinta.

Usa `review` para identificar el borrador concreto por su hash. Presenta el
contenido revisado, su procedencia y cualquier pérdida o incompatibilidad
material. Cuando Félix haya aprobado ese contenido, o delegado explícitamente
esa decisión, ejecuta `approve URN --reviewed SHA` con el hash revisado. Si cambió
el borrador o su revisión base, revisa el cambio antes de publicarlo. La autoridad
para reparar maquinaria no aprueba contenido de conocimiento.

La publicación conserva la versión y actualiza una referencia estable; una
consulta por revisión permite recuperar la versión exacta. Comprueba que la
identidad resuelve al resultado publicado y entrega esa referencia. Si todavía
falta aprobación, entrega el borrador revisable como tal. Distingue la revisión
semántica hecha de la validez de archivos y de la aprobación. Los conocimientos
heredados con estado `legacy` conservan su disponibilidad sin acreditar una
aprobación nueva. Si falta una parte material de la fuente, conserva y explica
esa ausencia; no presentes la transformación como completa.
