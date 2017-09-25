import os
from flask import Flask, request, make_response, render_template, session, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from forms import RegisterForm


app = Flask(__name__)
app.config['SECRET_KEY']='AJMSFNDKSFDLANSFDLN'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
import entities
migrate = Migrate(app, db)

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

@app.route('/register',methods=('GET','POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        first_name  =   form.first_name.data
        last_name   =   form.last_name.data
        email       =   form.email.data
        session['user_mail'] =email


        return redirect(url_for('account'))
    return render_template('register.html',form=form)

@app.route('/account')
def account():
    return render_template('account.html')


if __name__ == '__main__':
    app.run(port=5000,debug=True)

