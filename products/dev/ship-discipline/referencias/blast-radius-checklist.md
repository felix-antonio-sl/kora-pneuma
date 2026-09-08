# Blast radius checklist

Estimar consecuencias y reversibilidad para elegir el trabajo y las pruebas.

## Criterios de estimacion

Considera lo que pueda cambiar la decisión:

- conducta, datos y consumidores afectados directa o indirectamente;
- compatibilidad de interfaces y dependencias;
- costo de equivocarse y forma de conservar o recuperar el estado anterior;
- incertidumbre que convenga resolver antes de escribir;
- autoridad disponible para los efectos concretos.

La cantidad de archivos ayuda a localizar el alcance; no determina el riesgo.
Una migración puede requerir ensayar lectura y recuperación de datos, mientras
que un cambio de instrucciones puede alterar conducta sin tocar código.

## Elegir la intervención

Ejecuta directamente si el efecto y la reversión son claros. Ordena los pasos
cuando existan dependencias entre ellos y ensaya las condiciones cuyo fallo
tendría consecuencias materiales. Crea tooling solo si resuelve una necesidad
concreta que las herramientas existentes no cubren.

## Reglas

- Explica el riesgo relevante cuando cambie el plan o ayude a revisar el trabajo.
- Si aparece un efecto nuevo, revisa su alcance antes de ejecutarlo y conserva
  el trabajo independiente que siga siendo seguro y útil.
- Los efectos destructivos o externos deben estar cubiertos por la autorización
  vigente. Su aparición exige resolver el alcance cuando no esté concedido;
  no exige renovar una autorización explícita que ya los incluye.

## Antipatrones

| Antipatron | Falla | Correccion |
|---|---|---|
| Contar archivos como riesgo | Omitir consecuencias de un cambio pequeño | Examinar comportamiento y consumidores |
| Dar por supuesta la reversión | Perder datos o trabajo ajeno | Comprobar cómo se conserva el estado previo |
| Plan elaborado sin incertidumbre material | Costo sin efecto útil | Ejecutar el menor cambio completo |
| Actuar con efectos todavía desconocidos | Exceder alcance o dañar consumidores | Resolver la incertidumbre decisiva |
