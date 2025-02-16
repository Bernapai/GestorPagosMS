# **Servicio de Reportes (Reports) 📊**  

Este microservicio maneja la **generación de reportes** relacionados con transacciones. Está construido con **Django Rest Framework (DRF)** y usa **MongoDB** como base de datos. Además, la generación de reportes se activa mediante mensajes enviados a través de **RabbitMQ**.  

## 📌 Requisitos  
- Docker instalado  
- Python 3.9+  
- MongoDB en ejecución (local o en la nube)  
- RabbitMQ configurado y en ejecución  

## 📡 Endpoints de la API  

| Método | Endpoint         | Descripción |
|--------|-----------------|-------------|
| GET    | `/reports/`     | Obtener todos los reportes generados |
| POST   | `/reports/`     | Solicitar la generación de un nuevo reporte (se envía a RabbitMQ) |
| GET    | `/reports/<id>/` | Obtener un reporte específico |
| DELETE | `/reports/<id>/` | Eliminar un reporte |

## 🔄 Flujo de Generación de Reportes con RabbitMQ  
1. Se realiza un **POST** a `/transaccionesMicro/` con los parámetros necesarios .
2.RabbitMQ redirige el mensaje a /reports y crea un post con sus parametros del report.  

