import logging
import time


class KafkaMock:
    def __init__(self):
        self.logger = logging.getLogger('kafkamock')
        self.logger.info('Init KafkaMock')

    def send(self, topic, key, value):
        self.logger.info(value)
        time.sleep(1)
        metamock = MetaDataMock(topic)
        return metamock


class MetaDataMock:
    def __init__(self, topic):
        self.logger = logging.getLogger('MetadataMock')
        self.logger.info('Init MetadataMock')
        self.topic = topic

    def get(self, timeout=10):
        self.logger.info(timeout)
        time.sleep(1)
        return self
