import os
import pika


def publish(message, exchange):
    amqp_url = 'amqp://rabbit1?connection_attempts=5&retry_delay=5'
    connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
    channel = connection.channel()
    channel.exchange_declare(
        exchange=exchange, 
        exchange_type='fanout', 
        durable=True
    )
    channel.basic_publish(exchange=exchange, 
        routing_key='somekey', 
        body=message,
        properties=pika.BasicProperties(
        delivery_mode=2,
    ))