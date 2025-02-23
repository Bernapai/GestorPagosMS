import json
import pika
from reportMicro.config import settings
from .models import Report

def callback(ch, method, properties, body):
    """Procesa el mensaje recibido de la cola de RabbitMQ"""

    # 1 Convertir el mensaje JSON a diccionario
    data = json.loads(body)
    
    # 2️ Crear un nuevo registro en la base de datos
    Report.objects.create(
        title=data["title"],
        user=data["user"],
        description=data["description"]
    )

    print(f" Reporte creado: {data}")

    # 3️ Confirmar que el mensaje fue procesado correctamente
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