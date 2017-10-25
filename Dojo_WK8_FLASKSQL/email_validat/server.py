from flask import Flask, session, redirect, request, render_template, flash
import os 
from email_dbconnection import MySQLConnector

app = Flask (__name__)
app.secret_key = os.urandom(32)

mysql = MySQLConnector(app, 'emailsdb')

@app.route('/')
def index():
    if 'email' not in session:
        print "It begins"
        session['email'] = ''
        return render_template('index.html')
    else:
        return render_template('index.html')
        
    
@app.route('/email', methods=['POST'])
def email():
    email = request.form['email']
    if '@' in request.form['email'] and '.com' in request.form['email'] and len(request.form['email']) > 1:
        session['email'] = request.form['email']
        query = "INSERT INTO emails (email_entered) VALUES (:email)"
        # We'll then create a dictionary of data from the POST data received.
        data = {
        'email': request.form['email'], 
        }
        mysql.query_db(query, data)
        flash('Email recorded')
        print session['email']
        return render_template('index2.html', email = request.form['email'])
    else:
        flash("Email must include '@' and '.com'")
        print "Email not recorded, starting over"
        return render_template('index.html')
    print email
    return redirect('/')

@app.route('/show_emails')
def show_emails():
    query = "SELECT * FROM emails"                           # define your query
    emails = mysql.query_db(query)                           # run query with query_db()
    print (emails)
    return render_template('show_emails.html', all_emails=emails) 

app.run(debug=True)


#FINISH WITH CORRECT FLASH AND ENSURE ALL ROUTES WORK
#GREAT JOB