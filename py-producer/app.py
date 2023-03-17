import os
import logging

from flask import Flask, request, render_template
from urllib.parse import urlparse
from dotenv import load_dotenv


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


if __name__ == '__main__':
    load_dotenv()
    app.run(host='0.0.0.0', port=5050)

