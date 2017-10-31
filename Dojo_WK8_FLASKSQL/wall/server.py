from flask import Flask, redirect, render_template, flash, session, request
from wall_connection import MySQLConnector
from flask_bcrypt import Bcrypt
import re 
import os

app = Flask (__name__)
bcrypt = Bcrypt(app)
app.secret_key = os.urandom(32)
mysql = MySQLConnector(app, 'walldb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    print "HOME PAGE"
    return render_template('index.html')

@app.route('/registration', methods=['POST'])
def register():
    valid = True
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    pw_hash = bcrypt.generate_password_hash(password)
    confirm_password = request.form['confirm_pw']
    form = request.form['form']

    if form == 'register': #registration works
        if len(first_name) < 3: #validation
            valid = False
            flash('First Name must be at least 2 characters')
            return redirect ('/')
        if len(last_name) < 3: #validation
            valid = False
            flash('Last Name must be at least 2 characters')
            return redirect ('/')
        elif not EMAIL_REGEX.match(request.form['email']): #validation
            valid = False
            flash('Email must contain non-special characters followed by "2" sign then other characters followed by "." with more non-specail characters')
            return redirect ('/')
        if len(password) < 1: #validation
            valid = False
            flash('PW must be at least 8 characters')
            return redirect ('/')
        if confirm_password != password: #validation
            valid = False
            flash('Confirm_PW must be identical to PW')
            return redirect ('/')

        if valid:
            query = '''INSERT INTO users(first_name, last_name, email, password, confirm_password, created_At, updated_At) 
            VALUES (:first_name, :last_name, :email, :pw_hash, :confirm_pw, NOW(), NOW())'''
            data = {
                'first_name':request.form['first_name'],
                'last_name':request.form['last_name'],
                'email':request.form['email'],
                'pw_hash': pw_hash,
                'confirm_pw': request.form['confirm_pw']
            }
            new_user = mysql.query_db(query,data)
            print "RECORD INSERTED"    
            return redirect('/')

@app.route('/login', methods=['POST'])  #login works
def login():
    login_email = request.form['email']
    password = request.form['password']
    query = 'SELECT * FROM users WHERE email = :email LIMIT 1'
    data = {
        'email':str(login_email)
    }
    user = mysql.query_db(query, data) #Getting user information from database
    session['user_id'] = user[0]['id'] #id = ser_id to pull later for comments
    session['first'] = user[0]['first_name'] #works!
    session['last'] = user[0]['last_name'] #id = ser_id to pull later for comments
    session['email'] = user[0]['email']
    if bcrypt.check_password_hash(user[0]['password'],password): #uses password to decrpyt code
        print session['user_id']
        print session['first']
        print session['last']
        return redirect('/show_messages')
    else:
        ('Password not confirmed')
        flash('Passwords do not match')
        print "passwords do not match"
        return redirect('/')
                    
@app.route('/show_messages') #need post method as well
def show_messages_and_comments():
    show_query = '''SELECT *
                    FROM messages
                
                    '''
    message_query = mysql.query_db(show_query)
    f_message_created = message_query[0]['created_at']
    f_message_id = message_query[0]['users_id']
    f_message = message_query[2]['content']

    print message_query
    return render_template('messages.html', thingy = f_message, thingy1 = f_message_created,thingy2 = f_message_id,  message_query = message_query[0])

@app.route('/comments')
def comments():
    return render_template('comments.html', email = session['email'], content = session['content'])
#user not showing

@app.route('/store_comments_and_messages', methods=['POST']) 
def store_message_comment():
    query = '''INSERT INTO messages(users_id, content, created_at, updated_at) 
    VALUES (:users_id, :content, NOW(), NOW())'''
    data = {
        'users_id': session['user_id'],
        'content':request.form['message_content'],
    }
    mysql.query_db(query,data)
    print request.form['message_content']
    return redirect('/show_messages')

app.run(debug=True)