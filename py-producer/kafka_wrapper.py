import hashlib
import json
import logging
import threading
import time

from datetime import datetime
from threading import Thread
from kafka import KafkaProducer
from kafka.errors import KafkaError
from kafka_mock import KafkaMock


class DBKafkaProducer(Thread):
    def __init__(self, topic, kafka_bootstrap, count):
        Thread.__init__(self)
        self.logger = logging.getLogger("DBKafkaProducer")
        self.logger.info('Init DBKafkaProducer ' + self.name)
        self.topic = topic
        self.kafka_bootstrap = kafka_bootstrap
        self.count = count

    def run(self):
        start = datetime.now()
        if self.kafka_bootstrap == 'MOCK':
            producer = KafkaMock()
        else:
            producer = KafkaProducer(bootstrap_servers=[self.kafka_bootstrap])
        thread = threading.current_thread()
        for i in range(0, int(self.count)):
            key = str(i).encode()
            message = {'deviceId': hashlib.md5(bytes(thread.name, 'utf-8')).hexdigest(), 'timestamp': str(time.time()),
                       'key': 'POSITION', 'value': '13.330059,74.74467,-12.0'}

            # Encode the dictionary into a JSON Byte Array
            data = json.dumps(message, default=str).encode('utf-8')

            # Asynchronous by default
            future = producer.send(self.topic, key=key, value=data)
            # Block for 'synchronous' sends
            try:
                record_metadata = future.get(timeout=10)
                # Successful result returns assigned partition and offset
                self.logger.info(record_metadata.topic + ":" + str(data))
            except KafkaError:
                # Decide what to do if produce request failed...
                self.logger.error("Error")
                pass

        end = datetime.now()
        self.logger.info('Duration ' + self.name + ' : ' + str((end - start).seconds) + ' seconds')

    def join(self, **kwargs):
        Thread.join(self)
