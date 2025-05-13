import pika

def get_connection():
    return pika.BlockingConnection(pika.ConnectionParameters('localhost'))

def get_channel():
    connection = get_connection()
    return connection.channel()