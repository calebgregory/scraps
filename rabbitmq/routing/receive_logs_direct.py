#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
        type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# if you only want to save 'warning' and 'error' (and not 'info') log messages to a file,
# open a console and type:
#   $ python receive_logs_direct.py warning error >> logs_from_rabbit.log
# if you want to see all of the messages on your screen, open a new terminal and
#   $ python receive_logs_direct.py warning error info

severities = sys.argv[1:]
if not severities:
    print >> sys.stderr, "Usage: %s [info] [warning] [error]" % \
            (sys.argv[0],)
    sys.exit(1)

for severity in severities:
    channel.queue_bind(exchange='direct_logs',
            queue=queue_name,
            routing_key=severity)

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] %r:%r" % (method.routing_key, body,)

channel.basic_consume(callback,
        queue=queue_name,
        no_ack=True)

channel.start_consuming()
