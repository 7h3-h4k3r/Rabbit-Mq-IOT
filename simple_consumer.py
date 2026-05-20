#!/usr/bin/env python
import pika
def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
credentials = pika.PlainCredentials('dharani','dharani@123')
parameter = pika.ConnectionParameters('rabbitmq.selfmade.ninja',5672,'username420sri_dharani',credentials)

connection = pika.BlockingConnection(parameter)
channel = connection.channel()
channel.queue_declare(queue='hello', durable=True, arguments={'x-queue-type': 'quorum'})
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()