from flask import Flask, session, redirect, request, render_template, flash
import os 
from ff_connection import MySQLConnector

app = Flask(__name__)
app.secret_key = os.urandom(32)

mysql = MySQLConnector(app, 'full_friendsdb')

#basic read/view route
@app.route('/')
def index():
    query = 'SELECT * FROM friends'
    all_friends = mysql.query_db(query)
    # session['last_name'] = request.form['for_edit']
    print 'SQUARE ONE'
    return render_template('index.html', all_friends = all_friends) 
# l_name = session['last_name'])

#basic create route
@app.route("/add_record", methods=['POST'])
def add():
    query = "INSERT INTO friends (first_name, last_name, emails, created_at, updated_at) VALUES (:first_name, :last_name, :emails, NOW(), NOW())"
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'emails':request.form['emails'],
    }
    mysql.query_db(query,data)
    print "RECORD INSERTED"    
    return redirect('/')

#basic delete route
@app.route('/<last_name>/delete_records')
def delete_records(last_name):
    query = "DELETE FROM friends WHERE last_name = :last_name"
    data = {
        'last_name' : last_name
    }
    deleted_record = mysql.query_db(query,data) 
    #Will not show result since result is already gone once query is ran
    #Not sure how to handle renumbering or if thats necessary
    print 'RECORD DELETED'
    return redirect('/')



@app.route('/update_record', methods=['POST'])
def update_record():
    query = "UPDATE friends \
             SET first_name = :first_name, last_name = :last_name, emails = :emails \
             WHERE emails = :emails"
    data = {
             'first_name': request.form['first_name'], 
             'last_name':  'awesome',
             'emails': request.form['emails']
           }
    mysql.query_db(query, data) #Does not update db
    print 'RECORD UPDATED'
    return redirect('/')
    
@app.route('/<last_name>/edit_page')
def edit_page(last_name):
    show_query = "SELECT * FROM friends WHERE last_name = :last_name"
    show_data = {
        'last_name': last_name
    }
    changing_record = mysql.query_db(show_query,show_data)
    first = changing_record[0]['first_name']
    last = changing_record[0]['last_name']
    emails = changing_record[0]['emails']
    print "NEW RECORD FOR UPDATE"
    return render_template('edit.html',first = first, last = last, emails = emails)

app.run(debug=True)



    
