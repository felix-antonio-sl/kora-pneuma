# HANDOFF

Estado: proyección runtime pendiente

## Pendiente

Las fuentes y emisiones locales de `urn:dev:artefacto:diagnosing-bugs` y
`urn:dev:artefacto:code-review` existen, pero ambas instalaciones Codex siguen
`no-instalada`. Este piloto no ejecutó `transmutar --aplicar`, no cambió
lifecycle y no desplegó.

La integración y materialización de consumidores KORA en OpenClaw Fleet es un
frente externo. Su `main` local está adelantado y contiene cambios sin cerrar;
no lo mezcles con una operación KORA.

## Al retomar

1. Elige uno de los dos frentes; no los cierres como una sola entrega.
2. Revalida Git, emisiones, instalación y paridad en vivo.
3. Obtén autoridad explícita antes de aplicar o desplegar.
4. Canariza, verifica el runtime y conserva rollback.

El cierre histórico y otros pendientes curatoriales se recuperan desde
`0f9ed3b`; no se duplican aquí. Elimina este archivo cuando no quede trabajo
material inconcluso.
