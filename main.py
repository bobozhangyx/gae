# test.py

import urllib
import urllib2
import json

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    url = 'http://ipecho.net/plain'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    return response.read()


@app.route('/down', methods=['POST'])
def down():
    down_method = request.form.get('down_method', '')
    down_url = request.form.get('down_url','')
    down_header = json.loads(request.form.get('down_header', ''))
    if down_method == 'get':
        target_request = urllib2.Request(down_url, headers=down_header)
        response = urllib2.urlopen(target_request)
        return response.read()
    elif down_method == 'post':
        data = json.loads(request.form.get('data', ''))
        target_request = urllib2.Request(down_url, urllib.urlencode(data), down_header)
        response = urllib2.urlopen(target_request)
        return response.read()
    return 'method must be defined'


if __name__ == '__main__':
    app.run()
