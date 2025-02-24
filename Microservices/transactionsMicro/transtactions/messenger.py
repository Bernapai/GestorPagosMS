import json
import pika
from config import settings
from .models import Transaction

def send_message_to_queue(queue_name, message):
    """Envía un mensaje a la cola de RabbitMQ"""
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=settings.RABBITMQ_HOST)
    )
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)

    channel.basic_publish(
        exchange="",
        routing_key=queue_name,
        body=json.dumps(message),
        properties=pika.BasicProperties(delivery_mode=2)  # Hace que el mensaje sea persistente
    )

    connection.close()

    
def create_transaction_and_send_messages(serializer):
    """Crea una transacción y envía mensajes a RabbitMQ"""
    transaction = serializer.save()

    # Crear mensaje para reportes
    report_message = {
        "title": f"Reporte de Transacción {transaction.id}",
        "user": transaction.user_id,
        "description": f"Se realizó una transacción de ${transaction.amount} en la categoría {transaction.category}.",
    }
    send_message_to_queue(settings.RABBITMQ_QUEUE_REPORTS, report_message)

    # Crear mensaje para notificaciones
    notification_message = {
        "titulo": "Nueva Transacción",
        "descripcion": f"Tu transacción de ${transaction.amount} ha sido procesada.",
    }
    send_message_to_queue(settings.RABBITMQ_QUEUE_NOTIFICATIONS, notification_message)