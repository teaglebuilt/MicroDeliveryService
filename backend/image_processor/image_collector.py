from lib.consumer import Consumer
import pika


EXCHANGE = 'Image_Exchange'
QUEUE = 'Image_Queue'


class Singleton(type):

    _instance ={}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instance[cls]



class ImageHandler(metaclass=Singleton):

    def __init__(self):
        print("Image Handler...")

    @property
    def get(self, filename):
        with open(filename, "rb") as f:
            data = f.read()
        return data

    def publish(self, message, exchange):
        print("publishing: message {} at exchange {}".format(message, exchange))
        self.channel.basic_publish(
            exchange=exchange, 
            routing_key='somekey', 
            body=message,
            properties=pika.BasicProperties(delivery_mode=2)
        )

    def on_message(self, channel, delivery, name):
        print("Received {}".format(name))
        img = self.get("./static/pic1.png")
        self.publish(img, 'jobmanager')
        channel.basic_ack(delivery.delivery_tag)


if __name__ == '__main__':
    handler = ImageHandler()
    Consumer(EXCHANGE, QUEUE, handler)
