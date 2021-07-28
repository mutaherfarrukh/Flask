from os import read
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', color1 = 'black', color2 = 'red' )  

@app.route('/4')
def hello_world2():
    return render_template('index2.html', color1 = 'whitesmoke', color2 = 'green' )

@app.route('/<int:times>/<int:mul>')
def index2(times, mul):
    return render_template('index3.html',  color1 = 'black', color2 = 'red', times = times, mul = mul)

if __name__=="__main__":
    app.run(debug=True)
