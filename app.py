from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello_whale():
    return 'Hello, world'


@app.route('/gpu')
def print_():
    return os.system("nvidia-smi")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
