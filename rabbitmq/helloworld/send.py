#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# if we want to connect to a broker on a different machine we'd simply specify its name or IP address here

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
        routing_key='hello',
        body='Hello World!')
print " [x] Sent 'Hello World!'"

connection.close()
