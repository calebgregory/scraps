#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# if we want to connect to a broker on a different machine we'd simply specify its name or IP address here

channel.exchange_declare(exchange='direct_logs',
        type='direct')

# to emit, for example, an error log message, type
#   $ python emit_log_direct.py error "THIS IS AN ERROR MESSAGE"

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs',
        routing_key=severity,
        body=message,)

print " [x] Sent %r:%r" % (severity,message,)

connection.close()
