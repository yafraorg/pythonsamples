#!/usr/bin/env python

import pika

#credentials = pika.PlainCredentials('guest', 'guest')
#parameters = pika.ConnectionParameters('amqp.k8sd.pax.ch', 80, '/', credentials)
#parameters = pika.URLParameters('amqp://guest:guest@localhost:5672/%2F')
#connection = pika.BlockingConnection(parameters)
connection = pika.BlockingConnection()

channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World! MWN')
print(" [x] Sent 'Hello World! MWN'")

connection.close()
