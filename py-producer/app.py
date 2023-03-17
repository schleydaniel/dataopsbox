import os
import logging

from flask import Flask, request, render_template
from urllib.parse import urlparse
from dotenv import load_dotenv
from kafka.admin import KafkaAdminClient
from kafka_wrapper import DBKafkaProducer


load_dotenv()
log_path = os.environ.get("LOG_PATH")
logging.basicConfig(filename=log_path, level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
app = Flask(__name__)


@app.route('/')
def home():
    o = urlparse(request.base_url)
    app.logger.info("Request from: {}, {}, {}".format(o.hostname, o.port, o.path))
    return render_template(
        'home.html',
        title="DataOpsBox",
        description="Container based data environment for data ops showcases"
    )


@app.route('/produce', methods=['GET'])
def produce():
    app.logger.info("/produce init (GET)")
    try:
        kafka_bootstrap = os.environ.get("KAFKA_BOOTSTRAP")
        admin_client = KafkaAdminClient(bootstrap_servers=[kafka_bootstrap])
        topics = admin_client.list_topics()
        app.logger.info(topics)
    except Exception as error:
        app.logger.error('Error: ' + str(error))
    finally:
        topics = []
    return render_template(
        'produce.html',
        title="Message Producer",
        results=topics
    )


@app.route('/produce', methods=['POST'])
def produce_run():
    app.logger.info("/produce run (POST)")
    kafka_bootstrap = os.environ.get("KAFKA_BOOTSTRAP")
    workers = os.environ.get("PRODUCER_WORKERS")
    total_count = request.form['count']
    app.logger.info('Total count set to: ' + str(total_count))
    count = int(int(total_count) / int(workers))
    threads = []
    app.logger.info('Sending {} messages via {} worker threads ({} each).'.format(total_count, workers, count))
    for i in range(0, int(workers)):
        thread = DBKafkaProducer("quickstart-events", kafka_bootstrap, count)
        thread.daemon = True
        thread.start()
        threads.append(str(thread))
        app.logger.info('Thread started: ' + str(thread))

    return render_template(
        'produce.html',
        title="Message Producer",
        results=threads
    )


if __name__ == '__main__':
    load_dotenv()
    app.run(host='0.0.0.0', port=5050)

