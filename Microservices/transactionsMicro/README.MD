# **Servicio de Transacciones 💳**

Este microservicio maneja la gestión de transacciones en una arquitectura basada en microservicios. Está desarrollado con Django Rest Framework (DRF) y utiliza MongoDB como base de datos. Además, se implementa RabbitMQ con la librería Pika para la comunicación asincrónica entre servicios.

## 📌Requisitos
-Python 3.9+
-MongoDB en ejecución (local o en la nube)
-RabbitMQ configurado y en ejecución
-Docker (opcional, para despliegue)

## 📡 Endpoints de la API

| Método | Endpoint               | Descripción |
|--------|------------------------|-------------|
| GET    | `api/transaction/`      | Obtener todas las transaction |
| POST   | `api/transaction/`      | Crear una nueva transacción (envía mensaje a RabbitMQ) |
| GET    | `api/transaction/<id>/` | Obtener una transacción específica |
| DELETE | `api/transaction/<id>/` | Eliminar una transacción |

## 🔄 Flujo de Procesamiento de Transacciones con RabbitMQ
Se realiza un POST a api/transaction/ con los datos de la transacción.
La solicitud se almacena en MongoDB y se envía un mensaje a RabbitMQ a través de Pika.
Un consumidor escucha la cola de RabbitMQ y procesa la transacción de forma asincrónica.
Una vez procesada, la información se actualiza en la base de datos



## 📌 Notas Adicionales
Es recomendable usar Docker para facilitar la configuración de MongoDB y RabbitMQ.
Se pueden agregar más consumidores en RabbitMQ para balancear la carga y mejorar la escalabilidad del servicio.

