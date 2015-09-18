#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# if we want to connect to a broker on a different machine we'd simply specify its name or IP address here

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or 'Hello World!'
channel.basic_publish(exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode = 2, # makes message persistent
        ))
print " [x] Sent %r" % (message,)

connection.close()
