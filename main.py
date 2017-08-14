# test.py

import urllib2
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
    method = request.form['method']
    url = request.form['url']
    header = request.form['header']
    if method == 'method':
        target_request = urllib2.Request(url, headers=header)
        response = urllib2.urlopen(target_request)
        return response.read()
    elif method == 'post':
        data = request.form['data']
        target_request = urllib2.Request(url, data, header)
        response = urllib2.urlopen(target_request)
        return response.read()
    return 'method must be defined'


if __name__ == '__main__':
    app.run()
