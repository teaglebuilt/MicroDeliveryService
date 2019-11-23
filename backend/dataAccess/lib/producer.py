import os
import pika

def publish(message, exchange):
    amqp_url = 'amqp://guest:guest@localhost:5672'
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