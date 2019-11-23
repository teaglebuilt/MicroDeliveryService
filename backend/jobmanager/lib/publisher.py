import os
import pika 
import time


def publish(message, exchange):
    connection = pika.BlockingConnection(pika.URLParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange=exchange, exchange_type='fanout', durable=True)

    channel.basic_publish(exchange=exchange, routing_key='somekey', body=message,
                        properties=pika.BasicProperties(
                            delivery_mode=2,
                        ))