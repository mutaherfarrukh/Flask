from os import kill
from flask import Flask , render_template, request, redirect, session

app=Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    print('start of homescreen')
    if 'count' not in session:
        session['count']=0
    else:
        session['count']+=1
    return render_template("index.html", count= session['count'])

@app.route('/addTwo')
def addtwo():
    session['count']+=1
    return redirect('/')

@app.route('/reset')
def reset():
    session['count']=0
    return render_template('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    print('session destroyed')
    return redirect('/')

app.run(debug=True)