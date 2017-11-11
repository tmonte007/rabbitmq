#!/usr/bin/env python

import pika, os

url = os.environ.get('CLOUDAMQP_URL')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel

channel.queue_declare(queue='testqueue')

def callback(ch, method, properties, body):
  print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='testqueue',
                      no_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()