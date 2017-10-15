from flask import Flask, request, session, redirect, render_template, flash
import os 
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key  = os.urandom(32)

@app.route('/')
def index():
    if 'count' not in session:
        session['views']=0
    else:
        session['views'] += 1
    return render_template('simple_registration.html')

@app.route('/user', methods=['POST'])
def user():
    session['email']= request.form['email']
    session['first_name']=request.form['first_name']
    session['last_name']=request.form['last_name']
    session['password']=request.form['password']
    session['confirm_password']=request.form['confirm_password']

    if len(request.form['email']) <1:
        flash('Email cannot be blank')
        return redirect('/')
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    if len(request.form['first_name']) <1:
        flash('First Name cannot be blank')
        return redirect('/')
    if len(request.form['last_name']) <1:
        flash('Last Name cannot be blank')
        return redirect('/')
    if len(request.form['password']) <8:
        flash('Password must be at least 8 characters')
        return redirect('/')
    if len(request.form['confirm_password']) <1:
        flash('Confrim Password cannot be blank')
        return redirect('/')
    if request.form['password'] != request.form['confirm_password']:
        flash('Password and Confirm Password must match')
        return redirect('/')

    print('Received form data')
    # return redirect('/success')
    return redirect('/show')

@app.route('/success')
def success():
    return 'SUCCESS!'

@app.route('/show')
def show():
    return render_template('show.html')

app.run(debug=True)