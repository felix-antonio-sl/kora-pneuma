# AGENTS.md

## Misión

{{resultado que produce este software, para quién y por qué importa}}

## Entrada y autoridad

- Usa `README.md` para orientación humana y el estado vivo del repositorio para decidir.
- Si existe `HANDOFF.md`, léelo solo al retomar trabajo material inconcluso y
  revalídalo contra Git, código, pruebas y runtime.
- {{fuentes canónicas, autoridad externa y derivados; elimina si no aplica}}

## Arquitectura y alcance

- {{estructura principal y dirección de dependencias que debe preservarse}}
- Cambia solo lo trazable al objetivo; conserva trabajo ajeno y evita abstracciones,
  dependencias o automatización especulativas.
- {{paths preservados, límites entre repositorios o decisiones vinculantes}}

## Desarrollo y verificación

{{comandos reales que permiten trabajar y comprobar el resultado; si todavía no
existen, describe cómo se revisa el cambio sin atribuir comprobaciones ausentes}}

- Ejecuta primero la comprobación focal y amplía según el riesgo.
- Revisa el diff completo y no presentes como validado lo no ejecutado u observado.

## Seguridad y entrega

- No expongas secretos, PII/PHI ni datos productivos en prompts, logs, pruebas o commits.
- No publiques, despliegues ni produzcas efectos externos fuera de la autoridad solicitada.
