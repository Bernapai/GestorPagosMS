# **Servicio de Notificaciones (Notifications) 📩**

Este microservicio maneja el **envío de alertas y notificaciones** relacionadas con pagos. Está construido con **Django Rest Framework (DRF)** y usa **MongoDB** como base de datos.

## 📌 Requisitos
- Docker instalado
- Python 3.9+
- MongoDB en ejecución (local o en la nube)


## 📡 Endpoints de la API

| Método | Endpoint            | Descripción |
|--------|---------------------|-------------|
| GET    | `api/notification/`   | Obtener todas las notificaciones |
| POST   | `api/notification/`   | Crear una nueva notificación |
| GET    | `api/notification/<id>/` | Obtener una notificación específica |
| PUT    | `api/notification/<id>/` | Actualizar una notificación |
| DELETE | `api/notification/<id>/` | Eliminar una notificación |








