from kafka import KafkaProducer


def send_msg(server, topic: str, msg: str):
    producer = KafkaProducer(bootstrap_servers=server)
    msg_bytes = bytes(msg, 'UTF-8')
    producer.send(topic, msg_bytes)


if __name__ == '__main__':
    BOOTSTRAP_SERVER = 'localhost:9092'

    send_msg(server=BOOTSTRAP_SERVER, topic='test-topic', msg='the quick brown fox jumps over the lazy dog')
