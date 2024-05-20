from flask import Flask, render_template
import csv
import requests

app = Flask(__name__)
titol = 'ciao sito'


@app.route('/')  # route di default con slash
def hello_world():
    bottoni = {
        'b1': 'movies',
        'b2': 'music',
        'b3': 'book',
    }
    # per richiamare il diz in html si usa la sintassi 'bottoni.b1'
    return render_template("home_lab.html", titolo='Benvenuti nel nostro sito'.upper(), bottoni=bottoni)


@app.route('/data')  # route di default con slash
def data():
    return 'Ciao, data!'


@app.route('/movies')  # route di default con slash
def movies():
    return render_template('film.html')
#movies lavora lato server


@app.route('/book')
def book():
    return render_template('libri.html')


@app.route('/music')
def music():
    return render_template('musica.html')



if __name__ == '__main__':
    app.run(debug=True)