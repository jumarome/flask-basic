from flask import Flask, request, make_response, render_template

app = Flask(__name__)

comments = ['cool site','great app','cool stuff']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.route('/browser')
def browser():
    user_agent = request.headers.get('User-Agent')
    return "Your browser is: %s" % user_agent

@app.route('/cookie')
def cookie():
    response = make_response('This document carries a cookie')
    response.set_cookie('answer','100')
    return response

@app.route('/comments')
def get_comments():
    return  render_template('comments.html',comments=comments)

if __name__ == '__main__':
    app.run(port=5000,debug=True)