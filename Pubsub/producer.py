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
    exchange_type='fanout'
)

message =  'Hello i am from rabbit mq pub\sub '

channel.basic_publish(
    exchange='logs',
    routing_key='',
    body=message
)

print('send:',message)
connection_block.close()