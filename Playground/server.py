from os import P_OVERLAY
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<play>')
def index(play):
    return render_template('index.html', word = play)  

@app.route('/<string:play>/<int:times>')
def index2(play, times):
    print(play)
    return render_template('index2.html', play = play, times = times)


@app.route('/play/<int:x>/<string:color>')
def second(x, color):
    return render_template('index3.html', times = x, color = color)


if __name__=="__main__":
    app.run(debug=True)