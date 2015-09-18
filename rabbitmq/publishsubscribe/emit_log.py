#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# if we want to connect to a broker on a different machine we'd simply specify its name or IP address here

channel.exchange_declare(exchange='logs',
        type='fanout')

message = ' '.join(sys.argv[1:]) or 'info: Hello World!'
channel.basic_publish(exchange='logs',
        routing_key='',
        body=message,)

print " [x] Sent %r" % (message,)

connection.close()
