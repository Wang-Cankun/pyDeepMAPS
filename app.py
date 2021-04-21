from flask import Flask
import os
import time
import redis
import glob

app = Flask(__name__)
cache = redis.Redis(host='10.94.2.224', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)


@app.route('/data')
def list_data():
    return glob.glob("/data")


@app.route('/gpu')
def print_gpu():
    return os.system("nvidia-smi")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
