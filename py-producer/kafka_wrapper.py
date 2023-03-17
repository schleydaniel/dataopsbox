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
            message = thread.name + '-' + str(i) + ';' + str(time.time()) + ';' + str(datetime.now())
            # Asynchronous by default
            future = producer.send(self.topic, key=b'ts', value=bytes(message, 'utf-8'))
            # Block for 'synchronous' sends
            try:
                record_metadata = future.get(timeout=10)
                # Successful result returns assigned partition and offset
                self.logger.info(record_metadata.topic + ":" + message)
            except KafkaError:
                # Decide what to do if produce request failed...
                self.logger.error("Error")
                pass

        end = datetime.now()
        self.logger.info('Duration ' + self.name + ' : ' + str((end - start).seconds) + ' seconds')

    def join(self):
        Thread.join(self)
        return self._return
