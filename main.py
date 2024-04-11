import pika 


def producer():
    conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = conn.channel()

    channel.queue_declare(queue='punitRandi')

    channel.basic_publish(exchange='', routing_key='punitRandi', body='Hello World!')

    print(" [x] Sent 'Hello World!'")

    conn.close()

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")
    
def nomnom():
    conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = conn.channel()
    channel.queue_declare(queue='punitRandi')
    channel.basic_consume(queue='punitRandi',
                      auto_ack=True,
                      on_message_callback=callback)



nomnom()