#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('dharani','dharani@123')
parameter = pika.ConnectionParameters('rabbitmq.selfmade.ninja',5672,'username420sri_dharani',credentials)

connection = pika.BlockingConnection(parameter)
channel = connection.channel()
channel.queue_declare(queue='hello', durable=True, arguments={'x-queue-type': 'quorum'})
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
