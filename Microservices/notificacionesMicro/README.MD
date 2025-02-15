# **Servicio de Notificaciones (Notifications) 📩**

Este microservicio maneja el **envío de alertas y notificaciones** relacionadas con pagos. Está construido con **Django Rest Framework (DRF)** y usa **MongoDB** como base de datos.

## 📌 Requisitos
- Docker instalado
- Python 3.9+
- MongoDB en ejecución (local o en la nube)


## 📡 Endpoints de la API

| Método | Endpoint            | Descripción |
|--------|---------------------|-------------|
| GET    | `/notifications/`   | Obtener todas las notificaciones |
| POST   | `/notifications/`   | Crear una nueva notificación |
| GET    | `/notifications/<id>/` | Obtener una notificación específica |
| PUT    | `/notifications/<id>/` | Actualizar una notificación |
| DELETE | `/notifications/<id>/` | Eliminar una notificación |








