import json
import pika
from notificacionesMicro.config import settings
from .models import Notificacion

def callback(ch, method, properties, body):
    """Procesa el mensaje recibido de la cola de RabbitMQ"""
    
    data = json.loads(body)

    # Crear una nueva notificación
    Notificacion.objects.create(
        titulo=data["titulo"],
        descripcion=data["descripcion"]
    )

    print(f" Notificación creada: {data}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_consumer():
    """Inicia el consumidor para procesar mensajes de la cola"""

    # 1. Establecer conexión con RabbitMQ usando credenciales si son necesarias
    credentials = pika.PlainCredentials(settings.RABBITMQ_USER, settings.RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=settings.RABBITMQ_HOST, credentials=credentials)
    )
    channel = connection.channel()

    # 2. Asegurar que la cola existe
    channel.queue_declare(queue=settings.RABBITMQ_QUEUE, durable=True)

    # 3. Indicar que se usará la función `callback` para procesar mensajes
    channel.basic_consume(queue=settings.RABBITMQ_QUEUE, on_message_callback=callback)

    print("Esperando mensajes en la cola de reportes...")
    
    # 4. Iniciar el consumo de mensajes
    channel.start_consuming()