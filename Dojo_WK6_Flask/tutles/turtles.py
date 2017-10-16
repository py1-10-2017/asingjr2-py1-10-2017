from flask import Flask, session, redirect, render_template, request, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/result', methods=['POST'])
# def results():
#     color = request.form['color']
#     session['color']=request.form['color']
#     url = '/picture/' + request.form['color']
#     print 'Color chosen'
#     return redirect(url)

@app.route('/picture/<color>')
def picture(color):
    ninjas = {
        'orange':'michelangelo',
        'blue':'leonardo',
        'red':'raphael',
        'purple':'donatello',
        'yellow': 'splinter'
    }

    if color in ninjas:
        character = ninjas[color]
    elif color in ninjas.values():
        character = ninjas[color]
    else:
        character = 'notapril'
    return render_template('result.html', character=character)

    # print color
    # return render_template('index.html')


app.run(debug=True)

