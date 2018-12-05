#!/home/c4850/tryrest.na4u.ru/.env/bin/python

import os

import catch as catch
from flask import Flask

try:
    IP = os.environ['APP_IP']
    PORT = int(os.environ['APP_PORT'])
except:
    IP = '127.0.0.1'
    PORT = '5000'



app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host=IP, port=PORT, debug=True)
