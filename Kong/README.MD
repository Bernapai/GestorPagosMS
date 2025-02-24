# API Gateway 🌐

Este componente actúa como punto de entrada principal para el sistema de gestor de pagos. Redirige solicitudes a los microservicios correspondientes y maneja la autenticación y autorización mediante tokens JWT utilizando Kong.

## Funcionalidades
- Redirección de solicitudes a microservicios (`notificaciones`, `reports`, `transactions`, `users`).
- Manejo de autenticación y autorización con JWT.
- Protección de rutas según los permisos de usuario.

## Endpoints Principales
- `/auth/login`: Autenticación de usuario.
- `/auth/register`: Registro de nuevos usuarios.
- `/auth/refresh`: Renovación de tokens JWT.

## Tecnologías Utilizadas
- **Kong**
