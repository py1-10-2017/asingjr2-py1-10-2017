from flask import Flask, session, redirect, render_template, request
import os 
import random

app = Flask(__name__)
app.secret_key = os.urandom(32)
@app.route('/')
def index():
    session['correct_num'] = random.randrange(0,4)
    # guess = request.form['guess']
    return render_template('number_game.html')

@app.route('/results', methods=["POST"])
def post():
    session['guess'] = request.form['guess']
    print('Got results',session['correct_num'])
    print ("User guess is: ", request.form['guess'])
    if session['correct_num'] == int(request.form['guess']):
        session['result'] = 'perfect'
    elif session['correct_num'] < int(request.form['guess']):
        session['result'] = 'high'        
    else:
        session['result'] = 'low'
        
    return redirect('/')

@app.route('/correct')
def corect():
    return 'correct!'

@app.route('/reset')
def reset():
    session.pop('guess')
    session.pop('result')
    return redirect('/')

app.run(debug=True)