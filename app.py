#!/home/c4850/tryrest.na4u.ru/.env/bin/python

import os
import requests
import datetime
import json
from base64 import b64encode
from flask import Flask
from flask import request, jsonify, Response


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

@app.route('/api/v_0_0/push/ASUI/to_jira/created_item', methods=['GET', 'POST'])
def createItemFromNew():
    if request.method == 'POST':
        data = request.data
        try:
            f = open('requestdata.json','w')
        except:
            f= open('/home/c4850/tryrest.na4u.ru/app/requestdata.json', 'w')
        f.write(data)
        f.close()
        resp = Response("Foo bar baz")
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
#        return Response.data
    else:
        return "Hello, World!"

def in_out_json(data):
    e = data
    return e


if __name__ == '__main__':
    app.run(host=IP, port=PORT, debug=True)
