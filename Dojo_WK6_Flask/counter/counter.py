from flask import Flask, session, redirect, request, render_template
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def counter():
    try:
        session['counter'] += 1
    except: 
        session['counter'] = 0
        session['counter'] += 1  
    return render_template('counter.html' )

def index():
    print(app.secret_key)
    return render_template('counter.html')

app.run(debug=True)