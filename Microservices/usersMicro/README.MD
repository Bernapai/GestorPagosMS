# **Servicio de Users 👥**

Este microservicio maneja la gestión de Usuarios en una arquitectura basada en microservicios. Está desarrollado con Django Rest Framework (DRF) y utiliza MySql como base de datos. 
## 📌Requisitos
-Python 3.9+
-MySql en ejecución (local o en la nube)
-Docker (opcional, para despliegue)

## 📡 Endpoints de la API

| Método | Endpoint               | Descripción |
|--------|------------------------|-------------|
| GET    | `/api/users/`      | Obtener todos los usuarios |
| POST   | `/api/users/`      | Crear nuevo usuario |
| GET    | `/api/users/<id>/` | Obtener un usuario  |
| DELETE | `/api/users/<id>/` | Eliminar un usuario |