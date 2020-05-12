from flask import Flask, render_template
import os
import json
import logging.config

app = Flask(__name__)


@app.before_first_request
def setup_logging(
        default_path='logging.json',
        default_level=logging.DEBUG,
        env_key='LOG_CFG=my_logging.json'
):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


@app.route('/', methods=['GET', 'POST'])
def logging_demo():
    app.logger.info('Processing default request')
    app.logger.warning('Processing warning request')
    app.logger.debug('Processing debug request')
    app.logger.error('Processing error request')
    app.logger.critical('Processing critical request')
    return render_template('index.html')


# run always put in last statement or put after all @app.route
if __name__ == '__main__':
    app.run(host='localhost')
