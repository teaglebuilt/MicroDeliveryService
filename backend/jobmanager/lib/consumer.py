import os
import pika
import time
from functools import partial


class Consumer(object):

    def __init__(self, exchange, queue, handler):
        self._exchange = exchange
        self._queue = queue
        self.handler = handler

        parameters = pika.URLParameters('amqp://rabbit1?connection_attempts=5&retry_delay=5')
        connection = pika.SelectConnection(parameters, on_open_callback=self.on_open)

        try:
            connection.ioloop.start()
        except KeyboardInterrupt:
            connection.close()
            connection.ioloop.start()

    def on_open(self, connection):
        """Callback when we have connected to the AMQP broker."""
        print('Connected')
        connection.channel(on_open_callback=self.on_channel_open)


    def on_channel_open(self, channel):
        """Callback when we have opened a channel on the connection."""
        print('Have channel')

        channel.exchange_declare(exchange=self._exchange, exchange_type='fanout',
                                durable=True,
                                callback=partial(self.on_exchange, channel))


    def on_exchange(self, channel, frame):
        """Callback when we have successfully declared the exchange."""
        print('Have exchange')
        channel.queue_declare(queue=self._queue, durable=True,
                            callback=partial(self.on_queue, channel))


    def on_queue(self, channel, frame):
        """Callback when we have successfully declared the queue."""
        print('Have queue')

        channel.basic_qos(prefetch_count=1, callback=partial(self.on_qos, channel))


    def on_qos(self, channel, frame):
        """Callback when we have set the channel prefetch limit."""
        print('Set QoS')
        channel.queue_bind(queue=self._queue, exchange=self._exchange,
                        callback=partial(self.on_bind, channel))


    def on_bind(self, channel, frame):
        """Callback when we have successfully bound the queue to the exchange."""
        print('Bound')
        channel.basic_consume(queue=self._queue, on_message_callback=self.slurp)


    def slurp(self, channel, delivery, properties, body):
        print('preparing to slurp messages from {}'.format(self._queue))
        time.sleep(2)
        print('slurping message {}'.format(body))
        self.handler.on_message(channel, delivery, body)


if __name__ == '__main__':
    main()