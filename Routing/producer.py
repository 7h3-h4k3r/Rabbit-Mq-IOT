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

#create a direct exchange 

channel.exchange_declare(
    exchange='log_direct',
    exchange_type = 'direct'
)

# Routing key 

routing_key =  sys.argv[1] if len(sys.argv) > 1 else 'info'

#message body
message = 'hi iam from the rabbit mq error routing key'

# publish Message 

channel.basic_publish(
    exchange='logs_direct',
    routing_key=routing_key,
    body=message
)

print('Message Send successfully ')


connection_block.close()
