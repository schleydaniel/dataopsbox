import os
import time
import logging

from flask import Flask, render_template
from flask_sock import Sock
from dotenv import load_dotenv
from kafka import KafkaConsumer, TopicPartition

load_dotenv()
log_path = os.environ.get("LOG_PATH")
logging.basicConfig(filename=log_path, level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = Flask(__name__)
sock = Sock(app)

BOOTSTRAP_SERVERS = '10.106.7.84:9092'
TOPIC_NAME = 'telemetry-1'


@app.route('/')
def index():
    return render_template('index.html')


@sock.route('/echo')
def echo(sock):
    app.logger.info('Socket connected')
    while True:
        consumer = KafkaConsumer(group_id='consumer-1',
                                 bootstrap_servers=BOOTSTRAP_SERVERS)
        app.logger.info('consumer: {}'.format(str(consumer.topics())))
        tp = TopicPartition(TOPIC_NAME, 0)
        # register to the topic
        consumer.assign([tp])
        # obtain the last offset value
        consumer.seek_to_end(tp)
        last_offset = consumer.position(tp)
        app.logger.info('Last offset: {}'.format(str(last_offset)))
        consumer.seek_to_beginning(tp)
        for message in consumer:
            app.logger.info('Print msg: {}'.format(message.value.decode('utf-8')))
            data = message.value.decode('utf-8')
            sock.send(data)
            if message.offset == last_offset - 1:
                break
        consumer.close()
        time.sleep(5.0)

