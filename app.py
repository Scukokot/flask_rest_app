#!/home/c4850/tryrest.na4u.ru/.env/bin/python

import os
from flask import Flask

IP = os.environ['APP_IP']
PORT = int(os.environ['APP_PORT'])

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host=IP, port=PORT, debug=True)
