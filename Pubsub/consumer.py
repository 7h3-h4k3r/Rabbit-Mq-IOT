import pika

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
    exchange='logs',
    exchange_type = 'fanout'
)

result = channel.queue_declare(
    queue='',
    exclusive=True
)

queue_name = result.method.queue

channel.queue_bind(
    exchange='logs',
    queue=queue_name
)

def callback(ch,method,properties,body):
    print('receiverd ' ,body.decode())


channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True
)

channel.start_consuming()