# AGENTS.md

## Misión

{{una-línea: qué resultado produce este repositorio y para quién}}

## Entrada y autoridad

- Lee `README.md` y {{fuentes canónicas o continuidad vigente necesarias}}.
- Usa el estado vivo del repositorio; documentación histórica no prueba actualidad.
- {{autoridad externa, derivados o fronteras entre repositorios; borrar si no aplica}}

## Arquitectura y reglas

- {{estructura o dirección de dependencias que debe preservarse}}
- Cambia solo lo trazable al objetivo y conserva trabajo ajeno.
- No agregues dependencias, abstracciones ni automatización sin una necesidad actual.
- {{reglas específicas del arquetipo; en conocimiento/cuaderno, declarar que no hay código}}

## Verificación

{{Añade solo comandos reales y ejecutables. Si todavía no existen, escribe
`Verificación automatizada: ABSENT` sin crear un bloque Bash.}}

- Amplía las comprobaciones según el riesgo y revisa el diff completo del alcance.
- No presentes como validado lo que no fue ejecutado u observado.

## Seguridad y entrega

- No expongas secretos, PII/PHI ni datos productivos en prompts, logs, pruebas o commits.
- No publiques, despliegues ni ejecutes efectos externos fuera de la autoridad solicitada.
