from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/user/<name>')
def user(name):
    return "Hello, %s!" %name

@app.route('/browser')
def browser():
    user_agent = request.headers.get('User-Agent')
    return "Your browser is: %s" % user_agent

@app.route('/cookie')
def cookie():
    response = make_response('This document carries a cookie')
    response.set_cookie('answer','100')
    return response

if __name__ == '__main__':
    app.run(port=5000,debug=True)