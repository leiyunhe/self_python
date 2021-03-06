from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///tutorial.db', echo=True)
 
app = Flask(__name__)
 
@app.route('/')
def home():
    '''login page'''
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!  <a href='/logout'>Logout</a>"

@app.route('/error')
def error():
    return "wrong"

@app.route('/login', methods=['POST'])
def do_admin_login():
    '''deal with login'''
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()

    if result:
        session['logged_in'] = True
        return home()
    else:
        print('wrong')
        flash('wrong password!')
        return error()
 
    # https://pythonspot.com/en/flask-web-forms/

@app.route("/logout")
def logout():
    '''deal with logout'''
    session['logged_in'] = False
    return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)