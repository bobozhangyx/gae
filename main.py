# test.py
import urllib
import urllib2
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

@app.route('/down_get', methods=['GET', 'POST'])
def down_get():
    url = 'http://www.baidu.com'
    values = {}
    values['username'] = "1016903103@qq.com"
    values['password'] = "XXXX"
    data = urllib.urlencode(values)
    geturl = url + "?" + data
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    header = {'User-Agent': user_agent}
    request = urllib2.Request(geturl, headers=header)
    response = urllib2.urlopen(request)
    return response.read()

@app.route('/down_post', methods=['GET', 'POST'])
def down_post():
    values = {"username": "1016903103@qq.com", "password": "XXXX"}
    data = urllib.urlencode(values)
    url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    data = urllib.urlencode(values)
    request = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(request)
    return response.read()
if __name__ == '__main__':
    app.run()
