#GOAL TO CREATE BASIC MESSAGING SITE THAT ALLOWS FOR REGISTRATION, LOGIN, MESSAGES, and COMMENTS

#main file
from flask import Flask, redirect, render_template, flash, session, request, url_for
from wall_connection import MySQLConnector
from flask_bcrypt import Bcrypt
import re 
import os #used for os.urandom()

app = Flask (__name__)
bcrypt = Bcrypt(app)
app.secret_key = os.urandom(32)
mysql = MySQLConnector(app, 'wall')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$') #standard from site

@app.route('/')  #  WORKS
def index():
    print "HOME PAGE"
    return render_template('index.html')

@app.route('/registration', methods=['POST'])  #works.  Was originally going to send comment form and message form here but didnt
def register():
    valid = True
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']  #    NOTE:  DATABASE I created had spelling error since i made it EMAILS
    password = request.form['password']
    pw_hash = bcrypt.generate_password_hash(password)
    confirm_password = request.form['confirm_pw']
    form = request.form['form']

    if len(first_name) < 1: #validation         shortened for testing
        valid = False
        flash('First Name must be at least 2 characters')
        return redirect ('/')
    if len(last_name) < 1: #validation          shortened for testing
        valid = False
        flash('Last Name must be at least 2 characters')
        return redirect ('/')
    # elif not EMAIL_REGEX.match(request.form['email']): #validation        removed for testing
        # valid = False
        # flash('Email must contain non-special characters followed by "2" sign then other characters followed by "." with more non-specail characters')
        # return redirect ('/')
    if len(password) < 1: #validation
        valid = False
        flash('PW must be at least 8 characters')
        return redirect ('/')
    if confirm_password != password: #validation
        valid = False
        flash('Confirm_PW must be identical to PW')
        return redirect ('/')

    if valid: 
        query = '''INSERT INTO users(first_name, last_name, email, password, confirm_password, created_at, updated_At) 
        VALUES (:first_name, :last_name, :email, :pw_hash, :confirm_pw, NOW(), NOW())'''
        data = {
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'email':request.form['email'],
            'pw_hash': pw_hash,
            'confirm_pw': request.form['confirm_pw']
        }
        new_user = mysql.query_db(query,data)
        print "RECORD INSERTED.  NEW USER INFORMATION INCLUDES: ", new_user    
        return redirect('/')

@app.route('/login', methods=['POST'])  #   WORKS
def login():
    login_email = request.form['email']
    password = request.form['password']
    query = 'SELECT * FROM users WHERE email = :email LIMIT 1'
    data = {
        'email':login_email
    }
    user = mysql.query_db(query, data) #    WORKS
    if "user_id" not in session:
        session['user_id'] = int(user[0]['id']) #id = user_id to pull later for comments
        session['first'] = user[0]['first_name'] 
        session['last'] = user[0]['last_name'] 
        session['email'] = user[0]['email']
    if bcrypt.check_password_hash(user[0]['password'],password): #uses password to decrpyt code
        session['user_id'] = int(user[0]['id']) #id = user_id to pull later for comments
        session['first'] = user[0]['first_name'] 
        session['last'] = user[0]['last_name'] 
        session['email'] = user[0]['email']
        print session['user_id']
        print session['first']
        print session['last']
        return redirect('/show_messages')
    else:
        ('Password not confirmed')
        flash('Passwords do not match')
        print "passwords do not match"
        return redirect('/')
                    
@app.route('/show_messages')   #    WORKS
def show_messages_and_comments():
    show_query = '''SELECT *
                    FROM messages
                    '''
    message_query = mysql.query_db(show_query)  #Created to pull and show using JINJA in FLASK MESSAGES TEMPLATE WITH INTERPOLATION
    full_name_query = "SELECT concat_ws(' ', first_name, last_name) as full FROM users"
    full_name= mysql.query_db(full_name_query)
    f_message_created = message_query[0]['created_at']
    f_message_id = message_query[0]['users_id']
    f_user = full_name[0]['full']
    print message_query
    print f_user
    print "hey"
    if len(message_query) != 0:
        return render_template('messages.html',thingy = f_user, thingy1 = f_message_created,thingy2 = f_message_id, mq = message_query)
    else:
        return render_template('messages.html')

@app.route('/store_messages', methods=['POST']) #   WORKS
def store_message_comment():
    query = '''INSERT INTO messages(users_id, content, created_at, updated_at) 
    VALUES (:users_id, :content, NOW(), NOW())'''
    data = {
        'users_id': session['user_id'],
        'content':request.form['message_content'],
    }
    mysql.query_db(query,data)
    print session['user_id']
    print request.form['message_content']
    return redirect('/show_messages')

@app.route('/store_comments', methods=['POST']) 
def store_comment():
    return redirect('/show_messages')
app.run(debug=True)