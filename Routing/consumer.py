import pika 
import sys
credentials = pika.PlainCredentials('dharani','dharani@123')


parameter = pika.ConnectionParameters(
    'rabbitmq.selfmade.ninja',
    5672,
    'username420sri_dharani',
    credentials
)

connection_block = pika.BlockingConnection(parameter)

channel = connection_block.channel()

channel.exchange_declare(
    exchange='logs_direct',
    exchange_type='direct'
)

result = channel.queue_declare(queue='')

queue_name = result.method.queue

routing_key =  sys.argv[1] if len(sys.argv) > 1 else 'info'
channel.queue_bind(
    exchange='logs_direct',
    queue=queue_name,
    routing_key=routing_key
)

print('Waiting for a message ')

def callback(ch,method,properties,body):
    print('Recevied : ',body.decode())


channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True
)


channel.start_consuming()