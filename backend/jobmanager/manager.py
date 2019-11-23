from lib.publisher import publish
from lib.consumer import Consumer
import os
import pika  
import time


class DataCollector():

    def __init__(self):
        print("Listening...")

        def on_message(self, channel, delivery, body):
            print("Received: {} at JobManager".format(body))
            msg = body.decode('utf=8')
            split_command = msg.split(' ', 1)
            print(split_command[0])
            channel.basic_ack(delivery.delivery_tag)
            


if __name__ == '__main__':
    exchange = 'jobmanager'
    consumer = Consumer(exchange, 'jobmanager', DataCollector())